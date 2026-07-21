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
| [0011](0011-madr-v4-at-docs-internal-decisions.md) | Adopt MADR v4, locate records here, and correct rather than supersede transcription errors | 2026-07-13 |
| [0012](0012-evidence-outranks-catalog-and-paired-skill.md) | Primary evidence outranks the catalog and the paired skill; conflicts are reported, not absorbed | 2026-07-14 |
| [0013](0013-local-split-and-going-public.md) | Split `_local/`: promote what public docs cite into `docs/internal/`, untrack the rest, and go public | 2026-07-14 |
| [0014](0014-gate-may-use-pyyaml-for-frontmatter-validity.md) | The gate may use PyYAML for one check (frontmatter validity); the other six stay pure stdlib | 2026-07-16 |
| [0015](0015-second-taxonomy-axis-phase-xor-classification.md) | A bundle declares a `phase` XOR a `classification`, never both, never neither (closes TX-1, unblocks the metadata schema) | 2026-07-17 |
| [0016](0016-adopt-machine-checkable-metadata-schema.md) | A machine-checkable metadata schema (`tools/meta.schema.json`) is the meta contract, validated in CI (WP-21, from RFC-0001) | 2026-07-17 |
| [0017](0017-gate-may-use-jsonschema-for-meta-validation.md) | The gate may use a JSON Schema validator for one more check (meta validation); the stdlib checks stay pure | 2026-07-17 |
| [0018](0018-machine-catalog-generated-manifest.md) | The machine catalog is a generated `manifest.json`, committed to VC and kept fresh by the gate (WP-22, delivers RFC-0001's second artifact) | 2026-07-17 |
| [0019](0019-selection-metadata-and-approx-tokens.md) | Selection metadata: authored `default_size` + `sizing_guidance`, and a generated heuristic `approx_tokens` (no tokenizer dependency) (WP-23) | 2026-07-18 |
| [0020](0020-adopt-delivery-docs-family-contract.md) | Adopt the delivery-docs family contract, enforced by gate check K; methodology is descriptive, not a membership rule (WP-24) | 2026-07-20 |
| [0021](0021-complete-the-tier-1-floor.md) | Complete the Tier-1 floor on a schedule; grow-by-pull governs Tier-2/Tier-3 only (adopts the buildout plan) | 2026-07-20 |

## Correction versus supersession

The rule, from [0011](0011-madr-v4-at-docs-internal-decisions.md):

> A **factual error** in a record gets corrected in place, with the correction dated and the error named. A **change in the decision itself** gets a new number.

[0003 (phase vocabulary)](0003-phase-vocabulary.md) is the worked example. It was transcribed with a false claim about the pm-skills phase enum, but the decision it records (lowercase values matching pm-skills) never changed. Superseding it would tell a future reader that this project once believed something different about phase casing, which it never did. So it carries a dated Correction instead, and the version history shows exactly what was believed and when it was fixed. A record that silently rewrites itself is worth less than one that shows its scars.
