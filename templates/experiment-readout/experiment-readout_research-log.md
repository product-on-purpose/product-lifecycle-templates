# experiment-readout: research log

Research conducted 2026-10-11, building on the admission sweep of 2026-10-05 and the spec research of 2026-10-06
that the [experiment-design-doc research log](../experiment-design-doc/experiment-design-doc_research-log.md) also
draws on. The build's six-dimension fan-out covered the product-experimentation canon, contested practice (learning,
archives and who decides), the boundaries with this library's neighbours and the worked example's commitments,
reporting honestly (validity checks, uncertainty and the named traps), the two non-product lineages, and the standing
gap question. **28 sources are recorded below, all fetched-and-verified.** Only `fetched-and-verified` sources are
quoted anywhere in this bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a retrieval tool
returns. The agents returned 198 quotations. 177 passed as normalized substrings, and 6 more pass once a rendering
artifact is removed. Of the other 15, two were table rows an agent had joined with pipes; each cell was checked on its
own and is quoted separately below. One passes with whitespace ignored. The remaining 12 failed for reasons this
section names below, and each is either quoted below in the verbatim parts that pass or dropped. Every page first
cached during this build was fetched a second time with the cache bypassed: 54 quotations on 8 pages were re-checked
that way, 40 pass, and the 14 that do not are explained below. Dashes inside quotations are written as hyphens, as the
house rule requires.

---

## What the checks caught, and what was not read

**Eppo's metric columns are now read verbatim.** The spec recorded the column set under "Key Results: Primary Metrics"
as not independently raw-checked. [1]'s raw export carries it as one header row: "Metric Control Test Change (abs)
Change (rel) CI Sig?". The same columns repeat under "Key Results: Supporting Metrics".

**Eppo puts Next Steps before the results.** [1]'s sections run "Experiment Title", "Author & Team", "Executive
Summary", "Next Steps", then the two Key Results sections, "Deep-Dive" and "Implementation Details and Analysis Notes".
The spec's section order puts the decision and next steps after the results. Both orders are defensible: [1] leads
with what happens next, and the spec leads with the evidence. The companion should name the choice.

**One agent misattributed the Booking.com paper.** A dimension returned it as written by "Pavel Dmitriev et al.". The
paper's own author block names Raphael Lopez Kaufman, Jegar Pitchforth and Lukas Vermeer, and [14] carries those names.

**The arXiv abstract page's cache held the full paper.** One agent stored the paper's HTML rendering under the
`arxiv.org/abs/` address. A fresh fetch of that address returns the abstract only, so seven quotations failed the
second check. All seven pass against the ar5iv rendering, which [14] cites instead. An eighth quotation, read from a
second ar5iv mirror, sat across a citation marker ("p-hacking [10] and dubious decisions") and survives as the words
before the marker.

**The EMA guideline's PDF interleaves line numbers.** [18]'s text layer prints a line number at every line break, inside
sentences. Five quotations failed both checks for that reason. Each is quoted below in the parts that sit between the
numbers. [18] is also a 2014 draft, and it is a clinical-trial source, so the bundle labels anything it borrows as
clinical lineage.

**Five more failures were rendering, not wording.** [3]'s page carries a zero-width character inside its "Results
report" line, which is quoted in two parts. [19]'s publication-protocol sentence carries a footnote marker, and its
copyright line runs straight into the licence sentence; both are quoted in their parts. [17]'s item 24 failed on the
dash after its label and survives as the sentence after the label. [15]'s list of secondary metrics was joined into one
string and survives as its lead sentence. Separately, one quotation from Duolingo's post ([24]) failed both checks at
the address without a trailing slash; it passes at the address with one, which [24] cites.

**The spec's "machine-generated table" is not Microsoft's wording.** The spec describes Microsoft's scorecard as a
machine-generated table inside the experimentation platform, in the spec's own words. [23] never uses that phrase. Its
own sentence is quoted instead: "A scorecard is a collection of metrics used to evaluate the success of a product
change or experiment."

**CONSORT's checklist table did not render.** [17]'s copy carries the checklist's caption, its section names in prose,
and a "Changes in CONSORT 2010" passage naming items by number. The item-by-item table body did not survive extraction.
The spec's three section names pass against this copy. Nothing in this bundle quotes a checklist row that was not read.

**test-summary-report states no boundary from its own side.** A case-insensitive search of
`templates/test-summary-report/test-summary-report_guide.md` for "experiment", "hypothesis" and "A/B" returns nothing.
`test-plan_guide.md:27` names its collision under the heading *Your tool already has a "test plan"*. The readout's
companion states the distinction with test-summary-report on this bundle's side alone.

**What was not read.** The CONSORT 2010 Explanation and Elaboration paper, where the item-by-item guidance lives. Three
vendor pages on reporting a holdout group (Eppo, Statsig and GrowthBook), seen only as search summaries. Airbnb's 2014
post on its experiment reporting framework, which returned HTTP 403 to both a fetch and a direct request and is cited
nowhere. The Magenta Book's PDF edition, confirmed as the same text as [19] and not quoted. Whether Statsig ever shipped
the free-form recap surface [22] announced in 2023 is unknown, and nothing here depends on it.

---

## The admission record

**The spec's admission stands, and this research adds nothing that disturbs it.**
[ADR 0030](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md)'s test needs one named source that
publishes the type as a written document. [1] is a fillable readout template. [3] prescribes a written results summary:
"Purpose", "Details", "Results", "Lessons Learned" and "Revenue Impact". [17] is a standards-grade reporting checklist,
[20] is a published trial report, and [19] requires "publishing all evaluation reports". [5] is one practitioner's
"Experiment Readout Template" and corroborates the others. The five qualifying sources span three lineages, as the
spec records.

**The family is `experimentation-docs`, `phase: measure`, by
[ADR 0066](../../docs/internal/decisions/0066-adopt-experimentation-docs-family-contract.md).** Nothing read here
contradicts it. The contract's section 1 says a readout reports "the decision the results drove (ship, iterate or
stop), **after** the test ends", and every product source places the readout after the test: [3] says to "Share
results with the rest of your organization at the end of each test", and [7]'s fourth phase is "Phase 4: Analyze and
Decide".

**Scope: the written readout is in scope, the scorecard and the export are not.** [21] describes a live, configurable
in-tool surface: "An Experiment Scorecard template consists of the following modules:". [22] is a one-time export whose
contents are setup facts and "granular metric-by-metric raw stats", with no decision field. [23] answers its own
question about automating evaluation with "Not quite.", because "the experimentation platform typically has limited
context about the experiment itself." That is the clearest statement read that a results surface and a decision-bearing
document answer different questions. No source says a scorecard replaces a written readout or sits beside one.

**Licences decide what this bundle may adapt.** [17] is open access under a Creative Commons Attribution licence. [19]
is "licensed under the terms of the Open Government Licence v3.0 except where otherwise stated." [18] states
"Reproduction is authorised provided the source is acknowledged." None of the product sources ([1] to [7], [21], [22])
states a content licence, and [20] carries only a bare copyright notice. The bundle names sections after the canon and
adapts no vendor's template text.

---

## Claims flagged contested or time-bound

1. **One document or two.** [3] lists the "Experiment plan" and the results report as separate materials. [4], an
   Optimizely template distributed through Confluence, puts both on one page ("2 Set a plan for your experiment", "3
   Outline your results", "4 Draw conclusions"). [6] keeps plan and results in one document with "four distinct parts",
   and [7] closes its brief with the decision phase. [1] is readout-only. The maintainer ruled for two bundles in
   ADR 0066. The guide carries the spec's line for teams that keep one living document.
2. **What a null result is worth.** [13] counts a powered null as a result in its own right ("When all success metrics
   are neutral and the test is adequately powered, we still classify it as an EwL."). [15] describes Netflix shipping
   on a north-star gain while secondary metrics held ("None of these secondary metrics would decide an experiment for
   Netflix"). These are different acceptance grounds, and no source reconciles them. The bundle asks the author to
   state which ground the design doc fixed, and does not choose one.
3. **Who decides.** [14] describes decision rights spread to whoever owns the experiment, and argues against "a product
   organization where only product managers decide what features to test next." [15] gives the check on the story to
   data scientists ("the data scientists dive further into the overall metrics to make sure the story hangs
   together"). [3] lists a "Decision maker" among the people involved without tying the role to a field. No source
   states a split between who writes the readout and who signs off. The Decision Owner section stays the library's
   POSITION, as the spec records.
4. **Guardrails and trade-offs.** [9] says of a primary gain alongside a guardrail regression: "There is no standard
   way to evaluate those tradeoffs." It describes weights that "should be pre-determined". [21] alerts on guardrail
   thresholds. A pre-committed breach rule, like the one the worked example's design doc carries, is one form of a
   pre-determined trade-off. No source says a guardrail breach blocks shipping as a universal rule.
5. **Tags in an archive.** [14] reports that labelling experiments with tags "is proving not sustainable", and groups
   its archive instead "by teams, areas of the Booking.com products they ran on, segments of visitors they targeted".
   The bundle adds no tags field.
6. **Automated stops.** [14] says "we could easily automate such stops. However, we feel this goes contrary to
   democratizing experimentation which fosters end to end ownership". [21] automates guardrail alerts and ends them
   after a set period. This is a program-level choice, not a readout section; the companion mentions it only.
7. **Time-bound figures and vendor claims.** [13]'s rates ("the learning rate is ~64%, but the win rate is ~12%") are
   Spotify's, measured in two of its organizations in 2025. [21]'s "Guardrail alerts stop running 30 days after the
   experiment starts." is product behaviour that can change. [12]'s "Try 26.1%" is a worked example of repeated
   testing, not a measured rate. [10] is dated 2026; [8] and [9] are from 2021.
8. **No significance level is a convention.** No source read states one significance level, power level or minimum
   duration as a field-wide standard. [8] says only that early looks need stronger significance levels, without a
   number. [15] reports that at Netflix "many decisions are made at the 95% confidence level", which is Netflix's
   practice. The template asks the author to state the level the design doc fixed.

---

## Notes for the companion

### Honest framing

A readout reports one concluded test: what ran, the results with their uncertainty, whether the results can be
trusted, and the decision they drove, with its owner. [3] gives the core in five fields, and [1] gives a fillable
shape. The two non-product lineages ask for more: [17] asks trial reports to state "any changes to the primary and
secondary outcome (endpoint) measures after the trial started", and [19] asks for "communicating the uncertainty
around findings".

**No source measured whether writing a readout improves decisions.** [13]'s figures measure how Spotify classifies its
experiments, not whether a written report changed anything. [19] warns that a final report "is rarely the best way to
ensure impact and influence". The companion says the case for the document rests on the failure modes the sources name
(peeking, cherry-picking, a loss reported as a win) and on keeping a record a later reader can audit, not on a
measurement.

**The sources disagree less than they look.** The product sources agree on a summary, the setup, the primary result,
the supporting metrics and a next step. They differ on where the decision sits, whether plan and readout share a page,
and who decides. The companion presents those as choices, with the evidence for each.

### The evidentiary spine, section by section

The research keeps the spec's eleven sections and changes what three of them ask for. Context and Setup gains a line
for deviations from the design doc. Deep-Dive is limited to the questions the decision depends on, with exploratory
analysis moved to Further Analysis. Decision gains what a null result rules out and what it does not.

- **Executive Summary** (lean). [1]'s "Executive Summary", [5]'s "TL;DR" and [3]'s "Purpose". [2]: "Decide your reader
  persona and create a narrative." [1] states the decision in the summary itself ("This will now be rolled out to all
  new users."). [25] reports a team that led with what was learned: "the first thing they mentioned was the insights of
  the tests. Everything else fell below that, winners and losers included."
- **Context and Setup** (lean). [5]'s "Experiment Setup" and [3]'s "Details - Include the number of variations, a
  brief description of the differences, the dates when the test was run, the total visitor count, and the visitor
  count by variation." Link the design doc rather than restating it. **New:** a line for what ran differently from the
  design doc, traced to [17]'s item 6 and item 24 (clinical lineage, labelled) and to [14]'s pre-registration
  ("Experiment owners need to specify up front which customer behavior they want to impact and how").
- **Key Results: Primary Metrics** (lean, table, PRIORITY and ROW HINT). The column shape follows [1] ("Metric Control
  Test Change (abs) Change (rel) CI Sig?"). [3] asks for "the percentage lift or loss, compared to the original,
  conversion rates by variation, and the statistical significance". [17] recommends "both relative and absolute effect
  sizes" for binary outcomes, which is clinical lineage and corroborates [1]'s two change columns. The interval's level
  is stated, never assumed (contested item 8).
- **Key Results: Supporting Metrics** (lean, table). [1]'s second results section. [8] defines a guardrail as one that
  measures what "we don't want to degrade but won't necessarily improve"; [21] separates "Decision-making metrics" from
  "Guardrail metrics". Each guardrail row reports against the threshold the design doc fixed.
- **Validity Checks** (lean). **POSITION as a named section**, as the spec records. Its content is well sourced: a
  sample ratio mismatch ([10], [8]: SRMs "typically invalidate the A/B test"), a mismatch in one metric's own
  observation units ([9]: "Check for Imbalance in Metric Observation Units"), a novelty effect read by date ([8]:
  "Rapid decline of estimated treatment effect across date segments of an A/B test is an indicator of novelty
  effect"), early looks ([12], [11]'s "peeking (deciding on an experiment before it's completed)"), telemetry changes
  ([9]: "Check for any Telemetry-Breaking Changes") and interaction with other live experiments ([24], [26]). Each
  check reports against the design doc's own pre-commitment where one exists.
- **Deep-Dive** (full). [1]: "Structure this as business questions to be answered." [2]: "Experiment reports discuss
  the "why," not the "what."" Only segments fixed in the design doc may bear on the decision. [11] names the trap
  ("slicing the data until it shows what you want to see"), and [18] asks that when a "subgroup analysis is displayed,
  the analysis of the complement subset should also be displayed." (clinical lineage, labelled). An estimated impact
  goes here with its interval: [3]'s "Revenue Impact" and [25]'s "with a 90% certainty, the increase in conversion
  after implementation will be somewhere between 7.5% and 19%".
- **Decision: Ship, Iterate or Stop** (lean). The triad is the contract's wording and a **POSITION**; no source uses
  it. The nearest are [6]'s "ship/no-ship decision", [7]'s "Win Lose Flat", [5]'s "roll out to more users, end,
  iterate, etc." and [4]'s "inconclusive" or "hypothesis proved". **New:** a null result states what it rules out and
  what it does not. [13]'s "Neutral but informative" requires that "the test was strong enough to detect one if it
  existed", and [24] reports that "regardless of whether the experiment gets launched or shut down - we learn something
  new". An ASK on reversibility comes from [27]: most decisions "are changeable, reversible - they're two-way doors."
- **Decision Owner** (lean). **POSITION, unsourced**, as the spec records. [3]'s "Decision maker" is the nearest
  source, and it names a role, not a field.
- **Next Steps and Owners** (lean). [1]: "Roll out immediately to 100% of new users (owner: Ben Nowak)". [5] adds
  "Plan for this project going forward" as the frame.
- **Implementation Details and Analysis Notes** (full). [1]: "The geeky stuff goes here - what other data scientists
  and engineers would be interested in!" [17] corroborates the separation from its own lineage: CONSORT "solely
  addresses the reporting of what was done and what was found."
- **Further Analysis** (full). [5]: "This optional section is where you can include interesting analysis or insights
  for readers that are looking for more details on your project". The section is labelled exploratory: it carries
  nothing the decision rests on ([18]'s caution that, with enough subgroups, a treatment with no benefit "will
  inevitably appear" "disproportionately beneficial in one or more subgroups.", clinical lineage).

**Frontmatter, not a section:** the experiment's name, a link to its design doc, the author, the decision-maker, the
test's start and end dates, the decision and the readout date. The design-doc link is the library's POSITION, from the
contract's shared-scenario rule; no source read names a link field (dimension 6 searched for one).

**Sizes.** `[lean, full]`, lean the default. [2] is the evidence for a short core: "You cannot produce ten-page
experiment reports, and will have to leave out some interesting findings." [5] marks its Further Analysis section
optional. Full adds Deep-Dive, the analysis notes and Further Analysis, for a test whose decision rests on more than
its primary metric or whose readers will audit the analysis.

**When not to write one, for the guide.** A test that has not ended needs no readout: [12] says "Don't report
significance levels until an experiment is over". A spike, a test plan's pass or fail grade, an OKR score and a live
dashboard each have their own bundle (see Boundaries in the spec). A team that keeps one living experiment document
fills this bundle's sections into it, per the spec's guide line.

### The gap question's result, and what this build does with it

Dimension 6 searched for what a good readout does beyond the commonest published sections, without reading the
bundle. Each candidate went through
[decision procedure 12](../../docs/internal/decision-procedures.md#12-a-property-or-section-is-proposed-for-a-template).

- **Deviations from the pre-registered plan: adopted in Context and Setup, lean.** E1: [14], [17] items 6 and 24.
- **Segment effects without fishing: adopted in Deep-Dive as an ASK and a TRAP, full.** E1: [18], [11], and the
  worked example's own segment lock.
- **A null or mixed result as a result: adopted in Decision, lean.** E1: [13], [24], and the design doc's null
  branch.
- **Interaction with other live experiments: adopted as a Validity Checks row, lean.** E1: [24] ("we knew that this
  would conflict with the existing Friends feature on desktop"), [26].
- **Business impact stated with its uncertainty: adopted in Deep-Dive, full.** E1: [3], [25].
- **Leading with what was learned: adopted as an ASK in Executive Summary.** E1: [25], [2].
- **A searchable archive: frontmatter fields that group, no tags field.** E1: [14], including its finding against
  tags. The frontmatter carries the experiment name and the design-doc link.
- **The decision's reversibility: adopted as an ASK in Decision.** E1: [27].
- **Who may stop an experiment, and whether stops are automated: null result for the template.** It is program policy
  ([14], [21]), mentioned in the companion only.
- **Holdout groups and long-term follow-up: null result.** No source read in full describes reporting one.

### What the bundle must not say

- "Ship, iterate or stop" as a sourced convention, or the catalog's "ship/iterate/kill" at all.
- A significance level, power level or test duration as a convention. "95%" appears only as Netflix's practice ([15]).
- "Primacy effect" as a sourced term. No source read uses it.
- That Microsoft calls its scorecard "a machine-generated table". [23] says "A scorecard is a collection of metrics".
- Any clinical or public-sector element ([17], [18], [19], [20]) presented as product-management practice. Each
  borrowed element names its lineage, as contract section 3 item 6 requires.
- That a null result proves no effect. A null on a test powered for a large effect says nothing about a smaller one.
- That tags make an archive findable. [14] reports the opposite.
- That a guardrail breach blocks shipping as a universal rule ([9]).
- [13]'s rates as anything but Spotify's.
- That writing a readout improves decisions, as a measured result.
- That any vendor licenses its template.
- A quotation from a CONSORT checklist row. The table body was not read.
- Any gendered pronoun for a source author. Use the author's name.

### GOOD and WEAK illustrations use their own scenario

Every GOOD and WEAK example in the templates' guidance comments uses a scenario unrelated to the worked example: not
Acme Analytics, not the Reporting Platform Modernization program, not Saved Views, not a prompt or nudge, not
dashboards, views or reports, not Recurring Analysts, and none of Priya Nair, Dana Osei, Dana Okoro, Lee Zhang or
Marta Reyes. It should also differ from the scenarios the design doc's own GOOD and WEAK text uses. Two earlier builds
shipped GOOD text in the worked example's own scenario (`announcement-internal-comms` and `change-request`, caught
after every review lens had passed).

### The example

The readout of **the Saved Views adoption-nudge experiment**, dated **2026-09-04**, reporting the test that
`templates/experiment-design-doc/experiment-design-doc_example.md` planned. Contract section 4 binds it to that plan's
hypothesis, metrics and decision rule.

It must carry these commitments from the design doc, exactly:

| Commitment | Value | Design doc |
|---|---|---|
| Hypothesis | The fifth-view prompt raises weekly Saved Views adoption against a no-prompt control | lines 31-34 |
| The hypothesis's failure condition | Treatment "matches or trails the no-prompt control's own figure" at the end of the four weeks | lines 39-40 |
| Variants and unit | Control and treatment, 50/50; randomization by customer account, not analyst | lines 48-51 |
| Population | Roughly 230 eligible accounts (illustrative); the six design-partner analysts and their accounts excluded | lines 44-47, 59-64, 91-93 |
| Primary metric and baseline | Saved Views adoption, the share of Recurring Analysts using a saved view weekly; 41% (KPI dashboard, last reviewed 2026-07-20) | lines 68-76 |
| Statistical approach | Fixed horizon at the platform's standard setting: 80% power and a 5% significance level (illustrative) | lines 83-84 |
| Minimum detectable effect | About 18 percentage points, treatment against control | lines 83-90 |
| Run dates | 2026-08-03 through 2026-08-31; no decision-bearing look before 2026-08-31 | lines 94-100 |
| Guardrails | Weekly active analysts not below 480; dashboard load error rate not above its pre-test level; shared-view permission incidents at zero | lines 77-79 |
| Decision rule | Win: roll out to 100% and retire the control. Null: shelve the prompt rather than rerun it unchanged, bring the finding to the next Reporting Platform Modernization steering review, and weigh a different mitigation for R-04 (adoption risk). Breach: stop the test and send any permission incident to Dana Osei | lines 106-117 |
| Decision-maker | Priya Nair (PM, Reporting) | line 116, frontmatter |
| Validity pre-commitments | Daily SRM check owned by Lee Zhang (Data Eng); week-1 lift compared with weeks 2 to 4, a lift decaying toward zero flagged as novelty; no segments beyond the two arms | lines 132-137 |
| Support notification | Marta Reyes, before 2026-08-03 | lines 145-146 |

**The recommended outcome: a null, with the point estimate above control.** These figures are this log's
recommendation for the example, labelled illustrative in it, and chosen so every commitment above is exercised:

- 231 accounts assigned, 117 control and 114 treatment; the daily SRM check passed on every day of the run.
- Week-4 weekly adoption, the pre-registered read: control 43%, treatment 45%, a change of +2 points (+5% relative),
  with a 95% interval from -11 to +15 points, matching the 5% significance level the design doc fixed (lines
  83-84).
- The week-1 lift was +9 points, falling to +4, +3 and +2 over weeks 2 to 4. Under the design doc's pre-commitment that
  is a decay toward zero, so the early lift is flagged as novelty and not counted as the finding.
- Guardrails held: the lowest daily weekly-active-analysts reading was 487, the load error rate stayed at its pre-test
  level, and no permission incident occurred.
- Decision: stop. The prompt is shelved, not rerun unchanged. The null rules out a lift of about 18 points or more, and
  says nothing about a smaller one; the interval's upper end, +15, is consistent with that.

**What the example decides, and must say it decided.** The design doc's failure condition and its decision rule
disagree on this outcome. Treatment finished above control, so the hypothesis did not "fail" in the design doc's own
words. The difference was not significant, so the decision rule reads it as a null. The readout states that the
decision rule governs, because it is the pre-registered decision, and records the mismatch as a lesson for the next
design doc. The readout also names its next steps' owners from people the siblings already carry: Priya Nair takes the
finding to the steering review, and Lee Zhang marks `nudge_variant_assigned` for retirement in the tracking plan. Any
other assignment is stated as the readout's own choice.

It must not contain: the OKRs' Initiatives-table status line for Saved Views (`okrs_example.md:90`); any of the four
residuals PR #204 left unfixed (the announcement's "private views since late June", the retrospective's 2026-09-14
general-availability date, the release notes' known issue promising a fix in 2.4.1, and the definition of done's
"DEF-2291 shipped in build 2.3.2"); an explanation of why the 41% baseline predates the release; a date for the next
steering review, which no sibling gives; or any document dated after 2026-09-04 cited in body prose.

---

## Sources

### PRODUCT-EXPERIMENTATION CANON: WHAT A READOUT CARRIES

**[1] Eppo - "Experiment Report Template (Example)" (Google Doc export).** vendor. **fetched-and-verified.**
`https://docs.google.com/document/d/1mWWzaAdTfuQWGp2tHE5NVN6pL-Tx0_JTKlDLZOcmUqw/export?format=txt`
Supports: Full section/field order; Key Results table columns; decision stated in prose, not a labeled field; next-steps owners named per item
Quotable: "Experiment Title"
Quotable: "Author & Team"
Quotable: "Executive Summary"
Quotable: "Next Steps"
Quotable: "Key Results: Primary Metrics"
Quotable: "Key Results: Supporting Metrics"
Quotable: "Deep-Dive"
Quotable: "Implementation Details and Analysis Notes"
Quotable: "Metric Control Test Change (abs) Change (rel) CI Sig?"
Quotable: "This will now be rolled out to all new users."
Quotable: "Roll out immediately to 100% of new users (owner: Ben Nowak)"
Quotable: "Structure this as business questions to be answered."
Quotable: "The geeky stuff goes here - what other data scientists and engineers would be interested in!"

**[2] Ryan Lucht (Eppo blog) - "How to Craft Compelling, Impactful Experiment Reports".** vendor. **fetched-and-verified.**
`https://www.geteppo.com/blog/how-to-craft-compelling-impactful-experiment-reports`
Supports: Who writes/when (start before the test ends); the why-not-what framing; short main report + separate deep-dive notebook for weight
Quotable: "Start writing early, even before the experiment ends."
Quotable: "Experiment reports discuss the "why," not the "what.""
Quotable: "Decide your reader persona and create a narrative."
Quotable: "You cannot produce ten-page experiment reports, and will have to leave out some interesting findings. A common strategy is to do your deep-dive work within a notebook or BI report"
Quotable: "never pass up an opportunity to write up and share results from an experiment"

**[3] Optimizely docs - "Share your results with stakeholders".** vendor. **fetched-and-verified.**
`https://docs.optimizely.com/experimentation-strategy/docs/share-your-results-with-stakeholders`
Supports: Results-sharing section names; metric-result fields (narrative, not a table); cadence/audience per reader tier; plan vs. results report named as separate materials
Quotable: "Purpose - Briefly describe "why" you are running this test, including your experiment hypothesis."
Quotable: "Details - Include the number of variations, a brief description of the differences, the dates when the test was run, the total visitor count, and the visitor count by variation."
Quotable: "Results - Be concrete. Provide the percentage lift or loss, compared to the original, conversion rates by variation, and the statistical significance"
Quotable: "Lessons Learned - This is your chance to share your interpretation of what the numbers mean and critical insights generated from the data."
Quotable: "Revenue Impact - Whenever possible, quantify the value of a given percentage lift with year-over-year projected revenue impact."
Quotable: "Experiment plan"
Quotable: "Share results with the rest of your organization at the end of each test"
Quotable: "Share your progress with executive stakeholders once per quarter"
Quotable: "Results report (an Excel download, a link to the Experiment Results page"
Quotable: "or an internal analytics report)"
Quotable: "Decision maker"

**[4] Optimizely (via Atlassian Confluence) - "Experiment plan and results template".** vendor. **fetched-and-verified.**
`https://www.atlassian.com/software/confluence/templates/experiment-plan-and-results`
Supports: Section order and names for the results/conclusions part of a merged plan+results document; decision labels are 'inconclusive'/'hypothesis proved', not ship/iterate/stop; no metric-column table given on this page
Quotable: "1 Cover the basics"
Quotable: "2 Set a plan for your experiment"
Quotable: "3 Outline your results"
Quotable: "4 Draw conclusions"
Quotable: "Document them in the Results section of the template. Jot down your experiment start and end date, the link to your Optimizely results, and a short summary of the metrics that you monitored. Make sure you also assign a clear conclusion (such as "inconclusive" or "hypothesis proved") here"
Quotable: "In the Conclusions section of the template, highlight your primary goals and other metrics for easy reference. Then, write down key takeaways, questions, and observations and outline any next steps that your team should take."

**[5] Tanmayi Sai - "Experiment Readout Template".** practitioner. **fetched-and-verified.**
`https://tanmayisai.com/2020/11/20/experiment-readout-template/`
Supports: Full section order for one merged readout document; per-metric table columns are the variant names, not a fixed column set; next-steps language close to but not matching ship/iterate/stop; lean-vs-full evidence via the 'optional' Further Analysis section; who writes/reads
Quotable: "Subject / Title"
Quotable: "TL;DR"
Quotable: "Context"
Quotable: "Experiment Setup"
Quotable: "Results"
Quotable: "Next Steps"
Quotable: "Further Analysis"
Quotable: "Shoutouts"
Quotable: "Keeping track of the performance of an experiment or feature that you shipped, either in emails or an evolving document, is essential for maintaining stakeholder alignment and boosting your visibility as a product manager."
Quotable: "Plan for this project going forward - roll out to more users, end, iterate, etc."
Quotable: "This optional section is where you can include interesting analysis or insights for readers that are looking for more details on your project"

**[6] Adam Fishman - "Creating an Experiment Doc".** practitioner. **fetched-and-verified.**
`https://www.fishmanafnewsletter.com/p/experiment-document-template`
Supports: The Results section's analysis questions; the pre-committed ship/no-ship decision rule (worded 'ship/no-ship', not a triad); no metric-column table given; owners named earlier in the doc, not in Results itself
Quotable: "The Results"
Quotable: "What was the final outcome? Which version won and by how much? Why did we observe what we observed? What is the final recommendation and conclusion? Are any follow-ups needed? What were the takeaways of our metrics assessment - how were our tradeoff metrics impacted? Did we observe any other, interesting behavior?"
Quotable: "The most important aspect of the results is the "why.""
Quotable: "Post Experiment Decisions (aka If This Works We Should)"
Quotable: "Articulating this ship/no-ship decision in advance helps drive alignment."
Quotable: "there are four distinct parts to any meaningful experiment document: The Why The Plan The Results The Checklist"
Quotable: "Conduct analysis and share out the results."

**[7] Bhavik Patel (Amplitude blog) - "Use experiment briefs to design better experiments".** vendor. **fetched-and-verified.**
`https://amplitude.com/blog/experiment-brief`
Supports: Phase 4 'Analyze and Decide' fields; the pre-committed Win/Lose/Flat decision outcomes (not ship/iterate/stop); no owner field named at decision time; single document spanning all four phases
Quotable: "Phase 4: Analyze and Decide"
Quotable: "Analysis: Document the outcome of the experiment"
Quotable: "Decision: Decide next steps based on your planning phase."
Quotable: "Monitor ongoing performance: Continue to analyze behavior post-experiment"
Quotable: "Actions: What actions will you take based on each of the following outcomes of the test? Win Lose Flat"
Quotable: "Anyone should be able to quickly get access to the key facts and outcomes of every experiment"

### REPORTING HONESTLY: VALIDITY CHECKS, UNCERTAINTY AND THE NAMED TRAPS

**[8] Widad Machmouchi, Somit Gupta, Ruhan Zhang - "Patterns of Trustworthy Experimentation: During-Experiment Stage" (Microsoft Experimentation Platform / Microsoft Research, published January 25, 2021).** primary. **fetched-and-verified.**
`https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/`
Supports: Guardrail/OEC metric taxonomy and alerting policy; SRM definition and consequence; multiple-hypothesis-testing/peeking caveat; novelty-effect worked example via date segmentation
Quotable: "A/B metrics should be Sensitive, Trustworthy, Efficient, Debuggable, and Interpretable (STEDI) [2] to allow the experimenter to properly understand the treatment effect and interpret the metric movements observed."
Quotable: "Guardrail Metrics"
Quotable: "Measure aspects of the product that we don't want to degrade but won't necessarily improve"
Quotable: "Page Load Time, Crash Rate, Abandonment Rate"
Quotable: "Note that with these repeated measurements throughout the test, we need to account for multiple hypothesis testing and early peeking in our statistical methods [7][8][9]. At ExP, to make early results more trustworthy, we require stronger statistical significance levels and in the absence of highly certain metric movements, we recommend running the test until the end of its pre-determined duration and adopt the metric movements observed then."
Quotable: "At ExP, we recommend that a feature crew set up alerts for their business-critical metrics: Guardrails (e.g. page load time, error rates) and OECs (e.g. user satisfaction metrics)."
Quotable: "One of the main metrics to set alerts on are Sample Ratio Mismatches (SRMs). SRMs occur when the number of users in treatment and control are not balanced and their ratio doesn't satisfy the expected ratio. SRMs typically invalidate the A/B test and make any results and metric movements untrustworthy."
Quotable: "At ExP, we recommend segmenting every A/B test analysis by date. Rapid decline of estimated treatment effect across date segments of an A/B test is an indicator of novelty effect. A treatment effect that is different at the beginning of the test compared to the end, is an indicator of change in the product or environment interacting with the treatment."
Quotable: "This was evidence of a novelty effect where users were getting confused and clicking repeatedly on the button [3]. Looking at date segments prevented us from shipping a change that has diminishing and non-lasting returns."

**[9] Widad Machmouchi, Somit Gupta - "Patterns of Trustworthy Experimentation: Post-Experiment Stage" (Microsoft Experimentation Platform / Microsoft Research, published December 24, 2021).** primary. **fetched-and-verified.**
`https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-post-experiment-stage/`
Supports: The post-experiment stage's own named patterns: verifying metrics are not invalidated, diluting triggered-analysis gains, trading off OEC vs guardrail movements, and closing the loop (reproduce, share, archive)
Quotable: "Verify Treatment Effects do not Invalidate Metrics"
Quotable: "Ensure Metric Movements Align with the Test Set-Up"
Quotable: "Check for any Telemetry-Breaking Changes"
Quotable: "Check for Imbalance in Metric Observation Units"
Quotable: "A metric movement can be hard to interpret if the number of samples in its computation changes during the experiment. ... Our guidance is to 1) create a separate metric for the denominator to test if it has moved in stat-sig way and 2) use the metric with the most fine-grained denominator where the denominator has no stat-sig movement."
Quotable: "Another example of an imbalance in the metric observation unit is a Metric SRM [3]. Such SRMs occur when the number of the metric's observation units is mismatched between treatment and control."
Quotable: "Estimate the Final Impact of the Treatment"
Quotable: "Segment By Triggered/Non-Triggered Users"
Quotable: "To verify that the trigger condition is all-inclusive of the treatment effect and that counterfactual logging is done correctly: 1) verify that the triggered scorecard has no Sample Ratio Mismatch [6] and 2) generate a triggered-complement analysis ... and confirm that it looks like an A/A."
Quotable: "Dilute Gains to Reflect the Trigger Rate"
Quotable: "There are two main requirements for dilution to apply in a specific A/B test: 1) There is a detectable statistically significant treatment effect in the metric when measured in the user-triggered analysis, and 2) there is no treatment effect detected in the triggered-complement user analysis."
Quotable: "Tradeoff the Observed Metric Movements"
Quotable: "There is no standard way to evaluate those tradeoffs. One method used by Bing [7] is to assign different weights for the various metrics used to make a ship decision. ... Note that these weights should be pre-determined and not depend on the specific A/B test being analyzed."
Quotable: "Close the Loop on Experiment Results"
Quotable: "When in Doubt, Reproduce Results"
Quotable: "Twyman's Law [8] implies that the metric movements, in this case, might not be trustworthy because we did not expect that a feature that has an extremely low engagement to have such a large effect on user satisfaction. ... We made the decision to re-run the experiment with a set of re-randomized users and with higher traffic."
Quotable: "The ultimate test for a treatment effect detected in an A/B experiment is reproducibility. Rerunning an A/B test (on a resampled set of users) and observing a comparable treatment effect greatly increases our confidence that the treatment effect is real. When in doubt, we re-run."
Quotable: "Regularly Share Experiment Results"
Quotable: "Archive Hypothesis, Tests, and Metric Movements"
Quotable: "One other reason to archive A/B tests and their metric movements across the organization is to provide transparency about all changes shipped that could impact a key metric. ... Having a central location visible to all teams, where shipped changes are recorded along with their impact on key metrics avoids this vicious cycle of shipping and unshipping the same or similar changes."

**[10] Casandra Campbell - "Sample ratio mismatch (SRM): how to identify the root cause and decide whether to restart your experiment" (GrowthBook Blog, Aug 7, 2026).** vendor. **fetched-and-verified.**
`https://www.growthbook.io/blog/sample-ratio-mismatch`
Supports: SRM definition, detection mechanism, and the decision tree for what to do once one is found at analysis time (recover, restart, or salvage a directional insight)
Quotable: "A sample ratio mismatch is a statistically significant gap between the traffic split you configured and the split your experiment produced. If you implemented a 50/50 test and the realized allocation is far enough from 50/50 that chance can't explain it, you have an SRM."
Quotable: "A chi-squared goodness-of-fit test detects an SRM by comparing the observed unit counts to the expected ones and returning a p-value, the probability of seeing an imbalance this large or larger if the samples were randomized correctly."
Quotable: "Once you've identified the cause of your SRM, there are 3 possible outcomes: recover the result, restart the experiment, or salvage a directional insight. Which outcome applies depends on whether the correct data exists and whether the treatment itself changed which units were counted."
Quotable: "If the raw events were logged correctly and a processing step created the SRM, you can fix that step, rerun the analysis, and keep the result."
Quotable: "If the correct data was never captured, or the treatment changed the underlying population, no reprocessing brings the lost units back, and you have to restart. ... You'll also want to restart when the imbalance is severe and the cause remains unidentified because with an unknown bias direction, neither a win nor a loss can be trusted."
Quotable: "If the cause is unrelated to user characteristics (like an issue with how units were allocated to buckets), or external and time-bounded (like a one-day bot spike that doesn't coincide with the movement in your metrics), you can sometimes treat the result as directional evidence. Document your reasoning before making decisions on any SRM-affected number so readers know it's directional."
Quotable: "The imbalance is severe and no root cause was found"
Quotable: "Unknown"
Quotable: "Restart. The result is not trustworthy in either direction"

**[11] Graham McNicoll - "9 common experimentation program mistakes to avoid" (GrowthBook Blog, Sep 6, 2024).** vendor. **fetched-and-verified.**
`https://www.growthbook.io/blog/experimentation-program-mistakes-to-avoid`
Supports: Named failure of reporting a non-win as a win via cherry-picking/multiple-comparison problems; peeking named as a bad-statistics failure mode
Quotable: "There are about a million ways to screw up interpreting data that can sink an experimentation program. The most common ones are: peeking (deciding on an experiment before it's completed), multiple-comparison problems (adding so many metrics or slicing the data until it shows what you want to see), and just cherry-picking data (ignoring bad results)."
Quotable: "I've seen experiments where every metric is down, save one that is partially up, and be called a winner because the product manager wanted it to win and focused on that one metric. Experimentation results used inappropriately can be used to confirm biases rather than reflect reality."
Quotable: "The fix? Train your team to interpret statistics correctly. Your data team should be the center of excellence, ensuring experiments are designed well and results are objective - not just confirming someone's bias."
Quotable: "Tools like GrowthBook, offer templated readouts that give everyone a clear, consistent understanding of what really happened in the A/B test. These templates, set up by experts, embed best practices to ensure business stakeholders can follow along and keep everyone on the same page."

**[12] Evan Miller - "How Not To Run an A/B Test" (evanmiller.org, April 18, 2010).** practitioner. **fetched-and-verified.**
`https://www.evanmiller.org/how-not-to-run-an-ab-test.html`
Supports: Peeking and early stopping as a statistical-significance trap that invalidates what a readout may claim about significance
Quotable: "When an A/B testing dashboard says there is a "95% chance of beating original" or "90% probability of statistical significance," it's asking the following question: Assuming there is no underlying difference between A and B, how often will we see a difference like we do in the data just by chance? The answer to that question is called the significance level."
Quotable: "However, the significance calculation makes a critical assumption that you have probably violated without even realizing it: that the sample size was fixed in advance. If instead of deciding ahead of time, "this experiment will collect exactly 1,000 observations," you say, "we'll run it until we see a significant difference," all the reported significance levels become meaningless."
Quotable: "Repeated significance testing always increases the rate of false positives, that is, you'll think many insignificant results are significant (but not the other way around)."
Quotable: "Try 26.1% - more than five times what you probably thought the significance level was."
Quotable: "If you run experiments: the best way to avoid repeated significance testing errors is to not test significance repeatedly. Decide on a sample size in advance and wait until the experiment is over before you start believing the "chance of beating original" figures that the A/B testing software gives you."
Quotable: "Don't report significance levels until an experiment is over, and stop using significance levels to decide whether an experiment should stop or continue. Instead of reporting significance of ongoing experiments, report how large of an effect can be detected given the current sample size."
Quotable: "Although they seem powerful and convenient, dashboard views of ongoing A/B experiments invite misuse. Any time they are used in conjunction with a manual or automatic "stopping rule," the resulting significance tests are simply invalid."

### LEARNING, ARCHIVES AND WHO DECIDES

**[13] Michael Bellato, Mårten Schultzberg, and Sebastian Ankargren (Spotify Data Science), "Beyond Winning: Spotify's Experiments with Learning Framework".** practitioner. **fetched-and-verified.**
`https://engineering.atspotify.com/2025/9/spotifys-experiments-with-learning-framework`
Supports: Winning vs. learning as a named, metric-backed distinction; explicit acceptance of shipping on a neutral/inconclusive result when the test was adequately powered
Quotable: "A successful experiment yields enough valid information to inform product decisions, not just those that find "winners.""
Quotable: "Our learning rate (~64%) far exceeds our win rate, emphasizing that most value comes from understanding what doesn't work or detecting regressions, not just shipping improvements."
Quotable: "Bottom line: A "successful experiment" isn't just one that finds a win - it's one that delivers trustworthy insights to guide product decisions."
Quotable: "Neutral but informative: No effect but the test was strong enough to detect one if it existed → Iterate, abandon, or ship if infra-only."
Quotable: "Powered, no recommendation: neutral metrics but informative ... When all success metrics are neutral and the test is adequately powered, we still classify it as an EwL."
Quotable: "Abort due to regression ... They may not be the wins experimenters hoped for, but they're valuable for the business and reflect Spotify's fail fast, learn fast approach"
Quotable: "Most of our learning doesn't come from wins - it comes from discovering what not to ship."
Quotable: "In the two orgs running ~80% of Spotify experiments, the learning rate is ~64%, but the win rate is ~12%."
Quotable: "We've seen that small things like adding experiment reviewers can drastically impact learning rates, both because practices improve when there are more eyes on experiments, but also because ideas get discussed and scrutinized more before tests start."

**[14] Raphael Lopez Kaufman, Jegar Pitchforth and Lukas Vermeer (Booking.com), "Democratizing online controlled experiments at Booking.com" (arXiv:1710.08217), read at its ar5iv HTML rendering.** primary. **fetched-and-verified.**
`https://ar5iv.labs.arxiv.org/html/1710.08217`
Supports: The searchable experiment archive/knowledge repository, what it stores and its findability limits; a readout that lives as one evolving record (hypothesis plus iterations plus final decision) rather than separate plan and readout files; who analyses results and makes the call; peer review as the sign-off mechanism; the readout's archive function (searchable repository, tagging abandoned), pre-registration of hypothesis and metrics, and who is authorized to act on a harmful result
Quotable: "Booking.com experiment platform acts as a searchable repository of all the previous successes and failures, dating back to the very first experiment, which everyone can consult and audit."
Quotable: "The data of these previous experiments is shown in the exact same state as it was to their owners, along with the hypotheses that were put to the test. Moreover, descriptions of all the iterations and of the final decision, whether the experiment was a success or not, are available."
Quotable: "one of the challenges we are still facing is being able to answer questions such as "what were the findings related to improving the clarity of the cancellation policies in the past year" in the central repository ... without resorting to using a set of tags to label experiments. Indeed, this approach is proving not sustainable both because it involves making sure the tags are normalized and kept up to date and because it entails poor discoverability and usability of the central repository."
Quotable: "all the steps required to validate new product ideas are fully decentralized: gathering learnings from previous experiments to inform new hypotheses, implementing and running new tests, creating metrics to support new areas of the business and most importantly analysing the results and making decisions."
Quotable: "deciding whether an experiment is more harmful than beneficial, given that some experiments are aiming at gaining a better understanding of visitors' behaviour rather than bringing a "win", is a judgement call which is best made by those who own the change."
Quotable: "Enabling everyone to come up with new hypotheses is key to democratizing experimentation and move away from a product organization where only product managers decide what features to test next."
Quotable: "acts as a searchable repository of all the previous successes and failures, dating back to the very first experiment, which everyone can consult and audit"
Quotable: "Experiments can be grouped by teams, areas of the Booking.com products they ran on, segments of visitors they targeted and much more"
Quotable: "this approach is proving not sustainable both because it involves making sure the tags are normalized and kept up to date and because it entails poor discoverability and usability of the central repository"
Quotable: "Experiment owners need to specify up front which customer behavior they want to impact and how, the set of metrics which is going to support their hypothesis, and how these metrics are going to change"
Quotable: "Coupled with a culture which encourages peer review of successes this enforcement considerably reduces p-hacking"
Quotable: "Everyone in the company must be able and feel empowered to stop harmful experiments of their own accord"
Quotable: "we could easily automate such stops. However, we feel this goes contrary to democratizing experimentation which fosters end to end ownership"

**[15] Aakash Gupta (with Bandan, Booking.com/Gojek product leader), "Netflix: Lessons in Experimentation".** practitioner. **fetched-and-verified.**
`https://www.aakashg.com/netflix-experimentation/`
Supports: Secondary-metric guardrails versus a single north-star metric as the basis for a ship decision; a quality-control step on the write-up before a result is trusted
Quotable: "Although north star metrics help, many decisions are made at the 95% confidence level. How do you make a final conclusion? At Netflix, the data scientists dive further into the overall metrics to make sure the story hangs together and compare with results from other experiments. This helps the larger company generate more confidence in its results."
Quotable: "This is important to double-click on. Experiments often will have varying results on different metrics, so it is important for the team and company to have a north star metric everyone can agree on."
Quotable: "None of these secondary metrics would decide an experiment for Netflix"

**[16] Itamar Gilad, "Idea Validation Using the AFTER Model".** practitioner. **fetched-and-verified.**
`https://itamargilad.com/idea-validation-much-more-than-just-a-b-experiments/`
Supports: Boundary finding only: this source argues against treating A/B experiments as the only or default validation method, but it does not discuss the readout document itself, archiving, authorship/sign-off, shipping on neutral results, or living-document-versus-separate-files practice
Quotable: "While experiments are the gold standard, of validation, there are many other, far cheaper and more immediate ways to test an idea. By fixating on experiments many companies set the bar too high, miss out on easier opportunities, and often give themselves an excuse to keep doing things the old way."
Quotable: "Experiments are tests that include a control element to guard against false results caused by random chance. Per this definition an A/B test is an experiment, but a usability test is not. I realize that this is not the common definition used in the industry - in many cases the words test and experiment are used interchangeably."

### THE OTHER TWO LINEAGES: TRIAL REPORTING AND PUBLIC-SECTOR EVALUATION

**[17] Kenneth F. Schulz, Douglas G. Altman, David Moher, for the CONSORT Group - "CONSORT 2010 Statement: Updated Guidelines for Reporting Parallel Group Randomised Trials" (PLoS Medicine, 24 March 2010).** primary. **fetched-and-verified.**
`https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000251`
Supports: academic-trial-reporting: the CONSORT 2010 checklist's scope, its licence, and the specific items the 2010 revision added or changed (outcomes, blinding, statistical methods, recruitment, baseline data, outcomes/estimation, harms, limitations, interpretation, registration, protocol, funding)
Quotable: "The CONSORT 2010 Statement is this paper including the 25 item checklist in the table (Table 1) and the flow diagram (Figure 1)."
Quotable: "Item 15 (baseline data)- We specified “A table” to clarify that baseline and clinical characteristics of each group are most clearly expressed in a table."
Quotable: "Sub-item 17b (outcomes and estimation)- For appropriate clinical interpretability, prevailing experience suggested the addition of “For binary outcomes, presentation of both relative and absolute effect sizes is recommended”."
Quotable: "Item 19 (harms)- We included a reference to the CONSORT paper on harms."
Quotable: "Item 20 (limitations)- We changed the topic from “Interpretation” and supplanted the prior text with a sentence focusing on the reporting of sources of potential bias and imprecision."
Quotable: "Item 23 (registration)- We added a new item on trial registration. Empirical evidence supports the need for trial registration, and recent requirements by journal editors have fostered compliance."
Quotable: "Item 6 (outcomes)- We added a sub-item on identifying any changes to the primary and secondary outcome (endpoint) measures after the trial started. This followed from empirical evidence that authors frequently provide analyses of outcomes in their published papers that were not the prespecified primary and secondary outcomes in their protocols, while ignoring their prespecified outcomes (that is, selective outcome reporting)."
Quotable: "Thus, CONSORT 2010 is not intended as an instrument to evaluate the quality of a trial. Nor is it appropriate to use the checklist to construct a “quality score.”"
Quotable: "Copyright: © 2010 Schulz et al. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited."
Quotable: "We added a new item on availability of the trial protocol. Empirical evidence suggests that authors often ignore, in the conduct and reporting of their trial, what they stated in the protocol."
Quotable: "It solely addresses the reporting of what was done and what was found."

**[18] European Medicines Agency, Committee for Medicinal Products for Human Use, "Guideline on the investigation of subgroups in confirmatory clinical trials" (EMA/CHMP/539146/2013, draft dated 23 January 2014). A clinical-trial lineage source, not product practice.** primary. **fetched-and-verified.**
`https://www.ema.europa.eu/en/documents/scientific-guideline/draft-guideline-investigation-subgroups-confirmatory-clinical-trials_en.pdf`
Supports: how to report heterogeneous/segment effects without fishing: pre-specify which subgroups will be examined, report interaction confidence intervals rather than a bare p-value, always show the complement subgroup, and do not reflexively dismiss undeclared heterogeneity either
Quotable: "strategy that simply assumes homogeneity of a population in terms of its likely response to"
Quotable: "treatment, without discussion and without further investigation, is not sufficient."
Quotable: "not sufficient to dismiss all subgroup findings that indicate heterogeneity of response as being"
Quotable: "associated with no benefit, if a large number of subgroups are examined it will inevitably appear"
Quotable: "disproportionately beneficial in one or more subgroups."
Quotable: "The test for interaction will be associated with a p-value. Although still common practice, the sole"
Quotable: "reporting of a p-value from a test for interaction cannot be considered adequate."
Quotable: "subgroup analysis is displayed, the analysis of the complement subset should also be displayed."
Quotable: "Patients excluded from a particular subgroup are described as the complement subgroup."
Quotable: "Reproduction is authorised provided the source is acknowledged."

**[19] HM Treasury - The Magenta Book: Central Government Guidance on Evaluation (HTML edition, cited text dated May 2026).** primary. **fetched-and-verified.**
`https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html`
Supports: public-sector-evaluation: when an evaluation report is written in the evaluation lifecycle, what it must cover on publication/transparency, its treatment of unintended/negative impacts, its caution on the report's limited value for impact and influence, and its Open Government Licence
Quotable: "While a final evaluation report is an important document in an evaluation study, it is rarely the best way to ensure impact and influence. For example, front-line delivery staff and ministers will have very different information needs and preferred communication styles."
Quotable: "Were there any unintended or negative impacts?"
Quotable: "Principle 1: The products of government social research and analysis will be made publicly available. ... This establishes a presumption that all outputs will be published."
Quotable: "Principle 2: There will be prompt release of all government social research and analysis. ... This sets a 12-week maximum from agreement of a final output to publication."
Quotable: "Reporting transparency (publishing all evaluation reports and fully describing all key methodological choices, communicating the uncertainty around findings, and demonstrating the robustness of results to alternative analytical approaches)."
Quotable: "Disseminate, use & learning ... Prepare final evaluation analysis and outputs. ... Implement end-of-project QA plan. ... Implement dissemination plan, including publication."
Quotable: "provides cross-government advice on the publication of research, including evaluation. It covers all aspects of publication through the following five principles."
Quotable: "Crown copyright 2026"
Quotable: "This publication is licensed under the terms of the Open Government Licence v3.0 except where otherwise stated."

**[20] Kate Glazebrook, Chris Larkin and Elisabeth Costa (Behavioural Insights Team) - "Improving engagement with pension decisions: The results from three randomised controlled trials" (report prepared for the UK Government's Pension Wise service, October 2017).** practitioner. **fetched-and-verified.**
`https://www.bi.team/wp-content/uploads/2017/10/Pension-wise-trials.pdf`
Supports: public-sector-evaluation (applied RCT in a public-sector delivery context): the report's exact section order, its method (TEST framework), headline-results framing, and the policy-implications conclusion
Quotable: "1. Introduction ... Policy background ... The behavioural insights approach"
Quotable: "2. Headline results ... 3. The Royal London trial ... Behavioural literature ... Trial design ... Results ... 4. The Standard Life trial ... Behavioural literature ... Trial design ... Results ... 5. The Liverpool Victoria (LV=) trial ... Behavioural literature ... Trial design ... Results ... 6. Conclusion and policy implications ... Annexes"
Quotable: "The Behavioural Insights Team uses a consistent methodological approach for each project. It forms a mnemonic known as TEST, and includes four key components: 1. Target ... 2. Explore ... 3. Solution ... 4. Trial"
Quotable: "We tested three interventions across three trials. Results were mixed, with a statistically significant negative effect for one of the trials, and statistically significant positive effects for the other two."
Quotable: "A statistically-significant decrease of 2.6 percentage points in the likelihood of visiting the PW website as a result of the intervention."
Quotable: "A statistically-significant increase of 9.8 percentage points in the likelihood of visiting the PW website, and a statistically-significant increase of 3.5 percentage points in the likelihood of calling the PW booking line as a result of receiving the intervention."
Quotable: "There are several conclusions that we can draw from the interventions tested in the trials presented in this report. The first is that salience matters."
Quotable: "we recommend that RCTs, or perhaps quasi-experimental methods if necessary, are used by PW in trialling further iterations of the Pension Passport."

### BOUNDARIES: THE SCORECARD, THE GENERATED SUMMARY AND THE METRIC TABLE

**[21] Optimizely docs, "Understand your Experiment Scorecard" (Analytics docs).** vendor. **fetched-and-verified.**
`https://docs.optimizely.com/analytics/docs/understand-your-experiment-scorecard`
Supports: What an in-tool experiment scorecard contains, and that it is a live configurable surface, not a document
Quotable: "An Experiment Scorecard template consists of the following modules:"
Quotable: "Measure module"
Quotable: "Experiment module"
Quotable: "Metrics module"
Quotable: "Segmentation module"
Quotable: "Filters module"
Quotable: "Visualization module"
Quotable: "Decision-making metrics"
Quotable: "Guardrail metrics"
Quotable: "Statsig over time - Displays the statistical significance of different variants over time."
Quotable: "The Set alerts option lets you set thresholds on key experiment metrics and receive alerts when a metric crosses one."
Quotable: "Guardrail alerts stop running 30 days after the experiment starts."

**[22] Statsig, "Experiment Summary PDF" (Product Updates).** vendor. **fetched-and-verified.**
`https://www.statsig.com/updates/update/experiment-summary-pdf`
Supports: What a results export (PDF) contains today, and the vendor's own statement that a decision-maker's free-form interpretation is a future feature, not a shipped one, as of the post's 10/9/2023 date
Quotable: "Today, we're excited to start rolling out an easy way to export a shareable summary of your experiment via PDF."
Quotable: "Your PDF summary will contain- Key Setup Information, such as hypothesis, actual vs. target duration, primary/ secondary metrics, experiment variants (w/ group descriptions and images), etc."
Quotable: "Results Overview, such as a snapshot of your experiment's Pulse results, experiment settings (CUPED enabled, etc.), and granular metric-by-metric raw stats"
Quotable: "In the future, we'll also be adding a surface for experiment decision-makers to add more free-form recap text, to provide future viewers of this experiment with additional helpful context."

**[23] Kai Qi and Momo Meng, Microsoft Experimentation Platform, "Treatment Effect Assessment at Scale: Accounting for Correlated Metrics and Metric Relevance in Modern Experimentation" (Microsoft Research articles).** practitioner. **fetched-and-verified.**
`https://www.microsoft.com/en-us/research/articles/treatment-effect-assessment-at-scale-accounting-for-correlated-metrics-and-metric-relevance-in-modern-experimentation/`
Supports: What a scorecard is (a statistical metric-aggregation surface) and that automated scoring cannot substitute for human interpretation of relevance/decision
Quotable: "feature launches are routinely evaluated through A/B tests that can generate hundreds-or even thousands-of metrics for a single experiment."
Quotable: "A scorecard is a collection of metrics used to evaluate the success of a product change or experiment."
Quotable: "teams often reuse standardized scorecard templates and shared metric sets across many experiments."
Quotable: "Does that mean experiment evaluation can now be automated based on metric movements and a TEA p-value? Not quite."
Quotable: "the experimentation platform typically has limited context about the experiment itself. Feature flags are often identifiers, and metrics are often little more than names. Without deeper product knowledge, and in some cases due to privacy constraints, the platform cannot reliably determine which metrics are truly related to the feature under test."
Quotable: "an agent that can identify and prioritize experiment-relevant metrics is likely to make better decisions than one that treats every metric equally."

### THE GAP QUESTION

**[24] Lavanya Aprameya (Duolingo Engineering Blog), "Improving Duolingo, one experiment at a time".** practitioner. **fetched-and-verified.**
`https://blog.duolingo.com/improving-duolingo-one-experiment-at-a-time/`
Supports: what a readout does with a null or mixed result, and how a readout accounts for interaction with a concurrently running feature
Quotable: "we found a double-edged sword: while there was a slight increase in revenue, we unfortunately also saw a decrease in user retention"
Quotable: "even though this experiment was successful from a revenue standpoint, we decided to shut it down and iterate on it"
Quotable: "with each experiment report - regardless of whether the experiment gets launched or shut down - we learn something new about our learners and our app"
Quotable: "we knew that this would conflict with the existing Friends feature on desktop, since both involved comparing progress among certain sets of users. To account for this, the experiment we ran had two branches"
Quotable: "the experiments service attempts to address this by defining a set of report templates, where each template contains a curated list of relevant metrics, in addition to universal metrics that are always important to consider"

**[25] Alex Birkett (CXL), "How To Communicate A/B Test Results To Stakeholders" (citing Kevin Hillstrom of Mine That Data, Joanna Lord of Porch, Optimizely's knowledge base, and Annemarie Klaassen & Ton Wesseling of Online Dialogue).** practitioner. **fetched-and-verified.**
`https://cxl.com/blog/how-to-communicate-ab-test-results/`
Supports: the readout's business-impact section (quantified revenue impact plus a stated confidence level) and the stakeholder-communication practice of leading with insight rather than win/loss
Quotable: "In general, here are the things they recommend you put in your reports: Purpose... Details... Results: Be concrete. Provide the percentage lift or loss... Lessons Learned: This is your chance to share your interpretation of what the numbers mean, and key insights generated from the data."
Quotable: "Revenue Impact: Whenever possible, quantify the value of a given percentage lift with year-over-year projected revenue impact."
Quotable: "the analyst can easily explain to other team members or executives that, with a 90% certainty, the increase in conversion after implementation will be somewhere between 7.5% and 19%"
Quotable: "at Porch they put out a weekly newsletter on testing. In it, the first thing they mentioned was the insights of the tests. Everything else fell below that, winners and losers included."
Quotable: "Is there a segment where you can still get a lot of value from a losing variation?"

**[26] Google Research Blog, "Overlapping Experiment Infrastructure: More, Better, Faster Experimentation" (summarizing Tang, Agarwal, O'Brien & Meyer, KDD 2010).** primary. **fetched-and-verified.**
`https://research.google/blog/overlapping-experiment-infrastructure-more-better-faster-experimentation/`
Supports: the mechanism by which concurrently running experiments are kept independent, which a readout would need to invoke if it claims its estimate is uncontaminated by other live experiments
Quotable: "Google's infrastructure supports this vast experimentation by using orthogonal diversion criteria for experiments in different "layers" so that each event (e.g. a web search) can be assigned to multiple experiments."
Quotable: "Decision making is improved by the consistency and accuracy in metrics assured by these tools."

**[27] Farnam Street, "Reversible and Irreversible Decisions" (quoting Jeff Bezos's Amazon shareholder letter).** practitioner. **fetched-and-verified.**
`https://fs.blog/reversible-irreversible-decisions/`
Supports: naming a launch decision's reversibility explicitly ties back to experimentation itself: over-applying irreversible-decision rigor is linked directly to under-experimenting
Quotable: "Some decisions are consequential and irreversible or nearly irreversible - one-way doors - and these decisions must be made methodically, carefully, slowly, with great deliberation and consultation."
Quotable: "most decisions aren't like that - they are changeable, reversible - they're two-way doors. If you've made a suboptimal Type 2 decision, you don't have to live with the consequences for that long."
Quotable: "The end result of this is slowness, unthoughtful risk aversion, failure to experiment sufficiently, and consequently diminished invention."

**[28] Maggie Stewart (Statsig) - "Product experimentation best practices" (Statsig blog, 2024-07-10).** vendor. **fetched-and-verified.**
`https://www.statsig.com/blog/product-experimentation-best-practices`
Supports: A ratio metric's overall value can move in a direction opposite to the change in its own numerator and denominator, a hazard in reading a readout's reported ratio rather than a question of the comparison's validity
Quotable: "Ratio metrics require extra attention. It's possible for the overall value of the ratio to move in a direction that is opposite to the change in the absolute numerator and denominator values. It's always good practice to check the numerator and denominator separately to understand the true effect."
