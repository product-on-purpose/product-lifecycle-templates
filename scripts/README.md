---
title: "Site build scripts"
---

# `scripts/` - the Node side of the toolchain

Everything in this folder is **dependency-free Node ESM (`.mjs`)** and exists to build or guard the
Astro site. Nothing here touches the template library itself.

## Why this folder exists at all, next to `tools/`

Every generator and every gate step in this repository is Python, and lives in
[`tools/`](../tools/). The family Astro site standard's clause 14.3 states outright that new
**Python site generators MUST NOT be introduced**, so the site's generator cannot live there. The
split is therefore a rule rather than a preference:

| | `tools/` | `scripts/` |
|---|---|---|
| Language | Python | Node ESM `.mjs` |
| Scope | the template library, the gate, the catalog | the Astro site only |
| Run by | `tools/run-gate.py`, CI | `npm run` inside `site/`, and `site.yml` |

Adopted in [ADR 0046 (the site is Astro Starlight under Pattern S)](../docs/internal/decisions/0046-the-site-is-astro-starlight-under-pattern-s.md);
the slice is specified in [`site-s0-spec.md`](../docs/internal/site-s0-spec.md).

## Inventory

- [`gen-site.mjs`](gen-site.mjs) - the site content generator. Reads `manifest.json`,
  `sections.json`, `atlas/catalog-data.json` and `templates/`, and writes one Starlight page per
  bundle plus an index into `site/src/content/docs/bundles/`. It needs no YAML parser because the
  Python tooling has already distilled every `*_meta.yaml` into `manifest.json`. It also carries
  `--check`, the honesty gate over its own output (AC-16): the build fails if a page calls a
  bundle proven, verified or validated, or puts a percentage beside a claim about a bundle
- [`site-base.mjs`](site-base.mjs) - the **only** place the published base path is written.
  `site/astro.config.mjs` imports it rather than restating it, as do the generator and the link
  checker, so there is no second copy to drift (clause 14.7, AC-5)
- [`check-rendered-links.mjs`](check-rendered-links.mjs) - resolves every internal link against
  the page's real published URL and asserts the target exists in `dist/`. A filesystem-correct
  relative link can still 404, because pages build to `slug/index.html` and are served one level
  deeper than their source
- [`check-route-parity.mjs`](check-route-parity.mjs) - compares the built routes against the
  committed baseline in [`route-manifest.txt`](route-manifest.txt) and fails if a published URL
  has disappeared. New routes are allowed; `--update` rewrites the baseline
- [`route-manifest.txt`](route-manifest.txt) - the committed record of every URL this site has
  published. Snapshotted from a finished build, never generated from source: the thing it guards
  is a promise the source no longer contains once a route is removed
- [`check-favicon.mjs`](check-favicon.mjs) - asserts every built page declares a favicon and that
  the declared file exists in the build, `404.html` included. Matches `rel="shortcut icon"` as
  well as `rel="icon"`, because Starlight emits only the former for a configured PNG and the
  obvious guard reports a false failure on a healthy site
- [`verify-edit-links.mjs`](verify-edit-links.mjs) - asserts every "Edit this page" target is
  **git-tracked**, not merely present on disk, and that the link count stays above a floor. The
  donor checks existence, which cannot fail the one mutation it exists to catch

All five guards run inside [`site.yml`](../.github/workflows/site.yml) **between `astro build` and
`upload-pages-artifact`**, so the artifact that is guarded is the artifact that ships. The
reference implementation does not do this: it guards a separate build in a workflow that races the
deploy, so a guard failure there does not stop a deploy.

**Every guard has been run against a deliberately broken fixture and observed to fail** (AC-12,
AC-6): a broken link, a removed route, a stripped `editUrl`, a deleted favicon, a favicon link
stripped from `404.html`, and an empty-but-existing `dist`. A guard that
has never gone red is a report, not a gate.

## Conventions anything added here must follow

- **Zero dependencies.** No `package.json` in this folder and no imports outside `node:*`.
- **A docblock header** carrying `what-it-is`, `what-it-does`, `why` and `used-by`, per the family
  standard's G9. The conformance gate fails without it.
- **The base path is never redeclared.** [`site-base.mjs`](site-base.mjs) holds the only literal;
  `site/astro.config.mjs`, the generator and the link checker all **import** it (clause 14.7,
  AC-5). A wrong base passes every local check and 404s on the live site, so the arrangement that
  removes the failure is having nothing to disagree with.
- **Only the generated subpath is written.** `site/src/content/docs/bundles/` is the single
  gitignored generated directory. Hand-authored narrative pages live one level up in
  `site/src/content/docs/` and are **tracked**; nothing here may remove or rewrite them.
- **LF, explicitly.** Write `\n` and never rely on the platform default. A whole-file CRLF rewrite
  is invisible to every diff-based check on this machine and has cost this repository real time.

## Running them

```bash
cd site
npm run gen            # regenerate the bundle pages
npm run check:honesty  # scan the generated pages (AC-16)
npm run build          # prebuild runs gen automatically, then astro build
```

`npm run build` is wired so a clean checkout plus `npm ci && npm run build` produces the whole
site, which is what AC-3 requires of the generated-content model.
