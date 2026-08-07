---
title: "Sprint 24 Retrospective Notes"
doc_type: sprint-retrospective-notes
size: lean
sprint: "Sprint 24"
team: "Reporting Squad"
facilitator: "Priya Nair (PM, Reporting)"
status: "final"
doc_version: "1.0.0"
created: "2026-07-24"
updated: "2026-07-24"
related_links:
  - "../sprint-backlog/sprint-backlog_example.md (Sprint 24 Sprint Backlog; the sprint this retrospective looks back on)"
  - "../bug-report/bug-report_example.md (DEF-2291; named below and pointed at this family's incident-postmortem member, not analyzed here)"
  - "../definition-of-done/definition-of-done_example.md (Reporting Squad Definition of Done; the gap DEF-2291 exposed was raised at Sprint 25 planning, not at this retrospective)"
source_template: sprint-retrospective-notes
source_template_version: 0.1.0
---

> **Worked example.** A filled `sprint-retrospective-notes`, the bundle's one shipped size, for Sprint 24 of
> the Reporting Squad at Acme Analytics, the same sprint the
> [`sprint-backlog`](../sprint-backlog/sprint-backlog_example.md) example already forecasts. Per the
> `process-docs` family contract, this document covers that sprint and deliberately does not become an
> account of DEF-2291, the entitlement defect ([`bug-report`](../bug-report/bug-report_example.md)) the
> squad also lived through that sprint: it names the incident, in What Went Well, and points its causal
> analysis at this family's incident-postmortem member instead of narrating it here. Dated 2026-07-24, the
> day Sprint 24 ended, before the [Definition of Done](../definition-of-done/definition-of-done_example.md)
> amendment DEF-2291 triggered was raised, at Sprint 25 planning, not at this retrospective. All figures and
> any named individual beyond those already established in the library's Acme Analytics thread are
> illustrative.

# Sprint 24 Retrospective Notes

## Sprint and Participants

**Sprint:** Sprint 24 (2026-07-13 to 2026-07-24)
**Facilitator:** Priya Nair (PM, Reporting)
**Present:** Priya Nair (PM, Reporting, facilitating), Marcus Bell (Staff Engineer), Mei Lin, and Jordan
Vance - the full three-developer squad. Sofia Marino (Design Systems) was invited for the accessibility
discussion below but was out sick; her finding is relayed secondhand under What To Improve, not from her
own account, and is marked as such there.

## Previous Actions

| Action from previous retrospective | Owner | Status | Note |
|---|---|---|---|
| Write a short design note for the `saved_view` schema before SV-1 starts, so review isn't the first time anyone sees the data model | Marcus Bell | Done | Circulated 2026-07-02; became the Context and Scope section of the Saved Views design doc, with review comments folded in before anyone wrote code against the schema. |
| Schedule the migration dry run and rollback rehearsal before Sprint 24 opens, not after coding starts | Lee Zhang (Data Eng) | Done | Completed 2026-07-09, four days before Sprint 24 opened, with a zero-row reconciliation mismatch; SV-1 built straight on the reconciled schema from day one instead of the team discovering a data problem mid-sprint. |

## What Went Well

| What went well | Why it worked |
|---|---|
| Sequencing SV-1 (storage) ahead of SV-2 and SV-3, exactly as the delivery plan called for | SV-1's repository and CRUD API landed by mid-sprint, so SV-2's save endpoint and SV-3's list-and-switch view could build against the real `saved_view` store instead of a mock. The one piece the sprint backlog flagged as the risk to the whole goal turned out to be the one piece that did not slip. |
| Re-planning the board the same afternoon DEF-2291 was triaged (2026-07-13) | When Anjali Rao suspended phase 2 sharing testing and flagged the entitlement gap, Marcus Bell moved onto the fix that same afternoon instead of waiting for the next Daily Scrum, so the board matched reality by end of day and nobody spent the next morning working against a plan that was already wrong. What the gap actually was, and why it existed, is DEF-2291's own causal analysis; it belongs in this family's incident-postmortem document, not here. |
| The delivery plan's own buffer and cut order worked exactly as written when DEF-2291 landed | The plan set aside roughly a day of slack for the unplanned and named BUG-231 as the first thing to cut if capacity tightened. DEF-2291 cost Marcus Bell more than that one day of buffer mid-sprint, and BUG-231 absorbed the rest exactly as planned, so the Sprint Goal itself never came under threat. |

## What To Improve

| What did not work | Idea to change it |
|---|---|
| BUG-231 stayed "To do" through most Daily Scrums after DEF-2291 ate the buffer, and nobody said out loud it would not make it until two days before sprint end. It felt like giving up on a Must-priority customer bug, even though the delivery plan had already named it the first thing to cut if capacity tightened. | The day unplanned work eats the buffer, name the cut candidate at the next Daily Scrum instead of waiting to see if it somehow still fits. BUG-231 was always the plan's own first cut; saying so on 2026-07-14 would have cost nothing that waiting until 2026-07-22 did not also cost, except two weeks of everyone quietly hoping. |
| The Views control's keyboard and screen-reader check slipped past the test plan's own window, which closed 2026-07-17, and did not happen until the sprint's final week, because Sofia Marino was not booked until the control looked finished. Relayed secondhand: she found one AA-level issue with no time left to fix it, so it went to Priya Nair for a written acceptance instead of a fix, per the test plan's own exit criterion for accessibility. | Book Sofia Marino's walkthrough against the control's first working build, not its "done" build, so a finding surfaces with most of a sprint left to fix it, and inside the test plan's window rather than after it. |

## Action Items

| Action | Owner | Due |
|---|---|---|
| Add "name the cut candidate out loud" as a standing line in the Daily Scrum agenda, starting the first Daily Scrum any unplanned work eats into the sprint's buffer | Priya Nair | 2026-07-27 |
| Carry BUG-231 back to the product backlog for Priya Nair to re-rank against everything else; it did not meet the Sprint Goal and does not roll into Sprint 25 by default | Priya Nair | 2026-07-27 |
| Book Sofia Marino for an accessibility walkthrough of SV-4's default-view control at its first working build, not at "done" | Mei Lin | 2026-07-31 |
