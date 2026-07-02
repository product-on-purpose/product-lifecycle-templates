---
title: "Acceptance criteria: set a default saved view"
doc_type: acceptance-criteria
size: full
owner: "Priya Nair (PM, Reporting)"
status: in-review
doc_version: "0.1.0"
created: "2026-06-22"
updated: "2026-06-30"
related_links:
  - "Story: set a default saved view (user-stories_example.md)"
  - "PRD: Saved Views for Dashboards (prd_example.md)"
source_template: acceptance-criteria
source_template_version: 0.1.0
---

<!--
Worked example for the Acceptance Criteria bundle. These are full acceptance criteria for the "set a
default saved view" story from the user-stories example. It shows rule-based criteria, Given/When/Then
scenarios, an explicit edge case (a missing filter), and a non-functional criterion. Figures marked
"illustrative" are made up for the example.
-->

# Acceptance criteria: set a default saved view

## Story reference

As a recurring analyst, I want to set one of my saved views as the default for a dashboard, so that the
dashboard opens the way I work instead of in its generic default state. (See user-stories_example.md.)

## Acceptance criteria

- [ ] I can mark exactly one of my saved views as the default for a given dashboard.
- [ ] Marking a new view as default un-marks the previous default automatically.
- [ ] Opening the dashboard loads my default view instead of the generic default state.
- [ ] The default is mine alone; it does not change the default for any other user.

## Scenarios (Given / When / Then)

**Scenario: default view loads on open**
- Given I have set "EMEA, last 30 days" as my default view for the Sales dashboard
- When I open the Sales dashboard
- Then it loads with the "EMEA, last 30 days" filters applied, not the generic default

**Scenario: switching the default**
- Given "EMEA, last 30 days" is currently my default
- When I mark "APAC, last 7 days" as the default
- Then "APAC, last 7 days" becomes my default and "EMEA, last 30 days" is no longer marked default

## Edge cases and negative paths

- [ ] Given my default view references a filter that has since been deleted, when I open the dashboard,
      then it loads the still-valid filters and shows a clear message naming the missing filter, rather
      than failing to load.
- [ ] Given I have no default set, when I open the dashboard, then it loads the generic default state
      with no error.

## Non-functional criteria

- [ ] Loading a default view on dashboard open completes within 1 second at p95 (illustrative target).
- [ ] The "set as default" control is keyboard-operable and screen-reader labeled (WCAG 2.2 AA).

## Out of scope and notes

Out of scope: team-level defaults (a Team Lead setting a default for everyone) are a separate, open
decision and not covered here. Assumes per-user preference storage (shipped Q1). Does not cover sharing,
which has its own story.
