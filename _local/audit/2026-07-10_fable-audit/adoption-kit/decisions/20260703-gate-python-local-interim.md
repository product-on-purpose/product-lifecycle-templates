# Ship the governance gate as a local Python script, as a decided interim

Status: accepted as interim (decided 2026-07-03; transcribed 2026-07-11; ratify on adoption; supersession condition below)
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
