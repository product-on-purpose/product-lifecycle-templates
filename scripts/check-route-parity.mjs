#!/usr/bin/env node
// what-it-is:   the guard against silently removing a published URL
// what-it-does: compares every *.html in the built dist/ against a committed baseline and fails
//               if a baseline route has disappeared; added routes are allowed
// why:          a removed or renamed URL is a "Site not found" for every existing link and
//               bookmark, and nothing else in the build notices (site-s0-spec AC-12)
// used-by:      .github/workflows/site.yml, between `astro build` and `upload-pages-artifact`;
//               locally as `node scripts/check-route-parity.mjs`
//
// Ported from pm-skills/scripts/check-route-parity.mjs. The logic is the donor's; what changed is
// where it runs. See the note on placement at the bottom of this header.
//
// WHY A COMMITTED BASELINE AND NOT A GENERATED ONE. The route set cannot be derived from the
// source tree, because the thing being guarded is a promise about URLs that the source no longer
// contains. A removed bundle leaves no trace in manifest.json; only a snapshot taken when the
// route existed can notice it is gone. So scripts/route-manifest.txt is generated from a finished
// build, committed, and treated as a record of what this site has promised the outside world.
// gen-site.mjs deliberately does NOT emit it: a generator writing its own baseline would be
// grading its own homework.
//
// SCOPE, deliberately. This checks route PRESENCE, not page CONTENT. A route that keeps its path
// while its page regresses to empty still passes here. That is the same mechanism that lets an
// intentional redirect pass, and it is why site.yml also asserts the artifact is non-empty.
//
// WHEN YOU INTENTIONALLY REMOVE A ROUTE: add a redirect for it (Astro renders the redirect source
// as a real page, so the route stays present and this check still passes), OR run --update and
// commit the new baseline in the same commit, with a reason.
//
// Usage:  node scripts/check-route-parity.mjs [distDir] [baselineFile]
//         node scripts/check-route-parity.mjs --update     rewrite the baseline from this build
// Exit:   0 = every baseline route still present; 1 = one or more removed.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const argv = process.argv.slice(2).filter((a) => a !== '--update');
const UPDATE = process.argv.includes('--update');
const DIST = path.resolve(argv[0] || path.join(ROOT, 'site', 'dist'));
const BASELINE = path.resolve(argv[1] || path.join(ROOT, 'scripts', 'route-manifest.txt'));

function routesIn(dir) {
  const out = [];
  const walk = (d) => {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const full = path.join(d, e.name);
      if (e.isDirectory()) walk(full);
      else if (e.name.endsWith('.html')) out.push('/' + path.relative(dir, full).split(path.sep).join('/'));
    }
  };
  walk(dir);
  return out.sort();
}

if (!fs.existsSync(DIST)) {
  console.error(`route-parity: dist not found at ${DIST}; build the site first (cd site && npm run build).`);
  process.exit(1);
}

const current = routesIn(DIST);

// An empty dist that EXISTS is the case a naive guard passes: the walk returns nothing, every
// comparison is vacuous, and the check reports success over a site that would deploy blank.
if (current.length === 0) {
  console.error(`route-parity: FAIL, ${DIST} exists but contains no .html files. A build that produced no pages is not a build.`);
  process.exit(1);
}

if (UPDATE) {
  fs.writeFileSync(BASELINE, current.join('\n') + '\n', 'utf8');
  console.log(`route-parity: wrote ${current.length} routes to ${path.relative(ROOT, BASELINE)}`);
  process.exit(0);
}

if (!fs.existsSync(BASELINE)) {
  console.error(`route-parity: baseline not found at ${BASELINE}. Generate it with: node scripts/check-route-parity.mjs --update`);
  process.exit(1);
}

const baseline = fs.readFileSync(BASELINE, 'utf8').split(/\r?\n/).map((s) => s.trim()).filter(Boolean);
const currentSet = new Set(current);
const baselineSet = new Set(baseline);
const removed = baseline.filter((r) => !currentSet.has(r));
const added = current.filter((r) => !baselineSet.has(r));

console.log('=== Route Parity Check ===');
console.log(`baseline routes: ${baseline.length}   current routes: ${current.length}`);
if (added.length) {
  console.log(`\n${added.length} new route(s) (allowed; update the baseline when convenient):`);
  for (const r of added.slice(0, 20)) console.log(`  + ${r}`);
  if (added.length > 20) console.log(`  ... and ${added.length - 20} more`);
}

if (removed.length === 0) {
  console.log('\nPASS: every baseline route is still present in the build.');
  process.exit(0);
}

console.log(`\nFAIL: ${removed.length} baseline route(s) removed (these would 404 for existing links and bookmarks):`);
for (const r of removed) console.log(`  - ${r}`);
console.log('\nIf intentional: add a redirect (keeps the route present as a redirect page),');
console.log('or run `node scripts/check-route-parity.mjs --update` and commit the new baseline with a reason.');
process.exit(1);
