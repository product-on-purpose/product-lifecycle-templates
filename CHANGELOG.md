# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) 1.1.0, and this
project adheres to [Semantic Versioning](https://semver.org/).

The customer-facing announcement for each release lives in [`docs/releases/`](docs/releases/) and is
written using this library's own `release-notes` template. This file is the record; that is the
announcement. The distinction is the one the `release-notes` bundle teaches: a changelog is for
people who want every change, release notes are for people who want to know what it means for them.

## [Unreleased]

Backfilled 2026-07-26 covering 28 commits since 0.1.0. This section was empty while nine bundles, five
family contracts and fourteen decision records landed, which is recorded as finding DF-3 (gated documents stay fresh, ungated ones drift) in
[`STATE.md`](STATE.md) rather than quietly corrected: the documents this repository gates for freshness
stayed fresh, and the ones it does not gate drifted.

### Added

- **`okrs` (2026-07-30), the nineteenth bundle and the fourth `strategy-docs` member, completing that
  family** and with it one continuous worked thread from a product vision down to a bug report. One format
  ships: six candidates examined individually and five rejected, then nine further named goal-setting
  frameworks checked for a counterexample. Its honest core is a tested negative, that no study measures
  whether the OKR artifact improves outcomes, and that neither the goal-setting literature nor its published
  critics mention OKRs at all.
- **`tools/check-example-independence.py`, wired into CI**, gating a defect that had recurred four times and
  survived the convention adopted to prevent it. It failed 16 of 19 bundles on first run with **zero false
  positives on triage**, which is recorded as finding **DF-6 (worked examples reuse their own template's
  guidance text)** in [`STATE.md`](STATE.md). The 16 are grandfathered at measured ceilings that may only
  shrink, with 132 copied passages outstanding.
- **Catalog entry 6 corrected**: it had listed V2MOM as "Salesforce's named variant" of OKRs since the
  catalog was written, and Salesforce's own training material defines all five V2MOM components without
  mentioning OKRs once. Corrected with a dated note in the EC-2 pattern, across `catalog.md`,
  `catalog-data.json` and `buildout-specs.md`.

- **Nine bundles, taking the library from 6 to 15**, and completing three families:
  - `delivery-docs` completed: `product-backlog`, `sprint-backlog`.
  - `decision-docs` completed: `sdd`.
  - `governance-docs`, a new family and the first on the **classification** axis: `risk-register`,
    `raid-log`, `kpi-dashboard`.
  - `qa-docs`, a new family at phase `develop`: `test-plan`, `test-case`, `bug-report`. Their examples form
    the library's first **cross-family** chain, running from a risk to a test plan row to a test case to a
    defect to the regression that guards it.
- **Five family contracts**, each ratified before its members were built and enforced by gate check K:
  [delivery-docs](docs/internal/decisions/0020-adopt-delivery-docs-family-contract.md) (ADR 0020),
  [decision-docs](docs/internal/decisions/0022-adopt-decision-docs-family-contract.md) (ADR 0022),
  [governance-docs](docs/internal/decisions/0024-adopt-governance-docs-family-contract.md) (ADR 0024),
  [qa-docs](docs/internal/decisions/0026-adopt-qa-docs-family-contract.md) (ADR 0026),
  [strategy-docs](docs/internal/decisions/0027-adopt-strategy-docs-family-contract.md) (ADR 0027, the first
  to gate a **set** of axis values).
- **A second taxonomy axis**: a bundle declares `phase` XOR `classification`, never both, never neither
  ([ADR 0015](docs/internal/decisions/0015-second-taxonomy-axis-phase-xor-classification.md)). The Tier-1
  family map was resolved against it in
  [ADR 0023](docs/internal/decisions/0023-resolve-the-tier-1-family-taxonomy.md).
- **A format axis, orthogonal to size** ([ADR 0028](docs/internal/decisions/0028-adopt-a-format-axis.md)):
  optional `default_format` and `additional_formats` keys let one bundle ship a document in several shapes.
  Strict nesting now applies **within** a format and is never asserted across formats, because a canvas and a
  press release are siblings rather than parent and child. The default format keeps the plain filenames, so
  adopting it in an existing bundle is a metadata addition with no renames.
- **A machine-checkable metadata schema**, `tools/meta.schema.json`, validated in CI as gate check J
  ([ADR 0016](docs/internal/decisions/0016-adopt-machine-checkable-metadata-schema.md),
  [ADR 0017](docs/internal/decisions/0017-gate-may-use-jsonschema-for-meta-validation.md)).
- **A generated machine catalog**, `manifest.json`, committed to version control and kept fresh by the gate
  ([ADR 0018](docs/internal/decisions/0018-machine-catalog-generated-manifest.md)), plus a generated atlas.
- **Selection metadata** for agents budgeting context: authored `default_size` and `sizing_guidance`, and a
  generated heuristic `approx_tokens` with no tokenizer dependency
  ([ADR 0019](docs/internal/decisions/0019-selection-metadata-and-approx-tokens.md)).
- **Executable tests for gate logic that has no live subject**
  ([ADR 0025](docs/internal/decisions/0025-executable-tests-for-gate-logic.md)): `tools/test-check-k.py`
  (65 assertions) and `tools/test-check-formats.py` (64 assertions). Both run in CI and block merge. Both
  counts scale with the live tree, so they are read from the tools rather than quoted from memory.
- **Freshness gates** for the generated artifacts: `gen-manifest.py --check`, `gen-atlas.py --check`, and
  `check-adr-index.py`, each added after the corresponding drift was found in the tree rather than in theory.
- **A scope commitment**: complete the catalog's 27-type Tier-1 floor on a schedule, with grow-by-pull
  reserved for Tier 2 and Tier 3
  ([ADR 0021](docs/internal/decisions/0021-complete-the-tier-1-floor.md)). 17 of the 27 are built.
- **`product-roadmap`**, the eighteenth bundle and the third `strategy-docs` member. Ships three formats
  from eight researched: `now-next-later` (default), the GO goal-and-metric grid, and the themes format that
  carries vision and objectives inside the document. **The five rejections matter more than the three
  admissions**: the timeline form has no named product-management defender, the release plan is a different
  artifact, the release roadmap and Kanban board are a relabel and a source-less glossary entry, and the
  opportunity solution tree and Cagan's OKR alternative were excluded because their own authors do not
  present them as roadmaps. **This closes the evidence question the `default_format` backfill was waiting
  on** (D-E): ADR 0028's rule has now discriminated twice, 2 of 5 and 3 of 8. Its honest core is a confirmed
  evidence gap, and two circulating statistics were found and deliberately excluded as untraceable.
- **`product-strategy`**, the seventeenth bundle and the second `strategy-docs` member. Ships the Rumelt
  kernel (diagnosis, guiding policy, coherent action) as its default format at lean and full, plus a
  Playing-to-Win one-pager. Its honest core is a **tested negative**: no study measures whether writing a
  product strategy document improves product outcomes, and the bundle shows the search that establishes it
  rather than assuming either direction. Three further formats were researched and rejected under ADR 0028's
  rule, which is the first evidence that the rule discriminates rather than admitting everything.
  **It is also half the evidence the `default_format` backfill was waiting on**: format variation is not
  peculiar to `product-vision`.
- **`product-vision`**, the sixteenth bundle, the first `strategy-docs` member, and the first bundle to ship
  more than one format: canvas lean and full (the default), plus a narrative and a PR/FAQ at full only. Ten
  files rather than eight. A fourth shape, the positioning sentence, was researched and excluded on
  attribution grounds. Its example opens the Acme Analytics chain that runs down through the PRD to a
  regression test.
- **The research-log contract, now gated** by `tools/check-research-logs.py` (ADR 0029, built 2026-07-28).
  Every source in a checked log must carry a contiguous unique number, an identity, a URL or an explicit
  statement of why there is none, a tier, a retrieval status from the three-token enum, and a `Supports:`
  clause. All three numbered layouts are legal, because the contract is the rule and presentation is not.
  Covered by `tools/test-check-research-logs.py` (80 assertions, mutation-checked against seven deliberate
  breakages). **12 of 18 logs and 472 of 558 sources are gated**; the six table-layout logs are exempt by
  name with a measured reason printed on every run, and tracked as finding DF-4.
  **Building it disproved the finding it was built for:** the three logs ADR 0029 called status-less carry
  the contract in full, in a third numbered layout the original audit's regexes did not match. The ADR
  carries a dated correction rather than a silent edit.
  The honest-retrieval standard is this library's central quality claim, and until this landed nothing
  verified it: the requirement bound the research workflow's JSON schema, never the markdown that schema
  produces ([ADR 0029](docs/internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md),
  finding DF-2). `Quotable:` and `Contested/time-bound:` remain optional, because the written standard says
  so.
- **Build-out documentation**: `docs/internal/buildout-specs.md` (the per-type spec sheet and progress
  tracker) and `docs/internal/bundle-pipeline.md` (the six-phase runbook, including the honest-retrieval
  standard and the adversarial four-lens review).

### Changed

- The gate grew from nine checks to **eleven** (adding check J, meta-schema validation, and check K, family
  contract conformance).
- Check A now rejects **any** undeclared `_template-*.md` file, and `bundle_files()` scans by pattern rather
  than by size vocabulary. Previously both iterated known size tokens, so a file such as
  `x_template-narrative-full.md` failed no check **and was read by no scan**, meaning it could ship without
  ever being checked for dashes, citations, or links (ADR 0028).
- The catalog's `phase` field was renamed to `stage`, to stop it colliding with the bundle metadata's own
  `phase` (TX-2).
- The README was restyled without changing its claims.

### Fixed

- `release-notes` gained a first-release mode, so the template no longer assumes a previous version exists
  (DF-1, template 0.1.1).
- The catalog's prose said "core 28-type must-have tier" against its own machine data's 27, in two places.
  Corrected with a dated note; the Tier-1 floor count and two stale gate counts were reconciled at the same
  time.
- `bug-report` research log entry [17] declared its retrieval status as `not retrieved` rather than the
  schema's enum token `not-retrieved`.
- `risk-register` research log entry [33] carried no URL. It is a print book, and the absence is now
  documented as deliberate rather than left looking like an omission.

## [0.1.0] - 2026-07-17

First tagged release. Status `beta`: gate-green and cited to raw sources, with zero fills by anyone
but the author.

### Added

- Six governed bundles across two families, eight files each, `template_version` 0.1.0:
  - `delivery-docs`: `prd`, `user-stories`, `acceptance-criteria`, `release-notes`. Their worked
    examples chain across one feature, so the family reads as one traceable set.
  - `decision-docs`: `rfc` (propose a decision) and `adr` (record it, in MADR v4).
- `tools/check-bundles.py`, the governance gate: nine structural checks per bundle. Eight are pure
  standard library; check G (frontmatter YAML) uses PyYAML and skips honestly when it is absent
  (ADR 0014).
- `tools/check-links.py`, the link gate: every relative link and in-page anchor across every tracked
  Markdown file must resolve, and no tracked file may link into `_local/` (ADR 0013).
- `tools/known-skills.txt`, the pinned skill-ID list that `pairs_with` is validated against.
- CI on every push and pull request, with `main` branch-protected on the gate.
- `templates/methodology.md` (v0.2.3): the authoring process, the citation standard, and the
  per-bundle Definition of Done.
- `atlas/atlas.html`: a self-contained interactive map of all 205 catalog types.
- A six-step consumer quickstart in the README.
- Fourteen decision records at `docs/internal/decisions/` in MADR v4.
- Apache-2.0 license.

### Changed

- Citation standard hardened after a full integrity pass (methodology 0.2.3, section 6): one entry per
  source, honest retrieval status, blocked and paywalled sources labeled in the reference itself, and
  print books labeled as such rather than hidden inside a combined entry carrying a sibling's URL.
- Gate widened from seven checks to nine: citations are now verified in both directions, heading
  nesting compares depth as well as text, the meta is scanned for unfilled placeholders, the history
  must document the version the meta claims, and `pairs_with` / `related_templates` must resolve.
- README claims reconciled against what is true (see Fixed).

### Fixed

- 28 citation defects across the four `delivery-docs` bundles, every one of which had been passing the
  gate green. Included two wrong dates (Gherkin as 2007 rather than 2008; a 2006 Cagan essay dated
  2007), two quotations from sources that could not be read (one paywalled, one unreachable), claims
  attributed to authors who do not make them, and uncited padding.
- README overclaims: deterministic agent selection (no such path exists), a family described as
  "complete" and "verified", a stale four-bundle list, and a `docs/decisions/` path that does not
  exist and is forbidden by the org's scaffolder.
- `tools/check-links.py` did not skip fenced code blocks, so a documented Markdown-link example was
  read as a real link.

### Known gaps

Named here because the release is `beta` and the gaps are the reason:

- **No machine-consumption path.** No metadata schema, so an agent cannot select a bundle
  deterministically.
- **Not installable or listable.** `npx skills add` clones this repo and installs nothing, and
  agentskills.io has no template resource type: both take exactly one unit, the skill, and this repo
  ships no `SKILL.md` (decisions D2 and D3, resolved 2026-07-17).
- **No efficacy evals.** Template quality is argued, not measured.
- **No real usage cycle.** Every filled artifact in the repo is an authored example.
- **The gate cannot check citation truth.** It proves a citation resolves, never that the source
  supports the claim. The 28 defects above were all invisible to it.

[Unreleased]: https://github.com/product-on-purpose/product-lifecycle-templates/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/product-on-purpose/product-lifecycle-templates/releases/tag/v0.1.0
