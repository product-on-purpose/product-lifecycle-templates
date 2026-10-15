---
status: proposed
date: 2026-10-15
decision-makers: [jprisant]
consulted: [claude]
---

# `use-case-specification` joins `delivery-docs`, and the family's membership test gains the verb "elaborates"

## TL;DR

- **Decision.** The `use-case-specification` bundle declares **`family: delivery-docs`** and
  **`phase: deliver`**, in two sizes, `lean` (Cockburn's casual use case) and `full` (Cockburn's fully
  dressed use case). The [contract](../contracts/delivery-docs.md) moves to `0.3.0`.
- **Why this record is different from every earlier admission except three.** Most admissions to this
  contract (ADR 0042, epic) fit a membership test the contract already stated. This one does not. A
  research pass on 2026-10-12 tested a use case specification against all ten family contracts, and nine
  excluded it outright; `delivery-docs` offered only a strained fit on its five verbs as they stood.
  Admitting it **widens the membership test**, the fourth time this has happened in the library, after
  [ADR 0060 (change-request joins delivery-docs)](0060-change-request-joins-delivery-docs.md),
  [ADR 0067 (tracking-plan joins governance-docs as a sixth member)](0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md)
  and [ADR 0070 (north-star-metrics joins strategy-docs as a fifth member)](0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md).
- **What settled it.** `templates/user-stories/user-stories_guide.md:15` already tells a reader who needs
  "exhaustive actor-system flows" to use a use-case specification. No contract admits the type as written,
  and declining it on family-fit grounds alone would leave that sentence pointing at nothing this library
  ships. `delivery-docs` is the smallest honest widening: its chain already carries one unit of product
  work from definition to delivery, and a use case elaborates one actor's path through that same unit of
  work before acceptance criteria confirm it.
- **What this does NOT decide:** admission, which four independently read sources settle (see
  [`tier2-specs.md`](../tier2-specs.md)); and the placement of `user-flow-task-flow`, the nearest neighbour
  this record keeps out and defers rather than places.
- **Status:** proposed 2026-10-15. Held, like ADR 0060 and ADR 0067 before it, until the maintainer reads
  the contract diff, because a family contract is "adopted only after a maintainer read"
  ([decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer)).

## Context and Problem Statement

One shipped bundle sends a reader to a document this library does not ship.
`templates/user-stories/user-stories_guide.md:15` states, under "When NOT to use": "You need exhaustive
actor-system flows. Use a use-case specification." The companion repeats the boundary from its own side
(`user-stories_companion.md:151-153`): "A use case documents an actor-system interaction in full (main and
alternate flows); a story is a thin slice that triggers a conversation." That sentence has been live since
the bundle shipped, with nothing behind it.

A 2026-10-12 research pass (GitHub issue #254, bundle: use-case-specification) tested the type against
[ADR 0030](0030-templating-scope-markdown-documents.md)'s admission test and against all ten family
contracts, with no family assumed. Four named sources clear admission several times over: Alistair
Cockburn's 1998 Basic Use Case Template, Karl Wiegers's 1999 Use Case Template, IBM/Rational's Rational
Unified Process Use-Case Specification template, and Cockburn's own 2001 pre-publication book draft, which
states the casual-versus-fully-dressed formality scheme directly in its own text. The literal
"Fully Dressed Use Case Template" box on pages 119 to 120 of Cockburn's published book was never read;
every Internet Archive copy is lending-restricted, and a 2026-10-12 gap-fill confirmed the field set
instead from the book's own table of contents, index, and preface, read directly.

## Decision Drivers

- **Do not bend a contract's identity to fit one type.** The same driver ADR 0060 named for change-request.
- **Prefer the smallest widening**, and state it as a widening rather than a reading, following ADR 0060
  and ADR 0067.
- **Follow the library's own routing**: a reader already points at this type from a shipped bundle, and
  declining on family-fit alone would contradict text this library already ships.
- **Name what a verb admits and what it does not**, the same discipline the contract's own "What 'changes'
  admits" paragraph set, so a new verb cannot become a door for everything that resembles it.

## Considered Options

1. **Widen `delivery-docs` with a sixth verb, "elaborates."** Chosen.
2. **Decline on family-fit grounds alone**, in the shape of
   [ADR 0064](0064-deployment-plan-is-declined.md) and
   [ADR 0065](0065-steering-committee-pack-is-declined.md). Rejected: those two were declined because their
   content already ships elsewhere in the library. Here, `user-stories_guide.md:15` says the opposite: it
   names "exhaustive actor-system flows" as something the library does not ship today, so a decline would
   stand in tension with the library's own routing text rather than being corroborated by it.
3. **Hold the question open rather than amend**, per
   [procedure 10](../decision-procedures.md#10-a-family-or-axis-assignment-is-uncertain). This was the
   maintainer's first answer, on 2026-10-13, with the note "clarify more what is intended, gained, and the
   impact of "elaborates"?" Superseded the same day once the verb comparison below answered the note.
4. **A new, one-member family**, on the precedent ADR 0060 considered and rejected for change-request.
   Rejected for the same reason: more machinery for one type, when an existing contract's chain already
   carries the job this type does.
5. **Admit it into `standing-standards` or `qa-docs`.** Rejected by the research: a use case is authored
   once per unit of work, not agreed once and applied every time, and it verifies nothing by itself; both
   contracts exclude it on their own membership clause.

## Decision Outcome

**Chosen: option 1.** The membership clause becomes "it defines, decomposes, elaborates, verifies, changes,
or announces a unit of product work," and the chain sentence gains one link: a use case specification
elaborates one actor's full path through the system to reach a goal, including alternative and exception
flows, between the point a PRD or epic defines the work and the point acceptance criteria confirm it.

### Choosing the verb

The maintainer's first answer, on 2026-10-13, held the placement open and asked for the verb's effect to be
clarified, not asserted. The maintainer agreed that "defines" would confuse readers and asked whether
"extends", "expands" or "clarifies" would serve better. After a comparison of the four, the maintainer chose
"elaborates" the same day ("elaborates, let's go with it"). The comparison was held in conversation and
is not otherwise recorded, so the reasons below are this record's own. "Extends" and "expands" both suggest adding new scope to
the unit of work, which a use case specification does not do: it walks through a path the PRD or epic
already defined, in more detail, without adding anything to what was agreed. "Clarifies" undersells the
content: a use case specification adds a main success scenario and numbered extensions that did not exist
before, not merely a clearer restatement of something already written. "Elaborates" names the actual
relationship: it takes a unit of work already defined elsewhere and works out one actor's complete path
through it, in detail no PRD, epic, or story carries.

### What "elaborates" admits, and what it does not

The contract states the boundary so the new verb cannot become a door for anything that resembles detail
work. It admits a document that walks one named actor through a complete interaction with the system
toward one goal: a main success scenario, stated as a numbered sequence of steps, with the alternative and
exception paths that branch off it. It does **not** admit:

- **A diagram, a board, or a live tool schema.** All four admitting sources ship a written, sectioned
  document. Three independent sources read in this sweep (Fowler, the OMG UML 2.5.1 specification, and a
  2024 conference deck) treat the UML use case diagram as a separate artifact from the written
  specification. The diagram is out of scope under ADR 0030 (templating scope: Markdown documents).
- **A user flow.** `user-flow-task-flow` (`docs/internal/catalog.md:100`, row 57) states its own purpose as
  "Map the steps and decisions a user takes through a task", at category "Design / Architecture" and stage
  "design", and its catalog aliases are "flow diagram" and "wireflow". A bare test of "one actor, one goal,
  step by step" would admit this type too. The exclusion therefore rests on what the catalog says a user
  flow is, a design artifact drawn as a diagram, not on the actor-goal framing alone. A user flow written
  out as text is the case this boundary leaves to that type's own placement, which this record defers
  rather than decides.
- **A document that checks a path rather than specifying it.** `test-case` shares the closest structural
  shape of any shipped bundle (preconditions, steps, expected results), but it verifies behaviour, and
  `qa-docs` already carries it.

**What the library gains.** `user-stories_guide.md:15` has routed a reader to this type since the user
story bundle shipped, naming "exhaustive actor-system flows" as content the library does not carry. The
library gains the thing that sentence has promised and not delivered: a document that actually carries a
main success scenario and its numbered extensions, distinct from a story's single sentence and from
acceptance criteria's discrete pass/fail rules.

**The impact on existing members.** None. No existing member's placement or obligations change. The
membership clause gains one word and the chain sentence gains one clause, the same shape ADR 0060 used for
"changes." `user-stories`, `acceptance-criteria`, `epic`, and `prd` keep their own sections, their own
obligations, and their own chain positions exactly as they stand today. Whether any of their companions
gains a line naming the new neighbour is a build decision, following the precedent ADR 0067 and ADR 0070
both set: neither amendment required an existing member's companion to change.

### Consequences

- **The contract moves to `0.3.0`**, with the widening recorded in its change note and the boundary above
  in section 1.
- **`templates/user-stories/user-stories_guide.md:15` becomes resolvable.** The build must update that line
  so it links to the new bundle rather than naming a type the library does not ship.
- **The catalog entry must be corrected when the bundle lands**, per
  [procedure 1](../decision-procedures.md#1-a-catalog-call-loses-to-research): the `methodology` field
  (`Waterfall/UP/RUP`) has no supporting source among the admitting sources, the `size_variant` field
  (`S/M`) does not name the two sizes this bundle ships, and the `relationships` field is empty while every
  boundary source contrasts the type with the user story.
- **The example chains onto the delivery-docs scenario.** It elaborates the "set a default saved view"
  story already shipped in `user-stories_example.md` and already the subject of
  `acceptance-criteria_example.md`'s Given/When/Then scenarios, dated between the two.
- **`pairs_with: []`.** No skill listed in `tools/known-skills.txt` names a use case specification.

## More Information

- Family contract: [`delivery-docs`](../contracts/delivery-docs.md), adopted by
  [ADR 0020](0020-adopt-delivery-docs-family-contract.md); the previous amendments were
  [ADR 0059 (announcement-internal-comms joins delivery-docs)](0059-announcement-internal-comms-joins-delivery-docs.md)
  and [ADR 0060 (change-request joins delivery-docs)](0060-change-request-joins-delivery-docs.md).
- The precedents for widening a membership test:
  [ADR 0060](0060-change-request-joins-delivery-docs.md),
  [ADR 0067](0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md), and
  [ADR 0070 (north-star-metrics joins strategy-docs as a fifth member)](0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md).
- The exclusion this record could not use: nine family contracts' own membership clauses, read directly
  against the type on 2026-10-12.
- The spec and the admission evidence: [`tier2-specs.md`](../tier2-specs.md), the `delivery-docs` (new
  member, by amendment) section for the use case specification.
- **Build order.** Not yet scheduled; this record is held for the maintainer's read of the contract diff,
  per [ADR 0041](0041-maintainer-preference-sets-the-build-order.md)'s rule that the maintainer's preference
  sets the build order.
