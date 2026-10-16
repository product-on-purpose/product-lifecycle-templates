---
title: "Acme Analytics Reporting Warehouse Data Dictionary"
dataset: "Reporting analytics warehouse: the events, report_sessions, users, and accounts tables"
owner: "Lee Zhang (Data Eng)"
steward: "Lee Zhang (Data Eng)"
dictionary_version: "v1.1"
last_reviewed: "2026-09-08"
status: "active"
doc_type: data-dictionary
size: full
source_template: data-dictionary
source_template_version: 0.1.0
---

> **Worked example.** A filled `data-dictionary`, full variant, for the Reporting Platform Modernization
> program at the fictional Acme Analytics, the same program the
> [`tracking-plan`](../tracking-plan/tracking-plan_example.md) and
> [`kpi-dashboard`](../kpi-dashboard/kpi-dashboard_example.md) examples already cover, and the same program
> whose [risk register](../risk-register/risk-register_example.md),
> [RAID log](../raid-log/raid-log_example.md), [issue log](../issue-log/issue-log_example.md), and
> [change log](../change-log/change-log_example.md) Marta Reyes already keeps as its other standing
> governance instruments. `data-dictionary` joined the `governance-docs` family as its seventh member on
> 2026-10-15 under
> [ADR 0073](../../docs/internal/decisions/0073-data-dictionary-joins-governance-docs-as-a-seventh-member.md),
> distinct from the tracking plan upstream of it: the tracking plan specifies the events and properties the
> Reporting product emits, and this document describes what the warehouse columns those events land in
> actually mean. It is dated **2026-09-08**: after the tracking plan's own last review on 2026-08-24, and
> after the Saved Views adoption-nudge experiment closed on 2026-08-31, so the `variant_id` column below is
> documented as a closed test's assignment field, without this document restating what the test found. No
> version-history entry below predates 2026-08-24.
>
> Figures not already fixed by a sibling example, including every table and column name, every type and
> nullability statement, the warehouse's internal grain and join structure, and the review channel name,
> are illustrative: plausible for this document, invented for it, and not drawn from a real company.

# Acme Analytics Reporting Warehouse Data Dictionary

## Purpose and Boundary

This document covers four tables in the warehouse the Reporting product's events land in once Amplitude
exports them: `events`, `report_sessions`, `users`, and `accounts`. It does not catalog which events the
Reporting web app emits or why each one is tracked; a reader after that, including each event's own
business question, wants the [tracking plan](../tracking-plan/tracking-plan_example.md) open instead, and
this document assumes they already have it. It does not fix Time to Insight's formula, inclusions, or
exclusions; the [KPI dashboard](../kpi-dashboard/kpi-dashboard_example.md) already settles those in its
own Metric Definitions section. What this document adds that neither sibling states is the warehouse's own
shape: the table and column names an analyst actually queries, each column's type and nullability as a
schema fact, the keys that enforce each table's grain, and the joins between them.

## Dataset Metadata

**Source system(s):** The nightly Amplitude product-event export (the ten events the tracking plan's Event
and Property Catalog names) and the nightly entitlements-database export (`analyst_segment` and
`migration_reconciled`, the two user and account traits the tracking plan names), both loaded into the
Reporting analytics warehouse.

**Version:** v1.1

**Effective date:** 2026-09-08

**Refresh cadence:** Nightly for both source exports, matching the cadence the tracking plan states for the
entitlements export.

**Primary consumers:** The Looker executive view that implements the KPI dashboard's live metrics, and the
Data Eng team's own debugging queries against the warehouse directly.

## Field Definitions

**Table:** events

**Grain:** One row per event occurrence the Reporting web app logs to Amplitude and the nightly export
lands in this warehouse. **Key column(s):** `event_id` enforces the grain.

| Field | Type and nullability | Definition | Allowed values, units, or missing codes | Source | Sensitivity | Owner |
|---|---|---|---|---|---|---|
| event_id | string, not null | A unique identifier for one logged event occurrence, assigned by the warehouse's nightly load job when the row lands | Free-form; no coding scheme | Assigned at load from the Amplitude export | none | Data Eng |
| event_name | string, not null | Which of the ten events in the tracking plan's Event and Property Catalog this row records | Enum: view_saved, view_switched, view_set_default, view_shared, view_load_error, report_opened, report_exported, report_shared, report_annotated, nudge_variant_assigned | Amplitude export, loaded nightly | none | Data Eng |
| occurred_at | timestamp, not null | When the event fired in the Reporting web app, as Amplitude timestamped it | UTC | Amplitude export | none | Data Eng |
| user_id | string, nullable | The user who fired the event; joins to users.user_id | Free-form; null only on nudge_variant_assigned, the one event the tracking plan ties to the account rather than a user | Amplitude export | none | Data Eng |
| account_id | string, nullable | The account the event's user belongs to; joins to accounts.account_id | Free-form; populated directly on nudge_variant_assigned, where the tracking plan names it as the event's own property; derived at load by joining user_id to accounts for every other event | Direct on nudge_variant_assigned; derived for every other event name | none | Data Eng |
| dashboard_id | string, nullable | The dashboard the event names: the saved view's own dashboard on the five Saved Views events, or the dashboard a report belongs to on report_opened | Free-form; null on report_exported, report_shared, report_annotated, and nudge_variant_assigned | Amplitude export | none | Data Eng |
| view_scope | string, nullable | The saved view's own scope property, carried through unchanged from the tracking plan's property of the same name | Free-form; populated on the five Saved Views events only | Amplitude export | none | Data Eng |
| report_id | string, nullable | The report the event names | Free-form; populated on report_opened, report_exported, report_shared, and report_annotated only | Amplitude export | none | Data Eng |
| reason | string, nullable | Why a saved view failed to load | Enum: filters_removed, permission_denied, timeout, unknown; populated on view_load_error only | Amplitude export | none | Data Eng |
| export_format | string, nullable | The file format a report was exported in | Enum: csv, pdf, image; populated on report_exported only | Amplitude export | none | Data Eng |
| annotation_id | string, nullable | The annotation the event names | Free-form; populated on report_annotated only | Amplitude export | none | Data Eng |
| recipient_user_id_hash | string, nullable | The colleague a view or a report was shared with, already hashed before this warehouse received it | Free-form hash; populated on view_shared and report_shared only; the tracking plan's own retention figure for this column (180 days) is still pending legal confirmation as of this document's date | Amplitude export, hashed in the ingestion pipeline before load | pii | Data Eng |
| variant_id | string, nullable | Which arm of the Saved Views adoption-nudge test the account was assigned to | Free-form; populated on nudge_variant_assigned only; the test closed 2026-08-31, so no row dated after that carries this event name | Amplitude export | none | Data Eng |

**Table:** report_sessions

**Grain:** One row per report-opening session: one row is created for every report_opened event row in the
events table above. **Key column(s):** `report_session_id` enforces the grain.

| Field | Type and nullability | Definition | Allowed values, units, or missing codes | Source | Sensitivity | Owner |
|---|---|---|---|---|---|---|
| report_session_id | string, not null | A surrogate key assigned when this session row is created from its originating report_opened event | Free-form | Assigned at load, one per report_opened row | none | Data Eng |
| report_id | string, not null | The report this session opened; carried through from the originating report_opened event's own property | Free-form; this warehouse does not yet carry a separate reports dimension table, so this column cannot be joined further than the events table it was copied from | Copied from events.report_id at load | none | Data Eng |
| user_id | string, not null | The analyst who opened the report; joins to users.user_id | Free-form | Copied from events.user_id at load | none | Data Eng |
| report_opened_at | timestamp, not null | When the report was opened: the first of Time to Insight's two timestamps | UTC; copied from the originating report_opened event's occurred_at | Derived at load from events | none | Data Eng |
| first_action_at | timestamp, nullable | The earliest occurred_at among this session's report_exported, report_shared, and report_annotated events: the second of Time to Insight's two timestamps | UTC; null until one of the three actions fires for this session | Derived at load from events | none | Data Eng |
| first_action_type | string, nullable | Which of the three logged actions set first_action_at | Enum: report_exported, report_shared, report_annotated; null while first_action_at is null | Derived at load from events | none | Data Eng |

**Table:** users

**Grain:** One row per user. **Key column(s):** `user_id` enforces the grain.

| Field | Type and nullability | Definition | Allowed values, units, or missing codes | Source | Sensitivity | Owner |
|---|---|---|---|---|---|---|
| user_id | string, not null | A unique identifier for one Reporting user | Free-form | Entitlements export | none | Data Eng |
| account_id | string, not null | The account this user belongs to; joins to accounts.account_id | Free-form | Entitlements export | none | Data Eng |
| analyst_segment | string, not null | Which segment this user is classified into, the same property the tracking plan names | Enum: recurring, trialist, internal | Entitlements database, refreshed nightly, the same cadence the tracking plan states | none | Data Eng |

This table carries no column marking a service account. The Weekly active analysts metric's service-account
exclusion, named in the KPI dashboard's Metric Definitions section, is applied outside this warehouse today.
Closing that gap is a known caveat of this table, not a column a reader can look up here yet.

**Table:** accounts

**Grain:** One row per account. **Key column(s):** `account_id` enforces the grain.

| Field | Type and nullability | Definition | Allowed values, units, or missing codes | Source | Sensitivity | Owner |
|---|---|---|---|---|---|---|
| account_id | string, not null | A unique identifier for one Reporting account | Free-form | Entitlements export | none | Data Eng |
| migration_reconciled | boolean, nullable | Whether this account's legacy saved-view configuration has been reconciled against the new schema, the same property the tracking plan names | True, false, or null before the migration cutover runs | Set by the migration reconciliation job at cutover | none | Data Eng |

## Relationships

| This field | Related table and field | Relationship | Notes |
|---|---|---|---|
| events.user_id | users.user_id | Foreign key | Null on nudge_variant_assigned; populated on every other event name |
| events.account_id | accounts.account_id | Foreign key | Direct on nudge_variant_assigned; derived by joining user_id to accounts for every other event name |
| report_sessions.report_id | events.report_id | Derived | Copied from the originating report_opened row; not an enforced foreign key, because no reports dimension table exists yet |
| report_sessions.user_id | users.user_id | Foreign key | The analyst who opened the report |
| users.account_id | accounts.account_id | Foreign key | Every user belongs to exactly one account |

## Validation Rules

| Field | Rule |
|---|---|
| events.event_id | No two rows may share the same value |
| events.occurred_at | Required on every row |
| report_sessions.report_session_id | No two rows may share the same value |
| report_sessions.first_action_at | When populated, must be later than report_opened_at on the same row |
| users.analyst_segment | Must be one of recurring, trialist, internal |
| users.account_id | Required on every row; every user belongs to exactly one account |

## Ownership and Review

**Table owner:** Lee Zhang (Data Eng), who built and maintains this warehouse's schema.

**Table steward:** Lee Zhang (Data Eng).

**How to propose a change:** Propose a change in the #reporting-warehouse channel. Lee Zhang checks a
proposed column against the tracking plan's own event and property names before it is added here.

**Review interval:** Monthly, the Tuesday before the tracking plan's own monthly review, so a schema
question raised here is already settled by the time that review reads events against it. This interval is
Data Eng's own choice, not borrowed from elsewhere.

**Other review triggers:** Every schema change to the warehouse, ahead of the monthly date rather than
waiting for it, the same trigger shape the tracking plan uses for its own event changes.

## Review and Sign-off

**Preparer:** Lee Zhang (Data Eng).

**Reviewer:** Dana Osei (Staff Engineer, Platform).

**Approver:** Marta Reyes (Program Manager, Reporting Platform Modernization).

**Review cycle:** Monthly.

**Status:** Approved.

| Version | Date | What changed | Approved by |
|---|---|---|---|
| v1.0 | 2026-09-01 | Initial dictionary published, covering the events, report_sessions, users, and accounts tables | Marta Reyes |
| v1.1 | 2026-09-08 | events.account_id's Definition cell clarified to state that every event besides nudge_variant_assigned derives account_id by joining user_id to accounts, rather than carrying it directly; and variant_id's allowed-values note updated to record that the adoption-nudge test closed on 2026-08-31 | Marta Reyes |
