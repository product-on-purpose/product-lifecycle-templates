---
title: "Acme Analytics Product Backlog"
product: "Acme Analytics"
product_owner: "Priya Nair (PM, Reporting)"
last_refined: "2026-07-06"
status: active
related: ["../prd/prd_example.md (Saved Views for Dashboards PRD)", "../user-stories/user-stories_example.md (Saved Views user stories)", "../sdd/sdd_example.md (Saved Views for Dashboards design)", "../release-notes/release-notes_example.md (the release note completed items surface in)"]
doc_type: product-backlog
size: full
source_template: product-backlog
source_template_version: 0.1.0
---

<!--
This is a worked example for the product-backlog bundle. It is a realistic, fully filled full-variant
product backlog for the Reporting team of a fictional analytics product, scoped by the same "Saved Views"
Product Goal that the delivery-docs family's other examples chain on (see prd_example.md and the Saved
Views user stories). Figures and IDs are illustrative. A product backlog is a living document; this is a
snapshot as of the last-refined date. Use it as a model of shape and tone, not as a source of facts.
-->

# Acme Analytics Product Backlog

## Product Goal

**Cut the median time from opening a report to acting on it by 30% for Recurring Analysts, by the end of
Q3, measured on the Time to Insight panel.** (Illustrative target; the [Saved Views PRD](../prd/prd_example.md)
leaves the exact magnitude to be set with the data team, so 30% is this backlog's working assumption, not a
committed number.)

Everything currently at the top of this backlog serves this one goal; the few items that do not (a
production bug, one piece of tech debt) are here because they are cheap and painful, and they are ordered
on their own merits rather than against the goal.

## Backlog Items

Ordered top to bottom; Rank 1 is next. The Saved Views epic (IDs `SV-*`) decomposes the PRD; its stories
are the ones detailed in the [Saved Views user stories](../user-stories/user-stories_example.md). Items
below the waterline (Rank 9+) are deliberately coarse.

| Rank | ID | Item | Type | Priority | Value / problem it serves | Estimate | Depends on | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | SV-1 | Persist a saved view (new `saved_view` store) | tech/enabler | Must | Nothing else in the epic can ship without a place to store a view | 5 | - | Ready |
| 2 | SV-2 | Save the current dashboard state (filters, date range, columns) as a named view | story | Must | Recurring Analysts stop rebuilding their filters every visit | 5 | SV-1 | Ready |
| 3 | BUG-231 | CSV export drops the last row on reports over 10k rows | bug | Must | Analysts silently lose data; reported by 4 customers | 3 | - | Ready |
| 4 | SV-3 | List a user's views and switch between them in one action | story | Must | A saved view is only useful if it is one click to reopen | 5 | SV-1 | Ready |
| 5 | SV-4 | Set a view as the user's default for a dashboard | story | Must | The dashboard opens the way the analyst works | 3 | SV-2 | Ready |
| 6 | SV-0 | Spike: validate the shared-view permission model | spike | Should | Retire the risk that sharing could leak data before we build it | 2 | - | Ready |
| 7 | SV-5 | Share a view with the team (permission-checked) | story | Should | Team Leads get everyone on one agreed view | 8 | SV-1, SV-2, SV-0, Dashboard permissions service | Refining |
| 8 | SV-6 | Rename and delete views the user owns | story | Should | Keeps a user's view list meaningful | 2 | SV-2 | Refining |
| 9 | TD-12 | Migrate the legacy filter state off the deprecated cache | tech debt | Should | Removes the fragile store the Q1 preferences work left behind | 5 | - | Coarse |
| 10 | SV-7 | Flag a shared view whose underlying dashboard changed | story | Could | Prevents silent confusion when a dashboard evolves | 3 | SV-5 | Coarse |

**Not in the ordered backlog (parked):** EXP-4, scheduled email/Slack delivery of a saved view, is a PRD
**non-goal** ("out of scope now; likely a fast follow"). It is kept in the someday-maybe archive, not the
ordered list, so a deliberate scope exclusion is never confused with low-ranked work; it would enter the
backlog only if the PRD lifts that non-goal.

## Ordering Rationale

Ordered by **dependency and risk first, then value toward the goal**, not by raw value alone:

- **SV-1 (storage) leads** because every Saved Views story depends on it; a higher-value story cannot go
  first if the thing it needs does not exist yet.
- **BUG-231 sits at Rank 3**, above some Must stories, because it is cheap (3 points) and is actively
  losing customer data now; the cost of leaving it is higher than its value score alone suggests.
- **The spike (SV-0) is ordered before the sharing story (SV-5)** it de-risks, so we learn whether the
  permission model holds before committing eight points to building on it.
- **Should and Could items sit below the Musts**, with the tech debt (TD-12) and the lowest-value Could
  story (SV-7) forming the coarse tail. The one PRD non-goal (scheduled delivery) is parked out of the
  ordered backlog entirely, so a deliberate exclusion is not mistaken for merely low-ranked work.

Ties within a band are broken by the Product Owner in refinement, informed by the framework below.

## Refinement and Readiness

Refined **continuously, roughly 10% of each sprint, as a team** (Product Owner plus the developers), with a
standing 30-minute session mid-sprint. Only the top of the backlog is kept sprint-ready; items at Rank 9
and below are intentionally coarse.

An item is **ready** when it is: clear (shared understanding of what and why), testable (acceptance
criteria exist, tracked in the [acceptance-criteria](../acceptance-criteria/acceptance-criteria_example.md)
artifact for the Saved Views stories), and small enough to finish in one sprint. This is a lightweight
heuristic, not a stage-gate: an item that is 90% ready can still be pulled if the team is confident, and
the last details settle in sprint planning.

## Prioritization Framework

**MoSCoW** for the Saved Views epic, inherited directly from the PRD's Must/Should/Could requirement
priorities, so the backlog and the PRD stay in sync. The Product Owner interleaves non-epic work (the
production bug, tech debt) by judgment rather than by MoSCoW, because a "Must-have bug fix" and a
"Must-have feature" are not the same kind of Must and forcing them into one scale would be false
precision.

No numeric framework (WSJF, RICE) is used yet: this is one team with one goal and ten ordered items, small
enough to order by conversation. If the Saved Views work grows into a cross-team program, WSJF would be
the right next step, to make the cost-of-delay trade-offs (the CSV bug, the sharing risk) legible across
teams. No single framework is treated as gospel; the Rank column is the Product Owner's decision, and the
Priority column only informs it.

## Dependencies and Risks

- **SV-1 (storage) blocks the whole epic.** It is ranked first for exactly this reason.
- **SV-5 (share a view) has an external dependency**: the Dashboard permissions service (owned by the
  Platform team), needed to re-check each recipient's access to the underlying data. Confirmed with
  Platform, integration pending (per the PRD's dependency table).
- **Risk, carried into the design:** the storage-model decision (a dedicated `saved_view` store versus
  extending the Q1 per-user preferences store) is architecturally significant and should be recorded as an
  **ADR**, not left implicit in the backlog. This backlog item (SV-1) is where that decision surfaces; the
  decision itself belongs next to the code.
- **Risk, de-risked by a spike:** a bug in the shared-view permission re-check could leak data. SV-0 (the
  spike) is ranked ahead of SV-5 to retire that risk on paper before eight points are spent building on it.
- **Invalidation risk:** if the Time to Insight metric does not move after the Must stories ship, the
  Should and Could items (sharing, stale-view flagging) may be re-ordered or dropped, because they would no
  longer clearly serve the goal.

## Backlog Health and Metrics

- **Size:** 10 active ordered items, plus one parked non-goal (EXP-4) in someday-maybe. Small and fully
  orderable by a human; no bankruptcy risk today.
- **Age:** nothing above Rank 8 is older than the current quarter; the coarse tail (TD-12, SV-7) is the
  oldest active work and is a candidate for archive if it slips another quarter without being pulled.
- **Pull depth:** the team realistically pulls from the top ~5 each sprint, so anything below Rank 8 is a
  hypothesis, not a commitment, and is kept coarse on purpose.
- **Archive rule:** any item untouched for two quarters moves to a `someday-maybe` archive: recoverable,
  but out of the ordered list so it does not cost the team focus. EXP-4 (scheduled delivery) already lives
  there as a PRD non-goal; TD-12 is the first active item at risk of joining it.
