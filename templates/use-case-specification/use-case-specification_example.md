---
title: "Set a Default Saved View"
use_case_id: "UC-SV-04"
primary_actor: "Recurring Analyst"
doc_type: use-case-specification
size: full
owner: "Priya Nair (PM, Reporting)"
status: "in-review"
doc_version: "0.1.0"
created: "2026-06-20"
updated: "2026-06-30"
related_links:
  - "Story: set a default saved view (user-stories_example.md)"
  - "PRD: Saved Views (prd_example.md)"
source_template: use-case-specification
source_template_version: 0.1.0
---

> **Worked example.** A filled `use-case-specification`, full variant, elaborating the
> [set a default saved view](../user-stories/user-stories_example.md) story from this library's own
> "Saved Views" chain, the same work the
> [acceptance criteria](../acceptance-criteria/acceptance-criteria_example.md) that follow it go on to
> confirm. `use-case-specification` joined the `delivery-docs` family on 2026-10-15 under
> [ADR 0072](../../docs/internal/decisions/0072-use-case-specification-joins-delivery-docs.md), and sits
> in the chain between the story it elaborates and the acceptance criteria that confirm it. It is dated
> **created 2026-06-20**, after the story entered review on 2026-06-18 and before the acceptance criteria
> that follow it were drafted on 2026-06-22, so its related links name the story and the PRD but not
> the acceptance criteria, which did not yet exist on this document's own created date; **updated
> 2026-06-30**, the same date every document in this chain carries as its latest revision, and the revision
> that took the acceptance criteria's performance target. The priority traces to the PRD's FR-3. The
> frequency below is illustrative: plausible for this document and labeled where it appears, not drawn
> from a real company.

# Set a Default Saved View

## Title and Actor

**Use Case ID:** UC-SV-04

**Primary Actor:** Recurring Analyst - an internal or customer analyst who returns to the same
dashboards daily or weekly and works within a stable set of filters.

## Goal in Context

A recurring analyst who already has one or more saved views for a dashboard wants one of them to load
automatically every time they return to it, instead of re-selecting a view or starting from the
dashboard's generic default state on every visit. The goal arises out of a daily or weekly habit: once an
analyst has saved the filters, date range and columns they actually work from, choosing among several
saved views on every single visit is itself a small repeated cost, the same re-filtering tax that saving
a view in the first place was meant to remove. Setting a default lets that habit stop costing anything
after the first time it is set, and the analyst may change which view is the default again later if the
slice they work from changes.

## Scope and Level

**Scope:** Dashboards in Acme Analytics, considered as a black box: which one of a user's own saved
views, if any, is marked as the view that loads automatically when that user opens a given dashboard. How
a dashboard renders the data inside a view, and how a view is captured and saved in the first place, sit
outside this use case's own scope.

**Level:** User-goal. Setting the default takes one sitting; step 4 is its payoff, on the analyst's
next visit.

## Stakeholders and Interests

| Stakeholder | Interest |
|---|---|
| Team Lead | Wants a personal default one analyst sets for themselves to never change what any other user of the same dashboard sees, since whether a Team Lead can set a team-wide default for everyone is still an open question for this dashboard |
| Other users of the same dashboard | Want their own default, or the absence of one, to stay exactly as it was, regardless of what any other user marks as their own default |

## Preconditions and Trigger

**Preconditions:** The recurring analyst already has at least one saved view for this dashboard; the
save-view story is a sequenced prerequisite for this one. The per-user preferences store, which the
Platform team shipped in Q1, already holds that analyst's existing saved views for this dashboard.

**Trigger:** The recurring analyst, from the dashboard's Views control, chooses one of their existing
saved views to become this dashboard's default.

## Main Success Scenario

1. The recurring analyst chooses one of their saved views for this dashboard to become their default.
2. The system un-marks whichever saved view currently holds default status for this dashboard for that
   analyst.
3. The system marks the chosen view as the recurring analyst's default for this dashboard.
4. The next time the recurring analyst opens this dashboard, the system loads it already in the default
   view's filters, date range and columns applied, instead of the dashboard's generic default state.

## Extensions

| Extension | Condition | Handling | Outcome |
|---|---|---|---|
| 2a | The recurring analyst has no default for this dashboard yet, so the dashboard still opens in its generic default state | Nothing needs un-marking | Rejoins the main scenario at step 3 |
| 4a | The default view references a filter that has since been deleted | The system loads the still-valid filters and shows a clear "some filters in this view no longer exist" message, with a way to fix and re-save | Ends in a separate success; the analyst sees the dashboard and knows exactly what to fix |

## Minimal and Success Guarantees

**Minimal Guarantees:** However the attempt ends, no other user's default for this dashboard changes,
which is the interest both stakeholders above hold, and this analyst never holds more than one default
for it. If the attempt stops partway, the dashboard still opens, in its generic default state if no
default of theirs survived.

**Success Guarantees:** The chosen view is this recurring analyst's one default for this dashboard, and
the view that held that status before no longer does.

## Related Information

**Priority:** High. FR-3 is a Must-priority requirement for the Phase 1 release, which ships private
views (FR-1 to FR-3, FR-5) behind a feature flag.

**Performance Target:** Loading the default view on dashboard open completes within 1 second at p95
(illustrative target, the same one the acceptance criteria carry).

**Frequency:** Not measured directly. The only related figure is how often a recurring analyst visits a
dashboard at all, daily or weekly, not how often any one of them changes their default
(illustrative, inferred from that visiting cadence rather than drawn from a measurement of this use case
itself).

**Technology and Data Variations:** None known.

**Secondary Actors:** The per-user preferences store, the Q1 Platform-team service that records and
returns which saved view is marked default for a given user and dashboard.

**Superordinate/Subordinate Use Cases:** None known.

## Open Issues and Schedule

| Open Issue | Owner | Needed By |
|---|---|---|
| Should a Team Lead be able to set a team default for a dashboard, or should only personal defaults ever exist? | Priya Nair | Before Phase 2 |

**Due Date:** Phase 1 (private views only, behind a feature flag).
