---
title: "Saved Views: story set"
doc_type: user-stories
size: full
owner: "Priya Nair (PM, Reporting)"
status: in-review
doc_version: "0.2.0"
created: "2026-06-18"
updated: "2026-06-30"
related_links:
  - "PRD: Saved Views for Dashboards (prd_example.md)"
source_template: user-stories
source_template_version: 0.1.0
---

<!--
Worked example for the User Story bundle. It shows three things for the same "Saved Views" feature used
in the PRD example: a lean card, a fully scaffolded story, and the same need as a job story for
contrast. Figures marked "illustrative" are made up for the example.
-->

# Saved Views: story set

Epic: Saved Views (see the PRD example). Below: one lean card, one full story, and a job-story variant.

---

## Lean card

## Story

As a recurring analyst, I want to save my current dashboard filters as a named view, so that I can
return to exactly this slice tomorrow without rebuilding it.

## Acceptance criteria

- I can name and save the current filters, date range, and visible columns as a view.
- The saved view appears in my list of views for this dashboard.

## Notes and open questions

Parent epic: Saved Views. Prototype: figma.com/acme/saved-views (illustrative).

---

## Full story

## Story

As a recurring analyst, I want to set one of my saved views as the default for a dashboard, so that the
dashboard opens the way I work instead of in its generic default state.

## Description and context

Follows from the Saved Views PRD. Depends on a view already existing (the save story above). The default
is per-user, not per-dashboard, per the Q1 storage decision.

## Acceptance criteria

- I can mark exactly one of my views as the default for a given dashboard.
- When I open that dashboard, my default view loads instead of the generic default.
- If my default view references a filter that no longer exists, the dashboard loads the valid parts and
  tells me which filter is missing.

## INVEST check

- [x] Independent: depends only on the save-view story, which is a sequenced prerequisite, not a sibling.
- [x] Negotiable: how "default" is surfaced in the UI is open.
- [x] Valuable: removes the daily re-filtering tax for recurring analysts.
- [x] Estimable: team sized it at 3 points (illustrative).
- [x] Small: fits one iteration.
- [x] Testable: criteria above are observable.

## Estimate and sizing

3 story points (illustrative), high confidence; the storage and load paths already exist.

## Dependencies

- Save-view story must ship first (provides the view to set as default).
- Per-user preferences storage (shipped Q1).

## Notes and open questions

Open: should a Team Lead be able to set a team default, or only personal defaults? Owner: Priya, needed
before Phase 2.

---

## Same need, as a job story (for contrast)

When I open a dashboard I check every morning, I want it to already show my usual region and date range,
so I can start reading the numbers instead of rebuilding the filters first.

<!--
Note how the job story drops the "recurring analyst" role and leads with the situation ("every morning")
and motivation. Use this form when the situation is the crux; use the role-based story when the role is
what varies. See the companion, section 6.
-->
