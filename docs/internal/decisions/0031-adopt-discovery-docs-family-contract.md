---
status: accepted
date: 2026-08-04
decision-makers: [jprisant]
consulted: [claude]
---

# Adopt the discovery-docs family contract (business-case, user-persona, prototype-brief), the first family to extend the worked thread backward and the first ratified with a provisional member

## TL;DR

- **Decision:** Adopt the discovery-docs family contract with `business-case`, `user-persona`, and a
  provisional third member `prototype-brief`, and register the family in check K on the `phase` axis at the
  single value `discover`.
- **Why:** the persona is checkable rather than asserted (`Recurring Analyst` appears in sixteen files and no
  bundle has ever defined it), and ratifying `prototype-brief`'s membership now, with its admission-test
  outcome pre-committed, avoids deciding membership after the research runs, when a negative answer is harder
  to accept.
- **Status:** accepted 2026-08-04.

## Context and Problem Statement

The Tier-1 floor build-out ([ADR 0021](0021-complete-the-tier-1-floor.md)) turns next to `discovery-docs`:
the family of documents that exist to decide **whether to build something, before anyone commits to building
it**. Every new family gets a ratified contract before its members are built (the
[ADR 0020](0020-adopt-delivery-docs-family-contract.md) pattern), so a member is born into an enforced family
rather than joining an honour system. The contract was drafted in PR #55 and has sat at *proposed, pending
maintainer review* since; this record ratifies it.

Three things make this contract different from the five before it.

**It extends the library's worked thread backward in time, and it does so to pay off a debt.** `qa-docs`
extended the Acme Analytics scenario downward into verification; `strategy-docs` extended it upward into
direction. Both added new ground. This family goes **backward, to before the decisions the library has
already documented**: the business case justifies the investment the FY26 strategy later spends, the persona
*is* the Recurring Analyst, and the prototype brief commissions the cheap test of the question-first entry
hypothesis that the roadmap carries in its Now lane.

The persona is the sharpest case, and it is checkable rather than asserted. **"Recurring Analyst" appears in
sixteen files across the library** and no bundle has ever defined it. The kpi-dashboard metric definitions
and the acceptance-criteria example have both been referring for months to a person the library never
described. This family is not inventing a scenario; it is defining a term already in use.

**It is the first family ratified with a member that may never be built.** `prototype-brief` is a new type
added by [ADR 0030](0030-templating-scope-markdown-documents.md), not a rename of catalog 54
(`interactive-prototype`), whose artifact is executable and therefore out of scope. Its membership is
conditional on its own research passing ADR 0030's admission test: **a named source must publish this as a
written document.** That test was applied rigorously to reject `wireframe` and has not been applied with
equal rigour to admit this.

Ratifying now, with that condition stated and its outcome pre-committed, is the point. The alternative is
deciding membership *after* the research, when a negative answer costs a bundle and is correspondingly easier
to rationalise away. The contract therefore states plainly that if no named source is found, **the type does
not ship and this family has two members, which is a legitimate outcome and not a failure of the contract.**

**It is the family most exposed to this library's dominant defect class.** The contract names the hazard in
its own words: business cases and personas both attract invented percentages, and the prototype literature
attracts vendor claims. A business case is a document whose genre convention is a confident number. Two
report-only lints shipped days before this ratification target exactly that failure
(`lint-number-provenance`, `lint-unsourced-confidence`), and pipeline phase 3.5 runs both before the review.
That is fortunate timing rather than design, and it is worth recording as such.

## Decision

**Adopt the contract as written**, and register `discovery-docs` in check K on the `phase` axis with the
single value `discover`.

The axis value is single by construction rather than by preference: every member is written once for a
decision and is finished when that decision is made, so no member of this family can be a standing
instrument. A candidate whose honest axis is `classification` belongs to a different family.

Two obligations in the contract are worth naming here because they bind the build directly.

**The chronology obligation.** A discovery document is written *before* the documents it leads to, so its
example's date must precede the artifacts it anticipates and it must not cite them as existing. The contract
adds this on evidence: the `product-roadmap` example shipped dated February while citing a PRD created in
June. Every member of this family points forward, which makes the defect easier to commit here than
anywhere else. Concretely, the existing thread runs `product-vision` 2026-01-14, `product-strategy`
2026-01-28, `product-roadmap` 2026-02-11, so a business case justifying the FY26 investment dates to roughly
Q4 2025. `tools/check-example-chronology.py`, which did not exist when this contract was drafted, now
enforces exactly this in CI.

**No grandfathering on example independence.** Sixteen shipped bundles are grandfathered at measured ceilings
by `tools/check-example-independence.py`. The contract states that no member of this family is, so a copied
passage fails on its first commit.

## Consequences

- Check K gates `phase: discover` and the status and size shapes on every `discovery-docs` member. The entry
  is latent until `business-case` lands, exactly as `governance-docs` was latent until `risk-register`.
- The family ships two or three bundles. The build backlog is 8 if `prototype-brief` is admitted and 7 if it
  is not, and that number is not known until its research runs.
- `methodology` stays descriptive rather than gated, the [ADR 0020](0020-adopt-delivery-docs-family-contract.md)
  lesson: a business case is methodology-agnostic, a persona leans research practice, and a prototype brief
  leans dual-track or design thinking. A single required value would force at least one to misdescribe itself.
- `sizes_available` may be `[lean]` alone where a member's research shows it does not earn a second weight.
  The catalog's size calls are hypotheses, not facts (finding EC-2 in `STATE.md`), and two `qa-docs` members
  have already departed from them on evidence.
- If `prototype-brief`'s research shows its dominant use is handoff-to-build rather than testing an
  assumption, `phase: develop` becomes the better call and the placement is revisited per
  [`decision-procedures.md`](../decision-procedures.md) section 10, rather than being defended because it is
  now written down.
