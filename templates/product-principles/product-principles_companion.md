# Companion: Product Principles

> The deep explainer for the product-principles bundle. Read this to understand what a product
> principles document is, where Marty Cagan places it, what published sets put in each principle, and
> where practitioners disagree about authorship, ranking, the truism test and the right number. The
> short operator card is [`product-principles_guide.md`](product-principles_guide.md); a fully worked
> instance is [`product-principles_example.md`](product-principles_example.md). Inline citations like
> [[1]](#ref-1) resolve to the [References](#references) at the bottom, numbered exactly as the
> research log numbers them. The full retrieval trail, including the pages this bundle could not
> read, is [`product-principles_research-log.md`](product-principles_research-log.md).
> This bundle sits in the `standing-standards` family as a **foundation**: a standard that a team's
> product decisions are judged against, not an instrument executed under time pressure, per
> [ADR 0090 (product principles joins standing-standards as a foundation)](../../docs/internal/decisions/0090-product-principles-joins-standing-standards-as-a-foundation.md).

---

## 1. Orientation and TL;DR

A product principles document is a short, standing set of beliefs that a product team agrees once and
then uses to settle product trade-offs. Marty Cagan's 2020 book defines the type this way: "Product
principles complement the product vision by stating the values and beliefs that are intended to inform
the many product decisions that will need to be made." [[40]](#ref-40) His coaching article lists
principles as one of six kinds of strategic context, and says that context "is meant to apply to all
product teams in the company" [[2]](#ref-2). The library's own reading goes past that sentence: it
takes the set to settle what the team builds and what it refuses. Slack limits a set to execution
[[25]](#ref-25), so section 6 holds that reading at medium-low confidence.

The job in one sentence: a short standing set that tells the people who decide what the product
does which way their decisions should lean when two good options compete, and who reopens the set
when conditions change.

**At a glance**

- **It is a standing set, not a feature list and not a release plan.** Cagan writes "Product
  principles are not a list of features, and they are not tied to any one product release." [[39]](#ref-39)
  ProductPlan adds "You don’t build principles, they guide what you decide to build and how to build
  it." [[22]](#ref-22)
- **A principle that no reasonable team would reverse is a truism.** Intercom's test is "The opposite
  of a principle should itself be a principle" [[7]](#ref-7). AWS, writing about tenets, states a
  matching test [[38]](#ref-38), and a vendor's AI prompt says a principle with no reasonable
  opposite is not one [[4]](#ref-4). One vendor dissents, and section 6 says how.
- **The strongest finding is negative.** Across the eight published sets this research tabulated, none
  carries a field for what a principle rules out. Among the sets and prompts in the structure table, only a
  vendor's AI prompt [[4]](#ref-4) does. A single list in one company's handbook [[15]](#ref-15) and
  Box's per-principle "Versus", known only through Pendo's report [[36]](#ref-36), come close, and neither
  is in that table. The template asks for the field, and it says it is asking for more than published
  sets do.
- **It is not a design principles document.** The sources split the two by scope [[22]](#ref-22),
  [[23]](#ref-23), [[32]](#ref-32). The library's own test for the line is in section 8.
- **Every count and every revision interval is a heuristic.** Sources say three to five, up to seven,
  or fourteen in layers, and a review every three months or every one to two years. None cites a
  measurement.

If you read nothing else: write principles that a reasonable team could reverse, and say what each
one rules out and what it costs. The rest of the template is structure around that test.

**Confidence.** High on the quoted definition and the two exclusions, which Cagan and ProductPlan state
in their own words. Medium-low on the library's reading that the set settles what to build and what to
refuse. High on the negative finding about a rules-out field, which is a statement about the
eight sets read. Medium on the section design, because no source other than a vendor's AI prompt
publishes a template, so most of the structure is the library's own position. Low on any claim about
how many principles are right or how often a set changes, because the sources disagree and none
measures.

## 2. Origins and evolution

**No source read names who first wrote about a team writing its own product principles.** This
companion therefore names no originator and draws no lineage from one.

**The earliest source read is Cagan's PRD guide** [[1]](#ref-1). It carries a "Step 4: Define your
Product Principles" as one of ten steps in producing a product requirements document. Its only date is
a 2005 copyright footer on every page, and the PDF now sits under a 2024 upload path, so the date
rests on the footer alone. The guide already reports earlier sets: a TiVo list, and eBay's, where "at
eBay the mantra was: 1) easy to use; 2) safe; and 3) fun." [[1]](#ref-1) The log reads that as
evidence that the practice predates the guide. That is an inference from the examples, not a dated
fact.

**Cagan's texts frame the scope of a set in three ways, in date order**, each tied to a source.

| Year | Scope of a set | Author | Source |
|---|---|---|---|
| 2005 | One project: "These principles will be specific to your domain and your particular project." | The team | [[1]](#ref-1) |
| 2017 | A product line: "The principles are aligned with the product vision for an entire product line." | Not stated | [[39]](#ref-39) |
| 2020 | The strategic context for every team: "As the product leaders create the product vision, I encourage them to also prepare a set of product principles to complement the vision" | Product leaders | [[40]](#ref-40), [[2]](#ref-2) |

Read in order, the texts run from a step in writing one PRD to a standing artifact that sits beside the
vision and the strategy. That order is not a record of Cagan changing his mind. The 2005 text is a PRD
guide, so its project scope may reflect its genre, its only date is a copyright footer, and the research
read nothing of his between 2005 and 2017. The 2017 chapter says "I always like to complement the product vision and product strategy
with a set of product principles." [[39]](#ref-39) It also allows a set to stay internal: "In many
cases, the principles are simply a tool for the product teams." [[39]](#ref-39) Its worked example is
eBay's rule for buyers and sellers, which opens "In cases where the needs of the buyers and the
sellers conflict" [[39]](#ref-39).

**A caution about Cagan's 2017 article.** His article titled "Principles" [[3]](#ref-3) is about
principles of product management in general, and it explains why the second edition of *Inspired* is
organised around them. It is not about this document, and this companion does not cite it for the
type. It is listed only so a reader who finds it does not mistake it for a source.

**Practice moved too, and Intercom gives the one dated record.** Intercom's 2019 podcast says "we have
three high level principles today, we used to have five and then we merged three of them into one"
[[16]](#ref-16). By October 2021 the set had four top-level principles, five for product design and
five for engineering [[7]](#ref-7). In 2022 Emmet Connolly wrote that the R&D set "is the third major
iteration since we first introduced them about eight years ago" [[8]](#ref-8). Slack's set also
differs between two snapshots, and section 3 reports how far that comparison can be pushed.

**What the research did not find.** The log records nothing on what the product principles
document replaced or on how its form changed, and it records no founding text for the type. The
next section therefore reports sets and arguments rather than a lineage.

**Time-bound items.** GitLab's handbook page was last modified on 30 October 2026 [[5]](#ref-5).
Productboard's prompt carries a 2026 copyright footer [[4]](#ref-4). Product School's article is dated
August 2025 [[24]](#ref-24). Slack's published set changed between the two snapshots read
[[18]](#ref-18), [[10]](#ref-10). Intercom's set had changed by 2019, when it said it had merged five top-level principles into three, and
had changed again by 2021 [[16]](#ref-16), [[7]](#ref-7). Re-read any of these before relying on it as current.

## 3. Anatomy (section by section)

The template has six sections, in one size. **No source publishes a template for a product principles
document, other than a vendor's AI prompt** [[4]](#ref-4), so every section was assembled from
published sets and method articles. Most of the structure is therefore the library's own position,
and each subsection says which parts a source supports. The structure table below is the evidence the
sections rest on.

| Set | Count | What each principle carries |
|---|---|---|
| GitLab [[5]](#ref-5) | 8 | A clause that is both name and statement, then reasoning. Three use an "over" form, such as "We value quality over velocity:" |
| Monzo [[6]](#ref-6) | 6, for one internal product | A name and a reasoning paragraph. Two carry a case study of a decision the principle settled |
| Intercom [[7]](#ref-7) | 14, in layers of 4, 5 and 5 | A numbered name and one to three sentences |
| Linear [[9]](#ref-9) | 7 | A name and one to three sentences. Some names carry the trade-off, such as "Simple first, then powerful" |
| Slack, via Salesforce [[10]](#ref-10) | 5 | A name, "What it means:" and "How it shows up:", with a product example |
| Supabase [[11]](#ref-11) | 7 | A name and one to three sentences, some with a litmus test or a stated sacrifice |
| PostHog [[12]](#ref-12) | 3 | One line each, such as "Get in first." |
| David Pereira [[14]](#ref-14) | 12, in four layers of three | A name and one sentence |
| Productboard's prompt [[4]](#ref-4) | 5, prescribed | A name, a statement, what it means in practice, what it means the team will not do, and a tension line |

Productboard's row is a vendor's AI prompt, not a published set. It reserves its rights, so this
companion describes its fields and copies no more than field names and a few short quoted phrases
[[4]](#ref-4). The Slack row rests on a Salesforce marketing article dated 24 March 2026 whose URL and
context lean toward design [[10]](#ref-10), so the Slack change comparison below rests on a
design-adjacent snapshot. Sections 2 and 3 of the template carry the weight, and section 6 carries the
family's obligation.

### Purpose and Scope

**What it is.** The product or products the set covers, the level at which it applies (company,
product line or product), how it relates to the product vision, the product strategy and the design
principles, and any principle that straddles the line with design principles. It is short.

**Why it exists.** A set with no stated scope leaves a new product with no way to know whether the
set covers it. Sources place sets at different levels. Cagan's 2017 chapter says a set is aligned "with
the product vision for an entire product line" [[39]](#ref-39), and his 2020 article says the strategic
context "is meant to apply to all product teams in the company" [[2]](#ref-2). Slack says "Product
principles should be company-wide, not siloed into the product or design team." [[25]](#ref-25) Intercom
layers its set into R&D, product design and engineering levels that every contributor inherits
[[7]](#ref-7), and Tig Kindel describes tenets at the company, organisation, team and project levels
[[37]](#ref-37). Kindel also names two kinds of tenet, foundational and aspirational [[37]](#ref-37).
Stating the level is the library's field and its position, assembled from sources that each place a
set at one level.

**What the set covers is itself disputed.** ProductPlan says principles "guide what you decide to build
and how to build it" [[22]](#ref-22), and Cagan ties them to "the many product decisions" a team makes
[[40]](#ref-40). Slack scopes them more narrowly: "Product principles exist to inform execution rather
than roadmapping, strategic thinking or planning." [[25]](#ref-25) The template's definition follows
Cagan and ProductPlan, which is the library's reading. An author who wants Slack's limit can state it
in this section.

**The line with design principles is first drawn here.** ProductPlan says "They also aren’t design
principles" [[22]](#ref-22), and section 8 gives the library's test for the line and its confidence. Linear
keeps its seven principles separate from thirteen practices [[9]](#ref-9). The research did not
examine what the practices contain, so it draws nothing further from the split.

**Beginner note.** Name the product or products, say whether the set is company-wide, per product line
or per product. One sentence for each is enough. Then
apply the test in section 8 to each principle before you write the straddling line.

**Expert note.** The scope statement is also what tells you when to reopen the set, because a new
product that falls inside the scope is a reason to ask whether the set still fits. If the scope
drifts toward how a screen behaves, the document has strayed into the sibling bundle's territory.

### The Principles

**What it is.** The set itself: three to five principles, each with five fields. A name and a
statement open each principle. The other four fields are why we hold it, the trade-off it accepts,
what it rules out, and a decision it settled. This is the document. The rest of the template exists to
keep these fields honest.

**Why it exists.** The definition makes principles the thing that informs product decisions
[[40]](#ref-40), so each one has to be specific enough to inform one. Productboard's prompt makes the
same demand, in the words "specific enough that they could be used to resolve an argument"
[[4]](#ref-4). The table states what the research found for each field, and where a field has no
support.

| Field | What it holds | What the research found |
|---|---|---|
| **Statement** | The principle's name and one to three sentences | Every set in the structure table carries a name and a statement [[5]](#ref-5), [[6]](#ref-6), [[7]](#ref-7), [[9]](#ref-9), [[10]](#ref-10), [[11]](#ref-11), [[12]](#ref-12), [[14]](#ref-14) |
| **Why we hold it** | The reasoning that makes the statement defensible | Cagan: "The product team needs to understand these principles and the reasoning behind each one." [[40]](#ref-40) GitLab gives an explanation paragraph after each principle [[5]](#ref-5), and Monzo gives a reasoning paragraph [[6]](#ref-6). Slack's set carries a "What it means:" field [[10]](#ref-10). PostHog gives one line and no reasoning [[12]](#ref-12) |
| **The trade-off it accepts** | What the principle costs, written into the principle | GitLab writes three of eight as "X over Y" [[5]](#ref-5). Linear names the sequence in "Simple first, then powerful" [[9]](#ref-9). Microsoft's patterns and practices team wrote "Quality over scope" [[35]](#ref-35). Box published a "Versus" and a named cost with each principle, such as "The tradeoff? Expense." [[36]](#ref-36). Supabase's pages add a stated sacrifice to some principles [[11]](#ref-11). Nir Gazit's rule is "Take a stand by preferring one alternative over the other(s)." [[26]](#ref-26). Productboard's prompt has a field headed "TENSION" [[4]](#ref-4) |
| **What it rules out** | The choice a team can no longer make once it holds the principle | Productboard's prompt has a field headed "WHAT IT MEANS WE WON'T DO" [[4]](#ref-4). Langfuse's handbook has a list headed "What we don't do", as one list for the whole set [[15]](#ref-15). LogRocket's prerequisites include "Boundaries - What lines can you not cross?" [[28]](#ref-28). Pendo reports that Box does not pursue a feature idea that fails its principles [[36]](#ref-36). No published set read carries the field per principle |
| **A decision it settled** | One real case where the principle decided the outcome | Monzo follows two principles with a case study, such as "Case Study: Refunding customers during the upgrade" [[6]](#ref-6). Slack's "How it shows up:" gives a product example [[10]](#ref-10). Gazit's article works one decision that a security principle settled [[26]](#ref-26). LogRocket advises "Look for real stories where principles helped you and why so you can leverage that." [[28]](#ref-28). Cagan's eBay example is a principle for the case where buyers' and sellers' needs conflict [[39]](#ref-39) |

**What is received practice and what is the library's addition.** A name and a statement are
universal in the sets read. Reasoning is common. The trade-off form is shown by several publishers
and method writers. An examples field appears in two published sets, Slack's and Monzo's
[[10]](#ref-10), [[6]](#ref-6). **A field for what a principle rules out, and a separate field for its
tension, appear only in Productboard's prompt among the sets and prompts in the structure table**
[[4]](#ref-4), which is a vendor's AI prompt. Box's per-principle "Versus" and named cost, known only
through Pendo's report, is a comparable field outside that table [[36]](#ref-36). The template asks for all five fields and says so plainly, because the library cannot claim more
support than that.

**The truism test, and the dissent.** Intercom writes "no principle is a truism" and "The opposite of
a principle should itself be a principle" [[7]](#ref-7), and its 2022 post gives the method: "A good
litmus test here is to flip the principle around to express the exact opposite and see if it holds
up." [[8]](#ref-8) AWS writes that "To be effective a tenet needs to have an opposite which could be
acceptable to an organisation." [[38]](#ref-38) Productboard's prompt says a principle without a
reasonable opposite is not a principle [[4]](#ref-4). airfocus holds a different view, that
principles "should trigger an emotional response" [[23]](#ref-23). A moving line that nobody would
oppose passes airfocus and fails Intercom. The template follows Intercom, AWS and Productboard.
The library's reasoning is that a reader can apply the opposite test and cannot apply an emotional
response. Section 6 returns to this.

**How many.** Gazit says "No more than three to five principles are needed." [[26]](#ref-26) Product
School says "A good set has 3-5 principles." [[24]](#ref-24) Slack says "no more than seven"
[[25]](#ref-25). ThoughtSpot says "nine is too many, five is a great number, if you can get there" and
"We landed on seven." [[27]](#ref-27) Of the eight published sets in the table, leaving out
Productboard's prompt, two fall inside three to five: Slack's and PostHog's. The rest run from six to
fourteen, and Intercom's fourteen come in layers [[7]](#ref-7). **None of the sources cites a measurement.** The template asks for three to
five and treats the number as advice.

**Beginner note.** Draft the statement last. Start from a decision the team has argued about, and ask
which option the principle would have chosen. Write down what it rules out and what it costs, then
write the decision as the example. If you cannot attach a decision to a principle, it is probably not
yet a principle.

**Expert note.** Writing the trade-off inside the statement, as GitLab, Linear and Box do
[[5]](#ref-5), [[9]](#ref-9), [[36]](#ref-36), keeps the cost attached to the principle when someone
quotes it. That is the library's reading of why the form matters, not a finding. Distrust a principle
that no proposed decision has ever strained. That is the library's inference from the opposite test.

### When Principles Conflict

**What it is.** A statement of which principle wins when two pull apart, and in which kind of decision.

**Why it exists.** AWS expects tensions between tenets and says they need judgement
[[38]](#ref-38). ProductPlan writes "The principles
should clearly state what is most important." [[22]](#ref-22) Productboard's prompt has a set-level
section headed "When Principles Conflict" [[4]](#ref-4). It asks the author to explain a hierarchy or a
process for resolving conflicts, and gives a hypothetical example in which one principle wins for
user-facing decisions and another for internal tooling. That is a vendor's AI prompt, not a team's
recorded practice. A set that never says which one wins leaves the argument to whoever
is in the room. That last sentence is the library's inference, not a sourced claim.

**This section takes a side in a live dispute, and that side is the library's position.** ThoughtSpot
stack-ranked its candidates "within each category from most to least important" [[27]](#ref-27), yet
the same post says "it didn’t matter if some principles contradicted others" [[27]](#ref-27). Salesforce
UX, writing about design principles rather than product principles, wrote "we stack-ranked them" and "giving
our principles a clear order has made all the difference" [[30]](#ref-30). Nielsen Norman Group, also
writing about design principles, takes a middle position: principles should "Not conflict with one
another", and where two matter, "then clearly specify in which contexts one of these principles is
more important than the other" [[31]](#ref-31). AWS, writing about tenets, says they are ordered by
priority [[38]](#ref-38). **No source read opposes ordering outright, and none gives
a worked rule for two principles that conflict.** The template asks the author to say which principle
wins in a named kind of decision. That is closest to the NN/g position and is the library's
choice.

**Forms a resolution takes.** The "X over Y" form, shown by GitLab and Microsoft [[5]](#ref-5),
[[35]](#ref-35), and the "even over" form that Martin Eriksson teaches, for example "Conversion even
over revenue" [[13]](#ref-13), put the priority inside the principle. David Pereira's LogRocket
article names the same "'even over' statements" [[28]](#ref-28), and his Substack article gives the
same recommendation, citing Eriksson [[14]](#ref-14). That is one author's advice in two places, and
Eriksson [[13]](#ref-13) is the independent source. A ranked list is the other shape
[[27]](#ref-27), [[30]](#ref-30).

**Beginner note.** Pick the two principles most likely to collide, name one kind of decision where they
do, and say which one wins there and why. Do not rank every pair. One resolved conflict is more useful
than a complete table nobody applies.

**Expert note.** A full ranking is the most committal form. The library's reading is that a
resolution scoped to a kind of decision is less brittle than a global order. That reading is the
library's, not a source's, and the only support for the scoped form is NN/g's design-principles
method [[31]](#ref-31), which is a method analogue and not product evidence.

### Using Them in Decisions

**What it is.** Where the set is applied, such as product review, prioritisation, a request the team
may decline and onboarding, and how a decision cites a principle.

**Why it exists.** The sources describe sets in use, mostly in review settings. Stephen Forbes
describes Intercom's first principle in use "Not just in product reviews, roadmap meetings, or design
critiques" [[17]](#ref-17). At Slack, "Product managers and designers at Slack
reference them in weekly workshops where projects are shared at every stage" [[18]](#ref-18). Slack
also advises "it’s critical to designate clear checkpoints for assessing your work against the
principles" [[25]](#ref-25). ThoughtSpot tested its set by "injecting them into product design
conversations" [[27]](#ref-27). Intercom's account of its own practice mentions design and product
reviews, scope documents and posters [[16]](#ref-16). Cagan reports that "Product teams often tell
me that the product principles are the part of the strategic context that they use most often in
their daily discovery work" [[40]](#ref-40). That is Cagan's report of what teams tell him, not a
measurement.

**Onboarding is a use.** Intercom's new joiners get an onboarding pack that "contains their first
“Intermission”" [[17]](#ref-17), and Intercom also says its principles are used to assess and debate
options [[8]](#ref-8).

**Saying no is asserted more than shown.** Pendo reports of Box: "If a feature idea doesn’t align with
these principles, then Box does not pursue it." [[36]](#ref-36) PostHog's article argues that
principles make it easier to say no [[12]](#ref-12). This research found no named company source that
describes a principle being used to decline a specific request. The template names saying no as one
of the moments to record, which is the library's position. Confidence that sets are used this way is
medium-low.

**How a decision cites a principle is the library's position.** ProductPlan names the ability to
point back to a principle to justify a decision [[22]](#ref-22), but the log records no prescribed
citation form. The template asks the author to say where the set is cited and in what form. The family
contract calls a foundation a standard that work is judged against, and the library reads that as
judgement, not mechanical compliance. Intercom says "Principles are not rules - they exist to guide,
not control." [[8]](#ref-8) Its podcast makes the same point: "these are guides, they’re not rules"
[[16]](#ref-16).

**Beginner note.** List the two or three moments when a principle is cited, such as a product review,
a prioritisation discussion and a request the team is about to turn down. Say how the citation is
written, for example one line in the decision record naming the principle relied on.

**Expert note.** In the library's reading, a set that no decision ever cites is decoration. The log
records no measured effect of a set on decisions, so this companion cannot say that using one works.
It can say that sources describe teams using sets in review.

### Ownership and Changes

**What it is.** The named owner, how anyone proposes a change, who decides, and a dated change log.

**Why it exists.** This is where the set's own staleness is handled. **No source read names who owns a
set after it is written, or who approves a later change.** LogRocket describes leadership signing off a
draft [[28]](#ref-28), and Slack says the set should be company-wide [[25]](#ref-25). Cagan's 2020
position is that product leaders prepare the set [[40]](#ref-40) and that "The product manager needs to
understand these principles and the reasoning behind each one." [[2]](#ref-2) Intercom describes organic
change: its principles "evolve very slowly" [[16]](#ref-16). The role names the template asks for are
the library's position.

**The authorship debate sits behind this field.** ProductPlan writes "defined product principles are
driven by the team itself" [[22]](#ref-22). Product School says "Talk to your team, not just
leadership" [[24]](#ref-24). ThoughtSpot's set was built by a cross-functional team [[27]](#ref-27).
LogRocket recommends "A hybrid approach works better where leadership presents a draft and sharpens the
principles with the team" [[28]](#ref-28). Cagan's 2020 text has product leaders prepare the set
[[40]](#ref-40). This is a real split, and the template does not settle it. It asks only that an owner
be named and that the way a change is proposed be stated.

**The dated record is sourced in practice, not in method.** Intercom gives the one dated record of a
set changing, in three snapshots [[16]](#ref-16), [[7]](#ref-7), [[8]](#ref-8), as section 2 reports.
Two Intercom statements do not fit each other without an assumption. The company says "We also update
them every 1-2 years" [[7]](#ref-7), yet it describes the set in 2022 as the third major iteration in
about eight years [[8]](#ref-8). The sources do not say whether wording edits count as updates. Slack's
set differs by one principle between the 2021 list and a later list [[18]](#ref-18), [[10]](#ref-10).
Neither source gives a reason or a date for the difference, so this is a comparison and not a change
record. A curator's copy corroborates the 2021 list [[19]](#ref-19).

**Revision is invited, and rarely.** Kindel's tenets carry the phrase "unless you know better ones"
[[37]](#ref-37), which invites a change. ProductPlan says "An update should be an unusual and
well-considered event, not a regular occurrence." [[22]](#ref-22) A set that is set at the start of a
product can be consulted for years: Glitch reports that Trello's team "referred back to these
principles as they continued to develop it, even years later." [[29]](#ref-29) That is one company's
account as the author tells it.

**Beginner note.** Name one person who owns the set and one place where anyone can propose a change.
State who decides. Start the change log with the date the set was first agreed.

**Expert note.** A change log that shows only additions hides the retirements. The one sourced merge
is Intercom's, from five top-level principles to three, which it reported in 2019 [[16]](#ref-16). Record a retirement or a merge as a change,
and keep the reason. Each logged change is also the evidence that the Review Trigger below is working.

### Review Trigger

**What it is.** A table of three columns: the Condition that makes the set wrong or incomplete, the
Owner who notices, and What They Do About It. It is the family's own obligation, not a published
convention for this type.

**Why it exists.** The `standing-standards` contract requires every member to ship a trigger with a
named owner and a condition, not a calendar reminder, because members fail by going quietly out of
date ([family contract, section 4](../../docs/internal/contracts/standing-standards.md)). **No source
read names who owns a set after it is written, so none names an owner for a trigger.** Where a condition
has a source, the table names it. The owner
column is the library's. The conditions below are statements of intent, not logged events.

| Condition | Where it comes from |
|---|---|
| The company strategy changes significantly | Productboard's AI prompt lists "The company strategy changes significantly" as a condition for revisiting the set [[4]](#ref-4). That is a vendor's statement, and the library reads it as a trigger, not a calendar |
| A principle is consistently violated without a decision to change it | The same prompt lists "consistently violated one without deciding to change it" [[4]](#ref-4) |
| A new principle would have settled repeated debates | The same prompt, which sets its own threshold: "A new principle would have resolved 3+ debates in the last quarter" [[4]](#ref-4). That is the prompt's figure, presented here as a vendor's, not a measured one |
| A valid exception recurs | Intercom says to "try and re-codify that back in or change a principle, evolve it" [[16]](#ref-16). The quotation speaks of a valid exception and carries no count, so "recurs" and its threshold of a second occurrence are the library's reading |
| A principle does not take hold | Slack says "If a principle doesn’t take hold, it’s important to observe how it’s being used in the business and tune it based on your findings." [[18]](#ref-18) |

A secondary source lists strategic, technical and customer-expectation triggers for re-evaluating
principles. It is commentary, not an owner's account of its own set [[20]](#ref-20).

**The stated intervals disagree, and the template takes none of them.** Guru says "The principles you
write should be able to hold their ground for at least a year" [[21]](#ref-21). LogRocket says "Review
your product principles every three months" [[28]](#ref-28), which is a review and not a rewrite. David
Pereira's Substack article gives the same three-monthly review [[14]](#ref-14), so that is one author's
advice in two places and not two sources agreeing. Intercom says "We also update
them every 1-2 years" [[7]](#ref-7). ProductPlan says updates should be unusual [[22]](#ref-22), and
airfocus says principles should be "relevant, constantly adapting to the market and customer needs"
[[23]](#ref-23) while also noting that "Sticking with the same principles over a long time can be
helpful for conveying brand identity" [[23]](#ref-23). **No calendar interval is required, and the
`foundation` classification holds.** A team that wants a review date may add one as a floor and should
label it as its own choice.

**Beginner note.** Write each condition as an event someone can observe, not as a date. Give each row an
owner by role and say what that person does: reopen the set, run a short check against recent
decisions, or write the change into the log.

**Expert note.** The strongest rows are the ones that have already fired once. The row about a
significant strategy change is also the visible link to the product strategy, which this set outlives
and does not restate.

## 4. Variants and sizing

**The bundle ships one size, `lean`.** The maintainer ruled on 2026-11-20 that the bundle has a single
size. No source read publishes a long and a short version of one set. Intercom's overview announces
a plan to publish one post per principle [[8]](#ref-8), and this research read one such post
[[17]](#ref-17) and none of the others. GitLab follows its eight principles with a long section
headed "How we follow our Principles" [[5]](#ref-5). Neither is two versions of one set. The library
reads a set of three to five principles as not earning a second weight. Confidence in a single size
is medium, because it rests on the absence of a published pair and on the maintainer's ruling.

**What to do when a team wants more.** The research found no source for a fuller shape, so there is no
second variant. Depth in the sources lives per principle, not per document: Monzo's case studies
[[6]](#ref-6) and Slack's "How it shows up:" [[10]](#ref-10), and, as Intercom announces it, a post per
principle [[8]](#ref-8), of which this research read one [[17]](#ref-17). The
template's fields for a decision a principle settled and a trade-off it accepts are the places to add
depth. A team that needs only a few rules inside its strategy should use the
[`product-strategy` one-pager's Product Principles section](../product-strategy/product-strategy_template-one-pager-full.md)
instead. That choice is a matter of size, and section 8 states the rest.

**There is no second axis here.** This bundle has one size and one format.

## 5. Methodology lineage

**The log records no tie between product principles and a delivery methodology.** It records no
treatment of the type by any named delivery methodology or by any regulated-industry school, so this
companion claims no lineage by school. A table that sorted the type into methods would be invented.

What the sources do show is the lineage of the document's neighbours and a set of working methods for
writing a set, each from one author or team.

- **Cagan and the strategic context.** In the 2020 book the set is one of the things product leaders give
  a team [[40]](#ref-40), and in the coaching article it is the sixth of six kinds of strategic
  context [[2]](#ref-2). That is a method's placement of the artifact, not a procedure for writing it.
- **Tenets.** Tig Kindel and an AWS blog describe tenets, an Amazon-style practice that exists to
  settle questions that cannot be verified factually, and that requires an opposite which an
  organisation could accept [[37]](#ref-37), [[38]](#ref-38). The research read tenets as an
  analogue of principles. This companion does not equate the two.
- **The "X over Y" form.** The patterns and practices team at Microsoft modelled its guiding principles on
  the Agile Manifesto, and the page says a principle "contrasts one value over another" [[35]](#ref-35).
- **ThoughtSpot's process.** Name an audience and quality criteria, brainstorm, stack-rank within
  categories, take feedback in rounds, test in design conversations, then socialise [[27]](#ref-27).
- **LogRocket's prerequisites and categories.** The ideal customer, the experience level, boundaries and
  quality standards come first, then categories such as strategy, discovery, delivery and collaboration
  [[28]](#ref-28).
- **Gazit's do and don't list.** Take a stand, name the trade-off, describe how to build and not what to
  build, and keep the set to three to five [[26]](#ref-26). On the rule about how and what to
  build, Gazit and ProductPlan do not match, and section 6 records that.
- **Productboard's quality test.** A vendor's AI prompt tests whether each principle captures a real
  tension [[4]](#ref-4). It is a prompt, not a method.
- **A design-principles method as analogue.** NN/g's method for design principles tells an author to
  identify common trade-offs before writing [[31]](#ref-31). It is used here only as an analogue.

**Who publishes sets.** The sets read are published by companies about their own products (GitLab,
Monzo, Intercom, Linear, Supabase, PostHog, Slack) [[5]](#ref-5), [[6]](#ref-6), [[7]](#ref-7),
[[9]](#ref-9), [[11]](#ref-11), [[12]](#ref-12), [[18]](#ref-18), and by one product leader, David
Pereira, writing about his own twelve [[14]](#ref-14). The research does not show that these
publishers use the type differently.

## 6. Debates and contested boundaries

The sources agree on the type's definition and disagree on its edges. Several of the sources are
vendors with a product to sell: Productboard, ProductPlan, airfocus, Guru, Product School, Hyperact,
The Org and Pendo are among those tagged vendor in the log [[4]](#ref-4), [[22]](#ref-22),
[[23]](#ref-23), [[21]](#ref-21), [[24]](#ref-24), [[33]](#ref-33), [[34]](#ref-34),
[[36]](#ref-36). The library's reading of that tag is that a vendor is reliable on convention, and its
claims of fact need corroboration. Product School's company examples could not be matched to primary
sources, so this companion uses its stated advice and none of its attributions [[24]](#ref-24).

**Inside the strategy, or beside it?** No source read says a set should live only as a section of a
strategy document, but the sources split on how close the two sit. Hyperact calls principles "an
important asset of a solid product strategy" [[33]](#ref-33), Product School treats them as a lens inside
product strategy [[24]](#ref-24), and David Pereira groups one layer of his principles under strategy
[[28]](#ref-28). On the other side, Cagan places them beside the vision and the strategy [[39]](#ref-39),
and Slack keeps them out of strategy altogether [[25]](#ref-25). Guru says "Product
principles tie the product’s vision and strategy together." [[21]](#ref-21) **No source
ties a principle's life to one strategy period.** That is the library's ground for treating the set
as standing. The ground is the library's reading of the absence, at medium confidence.
**Recommendation: keep the set beside the strategy and let it outlive any one of them.**

**Standing, or per project?** Cagan's two texts frame the scope differently. His 2005 principles are
"specific to your domain and your particular project" [[1]](#ref-1), and his 2017 principles "are not
tied to any one product release" [[39]](#ref-39). Intercom does both: "We sometimes even create
principles for specific projects to get aligned on our approach up front." [[8]](#ref-8)
**Recommendation: the bundle is the standing set, and a project's own principles belong in that
project's PRD.** That is the library's reading. The two Cagan texts are consistent with it, though the
2005 text is a PRD guide dated only by a copyright footer and may reflect its genre, and Intercom's
practice shows that both forms can coexist.

**Whose set?** Team-driven (ProductPlan, and ThoughtSpot's cross-functional team [[22]](#ref-22),
[[27]](#ref-27)), team as well as leadership (Product School [[24]](#ref-24)), leader-prepared (Cagan,
2020 [[40]](#ref-40)) or a hybrid (LogRocket [[28]](#ref-28)).
**Recommendation: name an owner either way, and say in the set how the team's view reaches the
wording.** The sources do not say that any of the three outperforms the others, so this companion
does not pick one. The template asks only for a named owner and a stated way to propose a change.

**Memorable, or arguable?** airfocus wants a principle that triggers an emotional response
[[23]](#ref-23). Intercom, AWS and Productboard want an opposite that a reasonable team might choose
[[7]](#ref-7), [[38]](#ref-38), [[4]](#ref-4). **Recommendation: apply the opposite test first, and let
memorability be a bonus.** A line that nobody would argue against fails the test and cannot settle an
argument, however well it lands.

**Ranked, or a trade-off in each principle?** ThoughtSpot, ProductPlan and AWS lean toward ordering
[[27]](#ref-27), [[22]](#ref-22), [[38]](#ref-38). Gazit, Microsoft's team and LogRocket's "even over" form write the
trade-off into each principle [[26]](#ref-26), [[35]](#ref-35), [[28]](#ref-28). ThoughtSpot also wrote that
contradiction between principles did not matter [[27]](#ref-27). **Recommendation: write the trade-off
into the principle and name which principle wins in a named kind of decision.** No source opposes
ordering outright, and none gives a worked rule for two that conflict.

**How many?** Three to five (Gazit, Product School [[26]](#ref-26), [[24]](#ref-24)), no more than
seven (Slack [[25]](#ref-25)), seven after considering more (ThoughtSpot [[27]](#ref-27)), or fourteen in
layers (Intercom [[7]](#ref-7)). **None cites a measurement.** Treat every number as a heuristic. The
template asks for three to five, and the guide should say it is advice.

**How often is it revised?** Quarterly review, yearly hold or every one to two years, or rarely
[[28]](#ref-28), [[21]](#ref-21), [[7]](#ref-7), [[22]](#ref-22). Intercom's two figures fit each other only
if wording edits count as updates, and the sources do not say whether they do, as section 3 shows. **Recommendation: a condition, not a calendar.** The Review Trigger
section carries the conditions, and the log records no measurement behind any of those intervals.

**Does it cover execution or the choice of what to build?** Slack limits a set to execution
[[25]](#ref-25), while ProductPlan and Cagan describe the set as guiding what to build
[[22]](#ref-22), [[40]](#ref-40). Gazit's rule that principles describe how to build and not what to
build sits with Slack [[26]](#ref-26). **Recommendation: follow Cagan and ProductPlan, and say which
sense is meant if the set states its scope.** This is the library's position, held at medium-low
confidence, because the sources read it both ways.

**What no source measures.** Cagan's report that teams use principles most often in discovery is his
report, not a measurement [[40]](#ref-40). The log records no measured effect of a set on decisions
or outcomes, so this companion cites none. The sample is mostly practitioners and vendors who
recommend the type, and that is a property of who writes about it, not evidence that it works.

## 7. Anti-patterns and failure modes

**Beginner failures**

- **A truism.** A principle whose opposite no reasonable team would choose. Intercom: "no principle is a
  truism" [[7]](#ref-7). A vendor's prompt says a principle without a reasonable opposite is not a
  principle [[4]](#ref-4). The test is whether a thoughtful team could choose the reverse.
- **A feature list or a release plan.** Cagan: "Product principles are not a list of features, and they
  are not tied to any one product release." [[39]](#ref-39) ProductPlan: "You don’t build principles".
  [[22]](#ref-22)
- **Mission, vision or goals relabelled as principles.** ProductPlan: "A common mistake is conflating the
  company’s mission, product vision, and goals with product principles." [[22]](#ref-22)
- **No stated cost.** A principle with no trade-off cannot show what it gives up. Gazit says to take a
  stand by preferring one alternative [[26]](#ref-26), and Box's published set names a cost with each
  principle [[36]](#ref-36).
- **Too many.** Sources say three to five, up to seven, or fourteen in layers [[26]](#ref-26),
  [[25]](#ref-25), [[7]](#ref-7). Treat the figure as a heuristic and not as a finding.
- **A principle copied from a published set.** No page read states a reuse licence. Productboard reserves
  its rights [[4]](#ref-4), and the Salesforce page and the Mind the Product page carry reserved-rights
  footers [[10]](#ref-10), [[13]](#ref-13). The library describes the structures it found and copies
  no set's text. Write the team's own words.

**Subtle failures**

- **A set nobody cites.** Sources describe teams that use a set in review, onboarding and workshops
  [[17]](#ref-17), [[18]](#ref-18), [[16]](#ref-16). The library's inference is that a set with no place
  where it is cited risks being read once and not applied. This is the library's inference and not a
  sourced finding.
- **A principle the team consistently violates.** A vendor's prompt treats consistent violation without a
  decision to change the principle as a reason to reopen the set [[4]](#ref-4). The library's
  reading is that a violated principle is either a wrong principle or a missing decision.
- **A set that never changes, or changes with no record.** Intercom's record shows five principles
  merged into three, and a later set of four at the top level [[16]](#ref-16), [[7]](#ref-7). Slack's set
  differs between two snapshots with no stated reason [[18]](#ref-18), [[10]](#ref-10). A set with no
  owner and no reopening condition has no way to do either.
- **Principles treated as rules.** Intercom: "Principles are not rules - they exist to guide, not
  control." [[8]](#ref-8) ProductPlan: "A product principle is never “reached.”" [[22]](#ref-22)
- **Project principles inside the standing set.** Cagan's 2005 principles were "specific to your
  domain and your particular project" [[1]](#ref-1), and his later ones are not tied to one release
  [[39]](#ref-39). A principle that belongs to one project goes in that project's PRD.
- **A set that restates the current strategy.** This is the library's own caution, not a sourced one.
  A principle that restates one period's strategy choice will go stale when that strategy does, and no
  source ties a principle's life to a strategy period.
- **A design principle in the product set.** A principle that settles how a screen, message or
  interaction behaves belongs to design principles. That is the library's test, in section 8.
- **A claim that a principle is used to say no, with no case behind it.** The claim is asserted more
  often than shown, as section 3 reports [[36]](#ref-36).
- **Borrowing a set from a different company.** This is the library's caution, not a sourced one.
  Treat any borrowed set as untested until it passes the team's own opposite test.

**Naming trap.** The Org says "Principles of product differ slightly to product principles, as they
refer strictly to the design phase of a product." [[34]](#ref-34) The library's sibling bundle for that
sense is `design-principles`. Write "product principles" for the standing set that settles what the team
builds.

## 8. Relationships to other artifacts

**Design principles.** The sources split the two by scope. ProductPlan: "They also aren’t design
principles", which are "much more about implementation" [[22]](#ref-22). airfocus: "Design principles
refer purely to the design aspect of a product" [[23]](#ref-23). Marc Abraham: "I treat them very much
as two distinct concepts" [[32]](#ref-32). The Org's page scopes "principles of product" to the design
phase, and then blurs the two by saying principles guide product and design work [[34]](#ref-34).
Intercom keeps five product design principles inside its product principles [[7]](#ref-7), so one
company holds both under one roof.

**The library's test is its own, held at medium-low confidence, and the sibling bundle states it.** The
[`design-principles` companion](../design-principles/design-principles_companion.md) section 8 says that
a principle that settles how a screen, message or interaction behaves is a design principle, and one
that settles what the team builds, funds or declines is a product principle. The sources' scope test
and the library's test point the same way. No source draws the library's line in its words. The
[`design-principles` guide](../design-principles/design-principles_guide.md) is the sibling's operator
card. Some principles will straddle, and the Purpose and Scope section has a line for them.

**Company values.** The sources read that address values put them upstream and broader: Abraham, Guru
and ProductPlan do, and Cagan's 2020 text has principles state values and beliefs. Most of the other sources say nothing about values. Marc Abraham calls principles
"a clear set of standards and goals that connect company values with the outcomes that we’re trying to
achieve" [[32]](#ref-32). Guru: "Product principles are often inspired by your company's core values or
mission statement" [[21]](#ref-21). Cagan's 2020 chapter says "The principles reflect the values of the
organization" [[40]](#ref-40). ProductPlan warns about conflating mission, vision and goals with
principles [[22]](#ref-22). **No source gives a test between a value and a principle.** The
`product-strategy` one-pager's TRAP supplies one, which is the library's: values describe how you want
to behave, and principles decide arguments
([template](../product-strategy/product-strategy_template-one-pager-full.md)).

**Vision and strategy sit beside the set.** Cagan: "I always like to complement the product vision and product
strategy with a set of product principles." [[39]](#ref-39) Guru says principles capture what "aren’t
addressed or implied in the Vision or Strategy" [[21]](#ref-21). In this library the neighbouring
artifacts are the [product vision](../product-vision/product-vision_guide.md) and the
[product strategy](../product-strategy/product-strategy_guide.md). The vision says where the product is
going, and a principle says which way a trade-off leans on the way there. That reading is the library's.
A significant change to the strategy is one of the Review Trigger's conditions, and Productboard's AI
prompt lists it as a reason to revisit the set [[4]](#ref-4).

**The strategy neighbour is a matter of size.** The Product Principles section of the
[`product-strategy` one-pager, full variant](../product-strategy/product-strategy_template-one-pager-full.md)
(lines 157-175) asks for two to five rules that resolve recurring trade-offs. That section summarises
a set inside a strategy. This bundle is the set. A team that needs a few rules inside its strategy uses
the one-pager's section. A team that needs the standing set, with a reason, a cost, a boundary and a
settled decision for each principle, uses this bundle. The maintainer ruled on 2026-11-20 that the
one-pager's guidance gains a pointer to this bundle.

**The PRD.** Cagan's 2005 guide is the only source that relates principles to a PRD, and it places
project principles inside it [[1]](#ref-1). The library's reading is that a PRD is the home of a
project's own principles, while this bundle is the standing set that the PRD may cite. See the
[PRD guide](../prd/prd_guide.md).

**Engineering principles.** Hyperact separates product, engineering and design principles, and writes that
"engineering principles focus on the technical implementation" [[33]](#ref-33). Intercom has an
engineering layer in its set [[7]](#ref-7), and Langfuse's handbook publishes product-engineering
principles as a "What we do" and "What we don't do" list [[15]](#ref-15). Abraham describes three layers:
values, product principles and design principles [[32]](#ref-32).

**What no source relates.** No source read relates product principles to a trade study, a definition of
done or a positioning statement. Any line the library draws to those bundles is the library's
inference, and this companion draws none.

## 9. Adaptations

The log records limited research on adaptations, so this section reports what the sources show and
marks the rest as untested.

- **Scale and level.** Sources publish sets at several levels: Cagan's product line [[39]](#ref-39), his
  all-teams strategic context [[2]](#ref-2), Intercom's layered sets that every contributor
  inherits [[7]](#ref-7), and Monzo's set for one internal product [[6]](#ref-6). The Purpose and Scope
  section is where the choice is made.
- **Starting small.** Glitch reports a set written at the start of one product and consulted for years
  [[29]](#ref-29). The library infers from that one account that a set for a new product need not wait
  for scale.
- **Internal or published.** Cagan allows a set to stay a tool for the product teams [[39]](#ref-39).
  GitLab, Monzo and Linear publish theirs [[5]](#ref-5), [[6]](#ref-6), [[9]](#ref-9).
- **Writing the set with others.** A cross-functional team built ThoughtSpot's set [[27]](#ref-27),
  and LogRocket recommends a leadership draft sharpened with the team [[28]](#ref-28).
- **Reusing a published set.** No page read states a reuse licence, and Productboard reserves its rights
  [[4]](#ref-4). A team that wants to adapt a published set should check its licence and should still
  apply the opposite test, because a set written for another company may not pass it. That is the
  library's inference, not a sourced claim.
- **Ethics.** Cagan's chapter on product principles in *Empowered* is titled "Product Principles and
  Ethics" [[40]](#ref-40). The log records only that the chapter adds ethics guidance, not what it
  says, so this companion says nothing about it.
- **Methodology-specific tailoring, solo practitioners and regulated products.** The log records no
  research on any of them, as section 5 says. The template is untested for all three. A solo author
  can still use the rules-out and decision fields, which need no group.

## 10. Worked example

[`product-principles_example.md`](product-principles_example.md) is the product principles document for
Acme Analytics, in the `lean` size, owned by Dana Okoro, VP Product, who also owns the vision and the
strategy. It is dated after the FY26 strategy and after the design principles, so a reader can see a
product trade-off set sit beside an experience set and watch the line in section 8 being drawn. It is
worth checking five things. First, that each principle carries every field in section 3, including
what it rules out and a decision it settled. Second, that at least one principle rules out something
a stakeholder has asked for. Third, that its conflict section resolves a real tension between two of
its principles in a named kind of decision. Fourth, that a Review Trigger row names a significant
change to the strategy, so the link to the product strategy is visible. Fifth, that none of its
principles settles how a screen behaves and none restates a principle from the design set. Every
figure in it is labelled illustrative.

---

## References

Access dates are the research date, 2026-11-20, because the research log records no per-source fetch
date. Entries [39] and [40] are print books read from the maintainer's own copies, so they carry no
URL.

<a id="ref-1"></a>[1] Martin Cagan (Silicon Valley Product Group). "[How To Write a Good PRD](https://www.svpg.com/wp-content/uploads/2024/07/How-To-Write-a-Good-PRD.pdf)." svpg.com, copyright 2005, PDF hosted under a 2024 upload path (accessed 2026-11-20). Supports "Step 4: Define your Product Principles" as one of ten PRD steps, the 2005 framing of principles as specific to one project and written by the team, and the TiVo and eBay examples. The only date is the copyright footer. Steps 6 to 10 were not read line by line. [primary]

<a id="ref-2"></a>[2] Marty Cagan. "[Coaching - Strategic Context](https://www.svpg.com/coaching-strategic-context/)." svpg.com, 9 January 2020 (accessed 2026-11-20). Supports principles as the sixth of six kinds of strategic context, the statement that the context applies to all product teams in the company, and the product manager's need to understand each principle and its reasoning. [primary]

<a id="ref-3"></a>[3] Marty Cagan. "[Principles](https://www.svpg.com/principles/)." svpg.com, 27 December 2017 (accessed 2026-11-20). Supports only a caution: it is about principles of product management in general, not the product principles document, and it is not a source on the artifact. [primary]

<a id="ref-4"></a>[4] Productboard. "[Product Principles Document](https://www.productboard.com/product-management-prompts-library/product-principles-document/)." Product Management Prompts Library (accessed 2026-11-20). Supports the only blank structure found, a vendor's AI prompt prescribing five principles with five fields each, a "TENSION" field, a "WHAT IT MEANS WE WON'T DO" field, a "When Principles Conflict" section, the opposite test, and three revisit conditions. The page reserves its rights, so no wording beyond field names and a few short quoted phrases is copied here. [vendor]

<a id="ref-5"></a>[5] GitLab. "[Product Principles](https://handbook.gitlab.com/handbook/product/product-principles/)." GitLab Handbook, last modified 30 October 2026 at the time of reading (accessed 2026-11-20). Supports a set of eight principles, each a bold clause followed by an explanation paragraph, three in "X over Y" form, with no examples field and no rules-out field, and a long section headed "How we follow our Principles". No licence is stated in the page text read. [practitioner]

<a id="ref-6"></a>[6] Monzo. "[The Vision and Principles for Our Internal Product](https://monzo.com/internal-product)." monzo.com (accessed 2026-11-20). Supports six principles for one internal product, each a reasoning paragraph, two followed by a case study of a decision it settled, and a set-level list of purposes. No licence is stated. [practitioner]

<a id="ref-7"></a>[7] Des Traynor (Intercom). "[Foundations to build on: Intercom's principles for building product](https://www.intercom.com/blog/intercom-product-principles/)." Intercom blog, 20 October 2021 (accessed 2026-11-20). Supports fourteen principles in layers of four, five and five, the truism and opposite tests, the stated 1-2 year update cadence, and layered sets that every contributor inherits. No licence is stated. [practitioner]

<a id="ref-8"></a>[8] Emmet Connolly (Intercom). "[Introducing Intercom's product principles](https://www.intercom.com/blog/product-principles/)." Intercom blog, 9 February 2022 (accessed 2026-11-20). Supports the flip-it-around test for truisms, the statement that principles are not rules, the third major iteration in about eight years, standing sets plus occasional per-project principles, and use in onboarding and in assessing options. The overview was read, not the per-principle posts. No licence is stated. [practitioner]

<a id="ref-9"></a>[9] Linear. "[Principles & Practices](https://linear.app/method/introduction)." Linear Method (accessed 2026-11-20). Supports seven principles kept separate from thirteen practices, with names that sometimes carry a sequence or contrast. No licence is stated. [practitioner]

<a id="ref-10"></a>[10] Niki Bamford (Salesforce blog for Slack). "[Slack product design principles article](https://www.salesforce.com/blog/slack-product-design-principles/)." salesforce.com blog (accessed 2026-11-20). Supports a later set of five principles, each with a name, "What it means:" and "How it shows up:", differing by one principle from the 2021 list. A marketing-authored page whose footer reserves all rights, so it is a weaker source on process. [vendor]

<a id="ref-11"></a>[11] Supabase. "[Architecture](https://supabase.com/docs/guides/getting-started/architecture)." Supabase docs, section "Product principles" (accessed 2026-11-20). Supports seven principles, each a name and one to three sentences, some with a litmus test or a stated sacrifice. No licence is stated for the page text. [practitioner]

<a id="ref-12"></a>[12] Ian Vanagas (PostHog). "[How we decide what to build](https://posthog.com/newsletter/how-we-decide-what-to-build)." PostHog newsletter, 10 January 2024 (accessed 2026-11-20). Supports three one-line principles for what to build and an argument that principles make it easier to say no. No licence is stated. [practitioner]

<a id="ref-13"></a>[13] Tobias Freudenreich (Mind the Product). "[Using principles to make better decisions faster by Martin Eriksson](https://www.mindtheproduct.com/overcoming-decision-overload-using-principles-to-make-better-decisions-faster-by-martin-eriksson/)." Mind the Product, 15 August 2022 (accessed 2026-11-20). Supports a product leader's guidance to write principles as "even over" trade-offs, with three sample lines only. The page reserves rights. [practitioner]

<a id="ref-14"></a>[14] David Pereira (Untrapping Product Teams). "[How to Implement Product Principles so You Stop Struggling with Decisions](https://dpereira.substack.com/p/implementing-product-principles-effectively)." Substack (accessed 2026-11-20). Supports a product leader's twelve principles in four layers of three, each a name and one sentence, a recommendation of the "even over" form citing Eriksson, and a three-monthly review. No reuse licence is stated. [practitioner]

<a id="ref-15"></a>[15] Langfuse. "[Product Engineering Principles](https://langfuse.com/handbook/product-engineering/principles)." Langfuse handbook (accessed 2026-11-20). Supports a counter-example: titled principles built as "What we do" and "What we don't do" lists with no named principles, so a rules-out structure only. No reuse licence is stated. [practitioner]

<a id="ref-16"></a>[16] Des Traynor, with Paul Adams (Intercom). "[Intercom on Product: The principles behind how we build](https://www.intercom.com/blog/podcasts/intercom-on-product-ep04)." Intercom podcast and transcript, 25 July 2019 (accessed 2026-11-20). Supports Intercom's own account of use in design and product reviews, scope documents and posters, the merge of five top-level principles into three, and re-codifying after a valid exception. [practitioner]

<a id="ref-17"></a>[17] Stephen Forbes (Intercom). "[Intercom's product principles: Start with the problem to achieve better solutions](https://www.intercom.com/blog/intercom-product-principles-start-with-the-problem/)." Intercom blog, 5 October 2022 (accessed 2026-11-20). Supports one principle used in product reviews, roadmap meetings, design critiques and show-and-tells, and in the new-joiner onboarding pack. [practitioner]

<a id="ref-18"></a>[18] Ethan Eismann (Slack). "[Why your organization needs product principles](https://slack.design/articles/why-your-organization-needs-product-principles/)." Slack Design (accessed 2026-11-20). Supports Slack's 2021 set of five, weekly workshops where principles are cited, the limit to execution, and the keep, tune or drop stance. The page text shows no date, and 2021 is inferred from the TechCrunch URL of the same article, which is entry [25]. The two entries are one author's one argument. [practitioner]

<a id="ref-19"></a>[19] Ben Brignell (curator). "[Slack Product Principles](https://principles.design/examples/slack-product-principles)." principles.design (accessed 2026-11-20). Supports only that a curator's copy corroborates the 2021 list of five principles, citing Slack's own article. A secondary copy, not used for process claims. [practitioner]

<a id="ref-20"></a>[20] Department of Product. "[Product Principles - Examples for Product Managers](https://departmentofproduct.com/blog/product-principles-examples-for-product-managers)." departmentofproduct.com (accessed 2026-11-20). Supports secondary commentary only: strategic, technical and customer-expectation triggers for re-evaluating principles, and a repeat of Intercom's 1-2 year cadence. Author and date are not shown in the text read. Not an owner's account of its own use. [practitioner]

<a id="ref-21"></a>[21] Guru. "[How Good Product Principles Support Your Workflow and Team](https://www.getguru.com/blog/how-good-product-principles-support-your-workflow-team)." Guru blog (accessed 2026-11-20). Supports the statement that principles tie vision and strategy together, that they are often inspired by company values, that they should last at least a year, and a size of three to five ideas. It is a vendor's general advice, not a record of Guru revising its own set. [vendor]

<a id="ref-22"></a>[22] ProductPlan. "[How to Define Your Product Principles](https://www.productplan.com/learn/product-principles/)." ProductPlan Learn (accessed 2026-11-20). Supports the exclusions (mission, vision, goals, metrics, requirements and design principles), that a principle is never reached, that updates should be rare, that principles should state what is most important, that there should be no more than a handful, and that they are team-driven. [vendor]

<a id="ref-23"></a>[23] airfocus. "[What Are Product Principles? Definition & FAQ](https://airfocus.com/glossary/what-are-product-principles/)." airfocus glossary (accessed 2026-11-20). Supports the scope split from design principles, and a counter-position that principles should be simple, emotive and constantly adapting, while noting that long-lived principles can convey brand identity. [vendor]

<a id="ref-24"></a>[24] Carlos Gonzalez de Villaumbrosia (Product School). "[Product Principles That Drive Great Products](https://productschool.com/blog/product-strategy/product-principles)." Product School blog, August 2025 (accessed 2026-11-20). Supports a set size of three to five, drawing principles from the whole team, and the point that principles make trade-offs easier to navigate and support the product strategy. Its company attributions could not be matched to primary sources, so none is used here. [vendor]

<a id="ref-25"></a>[25] Ethan Eismann (Slack). "[Why your organization needs product principles](https://techcrunch.com/2021/03/01/why-your-organization-needs-product-principles/)." TechCrunch, 1 March 2021 (accessed 2026-11-20). Supports Slack's five principles, the limit to execution, company-wide ownership, a cap of seven, designated checkpoints, and principles that are never static. The same article as entry [18]. [practitioner]

<a id="ref-26"></a>[26] Nir Gazit. "[Applying product principles to guide better product decisions](https://www.mindtheproduct.com/applying-product-principles-guide-better-product-decisions)." Mind the Product, 2017 (accessed 2026-11-20). Supports do and don't guidance: take a stand, name the trade-off, describe how to build and not what to build, three to five principles, principles can change, and one worked decision settled by a security principle. [practitioner]

<a id="ref-27"></a>[27] ThoughtSpot product team. "[How We Crafted Our Product Principles](https://www.thoughtspot.com/blog/how-we-crafted-our-product-principles)." ThoughtSpot blog (accessed 2026-11-20). Supports a cross-functional process (audience, criteria, brainstorm, stack-rank within categories, feedback, testing in design conversations), the view that contradiction did not matter, and a set of seven reached after debating the count. [practitioner]

<a id="ref-28"></a>[28] David Pereira. "[How to define and implement product principles](https://blog.logrocket.com/product-management/product-principles-guide/)." LogRocket Blog, 23 September 2024 (accessed 2026-11-20). Supports prerequisites that precede principles (including boundaries), top-down, bottom-up and hybrid authorship, "even over" statements attributed to Martin Eriksson, stories as evidence, and a three-monthly review. [practitioner]

<a id="ref-29"></a>[29] Glitch (author not named on the page). "[Principle-led Product Development](https://blog.glitch.com/post/principle-led-product-development)." Glitch blog, 8 February 2018 (accessed 2026-11-20). Supports principles set at the start of one product (Trello) and consulted for years, as the author reports it. [practitioner]

<a id="ref-30"></a>[30] Salesforce UX. "[Defining Principles to Drive Design Decisions](https://medium.com/@salesforce/defining-principles-to-drive-design-decisions-811a85032c56)." Medium (accessed 2026-11-20). Supports the strongest case found for a ranked set. It concerns design principles, not product principles, and is used here only as a method analogue. [practitioner]

<a id="ref-31"></a>[31] Nielsen Norman Group. "[Crafting Product-Specific Design Principles to Support Better Decision Making](https://www.nngroup.com/articles/design-principles/)." nngroup.com (accessed 2026-11-20). Supports a middle position between global ranking and none: principles should not conflict, and where two matter the context in which each wins should be stated, plus a step to identify common trade-offs. It concerns design principles and is used here only as a method analogue. [practitioner]

<a id="ref-32"></a>[32] Marc Abraham. "[My Product Management Toolkit (34): Product Principles](https://marcabraham.com/2019/01/11/my-product-management-toolkit-34-product-principles/)." marcabraham.com, 2019 (accessed 2026-11-20). Supports values, product principles and design principles as three layers, principles as the link between company values and outcomes, and a statement that he treats product and design principles as distinct. [practitioner]

<a id="ref-33"></a>[33] Hyperact. "[Product Principles for Better Decision Making](https://www.hyperact.co.uk/blog/product-principles)." hyperact.co.uk (accessed 2026-11-20). Supports a three-way split of product, engineering and design principles, and principles as an asset of a product strategy. [vendor]

<a id="ref-34"></a>[34] Anna Bradley-Smith (The Org). "[What is the Role of Principles in Product Work?](https://theorg.com/iterate/role-of-principles-in-product-work)." The Org, April 2023 (accessed 2026-11-20). Supports the statement that "principles of product" refer to the design phase, which the page also blurs with product and design work. [vendor]

<a id="ref-35"></a>[35] J.D. Meier (Microsoft patterns & practices). "[patterns & practices Guiding Principles](https://learn.microsoft.com/en-us/archive/blogs/jmeier/patterns-practices-guiding-principles)." Microsoft Learn archive blog, last updated 20 June 2006 (accessed 2026-11-20). Supports the "X over Y" contrast form, modelled on the Agile Manifesto, and principles as a way to govern actions without a rule for every situation. The page mixes contrast pairs with non-contrast statements. [practitioner]

<a id="ref-36"></a>[36] Erin Wilkinson (Pendo). "[Using Product Principles to Guide Your Decision-Making](https://www.pendo.io/pendo-blog/using-product-principles-to-guide-your-decision-making)." Pendo ProductCraft blog, 12 June 2020 (accessed 2026-11-20). Supports Box's seven principles, each published with a "Versus" and a named cost, and the use of a principle as a go or no-go filter on feature ideas. The use is reported by a vendor and not shown by a case. [vendor]

<a id="ref-37"></a>[37] Tig Kindel. "[Tenets](https://blog.kindel.com/2020/02/10/tenets/)." tig.log, 10 February 2020 (the page shows a later update) (accessed 2026-11-20). Supports Amazon-style tenets of two kinds, foundational and aspirational, the invitation to revise "unless you know better ones", and tenets at company, organisation, team and project levels. [practitioner]

<a id="ref-38"></a>[38] AWS Executive in Residence Blog (author not captured in the extract). "[Tenets: supercharging decision-making](https://aws.amazon.com/blogs/enterprise-strategy/tenets-supercharging-decision-making)." AWS Cloud Enterprise Strategy Blog (accessed 2026-11-20). Supports the requirement that a tenet has a plausible opposite, tenets ordered by priority, and tensions between tenets that need judgement. [practitioner]

<a id="ref-39"></a>[39] Marty Cagan. *Inspired: How to Create Tech Products Customers Love*, second edition. Wiley, 2017, chapter 27, "Product Principles," printed pages 135-136. A copyrighted book read from the maintainer's own copy on 2026-11-20, with no URL (accessed 2026-11-20). Supports the 2017 framing of principles as a standing artifact beside the vision and the strategy, not a list of features, not tied to one release, aligned with the vision for a product line, optionally internal, with eBay's buyers-and-sellers example. [primary]

<a id="ref-40"></a>[40] Marty Cagan. *Empowered: Ordinary People, Extraordinary Products*. Wiley, 2020, chapter 39, "Product Principles and Ethics," printed pages 201-202. A copyrighted book read from the maintainer's own copy on 2026-11-20, with no URL (accessed 2026-11-20). Supports the 2020 framing of principles as part of the strategic context product leaders prepare, the need for a team to understand each principle and its reasoning, and Cagan's report that teams use them most often in discovery, which is his report and not a measurement. [primary]
