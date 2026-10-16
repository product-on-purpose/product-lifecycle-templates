# Guide: Use Case Specification (operator card)

Self-grade against this before you share a use case specification. For the full reasoning, the
field-by-field provenance and where practitioners disagree, read
[`use-case-specification_companion.md`](use-case-specification_companion.md). A fully worked instance
is [`use-case-specification_example.md`](use-case-specification_example.md).

---

## When to use

- One named actor has one goal, and the system's behavior toward that goal needs writing down step by
  step, success included. A use case states a numbered main scenario plus the branches that can go
  another way; a single sentence or a pass/fail check will not carry that.
- The branches matter as much as the happy path, or more. Cockburn's own account puts the use case's
  greatest value in its alternative behaviors, not its main scenario, so reach for this type when a
  reader genuinely needs every detected deviation and where it ends up, not just the success story.
- This document will be elaborated into acceptance criteria or test cases downstream, and the person
  writing those needs a complete set of flows to derive them from, not a one-line summary.
- A project is running several related use cases that reference each other, need a shared stakeholder
  list, or need the same project annotation (priority, performance target, frequency) recorded once per
  use case rather than scattered across other documents.

## When NOT to use

- **The work is still a conversation starter, not a specified flow.** A user story is a placeholder for
  a future conversation; use [user stories](../user-stories/user-stories_guide.md) and come back to a
  use case specification once the flow itself, not just the goal, needs writing down.
- **You need field-level data definitions.** A data dictionary or data map is the sourced home for what
  a field means and holds; use [data-dictionary](../data-dictionary/data-dictionary_guide.md) and keep
  this document free of data descriptions.
- **You need to say how the system is built, not what it does from outside.** This bundle templates the
  black-box reading only: the system's behavior as seen from outside it. A reader who wants the
  internals wants [sdd](../sdd/sdd_guide.md) instead.
- **You need to check whether a path already works, not specify what it should do.** That is
  [test-case](../test-case/test-case_guide.md); a use case is missing the data values a test case
  needs, and is not itself a test plan.
- **You need a diagram or a board, not prose.** A flow diagram or wireflow is this library's nearest
  kept-out neighbor to this type; this bundle does not template a diagram, and that neighbor's own
  placement in the library is still undecided.
- **The whole thing is genuinely two to six sentences with no real branching.** That is Cockburn's own
  brief form, and it sits below anything this library templates. Write it as a note, not a document.

## Pick a variant

| If the use case is... | Use |
|---|---|
| Low-ceremony, early-stage, or you need the main path and one line on each known deviation | **lean** |
| Formal, critical, or complex enough that a reviewer needs the full header, the stakeholder list, and every branch numbered and findable on its own | **full** |

Cockburn names three degrees of formality: brief, casual, and fully dressed. This library ships `lean`
for casual and `full` for fully dressed, and **that mapping is this library's own choice, not a reading
any source states.** Cockburn's own casual form is written as prose paragraphs; the lean template keeps
numbered steps instead, so lean is casual's nearest equivalent in how much it covers, not in what shape
it takes. Lean drops the project annotation and the separate Extensions section the way casual drops
them, and asks for each known deviation in one line of prose inside the Main Success Scenario rather
than opening a separate section for them.

**Growing lean into full.** Cockburn's own writing order moves from lower precision to higher: the
actor's name and goal first, then the main scenario, then the extension conditions, then the
extension-handling steps. Follow the same order to grow a lean use case into a full one: add Scope and
Level, Stakeholders and Interests, a separate Extensions section, Related Information, and Open Issues
and Schedule, at the points the full template places them. Never reorder or rename the five sections the
two variants share; the full variant is a strict superset of the lean one.

---

## The rubric

Score each row 0, 1 or 2. Under 13 out of 18 on the full variant, a reviewer cannot confirm every path
was actually considered, and the document comes back for another pass before it feeds acceptance
criteria or tests downstream rather than going out as finished. The lean variant carries only the first
five rows (maximum 10); the same consequence applies under 7.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Named for the goal** | Titled after a feature, screen, or system area | Names a goal, but a different use case could plausibly share the same title | Names this actor's specific goal as a verb phrase, and a different feature built the same way would not earn this title |
| 2 | **Intention, not UI** | A step names a screen element ("clicks Submit", "a form appears") | Mostly intention, with one or two interface words left in | Every step survives a redesign of the interface unchanged; you could swap the UI and not touch a word |
| 3 | **Deviations handled** | No deviation is handled, or one is named with no stated outcome | At least one deviation states both a condition and where it ends up | The branches took more drafting effort than the main scenario, and each names the condition the system actually detected and whether it rejoins, succeeds separately, or fails |
| 4 | **Guarantee survives failure** | Only a success condition is stated; failure is untreated | A failure condition is named, but only as an absence of failure ("nothing crashes") | A positive, checkable condition holds on every exit, success included, stated separately from what additionally holds only on success |
| 5 | **Preconditions state facts** | Preconditions are blank, "none," or restate the trigger | Preconditions list facts but blur into actions the actor takes once the case has started | Preconditions state only what is already true before the trigger; the trigger names one event, action or time-based, that starts the case |
| 6 | **Black-box scope** *(full only)* | Scope names internal components or how something is built | Scope names the system, but some internal detail leaks in | Scope names what the system does, seen from outside, with no implementation detail, and level is stated |
| 7 | **Stakeholders beyond actor** *(full only)* | No stakeholder beyond the primary actor is named | Stakeholders are listed, but their interests are generic enough to belong to any use case | At least one stakeholder who never touches the system directly is named, with a specific, checkable interest |
| 8 | **Rules linked, not copied** *(full only)* | A business rule's text is copied inline, or a requirement shared by many use cases is restated here | Some rules are referenced by identifier; others are still restated | Every business rule a step enforces is referenced by identifier with where its text lives, and anything that applies to many use cases is linked, not copied |
| 9 | **Open issues owned** *(full only)* | An open issue is listed with no owner | An owner is named, but no date by which it must be resolved | Every open issue names both an owner and when it must be resolved by |

**Which rows apply to what.** Rows 6 through 9 grade sections the lean variant does not ship at all
(Scope and Level, Stakeholders and Interests, Related Information, and Open Issues and Schedule), so
scoring lean against them would penalize the choice of variant rather than the quality of the document.

| Variant | Rows that apply | Maximum | Score against |
|---|---|---|---|
| full | all 9 | 18 | **13** |
| lean | 1-5 (it carries none of Scope and Level, Stakeholders and Interests, a separate Extensions section, Related Information, or Open Issues and Schedule) | 10 | **7** |

Every cell above describes evidence, not a count. That is deliberate: a threshold cleared by adding
items will be cleared by adding items rather than by improving the document, which is exactly what this
library's own research into defect-count gaming documents happening the moment a count becomes a target.
If a cell can be satisfied without making the document better, it is written wrong.

---

## Named anti-patterns

1. **UI standing in for intention.** Writing what the screen does ("clicks Submit") instead of what the
   actor is trying to accomplish. Cockburn names this, alongside including too many details, as the two
   most common and most costly mistakes a use case writer makes; a redesigned screen breaks every step
   written this way.
2. **The happy path gets all the care.** Extensions, or the lean variant's deviation lines, written as an
   afterthought, when the form's own value sits in the branches rather than the main scenario.
3. **A detected condition that never says what was detected.** "Something goes wrong: handle it" names
   no condition the system can actually check for and no outcome; the next reader has to guess both, and
   the branch cannot be verified against anything.
4. **An undefined or generic actor.** "User" stands in for a role so broad the use case could be about
   almost anything, leaving no way to tell a novice's path through the system from an expert's.
5. **A step outside the goal.** A step that happens before the stated precondition, after the stated
   guarantee, or that is otherwise unrelated to the actor's goal is a sign the use case needs to split
   into more than one, not a sign it needs one more step.
6. **Inconsistent terms.** The same thing named two different ways across steps and extensions, so a
   reader tracing a condition back to the step that detects it cannot tell whether it is the same thing.
7. **An unowned open issue.** Recorded as a question with nobody responsible for closing it tends to
   stay open past the date the use case itself is due.
8. **A business rule restated instead of referenced.** Copying a rule's full text into the step that
   enforces it, or restating a requirement that applies to many use cases, instead of naming it by
   identifier and pointing at where its text actually lives.
