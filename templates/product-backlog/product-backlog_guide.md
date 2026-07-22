# Guide: Product Backlog (operator card)

Fast reference for using the product-backlog bundle. For the full reasoning, history, and sources, read
[`product-backlog_companion.md`](product-backlog_companion.md).

## When to use

- You have a **team delivering against a product** and need one ordered, shared list of what to do next.
- The work comes from **more than one source** (discovery, stakeholder requests, bugs, tech debt) and
  needs to be sequenced against each other in one place.
- You have a **Product Goal** (or can write one) that the work should serve.
- You want the top of the list **continuously sprint-ready** so planning is a selection, not a scramble.

## When NOT to use

- **You have no goal and no owner.** A backlog with no Product Goal above it and no single owner of the
  order is a feature factory with a sort order. Write the goal first, or you are just collecting requests.
- **You are describing strategy, not sequencing work.** That is a **roadmap** (strategic, outcome-focused),
  not a backlog (tactical, output-focused). Keep them separate; derive the backlog from the roadmap's next
  goal, not the reverse.
- **You are a pure Kanban team.** The Kanban Method manages uncommitted work as "options" upstream of a
  commitment point, not as a standing ordered backlog. If you limit WIP and pull, you may not want a
  backlog at all.
- **You are capturing a decision or a design.** Those are an [ADR](../adr/adr_guide.md), an
  [RFC](../rfc/rfc_guide.md), or a design doc, not backlog items.

## Backlog or roadmap? (the question people actually have)

| | **Product Backlog** | **Product Roadmap** |
|---|---|---|
| Answers | "What work, in what order, next?" | "Where is the product going, and why?" |
| Focus | Tactical, **output** (items to build) | Strategic, **outcome** (goals to achieve) |
| Horizon | Now to a few sprints (top); coarse below | Quarters to a year |
| Owner's act | Ordering the list | Setting the goals |
| Feeds | The sprint backlog | The product backlog |

They are a sequence, not a choice: the roadmap's next goal **scopes** the backlog. The failure is a
roadmap that is secretly a feature list, which makes the backlog a feature factory.

## Pick a variant

- **Lean** (default): Product Goal, Backlog Items, Ordering Rationale, Refinement and Readiness. A complete
  working backlog for a single team with one clear goal.
- **Full**: adds a Prioritization Framework, Dependencies and Risks, and Backlog Health and Metrics. Use it
  when multiple teams or stakeholders dispute the order, there are real cross-team dependencies, or the
  list is large enough that its health must be measured.

Grow lean into full by adding sections; never reorder the shared ones. The scaling signal is **scale and
contention**, not the age of the product.

## Quality rubric (self-grade)

- [ ] There is **one measurable Product Goal** at the top, and the backlog serves it.
- [ ] The list is **genuinely ordered** (a true sequence, 1 = next), not just bucketed by priority label.
- [ ] The **top items are sprint-ready** (small, clear, testable) and the **bottom items are coarse** (the
      iceberg), not everything detailed to the same depth.
- [ ] Each item states the **value or problem it serves**, not just a feature name.
- [ ] The **ordering rationale is stated** and accounts for risk and dependencies, not only raw value.
- [ ] Refinement is **continuous and shared**, and readiness is a **lightweight heuristic**, not a rigid
      stage-gate.
- [ ] (Full) The **prioritization framework**, if any, informs the order without overriding judgment.
- [ ] (Full) **Dependencies are explicit**, and risky assumptions are ordered to be retired early.
- [ ] (Full) The backlog's **health is measured** (size, age, pull-depth) and there is an **archive rule**.
- [ ] The backlog is **not just growing**: stale items are archived, not hoarded.

## Named anti-patterns (the usual wrecks)

1. **The feature factory.** A backlog of pre-decided features with no Product Goal, so the team ships
   output that moves no outcome. Write a measurable goal and filter items against it.
2. **Backlog bankruptcy.** A backlog that only grows, spanning years, most of it never pulled. Delete
   aggressively; archive is recoverable, lost focus is not.
3. **Must-have inflation.** Under MoSCoW, everything becomes a "Must," which defeats the framework. Force a
   true order even within a priority band.
4. **The rigid Definition of Ready.** A readiness checklist enforced as a stage-gate, reintroducing the
   phase-gate bureaucracy agile removed. Keep readiness a heuristic.
5. **Velocity as a target.** Using story points to compare teams or push speed, which drives teams to skimp
   on quality. Estimate to plan, not to pressure.
6. **Ordering by loudest stakeholder.** Letting whoever pushes hardest set the order, instead of a stated
   principle. That is the "backlog administrator" failure in miniature.

## No paired skill (yet)

There is **no `deliver-product-backlog` skill** in the product-on-purpose org today, so this bundle's
`pairs_with` is empty. Until one exists, this template is filled by hand.
