# STATE

> **The single source of current truth for this repository.** Update this file in the same commit as any milestone exit, release, or status change.
>
> Plans and briefs are dated projections. Where they disagree with this file, **this file wins**.
>
> This file exists because of audit finding G-01: the implementation plan's progress table said "Not started" for all seven phases while two of them were demonstrably complete, and it went stale within a week of being written. A plan that lies about the tree is worse than no plan. The fix is not "remember to update the plan"; it is to have one short file that is cheap to keep honest and that outranks everything else.

**Last updated:** 2026-07-20 (**M2 machine layer: WP-21 (schema), WP-22 (manifest), WP-23 (selection metadata), WP-24 (family contract) landed.** Every meta is schema-validated (check J) and every family member is contract-validated (check K); the gate is eleven checks. `manifest.json` is the machine catalog with selection metadata and a generated `approx_tokens`. The delivery-docs family contract is adopted and enforced; on first enforcement check K found its `methodology: generic` rule contradicted the members' honest values, so methodology was made descriptive ([ADR 0020](docs/internal/decisions/0020-adopt-delivery-docs-family-contract.md)). ADRs 0016 through 0020. WP-20 confirmed done via ADR 0009. M1 complete, v0.1.0 tagged 2026-07-17; TX-1, TX-2, D2, D3 closed)

---

## Built and true today

| What | State |
|---|---|
| **Bundles** | 6 of 27 Tier-1 catalog types. Family `delivery-docs`: `prd`, `user-stories`, `acceptance-criteria`, `release-notes`. Family `decision-docs`: `adr`, `rfc`. Eight files each. Status `beta`, `template_version` 0.1.0. |
| **License** | Apache-2.0, granted at the repo root. Copyright Jonathan Prisant. |
| **Governance gate** | `tools/check-bundles.py`, **eleven checks** (files, dashes, nesting incl. heading level, clean example, citations **in both directions**, meta contract + placeholder scan, frontmatter YAML validity, history-documents-version, pairs_with/related_templates resolution, **meta-schema validation**, and **family-contract conformance**). Nine are pure stdlib; G uses PyYAML ([ADR 0014](docs/internal/decisions/0014-gate-may-use-pyyaml-for-frontmatter-validity.md)) and J uses PyYAML plus jsonschema ([ADR 0017](docs/internal/decisions/0017-gate-may-use-jsonschema-for-meta-validation.md)), each SKIPping locally if its dependency is absent. **Runs in CI** on every push and PR; branch protection on `main` requires it to pass before merge. Passing on all six bundles. |
| **Machine catalog** | [`manifest.json`](manifest.json) at the repo root: every bundle's selectable fields (`id`, `title`, `summary`, `doc_type`, `phase` or `classification`, `family`, `sizes_available`, `default_size`, `sizing_guidance`, `status`, `tags`, `aliases`) plus a generated `approx_tokens` estimate per size variant, as one structured surface an agent selects a bundle *and a size* from. **Generated** by [`tools/gen-manifest.py`](tools/gen-manifest.py) from the metas and the template files, committed, and kept fresh by CI (`gen-manifest.py --check` fails on drift or a stale README count marker). WP-22 + WP-23, [ADR 0018](docs/internal/decisions/0018-machine-catalog-generated-manifest.md), [ADR 0019](docs/internal/decisions/0019-selection-metadata-and-approx-tokens.md). |
| **Decision records** | `docs/internal/decisions/`, twenty ADRs in [MADR v4](https://github.com/adr/madr) format, plus a README documenting the convention. All accepted. Matches the org standard used by `agent-config-toolkit` and scaffolded by `jp-init-project`. |
| **Layout** | The library lives at `templates/` (flat, by document type), the gate at `tools/`, the atlas at `atlas/`, and the planning, strategy, catalog, roadmap and decision records at `docs/internal/`. Decision HY-2 (scaffold graduation) closed 2026-07-12; the `_local/` split closed 2026-07-14 ([ADR 0013](docs/internal/decisions/0013-local-split-and-going-public.md)). |
| **Atlas** | 205-type interactive catalog map at `atlas/atlas.html`. |
| **Methodology** | v0.2.3 (`templates/methodology.md`), status draft. Governs authoring. Section 6 now codifies the source conventions (one entry one source; honest retrieval; blocked/paywalled; books). |
| **Master catalog** | [`docs/internal/catalog.md`](docs/internal/catalog.md). 205 types, 27 at Tier 1. Cited by the methodology and by every bundle companion. **Its size calls are hypotheses, not facts** (see EC-2 below). |
| **Audit corpus** | `_local/audit/2026-07-10_fable-audit/` on the maintainer's disk. **Deliberately NOT in git** (see [ADR 0013](docs/internal/decisions/0013-local-split-and-going-public.md)); its two load-bearing artifacts were promoted to [`docs/internal/roadmap.md`](docs/internal/roadmap.md) and [`docs/internal/contracts/delivery-docs.md`](docs/internal/contracts/delivery-docs.md). |

## Nothing broken right now

For the first time in this repo's life, that heading is true. Recently closed:

- **CI runs, and is green.** The gate had never once run (private repo, out of Actions minutes; every run died in 3s with zero steps). The repo went **public** on 2026-07-16, and the first real CI run passed. `main` is **branch-protected**: direct pushes blocked, the `gate` check required (strict), force-pushes and deletions blocked, linear history required.
- **M0 is merged.** PR #2 landed the credibility floor, the ADR bundle, and the `_local/` split. PR #1 was auto-closed by the history rewrite.
- **PB-1 (history exposure) is resolved.** `_local/` was purged from every commit (verified 0 paths in history, and `Not Found` on the remote) before going public, so publishing did not expose the audit corpus or session logs. The 29 files remain on the maintainer's disk, backed up at `E:/tmp/_local-backup-20260714`. ADR 0013 is now `accepted` and **confirmed** (its success condition, CI green on `main`, is met).

The reason this section exists at all: STATE.md is here because of audit finding G-01, *a plan that lies about the tree is worse than no plan*. Between 2026-07-13 and 2026-07-14 it had started doing exactly that (claiming CI passed when it had never run). That is fixed, and the section is kept, now empty of breakage, as the place the next breakage gets recorded first.

## Not built (deliberately visible)

- ~~No version tags. No CHANGELOG.~~ **Shipped 2026-07-17: [v0.1.0](CHANGELOG.md) is tagged**, with a [release note](docs/releases/v0.1.0.md) written by filling this library's own `release-notes` lean template. First dogfood artifact.
- **No distribution surface** beyond `git clone`. No plugin manifest and no marketplace entry (the [`manifest.json`](manifest.json) at the root is a machine-selection catalog, WP-22, not a distribution surface). **As of D2/D3 (resolved 2026-07-17) the reason is precise, not vague:** both the skills CLI and agentskills.io take exactly one unit, the skill, and this repo ships no `SKILL.md`, so `npx skills add` clones it and installs nothing. One missing file (roadmap LP-2), not an architecture problem.
- ~~No family contract adopted.~~ **Adopted 2026-07-20 (#24, [ADR 0020](docs/internal/decisions/0020-adopt-delivery-docs-family-contract.md)):** the [delivery-docs contract](docs/internal/contracts/delivery-docs.md) is enforced by gate check K (phase, status, size shape, and that the contract resolves). `decision-docs` still has no contract; its members pass check K with a note until it earns one.
- ~~No metadata schema, so no machine-consumption path.~~ **Shipped 2026-07-17 onward (#20, #22, #23):** every meta validates against [`tools/meta.schema.json`](tools/meta.schema.json) in CI (check J), and [`manifest.json`](manifest.json) is the machine catalog an agent selects a bundle and size from. Installability (a `SKILL.md`) is the remaining gap, above.
- **No efficacy evals.** Template quality is currently argued, not measured. This is the gap the audit weighted most heavily (finding D-04).
- **No real usage cycle. Zero fills by anyone but the author.** Every filled artifact in the repo is an authored example. The catalog's own tier rule gates Tier 2 on "survives one real usage cycle", so by its own standard nothing here has graduated.

## Open by choice, not by oversight

- **B-08, the `_working/` folder.** `templates/_working/` still holds the A/B/C guidance-style prototypes, even though its own README line 6 orders its deletion once the decision was made, and the decision *was* made (Approach A, see [`docs/internal/decisions/0006-guidance-style-approach-a.md`](docs/internal/decisions/0006-guidance-style-approach-a.md)). The maintainer chose on 2026-07-12 to keep it. Recorded here so it reads as a decision rather than a miss.

## Findings the library raised about itself, by using itself

**DF-1, the first dogfood finding, 2026-07-17. The lean `release-notes` template has no first-release
mode.** Found the only way this class of defect ever gets found: by filling the template for real, to
write [this repository's own v0.1.0 release note](docs/releases/v0.1.0.md).

"Improved" and "Fixed" are defined relative to a previous release, and a `0.1.0` has none. Worse, the
template's own fill rule ("if a section does not apply, write 'None in this release'") would produce a
first release note declaring that nothing was improved and nothing was fixed, which is false in
spirit: plenty was, it simply was never *released* before. The bundle already cites the source that
solves this (Keep a Changelog treats a first release as entirely "Added") and failed to carry the
guidance across.

**FIXED 2026-07-17 in `release-notes` 0.1.1**, once v0.1.0 was tagged and the fix could no longer
contradict the artifact that produced it. Both variants and the guide now carry an explicit
first-release rule: delete the comparative sections rather than filling them, stated as an override
(it contradicts the rule directly above it), with the reasoning given and the escape hatch named
(real users on an untagged `main` did experience change, so the sections may carry that if the
Summary says what "improved" is measured against). Recorded in
[`release-notes_history.md`](templates/release-notes/release-notes_history.md).

**This is the library's first template change driven by evidence from use rather than from review**,
which is the entire argument for the usage loop, demonstrated on a sample size of one.

The dogfood is worth more than the release. Six bundles have been argued to be good; this is the first
evidence of one meeting a real task, and it took exactly one use to find a real gap. That is the case
for the usage loop (roadmap M3) in one data point.

## Findings the library raised about its own ecosystem

Building a bundle turns out to be an audit of everything the bundle touches. The ADR bundle
(2026-07-14) surfaced two defects outside this repo; the RFC bundle (2026-07-16) surfaced a third.
All are **recorded, not silently patched**, because a template library that quietly edits its
neighbors is worse than one that reports.

| # | Finding | Where it lives | Status |
|---|---|---|---|
| **EC-1** | **`develop-adr` (pm-skills) ships a Nygard-format ADR template**, diverging from the MADR v4 convention the org standardized on for its own decision records (mandated by `jp-init-project` SKILL.md lines 8 and 98, adopted here by [ADR 0011](docs/internal/decisions/0011-madr-v4-at-docs-internal-decisions.md), and verified in use by `agent-config-toolkit`). An agent invoking that skill inside an org repo produces records in the wrong format. This bundle follows MADR and ships a Nygard-to-MADR mapping table in `adr_guide.md` so the two interoperate. **Reported to pm-skills 2026-07-16** as a durable audit ([PR #238](https://github.com/product-on-purpose/pm-skills/pull/238), `docs/internal/audit/2026-07-16_adr-format-divergence.md`): reported, not patched, because the skill's output format is a genuine decision (it is a public product; Nygard is the best-known ADR format; the MADR mandate governs the org's *own* records). **Two corrections, 2026-07-16.** (1) This row previously claimed MADR v4 was "in use by `agent-config-toolkit` and `thinking-framework-skills`". The second half was false: `thinking-framework-skills` has no tracked `docs/internal/decisions/` and no MADR reference at all. The mandate is real; adoption is partial. (2) The path given was `.claude/skills/...`, which is gitignored in pm-skills; the tracked source is `skills/develop-adr/references/TEMPLATE.md`. Re-checking also surfaced a second locus the original finding missed: pm-skills' `docs/internal/audit/README.md` plans "e.g., Nygard format ADRs" for a `docs/internal/decisions/` folder that does not exist yet. | `pm-skills`, `skills/develop-adr/references/TEMPLATE.md` | Reported 2026-07-16; decision open, for the pm-skills maintainer |
| **EC-2** | ~~Master catalog entry 64 (ADR) classifies the type as single-size ("S only").~~ **RESOLVED 2026-07-16.** MADR ships a minimal and a full template, so the type earns two weights. The catalog entry is corrected (now `S/L`, with a dated correction note), and a catalog-header note now states that all size calls are hypotheses. The bundle ships `lean` + `full`. | [`docs/internal/catalog.md`](docs/internal/catalog.md), entry 64 | **Resolved** |
| **EC-3** | **No `develop-rfc` skill exists in pm-skills.** The org ships `develop-adr` (a skill for the decision *record*) but nothing that generates an RFC (the *proposal* that precedes it), even though the RFC comes first in the sequence. An agent can be told to record a decision but not to propose one. The RFC bundle's `pairs_with` is therefore empty and the template is filled by hand. Not a defect in existing code, a gap in coverage. | `pm-skills` (absent skill) | Open, for the pm-skills maintainer |

Worth noting what EC-2 implies: **the catalog's size calls are hypotheses, not facts.** One of the
27 Tier-1 entries has now been checked against primary evidence and did not survive. The other 26
have not been checked. Expect more corrections as bundles get built, and treat the catalog's
`size_variant` column as a starting guess rather than a specification. The catalog now says this
about itself, in a header note.

## Gate coverage, stated honestly

The gate automates roughly **half** the methodology's Definition of Done (audit finding D-01). Seven checks run; the research-tracing, guidance-comment-structure, companion-skeleton, guide-structure, and history-content clauses have **zero** automation and are human-verified. Gate hardening is roadmap WP-11 in milestone M1, now partly done (see below).

One honest qualifier: the gate covers about half the DoD. Since M0 it **does** run in CI on every push and PR, and branch protection requires it to pass before merge, so for the half it covers, "enforceable, not aspirational" is finally true rather than aspirational.

**The YAML gap is closed (2026-07-16).** The ADR bundle had shipped with invalid YAML in both template frontmatters (`decision-makers: [{{decision_makers}}]` parses as a flow mapping with an unhashable key) and **the gate passed it green**, because it read `sizes_available` with a regex and never parsed YAML as YAML. Check **G (frontmatter YAML)** now closes that: the meta and every template/example frontmatter must parse, which forces placeholders to be quoted. This needed a YAML parser, which the stdlib lacks, so [ADR 0014](docs/internal/decisions/0014-gate-may-use-pyyaml-for-frontmatter-validity.md) grants the gate one dependency (PyYAML) for this one check; the other six stay pure stdlib and G SKIPs (honestly, not as a pass) if PyYAML is absent locally. CI installs it, so G is enforced. Verified by reintroducing the original bug and watching G fail.

**What remains of WP-11 is the hard half: citation-tracing.** Check E confirms a companion's inline citations *resolve* to anchors; nothing checks that the anchored source *supports the claim*. That is the failure mode that produced ~15 defects in the ADR bundle across three review rounds, it is still entirely human-verified, and it may not be fully mechanizable. Tracked as the open remainder of WP-11.

**WP-10 (citation integrity pass) is done, 2026-07-16, and it is the strongest evidence yet for the paragraph above.** All four delivery-docs bundles were verified against raw sources; every one had been passing the gate green the whole time. **28 defects across four bundles**, including three the gate is structurally incapable of seeing:

- **Two factual errors.** Gherkin is 2008 (Cucumber, Hellesoy), not 2007, and the word "Gherkin" appears nowhere in the Dan North article it was cited to. Cagan's "Revisiting the Product Spec" is 2006, not 2007, in a sentence whose whole point was how long he has held the position.
- **Two unverifiable quotations**, both now de-quoted: one from a paywalled post ("This post is for paid subscribers"), one from a domain that times out. Neither could ever have been checked.
- **Claims attributed to authors who do not make them.** Bill Wake does not say stories are "sized to fit inside one iteration" (he says "at most a few person-weeks"); Ranorex was cited five times and supports two.
- **Uncited padding the gate cannot catch**, exactly as predicted: check E fails an inline citation with no anchor but **never an anchor with no citation**. PRD refs 8 and 12 had zero citations each.

**The audit itself was wrong once.** WP-10 instructed "Keep a Changelog corrected to 1.1.2 with root URL". The spec site serves **1.1.0** as canonical and redirects `/en/1.1.1/` and `/en/1.1.2/` back to it; the repo tags the audit likely read are site releases, not spec versions. The existing citation was already correct. **Following the roadmap on faith would have introduced the defect class WP-10 exists to remove.** The roadmap row was withdrawn and corrected instead. A finding is a claim, and claims get checked.

**The durable fix shipped with it:** methodology 0.2.3 codifies four source conventions ([§6.1](templates/methodology.md#61-one-entry-one-source-no-combined-entries) one entry one source, [§6.2](templates/methodology.md#62-retrieval-status-must-be-honest) honest retrieval, [§6.3](templates/methodology.md#63-blocked-and-paywalled-sources) blocked/paywalled, [§6.4](templates/methodology.md#64-books-and-pre-web-sources-no-url) books), and the Definition of Done gained five checks so they are conditions of shipping rather than advice. **Combined entries were the single largest root cause**: they destroy traceability, launder sources with no URL behind a sibling's link, and attach claims to sources that do not make them.

## Next milestone

**M1 is complete (2026-07-17): [v0.1.0](CHANGELOG.md) is tagged.** All five work packages landed; the
table below is the record. Two open questions that gated M2 were also closed the same day: TX-1 (the
second taxonomy axis, [ADR 0015](docs/internal/decisions/0015-second-taxonomy-axis-phase-xor-classification.md))
and TX-2 (the catalog `phase` -> `stage` rename). Plus DF-1, the first dogfood finding, found by use and
fixed in `release-notes` 0.1.1.

**M2, the machine layer, is under way.** Its first items landed 2026-07-17, with WP-20's graduation confirmed already done:

| WP | What | State |
|---|---|---|
| **WP-20** | HY-2 decision + graduation | **Done (2026-07-12, [ADR 0009](docs/internal/decisions/0009-scaffold-graduation-flat-templates.md)).** The flat `templates/` scaffold graduated before M2, so WP-22's machine surfaces are built against final paths, satisfying the roadmap's ordering note. Confirmed 2026-07-17; the only unmet deliverable was a redirect note in the gitignored `_local/`, which is not a tracked artifact. |
| **WP-21** | Metadata schema (`tools/meta.schema.json`; gate check J validates every meta against it) | **Done 2026-07-17 (#20).** The schema encodes `phase` XOR `classification` (ADR 0015) and codifies the 18 fields the six metas carry; check J enforces it in CI, adversarially tested against a 37-case battery hardened by an independent red-team. [ADR 0016](docs/internal/decisions/0016-adopt-machine-checkable-metadata-schema.md) (the schema), [ADR 0017](docs/internal/decisions/0017-gate-may-use-jsonschema-for-meta-validation.md) (the jsonschema dependency). The worked RFC example [RFC-0001](templates/rfc/rfc_example.md) *was* this proposal and is now accepted, written from into ADR 0016. |
| **WP-22** | Machine catalog (`manifest.json`; `tools/gen-manifest.py`; freshness check) | **Done 2026-07-17 (#22).** `manifest.json` is generated from the metas and committed; `gen-manifest.py --check` fails CI on drift or a stale README count marker (audit C-03). Delivers RFC-0001's second artifact. [ADR 0018](docs/internal/decisions/0018-machine-catalog-generated-manifest.md). |
| **WP-23** | Selection metadata (`default_size`, `sizing_guidance`, `approx_tokens`) | **Done 2026-07-18 (#23).** Authored `default_size` (checked against `sizes_available` by check F) and `sizing_guidance` in every meta; a generated `approx_tokens` estimate per variant in the manifest (stdlib chars/4 heuristic, no tokenizer dependency). [ADR 0019](docs/internal/decisions/0019-selection-metadata-and-approx-tokens.md). |
| **WP-24** | Family contract (`delivery-docs`) + gate check | **Done 2026-07-20 (#24).** The `delivery-docs` contract ([docs/internal/contracts/delivery-docs.md](docs/internal/contracts/delivery-docs.md)) is adopted and enforced by check K (phase/status/size shape + contract resolves). Check K's first run found the contract's `methodology: generic` rule contradicted three members' honest values, so methodology was made descriptive, not gated ([ADR 0020](docs/internal/decisions/0020-adopt-delivery-docs-family-contract.md)). Methodology-specific *packs* (Scrum/XP/SAFe collections) reserved as a Tier-2 future. |
| **WP-25..28** | Fill tooling, freshness automation, docs tree, v0.2.0 | Next up: WP-25 (fill tooling: strip comments, stamp provenance) toward the v0.2.0 tag. |

Full definition: [`docs/internal/roadmap.md`](docs/internal/roadmap.md).

### M1 record

| WP | What | State |
|---|---|---|

| WP | What | State |
|---|---|---|
| **WP-10** | Citation integrity pass (A-01..A-06) | **Done.** All four delivery-docs bundles verified against raw sources; 28 defects fixed; methodology 0.2.3 codifies the source conventions so the class does not recur. One WP-10 instruction was itself wrong and was withdrawn rather than executed. |
| **WP-11** | Gate hardening v1 | **Done, except the half that may be impossible.** All six named items shipped 2026-07-17: reverse citation direction, meta placeholder scan, history-documents-version, `pairs_with` against a pinned skill list, `related_templates` resolution with the `future:` convention, and heading comparison on (level, text) tuples. Seven checks became nine, each adversarially tested to prove it fails when it should. **The first run of the new padding check failed the `rfc` bundle**, catching three uncited references the author had noticed and rationalised away the day before. Citation-tracing (does the source *support* the claim?) remains open and may not be mechanizable. |
| **WP-12** | Decision closure (D2, D3) | **Done 2026-07-17.** Both resolved by test and by reading the spec, and both answer the same question: **the ecosystem's unit is the skill, not the template.** The CLI installs nothing from this repo because it ships no `SKILL.md`; the spec has no template resource type at all. The pair took under an hour once attempted, having sat open 18 days against a three-day SLA. |
| **WP-13** | Consumer quickstart | **Done 2026-07-17.** Six literal steps, leading the README. Claim reconciliation found the front door claiming deterministic agent selection that does not exist, a family called "verified" days before 28 defects were found in it, a stale four-bundle list omitting all of `decision-docs`, and a `docs/decisions/` path that is both nonexistent and org-forbidden. |
| **WP-14** | Release v0.1.0 (dogfooded release note) | **Done 2026-07-17.** CHANGELOG in Keep a Changelog 1.1.0, [release note](docs/releases/v0.1.0.md) filled from the library's own lean template, tag pushed. **The dogfood worked as intended: it produced DF-1 on its first use** (see below). |

Full definition: [`docs/internal/roadmap.md`](docs/internal/roadmap.md).

## Open decisions, with ages

| ID | Decision | Open since | Cost to resolve | Scheduled |
|---|---|---|---|---|
| D1 | Build the Layer 1 generator, or not | 2026-06-29 | n/a | Correctly gated on a usage signal |
| ~~D2~~ | ~~Does `npx skills add` install this repo~~ **RESOLVED 2026-07-17: no.** Tested: the CLI clones the repo and installs **nothing**, reporting "No valid skills found. Skills require a SKILL.md with name and description." Verified against a control (`skills add product-on-purpose/pm-skills` succeeds), so the CLI and the org path both work; **this repo is the gap, because it ships no `SKILL.md`.** Unlock is known and cheap: ship one (roadmap LP-2). | 2026-06-29 | 30 min | **Resolved** |
| ~~D3~~ | ~~agentskills.io resource type for templates~~ **RESOLVED 2026-07-17: there is no template resource type.** The [Agent Skills specification](https://agentskills.io/specification) defines exactly **one** unit: a skill, i.e. a directory containing `SKILL.md` (`name` and `description` required; `name` must match the parent directory). **Templates are explicitly an optional bundled asset inside a skill**, not a resource of their own: `assets/` "Contains static resources: Templates (document templates, configuration templates)". A template library is therefore only listable by being wrapped in a skill. | 2026-06-29 | 1 hour | **Resolved** |
| D4 | Regulated-industry tier appetite | 2026-06-29 | n/a | Unscheduled |
| ~~TX-1~~ | ~~Does this library need a second taxonomy axis?~~ **RESOLVED 2026-07-17: yes, `phase` XOR `classification`** ([ADR 0015](docs/internal/decisions/0015-second-taxonomy-axis-phase-xor-classification.md)). Not a judgment call but a verified partition: parsing all **68** tracked `SKILL.md` in pm-skills gives **30** phase-only, **38** classification-only, **0** both, **0** neither. The Tier-1 set already contains phase-less types (Risk Register, RAID Log, Status Report, Definition of Done). WP-21 will require `phase XOR classification`. (The old row's "89 of 175 / 86" counts were inflated ~2.5x by counting gitignored `.claude/skills/` build copies; the canonical count is 68. ADR 0003 carries the correction.) | 2026-07-12 | ~1 hour | **Resolved** |
| ~~TX-2~~ | ~~The catalog's `phase` field is a different vocabulary from the bundles' `phase`, under the same name.~~ **RESOLVED 2026-07-17 (#18): the catalog field was renamed to `stage`, so `phase` is now unambiguous library-wide.** The catalog/atlas `phase` had ~30 values (`ideation`, `strategy`, `governance`, `communication`, ...); the bundle/pm-skills `phase` has six (`discover`...`iterate`), with near-collisions (`discovery`/`discover`, `definition`/`define`, `measurement`/`measure`). That is a document *stage*, not a lifecycle phase. Decided 2026-07-17 (alongside [ADR 0015](docs/internal/decisions/0015-second-taxonomy-axis-phase-xor-classification.md)): **rename the catalog's field to `stage`** so `phase` is unambiguous library-wide, before WP-21 writes a schema that has to name which `phase` it means. Mechanical but spanned `atlas/catalog-data.json`, `atlas/atlas.html` (an interactive app), and the catalog prose, so it shipped as its own verified change. | 2026-07-17 | ~1 hour | **Resolved** |
| VL-1 | Business model | 2026-07-02 | n/a | Unscheduled |
| VL-3 | Maintenance cadence | 2026-07-02 | n/a | M6 |

**Decision SLA** (audit finding E-05): any open decision whose stated resolution cost is under two hours is resolved within three working days, or explicitly re-dated with a reason. **This is the rule, and it lives here until a CONTRIBUTING.md exists to hold it.**

**D2 and D3 are closed as of 2026-07-17**, 18 days after they were opened and long past the three-day SLA the rule states. Recording that plainly rather than quietly marking them done: the SLA was breached by a factor of six, and the pair took **under an hour** to settle once actually attempted. That is the lesson worth keeping. Both were cheap; both sat open for weeks; and both turned out to answer the same question.

**What D2 and D3 turned out to share.** They were logged as two decisions and are really one fact: **the ecosystem's unit of distribution is the skill, not the template.** The CLI installs skills (`SKILL.md` required); the spec defines skills (templates are an *asset inside* one). This library ships no `SKILL.md`, so today it is **not installable or listable by either route**, and no amount of metadata changes that. The blocker is a single missing file, not an architecture problem, which makes the "agent-native" claim's remaining debt smaller and more concrete than it looked.

**Consequence for the roadmap:** WP-52 (distribution wiring) was scheduled "per D2/D3 outcomes". The outcome is now known, so it is no longer research: it is "ship a `SKILL.md` that exposes the bundles as skill assets" (roadmap LP-2), whose name must be lowercase, hyphenated, and match its directory, with a description under 1024 characters. The reference validator `skills-ref validate ./my-skill` exists to check it.

## The claim, and what it is currently worth

The front door claims a **governed, best-in-class, agent-native reference implementation**. As of today:

- **Earned:** researched, dual-reader, nesting-disciplined, provenance-stamped content that the named competitors (curated awesome-lists) do not attempt.
- **Now true, as of M0:** licensed, decision-recorded, CI-enforced (the gate runs on every push and PR, and branch protection requires it before merge), and living at an address that describes it (`templates/`, not `_local/templates/`).
- **Still on credit:** "agent-native" (no machine consumption path exists, so no agent can select a bundle deterministically; and per D2/D3, resolved 2026-07-17, the library is not installable or listable by the skills CLI or agentskills.io either, because it ships no `SKILL.md`) and "reference implementation" (untagged, 6 of 205 types, zero external users).

Keep this section honest. It is the fastest way to tell whether the roadmap is working.
