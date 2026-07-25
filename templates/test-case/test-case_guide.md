# Guide: Test Case (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`test-case_companion.md`](test-case_companion.md). A fully worked instance is
[`test-case_example.md`](test-case_example.md).

## When to use

- A verification must be repeatable by someone who is not you, next month.
- A defect has been fixed and you want it to stay fixed: a regression case is the guard.
- The behavior is high-risk (entitlement, money, data loss) and you want the check reviewed before it runs.
- The work is regulated or audited and every requirement must link to a test.
- A behavior needs checking under a configuration matrix, where "I tried it" is not evidence.

## When NOT to use

- **Once, throwing away.** Checking something during development that nobody will re-run. Do the check.
- **Instead of exploring.** Cases verify what you already thought of. They do not find the thing you did not
  think of, and a suite that grows while nobody explores is a quiet failure mode.
- **To hit a number.** If cases are being written because a count is being watched, the count is the problem.
- **As a bug report.** A test case is written before, to define correct behavior; a bug report is written
  after, because something was not.
- **As a test plan.** The plan scopes and ranks the effort; the case is one unit inside it.
- **As a record of a run.** No actual-result or pass/fail field belongs in the specification. One case, many
  runs.

## Case, scenario, script, or criterion? (the question people actually have)

| You want to say | Write |
|---|---|
| What must be true for the business to accept this story | An **acceptance criterion** (`acceptance-criteria`) |
| How we verify one specific behavior, repeatably | A **test case** (this template) |
| What we are testing, at a high level, before designing cases | Most teams call this a **test scenario** |
| The ordered sequence in which a set of cases is run | Most teams call this a **test script** or procedure |

**A warning about those last two rows.** The ISTQB glossary does not draw the line most practitioners draw:
it gives *test procedure* and *test script* identical definitions, and defines *test scenario* as a synonym
for test script rather than as a high-level description. Your team's usage is probably the folk taxonomy, and
that is fine. What is not fine is assuming everyone shares it. Write down which you mean; the vocabulary will
not settle it for you (companion section 8).

**And the one that matters most.** Acceptance criteria are agreed with the business before the work; test
cases are designed by whoever tests, and they continue past the agreement into negative paths, boundaries,
regression and non-functional checks that nobody signed off on. Some practitioners argue the two should be
merged, and that is a real position with real practitioners behind it. Whichever you choose, choose it
deliberately: the failure mode is assuming the criteria already cover what test design would have found
(companion section 6).

## Pick a variant

**Lean (four sections)** is the default and should stay the default: Identification and Traceability,
Preconditions and Test Data, Steps and Expected Results, Postconditions and Teardown. A test case is written
hundreds of times over a project, so every field costs hundreds of times.

**Full (eight sections)** adds Design Rationale, Environment and Configuration, Automation Status, and Version
and Approval. Reach for it when:

- the work is regulated or audited and the case is evidence;
- cases are reviewed as artifacts, not just executed;
- the case is configuration-sensitive and a result is meaningless without the configuration;
- the suite is large enough that knowing *why* a case exists is what lets you retire it.

Note that the master catalog marks this type single-size. This bundle ships two anyway, for the reasons in
companion section 4; the catalog's size calls are hypotheses, and this is one tested against evidence.

## Quality rubric (self-grade)

Score each 0, 1 or 2. Under 11 out of 16 and the case will not survive its first re-run by someone else.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **One objective** | Verifies several unrelated things | Mostly one thing | Exactly one objective, stated in the title |
| 2 | **Traceable** | Traces to nothing | Named loosely | Traces to a specific ID: criterion, requirement, risk or defect |
| 3 | **Preconditions real** | None stated | Vague ("user is logged in") | Specific enough that a stranger can construct the state |
| 4 | **Expected results pre-written** | Blank or written after the run | Present but vague | Observable, specific, and written before execution |
| 5 | **No execution state** | Has actual-result and pass/fail fields | One creeping in | Pure specification; runs recorded elsewhere |
| 6 | **Independent** | Requires another case to run first | Implicit ordering | Runs in any order; postconditions stated |
| 7 | **Right level of detail** | Every click, or "check it works" | Uneven | A competent stranger could run it; no more than that |
| 8 | **Title survives a redesign** | Describes the click path | Mixed | Describes the behavior and the condition |

## Named anti-patterns (the usual wrecks)

1. **The single-use case.** Actual-result and status fields baked into the specification, so the reusable
   artifact and one run's record are the same file. Fix: keep run state in the tool.
2. **Retrofitted expectations.** Expected results written after execution. They cannot fail. Fix: write them
   first, always.
3. **The three-in-one.** One case verifying three things, so a failure tells you nothing. Fix: split it.
4. **Order dependence.** Passes in the suite, fails alone, because a predecessor left state behind. Fix: real
   preconditions, real teardown.
5. **Click-by-click.** Every UI interaction enumerated, so the case breaks on a redesign that broke nothing.
   Fix: specify behavior and data, not the path.
6. **"Log in and check it works."** Not repeatable by anyone but the author. Fix: preconditions and an
   observable expected result.
7. **The orphan.** Traces to nothing, so nobody can tell whether it still matters, and it is never deleted.
   Fix: every case names what it covers.
8. **Counting cases.** "We have 5,000 tests" says nothing, and once the count is a target it gets gamed with
   shallow cases. Fix: measure risk coverage, never volume.

## Pairing with a skill

`pairs_with: [deliver-edge-cases]`. There is **no testing or QA skill** in the `pm-skills` library (finding
EC-4 in the repository's `STATE.md`). `deliver-edge-cases` is the one honest pairing, and for this member it
is a particularly direct one: the edge-case catalog it produces is exactly the negative, boundary and
error-state territory that acceptance criteria do not cover, which is where a large share of test cases should
come from. See companion sections 6 and 8.
