# Security policy

## What this repository is, and what that means for risk

This repository ships **markdown documents and small Python scripts**. It has no runtime, no server, no
network listener, and no dependency tree beyond two packages used by CI (`pyyaml` and `jsonschema`).
Nothing here executes on a user's machine unless they choose to run a script in `tools/`.

The realistic risks are therefore narrow, and worth naming precisely rather than covering with a generic
policy:

- **A malicious link in a template or research log.** Every relative link is gated by CI, but external URLs
  in research logs point wherever the source lived. Treat them as you would any link in a document.
- **A script in `tools/` doing more than it says.** All are short and stdlib-only except where noted, and
  read-only apart from the generators (`gen-manifest.py`, `gen-atlas.py`, `gen-research-log.py`). Read
  before running.
- **A supply-chain issue in the two CI dependencies**, which affects CI rather than users.

## Reporting

Open a **private security advisory** through GitHub on this repository, or a normal issue if the finding is
not sensitive. There is no separate security contact and no bug bounty.

**Expected response:** this is a single-maintainer project. A realistic acknowledgement window is days, not
hours. If that is not fast enough for your situation, say so in the report and treat the finding as public.

## What is not a security issue here

- A factual error in a template, companion, or research log. Those are correctness issues and belong in a
  normal issue. They are taken seriously; `CONTRIBUTING.md` explains how.
- A template producing a document that discloses something it should not. The templates prompt for content;
  what a filled document contains is the author's call. Several bundles warn about this explicitly.
