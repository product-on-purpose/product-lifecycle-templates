---
title: "{{sprint_name}} Sprint Backlog"
sprint: "{{sprint_name}}"
team: "{{team_name}}"
dates: "{{start_date}} to {{end_date}}"
status: "{{status}}"
related: ["{{related_docs}}"]
doc_type: sprint-backlog
size: full
source_template: sprint-backlog
source_template_version: 0.1.0
---

<!--
FULL SPRINT BACKLOG. Every section, for a sprint whose planning earns the weight: a team still calibrating
its capacity, a setting where the forecast and tracking must be legible beyond the team, or a sprint with
real dependencies and carry-over risk. Most settled teams do not need this; a lean goal + items + plan on a
board is the whole artifact.

The full variant is a strict superset of the lean one: the shared sections keep their names and order, and
this file only ADDS (Capacity and Forecast, Progress and Tracking, Risks and Carry-over).

A SPRINT BACKLOG IS THE DEVELOPERS' LIVING PLAN, NOT A CONTRACT. It is "by and for the Developers"; it is a
FORECAST, and the one thing you commit to is the SPRINT GOAL, which fixes the objective while leaving the
exact work flexible. Keep it updated throughout the sprint. See sprint-backlog_companion.md sections 1 and 6.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   sprint-backlog_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to
   avoid. For the table, PRIORITY explains the legend and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Select the goal first, then the items that serve it.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This is a living document; before you first share it: self-grade against sprint-backlog_guide.md, then
   DELETE every HTML comment.
-->

# {{sprint_name}} Sprint Backlog

## Sprint Goal

<!-- WHAT  The single objective for this sprint: the one outcome that makes the sprint worthwhile, stated
           as a goal, not a list of items.
     WHY   The Sprint Goal is the sprint's "why" and the thing you actually commit to; it gives the work
           coherence and is the source of your flexibility. Select it FIRST. Deep dive:
           sprint-backlog_companion.md section 3 (Anatomy > Sprint Goal).
     ASK   What is the one objective of this sprint? Why now? How will we know we met it?
     GOOD  "A Recurring Analyst can save the current dashboard state as a named view and reopen it, in one
           click, across sessions."
     WEAK  "Finish SV-1, SV-2, and SV-3." (a list of items, not an objective)
     TRAP  Writing the goal as the item list, so you have no basis to renegotiate scope mid-sprint. -->

{{sprint_goal}}

## Selected Items

<!-- WHAT  The Product Backlog items pulled into this sprint to meet the goal, ordered by contribution to
           it. Drawn from the top of the product backlog.
     WHY   These are the Developers' forecast, informed by the goal and capacity; a subset of the product
           backlog, not a copy. Deep dive: sprint-backlog_companion.md section 3 (Anatomy > Selected Items).
     ASK   Which product-backlog items serve the goal? Are they small enough to finish this sprint? Is each
           clear enough to start?
     PRIORITY  Order rows by contribution to the Sprint Goal (top = do first). A forecast, not a contract.
     ROW HINT  A good row: the item id (from the product backlog), a short title, its estimate, and a
           daily-updatable status.
     GOOD  | SV-1 | Persist a saved view (storage) | 5 | In progress |
     WEAK  | | "Views stuff" | | (no id, no estimate, no status)
     TRAP  Copying the whole product backlog in, or inventing items not in it. Draw a sprint-sized subset;
           do not duplicate or bypass the product backlog. -->

| Item | Title | Estimate | Status |
|---|---|---|---|
| {{item_id}} | {{item_title}} | {{estimate}} | {{item_status}} |

## Delivery Plan

<!-- WHAT  The actionable plan for turning the selected items into a done increment: the "how", at enough
           detail to inspect progress daily. Often broken into tasks.
     WHY   The plan makes daily progress visible and re-plannable; the Guide requires only that it be
           "actionable", and it is meant to change as you learn. Deep dive: sprint-backlog_companion.md
           section 3 (Anatomy > Delivery Plan).
     ASK   What tasks does each item break into? What is the sequence and who does what? What must be true
           for an item to meet the Definition of Done? What do we update daily?
     GOOD  "SV-1: migration (done), repository + API (in progress), tests. SV-2: capture-state UI, save
           endpoint, acceptance tests. Board updated at the Daily Scrum; done means meets the team DoD."
     WEAK  "Build the features." (no tasks, no sequence, nothing to inspect)
     TRAP  Over-specifying up front. The plan is the part most certain to change; plan enough to see
           movement, not a fixed schedule to defend. -->

{{delivery_plan}}

## Capacity and Forecast

<!-- WHAT  How much the Developers can take on this sprint, and the basis for the forecast: capacity
           (plannable hours), velocity (typical story points), holidays/leave, and the buffer for the
           unplanned.
     WHY   The selection is a forecast, and a forecast needs a basis. Capacity and velocity are different
           measures (hours vs story points) and easy to confuse; making the basis explicit is what a
           calibrating team needs. Deep dive: sprint-backlog_companion.md section 3 (Anatomy > Capacity and
           Forecast) and the debates in section 6.
     ASK   What is the team's available capacity this sprint (who is out, what else is committed)? What is
           recent velocity? Are we selecting by velocity or by tasked-out hours? How much buffer did we
           leave for the unplanned?
     GOOD  "Available capacity ~6 dev-days after one person's 2 days of leave. Recent velocity ~18 points;
           we selected 15 to leave slack for the SV-1 migration risk. Basis: capacity (tasked out), with
           velocity as a sanity check."
     WEAK  "We took 20 points because that's our velocity." (velocity used as a target, no capacity check,
           no buffer)
     TRAP  Treating velocity as a target to hit or exceed, or filling to 100% of capacity. Velocity is a
           measure, not a goal, and a sprint with no buffer breaks on the first surprise. -->

{{capacity_and_forecast}}

## Progress and Tracking

<!-- WHAT  How the Developers make progress visible and re-plan daily: the board or chart, the Daily Scrum
           cadence, and how "done" is tracked.
     WHY   Tracking exists to serve the Daily Scrum's re-planning toward the goal, not to produce a
           management report. The 2020 Scrum Guide deprescribed the burndown; pick whatever visualization
           the team will keep current. Deep dive: sprint-backlog_companion.md section 3 (Anatomy > Progress
           and Tracking).
     ASK   What visualization do we use (board, burndown, burn-up), and is it current? How do we re-plan at
           the Daily Scrum? How do we know an item is done (meets the DoD)?
     GOOD  "Kanban board (To do / In progress / In review / Done), updated live; Daily Scrum re-plans the
           day against the Sprint Goal. An item moves to Done only when it meets the team DoD."
     WEAK  "We have a burndown chart." (a chart nobody updates, standing in for actual re-planning)
     TRAP  Turning tracking into a status ritual for managers. The chart is for the team's re-planning; if
           it is maintained for someone outside the team, it has stopped doing its job. -->

{{progress_and_tracking}}

## Risks and Carry-over

<!-- WHAT  The dependencies and risks to the Sprint Goal, and the plan for work that does not finish.
     WHY   Naming the risks to the goal up front is how you protect the commitment (the goal), and deciding
           the carry-over rule keeps unfinished work honest: it returns to the product backlog for
           re-ordering, not silently into the next sprint. Deep dive: sprint-backlog_companion.md section 3
           (Anatomy > Risks and Carry-over).
     ASK   What could stop us meeting the goal (a dependency, an unknown, a person out)? What is the plan if
           an item does not finish? What scope could we renegotiate with the PO without endangering the
           goal?
     GOOD  "Risk: the SV-1 storage migration is unproven; if it slips, we cut SV-3 (still meeting the goal
           with save + reopen). Unfinished items return to the product backlog for the PO to re-order, not
           auto-rolled to next sprint."
     WEAK  "No risks." (on any real sprint, undisclosed rather than absent)
     TRAP  Auto-rolling unfinished items into the next sprint. Carry-over is new information: put it back on
           the product backlog and let the Product Owner re-order it against everything else. -->

{{risks_and_carryover}}
