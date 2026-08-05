---
status: accepted
date: 2026-08-05
decision-makers: [jprisant]
consulted: [claude]
---

# Adopt the standing-standards family contract (definition-of-done, runbook), the first family to pair foundation with tool

## Context and Problem Statement

Two Tier-1 types are neither phase-bound nor periodic. A **definition of done** is agreed by a team and then
judged against every increment; a **runbook** is written once and executed whenever a known situation
occurs. Neither is the output of a lifecycle stage, and neither is revised on a calendar. They were moved
here by [ADR 0023 (the Tier-1 family taxonomy)](0023-resolve-the-tier-1-family-taxonomy.md) on the shared
reasoning that both are *agreed once, applied every time*, which that record required be argued against real
members in a contract. This is that contract.

**The axis question is the substance.** Both members are standing, so both sit on `classification` rather
than `phase`. But they are not the same kind of standing artifact, and one value would misdescribe one of
them:

- **`definition-of-done` is `foundation`.** A standard you are judged **against**. Its authority comes from
  having been agreed; its failure is being agreed once and never honoured.
- **`runbook` is `tool`.** An instrument you **execute**, under time pressure, often by someone who did not
  write it. Its authority comes from being correct right now; its failure is being correct on the day it was
  written and wrong on the day it is needed.

**The distinguishing test: is it a standard you judge against, or an instrument you execute?** That is a
different cut from `strategy-docs`' set, which split `foundation` from `utility` on argued-and-durable versus
maintained-and-periodic. Both cuts are legitimate because the axis has three legal values, and the cut here
is not invented for convenience: [ADR 0015](0015-second-taxonomy-axis-phase-xor-classification.md) adopted
this vocabulary **because pm-skills uses it**, and pm-skills introduced `classification: tool` for its Sprint
families, which are defined procedures a team runs. A runbook is structurally that kind of object.

## Decision

**Adopt the contract as written**, and register `standing-standards` in check K on the `classification` axis
with the **set** `foundation` or `tool`.

**The family-specific obligation is a staleness rule rather than a shared scenario.** Every other family
chains its examples on one narrative; this one binds a mechanism instead, because its members share a failure
mode rather than a position in a story. Both go quietly out of date, so **every member's template must carry
a review trigger with a named owner and a condition** - what event makes this document wrong, and who
notices - not a calendar reminder. A definition of done goes stale when practice changes without the document
changing; a runbook goes stale when the system it describes is redeployed. This is the repository's own
finding **DF-3** turned into a template requirement: what is gated for freshness stays fresh, what is not
drifts.

**`tools/test-check-k.py` gains the fixture the contract asks for, before the first member lands.**
`strategy-docs` proved that a set works; it did not prove that *this* set works, because it spans
`foundation`/`utility` and the check reports back whichever values it was given. The new block asserts that
`foundation` and `tool` both conform, that `utility` is rejected, that the rejection message lists
`foundation/tool` rather than `foundation/utility`, and that a phase-axis member is still refused. The suite
goes from 69 to 80 assertions.

## Consequences

- Check K gates the set, the status and the size shapes on every member. The entry is latent until
  `definition-of-done` or `runbook` lands.
- **Check K can enforce membership OF the set and never that a member picked the RIGHT value.** Nothing
  mechanical stops `runbook` declaring `foundation`. That assignment is a review obligation, and the argued
  split above is the standard it is reviewed against. This limit is stated in the registry comment so it is
  read at the point of use.
- **This family's coherence is thinner than `governance-docs`' or `strategy-docs`', and the contract says so
  rather than asserting strength it does not have.** "Agreed once, applied every time" is closer to a cadence
  than to a job, and grouping by rhythm is weaker than grouping by function. The contract therefore supplies
  its own falsifier: **if a candidate arrives that matches the cadence but is not consulted at the moment of
  action, this family was drawn around the axis rather than around a job, and it should split rather than
  absorb the candidate.** Ratifying a weaker argument with its disproof attached is the point; the
  alternative is discovering the weakness later with members already inside.
- The shared-scenario rule applies only where natural (a definition of done the `sprint-backlog` and
  `acceptance-criteria` examples could be judged against; a runbook for the Saved Views service the `sdd` and
  `test-plan` examples describe). Chaining is deliberately weaker here, because a standing standard belongs to
  a team rather than to a moment in a story.
- `methodology` stays descriptive: `definition-of-done` is agile-lineage, `runbook` is DevOps and SRE-lineage,
  and one required value would force one to misdescribe itself ([ADR 0020](0020-adopt-delivery-docs-family-contract.md)).
- The citation hazard is named: **folklore presented as standard.** "Definition of done" is Scrum-adjacent
  vocabulary whose actual definition in the Scrum Guide must be checked rather than assumed, and runbook
  practice is dominated by vendor content.
