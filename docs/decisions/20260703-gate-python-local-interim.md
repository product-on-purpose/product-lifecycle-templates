# Ship the governance gate as a local Python script, as a decided interim

Status: accepted as interim (decided 2026-07-03; transcribed 2026-07-11; ratified 2026-07-12; supersession condition below)
Date: 2026-07-03
Deciders: jprisant

## Context and problem statement

The implementation plan's P3 committed to a suite of Node `.mjs` lint scripts under `scripts/` wired to GitHub Actions on push. When the four bundles were built ahead of that phase, the Definition of Done was being verified by hand. A single local Python script (`_local/tools/check-bundles.py`, six checks) was built 2026-07-03 to make that verification repeatable, explicitly self-described in its docstring and in the README as "a local prototype of the CI gate planned in the implementation plan (P3)."

## Considered options

* Option A: one local Python script now; CI wiring and the fuller check suite later.
* Option B: execute P3 as planned (Node script suite plus ci.yml) before or alongside content.
* Option C: no automation until P3 runs properly.

## Decision outcome

Chosen option: A. It converted hand-verification into one repeatable command on the day it was needed, at a fraction of P3's cost, and its docstring records its interim status honestly.

### Consequences

* Good: six structural DoD checks became enforceable immediately; the gate caught real issues during authoring.
* Accepted risk: local-only means zero push protection (every merge to main relies on one person remembering to run it), and the six checks cover roughly half the DoD; both were flagged by the 2026-07-10 audit (findings D-01 gate coverage and D-03 CI absence).
* Supersession condition: this decision is superseded in two steps. Step 1 (immediate, roadmap WP-02): a ci.yml that runs this same Python script on push, making the gate enforcing without rewriting it. Step 2 (open): whether the Node port ever happens is a fresh decision to take when the gate next grows substantially; Python-in-CI may simply be the permanent answer, in which case update the plan's P3 text rather than carrying a phantom migration forever.

## Follow-up

**2026-07-12: Step 1 is satisfied.** `.github/workflows/ci.yml` now runs this same script on every push to `main` and on every pull request (roadmap WP-02, closing audit finding D-03). The "zero push protection" risk recorded above is therefore historical rather than current: the gate is enforcing, and it no longer depends on one person remembering to run it.

Two things this does **not** close. Finding D-01 (the six checks automate roughly half the Definition of Done) is untouched; gate hardening is roadmap WP-11 in milestone M1. And Step 2 stays open by design: whether the Node port ever happens remains a fresh decision for whenever the gate next grows substantially. Python-in-CI may simply be the permanent answer, and if it is, the honest move is to update the implementation plan's P3 text (port the CI quality gate from pm-skills) rather than carry a phantom migration forever.
