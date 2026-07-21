---
status: accepted
date: 2026-07-21
decision-makers: [jprisant]
consulted: [claude]
---

# Adopt the decision-docs family contract (rfc, adr, sdd), enforced by gate check K

## Context and Problem Statement

The `decision-docs` family had two members (`rfc`, `adr`) and no ratified contract, so its members passed
gate check K with a "no ratified contract yet; not enforced" note ([ADR 0020](0020-adopt-delivery-docs-family-contract.md)
set up the check to do exactly that, so adding a family would not break the gate before its contract
existed). Landing the `sdd` bundle ([ADR 0021](0021-complete-the-tier-1-floor.md), the first Tier-1 floor
bundle) made the family a trio and gave it a clear, teachable shape: three technical decision-and-design
artifacts with distinct jobs. The family now earns the contract that ADR 0020 said it would get "when the
pair earns one."

Unlike delivery-docs, whose contract pre-existed as a draft and whose first enforcement surfaced a
methodology conflict, decision-docs is a clean case: all three members already share `phase: develop`,
`status: beta`, `sizes_available: [lean, full]`, and `methodology: generic`, so the contract describes a
set that already conforms rather than one that must be bent to fit.

## Decision Drivers

- **A family with three members and none enforced is an honor system.** Membership should be a mechanical
  gate so a bundle that drifts to the wrong phase, status, or size shape is caught in CI.
- **Do not re-learn the ADR 0020 lesson.** Methodology is descriptive, not a membership rule; the contract
  should be written that way from the start, not gated and then amended.
- **The check should generalize, not grow machinery.** ADR 0020 built check K to read a per-family
  registry (`FAMILY_CONTRACTS`); a second family should be one registry entry, no new code.
- **Make the family's internal claims honest while touching it.** `adr` and `rfc` both carried stale
  `future:` cross-references to bundles that now exist (`rfc`, and the design doc that shipped as `sdd`).

## Considered Options

- **Option A: adopt a decision-docs contract now, methodology descriptive, enforced by check K via a
  registry entry.** Chosen.
- **Option B: leave decision-docs unenforced** until it has more members. Rejected: the family is stable
  at three, the cost is one registry entry, and "unenforced" means a member could silently drift.
- **Option C: merge decision-docs and delivery-docs into one contract** parameterized by phase. Rejected:
  they are genuinely different families (deliver vs develop, delivery-chain vs decision-and-design), and
  one member-specific rule differs (delivery-docs chains examples on a shared scenario; decision-docs
  keeps examples deliberately independent to teach the role distinction).

## Decision Outcome

**Adopt [docs/internal/contracts/decision-docs.md](../contracts/decision-docs.md) (version 0.1.0),
enforced by the existing gate check K via a new `FAMILY_CONTRACTS` entry.** For every bundle declaring
`family: decision-docs`, check K requires `phase: develop`, a `beta` or `stable` `status`, a size shape of
`[lean, full]` or `[lean]`, and that the contract file resolves. Methodology is descriptive and is not
gated, carrying the ADR 0020 lesson forward from the start.

**The family-specific rule differs from delivery-docs on purpose.** delivery-docs members chain their
examples on one shared "Saved Views" scenario to demonstrate end-to-end traceability. decision-docs
members' examples are deliberately independent (RFC-0001 is a real accepted proposal, the ADR examples are
real repository decisions, the SDD example is a worked design), because the family's teaching value is the
*distinction* between propose / record / describe, not a single thread. The contract encodes a
cross-reference rule instead: each companion must place its member correctly against the other two, and
must not overstate the RFC-versus-design-doc boundary (which the industry genuinely blurs) while keeping
the ADR categorically distinct. This rule is a review obligation, not gate-checkable.

**Stale cross-references fixed in the same change.** `adr`'s `related_templates` carried `future:rfc` and
`future:technical-design-doc`, and `rfc`'s carried `future:design-doc`; `rfc` and `sdd` both now exist, so
those references were stale claims that the `future:` prefix let pass the gate silently. They are corrected
to `rfc` and `sdd`. `future:spike-report` and `future:solution-brief` remain, as those bundles do not
exist yet.

### Consequences

* Good: decision-docs membership is enforced in CI, exactly as delivery-docs has been since ADR 0020. A
  member that drifts to the wrong phase, status, or size shape fails the gate.
* Good: the two family contracts now demonstrate the registry generalizes: a second family is one entry
  (`FAMILY_CONTRACTS["decision-docs"]`), no new check code.
* Good: the family's internal cross-references are honest again; `future:rfc` and `future:design-doc` no
  longer claim as unbuilt what has shipped.
* Neutral: the family stays at three members; a fourth (a spike report, a solution brief) would join under
  the same contract with no contract change unless it declares a different phase or size shape.

### Confirmation

Enforced by check K in `tools/check-bundles.py`, run in CI by `.github/workflows/ci.yml`, with branch
protection on `main` requiring the `gate` job.

Adversarially tested at authoring time (2026-07-21): with the registry entry in place, `rfc`, `adr`, and
`sdd` each report "conforms to decision-docs contract (phase, status, sizes)" instead of the previous "no
ratified contract yet" note; temporarily setting a member's `phase` to a non-`develop` value, its `status`
to `draft`, or its size shape outside `[lean, full]` / `[lean]` each fails check K with a located message;
and a missing contract file fails. The gate is green at eleven checks on all seven bundles.

## More Information

This is the second family contract, after [delivery-docs](../contracts/delivery-docs.md)
([ADR 0020](0020-adopt-delivery-docs-family-contract.md)). Whether `decision-docs` earns a fourth member is
governed by the Tier-1 floor build-out ([ADR 0021](0021-complete-the-tier-1-floor.md) and
[docs/internal/buildout-plan.md](../buildout-plan.md)); the contract does not schedule one. The eight new
families the build-out will create each get a contract on this same pattern before their members are
enforced.
