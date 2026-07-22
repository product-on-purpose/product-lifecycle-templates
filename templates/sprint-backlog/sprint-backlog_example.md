---
title: "Sprint 24 Sprint Backlog"
sprint: "Sprint 24"
team: "Reporting Squad"
dates: "2026-07-13 to 2026-07-24"
status: active
related: ["../product-backlog/product-backlog_example.md (Saved Views product backlog)", "../prd/prd_example.md (Saved Views for Dashboards PRD)", "../user-stories/user-stories_example.md (Saved Views user stories)", "../release-notes/release-notes_example.md (the release note the shipped increment surfaces in)"]
doc_type: sprint-backlog
size: full
source_template: sprint-backlog
source_template_version: 0.1.0
---

<!--
This is a worked example for the sprint-backlog bundle. It is a realistic, fully filled full-variant Sprint
Backlog for one sprint of the Reporting Squad, drawing its selected items from the top of the Saved Views
product backlog (see product-backlog_example.md). Figures are illustrative. A Sprint Backlog is a living
document; this is a snapshot mid-sprint. This is a representative, not exhaustive, example: a real sprint
will differ in item count, estimating style, and planning depth. Use it as a model of shape and tone, not
as a source of facts.
-->

# Sprint 24 Sprint Backlog

## Sprint Goal

**A Recurring Analyst can save the current dashboard state (filters, date range, columns) as a named view
and reopen it in one click, across sessions.**

This is what the sprint is for. It is the one thing the Reporting Squad commits to; the items below are the
forecast of how we expect to get there, and the exact list may change as we learn, as long as save-and-
reopen lands.

## Selected Items

Selected from the top four items (Ranks 1 to 4) of the
[Saved Views product backlog](../product-backlog/product-backlog_example.md), then ordered *here* by
contribution to the Sprint Goal rather than by backlog rank: SV-1 through SV-3 serve the goal; BUG-231 is
committed non-goal work (a cheap, painful production bug) and is the first thing we cut if capacity
tightens.

| Item | Title | Estimate | Status |
|---|---|---|---|
| SV-1 | Persist a saved view (new `saved_view` store) | 5 | In progress |
| SV-2 | Save the current dashboard state (filters, date range, columns) as a named view | 5 | To do |
| SV-3 | List a user's views and switch between them in one action | 5 | To do |
| BUG-231 | CSV export drops the last row on reports over 10k rows | 3 | To do |

SV-1, SV-2, and SV-3 together deliver the goal (store, save, reopen). BUG-231 does not serve the goal; it
is here because it is cheap and is losing customer data now.

## Delivery Plan

- **SV-1 (storage):** migration for the `saved_view` table (done); repository and CRUD API (in progress);
  unit and integration tests; wire the feature flag. An item is done only when it meets the team Definition
  of Done.
- **SV-2 (save):** "save current view" control in the dashboard header; capture the current filter/date/
  column state into the config payload; POST endpoint; acceptance tests against the PRD's FR-1.
- **SV-3 (reopen):** views list and one-click switch; rehydrate dashboard state from a saved view; handle a
  view that references a since-deleted filter (apply what resolves).
- **BUG-231:** reproduce on a >10k-row export; fix the off-by-one in the streaming writer; regression test.

The board is updated live and re-planned at each Daily Scrum against the Sprint Goal.

## Capacity and Forecast

- **Capacity:** a three-developer squad; ~7 net developer-days available this sprint after one engineer's
  2 days of leave, the standing on-call rotation, and sprint ceremonies.
- **Velocity:** the squad's recent average is ~18 points over the last eight sprints. We selected 18 points
  (SV-1 5 + SV-2 5 + SV-3 5 + BUG-231 3), tasked out against capacity, with velocity as a sanity check.
- **Basis:** capacity-driven (we tasked the work out and confirmed it fits the plannable days); velocity
  only confirmed the load is in the normal range. This is a **forecast**, not a guarantee.
- **Buffer:** we deliberately left roughly a day of slack for the SV-1 migration risk and the unplanned;
  velocity is a measure we watch, not a number we push to hit.

## Progress and Tracking

- **Board:** a Kanban board (To do / In progress / In review / Done), updated live by whoever moves a card.
- **Daily Scrum:** the squad re-plans the day against the Sprint Goal; the board is the shared picture, not
  a report for anyone outside the team.
- **Done:** an item moves to Done only when it meets the team Definition of Done (coded, reviewed, tested,
  behind the flag, acceptance criteria met). We are not using a burndown chart this sprint; the board is
  enough for a four-item sprint.

## Risks and Carry-over

- **Risk to the goal:** SV-1 (the new storage) is the unproven piece, and the whole goal depends on it, so
  it is sequenced first and de-risked early. If SV-1 slips badly, the Sprint Goal itself is at risk and we
  raise it with the Product Owner (Priya Nair) at once rather than quietly dropping stories.
- **Scope we can renegotiate without endangering the goal:** BUG-231 is non-goal work; if capacity
  tightens, we cut it first and it returns to the product backlog. The goal (save-and-reopen) stays.
- **Carry-over rule:** any item that does not finish returns to the **product backlog** for the Product
  Owner to re-order against everything else, not automatically into Sprint 25. Unfinished work is new
  information, not a debt silently rolled forward.
