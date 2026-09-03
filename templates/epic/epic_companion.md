# Epic: the companion

The reference behind the template. Read this when you want to know *why* a section exists, what the
research actually says, and where the trackers, the methodologies and the founding text disagree with each
other.

## 1. Orientation

Open a tracker and add an epic and you get a form: a title field, a status field, maybe a date range. That
is what every tool this research examined actually ships [[1]](#ref-1)[[2]](#ref-2)[[4]](#ref-4)
[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7)[[8]](#ref-8)[[9]](#ref-9). This template exists for the handful of
things none of those fields carry: why the body of work exists, who it serves, what is deliberately left
out, and what it sits under. Write it when a form would leave those unsaid; use the tracker's own record for
everything a form already does well.

At a glance:

- **Your framework probably does not define this word.** Four of the five methodologies this research
  surveyed have no epic at all [[17]](#ref-17)[[18]](#ref-18)[[19]](#ref-19)[[20]](#ref-20). SAFe is the
  exception, and it formalizes the artifact heavily: an MVP, a Lean business case, an estimate of costs
  [[21]](#ref-21), and a named accountable Epic Owner role [[22]](#ref-22).
- **The founding definition is one sentence and means something narrower than what most people now mean.**
  Mike Cohn's 2004 wording is a single oversized story, destined to be split and then to disappear from the
  backlog [[14]](#ref-14). Cohn himself flags today's container usage as a departure he did not author
  [[15]](#ref-15).
- **In its native habitat an epic is a record, not a document.** Every tracker surveyed publishes it as
  typed fields on a work-item panel, and the only epic-level reporting found anywhere, Jira's Epic Burndown,
  is a rollup computed from child-story estimates, never a narrative status [[3]](#ref-3).
- **Two named sources publish an epic as prose rather than fields, and this bundle follows their precedent
  rather than a tracker's.** ProductPlan's persona narrative and explicit boundary-writing step
  [[23]](#ref-23), and SAFe's Lean Business Case, which is also where this bundle draws its sharpest
  boundary against `business-case` [[12]](#ref-12).
- **The never-closing epic is a documented failure**, and the published fixes disagree with each other:
  dissolve the artifact entirely [[25]](#ref-25), or hold it to an evidence-based Done [[10]](#ref-10).

## 2. Origins and evolution

The first durable published definition is one sentence in Mike Cohn's *User Stories Applied* (2004): "When a
story is too large it is sometimes referred to as an epic. Epics can be split into two or more stories of
smaller size" [[14]](#ref-14). That epic is singular, one oversized story, not a group. Cohn does not claim
he coined the term; he attributes it to "the XP teams that invented user stories" [[15]](#ref-15), and no
source this research could fetch gives a date or document for that informal coinage, so 2004 is the date of
first published definition, not of first use. The Agile Alliance glossary corroborates the same origin and
publication [[16]](#ref-16).

The meaning drifted, and Cohn names the drift rather than claiming it: "Jira, for example, uses epic to mean
a group of user stories rather than a single, big user story. I do not know if this was a mistake on their
part or not" [[15]](#ref-15). Every tracker this research examined implements that container sense, not the
2004 sense [[1]](#ref-1)[[2]](#ref-2)[[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7)[[8]](#ref-8)
[[9]](#ref-9). This template teaches the container, because that is what a reader actually has open in
front of them, while saying plainly that the word once meant something narrower.

## 3. Anatomy (section by section)

### Title and Narrative Summary (lean and full)

Every tracker asks for a title; ProductPlan is the named source for asking for more than one. Its
prescription is a title, then a short description of the goal, then a persona-form narrative: "As the
[persona], I want to [objective] so that [value]" [[23]](#ref-23). A tracker's title field forces brevity; it
does not force a stated audience or a stated value, which is exactly the gap the narrative sentence closes.
Jira's own landing page is explicit that even the label is not fixed: "Epic is the default name, but you can
rename it and the functionality remains the same" [[8]](#ref-8), a small fact worth knowing before treating
"epic" as a proper noun a reader must already share the meaning of.

### Goal and Context (lean and full)

The section the rest of the document has to answer to, and the reason to write an epic as prose instead of
opening a ticket: everything a tracker's fields already do well, they should keep doing, and this section is
where prose earns a place they cannot fill. It states what larger effort the work ladders up to. What that
larger effort is called is itself unsettled: SAFe formalizes an Epic Hypothesis Statement naming a target
customer, a need, and a measurable outcome [[11]](#ref-11), while three separate tool hierarchies disagree
on what sits above an epic at all [[10]](#ref-10)[[26]](#ref-26)[[27]](#ref-27) (see Debates below). This
section states the goal in whatever form the reader actually has above them, rather than assuming one name
for it.

### Scope (lean and full)

ProductPlan names this step directly: "jot down the scope of work for this epic - in other words, the
boundaries" [[23]](#ref-23). No tracker examined ships a dedicated scope-boundary field; Azure Boards' epic
fields, for comparison, describe priority and timing (Value Area, Business Value, Time Criticality, Target
Date) rather than boundaries [[1]](#ref-1). Scope here is the description of what is included, distinct from
the exclusions the next full-only section asks for separately.

### Child Stories (lean and full)

The founding relation itself: "Epics can be split into two or more stories of smaller size" [[14]](#ref-14).
Aha!'s present-day description keeps the same grouping shape from the other direction: "Epics are used to
group features that often share a common business objective" [[7]](#ref-7). Every tracker examined implements
this as a parent-child link between work items [[2]](#ref-2)[[9]](#ref-9), and Microsoft Learn states the
hierarchy plainly: "Epics group Features, Features group Requirements... You connect items across the
hierarchy with parent-child links" [[2]](#ref-2). The document's version is a maintained, intentional list;
the tracker's version is what that list later feeds into a rollup such as Jira's Epic Burndown
[[3]](#ref-3).

### Acceptance Criteria (lean and full)

ProductPlan frames this as the completion gate: "a clear set of acceptance criteria - the high-level list
of requirements your team will need to approve" [[23]](#ref-23), and this template follows that convention.
It is not the only published answer to how an epic closes. SAFe substitutes a falsifiable hypothesis for
acceptance criteria instead [[10]](#ref-10)[[11]](#ref-11), and the Cohn lineage has no closure artifact for
an epic at all, because an epic there is not distinct enough from a story to need one
[[15]](#ref-15). See Debates below for both alternatives stated in full.

### Out of Scope (full only)

One of the sharpest teaching points this research returned for this document: write the exclusions, not just
the scope. ProductPlan frames the boundary step as writing what is deliberately left out, not only what is
included [[23]](#ref-23), and no tracker examined ships a dedicated field for it
[[1]](#ref-1)[[2]](#ref-2)[[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7)[[8]](#ref-8)[[9]](#ref-9). A
scope section that never states an exclusion is the likeliest single reason an epic never closes; see
Anti-patterns below.

### Dependencies (full only)

Sourced from a SAFe practitioner source on assessing cross-team dependencies: "Classify each dependency by
type (knowledge, technical, process) and severity (blocking versus informational)," and, more pointedly,
"Every dependency gets an owner on both sides - the requesting team and the providing team. Unowned
dependencies are invisible dependencies in disguise" [[30]](#ref-30). This section asks for a classification
and a named owner on each side of every dependency, which is more structure than a tracker's own linked-item
field carries on its own.

### Link Upward (Initiative, Theme, or nothing) (full only)

The layer above the epic is real in some tools and absent from most methodologies, so this section is a
pointer rather than an assertion of a named tier. Three hierarchies disagree with each other: Jira and
Atlassian place an Initiative above the epic [[26]](#ref-26), Aha! places its own Initiative above Epic above
Feature [[27]](#ref-27), and SAFe has no initiative tier at all, running Epic above Feature above Story, with
Capability inserted only at Large Solution scale [[10]](#ref-10). No source claims one of these is correct.
The catalog also lists Theme among an epic's relationships, and this section deliberately does not present
Theme as a rung to link into: the Agile Alliance glossary records that themes are "typically not used as a
level in a backlog hierarchy" [[16]](#ref-16), and Cohn defines a theme as a collection of stories rather
than a tier above one [[15]](#ref-15). This field records whatever the reader's own organization actually
calls the thing above them, including nothing at all.

## 4. Variants and sizing

**Lean** carries Title and Narrative Summary, Goal and Context, Scope, Child Stories, and Acceptance
Criteria: enough to state what the work is, why it exists, and what closes it, without asking for anything a
tracker record does not already force a reader to think about once. **Full** adds Out of Scope, Dependencies,
and Link Upward, the three places this research found prose doing work a tracker's own fields do not do for
it: a named exclusion [[23]](#ref-23), a two-sided owned dependency [[30]](#ref-30), and a stated (or
explicitly absent) position in a hierarchy that even the vendors who publish one cannot agree on
[[10]](#ref-10)[[26]](#ref-26)[[27]](#ref-27). A team living entirely inside one tool's epic record, with
short-lived, single-team work, is well served by lean; a body of work crossing teams, with real dependencies
and a real answer to what it ladders up to, needs the weight full carries.

SAFe's Lean Business Case is not a third size of this template, and the boundary is worth naming here as
well as in Relationships below: it substitutes a hypothesis and leading indicators for the exclusions and
dependency structure above, and it adds a cost estimate and a go/no-go recommendation this template
deliberately does not carry [[12]](#ref-12). A reader choosing between the two is choosing between two
different documents, not two sizes of one.

## 5. Methodology lineage

Four of the five methodologies surveyed have no epic at all, and each absence is a different substitution
rather than a shared omission.

**Scrum** is absent, confirmed by literal string search over the raw fetched 2020 Scrum Guide: zero
occurrences of "epic." In its place is one flat Product Backlog plus an ongoing activity, refinement, which
"the act of breaking down and further defining Product Backlog items into smaller more precise items"
[[17]](#ref-17). The nearest thing to a container is the Product Goal, "a future state of the product" that
serves as a target rather than a groupable unit [[17]](#ref-17).

**XP** is absent. There is no container artifact; instead a time-box rule applies to the story itself:
"Longer than 3 weeks means you need to break the story down further. Less than 1 week and you are at too
detailed a level, combine some stories" [[18]](#ref-18).

**The Kanban Method** is absent, and flatter than Scrum: it has no product-specific work unit at all, using
generic terms such as "request," "card," and "work item" for whatever flows through the board
[[19]](#ref-19).

**LeSS Huge** has no epic either. It partitions one backlog by customer concern into Requirement Areas, "a
categorization of the requirements leading to different views of the Product Backlog" [[20]](#ref-20). That
is an orthogonal axis over the existing backlog, not a new size tier above it, the architectural opposite of
what SAFe does with the same underlying problem.

**SAFe** is the outlier, and it formalizes the artifact heavily. "An Epic is a significant solution
development initiative," requiring "an MVP, a Lean business case, and an estimate of costs"
[[21]](#ref-21), approved through Portfolio Leadership and tracked in a Portfolio Kanban system
[[21]](#ref-21). A named, accountable Epic Owner "work[s] collaboratively with stakeholders to define the
Epic, the Lean business case, and the definition of a Minimum Viable Product (MVP)" and is "responsible for
shepherding the epic through the portfolio Kanban system" [[22]](#ref-22). A practitioner elaboration adds
detail Scaled Agile's own page keeps behind a login wall: the MVP is "the minimum investment required to
test the epic's benefit hypothesis with sufficient confidence to make a pivot-or-persevere decision," and
closure is defined the same way, as "hypothesis validation: the epic's benefit hypothesis has been tested
and the outcome measured," not as work completion [[10]](#ref-10).

A reader working in Scrum, XP, or the Kanban Method is using a word their own framework does not define.
That is not a reason to stop using this template; it is a reason to know the vocabulary is borrowed. Of the
five approaches surveyed here, only SAFe defines the word [[21]](#ref-21), while every tracker surveyed
ships it as a named work-item type [[1]](#ref-1)[[4]](#ref-4)[[7]](#ref-7)[[8]](#ref-8), except Linear,
whose nearest analog is a Project rather than an Epic [[6]](#ref-6).

## 6. Debates and contested boundaries

**Is an epic a big story, or a different kind of object?** The oldest and deepest split. Cohn and the XP
lineage say a large story with "no magic threshold" separating it from an ordinary one
[[15]](#ref-15); SAFe says "a significant solution development initiative" requiring a formal business case
[[21]](#ref-21). A named skeptic doubts the second camp's overhead earns its keep: "It's difficult to tell
whether having a separate thing, as opposed to a bigger version of the same thing, actually furthers that
goal" [[24]](#ref-24). This template takes the container side because that is what a reader's tools actually
give them, without claiming the question is settled.

**Should an epic close on acceptance criteria or on a tested hypothesis?** SAFe substitutes a falsifiable
hypothesis for acceptance criteria, framed as "a falsifiable scientific hypothesis, not a fill-in-the-blank
form" [[10]](#ref-10), with a named seven-slot sentence template ending "We will know we are successful when
[measurable outcome with leading indicators]" [[11]](#ref-11). ProductPlan uses acceptance criteria as the
gate instead [[23]](#ref-23). The Cohn lineage sidesteps the question entirely, since an epic there is not
distinct enough from a story to need its own closure artifact [[15]](#ref-15).

**Are epics an anti-pattern outright?** One published argument says yes: the container model "becomes
bloated. It contains epics that you don't need any more," and the proposed fix is to dissolve the epic into
a story attribute rather than discipline it, while admitting the cost: "what you lose is the ordered list of
the backlog. How do you determine the implementation order then?" [[25]](#ref-25). SAFe's answer to the
same failure is not removal but an evidence-based Done, closing only once the benefit hypothesis is actually
tested [[10]](#ref-10). Both camps agree the failure, an epic that never closes, is real; they disagree
entirely on the fix.

**What sits above the epic?** Three hierarchies disagree and none claims the others are wrong: Jira and
Atlassian run Initiative above Epic above Story [[26]](#ref-26), Aha! runs its own Initiative above Epic
above Feature [[27]](#ref-27), and SAFe runs Epic above Feature above Story with no initiative tier, adding
Capability only at Large Solution scale [[10]](#ref-10).

**Is timeboxing the right constraint on large work?** A flow-method argument against timeboxed sprints
generally exists [[28]](#ref-28), but it never mentions epics; connecting it to how epics specifically should
be governed would be an inference this research does not make, and no epic-specific position should be
attributed to that source.

**Whose hypothesis-statement template is this, exactly?** The seven-slot sentence and the
falsifiable-hypothesis framing come from a practitioner explainer, not from Scaled Agile Inc.'s own page,
which was reachable only past a login wall [[11]](#ref-11). Likewise, the Lean Business Case's named section
list is Atlassian's own rendering of the SAFe artifact, not a publication from Scaled Agile Inc. itself
[[12]](#ref-12). Both should be attributed to the party that actually published them.

**Is Theme a rung in the hierarchy?** The catalog lists Theme among an epic's relationships, but the sources
say otherwise: themes are "typically not used as a level in a backlog hierarchy" [[16]](#ref-16), and Cohn
defines a theme as a collection of stories sharing a topic, not a tier above one [[15]](#ref-15). This
template's Link Upward section (see Anatomy above) does not offer Theme as a rung to point into.

## 7. Anti-patterns and failure modes

**The epic that never closes.** The documented failure this research found, and the fixes disagree with
each other. One camp abolishes the artifact [[25]](#ref-25); SAFe instead ties closure to a tested
hypothesis rather than to a completion checklist [[10]](#ref-10). A third named mechanism, from an unrelated
methodology, is worth knowing as a third option rather than a second vote: Shape Up cancels a large piece of
work by default unless it is deliberately renewed, "as pitched," at a recurring review, rather than extending
it by default [[29]](#ref-29). That analogy between a Shape Up project and an epic is this library's own,
not a claim made by Shape Up's author.

**Scope with no stated exclusions.** ProductPlan treats naming the boundary as a distinct authored step, not
an afterthought to scope [[23]](#ref-23), and no tracker examined forces the question with a field
[[1]](#ref-1)[[2]](#ref-2)[[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7)[[8]](#ref-8)[[9]](#ref-9). A
scope section that never says what is out invites the drift that later makes the epic hard to close.

**Unowned dependencies.** "Unowned dependencies are invisible dependencies in disguise"
[[30]](#ref-30). A dependency recorded as a bare link, with no named owner on each side, is not meaningfully
tracked at all.

**Writing an epic that only repeats field values.** Every tracker examined already does titles, dates,
and parent-child links well [[1]](#ref-1)[[2]](#ref-2)[[3]](#ref-3)[[4]](#ref-4)[[5]](#ref-5)
[[6]](#ref-6)[[7]](#ref-7)[[8]](#ref-8)[[9]](#ref-9), and rollups where the tracker supports them
[[3]](#ref-3)[[7]](#ref-7). An epic document earns its place only where it says
something none of those fields say: the context, the exclusions, the owned dependencies, and the position
above it.

**Crossing into a business case's territory.** A cost estimate, a value-return figure, or a go/no-go
recommendation belongs to `business-case`, not here [[12]](#ref-12). See Relationships below for the full
boundary statement.

**Treating one vendor's hierarchy as the only correct one.** Three disagree with each other
[[10]](#ref-10)[[26]](#ref-26)[[27]](#ref-27), and asserting one as universal will read as wrong to a reader
using either of the other two.

## 8. Relationships to other artifacts

**What precedes and follows.** An epic groups and precedes the stories it will be split into. Cohn's
founding relation states the direction: "Epics can be split into two or more stories of smaller size"
[[14]](#ref-14). Aha!'s present-day description keeps the same shape from the grouping side: "Epics are used
to group features that often share a common business objective" [[7]](#ref-7).

**The sharpest boundary is against `business-case`.** This library already ships that type, and the
research here found the clearest evidence anywhere that an epic, when it is written as a document at all, is
often written as a business case: the SAFe Lean Business Case is a genuine multi-section document, carrying
Business Outcomes Hypothesis, Scope Definition, MVP Definition, In Scope, Out of Scope, Cost Estimate, Value
Return, and a Go/No-Go Recommendation, with the shorter Epic Hypothesis Statement sitting inside it as one
section [[12]](#ref-12). The line this template holds: a business case argues for an investment; this
document groups the work and states what it is in service of. Costing, value return, and a go/no-go
recommendation stay out of scope for `epic` and belong to `business-case` instead.

**What sits above is unsettled, and this document does not force a name onto it.** See Link Upward in
Anatomy and the hierarchy debate above [[10]](#ref-10)[[26]](#ref-26)[[27]](#ref-27).

**What the epic mostly lives inside.** In its native habitat this is a tracker record, not a freestanding
document: Jira, Azure Boards, GitLab, Linear, and Aha! all publish it as typed fields on a work-item panel
[[1]](#ref-1)[[2]](#ref-2)[[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7)[[8]](#ref-8)[[9]](#ref-9), and
this document is written only for what that record's fields cannot carry.

## 9. Adaptations

**SAFe and scaled organizations** should expect the fully formalized version: an MVP, a Lean business case,
Portfolio Leadership approval, and a named accountable Epic Owner [[21]](#ref-21)[[22]](#ref-22), closing on
a tested hypothesis rather than a checklist [[10]](#ref-10)[[11]](#ref-11), and possibly a Requirement-Area
partition instead if the scale reaches LeSS Huge's territory [[20]](#ref-20).

**Scrum, XP, and Kanban Method teams** are using vocabulary their own framework does not define
[[17]](#ref-17)[[18]](#ref-18)[[19]](#ref-19). That is not a reason to avoid this template; it is a reason to
know the word arrived from a tool, not from the method, before treating it as a required artifact.

**Teams living entirely inside one tool's epic record** are already well served by that record's fields for
titles, dates and parent-child links [[1]](#ref-1)[[2]](#ref-2)[[3]](#ref-3)[[4]](#ref-4)
[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7)[[8]](#ref-8)[[9]](#ref-9), and for rollups where the tracker
supports them [[3]](#ref-3)[[7]](#ref-7). This document earns its place for such a
team only at the lean size, and often only for the narrative summary and the exclusions a field-based record
does not force.

**Teams with no formal tier above the epic** should leave Link Upward blank or informal rather than invent a
name for it. Three vendor hierarchies disagree with each other and none is authoritative
[[10]](#ref-10)[[26]](#ref-26)[[27]](#ref-27).

## 10. Worked example

See `epic_example.md`. Per the delivery-docs family's shared-example rule, it continues this library's
common scenario, positioned in the chain between the artifact that opens it and the stories this epic groups
and precedes [[14]](#ref-14)[[7]](#ref-7).

## References

<a id="ref-1"></a>[1] Microsoft Learn. "[Define features and epics to organize backlog items](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/define-features-epics?view=azure-devops)," Azure Boards. [primary]

<a id="ref-2"></a>[2] Microsoft Learn. "[About work items and work item types](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/about-work-items?view=azure-devops)," Azure Boards. [primary]

<a id="ref-3"></a>[3] Atlassian Support. "[View and understand the epic burndown report](https://support.atlassian.com/jira-software-cloud/docs/view-and-understand-the-epic-burndown-report/)." [primary]

<a id="ref-4"></a>[4] GitLab Docs. "[Manage epics](https://docs.gitlab.com/user/group/epics/manage_epics/)." [primary]

<a id="ref-5"></a>[5] GitLab Docs. "[Epics overview](https://docs.gitlab.com/user/group/epics/)." [primary]

<a id="ref-6"></a>[6] Linear Docs. "[Projects](https://linear.app/docs/projects)." [primary]

<a id="ref-7"></a>[7] Aha! Support. "[Get Started With Epics in Aha! Roadmaps](https://support.aha.io/aha-roadmaps/support-articles/features/epics-introduction)." [vendor]

<a id="ref-8"></a>[8] Atlassian Support. "[What is an epic?](https://support.atlassian.com/jira-software-cloud/docs/what-is-an-epic/)" Jira Software Cloud. [primary]

<a id="ref-9"></a>[9] Atlassian Support. "[Manage epics in a scrum space](https://support.atlassian.com/jira-software-cloud/docs/manage-epics-in-a-scrum-project/)," Jira Software Cloud. [primary]

<a id="ref-10"></a>[10] Morne Wiggins, Agility at Scale. "[SAFe Epics: Strategic Portfolio Initiatives](https://agility-at-scale.com/safe/lpm/epics/)." [practitioner]

<a id="ref-11"></a>[11] Agility at Scale. "[SAFe Epics](https://agility-at-scale.com/safe/epics/)" (hypothesis statement page). [practitioner] A practitioner explainer, not Scaled Agile Inc.'s own page, which was reachable only past a login wall; the seven-slot template and the falsifiable-hypothesis framing are attributed to this source, not to Scaled Agile Inc.

<a id="ref-12"></a>[12] Atlassian. "[SAFe lean business case template](https://www.atlassian.com/software/confluence/templates/safe-lean-business-case)," Confluence Templates. [vendor] Atlassian's own rendering of a SAFe artifact, not Scaled Agile Inc.'s publication of it; the section list is Atlassian's.

<a id="ref-14"></a>[14] Mike Cohn. *User Stories Applied: For Agile Software Development*. Pearson Education, 2004, ISBN 0-321-20568-5. [primary]

<a id="ref-15"></a>[15] Mike Cohn, Mountain Goat Software. "[Epics, Features and User Stories](https://www.mountaingoatsoftware.com/agile/stories-epics-and-themes)." [practitioner] A maintained present-day restatement (dateModified 2025-04-28), used only for present-day and attribution claims; the 2004 wording is carried by [[14]](#ref-14).

<a id="ref-16"></a>[16] Agile Alliance. "[What is an Epic?](https://agilealliance.org/glossary/epic/)" Agile Glossary. [primary]

<a id="ref-17"></a>[17] Ken Schwaber and Jeff Sutherland. "[The 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html)." [primary]

<a id="ref-18"></a>[18] Don Wells. "[User Stories](http://www.extremeprogramming.org/rules/userstories.html)," ExtremeProgramming.org. [practitioner]

<a id="ref-19"></a>[19] David J. Anderson School of Management. "[Revisiting the Principles and General Practices of the Kanban Method](https://djaa.com/revisiting-the-principles-and-general-practices-of-the-kanban-method/)." [practitioner]

<a id="ref-20"></a>[20] Craig Larman and Bas Vodde, LeSS.works. "[Requirement Areas](https://less.works/less/less-huge/requirement-areas)," LeSS Huge. [primary]

<a id="ref-21"></a>[21] Scaled Agile, Inc. "[Epic](https://framework.scaledagile.com/epic/)," SAFe framework article. [vendor] The page is paywalled past its public summary; deeper sections on cost and duration forecasting are not claimed here.

<a id="ref-22"></a>[22] Scaled Agile, Inc. "[Epic Owners](https://framework.scaledagile.com/epic-owner/)," SAFe extended guidance. [vendor] Same paywall caveat as [[21]](#ref-21); only public-summary text is used.

<a id="ref-23"></a>[23] ProductPlan. "[How to Write an Epic (for Product Managers)](https://www.productplan.com/learn/how-to-write-an-epic)." [practitioner]

<a id="ref-24"></a>[24] Kent McDonald, Agile Alliance. "[Epic Confusion](https://agilealliance.org/epic-confusion/)." [practitioner]

<a id="ref-25"></a>[25] Bertil Muth. "[Epics are dead. Here's what we should do instead.](https://www.freecodecamp.org/news/epics-are-dead-heres-what-we-should-do-instead-279bada1e644/)" freeCodeCamp. [practitioner]

<a id="ref-26"></a>[26] Tempo. "[SAFe hierarchy: Epic-Feature-Story vs Initiative-Epic-Story?](https://www.tempo.io/blog/which-safe-hierarchy-should-you-choose)" [vendor]

<a id="ref-27"></a>[27] Brian de Haaff, Aha!. "[Initiatives vs. Epics vs. Features: What Is the Difference?](https://www.aha.io/blog/initiatives-vs-epics-vs-features)" [vendor]

<a id="ref-28"></a>[28] David J. Anderson. "[Tyranny of the Timebox Revisited](https://djaa.com/tyranny-of-the-timebox-revisited/)," DJAA. [practitioner] Never mentions epics; used only for the flow-versus-timebox debate in general, with no epic-specific position attributed to this source.

<a id="ref-29"></a>[29] Ryan Singer. "[The Circuit Breaker](https://basecamp.com/shapeup/2.2-chapter-08)," Shape Up, Basecamp. [practitioner] The analogy between a Shape Up project and an epic is this library's own, not a claim made by this source.

<a id="ref-30"></a>[30] Agility at Scale. "[SAFe Dependencies Assessment](https://agility-at-scale.com/safe/requirements-model/safe-dependencies-assessment/)." [practitioner]
