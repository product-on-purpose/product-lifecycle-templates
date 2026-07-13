# STATE

> **The single source of current truth for this repository.** Update this file in the same commit as any milestone exit, release, or status change.
>
> Plans and briefs are dated projections. Where they disagree with this file, **this file wins**.
>
> This file exists because of audit finding G-01: the implementation plan's progress table said "Not started" for all seven phases while two of them were demonstrably complete, and it went stale within a week of being written. A plan that lies about the tree is worse than no plan. The fix is not "remember to update the plan"; it is to have one short file that is cheap to keep honest and that outranks everything else.

**Last updated:** 2026-07-12 (milestone M0, the credibility floor, executed; HY-2 scaffold graduation closed)

---

## Built and true today

| What | State |
|---|---|
| **Bundles** | 4 of 27 Tier-1 catalog types: `prd`, `user-stories`, `acceptance-criteria`, `release-notes`. Eight files each. Family `delivery-docs`. Status `beta`, `template_version` 0.1.0. |
| **License** | Apache-2.0, granted at the repo root. Copyright Jonathan Prisant. |
| **Governance gate** | `tools/check-bundles.py`, six checks (files, dashes, nesting, clean example, citation resolution, meta sizes). **Runs in CI** on every push to `main` and every pull request. Passing. |
| **Decision records** | `docs/decisions/`, nine ADRs plus a MADR template. All ratified 2026-07-12. |
| **Layout** | The library lives at `templates/` (flat, by document type), the gate at `tools/`, the atlas at `atlas/`. `_local/` now holds only internal working material. Decision HY-2 (scaffold graduation) closed 2026-07-12. |
| **Atlas** | 205-type interactive catalog map at `atlas/atlas.html`. |
| **Methodology** | v0.2.1 (`templates/methodology.md`), status draft. Governs authoring. |
| **Audit corpus** | `_local/audit/2026-07-10_fable-audit/`. Start at its `INDEX.md`. |

## Not built (deliberately visible)

- **No version tags. No CHANGELOG.** v0.1.0 is roadmap WP-14, in milestone M1.
- **No distribution surface** beyond `git clone`. No plugin manifest, no marketplace entry, no `manifest.json`.
- **No family contract adopted.** One is drafted and tracked in git, but only as an audit artifact (`_local/audit/2026-07-10_fable-audit/adoption-kit/delivery-docs.contract.md`). It reaches a canonical path with the scaffold decision, roadmap WP-24 in milestone M2. Nothing validates family conformance today: the bundle gate checks bundles one at a time and never checks them as a set.
- **No metadata schema**, so no machine-consumption path. An agent cannot yet select a bundle deterministically.
- **No efficacy evals.** Template quality is currently argued, not measured. This is the gap the audit weighted most heavily (finding D-04).
- **No real usage cycle. Zero fills by anyone but the author.** Every filled artifact in the repo is an authored example. The catalog's own tier rule gates Tier 2 on "survives one real usage cycle", so by its own standard nothing here has graduated.

## Open by choice, not by oversight

- **B-08, the `_working/` folder.** `templates/_working/` still holds the A/B/C guidance-style prototypes, even though its own README line 6 orders its deletion once the decision was made, and the decision *was* made (Approach A, see [`docs/decisions/20260630-guidance-style-approach-a.md`](docs/decisions/20260630-guidance-style-approach-a.md)). The maintainer chose on 2026-07-12 to keep it. Recorded here so it reads as a decision rather than a miss.

## Gate coverage, stated honestly

The gate automates roughly **half** the methodology's Definition of Done (audit finding D-01). Six checks run; the research-tracing, guidance-comment-structure, companion-skeleton, guide-structure, and history-content clauses have **zero** automation and are human-verified. "Enforceable, not aspirational" is now true of what CI runs, and only of that. Gate hardening is roadmap WP-11 in milestone M1.

## Next milestone

**M1, integrity and truth** (roughly one week). Citation integrity pass (findings A-01 through A-06), gate hardening, close decisions D2 and D3, a consumer quickstart in the README, then tag **v0.1.0** with a release note written using this library's own release-notes template, which makes it the first dogfood artifact.

Full definition: [`_local/audit/2026-07-10_fable-audit/10_roadmap-expanded.md`](_local/audit/2026-07-10_fable-audit/10_roadmap-expanded.md).

## Open decisions, with ages

| ID | Decision | Open since | Cost to resolve | Scheduled |
|---|---|---|---|---|
| D1 | Build the Layer 1 generator, or not | 2026-06-29 | n/a | Correctly gated on a usage signal |
| D2 | Does `npx skills add` install this repo | 2026-06-29 | 30 min | M1 |
| D3 | agentskills.io resource type for templates | 2026-06-29 | 1 hour | M1 |
| D4 | Regulated-industry tier appetite | 2026-06-29 | n/a | Unscheduled |
| **TX-1** | **Does this library need a second taxonomy axis?** pm-skills carries 89 skills on `phase:` and 86 on a separate `classification:` axis (`foundation`/`utility`/`tool`) with no phase at all. Every bundle here declares a `phase:`, which has been fine only because all four are genuinely `deliver` artifacts. Types like a glossary or a team charter may have no phase to declare. **Must be settled before the metadata schema makes `phase` a required enum.** Surfaced 2026-07-12 by the correction to [ADR 20260629 (phase vocabulary)](docs/decisions/20260629-phase-vocabulary.md). | 2026-07-12 | ~1 hour | M2 (blocks WP-21) |
| VL-1 | Business model | 2026-07-02 | n/a | Unscheduled |
| VL-3 | Maintenance cadence | 2026-07-02 | n/a | M6 |

**Decision SLA** (audit finding E-05): any open decision whose stated resolution cost is under two hours is resolved within three working days, or explicitly re-dated with a reason. **D2 (30 minutes) and D3 (1 hour) are both long past due.** That is why M1 leads with decision closure rather than with content.

## The claim, and what it is currently worth

The front door claims a **governed, best-in-class, agent-native reference implementation**. As of today:

- **Earned:** researched, dual-reader, nesting-disciplined, provenance-stamped content that the named competitors (curated awesome-lists) do not attempt.
- **Now true, as of M0:** licensed, CI-enforced, decision-recorded, and living at an address that describes it (`templates/`, not `_local/templates/`).
- **Still on credit:** "agent-native" (no machine consumption path exists, so no agent can select a bundle deterministically) and "reference implementation" (untagged, 4 of 205 types, zero external users).

Keep this section honest. It is the fastest way to tell whether the roadmap is working.
