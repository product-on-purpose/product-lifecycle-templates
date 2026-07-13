---
status: accepted
date: 2026-06-29
decision-makers: [jprisant]
---

# Use lowercase phase values matching pm-skills frontmatter

## Context and Problem Statement

The design spec wrote `phase: Deliver` (capitalized) while the live pm-skills repo uses lowercase `phase: deliver` in real skill frontmatter. The phase axis is the taxonomy seam between the two repos; the seam is only real if the vocabulary matches exactly.

## Considered Options

* Option A: lowercase values matching pm-skills as built: `discover`, `define`, `develop`, `deliver`, `measure`, `iterate`.
* Option B: the design spec's capitalized Triple Diamond labels.

## Decision Outcome

Chosen option: A. The design spec's casing was corrected rather than propagated.

The phase enum is **six values**, verified 2026-07-12 by enumerating every `phase:` across all 175 `SKILL.md` files in pm-skills rather than by sampling one:

| Value | Skills carrying it |
|---|---|
| `deliver` | 18 |
| `measure` | 17 |
| `define` | 15 |
| `discover` | 13 |
| `iterate` | 12 |
| `develop` | 12 |

### Consequences

* Good: `pairs_with` and phase filtering resolve against pm-skills without a translation layer; one vocabulary across the ecosystem.
* Accepted risk: none material. The **six** allowed values should be enforced by the metadata schema (see the machine-metadata spec in the audit package) so the vocabulary cannot drift.
* Scope note: the plan's version of this decision also prescribed `<phase>-<doctype>` bundle IDs. That half was superseded by practice and is recorded separately in [0005-bundle-ids-doctype-spine.md](0005-bundle-ids-doctype-spine.md).

## Correction (2026-07-12)

**This record was wrong on the day it was ratified. The error is named here rather than quietly edited, because a governance record that silently rewrites itself is worth less than one that shows its scars.**

As transcribed, it claimed the enum was **eight** values: the six above "plus `foundation` and `tool`". It justified that with the line "verified against the actual pm-skills frontmatter (`skills/deliver-prd/SKILL.md`)". That check read exactly one skill, which trivially reports `deliver`. It could not have discovered the enum, and it did not.

What is actually true is that **pm-skills has a two-axis taxonomy, and this record collapsed it into one**:

- **89** of its 175 skills carry a `phase:` field, drawn from the six lifecycle values above.
- **86** carry **no `phase:` field at all**. They sit on a separate axis, `classification:`, whose values are `foundation` (22 skills), `utility` (27), and `tool` (30). See `foundation-lean-canvas/SKILL.md`: `classification: foundation`, and no phase anywhere in its frontmatter.

So `foundation` and `tool` are not phases. They are values on a different axis, and `tool` is one of three there, not one of two.

Left uncorrected, this record would have instructed the metadata schema (roadmap WP-21, the metadata schema, in milestone M2) to enforce an eight-value phase enum, breaking the exact pm-skills seam this decision exists to protect. The irony is the useful part: the record's own stated rationale is that the seam is only real if the vocabulary matches, and it got the vocabulary wrong.

The **decision** stands unchanged: lowercase, matching pm-skills. Only the factual claim about the enum was defective.

### What this correction opens

pm-skills needs a second axis because roughly half its skills have no lifecycle phase. This library has never asked whether it needs the same thing. Today every bundle carries a `phase:` and nothing carries a `classification:`, and that has been fine only because all four bundles so far are genuinely `deliver` artifacts.

It will not stay fine. Several catalog types plausibly have no lifecycle phase at all: a glossary, a team charter, a decision record. Forcing them to declare one would be the same category error this correction just fixed, one level up.

This is now a live question, not an answered one, and it must be settled **before** the metadata schema hardens `phase` into a required six-value enum. "Required" is the wrong answer if some document types have nothing true to put there. Tracked for milestone M2 (roadmap WP-21, the metadata schema).

## More Information

Provenance: accepted (decided 2026-06-29; transcribed 2026-07-11 from strategy brief section 5; ratified 2026-07-12; **factually corrected 2026-07-12, see Correction below**)
