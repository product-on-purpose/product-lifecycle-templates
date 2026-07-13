---
title: "Saved Views for Dashboards"
doc_type: prd
size: full
owner: "Priya Nair (PM, Reporting)"
status: in-review
doc_version: "0.3.0"
created: "2026-06-12"
updated: "2026-06-30"
related_links:
  - "Prototype: figma.com/acme/saved-views (illustrative)"
  - "Discovery readout: Reporting friction study, 2026-05"
source_template: prd
source_template_version: 0.1.0
---

<!--
This is a worked example for the PRD bundle. It is a realistic, fully filled full-variant PRD for a
single feature. Figures marked "illustrative" are made up for the example and would be real data in a
live PRD. Use it as a model of shape and tone, not as a source of facts.
-->

# Saved Views for Dashboards

## Summary

Analysts in our product repeatedly rebuild the same dashboard filters every time they return to a
report. "Saved Views" lets a user capture a dashboard's current filter, date range, and column setup
as a named view they can reopen in one click and share with teammates. The outcome we want: analysts
spend their time reading data, not reconstructing the lens to see it.

## Context and background

This serves the FY26 "Time to Insight" company goal (reduce the median time from opening a report to
acting on it). The 2026-05 Reporting friction study found that re-filtering was the single most
frequent repeated action in the dashboard, ahead of export and share. We have deferred this twice
because filtering "worked"; the study reframed it from a feature gap to a recurring time tax. Nothing
about the data model blocks it now that per-user preferences storage shipped in Q1.

## Problem

Analysts who monitor the same slice of data (one region, one product line, last 30 days) must re-apply
that filter set on every visit, because the dashboard always opens in its default state. In the
friction study, 9 of 12 interviewed analysts described manually rebuilding filters several times a day,
and 3 kept a personal text file of "the filters I always use" (illustrative counts from a 12-person
study). The cost is not just minutes; it is broken flow and the risk of analyzing the wrong slice
because a filter was set incorrectly from memory. This matters now because reporting usage has grown
and the repeated-setup tax scales with it.

## Goals and non-goals

**Goals**
- Let a user save the current dashboard state (filters, date range, visible columns) as a named view.
- Let a user reopen a saved view in one action and set one view as their default for a dashboard.
- Let a user share a view with a teammate or team.

**Non-goals**
- Scheduled delivery of a view by email or Slack. Out of scope now; likely a fast follow.
- Cross-dashboard "global" views that span multiple reports. Deliberately not doing this; it raises
  hard scoping and permissions questions we do not need to answer yet.
- Editing the underlying dashboard definition. Saved Views capture state, not structure.

## Target users and personas

Primary: the **Recurring Analyst** persona, an internal or customer analyst who returns to the same
dashboards daily or weekly and works within a stable set of filters. Secondary: the **Team Lead** who
wants their team looking at a consistent, agreed view. Not optimized for the one-time explorer, who
rarely benefits from saving state.

## Solution overview

A "Views" control sits at the top of every dashboard. It shows the active view (or "Default"), and
opens a menu to save the current state as a new view, switch between saved views, set a default, and
share. Saving prompts for a name and a scope (private or shared). The interactive prototype
(figma.com/acme/saved-views, illustrative) is the source of truth for the experience; this document
carries the why, the scope, and the success criteria.

## User stories

- As a Recurring Analyst, I want to save my current filters as a named view, so that I can return to
  exactly this slice tomorrow without rebuilding it.
- As a Recurring Analyst, I want to set a view as my default for this dashboard, so that it opens the
  way I work.
- As a Team Lead, I want to share a view with my team, so that we are all looking at the same numbers.
- As a Recurring Analyst, I want to rename or delete a view I made, so that my list stays meaningful.

## Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | Save the current dashboard state (filters, date range, visible columns) as a named view | Must |
| FR-2 | List a user's saved views for a dashboard and switch between them in one action | Must |
| FR-3 | Set one view as the user's default for a dashboard; that view loads on open | Must |
| FR-4 | Share a view as "shared" so other permitted users of that dashboard can select it | Should |
| FR-5 | Rename and delete views the user owns | Should |
| FR-6 | Indicate when a shared view's underlying dashboard has changed in a way that affects it | Could |

## Non-functional requirements

| Attribute | Target |
|---|---|
| Performance | Switching to a saved view renders in under 1s at p95 on a standard dashboard (illustrative target) |
| Permissions | A shared view never exposes data the recipient could not already access on that dashboard |
| Reliability | A saved view that references a now-deleted filter degrades gracefully (loads what it can, flags the rest) |
| Accessibility | The Views control is fully keyboard-operable and screen-reader labeled (WCAG 2.2 AA) |

## UX and design

Key flows: save a view, switch view, set default, share view, handle a stale view. States that must be
designed, not just the happy path:
- **Empty:** a user with no saved views sees a one-line prompt explaining what views do.
- **Loading:** switching views shows a non-blocking indicator; the dashboard does not flash to default first.
- **Error:** a view that references a deleted filter loads the valid parts and shows a clear "some
  filters in this view no longer exist" message with a way to fix and re-save.
- **Permission edge:** a shared view selected by a user who lacks access to one of its filters loads
  only what they are permitted to see.

## Success metrics

- Primary: median time from dashboard open to first meaningful interaction drops for Recurring Analysts
  (tied to the Time to Insight goal). Target direction: down; magnitude to be set with the data team.
- Guardrail: dashboard load error rate does not increase, and shared-view permission incidents stay at zero.
- Measurement window: 4 weeks post-rollout, compared to the 4 weeks prior, for the Recurring Analyst cohort.

## Analytics and instrumentation

Instrument before launch: `view_saved`, `view_switched`, `view_set_default`, `view_shared`,
`view_load_error` (with reason), each with dashboard ID and view scope. Build a Saved Views adoption
dashboard (views created per active analyst, share rate, default-set rate) and wire the primary metric
to the existing Time to Insight panel. Without this, we cannot tell whether the primary metric moved.

## Dependencies

| Dependency | Owner | Status |
|---|---|---|
| Per-user preferences storage (shipped Q1) | Platform | Done |
| Dashboard permissions service (for shared-view access checks) | Platform | Confirmed, integration pending |
| Design system menu component update | Design Systems | In progress |

## Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Shared views leak data via mismatched permissions | Low | High | Enforce per-recipient permission checks at load (NFR); security review before GA |
| Low adoption because the control is not noticed | Medium | Medium | Empty-state prompt; one-time tooltip; track adoption from day one |
| Stale views confuse users after a dashboard changes | Medium | Low | Graceful degradation (FR-6 + error state); clear "filters changed" messaging |

## Rollout and release plan

Phase 1: private views only (FR-1 to FR-3, FR-5) behind a feature flag, internal dogfood for 1 week.
Phase 2: enable sharing (FR-4) after the security review passes. Phase 3: GA via gradual flag rollout
(10 percent, 50 percent, 100 percent) with the adoption dashboard watched at each step. Rollback: the
flag disables the Views control and falls back to default dashboard state; saved view data is retained,
not deleted, so re-enabling is safe. Release notes and the launch checklist are tracked in their own
artifacts.

## Open questions

| Question | Owner | Needed by |
|---|---|---|
| What exact magnitude of time-to-insight improvement counts as success? | Priya + Data | Before GA |
| Should a team default view be possible (Team Lead sets the team's default), or only personal defaults? | Priya | Before Phase 2 |
| Do we cap the number of saved views per user, and if so at what number? | Priya + Platform | Before Phase 1 |

## Appendix

- Discovery readout: Reporting friction study, 2026-05 (n=12 analysts, illustrative).
- Prior decision: per-user preferences storage chosen over per-dashboard storage in Q1 (see ADR-014, illustrative).
- Glossary: "view" = a saved combination of filters, date range, and visible columns for one dashboard;
  it does not change the dashboard's structure.
