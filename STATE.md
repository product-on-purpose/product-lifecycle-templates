# STATE

> **The single source of current truth for this repository.** Update this file in the same commit as any milestone exit, release, or status change.
>
> Plans and briefs are dated projections. Where they disagree with this file, **this file wins**.
>
> This file exists because of audit finding G-01: the implementation plan's progress table said "Not started" for all seven phases while two of them were demonstrably complete, and it went stale within a week of being written. A plan that lies about the tree is worse than no plan. The fix is not "remember to update the plan"; it is to have one short file that is cheap to keep honest and that outranks everything else.

**Last updated:** 2026-07-14 (ADR bundle shipped, opening the `decision-docs` family; M0 credibility floor executed; HY-2 scaffold graduation closed; gate size-contract rework; decision records conformed to MADR v4)

---

## Built and true today

| What | State |
|---|---|
| **Bundles** | 5 of 27 Tier-1 catalog types. Family `delivery-docs`: `prd`, `user-stories`, `acceptance-criteria`, `release-notes`. Family `decision-docs`: `adr`. Eight files each. Status `beta`, `template_version` 0.1.0. |
| **License** | Apache-2.0, granted at the repo root. Copyright Jonathan Prisant. |
| **Governance gate** | `tools/check-bundles.py`, six checks (files, dashes, nesting, clean example, citation resolution, meta size contract). **Passing locally** on all five bundles. **NOT running in CI** (see below). |
| **Decision records** | `docs/internal/decisions/`, thirteen ADRs in [MADR v4](https://github.com/adr/madr) format, plus a README documenting the convention. All accepted. Matches the org standard used by `agent-config-toolkit` and scaffolded by `jp-init-project`. |
| **Layout** | The library lives at `templates/` (flat, by document type), the gate at `tools/`, the atlas at `atlas/`, and the planning, strategy, catalog, roadmap and decision records at `docs/internal/`. Decision HY-2 (scaffold graduation) closed 2026-07-12; the `_local/` split closed 2026-07-14 ([ADR 0013](docs/internal/decisions/0013-local-split-and-going-public.md)). |
| **Atlas** | 205-type interactive catalog map at `atlas/atlas.html`. |
| **Methodology** | v0.2.2 (`templates/methodology.md`), status draft. Governs authoring. |
| **Master catalog** | [`docs/internal/catalog.md`](docs/internal/catalog.md). 205 types, 27 at Tier 1. Cited by the methodology and by every bundle companion. **Its size calls are hypotheses, not facts** (see EC-2 below). |
| **Audit corpus** | `_local/audit/2026-07-10_fable-audit/` on the maintainer's disk. **Deliberately NOT in git** (see [ADR 0013](docs/internal/decisions/0013-local-split-and-going-public.md)); its two load-bearing artifacts were promoted to [`docs/internal/roadmap.md`](docs/internal/roadmap.md) and [`docs/internal/contracts/delivery-docs.md`](docs/internal/contracts/delivery-docs.md). |

## Broken right now

**CI has never once run.** `.github/workflows/ci.yml` is correct (verified against a clean clone of the pushed commit), Actions are enabled, and the gate passes locally on all five bundles. But every run since 2026-07-13 has failed in 3-4 seconds with the `gate` job executing **zero steps**, which is the signature of a job that never got a runner: this repo is **private and out of Actions minutes**. `pm-skills`, public in the same org, runs its CI normally.

So the gate is real, and "enforceable, not aspirational" is currently **false in CI and true only on a developer's machine.** Nothing stops a bad bundle from being merged. [PR #1 (M0: the credibility floor)](https://github.com/product-on-purpose/product-lifecycle-templates/pull/1) has been open and red since 2026-07-13 for this reason and no other.

This entry exists because until 2026-07-14 the row above claimed the gate "**Runs in CI** on every push to `main` and every pull request. Passing." That was false the day it was written. STATE.md exists because of audit finding G-01, *a plan that lies about the tree is worse than no plan*, and it had started doing precisely that. The fix is a visibility decision, not a code change.

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
(2026-07-14) surfaced two defects outside this repo. Both are **recorded, not silently patched**,
because a template library that quietly edits its neighbors is worse than one that reports.

| # | Finding | Where it lives | Status |
|---|---|---|---|
| **EC-1** | **`develop-adr` (pm-skills) ships a Nygard-format ADR template**, diverging from the MADR v4 convention the org standardized on for its own decision records (mandated by `jp-init-project`, adopted here by [ADR 0011](docs/internal/decisions/0011-madr-v4-at-docs-internal-decisions.md), in use by `agent-config-toolkit` and `thinking-framework-skills`). An agent invoking that skill inside an org repo produces records in the wrong format. This bundle follows MADR and ships a Nygard-to-MADR mapping table in `adr_guide.md` so the two interoperate. | `pm-skills`, `.claude/skills/develop-adr/references/TEMPLATE.md` | Open, for the pm-skills maintainer |
| **EC-2** | **Master catalog entry 64 (ADR) classifies the type as single-size ("S only"). It is wrong.** MADR itself ships a minimal template and a full template as separate files, which is decisive evidence from the standard's own maintainers that the type earns two weights. The bundle ships `lean` + `full`. The catalog should be corrected at the source. | [`docs/internal/catalog.md`](docs/internal/catalog.md), entry 64 | Open |

Worth noting what EC-2 implies: **the catalog's size calls are hypotheses, not facts.** One of the
27 Tier-1 entries has now been checked against primary evidence and did not survive. The other 26
have not been checked. Expect more corrections as bundles get built, and treat the catalog's
`size_variant` column as a starting guess rather than a specification.

## Gate coverage, stated honestly

The gate automates roughly **half** the methodology's Definition of Done (audit finding D-01). Six checks run; the research-tracing, guidance-comment-structure, companion-skeleton, guide-structure, and history-content clauses have **zero** automation and are human-verified. Gate hardening is roadmap WP-11 in milestone M1.

Two honest qualifiers on that, and they compound. First, the gate covers half the DoD. Second, per [Broken right now](#broken-right-now), **it does not run in CI at all**, so even that half is enforced only when a human remembers to type the command. "Enforceable, not aspirational" is currently aspirational.

**A known gap, found the hard way on 2026-07-14.** The ADR bundle shipped with invalid YAML in both template frontmatters (`decision-makers: [{{decision_makers}}]` parses as a flow mapping with an unhashable key; the fix is to quote the placeholder). **The gate passed it green.** It reads `sizes_available` with a regular expression and never parses YAML as YAML, so "the frontmatter is well-formed" is a DoD clause with no automation behind it at all. The other four bundles were swept and are clean, so this was a one-off defect rather than a systemic one, but the hole is real.

The fix is not free, and the reason is worth understanding: [ADR 0008](docs/internal/decisions/0008-gate-python-local-interim.md) committed the gate to the pure standard library, so it cannot simply import a YAML parser. Adding this check means either taking a dependency (reopening 0008) or hand-rolling a parser (a bad idea). This tension is filed against **WP-11 (gate hardening)** and is exactly the cost that [ADR 0010](docs/internal/decisions/0010-meta-declares-size-contract.md) records as a "Bad, because" consequence of the pure-stdlib constraint. The decision record predicted this bill; it has now arrived.

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
- **Now true, as of M0:** licensed, decision-recorded, and living at an address that describes it (`templates/`, not `_local/templates/`).
- **Claimed too early:** "CI-enforced." The gate exists and passes, but it has never run in CI (see [Broken right now](#broken-right-now)). It is enforced on the maintainer's machine, which is a different and much weaker claim.
- **Still on credit:** "agent-native" (no machine consumption path exists, so no agent can select a bundle deterministically) and "reference implementation" (untagged, 5 of 205 types, zero external users).

Keep this section honest. It is the fastest way to tell whether the roadmap is working.
