---
title: "Acme Analytics Reporting Tracking Plan"
product: "Acme Analytics Reporting"
plan_owner: "Marta Reyes (Program Manager, Reporting Platform Modernization)"
data_steward: "Lee Zhang (Data Eng)"
sources_and_destinations: "Amplitude for product events, Looker for the executive view"
plan_version: "v1.2"
last_reviewed: "2026-08-24"
status: "active"
doc_type: tracking-plan
size: full
source_template: tracking-plan
source_template_version: 0.1.0
---

> **Worked example.** A filled `tracking-plan`, full variant, for the Reporting Platform Modernization
> program at the fictional Acme Analytics, the same program the
> [`prd`](../prd/prd_example.md), [`release-notes`](../release-notes/release-notes_example.md),
> [`experiment-design-doc`](../experiment-design-doc/experiment-design-doc_example.md),
> [`kpi-dashboard`](../kpi-dashboard/kpi-dashboard_example.md), and [`okrs`](../okrs/okrs_example.md)
> examples already cover, and the same program whose
> [risk register](../risk-register/risk-register_example.md),
> [RAID log](../raid-log/raid-log_example.md), [issue log](../issue-log/issue-log_example.md), and
> [change log](../change-log/change-log_example.md) Marta Reyes already keeps as its other standing
> governance instruments. `tracking-plan` joined the `governance-docs` family as its sixth member on
> 2026-10-06 under
> [ADR 0067](../../docs/internal/decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md),
> and this plan sits upstream of the KPI dashboard the family already built: the dashboard defines the
> metrics the program tracks against targets, and this plan defines the events those metrics are computed
> from. Dated 2026-08-24: after the 2.4.0 release (2026-07-21) that shipped Saved Views, after the
> adoption-nudge experiment's design doc (2026-07-30), and before that test ends (2026-08-31) and its
> readout is written, so the plan below lists the test's exposure event as active without knowing what it
> found.
>
> Figures not already fixed by a sibling example, including every per-event reason, every
> source-and-destination cell, the privacy retention figure, and the earliest version-history date, are
> illustrative: plausible for this document, invented for it, and not drawn from a real company.

# Acme Analytics Reporting Tracking Plan

## Purpose and Boundary

This plan covers every event Acme Analytics' Reporting product records, product-wide: the Reporting web
application Recurring Analysts use to open, export, share, and annotate reports, and the Saved Views
feature layered on top of it. It is not the place a single feature's own instrumentation slice is first
proposed; the five Saved Views events below (`view_saved`, `view_switched`, `view_set_default`,
`view_shared`, `view_load_error`) were first proposed in the
[Saved Views for Dashboards PRD](../prd/prd_example.md)'s own Analytics and instrumentation section, and
this plan carries them forward as version-history entries rather than re-proposing them from nothing. It
is not the data dictionary, the document that will state what the data in these events' destination
tables actually means once it is implemented, which this program has not yet written. It is not the
measurement plan, the document that would state why the program tracks Time to Insight at a thirty percent
reduction by Q3 in the first place; that reasoning lives in the [FY26 OKRs](../okrs/okrs_example.md) and
the [KPI dashboard](../kpi-dashboard/kpi-dashboard_example.md), not here. The KPI dashboard's Metric
Definitions section is a different document's job, not this one: it is where the Time to Insight formula
itself gets fixed, median minutes from a report's opening to the first logged action on it. This plan only
supplies the events that formula reads; it does not pin the formula down a second time. Nor is it the
live, enforced copy of this plan that actually runs: that
copy lives in Amplitude, where these events land, and in Looker, where the executive view of them is
built. Where the live tool and this document disagree, this document is what gets corrected.

One dashboard metric has no row below and will not get one: View-list load (p95) is client-measured,
read from the Reporting web app's real-user-monitoring pipeline rather than from a logged event, so this
plan has nothing to add to it beyond naming the gap.

## Naming Conventions

Every event name in this catalog follows the same shape: an object, then a past-tense action, written in
snake_case, for example `view_saved`, `report_opened`, and `nudge_variant_assigned`. The plan's own first
events, the four report events added in v1.0, already used that shape, and the Saved Views for Dashboards
PRD's five events follow it too, so every event added since has kept it rather than starting a second
convention. Two different
objects, a saved view and a report, each carry a "shared" action (`view_shared`, `report_shared`), so the
object is what keeps the two apart in the catalog below; a reader
checking what happens when something is shared has to read the object, not only the verb. The Reporting
product ships as a single web application today. The FY26 OKRs record that mobile authoring is out of
scope for this cycle while mobile consumption keeps working, so a platform-specific divergence in these
names has not yet come up. If a mobile surface's own automatic tracking were ever to fire a differently
named event for the same action, this plan's answer, not that surface's default, is the one this catalog
uses.

## Event and Property Catalog

Neither the Saved Views PRD nor the KPI dashboard names an owner for an individual event, and the KPI
dashboard names its three proxy actions, export, share, and annotate, and the report-open moment, without
naming the events behind them. Both choices are this plan's own. Event owners below follow the metric
owner each event feeds: Priya Nair for the events behind the metrics she owns, Dana Osei for
`view_load_error`, with Lee Zhang named as data steward across every row rather than as an individual
event's owner. The report-open moment and the three proxy actions are named `report_opened`,
`report_exported`, `report_shared`, and `report_annotated`, in the same object-then-past-tense form the
PRD already used. One property is also this plan's own addition rather than the PRD's: the PRD's slice
fixed only dashboard ID and view scope for its five events, so `recipient_user_id` on `view_shared` below
is this plan's own, needed to make that event's privacy row possible.

**Status vocabulary used below:** proposed, active, deprecated, removed.

| Event | Fires when | Why (business question) | Properties | Source -> Destination | Owner | Status |
|---|---|---|---|---|---|---|
| view_saved | An analyst saves the dashboard's current filters as a named view | Measures whether Saved Views are being created at all, feeding the Saved Views adoption key result | dashboard_id (string), view_scope (string) | Reporting web app -> Amplitude | Priya Nair | active |
| view_switched | An analyst switches to a previously saved view | Measures reuse of a saved view after it exists, not only its creation | dashboard_id (string), view_scope (string) | Reporting web app -> Amplitude | Priya Nair | active |
| view_set_default | An analyst sets a saved view as the default for a dashboard | Measures the strongest form of adoption, a view used without being re-selected each visit | dashboard_id (string), view_scope (string) | Reporting web app -> Amplitude | Priya Nair | active |
| view_shared | An analyst shares a saved view with another user | Measures collaboration around views, and is the source of the shared-view permission guardrail the PRD names | dashboard_id (string), view_scope (string), recipient_user_id (string) | Reporting web app -> Amplitude | Priya Nair | active |
| view_load_error | A saved view fails to load, with a reason | Feeds the dashboard load error rate guardrail and the failure side of View-list load (p95) | dashboard_id (string), view_scope (string), reason (enum: filters_removed, permission_denied, timeout, unknown) | Reporting web app -> Amplitude | Dana Osei | active |
| report_opened | An analyst opens a report | Marks the start of the Time to Insight window for that report-session | report_id (string), dashboard_id (string) | Reporting web app -> Amplitude | Priya Nair | active |
| report_exported | An analyst exports a report | One of the three logged actions that proxy "taking action" on a report for Time to Insight | report_id (string), export_format (enum: csv, pdf, image) | Reporting web app -> Amplitude | Priya Nair | active |
| report_shared | An analyst shares a report with another user | One of the three logged actions that proxy "taking action" on a report for Time to Insight | report_id (string), recipient_user_id (string) | Reporting web app -> Amplitude | Priya Nair | active |
| report_annotated | An analyst adds an annotation to a report | One of the three logged actions that proxy "taking action" on a report for Time to Insight | report_id (string), annotation_id (string) | Reporting web app -> Amplitude | Priya Nair | active |
| nudge_variant_assigned | An eligible account crosses its fifth dashboard view during the Saved Views adoption-nudge test (2026-08-03 through 2026-08-31) | Assigns an account to a test arm so the weekly adoption read can be attributed to the right side of the test | variant_id (string), account_id (string) | Reporting web app -> Amplitude | Priya Nair | active |

## User and Account Properties

| Trait | Subject (user or account) | Type and allowed values | Source (where it is set) |
|---|---|---|---|
| analyst_segment | user | enum: recurring, trialist, internal | Set from the entitlements database, refreshed nightly, the same source and cadence the OKRs' Saved Views adoption key result reads |
| migration_reconciled | account | boolean | Set by the migration reconciliation job at cutover; feeds the Migration integrity metric |

## Privacy, Sensitivity and Retention

| Event or property | What is sensitive | Flag | Retention | Handling before storage |
|---|---|---|---|---|
| view_shared and report_shared | recipient_user_id: the colleague a view or a report is shared with | pii_flag: true | 180 days, then purged (this program's own figure, pending legal confirmation) | Hashed on the way into the warehouse; the retention figure above is still pending legal's confirmation |

## Review and Ownership

**Plan owner (apart from any event's owner):** Marta Reyes (Program Manager, Reporting Platform
Modernization).

**Review interval:** Monthly, the week after the program steering review where the KPI dashboard is read,
so any event question that review raises is settled here before the dashboard is next read. This interval is the
program's own choice, not a figure borrowed from outside the program.

**Other review triggers:** A release that ships a new event, as 2.4.0 did for the five Saved Views events,
or a new experiment's exposure event, as the adoption-nudge test did for `nudge_variant_assigned`, each
trigger a review ahead of the monthly date rather than waiting for it.

## Change Process and Version History

A new event starts as a proposal attached to the feature or experiment that needs it: the five Saved
Views events began in the Saved Views PRD's own Analytics and instrumentation section, and
`nudge_variant_assigned` began in the adoption-nudge experiment design doc. Lee Zhang, as data steward,
checks a proposed name against the convention above and against every event already listed before it is
added here. Priya Nair, as domain owner for Reporting, approves events behind the metrics she owns; Dana
Osei approves events behind the metrics he owns, such as `view_load_error`. An event is never removed by a
quiet status flip; removal runs through the same proposal, steward check, and domain-owner approval as
adding one, recorded in the table below. Before an event goes active, someone checks that what actually
fires matches what this plan says it fires: `nudge_variant_assigned` was checked in the staging
environment on 2026-07-29, five days before the test it belongs to began.

| Version | Date | What changed | Approved by |
|---|---|---|---|
| v1.0 | 2026-05-18 (illustrative; predates the Saved Views PRD, created 2026-06-12) | report_opened, report_exported, report_shared, report_annotated added (proposed -> active), feeding the pre-existing Time to Insight metric | Reviewed by Lee Zhang, approved by Priya Nair for Reporting |
| v1.1 | 2026-07-21 | view_saved, view_switched, view_set_default, view_shared, view_load_error added (proposed -> active), shipping with Saved Views in release 2.4.0 | Reviewed by Lee Zhang; view_saved, view_switched, view_set_default and view_shared approved by Priya Nair for Reporting, view_load_error approved by Dana Osei for Platform |
| v1.2 | 2026-07-29 | nudge_variant_assigned added (proposed -> active), checked in staging ahead of the Saved Views adoption-nudge test | Reviewed by Lee Zhang, approved by Priya Nair, the test's decision-maker |
