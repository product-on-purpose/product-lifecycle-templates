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

Three guards (`check-rendered-links.mjs`, `check-route-parity.mjs`, `verify-edit-links.mjs`) land
in S0 PR 3 and will run inside `site.yml` between `astro build` and `upload-pages-artifact`, so the
artifact that is guarded is the artifact that ships.

## Conventions anything added here must follow

- **Zero dependencies.** No `package.json` in this folder and no imports outside `node:*`.
- **A docblock header** carrying `what-it-is`, `what-it-does`, `why` and `used-by`, per the family
  standard's G9. The conformance gate fails without it.
- **The base path is never redeclared.** `site/astro.config.mjs` owns `site` and `base` (clause
  14.7). `gen-site.mjs` holds the one constant it needs to emit links and **asserts it against the
  config at startup**, so the two cannot silently disagree; a wrong base passes every local check
  and 404s on the live site.
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
