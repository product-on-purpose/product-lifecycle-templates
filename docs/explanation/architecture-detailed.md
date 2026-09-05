---
title: "Detailed architecture: the bundle contract and the build pipeline"
description: "The mechanics an engineer needs to extend this library safely, from the bundle file contract through every gate check to the six-phase build pipeline"
audience: engineer
level: advanced
tags:
  - architecture
  - governance
  - tooling
doc-role: architecture-detailed
---

# Detailed architecture: the bundle contract and the build pipeline

This page is for someone who is about to add a bundle, add a size or format variant, add a family contract,
or change a gate check, and needs the mechanics precisely rather than the pitch. It assumes you have read
[`what-the-gate-proves.md`](what-the-gate-proves.md) for the honest scope of the quality claim; this page is
about how the machinery that backs that claim actually works, file by file and check by check.

Every mechanism below is named with the file that implements it. Where a rule was set by a decision record,
it is named with a handle and linked under [`../internal/decisions/`](../internal/decisions/).

## The bundle file contract, file by file

A bundle is a folder under `templates/` named by a bare document-type handle (`prd/`, not `deliver-prd/`).
[ADR 0005 (bundle IDs are bare document-type handles)](../internal/decisions/0005-bundle-ids-doctype-spine.md)
settled this: phase lives only in metadata, never in the folder name or the path, so the directory scaffold
is a derivable choice. Every file inside is prefixed with that same handle, so a file is self-identifying if
it is moved or attached out of context.

Six core files exist in every bundle regardless of size (`CORE_ROLES` in
[`tools/check-bundles.py`](../../tools/check-bundles.py)):

| File | Role |
|---|---|
| `<type>_companion.md` | The deep, cited explainer: origins, anatomy, methodology lineage, debates, anti-patterns, relationships, adaptations, references |
| `<type>_guide.md` | The operator card: when to use, when not to, a self-gradable rubric, named anti-patterns |
| `<type>_example.md` | One fully worked instance, no placeholders, no fabricated metrics |
| `<type>_meta.yaml` | The machine manifest: identity, taxonomy, size and format contract, relationships, provenance |
| `<type>_history.md` | Per-bundle changelog keyed to `template_version` |
| `<type>_research-log.md` | The evidence trail: every source consulted, its tier, and its retrieval status |

The research log ships as a committed file, not disposable scaffolding.
[ADR 0007 (the research log is a committed bundle artifact)](../internal/decisions/0007-research-log-as-bundle-artifact.md)
made this the case: it is what the freshness automation and the citation-integrity pass both read, and
without it "researched, not remembered" is an assertion nobody can audit.

On top of the six core files, a bundle ships one blank-template file per size variant it earns
(`<type>_template-lean.md`, `<type>_template-full.md`, or an `s`/`m`/`l` set), plus, only if it declares the
optional format axis, one further file per additional format per size
(`<type>_template-<format>-<size>.md`; see the format axis below). The PRD bundle
([`templates/prd/`](../../templates/prd/)) is the concrete example of the common case: eight files, the six
core files plus `prd_template-lean.md` and `prd_template-full.md`.

## The variant and nesting rule, and how it is enforced

**The meta declares the contract; it is not read off the disk.** `sizes_available` in `<type>_meta.yaml` is
the declaration of what the bundle *is*, and check A enforces the files on disk against it in both
directions: a size the meta declares but that has no file fails, and a variant file the meta never declared
also fails.
[ADR 0010 (the meta declares the size contract)](../internal/decisions/0010-meta-declares-size-contract.md)
made this explicit after the first single-size bundle exposed the gap; before it, a stray
`template-full.md` could linger in a lean-only bundle and nothing would catch it.

Two legal size vocabularies exist, and a bundle uses exactly one, never mixed: `lean`/`full` (the default,
earned by most types) and `s`/`m`/`l` (for a type that genuinely earns three weights). This traces to
[ADR 0002 (the variant model)](../internal/decisions/0002-variant-model.md), which also set the nesting rule:
**a smaller variant's section IDs are a strict ordered subset of the larger's**, so a document can grow from
lean to full in place without re-authoring.

Check C (`check_nesting` in `tools/check-bundles.py`) enforces this mechanically. It reads each variant's
headings as `(level, text)` tuples, H2 and deeper, not text alone, because demoting a heading one level is a
real structural change a text-only comparison would miss. It then proves the smaller variant's tuple sequence
is an ordered subset of the larger's. A single-size bundle is reported `single variant, nesting rule not
applicable`, never silently passed: the gate says out loud when a rule does not apply rather than staying
quiet about it.

**The format axis is a second, orthogonal axis, added later.**
[ADR 0028 (adopt a format axis)](../internal/decisions/0028-adopt-a-format-axis.md) lets a bundle ship the
same document type in more than one structurally distinct shape (a canvas and a narrative for
`product-vision`, for example), declared with optional `default_format` / `default_format_guidance` /
`additional_formats` keys. Nesting still applies, but only *within* a format; nothing is asserted *across*
formats, because two formats are siblings, not parent and child. A format earns a file only when it is
structurally distinct from the default **and** in circulation with a named source; a stylistic preference is
a companion paragraph, not a file. As of this ADR only `product-vision` uses the axis; the other bundles are
deliberately not backfilled pending evidence from later strategy-docs members.

## The two metadata axes, and why a bundle declares one and not both

Every `<type>_meta.yaml` declares exactly one of two taxonomy fields, never both and never neither:

- `phase`, one of `discover`, `define`, `develop`, `deliver`, `measure`, `iterate`, for a lifecycle artifact
  that belongs to one stage of a product's life.
- `classification`, one of `foundation`, `utility`, `tool`, for a standing, cross-phase artifact with no
  honest single phase.

[ADR 0015 (a bundle declares phase XOR classification)](../internal/decisions/0015-second-taxonomy-axis-phase-xor-classification.md)
set this after finding catalog types (Risk Register, RAID Log, Status Report, Definition of Done) that a
required `phase` field would have forced into a fiction: a Risk Register is maintained across every phase,
not opened in one and closed in another. The XOR is not a guess; it mirrors an already-proven partition in
the sibling `pm-skills` project, verified across all 68 tracked skills at zero skills with both fields and
zero with neither. `tools/meta.schema.json` encodes the rule as a `oneOf` with two branches, each requiring
its own field and explicitly forbidding the other:

```json
"oneOf": [
  { "required": ["phase"], "not": { "required": ["classification"] } },
  { "required": ["classification"], "not": { "required": ["phase"] } }
]
```

A bundle declares one axis because the two answer different questions: `phase` says where in the delivery
sequence a document sits, `classification` says that the document has no such sequence and stands beside all
of them instead. Forcing every type onto one axis would make the field lie for whichever half of the catalog
does not fit it.

## Every gate check, what it guarantees, and what it deliberately does not

`tools/check-bundles.py` is the gate: eleven lettered checks, A through K, run against every bundle under
`templates/`. It is the same script CI runs (`.github/workflows/ci.yml`, the "Bundle gate" step), not a
prototype of one. Nine checks are pure standard library and always run; two (G and J) need a real parser the
standard library does not provide and SKIP with a stated reason if it is absent locally, though CI always
installs both dependencies, so G and J are enforced there.

| Check | Guarantees | Deliberately does not |
|---|---|---|
| A Files | The six core files exist, plus exactly the size and format variants the meta declares, in both directions | Whether the content of any file is any good |
| B Dashes | No em-dash or en-dash character anywhere in a file the bundle owns | Anything outside the bundle; the repo-wide sweep is a separate CI step |
| C Nesting | The smaller variant's `(level, text)` heading sequence is an ordered subset of the next larger variant's, within each format | Nesting across formats (never asserted, by design); the quality of what is inside a nested section |
| D Example | No `{{placeholder}}` token survives in the worked example | Whether the example is realistic, independent of the template's own guidance, or free of fabricated figures (separate CI steps and review own this) |
| E Citations | Every inline `[[n]](#ref-n)` resolves to an anchor, and every anchor is cited by something, both directions; no bare `[n]` left unlinked | Whether the cited source actually supports the claim. A 2026-07-16 pass found 28 defects, including fabricated quotations, that had been green for weeks; this is stated in the script's own docstring |
| F Meta contract | `sizes_available` is non-empty, uses one legal vocabulary, carries no unfilled placeholder, and `default_size` names a declared size | The legality of any other meta field; that is check J's job |
| G Frontmatter YAML | The meta and every template/example frontmatter block parse as real YAML (an unquoted `{{placeholder}}` that breaks a flow mapping is caught) | Whether the parsed values are the *right* values; SKIPs locally without PyYAML, per [ADR 0014](../internal/decisions/0014-gate-may-use-pyyaml-for-frontmatter-validity.md) |
| H History | `<type>_history.md` carries an entry whose heading starts with the exact `template_version` the meta currently claims | The quality or completeness of the changelog entry itself |
| I Refs resolve | `pairs_with` names a skill on the pinned `tools/known-skills.txt` list (or is reported unchecked if that list is absent); `related_templates` names a bundle that exists, or uses `future:` for one that does not (a `future:` target that is built fails) | Whether the relationship claimed is substantively true, only that it resolves |
| J Meta schema | The meta validates against `tools/meta.schema.json`: required fields present, enums legal, exactly one of `phase`/`classification` | SKIPs locally without PyYAML and a JSON Schema validator, per [ADR 0017](../internal/decisions/0017-gate-may-use-jsonschema-for-meta-validation.md); enforced in CI |
| K Family | A bundle that declares a family conforms to that family's registry entry: the right axis and value, an allowed status, an allowed size shape, and that the contract file resolves | The non-registry obligations of the contract (guidance-comment grammar, companion skeleton, guide shape, shared-example rule); a family with no ratified contract yet passes with a note |

The gate's own docstring states its coverage plainly: these eleven checks automate roughly half the
methodology's Definition of Done. A green run means the structure holds, not that the content is true; that
judgment belongs to the four-lens review (see the build pipeline, phase 4, below).

CI runs the gate first and then a further sequence of steps that each prove something the per-bundle gate
cannot see by construction: fixture-driven self-tests for check K and the format axis (most of their failure
branches have no live subject in a clean tree), the repo-wide link gate, manifest and atlas freshness checks
(`gen-manifest.py --check`, `gen-atlas.py --check`), the ADR index check, changelog freshness, the
research-log contract and its self-test, the self-reported counts check, example independence and
chronology checks, rubric-scope check, workflow-prompt-string check, the research-log generator's self-test,
and a final repo-wide dash sweep. The exact order is in
[`.github/workflows/ci.yml`](../../.github/workflows/ci.yml); each step carries an inline comment naming the
real defect it was added to close.

## The family-contract mechanism and check K

A bundle may declare a `family` (for example `family: delivery-docs`). If the family has a ratified contract,
that contract narrows the general schema to family-specific values, and check K enforces the narrowing.
`docs/internal/contracts/delivery-docs.md` is the worked example: adopted by
[ADR 0020 (adopt the delivery-docs family contract)](../internal/decisions/0020-adopt-delivery-docs-family-contract.md),
its section 2 constrains every member to `phase: deliver`, a `beta` or `stable` status, and a `[lean, full]`
or `[lean]` size shape, while leaving `methodology` descriptive rather than gated (three of its four founding
members honestly declared different methodology values, so forcing one would have made the metadata less
true).

The mapping from `family:` to a contract's constraints lives in `FAMILY_CONTRACTS`, a registry inside
`tools/check-bundles.py`. Each entry names the contract file, the taxonomy axis the family is coherent on
(`phase` or `classification`, never both, per ADR 0015), the allowed value or set of values on that axis, the
allowed status values, and the allowed size shapes. Check K reads a bundle's meta, looks up its declared
family in the registry, and reports a failure naming exactly which constraint was violated. A family with no
registry entry yet (a contract not written) passes with a note rather than failing, so declaring a new family
does not retroactively break the gate before its contract exists.

**Check K enforces membership of a value, never correctness of the choice.** A `classification`-axis family
like `strategy-docs` can gate a *set* of allowed values (`foundation` or `utility`); the check proves a member
picked a value from that set, never that it picked the *right* one for its content. That judgment is a review
obligation against the contract's own section 2, not a gate obligation.

Every ratified family contract states its own enforcement boundary in a section 6, naming exactly which of
its numbered obligations the gate covers and which remain review or audit obligations. For delivery-docs:
the eight files (its section 3.1), nesting (3.2), citations (3.6), and the clean example (3.7) are covered by
gate checks A, C, E, and D respectively; guidance-comment grammar (3.3), the companion skeleton (3.4), and
guide shape (3.5) have no mechanical check and are authoring-time review obligations; the shared-example rule
(section 4) and the shareable-boundary rule (section 5) are review and audit obligations. A member failing
the contract is not "in the family with issues"; it is out of the family until green.

## The research-log contract and its three retrieval tokens

`tools/check-research-logs.py` runs in CI and gates every source entry in every checked research log,
independently of the citations that reference it. Governed by
[ADR 0029 (gate the research log's contract, not its layout)](../internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md),
it exists because the honest-retrieval standard was originally written only into the research fan-out's JSON
schema, which constrains what an agent *returns*, and nothing downstream re-checked the markdown log a human
then wrote from those returns.

Per source, the check requires: a contiguous unique number in document order, a title, an author or
organization, a URL (or an explicit stated reason there is none, read from that reason's own line so a
`Supports:` clause elsewhere cannot supply the words), a tier from a fixed vocabulary (`primary`,
`standards`, `academic`, `practitioner`, `vendor`, `reference`, `internal`, each optionally qualified in
parentheses), a retrieval status that is exactly one of three enum tokens, and a `Supports:` clause, written
even when the honest answer is that the source supports nothing in this bundle. `Quotable:` and
`Contested/time-bound:` are optional, not required; an earlier internal audit that treated them as mandatory
reported 76 defects where there were 2, which is why `docs/internal/bundle-pipeline.md` states the correction
explicitly.

**The three retrieval tokens, and which one permits a quotation:**

- **`fetched-and-verified`.** The source's body was actually read and the claim compared against it. This is
  the only status that permits a verbatim quotation.
- **`url-confirmed-not-read`.** The link resolves to real content, but the body was not checked against any
  claim. No claim may rest on a source at this status alone.
- **`not-retrieved`.** Paywalled, blocked, unreachable, or a print source. Never quotable.

Three layouts are legal, and the check accepts any of them: numbered prose (the house form for a new bundle),
a numbered-period form, and a table form. The table form is restricted by name to six exempted legacy logs,
measured at zero URLs and zero retrieval tokens across 86 sources; any other shape that carries no
per-source record fails rather than passing quietly.

**What the check does not verify, stated in its own docstring:** whether a retrieval status is truthful,
whether a `Supports:` clause is accurate, or whether a URL actually belongs to the source it sits beside.
Those are the four-lens review's job (phase 4 of the build pipeline, below), specifically the
citation-support lens.

## The generated-versus-authored boundary across the tooling

Four mechanisms in this repository generate a fact from the tree rather than accept it as typed prose, and
each one states the same rationale in its own docstring: **every count this repository generates stays
fresh; every count it retypes goes stale.**

- **`manifest.json`**, generated by [`tools/gen-manifest.py`](../../tools/gen-manifest.py) from every
  bundle's `meta.yaml`, per
  [ADR 0018 (the machine catalog is a generated manifest.json)](../internal/decisions/0018-machine-catalog-generated-manifest.md).
  `--check` mode regenerates in memory and fails on any diff against the committed file, and separately
  checks the README's `<!-- bundle-count: N -->` marker against the real count.
- **The atlas `built` flags**, generated by [`tools/gen-atlas.py`](../../tools/gen-atlas.py) from which
  catalog types (by `catalog_ref`) have a bundle on disk, writing the same value into both
  `atlas/catalog-data.json` and the duplicate JSON island inside `atlas/atlas.html`. Before this generator
  existed, the two hand-maintained copies drifted for weeks, advertising four built bundles while twelve
  existed; `--check` mode now fails on drift between either file and the bundles on disk.
- **Research-log source-entry blocks**, generated by [`tools/gen-research-log.py`](../../tools/gen-research-log.py)
  from the build pipeline's research fan-out JSON output. It deduplicates sources by a normalized URL (fixing
  a bug where a `www` and non-`www` URL pair for the same source filed under two numbers) and unions, never
  overwrites, the `Supports:` and `Quotable:` fields when two research dimensions or two reruns both own the
  same source (fixing a bug where a naive merge silently dropped verified quotables). The log's framing
  prose, its contested-claims section, and its "Notes for the companion" block stay hand-written, because
  those are judgment, not transcription.

None of the three generators claims to verify truth. `gen-research-log.py`'s docstring states it directly:
"It proves nothing about truth... Those are the four-lens review's job." `gen-manifest.py` and
`check-counts.py` carry the equivalent disclaimer.

## The counts-marker mechanism

`tools/check-counts.py` takes a different approach from the three generators above: instead of generating
prose, it gates a machine-checkable marker embedded in any tracked markdown file, of the form:

The marker is an **HTML comment whose body opens with the word `counts:`**, followed by comma-separated
`key=value` pairs. The keys are a fixed vocabulary the checker computes live: `bundles`, `tier1`,
`tier1remaining`, `adrs`, `adrmax`, `cisteps`, `checkk`, `checkformats`, `checklogs`, `logsgated` and
`sourcesgated`.

**No literal specimen appears on this page, and that is deliberate.** `check-counts.py` scans raw file
text and strips neither fenced blocks nor placeholder values, so any syntactically valid marker written
here as an illustration is read as a live claim about the tree. Writing this page produced that failure
twice: once with real-looking values copied from the tool's own docstring, and again with a `KEY=VALUE`
placeholder, which failed as an unknown fact name rather than passing as an obvious dummy.

That is a real gap and it is worth stating plainly, because the same class of bug was already fixed once
for **inline** code spans after a specimen quoted inside `STATE.md` was read as a live claim. Fenced blocks
were never covered. The sibling `folder-readme` check in the Standard toolkit calls a `stripFences` helper
before parsing for exactly this reason, so the two checks currently disagree about whether a documented
example is data.

The check recomputes each named fact live from the tree (a bundle count via the same rule
`check-bundles.py` uses, a directory carrying `<name>_meta.yaml`; research-log gate counts via
`check-research-logs.py`'s own output; the ADR count by scanning `docs/internal/decisions/`; the CI step
count from `ci.yml`; and several self-test assertion counts) and fails if any marker's claimed value
disagrees. It explicitly does not read the prose around the marker: a green run means no underlying number
has changed since an author last confirmed the sentences near it, not that those sentences are correct.
Every marker in a file is checked, via `finditer` rather than `search`, after a real defect where only the
first marker in a file was validated while stale prose sat unguarded elsewhere in the same document. A
marker wrapped in backticks is treated as an illustration rather than a live claim and is skipped.

## The build pipeline, phase by phase

The runbook for building one bundle is [`docs/internal/bundle-pipeline.md`](../internal/bundle-pipeline.md),
executable via [`.claude/commands/build-bundle.md`](../../.claude/commands/build-bundle.md), which
drives [`.claude/workflows/build-bundle.js`](../../.claude/workflows/build-bundle.js) for its two parallel
fan-out stages. The prose in the runbook remains the authority; the script is one way of executing it.

**Phase 0, spec.** Read the bundle's entry in `docs/internal/buildout-specs.md` (family, axis value, sizes,
methodology, catalog reference, key sources) and confirm the family's contract already exists; a new family
needs its contract adopted first. Read one sibling bundle end to end to mirror its file formats.

**Phase 1, research fan-out.** A Workflow of four to six parallel `sonnet`-model agents, one per research
dimension (origins and canon, structure, methodology lineage, debates and status, relationships and
tooling), each performing real `WebSearch`/`WebFetch` under a strict honest-retrieval discipline: record
`retrieval_status` truthfully per source, quote only what was verbatim-read, never fabricate a quote, date,
author, or URL, and check a page's body rather than trusting a 200 status code alone, since a stale URL can
resolve while its content has moved.

**Phase 2, synthesize the research log.** Consolidate the fan-out output into `<type>_research-log.md`
(`tools/gen-research-log.py` does the mechanical merge; a human or agent writes the framing prose, the
contested-claims section, and notes for the companion).

**Phase 3, draft, in a fixed order.** Companion (the 11-section skeleton, citing inline as written), then
`template-lean` and `template-full` (lean first, full as a strict superset), then guide, then example, then
`meta.yaml`, then `history.md`. Each step draws on the research log finalized in phase 2.

**Phase 3.5, machine pre-read.** Two non-gating, report-only lints, `tools/lint-number-provenance.py` and
`tools/lint-unsourced-confidence.py`, run in seconds and surface candidate defects (numbers and proper nouns
not traceable to the log, frequency or superlative claims nothing measured) for phase 4 to judge. Neither
produces a defect list on its own; a flagged line is a candidate, not a finding.

**Phase 4, adversarial four-lens review.** A Workflow of four parallel `sonnet`-model lenses, each reading
only the files it needs against a shared brief (`docs/internal/review-standards.md` plus the bundle's family
contract): citation-support (every claim against the log's `Supports:` clause, every quote against a
`Quotable:` entry), dod-family-conformance (guidance-comment grammar, the companion skeleton, guide shape,
the family's non-gated obligations), accuracy-teaching-point (historical and conceptual claims against the
log, consistency across companion/guide/example), and chaining-consistency (the example's internal
soundness and consistency with sibling examples).

**Phase 5, apply findings and re-verify.** Every review finding is itself a claim and is checked against its
source before being applied; the review occasionally proposes a fix that would break a gate check (for
example, renumbering the `## References` heading, which would break check E's body/references split).

**Phase 6, gate and land.** `git add templates/<type>` before running the link gate, since it only scans
git-tracked files; then `python tools/check-bundles.py <type>`, `python tools/gen-manifest.py` followed by
`--check`, and `python tools/check-links.py`. Then update the README bundle-count marker and family table,
`STATE.md`, and `buildout-specs.md`'s progress table, open a PR against `origin/main`, let CI pass without an
admin merge, and land.

Phases 1 and 4 are Workflow fan-outs on the `sonnet` model, per the project's model-routing rule: a
research-with-judgment or rubric-based task is sonnet's lane, and a four-to-six-way fan-out drops one tier
from what a single adversarial-verify agent would get. Phases 0, 2, 3, 5, and 6 stay in the main loop, which
synthesizes and re-verifies every subagent finding rather than trusting it outright, an asymmetric-verification
pattern: frontier checks sonnet, never sonnet-checks-sonnet.
