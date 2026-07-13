# Audit Report: product-lifecycle-templates

- **Date:** 2026-07-10
- **Auditor:** lead auditor (Claude Fable 5) orchestrating 7 dimension auditors and 19 adversarial verifiers (26 agents total; method in the Appendix)
- **Scope:** the full repository at commit `737354e` (feat(gate): add check-bundles.py governance gate), judged against its own governance corpus first and external best practice second
- **Bar applied:** the repo's own stated bar: "the indisputable best-in-class reference implementation of a template library, not a folder of templates" (README.md:7)
- **Location note:** the audit commission's default output location (repo root) was overridden by the requester's directive to write all results to `_local/audit/2026-07-10_fable-audit/`. Companion files: [00_context-sheet.md](00_context-sheet.md) (Phase 0 fingerprint), [findings/raw-results.json](findings/raw-results.json) (all agent output), [findings/digest.md](findings/digest.md) (merged digest).

---

## 1. Executive summary

Overall: **B-** against the repo's own bar. The craft is real; the product around the craft is not yet built.
Dimension grades: A research integrity **B**; B bundle contract **B**; C agent-native readiness **C**; D governance automation **C**; E distribution and sustainability **D**; F documentation and onboarding **C**; G strategy coherence **B**.
49 findings (1 Critical, 15 High, 24 Medium, 9 Low after verification); every High/Critical finding was adversarially verified: 16 confirmed, 3 downgraded, 0 refuted.
The finding that matters most is E-01 (missing LICENSE file): Apache-2.0 is declared in the README and every meta.yaml but granted nowhere, so every consumer copy of a copy-and-fill product is technically unlicensed; the fix takes five minutes.
Second: G-02 (governed claim outruns reality): the front door says "enforceable, not aspirational" and the design spec says "CI-enforced" while enforcement is a hand-run local prototype covering roughly half the Definition of Done, with no CI and no push protection.
Third: D-05 (zero real usage): no template has ever been filled by anyone but its author, and no current plan phase produces the first real user that the catalog's own tier gate ("survives one real usage cycle") requires.
The single highest-leverage improvement is a one-day credibility-floor sprint: LICENSE, a ci.yml that runs the existing gate on push, a v0.1.0 tag plus CHANGELOG, a truth-up of the stale plan table, and seven ADR transcriptions; it converts "governed" from claim to fact using assets that already exist.
The central claim (governed, best-in-class, agent-native reference implementation) is **partially true**.
Earned: researched, dual-reader, nesting-disciplined, provenance-stamped content that the repo's named competitors (curated awesome-lists) do not attempt. On credit: "governed" (local, partial, un-wired), "agent-native" (no machine consumption path exists), and "reference implementation" (unlicensed, untagged, 4 of 205 types, living in a directory named provisional).
The strategy corpus already knows most of this (the raising-the-ceiling brief admits "best-in-class is asserted, not proven"); the audit's core verdict is that execution of the cheap credibility work has lagged the quality of the thinking by exactly eleven days.

---

## 2. Corpus fingerprint (Phase 0)

Condensed from the full context sheet at [00_context-sheet.md](00_context-sheet.md), which every audit agent read before working.

### 2.1 Identity and inventory

- Remote `https://github.com/product-on-purpose/product-lifecycle-templates.git`, branch `main`, in sync. 5 commits (2026-06-29 to 2026-07-03), single contributor, **zero git tags**, no CHANGELOG, **no LICENSE file**.
- 51 tracked files (~800 KB); 1 untracked (`_local/2026-07-10_overview.md`, a same-day synthesis; treated as secondary, not governance).
- All substance lives under `_local/` (documented as deliberate: `.gitignore:1-8`, README.md:69 "a provisional home").

### 2.2 Governance corpus (the internal contract)

| ID | Document | Version / status | Role |
|---|---|---|---|
| G1 | `_local/templates/methodology.md` | v0.2.0, draft | THE operative rulebook: bundle contract, research protocol, citation standard (sec. 6), companion skeleton (sec. 5), guidance comment standard (B1), 11-clause Definition of Done (sec. 7) |
| G2 | `_local/initial-discovery/docs/template-library-design-spec.md` | v0.1.0, draft | Original formal spec; partially superseded (S/M/L naming, `pm-templates` name, 6-file bundle) with no superseded banner |
| G3 | `_local/initial-discovery/docs/strategy-brief_catalog-to-template-library.md` | v0.1.0, draft | Approach A; the four foundational decisions recorded as inline "[Resolved 2026-06-29]" amendments (sec. 5) |
| G4 | `_local/initial-discovery/docs/implementation-plan_catalog-to-template-library.md` | TL-01, draft | 7 phases P1-P7, AC-1..AC-14, open decisions D1-D4; its progress table (lines 38-48) still reads "Not started" for all seven phases while calling itself "the source of truth for progress" |
| G5 | `_local/initial-discovery/docs/template-system-layered-design.md` | v0.1.0, draft | 3-layer model, the bright line, generator decision gate; declares `pairs_with` "human-facing, not load-bearing" (sec. 8) |
| G6 | `_local/initial-discovery/docs/strategy-brief_raising-the-ceiling_2026-07-02.md` | v0.1.0, draft | Newest strategy layer: EV/LP/AG/CT/FR/VS/VL/HY idea set, prioritization, recommended sequence |
| G7 | `_local/initial-discovery/docs/deep-research_master-catalog.md` | n/a | 205 types, 19 groups, must-have 28, Recommendations 1-6; the scope document |
| G8-G10 | research prompt; `_working/README.md` (guidance-style experiment, says "delete me", still present); session log 2026-06-30 | n/a | Provenance and build records |

**ADR files: none exist.** Decisions live inline in G3 section 5, G4 lines 374-381, the `.gitignore` header, the gate docstring, and the methodology itself.

### 2.3 Bundles, catalog, automation, distribution, seams

- **Bundles:** 4 (`prd`, `user-stories`, `acceptance-criteria`, `release-notes`), each 8 files, `family: delivery-docs`, `status: beta`, `template_version: 0.1.0`, `sizes_available: [lean, full]`. Examples chain on one fictional "Saved Views" B2B SaaS feature (documented limitation, CT-1 in G6).
- **Catalog:** 4 of 205 types built (4 of the must-have 28). Atlas (`_local/atlas/atlas.html`) renders all 205. No root `catalog.md`/`manifest.json`, no roadmap/pull-queue/alias-index (P5/P7 not started).
- **Automation:** one gate, `_local/tools/check-bundles.py` (Python, local-only, 6 checks A-F), self-documented as a "local prototype" of the planned P3 CI gate. Run 2026-07-10 by the lead auditor and re-run by verifiers: exit 0, all four bundles pass. No `.github/workflows/`. Nothing else is automated.
- **Distribution surfaces:** none exist (no plugin manifest, marketplace metadata, root catalog/manifest, MCP server, tags, CHANGELOG, CONTRIBUTING, AGENTS.md, LICENSE). The only acquisition path is `git clone`.
- **Ecosystem seams:** sibling `pm-skills` is real and mature; all four `pairs_with` targets resolve to real skill directories and `skill-manifest.json` entries. Nothing consumes `pairs_with` programmatically (documented as intentional in G5 sec. 8). `related_templates` contains two dangling entries (`solution-brief`, `launch-checklist`). `pm-skills` has a per-skill `evals/` harness this repo lacks.

### 2.4 Plan-vs-actual gap map

| Phase | Planned (G4, 2026-06-29) | Actual (2026-07-10) | Character |
|---|---|---|---|
| P1 four ADRs | `docs/decisions/` x4, **blocking** gate before P2-P4 | No ADR files anywhere; decisions made 2026-06-29 and recorded inline (G3 sec. 5, G4:374-381) | Decided in substance, undocumented in the mandated durable format; G4:381 falsely claims "recorded as ADRs in P1" |
| P2 scaffold | Root `templates/`, `_families/`, `docs/`, `scripts/`, `.github/`, `.claude-plugin/`, `profiles/`, plus LICENSE/AGENTS/CONTRIBUTING/CHANGELOG | None of it; content lives under `_local/` | Location documented as deliberate; the missing root files (LICENSE above all) are silent drift |
| P3 CI gate | 7 Node `.mjs` scripts + `ci.yml` on push/PR | One local Python script covering parts of 5-6 planned checks; no CI | Deviation self-documented as interim prototype; CI absence is live risk |
| P4 reference bundle | `templates/deliver-prd/`, 6 files | `_local/templates/prd/`, **8** files (companion + research log added), `<type>_` naming | Built beyond plan per methodology v0.2.0; the rename and 6-to-8 growth have no decision record other than the methodology itself |
| P5 distribution + v0.1 | catalog/manifest generation, marketplace, install test (D2), CHANGELOG, tag | Nothing | Not started; D2 open 11 days |
| P6 family + contract + validator + v0.2 | Contract file, 3 bundles, family validator, tag | 3 bundles built; **no contract file, no validator, no tag** | Content half of the phase done ahead of its rails |
| P7 roadmap governance | roadmap.md, pull-queue.md, alias-index.json, generator-gate ADR | None; atlas partially serves the scoping intent | Not started |

**Order actually followed:** content first (bundles + methodology, 2026-06-30), then durability (version control, 2026-07-02), map (atlas), front door (README), gate prototype (2026-07-03). The plan's own progress table was never updated.

### 2.5 Open decisions ledger (age at audit date)

| ID | Decision | Open since | Age | Stated cost to resolve |
|---|---|---|---|---|
| D1 (generator) | Build Layer 1 or not | 2026-06-29 | 11 d | Correctly gated on real usage |
| D2 (CLI install) | Does the skills CLI install a template-only repo | 2026-06-29 | 11 d | "a 30-minute test" (G3 sec. 7) |
| D3 (spec type) | agentskills.io resource type | 2026-06-29 | 11 d | ~1 hour spec read |
| D4 (regulated tier) | Tier 3 appetite | 2026-06-29 | 11 d | A decision |
| HY-2 (scaffold) | Does `_local/` graduate to `templates/` | 2026-07-02 | 8 d | Low; blocks P2 |
| VL-1 (business model) | Open-core vs pure funnel | 2026-07-02 | 8 d | A decision; G6 says decide before distribution |

### 2.6 Citation sampling strategy (as executed)

The four companions carry 37 reference entries (prd 13, user-stories 9, acceptance-criteria 8, release-notes 7): small enough for a **full census of all 37** (numbering, tier tags, anchors, hyperlinks, inline usage), which was performed. Live fetches prioritized standards-body and normative claims, sources the session log flagged as not directly fetched (SVPG, Lenny's Newsletter, Scrum.org), and quantitative claims; fetch results for finding-bearing URLs are recorded in section 8. Claim-to-research-log tracing was spot-checked per bundle. No silent truncation occurred.

---

## 3. Prioritized findings table

Priority score = (severity x reach x confidence) / effort, with severity Critical=4 / High=3 / Medium=2 / Low=1, reach 1-5 (5 = whole library or every consumer), confidence 0-1, effort S=1 / M=2 / L=3. Severities are **post-verification** (downgrades applied). Verification: CONF = CONFIRMED by an adversarial verifier, DOWN = confirmed but downgraded, "-" = below the High/Critical verification threshold. Findings marked "= X-nn" were independently discovered by multiple dimensions and are detailed once under the canonical ID.

| Score | ID | Dim | Sev | Verif | Eff | Title | Primary evidence | Fix (short) |
|---|---|---|---|---|---|---|---|---|
| 20.00 | E-01 | E | Critical | CONF | S | LICENSE file absent; Apache-2.0 declared but never granted | README.md:116; `git ls-files` | Copy pm-skills/LICENSE to root |
| 14.25 | F-01 | F | High | CONF | S | No consumer quickstart; beginner path breaks before first fill | README.md:21,25-40 | Add quickstart section / doc |
| 12.45 | G-02 | G | High | CONF | S | "Governed / CI-enforced" claim outruns local prototype | README.md:100; design spec:54 | Wire CI + soften wording |
| 11.88 | D-05 | D | High | CONF | S | Zero real usage cycles; no path to first user in any plan | catalog G7:289; G6:57-58 | One real fill + EV-3 form |
| 11.64 | B-02 | B | High | CONF | S | No JSON Schema for meta.yaml; `{{maintainer}}` ships in all 4 | check-bundles.py:146-173; prd_meta.yaml:18 | Add meta.schema.json + gate check |
| 10.80 | G-01 | G | High | CONF | S | Plan stale and self-contradictory: "Not started" x7 as source of truth | plan G4:38-48,98 | Truth-up table + ratify deviation |
| 9.90 | C-05 | C | Medium | - | S | `{{maintainer}}` placeholder breaks meta as machine artifact (= B-02) | all 4 meta.yaml:18 | Fill values; extend gate check D |
| 9.80 | D-03 | D | Medium | - | S | No CI push enforcement; solo discipline is the only protection | plan G4:179; no .github/ | 10-minute ci.yml bridge |
| 9.70 | C-03 | C | Medium | - | S | No machine catalog; agent must glob + parse 4 schemaless YAMLs | plan G4:244-283 | Generate root manifest.json |
| 9.30 | C-06 | C | Medium | - | S | No token/size metadata; agents cannot budget context | prd_meta.yaml:1-20 | Add approx_tokens map |
| 9.20 | C-04 | C | Medium | - | S | Size selection non-deterministic from meta (3 of 3 intents failed on size) | meta sizes_available fields | Add sizing_guidance + default_size |
| 8.73 | A-02 | A | High | CONF | S | Three SVPG refs claim "(accessed 2026-06-30)" for 403-blocked pages | prd_companion.md:171-175; research log:12,27 | Add retrieval qualifiers + convention |
| 8.00 | E-07 | E | Medium | - | S | template_version 0.1.0 has no tag or CHANGELOG anchor | prd_meta.yaml:12; `git tag` empty | CHANGELOG + v0.1.0 tag |
| 7.92 | C-07 | C | Medium | - | S | Methodology says seven files, contract is eight (= B-04) | methodology.md:41; gate ROLES | Fix methodology sec. 2 |
| 7.92 | D-02 | D | Medium | - | S | Citation gate one-directional; padded entries pass (false negative demonstrated) | check-bundles.py:126-143 | 2-line reverse check |
| 7.50 | E-02 | E | High | CONF | M | All planned distribution surfaces absent | design spec:265-273; plan:129-136 | One-day P2 skeleton sprint |
| 7.35 | C-01 | C | High | CONF | M | No machine path from blank template to validated filled doc (LP-1 unbuilt) | G6:58; template preambles | Thin fill flow reusing ASK lines |
| 7.27 | D-01 | D | High | CONF | M | Gate covers ~half of DoD; 9 of 14 plan ACs have zero automation | methodology.md:189-203; gate:17-23 | Add 3 cheap checks + honest wording |
| 7.12 | D-04 | D | High | CONF | M | No efficacy evals; best-in-class asserted, not measured | G6:39-41; pm-skills evals harness | Port EV-1 from pm-skills |
| 6.80 | E-03 | E | Medium | DOWN | S | Skills-CLI channel untested; D2 (30-min test) open 11 days | plan:376-377; code.claude.com docs | Run the test this week |
| 6.38 | E-04 | E | High | CONF | M | Maintainer math does not close at Tier 1 (224 files, ~259 citations, solo) | G6:98,158; catalog:289 | VL-3 cadence + pull queue + CONTRIBUTING |
| 6.38 | G-03 | G | High | CONF | M | Roadmap prioritizes proving/reach while credibility floor is missing | G6:139 vs G6:157 | Floor first, then wedge, then evals/MCP |
| 5.94 | B-04 | B | Medium | - | S | Methodology "seven files" vs 8-file reality (canonical; = C-07, F-04) | methodology.md:41,107 | One-line + table-row fix |
| 5.94 | F-03 | F | High | CONF | M | Four mandated ADR files missing; decisions are undiscoverable prose (= G-06) | plan:81-109,381; G3:139-142 | Write 7 ADRs (MADR) |
| 5.94 | F-04 | F | Medium | - | S | Duplicate of B-04 (methodology internal inconsistency) | methodology.md:41 | See B-04 |
| 5.88 | B-01 | B | High | CONF | M | Family contract file absent; AC-12 violated; family is a bare label | plan:69,295; design spec:248 | Author delivery-docs contract |
| 5.82 | F-05 | F | Medium | - | S | README "complete/verified" vs `status: beta` everywhere | README.md:27; prd_meta.yaml:12 | Reconcile status language |
| 5.58 | A-01 | A | High | CONF | S | Ranorex citation resolves but does not support its claim (cited 4-5x) | ac_companion.md:96,122,202 | Replace source or label judgment |
| 5.40 | E-05 | E | Medium | - | S | No decision triage; cheap decisions age without process | plan:374-381; G6:119-121 | Decision-aging rule (2h/3d) |
| 4.85 | C-02 | C | Low | DOWN | S | pairs_with decorative (documented as intended); residual = dangling related_templates (= B-05) | G5 sec. 8; prd_meta.yaml:15 | See B-05 |
| 4.50 | C-08 | C | Low | - | S | No fill provenance fields (filled_by, fill_date, fill_method) | template frontmatter | Add 2 placeholder fields |
| 4.32 | G-04 | G | Medium | - | S | Roadmap anchored to bypassed plan spine; design spec teaches superseded model | G6:120; design spec:14 | Re-base + superseded banner |
| 3.96 | B-05 | B | Medium | - | S | Dangling related_templates: solution-brief, launch-checklist (canonical) | prd_meta.yaml:15; rn_meta.yaml:15 | Remove or mark `future:` |
| 3.96 | C-09 | C | Low | - | S | Guidance strip is manual; no strip script exists | template preambles; _local/tools/ | 20-line strip-template.py |
| 3.88 | A-04 | A | Medium | - | S | Two padded PRD reference entries; ref-12 tier tag inflated (= B-03) | prd_companion.md:183,191 | Cite, remove, or retag |
| 3.88 | F-02 | F | Medium | DOWN | M | No docs/ reference tree; authoring contract has no single home | README.md:67-83; design spec:148-173 | authoring-contract.md index |
| 3.80 | A-03 | A | Medium | - | S | Keep a Changelog cited as "current 1.1.0"; 1.1.2 shipped 2024-09 | rn_companion.md:38,212 | Correct version + staleness DoD step |
| 3.80 | F-06 | F | Medium | - | M | Consumer and contributor journeys interleaved in README | README.md:21,67-116 | Split README / CONTRIBUTING.md |
| 3.28 | A-05 | A | Medium | - | S | Direct quote attributed to paywalled Lenny post never read | prd_companion.md:48,181 | De-quote to paraphrase or verify |
| 3.12 | G-05 | G | Medium | - | M | Sustainability risks named but unowned (bus factor, rot, cadence) | G6:84,104,108 | Decide VL-3 + link-check in CI |
| 2.70 | E-06 | E | Medium | - | M | _local/ graduation uncharted: 14+ path refs, global-gitignore hazard | .gitignore:1-5; gate:31 | Decide HY-2 + migration checklist |
| 2.40 | G-06 | G | Medium | - | M | Duplicate of F-03 (decisions never recorded in mandated ADR format) | plan:92,381 | See F-03 |
| 1.98 | B-03 | B | Medium | - | S | Duplicate of A-04 / D-02 (padded entries + one-way gate) | prd_companion.md:183,191 | See A-04, D-02 |
| 1.80 | F-07 | F | Low | - | S | "IDs carry a handle" convention violated in own governance docs | README.md:111; plan:381; gate:8 | Sweep bare P1/P3 refs |
| 1.76 | A-06 | A | Low | - | S | Four refs deviate from one-source-per-entry format | ac_companion.md:194; rn_companion.md:222 | Split entries; book/pre-web rules |
| 1.50 | D-06 | D | Low | - | S | Nesting gate checks H2 text only (no current false negative) | check-bundles.py:35 | Extend regex to (level, text) |
| 0.95 | B-06 | B | Low | - | S | "NFRs" prose pointer does not match companion label | prd_template-full.md:166 | Spell out the label |
| 0.95 | B-08 | B | Low | - | S | _working/ folder ignores its own deletion instruction | _working/README.md:6 | Delete the folder |
| 0.92 | B-07 | B | Low | - | S | Open-questions table comment lacks labeled ROW HINT | prd_template-lean.md:128-136 | Add ROW HINT field |

---

## 4. Detailed findings

Organized by dimension. Every High/Critical finding below survived an independent adversarial verification pass (re-read of cited lines, re-run of commands, re-fetch of URLs, and a check for governance-permitted deviations). Where a verifier corrected a detail, the correction is stated. Duplicates are consolidated under their canonical ID.

### Dimension A: Content quality and research integrity (grade B)

**Where credibility is already earned.** The research is genuine, not theater: all four research logs exist and honestly distinguish "fetched, verified" from "search excerpt" from "search-corroborated," naming the SVPG 403s, the Lenny paywall, and the Scrum.org empty render explicitly. The primary-tier anchors were live-verified during this audit and support their claims: the Scrum Guide's three-artifacts claim, Keep a Changelog's six change types and anti-git-log principle, SemVer semantics, Conventional Commits mapping, and the Working Backwards PR/FAQ sequencing all check out. 35 of 37 reference entries are cited inline (94.6 percent). Every illustrative figure in all four examples carries an explicit "(illustrative)" label; no fabricated metrics are presented as real. The cross-bundle "Saved Views" example chain is coherent where it matters: identical personas, the same 1-second p95 and WCAG 2.2 AA thresholds in PRD and acceptance criteria, and open questions that flow between documents. Debate sections present real contested terrain with named camps rather than false consensus. Writing quality sampled against the Google developer documentation style guide produced no finding.

**A-01 (Ranorex citation does not support its claim). High, CONFIRMED, effort S.**
What: the acceptance-criteria companion attributes its central form-selection guidance ("some teams default to checklists, others to Given/When/Then"; "default to the checklist; reach for scenarios when...") to a Ranorex article four to five times (`acceptance-criteria_companion.md:24,62,96,122,124`; entry at line 202). The live fetch confirmed the article implements GWT and promotes Ranorex tooling; it never compares checklists to scenarios and never discusses form selection. The research log compounds it by logging the source's claimed support incorrectly.
Why it matters: a citation that resolves but does not support its claim is worse than a dead link; it fails methodology A4 ("never paraphrase a source into a stronger claim than it makes") and A2 (vendor claims must be corroborated) at the companion's most instructive point.
Fix: replace with a source that actually makes the comparison (Gojko Adzic's BDD writing or Cucumber documentation), keep Ranorex only for Gherkin-keyword claims, or label the guidance author judgment per methodology principle 2.
External grounding: https://www.ranorex.com/blog/given-when-then-tests/ (resolved; content verified twice, by auditor and verifier).

**A-02 (SVPG references claim access dates for 403-blocked pages). High, CONFIRMED, effort S.**
What: three PRD companion entries (`prd_companion.md:171,173,175`) carry "(accessed 2026-06-30)" while the research log (`prd_research-log.md:12,27`) records that svpg.com returned HTTP 403 and substance came from search excerpts. The verifier re-fetched all three URLs on 2026-07-10: still 403, so the condition is persistent.
Why it matters: "(accessed DATE)" conventionally asserts successful retrieval. The research log is honest; the reader-facing companion contradicts that honesty on the three most-cited entries anchoring the library's central PRD-vs-prototype debate. For a "researched, not remembered" library this is a material integrity gap, and methodology section 6 currently has no convention for blocked or paywalled sources (the words 403, paywall, and search excerpt appear nowhere in it).
Fix: one line per entry, e.g. "(accessed 2026-06-30 via search excerpt; direct fetch blocked, HTTP 403)", plus a methodology section 6 convention so future bundles handle this uniformly.

**A-03 (stale Keep a Changelog version claim). Medium, effort S.** `release-notes_companion.md:38` asserts "The current version is 1.1.0"; keepachangelog.com shows 1.1.1 (2023-03) and 1.1.2 (2024-09) both predating the June 2026 research date, and the reference URL is pinned to `/en/1.1.0/`. Fix the text and URL; add a DoD staleness question ("is the cited version of every versioned standard still current?"). This is the concrete case for the FR-1 staleness gate (lychee-based link and version checking).

**A-04 (padded entries and an inflated tier tag; canonical for B-03). Medium, effort S.** PRD refs 8 and 11 to 13: entries [8] (Atlassian Confluence template, `prd_companion.md:183`) and [12] (Hustle Badger, `prd_companion.md:191`) are never cited inline anywhere in the body (grep-verified zero occurrences), violating the DoD "no padded entries" clause (methodology.md:200). Ref-12 is also tagged [practitioner], a credibility inflation for a content-marketing site the methodology's own tier definitions would tag [vendor]. Fix: cite or remove; retag; and see D-02 for the gate extension that would have caught it.

**A-05 (unverifiable direct quote from a paywalled source). Medium, effort S.** `prd_companion.md:48` quotes "the single most important step in solving any problem" against a Lenny's Newsletter post whose body is paywalled and was never read (research log:17 admits only the public summary was used). Under methodology A4 ("quote sparingly and exactly"), either verify with subscriber access or drop the quotation marks and log it as paraphrase-from-excerpt.

**A-06 (reference format deviations). Low, effort S.** Two entries combine two distinct sources under one number (`acceptance-criteria_companion.md:194` Jeffries+Cohn; `release-notes_companion.md:222` Appcues+AnnounceKit), and book/pre-web sources have no format rule. Split the combined entries; add a methodology paragraph for print books and pre-web practices.

### Dimension B: Bundle contract and structural governance (grade B)

**Where credibility is already earned.** The invariants were re-derived independently, not trusted: all four bundles pass H2 ordered-subset nesting (prd 7-in-17, user-stories 3-in-7, acceptance-criteria 3-in-6, release-notes 4-in-11); no H3 headings exist to drift; no same-heading-different-intent case was found. All 68 guidance comment blocks across the 8 variant files carry all six required fields (WHAT/WHY/ASK/GOOD/WEAK/TRAP) plus preambles. All four companions contain all 11 skeleton sections. Every guide has six named anti-patterns, three times the DoD minimum. Repo-wide link integrity is clean: 69 relative links and 24 anchors checked, zero genuinely broken. Prose deep-pointers resolve correctly in three of four bundles (one label mismatch). Histories are compliant. This is the hardest layer to fake, and it holds.

**B-01 (family contract file absent). High, CONFIRMED, effort M.**
What: all four metas declare `family: delivery-docs`; `_families/delivery-docs.contract.md` and the `_families/` directory do not exist (Glob-verified), and no validator enforces family conformance. Plan AC-12 (G4:69) requires both; design spec section 11 (line 248) specifies the contract's contents; the plan even names the pm-skills model file to copy (G4:295).
Why it matters: the family is currently a label with no reviewable definition; conformance rests on shared prose conventions that weaken with every bundle added. The verifier confirmed no governance document ratifies the absence.
Fix: author the contract per design spec section 11 (membership criteria, required meta fields and allowed values, nesting rule, companion skeleton, guidance standard), modeled on `pm-skills` meeting-skills contract, then add a family check to the gate.

**B-02 (no schema for bundle metadata; canonical for C-05). High, CONFIRMED, effort S.**
What: no JSON Schema or equivalent exists anywhere in the repo; gate check F is a regex over `sizes_available` only. Three fields shipped in all four metas are undeclared in the methodology B5 field list (`aliases`, `catalog_ref`, `maintainer`); methodology and design spec section 9.1 conflict on `maintainer`; and every meta ships `maintainer: "{{maintainer}}"`, a literal placeholder any YAML consumer receives as a string (the methodology's own frontmatter has `owner: "{{owner}}"`). No check catches any of this; the gate passes.
Why it matters: metadata contracts enforced by convention rot silently; this one has already drifted twice (undeclared fields, unfilled placeholder) in a four-bundle library that plans 28.
Fix: commit a schema and validate it in the gate; fill the placeholders. Ready-to-commit stub (`_local/tools/meta.schema.json`):

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "BundleMeta",
  "type": "object",
  "required": ["id", "title", "summary", "doc_type", "phase", "family",
               "sizes_available", "methodology", "pairs_with", "status",
               "template_version", "tags", "related_templates",
               "last_reviewed", "license"],
  "properties": {
    "id": { "type": "string", "pattern": "^[a-z0-9-]+$" },
    "title": { "type": "string" },
    "summary": { "type": "string", "maxLength": 300 },
    "doc_type": { "type": "string" },
    "phase": { "enum": ["discover", "define", "develop", "deliver",
                         "measure", "iterate", "foundation", "tool"] },
    "family": { "enum": ["delivery-docs"] },
    "sizes_available": { "type": "array",
                          "items": { "enum": ["lean", "full", "s", "m", "l"] } },
    "pairs_with": { "type": ["array", "null"], "items": { "type": "string" } },
    "status": { "enum": ["beta", "stable", "deprecated"] },
    "template_version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "aliases": { "type": "array", "items": { "type": "string" } },
    "catalog_ref": { "type": "integer" },
    "maintainer": { "type": "string", "not": { "pattern": "\\{\\{" } },
    "license": { "const": "Apache-2.0" }
  },
  "additionalProperties": false
}
```

**B-04 (methodology says seven files; the contract is eight; canonical for C-07 and F-04). Medium, effort S.**
What: `methodology.md:41` ("containing seven files") and its section 2 table omit the research log; `methodology.md:107` repeats "seven" in the drafting protocol. The gate ROLES list (`check-bundles.py:41-50`), the README anatomy table (README.md:46-58), and the DoD's own Research clause all require eight. Three dimensions (B, C, F) found this independently, which is itself a signal: an author or agent following the rulebook exclusively would build a 7-file bundle that fails gate check A.
Fix: change both "seven" occurrences to "eight", add the research-log row to the section 2 table, and add a drafting step for it (B6 or an explicit pointer to A6).

**B-05 (dangling related_templates; canonical for the surviving residue of C-02). Medium, effort S.** `prd_meta.yaml:15` lists `solution-brief` and `release-notes_meta.yaml:15` lists `launch-checklist`; neither bundle exists (skills of similar names do, in pm-skills). Machine consumers follow these to dead ends. Remove, or mark with a `future:` convention, and add a gate resolver against the actual bundle list. (The broader C-02 claim that `pairs_with` being unconsumed is a High defect was **refuted in substance** by verification: layered design G5 section 8 documents `pairs_with` as "human-facing, not load-bearing," so the decorative seam is a decided design posture, not drift. The dangling entries are the real residue.)

**B-06, B-07, B-08 (polish). Low, effort S each.** A prose pointer says "Anatomy > NFRs" where the companion's label is "Non-functional requirements (full)" (`prd_template-full.md:166`); the PRD open-questions table comment lacks a labeled ROW HINT (`prd_template-lean.md:128-136` and full counterpart; methodology.md:121 requires it for tables); and `_working/` still exists although its own README line 6 orders its deletion once the guidance-style decision (made; Approach A) landed.

### Dimension C: Agent-native readiness (grade C)

**Where credibility is already earned.** The architecture beneath the claim is real: all four `pairs_with` values resolve to real skills and manifest entries; provenance (`source_template`, `source_template_version`) is stamped consistently in all variants and examples; lean variants (roughly 1,000 to 1,800 tokens) genuinely fit alongside a drafting task in any production context window; `{{snake_case}}` placeholders are uniform and machine-findable; the WHAT/ASK comment fields already constitute a latent per-section interview script; `catalog_ref` integers were verified correct against the master catalog (29, 30, 38, 115); and in the selection simulation, all three test intents resolved to the correct **bundle** deterministically from `aliases` and `summary` alone.

**C-01 (no machine fill-and-validate path). High, CONFIRMED, effort M.**
What: there is no MCP server, CLI, skill, or interview flow; the only path from blank template to document is a human reading HTML comments and hand-deleting them (`prd_template-lean.md:22-28`). G6:58 calls LP-1 "the single most important unshipped thing"; the gate's check D validates only the authored example, not user fills.
Why it matters: README line 3 and the design spec's agent-native pillar are written in the present tense while no agent can consume the library today. The gap is documented (not drift), but the marketing tense is not.
Fix: build the minimum viable loop as a thin skill or CLI: select via meta, interview via the ASK lines (regex-extractable), fill placeholders, stamp provenance and fill date, strip comments, run the placeholder check. Benchmarked against Anthropic's tool-writing guidance (fetched: tool consolidation, context efficiency), a single "fill this template" operation beats exposing raw file reads.
External grounding: https://www.anthropic.com/engineering/writing-tools-for-agents (resolved).

**C-03 (no machine catalog). Medium, effort S.** An agent must glob directories, construct filenames, read four YAMLs, and parse them with no schema; `manifest.json` is planned (P5) but absent. One generated root manifest plus the B-02 schema cuts enumeration to a single read. **C-04 (size selection non-deterministic). Medium, effort S.** Bundle selection succeeded 3 of 3 but size selection failed 3 of 3: nothing in meta distinguishes lean from full use cases; add `sizing_guidance` and `default_size`. **C-06 (no size/token metadata). Medium, effort S.** Measured: companions 3.2k-5.3k tokens, full templates 2.0k-4.2k, leans 1.0k-1.8k, guides ~0.6k; nothing declares this; add a generated `approx_tokens` map so agents can budget before fetching. **C-05** is consolidated into B-02. **C-08 (no fill provenance beyond template identity). Low, effort S.** Add `filled_by` / `fill_method` placeholders and stamp `fill_date` at strip time. **C-09 (manual comment stripping). Low, effort S.** A 20-line `strip-template.py` closes it; wire into the preamble instructions.

**C-02 (pairs_with decorative). Downgraded High to Low by verification.** The verifier found G5 section 8 explicitly designates `pairs_with` as "human-facing, not load-bearing"; a documented decision, not a finding. Surviving residue merged into B-05. Recorded here as a model case of the audit's deviation rule working as intended.

### Dimension D: Governance automation and measurement (grade C)

**Where credibility is already earned.** The gate's philosophy is right: its six checks target real regression classes, run in seconds, produce readable per-check output, and passed all four bundles on a fresh run (exit 0, re-verified independently three times during this audit). Its dash sweep covers all eight files, the correct scope for a house rule. The P3 deviation (Python/local instead of Node/CI) is self-documented in two places, so it is decided-interim, not drift. And the sibling repo removes all excuse on evals: `pm-skills` ships a complete output-eval harness (with-skill vs freehand control arms, blind judge panels, aggregation) whose rubrics already cover all four delivery-docs types.

**D-01 (gate covers roughly half the DoD; "enforceable" overstates). High, CONFIRMED, effort M.**
What: mapping the 11 DoD clauses (methodology.md:189-203) to gate checks A-F: the gate automates portions of about 6 clauses; the research-tracing, guidance-comment-structure, companion-skeleton, guide-structure, and history-content clauses have zero automation. Of the plan's AC-1..AC-14, 9 have no automation at all. The verifier corrected the count (about 6 partially covered, not 5) and noted the README is more hedged than the finding implied (line 106 says "local prototype"), but confirmed the gate's own docstring ("runs the structural quality checks that the methodology's Definition of Done requires") overstates coverage, and README line 100 leads with "enforceable, not aspirational."
Fix: add the three cheap checks (history entry for current version; pairs_with against the pinned skill-ID list; reverse citations), and make the coverage map explicit in the README or a reference doc so unchecked clauses are visibly human-verified rather than silently assumed.

**D-02 (one-directional citation check; false negative demonstrated). Medium, effort S.**
What: check E computes both sets but only tests inline-to-anchor. The auditor copied the gate plus the prd bundle to a scratch directory, added a synthetic never-cited ref-14, and the gate reported "PASS ... 14 anchors, 11 cited" with exit 0: an empirical false negative against the DoD's "no padded entries" clause, which A-04 shows is violated in production today. Ready-to-commit patch (inside `check_citations`, after line 135):

```python
    uncited = sorted(anchors - inline, key=int)
    if uncited:
        problems.append("uncited (padded) reference entr(y/ies) [" + ", ".join(uncited) + "]")
```

**D-03 (no CI on push). Medium, effort S.** No `.github/workflows/` exists; every merge to main relies on one person's discipline for everything the gate does not check (and the gate itself must be remembered). The Python-vs-Node deviation is documented; the absence of any CI wrapper around the existing script is pure gap. Ready-to-commit `.github/workflows/ci.yml`:

```yaml
name: bundle-gate
on:
  push:
    branches: [main]
  pull_request:
jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python _local/tools/check-bundles.py
```

**D-04 (no efficacy evals). High, CONFIRMED, effort M.**
What: nothing measures whether a template produces a better document than a bare prompt. G6 section 2 names this the single highest-leverage gap. Portability was assessed concretely: `pm-skills/scripts/output-eval.workflow.mjs` (skill arm vs control arm, blind N-judge rubric panel) and the eval rubrics cover deliver-prd, deliver-acceptance-criteria, deliver-user-stories (specification family) and deliver-release-notes (communication family; the verifier corrected the auditor's claim that one rubric covers all four). What must be new: a 12-scenario bank (3 per bundle) and a runner adaptation where the "skill arm" injects the blank template plus guidance.
Why it matters: this is the difference between claiming best-in-class and measuring it; the audit weights it heavily because the entire positioning rests on it.
Fix: port EV-1 with the next template change so it doubles as a regression harness; record a baseline discrimination gap per bundle.

**D-05 (zero real usage; no path to user one). High, CONFIRMED, effort S.**
What: every filled artifact in the repo is an authored example (12 files carry `source_template`, all author-produced; the verifier corrected the count from four). Catalog Recommendation 1 (G7:289) gates Tier 2 on "surviving one real usage cycle"; EV-3 (feedback protocol) and LP-1/LP-2 exist only as brief ideas; P5 tests installation, not usage; D2 has sat open 11 days at a self-estimated 30-minute cost.
Fix: make "one real fill" a named milestone that blocks bundle #5: fill one real internal document from the lean PRD template, capture the EV-3 five-question form, and bank the result as both the first usage cycle and the first eval baseline. Cost: one working session.

**D-06 (H2-only nesting check). Low, effort S.** No current false negative (no H3s exist in any variant), but the check would miss H3 drift in future bundles; extend to (level, text) tuples.

### Dimension E: Distribution, adoption, and sustainability (grade D)

**Where credibility is already earned.** The adoption thinking is better than the adoption reality: G6's YAGNI sequencing ("get real usage first, then invest in heavy machinery") is genuinely sound strategy; the `_local/` location is a documented, reasoned deferral rather than drift; the pull-based roadmap design is the right architecture for a solo maintainer; and every missing distribution surface has a proven, copyable reference implementation one directory away in pm-skills, making remediation mechanical rather than uncertain.

**E-01 (no LICENSE file). Critical, CONFIRMED, effort S.**
What: README.md:116 and every meta.yaml declare Apache-2.0; the design spec root diagram (lines 147-173) and plan P2 (line 132) both commit to a LICENSE file copied from pm-skills; `git ls-files`, Glob, and repo-wide grep all confirm none exists. The repo is public on GitHub now.
Why it matters: prose and metadata declarations do not grant a copyright license; only the LICENSE file does. For a product whose entire use case is "copy this file and fill it in," every consumer copy is technically infringing until this lands. This is the cheapest Critical finding the audit has ever likely to see: the plan even names the source file to copy.
Fix: copy `pm-skills/LICENSE` to the repo root as the next commit.

**E-02 (all distribution surfaces absent). High, CONFIRMED, effort M.**
What: no plugin manifest, marketplace.json, AGENTS.md, CONTRIBUTING, CHANGELOG, CI, or tags (design spec section 12 committed to six channels; plan P2/P5 committed to the files). The plan's own progress table records P2/P5 as "Not started," so this is acknowledged deferral, but the consequence stands: for a library claiming agents "reach for it first," no agent discovery path exists at all.
Fix: a one-day P2 skeleton sprint (LICENSE, AGENTS.md, CHANGELOG stub, plugin.json stub from the pm-skills reference); defer marketplace/MCP until the wedge produces usage signal.

**E-03 (skills-CLI channel untested; D2 aging). High downgraded to Medium by verification, effort S.**
The gap is real (no SKILL.md exists; the fetched plugin docs confirm skills require one; D2 open 11 days against a 30-minute estimate). The verifier downgraded because the governance corpus explicitly marks D2 non-blocking for v0.1 (plan lines 271, 411-412) and stages it to P5, so the "no triage process" indictment overreached; what survives is that the test remains cheap, decisive for the distribution story, and undone. Fix: run it this week; record the outcome; close D2.

**E-04 (maintainer math does not close). High, CONFIRMED, effort M.**
What: Tier 1 = 28 bundles x 8 files = 224 authored files; current citation density (37 anchors / 4 bundles, arithmetic re-derived by the verifier) projects ~259 citations needing staleness re-verification; there is no CONTRIBUTING file, no pull queue (P7 not started), no maintenance cadence (VL-3 open), and G6 section 3.G itself calls the business model "the total whitespace."
Why it matters: the moat is expensive-to-maintain freshness and rigor on a solo maintainer's clock; without a cadence, contributors, or funding, the quality ceiling is bounded by one person's spare time, and the positioning claims more than that ceiling can hold.
Fix: decide VL-3 at one-paragraph depth (owner, cadence, e.g. quarterly re-verification), stand up the P7 pull queue before bundle #5, and write a minimal CONTRIBUTING signal.

**E-05 (no decision triage). Medium, effort S.** D2/D3 (11 days at 30-60 minute cost) and HY-2/VL-1 (8 days) age without owners or dates; adopt a rule: any decision with stated resolution cost under 2 hours is resolved within 3 working days, applied retroactively this week. **E-06 (_local graduation uncharted). Medium, effort M.** The migration touches README (14 references), methodology `applies_to`, the gate's `TEMPLATES_DIR`, and future deep links; the `.gitignore` itself documents the global `_LOCAL/` ignore hazard for any second contributor. Decide HY-2, write the checklist, move atomically. **E-07 (version anchor missing). Medium, effort S.** All bundles declare 0.1.0; zero tags and no CHANGELOG exist to pin what 0.1.0 was; provenance stamped into filled documents will point at an unanchored version. One hour: CHANGELOG with a [0.1.0] section, tag it.

### Dimension F: Documentation and onboarding excellence (grade C)

**Where credibility is already earned.** At the point of use, the documentation is excellent: the WHAT/WHY/ASK/GOOD/WEAK/TRAP comments are the how-to quadrant delivered exactly where the author needs it; the 11-section companions are a genuine explanation quadrant most template libraries never attempt; the methodology is a strong, internally consistent contributor reference; the strategy briefs preserve decision reasoning with named lenses and honest confidence labels; and the README's anatomy table gives an accurate mental model in eight rows. The failure is architectural, not substantive: the content exists and the tree does not.

**F-01 (no consumer quickstart; the beginner path breaks at the first fill). High, CONFIRMED, effort S.**
What: from the README alone a newcomer can find a bundle (table, lines 29-34) and understand the anatomy (lines 44-58) but never learns how to fill one: the fill instructions live only inside HTML comments (`prd_template-lean.md:15-28`) that GitHub's rendered view hides, and the README's only "learn more" pointer (line 21) goes to the contributor methodology. Diataxis's tutorial quadrant is empty (diataxis.fr returned HTTP 429 during the audit; the framework was applied from documented knowledge and is marked accordingly in section 8).
Why it matters: a documentation product that cannot onboard its own first user from its front door undercuts the best-in-class claim at the very first interaction; the verifier confirmed the GitHub-rendering blindspot makes it worse than it looks.
Fix: a 30-minute "Quick start: use a template" section (clone, open lean template in an editor, read the preamble, replace placeholders, self-grade against the guide, delete comments), later graduating to `docs/quickstart-use-a-template.md`.

**F-03 (mandated ADRs missing; decisions are undiscoverable prose; canonical for G-06). High, CONFIRMED, effort M.**
What: plan P1 (lines 81-109) mandated four ADR files behind a blocking gate; G4:381 claims they were "recorded as ADRs in P1"; no `docs/decisions/` exists anywhere, so the traceability pointer asserts records that do not exist. Three further decisions have no durable record at all: Approach A guidance style, the research log as the 8th bundle file, and the Python/local gate as interim. Both external ADR references were fetched live (HTTP 200).
Fix: transcribe seven ADRs (an hour's work; the content already exists in prose), or explicitly retire the ADR requirement and correct G4:381. Ready-to-commit `docs/decisions/TEMPLATE.md` (MADR-style, 22 lines):

```markdown
# [Short imperative title of the decision]

Status: [proposed | accepted | deprecated | superseded-by YYYYMMDD-title.md]
Date: YYYY-MM-DD
Deciders: [names]

## Context and problem statement

[The situation and the question that required a decision. One to three sentences.]

## Considered options

* Option A: ...
* Option B: ...

## Decision outcome

Chosen option: Option A, because [one-line justification].

### Consequences

* Good: [positive outcome]
* Accepted risk: [trade-off knowingly taken]
```

**F-02 (no reference home for the authoring contract). High downgraded to Medium by verification, effort M.** The verifier corrected the claim that five documents are required: methodology B1 does codify the variant model and guidance style, so the methodology alone carries more of the contract than the finding asserted. What survives: gate behavior and its known gaps are documented only in the script source, no family contract exists, no `docs/reference/` tree was built although the design spec planned one (lines 148-173), and no index composes the contract into one findable place. Fix: `docs/contributing/authoring-contract.md` as a composed index, not a rewrite.

**F-05 (status language conflict). Medium, effort S.** README.md:27 says "complete ... researched, enriched, cross-linked, and verified" while all four metas say `status: beta` and every governance doc says `status: draft`; "family is complete" is also contested by the missing contract (B-01). Reconcile: "first family shipped, quality-gated at beta." **F-06 (audiences interleaved). Medium, effort M.** Lines 67-116 of the README are contributor/governance content; no CONTRIBUTING.md exists; split the journeys (see section 7). **F-04** is consolidated into B-04. **F-07 (house convention violated at home). Low, effort S.** README.md:111 declares "reference IDs carry a human-readable handle" while G4:381 and the gate docstring use bare P1/P3; sweep them.

### Dimension G: Strategy and roadmap coherence (grade B)

**Where credibility is already earned.** The strategy corpus is unusually rigorous and self-aware: the reversibility lens was applied correctly and the four expensive-to-reverse decisions were settled before content and are consistent with what was actually built (verified field-by-field in the metas); coverage-first was named "the seductive wrong answer" and rejected; G6 opens by naming its own biggest gap ("asserted, not proven"). The differentiation claim survives direct inspection: both named competitors (dend/awesome-product-management, lorabv/awesome-agile) were fetched live and confirmed to be outward-pointing link lists, not governed template systems; nothing in that set attempts dual-reader companions, nesting discipline, or provenance. The content axis of the moat is built, not promised.

**G-01 (the operative plan is stale and self-contradictory). High, CONFIRMED, effort S.**
What: the progress table (G4:38-46) reads "Not started" for all seven phases below the sentence "it is the source of truth for progress" (line 48), while four bundles, a methodology, an atlas, a README, and a gate exist; the P1 blocking gate (line 98) was bypassed in form. G6 re-sequences "relative to the existing P1-P7 plan" without ratifying the skip.
Why it matters: a cold-start contributor (or the maintainer in six months) reading the source of truth concludes nothing is built. Plan-vs-actual coherence is precisely what this dimension measures, and the deviation, though defensible on the merits, is silent.
Fix: truth-up the table (P4 done; P6 content done, rails not; P1/P2/P3/P5/P7 not started), add a dated Revisions row recording the content-first re-sequencing and its rationale, and either write the four mandated ADRs or retire the requirement explicitly.

**G-02 (the governed moat claim outruns enforcement). High, CONFIRMED, effort S.**
What: README.md:100 ("The governance is enforceable, not aspirational") and design spec line 54 ("A CI-enforced Definition of Done means there are no half-finished or undocumented templates") lead unqualified, while enforcement is a hand-run local script covering roughly half the DoD with no CI, no LICENSE, and a stale plan. The interior qualifications (README:106 "local prototype"; the gate docstring) do not neutralize the front-door claims.
Why it matters: the repo's entire positioning is credibility; a reader who clones and finds the gap between claim and artifact experiences exactly the failure mode the repo exists to prevent.
Fix: close the gap rather than soften where closing is cheap: the D-03 ci.yml makes "enforceable" true for the six existing checks in an afternoon; reword the design spec pillar to "enforced locally today, in CI next" until then; reconcile the seven-vs-eight-file methodology text (B-04) in the same pass.

**G-03 (roadmap sequencing: proving and reach are prioritized over the credibility floor). High, CONFIRMED, effort M.**
What: G6's 80/20 headline names EV-1 (evals), LP-1/LP-2 (usage loop), and AG-2 (MCP) as the three bets, while its own risk section (line 157) argues the opposite order ("do not build heavy machinery for a library nobody uses yet"), and neither mentions that the library today is unlicensed, untagged, uninstallable, and unreachable. The adversarial stress test of the repo's next-three concluded the opposite ordering survives: **floor (LICENSE, CI, tag, ADR truth-up) then wedge (LP-2 grade-my-doc, which needs only the four existing bundles) then proof (EV-1) then reach (AG-2 MCP last)**. A wedge with no license converts nobody; evals before any real usage over-fit to authored examples; MCP amplifies whatever exists, so it multiplies zero until there is usage.
This finding also carries the dimension's central-claim verdict, adopted in the executive summary: partially true; content earned, "governed"/"agent-native"/"reference implementation" on credit.
Fix: adopt the floor-wedge-proof-reach sequence in section 5; it inverts G6's headline in favor of G6's own risk logic.

**G-04 (roadmap anchored to a bypassed spine; superseded spec still teaches the old model). Medium, effort S.** The design spec still says "Working name: pm-templates" (line 14) and teaches S/M/L with `sizes_available: [s, m, l]` (section 6, Appendix A) with no superseded banner; G6's "When" column sequences against plan phases that were leapfrogged; the G6 section 7 questions have no owners or dates. Fix: superseded banner on the spec header pointing at the 2026-06-29 resolutions; restate the next-three as standalone items with owner and date. **G-05 (sustainability risks named but unowned). Medium, effort M.** VL-3 undecided, FR-1 unbuilt (37 URLs, zero automation), bus factor unmitigated; convert to owned commitments: a written cadence plus a link-check in the same CI run. **G-06** is consolidated into F-03.

**Risk register (from Dimension G, verified where factual):**

| Risk | Likelihood | Impact | Cheapest real mitigation |
|---|---|---|---|
| Citation rot across 37 (going on ~259) URLs, silent | H | H | Link-check (lychee) in the D-03 CI job; FR-1 minimum form |
| Solo-maintainer bus factor | M | H | CONTRIBUTING.md + AG-3 authoring kit (mostly exists as tacit process) |
| Licensing ambiguity while public | H (live now) | H | E-01: copy the LICENSE file |
| Ecosystem contract change (pm-skills IDs, Claude plugin spec, agentskills.io) | M | M | Pin skill-ID list in the gate; resolve D3 (1-hour spec read) |
| Zero-usage vacuum (building on assumption) | H | H | D-05: one real fill + EV-3 form before bundle #5 |
| Stale plan misleads future contributors | H | M | G-01 truth-up (30 minutes) |
| `_local/` global-gitignore hazard for any second clone/contributor | M | M | Resolve HY-2; graduate per E-06 checklist |
| Single-domain examples cap the "templates travel" claim | M | M | CT-1 second-domain example for one bundle; scope note meanwhile |

---

## 5. Improvement roadmap

Sequencing thesis, defended: **floor, then wedge, then proof, then reach.** The audit's stress test (G-03, confirmed) found the repo's own published 80/20 (evals, usage loop, MCP) is internally contradicted by its own risk section, and both are pre-empted by a cheaper truth: every deep investment is discounted while the front door makes claims a clone disproves in five minutes. The floor costs about one day and makes the claims true; the wedge (LP-2) needs only the four existing bundles and produces the usage signal; evals then measure something real instead of authored examples; MCP amplifies last. Infrastructure beyond the floor is deliberately deferred behind adoption signal, which is G6's own YAGNI logic applied consistently.

### Now (this week; nearly all S-effort; the floor plus integrity fixes)

| # | Action | Findings closed / advanced | Cost |
|---|---|---|---|
| 1 | Copy `pm-skills/LICENSE` to repo root | E-01 (LICENSE) | 5 min |
| 2 | Add `.github/workflows/ci.yml` running the existing gate (snippet in D-03) | D-03 (CI), G-02 partial (makes "enforceable" true for checks A-F) | 30 min |
| 3 | CHANGELOG.md with [0.1.0]; tag `v0.1.0` | E-07 (version anchor) | 1 h |
| 4 | Truth-up the plan progress table + dated Revisions row | G-01 (stale plan) | 30 min |
| 5 | Transcribe 7 ADRs into `docs/decisions/` (template in F-03) | F-03, G-06, G-01 partial | 2 h |
| 6 | Fix methodology "seven files" to eight (both occurrences + table row) | B-04, C-07, F-04 | 15 min |
| 7 | Citation integrity pass: SVPG qualifiers, Ranorex replacement, Keep a Changelog 1.1.2, cite-or-remove refs 8/12 + retag 12, de-quote the Lenny phrase, split combined entries | A-01, A-02, A-03, A-04, A-05, A-06, B-03 | 2-3 h |
| 8 | Gate: reverse-citation check (snippet in D-02) + placeholder scan over meta.yaml | D-02, part of B-02/C-05 | 30 min |
| 9 | Fill `maintainer`/`owner` placeholders in 4 metas + methodology | C-05 (with B-02) | 10 min |
| 10 | README reconciliation: "enforceable" wording, "complete/verified" vs beta, quickstart section | G-02, F-05, F-01 | 1 h |
| 11 | Run the D2 skills-CLI test; record outcome; close D2 | E-03, E-05 partial | 30 min |
| 12 | Delete `_local/templates/_working/`; sweep bare P1/P3 IDs | B-08, F-07 | 15 min |

### Next (structural; the following 2-3 weeks)

| # | Action | Findings | Notes |
|---|---|---|---|
| 13 | `meta.schema.json` + gate check G (schema validation) | B-02, C-03 partial | Stub in B-02 |
| 14 | `_families/delivery-docs.contract.md` + family gate check | B-01 | Model on pm-skills contract |
| 15 | Generated root `manifest.json` + count-consistency check | C-03, E-02 partial | P5 step, pulled forward |
| 16 | `sizing_guidance`, `default_size`, `approx_tokens` in metas (generated) | C-04, C-06 | Makes selection fully deterministic |
| 17 | `strip-template.py` + `filled_by`/`fill_method` provenance fields | C-09, C-08 | Completes the manual loop |
| 18 | Link-check (lychee) + staleness dates in the CI job | A-03 systemic, G-05, FR-1 | The rot detector |
| 19 | README split + CONTRIBUTING.md + `docs/contributing/authoring-contract.md` | F-06, F-02, E-04 partial | Section 7 tree |
| 20 | Decision-aging rule (under-2h decisions resolve in 3 days); resolve HY-2; write the `_local/` graduation checklist | E-05, E-06 | Graduation executes in Later |
| 21 | **LP-2 grade-my-existing-doc wedge** (as a skill; reuses each guide's rubric) | D-05 path, E-04, G-03 | The adoption wedge; first real usage signal |
| 22 | One real fill of one template + EV-3 five-question capture | D-05 | The first usage cycle; blocks bundle #5 |

### Later (strategic; gated on usage signal from 21-22)

| # | Action | Findings | Gate |
|---|---|---|---|
| 23 | LP-1 use-template fill flow (interview via ASK lines) | C-01 | After LP-2 shows demand shape |
| 24 | EV-1 efficacy evals ported from pm-skills (12 scenarios, discrimination gap baseline) | D-04 | With the first template change, as regression harness |
| 25 | Execute `_local/` graduation to `templates/` | E-06 | After HY-2 decision + checklist |
| 26 | AG-2 MCP server (bundle-summary resource pattern) + AG-1 section schema | C-01 follow-on, C-06 | After LP-1/LP-2 prove the loop |
| 27 | Second-domain + lean-variant examples for one bundle (CT-1) | A dimension validity limit | When a real user from another domain appears, or before public launch |
| 28 | VL-1 business-model decision + VL-3 maintenance cadence; plugin/marketplace wiring | E-04, E-02 remainder | VL-1 before anything goes to a marketplace |

---

## 6. Ideas and insights (not findings)

Non-defect opportunities surfaced by the auditors, deduplicated and labeled by source dimension:

1. **fetch_status column in research logs** (A): a machine-readable retrieval state (OK / 403 / PAYWALL / EMPTY / CORROBORATED) per source, with a gate rule that any non-OK source requires a qualifier in the companion entry. Systematizes the A-02 fix forever.
2. **Latest-URL pinning policy** (A): cite versioned standards at their redirecting root or latest path, and add a DoD question "is the cited edition still current?"; prevents the A-03 class.
3. **Subscriber access for the most-cited paywalled source** (A): the Lenny post is cited seven times across the PRD companion; one subscription closes the biggest excerpt-only gap.
4. **Example scope note** (A): one header line per example naming the illustrative domain (B2B SaaS analytics) so the CT-1 single-domain limitation is visible to users before the second-domain examples exist.
5. **Schema-derived family contract** (B): once `_families/delivery-docs.contract.md` exists, derive the allowed-values vocabulary in `meta.schema.json` from it so contract and schema cannot drift.
6. **related_templates resolver** (B): gate check that every entry resolves to an existing bundle or carries a `future:` prefix.
7. **ROW HINT presence check** (B): if a section body contains a table pipe and the comment lacks ROW HINT, fail; automates methodology B1's table rule.
8. **LP-1 as an orchestration layer, not a build** (C): the ASK lines are already the interview script; regex-extract them, fill, stamp, strip, check. Most ingredients exist today.
9. **MCP bundle-summary resource** (C): when AG-2 lands, serve guide + meta (~800-1,000 tokens) as the default resource and the companion only on request; aligns with Anthropic's context-efficiency guidance.
10. **STATE.md single source of current truth** (G): one file stating what is built vs planned (4 of 205, 1 family, local gate, CI status), replacing the scattered plan-table/README/brief triangulation.
11. **"Deliberately not built" as a first-class state** (G, VS-3): mark the ~201 unbuilt types in the atlas as pull-gated decisions; turns the coverage gap into visible discipline.
12. **The pm-skills flywheel diagram + pairs_with validator** (G): make the two-repo loop a literal diagram and give the seam its pinned-ID validator so ecosystem coherence is demonstrable.
13. **LP-2's triple payoff** (D): one grade-my-doc session simultaneously produces the first real usage cycle (D-05), tests whether the guide rubric is complete enough to score against, and informally exercises the fill flow. Highest information-per-hour action available.
14. **Eval-on-first-change timing** (D): the "ship evals with the reference bundle" window has passed; the next-best moment is the first edit to any bundle, where the eval doubles as the regression test.
15. **Agent authoring kit** (G6's AG-3, endorsed by D/E): formalize the methodology + scaffold prompt + verification recipe as the second-maintainer mitigation; most of it exists as tacit process.

---

## 7. Documentation rebuild plan (Dimension F scored C)

Target tree implementing progressive disclosure for both audiences. Compose from existing content; almost nothing needs writing from scratch.

**Consumer path:**

| File | Content | Source material |
|---|---|---|
| `README.md` (target: under 120 lines) | Positioning, quick start block, bundle table, anatomy table, pm-skills loop, pointer to docs/ | Current README minus lines 67-116 |
| `docs/quickstart-use-a-template.md` | Tutorial: clone, open lean template in editor, read preamble, fill, self-grade, strip comments (or run strip script) | Template preambles + F-01 fix |
| `_local/templates/<type>/README.md` x4 | Per-bundle landing: what it is, lean-vs-full signal, links to guide/companion/example | Guides + meta summaries |

**Contributor path:**

| File | Content | Source material |
|---|---|---|
| `CONTRIBUTING.md` | Authoring overview; pointers to methodology, contract, ADRs, gate | New (short) |
| `docs/contributing/authoring-contract.md` | The single reference home: 8-file anatomy, citation standard, comment standard, nesting rule, gate checks A-F with known gaps, meta schema, family contract, 11-clause DoD | Composed index over methodology + design spec + gate source |
| `docs/decisions/TEMPLATE.md` | MADR stub (22 lines, provided in F-03) | This report |
| `docs/decisions/20260629-repo-and-package-name.md` | status: accepted | G3 sec. 5 item 1 |
| `docs/decisions/20260629-variant-model.md` | status: accepted | G3 sec. 5 item 2 |
| `docs/decisions/20260629-phase-vocabulary.md` | status: accepted | G3 sec. 5 item 3 |
| `docs/decisions/20260629-first-family-and-bundle.md` | status: accepted | G3 sec. 5 item 4 |
| `docs/decisions/20260630-guidance-style-approach-a.md` | status: accepted | `_working/README.md` (then delete the folder) |
| `docs/decisions/20260630-research-log-as-8th-file.md` | status: accepted | DoD Research clause + gate ROLES |
| `docs/decisions/20260703-gate-python-local-interim.md` | status: accepted (interim) | Gate docstring + README:106 |
| `docs/reference/gate-checks.md` | Checks A-F, scope, known gaps (one-way citations until patched, H2-only nesting) | check-bundles.py |
| `docs/reference/metadata-schema.md` | Catalog meta + instance meta fields, allowed values, the two-tier rule | Design spec sec. 9 + meta.schema.json |
| `docs/reference/family-contracts.md` (or `_families/delivery-docs.contract.md`) | The delivery-docs contract | B-01 fix |

Also: a one-line superseded banner atop the design spec (G-04) pointing to the 2026-06-29 resolutions, so the spec stops teaching `pm-templates` and S/M/L to newcomers.

---

## 8. Traceable source and reference list

### Part 1: Internal repo files cited by findings

Every file below is cited as evidence by at least one finding; every finding's evidence resolves to at least one entry here or in Part 2.

| # | File | Cited by findings |
|---|---|---|
| I-1 | `README.md` | B-04, C-01, C-02, C-07, D-01, D-03, D-04, E-01, E-02, E-06, F-01, F-02, F-04, F-05, F-06, F-07, G-02, G-03 |
| I-2 | `_local/templates/methodology.md` | A-04, A-06, B-02, B-03, B-04, B-07, C-03, C-04, C-05, C-07, D-01, D-02, D-06, E-06, F-02, F-04, F-05, G-02 |
| I-3 | `_local/tools/check-bundles.py` | B-02, B-03, B-04, C-02, C-07, C-09, D-01, D-02, D-03, D-06, E-06, F-04, F-07, G-02 |
| I-4 | `_local/initial-discovery/docs/implementation-plan_catalog-to-template-library.md` | B-01, C-03, D-01, D-03, D-05, E-01, E-02, E-03, E-04, E-05, E-07, F-03, F-07, G-01, G-06 |
| I-5 | `_local/initial-discovery/docs/template-library-design-spec.md` | B-01, B-02, C-01, C-08, E-01, E-02, E-03, E-07, F-02, F-05, G-02, G-04 |
| I-6 | `_local/initial-discovery/docs/strategy-brief_raising-the-ceiling_2026-07-02.md` | C-01, D-04, D-05, E-04, E-05, G-01, G-03, G-04, G-05 |
| I-7 | `_local/initial-discovery/docs/strategy-brief_catalog-to-template-library.md` | E-03, E-05, F-03, G-06 |
| I-8 | `_local/initial-discovery/docs/deep-research_master-catalog.md` | D-05, E-04 |
| I-9 | `_local/templates/prd/prd_meta.yaml` | B-01, B-02, B-05, C-02, C-03, C-04, C-05, C-06, E-01, E-07, F-05 |
| I-10 | `_local/templates/prd/prd_companion.md` | A-02, A-04, A-05, B-03, B-06, C-06, D-02 |
| I-11 | `_local/templates/prd/prd_research-log.md` | A-02, A-05 |
| I-12 | `_local/templates/prd/prd_template-lean.md` | B-07, C-01, C-08, C-09, F-01 |
| I-13 | `_local/templates/prd/prd_template-full.md` | B-06, B-07, C-06, C-09 |
| I-14 | `_local/templates/prd/prd_example.md` | C-08, D-05 |
| I-15 | `_local/templates/acceptance-criteria/acceptance-criteria_companion.md` | A-01, A-06 |
| I-16 | `_local/templates/acceptance-criteria/acceptance-criteria_meta.yaml` | C-05 |
| I-17 | `_local/templates/release-notes/release-notes_companion.md` | A-03, A-06 |
| I-18 | `_local/templates/release-notes/release-notes_research-log.md` | A-03 |
| I-19 | `_local/templates/release-notes/release-notes_meta.yaml` | B-05, C-02, C-05 |
| I-20 | `_local/templates/user-stories/user-stories_companion.md` | A-06 |
| I-21 | `_local/templates/user-stories/user-stories_meta.yaml` | C-04, C-05 |
| I-22 | `_local/templates/_working/README.md` | B-08 |
| I-23 | `.gitignore` | E-06 |
| I-24 | `E:/Projects/product-on-purpose/pm-skills/scripts/output-eval.workflow.mjs` (sibling repo) | D-04 |
| I-25 | `E:/Projects/product-on-purpose/pm-skills/docs/internal/eval-rubrics/specification.md` (sibling repo; communication.md verified by the D-04 verifier) | D-04 |

Phase 0 corpus documents not individually cited by a finding ID (G5 layered design, G8 research prompt, G10 session log, atlas files, `pm-skills/skill-manifest.json`) are cited in the context sheet and in verifier notes (G5 section 8 decided the C-02 downgrade; G10 seeded the A-02 fetch targets).

### Part 2: External URLs

Numbered entries are cited by findings (no orphans in either direction). Retrieval results are from this audit's live fetches (2026-07-10).

| # | URL | Title / why used | Retrieval result | Findings |
|---|---|---|---|---|
| X-1 | https://www.ranorex.com/blog/given-when-then-tests/ | Cited source under test (form-selection claim) | Resolved; content does NOT support the attributed claim (fetched twice: auditor + verifier) | A-01 |
| X-2 | https://www.svpg.com/revisiting-the-product-spec/ | Cited source under test (access-date claim) | HTTP 403 Forbidden (re-verified during verification) | A-02 |
| X-3 | https://www.svpg.com/discovery-vs-documentation/ | Cited source under test | HTTP 403 Forbidden (re-verified) | A-02 |
| X-4 | https://keepachangelog.com/en/1.1.0/ | Cited normative spec; staleness check | Resolved; site changelog shows 1.1.1 (2023-03) and 1.1.2 (2024-09) superseding the cited 1.1.0 | A-03 |
| X-5 | https://www.anthropic.com/engineering/writing-tools-for-agents | Benchmark for agent-tool design (consolidation, context efficiency) | Resolved | C-01, C-03, C-06 |
| X-6 | https://adr.github.io | ADR practice reference | Resolved (HTTP 200) | F-03 |
| X-7 | https://adr.github.io/madr/ | MADR template format | Resolved (HTTP 200) | F-03 |
| X-8 | https://code.claude.com/docs/en/plugins | Claude plugin/skill packaging requirements (SKILL.md requirement) | Resolved | E-03, E-02 |
| X-9 | https://diataxis.fr | Documentation framework grading standard | HTTP 429 (rate-limited) at audit time; framework applied from documented knowledge, marked accordingly | F-01, F-02, F-06 |
| X-10 | https://github.com/dend/awesome-product-management | Competitor named by the design spec; moat reality check | Resolved; confirmed outward-pointing curated list | G-03 (moat verdict; also G strengths) |
| X-11 | https://github.com/lorabv/awesome-agile | Competitor named by the design spec | Resolved; confirmed curated list | G-03 |
| X-12 | https://json-schema.org (draft 2020-12) | Grounds the B-02 schema recommendation | Referenced as recommendation grounding; not fetched in this audit (unverified) | B-02 |
| X-13 | https://github.com/lycheeverse/lychee | Grounds the link-rot gate recommendation | Referenced as recommendation grounding; not fetched (unverified) | A-03 recommendation, roadmap item 18 |
| X-14 | https://docs.github.com/en/actions | Grounds the CI wiring recommendation | Referenced; not fetched (unverified) | D-03 |
| X-15 | https://modelcontextprotocol.io | Grounds the MCP-path recommendation | Referenced per audit charter; retrieval result not recorded by the auditor (unverified) | C-01 recommendation |
| X-16 | https://semver.org | Grounds tag/version hygiene (design spec sec. 14 commitment) | Referenced; not fetched this audit (unverified) | E-07 |
| X-17 | https://developers.google.com/style | Writing-quality bar for Dimension A | Fetched by the Dimension A auditor; produced no finding (strengths only) | A dimension grade rationale |

Additional non-finding verification fetches by Dimension A (supporting strengths, not findings, listed for completeness): the Scrum Guide (three-artifacts claim), SemVer 2.0.0, Conventional Commits 1.0.0, and the Working Backwards site, each resolved and confirmed to support the companion claims they anchor.

---

## Appendix: Method

- **Phases:** Phase 0 corpus fingerprint built inline by the lead auditor (context sheet, gap map, sampling strategy) before any delegation. Phase 1: seven parallel dimension auditors (A-F on Sonnet, G on Opus; reasoning effort high), each required to read the context sheet, verify its leads independently, and return schema-validated JSON findings with file:line evidence. Phase 2: every High/Critical finding (19) went to an independent adversarial verifier (Sonnet, effort high) instructed to refute it: re-read cited lines, re-run commands, re-fetch URLs, and check the governance corpus for decided deviations. Phase 3: synthesis, cross-dimension dedup, and this report by the lead auditor (Fable).
- **Scale:** 26 agents, 493 tool calls, ~1.51M subagent tokens, 17.4 minutes wall-clock, zero agent errors.
- **Verification outcomes:** 16 CONFIRMED, 3 DOWNGRADED (C-02 High to Low: the "decorative seam" is a documented design decision in the layered design section 8; E-03 High to Medium: D2 is documented non-blocking and staged; F-02 High to Medium: the methodology carries more of the authoring contract than claimed), 0 REFUTED outright. Verifiers also corrected four factual details in confirmed findings (D-01 clause count, D-04 rubric file, D-05 filled-file count, E-01 two line numbers off by one), all noted in section 4.
- **Dedup:** six findings consolidated under canonical IDs (C-07 and F-04 into B-04; B-03 into A-04/D-02; C-05 into B-02; C-02 residue into B-05; G-06 into F-03). All 49 IDs remain in the section 3 table.
- **Deviation rule applied:** documented, reasoned deviations were not counted as findings (the `_local/` location, the Python/local gate as interim, `pairs_with` as human-facing); silent drift and undocumented decisions were (missing LICENSE, stale plan table, seven-vs-eight files, missing ADRs despite the plan claiming they exist).
- **House rules:** no em-dash or en-dash characters anywhere in this report or its companion files; reference IDs carry human-readable handles on first use.
