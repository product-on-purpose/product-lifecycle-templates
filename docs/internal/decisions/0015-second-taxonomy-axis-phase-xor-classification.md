---
status: accepted
date: 2026-07-17
decision-makers: [jprisant]
consulted: [claude]
---

# A bundle declares a phase XOR a classification, never both, never neither

## Context and Problem Statement

Every bundle's `<type>_meta.yaml` currently declares a lifecycle `phase` (one of the six from
[ADR 0003](0003-phase-vocabulary.md): `discover`, `define`, `develop`, `deliver`, `measure`,
`iterate`). This has been fine only because all six bundles built so far are genuinely lifecycle
artifacts: four `deliver`, two `develop`.

It stops being fine at the next few bundles. The metadata schema (roadmap WP-21) needs to decide
whether `phase` is a required enum, and it cannot, because some document types have no honest phase.
A Risk Register is maintained across every phase; a Status Report is a communication artifact; a
Definition of Done is a standing agreement. Forcing them into `deliver` or `discover` would be a
polite fiction, and a schema built on a fiction fails the first time someone reads it literally.

This was tracked as open question **TX-1** (surfaced 2026-07-12 by the correction to ADR 0003) and it
**blocks WP-21**.

## Decision Drivers

* WP-21 (the metadata schema) cannot make `phase` required until this is settled.
* The `phase` axis is the taxonomy seam with pm-skills (ADR 0003's whole point). Whatever this library
  does should match how pm-skills already solved the same problem, or the seam is fictional.
* The catalog's own Tier-1 set already contains types with no lifecycle phase, so this is not a
  hypothetical for some far-future bundle.
* A schema field that is a fiction for some values is worse than an honest "this type has a different
  kind of identity."

## Considered Options

* **Option A: adopt a second axis, `phase` XOR `classification`.** Every bundle declares exactly one
  of the two. Mirrors pm-skills.
* **Option B: keep `phase` required for every type.** One axis; force a phase onto every type.
* **Option C: make `phase` optional, add no second axis.** Ship the schema with `phase` optional.

## Decision Outcome

Chosen option: **A**. A bundle's meta declares **either** a `phase` (a lifecycle artifact) **or** a
`classification` (a standing, cross-phase artifact), never both and never neither. The metadata schema
will encode this as an XOR constraint, which resolves WP-21's blocker: `phase` is not "required," it is
"required unless `classification` is present."

**The evidence is not a judgment call; it is a partition.** Verified 2026-07-17 by parsing the
frontmatter of all 68 tracked `SKILL.md` files in pm-skills (`skills/*/SKILL.md`, the canonical
source; `.claude/skills/` is a gitignored build copy and was excluded):

| | Count |
|---|---|
| Skills with a `phase`, no `classification` | 30 |
| Skills with a `classification`, no `phase` | 38 |
| Skills with **both** | **0** |
| Skills with **neither** | **0** |

pm-skills has already run this experiment across 68 skills and landed on a clean disjoint partition. A
skill is either a phase artifact or a classification artifact; the two sets do not overlap and cover
everything. This library adopts the same rule rather than inventing a different one for the same
domain.

The `classification` vocabulary matches pm-skills as built (verified in the same pass):
`foundation` (11), `utility` (12), `tool` (15). The `phase` vocabulary is unchanged from ADR 0003.

That the catalog's own Tier-1 set needs this is independently verified from
[`atlas/catalog-data.json`](../../../atlas/catalog-data.json): of the 27 Tier-1 types, several are
governance or communication artifacts with no lifecycle phase, e.g. **Risk Register**, **RAID Log**,
**Status Report**, and **Definition of Done**. These are exactly the types that would have forced the
fiction.

### Consequences

* Good: WP-21 is unblocked. The schema can require `phase XOR classification` honestly.
* Good: the pm-skills taxonomy seam stays real, on both axes rather than one.
* Good: bundles like a future Risk Register can declare `classification: foundation` truthfully
  instead of picking a phase to satisfy a validator.
* Bad: the schema is slightly more complex (an XOR rather than a single required enum). This is
  complexity the domain actually has, not complexity we added.
* Neutral: the six existing bundles are unaffected. All six are genuine phase artifacts and keep their
  `phase`; none needs a `classification`.

### Confirmation

WP-21's `meta.schema.json` encodes the XOR (a meta validates iff exactly one of `phase` /
`classification` is present, each against its enum), and the gate validates every meta against it. The
first bundle of a standing artifact type (a Risk Register, a Team Charter) will exercise the
`classification` branch; until then the rule is enforced but only the `phase` branch is used.

## More Information

**A prerequisite this decision exposes, handled separately.** The catalog carries a field also named
`phase`, with a *different* 15-value vocabulary (`discovery`, `strategy`, `requirements`,
`governance`, `communication`, `testing`, ...). That is a document *stage*, not a lifecycle phase, and
its near-collisions with the bundle vocabulary (`discovery`/`discover`, `definition`/`define`,
`measurement`/`measure`) would make the schema ambiguous about which `phase` it means. The catalog's
field is renamed to `stage` so the name `phase` is unambiguous library-wide. Recorded as finding TX-2
in `STATE.md` and done alongside this ADR.

This decision corrects a factual error in ADR 0003, which cited "175 SKILL.md files." That number
counted every `SKILL.md` on disk (68 tracked, plus 68 gitignored `.claude/skills/` build copies, plus
`_LOCAL/` backups), i.e. the same 68 skills roughly 2.5 times. The canonical count is **68**. ADR 0003
carries a dated correction.
