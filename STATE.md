# STATE

> **The single source of current truth for this repository.** Update this file in the same commit as any milestone exit, release, or status change.
>
> Plans and briefs are dated projections. Where they disagree with this file, **this file wins**.
>
> This file exists because of audit finding G-01: the implementation plan's progress table said "Not started" for all seven phases while two of them were demonstrably complete, and it went stale within a week of being written. A plan that lies about the tree is worse than no plan. The fix is not "remember to update the plan"; it is to have one short file that is cheap to keep honest and that outranks everything else.

**Last updated:** 2026-07-16 (RFC bundle shipped, 6th type and 2nd in `decision-docs`; repo public; CI green and branch-protected; M0 merged; gate hardened with YAML check G + ADR 0014; EC-2 catalog fix)

---

## Built and true today

| What | State |
|---|---|
| **Bundles** | 6 of 27 Tier-1 catalog types. Family `delivery-docs`: `prd`, `user-stories`, `acceptance-criteria`, `release-notes`. Family `decision-docs`: `adr`, `rfc`. Eight files each. Status `beta`, `template_version` 0.1.0. |
| **License** | Apache-2.0, granted at the repo root. Copyright Jonathan Prisant. |
| **Governance gate** | `tools/check-bundles.py`, seven checks (files, dashes, nesting, clean example, citation resolution, meta size contract, frontmatter YAML validity). Six are pure stdlib; the seventh (G) uses PyYAML and SKIPs locally if absent ([ADR 0014](docs/internal/decisions/0014-gate-may-use-pyyaml-for-frontmatter-validity.md)). **Runs in CI** on every push and PR; branch protection on `main` requires it to pass before merge. Passing on all six bundles. |
| **Decision records** | `docs/internal/decisions/`, fourteen ADRs in [MADR v4](https://github.com/adr/madr) format, plus a README documenting the convention. All accepted. Matches the org standard used by `agent-config-toolkit` and scaffolded by `jp-init-project`. |
| **Layout** | The library lives at `templates/` (flat, by document type), the gate at `tools/`, the atlas at `atlas/`, and the planning, strategy, catalog, roadmap and decision records at `docs/internal/`. Decision HY-2 (scaffold graduation) closed 2026-07-12; the `_local/` split closed 2026-07-14 ([ADR 0013](docs/internal/decisions/0013-local-split-and-going-public.md)). |
| **Atlas** | 205-type interactive catalog map at `atlas/atlas.html`. |
| **Methodology** | v0.2.2 (`templates/methodology.md`), status draft. Governs authoring. |
| **Master catalog** | [`docs/internal/catalog.md`](docs/internal/catalog.md). 205 types, 27 at Tier 1. Cited by the methodology and by every bundle companion. **Its size calls are hypotheses, not facts** (see EC-2 below). |
| **Audit corpus** | `_local/audit/2026-07-10_fable-audit/` on the maintainer's disk. **Deliberately NOT in git** (see [ADR 0013](docs/internal/decisions/0013-local-split-and-going-public.md)); its two load-bearing artifacts were promoted to [`docs/internal/roadmap.md`](docs/internal/roadmap.md) and [`docs/internal/contracts/delivery-docs.md`](docs/internal/contracts/delivery-docs.md). |

## Nothing broken right now

For the first time in this repo's life, that heading is true. Recently closed:

- **CI runs, and is green.** The gate had never once run (private repo, out of Actions minutes; every run died in 3s with zero steps). The repo went **public** on 2026-07-16, and the first real CI run passed. `main` is **branch-protected**: direct pushes blocked, the `gate` check required (strict), force-pushes and deletions blocked, linear history required.
- **M0 is merged.** PR #2 landed the credibility floor, the ADR bundle, and the `_local/` split. PR #1 was auto-closed by the history rewrite.
- **PB-1 (history exposure) is resolved.** `_local/` was purged from every commit (verified 0 paths in history, and `Not Found` on the remote) before going public, so publishing did not expose the audit corpus or session logs. The 29 files remain on the maintainer's disk, backed up at `E:/tmp/_local-backup-20260714`. ADR 0013 is now `accepted` and **confirmed** (its success condition, CI green on `main`, is met).

The reason this section exists at all: STATE.md is here because of audit finding G-01, *a plan that lies about the tree is worse than no plan*. Between 2026-07-13 and 2026-07-14 it had started doing exactly that (claiming CI passed when it had never run). That is fixed, and the section is kept, now empty of breakage, as the place the next breakage gets recorded first.

## Not built (deliberately visible)

- **No version tags. No CHANGELOG.** v0.1.0 is roadmap WP-14, in milestone M1.
- **No distribution surface** beyond `git clone`. No plugin manifest, no marketplace entry, no `manifest.json`.
- **No family contract adopted.** One is drafted and now sits at a canonical path, [`docs/internal/contracts/delivery-docs.md`](docs/internal/contracts/delivery-docs.md), but it is still only a draft: nothing *adopts* it and nothing *validates* against it. Adoption is roadmap WP-24 in milestone M2. The bundle gate checks bundles one at a time and never checks them as a set, so family conformance is unenforced today. (Note that `decision-docs`, opened by the ADR bundle, has no contract at all.)
- **No metadata schema**, so no machine-consumption path. An agent cannot yet select a bundle deterministically.
- **No efficacy evals.** Template quality is currently argued, not measured. This is the gap the audit weighted most heavily (finding D-04).
- **No real usage cycle. Zero fills by anyone but the author.** Every filled artifact in the repo is an authored example. The catalog's own tier rule gates Tier 2 on "survives one real usage cycle", so by its own standard nothing here has graduated.

## Open by choice, not by oversight

- **B-08, the `_working/` folder.** `templates/_working/` still holds the A/B/C guidance-style prototypes, even though its own README line 6 orders its deletion once the decision was made, and the decision *was* made (Approach A, see [`docs/internal/decisions/0006-guidance-style-approach-a.md`](docs/internal/decisions/0006-guidance-style-approach-a.md)). The maintainer chose on 2026-07-12 to keep it. Recorded here so it reads as a decision rather than a miss.

## Findings the library raised about its own ecosystem

Building a bundle turns out to be an audit of everything the bundle touches. The ADR bundle
(2026-07-14) surfaced two defects outside this repo; the RFC bundle (2026-07-16) surfaced a third.
All are **recorded, not silently patched**, because a template library that quietly edits its
neighbors is worse than one that reports.

| # | Finding | Where it lives | Status |
|---|---|---|---|
| **EC-1** | **`develop-adr` (pm-skills) ships a Nygard-format ADR template**, diverging from the MADR v4 convention the org standardized on for its own decision records (mandated by `jp-init-project`, adopted here by [ADR 0011](docs/internal/decisions/0011-madr-v4-at-docs-internal-decisions.md), in use by `agent-config-toolkit` and `thinking-framework-skills`). An agent invoking that skill inside an org repo produces records in the wrong format. This bundle follows MADR and ships a Nygard-to-MADR mapping table in `adr_guide.md` so the two interoperate. | `pm-skills`, `.claude/skills/develop-adr/references/TEMPLATE.md` | Open, for the pm-skills maintainer |
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

## Next milestone

**M1, integrity and truth** (roughly one week). Citation integrity pass (findings A-01 through A-06), gate hardening, close decisions D2 and D3, a consumer quickstart in the README, then tag **v0.1.0** with a release note written using this library's own release-notes template, which makes it the first dogfood artifact.

Full definition: [`docs/internal/roadmap.md`](docs/internal/roadmap.md).

## Open decisions, with ages

| ID | Decision | Open since | Cost to resolve | Scheduled |
|---|---|---|---|---|
| D1 | Build the Layer 1 generator, or not | 2026-06-29 | n/a | Correctly gated on a usage signal |
| D2 | Does `npx skills add` install this repo | 2026-06-29 | 30 min | M1 |
| D3 | agentskills.io resource type for templates | 2026-06-29 | 1 hour | M1 |
| D4 | Regulated-industry tier appetite | 2026-06-29 | n/a | Unscheduled |
| **TX-1** | **Does this library need a second taxonomy axis?** pm-skills carries 89 skills on `phase:` and 86 on a separate `classification:` axis (`foundation`/`utility`/`tool`) with no phase at all. Every bundle here declares a `phase:`, which has been fine only because all four are genuinely `deliver` artifacts. Types like a glossary or a team charter may have no phase to declare. **Must be settled before the metadata schema makes `phase` a required enum.** Surfaced 2026-07-12 by the correction to [ADR 0003 (phase vocabulary)](docs/internal/decisions/0003-phase-vocabulary.md). | 2026-07-12 | ~1 hour | M2 (blocks WP-21) |
| VL-1 | Business model | 2026-07-02 | n/a | Unscheduled |
| VL-3 | Maintenance cadence | 2026-07-02 | n/a | M6 |

**Decision SLA** (audit finding E-05): any open decision whose stated resolution cost is under two hours is resolved within three working days, or explicitly re-dated with a reason. **D2 (30 minutes) and D3 (1 hour) are both long past due.** That is why M1 leads with decision closure rather than with content.

## The claim, and what it is currently worth

The front door claims a **governed, best-in-class, agent-native reference implementation**. As of today:

- **Earned:** researched, dual-reader, nesting-disciplined, provenance-stamped content that the named competitors (curated awesome-lists) do not attempt.
- **Now true, as of M0:** licensed, decision-recorded, CI-enforced (the gate runs on every push and PR, and branch protection requires it before merge), and living at an address that describes it (`templates/`, not `_local/templates/`).
- **Still on credit:** "agent-native" (no machine consumption path exists, so no agent can select a bundle deterministically) and "reference implementation" (untagged, 6 of 205 types, zero external users).

Keep this section honest. It is the fastest way to tell whether the roadmap is working.
