---
date: 2026-06-30T16:03:00
repo: https://github.com/product-on-purpose/product-lifecycle-templates
branch: main
summary: "Planned the template library from the master catalog, then built the full delivery-docs family (4 bundles) under a new methodology"
files-changed:
  - _local/initial-discovery/docs/strategy-brief_catalog-to-template-library.md
  - _local/initial-discovery/docs/implementation-plan_catalog-to-template-library.md
  - _local/initial-discovery/docs/template-library-design-spec.md
  - _local/templates/methodology.md
  - _local/templates/prd/ (8 files)
  - _local/templates/user-stories/ (8 files)
  - _local/templates/acceptance-criteria/ (8 files)
  - _local/templates/release-notes/ (8 files)
session-type: planning+feature+docs
model: claude opus 4.8
model-settings: explanatory output style; superpowers skills active
agent: claude-code
status: completed
decisions-count: 15
---

# Session Log: Template Library Planning and the delivery-docs Family

## Summary

Took the 205-type master catalog and three design docs from raw discovery to two outcomes: a decision-ready strategy brief plus a phased implementation plan, then a working methodology and the complete `delivery-docs` template family (PRD, user stories, acceptance criteria, release notes), four bundles of eight files each, all researched against real sources and verified by hand. The session settled several architecture decisions the source docs had left open or contradictory (naming, variant model, bundle identity) and established a repeatable bundle-authoring methodology. All output lives under `_local/`, which is gitignored, so nothing is yet version-controlled.

## Work Completed

- **Reviewed the discovery set**: `deep-research_master-catalog.md` (205 types, 19 categories, must-have 28), `template-library-design-spec.md`, `template-system-layered-design.md`, `pm-sdlc-document-research-prompt.md`, plus the sibling `pm-skills` repo's conventions.
- **Strategy brief** (`strategy-brief_catalog-to-template-library.md`): 7-section jp-strategy-brief; weighed three approaches, recommended Approach A (static library, one-bundle-first, mirror pm-skills), surfaced the three doc-level contradictions (variant model, phase casing, name).
- **Implementation plan** (`implementation-plan_catalog-to-template-library.md`): 7-phase jp-implementation-plan with completion-status table; AC mapped to the design spec's §13 Definition of Done (AC-1..AC-14, restated not invented); reciprocal `linked-*` frontmatter added to the design spec for round-trip integrity.
- **Methodology** (`_local/templates/methodology.md`): the repeatable research + drafting process governing every bundle. Research protocol (seed from catalog, tiered sources, live research, cite-or-cut, research log), drafting protocol, the fixed 11-section companion skeleton, the citation standard with reliability tags, and a per-bundle Definition of Done.
- **Four bundles built and verified** under `_local/templates/`: `prd/`, `user-stories/`, `acceptance-criteria/`, `release-notes/`. Each has 8 files: `_meta.yaml`, `_template-lean.md`, `_template-full.md`, `_companion.md`, `_guide.md`, `_example.md`, `_history.md`, `_research-log.md`.
- **Real research per bundle**: live web searches and fetches; sources tiered `[primary]`/`[practitioner]`/`[vendor]`; per-bundle research logs record retrieval status and limitations honestly.
- **Cross-bundle coherence**: all four examples chain on one fictional "Saved Views" feature (PRD -> stories -> acceptance criteria -> the 2.4.0 release note), so the family reads as one traceable set.
- **Project memory** written (outside the repo): `template-library-conventions.md` + `MEMORY.md` index capturing the locked decisions and family status.

## Decisions Made

1. **Approach A over breadth-first or library+generator (architectural).** Build the static library one fully-worked bundle at a time and mirror pm-skills, rather than mass-producing thin stubs (Approach B) or committing to the org-profile generator now (Approach C). Lowest-regret; matches the source docs' own logic; defers the unanswered generator question.
2. **Name: `product-lifecycle-templates` everywhere (user decision).** Dropped the `pm-` family handle entirely (repo, plugin/marketplace name, install command). Broader name ages better if the library outgrows pure PM; coherence with pm-skills is carried by shared conventions and `pairs_with`, not a name prefix.
3. **Drop the lifecycle-phase prefix from bundle IDs (architectural, user-prompted).** Bundles are named by document type (`prd/`, not `deliver-prd/`); phase lives in frontmatter (`phase: deliver`) and `pairs_with: [deliver-prd]` links the skill. Reason: the library's own spine is document type; phase is contested for cross-phase docs (the catalog files PRD under Requirements, not Deliver); keeping phase in metadata makes the eventual directory scaffold a derivable, deferred choice.
4. **Variant model: lean/full with descriptive filenames + strict nesting (architectural).** Resolved the design spec's rigid S/M/L against the layered doc's lean/full. Ship the variants a type earns (most earn two), keep the nesting rule (smaller is a strict subset), use s/m/l only where three weights genuinely differ. Rationale: the catalog's own size_variant column shows most types vary in two weights; descriptive names self-document; deterministic agent selection runs off `sizes_available` metadata, not filenames.
5. **Separate companion + guide, not one merged doc (user-approved).** Diataxis split: `_companion.md` is the deep dual-reader explainer with exhaustive references; `_guide.md` is the short operator card (when-to-use, rubric, anti-patterns). Each serves one reader-mode well.
6. **Real research per template (user decision).** Live web research per bundle with tiered, reliability-tagged citations, over curating from memory.
7. **Build location `_local/templates/`, scaffold deferred (user decision).** Provisional flat home; the flat-vs-nested directory decision is explicitly deferred and made cheap by keeping phase in metadata.
8. **Research log as an 8th file per bundle (agent call, flagged).** Kept a `_research-log.md` to demonstrate the methodology; flagged to the user that it could fold into the companion's references for future bundles.
9. **Fixed 11-section companion skeleton.** Orientation, Origins, Anatomy, Variants, Methodology lineage, Debates, Anti-patterns, Relationships, Adaptations, Worked example, References. Enforces dual-reader consistency.
10. **Citation standard with reliability tags.** `[primary]`/`[practitioner]`/`[vendor]`/`[internal]`; inline numbered citations must resolve 1:1 to the reference list; cite-or-cut; no fabricated sources.
11. **delivery-docs as the first family.** Its members (`prd`, `user-stories`, `acceptance-criteria`, `release-notes`) have live `pairs_with` targets in pm-skills, so the compatibility bridge has real anchors from day one.
12. **All examples chain on one feature.** "Saved Views" runs through all four bundles so the family demonstrates document lineage, not four isolated samples.
13. **Defer the Layer 1 generator behind the decision gate.** Recorded as an open decision; build nothing until usage shows whether org customization is one-time or recurring.
14. **Implementation plan maps AC to the design spec's §13 DoD.** Honored the jp-implementation-plan "AC live in the spec" rule by restating the design spec's Definition of Done rather than inventing acceptance criteria, since there was no formal jp-spec.
15. **Used jp-library skills for the planning deliverables.** jp-strategy-brief and jp-implementation-plan for the two planning docs; brainstorming to lock the methodology and bundle design before building.

## Files Changed

All paths under `_local/` (gitignored; working tree only).

**Planning (initial-discovery/docs/):**
- `strategy-brief_catalog-to-template-library.md` (created)
- `implementation-plan_catalog-to-template-library.md` (created)
- `template-library-design-spec.md` (edited: added `linked-strategy-brief`, `linked-implementation-plan` frontmatter)

**Methodology:**
- `_local/templates/methodology.md` (created)

**Bundles (8 files each, all created):**
- `_local/templates/prd/` : prd_meta.yaml, prd_template-lean.md, prd_template-full.md, prd_companion.md, prd_guide.md, prd_example.md, prd_history.md, prd_research-log.md
- `_local/templates/user-stories/` : user-stories_{meta.yaml, template-lean.md, template-full.md, companion.md, guide.md, example.md, history.md, research-log.md}
- `_local/templates/acceptance-criteria/` : acceptance-criteria_{meta.yaml, template-lean.md, template-full.md, companion.md, guide.md, example.md, history.md, research-log.md}
- `_local/templates/release-notes/` : release-notes_{meta.yaml, template-lean.md, template-full.md, companion.md, guide.md, example.md, history.md, research-log.md}

**Outside the repo (project memory):**
- `~/.claude/projects/E--Projects-.../memory/template-library-conventions.md` (created)
- `~/.claude/projects/E--Projects-.../memory/MEMORY.md` (created)

## Verification

**Verified by script (grep over `_local/templates/`):**
- [x] Zero em-dash / en-dash characters across all four bundles and the methodology.
- [x] Lean/full section nesting holds for all four bundles (every lean heading is present in the full variant; `comm -23` returns empty).
- [x] Zero `{{placeholders}}` left in any `_example.md`.
- [x] Companion inline citations resolve 1:1 to reference definitions: prd 13/13, user-stories 9/9, acceptance-criteria 8/8, release-notes 7/7.
- [x] 8 files per bundle; 33 files total under `_local/templates/` (32 bundle + methodology).

**Verified by direct web fetch (primary sources read, not just searched):**
- [x] Scrum Guide 2020 (three artifacts; PRD not canonical).
- [x] ProductPlan PRD glossary (canonical components).
- [x] Mike Cohn / Mountain Goat Software (user-story definition, Three C's, "placeholder for a conversation").
- [x] Wikipedia "User story" (dated history).
- [x] Keep a Changelog 1.1.0 (six change types, principles, changelog-vs-release-notes distinction).

**Assumed / corroborated, NOT directly fetched (flagged in each research log):**
- [ ] Cagan/SVPG pages (HTTP 403 to fetch); substance from search excerpts + catalog corroboration.
- [ ] Lenny's Newsletter PRD post (paywalled body); only public summary used.
- [ ] Scrum.org AC-vs-DoD page (rendered empty on fetch); substance from detailed search excerpt.
- [ ] SemVer and Conventional Commits (search-corroborated; primary URLs cited but not fetched).

**NOT verified / not done (important):**
- [ ] No real CI gate ran. Nesting/dashes/citations were checked by hand-written grep, NOT by the eventual CI scripts (which do not exist yet; they are P3 of the implementation plan).
- [ ] No bundle was "used" (filled by an author or via a use-template flow).
- [ ] No repo scaffold, no skeleton, no manifests, no marketplace entry.
- [ ] Nothing committed to git; `_local/` is gitignored.

## Evidence Index

- **Hand-verification commands**: grep for U+2014/U+2013; `comm -23` of sorted `## ` headings lean vs full; `grep -oE '\{\{...\}\}'` over examples; inline-vs-defined citation counts via `grep -oE '\[[0-9]+\]'` and `grep -cE '^\[[0-9]+\] '`. All run this session, all green.
- **Per-bundle research logs**: `<type>_research-log.md` in each bundle records every source, its tier, retrieval status (fetched/verified vs search-corroborated vs blocked), and the specific claims it supports.
- **Source tiers used**: primary (Scrum Guide, Keep a Changelog, SemVer, Conventional Commits, Pragmatic Institute, Dan North BDD); practitioner (Cagan/SVPG, Cohn, Jeffries, Wake, Klement/Intercom, Bryar & Carr); vendor (ProductPlan, Atlassian, Figma, Thoughtworks, Cucumber, Ranorex, Appcues/AnnounceKit).
- **Governing artifacts**: `_local/templates/methodology.md` (process + DoD); `implementation-plan_catalog-to-template-library.md` (7 phases, AC-1..AC-14); `strategy-brief_catalog-to-template-library.md` (approach + resolved decisions).

## Outstanding Issues

- **RISK (durability): all session output is gitignored.** Everything under `_local/` (40+ files: bundles, methodology, strategy brief, implementation plan) is in the working tree only and not under version control. If the working tree is lost, the work is lost. Decide whether `_local/` should stay gitignored or whether this work should graduate to a tracked path.
- **Scaffold undecided.** Flat (`templates/<type>/`) vs nested (`templates/<phase>/<type>/`). Cheap to choose later because phase is in metadata, but it blocks standing up the repo skeleton.
- **CI gate not built.** The checks that passed by hand need to exist as scripts (P3 of the plan: check-emdash, lint-template-frontmatter, check-size-nesting, validate-pairs-with) so quality is enforced, not manual.
- **Citation fidelity gaps.** Several sources were corroborated via search, not primary fetch (bot-blocks/paywalls). An audit-grade pass would capture exact quotes; flagged honestly in each research log but not resolved.
- **research-log as 8th file: open question.** Ship it per bundle or fold into the companion references? Pending user call.
- **meta.yaml extends the spec.** Added `aliases` and `catalog_ref` beyond the design spec's §9.1 field list; reconcile with the spec (or the spec's schema) when CI is built.
- **Keep a Changelog 2.0.0** is planned for 2026; the release-notes bundle cites 1.1.0 and should be re-checked when 2.0.0 ships.

## What's Next

1. **Decide whether `_local/` stays gitignored** or this work graduates to a tracked location. This is the durability question and should come first.
2. **Decide the scaffold** (flat `templates/<type>/` vs nested `templates/<phase>/<type>/`). Unblocks the repo skeleton.
3. **Stand up the repo skeleton + port the CI gate from pm-skills** (implementation plan P2 + P3) so the four bundles pass automatically instead of by hand.
4. **Resolve the research-log question** (8th file vs folded into companion).
5. **Continue Tier-1 bundles by pull** (the catalog's must-have 28), reusing `methodology.md` for each.
6. **Optional review pass** on the four bundles, especially the examples and guides, for quality before scaling.

## Continuation Prompt

```
Continue building the product-lifecycle-templates library (repo: E:/Projects/product-on-purpose/product-lifecycle-templates, branch: main).

CONTEXT: This is a local-first markdown template library derived from the 205-type master catalog in _local/initial-discovery/docs/deep-research_master-catalog.md, sibling to the pm-skills repo (we borrow its hygiene conventions, not its information architecture). Last session produced a strategy brief and a 7-phase implementation plan (both in _local/initial-discovery/docs/), a governing methodology (_local/templates/methodology.md), and the COMPLETE delivery-docs family: four bundles under _local/templates/ (prd, user-stories, acceptance-criteria, release-notes), eight files each (_meta.yaml, _template-lean.md, _template-full.md, _companion.md, _guide.md, _example.md, _history.md, _research-log.md). All four were researched against real, tiered sources and verified by hand (no em-dashes, lean-subset-of-full nesting, no placeholders in examples, companion citations all resolve). All four examples chain on one fictional "Saved Views" feature.

LOCKED CONVENTIONS (do not relitigate without reason): name = product-lifecycle-templates everywhere (no pm- prefix); bundles named by document type with NO phase prefix (prd/, not deliver-prd/); phase lives in frontmatter (phase: deliver) and pairs_with: [deliver-prd] links the pm-skills skill; variant model = lean/full with descriptive filenames + strict nesting (smaller is a subset of larger), s/m/l only where a type earns three weights; companion (deep explainer + tiered references) and guide (short operator card) are SEPARATE files; real web research per template with [primary]/[practitioner]/[vendor] reliability tags and cite-or-cut. Follow _local/templates/methodology.md for any new bundle (it defines the 11-section companion skeleton, the citation standard, and the per-bundle Definition of Done).

CRITICAL STATE NOTE: _local/ is gitignored, so ALL of last session's output is in the working tree only, NOT under version control. Before doing anything destructive to the working tree, confirm this work is safe.

IMMEDIATE NEXT ACTION: Ask me (the user) to decide two things that gate everything downstream: (1) whether _local/ should stay gitignored or this work graduates to a tracked path, and (2) the scaffold shape (flat templates/<type>/ vs nested templates/<phase>/<type>/). Present the trade-offs briefly and recommend one of each; do not start building scaffolding until both are answered.

THEN, in order: (a) stand up the repo skeleton and port the CI gate from pm-skills (implementation plan P2 + P3: check-emdash, lint-template-frontmatter, check-size-nesting, validate-pairs-with) so the four existing bundles pass automatically; (b) resolve whether the per-bundle research-log ships as an 8th file or folds into the companion references; (c) continue into the catalog's Tier-1 "must-have 28" bundles by pull, building each with the methodology. House rule: never use em-dash or en-dash characters in any output.
```

<!--
Note on surrounding docs: did not touch README.md or CHANGELOG.md. Nothing release-worthy is committed (all
work is in gitignored _local/), so neither warrants an update this session.
Transcript: this session's full tool history is in the Claude Code session transcript; not embedded here per policy.
-->
