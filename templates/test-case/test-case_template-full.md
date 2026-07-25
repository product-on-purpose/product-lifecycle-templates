---
title: "{{case_title}}"
case_id: "{{case_id}}"
verifies: "{{what_this_traces_to}}"
priority: "{{priority}}"
case_status: "{{case_status}}"
case_version: "{{case_version}}"
last_updated: "{{date}}"
doc_type: test-case
size: full
source_template: test-case
source_template_version: 0.1.0
---

<!--
FULL TEST CASE. The reviewable, auditable case: everything the lean variant carries, plus why this case was
designed the way it was, the environment it is valid for, its automation link, and its version and approval
record. Use it when the work is regulated or audited, when cases are reviewed as artifacts rather than just
executed, when a configuration matrix is in play, or when the suite is large enough that knowing WHY a case
exists is what lets you retire it later.

THIS VARIANT IS A STRICT SUPERSET OF THE LEAN ONE. The four lean sections appear here in the same order, with
the same headings and the same placeholders, and four sections are added. Growing a lean case into this one
is additive.

BE SPARING WITH THIS VARIANT. A test case is written hundreds of times over a project, so every extra field
is paid for hundreds of times. Reach for full where the extra fields are actually consumed by a reviewer, an
auditor or an automation pipeline - not by default. See test-case_companion.md section 4.

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
   tables, PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Write the expected results BEFORE you run anything.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you submit it for review: self-grade against test-case_guide.md, then DELETE every HTML comment.
   They are guidance, not content.
-->

# {{case_id}}: {{case_title}}

## Identification and Traceability

<!-- WHAT  What this case verifies in one sentence, and what it traces to: an acceptance criterion, a
           requirement, a risk in the test plan, or a defect it now guards against. Plus its priority.
     WHY   A case that traces to nothing is a case nobody can ever decide to delete, which is how suites turn
           into landfill. In an audited context this section is the spine of the traceability matrix: linking
           every requirement to its test is the thing being checked. Deep dive: test-case_companion.md
           section 3 (Identification and Traceability).
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

## Design Rationale

<!-- WHAT  Which test design technique produced this case, and why these values rather than others.
     WHY   This is what makes a case reviewable rather than merely runnable, and it is what lets someone
           later decide the case is redundant. Naming the technique also exposes gaps: if every case in a
           suite says "happy path", nobody has done boundary or combination analysis. Deep dive:
           test-case_companion.md section 3 (Design Rationale).
     ASK   Which technique derived this: equivalence partitioning, boundary value analysis, a decision table,
           state transition, combinatorial? Why these specific values? Which partition or boundary does this
           case represent, and which sibling cases cover the others? What is deliberately NOT covered here?
     GOOD  "Equivalence partitioning on entitlement: the partitions are entitled, partially entitled and not
           entitled. This case covers partially entitled, which is the partition where a filter-level leak
           can occur; TC-046 and TC-048 cover the other two. Boundary values are not meaningful for a
           set-membership check, so BVA is not applied."
     WEAK  "Negative test." (names no technique, no partition, and gives no way to tell whether the set of
           cases is complete)
     TRAP  Writing the rationale after the fact to satisfy the heading. If you cannot name why these values,
           the case may be arbitrary - which is worth discovering now rather than in a review. -->

{{design_rationale}}

## Environment and Configuration

<!-- WHAT  The environment, build, configuration and device or browser matrix this case is valid for.
     WHY   A case that passed somewhere is only evidence about that somewhere. Where a case is
           configuration-sensitive, an unrecorded environment makes the result unreproducible and, in an
           audit, unusable. Deep dive: test-case_companion.md section 3 (Environment and Configuration).
     ASK   Which environment and build is this case valid against? Which configurations must it be run under,
           and which are out of scope? Is the case sensitive to data volume, locale, timezone or device? What
           would invalidate a past result?
     GOOD  "Staging, build 2.3.1 or later, saved_views flag on. Entitlement checks are evaluated server-side,
           so this case is browser-independent and is run once on Chrome; the accessibility cases cover the
           browser matrix separately."
     WEAK  "Any environment." (either untrue or an admission that nobody has thought about it)
     TRAP  Listing a matrix nobody will run. A configuration named here is a commitment; if it will not be
           covered, say which are out of scope and why. -->

{{environment_and_configuration}}

## Automation Status

<!-- WHAT  Whether this case is automated, what it is linked to, and what the automation does NOT cover.
     WHY   Automating a case changes its role rather than retiring it: the case stays the specification and
           the code becomes an implementation of it. Recording the link is also how you avoid the common
           surprise that manual parameters do not carry into an automated run. Deep dive:
           test-case_companion.md section 3 (Automation Status) and section 8.
     ASK   Is this automated, planned for automation, or deliberately manual? Where does the automated test
           live, by path or ID? What does the automated version not check that the manual one did? Who owns
           the automation?
     GOOD  "Automated. Linked to `tests/entitlement/shared_view_restricted_viewer_spec.rb`. The automated
           version asserts on the API response only; the check that no EMEA value appears in a rendered
           aggregate total remains manual and is run once per release."
     WEAK  "Yes." (no link, no owner, and no statement of what the automation gave up)
     TRAP  Deleting the manual case once it is automated. The case is the specification of what should be
           true; the automation is one way of checking it, and it usually checks less. -->

{{automation_status}}

## Version and Approval

<!-- WHAT  The version of this case, who reviewed or approved it, and when.
     WHY   This exists for regulated and audited work, where the case is evidence rather than a convenience.
           The bar does not depend on who or what wrote the case: a generated case carries the same
           traceability and version-control obligation as a hand-written one. Everywhere else, delete this
           section and let version control do its job. Deep dive: test-case_companion.md section 3 (Version
           and Approval) and section 9.
     ASK   What version is this, and what changed from the last one? Who reviewed it, in what role, and on
           what date? What kind of change requires re-review rather than an edit? Where does the history
           live?
     PRIORITY  Reviewers are named individuals with roles, never a team. State plainly which changes need
           re-review; "material change" with no definition is not a rule.
     ROW HINT  A good row names a person, a role, what they reviewed, and a date. A weak row is a role with
           no name and no date.
     GOOD  | Sam Okafor | Security | Entitlement assertions and the partition choice | 2026-07-08 |
     WEAK  | QA | | Reviewed | |
     TRAP  Collecting approvals on a case nobody executed. A signature on an unrun case attests to the
           document, not to the software. -->

| Reviewer | Role | What they reviewed | Date |
|---|---|---|---|
| {{reviewer}} | {{reviewer_role}} | {{review_scope}} | {{review_date}} |

{{version_and_change_rule}}
