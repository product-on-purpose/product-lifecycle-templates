# Companion: The Experiment Readout

> The deep explainer for the experiment-readout bundle. Read this to understand what the document is,
> where its sections come from, and where the sources genuinely disagree. The short operator card is
> [`experiment-readout_guide.md`](experiment-readout_guide.md); a fully worked instance is
> [`experiment-readout_example.md`](experiment-readout_example.md). Inline citations like
> [[1]](#ref-1) resolve to the [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

An experiment readout reports one concluded test: what ran, the results with their uncertainty, whether
those results can be trusted, and the decision they drove, with its owner. Optimizely's own stakeholder
guidance gives the core in five fields, Purpose, Details, Results, Lessons Learned and Revenue Impact
[[3]](#ref-3), and Eppo ships a fillable shape that carries the same job end to end [[1]](#ref-1). The
document exists after a test has run its course, not during it: Amplitude's fourth phase is named
plainly, "Phase 4: Analyze and Decide" [[7]](#ref-7), and Optimizely's own guidance is to "Share results
with the rest of your organization at the end of each test" [[3]](#ref-3).

**At a glance**

- It is **post-test and decision-bearing**. The family contract's own wording is that a readout reports
  "the decision the results drove (ship, iterate or stop), after the test ends," and that finish line is
  the recorded decision, not the reading of the result
  ([contract](../../docs/internal/contracts/experimentation-docs.md), section 1).
- It is the second half of a sequential pair. The
  [experiment-design-doc](../experiment-design-doc/experiment-design-doc_companion.md) states the
  hypothesis, the allocation, the sample size and the decision rule before the test runs; this document
  reports against that plan after the test ends, and must report the same test
  ([contract](../../docs/internal/contracts/experimentation-docs.md), section 4).
- **The written document is in scope. A live scorecard and a one-time export are not.** Optimizely's
  Experiment Scorecard is a live, configurable in-tool surface assembled from modules ("An Experiment
  Scorecard template consists of the following modules:") [[21]](#ref-21); Statsig's
  export is a one-time PDF of "Key Setup Information" and "granular metric-by-metric raw stats," with no
  decision field [[22]](#ref-22). Microsoft's own research answers the automation question directly: asked
  whether evaluation can be automated from metric movements alone, the answer is "Not quite," because "the
  experimentation platform typically has limited context about the experiment itself" [[23]](#ref-23). No
  source read says a scorecard replaces a written readout or sits beside one.
- **No source measured whether writing a readout improves decisions.** The case for the document rests on
  the failure modes the sources name (peeking, cherry-picking, a loss reported as a win) and on keeping a
  record a later reader can audit, not on a controlled comparison. Section 7 below names those failure
  modes; this section says so plainly so a reader does not infer a stronger claim than the research
  supports.
- It ships **lean by default**, eight sections, and the **full** variant adds three more for a test whose
  decision rests on more than its primary metric. Section 4 below covers the split.

**A terminology warning worth having on the first page.** This bundle's nearest-sounding neighbor in
`qa-docs`, the test summary report, never raises its hand to say so. A case-insensitive search of
`templates/test-summary-report/test-summary-report_guide.md` for "experiment," "hypothesis" and "A/B"
returns nothing, so this companion states the boundary from this side alone. `test-plan_guide.md:27`
names the collision from its own family's side, under the heading *Your tool already has a "test plan."*
A test plan and its summary report verify a product increment against an agreed specification and grade
it pass or fail. This document tests an open hypothesis and estimates an effect against a baseline. The
shared word is "test," and section 8 states the full boundary.

## 2. Origins and evolution

The research log carries no single founder and no founding date for the experiment readout. Like its
sibling design document, it is a convention several lineages converged on independently rather than an
artifact with a traceable inventor, and this companion does not guess at one where the log does not supply
it.

**Product experimentation** is the lineage every current field source belongs to. Eppo ships a fillable
"Experiment Report Template" [[1]](#ref-1) and a companion post on writing one well [[2]](#ref-2);
Optimizely publishes both a narrative field list [[3]](#ref-3) and, through Atlassian, a one-page
plan-and-results template [[4]](#ref-4); independent practitioners Tanmayi Sai [[5]](#ref-5) and Adam
Fishman [[6]](#ref-6) each publish a full section order from their own practice; and Amplitude's Bhavik
Patel folds the readout into the fourth phase of a four-phase brief [[7]](#ref-7). None of these sources
dates the convention's origin.

**Academic and clinical trial reporting** reaches a written, standardized post-test report through a much
older and more formal route. CONSORT's 2010 statement is itself a revision: its own text names the
items it added or changed from the prior version, including a new item on "identifying any changes to the
primary and secondary outcome (endpoint) measures after the trial started" [[17]](#ref-17), which is the
same deviations-from-plan discipline this bundle's Context and Setup section borrows. The guideline is
explicit that its own scope stops at the report: "It solely addresses the reporting of what was done and
what was found" [[17]](#ref-17).

**Public-sector evaluation** reaches the same post-test discipline through government accountability
policy. The Magenta Book places "Prepare final evaluation analysis and outputs" inside its own
"Disseminate, use & learning" phase of an evaluation's lifecycle [[19]](#ref-19), and a real applied
instance of the lineage, the Behavioural Insights Team's Pension Wise report, runs a fixed section order
from policy background through headline results to "Conclusion and policy implications" [[20]](#ref-20).

What the product lineage borrows from the other two, and what it deliberately leaves behind, is section 5's
subject. This companion does not attempt a methodology-family history for this document type: the
2026-10-11 research did not look at which named software-delivery frameworks originate or favor this
artifact, and nothing in the log supports a claim about any of them.

## 3. Anatomy (section by section)

The full variant carries eleven body sections; the lean variant carries eight of them, unchanged in name
and order. Three sections, Deep-Dive, Implementation Details and Analysis Notes, and Further Analysis,
are full-variant only.

### Executive Summary (lean)

The decision itself, stated up front, not buried under the evidence that supports it.

Three canon templates open their body with this section, under three different titles: Eppo's "Executive
Summary" [[1]](#ref-1), after its title and author fields; Tanmayi Sai's "TL;DR" [[5]](#ref-5), after its
subject line; and Optimizely's "Purpose" [[3]](#ref-3). Eppo's
own guidance on writing one is to "Decide your reader persona and create a narrative" [[2]](#ref-2), and
Eppo's own filled example puts the decision in the summary itself, not just the Decision section further
down: "This will now be rolled out to all new users" [[1]](#ref-1). A separate account of one team's
practice argues for leading with insight over outcome: a weekly internal newsletter put the test's findings
first and the win-or-loss verdict below it, "the first thing they mentioned was the insights of the tests.
Everything else fell below that, winners and losers included" [[25]](#ref-25).

### Context and Setup (lean)

What ran: the variants, the dates, the population, and anything that ran differently from the plan.

Tanmayi Sai's "Experiment Setup" [[5]](#ref-5) and Optimizely's "Details" field, "Include the number of
variations, a brief description of the differences, the dates when the test was run, the total visitor
count, and the visitor count by variation" [[3]](#ref-3), give this section's core. The section links the
design doc rather than restating it, the same non-duplication principle the design doc's own companion
states against the PRD.

**New in this research: a line for what ran differently from the design doc.** No product source asks for
this explicitly; it is traced instead to the clinical lineage, where CONSORT added "identifying any changes
to the primary and secondary outcome (endpoint) measures after the trial started" as a 2010 addition
[[17]](#ref-17), and to Booking.com's pre-registration practice, where "Experiment owners need to specify
up front which customer behavior they want to impact and how, the set of metrics which is going to support
their hypothesis, and how these metrics are going to change" [[14]](#ref-14) sets the baseline a deviation
is measured against. The clinical origin is named, per the family contract's lineage-labeling requirement.

### Key Results: Primary Metrics (lean, table)

The primary metric's movement against its baseline, stated with its uncertainty.

The table's column shape follows Eppo's own export, read verbatim: "Metric Control Test Change (abs)
Change (rel) CI Sig?" [[1]](#ref-1). Optimizely's narrative version asks for the same content in prose,
"the percentage lift or loss, compared to the original, conversion rates by variation, and the statistical
significance" [[3]](#ref-3). The two change columns, absolute and relative, are corroborated from the
clinical lineage: CONSORT's own 2010 addition recommends that "for binary outcomes, presentation of both
relative and absolute effect sizes is recommended" [[17]](#ref-17). **The interval's confidence level is
stated in the row, never assumed as a field default**; no source read states one level as a convention, and
section 6, item 8 covers why.

### Key Results: Supporting Metrics (lean, table)

Every guardrail's movement, reported against the threshold the design doc fixed.

This is Eppo's own second results section [[1]](#ref-1). A guardrail metric is one source's own definition,
"measure aspects of the product that we don't want to degrade but won't necessarily improve" [[8]](#ref-8),
and a separate vendor's in-tool surface draws the same line between "Decision-making metrics" and
"Guardrail metrics" [[21]](#ref-21). Each row in this table is read against the number the design doc
pre-committed, not re-derived here: that pre-commitment is what makes a breach legible rather than a
judgment call made after the fact.

### Validity Checks (lean)

Whether the result can be trusted at all, checked before it is read as a finding.

**This section's name and scope are this library's own POSITION.** No single source read names one section
with this exact job; it is built by combining several individually sourced checks, the same way the design
doc's own Validity Pre-Commitments section was built. Each check here reads against the pre-commitment the
design doc already made, where one exists:

- **Sample ratio mismatch.** "A sample ratio mismatch is a statistically significant gap between the
  traffic split you configured and the split your experiment produced" [[10]](#ref-10), and it matters
  because such a mismatch "typically invalidate[s] the A/B test and make[s] any results and metric
  movements untrustworthy" [[8]](#ref-8).
- **A mismatch in the metric's own observation units.** A metric movement "can be hard to interpret if the
  number of samples in its computation changes during the experiment," distinct from a user-level SRM and
  checked separately [[9]](#ref-9).
- **A novelty effect, read by date.** "Rapid decline of estimated treatment effect across date segments of
  an A/B test is an indicator of novelty effect" [[8]](#ref-8).
- **Early looks.** Evan Miller's classic warning that an unplanned early stop inflates the reported
  significance level stands behind this row [[12]](#ref-12), and a separate source names "peeking (deciding
  on an experiment before it's completed)" among the statistics mistakes an experimentation program commits
  [[11]](#ref-11).
- **Telemetry changes mid-test.** Named directly as its own check, "Check for any Telemetry-Breaking
  Changes" [[9]](#ref-9).
- **Interaction with other live experiments.** Duolingo's own account of a feature that collided with an
  existing one in the product describes building around the conflict by design: "we knew that this would
  conflict with the existing Friends feature on desktop ... To account for this, the experiment we ran had
  two branches" [[24]](#ref-24); Google's overlapping-infrastructure summary describes the mechanism that
  keeps concurrent experiments independent in the first place [[26]](#ref-26).

### Deep-Dive (full)

The business questions the decision actually depends on, answered one at a time, with exploratory work
kept out.

Eppo's own instruction is to "Structure this as business questions to be answered" [[1]](#ref-1), and
Eppo's own blog states the reason the whole report exists to answer a why, not a what: "Experiment reports
discuss the 'why,' not the 'what'" [[2]](#ref-2). **Only the segments the design doc fixed in advance may
bear on the decision.** The trap this guards against is named directly: "multiple-comparison problems
(adding so many metrics or slicing the data until it shows what you want to see)" [[11]](#ref-11), and the
clinical lineage states the same discipline as a rule rather than a warning, that whenever "subgroup
analysis is displayed, the analysis of the complement subset should also be displayed" [[18]](#ref-18).
Any estimated business impact, stated with its own interval rather than as a bare number, goes here:
Optimizely's "Revenue Impact" field [[3]](#ref-3) and a worked account of exactly that framing, "with a 90%
certainty, the increase in conversion after implementation will be somewhere between 7.5% and 19%"
[[25]](#ref-25).

### Decision: Ship, Iterate or Stop (lean)

The outcome the pre-committed decision rule actually produced, including what a null result does and does
not rule out.

**"Ship, iterate or stop" is this family's own wording for the three-way choice, stated as the
[contract's](../../docs/internal/contracts/experimentation-docs.md) own POSITION in its section 1, not a
phrase any source read here uses verbatim.** The nearest conventions in the sources are Adam Fishman's
pre-committed "ship/no-ship decision" [[6]](#ref-6), Amplitude's "Win Lose Flat" outcomes
[[7]](#ref-7), Tanmayi Sai's "roll out to more users, end, iterate, etc." [[5]](#ref-5), and the
Atlassian/Optimizely template's "inconclusive" or "hypothesis proved" [[4]](#ref-4).

**New in this research: a null result states what it rules out, and what it does not.** Spotify's own
framework counts an adequately powered null as a result in its own right rather than a non-result: "When
all success metrics are neutral and the test is adequately powered, we still classify it as an EwL" and
names the default action, "Iterate, abandon, or ship if infra-only" [[13]](#ref-13). Duolingo's own account
of a shut-down test states the same principle from the opposite direction, that a decision not to ship is
still a finding: "regardless of whether the experiment gets launched or shut down - we learn something new"
[[24]](#ref-24). An ASK on the decision's reversibility is traced to a source outside the experimentation
canon entirely: most decisions "are changeable, reversible - they're two-way doors," and only a smaller set
deserve the slower, more deliberate process a one-way door warrants [[27]](#ref-27).

### Decision Owner (lean)

Who is named as having made the call, as a field rather than a signature buried in prose.

**This section is this library's own POSITION, and it is unsourced.** No source read names a field for the
decision owner. The nearest is Optimizely's "Decision maker" [[3]](#ref-3), which names a role among the
people involved in a test, not a field this document itself carries. Section 6, item 3 covers who decides
in full; this section exists so that whoever that person turns out to be, their name is written down rather
than implied.

### Next Steps and Owners (lean)

The concrete actions the decision requires, each with a named owner.

Eppo's own filled example assigns an owner to the very first next step: "Roll out immediately to 100% of
new users (owner: Ben Nowak)" [[1]](#ref-1). Tanmayi Sai frames the same section more broadly, as "Plan for
this project going forward" [[5]](#ref-5), which is why this section carries not only the immediate rollout
action but anything else the decision implies, each with its own owner.

### Implementation Details and Analysis Notes (full)

The technical detail a future engineer or data scientist would want, kept out of the sections decision
makers actually read.

Eppo's own label for this section states its audience directly: "The geeky stuff goes here - what other
data scientists and engineers would be interested in!" [[1]](#ref-1). The clinical lineage corroborates the
same separation from its own, much stricter side: CONSORT's reporting standard states plainly that "It
solely addresses the reporting of what was done and what was found" [[17]](#ref-17), leaving a results
report's deeper analysis notes outside its own scope by design.

### Further Analysis (full)

Interesting findings that do not bear on the decision, kept clearly separate from the sections that do.

Tanmayi Sai's own section is explicitly optional: "This optional section is where you can include
interesting analysis or insights for readers that are looking for more details on your project"
[[5]](#ref-5). The section is labelled exploratory for a reason stated directly in the clinical lineage:
examine enough subgroups, and a treatment with no real benefit at all "will inevitably appear"
disproportionately beneficial in one or more of them [[18]](#ref-18). Nothing the decision rests on may be
moved here instead of into Deep-Dive.

**Frontmatter, not a section.** The experiment's name, a link to its design doc, the author, the
decision-maker, the test's start and end dates, the decision, and the readout date live in frontmatter
rather than a body section. The link to the design doc is this library's own POSITION, drawn from the
family contract's shared-scenario rule rather than from any source: no source read in this research names a
link field as part of a readout, and the research specifically searched for one.

## 4. Variants and sizing

**Lean (eight sections)** is the default: Executive Summary, Context and Setup, Key Results: Primary
Metrics, Key Results: Supporting Metrics, Validity Checks, Decision, Decision Owner, and Next Steps and
Owners. Eppo's own warning against an overlong report is the direct precedent for keeping the default
short: "You cannot produce ten-page experiment reports, and will have to leave out some interesting
findings. A common strategy is to do your deep-dive work within a notebook or BI report" [[2]](#ref-2).

**Full (eleven sections)** adds Deep-Dive, Implementation Details and Analysis Notes, and Further Analysis.
Tanmayi Sai's own template marks the Further Analysis section optional rather than core [[5]](#ref-5),
which is the direct precedent for treating the same three sections as an addition rather than a default.
The nesting is strict: every lean heading appears in full, in the same name and order.

**How to choose.** A test whose decision rests on more than its primary metric, or whose readers will want
to audit the underlying analysis later, earns the full variant. A test where the eight lean sections already
carry the whole decision does not need the other three.

## 5. Methodology lineage

This document type has one home lineage and borrows deliberately, and by name, from two older ones.

**Product experimentation** is where the convention lives today, across every source in section 2's first
lineage. Within it, the live disagreement is less about structure than about what counts as a result worth
reporting at all: section 6 below, items 2 and 7, cover the learning-versus-winning question in full.

**Clinical and academic trial reporting** contributes the discipline of reporting deviations from a
pre-registered plan, both-sided effect sizes for binary outcomes, and a hard rule against looking at a
subgroup without also showing its complement [[17]](#ref-17)[[18]](#ref-18). This bundle borrows each of
these three pieces by name into Context and Setup, Key Results: Primary Metrics, and Deep-Dive
respectively, and labels each one as a clinical-lineage borrowing rather than presenting it as product
practice, which the family contract requires explicitly.

**Public-sector evaluation** contributes the framing this companion's own honest-framing section leans on:
a final report is valuable for the record it leaves, not necessarily for the decision it changes. The
Magenta Book states this caution about its own genre directly: "a final evaluation report is an important
document in an evaluation study" but "is rarely the best way to ensure impact and influence," because
"front-line delivery staff and ministers will have very different information needs and preferred
communication styles" [[19]](#ref-19). This bundle borrows the caution, not the Magenta Book's own
machinery: its 12-week publication deadline and Open Government Licence apply to that lineage's own
accountability regime, not to this one.

**What the product lineage does not borrow from either older lineage.** Neither CONSORT's item-by-item
checklist discipline nor the Magenta Book's mandatory publication regime is adopted here as a product
practice. A team that wants that level of formal rigor should say so explicitly and read the clinical or
public-sector source directly, rather than infer it from a borrowed sentence in this companion.

## 6. Debates and contested boundaries

Eight questions are not settled by the sources read for this bundle. Each is named here with its camps,
because flattening a live disagreement into a false convention is the dominant way this kind of document
goes wrong.

**1. One document, or two.** Optimizely's own narrative guidance lists the "Experiment plan" and the
results report as separate materials [[3]](#ref-3). An Optimizely template distributed through Atlassian
puts both on one page instead, moving from "2 Set a plan for your experiment" straight through to "3
Outline your results" and "4 Draw conclusions" [[4]](#ref-4); Adam Fishman's document keeps plan and results
in "four distinct parts" of one file [[6]](#ref-6); and Amplitude's brief closes its own four phases with
the decision itself [[7]](#ref-7). Eppo's own template is readout-only [[1]](#ref-1). No source argues
either side is correct. **This library's own contract settles the question for its own purposes, not as a
finding**: it ships two separate bundles, this one and the design doc, following the same precedent
`qa-docs` set with `test-plan` and `test-summary-report`
([contract](../../docs/internal/contracts/experimentation-docs.md), section 1). This bundle's own guide
carries a line for a team that keeps one living document instead.

**2. What a null result is worth.** Spotify's own framework counts a powered null as a result in its own
right, "Neutral but informative" [[13]](#ref-13). A separate account of Netflix's practice describes
shipping on a north-star gain while secondary metrics held, "None of these secondary metrics would decide
an experiment for Netflix" [[15]](#ref-15). These are different acceptance grounds, and no source
reconciles them; this bundle asks the author to state which ground the design doc fixed, rather than
choosing one itself.

**3. Who decides.** Booking.com describes decision rights spread to whoever owns the change, arguing
against "a product organization where only product managers decide what features to test next"
[[14]](#ref-14); a separate account of Netflix's practice puts the check on the story with data scientists,
"the data scientists dive further into the overall metrics to make sure the story hangs together"
[[15]](#ref-15); Optimizely's own field list names a "Decision maker" among the people involved, without
tying the role to a document field [[3]](#ref-3). No source states a split between who writes the readout
and who signs off on it. The Decision Owner section stays this library's own POSITION, per section 3 above.

**4. Guardrails and trade-offs.** Microsoft's own research states the limit of the field's agreement
directly: "There is no standard way to evaluate those tradeoffs" between a primary gain and a guardrail
regression, and describes weights that "should be pre-determined" rather than argued over after the fact
[[9]](#ref-9). A separate in-tool surface alerts on guardrail thresholds automatically [[21]](#ref-21). A
pre-committed breach rule is one form of a pre-determined trade-off; no source states that a guardrail
breach blocks shipping as a universal rule.

**5. Tags in an archive.** Booking.com reports that labelling experiments with tags "is proving not
sustainable" at its own scale, and groups its archive instead "by teams, areas of the Booking.com products
they ran on, segments of visitors they targeted" [[14]](#ref-14). This bundle adds no tags field for that
reason; its frontmatter carries the fields that group instead.

**6. Automated stops.** Booking.com states a deliberate choice against automating a harmful-experiment stop
even though the mechanism exists: "we could easily automate such stops. However, we feel this goes contrary
to democratizing experimentation which fosters end to end ownership" [[14]](#ref-14). A separate vendor's
surface automates guardrail alerts and ends them after a fixed window instead [[21]](#ref-21). This is a
program-level policy choice, not a readout section, and this companion mentions it only; the template does
not take a side.

**7. Time-bound figures and vendor claims.** Spotify's own learning and win rates, "the learning rate is
~64%, but the win rate is ~12%," are measured figures for two of its own organizations in 2025
[[13]](#ref-13), not a field-wide norm. A vendor's own alerting behavior, "Guardrail alerts stop running 30
days after the experiment starts," is product behavior that can change without notice [[21]](#ref-21). None
of these figures is presented here as a convention.

**8. No significance level is a convention.** No source read for this bundle states one significance level,
power level or minimum duration as a field-wide standard. A separate account of Netflix's practice reports
that "many decisions are made at the 95% confidence level" [[15]](#ref-15), which is stated as Netflix's own
practice, not a cross-industry default. The Key Results table states whichever level the design doc or the
platform actually used, in the row, rather than assuming one.

## 7. Anti-patterns and failure modes

**Naming the early-lift decay pattern a "primacy effect."** No source read for this research uses that
term. The pattern this bundle actually sources, a lift that falls across date segments, is named
differently and more precisely: Microsoft's own research calls it a novelty effect, detected by segmenting
"every A/B test analysis by date" [[8]](#ref-8). Fix: use novelty effect, sourced to [[8]](#ref-8), and do
not borrow a term no source in this bundle's log uses.

**Presenting "ship, iterate or stop," or the catalog's "ship/iterate/kill," as a sourced field
convention.** It is this family's own wording, stated as the contract's POSITION in section 1 above. Fix:
state it as this library's own choice, as the Decision section of the anatomy above does, rather than
attributing it to the sources.

**Presenting a significance level, power level, or test duration as a field-wide convention.** The only
specific figure in the sources, 95 percent confidence, is one company's own reported practice, not a norm
[[15]](#ref-15). Fix: state whichever level the design doc or the platform actually used, and do not
present a borrowed number as a default.

**Treating a null result as proof of no effect.** A null on a test powered to detect a large effect says
nothing about a smaller one; the interval around a null point estimate, not the point estimate alone, is
what tells a reader how small an effect the test could still be hiding. Fix: state what the null rules out
and what it does not, as the Decision section above requires.

**Treating a guardrail breach as a universal block on shipping.** Microsoft's own research states plainly
that "there is no standard way to evaluate" the trade-off between a primary gain and a guardrail regression
[[9]](#ref-9). Fix: report the guardrail's movement against the design doc's own pre-committed threshold,
and let the pre-committed decision rule, not a blanket policy, decide what the breach means.

**Claiming that tags make an experiment archive findable.** Booking.com reports the opposite of its own
practice, that tagging "is proving not sustainable" at scale [[14]](#ref-14). Fix: rely on the frontmatter
fields that already group a readout, the experiment's name and its design-doc link, rather than adding a
tags field this bundle has no source for.

**Borrowing a clinical or public-sector element and presenting it as product-management practice.** The
deviations-from-plan line, the both-sided effect-size columns, and the complement-subgroup rule in sections
3 and 5 above each come from a clinical trial-reporting standard [[17]](#ref-17)[[18]](#ref-18), not from
any product source. Fix: name the lineage each time, as the anatomy above does, rather than letting a
clinical convention read as settled product practice.

**Treating a vendor's in-tool scorecard or export as a substitute for, or a companion to, this written
document.** Optimizely's scorecard is a live, configurable surface built from modules
[[21]](#ref-21); Statsig's export is a one-time PDF with no decision field [[22]](#ref-22). None of these
sources claims its surface replaces or sits alongside a written readout. Fix: use the in-tool surface for
what it is built for, live monitoring and raw metric export, and keep the decision and its rationale in
this document.

## 8. Relationships to other artifacts

**The other family member.** Per the
[contract](../../docs/internal/contracts/experimentation-docs.md), the
[experiment-design-doc](../experiment-design-doc/experiment-design-doc_companion.md) states the plan,
hypothesis, allocation, sample size and decision rule before the test launches; this document reports
against that exact plan after the test ends, with the same hypothesis, metrics and decision rule
(contract, section 4). A readout that invents a different hypothesis, metric, or decision rule from the one
its design doc fixed is out of contract even if every section is filled.

**The spike report (`decision-docs`).** The family contract requires stating this boundary by name. A
spike report's own companion describes a spike as answering one specific technical question fast, and
states of a spike that fails to confirm its premise, "A refuted hypothesis is a successful spike"
(`templates/spike-report/spike-report_companion.md:188`). The vocabulary overlaps, both documents use
"hypothesis," but a spike carries no control group, no allocation between variants, and no statistical
decision rule. This document reports on an open hypothesis tested against a baseline with a pre-committed
decision rule.

**The test plan and test summary report (`qa-docs`).** Also a required boundary statement, stated here
from this bundle's own side because its nearest neighbor does not state it from its own: a case-insensitive
search of `templates/test-summary-report/test-summary-report_guide.md` for "experiment," "hypothesis" and
"A/B" returns nothing. `qa-docs`'s own test-plan guide names the collision from its side, under the heading
*Your tool already has a "test plan"* (`templates/test-plan/test-plan_guide.md:27`). A test plan and its
summary report verify a product increment against an agreed specification and grade it pass or fail.
Neither carries a hypothesis, an allocation between variants, or a statistical decision rule. This document
estimates an effect against a baseline and reports a ship, iterate or stop decision rather than a pass or
fail grade.

**Standing measurement instruments.** A tracking plan, a KPI dashboard, or an OKR scorecard is maintained
across many tests and is never finished the way a single test's readout is. The
[contract](../../docs/internal/contracts/experimentation-docs.md) excludes this category from the family by
name; the tracking plan specifically joins `governance-docs` instead, by
[ADR 0067](../../docs/internal/decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md).
This bundle's own worked example draws its primary metric's baseline from this library's own KPI dashboard
rather than inventing one, and its Next Steps section marks a tracking-plan field for retirement rather than
restating the tracking plan itself.

**In-tool experiment surfaces.** Optimizely's Experiment Scorecard [[21]](#ref-21), Statsig's Experiment
Summary PDF export [[22]](#ref-22), and Microsoft's own framing of a scorecard as "a collection of metrics
used to evaluate the success of a product change or experiment" [[23]](#ref-23) are live, tool-native
surfaces, not narrative documents. None of these sources claims its surface replaces or sits beside a
written readout; the boundary that keeps this document out of their territory, and them out of this
document's, is this library's own, under
[ADR 0030](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md).

**Pre-build validation and other validation methods.** A test run before anything is built, to decide
whether to build it at all, is excluded from this family by the contract's own second boundary sentence
([contract](../../docs/internal/contracts/experimentation-docs.md), section 1). A separate source argues
more broadly that controlled experiments are not the only validation method and that "many companies set
the bar too high" by defaulting to them [[16]](#ref-16); that source says nothing about this document, its
archive, or its authorship, and this companion draws nothing further from it than the boundary point itself.

## 9. Adaptations

**Lean versus full.** Section 4 above covers the sizing signal in full: a test whose decision rests on more
than its primary metric, or whose readers will audit the analysis later, earns the full variant.

**Regulated or high-stakes tests.** A team operating under clinical-trial-grade or public-sector-grade
reporting obligations should read CONSORT [[17]](#ref-17), the EMA subgroup guideline [[18]](#ref-18), or
the Magenta Book [[19]](#ref-19) directly rather than inferring their formal requirements from this
companion's borrowed sentences. This bundle adopts their reporting discipline, not their governance
machinery.

**One-living-document teams.** Section 6, item 1 covers the live disagreement over whether a plan and its
results belong in one document. This bundle still works for a team that prefers one document: its sections
are that document's second half, and the guide, not this companion, walks through how to use it that way.

**What may be adapted, and under what terms.** CONSORT is "an open-access article distributed under the
terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and
reproduction in any medium, provided the original author and source are credited" [[17]](#ref-17); the EMA
guideline states that "Reproduction is authorised provided the source is acknowledged" [[18]](#ref-18); and
the Magenta Book "is licensed under the terms of the Open Government Licence v3.0 except where otherwise
stated" [[19]](#ref-19). None of the product sources ([[1]](#ref-1) through [[7]](#ref-7),
[[21]](#ref-21), [[22]](#ref-22)) states a content licence on the page read, and this bundle adapts no
vendor's template text; it names sections after the shared canon instead.

## 10. Worked example

[`experiment-readout_example.md`](experiment-readout_example.md) will be the readout of the Saved Views
adoption-nudge experiment at Acme Analytics, dated 2026-09-04, reporting the exact test that
[`experiment-design-doc_example.md`](../experiment-design-doc/experiment-design-doc_example.md) planned,
with the same hypothesis, metrics and decision rule.

Two things in it are worth studying past the shape of a filled template. **Its recommended outcome is a
null, with the point estimate finishing above control**, chosen specifically because it exercises every
commitment the design doc made: the daily sample-ratio check, the week-by-week novelty read, the guardrail
thresholds, and the decision rule's own null branch, rather than its easier win branch. **It states, in its
own words, where the design doc's failure condition and its decision rule disagree on this exact outcome.**
Treatment finished above control, so the hypothesis did not "fail" in the design doc's own wording, but the
difference was not statistically significant, so the pre-registered decision rule reads it as a null. The
readout states that the decision rule governs because it was the pre-registered commitment, and records the
mismatch as a lesson for the next design doc rather than quietly resolving it in prose.

---

## References

<a id="ref-1"></a>[1] Eppo. "[Experiment Report Template (Example)](https://docs.google.com/document/d/1mWWzaAdTfuQWGp2tHE5NVN6pL-Tx0_JTKlDLZOcmUqw/export?format=txt)." Google Doc export (accessed 2026-10-11). Supports the full section and field order, the Key Results table's column shape, a decision stated in prose rather than a labeled field, and per-item next-steps owners ("Metric Control Test Change (abs) Change (rel) CI Sig?"; "This will now be rolled out to all new users."). [vendor]

<a id="ref-2"></a>[2] Ryan Lucht (Eppo blog). "[How to Craft Compelling, Impactful Experiment Reports](https://www.geteppo.com/blog/how-to-craft-compelling-impactful-experiment-reports)." Eppo blog (accessed 2026-10-11). Supports writing early, the why-not-what framing, and a short main report with deep-dive work kept in a separate notebook ("Experiment reports discuss the 'why,' not the 'what.'"; "You cannot produce ten-page experiment reports, and will have to leave out some interesting findings."). [vendor]

<a id="ref-3"></a>[3] Optimizely docs. "[Share your results with stakeholders](https://docs.optimizely.com/experimentation-strategy/docs/share-your-results-with-stakeholders)." Optimizely Experimentation Strategy documentation (accessed 2026-10-11). Supports the five-field core (Purpose, Details, Results, Lessons Learned, Revenue Impact), the plan-versus-results-report separation, and the "Decision maker" role ("Purpose - Briefly describe 'why' you are running this test, including your experiment hypothesis."). [vendor]

<a id="ref-4"></a>[4] Optimizely (via Atlassian Confluence). "[Experiment plan and results template](https://www.atlassian.com/software/confluence/templates/experiment-plan-and-results)." Atlassian Confluence templates (accessed 2026-10-11). Supports a one-page plan-plus-results structure and "inconclusive"/"hypothesis proved" as recorded conclusions ("3 Outline your results"; "assign a clear conclusion (such as 'inconclusive' or 'hypothesis proved')"). [vendor]

<a id="ref-5"></a>[5] Tanmayi Sai. "[Experiment Readout Template](https://tanmayisai.com/2020/11/20/experiment-readout-template/)." tanmayisai.com (accessed 2026-10-11). Supports the full section order for one merged readout document, the optional Further Analysis section as lean-versus-full evidence, and the "Plan for this project going forward" framing ("This optional section is where you can include interesting analysis or insights for readers that are looking for more details on your project"). [practitioner]

<a id="ref-6"></a>[6] Adam Fishman. "[Creating an Experiment Doc](https://www.fishmanafnewsletter.com/p/experiment-document-template)." Fishman AF Newsletter (accessed 2026-10-11). Supports the Results section's analysis questions and the pre-committed ship/no-ship decision rule ("Articulating this ship/no-ship decision in advance helps drive alignment."). [practitioner]

<a id="ref-7"></a>[7] Bhavik Patel (Amplitude blog). "[Use experiment briefs to design better experiments](https://amplitude.com/blog/experiment-brief)." Amplitude blog (accessed 2026-10-11). Supports the fourth-phase "Analyze and Decide" fields and the Win/Lose/Flat decision outcomes ("Actions: What actions will you take based on each of the following outcomes of the test? Win Lose Flat"). [vendor]

<a id="ref-8"></a>[8] Widad Machmouchi, Somit Gupta, Ruhan Zhang (Microsoft Experimentation Platform). "[Patterns of Trustworthy Experimentation: During-Experiment Stage](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/)." Microsoft Research (published January 25, 2021; accessed 2026-10-11). Supports the guardrail-metric definition, sample-ratio-mismatch consequence, and date-segmented novelty-effect detection ("SRMs typically invalidate the A/B test and make any results and metric movements untrustworthy."; "Rapid decline of estimated treatment effect across date segments of an A/B test is an indicator of novelty effect."). [primary]

<a id="ref-9"></a>[9] Widad Machmouchi, Somit Gupta (Microsoft Experimentation Platform). "[Patterns of Trustworthy Experimentation: Post-Experiment Stage](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-post-experiment-stage/)." Microsoft Research (published December 24, 2021; accessed 2026-10-11). Supports metric-observation-unit imbalance checks, telemetry-breaking-change checks, and the lack of a standard rule for trading off a primary gain against a guardrail regression ("Check for any Telemetry-Breaking Changes"; "There is no standard way to evaluate those tradeoffs."). [primary]

<a id="ref-10"></a>[10] Casandra Campbell (GrowthBook Blog). "[Sample ratio mismatch (SRM): how to identify the root cause and decide whether to restart your experiment](https://www.growthbook.io/blog/sample-ratio-mismatch)." GrowthBook Blog (Aug 7, 2026; accessed 2026-10-11). Supports the SRM definition and its detection mechanism ("A sample ratio mismatch is a statistically significant gap between the traffic split you configured and the split your experiment produced."). [vendor]

<a id="ref-11"></a>[11] Graham McNicoll (GrowthBook Blog). "[9 common experimentation program mistakes to avoid](https://www.growthbook.io/blog/experimentation-program-mistakes-to-avoid)." GrowthBook Blog (Sep 6, 2024; accessed 2026-10-11). Supports peeking and multiple-comparison fishing as named statistics mistakes ("peeking (deciding on an experiment before it's completed), multiple-comparison problems (adding so many metrics or slicing the data until it shows what you want to see)"). [vendor]

<a id="ref-12"></a>[12] Evan Miller. "[How Not To Run an A/B Test](https://www.evanmiller.org/how-not-to-run-an-ab-test.html)." evanmiller.org (April 18, 2010; accessed 2026-10-11). Supports repeated significance testing (peeking) as a trap that invalidates reported significance, and the instruction not to report significance until the test is over ("Don't report significance levels until an experiment is over, and stop using significance levels to decide whether an experiment should stop or continue."). [practitioner]

<a id="ref-13"></a>[13] Michael Bellato, Mårten Schultzberg, Sebastian Ankargren (Spotify Data Science). "[Beyond Winning: Spotify's Experiments with Learning Framework](https://engineering.atspotify.com/2025/9/spotifys-experiments-with-learning-framework)." Spotify Engineering (2025; accessed 2026-10-11). Supports an adequately powered null treated as a result in its own right, with its own default action, and Spotify's own 2025 learning-rate and win-rate figures as Spotify's own figures, not a field norm ("When all success metrics are neutral and the test is adequately powered, we still classify it as an EwL."; "Neutral but informative: No effect but the test was strong enough to detect one if it existed -> Iterate, abandon, or ship if infra-only."). [practitioner]

<a id="ref-14"></a>[14] Raphael Lopez Kaufman, Jegar Pitchforth, Lukas Vermeer (Booking.com). "[Democratizing online controlled experiments at Booking.com](https://ar5iv.labs.arxiv.org/html/1710.08217)." arXiv:1710.08217, read at its ar5iv HTML rendering (accessed 2026-10-11). Supports decision rights spread to experiment owners, pre-registration of hypothesis and metrics, tags as an unsustainable archive mechanism, and the deliberate choice not to automate harmful-experiment stops ("Experiment owners need to specify up front which customer behavior they want to impact and how, the set of metrics which is going to support their hypothesis, and how these metrics are going to change."; "this approach is proving not sustainable both because it involves making sure the tags are normalized and kept up to date and because it entails poor discoverability and usability of the central repository."; "we could easily automate such stops. However, we feel this goes contrary to democratizing experimentation which fosters end to end ownership"). [primary]

<a id="ref-15"></a>[15] Aakash Gupta (with Bandan, Booking.com/Gojek product leader). "[Netflix: Lessons in Experimentation](https://www.aakashg.com/netflix-experimentation/)." aakashg.com (accessed 2026-10-11). Supports secondary-metric guardrails versus a single north-star metric as the basis for a ship decision, and Netflix's own reported confidence-level practice ("Although north star metrics help, many decisions are made at the 95% confidence level."; "None of these secondary metrics would decide an experiment for Netflix"). [practitioner]

<a id="ref-16"></a>[16] Itamar Gilad. "[Idea Validation Using the AFTER Model](https://itamargilad.com/idea-validation-much-more-than-just-a-b-experiments/)." itamargilad.com (accessed 2026-10-11). Supports a boundary finding only, that controlled experiments are not the only or default validation method; it says nothing about the readout document, its archive, or its authorship ("While experiments are the gold standard, of validation, there are many other, far cheaper and more immediate ways to test an idea."). [practitioner]

<a id="ref-17"></a>[17] Kenneth F. Schulz, Douglas G. Altman, David Moher, for the CONSORT Group. "[CONSORT 2010 Statement: Updated Guidelines for Reporting Parallel Group Randomised Trials](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000251)." PLoS Medicine (24 March 2010; accessed 2026-10-11). Supports the deviations-from-plan item added to this revision, the both-sided effect-size recommendation for binary outcomes, the statement that the guideline addresses reporting only, and its Creative Commons licence ("We added a sub-item on identifying any changes to the primary and secondary outcome (endpoint) measures after the trial started."; "For appropriate clinical interpretability, prevailing experience suggested the addition of 'For binary outcomes, presentation of both relative and absolute effect sizes is recommended.'"; "It solely addresses the reporting of what was done and what was found."). A clinical-trial lineage source; any element borrowed from it is labelled as such in this companion. [primary]

<a id="ref-18"></a>[18] European Medicines Agency, Committee for Medicinal Products for Human Use. "[Guideline on the investigation of subgroups in confirmatory clinical trials](https://www.ema.europa.eu/en/documents/scientific-guideline/draft-guideline-investigation-subgroups-confirmatory-clinical-trials_en.pdf)." EMA/CHMP/539146/2013, draft dated 23 January 2014 (accessed 2026-10-11). Supports the complement-subgroup display rule and the caution that enough subgroups will inevitably surface an apparently beneficial one even with no real effect ("subgroup analysis is displayed, the analysis of the complement subset should also be displayed."; "if a large number of subgroups are examined it will inevitably appear disproportionately beneficial in one or more subgroups."). A clinical-trial lineage source; any element borrowed from it is labelled as such in this companion. [primary]

<a id="ref-19"></a>[19] HM Treasury. "[The Magenta Book: Central Government Guidance on Evaluation](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html)." HTML edition, cited text dated May 2026 (accessed 2026-10-11). Supports the final-report stage of an evaluation's lifecycle, the caution that a final report is rarely the best way to ensure impact and influence, and the Open Government Licence ("While a final evaluation report is an important document in an evaluation study, it is rarely the best way to ensure impact and influence."; "This publication is licensed under the terms of the Open Government Licence v3.0 except where otherwise stated."). A public-sector lineage source; any element borrowed from it is labelled as such in this companion. [primary]

<a id="ref-20"></a>[20] Kate Glazebrook, Chris Larkin, Elisabeth Costa (Behavioural Insights Team). "[Improving engagement with pension decisions: The results from three randomised controlled trials](https://www.bi.team/wp-content/uploads/2017/10/Pension-wise-trials.pdf)." Report prepared for the UK Government's Pension Wise service (October 2017; accessed 2026-10-11). Supports an applied public-sector readout's section order and its policy-implications conclusion ("6. Conclusion and policy implications"). [practitioner]

<a id="ref-21"></a>[21] Optimizely docs. "[Understand your Experiment Scorecard](https://docs.optimizely.com/analytics/docs/understand-your-experiment-scorecard)." Optimizely Analytics documentation (accessed 2026-10-11). Supports the in-tool scorecard as a live, configurable, module-built surface, the decision-making-versus-guardrail metric split, and automated guardrail alerting on a fixed window ("An Experiment Scorecard template consists of the following modules:"; "Guardrail alerts stop running 30 days after the experiment starts."). [vendor]

<a id="ref-22"></a>[22] Statsig. "[Experiment Summary PDF](https://www.statsig.com/updates/update/experiment-summary-pdf)." Statsig Product Updates (accessed 2026-10-11). Supports a one-time results export with setup facts and raw metric stats, and the vendor's own statement that free-form decision-maker commentary is a future feature, not a shipped one, as of the post's 10/9/2023 date ("Your PDF summary will contain- Key Setup Information ... Results Overview, such as a snapshot of your experiment's Pulse results ... and granular metric-by-metric raw stats"; "In the future, we'll also be adding a surface for experiment decision-makers to add more free-form recap text"). [vendor]

<a id="ref-23"></a>[23] Kai Qi, Momo Meng (Microsoft Experimentation Platform). "[Treatment Effect Assessment at Scale: Accounting for Correlated Metrics and Metric Relevance in Modern Experimentation](https://www.microsoft.com/en-us/research/articles/treatment-effect-assessment-at-scale-accounting-for-correlated-metrics-and-metric-relevance-in-modern-experimentation/)." Microsoft Research articles (accessed 2026-10-11). Supports a scorecard's own definition and the limit of automated evaluation without human interpretation ("A scorecard is a collection of metrics used to evaluate the success of a product change or experiment."; "Does that mean experiment evaluation can now be automated based on metric movements and a TEA p-value? Not quite."). [practitioner]

<a id="ref-24"></a>[24] Lavanya Aprameya (Duolingo Engineering Blog). "[Improving Duolingo, one experiment at a time](https://blog.duolingo.com/improving-duolingo-one-experiment-at-a-time/)." Duolingo Engineering Blog (accessed 2026-10-11). Supports treating a shut-down test as a finding in its own right, and designing a readout's analysis around a known concurrent experiment ("with each experiment report - regardless of whether the experiment gets launched or shut down - we learn something new about our learners and our app"; "we knew that this would conflict with the existing Friends feature on desktop ... the experiment we ran had two branches"). [practitioner]

<a id="ref-25"></a>[25] Alex Birkett (CXL). "[How To Communicate A/B Test Results To Stakeholders](https://cxl.com/blog/how-to-communicate-ab-test-results/)." CXL (accessed 2026-10-11). Supports a quantified-impact framing with a stated confidence interval, and the practice of leading an internal readership with insight rather than a win/loss label ("with a 90% certainty, the increase in conversion after implementation will be somewhere between 7.5% and 19%"; "the first thing they mentioned was the insights of the tests. Everything else fell below that, winners and losers included."). [practitioner]

<a id="ref-26"></a>[26] Google Research Blog. "[Overlapping Experiment Infrastructure: More, Better, Faster Experimentation](https://research.google/blog/overlapping-experiment-infrastructure-more-better-faster-experimentation/)." Google Research (summarizing Tang, Agarwal, O'Brien and Meyer, KDD 2010; accessed 2026-10-11). Supports the mechanism by which concurrently running experiments are kept statistically independent ("Google's infrastructure supports this vast experimentation by using orthogonal diversion criteria for experiments in different 'layers' so that each event ... can be assigned to multiple experiments."). [primary]

<a id="ref-27"></a>[27] Farnam Street. "[Reversible and Irreversible Decisions](https://fs.blog/reversible-irreversible-decisions/)." fs.blog, quoting Jeff Bezos's Amazon shareholder letter (accessed 2026-10-11). Supports naming a launch decision's reversibility explicitly, and the link between over-applying irreversible-decision rigor and under-experimenting ("most decisions aren't like that - they are changeable, reversible - they're two-way doors."; "The end result of this is slowness, unthoughtful risk aversion, failure to experiment sufficiently, and consequently diminished invention."). [practitioner]
