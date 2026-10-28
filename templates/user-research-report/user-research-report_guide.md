# User Research Report: the guide

This document records what one study of the people a product serves found, and what it recommends,
after the study ends. It is not the **user research plan**, the sibling bundle that sets the same
study's questions before the sessions run; this report answers them after. The deep explainer behind
every rule here is [`user-research-report_companion.md`](user-research-report_companion.md); a fully
worked instance is [`user-research-report_example.md`](user-research-report_example.md).

## Before you start: is this the right document at all?

Write a user research report once a study has run and you need to tell stakeholders what it found,
what to do about it, and whether it answered the questions the plan set out to ask. Dovetail separates
the report from its parts: "A report packages several insights into a narrative for a specific
audience, with method, context, and recommendations." User Interviews names the same shape: "A
research report is a document that summarizes all the details of a research study, including the
research questions, methodology, notable insights, and recommended next steps."

**Write something else if:**

| You actually need | Because |
|---|---|
| a **user research plan** | the not-yet-run sibling to this bundle; it sets out the same study's questions before the sessions happen, and this report answers them after |
| a **debrief** | Dovetail's own line draws the boundary: "A debrief is not a research report for peer review." A debrief is a lighter, often async record a team can lean on quickly; it does not replace this document, though "the async debrief still serves as the foundation" for it |
| a **test-summary-report** (the QA pair's own report, `qa-docs`) | that document verifies a product increment against an agreed specification and grades it; this report studies how people use a product and records observations, not a verdict against a spec |
| an **experiment readout** (`experimentation-docs`) | Gilad draws the line this library relies on: "Per this definition an A/B test is an experiment, but a usability test is not." A usability study assigns no participant to a variant and applies no decision rule against a baseline |
| a **persona, a problem statement, or a design brief** (`discovery-docs`) | this family's own contract states the boundary directly: "The persona, the problem statement and the design brief take the findings and frame or decide." This report may recommend; it frames no problem and chooses no concept |
| a **Voice of Customer report, or any standing research repository** | those aggregate findings across many studies, ongoing; this report is written for, and finishes with, the one study it reports |

**Avoid the bare phrase "test report" or "test results" for this document.** The words collide with
`test-summary-report`, a separate bundle in this library's QA family. Name this one fully, as a
usability study report or a user research report.

**Who writes it.** No source read for this bundle gives one role a majority. GitLab names the role, not
the credential: "In GitLab, anyone can be the DRI of a UX Research project. If the Research DRI is not
a UX Researcher, they are partnered with a UX Researcher acting in a supporting role." User Interviews
assumes the researcher who ran the study writes it up. This library lets either a researcher or a
product person write this report, without claiming either one usually does.

**A report with no written plan behind it still fills Research Questions and Answers.** The sources
tie a report to a plan only where one exists; if no plan was written, fill that section from what the
study actually set out to learn.

## Picking a variant

**Lean** carries the six sections every size ships, in this order: Summary, Research Questions and
Answers, What We Did, Key Findings, Task Results, and Recommendations. **Full** adds three, in this
order: Background and Objectives (after Summary), Open Questions (after Recommendations), and Appendix
(after Open Questions).

Use full when at least one of these is true: the decision these findings inform needs restating with
its own context for a reader who never saw the plan; a question the study raised and could not answer
needs its own place, rather than folding into a single status column; or the session list, the
materials used, and where the raw notes live are worth pointing to in their own section. Use lean when
none of those is true: the decision is already clear from Summary, every question the plan set gets a
clean status in Research Questions and Answers, and nobody downstream needs the raw materials linked
from this document itself.

**Task Results ships at every size, filled in only for a usability test.** For any other method -
interviews, a diary study, a survey, a field visit - the section is one line naming the method actually
used, with the task table and the questionnaire line marked N/A. That is a complete answer, not a
placeholder waiting to be filled in later. The content this block carries, task completion against a
stated criterion, errors, time, and questionnaire scores, comes from usability-specific sources only;
no general report list in this bundle's research carries it, which is why it is conditional rather than
dropped at the smaller size.

**Two depths, not three, at medium confidence.** This is where the report differs from the plan: no
source read for the plan's own bundle names a short and a long form of one plan, but several name a
short and a long form of one report. Dovetail states the two audiences directly: "Executives want one
page with the decision; your product team wants the detail behind it." UserTesting names a third,
shortest form too, a "Quick feedback snapshot," but its four listed items each map onto a lean section
this bundle already ships, which is why this library treats it as a restatement of lean rather than a
third size.

## The rubric

Below 13 out of 18 on a full report, a reader cannot tell what the study found, what to do about it, or
how far a thin sample lets them trust it, without going back to ask the author questions this document
should have answered on its own. Below 8 out of 12 on a lean report, the same gap opens with three
fewer sections standing between a weak answer and the stakeholder reading it.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Answer comes first** | Summary opens with the method, the participant count, or a vague statement, with no finding stated | A finding is stated, but the recommendation is missing, or only restates the finding rather than naming an action | A reader who stops after Summary already knows what was found, what the team should do about it, and, where it is named, what decision that informs and who decides it |
| 2 | **Each question answered** | The section summarizes themes across the study instead of going question by question, or a question is answered more broadly than the plan asked it | Each plan question gets its own row, but the status, confirmed, contradicted, or still open, is missing or inconsistent for at least one | Every question the plan set gets its own answer, on the plan's own terms, backed by a named finding, with a status a reader can check against Key Findings |
| 3 | **Method and limits named** | Participants are reported with no denominator, so a reader cannot tell how many actually ran against how many were recruited, or no limit is stated for what this sample lets you claim | A fraction with its denominator is given, but the stated limit is generic rather than specific to what this sample size can and cannot support | The method is named and matches the plan, or a deviation is named and why; participants are a fraction with a denominator; and the stated limit names specifically what this sample lets a reader conclude and what it does not |
| 4 | **Findings carry checkable evidence** | A finding is an opinion with a number attached, no quote or observed action a reader could go check, and no positive finding appears anywhere | Evidence exists, but a count is given as a bare percentage with no denominator stated nearby, or a participant's own suggestion is folded into the team's recommendation instead of labeled as the participant's words | Every finding names a pattern, a fraction with its denominator, and a quote or observed action a reader could check; at least one positive finding carries the same evidence standard as the problems; and a participant's own suggestion is labeled as such |
| 5 | **Task Results scoped correctly** | A usability test's table has no stated success criterion behind its completion numbers, or a study that is not a usability test leaves the table blank with no line explaining why | A criterion or an N/A line is present, but thin: a completion rate with the criterion unstated, or an N/A line that names no actual method | For a usability test, every task states completion as a fraction against the plan's own success criterion, with errors and time where the plan collected them; for any other method, one line names the method used and marks the table and the questionnaire line N/A |
| 6 | **Recommends without deciding** | A recommendation names a destination with no finding behind it, or the document states what the team has decided, or names the concept it will build | Every recommendation ties to a finding, but at least one does not say why that finding makes the change worth weighing, or the line between a recommendation and a decision blurs somewhere in the section | Every recommendation names a specific change, points at the finding or findings it answers to, states why that finding makes the change worth weighing, and nowhere does the document name the decision made or the concept chosen |
| 7 | **Background links the plan** *(full only)* | The section restates the study's title, with no link to the plan and no decision restated | The plan is linked and the decision is restated, but, where this studies something people already use, the reasoning for why that is still discovery work is missing or asserted with no reasoning attached | A reader who has not seen the plan gets why the study ran, the decision restated, a working link to the plan, and, where the product already ships, a stated reason the study still asks the generative question rather than grading a spec |
| 8 | **Open Questions point forward** *(full only)* | A question restates something the study already answered, just more vaguely, or names a vague area of curiosity with no path to an answer | The question is specific, but the section does not say why this study could not answer it, or does not say what a future study would need to do differently | Each open question is specific and checkable, names why this study could not answer it, and names what a future study would need to do differently to answer it |
| 9 | **Appendix points to policy** *(full only)* | No session list or materials a reader could actually open, or a retention period stated as a figure this study set | The session list and materials are linked, but the raw notes' location names no retention policy, or restates a figure that belongs to a standing program as though it were this study's own | The session list, the materials used, and where the raw notes live are all things a reader could open, and retention points to the organization's own standing policy rather than a figure this report restates as its own |

**Which rows apply to what.** Full ships all nine rows, because a reader of a full report can ask about
the restated background, the questions the study genuinely could not reach, and where the raw materials
live, as well as the six every size must get right. Lean ships the first six, every row the lean variant
has a section to support.

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| lean | 1-6 | 12 | **8** |
| full | all 9 | 18 | **13** |

The test behind every row above: could someone satisfy the cell by adding words without the report
actually telling a reader more? Row 4's count, for instance, is never graded by how many findings are
listed; it is graded by whether a reader could go check the evidence behind any one of them, which is
the one thing padding cannot fake.

## Named anti-patterns

**Opening with the method or the participant count instead of the answer.** The tell: a reader has to
get past Background or What We Did before learning what the study found. Fix by stating what was found
and what to do about it in Summary's first lines, the way Dovetail puts it: "Put the headline finding
in the first three sentences-don't make readers excavate it."

**Answering a broader question than the one the plan asked.** The tell: Research Questions and Answers
reads like a theme summary rather than a row-by-row answer to the plan's own list. Fix by taking each
question in the plan's own words, giving it a short answer backed by a named finding, and marking
plainly whether it stayed open.

**Reporting a participant count with no denominator.** The tell: "9 participants," with no stated
number recruited, so a reader cannot tell how many actually ran against how many were asked. Fix by
stating participants as a fraction, the way Sauro and Lewis recommend: "Unless this information appears
elsewhere in your report, we recommend presenting fractions."

**Reporting an opinion with a number attached instead of a finding with evidence.** The tell: a row in
Key Findings names a feeling, such as "users don't like X," with a count and no quote or observed action
behind it. Fix by naming the pattern, the fraction, and a quote or action a reader could go check.
Dovetail states the failure directly: "A finding without evidence is an opinion with formatting."

**Reporting a completion rate with no stated success criterion.** The tell: Task Results gives a
percentage with no sentence saying what counted as success. Fix by stating the plan's own criterion
beside every completion fraction, the way NIST defines the measure itself: "The total number of
successes were calculated for each task and then divided by the total number of times that task was
attempted."

**Naming the concept the team should build, or stating that a decision has been made.** The tell:
Recommendations reads like a decision record instead of a list of changes worth weighing. Fix by
naming what is worth weighing and why, and leaving the decision itself, and the chosen concept, to a
later document such as `design-brief` or `problem-statement`.

**Restating an organization's retention period as though it were this study's own figure.** The tell: a
number of months in Appendix that reads copied from somewhere else rather than set by this study. Fix
by pointing to the organization's standing policy instead, as GOV.UK instructs: "Keep your research
data only in places that your organisation has approved for storing personal data."

**Calling this document a bare "test report" or "test results."** The tell: the word "test" appears
with no "research," "usability," or "user" attached, inviting confusion with `test-summary-report`, the
QA pair's own document. Fix by naming the document fully, a usability study report or a user research
report, never a bare "test report" or "test results."

## When it is good enough

When a reader who stops after Summary already knows what was found and what to do about it, when every
question the plan set gets its own checkable answer, when every finding carries evidence a reader could
go verify rather than an opinion with a number attached, and when the document recommends without
quietly deciding, the report has done its job.

Then self-grade against the rubric above, and delete every HTML comment. A report that reads well but
leaves a finding's evidence to the reader's trust, or that slides from recommending into deciding, has
not finished the job it exists to do, whatever else it contains.
