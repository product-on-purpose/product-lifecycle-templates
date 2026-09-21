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

**These are two workflows, deliberately, and only `ci.yml` is a required check** (AC-18). The
content gate protects the template library; the site is downstream of it. Until the site has
proven itself, a site failure must not be able to block a template change.
