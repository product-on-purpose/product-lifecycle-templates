# Guide: Definition of Done (operator card)

The short card. Why the document is shaped this way, and the full argument behind every rule here, is in
[`definition-of-done_companion.md`](definition-of-done_companion.md). A fully worked instance is
[`definition-of-done_example.md`](definition-of-done_example.md).

One framing worth carrying into every use of this card: a Definition of Done is a commitment attached to
the Increment, not a standalone artifact you file and forget. That is a 2020 Scrum Guide change from how a
lot of circulating material still describes it, and it is the difference between a document you are judged
against and a document you wrote once.

## When to use

- A team is forming, or an existing team keeps disagreeing about what "done" actually means for an
  increment, and the argument keeps happening at the worst possible moment: review.
- An organizational standard exists somewhere above the team, but nobody has written down whether this
  team's own criteria only add to it or might quietly undercut it.
- More than one team is building the same product and needs to be working against the same bar, not one
  each.
- The cost of an ambiguous "this does not meet it" moment is high enough to be worth settling in advance,
  before anyone has a stake in the answer.

## When NOT to use

Four documents get conflated with a Definition of Done often enough that reaching for this template when
you need one of them is the more common mistake, not the less common one.

| You actually need | Because |
|---|---|
| **Acceptance criteria** | Acceptance criteria state the conditions for one specific item. A Definition of Done is the standing floor every item must clear regardless of what its own acceptance criteria say. Writing a DoD when you mean one item's criteria produces a document that is either too broad to check or too narrow to reuse. |
| **A Definition of Ready** | The DoR gates entry into work, not exit from it. Note that unlike the DoD, whether a DoR should exist at all is a real, named disagreement in the field, not settled practice; do not present it to your team as if it were. |
| **A quality gate** | A quality gate is an automated, tool-checked pipeline checkpoint. A DoD can cite passing one as a single criterion; it is not itself a quality gate, and folding the whole gate configuration into this document duplicates something that already lives in the pipeline. |
| **Coding conventions** | Style and practice guidance, unenforced by a compiler, human-facing rather than a checkable completion criterion. A DoD may reference a conventions guide; it should not restate it. |

## Pick a variant

**Lean** carries three sections: Scope and Ownership, Done Criteria, and Review Trigger. This is the
minimum for an honest, usable Definition of Done: who it binds, what it requires, and what would make it
stale. Most teams should be running this, not treating it as a placeholder for something bigger.

**Full** inserts three more between Done Criteria and Review Trigger: Criteria by Level, What This
Excludes, and When Work Does Not Meet It.

**The signal to scale up is scope, not team maturity.** Reach for full when at least one of these is true:

- the Definition of Done has to gate more than one cadence (feature, sprint, and release), not just one;
- it has neighbors worth disclaiming explicitly, because a team new to the practice keeps re-litigating the
  boundary against a Definition of Ready or a quality gate;
- the cost of an ambiguous "does not meet it" moment is high enough to be worth writing the consequence
  down in advance.

Otherwise lean is not a compromise. A short, flat checklist scoped to one team is a legitimate, commonly
published shape, not a lesser version of the sectioned form.

## The rubric

Score each 0, 1 or 2. **Under 11 out of 16 on a full Definition of Done, and an increment can clear it
without anyone being able to say who checked what.** Under 7 out of 10 on a lean Definition of Done, and it
cannot carry the "is this actually done" argument it exists to settle, so that argument gets decided on
something other than what the document says.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Bound parties are named** | No one is named as bound; reads like "the team's quality bar" | A role or team is named, but whether an organizational standard exists is unclear | You can name who is bound, and the document states outright whether an organizational standard exists, naming it if so |
| 2 | **No single owner claimed** | One role is named the owner, such as "the Product Owner owns this document" | No sole owner is named, but conformance also is not stated as anyone's job | Conformance is stated as belonging to the people doing the work, collectively, not to one role above them |
| 3 | **Floor never weakens** | An organizational standard is mentioned, but nothing says whether local criteria add to it or could undercut it | It states that the standard is inherited, but you cannot tell which specific items are inherited versus added locally | You can point at which criteria are inherited and which are local additions, and none of the local ones reads as weaker than the inherited floor |
| 4 | **Criteria are checkable states** | Every item is an activity, such as "write tests" or "do a review" | Some items are states; others are still activities or impressions, such as "code is good quality" | Every item is a state a teammate who was not in the room could mark pass or fail without asking what you meant |
| 5 | **Levels sorted honestly** *(full only)* | Every criterion defaults to feature level regardless of whether that is realistic | Some items are sorted by level, but at least one release-only activity, such as a full security audit, still sits at feature level | Every criterion was tested against "can this happen every feature, then every sprint, then only at release" and placed at the level it actually clears, even when that is inconvenient |
| 6 | **Neighbors are distinguished** *(full only)* | The section is blank, or a neighbor, such as a quality gate or a coding-conventions guide, is folded wholesale into this document instead of named | Neighbors are named, but a reader still cannot tell what belongs where without asking | For each neighbor named, you can point at the line that says what it is instead, and any overlap is cited as one line item, not absorbed |
| 7 | **Failure has consequence** *(full only)* | The section is blank, or says something like "we will figure it out case by case" | It says where unfinished work goes, but not who decides it missed the bar | It names where the work goes and who decides, agreed before anyone has a stake in the answer |
| 8 | **Trigger is a condition** | A date-based cadence, such as "reviewed every quarter," or nothing at all | An event is named, but no one is named to notice it | A named event that would make the document wrong, and a named person or role who notices it and brings it back to the team |

Every cell above describes evidence, not a count. That is deliberate: a threshold you can clear by adding
items will be cleared by adding items rather than by improving anything. The test for each cell is whether
someone could satisfy it without making the document better; if they could, the cell is written wrong.

**Which rows apply to what.** Full ships all eight rows because it carries all six template sections. Lean
ships five: it carries no per-level sorting section, no boundary section against this document's neighbors,
and no explicit failure-consequence section, so rows 5, 6 and 7 have nothing to grade.

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| lean | 1-4, 8 | 10 | **7** |
| full | all 8 | 16 | **11** |

## Named anti-patterns

1. **The undocumented DoD.** An unwritten standard is not a lower-cost standard; it is a standard nobody
   can point to when it matters. This is one of the most commonly reported problems with real, in-use
   Definitions of Done.
2. **The DoD written once and never revisited.** Written down at the start, never touched again, until it
   no longer matches how the team actually works. This is exactly the failure the Review Trigger section
   exists to prevent, and it is common enough that "we never got around to updating it" is close to the
   default outcome without one.
3. **The creeping DoD.** Growth without a sorting rule: items get added over time until the document stops
   being usable at the level it was meant to gate. The full variant's Criteria by Level section exists to
   catch exactly this before it happens.
4. **Written without the people who will be held to it.** A Definition of Done authored above the team and
   handed down is a common, well-documented pattern, and it is a surprising one given that the people held
   to it use it every day.
5. **Nobody cares because nobody was asked.** A related but distinct failure: even a well-written DoD gets
   its items quietly omitted when the people executing against it were never involved in writing it.
6. **DoD theatre.** A checklist that exists but is not read, especially when it was externally imposed: the
   team never feels ownership over it and treats it as optional.
7. **Unverifiable criteria.** Items phrased as impressions rather than checkable states, such as "code is
   good quality" or "testing done." Two different reviewers can disagree about whether either one is true,
   which means the criterion is not actually gating anything.
8. **The static DoD, mistaken for stability.** A Definition of Done that never changes can look admirably
   settled. Read the other way, a document that never changes because nobody notices it should have is a
   team that has stopped raising its own quality bar.
9. **Naming a single owner.** Tempting, and common in practice, but no source behind this bundle names a
   sole accountable role. Conformance is collective; authorship is contingent on whether an organizational
   standard exists above the team. Naming one person as the owner misstates how the document is actually
   enforced and gives everyone else permission to stop caring about it.

## When it is good enough

When a teammate who was not in the room can read every criterion and mark it pass or fail without asking
what you meant, when the document says outright who is bound and whether it only adds to a standard above
it, and when everyone already knows where unfinished work goes and who decides it did not clear the bar,
before that decision is ever actually contested.

Then delete every HTML comment, and treat the document as something you are judged against, not something
you filed. The Review Trigger you wrote is what keeps that true after today.
