# Companion: Use Case Specification

> The deep explainer for the use-case-specification bundle. Read this to understand what a use case
> specification is, where its field set comes from, how brief, casual and fully dressed use cases
> differ, and where practitioners disagree about what belongs inside one. The short operator card is
> [`use-case-specification_guide.md`](use-case-specification_guide.md); a fully worked instance is
> [`use-case-specification_example.md`](use-case-specification_example.md). Inline citations like
> [[1]](#ref-1) resolve to the [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A use case specification writes down, for one primary actor and one goal, what the actor and the
system do, step by step, when everything goes right, and what happens at each point where something
can go another way. Alistair Cockburn's own definition states the job directly: "A use case captures a
contract between the stakeholders of a system about its behavior." [[3]](#ref-3). Its numbered main
scenario and its lettered extensions [[1]](#ref-1)[[3]](#ref-3) are what separate it from a user
story's one sentence and from acceptance criteria's pass or fail checks.

The document's weight does not sit in its happy path. Cockburn says plainly that "The greatest value of
the use case does not lie in the main scenario, but in alternative behaviors." [[6]](#ref-6), and Doug
Rosenberg makes the same point from a different angle: "more than half the complexity of the use case
occurs in the alternative courses of action; you're not done when you've written the basic course."
[[18]](#ref-18). It states requirements, not design [[3]](#ref-3)[[24]](#ref-24), and it is not a test
plan: "Use cases are not test plans or test cases. They are missing the data values needed for test
cases." [[6]](#ref-6).

**Its place in this library's own family is a chosen widening, not a reading of an existing
contract.** No family contract admitted this type as written; the `delivery-docs` family contract
gained a sixth membership verb, "elaborates," specifically to hold it
(`docs/internal/contracts/delivery-docs.md`, ADR 0072, the amendment that adopted this type into the
family). The research behind that amendment found that a maintainer could as reasonably have read the
contract as excluding the type (`docs/internal/tier2-specs.md:4877-4883`). This companion presents
"elaborates" as that choice, not as a fact about the world, and states the chain position the contract
gives it in section 8: after the stories a backlog decomposes, and before the acceptance criteria that
confirm them (`docs/internal/contracts/delivery-docs.md:11`).

**No source read for this bundle measured whether writing a use case specification changes a project
outcome.** One academic protocol reports that it "successfully derived two-unit test cases with 100%
basis path coverage, demonstrating complete traceability from functional requirements to unit test
scenarios with one-to-one mapping between control flow paths and test cases" [[26]](#ref-26), which
measures the protocol against its own worked case, not what writing use cases does for a project more
generally. The same paper's observation that "most students operate without granular traceability,
standardized structures, or alternate flow testing" [[26]](#ref-26) describes student work and ties to
no outcome. Cockburn relays one consultant's account of a team that, having listed stakeholders and
interests only after shipping, concluded that "had they simply written down the stakeholders and
interests for each use case early on, they would have avoided an entire category of mistakes"
[[6]](#ref-6); that is one practitioner's story as Cockburn tells it, not a measurement.

**At a glance**
- A use case specification elaborates one primary actor's complete path toward one goal: a numbered
  main success scenario plus the alternative and exception paths that branch off it
  [[1]](#ref-1)[[3]](#ref-3)[[8]](#ref-8).
- It comes in three degrees of formality Cockburn names brief, casual and fully dressed
  [[6]](#ref-6); this library templates only the two heavier of the three (section 4).
- Its value is concentrated in the branches, not the happy path [[6]](#ref-6)[[18]](#ref-18), and it
  states what the system must do, not how it is built [[3]](#ref-3)[[24]](#ref-24).
- Whether use cases have fallen out of favor against user stories is a live, dated argument this
  companion reports rather than settles (section 6).
- Its place in this library's `delivery-docs` family is this library's own choice, stated honestly as a
  widening rather than a fit the contract already had (section 8).

---

## 2. Origins and evolution

Use cases trace to Ivar Jacobson. Use-Case 3.0's own bibliography states that use cases "have been used
to drive the development of software systems since their initial introduction by Ivar Jacobson at
OOPSLA in 1987." [[13]](#ref-13), citing a 1987 paper it calls "The first published paper to describe
Use Cases." [[13]](#ref-13), followed in 1992 by a book it calls "The original book that introduced use
cases to the world." [[13]](#ref-13). Neither the 1987 paper nor the 1992 book was read for this
research; both are known only through Use-Case 3.0's own bibliography entry, so this companion cites
[[13]](#ref-13) for the dates and does not describe either text's own content.

Cockburn's own template work is read directly. His 1998 "Basic Use Case Template" (document TR.96.03a,
"This Version Date: October 26, 1998 Version: 2 Previous Version Date: April 26, 1996" [[2]](#ref-2))
ships a field set with no mention of stakeholders anywhere in it [[1]](#ref-1)[[2]](#ref-2). The
template's own cover page states it is reusable: "You have permission to copy and distribute the
documents as long as you reference the source of the originals." [[1]](#ref-1). Independently, Karl
Wiegers published his own "Use Cases for <Project>" template in 1999 under a similar open license,
"Permission is granted to use, modify, and distribute this document" [[7]](#ref-7), and the Rational
Unified Process shipped its own "Use-Case Specification" template inside its requirements artifact set
[[8]](#ref-8). Three organizations published the same genre of document, each with its own field set; this
research did not establish when RUP's template first shipped.

Cockburn's own thinking kept moving. A pre-publication draft of his book, dated 2000.02.21, already
carries fields the 1998 template does not: a "Stakeholders & Interests" field, and "Minimal Guarantees"
and "Success Guarantees" in place of the 1998 template's single "Failed End Condition"
[[3]](#ref-3). *Writing Effective Use Cases* was published by Addison-Wesley in 2001. Its own preface,
read from Pearson's free sample pages, states that the Stakeholders and Interests idea is new relative
to his earlier work: "led to the explanations in this book and to the Stakeholders and Interests model,
which is a new idea presented here." [[5]](#ref-5). Those same sample pages carry the book's table of
contents and index but not its own fully dressed template box; the index lists only the entry "Use Case
24 (Fully Dressed Use Case Tem-plate), 119-120" [[5]](#ref-5), never the template's own body text.
That newness is relative to the 1998 template, which never uses the word stakeholder at all
[[1]](#ref-1)[[2]](#ref-2); it does not mean the idea arrived late in the book's own writing, because
the pre-publication draft already carries it, both in its template and in its step-by-step writing
process [[3]](#ref-3), and Cockburn's own 2002 retrospective places the idea's emergence around 1997
[[6]](#ref-6). One question this research could not close: whether the published book's own fully
dressed template, printed on the pages the index names, differs in any field from the draft's own
template, printed earlier in the manuscript as "Use Case 7" rather than "Use Case 24"
[[3]](#ref-3). This companion cites the draft for the field list and names it as the draft's, never as
the published book's.

The Unified Modeling Language absorbed use cases as a modeling element later. Girvan's own conference
timeline dates the OOPSLA introduction to 1987 and places use cases' incorporation into UML at 1997
[[21]](#ref-21), and OMG's UML specification (version 2.5.1, formally dated December 2017) still defines
"Actors, UseCases, and subjects" [[15]](#ref-15) as elements of a use case model, with the use case's
own behavior describable "by pre-conditions, post-conditions and natural language text where
appropriate" [[15]](#ref-15), leaving the written narrative's own format unstandardized. Jacobson's own
later work moved toward agile practice: Use-Case 3.0, dated December 2024, describes itself as a guide
to applying use cases "in an agile and scalable fashion" [[13]](#ref-13), and a jointly authored
"Use-Case Foundation" was published the same year, stating that "The amount of detail and the format
used will vary to match your circumstances" [[14]](#ref-14). Girvan's own 2024 slides name a competing
narrative in the same period, that use cases have "fallen out of favour" [[21]](#ref-21); section 6
reports that argument rather than settling it. This bundle's own place in this library dates to
2026-10-15, when ADR 0072 widened the `delivery-docs` family contract to admit it.

---

## 3. Anatomy (section by section)

The full variant carries ten sections, in this order: Title and Actor, Goal in Context, Scope and
Level, Stakeholders and Interests, Preconditions and Trigger, Main Success Scenario, Extensions,
Minimal and Success Guarantees, Related Information, and Open Issues and Schedule. The lean variant
carries five of them, in the same relative order: Title and Actor, Goal in Context, Preconditions and
Trigger, Main Success Scenario, and Minimal and Success Guarantees. Each subsection below names which
variant or variants carry it.

### Title and Actor (lean and full)

**What it is:** the use case's name, stated as a short active verb phrase naming the goal, and the name
of the primary actor who wants that goal. **Why it exists:** every template read opens this way. The
1998 template's own header opens with "Use Case: <number> <the name should be the goal as a short
active verb phrase>", and the same header block names "Primary Actor: <a role name for the primary
actor, or description>" six fields further down [[1]](#ref-1)[[2]](#ref-2). The draft's header also
names the primary actor, after its scope and level fields [[3]](#ref-3). **Beginner note:** name
the use case after the actor's goal, in active-verb form, the way the practitioner reproduction's own
template illustrates it: "Title: <verb + goal, active form> - "Place an order"" [[12]](#ref-12).
**Expert note:** this bundle adds an identifier beyond what the 1998 template carries. The 1998 header
already has a plain number, and three further sources independently ask for one: Wiegers' "Give each
use case a unique numeric identifier, in hierarchical form: X.Y." [[7]](#ref-7), NYU's "Use Case ID"
field [[10]](#ref-10), and Notre Dame's "Each use case should have a unique identifier that can be used
for quick reference and traceability." [[25]](#ref-25). Cockburn's own optional goal-level marking
convention, appending a character to the name [[4]](#ref-4), is a guide-level convention, not a
required field.

### Goal in Context (lean and full)

**What it is:** a longer statement of the actor's goal than the title line gives, including the
circumstances under which the goal normally arises. **Why it exists:** the 1998 template's field reads
"Goal in Context: <a longer statement of the goal, if needed>" [[1]](#ref-1), and this library keeps
that name rather than the draft's later rewording, "Context of use: <a longer statement of the goal, if
needed, its normal occurrence conditions>" [[3]](#ref-3). **Beginner note:** this is the field the
contract's own verb, "elaborates," is organized around: the goal that everything else in the document
serves. **Expert note:** the draft's own addition, "normal occurrence conditions," is read verbatim
here, not as the section's name but as a question the guide asks the author to answer: under what
circumstances does this goal typically arise.

### Scope and Level (full only)

**What it is:** the system under design, stated as a black box, and how large a unit of work the use
case covers. **Why it exists, and why it is full only:** a small or low-ceremony use case does not need
these stated; a project running several use cases at different granularities does. The draft prints
both fields together, "Scope: <design scope, what system is being considered black-box under design>"
and "Level: <one of: Summary, User-goal, Subfunction>" [[3]](#ref-3). **Beginner note:** scope answers
"what system is this use case about," and level answers "how big a slice of work is this." **Expert
note:** the guide uses the draft's own middle-level name, "User-goal," rather than the 1998 template's
"Primary task" [[1]](#ref-1)[[3]](#ref-3); section 6, item 4, names this as a live naming disagreement
across Cockburn's own templates, not a correction of one by the other. Scope's own black-box framing,
read against the draft's own distinction, "a black-box use case does not discuss the internal structure
of the system under discussion, while a white-box use case does." [[3]](#ref-3), is also this bundle's
main tool for keeping design out (section 6, item 11, and section 8).

### Stakeholders and Interests (full only)

**What it is:** a list of everyone with a vested interest in how the use case behaves, including people
who never interact with the system directly, and what each of them wants from it. **Why it exists, and
why it is full only, at medium confidence:** the 1998 template never mentions a stakeholder
[[1]](#ref-1)[[2]](#ref-2), so this section rests entirely on Cockburn's later work: the draft's own
field, "Stakeholders & Interests: <list of stakeholders and key interests in the use case>"
[[3]](#ref-3), and his 2002 article, which lists "fields for stakeholders" first among the fully
dressed template's own fields [[6]](#ref-6). A stakeholder, in the draft's own words, "is someone with a
vested interest in the behavior of the use case, even if they never interact directly with the system."
[[3]](#ref-3). **Beginner note:** list a stakeholder even if they never touch the system, such as a
finance team that cares how an order use case handles a refund. **Expert note:** the draft's own
writing process makes the rest of the fully dressed document answer to this list: "7. Capture
stakeholders and interests, preconditions and guarantees. The system will ensure the preconditions and
guarantee the interests." and "8. Write the main success scenario (MSS). Use 3 to 9 steps to meet all
interests and guarantees." [[3]](#ref-3). In this library's own full variant the section sits between
Scope and Level and Preconditions and Trigger, following the draft's own field order. No source
independent of Cockburn's own lineage was found carrying this field; the practitioner reproduction that
also carries it [[12]](#ref-12) is itself built from Cockburn's own template and corroborates nothing
beyond it.

### Preconditions and Trigger (lean and full)

**What it is:** what must already be true of the world before the use case can start, and the event
that actually starts it. **Why it exists:** every template read that carries a precondition field names
it this way. The 1998 template: "Preconditions: <what we expect is already the state of the world>" and
"Trigger: <the action upon the system that starts the use case, may be time event>" [[1]](#ref-1); the
draft keeps the same field under "Precondition: <what we expect is already the state of the world>" and
rewords the trigger slightly to "Trigger: <what starts the use case, may be time event>"
[[3]](#ref-3); Wiegers asks the author to "List any activities that must take place, or any conditions
that must be true, before the use case can be started." [[7]](#ref-7); and RUP defines the term
directly, "A precondition of a use case is the state of the system that must be present prior to a use
case being performed." [[8]](#ref-8). **Beginner note:** a precondition is a fact about the world, not a
step the actor takes; the trigger is the one event that starts the clock. **Expert note:** a trigger can
be a time event rather than an action, per the 1998 field's own wording [[1]](#ref-1); do not assume
every use case starts with a user clicking something.

### Main Success Scenario (lean and full)

**What it is:** the numbered sequence of steps, from trigger to goal delivery, that plays out when
nothing goes wrong. **Why it exists:** this is the section every template read carries in some form, as
the 1998 template's own placeholder, "<put here the steps of the scenario from trigger to goal
delivery, and any cleanup after>" [[1]](#ref-1), and RUP's "2.1 Basic Flow" [[8]](#ref-8). **Beginner
note:** write each step to "Show a goal succeeding. Highlight the actor's intention, not the user
interface details. Have an actor pass information, validate a condition, or update state."
[[3]](#ref-3), alternating actor and system the way Sehlhorst describes it, "Reading a use case should
be like watching a tennis match, with activities being performed alternately by the user and the
system." [[19]](#ref-19); each step reflects "one activity and one activity only" and is "written in
the active voice" [[22]](#ref-22). **Expert note:** keep it short. Cockburn's own writing-process step
asks for "3 to 9 steps" [[3]](#ref-3), and his 2002 retrospective reports that he is "yet to write a
main success scenario longer than nine steps" [[6]](#ref-6). The lean variant asks for a line of prose
for each known deviation inside this section rather than a separate Extensions section; section 4 explains why that, and not the full Extensions treatment, is this library's own
reading of the casual form.

### Extensions (full only)

**What it is:** the branches off the main success scenario, each naming the condition that triggers it
and where it rejoins the scenario, succeeds separately, or fails. **Why it exists, and why it is full
only:** a casual, low-ceremony use case covers its deviations in prose inside the main narrative; a
fully dressed one separates them so each can be found, numbered and checked on its own. The 1998
template's own placeholder for an extension, "<step altered> <condition> : <action or sub.use case>"
[[1]](#ref-1), and the draft's own numbering convention, "the numbering convention in the extensions
sections involving combinations of digits and letters (e.g., 2a, 2a1, 2a2 and so on)" [[3]](#ref-3),
both treat extensions as branches inside one document, not as links to other documents. **Beginner
note:** brainstorm every condition the system can detect before writing the handling steps: "9.
Brainstorm and exhaustively list the extension conditions. Include all that the system can detect and
must handle." then "10. Write the extension-handling steps. Each will ends back in the MSS, at a
separate success exit, or in failure." [[3]](#ref-3). **Expert note:** this bundle keeps alternative and
exception paths inside one Extensions section rather than splitting them, following RUP's own single
"2.2 Alternative Flows" section [[8]](#ref-8) and the foundation's own framing, "A list of all the
special cases, alternative paths, optional steps, and errors that need to be handled."
[[14]](#ref-14), over Wiegers' and NYU's own separate numbering of alternative courses and exceptions
[[7]](#ref-7)[[10]](#ref-10); section 6, item 8, names the split. RUP's own "Extension Points" heading
is not cited for this section: an extension point marks where a *different* use case may extend this
one [[8]](#ref-8)[[15]](#ref-15), which belongs to the include-and-extend relationship this bundle does
not template (section 6, item 5), not to a branch inside this document.

### Minimal and Success Guarantees (lean and full)

**What it is:** what stays true no matter how the use case ends, paired with what is additionally true
when it ends successfully. **Why it exists, and why the name changes here:** the 1998 template's own
field, "Failed End Condition: <the state of the world if goal abandoned>" [[1]](#ref-1), is a property
of the failure exit alone. The draft replaces it with two paired fields: "Minimal Guarantees: <how the
interests are protected under all exits>" and "Success Guarantees: <the state of the world if goal
succeeds>" [[3]](#ref-3), and the book's own table of contents confirms both names, "6.2 Minimal
Guarantees" and "6.3 Success Guarantee" [[5]](#ref-5). An editorial note on the same mirror that carries
the 1998 template records the rename directly: "(Note: The book Writing Effective Use Cases made a
couple of small changes to these templates, most notably renaming "Failed End Condistion" to the more
correct "Minimal Guarantee" and "Subvariation" to the more correct "Technology and Data Variations
List."" [[1]](#ref-1) (spelling and punctuation as printed on the source page). **Beginner note:** a
minimal guarantee holds on every exit, success included, the way OpenUP's own checklist states it, "(A
Minimal Guarantee represents a condition that will be true when the use case ends, regardless of how it
terminates.)" [[24]](#ref-24); a success guarantee holds only "when the use case ends successfully,
regardless of which path it takes" [[24]](#ref-24). **Expert note:** this is the field a template that
asks only for success and failure end conditions never asks: what must stay true however the case ends,
success included. The section's own WHAT comment names "postconditions" as the term the other read
templates use for roughly this content, since Wiegers, RUP and NYU each ask for a postcondition field
without the minimal-versus-success split [[7]](#ref-7)[[8]](#ref-8)[[10]](#ref-10).

### Related Information (full only)

**What it is:** an open slot for whatever project-specific facts a use case needs beyond its core
fields: priority, performance target, frequency, channel, related use cases, technology and data
variations, and secondary actors. **Why it exists, and why it is full only:** a casual use case carries
none of this; a fully dressed one, per the draft's own definition, adds "project annotation
information" [[3]](#ref-3) beyond the header fields every variant shares. The 1998 template's own
closing block carries this whole set: "RELATED INFORMATION (optional) Priority: <how critical to your
system / organization> Performance Target: <the amount of time this use case should take> Frequency:
<how often it is expected to happen> Superordinate Use Case: <optional, name of use case that includes
this one> Subordinate Use Cases: <optional, depending on tools, links to sub.use cases> Channel to
primary actor: <e.g. interactive, static files, database> Secondary Actors: <list of other systems
needed to accomplish use case> Channel to Secondary Actors: <e.g. interactive, static, file, database,
timeout>" [[1]](#ref-1). **Beginner note:** a non-functional requirement that applies to many use
cases, not just this one, is better linked from here than copied into it; OpenUP's own checklist asks,
"Are these nonfunctional requirements applicable to many use cases?" and answers, "consider capturing
them in the supporting Requirements Specification to simplify maintenance" [[24]](#ref-24). **Expert
note:** two further lines are homed here rather than given their own sections. A technology and data
variations line, naming a channel or device difference so the main scenario's own steps can stay at the
level of intention, traces to the 1998 template's own "SUB-VARIATIONS <put here the sub-variations that
will cause eventual bifurcation in the scenario>" field [[1]](#ref-1), later renamed, per the editorial
note quoted above, to "Technology and Data Variations List" [[1]](#ref-1); the draft's own template carries a field
of the same name [[3]](#ref-3). A secondary
actors line, naming anyone or anything involved in the use case without gaining direct benefit from it,
traces to the 1998 field "Secondary Actors: <list of other systems needed to accomplish use case>"
[[1]](#ref-1) and Notre Dame's own definition, "A Secondary actor is anyone or anything that is involved
in achieving a use case but does not gain direct benefit from the use case." [[25]](#ref-25). The
draft's own prose, read in full but not submitted as a quotation, says use cases do not carry
performance requirements, priority, business rules, UI design or data descriptions, which belong in
their own chapters of the requirements and are cross-linked from the use cases [[3]](#ref-3); that sits
awkwardly beside the 1998 block's own Priority and Performance Target fields. This companion reads
those two fields as exactly the "project annotation information" a fully dressed use case adds beyond
the leaner header [[3]](#ref-3), not as a contradiction to resolve.

### Open Issues and Schedule (full only)

**What it is:** unresolved questions the use case still carries, and the release or date it is due by.
**Why it exists, and why it is full only:** the 1998 template's own closing block carries both fields:
"OPEN ISSUES (optional) <list of issues about this use cases awaiting decisions>" and "SCHEDULE Due
Date: <date or release of deployment>" [[1]](#ref-1), and Wiegers asks for the same content in
different words, "List any additional comments about this use case or any remaining open issues or TBDs
(To Be Determineds) that must be resolved." [[7]](#ref-7). **Beginner note:** name an open question and
who owns resolving it, not just that one exists. **Expert note:** the draft's own template carries
neither field [[3]](#ref-3), so this section rests on the 1998 template and Wiegers alone; it is the one
section with no corroboration from Cockburn's own later work. Wiegers' own separate Assumptions field is
not adopted here; an assumption is asked for under this section instead, since no source beyond
Wiegers' own template carries a dedicated field for it [[7]](#ref-7).

---

## 4. Variants and sizing

Cockburn names three degrees of formality: "In Writing Effective Use Cases, I name three degrees of
detail in writing use cases: brief, casual, and fully dressed." [[6]](#ref-6). A brief use case is "a
2-6 sentence description of the use case behavior, mentioning only the most significant activity and
failures." [[3]](#ref-3); his own 2002 article gives a narrower range, "two to four sentences"
[[6]](#ref-6). This bundle does not fix a sentence count for either range, and the brief form sits
below anything this library templates: a form this short needs no document of its own.

A casual use case "is one written in simple, paragraph, prose style. It is likely to be missing project
information associated with the use case, and is likely to be less rigorous in its description than a
fully dressed use case." [[3]](#ref-3); the 2002 article calls it "a few paragraphs of text, covering
the items mentioned above" [[6]](#ref-6). A fully dressed use case "is written with one of the full
templates, identifying actors, scope, level, trigger condition, precondition, and all the rest of the
template header information, plus project annotation information." [[3]](#ref-3).

**This library ships `lean` for casual and `full` for fully dressed, and that mapping is this
library's own position, not a reading any source states.** Cockburn's own casual form is prose
paragraphs [[3]](#ref-3)[[6]](#ref-6); the lean template keeps numbered steps instead, because the
`delivery-docs` contract's own verb admits "a main success scenario, stated as a numbered sequence of
steps" (`docs/internal/contracts/delivery-docs.md:15`). Lean is casual's nearest equivalent in
coverage, not in form: it drops the project annotation information and the separate Extensions section
the way casual does, while keeping the numbered steps casual would write as prose, and it gives each known
deviation one line of prose inside the Main Success Scenario section rather than opening
Extensions for it.

The draft argues that one template is never enough for a whole project: "There must be at least two, a
casual one for low-ceremony projects, and a fully dressed one for higherceremony projects."
[[3]](#ref-3), and shows the same scenario written both ways, "USE CASE 4: BUY SOMETHING (CASUAL
VERSION)" against "USE CASE 5: BUY SOMETHING (FULLY DRESSED VERSION)" [[3]](#ref-3). The jointly
authored foundation states the same idea as a general rule: "The amount of detail and the format used
will vary to match your circumstances" [[14]](#ref-14). A practitioner reproduction of Cockburn's field
list, not Cockburn's own text, gives the same advice in its own words: "Keep most UCs at brief or
casual. Fully-dress only the important ones." [[12]](#ref-12).

To grow a lean use case into a full one, the draft's own writing order is the sourced path: "Work
breadth-first, from lower precision to higher precision. Precision Level 1: Primary actor's name and
goal Precision Level 2: The use case brief, or the main success scenario Precision Level 3: The
extension conditions Precision Level 4: The extension handling steps" [[4]](#ref-4). The guide gives
Cockburn's own names (brief, casual, fully dressed) beside this library's own (lean, full) rather than
treating them as synonyms.

---

## 5. Methodology lineage

The catalog this bundle started from tied the type to Waterfall, the Unified Process and RUP by
default. This research does not support that as a requirement, and recommends `methodology-agnostic`
instead, at medium-high confidence.

**No source ties the type to Waterfall as a requirement.** Use-Case 3.0 names waterfall teams only as
one mode among several it supports: "The two most common types of work item we see in use now are user
stories (for agile teams) and Tasks (for waterfall project teams)." [[13]](#ref-13).

**The Unified Process and RUP are a lineage, not a requirement.** RUP publishes its own use-case
specification template [[8]](#ref-8), sitting inside RUP's own requirements artifact set under its
use-case model. Jacobson himself "is a father of components and component architecture, use cases,
aspect-oriented software development, modern business engineering, the Unified Modeling Language and
the Rational Unified Process." [[13]](#ref-13), and his co-author Ian Spence "specialized in the agile
application of the Unified Process" and is "a certified RUP practitioner" [[13]](#ref-13). Girvan's own
timeline records use cases being incorporated into UML and, by extension, into IBM's RUP
[[21]](#ref-21), and Cockburn's own draft lists the RUP template as one format among several, not the
required one [[3]](#ref-3). These are ties of lineage and authorship; no source read states that a use
case specification requires RUP or the Unified Process.

**Agile practice claims the type directly.** Use-Case 3.0 states its own purpose as applying use cases
"to capture system requirements in an agile and scalable fashion." [[13]](#ref-13); the same source
states that the development of use cases should be done "in some cases in a lightweight and agile way,
in other cases in a rigorous way." [[13]](#ref-13); Scott Ambler, writing from agile modeling, warns
that "It is very easy for use case modeling to become un-agile." [[22]](#ref-22); and Notre Dame's own
inventory step names a sprint "if using an Agile development methodology" [[25]](#ref-25).

**The strongest reading is methodology-neutral.** Use-Case 3.0 states its own neutrality directly:
"Use-Case 3.0 will support, focus and complement whatever planning, work management and development
approaches your teams have selected." [[13]](#ref-13). A text search of the raw pages behind this
research found none of waterfall, agile, Unified Process, RUP or Scrum anywhere in the 1998 template
[[1]](#ref-1), the Wiegers template [[7]](#ref-7), the Use-Case Foundation [[14]](#ref-14) or the UML
specification [[15]](#ref-15). The foundation's own first principle, "1. Use Cases apply to systems of
all types and sizes: businesses, IT systems, physical systems or any combinations thereof."
[[14]](#ref-14), reads as a statement about kinds of system rather than a methodology disclaimer, so
this recommendation rests on [[13]](#ref-13) and on the silence of the other four sources, not on that
principle.

---

## 6. Debates and contested boundaries

**1. Stories versus use cases: the shapes differ, and the sources disagree about which to reach for.**
Mike Cohn argues for stories: "User stories typically, but not always, and not in every case, are the
best choice for teams using Scrum" [[17]](#ref-17), because "Use cases are often too large to estimate
usefully." [[17]](#ref-17), and because a story "is a placeholder for a future conversation"
[[17]](#ref-17). Carlton Nettleton reports a camp that "felt use cases were too heavyweight"
[[23]](#ref-23) and relays Cockburn's own distinction for the other side: "A use case provides a
contextual view of what is to be built, serving to bind the organization together, among other
things." [[23]](#ref-23), adding his own view that "their absence is a sign that a software project is
in trouble" [[23]](#ref-23). Girvan lists "Use cases are the same as user stories" under a heading of
myths [[21]](#ref-21) and quotes Cockburn directly from 2024: "Use Cases have structure and cease to be
useful if at too low a level, whereas user stories can decompose forever" [[21]](#ref-21). Use-Case 3.0
treats stories as one kind of work item a use case can feed, not as a competitor
[[13]](#ref-13). This library's own `user-stories` companion already states the boundary from the
story's own side, and its guide already routes a reader who needs "exhaustive actor-system flows" to
this bundle (`templates/user-stories/user-stories_guide.md:15`). This bundle takes neither camp's side.

**2. Whether use cases are out of fashion.** This claim is time-bound, carried by dated camps, and
settled by nothing measured. Girvan's own 2024 slide, headed "Why use cases have fallen out of favour"
[[21]](#ref-21), names "Over complicated use within UML" [[21]](#ref-21) and then the Agile Manifesto
and the popularization of user stories, with a timeline dating use cases to 1987, their incorporation
into UML to 1997, the Agile Manifesto to 2001 and the popularization of user stories to 2005
[[21]](#ref-21). The same deck records a counter-move: a jointly authored Use-Case Foundation published
in 2024 [[21]](#ref-21), which Use-Case 3.0 confirms independently: "The Use-Case Foundation principles
were published in 2024" [[13]](#ref-13). Nettleton's own push-back piece dates to 2014
[[23]](#ref-23); Cohn's own page states it was "Last updated April 23rd, 2026" [[17]](#ref-17). No
source read for this bundle measured how many teams actually write use cases at any date. This
companion reports that the claim is made, and by whom, and states neither decline nor resurgence as a
fact.

**3. What belongs inside a use case: three separate questions, with three separate answers.**
- *User interface detail is genuinely contested.* Against including it: Cockburn's own step-writing
  rule, "Highlight the actor's intention, not the user interface details." [[3]](#ref-3)[[4]](#ref-4);
  his own ranking of the two costliest mistakes, "including too many details and including UI
  specifics." [[6]](#ref-6); Laura Brandenburg's "By far the most common mistake we see in use cases is
  that they use the language of the user interface to talk about the user behavior."
  [[20]](#ref-20); OpenUP's checklist question, "Is each step technology-independent? Is it free of
  technical details and inadvertent design decisions?" [[24]](#ref-24). For including it, in a
  qualified form: Rosenberg names interface objects that "are identified by describing system usage
  from the user manual perspective" [[18]](#ref-18) and advises to "write the user manual before you
  write the code" [[18]](#ref-18); Ambler states that "A formalized system use case refers to specific
  user interface components-such as screens, HTML pages, or reports" [[22]](#ref-22), a position he
  draws by *kind* of use case (a formal system use case, not an essential or business one) that the
  other sources do not share. Both "most common mistake" claims above are their own authors' judgments,
  not measurements.
- *Business rules converge on reference-by-identifier, with the text kept elsewhere.* Cockburn's own
  writing is not fully consistent here. His 2002 article lists business rules among the fully dressed
  template's own fields: "The fully dressed use case features the long template with fields for
  stakeholders, minimum guarantees, postconditions, business rules, performance constraints, and so
  on." [[6]](#ref-6). His draft, read in full but not submitted as a quotation, instead says use cases
  do not contain business rules, which belong in their own chapter of the requirements and are
  cross-linked from the use cases [[3]](#ref-3), and the draft's own fully dressed template carries no
  business-rules field at all [[3]](#ref-3), matching the 1998 template [[1]](#ref-1), Wiegers
  [[7]](#ref-7), RUP [[8]](#ref-8) and NYU [[10]](#ref-10), none of which print one either. Ambler's own
  formal use case refers to a rule by its identifier from the step that applies it, "because business
  rules reflect essential characteristics of your domain that your system must implement"
  [[22]](#ref-22), writing the rule's text inline only "For very simple systems without very many
  complex business rules" [[22]](#ref-22). Girvan's own worked example refers to a rule the same way, by
  identifier, listed below the use case: "BR1 - No more than 100 people allowed in library at any time"
  [[21]](#ref-21). Notre Dame keeps rules in a catch-all section for "requirements that are not directly
  related to the actions" [[25]](#ref-25). This bundle does not template a business-rules section; it
  asks, in its guide's own rubric, that a step enforcing a rule name it by identifier and say where its
  text lives.
- *Data definitions belong elsewhere, and no source read says otherwise.* Brandenburg lists "Specific
  data elements or data tables" among the technical details to keep out [[20]](#ref-20), and
  recommends that "a best practice is to use a data dictionary or data map to analyze the data
  requirements." [[20]](#ref-20). Cockburn's own draft excludes data descriptions from the use case
  [[3]](#ref-3), and Girvan's own comparison table excludes data as well [[21]](#ref-21). This library
  routes a reader who needs field-level definitions to `data-dictionary`.

**4. Goal levels are named differently across Cockburn's own templates, and absent outside them.** The
draft names three levels: "User-goals (blue, sea-level )", "Summary level (white, cloud / kite )" and
"Subfunctions (indigo/black, underwater /clam )" [[3]](#ref-3). The user goal is "the goal of greatest
interest," sized at "One person, one sitting (2-20 minutes)." [[3]](#ref-3); subfunctions should be
included "only as you have to" [[3]](#ref-3). The 1998 template names the middle level differently,
"Level: <one of: Summary, Primary task, Subfunction>" [[1]](#ref-1), against the draft's "Level: <one
of: Summary, User-goal, Subfunction>" [[3]](#ref-3). An optional marking convention appends a character
to the use case name for the same purpose [[4]](#ref-4). Design scope is a separate axis entirely: "A
business use case has the enterprise as its design scope." against "A system use case has a computer
system as its design scope." [[3]](#ref-3). Wiegers [[7]](#ref-7), RUP [[8]](#ref-8) and NYU
[[10]](#ref-10) carry no level field at all. Ambler's own essential-versus-system distinction
[[22]](#ref-22) is read here as a third, separate axis, about how much technology a use case names, and
this companion does not merge it with either goal level or design scope. The guide uses the draft's own
names (user-goal, summary, subfunction).

**5. Include and extend are a relationship between use cases, not a section of one.** UML defines both
formally as relationships: "Include is a DirectedRelationship between two UseCases, indicating that the
behavior of the included UseCase (the addition) is inserted into the behavior of the including UseCase
(the includingCase)." [[15]](#ref-15), and "An Extend is a relationship from an extending UseCase (the
extension) to an extended UseCase (the extendedCase) that specifies how and when the behavior defined
in the extending UseCase can be inserted into the behavior defined in the extended UseCase."
[[15]](#ref-15), with the format left open: "UseCases may be specified in various formats such as
natural language, tables, trees, etc." [[15]](#ref-15). RUP gives the extend relationship its own
section, "6. Extension Points" [[8]](#ref-8); NYU folds it into its own extensions section instead,
which "presents those use cases that have an extends relation with the current use case"
[[10]](#ref-10). Cockburn's own extensions are branches inside one document, using "the numbering
convention in the extensions sections involving combinations of digits and letters (e.g., 2a, 2a1, 2a2
and so on)" [[3]](#ref-3), and a branch may hand off to a separate use case entirely from inside a step:
"<step altered> <condition> : <action or sub.use case>" [[1]](#ref-1). Wiegers carries a separate
Includes field [[7]](#ref-7). No source read names overuse of include or extend as a named failure
mode. **This library's own position:** one Extensions section, in Cockburn's own numbering; a link to
another use case sits inside the step that calls it, or in Related Information; no separate Extension
Points section.

**6. The methodology question is covered on its own in section 5.**

**7. The "use case model" alias names the whole set; UML's diagram is one way to draw it.** In the
sources that use the phrase, a use case model is a system's whole set of use cases and actors: RUP
files its own specification template inside its use-case model artifact [[8]](#ref-8), and Use-Case 3.0
defines a use-case model, in substance, as the model that captures and visualizes all the useful ways
to use a system [[13]](#ref-13). UML itself specifies the elements, "Actors, UseCases, and subjects"
[[15]](#ref-15), and the diagram, "A UseCase is shown as an ellipse, either containing the name of the
UseCase or with the name of the UseCase placed below the ellipse." [[15]](#ref-15), while allowing the
behavior itself to be described by "natural language text where appropriate" [[15]](#ref-15). Whether
the diagram matters is itself contested: Martin Fowler argues it does not, "these diagrams are of
little value - the key value of use cases lies in the text which is not standardized in UML. So when
you do use cases put your energy into the text." [[16]](#ref-16), against UML's own clause, which
standardizes the diagram and leaves the text unstandardized. Girvan lists "Use cases are models as in
use case diagram" among her own named myths [[21]](#ref-21). This companion reads a use case model as a
system's full set of use cases and actors, which UML draws as a use case diagram, and this bundle
templates the written specification of one use case inside such a model, never the diagram itself. The
diagram stays out of this library's scope under ADR 0030 (templating scope: Markdown documents), as
ADR 0072 records.

**8. Alternative and exception paths: one section, or two.** Wiegers numbers them apart, alternative
courses as "X.Y.AC.1" and exceptions as "X.Y.EX.1" [[7]](#ref-7), and NYU gives exceptions their own
section, "Exceptions: {This section describes all error conditions that can arise in the use case.}"
[[10]](#ref-10). RUP folds both into a single "2.2 Alternative Flows" [[8]](#ref-8); Cockburn folds both
into one Extensions section [[3]](#ref-3); and the jointly authored foundation lists "all the special
cases, alternative paths, optional steps, and errors that need to be handled" [[14]](#ref-14) under one
heading. This bundle's single Extensions section follows Cockburn, RUP and the foundation.

**9. The W3C eGovernment template shares the name and not the genre.** It asks the author to "Define
the problem that the standard aims to solve and proposed benefits." and to reach "A conclusion on
whether the use case has the critical mass for recommendation, and a justification" [[9]](#ref-9). It
has no actor field, no conditions and no steps; it is a standards-opportunity proposal, not an
actor-and-scenario specification. It does not count toward any claim in this companion about which
sections a use case specification template carries.

**10. The stakeholder model's own provenance.** The preface's claim that Stakeholders and Interests is
"a new idea presented here" [[5]](#ref-5) is new relative to the 1998 template, which never uses the
word stakeholder at all [[1]](#ref-1)[[2]](#ref-2). It does not mean the idea arrived late in the
published book's own writing: the pre-publication draft already carries "Stakeholders & Interests" in
both its template and step 7 of its own writing process [[3]](#ref-3), and Cockburn's 2002 article
places the idea's own emergence around 1997 [[6]](#ref-6).

**11. Distinctness from this bundle's four delivery-docs siblings stays contested, not settled.** The
boundaries against `acceptance-criteria`, `epic`, `prd` and `test-case` are drawn from their own
headings and from this library's own shipped boundary sentence
(`user-stories_companion.md:151-153`), not from a flow-by-flow audit of their content. This companion
does not claim a clean, settled boundary against any of the four. One boundary, against `sdd`, now has
sources on both sides where this library had previously named it as the library's own unsourced
position. For keeping design out of a use case: Brandenburg states that technical detail is "best saved
for a technical design document." [[20]](#ref-20); Cockburn's own draft separates the two kinds of use
case by whether design is visible, "a black-box use case does not discuss the internal structure of the
system under discussion, while a white-box use case does." [[3]](#ref-3); and both of his own templates
define Scope as the system "black-box under design" [[1]](#ref-1)[[3]](#ref-3). Against a clean line:
Cockburn himself concedes the form can carry design, "As design documentation, the use case describes:
the user does this; some first component does a set of things" [[6]](#ref-6). This companion states
the black-box rule as the boundary this bundle follows, and names a white-box use case written as
design documentation as a use the form itself permits and this bundle does not template.

**12. Several sources are time-bound and should be read with their date.** Cohn's own page is revised
in place and currently says "Last updated April 23rd, 2026" [[17]](#ref-17). Use-Case 3.0 is version
1.00 of December 2024 [[13]](#ref-13). The practitioner reproduction of Cockburn's field list is a
versioned package, 0.1.0 [[12]](#ref-12). ArgonDigital's own page is a vendor page [[11]](#ref-11). The
W3C template is an archived wiki page last modified in December 2008 [[9]](#ref-9).

---

## 7. Anti-patterns and failure modes

**Beginner-level failures.** Scott Sehlhorst's own top-ten list names several that recur in early
drafts: "Unanticipated error conditions. The error conditions are explicitly called out in a formal use
case as exception courses. When we fail to think about how things can go wrong, we take a bad situation
(an error) and make it worse by leaving our users with no reasonable way to deal with the errors."
[[19]](#ref-19); "Overlooking system responses. When people use computers, the computers respond. ...
Reading a use case should be like watching a tennis match, with activities being performed alternately
by the user and the system." [[19]](#ref-19); and "Undefined actors. Novice and expert users have
different ways of using an application." [[19]](#ref-19). Brandenburg's own list of mistakes names a
related pair: inconsistent terms, "A final mistake that can cause significant confusion is when BAs use
terms inconsistently." [[20]](#ref-20), and a use case that drifts outside its own goal, "A common
mistake is to include steps that happen before the pre-conditions, after the post-conditions, or are
otherwise unrelated to the user's goal in the use case. This mistake is an indicator that the use case
needs to be split into more than one use case." [[20]](#ref-20).

**The costliest and most common mistakes, by Cockburn's own account.** "There are many kinds of
mistakes a use case writer can make. The two most common and most costly to the project are including
too many details and including UI specifics." [[6]](#ref-6). Brandenburg's own survey agrees on the UI
mistake: "By far the most common mistake we see in use cases is that they use the language of the user
interface to talk about the user behavior." [[20]](#ref-20), and "Using user interface details leads to
ambiguity." [[20]](#ref-20). Both "most common" claims are their own authors' stated judgments, not a
measured count, and this companion repeats them as such rather than as settled fact.

**A quality checklist, independent of either template's own field list.** OpenUP's "Checklist: Use
Case" asks a reviewer to confirm each step is "technology-independent" and "free of technical details
and inadvertent design decisions" [[24]](#ref-24), and to check the minimal-versus-success guarantee
distinction directly: whether a minimal guarantee holds "when the use case ends, regardless of how it
terminates" [[24]](#ref-24), and whether a success guarantee holds "when the use case ends
successfully, regardless of which path it takes" [[24]](#ref-24).

**A named failure of scope, not of a single step.** Sehlhorst names a boundary failure as its own
mistake, "Out of scope use cases. If we don't define the system boundaries, or scope of our effort, we
risk wasting a lot of time and money documenting irrelevant processes." [[19]](#ref-19), alongside a
shorter list of further named failures this research did not expand beyond their labels:
"Inconsistency. Incorrectness. Wrong priorities. Implementation cues. Broken traceability."
[[19]](#ref-19).

**A named myth about what a use case even is.** Girvan lists "Use cases are the same as user stories"
[[21]](#ref-21) and "Use cases are models as in use case diagram" [[21]](#ref-21) directly as myths,
under a slide heading naming them as misconceptions, not as positions she endorses. Section 6, items 1
and 7, read each claim in full.

---

## 8. Relationships to other artifacts

**Chain position.** This bundle sits between the user stories a product backlog decomposes and the
acceptance criteria that confirm a unit of work, per the `delivery-docs` family contract: "a use case
specification elaborates one actor's full path through the system to reach a goal, including
alternative and exception flows, acceptance criteria confirm it"
(`docs/internal/contracts/delivery-docs.md:11`). This library's own `user-stories` guide already routes
a reader who needs "exhaustive actor-system flows" to this bundle
(`templates/user-stories/user-stories_guide.md:15`), naming content this library had not yet shipped at
the time that line was written.

**Downstream into tests.** Two academic sources, independent of each other and twenty-two years apart,
treat the use case's own flows as a source tests can be derived from mechanically: a 2026 test-first
protocol reports "one-to-one mapping between control flow paths and test cases" [[26]](#ref-26), and a
2004 paper on scenario-based testing states that "Tests are derived from use case scenarios via
continuous refinement." [[27]](#ref-27) (the 2004 paper's own abstract and record page were read; its
full text was not retrieved for this research). This is what `acceptance-criteria` and `test-case` do
with this document downstream, and Cockburn's own observation that use cases "are missing the data
values needed for test cases" [[6]](#ref-6) names why they remain separate documents rather than one.

**`sdd` (design): kept out by a black-box rule, not by a clean line.** Section 6, item 11, states the
argument on both sides in full. This bundle's own working rule follows Cockburn's own black-box framing
[[1]](#ref-1)[[3]](#ref-3): a use case describes the system's behavior from outside it, and a reader
wanting how that behavior is implemented wants `sdd` instead. Cockburn's own concession that the form
can carry design documentation [[6]](#ref-6) means a white-box use case is something the form permits,
not something this companion claims never happens; this bundle templates only the black-box reading.

**`data-dictionary`: field-level meaning lives there, not here.** Section 6, item 3, states the full
argument; Brandenburg's own recommendation to use "a data dictionary or data map to analyze the data
requirements" [[20]](#ref-20) is this bundle's own routing rule for a reader who needs field
definitions.

**`user-flow-task-flow`: the nearest neighbor this bundle keeps out, without deciding its own
placement.** The `delivery-docs` contract's own amendment states this directly: the "elaborates" verb
"does not admit a diagram, a board, or a live tool schema," and names `user-flow-task-flow`, whose
aliases are "flow diagram" and "wireflow," as the nearest neighbour kept out, with that type's own
placement in the library "deferred rather than decided here"
(`docs/internal/contracts/delivery-docs.md:15`).

**`qa-docs`'s `test-case`: checks a path, this bundle specifies one.** The same contract amendment
draws this line explicitly: this bundle's verb "does not admit a document that checks a path rather
than specifying it, which `qa-docs` carries as `test-case`"
(`docs/internal/contracts/delivery-docs.md:15`).

**The use case model and its UML diagram: a larger artifact this bundle does not template.** Section 6,
item 7, states the full argument. A use case model is the whole set of a system's use cases and
actors, which UML draws as a diagram; this bundle templates the written specification of one use case
inside such a model, and the diagram itself stays out of this library's scope under ADR 0030, as ADR
0072 records.

---

## 9. Adaptations

- **Low-ceremony or early-stage work.** The draft's own guidance is to use a casual form for a
  low-ceremony project [[3]](#ref-3); this library's own lean variant is the nearest equivalent, keeping
  numbered steps where Cockburn's casual form writes prose (section 4).
- **Higher-ceremony, critical or complex use cases.** The draft asks for a fully dressed template on
  higher-ceremony projects [[3]](#ref-3); the practitioner reproduction of Cockburn's field list gives
  the same advice in its own words, to "Fully-dress only the important ones." [[12]](#ref-12). This
  library's own full variant is sized for this case.
- **Agile and scalable delivery.** Use-Case 3.0 states its own purpose as applying use cases "in an
  agile and scalable fashion" [[13]](#ref-13), and the jointly authored foundation names incremental
  delivery directly: "A use case can be implemented in stages: develop and put into place some key
  scenarios of a use case early to capture value and feedback, add less used or less critical scenarios
  over time strategically." [[14]](#ref-14).
- **A project running several related use cases.** Related Information's own superordinate and
  subordinate use case fields [[1]](#ref-1), and Notre Dame's own master inventory step before any one
  use case is written [[25]](#ref-25), are the sourced tools for this case; this library does not
  template the inventory itself, which is the use case model this bundle keeps out of scope (section 6,
  item 7, and section 8).
- **No source read for this bundle addresses solo authorship versus a team writing use cases together
  as a distinct practice**, so this companion names no adaptation for it rather than inventing one.

---

## 10. Worked example

`use-case-specification_example.md` elaborates the "set a default saved view" story this library's own
`user-stories` example already carries
(`templates/user-stories/user-stories_example.md:50-51`), dated `created: "2026-06-20"` and `updated:
"2026-06-30"`, which places it after the story it elaborates and before the acceptance criteria it
feeds in this library's shared chain. It demonstrates the full variant's own shape at work on a real
scenario: a Recurring Analyst's goal of opening a dashboard already filtered the way they work, the main
success scenario that delivers it, the two extensions this library's own siblings already name (a
deleted filter, and no default set), and a minimal guarantee the siblings do not state outright: an
attempt that stops partway changes no other user's default and never leaves this analyst with two. It must not add facts
the chain's siblings do not already carry, such as a shared-view permission edge or a team-wide
default, both of which belong to work this document's own scenario explicitly excludes.

---

## References

<a id="ref-1"></a>[1] Alistair Cockburn. "[Basic Use Case Template](https://cs.otago.ac.nz/coursework/cosc461/uctempla.htm)" (HaT TR.96.03a, v.2, 1998-10-26), University of Otago mirror. cs.otago.ac.nz (accessed 2026-10-15). [primary]

<a id="ref-2"></a>[2] Alistair Cockburn. "[Use Case Template](https://cis.bentley.edu/lwaguespack/CS360_Site/Downloads_files/Use%20Case%20Template%20(Cockburn).pdf)" (same HaT TR.96.03a text), Bentley University mirror, PDF. cis.bentley.edu (accessed 2026-10-15). [primary]

<a id="ref-3"></a>[3] Alistair Cockburn. "[Writing Effective Use Cases](https://kurzy.kpi.fei.tuke.sk/zsi/resources/CockburnBookDraft.pdf)," pre-publication draft #3, edit date 2000.02.21 (published by Addison-Wesley, c.2001). kurzy.kpi.fei.tuke.sk (accessed 2026-10-15). [primary]

<a id="ref-4"></a>[4] Alistair Cockburn. "[Writing Effective Use Cases](https://courses.cs.duke.edu/spring23/compsci308/readings/cockburn_use_cases.pdf)," pre-publication draft #3, Reminders cheat-sheet pages i and 2, Duke course extract. courses.cs.duke.edu (accessed 2026-10-15). [primary]

<a id="ref-5"></a>[5] Alistair Cockburn. "[Writing Effective Use Cases](https://ptgmedia.pearsoncmg.com/images/9780201702255/samplepages/0201702258.pdf)" (Addison-Wesley, 2001, ISBN 0201702258), Pearson free sample pages. ptgmedia.pearsoncmg.com (accessed 2026-10-15). [primary]

<a id="ref-6"></a>[6] Alistair Cockburn. "[Use Cases, Ten Years Later](https://www.dsc.ufcg.edu.br/~garcia/cursos/ger_processos/seminarios/Crystal/Use%20Cases,%20Ten%20Years%20Later.htm)." STQE magazine, Mar/Apr 2002. dsc.ufcg.edu.br (accessed 2026-10-15). [primary]

<a id="ref-7"></a>[7] Karl E. Wiegers. "[Use Cases for <Project> / Guidance for Use Case Template](https://people.eecs.ku.edu/~saiedian/812/Lectures/UML/use-case-template1.pdf)" (Process Impact, 1999), University of Kansas course mirror. people.eecs.ku.edu (accessed 2026-10-15). [primary]

<a id="ref-8"></a>[8] Rational Unified Process. "[Use-Case Specification: <Use-Case Name>](https://cin.ufpe.br/~if682/RUP/webtmpl/templates/req/rup_ucspec.htm)" template, UFPE mirror of the RUP web templates. cin.ufpe.br (accessed 2026-10-15). [primary]

<a id="ref-9"></a>[9] W3C eGovernment Interest Group. "[Use Case Template](https://www.w3.org/egov/wiki/Use_Case_Template)," archived W3C eGov Wiki, last modified 2 December 2008. w3.org (accessed 2026-10-15). [standards]

<a id="ref-10"></a>[10] NYU Courant CS. "[Use Case Specification](https://cs.nyu.edu/~jcf/classes/CSCI-GA.2440-001_sp18/handouts/UseCaseTemplate.pdf)" template, CSCI-GA.2440-001 (Spring 2018) course handout. cs.nyu.edu (accessed 2026-10-15). [practitioner]

<a id="ref-11"></a>[11] ArgonDigital. "[RML Use Case Template](https://argondigital.com/resource/tools-templates/rml-use-case-template)." argondigital.com (accessed 2026-10-15). [vendor]

<a id="ref-12"></a>[12] Practitioner reproduction of Alistair Cockburn's fully-dressed use case field list, distributed as a Claude skill guide, "[Cockburn use case writing guide](https://cdn.jsdelivr.net/npm/usecases-skill@0.1.0/skills/usecases/use-case-guide.md)." cdn.jsdelivr.net (accessed 2026-10-15). Not Cockburn's own text. [practitioner]

<a id="ref-13"></a>[13] Ivar Jacobson, Ian Spence and Keith de Mendonca. "[Use-Case 3.0: The Guide to Succeeding with Use Cases](https://ss-usa.s3.amazonaws.com/c/308454236/media/42906756d195e3bed93712764146367/Use-Case%203.0%20v1.0%20candidate%202.13.pdf)" (v1.00, December 2024, Ivar Jacobson International). ss-usa.s3.amazonaws.com (accessed 2026-10-15). [practitioner]

<a id="ref-14"></a>[14] Ivar Jacobson and Alistair Cockburn. "[Use-Case Foundation](https://alistaircockburn.com/Use%20Case%20Foundation.pdf)" (version 1.1, Ivar Jacobson International / Alistair Cockburn). alistaircockburn.com (accessed 2026-10-15). [practitioner]

<a id="ref-15"></a>[15] Object Management Group. "[OMG Unified Modeling Language (OMG UML), Version 2.5.1](https://www.omg.org/spec/UML/2.5.1/PDF)," Clause 18 "Use Cases" (formal/2017-12-05, December 2017). omg.org (accessed 2026-10-15). [standards]

<a id="ref-16"></a>[16] Martin Fowler. "[Use Case](https://www.martinfowler.com/bliki/UseCase.html)." martinfowler.com bliki, 3 August 2004 (accessed 2026-10-15). [practitioner]

<a id="ref-17"></a>[17] Mike Cohn. "[Advantages of User Stories over Requirements and Use Cases](https://www.mountaingoatsoftware.com/articles/advantages-of-user-stories-for-requirements)." Mountain Goat Software (page states "Last updated April 23rd, 2026") (accessed 2026-10-15). [practitioner]

<a id="ref-18"></a>[18] Doug Rosenberg. "[Use Cases vs Requirements vs Attributes/Methods](https://ootips.org/use-cases-vs-requirements.html)," posting to otug@rational.com, reproduced in the ootips digest, dated 30-Aug-97. ootips.org (accessed 2026-10-15). [practitioner]

<a id="ref-19"></a>[19] Scott Sehlhorst. "[Top Ten Use Case Mistakes](https://tynerblain.com/2006/01/26/top-ten-use-case-mistakes/)." Tyner Blain, posted January 26, 2006 (accessed 2026-10-15). [practitioner]

<a id="ref-20"></a>[20] Laura Brandenburg. "[7 Mistakes Even the Best Make When Writing Use Cases](https://www.bridging-the-gap.com/7-use-case-writing-mistakes/)." Bridging the Gap (accessed 2026-10-15). [practitioner]

<a id="ref-21"></a>[21] Lyn Girvan. "[So, you think you know use cases?](https://irmuk.co.uk/wp-content/uploads/2024/08/Girvan_So_You_Think_You_Know.pdf)" CMC Partnership Consultancy, IRMUK conference slides, 2024. irmuk.co.uk (accessed 2026-10-15). [vendor]

<a id="ref-22"></a>[22] Scott W. Ambler. "[System Use Cases: An Agile Introduction](https://agilemodeling.com/artifacts/systemusecase.htm)," excerpted from The Object Primer 3rd Edition. agilemodeling.com (accessed 2026-10-15). [practitioner]

<a id="ref-23"></a>[23] Carlton Nettleton. "[Why Use Cases Are Still Important...with User Stories](https://agile.appliedframeworks.com/applied-frameworks-agile-blog/why-use-cases-are-still-important-with-user-stories)." Applied Frameworks blog, June 26, 2014 (accessed 2026-10-15). [practitioner]

<a id="ref-24"></a>[24] Eclipse Process Framework / OpenUP. "[Checklist: Use Case](https://www.utm.mx/~caff/doc/OpenUPWeb/openup/guidances/checklists/use_case_C5362874.html)." utm.mx (accessed 2026-10-15). [practitioner]

<a id="ref-25"></a>[25] University of Notre Dame Business Analysis Process. "[Use Case Guide](https://sites.nd.edu/businessanalysis/?p=230)." sites.nd.edu (accessed 2026-10-15). [practitioner]

<a id="ref-26"></a>[26] Muhammad Ridho Kurniawan Pratama, Deni Utama and Rauhil Fahmi. "[Test-First Protocol for Deriving Unit Tests from Use Case Specifications](https://journal.ugm.ac.id/v3/JNTETI/article/view/24073)." Jurnal Nasional Teknik Elektro dan Teknologi Informasi, vol. 15 no. 1, Feb 2026 (accessed 2026-10-15). [practitioner]

<a id="ref-27"></a>[27] Mark Strembeck and Uwe Zdun. "[Scenario-based component testing using embedded metadata](https://dl.gi.de/handle/20.500.12116/28495)." Testing of Component-Based Systems and Software Quality, Gesellschaft fur Informatik, 2004 (accessed 2026-10-15). Abstract and record page only; full text not retrieved. [practitioner]
