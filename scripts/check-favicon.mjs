#!/usr/bin/env node
// what-it-is:   the guard on the favicon reference in every built page
// what-it-does: asserts every page in dist/ declares a favicon, that the declared file actually
//               exists in the build, and that the count of pages carrying one is non-zero
// why:          site-s0-spec AC-6 requires a favicon to resolve on every built page INCLUDING
//               404.html, and requires the guard to match the rel form Starlight actually emits
// used-by:      .github/workflows/site.yml, between `astro build` and `upload-pages-artifact`;
//               locally as `node scripts/check-favicon.mjs`
//
// THE REL FORM IS THE WHOLE POINT, and getting it wrong is the trap this guard was written for.
//
// Spec finding 4.3, observed in the 2026-09-18 spike and re-confirmed 2026-09-21 against a real
// build of 34 pages: for a configured PNG, Starlight emits
//
//     <link rel="shortcut icon" href="/product-lifecycle-templates/favicon.png" ...>
//
// and emits NO `rel="icon"` link at all. A guard matching only `rel="icon"` - which is the obvious
// thing to write, and what the modern HTML spec prefers - reports a false failure on every page of
// a site whose favicon is perfectly fine. So both forms are matched, and the reason is recorded
// here rather than left for the next person to rediscover from a red build.
//
// 404.html IS IN SCOPE and is the page most likely to lose its head tags, because it is generated
// by a different path from ordinary content pages. It is also the page a visitor is most likely to
// hit from a stale external link, which is exactly when a broken-looking site costs most.
//
// Usage:  node scripts/check-favicon.mjs [distDir]
// Exit:   0 = every page declares a favicon and the target exists
//         1 = a page has none, or the declared file is missing, or dist has no pages

import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

import { BASE } from './site-base.mjs';

// Both forms, deliberately. See the header.
const FAVICON_RE = /<link[^>]*\brel=["'](icon|shortcut icon)["'][^>]*\bhref=["']([^"']+)["']/gi;
// Starlight orders attributes href-then-rel in some emissions; match that shape too rather than
// assume one ordering, because attribute order is not part of any contract.
const FAVICON_RE_ALT = /<link[^>]*\bhref=["']([^"']+)["'][^>]*\brel=["'](icon|shortcut icon)["']/gi;

function walk(dir, acc = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, e.name);
    if (e.isDirectory()) walk(full, acc);
    else if (e.name.endsWith('.html')) acc.push(full);
  }
  return acc;
}

export function checkFavicon(distArg, base = BASE) {
  const DIST = path.resolve(distArg || 'site/dist');

  if (!fs.existsSync(DIST)) {
    console.error(`check-favicon: dist not found at ${DIST}; build the site first.`);
    return 1;
  }

  const pages = walk(DIST);
  // Symmetric with the other guards: an existing-but-empty dist must fail, not vacuously pass.
  if (pages.length === 0) {
    console.error(`check-favicon: ${DIST} exists but has no .html pages. A built site is never empty.`);
    return 1;
  }

  const noDeclaration = [];
  const missingTarget = new Map(); // href -> first page that referenced it
  const relForms = new Set();

  for (const file of pages) {
    const html = fs.readFileSync(file, 'utf8');
    const rel = path.relative(DIST, file).split(path.sep).join('/');

    const hrefs = [];
    for (const m of html.matchAll(FAVICON_RE)) {
      relForms.add(m[1].toLowerCase());
      hrefs.push(m[2]);
    }
    for (const m of html.matchAll(FAVICON_RE_ALT)) {
      relForms.add(m[2].toLowerCase());
      hrefs.push(m[1]);
    }

    if (hrefs.length === 0) {
      noDeclaration.push(rel);
      continue;
    }

    for (const href of hrefs) {
      if (/^(https?:|data:|\/\/)/i.test(href)) continue; // externally hosted: out of scope
      // Base-absolute (/product-lifecycle-templates/favicon.png) -> a file inside dist.
      let target = href.split('?')[0].split('#')[0];
      if (target.startsWith(base + '/')) target = target.slice((base + '/').length);
      else if (target.startsWith('/')) target = target.slice(1);
      else target = path.posix.join(path.posix.dirname(rel), target);

      if (!fs.existsSync(path.join(DIST, target)) && !missingTarget.has(href)) {
        missingTarget.set(href, rel);
      }
    }
  }

  console.log('=== Favicon Check ===');
  console.log(`Pages scanned: ${pages.length}`);
  console.log(`rel form(s) emitted: ${[...relForms].join(', ') || 'none'}`);

  if (noDeclaration.length === 0 && missingTarget.size === 0) {
    console.log(`\nPASS: all ${pages.length} page(s) declare a favicon and every target exists in the build.`);
    return 0;
  }

  if (noDeclaration.length) {
    console.error(`\nFAIL: ${noDeclaration.length} page(s) declare no favicon at all:`);
    for (const p of noDeclaration.slice(0, 20)) console.error(`  ${p}`);
    if (noDeclaration.length > 20) console.error(`  ... and ${noDeclaration.length - 20} more`);
    console.error('  404.html is generated by a different path from content pages and is the usual');
    console.error('  first casualty; it is also the page a stale external link lands on.');
  }

  if (missingTarget.size) {
    console.error(`\nFAIL: ${missingTarget.size} favicon target(s) referenced but absent from the build:`);
    for (const [href, page] of missingTarget) console.error(`  ${href}   (first seen in ${page})`);
    console.error('  Check site/public/ ships the file and that astro.config.mjs points at it.');
  }

  return 1;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  process.exit(checkFavicon(process.argv[2]));
}
