# Guide: Experiment Design Doc (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`experiment-design-doc_companion.md`](experiment-design-doc_companion.md). A fully worked instance is
[`experiment-design-doc_example.md`](experiment-design-doc_example.md).

**One honest limit before anything else.** No source read for this bundle measured whether writing this
document improves an experiment's outcome. The case for it rests on practitioner testimony and on the
statistics of what goes wrong without a pre-committed stopping rule, not on a controlled comparison of
documented against undocumented tests. Read the rest of this card with that limit in mind.

## When to use

- A product change is about to be tested against a baseline with real traffic, and the decisions that
  follow the result are expensive enough to fix in advance rather than argue about after the data arrives.
- More than one person needs to agree, before anyone has seen any data, on what counts as a win, a null
  result, and a loss.
- The surface is mature, or the blast radius of a mistake on it is large enough that a pre-committed
  stopping rule and a shutdown threshold are worth the extra page.
- The team runs on a shared experimentation platform whose statistical framework this document can simply
  name, rather than argue out per test.

## When NOT to use

- **You will ship the change regardless of what the test shows.** Running a controlled test to confirm a
  decision already made spends real complexity on nothing. Skip the experiment.
- **The population available is too small to produce a result anyone could act on.** A low-traffic surface
  cannot reach a trustworthy effect size no matter how carefully this document is written. Pick a cheaper
  validation method instead.
- **A cheaper method, such as a user interview or a smoke test, would already answer the question.**
  Fixating on controlled experiments for every idea sets the bar too high for the easy cases.
- **You need a qa-docs test plan.** A test plan verifies a product increment against an agreed
  specification and grades it pass or fail. It carries no hypothesis, no allocation between variants, and
  no statistical decision rule. This document tests an open hypothesis and estimates an effect against a
  baseline. See companion section 8 for the boundary in full.
- **You need a spike report (decision-docs).** A spike reduces uncertainty about a technical or design
  question, with no control group and no statistical decision rule; a refuted hypothesis there is a
  successful spike. That is never true of a result reported here. See companion section 8.
- **Nothing is built yet, and the question is only whether to build it.** A test run before anything exists,
  to decide whether to build it at all, is excluded from this family by name; it is not this document's job
  under any variant.
- **You need a standing instrument, not a one-time record.** A tracking plan, a data dictionary, or an
  experiment log is maintained across many tests and is never finished. This document is written once per
  test and is finished when the test's own decision is recorded. See companion section 8.

## Pick a variant

**Lean (five sections)** is the default: Hypothesis, Population/Variants/Allocation, Primary and Guardrail
Metrics, Minimum Detectable Effect and Sample Size or Duration, and Decision Rule. Use it while a team is
running its first tests, or on a small test where those five sections already force every decision that
matters.

**Full (seven sections)** adds Tracking and Instrumentation Note and Validity Pre-Commitments. Use it when
at least one of these is true:

- the experimentation program is mature enough to need a pre-committed shutdown threshold and a ramp-up
  plan, not only a decision rule;
- the surface is high-traffic or high-stakes enough that the blast radius of a mistake is large;
- the context is regulated or public-sector-adjacent, where proportionality to stakes is itself a named
  expectation rather than a courtesy.

Every lean heading appears in full, unchanged in name and order, so growing from lean to full never means
rewriting a section you already filled in.

## The rubric (self-grade)

Score each row 0, 1 or 2. **Score a full-variant document under 11 out of 16, and the test launches with no
stopping point anyone can act on: the readout that follows will spend its own time reconstructing decisions
the design doc should have already made.** The lean variant scores against fewer rows; see the scope table
below.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Hypothesis is falsifiable** | States a goal ("increase open rate") with no mechanism and no way to know it failed | States a mechanism or the losing condition, but not both, or states evidence with no stated connection to the mechanism | States the mechanism, cites the evidence already pointing that way, and names the specific result that would prove it wrong |
| 2 | **Randomization unit is justified** | No randomization unit is stated | A unit is named, with no stated reason | A unit is named, and the reason ties to who or what the change is visible to, ruling out spillover to someone outside their own assignment |
| 3 | **Metrics carry a baseline** | A metric is named with no baseline and no target or margin | A baseline or a target/margin is given, not both, or the table restates the PRD's own metrics with no statement of whether this test needs its own numbers | Every row has both a baseline and a target or margin, and the document states in one line whether any row needs nothing beyond what the PRD already carries |
| 4 | **Sample size is derived** | A duration or sample size appears with no stated effect size and no named statistical framework | An effect size or a framework is named, not both, or a framework is named with no stated commitment against reviewing results early | The effect size, the named framework, and the resulting sample size or duration are all stated, with an explicit commitment not to review results before that point |
| 5 | **Decision rule covers outcomes** | Only a win outcome has a named action | A win and one of (null result, guardrail breach) have named actions; the other does not | A win, a null result, and an early guardrail breach each have a named action, and the named decision-maker matches the frontmatter |
| 6 | **Tracking note is specific** *(full)* | No events are named, or the note repeats the PRD's instrumentation section with nothing said about what differs | Events are named but the exposure event is missing, or a verification is claimed with no stated date or environment | The exposure event is named, the existing events feeding each metric are named, and a verification is stated with the environment and the date it happened |
| 7 | **Validity checks are owned** *(full)* | A row names a worry with no threshold and no owner | Some rows carry both a threshold and a named owner; others carry one or neither | Every row that applies names a threshold or trigger and a named owner, and a check that does not apply says so in one line rather than being dropped silently |
| 8 | **Overlap and risk are named** *(full)* | Both the overlap line and the risk line are empty, or a bare "N/A" with no stated reason | One of the two names a concrete practice; the other is generic or missing | The overlap line names a specific mechanism or states in one line why none applies, and the risk line names specific people or teams told, not a general claim that "stakeholders know" |

**Which rows apply to what.**

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| full | all 8 | 16 | **11** |
| lean | 1-5 | 10 | **7** |

**Rows 6, 7 and 8 are scored only against the full variant.** The lean variant ships no Tracking and
Instrumentation Note and no Validity Pre-Commitments section, so grading it on those rows would penalize
the choice of variant rather than the quality of the document.

Every cell above is written to resist the gaming test: could a document satisfy it without actually getting
better? A cell that only asks for a count, such as "names at least two checks," can be satisfied by padding
a table with rows that name nothing concrete. Every 2-point cell above instead asks you to point at a
specific sentence, a specific number, or a specific name, which is why it cannot be satisfied by volume
alone.

## Named anti-patterns

**Restating the PRD's metrics, renamed.** The tell: the Primary and Guardrail Metrics table repeats the
PRD's primary metric, guardrail and measurement window with no new baseline or margin of its own. The fix:
state only what this test adds beyond the PRD, or write in one line that this test needs nothing beyond
what the PRD already states. Deep dive: companion section 3 (Anatomy > Primary and Guardrail Metrics) and
section 7.

**Peeking, called monitoring.** The tell: someone checks the results before the committed sample size or
duration is reached, and treats what they see as informing whether to stop, rather than as informational
only. The fix: fix the sample size or duration in this document before the test launches, and treat any
early look as informational unless a sequential design was named in the Minimum Detectable Effect section.
Deep dive: companion section 3 (Anatomy > Minimum Detectable Effect and Sample Size or Duration) and
section 7.

**Presenting a borrowed duration as a standard.** The tell: a draft states a fixed duration, such as a
week, with no effect size, no variance estimate, and no named framework behind the number. The fix: derive
the duration from the effect size and variance this specific test needs, using the platform's own
calculator. A reported typical duration from one company's own program is not a field-wide convention. Deep
dive: companion section 6, item 5.

**Leaving the null outcome undecided.** The tell: the Decision Rule names an action for a win and says
nothing about what happens if nothing moves. The fix: name an action for the null outcome with the same
specificity as the win, before the test launches; a fully powered test that shows no movement is a result,
not a failure to get one. Deep dive: companion section 3 (Anatomy > Decision Rule).

**Treating a vendor's in-tool surface as a substitute for this document.** The tell: the team points at a
live dashboard, a configured experiment, or an exported results file and calls that the design document.
The fix: keep the written rationale here. An in-tool configuration or analysis surface is built for setup
and reporting, not for recording why the test exists or what each outcome will mean. Deep dive: companion
section 7.

**Amending the design silently after launch.** The tell: the sample size, a metric, or the decision rule
changes mid-test, and the document is edited in place with no record of what changed or why. The fix:
record the amendment and the reason in the document itself, rather than quietly editing the original. Deep
dive: companion section 7.

**Running an experiment a cheaper method would already answer.** The tell: the team will ship the change
regardless of the result, or the available population is too small to produce a result anyone could act on.
The fix: this is a decision for before you open this template; the "When NOT to use" section above names it
directly. Deep dive: companion section 7.

**Borrowing a frequency claim no source actually makes.** The tell: a draft states a frequency for why
experiments fail, or calls a practice "universal," with no specific source behind the claim.
The fix: state only the design principle actually supported, and drop the frequency claim entirely rather
than hunting for a citation to justify a sentence already written. Deep dive: companion section 7 and
[`docs/internal/review-standards.md`](../../docs/internal/review-standards.md) section 5.

## When it is good enough

When a reader who was not in the room could tell, from the document alone, what action each possible result
triggers and who makes that call. A design document that still requires a meeting after the results arrive
to decide what they mean has not finished its own job.

Then self-grade against the rubric above, fill in the frontmatter owner, reviewers, decision-maker, status,
planned start date and duration, and delete every HTML comment before sharing it.
