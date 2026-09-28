---
status: accepted
date: 2026-09-27
decision-makers: [jprisant]
consulted: [claude]
---

# `deployment-plan` clears the admission test and does not ship: its content is already shipped, and no family admits it

## TL;DR

- **Decision:** `deployment-plan` **does not ship**. The library already ships its content in other shapes
  for this library's audience, and all nine family contracts exclude it as written.
- **This is not a zero-source refusal**, and it must not be read as one. Unlike
  [ADR 0049 (pi-release retrospective fails the admission test)](0049-pi-release-retrospective-fails-the-admission-test.md)
  and [ADR 0035 (prototype-brief fails the admission test)](0035-prototype-brief-fails-the-admission-test.md),
  this type **clears** [ADR 0030](0030-templating-scope-markdown-documents.md)'s admission test on five
  named public-sector sources. The admission test asks whether a document exists; it does not oblige the
  library to build every document that does.
- **It answers the question [ADR 0060 (change-request joins delivery-docs)](0060-change-request-joins-delivery-docs.md)
  left open.** That record widened `delivery-docs` with the verb "changes", and the open question was
  whether the widening would become a door. `deployment-plan` is the next candidate whose closest family is
  `delivery-docs`, and it stays out.
- **Who loses:** teams in government or other regulated delivery who must produce a standalone deployment
  plan as a gated deliverable. The record names them in its reopening conditions.
- **Status:** accepted 2026-09-27. The maintainer ruled on the research the same day and accepted this
  record on reading the contract diff, as with [ADR 0059](0059-announcement-internal-comms-joins-delivery-docs.md)
  and [ADR 0060](0060-change-request-joins-delivery-docs.md).

## Context and Problem Statement

The catalog lists `deployment-plan` as a Tier-2 candidate (aliases `rollout plan`, `cutover plan`,
`go-live plan`; category Release / Deployment / Runbooks; relationships `Release Plan`). The shipped
`release-notes` companion names "the release plan and deployment plan (what ships and when)" as upstream of
a release note. A research pass on 2026-09-27 tested the type against ADR 0030's admission test and against
every family contract, with no family assumed. It returned a result no earlier record has had to handle: the
type clears admission, and nothing in the library can honestly hold it.

## Decision Drivers

- **Admission and the build decision are separate questions.** ADR 0030 asks whether a named source
  publishes a type as a written document. Nothing in ADR 0030 or
  [ADR 0048 (one named source clears the admission test)](0048-one-named-source-clears-the-admission-test.md)
  says every admitted type must be built.
- **A decline must be argued on the ground it actually rests on.** Filing this in ADR 0049's zero-source
  shape would misstate what the research found.
- **A family-contract widening stops for the maintainer**
  ([decision-procedures.md, "What always stops for the maintainer"](../decision-procedures.md)), and the
  maintainer ruled against it on 2026-09-27.

## Considered Options

1. **Decline on redundancy and family fit**, with falsifiable reopening conditions. Chosen.
2. **Widen `delivery-docs` again**, as ADR 0060 did for `change-request`, by stretching a verb or adding one.
3. **A new one-member family.** A one-member family is a legal shape (`communication-docs` is one), but a
   family drawn around a document whose content the library already ships holds nothing new.
4. **Defer** until a commercial source keeps the plan as its own document. The targeted search a deferral
   would wait for has already run (below).

## Decision Outcome

**Chosen: option 1.**

### Admission clears, and the record says so

Five named sources publish the type as a written, sectioned document. Each quotation below passed the
raw-text check against the page.

- **US Department of Justice**, *Systems Development Life Cycle Guidance*, Appendix C-20: "The Implementation
  Plan describes how the information system will be deployed, installed and transitioned into an operational
  system".
- **Federal Highway Administration**, *Systems Engineering for ITS*, section 6.9, a "Deployment Plan
  Template": "A Deployment Plan is developed based on a thorough analysis of the steps necessary to achieve
  the deployment goals of the project".
- **US Department of Health and Human Services**, EPLC *Implementation Planning Practices Guide*, read from
  an Internet Archive copy because hhs.gov refuses scripted requests: "Proper implementation planning requires
  documenting these and other items in the form of an Implementation Plan".
- **California Department of Technology**, CA-PMF templates, an "Implementation Management Plan": "Describes
  how the system developed by the project will be implemented in the target environment".
- **US Department of Veterans Affairs**, *Deployment, Installation, Back-Out, and Rollback Guide* (TMP 4.6):
  "This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going
  into the VA Enterprise."

Every one of the five is a US public-sector system development life cycle. That concentration is the first
half of the finding.

### Ground (a): outside that lineage, the content already lives in shapes this library ships or declines

- **IT service management keeps it as two fields on a change record.** The University of Texas's ServiceNow
  instance labels the fields "Detailed plan on how the change will be implemented" and "The steps required to
  restore a system to its original or earlier state", both on the change request itself. The IT service
  change record is the neighbour the `delivery-docs` contract already declines to template: its "changes"
  verb "does not admit a change to a running production system (IT service change enablement, reviewed by a
  change advisory board), which this library names as a neighbour and does not template"
  ([`delivery-docs.md`](../contracts/delivery-docs.md), section 1).
- **SRE and DevOps practice keeps it inside a launch checklist, and this library already ships that
  checklist.** Google's Launch Coordination Checklist (SRE book, Appendix E) carries "Schedule and rollout
  planning" as one of its sections. The shipped `launch-coordination-checklist` full template carries a
  `{{rollout_stages}}` block and a rollback table with the columns Rollback Trigger, Evidence Threshold and
  Authorized To Pull It
  ([`launch-coordination-checklist_template-full.md`](../../../templates/launch-coordination-checklist/launch-coordination-checklist_template-full.md),
  lines 240-244).
- **Commercial release-management vendors fold it into a checklist.** Eight vendor pages were read:
  CloudBees, Octopus Deploy, LaunchDarkly, Aha!, Harness, Stackify, ClickUp and Atlassian. LaunchDarkly
  carries "Create step-by-step deployment plan" as one checkbox of a release checklist, and ClickUp's
  "Deployment Plan Template" is a task board. Only CloudBees describes the plan as a broader document, in a
  single sentence inside a checklist article, with no template. Asana's and GitLab's pages could not be read,
  and the DSDM Agile Project Framework, checked as a control, names no deployment plan product at all.

**This library's POSITION, drawn from that evidence:** for readers in product management and commercial
software delivery, a standalone deployment plan would duplicate the rollout and rollback content of
`launch-coordination-checklist` and the implementation and backout content of an IT service change record.

### Ground (b): all nine family contracts exclude it as written

| Family | Verdict | Why |
|---|---|---|
| `delivery-docs` | Closest, and excluded | Its `phase: deliver` fits, but none of its five verbs (defines, decomposes, verifies, changes, announces) covers planning a release into production, and admitting it would reverse the production-change exclusion quoted above |
| `standing-standards` | Excludes | A deployment plan is written for one release and then finished, the opposite of a standard "agreed once and applied every time" |
| `governance-docs` | Excludes | Its membership section names an event-driven or phase-bound artifact as out of the family |
| `communication-docs` | Excludes | It directs execution; it does not summarise recorded facts for an audience outside the work |
| `decision-docs` | Excludes | It records no technical decision and describes no design; it executes a decided release |
| `qa-docs` | Excludes | Its job is release execution and rollback, not verification |
| `process-docs` | Excludes | It looks forward, not back |
| `discovery-docs` | Excludes | It is written after the build decision, not before it |
| `strategy-docs` | Excludes | It sits at execution detail, not direction |

**The near-miss is the one that matters.** Admitting the type to `delivery-docs` under any verb would put a
production-change artifact inside a family whose contract, amended two days earlier by ADR 0060, excludes
production change by name. One reading would avoid that: frame the plan as the delivery team's own artifact
that feeds a change advisory board's review. No source read in this pass supports that framing, so it would
be the library's invention.

### Consequences

**Good.**

- The type is declined on its real ground, and the record does not misstate a five-source admission as a
  zero-source one.
- The production-change boundary ADR 0060 drew is tested against a real candidate, and it holds.

**Bad, and stated plainly.**

- **Teams in government or regulated delivery lose a template they may be required to produce.** The VA
  guide is a gated deliverable in a real federal life cycle. Those teams will not find it here.
- **The catalog row stays `candidate` and carries no state override**, following ADR 0049's rule: the
  `out-of-scope` value is for a refusal about the medium, and `gen-atlas.py` forces `state_note` to empty for
  any candidate. The decline is therefore discoverable only through this record and the
  [`tier2-specs.md`](../tier2-specs.md) progress table, the same cost ADR 0049 accepted.
- **A catalog alias is missing.** Three of the five sources call the document an "Implementation Plan", and
  no current alias covers that name. The row is left as it is, because an alias edit to a type that does not
  ship would only make a search find a type the library declined.

### What would reopen this, stated so it is falsifiable

Any one of these reopens the question; none requires re-arguing admission, which already stands.

1. **A named commercial source outside public-sector and ERP work publishes a standalone deployment plan**
   and distinguishes it by name from a launch or go-live checklist. That would remove ground (a)'s strongest
   support.
2. **The maintainer chooses to widen `delivery-docs` for this type** and argues through the production-change
   exclusion rather than around it. That is a contract decision reserved for the maintainer.
3. **A real team in regulated or public-sector delivery asks for the standalone document.** A documented
   request is evidence a web search cannot produce.

## More Information

- The research: the admission sweep of 2026-09-27, summarised in the `deployment-plan` row of
  [`tier2-specs.md`](../tier2-specs.md)'s progress table.
- Related records: [ADR 0030 (templating scope)](0030-templating-scope-markdown-documents.md),
  [ADR 0048 (one named source clears the admission test)](0048-one-named-source-clears-the-admission-test.md),
  [ADR 0049 (pi-release retrospective fails the admission test)](0049-pi-release-retrospective-fails-the-admission-test.md),
  [ADR 0060 (change-request joins delivery-docs)](0060-change-request-joins-delivery-docs.md), and
  [ADR 0065 (the steering committee pack is declined)](0065-steering-committee-pack-is-declined.md), decided
  the same day on the same kind of ground.
