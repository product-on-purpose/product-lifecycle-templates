---
status: accepted
date: 2026-10-13
decision-makers: [jprisant]
consulted: [claude]
---

# `business-continuity-plan` joins `standing-standards` as a `tool`, its sixth member and second unforecast one

## TL;DR

- **Decision.** The `business-continuity-plan` bundle (catalog id `disaster-recovery-business-continuity-plan`;
  issue #263, bundle: disaster-recovery-business-continuity-plan; bundle id by the maintainer's ruling of
  2026-10-13) declares **`family: standing-standards`** and **`classification: tool`**. It becomes that family's
  sixth member, beside `definition-of-done` (`foundation`), `runbook` (`tool`), `launch-coordination-checklist`
  (`tool`), `definition-of-ready` (`foundation`) and `production-readiness-review` (`tool`), and the
  [contract](../contracts/standing-standards.md) moves to `0.5.0`.
- **One bundle, not two, by the maintainer's ruling of 2026-10-13.** The Business Continuity Plan is the primary
  document; disaster recovery is a section inside it, modeled on California's SIMM 5325-A structure, not a sibling
  bundle. A 2026-10-12 gap-fill was run specifically to test whether any named source ships a standalone,
  template-grade Disaster Recovery Plan. Such a plan is distinct from a BCP's own DR appendix. The gap-fill found
  none among the government, standards and practitioner sources it read. That confirms the shape rather than
  deciding it.
- **Why a record is needed.** Like `production-readiness-review` (ADR 0062), this type was never named on the
  contract's "likely future members" list (`standing-standards.md:46`). It is the family's second member admitted
  purely on the membership test and falsifier, with no forecast to confirm.
- **What settled membership:** the family's own falsifier
  ([ADR 0032](0032-adopt-standing-standards-family-contract.md)) is the same test ADR 0053 and ADR 0062 applied. A
  maintained business continuity plan, "tested via failover drills" in the catalog's own words, is consulted at the
  moment of action. A plan written for one disruption after the fact excludes on the contract's own analogy. That
  analogy states: "a runbook written for one incident is an incident report" (`standing-standards.md:37`).
- **What settled classification:** the contract's section 2 cut, "is it a standard you judge against, or an
  instrument you execute?" This is argued marker-by-marker below, on the same reasoning ADR 0062 used for the
  production readiness review.
- **A consequence this record keeps rather than resolves by amendment: the cadence tension.** Section 1 of the
  contract says members are "not revised on a calendar." NIST and a banking regulator's superseded guidance both
  state an annual review-or-test requirement. This ADR records the tension and routes it to the bundle's own Review
  Trigger section, stated as a condition, rather than widening the contract.
- **Status:** accepted 2026-10-13. The maintainer was asked to read the contract diff and this record's admission
  that the authorship half of the `tool` marker is not shown, and replied "Merge then wrap" (PR #278, the spec PR).

## Context and Problem Statement

The 2026-10-12 admission sweep of five queued candidates tested `disaster-recovery-business-continuity-plan`
against its admission evidence and against all ten family contracts, on both axes. Only `standing-standards`
admitted it. Two primary federal sources publish the Business Continuity Plan half of the catalog's merged name as
a written document. NIST SP 800-34 Rev. 1 defines a BCP as "The documentation of a predetermined set of
instructions or procedures that describe how an organization's mission/business processes will be sustained during
and after a significant disruption." FEMA's Ready.gov ships a literal four-page fill-in BCP template. The Disaster
Recovery Plan half clears the admission bar only on NIST's own definition: "A written plan for recovering one or
more information systems at an alternate facility in response to a major hardware or software failure or
destruction of facilities." This is because NIST's own template-building effort went to a different artifact, the
Information System Contingency Plan, not to a standalone DRP.

A second research pass, a gap-fill run on 2026-10-12, was aimed specifically at the one-document-or-two question.
It read US federal, US state and practitioner sources. Among those, it found no named source that ships
a complete fill-in template titled and scoped as a standalone "Disaster Recovery Plan." Such a plan is distinct
from a BCP's own DR appendix. The one template-grade structure found, California's SIMM 5325-A, is explicitly not
titled "Disaster Recovery Plan." California renamed it from "Disaster Recovery Documentation for Agencies
Preparation Instructions" in September 2013, specifically to move away from the disaster-recovery name. The
document itself states it is "just one portion of contingency planning and business continuity." This confirms,
rather than newly decides, the shape the maintainer had already settled before this ADR was drafted. That shape is
one bundle: the Business Continuity Plan as the primary document, with a disaster-recovery section inside it
structured on SIMM 5325-A.

This record exists to make the family and classification calls reviewable rather than asserted, the way
[ADR 0062](0062-production-readiness-review-joins-standing-standards-as-a-tool.md) did for the production readiness
review. That is because [ADR 0032](0032-adopt-standing-standards-family-contract.md) and check K can verify only
that a member picked a value from the set `{foundation, tool}`. They cannot verify that it picked the right one.

## Decision Drivers

- The classification must follow what the document does, per the contract's own cut, not what its strongest
  admission quotation sounds like out of context. That is the same caution ADR 0062 named for the production
  readiness review.
- Family membership (the falsifier) and classification (the cut) are two different questions.
  [ADR 0058](0058-definition-of-ready-joins-standing-standards-as-a-foundation.md) already warns that conflating
  them is the easiest way to get a member wrong.
- This is the family's second member with no forecast to confirm. So the admission argument must rest entirely on
  the membership test as written. That follows
  [ADR 0057](0057-issue-log-joins-governance-docs-as-a-fourth-member.md)'s principle that the membership test, not
  a list of members once predicted, governs a candidate.
- The research surfaced a cadence tension: NIST's and a banking regulator's annual review-or-test language against
  section 1's "not revised on a calendar." That tension needs an explicit answer rather than a silent pass, per
  [decision-procedures.md procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world).

## Considered Options

1. **`standing-standards`, `classification: tool`.** Chosen.
2. **`standing-standards`, `classification: foundation`.** The case for it: the plan's criteria, which functions
   are critical, what recovery strategy is chosen, read as a standard a team is judged against. That is the same
   register `definition-of-done` and `definition-of-ready`'s own admission language uses. Rejected below.
3. **`governance-docs`.** The case for it: a standing, whole-lifecycle instrument. Rejected: that family's
   membership test names "a continuously-maintained register, log, or dashboard" (`governance-docs.md:13`).
   A recovery plan with named procedures and a recovery strategy is none of the three in form. The research's own family-fit dimension scored
   this `excludes`, with no strain needed to reach that verdict. That is a cleaner exclusion than
   `production-readiness-review` got from the same family.
4. **Decline, per the ADR 0049 shape.** Rejected on the evidence: a refusal in that shape needs zero qualifying
   sources. Two named primary sources (NIST, FEMA/Ready.gov) publish the Business Continuity Plan half decisively,
   independent of how the Disaster Recovery half admits.
5. **Two bundles, one for each half of the catalog's merged name.** Not this ADR's call. The maintainer settled one
   bundle before this spec was written. That rests on the gap-fill's finding that no source in the sweep ships the
   two as co-equal, separately structured documents. Recorded here as the option this ADR does not reopen.

## Decision Outcome

**Chosen: `standing-standards` with `classification: tool`.**

### Why the family question was never really in doubt

Read as a maintained plan, this type passes the same falsifier ADR 0053 and ADR 0062 both applied: "if a candidate
arrives that matches the cadence but is not consulted at the moment of action, this family has been drawn around
the axis rather than around a job" (`standing-standards.md:108-110`). The catalog's own notes field already states
the plan is "tested via failover drills." That is a cadence of consultation at the moment an exercise or a real
disruption calls for it, not authorship once and shelving. Read as a one-time record written for one specific
disruption after the fact, the type excludes from every family the research tested, `standing-standards` included.
That follows the contract's own analogy at `standing-standards.md:37`: "a runbook written for one incident is an
incident report." **This bundle is the standing plan**, and any filled instance written for one real event is a
different, narrower artifact this bundle does not template.

### Why `tool`, marker by marker, against the honest `foundation` case

The contract gives each value three markers (`standing-standards.md:80-85`). A production readiness review did not
split cleanly either, and ADR 0062's table is the model this ADR follows rather than picking the convenient row:

| Marker | `foundation` | `tool` | A business continuity plan, with disaster recovery inside it |
|---|---|---|---|
| What it is | "a standard you are judged against" | "an instrument you execute" | Both, on different readings: which functions are critical and what recovery strategy is chosen read as a standard a team's planning is judged against, but the plan itself is executed, under time pressure, once a disruption is declared or a drill begins |
| When and by whom | "argued to, agreed by a team, and changed deliberately and rarely" | "usually under time pressure and often by someone who did not write it" | Split. **When** fits `tool`: the plan's activation, recovery and testing content describes steps run once a disruption is declared or a drill begins, which is this library's reading of the sources rather than a sentence any one of them states. NIST's ISCP sample templates carry a yearly-test attestation line (a structural finding, not rechecked as a quotation). **By whom** is not shown: no source in this sweep says who activates a plan relative to who wrote it, and a business continuity team may both write and run its own plan |
| Where authority comes from | "from having been agreed" | "from being correct right now" | The plan's value is whether its recovery steps and contacts are correct at the moment a disruption hits, present-tense, not whether the team once agreed to a standard and left it alone. NIST's own staleness language ("Certain elements, such as contact lists, will require more frequent reviews") names exactly this failure mode |

**The honest `foundation` case, stated rather than hidden.** A plan's own criteria, which functions are critical
and what RTOs apply to them, read on their own as judged-against language. That is the same register
`definition-of-done` and `definition-of-ready`'s admission quotations use. What breaks the parallel is the timing
half of the second marker. A Definition of Done is applied by the same team that agreed it, to its own work, on a
cadence that team controls. A business continuity plan's criteria may be standing, but activating them happens
under a condition the authoring team does not control. That condition is the moment a disruption is declared or a
drill is run. **The authorship half of that marker is not met on the evidence**, as the table says, so this record
does not lean on it. The `tool` call rests on the timing half and on the third marker. ADR 0062 could point to an
outside reviewer; this record cannot, and says so.

### The cadence tension, recorded as a consequence rather than resolved by amendment

`standing-standards.md` section 1 states members are "not revised on a calendar." NIST states "the ISCP should be
reviewed for accuracy and completeness at least annually." NIST also states "All ISCPs should be reviewed and
tested at the organization defined frequency (e.g. yearly)." The Federal Financial Institutions Examination
Council's Business Continuity Planning booklet states "Testing the BCP at least annually." It was retrieved from
the superseded March 2003 edition, via an FDIC mirror, because the current 2019 edition returned a 403 on both
attempts. All three spans passed the recheck. That is a calendar cadence, plainly, against section 1's own phrase.

**This ADR does not widen the contract to accommodate it.** The contract-mandated Review Trigger section (section
4, required of every member) already asks each member to name a condition rather than a date. That condition is
what event makes the document wrong, and who notices. This bundle's Review Trigger section states the trigger as a
condition, among them a failed test or drill finding, or an actual activation. A third condition is a change to
"key personnel, policies, procedures, facilities, equipment, outsourcing relationships, vendors, or other
components that impact a critical business function." That span is from the FFIEC, and it passed the recheck. The
annual exercise NIST and the FFIEC both name is read here as the plan's own stated condition, restated as a minimum
frequency. That is a floor on how long the condition can go unchecked, not a calendar rewrite of the document's
content. Whether the 2019 FFIEC edition keeps this fixed interval or moves to risk-based language, as unverified
secondary summaries suggest, was not confirmed in this research. That is not needed to reach this reading. **The
tension is recorded here, as a consequence of admitting this member, not argued away.**

### Why not `governance-docs`

`governance-docs.md:13` names three specific forms: "a continuously-maintained register, log, or dashboard".
A business continuity plan, with named recovery procedures and a chosen recovery strategy, is none of the three. It is a plan with activation
and execution content, not a continuously-updated tracked list of open items. The research's own family-fit
dimension recorded this exclusion cleanly, with no strain, unlike the `admits-with-strain` verdict
`production-readiness-review` drew from the same family in ADR 0062.

### The counter-argument this record keeps rather than omits

**No contract's forecast list named this type**, the same gap ADR 0062 recorded for the production readiness
review. `standing-standards.md:46` names only "a coding-standards or engineering-handbook document." A reader who
expects family assignment to track a contract's own predictions would find nothing here to point to, unlike
`launch-coordination-checklist` and `definition-of-ready`. It does not change the outcome, for the same reason ADR
0062 gave: the membership test, not the forecast list, governs a candidate. The tension is recorded so a future
reader sees this family's second unforecast admission was reasoned through the test. It was not waved in on the
precedent the first one set.

**A second counter-argument, specific to this candidate: the catalog's own merged name reads DR and BCP as
synonyms, and the research disagrees.** The gap-fill reports that every source in the sweep that takes a position
places disaster recovery inside or beneath business continuity. NIST's definitions scope a DRP more narrowly than a
BCP. AWS's whitepaper says the same in a sentence that failed the recheck, so it is paraphrased here and carries no
weight on its own. This ADR does not change the catalog id, which stays
`disaster-recovery-business-continuity-plan`. That is the same choice
[the north-star-metrics spec](../tier2-specs.md) made when it kept a bundle id distinct from its catalog id. The
spec's catalog corrections subsection addresses the alias framing; this ADR does not need a further amendment to
state it.

### Consequences

- `standing-standards` grows from five members to six. Its contract's Members line and change note are updated in
  this change. That follows the contract's own requirement that a change to itself carry a decision record.
- Check K gates `classification` membership of the set `{foundation, tool}` and cannot verify this member picked
  the right value. That stays a review obligation. The marker-by-marker argument above is the standard this member
  is reviewed against.
- **The cadence tension is a standing consequence of this admission, not a resolved question.** A future reader of
  the contract should expect the Review Trigger section, not a contract amendment, to be where this tension is
  answered. That holds for every member that carries a numeric industry cadence alongside a condition-based
  trigger.
- **The one-document-or-two question is settled for this bundle's own purposes by the gap-fill, and recorded here
  as evidence the maintainer's prior ruling was sound.** It is not a new finding this ADR makes on its own
  authority. No source in the sweep ships a standalone, template-grade Disaster Recovery Plan. The bundle's own
  Disaster Recovery section, modeled on SIMM 5325-A, matches how the sources that take a position place DR content
  inside a BCP.
- **The classification rests on two of the three markers.** The authorship half of the `tool` marker is not shown
  by any source. If a later reader finds the plan is in practice run only by the team that wrote it, the
  `foundation` case gets stronger. This record is where to reopen it.
- `tier2-specs.md` records this type as specced. The maintainer's read of this ADR, the spec and the contract diff
  together decides whether the build proceeds. That follows
  [ADR 0041](0041-maintainer-preference-sets-the-build-order.md)'s rule that the maintainer's preference sets the
  build order.

## More Information

- Family contract: [`standing-standards`](../contracts/standing-standards.md), adopted by
  [ADR 0032](0032-adopt-standing-standards-family-contract.md).
- The classification precedent this follows most closely, on both membership and classification:
  [ADR 0062](0062-production-readiness-review-joins-standing-standards-as-a-tool.md) (`tool`, the family's first
  unforecast member). The membership precedent on the launch-checklist side:
  [ADR 0053](0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md). The one this record argues
  against on classification: [ADR 0058](0058-definition-of-ready-joins-standing-standards-as-a-foundation.md)
  (`foundation`, on the same three markers).
- The family it does not join: [`governance-docs`](../contracts/governance-docs.md), adopted by
  [ADR 0024](0024-adopt-governance-docs-family-contract.md).
- The refusal-record shape considered and not used:
  [ADR 0049 (pi-release-retrospective fails the admission test)](0049-pi-release-retrospective-fails-the-admission-test.md).
- The admission standard for new types:
  [ADR 0030 (templating scope: markdown documents)](0030-templating-scope-markdown-documents.md), and
  [ADR 0048 (one named source clears the admission test)](0048-one-named-source-clears-the-admission-test.md).
- The precedent for a bundle id distinct from its catalog id: [north-star-metrics](../tier2-specs.md), catalog id
  `north-star-metric-definition`.
- Where the spec, the one-document-or-two argument in full, and the section design live: [`tier2-specs.md`](../tier2-specs.md).
