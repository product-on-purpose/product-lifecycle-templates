# History: Epic bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-09-02

- Initial Epic bundle. Member of the `delivery-docs` family, alongside `prd`, `user-stories`,
  `acceptance-criteria`, `release-notes`, `product-backlog`, and `sprint-backlog`. Catalog entry 31.
  Conforms to the [delivery-docs contract](../../docs/internal/contracts/delivery-docs.md) (phase
  `deliver`, `beta`, sizes `[lean, full]`).
- **Scope: the epic as a document, not a tracker record.** The companion's orientation section makes the
  case: every tracker surveyed ships an epic as fields on a work-item panel, so this bundle exists only for
  what a form does not carry, why the body of work exists, who it serves, what is deliberately left out,
  and what it sits under. Teams whose epic lives entirely in one tool's short-lived record should keep
  using that record and write only the narrative summary and exclusions here.
- **Methodology lineage surfaced, not flattened.** Four of five methodologies surveyed have no epic at all:
  Scrum substitutes the Product Goal and ongoing refinement, XP substitutes a time-box rule on the story
  itself, the Kanban Method has no product-specific unit, and LeSS Huge partitions the backlog by
  Requirement Area instead of adding a size tier. SAFe is the outlier and formalizes the artifact heavily,
  with an MVP, a Lean business case, and a named accountable Epic Owner. `methodology` is set to
  `SAFe-lineage` on that basis: the one framework that actually defines the word, everywhere else a
  vocabulary borrowed from a tool rather than a method.
- **Variants: `lean` and `full`.** Lean carries Title and Narrative Summary, Goal and Context, Scope, Child
  Stories, and Acceptance Criteria, enough to state what the work is, why it exists, and what closes it, for
  a single-team epic living inside one tool. Full adds Out of Scope, Dependencies, and Link Upward for work
  that crosses teams, carries real dependencies, or needs a stated position above it. Nesting verified:
  lean's H2 headings are a strict ordered subset of full's.
- **The sharpest teaching points**, carried through companion, guide, and example: (1) the founding
  definition (a single oversized story, destined to split and disappear) is narrower than today's common
  container usage, and Cohn himself flags that departure; (2) an epic is a record in its native habitat, not
  a narrative document, so this bundle is deliberately additive to the tracker rather than a replacement for
  it; (3) the big-story-versus-different-object debate runs through the whole methodology lineage and is
  surfaced rather than resolved.
- **`pairs_with: []`.** There is no `deliver-epic` skill in pm-skills (checked against
  `tools/known-skills.txt`, 2026-09-02).
- **`related_templates: [user-stories, product-backlog, product-roadmap]`.** An epic's child stories are the
  `user-stories` bundle's subject; a backlog orders items that may themselves be epics or their stories; a
  roadmap is the catalog's other named home for epic-level "roadmapping" work.
- Companion researched across the methodology lineage above plus tracker practice (Jira, Azure Boards, Aha!,
  and others) documented in `epic_research-log.md`, with retrieval status per source. Nothing not
  fetched-and-verified is quoted.
- Status: `beta`. Gate-green, zero real usage by anyone other than the author.
