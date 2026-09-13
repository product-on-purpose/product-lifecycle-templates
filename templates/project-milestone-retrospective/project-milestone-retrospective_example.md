---
title: "Reporting Platform Modernization: Close-Out Retrospective"
doc_type: project-milestone-retrospective
size: full
project: "Reporting Platform Modernization (Acme Analytics)"
author: "Marta Reyes (Program Manager)"
facilitator: "Ravi Menon (PMO; not a member of the programme)"
status: "final"
doc_version: "1.0.0"
created: "2026-10-09"
updated: "2026-10-09"
related_links:
  - "../kpi-dashboard/kpi-dashboard_example.md (programme KPI dashboard; the planned column of every measure below is read from it)"
  - "../risk-register/risk-register_example.md (programme risk register; R-01, R-02, R-04, R-05, R-06 and the appetite lines this document scores against)"
  - "../raid-log/raid-log_example.md (programme RAID log; ISS-11, ISS-12, A-02, D-01 and D-02)"
  - "../status-report/status-report_example.md (the 14-28 July fortnightly report to the same steering group; the last one before close is its successor)"
  - "../incident-postmortem/incident-postmortem_example.md (DEF-2291; named here as an event and deliberately not re-analysed)"
  - "../sprint-retrospective-notes/sprint-retrospective-notes_example.md (Sprint 24 retrospective; a cadence review of how one squad worked, which is a different document doing a different job)"
  - "../product-backlog/product-backlog_example.md (Saved Views product backlog; where two actions below are tracked)"
source_template: project-milestone-retrospective
source_template_version: 0.1.0
---

> **Worked example.** A filled `project-milestone-retrospective`, **full** variant, for the
> **Reporting Platform Modernization** programme at Acme Analytics, the same programme the
> [`kpi-dashboard`](../kpi-dashboard/kpi-dashboard_example.md),
> [`risk-register`](../risk-register/risk-register_example.md),
> [`raid-log`](../raid-log/raid-log_example.md) and
> [`status-report`](../status-report/status-report_example.md) examples already cover while it was running.
> Those documents managed the work. This one closes it.
>
> **Full rather than lean, for the reasons the guide gives:** the readers can fund or stop what comes next,
> a prior review of this same system exists and its findings needed checking, and the programme was closed
> formally against a baseline. That is why it carries a Previously Identified Issues section and a
> planned-against-actual table the lean variant does not have.
>
> **Read the dates.** The programme closed on 2026-09-30; the session ran on 2026-10-07 and this write-up is
> dated 2026-10-09, which is why everything it cites is older than it. The planned values are read from
> siblings that already exist, the actuals are this example's own, and **every figure, identifier and date is
> illustrative**, as are Ravi Menon, the backfill contractor and the predecessor programme's close-out review.
>
> **It is deliberately not its two siblings, and says so in its own Scope and Period.** It is not
> [Sprint 24's retrospective](../sprint-retrospective-notes/sprint-retrospective-notes_example.md), which
> looks back on a two-week period at how one squad worked and feeds that squad's next sprint. It is not
> [DEF-2291's postmortem](../incident-postmortem/incident-postmortem_example.md), which is event-triggered
> causal analysis of one failure. This document is triggered by an ending, covers eight months of bounded
> work, and is written for readers who were not in the room and in some cases were never on the programme.
>
> One convention to flag: two actions below are tracked in the programme risk register and a successor
> programme's RAID log. Per the `process-docs` family contract, the ordinary ticket tracker is the
> destination published practice actually names; the register and the log are this library's own convention.

# Reporting Platform Modernization: Close-Out Retrospective

## Scope and Period

**Work reviewed:** the Reporting Platform Modernization programme at Acme Analytics, from programme board
approval on 2026-02-16 to formal close on 2026-09-30. Three deliverables sat inside it: the Saved Views
capability, the migration of saved-view configurations from the legacy key-value store onto the new schema,
and the query-engine handoff from the Platform team.

**Period:** 2026-02-16 to 2026-09-30.

**Deliberately outside this review:** the causal analysis of DEF-2291, which has its own
[postmortem](../incident-postmortem/incident-postmortem_example.md) and is named below as an event rather
than argued again here; how the Reporting Squad worked sprint to sprint, which belongs to its own cadence
retrospectives; the Recommendations programme's own delivery, which is under way and reports separately; and
the charting vendor's commercial terms, which Legal holds and reviews on its own cycle.

**Who reads this:** the programme steering group, and Priya Nair in her incoming role as product lead of the
Recommendations programme, which inherits this system and its telemetry under RAID log dependency D-02.

**What they decide with it:** two decisions, both still ahead of the reader. First, at the 2026-11-06
steering review, whether the platform-level entitlement-aggregate control is funded inside the
Recommendations programme's scope before saved-view telemetry begins leaving its source workspace, or whether
the accepted residual stands. Second, on 2026-11-13, when the 60-day launch-success window closes, whether
the remediation sprint reserved by risk R-04, the adoption risk, is triggered. Both decisions turn on
material below, which is why this document leads with measures and boundaries rather than with what the room
felt.

**Circulation, agreed before the discussion:** settled on 2026-09-28 with the invitation, nine days before
anyone spoke. This document goes to the steering group, the programme's workstream leads and the PMO library,
and any Acme employee may read it. Two things are deliberately not in it: the personnel circumstances behind
the query-engine lead's departure, and the vendor's commercial terms. A narrower note on the first exists and
is held by Marta Reyes with HR. Everyone in the room knew all of this before they spoke, which is the point of
settling it in advance rather than at publication.

**Who contributed, and who could not be reached:** nine of the eleven workstream contributors attended the
session on 2026-10-07, facilitated by Ravi Menon of the PMO, who was not on the programme. The backfill
contractor's engagement ended at close and his account arrived in writing beforehand. The query-engine lead,
whose departure is logged as ISS-11, was not approached. That is the largest gap in this record: why the
predecessor programme's handover guide stopped where it did is reconstructed here from the documents and from
colleagues, and not from the one person who knew.

## What Happened

The programme was approved on 2026-02-16 to cut the median Time to Insight for Recurring Analysts by 30
percent by the end of Q3, with Saved Views as the headline deliverable. Saved Views reached general
availability for all Recurring Analysts on 2026-09-14. The saved-view configuration migration cut over on
2026-09-11 and the legacy key-value store was held read-only until 2026-10-11, as the agreed mitigation for
risk R-02, silent configuration loss on migration, specified. The query engine arrived from the Platform team
on 2026-08-21, against the 2026-08-01 date carried on the RAID log as dependency D-01, which is 15 working
days later. The programme closed on 2026-09-30, its planned date.

Two events during the programme have their own documents. DEF-2291, an aggregate that disclosed data across an
entitlement boundary, was found on staging on 2026-07-13 by a planned test, suspended Phase 2 sharing testing
for two days, and was fixed and verified on 2026-07-15; its causes are in the
[postmortem](../incident-postmortem/incident-postmortem_example.md) and are not restated here. The
query-engine lead's departure was logged as ISS-11 on 2026-06-14 with the handover incomplete. The backfill
contractor budget of GBP 45,000 was approved on 2026-08-10, past the issue's own 2026-07-31 resolution target
and past the RAID log's two-week escalation ageing line; the contractor started on 2026-08-17, and Lee Zhang
signed off the handoff on 2026-08-21 covering deployment and the schema, with the query planner recorded as
not covered.

Four tracked items closed or landed during the period. R-05, the entitlement-exposure risk, was escalated to the
steering group on 2026-07-14 and its residual was formally accepted on 2026-08-17, 34 days later, with the
platform-level control deferred rather than funded. R-01 closed on 2026-08-12 when the charting vendor renewed
on existing terms; the fallback rendering path the register had budgeted for was never started. ISS-12, the
view-list load issue, closed on 2026-09-02 when the production p95 first read under the 500ms budget. The
outbound telemetry dependency D-02 was delivered to the Recommendations team on 2026-09-23, ahead of its
2026-09-30 date.

After cutover, three saved views using the legacy relative-date syntax reconciled clean and rendered
differently from their pre-cutover form. Their owners reported them within four days and Data Eng repaired all
three from the read-only legacy store by 2026-09-18. No other configuration defect was reported between
cutover and close.

*(All figures illustrative. Planned values are read from the programme KPI dashboard and risk register as they
stood at their 2026-07-20 review; actuals are readings taken in the week ending 2026-09-30 unless the row says
otherwise.)*

| Measure | Planned | Actual | Where a reader can check it |
|---|---|---|---|
| Time to Insight, the outcome the programme was commissioned on | 30 percent faster than the FY26 baseline by end Q3; 25 percent was the separate green line | 26 percent faster at close. It cleared the green line and missed the commitment | [KPI dashboard](../kpi-dashboard/kpi-dashboard_example.md) definition, computed from the product analytics event stream; Looker executive view |
| Saved Views adoption | 60 percent of Recurring Analysts weekly by end Q3 | 48 percent, read on day 16 of the 60-day launch-success window. The window's own final reading falls on 2026-11-13, after this document and after the team | Entitlements database and event stream, per the dashboard's locked definition |
| View-list load, p95 | Under 500ms | 430ms in the week to close, from 620ms at the July review | Front-end RUM pipeline; the metric ISS-12 moved |
| Weekly active analysts, the guardrail | Hold at 480 or more | 502 | Same nightly pipeline as adoption |
| Migration integrity at cutover | 100 percent of in-scope legacy configurations reconciled | 100 percent, on 14,812 configurations | Output of the R-02 dual-write reconciliation script, cutover run of 2026-09-11 |
| Configuration defects reported after cutover | None expected once the gate above read 100 percent | 3 views, all repaired by 2026-09-18 | Support queue, tagged to the cutover window |
| Schedule slip on the critical path | The programme's stated appetite is a slip of up to two weeks, that is 10 working days | 15 working days on D-01. The close date did not move; general availability did | RAID log D-01 against the appetite section of the [risk register](../risk-register/risk-register_example.md) |
| Unplanned cost | Appetite of GBP 100,000 | GBP 45,000, the backfill contractor, and nothing else | Steering minutes of 2026-08-10; ISS-11 |

## What Worked

| What worked | Why it worked | How someone else repeats it |
|---|---|---|
| Dual-writing configurations during the transition and holding the legacy store readable for 30 days after cutover | The reconciliation proved the counts matched; the read-only window is what made the three broken views a four-day repair instead of a reconstruction from memory. The mitigation that mattered most was the one that assumed the check could miss something | Keep the source store readable for a fixed window after cutover and say in advance who may read from it. Budget the window as part of the migration, not as contingency, because its value only appears when the gate has already reported success |
| Paginating and lazy-loading the view list, then load-testing at three times the expected view count before general availability | The test ran against a volume no analyst had yet produced, so the 620ms reading in July became a production problem on paper before it became one in use. p95 read 430ms in the week to close | Load-test against a multiple of expected volume rather than today's volume, and measure the same way the user experiences it. This programme kept a client-side measurement, which includes network time Acme does not control, precisely so the number would not flatter the server |
| Amending the squad's Definition of Done on 2026-07-24 so that any change touching entitlement logic re-runs the full permission matrix | It moved a check from a risk-tier test that ran once per phase onto every change, so the next occurrence of that defect class is caught by the change that causes it rather than by the calendar | When a defect class is caught by a scheduled test, move the check onto the change rather than adding another scheduled test. The trigger is the thing to fix, not the coverage |
| Settling circulation before the retrospective session rather than at publication, and naming what a narrower note covers | Contributors knew who would read this before they spoke, so nobody had to guess how frankly to describe the handover failure, and nobody had to discover the constraint afterwards. The one genuinely sensitive topic was fenced by name rather than by omission | Decide who may read the document before the invitation goes out, and where something must stay out, say in the document that a narrower account exists and who holds it. Silence about a gap reads as an absence of findings |

## What Did Not

| What did not work | Why it happened | What would have prevented it |
|---|---|---|
| The programme closed on 2026-09-30 with its own success window still running. The number it was commissioned on, adoption at 60 percent, will not exist until 2026-11-13, six weeks after the team dispersed | The close date was anchored to the Q3 commitment and the success window was anchored to general availability plus 60 days. When the query-engine dependency D-01 slipped 15 working days, general availability moved and the close date did not, so the gap between them closed to 16 days without anyone deciding it should | Anchoring close-out to general availability plus the measurement window at charter, so a delivery slip moves both dates together. Failing that, a named reader for the final measurement, agreed at charter rather than improvised at close |
| The decision to fund the backfill contractor sat past the RAID log's own two-week escalation ageing line and past the issue's 2026-07-31 target, and was taken on 2026-08-10. The query-engine handoff, and with it the critical path, waited on it | The ageing line reported the delay and did nothing about it. Escalated items moved at the pace of the monthly steering slot, so an item that missed a slot waited for the next one regardless of how old the log said it was | An automatic consequence on the ageing line: at 14 days an item joins the board's exception list without waiting for a steering slot. The ageing column was accurate throughout and had no effect on anything, which is the problem |
| The migration gate reported 100 percent and three views still behaved differently after cutover | The migration-integrity metric matches on configuration identifier and field count, not on semantic equivalence of every field. That limitation was written into the dashboard specification when the metric was locked, and it was not carried onto the line where the gate result was reported, so the number was read at close as though it meant every view behaved the same | Printing the limitation beside the result wherever the gate is reported, not only where the metric is defined. Nothing about the gate itself needed to change; what needed to change is what a reader sees next to the number |
| The design-partner pilot on 2026-08-05 predicted the adoption shortfall and changed nothing before general availability. Six analysts were observed rebuilding filters by hand with a save control visible on screen; the finding reached the backlog and was not funded before launch | No capacity was reserved for acting on the pilot's findings. The pilot was scheduled to test assumption A-02, that analysts want saved views enough to change a habitual workflow, and the plan around it assumed the answer would be yes, so there was room to run the test and no room to respond to it | Reserving build capacity for the pilot's outcome before the pilot runs, sized against the change it could plausibly demand. A test whose only possible consequence is a backlog item is an observation, not a gate |

## Previously Identified Issues

Ordered as the template asks: the issue that was declared closed and recurred comes first, then the one that
is open and leaving this programme, then the one that was knowingly accepted and materialised at the small end.

| Issue, as it was written then | Where and when it was raised | Action that was agreed | What actually happened | Status now |
|---|---|---|---|---|
| "The query planner has a single maintainer and no written handover. If he leaves, nobody can change it safely" | Close-out retrospective of the Query Engine Consolidation programme, 2026-01-22, lesson 3. Filed in the PMO wiki archive; its page had been opened twice between filing and this programme's planning, both times by its own author | A maintainer guide, and a second engineer paired onto the engine, by 2026-03-31 | The guide was written and covers deployment and schema. The query planner section was never started. The action was closed as complete on 2026-04-02 against the existence of the guide, not against what it covered. The lead's departure was logged on 2026-06-14 with the handover incomplete, as ISS-11 | **Recurred.** It is the cause behind the D-01 slip in What Did Not, and behind the fourth lesson below, on closing an action against coverage rather than against a deliverable. The unwritten section is now action 3 below, the query planner guide |
| "A shared saved view can disclose data across an entitlement boundary. Fund a platform-level entitlement-aggregate control, or accept the residual formally at board level" | Raised at DEF-2291's triage on 2026-07-13 and escalated to the steering group on 2026-07-14; carried on the register as R-05, above the near-zero appetite line for this risk class | One of two outcomes: funding for the control, or formal acceptance of the residual | Neither happened for 34 days. On 2026-08-17 the residual was formally accepted and the control was deferred to a future programme's scope, where it is currently in nobody's budget | **Open, and transferred.** The residual acceptance stands and the control does not exist. It is action 1 below, funding or re-presenting the control, and the first thing the 2026-11-06 steering review has to settle |
| "Reconciliation matches on configuration identifier and field count, not semantic equivalence of every field" | Recorded as the migration-integrity metric's own known limitation when the dashboard specification was locked, 2026-07-20 | None. The limitation was accepted knowingly as the price of an automated cutover gate, in preference to a manual check that could not cover every configuration | It materialised at the small end: three views, reported by their owners within four days, repaired from the read-only legacy store by 2026-09-18 | **Closed, and knowingly accepted rather than missed.** The gate is unchanged and should be. What changes is where the limitation is printed, which is action 5 below, the gate report line |

## Lessons for Others

| Lesson | Who it is for | What to do differently |
|---|---|---|
| A lesson that exists only as a filed document is not a lesson. The handover failure that cost this programme 15 working days on its critical path had already been written down, accurately, eight months earlier, in a document of exactly this type that nobody opened | The PMO, and whoever writes or commissions the next close-out of any Acme system | Present the previous close-out for the same system at the next programme's kickoff, as an agenda item with a named presenter. Add "what did the last close-out of this system say" to the charter checklist, so retrieval is somebody's task rather than an act of initiative by a stranger who does not know the document exists |
| A close date and a success measure can be anchored to different events, and nobody notices until the close date arrives with the measurement still running | Any programme whose success is a behaviour change measured after launch, in or outside this organisation | At charter, write the close date as launch plus the measurement window, or name in the charter the person who reads the final number after close and what they are expected to do with it. Deciding it at close means deciding it when the people who would act on it have already been assigned elsewhere |
| A completion gate is only as strong as the comparison underneath it, and the cheapest insurance is keeping the old thing readable | Any team migrating configuration or data between stores | Print the comparison's known limitation next to the gate result, and keep the source readable long enough to repair what the comparison cannot see. In this migration the 30-day read-only window, not the 100 percent reading, is what made the defects cheap |
| An action closed because a deliverable exists has not been closed. The predecessor's handover guide existed, was signed off, and did not cover the part that mattered | Anyone at Acme who signs off corrective actions: programme boards, the PMO, workstream leads | State the coverage test when the action is agreed, not when it is reviewed, and close against that test. For a handover guide the test is cheap and specific: an engineer who has never touched the component makes a scoped change using only the guide |

## Actions and Owners

Ordered so that the actions which must outlive this programme come first. Every owner below confirmed on
2026-10-07 that they hold the row after close; the programme itself no longer exists to chase them, which is
the condition this section is written for.

| Action | Owner | Due | Tracked in |
|---|---|---|---|
| Put the platform-level entitlement-aggregate control into the Recommendations programme's funded scope before saved-view telemetry begins leaving its source workspace; if it is not funded by then, re-present the accepted residual to the board as a standing exposure rather than a closed item | Sam Okafor | 2026-11-06 | Risk register R-05, mirrored onto the Recommendations programme's RAID log |
| Take the final Saved Views adoption reading when the 60-day launch-success window closes, and tell the steering group whether the remediation sprint reserved by risk R-04, the adoption risk, is triggered | Priya Nair | 2026-11-13 | Product backlog SV-21, and the KPI dashboard's November review |
| Write the query planner section of the query-engine maintainer guide, and close it against an agreed coverage test: an engineer who has not worked on the planner makes a scoped change using only the guide | Lee Zhang | 2026-12-04 | Platform team backlog PLAT-207 |
| Present this retrospective at the Recommendations programme kickoff, and add a "last close-out for this system" line to the PMO charter checklist so the next programme does not have to think of it | Marta Reyes | 2026-10-30 | PMO charter checklist v4 |
| Print the migration-integrity limitation on the line where the gate result is reported, not only in the metric definition | Lee Zhang | 2026-10-23 | KPI dashboard specification change DE-118 |
| Propose to the PMO that the escalation ageing line carries an automatic consequence at 14 days, and bring the proposal with this programme's own D-01 evidence attached | Ravi Menon | 2026-11-27 | PMO governance backlog GOV-44 |

*(All identifiers, dates, figures and names above are illustrative.)*
