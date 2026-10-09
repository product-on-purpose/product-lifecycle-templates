# Companion: The Experiment Design Doc

> The deep explainer for the experiment-design-doc bundle. Read this to understand what the document is,
> where its sections come from, and where the sources genuinely disagree. The short operator card is
> [`experiment-design-doc_guide.md`](experiment-design-doc_guide.md); a fully worked instance is
> [`experiment-design-doc_example.md`](experiment-design-doc_example.md). Inline citations like
> [[1]](#ref-1) resolve to the [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

An experiment design document is written before a product experiment launches, while nobody has seen any
data, and it exists to fix the decisions a team would otherwise make after seeing the results. LaunchDarkly
states the purpose in one sentence: "Experiment design documents contain the definition of why you are
running this test and the decisions you want to make based on its outcomes" [[3]](#ref-3). A practitioner
gives the same point its reason: "It's really important to put a stake in the ground before you run the
experiment and call out how you will make decisions based on the results" [[7]](#ref-7).

**At a glance**

- It is **pre-launch and design-only**. GrowthBook's own skill reference is explicit that it "does not
  create the experiment" in the tool; it hands off to a separate launch step [[1]](#ref-1).
- It carries one core that no other document in this library ships: the variants and how traffic is
  allocated between them, the effect size the test is sized to detect and the sample or duration that
  implies, and a decision rule naming an action for every outcome, including a null one.
- **It leads with what the PRD does not already ship.** A PRD's Success metrics section already names a
  primary metric, a guardrail and a measurement window
  (`templates/prd/prd_template-full.md:192-207`); this document's job starts past that point.
- It ships **lean by default**, five sections; the **full** variant adds two more for teams running at
  scale.
- **No source measured whether writing one improves an experiment's outcome.** The case for the document
  rests on practitioner testimony and on the statistics of what goes wrong without a pre-committed stopping
  rule, not on a controlled comparison of documented against undocumented tests. Section 6 below says this
  plainly, because a reader should not infer a stronger claim than the sources make.

**A terminology warning worth having on the first page.** If your organization already has a QA "test
plan", this is not that document. `qa-docs`'s own test-plan guide names the collision from its side: "Your
tool already has a 'test plan'" probably means an execution container grouping suites and runs, which that
template distinguishes from its own planning document
(`templates/test-plan/test-plan_guide.md:27`). This bundle's own collision is sharper still, because the
word is the same on both sides: a test plan verifies a product increment against an agreed specification
and grades it pass or fail; this document tests an open hypothesis and estimates an effect against a
baseline. Section 8 states the boundary in full.

## 2. Origins and evolution

The research log carries no single founder and no founding date for this document type - it is a
convention that several experimentation platforms and practitioners converged on independently, not an
artifact with a traceable inventor. What it does carry is three separate lineages that arrived at a
pre-launch written record by different routes.

**Product experimentation.** Every current A/B-testing vendor and several independent practitioners publish
some version of this document. GrowthBook ships a fill-in "Experiment spec" block as a skill reference
[[1]](#ref-1); LaunchDarkly names the type outright and lists its full pre-launch field set [[3]](#ref-3);
Optimizely publishes two tiers, a basic plan for teams starting out and an advanced "Experiment design
document template" for mature programs [[4]](#ref-4)[[5]](#ref-5); Amplitude's Bhavik Patel publishes an
"Experiment Brief" with a linked template [[6]](#ref-6); Adam Fishman's newsletter walks through a
four-part experiment document from first principles [[7]](#ref-7); and Atlassian hosts a Confluence
template, created by Optimizely, that a team can adopt directly [[8]](#ref-8). None of these sources dates
the convention's origin; the earliest dated source in this lineage is Spotify Engineering's 2025 account of
its own program [[22]](#ref-22), and the newest is Spotify's 2026-09-08 post on why it has not adopted a
second statistical framework [[23]](#ref-23), which this companion treats as a current position, not a
settled one.

**Academic preregistration**, which long predates the product convention, holds the same idea to a public
and legally time-stamped standard: "Preregistration is the practice of posting a time-stamped, read-only
version of your study plan to a public repository before beginning data collection or analysis. This
establishes a transparent record of your research intentions" [[18]](#ref-18). AsPredicted's own filed form
asks eight fixed questions, including which analyses will be run and how sample size will be determined
[[17]](#ref-17).

**Public-sector evaluation** reaches the same discipline through a different door: deciding before the
data. The UK's behavioural-insights team set out nine numbered steps for designing a randomised trial as
early as June 2012, including "Decide on the randomisation unit" as its own explicit step
[[20]](#ref-20). The Magenta Book, in its current edition, requires "all evaluation planning documents -
including evaluation plans, protocols and statistical analysis plans" to be "completed before the
evaluation begins, time-stamped, and preserved within the department" [[19]](#ref-19).

What the product lineage borrows from the other two, and what it deliberately leaves behind, is section 5's
subject. This companion does not attempt a methodology-family history for this document type: the
2026-10-08 research did not look at which named software-delivery frameworks originated or favor this
artifact, and nothing in the log supports a claim about any of them.

## 3. Anatomy (section by section)

The full variant carries seven sections; the lean variant carries the first five, unchanged in name and
order. Two sections, Tracking and Instrumentation Note and Validity Pre-Commitments, are full-variant only.

### Hypothesis

What you believe will happen, why, and what would prove you wrong.

No source converges on one sentence form, and that is a finding worth stating rather than hiding. This log
found four distinct, named conventions in circulation: GrowthBook's if/then/because ("If we change X, then
Y will improve, because Z") [[1]](#ref-1), also used by LaunchDarkly [[3]](#ref-3) and, in a plain if-then
variant with an optional because clause, by Rich Holmes [[27]](#ref-27); Amplitude's four-slot form, "We
observed:", "By:", "We expect:", "Leading to:" [[6]](#ref-6); Adam Fishman's two-sentence form, which names
its own refutation in the same breath ("We will know whether our hypothesis was right when we observe this
change in a metric, and our hypothesis will be refuted if we observe this other change") [[7]](#ref-7); and
Spotify Confidence's doing-this-for-these-people framing [[21]](#ref-21). The field in this bundle is left
free text for exactly that reason: a template that picked one of the four would be choosing a convention no
source argues for over the others.

What every convention agrees on is that the hypothesis must be falsifiable. The ICSE-SEIP checklist names it
as a design-review item, "Experiment hypothesis is defined and falsifiable" [[15]](#ref-15); Spotify
Confidence asks that it be "clear about what experiment outcomes would support or weaken it"
[[21]](#ref-21); Fishman's form bakes the refutation condition directly into the sentence [[7]](#ref-7).

**The evidence behind the hypothesis belongs in this section, not a separate one.** Fishman's "Supporting
evidence" field calls this "a very important aspect of your experiment document" [[7]](#ref-7); Amplitude
asks the author to "document the qualitative, quantitative, or competitive insight" the team observed
[[6]](#ref-6); Spotify Confidence wants the hypothesis "grounded in past research/learnings"
[[21]](#ref-21); and a separate framework for grading idea confidence states the principle generally: "There
is only one way to calculate confidence - looking for supporting evidence" [[35]](#ref-35). A hypothesis
with no stated evidence is a guess wearing a template.

### Population, Variants, and Allocation

Who is eligible for the test, how many variants it has, and what share of traffic each one gets.

The default is two: "control (current state) and treatment (the change)." Three or more variants are
allowed but "cost statistical power" [[1]](#ref-1). LaunchDarkly's field list separates the audience
("the target population for your experiment and the logic you use to identify it") from the variations
("how many variations this experiment uses, and what percentage of traffic each is assigned")
[[3]](#ref-3); Amplitude asks the same two questions as "Split" and "Audience cohort" [[6]](#ref-6).

**The randomization unit is named explicitly here, and it is a real design choice, not a formality.**
Fishman lists it first among his "five critical elements of experiment design" [[7]](#ref-7). Microsoft's
Experimentation Platform (ExP) warns that "all identifiers have some limitations and we cannot test all
features with a single randomization unit" [[9]](#ref-9), and names the reason: when a change affects both
a user and the people they are connected to, "the stable unit treatment value assumption (SUTVA) ... is
violated" [[9]](#ref-9). The UK's "Test, Learn, Adapt" guidance makes the same choice a numbered step of its
own, from a different lineage entirely: "Decide on the randomisation unit: whether to randomise to
intervention and control groups at the level of individuals, institutions (e.g. schools), or geographical
areas (e.g. local authorities)" [[20]](#ref-20). A team that randomizes by account rather than by individual
user because a change is visible to a user's colleagues is making exactly this choice, and the section
exists so the choice is written down rather than discovered after the fact.

### Primary and Guardrail Metrics

What moves if the hypothesis is right, what must not get worse, and by how much either way.

**This section leads with what the PRD does not already ship.** A PRD's Success metrics section already
names a primary metric, a guardrail metric and a measurement window
(`templates/prd/prd_template-full.md:192-207`), so this section's job is not to restate that but to carry
the number this experiment is specifically sized around: GrowthBook asks the author to "pick goal metrics
(ideally one, two max)" and "pick guardrails (1-3)" [[1]](#ref-1), and to give each a baseline. GrowthBook's
own metrics playbook calls the primary metric "the main measure of success in an experiment, typically one
per test" and the thing that "ultimately determines whether a change should be launched or rolled back"
[[14]](#ref-14). Guardrails exist for a different job: Microsoft ExP frames them as metrics that "measure
aspects of the product that we don't want to degrade but won't necessarily improve" [[10]](#ref-10), tested
as "non-inferiority" against a margin [[14]](#ref-14)[[21]](#ref-21); the ICSE-SEIP checklist names the
expectation as a design-review item, "Metrics and their expected movement are defined" [[15]](#ref-15).

**The multiple-metrics danger is worth naming in the section itself.** GrowthBook's own metrics playbook
warns that the more metrics a test analyzes, "the greater the chance of observing a" result that is "random
noise" rather than a real effect [[14]](#ref-14); its separate mistakes post names the mechanism outright as
one of the two statistics errors an experimentation program most often commits: "multiple-comparison
problems (adding so many metrics or slicing the data until it shows what you want to see)"
[[13]](#ref-13). Capping goal metrics at one or two and guardrails at a handful, as GrowthBook's own field
guidance does [[1]](#ref-1), is the direct answer to that danger, not a separate convention.

How many primary metrics is itself contested; see section 6, item 6.

### Minimum Detectable Effect and Sample Size or Duration

The smallest effect worth detecting, and how much traffic or time the test needs to detect it reliably.

**This is the single non-duplicated core this bundle exists to carry.** Evan Miller's classic piece on
running A/B tests gives the shape of the relationship without a magic number: a sample-size rule of thumb
driven by "the minimum effect you wish to detect" and "the sample variance you expect," such that a smaller
effect or a larger variance both demand a larger sample [[16]](#ref-16). Microsoft ExP frames the same
relationship from the power side: "power calculation sets a lower bound on the number of randomization
units that will be directly affected by the A/B test" [[9]](#ref-9). The field names recur across the
product vendors: GrowthBook's "MDE", "Estimated sample size" and "Estimated duration" [[1]](#ref-1);
Amplitude's "Total Sample Size", "Minimum Detectable Effect" and "Duration (days)" [[6]](#ref-6);
LaunchDarkly's plain "Sample size: how much traffic you need before you can check your results and determine
an outcome" [[3]](#ref-3); and the ICSE-SEIP checklist's design item, "Effect size and experiment duration
are set" [[15]](#ref-15).

**The stopping rule is fixed here too, and it is the point of the whole section.** Miller's argument is that
committing to a sample size in advance "completely mitigates" the statistical problem that peeking causes,
and that the honest way to stop early is a sequential design chosen before the test starts, not a decision
made once the numbers look good [[16]](#ref-16). Microsoft ExP's own practice is the same: in the absence of
a highly certain result, "we recommend running the test until the end of its pre-determined duration"
[[10]](#ref-10).

**Which statistical framework** - a fixed-horizon test, a sequential design, or a Bayesian stopping rule -
**is a live, unresolved question, and the section asks the author to name the one the team's platform
actually uses rather than choosing for them.** Spotify Engineering argues the choice belongs to the whole
program, not to each test, because "supporting both modes of inference would require different planning,
different monitoring, different interpretation, and possibly different-looking outputs" [[23]](#ref-23); a
practitioner guide to working with experimentation teams frames the same choice per test instead, as a trade
between confidence and time [[25]](#ref-25). Section 6, item 3 covers this in full.

**No power level or significance level is a field convention, and this bundle does not present one as
though it were.** The 95 percent and 80 percent figures that appear in the sources are one practitioner's
illustrative trade [[25]](#ref-25) and one company's reported practice [[26]](#ref-26), not a cross-industry
norm; neither is treated as a default here.

### Decision Rule

What the team will actually do for every outcome the test can produce, decided before the data arrives.

Eppo names the practice directly: "decision pre-registration" is the discipline of thinking "through as a
team what data would imply what decisions and write down quantitative thresholds," in the form "We will do
[A] if [metric X > 1%] and [metric Y is > -1%]" [[11]](#ref-11). Every source in this lineage ties an action
to every outcome: Amplitude asks "what actions will you take based on each of the following outcomes of the
test?" over "Win," "Lose" and "Flat" [[6]](#ref-6); Fishman's section is titled "Post Experiment Decisions
(aka If This Works We Should)" [[7]](#ref-7); Optimizely's basic plan asks for "parameters for significance
and lift that indicate the change is implemented permanently" [[4]](#ref-4).

**The null outcome is decided here as well, not treated as an afterthought.** Eppo asks teams to settle "the
decision from a null experiment" in advance [[11]](#ref-11); Spotify Engineering treats an adequately
powered null as a success in its own right, "Neutral but informative," with its own default action,
"Iterate, abandon, or ship if infra-only" [[22]](#ref-22). **The early stop for harm belongs here too**:
Eppo frames guardrails as the question that answers "what results would be bad enough that we end an
experiment early?" [[11]](#ref-11). **Who decides is named in the same place**: Eppo wants the decision
discussion held with the named "decision-maker" [[11]](#ref-11), and one practitioner account splits
ownership along exactly this line - "The PM owns the product decision. The experimentation team owns the
methodology and the rigor" [[25]](#ref-25).

"Ship, iterate or stop" is this family's own wording for the three-way choice, not a phrase any source uses
verbatim; it is stated as the
[contract's](../../docs/internal/contracts/experimentation-docs.md) own POSITION in its section 1. Spotify
Engineering's "Iterate, abandon, or ship if infra-only" [[22]](#ref-22) is the closest any source comes, and
it covers one outcome class, not the full decision space.

### Tracking and Instrumentation Note (full variant only)

What events feed each metric, the experiment's own exposure event, and a check that tracking works before
launch.

This is a pointer, not a restatement. The PRD's own Analytics and instrumentation section already lists the
events a feature needs (`templates/prd/prd_template-full.md:209-223`); what this note adds is which of those
events, plus any new ones, actually feed this test's metrics, and the experiment-specific exposure event
that marks who saw which variant. GrowthBook's field guidance asks for a "tracking key suggestion"
[[1]](#ref-1); Amplitude names an "Experiment Event Name" and "Experiment Event Parameters" and asks the
author to "ensure tracking in analytics is working" before the test runs, not after
[[6]](#ref-6); the ICSE-SEIP checklist names the underlying design concern, "Telemetry data can be
collected" [[15]](#ref-15). A test that launches with its metrics defined but its events unverified
discovers the gap only once it is too late to fix cheaply, which is why this note sits in the full variant
rather than being left to chance.

### Validity Pre-Commitments (full variant only)

The checks and thresholds that decide, before the test runs, whether its result will be trustworthy.

**This section's name and grouping are this library's own POSITION**: no single source in this research
names a section with this scope, and it is built by combining several sources' individually sourced
guidance rather than copying one template. Each piece is sourced on its own:

- **Sample ratio mismatch.** "A sample ratio mismatch is a statistically significant gap between the
  traffic split you configured and the split your experiment produced" [[12]](#ref-12), and it matters
  because "SRMs typically invalidate the A/B test and make any results and metric movements untrustworthy"
  [[10]](#ref-10).
- **Peeking.** Covered fully in the Minimum Detectable Effect section above; GrowthBook separately names
  "peeking (deciding on an experiment before it's completed)" among the statistics mistakes a program
  commits [[13]](#ref-13).
- **Shutdown for harm.** The ICSE-SEIP checklist names "criteria for alerting and shutdown are configured"
  as a design-review item [[15]](#ref-15); Microsoft ExP explains why it is pre-committed rather than
  improvised: "setting up auto-shutdown for A/B tests that significantly degrade the product or the user
  experience will resolve issues as soon as they are detected, instead of relying on (a possibly delayed)
  manual intervention" [[10]](#ref-10).
- **Ramp-up.** Microsoft ExP's own pattern: "an experiment can be first exposed to 1% of the traffic and
  gradually ramped-up to 5%, then 10% until the desired final traffic is achieved" [[9]](#ref-9).
- **Novelty effects and segments fixed in advance.** Microsoft ExP recommends computing metrics "segmented
  by each date in the test's period" to catch a novelty effect early, and recommends "'static' segments
  that rarely get affected by treatment" so a segment's own composition does not shift mid-test
  [[10]](#ref-10).
- **Overlap with concurrent experiments, labelled contested.** The ICSE-SEIP checklist names "overlap with
  related experiments is handled" as a design concern [[15]](#ref-15), and LaunchDarkly's own roadmap field
  asks whether an experiment belongs in a mutually exclusive set, which it calls "Layers"
  [[3]](#ref-3). Two vendors argue the opposite emphasis: Eppo reports that "research from Microsoft has
  shown that in practice interaction effects are vanishingly rare" [[32]](#ref-32), and GrowthBook states
  that "meaningful interactions are actually quite rare, and keeping a higher rate of experimentation is
  usually more beneficial" [[34]](#ref-34). Both rarity claims are the vendors' own reported positions, not
  independently measured here, and the guidance in this bundle says so rather than picking a side. Eppo
  separately names the two ways experiments can interact when they do overlap, assignment dependence and
  effect interaction, each with its own detection test [[33]](#ref-33).
- **Risks, and who must be told.** Fishman frames this plainly: "you can also use this as a way to identify
  what other teams might need to be aware of the experiment and its risks" [[7]](#ref-7).

**Frontmatter, not an eighth section.** The owner, the reviewers, the decision-maker, the status, and the
planned start date and duration live in the document's frontmatter rather than a body section. Atlassian's
template fills "the experiment owner, reviewers, approvers, and the status" in its top table
[[8]](#ref-8); Fishman lists "Experiment owners" [[7]](#ref-7) and the ICSE-SEIP checklist names the item
"Experiment owners are known" [[15]](#ref-15); LaunchDarkly's status field distinguishes "still being
drafted, is running, is being analyzed after collecting data, or is complete" [[3]](#ref-3); and the same
source gives the start date and duration fields their plainest wording, "the date your experiment will
start" and "how long your experiment will run" [[3]](#ref-3).

## 4. Variants and sizing

**Lean (five sections)** is the default: Hypothesis, Population/Variants/Allocation, Primary and Guardrail
Metrics, Minimum Detectable Effect and Sample Size or Duration, and Decision Rule. Optimizely's own basic
plan is the direct precedent for a lightweight variant, built for "if your team is starting to run its first
tests" [[4]](#ref-4).

**Full (seven sections)** adds the Tracking and Instrumentation Note and Validity Pre-Commitments.
Optimizely's advanced plan is the precedent again, aimed at a team whose "experimentation program is more
mature" and layering on an "Experiment design document template" plus a separate QA checklist
[[5]](#ref-5). The public-sector lineage states the same scaling principle independently, as proportion
rather than maturity: "for smaller or lower-risk evaluations, a short study registration may be sufficient.
For larger, more resource-intensive or higher stakes evaluations, pre-registration should normally include a
full evaluation protocol and a pre-registered statistical analysis plan" [[19]](#ref-19). Fishman makes the
same concession at field level from inside the product lineage: "some elements of this section will be
overkill" for a small test [[7]](#ref-7). The nesting is strict: every lean heading appears in full, in the
same name and order.

**How to choose.** A test run on a mature, high-traffic surface, or one that needs an auto-shutdown and a
ramp-up plan because the blast radius of a mistake is large, earns the full variant. A small test on a
constrained population, where the five lean sections already force every decision that matters, does not.

## 5. Methodology lineage

This document type has one home lineage and borrows deliberately from two older ones; it is not, as far as
this research found, claimed by any single named software-delivery framework. Which such frameworks favor
or originate this artifact is outside what the 2026-10-08 research covered, and nothing here should be read
as a claim about any of them.

**Product experimentation** is where the convention lives today, across every vendor and practitioner source
in section 2's first lineage. Within it, one methodological question is genuinely unresolved: whether the
statistical framework (fixed-horizon, sequential, or Bayesian) is a per-program decision or a per-test
trade-off. Spotify Engineering argues for the program-wide choice, on the grounds that "supporting both
modes of inference would require different planning, different monitoring, different interpretation, and
possibly different-looking outputs" [[23]](#ref-23); it also undercuts the idea of a clean three-way choice,
noting that "the mixture Sequential Probability Ratio Test, one of the most well-known frequentist
sequential procedures, is exactly the Bayes factor stopping under the same prior" [[23]](#ref-23). A
practitioner guide to working with experimentation teams frames the same choice per test, as a trade between
confidence and time [[25]](#ref-25). Spotify's post is dated 2026-09-08 and explicitly states its own
company's current position - "for Spotify today, it does not" - rather than a settled industry answer
[[23]](#ref-23), so this companion treats it as time-bound.

**Academic preregistration** contributes the discipline of a public, time-stamped, legally binding
commitment: "preregistration is the practice of posting a time-stamped, read-only version of your study
plan to a public repository before beginning data collection or analysis" [[18]](#ref-18), and once
submitted, "you will not be able to edit or make changes to it or any associated files" [[18]](#ref-18).
AsPredicted's own eight-question form is the lineage's working instrument [[17]](#ref-17).

**Public-sector evaluation** reaches the same discipline of deciding-before-data through government policy
practice rather than academic method. The Magenta Book requires planning documents "completed before the
evaluation begins, time-stamped, and preserved within the department," explicitly "to prevent researchers
from 'fishing' for significant or positive findings by arbitrarily adjusting the way that data is collected
or analysed" [[19]](#ref-19); "Test, Learn, Adapt" supplies the nine-step method a government team follows
to design the trial itself [[20]](#ref-20).

**What a product design document borrows from the two older lineages, and what it deliberately does not.**
It borrows the discipline of deciding before the data: the Magenta Book's own description of pre-registration
as "documenting key elements of the evaluation such as its objectives, research questions, design, data
collection procedures and analytical approach, before any outcome data is collected or analysed"
[[19]](#ref-19), and AsPredicted's instruction to "specify exactly which analyses you will conduct to
examine the main question/hypothesis" [[17]](#ref-17), describe exactly the discipline this bundle's
Decision Rule and Validity Pre-Commitments sections encode. It does **not** borrow their accountability
machinery: no source in the product lineage asks for a public, read-only, permanently time-stamped registry
entry the way OSF does [[18]](#ref-18), or a mandatory government registry the way the Magenta Book does
[[19]](#ref-19). A product team that wants the amendment discipline without the registry should say which
tradition it is borrowing from, which section 7 returns to as an anti-pattern when that attribution is
dropped.

## 6. Debates and contested boundaries

None of these nine questions is settled by the sources read for this bundle. Each is named here with its
camps, because flattening a live disagreement into a false convention is the dominant way this kind of
document goes wrong.

**1. One document, or two.** Three sources keep the plan and the results in a single document across its
life: Amplitude's four-phase brief runs through "Phase 4: Analyze and Decide" [[6]](#ref-6); Fishman's
document has four parts, "The Why The Plan The Results The Checklist" [[7]](#ref-7); Atlassian's template
steps through "1 Cover the basics," "2 Set a plan for your experiment," "3 Outline your results," and "4
Draw conclusions" [[8]](#ref-8). Four others are design-only: GrowthBook's skill explicitly "does not create
the experiment" and hands off elsewhere [[1]](#ref-1); Optimizely's two plans [[4]](#ref-4)[[5]](#ref-5) and
LaunchDarkly's field list [[3]](#ref-3) hold no results artifact. No source argues either side is correct.
This library's own contract settles the question for its own purposes, not as a finding: it ships two
separate bundles, this one and the not-yet-built `experiment-readout`, following the same precedent
`qa-docs` set with `test-plan` and `test-summary-report`
([contract](../../docs/internal/contracts/experimentation-docs.md), section 1). A team that keeps one living
document can still use this bundle; its sections are that document's first half.

**2. The hypothesis sentence's form.** Four distinct, named conventions: covered in full in section 3's
Hypothesis subsection. No source argues that its own form is the correct one over the others.

**3. Whether the statistical framework is a per-test or a per-program choice.** Covered in full in sections
3 and 5 above. Spotify Engineering argues for the whole program [[23]](#ref-23); a practitioner guide frames
it per test [[25]](#ref-25). Neither reconciles the other.

**4. Whether overlap with concurrent experiments needs designing around.** Covered in full in section 3's
Validity Pre-Commitments subsection. The ICSE-SEIP checklist and LaunchDarkly both treat it as something a
design document should handle [[15]](#ref-15)[[3]](#ref-3); Eppo and GrowthBook both report that meaningful
interaction effects are rare in practice [[32]](#ref-32)[[34]](#ref-34). The rarity claim is each vendor's
own reported position, and Eppo attributes its version to unread Microsoft research [[32]](#ref-32); this
companion does not adopt either rarity claim as fact.

**5. How long a test should run.** Microsoft ExP reports its own company's norm, "the typical duration of
an A/B test is 7 days" [[10]](#ref-10); separately, the same source and Evan Miller both derive duration
from the effect size and the variance rather than from a fixed number [[16]](#ref-16)[[9]](#ref-9)[[10]](#ref-10).
These are compatible - a norm can function as a floor - but seven days is Microsoft's own typical duration,
not a cross-industry convention, and this bundle does not present it as one.

**6. How many primary metrics a test should carry.** GrowthBook's metrics playbook says "typically one per
test" [[14]](#ref-14); GrowthBook's own field guidance separately says "ideally one, two max"
[[1]](#ref-1); Spotify Confidence says "many experiments use one or two success metrics and a few guardrail
metrics" [[21]](#ref-21). All three warn against stacking many primary metrics onto one test; none agrees on
the exact ceiling. This companion's own reading, given that all three independently warn in the same
direction, is that one or two is the safer default, not a hard rule.

**7. Who owns the document.** A practitioner guide splits ownership cleanly: "the PM owns the product
decision. The experimentation team owns the methodology and the rigor" [[25]](#ref-25). Fishman lists
several "experiment owners" without specifying a role [[7]](#ref-7), and Atlassian's template names an
owner, reviewers and approvers as three separate fields [[8]](#ref-8). A fourth source gives the product
manager the final call on which experiments to run at all, which is a prioritization decision, not
authorship of the document [[27]](#ref-27). No source hands the whole document to one named role.

**8. What a null result is, and what it is called.** Spotify Engineering treats an adequately powered null
as a success in its own right, "neutral but informative" [[22]](#ref-22); Eppo asks teams to settle "the
decision from a null experiment" in advance, without naming the outcome [[11]](#ref-11); Atlassian's
template simply offers "inconclusive" as a conclusion to record [[8]](#ref-8). All three agree a null result
must be decided on in advance rather than discovered as a surprise; they differ only on its name.

**9. Time-bound figures that read like norms but are not.** Spotify Engineering's own 64 percent learning
rate and roughly 12 percent win rate describe two of its own organizations, published in 2025
[[22]](#ref-22); a secondary account of Netflix's practice reports decisions "made at the 95% confidence
level," as of a 2022 publication [[26]](#ref-26). Neither figure is a field-wide norm, and neither is
presented as one here.

## 7. Anti-patterns and failure modes

**Claiming a measured frequency for why experiments fail.** One early research pass attributed to Fishman
the claim that "most experiment failures trace back to" a specific small set of causes. That string does not
appear on his page; what he actually writes is narrower and does not claim a frequency at all: "it IS a
failed experiment if you can't learn something reliable due to poor design" [[7]](#ref-7). Fix: state the
design principle Fishman actually makes, and do not borrow a frequency claim no source makes.

**Treating the metrics section as the PRD's section, renamed.** The PRD already carries a primary metric, a
guardrail and a measurement window (`templates/prd/prd_template-full.md:192-207`). A design document that
opens by restating those fields, rather than leading with the variants, the allocation, the minimum
detectable effect, and the decision rule, duplicates work the PRD already did and buries the one content
this document exists to add.

**Peeking, and calling it monitoring.** Deciding on an experiment before its pre-committed sample size or
duration is reached inflates the false-positive rate in a way that makes "all the reported significance
levels become meaningless" [[16]](#ref-16); GrowthBook separately names "peeking (deciding on an experiment
before it's completed)" as one of two recurring statistics mistakes a program commits [[13]](#ref-13). Fix:
fix the sample size or duration in the design document itself, before the test launches, and treat any
early look as informational only unless a sequential design was chosen in advance.

**Presenting seven days as a standard test duration.** It is Microsoft's own reported typical duration
[[10]](#ref-10), not a field convention; see section 6, item 5.

**Treating a vendor's in-tool configuration surface as a substitute for, or a companion to, this written
document.** Optimizely's Experiment Scorecard is a live, configurable analysis surface built from modules,
not a document [[28]](#ref-28); Statsig's Experiment Summary PDF is an export generated from a *finished*
experiment, the opposite end of a test's life from a design document [[29]](#ref-29); Statsig's and
GrowthBook's own "templates" features preconfigure an experiment's setup fields at creation time, not a
rationale for running it [[30]](#ref-30)[[31]](#ref-31). None of these four sources claims its tool's
configuration replaces or sits alongside a written design document; that boundary is this library's own,
under [ADR 0030 (templating scope: Markdown documents)](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md).
Fix: use the in-tool surface for what it is built for, and keep the written rationale here.

**Amending the design silently after the test has launched.** No source in the product-experimentation
lineage speaks to this directly; the public-sector lineage does, and the habit is worth borrowing by name:
"pre-registration does not prevent changes being made to an evaluation design, but it requires that
amendments to evaluation plans are documented and explained" [[19]](#ref-19). Fix: if the design changes
after launch, record the change and the reason, in the document, rather than quietly editing the original.

**Running an experiment when a cheaper validation method would answer the question.** "Not everything needs
to be run as an experiment. A lot of product teams over-rely on experiments, which can be quite costly,"
and "if you're going to ship a change regardless of the experiment results, save yourself the complexity and
skip the experiment" [[7]](#ref-7). A separate validation framework names the same risk from the opposite
direction: "by fixating on experiments many companies set the bar too high, miss out on easier
opportunities, and often give themselves an excuse to keep doing things the old way" [[24]](#ref-24); a
startup without enough traffic "to generate results that are statistically significant in any meaningful
way" faces the same problem from a different cause [[27]](#ref-27). Fix: this is the guide's own decision
point, not this document's; the guide states when not to write one at all.

**An ethics or consent review, treated as either required or irrelevant.** No source read for this research
describes an ethics or consent review as a step before a product A/B test; the one paper most directly on
point was not retrieved (HTTP 403). This bundle makes no claim either way, because none is supported, and a
reader should not infer from its absence here that the question has been considered and dismissed.

## 8. Relationships to other artifacts

**The other family member.** Per the
[contract](../../docs/internal/contracts/experimentation-docs.md), this document states the plan; the
not-yet-built `experiment-readout` reports the same test's results and the decision it drove, after the
test ends. The contract requires every member to finish this pair sequentially rather than as alternatives:
a design document that is never followed by a readout has recorded a decision rule nobody checked it
against.

**The spike report (`decision-docs`).** This family's contract requires stating the boundary by name. A
spike report's own companion describes a spike as a "time-boxed research experiment that answers one
specific question fast" and states plainly, of a spike that fails to confirm its premise, "a refuted
hypothesis is a successful spike" (`templates/spike-report/spike-report_companion.md:179,188`). The
vocabulary overlaps - both documents use "hypothesis" and "experiment" - but a spike reduces uncertainty
about a technical or design question. It carries no control group, no allocation between variants, and no
statistical decision rule. This document tests an open hypothesis about user behavior against a baseline,
with a control group and a pre-committed effect size.

**The test plan and test summary report (`qa-docs`).** Also a required boundary statement. `qa-docs`'s own
test-plan guide names the collision from its side: "your tool already has a 'test plan'" probably means an
execution container (`templates/test-plan/test-plan_guide.md:27`). Framed from this side: a test plan and
its summary report verify a product increment against an agreed specification and grade it pass or fail.
Neither carries a hypothesis, an allocation between variants, or a statistical decision rule. This document
tests an open hypothesis and estimates an effect against a baseline rather than grading conformance to a
spec. The shared word is "test," which is exactly the collision both contracts name.

**Standing measurement instruments.** A tracking plan, a data dictionary, or an experiment log is maintained
across many tests and is never finished in the way a single test's design document is. The
[contract](../../docs/internal/contracts/experimentation-docs.md) excludes this category from the family by
name, and the tracking plan specifically joins `governance-docs` instead, by
[ADR 0067 (tracking plan joins governance-docs as a sixth member)](../../docs/internal/decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md).
This document's own Tracking and Instrumentation Note (full variant) points at a tracking plan's events
where one exists; it does not duplicate one.

**Pre-build validation.** A test run before anything is built, to decide whether to build it at all, is a
different job and is excluded from this family by the contract's own second boundary sentence
([contract](../../docs/internal/contracts/experimentation-docs.md), section 1). This document assumes the
thing under test already exists in a shippable form.

**In-tool experiment surfaces.** Optimizely's Experiment Scorecard [[28]](#ref-28), Statsig's Experiment
Summary PDF export [[29]](#ref-29), and Statsig's and GrowthBook's own "templates" features
[[30]](#ref-30)[[31]](#ref-31) are live, tool-native configuration and analysis surfaces, not narrative
documents. None of these sources claims its surface replaces or sits beside a written design document; the
boundary that keeps this document out of their territory, and them out of this document's, is this
library's own, under
[ADR 0030](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md).

**The PRD.** Covered in full in section 3. The PRD's Success metrics and Analytics and instrumentation
sections are the upstream input this document starts from and must not repeat
(`templates/prd/prd_template-full.md:192-223`).

## 9. Adaptations

**Mature versus starting-out experimentation programs.** Use lean while a team is running its first tests;
move to full once the program is mature enough to need a tracking note and pre-committed validity checks,
following Optimizely's own two-tier precedent [[4]](#ref-4)[[5]](#ref-5).

**Regulated or public-sector-adjacent contexts.** The Magenta Book's proportionality principle generalizes
beyond government: "pre-registration should be applied in a proportionate way," with a fuller protocol and
statistical analysis plan for higher-stakes evaluations [[19]](#ref-19). This bundle does not define
"protocol" or "statistical analysis plan" in the Magenta Book's own formal sense, because its Annex A, where
those terms are defined, was not read for this research; a team that needs that formal definition should
read the Magenta Book directly rather than infer it from this companion.

**Teams on one shared statistical framework versus teams choosing per test.** Section 5 and 6 (item 3) cover
the live disagreement. A program-wide platform choice, as Spotify Engineering argues for
[[23]](#ref-23), means every design document can skip naming the framework; a team that allows the
trade-off per test [[25]](#ref-25) should name the chosen framework, the confidence level, and the time
implication in this section explicitly, because a reader cannot otherwise tell which trade was made.

**One-living-document teams.** Section 6, item 1 covers the live disagreement over whether the plan and
results belong in one document. This bundle still works for a team that prefers one document: its sections
are that document's first half, and the guide, not this companion, walks through how to use it that way.

**What may be adapted, and under what terms.** GrowthBook's skill-reference structure [[1]](#ref-1) may be
adapted with attribution and the MIT notice, because the repository that ships it is MIT-licensed:
"MIT License. Copyright (c) 2026 GrowthBook" [[2]](#ref-2). The Magenta Book's and "Test, Learn, Adapt"'s
wording [[19]](#ref-19)[[20]](#ref-20) may likewise be adapted with attribution, as both are Crown copyright
under the Open Government Licence: "you may reuse this information (not including logos) free of charge in
any format or medium, under the terms of the Open Government Licence" [[20]](#ref-20). OSF's own reference
article is offered for reuse without attribution, printed as "CCO" rather than the expected zero: "this
article is licensed under CCO for maximum reuse" [[18]](#ref-18). The ICSE-SEIP checklist [[15]](#ref-15) is
marked "not for redistribution," so this bundle takes only its item names and section titles from it, never
a reproduced sentence. Every other source states no licence on the page read, and this bundle quotes it
briefly without adapting its structure.

## 10. Worked example

[`experiment-design-doc_example.md`](experiment-design-doc_example.md) is a full-variant design document
for the Saved Views adoption-nudge experiment at Acme Analytics, dated 2026-07-30: a one-time in-app prompt
shown to a Recurring Analyst after their fifth dashboard view, suggesting they save their current filter,
date range and column setup as a view, against a no-prompt control. It runs 2026-08-03 through 2026-08-31,
and its primary metric, starting value and target are drawn directly from this library's own KPI dashboard
and OKRs examples rather than invented.

Three things in it are worth studying past the shape of a filled template. Its **population is honestly
small** - roughly 495 weekly active Recurring Analysts at the time the document is written - and the example
says so plainly, labelling every sample-size and duration figure illustrative rather than pretending to a
precision the population cannot support. Its **Primary and Guardrail Metrics section states explicitly why
it is not the PRD's metrics section again**: the nudge's own target is adoption share, not the PRD's primary
metric of time to first meaningful interaction, and the document says so in one line. And its **Decision
Rule names an action for the null outcome**, not only for a win, which is the exact gap section 3 argues a
design document must not leave open.

---

## References

<a id="ref-1"></a>[1] GrowthBook. "[experiment-design skill reference](https://github.com/growthbook/skills/blob/main/skills/experiments/references/experiment-design.md)." GrowthBook skills repository (accessed 2026-10-08). Supports the fill-in "Experiment spec" field order (hypothesis, variations, primary metric with baseline, guardrails, MDE, estimated sample size, estimated duration, tracking key), the if/then/because hypothesis form, the default of two variants, and one-or-two goal metrics with one-to-three guardrails ("Help the user design a well-formed GrowthBook experiment before it's launched."; "Does not create the experiment in GrowthBook."). [vendor]

<a id="ref-2"></a>[2] GrowthBook. "[LICENSE](https://raw.githubusercontent.com/growthbook/skills/main/LICENSE)." GrowthBook skills repository (accessed 2026-10-08). Supports that the repository shipping [[1]](#ref-1) is MIT-licensed ("MIT License"; "Copyright (c) 2026 GrowthBook"), which is why its structure may be adapted with attribution. [vendor]

<a id="ref-3"></a>[3] LaunchDarkly. "[Designing experiments](https://launchdarkly.com/docs/guides/experimentation/designing-experiments)." LaunchDarkly documentation (accessed 2026-10-08). Supports the document type's purpose statement, the if/then/because hypothesis form, the full pre-launch field list (audience, variations, sample size, layers, holdouts, start date, duration, status), and the status vocabulary ("Experiment design documents contain the definition of why you are running this test and the decisions you want to make based on its outcomes."). [vendor]

<a id="ref-4"></a>[4] Optimizely. "[Create a basic experiment plan](https://docs.optimizely.com/experimentation-strategy/docs/create-a-basic-experiment-plan)." Optimizely Experimentation Strategy documentation (accessed 2026-10-08). Supports the lean-plan precedent for teams starting out, its field questions, and the pointer onward to the advanced plan ("If your experimentation program is more mature, see the advanced experiment design template and QA checklist."). [vendor]

<a id="ref-5"></a>[5] Optimizely. "[Create an advanced experiment plan and QA checklist](https://docs.optimizely.com/experimentation-strategy/docs/create-an-advanced-experiment-plan-and-qa-checklist)." Optimizely Experimentation Strategy documentation (accessed 2026-10-08). Supports what the full-variant precedent adds over the basic plan ("A full experiment plan gathers decisions from stakeholders into a single, collaborative document."; "Experiment design document template"). [vendor]

<a id="ref-6"></a>[6] Bhavik Patel. "[Use Experiment Briefs to Design Better Experiments](https://amplitude.com/blog/experiment-brief)." Amplitude blog (accessed 2026-10-08). Supports the four-phase "Experiment Brief" structure, its four-slot hypothesis form, separate metric lists for hypothesis and do-no-harm tests, the sample size/MDE/duration fields, and the per-outcome action requirement ("Actions: What actions will you take based on each of the following outcomes of the test?"). [vendor]

<a id="ref-7"></a>[7] Adam Fishman. "[Creating an Experiment Doc](https://www.fishmanafnewsletter.com/p/experiment-document-template)." Fishman AF Newsletter (accessed 2026-10-08). Supports the four-part document structure, its two-sentence self-refuting hypothesis form, the five critical design elements led by the randomization unit, the risks-and-notification practice, the decision rule fixed before the test, and the guidance on when not to run an experiment at all ("It's really important to put a stake in the ground before you run the experiment and call out how you will make decisions based on the results."). [practitioner]

<a id="ref-8"></a>[8] Atlassian. "[Experiment plan and results template](https://www.atlassian.com/software/confluence/templates/experiment-plan-and-results)." Atlassian Confluence templates, created by Optimizely (accessed 2026-10-08). Supports the one-document, four-step template structure (basics, plan, results, conclusions), the owner/reviewers/approvers frontmatter fields, and "inconclusive" as a recorded conclusion ("The top table of the template has space to outline the basics - including the name of the experiment, the experiment owner, reviewers, approvers, and the status."). [vendor]

<a id="ref-9"></a>[9] Microsoft Experimentation Platform (ExP). "[Patterns of Trustworthy Experimentation: Pre-Experiment Stage](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/)." Microsoft Research (accessed 2026-10-08). Supports the power-calculation lower bound on randomization units, the randomization unit as a constrained design choice, the SUTVA network-effects violation, and the gradual safe-rollout ramp-up pattern ("Pay attention to the choice of the randomization unit for the A/B test. All identifiers have some limitations and we cannot test all features with a single randomization unit."). [primary]

<a id="ref-10"></a>[10] Microsoft Experimentation Platform (ExP). "[Patterns of Trustworthy Experimentation: During-Experiment Stage](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/)." Microsoft Research (accessed 2026-10-08). Supports Microsoft's own typical 7-day test duration, running to a pre-determined duration rather than stopping early, sample ratio mismatch and its consequence, guardrail alerting, auto-shutdown, and date-segmented novelty-effect detection with static segments ("the typical duration of an A/B test is 7 days"; "SRMs typically invalidate the A/B test and make any results and metric movements untrustworthy."). [primary]

<a id="ref-11"></a>[11] Eppo. "[Make Decisions Before Experimenting](https://www.geteppo.com/blog/make-decisions-before-experimenting)." Eppo blog (accessed 2026-10-08). Supports decision pre-registration, its "we will do" conditional form, guardrails as the early-stop question, holding the discussion with a named decision-maker, and deciding the null outcome in advance ("think through as a team what data would imply what decisions and write down quantitative thresholds"). [vendor]

<a id="ref-12"></a>[12] GrowthBook. "[Sample Ratio Mismatch (SRM): Types, Causes, and How to Identify](https://www.growthbook.io/blog/sample-ratio-mismatch)." GrowthBook blog (accessed 2026-10-08). Supports the definition of sample ratio mismatch ("A sample ratio mismatch is a statistically significant gap between the traffic split you configured and the split your experiment produced."). [vendor]

<a id="ref-13"></a>[13] GrowthBook. "[Experimentation Program Mistakes to Avoid](https://www.growthbook.io/blog/experimentation-program-mistakes-to-avoid)." GrowthBook blog (accessed 2026-10-08). Supports peeking and multiple comparisons as named statistics mistakes an experimentation program commits ("peeking (deciding on an experiment before it's completed)"; "multiple-comparison problems (adding so many metrics or slicing the data until it shows what you want to see)"). [vendor]

<a id="ref-14"></a>[14] GrowthBook. "[KPI Playbook: A/B Testing Metrics](https://www.growthbook.io/blog/kpi-playbook-ab-testing-metrics)." GrowthBook blog (accessed 2026-10-08). Supports one primary metric deciding launch or rollback, guardrails monitoring for harm through non-inferiority tests, and the multiple-metrics danger ("The primary metric is the main measure of success in an experiment, typically one per test."; "Guardrail metrics monitor for unintended harm."). [vendor]

<a id="ref-15"></a>[15] A. Fabijan, P. Dmitriev, H. H. Olsson, J. Bosch, L. Vermeer and D. Lewis. "[Three Key Checklists and Remedies for Trustworthy Analysis of Online Controlled Experiments at Scale](https://exp-platform.com/Documents/2019%20FabijanDmitrievOlssonBoschVermeerLewis_Three-Key-Checklists_ICSE_SEIP.pdf)." ICSE-SEIP 2019, authors' preprint (accessed 2026-10-08). Supports the pre-launch design checklist's item names: a falsifiable hypothesis, defined metrics and expected movement, telemetry readiness, effect size and duration, overlap with related experiments, early-stopping and shutdown criteria, owners, and randomization quality. Marked "Not for redistribution": item names and section titles cited here, nothing else reproduced. [academic]

<a id="ref-16"></a>[16] Evan Miller. "[How Not To Run an A/B Test](https://www.evanmiller.org/how-not-to-run-an-ab-test.html)." evanmiller.org (accessed 2026-10-08). Supports repeated significance testing (peeking) and why it invalidates reported significance, a sample size driven by the minimum effect and the expected variance, committing to a sample size in advance, and sequential design as the legitimate way to stop early ("Committing to a sample size completely mitigates the problem described here."). The page's own illustrative false-positive-rate calculation is not a field measurement and is not cited. [practitioner]

<a id="ref-17"></a>[17] AsPredicted. "[AI agent Field Study (The second Batch)](https://aspredicted.org/MQQ_B7B)." AsPredicted public pre-registration #133868 (accessed 2026-10-08). Supports the eight numbered questions of AsPredicted's filed form, in order, on a real time-stamped instance ("Specify exactly which analyses you will conduct to examine the main question/hypothesis."). [primary]

<a id="ref-18"></a>[18] Open Science Framework (OSF) Support. "[Welcome to Registrations & Preregistrations!](https://help.osf.io/article/330-welcome-to-registrations)" OSF Support (accessed 2026-10-08). Supports the definition of preregistration as a time-stamped, read-only public record, that a submitted registration cannot be edited, that OSF recommends no single default template, and the article's own CC0 licence line, printed "CCO" ("Preregistration is the practice of posting a time-stamped, read-only version of your study plan to a public repository before beginning data collection or analysis."). [primary]

<a id="ref-19"></a>[19] HM Treasury. "[The Magenta Book: Central Government guidance on evaluation](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html)." HTML edition, May 2026 (accessed 2026-10-08). Supports evaluation plans, protocols and statistical analysis plans completed and time-stamped before an evaluation begins, pre-registration applied proportionately to stakes, amendments documented rather than forbidden, and the Open Government Licence ("all evaluation planning documents - including evaluation plans, protocols and statistical analysis plans - should be completed before the evaluation begins, time-stamped, and preserved within the department"). This companion does not define "protocol" or "statistical analysis plan" in the Magenta Book's own formal sense, because its Annex A was not read. [primary]

<a id="ref-20"></a>[20] Laura Haynes, Owain Service, Ben Goldacre and David Torgerson (Cabinet Office Behavioural Insights Team). "[Test, Learn, Adapt: Developing Public Policy with Randomised Controlled Trials](https://assets.publishing.service.gov.uk/media/5a7488c8e5274a7f9c586c23/TLA-1906126.pdf)." Cabinet Office (June 2012; accessed 2026-10-08). Supports the nine numbered steps for designing and using a randomised trial, including deciding the randomisation unit and the required number of units, and the Open Government Licence ("Decide on the randomisation unit: whether to randomise to intervention and control groups at the level of individuals, institutions (e.g. schools), or geographical areas (e.g. local authorities)"). [primary]

<a id="ref-21"></a>[21] Spotify Confidence. "[Hypothesis](https://confidence.spotify.com/docs/experiments/design/hypothesis)." Spotify Confidence product documentation (accessed 2026-10-08). Supports Spotify Confidence's hypothesis form and criteria, one hypothesis per success metric, and non-inferiority margins stated as guardrail hypotheses ("Many experiments use one or two success metrics and a few guardrail metrics."). [vendor]

<a id="ref-22"></a>[22] Michael Bellato, Mårten Schultzberg and Sebastian Ankargren (Spotify Engineering). "[Beyond Winning: Spotify's Experiments with Learning Framework](https://engineering.atspotify.com/2025/9/spotifys-experiments-with-learning-framework)." Spotify Engineering (2025; accessed 2026-10-08). Supports a successful experiment defined as valid and decision-ready rather than a win, an adequately powered null treated as "neutral but informative," and Spotify's own 2025 learning-rate and win-rate figures for two of its organizations, reported as Spotify's own figures, not a field norm ("Neutral but informative: No effect but the test was strong enough to detect one if it existed -> Iterate, abandon, or ship if infra-only."). [primary]

<a id="ref-23"></a>[23] Mattias Frånberg and Mårten Schultzberg (Spotify Engineering). "[Why Spotify Is Not Using Bayesian A/B Testing](https://engineering.atspotify.com/2026/9/why-spotify-is-not-using-bayesian-a-b-testing)." Spotify Engineering (2026-09-08; accessed 2026-10-08). Supports one organization's reasoned case for a program-wide statistical framework rather than a per-test choice, stated explicitly as a current, time-bound position ("For Spotify today, it does not."). [primary]

<a id="ref-24"></a>[24] Itamar Gilad. "[Idea validation: much more than just A/B experiments](https://itamargilad.com/idea-validation-much-more-than-just-a-b-experiments/)." itamargilad.com (accessed 2026-10-08). Supports controlled experiments as one of several validation levels and the case against defaulting to them for every idea ("By fixating on experiments many companies set the bar too high, miss out on easier opportunities, and often give themselves an excuse to keep doing things the old way."). [practitioner]

<a id="ref-25"></a>[25] Atticus Li. "[The Product Manager's Guide to Working with Experimentation Teams](https://atticusli.com/blog/posts/product-managers-guide-working-with-experimentation-teams/)." atticusli.com (published 2026-04-09, updated 2026-07-23; accessed 2026-10-08). Supports the PM/experimentation-team ownership split, the statistical framework framed as a per-test trade between confidence and time, and bringing the experimentation team into planning ("The PM owns the product decision. The experimentation team owns the methodology and the rigor."). The author also promotes a commercial experimentation tool; the confidence/duration figures given are one illustrative trade, not a norm. [practitioner]

<a id="ref-26"></a>[26] Aakash Gupta (with Bandan). "[Netflix: Lessons in Experimentation](https://www.aakashg.com/netflix-experimentation/)." Product Growth (2022-01-18; accessed 2026-10-08). Supports a secondary, 2022-dated account of cases where Netflix used a quasi-experimental design instead of randomization, and Netflix's own reported confidence-level practice ("Although north star metrics help, many decisions are made at the 95% confidence level."). A secondary account, not Netflix's own publication. [practitioner]

<a id="ref-27"></a>[27] Rich Holmes. "[How to Design Experiments for Your Product](https://www.departmentofproduct.com/blog/design-experiments-product/)." Department of Product (accessed 2026-10-08). Supports the plain if-then hypothesis with an optional because clause, low traffic as a reason to avoid optimization experiments, and the product manager's final call on experiment prioritization ("Often, startups do not have the traffic required to generate results that are statistically significant in any meaningful way"). [practitioner]

<a id="ref-28"></a>[28] Optimizely. "[Understand your Experiment Scorecard](https://docs.optimizely.com/analytics/docs/understand-your-experiment-scorecard)." Optimizely Analytics documentation (accessed 2026-10-08). Supports that an in-tool experiment scorecard is a live, configurable analysis surface built from modules, not a written document, and distinguishes decision-making and guardrail metrics ("An Experiment Scorecard template consists of the following modules:"). [vendor]

<a id="ref-29"></a>[29] Statsig. "[Experiment Summary PDF](https://www.statsig.com/updates/update/experiment-summary-pdf)." Statsig product update (2023-10-09; accessed 2026-10-08). Supports an in-tool export generated from a finished experiment, holding setup information and results, as the opposite end of a test's life from a design document ("To export a PDF of your experiment summary, go to the Pulse tab in your finished experiment."). [vendor]

<a id="ref-30"></a>[30] Margaret-Ann Seger (Statsig). "[Templates](https://www.statsig.com/updates/update/templates-two)." Statsig product update (2024-03-26; accessed 2026-10-08). Supports Statsig's templates as reusable experiment-creation configuration managed in project settings, naming no field list and not framing templates as a written document ("Templates enable you to codify a blueprint for config creation that fellow team members can use to bootstrap their own feature gates and experiments."). [vendor]

<a id="ref-31"></a>[31] GrowthBook. "[Experiment Templates](https://docs.growthbook.io/running-experiments/experiment-templates)." GrowthBook documentation (accessed 2026-10-08). Supports GrowthBook's in-tool templates preconfiguring metadata, traffic allocation, targeting and metrics at experiment creation, for consistency rather than rationale ("Experiment Templates provide standardized configurations for experiment creation across your team."). [vendor]

<a id="ref-32"></a>[32] Eppo. "[Mutual exclusion (Layers)](https://docs.geteppo.com/feature-flagging/concepts/mutual_exclusion/)." Eppo documentation (accessed 2026-10-08). Supports mutually exclusive experiments as an option for tests on the same surface, and the vendor's own reported position that interaction effects are rare, citing unread Microsoft research ("Research from Microsoft has shown that in practice interaction effects are vanishingly rare."). [vendor]

<a id="ref-33"></a>[33] Eppo. "[Interaction Detection](https://docs.geteppo.com/statistics/interaction-detection/)." Eppo documentation (accessed 2026-10-08). Supports two named ways concurrent experiments can interact, assignment dependence and effect interaction, and the statistical test used to detect each ("Experiments can interact in two possible ways"). [vendor]

<a id="ref-34"></a>[34] GrowthBook. "[Experimentation Best Practices](https://docs.growthbook.io/using/experimentation-best-practices)." GrowthBook documentation (accessed 2026-10-08). Supports the vendor's own position that meaningful interactions between parallel tests are rare, with mutually exclusive tests available when needed ("meaningful interactions are actually quite rare, and keeping a higher rate of experimentation is usually more beneficial"). [vendor]

<a id="ref-35"></a>[35] Itamar Gilad. "[Product Discovery With ICE and The Confidence Meter](https://itamargilad.com/the-tool-that-will-help-you-choose-better-product-ideas/)." itamargilad.com (accessed 2026-10-08). Supports a graded scale for the evidence behind an idea, assessed before committing resources ("There is only one way to calculate confidence - looking for supporting evidence."). [practitioner]
