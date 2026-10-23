# Problem Statement: the guide

How to tell whether you need one, how to pick lean or full, and how to grade what comes back before
it goes to the decider named in Decision This Informs.

## Before you start: is this the right document at all?

Write a problem statement when you need to name which problem is worth solving, who has it, and what
evidence shows it is real, before anyone names a solution. Nielsen Norman Group's own definition is
the anchor this bundle builds from: "A concise description of the problem that needs to be solved."
This document's whole job, per this library's `discovery-docs` family contract, is to frame one
problem and name no solution, option, project, or investment.

**Write something else if:**

| You actually need | Because |
|---|---|
| a **business case** | `business-case`'s own Problem and Opportunity section asks the same questions inside a funded investment comparison. This document comes earlier, asks for no money, and decides whether a problem is worth that comparison at all. One Six Sigma source draws the same line by name: the problem statement "describes what, where, and how much, without the persuasive framing". The order, statement first, is this library's own position |
| a **project brief** | a project brief asks a named approver for authority to start initiation. This document asks for no authority and names no project. The Association for Project Management's own published glossary has no entry under this document's name, and defines Brief and Charter as two different things |
| a **PRD** | this library's own `prd` companion already names a problem statement as one of the things that precede a PRD |
| a **How Might We question** | it already points toward generating solutions, where this document names none |
| a **list of constraints** | a limit any answer must respect, such as a budget, a deadline or a regulation, bounds a solution, and this document names none. Engineering-design teaching and a capstone proposal label constraints, and one engineering paper puts them inside the problem statement, a dissent this library does not follow; `project-brief`'s Constraints and Who Should Be Involved section carries them. That routing is this library's own position |

**An opportunity statement is a separate type in this library, and it is not built.** Nielsen
Norman Group names the two as aliases, "written and used in the same way", phrased positively instead
of as a problem. One business-analysis source dissents for projects specifically, naming the move where
"practitioners treat problems and opportunities interchangeably when developing Business Cases and
Project Charters" as an error, not a harmless alias. On 2026-10-17 the maintainer ruled the two
different documents, and the opportunity statement became catalog entry 207, a candidate type of its
own. On 2026-10-22 the maintainer parked it rather than build it (#298), because no template with
sections for it was found. Frame an opportunity here when Nielsen Norman Group's reading fits your case.
A design-thinking Point of View statement, by contrast, is listed as an alias of this document.

**A net-new initiative, where no product exists yet, can use this document too.** Jeff Gothelf
publishes a Business Opportunity Statement for that case, and still says: "My advice is to try the
Business Problem Statement first." To fill this document from his formula, put the people the gap
leaves unserved in Who Is Affected, named closely enough that someone could go and find one. Put the
gap itself in Evidence, with where you saw it. His formula's line for it reads "What existing products /
services fail to address is [this gap]." Leave out his next line, "Our product / service will address
this gap by [vision / strategy]." That line names a direction for a solution, which this document never
names. Carry it to the document you name in Decision This Informs.

**Write nothing at all if** no one is positioned to decide, once this document exists, whether the
problem is worth pursuing further. GOV.UK frames exactly this decision: "Your discovery is finished
when you've decided whether or not you want to move on to alpha." A statement with no real decider
named in Decision This Informs has not finished the job this document exists to do.

## Picking a variant

**Lean** carries Problem Statement, Background, Who Is Affected, Impact and Why Now, Evidence, and
Decision This Informs: enough to frame the problem, show it is real, and name the decision it feeds.
**Full** inserts How People Cope Today, What Is Not Part of the Problem, How We Will Know It Is
Solved, and Open Questions and Assumptions, in that order, between Evidence and Decision This
Informs. The signal to move from lean to full: will a reader reasonably ask how people work around
the problem today, what this statement deliberately excludes, what solved would look like, or what
is still unknown, not only who has the problem and what shows it is real.

Both sizes stay short. NHS Wales puts a typical instance at "about 18 words long", and Nielsen
Norman Group's own brevity rule holds at both sizes: "If you can condense your problem statement
down to a few sentences, others will quickly understand what you focus on and why, and what's out
of scope." The full variant adds four named fields around the statement; it does not add length to
the statement itself, and no source read for this bundle abandons that brevity convention for a
longer form.

## The rubric

Score each row 0, 1 or 2. Below 14 out of 20 on a full statement, a reader cannot tell whether this
problem is worth taking to a project brief or a business case without going back to ask the author
questions this document should have answered on its own. Below 9 out of 12 on a lean statement, the
same gap opens with four fewer sections standing between a weak answer and the decider.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **No solution or cause** | The statement names a feature, a tool, or a fix to build, or states a cause as settled fact | No solution or cause is named, but you cannot tell from the sentence who has the problem or what is happening to them | You can point to the sentence, name the affected person and what is happening to them, and no solution or cause appears anywhere in it |
| 2 | **Affected group is findable** | "Users" or "customers," with nothing more | A group is named, but too broadly for anyone to go find a member of it | Someone could take the sentence and go find a person who matches it, without guessing |
| 3 | **Origin is traceable** | No indication of how the problem came to attention, or which team or product owns it | An origin is named, but you cannot tell what specifically surfaced it now rather than earlier | You can name who or what flagged the problem, and point to the specific event that surfaced it |
| 4 | **Evidence outranks opinion** | Every row in the table is an assertion with no named source | At least one row names a source, but the strongest row is still an unsourced assertion | The strongest row names where it came from, specifically enough that someone could go check it themselves |
| 5 | **Cost tied to timing** | No cost or consequence is named, or a cost is named with no reason to act now rather than later | A cost and a timing reason both appear, but you cannot tell whether the cost actually grows if nothing changes | You can point to a trend or a date in the document, and tell from it why waiting costs more than acting now |
| 6 | **Decision has an owner** | No name, role, or date appears, and the next document is left generic | A decider, a date, and a next document are all named, but nothing shows the decider agreed to decide | You can point to when and how the named decider agreed to decide, and the specific next document the decision leads to |
| 7 | **Workaround stays evidence** *(full only)* | No workaround or prior attempt is named | A workaround is named in enough implementation detail that it reads as a proposed fix | The workaround is named at the level needed to judge how painful it is, and a prior attempt plus why it fell short is also named |
| 8 | **Exclusion draws a boundary** *(full only)* | The field is blank, or says everything else is out of scope | A neighbouring problem is named, but you cannot say who would have assumed it was included | A specific neighbouring problem is named, and you can say who would reasonably have assumed it was in scope before this line drew the boundary |
| 9 | **Measure carries no target** *(full only)* | No measure is named, or the row names a solution's output instead of a measure of the affected person's experience | A measure and a current level both appear, but a target number or a solution's output also appears in the row | The row names a measure, its current level, and a direction, with no target number anywhere in it |
| 10 | **Root cause stays hypothesis** *(full only)* | A cause is stated as settled fact anywhere in the document | A cause is labeled a hypothesis in this section, but an open question or assumption elsewhere still reads as settled | Every suspected cause in the document sits only here, labeled a hypothesis, and at least one open question is named that would change the statement if answered differently |

**Which rows apply to what.** Full ships all ten rows because a reader of the full variant can ask
about coping, exclusion, success, and open questions as well as who, what, and why. Lean ships six,
every row the lean variant has a section to support.

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| lean | 1-6 | 12 | **9** |
| full | all 10 | 20 | **14** |

## Anti-patterns

**A solution in disguise.** Digital NSW and GOV.UK both publish the identical corrective move,
rewriting a handed-down solution as a problem, and Build for Good states the rule directly: "Do not
include solutions in your problem statement."

**Scope set too broad or too narrow.** A UX design guide states the tension directly: the scope
should be "broad enough to allow for creative thinking and innovative solutions, but narrow enough
that it can provide a direction for that solution."

**Opinion standing in for evidence.** NHS Wales's own warning is blunt: "without evidence of your
problem, you are left with opinion." Digital NSW's review checklist asks the same question as a
gate: "Is this based on evidence rather than assumptions?"

**A predetermined cause dressed up as a problem statement.** A good statement "does not offer
commentary on a proposed solution. It does not attempt to diagnose the problem, nor assign blame. It
is objective and factual." NHS Wales draws the same line from the other side: "problem statements do
not describe the solution or root causes."

**A laundry list of unrelated problems.** Nielsen Norman Group's own rule holds that a discovery
effort "should have one problem statement, and the problem statement should be focused on one
problem."

**One neutral statement flattening genuinely different stakeholder views.** A Canada School of
Public Service job aid writes a point-of-view statement once per stakeholder rather than merging
them into a single voice, illustrated from one inspector's own line about a device that "is not
secure, which makes me feel vulnerable and inefficient." Where stakeholders genuinely disagree on
what the problem is, write more than one statement rather than flattening the disagreement into a
false consensus.

**A costed estimate where a directional figure belongs.** A Six Sigma source draws the line this
document stops short of: "the problem statement describes what, where, and how much, without the
persuasive framing", while a specific dollar estimate "gives a sponsor something concrete to weigh"
in a business case, not here. Writing a full costed estimate with its own methodology has stepped
into `business-case`'s job, not this document's.

**A target number smuggled into the success-measure row.** *(full only)* Queensland's own "Defining
success" play draws a line this section is built to respect: "The outcome is not an output or a
metric of your project." Name the measure and its current level; leave the number that says how far
to move it for the document that proposes how to move it.

## When it is good enough

When the statement names no solution anywhere in it, when the strongest row in the Evidence table
names a source a reader could go check, and when a named person has actually agreed to decide
whether the problem is worth pursuing further, by a real date.

Then delete every HTML comment. A statement nobody has agreed to decide on has not finished the job
it exists to do, whatever else it contains, so the last thing worth checking is not a section of
the statement at all: has the person named in Decision This Informs actually agreed to decide, not
merely been copied on the draft.
