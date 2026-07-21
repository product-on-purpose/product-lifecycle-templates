# History: Product Backlog bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-07-21

- Initial Product Backlog bundle. Fifth member of the `delivery-docs` family, alongside `prd`,
  `user-stories`, `acceptance-criteria`, and `release-notes`, and the second bundle built under the Tier-1
  floor build-out ([ADR 0021](../../docs/internal/decisions/0021-complete-the-tier-1-floor.md)). Catalog
  entry 75. Conforms to the [delivery-docs contract](../../docs/internal/contracts/delivery-docs.md)
  (phase `deliver`, `beta`, sizes `[lean, full]`); gate check K green.
- **Scope: the Scrum-canonical, goal-anchored product backlog**, framed honestly. The companion's sections
  1, 5, and 6 make the case: the backlog is Scrum-canonical (the 2020 Guide's one of three artifacts, with
  the Product Goal as its commitment) but is a general agile concept with real variants (Kanban's
  "options", SAFe's ART/Portfolio backlogs, XP's story cards) and is under sustained outcome-over-output
  pressure. The bundle teaches the ordered, emergent, goal-anchored form with the debates surfaced, not
  flattened.
- **Variants: `lean` and `full`.** The catalog lists M/L (living); the two-weight split fits the artifact.
  Lean is the four sections every backlog needs: Product Goal, Backlog Items (the ordered table), Ordering
  Rationale, and Refinement and Readiness. Full adds the management apparatus a larger or contested backlog
  earns: a Prioritization Framework, Dependencies and Risks, and Backlog Health and Metrics, plus a richer
  item table (ID, priority signal, depends-on). Nesting verified: lean's H2 headings are a strict ordered
  subset of full's.
- **The sharpest teaching points**, carried through companion, guide, and example: (1) the backlog is
  **ordered, not merely prioritized** (the 2020 Scrum Guide's deliberate word choice, so risk and
  dependencies can override a single value score); (2) a backlog is **output, so anchor it to a Product
  Goal** or it becomes a feature factory; (3) **backlog versus roadmap** (tactical output list versus
  strategic outcome plan). These run through the guide's comparison table and anti-patterns.
- **Worked example chains with the delivery-docs family.** `product-backlog_example.md` is the Reporting
  team's backlog scoped by the same "Saved Views for Dashboards" Product Goal the `prd`, `user-stories`,
  `acceptance-criteria`, and `release-notes` examples share. It shows the backlog as the tactical center of
  the family: the Saved Views epic and its stories sit ordered among a production bug, tech debt, and a
  de-risking spike, with an explicit ordering rationale (dependency and risk first) and the storage-model
  decision flagged for an ADR (chaining to the `sdd` design-doc example's treatment of the same choice).
- **`pairs_with: []`.** There is no `deliver-product-backlog` skill in pm-skills (checked against
  `tools/known-skills.txt`, 2026-07-21). Recorded as context in `product-backlog_guide.md`.
- Companion researched 2026-07-21 across five parallel dimensions and 36 tier-ranked sources (see
  `product-backlog_research-log.md` for per-source retrieval status). The primary anchor is the 2020 Scrum
  Guide (with the 2017 edition and the official revision history to trace the "prioritized" to "ordered"
  and Product Goal changes). Two Atlassian how-to pages were confirmed live but not read and carry no
  claim; several claims are flagged contested (ordered vs prioritized as a meaningful distinction, who
  coined DEEP, refinement cadence, the outcome-over-output debate camps, no-estimates vs story points, the
  Definition of Ready, and the backlog-bankruptcy survey figures). Nothing not fetched-and-verified is
  quoted.
- Status: `beta`. Gate-green, zero real usage by anyone other than the author.
