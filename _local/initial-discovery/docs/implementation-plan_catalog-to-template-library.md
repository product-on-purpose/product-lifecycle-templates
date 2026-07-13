---
id: TL-01
title: "Template Library (catalog to v0.2): implementation plan"
type: implementation-plan
status: draft
created: 2026-06-29
updated: 2026-06-29
linked-spec: _local/initial-discovery/docs/template-library-design-spec.md
linked-specs:
  - _local/initial-discovery/docs/template-system-layered-design.md
linked-strategy-brief: _local/initial-discovery/docs/strategy-brief_catalog-to-template-library.md
linked-catalog: _local/initial-discovery/docs/deep-research_master-catalog.md
linked-effort: null
linked-release: null
phase-count: 7
ac-coverage: complete
target-release: v0.2.0
priority: P1
---

# Implementation Plan: Template Library (catalog to v0.2)

> **Scope note (read first).** This plan implements the static **Layer 0** template library defined in [`template-library-design-spec.md`](template-library-design-spec.md), sequenced per the [strategy brief](strategy-brief_catalog-to-template-library.md) (Approach A: static library, one-bundle-first, mirror `pm-skills`). It covers the path from the [Master Catalog](deep-research_master-catalog.md) to a tagged **v0.2** (one reference bundle, then one complete family). The optional **Layer 1 generator** is deliberately out of scope and held behind the decision gate in [D1](#d1-build-the-layer-1-generator-or-not-open).
>
> **On acceptance criteria.** The "AC" referenced here are restated, condensed, from the design spec's **§13 Definition of Done** (AC-1..AC-10) and its **§10 / §11 / §12 / §14 / §16** system requirements (AC-11..AC-14). They are not introduced by this plan. To change a criterion, revise the design spec, not this plan.

## Task Summary

**Status:** draft
**Last updated:** 2026-06-29 by jp-implementation-plan
**Linked spec:** `_local/initial-discovery/docs/template-library-design-spec.md`
**Phases:** 7
**AC coverage:** complete
**Open questions:** 4 (see [Open Questions / Decisions](#open-questions--decisions))

### Completion Status

| Phase | Goal | Fulfills AC | Owner | Status |
|-------|------|-------------|-------|--------|
| P1 | Settle + record the four foundational decisions as ADRs | AC-1, AC-5, AC-9 | human | Not started |
| P2 | Scaffold repo skeleton, conventions, and the `profiles/` attach point | AC-11 | either | Not started |
| P3 | Port the CI quality gate from `pm-skills` | AC-1, AC-4, AC-5, AC-6, AC-7, AC-8, AC-9 | LLM | Not started |
| P4 | Build the `deliver-prd` reference bundle end-to-end | AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-7, AC-8, AC-9, AC-10, AC-14 | either | Not started |
| P5 | Wire distribution (catalog/manifest, plugin + marketplace); tag v0.1 | AC-11, AC-13, AC-14 | either | Not started |
| P6 | Complete the `delivery-docs` family + family contract + validator; tag v0.2 | AC-12, AC-14 | either | Not started |
| P7 | Stand up the demand-gated roadmap + generator decision-gate checkpoint | AC-12, AC-14 | human | Not started |

(See the design spec §13 for the source DoD. Update this table as phases complete; it is the source of truth for progress. Tick `Done` only with evidence: a commit, PR, or passing CI run.)

---

### Acceptance Criteria (restated from the design spec)

These are the targets each phase maps to. Source section in parentheses.

| AC | Criterion | Source |
|----|-----------|--------|
| AC-1 | All declared variants present; section IDs nest (smaller is a strict subset of larger) | §13, §6 |
| AC-2 | `example.md` is a genuine worked example, not placeholder filler | §13 |
| AC-3 | `guide.md` includes when-to-use, a quality rubric, and named anti-patterns | §13 |
| AC-4 | `template.meta.yaml` passes schema lint | §13, §9.1 |
| AC-5 | Placeholder convention consistent (`{{snake_case}}`) across all variants | §13, §5 |
| AC-6 | Guidance lives in HTML comments and strips cleanly on render | §13, §5 |
| AC-7 | Zero emdash/endash characters (CI sweep) | §13, §5 |
| AC-8 | Valid YAML frontmatter on every variant | §13 |
| AC-9 | `pairs_with` resolves to known `pm-skills` skill IDs or is explicitly `null` | §13, §10 |
| AC-10 | A HISTORY entry exists for the current `template_version` | §13, §14 |
| AC-11 | Shared distribution rails + plugin/marketplace manifests present and install-validated | §10.2, §12 |
| AC-12 | A family contract exists and CI enforces family conformance | §11 |
| AC-13 | Generated `catalog.md` + `manifest.json` with a count-consistency guard | §8, §14 |
| AC-14 | v0.1 = one bundle exercises every pattern; v0.2 = one complete family | §16 |

---

## Phase 1: Settle and record the four foundational decisions as ADRs

**Addresses:** AC-1, AC-5, AC-9

These four decisions are expensive to reverse once bundle content exists (strategy brief §5). Settle them first and record each as a dated decision file so later phases have a fixed convention to build and lint against.

### Steps

1. Create `docs/decisions/` in the repo root (mirrors the `pm-skills` `develop-adr` / MADR convention; filename pattern `YYYYMMDD-title.md`).
2. Write `docs/decisions/20260629-repo-and-package-name.md`: record that **`product-lifecycle-templates` is used everywhere** (resolved 2026-06-29) - the git repo, the plugin/marketplace `name` field, and the install command; the `pm-` family handle is dropped (the broader name ages better if the library spans general software docs beyond PM, design spec §15). State the install string `npx skills add product-on-purpose/product-lifecycle-templates` and `name: product-lifecycle-templates` in `.claude-plugin/plugin.json`.
3. Write `docs/decisions/20260629-variant-model.md`: record the **descriptive-filename variant model** - ship the number of variants a type earns (most earn two: `template.lean.md` and `template.full.md`; use `template.s.md`/`template.m.md`/`template.l.md` only where three weights genuinely differ), keep the **strict nesting rule** (a smaller variant's section IDs are a subset of the larger's). This resolves the contradiction between design spec §6 (rigid S/M/L) and layered design §3 (lean/full, descriptive names) in favor of the latter. Note the residual open item in [D-resolved log].
4. Write `docs/decisions/20260629-phase-vocabulary.md`: record that **`phase` frontmatter values are lowercase** (`discover`, `define`, `develop`, `deliver`, `measure`, `iterate`, plus `foundation`, `tool`) and **bundle IDs are `<phase>-<doctype>`** (e.g. `deliver-prd`), matching the real `pm-skills` frontmatter (verify against `E:/Projects/product-on-purpose/pm-skills/skills/deliver-prd/SKILL.md` line 6). This corrects the design spec's capitalized `phase: Deliver`.
5. Write `docs/decisions/20260629-first-family-and-bundle.md`: record **first family = `delivery-docs`**, **first bundle = `deliver-prd`**, chosen because its `pairs_with` targets already exist in `pm-skills` (`deliver-prd`, `deliver-user-stories`, `deliver-acceptance-criteria`, `deliver-release-notes`).
6. In each ADR, fill the standard sections: context, decision, consequences, status `accepted`.

### Verification

- [ ] Four files exist under `docs/decisions/` with `YYYYMMDD-` prefixes and `status: accepted`.
- [ ] Each ADR states a single decision with a concrete chosen value (name string, filename pattern, casing rule, family/bundle IDs).
- [ ] The phase-vocabulary ADR's lowercase values match `pm-skills/skills/deliver-prd/SKILL.md` `metadata.phase`.

### Decision Gate

**Blocking.** All four decisions must be `accepted` before P2-P4 start: P2 (the repo scaffold) needs the name (manifests), P3 (the CI gate) needs the placeholder + phase conventions (lints), P4 (the reference bundle) needs the variant model + family/bundle IDs. If any is left open, downstream phases inherit churn.

### Output Artifacts

- `docs/decisions/20260629-repo-and-package-name.md` - created
- `docs/decisions/20260629-variant-model.md` - created
- `docs/decisions/20260629-phase-vocabulary.md` - created
- `docs/decisions/20260629-first-family-and-bundle.md` - created

### Suggested Owner

human - these are identity/branding and convention judgment calls (strategy brief §7); an agent can draft, but a human ratifies.

---

## Phase 2: Scaffold repo skeleton, conventions, and the `profiles/` attach point

**Addresses:** AC-11

Stand up the directory structure and root files from design spec §8, mirroring `pm-skills` so linters and rails are shared in spirit. Reserve the generator attach point per layered design §10 without building any generator.

### Steps

1. Create the top-level tree from design spec §8:
   - `templates/` (bundles live here)
   - `_families/` (family contracts)
   - `docs/reference/` and `docs/guides/`
   - `scripts/` (lint + validate + generate)
   - `.github/workflows/`
   - `.claude-plugin/`
   - `profiles/` with a `profiles/README.md` stating intent: "Reserved attach point for the optional Layer 1 generator (see template-system-layered-design.md). Empty by design; build nothing here until the decision gate D1 clears."
2. Author root files, porting structure from the corresponding `pm-skills` files (`E:/Projects/product-on-purpose/pm-skills/`):
   - `README.md` - positioning paragraph from design spec §1-§3; one-line "N bundles" count (start at 0, becomes 1 after P4 (the reference bundle build)).
   - `AGENTS.md` - universal agent-discovery file (adapt `pm-skills/AGENTS.md` header + a templates catalog section).
   - `LICENSE` - Apache-2.0 (copy from `pm-skills/LICENSE`).
   - `CONTRIBUTING.md`, `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` (adapt from `pm-skills` equivalents).
   - `.gitignore` (include `_output-jp-library/`, `node_modules/`, `_local/`), `.gitattributes`, `.nvmrc` (copy `pm-skills/.nvmrc`), `package.json` (name `product-lifecycle-templates`, scripts wired in P3 (the CI gate port)).
3. Author `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` with the `name` from the P1 (foundational ADRs) name ADR; align field names to `pm-skills/.claude-plugin/plugin.json` (verify the real schema there before writing). Leave `entries` empty until P5.
4. Create `templates/.gitkeep` and `_families/.gitkeep` so the empty dirs commit.

### Verification

- [ ] `find . -maxdepth 2 -type d` shows `templates/`, `_families/`, `docs/reference/`, `docs/guides/`, `scripts/`, `.github/workflows/`, `.claude-plugin/`, `profiles/`.
- [ ] `node -e "JSON.parse(require('fs').readFileSync('.claude-plugin/plugin.json'))"` exits 0 (valid JSON).
- [ ] `profiles/README.md` exists and states the "build nothing yet" intent.
- [ ] No emdash/endash anywhere: `node scripts/check-emdash.mjs` is deferred to P3, so for now grep manually.

### Decision Gate

N/A - no decision required before Phase 3 (P1 already fixed the name used in the manifests).

### Output Artifacts

- Repo skeleton directories - created
- `README.md`, `AGENTS.md`, `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `.gitignore`, `.gitattributes`, `.nvmrc`, `package.json` - created
- `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` - created
- `profiles/README.md` - created

### Suggested Owner

either - mostly mechanical porting; an LLM can do it, a human may prefer to hand-tune the README positioning.

---

## Phase 3: Port the CI quality gate from `pm-skills`

**Addresses:** AC-1, AC-4, AC-5, AC-6, AC-7, AC-8, AC-9

Build only the checks that protect a single bundle's contract (design spec §13 CI script list). Port each from its `pm-skills` analog so tooling lineage is shared. Defer the family validator to P6 (the delivery-docs family) and the catalog generator to P5 (distribution and v0.1 tag).

### Steps

1. `scripts/check-emdash.mjs` - port from `E:/Projects/product-on-purpose/pm-skills/scripts/check-emdash-scars.mjs`; scan `templates/**` and root docs for U+2014 / U+2013; exit non-zero on any hit (AC-7).
2. `scripts/lint-template-frontmatter.mjs` - adapt from `pm-skills/scripts/lint-skills-frontmatter.*` + `check-frontmatter-yaml.mjs`; validate that every `template.*.md` has parseable YAML frontmatter (AC-8) with required instance fields from design spec §9.2 (`title`, `doc_type`, `size`, `owner`, `status`, `doc_version`, `created`, `updated`, `source_template`, `source_template_version`).
3. `scripts/validate-meta-schema.mjs` - validate `template.meta.yaml` against the catalog-meta field set in design spec §9.1 (`id`, `title`, `summary`, `doc_type`, `phase`, `sizes_available`, `methodology`, `pairs_with`, `status`, `template_version`, `last_reviewed`, `license`); enforce `sizes_available` matches the variant files present (AC-4).
4. `scripts/check-size-nesting.mjs` - parse section IDs (HTML-comment anchors or heading slugs) from each variant; assert the smaller variant's set is a strict subset of the larger's (AC-1, per the P1 (foundational ADRs) variant-model ADR nesting rule).
5. `scripts/check-placeholder-convention.mjs` - assert every placeholder matches `{{snake_case}}` across variants (AC-5); flag camelCase or spaced placeholders.
6. `scripts/check-guidance-comments.mjs` - assert author guidance is inside `<!-- ... -->` and that stripping comments leaves valid markdown (AC-6).
7. `scripts/validate-pairs-with.mjs` - read a pinned ID list `scripts/known-skill-ids.txt` (seed it from `pm-skills/skill-manifest.json` skill names); assert each bundle's `pairs_with` entry is in the list or is explicitly `null` (AC-9).
8. Provide `.sh`/`.ps1` thin wrappers for the two checks the design spec names as shell pairs if cross-shell parity is wanted (`check-emdash`, `lint-template-frontmatter`); the rest can stay `.mjs` (match whatever `pm-skills` does per script).
9. Wire `package.json` `scripts`: `"lint": "node scripts/lint-template-frontmatter.mjs && node scripts/validate-meta-schema.mjs && node scripts/check-size-nesting.mjs && node scripts/check-placeholder-convention.mjs && node scripts/check-guidance-comments.mjs && node scripts/validate-pairs-with.mjs && node scripts/check-emdash.mjs"`.
10. `.github/workflows/ci.yml` - run `npm run lint` on push/PR; Node version from `.nvmrc`.

### Verification

- [ ] `npm run lint` exits 0 on the empty `templates/` dir (no bundles yet, no failures).
- [ ] Seed a deliberately broken fixture under `scripts/__fixtures__/bad-bundle/` (camelCase placeholder, an emdash, a missing meta field) and confirm each script flags its own failure class, then delete the fixture.
- [ ] `.github/workflows/ci.yml` parses (`node -e` YAML check or push to a branch and observe the run).

### Decision Gate

N/A - no decision required before Phase 4. (Whether to ship `.sh`/`.ps1` for every script vs `.mjs`-only is a style choice; default to matching `pm-skills` per-script and move on.)

### Output Artifacts

- `scripts/check-emdash.mjs`, `scripts/lint-template-frontmatter.mjs`, `scripts/validate-meta-schema.mjs`, `scripts/check-size-nesting.mjs`, `scripts/check-placeholder-convention.mjs`, `scripts/check-guidance-comments.mjs`, `scripts/validate-pairs-with.mjs` - created
- `scripts/known-skill-ids.txt` - created
- `.github/workflows/ci.yml` - created
- `package.json` - modified (scripts block)

### Suggested Owner

LLM - mechanical port of existing scripts with clear source files; deterministic to verify.

---

## Phase 4: Build the `deliver-prd` reference bundle end-to-end

**Addresses:** AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-7, AC-8, AC-9, AC-10, AC-14

The single most important phase: one bundle that exercises every pattern in the spec (design spec §16 v0.1). Everything after this is repetition. Source the structure from the catalog entry #29 (PRD) and the existing `pm-skills` template.

### Steps

1. Create `templates/deliver-prd/`.
2. `templates/deliver-prd/template.meta.yaml` - catalog meta per design spec §9.1 / Appendix A: `id: deliver-prd`, `title: Product Requirements Document`, `doc_type: prd`, `phase: deliver` (lowercase per P1), `family: delivery-docs`, `sizes_available: [lean, full]` (per P1 variant ADR), `methodology: generic`, `pairs_with: [deliver-prd]`, `status: beta`, `template_version: 0.1.0`, `tags: [requirements, delivery, prd]`, `related_templates: [deliver-user-stories, deliver-release-notes]`, `last_reviewed: 2026-06-29`, `license: Apache-2.0`.
3. `templates/deliver-prd/template.lean.md` - the small variant. Instance frontmatter per design spec §9.2 / Appendix B (`doc_type: prd`, `size: lean`, provenance fields `source_template: deliver-prd`, `source_template_version: 0.1.0`, placeholders `{{title}}`, `{{owner}}`, `{{version}}`, `{{date}}`). Body sections (catalog #29 + design spec §6 nesting example): `problem`, `goals-non-goals`, `scope`, `success-metrics`. Author guidance for each section in `<!-- ... -->` comments.
4. `templates/deliver-prd/template.full.md` - the large variant. Same frontmatter shape with `size: full`; body is a **strict superset**: the four lean sections (identical section IDs) plus `users-personas`, `user-stories`, `ux-design`, `risks`, `dependencies`, `rollout`, `open-questions`, `appendix`. Verify section-ID nesting against the lean variant.
5. `templates/deliver-prd/example.md` - a genuine worked PRD (AC-2): a realistic, fully filled instance (not lorem), e.g. a concrete feature, with every full-variant section populated and the provenance frontmatter stamped. Mirror the quality bar of `pm-skills/skills/deliver-prd/references/EXAMPLE.md`.
6. `templates/deliver-prd/guide.md` - when-to-use, the quality rubric, and named anti-patterns (AC-3). Pull the "When to Use / When NOT to Use" framing from `pm-skills/skills/deliver-prd/SKILL.md` and Cagan's caution (catalog #29: "the majority of the product spec should be the high-fidelity prototype") as a named anti-pattern.
7. `templates/deliver-prd/HISTORY.md` - first entry for `template_version: 0.1.0` (AC-10), dated 2026-06-29.
8. Run `npm run lint`; fix any failures until green.

### Verification

- [ ] `npm run lint` exits 0 with the bundle present.
- [ ] `node scripts/check-size-nesting.mjs` confirms `template.lean.md` section IDs are a strict subset of `template.full.md` (AC-1).
- [ ] `example.md` contains no `{{placeholder}}` tokens (it is filled, not a template) and no emdash.
- [ ] `guide.md` contains all three required parts: a "When to use" section, a rubric (checklist or table), and at least two named anti-patterns.
- [ ] `validate-pairs-with.mjs` resolves `deliver-prd` against `scripts/known-skill-ids.txt` (AC-9).
- [ ] `validate-meta-schema.mjs` confirms `sizes_available: [lean, full]` matches the two variant files (AC-4).

### Decision Gate

N/A - the variant model and conventions were fixed in P1 (the foundational ADRs); this phase consumes them.

### Output Artifacts

- `templates/deliver-prd/template.meta.yaml`, `template.lean.md`, `template.full.md`, `example.md`, `guide.md`, `HISTORY.md` - created

### Suggested Owner

either - an LLM can draft all six files; a human should validate that `example.md` and `guide.md` clear the "genuinely worth shipping" quality bar (AC-2, AC-3), since that is the differentiation and an agent tends to under-deliver on real-example richness.

---

## Phase 5: Wire distribution, generate the catalog/manifest, and tag v0.1

**Addresses:** AC-11, AC-13, AC-14

Make the one bundle installable and discoverable on the same rails as `pm-skills`, then cut the first release (design spec §12, §14, §16 v0.1).

### Steps

1. `scripts/generate-catalog.mjs` - adapt from `pm-skills/scripts/gen-skill-manifest.mjs`; walk `templates/*/template.meta.yaml`, emit `catalog.md` (human index) and `manifest.json` (machine catalog) at repo root (AC-13).
2. `scripts/check-count-consistency.mjs` - adapt from `pm-skills/scripts/check-count-consistency.*`; assert the bundle count is identical across `README.md`, `manifest.json`, and `marketplace.json` (AC-13 guard).
3. Run `node scripts/generate-catalog.mjs`; commit generated `catalog.md` and `manifest.json`.
4. Update `.claude-plugin/marketplace.json` `entries` with the `deliver-prd` entry (design spec Appendix C shape: `id`, `doc_type`, `phase`, `sizes_available`, `pairs_with`, `path: templates/deliver-prd`).
5. Update `README.md` bundle count to 1; run `node scripts/check-count-consistency.mjs` until green.
6. Add the two new scripts to `package.json` `lint`/`build` and to `.github/workflows/ci.yml`.
7. Validate installability (AC-11): test `git clone` and ZIP paths always; run the `skills` CLI install against the repo and record the result in `docs/reference/distribution-test.md`. If the CLI ignores a repo with no `SKILL.md`, that confirms [D2](#d2-does-the-skills-cli-install-a-template-only-repo-open) and means the `use-template` companion skill is required (defer the build, log the finding).
8. Update `CHANGELOG.md` with the v0.1.0 entry; tag `v0.1.0` (Conventional Commits + SemVer, per design spec §14).

### Verification

- [ ] `node scripts/generate-catalog.mjs` produces `catalog.md` + `manifest.json` listing exactly one bundle.
- [ ] `node scripts/check-count-consistency.mjs` exits 0 (README, manifest, marketplace all say 1).
- [ ] `git clone` of the repo into a temp dir surfaces `templates/deliver-prd/` intact.
- [ ] `docs/reference/distribution-test.md` records the `skills` CLI result (installs / ignores).
- [ ] `git tag` shows `v0.1.0`.

### Decision Gate

**Decision surfaced, non-blocking for tagging:** the CLI-install test result (D2) determines whether the `use-template` companion skill is required for the distribution story. Log the outcome; it gates a *future* phase, not v0.1.

### Output Artifacts

- `scripts/generate-catalog.mjs`, `scripts/check-count-consistency.mjs` - created
- `catalog.md`, `manifest.json` - created (generated)
- `.claude-plugin/marketplace.json`, `README.md`, `CHANGELOG.md`, `package.json`, `.github/workflows/ci.yml` - modified
- `docs/reference/distribution-test.md` - created
- `v0.1.0` git tag

### Suggested Owner

either - generation and wiring are LLM-suitable; cutting the tag (release decision) is a human action.

---

## Phase 6: Complete the `delivery-docs` family + family contract + validator; tag v0.2

**Addresses:** AC-12, AC-14

Prove the family contract pattern (design spec §11, §16 v0.2) by completing the first family. Each new bundle is a repeat of P4 (the reference bundle pattern) against the now-proven contract.

### Steps

1. `_families/delivery-docs.contract.md` - author the family contract per design spec §11: shared section vocabulary, required catalog-meta fields and allowed values for the family, the size-nesting expectation, and the shareable-boundary rule (body vs guidance vs example). Model it on a `pm-skills` family contract (e.g. `E:/Projects/product-on-purpose/pm-skills/site/src/content/docs/reference/skill-families/meeting-skills-contract.md`).
2. Build three bundles, each a full P4 repeat (variants + example + guide + meta + HISTORY), sourced from the catalog:
   - `templates/deliver-user-stories/` (catalog #30; `pairs_with: [deliver-user-stories]`; likely `sizes_available: [full]` only, since a user story is inherently small - let the type earn its variant count per the P1 (foundational ADRs) variant-model ADR).
   - `templates/deliver-acceptance-criteria/` (catalog #38; `pairs_with: [deliver-acceptance-criteria]`).
   - `templates/deliver-release-notes/` (catalog #115; `pairs_with: [deliver-release-notes]`; lean = customer-facing, full = customer + internal).
3. `scripts/validate-template-family.mjs` - adapt from `pm-skills/scripts/validate-skill-family-registration.*` + `validate-meeting-skills-family.*`; enforce, for every member of a declared family: filename convention, manifest schema, declared sizes present, example + guide present, nesting integrity (AC-12).
4. Add `validate-template-family.mjs` to `package.json` `lint` and CI.
5. Regenerate `catalog.md` + `manifest.json` (now four bundles); update `README.md` count to 4; run count-consistency until green.
6. Update `CHANGELOG.md`; tag `v0.2.0`.

### Verification

- [ ] `node scripts/validate-template-family.mjs delivery-docs` exits 0 (all four members conform).
- [ ] `npm run lint` exits 0 across all four bundles.
- [ ] Each new bundle's `pairs_with` resolves against `scripts/known-skill-ids.txt`.
- [ ] `catalog.md` lists four bundles; count-consistency passes.
- [ ] `git tag` shows `v0.2.0`.

### Decision Gate

N/A - no decision blocks subsequent work; P7 (the demand-gated roadmap) is governance, not a build dependency.

### Output Artifacts

- `_families/delivery-docs.contract.md` - created
- `templates/deliver-user-stories/`, `templates/deliver-acceptance-criteria/`, `templates/deliver-release-notes/` (full bundles) - created
- `scripts/validate-template-family.mjs` - created
- `catalog.md`, `manifest.json`, `README.md`, `CHANGELOG.md`, `package.json`, `.github/workflows/ci.yml` - modified
- `v0.2.0` git tag

### Suggested Owner

either - bundles are P4 repeats (LLM-suitable); the family contract benefits from a human pass to set allowed-value vocabularies deliberately.

---

## Phase 7: Stand up the demand-gated roadmap and the generator decision-gate checkpoint

**Addresses:** AC-12, AC-14

Convert the catalog's tiering into a governed, pull-driven backlog rather than a build-everything mandate (catalog Recommendations 1-3, strategy brief §5). No new bundles are built speculatively here; this phase installs the *rules* for what gets built next and when.

### Steps

1. `docs/reference/roadmap.md` - record the tiered sequencing:
   - **Tier 1 (must-have 28, catalog TL;DR):** list the 28 with their target `<phase>-<doctype>` IDs and `pairs_with` targets; mark `delivery-docs` done. A Tier-1 bundle graduates only when a team pulls it (catalog Recommendation 1 threshold).
   - **Tier 2 (methodology + discipline packs):** list candidate families (`scrum-docs`, `shape-up-docs`, `amazon-working-backwards`, `ux-discovery`, `analytics`, `release-ops`); rule: build a pack only when a team is actively practicing it (catalog Recommendation 2).
   - **Tier 3 (regulated):** a separate, access-controlled module with built-in traceability fields; FDA/ISO 14971/SOC 2/GDPR; gate on operating in a regulated domain; verify current regulation text on ecfr.gov before authoring (catalog Recommendation 3, QMSR note effective 2026-02-02).
2. `docs/reference/pull-queue.md` - a lightweight intake: a team requesting a bundle adds a row (requested type, requesting team, methodology in use, target date); the next bundle to build is the top pulled row, not the next catalog number.
3. `scripts/check-count-consistency.mjs` - extend to assert the Tier-1 "N of 28" progress count matches between `README.md` and `roadmap.md`.
4. Add an **alias-index** stub `alias-index.json` (catalog Appendix; design spec discoverability): map known aliases to canonical bundle paths (seed from the catalog's alias entries for the four shipped bundles, e.g. `"product spec" -> "templates/deliver-prd"`). Wire a CI check that every alias target path exists.
5. **Generator decision-gate checkpoint:** in `docs/decisions/`, open `docs/decisions/2026XXXX-generator-decision-gate.md` as `status: open` capturing the [D1](#d1-build-the-layer-1-generator-or-not-open) question (one-time fork vs recurring re-apply, layered design §9). Do not build the generator. Schedule a review against real usage after Tier 1 has two or more families shipped.

### Verification

- [ ] `docs/reference/roadmap.md` lists all three tiers; Tier 1 enumerates the 28 with IDs; `delivery-docs` marked done.
- [ ] `docs/reference/pull-queue.md` exists with the intake table schema.
- [ ] `alias-index.json` validates: every target path exists on disk for shipped bundles.
- [ ] `docs/decisions/2026XXXX-generator-decision-gate.md` exists as `status: open` and references the layered design §9 gate.

### Decision Gate

**D1 (open, deferred):** whether to build the Layer 1 generator. This phase records the gate; it does not resolve it. Resolution requires real usage evidence (is customization one-time or recurring?). Until resolved, `profiles/` stays empty (P2, the repo scaffold).

### Output Artifacts

- `docs/reference/roadmap.md`, `docs/reference/pull-queue.md` - created
- `alias-index.json` - created
- `docs/decisions/2026XXXX-generator-decision-gate.md` - created (status: open)
- `scripts/check-count-consistency.mjs` - modified (Tier-1 progress guard)

### Suggested Owner

human - tiering, pull-prioritization, and the generator gate are sequencing/strategy judgment calls (strategy brief §7); an agent maintains the files, a human sets priority.

---

## Open Questions / Decisions

| ID | Title | Resolution | Status | Updated |
|----|-------|------------|--------|---------|
| D1 | Build the Layer 1 generator or not | (pending real-usage evidence) | Open | 2026-06-29 |
| D2 | Does the `skills` CLI install a template-only repo (no SKILL.md) | (pending CLI test in P5) | Open | 2026-06-29 |
| D3 | Does agentskills.io define a non-skill "resource/template" type | (pending spec read) | Open | 2026-06-29 |
| D4 | Regulated-tier (Tier 3) scope and appetite | (pending domain decision) | Open | 2026-06-29 |

Resolved 2026-06-29 (recorded as ADRs in P1 (foundational decisions), listed here for traceability): repo/package name (`product-lifecycle-templates` everywhere, `pm-` handle dropped); variant model (descriptive lean/full + strict nesting, `s/m/l` only where a type earns three weights); phase vocabulary (lowercase, `<phase>-<doctype>`); first family/bundle (`delivery-docs` / `deliver-prd`).

### D1: Build the Layer 1 generator, or not (Open)

**Summary.** Whether to build the optional org-profile generator (layered design Layer 1).

**Context.** The generator's value is conditional on a fact not yet in evidence: is org template customization a one-time fork (git suffices, no generator) or a recurring re-apply as the upstream library improves (the generator becomes "the actual point")? Layered design §9 is explicit: build nothing for Layer 1 until this is answered.

**Desired outcome.** A clear go/no-go after Tier 1 has shipped two or more families and real teams have customized templates.

**Options / approaches.**
- **Option A:** Defer (recommended). Keep `profiles/` reserved and empty; revisit after v0.2 + real usage.
- **Option B:** Build now as a sibling utility (packaging Shape C). Rejected for now: spends the early window on an unproven bet (strategy brief Approach C).

**Recommendation.** Option A. Re-open this gate only with usage evidence.

---

> **Maintainer decision:** _(pending)_
>
> * **Status:** Open
> * **Choice:** (none)
> * **Reasoning:** (none)
> * **Decided by / date:** (none)

### D2: Does the `skills` CLI install a template-only repo (Open)

**Summary.** Whether `npx skills add ...` installs a repo with no `SKILL.md`.

**Context.** Determines whether the `use-template` companion skill (design spec §12) is *required* for CLI distribution or merely a convenience. Tested in P5 (the distribution phase) step 7.

**Recommendation.** Run the test in P5; if the CLI ignores the repo, schedule the `use-template` companion skill as the first post-v0.2 utility. Git clone and ZIP paths work regardless, so this does not block v0.1.

---

> **Maintainer decision:** _(pending)_
>
> * **Status:** Open
> * **Choice:** (none)
> * **Reasoning:** (none)
> * **Decided by / date:** (none)

### D3: Does agentskills.io define a non-skill "resource/template" type (Open)

**Summary.** Whether the manifest should conform to an existing spec type rather than inventing one (design spec §17 item 2).

**Context.** If the spec defines a template/resource type, `template.meta.yaml` and `manifest.json` should match it for ecosystem coherence.

**Recommendation.** Read the current agentskills.io spec before v1.0; cheap to align early, costly to retrofit after many bundles.

---

> **Maintainer decision:** _(pending)_
>
> * **Status:** Open
> * **Choice:** (none)
> * **Reasoning:** (none)
> * **Decided by / date:** (none)

### D4: Regulated-tier (Tier 3) scope and appetite (Open)

**Summary.** Whether the library serves regulated domains at all.

**Context.** Tier 3 artifacts (FDA design controls, ISO 14971, SOC 2, GDPR) are auditable and demand traceability-first templates plus current-regulation verification (catalog Recommendation 3; QMSR effective 2026-02-02). A blank-but-wrong regulated template is worse than none.

**Recommendation.** Out of scope for v0.2. Decide appetite before any Tier 3 work; if yes, build it as a separate access-controlled module with built-in traceability fields.

---

> **Maintainer decision:** _(pending)_
>
> * **Status:** Open
> * **Choice:** (none)
> * **Reasoning:** (none)
> * **Decided by / date:** (none)

---

## Revisions

| Date | Author | Type | Description |
|------|--------|------|-------------|
| 2026-06-29 | jp-implementation-plan | added | Initial plan created from the master catalog + design spec + strategy brief |

Types: `added`, `re-decomposed`, `phase-completed`, `closed`.

## Notes on this plan

- **AC are sourced, not invented.** AC-1..AC-14 restate the design spec's §13 Definition of Done and its §10/§11/§12/§14/§16 system requirements. To change a criterion, revise [`template-library-design-spec.md`](template-library-design-spec.md), then re-run the AC-coverage lint.
- **Round-trip links.** This plan's `linked-spec` points at the design spec; the design spec should carry a reciprocal `linked-implementation-plan` field (added alongside this plan) so the pair resolves both ways.
- **Phase boundaries** are reviewable/resumable units: P1 (decisions), P2 (skeleton), P3 (gate), P4 (the one bundle), P5 (ship it), P6 (the one family), P7 (govern the rest). A cold-start agent can open any phase and execute from its Steps without re-reading the source docs.
- **The 80/20 lives in P4.** If only one phase ships, it is P4 (plus the P1-P3 scaffolding it needs): a single fully-worked bundle is the v0.1 that proves the entire system (design spec §16; strategy brief §5).
