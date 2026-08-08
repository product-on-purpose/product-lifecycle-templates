---
status: accepted
date: 2026-08-05
decision-makers: [jprisant]
consulted: [claude]
---

# Adopt the communication-docs family contract (status-report), a one-member family whose members own none of their own facts

## TL;DR

- **Decision:** Adopt the communication-docs family contract with `status-report` as its sole Tier-1 member,
  and register the family in check K on `classification: utility`, single value.
- **Why:** a status report owns none of its own facts, every figure is read from an artifact of greater
  authority elsewhere in the library, so its real failure mode is being stale or disagreeing with the source
  it summarises rather than being wrong outright; the contract's no-new-facts rule enforces exactly that.
- **Status:** accepted 2026-08-05.

## Context and Problem Statement

One Tier-1 type exists to tell people who are **not** doing the work what is happening with it. A **status
report**'s audience is outside the team, its content summarises things recorded elsewhere, and its value
expires.

**The defining property is that the document owns none of its own facts.** Every number in a status report is
read from somewhere with more authority: a KPI dashboard, a risk register, a RAID log, a roadmap, a backlog.
That makes its failure mode specific and unlike any other family's. It is not *being wrong*. It is **being
stale, or disagreeing with the source it summarises** - and a report that contradicts the dashboard is worse
than no report, because someone will act on it.

**This family has one Tier-1 member, which is stated rather than hidden.** A one-member family is a legal
shape, and the contract exists for the same reason the others do: to bind the member that is coming and any
that follow. It names what would join (an executive briefing or steering pack, a release announcement
distinct from `release-notes`, a stakeholder update), all Tier 2 and all grow-by-pull, so a future reader can
tell whether the family was drawn around a real category or around a single document that needed somewhere to
live.

## Decision

**Adopt the contract as written**, and register `communication-docs` in check K on `classification: utility`,
single value.

**Why `classification` and not `phase`.** A status report is not the output of a lifecycle stage. It is
produced throughout, on a cadence, for as long as the work continues. It has no phase that is honestly its
own, and forcing one would misdescribe it. It is a standing periodic instrument, which is what the second
axis exists for ([ADR 0015](0015-second-taxonomy-axis-phase-xor-classification.md)), and `utility` is the
same call `governance-docs` made for the same reason: maintained, periodic, valuable only while current.

**The family-specific obligation is the no-new-facts rule, and it is stricter than any other family's
shared-scenario rule on purpose.** Every figure in a member's example must be **read from an artifact that
already exists in this library**, and the example must say where each one comes from. **A disagreement
between the report and any source it cites is a contract failure, not a rounding difference.** That is the
only way to demonstrate the type's real discipline: an example that invents its own numbers teaches exactly
the failure the document type has.

The sources exist and this was verified rather than assumed. The `status-report` example reads from the
`kpi-dashboard`, `risk-register`, `raid-log`, `product-roadmap` and `okrs` examples, all five of which are
present and already agree with each other.

**One further obligation: the example must show one thing going badly**, sourced from the thread rather than
invented. The material is already there and was confirmed: Time to Insight sits at **-18% against a -30%
target**, below the 25% green line, and reads as lagging in the `kpi-dashboard` example. A status report where
everything is green teaches nothing, because the whole skill of the type is saying a bad thing clearly to an
audience that outranks you.

## Consequences

- Check K gates `classification: utility`, the status and the size shapes. The entry is latent until
  `status-report` lands.
- **The no-new-facts rule creates a maintenance coupling that no other family has.** If a figure in one of
  the five source examples changes, the status report example is wrong. That is a real cost and it is
  accepted, because the alternative (a report whose numbers agree with nothing) would misrepresent the type
  entirely. `tools/check-example-chronology.py` already enforces the temporal half of this coupling; the
  numeric half is a review obligation.
- A candidate that **owns** its facts belongs elsewhere: `governance-docs` for standing instruments,
  `strategy-docs` for direction, `process-docs` for retrospective learning
  ([ADR 0033](0033-adopt-process-docs-family-contract.md)). A candidate written for the team doing the work
  rather than for an audience outside it is not a communication document, it is a working one.
- **The citation hazard is that the literature is thin and vendor-dominated.** Status reporting is widely
  practised and rarely written about by named practitioners, so the honest finding will probably be that most
  guidance traces to project-management tooling vendors. The contract requires recording that rather than
  dressing vendor content as practice, which is the same discipline the `okrs` and `business-case` research
  logs already apply.
- If no further member is ever pulled, this family stays at one permanently. The contract states that is an
  acceptable outcome rather than a defect.
