# Lean UX Canvas: the companion

The reference behind the template. Read this when you want to know why a section exists, what the
research actually says, and where the sources genuinely disagree.

## 1. Orientation

A Lean UX Canvas frames one initiative on a single page before anyone commits to building anything. It
links the business problem the team is solving, the outcomes the business wants, the users affected, the
outcomes those users want, and the candidate solutions, then turns those links into testable hypotheses.
It closes by naming the single most important thing the team needs to learn right now and the smallest
piece of work that would learn it [[5]](#ref-5)[[19]](#ref-19). Jeff Gothelf created it in 2016 to codify
training he had already been giving a client, built on the process his and Josh Seiden's Lean UX book
describes [[1]](#ref-1). He updated it in 2019 [[4]](#ref-4) and, with Seiden, renamed it the Lean Product
Canvas in 2024 [[2]](#ref-2); this bundle keeps the older name as its title and the newer
one as an alias, by the maintainer's ruling.

At a glance:

- **It is a facilitation tool first, and its originators say so in those words**: "a facilitation tool for
  cross-functional teams designed to create a customer-centric conversation" [[4]](#ref-4). The filled page
  is the record of that conversation, not the thing of value by itself.
- **It has eight boxes, filled roughly in order**, from the business problem through to the smallest
  experiment that would test the riskiest hypothesis [[4]](#ref-4)[[5]](#ref-5). This bundle adds a ninth
  section to log revisions, covered in section 3 below.
- **It is written at the start of an initiative, by the whole team**, with stakeholders and clients joining
  where possible, and a first pass rarely takes less than half a day and sometimes spreads across meetings
  over a couple of weeks [[19]](#ref-19).
- **It is revised while the initiative's experiments run.** After the smallest experiment returns a result,
  the team asks Box 7's question again, "What’s the next most important thing we need to learn?"
  [[7]](#ref-7), and it can even send
  the team back to the business problem box if the evidence says the team had the wrong problem, the wrong
  audience, or the wrong measure of success [[19]](#ref-19).
- **Two things this companion says about where the canvas sits are this library's own position, not a
  claim any source makes.** Section 8 states both plainly, because the honesty of that distinction matters
  more than the convenience of skipping it.

## 2. Origins and evolution

Gothelf published the first version of the canvas on December 15, 2016, and he is explicit that a client
request, not a personal initiative, prompted it: he had been asked to codify product discovery training he
had already delivered, and he built the canvas as a codification of the process his Lean UX book
introduced [[1]](#ref-1). The first edition of that book dates to 2013, three years before the canvas
existed [[2]](#ref-2).

Version 2 followed on September 9, 2019 [[4]](#ref-4). Gothelf explained changes to Boxes 2, 3 and 4 in that
pass, and widened Box 5. The business outcomes box needed a clearer line against the user outcomes and
benefits box, and the user outcomes box was, in his words, the part of the canvas with the most confusion,
so he rewrote both to draw a sharper line between the two [[4]](#ref-4). He also tightened the users box, because teams were taking what he called a
shortcut on it, and he widened the solutions box to admit new systems, business models, and non-technical
solutions rather than only product features [[4]](#ref-4). The hypotheses box itself did not change in any
meaningful way in this pass [[4]](#ref-4).

On November 4, 2024, Gothelf and Seiden renamed the canvas the Lean Product Canvas, alongside a new
companion tool, the Lean Strategy Canvas [[2]](#ref-2). They frame the rename as a response to scope rather
than a fix to a flaw: the canvas itself had not gone wrong, but its positioning and prompts needed to shift
to match a broader practice that had grown to include a full product's strategy and OKRs
[[2]](#ref-2). The 2024 PDF keeps all eight boxes and their order, with heading changes to three of
them and prompt changes to three others: the business outcomes box now echoes the language of Gothelf and
Seiden's own OKR book, the user outcomes box adds jobs-to-be-done language, and the box that chooses what
to learn first now points explicitly to the companion Hypothesis Prioritization Canvas
[[2]](#ref-2)[[5]](#ref-5). The hypothesis sentence itself changed grammatically between the two eras: the
book states it in the active voice, "we believe we will achieve," while the 2024 PDF states it in the
passive voice, "will be achieved if." Both carry the same four slots, business outcome, user, benefit, and
feature, so this is a documented change in wording rather than an error in either source
[[5]](#ref-5)[[19]](#ref-19).

The third edition of the Lean UX book, published in 2021, is organized around the canvas rather than
introducing it as one tool among several: chapter 4 presents it, and each of chapters 5 through 12 takes
one box in turn [[7]](#ref-7)[[19]](#ref-19). That same book calls the canvas optional to the method itself,
useful as a teaching device even for a team that practices Lean UX without filling one out
[[19]](#ref-19).

This bundle, following a 2026-10-30 build and the maintainer's own ruling on the question, uses "Lean UX
Canvas" as the title, because that is the name issue #330 and the third edition of the Lean UX book use, and
at least one third-party guide written after the rename still leads with it [[13]](#ref-13). It records "Lean Product Canvas" as an alias so a reader
searching under the newer name still finds it.

## 3. Anatomy (section by section)

The template follows Gothelf's eight boxes in his own numbering and filling order, then adds a ninth
section this library introduces. The numbering describes the order a team fills the canvas in on a first
pass, not a rule that later boxes cannot be revisited; the book is explicit that each box can also be used
on its own, as a standalone technique [[19]](#ref-19).

### Box 1: Business Problem

This box opens the canvas, and Gothelf's own walkthrough of how to use it starts here: the team names the
business problem statement before touching any other box [[7]](#ref-7). The 2024 heading shortens the 2019
wording, "Business problem statement," to "Business Problem," without changing what the box asks for
[[4]](#ref-4)[[5]](#ref-5). Writing in Gothelf's own words elsewhere, the box's "how might we" ending also
supplies the objective half of an OKR built from the canvas, with the business outcomes box supplying the
key results half [[16]](#ref-16).

Beginner note: describe what changed in the world and why it makes this a business problem worth the
organization's attention right now, not a description of a solution or a feature idea.

Expert note: a team that has already written a standalone problem statement can carry it into this box
rather than redoing the work. Gothelf's walkthrough begins by writing the business problem statement
[[7]](#ref-7); whether an existing problem-statement document should feed this box is this library's own
position, not a sourced rule; see section 8.

### Box 2: Business Outcomes

Gothelf defines a business outcome as a measured change in human behavior, not a revenue or output target
[[10]](#ref-10)[[19]](#ref-19), and he has separately called this "Perhaps the most critical box in the entire
canvas", because its outcomes become the success criteria the hypotheses box later tests against
[[11]](#ref-11). The 2024 prompt made that discipline more explicit by adding the format his and Seiden's
OKR book uses for stating who does what by how much [[2]](#ref-2)[[5]](#ref-5).

Beginner note: state a measurable change in what people do, not a number the business wants to see on a
report.

Expert note: this box exists partly to be distinguished from Box 4, and the two are the canvas's most
commonly confused pair. See the debate recorded in section 6 before filling either box.

### Box 3: Users

The 2024 wording widens this box past paying customers to anyone who configures the product or is affected
by its use [[5]](#ref-5). Gothelf flagged this box in his 2019 revision because teams had been taking a
shortcut on it, treating it too casually, and he tightened the language in response
[[4]](#ref-4)[[12]](#ref-12). The book's own practice fills this box with proto-personas where the team has
them [[19]](#ref-19).

Beginner note: name the users specifically enough that someone unfamiliar with the project could picture
them, including any non-buyer users the product has to serve.

Expert note: where a researched persona already exists, point to it rather than inventing a thinner
sketch for the canvas; whether that pointer should be a formal rule is this library's own position, not a
sourced one. See section 8.

### Box 4: User Outcomes and Benefits

Gothelf names this box as the part of the canvas with the most confusion [[4]](#ref-4), and an independent
podcast discussion of the 2019 update corroborates that it was the single most confusing box, more so than
any other [[12]](#ref-12). His own resolution distinguishes it from Box 2 directly: business outcomes are
measurable behavior, while user outcomes are the reasons users seek out a product in the first place, and
those reasons are often not measurable goals at all but intangible states of being
[[10]](#ref-10). The 2024 prompt adds jobs-to-be-done language to this box [[2]](#ref-2)[[5]](#ref-5).

Beginner note: describe what users want to achieve and how they want to feel, in language a user would
recognize, not a restatement of the business outcome in different words.

Expert note: one independent source records a minority reading of this box as an "ethics box," a place to
map what could go wrong for users, which Gothelf's own pages do not use [[12]](#ref-12). Section 6 names
this as a contested reading rather than a settled one.

### Box 5: Solutions

The 2024 prompt asks for product, feature, or enhancement ideas [[5]](#ref-5); the 2019 version had
explicitly widened the box to admit new systems, business models, and non-technical solutions, not only
software features, and Gothelf's own guidance calls for ideas that can be big, small, innovative, or even a
little unconventional [[4]](#ref-4).

Beginner note: list candidate solutions as widely as the box's 2019 widening invites, including a
non-technical option, before narrowing to anything specific.

Expert note: nothing in this box commits the team to building anything; naming a solution here is not the
same as choosing one. The library's position on what document takes over once a team does choose is in
section 8.

### Box 6: Hypotheses

This box combines Boxes 2 through 5 into a single sentence, carrying four slots: the business outcome, the
user, the benefit the user attains, and the feature or solution that attains it
[[5]](#ref-5)[[19]](#ref-19). Each hypothesis should address exactly one feature; a hypothesis spanning
several features cannot be tested cleanly [[5]](#ref-5). Gothelf's own 2019 post reports that the box saw
no significant change in that revision, unlike its neighbors [[4]](#ref-4). A companion
tool, the Hypothesis Prioritization Canvas, slots in immediately after this box, ranking the hypotheses it
produced on a two-by-two of risk against perceived value before the team moves to Box 7
[[6]](#ref-6)[[19]](#ref-19).

Beginner note: write one hypothesis per candidate feature, following the four-slot grammar exactly, rather
than one long hypothesis that bundles several ideas.

Expert note: when a canvas produces more hypotheses than the team can act on at once, use the Hypothesis
Prioritization Canvas to narrow them before choosing which one to learn about first in Box 7
[[6]](#ref-6).

### Box 7: What We Need to Learn First

Here the team picks one hypothesis, lists the ways it might fail, and names the single riskiest assumption
behind it [[5]](#ref-5). In a hypothesis's early stages, the guidance favors risks to value over risks to
feasibility [[4]](#ref-4)[[5]](#ref-5). Gothelf is pointed about scope here: the job is not to list every
risk a hypothesis carries, but to identify the one thing that matters most to learn right now
[[7]](#ref-7).

Beginner note: choose the single riskiest assumption behind one hypothesis, not a list of everything that
could go wrong with it.

Expert note: this box is revisited, not answered once. After an experiment from Box 8 returns, the team
asks this box's question again, and evidence from an experiment can even send the team back to Box 1 if it
shows the wrong problem, audience, or measure of success was in play
[[7]](#ref-7)[[19]](#ref-19).

### Box 8: The Least Work to Learn It

This box designs the smallest experiment that would show whether the riskiest assumption named in Box 7 is
true or false [[5]](#ref-5). The book is explicit that "MVP" in this context means a small and fast way of
learning something, not a stripped-down release meant to ship [[19]](#ref-19).

Beginner note: design the cheapest test that would actually answer the question Box 7 named, not a smaller
version of the final product.

Expert note: this box sketches the shape of a test; it does not plan one. No source this research read
gives this box a decision rule, an allocation, or named variants, and a document that does that work is
this library's position for what comes next, stated plainly in section 8.

### Box 9: Revisions and What Takes Over

This section is this library's own addition; no source read gives the original canvas a dedicated place to
log revisions, and the family contract's second cadence exception exists precisely because a canvas that
is revised without any record cannot show what the team actually learned. Part of it is sourced, and part
of it is not, and this companion keeps that distinction visible rather than blurring it.

The dated, iterative half is sourced. The 2024 PDF carries its own date and iteration fields in its header
[[5]](#ref-5), a GitHub skill file for the canvas treats it explicitly as "not a one-time exercise" that
gets revisited as the team learns [[18]](#ref-18), and a vendor guide advises using versioning and
iteration so the canvas keeps reflecting current knowledge and asks for outcomes, insights, and next steps
to be documented and linked back to the assumptions they test [[13]](#ref-13)[[18]](#ref-18).

The successor half is this library's position, not sourced. No source this research read names which
document takes over once a canvas has served its purpose. The best evidence available is indirect: one
named software consultancy reports that on every project there came a point where the canvas had enough
definition that it was essentially abandoned in favor of other tools, after serving as a living document
for as long as it lasted [[8]](#ref-8). This companion treats that account, together with the family
contract's own successor obligation, as the basis for naming a successor document here, and says so rather
than presenting it as something Gothelf's own sources establish.

Beginner note: every time the team loops back through Box 7 and Box 8, add a dated row recording what was
learned, whether the assumption held, and which boxes changed as a result.

Expert note: when the canvas stops changing because the team has committed to a direction, changed course,
or stopped the initiative, name the document that takes over in this section rather than letting the
canvas quietly go stale. Which document that should be is argued, not sourced; section 8 states the
argument.

## 4. Variants and sizing

This bundle ships one size, lean, with no full variant. That is a structural decision about this bundle,
not a claim drawn from the research: Gothelf publishes the canvas as a single one-page shape in both the
2019 and 2024 versions, and this research found no source that splits a short form of the canvas from a
longer one [[4]](#ref-4)[[5]](#ref-5). A team that wants more structure than the canvas itself offers is
better served by the documents named in section 8, which take over once the canvas has done its job, than
by an invented full variant of the canvas itself.

## 5. Methodology lineage

The canvas belongs to Lean UX, and this research traced it to a single lineage: Gothelf and Seiden's own
practice, developed first in the Lean UX book and then packaged as a facilitation tool for the kind of
discovery work that book describes [[1]](#ref-1)[[19]](#ref-19). It was written with a software audience in
mind from early on. The 2024 rename post states that none of the canvas's prompts are specific to UX
designers, product managers, or software engineers [[2]](#ref-2), and a named software design and
development consultancy reports using it at the start of new software products to align a team around the
problem before work begins [[8]](#ref-8).

This research did not investigate how any named delivery framework, or a regulated environment, treats
this canvas, and this companion claims nothing about it. Inventing a comparison here would be exactly the kind of unsourced
confidence this library's own review standards exist to catch. A reader working in one of those frameworks
should treat the canvas as a Lean UX artifact that can sit at the start of an initiative inside any of
them, rather than as something any of them formally adopts.

## 6. Debates and contested boundaries

**Business outcomes against user outcomes.** This is the canvas's best-documented point of confusion.
Gothelf names Box 4 as the part of the canvas that caused the most trouble when he revised it in 2019
[[4]](#ref-4), and an independent podcast discussion of that same revision corroborates it, calling Box 4
more confusing than any other box, including Box 2 [[12]](#ref-12). Gothelf's own resolution draws the line
on measurability: business outcomes are measured behavior, user outcomes are often not measurable at all,
and the two ideally align so that a user's behavior change also benefits the business
[[10]](#ref-10). A minority reading, recorded independently rather than by Gothelf himself, treats Box 4 as
an "ethics box," a place to map what could go wrong for users rather than only what they want
[[12]](#ref-12). Gothelf's own pages do not use that reading, and this research found no camp of named
proponents defending it beyond the one podcast episode, so this companion records it as a documented
dissent rather than a settled second interpretation.

**Facilitation tool or written document.** No source this research read full argues either side of this by
name, so it is not a debate with camps so much as a tension the sources leave open. The originators
describe the canvas as a facilitation tool whose job is to produce a certain kind of conversation
[[4]](#ref-4)[[19]](#ref-19), and the 2024 rename post frames both the canvas and its companion as devices
for having the right conversations at the start of an initiative [[2]](#ref-2). At the same time, the
book's own list of what the canvas does for a team includes communicating the work to people outside the
team, which only the written artifact can do [[19]](#ref-19). In practice this plays out differently from
team to team: one lead business analyst's team filled it on brown paper and photographed the result before
moving on [[9]](#ref-9), while a software consultancy kept it as a living document for as long as it
lasted before other tools took over [[8]](#ref-8).

**The 2024 rename.** Gothelf and Seiden renamed the canvas in 2024 [[2]](#ref-2). A vendor guide written
after that rename still titles its own page under the older name and treats the newer one as the canvas's
latest evolution rather than a replacement in current use [[13]](#ref-13). One source is not a measure of
adoption across the field, so this companion states only that the older name persists in at least one
current third-party guide, not that it remains the majority usage.

**The hypothesis sentence's two wordings.** The book states the hypothesis in the active voice, and the
2024 PDF states it in the passive voice, though both carry the same four slots
[[5]](#ref-5)[[19]](#ref-19). This is a documented evolution in wording across two eras of the same source
family, not a disagreement between independent camps, and it is listed here because a reader comparing an
older filled canvas with a newer one should not read the different phrasing as an error.

## 7. Anti-patterns and failure modes

A six-item pitfalls list from a community-contributed skill file, built on top of the canvas rather than
by its originators, names the recurring ways teams get this wrong: starting from a solution rather than a
problem, writing a vague business outcome, naming a user segment too broadly to act on, confusing the
business outcomes box with the user outcomes box, filling the solutions box with only one idea, and
skipping the experiment step entirely [[18]](#ref-18). Each of the first five has a direct root in the
boxes themselves: a vague business outcome fails Gothelf's own test that outcomes be measurable behavior
changes [[10]](#ref-10), and a single solution in Box 5 undercuts the box's own 2019 widening to admit
several kinds of candidate solutions [[4]](#ref-4).

Two further failure modes come directly from the structural rules the boxes themselves carry. A hypothesis
that bundles several features into one sentence breaks the canvas's own rule that each hypothesis address
exactly one feature, and it cannot be tested cleanly as a result [[5]](#ref-5). And Box 2 against Box 4 is
not only a debate (section 6); filling either box with language that belongs in the other is the
confusion Gothelf rewrote the user outcomes box to remove, calling it the part of the canvas with the most
confusion [[4]](#ref-4), and a community pitfalls list names it as one of six recurring failures
[[18]](#ref-18).

A practical failure mode belongs here too, distinct from how any one box is filled. One named software
consultancy reports that distributing and maintaining the canvas with clients who were not in the room for
its creation was the hardest practical problem across their projects, worse than any disagreement about
what belonged in a given box [[8]](#ref-8).

## 8. Relationships to other artifacts

**The Hypothesis Prioritization Canvas** is a companion tool, not an alternative canvas. It slots in
between Box 6 and Box 7, ranking the hypotheses Box 6 already produced on a two-by-two of risk against
perceived value, rather than re-deriving them [[6]](#ref-6).

**The Lean Strategy Canvas**, introduced alongside the 2024 rename, is a facilitation tool for setting up
better work using the renamed canvas [[2]](#ref-2). It is not admitted to this library.

**Ash Maurya's Lean Canvas** is a one-page business modeling tool for a whole business, rather than one
initiative's hypotheses [[15]](#ref-15). A vendor guide draws the line in practical terms: use the Lean UX
Canvas to validate a product or feature assumption quickly with real users, and use Maurya's Lean Canvas
for early-stage business-model or revenue validation [[13]](#ref-13).

**Jeff Patton's Opportunity Canvas** overlaps this canvas most closely. Patton scopes his canvas to a new
feature on an existing product, drawing his own line against the Business Model Canvas rather than against
this one [[14]](#ref-14). Marty Cagan's Opportunity Assessment draws the same existing-product-versus-new-
business line, from a different named practitioner tool [[17]](#ref-17). No source this research read
compares the Lean UX Canvas against either tool by name; the overlap with Patton's canvas in particular is
close enough that this library ships one of the two, and this companion names the overlap rather than
hiding it.

**OKRs** are not a separate artifact the canvas defers to. Gothelf maps an OKR directly onto the canvas: the
objective comes out of Box 1's closing "how might we" statement, and the key results come out of Box 2's
business outcomes, which he describes as always quantifiable [[16]](#ref-16).

**Where the canvas sits before an experiment, a design brief, or a PRD is this library's own position, not
a sourced sequence.** No source this research read states what happens after Box 8's smallest experiment
runs. This companion's position is that when that work becomes a real experiment with variants and a
decision rule, a document like `experiment-design-doc` plans it; when the team instead commits to a
concept, `design-brief` hands it to the people who will design it, or the PRD specifies how it works. Box 8
only sketches the shape of a test; it does not plan one, and nothing read here names what takes over.

**A standalone problem statement, where one exists, may feed Box 1, but nothing read here makes that a
rule.** Gothelf's own walkthrough starts from the business problem statement as an input
[[7]](#ref-7), and a team with no such document can equally start the canvas cold. Whether a formal
problem-statement document should feed this box, or a researched persona should formally feed Box 3, is
this library's own judgment to draw rather than something any source states.

**The product vision** sits at a different scale entirely. Where a vision states a whole product's
direction over years, this canvas frames one initiative for a matter of weeks.

## 9. Adaptations

This research found variation in how long a first pass takes and in the medium teams use to capture it,
but it found no adaptation by regulated industry, by methodology beyond Lean UX itself, or by organization
size, and this companion does not invent one. A first pass can take as little as half a day or stretch
across a series of meetings over a couple of weeks, depending on the scope of the initiative
[[19]](#ref-19); one lead business analyst's team completed the whole canvas in about a day on a
fast-moving delivery project [[9]](#ref-9). The medium teams use to fill and keep the canvas varies by what
is practical for the people involved: brown paper photographed and set aside [[9]](#ref-9), or a
whiteboard, digital stickies, a shareable spreadsheet, or a shared board kept current for as long as the
canvas lasts [[8]](#ref-8). The book's own advice for a question the team cannot yet answer is to park it
rather than stall the session [[19]](#ref-19).

## 10. Worked example

`lean-ux-canvas_example.md` fills the canvas for the "Collaborative analysis" initiative named in the FY26
product roadmap's Later lane: a support request that keeps recurring because nobody has shaped it, and
that may belong to the support team rather than to the product itself. It is an unshaped initiative with no
investment behind it yet, which is exactly the ground the canvas is built for, and its solutions box
includes the non-technical, support-team option the canvas's own 2019 widening makes room for.

## References

<a id="ref-1"></a>[1] Jeff Gothelf. "[The Lean UX Canvas](https://jeffgothelf.com/blog/leanuxcanvas/)" (v1 blog post), jeffgothelf.com, 2016. [primary]

<a id="ref-2"></a>[2] Jeff Gothelf. "[The Lean Product Canvas](https://jeffgothelf.com/blog/the-lean-product-canvas/)" (2024 rename post), jeffgothelf.com, 2024. [primary]

<a id="ref-4"></a>[4] Jeff Gothelf. "[Lean UX Canvas V2](https://jeffgothelf.com/blog/leanuxcanvas-v2/)," jeffgothelf.com, 2019. [primary]

<a id="ref-5"></a>[5] Jeff Gothelf. "[Lean Product Canvas (v3) and Lean Strategy Canvas (v1)](https://jeffgothelf.com/wp-content/uploads/2024/11/LeanProduct_canvas_v1-nov2024_FINAL.pdf)" (PDF), jeffgothelf.com, 2024. [primary]

<a id="ref-6"></a>[6] Jeff Gothelf. "[The Hypothesis Prioritization Canvas](https://jeffgothelf.com/blog/the-hypothesis-prioritization-canvas/)," jeffgothelf.com, 2019. [primary]

<a id="ref-7"></a>[7] Jeff Gothelf. "[How to use the Lean UX Canvas](https://jeffgothelf.com/blog/how-to-use-the-lean-ux-canvas/)" (video transcript), jeffgothelf.com, 2021. [primary]

<a id="ref-8"></a>[8] Bryan Elkus. "[Intro to Lean UX Canvas: Defining a Software Solution](https://spin.atomicobject.com/lean-ux-canvas-intro/)," Atomic Object blog, 2019. [practitioner]

<a id="ref-9"></a>[9] Rohela Raouf. "[UX Canvas](https://modernanalyst.com/Community/CommunityBlog/tabid/182/ID/3861/UX-Canvas.aspx)," Modern Analyst Community Blog, 2017. [practitioner]

<a id="ref-10"></a>[10] Jeff Gothelf. "[What's the difference between a user outcome and a business outcome?](https://jeffgothelf.com/blog/difference-between-user-outcome-and-business-outcome/)," jeffgothelf.com, 2023. [primary]

<a id="ref-11"></a>[11] Jeff Gothelf. "[Outcomes are the success criteria for your hypotheses](https://jeffgothelf.com/blog/outcomes-are-the-success-criteria-for-your-hypotheses)," jeffgothelf.com, 2022. [primary]

<a id="ref-12"></a>[12] James Royal-Lawson and Per Axbom. "[Positive user experience](https://uxpodcast.com/positive-user-experience-2)" (UX Podcast, episode 220), 2019. [practitioner]

<a id="ref-13"></a>[13] Creately (Cinergix Pty Ltd). "[Lean UX Canvas: A Practical Tool for the Lean UX Process](https://creately.com/guides/lean-ux-canvas/)." [vendor]

<a id="ref-14"></a>[14] Jeff Patton. "[Opportunity Canvas](https://jpattonassociates.com/opportunity-canvas/)," jpattonassociates.com. [practitioner]

<a id="ref-15"></a>[15] Ash Maurya. "[What is a Lean Canvas?](https://leanspark.ai/learn/what-is-lean-canvas)," LEANSpark / LEANSTACK. [primary]

<a id="ref-16"></a>[16] Jeff Gothelf. "[Creating OKRs with the Lean UX Canvas](https://jeffgothelf.com/blog/creating-okrs-with-lean-ux-canvas/)," jeffgothelf.com, 2021. [primary]

<a id="ref-17"></a>[17] Marty Cagan. "[Lean Canvas vs. Opportunity Assessment](https://www.svpg.com/lean-canvas-vs-opportunity-assessment/)," Silicon Valley Product Group, 2013. [practitioner]

<a id="ref-18"></a>[18] Dean Peters. "[lean-ux-canvas skill, SKILL.md](https://raw.githubusercontent.com/deanpeters/Product-Manager-Skills/main/skills/lean-ux-canvas/SKILL.md)," deanpeters/Product-Manager-Skills (GitHub). [practitioner]

<a id="ref-19"></a>[19] Jeff Gothelf and Josh Seiden. *Lean UX: Designing Great Products with Agile Teams*, third edition. O'Reilly, 2021 (chapters 3 to 13). Print book; no URL. Read from the maintainer's own copy, not retrieved online, and its text is never committed. [primary]
