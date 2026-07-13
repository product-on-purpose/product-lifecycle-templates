# Adoption Kit: Ready-to-Review Drafts for M0

> **[ADOPTED 2026-07-12. THESE COPIES ARE HISTORICAL. DO NOT CITE THEM AS DECISION RECORDS.]**
>
> The canonical decision records now live at [`docs/internal/decisions/`](../../../../docs/internal/decisions/) and `STATE.md` is at the repo root. The copies in this folder are the **proposals as drafted on 2026-07-11**, preserved to show what was put forward before review.
>
> **They have already diverged from the canonical records**, deliberately. Review before adoption caught a material error and one staleness:
>
> - **`decisions/0003-phase-vocabulary.md`**: the draft here claims the pm-skills phase enum has **eight** values, "plus `foundation` and `tool`". That is wrong. pm-skills has a two-axis taxonomy: six `phase:` values, and a separate `classification:` axis (`foundation`/`utility`/`tool`) carried by the 86 skills that have no phase at all. The canonical record states the correct enum and documents the error. Had the draft been adopted as written, it would have instructed the metadata schema to enforce a broken enum.
> - **`decisions/0008-gate-python-local-interim.md`**: the draft's accepted risk says "local-only means zero push protection", which stopped being true when M0 wired CI. The canonical record carries a dated Follow-up.
>
> Where this folder disagrees with `docs/internal/decisions/`, **`docs/internal/decisions/` wins**.

Drafts of the judgment-bearing M0 artifacts (roadmap work packages WP-04 and WP-05), staged here rather than committed to the repo because the ADRs record the **maintainer's** decisions; you ratify, this kit only transcribes.

## How to adopt

1. Review each file; edit anything that misstates the decision or its reasoning.
2. Move into place:
   - `decisions/*.md` to `docs/internal/decisions/`
   - `STATE.md` to the repo root
   - `delivery-docs.contract.md` to `_families/` (or `templates/_families/` per your HY-2 scaffold call; it is referenced by roadmap WP-24)
3. Commit with a message referencing audit finding F-03 (missing ADRs) and G-01 (stale plan).
4. Update the plan's progress table in the same commit (WP-04) so the truth-up and the records land together.

## Contents

| File | What it records | Source transcribed from |
|---|---|---|
| decisions/TEMPLATE.md | MADR-style stub for future decisions | Audit report finding F-03 |
| decisions/0001-repo-and-package-name.md | `product-lifecycle-templates` everywhere; `pm-` prefix dropped | Strategy brief section 5 item 1; plan P1 step 2 |
| decisions/0002-variant-model.md | lean/full descriptive filenames + strict nesting | Strategy brief section 5 item 2; plan P1 step 3 |
| decisions/0003-phase-vocabulary.md | Lowercase phase values matching pm-skills | Strategy brief section 5 item 3; plan P1 step 4 |
| decisions/0004-first-family-and-bundle.md | delivery-docs first; prd first | Strategy brief section 5 item 4; plan P1 step 5 |
| decisions/0005-bundle-ids-doctype-spine.md | **Bundle IDs are bare doc-type handles; phase lives in metadata, never in path or ID.** Not in the audit's list of seven; surfaced during transcription because the plan's intended ADR said IDs would be `deliver-prd` style and practice deliberately diverged (methodology section 2). This records the divergence as the decision it was | methodology.md:41; contrast with plan P1 step 4 |
| decisions/0006-guidance-style-approach-a.md | Enriched HTML comments (Approach A) | _working/README.md; methodology B1 |
| decisions/0007-research-log-as-bundle-artifact.md | Research log is a committed bundle artifact | Methodology DoD; gate ROLES; G6 idea HY-3 |
| decisions/0008-gate-python-local-interim.md | Python local gate as decided interim; supersession condition stated | check-bundles.py docstring; README line 106 |
| delivery-docs.contract.md | The family contract (audit finding B-01, plan AC-12) | Methodology + design spec section 11 + the four bundles' verified shared shape |
| STATE.md | The single current-truth block (audit finding G-01's antidote) | Audit corpus fingerprint |

## Caveat

Dates in the ADR filenames are the dates the decisions were actually made (per the source documents), not the transcription date. If you disagree with any "Consequences" line, that is exactly the review this kit exists for; the Context and Decision sections are faithful to the sources.
