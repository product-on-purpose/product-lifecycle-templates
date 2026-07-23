---
title: "{{dashboard_name}} KPI Dashboard"
monitors: "{{objective_or_program}}"
audience: "{{audience_tier}}"
dashboard_owner: "{{dashboard_owner}}"
last_reviewed: "{{date}}"
review_cadence: "{{cadence}}"
status: "{{status}}"
doc_type: kpi-dashboard
size: lean
source_template: kpi-dashboard
source_template_version: 0.1.0
---

<!--
LEAN KPI DASHBOARD SPECIFICATION. The smallest real dashboard spec: what objective it monitors and for whom,
the KPIs themselves (each a metric paired with an objective and target), and the cadence that keeps it alive.
Use it for one team to agree on what it watches and act on it. To grow it into a governance-grade spec (see
kpi-dashboard_template-full.md), ADD sections; never rename or reorder the ones below, because the full
variant is a strict superset of this one.

THIS IS A DASHBOARD DEFINITION, NOT A LIVE TOOL. It specifies which metrics matter, how each is measured, the
target, the owner, and the cadence - platform-agnostic. It precedes and outlives the build in Tableau,
Looker, Power BI, or Amplitude. Write the definition first: if a metric's meaning is unclear, it is useless.
See kpi-dashboard_companion.md section 1.

A KPI IS NOT JUST ANY METRIC. A metric becomes a KPI when it is paired with a specific business objective and
a target. Keep the list short (fewer than ten). Prefer ACTIONABLE metrics - ones that change what you do -
over VANITY metrics that feel good but guide no decision. See kpi-dashboard_companion.md sections 3 and 6.

BEWARE GOODHART'S LAW. "When a measure becomes a target, it ceases to be a good measure." A KPI under
target-pressure gets gamed. Pair headline (lagging) targets with leading indicators, and treat an all-green
dashboard with suspicion, not relief. See kpi-dashboard_companion.md section 6.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a companion pointer), guiding
   questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid. Tables add PRIORITY and ROW HINT.
2. Replace each {{placeholder}}. Give every KPI a target and one named owner.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Never finished, but before you share it: self-grade against kpi-dashboard_guide.md, then DELETE every HTML
   comment.
-->

# {{dashboard_name}} KPI Dashboard

## Purpose and Audience

<!-- WHAT  What objective this dashboard monitors, who reads it (audience tier), and the review cadence. One
           short block.
     WHY   The audience determines everything downstream: an executive dashboard is 3-5 headline metrics, an
           operational one is dozens refreshed in minutes, an analytical one is for data-literate users. Name
           the objective the metrics serve, or the dashboard is a pile of numbers. Deep dive:
           kpi-dashboard_companion.md section 3 (Purpose and Audience).
     ASK   What objective or program does this monitor? Who is the audience (executive / operational /
           analytical)? How often is it reviewed, and by whom?
     GOOD  "Monitors progress toward the Reporting Platform Modernization program's value goal (cut Time to
           Insight 30% by Q3). Audience: the program steering group (strategic). Reviewed monthly; owned by
           the program manager."
     WEAK  "A dashboard of our metrics." (no objective, no audience, no cadence; nothing to judge the metrics
           against)
     TRAP  Building for "everyone." A dashboard that serves executives and analysts at once serves neither;
           pick the audience and design for it. -->

{{purpose_and_audience}}

## KPIs

<!-- WHAT  The key performance indicators, one row each: name, a one-line definition, the target, the current
           value, the trend, whether it is leading or lagging, and the owner.
     WHY   This is the dashboard. A KPI is a metric paired with an objective and a target - not every metric
           qualifies. SMART (specific, measurable, achievable, relevant, time-bound) is the quality bar. Mark
           leading vs lagging: leading indicators can be acted on; lagging ones only confirm the past. Deep
           dive: kpi-dashboard_companion.md section 3 (KPIs).
     ASK   For each KPI: what is measured (in one line)? What is the target, and by when? What is the current
           value and trend? Is it leading (predictive, actionable) or lagging (confirms past)? Who owns it?
     PRIORITY  Keep it short (under ten; 5-9 is what the eye holds). Order by importance, headline metrics
           first. Owner is one named person. Every KPI has a target - a metric with no target is not a KPI.
     ROW HINT  A good row is a SMART, actionable metric with a target and an owner. A weak row is a vanity
           number (goes up, guides no decision) or a metric with no target.
     GOOD  | Time to Insight | Median minutes from opening a report to acting | -30% vs baseline by Q3 | -18% | improving | leading | Priya Nair |
     WEAK  | Page views | Total report page views | (no target, no objective; a vanity metric) | 2.1M | up | | |
     TRAP  Vanity metrics and metric bloat. Ask of every row: "if this moved, what would we do differently?"
           If the answer is nothing, it does not belong. Thirty metrics is not a dashboard; it is noise. -->

| KPI | Definition (one line) | Target | Current | Trend | Lead/Lag | Owner |
|---|---|---|---|---|---|---|
| {{kpi_name}} | {{definition}} | {{target}} | {{current}} | {{trend}} | {{lead_lag}} | {{owner}} |

## Review and Ownership

<!-- WHAT  How often the dashboard is reviewed, who owns it, and what happens when a metric turns red. A few
           lines.
     WHY   A dashboard is an instrument for a review meeting; the meeting is where value is created or lost.
           An exception-driven review (discuss what moved, not every green metric) plus a clear escalation
           when a metric goes red is what keeps the dashboard a decision tool, not wallpaper. Deep dive:
           kpi-dashboard_companion.md section 3 (Review and Ownership).
     ASK   How often is the dashboard reviewed, and by whom? Is the review exception-driven (focus on what
           changed)? Who owns the dashboard overall? What action triggers when a KPI turns red?
     GOOD  "Reviewed monthly by the steering group, exception-driven (owners speak only to metrics off-target
           or off-trend). The program manager owns the dashboard; each KPI has a named owner. A red KPI gets
           a root-cause and an action item at the review. Last reviewed 2026-07-20."
     WEAK  "Reviewed periodically." (no cadence, no owner, no escalation; the dashboard becomes wallpaper)
     TRAP  A review where every metric is green and everyone nods. The most dangerous dashboard is the one
           that is all green; either the targets are too soft or the risks are tracked nowhere. Read it
           beside the risk register. -->

{{review_and_ownership}}
