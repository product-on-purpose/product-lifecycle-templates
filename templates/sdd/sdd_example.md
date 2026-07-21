---
title: "Saved Views for Dashboards: design"
status: in-review
authors: ["Marcus Bell (Staff Engineer, Reporting)"]
reviewers: ["Priya Nair (PM, Reporting)", "Dana Osei (Staff Engineer, Platform)"]
created: "2026-07-02"
updated: "2026-07-09"
related: ["prd_example.md (Saved Views for Dashboards PRD)", "future ADR: saved-view storage model"]
doc_type: sdd
size: full
source_template: sdd
source_template_version: 0.1.0
---

<!--
This is a worked example for the SDD bundle. It is a realistic, fully filled full-variant design doc for
a single feature, the design counterpart to the PRD in prd_example.md (both use the fictional "Saved
Views" feature, so the delivery-docs and decision-docs families chain on one scenario). Figures marked
"illustrative" are described in text for the example and would be real diagrams in a live design doc. Use
it as a model of shape and tone, not as a source of facts.
-->

# Saved Views for Dashboards: design

## Context and Scope

Today, a dashboard's filters, date range, and visible columns live only in the page's ephemeral state and
reset to the dashboard default every time it is opened. The [Saved Views PRD](prd_example.md) established
the need: Recurring Analysts rebuild the same filter set several times a day, and Team Leads want their
team looking at one agreed view. This design describes how we build saved, reusable, and shareable views
on top of the dashboard-service and the per-user preferences storage that shipped in Q1.

**In scope:** persisting a view (filters, date range, visible columns) for a dashboard; listing and
switching a user's views; setting a personal default; sharing a view with other permitted users of the
same dashboard.

**Out of scope:** cross-dashboard "global" views, scheduled delivery of a view, and any change to the
dashboard definition or the filtering engine itself. These are the PRD's non-goals and are unchanged here.

## Goals and Non-Goals

**Goals**
- A user can save the current dashboard state as a named view and reopen it in one action, across
  sessions and devices.
- A user can set one view as their personal default for a dashboard.
- A user can share a view so other permitted users of that dashboard can select it, with no path to data
  the recipient could not already see.

**Non-Goals**
- **Real-time co-editing of a view.** Views are saved and shared, not co-edited live; that is a separate
  feature and a much harder concurrency problem.
- **A team-owned default** (a Team Lead setting the team's default view). This is an open product
  question (see Risks and Open Issues) and is deliberately not designed here yet.
- **Changing the Q1 storage decision.** Per-user preferences already chose per-user over per-dashboard
  storage; this design adds an entity, it does not revisit that.

## The Design

Saved views are one new entity owned by the existing dashboard-service and stored in the main application
database, exposed by a small set of new REST endpoints and a "Views" control in the dashboard header. A
view captures the dashboard state as a versioned JSON blob; sharing is a scope flag plus a permission
check delegated to the existing dashboard permissions service. The four views below detail the static
structure, the runtime behavior, the interface contracts, and how it deploys. The one decision worth
lifting out of this document and into an ADR is the storage model (a dedicated table versus extending the
Q1 per-user preferences store); it is called out in Alternatives Considered and Risks and Open Issues.

### Static Structure and Components

One new table and one new controller; everything else is reused.

**New `saved_view` table** (main Postgres database):

| Column | Type | Notes |
|---|---|---|
| `id` | uuid, PK | |
| `name` | text | user-supplied, non-empty |
| `owner_id` | uuid, FK users | the creator |
| `dashboard_id` | uuid, FK dashboards | the view's dashboard |
| `scope` | enum(`private`, `shared`) | default `private` |
| `config` | jsonb | versioned view state (see Interfaces) |
| `created_at` / `updated_at` | timestamptz | |

Per-user default is a single `default_view_id` added to the existing per-user preferences record, keyed
by dashboard, rather than a column on `saved_view`: a default is a per-user choice about a view, not a
property of the view, and shared views must be defaultable by users who do not own them.

**New `ViewsController`** in the dashboard-service, exposing the endpoints in Interfaces and Contracts.
**Reused:** the existing auth middleware, the dashboard permissions service (for shared-view access
checks), and the frontend dashboard state store (the Views control reads and writes the same filter/date/
column state the dashboard already manages).

*Figure 1 (illustrative): a C4 component diagram would show the dashboard-service containing the new
ViewsController alongside the existing DashboardController, both calling the permissions service, with the
`saved_view` table and the per-user preferences store as the two data stores touched.*

### Runtime and Data Flow

- **Save a view:** the client posts the current dashboard state to `POST /dashboards/{id}/views`. The
  service checks the caller's read access to the dashboard, validates the `config` against the current
  schema version, persists the row with `scope = private`, and returns the new view.
- **Apply a view:** the client fetches `GET /dashboards/{id}/views/{viewId}` and rehydrates the dashboard
  state from `config`. If a `config` references a filter field that no longer exists, the service returns
  the resolvable parts and a `stale_fields` list; the client applies what it can and shows the PRD's
  "some filters no longer exist" message rather than failing the load.
- **Share a view:** the owner sets `scope = shared` via `PUT`. On any subsequent read of a shared view by
  another user, the service re-checks that user's access to the underlying dashboard data through the
  permissions service, so a shared view can never widen what a recipient may see.
- **Set default:** writing `default_view_id` to the caller's preferences record; on dashboard open, the
  service resolves the default (if any and still readable) and applies it.

*Figure 2 (illustrative): a sequence diagram would show the share-then-apply path, with the permission
re-check happening on the recipient's read, not at share time.*

### Interfaces and Contracts

**REST endpoints** (all under the dashboard-service, authenticated as today):

- `GET /dashboards/{id}/views` - list the caller's own views plus shared views on this dashboard.
- `POST /dashboards/{id}/views` - create a view from a `config` payload.
- `GET /dashboards/{id}/views/{viewId}` - fetch one view, with `stale_fields` if any.
- `PUT /dashboards/{id}/views/{viewId}` - rename, change scope, or update `config` (owner only).
- `DELETE /dashboards/{id}/views/{viewId}` - delete (owner only).

**Config schema (versioned).** The stored JSON is the real contract, so it carries a version from day
one:

```
{ "version": 1,
  "filters": [ { "field": "region", "op": "in", "value": ["EMEA"] } ],
  "date_range": { "preset": "last_30_days" },
  "columns": ["name", "owner", "status", "updated_at"] }
```

**Events** (for the PRD's analytics): `view_saved`, `view_switched`, `view_set_default`, `view_shared`,
`view_load_error` (with reason), each carrying dashboard id and scope. No existing dashboard endpoint
changes.

### Deployment and Operations

- **Migration:** additive only. Create the `saved_view` table and add the nullable `default_view_id` to
  the preferences record; no existing table is altered, so the migration is reversible.
- **Rollout:** behind a `saved_views` feature flag, enabled per-dashboard, dark-launched to internal
  dashboards for a week, matching the PRD's phased plan (private views first, sharing after the security
  review).
- **Backout:** disable the flag; the Views control disappears and dashboards fall back to default state.
  Saved-view rows are retained, not deleted, so re-enabling is safe.
- **Ownership:** the Reporting team owns the ViewsController and the table; no new service is introduced,
  so there is no new on-call surface.

## Alternatives Considered

- **Extend the Q1 per-user preferences store** (keep views as entries in the existing per-user key-value
  preferences record). Rejected: that store is per-user by construction and has no project- or
  dashboard-scoped query path and no notion of a shared, permission-checked object. Sharing is a core
  goal (PRD FR-4), and bolting it onto a per-user KV blob would mean reinventing scoping and access
  control in application code. A dedicated table models the object honestly.
- **Client-only storage (URL and localStorage).** Rejected: no sharing, lost across devices, and directly
  contradicts the PRD's cross-device and sharing goals.
- **A separate saved-views microservice.** Rejected: a new service, a new data store to keep in sync with
  dashboards, and a new on-call rotation, all for what is fundamentally one table and one controller.
  Overkill against the goals.

The choice between the first option and the adopted dedicated-table design is significant and hard to
reverse once views exist, so it should be recorded as its own **ADR** (the design-doc-to-ADR
relationship: this document holds the whole design; the storage decision is the one piece worth finding
next to the code on its own). The Q1 per-user-versus-per-dashboard decision is already recorded as
ADR-014 (illustrative); this is its sequel.

## Cross-Cutting Concerns

- **Security and privacy.** Write is owner-only, enforced in the controller. A shared view's read
  re-checks the reader's access to the underlying data through the permissions service on every load, so
  a shared view never exposes data the recipient could not already access (PRD security NFR). Private
  views are never returned to anyone but the owner.
- **Observability.** The five analytics events above, plus standard request metrics on the new endpoints;
  a `view_load_error` rate panel is wired before GA so stale-view degradation is visible.
- **Failure handling.** A `config` referencing a deleted field degrades gracefully (apply-what-resolves,
  flag the rest) rather than erroring the dashboard load.
- **Cost and quota.** A cap of 100 saved views per user per dashboard bounds storage and keeps the list
  usable; the cap is configurable and logged when hit. (The PRD left the exact cap open, owned by the PM
  before Phase 1; 100 is this design's input to that decision, not a final answer.)
- **Accessibility.** The Views control is keyboard-operable and screen-reader labeled to WCAG 2.2 AA,
  reusing the design-system menu component; no new accessibility surface is invented.

## Quality Attributes

- **Performance.** Applying a saved view renders in under 1s at p95 on a standard dashboard (the PRD
  target); the views list responds in p95 < 150ms at up to 50 views at launch (a single indexed query on
  `(dashboard_id, owner_id, scope)`). The path from that launch state to the full 500-view scale envelope
  is the pagination debt noted in Risks and Open Issues.
- **Scale.** Up to roughly 500 shared views per dashboard and 100 private views per user per dashboard;
  beyond that the list paginates (see Risks).
- **Availability.** Inherits the dashboard-service SLO (99.9%); saved views add no new hard dependency
  beyond the already-required permissions service.
- **Maintainability and evolvability.** The `config` schema is versioned, so the filter vocabulary can
  change without breaking stored views: a reader migrates an older `config` version forward or applies it
  best-effort.

## Risks and Open Issues

- **Risk: stored `config` drifts from the dashboard's real fields.** As filters and columns evolve, older
  views reference fields that no longer exist. Mitigation: the versioned schema plus apply-what-resolves
  and the `stale_fields` signal (PRD FR-6). This is accepted, not eliminated.
- **Risk: a shared-view permission leak.** A bug in the read-time permission re-check could expose data.
  Mitigation: the re-check is centralized in one code path, covered by tests that assert a
  reduced-permission recipient sees only permitted data, and gated behind a security review before
  sharing goes GA (PRD Phase 2).
- **Open issue: team-owned default views.** Should a Team Lead be able to set a team default (PRD open
  question)? Not designed here; it raises ownership and override questions. Owner: Priya Nair (PM), before
  Phase 2.
- **Open decision: the storage model belongs in an ADR.** As noted in Alternatives Considered, the
  dedicated-table choice should be recorded as its own decision record.
- **Debt: no pagination on the views list at launch.** Acceptable while dashboards stay under ~200 views;
  tracked to add before that threshold is reached.
