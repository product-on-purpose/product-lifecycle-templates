---
status: accepted
date: 2026-08-05
decision-makers: [jprisant]
consulted: [claude]
---

# Adopt the process-docs family contract (sprint-retrospective-notes, incident-postmortem), the family that exists to be taught by contrast

## TL;DR

- **Decision:** Adopt the process-docs family contract with `sprint-retrospective-notes` and
  `incident-postmortem`, and register the family in check K on `phase: iterate`, single value.
- **Why:** the family exists to teach, by contrast, the distinction between a retrospective (looks back on a
  period, on a cadence, at how the team worked) and a postmortem (looks back on an event, triggered by it, at
  why a specific thing failed); each member's companion must state what the other is for and when a team is
  reaching for the wrong one.
- **Status:** accepted 2026-08-05.

## Context and Problem Statement

Two Tier-1 types look backward in order to change what happens next. A **sprint retrospective** looks back on
a **period**, on a cadence, at how the team worked. An **incident postmortem** looks back on an **event**,
triggered by it, at why a specific thing failed. [ADR 0023 (the Tier-1 family
taxonomy)](0023-resolve-the-tier-1-family-taxonomy.md) placed both here **specifically so the distinction
between them could be taught by contrast rather than asserted twice in two unrelated bundles.**

The shared job is converting hindsight into a change someone owns. The shared failure is producing a document
that records feelings or timelines and commits nobody to anything.

## Decision

**Adopt the contract as written**, and register `process-docs` in check K on `phase: iterate`, single value.

The second family on `phase: iterate` is not a collision, for the same reason `qa-docs` and `decision-docs`
both sit on `develop`: check K gates per declared family, so a phase value is constrained within a family and
never claimed by one.

**The family-specific obligation is the contrast itself.** Each member's companion must state, in its
Relationships section, what the **other** member is for and when a team is reaching for the wrong one. The
contract names the real-world error precisely: running a retro on an incident produces a blameless discussion
of something that needed causal analysis, and running a postmortem on a sprint pathologises ordinary work.

**Two obligations bind the examples, and both exist to stop the family teaching the opposite of its point.**

- **The anti-blur rule.** The incident postmortem example analyses a real event from the existing Acme
  Analytics thread, and the retrospective example covers a sprint from the `sprint-backlog` scenario and
  **must not be about the incident.** Two examples about the same occurrence would demonstrate the confusion
  the family exists to dispel.
- **The honesty obligation.** *A postmortem example that ends with every action closed is a fiction.* At
  least one action must be open, owned and dated, because the failure this document type actually has is
  actions recorded and never done.

The thread already supplies the material, and this was verified rather than assumed: the `bug-report` example
documents **DEF-2291**, an aggregate computed before the entitlement row filter, which disclosed the magnitude
of hidden rows. That is exactly what a postmortem examines, and the `test-plan` example already records a
suspension rule firing and a triage disagreement left visible. Postmortem actions must land somewhere the
library already models: the `risk-register`, the `raid-log` or the `product-backlog`.

## Consequences

- Check K gates `phase: iterate`, the status and the size shapes on every member. The entry is latent until
  the first member lands.
- **`sizes_available` is expected to come under pressure, and the contract says so in advance.**
  Retrospective notes are a strong single-size candidate. The catalog's size calls are hypotheses rather than
  facts (finding EC-2 in `STATE.md`) and two `qa-docs` members have already departed from them on evidence, so
  `[lean]` alone is a legitimate outcome if that member's research supports it.
- `methodology` stays descriptive. The retro is Scrum and agile-lineage, the postmortem is SRE-lineage, and
  this family is a clear case of the [ADR 0020](0020-adopt-delivery-docs-family-contract.md) lesson: one
  required value would force one member to misdescribe itself.
- **The citation hazard is named as attributed folklore.** "Blameless postmortem", the retrospective prime
  directive, the five whys and the sprint retrospective's own canonical shape all circulate detached from
  whoever wrote them, and at least one has a contested origin. The contract requires verifying who said a
  thing before quoting it, and **recording the ones that could not be traced** rather than dropping them
  silently. The two report-only lints now running at pipeline phase 3.5 target exactly this class.
- A candidate that looks forward belongs elsewhere (`discovery-docs` before a decision, `strategy-docs` for
  direction, `delivery-docs` for the work itself), and a candidate consulted repeatedly rather than written
  per occasion belongs to `standing-standards` ([ADR 0032](0032-adopt-standing-standards-family-contract.md)).
- Likely future members, both Tier 2 and both grow-by-pull: `project-milestone-retrospective` and
  `pi-release-retrospective`.
