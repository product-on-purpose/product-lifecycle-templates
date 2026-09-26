---
status: proposed
date: 2026-09-25
decision-makers: [jprisant]
consulted: [claude]
---

# `announcement-internal-comms` joins `delivery-docs` at `phase: deliver`, not the `communication-docs` family that forecast it

## TL;DR

- **Decision.** The `announcement-internal-comms` bundle declares **`family: delivery-docs`** and
  **`phase: deliver`**. Its scope is the **internal** announcement of a product launch or change: written for
  people in the organization who did not do the work (support, sales, other teams, leadership), telling them
  what is launching or changing, why, what it means for them and what they must do. The
  [contract](../contracts/delivery-docs.md) moves to `0.2.0`, together with
  [ADR 0060 (change-request joins delivery-docs)](0060-change-request-joins-delivery-docs.md).
- **Why a record is needed.** The [`communication-docs` contract](../contracts/communication-docs.md) named "a
  release announcement distinct from `release-notes`" as a likely member, and
  [ADR 0034](0034-adopt-communication-docs-family-contract.md) repeated it. This record sends the type
  somewhere else, so the forecast needs an answer, not a silent contradiction.
- **What settled it: the axis, not the membership test.** `communication-docs`' membership test fits an
  announcement well. Its only axis value does not: ADR 0034 justified `classification: utility` as
  "maintained, periodic, valuable only while current", and an announcement is written once and never
  revised. The library's schema defines `classification` as a "standing (cross-phase) artifact". The only
  contract whose membership test admits the type **as written** is `delivery-docs` ("announces a unit of
  product work"), whose `phase: deliver` describes it honestly.
- **What this does NOT decide:** admission, which retrieval settled in
  [`tier2-specs.md`](../tier2-specs.md) (three qualifying sources, all vendor or practitioner tier).
- **Status:** proposed 2026-09-25. The maintainer chose `delivery-docs` for this type on 2026-09-25, after the
  research; the record is held until the maintainer has read the contract diff it carries, because a family
  contract is "adopted only after a maintainer read" ([`decision-procedures.md`](../decision-procedures.md)).

## Context and Problem Statement

`release-notes_guide.md` routes a reader who needs "a full launch plan and comms" to "a launch checklist and
announcement". The launch checklist shipped in `v0.12.0`; the announcement is catalog entry
`announcement-internal-comms` ("Announcement / Internal Comms", aliases `internal memo`, `launch
announcement`, `Slack canvas`). The maintainer directed its build on 2026-09-24 under
[ADR 0041](0041-maintainer-preference-sets-the-build-order.md) (GitHub issue #177, build-candidate 3).

A research pass on 2026-09-25 tested the type against the membership section and axis rule of all nine
family contracts. Two admitted it:

| Contract | Membership test | Axis | Verdict |
|---|---|---|---|
| `communication-docs` | "exists to tell people who are not doing the work what is happening with it" | `classification: utility`, justified as "maintained and periodic" | Admits with strain: the test fits, the axis does not |
| `delivery-docs` | "defines, decomposes, verifies, or announces a unit of product work" | `phase: deliver` | Admits as written |

The other seven exclude it: it decides nothing (`discovery-docs`, `strategy-docs`), verifies nothing
(`qa-docs`), is not a technical decision (`decision-docs`), does not look back (`process-docs`), is not a
standing instrument (`governance-docs`), and is written per occasion rather than "agreed once and applied
every time" (`standing-standards`).

## Decision Drivers

- **The metadata must stay honest** ([ADR 0020](0020-adopt-delivery-docs-family-contract.md)'s driver, and
  the reason `classification` exists at all, [ADR 0015](0015-second-taxonomy-axis-phase-xor-classification.md)).
  A one-shot document declared as a standing instrument is the "polite fiction" ADR 0015 was written to stop.
- **The membership test governs a candidate**, not a family's forecast list
  ([ADR 0050](0050-qa-docs-admits-a-fourth-member.md) held the same for a contract's descriptive sentence).
- **A forecast is a hypothesis made before the evidence**
  ([procedure 10](../decision-procedures.md#10-a-family-or-axis-assignment-is-uncertain)): the call is made
  against the family's actual members when the type is researched.

## Considered Options

1. **`delivery-docs`, `phase: deliver`.** Chosen.
2. **`communication-docs`, `classification: utility`, with the contract's axis justification reworded** from
   "maintained and periodic" to "has no phase of its own and loses its value when it is no longer current".
   The case for it: the contract named the type, its no-new-facts discipline suits an announcement, and
   pm-skills classifies its own per-occasion communication skills (`foundation-stakeholder-update`) on the
   classification axis. Rejected below.
3. **A phase-axis member inside `communication-docs`.** Rejected: the family is registered in check K on one
   axis, and a member on the other would need a gate change and break the family's single-axis shape for one
   type.

## Decision Outcome

**Chosen: option 1, `delivery-docs` at `phase: deliver`.**

**Why option 2 does not carry.** Rewording the justification would not make the value honest, because the
value's meaning is library-wide, not family-local: the metadata schema describes `classification` as "the
standing-artifact class for a cross-phase document with no single lifecycle phase", and `governance-docs`
defines `utility` as "a standing operational instrument". pm-skills' usage is looser, but this library adopted
the vocabulary and then defined it. The scope settles the phase question: the announcement this library is
building is the announcement of a **launch or change to a unit of product work**, which is what the
`release-notes` routing asks for, and that happens at delivery.

### Consequences

- **The contract moves to `0.2.0`** (with ADR 0060). The chain sentence gains the internal announcement beside
  the release note: the release note records and announces what changed, and the internal announcement tells
  the people who did not do the work what it means for them and what they must do. **The line is drawn by
  purpose, not audience**: `release-notes_companion.md` already recommends shipping "the full notes internally
  and the lean notes externally", so "customers versus colleagues" would contradict a shipped bundle. **That
  split is this library's own boundary**; no source read draws it in those words, and the bundle must label it
  so.
- **The `communication-docs` forecast is corrected in place, with a date**, not deleted. That family stays at
  one member, which its contract calls "an acceptable outcome rather than a defect". The other two candidates
  it forecasts (an executive briefing or steering pack, a stakeholder update) are untouched.
- **The alias collision must be fixed by the build.** `release-notes` carries the alias `release
  announcement`, the exact phrase the forecast used for this type. The new bundle must not take that alias,
  and its `summary` must say "internal" plainly, or an agent selecting by alias reaches the wrong bundle.
- **Its admission is vendor and practitioner tier only**: Staffbase, GitLab's handbook, and Jason Fried's
  account of Basecamp's internal "Deployment" posts. No standards body publishes the document. The
  `communication-docs` contract predicted exactly this about the category ("its literature is thin and
  vendor-dominated"), and the bundle inherits the obligation to say so rather than dress vendor content as
  practice.
- **`pairs_with: []`.** No pm-skills skill produces an internal launch announcement; the nearest,
  `foundation-stakeholder-update`, translates a meeting's outcomes for people who were not there.

## More Information

- Family contract: [`delivery-docs`](../contracts/delivery-docs.md), adopted by
  [ADR 0020](0020-adopt-delivery-docs-family-contract.md); the chain-sentence precedent is
  [ADR 0042 (epic joins delivery-docs)](0042-epic-joins-delivery-docs.md).
- The forecast this record answers: [`communication-docs`](../contracts/communication-docs.md) section 1, and
  [ADR 0034](0034-adopt-communication-docs-family-contract.md), which is left as written.
- The spec and the admission evidence: [`tier2-specs.md`](../tier2-specs.md).
