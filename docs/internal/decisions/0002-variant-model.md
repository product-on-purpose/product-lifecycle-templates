---
status: accepted
date: 2026-06-29
decision-makers: [jprisant]
---

# Ship lean/full variants with descriptive filenames and a strict nesting rule

## Context and Problem Statement

The design spec mandated rigid S/M/L variants with abstract filenames (`template.s.md`); the later layered-design doc softened this to "default lean/full, descriptive filenames, S/M/L only where a type earns three weights." The two positions produce different repositories, and the choice is expensive to reverse once bundle content exists.

## Considered Options

* Option A: lean/full descriptive filenames; ship the number of variants a type earns; keep the nesting discipline.
* Option B: rigid S/M/L with abstract size-letter filenames for every type.

## Decision Outcome

Chosen option: A. The catalog's own size_variant column shows most types vary in two weights, not three; descriptive filenames are self-documenting; and deterministic agent selection runs off the `sizes_available` metadata field, not the filename. The **nesting rule is retained in full force**: a smaller variant's section IDs are a strict ordered subset of the larger's, enabling upgrade-in-place.

### Consequences

* Good: no empty third variant padded out of obligation; filenames readable; nesting preserves the upgrade path.
* Accepted risk: a fixed S/M/L vocabulary is marginally easier for agents to select against; mitigated by `sizes_available` plus (later) `default_size` and `sizing_guidance` metadata.
* Note for single-size types (seven Tier-1 types are S-only per the catalog): the machine-metadata spec (audit package) proposes `sizes_available: [lean]` with the nesting check waived; record that refinement as its own decision when the first single-size bundle is built.

## More Information

Provenance: accepted (decided 2026-06-29; transcribed 2026-07-11 from strategy brief section 5; ratified 2026-07-12)
