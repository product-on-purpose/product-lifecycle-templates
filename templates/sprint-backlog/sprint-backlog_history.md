# History: Sprint Backlog bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-07-21

- Initial Sprint Backlog bundle. **Sixth and final `delivery-docs` member**, completing the family (with
  `prd`, `user-stories`, `product-backlog`, `acceptance-criteria`, `release-notes`), and the third bundle
  of the Tier-1 floor build-out ([ADR 0021](../../docs/internal/decisions/0021-complete-the-tier-1-floor.md)).
  Catalog entry 76. Conforms to the [delivery-docs contract](../../docs/internal/contracts/delivery-docs.md)
  (phase `deliver`, `beta`, sizes `[lean, full]`); gate check K green.
- **Note on family completion:** the buildout-plan originally listed `definition-of-done` as a delivery-docs
  member too, but a DoD is a standing quality standard (`classification: foundation`), which cannot honestly
  be `phase: deliver`; it is reassigned to a standing-standards family (see
  [`buildout-specs.md`](../../docs/internal/buildout-specs.md) decision D-A). So delivery-docs completes at
  sprint-backlog, its sixth phase-`deliver` member.
- **Scope: the Scrum-canonical Sprint Backlog**, anchored on the 2020 Scrum Guide. The companion frames it
  honestly as the **Developers' living forecast** for one Sprint, composed of the Sprint Goal (why) +
  selected items (what) + the delivery plan (how), whose commitment is the Sprint Goal, not the item list.
- **Variants: `lean` and `full`.** Lean is the Scrum Guide's exact three-part composition (Sprint Goal,
  Selected Items, Delivery Plan); full adds the planning apparatus a calibrating or higher-stakes sprint
  earns (Capacity and Forecast, Progress and Tracking, Risks and Carry-over). Nesting verified. The catalog
  lists the type as single-size M; the two-weight split reflects that most sprints need only the lean
  three-part artifact while some earn the heavier planning sections.
- **The sharpest teaching points**, through companion, guide, and example: (1) it is **by and for the
  Developers**, not the Product Owner's list; (2) it is a **forecast, and the commitment is the Sprint
  Goal**, not the items (the 2011 "commitment"-to-"forecast" change and the 2020 reattachment of
  "commitment" to the Sprint Goal are traced in the companion); (3) it is a **Sprint-sized subset drawn
  from the product backlog**, producing an Increment that meets the Definition of Done.
- **Worked example chains one level below the product backlog.** `sprint-backlog_example.md` is a sprint of
  the Reporting Squad drawing its top items (SV-1, SV-2, SV-3) from the
  [Saved Views product backlog](../product-backlog/product-backlog_example.md), so the family reads as one
  traceable set: the product backlog is the ordered whole, and this is one Sprint's forecast against one
  goal.
- **`pairs_with: []`.** There is no `deliver-sprint-backlog` skill in pm-skills (checked against
  `tools/known-skills.txt`, 2026-07-21). Recorded in `sprint-backlog_guide.md`.
- Companion researched 2026-07-21 across three parallel dimensions and 13 tier-ranked sources (see
  `sprint-backlog_research-log.md`). The primary anchor is the 2020 Scrum Guide (with the 2017 edition and
  the official revision history for the composition and commitment/forecast changes). The 2017 PDF was
  fetched through a paraphrasing layer and is cited for the structural contrast only, not quoted; one
  Scrum.org page was url-confirmed-not-read and carries no claim; several claims are flagged contested
  (forecast vs commitment, "yesterday's weather" as an unquoted concept, velocity as a target, sprint-goal
  consent vs acceptance, burndown's role, mid-sprint scope change). Nothing not fetched-and-verified is
  quoted.
- Status: `beta`. Gate-green, zero real usage by anyone other than the author.
