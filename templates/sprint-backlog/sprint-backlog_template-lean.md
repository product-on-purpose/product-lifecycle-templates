---
title: "{{sprint_name}} Sprint Backlog"
sprint: "{{sprint_name}}"
team: "{{team_name}}"
dates: "{{start_date}} to {{end_date}}"
status: "{{status}}"
doc_type: sprint-backlog
size: lean
source_template: sprint-backlog
source_template_version: 0.1.0
---

<!--
LEAN SPRINT BACKLOG. The whole artifact for most sprints: the Sprint Goal (why), the items you selected
(what), and the plan for delivering them (how). To grow it into a full sprint backlog (see
sprint-backlog_template-full.md), ADD sections; never rename or reorder the ones below, because the full
variant is a strict superset of this one.

A SPRINT BACKLOG IS THE DEVELOPERS' LIVING PLAN, NOT A CONTRACT. It is "by and for the Developers": the
Product Owner orders the product backlog and proposes the goal, but the Developers own this plan. It is a
FORECAST, not a promise to ship exactly these items; the one thing you commit to is the SPRINT GOAL, which
fixes the objective while leaving the exact work flexible. Keep it updated throughout the sprint. See
sprint-backlog_companion.md sections 1 and 6.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   sprint-backlog_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid. For the table, PRIORITY explains the legend and ROW HINT says what a
   good row contains.
2. Replace each {{placeholder}} with your content. Select the goal first, then the items that serve it.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This is a living document, updated as you learn, but before you first share it: self-grade against
   sprint-backlog_guide.md, then DELETE every HTML comment. They are guidance, not content.
-->

# {{sprint_name}} Sprint Backlog

## Sprint Goal

<!-- WHAT  The single objective for this sprint: the one outcome that makes the sprint worthwhile, stated
           as a goal, not a list of items.
     WHY   The Sprint Goal is the sprint's "why" and the thing you actually commit to. It gives the work
           coherence and it is the source of your flexibility: because you commit to the objective, the
           exact items can change as you learn. Select it FIRST, then the items that serve it. Deep dive:
           sprint-backlog_companion.md section 3 (Anatomy > Sprint Goal).
     ASK   What is the one objective of this sprint? Why is it worth doing now? How will we know we met
           it? Could a reasonable person tell whether we achieved it?
     GOOD  "A Recurring Analyst can save the current dashboard state as a named view and reopen it, in one
           click, across sessions."
     WEAK  "Finish SV-1, SV-2, and SV-3." (a list of items, not an objective; nothing to renegotiate scope
           against)
     TRAP  Writing the goal as the item list. If the goal is just "do these tickets", you have no basis to
           drop or swap an item mid-sprint, which is the whole point of committing to a goal. -->

{{sprint_goal}}

## Selected Items

<!-- WHAT  The Product Backlog items the Developers pulled into this sprint to meet the goal, ordered by
           their contribution to it. Drawn from the top of the product backlog, not invented here.
     WHY   These are your forecast of what will get done, informed by the goal and your capacity. They are
           a subset of the product backlog, not a copy of it. Deep dive: sprint-backlog_companion.md
           section 3 (Anatomy > Selected Items).
     ASK   Which product-backlog items serve the goal? Are they small enough to finish this sprint? Is each
           one clear enough to start? Who pulls each (or does the team pull)?
     PRIORITY  Order the rows by contribution to the Sprint Goal (top = do first). This is a forecast, not
           a ranked contract.
     ROW HINT  A good row: the item's id (from the product backlog), a short title, its estimate, and a
           status you can update daily.
     GOOD  | SV-1 | Persist a saved view (storage) | 5 | In progress |
     WEAK  | | "Views stuff" | | (no id, no estimate, no status; cannot be tracked or traced to the backlog)
     TRAP  Copying the whole product backlog in, or inventing items here that are not in it. The sprint
           backlog draws a sprint-sized subset from the product backlog; it does not duplicate or bypass
           it. -->

| Item | Title | Estimate | Status |
|---|---|---|---|
| {{item_id}} | {{item_title}} | {{estimate}} | {{item_status}} |

## Delivery Plan

<!-- WHAT  The actionable plan for turning the selected items into a done increment: the "how", at enough
           detail to inspect progress every day. Often the work is broken into tasks.
     WHY   The plan is what makes daily progress visible and re-plannable. The Scrum Guide requires only
           that it be "actionable" and detailed enough for the Daily Scrum; it prescribes no task format,
           and the plan is meant to change as you learn. Deep dive: sprint-backlog_companion.md section 3
           (Anatomy > Delivery Plan).
     ASK   What tasks does each item break into? What is the sequence and who is doing what? What must be
           true for an item to be "done" (does it meet the Definition of Done)? What do we update daily?
     GOOD  "SV-1: migration for the saved_view table (done), repository + API (in progress), tests. SV-2:
           capture-current-state UI, save endpoint, acceptance tests. Board updated at the Daily Scrum;
           each item is done only when it meets the team DoD."
     WEAK  "Build the features." (no tasks, no sequence, nothing to inspect day to day)
     TRAP  Over-specifying the plan up front. It is the part most certain to change, so plan enough to
           see movement, not a fixed task schedule you will spend the sprint defending. -->

{{delivery_plan}}
