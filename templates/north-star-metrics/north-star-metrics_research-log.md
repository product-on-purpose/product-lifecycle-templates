# north-star-metrics: research log

Research conducted 2026-10-12, before the spec merged, building on the admission sweep of 2026-10-05. Its verdicts
are summarised in [`tier2-specs.md`](../../docs/internal/tier2-specs.md) and recorded in
[ADR 0070 (north-star-metrics joins strategy-docs as a fifth member)](../../docs/internal/decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md).
Six research dimensions ran: origins and canon, the structure of a written North Star document, input metrics,
debates and cadence, relationships with this family's other documents, and the standing gap question. **54 sources are
recorded below: 47 fetched-and-verified, 6 url-confirmed-not-read and 1 not-retrieved.** Only `fetched-and-verified`
sources are quoted anywhere in this bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a retrieval tool
returns. The six dimensions filed 353 quotations, and 60 of them failed the first check as filed. Ten of the 60 came
from Umbrex [10], whose page refused a plain fetch; it was read in a browser on 2026-10-12, and all ten pass against
that read. Seventeen more had joined a numbered list or several passages into one string. Their 46 verbatim parts pass,
and each is kept as a separate quotation. The other 33 are dropped, and no claim in this bundle rests on them. The
build's main loop added eight quotations after the same raw check: Amplitude's copyright line in [1] and [2], the
revisit rule in [3], three lines from the write-up of Sean Ellis's interview in [4], a sentence from [7], and the line in
[22] that attributes a quotation to John Cutler. Five of them were added before drafting, and three after drafting,
when the companion quoted them from pages the agents had read but not listed. After merging the sources that two
dimensions both owned, and removing the quotations filed on the four agent-skill files [12] to [15], the log carries
345 quotations on 42 sources, two of them from the browser read of Reforge [54]. Dashes inside quotations are written as hyphens, as the house rule requires.

---

## What the checks caught, and what was not read

**The full variant is earned, and the spec's stop condition does not trigger.** The spec added one condition for this
bundle: if the research cannot support a full variant, the build stops and reports rather than padding one. Each of
the four full-only sections rests on at least two independent publishers:

1. **Candidates Considered**, in [1], [22], [48] and [49]. [1] describes a delivery app that "had considered potential
   North Star Metrics", names three, and says "These metrics masked the real drivers of user retention and customer
   lifetime value (CLTV)". [22] says "Your team selected this metric
   over something like" two others, and gives the reason. [48] says "Total registered users, cumulative downloads, and
   pageviews only go up", and [49] says "Total signups, page views, and registered users all fail that test." [1] and
   [22] are one publisher, Amplitude.
2. **Guardrails**, in [49], [51] and [10]. [49] says "The fix is pairing your north star with guardrail metrics like
   retention and gross margin." [51] says "Pair the shared measure with checks for harm or declining quality." [10]
   lists guardrails as quality and economics limits, to prevent "hitting the target but missing the point." [25] uses
   the word for something narrower, a check run during one experiment.
3. **What It Does Not Tell Us**, in [1], [10] and [11]. [1] asks "What doesn't this metric tell you?" [10] asks "How
   do we keep the NSM from being gamed?" [11] says "North star metrics tend to be high-level and slow-moving."
4. **Definition History**, in [51], [24], [10] and [23]. [51] says "Preserve the old definition and explain the break
   in the series rather than silently rewriting history." [24] says "Every metric should have clear documentation -
   how it's defined, calculated, and where the data comes from." [10] says "Keep a versioned definition history to
   preserve comparability." [23] is Amplitude's own account of replacing its North Star, with its reasons.

**Guardrails are not part of Amplitude's framework, and the companion must say so.** This build searched both Amplitude
documents' cached text for the word. [1] never uses it. [2] uses it once, in an aside about brainstorming what a
terrible North Star would be: "These anti-examples free participants' thinking and can set helpful guardrails when
you're defining your metric and inputs later on." That aside is about the act of choosing, not a measure tracked beside
the metric. Neither document uses "counter-metric" or "gaming". The full variant's Guardrails section therefore rests
on [49], [51] and [10], not on the admitting publisher.

**Where the formula lives is this library's POSITION.** The input-metrics dimension found no source among those read
that asks whether a North Star document should carry the precise calculation or leave it to an analytics specification.
The sources state a definition, with its behaviour and its window, wherever they name a North Star: [49] says "Pick a
metric that counts that action across a sensible time window, like weekly", and [51] says "Prefer a definition people
can explain, inspect and reproduce." This bundle keeps that statement. The calculation, data source, exclusions,
targets and refresh go to `kpi-dashboard`, as the maintainer ruled on 2026-10-12.

**The methodology is growth and the North Star Framework, not OKR.** [1] lists "A goal-setting framework, like
objectives and key results (OKRs)" among the things the framework is not. [4], a write-up of an interview with Sean
Ellis, calls the metric "Sean's way of quantifying the point where customers experience the value of your product",
and describes it as "a key cog in a sustainable growth strategy".

**Who coined the term is contested, not settled.** One source read says Sean Ellis did: [7], a reference wiki, writes
"According to Sean Ellis, who coined this term, this is the single metric that best captures the core value that your
product delivers to customers." No primary source read confirms it. This build searched both Amplitude documents'
cached text: neither mentions Sean Ellis or growth hacking, and both name John Cutler as a co-author of the playbook.
In [4], Ellis says of growth hacking "I came up with the phrase", and makes no such claim about the North Star
Metric; the write-up's own narration calls the metric "Sean's way of quantifying the point where customers experience
the value of your product". Further pages making the claim, among them [5], were not read. The bundle says that
Amplitude formalized the framework in [1] and [2], that [4] ties the metric to Ellis's growth practice, and that [7]
credits him with the term while no primary source does.

**The chain position is contested, and the library's third place is an inference.** [44] puts the North Star first:
"...first defining your North Star Metric, then articulating a Strategy and finally establishing OKRs ensures each gets
the attention it deserves." [45] puts it last, as an alignment device across the chain: "So how do you bring all of
that - vision, strategy, tactics - into alignment? Defining a North Star metric is a great step." Five sources describe
the North Star as measuring the current strategy: [21] "A metric that serves as a key measure of your current product
strategy", [23] "better reflects our current product strategy", [47] "It represents the core of the product strategy.",
[11] "The north star should reflect the current strategic question", and [10] "Only change the NSM when strategy or
product fundamentally shifts". No source read places the North Star third, between the strategy and the roadmap, as a
sequence. ADR 0070 places it there, labelled the library's POSITION.

**Not read.**

- [42], Lenny Rachitsky's post: only the introduction and the comments rendered. Its six categories of North Star sit
  on a linked page this build did not read, and the bundle must not list them.
- [43], Brian Balfour's talk: not retrieved. Search summaries attributed positions to it, and none is used.
- [5] (VentureBeat), [6] (a webinar listing for John Cutler), [18] (a concept page on guardrail metrics), [19] (a
  development bank's Notion page), [20] (Mural's workshop template) and [53] (UXCam): each URL resolved, and no body
  was read. No claim rests on them.
- No company's own internal North Star document was found. Every named company example in these sources, Airbnb,
  Facebook, Netflix and Spotify among them, is relayed by a third party, not published by the company itself.
- No nonprofit or public-sector North Star document was found, despite a targeted search.

**Six source records are not used, and two of them are not in this log.** The four agent-skill files on GitHub, [12]
to [15], are listed so that the consultation is on record. No named publisher stands behind them, so the spec rules them
out as structural sources, and they carry no quotation. Two further records are left out of this log entirely. One was
a not-retrieved entry for [42]'s post, filed under the newsletter's home page rather than the post, which would have
listed one source twice. The other combined five websites' write-ups on Sean Ellis under one number, and none of the
five was read.

---

## The admission record

The type cleared [ADR 0030](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md)'s admission test
in the sweep of 2026-10-05, on one publisher, Amplitude, in two of its own documents. One named source suffices under
[ADR 0048](../../docs/internal/decisions/0048-one-named-source-clears-the-admission-test.md). [1] says "When you define
the metric, you complete this template: Our North Star Metric is called X, which we define as Y." [2]'s worksheet asks
"What will the impacts to the business be?", and its checklist asks "Does it express customer value?" and "Is it a
leading indicator of success?"

**Both documents reserve all rights.** Each carries "©2024 Amplitude, Inc. All rights reserved." So every field name in
this bundle is the library's own wording. The template reproduces no Amplitude worksheet, field label, sidebar
heuristic or worked example.

**Reforge [54] is a negative finding.** Its artifacts page, read in a browser on 2026-10-12, says "Explore 2 examples
of North Star Metrics so you never have to start from scratch." The two are member submissions: a framework for
cascading goal targets through a leadership team, and a brand concept document. Neither is a North Star metric
document, and the page shows no field names. Admission stays on one publisher.

The other sources explain the practice without publishing a document of this type. Among them are Mixpanel [24],
Herbig [44] and the Ellis interview [4].

---

## Claims flagged contested or time-bound

1. **Where the North Star sits in the chain.** Sequence: [44] first, before the strategy; [45] last, as an alignment
   device. Dependency: [21], [23], [47], [11] and [10] describe the North Star as measuring the current strategy. [44]
   also says "Your North Star Metrics shouldn't be set backwards from a KPI dashboard but develop forwards from your
   Product Vision." Every source that relates the North Star to OKRs puts it above them: [44] says "OKRs are point-in-time
   goals that implement that Strategy", and [10] says "OKRs/KRs roll up to NSM movement". The bundle places it third, as
   the library's POSITION, and the companion names both camps.
2. **One North Star or several.** One: [24] says "Companies typically have only one North Star metric", and [48] says
   "The purpose of a north star is focus, and multiple north stars defeat that." Several: [24] adds "However, a single
   north star can be limiting, especially if your company has multiple core products with separate goals". [40] proposes
   two for a healthcare business, "One could be payor centric and the other patient centric." [41] says of one North
   Star Metric, "it probably isn't" a good idea. A middle position is shared by [10], "Each product line or distinct
   customer journey can have one NSM", and by [48], "The exception is a company with separate product lines, which may
   need one per line." The bundle defines one North Star for one product, and asks which product where a company has
   several.
3. **Whether guardrails belong beside the North Star.** [49], [51] and [10] pair them with it. Amplitude's documents
   [1] and [2] do not use the word for a tracked measure, as recorded above. [25] scopes guardrails to experiments. The
   bundle carries Guardrails in the full variant only.
4. **How input metrics are categorized.** [21] offers breadth, depth, frequency and efficiency as "One heuristic we've
   found helpful when teams are determining inputs". [24] structures inputs as a hierarchy instead: "A metric tree is a
   logical hierarchy of your growth model that maps how input metrics (at varying levels of granularity) feed into focus
   metrics, which in turn impact your North Star." The companion reports both, and the template prescribes neither.
5. **How often the North Star changes.** By trigger: [1] asks "What will be your signal to revisit this metric?", and
   [3] says "You should revisit your North Star metric periodically, whenever there's a significant shift in your
   product, market, or business strategy." By stage: [3] says early-stage companies "might modify their North Star
   Metric every six to 12 months", while for established ones "every one to three years is more typical." By rule of
   thumb: [37] says "Rarely - treat it as stable for at least a year unless the underlying strategic objectives
   genuinely shift". On a calendar: [10] reviews definitions quarterly ("Quarterly: reassess definitions, targets, and
   input set."). The template asks for the trigger, not a date.
6. **Revenue as the North Star.** Not contested in direction. [22] says "Revenue is a lagging indicator", [50] rules
   out "a lagging financial result (revenue, MRR)", and [52] says the metric "should correlate with revenue growth but
   should not be revenue itself." [27] keeps a top business KPI beside the North Star rather than inside it.
7. **"Not a ratio" is a single source.** [52] says the metric "should be actionable, not a ratio, and capable of scaling
   up over time." It is the newsletter's own summary of an interview, not a quotation of Ellis, and no other source read
   repeats it. The bundle may report it as [52]'s, and nothing may rest on it alone.
8. **A secondary source misattributes a "balancing metric".** [28], a curated digest, says Itamar Gilad "suggests
   three true-north metrics instead: one for value to the customer, one top business KPI, and one balancing health
   metric that catches the damage." This build searched [27], Gilad's own article, and the word "balancing" does not
   appear. His third element is a short-term focus metric, which [27] calls "designed to be actionable." The bundle
   must not attribute a balancing metric to Gilad.
9. **Time-bound.** [1] and [2] are dated 2024 by their copyright lines. [22] says Amplitude has "changed our North Star
   Metric at least three times", and [23] is the account of one such change. [54] reads "Updated July 1, 2024". [37]'s
   one-year figure is that publisher's prescription, not a measured finding.

---

## Notes for the companion

### Honest framing

- **Admission rests on one publisher, and that publisher reserves all rights.** The companion states both plainly.
  Field names, section names and the layout are this library's own.
- **The duplication with `kpi-dashboard` is real, and the companion says so.** `kpi-dashboard`'s Metric Definitions
  section already carries a headline metric's formula, scope, exclusions and known limitations. This bundle carries one
  statement line and the case for choosing the metric and its inputs, which no other bundle carries. The division is
  this library's POSITION.
- **The metaphor and the artifact share a name.** `product-vision_companion.md:271-273` already separates "north star"
  as a description of what a vision does from the North Star Metric as an artifact. The companion cites that passage
  and keeps the two apart.
- **One document defines one North Star.** The bundle id is plural because it names the practice, as [44]'s title
  does. One filled document defines one North Star for one product, with its input metrics beneath it.
- **The chain position is a POSITION, not a finding.** Third place is inferred from the dependency evidence above.
  [44]'s opposite order is reported, not dismissed.
- **This is not a goal-setting document.** [1] lists a goal-setting framework among the things the North Star
  Framework is not. Targets stay out at every size, and the companion routes them to `okrs` and `kpi-dashboard`.

### The evidentiary spine, section by section

| Section | In lean | Sources |
|---|---|---|
| The North Star | yes | [1] "Our North Star Metric is called X, which we define as Y."; [49] "Pick a metric that counts that action across a sensible time window, like weekly."; [51] "Prefer a definition people can explain, inspect and reproduce."; [10] and [48] on naming the product where a company has several |
| Why This Metric | yes | [1] and [2] "Does it express customer value?", "Is it a leading indicator of success?" and "It's not a vanity metric?"; [22] "Validate that it predicts retention and revenue in your own data."; [50] "You cannot write this sentence by staring at a dashboard."; [48] "Write down the value your product delivers in one sentence."; [21] on leading against lagging indicators |
| Input Metrics | yes | [21] "Inputs are a set of three to five influential, complementary factors that you believe most directly affect your North Star Metric and that your team can directly influence through your product."; [48] "Each input is something a specific team can own and affect directly."; [10] "Teams own 1-3 input metrics each"; [21]'s breadth-depth-frequency-efficiency heuristic and [24]'s metric tree, both reported and neither prescribed |
| What It Serves | yes | [21] "A metric that serves as a key measure of your current product strategy"; [44] for the other order; [2] "What will the impacts to the business be?"; [52] on correlating with revenue without being revenue |
| When We Revisit It | yes | [1] "What will be your signal to revisit this metric?"; [3] "whenever there's a significant shift in your product, market, or business strategy"; [10] "Only change the NSM when strategy or product fundamentally shifts"; [11] "Changing the north star is a significant organizational decision." |
| Candidates Considered | full | [1]'s delivery-app passage; [22] "Your team selected this metric over something like"; [48]; [49] |
| Guardrails | full | [49] "The fix is pairing your north star with guardrail metrics like retention and gross margin."; [51] "Pair the shared measure with checks for harm or declining quality."; [10] "hitting the target but missing the point" |
| What It Does Not Tell Us | full | [1] "What doesn't this metric tell you?"; [10] "How do we keep the NSM from being gamed?"; [11] "North star metrics tend to be high-level and slow-moving." |
| Definition History | full | [51] "Preserve the old definition and explain the break in the series"; [24] "Every metric should have clear documentation"; [10] "Keep a versioned definition history to preserve comparability."; [23] Amplitude's account of its own change |

**Two findings go to the guide, not the template**, under decision procedure 12. The one-sentence test is [48]'s:
"Everyone from sales to engineering should be able to say what it means in one sentence." The planning filter is
[49]'s: "Every project then earns a simple question: does this move the north star?" Both are rubric rows.

**What stays out at any size:** the operational formula, the data source and refresh schedule, targets and thresholds,
a dashboard layout, and a tree of metrics below the input metrics. The first four are `kpi-dashboard`'s. The catalog
lists a metric tree as its own type, which places the North Star at its top node.

### The gap question's result, and what this build does with it

The gap dimension searched without reading the library, and found nine candidates. Each is routed under decision
procedure 12:

1. **The customer value, in the customer's words.** [50], [51], [48] and [49]. Routed to Why This Metric's ASK.
2. **A behaviour and a time window, not only a name.** [22], [23], [48] and [49]. Routed into The North Star section.
3. **Validation against the product's own data.** [22], [21], [23], [48] and [50]. Routed to Why This Metric, which
   asks what shows the metric predicts retention or revenue, or says it has not been validated yet.
4. **Alternatives named and rejected.** [22], [21], [23], [48] and [49]. Adopted as the full variant's Candidates
   Considered.
5. **A named owner for each input.** [24] and [48]. Routed to Input Metrics, which names an owner per input.
6. **A one-sentence test.** [48]. Routed to the guide's rubric.
7. **A trigger for changing the metric, distinct from redefining it.** [48], [23], [22] and [51]. Routed to When We
   Revisit It.
8. **A change log that preserves the old definition.** [24] and [51]. Adopted as the full variant's Definition
   History.
9. **Guardrails.** [49] and [51], with [10]. Adopted as the full variant's Guardrails.

**Null results, recorded so the next author does not search again:** no company's own North Star document; no
nonprofit or public-sector North Star document; and no time-based measure proposed as a North Star in any of the
sources read. The input-metrics dimension searched analytics products specifically for the last of these.

### What the bundle must not say

- That Sean Ellis coined the North Star Metric, as a settled fact. [7] says he did, and neither Ellis in [4] nor
  Amplitude in [1] and [2] says so. Nor that Amplitude invented the idea; no source read establishes it.
- That guardrails are part of Amplitude's North Star Framework.
- Any Amplitude field label, worksheet layout, sidebar heuristic or worked example, presented as this template's own.
  The breadth-depth-frequency-efficiency heuristic may be reported as Amplitude's, never prescribed.
- [42]'s six categories, which were not read; or any position attributed to Balfour [43].
- That a fixed review cadence is the canon's. The sources disagree, as recorded above.
- That any named company's North Star is quoted from that company's own document.
- That a time-based measure cannot be a North Star. The research found none, which is an absence in these sources,
  not a rule.
- That Itamar Gilad proposes a "balancing metric".
- Any statistic about how many companies use a North Star Metric. No source read carries one.

### GOOD and WEAK illustrations use their own scenario

The worked example defines a North Star for Acme Analytics in early February 2026. GOOD and WEAK text in both templates
must use a different scenario, and must not use these nouns: Acme, Acme Analytics, Dana Okoro, Priya Nair, Elena Cho,
Time to Insight, second view, second dashboard view, 31 percent, 14 days, Saved Views, Recurring Analyst, dataset
picker, self-served, or the example's own North Star name. They must not reuse Amplitude's worked examples either:
the delivery app and its "Happy Deliveries", Netflix's DVD queue, or Amplitude's own weekly querying and learning users.

### The example

[`tier2-specs.md`](../../docs/internal/tier2-specs.md), section "The example: Acme's North Star", fixes most of it. The
facts below are what the example must carry, and its author reads only this paragraph and the sibling examples.

**Who and when.** A North Star metric for Acme Analytics, owned by Dana Okoro, VP Product, who owns the vision, the
strategy and the roadmap. Dated between 2026-01-29 and 2026-02-10; 2026-02-04 fits. That is after the product
strategy (2026-01-28) and before the product roadmap (2026-02-11).

**What it may cite as existing.** Only documents dated before it: the problem statement (2026-01-09), the vision
(2026-01-14), the project brief (2026-01-16), the business case (2026-01-20) and the product strategy (2026-01-28),
each by relative path, for example `../product-strategy/product-strategy_example.md`. It must not cite the roadmap,
the OKRs, the PRD, the KPI dashboard or the tracking plan as existing. Only the opening "> **Worked example.**"
blockquote, which addresses the library's reader, may point forward.

**Facts it must match exactly.** From the vision: the 2029 horizon; "anyone at a company running Acme can answer a
question about their own operations in the time it takes to ask it out loud"; and "Removing the analytics team as a
bottleneck". From the problem statement and the strategy: only 31 percent of new accounts build a second view within
14 days, a Q4 FY25 baseline. From the strategy: the leading indicator is the "share of new accounts that build a second
view within 14 days", and the lagging measures are self-serve net revenue retention and the FY26 "Time to Insight"
company goal. The strategy's 50 percent target stays out, because targets are `kpi-dashboard`'s and `okrs`'.

**The choice this build made: the second-view share is Input 1, and the North Star sits above it.** Three things
decide it. First, the OKRs example, dated 2026-07-27, makes the second-view share a Key Result, and [10] says "OKRs/KRs
roll up to NSM movement", so a Key Result belongs beneath the North Star, not as it. Second, [21] defines inputs as factors "that
your team can directly influence through your product", which an onboarding share is. Third, the share counts new
accounts only, so it cannot show whether established accounts keep getting value. [52]'s "not a ratio" agrees, and is
a single source, so the example must not rest on it.

**The North Star's shape.** A count, not a share, across all active accounts, of a behaviour that shows someone outside
an analytics role got an answer from Acme and acted on it without asking the analytics team, over a weekly window. It
comes from the vision's two sentences above, and it leads the two lagging measures. A name such as "weekly self-served
answers" fits; the example's author may choose its own. **It must not be a weekly count of users who perform one
action**, which is the shape of Amplitude's own North Star, nor any reworded Amplitude example.

**What it must say about the number every team already watches.** The strategy says "Every team sees the same number,
on the same dashboard, weekly", and that number is the second-view share. The example says, in its own voice, that the
second-view share stays on that dashboard as Input 1, and that the near-term planning ladders to Input 1 because it is
the strategy's own leading indicator. The North Star shows whether that activation turns into repeated value.
The roadmap, dated a week later, then names the second-view share as "the measure everything below ladders to", and
the example must not contradict it.

**The full variant's sections, in this scenario.** Candidates Considered names at least Time to Insight (rejected,
because the strategy labels it lagging), the second-view share (kept as Input 1, not the North Star) and self-serve
net revenue retention (rejected, because it is revenue). Guardrails may draw on the vision's warning that "if users
take our answers to Dev to check them, we have not removed a bottleneck". Definition History records this as the first
definition.

**What it must not contain.** No operational formula, data source, target or threshold; the North Star section points
to the KPI dashboard for those, without citing it as existing. No new figure unless it is labelled illustrative, and
no figure that differs from a sibling's. Why This Metric must either label its validation evidence illustrative or say
plainly that the validation has not been run yet, and how it will be.

---

## Sources

### ORIGINS AND CANON: WHO DEFINED THE NORTH STAR METRIC

**[1] Amplitude, Inc. (co-authored by John Cutler, Former Amplitude Product Evangelist; with Abbie Kouzmanoff and Ibrahim Bashir credited as contributing experts) - The North Star Playbook.** vendor. **fetched-and-verified.**
`https://info.amplitude.com/rs/138-CDN-550/images/Amplitude-The-North-Star-Playbook.pdf`
Supports: Full definition of the North Star Framework and North Star Metric; The three core qualities of a North Star Metric; The three purposes the framework serves (decision-making, alignment, focus); The leading-indicator / predicting-future-results framing; The North Star statement fill-in exercise template; The metric name-and-definition fill-in template; The explicit 'what the North Star is not' list, including its relationship to OKRs; John Cutler's quoted contributions to the framework's philosophy; Copyright and trademark statement; Confirms Sean Ellis is NOT cited anywhere in this document. Contested/time-bound: The playbook names no origin, inventor, or date for the North Star Metric concept, and never cites Sean Ellis, GrowthHackers, or growth hacking anywhere in its text or its six endnotes (which instead cite Andrew Chen, Dr. Jabe Bloom, a LinkedIn post, and Ben Horowitz's 'The Hard Thing About Hard Things'). The copyright year (2024) is time-bound and may be superseded by a later edition. The full 63-page playbook: the 7-item North Star checklist, the North Star statement exercise worksheet (North Star / Inputs / Opportunities / Interventions rows with 'Measurement Options' blanks and a descriptor column), the name-and-definition template ('Our North Star Metric is called X, which we define as Y'), the inputs fill-in template, belief-surfacing fill-in templates, the Crossing-the-Chasm-style vision-statement template, the 'One North Star Metric' section on multi-division companies, Chapter 4's trap #3 on insisting on multiple North Stars, Chapter 5 on when and why to change the North Star, and the vanity-metric test with a worked 'Happy Deliveries' example. Contested/time-bound: The playbook itself documents that Amplitude's own North Star Metric has changed more than once (from Weekly Learning Users to a collaboration-focused metric), which the library should treat as an illustration, not a claim that any one metric is permanent.
Quotable: "THE DEFINITION The North Star Framework is a product management model based on a single metric"
Quotable: "your North Star Metric"
Quotable: "that best captures the value customers derive from your product."
Quotable: "The North Star Metric is defined by three core qualities: 1 It represents the value users get from your product. 2 It's within product and marketing's sphere of influence. 3 It's a leading indicator of revenue."
Quotable: "Product and marketing teams may use very different inputs to move the North Star, but they reference the same North Star when deciding which inputs to prioritize. This serves three critical purposes: 1 Helps prioritize and accelerate informed but decentralized decision-making. 2 Helps teams align and communicate. 3 Enables teams to focus on impact and sustainable, product-led growth."
Quotable: "A good North Star Metric is a leading indicator of business success. Metrics like "Monthly Recurring Revenue" or "Average Revenue per User (ARPU)" aren't optimal North Star Metrics because they tell you what happened in the past rather than predicting future results."
Quotable: "Ideally, your North Star Metric predicts medium- to long-term sustainable growth."
Quotable: "Your software development process"
Quotable: "A goal-setting framework, like objectives and key results (OKRs)"
Quotable: "although the North Star can be a strong foundation upon which to base goals"
Quotable: "Management by objectives (MBOs)"
Quotable: "A one-time quick fix"
Quotable: "Our path to medium-to long- term sustainable (and defensible or differentiated) growth is a function of our ability to:"
Quotable: "...which is a function of our ability to:"
Quotable: "...we believe the key opportunities and leverage points to influence these inputs are:"
Quotable: "...and some representative options to make tangible progress include:"
Quotable: "When you define the metric, you complete this template: Our North Star Metric is called X, which we define as Y."
Quotable: ""If you can move your North Star directly, it's probably not a good North Star," explains John Cutler, former Amplitude Product Evangelist and co-author of the North Star Playbook. "The goal of the North Star is to be one level out of reach."
Quotable: "©2024 Amplitude, Inc. All rights reserved. Amplitude is a registered trademark of Amplitude, Inc."
Quotable: "©2024 Amplitude, Inc. All rights reserved."
Quotable: "Does it express customer value?"
Quotable: "Does it represent your vision and strategy?"
Quotable: "Is it a leading indicator of success?"
Quotable: "Is it understandable to non-technical partners?"
Quotable: "It's not a vanity metric?"
Quotable: "Our North Star Metric is called X, which we define as Y."
Quotable: "What doesn't this metric tell you? Are any of those questions or uncertainties more important to address?"
Quotable: "What will be your signal to revisit this metric? Assuming you revisit it periodically, what tests will you run to determine that it is still useful?"
Quotable: "Certainly, larger enterprises with multiple or diverse divisions, product management and development departments, and customer bases could have different North Star Metrics, each with their own inputs."
Quotable: "But if a team contributes to a single profit and loss (P&L) statement with a single product development department, and a single product or even a product portfolio that serves a single customer base, we recommend having a single North Star Metric and its inputs per product."
Quotable: "3 Insisting you need more than one North Star Metric"
Quotable: "Challenge the need for multiple North Star Metrics. Look for real boundaries in terms of users, their needs, and the strategy to meet those needs."
Quotable: "The teams who've seen the most success implementing"
Quotable: "A delivery app had considered potential North Star Metrics like "People Opening the App," "Scheduled Deliveries," or "Early Deliveries." But there was a problem: These metrics masked the real drivers of user retention and customer lifetime value (CLTV)... the team ultimately called "Happy Deliveries.""

**[2] Amplitude, Inc. - How-to Guide: Running Your North Star Workshop (2024).** vendor. **fetched-and-verified.**
`https://info.amplitude.com/rs/138-CDN-550/images/North-Star_how-to-Guide_2024.pdf`
Supports: Confirms the How-to Guide is a companion to, and assumes the reader has already read, The North Star Playbook; Repeats the same John Cutler / Abbie Kouzmanoff / Ibrahim Bashir / Ted Clark expert-contributor roster as the playbook; Copyright and trademark statement, identical wording to the playbook; Confirms Sean Ellis is NOT cited anywhere in this document; contains no 'OKR' mentions at all. Contested/time-bound: This guide does not restate the core NSM/framework definitions itself; it is a facilitation/workshop-logistics document that defers to the playbook for definitions. Dated 2024 in its filename and copyright line; may be superseded. The companion 28-page workshop guide. Carries the same North Star statement exercise worksheet as the playbook, plus a second, distinct worksheet: the 'North Star Framework worksheet' with fields Team name / Input metrics (Breadth, Depth, Frequency, Other, each with a sub-question) / North Star Metric ('What's your product's North Star?') / Mid/long-term impacts ('What will the impacts to the business be?'). Also carries the 8-part workshop agenda, the three-games classification, the converging questions, and the silent-brainstorm fill-in-the-blank template. Contested/time-bound: The 'helpful guardrails' sentence uses 'guardrail' to mean brainstormed anti-examples that bound the team's thinking during definition, not a tracked guardrail/counter-metric field in the finished document. This is a different sense of 'guardrail' from the one used by Umbrex, Spotify, and the borghei templates below, and the library should not conflate the two. Q1; Q2; Q3; Q4. Contested/time-bound: This is the exact PDF named in the research brief. It is a companion 'how-to' workshop guide, not the full North Star Playbook ebook it repeatedly points readers to (that longer ebook is gated behind an email form and was not fetched). On Q4: this source shows the playbook deliberately defers PRECISE formula wording to a later step ('the next step will be precisely defining...') during workshop facilitation, but it still frames that precise definition as part of finishing the North Star artifact itself, not as handoff to a separate analytics/tracking-plan document -- no source found makes that document-boundary distinction explicitly.
Quotable: "You're ready to run your North Star workshop"
Quotable: "woohoo! Before facilitating your workshop, we highly recommend reading our complete North Star Playbook."
Quotable: "John Cutler ... Former Product Evangelist, Amplitude, and co-author of The North Star Playbook"
Quotable: "©2024 Amplitude, Inc. All rights reserved. Amplitude is a registered trademark of Amplitude, Inc."
Quotable: "©2024 Amplitude, Inc. All rights reserved."
Quotable: "North Star Framework worksheet"
Quotable: "Breadth - How many users are engaging?"
Quotable: "Depth - What level of engagement are they reaching?"
Quotable: "Frequency - How often does each user engage?"
Quotable: "Other - Add in your own leading metrics"
Quotable: "What's your product's North Star?"
Quotable: "What will the impacts to the business be?"
Quotable: "Spend a few minutes brainstorming what a terrible North Star would be for your company. These anti-examples free participants' thinking and can set helpful guardrails when you're defining your metric and inputs later on."
Quotable: "“I would be more confident that our current product strategy is setting us up for sustainable long-term growth, if I observed an increase in [INSERT CUSTOMER CHARACTERISTIC BEHAVIOR OR CHARACTERISTIC] which we could measure by [INSERT FORMULA AND TACTICS FOR MEASURING].”"
Quotable: "reasons for the North Star"
Quotable: "The real muscle to develop is continuously checking to see whether your North Star Metric and inputs represent your current beliefs, product vision, and product strategy"
Quotable: "The inputs are the actionable factors that combine to drive your North Star Metric. Your inputs are the causes most likely to produce an effect."
Quotable: "Does it express customer value?"
Quotable: "Does it represent your vision and strategy?"
Quotable: "Is it a leading indicator of success?"
Quotable: "Is it understandable to non-technical partners?"
Quotable: "It's not a vanity metric?"
Quotable: "Gibson Biddle, then the VP of product at Netflix, knew that retention was a lagging indicator, not a leading indicator. He needed to identify a leading indicator metric that his team could directly influence. He needed a North Star."
Quotable: "“At Netflix, we knew that improving retention was the critical metric to improve - it would improve both customer and shareholder value. But retention is very hard to move and A/B tests for retention require lots of time to see a meaningful difference,” said Gibson. “So we developed more sensitive proxy metrics. Our ‘percentage of new members who add at least three titles to their queue during their very first session with the service' is a good example.”"
Quotable: "To determine your metric and inputs, think conceptually about your North Star as a formula or equation... The North Star Metric is a function of a handful of factors."
Quotable: "Whether you do it now or later, the next step will be precisely defining your North Star Metric and its inputs."

**[3] Amplitude, Inc. - Find your North Star (North Star Hub).** vendor. **fetched-and-verified.**
`https://amplitude.com/north-star-hub`
Supports: Restates the playbook's core NSM definition in an FAQ format, confirming the definition is consistent across Amplitude's canon; Confirms the hub page's copyright notice and its auto-updating year template. Contested/time-bound: Retrieved by downloading the raw HTML directly (not WebFetch's summarizer) and stripping tags myself, so the extracted text is machine-rendered plaintext, not a hand-copied transcription; minor tag-stripping artifacts (e.g. a truncated word at a markup boundary) are possible at extraction seams. The page's footer copyright uses a live template ("© {{ currentYear }} Amplitude, Inc.") confirmed in the raw markup, meaning the displayed year (2026 at retrieval time) is not a fixed publication date.
Quotable: "What is a North Star Metric? A North Star Metric is a single metric that best captures the value customers derive from your product. The North Star Metric is defined by three core qualities:"
Quotable: "Early-stage startups and companies new to the framework might modify their North Star Metric every six to 12 months. However, more established organizations usually don't need to change their North Star Metric as frequently"
Quotable: "every one to three years is more typical."
Quotable: "You should revisit your North Star metric periodically, whenever there's a significant shift in your product, market, or business strategy."

**[4] Intercom (interviewer: Adam Risman), featuring Sean Ellis - Sean Ellis on charting a path toward sustainable growth (Inside Intercom podcast, episode write-up).** primary. **fetched-and-verified.**
`https://www.intercom.com/blog/podcasts/sean-ellis-growth/`
Supports: Sean Ellis's own, first-person definition and discussion of the North Star Metric, in his own words, dated 7 June 2018; Confirms Ellis explicitly claims authorship of 'growth hacking' (coined 2010) in this same interview, by contrast with his NOT making an equivalent explicit originator claim for 'North Star Metric'; Ellis's own worked examples of North Star Metrics (Airbnb nights booked, Facebook DAU); Ellis distinguishing the North Star Metric from 'the one metric that matters'. Contested/time-bound: IMPORTANT CAVEAT: this is a published interview write-up, not a raw transcript; narration and editorial framing are interleaved with Sean Ellis's first-person answers under the same 'Sean:' speaker tag (e.g. a third-person aside, 'In Sean’s recently revised Growth Pyramid, finding a North Star Metric directly follows product/market fit,' appears mid-answer and cannot be Ellis's own first-person wording even though it sits inside a block attributed to him -- I excluded that sentence from the quotable list for this reason). Within this interview Ellis explicitly claims personal authorship of 'growth hacking' ('I came up with the phrase') but at no point in this piece does he make an equivalent first-person originator claim for 'North Star Metric' -- he defines and advocates for it but does not say 'I coined this' or give a date of invention. This is the strongest primary source found for Ellis's own voice on the concept; it does NOT settle the origination-date question.
Quotable: "The North Star Metric is really trying to quantify that value over time."
Quotable: "Sean: Airbnb’s metric is nights booked."
Quotable: "For something like Facebook, an easier proxy for value is just “daily active users.” That’s their North Star Metric."
Quotable: "I don’t think the North Star Metric is necessarily the same thing. The North Star Metric is a persistent overall success metric, and if you want to drive the North Star Metric, there might be a “one metric that matters” right now."
Quotable: "The North Star Metric is Sean's way of quantifying the point where customers experience the value of your product."
Quotable: "a key cog in a sustainable growth strategy"
Quotable: "I came up with the phrase because I thought startups had no choice but to be super focused on growth."

**[5] VentureBeat - Growing Your Company? Why the North Star Metric Works.** practitioner. **url-confirmed-not-read.**
`https://venturebeat.com/business/growing-your-company-why-the-north-star-metric-works`
Supports: Secondary credit: identified by WebSearch summary as crediting Sean Ellis (described as GrowthHackers CEO/founder) with coining the term. Contested/time-bound: Not read directly -- only a WebSearch-generated summary was available, so nothing from this source is quotable and its claim (Ellis as coiner) should be treated as a secondary, unverified attribution until the article itself is read.

**[6] BrightTalk, presented by John Cutler - Increase the Business Impact of your Product Team | North Star Framework & OKRs (webinar listing).** practitioner. **url-confirmed-not-read.**
`https://brighttalk.com/webcast/19204/520343`
Supports: Webinar description (per WebSearch summary) frames OKRs and North Star Metrics as 'different but complementary' and covers how to integrate OKRs with the Framework -- i.e., Cutler himself treats them as adjacent, not nested, methodologies. Contested/time-bound: Only the listing's search-engine summary was seen, not the webinar itself or a transcript; the 'different but complementary' characterization is a WebSearch paraphrase of the listing copy, not a verified direct quote from Cutler.

**[7] Open Practice Library - North Star Framework (practice entry).** reference. **fetched-and-verified.**
`https://openpracticelibrary.com/practice/north-star-framework`
Supports: A free, CC-BY-licensed community wiki page that explicitly points back to Amplitude's playbook and canvas as its source and reproduces Amplitude's seven-point checklist near-verbatim. Useful mainly as independent confirmation that Amplitude's checklist and canvas are the reference point other write-ups build on, and that it extends the framework to operational (not just product) decisions. Contested/time-bound: Does not independently corroborate guardrail/counter-metrics, ownership, or multi-product sections; it defers to Amplitude's canvas rather than adding structure of its own.
Quotable: "The framework is equally useful for decisions related to the product as well as to operational aspects of the organization aligned to the product, e.g. Support, Customer Success, Product Marketing."
Quotable: "According to Sean Ellis, who coined this term, this is the single metric that best captures the core value that your product delivers to customers."
Quotable: "To help find a North Star, we make use of a simple canvas, such as the one provided in Amplitude's playbook"

### STRUCTURE: WHAT A NORTH STAR DOCUMENT CARRIES

**[8] Lilach Bullock - The North Star Metric Worksheet Template.** practitioner. **fetched-and-verified.**
`https://www.lilachbullock.com/resources/north-star-metric-worksheet-template/`
Supports: A six-section written worksheet distinct from Amplitude's. Confirms 'alternative metrics considered and rejected' as a named section family ('Vanity Metric Audit', 'Metric Hierarchy (What Stays and What Goes)') and a time-boxed target section ('Set Your 90-Day Target'). Gated behind an email/name signup; only the landing page (intro sentence and the six section titles) was readable, not the worksheet's internal fields or prompts. Contested/time-bound: Access gated behind an email/name form ('Free instant access' is misleading -- the resource opens only after signup); internal section content could not be verified.
Quotable: "Work through each section in order and you will leave with one metric, a 90-day target, and a clear view of what to stop measuring."
Quotable: "What is inside Your Vanity Metric Audit Map Your Revenue Path The North Star Candidate Test Pressure-Test Your North Star Set Your 90-Day Target The Metric Hierarchy (What Stays and What Goes)"

**[9] Process Street - North Star Strategy Template.** vendor. **fetched-and-verified.**
`https://www.process.st/templates/north-star-strategy-template/`
Supports: A 20-step written workflow template (not a canvas) with a free-text or file-upload field per step: defining the metric and its inputs, an input-outcome model, goals and measurement plans per input (up to 5), success metrics, a communication plan, ongoing monitoring, and two review/iteration steps near the end. Supports 'when and why it is revisited' (steps 17 and 20) but has no field for rejected alternatives, counter-metrics/guardrails, an explicit owner, or multi-product handling. Contested/time-bound: The page does not state whether the template is free to use; it offers 'Edit in Process Street' and 'Request a demo' links without listing a price.
Quotable: "1 Identify Critical Inputs for North Star Metric 2 Define North Star Metric 3 Approval: North Star Metric Definition 4 Determine the Key Factors or Inputs 5 Create an Input-Outcome Model 6 Approval: Input-Outcome Model 7 Identify the Key Behaviors 8 Validation of Inputs and Key Behaviors 9 Approval: Inputs and Behaviors Validation 10 Establish Goals for Each Input 11 Create Plan for Measuring and Tracking Inputs 12 Gather Base Data for Inputs 13 Define Success Metrics 14 Approval: Success Metrics Definition 15 Communicate Strategy and Goals to Team 16 Implement Monitoring of Inputs 17 Regular Analysis of the North Star Metric and Inputs 18 Adjust Strategy Based on Data Analysis 19 Approval: Strategy Adjustments 20 Review and Iteration of the North Star Strategy"
Quotable: "Input 1 Goal Input 2 Goal Input 3 Goal Input 4 Goal Input 5 Goal"
Quotable: "North Star Metric Success Metric Input 1 Success Metric Input 2 Success Metric Input 3 Success Metric Input 4 Success Metric"

**[10] Umbrex (consulting network resource page) - North Star Metric Framework (Product-Led Growth).** reference. **fetched-and-verified.**
`https://umbrex.com/resources/frameworks/marketing-frameworks/north-star-metric-framework-product-led-growth/`
Supports: An 11-section reference article, not a fillable worksheet, but the single richest source found for the four hardest candidate sections: guardrail/counter-metrics, gaming, ownership, and revisit cadence. Also names 'Complex portfolios' (multi-product) as a stated limitation and answers 'Can we have multiple North Stars?' directly in its FAQ. Contested/time-bound: The page reads as a generated/SEO reference article (part of a 400+ entry marketing-framework catalog) rather than a primary practitioner account; its numbers (e.g. '6-10 input metrics', specific LTV/CAC figures in the worked example) are illustrative, not sourced to a named company.
Quotable: "A strong NSM reflects the core “job” your product does for users - e.g., “weekly active teams collaborating,” “successful orders delivered,” or “hours of learner mastery.” It is supported by a small set of input metrics (the levers teams can pull) and guardrails (quality, margin, reliability) to prevent local optimizations that harm long-term value."
Quotable: "Guardrails: Quality and economics limits to prevent “hitting the target but missing the point.” Examples: NPS/CSAT, complaint/return rates, reliability (P95 latency, errors), margins, compliance/privacy incidents."
Quotable: "Define input metrics and guardrails For the chosen NSM, identify 6-10 input metrics across the customer journey - each mapped to an owning team. Define guardrails (quality, margin, reliability, compliance) and thresholds that must not be breached."
Quotable: "Teams own 1-3 input metrics each; OKRs/KRs roll up to NSM movement while respecting guardrails."
Quotable: "Operate the cadence Weekly: review NSM and input deltas; unblock owners. Monthly: deep dive cohorts and economics; rebalance capacity to the most responsive inputs. Quarterly: reassess definitions, targets, and input set."
Quotable: "Evolve thoughtfully Only change the NSM when strategy or product fundamentally shifts, and after parallel tracking. Keep a versioned definition history to preserve comparability."
Quotable: "Limitations Oversimplification risk: A single metric can mask trade-offs; without guardrails, teams may “game” the NSM. Selection risk: A poor NSM (activity not value) drives the wrong behavior and breaks the revenue link. Data dependency: Requires trustworthy telemetry, cohort analysis, and consistent definitions. Complex portfolios: Multi-product or multi-journey businesses may need a small set of NSMs or a hierarchy (corporate NSM with product-level NSMs)."
Quotable: "How do we keep the NSM from being gamed? Define guardrails (quality, reliability, margin) and audit them weekly. Maintain a clear, versioned definition; monitor segment cuts; and tie recognition to moving NSM and staying within guardrails."
Quotable: "Can we have multiple North Stars? Each product line or distinct customer journey can have one NSM. At the company level, maintain one roll-up NSM or a small hierarchy with a clear mapping. Too many “north stars” erode focus."
Quotable: "How often should we change the NSM? Rarely. Adjust only when strategy or product fundamentally shifts. If you change, run the new and old in parallel for at least a quarter and communicate the rationale and differences."

**[11] Confidence by Spotify - What is a North Star Metric? (glossary).** vendor. **fetched-and-verified.**
`https://confidence.spotify.com/glossary/north-star-metric`
Supports: Spotify's own experimentation-platform glossary. Directly supports 'gaming' and 'limitations' with named sentences, and 'when to revisit' via its own Q&A heading. Also defines 'Guardrail Metric' as a related glossary term, but as a general experimentation concept (monitored during an experiment), not as a field inside a North Star document. Contested/time-bound: None observed beyond the note above.
Quotable: "North star metrics tend to be high-level and slow-moving. A change to one feature in a large product may genuinely improve user value, but the effect on a product-wide north star metric will be tiny and drowned out by variance from everything else happening in the product. An experiment would need an impractically large sample size to detect a statistically significant change."
Quotable: "It's resistant to gaming. Because the north star influences priorities across the organization, it will be optimized for. If it can be inflated by tactics that don't create real value (the same failure mode that plagues proxy metrics), it will be. The best north star metrics measure outcomes that are hard to fake."
Quotable: "Can a north star metric change? Yes, and it should when the product's value proposition evolves... The north star should reflect the current strategic question: what is the most important dimension of value we need to grow right now?"
Quotable: "Changing the north star is a significant organizational decision. It resets what teams prioritize, which experiments they run, and how they measure success."
Quotable: "Guardrail Metric A guardrail metric is a metric monitored during an experiment to ensure the change doesn't cause unintended harm, even when the success metric improves."

**[12] borghei/Claude-Skills (GitHub, open-source AI-skill repository; author handle 'borghei') - north-star-metric SKILL.md.** reference. **fetched-and-verified.**
`https://github.com/borghei/Claude-Skills/blob/main/project-management/execution/north-star-metric/SKILL.md`
Supports: Relied on for nothing in this bundle: an agent-skill file with no named publisher behind it, so not a structural source (tier2-specs.md, 2026-10-12). What the researcher recorded: An open-source (MIT + Commons Clause) skill definition that names anti-metrics and counter-metrics as explicit, distinct components of an NSM specification, ties counter-metrics explicitly to 'guard against gaming', and references a fill-in template (verified separately below). Contested/time-bound: This is an unofficial, third-party AI-tooling artifact, not a product-management institution's published guidance; it is evidence of a pattern spreading through practitioner tooling, not a second primary source.

**[13] borghei/Claude-Skills (GitHub) - nsm_spec_template.md.** reference. **fetched-and-verified.**
`https://github.com/borghei/Claude-Skills/blob/main/project-management/execution/north-star-metric/assets/nsm_spec_template.md`
Supports: Relied on for nothing in this bundle: an agent-skill file with no named publisher behind it, so not a structural source (tier2-specs.md, 2026-10-12). What the researcher recorded: The single most direct piece of evidence found for a FULL-variant structure: a complete fill-in-the-blank written document (not a canvas) with named sections for 'Rejected alternatives', an 'Owner' column on every metric table, a 'Review cadence' field and a 'Next review' date field, and distinct 'Anti-metrics' and 'Counter-metrics' tables with thresholds and owners. Contested/time-bound: Same provenance caveat as the SKILL.md above: an individual practitioner's open-source template, not an institutionally published one. It is also the only source found that gives the NSM document itself an 'Owner'/'Sponsor' field rather than only giving owners to individual input metrics.

**[14] borghei/Claude-Skills (GitHub) - metrics-dashboard SKILL.md.** reference. **fetched-and-verified.**
`https://github.com/borghei/Claude-Skills/blob/main/project-management/discovery/metrics-dashboard/SKILL.md`
Supports: Relied on for nothing in this bundle: an agent-skill file with no named publisher behind it, so not a structural source (tier2-specs.md, 2026-10-12). What the researcher recorded: A companion skill describing a 4-layer metrics architecture (North Star / input metrics / guardrails / operational metrics) with named owners per team and weekly cadence; corroborates guardrails-as-counter-metrics and 'hard to game' as a quality bar for the North Star itself. Contested/time-bound: Same unofficial-tooling caveat as the other borghei/Claude-Skills entries.

**[15] phuryn/pm-skills (GitHub, open-source AI-skill repository) - north-star-metric SKILL.md.** reference. **fetched-and-verified.**
`https://github.com/phuryn/pm-skills/blob/main/pm-marketing-growth/skills/north-star-metric/SKILL.md`
Supports: Relied on for nothing in this bundle: an agent-skill file with no named publisher behind it, so not a structural source (tier2-specs.md, 2026-10-12). What the researcher recorded: A second, independently authored open-source skill. Reproduces Amplitude's three-game classification (Attention/Transaction/Productivity) near-verbatim under different branding, confirming that typology's spread, and a 7-criteria checklist close to but not identical to Amplitude's 7-item checklist. Notably contains NO mention of guardrails, counter-metrics, an owner field, or a revisit cadence -- unlike the borghei repository above, despite covering the same topic. Contested/time-bound: This source's silence on guardrails/ownership/revisit-cadence is itself evidence that these fields are NOT yet a universal convention across derivative North Star templates -- only some adopt them.

**[16] Grow & Retain (Substack newsletter) - Review of your key metric (newsletter post).** practitioner. **fetched-and-verified.**
`https://growandretain.substack.com/p/north-star-metrics-`
Supports: Independent, non-Amplitude-affiliated corroboration that periodic revisiting of the North Star Metric is treated as standard practitioner advice, using Netflix as the worked example (the same Netflix example Amplitude uses, but reaching it independently). Contested/time-bound: None observed.
Quotable: "It's also the case that you should review your key metric regularly. Especially for a start up, your focus may need to shift from customer acquisition to retention. Netflix has changed its North Star metric multiple times - it certainly wouldn't make sense for it still to be tracking the percentage of DVDs that arrived the next day in the mail."

**[17] UserJot (product feedback-board SaaS company blog) - Defining Your North Star Metric: A Step-by-Step Approach.** vendor. **fetched-and-verified.**
`https://userjot.com/blog/how-to-define-north-star-metric`
Supports: A step-by-step article (no document template with named fields) that independently corroborates 'when and why it is revisited' as a step in the process, framed as ongoing validation rather than a scheduled cadence. Contested/time-bound: None observed.
Quotable: "And as your product changes, check if the metric still makes sense. If it doesn't, update it."
Quotable: "Your product and customers will change, so your metric might need to shift too."

**[18] concepts.dsebastien.net (personal knowledge-base site) - Guardrail Metrics (concept page).** reference. **url-confirmed-not-read.**
`https://concepts.dsebastien.net/concept/guardrail-metrics/`
Supports: URL resolves and the page title confirms the topic ('Guardrail Metrics'), but the page is a client-side-rendered single-page app; the body text did not load in a plain HTTP fetch, so no claim rests on this source alone. Contested/time-bound: Could not independently verify a WebSearch-reported claim that this page lists 'Counter Metrics' and 'Balancing Metrics' as alternate names for guardrail metrics.

**[19] Inter-American Development Bank (IDB), hosted on iadb.notion.site - North Star metric (internal Notion page).** practitioner. **url-confirmed-not-read.**
`https://iadb.notion.site/North-Star-metric-9e54d5a9e3ae46b28b45a17bfbac059e`
Supports: Notable as a real organization's own North Star Metric Notion page (a genuine Notion-hosted written document, not a vendor template), potentially relevant to the 'applies to a company with several products' question given IDB's multi-program structure. Could not be read: Notion renders content client-side in JavaScript, which a plain HTTP fetch does not execute, so the page returned no body text. Contested/time-bound: Unverified; do not rely on secondhand summaries of this page's content.

**[20] Mural - Project North Star (workshop template).** vendor. **url-confirmed-not-read.**
`https://www.mural.co/templates/project-north-star`
Supports: Identified via search as a Mural whiteboard template for North Star workshops. Explicitly excluded from this dimension's scope per the task's own instruction that Miro/Mural-style boards are canvases, not documents, and so do not count as evidence of written-document structure. Contested/time-bound: Not analyzed further; listed only to record that it was found and deliberately excluded.

### INPUT METRICS AND HOW THEY ARE CHOSEN

**[21] Julia Sholtz, Amplitude - Every Product Needs a North Star Metric: Here's How to Find Yours.** vendor. **fetched-and-verified.**
`https://amplitude.com/blog/product-north-star-metric`
Supports: Q1; Q2. Contested/time-bound: None observed; consistent with Amplitude's other North Star material fetched in this research. Defines a good North Star Metric as having two parts, one of which IS a vision statement and the other a strategy measure -- vision and strategy are folded into the metric's own definition rather than placed in a sequence before or after it. Never mentions OKRs, objectives, or key results anywhere in the article (confirmed absent by full-text search). Mentions roadmaps only once, in a table-of-contents-style line about operationalizing the metric, with no detail on ordering. Contested/time-bound: Differs from Herbig in framing: Amplitude folds 'a statement of your product vision' directly into the definition of the North Star Metric itself, rather than treating vision as a separate, prior document the metric flows from. Amplitude's own primary North Star explainer never mentions OKRs at all, which is notable given how central the NSM-vs-OKR distinction is to Herbig's piece. A good NSM write-up pairs a product-vision statement with the metric; stresses the metric must align to customer value and be a leading indicator; describes the 3-5 input-metric structure and the breadth/depth/frequency/efficiency heuristic for deriving inputs; states the NSM's communication and accountability purpose; lists 'When to change your North Star Metric' as a named topic the company's own playbook covers (but this article does not itself explain it).
Quotable: "Inputs are a set of three to five influential, complementary factors that you believe most directly affect your North Star Metric and that your team can directly influence through your product."
Quotable: "One heuristic we've found helpful when teams are determining inputs is considering breadth, depth, frequency, and efficiency. The inputs to a North Star Metric often follow this pattern, which you can easily adapt to different contexts."
Quotable: "A critical aspect of a good North Star Metric is that it's a leading indicator of future success. Lagging indicators like monthly revenue or average revenue per user (ARPU) don't give you an early signal of product impact. They tell you what happened in the past rather than predicting future revenue. The further upstream of revenue and market capitalization you can get your metric, the more future impact you can drive."
Quotable: "In most cases, the answer to this question is "yes." It's unlikely that one product leader should manage more than one North Star. Certainly, larger enterprises with multiple or diverse divisions, product management and development departments, and customer bases could have different North Star Metrics, each with its own inputs."
Quotable: "we recommend having a single North Star with one metric and its inputs per product."
Quotable: "A good North Star Metric consists of two parts: A statement of your product vision A metric that serves as a key measure of your current product strategy"
Quotable: "The North Star Metric you define should spring from a deep understanding of the actions within your product that provide realized value to your customer."
Quotable: "expressing your company’s and your product’s strategy and mission"
Quotable: "Putting Your North Star Metric into action by connecting it to your work through levels of bets, incorporating into your roadmaps, and more."
Quotable: "Your North Star Metric should be the key measure of success for your company's product team. It defines the relationship between the"
Quotable: "It gives your organization"
Quotable: "clarity and alignment"
Quotable: "on what your product team needs to optimize and what they can trade off."
Quotable: "It communicates your product organization’s"
Quotable: "impact and progress"
Quotable: "to the rest of the company - resulting in more support and acceleration of"
Quotable: "Most importantly, it holds product teams"
Quotable: "accountable for an outcome."
Quotable: "A good North Star Metric consists of two parts:"
Quotable: "A statement of your product vision"
Quotable: "A metric that serves as a key measure of your current product strategy"
Quotable: "A good North Star Metric also aligns to"
Quotable: "customer value"
Quotable: ", represents your product strategy, and is a leading indicator of success."
Quotable: "” or “Registered Users” don't make good North Star Metrics. Though anecdotally useful, they say nothing about what your customers value about your product."
Quotable: "A critical aspect of a good North Star Metric is that it's a leading indicator of future success."
Quotable: "Instead, a subscription-based business could identify characteristics that correlate with a user who is likely to renew their subscription and then build a North Star around that."
Quotable: "One heuristic we've found helpful when teams are determining inputs is considering breadth, depth, frequency, and efficiency."
Quotable: "Using this framework, every team knows what their inputs are and how they contribute to the North Star. This enables everyone to make the right trade-offs and resourcing decisions."
Quotable: "But if a team contributes to a single profit and loss (P&L) statement with a single product development department and a single product or even a product portfolio that serves a single customer base, we recommend having a single North Star with one metric and its inputs per product."
Quotable: "When to change your North Star Metric."

**[22] Julia Sholtz, Amplitude - What Makes a Good vs Bad North Star Metric.** vendor. **fetched-and-verified.**
`https://amplitude.com/blog/good-bad-north-star-metric`
Supports: Q1; Q2; Q3; Q4. Contested/time-bound: None observed. Note: this article states precise formulas directly in the narrative itself (e.g. the >3-users-week-1 example), which is evidence on Q4 that industry practice tends to put the formula in the same artifact that names the metric, rather than deferring it to a separate spec -- though no source explicitly discusses document architecture. Q2: names vanity metrics, lagging indicators (MRR/ARPU), and revenue-as-NSM as bad-metric patterns; also states the NSM should not be influenced directly (deliberate design choice, not accidental flaw) and that teams fail when they don't connect the NSM to customer value; Q2: attributes to John Cutler the design rule that a directly-movable metric is probably not a good North Star; Q4: Amplitude says it changed its own North Star Metric at least three times, and a strong North Star 'can and should evolve' as product/strategy grow; a named practitioner (Ted Clark) suggests revising when the NSM stops directionally predicting revenue. Contested/time-bound: Amplitude is the company that formalized the North Star Framework (named in the task brief), so this source doubles as near-primary material on the framework's own design rules, even though it is commercial/vendor content. Its claim that a metric you can move directly is 'probably not a good North Star' is in tension with the separate practitioner criticism (HackerNoon, below) that a North Star the team cannot influence at all is also a named failure mode -- the resolution both camps converge on is indirect influence via input metrics, not direct and not zero. Core definition and three qualities of a good NSM; explicit instruction to validate the metric against retention and revenue in the company's own data; named practitioner quotes (John Cutler, Ted Clark) on why the metric must be one level removed from direct control and must track revenue direction; traps around vanity/lagging metrics and over-fitting to current data/tooling. Contested/time-bound: Amplitude's own company examples (Airbnb nights booked, Spotify time spent listening, etc.) are flagged by Amplitude itself as community-cited illustrations, not confirmed official statements from those companies.
Quotable: "A North Star Metric is a single metric that best captures the value customers derive from your product. It's defined by three core qualities"
Quotable: "It represents the value users get from your product."
Quotable: "It's within product and marketing's sphere of influence."
Quotable: "It's a leading indicator of revenue."
Quotable: "So how does a North Star Metric differ from a KPI? Think of it as the single, value-based outcome that sits above the many operational KPIs your team already tracks. Measures like monthly recurring revenue (MRR) or average revenue per user (ARPU) tell you how the business performed, but your North Star captures the core value customers get and points to where those numbers are heading - it's a leading indicator, not a lagging one."
Quotable: "Inputs are typically a set of three to five influential, complementary factors that you believe most directly affect your North Star Metric and that your teams can directly influence with their day-to-day work through your product offering."
Quotable: "Your North Star Metric is an outcome or output, meaning its value depends on changes in your inputs. As such, you shouldn't be able to influence the North Star directly."
Quotable: "We view the North Star Metric as a function of key inputs that are both descriptive and actionable."
Quotable: "Lagging metrics like “Monthly Recurring Revenue” or “Average Revenue per User (ARPU)” aren't optimal North Star Metrics because they tell you what happened in the past rather than predicting future results. Leave the past in the past, and focus on leading indicators."
Quotable: "While North Stars should be a leading indicator of revenue, they shouldn't over focus on revenue. Why? Revenue is a lagging indicator. With revenue, what's done is done - meaning, you can no longer impact the outcome. So “don't” make revenue your North Star Metric, but “do” relate your North Star Metric to revenue."
Quotable: "This more precise metric - "trial accounts with >3 users active in week 1” - provides more insight into the value the account is getting and provides a signal of future trial conversion and subscription revenue that the product team can predict and drive."
Quotable: "Start from the customer's value moment - the point where people get what they came for."
Quotable: "Express that moment as a specific, measurable behavior rather than a feeling."
Quotable: "Make it time-bound and within your control, so teams can actually move it through their work."
Quotable: "Confirm it's a leading indicator of revenue, not a lagging measure like MRR or ARPU."
Quotable: "Validate that it predicts retention and revenue in your own data."
Quotable: "However, avoid the trap of thinking that your North Star must be something you can measure with your current data and tools."
Quotable: "explains John Cutler, former Amplitude Product Evangelist and co-author of The North Star Playbook"
Quotable: "Be wary of choosing vanity metrics for your North Star Metric."
Quotable: "aren't optimal North Star Metrics because they tell you what happened in the past"
Quotable: "you shouldn't be able to influence the North Star directly"
Quotable: "If you can move your North Star directly, it's probably not a good North Star."
Quotable: "changed our North Star Metric at least three times"
Quotable: "can and should evolve as your product and strategy grow"
Quotable: "A North Star Metric is a single metric that best captures the value customers derive from your product. It’s defined by three core qualities:"
Quotable: "It’s within product and marketing’s sphere of influence."
Quotable: "It’s a leading indicator of revenue."
Quotable: "This more precise metric - “trial accounts with >3 users active in week 1” - provides more insight into the value the account is getting and provides a signal of future trial conversion and subscription revenue that the product team can predict and drive."
Quotable: "“If you can move your North Star directly, it’s probably not a good North Star,” explains John Cutler, former Amplitude Product Evangelist and co-author of"
Quotable: "Your team selected this metric over something like “total number of items delivered monthly” or “total order value” because your data shows that customers value on-time deliveries, and they’re a strong predictor of future purchases."
Quotable: "Be wary of choosing vanity metrics for your North Star Metric. They look great on the surface but don't translate to meaningful business outcomes or tell you about your product’s long-term success."
Quotable: "So “don’t” make revenue your North Star Metric, but “do” relate your North Star Metric to revenue."
Quotable: "“If your North Star is flat, then expect your revenue to be flat,” explains Ted Clark, Senior Customer Success Architect at Amplitude. “But if at any point your North Star isn’t directionally indicating where your revenue is going, then it’s time to revise it.”"
Quotable: "Validate that it predicts retention and revenue in your own data. With"
Quotable: "product analytics"
Quotable: ", you can test a candidate metric against funnels, user journeys, and retention to see whether it holds up before you commit."
Quotable: "There’s no one-size-fits-all approach to the North Star Metric. It's different for every business, and to make things more complex, it also changes over time. Heck, at Amplitude, we’ve changed our North Star Metric at least three times as we’ve evolved and tweaked our strategy."
Quotable: "These examples are widely cited across the product community, so treat them as illustrations rather than official statements from each company."

**[23] Justin Bauer (former CPO), Amplitude - We're Evolving Our Product's North Star Metric. Here's Why.** vendor. **fetched-and-verified.**
`https://amplitude.com/blog/evolving-the-product-north-star-metric`
Supports: Q1; Q2. Contested/time-bound: This is Amplitude's own, first-party example of a North Star Metric and its named leading-indicator inputs for an analytics product (itself an analytics/BI vendor), directly answering Q2's request for an analytics-product example. It predates the >3-years-old blog refresh date visible on the other two Amplitude posts (2026 recommended-reading modules), so the WLU metric described may no longer be Amplitude's current North Star -- the 2024 good-bad-north-star-metric post says Amplitude has 'changed our North Star Metric at least three times.' A real, named company's first-person account of choosing, validating, and later replacing its own North Star Metric: explains the original metric (weekly querying users), how it was validated as a leading indicator of retention/expansion, why it was abandoned when the strategy changed, the precise behavior-plus-7-day-window definition of the replacement metric (weekly learning user), and the three new named input metrics with their own definitions and time windows. Contested/time-bound: Describes Amplitude's own metric as of this article's writing; the company's good-bad-north-star-metric article (above) says it has since changed its North Star at least three times, so WLU/BL/CoL may not be current.
Quotable: "We organize our product team around our own north star and its leading indicators - this has been a very successful strategy for us, driving more than 4x growth of our user base in the past two years."
Quotable: "As a product analytics solution, our main value proposition was helping product managers and analysts answer questions, so we decided to use a ‘query' as our indicator of value... So we aligned around ‘weekly querying users' (WQUs) as our north star."
Quotable: "But in addition to adapting our north star, we also wanted to identify the key leading indicators of this new metric so that we could align our pods to that strategy. We identified three new metrics for our team to set goals against: 1. Activated Accounts ... 2. Broadcasted Learnings ... 3. Consumption of Learnings"
Quotable: "A WLU is a user who is active and shares a learning that is consumed by at least 2 other people in the previous 7 days."
Quotable: "We believe our new north star metric better reflects our current product strategy - the value that we are delivering to our customers - and is a good leading indicator of revenue for the company."
Quotable: "This isn’t just a “set it and forget it” thing we do at the leadership level."
Quotable: "But what do you do when your strategy changes?"
Quotable: "So we aligned around ‘weekly querying users’ (WQUs) as our north star. This worked really well for us - we found that not only did WQUs reflect customers getting value out of Amplitude, but that this was also a leading indicator of our ability to retain and expand accounts to grow our business."
Quotable: "But over time we recognized that this metric wasn’t truly reflecting the type of impact we wanted to have with our customers. Our mission isn’t to help users build better analyses - it’s to help companies build better products."
Quotable: "Changing a north star metric, especially at a company as analytically oriented as ours, is no small task."
Quotable: "Based on all of this, we ran correlations against our contract data and compared that to our existing WQU metric."
Quotable: "We ultimately landed on a north star definition that we felt was simple enough for people to understand…we call it the “weekly learning user” (WLU)."
Quotable: "Activated accounts are organizations that have reached at least 5 WLUs. We have found that once we reach this threshold, there is a high likelihood that this customer will continue to grow with us."
Quotable: "A chart, dashboard, or"
Quotable: "Notebook"
Quotable: "is considered to be a “broadcasted learning” (BL) when it is consumed by 2 or more people within a 7 day period."
Quotable: "Consumption of learnings (CoL) measures the total reach of all BL."
Quotable: "We believe our new north star metric better reflects our current product strategy - the value that we are delivering to our customers - and is a good leading indicator of revenue for the company. In the past 6 months we’ve seen a 50% increase in the number of WLUs per active organization."

**[24] Mixpanel Team - What is a North Star metric?.** vendor. **fetched-and-verified.**
`https://mixpanel.com/blog/north-star-metric/`
Supports: Q1; Q3. Contested/time-bound: Mixpanel is a competitor vendor to Amplitude selling a 'Metric Trees' product feature, so its framing (preferring a 'focus metric' + KPIs over a strict single North Star) is commercially motivated, not a neutral academic claim. Q1: states companies typically have only one NSM but argues a single one can be limiting for multi-product companies; prefers a 'focus metric' framing; says complex business models can have multiple North Stars; Q2: lagging-ness of focus/NSM metrics; insight vs. action gap; revenue-without-customer-value fails long run; comp-structure conflicts create internal resistance to adoption; Q4: companies should feel free to reevaluate and amend a flawed NSM; sometimes need to 'pivot and rejigger' it to match a new mission; always okay to rethink rather than chase the wrong star; Q5: NSM only works if not taken too literally, must reflect all three of customer happiness/profit/measurable progress, and needs cross-silo culture or adoption suffers. Contested/time-bound: This is the source of the one-vs-several debate named in the brief. Mixpanel (a vendor competing with Amplitude, which formalized the North Star Framework) takes the 'several is fine / prefer a softer focus-metric framing' side; Amplitude's own material takes the 'one per product leader' side (see Amplitude source below). Treat as a vendor-vs-vendor framing disagreement, not a neutral academic one. Explicit ownership requirement per metric in the tree; a governance/change-log practice distinct from a one-time 'when to change it' rule; a named contested claim that the single-metric framing is 'mostly rhetorical'; a named organizational-incentive blind spot (compensation conflicts can make employees reject the metric); an unattributed practitioner pull-quote on using the metric as a planning/prioritization filter. Contested/time-bound: Directly contests the single-metric premise that Amplitude, Basedash, Cut the SaaS, and Koji.so all argue for: Mixpanel calls the 'one metric' framing 'mostly rhetorical' and says complex companies can have multiple North Stars.
Quotable: "A North Star metric is the one measurement that's most predictive of a company's long-term success. To qualify as a “North Star,” a metric must do three things: lead to revenue, reflect customer value, and measure progress."
Quotable: "A metric tree is a logical hierarchy of your growth model that maps how input metrics (at varying levels of granularity) feed into focus metrics, which in turn impact your North Star."
Quotable: "while they're great indicators of overall health, they're often lagging and don't help with daily decisions. Focus metric = Business/team value moment + Natural frequency"
Quotable: "Companies typically have only one North Star metric. However, a single north star can be limiting, especially if your company has multiple core products with separate goals... As such, we prefer the softer framing of a “focus metric” working in conjunction with other key performance indicators (KPIs)."
Quotable: "Ask "What is essential to the business's functioning?" Prioritize a list. Ask "What KPIs and metrics measure the top few key factors?" Ask "What metric encapsulates all of the above?" Build a metric hierarchy with the North Star metric on top of the pyramid."
Quotable: "Every metric should have clear documentation - how it's defined, calculated, and where the data comes from."
Quotable: "Companies typically have only one North Star metric."
Quotable: "However, a single north star can be limiting, especially if your company has multiple core products with separate goals"
Quotable: "we prefer the softer framing of a “focus metric” working in conjunction with other key performance indicators (KPIs)"
Quotable: "Companies with complex business models can have multiple North Stars."
Quotable: "they're often lagging and don't help with daily decisions"
Quotable: "spotting a change isn't the same as knowing what to do about it"
Quotable: "A metric that simply makes money without satisfying customers will fail in the long run."
Quotable: "Companies should feel equally free to reevaluate their North Star metrics"
Quotable: "amend them when they prove flawed"
Quotable: "always okay to backstep and rethink things, as the last thing you want is to be chasing the wrong star"
Quotable: "A North Star metric is the one measurement that’s most predictive of a company’s long-term success. To qualify as a “North Star,” a metric must do three things: lead to revenue, reflect customer value, and measure progress."
Quotable: "The term North Star metric - drawn from the common name for Polaris, the star that lies directly above the Earth’s Northern pole - is mostly rhetorical. Companies with complex business models can have multiple North Stars, and any given North Star metric is composed of sub-metrics anyway."
Quotable: "Companies should feel equally free to reevaluate their North Star metrics to make sure they still point the right direction, and amend them when they prove flawed."
Quotable: "Without cross-silo relationships and a willingness to prioritize the company good above the team good, some employees may reject the North Star metric, especially if they must change their behavior significantly, or if, like many sales teams, their compensation structure presents a conflict of interest."
Quotable: "“An effective north star metric is a product manager’s best friend. It provides cross-functional alignment on goals and tasks, and an objective barometer for success when a product ships. Even products that generate direct revenue require an alternative product metric that tells a more holistic story of what’s going on. When your north star metric is clear, product ideation becomes a lot easier. Instead of asking yourself 'What should I build next?' you should be asking 'What feature or product is most likely to move this metric the most?”"
Quotable: "Every key metric in your tree should have an owner accountable for monitoring it, interpreting changes, and initiating action. That doesn’t mean they solve every problem alone, but it does mean they don’t wait for someone else to notice an issue."
Quotable: "A marketing lead might own campaign-specific churn, while the product team owns retention overall."
Quotable: "Assign ownership and accountability. Ensure every key metric has a clear owner responsible for monitoring trends and acting on insights."
Quotable: "As your metric trees grow, governance becomes essential. Every metric should have clear documentation - how it’s defined, calculated, and where the data comes from. Changes to any metric, thresholds, or definitions should be communicated broadly. It’s best to maintain a log of decisions tied to metric shifts (who acted, when, why) to ensure continuity and help new hires ramp up quickly."

**[25] Mixpanel Team - Guardrail metrics: The complete guide to balanced product growth.** vendor. **fetched-and-verified.**
`https://mixpanel.com/blog/guardrail-metrics/`
Supports: Q5. Contested/time-bound: Mixpanel's own framing scopes guardrail/counter-metrics primarily to A/B-test safety (catching an experiment's side effects), which is a narrower use than 'a metric permanently paired with the North Star.' The Airbnb and Spotify examples it cites are about experiment guardrails specifically, not standing North-Star companions.
Quotable: "Guardrail metrics (sometimes called counter-metrics) are secondary metrics that you monitor while conducting experiments and A/B testing."
Quotable: "A negatively-impacted guardrail metric is an early sign that an experiment is having unintended consequences in other parts of the product, so you can evaluate if it's actually performing as hoped (and pause it if it isn't)."
Quotable: "North star metrics are guiding metrics that a company uses to determine long-term strategy. They serve to get the company aligned and working towards a shared goal. North Star metrics can change, but they're intended as overarching metrics that guide companies over time."
Quotable: "Guardrail metrics are secondary metrics. If primary metrics tell you if a project is successful, secondary metrics help you see the broader context and measure potential unintended impacts that your experiment can have on your product."
Quotable: "You can choose two or three guardrail metrics for an experiment, but don't go wild either - tracking too many guardrail metrics will increase the risk of false positives."
Quotable: "To mitigate risk, Airbnb developed their Experiment Guardrail system. If an experiment triggers a guardrail (harms a key metric that the company wants to protect), it goes through an escalation process to discuss results before proceeding."
Quotable: "Start with 2-3 guardrails that matter most to your product health."
Quotable: "Mixpanel can help you track, monitor, and analyze all of your metrics in a single convenient platform, from your North Star to your guardrails."

**[26] Mixpanel Team (quoting Dan Schmidt, Mixpanel Product Engineer) - North Star maps vs. algebraic KPI trees: How to know what to choose.** vendor. **fetched-and-verified.**
`https://mixpanel.com/blog/north-star-framework-vs-kpi-tree/`
Supports: Q3. Contested/time-bound: This Mixpanel post independently corroborates the Netflix DVD-queue leading-indicator story told in Amplitude's workshop PDF, though both are vendor retellings of Gibson Biddle's anecdote rather than a primary account from Biddle himself.
Quotable: "Different companies use different languages. Some talk about input metrics. Others have growth models, KPI trees, or rely on North Star frameworks. The terminology varies, but the underlying idea is the same: the best companies have a clear model that connects everyday work to the business outcomes that matter."
Quotable: "An algebraic KPI tree (sometimes called a deterministic metric tree) is built on fixed mathematical relationships. You take a top-level metric and break it into its mathematical components... Each parent metric is the precise calculation of its children."
Quotable: "A North Star map (also called a probabilistic or hypothesis metric tree) deals in hypotheses rather than certainties. The connections are based on evidence, not formulas: for example, the hypothesis that improving onboarding completion will increase week-one retention."
Quotable: "Netflix is the classic example. When it was still shipping DVDs to people's homes, it was trying to grow retention, a lagging indicator that's hard to move... Netflix found that subscribers with three or more DVDs in their queue were far more likely to stick around. That signal became its North Star metric."
Quotable: "Three DVDs in a queue was a valuable indicator, but unlike a number in an algebraic tree, it isn't a mathematical certainty and can't be calculated cleanly."
Quotable: "In general, Algebraic KPI trees support fast fixes and quick gains. North Star maps are more conducive to long-term strategy planning."

**[27] Itamar Gilad - The Three True-North Metrics that Your Product and Business Need.** practitioner. **fetched-and-verified.**
`https://itamargilad.com/the-three-true-north-metrics-that-your-product-and-business-need/`
Supports: Q1; Q3; Q5. Contested/time-bound: CONTESTED/DISCREPANCY: a secondary aggregator (Zurb Radar, see below) summarizes this same article as proposing 'three true-north metrics: one for value to the customer, one top business KPI, and one balancing health metric that catches the damage.' Reading the primary article directly, I found no 'balancing health metric' concept anywhere in the text -- the article's three elements are the NSM (value delivered), the Top Business KPI (value captured), and the OMTM (tactical focus). The secondary source's gloss appears to be an inaccurate paraphrase of this primary source; treat the 'balancing metric' framing as belonging to Zurb Radar / its other cited author, not to Gilad's piece as actually written.
Quotable: "Growth guru, Sean Ellis, defines the north star metric as the “aggregate value that people get from you product, … your value footprint”."
Quotable: "many people believe you have to pick just one top-level metric and call it the North Star. Given this choice most leadership teams will pick a business KPI (“Our north star is profit”), and push back against a company-wide value-delivered metric. In practice it's important to define, measure and set goals for both."
Quotable: "Croll and Yoskovitz define the OMTM as the “one number that you're completely focused on above anything else at your current stage”, and that “answers the most important question you have”."
Quotable: "The north star metric and top business KPI are usually too high-level, and dependent on too many factors to influence directly. The OMTM is designed to be actionable."
Quotable: "The OMTM brings focus to your tactical execution, while the NSM and top KPI set the strategic goals."
Quotable: "A good way to test this is to decompose the North Star Metric and top business KPI into their supporting metrics trees and check how much overlap there is."

**[28] Ray / Benjamin Scott, ZURB Radar (curated digest, citing Itamar Gilad, Petra Wille, Ethan Garr, and 'Justin C') - One Number Is a Trap: Build a Metric Tree Your Whole Team Can Aim At.** practitioner. **fetched-and-verified.**
`https://radar.zurb.com/article/one-number-is-a-trap-build-a-metric-tree-your-whole-team-can-aim-at`
Supports: Q3; Q5. Contested/time-bound: This is a curated digest article (dated Jul 8, 2026) that paraphrases several other writers' primary posts rather than presenting its own original framework. Its paraphrase of Itamar Gilad's article (see above) does not match what that primary source actually says -- flagged as a contested/inaccurate secondary gloss, not a camp disagreement between primary sources.
Quotable: "The problem is not that you picked a metric. It is that you picked only one, and left it hanging with nothing around it."
Quotable: "Itamar Gilad makes the case that one metric cannot carry a whole product and business. He suggests three true-north metrics instead: one for value to the customer, one top business KPI, and one balancing health metric that catches the damage."
Quotable: "Most teams cannot say which numbers matter or why their daily work moves the big goal. A KPI tree fixes that."
Quotable: "The metric tree is not really a measurement tool. It is a way to argue in public."
Quotable: "A lone north star hides those fights."

**[29] Ward van Gasteren, growwithward.com - OMTM: What is the One Metric That Matters? (4 steps to find yours + examples).** practitioner. **fetched-and-verified.**
`https://growwithward.com/one-metric-that-matter`
Supports: Q3. Contested/time-bound: The quoted sentence 'The OMTM concept was coined in 2013 by' is cut off mid-sentence in the extracted text (the attribution, presumably to Lean Analytics / Croll and Yoskovitz, is on the next element); do not rely on this source alone for the coining date or attribution -- corroborated instead by Itamar Gilad's piece and Mixpanel's North Star article, both of which attribute OMTM to the book Lean Analytics.
Quotable: "The One Metric That Matters is a number that you only use within your growth team, while a North Star Metric is even higher above the organization and is intended as a focus for the entire company to grow to. You can therefore also have multiple OMTMs within one company (if you have several growth teams), but always a maximum of one North Star Metric."
Quotable: "You use an OMTM for about 2 to 4 months and then choose another OMTM for the following months. However, your North Star Metric never changes unless you would completely change your business model."
Quotable: "Finally, your OMTM is actually supporting your North Star Metric. After you decide what your North Star Metric is, the growth team determines which number they should target as One Metric That Matters to contribute the most to the North Star Metric."
Quotable: "The OMTM concept was coined in 2013 by"

**[30] Sean Ellis and Ben Yoskovitz, Growth with Sean Ellis (Substack) - OMTM vs. NSM: Why You Need Both to Drive Startup Growth.** practitioner. **fetched-and-verified.**
`https://seanellis.substack.com/p/omtm-vs-nsm-why-you-need-both-to`
Supports: Q3. Contested/time-bound: This post is paywalled past its opening paragraph. Only the free preview shown above was read; the full comparison (which the title promises: 'Why You Need Both') was NOT retrieved and no claim here rests on its unseen content. Notable as a primary-ish source since it is co-written by both term-originators, but its substantive comparison is inaccessible without a paid subscription.
Quotable: "Ben Yoskovitz and I write a shared post about two key startup concepts: The One Metric That Matters and the North Star Metric"
Quotable: "Ben introduced the world to the concept of the One Metric That Matters, and he's helped countless teams focus their efforts and find traction."

**[31] Monetizely (getmonetizely.com) - Time to Activation: The Critical SaaS Metric You Should Be Tracking.** vendor. **fetched-and-verified.**
`https://www.getmonetizely.com/articles/time-to-activation-the-critical-saas-metric-you-should-be-tracking`
Supports: Q2. Contested/time-bound: This article explicitly places Time to Activation on the EXECUTIVE DASHBOARD alongside CAC/LTV/churn -- i.e. treats it as a KPI, not as the formal North Star Metric -- and its one use of the phrase 'north star' ('speed to value their north star') is the colloquial, non-technical sense of 'top priority,' not an invocation of the Sean Ellis North Star Metric framework. Its benchmark figures (median TTA of 14/7/1-3 days by segment) are attributed to 'a ProfitWell study' that I could not locate or verify; treat those specific numbers as unverified. No analytics/BI-specific (as opposed to general SaaS) example of time-to-value or time-to-insight as a North Star candidate was found in this research; this is a gap, not a finding -- see key_findings.
Quotable: "Time to Activation (TTA) measures how long it takes a new user to reach their first "aha moment" or value realization after signup."
Quotable: "Time to Activation = Time of Activation Event - Time of Initial Signup"
Quotable: "Dropbox famously improved their activation rate by identifying that users who uploaded at least one file were significantly more likely to become paying customers. By focusing their onboarding flow on getting users to upload a file as quickly as possible, they reduced their Time to Activation by 30%, which correlated with a 10% increase in conversion rates."
Quotable: "Time to Activation deserves a place on your executive dashboard alongside CAC, LTV, and churn."
Quotable: "the companies that make simplicity and speed to value their north star will maintain a significant competitive advantage."

### DEBATES, CRITIQUES AND CADENCE

**[32] Kerry Jones - How North Star Metrics Can Lead You South.** practitioner. **fetched-and-verified.**
`https://hackernoon.com/how-north-star-metrics-can-lead-you-south-1488c09891de`
Supports: Q2: names gaming directly -- applying pressure to a metric produces 'screwy results'; flags the NSM as a lagging metric that wouldn't catch a problem immediately; flags that a growth-only NSM 'completely misses anything that relates to retention' (ignores customer value); Q1/Q3: notes departments getting their own 'isolated NSMs' becomes more common and more of a problem as a company grows -- an implicit argument against proliferating North Stars per team.
Quotable: "When you don’t properly qualify metrics people will turn them into a game."
Quotable: "give someone a metric and apply pressure to them to hit that metric and you get some screwy results."
Quotable: "Note, this is a lagging metric, so it wouldn’t catch something immediately."
Quotable: "It completely misses anything that relates to retention."
Quotable: "This becomes more important and apparent when a company is growing and departments get their own isolated NSMs."
Quotable: "the single metric that best captures the core value that your product delivers to customers"

**[33] Maahir Shah (Product Manager, Facebook), interviewed on Mind the Product's The Product Experience - When not to use a North Star (The Product Experience podcast).** practitioner. **fetched-and-verified.**
`https://mindtheproduct.com/north-star-maahir-shah-the-product-experience`
Supports: Q2: North Star 'becomes bad' when it is treated as the primary or sole input to every product decision, producing 'short sighted near term myopic thinking' instead of long-term user value; notes it's unlikely every small piece of work will move the metric; Q3: for zero-to-one products, data can't reliably predict outcomes yet, and it is 'naive' to go straight from building a product to exposing it to very large audiences before checking quality -- an argument for delaying a precise, scaled North Star in very early-stage work. Contested/time-bound: Dated March 2, 2022; a podcast transcript, so some phrasing is conversational rather than written prose. Does not name pre-PMF startups or internal platforms explicitly -- the zero-to-one framing is the closest analogue found for Q3 in this source.
Quotable: "it's very hard to like accurately use data to like tell you exactly what is going to happen"
Quotable: "it's unlikely that every single small thing that you do is going to move a Northstar metric"
Quotable: "short sighted near term myopic thinking versus thinking about long term value and what's good for the end user"

**[34] Ibrahim Bashir - South Star Metrics.** practitioner. **fetched-and-verified.**
`https://runthebusiness.substack.com/p/south-star-metrics`
Supports: Q2: states Goodhart's law explicitly, gives a named gaming example (a Windows Update team that stopped asking users a question rather than fix the underlying issue), and flags business metrics that rise while hurting customer experience (ad load up, CSAT down); Q2: argues revenue is partly a function of sales execution and demand pipeline, not just product value, so holding a product team to a revenue-flavored North Star can demoralize them for outcomes they don't control. Contested/time-bound: Published June 30, 2020. Coins the term 'south star metric' for a metric optimized in a way that damages the business -- a practitioner-coined label, not an industry-standard term.
Quotable: "when a measure becomes a target it ceases to be a good measure"
Quotable: "we decided to just stop asking users!"
Quotable: "revenue is a function of demand pipeline / sales execution and not just product value"

**[35] Sam Blumenthal - The North Star Metric: A Simple Guide.** practitioner. **fetched-and-verified.**
`https://compoundingthoughts.substack.com/p/the-north-star-metric-a-simple-guide`
Supports: Q2: names vanity metrics (DAUs/registered users) and lagging metrics (revenue lags behavioral signals) as two of the core failure modes.

**[36] Britt Mills, Bridgenext - Five Common Mistakes When Creating a North Star for Digital Experiences (and How to Avoid Them).** vendor. **fetched-and-verified.**
`https://www.bridgenext.com/blog/how-to-avoid-common-mistakes-when-creating-a-north-star/`
Supports: Q5: names five document-writing mistakes directly: being too vague/generic, focusing on outputs instead of outcomes, ignoring the user's emotional journey, creating the North Star in a leadership silo without buy-in, and not evolving the North Star as the product grows. Contested/time-bound: Published by a CX consultancy (09.10.25); framed around 'North Star' as a CX/digital-experience vision as much as a single quantitative metric, slightly broader than the strict NSM definition used elsewhere in this research set.
Quotable: "Mistake: Being Too Vague or Generic."
Quotable: "Mistake: Focusing on Outputs, Not Outcomes."
Quotable: "Mistake: Ignoring the User’s Emotional Journey."
Quotable: "Mistake: Creating a North Star in a Silo."
Quotable: "Mistake: Not Evolving the North Star as the Product Grows (Recalibrating)."

**[37] ThinkInsights - Data-Driven Strategy and KPI Design Playbook (Strategy Pyramid, Metrics Framework).** vendor. **fetched-and-verified.**
`https://thinkinsights.net/playbooks/data-driven-strategy-and-kpi-design-playbook-strategy-pyramid-metrics-framework`
Supports: Q4: gives a specific stability rule (treat as stable for at least a year) and named triggers (growth stage, business model, or competitive position shift); states the rationale that frequent changes undermine the point of having a North Star at all. Contested/time-bound: A consulting/playbook site rather than a named company's own practice; the one-year stability figure is this source's own prescription, not a reported empirical finding.
Quotable: "Rarely - treat it as stable for at least a year unless the underlying strategic objectives genuinely shift"
Quotable: "a change in growth stage, business model, or competitive position"
Quotable: "Changing the North Star metric frequently undermines the entire point of having one"

**[38] Nick Chasinov, Teknicks - Airbnb's North Star Metric: Explained.** vendor. **fetched-and-verified.**
`https://teknicks.com/blog/airbnb-north-star-metric`
Supports: Q2/Q3: using Airbnb's 'Nights Booked' as the worked example, names tunnel vision and overfixation on the single number as risks, and notes the metric may not be equally relevant across all of Airbnb's markets. Contested/time-bound: Published May 23, 2024 (updated July 30, 2024) by a marketing agency; this is commentary on Airbnb's publicly known metric, not a statement from Airbnb itself. A WebSearch summary separately claimed Nights Booked 'ignores profit' and pushes geographic expansion, but that specific framing could not be confirmed verbatim on this page or any other fetched page, so it is omitted as unverified.
Quotable: "it can also lead to tunnel vision if not carefully managed"
Quotable: "Airbnb must ensure they don't become overly fixated on nights booked at the expense of other important metrics"
Quotable: "in some markets, the number of nights booked may not be the most relevant metric"

**[39] Brandon Weaver, Mixpanel - Go beyond the North Star: How to operationalize your growth strategy with metric trees.** vendor. **fetched-and-verified.**
`https://mixpanel.com/blog/beyond-north-star-metric-trees/`
Supports: Q2: argues a North Star alone 'leaves a gap in operational execution' and promotes a metric tree (input metrics feeding focus metrics feeding the North Star) as the fix, i.e. a named vendor camp arguing the single-NSM practice is insufficient by itself. Contested/time-bound: Published July 23, 2025 (last edited June 9, 2026) by Mixpanel, a vendor with a commercial incentive to sell a more elaborate metrics product than 'pick one North Star.' Read alongside Amplitude's material (which defends the single-NSM-plus-inputs design as sufficient) as a vendor-vs-vendor disagreement about whether the North Star Framework needs a bigger companion structure.
Quotable: "often leaves a gap in operational execution"

**[40] Gabe Strauss (post author), replying to commenter Jake Goldman - Flywheels: Theory to Action (comment thread).** practitioner. **fetched-and-verified.**
`https://behavioralhealthpm.substack.com/p/flywheels-theory-to-action/comments`
Supports: Q1: a named practitioner explicitly argues it is 'possible, and often valuable' for a company to have more than one North Star, giving a payor-centric vs. patient-centric split (healthcare) as the example, while still preferring to eventually integrate them into one higher-order metric. Contested/time-bound: A comment-thread exchange, not a published essay; low visibility/authority relative to Amplitude or Mixpanel's own material, but it is a named practitioner taking the explicit 'several is fine' side with a concrete two-sided (payor/patient) example, which is exactly the kind of split the task brief asks about.
Quotable: "I definitely think it's possible, and often valuable, for a company to have more than one north star."
Quotable: "One could be payor centric and the other patient centric."
Quotable: "ideally, you'd want to find a way to integrate them together into a single higher-order metric"

**[41] Jason Knight, One Knight in Product - Users, buyers, not picking favourites & noodling on North Star Metrics.** practitioner. **fetched-and-verified.**
`https://oneknightinproduct.substack.com/p/users-buyers-not-picking-favourites-noodling-on-north-star-metrics-1074472`
Supports: Q1: a named practitioner states in passing that a single North Star Metric 'probably isn't' a good idea for platform/B2B products with distinct stakeholder groups (buyers vs. users), though he does not develop a full alternative structure in the fetched text. Contested/time-bound: Published March 21, 2022. The one-NSM skepticism is stated as an aside ('leaving aside discussions...') rather than argued at length in what was retrieved; treat the position as asserted, not demonstrated, by this source.
Quotable: "Leaving aside discussions about whether one North Star Metric is a good idea (it probably isn't)."
Quotable: "You need to keep buyers onside otherwise you won't make any new sales."
Quotable: "But you need to keep the users onside otherwise you may not get that year 2 renewal."

**[42] Lenny Rachitsky, Lenny's Newsletter - Choosing Your North Star Metric.** practitioner. **fetched-and-verified.**
`https://www.lennysnewsletter.com/p/choosing-your-north-star-metric`
Supports: Referenced for completeness as one of the most widely cited North Star essays (six metric categories: revenue, customer growth, consumption growth, engagement, growth efficiency, user experience), but the fetched page only rendered the intro and comments -- the six-category breakdown itself lives on the linked a16z Future piece, which was not independently fetched, so that specific claim is not used as quotable here. Contested/time-bound: The deeper six-category taxonomy commonly attributed to this piece could not be verified against the primary page itself in this research pass; cite with that caveat if used elsewhere in the bundle.
Quotable: "Your North Star Metric is your strategy, and your strategy is your North Star Metric."

**[43] Brian Balfour, Reforge (transcript hosted by Roadmunk) - North star product metrics are leading you astray (Reforge / Brian Balfour).** practitioner. **not-retrieved.**
`https://roadmunk.com/guides/north-star-product-metrics-brian-balfour-reforge`
Supports: Not used for any standalone claim. WebSearch result summaries (not a verified page read) attributed to Balfour the positions that copying another company's North Star is a mistake, that revenue is an output of usage rather than a good North Star, and that changing the metric monthly means the strategy is effectively changing monthly. These are plausible and consistent with other verified sources in this set (e.g. ThinkInsights on change frequency, South Star Metrics and Compounding Thoughts on revenue-as-lagging) but could not be confirmed verbatim because the page returned HTTP 404 on two direct fetch attempts. Contested/time-bound: Excluded from quotable claims per honest-retrieval requirement; flagged here only so a future researcher knows this source was attempted and failed, not skipped.

### RELATIONSHIPS: VISION, STRATEGY, OKRS AND DASHBOARDS

**[44] Tim Herbig - How to connect North Star Metrics, Product Strategy, and OKRs.** practitioner. **fetched-and-verified.**
`https://herbig.co/product-strategy-metrics-sandwich/`
Supports: Primary source for the vision-then-NSM-then-strategy-then-OKRs chain under investigation. States the North Star Metric develops forward from the Product Vision and feeds Product Strategy; OKRs implement Strategy. Gives explicit time horizons: Vision and NSM are '(potentially) infinite'; Strategy has a 'smaller time horizon' (one source quoted in the piece puts strategy bets at roughly 12 to 18 months); OKRs are quarterly, 'sometimes even annual'. States the sequence explicitly as NSM, then Strategy, then OKRs. Does not mention 'roadmap' anywhere in the article (confirmed absent by full-text search of the downloaded page). Contested/time-bound: This is the only source found that states the NSM-before-Strategy sequence explicitly and by name ('first defining your North Star Metric, then articulating a Strategy'). The article never uses the word 'roadmap', so it cannot corroborate where a roadmap sits in the chain the task describes.
Quotable: "North Star Metrics are persistent goals that influence Product Strategy, whereas OKRs are point-in-time goals that implement that Strategy."
Quotable: "The North Star Metric is the Quantified Sibling of the Product Vision, which both sit within the Strategic Narrative Pattern as inputs for defining your Product Strategy."
Quotable: "Your North Star Metrics shouldn’t be set backwards from a KPI dashboard but develop forwards from your Product Vision."
Quotable: "If you have a genuinely user-centered Product Vision, your North Star Metric should almost "automagically" flow from it."
Quotable: "Vision and North Star Metric are about the (potentially) infinite product development journey, whereas Strategy has a smaller time horizon."
Quotable: "...first defining your North Star Metric, then articulating a Strategy and finally establishing OKRs ensures each gets the attention it deserves."
Quotable: "...how big are the risky bets over the next 12 to 18 months."
Quotable: "In contrast, OKRs typically have a quarterly (sometimes even annual) horizon, to implement Strategy."

**[45] Adam Farren (10x Operator, Substack) - What's a good North Star metric? It helps to have one metric to rule them all.** practitioner. **fetched-and-verified.**
`https://10xoperator.substack.com/p/guide-to-the-north-star-metric`
Supports: Lays out an explicit sequence -- vision first ('evergreen'), then product/go-to-market strategy ('durable...3-5 year timeframe'), then goals that 'translate to your roadmap and tactics', 'typically...annual and quarterly goals or OKRs' -- with all of that already established BEFORE the North Star Metric is introduced. The NSM is presented afterward as a cross-cutting alignment device layered on top of an existing vision-strategy-goals/OKRs stack, not as a step that precedes Strategy. Contested/time-bound: CONTESTED, directly against Herbig's stated sequence. Camp A (Herbig): North Star Metric is defined first, before Product Strategy, and persists above it. Camp B (Farren/10x Operator): vision, strategy, and goals/OKRs are already built out in that order; the North Star Metric is introduced afterward, as a unifying device layered on top of an existing stack, and is explicitly time-boxed to a maturity window ('after product/market fit...but before your company is truly scaling') rather than treated as a persistent, infinite-horizon artifact set ahead of strategy.
Quotable: "For any startup or product launch, everything starts with your vision."
Quotable: "Next you build product and go-to-market strategy. How will we achieve our vision, why will we win, what problem will we solve for our customers? This is durable, lasting you for a 3-5 year timeframe."
Quotable: "Then set your goals; these are shorter, more actionable, and can translate to your roadmap and tactics. Typically you set annual and quarterly goals or OKRs."
Quotable: "So how do you bring all of that - vision, strategy, tactics - into alignment? Defining a North Star metric is a great step."
Quotable: "The North Star is most useful after product/market fit (where you won’t be ready to set it), but before your company is truly scaling (where the complexity of goal-setting and operations makes aligning on a single metric impractical)"

**[46] Tability - What is a North Star Metric? (and how to actually use one).** vendor. **fetched-and-verified.**
`https://www.tability.io/odt/articles/north-star-metric`
Supports: Places the North Star Metric explicitly above OKRs in a hierarchy: NSM at the top, team-level KPIs as levers beneath it, OKRs translating those levers into time-bound goals. Explicitly frames a Key Result as a contribution TO the North Star, not as the North Star itself and not as a peer of it -- consistent with Herbig's and 10x Operator's shared view that the NSM sits above, not inside, the Objective/Key-Result structure. Full-text search of the downloaded page confirmed the word 'vision' does not appear anywhere on the page, so it is silent on vision placement. Contested/time-bound: Agrees with Herbig and with the general consensus found across sources: no source located treats the North Star Metric as literally an Objective or a Key Result within the OKR framework -- all treat it as sitting above or outside that structure, with Key Results contributing to it. This source is silent on vision and product strategy, so it cannot confirm or deny Herbig's specific vision-then-NSM-then-strategy order.
Quotable: "your North Star metric sits at the top. Your team-level KPIs describe the specific levers that move it. Your OKRs translate those levers into time-bound goals with clear ownership and regular check-ins."
Quotable: "You can set your North Star metric as a top-level outcome, then layer OKRs and initiatives underneath it."
Quotable: "Your North Star metric describes where you want to go. Your OKRs describe the specific progress you are committing to make this quarter. Each key result is a measurable contribution to moving the North Star."

**[47] Swiss Post (Post CH AG) - Digital Commerce Blog - North star guides product development.** vendor. **fetched-and-verified.**
`https://digital-commerce.post.ch/en/pages/blog/2020/north-star-guides-product-development`
Supports: Describes the North Star Metric as representing Product Strategy ('It represents the core of the product strategy') rather than preceding or generating it -- a softer, descriptive relationship than Herbig's directional 'NSM develops forwards from Vision and influences Strategy.' Connects OKRs to the North Star via sub-KPIs: the OKR carries out the process needed to hit a sub-KPI, which in turn is derived from the North Star. Ties the metric loosely to vision via example ('parameters more closely combined with the product vision') rather than stating vision precedes the metric. Contested/time-bound: Minor variant within the same broad camp as Herbig (NSM above OKRs, OKRs implement sub-goals), but frames the NSM-Strategy relationship as representational ('represents the core of') rather than sequential/causal ('develops forwards from... influences'). Does not state whether vision or strategy is written/decided first.
Quotable: "It represents the core of the product strategy."
Quotable: "there are other parameters more closely combined with the product vision"
Quotable: "the OKR defines the process that needs to be carried out in order to achieve a desired result (sub-KPI)"

### THE GAP QUESTION

**[48] Max Musing (Founder and CEO, Basedash) - How to choose a north star metric: a practical framework.** vendor. **fetched-and-verified.**
`https://www.basedash.com/blog/how-to-choose-a-north-star-metric-a-practical-framework`
Supports: A one-sentence communicability test distinct from the value statement itself; an explicit rule for when a metric may be changed versus merely redefined; an inversion test for catching metrics that can only rise; explicit alternatives ruled out with reasons (revenue, vanity counts, composite scores, per-team north stars); a single-exception rule (separate product lines) to the one-metric premise.
Quotable: "A north star metric is the one number that best represents the value customers get from your product. Moving it should reliably move long-term revenue and retention."
Quotable: "The emphasis on value matters. Your north star should be the measure that sits closest to the moment a customer gets what they came for, even if it is not your biggest number or your most impressive chart."
Quotable: "The healthiest setup is to treat the north star as the primary operating metric and revenue as the business result it should predict. If your north star climbs for two quarters and revenue does not follow, you probably picked the wrong north star, but that is no reason to abandon the approach."
Quotable: "Total registered users, cumulative downloads, and pageviews only go up. A metric that can never fall cannot warn you when something is wrong."
Quotable: "A north star only compounds if it holds long enough to shape decisions across many cycles. Redefine the calculation if you must, but do not swap the whole metric on a whim."
Quotable: "Rarely. A north star only compounds if it holds long enough to shape many decisions. You may refine how it is calculated as your understanding improves, but swapping the metric itself every quarter signals that it was not the right choice. Change it only when the business model or the value you deliver shifts."
Quotable: "Each input is something a specific team can own and affect directly."
Quotable: "If the metric seems to move on its own, teams stop trying. It has to connect to work people control."
Quotable: "Letting every team have its own north star."
Quotable: "A north star exists to align the company, and competing north stars undo that. Teams should have their own input metrics under the shared one."
Quotable: "Usually no. The purpose of a north star is focus, and multiple north stars defeat that. The exception is a company with separate product lines, which may need one per line. Individual teams should have their own input metrics, but the company should share a single north star."
Quotable: "Everyone from sales to engineering should be able to say what it means in one sentence. Composite scores with five weighted inputs fail this test even when they are technically better."
Quotable: "Write down the value your product delivers in one sentence."

**[49] Sameer and Ankit (Cut the SaaS) - North Star Metric: How to Pick One That Actually Works.** vendor. **fetched-and-verified.**
`https://cut-the-saas.com/guides/north-star-metric`
Supports: A plain-language value statement exercise ('fits on an index card'); explicit time-window instruction; the doubling test for catching vanity metrics; Goodhart's law named explicitly as the central blind spot, with a concrete failure story; guardrail-metric pairing (retention, gross margin) as the fix; the metric used as a planning filter ('does this move the north star?') with inputs explicitly named as 'where your roadmap lives'.
Quotable: "A north star metric is the one number that tells you whether your product is actually working, before your bank account does."
Quotable: "It is the single metric that best captures the value your customers get from your product, and it should move before revenue does, not after."
Quotable: "Name the value your customer actually pays you for, in one line on an index card."
Quotable: "Pick a metric that counts that action across a sensible time window, like weekly."
Quotable: "If this number doubled next month, would the business clearly be healthier? If not, it's a vanity metric."
Quotable: "Total signups, page views, and registered users all fail that test."
Quotable: "Start from the value your customer pays you for, then find the smallest number that proves they got it. Write down the core job your product does, identify the action that signals success, and pick a metric that counts that action over a sensible time window. That is the whole exercise, and it should fit on an index card."
Quotable: "when a measure becomes a target, it ceases to be a good measure."
Quotable: "Make signups the only metric that matters, and your team will chase junk traffic, buy questionable installs, and quietly let churn climb, all while the chart goes up and to the right. They are technically winning. The business is technically losing."
Quotable: "The other failure modes are betting the company on the wrong metric and tunnel vision that kills any experiment that might dent the number short term."
Quotable: "The fix is pairing your north star with guardrail metrics like retention and gross margin."
Quotable: "Every project then earns a simple question: does this move the north star? If not, you get to question why you are doing it."
Quotable: "recommends pairing your north star with three to five input metrics that your team can directly influence with day-to-day work. If your north star is weekly active users, your inputs might be activation rate, repeat usage, and re-engagement. Those inputs are where your roadmap lives."
Quotable: "an early marketer at Dropbox, LogMeIn, and Eventbrite, who wanted teams to stop arguing in meetings and rally around one number."

**[50] Koji (koji.so) - North Star Metric Framework: How to Find, Validate, and Move Your Product's One Metric That Matters (2026 Guide).** vendor. **fetched-and-verified.**
`https://www.koji.so/docs/north-star-metric-framework`
Supports: A reusable sentence template for stating customer value, explicitly sourced from customer language rather than a dashboard; a named instruction to validate the metric through customer interviews rather than data alone (to establish causation, not just correlation); a table of named real-company examples each attached to a named source (a practice this research could not independently verify for every row -- see caveat). Contested/time-bound: The per-company source table (e.g., 'Lenny Rachitsky, former Airbnb PM; S-1 (2020)' for Airbnb, 'Andrew Bosworth, internal memos; 10-K filings' for Meta) is Koji's own claim; this research verified only that Koji's page states these attributions, not that each underlying S-1/memo/interview actually says what Koji claims. The Sean Ellis 'canonical definition' Koji quotes could not be traced to and verified against Ellis's original 2017 post within this research's budget; treat that specific quote as vendor-relayed, not primary-verified.
Quotable: "A North Star Metric is the"
Quotable: "one measurable expression of customer value"
Quotable: "that every team in your company can rally around."
Quotable: ""We win when our customers [achieve X outcome] more often / more deeply / faster.""
Quotable: ""We win when our listeners spend more time experiencing music and audio they love.""
Quotable: ""We win when more travelers stay in homes they couldn't find on any other platform.""
Quotable: ""We win when more teams replace email with conversations that move work forward.""
Quotable: "You cannot write this sentence by staring at a dashboard. You write it by"
Quotable: "listening to customers describe value in their own words"
Quotable: "the metric must be validated against the people whose value it claims to represent."
Quotable: "A drop in Spotify's Time Spent Listening could be UX regression, content gap, competitive substitution, or seasonality. Dashboards correlate; interviews explain."
Quotable: "Notice the pattern: every metric describes a"
Quotable: "user behavior"
Quotable: "that delivers value, not an internal activity (signups, pageviews) or a lagging financial result (revenue, MRR)."

**[51] Ballpark - North Star Metric (glossary entry).** vendor. **fetched-and-verified.**
`https://ballparkhq.com/research-glossary/north-star-metric`
Supports: Instructs defining the customer outcome in ordinary language before picking a count; names a change-log practice -- preserving the old definition and explaining the break rather than silently rewriting history -- when the metric changes; guardrail pairing against harm/declining quality; a blind-spot framing that keeping a stale metric unchanged is 'not consistency but a measurement problem.'
Quotable: "A north star metric is a principal product measure intended to reflect customer value and align team decisions, supported by input measures and checks on trade-offs."
Quotable: "Define the customer outcome in ordinary language, identify behaviour that plausibly reflects it and investigate the relationship using research and product data."
Quotable: "Prefer a definition people can explain, inspect and reproduce."
Quotable: "Pair the shared measure with checks for harm or declining quality."
Quotable: "Revisit the measure when the product’s purpose or audience changes. Preserve the old definition and explain the break in the series rather than silently rewriting history."
Quotable: "A north star earns its place by helping people make coherent decisions; when it rewards activity that no longer represents value, keeping it unchanged is not consistency but a measurement problem."

**[52] Lenny Rachitsky (Lenny's Podcast / Lenny's Newsletter), summarizing an interview with Sean Ellis - The original growth hacker reveals his secrets | Sean Ellis (author of “Hacking Growth”).** practitioner. **fetched-and-verified.**
`https://www.lennysnewsletter.com/p/the-original-growth-hacker-sean-ellis`
Supports: An editorial 'takeaway' bullet (not a direct Sean Ellis quote) adding two selection criteria rarely repeated elsewhere: the metric must be actionable and 'not a ratio', and capable of scaling up over time. Contested/time-bound: This is the newsletter's own 'Some takeaways' summary of the Sean Ellis interview (Sep 05, 2024), not a transcript quotation from Ellis himself; the full episode transcript was not accessible to this research (paywalled/truncated page).
Quotable: "Choose a North Star metric that reflects the core value your product delivers to users. This metric should be actionable, not a ratio, and capable of scaling up over time. It should correlate with revenue growth but should not be revenue itself. Ensure that it provides a clear direction for the team and aligns with customer value."

**[53] UXCam Academy - Qualities of a great North Star metric.** vendor. **url-confirmed-not-read.**
`https://blog.uxcam.com/academy/mobile-app-product-management-certification/qualities-of-a-great-north-star-metric/`
Supports: WebSearch summary reports a seven-item checklist including 'not easily gamed' as a named quality, consistent with (but not independently verified against) the Goodhart's-law material this research did verify from Cut the SaaS and Basedash.

### ADMISSION SWEEP: READ IN A BROWSER, 2026-10-12

**[54] Reforge - North Star Metric (artifacts page).** vendor. **fetched-and-verified.**
`https://www.reforge.com/artifacts/c/team-operations/north-star-metric`
Supports: A negative finding for admission. The page lists two member-submitted artifacts under its North Star Metric heading: a framework for cascading goal targets through a leadership team, and a brand concept document. Neither is a North Star metric document, and the page shows no field names. Read in a browser on 2026-10-12, and every quotation here was checked against that read.
Quotable: "Explore 2 examples of North Star Metrics so you never have to start from scratch."
Quotable: "Updated July 1, 2024"
