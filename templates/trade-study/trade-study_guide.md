# Guide: Trade Study (operator card)

Fast reference for using the trade-study bundle. For the full reasoning, history, and sources, read
[`trade-study_companion.md`](trade-study_companion.md). A fully worked instance is
[`trade-study_example.md`](trade-study_example.md).

## When to use

- You already own the problem, and now have to choose among **named technical approaches** to solve
  it: a runner model, a message-ingestion technology, a persistence engine, an architecture pattern.
- **More than one approach is genuinely on the table**, and the choice is not obvious from where you
  stand today.
- The comparison needs to **survive a reader who was not in the room**: a reviewer, an auditor, or
  whoever revisits this decision in a year and wants to know what the road not taken would have cost.
- Reasonable people on the team would **weight the criteria differently**, and writing the weights
  down, with a reason for each, is cheaper than arguing from memory later.
- You are about to **feed an ADR, an RFC, or an SDD** a weighted comparison, rather than a paragraph
  of reasoning, for their own Alternatives Considered prose.

## When NOT to use

- **There was never a real second option.** Skip this document and write the decision straight into
  whatever record normally follows one (see [`adr`](../adr/adr_guide.md)); companion section 4 names the
  source that says to skip it.
- **You are deciding whether to invest in something at all, not how to solve a problem you already
  own.** No definition this bundle's research read frames a trade study as an investment decision; cost
  sits inside the comparison as one criterion among several, not as the question itself. That is a
  [business case](../business-case/business-case_guide.md)'s job, and it is this bundle's own boundary
  to draw, stated plainly rather than borrowed from a source (see companion section 1 and section 8).
- **The decision is already made and you want to justify it after the fact.** A trade study with the
  answer chosen before the criteria is the predetermined-winner failure named below. Write the ADR
  honestly instead, or rerun the comparison for real.
- **You want feedback on a proposal before anything is decided.** That is an
  [RFC](../rfc/rfc_guide.md)'s job: it asks for input before the call is made. This document evaluates
  named alternatives against stated criteria; it does not gather opinions on whether to proceed.
- **You are describing how a system will be built, not choosing among named approaches to building
  it.** That is an [SDD](../sdd/sdd_guide.md)'s job. An SDD's own Alternatives Considered section can
  cite a finished trade study instead of rebuilding the matrix in prose.
- **The alternatives cannot yet be named with confidence.** A
  [spike report](../spike-report/spike-report_guide.md) exists to resolve that uncertainty first. Run
  it before the Alternatives section below can be filled in honestly.

## Trade study, RFC, ADR, or SDD?

| | **Trade study** | **RFC** | **ADR** | **SDD** |
|---|---|---|---|---|
| Answers | "Which named option wins, and why?" | "Should we, and which way?" | "What did we decide, and why?" | "How will we build it?" |
| Timing | Before the decision, once alternatives can be named | Before the decision | After the decision | Before or while building |
| Produces | A scored comparison and a recommendation | A proposal | A record | A description |
| Records the decision itself | No, it points to the record that does | No | Yes, immutably | No |

These are a division of labor, not four names for one job. A trade study's Recommendation section may
name the decision taken in one line; the ADR is where that decision is recorded for good.

## Pick a variant

**Lean (five sections, the default):** Problem and Decision Framing, Criteria and Weights,
Alternatives, Scoring Matrix, Recommendation. Write lean when the stakes are contained and the
comparison is between a small set of options whose tradeoffs are already mostly understood. The
sources allow a short report as readily as a formal one (companion section 4).

**Full (nine sections):** adds Sensitivity Analysis, Risk and Benefit, Dissent or Independent Review,
and References. Reach for full when the decision is high-stakes or hard to reverse, the team disagrees about the criteria or their weights, or a reviewer outside the
immediate group will need to check the reasoning later.

Grow lean into full by adding sections; never reorder or rename the shared ones, because the full
variant is a strict superset of lean. The scaling signal is how hard the decision is to reverse and how
contested the criteria are, not the size of the system being decided about.

**One caution that applies to either variant.** If the do-nothing row in Alternatives is also doing the
job of a scoring reference point (a Pugh datum), say so explicitly, because a poor or biased reference
option can distort the entire comparison. A do-nothing baseline and a Pugh datum are not automatically the same
thing; using one as both is a choice the author makes, not a default the template assumes (companion
section 6.3).

## Quality rubric (self-grade before you ship it)

Score each 0, 1, or 2. Under 14 out of 20 and the recommendation should not be acted on without a
second look; send the document back for another pass before anyone treats it as settled.

**Rows 7 through 10 grade sections the lean variant does not ship:** Sensitivity Analysis, Risk and
Benefit, Dissent or Independent Review, and References. Grade lean against the scope table below the
main table instead of against all ten rows.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Question answered, not posed** | No question stated, or the title names a topic rather than a comparison | A question is stated, but no decision maker is named or the decision it feeds is unclear | A reader can point at the sentence naming the question, the decision it feeds, and who decides it |
| 2 | **Weights justified and typed** | Weights appear with no stated reason | Each weight has a reason, but the document never says whether a weight means importance or the swing between the best and worst option | Every weight carries a stated reason, and the document names which of the two meanings its weights use |
| 3 | **Do-nothing row scored** | No do-nothing or do-minimum row, and no line explaining its absence | A do-nothing row exists, but it is a label with no real cost or risk behind it | The do-nothing row is scored as a genuine alternative, or a specific reason for its absence is written in Alternatives |
| 4 | **Scores have a basis** | Scores are bare numbers | Some scores carry a basis, others do not | Every score in the matrix carries a basis a reader could dispute, and the weighted total can be recomputed from the rows shown |
| 5 | **Recommendation reasons from rows** | The recommendation restates the highest weighted total with no reasoning | The recommendation names which rows it depends on, but states no condition under which it would change | A reader can name the specific rows the recommendation depends on and the condition that would overturn it, and a genuine near-tie is reported as one rather than forced apart |
| 6 | **Record pointer given** | No decision is named, and no record is pointed to | A decision is named, but no record is pointed to, or the pointer is to this same document | The line names the decision taken and a specific record elsewhere that holds it, or states plainly that no decision has been taken yet |
| 7 | **Sensitivity tested** *(full)* | No weight or score was moved; confidence is asserted rather than tested | A weight or score was moved, but the result is not stated either way | A specific weight or score was moved by a stated amount, and the document says plainly whether the recommendation survives |
| 8 | **Every contender covered** *(full)* | Only the recommended option has a risk or a benefit written down | More than one option is covered, but the mitigation the leading option would need is missing | Every alternative still in contention has a risk, a benefit, and the leading option's mitigation is named |
| 9 | **Reviewer independence stated** *(full)* | The section is silent, or says only that the team reviewed its own work | A reviewer is named, but their stake in the outcome is not addressed | A named person or group checked the scoring, and the document states how independent of the outcome they are, or says plainly that no independent check happened |
| 10 | **References dated, checkable** *(full)* | Sources are named generically ("various documents") or not at all | Specific sources are named, but without a date | Each criterion's score traces to a named, dated source a reader could open and check |

**Score lean against this table instead of the headline threshold above.**

| Variant | Rows that apply | Maximum | Score against |
|---|---|---|---|
| full | all 10 | 20 | **14** |
| lean | 1-6 (it carries none of the four full-only sections) | 12 | **9** |

Every cell above describes evidence, not a count. A rubric cell that can be satisfied by adding items
will be satisfied by adding items, so none of them ask for a number of anything; each asks whether a
reader could point at the specific sentence that does the work.

## Named anti-patterns (the usual wrecks)

Each one is sourced in companion section 7.

1. **Criteria chosen after the alternatives, to fit the one already wanted.** The list quietly favors
   the option someone preferred before scoring began. Set the criteria and their weights before anyone
   scores an option.
2. **A criterion with no way to measure it.** A criterion only opinion can score gives a favored option
   somewhere to hide. Pick criteria that are transparent and measurable before scoring starts.
3. **A must-have outvoted by a pile of minor criteria.** Weighting does not stop scoring from
   equalizing requirements, so enough small criteria can add up to select an option that fails
   something the team actually needed. Mark a must-have mandatory instead of only weighting it.
4. **A recommendation that survives no real test, because nothing was moved.** If a minor change in
   one input changes the answer, the study is probably not sound, and a matrix with no sensitivity
   check has nothing to answer that criticism with.
5. **Scorers using the same scale differently, with no discussion to close the gap.** One scorer uses
   the full range and another clusters in the middle. Left unaddressed, two scorers are not comparing
   the same thing.
6. **Averaging away a disagreement instead of resolving it.** A quiet average, or a vote, hides exactly
   the disagreement a reader would want surfaced.
7. **A biased or unexamined datum, when the scoring method uses one.** A poor reference option can
   distort the entire comparison. Naming the datum and testing whether the ranking survives a
   different one is the fix.
8. **Treating the weighted total as the decision rather than a prompt for one.** The option with the
   highest score is not necessarily the one to choose. The total tells you where the discussion should
   focus, not what to conclude from it.
