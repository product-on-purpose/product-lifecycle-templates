---
status: accepted
date: 2026-07-22
decision-makers: [jprisant]
consulted: [claude]
---

# Adopt the governance-docs family contract (risk-register, raid-log, kpi-dashboard), the first on the classification axis

## Context and Problem Statement

The Tier-1 floor build-out ([ADR 0021](0021-complete-the-tier-1-floor.md)) turns next to `governance-docs`, the family of standing governance instruments: a risk register, a RAID log, and a KPI dashboard. Every new family gets a ratified contract before its members are built ([ADR 0020](0020-adopt-delivery-docs-family-contract.md) pattern), so a member is born into an enforced family rather than joining an honor system.

Two things make this contract different from the two before it.

First, it is the **first family on the `classification` axis**. delivery-docs and decision-docs both gate `phase`; governance-docs' members are standing instruments with no single lifecycle phase, so the family gates `classification` instead. The gate capability to do this landed in [ADR 0023](0023-resolve-the-tier-1-family-taxonomy.md)'s implementation (check K reads whichever axis a contract names), so this contract is the first live use of it.

Second, it is adopted **before any member is built**. decision-docs earned its contract once it already had three members; governance-docs has none yet. The contract therefore describes the set its three planned members must join, and the first member built (risk-register) is the live confirmation.

[ADR 0023](0023-resolve-the-tier-1-family-taxonomy.md) also deferred one open question to this step: whether `kpi-dashboard` is `classification: utility` or `phase: measure`. That question is answered here, against the real members, as the ADR 0023 rule requires.

## Decision Drivers

- **Contract-first, so membership is mechanical from the first member.** A family whose members are built before its contract exists risks a member drifting to the wrong axis or value with nothing to catch it.
- **The axis call must be honest, not convenient.** kpi-dashboard's axis is decided by what a KPI dashboard is, not by what keeps the family tidiest, even though the honest answer happens to keep it coherent.
- **Do not re-learn the ADR 0020 lesson.** Methodology is descriptive, not a membership rule; the contract is written that way from the start.
- **The check should generalize, not grow machinery.** A third family, and the first on a new axis, should be one `FAMILY_CONTRACTS` entry plus the axis-set support already built, no new check code.

## Considered Options

- **Option A: adopt a governance-docs contract now, `classification: utility`, methodology descriptive, kpi-dashboard resolved to `utility`, enforced by check K via a registry entry.** Chosen.
- **Option B: defer the contract until the first member is built**, as decision-docs did. Rejected: decision-docs deferred because it already *had* members; deferring here would build the first member into an unenforced family, the exact thing the contract-first rule prevents, and it would leave the kpi-dashboard axis unsettled while drafting begins.
- **Option C: make kpi-dashboard `phase: measure`.** Rejected: it would split the family across two axes (forcing either a mixed-axis contract or kpi-dashboard's removal), and it misstates the artifact. A KPI dashboard is a standing, continuously-maintained instrument (catalog entry 139: "measurement / ongoing"), not a deliverable produced once at a measure phase. This is the D-B / [ADR 0023](0023-resolve-the-tier-1-family-taxonomy.md) reasoning applied to the last member it was deferred for.

## Decision Outcome

**Adopt [docs/internal/contracts/governance-docs.md](../contracts/governance-docs.md) (version 0.1.0), enforced by the existing gate check K via a new `FAMILY_CONTRACTS` entry keyed on `classification`.** For every bundle declaring `family: governance-docs`, check K requires `classification: utility`, a `beta` or `stable` `status`, a size shape of `[lean, full]` or `[lean]`, and that the contract file resolves. Methodology is descriptive and is not gated, carrying the ADR 0020 lesson forward.

**kpi-dashboard is `classification: utility`.** The catalog marks it "measurement / ongoing"; it is a standing governance surface maintained continuously, beside the risk register and RAID log, not a phase-`measure` output. This keeps governance-docs a coherent three-member classification family, but the call is made on the merits of what the artifact is, and would be the same if it stood alone.

**The family-specific rule is a shared scenario, like delivery-docs and unlike decision-docs.** governance-docs members chain their examples on one project, because the members genuinely overlap on the same project (the risk register is the R of the RAID log; the dashboard tracks the health of what those risks threaten). Showing them together teaches the relationship, where decision-docs keeps its examples independent to teach a distinction. This is a review obligation, not gate-checkable.

### Consequences

* Good: governance-docs membership is enforced in CI from its first member, on the `classification` axis, exactly as the two phase families are on `phase`.
* Good: the three family contracts now demonstrate the registry generalizes across *axes*, not just across families: a third family, and the first classification one, is one entry (`FAMILY_CONTRACTS["governance-docs"]`) with no new check code, because [ADR 0023](0023-resolve-the-tier-1-family-taxonomy.md) already taught check K to read either axis.
* Good: the last axis question ADR 0023 left open (kpi-dashboard) is closed, against real members, at the step the rule designates for it.
* Neutral: the contract is adopted with zero members, so check K has nothing to gate for this family until risk-register lands. The gate stays green in the meantime; the enforcement is latent, not absent.
* Bad: `governance-docs` at `classification: utility` assumes all three members are standing utilities. If kpi-dashboard's own research later argues it is genuinely a `tool` (an executed instrument) rather than a `utility` (a maintained one), the contract would widen to a value set `[utility, tool]` (a contract change with a decision record), not break, thanks to the axis-set support from ADR 0023.

### Confirmation

Enforced by check K in `tools/check-bundles.py`, run in CI by `.github/workflows/ci.yml`, with branch protection on `main` requiring the `gate` job.

Because no governance-docs member exists yet, confirmation has two parts. **Now:** the registry entry is in place and the gate is green (nothing to gate yet, and the contract file resolves); the classification-axis machinery this contract relies on is covered by `tools/test-check-k.py`, whose fixtures use a `governance-docs` classification family and assert that `classification: utility` conforms while a wrong value and a `phase: measure` axis-mismatch each fail with a located message (37 assertions, mutation-checked, run in CI). **When risk-register lands:** it becomes the live confirmation, reporting "conforms to governance-docs contract (classification, status, sizes)"; a member declaring `phase: measure`, a non-`utility` classification, a `draft` status, or an out-of-shape size will each fail check K.

## More Information

This is the third family contract, after [delivery-docs](../contracts/delivery-docs.md) ([ADR 0020](0020-adopt-delivery-docs-family-contract.md)) and [decision-docs](../contracts/decision-docs.md) ([ADR 0022](0022-adopt-decision-docs-family-contract.md)), and the first on the `classification` axis ([ADR 0015](0015-second-taxonomy-axis-phase-xor-classification.md), [ADR 0023](0023-resolve-the-tier-1-family-taxonomy.md)). Its three members (risk-register, raid-log, kpi-dashboard) are built next through the per-bundle pipeline ([docs/internal/bundle-pipeline.md](../bundle-pipeline.md)); the build-out stops at the governance-docs family boundary for maintainer batch review.
