# Companion: The Trade Study

> The deep explainer for the trade-study bundle. Read this to understand what a trade study is, where its
> shape comes from, why the template asks for what it asks for, and where practitioners disagree about it.
> The short operator card is [`trade-study_guide.md`](trade-study_guide.md); a fully worked instance is
> [`trade-study_example.md`](trade-study_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A trade study compares a named set of technical alternatives against weighted criteria and records the
recommendation that comparison supports. NASA's Systems Engineering Handbook defines it as "a means of
evaluating system designs by devising alternative means to meet functional requirements, evaluating these
alternatives in terms of the measures of effectiveness and system cost, ranking the alternatives according
to appropriate selection criteria, dropping less promising alternatives, and proceeding to the next level of
resolution, if needed" [[1]](#ref-1). The Federal Highway Administration puts the same idea more plainly:
trade studies "compare the relative merits of alternative approaches to ensure that the most cost-effective
system is developed" [[4]](#ref-4). ECSS, the European space-engineering standard, requires the same
comparison and names what it is for: to "assist in selecting system concepts, designs and solutions"
[[3]](#ref-3). In every definition this research found, an organization has already taken the problem on,
and the question a trade study answers is which approach solves it. Cost sits inside the comparison as one
criterion among several, not as the question itself. That distinction is the ground for this type's
boundary against `business-case` ([section 8](#8-relationships-to-other-artifacts)), and it is a boundary
this bundle draws itself: no definition quoted anywhere in this research frames a trade study as the
decision whether to invest.

**At a glance**

- **The subject is technical, not financial.** A trade study chooses among named engineering approaches to
  a problem the organization already owns; it is not an investment appraisal, even though both tools can
  look like a scored table [[1]](#ref-1)[[4]](#ref-4)[[3]](#ref-3).
- **Criteria come before alternatives.** Every outline this research read that addresses ordering agrees:
  set the criteria first, "to avoid subconsciously biasing the criteria to favor a pre-determined preferred
  alternative" [[4]](#ref-4).
- **Two sizes track formality, not length alone.** NASA allows "a simple white paper or a more formally
  formatted document" [[1]](#ref-1); AcqNotes reserves the heavier process for "high-value, high-risk, or
  other high-impact decisions" [[5]](#ref-5); and Microsoft's engineering playbook says to skip the exercise
  entirely "if there is a clear solution choice" [[8]](#ref-8) ([section 4](#4-variants-and-sizing)).
- **A trade study evaluates options; it does not have to be where the decision is recorded.** This bundle's
  own division of labor hands the recorded decision to an [ADR](../adr/adr_companion.md)
  ([section 8](#8-relationships-to-other-artifacts)).
- **Nothing in this research measured whether writing a trade study improves a decision.** Every claim of
  value found here, traceability and repeatability among them, is an assertion by the bodies that
  recommend the practice, not a measured outcome [[24]](#ref-24)[[2]](#ref-2)[[4]](#ref-4). Say so plainly
  rather than borrowing more confidence than the evidence carries.

---

## 2. Origins and evolution

The trade study's clearest lineage runs through defense and aerospace systems engineering. The Defense
Systems Management College's *Systems Engineering Fundamentals* names it "a formal decision making
methodology used by integrated teams to make choices and resolve conflicts during the systems engineering
process" [[6]](#ref-6), and lays out the classic sequence this template still follows: state the problem and
its constraints, choose a weighting methodology, select viable alternatives, evaluate them against a
trade-off matrix, run a sensitivity analysis, and document the result [[6]](#ref-6). The U.S. Air Force Space
and Missile Systems Center's 2005 primer carries the same shape into a named service outline, and attributes
the practice's purpose to INCOSE: "to provide an objective foundation for the selection of one of two or more
alternative approaches to solution of an engineering problem" [[7]](#ref-7). NASA's Systems Engineering
Handbook (2016, Rev 2) folds the trade study into a broader Decision Analysis process and is the most
complete public source this research found for a decision report's expected contents, down to a named table,
"Typical Information to Capture in a Decision Report" [[1]](#ref-1). The FAA's own systems handbook, read
here only as Ullman and Spiegel quote it, calls it "the activity of a multidisciplinary team" charged with
finding "the most balanced technical solutions among a set of proposed viable solutions" [[22]](#ref-22).

The civilian and commercial lines diverge from there rather than converge. The Federal Highway
Administration's Systems Engineering for ITS guide keeps the defense-era shape but drops its formality, with
a six-item review checklist in place of a milestone-review culture [[4]](#ref-4). ECSS-E-ST-10C, the European
space standard revised in 2017, goes the other way and makes the report's content normative: its Annex L is
a clause-by-clause data-requirement document with no equivalent elsewhere in this research, down to naming
who is responsible for each criterion's evaluation and who agreed the weights [[3]](#ref-3). Decades later,
Microsoft's Code-With Engineering Playbook adapts the same skeleton for software and cloud teams as a living
web page rather than a standard, and is the only source read here that tells a team outright when to skip
the exercise [[8]](#ref-8)[[9]](#ref-9).

The scoring mechanism has its own, separate ancestry. The weighted decision matrix, also called the Pugh
method after its originator, compares each option against a reference design rather than against an absolute
scale [[12]](#ref-12). The American Society for Quality's own treatment names three distinct scoring methods,
including a numbered Pugh variant, and the multiply-and-sum rule that turns a scored row into a total
[[13]](#ref-13). Kepner-Tregoe markets a named decision-analysis methodology built around a must-have and
want-criteria split, but its own available text is a course catalogue with no content on how it actually
weights, scores, or screens [[11]](#ref-11); what this bundle can say about that split rests on a consulting
firm's description of it [[15]](#ref-15) and on a worked example styled on it [[24]](#ref-24), not on
Kepner-Tregoe's own words. The Analytic Hierarchy Process, developed by Thomas Saaty in the 1970s, derives
both weights and scores from pairwise comparisons rather than direct ratings [[16]](#ref-16). The fullest
treatment of criteria weighting this research found is a 2009 UK government manual on multi-criteria
analysis, which documents the shift from naive importance weighting toward "swing weighting" as the method
most proponents now use [[14]](#ref-14).

None of these lines rejects the trade study outright; they disagree about how formal it should be and how
its arithmetic should work. [Section 5](#5-methodology-lineage) and
[section 6](#6-debates-and-contested-boundaries) take up both disagreements in turn.

---

## 3. Anatomy (section by section)

The lean variant carries the first five sections below; the full variant adds Sensitivity Analysis, Risk and
Benefit, Dissent or Independent Review, and References, marked *(full variant only)*. The order itself is not
this bundle's invention: NASA's Table 6.8-1 runs problem, criteria setup, scoring rationale, the final
matrix, risk and benefit, recommendation, and dissent in that sequence [[1]](#ref-1), and ECSS's Annex L runs
objective, criteria, alternatives, evaluation, robustness, and conclusion in the same order [[3]](#ref-3).

### Problem and Decision Framing

States the question the study answers, the decision it feeds, who decides, and the constraints and
assumptions every alternative must respect. The FHWA puts this first for a reason: "First, define the
question the trade study is to answer" [[4]](#ref-4). AcqNotes opens its own nine-step sequence the same
way: "Define the problem - Make sure you address the actual problem, not a symptom" [[5]](#ref-5), and DSMC
warns that "defining the problem entails developing a problem statement including any constraints" and that
"problem definition should be done with extreme care" [[6]](#ref-6). SEBoK's decision context adds the
people: "the analyst should describe the system baseline, boundaries and interfaces," including "a list of
decision makers and stakeholders" [[2]](#ref-2); NASA's own decision report names its decision makers in the
same section [[1]](#ref-1), and Microsoft's template separates "Conducted by" from "Decision Makers" as two
distinct named fields [[9]](#ref-9).

*Beginner note:* write the question and name who decides before anything else. A study that skips this
drifts toward whichever alternative the author already favors, because no stated question exists to hold
the comparison to.

*Expert note:* this is also where the predetermined-winner failure gets its opening, when criteria are
written to fit an answer already chosen rather than the other way around. See
[section 6.7](#67-the-predetermined-winner-critique-one-advocacy-document-not-an-audit-finding).

### Criteria and Weights

Lists each criterion, its weight, why it was chosen and weighted that way, which criteria (if any) are
mandatory, and the scoring method and scale in use. The FHWA states both the sequencing and the mechanism:
"ideally, the criteria are developed early in the trade study process, before the alternatives are selected,
to avoid subconsciously biasing the criteria to favor a pre-determined preferred alternative" [[4]](#ref-4),
and "these disparate evaluations are merged using the weighting factors to give a measure of overall
effectiveness for each alternative" [[4]](#ref-4). ECSS requires the weighting itself to be justified, not
merely stated: "the trade-off report shall list the selected evaluation criteria and precise the
justification for selecting those criteria, and provide the weighting of criteria and their justifications"
[[3]](#ref-3), and names who is accountable for it: "the entity responsible for the evaluation of the design
solutions for any criteria, as well as the source and agreement regarding weighting factors" [[3]](#ref-3).
NASA allows criteria to be marked mandatory: "criteria may be mandatory (i.e., 'shall have') or enhancing. An
option that does not meet mandatory criteria should be disregarded" [[1]](#ref-1). AcqNotes and DSMC both
name weighting as its own explicit step [[5]](#ref-5)[[6]](#ref-6), and ASQ's procedure lays out how to turn
a rating into a weighted number [[13]](#ref-13).

*Beginner note:* pick and weight the criteria before you look hard at the alternatives, and write down why
each weight is what it is. The justification is what a reader checks six months later, not the number alone.

*Expert note:* two live arguments live in this section and the template deliberately does not resolve
either: whether a mandatory criterion should be a separate screen or folded into the weighted pass
([section 6.2](#62-a-separate-must-have-screen-or-one-weighted-pass)), and what a weight is even supposed to
mean ([section 6.4](#64-one-weight-two-meanings-importance-or-swing)).

### Alternatives, Including a Do-Nothing Baseline

Lists every option that was actually considered, how a larger field was narrowed, and a do-nothing or
do-minimum row. The FHWA's checklist asks reviewers to confirm "a broad and reasonable selection of
alternatives been examined" [[4]](#ref-4), and its own guidance is blunter: "be sure that all reasonable
alternatives are on the table" [[4]](#ref-4). NASA's trade tree is the named tool for narrowing a large field
before detailed analysis begins: "an excellent way to prune the set of variations before extensive analysis
is undertaken" [[1]](#ref-1); the FHWA achieves the same narrowing through "multiple passes where a limited
set of criteria is applied to a broad set of alternatives" [[4]](#ref-4); and Microsoft tells a team to
"brainstorm solutions" and then "pick the 2-4 solutions that seem most promising" [[8]](#ref-8).

The do-nothing row deserves a direct word, because **this bundle requires it and the sources do not.** NASA
notes only that "sometimes doing nothing or not making a decision is an option" [[1]](#ref-1), and the FHWA
calls including one "often good practice," but "depending on the nature of the trade study" [[4]](#ref-4).
Of the other outlines this research read closely, AcqNotes, Microsoft, the SMC primer, and DSMC mention no
such row at all. Requiring it is this bundle's own position, not a documented consensus, and the template
says so rather than dressing the requirement up as something every source demands. The reason to keep it
anyway is structural: adding or removing a do-nothing baseline can itself change which live option ranks
first, because that is exactly the mechanism a rank reversal describes
([section 6.1](#61-is-weighted-scoring-reliable-or-only-as-reliable-as-its-inputs)), and because a weight set
on the range between the best and worst option on a criterion [[14]](#ref-14) shifts when a new baseline
widens that range. A document that genuinely has no credible do-nothing option should say so in one line
rather than silently drop the row.

*Beginner note:* a do-nothing option can sound like an odd thing to score. It means continuing the current
system or waiting, and both of those have real costs and risks worth putting next to the others.

*Expert note:* a do-nothing row is not the same thing as a Pugh datum, and conflating the two is a specific,
recurring mistake ([section 6.3](#63-the-pugh-datum-and-the-do-nothing-baseline-are-not-the-same-thing)).

### Scoring Matrix

The completed comparison: alternatives against criteria, a weighted total per alternative, and the basis for
each individual score. The FHWA's matrix orientation is the template's own default and leaves rows and
columns to the author: "a trade study matrix that lists the alternatives on one axis, the criteria on the
second axis, and the relative scores of each alternative versus each criteria in the body of the matrix"
[[4]](#ref-4). ECSS requires the result to be presented "in a table, the result of the evaluation per
criteria" and then classified against that evaluation [[3]](#ref-3). ASQ states the arithmetic directly:
"multiply each option's rating by the weight. Add the points for each option" [[13]](#ref-13), but immediately
cautions against reading the sum as the answer: "the option with the highest score will not necessarily be
the one to choose, but the relative scores can generate meaningful discussion" [[13]](#ref-13). The FHWA adds
a readability requirement that is easy to forget while building the matrix: it "should be easily
comprehensible to management and other stakeholders who may not be as familiar with the technical details"
[[4]](#ref-4).

*Beginner note:* write the basis for each score next to the score itself, even in one phrase. A number with
no reasoning attached cannot be checked, disputed, or trusted later.

*Expert note:* the total is a prompt for discussion, not a verdict. Treating it as the decision is a failure
mode [section 7](#7-anti-patterns-and-failure-modes) names.

### Sensitivity Analysis *(full variant only)*

Asks how far a weight or a score would have to move before the recommendation changes. NASA's own definition
of the trade study report lists "computational results, including uncertainty ranges and sensitivity
analyses performed" as required content [[1]](#ref-1), and its separate treatment of uncertainty is precise
about when it matters: "uncertainty matters in a particular analysis only if there is a non-zero probability
that uncertainty reduction could alter the ranking of alternatives" [[1]](#ref-1). ECSS requires "the result
of a sensitivity analysis of the criteria that provide advantage to the solution ranked first, e.g. when
changing the weighting of the evaluation criteria" [[3]](#ref-3). DSMC states the stakes most directly: "to
ensure study viability, sensitivity analysis should always be done to examine the consequences of methodology
choice," and "if the solution can be changed with relatively minor changes in data input, the study is
probably invalid" [[6]](#ref-6). Wikipedia's decision-matrix article frames the test from the reader's own
seat: "to see how much your opinion would have to change in order for a lower ranked alternative to outrank a
competing alternative" [[12]](#ref-12). A separate, named vocabulary for the same idea comes from software
architecture tradeoff analysis, where a sensitivity point is defined as "a parameter in the architecture to
which some measurable attribute is highly correlated", such that "small changes in such parameters are
likely to have significant effects on the measurable behavior of the system", and a trade-off point is a
parameter affecting two sensitivities at once, as in one paper's own case, where "two parameters control the
tradeoff point between the overall performance of the system... and... the availability of the system"
[[20]](#ref-20). Either name is useful for pointing at the exact number in the matrix that the recommendation
actually hinges on.

*Beginner note:* pick the one or two weights or scores you are least sure of, and move them. If the
recommendation survives, say so; if it does not, say that plainly, because the reader needs to know the
recommendation turns on that number.

*Expert note:* this section is the honest answer to the false-precision critique of the whole method
([section 6.1](#61-is-weighted-scoring-reliable-or-only-as-reliable-as-its-inputs)). A matrix with no
sensitivity check invites exactly that critique and has no defense against it.

### Risk and Benefit *(full variant only)*

Covers the risks and benefits of every option still in contention, not only the one the matrix favors, plus
the mitigation the leading option would need. NASA's decision report groups "recommendation, and final
decision" together with the evaluation [[1]](#ref-1), and its decision-report table gives this content its
own row covering every option still under consideration, not only the winner. ECSS places the equivalent
content after the recommendation instead, and scopes it to the chosen solution alone: "the trade-off report
shall present the identified technical and programmatic risks induced by the choice of the recommended
solution, and any additional activity necessary to be performed for risk mitigation" [[3]](#ref-3). This
bundle follows NASA's wider scope rather than ECSS's narrower one: a reader comparing two close alternatives
wants to see what each one would have cost, not only what the winner costs. That is this bundle's own choice
between two sourced positions, stated as such.

*Beginner note:* write this section for every option still genuinely in contention, even the one you are not
recommending. A reader revisiting the decision later needs to know what the road not taken would have
required.

### Recommendation

States the option the matrix supports, the rows it depends on, the conditions under which it holds, and
reports a genuine near-tie as one outcome rather than forcing a false precision onto it. The FHWA's own
language for this step is plain: "select and document the preferred candidate" [[4]](#ref-4). ECSS requires
both the choice and its conditions: "the trade-off report shall recommend one solution and explain the
reason for this choice... and precise the condition for the application of the recommended solution"
[[3]](#ref-3). NASA allows the near-tie case explicitly: "generally, a single alternative should be
recommended. However, if the alternatives do not significantly differ, or if uncertainty reduction could
credibly alter the ranking, the recommendation should include all closely ranked alternatives for a final
selection by the decision-maker" [[1]](#ref-1), the case
[section 6.5](#65-one-recommended-option-or-every-closely-ranked-one) takes up directly. Microsoft's template
allows a different kind of honest incompleteness: the decision can instead be "a list of
questions that need to be answered before the decision can be made," each with "an action item and an
assigned person" [[9]](#ref-9).

*Beginner note:* if two options are genuinely close, say that plainly rather than reporting a winner the
matrix cannot actually support.

*Expert note:* this bundle's own division of labor stops the recommendation short of recording the decision
itself. NASA's own decision report folds "final decision" into the same section [[1]](#ref-1); this template
instead asks the author to name the decision in one line and point to the record that holds it
([section 8](#8-relationships-to-other-artifacts)).

### Dissent or Independent Review *(full variant only)*

Records who disagreed with the recommendation and how that was addressed, or who checked the scoring and how
independent of the outcome they were. NASA's decision-report table carries a named row for this, asking how
dissent was addressed. SEBoK gives the strongest named standard for independence: review "should come from
an outside body... this authority must be both organizationally and financially independent of the program
in question" [[2]](#ref-2). Bromage's practitioner advice is the same idea stated as a personal rule: "if you
stand to benefit greatly from one of the possible outcomes of the decision, have an independent, third party
lead the decision-making process" [[17]](#ref-17). The FHWA's own review checklist asks the question
directly: "have key stakeholders reviewed and support the trade study results?" [[4]](#ref-4). ECSS's Annex L
carries no equivalent clause, which is one reason this section sits in the full variant only.

*Beginner note:* name an actual person or group and what they checked. Saying the team reviewed its own work
answers a different question than saying an independent reviewer confirmed the scores.

### References *(full variant only)*

Lists the data, models, and documents the criteria, weights, and scores actually rest on. NASA's own
definition of the report requires "all data sources used" [[1]](#ref-1), and its decision-report table gives
this its own row. ECSS's Annex L lists applicable and reference documents as its second clause, right
after the introduction [[3]](#ref-3).

---

## 4. Variants and sizing

Lean carries five sections: Problem and Decision Framing, Criteria and Weights, Alternatives (Including a
Do-Nothing Baseline), Scoring Matrix, and Recommendation. Full adds Sensitivity Analysis, Risk and Benefit,
Dissent or Independent Review, and References.

The signal for which one to write is formality, and every source that addresses it points the same way.
NASA allows "a simple white paper or a more formally formatted document," leaving the choice to "the mission
and system context and the decision made" [[1]](#ref-1). AcqNotes ties the formal process to the stakes:
"generally, formal trade studies are indicated for high-value, high-risk, or other high-impact decisions"
[[5]](#ref-5), and adds that "most trade studies are not strictly formal or informal; they usually fall
between these two extremes" [[5]](#ref-5). DSMC draws the same line around where the result will be used:
formal studies "tend to be those that will be used in formal decision forums, e.g., milestone decisions,"
while the rest "are documented in summary detail only, but they are important in that they define the design
as it evolves" [[6]](#ref-6). Microsoft's playbook goes a step further than either and names the condition
for skipping the exercise entirely: "trade studies should be avoided if there is a clear solution choice...
when there is a clear design, the trade study should be omitted, and an entry should be made in the Decision
Log" [[8]](#ref-8).

A practical reading of all four: write lean when the stakes are contained and the comparison is between a
small set of options whose tradeoffs are already mostly understood; write full when the decision is hard to
reverse, the field disagrees about the criteria or their weights, or a reviewer outside the immediate team
will need to check the reasoning later. Write nothing at all, and log the decision directly, when there was
never a real second option.

---

## 5. Methodology lineage

The trade study is methodology-agnostic in the sense that matters for this template: the catalog classifies
it that way, and this research did not look for a software-delivery methodology that defines or governs
it. What differs by tradition is how formal the practice is expected to be and how the scoring is done.

**Defense and aerospace acquisition** treats the trade study as part of a milestone-review culture: DSMC's
process feeds "formal decision forums" [[6]](#ref-6), the SMC primer's outline is a named service-level
template with its own cost- and risk-analysis subsections [[7]](#ref-7), and AcqNotes documents a nine-step
sequence tied to program decisions [[5]](#ref-5). **European space systems engineering**, through ECSS, is
the most prescriptive tradition this research found: its Annex L is a normative data-requirements document,
not a recommended outline, and it is the only source here that names an accountable party for each
criterion's evaluation [[3]](#ref-3). **U.S. civil systems engineering**, through the FHWA's guide for
transportation ITS projects, keeps the same process shape at a lighter formality, with a short review
checklist in place of a milestone-review board [[4]](#ref-4). **General systems engineering**, through
NASA's handbook and SEBoK, treats the trade study as one instrument inside a broader Decision Analysis
discipline, with its own named participants (analyst, decision team, decision maker, subject matter experts,
stakeholders) and its own cognitive-bias literature [[1]](#ref-1)[[2]](#ref-2). **Quality engineering**
contributes the scoring mechanism more than the process shape: ASQ's decision matrix and the Pugh method it
names are quality tools applied here to a technical comparison, and the same tool is also used outside
engineering entirely to rank investment and vendor options [[12]](#ref-12)[[13]](#ref-13)
([section 6.6](#66-analysis-of-alternatives-the-vocabulary-two-different-decisions-share)). **Modern software
and cloud engineering**, through Microsoft's Code-With Engineering Playbook, is the lightest tradition this
research found and the only one that names a condition for skipping the exercise outright [[8]](#ref-8).
**Consulting frameworks**, Kepner-Tregoe and the Pugh-matrix literature that cites it, sell the must-have and
want-criteria split as packaged methodology, though this research could read only secondary descriptions of
Kepner-Tregoe's own text [[11]](#ref-11)[[15]](#ref-15).

None of these traditions rejects the trade study; the practitioner sources that describe no must-have screen
at all (the FHWA, AcqNotes, Microsoft, the SMC outline) are silent on the question rather than disagreeing
with it [[4]](#ref-4)[[5]](#ref-5)[[8]](#ref-8)[[7]](#ref-7).

---

## 6. Debates and contested boundaries

### 6.1 Is weighted scoring reliable, or only as reliable as its inputs?

One camp treats the arithmetic itself as fragile. A rank reversal is "a change in the rank ordering of the
preferability of alternative possible decisions when, for example, the method of choosing changes or the set
of other available alternatives changes" [[18]](#ref-18), and the methods confirmed to exhibit it include
"the analytic hierarchy process (AHP) and some of its variants" and "the TOPSIS method" [[18]](#ref-18).
Wikipedia's decision-matrix article states the false-precision worry directly: "the values assigned to each
option are guesses, not based on any quantitative measurements" [[12]](#ref-12), and mechanicalc warns
plainly that "the results of the trade study should not be taken as absolute" [[23]](#ref-23). Ullman and
Spiegel go further and say the standard matrix "can not support uncertainty, a mix of quantitative and
qualitative information, or teams" [[22]](#ref-22).

The other camp locates the failure in the inputs, not the method. Bromage writes "I use it often, and I
think its simplicity is the key to its popularity," and puts the real risk in "the selection of decision
objectives, the criteria for making the decision" [[17]](#ref-17). ASQ treats the total as a prompt rather
than a verdict: "the option with the highest score will not necessarily be the one to choose" [[13]](#ref-13).
Even the rank-reversal camp is divided on whether the phenomenon is always a defect: Wikipedia calls the
question itself "highly debated" and notes that a reversal "may not be indicative to faulty decision making"
[[18]](#ref-18), and the current version of AHP offers one mode that "preserves rank" and one that "allows
the ranks to change" [[16]](#ref-16).

This bundle does not adjudicate. Its position, stated through the template, is to require a named scoring
method and a justified weight per criterion [[3]](#ref-3), a full sensitivity check [[6]](#ref-6)[[14]](#ref-14),
and the discipline of treating the total as something that informs the recommendation without making it for
you [[13]](#ref-13). One honest gap: George Hazelrigg's structural critique of weighted scoring, and the
primary texts behind both Pugh's and Saaty's methods, were not available to this research in primary form.
What this bundle says about Pugh and AHP rests on secondary treatments [[12]](#ref-12)[[13]](#ref-13)
[[15]](#ref-15)[[16]](#ref-16)[[14]](#ref-14), and no consistency-ratio threshold for AHP appears anywhere in
this bundle because none was found sourced.

### 6.2 A separate must-have screen, or one weighted pass?

NASA treats some criteria as mandatory, with a hard rule: "an option that does not meet mandatory criteria
should be disregarded" [[1]](#ref-1). The UK government's MCA manual names the formal version of this screen,
the conjunctive model, and is honest about when it earns its own step: it "eliminates options that fail to
reach externally set levels of performance," and is valid "if the external benchmarks are set independently,"
though "it is arguable that it scarcely needs formal MCA to make the judgement" [[14]](#ref-14). Wikipedia
names the risk of skipping the screen: "scoring methods, even with weighting, tend to equalize all the
requirements. But a few requirements are 'must haves'. If enough minor criteria are listed, it is possible
for them to add up and select an option that misses a 'must have' requirement" [[12]](#ref-12). Umbrex
attributes a formal version of this split to Kepner-Tregoe: "Kepner-Tregoe is typically more formal. It
separates must-have requirements from wants" [[15]](#ref-15), and Baker and Whalen's worked example screens
every option against named must-haves before any weighted scoring begins [[24]](#ref-24).

The FHWA, AcqNotes, Microsoft, and the SMC outline describe no must-have screen at all, which this bundle
reads as silence rather than disagreement; the FHWA's multiple-pass narrowing achieves something similar
without naming a formal gate [[4]](#ref-4). ASQ's instruction to "identify any criteria that must be included
and any that must not be included" [[13]](#ref-13) is about curating the criteria list itself, and should not
be read as this same performance screen. The sources agree on the risk and differ on the remedy; the template
leaves the choice to the author and asks that a mandatory marker, where used, be stated plainly.

### 6.3 The Pugh datum and the do-nothing baseline are not the same thing

A Pugh datum is a comparator every other option is scored against, not necessarily a candidate in its own
right. Umbrex: "then select the datum, which may be the current product, the status quo, the leading
concept, or another reasonable reference point" [[15]](#ref-15). ASQ's own Pugh variant does the same:
"establish a baseline, which may be one of the alternatives or the current product or service" [[13]](#ref-13).
Umbrex also carries the clearest warning about that choice: "it is sensitive to the datum. A poor or biased
reference option can distort the entire comparison," and the fix is to "test whether conclusions change when
the datum changes" [[15]](#ref-15).

A do-nothing baseline, as this bundle requires it, is different in kind: it is a scored alternative in its
own right, not merely the ruler the others are measured against. The FHWA frames it that way, as an
alternative scored "as the base case, depending on the nature of the trade study" [[4]](#ref-4), and so does
NASA, naming it as something that is "sometimes" an option, not the default yardstick [[1]](#ref-1). No
source read for this bundle calls a Pugh datum a do-nothing alternative, and the template should not either.
An author who wants to use the do-nothing baseline as the Pugh datum as well may do so, but that choice
inherits Umbrex's caution about a biased reference point, and the template does not make that choice for
them.

### 6.4 One weight, two meanings: importance or swing?

Wikipedia states the naive version plainly: "the more important the criterion the higher the weighting it
should be given" [[12]](#ref-12), and ASQ's simplest method distributes weight the same way, "by distributing
10 points among the criteria" [[13]](#ref-13). The UK government's MCA manual documents a different and, it
says, now more common practice: "most proponents of MCDA now use the method of 'swing weighting' to elicit
weights for the criteria," because "the weight on a criterion reflects both the range of difference of the
options, and how much that difference matters" [[14]](#ref-14). These are two different definitions of the
same word, not two names for one idea, and a weight set under one definition is not comparable to a weight
set under the other. The sources also differ on whether Pugh scores should even be summed: the basic matrix
displays its tallies "but not summed up" [[12]](#ref-12), ASQ multiplies and adds [[13]](#ref-13), and Umbrex
reports that "some [teams] also add criterion weights or convert symbols into numbers" [[15]](#ref-15). The
template asks the author to state which meaning their weights carry; it does not pick one for them.

### 6.5 One recommended option, or every closely ranked one?

ECSS requires a single answer: "the trade-off report shall recommend one solution and explain the reason for
this choice" [[3]](#ref-3). NASA allows more room: "generally, a single alternative should be recommended,"
but where the alternatives do not differ significantly, or uncertainty could alter the ranking, "the
recommendation should include all closely ranked alternatives for a final selection by the decision-maker"
[[1]](#ref-1). Microsoft's template allows a third kind of honest outcome entirely, a decision deferred to
"a list of questions that need to be answered before the decision can be made," each with "an action item and
an assigned person" [[9]](#ref-9). This bundle reads ECSS's single-answer rule against NASA's and Microsoft's
more honest handling of a genuine near-tie, and lets the Recommendation section report a close result as one,
naming what would separate the options, rather than forcing a false precision onto a comparison that cannot
support it.

### 6.6 "Analysis of alternatives": the vocabulary two different decisions share

The phrase "analysis of alternatives" names two different things depending on who is using it, and the
scoring mechanism underneath does not separate them; the subject of the decision does. In defense
acquisition, the phrase names a decision about what to procure: RAND's presentation to an acquisition
research symposium frames it around "measuring the cost and benefits of each alternative," with a named
effectiveness-analysis task and a separate life-cycle-cost-estimation task feeding a combined
cost-effectiveness comparison [[25]](#ref-25). Yet the SMC primer's own trade study outline lists an analysis
of alternatives, glossed there as a comparative analysis, as one purpose a trade study can serve
[[7]](#ref-7), and Wikipedia notes that the decision matrix, "frequently used in engineering for making
design decisions," is also used to rank investment and vendor options [[12]](#ref-12). A reader who reaches
for this type under the label "analysis of alternatives" expecting an investment appraisal will find a
technical comparison instead, and the reverse is just as true. Treat the phrase as a shared name for two
different jobs, not as another name for the same job this bundle covers.

### 6.7 The predetermined-winner critique: one advocacy document, not an audit finding

The strongest statement of this failure in this research comes from an advocacy document, not a neutral
audit. A critique prepared for two trade unions opposing a public-sector service transfer says plainly: "the
options appraisal process is flawed because it is operating to a predetermined agenda," and describes a
sequence that opens with the decision already made: "decide on a preferred solution" and "select a consultant
who will deliver the" chosen direction [[21]](#ref-21). Bromage's own anecdote is the same pattern from the
inside: "lo and behold, the alternative selected based on the evaluation of the decision objectives ended up
to be number 4! That was no surprise" [[17]](#ref-17). Both are worth naming because the mechanism they
describe, criteria and weights reverse-engineered from an answer already chosen, is a real and recurring
failure mode ([section 7](#7-anti-patterns-and-failure-modes)). Neither is evidence of how often it happens;
the advocacy document is one party's account of one case, and the anecdote is one practitioner's story. Name
the pattern without claiming either source proved its frequency.

---

## 7. Anti-patterns and failure modes

- **Criteria chosen after the alternatives, to favor one.** The exact inversion of the FHWA's own advice to
  set criteria "before the alternatives are selected, to avoid subconsciously biasing the criteria to favor a
  pre-determined preferred alternative" [[4]](#ref-4), and the mechanism behind
  [section 6.7](#67-the-predetermined-winner-critique-one-advocacy-document-not-an-audit-finding).
- **A criterion with no way to measure it.** Bromage names this directly as a way to dodge scrutiny: it lets
  someone "avoid exposing yourself to criticism in your analysis by selecting weak criteria that have only
  qualitative evaluation possibilities" [[17]](#ref-17).
- **A must-have outvoted by a pile of minor criteria.** Wikipedia's own warning about weighted scoring:
  enough small criteria "can add up and select an option that misses a 'must have' requirement"
  [[12]](#ref-12) ([section 6.2](#62-a-separate-must-have-screen-or-one-weighted-pass)).
- **A recommendation that flips on a small input change, with no sensitivity check to catch it.** DSMC's own
  diagnosis: "if the solution can be changed with relatively minor changes in data input, the study is
  probably invalid" [[6]](#ref-6).
- **Scorers using the same scale differently, with no discussion to reconcile it.** Donald's account of panel
  scoring: "if asked to score between 1 and 10 against some criterion, some people will use the full range,
  but others will probably cluster scores between 4 and 8" [[19]](#ref-19); and anchoring on whoever speaks
  first, "a strongly positive message can be conveyed which later speakers find hard or are unwilling to
  challenge" [[19]](#ref-19).
- **Averaging disagreement instead of resolving it.** ASQ's rule is explicit: "do not average the ratings or
  vote for the most popular one" when scorers disagree [[13]](#ref-13).
- **A biased or unexamined datum, when the scoring method uses one.** Umbrex's own caution: "a poor or biased
  reference option can distort the entire comparison" [[15]](#ref-15)
  ([section 6.3](#63-the-pugh-datum-and-the-do-nothing-baseline-are-not-the-same-thing)).
- **Treating the weighted total as the decision rather than a prompt for one.** ASQ and mechanicalc both warn
  against this directly: the highest score "will not necessarily be the one to choose" [[13]](#ref-13), and
  "the results of the trade study should not be taken as absolute" [[23]](#ref-23).
- **Treating a vendor's current documentation as a timeless property of the technology.** A criterion like a
  message broker's durability guarantee depends on a specific configuration, not the product's name alone;
  Apache Kafka's own documentation states the tradeoff as a setting the producer chooses, "depending on their
  preference for tradeoff between latency and durability" [[26]](#ref-26), not as a fixed property of Kafka.
  Any technical fact scored into a matrix from product documentation is a snapshot of that documentation on
  the day it was read, and should be dated as such.

---

## 8. Relationships to other artifacts

A trade study's job, evaluating named alternatives against weighted criteria, is none of the three verbs the
decision-docs family contract assigns its members: an RFC proposes a decision, an ADR records one, and an
SDD describes an implementation, per
[ADR 0022 (adopt the decision-docs family contract)](../../docs/internal/decisions/0022-adopt-decision-docs-family-contract.md).
Read that contract clause alone and a trade study would not belong in this family at all. It joins instead
under the record that adopted the contract, whose consequences say a further member "would join under the
same contract with no contract change unless it declares a different phase or size shape", the same way
`spike-report` joined earlier. A trade study evaluates options rather than proposing, recording, or
describing a decision, and that is the fifth role in the family, after `spike-report`'s investigation,
rather than a variation on one of the first three.

- **Feeds an [ADR](../adr/adr_companion.md).** The options a trade study evaluates are exactly the input an
  ADR's own Alternatives Considered section needs, and the decision the trade study's recommendation supports
  is what the ADR records, immutably, after it is made. NASA's own decision report folds the final decision
  into the same document as the evaluation [[1]](#ref-1); this bundle deliberately separates the two, and
  Microsoft's playbook recommends the identical hand-off in its own vocabulary: "once the decision has been
  made we recommend adding an entry to the Decision Log that has references back to the full text of the
  trade study" [[8]](#ref-8). A trade study's Recommendation section may name the decision taken in one line,
  but the ADR is where that decision is recorded for good.
- **Can be cited by an [RFC](../rfc/rfc_companion.md).** An RFC proposes a decision and asks for feedback
  before it is made; where its own Alternatives Considered prose needs a weighted comparison rather than a
  paragraph of reasoning, it can point to a trade study carrying that comparison, rather than duplicating the
  matrix inline.
- **Can be cited by an [SDD](../sdd/sdd_companion.md).** A design document describes how a system will be
  built, and its own Alternatives Considered section can likewise point to a trade study when the choice
  among approaches needed a weighted comparison rather than a short discussion.
- **Follows a [spike report](../spike-report/spike-report_companion.md).** A spike reduces a specific
  technical unknown before the options in a trade study can even be named with confidence; where the
  alternatives themselves are still uncertain, that uncertainty is a spike's job to resolve first.
- **Is not a [business case](../business-case/business-case_companion.md).** The boundary stated in
  [section 1](#1-orientation) is worth restating here because it is the one most likely to be confused in
  practice: no definition of a trade study read for this research frames it as a decision about whether to
  invest, and the only source in this research that uses the term "business case" places it after an options
  appraisal, in that investment sense [[21]](#ref-21). The line is clean on subject, choosing among technical
  approaches to a problem already owned, and blurred only in vocabulary: SEBoK says trade studies "aim to
  define, measure, and assess shareholder and stakeholder" value [[2]](#ref-2), the SMC outline lists an
  analysis of alternatives among a trade study's purposes [[7]](#ref-7), and the decision matrix itself is
  also used for investment ranking [[12]](#ref-12), the overlap
  [section 6.6](#66-analysis-of-alternatives-the-vocabulary-two-different-decisions-share) names directly.
  A reader deciding whether to invest in something at all wants `business-case`; a reader who has already
  decided to solve a problem and needs to choose how wants this type.

---

## 9. Adaptations

- **Regulated and safety-critical settings.** Adopt ECSS's clause-by-clause discipline even outside space
  engineering: name who is responsible for each criterion's evaluation, require a signed-off weighting
  scheme, and treat the sensitivity analysis and the recommendation's conditions as mandatory content, not
  optional polish [[3]](#ref-3).
- **Defense and large-program acquisition.** Expect the full variant tied to a milestone-review culture, with
  cost and risk analysis as named subsections of their own, matching the SMC primer's and AcqNotes' service
  and program-level outlines [[7]](#ref-7)[[5]](#ref-5).
- **Civil infrastructure and public-sector systems engineering.** The FHWA's lighter process view, with its
  short review checklist in place of a formal milestone board, is the closest documented fit for a public
  agency that wants the same rigor without the acquisition apparatus [[4]](#ref-4).
- **Software and cloud teams.** Microsoft's playbook is the clearest model: default to lean, skip the exercise
  entirely when the choice is already obvious, and route the finished decision into a Decision Log rather
  than treating the trade study itself as the permanent record [[8]](#ref-8)[[9]](#ref-9), the same hand-off
  [section 8](#8-relationships-to-other-artifacts) describes.
- **Solo work and small teams.** The lean variant, or an even shorter version of it, is enough when the
  stakes are contained; the point of writing anything down is to force the criteria into the open before the
  choice is made, not to produce a formal artifact for its own sake.
- **Choice of scoring method.** Nothing here requires one scoring method over another. A team comfortable
  with a reference design can use a Pugh-style datum comparison [[12]](#ref-12)[[15]](#ref-15); a team that
  wants an additive, weighted total can use ASQ's multiply-and-sum procedure [[13]](#ref-13); a team facing a
  genuinely hard-to-compare set of criteria can use pairwise comparison, carrying AHP's own rank-reversal
  caveat with it [[16]](#ref-16)[[14]](#ref-14); see
  [section 6.1](#61-is-weighted-scoring-reliable-or-only-as-reliable-as-its-inputs). State the chosen method
  in the Criteria and Weights section rather than leaving the reader to infer it from
  the numbers.
- **Methodology.** The template is methodology-agnostic by design, matching the catalog's own classification
  of the type; this research did not look for a software-delivery methodology that governs it. Use it inside
  whatever delivery process already governs the decision it feeds.

---

## 10. Worked example

[`trade-study_example.md`](trade-study_example.md) works through a fictional logistics company choosing a
message-ingestion technology for GPS telemetry from its truck fleet, scored against its current nightly
batch upload as the do-nothing baseline. The technical facts behind its criteria and scores are drawn from
primary vendor and project documentation, read in full rather than summarized
[[26]](#ref-26)[[27]](#ref-27)[[28]](#ref-28)[[29]](#ref-29)[[30]](#ref-30)[[31]](#ref-31). Every one of those
facts is a snapshot of a product's documentation as read on a stated date, not a timeless property of the
technology, and the example labels its figures as illustrative for exactly that reason
([section 7](#7-anti-patterns-and-failure-modes)).

---

## References

Tagged by reliability, following this bundle's research log: `[primary]` the originating standards body,
regulator, or source document itself; `[standards]` a named standards or professional body's published
guidance; `[practitioner]` a recognized independent authority, consulting resource, or widely used reference
page; `[vendor]` a commercially motivated source, reliable on convention and corroborated for claims of
fact. Researched 2026-10-15; per-source retrieval status, every quotation's verification against raw text,
and what was not retrieved are recorded in full in
[`trade-study_research-log.md`](trade-study_research-log.md). Only sources marked fetched-and-verified there
are quoted here, verbatim from the log's own Quotable lines.

<a id="ref-1"></a>[1] NASA. "[NASA Systems Engineering Handbook, SP-2016-6105 Rev 2](https://ntrs.nasa.gov/api/citations/20170001761/downloads/20170001761.pdf)." NASA, 2016 (accessed 2026-10-15). Supports the handbook's definitions of trade study and trade study report, Section 6.8's Decision Analysis process, mandatory versus enhancing criteria, the trade tree, uncertainty and sensitivity treatment, the single-or-closely-ranked recommendation rule, the two-size allowance, and Table 6.8-1's content and row order. [primary]

<a id="ref-2"></a>[2] SEBoK Editorial Board (Lead Author Matt Cilli; Contributing Authors Garry Roedler, Greg Parnell, Scott Jackson). "[Decision Management](https://sebokwiki.org/wiki/Decision_Management)." SEBoK wiki (accessed 2026-10-15). Supports the trade study's standing as the most common decision-management method among systems engineers, the decision-context elements, the named roles, the cognitive-bias caution, and the independent-review standard. [standards]

<a id="ref-3"></a>[3] ECSS Secretariat. "[ECSS-E-ST-10C Rev.1, Space engineering - System engineering general requirements](https://ecss.nl/wp-content/uploads/2017/02/ECSS-E-ST-10C-Rev.1(15February2017).pdf)." ECSS, 2017-02-15 (accessed 2026-10-15). Supports the trade-off analysis requirement and the normative Annex L content requirements: justified criteria and weights, a named accountable evaluator, a results table, a classification, a sensitivity analysis, a recommendation with conditions, and the recommended solution's induced risks. [standards]

<a id="ref-4"></a>[4] Federal Highway Administration. "[Systems Engineering for ITS (SEITS), Section 3.4.5, Conduct Trade Studies](https://ops.fhwa.dot.gov/seits/sections/section3/3_4_5.html)." FHWA, Process View (accessed 2026-10-15). Supports the full trade study step sequence, the criteria-before-alternatives ordering, the weighting-factor merge, the trade matrix orientation, the do-nothing alternative, the readability requirement, and the six-item review checklist. [standards]

<a id="ref-5"></a>[5] AcqNotes. "[Trade Study](https://acqnotes.com/acqnote/careerfields/trade-study)." AcqNotes, Systems Engineering career field (accessed 2026-10-15). Supports a nine-step trade study sequence, the full report-content list, and the formal-versus-informal tailoring guidance tied to decision stakes. [practitioner]

<a id="ref-6"></a>[6] Defense Systems Management College. "Systems Engineering Fundamentals, Chapter 12, Trade Studies" (retrieved via [METU OpenCourseWare mirror](https://ocw.metu.edu.tr/pluginfile.php/408/mod_resource/content/0/lecture12.pdf)). DSMC (accessed 2026-10-15). Supports the classic trade study process sequence, the weighting-methodology step, the trade-off matrix and sensitivity-analysis requirement, and the formal-versus-informal distinction tied to decision forums. [standards]

<a id="ref-7"></a>[7] U.S. Air Force Space and Missile Systems Center. "[SMC Systems Engineering Primer & Handbook](https://spacese.spacegrant.org/SEModules/Reference%20Docs/SMC_SE_Primer4-05.pdf)," 4th ed., Chapter 4 and Appendix C8. SMC, 2005-04-29 (accessed 2026-10-15). Supports the named example trade study outline, the Sensitivity Analysis step, DSMC's definition as quoted here, and INCOSE's purpose statement as the primer quotes it. [standards]

<a id="ref-8"></a>[8] Microsoft. "[Trade Studies](https://microsoft.github.io/code-with-engineering-playbook/design/design-reviews/trade-studies/)." Code-With Engineering Playbook (accessed 2026-10-15). Supports the five-step trade study flow, the skip-if-clear guidance, the 2-4-alternatives shortlisting advice, and the hand-off to a separate Decision Log. [vendor]

<a id="ref-9"></a>[9] Microsoft. "[Trade Study Template](https://microsoft.github.io/code-with-engineering-playbook/design/design-reviews/trade-studies/template/)." Code-With Engineering Playbook (accessed 2026-10-15). Supports the named Conducted-by and Decision-Makers fields, explicit assumptions and constraints sections, evidence-backed solution evaluation, and the option to leave the decision as open questions with owners. [practitioner]

<a id="ref-11"></a>[11] Kepner-Tregoe. "[Think Clearly / Decision Making](https://kepner-tregoe.com/solution/think-clearly-decision-making/)." Kepner-Tregoe (accessed 2026-10-15). Confirms Kepner-Tregoe markets a named decision-analysis methodology and sells training on it; the page carries no methodological content on how the method weights, scores, or screens, which is why this bundle attributes the must/want split to secondary sources instead. [vendor]

<a id="ref-12"></a>[12] Wikipedia contributors. "[Decision-matrix method](https://en.wikipedia.org/wiki/Decision-matrix_method)." Wikipedia (accessed 2026-10-15). Supports the Pugh-method naming, the basic (unsummed, reference-design) versus weighted matrix distinction, the sensitivity-study description, the must-have-outvoted warning, and the method's dual use in engineering and investment ranking. [practitioner]

<a id="ref-13"></a>[13] American Society for Quality. "[What is a Decision Matrix? Pugh, Problem, or Selection Grid](https://asq.org/quality-resources/decision-matrix)." ASQ (accessed 2026-10-15). Supports the full named procedure for weighting criteria, three distinct scoring methods including a numbered Pugh variant, the multiply-and-sum rule, the no-averaging-disagreement rule, and the caution against treating the total as the decision. [practitioner]

<a id="ref-14"></a>[14] Department for Communities and Local Government (UK). "[Multi-criteria analysis: a manual](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/7612/1132618.pdf)." UK Government, 2009 (accessed 2026-10-15). Supports the eight-step MCA process, swing weighting as the modern standard, the conjunctive (must-have) screening model, and the rank-reversal critique of AHP's pairwise weighting. [standards]

<a id="ref-15"></a>[15] Umbrex. "[Pugh Matrix](https://umbrex.com/resources/frameworks/decision-making-frameworks/pugh-matrix/)." Umbrex (accessed 2026-10-15). Supports the datum/baseline concept and its candidate anchors, the classic scoring convention, the datum-sensitivity caution, and the attributed comparison to Kepner-Tregoe's must/want split. [vendor]

<a id="ref-16"></a>[16] Wikipedia contributors. "[Analytic hierarchy process](https://en.wikipedia.org/wiki/Analytic_hierarchy_process)." Wikipedia (accessed 2026-10-15). Supports AHP's origin with Thomas L. Saaty in the 1970s, its pairwise-comparison derivation of weights and
scores, the consistency-check step, and the two named schools of thought on rank reversal. [practitioner]

<a id="ref-17"></a>[17] Bromage, Alex (Kepner-Tregoe Program Leader, Tetra Pak). "[Decisions Decisions...](https://kepner-tregoe.com/blogs/decisions-decisions)." Kepner-Tregoe Blog, 2016-03 (accessed 2026-10-15). Supports the favored-option-framed-in failure, weak-criteria selection as a way to dodge scrutiny, and the independent-third-party remedy when the analyst has a stake in the outcome. [practitioner]

<a id="ref-18"></a>[18] Wikipedia contributors. "[Rank reversals in decision-making](https://en.wikipedia.org/wiki/Rank_reversals_in_decision-making)." Wikipedia (accessed 2026-10-15). Supports the definition of a rank reversal, the methods confirmed to exhibit it, and the ongoing debate over whether a reversal is always a defect. [practitioner]

<a id="ref-19"></a>[19] Donald, Athene. "[The ABC of panel scoring: Anchoring, Bias and Committee Procedures](https://occamstypewriter.org/athenedonald/2017/01/20/the-abc-of-panel-scoring-anchoring-bias-and-committee-procedures/)." Occam's Typewriter, 2017-01-20 (accessed 2026-10-15). Supports inconsistent scale use across scorers, anchoring on an initial figure or first speaker, and order-of-presentation effects in group scoring. [practitioner]

<a id="ref-20"></a>[20] Kazman, Rick; Barbacci, Mario; Klein, Mark; Carriere, S. Jeromy (Software Engineering Institute, Carnegie Mellon University). "[Experience with Performing Architecture Tradeoff Analysis](https://www.se.rit.edu/~se440/documents/atam_experience.pdf)." SEI/CMU (accessed 2026-10-15). Supports ATAM's own definitions of a sensitivity point and a trade-off point, and that an architecture evaluation produces a written output. [primary]

<a id="ref-21"></a>[21] European Services Strategy Unit (prepared for GMB and Unison). "[Adult Social Care In-House Provider Services: Options Appraisal, Critique](https://www.european-services-strategy.org.uk/wp-content/uploads/2014/09/barnet-adult-services-option-appraisal.pdf)." London Borough of Barnet, 2014-09 (accessed 2026-10-15). A critique prepared for two trade unions opposing the service transfer it describes, not a neutral audit. Supports a documented public-sector case alleging a predetermined agenda in an options appraisal, and the term "business case" used in the investment sense. [practitioner]

<a id="ref-22"></a>[22] Ullman, David G.; Spiegel, Brian P. "Trade Studies with Uncertain Information." INCOSE 16th Annual International Symposium, 2006 (accessed 2026-10-15). Supports the limits of the standard decision-analysis matrix with uncertain, mixed, or team-generated information, the uncertainty-range supplement to point estimates, and the FAA's definition of a trade study as quoted here. [primary]

<a id="ref-23"></a>[23] mechanicalc.com. "[Trade Study](https://mechanicalc.com/reference/trade-study)." mechanicalc.com (accessed 2026-10-15). Supports a worked qualitative rating scale and the caution that an undisclosed bias in weighting or rating is reflected directly in the result. [practitioner]

<a id="ref-24"></a>[24] Baker, Paula J. (NASA IV&V Facility / TASC, Inc.); Whalen, James T. (Stevens Institute of Technology). "[Survey of Trade Study Methods for Practical Decision-Making](https://www.nasa.gov/wp-content/uploads/2016/10/survey_of_trade_study_methods_-_baker.pdf)." Conference poster (accessed 2026-10-15). Supports documenting a trade study for traceability and repeatability, and a worked example that screens alternatives against named must-haves before weighting the remaining criteria. [primary]

<a id="ref-25"></a>[25] RAND Corporation. "Analysis of Alternatives: Keys to Success." NPS Annual Acquisition Research Symposium, 2012-05 (accessed 2026-10-15). Supports the acquisition sense of "analysis of alternatives," kept as a distinct cost-versus-effectiveness comparison, and a steering group's approval of interim study decisions. [practitioner]

<a id="ref-26"></a>[26] Apache Software Foundation. "[Apache Kafka 4.2 Documentation, Design, Replication](https://kafka.apache.org/42/design/design/)." Apache Kafka (accessed 2026-10-15). Supports the per-topic replication factor, the leader/follower and in-sync-replica model, the `acks` setting as a stated latency/durability tradeoff, and the conditional nature of Kafka's durability guarantee. [primary]

<a id="ref-27"></a>[27] Amazon Web Services. "[Amazon Kinesis Data Streams Developer Guide, Key Concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html)." AWS (accessed 2026-10-15). Supports Kinesis's default and maximum retention periods, per-shard throughput limits, and on-demand versus provisioned capacity modes. [primary]

<a id="ref-28"></a>[28] Amazon Web Services. "[Amazon MSK Developer Guide, What Is Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html)." AWS (accessed 2026-10-15). Supports what MSK manages on the customer's behalf (control plane, ZooKeeper and KRaft nodes, broker-failure detection and replacement), the per-Availability-Zone broker minimum, and MSK Serverless's framing. [primary]

<a id="ref-29"></a>[29] VMware/Broadcom (the RabbitMQ project). "[RabbitMQ Documentation, Streams](https://www.rabbitmq.com/docs/streams)." RabbitMQ (accessed 2026-10-15). Supports Streams' persistence and replication model, the publisher-confirm delivery guarantee, the no-fsync-by-default durability trap, and the operator's responsibility for replica and quorum management. [primary]

<a id="ref-30"></a>[30] NATS.io / CNCF. "[NATS Concepts: JetStream](https://docs.nats.io/nats-concepts/jetstream)." NATS documentation (accessed 2026-10-15). Supports JetStream's at-least-once delivery guarantee, contrasted with Core NATS's at-most-once default. [primary]

<a id="ref-31"></a>[31] Google LLC. "[Google Cloud Pub/Sub Documentation, Exactly-once delivery](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery)." Google Cloud (accessed 2026-10-15). Supports the pull-only and same-region scope of Pub/Sub's exactly-once feature, and the publish-side duplication and acknowledgment-failure cases it does not cover. [primary]
