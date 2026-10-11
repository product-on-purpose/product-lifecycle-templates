---
title: "{{experiment_name}} Experiment Readout"
experiment_name: "{{experiment_name}}"
design_doc: "{{design_doc_link}}"
author: "{{author}}"
decision_maker: "{{decision_maker}}"
start_date: "{{start_date}}"
end_date: "{{end_date}}"
decision: "{{decision}}"
readout_date: "{{readout_date}}"
doc_type: experiment-readout
size: lean
source_template: experiment-readout
source_template_version: 0.1.0
---

<!--
LEAN EXPERIMENT READOUT. The eight sections a concluded test must report: the decision stated up front,
what ran, the primary and supporting results with their uncertainty, whether the result can be trusted,
the decision the pre-committed rule actually produced, who owns that call, and what happens next. Use it
for a test whose decision rests on its primary metric alone. To grow it into the full variant (see
experiment-readout_template-full.md), ADD sections; never rename or reorder the ones below, because the
full variant is a strict superset of this one.

WHAT AN EXPERIMENT READOUT IS, AND IS NOT
It is written after a test ends, reporting what ran, the results with their uncertainty, whether those
results can be trusted, and the decision they drove, with its owner. It is NOT the experiment design doc
restated: that document fixed the hypothesis, the variants, the metrics and the decision rule before the
test ran, and this document reports against that exact plan rather than repeating it. It is NOT a
test-summary-report: that qa-docs document verifies a product increment against an agreed specification
and grades it pass or fail, with no hypothesis, no allocation between variants, and no statistical
decision rule, while this document estimates an effect against a baseline. It is NOT a spike report:
a spike reduces uncertainty about a technical question and carries no control group or statistical
decision rule. It is NOT a live experiment scorecard or a one-time metrics export: those are tool-native
surfaces for monitoring and raw data, not a decision-bearing document, and neither replaces this one or
sits beside it as a substitute. See experiment-readout_companion.md section 8.

NO SOURCE MEASURED WHETHER WRITING ONE IMPROVES DECISIONS
The case for this document rests on the failure modes the sources name (peeking, cherry-picking, a loss
reported as a win) and on keeping a record a later reader can audit, not on a controlled comparison of
documented against undocumented tests. See experiment-readout_companion.md section 1.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   experiment-readout_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to
   avoid. For table sections, PRIORITY explains the ordering rule and ROW HINT says what a good row
   contains.
2. The experiment's name, a link to its design doc, the author, the decision-maker, the test's start and
   end dates, the decision, and the readout date live in the frontmatter above, not in a body section. Fill
   the design doc link first: every section below reports against that exact plan.
3. Report the same hypothesis, metrics and decision rule the design doc fixed, applied to what actually
   happened. If anything ran differently from the plan, say so in Context and Setup rather than quietly
   reporting as if the plan and the run were identical.
4. If a section, or a row in a table, does not apply, write "N/A" and one line of why, rather than deleting
   it silently. A reader cannot tell a deleted section from one nobody considered.
5. Before you share it: self-grade against experiment-readout_guide.md, then DELETE every HTML comment.
   They are guidance, not content.
-->

# {{experiment_name}} Experiment Readout

## Executive Summary

<!-- WHAT  The decision itself, stated up front, not buried under the evidence that supports it.
     WHY   Every section-order source names this section first, under three different titles: Eppo's
           "Executive Summary", Tanmayi Sai's "TL;DR", and Optimizely's "Purpose". A separate account of one
           team's own practice found that leading with what was learned, rather than a win or loss label,
           was what readers actually remembered. Deep dive: experiment-readout_companion.md section 3
           (Anatomy > Executive Summary).
     ASK   What is the decision, in one line? What is the single sentence a reader who stops here needs to
           walk away with? Does the summary lead with the finding, or does it make a reader hunt through the
           results sections below to find out what was decided?
     GOOD  "Decision: stop. The one-click reorder button did not raise the 7-day reorder rate past what
           control already does; the result is a null, not a win or a loss, and the finding is that
           returning customers already use the existing reorder flow when they want one."
     WEAK  "The test ran for three weeks and here is what we found." (no decision stated, forces the reader
           to hunt for it below)
     TRAP  Treating the summary as a teaser for the sections below rather than the decision itself. A reader
           who reads only this paragraph should still know what was decided. -->

{{executive_summary}}

## Context and Setup

<!-- WHAT  What ran: the variants, the dates, and the population, with a link to the design doc rather than
           a restatement of it, plus one line on anything that ran differently from the plan.
     WHY   Sourced to Tanmayi Sai's "Experiment Setup" and Optimizely's "Details" field (number of
           variations, the dates the test ran, and the visitor counts by variation). The deviations line is
           new in this bundle's own research and is borrowed from the clinical trial-reporting lineage, not
           from product practice: it traces to CONSORT's own 2010 addition of an item for identifying "any
           changes to the primary and secondary outcome (endpoint) measures after the trial started," and is
           corroborated by Booking.com's pre-registration discipline, which fixes the metrics a hypothesis is
           tested against before the test begins. Deep dive: experiment-readout_companion.md section 3
           (Anatomy > Context and Setup).
     ASK   What variants ran, over what dates, against what population, as the design doc specified? Does
           this match the design doc exactly, or did anything change, such as the traffic split, the dates,
           or who was eligible, after the test launched? What is the one-line answer on what ran differently
           from the plan, if anything?
     GOOD  "Ran 2026-09-01 through 2026-09-21, control and treatment at the planned 50/50 split, on the
           order-history page for all logged-in customers with at least one prior order, as the design doc
           specified. Deviations from the design doc: none; the test ran the full 21 days with no early
           stop."
     WEAK  "We ran the test for about three weeks." (no dates, no population, no statement on deviations)
     TRAP  Restating the design doc's hypothesis and metric baselines in full here. Link to it instead; this
           section's job is what actually ran, not what was planned. -->

{{context_and_setup}}

**What ran differently from the design doc.** {{deviations_from_design_doc}}

## Key Results: Primary Metrics

<!-- WHAT  The primary metric's movement against its baseline, stated with its uncertainty.
     WHY   The column shape is read verbatim from Eppo's own export: "Metric Control Test Change (abs)
           Change (rel) CI Sig?". Optimizely's narrative version asks for the same content in prose. The
           two change columns, absolute and relative, are corroborated from the clinical trial-reporting
           lineage, labeled here rather than presented as product practice: CONSORT's 2010 revision
           recommends that "for binary outcomes, presentation of both relative and absolute effect sizes is
           recommended." The interval's confidence level is stated in the row, never assumed as a field
           default; no source read states one level as a convention. Deep dive:
           experiment-readout_companion.md section 3 (Anatomy > Key Results: Primary Metrics) and section 6,
           item 8.
     ASK   What is the primary metric's control value and test value? What is the absolute change, and the
           relative change? What is the confidence interval, and at what confidence level (state the level
           in the row)? Is the change significant at that level?
     PRIORITY  List the primary metric row or rows first; the design doc capped these at one or two, and
           this table should not grow past what the design doc actually named as primary.
     ROW HINT  A good row names the metric, both values, both change columns, an interval with its stated
           confidence level, and a significance call. A weak row reports a change with no interval, so a
           reader cannot tell it from noise.
     GOOD  | 7-day reorder rate | 11.0% | 11.3% | +0.3 pts | +2.7% | -0.6 to +1.2 pts (95% CI) | No |
     WEAK  | Reorder rate | up slightly | | | | | |
     TRAP  Reporting the relative change alone. A small relative lift on a tiny base can read as dramatic;
           report both, per the clinical-lineage recommendation this bundle borrows for binary outcomes. -->

| Metric | Control | Test | Change (abs) | Change (rel) | CI | Sig? |
|---|---|---|---|---|---|---|
| {{metric_name}} | {{metric_control}} | {{metric_test}} | {{metric_change_abs}} | {{metric_change_rel}} | {{metric_ci}} | {{metric_significant}} |

## Key Results: Supporting Metrics

<!-- WHAT  Every guardrail's movement, reported against the threshold the design doc fixed.
     WHY   This is Eppo's own second results section. A guardrail metric is one that measures what a team
           does not want to degrade but does not expect to improve; a separate vendor's in-tool surface draws
           the same line between decision-making metrics and guardrail metrics. Each row here is read
           against the number the design doc pre-committed, not re-derived at readout time: that
           pre-commitment is what makes a breach legible rather than a judgment call made after the fact.
           Deep dive: experiment-readout_companion.md section 3 (Anatomy > Key Results: Supporting Metrics).
     ASK   What is each guardrail's movement, control against test? What threshold did the design doc set
           for a breach? Did any guardrail breach its threshold, and if so, when?
     PRIORITY  List every guardrail the design doc named, even one that held with no interesting movement; a
           guardrail silently dropped from the readout cannot be checked by a reader.
     ROW HINT  A good row names the guardrail, the design doc's own threshold, both values, and a held or
           breached call. A weak row reports a number with no threshold to compare it to.
     GOOD  | Checkout error rate | Design doc: no increase past 0.4% | 0.31% | 0.33% | Held |
     WEAK  | Checkout errors | about the same | | |
     TRAP  Re-deriving a new threshold here instead of using the one the design doc pre-committed. A
           threshold decided after seeing the data is not a guardrail, it is a rationalization. -->

| Guardrail | Design-doc threshold | Control | Test | Status |
|---|---|---|---|---|
| {{guardrail_name}} | {{guardrail_threshold}} | {{guardrail_control}} | {{guardrail_test}} | {{guardrail_status}} |

## Validity Checks

<!-- WHAT  Whether the result can be trusted at all, checked before it is read as a finding: a sample ratio
           mismatch, a mismatch in a metric's own observation units, a novelty effect read by date, an early
           look before the test finished, a telemetry change mid-test, and interaction with another live
           experiment on the same surface.
     WHY   This section's name and scope are this library's own POSITION: no single source names one section
           with exactly this job, and it is built by combining several individually sourced checks, the same
           way the design doc's own Validity Pre-Commitments section was built. Each check reports against
           the design doc's pre-commitment where one exists: an uneven traffic split invalidates the
           comparison itself; a decline in the lift across date segments is a named indicator of a novelty
           effect; reading results before the pre-committed duration ends inflates the reported
           significance level; and two sources note that interaction with another concurrently running
           experiment is worth designing around even though vendors report it is rare in practice. Deep
           dive: experiment-readout_companion.md section 3 (Anatomy > Validity Checks).
     ASK   Did the sample ratio match the configured split on every scheduled check? Did any metric's own
           observation unit shift mid-test? Did the lift decay across date segments, which would flag a
           novelty effect? Was the result read or acted on before the pre-committed duration ended? Did any
           telemetry change mid-test? Did this test overlap with another live experiment on the same
           surface, and if so, how was that handled?
     PRIORITY  Report every check the design doc pre-committed to running, ordered so a check whose failure
           would most undermine trust in the result comes first. A check the design doc did not pre-commit
           to is reported as "not pre-committed," not invented after the fact.
     ROW HINT  A good row names the check, states the result plainly (passed, flagged, not applicable), and
           if flagged, what it changes about how the result should be read. A weak row says "looks fine"
           with no specific check named.
     GOOD  | Sample ratio mismatch | Passed on every daily read | Configured 50/50; the largest daily gap
           stayed within the design doc's own chi-squared threshold |
     WEAK  | Validity | Looks OK | No major issues noticed |
     TRAP  Treating a passed sample-ratio check as proof the whole result is trustworthy. Each row here
           catches a different failure mode; a result needs all of them checked, not just the one that is
           easiest to run. -->

| Check | Result | Notes |
|---|---|---|
| {{validity_check_name}} | {{validity_check_result}} | {{validity_check_notes}} |

## Decision: Ship, Iterate or Stop

<!-- WHAT  The outcome the pre-committed decision rule actually produced, including what a null result does
           and does not rule out, and whether the decision is reversible.
     WHY   "Ship, iterate or stop" is this family's own wording for the three-way choice, stated as the
           contract's own POSITION, not a phrase any source read here uses verbatim. The nearest conventions
           in the sources are a pre-committed "ship/no-ship decision," "Win Lose Flat" outcomes, "roll out to
           more users, end, iterate, etc.," and "inconclusive" or "hypothesis proved." New in this bundle's
           own research: a null result states what it rules out and what it does not. One source's own
           framework counts an adequately powered null as a result in its own right rather than a
           non-result, with its own default action of iterating, abandoning, or shipping if the change is
           infrastructure-only; a separate account states the same principle from the opposite direction,
           that a decision not to ship is still a finding. An ASK on the decision's reversibility is traced
           to a source outside the experimentation canon entirely: most decisions are changeable and
           reversible, and only a smaller set deserve the slower process a one-way door warrants. Deep dive:
           experiment-readout_companion.md section 3 (Anatomy > Decision) and section 6, items 2 and 8.
     ASK   Which of ship, iterate or stop does the design doc's pre-committed decision rule actually produce
           for this result? If the result is a null, what effect size does it rule out, and what smaller
           effect does it not rule out (the interval's width, not the point estimate, answers this)? Is this
           decision reversible, and does that change how fast it needs to be made?
     GOOD  "Null. The design doc's decision rule for a null result is to iterate on a different mechanism
           rather than re-run this exact test unchanged. This result rules out a lift of 1.2 points or more
           at 95% confidence; it does not rule out a smaller lift the test was not powered to detect. The
           decision is reversible: the button can be removed with no migration cost, so this is a two-way
           door."
     WEAK  "It didn't really work so we're not shipping it." (no named outcome category, no statement of
           what the null rules out, no reversibility note)
     TRAP  Treating a null result as proof the change has no effect. A null on a test powered to detect a
           1.2-point lift says nothing about a 0.3-point one; state the interval's width, not just its
           center. -->

{{decision_narrative}}

**What this result rules out, and what it does not.** {{null_result_scope}}

**Reversibility.** {{decision_reversibility}}

## Decision Owner

<!-- WHAT  Who is named as having made the call, written as a field rather than a signature buried in prose.
     WHY   This section is this library's own POSITION, and it is unsourced: no source read names a field
           for the decision owner. The nearest is Optimizely's "Decision maker," which names a role among the
           people involved in a test, not a field this document itself carries. This section exists so that
           whoever that person turns out to be, their name is written down rather than implied. Deep dive:
           experiment-readout_companion.md section 3 (Anatomy > Decision Owner) and section 6, item 3.
     ASK   Who made this call? Is it the same person the design doc named as decision-maker in its own
           frontmatter? If not, who, and in what forum was the call made?
     GOOD  "Jordan Alvarez (PM, Checkout), the decision-maker named in the design doc's frontmatter, made
           this call at the 2026-09-22 experiment review."
     WEAK  "The team decided to stop." (no named person, no venue, cannot be traced back to the
           pre-committed decision-maker)
     TRAP  Leaving this section's named person different from the frontmatter's decision-maker field with no
           note of why. If the decision-maker changed, say so; if not, confirm the match rather than letting
           the two fields silently disagree. -->

{{decision_owner_statement}}

## Next Steps and Owners

<!-- WHAT  The concrete actions the decision requires, each with a named owner.
     WHY   Eppo's own filled example assigns an owner to its very first next step. A separate practitioner
           frames the same section more broadly, as the plan for the project going forward, which is why this
           section carries not only the immediate action the decision requires but anything else it implies,
           each with its own owner. Deep dive: experiment-readout_companion.md section 3 (Anatomy > Next
           Steps and Owners).
     ASK   What does the decision itself require (a rollout, a rollback, a retirement of a tracking field)?
           What does it imply beyond that immediate action? Who, by name, owns each one?
     PRIORITY  List the action the decision itself requires first, then anything downstream of it.
     ROW HINT  A good row names a concrete action, one owner, and a status. A weak row names a hope with no
           owner.
     GOOD  | Remove the reorder-button flag and the control path from the codebase | Sam Ruiz (Eng) | Not
           started |
     WEAK  | Think about next steps | | |
     TRAP  Naming "the team" as the owner. One name per row, the same discipline the Decision Owner section
           above asks for. -->

| Action | Owner | Status |
|---|---|---|
| {{next_step_action}} | {{next_step_owner}} | {{next_step_status}} |
