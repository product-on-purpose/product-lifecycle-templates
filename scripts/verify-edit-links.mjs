#!/usr/bin/env node
// what-it-is:   the guard on every "Edit this page" link in the built site
// what-it-does: extracts each editLink href from dist/, normalises it to a repo-relative path,
//               and asserts the target is a GIT-TRACKED file; also enforces a minimum occurrence
//               count so that editLink emission breaking entirely fails instead of passing on 0/0
// why:          a generated page's edit link must point at its real editable source, and the
//               naive existence check cannot tell a tracked file from a generated one
//               (site-s0-spec AC-4, amended 2026-09-20; AC-12)
// used-by:      .github/workflows/site.yml, between `astro build` and `upload-pages-artifact`;
//               locally as `node scripts/verify-edit-links.mjs`
//
// Ported from pm-skills/scripts/verify-edit-links.mjs WITH ONE DELIBERATE CHANGE, and the change
// is the whole reason this file is not a copy.
//
// THE DONOR'S CHECK CANNOT FAIL THE MUTATION IT EXISTS TO CATCH.
//
// The donor validates each target with existsSync, a filesystem check. Now trace the mutation
// AC-4 requires: strip the editUrl stamp from a generated bundle page. Starlight falls back to
// deriving the URL from the entry's own filePath, which is
// site/src/content/docs/bundles/<id>.mdx. That file IS on disk - gen-site.mjs just wrote it, in
// CI exactly as locally - so existsSync returns true and the guard PASSES. But that path is
// gitignored under AC-3, so the link 404s on GitHub for every real visitor.
//
// A guard that passes on the exact defect it was written for is DF-7's shape: a check that
// returns something rather than the right thing. So this port asks git, not the filesystem:
// a target must appear in `git ls-files`. A generated page's fallback URL is then caught,
// because a gitignored file is not tracked.
//
// THE MINIMUM COUNT, kept from the donor and worth keeping. Without it the script passes on 0/0:
// if editLink emission breaks completely (a baseUrl typo, a loader change, a Starlight upgrade),
// there are no links to validate, every assertion is vacuous, and the check reports success over
// a site with no edit links at all. The floor turns that silence into a failure.
//
// Usage:  node scripts/verify-edit-links.mjs [distDir] [repoRoot]
// Exit:   0 = every target tracked and the count is above the floor
//         1 = a target is missing or untracked, or the count fell below the floor
//         2 = dist/ does not exist

import { execFileSync } from 'node:child_process';
import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { join, relative, resolve } from 'node:path';

const EDIT_BASE_URL = 'https://github.com/product-on-purpose/product-lifecycle-templates/edit/main/';

// 30 bundle pages, each emitting at least one edit link, plus the hand-authored pages. Set well
// below the real figure so ordinary content movement does not trip it, and far above zero so a
// total emission failure does. Tune via MIN_EDIT_LINKS only for deliberate content shrinkage.
const MIN_EDIT_LINKS = Number.parseInt(process.env.MIN_EDIT_LINKS ?? '25', 10);

const distDir = resolve(process.argv[2] ?? 'site/dist');
const repoRoot = resolve(process.argv[3] ?? '.');

function* walk(dir) {
  for (const name of readdirSync(dir)) {
    const full = join(dir, name);
    const stat = statSync(full);
    if (stat.isDirectory()) yield* walk(full);
    else if (stat.isFile()) yield full;
  }
}

const escapeForRegex = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

/** Every path git tracks, as forward-slash repo-relative strings. The oracle for "is this real". */
function trackedFiles(root) {
  const out = execFileSync('git', ['-C', root, 'ls-files', '-z'], {
    encoding: 'utf8',
    maxBuffer: 64 * 1024 * 1024,
  });
  return new Set(out.split('\0').filter(Boolean));
}

if (!existsSync(distDir)) {
  console.error(`ERROR: dist directory does not exist: ${distDir}`);
  console.error("       Run 'npm run build' first.");
  process.exit(2);
}

let tracked;
try {
  tracked = trackedFiles(repoRoot);
} catch (err) {
  console.error(`ERROR: could not list git-tracked files in ${repoRoot}: ${err.message}`);
  console.error('       This guard asserts targets are TRACKED, not merely present, so it cannot');
  console.error('       fall back to a filesystem check without becoming the thing it replaced.');
  process.exit(2);
}

const HREF_RE = new RegExp(`href=["']${escapeForRegex(EDIT_BASE_URL)}([^"'#?]+)`, 'g');

let totalLinks = 0;
const untracked = [];
const missing = [];
const checkedTargets = new Set();

for (const file of walk(distDir)) {
  if (!file.endsWith('.html')) continue;
  const html = readFileSync(file, 'utf-8');
  for (const match of html.matchAll(HREF_RE)) {
    totalLinks++;
    const repoRelPath = decodeURIComponent(match[1]);
    if (checkedTargets.has(repoRelPath)) continue;
    checkedTargets.add(repoRelPath);

    const onDisk = existsSync(join(repoRoot, repoRelPath));
    if (!tracked.has(repoRelPath)) {
      // Split the two cases: "does not exist" and "exists but is generated" are different bugs
      // and the second is the one the donor could not see.
      (onDisk ? untracked : missing).push({ firstSeenIn: relative(repoRoot, file), target: repoRelPath });
    }
  }
}

if (missing.length || untracked.length) {
  console.error(
    `FAIL: ${missing.length + untracked.length} unique editLink target(s) do not resolve ` +
      `(across ${totalLinks} occurrences, ${checkedTargets.size} unique targets)`
  );
  for (const f of missing.slice(0, 20)) {
    console.error(`  MISSING   ${f.target}`);
    console.error(`    first seen in: ${f.firstSeenIn}`);
  }
  for (const f of untracked.slice(0, 20)) {
    console.error(`  UNTRACKED ${f.target}`);
    console.error(`    first seen in: ${f.firstSeenIn}`);
    console.error('    This file exists locally but git does not track it, so the link 404s on');
    console.error('    GitHub. The usual cause is a page whose editUrl stamp was lost, letting');
    console.error('    Starlight fall back to the generated, gitignored content path.');
  }
  process.exit(1);
}

if (totalLinks < MIN_EDIT_LINKS) {
  console.error(
    `FAIL: editLink occurrence count (${totalLinks}) is below the minimum threshold ` +
      `(${MIN_EDIT_LINKS}). This usually signals that editLink emission silently broke: Starlight ` +
      'config drift, a baseUrl typo, or a loader change. A guard that passed here would be ' +
      'reporting success over a site with no edit links at all.'
  );
  console.error('  Investigate site/astro.config.mjs editLink config and src/content.config.ts.');
  console.error('  Tip: tune MIN_EDIT_LINKS only if intentional content shrinkage caused this.');
  process.exit(1);
}

console.log(
  `PASS: ${totalLinks} editLink occurrences across ${checkedTargets.size} unique targets, ` +
    `all git-tracked, above the floor of ${MIN_EDIT_LINKS}.`
);
