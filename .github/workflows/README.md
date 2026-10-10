---
title: "CI workflows"
---

# CI workflows

Every check this repository enforces runs from here. The workflow **invokes scripts and contains no
check logic of its own**, so any check can be reproduced locally by running the same command; that
separation is what makes a red build debuggable without pushing.

What the steps prove, and the boundary they cannot cross, is written up in
[`review-standards.md`](../../docs/internal/review-standards.md). The short version: the gate proves
form, and no step in this file can prove that a claim is true.

## Inventory

- [`ci.yml`](ci.yml) - the content gate, running the bundle gate, the tool self-tests, the link
  gate, freshness checks on every generated artifact, and a repo-wide dash sweep over tracked files
- [`site.yml`](site.yml) - builds the Astro Starlight site, guards the artifact, and deploys it to
  GitHub Pages. **Its four guards run between `astro build` and `upload-pages-artifact`**, against
  the very directory about to be uploaded, so a guard failure means nothing is deployed. The
  reference implementation instead guards a separate build in a workflow that races its deploy,
  which meets the letter of nothing; clause 14.11 requires the deployed artifact to be checked

**These are two workflows, deliberately** (AC-18). The content gate protects the template library,
and the site is downstream of it, so the site's build and deploy logic stays out of `ci.yml`.

**Both are required checks on `main` since 2026-10-08:** `gate` from `ci.yml` and `build` from
`site.yml`, by the maintainer's decision. Until then this section said only `ci.yml` was required,
so that a site failure could not block a template change. `site.yml` has no path filter on
`pull_request`, so every PR now runs `build`, and a site failure blocks a template-only change too.
`tools/run-gate.py` runs only `ci.yml`'s steps, so a green local gate says nothing about the site;
`npm run build` in `site/` is the local equivalent of the build step.
