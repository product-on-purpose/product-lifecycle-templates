---
title: "{{experiment_name}} Experiment Design Doc"
experiment_name: "{{experiment_name}}"
owner: "{{owner}}"
reviewers: "{{reviewers}}"
decision_maker: "{{decision_maker}}"
status: "{{status}}"
planned_start_date: "{{planned_start_date}}"
planned_duration: "{{planned_duration}}"
last_updated: "{{date}}"
doc_type: experiment-design-doc
size: full
source_template: experiment-design-doc
source_template_version: 0.1.0
---

<!--
FULL EXPERIMENT DESIGN DOC. Everything the lean variant carries, plus a note on what feeds each metric and
the exposure event that is new to this test, and a set of checks fixed before the test runs that decide
whether its result will be trustworthy. Use it when the program is mature enough to need a pre-committed
shutdown threshold and a ramp-up plan, or when the blast radius of a mistake on this surface is large.

THIS VARIANT IS A STRICT SUPERSET OF THE LEAN ONE. The five lean sections appear here in the same order, with
the same headings and the same placeholders, and two sections are added at the end. If you started lean, you
can grow into this without rewriting anything you already filled in.

WHAT AN EXPERIMENT DESIGN DOC IS, AND IS NOT
It is written before the test launches, while nobody has seen any data, to fix the decisions a team would
otherwise make only after seeing the results. It is NOT the PRD's Success metrics section restated: that
section already names a primary metric, a guardrail and a measurement window, and this document starts past
that point, with the variants, the allocation, the minimum detectable effect, and the decision rule. It is
NOT a spike report: a spike reduces uncertainty about a technical question and carries no control group or
statistical decision rule. It is NOT a qa-docs test plan: a test plan verifies a product increment against
an agreed specification and grades it pass or fail, while this document tests an open hypothesis and
estimates an effect against a baseline. See experiment-design-doc_companion.md section 8.

NO SOURCE MEASURED WHETHER WRITING ONE IMPROVES AN EXPERIMENT'S OUTCOME
The case for this document rests on practitioner testimony and on the statistics of what goes wrong without a
pre-committed stopping rule, not on a controlled comparison of documented against undocumented tests. See
experiment-design-doc_companion.md section 1.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   experiment-design-doc_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to
   avoid. For table sections, PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Fill Hypothesis and Primary and Guardrail Metrics first;
   every section after them depends on what you name there.
3. The owner, reviewers, decision-maker, status, planned start date and duration live in the frontmatter
   above, not in a body section. See experiment-design-doc_companion.md section 3.
4. If a section does not apply, write "N/A" and one line of why, rather than deleting it silently. This
   applies to individual rows of the Validity Pre-Commitments table as much as to a whole section: a check
   this test cannot run, such as a ramp-up plan on a test too small to ramp, is still worth one line saying
   so.
5. Before you share it: self-grade against experiment-design-doc_guide.md, then DELETE every HTML comment.
   They are guidance, not content.
-->

# {{experiment_name}} Experiment Design Doc

## Hypothesis

<!-- WHAT  What you believe will happen, why you believe it, the evidence already behind that belief, and
           what result would prove you wrong.
     WHY   Every convention in use agrees on one thing: the hypothesis must be falsifiable, and the evidence
           behind it belongs in this same sentence rather than a separate section. No source converges on one
           sentence form; this field is left free text on purpose, because at least four distinct, named
           conventions are in circulation and no source argues its own form is correct over the others. Deep
           dive: experiment-design-doc_companion.md section 3 (Anatomy > Hypothesis).
     ASK   What do you believe will happen, and why, in mechanism terms rather than a wish? What evidence,
           qualitative or quantitative, already points this way? What result would prove the hypothesis
           wrong?
     GOOD  "If we send the weekly digest at 9am local time instead of 6am, then open rate will rise, because
           recipients check email after arriving at work rather than before it. Supporting evidence: a
           support-ticket review found several users asking to delay the send. We will know we are wrong if
           open rate among the 9am group is no higher than the 6am control."
     WEAK  "We think the new send time will help engagement." (no mechanism, no stated evidence, no condition
           that would prove it wrong)
     TRAP  Writing a goal instead of a hypothesis. "Increase open rate" is an outcome you want; it is not a
           bet that can turn out to be wrong, and a hypothesis that cannot lose is not one. -->

{{hypothesis}}

## Population, Variants, and Allocation

<!-- WHAT  Who is eligible for the test and what excludes someone, how many variants it carries and what each
           one changes, what share of traffic each variant gets, and the unit the test randomizes on.
     WHY   The randomization unit is a real design choice, not a formality: when a change is visible to people
           connected to each other, such as teammates or a shared account, randomizing by the wrong unit
           violates the assumption that one person's assignment does not affect another's outcome, and the
           test's results stop meaning what they appear to mean. Deep dive: experiment-design-doc_companion.md
           section 3 (Anatomy > Population, Variants, and Allocation).
     ASK   Who is eligible, and what excludes someone (a beta cohort, a region, an existing treatment)? How
           many variants, and what does each one actually change? What share of traffic does each get? What is
           the randomization unit, and could the change spill over to someone outside their own assignment?
     GOOD  "Eligible: active weekly-digest subscribers on the standard plan, excluding anyone already in the
           digest-frequency beta. Two variants: control (6am send, unchanged) and treatment (9am send), 50/50
           split. Randomization unit: subscriber account, because the digest is sent once per account
           regardless of how many people read it, so account-level randomization avoids splitting a shared
           inbox across two send times."
     WEAK  "Everyone in the test gets either the old time or the new time." (no eligibility rule, no stated
           split, no randomization unit)
     TRAP  Leaving the randomization unit unstated. A change visible to a user's teammates or household needs
           a unit bigger than the individual, and discovering that gap after launch is expensive to fix. -->

{{population_variants_and_allocation}}

## Primary and Guardrail Metrics

<!-- WHAT  The one or two metrics that decide whether the hypothesis held, each with its baseline; the
           guardrail metrics that must not get worse, each with the margin that defines a breach. This is not
           the PRD's Success metrics section restated.
     WHY   A PRD's Success metrics section already names a primary metric, a guardrail and a measurement
           window; this section's job is to carry the baseline and margin this specific test is sized around,
           not to repeat what the PRD already states. The more metrics a test analyzes for significance, the
           greater the chance one of them moves by chance alone rather than because of the change, which is
           why the sources that warn about this converge on capping primary metrics at one or two even though
           none agrees on the exact ceiling. Deep dive: experiment-design-doc_companion.md section 3 (Anatomy
           > Primary and Guardrail Metrics) and section 6, item 6.
     ASK   What is the primary metric, and its current baseline? What guardrails must not get worse, and by
           how much before that counts as a breach? Does any row duplicate a metric the PRD already names,
           and if so, does this test need its own baseline or margin for it, or does it need nothing beyond
           what the PRD already states?
     PRIORITY  List the primary metric or metrics first, then guardrails. Keep primary metrics to one or two
           and guardrails to a handful; a long list of primary metrics has usually stopped deciding anything
           and started hoping one of them moves.
     ROW HINT  A good row names the metric, states whether it is primary or guardrail, gives a numeric
           baseline, and states the target or margin that defines success or breach. A weak row is a metric
           name with no baseline and no threshold.
     GOOD  | Digest open rate (24h) | primary | 31% | Target: +3 points or more |
     WEAK  | Engagement | primary | | Higher is better |
     TRAP  Copying the PRD's metrics section verbatim into this table. If this test needs its own baseline or
           margin, state it; if it needs nothing beyond what the PRD already carries, say that in one line
           instead of restating the PRD's own numbers. -->

| Metric | Type (primary or guardrail) | Baseline | Target or guardrail margin |
|---|---|---|---|
| {{metric_name}} | {{metric_type}} | {{metric_baseline}} | {{metric_target_or_margin}} |

## Minimum Detectable Effect and Sample Size or Duration

<!-- WHAT  The smallest effect worth detecting, the statistical framework the test actually runs on, and the
           sample size or duration that follows from both, fixed before the test starts.
     WHY   This is the content no other document in this library carries, and it is the point of the whole
           section: committing to a sample size or duration in advance, before any data arrives, is what
           stops a team from deciding the test is done once the numbers happen to look good. Which statistical
           framework a test uses (fixed-horizon, sequential, or Bayesian) is a live, unresolved question
           across sources; this field asks you to name the one your platform actually runs rather than
           choosing one for you, and no power level or significance threshold is treated as a default here.
           Deep dive: experiment-design-doc_companion.md section 3 (Anatomy > Minimum Detectable Effect and
           Sample Size or Duration) and section 6, items 3 and 5.
     ASK   What is the smallest effect worth acting on if you saw it? What statistical framework does the
           team's platform run on, and who chose it for this test? What sample size or duration follows from
           the effect size, the expected variance, and current traffic? Is the commitment not to look at
           results before that point written down, not just assumed?
     GOOD  "MDE: 3 percentage points on open rate. Framework: fixed-horizon, the team's platform default.
           Duration: 14 days, from the platform's own sample-size calculator given current send volume and
           the stated MDE. The team will not review results before day 14 except to confirm the test is
           running."
     WEAK  "We will run it for a couple of weeks and check." (no effect size, no named framework, no stated
           commitment against looking early)
     TRAP  Treating a reported duration from another team's program, such as "about a week," as a rule for
           this test. A borrowed norm is not a substitute for a number derived from this test's own effect
           size, variance, and traffic; see experiment-design-doc_companion.md section 6, item 5. -->

{{mde_and_sample_size_or_duration}}

## Decision Rule

<!-- WHAT  The action the team commits to for every outcome the test can produce, including a null result and
           an early guardrail breach, decided before any data arrives, and who makes the call.
     WHY   Every source in this lineage ties a named action to every outcome a test can produce, including the
           outcome where nothing moves; deciding this only after seeing the data is the exact failure this
           whole document exists to prevent. "Ship, iterate or stop" is this family's own wording for the
           three-way choice, not a phrase a cited source uses verbatim. Deep dive:
           experiment-design-doc_companion.md section 3 (Anatomy > Decision Rule) and section 6, item 8.
     ASK   What happens if the primary metric moves favorably past the MDE with no guardrail breach? What
           happens if it does not move, and the test was fully powered to detect it if it existed? What
           happens if a guardrail breaches its margin before the test finishes? Who makes the final call, and
           is that the same person named as decision-maker in the frontmatter?
     GOOD  "Win (open rate up 3 points or more, no guardrail breach): ship 9am as the new default. Null (no
           detectable movement, test ran to its full powered duration): keep 6am; do not re-run this exact
           test without a new hypothesis. Guardrail breach (unsubscribe rate exceeds its margin at any point):
           stop the test immediately, regardless of the primary metric's reading. Decision-maker: the
           digest's product owner, named in the frontmatter above."
     WEAK  "We'll ship it if it works out." (no definition of what counts as working, no stated action for a
           null result, no stop condition, no named decision-maker)
     TRAP  Leaving the null result undecided. A fully powered test that shows no movement is a result, not a
           failure to get one, and it needs its own named action as much as a win does. -->

{{decision_rule}}

## Tracking and Instrumentation Note

<!-- WHAT  Which existing events feed each metric named above, any new event this test needs, the
           test-specific exposure event that marks who saw which variant, and a statement that tracking has
           been verified before launch rather than assumed. This is a pointer, not a restatement of the PRD's
           own instrumentation section.
     WHY   The PRD's own Analytics and instrumentation section already lists the events a feature needs; what
           this note adds is which of those events, plus anything new, actually feed this test's metrics, and
           the exposure event that has no PRD equivalent because it belongs to the test rather than the
           feature. A test that launches with its metrics defined but its events unverified discovers the gap
           only once it is too late to fix cheaply. Deep dive: experiment-design-doc_companion.md section 3
           (Anatomy > Tracking and Instrumentation Note).
     ASK   Which existing events feed each metric above? What new event, if any, does this test need that the
           feature's own instrumentation does not already fire? What is the exposure event, and does it fire
           correctly for every variant? Has tracking been checked in a lower environment before launch, and
           on what date?
     GOOD  "Open rate: existing `digest_opened` event, unchanged. Unsubscribe rate: existing `unsubscribed`
           event, unchanged. New exposure event: `digest_send_variant_assigned`, firing at send time with the
           variant id as a property. Verified in staging on 2026-07-28 against both variants; both fired
           correctly."
     WEAK  "Tracking already works for this." (no events named, no exposure event, no verification date)
     TRAP  Treating this section as a restatement of the PRD's instrumentation section. If nothing here is
           new or test-specific, say that in one line; if something is, name only what the test itself adds.
           -->

{{tracking_and_instrumentation_note}}

## Validity Pre-Commitments

<!-- WHAT  The checks and thresholds, fixed before the test runs, that decide whether its result will be
           trustworthy: a sample ratio mismatch threshold, an early-stop threshold for harm, a ramp-up plan
           where one applies, and how novelty effects and segments fixed in advance will be watched for. Plus
           two items that are not table rows: how this test handles overlap with concurrent experiments, and
           who else must be told the test is running and what its risks are.
     WHY   This section's name and grouping are this library's own synthesis: no single source names a
           section with exactly this scope, and it is built by combining several sources' individually
           sourced guidance rather than copying one template. Each check exists to catch a specific way a
           result can look real and not be: an uneven traffic split invalidates the comparison itself, an
           unmonitored guardrail breach does real harm before anyone notices, and an unflagged novelty effect
           gets read as a stable one. Whether overlap with concurrent experiments needs designing around is
           contested: two sources treat it as a design check, while two vendors report, from their own
           experience, that meaningful interaction effects between parallel tests are rare. This bundle does
           not adopt either position as settled; it only asks you to state how this test handles the
           question. Deep dive: experiment-design-doc_companion.md section 3 (Anatomy > Validity
           Pre-Commitments) and section 6, item 4.
     ASK   What sample-ratio check, run how often, would make you distrust the split itself? What guardrail
           breach, and detected how, stops the test early rather than waiting for the scheduled end? Does this test ramp up gradually, and if so, on what schedule; if not, why not?
           How will a novelty effect be checked for, and were any segments fixed before launch so their own
           composition cannot shift mid-test? Does this test run alongside another experiment on the same
           surface, and if so, how is that handled? Who outside this team needs to know the test is running
           and what its risks are?
     PRIORITY  List only the checks that genuinely apply to this test; a ramp-up row on a test too small to
           ramp is not a check, it is padding. Order by how much skipping the check would undermine trust in
           the result if it went unnoticed.
     ROW HINT  A good row names the check, the threshold or trigger that would act on it, and who owns
           watching for it. A weak row names a worry with no threshold and no owner.
     GOOD  | Sample ratio mismatch | Flag if the platform's chi-squared check on assigned subscriber counts
           reports a significant gap from the configured 50/50 on any daily read | Data analyst on the digest
           team |
           Overlap line: "The subject-line test on the same weekly digest ends on 14 March and this test
           starts on 17 March, so no subscriber receives a send from both."
           Risks line: "A later send time can raise unsubscribes, which the guardrail row above stops on.
           Support hears two days before launch; the lifecycle marketing lead owns that note."
     WEAK  | Watch for problems | | QA |
           Overlap line: "Other tests should not interfere." Risks line: "Stakeholders will be informed as
           needed." Neither names a test, a date, a person, or a consequence.
     TRAP  Listing every check from a generic list regardless of whether it applies to this test. A row with
           no threshold and no owner is not pre-committed, it is a reminder to worry; write "N/A" with one
           line of why instead. -->

| Check | Threshold or trigger | Owner |
|---|---|---|
| {{validity_check}} | {{validity_threshold_or_trigger}} | {{validity_owner}} |

**Overlap with concurrent experiments.** {{overlap_handling}}

**Risks, and who else must be told.** {{risks_and_notification}}
