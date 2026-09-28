---
status: proposed
date: 2026-09-27
decision-makers: [jprisant]
consulted: [claude]
---

# `production-readiness-review` joins `standing-standards` as a `tool`, its fifth member and first unforecast one

## TL;DR

- **Decision.** The `production-readiness-review` bundle declares **`family: standing-standards`** and
  **`classification: tool`**. It becomes that family's fifth member, beside `definition-of-done`
  (`foundation`), `runbook` (`tool`), `launch-coordination-checklist` (`tool`) and `definition-of-ready`
  (`foundation`), and the [contract](../contracts/standing-standards.md) moves to `0.4.0`.
- **Why a record is needed.** Unlike `launch-coordination-checklist` (ADR 0053) and `definition-of-ready`
  (ADR 0058), this type was never named on the contract's "likely future members" list
  (`standing-standards.md:38`). It is the family's first member admitted purely on the membership test and
  falsifier, with no forecast to confirm.
- **What settled membership:** the family's own falsifier
  ([ADR 0032](0032-adopt-standing-standards-family-contract.md)) - a maintained PRR checklist is "consulted at
  the moment of action," the same test that admitted `launch-coordination-checklist`. A per-service, one-time
  review record excludes on the contract's own analogy: "a runbook written for one incident is an incident
  report" (`standing-standards.md:29`).
- **What settled classification:** the contract's section 2 cut, "is it a standard you judge against, or an
  instrument you execute?", argued marker-by-marker below. **Recorded honestly:** the strongest single
  admission quotation reads as judged-against language, and this record explains why that does not carry the
  classification.
- **The central open risk this record does not resolve:** the boundary with `launch-coordination-checklist`.
  A gap-fill retrieval in the 2026-09-27 admission sweep read Google's own Appendix E and found it
  engineering-scoped throughout, which falsifies the subject-matter half of the two bundles' distinction. Only
  trigger, team and timing survive, and the spec, not this record, carries that argument in full.
- **Status:** proposed 2026-09-27. **Held proposed until the maintainer reads the contract diff**, the way
  [ADR 0059](0059-announcement-internal-comms-joins-delivery-docs.md) and
  [ADR 0060](0060-change-request-joins-delivery-docs.md) were before their own contract diffs landed.

## Context and Problem Statement

A research sweep run 2026-09-27 tested five queued candidate types against their admission evidence and, where
a family question was open, against all nine family contracts. For `production-readiness-review`, three named
sources publish the document as a written checklist or template: Susan Fowler's *Production-Ready
Microservices* (O'Reilly), Appendix A; GitLab's production readiness review template, since archived; and
Mercari's production readiness checklist. Google's SRE book describes the review and says its SRE team
"establishes and maintains a PRR checklist explicitly for the Analysis phase". The `launch-coordination-checklist`
spec had asked its own research to look for exactly such a source (`tier2-specs.md:465-468`: "One source
suffices; a second would change the teaching"). The maintainer reviewed the
sweep's verdicts on 2026-09-27 and ruled: build, joining `standing-standards` as `classification: tool`.

This record exists to make that classification call reviewable rather than asserted, the way
[ADR 0058](0058-definition-of-ready-joins-standing-standards-as-a-foundation.md) did for
`definition-of-ready`, since [ADR 0032](0032-adopt-standing-standards-family-contract.md) and check K can
verify a member picked a value from the set `{foundation, tool}`, never that it picked the right one.

## Decision Drivers

- The classification must follow what the document **does**, per the contract's own cut, not what its
  strongest admission quotation sounds like out of context.
- Family membership (the falsifier) and classification (the cut) are two different questions, and
  [ADR 0058](0058-definition-of-ready-joins-standing-standards-as-a-foundation.md) already warns that
  conflating them is the easiest way to get a member wrong.
- This is the family's first member with no forecast to confirm, so the admission argument must rest entirely
  on the membership test as written, per
  [ADR 0057](0057-issue-log-joins-governance-docs-as-a-fourth-member.md)'s principle that the membership test,
  not a list of members once predicted, governs a candidate.

## Considered Options

1. **`standing-standards`, `classification: tool`.** Chosen.
2. **`standing-standards`, `classification: foundation`.** The case for it: the strongest single admission
   quotation, "Verify that a service meets accepted standards of production setup and operational readiness"
   (Google, ch. 32), is judged-against language, the same register as `definition-of-done` and
   `definition-of-ready`'s own admission quotations. Rejected below.
3. **`governance-docs`.** The case for it: a standing, whole-lifecycle instrument, and AWS's ORR sibling is
   explicitly framed that way ("throughout the complete lifecycle of their service, from inception to
   post-release operations"). Rejected: that family's membership test names "a register, log, or dashboard"
   (`governance-docs.md:11`), and a review checklist with pass/fail criteria is none of the three in form. The
   sweep's own family-fit dimension scored this `admits-with-strain`, not as written.
4. **Decline, per the ADR 0049 shape.** Rejected on the evidence: a refusal in that shape needs zero
   qualifying sources, and three named sources publish the document. The maintainer's ruling was to build.

## Decision Outcome

**Chosen: `standing-standards` with `classification: tool`.**

### Why the family question was never really in doubt

`production-readiness-review`, read as a maintained checklist, passes the same falsifier
[ADR 0053](0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md) applied: "if a candidate
arrives that matches the cadence but is not consulted at the moment of action, this family has been drawn
around the axis rather than around a job" (`standing-standards.md:100-102`). Google's own chapter 32, raw-checked
in this sweep, describes the checklist as something SRE "establishes and maintains ... explicitly for the
Analysis phase" and consults during a review conducted at the moment SRE evaluates whether to take a service on,
not authored once and shelved. Read as a one-time, per-service filled record, the type
excludes from every family the sweep tested, `standing-standards` included, on the contract's own analogy at
`standing-standards.md:29`: "a runbook written for one incident is an incident report." **This bundle is the
standing checklist**, and its worked example is a filled instance of it, the same relationship
`launch-coordination-checklist_example.md` already has to its own template.

### Why `tool`, marker by marker, against the honest `foundation` case

The contract gives each value three markers (`standing-standards.md:72-77`). A Definition of Ready matched all
three of `foundation`'s and none of `tool`'s ([ADR 0058](0058-definition-of-ready-joins-standing-standards-as-a-foundation.md)).
A PRR does not split as cleanly, and the table says so rather than picking the convenient row:

| Marker | `foundation` | `tool` | A production readiness review |
|---|---|---|---|
| What it is | "a standard you are judged against" | "an instrument you execute" | Both, on different readings: its criteria are a standard a service is judged against, but the review itself is executed, once, by a named reviewer, against one service, at one moment |
| When and by whom | "argued to, agreed by a team, and changed deliberately and rarely" | "usually under time pressure and often by someone who did not write it" | **This is where it resolves.** "Usually one to three SREs are selected or self-nominated to conduct the PRR" (Google), and "an experienced engineer, ideally outside of the product team" (Grafana): the reviewer is, by every source read, someone other than the team that wrote the service under review, exactly `tool`'s marker |
| Where authority comes from | "from having been agreed" | "from being correct right now" | The review's finding is a claim about the service's **current** state ("Verify that a service meets accepted standards of production setup and operational readiness," present tense, checked against today's system), not a standard agreed once and left alone |

**The honest `foundation` case, stated rather than hidden.** "Verify that a service meets accepted standards of
production setup and operational readiness" reads, on its own, as judged-against language, the same register
`definition-of-done` and `definition-of-ready`'s admission quotations use. What breaks the parallel is the
second marker: a Definition of Done is applied by the same team that agreed it, to its own work, on a
recurring cadence it controls. A PRR's criteria may be standing, but the act of applying them is executed by
an outside reviewer at a moment the reviewed team does not control, "under time pressure" in the sense that
matters here: SRE will not take on the service, or a maturity gate will not open, until the review closes. That
is `tool`'s marker, not `foundation`'s, and it is what the maintainer's ruling tracks.

### Why not `governance-docs`

`governance-docs.md:11` names three specific forms: "a register, log, or dashboard." A PRR is none of the
three; it is a review instrument with pass/fail criteria applied at a trigger, not a continuously-updated
tracked list of open items. AWS's ORR sibling process being explicitly whole-lifecycle in its own framing
argues for the family's spirit, not its letter, and the sweep's own family-fit dimension recorded this
distinction as `admits-with-strain` against `standing-standards`' clean `admits-as-written`.

### The counter-argument this record keeps rather than omits

**No contract's forecast list named this type.** `standing-standards.md:38` names only "a coding-standards or
engineering-handbook document." A reader who expects family assignment to track a contract's own predictions
would find nothing here to point to, unlike `launch-coordination-checklist` and `definition-of-ready`. It does
not change the outcome, because [ADR 0057](0057-issue-log-joins-governance-docs-as-a-fourth-member.md) already
established that the membership test, not the forecast list, governs a candidate; the tension is recorded so a
future reader sees the family's first unforecast admission was reasoned through the test, not waved in on
precedent.

### Consequences

- `standing-standards` grows from four members to five. Its contract's Members line and change note are
  updated in this change, per the contract's own requirement that a change to itself carry a decision record.
- Check K gates `classification` membership of the set `{foundation, tool}` and cannot verify this member
  picked the *right* value; that stays a review obligation, and the marker-by-marker argument above is the
  standard this member is reviewed against.
- **The launch-checklist boundary remains the build's central risk, not this record's to resolve.** This ADR
  settles family and classification; it does not settle, and does not attempt to settle, whether the new
  bundle's companion correctly states its position against `launch-coordination-checklist_companion.md:464-469`.
  That argument lives in the spec.
- `tier2-specs.md` records this type as specced. The maintainer directed the build on 2026-09-27, under
  [ADR 0041](0041-maintainer-preference-sets-the-build-order.md)'s rule that the maintainer's preference sets
  the build order.

## More Information

- Family contract: [`standing-standards`](../contracts/standing-standards.md), adopted by
  [ADR 0032](0032-adopt-standing-standards-family-contract.md).
- The classification precedent this follows on membership, not on classification:
  [ADR 0053](0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md) (`tool`, by the same
  falsifier). The one it argues against on classification:
  [ADR 0058](0058-definition-of-ready-joins-standing-standards-as-a-foundation.md) (`foundation`, on the same
  three markers).
- The family it does not join: [`governance-docs`](../contracts/governance-docs.md), adopted by
  [ADR 0024](0024-adopt-governance-docs-family-contract.md).
- The refusal-record shape considered and not used:
  [ADR 0049 (pi-release-retrospective fails the admission test)](0049-pi-release-retrospective-fails-the-admission-test.md).
- The admission standard for new types:
  [ADR 0030 (templating scope: markdown documents)](0030-templating-scope-markdown-documents.md), and
  [ADR 0048 (one named source clears the admission test)](0048-one-named-source-clears-the-admission-test.md).
- Where the spec, the boundary argument in full, and the admission source table live:
  [`tier2-specs.md`](../tier2-specs.md).
