# Use lowercase phase values matching pm-skills frontmatter

Status: accepted (decided 2026-06-29; transcribed 2026-07-11 from strategy brief section 5; ratified 2026-07-12)
Date: 2026-06-29
Deciders: jprisant

## Context and problem statement

The design spec wrote `phase: Deliver` (capitalized) while the live pm-skills repo uses lowercase `phase: deliver` in real skill frontmatter. The phase axis is the taxonomy seam between the two repos; the seam is only real if the casing matches exactly.

## Considered options

* Option A: lowercase values matching pm-skills as built: `discover`, `define`, `develop`, `deliver`, `measure`, `iterate`, plus `foundation` and `tool`.
* Option B: the design spec's capitalized Triple Diamond labels.

## Decision outcome

Chosen option: A, verified against the actual pm-skills frontmatter (`skills/deliver-prd/SKILL.md`). The design spec's casing was corrected rather than propagated.

### Consequences

* Good: `pairs_with` and phase filtering resolve against pm-skills without a translation layer; one vocabulary across the ecosystem.
* Accepted risk: none material; the eight allowed values should be enforced by the metadata schema (audit package, machine-metadata spec) so the vocabulary cannot drift.
* Scope note: the plan's version of this decision also prescribed `<phase>-<doctype>` bundle IDs; that half was superseded by practice and is recorded separately in 20260630-bundle-ids-doctype-spine.md.
