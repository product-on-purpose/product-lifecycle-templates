# Design Brief: the guide

How to tell whether you need one, how to pick lean or full, and how to grade what comes back
before it goes to the people who will design from it.

## Before you start: is this the right document at all?

Write a design brief when you have one chosen problem and one concept chosen for design, and you
need to hand both to the people who will design it, before anyone specifies how that concept
works. The Design Council's own page names this hand-off directly, placed at the close of Define:
"The result is to create a design brief which clearly defines the challenge based on these
insights." This document's whole job, per this library's `discovery-docs` family contract, is to
converge on one chosen problem and, at most, name the one concept chosen for design, never how
that concept works, and it decides no investment.

**Write something else if:**

| You actually need | Because |
|---|---|
| a **problem statement** | this library's own `problem-statement` bundle already names the chosen problem; where one exists, point to it from The Challenge rather than reframing it here |
| a **project brief** | a project brief asks a named approver for authority to start finding out whether and how to proceed; this document asks for no such authority, and names a concept already chosen |
| a **business case** | no source read for this bundle orders the two against each other in either direction; treat that as open, at medium-low confidence, rather than as a settled sequence |
| a **specification, a product design specification, or a PRD** | Ignitec draws the line directly, "The commercial considerations will come later when you write your product design specification," and UXPin agrees that "A design brief outlines what designers must create, while the specifications define specific details" |
| a **creative brief** | Figma's own account orders the two: "In many design workflows, the creative brief informs the design brief, ensuring visual decisions support broader project goals." Write the creative brief first if your team already writes one |
| the **Shape Up pitch** | a pitch arrives shaped, where "the overall solution is spelled out," and exists, in Basecamp's own words, "to present a good potential bet"; this document hands over a concept and asks for no bet |
| a **Design Sprint brief** | Google Ventures' own page describes "a five-day process" and publishes no separately named Sprint Brief to write instead |
| a **commissioning agreement between a client and a designer** | that is the commonest sense of the term in the literature this bundle's research read, carried by Visser, the Design Commission for Wales, and Wikipedia; this bundle builds a different sense and says so throughout |

**Write nothing at all if** no one distinct from the chosen problem's own owner will design from
this document. Visser's own research found that "in many of the interviews the projects discussed
started without a design brief," and at least one named software design team, Intercom's own,
describes an iterative process with no brief-shaped kickoff document at all: "We're continually
iterating this process, figuring out ways in which we can design better things faster." A document
nobody reads before designing has not finished the job this bundle exists to do.

## Picking a variant

**Lean** carries The Challenge, Who It Is For and What We Learned, The Chosen Concept, and The
Handoff: enough to hand a chosen problem, a chosen concept, and an approved start to the people who
will design it. **Full** inserts Constraints on the Design and Open Questions for Design between
The Chosen Concept and The Handoff, and The Handoff's Scope, Time Line and Budget after it.

Use full when a separate design team needs limits on the design work, open questions, and a
design-scoped time line and budget stated in writing, not only a chosen concept and a handoff. Use
lean when a team's own designers are already close to the work and need none of that written down
on its own. The three added sections do not carry equal weight with the four lean ones: no source
read for this bundle publishes a design-only constraints section or a time line and budget scoped
to a design handoff alone, and the Open Questions field rests on one practitioner template, Heap's
own. The candidates list inside The Chosen Concept, which both sizes carry and row 5 scores, rests on
that same template's "Discarded Alternatives" field; the spec rated it low, and the research log
proposes low to medium-low. Treat each as this library's own construction, stated at its own confidence in the template's
own section comments, never as received practice.

## The rubric

Below 16 out of 22 on a full brief, the designers inheriting it cannot tell what altitude the
concept is pitched at, what it leaves out, or who settles a disagreement once design starts,
without coming back to ask you questions this document should have answered on its own. Below 12
out of 16 on a lean brief, the same gap opens with three fewer sections standing between a weak
answer and the people who design from it.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Challenge stays a problem** | The section names a feature, a screen, or a channel to build, or already reads like the concept below | A problem is named, but you cannot tell from the sentence what a good outcome would change for the people who have it | You can point at the sentence, say what a good outcome changes, and no screen, button, or channel appears anywhere in it |
| 2 | **Audience and insight** | "Users" or "the team," with no insight stated | A group is named, but you cannot point to the single research insight the challenge rests on | You can name a group someone could go find a member of, and point to the one insight, in a sentence or two, that this challenge rests on |
| 3 | **Concept held at altitude** | The chosen concept names a screen, a button, a flow, or how a feature works | The concept is named at the level of a kind of answer, but a reader could reasonably mistake it for a solution already begun | You can point at the concept sentence, and it names the kind of answer chosen, never what a screen shows, what a button does, or how a flow proceeds |
| 4 | **What it leaves out** | Nothing is named as excluded, or the field says only that everything else is out of scope | Something is named as excluded, but you cannot say who would have reasonably assumed it was included before this line | You can name the specific thing excluded and say who would have assumed it was in, before this line said otherwise |
| 5 | **Candidates genuinely weighed** | No other candidate is named, or the "candidates" are the chosen concept restated | A candidate is named, but the reason it was set aside is missing, or is really the reason the chosen one was picked, said twice | You can name a genuinely different candidate and the specific reason it was set aside, distinct from the reason the chosen one was picked |
| 6 | **Approval recorded, not granted** | No named approver appears, or the section reads as granting the project its funding or its authorization to exist | A named approver and a date appear, but you cannot tell from the sentence that only design beginning, not project funding, was approved | You can point at the name and the date, and the sentence makes clear that what was approved is design beginning, never the project's funding |
| 7 | **Revision names its review** | No revision process is named, or the brief reads as fixed once written | A revision process is named, but you cannot tell whether it means reviewing this document before it goes out, or reviewing the design as the work proceeds | You can tell, from the sentence alone, which of the two reviews the team means, and roughly when it happens |
| 8 | **Feedback has a decider** | No one is named as the person who settles disagreement in feedback on the design | A decider is named, but only as part of a group, with no single name a designer could actually go to | One named person settles a disagreement in design feedback, distinct from whoever approved the concept |
| 9 | **Constraint is design-scoped** *(full only)* | A limit is named at the level of the whole project, such as a launch date or a total budget, or the row states a goal rather than a limit | A limit on the design work is named, but you cannot tell why it binds design specifically rather than the whole project | You can point at the limit and the same row says why it binds the design work itself, not a limit a project brief would already carry |
| 10 | **Open question is unresolved** *(full only)* | The field restates a constraint already named above, or says only that there might be open questions | A question is named, but you cannot tell whether anyone actually does not yet know the answer | The question names something nobody yet knows, distinct from every constraint above, with an assumption held until it is answered |
| 11 | **Scope, time, budget design-scoped** *(full only)* | The budget line carries a project figure, or neither the scope nor the deadline names a deliverable short of a finished screen or flow | Scope and timing name the design work alone, but the budget line is silent where it should plainly say none exists | Scope, timing, and budget each name the design work alone, and where no design-scoped budget exists, the row says so instead of carrying a project figure |

**Which rows apply to what.** Full ships all eleven rows because a reader of the full variant can
ask about design-only limits, open questions, and a design-scoped time line and budget, as well as
the four sections every size must get right. Lean ships eight, every row the lean variant has a
section to support.

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| lean | 1-8 | 16 | **12** |
| full | all 11 | 22 | **16** |

## Anti-patterns

**Specifying how the concept works, inside a document meant to name only what it is.** Shape Up's
own description of a shaped concept, "It defines what the feature does, how it works, and where it
fits into existing flows," is exactly the content this document excludes. A sentence that reads
like that description has crossed into a specification.

**Treating Heap's own template as proof this sense reaches into solution detail.** Heap's template
is real and literal, including "Discarded Alternatives:" and "Open Questions," but its own goal
line names "your proposed design solution(s)," not a chosen concept. Cite its headings only with
that solution-sense label attached, never as this document's own structure confirmed.

**Reading the no-solution camp as support for naming a concept.** GANSW's advisory note states
"Focus on desired outcomes, but don't prescribe a solution," and Ignitec's is "Say what and why, but
not how." Both forbid naming any solution at all. This library's own chosen-concept rule departs
from that camp; neither source argues for it.

**Reusing Basecamp's pitch line to describe this document's own altitude.** Shape Up's "the overall solution is
spelled out" and "The purpose of the pitch is to present a good potential bet" both describe the
pitch, a rung above this document and a separate, unbuilt catalog candidate. Neither sentence
argues that a design brief needs a worked solution.

**Writing a budget section that actually holds a project's budget.** *(full only)* Every sourced
budget question this research found scopes to the whole project: Kaninsky's own template asks "What
is your budget for this?" and Eleken's asks "7. What are the project timeline and budget?" This
section's own figure, where one exists at all, is the design work's alone, never a stand-in for the
project's.

**Treating the sign-off recorded here as the decision that funds the project.** The Eleven Lessons
report describes what that sign-off actually buys: "the corporate and financial backing to the
development of one or more concepts that have addressed the initial problem." The Handoff may
record that design was approved, by whom and when; it is never the record that grants the backing
itself.

**Setting the challenge too broad or too narrow.** Visser warns that "design briefs could be too
broad as well as too narrow." Shape Up describes the too-broad failure from the inside: "You're
solving a problem with no context. You have to be a mind reader." The too-narrow failure is the
specification creep rows 1 and 3 are built to catch.

**Importing creative-brief tone and voice guidance.** Asana's own tone discussion, "Think of your
message as a person. It should have a voice (a personality) and a tone (a mood or attitude),"
belongs to creative briefs specifically. This document carries no tone or voice section at any
size.

**Claiming a Google Ventures Sprint Brief, or Atlassian's project poster, as evidence for this
document.** GV's own page names "a five-day process" and publishes no separate Sprint Brief.
Atlassian's own poster is a living kickoff document whose text points toward a project plan, nearer
this library's `project-brief` than this one.

## When it is good enough

When the concept is named at the level of a kind of answer and nowhere crosses into how it works,
when what it leaves out is specific enough that someone could say who would have assumed it was
in, and when a named person has actually approved design to begin, by a real date, without that
approval reading as the project's funding.

Then delete every HTML comment. A brief nobody has approved, or one that quietly grants a project
its backing instead of recording that design may start, has not finished the job it exists to do,
whatever else it contains.
