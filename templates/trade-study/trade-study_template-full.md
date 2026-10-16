---
title: "{{title}}"
status: "{{status}}"
date: "{{date}}"
decision_makers: ["{{decision_makers}}"]
doc_type: trade-study
size: full
source_template: trade-study
source_template_version: 0.1.0
---

<!--
FULL TRADE STUDY. All nine sections this bundle defines: the lean five, plus the four this
variant adds, Sensitivity Analysis, Risk and Benefit, Dissent or Independent Review, and
References. Use this weight when the decision is hard to reverse, the field disagrees about the
criteria or their weights, or a reviewer outside the immediate team will need to check the
reasoning later. NASA allows "a simple white paper or a more formally formatted document",
leaving the choice to "the mission and system context and the decision made". AcqNotes ties the
heavier process to the stakes: "formal trade studies are indicated for high-value, high-risk, or
other high-impact decisions." See trade-study_companion.md section 4 (Variants and sizing).

Most comparisons do not earn this weight. The lean variant (trade-study_template-lean.md) is the
default, and Microsoft's own engineering playbook names the condition for skipping the exercise
entirely: "Trade studies should be avoided if there is a clear solution choice." The full variant
is a strict superset of lean: the shared sections keep their names and their order, and this file
only ADDS.

THIS IS NOT A BUSINESS CASE, AND THAT DRIFT IS THE EASIEST MISTAKE TO MAKE HERE.
A trade study compares named technical approaches to a problem the organization has already
decided to solve; cost sits inside the comparison as one criterion among several, not as the
question itself. No definition this bundle's research could read frames a trade study as the
decision whether to invest. If you are actually asking whether to invest in something at all,
rather than how best to solve a problem you already own, write a business case instead. See
trade-study_companion.md section 1 (Orientation) and section 8 (Relationships to other
artifacts).

THIS EVALUATES OPTIONS; IT DOES NOT RECORD THE DECISION.
This bundle's own division of labor hands the decision itself to an ADR, written once the
recommendation below is acted on. An RFC or an SDD whose own Alternatives Considered prose needs
a weighted comparison can cite this document instead of rebuilding the matrix in prose. A spike
report, if one came first, reduced the uncertainty that let these alternatives be named with
confidence in the first place. See trade-study_companion.md section 8 (Relationships to other
artifacts).

THE DO-NOTHING BASELINE IS THIS BUNDLE'S OWN REQUIREMENT, NOT A DOCUMENTED CONSENSUS.
NASA notes only that "(Sometimes doing nothing or not making a decision is an option.)" The FHWA
is just as conditional: "It is often good practice to include a" ... "alternative as the base
case, depending on the nature of the trade study." Several other named outlines mention no such
row at all. This bundle requires it anyway: adding
or dropping a do-nothing row can change which live option ranks first, because that is exactly
the mechanism a rank reversal describes. A comparison with no credible do-nothing option should
say so in one line in Alternatives, rather than silently drop the row. See
trade-study_companion.md section 3 (Anatomy > Alternatives, Including a Do-Nothing Baseline).

WHERE THIS FILE GOES: wherever your team keeps design and decision records. This bundle
prescribes no location. Once a decision is taken from this comparison, link this document from
the ADR that records it; do not fold the two together.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   trade-study_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid. For a table, PRIORITY explains the coverage rule and ROW HINT
   says what a good row contains.
2. Replace each {{placeholder}} with your content. If a section does not apply, write "N/A" and
   one line of why, rather than deleting it.
3. Before you ship it: self-grade against trade-study_guide.md, then DELETE every HTML comment.
   They are guidance, not content.
-->

# {{title}}

<!-- WHAT  A title naming both the problem this study is solving and, once you know it, the option it
           recommends. A statement, not a topic.
     WHY   A comparison filed under a topic name alone, such as CI runner options, tells a later reader
           nothing about what was decided; a title naming the recommendation lets them judge in one line
           whether to open the rest.
           Deep dive: trade-study_companion.md section 3 (Anatomy > Problem and Decision Framing).
     ASK   What problem does this comparison solve? Once you have an answer below, does the title still
           read true, or does it only describe the question?
     GOOD  "CI runner model for the platform team: recommend self-hosted over the hosted service"
     WEAK  "CI options" (a topic, not a comparison; nobody can tell what was found)
     TRAP  Titling the technology area instead of the comparison. A title can be written before you start
           and revised once you finish; revise it, rather than shipping the question as if it were the
           answer. -->

## Problem and Decision Framing

<!-- WHAT  The question this study answers, the decision it feeds and who decides it, and the
           constraints and assumptions every alternative below must respect.
     WHY   The FHWA puts this first for a reason: "First, define the question the trade study is to
           answer." Everything below is only as good as the question it is answering, and drift here is
           where the predetermined-winner failure gets its opening, when criteria get written to fit an
           answer already chosen rather than the other way around.
           Deep dive: trade-study_companion.md section 3 (Anatomy > Problem and Decision Framing), section
           6.7 (The predetermined-winner critique).
     ASK   What question is this study actually answering? What decision does the answer feed, and who
           makes that decision? What constraint or assumption must every alternative respect, whether or
           not anyone ever says it out loud?
     GOOD  "Question: should the platform team keep the current shared CI runner pool, or move to a
           different model, before the fourth product team onboards next quarter. Decision this feeds:
           which runner model to standardize on for the next two years. Decided by: the platform lead,
           with sign-off from the three onboarding teams' leads. Constraints: must support the existing
           container build images without a rewrite; budget ceiling of 4,000 dollars a month."
     WEAK  "We need a CI solution." (no question evidence could answer, no named decision maker, no
           constraint)
     TRAP  Writing this section after the alternatives are already chosen, to justify them. A question and
           a decision maker written down before the comparison starts is what keeps the criteria in the
           next section from being reverse-engineered to fit an answer you already picked. -->

* Question this study answers: {{the_question}}
* Decision this feeds, and who decides: {{decision_and_decision_makers}}
* Constraints and assumptions every alternative must respect: {{constraints_and_assumptions}}

## Criteria and Weights

<!-- WHAT  Each criterion this study will score alternatives against, its weight, why it was chosen and
           weighted that way, whether it is mandatory, and the scoring method and scale in use.
     WHY   The FHWA's sequencing exists on purpose: criteria are set "before the alternatives are
           selected, to avoid subconsciously biasing the criteria to favor a pre-determined preferred
           alternative." ECSS requires the weighting itself to be justified, not merely stated. A weight
           also carries one of two different meanings, importance or how much the best and worst
           alternative actually differ (a swing weight), and this template asks you to say which one you
           mean rather than picking one for you.
           Deep dive: trade-study_companion.md section 3 (Anatomy > Criteria and Weights), section 6.2 (A
           separate must-have screen, or one weighted pass), section 6.4 (One weight, two meanings).
     ASK   What criteria actually matter here, and why these and not others? Is each weight measuring
           importance, or the swing between the best and worst alternative on that criterion, and have you
           said which? Is any criterion mandatory, meaning an alternative that fails it is dropped
           outright rather than merely docked points?
     PRIORITY  Set every criterion and its weight before you look hard at the alternatives in the next
           section, to avoid biasing the criteria toward an answer you have already chosen. Mark a
           criterion mandatory only when failing it should drop the alternative outright, not merely cost
           it points.
     ROW HINT  A good row states the weight and the reason for that number, not the number alone.
           "Reliability, weight 30" with no reason cannot be checked six months later; "weight 30, because
           an outage here is customer-visible within minutes" can.
     GOOD  | C1 | Queue wait at peak load | 30 | No | Weighted this high because the fourth team's
           onboarding is what forces this decision, and the shared pool already hits its job cap at peak |
     WEAK  | C1 | Good support | High | | Because it matters |
     TRAP  Picking the criteria after seeing how each alternative would score, so the list quietly favors
           the one you already wanted. If a criterion only occurred to you after looking at the options,
           say so and weigh honestly whether it belongs. -->

Scoring method and scale in use: {{scoring_method_and_scale}}
What a weight means here (importance, or the swing between the best and worst alternative on that
criterion): {{weight_meaning}}

| ID | Criterion | Weight | Mandatory? | Justification |
|---|---|---|---|---|
| {{criterion_id}} | {{criterion_name}} | {{weight}} | {{mandatory_yes_no}} | {{criterion_justification}} |

## Alternatives, Including a Do-Nothing Baseline

<!-- WHAT  Every alternative actually considered, including a do-nothing or do-minimum baseline, and, if a
           larger field was narrowed first, how.
     WHY   The FHWA's own advice: "Be sure that all reasonable alternatives are on the table." NASA's trade
           tree is the named tool for narrowing a large field before detailed analysis begins. The
           do-nothing row is this bundle's own requirement, not a documented consensus; see the note at the
           top of this file and the reasoning behind it.
           Deep dive: trade-study_companion.md section 3 (Anatomy > Alternatives, Including a Do-Nothing
           Baseline), section 6.3 (The Pugh datum and the do-nothing baseline are not the same thing).
     ASK   What alternatives were genuinely on the table, not just the one you expect to win? If the field
           started larger, how was it narrowed, and on what basis? What would doing nothing, or the
           minimum, actually look like here, and what would it cost?
     PRIORITY  Every comparison needs a do-nothing or do-minimum row, even when it is rejected in one line.
           If a comparison genuinely has no credible do-nothing option, write one line here saying why
           rather than silently dropping the row.
     ROW HINT  A good row names a real alternative a reasonable team could actually choose, with what it
           would concretely involve. A weak row is a label with nothing behind it, or a straw alternative
           built to lose.
     GOOD  | A1 | Keep the current shared runner pool (do-nothing) | No new cost, but queue time grows
           once the fourth team onboards | Yes |
     WEAK  | A3 | The obvious choice | | No |
     TRAP  Treating this table's do-nothing row as the same thing as a scoring reference point (a Pugh
           datum), if you are also using one. A datum is what every score is measured against; a
           do-nothing row is a candidate being scored in its own right. Say explicitly if the same
           alternative is doing both jobs. -->

How the field was narrowed to the alternatives below (or "N/A, nothing was narrowed"):
{{how_the_field_was_narrowed}}

| ID | Alternative | Description | Do-nothing or do-minimum baseline? |
|---|---|---|---|
| {{alternative_id}} | {{alternative_name}} | {{alternative_description}} | {{is_do_nothing_baseline}} |

## Scoring Matrix

<!-- WHAT  The completed comparison: each criterion against each alternative, a weighted total per
           alternative, and the basis for each individual score, laid out so a reader outside this team
           could still follow it.
     WHY   The FHWA's orientation is this template's default, alternatives on one axis, criteria on the
           other, with a readability requirement stated directly: the matrix "should be easily
           comprehensible to management and other stakeholders". ASQ gives the arithmetic and the caution
           in one breath: the highest score "will not necessarily be the one to choose, but the relative
           scores can generate meaningful discussion".
           Deep dive: trade-study_companion.md section 3 (Anatomy > Scoring Matrix), section 6.1 (Is
           weighted scoring reliable, or only as reliable as its inputs).
     ASK   What is the basis for each score, in one phrase a reader could check or dispute? Does each
           weighted total actually equal score times weight, summed across criteria? If two scorers
           disagreed on a cell, did you discuss it to a real answer, or quietly average the disagreement
           away?
     PRIORITY  Every criterion from Criteria and Weights gets exactly one row here; every alternative from
           the table above gets its own column. Add a column for each further alternative and a row for
           each further criterion.
     ROW HINT  A good row scores every alternative against one named criterion and gives the basis for
           each score beside the number. A row of bare numbers with no basis cannot be checked, disputed,
           or trusted later.
     GOOD  "Queue wait at peak load, weight 30: self-hosted runners score 8, because the team can add
           machines as the fourth team's builds arrive; the hosted service scores 4, because its plan caps
           concurrent jobs at the level the shared pool already reaches at peak."
     WEAK  "Queue wait: 8 / 4." (numbers with no basis; nothing here can be checked or disputed)
     TRAP  Treating the highest weighted total as the decision rather than a prompt for one. The total
           tells you where the discussion should focus, not what to conclude from it; write Recommendation
           as reasoning from specific rows below, not as a restatement of this total. -->

| Criterion | Weight | {{alternative_1_name}} | {{alternative_2_name}} |
|---|---|---|---|
| {{criterion_name}} | {{weight}} | {{score}} ({{basis}}) | {{score}} ({{basis}}) |
| **Weighted total** |  | {{weighted_total_1}} | {{weighted_total_2}} |

## Sensitivity Analysis

<!-- WHAT  The one or two weights or scores you are least sure of, moved to see whether the recommendation
           survives, and the honest answer either way.
     WHY   DSMC states the stakes directly: "If the solution can be changed with relatively minor changes
           in data input, the study is probably invalid". This is also the section's honest answer to the
           false-precision critique of the whole method; a matrix with no sensitivity check invites that
           critique and has no defense against it.
           Deep dive: trade-study_companion.md section 3 (Anatomy > Sensitivity Analysis), section 6.1 (Is
           weighted scoring reliable, or only as reliable as its inputs).
     ASK   Which weight or score are you least confident in? How far would it have to move before a
           different alternative wins? Does the recommendation survive that move? If it does not, what
           does that imply about how confidently you can recommend anything?
     GOOD  "Moved the queue-wait weight from 30 to 22 of the total 100 points, the number the team
           disagreed about most. The self-hosted runner still ranks first, by under a point. At 20 the two
           tie, and moving it to 15 flips the result to the hosted service. The recommendation holds for
           any queue-wait weight above 20."
     WEAK  "We're fairly confident in our weights." (no variable named, nothing moved, nothing a reader can
           check)
     TRAP  Running this check after the recommendation is already written, to defend it rather than test
           it. If nothing you tried could have changed the outcome, say exactly which values you moved and
           by how much, so a reader can see that for themselves rather than take your word for it. -->

* Weight or score tested: {{sensitivity_variable}}
* How far it would have to move before the recommendation changes: {{sensitivity_threshold}}
* Does the recommendation survive this test: {{recommendation_survives}}

## Risk and Benefit

<!-- WHAT  The risks and benefits of every alternative still in contention, not only the one Scoring
           Matrix favors, plus the mitigation the leading alternative would need.
     WHY   NASA's own decision report gives this content a row covering every option still under
           consideration. This bundle follows that wider scope rather than ECSS's narrower one, which
           scopes the same content to the recommended solution alone, because a reader comparing two close
           alternatives wants to see what each one would have cost, not only what the winner costs. That
           is this bundle's own choice between two sourced positions.
           Deep dive: trade-study_companion.md section 3 (Anatomy > Risk and Benefit).
     ASK   What could go wrong with this alternative, and what would it cost if it did? What does this
           alternative buy that the others do not? For the alternative you expect to recommend, what would
           it take to live with its risk?
     PRIORITY  Cover every alternative still in contention, not only the one Scoring Matrix favors. A
           reader comparing two close alternatives wants to know what each would have cost, not only what
           the winner costs.
     ROW HINT  A good row names a risk or benefit specific to that alternative, with what it would take to
           live with it. "Could fail" or "has upside" said about every row equally is not a row, it is a
           shrug.
     GOOD  | Self-hosted runners | Risk: a single maintainer leaving leaves nobody who knows the setup |
           Benefit: no per-minute vendor billing | Mitigation if recommended: document the setup and
           cross-train a second engineer before go-live |
     WEAK  | Self-hosted runners | Risk: things could break | Benefit: it's ours | |
     TRAP  Writing this section only for the alternative you are about to recommend. The risk and benefit
           of the road not taken is exactly what a reader revisiting this decision later will want to
           know. -->

| Alternative | Risk | Benefit | Mitigation (if this becomes the recommendation) |
|---|---|---|---|
| {{alternative_name}} | {{risk}} | {{benefit}} | {{mitigation_if_recommended}} |

## Recommendation

<!-- WHAT  The option the matrix supports, the rows it depends on, the conditions under which it holds, a
           genuine near-tie reported as one outcome rather than forced apart, and the decision actually
           taken, in one line, with a pointer to the record that holds it for good.
     WHY   The FHWA's own instruction is plain: "Select and document the preferred candidate". ECSS
           requires both the choice and its conditions. NASA and Microsoft both allow a genuine near-tie,
           or a list of open questions, rather than forcing a false precision onto a comparison that cannot
           support it. This bundle's own division of labor stops the recommendation short of the permanent
           record, which belongs to an ADR.
           Deep dive: trade-study_companion.md section 3 (Anatomy > Recommendation), section 6.5 (One
           recommended option, or every closely ranked one), section 8 (Relationships to other artifacts).
     ASK   Which option does the comparison actually support? Which specific rows does that depend on?
           Under what condition would this recommendation no longer hold? If two options are genuinely
           close, say that plainly, rather than reporting a winner the matrix cannot support. What decision
           was actually taken, and where is it recorded?
     GOOD  "Recommended: the self-hosted runner, ahead by 4 points on the current weights, conditional on
           the queue-wait weight staying above 20 (see Sensitivity Analysis). Re-run this
           comparison if the hosted plan raises its concurrent-job cap; queue wait was the deciding
           criterion. Decision taken: adopt the self-hosted runner, recorded in ADR 0091."
     WEAK  "We recommend the self-hosted option because it scored highest." (restates the matrix total,
           names no condition, points to no record)
     TRAP  Forcing a clean winner out of a genuine near-tie. If two alternatives are within noise of each
           other on the weights you actually trust, say that plainly and name what would separate them,
           rather than dressing up a coin flip as a confident recommendation. -->

* Recommended alternative, or alternatives if genuinely close: {{recommended_option}}
* Rows this depends on: {{dependent_rows}}
* Conditions under which this holds: {{conditions}}
* Decision taken, and where it is recorded for good: {{decision_and_record_pointer}}

## Dissent or Independent Review

<!-- WHAT  Who disagreed with the recommendation and how that was addressed, or who checked the scoring
           and how independent of the outcome they were.
     WHY   SEBoK sets the strongest named standard: independent review "should come from an outside body"
           that "must be both organizationally and financially independent of the program in question."
           The FHWA's own review checklist asks the question directly: "Have key stakeholders reviewed and
           support the trade study results?"
           Deep dive: trade-study_companion.md section 3 (Anatomy > Dissent or Independent Review).
     ASK   Did anyone on the team, or reviewing it, disagree with the recommendation? How was that
           disagreement addressed, not just noted? Who checked the scoring, and what is their stake in the
           outcome?
     GOOD  "The engineer who favored the hosted service reviewed the final matrix
           and disputed its reliability score, not the weights; the team re-scored that row from the
           internal incident log, the recommendation held, and she accepted it. No
           reviewer outside the team checked the scoring independently."
     WEAK  "The team reviewed its own work and is confident in the result." (answers a different question
           than whether anyone independent of the outcome checked it)
     TRAP  Treating silence as agreement. A team that never surfaced a disagreement either genuinely had
           none, worth stating plainly, or suppressed one, which this section exists to catch either way. -->

* Who disagreed, and how it was addressed: {{dissent_and_resolution}}
* Who checked the scoring, and how independent of the outcome they are: {{reviewer_independence}}

## References

<!-- WHAT  The data, models, and documents the criteria, weights, and scores in this study actually rest
           on.
     WHY   NASA's own report lists "all data sources used" among a trade study report's required content,
           and its decision report carries a dedicated row for it. ECSS's Annex L opens with applicable
           and reference documents as its second clause.
           Deep dive: trade-study_companion.md section 3 (Anatomy > References).
     ASK   What document, benchmark, vendor page, or prior study did a specific score or weight actually
           come from? Is each one dated, since most of what a trade study cites changes with the product
           or the market it describes?
     GOOD  "[1] Vendor X runner pricing page, read 2026-09-30, source for the job cap and the cost row. [2] Internal
           incident log, Q2 to Q3 2026, source for the reliability scores on both options."
     WEAK  "Various internal documents and vendor sites." (names nothing a reader could open and check)
     TRAP  Citing a product's current documentation as a timeless fact about the technology rather than a
           snapshot dated the day it was read. Date every technical fact a criterion's score actually rests
           on. -->

* {{reference_1}}
* {{reference_2}}
