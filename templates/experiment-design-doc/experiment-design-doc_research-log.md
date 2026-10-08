# experiment-design-doc: research log

Research conducted 2026-10-08, building on an admission sweep run on 2026-10-05 while the spec was written. The
build's six-dimension fan-out covered the product-experimentation canon, the statistical core (minimum detectable
effect, sample size, duration and the decision rule), the academic preregistration and public-sector evaluation
lineages, contested practice, the boundaries with this library's neighbours and with in-tool experiment surfaces, and
the standing gap question. **35 sources are recorded below, all fetched-and-verified.** Only `fetched-and-verified`
sources are quoted anywhere in this bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a retrieval tool
returns: pages as downloaded and PDFs through a text extractor. Every page first cached during this build was checked a
second time against a fresh download, so no quotation can pass against a copy an agent stored. The agents returned 324
quotations in their quotable fields. 301 passed as returned, and 14 more are verbatim apart from a rendering artifact,
such as a space before punctuation where a link closed. Of the other 9, two are field labels too short for the checker
("By:" and "Win"), which a reading of the raw page confirms. Two were interrupted in the source by a citation marker
("[23]", "[10]"), one by an invisible character, and two by a formula typeset in LaTeX. One was a list into which the
agent had added commas. Each of those is quoted below in its verbatim parts. The last was a sentence from this library's
own spec, filed by an agent as a quotation from Fishman, and it was dropped. Claims the agents made in their findings
prose rather than their quotable fields were checked the same way where this log relies on them; see the next
section. Dashes inside quotations are written as hyphens, as the house rule requires. **235 quotations remain in the
source entries below: 216 pass as normalized substrings, and 19 pass only with whitespace ignored**, because a PDF's
text layer drops its spaces ([20]) or a page splits a sentence across markup ([4], [9], [21], [22], [29], [32], [33]).

---

## What the checks caught, and what was not read

**An agent's frequency claim about Fishman is not on Fishman's page.** One dimension reported that Fishman "reports that
most experiment failures trace back to one of these five" elements. The string is absent from [7]. What [7] says is
different: "it's not a failed experiment if the treatment underperforms control, but it IS a failed experiment if you
can't learn something reliable due to poor design." The frequency claim is dropped, and the bundle must not make it.

**The Atlassian template's four-part order is now read in raw text.** The spec flagged the ordering as "this spec's own
reading of a WebFetch summary, not independently raw-checked." [8] carries it verbatim: "1 Cover the basics", "2 Set a
plan for your experiment", "3 Outline your results", "4 Draw conclusions". The spec needs a dated note when this bundle
lands.

**GrowthBook's skills repository is MIT-licensed.** The spec recorded the licence as unverified until someone read the
repository's own `LICENSE` file. [2] is that file, and it reads "MIT License" and "Copyright (c) 2026 GrowthBook". The
spec's licence table needs a dated correction at landing.

**OSF's licence line is printed with a letter O.** The spec reported that a re-check found "Licensed Under" but not the
fuller CC0 phrase. [18] reads "This Article Is Licensed Under CCO For Maximum Reuse.", with the letter O where a zero
would be expected, which is why a search for "CC0" missed it. Treat the article as offered for reuse under CC0, and
quote its line as printed.

**OSF does not name a default template.** The spec quoted "Standard, comprehensive, and general purpose preregistration
form" as OSF's default. [18] says the opposite in plain words: "We do not recommend a specific template as we do not know
the details of your study, your institution's policies (if any), or the standards of your community." "Most commonly
used" is the nearest it comes. The spec's wording needs a dated note at landing.

**The Magenta Book's licence line is on the HTML edition, not the PDF.** The PDF URL the spec cites redirects to the
current (May 2026) edition, and its extracted text carries no licence statement. [19], the HTML edition of the same
guidance, carries every passage this log quotes and the Open Government Licence line, so it is the edition cited.

**Test, Learn, Adapt's text layer drops its spaces.** The PDF's extracted text runs words together ("Decideon the
randomisation unit"). Its nine steps were checked with whitespace ignored, and all nine pass. The lineage dimension read
the paper in full but filed it as referenced rather than owned; this log owns it as [20].

**One field list was attributed to the wrong vendor.** The boundaries dimension gave Statsig's templates feature the
same list of preconfigured fields as GrowthBook's. That list is [31]'s. [30] says what Statsig's templates are for
("codify a blueprint for config creation") and names no field list. The companion uses [31] for the list.

**The gap dimension read sources other dimensions owned.** It read [7], [9], [10], [16] and [22] despite an instruction
not to. Its extracts were checked like every other, and its verified quotations are merged into the owners' entries
below: one entry per source.

**The ICSE-SEIP paper is quoted by item name only.** [15] is an authors' preprint marked "Not for redistribution".
Anything this bundle takes from it beyond checklist item names and section titles is paraphrased.

**The spec cites the OKRs period at the wrong line.** It points at `okrs_example.md:3` for the period field; the field
is at line 4 ("FY26 Q3 (August to October 2026)"). The fact is unchanged.

**What was not read.** Reforge was excluded: its page renders only with JavaScript, and two earlier attempts failed. Jiang,
Martin and Wilson's "Who's the Guinea Pig?" (ACM FAT* 2019), the paper most directly on ethics review for product A/B
tests, returned HTTP 403. An arXiv paper on novelty and primacy effects, Amplitude's pre-launch checklist post, Statsig's
variance-reduction documentation and Atlassian's DACI page were found by search and not read. The Magenta Book's Annex A,
which it names as the place its terms are defined, and its transparency annex were not read, so this bundle does not
define "protocol" or "statistical analysis plan" beyond what [19]'s body says. AsPredicted's terms of use, OSF's
per-template documents, Optimizely's QA checklist spreadsheet and Amplitude's linked brief template file were not opened.
Kohavi, Tang and Xu's book *Trustworthy Online Controlled Experiments* was not read; it is not cited.

---

## The admission record

**[ADR 0030](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md)'s test is met several times
over, in three lineages.** A named source publishing the type as a written document is sufficient, and this log has more
than one in each lineage.

- **Product experimentation.** [3] names the document type outright: "Experiment design documents contain the
  definition of why you are running this test and the decisions you want to make based on its outcomes." [1] ships a
  fill-in "Experiment spec" block. [5] names an "Experiment design document template". [6] publishes an "Experiment
  Brief" with a linked template, [7] a four-part experiment document, and [8] a Confluence template created by
  Optimizely.
- **Academic preregistration.** [17] is a filed preregistration on AsPredicted's eight-question form, and [18] lists
  OSF's named preregistration templates.
- **Public-sector evaluation.** [19] requires "evaluation plans, protocols and statistical analysis plans" to be
  "completed before the evaluation begins, time-stamped, and preserved within the department". [20] sets out the steps
  of designing a randomised trial.

**The family is `experimentation-docs`, `phase: measure`, by
[ADR 0066](../../docs/internal/decisions/0066-adopt-experimentation-docs-family-contract.md).** Nothing read here
contradicts the contract's membership test. Every product source places the document before launch ([1] "before it's
launched", [3] "before you run them") and ties it to a decision ([3], [6], [7], [11]). That is the contract's "plans or
reports on one discrete test of a hypothesis".

**Licences decide what this bundle may adapt.** [1] is MIT-licensed through its repository's `LICENSE` file ([2]), so
its spec block may be adapted with attribution and the MIT notice. [19] and [20] are Crown copyright under the Open
Government Licence ([20]: "You may reuse this information (not including logos) free of charge in any format or medium,
under the terms of the Open Government Licence."), so their wording may be adapted with attribution. [18] offers itself
for reuse under CC0, printed "CCO". [15] is marked "Not for redistribution": paraphrase it, never reproduce it. Every
other source states no licence on the page read: quote it briefly, never adapt it.

---

## Claims flagged contested or time-bound

1. **One document or two.** [6], [7] and [8] keep the plan and the results in one document: [6] closes with "Phase 4:
   Analyze and Decide", [7]'s four parts run "The Why The Plan The Results The Checklist", and [8]'s third step is
   "Outline your results". [1], [3], [4] and [5] are design-only: [1] "Does not create the experiment in GrowthBook" and
   hands off to a separate launch reference, and neither Optimizely deliverables list holds a results artifact. [21]'s
   hypothesis page links to "Analyze Results" as a separate page under "Related Resources", which is a structural
   signal and not an argued position. No source argues either side. The maintainer ruled for two bundles (ADR 0066), following the
   `qa-docs` pair; the guide tells a one-document team how to use this bundle anyway.
2. **The hypothesis sentence.** This log records four distinct published forms. If-then-because appears in [1] ("If we
   change X, then Y will improve, because Z."), [3] and [27]. [6] uses four slots ("We observed:", "By:", "We expect:",
   "Leading to:"). [7] uses a two-sentence form that names its own refutation. [21] uses "Doing this ... for these
   people/personas should result in a change in their behavior, as measured by success metrics." No source argues one
   form is correct. The spec's fifth form, attributed to the ICSE paper, was not re-verified here, because [15] may be
   quoted by item name only.
3. **Whether the statistical framework is chosen per test or per program.** [23] argues for one framework for the whole
   program: "Supporting both modes of inference would require different planning, different monitoring, different
   interpretation, and possibly different-looking outputs." [25] frames the choice per test, as a trade between
   confidence and time ("If we want 95% confidence, we need 6 weeks. If we are willing to act on 80% Bayesian
   probability, we can decide in 3 weeks."). The two are not reconciled by any source. [23] also undercuts a clean
   three-way choice: "The mixture Sequential Probability Ratio Test, one of the most well-known frequentist sequential
   procedures, is exactly the Bayes factor stopping under the same prior." [23] is dated 2026-09-08 and states Spotify's
   current position ("For Spotify today, it does not."); treat it as time-bound.
4. **Overlap with experiments running at the same time.** [15] lists "Overlap with related experiments is handled" among
   its design checks, and [3]'s roadmap asks whether an experiment belongs in a set of mutually exclusive experiments
   ("Layers"). [32] and [34] argue the opposite emphasis: [32] "Research from Microsoft has shown that in practice
   interaction effects are vanishingly rare", and [34] "meaningful interactions are actually quite rare". [32]'s claim is
   its own report of research this log did not read; attribute it to [32].
5. **How long a test runs.** [10] reports Microsoft's own norm, "the typical duration of an A/B test is 7 days". [16] and
   [9] derive duration from the effect size, variance and traffic. These are compatible (a norm can be a floor), but a
   companion must not present seven days as a field convention.
6. **How many primary metrics.** [14]: "typically one per test". [1]: "ideally one, two max". [21]: "Many experiments
   use one or two success metrics and a few guardrail metrics." All three warn against many; none agrees on exactly one.
7. **Who owns the document.** [25] splits it: "The PM owns the product decision. The experimentation team owns the
   methodology and the rigor." [7] lists several "Experiment owners", and [8] names an owner, reviewers and approvers as
   separate fields. [27] gives the product manager the final call on which experiments to run, which is prioritisation,
   not authorship. No source gives the document to a single role.
8. **What a null result is.** [22] treats an adequately powered null as a success ("Neutral but informative"), and [11]
   asks teams to settle "the decision from a null experiment" in advance. [8]'s template offers "inconclusive" as a
   conclusion to record. These agree that a null must be decided on; they differ on what it is called.
9. **Time-bound figures.** [22]'s learning rate (64%) and win rate (about 12%) are Spotify's own figures for two of its
   organisations, published in 2025. [26]'s "many decisions are made at the 95% confidence level" describes Netflix as
   reported in 2022. Neither is a field norm.

---

## Notes for the companion

### Honest framing

An experiment design document is written before a product experiment launches, and it exists to fix, while nobody has
seen any data, the decisions a team would otherwise make after seeing it. [3] puts the purpose in one sentence:
"Experiment design documents contain the definition of why you are running this test and the decisions you want to make
based on its outcomes." [7] gives the reason in a practitioner's words: "It's really important to put a stake in the
ground before you run the experiment and call out how you will make decisions based on the results." [16] shows what
goes wrong without it. Significance calculations assume "that the sample size was fixed in advance", and a team that
stops when the numbers look good makes "all the reported significance levels become meaningless".

The sources agree on a core: a hypothesis, the variants and who sees them, a primary metric and guardrails, an effect
size and the sample or duration it implies, and what will be done with each outcome. Past that core they disagree: on
whether the plan and the results share one document, on how the hypothesis sentence should read, on whether the
statistical framework is chosen per test or once for the whole program, and on whether overlap with concurrent tests
needs designing around. The same discipline appears in two older traditions, academic preregistration ([17], [18]) and
public-sector evaluation ([19], [20]), which add machinery a product team does not need: a public, time-stamped,
read-only record, and in UK government a mandatory registry.

**No source measured whether writing a design document improves an experiment's outcome.** [22] reports that "adding
experiment reviewers can drastically impact learning rates", as something Spotify has "seen", not a controlled
comparison, and it is about review rather than the document. The companion says plainly that the case for the document
rests on practitioners' testimony and on the statistics of peeking, not on a measurement of the document itself.

### The evidentiary spine, section by section

The template's sections are the spec's; the sourcing below is this log's, and it replaces the spec's sourcing where the
two differ.

- **Hypothesis.** The forms: contested item 2. That it must be falsifiable: [15]'s item "Experiment hypothesis is
  defined and falsifiable", [21] ("clear about what experiment outcomes would support or weaken it"), and [7]'s "our
  hypothesis will be refuted if we observe this other change". **The evidence behind it belongs here too** (see the gap
  result below): [7]'s "Supporting evidence" field ("This is a very important aspect of your experiment document."), [6]'s
  "We observed: Document the qualitative, quantitative, or competitive insight", [21]'s "grounded in past
  research/learnings", and [35]'s graded scale ("There is only one way to calculate confidence - looking for supporting
  evidence."). The field is left free text, as the spec's POSITION, because no source converges on one form.
- **Population, Variants, and Allocation.** Who is eligible and how traffic splits: [3] ("Audience: the target
  population for your experiment and the logic you use to identify it."; "Variations: how many variations this
  experiment uses, and what percentage of traffic each is assigned."), [6] ("Split: This could be 50/50"; "Audience
  cohort"), [1] ("Default to two: control (current state) and treatment (the change). Three or more variations are valid
  but cost statistical power"). **The randomization unit is named explicitly here** (see the gap result): [7] lists it
  first among "The five critical elements of experiment design", [9] warns that the unit is a real choice ("Pay
  attention to the choice of the randomization unit for the A/B test. All identifiers have some limitations and we
  cannot test all features with a single randomization unit.") and names network effects as the reason ([9]: "the
  stable unit treatment value assumption (SUTVA) ... is violated"), and [20] makes it a numbered step of its own ("Decide
  on the randomisation unit"), from the public-sector lineage.
- **Primary and Guardrail Metrics.** **This section leads with what the PRD does not already ship**: the baseline, the
  expected movement, and the margin each guardrail may not cross. The PRD's Success metrics section
  (`templates/prd/prd_template-full.md:192-207`) already names a primary metric, a guardrail and a window. Sources: [1]
  ("Pick goal metrics (ideally one, two max)."; "Pick guardrails (1-3)."; the spec block's "baseline"), [14] ("The
  primary metric is the main measure of success in an experiment, typically one per test."; "Guardrail metrics monitor
  for unintended harm."; "non-inferiority tests"), [10] (guardrails "Measure aspects of the product that we don't want
  to degrade but won't necessarily improve"), [21] (a guardrail hypothesis states "non-inferiority margins"), [15] (the
  item "Metrics and their expected movement are defined"), and [6] (separate metric lists "For Hypothesis Tests" and
  "For Do No Harm Tests"). The multiple-metrics danger: [14]'s three fragments, used separately and never joined ("the
  more metrics analyzed, the greater the chance of observing a" / "significant" / "result that is actually random
  noise"), and [13] ("multiple-comparison problems (adding so many metrics or slicing the data until it shows what you
  want to see)").
- **Minimum Detectable Effect and Sample Size or Duration.** The single non-duplicated core this bundle carries. [16]'s
  rule of thumb (n equals 16 times the variance over the square of the effect, where the effect "is the minimum effect
  you wish to detect" and the variance "is the sample variance you expect"), with "Committing to a sample size completely
  mitigates the problem described here."; [9] ("power calculation sets a lower bound on the number of randomization units
  that will be directly affected by the A/B test"); [1] ("MDE", "Estimated sample size", "Estimated duration"); [6]
  ("Total Sample Size", "Minimum Detectable Effect", "Duration (days)"); [3] ("Sample size: how much traffic you need
  before you can check your results and determine an outcome."); [15]'s item "Effect size and experiment duration are
  set". **The stopping rule is fixed here as well**: [16] ("Decide on a sample size in advance and wait until the
  experiment is over"; "Sequential experiment design lets you set up checkpoints in advance"), and [10] ("we recommend
  running the test until the end of its pre-determined duration"). Which framework (fixed horizon, sequential,
  Bayesian) is contested item 3: the section asks the author to state the one the team's platform uses, and does not
  choose for them. **No power or significance level is a convention in this bundle.** No owned source states one as a
  field norm; [25]'s 95% and 80% and [26]'s 95% are one practitioner's example and one company's practice.
- **Decision Rule.** [11] names the practice and its form: "decision pre-registration", "think through as a team what
  data would imply what decisions and write down quantitative thresholds", and "We will do [A] if [metric X > 1%] and
  [metric Y is > -1%]." Every outcome gets an action: [6] ("Actions: What actions will you take based on each of the
  following outcomes of the test?", over "Win", "Lose" and "Flat"), [7] ("Post Experiment Decisions (aka If This Works
  We Should)"), [4] ("Parameters for significance and lift that indicate the change is implemented permanently."). **The
  null outcome is decided here too** (see the gap result): [11] ("the decision from a null experiment"), [22] ("Neutral
  but informative: No effect but the test was strong enough to detect one if it existed → Iterate, abandon, or ship if
  infra-only."). **The early stop for harm belongs here**: [11] ("Guardrail metrics answer the question "what results
  would be bad enough that we end an experiment early?""). **Who decides is named**: [11] wants the discussion held with
  the "decision-maker", and [25] has the PM set "the decision criteria". "Ship, iterate or stop" is the contract's own
  wording, a POSITION; [22]'s "Iterate, abandon, or ship" is the closest wording any source uses, for one outcome class.
- **Tracking and Instrumentation Note** (full). A pointer, not a restatement: the PRD's Analytics and instrumentation
  section (`templates/prd/prd_template-full.md:209-223`) already lists the events. What the design document adds is which
  events feed which metric, the experiment's own exposure event, and a check that tracking works before launch: [1]
  ("Tracking key suggestion"), [6] ("Experiment Event Name", "Experiment Event Parameters", "Ensure tracking in analytics
  is working:"), [15] ("Telemetry data can be collected").
- **Validity Pre-Commitments** (full). The section's name and grouping are the library's own POSITION: no source names
  such a section in a design document. Its content is sourced, item by item. Sample ratio mismatch: [12] ("A sample ratio
  mismatch is a statistically significant gap between the traffic split you configured and the split your experiment
  produced."), [10] ("SRMs typically invalidate the A/B test and make any results and metric movements untrustworthy.").
  Peeking: [16], [13] ("peeking (deciding on an experiment before it's completed)"). Shutdown for harm: [15] ("Criteria
  for alerting and shutdown are configured"), [10] ("Setting up auto-shutdown for A/B tests that significantly degrade
  the product or the user experience will resolve issues as soon as they are detected"). Ramp-up: [9] ("An experiment
  can be first exposed to 1% of the traffic and gradually ramped-up to 5%, then 10% until the desired final traffic is
  achieved."). Novelty effects and segments fixed in advance: [10] ("We usually compute the metric set segmented by each
  date in the test's period."; "At ExP, we recommend "static" segments that rarely get affected by treatment"). Overlap
  with other experiments, as contested item 4: [15], [3], against [32] and [34]. Risks and who must be told: [7] ("You can
  also use this as a way to identify what other teams might need to be aware of the experiment and its risks.").

**Frontmatter, not a section: the owner, the reviewers, the decision-maker and the status.** [8] fills "the experiment
owner, reviewers, approvers, and the status" in its top table. [7] has "Experiment owners", [15] the item "Experiment
owners are known", and [3] a status of "still being drafted, is running, is being analyzed after collecting data, or is
complete". The planned start date and duration also belong in frontmatter ([3]: "The date your experiment will start.";
"How long your experiment will run.").

**Sizes.** `[lean, full]`, lean the default. [4] and [5] are the direct evidence: the basic plan is for teams starting
out ("If your team is starting to run its first tests, see the basic experiment plan."), and the advanced plan adds an
"Experiment design document template" and a QA checklist for teams whose "experimentation program is more mature". From
the public-sector lineage, [19] states the same principle as proportion: "For smaller or lower-risk evaluations, a short
study registration may be sufficient. For larger, more resource-intensive or higher stakes evaluations, pre-registration
should normally include a full evaluation protocol and a pre-registered statistical analysis plan." [7] concedes the
same at field level ("some elements of this section will be overkill"). The lean variant carries the five sections that
make a decision possible; the full variant adds the two that make the result trustworthy at scale.

**When not to write one, for the guide.** [7] ("Not everything needs to be run as an experiment. A lot of product teams
over-rely on experiments, which can be quite costly."; "If you're going to ship a change regardless of the experiment
results, save yourself the complexity and skip the experiment"), [27] (startups often lack "the traffic required to
generate results that are statistically significant in any meaningful way"), [24] (cheaper validation first: "By
fixating on experiments many companies set the bar too high"), and [26] ("creative shows cannot be properly A/B tested").
No source read names an ethics concern as a reason not to run a test; the one paper on point returned HTTP 403.

**One document or two, for the guide.** Contested item 1. The guide tells a team that keeps one living experiment
document that this bundle's sections are its first half, and that the `experiment-readout` bundle (built next, not yet
shipped) is its second.

### The gap question's result, and what this build does with it

Dimension 6 searched for what a good design document does beyond the commonest sections. Each candidate went through
[decision procedure 12](../../docs/internal/decision-procedures.md#12-a-property-or-section-is-proposed-for-a-template).

- **The randomization unit: adopted, inside Population, Variants, and Allocation, lean.** E1, sourced by [7], [9], [20]
  and, at execution, [15]'s "Randomization quality is sufficient". E3, homed: it is part of who is assigned to what. E4:
  one line, so lean.
- **The evidence behind the hypothesis: adopted, inside Hypothesis, lean.** E1: [7], [6], [21], [35]. E3: it is why the
  hypothesis is worth testing, so it sits with the hypothesis.
- **What a null result will mean: adopted, inside Decision Rule, lean.** E1: [11], [22], and [6]'s "Flat". E3: a null is
  an outcome, and the decision rule is where outcomes get actions.
- **Ramp-up, alerting and shutdown: adopted, inside Validity Pre-Commitments, full only.** E1: [9], [10], [15]. E3: the
  library's `launch-coordination-checklist` and `production-readiness-review` cover a release, not one test's traffic, so
  the test's own design document is the home. E4: full only, because a small test with a simple flag does not need it.
- **Novelty effects and segments fixed in advance: adopted, inside Validity Pre-Commitments, full only.** E1: [10].
- **Overlap with concurrent experiments: adopted as an ASK in Validity Pre-Commitments, full only, labelled contested.**
  E1 is met by [15] and [3]; [32] and [34] argue it rarely matters, so the guidance says so.
- **Risks, and who must be told: adopted inside Validity Pre-Commitments, full only.** E1: [7].
- **Whether to run an experiment at all: the guide, not the template.** [7], [24], [27], [26]. It decides whether the
  document is written, not what it contains.
- **Amendments after launch: the guide, as an anti-pattern.** [19], from the public-sector lineage: "Pre-registration does
  not prevent changes being made to an evaluation design, but it requires that amendments to evaluation plans are
  documented and explained." A product document borrows the habit, not the registry, and the guide says which tradition
  it comes from.
- **An ethics or consent review: null result.** No source read in full describes one as a step before a product A/B
  test. The one paper on point returned HTTP 403. The bundle claims nothing about ethics review either way.
- **A named sign-off: folded into frontmatter.** [8]'s owner, reviewers and approvers; [22]'s reviewers ("ideas get
  discussed and scrutinized more before tests start").

### What the lineages lend, and what they do not

From academic preregistration and public-sector evaluation, a product design document borrows the discipline of deciding
before the data: [19] ("documenting key elements of the evaluation such as its objectives, research questions, design,
data collection procedures and analytical approach, before any outcome data is collected or analysed"), [17]'s question
"Specify exactly which analyses you will conduct to examine the main question/hypothesis.", and [20]'s explicit
randomisation unit. It does not borrow their accountability machinery: [18]'s "time-stamped, read-only version of your
study plan to a public repository", [18]'s "Once you submit a registration, you will not be able to edit or make changes
to it", or [19]'s rule that government evaluations "must be registered on the Government Evaluation Registry". Every
borrowed habit names its tradition in the same sentence, per the contract's section 3.6.

### What the bundle must not say

- That Fishman, or anyone, measured how often experiments fail, or why. [7] does not.
- That any power level or significance level (80%, 90%, 95%, 5%) is a convention. Attribute [25]'s and [26]'s figures
  to them, as examples.
- That seven days is a standard duration. It is Microsoft's own typical duration ([10]).
- "Problem Statement" or "Learning Objectives" as Fishman's headings. His are "The problem we are solving" and "What are
  we hoping to learn from this".
- That AsPredicted belongs to Wharton or to the Credibility Lab.
- That OSF names a default template.
- Any definition of "protocol" or "statistical analysis plan" drawn from the Magenta Book's Annex A, which was not read.
- GrowthBook's preconfigured-field list ([31]) as Statsig's.
- That a vendor says its tool's configuration replaces a written design document, or sits beside one. No source in
  [28]-[31] says either; the boundary is the library's, under ADR 0030.
- That interaction effects are rare, as a fact. It is [32]'s and [34]'s position.
- That writing a design document improves an experiment's outcome.
- [14]'s three fragments joined into one sentence.
- Any sentence of [15] reproduced. Item names only.
- Spotify's 64% and 12% as anyone's figures but Spotify's ([22]).
- A clinical or academic reporting standard as product-management practice, or any lineage's habit without naming the
  lineage.
- "Ship, iterate or stop" as a sourced convention. It is the contract's POSITION.
- That GrowthBook's licence is unverified. It is MIT ([2]).
- Any gendered pronoun for a source author. Use the author's name.

### GOOD and WEAK illustrations use their own scenario

Every GOOD and WEAK example in the templates' guidance comments uses a scenario unrelated to the worked example: not
Acme Analytics, not Saved Views, not an adoption nudge or prompt, not a dashboard product, and none of Priya Nair, Dana
Okoro, Marta Reyes, Meridian Freight or the Recurring Analyst. Two earlier builds shipped GOOD text in the worked
example's own scenario (`announcement-internal-comms` and `change-request`, caught after every review lens had passed).

### The example

A design document for the **Saved Views adoption-nudge experiment** at Acme Analytics, dated **2026-07-30**. The test is
a one-time in-app prompt, shown to a Recurring Analyst after their fifth dashboard view following the 2.4.0 release,
suggesting they save their current filter, date range and column setup as a view, against a no-prompt control. It runs
**2026-08-03 through 2026-08-31**, four weeks, and the readout (the next bundle's example) is written 2026-09-04. These
dates were chosen for the spec, not read off a sibling, and the readout's example will report against them.

It must carry these facts from its siblings, exactly, and invent none of them:

| Fact | Value | Source |
|---|---|---|
| Release the test follows | Saved Views shipped in 2.4.0, "Release date: 2026-07-21." | `templates/release-notes/release-notes_example.md:26` |
| Primary metric | Saved Views adoption, "Share of Recurring Analysts using a saved view weekly" | `templates/kpi-dashboard/kpi-dashboard_example.md:54` |
| Starting value | 41%, KR2's starting figure, also the KPI dashboard's current value at its `last_reviewed: "2026-07-20"` | `templates/okrs/okrs_example.md:52`; `templates/kpi-dashboard/kpi-dashboard_example.md:6,54` |
| Target the test serves | 60% by end Q3; the OKRs' period is "FY26 Q3 (August to October 2026)" | `templates/kpi-dashboard/kpi-dashboard_example.md:54`; `templates/okrs/okrs_example.md:4,52` |
| Metric owner and document owner | Priya Nair, "PM, Reporting" | `templates/kpi-dashboard/kpi-dashboard_example.md:54`; `templates/prd/prd_example.md:5` |
| Guardrail 1 | Weekly active analysts, hold >= 480 (495 at the same snapshot) | `templates/kpi-dashboard/kpi-dashboard_example.md:56` |
| Guardrail 2 | Dashboard load error rate does not increase; shared-view permission incidents stay at zero | `templates/prd/prd_example.md:128` |
| Events already instrumented | `view_saved`, `view_switched`, `view_set_default`, `view_shared`, `view_load_error` | `templates/prd/prd_example.md:133-134` |
| Why the nudge exists | The risk register lists "in-product nudge" as a mitigation for R-04, analysts not adopting Saved Views inside the program's 60-day launch-success window | `templates/risk-register/risk-register_example.md:69` (`last_reviewed: "2026-07-20"`) |

**The population is small, and the example must say so.** The KPI dashboard counts 495 weekly active Recurring
Analysts ("Distinct Recurring Analysts active in the trailing 7 days"), which is the population active in any given
week. Over a four-week window the eligible set may be somewhat larger, but it is of that order. Any sample size, minimum
detectable effect or duration the example computes must be consistent with a population of roughly that size, and every
such figure is labelled illustrative. A
test this small can detect only a large effect, and an honest design document states that, and says what the team
will decide if the true effect is smaller than the test can see. If the example randomizes by customer account rather
than by analyst, because a view one analyst shares is visible to colleagues, it says why ([9]'s network effects) and
accepts the smaller effective sample. The example must not invent an account count; if it needs one, it labels it
illustrative.

It must not contain:

1. The OKRs' Initiatives-table status line for Saved Views ("in build, spec at 0.3.0", `okrs_example.md:90`), which
   contradicts the release date. Cite KR2's numbers only.
2. Any of the four residuals PR #204 recorded and left unfixed: the announcement's "private views since late June", the
   retrospective's 2026-09-14 general availability date, the release notes' known issue promising a fix in 2.4.1, and
   the definition of done's "DEF-2291 shipped in build 2.3.2". It must not explain why 41% predates the release.
3. CR-SV-01 (scheduled email delivery for Saved Views) as shipping anything. It was postponed on 2026-08-14 and shipped
   nothing, so no Saved Views change lands inside the test window; the example may say so, but need not.
4. Any result. The test has not run on 2026-07-30.
5. The design-partner pilot's result. The risk register names a pilot and a two-week checkpoint but records no outcome.
6. Any document dated after 2026-07-30 cited as existing in body prose. The opening "Worked example" blockquote may
   mention the readout.

Its primary metric is KR2's adoption share, not the PRD's primary metric (time to first meaningful interaction), and
it says why in one line: the nudge targets adoption.

---

## Sources

### CANON: WHAT VENDORS AND PRACTITIONERS PUT IN A WRITTEN EXPERIMENT DESIGN DOCUMENT

**[1] GrowthBook - "experiment-design" skill reference (skills/experiments/references/experiment-design.md).** vendor. **fetched-and-verified.**
`https://github.com/growthbook/skills/blob/main/skills/experiments/references/experiment-design.md`
Supports: A fill-in "Experiment spec" block and its field order (hypothesis, variations, primary metric with baseline, guardrails, MDE, estimated sample size, estimated duration, project, tracking key); the if-then-because hypothesis form; default of two variations; one or two goal metrics and one to three guardrails; the document is pre-launch and design-only, handing off to a separate launch reference
Quotable: "Help the user design a well-formed GrowthBook experiment before it's launched."
Quotable: "Does not create the experiment in GrowthBook."
Quotable: "Falsifiable, if/then/because format: If we change X, then Y will improve, because Z."
Quotable: "Define variations. Default to two: control (current state) and treatment (the change). Three or more variations are valid but cost statistical power"
Quotable: "Pick goal metrics (ideally one, two max)."
Quotable: "Pick guardrails (1-3)."
Quotable: "**Hypothesis:** If <change>, then <outcome>, because <mechanism>."
Quotable: "**Estimated duration:** <D> days at <T> visitors/day on the affected surface"
Quotable: "**Tracking key suggestion:** <kebab-case-name>"
Quotable: "Ask the user to confirm before handing off to references/experiment-launch.md."

**[2] GrowthBook - skills repository LICENSE file.** vendor. **fetched-and-verified.**
`https://raw.githubusercontent.com/growthbook/skills/main/LICENSE`
Supports: The repository that ships [1] is MIT-licensed, so [1]'s structure may be adapted with attribution and the MIT notice
Quotable: "MIT License"
Quotable: "Copyright (c) 2026 GrowthBook"

**[3] LaunchDarkly - "Designing experiments" (guide).** vendor. **fetched-and-verified.**
`https://launchdarkly.com/docs/guides/experimentation/designing-experiments`
Supports: Names the document type and its purpose; the if-then-because form; the full pre-launch field list (name, description, hypothesis, sample size, audience, variations with traffic share, metrics, location, layers, holdouts, start date, duration, status, priority); the status vocabulary; design-only scope
Quotable: "It is critical to plan out and document experiments before you run them. Experiment design documents contain the definition of why you are running this test and the decisions you want to make based on its outcomes."
Quotable: "If [I make a specific change to our codebase], then [one or more measurable metrics will improve] because [the change had this effect]."
Quotable: "Your roadmap should contain the following:"
Quotable: "Sample size: how much traffic you need before you can check your results and determine an outcome."
Quotable: "Audience: the target population for your experiment and the logic you use to identify it."
Quotable: "Variations: how many variations this experiment uses, and what percentage of traffic each is assigned."
Quotable: "Layers: whether the experiment should be part of a set of mutually exclusive experiments."
Quotable: "Holdouts: whether to include the experiment in a running holdout."
Quotable: "The date your experiment will start."
Quotable: "How long your experiment will run."
Quotable: "Status: whether your experiment is still being drafted, is running, is being analyzed after collecting data, or is complete."

**[4] Optimizely - "Create a basic experiment plan" (Experimentation Strategy docs).** vendor. **fetched-and-verified.**
`https://docs.optimizely.com/experimentation-strategy/docs/create-a-basic-experiment-plan`
Supports: A lightweight plan for teams starting out, its questions and materials, a pre-set significance and lift threshold for the ship decision, stakeholder review before build, and a pointer to the advanced plan for mature programs; evidence for a lean variant
Quotable: "Why you are running this experiment (hypothesis)."
Quotable: "Who you want to see this experiment."
Quotable: "How you measure success."
Quotable: "Parameters for significance and lift that indicate the change is implemented permanently."
Quotable: "review and update the plan with stakeholders"
Quotable: "If your experimentation program is more mature, see the advanced experiment design template and QA checklist."
Quotable: "Create this plan as a shareable document that multiple stakeholders can reference. For example, you can create this document as a presentation slide, an email template, or a wiki page covering basic test information."

**[5] Optimizely - "Create an advanced experiment plan and QA checklist" (Experimentation Strategy docs).** vendor. **fetched-and-verified.**
`https://docs.optimizely.com/experimentation-strategy/docs/create-an-advanced-experiment-plan-and-qa-checklist`
Supports: What the advanced plan adds over the basic one (an "Experiment design document template" with implementation, ownership and goal fields, and a separate QA checklist); evidence for a full variant
Quotable: "A full experiment plan gathers decisions from stakeholders into a single, collaborative document. It provides a detailed summary of the motivations and mechanics of your experiment or campaign."
Quotable: "Experiment design document template"
Quotable: "Your experiment design document should include:"
Quotable: "Roles/responsibilities"
Quotable: "Primary, secondary, and monitoring goals"
Quotable: "Correlating goals to business value"
Quotable: "QA checklist template"
Quotable: "If your team is starting to run its first tests, see the basic experiment plan."

**[6] Bhavik Patel (Amplitude) - "Use Experiment Briefs to Design Better Experiments".** vendor. **fetched-and-verified.**
`https://amplitude.com/blog/experiment-brief`
Supports: A four-phase "Experiment Brief" (Plan, Configure, Monitor, Analyze and Decide) that keeps plan and results in one document; its four-slot hypothesis form; separate metric lists for hypothesis tests and do-no-harm tests; sample size, MDE and duration fields; an action decided in advance for each outcome (win, lose, flat); an experiment event and a tracking check
Quotable: "Phase 1: Plan"
Quotable: "We observed:"
Quotable: "Document the qualitative, quantitative, or competitive insight"
Quotable: "By:"
Quotable: "We expect:"
Quotable: "Leading to:"
Quotable: "For Hypothesis Tests"
Quotable: "For Do No Harm Tests"
Quotable: "Total Sample Size"
Quotable: "Minimum Detectable Effect"
Quotable: "Experiment Event Name"
Quotable: "Experiment Event Parameters"
Quotable: "Actions: What actions will you take based on each of the following outcomes of the test?"
Quotable: "Win"
Quotable: "Lose"
Quotable: "Flat"
Quotable: "Split: This could be 50/50"
Quotable: "Audience cohort: Are we targeting existing customers, new users, etc.?"
Quotable: "Duration (days)"
Quotable: "Ensure tracking in analytics is working:"
Quotable: "Phase 4: Analyze and Decide"
Quotable: "Decision: Decide next steps based on your planning phase."

**[7] Adam Fishman - "Creating an Experiment Doc" (Fishman AF Newsletter).** practitioner. **fetched-and-verified.**
`https://www.fishmanafnewsletter.com/p/experiment-document-template`
Supports: A four-part experiment document that keeps plan and results together; its named fields (owners, the problem, the hypothesis, what the team hopes to learn, supporting evidence); a two-sentence hypothesis form that names its own refutation; five critical elements of design, the randomization unit first; risks and who to notify; a decision rule fixed before the test; when not to run an experiment
Quotable: "there are four distinct parts to any meaningful experiment document: The Why The Plan The Results The Checklist"
Quotable: "Experiment owners"
Quotable: "The problem we are solving"
Quotable: "What are we hoping to learn from this"
Quotable: "Supporting evidence This is a very important aspect of your experiment document. Here you want to include what other information you have that has informed your thinking."
Quotable: "We believe that this thing will have an impact on the metric because of a belief which was informed by this briefly presented or linked evidence. We will know whether our hypothesis was right when we observe this change in a metric, and our hypothesis will be refuted if we observe this other change."
Quotable: "The five critical elements of experiment design are: Randomization unit Platform Eligibility criteria Assignment criteria Response metric"
Quotable: "it IS a failed experiment if you can't learn something reliable due to poor design"
Quotable: "Post Experiment Decisions (aka If This Works We Should)"
Quotable: "It's really important to put a stake in the ground before you run the experiment and call out how you will make decisions based on the results."
Quotable: "You can also use this as a way to identify what other teams might need to be aware of the experiment and its risks."
Quotable: "notify any important stakeholders"
Quotable: "some elements of this section will be overkill"
Quotable: "Not everything needs to be run as an experiment. A lot of product teams over-rely on experiments, which can be quite costly."
Quotable: "If you're going to ship a change regardless of the experiment results, save yourself the complexity and skip the experiment"

**[8] Atlassian - "Experiment plan and results template" (Confluence; created by Optimizely).** vendor. **fetched-and-verified.**
`https://www.atlassian.com/software/confluence/templates/experiment-plan-and-results`
Supports: A one-document template whose four steps (basics, plan, results, conclusions) are read in raw text; an owner, reviewers and approvers as separate fields; "inconclusive" as a conclusion to record
Quotable: "1 Cover the basics"
Quotable: "The top table of the template has space to outline the basics - including the name of the experiment, the experiment owner, reviewers, approvers, and the status."
Quotable: "2 Set a plan for your experiment"
Quotable: "Provide a high-level overview of the experiment, establish your hypothesis, define your metrics and targets, establish your variations, and include any baseline data or notes you might need to refer to."
Quotable: "3 Outline your results"
Quotable: "Make sure you also assign a clear conclusion (such as "inconclusive" or "hypothesis proved")"
Quotable: "4 Draw conclusions"

### THE STATISTICAL CORE: EFFECT SIZE, SAMPLE SIZE, DURATION, THE DECISION RULE AND VALIDITY

**[9] Microsoft Experimentation Platform (ExP), pre-experiment stage - "Patterns of Trustworthy Experimentation: Pre-Experiment Stage".** primary (Microsoft Research). **fetched-and-verified.**
`https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/`
Supports: Power sets a lower bound on randomization units; the hypothesis carries its metrics; the randomization unit is a real design choice constrained by network effects; a gradual safe rollout trades risk against the cost of exposure
Quotable: "the hypothesis should also include a set of metrics to measure the impact of the change"
Quotable: "power calculation sets a lower bound on the number of randomization units that will be directly affected by the A/B test"
Quotable: "Pay attention to the choice of the randomization unit for the A/B test. All identifiers have some limitations and we cannot test all features with a single randomization unit."
Quotable: "Network Effects: When product changes impact both the user and their collaborators/connections, the stable unit treatment value assumption (SUTVA) ... is violated."
Quotable: "This introduces a tradeoff between risk and certainty. If a change is indeed not desirable, exposing it to a large number of users will increase the cost."
Quotable: "Our solution is to perform a safe rollout ... where the treatment is tested gradually across various user populations or rings, and gradually increasing percentages within a user population."
Quotable: "An experiment can be first exposed to 1% of the traffic and gradually ramped-up to 5%, then 10% until the desired final traffic is achieved."

**[10] Microsoft Experimentation Platform (ExP), during-experiment stage - "Patterns of Trustworthy Experimentation: During-Experiment Stage".** primary (Microsoft Research). **fetched-and-verified.**
`https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/`
Supports: Microsoft's own typical duration; peeking and multiple testing; running to the pre-determined duration; sample ratio mismatch and its consequence; guardrail definition and alerts; auto-shutdown; date-segmented analysis for novelty effects; static segments
Quotable: "the typical duration of an A/B test is 7 days"
Quotable: "we need to account for multiple hypothesis testing and early peeking in our statistical methods"
Quotable: "At ExP, to make early results more trustworthy, we require stronger statistical significance levels and in the absence of highly certain metric movements, we recommend running the test until the end of its pre-determined duration and adopt the metric movements observed then."
Quotable: "SRMs occur when the number of users in treatment and control are not balanced and their ratio doesn't satisfy the expected ratio."
Quotable: "SRMs typically invalidate the A/B test and make any results and metric movements untrustworthy."
Quotable: "Measure aspects of the product that we don't want to degrade but won't necessarily improve"
Quotable: "At ExP, we recommend that a feature crew set up alerts for their business-critical metrics: Guardrails (e.g. page load time, error rates) and OECs (e.g. user satisfaction metrics)."
Quotable: "Setting up auto-shutdown for A/B tests that significantly degrade the product or the user experience will resolve issues as soon as they are detected, instead of relying on (a possibly delayed) manual intervention."
Quotable: "dictated that we look deeper. We usually compute the metric set segmented by each date in the test's period."
Quotable: "This was evidence of a novelty effect where users were getting confused and clicking repeatedly on the button."
Quotable: "At ExP, we recommend "static" segments that rarely get affected by treatment, where the user remains in the same segment value throughout the A/B test."

**[11] Eppo - "Make Decisions Before Experimenting" (blog).** vendor. **fetched-and-verified.**
`https://www.geteppo.com/blog/make-decisions-before-experimenting`
Supports: Decision pre-registration, its "We will do" form, guardrails as the early-stop question, holding the discussion with the decision-maker, and deciding the null outcome in advance
Quotable: "decision pre-registration"
Quotable: "think through as a team what data would imply what decisions and write down quantitative thresholds"
Quotable: "We will do [A] if [metric X > 1%] and [metric Y is > -1%]."
Quotable: "Guardrail metrics answer the question "what results would be bad enough that we end an experiment early?""
Quotable: "the decision from a null experiment"
Quotable: "decision-maker"
Quotable: "Write up the decision pre-registration."

**[12] GrowthBook - "Sample Ratio Mismatch (SRM): Types, Causes, and How to Identify" (blog).** vendor. **fetched-and-verified.**
`https://www.growthbook.io/blog/sample-ratio-mismatch`
Supports: The definition of sample ratio mismatch and the test that detects it
Quotable: "A sample ratio mismatch is a statistically significant gap between the traffic split you configured and the split your experiment produced."
Quotable: "A chi-squared goodness-of-fit test detects an SRM by comparing the observed unit counts to the expected ones and returning a p-value"

**[13] GrowthBook - "Experimentation Program Mistakes to Avoid" (blog).** vendor. **fetched-and-verified.**
`https://www.growthbook.io/blog/experimentation-program-mistakes-to-avoid`
Supports: Peeking and multiple comparisons named as statistics mistakes in an experimentation program
Quotable: "peeking (deciding on an experiment before it's completed)"
Quotable: "multiple-comparison problems (adding so many metrics or slicing the data until it shows what you want to see)"

**[14] GrowthBook - "KPI Playbook: A/B Testing Metrics" (blog).** vendor. **fetched-and-verified.**
`https://www.growthbook.io/blog/kpi-playbook-ab-testing-metrics`
Supports: One primary metric that decides launch or rollback; guardrails monitoring for harm through non-inferiority tests; the multiple-metrics problem (as three separate fragments, never joined); a correction for teams that track many metrics
Quotable: "The primary metric is the main measure of success in an experiment, typically one per test."
Quotable: "ultimately determines whether a change should be launched or rolled back"
Quotable: "anchored around a single primary KPI"
Quotable: "Guardrail metrics monitor for unintended harm."
Quotable: "non-inferiority tests"
Quotable: "the more metrics analyzed, the greater the chance of observing a"
Quotable: "significant"
Quotable: "result that is actually random noise"
Quotable: "Benjamini"

**[15] A. Fabijan, P. Dmitriev, H. H. Olsson, J. Bosch, L. Vermeer and D. Lewis - "Three Key Checklists and Remedies for Trustworthy Analysis of Online Controlled Experiments at Scale" (ICSE-SEIP 2019, authors' preprint).** academic. **fetched-and-verified.**
`https://exp-platform.com/Documents/2019%20FabijanDmitrievOlssonBoschVermeerLewis_Three-Key-Checklists_ICSE_SEIP.pdf`
Supports: A pre-launch design checklist and an execution checklist whose item names cover a falsifiable hypothesis, metrics and their expected movement, telemetry, effect size and duration, overlap with related experiments, harm, early stopping, alerting and shutdown, owners, and randomization quality. Marked "Not for redistribution": item names and section titles only; anything else is paraphrased
Quotable: "Not for redistribution"
Quotable: "Checklist 1. Experiment Design Analysis."
Quotable: "Checklist 2. Experiment Execution Analysis."
Quotable: "Experiment hypothesis is defined and falsifiable"
Quotable: "Metrics and their expected movement are defined"
Quotable: "Telemetry data can be collected"
Quotable: "Effect size and experiment duration are set"
Quotable: "Overlap with related experiments is handled"
Quotable: "Experiment is not causing excessive harm"
Quotable: "Possibility of early stopping is evaluated"
Quotable: "Criteria for alerting and shutdown are configured"
Quotable: "Experiment owners are known"
Quotable: "Randomization quality is sufficient"

**[16] Evan Miller - "How Not To Run an A/B Test".** practitioner. **fetched-and-verified.**
`https://www.evanmiller.org/how-not-to-run-an-ab-test.html`
Supports: Repeated significance testing (peeking) and why it invalidates reported significance; a rule-of-thumb sample-size formula driven by the minimum effect and the variance (typeset in LaTeX on the page, so described in words here); committing to a sample size in advance; sequential design as the legitimate way to stop early
Contested/time-bound: The page's worked example of how peeking inflates the false-positive rate (26.1% in its own example) is one illustrative calculation, not a field measurement
Quotable: "repeated significance testing errors"
Quotable: "that the sample size was fixed in advance"
Quotable: "all the reported significance levels become meaningless"
Quotable: "a good rule of thumb"
Quotable: "is the minimum effect you wish to detect and"
Quotable: "is the sample variance you expect"
Quotable: "Committing to a sample size completely mitigates the problem described here."
Quotable: "Decide on a sample size in advance and wait until the experiment is over before you start believing the "chance of beating original" figures that the A/B testing software gives you."
Quotable: "Sequential experiment design lets you set up checkpoints in advance where you will decide whether or not to continue the experiment, and it gives you the correct significance levels."
Quotable: "anyone running web experiments should only run experiments where the sample size has been fixed in advance, and stick to that sample size with near-religious discipline"

### THE OTHER TWO LINEAGES: ACADEMIC PREREGISTRATION AND PUBLIC-SECTOR EVALUATION

**[17] AsPredicted - public sample pre-registration #133868, "AI agent Field Study (The second Batch)".** primary (a filed pre-registration). **fetched-and-verified.**
`https://aspredicted.org/MQQ_B7B`
Supports: The eight numbered questions of AsPredicted's form, in order, on a filed and time-stamped instance; academic-preregistration lineage
Quotable: "1) Have any data been collected for this study already?"
Quotable: "2) What's the main question being asked or hypothesis being tested in this study?"
Quotable: "3) Describe the key dependent variable(s) specifying how they will be measured."
Quotable: "4) How many and which conditions will participants be assigned to?"
Quotable: "5) Specify exactly which analyses you will conduct to examine the main question/hypothesis."
Quotable: "6) Describe exactly how outliers will be defined and handled, and your precise rule(s) for excluding observations."
Quotable: "7) How many observations will be collected or what will determine sample size?"
Quotable: "8) Anything else you would like to pre-register?"
Quotable: "Version of AsPredicted Questions: 2.00"

**[18] Open Science Framework (OSF) Support - "Welcome to Registrations & Preregistrations!".** primary (reference documentation). **fetched-and-verified.**
`https://help.osf.io/article/330-welcome-to-registrations`
Supports: What preregistration is (a time-stamped, read-only public record); OSF's named templates; that OSF recommends no specific template; that a submitted registration cannot be edited; the article's own CC0 line, printed "CCO"; academic-preregistration lineage
Quotable: "Preregistration is the practice of posting a time-stamped, read-only version of your study plan to a public repository before beginning data collection or analysis. This establishes a transparent record of your research intentions."
Quotable: "We do not recommend a specific template as we do not know the details of your study, your institution's policies (if any), or the standards of your community."
Quotable: "Standard, comprehensive, and general purpose preregistration form."
Quotable: "Most commonly used."
Quotable: "Eight questions derived from content recommended by"
Quotable: "Make design and analysis decisions before you view the data"
Quotable: "Once you submit a registration, you will not be able to edit or make changes to it or any associated files."
Quotable: "This Article Is Licensed Under CCO For Maximum Reuse."

**[19] HM Treasury - "The Magenta Book: Central Government guidance on evaluation" (HTML edition, May 2026).** primary (government guidance). **fetched-and-verified.**
`https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html`
Supports: Evaluation plans, protocols and statistical analysis plans completed before an evaluation begins and time-stamped; what pre-registration documents, including power analyses for quantitative evaluations; proportion to the stakes; amendments documented rather than forbidden; the mandatory government registry; Open Government Licence; public-sector evaluation lineage. The PDF URL the spec cites redirects to the same edition and lacks the licence line
Quotable: "all evaluation planning documents - including evaluation plans, protocols and statistical analysis plans - should be completed before the evaluation begins, time-stamped, and preserved within the department"
Quotable: "Pre-registration means documenting key elements of the evaluation such as its objectives, research questions, design, data collection procedures and analytical approach, before any outcome data is collected or analysed."
Quotable: "For quantitative evaluations, pre-registration should also include power analyses and sample size calculations."
Quotable: "Pre-registration does not prevent changes being made to an evaluation design, but it requires that amendments to evaluation plans are documented and explained."
Quotable: "The purpose of pre-registration is to prevent researchers from 'fishing' for significant or positive findings by arbitrarily adjusting the way that data is collected or analysed."
Quotable: "Pre-registration should be applied in a proportionate way."
Quotable: "For smaller or lower-risk evaluations, a short study registration may be sufficient. For larger, more resource-intensive or higher stakes evaluations, pre-registration should normally include a full evaluation protocol and a pre-registered statistical analysis plan."
Quotable: "must be registered on the Government Evaluation Registry"
Quotable: "Open Government Licence"

**[20] Laura Haynes, Owain Service, Ben Goldacre and David Torgerson (Cabinet Office Behavioural Insights Team) - "Test, Learn, Adapt: Developing Public Policy with Randomised Controlled Trials" (June 2012).** primary (government paper). **fetched-and-verified.**
`https://assets.publishing.service.gov.uk/media/5a7488c8e5274a7f9c586c23/TLA-1906126.pdf`
Supports: Nine numbered steps for designing and using a randomised trial, including deciding the randomisation unit and how many units are needed; Open Government Licence; public-sector evaluation lineage. The PDF's text layer drops spaces, so its quotations were checked with whitespace ignored. Reached from the landing page `https://www.gov.uk/government/publications/test-learn-adapt-developing-public-policy-with-randomised-controlled-trials`
Quotable: "Identify two or more policy interventions to compare"
Quotable: "Determine the outcome that the policy is intended to influence and how it will be measured in the trial"
Quotable: "Decide on the randomisation unit: whether to randomise to intervention and control groups at the level of individuals, institutions (e.g. schools), or geographical areas (e.g. local authorities)"
Quotable: "Determine how many units (people, institutions, or areas) are required for robust results"
Quotable: "Assign each unit to one of the policy interventions, using a robust randomisation method"
Quotable: "Measure the results and determine the impact of the policy interventions"
Quotable: "Adapt your policy intervention to reflect your findings"
Quotable: "Return to Step 1 to continually improve your understanding of what works"
Quotable: "Publication date: June 2012"
Quotable: "You may reuse this information (not including logos) free of charge in any format or medium, under the terms of the Open Government Licence."

### CONTESTED QUESTIONS, AND HOW PRODUCT TEAMS PRACTISE EXPERIMENT DESIGN

**[21] Spotify Confidence - "Hypothesis" (product documentation).** vendor. **fetched-and-verified.**
`https://confidence.spotify.com/docs/experiments/design/hypothesis`
Supports: Spotify Confidence's hypothesis form and its criteria; one hypothesis per success metric, and non-inferiority margins for guardrails; the page links to results analysis as a separate page
Quotable: "Related Resources"
Quotable: "Analyze Results"
Quotable: "A well-formulated hypothesis is a specific assumption that can be conclusively tested through an experiment."
Quotable: "a statement, not a question"
Quotable: "clear about what experiment outcomes would support or weaken it"
Quotable: "grounded in past research/learnings"
Quotable: "written with as few assumptions as possible"
Quotable: "Doing this/building this feature/creating this experience for these people/personas should result in a change in their behavior, as measured by success metrics. The data supports the hypothesis if the success metrics change by the minimum detectable effect."
Quotable: "Many experiments use one or two success metrics and a few guardrail metrics. In this scenario you should write a hypothesis statement for each success metric, while for the guardrails it's generally enough to just state the hypothesis that the treatment does not deteriorate the guardrail metrics more than the acceptable margins (known as non-inferiority margins)."

**[22] Michael Bellato, Mårten Schultzberg and Sebastian Ankargren (Spotify Engineering) - "Beyond Winning: Spotify's Experiments with Learning Framework" (2025).** primary (Spotify Engineering). **fetched-and-verified.**
`https://engineering.atspotify.com/2025/9/spotifys-experiments-with-learning-framework`
Supports: A successful experiment defined as valid and decision-ready rather than a win; an adequately powered null as "neutral but informative"; Spotify's own learning and win rates for two organisations; reviewers before tests start, as Spotify's observation rather than a measurement
Contested/time-bound: The 64% and 12% figures are Spotify's own, for its own organisations
Quotable: "A successful experiment yields enough valid information to inform product decisions, not just those that find "winners.""
Quotable: "An Experiment with Learning is one that produces valid and decision-ready results"
Quotable: "At Spotify, we hold a high bar for decision-making: Experiments must be powered across all relevant metrics to count as informative."
Quotable: "Neutral but informative: No effect but the test was strong enough to detect one if it existed → Iterate, abandon, or ship if infra-only."
Quotable: "In the two orgs running ~80% of Spotify experiments, the learning rate is ~64%, but the win rate is ~12%. Most of our learning doesn't come from wins - it comes from discovering what not to ship."
Quotable: "We've seen that small things like adding experiment reviewers can drastically impact learning rates, both because practices improve when there are more eyes on experiments, but also because ideas get discussed and scrutinized more before tests start."

**[23] Mattias Frånberg and Mårten Schultzberg (Spotify Engineering) - "Why Spotify Is Not Using Bayesian A/B Testing" (2026-09-08).** primary (Spotify Engineering). **fetched-and-verified.**
`https://engineering.atspotify.com/2026/9/why-spotify-is-not-using-bayesian-a-b-testing`
Supports: One organisation's reasoned case for choosing the statistical framework once for a whole program, not per test; that "Bayesian" is a family of configurations; that one frequentist sequential test equals one Bayesian stopping rule under the same prior
Contested/time-bound: States Spotify's position as of its date
Quotable: "Historically, all of Spotify's production experiments are analyzed using frequentist statistics."
Quotable: "Supporting both modes of inference would require different planning, different monitoring, different interpretation, and possibly different-looking outputs. So far, the benefit of a second framework doesn't outweigh those costs."
Quotable: "The problem is that Bayesian inference for A/B testing is not one thing. It is a family of configurations, each defined by a stopping rule, a prior, and a likelihood."
Quotable: "The mixture Sequential Probability Ratio Test, one of the most well-known frequentist sequential procedures, is exactly the Bayes factor stopping under the same prior."
Quotable: "Start with the experimentation program you want. Decide which guarantees you need and can maintain consistently."
Quotable: "For Spotify today, it does not."

**[24] Itamar Gilad - "Idea validation: much more than just A/B experiments" (the AFTER model).** practitioner. **fetched-and-verified.**
`https://itamargilad.com/idea-validation-much-more-than-just-a-b-experiments/`
Supports: Controlled experiments as one of four levels of validation, distinguished by a control; the case against defaulting to experiments
Quotable: "While experiments are the gold standard, of validation, there are many other, far cheaper and more immediate ways to test an idea. By fixating on experiments many companies set the bar too high, miss out on easier opportunities, and often give themselves an excuse to keep doing things the old way."
Quotable: "Experiments are tests that include a control element to guard against false results caused by random chance."

**[25] Atticus Li - "The Product Manager's Guide to Working with Experimentation Teams" (published 2026-04-09, updated 2026-07-23).** practitioner. **fetched-and-verified.**
`https://atticusli.com/blog/posts/product-managers-guide-working-with-experimentation-teams/`
Supports: A split of ownership between the product manager (the decision and its criteria) and the experimentation team (methodology); the framework choice framed per test as a trade between confidence and time; bringing the experimentation team into planning
Contested/time-bound: The author also promotes a commercial experimentation tool; the confidence and duration figures are one illustrative trade, not norms
Quotable: "The PM owns the product decision. The experimentation team owns the methodology and the rigor."
Quotable: "The PM sets the priority, the timeline, and the decision criteria"
Quotable: "If we want 95% confidence, we need 6 weeks. If we are willing to act on 80% Bayesian probability, we can decide in 3 weeks. If we want to ship by next week, we can call it directional and be explicit that we are making a decision without statistical confidence."
Quotable: "Bring the experimentation team into planning, not execution."

**[26] Aakash Gupta (with Bandan) - "Netflix: Lessons in Experimentation" (Product Growth, 2022-01-18).** practitioner. **fetched-and-verified.**
`https://www.aakashg.com/netflix-experimentation/`
Supports: A secondary account of cases where Netflix did not run a randomized controlled experiment (creative work; small cohorts, handled by quasi-experiments); Netflix's decision practice at a stated confidence level, as reported
Contested/time-bound: A secondary account, published 2022, not Netflix's own publication
Quotable: "Although creative shows cannot be properly A/B tested, Netflix did at least experiment with the medium first with one big show."
Quotable: "Instead of randomly allocating individuals to A or B, these experiments relied on assigning individuals based on location."
Quotable: "Although north star metrics help, many decisions are made at the 95% confidence level."

**[27] Rich Holmes - "How to Design Experiments for Your Product" (Department of Product).** practitioner. **fetched-and-verified.**
`https://www.departmentofproduct.com/blog/design-experiments-product/`
Supports: The plain if-then hypothesis with an optional because clause; low traffic as a reason to avoid optimisation experiments; the product manager's final call on prioritising experiments
Quotable: "If we reduce the number of buttons on the homepage then we'll get more registrations"
Quotable: "Often, startups do not have the traffic required to generate results that are statistically significant in any meaningful way"
Quotable: "Experiments should supplement not supplant your product OKRs, goals and roadmaps."
Quotable: "the product manager should make the final decision on prioritisation"

### BOUNDARIES: IN-TOOL EXPERIMENT SURFACES

**[28] Optimizely - "Understand your Experiment Scorecard" (Analytics docs).** vendor. **fetched-and-verified.**
`https://docs.optimizely.com/analytics/docs/understand-your-experiment-scorecard`
Supports: An in-tool experiment scorecard is a live, configurable analysis surface built from modules, not a written document; it distinguishes decision-making and guardrail metrics and sets alerts
Quotable: "An Experiment Scorecard template consists of the following modules:"
Quotable: "Decision-making metrics"
Quotable: "Guardrail metrics"
Quotable: "The visualization module in the Experiment Scorecard template lets you run and view the analysis as a pivot chart. It also lets you add the chart to a dashboard."
Quotable: "Alerts help you detect negative impacts early so you can decide whether to continue, halt, or adjust an experiment."

**[29] Statsig - "Experiment Summary PDF" (product update, 2023-10-09).** vendor. **fetched-and-verified.**
`https://www.statsig.com/updates/update/experiment-summary-pdf`
Supports: An in-tool summary exported from a finished experiment, holding setup information and results; the opposite end of a test's life from a design document
Quotable: "To export a PDF of your experiment summary, go to the Pulse tab in your finished experiment, tap Export, and select Experiment Summary PDF."
Quotable: "Key Setup Information, such as hypothesis, actual vs. target duration, primary/ secondary metrics, experiment variants (w/ group descriptions and images), etc."

**[30] Margaret-Ann Seger (Statsig) - "Templates" (product update, 2024-03-26).** vendor. **fetched-and-verified.**
`https://www.statsig.com/updates/update/templates-two`
Supports: Statsig's templates as reusable configuration for new experiments and gates, managed in project settings; the page names no field list and does not frame templates as a written document
Quotable: "Want to standardize best practices for experiment design across the company? Templates enable you to codify a blueprint for config creation that fellow team members can use to bootstrap their own feature gates and experiments."

**[31] GrowthBook - "Experiment Templates" (documentation).** vendor. **fetched-and-verified.**
`https://docs.growthbook.io/running-experiments/experiment-templates`
Supports: GrowthBook's in-tool templates preconfigure metadata, traffic allocation, targeting and metrics at experiment creation, for consistency; configuration of the running experiment, not a rationale document
Quotable: "Experiment Templates provide standardized configurations for experiment creation across your team. By reducing setup overhead and eliminating common boilerplate, templates enable faster experiment initialization and consistency in experimental design."
Quotable: "Experiment metadata and details"
Quotable: "Traffic allocation"
Quotable: "Targeting rules (saved groups, attributes, and prerequisites)"
Quotable: "Data source with goal, secondary, and guardrail metrics"

### THE GAP QUESTION

**[32] Eppo - "Mutual exclusion (Layers)" (documentation).** vendor. **fetched-and-verified.**
`https://docs.geteppo.com/feature-flagging/concepts/mutual_exclusion/`
Supports: Mutually exclusive experiments as an option for tests on the same surface, and the vendor's position that interaction effects are rare, citing research from Microsoft that this log did not read
Contested/time-bound: The rarity claim is Eppo's report of other research
Quotable: "There are situations when you want to run concurrent experiments on the same surface. Eppo offers Layers as an option to keep your experiments mutually exclusive."
Quotable: "Research from Microsoft has shown that in practice interaction effects are vanishingly rare. Given this, we recommend only using mutual exclusion when the overlap of two new treatments critically degrades the user experience."

**[33] Eppo - "Interaction Detection" (documentation).** vendor. **fetched-and-verified.**
`https://docs.geteppo.com/statistics/interaction-detection/`
Supports: Two named ways concurrent experiments can interact (assignment dependence and effect interaction) and the tests that detect each
Quotable: "Experiments can interact in two possible ways"
Quotable: "Effect Interaction: The effect of one variant depends on exposure in some other experiment."
Quotable: "Assignment dependence is tested using a Chi-Square hypothesis test, and effect interaction is tested using Analysis of Variance (ANOVA)."

**[34] GrowthBook - "Experimentation Best Practices" (documentation).** vendor. **fetched-and-verified.**
`https://docs.growthbook.io/using/experimentation-best-practices`
Supports: The vendor's position that meaningful interactions between parallel tests are rare, with mutually exclusive tests available when needed
Contested/time-bound: A vendor's position, not a measurement
Quotable: "However, meaningful interactions are actually quite rare, and keeping a higher rate of experimentation is usually more beneficial."
Quotable: "If you need to run mutually exclusive tests, you can use GrowthBook's namespace feature."

**[35] Itamar Gilad - "Product Discovery With ICE and The Confidence Meter".** practitioner. **fetched-and-verified.**
`https://itamargilad.com/the-tool-that-will-help-you-choose-better-product-ideas/`
Supports: A graded scale for the evidence behind an idea, from opinion to observed customer behaviour, assessed before committing resources; the full cost of acting on a wrong idea
Quotable: "There is only one way to calculate confidence - looking for supporting evidence."
Quotable: "The penalty for choosing the wrong product idea can be quite high - cost of development + cost of deployment + cost of maintenance + opportunity cost + other residual costs."
