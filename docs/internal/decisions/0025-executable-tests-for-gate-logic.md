---
status: accepted
date: 2026-07-23
decision-makers: [jprisant]
consulted: [claude]
---

# Executable tests complement the structural gate; they live in `tools/`, run in CI, and block merge

## Context and Problem Statement

Until 2026-07-22 this repo had **no automated tests**, only the structural gate (`check-bundles.py` and
the link, manifest, and dash checks). That was defensible while the gate only inspected bundles: every gate
check has a live subject (twelve real bundles), so running the gate is itself the test - a broken check
fails against real data on the next run.

Two changes broke that assumption. The check-K classification-axis work
([ADR 0023](0023-resolve-the-tier-1-family-taxonomy.md)) added a branch with **no live subject**: no
classification-axis family existed until governance-docs landed, so running the gate could not exercise the
new code, and could not have caught it failing. A check that has never been observed failing is an
assumption, not a check. `tools/test-check-k.py` was written to close that gap (it fixture-tests the axis
logic, including that it FAILS on a wrong value, a wrong axis, and a misconfigured registry), landed with
the change, and was mutation-checked. That made it the repo's first test file - a new pattern that was
introduced without a decision record, which this ADR now supplies.

The question is narrow and worth settling once: **when does gate logic earn an executable test, where do
tests live, and are they blocking?** Left unsettled, the next gate change either gets no test (repeating the
untested-branch risk) or gets one placed and run ad hoc.

## Decision Drivers

- **Coverage without a live subject.** Gate logic that cannot be exercised by the real bundles on disk has
  no other way to be verified than a fixture test.
- **A check must be observed failing.** The value of a check is that it fails when it should; that property
  has to be demonstrated, not assumed, which means negative-case tests and, for the load-bearing ones,
  mutation checks.
- **Minimal machinery.** The repo's gate is pure-stdlib by preference (ADR 0008); a test harness should not
  drag in a framework or a new CI toolchain.
- **Do not over-test.** Most of the Definition of Done is structural and is already exercised by the real
  bundles; adding tests there would duplicate the gate without adding signal.

## Considered Options

- **Option A: adopt lightweight, stdlib, in-`tools/` executable tests for gate logic that lacks a live
  subject, run in CI as their own step, blocking merge.** Chosen.
- **Option B: no executable tests; rely on the gate against real bundles only.** Rejected: it cannot cover a
  branch with no live subject, which is exactly where a silent bug hid.
- **Option C: introduce a test framework (pytest) and a `tests/` tree.** Rejected as disproportionate: it
  adds a dependency and a second toolchain for what is, today, one file; ADR 0008 keeps the gate stdlib for
  the same reason. Revisit if the test surface grows past a handful of files.

## Decision Outcome

**Adopt Option A.** The convention, stated so it can be applied without re-deriving it:

1. **When.** Gate logic (or any tool logic) that **cannot be exercised by the real artifacts on disk** earns
   an executable test. Logic that the real bundles already exercise does not; the gate is its test.
2. **What the test must do.** Cover the positive case AND the negative cases (the check failing when it
   should), asserting on the failure message where the message is the deliverable. For load-bearing logic,
   **mutation-check** the test (deliberately break the code, confirm the test catches it) so the test is
   known to fail when the code is wrong, not merely known to pass.
3. **Where.** Tests live in `tools/`, named `test-<subject>.py`, pure standard library, no framework, no
   new dependency (matching ADR 0008's stdlib preference for the gate).
4. **Blocking.** Each test runs as its own step in `.github/workflows/ci.yml`, after the gate, and a failure
   blocks merge, exactly like the gate and the link, manifest, and dash checks.

`tools/test-check-k.py` is the reference instance and already conforms (49 assertions across both axes and
set-valued axes, mutation-checked, run in CI).

### Consequences

* Good: gate branches with no live subject can be verified, and their checks can be observed failing, which
  is what makes them checks rather than hopes.
* Good: the pattern is uniform - a future contributor knows a gate change of this kind ships with a
  `tools/test-*.py`, in CI, blocking.
* Good: no new dependency or test framework; the harness is stdlib, consistent with ADR 0008.
* Neutral: the test surface is deliberately small (one file today). Most of the Definition of Done stays
  covered by the real bundles, not by tests.
* Accepted cost: if the test surface grows past a handful of files, Option C (a framework and a `tests/`
  tree) may become worth revisiting; this ADR would then be superseded rather than corrected.

### Confirmation

Enforced by the `Check K self-test` step (and any future `test-*.py` steps) in `.github/workflows/ci.yml`,
with branch protection on `main` requiring the gate job. The reference test, `tools/test-check-k.py`, is
mutation-checked: breaking `check_family` two ways during development each failed the expected assertions.

## More Information

This ADR is a sibling of the "generated, committed, gate-checked" pattern
([ADR 0018](0018-machine-catalog-generated-manifest.md)), which keeps *derived data* honest; this one keeps
*logic* honest. The same session that prompted it also added two more instances of the generate-and-check
discipline for derived artifacts - `tools/gen-atlas.py` (the atlas `built` flags) and
`tools/check-adr-index.py` (the decision-record index) - both under ADR 0018's existing rationale rather
than needing their own records.
