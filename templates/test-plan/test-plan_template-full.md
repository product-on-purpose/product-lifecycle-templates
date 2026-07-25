---
title: "{{release_or_feature}} Test Plan"
release_or_feature: "{{release_or_feature}}"
plan_owner: "{{plan_owner}}"
status: "{{status}}"
last_updated: "{{date}}"
test_strategy_ref: "{{test_strategy_ref}}"
doc_type: test-plan
size: full
source_template: test-plan
source_template_version: 0.1.0
---

<!--
FULL TEST PLAN. The approvable plan: everything the lean variant carries, plus the levels and types breakdown,
the rule for stopping and restarting mid-cycle, the risks to the testing itself, and the sign-off record. Use
it when the context genuinely demands it: regulated or audited work, several teams or vendors testing one
release, a formal gate inside the cycle, or a process that requires an approved artifact.

THIS VARIANT IS A STRICT SUPERSET OF THE LEAN ONE. The five lean sections appear here in the same order, with
the same headings and the same placeholders, and four sections are added. If you started lean, you can grow
into this without rewriting anything you already filled in. (The guidance comments in the shared sections
carry a little extra context for the approvable case; the content you wrote does not change.)

LENGTH IS NOT RIGOR. A nine-section plan padded to look complete is the exact failure the critics of
standardized test documentation name: a document can satisfy every required heading and still say nothing.
Every section here should decide something. If one would change nothing by its absence, write "N/A" and one
line of why. See test-plan_companion.md sections 4 and 6.

WHAT A TEST PLAN IS, AND IS NOT
It is the prospective document that scopes and prioritizes a testing effort. It is NOT a test case (that is
one executable verification), NOT a test report (that is retrospective, written after), NOT a definition of
done (that is a standing team invariant), and NOT the thing your test management tool calls a "test plan"
(that is an execution container whose only required field is usually a name). See
test-plan_companion.md section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   test-plan_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid. For
   tables, PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Fill Scope and Risk-Ranked Approach first; everything else
   follows from them.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it silently.
4. Before you circulate it for approval: self-grade against test-plan_guide.md, then DELETE every HTML
   comment. They are guidance, not content.
-->

# {{release_or_feature}} Test Plan

## Scope and Non-Scope

<!-- WHAT  What is being tested (the concrete test items: builds, services, flag states, requirement IDs) and
           what is explicitly NOT being tested this cycle, with a reason for each exclusion.
     WHY   The exclusion half is the highest-value content in the document and the most commonly deleted. If
           nothing is out of scope, nothing can be found missing, and the scope argument happens after the
           release instead of before it. In an approvable plan it is also what the sign-off is actually
           signing. Deep dive: test-plan_companion.md section 3 (Anatomy > Scope and Non-Scope).
     ASK   What exactly is under test, by build or requirement ID? What is deliberately excluded, and why
           (deferred, covered elsewhere, owned by another team, accepted risk)? Who agreed to the exclusions?
     GOOD  "In scope: FR-1 to FR-5 of the Saved Views PRD, on build 2.3.x behind the saved_views flag. Out of
           scope: FR-6 (stale-view indicator), Could priority, deferred to the next release; and the
           permissions service itself, owned and tested by Platform."
     WEAK  "Testing the Saved Views feature." (no test items, no exclusions, nothing anyone can disagree with
           or be held to)
     TRAP  Leaving out the exclusions because they feel negative. An unstated exclusion is not a smaller
           scope, it is an unmanaged expectation. -->

{{scope_and_non_scope}}

## Risk-Ranked Approach

<!-- WHAT  The areas under test, ranked by product risk, with the reason for each ranking and the depth of
           testing it earns. This is the section that makes the plan a plan.
     WHY   Risk-based testing exists to steer effort rather than spread it evenly: high-risk areas earn
           heavier techniques and are tested FIRST, so that if time runs out what is missing is the least
           important coverage rather than a random sample. A section that only names test types
           ("functional, regression") decides nothing. Deep dive: test-plan_companion.md section 3
           (Risk-Ranked Approach) and section 5.
     ASK   What could go wrong here, and how bad would it be? Which areas therefore carry the most risk? What
           technique and depth does each risk tier earn? What order will they be tested in? Where do these
           risks come from (the PRD, the risk register, a risk-storming session)?
     PRIORITY  Order the table by risk, highest first, and test in that order. Reuse product risks already
           recorded upstream rather than inventing a parallel list. Risks that threaten the TESTING rather
           than the product belong in "Risks to the Test Effort" below, not here.
     ROW HINT  A good row names an area, states the risk as a consequence rather than a theme, gives a tier
           with a reason, and names the technique and depth. A weak row is a feature name with "high" beside
           it.
     GOOD  | Shared-view permissions | A shared view could expose rows the recipient may not see | High: low
           likelihood, severe and irreversible impact (data exposure) | Permission matrix across 3 personas x
           4 filter scopes; negative cases first; security review gate | 1 |
     WEAK  | Sharing | High | Test it thoroughly | 1 |
     TRAP  Ranking everything "high". If every area is top priority, the ranking has told the team nothing
           and the order of work is back to guesswork. -->

| Area under test | Risk (what could go wrong, and the consequence) | Tier and why | Technique and depth | Order |
|---|---|---|---|---|
| {{area}} | {{risk_and_consequence}} | {{tier_and_reason}} | {{technique_and_depth}} | {{order}} |

## Test Levels and Types

<!-- WHAT  Which test levels (unit, integration, system, end-to-end) and which types (functional, performance,
           security, accessibility, compatibility) are in play, who owns each, and which are out.
     WHY   A lean plan omits this because one team already knows. It earns its place the moment more than one
           group tests, a level belongs to somebody else, or a non-functional type needs its own environment,
           data or specialist. Writing it down is what stops two teams both assuming the other covered
           integration. Deep dive: test-plan_companion.md section 3 (Test Levels and Types).
     ASK   Which levels are in scope for this effort, and which are assumed already covered? Which
           non-functional types are required, and by what evidence (an NFR, a regulation, a past incident)?
           Who owns each row? Which types are explicitly not being run?
     PRIORITY  List only levels and types that someone will actually run or explicitly waive. A row with no
           owner is a gap, not a plan.
     ROW HINT  A good row names the level or type, its owner by name, the environment it needs, and the
           evidence that it is required. A weak row is a checkbox with no owner.
     GOOD  | System (API) | Anjali Rao | Staging | Required: the views endpoints are new in this release |
     WEAK  | Performance | TBD | | Nice to have |
     TRAP  Listing every level and type the organization has ever run. This section is a scope statement, not
           a catalog; unowned rows read as coverage that will not happen. -->

| Level or type | Owner | Environment | Why it is required (or waived) |
|---|---|---|---|
| {{level_or_type}} | {{level_owner}} | {{level_environment}} | {{level_rationale}} |

## Entry and Exit Criteria

<!-- WHAT  The conditions that must be true before testing starts, and the conditions that define testing as
           done, with who agreed the exit criteria and when.
     WHY   Criteria are thresholds, not adjectives. "Environment is ready" cannot be checked; a named build in
           a named state can. The functional test for an entry criterion is whether failing it would actually
           stop you: if not, it is not a criterion. Exit criteria are supposed to be agreed with
           stakeholders, and almost every template omits the evidence of that agreement, which is exactly what
           an approvable plan needs to carry. Deep dive: test-plan_companion.md section 3 (Entry and Exit
           Criteria) and section 7.
     ASK   What must exist before testing can start without wasting effort? What would make you stop and say
           testing is finished? How is each condition measured, and by whom? Who agreed the exit criteria, and
           on what date?
     GOOD  "Entry: build 2.3.1 deployed to staging with the flag on; three permission personas seeded; smoke
           suite green. Exit: every High-tier area has its planned cases executed; zero open Sev-1 or Sev-2
           defects in scope; the permission matrix 100 percent executed with no failures. Agreed with Priya
           Nair (PM) and Marcus Bell (Eng lead) on 2026-07-06."
     WEAK  "Entry: environment ready. Exit: 95 percent of tests pass." (the first cannot be checked; the
           second can be satisfied by writing more trivial tests, and a comfortable percentage can hide a
           single catastrophic failure)
     TRAP  A pass-rate number as the only exit criterion. Pair every count-based criterion with a
           risk-coverage criterion and a severity rule, or you have written a target that rewards writing
           easy tests. -->

{{entry_and_exit_criteria}}

## Suspension and Resumption Criteria

<!-- WHAT  What stops testing mid-cycle, who makes that call, and what has to be true to restart.
     WHY   This is the most commonly dropped section of the classic standard and the one teams wish they had
           written when a blocking defect lands on a Thursday afternoon. Deciding it calmly in advance is
           worth more than deciding it under pressure, particularly where a gate exists or an environment is
           shared. Deep dive: test-plan_companion.md section 3 (Suspension and Resumption Criteria).
     ASK   What class of finding should stop the cycle rather than just be logged? Who decides, and who is
           told? What must be true to resume, and does resuming require re-running anything already passed?
           Which failures pause only part of the effort rather than all of it?
     GOOD  "A confirmed permission leak suspends all phase 2 (sharing) testing immediately; Anjali Rao calls
           it and notifies Priya Nair and Marcus Bell the same day. Resumption requires a fix, a passing
           permission matrix re-run in full, and the security review signed. Phase 1 testing continues
           throughout."
     WEAK  "Testing will be suspended if there are too many defects." (no threshold, no decider, no
           resumption condition, and no statement of what keeps running)
     TRAP  Writing a suspension rule with no named decider. In practice the cycle then continues by default
           while people wait for someone to say stop. -->

{{suspension_and_resumption}}

## Environment, Data, and Ownership

<!-- WHAT  Where testing runs, what test data it needs and who provides it, and one named owner per area.
     WHY   Test data is where plans quietly fail: the data that exercises a permission boundary or an error
           path never exists by accident, and manufacturing it is often the longest lead-time item in the
           whole effort. Naming it early is what stops week one being spent making accounts. Deep dive:
           test-plan_companion.md section 3 (Environment, Data, and Ownership).
     ASK   Which environments, at which versions and configurations? What data is needed for the negative and
           boundary cases, and who creates it? What is anonymized or synthetic, and under what policy? Who
           owns each area, by name?
     GOOD  "Staging, build 2.3.x, flag on, seeded nightly from an anonymized production snapshot. Data: three
           personas (owner, permitted viewer, restricted viewer) and two dashboards with a restricted filter
           field, created by Platform (Dana Osei) before entry. Owners: functional and permissions, Anjali Rao;
           performance, Marcus Bell; accessibility, Sofia Marino."
     WEAK  "Test on staging with test data. QA owns testing." (no versions, no data specifics, no named
           person; "QA owns it" is owned by nobody)
     TRAP  Naming a team instead of a person. A team owns nothing on a Friday afternoon. -->

{{environment_data_and_ownership}}

## Schedule and Deliverables

<!-- WHAT  The timebox and milestones for the testing effort, and what testing will hand over at the end.
     WHY   Deliverables set expectations about what exists when testing stops: executed cases, a defect list,
           a summary, and any sign-off artifact. Naming them is also what keeps this plan prospective; if
           results start appearing in it, it has quietly become an execution tracker and stopped being a
           plan. Deep dive: test-plan_companion.md section 3 (Schedule and Deliverables) and section 7.
     ASK   When does testing start and stop, and against which milestones? What gates sit inside the window?
           What artifacts are handed over, to whom, and by when? Where does execution status actually live?
     GOOD  "Window: 2026-07-06 to 2026-07-17, with the security review gate on 2026-07-10 between phase 1 and
           phase 2. Deliverables: executed case results in the test tool, an open-defect list, and a one-page
           summary to the release checklist on 2026-07-17."
     WEAK  "Two weeks of testing before release. Deliverable: test results." (no gates, no owner of the
           handover, no statement of where results live)
     TRAP  Adding status or results columns to this plan. Keep execution state in the tool or the report; a
           plan that tracks itself becomes stale in both roles. -->

{{schedule_and_deliverables}}

## Risks to the Test Effort

<!-- WHAT  The risks that threaten the TESTING, with an owner and a contingency for each. Not the product
           risks that shape coverage; those are in the Risk-Ranked Approach above.
     WHY   These are two different lists, and merging them is why "risks" sections read as noise. Product
           risk: the permission check might leak data, so test it hardest. Project risk: the staging
           environment is shared and might be unavailable in week two, so the schedule needs a contingency.
           The first shapes what you test; the second shapes whether you get to test at all. Deep dive:
           test-plan_companion.md section 3 (Risks to the Test Effort).
     ASK   What could delay, block or invalidate the testing itself? How likely is it, and what would it cost
           in days or coverage? Who owns it? What is the contingency, and what is the trigger for invoking it?
     PRIORITY  Order by expected damage to the effort. Every row needs a named owner and a contingency that
           someone could actually execute; a risk with no contingency is just an anxiety.
     ROW HINT  A good row names the threat to testing, the impact in concrete terms (days, coverage lost), a
           named owner, and a contingency with a trigger. A weak row names a worry with no owner.
     GOOD  | Staging shared with the Billing migration in week 2 | Up to 3 days of blocked execution, losing
           the performance runs | Dana Osei | Book the window now; if lost, run performance against the
           pre-prod replica and note the deviation in the summary |
     WEAK  | Environment issues | Could delay testing | QA | Escalate |
     TRAP  Copying the product risk table into this section. If a row would change what you test rather than
           whether you can test, it belongs above. -->

| Risk to the testing | Impact if it happens | Owner | Contingency and trigger |
|---|---|---|---|
| {{effort_risk}} | {{effort_risk_impact}} | {{effort_risk_owner}} | {{effort_risk_contingency}} |

## Approvals and Change Control

<!-- WHAT  Who approved this plan and when, and how it changes once approved.
     WHY   This section exists for regulated, audited and multi-team contexts, and can be cut everywhere else.
           Its honest purpose is not ceremony: a plan that changes silently after sign-off is worse than one
           never signed, because it carries borrowed authority. The change rule is the part people forget, and
           it is the part that matters on day nine. Deep dive: test-plan_companion.md section 3 (Approvals and
           Change Control) and section 9.
     ASK   Who must approve this, in what role, and what are they actually attesting to? What kind of change
           requires re-approval rather than an edit? Where is the version history kept? Who is told when the
           plan changes?
     PRIORITY  Approvers are named individuals with roles, not distribution lists. State plainly which changes
           need re-approval; "material change" without a definition is not a rule.
     ROW HINT  A good row names a person, a role, what they are approving, and a date. A weak row is a role
           with no name and no date.
     GOOD  | Priya Nair | PM, Reporting | Scope, exclusions and exit criteria | 2026-07-06 |
     WEAK  | Product | | Approved | |
     TRAP  Collecting approvals on a plan nobody has read. A signature on an unread document transfers blame
           rather than creating agreement. -->

| Approver | Role | What they are approving | Date |
|---|---|---|---|
| {{approver}} | {{approver_role}} | {{approval_scope}} | {{approval_date}} |

{{change_control_rule}}
