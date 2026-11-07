---
title: "Saved Views for Dashboards Requirements Traceability Matrix"
product: "Saved Views for Dashboards (Acme Analytics, Reporting Platform Modernization)"
owner: "Anjali Rao (QA Lead, Reporting)"
created: "2026-07-20"
last_reconciled: "2026-07-20"
status: "active"
related:
  - "../prd/prd_example.md (Saved Views for Dashboards PRD, version 0.3.0; the requirement set this matrix covers)"
  - "../test-plan/test-plan_example.md (the test plan whose risk-ranked areas the Verified by column names)"
  - "../test-summary-report/test-summary-report_example.md (the final 2026-07-17 report whose counts and acceptances every status below rests on)"
  - "../test-case/test-case_example.md (TC-047, the case that traced to a risk and to no requirement)"
  - "../bug-report/bug-report_example.md (DEF-2291, closed, found by TC-047 step 4)"
  - "../risk-register/risk-register_example.md (the register that owns R-05, R-06 and R-02)"
  - "../acceptance-criteria/acceptance-criteria_example.md (the default-view criteria that DEF-2298 misses)"
  - "../epic/epic_example.md (the SV-n stories that serve each requirement, which is why Implementation Trace is N/A)"
  - "../incident-postmortem/incident-postmortem_example.md (the DEF-2291 postmortem, dated 2026-07-16)"
  - "../sdd/sdd_example.md (the design document that refers to the PRD security NFR)"
  - "../kpi-dashboard/kpi-dashboard_example.md (the dashboard that carries R-06's 500ms budget)"
  - "../issue-log/issue-log_example.md (ISS-12, the same view-list problem under Dana Osei)"
doc_type: requirements-traceability-matrix
size: full
source_template: requirements-traceability-matrix
source_template_version: 0.1.0
---

> **Worked example.** A filled `requirements-traceability-matrix`, full variant, for the Reporting
> Platform Modernization program at the fictional Acme Analytics. It is the same program, and the same
> Saved Views feature, that the [`prd`](../prd/prd_example.md), [`test-plan`](../test-plan/test-plan_example.md),
> [`test-case`](../test-case/test-case_example.md),
> [`test-summary-report`](../test-summary-report/test-summary-report_example.md),
> [`bug-report`](../bug-report/bug-report_example.md) and
> [`risk-register`](../risk-register/risk-register_example.md) examples already cover.
> `requirements-traceability-matrix` joined the `governance-docs` family as its eighth member on 2026-11-05
> under
> [ADR 0084 (the requirements traceability matrix joins governance-docs as an eighth member)](../../docs/internal/decisions/0084-requirements-traceability-matrix-joins-governance-docs-as-an-eighth-member.md).
>
> This matrix is dated **2026-07-20**, the first working day after the test summary report closed on
> 2026-07-17. Everything it cites existed by then, including the PRD, the epic, the product backlog, the
> test plan, TC-047, the bug report, the DEF-2291 postmortem, the risk register and the test summary report.
> It does not cite the
> `change-log` example of 2026-08-17. That log records that the PRD stayed at version 0.3.0, which is why
> this matrix labels the PRD's non-functional rows itself and does not edit the PRD.
>
> **What this example does and does not show.** It shows the shape of a matrix and the discipline of its
> status words. It does not argue that an unregulated team should keep one. This bundle's research found no
> named software team outside regulated or safety-critical work that describes keeping its own matrix, and
> nothing it read shows that a matrix improves outcomes. The team below makes a narrow, time-limited choice
> for one feature. NASA's software handbook describes the same bargain for projects with small budgets:
> value-based tracing that focuses the effort on the most important requirements. Read the Purpose and
> Boundary section first, and read the stop condition as part of the document.
>
> Counts, builds and defect states come from the test summary report as it stood at 2026-07-16 17:00 UTC.
> Every figure marked "illustrative" is made up for the example. All names, paths and dates not already
> fixed by the library's Acme Analytics thread are illustrative too. Acme is not regulated, and nothing in
> this example is a regulation or a contract that requires a matrix.

# Saved Views for Dashboards Requirements Traceability Matrix

## Purpose and Boundary

**Product and requirement set covered:** Saved Views for Dashboards, phases 1 and 2. The set is the six
functional requirements FR-1 to FR-6 and the four rows of the non-functional table in the
[PRD](../prd/prd_example.md), version 0.3.0. That is ten rows, and nothing else in the product.

**Not traced:**

- The dashboard permissions service. Platform owns and tests it, and this matrix traces only this feature's
  use of it.
- Adoption (R-04 on the register). It is measured on the KPI dashboard after launch, and a test cannot
  verify it.
- The legacy report flow, which the standing regression suite covers.
- The PRD's goals, UX states, success metrics, instrumentation list and rollout plan. The scope rule below
  explains why.
- Individual cases. Only five case IDs appear below. Every other row names a test plan area, because the
  run record already lists the cases.

**Kept by:** Anjali Rao, QA Lead for Reporting.

**The record:** This file is the record for one thing: the link from each PRD requirement to the cases or
the test plan area that verify it, and the status of that link. The PRD owns the requirement text. The
product backlog owns the work, and each story in the Saved Views epic names the requirement it serves.
The sprint 14 run record in the test tool owns the case results. The risk register owns every risk score.
This file copies none of those. What it adds is the whole-set view. The team's reasoning is that a
requirement with no test has no test record to carry a link to it, so a whole-set table is where that
requirement shows up.

**Why this team keeps a matrix:** R-05 (a shared view exposing personal data to a viewer without
entitlement) sits above the program's PII appetite line. It has been with the steering group since
2026-07-14, waiting on one decision: fund a stronger entitlement control, or accept the residual formally.
Shared-view entitlement was the first-ranked area in the test plan, and TC-047 (a restricted viewer opening
a shared view) found DEF-2291 (the aggregate that disclosed data across an entitlement boundary). Yet no
document pairs the PRD's permissions row with the cases that test it, because that row has no identifier.
The steering group will decide on the strength of how well the control is verified. So the team wants one
page that says which requirement states the control and what verifies it. The matrix covers one feature,
holds ten rows and is kept by hand, because one person can reconcile ten rows against four documents in a
sitting.

**When it will stop:** When two things have both happened: the steering group has decided R-05, and the
gradual rollout in the PRD has reached 100 percent. At the next reconcile after that, Anjali Rao takes a
last baseline, marks this file closed in Upkeep and stops updating it. The exception is a line from Priya
Nair, added here with a reason, saying it continues. Any finding the team still needs moves into the test
plan for the next release.

## Trace Conventions

**Requirement identifiers:** FR-1 to FR-6 are the PRD's own, unchanged. The PRD's non-functional table has
no identifiers. This matrix labels its four rows NFR-1 to NFR-4 in the PRD's table order: Performance,
Permissions, Reliability, Accessibility. The labels exist only in this file. The PRD stays at version
0.3.0, and Priya Nair decides whether its next revision adopts them.

**Test identifiers:** TC-nnn, as numbered in the test tool, for a case that is individually tied to a
requirement or a risk. The thread holds five of them: TC-046, TC-047, TC-048, TC-052 and TC-053. Every other
row names the test plan's risk-ranked area, with the planned, executed and passed counts the test summary
report gave on 2026-07-16 at 17:00 UTC. Those counts are a reading at one moment, and the run record is the
live source.

**What counts as a requirement:** Each row of the PRD's functional requirements table and each row of its
non-functional requirements table, at version 0.3.0. Goals, non-goals, UX states, success metrics,
instrumentation and rollout steps are not counted, because the team did not treat them as statements to
verify one by one. Stories and acceptance criteria are not counted either. They refine a requirement, and
they are reached through the requirement they serve.

**What counts as verified:** Every case the test plan planned for the requirement ran and passed. The pass
was on the release build, 2.3.2, or on the earlier build 2.3.1 with a named person's acceptance of that
earlier result for 2.3.2 recorded in the test summary report. Every defect raised against the requirement
is closed, or is accepted in that report by a named person. A case that exists does not make a row
verified. A case that is blocked, not run or failing leaves the row Partly verified or Test linked.

**Verified by other means:** None of the ten requirements rests on a review or an analysis alone, so the
Other means status below is defined and unused. The one review this release held, Sam Okafor's security review of 2026-07-10, gated phase 2 testing. It is
named in NFR-2's notes and does not stand in for the tests.

**Links that are not one-to-one:** One requirement may name several cases or areas, and one case or area
may serve several requirements. NFR-2 names four cases. The View-list load performance area serves both
FR-2 and NFR-1. A link is read in both directions from the Verified by cells.

| Status | What it means in this matrix |
|---|---|
| No verification | Nothing is linked: no case, area or other-means record names the requirement. It is a finding and goes to Coverage Gaps. No row holds it at version 1 |
| Test linked | A case or area is named, but this matrix holds no passing result for it. The case has not run, or its result has not been read into this file |
| Partly verified | Some planned cases passed and at least one did not. It failed, was blocked or was never run. The row says which, and who accepted what is open |
| Verified | The definition above is met |
| Other means | Checked by review, analysis or demonstration, with the record named. No row holds it at version 1 |
| Deferred | The requirement is not built in this release. The row carries the reason, and the status goes when the requirement is built |

## The Matrix

| Requirement ID | Requirement (short label) | Source | Verified by | Status | Notes |
|---|---|---|---|---|---|
| FR-1 | Save the current dashboard state as a named view | [PRD](../prd/prd_example.md), functional table | The save cases in the sprint 14 run record. The test plan names no area for them | Test linked | Must. The plan and the report count by area, so no pass count for save can be read from them. Open in Coverage Gaps |
| FR-2 | List saved views and switch between them in one action | [PRD](../prd/prd_example.md), functional table | The list and switch cases in the run record. Switch timing is also measured in the View-list load performance area | Test linked | Must. Same open item as FR-1. The timing result is carried under NFR-1. DEF-2304 (S2, open) is a finding against R-06's 500ms budget, which no numbered requirement carries, so this matrix does not count it against FR-2 |
| FR-3 | Set one view as the default for a dashboard | [PRD](../prd/prd_example.md), functional table | Default-view resolution area: 14 planned, 13 executed, 13 passed, 1 blocked. Run on 2.3.1 only | Partly verified | Must. The blocked case needs a mid-session access revocation that Platform has not scheduled. 9 of the 14 come from the [acceptance criteria](../acceptance-criteria/acceptance-criteria_example.md) and 5 from test design. Priya Nair accepted the 2.3.1 result for 2.3.2. DEF-2298 (S3, open) misses the criterion that a view with a deleted filter names it; see NFR-3 |
| FR-4 | Share a view so other permitted users of the dashboard can select it | [PRD](../prd/prd_example.md), functional table | Shared-view entitlement area: the 12-combination permission matrix, 12 of 12 passed on 2.3.2, including TC-046 (fully entitled recipient) | Verified | Should. The matrix ran in full on 2.3.2 after DEF-2291 (S1, closed). See NFR-2 |
| FR-5 | Rename and delete views the user owns | [PRD](../prd/prd_example.md), functional table | Rename and delete area: 8 planned, 8 passed. Run on 2.3.1 only | Verified | Should. Priya Nair accepted the 2.3.1 result for 2.3.2 in the report's residual-risk table |
| FR-6 | Indicate when a shared view's dashboard has changed in a way that affects it | [PRD](../prd/prd_example.md), functional table | None | Deferred | Could. It was not built in this release, so the test plan deferred it with the requirement and there is nothing to test |
| NFR-1 | Switching to a view renders in under 1s at p95 (illustrative target) | [PRD](../prd/prd_example.md), non-functional table | The view-switch cases in the View-list load performance area, run on the pre-prod replica at 2.3.2. p95 0.74s (illustrative) | Verified | The 500ms view-list budget is not in this PRD row. It belongs to risk R-06, and DEF-2304 (S2, open) is against that budget, not against NFR-1. See Risk Control Trace |
| NFR-2 | A shared view never exposes data the recipient could not already access | [PRD](../prd/prd_example.md), non-functional table | TC-046, TC-047 and TC-048, the three entitlement partitions of the permission matrix, all passed on 2.3.2 | Verified | ID assigned in this file, see Coverage Gaps. DEF-2291 was found by TC-047 step 4 and closed in 2.3.2. TC-047's rendered-UI step is manual, once per release, and Sam Okafor accepted that in the report. TC-053 was added on 2026-07-15 to guard the row-count badge on the same path, and its own result is in the run record, not here. The 2026-07-10 security review preceded the tests and is not counted as verification |
| NFR-3 | A view that references a deleted filter loads what it can and flags the rest | [PRD](../prd/prd_example.md), non-functional table | TC-052, in the Stale-field degradation area: 9 executed, 8 passed, 1 failed | Partly verified | TC-052 raised DEF-2277 on 2026-07-08, fixed and re-verified on 2.3.2. The failed case is DEF-2298 (S3, open): the notice gives a count and does not name the filters. Priya Nair accepted it on 2026-07-16 and deferred it |
| NFR-4 | The Views control is keyboard-operable and screen-reader labeled (WCAG 2.2 AA) | [PRD](../prd/prd_example.md), non-functional table | Accessibility area: 14 planned, 11 executed, 10 passed, 1 failed, 3 not run | Partly verified | NVDA on Windows is complete. The VoiceOver on macOS pass never started and has no owner or date. DEF-2286 (S3, open) was accepted in writing by Priya Nair on 2026-07-16. DEF-2284 was fixed in 2.3.2 |

## Coverage Gaps

On 2026-07-20 the five case IDs this matrix names were checked against the requirements, the backward
direction. TC-047 was the one whose own record names a risk and no requirement. TC-046, TC-048, TC-052
and TC-053 were placed by what each verifies. Cases named only by area were not checked backward, which is
the third row below.

| Gap | ID | Owner | Decision | Notes |
|---|---|---|---|---|
| Requirement with no identifier, so no row | The PRD's Permissions row, now NFR-2 | Anjali Rao | Assigned NFR-2 in this file and traced TC-046, TC-047 and TC-048 to it. The PRD is unchanged, and Priya Nair decides whether its next revision adopts NFR-1 to NFR-4 | The row is in the PRD at version 0.3.0. The design document refers to it as the PRD security NFR. The bug report and the postmortem do not point at it, and it had no number to point at. SV-9 (an acceptance criterion for what a partially entitled recipient sees inside an aggregate) is still proposed, and should name NFR-2 as its parent when written |
| Test with no requirement | TC-047 | Anjali Rao | Resolved by the row above. TC-047 now traces to NFR-2 as well as to R-05 | Its record names R-05 and states that no acceptance criterion covers it. It names no requirement |
| Requirement with no recorded result | FR-1 and FR-2 | Anjali Rao | Read the save and the list-and-switch cases in the run record, copy their IDs and results here, and move each row to Verified or leave it with the defect named. Done before the next reconcile | The test plan scopes save, list and switch but ranks no area for them. This is also the backward check for the cases named only by area |
| Planned cases never executed | FR-3 (1 blocked case) and NFR-4 (3 VoiceOver cases) | Dana Osei for the access-revocation slot, and Marta Reyes for the VoiceOver reviewer | Both asks are open in the test summary report's Impediments section. This row mirrors their state and holds no separate decision | The rows stay Partly verified until the cases run |
| Risk with no controlling requirement | R-02 and R-06 | Priya Nair | No requirement added. R-02's control is a Data Eng procedure, verified by the migration area. R-06's 500ms budget is a metric on the KPI dashboard. The test summary report tracks it as DEF-2304 under Marcus Bell, and the issue log tracks it as ISS-12 under Dana Osei, who owns R-06 on the register. A row here would be one more place for the same facts | Revisit when DEF-2304 is closed |

## Implementation Trace

N/A. The product backlog is the record. Each story in the [Saved Views epic](../epic/epic_example.md) names
the requirement it serves: SV-2 serves FR-1, SV-3 serves FR-2, SV-4 serves FR-3, SV-5 serves FR-4, SV-6
serves FR-5 and SV-7 serves FR-6. The design document holds the design. A table here would restate links
the backlog already holds, and the two could disagree.

## Risk Control Trace

| Risk ID | Risk (short label) | Controlling requirement | Verifying test | Notes |
|---|---|---|---|---|
| R-05 | Shared view exposes personal data to a viewer without entitlement | NFR-2 | TC-047, with TC-046 and TC-048 | Escalated on the register and with the steering group. The register owns the score. The evidence under NFR-2 is API assertions plus one manual rendered-UI step per release |
| R-06 | View-list load exceeds its budget as views accumulate | None numbered. The budget is stated in the register and in exit criterion 5, not in the PRD | View-list load performance area. The 150-view case failed (DEF-2304, open) | A finding, recorded in the last Coverage Gaps row |
| R-02 | Saved-view configs lost in the migration to the new schema | None in the PRD. The control is a Data Eng procedure | Config migration and rollback area: 18 planned, 18 passed. Run on 2.3.1 only | A finding by design, recorded in the same row |

R-01 (vendor licence), R-04 (adoption) and R-07 (the telemetry opportunity) are left out. No row in the
covered set controls them.

## Baselines

| Date | Release or review | Matrix version | Where the snapshot is kept | Reviewed and approved by |
|---|---|---|---|---|
| 2026-07-20 | Pack sent to the steering group for the R-05 decision | v1 | snapshots/saved-views-rtm-v1.md in the Reporting QA wiki (illustrative path) | Anjali Rao reconciled it, and Marta Reyes reviewed and approved it |

This is the first version and the only snapshot. It was reconciled on the day it was taken, so it does not
predate the table. The next snapshot is taken when the steering group decides R-05, so that the decision
records which evidence it saw.

## Upkeep and Review Trigger

**Owner:** Anjali Rao.

**Events that require an update:** The PRD moves past version 0.3.0, or a change request is approved against
it. The 12-combination permission matrix is re-run, or the entitlement area gains a case. DEF-2298, DEF-2286 or
DEF-2304 changes state. The register's row for R-05, R-06 or R-02 changes.

**Review points:** Before the steering group decides R-05, and at each step of the PRD's gradual rollout
(10, 50 and 100 percent). The whole table is checked against its sources at each one.

**Date last reconciled:** 2026-07-20, against the PRD at version 0.3.0, the test plan approved on
2026-07-06, the test summary report final on 2026-07-17, and the register's rows for R-05, R-06 and R-02.
The run record in the test tool was not read, which is why FR-1 and FR-2 read Test linked. Those two rows
are the first thing to reconcile next.
