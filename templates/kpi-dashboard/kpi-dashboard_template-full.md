---
title: "{{dashboard_name}} KPI Dashboard"
monitors: "{{objective_or_program}}"
audience: "{{audience_tier}}"
dashboard_owner: "{{dashboard_owner}}"
last_reviewed: "{{date}}"
review_cadence: "{{cadence}}"
status: "{{status}}"
doc_type: kpi-dashboard
size: full
source_template: kpi-dashboard
source_template_version: 0.1.0
---

<!--
FULL KPI DASHBOARD SPECIFICATION. The governance-grade spec: everything in the lean variant, plus a detailed
Metric Definitions section (formula, inclusions/exclusions, owner and data steward), a Layout and Thresholds
section (RAG bands and escalation), and a Data Sources and Refresh section. Use it when the dashboard feeds
governance, when multiple teams must agree what a metric means, or when someone other than the author will
build it on a BI platform.

This is a STRICT SUPERSET of kpi-dashboard_template-lean.md: Purpose and Audience, KPIs, and Review and
Ownership appear in the same relative order; full only inserts the three detail sections. If you are growing
from lean, add them; do not reorder.

THIS IS A DASHBOARD DEFINITION, NOT A LIVE TOOL. Platform-agnostic; it precedes and outlives the Tableau /
Looker / Power BI / Amplitude build. The Metric Definitions section is the point of the full variant: without
locked definitions, every dashboard becomes a new version of the truth, and governance meetings drift into
arguments about data quality rather than action. See kpi-dashboard_companion.md sections 1 and 3.

A KPI IS NOT JUST ANY METRIC (paired with an objective and target). Prefer ACTIONABLE over VANITY metrics.
BEWARE GOODHART'S LAW ("when a measure becomes a target, it ceases to be a good measure") - pair lagging
targets with leading indicators, and treat an all-green dashboard with suspicion. See kpi-dashboard_companion.md
sections 3 and 6.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP; tables
   add PRIORITY and ROW HINT.
2. Replace each {{placeholder}}. Every KPI has a target, one named owner, and (in Metric Definitions) a data
   steward and a locked formula.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Never finished, but before you share it: self-grade against kpi-dashboard_guide.md, then DELETE every HTML
   comment.
-->

# {{dashboard_name}} KPI Dashboard

## Purpose and Audience

<!-- WHAT  What objective this dashboard monitors, the audience tier, the review cadence, and its relationship
           to the live BI implementation.
     WHY   The audience determines metric count, refresh rate, and depth. At governance scale, also state that
           this is the spec (the source of truth for what each metric means) and where it is implemented.
           Deep dive: kpi-dashboard_companion.md section 3 (Purpose and Audience) and section 8 (vs the BI
           tool).
     ASK   What objective does this monitor? Audience (executive / operational / analytical)? Cadence? Which
           BI platform implements it, and who keeps the implementation in sync with this spec?
     GOOD  "Monitors progress toward the Reporting Platform Modernization program's value goal (cut Time to
           Insight 30% by Q3). Audience: program steering group (strategic). Reviewed monthly. This document
           is the metric source of truth; implemented in the Acme BI workspace (Amplitude + Looker)."
     WEAK  "Program metrics dashboard." (no objective, audience, cadence, or implementation link)
     TRAP  Letting the spec and the live dashboard drift. This document defines the metrics; the BI tool
           renders them. When they disagree, this document wins - so keep it current. -->

{{purpose_and_audience}}

## KPIs

<!-- WHAT  The key performance indicators, one row each: name, one-line definition, target, current, trend,
           lead/lag, and owner. The summary view; the detailed definitions are the next section.
     WHY   A KPI is a metric paired with an objective and target; SMART is the quality bar. Keep it short
           (5-9). Mark leading vs lagging so the dashboard shows both what you can act on now and what you can
           only confirm later. Deep dive: kpi-dashboard_companion.md section 3 (KPIs).
     ASK   For each KPI: one-line definition? target and by when? current and trend? leading or lagging? owner?
     PRIORITY  Under ten; headline metrics first. Every KPI has a target. Owner is one named person. The
           full definition (formula, inclusions/exclusions) lives in Metric Definitions below, linked by name.
     ROW HINT  A good row is a SMART, actionable metric with a target and an owner. A weak row is a vanity
           number or a metric with no target.
     GOOD  | Time to Insight | Median minutes from opening a report to acting | -30% vs baseline by Q3 | -18% | improving | leading | Priya Nair |
     WEAK  | Page views | Total report page views | (no target; vanity) | 2.1M | up | | |
     TRAP  Metric bloat and vanity. Ask of each: "if this moved, what would we do?" If nothing, cut it. -->

| KPI | Definition (one line) | Target | Current | Trend | Lead/Lag | Owner |
|---|---|---|---|---|---|---|
| {{kpi_name}} | {{definition}} | {{target}} | {{current}} | {{trend}} | {{lead_lag}} | {{owner}} |

## Metric Definitions

<!-- WHAT  The detailed definition record for each KPI: exact formula (numerator/denominator), inclusions and
           exclusions, grain and time window, leading/lagging, known limitations, the owner, and the data
           steward.
     WHY   This is the anti-ambiguity layer and the point of the full variant. The most dispute-generating
           omission is inclusions/exclusions. Without locked definitions, every dashboard becomes a new
           version of the truth. The owner is accountable for performance and interpretation; the data steward
           for data integrity - two distinct roles. Deep dive: kpi-dashboard_companion.md section 3 (Metric
           Definitions).
     ASK   For each KPI: exact formula? What is included and excluded (the critical part)? What grain and time
           window? Leading or lagging? Known limitations or edge cases? Owner and data steward?
     ROW HINT  A good definition is one another team could compute the same number from. A weak one is a name
           with no formula, so two teams produce two numbers and the review argues about which is right.
     GOOD  "Saved Views adoption = (distinct Recurring Analysts who used a saved view in the trailing 7 days)
           / (all Recurring Analysts). Includes: analysts active in the period. Excludes: trialists, internal
           test accounts. Grain: per analyst, trailing-7-day. Lagging. Limitation: a shared view counts for
           the viewer, not the creator. Owner: Priya Nair. Data steward: Lee Zhang (Data Eng)."
     WEAK  "Adoption: how many people use saved views." (no formula, no inclusions/exclusions; ungovernable)
     TRAP  Skipping inclusions/exclusions. "Active users" means five different things until you say whether a
           trialist counts. The undefined edge case is where every metric dispute starts. -->

{{metric_definitions}}

## Layout and Thresholds

<!-- WHAT  The visual specification: the layout (which metrics go where, for which audience), the chart type
           per metric, the red/yellow/green threshold bands, and the escalation rule when a metric turns red.
     WHY   Most KPI dashboards fail on design, not data. Color means status, not decoration; a consistent RAG
           scheme plus a stated escalation turns metrics into actionable responsibilities. A three-tier
           layout (headline / supporting / drill-down) keeps any one view within what the eye can hold. Deep
           dive: kpi-dashboard_companion.md section 3 (Layout and Thresholds).
     ASK   What is the layout (headline metrics, supporting, drill-down)? Chart type per metric (line for
           trend, bar for comparison, gauge for status)? RAG threshold bands per KPI? Who is escalated to
           when a metric is red, and how fast?
     PRIORITY  One row per KPI, in the same order as the KPIs table (headline metrics first). Every KPI on
           the dashboard needs a band and an escalation - do not leave any KPI unthresholded.
     ROW HINT  A good threshold row states the metric, the green/amber/red bands, and the escalation. A weak
           one colors a metric red with no band definition and no action.
     GOOD  "Time to Insight: green >=25% improvement, amber 10-25%, red <10%. Line chart, trailing 6 months
           with target line. Red escalates to the steering group within one week with a root-cause. Layout:
           Time to Insight and Adoption headline; performance and engagement supporting; the rest drill-down."
     WEAK  "Use red/yellow/green." (no bands defined, no escalation, no layout; color becomes decoration)
     TRAP  Coloring without defined bands. "Red" that anyone can argue into "amber" is theater; state the
           numeric band and the action it triggers. -->

{{layout_and_thresholds}}

## Data Sources and Refresh

<!-- WHAT  The system of record for each metric, its refresh cadence and latency, and the non-approved sources
           to avoid.
     WHY   A dashboard with an undocumented or manual source rots: a dashboard that requires manual data entry
           has an expiration date. Naming the approved source (and the ones NOT to use) is what makes "single
           source of truth" a governance decision rather than a slogan. Deep dive: kpi-dashboard_companion.md
           section 3 (Data Sources and Refresh).
     ASK   For each metric: what is the approved system of record? How is it refreshed (automated feed? how
           often? what latency)? Are there tempting non-approved sources to explicitly rule out?
     PRIORITY  One row per KPI, same order as the KPIs table. Every KPI needs a named source; a metric with
           no documented source of record does not belong on the dashboard.
     ROW HINT  A good row names the source, the refresh, and the latency. A weak one says "our database" with
           no table, pipeline, or cadence.
     GOOD  "Time to Insight: source = product analytics event stream (Amplitude), automated daily refresh,
           ~6h latency. Do NOT use the marketing dashboard's session metric (different definition of a
           'session'). Adoption: source = the entitlements DB, nightly."
     WEAK  "Data comes from our systems." (no source of record, no refresh, no latency; the number is
           untrustworthy)
     TRAP  A manual refresh. A metric a human copies in by hand will go stale the first busy week and the
           dashboard will quietly lie. Automate the feed or mark the metric as manual and short-lived. -->

{{data_sources_and_refresh}}

## Review and Ownership

<!-- WHAT  The review cadence, the dashboard owner, the audience-appropriate review, and what happens when a
           metric is red.
     WHY   The dashboard is an instrument for a review meeting; exception-driven reviews (discuss what moved,
           not every green) and a clear red-metric escalation keep it a decision tool. Discuss inputs, not
           just outputs - output metrics lag the inputs you can actually act on. Deep dive:
           kpi-dashboard_companion.md section 3 (Review and Ownership) and section 6.
     ASK   How often is the dashboard reviewed, by whom? Is it exception-driven? Who owns it? What triggers
           when a KPI is red? Do owners come prepared to explain inputs, not just report outputs?
     GOOD  "Reviewed monthly by the steering group, exception-driven; owners speak to metrics off-target or
           off-trend and come prepared with the input metrics behind them. The program manager owns the
           dashboard; each KPI has a named owner. A red KPI gets a root-cause and an action item. Last
           reviewed 2026-07-20."
     WEAK  "Reviewed at meetings." (no cadence, owner, or escalation)
     TRAP  A status-theater review where every metric is green and no decision is made. The most dangerous
           dashboard is all green; read it beside the risk register, and if nothing is ever red, question the
           targets. -->

{{review_and_ownership}}
