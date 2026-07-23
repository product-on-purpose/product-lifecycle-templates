---
title: "Acme Analytics - Reporting Platform Modernization KPI Dashboard"
monitors: "Reporting Platform Modernization program (value goal: cut Time to Insight 30% by Q3)"
audience: "Program steering group (strategic)"
dashboard_owner: "Marta Reyes (Program Manager)"
last_reviewed: "2026-07-20"
review_cadence: "Monthly, exception-driven, at the program steering review"
status: active
related: ["../risk-register/risk-register_example.md (the program risk register; tracks threats to these outcomes)", "../raid-log/raid-log_example.md (the program RAID log; tracks open items behind these outcomes)", "../prd/prd_example.md (Saved Views for Dashboards PRD, where the Time to Insight goal is set)"]
doc_type: kpi-dashboard
size: full
source_template: kpi-dashboard
source_template_version: 0.1.0
---

<!--
This is a worked example for the kpi-dashboard bundle: a realistic, fully filled full-variant KPI dashboard
SPECIFICATION (not a live BI tool) for the same Acme Analytics Reporting Platform Modernization program that
the risk-register and raid-log examples cover. It closes the governance-docs family loop:
- the risk register tracks THREATS to the program's objectives;
- the RAID log tracks OPEN ITEMS (risks, assumptions, issues, dependencies) behind them;
- this dashboard tracks whether the delivered program actually WORKS.
The cross-links are deliberate: Saved Views adoption is the outcome the register's R-04 adoption risk
threatens and the RAID log's A-02 assumption underlies; view-list load is the metric the RAID log's ISS-12
issue (from register risk R-06) moved.

All figures, targets, dates, and names are illustrative. This is a snapshot as of the last-reviewed date. Use
it as a model of shape, definition discipline, and tone, not as a source of facts about real products.
-->

# Acme Analytics - Reporting Platform Modernization KPI Dashboard

## Purpose and Audience

Monitors **progress toward the Reporting Platform Modernization program's value goal**: cut the median Time to
Insight for Recurring Analysts by 30% by the end of Q3 (the goal set in the
[Saved Views PRD](../prd/prd_example.md)). **Audience:** the program steering group (strategic tier) - a
handful of headline metrics, reviewed monthly. Owned by the program manager (Marta Reyes).

**This document is the metric source of truth**; the live dashboard is implemented in the Acme BI workspace
(Amplitude for product events, Looker for the executive view). Where the live dashboard and this spec
disagree, this spec wins. It is read **beside the [risk register](../risk-register/risk-register_example.md)**:
this dashboard shows whether the program is working; the register shows what could stop it.

## KPIs

Headline first. *(Illustrative.)*

| KPI | Definition (one line) | Target | Current | Trend | Lead/Lag | Owner |
|---|---|---|---|---|---|---|
| Time to Insight | Median minutes from opening a report to taking a logged action | -30% vs baseline by Q3 | -18% | improving | lagging | Priya Nair |
| Saved Views adoption | Share of Recurring Analysts using a saved view weekly | 60% by end Q3 | 41% | improving | leading | Priya Nair |
| View-list load (p95) | 95th-percentile time to render a dashboard's saved-view list | < 500ms | 620ms | declining | leading | Dana Osei |
| Weekly active analysts | Distinct Recurring Analysts active in the trailing 7 days | Hold >= 480 | 495 | stable | lagging | Priya Nair |
| Migration integrity | Share of legacy saved-view configs reconciled post-cutover | 100% at cutover | n/a (pre-cutover) | n/a | leading | Lee Zhang |

## Metric Definitions

Locked definitions - another team should compute the same number from these. *(Illustrative.)*

**Time to Insight.** Formula: median over the period of (timestamp of first logged action on a report -
timestamp the report was opened), in minutes, per analyst-session. **Includes:** Recurring Analysts (the
segment the program targets); sessions with at least one report opened. **Excludes:** trialists, internal test
accounts, sessions with no report opened. **Grain:** per analyst-session, reported as a monthly median.
**Lagging** (the program's headline outcome; a monthly median confirms whether the delivered feature improved
analyst efficiency, and by the time it is read the period is over - its leading drivers are adoption and
performance below). **Known limitation:** "action" is proxied by a set of logged events (export, share,
annotate); a purely visual read that changes a decision is not captured. **Owner:** Priya Nair. **Data
steward:** Lee Zhang (Data Eng).

**Saved Views adoption.** Formula: (distinct Recurring Analysts who used a saved view in the trailing 7 days)
/ (all Recurring Analysts). **Includes:** analysts active in the period. **Excludes:** trialists, internal
accounts. **Grain:** per analyst, trailing-7-day, reported monthly. **Leading** (a behavioral input that predicts the
Time-to-Insight outcome: if adoption rises, Time to Insight should follow). **Known limitation:** a shared
view counts for the viewer, not the creator, so heavy sharing can understate creator adoption. **Owner:**
Priya Nair. **Data steward:** Lee Zhang. *(This is the outcome the
[register's R-04 adoption risk](../risk-register/risk-register_example.md) threatens and the
[RAID log's A-02 assumption](../raid-log/raid-log_example.md) rests on.)*

**View-list load (p95).** Formula: 95th percentile of the client-measured time from view-list request to
render, in milliseconds. **Includes:** production sessions. **Excludes:** synthetic monitoring traffic.
**Grain:** per request, p95 over a trailing 24 hours. **Leading** (a degradation predicts the adoption and
Time-to-Insight risk before they move). **Known limitation:** client-measured, so it includes network time
outside Acme's control. **Owner:** Dana Osei. **Data steward:** Lee Zhang (Data Eng). *(This is the metric the
[RAID log's ISS-12](../raid-log/raid-log_example.md), which materialized from register risk R-06, moved.)*

**Weekly active analysts.** Formula: count of distinct Recurring Analysts with at least one report session in
the trailing 7 days. **Includes:** the Recurring Analyst segment. **Excludes:** trialists, internal accounts,
service accounts. **Grain:** per analyst, trailing-7-day, reported weekly. **Lagging** (an engagement outcome;
a guardrail that the program is not driving analysts away). **Known limitation:** multi-device use is
de-duplicated on analyst identity, not device, so a shared login understates the count. **Owner:** Priya Nair.
**Data steward:** Lee Zhang (Data Eng).

**Migration integrity.** Formula: (count of legacy saved-view configs reconciled against the new schema) /
(count of legacy configs in scope), as a percentage. **Includes:** all in-scope legacy configs at cutover.
**Excludes:** configs already deleted by their owners pre-migration. **Grain:** whole-migration, measured at
the cutover dry-run and at cutover. **Leading** (a cutover-quality gate: a shortfall predicts the data-loss
risk R-02 materializing). **Known limitation:** reconciliation matches on config ID and field count, not
semantic equivalence of every field. **Owner:** Lee Zhang. **Data steward:** Lee Zhang (Data Eng). *(Gates the
[register's R-02 data-loss risk](../risk-register/risk-register_example.md).)*

## Layout and Thresholds

RAG bands are set to the program's targets, not a generic scale. *(Illustrative.)*

| KPI | Green | Amber | Red | Chart | Escalation when red |
|---|---|---|---|---|---|
| Time to Insight | >= 25% improvement | 10-25% | < 10% | Line, trailing 6 months + target line | Steering group within 1 week, with root-cause |
| Saved Views adoption | >= 55% | 40-55% | < 40% | Line, trailing 6 months | Product review; feeds the R-04 mitigation |
| View-list load (p95) | < 500ms | 500-700ms | > 700ms | Line, trailing 30 days | Eng on-call same day (currently amber at 620ms) |
| Weekly active analysts | >= 480 | 460-479 | < 460 | Sparkline, trailing 30 days | Product review within 1 week (guardrail metric) |
| Migration integrity | 100% | n/a | < 100% | Single-value tile, cutover window only | Lee Zhang same day, with a reconciliation report |

**Layout:** Time to Insight and Saved Views adoption are the two headline panels; view-list load and weekly
active analysts are supporting; migration integrity is a cutover-window panel, hidden afterward. Everything
else (per-segment breakdowns) is drill-down.

## Data Sources and Refresh

*(Illustrative.)*

| KPI | Source of record | Refresh | Latency | Do NOT use |
|---|---|---|---|---|
| Time to Insight | Product analytics event stream (Amplitude) | Automated daily | ~6h | The marketing "engagement" metric (different "session" definition) |
| Saved Views adoption | Entitlements DB + event stream | Automated nightly | ~12h | Manual pilot spreadsheet (pilot-only; not the full segment) |
| View-list load (p95) | Front-end RUM pipeline | Automated hourly | ~1h | Staging load-test numbers (not production) |
| Weekly active analysts | Entitlements DB + event stream (same pipeline as adoption) | Automated nightly | ~12h | The raw session log (double-counts multi-device) |
| Migration integrity | Migration reconciliation script output (the R-02 dual-write reconciler) | Automated per dry-run and at cutover | minutes | Manual spot-checks (not exhaustive) |

No headline metric is entered by hand: an automated feed is a condition of a metric appearing on this
dashboard.

## Review and Ownership

Reviewed **monthly** by the program steering group, **exception-driven**: owners speak only to metrics that
are off-target or off-trend, and come prepared with the **input metrics** behind them, not just the headline
number. The program manager owns the dashboard; each KPI has a named owner. A **red** KPI gets a root-cause
and an action item at the review.

The dashboard is read **beside the [risk register](../risk-register/risk-register_example.md)**: by the bands
above, Time to Insight (-18% vs the 25% green line) and Saved Views adoption (41% vs the 55% green line) are
both **amber and improving**, view-list load is amber, and the register still carries the adoption risk (R-04)
and the PII risk (R-05) as open threats. This is exactly the picture the family is built to show - amber
headline metrics trending the right way while real risks stay live - and an all-green dashboard here would be
treated with suspicion, not relief. Last reviewed **2026-07-20**; next review **2026-08-17**.

*(All KPIs, targets, figures, and names are illustrative.)*
