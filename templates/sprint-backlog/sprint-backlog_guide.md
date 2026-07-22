# Guide: Sprint Backlog (operator card)

Fast reference for using the sprint-backlog bundle. For the full reasoning, history, and sources, read
[`sprint-backlog_companion.md`](sprint-backlog_companion.md).

## When to use

- Your team runs **time-boxed Sprints** and needs one place to hold this Sprint's goal, selected items,
  and plan.
- You are at **Sprint Planning** and need to turn a slice of the product backlog into a forecast the
  Developers own.
- You want the day-to-day work **visible and re-plannable** against a single objective.

## When NOT to use

- **You do not run Sprints.** A Kanban or continuous-flow team has no Sprint Backlog; pull work against WIP
  limits on a flow board and forecast with cycle time instead.
- **You need the ordered whole-product list.** That is the [product backlog](../product-backlog/product-backlog_guide.md)
  (strategic, ongoing); the Sprint Backlog is one Sprint's forecast drawn from it.
- **You want a management status report.** The Sprint Backlog is the Developers' working plan, not a report
  for stakeholders. A status update is a different artifact.
- **You are recording a standing quality bar.** "Done" criteria that apply to every increment are a
  Definition of Done, not a Sprint Backlog.

## Sprint backlog or product backlog? (the question people actually have)

| | **Sprint Backlog** | **Product Backlog** |
|---|---|---|
| Scope | One Sprint | The whole product |
| Owner | The **Developers** | The **Product Owner** |
| Commitment | The **Sprint Goal** | The Product Goal |
| Lifespan | One Sprint, then archived | Ongoing, emergent |
| Is | A **forecast** of this Sprint's work | The ordered list all work is drawn from |

The Sprint Backlog is a **Sprint-sized subset** drawn from the top of the product backlog; it never
duplicates or bypasses it.

## Pick a variant

- **Lean** (default): Sprint Goal, Selected Items, Delivery Plan. The Scrum Guide's three-part composition
  (why, what, how). For most settled teams this is the whole artifact, kept live on a board.
- **Full**: adds Capacity and Forecast, Progress and Tracking, and Risks and Carry-over. Use it when the
  team is still calibrating its capacity, the forecast and tracking must be legible beyond the team, or the
  Sprint carries real dependencies and carry-over risk.

Grow lean into full by adding sections; never reorder the shared ones. The scaling signal is **planning
weight**, not Sprint length.

## Quality rubric (self-grade)

- [ ] There is **one Sprint Goal**, written as an objective (an outcome), not a list of items.
- [ ] The goal was **selected first**, and the items were chosen to serve it.
- [ ] The selected items are a **Sprint-sized subset drawn from the product backlog**, each with an id, an
      estimate, and a daily-updatable status.
- [ ] The plan is **actionable and inspectable daily**, not a fixed task schedule to defend.
- [ ] The document reads as a **forecast**, and the only thing framed as a commitment is the **Sprint
      Goal**.
- [ ] The artifact is clearly **the Developers'**, not edited by the Product Owner or a manager.
- [ ] (Full) **Capacity** is stated with a buffer, and velocity is used as a measure, not a target.
- [ ] (Full) **Tracking** is something the team keeps current for its own re-planning, not a manager report.
- [ ] (Full) **Carry-over** returns unfinished work to the product backlog, not automatically to next
      Sprint.
- [ ] It is **kept updated** through the Sprint, not frozen at planning.

## Named anti-patterns (the usual wrecks)

1. **The Product Owner's list.** A Sprint Backlog dictated or edited by the PO or a manager. The
   Developers own the plan; the PO orders the product backlog and proposes the goal.
2. **The forecast as a contract.** Treating the selected items as a promise to ship exactly those, which
   punishes the team for learning. Commit to the Sprint Goal; forecast the items.
3. **Velocity as a target.** Pushing velocity up as a goal, which inflates estimates and erodes quality.
   Velocity is a measure, not a target.
4. **The goalless sprint.** A list of unrelated items with no Sprint Goal, so nothing coheres and there is
   no basis to renegotiate scope.
5. **Over-filling the sprint.** Planning to 100% of capacity with no buffer, so any surprise blows the
   Sprint.
6. **The frozen plan.** Written once at planning and never updated, so it stops being the real-time
   picture it is meant to be.

## No paired skill (yet)

There is **no `deliver-sprint-backlog` skill** in the product-on-purpose org today, so this bundle's
`pairs_with` is empty. Until one exists, this template is filled by hand.
