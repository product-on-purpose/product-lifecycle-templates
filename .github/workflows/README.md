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

- [`ci.yml`](ci.yml) - the single workflow, running the bundle gate, the tool self-tests, the link
  gate, freshness checks on every generated artifact, and a repo-wide dash sweep over tracked files
