# Companion: The Definition of Ready

> The deep explainer for the definition-of-ready bundle. Read this to understand what a Definition of
> Ready actually is, why neither the Scrum Guide nor SAFe's own text names it, and where practitioners
> disagree about whether a team should keep one at all. The short operator card is
> [`definition-of-ready_guide.md`](definition-of-ready_guide.md); a fully worked instance is
> [`definition-of-ready_example.md`](definition-of-ready_example.md). Inline citations like
> [[1]](#ref-1) resolve to the [References](#references) at the bottom, numbered exactly as the research
> log numbers them. The full retrieval trail, including three sources this bundle could not read and
> quarantines, is
> [`definition-of-ready_research-log.md`](definition-of-ready_research-log.md).

---

## 1. Orientation

A Definition of Ready is the agreement a Scrum team makes about how complete a backlog item has to be
before it can be pulled into a sprint. Microsoft's own playbook states it as "the agreement made by the
scrum team around how complete a user story should be in order to be selected as candidate for
estimation in the sprint planning" [[7]](#ref-7). It is a **gate on entry**, the mirror image of a
Definition of Done's gate on exit, and Scrum Alliance draws the line precisely: "The definition of done
refers to the PBI itself, while the definition of ready often refers to externalities" [[12]](#ref-12).

The job in one sentence: a small, team-owned set of guidelines that lets a team decline to start work
that is not yet clear enough to start, without turning that decline into a rule nobody can override.

At a glance:

- **It is optional, and neither of the two standards that could name it does.** The 2020 Scrum Guide
  never uses the phrase "Definition of Ready" [[4]](#ref-4). The Scaled Agile Framework's glossary
  defines a Definition of Done and has no entry for a Definition of Ready [[5]](#ref-5). Scrum Alliance
  states the asymmetry outright: "While the definition of done (DoD) is part of scrum, a definition of
  ready (DoR) is an external and optional tool" [[12]](#ref-12).
- **Whether to keep one at all is a live, three-sided argument**, not a settled question this companion
  resolves (see [section 6](#6-debates-and-contested-boundaries)).
- **It is owned jointly, by the team that applies it**, not handed down by one role to another
  [[10]](#ref-10)[[9]](#ref-9)[[29]](#ref-29).
- **It fails in both directions.** Too loose, and unready work slips into a sprint; too tight, and it
  becomes what Mountain Goat Software calls "a huge step towards a sequential, stage-gate approach"
  [[14]](#ref-14). This bundle's Review Trigger section is written to catch both.
- **No source read for this bundle measured its effect on flow or predictability.** Every claim about
  what a Definition of Ready does is a practitioner's account, and this companion says so wherever it
  matters rather than once and forgetting it.

This family's own contract names its citation hazard as "folklore presented as standard," and "a
Definition of Ready is part of Scrum" is that folklore exactly. This companion checked the Guide
directly rather than assuming what circulates about it.

---

## 2. Origins and evolution

Unlike a concept the Scrum canon has carried since its early editions, a Definition of Ready has no
canonical origin at all: it was never in the Guide to begin with, so there is no text to compare across
editions. What this bundle can trace instead is where the practitioner term was first published, and it
finds two separate lineages that never cite each other.

**The earliest verified published instance is a 2008 blog post.** Richard Kronfält's "Ready-ready: the
Definition of Ready for User Stories going into sprint planning" states: "So, the definition of Ready
should be;" followed by a six-item list, and names the resulting state directly: "Let's call this state
"Ready-Ready."" [[1]](#ref-1). The Scrum Patterns Group's own pattern, published in *A Scrum Book*,
credits this post with a hedge this bundle keeps rather than sharpens into fact: "Richard Kronfält
apparently published the first formal description of Definition of Ready in 2008" [[2]](#ref-2).

**A second, separate lineage credits a different origin for the same "ready-ready" name.** Jakobsen and
Sutherland write that "Systematic introduced the term ready-ready, to express that work from the
Product Backlog has been sufficiently elaborated to be allocated to a sprint for implementation"
[[3]](#ref-3). Nothing read for this bundle sequences these two lineages against each other or shows
either citing the other, so this companion records both and picks neither. (The paper's own venue and
year, Agile 2009, come from its filename and bibliographies rather than its body text, so they are
reported here as provenance, not as a verified fact of the text itself.)

**Two authors writing on Scrum.org, seven years apart, both read the Guide's silence as
deliberate rather than an oversight.** Barry Overeem, in 2016: "So why isn't the Definition of Ready
described in the Scrum Guide? Because it is. However not as a checklist but as an activity: backlog
refinement" [[19]](#ref-19). Joanna Płaskonka, in 2023: "Is Definition of Ready obligatory in Scrum? The
answer is short: no" [[20]](#ref-20). Both are individually authored posts on Scrum.org, not Scrum.org
policy, and this companion cites them that way.

No source read for this bundle documents the practice changing shape over time the way, for instance, a
standards body's own text would. What exists instead is a spread of independent practitioner
formulations from 2008 onward, each adding or trimming criteria on its own authority, which is itself
consistent with the dispute in [section 6](#6-debates-and-contested-boundaries): there is no single
lineage to converge on because there is no standards body steering it.

---

## 3. Anatomy (section by section)

The template ships one size, `lean`, with five sections. Each is covered here once, in template order.

### 3.1 Why We Keep One

**What it is.** A short statement of the specific problem this team's Definition of Ready exists to
solve, plus the condition under which the team would drop it.

**Why it exists.** Mountain Goat Software gives the reason a team keeps one at all: "The goal is to
prevent problems before they have a chance to start" [[14]](#ref-14). Allan Kelly gives the reason to
stop: he can see why a team adopts one and "might even recommend it myself but I'd hope it was an
temporary measure on the way to something better" [[15]](#ref-15) (the source's own wording, typo kept,
because this bundle quotes verbatim rather than silently correcting a source). No source read for this
bundle states a condition for retiring a Definition of Ready once adopted. This section asks the team to
write its own, and it is labelled in the template as this library's own contribution, not received
practice.

**Beginner note.** Write the actual pain, not agile vocabulary. "We keep pulling in stories the team
doesn't understand and losing the first two days of the sprint to questions" is a reason; "to ensure
alignment" is not.

**Expert note.** If a team cannot fill this section honestly, that is itself informative: the Agile
Alliance's neutral framing is that a Definition of Ready "provides the team with an explicit agreement
allowing it to "push back" on accepting ill-defined features" [[6]](#ref-6). A team with nothing to push
back against may be a candidate for keeping none, which [section 6](#6-debates-and-contested-boundaries)
treats as a legitimate outcome, not a gap.

### 3.2 Scope and Ownership

**What it is.** Which kinds of backlog items the Definition of Ready applies to, at which recurring
moment it is checked, and who owns it.

**Why it exists.** Ownership is where the sources that address it converge most closely: Roman Pichler, "I suggest that the definition of ready (DOR) is jointly owned by the product
owner and the team" [[10]](#ref-10); Atlassian, "Remember that the DoR is created for the team, by the
team" [[9]](#ref-9); Boldare, "agreed by the whole Scrum team" [[29]](#ref-29); Microsoft, "The ready
checklist can be written by a Product Owner in agreement with the development team and the Process Lead"
[[7]](#ref-7), the weakest form of the same agreement, since one role writes and the others agree.
t2informatik names what goes wrong when ownership slips to one role: "the Definition of
Ready is used as an argument and reason for rejecting backlog items" [[27]](#ref-27).

The moment it is applied has two names in the sources this bundle read, and both are real: Boldare
treats it as refinement's own success test, "Refinement results in product backlog items that are ready
for development, and the Definition of Ready is the criteria by which we can say that refinement has
been successful" [[29]](#ref-29); the 2020 Scrum Guide names the moment at sprint planning instead,
"Product Backlog items that can be Done by the Scrum Team within one Sprint are deemed ready for
selection in a Sprint Planning event" [[4]](#ref-4). The template does not force a single answer because
the sources do not.

**Beginner note.** Name the item types this applies to. Microsoft's own playbook writes the type for user
stories specifically [[7]](#ref-7); say so explicitly if a team also applies it to bugs or spikes. Pick
one of refinement or sprint planning as the moment this team actually checks it, or both.

**Expert note.** Microsoft's own caution scopes the checklist itself, not just who owns it: "The ready
checklist should contain items that apply broadly. Don't include items or details that only apply to one
or two user stories" [[7]](#ref-7). A criterion that only one story ever needs belongs in that story's
own acceptance criteria, not here.

### 3.3 Readiness Criteria

**What it is.** The load-bearing section of the document: each criterion stated as a question, the
evidence that answers it, and whether missing it stops the item at the door or only starts a
conversation.

**Why it exists.** This is where the dispute in [section 6](#6-debates-and-contested-boundaries) is
concentrated, and the template resolves it structurally rather than by argument: every criterion is a
guideline with a stated consequence, never a silent rule. The TRAP this section names comes directly
from Mountain Goat Software: "If these rules include saying that something must be 100 percent finished
before a story can be brought into an iteration, the definition of ready becomes a huge step towards a
sequential, stage-gate approach" [[14]](#ref-14). Robert Cooper's own description of what a stage gate
actually is makes clear why that matters: a stage gate is "an explicit decision point where the business
must choose whether and how to continue investing," with outcomes of "Go, Kill, Hold, or Recycle"
[[22]](#ref-22). A Definition of Ready with those outcomes has stopped being a Definition of Ready.

**One hard stop does have a source**, and it is the single exception this bundle's research found
anyone naming without hedging: Mountain Goat Software allows "the possible exception of dependencies on
certain teams or vendors" [[14]](#ref-14) as a rule rather than a guideline, because a team cannot
negotiate its way past another team's calendar.

Two competing shapes for what the criteria actually ask exist in what this research read, and the
template offers the questions either can ask rather than adopting one list wholesale. Roman Pichler's
three: a story is "clear if all Scrum team members have a shared understanding of what it means," it is
"feasible if it can be completed in one sprint, according to the definition of done," and it is
"testable if there is an effective way to determine if the functionality works as expected"
[[10]](#ref-10). Atlassian presents Bill Wake's six-part INVEST heuristic as a Definition of Ready's
components [[9]](#ref-9), but Wake's own article, the origin of INVEST, never uses the phrase
"Definition of Ready" [[11]](#ref-11); this bundle cites him for INVEST's origin only, not as a source
for the type itself. Microsoft's playbook, the one source in this research licensed for its wording to
be adapted, supplies example checklist items in a Definition of Ready's own voice [[7]](#ref-7)[[8]](#ref-8),
and Scrum Alliance offers one worth naming directly: "No blockers have been found that cannot be
addressed by the team during the sprint" [[12]](#ref-12).

**Beginner note.** Write each criterion as a question a reviewer could actually answer yes or no to
("Has the team agreed what 'done' looks like for this story?"), not as a state ("story is clear").

**Expert note.** If a criterion cannot be answered without the Product Owner personally weighing in
every time, it has probably drifted from a guideline back toward the gate this section exists to avoid.

### 3.4 When an Item Is Not Ready

**What it is.** The stated escape valve: what actually happens when a top-priority item does not meet
the Definition of Ready.

**Why it exists.** Every source in this research that discusses a top item that is not ready supplies
some version of a pressure valve, which is exactly why the template makes it a named
section rather than leaving it implied. RebelScrum's account of a team that refused an urgent item is
explicit that refusal is not the only legitimate outcome: "If an item doesn't fully meet the Definition
of Ready but the Scrum team believes it can be completed within a Sprint, it is acceptable to pull it
into the Sprint" [[26]](#ref-26). Allan Kelly's alternative is procedural rather than a waiver: "then the
first task is to make it ready" [[15]](#ref-15). Lance Dacy names the mechanism directly: "Let the team
override it with a quick, documented decision" [[17]](#ref-17). Box UK adds a maturity dimension:
newer teams may be advised to treat it "as mandatory, at least to begin with," while the same source
warns against "hard and fast, cannot-go-back phases of development, as this removes agility"
[[28]](#ref-28).

**Beginner note.** Decide, in the document itself, which of these three this team actually does: pull it
in anyway on team judgment, make it ready as the sprint's first task, or override with a documented
decision. Silence on this point is what turns a Definition of Ready into the stage gate
[section 3.3](#33-readiness-criteria) warns against.

**Expert note.** This section is the direct mirror of `definition-of-done`'s "When Work Does Not Meet
It" section: both exist because a standard nobody can bend under real pressure is a standard people
learn to route around instead of honour.

### 3.5 Review Trigger

**What it is.** A named condition, not a calendar date, that tells the team its Definition of Ready has
gone stale, and who is responsible for noticing.

**Why it exists.** The `standing-standards` family's own contract requires every member to carry this
mechanism, because both members of the family fail the same quiet way: by drifting out of date while
everyone still believes they are current. What makes this section distinctive for a Definition of Ready
is that the trigger has to fire in **both** directions, and both directions are sourced in this
research. Too loose: Microsoft's own guidance is to "Update or change the definition of ready anytime
the scrum team observes that there are missing information in the user stories that recurrently impacts
the planning" [[7]](#ref-7), and Atlassian names the same signal from the other side, "a lot of
scrambling to understand work within the sprint" [[9]](#ref-9). Too tight: Lance Dacy names the opposite
failure directly, "When the DoR blocks more value than it enables, it stops being a safety rail and
becomes a parking brake" [[17]](#ref-17). Boldare adds a third trigger, ambiguity in the document itself
rather than in its effect: "if a Definition of Ready is at all unclear, you need to revisit the
refinement process" [[29]](#ref-29).

**Beginner note.** Name a person or role who notices, and a concrete signal ("three sprints in a row
where a top item needed the override in [3.4](#34-when-an-item-is-not-ready)"), not "review quarterly."
A calendar date is not a trigger; it is a reminder, and it fires whether or not anything is actually
wrong.

**Expert note.** If this section only ever names the too-loose direction, the document has quietly
assumed the failure mode of a Definition of Done rather than its own. A Definition of Ready that has
never once been loosened is, per the dispute this bundle carries, at least as worth investigating as one
that has never been tightened.

---

## 4. Variants and sizing

**One size ships: `lean`.** This is a deliberate call, not an omission, and the evidence for it runs the
opposite direction from a document that earns a second, heavier weight. No source read argues for a
bigger Definition of Ready, and the sources that address its size at all argue for a smaller one, at
least as a starting point:
Stefan Roock, quoted by InfoQ, "For the Definition of Ready I recommend: The smaller the better," and
"should be shrinking over time and not growing" [[16]](#ref-16); Roman Pichler recommends "starting with
a good-enough DOR and adapting it in the sprint retrospectives if and when necessary" [[10]](#ref-10);
Mountain Goat Software's entire argument is guidelines over rules, never more rules [[14]](#ref-14).
agility.ac's framing of what the whole document should be treats growth itself as a sign of health, not
scope: "a living document that grows with the team as they mature," but as "a checklist of things to
consider, rather than a stage gate" [[30]](#ref-30), which is growth in maturity, not in weight. A `full`
variant that added more criteria sections would model the exact failure this bundle's dispute warns
against, which is why the design choice here is to keep the document itself small rather than to offer a
heavier option a team could reach for under pressure.

**The one place a second weight could honestly exist is readiness above the story, and this research did
not find one document that operates at two levels.** Applied Frameworks publishes a Definition of Ready
for SAFe PI Planning, one level above the sprint story: "Your PI Planning Definition of Ready will
likely revolve around two things: features and knowledge" [[13]](#ref-13). It is a consultancy's own
extension, not a SAFe artifact, since SAFe's glossary has no entry for the type at any level
[[5]](#ref-5). None of the sources read for this bundle publishes a single document that gates readiness
at two levels the way `definition-of-done`'s full variant gates "Criteria by Level," so this companion
describes feature-level readiness here rather than the template carrying it as a section.

**This size call is provisional**, consistent with how this library treats every size call in its
catalog: it is the best reading of the evidence gathered so far, not a claim that no team anywhere would
benefit from a second weight.

---

## 5. Methodology lineage

| School | Treatment | What it optimizes for |
|---|---|---|
| **Scrum canon (2020)** | Never names the phrase. Its own nearest sentence ties readiness to sprint planning: "Product Backlog items that can be Done by the Scrum Team within one Sprint are deemed ready for selection in a Sprint Planning event" [[4]](#ref-4). | Says nothing about a standing artifact; the closest thing is a moment, not a document. |
| **Scrum Patterns / practitioner pattern language** | Publishes it as a named pattern, with a hedged attribution to a 2008 blog post [[2]](#ref-2)[[1]](#ref-1). | A reusable shape a team can adopt deliberately. |
| **Scrum.org (individual authors, not policy)** | Two authors separately argue the Guide's silence is meaningful rather than accidental, one for refinement as the real mechanism [[19]](#ref-19), one for treating the whole practice as optional by design [[20]](#ref-20). | Keeping the practice out of the standard while explaining why. |
| **SAFe** | Its glossary has no entry for a Definition of Ready at all [[5]](#ref-5); one consultancy has published an extension for PI Planning, a level SAFe itself does not define the type for [[13]](#ref-13). | Nothing at the framework level; readiness above the story is a practitioner add-on, not a SAFe artifact. |
| **Testing lineage** | An unofficial mirror of the ISTQB glossary lists "definition of ready" among the synonyms of "entry criteria," "the set of generic and specific conditions for permitting a process to go forward with a defined task" [[21]](#ref-21). | The same entry-gate function, named from a different discipline, corroborated by only one mirror site rather than ISTQB's own text. |

Every source read for this bundle comes from Scrum and agile practice, or from the testing and stage-gate
traditions it is compared with. No other lineage was researched, so this companion adds no row for one.

---

## 6. Debates and contested boundaries

### 6.1 Should a Definition of Ready exist at all?

Three positions, and this research found no fourth. This bundle carries the dispute rather than settling
it, and the template's own design, guidelines over rules, keeping none as a legitimate outcome, a
mandatory pressure valve, is this library's answer to a question none of the three positions themselves
answers on their own.

**Against a rigid one, not against the idea.** Mountain Goat Software: "Avoid including rules that
require something be 100 percent done before a story is allowed into the iteration," and "Favor
guidelines rather than rules on your Definition of Ready" [[14]](#ref-14), while the same source also
says plainly "for most development teams, I do not recommend using a definition of ready" [[14]](#ref-14),
so its position spans this camp and the next one rather than sitting cleanly in either.
Lance Dacy: "a rigid DoR used like a phase-gate can just as easily undermine agility" [[17]](#ref-17).
Stefan Roock, quoted by InfoQ: "The smaller the better" [[16]](#ref-16).

**Against a named, standing artifact at all.** Barry Overeem: "I'm not a big fan of the Definition of
Ready. Quite often it becomes a contract - instead of a guideline - between the Development Team and the
Product Owner," preferring "the activity of Backlog Refinement" instead of "a sequential, phase-gate
checklist" [[19]](#ref-19). Allan Kelly: a Definition of Ready "reduces agility because it breaks up
process flow, assumes greater role specific responsibilities, introduces more wait states (delay) and
potentially undermines business-value based prioritisation" [[15]](#ref-15). Both concede real ground
rather than arguing for pure abolition: Overeem "do[es] support using a checklist that clarifies
'readiness' during backlog refinement" [[19]](#ref-19), and Kelly would himself recommend one "as an
temporary measure on the way to something better" [[15]](#ref-15).

**It depends, decided by the team.** Joanna Płaskonka: "Is Definition of Ready obligatory in Scrum? The
answer is short: no," and "Definition of Ready can be weaponized and it can become a threat to your
Agility" [[20]](#ref-20), handing the decision to the team rather than arguing either side.

**No source read for this bundle argues for a rigid, growing, non-negotiable Definition of Ready.** The
dispute runs from abolition to "keep it small"; there is no opposite pole in what this research found,
and this companion does not invent one for the sake of balance.

### 6.2 Is INVEST the Definition of Ready?

No. Atlassian presents the six INVEST criteria as a Definition of Ready's components [[9]](#ref-9), but
Bill Wake's own article, INVEST's origin, never uses the phrase "Definition of Ready" [[11]](#ref-11),
and Roman Pichler's own three-criterion model, clear, feasible, testable, is a distinct shape
[[10]](#ref-10). This bundle treats INVEST as one possible source of criteria a team might reach for, not
as a synonym for the type, and cites Wake for INVEST alone.

### 6.3 Who coined "ready-ready"?

Unresolved, and this companion does not pick a side. Two lineages exist in what this research read, both
verified, neither citing the other: Kronfält's 2008 blog post names the state directly [[1]](#ref-1), and
Jakobsen and Sutherland separately credit the term to Systematic's own practice [[3]](#ref-3). Which came
first, or whether they are independent coinages of the same idea, is not something this research could
establish, so both are reported and the question is left open.

### 6.4 Three sources not read, and quarantined

Two further pieces on this exact question were not retrieved: a Medium post on the practice's
(dis)advantages returned an access barrier, and a Project Management Institute page on ways to use the
type returned a bot-block page. A third, a chapter in a print book on readiness, was not attempted. None
of the three supports any claim in this companion; the research log records why each was not read.

### 6.5 A synonym this bundle did not expect to find

The research brief for this bundle assumed no source bridges a Definition of Ready and testing's own
vocabulary. One does, though only weakly: an unofficial mirror of the ISTQB glossary lists "definition of
ready" among the synonyms of "entry criteria" [[21]](#ref-21). The mirror states it is based on the
official ISTQB glossary rather than being ISTQB's own site, and whether the synonym reflects ISTQB's own
policy is not something this research could confirm, so this companion reports the synonym with that
caveat rather than as settled cross-discipline agreement.

---

## 7. Anti-patterns and failure modes

1. **The 100-percent rule.** Any criterion phrased as a requirement that something be fully finished
   before entry. Mountain Goat Software names this directly as the mechanism that turns the document
   into "a huge step towards a sequential, stage-gate approach" [[14]](#ref-14).
2. **The Definition of Ready as a rejection weapon.** t2informatik: "the Definition of Ready is used as
   an argument and reason for rejecting backlog items" [[27]](#ref-27), the direct consequence of letting
   one role own the document rather than the whole team.
3. **The contract, not the guideline.** Barry Overeem's own description of what the practice becomes when
   it drifts: "Quite often it becomes a contract - instead of a guideline - between the Development Team
   and the Product Owner" [[19]](#ref-19).
4. **Weaponization.** Joanna Płaskonka names this outcome by its own word: "Definition of Ready can be
   weaponized and it can become a threat to your Agility" [[20]](#ref-20).
5. **The over-regulated process.** A practitioner quoted by InfoQ describes the failure directly: "the
   Definition of Ready may be used to create an over regulated process that impedes collaboration," and
   names the consequence bluntly: "This is NOT Scrum and it is NOT Agile" [[16]](#ref-16). (This research
   log records the quote without a named speaker distinct from Roock's own attributed remark, so this
   companion attributes it to the article rather than to an individual.)
6. **Silent understaffing of the pressure valve.** A Definition of Ready with no stated answer to
   [section 3.4](#34-when-an-item-is-not-ready): Allan Kelly's own account of the cost is that it
   "reduces agility because it breaks up process flow, assumes greater role specific responsibilities,
   introduces more wait states (delay) and potentially undermines business-value based prioritisation"
   [[15]](#ref-15).
7. **The parking brake.** Lance Dacy's own name for a Definition of Ready that has drifted too tight:
   "When the DoR blocks more value than it enables, it stops being a safety rail and becomes a parking
   brake" [[17]](#ref-17).
8. **The irreversible phase.** Box UK's warning against treating adoption as one-way: "it is definitely
   not the intention to promote hard and fast, cannot-go-back phases of development, as this removes
   agility" [[28]](#ref-28).

---

## 8. Relationships to other artifacts

- **Sibling, opposite gate: Definition of Done.** [`../definition-of-done/`](../definition-of-done/)
  gates exit from a sprint; this type gates entry into one. Scrum Alliance draws the boundary directly:
  "The definition of done refers to the PBI itself, while the definition of ready often refers to
  externalities" [[12]](#ref-12), and a practitioner lays out definition of done, definition of ready and
  acceptance criteria side by side as three different jobs [[23]](#ref-23). Allan Kelly collapses the two into one flow-system
  statement worth reporting as a real position rather than smoothing over: "The definition of done at
  the end of one activity is the definition of ready for the next" [[15]](#ref-15).
- **Feeds into: Acceptance Criteria.** [`../acceptance-criteria/`](../acceptance-criteria/) states the
  conditions unique to one backlog item; a Definition of Ready applies across every item and may require
  that acceptance criteria exist without ever stating them itself. Scrum Alliance: "The definition of
  done applies to all work in the backlog. Contrast this with acceptance criteria, which are unique to
  each PBI" [[12]](#ref-12); Debashish Chakrabarty's own summary of the three-way boundary states it in
  one sentence: the Definition of Ready "aims to improve Product Backlog clarity and prevent unprepared
  work from entering the Sprint," distinct from both the Definition of Done's quality floor and
  acceptance criteria's per-item functionality [[23]](#ref-23).
- **What it aims at: Backlog Refinement.** Agile Alliance's own glossary entry names the relationship
  directly: "Definition of Ready involves creating clear criteria that a user story must meet before
  being accepted into an upcoming iteration" [[24]](#ref-24), and Boldare treats it as refinement's own
  success test [[29]](#ref-29). Refinement is the activity; a Definition of Ready is the target it
  refines items toward. The Scrum Guide names refinement itself without the vocabulary: "the act of
  breaking down and further defining Product Backlog items into smaller more precise items"
  [[4]](#ref-4).
- **Not a stage gate.** Robert Cooper's own model decides "Go, Kill, Hold, or Recycle" [[22]](#ref-22)
  at a governance level above the team. A Definition of Ready with those outcomes has become one; see
  [section 3.3](#33-readiness-criteria).
- **Adjacent, from a different discipline: testing's entry criteria.** An unofficial mirror of the
  ISTQB glossary lists this type as a synonym [[21]](#ref-21), with the caveat in
  [section 6.5](#65-a-synonym-this-bundle-did-not-expect-to-find) about how weak that bridge is.
- **Down the pipeline, at scale: PI Planning readiness.** [`../product-backlog/`](../product-backlog/)
  and this type both operate at the story level; Applied Frameworks' consultancy extension applies the
  same idea one level up, at features and program knowledge, for SAFe's PI Planning [[13]](#ref-13).

---

## 9. Adaptations

- **Team new to the practice.** Box UK's own guidance is to start firmer, then loosen: "Inexperienced
  teams may be advised to consider the Definition of Ready as mandatory, at least to begin with," while
  the same source cautions this must not calcify into "hard and fast, cannot-go-back phases of
  development" [[28]](#ref-28). Box UK's broader recommendation is to treat the whole adoption as an
  experiment: "experiment by using the construct on a project, inspect its impact on the project, and
  adapt your approach accordingly" [[28]](#ref-28).
- **Mature team.** Reach for fewer, smaller criteria rather than more: Roock's own maturity signal is
  that the document "should be shrinking over time and not growing" [[16]](#ref-16), and agility.ac
  frames the same trajectory as the document itself maturing with the team [[30]](#ref-30).
  [Section 4](#4-variants-and-sizing) makes this the reason the template ships one size rather than two.
- **Multiple item types.** Microsoft's own scoping advice applies regardless of type: keep criteria
  broad enough to apply across the backlog, and push anything item-specific down into that item's own
  acceptance criteria instead [[7]](#ref-7).
- **Above the story (features, PI Planning).** Treat Applied Frameworks' extension as a distinct,
  consultancy-authored practice rather than an assumed SAFe artifact, since SAFe's own glossary has no
  entry for the type at any level [[13]](#ref-13)[[5]](#ref-5); see [section 4](#4-variants-and-sizing).
- **Regulated or safety-critical work, and solo practitioners.** No source read for this bundle
  discusses either adaptation, and this companion does not invent guidance for them.

---

## 10. Worked example pointer

[`definition-of-ready_example.md`](definition-of-ready_example.md) is the fully worked instance: the
Reporting Squad's first Definition of Ready, written short by design, since a long one would itself
demonstrate the anti-pattern this bundle warns against. It chains onto a sentence
`definition-of-done_example.md` already committed to, that if the squad ever adopted one "it will gate
entry into the sprint, not exit from it, and will not replace anything above," and it uses the one hard
stop this research found anyone naming without a hedge, a cross-team dependency, as its example of
Mountain Goat Software's named exception [[14]](#ref-14).

---

## References

Tagged by the research log's own retrieval discipline: every entry below is `fetched-and-verified` in
[`definition-of-ready_research-log.md`](definition-of-ready_research-log.md), the only status this
bundle permits a quotation from. Numbers match the log's own numbering exactly, so a gap in the sequence
below means that source exists in the log but is not cited in this companion, not that it is missing.
Reliability tiers follow the log's own four-way split: `[primary]` a standards body or an originating
practitioner text with no secondary layer; `[practitioner]` an independent author or blog, not
commercially motivated; `[vendor]` a commercially motivated site, reliable on convention, corroborated
here rather than trusted alone; `[reference]` a glossary or glossary mirror. Researched 2026-09-23.

<a id="ref-1"></a>[1] Richard Kronfält. "[Ready-ready: the Definition of Ready for User Stories going into sprint planning](https://scrumftw.blogspot.com/2008/10/ready-ready-definition-of-ready-for.html)." Scrum FTW, 1 October 2008 (accessed 2026-09-23). [practitioner]

<a id="ref-2"></a>[2] The Scrum Patterns Group. "[Definition of Ready](https://scrumbook.org/value-stream/product-backlog/definition-of-ready.html)" pattern. scrumbook.org, companion site to *A Scrum Book* (Pragmatic Bookshelf, 2019) (accessed 2026-09-23). [practitioner]

<a id="ref-3"></a>[3] Carsten Ruseng Jakobsen and Jeff Sutherland. "[Scrum and CMMI - Going from Good to Great: Are you ready-ready to be done-done?](http://jeffsutherland.com/scrum/JakobsenScrumCMMIGoingfromGoodtoGreatAgile2009.pdf)" (accessed 2026-09-23). [primary]

<a id="ref-4"></a>[4] Ken Schwaber and Jeff Sutherland. "[The 2020 Scrum Guide](https://www.scrumguides.org/scrum-guide.html)." Scrum.org (accessed 2026-09-23). [primary]

<a id="ref-5"></a>[5] Scaled Agile, Inc. "[SAFe Glossary](https://framework.scaledagile.com/glossary)" (accessed 2026-09-23). [vendor]

<a id="ref-6"></a>[6] Agile Alliance. "[Definition of Ready](https://www.agilealliance.org/glossary/definition-of-ready/)," glossary entry (accessed 2026-09-23). [reference]

<a id="ref-7"></a>[7] Microsoft. "[Definition of Ready](https://microsoft.github.io/code-with-engineering-playbook/agile-development/team-agreements/definition-of-ready/)," Code-With Engineering Playbook (accessed 2026-09-23). [practitioner]

<a id="ref-8"></a>[8] Microsoft. "[LICENSE](https://raw.githubusercontent.com/microsoft/code-with-engineering-playbook/main/LICENSE)," code-with-engineering-playbook repository (accessed 2026-09-23). [reference]

<a id="ref-9"></a>[9] Atlassian. "[What is Definition of Ready? DoR Explained & Key Components](https://www.atlassian.com/agile/project-management/definition-of-ready)" (accessed 2026-09-23). [vendor]

<a id="ref-10"></a>[10] Roman Pichler. "[The Definition of Ready in Scrum](https://www.romanpichler.com/blog/the-definition-of-ready/)" (accessed 2026-09-23). [practitioner]

<a id="ref-11"></a>[11] Bill Wake. "[INVEST in Good Stories, and SMART Tasks](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)." xp123.com (accessed 2026-09-23). [practitioner]

<a id="ref-12"></a>[12] Scrum Alliance. "[Definition of Ready vs. Definition of Done: Understanding the Differences](https://resources.scrumalliance.org/Article/definition-vs-ready)" (accessed 2026-09-23). [practitioner]

<a id="ref-13"></a>[13] Applied Frameworks. "[A Definition of Ready for PI Planning](https://appliedframeworks.com/a-definition-of-ready-for-pi-planning/)" (accessed 2026-09-23). [vendor]

<a id="ref-14"></a>[14] Mountain Goat Software. "[Definition of Ready: What It Is and Why It's Dangerous](https://www.mountaingoatsoftware.com/agile/the-dangers-of-a-definition-of-ready)" (accessed 2026-09-23). [practitioner]

<a id="ref-15"></a>[15] Allan Kelly. "[Definition of Ready considered harmful](https://www.allankelly.net/archives/1615/definition-of-ready-considered-harmful/)" (2017) (accessed 2026-09-23). [practitioner]

<a id="ref-16"></a>[16] Ben Linders. "[Using Definition of Ready](https://www.infoq.com/news/2014/06/using-definition-of-ready)." InfoQ (2014) (accessed 2026-09-23). [practitioner]

<a id="ref-17"></a>[17] Lance Dacy. "[Definition of Ready: Guardrail or Roadblock?](https://big-agile.com/blog/definition-of-ready-guardrail-or-roadblock)" Big Agile (3 June 2025) (accessed 2026-09-23). [practitioner]

<a id="ref-19"></a>[19] Barry Overeem. "[Why isn't the Definition of Ready described in the Scrum Guide?](https://www.scrum.org/resources/blog/why-isnt-definition-ready-described-scrum-guide)" Scrum.org blog (5 September 2016) (accessed 2026-09-23). [practitioner]

<a id="ref-20"></a>[20] Joanna Płaskonka. "[Ready or Not? Demystifying the Definition of Ready in Scrum](https://www.scrum.org/resources/blog/ready-or-not-demystifying-definition-ready-scrum)" Scrum.org blog (27 September 2023) (accessed 2026-09-23). [practitioner]

<a id="ref-21"></a>[21] ISTQB Glossary (unofficial mirror). "[Entry Criteria](https://istqb-glossary.page/entry-criteria/)" (accessed 2026-09-23). [reference]

<a id="ref-22"></a>[22] Robert G. Cooper, Stage-Gate International. "[The Stage-Gate Model: An Overview](https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/)" (accessed 2026-09-23). [primary]

<a id="ref-23"></a>[23] Debashish Chakrabarty. "[Definition of Done, Definition of Ready and Acceptance Criteria are not the same darn thing](https://agilechronicles.substack.com/p/definition-of-done-definition-of)." The Agile Chronicles (accessed 2026-09-23). [practitioner]

<a id="ref-24"></a>[24] Agile Alliance. "[What is Backlog Refinement (or Backlog Grooming)?](https://agilealliance.org/glossary/backlog-refinement/)," glossary entry (accessed 2026-09-23). [reference]

<a id="ref-26"></a>[26] RebelScrum. "[Ready or Not!](https://www.rebelscrum.site/post/ready-or-not)" (accessed 2026-09-23). [practitioner]

<a id="ref-27"></a>[27] t2informatik. "[What is a Definition of Ready?](https://t2informatik.de/en/smartpedia/definition-of-ready/)" Smartpedia (accessed 2026-09-23). [vendor]

<a id="ref-28"></a>[28] Box UK. "[Definition of ready in agile](https://www.boxuk.com/insight/definition-of-ready-in-agile/)" (accessed 2026-09-23). [vendor]

<a id="ref-29"></a>[29] Boldare. "[Definition of Ready and Backlog Refinement Process](https://www.boldare.com/blog/definition-of-ready-and-backlog-refinement-process/)" (accessed 2026-09-23). [vendor]

<a id="ref-30"></a>[30] agility.ac. "[What is a definition of ready?](https://agility.ac/frequent-agile-questions/what-is-a-definition-of-ready)," Frequent Agile Questions (accessed 2026-09-23). [practitioner]
