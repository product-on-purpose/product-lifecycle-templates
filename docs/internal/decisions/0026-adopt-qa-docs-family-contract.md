---
status: accepted
date: 2026-07-25
decision-makers: [jprisant]
consulted: [claude]
---

# Adopt the qa-docs family contract (test-plan, test-case, bug-report) at phase develop, resolving the "QA may be utility" flag

## Context and Problem Statement

The Tier-1 floor build-out ([ADR 0021](0021-complete-the-tier-1-floor.md)) turns next to `qa-docs`, the family of verification artifacts: a test plan, a test case, and a bug report. Every new family gets a ratified contract before its members are built ([ADR 0020](0020-adopt-delivery-docs-family-contract.md) pattern), so a member is born into an enforced family rather than joining an honor system.

[`buildout-specs.md`](../buildout-specs.md) penciled this family in as `phase: develop` but flagged it *TBD (QA may be utility)*, and that flag is the decision this record exists to close. [ADR 0023](0023-resolve-the-tier-1-family-taxonomy.md) established the governing rule: a family must be coherent on exactly **one** axis, because its contract can gate only one. It also established where the call gets made, which is here, at contract time, against the family's actual members rather than in advance against a name.

Two further questions arrive with this family, neither of which the three previous contracts had to answer.

**Can two families share a phase value?** `decision-docs` is already `phase: develop`. If phase coherence implied phase ownership, `qa-docs` could not use `develop` and the axis call would be forced by bookkeeping rather than by what the documents are.

**Can a family's shared-scenario rule reach across a family boundary?** `delivery-docs` and `governance-docs` each chain their examples on one scenario of their own. The sharpest confusion `qa-docs` has to resolve, acceptance criteria versus test cases, sits exactly on the seam between this family and `delivery-docs`, and cannot be demonstrated from inside `qa-docs` alone.

## Decision Drivers

- **The axis call must be honest, not convenient.** It is decided by what a test plan, a test case, and a bug report are, not by what keeps the family map tidy.
- **Contract-first, so membership is mechanical from the first member.** A family whose members are built before its contract exists risks a member drifting to the wrong axis or value with nothing to catch it.
- **Do not re-learn the ADR 0020 lesson.** Methodology is descriptive, not a membership rule; the contract is written that way from the start.
- **The check should generalize, not grow machinery.** A fourth family should be one `FAMILY_CONTRACTS` entry, no new check code.
- **The family's teaching value is a boundary, so the contract has to protect the boundary.** A qa-docs family that does not force each member to place itself against acceptance criteria has skipped the main reason a reader needs it.

## Considered Options

- **Option A: adopt a qa-docs contract now at `phase: develop`, methodology descriptive, examples chained onto the existing delivery-docs scenario, enforced by check K via a registry entry.** Chosen.
- **Option B: make qa-docs a `classification: utility` family**, on the reading that QA is a standing, continuously-maintained function rather than a phase output. Rejected, and the reasoning matters because the surface appeal is real: a regression suite genuinely is maintained for years, and a defect backlog genuinely is continuous. But the standing thing in both cases is a **collection** (the suite, the backlog), and this library templates **documents**, not collections. `governance-docs` earned `classification` because each of its members *is itself* the standing instrument: a risk register is the maintained artifact, updated in place forever. A test case is not maintained in place forever; it is written once for one behavior and then executed repeatedly, which is a different thing. Applying the governance-docs test to these three members fails for all three.
- **Option C: split the family**, keeping `test-plan` as a phase artifact and moving `test-case` and `bug-report` elsewhere. Rejected: it manufactures one-member families to solve a coherence problem that does not exist. All three share a stage in the catalog (`testing/QA`, entries 102, 104, 107) and a job (verifying an increment), which is a stronger coherence signal than any of the previous three families started with.
- **Option D: no new family; fold the three types into `decision-docs`** (also `phase: develop`) or `delivery-docs`. Rejected: `decision-docs`' membership rule is "proposes, records, or describes a technical decision or design", and a test plan does none of the three; `delivery-docs` is `phase: deliver`. Folding would require widening a membership rule until it stopped constraining anything, which is the failure mode contracts exist to prevent.

## Decision Outcome

**Adopt [docs/internal/contracts/qa-docs.md](../contracts/qa-docs.md) (version 0.1.0), enforced by the existing gate check K via a new `FAMILY_CONTRACTS` entry keyed on `phase`.** For every bundle declaring `family: qa-docs`, check K requires `phase: develop`, a `beta` or `stable` `status`, a size shape of `[lean, full]` or `[lean]`, and that the contract file resolves. Methodology is descriptive and is not gated, carrying the ADR 0020 lesson forward.

**qa-docs is `phase: develop`.** The `classification` axis describes a document set up once and maintained indefinitely; none of these three is. Each is authored at a stage and finished: a test plan closes at its exit criteria, a test case is written once for one behavior, a bug report is opened and closed. The catalog independently agrees, giving all three the same `stage` value (`testing/QA`). The "QA may be utility" flag is closed as **no**.

**Being an instance artifact does not imply a classification.** This objection was already answered by `decision-docs`, where an ADR is one-per-decision, event-driven, read for years, and nonetheless `phase: develop`. The axis records where a type is authored in the lifecycle, not how long its instances are read afterward. Recording this explicitly because the same question will arrive again at `process-docs` and `discovery-docs`.

**Two families may share a phase value, and this is the first case.** `phase` and `family` are separate fields; check K gates per declared family; the two membership rules do not overlap. Phase coherence constrains a family internally and never claims a phase for one family. Had this not been settled, the axis call would have been decided by bookkeeping rather than by the artifacts.

**The shared-scenario rule reaches across the family boundary.** `qa-docs` examples chain onto the existing Acme Analytics "Saved Views for Dashboards" thread from `delivery-docs` rather than onto a new scenario, so that the acceptance-criteria-versus-test-case boundary is taught by showing the real acceptance criteria beside the real test cases derived from them, and then the test cases no acceptance criterion called for. This is the first cross-family example chain in the library; previous families chained internally or (in `decision-docs`) deliberately not at all.

**Each member must place itself against acceptance criteria**, not only against its two siblings, in its companion's Relationships section. This is a review obligation, not gate-checkable.

### Consequences

* Good: qa-docs membership is enforced in CI from its first member, and the fourth family is one registry entry with no new check code, on both axes now demonstrated.
* Good: the axis flag that would otherwise have been resolved mid-build, after two members were drafted, is closed before drafting starts, which is the whole point of contract-first.
* Good: the cross-family chain gives the library its first end-to-end worked thread (PRD to user story to acceptance criteria to test plan to test case to bug report), which is a stronger demonstration of the library's coherence than any single bundle.
* Neutral: the contract is adopted with zero members, so check K has nothing to gate for this family until test-plan lands. The gate stays green in the meantime; the enforcement is latent, not absent.
* Bad: chaining across a family boundary couples `qa-docs` examples to `delivery-docs` files. If a delivery-docs example is ever rewritten around a different feature, three qa-docs examples go stale with it. Accepted deliberately: the coupling is what teaches the boundary, the link gate catches a moved or deleted file, and the alternative (an isolated QA scenario) costs the family its main teaching point. Recorded here so a future rewrite knows the blast radius.
* Bad: `pairs_with` will be thin. pm-skills ships no testing or QA skill at all (finding EC-4, recorded in `STATE.md` alongside this contract), so the only honest pairing available is `deliver-edge-cases`, and only where that claim is true of the specific member.

### Confirmation

Enforced by check K in `tools/check-bundles.py`, run in CI by `.github/workflows/ci.yml`, with branch protection on `main` requiring the `gate` job.

Because no qa-docs member exists yet, confirmation has two parts, as [ADR 0024](0024-adopt-governance-docs-family-contract.md)'s did. **Now:** the registry entry is in place and the gate is green (nothing to gate yet, and the contract file resolves), and `tools/test-check-k.py` section 5 asserts over the live `FAMILY_CONTRACTS` that every ratified entry (now including `qa-docs`) declares exactly one axis and a contract path that resolves, so a registry typo fails CI rather than waiting for a member to trip it. **When test-plan lands:** it becomes the live confirmation, reporting "conforms to qa-docs contract (phase, status, sizes)"; a member declaring `classification: utility`, a wrong phase, a `draft` status, or an out-of-shape size will each fail check K with a message naming what it required.

## More Information

This is the fourth family contract, after [delivery-docs](../contracts/delivery-docs.md) ([ADR 0020](0020-adopt-delivery-docs-family-contract.md)), [decision-docs](../contracts/decision-docs.md) ([ADR 0022](0022-adopt-decision-docs-family-contract.md)), and [governance-docs](../contracts/governance-docs.md) ([ADR 0024](0024-adopt-governance-docs-family-contract.md)), and the second on `phase: develop`. Its three members (test-plan, test-case, bug-report) are built next through the per-bundle pipeline ([docs/internal/bundle-pipeline.md](../bundle-pipeline.md)); the build-out stops at the qa-docs family boundary for maintainer batch review.

One standards-recency trap is named in the contract's section 3.6 because it will otherwise be repeated by every member: **IEEE 829 is superseded by ISO/IEC/IEEE 29119-3**. The catalog already notes this at entry 102; the contract makes it a citation obligation rather than a footnote. Its exact status (superseded, withdrawn, or both, and when) is a claim for the test-plan bundle's research to verify against the standards bodies rather than to inherit from the catalog.
