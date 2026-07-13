# STATE

> The single source of current truth for this repository. Update this file in the same commit as any milestone exit, release, or status change. Plans and briefs are dated projections; where they disagree with this file, this file wins. (Introduced by the 2026-07-10 audit, finding G-01: the implementation plan's progress table went stale within days of being written.)

Last updated: 2026-07-11

## Built and true today

- Bundles: 4 of 27 Tier-1 catalog types (prd, user-stories, acceptance-criteria, release-notes), all 8 files each, family delivery-docs, status beta, template_version 0.1.0.
- Governance gate: `_local/tools/check-bundles.py`, 6 checks, local-only, passing (last run 2026-07-10, exit 0).
- Atlas: 205-type interactive map at `_local/atlas/atlas.html`.
- Methodology v0.2.0 (draft status) governs authoring.
- Audit corpus: `_local/audit/2026-07-10_fable-audit/` (report, roadmap, specs, this kit).

## Not built (deliberately visible)

- No CI on push. No LICENSE file. No version tags or CHANGELOG. No distribution surface beyond git clone. No family contract file. No metadata schema. No efficacy evals. No real usage cycle yet (zero non-author fills).

## Next milestone

- M0 credibility floor (one day): LICENSE, ci.yml, hygiene sweep, plan truth-up, adopt the ADRs in this kit, methodology eight-file fix. Definition in `_local/audit/2026-07-10_fable-audit/10_roadmap-expanded.md`.

## Open decisions (with ages)

- D1 generator: open since 2026-06-29, correctly gated on usage.
- D2 skills-CLI install test: open since 2026-06-29; 30-minute cost; scheduled in M1.
- D3 agentskills.io resource type: open since 2026-06-29; 1-hour read; scheduled in M1.
- D4 regulated tier appetite: open since 2026-06-29.
- HY-2 scaffold graduation: open since 2026-07-02; decides in M2.
- VL-1 business model, VL-3 maintenance cadence: open since 2026-07-02.
