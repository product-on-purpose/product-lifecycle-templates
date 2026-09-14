---
title: "Saved Views for Dashboards Test Summary Report"
release_or_feature: "Saved Views for Dashboards (phases 1 and 2)"
build_or_version: "Builds 2.3.1 and 2.3.2 on staging; performance measured on the pre-prod replica at 2.3.2"
test_plan_ref: "../test-plan/test-plan_example.md (Saved Views for Dashboards Test Plan, approved 2026-07-06)"
report_author: "Anjali Rao (QA Lead, Reporting)"
test_period: "2026-07-06 to 2026-07-17"
distribution: "Priya Nair (PM, Reporting), Marcus Bell (Staff Engineer, Reporting), Sam Okafor (Security), Marta Reyes (Program Manager); attached to the 2.3.2 release checklist"
status: "final"
last_updated: "2026-07-17"
related:
  - "../test-plan/test-plan_example.md (the plan whose exit criteria this report grades)"
  - "../test-case/test-case_example.md (TC-047, the case that found DEF-2291)"
  - "../bug-report/bug-report_example.md (DEF-2291, the defect that suspended phase 2)"
  - "../acceptance-criteria/acceptance-criteria_example.md (the agreed criteria for the default-view story)"
  - "../prd/prd_example.md (Saved Views PRD; FR-1 to FR-5 are the scope tested)"
doc_type: test-summary-report
size: full
source_template: test-summary-report
source_template_version: 0.1.0
---

<!--
Worked example for the test-summary-report bundle: a full-variant report closing the qa-docs chain on the
Acme Analytics "Saved Views for Dashboards" feature. It reports the effort that the test plan scoped, running
the cases that plan scheduled, and it accounts for DEF-2291, the defect the bug report records. Every figure
in it is illustrative, and the load-bearing ones are marked so inline.

WHY THE FULL VARIANT: three groups tested (Reporting QA, Platform and Design Systems), a formal security gate
sat inside the cycle, the migration assets outlive the release, and a criterion is graded not met, so the
reasoning has to survive being read by people who were not in the room.

THREE THINGS TO STUDY. First, a pass rate of 96.1 percent sits above a criteria table with one criterion not
met and one partially met: the total and the judgement disagree, and the judgement is the document. Second,
criterion 6 is graded Met over a narrower base than planned, because a criterion about the disposition of
findings cannot be failed by not looking. Third, criterion 3 is graded Not met and left that way; the exit
review's decision to release anyway is recorded underneath it as a decision, not folded into the grade.
-->

# Saved Views for Dashboards Test Summary Report

## Scope and What Was Tested

This report closes the testing of **Saved Views for Dashboards, phases 1 and 2**, against the
[Saved Views test plan](../test-plan/test-plan_example.md) approved on 2026-07-06. It covers
**2026-07-06 to 2026-07-17** and grades the plan's six exit criteria.

**Builds.** Execution began on **build 2.3.1** on staging with the `saved_views` flag enabled. **Build
2.3.2** was cut on 2026-07-14 to carry the fix for DEF-2291 and was the build used from 2026-07-15 onward.
Both builds are named throughout, because the two are not interchangeable: 2.3.2 changed where dashboard
aggregates are computed, and most of phase 1 was verified before that change existed. The Execution Summary
says which areas' outcomes stand on which build.

**Environments.** Staging, reseeded nightly from the anonymized production snapshot, for functional,
end-to-end and accessibility work. The migration sandbox, holding a copy of the legacy key-value store, for
the dry run and rollback rehearsal. The pre-prod replica, frozen for the window, for performance only. No
entitlement assertion was made on the pre-prod replica at any point: its anonymization collapses the region
grants (illustrative), which would make the restricted persona appear fully entitled and every entitlement
case pass without proving anything.

**What was tested.** Functional requirements FR-1 to FR-5 of the [Saved Views PRD](../prd/prd_example.md)
across both rollout phases, exercised through the five `ViewsController` endpoints, the `saved_view` table
migration and its rollback, the `default_view_id` preference field, and the Views control in the dashboard
frontend. Non-functional coverage: the shared-view entitlement boundary, view-list load performance,
degradation when a saved config references a deleted filter field, and WCAG 2.2 AA keyboard and
screen-reader operation of the Views control.

**Who tested.** Anjali Rao (API, end-to-end, the permission matrix), Lee Zhang (migration and rollback),
Marcus Bell (performance), Sofia Marino (accessibility), Sam Okafor (security review on 2026-07-10).

**What this report does not cover, stated so that silence is not read as clearance.**

- **The dashboard permissions service.** Platform owns and tests it. What was verified here is this
  feature's *use* of it, specifically that a shared view re-checks the recipient's access when the recipient
  reads it.
- **FR-6, the stale-view change indicator.** Not built in this release, so there was nothing to test.
- **The legacy report flow.** The standing regression suite ran green against both builds but was not
  re-planned, re-scoped or re-read for this release, and no claim is made about it here.
- **Adoption.** Measured after launch on the KPI dashboard. Testing cannot verify it and did not try.
- **Any build other than 2.3.1 and 2.3.2, and any environment other than the three named above.** The
  performance figures in particular are claims about the pre-prod replica at its frozen data profile and
  about nothing else.

**A note on severity labels.** The test plan writes its severity bar as "Sev-1 or Sev-2". Acme's tracker
uses the four-level scale S1 Critical / S2 Major / S3 Minor / S4 Trivial. They are the same scale under two
spellings; the criterion below is quoted in the plan's own words and graded against tracker severities.

## Execution Summary

Rows are in the plan's own risk order, highest first, so the top of this table is the part of the release
that mattered most.

| Area or suite | Planned | Executed | Passed | Failed | Blocked | Not run | Coverage and notes |
|---|---|---|---|---|---|---|---|
| Shared-view entitlement (High, register R-05) | 12 | 12 | 12 | 0 | 0 | 0 | The full permission matrix: 3 personas against 4 filter scopes, including TC-046, TC-047 and TC-048, which between them exhaust the entitlement partitions. 7 of the 12 had run on 2.3.1 when TC-047 failed and the matrix was suspended; all 12 were executed from the start on 2.3.2. Denominator is the matrix the plan defined, not the sharing surface |
| Config migration and rollback (High, register R-02) | 18 | 18 | 18 | 0 | 0 | 0 | 12 seeded known-bad legacy configs reconciled, plus 6 rollback and schema-version cases. Run on 2.3.1 in the migration sandbox, 2026-07-08 to 2026-07-09, and not re-executed on 2.3.2. Coverage is of the 12 config shapes that were seeded, not of the shapes production holds |
| Stale-field degradation (Medium-high) | 9 | 9 | 8 | 1 | 0 | 0 | The PRD reliability requirement and the design's `stale_fields` path. Eight ran on 2.3.1, where TC-052 raised DEF-2277 on 2026-07-08; that case was re-verified on 2.3.2. The open failure is DEF-2298 (S3) |
| View-list load performance (Medium, register R-06) | 6 | 6 | 5 | 1 | 0 | 0 | Two thresholds at three view counts (50, 100 and 150 views on one dashboard) on the pre-prod replica, 2.3.2 only. The single failure is view-list load at 150 views: DEF-2304 |
| Default-view resolution (Medium) | 14 | 13 | 13 | 0 | 1 | 0 | 9 cases derive from the [agreed acceptance criteria](../acceptance-criteria/acceptance-criteria_example.md); 5 came from test design and no criterion names them. Run on 2.3.1 only. The blocked case needs a mid-session access revocation that Platform could not schedule |
| Accessibility of the Views control (Medium) | 14 | 11 | 10 | 1 | 0 | 3 | NVDA on Windows completed in full on 2.3.1; the accessible-name case was re-verified on 2.3.2. The 3 not run are the VoiceOver on macOS pass, which never started. The open failure is DEF-2286 (S3) |
| Rename and delete (Low) | 8 | 8 | 8 | 0 | 0 | 0 | Owner and non-owner against an existing and a deleted row, which is the equivalence partition set and deliberately no more. Run on 2.3.1 only |
| **Total** | **81** | **77** | **74** | **3** | **1** | **3** | |

Counts were taken on **2026-07-16 at 17:00 UTC**, at the close of execution. They will move: DEF-2298 and
DEF-2286 are open and their cases will flip when the fixes land. The live results are in the test tool's
sprint 14 run record; this table is a reading of it at one moment, not a replacement for it.

**On the 96.1 percent, because someone will quote it.** 74 of 77 executed cases passed. That figure is a
property of the cases this team chose to write and chose to run, and it says nothing about how much of the
product they reach. Four of the seven areas above were verified on 2.3.1 and never re-executed against
2.3.2, three planned accessibility cases were never attempted, and the coverage claim in each row names its
own denominator for that reason. The plan refused to make a pass rate an exit criterion, and this cycle is
the argument for that refusal: 96.1 percent would have cleared any plausible pass-rate bar on a release that
also suspended testing for an S1 data-exposure defect and finished with a criterion graded not met.

## Defects

**Eleven defects were raised in the window** (illustrative): one S1, three S2, five S3, two S4. Eight are
closed. Build 2.3.2 carried the DEF-2291 fix and, because it was the only build cut after entry, also picked
up the fixes for DEF-2277, DEF-2284 and the five lower-severity defects already merged and waiting.

**Three are open**, and they are the content of this section. By area, the open set clusters where the
release is thinnest rather than spreading evenly: one in performance, two in the user-facing edges of the
feature (the stale-field notice and keyboard focus). Nothing is open against entitlement, migration or
default-view resolution.

DEF-2291 is closed and still gets a row below, because it is the reason phase 2 was suspended, the reason
the permission matrix was executed twice, and the evidence behind criterion 2's grade. Its full record,
including the cause and the regression guard, is in the [bug report](../bug-report/bug-report_example.md);
nothing from it is retyped here.

| Defect | Severity | Status | Impact if it ships | Disposition: why it is open, who accepted it |
|---|---|---|---|---|
| [DEF-2291](../bug-report/bug-report_example.md) | S1 Critical | Closed | A recipient of a shared view could read the magnitude of data they are not entitled to, from an aggregate computed before the entitlement filter | Fixed in 2.3.2 (2026-07-14), verified by Anjali Rao 2026-07-15, full permission matrix re-executed from the start. Listed here because criterion 2 rests on that re-execution |
| DEF-2304 | S2 Major | Open | A dashboard carrying many saved views opens its view list slowly. p95 612ms at 150 views against the plan's 500ms budget (illustrative), so the feature degrades exactly where the heaviest users are | No fix attempted in the window; found 2026-07-15, after the build was cut. Accepted for release at the 2026-07-17 exit review by Priya Nair, Marcus Bell and Sam Okafor, under the conditions recorded in Evaluation Against Exit Criteria. Priya Nair is accountable for the acceptance; Marcus Bell owns the fix, scheduled for 2.4 |
| DEF-2286 | S3 Minor | Open | Closing the Views menu with Escape returns focus to the dashboard body instead of the Views trigger, so a keyboard user loses their place and has to tab back. A WCAG 2.2 AA finding | Accepted in writing by Priya Nair on 2026-07-16 under exit criterion 6, deferred to 2.4. Sofia Marino raised it on 2026-07-09 |
| DEF-2298 | S3 Minor | Open | The stale-field notice says how many filters are missing but does not name them, so an analyst cannot tell what to re-save without opening the view's configuration | Found 2026-07-15 while re-verifying DEF-2277; it could not be seen earlier, because the read path threw an error instead of rendering the notice at all. Accepted by Priya Nair on 2026-07-16, deferred to 2.4. **This one misses an agreed acceptance criterion**, which asks for a message naming the missing filter; see Evaluation Against Exit Criteria |

## Deviations from Planned Testing

**Phase 2 was suspended for two days, and the plan's resumption rule was applied in full.** TC-047 failed at
step 4 on 2026-07-13; Anjali Rao suspended all sharing testing at 15:10 UTC that day, per the plan's
suspension rule, and notified Priya Nair, Marcus Bell and Sam Okafor the same afternoon. Phase 1 continued,
because it does not exercise the sharing path. Testing resumed on 2026-07-15 once 2.3.2 was deployed and Sam
Okafor confirmed the security review unblocked. Cost: two of the four planned sharing days. Recovered by
dropping a second exploratory sharing session, not by shortening the matrix.

**The permission matrix was executed twice, which the plan did not budget for.** Seven of the twelve
combinations had run on 2.3.1 when TC-047 failed. The plan's resumption rule requires the entire matrix to
be re-run from the start rather than the failing case alone, because an entitlement defect invalidates the
assumption behind every result that passed before it. All twelve were re-executed on 2.3.2 on 2026-07-15.
This is the single largest difference between planned and actual effort in the cycle and it was the right
call; recording it here is what lets a reader see that the twelve passes are twelve passes on one build, not
seven on one and five on another.

**Three accessibility cases were never run.** Sofia Marino completed the NVDA on Windows keyboard and
announcement cases between 2026-07-09 and 2026-07-13 and returned to the Billing program on 2026-07-14, as
agreed before the cycle started. The VoiceOver on macOS pass was handed to Anjali Rao for 2026-07-14 to
2026-07-16, to be run against Sofia Marino's protocol. It never started: the plan's resumption rule put the
full twelve-combination permission matrix back on the 15th and the resumed sharing cases on the 15th and
16th, and one person could not do both. Anjali Rao flagged the clash to Marta Reyes on 2026-07-14 and did
not escalate for a second reviewer, judging the remaining window too short to be worth another team's
context-switch. That judgement is recorded rather than defended: the consequence is a coverage gap carried
as a residual risk below, and a different call was available.

**One default-view case was blocked.** Verifying that a default which is a shared view the user can no
longer read falls back cleanly requires revoking a recipient's dashboard access mid-session, which is a
Platform operation. Requested from Dana Osei on 2026-07-10; not scheduled inside the window.

**This report is not the one-page summary the plan promised.** The plan's deliverables list commits to "a
one-page test summary against the exit criteria". A suspension, an S1, a criterion graded not met and a
residual risk being carried by three named people do not compress to one page honestly. The one-page form
exists as the 2.3.2 release checklist entry and links here; this is the record it links to.

## Impediments and Blocked Progress

**The hotfix build was the constraint, not the fix.** The DEF-2291 fix was merged on 2026-07-13, the evening
it was triaged. Build 2.3.2 was cut on 2026-07-14 and deployed to staging that afternoon, so testing resumed
on the 15th. Cost: roughly one working day of the two-day suspension was the release train rather than the
engineering. Nobody is at fault in that sentence, and it is the single clearest candidate for shortening the
next suspension.

**The accessibility pass lost its stand-in and has no specialist owner.** The VoiceOver on macOS cases moved
to Anjali Rao when Sofia Marino returned to Billing on schedule, and the resumption rule then claimed the
same three days. Sofia Marino is committed to Billing through 2026-07-31, so the pass now has neither a date
nor anyone qualified to run it. **Still open at the time of writing**, and the ask is to Marta Reyes: either
a Design Systems reviewer for two days before the 2.4 window opens, or an explicit decision to ship the
Views control without a VoiceOver pass and record that on the accessibility register.

**The mid-session access revocation was never scheduled.** Requested from Dana Osei on 2026-07-10 and again
on 2026-07-14. Cost: one blocked case and one unverified fallback path. **Still open**; the ask is a
half-hour Platform slot in the 2.4 entry window, which is small enough that the honest reading is that it
was never anyone's priority, including this team's.

**What did not go wrong, because the plan said it probably would.** The plan's top risk to the effort was
staging contention with the Billing migration in week two, landing exactly on the phase 2 window. The
2026-06-29 booking for 13 to 16 July was honoured and the contention never materialised, so the plan's
fallback of running the permission matrix on the pre-prod replica was never invoked. That matters more than
a clean risk usually does: TC-047 is explicitly not valid on the replica, whose anonymization collapses the
region grants, so the fallback would have produced twelve passes that proved nothing. The contingency in the
plan was wrong, and only luck stopped it being used. It should not survive into the 2.4 plan.

## Evaluation Against Exit Criteria

The six criteria are quoted in the plan's own words and in the plan's own order. None has been reworded to
match a result.

| Exit criterion (as the plan wrote it) | Verdict | Evidence | Consequence if released as is |
|---|---|---|---|
| 1. "Every High and Medium-high tier area in the Risk-Ranked Approach has its planned cases executed. Not "most cases": these three areas, complete." | Met | Shared-view entitlement 12 of 12, config migration and rollback 18 of 18, stale-field degradation 9 of 9. No case in these three areas is blocked or unrun | None |
| 2. "The permission matrix is 100 percent executed with zero failures. This one is absolute; a single failure here is a suspension event, not a defect to triage." | Met, on re-execution | 7 of 12 combinations had run on 2.3.1 when TC-047 failed at step 4; the matrix was suspended, DEF-2291 was fixed in 2.3.2, and all 12 were executed with zero failures on 2026-07-15 under the plan's resumption rule | None for release. The criterion is met against the build being shipped. The failure it records against 2.3.1 is DEF-2291, closed |
| 3. "Zero open Sev-1 or Sev-2 defects against in-scope requirements." | **Not met** | DEF-2304 (S2 Major) is open against the plan's view-list load budget, carried in the register as risk R-06 | View-list load runs 612ms at p95 against a 500ms budget at 150 views (illustrative), roughly 22 percent over. It degrades rather than breaks, and it degrades worst for the analysts with the most saved views, who are the feature's heaviest users |
| 4. "Migration reconciliation shows a zero-row mismatch on the dry run, and the rollback rehearsal has been completed once end to end." | Met | Zero mismatch across the seeded legacy extract on 2026-07-08; rollback rehearsed once to the read-only legacy store on 2026-07-09, by Lee Zhang | None. Worth noting what the criterion does not assert: reconciliation counts rows and does not prove a converted config is semantically right. DEF-2277 was exactly that case, a row that migrated correctly and could not be read |
| 5. "p95 view switch under 1s and p95 view-list load under 500ms on the pre-prod replica at 3x expected view count (illustrative thresholds, taken from the PRD and the register)." | Partially met | View switch p95 0.74s, met. View-list load p95 180ms at 50 views, 340ms at 100, and 612ms at 150, so not met at the 3x count the criterion names (all illustrative). DEF-2304 | As criterion 3. The two criteria fail on one defect, not two problems |
| 6. "Accessibility findings at AA level are either fixed or accepted in writing by Priya Nair." | Met | Two AA findings. DEF-2284 (missing accessible name on the Views trigger) fixed in 2.3.2 and re-verified 2026-07-15. DEF-2286 accepted in writing by Priya Nair on 2026-07-16 | The criterion is met over 11 of 14 planned cases, on NVDA only. A criterion about the disposition of findings cannot be failed by not looking, so meeting it proves less here than its wording suggests. The unrun VoiceOver pass is carried as a residual risk below |

**What the testing concludes.** Four criteria are met, one of them only because the permission matrix was
re-run in full on a second build; one is partially met; one is not met. The three highest-ranked product
risks the plan carried, entitlement, migration and stale-field degradation, are all cleared on evidence, and
the S1 that interrupted the cycle is fixed, verified and guarded by a regression case. **Testing therefore
supports releasing phases 1 and 2 on build 2.3.2 with DEF-2304 open**, on three conditions: that the phased
rollout in the PRD is followed so the 150-view profile is reached gradually rather than on day one, that a
p95 alert on view-list load is live before the first cohort, and that Marcus Bell owns DEF-2304 into 2.4.
Testing does not support releasing on a build where criteria 1, 2 or 4 are anything other than met.

**The unmet criterion was not rewritten, and that distinction is the point.** Criterion 3 stays graded Not
met in this document. What happened at the exit review on 2026-07-17 is that Priya Nair, Marcus Bell and Sam
Okafor, the three signatories the plan's change control names for criteria 2 and 3, decided to release with
DEF-2304 open and to carry the exposure under the conditions above. That is a decision about an unmet
criterion. It is not a relaxation of the criterion, and if the plan's bar changes for 2.4 it changes in the
2.4 plan, in advance, where the next team can see it before they start.

**One thing no criterion catches.** DEF-2298 is an S3, so it sits comfortably inside criterion 3's bar, and
it misses an agreed acceptance criterion: the default-view story asks that a view referencing a deleted
filter "shows a clear message naming the missing filter", and the shipped notice gives a count instead. The
plan's exit criteria are severity bars, and a severity bar cannot see the difference between a cosmetic S3
and an S3 that breaks something the business agreed to. Priya Nair accepted it knowing that; it is recorded
here so the acceptance is on the record rather than implied by a number.

## Residual Risk and What Was Not Tested

Ordered by what it would cost if it went wrong. Every row names a person carrying it; an entry with no name
on it would be a risk nobody has accepted.

| Untested area or unfixed defect | Exposure: what could go wrong, and to whom | Accepted by | How it surfaces |
|---|---|---|---|
| Phase 1 outcomes stand on build 2.3.1 and were not re-executed on 2.3.2 | 2.3.2 moved aggregate computation behind the entitlement filter. Migration, default-view resolution and rename/delete were verified before that change existed, and their evidence is therefore one build old. A regression in any of them would reach analysts as silently as DEF-2291 did | Priya Nair | CI unit and component gate plus the smoke suite, both green on 2.3.2. Neither exercises the migration path or the default-view precedence rules, so in practice this surfaces as a user report |
| View-list load p95 exceeds the budget at 150 views (DEF-2304, open) | Analysts who accumulate views, who are the feature's most engaged users, wait longest. The program is selling speed, so this erodes the thing being sold rather than breaking it | Priya Nair, accountable, at the 2026-07-17 exit review with Marcus Bell and Sam Okafor co-signing | p95 view-list alert on the reporting latency panel, threshold 550ms (illustrative), live before the first rollout cohort |
| VoiceOver on macOS was never exercised (3 cases not run) | Undetermined. NVDA passed on 10 of 11 cases, and the two engines diverge most on exactly the custom-menu pattern the Views control uses, so NVDA passing is weak evidence for VoiceOver. A macOS screen-reader user could find the control unusable and the release would not know | Priya Nair | Nothing automated detects this. It surfaces through a support ticket or an accessibility complaint, which is the slowest and most expensive path available |
| A recipient losing dashboard access while a shared default view is open (1 case blocked) | The fallback is unverified. Worst case the dashboard fails to load rather than falling back to the generic state, which locks a user out of a dashboard they still have rights to | Marcus Bell | Error-rate panel on dashboard open. The fallback path is logged, so the signal exists; nobody is watching it today |
| Migration coverage is bounded by the 12 seeded known-bad configs | Undetermined, and deliberately so. Nobody enumerated the config shapes production actually holds, so the reconciliation proves the converter handles twelve shapes rather than all of them. An unseen shape fails at cutover, when the legacy store is already read-only | Lee Zhang | Reconciliation counter runs at cutover and halts the migration on any mismatch, which converts a silent loss into a visible stop. That is the mitigation; it is not detection in advance |
| The rendered-UI entitlement assertion runs once per release, by hand | TC-047's automated form asserts on the API response only. Nothing in the pipeline checks that an unentitled value never appears in a rendered tooltip, chart label or tile. A future change that leaks through the render layer alone passes every automated gate | Sam Okafor | Only the manual step 5, run once per release. Until it is automated, the guard on the class of defect DEF-2291 belongs to is thinner than the regression set implies |

## Test Deliverables and Reusable Assets

| Deliverable or asset | Where it lives | Owner now | Retention or reuse note |
|---|---|---|---|
| Executed case results, all 77 | Test tool, sprint 14 run record for Saved Views | Anjali Rao | Retained for the life of the 2.3 branch per the release checklist. This report is a reading of it, not a copy |
| Open-defect list with severities | Tracker, filter `feature = saved-views AND status = open` | Anjali Rao | Live. The three rows in Defects above are a snapshot at 2026-07-16 17:00 UTC |
| Migration rollback rehearsal record | Migration sandbox run log, 2026-07-09 | Lee Zhang | Required separately by the release checklist; keep until the legacy key-value store is decommissioned |
| DEF-2291 evidence bundle (screenshot, API response, staging log with the request ID) | Attached to [DEF-2291](../bug-report/bug-report_example.md) | Marcus Bell | Keep as long as the defect record. It is the only artifact showing the pre-fix behaviour |
| Permission persona set: owner, permitted viewer, restricted viewer | Platform persona fixtures, staging seed | Dana Osei | Reusable and fragile. The personas are manufactured rather than sampled, because the anonymized snapshot carries no restricted filter field; regenerate whenever the entitlement model changes |
| Entitlement spec directory, including `tests/entitlement/shared_view_restricted_viewer_spec.rb` | Release branch CI | Marcus Bell | In the release regression set, runs on every pipeline execution. TC-053 was added to it after DEF-2291 to cover the row-count badge, which shares the pre-filter computation path |
| 150-view fixture generator for the pre-prod replica | `reporting-qa/fixtures/view-volume` (illustrative path) | Marcus Bell | Reusable for any view-count performance work. It assumes the frozen replica profile; re-check it after the next replica refresh or the numbers are not comparable |
| Legacy-store extract with 12 known-bad configs | Migration sandbox | Lee Zhang | Keep until the migration is retired. Its weakness is written into the residual-risk table above: twelve shapes, chosen by hand |
| Hand-built fallback fixtures from the plan's contingency | Not built | Nobody | **Do not inherit.** The contingency was never triggered, so no fixtures exist. Listed so the next team does not go looking for them |

## Lessons Learned

**Review High-tier cases before they run, and make it an entry criterion.** TC-047 version 1.0 asserted on
returned rows only and would have passed against a build carrying DEF-2291. Step 4, the aggregate assertion,
was added at version 1.1 on 2026-07-08 after Sam Okafor reviewed the case, five days before it fired. The
case review, not the case, is what found the S1. **Anjali Rao** to add security review of every High-tier
case to the 2.4 plan's entry criteria.

**A row-level assertion cannot see an aggregate leak, and that generalises past this feature.** Every
entitlement case written before TC-047 asserted on rows, and the rows were always correct. Anywhere the
product computes a number over a filtered set, the number needs its own assertion. **Marcus Bell** has
carried this into the entitlement spec directory via TC-053; the wider sweep of other aggregate surfaces has
no owner yet and should get one in 2.4 planning.

**Schedule accessibility against the first stable build, not the last.** Accessibility was ordered sixth of
seven, which put its last three cases after the specialist's agreed departure date and inside the days the
resumption rule reclaimed. Nothing about the Views control's keyboard or screen-reader behaviour required a
late build, so ordering it late bought nothing and cost three cases. **Anjali Rao** to reorder it in the 2.4
plan.

**Retire the plan's staging-contention contingency instead of reusing it.** Running the permission matrix on
the pre-prod replica was written into the plan as the fallback and would have produced twelve meaningless
passes, because the replica's anonymization collapses exactly the grants the matrix tests. The contingency
was never needed, which is the only reason it caused no harm. **Anjali Rao and Dana Osei** to replace it in
2.4 with a second staging slice, or to record that there is no fallback and the booked window is the
mitigation.

**Keeping on purpose: inheriting product risks from the register rather than re-deriving them.** The
Execution Summary's row order is the plan's risk order, which is the register's risk order. A reader
scanning the top of that table is reading the areas the program already agreed mattered most, and nobody had
to argue about ordering at any point in the cycle.

No retrospective was held for this cycle; the team runs one per release train rather than per feature, and
the next falls after 2.4 opens. These five items are therefore recorded here because this document is where
they survive, and each has a name against it for the same reason.
