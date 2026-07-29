# Product Roadmap: the companion

The reference behind the template. Read this when you want to know *why* a section exists, what the research
actually says, and where the field disagrees with itself.

## 1. Orientation

A product roadmap says in what order this product intends to solve the problems its strategy chose, and how
certain it is at each horizon. It sits below the strategy, which decides which problems are worth solving
[[24]](#ref-24), and above the backlog, which holds the specific work [[19]](#ref-19).

At a glance:

- Its lanes or timeframes are **confidence levels**, not dates in disguise [[7]](#ref-7).
- The sentence that settles most arguments about it: **"The roadmap shows the plan. The OKRs carry the
  commitment"** [[7]](#ref-7).
- **Nothing measures whether any roadmap practice improves outcomes.** That is a confirmed gap, searched
  for, and it is the most important thing on this page.
- Three formats ship here, from eight researched. Five were rejected, two of them because their own authors
  say they are not roadmaps.
- The word "roadmap" appears **nowhere** in the Scrum Guide [[21]](#ref-21).

**On evidence, plainly.** Two separate literatures use this word. Technology roadmapping has a documented,
peer-reviewed tradition going back to Motorola in the 1980s and formalised at Cambridge
[[1]](#ref-1)[[2]](#ref-2), and it studies organisation-level R&D planning. Software product roadmaps have a
much smaller, newer research thread [[3]](#ref-3)[[4]](#ref-4). **Neither measures whether a roadmap improves
outcomes**, and the first is not evidence for the second. Searching arXiv, Semantic Scholar and the general
web for a causal link between roadmap format, cadence or confidence device and product results returned
nothing.

What does exist is a convergence: Perri [[26]](#ref-26), Cagan [[15]](#ref-15), Bastow [[7]](#ref-7) and
Torres [[27]](#ref-27) arrive independently at the same design principle, **express less certainty further
out**. Four people reaching one conclusion without citing each other is worth following. It is still a
convergence of prescription, not a measurement, and this bundle will not dress it up as one.

## 2. Origins and evolution

**The origin is genuinely unresolved, and this bundle reports that rather than picking a story.**

Technology roadmapping has real history. The first journal paper is credited to Willyard and McClees in 1987
on Motorola's process, Robert Galvin supplied the definition everyone quotes, EIRMA formalised a generic
method in 1997, and Cambridge's T-Plan packaged it in the late 1990s [[1]](#ref-1)[[2]](#ref-2). Even that
account is contested by its own historians, who argue it under-credits earlier work at NASA, Boeing, GE,
Lockheed and elsewhere [[1]](#ref-1). Note what EIRMA already understood in 1997: a roadmap "is a living
document and is constantly evolving as circumstances change. It is quite different from a project plan"
[[1]](#ref-1).

**No transmission chain from that tradition into software product management was found.** The encyclopedia
article that would assert one does not [[5]](#ref-5). And the creator of one of the most widely used modern
formats describes inventing it in 2012 as a reaction to Gantt charts, with no reference to any of the
industrial lineage [[6]](#ref-6). The two practices share a name and a rough shape; whether one descends from
the other is **not verified**, and calling it settled either way would be inventing history.

## 3. Anatomy (section by section)

### The Outcome This Serves

The section that makes every other one judgeable. Without it, a reader cannot tell whether an item belongs,
and the roadmap silently becomes a list of whatever accumulated. That failure has a name and a mechanism:
when work is assembled bottom-up, "the intent behind the work has been quietly replaced by the gravity of the
backlog itself" [[8]](#ref-8).

### Now

Work in progress, shaped and understood. Say what problem each item solves rather than which feature ships:
a theme "commits to solving a specific customer problem" instead of promising a named thing
[[17]](#ref-17), which is what lets the team change its approach without breaking its word.

### Next

Problems being sharpened, expected to change. This is where roadmaps most often go dishonest, because Next is
close enough that people want dates and far enough that estimates do not hold. The whole reason to sort by
confidence is that "the further away something is, the more uncertain it is. Your roadmap should reflect
that" [[27]](#ref-27).

### Later

Problem areas nobody has shaped. Deliberately coarse. This is the lane people delete for being vague, and the
vagueness is the honest content.

**Do not use Later as a graveyard for requests you do not want to refuse.** Put them in the exclusions
instead. A Later item nobody intends to do is a refusal with a longer fuse.

### What Is Not On Here

**In the lean variant, deliberately**, and added to both other formats as this bundle's own addition. A
roadmap that cannot be cited to decline a request settles no arguments and changes no behaviour. It is also
what stops Later filling with things nobody will ever do.

### Confidence, and How It Decays (full)

Make the gradient explicit rather than leaving it implied. One published rule of thumb puts the current
quarter around "90% accurate, with decreasing accuracy for future quarters" [[30]](#ref-30). Treat that as a
vendor's heuristic, not a measured figure, and state your own gradient instead of borrowing a number you
cannot defend.

### Dependencies and What Could Move It (full)

Most slippage is not estimation error, it is a dependency nobody wrote down. A dependency with no stated
consequence is decoration; say what it would reorder.

### Review Trigger (full)

**Cadence is genuinely contested and neither side has measured anything.** One vendor's guidance gives fixed
intervals, "at least once a year" for planning and weekly for feature-level views [[31]](#ref-31). Named
practitioners argue instead for continuous, trigger-based revision: a roadmap is "a living document. If you
invalidate a theme, update it" [[26]](#ref-26). Pick one deliberately and write down which.

### Release Goals (GO format)

Five columns, from the published original: date, name, goal, features, metrics [[10]](#ref-10). The ordering
is the argument. **Fill the goal before the features**: features chosen first will always look like they
serve a goal, because the goal gets written to fit them. The same author's checklist is explicit that a
roadmap should not "state any product details such as user stories" [[11]](#ref-11).

### Product Vision, Business Objectives, Themes, Timeframes, Disclaimer (themes format)

The five-part structure from *Product Roadmaps Relaunched* [[16]](#ref-16). **Provenance matters here**: the
book itself could not be obtained, and this structure is reported by a third-party summary rather than quoted
from the authors. It is used because two independent summaries agree, and it is labelled as
summary-reported wherever it appears.

The **disclaimer** is a real section, not boilerplate, because a roadmap that travels gets read as a
commitment. Its limit is worth stating in the same breath: a disclaimer does not undo the effect, since
"the customers who read it will still hold you to it" [[23]](#ref-23).

## 4. Variants and sizing

**Lean** is the outcome, three lanes, and the exclusions: enough to end the weekly what-are-we-doing
conversation. **Full** adds what a reader outside the team needs: how confidence decays, what could move
things, and what brings the team back.

**Three formats ship, from eight researched.** The rule they had to clear is ADR 0028's: structurally
distinct **and** in circulation with a named source.

| Format | Why it ships |
|---|---|
| **now-next-later** (default) | Confidence lanes, no false precision, showable externally without implying a schedule [[6]](#ref-6)[[7]](#ref-7) |
| **go** | A measurable goal per release, which the other two deliberately do not force [[9]](#ref-9)[[10]](#ref-10) |
| **themes** | The only one carrying vision and objectives inside the document, so it can argue for itself [[16]](#ref-16) |

**Five were rejected**, and the rejections are the more useful result. The timeline form has no named
product-management practitioner defending it, despite a search aimed at finding one [[28]](#ref-28). The
release plan is a different artifact by the account of the person who named both [[12]](#ref-12). The
"release roadmap" is a relabel, and the Kanban board has no named source [[29]](#ref-29). Most importantly,
the **opportunity solution tree** [[18]](#ref-18) and **Cagan's OKR-based alternative** [[14]](#ref-14) were
excluded because their own authors present them as, respectively, a discovery artifact and an alternative
*to* roadmaps.

## 5. Methodology lineage

Methodology-agnostic, and one fact makes that unusually concrete: **the word "roadmap" does not appear
anywhere in the Scrum Guide** [[21]](#ref-21), confirmed by direct text search. The Guide defines the Product
Backlog as "an emergent, ordered list of what is needed to improve the product" and stops there. Whatever
framework you run, this artifact sits outside it and having one is a choice.

## 6. Debates and contested boundaries

**Is a roadmap a promise?** This is a genuine, published disagreement between named authors. One position:
"your roadmap does not represent an obligation or commitment to accomplish everything on it"
[[22]](#ref-22). The other, stated just as plainly: "Roadmaps are promises to yourself, your company, and
your customers" [[25]](#ref-25). Both are vendors, both have published the argument, and this bundle teaches
the disagreement rather than quietly siding.

**Do committed dates belong?** The most date-committed enterprise framework commits only its current
increment and calls the following two a forecast [[13]](#ref-13). The strongest critics say estimates for
undiscovered work are unreliable [[28]](#ref-28). Notice these are closer than the rhetoric suggests: both
accept that certainty decays.

**The fight is narrower than it looks.** The most-cited critic of feature roadmaps names the two legitimate
reasons management wants them, that leadership needs the highest-value work first and that businesses
sometimes must make date-based commitments [[14]](#ref-14), and writes that "product roadmaps are one of my
favorite tools. When done right, they are incredibly useful" [[15]](#ref-15). Torres says outright: "I want
to clarify that my issue is not with roadmaps altogether" [[28]](#ref-28). A bundle quoting only the attacks
would misrepresent the people it was quoting.

**The credible case for dates**, stated fairly: enterprise frameworks need them for regulatory and
cross-department coordination [[13]](#ref-13); enterprise sales genuinely needs committed windows, managed
with a deliberate buffer, since "delivery dates should be a quarter later than engineering dates,
anticipating slippage" [[20]](#ref-20); and hardware development has externally imposed validation gates
that no amount of theme language removes [[32]](#ref-32).

## 7. Anti-patterns and failure modes

| Anti-pattern | What it looks like | Why it fails | Source |
|---|---|---|---|
| **The feature-list roadmap** | Named features pinned to dates | Locks in solutions before discovery: "to lock in specific features at the roadmap level is to effectively skip the most important part of your job" | [[15]](#ref-15) |
| **The Gantt in disguise** | Roadmap that has drifted into a bar chart | "Now, Roadmaps function more like Gantt Charts" | [[26]](#ref-26) |
| **Lane collapse** | Now/Next/Later adopted, but stakeholders treat every lane as a commitment | Destroys the format's only purpose | [[27]](#ref-27) |
| **The backlog as roadmap** | Assembled bottom-up from accumulated requests | "The intent behind the work has been quietly replaced by the gravity of the backlog itself" | [[8]](#ref-8) |
| **The sales leak** | Internal roadmap forwarded to a prospect | "It is not uncommon for sales reps to share internal roadmaps with customers, as a way of closing a deal" | [[33]](#ref-33) |
| **The stale roadmap** | Published once, never revised | "Most product roadmaps are out of date as soon as the ink touches the paper" | [[27]](#ref-27) |
| **False precision** | Equal certainty at every horizon | Claims knowledge nobody has | [[27]](#ref-27) |
| **Later as a graveyard** | Refusals parked in the last lane | A refusal with a longer fuse, and it corrodes trust when discovered | JUDGMENT, from the exclusions argument above |

## 8. Relationships to other artifacts

| This document | Neighbour | How to tell them apart |
|---|---|---|
| roadmap | [product strategy](../product-strategy/) | Strategy decides which problems are worth solving; the roadmap orders them. The roadmap "takes the strategy as input" [[24]](#ref-24) |
| roadmap | [product backlog](../product-backlog/) | The backlog is "the single source of work undertaken by the Scrum Team" [[21]](#ref-21); the roadmap scopes what becomes backlog. "The roadmap conveys your strategy vs. the backlog conveys your plan to implement it" [[19]](#ref-19) |
| roadmap | release plan | A release plan is "a type of project plan - albeit an agile one" covering one release [[12]](#ref-12) |
| roadmap | OKRs | Neither governs the other; both descend from strategy [[24]](#ref-24). "The roadmap shows the plan. The OKRs carry the commitment" [[7]](#ref-7) |
| roadmap | Gantt chart | "A Gantt chart can help a team set a plan that details how they will complete a project. On the other hand, a roadmap will help them define and communicate why they should complete it" [[34]](#ref-34) |
| internal roadmap | public roadmap | Different obligations entirely. See section 9 |

## 9. Adaptations

**If it will be seen by customers, it is a different document.** Assume permanent visibility: "everyone will
see your customer-facing roadmap as soon as you share it: industry analysts, your company's toughest media
critics, even your competitors" [[23]](#ref-23). Strip competitive and technical-debt detail, use coarse time
frames [[11]](#ref-11), and understand the trap a public roadmap creates, put memorably by one practitioner
quoting another: "Either I'm going to disappoint you by giving you exactly what we thought six months ahead
of time was the best solution when it's not, or by changing course and having lied to you"
[[35]](#ref-35).

**If you genuinely must commit to a date**, do it deliberately and separately rather than by letting the
whole roadmap harden. One named mechanism is a Plan of Record, "a document that is managed by the delivery
manager, but the only one that can typically add an item to this is the CTO/VP Engineering" [[36]](#ref-36).
Scarcity is the feature.

**If you are in hardware**, external validation gates impose real lead times [[32]](#ref-32), and a pure
themes-and-no-dates roadmap will be ignored by the people who have to order components.

**Who writes it.** Published guidance says creation "should be a group effort, but the product management
team should ultimately be responsible" [[33]](#ref-33), and the alignment literature agrees that "ideally,
the entire product team works out the various sections...jointly and iteratively" [[37]](#ref-37).

**Two live public examples worth reading.** GitLab publishes a themed direction page that dates what has
shipped and leaves what is coming undated, under the heading "Plans subject to change" [[38]](#ref-38).
Buffer publishes a public suggestions board [[39]](#ref-39), which is a **feature-status board rather than a
strategic roadmap**, and is included here precisely because the difference is instructive.

## 10. Worked example

See [`product-roadmap_example.md`](product-roadmap_example.md): Acme Analytics, full variant, now-next-later
format. It sits between the [product strategy example](../product-strategy/product-strategy_example.md) and
the [Saved Views PRD](../prd/prd_example.md), and its Now lane contains the work that PRD specifies.

## References

<a id="ref-1"></a>[1] Clive Kerr and Robert Phaal. "[Technology roadmapping: industrial roots, forgotten history and unknown origins](https://api.repository.cam.ac.uk/server/api/core/bitstreams/970ba01f-0733-4529-8973-058ebc3f4155/content)." Technological Forecasting and Social Change 155, 2020. [academic]

<a id="ref-2"></a>[2] University of Cambridge Institute for Manufacturing. "[Technology roadmapping](https://engage.ifm.eng.cam.ac.uk/technology-roadmapping/)." [academic]

<a id="ref-3"></a>[3] Jurgen Munch, Stefan Trieflinger and Dominic Lang. "[Product Roadmap, From Vision to Reality: A Systematic Literature Review](https://ieeexplore.ieee.org/document/8792654/)." ICE/ITMC, 2019. [academic] **Not read**: publisher blocked retrieval. Cited only for the fact that a review scoped to product roadmaps exists.

<a id="ref-4"></a>[4] Stefan Trieflinger. "[DEEP: The Product Roadmap Self-Assessment Tool](https://medium.com/@stefan.trieflinger/deep-the-product-roadmap-self-assessment-tool-e0bf1430d50d)." [practitioner] Its dimension count is disputed between this explainer and a summary of the underlying paper, so nothing here depends on it.

<a id="ref-5"></a>[5] Wikipedia. "[Technology roadmap](https://en.wikipedia.org/wiki/Technology_roadmap)." [reference] Cited for a checkable negative: it asserts no lineage to software product management.

<a id="ref-6"></a>[6] Janna Bastow. "[The Birth of the Modern Roadmap for Product Management](https://www.prodpad.com/blog/the-birth-of-the-modern-roadmap/)." ProdPad. [practitioner]

<a id="ref-7"></a>[7] Janna Bastow. "[Why I Invented the Now-Next-Later Roadmap](https://www.prodpad.com/blog/invented-now-next-later-roadmap/)." ProdPad. [practitioner] The format's own publisher credits two creators, Bastow and Simon Cast; its 2012 date is a retrospective account not checked against a period source.

<a id="ref-8"></a>[8] Janna Bastow. "[The Danger of Bottom-Up Roadmaps](https://www.prodpad.com/blog/bottom-up-roadmaps/)." ProdPad. [practitioner]

<a id="ref-9"></a>[9] Roman Pichler. "[The GO Product Roadmap](https://www.romanpichler.com/blog/goal-oriented-agile-product-roadmap/)." [primary]

<a id="ref-10"></a>[10] Roman Pichler. "[GO Product Roadmap with Checklist](https://www.romanpichler.com/downloads/tools/GO-Product-Roadmap-with-Checklist.pdf)" (PDF). [primary] The five field definitions are read from the author's own artifact.

<a id="ref-11"></a>[11] Roman Pichler. "[GO Product Roadmap Checklist](https://romanpichler.medium.com/go-product-roadmap-checklist-37ad6ba100e9)." [practitioner]

<a id="ref-12"></a>[12] Roman Pichler. "[The Product Roadmap and the Release Plan](https://www.romanpichler.com/blog/product-roadmap-vs-release-plan/)." [primary]

<a id="ref-13"></a>[13] Scaled Agile. "[Roadmap](https://framework.scaledagile.com/roadmap/)." [standards]

<a id="ref-14"></a>[14] Marty Cagan. "[The Alternative to Roadmaps](https://www.svpg.com/the-alternative-to-roadmaps/)." Silicon Valley Product Group. [primary]

<a id="ref-15"></a>[15] Marty Cagan. "[Product Roadmaps](https://www.svpg.com/product-roadmaps/)." Silicon Valley Product Group. [primary]

<a id="ref-16"></a>[16] C. Todd Lombardo, Bruce McCarthy, Evan Ryan and Michael Connors. *Product Roadmaps Relaunched* (O'Reilly, 2017), read via [a third-party summary](https://cdn.bookey.app/files/pdf/book/en/product-roadmaps-relaunched.pdf). [reference] **The book was not read**; the five-part structure is summary-reported.

<a id="ref-17"></a>[17] Jared Spool. "[Themes: A Small Change to Product Roadmaps with Large Effects](https://articles.centercentre.com/themes/)." [practitioner] Credits the idea to Bruce McCarthy, through this single account.

<a id="ref-18"></a>[18] Teresa Torres. "[Opportunity Solution Tree](https://www.producttalk.org/glossary-discovery-opportunity-solution-tree/)." Product Talk. [primary]

<a id="ref-19"></a>[19] ProductPlan. "[Product Roadmap vs. Product Backlog](https://www.productplan.com/learn/product-roadmap-vs-product-backlog)." [vendor]

<a id="ref-20"></a>[20] Rich Mironov. "[The Roadmap Less Traveled](https://www.mironov.com/the_roadmap_less_traveled/)." [practitioner] The page's displayed date is unusually early for some of its content; flagged and unresolved.

<a id="ref-21"></a>[21] Ken Schwaber and Jeff Sutherland. "[The Scrum Guide](https://scrumguides.org/scrum-guide.html)." [primary] The absence of the word "roadmap" was confirmed by direct text search.

<a id="ref-22"></a>[22] ProductPlan. "[Your Product Roadmap Is a Plan, Not a Promise](https://www.productplan.com/learn/product-roadmap-plan/)." [vendor]

<a id="ref-23"></a>[23] ProductPlan. "[How to Create a Customer-Facing Roadmap](https://www.productplan.com/learn/how-to-customer-facing-roadmap)." [vendor]

<a id="ref-24"></a>[24] Roman Pichler. "[OKRs and Product Roadmaps](https://www.romanpichler.com/blog/okrs-and-product-roadmaps/)." [practitioner]

<a id="ref-25"></a>[25] Brian de Haaff. "[Your Roadmap Is a Promise (Do You Keep It?)](https://www.aha.io/blog/your-roadmap-is-a-promise-do-you-keep-it)." Aha! [vendor]

<a id="ref-26"></a>[26] Melissa Perri. "[Effective Product Roadmaps](https://melissaperri.com/blog/2017/02/15/product-roadmaps)." [primary]

<a id="ref-27"></a>[27] Teresa Torres. "[Product Roadmaps: How the Best Product Teams Plan for Uncertainty](https://www.producttalk.org/product-roadmaps/)." Product Talk. [primary]

<a id="ref-28"></a>[28] Teresa Torres. "[My Leaders Still Want Roadmaps with Timelines, What Should I Do?](https://www.producttalk.org/roadmaps-with-timelines/)" Product Talk. [primary]

<a id="ref-29"></a>[29] ProductPlan. "[Kanban Roadmap](https://www.productplan.com/glossary/kanban-roadmap)" (glossary). [vendor] Cited as a candidate format rejected for having no named practitioner behind it.

<a id="ref-30"></a>[30] airfocus. "[The Ultimate Guide to Roadmaps](https://airfocus.com/resources/guides/roadmaps/)." [vendor] The 90 percent figure is a vendor rule of thumb with no study behind it.

<a id="ref-31"></a>[31] Aha! "[Roadmap Planning: How Often Should PMs Revisit Their Plans?](https://www.aha.io/roadmapping/guide/product-management/roadmap-planning)" [vendor]

<a id="ref-32"></a>[32] Kevin Jankay. "[7 Adaptive Roadmaps to Align Hardware and Software Integration](https://gocious.com/blog/7-adaptive-roadmaps-to-align-hardware-and-software-integration)." Gocious. [vendor] Vendor content arguing for its own category; treated as directional.

<a id="ref-33"></a>[33] ProductPlan. "[The Ultimate Guide to Product Roadmaps](https://www.productplan.com/learn/what-is-a-product-roadmap)." [vendor]

<a id="ref-34"></a>[34] ProductPlan. "[Gantt Chart vs. Roadmap](https://www.productplan.com/learn/gantt-chart-vs-roadmap-whats-the-difference)." [vendor]

<a id="ref-35"></a>[35] Bruce McCarthy. "[A Roadmap Doesn't Have to Lead to Broken Promises](https://www.mindtheproduct.com/roadmap-doesnt-lead-broken-promises/)." Mind the Product. [practitioner] The quoted words are attributed by that article to David Cancel of Drift, not to McCarthy.

<a id="ref-36"></a>[36] Marty Cagan. "[Roadmap Alternative FAQ](https://www.svpg.com/roadmap-alternative-faq/)." Silicon Valley Product Group. [primary]

<a id="ref-37"></a>[37] Grote and colleagues. "[Product Roadmap Alignment, Achieving the Vision Together: A Grey Literature Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC7510781/)." [academic]

<a id="ref-38"></a>[38] GitLab. "[Direction: Plan](https://about.gitlab.com/direction/plan/)." [primary]

<a id="ref-39"></a>[39] Buffer. "[Introducing Our New Roadmap: Buffer Suggestions](https://buffer.com/resources/transparent-product-roadmap-v2/)." [primary] A feature-status board rather than a strategic roadmap.
