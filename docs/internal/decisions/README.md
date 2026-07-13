# Decisions

Architectural Decision Records for `product-lifecycle-templates`, following the [MADR v4](https://github.com/adr/madr) standard.

## Format

- One file per decision: `NNNN-short-kebab-title.md`
- Numbered sequentially (0001, 0002, ...) by record-creation order. Records 0001 through 0008 were transcribed in one batch on 2026-07-11 from the strategy brief, the plan, and the shape of the code itself, so their numbers follow decision date rather than creation date; the `date` field is always the date the decision was actually made.
- YAML frontmatter: `status`, `date`, `decision-makers`
- Immutable once accepted. A new decision supersedes an old one rather than editing it.

## Status lifecycle

| Status | Meaning |
|---|---|
| `proposed` | Under consideration, not yet decided |
| `accepted` | Decision made, in effect |
| `deprecated` | No longer recommended, but not replaced |
| `superseded by ADR-NNNN` | Replaced by a newer decision |

## When to create an ADR

Create when:

- The decision shapes the library's structure, its metadata contract, or its authoring rules
- Multiple alternatives were seriously considered
- A future reader (human or agent) would ask "why was this done this way?"
- The decision is hard to reverse, or looks wrong-but-intentional from outside

Do not create for:

- Implementation details (a variable name, a minor refactor)
- Anything already stated in the methodology or the gate

## The records

| # | Decision | Date |
|---|---|---|
| [0001](0001-repo-and-package-name.md) | `product-lifecycle-templates` is the name everywhere; the `pm-` prefix is dropped | 2026-06-29 |
| [0002](0002-variant-model.md) | Ship lean/full variants with descriptive filenames and a strict nesting rule | 2026-06-29 |
| [0003](0003-phase-vocabulary.md) | Use lowercase phase values matching pm-skills frontmatter | 2026-06-29 |
| [0004](0004-first-family-and-bundle.md) | Build `delivery-docs` first, starting with the PRD bundle | 2026-06-29 |
| [0005](0005-bundle-ids-doctype-spine.md) | Bundle IDs are bare document-type handles; phase lives in metadata, never in the path | 2026-06-30 |
| [0006](0006-guidance-style-approach-a.md) | Carry section guidance as enriched HTML comments | 2026-06-30 |
| [0007](0007-research-log-as-bundle-artifact.md) | The research log is a committed bundle artifact | 2026-06-30 |
| [0008](0008-gate-python-local-interim.md) | Ship the governance gate as a local Python script, as a decided interim | 2026-07-03 |
| [0009](0009-scaffold-graduation-flat-templates.md) | Graduate the library out of `_local/` to a flat `templates/` scaffold | 2026-07-12 |
| [0010](0010-meta-declares-size-contract.md) | The meta declares the size contract; single-size bundles are a legal shape | 2026-07-12 |

## A note on 0003

[0003 (phase vocabulary)](0003-phase-vocabulary.md) carries a **Correction** section rather than being superseded. It is worth understanding why, because it tests the immutability rule.

The record was transcribed with a factual error: it claimed the pm-skills phase enum has eight values, "plus `foundation` and `tool`", on the strength of a check that had read exactly one skill file. pm-skills actually has a two-axis taxonomy (six `phase:` values; a separate `classification:` axis for the 86 skills that have no phase at all).

The **decision** was never wrong: lowercase values matching pm-skills, which still stands. Only the transcription's claim about what those values *are* was defective. Superseding a record implies the decision changed. It did not. So the record is corrected in place, with the error named and dated rather than quietly edited, which is what MADR's immutability is really protecting: the version history shows exactly what was believed and when it was fixed.

Correcting a transcription error is not the same as rewriting a decision. If the decision itself ever changes, it gets a new number.
