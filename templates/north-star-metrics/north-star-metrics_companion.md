# North Star Metric: the companion

The reference behind the template. Read this when you want to know *why* a section exists, what the
research actually says, and where the field disagrees with itself.

## 1. Orientation

A North Star Metric document names the single measure of customer value that shows a product's strategy is
working, states why that metric and not another, and names the small set of input metrics a team can
actually move to drive it [[1]](#ref-1)[[48]](#ref-48). It does not set a target and it is not a dashboard:
the number it names is explained here and calculated, sourced and tracked in `kpi-dashboard`.

At a glance:

- Formalized as a named framework by one publisher, Amplitude, across two documents that both reserve all
  rights [[1]](#ref-1)[[2]](#ref-2). This companion's field names, section names and layout are its own, not
  Amplitude's, and no Amplitude worksheet, checklist wording or worked example appears here as this template's
  own.
- Amplitude's own accounts name three qualities: it represents the value a customer gets, it sits within
  product and marketing's own influence, and it leads revenue rather than reports it [[1]](#ref-1)[[22]](#ref-22).
- It is meant to move only indirectly, through three to five input metrics a team owns [[1]](#ref-1)[[21]](#ref-21):
  "If you can move your North Star directly, it's probably not a good North Star." [[1]](#ref-1)
- Who coined the term is contested: one community wiki credits Sean Ellis [[7]](#ref-7), and neither of
  Amplitude's two framework documents mentions him. Whether Amplitude invented the practice is not settled by
  anything this research read firsthand. See Origins, below.
- Where it sits relative to the product strategy and OKRs is contested. This library places it third,
  between the strategy and the roadmap, and names that placement a POSITION rather than a finding.

## 2. Origins and evolution

Amplitude, with John Cutler credited as co-author, formalized the North Star Framework in a 63-page playbook
and a companion workshop guide, both copyrighted 2024 [[1]](#ref-1)[[2]](#ref-2). The playbook states the
definition: "The North Star Framework is a product
management model based on a single metric" [[1]](#ref-1) that "best captures the value customers derive from
your product" [[1]](#ref-1). Amplitude's own hub page repeats the same three qualities in FAQ form
[[3]](#ref-3).

**Who coined the term is contested.** One community reference wiki states it outright: "According to Sean
Ellis, who coined this term, this is the single metric that best captures the core value that your product
delivers to customers." [[7]](#ref-7) Nothing else this research read firsthand says so. Neither Amplitude
document cites Sean Ellis, GrowthHackers or growth hacking anywhere in its text or its six endnotes, which
instead cite Andrew Chen, Jabe Bloom, a LinkedIn post and Ben Horowitz. Intercom's write-up of its interview
with Ellis, in its own narration rather than in Ellis's words, calls the metric "Sean's way of quantifying the point where customers
experience the value of your product" and "a key cog in a sustainable growth strategy" [[4]](#ref-4). In that
same interview Ellis makes an explicit authorship claim for "growth hacking" ("I came up with the phrase")
without making the equivalent claim for the North Star Metric [[4]](#ref-4). A secondary digest also
attributes the coining to him; this research did not read that digest, so nothing here rests on it. Treat
the question as open.

Ellis's own worked examples, in his own words, are Airbnb's nights booked and Facebook's daily active users
[[4]](#ref-4), and he draws a boundary this bundle keeps: "I don't think the North Star Metric is necessarily
the same thing" as "the one metric that matters" right now; the North Star is "a persistent overall success
metric" [[4]](#ref-4) (see Debates, below, on the related One Metric That Matters).

**The leading-indicator story the vendors retell comes from Netflix's DVD years.** Gibson Biddle, then VP of
Product at Netflix, needed a leading indicator for retention while DVDs still shipped by mail: "our
'percentage of new members who add at least three titles to their queue during their very first session with
the service' is a good example" [[2]](#ref-2). Amplitude and Mixpanel both retell the story, Mixpanel calling
it "the classic example" [[2]](#ref-2)[[26]](#ref-26), though both are secondhand retellings of Biddle's
account rather than a reading of Biddle's own words.

**The exemplar institution has changed its own answer at least three times.** Amplitude says so of itself
[[22]](#ref-22), and one of those changes is documented first-person by its then-CPO: from "weekly querying
users" to a measure it calls the weekly learning user, with three new input metrics named alongside the change
[[23]](#ref-23).
That history is this bundle's strongest evidence that changing a North Star, done deliberately, is not a
failure of the framework; see Definition History, below.

**The method is growth and the North Star Framework, not a goal-setting method.** Amplitude's own playbook
lists "a goal-setting framework, like objectives and key results (OKRs)" among the things the North Star
Framework explicitly is not [[1]](#ref-1), "although the North Star can be a strong foundation upon which to
base goals" [[1]](#ref-1). See Relationships, below, for how this bundle keeps the two apart.

## 3. Anatomy (section by section)

The sections below follow the template in order. Lean carries the first five; full adds the next four.

### The North Star

The metric's name and its one-sentence definition, in Amplitude's own fill-in shape, reported here and not
reproduced as this template's own wording: "Our North Star Metric is called X, which we define as Y."
[[1]](#ref-1) Two independent sources add what that sentence needs beyond a name: a behavior counted "across
a sensible time window, like weekly" [[49]](#ref-49), stated so "people can explain, inspect and reproduce"
it [[51]](#ref-51). Where a company runs more than one product, this section names which product the North
Star belongs to [[10]](#ref-10)[[48]](#ref-48).

**Where the exact calculation lives is this library's own position, not a finding.** No source read asks
whether a North Star document should carry the formula or leave it to a separate specification; the sources
that name a North Star state its behavior and its window wherever they name it at all, and this bundle keeps
that much. The calculation, data source, exclusions, targets and refresh belong to `kpi-dashboard`, per the
maintainer's ruling of 2026-10-12. No source read proposes a time-based measure as a North Star either; this
research treats that as an absence in what it found, not as a rule against one.

### Why This Metric

The case for this metric over another, against Amplitude's own checklist questions, reported as the
publisher's own wording: "Does it express customer value?" [[1]](#ref-1), "Is it a leading indicator of
success?" [[1]](#ref-1), "It's not a vanity metric?" [[1]](#ref-1). Amplitude's own instruction is to check
the claim against the company's own data: "Validate that it predicts retention and revenue in your own data."
[[22]](#ref-22) A separate vendor states where that customer-value sentence has to come from: "You cannot
write this sentence by staring at a dashboard. You write it by" listening to customers describe value "in
their own words" [[50]](#ref-50).

**The guide carries the one-sentence test, not this section.** "Everyone from sales to engineering should be
able to say what it means in one sentence." [[48]](#ref-48) It is a rubric row, per decision procedure 12,
because it grades the finished sentence rather than asking a new question.

### Input Metrics

Amplitude names three to five inputs as "influential, complementary factors that you believe most directly
affect your North Star Metric and that your team can directly influence through your product"
[[21]](#ref-21), and offers a heuristic for finding them in two slightly different forms: breadth, depth,
frequency and efficiency in one article [[21]](#ref-21), and breadth, depth, frequency and an open "Other" in
its workshop worksheet [[2]](#ref-2). This bundle reports both as Amplitude's own and prescribes neither as the
template's. A
rival vendor instead structures inputs as a hierarchy: "A metric tree is a logical hierarchy of your growth
model that maps how input metrics...feed into focus metrics, which in turn impact your North Star."
[[24]](#ref-24) This section reports both and prescribes neither. Each input gets a named owner: "Each input
is something a specific team can own and affect directly." [[48]](#ref-48)

**What this section deliberately stops short of** is a tree of metrics below the inputs. The catalog lists a
metric tree as its own document type, with the North Star at its top node, so this bundle does not duplicate
it here.

### What It Serves

Amplitude's own two-part definition folds strategy into the metric itself: "A good North Star Metric consists
of two parts: A statement of your product vision" and "A metric that serves as a key measure of your current
product strategy." [[21]](#ref-21) A separate workshop prompt asks the business-impact question directly:
"What will the impacts to the business be?" [[2]](#ref-2) One newsletter's own takeaway from an Ellis
interview adds that the metric "should correlate with revenue growth but should not be revenue itself"
[[52]](#ref-52); treat that phrasing as the newsletter's gloss, not Ellis's own words, and see Debates, below,
on where this section sits relative to the strategy and OKRs documents.

### When We Revisit It

Amplitude's own template asks for a trigger, not a date: "What will be your signal to revisit this metric?"
[[1]](#ref-1) Its hub page adds that the trigger is usually a shift: "whenever there's a significant shift in
your product, market, or business strategy" [[3]](#ref-3). A reference article states the same rule from the
other direction: "Only change the NSM when strategy or product fundamentally shifts" [[10]](#ref-10), and
Spotify's own glossary names the stakes: "Changing the north star is a significant organizational decision."
[[11]](#ref-11) This section asks for the trigger. See Debates, below, for why it does not ask for a cadence.

### Candidates Considered (full)

Amplitude's own worked example shows what this section catches: a delivery app "had considered potential
North Star Metrics like 'People Opening the App,' 'Scheduled Deliveries,' or 'Early Deliveries.' But there
was a problem: These metrics masked the real drivers of user retention and customer lifetime value (CLTV)"
[[1]](#ref-1), reported here, not reused as this template's own scenario. Amplitude's own instruction names
the comparison directly: "Your team selected this metric over something like 'total number of items
delivered monthly' or 'total order value' because your data shows that customers value on-time deliveries"
[[22]](#ref-22). Two further sources give the test for ruling a candidate out: "Total registered users,
cumulative downloads, and pageviews only go up. A metric that can never fall cannot warn you when something
is wrong." [[48]](#ref-48) "Total signups, page views, and registered users all fail that test."
[[49]](#ref-49)

### Guardrails (full)

**This section does not rest on Amplitude's canon, and the companion says so plainly.** Amplitude's two
documents never use "guardrails" to mean a tracked measure beside the North Star; its one use of the word
describes anti-examples brainstormed during the definition workshop, to "set helpful guardrails when you're
defining your metric and inputs later on" [[2]](#ref-2), not a field in the finished document. The pairing
this section is built on comes from three other sources: "The fix is pairing your north star with guardrail
metrics like retention and gross margin." [[49]](#ref-49) "Pair the shared measure with checks for harm or
declining quality." [[51]](#ref-51) A reference article lists the shape: "Guardrails: Quality and economics
limits to prevent 'hitting the target but missing the point.'" [[10]](#ref-10) Two vendors scope the same word
more narrowly, to a single experiment's safety check rather than a standing companion to the North Star:
Mixpanel calls guardrail metrics "secondary metrics that you monitor while conducting experiments and A/B
testing" [[25]](#ref-25), and Spotify's glossary defines one as "monitored during an experiment to ensure the
change doesn't cause unintended harm" [[11]](#ref-11). See Debates, below.

### What It Does Not Tell Us (full)

Amplitude's own template asks the question directly: "What doesn't this metric tell you? Are any of those
questions or uncertainties more important to address?" [[1]](#ref-1) A reference article names the sharper
version of the same question: "How do we keep the NSM from being gamed?" [[10]](#ref-10) Spotify's glossary
names a structural limit worth stating here rather than assuming: "North star metrics tend to be high-level
and slow-moving." [[11]](#ref-11)

### Definition History (full)

A glossary entry states the discipline: "Preserve the old definition and explain the break in the series
rather than silently rewriting history." [[51]](#ref-51) A rival vendor states the same discipline as a
governance obligation: "Every metric should have clear documentation - how it's defined, calculated, and
where the data comes from," with "a log of decisions tied to metric shifts (who acted, when, why)."
[[24]](#ref-24) A reference article adds the reason: "Keep a versioned definition history to preserve
comparability." [[10]](#ref-10) Amplitude's own first-person account of replacing its North Star is this
bundle's worked illustration of what one entry in that history looks like [[23]](#ref-23).

## 4. Variants and sizing

The full variant earns its place on evidence: each of its four sections rests on at least two independent
publishers, which is the stop condition this bundle's own build was held to. Reach for full when the North
Star has already faced, or will soon face, real scrutiny: named alternatives were seriously compared,
stakeholders will ask "why not X," or the definition has already changed once and the change needs a record.
Lean names the metric, the case for it, its inputs, what it serves and its revisit trigger, and stops there;
that is enough for a first pass or a small team where nobody is likely to ask what was rejected.

Guardrails ships in full only, and the note above is worth repeating here: it rests on three sources outside
Amplitude's own canon, not on the publisher that formalized the rest of the Framework. A team using the lean
variant is not skipping an Amplitude step by leaving it out.

Nothing in either variant carries a formula, a data source, a refresh schedule, a target, a threshold, a
dashboard layout, or a tree of metrics below the inputs. All of that is `kpi-dashboard`'s, by the maintainer's
own ruling, not a gap in the research.

## 5. Methodology lineage

The North Star Framework names itself apart from goal-setting methods by its own hand: Amplitude's playbook
lists OKRs and management-by-objectives among the things it is not [[1]](#ref-1). Its lineage is growth
practice, not a delivery or planning methodology; the interview write-up's account of Ellis's view, that the
metric is "a key cog in a sustainable growth strategy" [[4]](#ref-4), and the related, faster-rotating One
Metric That Matters, which Gilad attributes to Croll and Yoskovitz [[27]](#ref-27)[[29]](#ref-29), both place
it there. **No source read in this bundle's research ties the North
Star Metric by name to Scrum, SAFe, Shape Up, Amazon's working-backwards process, or design thinking.** That
is this research's own absence, not a claim that those schools reject it; nothing here should be read as
evidence either way.

Inside the growth-analytics vendor space itself, the lineage forks. Amplitude's single-metric-plus-inputs
design treats one North Star as sufficient on its own. Mixpanel, a direct competitor, argues the single-metric
framing is "mostly rhetorical" and promotes a fuller "metric tree" instead [[24]](#ref-24), elsewhere arguing
a North Star alone "often leaves a gap in operational execution" [[39]](#ref-39). A third Mixpanel piece
distinguishes two kinds of tree one level down: an "algebraic KPI tree," built on "fixed mathematical
relationships," against a "North Star map," which "deals in hypotheses rather than certainties"
[[26]](#ref-26). Read this as a vendor-versus-vendor disagreement about how much structure the Framework
needs beyond what Amplitude itself ships, not as two schools of product management disagreeing.

**The Framework extends past product decisions into operational ones.** A community reference wiki that
points back to Amplitude's own playbook and canvas as its source also extends the Framework to "decisions
related to the product as well as to operational aspects of the organization aligned to the product, e.g.
Support, Customer Success, Product Marketing." [[7]](#ref-7)

## 6. Debates and contested boundaries

**Where it sits in the chain.** One practitioner states the sequence explicitly: "first defining your North
Star Metric, then articulating a Strategy and finally establishing OKRs ensures each gets the attention it
deserves" [[44]](#ref-44), and that "North Star Metrics shouldn't be set backwards from a KPI dashboard but
develop forwards from your Product Vision" [[44]](#ref-44). A second practitioner states the opposite order:
vision, then strategy, then annual and quarterly goals are already built out before the North Star Metric is
introduced: "Defining a North Star metric is a great step" toward aligning what already exists, and it is "most useful after product/market
fit...but before your company is truly scaling" [[45]](#ref-45). One vendor places it above OKRs without
saying where vision or strategy fit: "your North Star metric sits at the top...Each key result is a
measurable contribution to moving the North Star." [[46]](#ref-46) One newsletter collapses the distinction
entirely: "Your North Star Metric is your strategy, and your strategy is your North Star Metric."
[[42]](#ref-42) Five further sources describe the metric as measuring the *current* strategy rather than
preceding it: "a key measure of your current product strategy" [[21]](#ref-21); "better reflects our current
product strategy" [[23]](#ref-23); "It represents the core of the product strategy" [[47]](#ref-47); "The
north star should reflect the current strategic question" [[11]](#ref-11); "Only change the NSM when strategy
or product fundamentally shifts" [[10]](#ref-10). This library places the North Star third, between the
strategy and the roadmap. That placement is inferred from the measures-the-current-strategy camp, not stated
by any one source as a sequence, and the family contract names it a POSITION rather than a finding
([`strategy-docs.md`](../../docs/internal/contracts/strategy-docs.md)).

**One North Star or several.** Amplitude's own rule is one per product leader [[1]](#ref-1)[[21]](#ref-21).
A reference article and a vendor both carry a single, named exception: "Each product line or distinct
customer journey can have one NSM" [[10]](#ref-10); "The exception is a company with separate product lines,
which may need one per line." [[48]](#ref-48) A direct competitor disagrees with the premise itself: "The
term North Star metric...is mostly rhetorical. Companies with complex business models can have multiple
North Stars." [[24]](#ref-24) A comment-thread practitioner, a lower-authority source named here for
completeness rather than as a settled answer, argues the same for a two-sided business: "it's possible, and
often valuable, for a company to have more than one north star...One could be payor centric and the other
patient centric." [[40]](#ref-40) A third practitioner states, in passing, that one North Star "probably
isn't" right for a platform or B2B product split between buyers and users [[41]](#ref-41). This bundle follows
the one-per-product rule with the product-line exception, and asks the template to name the product.

**Whether guardrails belong beside the North Star.** Covered in Anatomy, above; restated here because it is
a live disagreement, not a settled convention. Three sources pair a standing guardrail with the North Star
[[49]](#ref-49)[[51]](#ref-51)[[10]](#ref-10). Amplitude's own two documents never do [[1]](#ref-1)[[2]](#ref-2).
Two vendors scope the same word to a single experiment instead [[25]](#ref-25)[[11]](#ref-11). The full
variant's section rests on the first three, explicitly.

**How input metrics are organized.** A heuristic, breadth, depth, frequency and efficiency [[21]](#ref-21),
against a hierarchy, the metric tree [[24]](#ref-24). Neither source is reconciled with the other in this
research, and the template prescribes neither.

**How often it changes.** Four different answers, and none of them is the field's consensus. By trigger:
"What will be your signal to revisit this metric?" [[1]](#ref-1) By stage: "Early-stage startups...might
modify their North Star Metric every six to 12 months. However, more established organizations...every one
to three years is more typical." [[3]](#ref-3) By flat rule of thumb: "treat it as stable for at least a year
unless the underlying strategic objectives genuinely shift" [[37]](#ref-37), on the stated reasoning that
"Changing the North Star metric frequently undermines the entire point of having one." [[37]](#ref-37) On a
fixed calendar: "Quarterly: reassess definitions, targets, and input set." [[10]](#ref-10) Two further
sources, neither affiliated with Amplitude, corroborate periodic review as standard practice without naming a
number: one retells Netflix's own repeated changes as evidence that "you should review your key metric
regularly" [[16]](#ref-16); the other advises simply, "as your product changes, check if the metric still
makes sense" [[17]](#ref-17). The template asks for the trigger, because no source read agrees on a cadence.

**Revenue as the North Star.** Uncontested in direction, across every source that addresses it. "Revenue is
a lagging indicator" [[22]](#ref-22); it should not itself be "a lagging financial result (revenue, MRR)"
[[50]](#ref-50); it "should correlate with revenue growth but should not be revenue itself" [[52]](#ref-52);
"The fix is pairing your north star with guardrail metrics like retention and gross margin" rather than
revenue itself [[49]](#ref-49). One practitioner keeps a top business KPI beside the North Star rather than
folding revenue into it [[27]](#ref-27).

**"Not a ratio" is one newsletter's gloss, not Ellis's own words.** A newsletter summarizing, not
transcribing, an interview with Sean Ellis adds that the metric "should be actionable, not a ratio, and
capable of scaling up over time" [[52]](#ref-52). No other source read repeats this, and nothing in this
bundle rests on it alone.

**A digest misattributes a "balancing metric" to Gilad.** Itamar Gilad's own article names three elements:
the North Star Metric for value delivered, a top business KPI for value captured, and the One Metric That
Matters for tactical focus [[27]](#ref-27). A curated digest paraphrasing that article instead reports "one
balancing health metric that catches the damage" [[28]](#ref-28), a phrase that does not appear in Gilad's own
piece. This bundle attributes the three-metric framing to Gilad and the "balancing metric" phrasing to the
digest's own inaccurate gloss.

**Gaming, named independently under different words.** Umbrex asks, "How do we keep the NSM from being
gamed?" [[10]](#ref-10); Spotify states the design goal, "the best north star metrics measure outcomes that
are hard to fake" [[11]](#ref-11); a practitioner's essay titled *South Star Metrics*, about a gamed outcome,
states Goodhart's law outright, "when a measure becomes a target it ceases to be a good measure," with a named
example of a team that "decided to just stop asking users" a question rather than fix what the question
exposed [[34]](#ref-34); another practitioner reports, "give someone a metric and apply pressure to them to
hit that metric and you get some screwy results," and separately warns that departments acquiring their own
"isolated NSMs" compounds the risk as a company grows [[32]](#ref-32).

**North Star Metric versus One Metric That Matters.** The two are distinct. The OMTM "is a number that
you only use within your growth team," and a company "can therefore also have multiple OMTMs...but always a
maximum of one North Star Metric" [[29]](#ref-29); it rotates "for about 2 to 4 months" while "your North Star
Metric never changes unless you would completely change your business model" [[29]](#ref-29). Gilad frames
the relationship directionally: the OMTM "brings focus to your tactical execution, while the NSM and top KPI
set the strategic goals." [[27]](#ref-27) Ellis himself draws the same line in his own words: the North Star
is "a persistent overall success metric," distinct from "the one metric that matters" right now [[4]](#ref-4).

## 7. Anti-patterns and failure modes

- **A metric that can only rise.** "Total registered users, cumulative downloads, and pageviews only go up.
  A metric that can never fall cannot warn you when something is wrong." [[48]](#ref-48) Test it with the
  doubling question: "If this number doubled next month, would the business clearly be healthier? If not,
  it's a vanity metric." [[49]](#ref-49)
- **A metric the team can move directly.** "If you can move your North Star directly, it's probably not a
  good North Star." [[1]](#ref-1)[[22]](#ref-22)
- **Revenue, or any lagging measure, standing in for the metric.** [[22]](#ref-22)[[48]](#ref-48)[[49]](#ref-49)[[50]](#ref-50)[[52]](#ref-52)
- **Treating it as the sole input to every decision.** A Facebook product manager describes the result:
  "short sighted near term myopic thinking versus thinking about long term value," because "it's unlikely
  that every single small thing that you do is going to move a Northstar metric." [[33]](#ref-33)
- **Gaming it once it becomes a target.** See Debates, above [[34]](#ref-34)[[32]](#ref-32)[[10]](#ref-10)[[11]](#ref-11).
- **Letting departments run their own, uncoordinated North Stars.** [[32]](#ref-32)[[48]](#ref-48)
- **Over-fixating on one number past the point it is still useful.** "it can also lead to tunnel vision if
  not carefully managed" [[38]](#ref-38), and the same metric "may not be the most relevant metric" in every
  market a product serves [[38]](#ref-38).
- **Silently rewriting the definition instead of recording the change.** [[51]](#ref-51)[[24]](#ref-24)
- **Mistaking it for a goal-setting method.** Amplitude's own playbook names this directly as what the
  Framework is not [[1]](#ref-1).
- **Writing it in a leadership silo, vaguely, around outputs instead of outcomes, and never revisiting it as
  the product grows.** Five named mistakes from one consultancy, reported together because they recur as a
  set: being too vague or generic, focusing on outputs rather than outcomes, ignoring the user's emotional
  journey, creating it in a silo without buy-in, and not evolving it as the product grows [[36]](#ref-36).
- **A composite score standing in for a single metric.** "Composite scores with five weighted inputs fail
  this test even when they are technically better." [[48]](#ref-48)

## 8. Relationships to other artifacts

| This document | Neighbour | How to tell them apart |
|---|---|---|
| north star metric | [product vision](../product-vision/) | Two things share the phrase "north star." As a metaphor, "north star" describes what a vision does; as an artifact, the North Star Metric is a distinct, quantitative thing. [`product-vision_companion.md`](../product-vision/product-vision_companion.md) already keeps them apart, calling the metric "the quantified sibling of the Product Vision", a phrase it cites to Tim Herbig |
| north star metric | product strategy | Contested and named a POSITION, not a finding: this library places the North Star after the strategy and before the roadmap, measuring whether the current strategy is moving the product toward the vision. One source read states the opposite order [[44]](#ref-44); five describe the metric as measuring the *current* strategy, which is the camp this library follows [[21]](#ref-21)[[23]](#ref-23)[[47]](#ref-47)[[11]](#ref-11)[[10]](#ref-10) |
| north star metric | product roadmap | The North Star names the value the roadmap's work is meant to move. It carries no dates and no features; the moment either appears, it is the roadmap, not this document |
| north star metric | OKRs | OKRs sit beneath the North Star, not beside it: "Each key result is a measurable contribution to moving the North Star." [[46]](#ref-46) One practitioner separates them by time horizon: OKRs "typically have a quarterly (sometimes even annual) horizon" [[44]](#ref-44), while the North Star is meant to persist |
| north star metric | `kpi-dashboard` | This document states the metric and the case for it. `kpi-dashboard` carries its formula, data source, exclusions, target and refresh schedule; this bundle does not duplicate that section, by the maintainer's own ruling |
| north star metric | One Metric That Matters | Not a family member, and easy to confuse with the North Star because both are growth-practice, single-number devices. The OMTM is a faster-rotating, team-level number that feeds the North Star; the North Star itself "never changes unless you would completely change your business model." [[29]](#ref-29) See Debates, above |

**This bundle's admission rests on one publisher, and that publisher reserves all rights.** Both of
Amplitude's documents carry "©2024 Amplitude, Inc. All rights reserved." [[1]](#ref-1)[[2]](#ref-2). Every
field name, section name and layout choice in this bundle's template is this library's own, not a
reproduction of Amplitude's worksheet, checklist wording, sidebar heuristic or worked example. A negative
finding from the admission sweep is worth recording here rather than only in the research log: Reforge's own
North Star artifacts page, read directly, lists two member-submitted examples under that heading, and neither
is a North Star metric document [[54]](#ref-54). No company's own North Star document, and no nonprofit or
public-sector one, was found anywhere in this research.

## 9. Adaptations

**Multi-product companies.** Amplitude's default is one North Star per product where a team contributes to a
single profit and loss statement and serves a single customer base [[1]](#ref-1)[[21]](#ref-21). A
reference article and a vendor name the exception, genuinely separate product lines
[[10]](#ref-10)[[48]](#ref-48). A lower-authority, comment-thread source argues for a two-sided split in a
healthcare business, payor-facing against patient-facing, while still preferring to integrate the two into
one higher-order metric eventually [[40]](#ref-40); report this as one practitioner's view, not a settled
pattern. A separate practitioner raises the same concern for platform and B2B products split between buyers
and users, without offering a full alternative structure [[41]](#ref-41).

**Company stage.** Early-stage companies "might modify their North Star Metric every six to 12 months,"
while more established ones typically go "every one to three years" [[3]](#ref-3); see Debates, above, for why
the template still asks for a trigger rather than a number.

**Pre-product-market-fit and zero-to-one products.** One practitioner argues against exposing a very early
product to a large audience before checking quality at small scale, because at that stage, in that account,
data cannot reliably tell a team what is going to happen [[33]](#ref-33). Treat a
confident, scaled North Star as premature until that validation has happened.

**Beyond product, into operational functions.** A community reference wiki extends the Framework to
"Support, Customer Success, Product Marketing" alongside product decisions, while pointing back to Amplitude's
own playbook and canvas as its source [[7]](#ref-7).

**Growth teams running an OMTM underneath.** A growth team may rotate a faster, team-level One Metric That
Matters every two to four months beneath a North Star that stays fixed [[29]](#ref-29), with the OMTM framed
as supporting tactical focus while the North Star sets the strategic goal [[27]](#ref-27).

## 10. Worked example

[`north-star-metrics_example.md`](north-star-metrics_example.md) continues this library's single Acme
Analytics thread, dated between the product strategy and the product roadmap examples it sits between. It
shows a single-product company naming a count-based North Star that sits above an input metric the strategy
and the roadmap already track by a different name, and states the trigger that would prompt a revisit rather
than a calendar date. It carries no formula, target, threshold or dashboard layout; those stay with the
worked `kpi-dashboard` example.

## References

<a id="ref-1"></a>[1] Amplitude, Inc. (co-authored by John Cutler) - [The North Star Playbook](https://info.amplitude.com/rs/138-CDN-550/images/Amplitude-The-North-Star-Playbook.pdf). 2024. [vendor]

<a id="ref-2"></a>[2] Amplitude, Inc. - [How-to Guide: Running Your North Star Workshop](https://info.amplitude.com/rs/138-CDN-550/images/North-Star_how-to-Guide_2024.pdf). 2024. [vendor]

<a id="ref-3"></a>[3] Amplitude, Inc. - [Find your North Star (North Star Hub)](https://amplitude.com/north-star-hub). [vendor]

<a id="ref-4"></a>[4] Intercom (interviewer Adam Risman), featuring Sean Ellis - [Sean Ellis on charting a path toward sustainable growth](https://www.intercom.com/blog/podcasts/sean-ellis-growth/). Inside Intercom podcast, 2018-06-07. [primary]

<a id="ref-7"></a>[7] Open Practice Library - [North Star Framework](https://openpracticelibrary.com/practice/north-star-framework). [reference]

<a id="ref-10"></a>[10] Umbrex - [North Star Metric Framework (Product-Led Growth)](https://umbrex.com/resources/frameworks/marketing-frameworks/north-star-metric-framework-product-led-growth/). [reference]

<a id="ref-11"></a>[11] Confidence by Spotify - [What is a North Star Metric?](https://confidence.spotify.com/glossary/north-star-metric). [vendor]

<a id="ref-16"></a>[16] Grow & Retain (Substack) - [Review of your key metric](https://growandretain.substack.com/p/north-star-metrics-). [practitioner]

<a id="ref-17"></a>[17] UserJot - [Defining Your North Star Metric: A Step-by-Step Approach](https://userjot.com/blog/how-to-define-north-star-metric). [vendor]

<a id="ref-21"></a>[21] Julia Sholtz, Amplitude - [Every Product Needs a North Star Metric: Here's How to Find Yours](https://amplitude.com/blog/product-north-star-metric). [vendor]

<a id="ref-22"></a>[22] Julia Sholtz, Amplitude - [What Makes a Good vs Bad North Star Metric](https://amplitude.com/blog/good-bad-north-star-metric). [vendor]

<a id="ref-23"></a>[23] Justin Bauer (former CPO), Amplitude - [We're Evolving Our Product's North Star Metric. Here's Why](https://amplitude.com/blog/evolving-the-product-north-star-metric). [vendor]

<a id="ref-24"></a>[24] Mixpanel Team - [What is a North Star metric?](https://mixpanel.com/blog/north-star-metric/). [vendor]

<a id="ref-25"></a>[25] Mixpanel Team - [Guardrail metrics: The complete guide to balanced product growth](https://mixpanel.com/blog/guardrail-metrics/). [vendor]

<a id="ref-26"></a>[26] Mixpanel Team (quoting Dan Schmidt) - [North Star maps vs. algebraic KPI trees: How to know what to choose](https://mixpanel.com/blog/north-star-framework-vs-kpi-tree/). [vendor]

<a id="ref-27"></a>[27] Itamar Gilad - [The Three True-North Metrics that Your Product and Business Need](https://itamargilad.com/the-three-true-north-metrics-that-your-product-and-business-need/). [practitioner]

<a id="ref-28"></a>[28] Ray / Benjamin Scott, ZURB Radar - [One Number Is a Trap: Build a Metric Tree Your Whole Team Can Aim At](https://radar.zurb.com/article/one-number-is-a-trap-build-a-metric-tree-your-whole-team-can-aim-at). 2026-07-08. [practitioner]

<a id="ref-29"></a>[29] Ward van Gasteren, growwithward.com - [OMTM: What is the One Metric That Matters?](https://growwithward.com/one-metric-that-matter). [practitioner]

<a id="ref-32"></a>[32] Kerry Jones - [How North Star Metrics Can Lead You South](https://hackernoon.com/how-north-star-metrics-can-lead-you-south-1488c09891de). [practitioner]

<a id="ref-33"></a>[33] Maahir Shah, interviewed on Mind the Product's The Product Experience - [When not to use a North Star](https://mindtheproduct.com/north-star-maahir-shah-the-product-experience). 2022-03-02. [practitioner]

<a id="ref-34"></a>[34] Ibrahim Bashir - [South Star Metrics](https://runthebusiness.substack.com/p/south-star-metrics). 2020-06-30. [practitioner]

<a id="ref-36"></a>[36] Britt Mills, Bridgenext - [Five Common Mistakes When Creating a North Star for Digital Experiences](https://www.bridgenext.com/blog/how-to-avoid-common-mistakes-when-creating-a-north-star/). 2025-09-10. [vendor]

<a id="ref-37"></a>[37] ThinkInsights - [Data-Driven Strategy and KPI Design Playbook](https://thinkinsights.net/playbooks/data-driven-strategy-and-kpi-design-playbook-strategy-pyramid-metrics-framework). [vendor]

<a id="ref-38"></a>[38] Nick Chasinov, Teknicks - [Airbnb's North Star Metric: Explained](https://teknicks.com/blog/airbnb-north-star-metric). 2024-05-23. [vendor]

<a id="ref-39"></a>[39] Brandon Weaver, Mixpanel - [Go beyond the North Star: How to operationalize your growth strategy with metric trees](https://mixpanel.com/blog/beyond-north-star-metric-trees/). 2025-07-23. [vendor]

<a id="ref-40"></a>[40] Gabe Strauss, replying to Jake Goldman - [Flywheels: Theory to Action (comment thread)](https://behavioralhealthpm.substack.com/p/flywheels-theory-to-action/comments). [practitioner]

<a id="ref-41"></a>[41] Jason Knight, One Knight in Product - [Users, buyers, not picking favourites & noodling on North Star Metrics](https://oneknightinproduct.substack.com/p/users-buyers-not-picking-favourites-noodling-on-north-star-metrics-1074472). 2022-03-21. [practitioner]

<a id="ref-42"></a>[42] Lenny Rachitsky, Lenny's Newsletter - [Choosing Your North Star Metric](https://www.lennysnewsletter.com/p/choosing-your-north-star-metric). [practitioner]

<a id="ref-44"></a>[44] Tim Herbig - [How to connect North Star Metrics, Product Strategy, and OKRs](https://herbig.co/product-strategy-metrics-sandwich/). [practitioner]

<a id="ref-45"></a>[45] Adam Farren, 10x Operator - [What's a good North Star metric? It helps to have one metric to rule them all](https://10xoperator.substack.com/p/guide-to-the-north-star-metric). [practitioner]

<a id="ref-46"></a>[46] Tability - [What is a North Star Metric? (and how to actually use one)](https://www.tability.io/odt/articles/north-star-metric). [vendor]

<a id="ref-47"></a>[47] Swiss Post (Post CH AG), Digital Commerce Blog - [North star guides product development](https://digital-commerce.post.ch/en/pages/blog/2020/north-star-guides-product-development). 2020. [vendor]

<a id="ref-48"></a>[48] Max Musing, Basedash - [How to choose a north star metric: a practical framework](https://www.basedash.com/blog/how-to-choose-a-north-star-metric-a-practical-framework). [vendor]

<a id="ref-49"></a>[49] Sameer and Ankit, Cut the SaaS - [North Star Metric: How to Pick One That Actually Works](https://cut-the-saas.com/guides/north-star-metric). [vendor]

<a id="ref-50"></a>[50] Koji - [North Star Metric Framework: How to Find, Validate, and Move Your Product's One Metric That Matters](https://www.koji.so/docs/north-star-metric-framework). 2026. [vendor]

<a id="ref-51"></a>[51] Ballpark - [North Star Metric (glossary entry)](https://ballparkhq.com/research-glossary/north-star-metric). [vendor]

<a id="ref-52"></a>[52] Lenny Rachitsky, Lenny's Newsletter, summarizing an interview with Sean Ellis - [The original growth hacker reveals his secrets](https://www.lennysnewsletter.com/p/the-original-growth-hacker-sean-ellis). 2024-09-05. [practitioner]

<a id="ref-54"></a>[54] Reforge - [North Star Metric (artifacts page)](https://www.reforge.com/artifacts/c/team-operations/north-star-metric). [vendor]
