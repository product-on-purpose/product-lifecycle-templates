# Design Brief: the companion

The reference behind the template. Read this when you want to know why a section exists, what the
research actually says, and where the sources genuinely disagree.

## 1. Orientation

In this bundle's sense, a design brief is a short document written at the close of Define. It hands one
chosen problem and one chosen concept to the people who will design it, before anyone specifies how that
concept works. The Design Council's own history page names the Define-stage deliverable directly: "The
result is to create a design brief which clearly defines the challenge based on these insights."
[[22]](#ref-22). This bundle builds that concept-handoff sense, which is one of at least four senses the
wider literature gives the term (section 2).

At a glance:

- **The term has no settled meaning, and the canon says so directly.** "There is no clear or univocal
  definition in the literature." [[3]](#ref-3). Commissioning, specification, problem framing and solution
  all recur as senses across the sources this research read (section 2 and section 6).
- **This bundle's narrow shape is the library's own composition, not a shape any single source publishes
  whole.** No source confines a brief to a chosen challenge, a chosen concept and a handoff. Some sources
  forbid naming any solution at all, and others demand a fully worked one (section 6).
- **The full variant rests more on the library's construction than the lean variant does.** Constraints
  on the Design and The Handoff's Scope, Time Line and Budget both carry low confidence in this research;
  each full-only section says so plainly in section 3.
- **Many teams write none of this.** "In many of the interviews the projects discussed started without a
  design brief" [[1]](#ref-1), and one named software design team describes an iterative process with no
  brief-shaped kickoff document at all [[20]](#ref-20).
- **The commissioning sense, a written agreement between a client and a designer, is the commonest sense
  in the literature this research read, not a misuse of the term.** This bundle builds a different sense and
  says so throughout.

## 2. Origins and evolution

No single body or author originates "design brief" as this bundle's own artifact. The term is older than
any one of its senses, and several independent traditions use it for different documents.

**Design-management research frames the four senses this research found** (see also section 6). Colombi
and Nocek survey the term across sub-disciplines and find it unsettled even inside design: a brief is
"commonly intended as a statement whose form may vary from a sentence to a structured document,
articulating a project's objectives, requirements, and constraints" [[3]](#ref-3). In Design Management
specifically, a brief is "a negotiation of preliminary knowledge and requirements between the designer and
the client" [[3]](#ref-3), the commissioning sense. Visser corroborates that sense from UX practice:
"design briefs are a document written by the person or organization wanting the design completed"
[[1]](#ref-1), and the same paper draws a sharp line against a different document written the other
direction, by the designer rather than the client [[1]](#ref-1). The Design Commission for Wales
corroborates the same commissioning sense from the built environment: "The project brief should be the
central reference document used in the appointment of a consultant team." [[5]](#ref-5).

**Design-process research places a different sense, a chosen problem narrowed to a chosen concept, at a
specific point in a staged process.** The Design Council's own history page puts it at the hinge between
Define and Develop: "The result is to create a design brief which clearly defines the challenge based on
these insights." [[22]](#ref-22). The Eleven Lessons report, the Design Council's 2007 study of eleven
global brands, is the primary source behind that placement: "At most of the companies we visited, the
Define stage would end with final sign-off of the concept and approval of work to begin on design and
development." [[14]](#ref-14). This bundle's phase traces to that study, and section 2 of
`docs/internal/contracts/discovery-docs.md` sets it. Its cadence exception rests on different sources, the
ones below that describe a brief as a living document, and section 1 of the same contract states it.

**Software product practice supplies a fourth entry point, closer to a worked solution than a chosen
concept.** Heap, a product-analytics company, names both documents in its own practice: "Two documents are
central to our approach: the Problem Brief and the Design Brief." [[7]](#ref-7). Its own goal line,
though, names a solution: "The goal of a Design Brief is to describe, holistically and at a high level,
your proposed design solution(s)" [[7]](#ref-7). Basecamp's Shape Up pitch does a neighbouring job at a
software company without using the term at all; this library treats it as a separate, unbuilt catalog
candidate (section 8).

**Who writes it varies with the sense in use.** The commissioning party writes it [[1]](#ref-1). Read and
Bohemia describe a design or project manager writing "in close consultation with the client and the
design team" [[2]](#ref-2). Wikipedia has a designer developing it "in consultation with a client"
[[23]](#ref-23). uxmagic.ai gives the job to a "Design lead" [[21]](#ref-21). No source read names a
product manager as the author; this bundle's own worked example names one anyway, following this
library's chain of authorship through the shared Acme Analytics scenario, a choice that is the library's
own rather than a sourced convention.

**When it is written also varies.** The Design Commission for Wales asks for the needs to be defined
first: "Before drafting the project brief, it is important to spend sufficient time clearly defining the
needs that the project must satisfy" [[5]](#ref-5). Kaninsky's own UX project brief, under a near name,
comes earlier still, written "before any research and design activities even start" [[9]](#ref-9); that
timing belongs to this library's `project-brief` neighbour, not to this bundle. And many teams write
nothing at all: "in many of the interviews the projects discussed started without a design brief"
[[1]](#ref-1).

**Once written, the document keeps moving.** Visser: "design briefs are seldom fixed, static documents,
but rather, they are often dynamic and evolve as the project progresses" [[1]](#ref-1). Read and Bohemia
find "most of the research expresses clearly that design briefs should not ever be set in stone"
[[2]](#ref-2). Wikipedia: "They usually change over time and are adjusted as the project scope evolves."
[[23]](#ref-23). The Design Commission for Wales: "Complex projects rarely have all aspects of the brief
fully defined at inception." [[5]](#ref-5). Jones and Askland add a use for that living document: it
"should be used as a validation tool periodically throughout the project when making key decisions."
[[24]](#ref-24). This is why the `discovery-docs` family contract gives this bundle alone, among its
members, an exception to be revised while the design work it hands off is running, rather than being
finished the moment it is written.

**A software-audience admission check (ADR 0080) asks whether a named software team uses the term, by
name, for its own practice.** Heap clears it alone: a software product-analytics company describing "our
approach" [[7]](#ref-7). Kaninsky shows a software audience under a near name, but the document itself is
a kickoff brief he built "while I was a UX designer at Which?, the UK consumer association" [[9]](#ref-9),
a UX team outside software. Y Combinator addresses startup founders generally, advice rather than one
named team's own practice [[8]](#ref-8). Vendor sources, Kuse [[6]](#ref-6), Figr [[29]](#ref-29), UXPin
[[31]](#ref-31) and uxmagic.ai [[21]](#ref-21), show the term inside product tooling's own vocabulary,
which is not the same thing as a team's own documented practice. Intercom's own design team describes an
end-to-end process with no brief-shaped kickoff document at all: "We're continually iterating this
process, figuring out ways in which we can design better things faster." [[20]](#ref-20). Atlassian
publishes a living kickoff document under a different name, the project poster, and its own text points
nearer this library's `project-brief`: "This section is where your project plan will come into focus."
[[19]](#ref-19).

## 3. Anatomy (section by section)

### The Challenge (lean and full)

Restates the chosen problem for the people who will design it, states what a good outcome would change,
and points to a problem statement where one already exists. The Design Council's own phrase anchors it: a
brief "clearly defines the challenge based on these insights." [[22]](#ref-22). Jones and Askland describe
the same job from the reader's side: a brief exists "to help the designer to understand the problem by
defining the objectives and parameters of the project toward generating the most appropriate solution."
[[24]](#ref-24), and call it, more plainly, "essentially a question or definition of a problem"
[[24]](#ref-24). Kuse's own definition agrees: a brief "defines the problem a design needs to solve, the
context in which it exists, and the constraints that shape the solution" [[6]](#ref-6). Y Combinator
frames the same job in different words: "Good design briefs provide a clear context for a product."
[[8]](#ref-8).

**Beginner note.** Where this library's `problem-statement` bundle already exists for the same challenge,
point to it rather than reframing the problem from scratch; this section's job is to carry that choice
forward for a designer, not to re-litigate it. Where none exists, state the problem in brief, the way
Kaninsky's own kickoff fields ask for a "Background" and an "Objective" [[9]](#ref-9).

**Expert note.** Point to measures that already exist rather than restating them. Kaninsky's own template
folds success directly into this kind of opening section, "Key results & Success criteria" [[9]](#ref-9),
Kuse's guide gives it a numbered step of its own, "3. Clarify Goals and Success Metrics" [[6]](#ref-6),
and Canny similarly recommends that "Having a set of “success factors” can help all parties drive the
correct response and results." [[30]](#ref-30). Where `problem-statement`'s full size already carries its
own measures section, this section should point there rather than duplicate it.

### Who It Is For and What We Learned (lean and full)

Summarizes who the design serves and the research insight the challenge rests on, short enough for a
designer to read in one pass. Kuse's guide gives users their own numbered step, "4. Describe Users and
Real Use Contexts" [[6]](#ref-6). The Design Council frames the insight half of the job directly:
"understanding how user needs and the problem align," closing "based on these insights."
[[22]](#ref-22). Y Combinator asks the evidence question plainly: "Have you done any user observations? If
yes, will you be able to share the process and the findings?" [[8]](#ref-8). Kaninsky's own fields cover
closely related ground, "Target audience," "Data" and "Prior UX experiences" [[9]](#ref-9), though his
brief is written before research runs, so those fields answer this section's users half better than its
learnings half.

**Beginner note.** Name the persona if one already exists in this library rather than re-describing the
group; cite it the way this bundle's own worked example cites `user-persona_example.md`.

**Expert note, and a caveat.** Kuse's own list of what a brief should cover, "including problem statement,
goals, target users, constraints, and deliverables" [[6]](#ref-6), sits inside a sample prompt for Kuse's
own AI drafting tool, not Kuse's statement of what a brief contains. Cite Kuse's own definition and his
fourth heading instead of that sample-prompt sentence.

### The Chosen Concept (lean and full)

Names the candidate concepts weighed, at the level of the kind of answer, names the one chosen and why,
and says what that concept deliberately leaves out. The Eleven Lessons report places the moment: "At most
of the companies we visited, the Define stage would end with final sign-off of the concept."
[[14]](#ref-14). Heap's own goal line names the altitude this bundle borrows without the solution
underneath it: "The goal of a Design Brief is to describe, holistically and at a high level, your proposed
design solution(s)" [[7]](#ref-7). Every citation of Heap in this section describes Heap's own solution
sense, not this bundle's concept sense; section 6 says why the two differ.

What the concept leaves out is this section's best-sourced element. Heap's template carries a dedicated
field for it, "Not Doing," answering "What's not in the solution that could be, and why?" [[7]](#ref-7).
Basecamp's pitch carries the same move under a different name, "No-gos - Anything specifically excluded
from the concept: functionality or use cases we intentionally aren't covering to fit the appetite or make
the problem tractable" [[10]](#ref-10), and states its purpose directly: "Lastly, shaped work indicates
what not to do. It tells the team where to stop." [[12]](#ref-12). Kaninsky's own field asks "What's not
in scope" [[9]](#ref-9), and Figr names a "Decision history: What the team already tried, rejected, or
deferred" [[29]](#ref-29).

A candidates list, naming the alternatives considered and why they were set aside, is less well sourced.
Only Heap's template carries one, under "Discarded Alternatives:," asking "To the extent they're useful
for context, what alternate solutions did we consider but eliminate? Why?" [[7]](#ref-7). No source this
research read publishes a candidates list as a section of a problem-framing brief outside Heap's own
solution-level template.

**Beginner note.** Name the concept at the level Shape Up calls shaped, but stop short of Shape Up's own
content. Shape Up's own description of shaped work is a useful bar to read and not meet: "The work isn't
specified down to individual tasks, but the overall solution is spelled out" [[12]](#ref-12), and its "shaped
concept... defines what the feature does, how it works, and where it fits into existing flows."
[[12]](#ref-12). That is a specification by this library's own line (section 6); name the concept's kind
of answer and stop before "how it works."

**Expert note.** Do not read Shape Up's own line, "A problem without a solution is unshaped work."
[[10]](#ref-10), as support for this bundle's altitude. It describes the pitch, a different, unbuilt
catalog candidate one rung above this document.

### Constraints on the Design (full only)

Names limits the design work itself must respect, limits a project brief would not already carry. Kuse's
guide gives constraints a numbered step, "6. Surface Constraints Early and Honestly," and its own
definition names "the constraints that shape the solution" [[6]](#ref-6). Heap's template carries a
dedicated field, "Key Constraints:," and its goal sentence closes on "the constraints within which it
exists." [[7]](#ref-7). Kaninsky's own field asks the design team to "Describe what the design team
should not challenge (e.g. hard technical constraints, change of CMS, major design overhauls during a
platform migration project, etc.)" [[9]](#ref-9). Colombi and Nocek's survey of the term names
"constraints" among the things a brief articulates generally, alongside objectives and requirements
[[3]](#ref-3).

This section rests on thin evidence: the spec rated it low, and the research log proposes low to medium.
No source this research read publishes a
design-only constraints section at this bundle's own altitude; Kaninsky's kinds-of-limit list is the
closest match, and it sits in a kickoff brief written before research runs, a neighbour document rather
than this one. Treat this section's distinctness from `project-brief`'s own constraints content as the
library's own reading, not a settled finding.

**Beginner note.** Name a kind of limit, such as a platform the team must not change or an existing flow
the concept must not break, rather than a specific number or deadline; those belong to `project-brief` or
to this bundle's own Scope, Time Line and Budget section.

**Expert note, on accessibility specifically.** Whether an accessibility obligation belongs in a brief or
in a specification is contested in this research. Design Pickle puts a compliance line directly in its own
brief instructions: "Ensure compliance with accessibility standards (e.g., sufficient color contrast)."
[[32]](#ref-32). UXPin instead lists "accessibility requirements" among what a companion specification
document carries, distinct from the brief itself [[31]](#ref-31). This bundle follows UXPin's split: name
an accessibility obligation here as a limit the concept must respect, and leave its pass or fail criteria
to the specification or the PRD that follows.

### Open Questions for Design (full only)

Says what the designers still need to find out, and what the brief assumes true until they do. Heap's
template carries both fields by name: "Open Questions," introduced by "This is a very early version of
your design! All sorts of things are up in the air, or under debate. Capture them here." [[7]](#ref-7),
and a separate "Assumptions:" field [[7]](#ref-7). No other source this research read names either field
at this bundle's own altitude, so this section rests on one practitioner template.

What could block the design work, as distinct from what could block the project, belongs here too.
Kaninsky's template names "Dependencies" and "Risks" as fields of their own [[9]](#ref-9), and Basecamp's
pitch carries "Rabbit holes - Details about the solution worth calling out to avoid problems"
[[10]](#ref-10); both sit in neighbouring documents, a kickoff brief and a pitch, so treat them as weak
corroboration rather than this bundle's own structural source.

**Beginner note.** Write an open question as a question a designer needs answered, not as a restatement of
a constraint already named above.

**Expert note.** Heap's own Open Questions field sits inside its core, lean-sized template, which argues,
at low confidence, for placing this section in the lean variant rather than full. This bundle keeps it in
full, following the maintainer's ruling on the section set; that movement is recorded here, not applied,
and a future review may revisit it.

### The Handoff (lean and full)

Names who will design from the brief and what they receive, records who approved design to begin and when,
says how the brief stays current while design runs, and names which document takes over once the concept
is specified. Kaninsky states the audience-alignment job directly: his brief exists "to get designers,
product managers and software engineers on the same page before any research and design activities even
start" [[9]](#ref-9); his own timing is earlier than this bundle's, but the audience he names, designers,
product managers and engineers together, is the same one this section addresses.

Recording approval is this section's clearest sourced content. Kaninsky's template asks "Who is the
ultimate decision-maker (sign-off)?" [[9]](#ref-9), and "What does the approval process look like?"
[[9]](#ref-9). Heap names its own gate, a joint review: "our next step is a product quality review" where
"the team goes over both Problem and Design Brief with leadership to get input." [[7]](#ref-7). The Eleven
Lessons report places the moment this bundle's own approval record points back to: "the Define stage would
end with final sign-off of the concept." [[14]](#ref-14).

Recording approval is not the same as granting it. The Eleven Lessons report describes what the sign-off
actually buys: "the corporate and financial backing to the development of one or more concepts that have
addressed the initial problem." [[14]](#ref-14). That backing is the investment decision the
`discovery-docs` contract excludes from every `define` member. This section may record that design was
approved, by whom and when; it is not the record that grants the backing itself.

Which document takes over is this bundle's own POSITION, not a rule every source shares. Ignitec names the
boundary cleanly: "The commercial considerations will come later when you write your product design
specification." [[17]](#ref-17). Wikipedia lists "Product design specification , a document that describes
design specifications" as a separate entry [[23]](#ref-23), and UXPin draws the same line: "A design brief
outlines what designers must create, while the specifications define specific details"
[[31]](#ref-31). uxmagic.ai places the PRD in the same company: "If your team already uses one of these,
treat the PRD as the more detailed document that follows once the idea is approved." [[21]](#ref-21). One
named team skips that step entirely: at Heap, once its review clears, "the design brief allows engineers to
start scoping and building at least the back end." [[7]](#ref-7). This bundle still names the PRD as what
typically follows; a team that goes straight to engineering, as Heap does, is a real variant this section
should not rule out.

**Beginner note.** Name the decider and the date, the way this bundle's worked example records that Priya
Nair's brief was approved, not only the fact that approval happened.

**Expert note, on keeping the brief current.** Every source that addresses revision agrees the document
keeps moving (section 2), but only two sources say which review they mean. Canny describes a review of the
brief itself, before it goes out: "Ensure that the design brief reaches the key decision-makers and
individuals who can provide valuable insights and feedback" [[30]](#ref-30). Figr and UXPin instead
describe a review of the design as it proceeds, "Review pattern: Revision limits, feedback rounds, and
approval owner" [[29]](#ref-29) and "Stakeholder feedback sessions" [[31]](#ref-31). Say explicitly which
one a given team means; the two are not the same meeting.

**Expert note, on decision rights.** Who settles a conflict when feedback on the design disagrees is a gap
this research found supported, but unhomed in any single published template as its own field. Kuse's guide
asks "Who approves final designs" and "How conflicts will be resolved" [[6]](#ref-6); Figr names an
"Approval path: Who decides when feedback conflicts" [[29]](#ref-29); UXPin recommends "the RACI project
management model" [[31]](#ref-31); Canny warns that "there always needs to be a lead point of contact in
every design project." [[30]](#ref-30). A full RACI table is more structure than this bundle's altitude
calls for; a single named decider is enough.

### The Handoff's Scope, Time Line and Budget (full only)

States the scope of the design work handed off, when it should finish, and any budget already set for that
work alone, never a project's whole budget, a funding request or commissioning terms. Basecamp's appetite
is the clearest sourced time box, though it is a pitch's ingredient, not a brief's: "How much time we want
to spend and how that constrains the solution" [[10]](#ref-10). UXPin gives the design work its own
milestone, separate from the project's, a "Design handoff date" [[31]](#ref-31), and Y Combinator asks the
question directly: "1. When do you need the design?" [[8]](#ref-8). Kuse's guide gives scope its own
numbered step, "5. Set Scope and Boundaries Explicitly" [[6]](#ref-6), and Kaninsky's template carries
three fields of its own, "What's in scope," "What might be in scope," and "What's not in scope"
[[9]](#ref-9). Eleken's guide asks for deliverables at the level of a kind of output: "2. What tasks
should the design solve? Describe the key deliverables." [[11]](#ref-11).

This section's budget half rests on no source at all. Every budget this research found scopes to the
whole project or design engagement, never to the design work alone. Kaninsky asks plainly, "What is your
budget for this?" [[9]](#ref-9), and Eleken bundles timeline and budget into one undifferentiated question,
"7. What are the project timeline and budget?" [[11]](#ref-11), adding "Determine your project budget in
advance." [[11]](#ref-11). Treat any figure placed in this section as the library's own construction and
never as this bundle's rule; where a team has no design-scoped budget at all, this field should say so
rather than carry a project figure.

**Beginner note.** Name a kind of deliverable, such as a concept ready for a specification, rather than a
specific screen or flow; naming screens or flows belongs to the document this brief hands off to.

**Expert note.** This section's budget half is the one element of the seven sections that the research
log leaves at low confidence. No source this research read
scopes a time line or a budget to a design handoff alone; the time half is corroborated in part by two
sources, and the budget half is not corroborated at all. State both as the library's own construction when
training a team on this bundle, not as received practice.

## 4. Variants and sizing

**Lean** carries The Challenge, Who It Is For and What We Learned, The Chosen Concept, and The Handoff: a
chosen problem, a chosen concept, and a handoff, in that order. **Full** adds Constraints on the Design,
Open Questions for Design, and The Handoff's Scope, Time Line and Budget, nested inside, keeping the lean
sections' own name and order.

No two of the six published briefs this research read share a section list. Heap's template
[[7]](#ref-7), Kaninsky's [[9]](#ref-9), Basecamp's pitch [[10]](#ref-10), Kuse's numbered guide
[[6]](#ref-6), Y Combinator's questionnaire [[8]](#ref-8) and Eleken's question list [[11]](#ref-11) each
differ in count, order and label. What recurs across them, loosely, is a sense of scope or exclusion in
five of the six, a sense of who the design serves in five of the six, and constraints in four of the six;
references recur in two, and open questions and a named approver each recur in only one. The research
log's Finding 3 names the templates behind each count. **No published
template this research read carries both an approver field and an open-questions section at once**, so the
full variant combines elements two different sources carry separately, at medium confidence.

Each full-only section carries an honest confidence label, never a silent promotion to settled structure.
The spec rated Constraints on the Design and The Handoff's Scope, Time Line and Budget low, and Open
Questions for Design medium-low, on one practitioner template alone. The research log proposes raising
Constraints to low to medium, Open Questions to medium-low to medium, and the time half of the handoff's
scope to low to medium-low, and it leaves the budget half at low. Those movements are candidates for the
maintainer, not settled here. Section 3
states each section's own sourcing in full; this section exists to say the three full-only sections do not
carry equal weight with each other or with the four lean sections.

One movement this research found and did not apply: Heap's own Open Questions field sits inside its
lean-sized core template, which argues, at low confidence, for lean placement rather than full. This
companion records that candidate without applying it; the maintainer's ruling on the section set stands.

## 5. Methodology lineage

**Design-process practice**, through the Design Council's double diamond and its 2007 Eleven Lessons
study, places the document at the Define/Develop hinge and is the source of this bundle's own phase and
cadence exception [[22]](#ref-22)[[14]](#ref-14)[[15]](#ref-15).

**Design-management and commissioning practice**, through Visser, Read and Bohemia, Colombi and Nocek,
Wikipedia and the Design Commission for Wales, converges on a different sense, the commonest in the
literature this research read: a written
agreement between a client and a designer [[1]](#ref-1)[[2]](#ref-2)[[3]](#ref-3)[[23]](#ref-23)
[[5]](#ref-5). This bundle routes that sense away rather than building it; sections 6 and 8 say where it
would live.

**Software product practice**, through Heap and through Basecamp's Shape Up, reaches a worked solution
rather than a chosen concept, and does so under a reading of "concept" that this library treats as a
specification once it names how the feature works [[7]](#ref-7)[[10]](#ref-10)[[12]](#ref-12)
[[13]](#ref-13).

**Vendor and product-tooling practice**, through Kuse, Figma, Figr, UXPin, uxmagic.ai and Eleken, writes
for product and UX teams generally rather than describing one named team's own documented use
[[6]](#ref-6)[[16]](#ref-16)[[29]](#ref-29)[[31]](#ref-31)[[21]](#ref-21)[[11]](#ref-11).

**Startup advisory practice**, through Y Combinator, addresses founders engaging an outside designer, a
context closer to commissioning than to an in-house concept handoff [[8]](#ref-8). **UX kickoff practice**,
through Kaninsky, writes a brief under a near name for a stage before research runs, a timing this
library's `project-brief` neighbour covers instead [[9]](#ref-9).

## 6. Debates and contested boundaries

**Whether a design brief may name a solution at all.** Three camps split the sources this research read,
and this bundle's own altitude sits between two of them, a POSITION rather than a consensus reading. GANSW
states the no-solution camp's rule plainly: "Focus on desired outcomes, but don't prescribe a solution."
[[18]](#ref-18). Ignitec agrees in spirit, "Say what and why, but not how" [[17]](#ref-17), and Y Combinator
frames the risk of not following it: "If you force a solution you risk creating a product that doesn't
solve your problem - and maybe solves no problem at all." [[8]](#ref-8). Kuse's second heading states the
rule as an instruction: "2. Define the Problem-Not the Solution" [[6]](#ref-6). Figma stands at the
opposite pole, naming the brief itself a specification: "A design brief, on the other hand, builds on this
foundation with specific technical and visual requirements." [[16]](#ref-16). Shape Up and Heap sit at a
third pole, a worked solution: Shape Up's shaped work has "the overall solution... spelled out"
[[12]](#ref-12), and Heap's own goal line names "your proposed design solution(s)" [[7]](#ref-7) directly.
This bundle's own concept, named at the level of the kind of answer and never at the level of how it
works, sits between the no-solution camp and the worked-solution camp.

**Ignitec's own line straddles the boundary this bundle draws.** It forbids the how, matching this bundle:
"A good brief should say what the solution needs to do, but not how it needs to do it."
[[17]](#ref-17). But the library's own rule for a `define` document puts "what it must do" on the
specification side, not the concept side. So Ignitec's brief carries content this bundle excludes while
excluding the chosen concept this bundle carries; the two lines are close, not identical.

**Whether "concept" names shared vocabulary.** It does not. Shape Up's own description of a shaped concept
reads, by this library's own line, as a specification: "The shaped concept is an interaction design viewed
from the user's perspective. It defines what the feature does, how it works, and where it fits into
existing flows." [[12]](#ref-12). This bundle's template must state what it means by the word rather than
assume a reader shares the definition.

**Whether the brief precedes or follows the decision to proceed.** Heap's own brief precedes its review:
"our next step is a product quality review" [[7]](#ref-7) happens after both the Problem Brief and the
Design Brief are written, and that review decides whether the project proceeds. The Eleven Lessons report
places the sign-off the other way, closing Define: "the Define stage would end with final sign-off of the
concept and approval of work to begin on design and development." [[14]](#ref-14). This bundle follows the
Eleven Lessons report's timing; Heap's own brief still precedes a go or no-go decision, just not the same
one this bundle's brief follows.

**Whether Heap is a structural source for this bundle's sense, or a collision with it.** Heap publishes a
literal, downloadable template with headings this bundle's own research could not resist citing, Discarded
Alternatives and Open Questions among them [[7]](#ref-7). But its own goal line and its Discarded
Alternatives field both describe a worked solution, not a chosen concept: "To the extent they're useful for
context, what alternate solutions did we consider but eliminate? Why?" [[7]](#ref-7) asks about solutions
eliminated, not concepts. This companion treats Heap as a collision: cite its headings and its goal
sentence, always labeled as the solution sense, and do not read its structure as this bundle's own
concept-handoff sense confirmed.

**Whether one concept or several leaves Define.** The Eleven Lessons report's own narrative sentence names
a singular: "the Define stage would end with final sign-off of the concept" [[14]](#ref-14). The same
report's account of the next stage names a plural: "the development of one or more concepts that have
addressed the initial problem." [[14]](#ref-14). This bundle reads the narrative sentence as its own rule
and carries one concept; the report's own Develop-stage sentence argues the opposite reading is also
available, at medium confidence.

**Whether a feedback round means reviewing the brief, or reviewing the design.** Canny describes the
former: "Ensure that the design brief reaches the key decision-makers and individuals who can provide
valuable insights and feedback" [[30]](#ref-30), a review of the document before it goes out. Figr and
UXPin describe the latter, a review of the design as the work proceeds, "Review pattern: Revision limits,
feedback rounds, and approval owner" [[29]](#ref-29) and "Stakeholder feedback sessions" [[31]](#ref-31).
Section 3's Handoff subsection asks a team to say which one it means rather than treating the two as
interchangeable.

**Whether accessibility belongs in the brief or in a separate specification.** Design Pickle places a
compliance line directly inside its own brief instructions [[32]](#ref-32); UXPin lists accessibility
requirements as part of a companion specification document instead [[31]](#ref-31). Section 3's
Constraints subsection follows UXPin's split, at the library's own choice.

**Whether the challenge is set too broad or too narrow.** Visser warns that "design briefs could be too
broad as well as too narrow" [[1]](#ref-1). Shape Up describes the too-broad failure from the inside:
"You're solving a problem with no context. You have to be a mind reader." [[12]](#ref-12). The too-narrow
failure is the specification creep this bundle's own concept-level altitude is built to stop.

## 7. Anti-patterns and failure modes

**Specifying how the concept works, inside a document meant to name only what it is.** Shape Up's own
description of a shaped concept, "It defines what the feature does, how it works, and where it fits into
existing flows." [[12]](#ref-12), is exactly the content this bundle's own rule excludes; a sentence that
reads like that description has crossed into `develop`.

**Treating Heap's own structure as proof that the concept-handoff sense may reach into solution detail.**
Heap's template is real and literal, but its content is the solution sense throughout, including its goal
line and its Discarded Alternatives field [[7]](#ref-7). Citing Heap's headings without the solution-sense
label invites a reader to copy its content, not only its shape.

**Reading the no-solution camp as support for naming a concept.** GANSW and Ignitec forbid naming any
solution at all [[18]](#ref-18)[[17]](#ref-17); this library's own chosen-concept rule departs from that
camp rather than resting on it. Citing either source as agreement for this bundle's altitude misreads what
they argue.

**Reusing Basecamp's pitch language to describe this bundle's own altitude.** "A problem without a
solution is unshaped work." [[10]](#ref-10) describes the pitch, a rung above this document and a
separate, unbuilt catalog candidate. The sentence does not argue that a design brief needs a worked
solution.

**Writing a budget section that actually holds a project's budget.** Every sourced budget question this
research found scopes to the whole project: "What is your budget for this?" [[9]](#ref-9) and "7. What are
the project timeline and budget?" [[11]](#ref-11). A design brief's own Scope, Time Line and Budget
section, where present, should hold the design work's own figure, not a stand-in for the project's.

**Claiming a Google Ventures Sprint Brief, or Atlassian's project poster, as evidence for this document.**
GV's own canonical page names a five-day process and no separately published Sprint Brief
[[25]](#ref-25); Atlassian's own poster play is a living kickoff document whose own text points toward a
project plan, "This section is where your project plan will come into focus." [[19]](#ref-19), nearer this
library's `project-brief` than this bundle.

**Treating the commissioning sense as a misuse of the term.** It is the commonest sense in the literature
this research read
[[1]](#ref-1)[[5]](#ref-5)[[23]](#ref-23), not an error; this bundle simply builds a different sense and
says so.

**Importing creative-brief tone and voice guidance into this bundle.** Asana's own tone discussion belongs
to creative briefs specifically: "Think of your message as a person. It should have a voice (a
personality) and a tone (a mood or attitude)." [[28]](#ref-28). This bundle carries no tone or voice
section at any size.

**Assuming every team writes one.** Many real projects proceed with none at all [[1]](#ref-1), and at
least one named software design team describes a working process with no brief-shaped kickoff document
[[20]](#ref-20).

**Quoting Phillips's or Dilanchian's genre-defining treatments at all.** Neither could be read this pass;
the genre's main book [[4]](#ref-4) and one practitioner's early-placement article [[27]](#ref-27) are
named here only so a reader knows they exist, never as the source of a specific sentence.

## 8. Relationships to other artifacts

**Not `problem-statement`.** Only one source orders the two by name: Heap pairs "the Problem Brief and the
Design Brief" [[7]](#ref-7), and names the first "The Problem Brief describes the problem to be solved and
the reasons to prioritize it" [[7]](#ref-7), already this library's alias for `problem-statement`. No other
source read times a handoff from problem framing into a design brief, so this chain position rests on one
source and is the library's POSITION.

**Not `project-brief`.** A project brief asks for authority to start finding out whether and how to
proceed, before anyone commits to building anything; a design brief names a chosen concept and asks for no
authority. The Design Commission for Wales calls its own commissioning document a project brief
[[5]](#ref-5), and Kaninsky's UX project brief, under a near name, is written "before any research and
design activities even start" [[9]](#ref-9), a kickoff timing that belongs to `project-brief`, not to this
bundle.

**Not `business-case`.** No source this research read orders a design brief against a business case in
either direction. A brief written before a case hands on a concept the case may weigh as one option; a
brief written after a funded case sits oddly against a membership rule that decides no investment. This
bundle fixes no order between the two, at medium-low confidence.

**Not `product-vision`.** No source this research read orders a design brief against a product vision
either, in either direction.

**Not a specification, a product design specification, or the PRD.** Ignitec names the boundary directly,
"The commercial considerations will come later when you write your product design specification."
[[17]](#ref-17). Wikipedia lists the product design specification as a separate entry
[[23]](#ref-23), and UXPin draws the content line, "A design brief outlines what designers must create,
while the specifications define specific details" [[31]](#ref-31). uxmagic.ai places a PRD in the same
company as a pitch or a PR/FAQ, "the more detailed document that follows once the idea is approved"
[[21]](#ref-21), and scopes a design brief narrowly against it, to a "Screen or flow" and "One design task"
[[21]](#ref-21). One named team skips the specification and goes straight to engineering once its brief
clears review [[7]](#ref-7); this bundle still names the specification or the PRD as what typically
follows.

**Follows a creative brief, in every source that orders the two.** Figma: "In many design workflows, the
creative brief informs the design brief, ensuring visual decisions support broader project goals."
[[16]](#ref-16). Read and Bohemia name an "initial request" a "'creative brief'" [[2]](#ref-2), and Kuse
gives the distinction its own heading, "Design Brief vs. Creative Brief" [[6]](#ref-6). No bundle or
catalog row exists in this library for a creative brief; a team that already writes one should treat this
bundle as the document that follows it, not the one that replaces it.

**Not the Shape Up pitch, catalog entry 45 and unbuilt.** The line has two parts, and both are the
library's POSITION. On altitude, a pitch arrives shaped: "A problem without a solution is unshaped work."
[[10]](#ref-10). On the act, a pitch exists to be bet on: "The purpose of the pitch is to present a good
potential bet." [[10]](#ref-10). The act half is weaker than it first looks, because Heap's own design
brief also feeds a go or no-go review [[7]](#ref-7); the line holds mainly on timing, this bundle's brief
following the concept's own sign-off rather than preceding a bet on it.

**Not a Design Sprint brief.** GV's own canonical page names a five-day process, "The sprint is a five-day
process for answering critical business questions through design, prototyping, and testing ideas with
customers." [[25]](#ref-25), and describes its mid-week storyboard as "a step-by-step plan for your
prototype" [[25]](#ref-25), not a pre-commissioning brief. GV's own page names no separately published
Sprint Brief, which `docs/internal/prototype-brief-admission-evidence.md` also records from an earlier
pass.

**Not an opportunity solution tree.** No mention of a design brief appears anywhere on Teresa Torres's own
page describing the opportunity solution tree; this research read it in full for exactly that contrast and
found none [[26]](#ref-26). The tree is a living, continuously updated map rather than a document handed
off at a point in time. No ordering claim between the two is possible from this source.

## 9. Adaptations

**Teams already running the Double Diamond** have the closest sourced fit: this bundle's phase and its
chosen-concept sense both trace to the Design Council's own study [[22]](#ref-22)[[14]](#ref-14), and the
brief closes Define exactly where their own process already expects a deliverable.

**Teams already running Shape Up** should not expect this bundle to replace a pitch. A pitch is shaped,
solution-bearing content that goes to a betting table [[10]](#ref-10)[[13]](#ref-13); a design brief this
library builds stops one altitude short of that. A team that already writes pitches may find it has, in
effect, already skipped the document this bundle builds.

**Teams running a kickoff-brief practice like Kaninsky's** are writing an earlier, neighbouring document.
Kaninsky's own brief exists "before any research and design activities even start" [[9]](#ref-9); this
bundle's brief comes later, once research has run and a concept has been chosen. A team in that position
should treat Kaninsky's kickoff as `project-brief`'s job and keep this bundle for the handoff that follows
research.

**Teams expecting a commissioning agreement**, the commonest sense in the literature this research read,
want a different document this library does not build. Visser's own definition [[1]](#ref-1) and the
Design Commission for Wales's own practice [[5]](#ref-5) both describe that agreement. Phillips's book on
the genre [[4]](#ref-4) exists, but this research could not read it, so nothing here rests on it. A team
in that position should look for a contract or a project brief, not this bundle.

**Teams expecting a visual or technical specification**, Figma's own sense [[16]](#ref-16), want content
this bundle deliberately excludes at every size. UXPin's and Wikipedia's own boundary lines route that
content to a specification or a product design specification instead [[31]](#ref-31)[[23]](#ref-23); a
team in that position should treat this bundle as the document that precedes the specification, not the
specification itself.

**Teams with no separate design team** may find the full variant's Handoff's Scope, Time Line and Budget
section does little work; Kaninsky's own practice shows the document aligning "designers, product managers
and software engineers" together [[9]](#ref-9) rather than handing off across an organizational boundary,
and a small team may prefer the lean variant's shorter Handoff alone.

## 10. Worked example

See `design-brief_example.md`. Per this library's `discovery-docs` family contract, the example chains onto
the shared Acme Analytics scenario: a design brief for Saved Views, written by Priya Nair, PM, Reporting,
and dated 2026-06-01, after the 2026-05 Reporting friction study and before the Saved Views PRD of
2026-06-12. It carries facts already true when it is dated, names the chosen concept at the level of the
kind of answer, and does not cite the PRD, a prototype, or any later document of the delivery thread as
already existing.

## References

<a id="ref-1"></a>[1] Steven C. Visser, Purdue University. "[Design Briefs from the Real World](https://idsa.org/wp-content/uploads/2023/09/Design-Briefs.pdf)" (IDSA 2023 Education Paper Submission). [academic]

<a id="ref-2"></a>[2] D. Read and E. Bohemia. "[The Functions of the Design Brief](https://www.designsociety.org/download-publication/32128/THE+FUNCTIONS+OF+THE+DESIGN+BRIEF)" (International Design Conference, Design 2012, Dubrovnik, Design Society). [academic]

<a id="ref-3"></a>[3] Chiara Colombi (Politecnico di Milano) and Adam Nocek (Arizona State University). "[Design Heresy: The Problem of the Brief](https://re.public.polimi.it/retrieve/7d41d429-57b0-43e0-89a5-930fcedfa09d/colombi_nocek.pdf)," diid disegno industriale industrial design, No. 84 (2024). [academic]

<a id="ref-4"></a>[4] Peter L. Phillips. "[Creating the Perfect Design Brief: How to Manage Design for Strategic Advantage](https://www.portal.goodeyes.com/public/browse/Documents/creating_the_perfect_design_brief.pdf)" (Allworth Press with the Design Management Institute, 2004), PDF excerpt. [primary; not read this pass, named for existence only]

<a id="ref-5"></a>[5] Design Commission for Wales. "[Introduction to Brief Writing](https://dcfw.org/wp-content/uploads/2025/08/Introduction-to-brief-writing_ENG_2025.pdf)" (2025). [primary]

<a id="ref-6"></a>[6] Kuse Blog, Kuse Inc. "[How to Write a Solid Design Brief: Workflows & Real Examples](https://www.kuse.ai/blog/tutorials/design-brief)." [vendor]

<a id="ref-7"></a>[7] Dave Feldman, Heap. "[Save Time and Get Aligned With a Design Brief](https://heap.io/blog/save-time-and-get-aligned-with-a-design-brief)." [practitioner]

<a id="ref-8"></a>[8] Dominika Blackappl, Y Combinator Part-Time Partner. "[Practical Design: Design Brief](https://www.ycombinator.com/blog/practical-design-design-brief)." [practitioner]

<a id="ref-9"></a>[9] Matěj Káninský. "[The power of a UX project brief (template included)](https://matejkaninsky.com/blog/ux-project-brief-template/)." [practitioner]

<a id="ref-10"></a>[10] Basecamp / 37signals. "[Shape Up, Chapter 6: Write the Pitch](https://basecamp.com/shapeup/1.5-chapter-06)." [primary]

<a id="ref-11"></a>[11] Mariia Kasym / Maksym Chervynskyi, Eleken. "[How to Create a Design Brief: Step-by-Step Guide with Examples](https://eleken.co/blog-posts/design-brief-example-how-it-should-look-like-and-what-it-should-contain)." [vendor]

<a id="ref-12"></a>[12] Ryan Singer, Basecamp (37signals). "[Shape Up, Chapter 2: Principles of Shaping](https://basecamp.com/shapeup/1.1-chapter-02)." [primary]

<a id="ref-13"></a>[13] Ryan Singer, Basecamp (37signals). "[Shape Up, Chapter 8: The Betting Table](https://basecamp.com/shapeup/2.2-chapter-08)." [primary]

<a id="ref-14"></a>[14] Design Council. "[Eleven lessons: managing design in eleven global brands](https://www.designcouncil.org.uk/fileadmin/uploads/dc/Documents/ElevenLessons_Design_Council%2520%25282%2529.pdf)" (2007). [primary]

<a id="ref-15"></a>[15] Design Council. "[The design process](https://web.archive.org/web/20101008093406/http://www.designcouncil.org.uk/about-design/How-designers-work/The-design-process/)" (archived 2010 page). [primary]

<a id="ref-16"></a>[16] Figma, FigJam Resource Library. "[How to write a creative brief: five steps for designers](https://www.figma.com/resource-library/how-to-write-a-creative-brief/)." [vendor]

<a id="ref-17"></a>[17] Ben Mazur, Ignitec. "[How to write an effective product design brief](https://ignitec.com/insights/how-to-write-an-effective-product-design-brief/)." [vendor]

<a id="ref-18"></a>[18] Government Architect New South Wales (GANSW). "[How to develop a design brief](https://www.planning.nsw.gov.au/sites/default/files/2023-10/how-to-develop-a-design-brief-advisory-note.pdf)," advisory note, V2 (12 September 2018). [standards]

<a id="ref-19"></a>[19] Atlassian Team Playbook. "[Project Poster](https://www.atlassian.com/team-playbook/plays/project-poster)" play. [practitioner]

<a id="ref-20"></a>[20] Paul Adams, Intercom. "[How we design at Intercom](https://www.intercom.com/blog/how-we-design-at-intercom/)." [practitioner]

<a id="ref-21"></a>[21] uxmagic.ai. "[What is a PRD?](https://uxmagic.ai/blog/what-is-a-prd)" [vendor]

<a id="ref-22"></a>[22] Design Council. "[History of the Double Diamond](https://www.designcouncil.org.uk/our-resources/the-double-diamond/history-of-the-double-diamond/)." [primary]

<a id="ref-23"></a>[23] Wikipedia contributors. "[Design brief](https://en.wikipedia.org/wiki/Design_brief)." [reference]

<a id="ref-24"></a>[24] Wyn M Jones and Hedda Haugen Askland. "[Design Briefs: Is There a Standard?](https://www.designsociety.org/download-publication/33176/design_briefs_is_there_a_standard)" (Design Society / EPDE 2012). [academic]

<a id="ref-25"></a>[25] GV (Google Ventures). "[The Design Sprint](https://www.gv.com/sprint/)." [vendor]

<a id="ref-26"></a>[26] Teresa Torres, Product Talk. "[Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/)." [practitioner]

<a id="ref-27"></a>[27] Noric Dilanchian, Dilanchian Lawyers & Consultants. "[Use design briefs to shape your projects](https://dilanchian.com.au/?p=789)" (2007). [practitioner; not read this pass, named for existence only]

<a id="ref-28"></a>[28] Julia Martins, Asana. "[The complete guide to writing creative briefs](https://asana.com/resources/how-write-creative-brief-examples-template)." [practitioner]

<a id="ref-29"></a>[29] Figr. "[How to Write a Design Brief: Actionable Guide](https://figr.design/blog/how-to-write-a-design-brief)." [vendor]

<a id="ref-30"></a>[30] Canny Creative. "[How to Write a Design Brief (Template Included!)](https://www.canny-creative.com/how-to-write-a-design-brief/)." [practitioner]

<a id="ref-31"></a>[31] UXPin. "[How to Write a Good Design Brief? (+ Templates)](https://www.uxpin.com/studio/blog/design-brief)." [vendor]

<a id="ref-32"></a>[32] Design Pickle Help Center (CJ Robles). "[How To Create A Successful Design Brief](https://intercom.help/design-pickle/en/articles/9532487-how-to-create-a-successful-design-brief)." [vendor]
