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

- **`definition-of-done` and `runbook` bundles, completing `standing-standards`** (2026-08-06). The
  twenty-second and twenty-third bundles, landed together because they share a contract and because the
  family's set-valued gating only means something with both members present. **The first family whose two
  members take different values on the same axis**: `classification: foundation` for the standard you are
  judged against, `classification: tool` for the instrument you execute. That set has carried only a check-K
  fixture since ADR 0023; this is its first live subject.
  **Both members ship a named Review Trigger section** with an owner and a condition rather than a calendar,
  and the research established that obligation twice over independently: neither the Scrum literature nor
  the SRE literature supplies a condition-based trigger, and both reach for cadences.
  **`definition-of-done`** was researched against the 2020 Scrum Guide directly, because the family contract
  names "folklore presented as standard" as this type's citation hazard. Three things everyone says about a
  Definition of Done are **not in the Guide**: that it is a checklist, that it is the team's contract, and
  that it gets stricter over time. What the Guide does say is that the **Developers** conform, and that an
  organisational standard is a **floor** teams may raise and never lower. It ships `[lean, full]` against a
  spec that called for one size, because published DoDs vary about sevenfold and the variance tracks scope.
  **`runbook`** ships the incident-scoped shape rather than the 65-header service-operations manual, on the
  family contract's own definition. Its sharpest finding is that **Google's SRE canon does not use the word
  runbook**: across seven chapters searched by full text it appears three times, every one inside a
  contributed third-party case study, and four of the chapters most likely to discuss it contain zero
  occurrences of either word. The four circulating MTTR statistics for runbooks are quarantined, none
  traceable to a method, including the percentage figures widely attributed to Google, which do not exist in
  its text.
- **A correction to the merged `acceptance-criteria` bundle.** It stated that "the development team owns the
  DoD, with the Product Owner having final say", citing a Scrum.org page its own reference entry records as
  HTTP 403 and never read. The 2020 Guide does not support it, and "development team" is vocabulary that
  edition retired.

### Changed

- **`prototype-brief` does not ship, and `discovery-docs` closes at two members**
  ([ADR 0035](docs/internal/decisions/0035-prototype-brief-fails-the-admission-test.md), **accepted
  2026-08-05**). The type was ratified as a **provisional** member by ADR 0031, conditional on its own
  research passing ADR 0030's admission test that a named source must publish it as a written document. **It
  failed.** Six research dimensions and 29 sources found prototyping practice everywhere and a commissioning
  document nowhere: GOV.UK's guidance is built around a code toolkit, which is structurally why `wireframe`
  was rejected; Google Ventures' Sprint Brief is real and named but scopes an entire five-day sprint, with
  the prototype's own plan produced mid-sprint as a storyboard; Strategyzer's Test Card is a card for
  business-model assumptions; and every assumption-test ancestor, Lean UX included, stops at a canvas or a
  worksheet. All six dimensions converged although only the first was asked the admission question.
  Shipping it anyway would have meant presenting an adjacent artifact under this type's name, the defect
  that got V2MOM rejected. The backlog drops to five, the Tier-1 floor is unchanged because this type was
  never one of the 27, and catalog entry 54's note is corrected from asserting the brief ships. The evidence
  is preserved in [`prototype-brief-admission-evidence.md`](docs/internal/prototype-brief-admission-evidence.md)
  and the record states four falsifiable conditions that would reopen it.

### Added

- **`user-persona` bundle, the twenty-first and the second `discovery-docs` member** (2026-08-05). Eight
  files, 45 researched sources of which 33 were read in full, `phase: discover`, sizes `[lean, full]`,
  `pairs_with: []`. **It defines the Recurring Analyst**, referenced across 19 files in this repository with
  no bundle having defined her, and its example is now the earliest document in the library. **The research
  changed the build spec in four places**: the anti-persona ships as a separate document rather than a
  section, "Behaviors" gets no standalone heading because none of the six published formats read carries
  one, a bounded "Quotes/Evidence" block appears in none of them, and `buyer persona` leaves the aliases
  because it is a different artifact scoped to the purchase decision. **The type's own canon could not be
  read**: *The Inmates Are Running the Asylum* chapter 9, *About Face* and *The Persona Lifecycle* were all
  unreachable, so the bundle states nothing about what they say, and Cooper is quoted from his own later
  essays instead, including that he gave the term away. The template carries a declared **evidence tier**,
  following Nielsen Norman Group's three-tier ladder, and the circulated 900 percent persona statistic is
  taught as an example of a number that traces to one uncontrolled case study isolating nothing.
- **`check-workflow-prompts.py`, gating a harness failure nothing else could see** (2026-08-05). A backtick
  written as markdown inside a workflow prompt closes the prompt's own template literal and makes the script
  unloadable. It shipped through a green PR and passed `node --check` with exit 0, because the stray
  backticks rebalanced into expressions Node tolerates. Nothing in CI parsed the workflow scripts before
  this. The check says in its own output that it cannot prove a script loads, because only invoking the
  Workflow tool proves that. Second failure of this shape after CRLF, and recorded as gotcha 7.
- **`business-case` bundle, the twentieth and the first `discovery-docs` member** (2026-08-05). Eight files,
  43 researched sources, `phase: discover`, sizes `[lean, full]`, `pairs_with: []` because no pm-skills skill
  serves this type. **One format ships**: the Five Case Model, with the SAFe Lean Business Case **deferred on a
  stated retrieval gap** rather than rejected, since only a practitioner mirror was read and not Scaled Agile's
  own page. Its central teaching point is that every standard readable in full treats the case as a **living
  document** while most use is a one-time gate, and its honest core is that **product-management literature is
  hostile or silent**: no product source found makes a positive case for the artifact. **PMBOK 7 could not be
  retrieved** despite being named a key source for this type, so the bundle states nothing about it, and the
  circulated benefits-realisation statistics (McKinsey, KPMG, PMI, Standish) are **quarantined, not cited**.
  Its worked example is the first to extend the Acme Analytics thread **backward**, dated eight days before the
  FY26 product strategy whose plans spend the investment it argues for.
- **The last three family contracts, adopted** ([ADR 0032](docs/internal/decisions/0032-adopt-standing-standards-family-contract.md),
  [ADR 0033](docs/internal/decisions/0033-adopt-process-docs-family-contract.md),
  [ADR 0034](docs/internal/decisions/0034-adopt-communication-docs-family-contract.md), **accepted 2026-08-05**):
  `standing-standards` (definition-of-done, runbook) on a **set** of `foundation` or `tool`, the first family to
  pair those two values; `process-docs` (sprint-retrospective-notes, incident-postmortem) on `phase: iterate`;
  and `communication-docs` (status-report) on `classification: utility`. **Every family in the library now has a
  ratified contract**, which is what unblocks the remaining eight bundles: a contract is a hard maintainer stop,
  so an unattended run would previously have stalled at the fourth bundle. Each carries a family-specific
  obligation that is genuinely distinct rather than boilerplate - a **review trigger** with a named owner and a
  condition for standing-standards, **teaching by contrast** for process-docs, and the **no-new-facts rule** for
  communication-docs, where every figure in an example must be read from an artifact already in the library and
  disagreeing with it is a contract failure rather than a rounding difference. `tools/test-check-k.py` gains the
  fixture ADR 0032 requires for the foundation+tool combination, before its first member lands; the suite goes
  from 69 to 80 assertions.
- **The `discovery-docs` family contract, adopted**
  ([ADR 0031](docs/internal/decisions/0031-adopt-discovery-docs-family-contract.md), **accepted 2026-08-04**):
  `business-case`, `user-persona` and `prototype-brief` on `phase: discover`, registered in check K and
  latent until the first member lands. Two firsts. It is the first family to extend the library's worked
  thread **backward** in time rather than adding new ground: its persona defines the **Recurring Analyst**
  that sixteen files across the library already reference and no bundle has ever described. And it is the
  first contract ratified with a **provisional member** - `prototype-brief` ships only if its own research
  finds a named source publishing it as a written document, and the contract pre-commits to a two-member
  family being a legitimate outcome rather than a failure. Ratifying with the condition stated is the point:
  deciding membership after the research is when a negative answer is easiest to rationalise away. The
  contract also carries a chronology obligation, since every member points forward and the `product-roadmap`
  February-citing-June defect is easiest to repeat here, and it waives example-independence grandfathering
  entirely.
- **A templating-scope rule** ([ADR 0030](docs/internal/decisions/0030-templating-scope-markdown-documents.md),
  **accepted 2026-07-31**): this library templates artifacts whose primary form is a written document, and names the ones
  it will not template rather than leaving them silently unbuilt. Applied to catalog 52 (`wireframe`) and 54
  (`interactive-prototype`), both out of scope because their artifacts are visual and executable. Adds
  **`prototype-brief`** as a new type in `discovery-docs`: the brief that commissions a prototype is a
  document even though the prototype is not. Generalises ADR 0028's format-admission test from formats to
  types. Two counts follow and are kept apart: the **catalog floor** is 18 of 25 templatable, and the **build backlog** is 8 bundles (the 7 remaining originals plus `prototype-brief`, which is not one of the 27).
  `design-docs` is therefore never created.
- **Four family contracts, drafted and pending maintainer review**:
  [`discovery-docs`](docs/internal/contracts/discovery-docs.md) (business-case, user-persona,
  prototype-brief; `phase: discover`), [`standing-standards`](docs/internal/contracts/standing-standards.md)
  (definition-of-done, runbook; **a set** on `classification`, `foundation` or `tool`, the second family to
  need one), [`process-docs`](docs/internal/contracts/process-docs.md) (sprint-retrospective-notes,
  incident-postmortem; `phase: iterate`), and
  [`communication-docs`](docs/internal/contracts/communication-docs.md) (status-report;
  `classification: utility`, one Tier-1 member, stated rather than hidden).
- **[`decision-procedures.md`](docs/internal/decision-procedures.md)**, ten recurring judgment calls with the
  precedent that earned each one. Not an ADR: an ADR records what was decided, this records how to decide.

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

- **Three documentation-drift defects found while landing `business-case`**, each shipped by an earlier PR
  that updated a count without re-reading the prose around it. The README's headline statistics table had a
  fragment of **PR #46's own commit message** spliced into it ("strategy-docs member and the first bundle to
  ship more than one format"), leaving a sentence that never closed its parenthesis; `okrs` landed in PR #53
  with **no row in its family table** while the table's heading already claimed four bundles, and the prose
  still read "Three are built; `okrs` completes it"; and both `STATE.md` and `buildout-specs.md` still said
  the remaining work included **family-contract ratifications** after PR #65 adopted the last three. This is
  the defect class `check-counts.py` names in its own output: it compares markers and cannot read the
  sentences that quote them.
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
