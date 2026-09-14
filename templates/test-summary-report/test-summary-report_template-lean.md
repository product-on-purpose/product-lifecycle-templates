---
title: "{{release_or_feature}} Test Summary Report"
release_or_feature: "{{release_or_feature}}"
build_or_version: "{{build_or_version}}"
test_plan_ref: "{{test_plan_ref}}"
report_author: "{{report_author}}"
test_period: "{{test_period}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: test-summary-report
size: lean
source_template: test-summary-report
source_template_version: 0.1.0
---

<!--
LEAN TEST SUMMARY REPORT. The smallest report that is still a real report: what was tested and on which
build, what ran, what broke, what did not happen as planned, whether the bar the test plan set was cleared,
and what is being carried forward untested or unfixed. Use it to close a release or a test cycle for readers
who were broadly in the room. To grow it into the accountability-grade report (see
test-summary-report_template-full.md), ADD sections; never rename or reorder the ones below, because the full
variant is a strict superset of this one.

IF THE DASHBOARD ALREADY SAYS IT, DO NOT RETYPE IT. The criticism this document type has never fully answered
is that it can satisfy every heading and still say nothing about the quality of the product. Your test tool
computes the counts better than this page can. What it cannot do is say what was not tested and why, what
residual risk somebody is accepting, and whether the result clears the bar. Spend your time there; where a
section adds nothing to the tool, keep it to a line and a link. See test-summary-report_companion.md
sections 6 and 7.

SOMETIMES THE HONEST ANSWER IS NOT TO WRITE ONE. If everyone who would read this sat in the same standup all
cycle, a short message carrying the exit-criteria call and the residual-risk list does the whole job. Write
the document when the result has to travel: beyond one iteration, beyond the immediate team, or into an
audit, a sign-off or a contract.

WHAT A TEST SUMMARY REPORT IS, AND IS NOT
It is the retrospective document that closes a testing effort: what was tested, what the testing found, what
was deliberately or accidentally not tested, and whether the result clears the bar the test plan set. It is
NOT a test plan (that is prospective, written before), NOT a test status or progress report (that is produced
at intervals while testing is still running), NOT your test tool's exported run or your CI dashboard (those
compute the counts; this document carries the judgment), and NOT a bug tracker (one failing verification is
one bug report). See test-summary-report_companion.md section 8.

IF YOU ARE LOOKING FOR A "RELEASE RECOMMENDATION" SECTION, IT IS DELIBERATELY NOT HERE. The ship call belongs
at the end of Evaluation Against Exit Criteria, underneath the criteria that justify it. A recommendation
with nothing above it is an opinion; the same sentence under a graded criteria table is a conclusion. This
library considered a standalone section and dropped it for want of evidence; the reasoning is in
test-summary-report_companion.md section 3.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   test-summary-report_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to
   avoid. For tables, PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Fill Scope and What Was Tested first, then Evaluation
   Against Exit Criteria; everything else exists to make that evaluation readable.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it silently.
4. Before you share it: self-grade against test-summary-report_guide.md, then DELETE every HTML comment.
   They are guidance, not content.
-->

# {{release_or_feature}} Test Summary Report

## Scope and What Was Tested

<!-- WHAT  What this report covers: the build or version under test, the environment and configuration, the
           test plan it answers to, the period it covers, and the boundary of the claim.
     WHY   Every number below is meaningless without the version that produced it, and the version is the
           field the one filled report in this bundle's research omits, which names
           no build anywhere, so nobody reading it later can tell what it was about. Bounding the claim is
           the other half: a report that does not say what it does not cover gets read as covering
           everything. Deep dive: test-summary-report_companion.md section 3 (Anatomy > Scope and What Was
           Tested).
     ASK   Which build, version or commit was tested, in which environment and configuration? Which test
           plan, and which of its criteria, does this report answer? What period does it cover, and who
           tested? What does the result explicitly not apply to?
     GOOD  "Covers Claims Intake R7.2, build 7.2.14, on pre-production with the fnol_v4 flag on, tested
           2026-03-02 to 2026-03-13 by Nadia Okonkwo and Fabiola Reyes against the R7.2 test plan. Results
           apply to that build and configuration only. The broker portal integration runs on its own release
           train and was not exercised here."
     WEAK  "Testing of the claims release. Ran on staging." (no build, no dates, no plan reference and no
           boundary, so a reader can tell neither what the report is about nor what it leaves out)
     TRAP  Omitting the build or version because everyone currently knows which one it was. In six months
           this report is the only record, and nobody will. -->

{{scope_and_what_was_tested}}

## Execution Summary

<!-- WHAT  The counts - planned, executed, passed, failed, blocked, not run - per area or suite, with
           coverage stated against something meaningful, and a line below the table saying when the
           counts were taken and where the live results live.
     WHY   This is the section your tooling can fill, and the only one. Test management tools and CI plugins
           compute exactly these numbers and draw them better than a document can, so a report that is
           mostly this section is a dashboard with a cover page, and out of date the moment it is written.
           Put the counts here so the judgment below has something to stand on, and put the judgment where
           the criteria are. Deep dive: test-summary-report_companion.md section 3 (Execution Summary) and
           section 6.
     ASK   How many cases were planned, and how many actually ran? What failed, what was blocked, what never
           ran at all? What is coverage a fraction of - risk areas, requirements, the plan's own priorities?
           When were these counts taken, and where does a reader go for the detail?
     PRIORITY  Order rows by the plan's own risk ranking, highest risk first, so a reader scanning the top of
           the table is reading about the areas that mattered most. Counts are a snapshot: state the date and
           time they were taken, because they moved the day after.
     ROW HINT  A good row names an area the plan recognizes, gives every count including the ones that did
           not run, and says what the coverage figure is a fraction of. A weak row is a suite name and a pass
           percentage.
     GOOD  | Payout calculation (High risk) | 48 | 46 | 42 | 3 | 1 | 2 | 46 of 48 planned cases; all 9
           High-risk scenarios executed |
     WEAK  | Regression | | | | | | | 97 percent |
     TRAP  Leading with a pass rate. "97 percent passed" hides whether the 3 percent was a cosmetic label or
           the permission check, and a percentage is an input to the exit-criteria evaluation below, never a
           substitute for it. -->

| Area or suite | Planned | Executed | Passed | Failed | Blocked | Not run | Coverage and notes |
|---|---|---|---|---|---|---|---|
| {{area}} | {{planned}} | {{executed}} | {{passed}} | {{failed}} | {{blocked}} | {{not_run}} | {{coverage_note}} |

{{execution_summary_notes}}

## Defects

<!-- WHAT  What was found, at what severity, what is fixed, and what is still open at the moment of writing -
           summarized and linked, never transcribed.
     WHY   Open defects are the content here; a list of what you fixed is history. The strongest real reports
           break the found defects down by something a team can act on, such as root cause or component, and
           give every open one a severity and a stated reason it is not being fixed. Deep dive:
           test-summary-report_companion.md section 3 (Defects).
     ASK   How many defects were found, at what severities, and what pattern do they show? How many remain
           open, and which are in scope for the release decision? For each open defect, what would a user
           experience, why is it not fixed, and who accepted that? What is fixed but not yet verified?
     PRIORITY  Severity first, highest first, and open before closed within a severity. Closed defects are a
           summary line above the table; every open defect in scope gets a row of its own.
     ROW HINT  A good row identifies the defect, gives severity and status, says what a user would
           experience, and names both the reason it stands and the person who accepted it. A weak row is a
           ticket number and a title.
     GOOD  | CLM-4471 | Sev-2 | Open | Payout total rounds down by one cent on multi-currency claims | Fix
           lands in 7.2.15; Ellen Wray accepted the cent-level variance for the two-week window and finance
           was notified 2026-03-11 |
     WEAK  | CLM-4471 | High | Open | Rounding bug | Will fix |
     TRAP  Pasting the tracker in. Forty rows of reproduction steps make a worse defect list than the tracker
           itself and bury the three that matter. Summarize, link out, and spend the words on the open
           ones. -->

{{defect_summary}}

| Defect | Severity | Status | Impact if it ships | Disposition: why it is open, who accepted it |
|---|---|---|---|---|
| {{defect_id}} | {{severity}} | {{defect_status}} | {{defect_impact}} | {{defect_disposition}} |

## Deviations from Planned Testing

<!-- WHAT  What the plan said would happen, what actually happened, and why the difference - in scope,
           schedule, depth, environment or data.
     WHY   Deviations are what make the numbers above interpretable: a 98 percent pass rate over half the
           planned depth is a different result from the same rate over all of it. The evidence for keeping
           this section is one-sided - both structural sources this bundle could read carry it, both real
           templates ask for it, and the one real filled report gives it a named subsection - which is why it
           is in the lean variant, against this library's own earlier internal spec. Deep dive:
           test-summary-report_companion.md section 3 (Deviations from Planned Testing) and section 4.
     ASK   What did the plan say, and what actually happened? Which areas were tested less deeply than
           planned, or not at all? What changed in scope, schedule, environment or data mid-effort, and who
           agreed it? Who knew at the time, and who is finding out from this document?
     GOOD  "The plan scheduled two full regression passes; one ran, because pre-production was rebuilt in
           week two. Fraud-scoring cases were executed against synthetic data rather than the anonymized
           production extract, which never arrived. Both were raised with Ellen Wray on 2026-03-06; neither
           changed the agreed exit criteria."
     WEAK  "Some testing was descoped due to time." (which testing, how much, whose decision, and what does
           it do to the counts above)
     TRAP  Writing this section after the release decision is made. A deviation that surfaces for the first
           time in the report is news, and news arriving this late damages trust in everything else on the
           page. Raise them as they happen and record them here. -->

{{deviations_from_planned_testing}}

## Evaluation Against Exit Criteria

<!-- WHAT  Each exit criterion the test plan set, whether it is met, and on what evidence - then the
           conclusion the testing reaches about releasing.
     WHY   This is the load-bearing section, and the evaluation against agreed criteria is the act that makes
           this a report rather than an export. Neither readable structural source gives the release call a
           heading of its own, and neither does this template: a recommendation with nothing above it is an
           opinion, while the same sentence underneath a graded criteria table is a conclusion. Write the
           table, then write the sentence: met, not met, and therefore. Deep dive:
           test-summary-report_companion.md section 3 (Evaluation Against Exit Criteria), which records why
           this library considered a standalone Release Recommendation section and dropped it for want of
           evidence.
     ASK   What exactly were the exit criteria, and who agreed them and when? Is each met, partially met or
           not met, and on what evidence? Where one is not met, what does releasing anyway cost? What does
           the testing therefore conclude, and who owns the decision this conclusion feeds?
     PRIORITY  One row per criterion, in the plan's own words and the plan's own order. Never rewrite a
           criterion to match the result. If the plan set no exit criteria, do not invent them after the
           fact: say so plainly in the conclusion and state the bar you are applying instead.
     ROW HINT  A good row quotes the criterion, gives a plain verdict (met, partially met, not met), points
           at the evidence, and where it is not met says what that costs. A weak row is a criterion and a
           tick.
     GOOD  | All 9 High-risk payout scenarios executed with no Sev-2 or worse left open | Not met |
           CLM-4471 (Sev-2) open, see Defects | Multi-currency claims round down by one cent until
           7.2.15 |
     WEAK  | Quality is acceptable | Met | Testing complete | |
     TRAP  The verdict with nothing above it. A confident release sentence sitting on ungraded criteria, or
           on no criteria at all, is exactly the failure this section's shape exists to prevent. -->

| Exit criterion (as the plan wrote it) | Verdict | Evidence | Consequence if released as is |
|---|---|---|---|
| {{exit_criterion}} | {{criterion_verdict}} | {{criterion_evidence}} | {{criterion_consequence}} |

{{conclusion_and_release_call}}

## Residual Risk and What Was Not Tested

<!-- WHAT  What remains untested, what remains unfixed, and what that exposes - written as risk somebody is
           accepting, not as a gap somebody forgot.
     WHY   This is the section a generated report cannot produce, and the one downstream readers thank you
           for. Silence gets read as coverage: an area nobody tested and nobody mentioned reads, later,
           exactly like an area that passed, which is why the sharpest assessments in this bundle's research
           warn their readers not to treat unexamined areas as cleared. Naming the untested area, the unfixed
           defect and the person carrying the consequence is what turns an omission into a decision. Deep
           dive: test-summary-report_companion.md section 3 (Residual Risk and What Was Not Tested) and
           section 7.
     ASK   What was not tested at all, and what was tested more shallowly than its risk deserved? What ships
           unfixed? For each item, what could go wrong, who is accepting it, and how would you find out in
           production? What is genuinely undetermined, as opposed to fine?
     PRIORITY  Order by what it would cost if it went wrong, worst first. Every row needs a named person
           accepting it; a residual risk with no name on it has been accepted by nobody. "Undetermined" is a
           legitimate entry and a better one than a confident guess.
     ROW HINT  A good row names the untested area or unfixed defect, states the exposure as a consequence to
           someone, names the person accepting it, and says what would detect it in production. A weak row is
           a topic with the word "risk" next to it.
     GOOD  | Fraud scoring exercised on synthetic data only | A rule tuned on real distributions could
           misfire on live claims; false declines reach customers | Tomas Brenner | Decline-rate alert on the
           R7.2 dashboard, reviewed daily for two weeks |
     WEAK  | Fraud scoring | Some risk | QA | Monitor |
     TRAP  Writing residual risk as an apology. "Unfortunately we ran out of time for the migration path" is
           a schedule confession. "An unmigrated legacy claim opens read-only and the adjuster cannot
           progress it; accepted by Ellen Wray for the 40 affected claims" is a risk statement. -->

| Untested area or unfixed defect | Exposure: what could go wrong, and to whom | Accepted by | How it surfaces |
|---|---|---|---|
| {{residual_item}} | {{residual_exposure}} | {{residual_accepted_by}} | {{residual_detection}} |
