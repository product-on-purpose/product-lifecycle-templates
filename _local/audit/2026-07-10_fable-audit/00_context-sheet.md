# Phase 0 Corpus Fingerprint and Context Sheet

Audit of `product-lifecycle-templates`, 2026-07-10. Built inline by the lead auditor before fan-out.
All paths are relative to the repo root `E:\Projects\product-on-purpose\product-lifecycle-templates` unless absolute.
House rule for all audit output: no em-dash (U+2014) or en-dash (U+2013) characters anywhere.

## 1. Repo identity and general inventory

- Remote: https://github.com/product-on-purpose/product-lifecycle-templates.git (origin), branch `main`, in sync.
- History: 5 commits, 2026-06-29 to 2026-07-03. Single contributor (jprisant). Zero git tags. No CHANGELOG.
  - `8fa24b0` 2026-06-29 Initial commit
  - `cd7c6bd` 2026-07-02 chore: version-control the working template library (HY-1)
  - `a52041e` 2026-07-02 feat(atlas): add the interactive Product Artifact Atlas (CT-3)
  - `3f9c39a` 2026-07-03 docs: write the front-door README
  - `737354e` 2026-07-03 feat(gate): add check-bundles.py governance gate
- 51 tracked files (~800 KB). 1 untracked: `_local/2026-07-10_overview.md` (a 2026-07-10 synthesis doc; secondary source, not governance).
- License: README.md:114-116 declares Apache-2.0; meta.yaml files and doc frontmatter declare `license: Apache-2.0`; **no LICENSE file exists in the tree** (verified via `git ls-files`).
- Everything of substance lives under `_local/` (deliberate, documented: `.gitignore:1-8` re-includes `_local/` and states "content stays under _local/ for now by choice"; README.md:69 calls it "a provisional home").

## 2. Governance corpus (the internal contract; judge against these first)

| # | Document | Path | Version / status | Role |
|---|---|---|---|---|
| G1 | Template Bundle Methodology | `_local/templates/methodology.md` | v0.2.0, status: draft, last_reviewed 2026-06-30 | THE operative rulebook: bundle contract, research protocol, citation standard (section 6), companion skeleton (section 5, 11 sections), guidance comment standard (B1: WHAT/WHY/ASK/GOOD/WEAK/TRAP + preamble), Definition of Done (section 7, 11 clauses) |
| G2 | Design spec | `_local/initial-discovery/docs/template-library-design-spec.md` | v0.1.0, draft, 2026-06-28 | Original formal spec: two-tier metadata (section 9), family contracts (section 11), distribution (section 12), DoD (section 13), governance (section 14). Partially superseded on: S/M/L naming, working name `pm-templates`, 6-file bundle anatomy |
| G3 | Strategy brief (catalog to library) | `_local/initial-discovery/docs/strategy-brief_catalog-to-template-library.md` | v0.1.0, draft, 2026-06-29 | Approach A decision; records the four foundational decisions as inline "[Resolved 2026-06-29 ...]" amendments (section 5): name, variant model (lean/full + nesting), phase vocabulary, first family |
| G4 | Implementation plan TL-01 | `_local/initial-discovery/docs/implementation-plan_catalog-to-template-library.md` | draft, created/updated 2026-06-29 | 7 phases P1-P7 with per-phase steps, verification, decision gates; AC-1..AC-14 restated from design spec section 13; open decisions D1-D4. NOTE: its Completion Status table (lines 38-46) says every phase "Not started" and line 48 calls that table "the source of truth for progress"; it was never updated after content was built |
| G5 | Layered design | `_local/initial-discovery/docs/template-system-layered-design.md` | v0.1.0, draft, 2026-06-28 | 3-layer model (library / generator / pm-skills), the bright line rule, generator decision gate, `profiles/` attach point |
| G6 | Raising-the-ceiling brief | `_local/initial-discovery/docs/strategy-brief_raising-the-ceiling_2026-07-02.md` | v0.1.0, draft, 2026-07-02 | The newest strategy layer: EV-1/2/3/4 (evals, scorecard, red-team, citation pass), LP-1/2/3 (use-template, grade-my-doc, telemetry), AG-1/2/3 (section schema, MCP, authoring kit), CT-1..4, FR-1/2 (staleness), VS-1..3, VL-1..3 (business model), HY-1..3; prioritization table and recommended sequence (section 5) |
| G7 | Master catalog | `_local/initial-discovery/docs/deep-research_master-catalog.md` | (no frontmatter version) | 205 artifact types, 19 groups, "must-have 28" Tier 1, Recommendations 1-6 (line 286+), caveats; the canonical scope document |
| G8 | Research prompt | `_local/initial-discovery/pm-sdlc-document-research-prompt.md` | n/a | Provenance of the catalog |
| G9 | Working-approaches note | `_local/templates/_working/README.md` | n/a | The A/B/C guidance-style experiment; recommends Approach A (adopted). Line 6 says "Delete `_working/` once you have decided"; the folder still exists |
| G10 | Session log | `_local/_session-logs/2026-06-30_16-03_claude_template-library-delivery-docs.md` | n/a | Build record of the four bundles; flags citation-verification honesty issues (Cagan/SVPG 403, Lenny paywall, Scrum.org empty render) |

**ADR files: none exist.** No `docs/internal/decisions/` anywhere. Decisions live inline: plan G4 lines 374-381 ("Resolved 2026-06-29" block), strategy brief G3 section 5 amendments, methodology G1 (bundle shape), `.gitignore:1-8` (location), `check-bundles.py:1-14` docstring (gate status "local prototype of the CI gate planned in the implementation plan (P3)").

## 3. Bundle inventory (against the declared contract)

The operative bundle contract is methodology G1 section 2 + DoD section 7: note the internal inconsistency that methodology.md:41 says "containing seven files" and its table lists 7 roles, while the de facto contract, the README (README.md:46-58), and the gate (`check-bundles.py:41-50` ROLES) all use **eight** files (adds `_research-log.md`; the DoD's Research clause requires it).

4 bundles, all in `_local/templates/<type>/`, all declaring `family: delivery-docs`, `status: beta`, `template_version: 0.1.0`, `sizes_available: [lean, full]`, `last_reviewed: 2026-06-30`:

| Bundle | 8 files present | pairs_with | catalog_ref | Notable |
|---|---|---|---|---|
| `prd` | yes (gate A pass) | `[deliver-prd]` | 29 | meta `related_templates` includes `solution-brief` (no such bundle exists); meta `maintainer: "{{maintainer}}"` is an unfilled placeholder |
| `user-stories` | yes | `[deliver-user-stories]` | (verify) | |
| `acceptance-criteria` | yes | `[deliver-acceptance-criteria]` | (verify) | |
| `release-notes` | yes | `[deliver-release-notes]` | (verify) | |

- Instance frontmatter in variants carries provenance (`source_template`, `source_template_version`); verified present in `prd_template-lean.md:11-12` and in the worked example `prd_example.md:13-14`.
- Guidance style: Approach A (enriched HTML comments; WHAT/WHY/ASK/GOOD/WEAK/TRAP), adopted per G9 and codified in methodology B1. Deep links into companions are **prose pointers inside comments** (e.g. "Deep dive: prd_companion.md section 3 (Anatomy > Summary)"), not clickable anchors; that is a documented Approach A trade-off (G9), so judge pointer accuracy (does the named section exist), not link syntax.
- Examples all chain on one fictional feature ("Saved Views" for dashboards, Acme, B2B SaaS analytics). Single-domain limitation is known and documented as CT-1 in G6.
- File size / rough token estimates (bytes/4): companions 3.2k-5.3k tokens (prd largest 21,387 B); full templates 2.0k-4.2k; lean 1.0k-1.8k; guides ~0.6k; examples 0.7k-2.3k; meta ~0.24k. No size or token fields are declared in any meta.yaml.

## 4. Catalog and scope

- Planned universe: 205 types / 19 categories (G7 TL;DR line 4). Tier 1 = must-have 28. Tier 2 = methodology packs. Tier 3 = regulated (QMSR note: effective 2026-02-02).
- Built: 4 of 205 (4 of the 28 Tier 1). The `delivery-docs` family is declared complete (README.md:27).
- Canonical catalog: G7. The atlas (`_local/atlas/atlas.html`, self-contained; data `_local/atlas/catalog-data.json`, `generated_from: deep-research_master-catalog.md`) renders all 205 types.
- No root `catalog.md` / `manifest.json` (planned in P5, absent). No `docs/reference/roadmap.md`, no `pull-queue.md`, no `alias-index.json` (planned in P7, absent).

## 5. Automation

- One gate: `_local/tools/check-bundles.py` (Python, 218 lines, committed 2026-07-03). Local-only; **no `.github/workflows/` exists; nothing runs in CI on push**. The plan (G4 P3) committed to seven Node `.mjs` scripts under `scripts/` plus `.github/workflows/ci.yml`. The Python/monolith/local deviation is self-documented as an interim prototype (docstring lines 8-9 and README.md:106).
- Gate checks (A-F): 8 files present; no em/en dashes; lean H2 headings are an ordered subset of full H2 headings (`HEADING_RE` at check-bundles.py:35 matches `##` only; H3+ and semantic drift are not checked); no `{{placeholder}}` left in example; companion inline `[[n]](#ref-n)` citations resolve to `<a id="ref-n">` anchors and no bare `[n]` remains in body (body = text before "## References", line 132); meta `sizes_available` matches variant files (regex parse, not schema validation).
- Gate run 2026-07-10 by lead auditor: **exit code 0, all 4 bundles pass all 6 checks.** Notable output detail: `prd` reports "13 anchors, 11 cited" (2 reference entries never cited inline; the gate only checks the inline-to-anchor direction, not the entry-is-used direction that the methodology's "no padded entries" DoD clause implies).
- Not automated anywhere: research-log claim tracing, guidance-comment structure, companion 11-section skeleton, guide 3-part structure, pairs_with resolution, history-entry-for-current-version, meta schema validation, frontmatter validity, placeholder convention in variants, link/anchor integrity outside companions, citation URL liveness/staleness, family contract conformance, count consistency.

## 6. Distribution surfaces

| Surface | Status |
|---|---|
| Plugin manifest (`.claude-plugin/plugin.json`) | absent |
| Marketplace metadata (`marketplace.json`) | absent |
| Root catalog (`catalog.md`) / machine manifest (`manifest.json`) | absent |
| MCP server | absent (AG-2 in G6: proposed, unbuilt; sibling `pm-skills-mcp` exists as a pattern) |
| Version tags | none (v0.1/v0.2 tagging planned in P5/P6) |
| CHANGELOG / CONTRIBUTING / AGENTS.md / CODE_OF_CONDUCT / SECURITY | all absent |
| LICENSE file | absent (declared Apache-2.0 in prose/meta only) |
| README.md | present (front door, 117 lines) |
| Atlas | present (repo-local HTML file, open-in-browser) |

Net: **no consumer can obtain the library today except by git clone or reading GitHub.**

## 7. Ecosystem seams

- Sibling `pm-skills` at `E:\Projects\product-on-purpose\pm-skills`: real and mature (68+ skills, `skill-manifest.json`, `.claude-plugin/`, CI scripts, site, evals). All four `pairs_with` targets exist both as skill directories and in `skill-manifest.json` (verified: deliver-prd, deliver-user-stories, deliver-acceptance-criteria, deliver-release-notes).
- `pm-skills/skills/deliver-prd/` contains `evals/` (behavioral eval harness pattern; relevant to EV-1 portability).
- Nothing on the pm-skills side references this template library back (per design spec section 4, that back-reference is optional/additive).
- Nothing programmatic consumes `meta.yaml` today except the gate's F check. `pairs_with` is currently decorative (no validator here, no consumer there).
- Sibling `pm-skills-mcp` repo exists (MCP wrapper pattern for AG-2).
- prd meta `related_templates: [user-stories, acceptance-criteria, release-notes, solution-brief]`: `solution-brief` has no bundle (dangling forward reference; a `develop-solution-brief` skill exists in pm-skills).

## 8. Plan-vs-actual gap map (seeds Dimension G)

Planned = implementation plan G4 (created 2026-06-29). Actual = tree as of 2026-07-10 (commit 737354e).

| Phase | Planned | Actual | Evidence | Character |
|---|---|---|---|---|
| P1 four ADRs | `docs/internal/decisions/2026*.md` x4, status accepted, BLOCKING gate before P2-P4 | No ADR files anywhere. Decisions themselves WERE made 2026-06-29, recorded inline in G3 section 5 and G4 lines 374-381 | plan lines 75-109; `git ls-files` | Decided content, undocumented format: the plan's own blocking gate ("All four decisions must be accepted before P2-P4 start") was satisfied in substance, violated in form |
| P2 scaffold | root `templates/`, `_families/`, `docs/`, `scripts/`, `.github/workflows/`, `.claude-plugin/`, `profiles/`, plus README/AGENTS/LICENSE/CONTRIBUTING/CHANGELOG/etc. | None of it. Content lives under `_local/`; root has only README + .gitignore | plan lines 121-136; ls-files | Location documented as deliberate (.gitignore, README "provisional"); the missing root files (LICENSE etc.) are silent drift |
| P3 CI gate | 7 Node `.mjs` scripts + `known-skill-ids.txt` + `ci.yml` on push/PR | One Python script `_local/tools/check-bundles.py`, local-only, covering parts of 5 of the 7 planned checks; no CI | plan lines 168-196; check-bundles.py | Deviation self-documented as "local prototype"; CI absence is open risk |
| P4 reference bundle | `templates/deliver-prd/` with 6 files (`template.lean.md`, `template.full.md`, `example.md`, `guide.md`, `template.meta.yaml`, `HISTORY.md`) | `_local/templates/prd/` with **8** files, `<type>_` filename prefixes, plus companion + research-log the plan never specified | plan lines 210-236; tree | Built beyond plan; naming and anatomy follow methodology G1 (v0.2.0), which evolved past plan/spec. No decision record for the rename (deliver-prd to prd) or the 6-to-8-file growth other than the methodology itself |
| P5 distribution + v0.1 | generate-catalog, count-consistency, marketplace entries, install test (resolves D2), CHANGELOG, tag v0.1.0 | Nothing | plan lines 244-283; section 6 above | Not started; D2 still open |
| P6 family + contract + validator + v0.2 | family contract file `_families/delivery-docs.contract.md`, 3 more bundles, `validate-template-family.mjs`, tag v0.2.0 | 3 more bundles built (content complete); **no family contract file, no family validator, no tag** | plan lines 287-323 | Content half done ahead of rails; contract exists only tacitly (shared conventions in methodology) |
| P7 roadmap governance | roadmap.md (tiers), pull-queue.md, alias-index.json, generator-gate ADR | None. Atlas (CT-3) partially serves the scoping intent | plan lines 331-363 | Not started |

**Order actually followed:** content first (P4+P6 bundles, methodology, enrichment 2026-06-30), then durability (HY-1 version control 2026-07-02), then map (atlas), then front door (README), then gate prototype (2026-07-03). Infrastructure phases P1/P2/P3/P5/P7 remain unbuilt. The G6 brief (2026-07-02) post-hoc acknowledges and re-sequences some of this but does not ratify the P1-P3 skip as a decision.
**The plan's own progress table (G4 lines 38-48) was never updated and still reads "Not started" for all seven phases, despite naming itself the source of truth for progress.**

## 9. Open decisions ledger (age as of 2026-07-10)

| ID | Decision | Where | Open since | Age | Stated resolution cost |
|---|---|---|---|---|---|
| D1 | Build Layer 1 generator or not | G4/G5 | 2026-06-29 | 11 days | gated on real usage (correctly deferred) |
| D2 | Does `skills` CLI install a template-only repo | G4/G2 section 17.3 | 2026-06-29 | 11 days | G3 section 7 calls it "a 30-minute test" |
| D3 | agentskills.io non-skill resource type | G4 | 2026-06-29 | 11 days | "reading the current spec" (~1 hour) |
| D4 | Regulated tier appetite | G4 | 2026-06-29 | 11 days | a decision, not a build |
| HY-2 | Final scaffold (does `_local/` graduate to `templates/`) | G6 | 2026-07-02 | 8 days | "low effort"; blocks P2 |
| VL-1 | Business model (open-core vs pure funnel) | G6 | 2026-07-02 | 8 days | a decision |
| G6 asks 1,3,5 | primary user; evals timing; 28-cap confirm | G6 section 7 | 2026-07-02 | 8 days | decisions |

## 10. Citation-audit sampling strategy (Dimension A)

The four companions carry 37 reference entries total (prd 13, user-stories 9, acceptance-criteria 8, release-notes 7). This is small enough for a **full census of all 37 entries** (format, tier tag, anchor, inline usage). Live-fetch a subset of at least 16 URLs (4+ per bundle), prioritizing: (a) standards-body/normative claims, (b) sources the session log G10 flagged as not directly fetched (SVPG/Cagan, Lenny's Newsletter, Scrum.org), (c) any entry whose claim is quantitative. Also spot-check claim-to-research-log traceability (DoD Research clause) for at least 3 claims per bundle.

## 11. Leads noted by the lead auditor (verify independently; do not copy as findings without your own evidence)

1. methodology.md:41 "seven files" vs 8-file reality (README.md:46-58, gate ROLES).
2. Gate citation check is one-directional; prd has 2 never-cited reference entries ("no padded entries" DoD clause unchecked).
3. No LICENSE file despite Apache-2.0 declarations (README.md:116, meta files).
4. Plan progress table stale at "Not started" x7 (G4:38-48) while calling itself source of truth.
5. `{{maintainer}}` / `{{owner}}` unfilled placeholders in shipped meta.yaml and governance-doc frontmatter (machine consumers get a placeholder token).
6. `related_templates: solution-brief` dangles (prd_meta.yaml:15).
7. `_working/` folder instructs its own deletion post-decision; decision made; folder remains.
8. No JSON Schema or equivalent for meta.yaml; gate F is a regex, not schema validation.
9. Family `delivery-docs` declared in 4 metas; no family contract file; plan AC-12 requires one plus CI enforcement.
10. README.md:27 "All four bundles are researched, enriched, cross-linked, and verified" while all four metas say `status: beta` and methodology/design-spec/plan are all `status: draft`. Assess whether statuses are coherent.
11. Nesting gate checks H2 text only; re-derive with H3s and semantic comparison.
12. All examples one domain (Saved Views B2B SaaS); documented CT-1; judge as validity limit, not news.
13. No efficacy evals; pm-skills has `evals/` per skill (portability reference).
14. Zero real usage cycles; catalog Recommendation 1 sets "survives one real usage cycle" as the Tier-2 gate.
