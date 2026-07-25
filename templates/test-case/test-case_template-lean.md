---
title: "{{case_title}}"
case_id: "{{case_id}}"
verifies: "{{what_this_traces_to}}"
priority: "{{priority}}"
case_status: "{{case_status}}"
last_updated: "{{date}}"
doc_type: test-case
size: lean
source_template: test-case
source_template_version: 0.1.0
---

<!--
LEAN TEST CASE. The smallest specification that is still a real test case: what it verifies and what it
traces to, what must be true before it runs, the steps paired with what should happen, and the state it
leaves behind. Use it for everyday cases written and run by one team. To grow it into a reviewable,
auditable case (see test-case_template-full.md), ADD sections; never rename or reorder the ones below,
because the full variant is a strict superset of this one.

A TEST CASE IS A DESIGN ARTIFACT, NOT A RECORD OF A RUN. There is deliberately no "actual result" and no
pass/fail field below. Those belong to an execution record: one case is run many times, and a specification
that carries the outcome of one run can only be used once. `case_status` above is the lifecycle of this
SPECIFICATION (draft, active, deprecated), not the outcome of a test. See test-case_companion.md sections 3
and 7.

ONE CASE, ONE OBJECTIVE. A case that verifies three things tells you almost nothing when it fails. One
objective does not mean one assertion; a single outcome may need several checks to confirm it.

WHAT A TEST CASE IS, AND IS NOT
It is the specification of ONE verification. It is NOT a test plan (that scopes and ranks a whole effort),
NOT a bug report (that is written after something failed), NOT a test run (that is an execution event), and
NOT necessarily the same thing your team means by "test scenario" or "test script" - those words are used
inconsistently across the industry and even the certification glossary. See test-case_companion.md section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   test-case_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid. For
   the steps table, PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Write the expected results BEFORE you run anything.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you share it: self-grade against test-case_guide.md, then DELETE every HTML comment. They are
   guidance, not content.
-->

# {{case_id}}: {{case_title}}

## Identification and Traceability

<!-- WHAT  What this case verifies in one sentence, and what it traces to: an acceptance criterion, a
           requirement, a risk in the test plan, or a defect it now guards against. Plus its priority.
     WHY   A case that traces to nothing is a case nobody can ever decide to delete, which is how suites turn
           into landfill. Traceability is also what an audit is actually auditing: linking every requirement
           to its test. Deep dive: test-case_companion.md section 3 (Identification and Traceability).
     ASK   What single thing does this verify? What does it trace to, by ID? Why does this case exist - which
           risk or criterion would go uncovered without it? How important is it relative to the others?
     GOOD  "Verifies that a restricted viewer opening a shared view receives only rows within their
           entitlement. Traces to: test plan risk R-05 (High). No acceptance criterion covers this case; it
           comes from test design, not from the agreed criteria. Priority: P1."
     WEAK  "Tests sharing. Priority: high." (verifies nothing specific, traces to nothing, and gives no
           reason to keep or delete it next year)
     TRAP  A title that describes the click path ("open Views menu, click Share") rather than the behavior. A
           behavior title survives a redesign; a path title does not. -->

{{identification_and_traceability}}

## Preconditions and Test Data

<!-- WHAT  The system state, accounts, permissions and configuration that must exist before step 1, and the
           specific data this case uses.
     WHY   This is what decides whether anyone other than the author can run the case and get the same
           answer. Practitioners rank understandability and repeatability at the top of what makes a case
           good, and a missing precondition is the usual cause of a case that "only works for Priya". Deep
           dive: test-case_companion.md section 3 (Preconditions and Test Data).
     ASK   What must already be true: which accounts, which permissions, which feature flags, which data?
           What values does this case feed in? Where does that data come from, and who creates it? What must
           NOT be true (a state that would invalidate the run)?
     GOOD  "Preconditions: saved_views flag on; dashboard DB-7 exists with a Region filter; user R (restricted
           viewer) has dashboard access but no entitlement to region EMEA; user O (owner) has a view on DB-7
           filtered to region=EMEA, scope=shared. Data: view SV-31; users O and R from the standard persona
           set."
     WEAK  "A shared view exists and a user opens it." (which user, with what entitlement, on which
           dashboard, filtered to what? Two testers will construct two different tests)
     TRAP  Folding preconditions into step 1. A precondition is state that must already hold; a step is
           something the test does. Merging them makes the case unrepeatable and hides its dependencies. -->

{{preconditions_and_test_data}}

## Steps and Expected Results

<!-- WHAT  The actions in order, each paired with what should happen. One row per step.
     WHY   The pairing is the case. A step with no expected result is navigation, not verification. And the
           expected result has to be written BEFORE the run: filled in afterwards it is a description of what
           happened, which can never fail. Deep dive: test-case_companion.md section 3 (Steps and Expected
           Results).
     ASK   What is the smallest sequence that exercises this one objective? What should happen at each step,
           observably? Which step is the actual verification, as opposed to setup? How would a tester know it
           failed?
     PRIORITY  Keep the sequence minimal: every step that is not needed to reach or observe the behavior is
           maintenance you pay for forever. Specify behavior and data, not the click path. Do NOT add an
           "actual result" or "pass/fail" column; those belong to the run record.
     ROW HINT  A good row has an action a competent stranger could perform without guessing, and an expected
           result that is observable and specific enough to be wrong. A weak row says "verify it works".
     GOOD  | 3 | As user R, open dashboard DB-7 and select saved view SV-31 | The view loads. Rows are limited
           to regions R is entitled to; no EMEA row appears in the table or in any aggregate total |
     WEAK  | 3 | Open the shared view | It works correctly |
     TRAP  Enumerating every click. Over-specified cases break on cosmetic UI changes that broke nothing, and
           reviewers stop reading them. Under-specified cases cannot be repeated. Aim for what a competent
           tester unfamiliar with the feature needs, and no more. -->

| # | Action | Expected result |
|---|---|---|
| {{step_number}} | {{action}} | {{expected_result}} |

## Postconditions and Teardown

<!-- WHAT  The state the system is left in, and anything that must be cleaned up before the next case runs.
     WHY   A suite is a set of cases where one case's postcondition often becomes the next one's
           precondition. A case that quietly leaves state behind becomes a hidden dependency, and that is the
           usual reason a test passes alone and fails in a suite. Deep dive: test-case_companion.md section 3
           (Postconditions and Teardown).
     ASK   What has changed in the system after this case runs? Does anything need deleting, resetting or
           re-seeding? Can this case run twice in a row without cleanup? Does anything it leaves behind
           affect another case?
     GOOD  "No data is created or modified; the case is read-only. User R's session is ended to avoid
           carrying an authenticated session into the next case."
     WEAK  (section deleted, or "N/A" with no explanation)
     TRAP  Skipping this because the case "does not change anything". Say that explicitly instead - "no state
           change; read-only" is information, and it is what tells the next person they can run this case in
           any order. -->

{{postconditions_and_teardown}}
