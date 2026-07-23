# Guide: KPI Dashboard (operator card)

Fast reference for using the kpi-dashboard bundle. For the full reasoning, history, and sources, read
[`kpi-dashboard_companion.md`](kpi-dashboard_companion.md).

**First, the scope:** this bundle is a document that **defines** a dashboard - which metrics matter, how each
is measured, targeted, owned, and reviewed. It is platform-agnostic and precedes the build in Tableau,
Looker, Power BI, or Amplitude. It is not the live tool.

## When to use

- You need to **agree, in writing, on the few metrics** that show whether an objective is being met - and
  exactly how each is calculated.
- Metrics are **disputed** across teams ("our number says X, yours says Y") and you need locked definitions.
- Someone **other than the author** will build the live dashboard, and needs a spec to build from.
- You want a **standing monitoring instrument** for progress toward objectives, reviewed on a cadence.

## When NOT to use

- **You are choosing objectives, not monitoring them.** That is OKRs (the objective and its key results). The
  dashboard monitors the KPIs; it does not set the direction. Use both, in sequence.
- **You want a periodic snapshot against targets, not live monitoring.** That is a scorecard. A dashboard
  monitors current state; a scorecard compares actual to target at a point in time.
- **You are reporting project status.** That is a status report (completion against a plan), not an ongoing
  performance monitor.
- **You have no objective to measure against.** A dashboard with no objective above it is a pile of numbers.
  Name the objective first, or you are collecting vanity metrics.

## Dashboard, OKRs, scorecard, or risk register? (the question people actually have)

| | **KPI dashboard** | **OKRs** | **Scorecard** | **Risk register** |
|---|---|---|---|---|
| Answers | "How are we doing, live?" | "Where are we going, by when?" | "Above or below target, this period?" | "What could stop us?" |
| Direction | Monitors progress | Sets direction | Compares to target | Tracks threats |
| Cadence | Continuous | Quarterly | Periodic snapshot | Weekly-to-quarterly |
| In this family | this bundle | (strategy-docs) | (a dashboard variant) | [`risk-register`](../risk-register/risk-register_guide.md) |

The dashboard and the **risk register** are governance siblings: the dashboard tracks **progress toward**
objectives, the register tracks **threats to** them. Read them together - a green dashboard beside an
unreviewed register is a program performing today while accumulating exposure for tomorrow.

## Pick a variant

- **Lean** (default): Purpose and Audience, KPIs, Review and Ownership. Enough for one team to agree what it
  watches and act on it.
- **Full**: adds Metric Definitions (formula, inclusions/exclusions, owner and data steward), Layout and
  Thresholds (RAG bands and escalation), and Data Sources and Refresh. Use it when the dashboard feeds
  governance, when teams must agree what a metric means, or when someone else builds it on a BI platform.

Grow lean into full by adding sections; never reorder the shared three. The scaling signal is **stakes and
audience**, not the number of charts.

## Quality rubric (self-grade)

- [ ] The dashboard **names the objective** it monitors and the **audience** it serves.
- [ ] Every row is a **KPI** (a metric paired with an objective and a **target**), not a bare metric.
- [ ] Metrics are **actionable**: for each, "if it moved, we would do X." No vanity numbers.
- [ ] The list is **short** (under ten; 5-9 on any one view), not thirty metrics of noise.
- [ ] Each KPI is marked **leading or lagging**, and headline lagging targets are paired with leading
      indicators.
- [ ] Every KPI has **one named owner**.
- [ ] There is a **stated review cadence** and the last-reviewed date is current.
- [ ] (Full) Each KPI has a **locked definition** with inclusions/exclusions, formula, grain, and a data
      steward distinct from the owner.
- [ ] (Full) **RAG thresholds** are defined numerically, with an escalation rule when a metric is red.
- [ ] (Full) Each metric names an **automated source of record**; nothing critical is entered by hand.
- [ ] The dashboard is read **beside the risk register**, and an all-green dashboard is treated with
      suspicion.

## Named anti-patterns (the usual wrecks)

1. **The vanity dashboard.** Numbers that go up and to the right but guide no decision. Fix: keep only metrics
   that change what you do.
2. **The gamed metric (Goodhart).** A KPI that became a target and is now optimized directly, decoupled from
   the outcome. Fix: pair lagging targets with leading indicators; watch for the metric improving while the
   outcome does not.
3. **The ambiguous metric.** No locked definition, so every team has its own number and reviews argue about
   data. Fix: define inclusions/exclusions, formula, grain, and source.
4. **Dashboard bloat.** Thirty metrics on one view. Fix: a three-tier hierarchy (headline / supporting /
   drill-down).
5. **The orphaned metric.** No owner, so no one can act when it moves. Fix: one named owner per KPI, distinct
   from the data steward.
6. **The all-green dashboard.** Every metric green, because the targets are soft or the risks are tracked
   nowhere. Fix: honest targets, and read it beside the risk register.

## No paired skill (yet)

There is **no `deliver-kpi-dashboard` or `govern-kpi-dashboard` skill** in the product-on-purpose org today,
so this bundle's `pairs_with` is empty. Until one exists, this template is filled by hand.
