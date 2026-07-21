# Companion: The Product Backlog

> The deep explainer for the product-backlog bundle. Read this to understand what a product backlog is,
> where it came from, why it is shaped the way it is, and where practitioners disagree about it. The short
> operator card is [`product-backlog_guide.md`](product-backlog_guide.md); a fully worked instance is
> [`product-backlog_example.md`](product-backlog_example.md). Inline citations like [[1]](#ref-1) resolve
> to the [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A product backlog is **the single, ordered list of everything the team might do to improve a product, kept
alive and re-ordered as you learn.** It is not a requirements document filed once, not a task tracker of
committed work, and not a wish list that only grows: it is the one place the delivery team draws its work
from, ordered so that the most valuable and most informative work sits at the top. The 2020 Scrum Guide,
which owns the canonical definition, calls it *"an emergent, ordered list of what is needed to improve the
product"* and *"the single source of work undertaken by the Scrum Team"* [[1]](#ref-1).

The honest first thing to know is that the product backlog is **Scrum-canonical but under sustained
pressure.** Scrum names it one of three formal artifacts and, since 2020, anchors it to a Product Goal as
its commitment [[1]](#ref-1). At the same time, a strong current of product thinking argues that a
backlog of pre-decided features is the signature of a "feature factory" that ships output without moving
outcomes [[20]](#ref-20)[[26]](#ref-26). This bundle teaches the backlog that survives that critique: an
**ordered, emergent list anchored to a goal**, fed by discovery rather than by a stakeholder wish list.

**At a glance**
- It is **ordered, not merely prioritized.** The 2020 Scrum Guide deliberately says "ordered": the
  sequence reflects value, risk, dependency, and learning together, not a single priority score
  [[1]](#ref-1)[[3]](#ref-3).
- It is **emergent.** It changes constantly; a static backlog is a contradiction in terms
  [[1]](#ref-1)[[6]](#ref-6).
- It has **one owner and one ordering.** The Product Owner is accountable for what is in it and the order
  it is in; the developers size the items [[1]](#ref-1).
- It needs a **goal above it.** Without a Product Goal, an ordered list of features is just a feature
  factory with a sort order [[9]](#ref-9)[[10]](#ref-10).
- It is **output; the goal and the outcome sit above it.** The most important discipline around a backlog
  is keeping it anchored to an outcome, not letting it become the strategy [[26]](#ref-26)[[20]](#ref-20).

If you read nothing else: a product backlog is a **living, ordered queue of work in service of a goal.**
The moment it stops being re-ordered against what you have learned, or stops serving a goal you can name,
it has become the thing its critics warn about.

---

## 2. Origins and evolution

**The backlog began as a requirements list inside early Scrum.** Jeff Sutherland ran the first Scrum team
at Easel Corporation in 1994, and he and Ken Schwaber presented Scrum at OOPSLA in 1995, drawing on
Takeuchi and Nonaka's 1986 idea of overlapping, self-organizing product development [[5]](#ref-5).
Schwaber's 1996 write-up used the term **"Backlog"** (not yet "Product Backlog") and defined it as *"an
identification of all requirements that should be fulfilled in the completed product"* [[4]](#ref-4): a
flat, complete requirements list, closer to a specification than to the emergent, ordered artifact Scrum
teaches today.

**The concept matured across nine editions of the Scrum Guide (2009 to 2020).** Two changes matter most.
First, in **2011 the language shifted from "prioritized" to "ordered"** [[3]](#ref-3)[[12]](#ref-12). This
was not cosmetic: "prioritized" implies a single ranking dimension, while "ordered" lets the Product Owner
sequence by value, risk, dependency, and the desire to learn early, all at once. The 2011 Guide described
the backlog as *"often ordered by value, risk, priority, and necessity"* [[12]](#ref-12). Second, the
grooming activity was renamed **refinement** around 2011 to 2013 [[3]](#ref-3).

**The 2020 revision made it outcome-anchored.** The 2017 Guide had defined the backlog as *"an ordered
list of everything that is known to be needed in the product"* and called it the *"single, authoritative
source of work"* [[2]](#ref-2). The 2020 revision changed four things: it added **"emergent"**, replaced
*"everything that is known to be needed"* with *"what is needed to improve the product"* (a shift from
knowledge-capture to continuous improvement), dropped "authoritative", and, most importantly, introduced
the **Product Goal** as the backlog's formal commitment [[1]](#ref-1)[[3]](#ref-3). That last change was
the framework's own answer to the outcome-over-output critique (see [section 6](#6-debates-and-contested-boundaries)):
the 2017 backlog had no strategic anchor above the item list, and the 2020 backlog does.

The through-line from 1996 to 2020 is a single migration: from a **complete requirements list** you try to
finish, to an **emergent, ordered, goal-anchored queue** you never finish because the product keeps
improving.

---

## 3. Anatomy (section by section)

The template's sections are the working parts of a backlog that a real team maintains. The lean variant
carries the four that every backlog needs; the full variant adds the management apparatus that a larger or
higher-stakes backlog earns.

### Frontmatter and ownership

The document names the product, the Product Owner (accountable for content and order), the last refinement
date, and the status. **The Product Owner is the single accountable owner**; the 2020 Scrum Guide is
explicit that one person is accountable for ordering the backlog, even though refinement is teamwork
[[1]](#ref-1)[[10]](#ref-10).

*Beginner note:* put the last-refined date at the top and keep it current. A backlog nobody has refined in
a month is a backlog nobody trusts.

*Expert note:* "accountable, single owner" and "refinement is teamwork" are not in tension. The Product
Owner owns the *order*; the whole team owns *understanding and sizing* the items [[10]](#ref-10). A backlog
ordered by committee has no owner; a backlog refined only by the owner has no shared understanding.

### Product Goal

The one objective the backlog currently serves: a measurable future state of the product. The 2020 Scrum
Guide defines it as *"a future state of the product which can serve as a target for the Scrum Team to plan
against"* and requires the team to *"fulfill (or abandon) one objective before taking on the next"*
[[1]](#ref-1).

*Beginner note:* write one goal, make it measurable, and put it at the very top of the backlog. Roman
Pichler frames it as a benefit or outcome to achieve over the next two to six months [[9]](#ref-9).

*Expert note:* the Product Goal is the backlog's filter, not decoration. Pichler's rule is blunt: *"Only
add an item to the product backlog if it helps meet the product goal"* [[9]](#ref-9). This is the single
most effective guard against the feature-factory failure: an item that serves no stated goal is either
evidence the goal is wrong or evidence the item does not belong.

### Backlog Items

The ordered list itself: the work, top to bottom, most valuable and most refined at the top. Items are
**typed** in practice (user stories, bugs, technical work, spikes) even though the Scrum Guide keeps them
all generic "Product Backlog items" [[1]](#ref-1); major tools such as Jira and Azure Boards model the
typed hierarchy of epics, stories, bugs, and tasks [[30]](#ref-30)[[31]](#ref-31).

*Beginner note:* each item needs a title, a type, a short statement of the value or problem, an estimate,
and a status. The top items should be small and clear enough to pull into a sprint; lower items can be
coarse.

*Expert note:* Mike Cohn and Roman Pichler summarize a healthy backlog with the acronym **DEEP**:
**D**etailed appropriately (top items refined, bottom items coarse), **E**stimated, **E**mergent, and
**P**rioritized [[6]](#ref-6). Cohn's **iceberg** image is the mental model: the small, sprint-ready tip is
visible above the waterline, and items *"become increasingly larger and less detailed as we approach the
waterline"* [[7]](#ref-7). A backlog where every item is fully detailed is over-refined (you specified work
you may never do); one where nothing is detailed is under-refined (you cannot plan the next sprint).

### Ordering Rationale

Why the list is in the order it is in. Ordering is the Product Owner's core act, and stating the principle
makes it reviewable.

*Beginner note:* write one or two sentences on how you order, for example "risk and learning first, then
value, respecting dependencies."

*Expert note:* Pichler recommends ordering by **risk first, then cost-benefit, while respecting
dependencies** [[10]](#ref-10); ordering the riskiest work early is how a team learns soonest whether its
plan holds. The word "ordered" (not "prioritized") is the point: sequencing by a single priority score is a
special case, and a poor one when a low-value item must go first to unblock high-value work or retire a
risk. The order is a decision, not the output of a formula (see the prioritization frameworks below and in
[section 6](#6-debates-and-contested-boundaries)).

### Refinement and Readiness

How the backlog is kept refined, and what makes an item ready to pull into a sprint. The 2020 Scrum Guide
defines refinement as *"the act of breaking down and further defining Product Backlog items into smaller
more precise items ... an ongoing activity"* and sets a soft readiness bar: items that *"can be Done by the
Scrum Team within one Sprint are deemed ready for selection"* [[1]](#ref-1).

*Beginner note:* refine continuously, not in a panic before sprint planning. Cohn suggests roughly *"10
percent of the effort in each sprint"* on refinement [[7]](#ref-7); Pichler suggests updating the backlog
at least once per sprint [[8]](#ref-8).

*Expert note:* the **Definition of Ready** is a genuine fork (full variant). Pichler treats a minimal DoR
(clear, testable, feasible) as a quality gate, warning that skipping it means *"garbage in, garbage out"*
[[29]](#ref-29). Cohn warns the opposite: a rigid DoR becomes a stage-gate that can *"prevent the team from
being agile"* by blocking the concurrent refinement agile depends on [[28]](#ref-28). The 2020 Scrum Guide
deliberately defines no DoR at all. The defensible practice is a *lightweight* readiness heuristic, not a
checklist bouncer.

### Prioritization Framework *(full variant only)*

The explicit method, if any, the team uses to inform ordering: MoSCoW, WSJF, RICE, and others.

*Beginner note:* you do not need a framework to have a backlog; the Product Owner's judgment is the default.
Reach for a framework when stakeholders dispute the order or the list is too large to sequence by feel.

*Expert note:* the frameworks encode different economics, and choosing one is choosing what you optimize.
**MoSCoW** (Must, Should, Could, Won't) came from Dai Clegg in 1994 and was used extensively with DSDM from
2002; it sorts by delivery-timebox criticality, but *"does not help decide between multiple requirements
within the same priority"* [[19]](#ref-19). **WSJF** (Weighted Shortest Job First), SAFe's model, sequences
by cost of delay divided by job duration, and its lean-economics root is Reinertsen's maxim *"If you only
quantify one thing, quantify the Cost of Delay"* [[15]](#ref-15). **RICE** (Reach x Impact x Confidence /
Effort) is popular but, as the same comparison notes, ignores time sensitivity and cost of delay, so a
time-critical feature scores no higher than one with no deadline [[18]](#ref-18). The one durable rule
across all of them: *"The most dangerous thing a product team can do is adopt a single prioritization
framework and treat it as gospel"* [[18]](#ref-18).

### Dependencies and Risks *(full variant only)*

The cross-item dependencies and the risks that shape the order.

*Beginner note:* note where one item blocks another, and where a risky assumption should be retired early
by ordering a spike near the top.

*Expert note:* dependencies are a primary reason "ordered" beats "prioritized": a high-value item that
depends on a low-value one forces the low-value item up the list [[10]](#ref-10). Making dependencies
explicit is also how a backlog stays honest at scale, where SAFe manages them across ART and portfolio
backlogs [[13]](#ref-13)[[14]](#ref-14).

### Backlog Health and Metrics *(full variant only)*

The signals that the backlog is a tool and not a graveyard: its size, the age of its items, how far down
items actually get pulled from.

*Beginner note:* track two things at least: how big the backlog is, and how old the oldest items near the
top are.

*Expert note:* the backlog-bankruptcy problem is real and, at least anecdotally, measurable. Survey data
from Humanizing Work (practitioner-survey-based, not peer-reviewed, and with its method not detailed) finds
most backlogs span two to four years with fifty to seventy-five percent of items never reaching the top
[[27]](#ref-27). Their remedy is a three-zone structure (active, archive, someday-maybe) and, when it is
past saving, zero-based reconstruction; their principle is worth memorizing: *"You can always recover an
item from the archive, but you'll never recover the focus you lose if you leave it in the backlog"*
[[27]](#ref-27).

---

## 4. Variants and sizing

**Lean is the default.** It carries the Product Goal, the ordered Backlog Items list, the Ordering
Rationale, and Refinement and Readiness. That is a complete, working backlog: a goal, an ordered list, a
stated ordering principle, and a way of keeping the top of the list sprint-ready. Most teams, most of the
time, need exactly this and no more.

**Full adds the management apparatus**: an explicit Prioritization Framework, a Dependencies and Risks
section, and Backlog Health and Metrics. The shared sections keep their names and order, so lean is a
strict subset of full and a backlog can grow from one to the other in place.

The signal to scale up is **scale and contention**, not the age of the product:

- Multiple teams or stakeholders dispute the order, so an explicit framework (WSJF, RICE, MoSCoW) is worth
  the overhead of making the trade-offs legible [[15]](#ref-15)[[18]](#ref-18).
- The work has real cross-team dependencies that the order must respect [[10]](#ref-10).
- The backlog is large enough that its health (size, age, pull-through) needs measuring to avoid
  bankruptcy [[27]](#ref-27).

Otherwise, lean. A small team with one clear goal that reaches for WSJF and a metrics dashboard has built
a bureaucracy around a list it could order by conversation.

---

## 5. Methodology lineage

The backlog is a **general agile concept that Scrum named and formalized**; the traditions treat it
differently, and the differences are instructive.

| Tradition | Form of the backlog | What it optimizes for |
|---|---|---|
| **Scrum** | One ordered, emergent Product Backlog, owned by the Product Owner, anchored to a Product Goal | A single source of work with a clear owner and a strategic anchor [[1]](#ref-1) |
| **XP** | Story cards prioritized by the customer in the Planning Game | Customer-driven value ordering, re-prioritized each iteration [[17]](#ref-17) |
| **Kanban Method** | No "backlog"; uncommitted work is "options" upstream of a commitment point | Deferring commitment and limiting work in progress, not accumulating a list [[16]](#ref-16) |
| **SAFe** | Multiple named backlogs (Team, ART, Portfolio), each a Kanban system, prioritized by WSJF | Coordinating flow and economics across many teams [[13]](#ref-13)[[15]](#ref-15) |
| **Continuous discovery** | An opportunity backlog of problems, feeding a delivery backlog of solutions | Keeping the list rooted in validated customer opportunities [[22]](#ref-22)[[23]](#ref-23) |

**Why this bundle teaches the Scrum-style goal-anchored backlog:** it is the canonical, most widely used
form, and its Product Goal commitment is the very thing that answers the strongest critique of backlogs.
The variants are covered in [section 9](#9-adaptations). Two are worth flagging here. **Kanban genuinely
rejects the artifact**: the Kanban Method calls uncommitted work "options," not a backlog, and holds that
*"in pull systems, completed work is regarded as more valuable than starting new work"* [[16]](#ref-16);
this bundle reads that as a caution that a standing list invites a team to treat the whole thing as
committed work. And **SAFe scales the backlog** into a hierarchy of Kanban systems prioritized economically
by WSJF [[13]](#ref-13)[[15]](#ref-15). Neither is wrong; they optimize for different constraints, and a
team should know which constraint it actually has.

---

## 6. Debates and contested boundaries

### 6.1 Outcome over output (the live one)

**Camp A, the backlog is a feature factory.** Marty Cagan's critique is the sharpest: a "feature team"
receives a prioritized feature list from stakeholders and the product manager's role collapses into
*"backlog administrator"* whose work is *"all about delivering output"* [[20]](#ref-20). His prescription
is to replace feature roadmaps with outcome objectives [[21]](#ref-21) and to run an **opportunity
backlog** of problems to solve rather than solutions to build, a concept he credits to Jeff Patton
[[22]](#ref-22). Jeff Gothelf supplies the vocabulary: an outcome is *"a measurable change in human
behavior we see when we give the output to our users and customers"*, not a feature shipped
[[26]](#ref-26).

**Camp B, the backlog endures but must be anchored.** Teresa Torres inserts an **Opportunity Solution
Tree** between the business outcome and the backlog, so solutions trace to validated customer
opportunities; the tree is *"a living document that should evolve as you learn"* and it shapes the backlog
rather than replacing it [[23]](#ref-23). Roman Pichler holds that roadmap and backlog coexist and that the
fix is to derive the backlog from outcome-based goals: *"clearly distinguish between a product goal and a
feature. The former describes a benefit or outcome you want to achieve; the latter captures the output"*
[[11]](#ref-11).

*This bundle's reading:* the evolution camp is winning inside the Scrum ecosystem, and the 2020 Product
Goal is the institutional proof: the framework added exactly the outcome anchor the 2017 backlog lacked
[[1]](#ref-1)[[3]](#ref-3). The template's answer is Camp B operationalized: a required Product Goal at the
top, an ordering rationale that can favor learning over raw value, and (in the guide) the anti-pattern of a
goal-less backlog. The backlog is not dead; the *unanchored* backlog is.

### 6.2 Ordered, not prioritized

The 2020 Scrum Guide's shift from "prioritized" to "ordered" [[3]](#ref-3) is treated by one camp as a
genuine improvement (ordering lets dependencies, risk, and learning override a single priority score) and
by another as a branding change (teams still rank most-to-least important). No primary source adjudicates
it. This bundle sides with "ordered" as the more honest word, because dependencies and risk-first
sequencing routinely produce an order that a pure value ranking would not [[10]](#ref-10), but it keeps
"prioritize" in the guide where readers expect it, since the practitioner literature (Pichler, DEEP) still
uses it [[6]](#ref-6)[[8]](#ref-8).

### 6.3 No-estimates versus story points

Ron Jeffries, a possible inventor of story points, now regrets them: *"I like to say that I may have
invented story points, and if I did, I'm sorry now"* [[24]](#ref-24), and he argues that comparing teams on
velocity is harmful and that story-slicing makes estimates unnecessary. The defenders' camp (Cohn,
SAFe/Leffingwell) holds that relative estimation and velocity remain practical planning tools; this bundle
did not fetch that camp's primary statement and so presents Jeffries's position as one camp, not the
settled view. The template stays neutral: it carries an estimate column but does not mandate story points,
and the guide names estimation *misuse* (velocity as a target) as the anti-pattern, not estimation itself.

### 6.4 Does a backlog belong at all

Jeffries goes further than the estimate debate to the artifact itself: *"If you're working from a backlog,
it's too easy to think that you have to do it all"*, which turns a product into a fixed-scope project and
crowds out creative problem-solving [[25]](#ref-25). The Kanban Method's "options, not backlog" position is
the same objection from a different tradition [[16]](#ref-16). This bundle takes the objection seriously:
its countermeasures are the Product Goal (the backlog serves a goal, not a scope to complete) and the
backlog-health section (delete aggressively; a bloated backlog is the failure Jeffries describes)
[[27]](#ref-27).

---

## 7. Anti-patterns and failure modes

1. **The feature factory.** A backlog of pre-decided features with no Product Goal above it, so the team
   ships output that moves no outcome [[20]](#ref-20)[[26]](#ref-26). The countermeasure is a required,
   measurable goal and Pichler's filter: an item that does not serve the goal does not belong
   [[9]](#ref-9).
2. **Backlog bankruptcy.** A backlog that only grows, spanning years, with most items never pulled
   [[27]](#ref-27). Delete aggressively; archive is recoverable, lost focus is not.
3. **Must-have inflation.** Under MoSCoW, everything becomes a "Must," which defeats the framework because
   it *"does not help decide between multiple requirements within the same priority"* [[19]](#ref-19).
4. **The rigid Definition of Ready.** A readiness checklist enforced as a stage-gate, reintroducing the
   phase-gate bureaucracy agile removed [[28]](#ref-28). Keep readiness a lightweight heuristic.
5. **Velocity as a target.** Using story points to compare teams or push speed, which Jeffries names as
   harmful: *"comparing teams on quality of estimates or velocity is harmful"* [[24]](#ref-24).
6. **The over-refined backlog.** Detailing items at the bottom you may never build, violating the iceberg
   and wasting refinement effort on work that will change or be dropped [[7]](#ref-7).
7. **Ordering by loudest stakeholder.** Letting the order be set by whoever pushes hardest rather than by a
   stated principle, which is the "backlog administrator" failure in miniature [[20]](#ref-20).

---

## 8. Relationships to other artifacts

The backlog sits at the tactical center of the delivery chain, so its boundaries with its neighbours are
where teams most often get confused.

- **Feeds it:** the **product vision** and **product roadmap** (strategic; the roadmap's next goal scopes
  the backlog [[11]](#ref-11)[[32]](#ref-32)); **product discovery** (validated opportunities
  [[23]](#ref-23)); the **[PRD](../prd/prd_companion.md)** (a concrete source of items); and stakeholder
  requests, production bugs, and tech-debt decisions. The directional flow is vision to roadmap to backlog:
  strategy above, execution below [[32]](#ref-32).
- **Contains:** typed items, most importantly **[user stories](../user-stories/user-stories_companion.md)**
  and the epics that group them, plus bugs, technical work, and spikes [[30]](#ref-30)[[31]](#ref-31).
  Each story carries its **[acceptance criteria](../acceptance-criteria/acceptance-criteria_companion.md)**.
- **Anchored by:** the **Product Goal**, its formal Scrum commitment, which sits at the top and filters
  what may enter [[1]](#ref-1)[[9]](#ref-9).
- **Feeds:** the **sprint backlog**, a time-boxed subset the developers select each sprint; the Scrum Guide
  is explicit that the Sprint Backlog is *"composed of ... the set of Product Backlog items selected for
  the Sprint"* [[1]](#ref-1). Completed items eventually surface in the
  **[release note](../release-notes/release-notes_companion.md)**.
- **The backlog-versus-roadmap line, which matters most:** the roadmap is **strategic and outcome-focused**
  (where the product is going and why), the backlog is **tactical and output-focused** (the ordered work to
  get there). Pichler draws the line at goal versus feature [[11]](#ref-11); the failure is a roadmap that
  is secretly a feature list, which is the feature factory again [[20]](#ref-20).

---

## 9. Adaptations

- **Small teams and solo work.** The lean variant, or a single ordered list with a goal at the top. The
  Product Owner orders by conversation; no framework or metrics dashboard is warranted until the list is
  too big or too contested to order by feel.
- **Scrum teams.** The lean variant is the Scrum-canonical backlog: one Product Goal, one ordered list,
  continuous refinement, and a soft readiness bar [[1]](#ref-1). Resist a heavy Definition of Ready
  [[28]](#ref-28).
- **Kanban teams.** Consider whether you need a backlog at all. The Kanban Method manages uncommitted work
  as "options" upstream of a commitment point, with replenishment policies rather than a standing ordered
  list [[16]](#ref-16). A hybrid (Scrumban) keeps a light backlog feeding a pull board; a pure Kanban team
  may not keep one.
- **Scaled organizations (SAFe or similar).** Expect a hierarchy of backlogs (team, ART, portfolio), each a
  Kanban system, prioritized economically by WSJF, with dependencies managed explicitly across levels
  [[13]](#ref-13)[[14]](#ref-14)[[15]](#ref-15). Use the full variant and treat the Dependencies and
  Prioritization Framework sections as mandatory.
- **Discovery-led product teams.** Run an **opportunity backlog** of problems above the delivery backlog,
  and let discovery (an Opportunity Solution Tree, customer interviews) decide what becomes a delivery item
  [[22]](#ref-22)[[23]](#ref-23). The delivery backlog then contains validated bets, not a stakeholder wish
  list.

---

## 10. Worked example

[`product-backlog_example.md`](product-backlog_example.md) is a full-variant product backlog for the same
fictional **"Saved Views for Dashboards"** feature the `delivery-docs` family's other examples chain on
(its [PRD](../prd/prd_example.md), user stories, acceptance criteria, and release note). It shows a real
Product Goal (tied to the PRD's time-to-insight objective), an ordered list mixing the Saved Views epic and
its stories with unrelated product work, bugs, tech debt, and a spike, an explicit ordering rationale
(dependency and risk first), and a lightweight readiness note. It demonstrates the backlog as the tactical
center of the family: the PRD says what Saved Views is and why, the user stories decompose it, and the
product backlog is where that work sits ordered among everything else the product might do.

---

## References

Tagged by reliability: `[primary]` standards body, regulator, or originating source; `[practitioner]`
recognized independent authority or canonical writing; `[vendor]` commercially motivated, reliable on
convention; `[reference]` consolidated secondary (an encyclopedia or aggregator). Researched 2026-07-21;
per-source retrieval status is recorded in
[`product-backlog_research-log.md`](product-backlog_research-log.md). Only sources fetched and verified are
quoted. Each source has its own entry (no combined entries), and each displayed number equals its anchor.

<a id="ref-1"></a>[1] Schwaber, Ken and Sutherland, Jeff. "[The 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html)." scrumguides.org (accessed 2026-07-21). Supports the canonical definition of the Product Backlog ("an emergent, ordered list of what is needed to improve the product"; "the single source of work undertaken by the Scrum Team"), the Product Goal as its commitment, the Product Owner's accountability for ordering, refinement as an ongoing activity, developers' responsibility for sizing, the sprint-readiness condition, and the Sprint Backlog composed from selected Product Backlog items. [primary]

<a id="ref-2"></a>[2] Schwaber, Ken and Sutherland, Jeff. "[The 2017 Scrum Guide](https://scrumguides.org/docs/scrumguide/v2017/2017-Scrum-Guide-US.pdf)." scrumguides.org (accessed 2026-07-21). Supports the pre-2020 wording ("an ordered list of everything that is known to be needed in the product"; "the single, authoritative source of work"), before the 2020 revision added "emergent" and the Product Goal. [primary]

<a id="ref-3"></a>[3] Schwaber, Ken and Sutherland, Jeff. "[Scrum Guide Revision History](https://scrumguides.org/revisions.html)." scrumguides.org (accessed 2026-07-21). Supports the official changelog: the 2011 shift from "prioritized" to "ordered", the rename of grooming to refinement, and the 2020 introduction of the Product Goal commitment. [primary]

<a id="ref-4"></a>[4] Schwaber, Ken. "[SCRUM Development Process (Controlled Chaos: Living on the Edge)](https://jeffsutherland.com/oopsla96/schwaber.html)." OOPSLA 1996, hosted at jeffsutherland.com (accessed 2026-07-21). Supports the earliest retrievable formal definition of the backlog concept, which used the term "Backlog" and framed it as a requirements list ("an identification of all requirements that should be fulfilled in the completed product"). [primary]

<a id="ref-5"></a>[5] ScrumDesk. "[The History of Scrum: How, When and Why](https://www.scrumdesk.com/the-history-of-scrum-how-when-and-why/)." scrumdesk.com (accessed 2026-07-21). Supports the historical timeline: the first Scrum team at Easel Corporation in 1994, the OOPSLA 1995 presentation, and the lineage to Takeuchi and Nonaka's 1986 "The New New Product Development Game". Secondary practitioner account; dates not traced to primary documents. [reference]

<a id="ref-6"></a>[6] Cohn, Mike. "[Make the Product Backlog DEEP](https://www.mountaingoatsoftware.com/blog/make-the-product-backlog-deep)." Mountain Goat Software (accessed 2026-07-21). Supports the DEEP acronym (Detailed appropriately, Estimated, Emergent, Prioritized), co-credited to Mike Cohn and Roman Pichler, and its four characteristics. The detailed treatment is in Cohn's book *Succeeding with Agile*; sole authorship of DEEP is not settled by a single source. [practitioner]

<a id="ref-7"></a>[7] Cohn, Mike. "[Why Your Product Backlog Should Look Like an Iceberg](https://www.mountaingoatsoftware.com/blog/why-your-product-backlog-should-look-like-an-iceberg)." Mountain Goat Software (accessed 2026-07-21). Supports the iceberg model (sprint-ready items at the top, coarser items below the waterline) and the guideline of roughly ten percent of each sprint's effort spent on refinement. [practitioner]

<a id="ref-8"></a>[8] Pichler, Roman. "[Product Backlog FAQs](https://www.romanpichler.com/blog/product-backlog-faqs/)." romanpichler.com (accessed 2026-07-21). Supports the backlog as a prioritised list of work, its contents, and a refinement cadence of at least once per sprint. Pichler uses "prioritised" where the 2020 Scrum Guide uses "ordered". [practitioner]

<a id="ref-9"></a>[9] Pichler, Roman. "[Product Goals in Scrum](https://www.romanpichler.com/blog/product-goals-in-scrum/)." romanpichler.com (accessed 2026-07-21). Supports the product goal as a time-bounded, measurable outcome that filters backlog items ("Only add an item to the product backlog if it helps meet the product goal") and a two-to-six-month timeframe (Pichler's own guidance, not the Scrum Guide's). [practitioner]

<a id="ref-10"></a>[10] Pichler, Roman. "[Seven Product Backlog Mistakes to Avoid](https://www.romanpichler.com/blog/product-backlog-mistakes/)." romanpichler.com (accessed 2026-07-21). Supports refinement as teamwork, ordering by risk first then cost-benefit while respecting dependencies, and the goal as scope-setter ("The product backlog should contain only the items that help you reach the product goal"). The Product Owner is the single accountable owner of the order while refinement is teamwork. [practitioner]

<a id="ref-11"></a>[11] Pichler, Roman. "[The Product Roadmap and the Product Backlog](https://www.romanpichler.com/blog/product-roadmap-product-backlog/)." romanpichler.com (accessed 2026-07-21). Supports the roadmap-versus-backlog distinction (goal/outcome versus feature/output) and deriving the backlog from the next roadmap goal ("clearly distinguish between a product goal and a feature. The former describes a benefit or outcome you want to achieve; the latter captures the output"). [practitioner]

<a id="ref-12"></a>[12] Agile Angel. "[The Scrum Guide Version History - 2010 to 2016](https://agileangelblog.wordpress.com/2016/10/15/the-scrum-guide-version-history-2010-to-2016/)." agileangelblog.wordpress.com, 2016-10-15 (accessed 2026-07-21). Corroborates the 2011 "prioritized" to "ordered" change and carries the 2011 Guide's wording verbatim ("The Product Backlog is often ordered by value, risk, priority, and necessity"). Independent practitioner analysis; coverage ends 2016. [practitioner]

<a id="ref-13"></a>[13] Scaled Agile, Inc. "[SAFe Glossary](https://framework.scaledagile.com/glossary)." framework.scaledagile.com (accessed 2026-07-21). Supports the SAFe ART Backlog as a Kanban system for features and enablers ("The ART Backlog is a Kanban system that is used to capture and manage the features and enablers"), the Feature definition, and WSJF as SAFe's prioritization model. [primary]

<a id="ref-14"></a>[14] Scaled Agile, Inc. "[Portfolio Backlog](https://framework.scaledagile.com/portfolio-backlog/)." framework.scaledagile.com (accessed 2026-07-21). Supports the Portfolio Backlog as a Kanban system for business and enabler epics, managed by Portfolio Leadership ("The Portfolio Backlog is a Kanban system that is used to capture and manage the business and enabler epics"). [primary]

<a id="ref-15"></a>[15] Scaled Agile, Inc. "[WSJF (Weighted Shortest Job First)](https://framework.scaledagile.com/wsjf/)." framework.scaledagile.com (accessed 2026-07-21; public portions, full detail behind a login). Supports the WSJF model (cost of delay divided by job duration) and its lean-economics rationale ("If you only quantify one thing, quantify the Cost of Delay"). [primary]

<a id="ref-16"></a>[16] Kanban University. "[The Official Guide to The Kanban Method](https://kanban.university/kanban-guide/)." kanban.university (accessed 2026-07-21). Supports Kanban's treatment of uncommitted work as "options" rather than a backlog, the commitment point, WIP limits, and the pull principle ("In pull systems, completed work is regarded as more valuable than starting new work"). [primary]

<a id="ref-17"></a>[17] InfoQ. "[eXtreme Programming The Methodology](https://www.infoq.com/articles/implementing-xp-methodology/)." infoq.com (accessed 2026-07-21). Supports XP's customer-driven prioritization by business value through the Planning Game. A practitioner article, not the canonical XP source (Kent Beck's *Extreme Programming Explained*, not fetched). [practitioner]

<a id="ref-18"></a>[18] Fygurs. "[Product Prioritization Frameworks Compared: RICE vs WSJF vs ICE vs MoSCoW](https://www.fygurs.com/blog/product-prioritization-frameworks-compared)." fygurs.com (accessed 2026-07-21). Supports the RICE formula and its blind spot on time sensitivity and cost of delay, and the caution against treating any single framework as gospel ("The most dangerous thing a product team can do is adopt a single prioritization framework and treat it as gospel"). [vendor]

<a id="ref-19"></a>[19] Wikipedia. "[MoSCoW method](https://en.wikipedia.org/wiki/MoSCoW_method)." en.wikipedia.org (accessed 2026-07-21). Supports the MoSCoW origin (Dai Clegg, 1994, RAD; used extensively with DSDM from 2002), the four category definitions, and the limitation that it cannot rank within a category ("Does not help decide between multiple requirements within the same priority"). [reference]

<a id="ref-20"></a>[20] Cagan, Marty. "[Product vs Feature Teams](https://www.svpg.com/product-vs-feature-teams/)." Silicon Valley Product Group (accessed 2026-07-21). Supports the critique that feature teams receive a prioritized feature list and the product-manager role collapses into "backlog administrator" delivering output ("this is all about delivering output"). [practitioner]

<a id="ref-21"></a>[21] Cagan, Marty. "[Roadmap Alternative FAQ](https://www.svpg.com/roadmap-alternative-faq/)." Silicon Valley Product Group (accessed 2026-07-21). Supports replacing feature roadmaps with outcome objectives, shifting "from specific features launching on specific dates, to business results". [practitioner]

<a id="ref-22"></a>[22] Cagan, Marty. "[The Opportunity Backlog](https://www.svpg.com/the-opportunity-backlog/)." Silicon Valley Product Group (accessed 2026-07-21). Supports the opportunity backlog as a list of problems and customer needs rather than pre-decided solutions, with discovery producing the delivery backlog; credits Jeff Patton as the concept's pioneer. [practitioner]

<a id="ref-23"></a>[23] Torres, Teresa. "[Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/)." Product Talk (accessed 2026-07-21). Supports the Opportunity Solution Tree as a discovery framework that inserts a validated-opportunity layer between outcome and solution, shaping the backlog rather than replacing it ("a living document that should evolve as you learn"). Formalized in Torres's 2021 book *Continuous Discovery Habits*. [practitioner]

<a id="ref-24"></a>[24] Jeffries, Ron. "[Story Points Revisited](https://ronjeffries.com/articles/019-01ff/story-points/Index.html)." ronjeffries.com (accessed 2026-07-21). Supports the NoEstimates critique of story points from a possible inventor ("I like to say that I may have invented story points, and if I did, I'm sorry now"; "comparing teams on quality of estimates or velocity is harmful"). Jeffries's regret targets misuse; the defenders' camp was not fetched. [practitioner]

<a id="ref-25"></a>[25] Jeffries, Ron. "[The Backlog](https://ronjeffries.com/articles/015-10/the-backlog/article.html)." ronjeffries.com (accessed 2026-07-21). Supports the radical critique that a comprehensive ordered backlog turns a product into a fixed-scope project and suppresses creative problem-solving ("If you're working from a backlog, it's too easy to think that you have to do it all"). [practitioner]

<a id="ref-26"></a>[26] Gothelf, Jeff. "[Output, Outcomes, Impact and KPIs](https://jeffgothelf.com/blog/output-outcomes-impact-and-kpis/)." jeffgothelf.com (accessed 2026-07-21). Supports the output/outcome/impact vocabulary and the definition of an outcome as measurable behavior change ("Outcome is a measurable change in human behavior we see when we give the output to our users and customers"). [practitioner]

<a id="ref-27"></a>[27] Lawrence, Richard and Green, Peter. "[The Life-Changing Focus of a Clean Backlog](https://www.humanizingwork.com/life-changing-focus-clean-backlog/)." Humanizing Work (accessed 2026-07-21). Supports the backlog-bankruptcy problem (most backlogs span two to four years with fifty to seventy-five percent of items never reaching the top) and the three-zone remedy ("you'll never recover the focus you lose if you leave it in the backlog"). The figures are practitioner-survey-based, not peer-reviewed, and the survey method is not detailed. [practitioner]

<a id="ref-28"></a>[28] Cohn, Mike. "[The Dangers of a Definition of Ready](https://www.mountaingoatsoftware.com/blog/the-dangers-of-a-definition-of-ready)." Mountain Goat Software (accessed 2026-07-21). Supports the Definition of Ready as a backlog-to-sprint gate and the caution that a rigid DoR reintroduces stage-gate behavior that can "prevent the team from being agile". [practitioner]

<a id="ref-29"></a>[29] Pichler, Roman. "[The Definition of Ready](https://www.romanpichler.com/blog/the-definition-of-ready/)." romanpichler.com (accessed 2026-07-21). Supports a minimal three-criteria readiness (clear, testable, feasible) and the "garbage in, garbage out" consequence of skipping it. [practitioner]

<a id="ref-30"></a>[30] Microsoft. "[Use backlogs to manage projects (Azure Boards)](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/backlogs-overview?view=azure-devops)." Microsoft Learn (accessed 2026-07-21). Supports the typed Epic > Feature > Product Backlog Item hierarchy and the backlog as "the prioritized list of work that drives every sprint". [vendor]

<a id="ref-31"></a>[31] Atlassian. "[Enable the backlog (Jira Software Cloud)](https://support.atlassian.com/jira-software-cloud/docs/enable-the-backlog/)." Atlassian Support (accessed 2026-07-21). Supports Jira's backlog as a space for defining and prioritizing work, with typed items and epics as containers ("Epics represent a group of smaller, related tasks, bugs and user stories"). [vendor]

<a id="ref-32"></a>[32] ProductPlan. "[Product Roadmap vs. Product Backlog](https://www.productplan.com/learn/product-roadmap-vs-product-backlog/)." productplan.com (accessed 2026-07-21). Supports the directional flow from vision to roadmap to backlog and the backlog as the task-level execution of roadmap strategy. [vendor]
