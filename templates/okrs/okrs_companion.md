# OKRs: companion

The reference document behind the `okrs` templates. Written for two readers: someone filling the template
who wants to know why a section exists, and someone deciding whether this document type is worth having at
all. Every non-obvious claim carries a citation to
[`okrs_research-log.md`](okrs_research-log.md), which is the declared source of truth for this bundle.

## 1. Orientation

An OKR set states **what measurable change you expect in this period, and how you will know whether you got
it.** It is one Objective, a short and qualitative statement of what you are trying to achieve, plus a small
number of Key Results, each a measurable outcome that would tell you the Objective happened. Google's own
guidance is "Pick just three to five objectives..." with "Determine around three key results per objective"
[[4]](#ref-4).

It sits **below** the product strategy, which chooses which problems are worth solving, and **beside** the
roadmap, which orders the work. It is the family's only member that answers "did it work."

At a glance:

- **A Key Result that names an activity is not a Key Result.** Google's own test is a word list: if a Key
  Result contains "consult," "help," "analyze," or "participate," it describes an activity, not an outcome
  [[13]](#ref-13).
- **Nothing measures whether writing OKRs improves product or business outcomes.** That is a confirmed gap,
  searched for, and it is the most important thing on this page.
- **The sentence to reach for when OKRs get confused with a plan:** the roadmap shows the plan, the OKRs
  carry the commitment.
- **One format ships.** Six candidates were examined individually and five rejected; nine further named
  frameworks were then checked for a counterexample and none qualified. The rejections are the useful result.
- This is the **only methodology-bound document type in its family**: the artifact *is* the method.

**On evidence, plainly.** Two things are true at once and the bundle refuses to blur them.

Goal-setting theory is real, old and replicated. Specific difficult goals outperform "do your best," with
meta-analytic effect sizes of **.42 to .80** on that comparison, and separately **.52 to .82** on goal
difficulty, established across "well over 100 different tasks involving more than 40,000 participants in at
least eight countries" [[21]](#ref-21). A genuine adversarial literature sits alongside it, arguing that the
benefits have been overstated and the harms ignored [[22]](#ref-22), and its authors received a published
rebuttal in the same journal issue [[23]](#ref-23). Both sides are real scholarship.

**Neither side mentions OKRs.** Not the term, not quarterly cadence, not scoring [[21]](#ref-21)[[22]](#ref-22).
The academic literature on the OKR artifact itself is thin: a systematic mapping identifies 47 primary studies
and its own authors call the topic "under-documented from a theoretical point of view" [[24]](#ref-24). The
best in-situ industry study, 47 interviews and 512 survey responses inside a large software company, measured
engineer perceptions and process friction rather than delivery outcomes [[25]](#ref-25).

So the move from "specific difficult goals work" to "the OKR format works" is an **assumption**. It is made
constantly in vendor content, including by pieces that argue OKRs are backed by goal-setting science without
citing the goal-setting literature at all [[26]](#ref-26). This bundle will not make that move. The one place
the adjacent literature touches quarterly cadence directly, it is a caution about short-termism rather than an
endorsement [[22]](#ref-22).

## 2. Origins and evolution

**The outline is well attested. The specifics that circulate are not.**

Andrew Grove built a goal system at Intel and documented it in *High Output Management* (1983). Its core is
two questions, and the second one produces the phrase everything else is built on: "A successful MBO system
needs only to answer two questions: 1. Where do I want to go? (The answer provides the objective.) 2. How will
I pace myself to see if I am getting there? (The answer gives us milestones or key results)"
[[1]](#ref-1). **That passage is quoted here from a secondary rendering**, because the primary chapter could
not be reached; the accessible portion of the book contains no instance of the acronym "OKR" and no mention of
Drucker, and that is a gap in access rather than a confirmed absence [[12]](#ref-12).

John Doerr learned the method at Intel and carried it to Google. He is explicit about the credit: "Andy
invented a system called 'Objectives and Key Results'" [[2]](#ref-2), and "They are Andy Grove's invention,
but I'm the messenger" [[3]](#ref-3). Wikipedia, citing Doerr's own book, records that when he met it in 1975
the method was "then called 'iMBOs'..." [[8]](#ref-8), which is a source close to Doerr indicating the name he
encountered was not "OKR."

**Three things that circulate as fact do not survive checking.**

**The year OKRs reached Google is given as three different years by three sources that should be
authoritative.** Doerr's own site says 1998 [[3]](#ref-3). Doerr's own TED talk says 1999 [[2]](#ref-2).
Google's own guide says "A few decades later in early 2000, Doerr introduced OKRs to Google's leadership"
[[4]](#ref-4). State the range, never a single year.

**The Drucker lineage is asserted everywhere and sourced nowhere.** Doerr's site says Grove "found it in the
work of Peter Drucker, who had introduced MBOs, or Management by Objectives, in the 1950s" [[5]](#ref-5),
with no citation to anything Grove said. Drucker did originate the term, in 1954 [[9]](#ref-9). But the two
lineages are documented separately: the encyclopedia article on management by objectives does not mention
Grove, Intel or OKRs, and the article on OKRs does not mention Drucker [[8]](#ref-8)[[9]](#ref-9). Treat the
chain as plausible and unverified.

**Grove-as-inventor is disputed by name.** "We should all be simply giving Grove credit for a more effective
way to implement MBO. Instead, the world has declared him the 'inventor' of something called OKRs even though
OKR and MBO are based on the same principles and follow roughly the same process" [[10]](#ref-10). That is
one side of a branding dispute rather than settled fact, and it belongs here because it is the strongest
challenge to the standard story.

The canonical worked example from the Intel era is Operation Crush, whose objective was to "Establish the
8086 as the highest performance 16-bit microprocessor family" [[6]](#ref-6).

**One more caution.** The formula that circulates as OKR shorthand, "I will [Objective] as measured by [Key
Results]," appears on Doerr's own FAQ **attributed to nobody** [[7]](#ref-7), and the book that would settle
its origin could not be retrieved. Use the formula; do not attribute it.

## 3. Anatomy (section by section)

### The Period and What This Serves

Which cycle this covers, and which document above it this set exists to move. One short paragraph.

It is first because it is the section that makes everything below it arguable. An Objective with no parent
cannot be traded off against anything, and the commonest way an OKR set goes wrong is not a badly written Key
Result but a set that nobody can connect to a decision anyone made. Naming the parent turns "is this a good
Objective" into "does this move that," which is a question with an answer. See section 8 for where each
neighbouring document draws its line.

### Objective

What you are trying to achieve, stated qualitatively and memorably. It is the "what," not the "how much."
A good Objective is the thing a team could repeat from memory a month later.

### Key Results (lean and full)

The measurable outcomes that would prove the Objective happened. This is where the document lives or dies.

**The outcome rule, in Google's own words:** Key Results "must describe outcomes, not activities. If your KRs
include words like 'consult,' 'help,' 'analyze,' or 'participate,' they describe activities. Instead, describe
the end-user impact of these activities: 'publish average and tail latency measurements from six Colossus
cells by March 7,' rather than 'assess Colossus latency'" [[13]](#ref-13). That word list is a check you can
run on your own draft in ten seconds, which is what makes it the most useful sentence in this bundle.

**The rule is dominant, not unanimous, and the honest version says so.** Felipe Castro argues against forcing
everything into outcome form: "Not everything needs to be an outcome-or an OKR," recommending that work whose
outcome genuinely cannot be measured yet, such as security and compliance, goes into a due-dates bucket
instead [[17]](#ref-17). Perdoo's CEO concedes that "Milestone Key Results are great for projects that have
distinct phases of completion, such as the release of a new feature," while still holding outcome-based Key
Results as the default [[18]](#ref-18).

**How many.** Convention, not settlement. Google says three to five objectives and around three Key Results
each [[4]](#ref-4). A summary of Doerr's book reports "In general, each objective should be tied to five or
fewer key results" [[11]](#ref-11). One vendor recommends "the right number of Key Results is between 2 and 4"
from its own platform data [[15]](#ref-15). No disinterested source settles it.

### What This Set Is Not Committing To

Two to four things asked for, considered and deliberately left out of this cycle, each with a line on why.

This is the section that makes the Objective usable, and it ships in **both** sizes rather than only in full,
because a set that cannot refuse anything settles no arguments. Its test is the same one the sibling bundles
use for their exclusion sections: can you point at the sentence, name who asked, and say who told them no. An
exclusion list made only of things nobody wanted is worse than none, because it looks like a decision while
protecting nothing, and the hard refusals then arrive mid-cycle as interruptions nobody agreed to. See the
anti-patterns in section 7 for what that looks like in practice.

### Initiatives (full)

The projects and work items expected to move the Key Results. **This section is convention rather than canon,
and the bundle says so rather than hiding it.** One vendor asserts that "John Doerr's OKR framework consists
of Objectives, Key Results, and Initiatives" while citing no page or quote for the structural claim
[[49]](#ref-49), and **Google's own guide never names an initiatives layer at all** [[4]](#ref-4). Ship it if
it helps your team see the link from work to outcome. Do not present it as part of the original method.

**On ownership.** There is no Owners section, deliberately. Every Key Result and every Initiative carries a
named person **in its own row**, because ownership belongs attached to the thing owned. A standalone list of
owners is a list of names with nothing to be accountable for, and it is what lets an OKR set end up as
nobody's problem while appearing to have owners. A team name in that column is the same failure wearing a
plural.

### Confidence and check-in (full)

**Three different instruments get merged here constantly, and they come from three different people. Keep
them apart.**

| Device | Whose | What it does |
|---|---|---|
| **Forecast confidence, 1 to 10** | Christina Wodtke [[16]](#ref-16) | A weekly forward-looking bet on whether you will make it |
| **Grading, 0.0 to 1.0 with colour bands** | Google [[13]](#ref-13) | An after-the-fact score of what happened |
| **Committed against aspirational** | Google, reported by Doerr [[13]](#ref-13)[[11]](#ref-11) | Which target you were even aiming at |

Wodtke's version is explicit and worth quoting because it names its own failure mode: "One great way to do
this is to set a confidence level of five of ten on the OKR. A confidence level of one means 'never gonna
happen my friend.' A confidence level of ten is also known as sandbagging" [[16]](#ref-16). She recommends
adjusting it "every single week" [[16]](#ref-16).

Google's grading is separate: "We grade them with a color scale to measure how well we did: 0.0-0.3 is red,
0.4-0.6 is yellow, 0.7-1.0 is green" [[13]](#ref-13), with a stated sweet spot of "60% - 70%; if someone
consistently fully attains their objectives, their OKRs aren't ambitious enough and they need to think bigger"
[[4]](#ref-4).

And the committed/aspirational split is a third thing again: "Commitments are OKRs that we agree will be
achieved, and we will be willing to adjust schedules and resources to ensure that they are delivered," with an
expected score of 1.0, against aspirational OKRs that "express how we'd like the world to look, even though we
have no clear idea how to get there," with "an expected average score of 0.7, with high variance"
[[13]](#ref-13).

That split is **Google's**, not Grove's and not Doerr's invention: Doerr's own organisation describes Google
creating the second category for itself [[14]](#ref-14), and Doerr's book reports it as Google's practice
[[11]](#ref-11).

**None of these numbers is measured.** They are stated as internal convention in the source that introduces
them. Do not cite 0.7 as evidence that OKRs work; it describes a scoring philosophy.

### Scoring and close-out (full)

How the set gets graded at the end, and what the grade is allowed to do. Written at the start of the cycle,
completed at the end.

Grading is Google's device, and the bands are stated as internal convention rather than derived from
anything: red, yellow and green at 0.0-0.3, 0.4-0.6 and 0.7-1.0 [[13]](#ref-13). What makes this a section
rather than a footnote is the second half. **The decision that actually determines whether the next set is
honest is whether these grades touch anyone's pay or review**, and the practitioner position on that is close
to one-sided: Doerr carves out sales quotas and otherwise says do not [[29]](#ref-29), Google says OKRs "are
not synonymous with employee evaluations" [[4]](#ref-4), and Lamorte draws it precisely, that outcomes may
influence compensation while scores should not determine it [[34]](#ref-34). A template that lets an author
skip the question produces a team that assumes the answer, and the assumed answer is the one that makes them
write an easier set next cycle.

## 4. Variants and sizing

**Two sizes.** `lean` is the period and its parent, the Objective, the Key Results and what the set
deliberately excludes, which is the whole artifact and enough for a team that shares context. `full` adds
**Initiatives, Confidence and check-in, and Scoring and close-out**, for a set that will be read outside the
room, carried into a review, or handed to someone who was not there when it was written. **Ownership is not
one of the additions:** a named person sits in every Key Result row at both sizes, for the reason given in
section 3.

**One format ships.** The rule is
[ADR 0028 (the format-axis rule)](../../docs/internal/decisions/0028-adopt-a-format-axis.md): a format ships
only when it is **structurally distinct** from the default **and** in circulation with a named source.

**Six candidates were examined individually and five rejected**, below. A further **nine named goal-setting
frameworks** were checked separately for a counterexample, which is the last bullet. The two tiers are kept
apart because they got different scrutiny, and collapsing them into a single number is how the sibling bundle
came to claim "eight researched, five rejected" while naming six rejections.

The rejections matter more than the admission:

- **V2MOM**, Marc Benioff's Vision, Values, Methods, Obstacles, Measures, is genuinely structurally distinct.
  Five components against two, with slots for Values and Obstacles that OKR has no equivalent for
  [[20]](#ref-20). It is rejected anyway, because **the Salesforce training unit that defines all five
  components and tells the origin story does not mention OKRs once** [[20]](#ref-20). Its author does not
  present it as an OKR variant, so it is a different artifact rather than a different shape of this one.
- **OKRs-with-initiatives** is not a distinct format. It is this document's own full form.
- **Cascading or tiered OKRs** describe an organisational process, not a document anatomy. The document at
  every tier has the same two parts.
- **Vendor canvases and scorecards** are competing tracking layouts on the same anatomy, from no single named
  author.
- **Wodtke's OKR Four Square** is a named single-author artifact, which is more than the vendor layouts can
  claim, but it is a check-in worksheet layered on standard Objectives and Key Results rather than a
  redefinition of them [[16]](#ref-16).
- **OGSM, Hoshin Kanri, 4DX, Balanced Scorecard and others** were checked for a counterexample and none was
  found: each is published as a competing framework, and where a named author relates one to OKRs, OKRs are
  nested inside it rather than claimed as a variant of it.

**One ambiguity in the rule, stated rather than hidden.** ADR 0028 requires a format to be in circulation
with a named source, and does not say **in circulation as what**. Two readings are available. On the loose
reading, V2MOM is in circulation and has a named author, so it qualifies. On the strict reading, a format
*of a document type* must be in circulation **as that type**, and V2MOM fails because its author circulates
it as its own artifact. This bundle used the strict reading, and so did `product-roadmap` before it when it
excluded the opportunity solution tree and Cagan's alternative.

**Neither reading has been ratified, and the two are not interchangeable.** Under the loose reading this
bundle ships two formats rather than one. `product-vision`'s PR/FAQ was admitted without the question being
asked. So the disambiguation is a real, open decision affecting at least three bundles, and it belongs in the
`default_format` backfill (decision D-E), which already needs its own ADR. Recording it here is not a
substitute for making it.

## 5. Methodology lineage

**This is the only methodology-bound member of `strategy-docs`, and the family contract says so explicitly.**
A product vision, a product strategy and a product roadmap can each be written under any methodology. An OKR
set cannot: the artifact **is** the OKR method. That is why the family's contract makes `methodology`
descriptive rather than gated, because a single required value would force one of the four members to
misdescribe itself.

The practical consequence for a filler: adopting this template means adopting a set of commitments that come
with it, and they are contested rather than settled. The cadence is convention. The scoring scale is
convention. The visibility default is a choice. Section 6 is where those are argued, and it is not optional
reading if you are introducing OKRs rather than filling in an existing practice.

## 6. Debates and contested boundaries

**Should OKRs be tied to compensation?** This is close to one-sided among named voices, which is itself worth
knowing. Doerr: "Don't tie the OKR goals to bonus payments, except for sales quotas. We want to build a bold,
risk-taking culture" [[29]](#ref-29). Google: "OKRs are not synonymous with employee evaluations"
[[4]](#ref-4). Ben Lamorte draws the line precisely: "Business outcomes may influence compensation. OKR scores
should not determine compensation" [[34]](#ref-34). What Matters puts the mechanism plainly: "You don't want
to penalize people for aiming high" [[30]](#ref-30). **No source found argues for general compensation
linkage.** Sales quotas are the named exception both camps accept.

**Should OKRs cascade?** The slogan is Felipe Castro's: "OKRs never cascade. OKRs align" [[31]](#ref-31).
Wodtke agrees on the mechanism, that "cascading creates bottlenecks. Everyone waits on the layer above to
finalize goals" [[32]](#ref-32), and Lamorte on the cost: "real alignment does not come from arrows connecting
boxes. It comes from conversation, clarity, and shared understanding" [[33]](#ref-33).

**But the disagreement is narrower than the slogans.** All three still want leadership to set direction first,
and Google's own guidance recommends organisations "commit first to organizational objectives, so that teams
and individuals can set their own objectives in service of those larger goals" [[4]](#ref-4), which is a
top-down sequencing step. The real fault line is whether Key Results get mechanically copied downward to
become the next level's Objectives, which every named source rejects, against direction flowing down with
objectives negotiated locally, which is what essentially everyone including Google actually does. Note also
that Doerr's own organisation describes OKRs flowing "downwards to department heads, managers, and individual
employees" [[53]](#ref-53) and gives **no** bottom-up percentage, despite a specific figure circulating widely.

**Is quarterly right?** It is convention, and no source of any tier offers comparative evidence for three
months over any other period. Castro calls it out: "It is a common misconception that OKR only works with
quarterly cycles, which was the model Google used until 2011" [[50]](#ref-50), replacing evidence with a
heuristic rather than data. John Cutler goes further: "quarterly planning hurts because it happens too
infrequently (and at an artificial cadence)," and "90.25 days might be perfect for your company, 60 for the
next, 30 for the next" [[40]](#ref-40). Google itself runs annual alongside quarterly [[4]](#ref-4).

**Must OKRs be public?** Google's default is yes: "OKRs are public so that everyone in the organization can
see what others are working on" [[4]](#ref-4). The clearest named dissent allows explicit carve-outs: "Transparency
is the default, but it's not absolute. Knowing when to keep goals private is a sign of thoughtful leadership,
not secrecy" [[51]](#ref-51), naming acquisitions, restructuring, personal development goals and
public-company financial exposure.

**And the strongest voices on both sides concede.** Doerr: "OKRs are not a silver bullet. They won't
substitute for good judgment and a strong culture" [[3]](#ref-3). Wodtke: "not everyone needs to set OKRs,"
and "I've botched OKRs more times than I can count" [[32]](#ref-32). **Rick Klau, whose video made OKRs famous
inside Google's ecosystem, published a public correction of his own guidance a decade later**, telling first-time
adopters to "ignore individual OKRs," calling his own earlier metric examples "are, well, not great!", and
warning that review linkage will "encourage your teams to sandbag their OKRs" [[19]](#ref-19).

From the other direction, a piece titled "Are OKRs 'Management Malpractice'?" concludes that "The best use of
OKRs is for multi-directional alignment" [[38]](#ref-38). A critic who writes that "Every single other time,
the OKRs have been bullshit, gamed, a wish-list, or a task-list" still reports one period where they worked
and names the conditions [[36]](#ref-36). And an academic critic who calls goal transparency "a panopticon, a
hardly visible but strongly felt control" still holds that "clear goals are still needed to enable thriving"
[[39]](#ref-39).

## 7. Anti-patterns and failure modes

1. **Key Results that are tasks or KPIs in disguise.** Run Google's word test [[13]](#ref-13). A vendor's
   analysis of its own platform found "52% were tasks or KPIs in disguise" [[15]](#ref-15), which is
   directional vendor data about one defect rather than a ranking against the failures below. **No source
   found ranks these anti-patterns against each other**, so this list is not in frequency order.
2. **Sandbagging.** Setting a target you already know you will hit. "Teams almost always sandbag their OKRs.
   Setting goals they know they can hit assures they not only keep their jobs but get their bonuses"
   [[35]](#ref-35). Google names it as a trap in its own playbook [[13]](#ref-13).
3. **Compensation coupling.** The mechanism behind sandbagging, and the reason the practitioner consensus is
   to keep them apart [[29]](#ref-29)[[34]](#ref-34).
4. **Cascading as waterfall.** Key Results copied downward to become the next level's Objectives, producing
   bottlenecks and silos rather than alignment [[31]](#ref-31)[[32]](#ref-32)[[33]](#ref-33).
5. **OKR theatre.** A full cycle of writing, scoring and reviewing that changes no prioritisation. Catalogued
   with nine hallmarks, including too many OKRs at once, non-measurable Key Results, and cascading that
   mirrors the org chart [[37]](#ref-37).
6. **Watermelon reporting.** Green on the dashboard, red underneath [[41]](#ref-41).
7. **Individual OKRs treated as a performance review.** Google says the two are not synonymous
   [[4]](#ref-4), and the author of the video that made OKRs famous inside Google's ecosystem reversed
   himself specifically on this point [[19]](#ref-19)[[8]](#ref-8).
8. **A cadence that does not match the work.** Ninety days applied regardless of how long anything actually
   takes [[40]](#ref-40).
9. **Layering OKRs onto an unchanged output-based process.** Named as the root of much of the backlash:
   "countless thousands of companies that thought that they could layer in the OKR technique on top of their
   existing, output-based product roadmap processes" [[42]](#ref-42).

## 8. Relationships to other artifacts

The family runs downhill, and this document is at the bottom of it: a **product vision** says where you are
going, a **product strategy** says which problems you will solve to get there, a **product roadmap** says in
what order, and **OKRs** say what measurable change you expect this period and whether you got it.

| This document | That document | The boundary |
|---|---|---|
| OKRs | product vision | Different horizons and different jobs. A vision states the destination and changes on a timescale of years; an OKR set states what measurable change one period should produce on the way there. A vision that changed quarterly was never a vision, and an OKR set that did not would not be doing its job. The family's own contract splits them on exactly this line, `foundation` against `utility` |
| OKRs | product strategy | OKRs are "a complement to strategy, not a substitute for strategy" [[45]](#ref-45). A list of objectives with no where-to-play choice behind it is, in Roger Martin's phrase, OKRs masquerading as strategy. His diagnostic: "Whenever anyone refers to their 'strategies,' I know they don't know what strategy is" [[45]](#ref-45). Pichler puts it structurally: "a product strategy is more than a collection of OKRs. It provides the basis for discovering the right objectives" [[43]](#ref-43) |
| OKRs | product roadmap | Compatible, and the two named positions differ on how cleanly. Pichler treats a roadmap goal as usable directly as an Objective if it is measurable [[44]](#ref-44). Cagan is harder: the technique "originated from, and is predicated upon, the product model," so bolting it onto an output roadmap is a category error rather than a slip [[42]](#ref-42) |
| OKRs | KPI dashboard | A KPI is a steady-state health metric; a Key Result is a goal metric. The lifecycle is the useful part: "KPIs often inform - and even become - your OKRs, if it's a measurement that you want to significantly change" [[46]](#ref-46), and the metric can revert to KPI status once the change lands. Worth carrying the dissent: "Switching from KPIs to OKRs doesn't fix neglect. It just gives neglect a more ambitious name" [[47]](#ref-47) |
| OKRs | project plan or backlog | "If OKRs are a compass, then your project plan is a GPS that takes you from Point A to Point B turn by turn" [[48]](#ref-48). Unfinished backlog work does not automatically become next period's Objective |

## 9. Adaptations

**Non-quarterly cadence.** Legitimate and under-used. Match the period to how fast you actually learn, and
write down which you chose and why [[50]](#ref-50)[[40]](#ref-40). **Do not borrow another company's cadence
from a blog post without checking it.** Spotify is widely cited as running a six-month and six-week variant of
OKRs; the person who wrote up the system describes it as what Spotify arrived at **after** moving away from
OKRs, which were later reintroduced alongside it [[52]](#ref-52).

**Partial visibility.** Default to public; carve out acquisitions, restructuring, personal development goals
and financial exposure, and say that the carve-out exists rather than hiding it [[51]](#ref-51).

**Teams that should not set OKRs at all.** Wodtke's boundary condition is worth honouring, and she states it
plainly: "not everyone needs to set OKRs" [[32]](#ref-32).

**Vendor tooling.** If you adopt an OKR tool, note that its data model may add an Initiatives layer that no
primary source establishes [[49]](#ref-49). That is fine as tooling. It is not the
method.

**A note on borrowed statistics.** OKR content on the open web carries a large number of untraceable
percentages, and at least two circulating claims attach real institutional names to studies that a direct
search could not find [[28]](#ref-28). The most-repeated impact figures trace to an internal company analysis
that was never peer-reviewed or published [[27]](#ref-27). If you need a number to justify adopting OKRs, the
honest answer is that you do not have one.

## 10. Worked example

[`okrs_example.md`](okrs_example.md) is a filled `full` variant for Acme Analytics, the scenario this library
carries from a product vision down to a bug report. Its Objective is the FY26 "Time to Insight" company goal
that the [PRD example](../prd/prd_example.md) cites and the
[KPI dashboard example](../kpi-dashboard/kpi-dashboard_example.md) tracks, so the example is the point where
the library's measurement layer and its direction layer meet.

## References

<a id="ref-1"></a>[1] Nat Eliason. "[High Output Management by Andy Grove: Notes and Review](https://www.nateliason.com/notes/high-output-management-andy-grove)." [practitioner] Cited as a secondary rendering of Grove's MBO chapter; the primary chapter could not be reached.

<a id="ref-2"></a>[2] John Doerr. "[Why the secret to success is setting the right goals](https://singjupost.com/why-the-secret-to-success-is-setting-the-right-goals-john-doerr-transcript/)," TED (2018), transcript. [primary] Read on a third-party transcript host.

<a id="ref-3"></a>[3] What Matters. "[OKRs Explained: John Doerr course intro](https://www.whatmatters.com/okrs-explained/why-okrs-john-joerr)." [vendor] Doerr's own organisation.

<a id="ref-4"></a>[4] Google re:Work. "[Set goals with OKRs](https://rework.withgoogle.com/intl/en/guides/set-goals-with-okrs)." [primary] Google's own account of its own practice.

<a id="ref-5"></a>[5] Giulia Pines. "[The Origin Story](https://www.whatmatters.com/articles/the-origin-story)," What Matters (2025). [vendor] The Drucker-lineage claim on this page carries no citation to anything Grove said.

<a id="ref-6"></a>[6] What Matters. "[OKR Example from John Doerr: How Intel Achieved their Goals](https://www.whatmatters.com/okrs-explained/john-doerr-operation-crush)." [vendor]

<a id="ref-7"></a>[7] What Matters. "[How to write OKRs with examples](https://www.whatmatters.com/faqs/okr-examples-and-how-to-write-them)." [vendor] States the formula and attributes it to nobody.

<a id="ref-8"></a>[8] Wikipedia. "[Objectives and key results](https://en.wikipedia.org/wiki/Objectives_and_key_results)." [reference]

<a id="ref-9"></a>[9] Wikipedia. "[Management by objectives](https://en.wikipedia.org/wiki/Management_by_objectives)." [reference] Cited for a checkable negative: this article does not connect MBO to Grove, Intel or OKRs.

<a id="ref-10"></a>[10] Balanced Scorecard Institute. "[No, Andy Grove Didn't Invent OKRs and Other 'Stake-Your-Claim' Problems](https://balancedscorecard.org/blog/no-andy-grove-didnt-invent-okrs-and-other-stake-your-claim-problems/)." [practitioner] One side of a branding dispute, from an institute with a competing methodology.

<a id="ref-11"></a>[11] Graham Mann. "[Measure What Matters by John Doerr: Book Summary and Notes](https://grahammann.net/book-notes/measure-what-matters-by-john-doerr)." [practitioner] A summariser's rendering; Doerr's primary text could not be retrieved.

<a id="ref-12"></a>[12] Andrew Grove. *High Output Management* (1983), [Internet Archive full-text stream](https://archive.org/stream/dli.ernet.213936/213936-High%20Output%20Management_djvu.txt). [primary (book)] **Read only in part**, stopping short of the MBO chapter, so the absence of "OKR" is a research gap and not a confirmed absence.

<a id="ref-13"></a>[13] Google. "[Google's OKR Playbook](https://assets.ctfassets.net/mu244eycyvsr/3T7YZSUplO5Wt2UMpHKBoF/70ca14665b9735a7f7cff5f4c95c34df/WhatMatters.com_-_Google_s_OKR_Playbook.pdf)." [primary] Internal Google document, reprinted with Google's permission.

<a id="ref-14"></a>[14] Lisa Shufro. "[Committed vs. Aspirational OKRs: What's the Difference?](https://www.whatmatters.com/faqs/committed-aspirational-okrs-examples-difference)," What Matters. [vendor]

<a id="ref-15"></a>[15] OKRs Tool. "[How Many Key Results Per Objective?](https://www.okrstool.com/blog/how-many-key-results-per-objective)" [vendor] Proprietary platform data, not independently audited.

<a id="ref-16"></a>[16] Christina Wodtke. "[The Art of the OKR](https://cwodtke.com/the-art-of-the-okr/)." [practitioner] Author of *Radical Focus*; the confidence device is her named contribution.

<a id="ref-17"></a>[17] Felipe Castro. "[Not everything needs to be an outcome - or an OKR](https://read.felipecastro.com/p/what-if-you-cant-measure-the-outcome)" (2024). [practitioner]

<a id="ref-18"></a>[18] Henrik van der Pol. "[Different types of Key Results and when to use them](https://www.perdoo.com/resources/blog/different-types-of-key-results-and-when-to-use-them)," Perdoo. [vendor] The author is the vendor's CEO.

<a id="ref-19"></a>[19] Rick Klau. "[What my OKRs video got wrong](https://tins.rklau.com/2022/01/what-my-okrs-video-got-wrong/)" (2022). [primary] The original video's own author correcting himself.

<a id="ref-20"></a>[20] Salesforce Trailhead. "[Achieve Organizational Alignment with V2MOM](https://trailhead.salesforce.com/content/learn/modules/manage_the_sfdc_organizational_alignment_v2mom/msfw_oav2m_creating_org_alignment_v2mom)." [primary] Salesforce's own training material. **One unit of a longer module was read**; the OKR-absence claim is stated at that scope.

<a id="ref-21"></a>[21] Edwin A. Locke and Gary P. Latham. "[Building a Practically Useful Theory of Goal Setting and Task Motivation: A 35-Year Odyssey](https://med.stanford.edu/content/dam/sm/s-spire/documents/PD.locke-and-latham-retrospective_Paper.pdf)," *American Psychologist* 57(9), 705-717 (2002). [academic]

<a id="ref-22"></a>[22] Lisa D. Ordonez, Maurice E. Schweitzer, Adam D. Galinsky and Max H. Bazerman. "[Goals Gone Wild: The Systematic Side Effects of Over-Prescribing Goal-Setting](https://knowledge.wharton.upenn.edu/wp-content/uploads/2013/09/1359.pdf)," *Academy of Management Perspectives* 23(1), 6-16 (2009). [academic]

<a id="ref-23"></a>[23] Edwin A. Locke and Gary P. Latham. "[Has Goal Setting Gone Wild, or Have Its Attackers Abandoned Good Scholarship?](https://journals.aom.org/doi/10.5465/amp.2009.37008000)" *Academy of Management Perspectives* 23(1) (2009). [academic] **Not read**; cited only to establish that a published rebuttal exists in the same issue. No wording is quoted.

<a id="ref-24"></a>[24] R. Silva and G. Santos. "[Surveying the Academic Literature on the Use of OKR - An Update](https://journals-sol.sbc.org.br/index.php/isys/article/view/3885)," *iSys*, Brazilian Journal of Information Systems (2024). [academic]

<a id="ref-25"></a>[25] J. Butler, T. Zimmermann and C. Bird. "[Objectives and Key Results in Software Teams: Challenges, Opportunities and Impact on Development](https://arxiv.org/abs/2311.00236)," arXiv:2311.00236 (2023). [academic] Measured perceptions and process, not delivery outcomes.

<a id="ref-26"></a>[26] Jop. "[Debunking the Myth: Exploring the Effectiveness of OKRs as a Goal-Setting Framework](https://www.getjop.com/blog/debunking-the-myth-exploring-the-effectiveness-of-okrs-as-a-goal-setting-framework)." [vendor] Cited as evidence that vendor content asserting a scientific basis does not engage the literature.

<a id="ref-27"></a>[27] OKRs.com. "[Sears Holding Company Study Concludes OKRs Impact the Bottom Line](https://okrs.com/2015/03/sears-holding-company-study-concludes-okrs-impact-the-bottom-line/)" (2015). [vendor] An unpublished internal company analysis, never peer-reviewed.

<a id="ref-28"></a>[28] The OKR Hub. "[Why OKRs Fail: The 7 Most Common Reasons](https://www.theokrhub.com/insights/why-okrs-fail)." [vendor] Cited only as the location of two statistics attributed to real institutions that a direct search could not trace.

<a id="ref-29"></a>[29] Betterworks. "[Keys to OKR Success: Q&A with John Doerr](https://www.betterworks.com/magazine/keys-okr-success-qa-john-doerr)." [primary] Direct interview.

<a id="ref-30"></a>[30] Valerie Gilbert. "[Should You Connect OKRs and Compensation? (Spoiler Alert: No)](https://www.whatmatters.com/articles/should-you-connect-okrs-and-compensation-spoiler-alert-no)," What Matters. [vendor]

<a id="ref-31"></a>[31] Felipe Castro. "[Why you should not cascade your goals](https://medium.com/the-alignment-shop/why-you-should-not-cascade-your-goals-c5f12020976a)." [practitioner]

<a id="ref-32"></a>[32] Christina Wodtke. "[What I've Learned from 15 Years of Doing OKRs](https://cwodtke.com/what-ive-learned-from-15-years-of-doing-okrs/)." [practitioner]

<a id="ref-33"></a>[33] Ben Lamorte. "[How to Align OKRs: Why Cascading Fails and What Works Instead](https://okrs.com/2026/02/align-okrs/)," OKRs.com. [practitioner]

<a id="ref-34"></a>[34] Ben Lamorte. "[OKRs and Compensation: 2 Mistakes to Avoid](https://okrs.com/2026/02/okrs-and-compensation/)," OKRs.com. [practitioner]

<a id="ref-35"></a>[35] Jeff Gothelf. "[OKR Anti-pattern: Sandbagging your key results](https://jeffgothelf.com/blog/sandbagging-okr-antipattern/)." [practitioner] "Almost always" is the author's characterisation, not a measured frequency.

<a id="ref-36"></a>[36] Tom Kerwin. "[OKRs sound good but they don't work (Part 1)](https://triggerstrategy.substack.com/p/okrs-sound-good-but-they-dont-work)," Trigger Strategy. [practitioner]

<a id="ref-37"></a>[37] Ant Murphy. "[Escape OKR Theatre](https://www.antmurphy.me/newsletter/escape-okr-theatre)." [practitioner]

<a id="ref-38"></a>[38] Daniel Walters. "[Are OKRs 'Management Malpractice'?](https://www.greatcto.me/p/are-okrs-management-malpractice)" [practitioner]

<a id="ref-39"></a>[39] Antoinette Weibel with Meike Wiemann. "[The Dark Side Of OKRs (And Why We Should Care)](https://www.corporate-rebels.com/blog/dark-side-of-okrs-and-why-we-should-care)," Corporate Rebels. [academic] The author is a professor of HRM, writing on a practitioner platform.

<a id="ref-40"></a>[40] John Cutler. "[Why Quarterly OKRs?](https://medium.com/hackernoon/why-quarterly-okrs-88113e885f56)" [practitioner]

<a id="ref-41"></a>[41] Steven Macdonald. "[Goal Gaming: Why 92% of Employees Do It](https://www.okrstool.com/blog/goal-gaming)," OKRs Tool. [vendor] A self-report survey of 210 employees run by a vendor; directional only.

<a id="ref-42"></a>[42] Marty Cagan. "[Outcomes Are Hard](https://www.svpg.com/outcomes-are-hard/)," Silicon Valley Product Group. [practitioner]

<a id="ref-43"></a>[43] Roman Pichler. "[How to Combine Product Strategy, OKRs, and KPIs](https://www.romanpichler.com/blog/product-strategy-okrs-and-kpis)." [practitioner]

<a id="ref-44"></a>[44] Roman Pichler. "[OKRs and Product Roadmaps](https://romanpichler.medium.com/okrs-and-product-roadmaps-5c00773b32c0)." [practitioner]

<a id="ref-45"></a>[45] Roger Martin. "[Stop Letting OKRs Masquerade as Strategy](https://rogermartin.medium.com/stop-letting-okrs-masquerade-as-strategy-a57fc2cea915)." [practitioner] Former Dean, Rotman School of Management. A strong normative position, not a neutral description.

<a id="ref-46"></a>[46] Danielle Hughes. "[The Difference Between KPIs and OKRs](https://www.whatmatters.com/resources/difference-between-okr-kpi)," What Matters. [vendor]

<a id="ref-47"></a>[47] Ted Jackson. "[OKRs vs. KPIs](https://www.clearpointstrategy.com/blog/okrs-vs-kpis)," ClearPoint Strategy. [vendor] A minority framing relative to the cleaner separation in [46].

<a id="ref-48"></a>[48] Billy Casey. "[Dear Andy: Are We Doing OKRs or Just Project Planning?](https://www.whatmatters.com/faqs/dear-andy-are-we-doing-okrs-or-just-project-planning)," What Matters. [vendor] **The byline is a staff writer, not John Doerr**, despite the column's framing.

<a id="ref-49"></a>[49] Profit.co. "[From Doerr's Book to Your Dashboard: Where Do Initiatives Actually Belong in OKRs?](https://www.profit.co/blog/okr-university/from-doerrs-book-to-your-dashboard-where-do-initiatives-actually-belong-in-okrs/)" [vendor] Cited for a negative: it asserts the three-layer structure without citing a page.

<a id="ref-50"></a>[50] Felipe Castro. "[How to find the right OKR cadence](https://www.perdoo.com/resources/blog/okr-cadence)," Perdoo. [vendor] Castro is an independent coach publishing on a vendor blog.

<a id="ref-51"></a>[51] Nicole Capobianco. "[When it's ok NOT to be transparent with OKRs](https://www.perdoo.com/resources/blog/when-its-ok-not-to-be-transparent-with-okrs)," Perdoo. [vendor]

<a id="ref-52"></a>[52] Henrik Kniberg. "[Spotify Rhythm - how we get aligned](https://blog.crisp.se/2016/06/08/henrikkniberg/spotify-rhythm)," Crisp (2016). [practitioner] Cited as a correction: Rhythm is what Spotify reached after moving away from OKRs, not a variant of them.

<a id="ref-53"></a>[53] What Matters. "[Cascading top-down OKRs: What are some examples?](https://www.whatmatters.com/faqs/cascading-top-down-okr-examples)" [vendor] Cited for a negative: it gives no bottom-up percentage.
