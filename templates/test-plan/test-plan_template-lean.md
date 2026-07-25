---
title: "{{release_or_feature}} Test Plan"
release_or_feature: "{{release_or_feature}}"
plan_owner: "{{plan_owner}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: test-plan
size: lean
source_template: test-plan
source_template_version: 0.1.0
---

<!--
LEAN TEST PLAN. The smallest plan that is still a real plan: what is in and out, how deeply each area will be
tested and why, the conditions that start and stop the work, who runs it where, and when. Use it for a
feature or a release owned by one team. To grow it into a formal, approvable plan (see
test-plan_template-full.md), ADD sections; never rename or reorder the ones below, because the full variant
is a strict superset of this one.

THE PLAN IS NOT THE DOCUMENT. The value is in the thinking this forces, not in the page count. A plan nobody
reads is not a safety net. Keep it short enough that the team actually reads it, and specific enough that
someone else could check it. Delete any section that would change nothing if it were missing, and say why.
See test-plan_companion.md sections 1 and 6.

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
4. Before you share it: self-grade against test-plan_guide.md, then DELETE every HTML comment. They are
   guidance, not content.
-->

# {{release_or_feature}} Test Plan

## Scope and Non-Scope

<!-- WHAT  What is being tested (the concrete test items: builds, services, flag states, requirement IDs) and
           what is explicitly NOT being tested this cycle, with a reason for each exclusion.
     WHY   The exclusion half is the highest-value content in the document and the most commonly deleted. If
           nothing is out of scope, nothing can be found missing, and the scope argument happens after the
           release instead of before it. Writing it down converts an assumption into an agreement. Deep dive:
           test-plan_companion.md section 3 (Anatomy > Scope and Non-Scope).
     ASK   What exactly is under test, by build or requirement ID? What is deliberately excluded, and why
           (deferred, covered elsewhere, accepted risk)? Who agreed to the exclusions?
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
           recorded upstream rather than inventing a parallel list. Risks that threaten the TESTING (not the
           product) do not belong here; in the full variant they have their own section.
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

## Entry and Exit Criteria

<!-- WHAT  The conditions that must be true before testing starts, and the conditions that define testing as
           done, with who agreed the exit criteria and when.
     WHY   Criteria are thresholds, not adjectives. "Environment is ready" cannot be checked; a named build in
           a named state can. The functional test for an entry criterion is whether failing it would actually
           stop you: if not, it is not a criterion. Exit criteria are supposed to be agreed with
           stakeholders, and almost every template omits the evidence of that agreement. Deep dive:
           test-plan_companion.md section 3 (Entry and Exit Criteria) and section 7.
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

## Environment, Data, and Ownership

<!-- WHAT  Where testing runs, what test data it needs and who provides it, and one named owner per area.
     WHY   Test data is where plans quietly fail: the data that exercises a permission boundary or an error
           path never exists by accident, and manufacturing it is often the longest lead-time item in the
           whole effort. Naming it early is what stops week one being spent making accounts. Deep dive:
           test-plan_companion.md section 3 (Environment, Data, and Ownership).
     ASK   Which environments, at which versions and configurations? What data is needed for the negative and
           boundary cases, and who creates it? What is anonymized or synthetic? Who owns each area, by name?
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
           a summary. Naming them is also what keeps this plan prospective; if results start appearing in it,
           it has quietly become an execution tracker and stopped being a plan. Deep dive:
           test-plan_companion.md section 3 (Schedule and Deliverables) and section 7.
     ASK   When does testing start and stop, and against which milestones? What gates sit inside the window?
           What artifacts are handed over, to whom? Where does execution status actually live?
     GOOD  "Window: 2026-07-06 to 2026-07-17, with the security review gate on 2026-07-10 between phase 1 and
           phase 2. Deliverables: executed case results in the test tool, an open-defect list, and a one-page
           summary to the release checklist on 2026-07-17."
     WEAK  "Two weeks of testing before release. Deliverable: test results." (no gates, no owner of the
           handover, no statement of where results live)
     TRAP  Adding status or results columns to this plan. Keep execution state in the tool or the report; a
           plan that tracks itself becomes stale in both roles. -->

{{schedule_and_deliverables}}
