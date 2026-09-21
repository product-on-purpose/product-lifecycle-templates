// what-it-is:   the single source of truth for the published base path
// what-it-does: exports BASE, the GitHub Pages project subpath every consumer derives links from
// why:          clause 14.7 and AC-5 require the base to be declared ONCE; a base that disagrees
//               between the build and a validator passes every local check and 404s on the live site
// used-by:      site/astro.config.mjs, scripts/gen-site.mjs, scripts/check-rendered-links.mjs

// The site is served at https://product-on-purpose.github.io/product-lifecycle-templates, so the
// project subpath is `/product-lifecycle-templates`. Settled by
// ADR 0052 (docs/internal/decisions/0052-the-site-is-a-standalone-property-at-the-github-io-path.md).
//
// THIS IS THE ONLY PLACE THE LITERAL LIVES. `astro.config.mjs` imports it rather than restating
// it, which is what makes AC-5 checkable rather than aspirational: there is no second copy to
// drift. An earlier draft of gen-site.mjs kept its own copy and asserted the two matched at
// startup; that assertion is gone, because one literal cannot disagree with itself.
//
// When the shared @product-on-purpose/astro-docs-preset lands, `base` moves into the preset call
// and this module retires. It does not exist yet (re-verified 2026-09-18).
export const BASE = '/product-lifecycle-templates';

// The full origin, for the few places that need an absolute URL (sitemap, robots.txt).
export const SITE = 'https://product-on-purpose.github.io';
