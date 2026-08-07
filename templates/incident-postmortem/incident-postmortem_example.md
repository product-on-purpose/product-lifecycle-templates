---
title: "Postmortem: Saved-View Aggregate Disclosed Data Across an Entitlement Boundary (DEF-2291)"
incident_id: "DEF-2291"
status: "final"
author: "Marcus Bell (Staff Engineer, Reporting)"
incident_date: "2026-07-13"
postmortem_date: "2026-07-16"
doc_type: incident-postmortem
size: full
source_template: incident-postmortem
source_template_version: 0.1.0
related:
  - "../bug-report/bug-report_example.md (DEF-2291, the defect this postmortem examines)"
  - "../test-plan/test-plan_example.md (Saved Views test plan; risk R-05, the suspension and resumption rules)"
  - "../test-case/test-case_example.md (TC-047, the case that caught this at step 4)"
  - "../sdd/sdd_example.md (Saved Views design; the entitlement re-check this incident bypassed)"
  - "../risk-register/risk-register_example.md (program risk register; R-05 was already the test plan's top-tier risk before this incident, and this postmortem's first action escalated it to the steering group on 2026-07-14)"
  - "../raid-log/raid-log_example.md (program RAID log; where R-05's steering-group escalation is tracked)"
  - "../product-backlog/product-backlog_example.md (Saved Views product backlog; two action items land here)"
---

> **Worked example.** A filled `incident-postmortem`, full variant, examining
> [DEF-2291](../bug-report/bug-report_example.md), the same defect the `bug-report`, `test-plan`, `test-case` and
> `sdd` examples already describe from their own vantage points. It is dated 2026-07-16, inside Sprint 24
> (2026-07-13 to 2026-07-24) and one day after Phase 2 (sharing) testing resumed on 2026-07-15, which is the
> earliest a real postmortem write-up could plausibly follow the fix being verified. It closes before two later
> documents this postmortem's own action items seed: the `definition-of-done` example's amendment on 2026-07-24,
> and the `runbook` example's entitlement-audit reconciliation job, added in build 2.4.0 "after DEF-2291." Neither
> is cited below except here, because the body may only know what had already happened by 2026-07-16.
>
> The incident itself never reached a customer: it was caught on staging by a planned test, not an alert or a
> report, which is deliberately unlike the template's own rate-limiter scenario and is the point this example
> makes about triggers in the Trigger section below. Figures marked "illustrative" are made up for the example.

# Postmortem: Saved-View Aggregate Disclosed Data Across an Entitlement Boundary (DEF-2291)

## Summary

On 2026-07-13, the first day of Phase 2 (sharing) testing for Saved Views, an automated regression assertion
(TC-047 step 4) caught a shared dashboard view whose aggregate total included revenue from a region the
recipient was not entitled to see, even though the same response's row-level data was filtered correctly. The
defect, tracked as DEF-2291, never reached production: it was confined to staging build 2.3.1, found by a
planned test rather than a customer report or a monitoring alert, and exercised only synthetic QA personas. It
still met Acme's own postmortem trigger and suspended all Phase 2 sharing testing for two days. Fixed and
verified 2026-07-15: the aggregate computation now runs behind the entitlement filter instead of ahead of it,
and the full 12-combination permission matrix was re-executed from the start before Phase 2 resumed the same
day.

## Impact

| Affected system or population | Duration | Magnitude |
|---|---|---|
| Production customers | None; the code path never left staging | Zero exposure. Both accounts in the reproduction, R and O, are synthetic QA personas, and the `saved_views` sharing flag had not opened to any real account |
| Phase 2 (sharing) test execution, Reporting Squad | 2026-07-13 15:10 UTC to 2026-07-15 (about two days) | All Phase 2 testing suspended under the test plan's suspension rule; on resumption the entire 12-combination permission matrix was re-executed from the start rather than only the failing case, per the plan's resumption rule |
| Confirmed exposure window, staging only | At most 7 days (illustrative): bounded between the sharing code reaching staging under build 2.3.1 by the test plan's 2026-07-06 entry date, and detection on 2026-07-13 | Limited to the two personas used in TC-047 and TC-048. A manual correlation of the existing `shared_view_served` and `permission_check_passed` staging log streams found no other account requesting a region-restricted shared view in that window (illustrative) |

## Detection

Detected by TC-047 step 4, the automated aggregate assertion added at case version 1.1 after Sam Okafor's
2026-07-08 security review. The assertion failed on the first pipeline run against the Phase 2 build, the
morning Phase 2 execution opened per the test plan's schedule. The same application log entry that shows the
entitlement re-check passing (request ID `7f3c-4a11-a91b`, 14:22 UTC, illustrative) is the request the failing
assertion flagged: the row filter ran correctly and the log says so, which is exactly why nothing about this
defect would have shown up in a re-check-failure alert even if one had existed. Anjali Rao (QA Lead) reproduced
the failure manually against the same build, five of five times via the API and three of three in the browser,
to rule out a flaky assertion before filing DEF-2291 the same day.

No customer report arrived, and none could have. The build was staging-only, and this class of defect produces
no user-visible symptom at all: the row-level data a user actually sees was correct throughout, which is what
made the leak invisible to every earlier entitlement case in the suite and is the subject of Root Causes below.

## Timeline

| Time (UTC) | Event |
|---|---|
| 2026-07-06 | Build 2.3.1 deployed to staging with the `saved_views` flag enabled, per the test plan's entry criteria. The sharing code path, including the aggregate-before-filter pattern, is present from this point at the latest |
| 2026-07-13, ~09:00 (illustrative) | Phase 2 (sharing) execution opens per the test plan's schedule. The automated entitlement regression suite, including TC-047, runs against the Phase 2 build |
| 2026-07-13, 14:22 | TC-047 step 4's aggregate assertion fails on request ID `7f3c-4a11-a91b` (illustrative). The same request's row-level check passes and is logged as passing |
| 2026-07-13, ~14:45 (illustrative) | Anjali Rao manually reproduces the failure, 5 of 5 via the API and 3 of 3 in the browser, and files DEF-2291 |
| 2026-07-13, 15:10 | Triage (Priya Nair, Marcus Bell, Sam Okafor) confirms Severity S1, raises Priority to P1, and Anjali Rao suspends all Phase 2 sharing testing under the test plan's suspension rule, notifying the same three that afternoon |
| 2026-07-14, ~10:00 (illustrative) | PR 812 (illustrative) merges, moving the aggregate computation behind the entitlement filter. Build 2.3.2 releases |
| 2026-07-14, later (illustrative) | Risk R-05 is escalated to the steering group with the specific ask raised at triage: fund a platform-level entitlement-aggregate control, or accept the residual formally |
| 2026-07-15 | Anjali Rao re-verifies against the original TC-047 steps. The full 12-combination permission matrix is re-executed from the start and all 12 pass. Sam Okafor confirms the security review unblocked. Phase 2 sharing testing resumes the same day |

## Trigger

This event meets Acme's own published postmortem criterion: any defect confirmed at Severity S1 on the squad's
four-level scale (S1 Critical / S2 Major / S3 Minor / S4 Trivial) triggers a postmortem regardless of
environment or customer impact, because data exposure is S1 by definition on that scale. It also meets a
second, independent criterion under the same policy: a confirmed entitlement failure that fires the test
plan's suspension rule, stopping planned testing outright rather than being logged as a defect to triage,
qualifies on its own.

This is deliberately not Google's published trigger list restated as though it were Acme's own. Google's canon
leads with user-visible downtime, data loss, on-call intervention, a resolution-time threshold and a monitoring
failure; none of those apply cleanly here. There was no downtime, because nothing was live. There was no
on-call intervention, because this was caught by a scheduled test run, not paged. Resolution time is not a
meaningful trigger for a defect fixed inside one calendar day. What actually fired was a criterion built for
exactly this shape of event: a severity scale that treats any confirmed data-boundary exposure as critical,
independent of who was exposed or how many. Without that criterion, this incident would likely have closed as
a well-handled defect and nothing more, and the questions this document asks, why the acceptance criteria never
reached this case and what would have caught it sooner, would not have been asked at all.

## Root Causes

| Contributing cause | Evidence |
|---|---|
| The dashboard tile's aggregate (`total_revenue`, and equally the row-count badge) was computed in the query layer before ViewsController's entitlement re-check ran, so the re-check filtered the returned `rows` array but never touched the already-computed aggregate | PR 812's diff (illustrative) shows the aggregate assignment executing three calls before the entitlement filter is applied; reproduced 5 of 5 via the API against build 2.3.1 |
| No acceptance criterion for the Saved Views epic addressed what a partially entitled recipient should see inside an aggregate; the agreed criteria stop at the row level (save, load, default, share) | Confirmed against the full acceptance-criteria set for the sharing story at triage on 2026-07-13; the design document's re-check statement was the only source for the expected behavior, not a signed-off criterion |
| The two earlier entitlement cases, TC-046 (fully entitled) and TC-048 (not entitled), assert only on returned rows, the pattern every earlier case used. Only the partially entitled partition can expose an aggregate leak, and TC-047 could not have caught it before version 1.1 added the aggregate assertion on 2026-07-08 | TC-047's version history. TC-048 passed against the same build 2.3.1 and did not surface this, confirming the gap was specific to partial entitlement, not to the test suite generally |

## Resolution

PR 812 (illustrative) moved the aggregate computation behind the entitlement filter, so `total_revenue` and the
row-count badge are now derived from the same permitted row set the response's `rows` array already used. Build
2.3.2 released on 2026-07-14. Anjali Rao re-verified on 2026-07-15 against the original TC-047 steps:
`total_revenue` returned the AMER-only total for recipient R, and owner O's own view was unchanged. Per the test
plan's resumption rule, the entire 12-combination permission matrix was re-executed from the start, not only the
failing case, because an entitlement defect invalidates the assumption behind every result the matrix had
already produced; all 12 passed. Sam Okafor confirmed the security review unblocked the same day, and Phase 2
(sharing) testing resumed on 2026-07-15.

## Lessons Learned

Row-level correctness is not evidence of entitlement correctness. Every earlier entitlement case in this suite
asserted only on returned rows, which is why none of them, and no acceptance criterion, ever exercised this
path. The squad's working assumption now is that any dashboard element derived from a filtered row set, an
aggregate, a count, a chart label, needs its own assertion tying it to the same filter, rather than inheriting
correctness from the rows being right.

The test plan's risk-ranked approach did what it was built to do; the acceptance criteria did not, and were
never going to. Risk R-05 was already the test plan's highest tier before this incident, which is exactly why
TC-047 existed to look for it. The acceptance criteria, by contrast, describe what the business agreed to, and
nobody had agreed to specify what a partially entitled recipient sees inside a total, because the question only
becomes visible once you look at how sharing is implemented. This incident is a data point for trusting
risk-ranked test design over acceptance criteria on exactly the surfaces acceptance criteria are not built to
reach, not a reason to distrust either one.

The squad's Definition of Done does not yet require the permission matrix to be re-executed whenever
entitlement-relevant code changes; nothing in it would have caught this earlier than TC-047 did, and nothing in
it currently prevents the same class of gap on a future change to this code path. Marcus Bell intends to raise
this specifically at Sprint 24's close, rather than folding it into this document's own action items below,
because Acme's Definition of Done is owned and amended at sprint planning, not by a postmortem.

## Action Items

| Action | Type | Owner | Ticket | Status |
|---|---|---|---|---|
| Escalate risk R-05 with the specific ask agreed at triage: fund a platform-level entitlement-aggregate reconciliation control, or accept the residual formally at board level | prevent | Sam Okafor | Risk register R-05 | Escalated to the steering group since 2026-07-14; open |
| Add an automated reconciliation job that cross-checks every `shared_view_served` event against a matching `permission_check_passed` event for the same request, so a future leak surfaces the same day rather than only at the next planned risk-tier test | detect | Marcus Bell | Product backlog SV-8 (proposed) | Open, raised 2026-07-16 |
| Add TC-053, asserting the same aggregate-before-filter defect class against the dashboard's row-count badge, the other metric on this computation path | detect | Anjali Rao | Product backlog SV-10, closed on delivery of TC-053 | Done, 2026-07-15 |
| Write an acceptance criterion for the sharing story covering what a partially entitled recipient sees inside an aggregate, closing the gap Root Causes names above | process | Priya Nair | Product backlog SV-9 (proposed) | Open, raised 2026-07-16 |
