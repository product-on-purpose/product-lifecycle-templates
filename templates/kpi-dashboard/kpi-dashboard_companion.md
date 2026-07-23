# Companion: The KPI Dashboard

> The deep explainer for the kpi-dashboard bundle. Read this to understand what a KPI dashboard is, where it
> came from, why it is shaped the way it is, and where practitioners disagree about it. The short operator
> card is [`kpi-dashboard_guide.md`](kpi-dashboard_guide.md); a fully worked instance is
> [`kpi-dashboard_example.md`](kpi-dashboard_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A KPI dashboard is **the defined set of key performance indicators an organization watches to know whether it
is making progress toward its objectives, and the specification of how each one is measured, targeted, owned,
and reviewed.** A dashboard is *"a visual display of different metrics"* [[9]](#ref-9); the KPIs on it are the
*"critical, quantifiable measures of progress toward a desired result"* [[2]](#ref-2).

**The load-bearing scope fact, stated first because it shapes everything: this bundle is a document that
DEFINES a dashboard - not a live BI tool.** It specifies which metrics matter, exactly how each is
calculated, what the target is, who owns it, where the data comes from, and when it is reviewed. That
specification is platform-agnostic; it precedes and outlives the build in Tableau, Looker, Power BI, or
Amplitude [[21]](#ref-21). The reason to write it down is blunt: *"A good metric therefore always has a clear,
practical meaning. If a metric's meaning is unclear, it is useless"* [[9]](#ref-9), and without a locked
definition *"every dashboard becomes a new version of the truth"* [[11]](#ref-11).

The honest second thing to know is that the KPI dashboard is **the artifact most exposed to the corrupting
power of measurement.** Goodhart's Law - *"when a measure becomes a target, it ceases to be a good measure"*
[[31]](#ref-31) - is aimed squarely at it, and so is the vanity-metric critique: one of *"the numbers that
make you feel good but seriously mislead"* [[30]](#ref-30). This bundle teaches the dashboard that survives both,
and section 6 states the argument in full.

**At a glance**
- A KPI is not just any metric. *"A metric becomes a KPI when it's paired with a specific business objective
  and target"* [[3]](#ref-3). Not everything measured belongs on the dashboard.
- An indicator shows *"whether progress is being made towards a goal, rather than the goal itself"*
  [[1]](#ref-1).
- Every metric needs a **locked definition** (formula, inclusions/exclusions, source) and **one named owner**
  [[10]](#ref-10)[[11]](#ref-11).
- Prefer **actionable** metrics over vanity ones: a good metric changes what you do [[30]](#ref-30).
- Keep it small. *"Humans can effectively process 5-9 pieces of information at once"* [[17]](#ref-17), and
  *"most KPI dashboards fail on design, not data"* [[17]](#ref-17).

If you read nothing else: a KPI dashboard is a **specified, owned, small set of actionable measures of
progress toward objectives.** The moment its metrics are vanity numbers, ambiguously defined, or gamed
because they became the target, it has stopped telling you the truth.

---

## 2. Origins and evolution

**The dashboard's name is a car metaphor, and the metaphor is load-bearing.** The word began as the *"wooden
board carriage makers attached to the front of carriages to prevent mud and rocks from being splashed (or
'dashed')"* onto passengers, and only in the early 1900s were *"'dashboards'... repurposed to house vehicle
instruments, like speedometers and gas gauges"* [[5]](#ref-5). The management artifact borrows exactly that:
a small panel of the few gauges you must watch while driving.

**The intellectual lineage runs through three strands.** First, in 1979 John Rockart's Critical Success
Factors gave executives a way to choose *which* few things to watch - *"those performance factors which must
receive the on-going attention of management if the company is to remain competitive"* [[8]](#ref-8) - which
is the root of the "key" in KPI. Second, the computing strand: Executive Information Systems in the 1980s put
those factors on a screen, evolving into the business-intelligence dashboard, *"a type of graphical user
interface which often provides at-a-glance views of data relevant to a particular objective..."* [[4]](#ref-4).
Third, the measurement-theory strand: Kaplan and Norton's 1992 **Balanced Scorecard** argued that *"traditional
financial accounting measures... can give misleading signals for continuous improvement and innovation"*
[[6]](#ref-6) and that *"financial measures tell the story of past events... [and are] inadequate... for
guiding and evaluating the journey that information age companies must make"* [[7]](#ref-7). Their four
perspectives (financial, customer, internal process, learning and growth) gave dashboards their category
vocabulary.

**The through-line is Kaplan and Norton's four-word warning: *"What you measure is what you get"*
[[6]](#ref-6).** Every debate in section 6 is a consequence of taking that sentence seriously.

---

## 3. Anatomy (section by section)

A KPI dashboard specification is, at its heart, a **table of KPIs** plus the definitions and rules that make
that table trustworthy. This section walks the parts; the template groups them into sections you fill.

### Purpose and Audience

**What it is:** what objective this dashboard monitors, who reads it, and at what cadence. **Why it exists:**
the audience determines everything downstream - metric count, refresh rate, and depth. The three canonical
tiers are **strategic/executive** (*"tracks long-term company performance against enterprise-wide goals"*),
**operational** (*"your real-time data command center... short-term performance and daily operations"*), and
**analytical** (*"deep analysis, using complex and historical datasets"*) [[18]](#ref-18). An executive
dashboard carries 3-5 headline metrics; an operational one carries dozens refreshed in minutes; an analytical
one *"should only serve users that are data literate"* [[35]](#ref-35).

### KPIs (the table)

**What it is:** the heart of the dashboard - one row per KPI, each carrying at minimum a **name**, a
**definition**, a **target**, the **current value**, a **trend**, and an **owner**. **Why each field:**

- **KPI, not metric.** A row earns its place only when it is a metric *"paired with a specific business
  objective and target"* [[3]](#ref-3); everything else is a supporting metric, not a KPI. Keep the list
  short - fewer than ten is a common practitioner ceiling [[16]](#ref-16).
- **SMART.** A good KPI is Specific, Measurable, Achievable, Relevant, and Time-bound: "increase organic
  traffic by 20% this quarter" beats "increase organic traffic" [[16]](#ref-16), and the time-bound target is
  what, in SimpleKPI's phrase, *"creates urgency and aids planning"* [[15]](#ref-15).
- **Target and current.** The target is the goal (absolute or directional); the current value is the measured
  result. Together they answer "are we on track?"
- **Trend.** A directional signal (improving/declining/stable), because a single number without a trajectory
  hides whether you are winning or losing.
- **Leading or lagging.** Mark which. A **leading** indicator is *"a predictive measurement that can influence
  change"*; a **lagging** one is *"an output measurement that can only record what has happened"* and is
  *"useless when attempting to influence the future"* [[13]](#ref-13). The practical stakes: *"by the time you
  determine last month's MRR, it's too late to change it"* [[14]](#ref-14). Use both - *"a combination of
  indicators results in enhanced business performance overall"* [[13]](#ref-13).
- **Owner.** One named person accountable for the metric's performance and interpretation [[10]](#ref-10).

### Metric Definitions (full variant)

**What it is:** the detailed definition record behind each KPI - the *"purpose, numerator, denominator,
inclusion rules, exclusion rules, data source, refresh frequency, threshold, owner, data steward, known
limitations, and review cadence"* [[10]](#ref-10). **Why it exists:** this is the anti-ambiguity governance
layer. The most dispute-generating omission is **inclusions and exclusions** - marked *"critical!"* by
practitioners [[11]](#ref-11) - because *"if KPI definitions aren't locked then every dashboard becomes a new
version of the truth"* [[11]](#ref-11) and *"governance meetings drift into arguments about data quality
rather than action"* [[10]](#ref-10). It also names two distinct roles: the **owner** (accountable for
performance and interpretation) and the **data steward** (accountable for data integrity and reproducibility)
- *"metric ownership is not a title on a chart"* [[10]](#ref-10). A dashboard is only *"decision-grade when
the organization can explain what each metric means, who owns it, how the data is produced, and what happens
when the number changes"* [[10]](#ref-10).

### Layout and Thresholds (full variant)

**What it is:** the visual specification - the layout, the chart type per metric, and the **red/yellow/green
threshold bands** with the escalation rule when a metric turns red [[19]](#ref-19). **Why it exists:** because
*"most KPI dashboards fail on design, not data"* [[17]](#ref-17). Color means status, not decoration; a
consistent RAG scheme and a stated *"escalation or corrective action when deviation occurs"* [[19]](#ref-19)
turn *"metrics into actionable responsibilities rather than just data"* [[19]](#ref-19).

### Data Sources and Refresh (full variant)

**What it is:** the system of record for each metric and its refresh cadence and latency. **Why it exists:**
a dashboard with an undocumented or manual source rots. *"A dashboard that requires manual data entry is a
dashboard with an expiration date"* [[17]](#ref-17); naming the approved source (and the non-approved ones to
avoid) is what makes the *"single source of truth... a governance decision, not a slogan"* [[11]](#ref-11).

### Review and Ownership

**What it is:** the review cadence, the owner of the dashboard, and what happens when a metric is red. **Why
it exists:** a dashboard is an instrument for a review meeting, and the meeting is where value is created or
lost. Amazon's Weekly Business Review is exception-driven - *"if the metric shows only routine variation, the
owner will say 'nothing to see here'"* [[25]](#ref-25) - and disciplined about acting on inputs, not just
outputs: *"you are not allowed to discuss output metrics during the WBR, except in a reporting sense"*
[[25]](#ref-25). Without a cadence and an owner, dashboards decay into wallpaper.

---

## 4. Variants and sizing

**Lean** is the smallest real dashboard spec: **Purpose and Audience**, the **KPIs** table (name, definition,
target, current, trend, owner), and **Review and Ownership**. It is enough for one team to agree on what it
watches and act on it.

**Full** is a strict superset. It keeps the three lean sections and adds **Metric Definitions** (the detailed
per-KPI definition records), **Layout and Thresholds** (the visual and RAG spec), and **Data Sources and
Refresh** (systems of record and cadence). Use it when the dashboard feeds governance, when multiple teams
must agree on what a metric means, or when it will be built by someone other than its author on a BI platform
[[10]](#ref-10)[[20]](#ref-20).

**The scaling signal is stakes and audience, not the number of charts.** ClearPoint's three-tier model is the
useful frame: 3-5 **North Star** metrics shown prominently, 8-12 **supporting** indicators that explain why
the headline moves, and **operational detail** reached only by drill-down [[17]](#ref-17). Move to full when
an executive or auditor consumes the dashboard, or when a metric dispute has already cost a governance meeting
- both are signs the definitions must be locked. Keep any single view within the 5-9 the eye can hold
[[17]](#ref-17).

---

## 5. Methodology lineage

Different frameworks decide *what goes on* the dashboard; knowing which one you are using tells you how to
choose metrics.

- **Balanced Scorecard (Kaplan and Norton).** Sets the category architecture: four perspectives (financial,
  customer, internal process, learning and growth), each with objectives, measures, and targets
  [[6]](#ref-6)[[7]](#ref-7). Reach for it when the dashboard must balance financial and non-financial health
  at the enterprise level.
- **OKRs.** A Key Result *is* a metric with a time-bound target; an OKR dashboard shows current, target, and
  progress. OKRs set which metrics matter this quarter and what success looks like (section 8 on how they
  relate to KPIs).
- **North Star Metric.** One headline value metric with a few input metrics beneath it; the *"bringing
  coherence to the work of everyone in your organization"* framing [[34]](#ref-34) drives the "one big number
  plus drivers" layout common in product-led companies.
- **The One Metric That Matters (Lean Analytics).** Not a permanent metric but a focus discipline: at each
  stage, *"finding the right thing to track at the right time, based on the type of business you're in and the
  stage you're at"* [[30]](#ref-30). It fights dashboard bloat by insisting on one rallying metric per period.
- **Amazon's operating cadence.** The WBR/MBR/QBR rhythm shapes dashboard design around review meetings and
  the input-over-output discipline [[25]](#ref-25).
- **Spec-first practice.** Independent of framework, the mature practice writes the **definition before the
  build**: a platform-independent spec (metrics, formulas, owners, sources, layout) that *"quickly
  communicate[s] ideas and test[s] concepts without having to touch a line of code"* [[21]](#ref-21) and is
  built by *"work[ing] backward from"* the end goal [[20]](#ref-20). This bundle is that spec.

---

## 6. Debates and contested boundaries

**The central tension is that measuring a thing changes it.** This is not a fringe worry; it has two named
laws behind it.

**Goodhart's Law and Campbell's Law.** The economist Charles Goodhart observed in 1975 that *"any observed
statistical regularity will tend to collapse once pressure is placed upon it for control purposes"*; Marilyn
Strathern's 1997 generalization is the canonical phrasing: *"when a measure becomes a target, it ceases to be
a good measure"* [[31]](#ref-31). Donald Campbell reached the same place from social science: *"the more any
quantitative social indicator is used for social decision-making, the more subject it will be to corruption
pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor"*
[[32]](#ref-32). The mechanism is target displacement: once people are judged on a number, they optimize the
number, not the thing it was a proxy for. A KPI dashboard, being a set of numbers attached to accountability,
is where this bites hardest.

**Vanity metrics vs actionable metrics.** Eric Ries coined *"what I call Vanity Metrics"* [[28]](#ref-28) in
2009 - numbers that look good but guide no decision - and later tied them to "success theater": *"the reason
companies like to talk about vanity metrics is they both make your competitors feel bad about themselves and
also reveal nothing about your business"* [[29]](#ref-29). Croll and Yoskovitz's test is the sharpest: a good
metric changes behavior, while vanity metrics are *"the numbers that make you feel good but seriously
mislead"* [[30]](#ref-30). The dissent, from Jeff Gothelf, is worth carrying honestly: for a team
building measurement capability from zero, a coarse metric is scaffolding - *"value will come later. So will
better metrics. For now, vanity metrics do help give us direction"* [[33]](#ref-33). The camps agree on the
goal (actionable metrics) and differ on whether coarse early metrics have transitional value.

**Where this bundle lands.** The template is built for the synthesis: choose **actionable** metrics tied to an
objective [[3]](#ref-3); **define them precisely** so they cannot be quietly re-specified to look green
[[11]](#ref-11); pair every target with the **leading indicators** that let you act before the lagging outcome
is fixed [[13]](#ref-13); and treat a green dashboard with suspicion, not relief. Diligent's warning is the
one to keep: *"the biggest mistake is measuring activities instead of outcomes"* [[27]](#ref-27).

**One headline metric or a balanced set?** A live, unresolved debate. North Star and OMTM argue for radical
focus on one number [[34]](#ref-34)[[30]](#ref-30); the Balanced Scorecard argues a single metric will be
gamed or miss critical dimensions [[7]](#ref-7). Practitioners usually resolve it by altitude: a North Star at
the company level, a balanced set at the functional level.

**Dashboard or scorecard?** The distinction (live monitoring vs periodic target-comparison snapshot
[[24]](#ref-24)) is dissolving as modern tools add target lines and RAG to any dashboard; whether the
conceptual difference still matters for governance is itself contested [[24]](#ref-24).

---

## 7. Anti-patterns and failure modes

1. **The vanity dashboard.** Full of numbers that go up and to the right but guide no decision. Fix: keep only
   metrics that change what you do [[30]](#ref-30); ask of each, "if this moved, what would we do
   differently?"
2. **The gamed metric (Goodhart).** A KPI that became a target and is now optimized directly, decoupled from
   the outcome it proxied [[31]](#ref-31). Fix: pair headline lagging targets with leading indicators, and
   watch for the metric improving while the outcome does not.
3. **The ambiguous metric.** No locked definition, so *"every dashboard becomes a new version of the truth"*
   [[11]](#ref-11) and reviews *"drift into arguments about data quality rather than action"* [[10]](#ref-10).
   *"Metric inconsistencies are one of the most common causes of confusion in analytics environments"*
   [[12]](#ref-12). Fix: define inclusions/exclusions, formula, grain, and source.
4. **Dashboard bloat.** Thirty metrics on one view when the eye holds *"5-9"* [[17]](#ref-17). Fix: a
   three-tier hierarchy; drill-down for the rest.
5. **The orphaned metric.** No owner, so no one can say what it means or act when it moves. Fix: one named
   owner per KPI, distinct from the data steward [[10]](#ref-10).
6. **The all-green dashboard.** Every metric green, usually because the targets are conservative or the risks
   are tracked nowhere. Fix: honest targets, and read the dashboard beside the risk register - a green
   dashboard with an unreviewed register is *"measuring activities instead of outcomes"* [[27]](#ref-27).
7. **The manual dashboard.** Fed by hand, so it rots. *"A dashboard that requires manual data entry is a
   dashboard with an expiration date"* [[17]](#ref-17). Fix: name an automated source per metric.

---

## 8. Relationships to other artifacts

**KPI dashboard vs OKRs.** Complementary, not rival. *"A KPI tells you how you're doing; an OKR tells you
where you're trying to get, and by when"* [[23]](#ref-23), or in the car metaphor, *"KPIs are what you find
on your car's dashboard... OKRs... are like your landmarks"* [[22]](#ref-22). They cycle: *"a KPI that drifts
red can become next quarter's Objective. An Objective you've hit settles into a KPI you monitor from then on"*
[[23]](#ref-23).

**KPI dashboard vs scorecard vs metrics report.** A dashboard is *"used as a monitoring tool in real-time"*;
a scorecard is a periodic snapshot that *"aren't live"* and compares actual to target [[24]](#ref-24); a
metrics report explains what the numbers were over a period. They sit on a spectrum from live monitoring to
periodic assessment.

**KPI dashboard vs risk register - the governance sibling.** This is the pairing that matters most in this
family. The dashboard tracks **progress toward** objectives; the risk register tracks **threats to** them.
ISACA states the distinction cleanly: *"while KPIs focus on business performance, KRIs focus on risk
management performance"* [[26]](#ref-26). The time horizons are opposite: *"risk management KPIs track
historical performance and program effectiveness, while key risk indicators provide forward-looking signals
about emerging threats"* [[27]](#ref-27). The failure mode is treating them separately: a program with a green
dashboard and an unreviewed [`risk-register`](../risk-register/risk-register_guide.md) is performing today
while accumulating exposure that will turn the dashboard red in six to twelve months. Read them together.

**KPI dashboard vs RAID log - the third governance sibling.** The [`raid-log`](../raid-log/raid-log_guide.md)
consolidates Risks, Assumptions, Issues, and Dependencies for the same program, and its quadrants feed the
dashboard's metrics from below: an **assumption** the program rests on (analysts will adopt the feature) is
exactly what a headline KPI later confirms or refutes (adoption rate); an **issue** that materializes (a
performance regression) shows up as a KPI turning amber. Where the RAID log tracks the **open items** in
flight, the dashboard tracks **whether the delivered result works**. Together the three read as one
governance surface: the register names the threats, the RAID log tracks the open items behind them, and the
dashboard measures the outcome. The worked examples in this family chain on one program to make that concrete.

**KPI dashboard vs the live BI tool.** This bundle is the **specification**; Tableau, Looker, Power BI, and
Amplitude are the implementations. The spec is platform-agnostic and precedes the build [[21]](#ref-21);
keeping them distinct is what lets the dashboard be rebuilt on a new platform without re-litigating what each
metric means.

---

## 9. Adaptations

- **Executive / strategic.** 3-5 North Star metrics, refreshed daily to monthly, oriented so a leader can
  orient in seconds [[18]](#ref-18); pair with the risk register for the threat side [[26]](#ref-26).
- **Operational.** Dozens of metrics, near-real-time, with exception alerts - the *"real-time data command
  center"* [[18]](#ref-18), reviewed on a fast cadence like the WBR [[25]](#ref-25).
- **Analytical.** Full historical grain with drill-down, for data-literate users only [[35]](#ref-35).
- **Regulated / GRC.** Lock every definition, name a data steward per metric, and integrate with the risk and
  KRI view so performance and risk are monitored together [[10]](#ref-10)[[26]](#ref-26).
- **Early-stage / one team.** The lean spec and a single OMTM for the current stage is enough [[30]](#ref-30);
  a coarse metric that builds the measurement habit can be defensible scaffolding [[33]](#ref-33), as long as
  you know it is a placeholder.

---

## 10. Worked example

[`kpi-dashboard_example.md`](kpi-dashboard_example.md) is a full-variant KPI dashboard specification for the
Acme Analytics **Reporting Platform Modernization** program - the same program the
[`risk-register`](../risk-register/risk-register_example.md) and [`raid-log`](../raid-log/raid-log_example.md)
examples cover. It closes the governance-docs family loop: where the register tracks threats and the RAID log
tracks open items, the dashboard tracks **whether the delivered program works**. Its headline metric is **Time
to Insight** (the program's value goal); **Saved Views adoption** is the outcome the register's adoption risk
(R-04) threatens and the RAID log's adoption assumption (A-02) underlies; **view-list load** is the metric the
performance issue (ISS-12) moved. It demonstrates the KPI table, full per-metric definition records (formula,
inclusions/exclusions, leading/lagging, owner and data steward), RAG thresholds with an escalation rule, data
sources, and a review cadence.

---

## References

<a id="ref-1"></a>[1] Wikipedia contributors. "[Performance indicator](https://en.wikipedia.org/wiki/Performance_indicator)." Wikipedia (accessed 2026-07-22). Supports the canonical KPI definition and the indicator-vs-goal distinction ("a type of performance measurement used to evaluate the success of an organization, activity, project, or process in achieving defined objectives"; "An indicator is a measurable variable used to show whether progress is being made towards a goal, rather than the goal itself."). [reference]

<a id="ref-2"></a>[2] KPI.org. "[KPI Basics - What is a Key Performance Indicator?](https://www.kpi.org/kpi-basics/)" kpi.org (accessed 2026-07-22). Authority-site definition emphasizing "critical" and "progress toward a desired result" ("Key Performance Indicators (KPIs) are the critical, quantifiable measures of progress toward a desired result."; "good KPIs truly reflect and measure strategic priorities"; "Effective KPIs are not off-the-shelf - they must be thoughtfully developed to reflect your organization's unique strategy, goals, and context."). [primary]

<a id="ref-3"></a>[3] Klipfolio. "[KPI vs Metric vs Measure](https://www.klipfolio.com/blog/kpi-metric-measure)." klipfolio.com (accessed 2026-07-22). Supports the measure -> metric -> KPI hierarchy and the elevation criterion ("Key performance indicators are the end goals. Metrics are what you track along the way to determine whether the goal will be met."; "A metric becomes a KPI when it's paired with a specific business objective and target."; "A Measure: A number or value that can be summed, counted, or averaged"). [practitioner]

<a id="ref-4"></a>[4] Wikipedia contributors. "[Dashboard (business)](https://en.wikipedia.org/wiki/Dashboard_(business))." Wikipedia (accessed 2026-07-22). Supports the business definition and the EIS-to-BI lineage ("a type of graphical user interface which often provides at-a-glance views of data relevant to a particular objective or process through a combination of visualizations and summary information"; "it was soon realized that the approach wasn't practical as information was often incomplete, unreliable, and spread across too many disparate sources"). [reference]

<a id="ref-5"></a>[5] The Hog Ring. "[Where did the term 'dashboard' come from?](https://thehogring.com/2012/11/25/where-did-the-term-dashboard-come-from/)" thehogring.com (accessed 2026-07-22). Supports the carriage-to-automobile etymology ("The word 'dashboard' was originally used to describe the wooden board carriage makers attached to the front of carriages to prevent mud and rocks from being splashed (or 'dashed') onto drivers and their passengers by the horses that pulled them about."; "It wasn't until the early 1900's...that 'dashboards' were repurposed to house vehicle instruments, like speedometers and gas gauges."). [reference]

<a id="ref-6"></a>[6] Kaplan, Robert S. and Norton, David P. "[The Balanced Scorecard: Measures that Drive Performance](https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2)." Harvard Business Review, January-February 1992 (accessed 2026-07-22). The foundational Balanced Scorecard article ("What you measure is what you get."; "traditional financial accounting measures like return on investment and earnings per share can give misleading signals for continuous improvement and innovation"). **Full text paywalled; only the introduction was read** - the four perspectives are corroborated by [[7]](#ref-7), not read verbatim here. [primary]

<a id="ref-7"></a>[7] Balanced Scorecard Institute. "[Balanced Scorecard Basics](https://balancedscorecard.org/bsc-basics-overview/)." balancedscorecard.org (accessed 2026-07-22). Supports the four perspectives and the BSC-as-management-system point ("The balanced scorecard retains traditional financial measures. But financial measures tell the story of past events...financial measures are inadequate...for guiding and evaluating the journey that information age companies must make to create future value."). The official BSC methodology body; the quoted line is from the 1992 HBR article. [reference]

<a id="ref-8"></a>[8] Rockart, J.F. "[Chief executives define their own data needs](https://pubmed.ncbi.nlm.nih.gov/10297607/)." Harvard Business Review, 1979; PubMed record (accessed 2026-07-22). Supports Critical Success Factors as the root of the "key" in KPI ("Critical success factors are those performance factors which must receive the on-going attention of management if the company is to remain competitive."). [primary]

<a id="ref-9"></a>[9] GoPractice. "[What are metrics: a guide for product managers](https://gopractice.io/product/what-are-metrics-a-guide-for-product-managers/)." gopractice.io (accessed 2026-07-22). Supports that a metric must have clear meaning and that a dashboard is a visual display of metrics ("A good metric therefore always has a clear, practical meaning. If a metric's meaning is unclear, it is useless."; "A dashboard is a visual display of different metrics"). [practitioner]

<a id="ref-10"></a>[10] Impact Insights Hub. "[Metric ownership and data governance](https://impactinsightshub.com/blogs/news/metric-ownership-and-data-governance-making-assurance-dashboards-reliable-enough-for-oversight)." impactinsightshub.com (accessed 2026-07-22). Supports the KPI-definition field list, the owner-vs-data-steward distinction, and the decision-grade bar ("purpose, numerator, denominator, inclusion rules, exclusion rules, data source, refresh frequency, threshold, owner, data steward, known limitations, and review cadence."; "Metric ownership is not a title on a chart. It is a working agreement that one named role is accountable for performance and interpretation, while another named role is accountable for data integrity and reproducibility."; "A dashboard is only decision-grade when the organization can explain what each metric means, who owns it, how the data is produced, and what happens when the number changes."; "teams debate which dataset is 'right,' and governance meetings drift into arguments about data quality rather than action."). [practitioner]

<a id="ref-11"></a>[11] FastSlowMotion. "[Analytics governance: metric definitions and single source of truth](https://www.fastslowmotion.com/salesforce-analytics-governance-metrics/)." fastslowmotion.com (accessed 2026-07-22). Supports the metric-definition discipline and the locked-definitions argument ("Analytics governance is the system for defining metrics, assigning owners, and controlling how KPIs are calculated so everyone uses the same numbers."; "If KPI definitions aren't locked then every dashboard becomes a new version of the truth."; "Inclusions and exclusions (critical!)"; "Single source of truth is a governance decision, not a slogan."). [practitioner]

<a id="ref-12"></a>[12] Data Never Lies. "[Metrics and definitions standardization](https://data-never-lies.com/metrics-definitions-standardization/)." data-never-lies.com (accessed 2026-07-22). Supports that metric inconsistency undermines trust and decisions ("Metric inconsistencies are one of the most common causes of confusion in analytics environments."; "When departments rely on different definitions for the same KPI, dashboards become difficult to trust and strategic discussions become unproductive."). [practitioner]

<a id="ref-13"></a>[13] Intrafocus. "[Lead and lag indicators](https://www.intrafocus.com/lead-and-lag-indicators/)." intrafocus.com (accessed 2026-07-22). Supports the leading/lagging definitions and the need for both ("A predictive measurement that can influence change."; "An output measurement that can only record what has happened."; "after-the-event measurement, essential for charting progress but useless when attempting to influence the future."; "a combination of indicators results in enhanced business performance overall."). Notes leading indicators are "always more challenging to determine" and do not "guarantee success." [practitioner]

<a id="ref-14"></a>[14] Amplitude. "[Leading vs lagging indicators](https://amplitude.com/blog/leading-lagging-indicators)." amplitude.com (accessed 2026-07-22). Supports SaaS leading/lagging examples and why lagging metrics cannot be acted on retrospectively ("predict future performance and help drive your daily initiatives."; "reflect past performance to assess success and shape long-term strategy."; "by the time you determine last month's MRR, it's too late to change it"). Amplitude sells product analytics tooling. [vendor]

<a id="ref-15"></a>[15] SimpleKPI. "[SMART and SMARTER KPIs explained](https://www.simplekpi.com/Blog/smart-and-smarter-kpis-explained)." simplekpi.com (accessed 2026-07-22). Supports the SMART criteria ("Be specific as to what you wish to achieve. What is the actual objective? Do not use jargon."; "When should the objective be achieved? Setting deadlines creates urgency and aids planning."; "Regularly assess your KPIs and their associated SMART goals"). SMARTER (adding Evaluate and Revise) is this vendor's proposal; most sources stop at SMART. [vendor]

<a id="ref-16"></a>[16] AgencyAnalytics. "[What are SMART KPIs?](https://agencyanalytics.com/blog/what-are-smart-kpis)" agencyanalytics.com (accessed 2026-07-22). Supports SMART with before/after examples and a sub-ten-KPI ceiling ("focus on what a campaign aims to achieve, leaving no room for vague intentions"; "success is tracked through quantifiable metrics"; "directly contribute to the bigger picture and deliver insights into areas that matter most"). [vendor]

<a id="ref-17"></a>[17] ClearPoint Strategy. "[KPI dashboard best practices](https://www.clearpointstrategy.com/blog/kpi-dashboard-best-practices)." clearpointstrategy.com (accessed 2026-07-22). Supports the design-not-data failure mode, the cognitive limit, the three-tier hierarchy, and the manual-entry warning ("most KPI dashboards fail on design, not data"; "humans can effectively process 5-9 pieces of information at once"; "A dashboard that requires manual data entry is a dashboard with an expiration date."). The 5-9 limit extrapolates Miller's Law to dashboard panels; directional, not measured. [practitioner]

<a id="ref-18"></a>[18] Yellowfin BI. "[Types of dashboards: operational, strategic, analytical](https://www.yellowfinbi.com/blog/operational-strategic-or-analytical-dashboard-which-type-best-for-bi)." yellowfinbi.com (accessed 2026-07-22). Supports the three-tier audience framework ("A strategic dashboard tracks long-term company performance against enterprise-wide goals."; "The operational dashboard is your real-time data command center. It monitors short-term performance and daily operations."; "Analytical dashboards are designed for deep analysis, using complex and historical datasets to uncover trends, comparisons, and predictions."). BI vendor. [vendor]

<a id="ref-19"></a>[19] Talento HR. "[KPI Card Template](https://talento-hr.com/en/knowledge-kit/kpi-card-template)." talento-hr.com (accessed 2026-07-22). Supports the KPI-card fields including RAG thresholds and escalation ("red / yellow / green zones"; "Escalation or corrective action when deviation occurs"; "metrics into actionable responsibilities rather than just data"). [practitioner]

<a id="ref-20"></a>[20] Databox. "[Gathering and understanding dashboard requirements](https://databox.com/dashboard-requirements)." databox.com (accessed 2026-07-22). Supports the dashboard-spec-as-pre-build-artifact process ("We work with stakeholders to determine a common end goal and work backward from there, making metric suggestions that can all help keep the story on track."; "coming up with the right dashboard as a team is much easier if we decide on the right layout ahead of time."). Dashboard vendor; quoted practitioners are anonymous. [vendor]

<a id="ref-21"></a>[21] Delivering Data Analytics. "[Dashboard Requirements Kit](https://deliveringdataanalytics.com/product/dashboard-requirements-kit/)." deliveringdataanalytics.com (accessed 2026-07-22). Supports the dashboard spec as a platform-independent pre-build artifact, separate from Tableau/Power BI/Qlik ("It doesn't matter if you are not a data pro. The kit allows you to quickly communicate ideas and test concepts without having to touch a line of code."). A paid-product landing page. [practitioner]

<a id="ref-22"></a>[22] Perdoo. "[OKRs vs KPIs](https://www.perdoo.com/resources/blog/okr-vs-kpi)." perdoo.com (accessed 2026-07-22). Supports the KPI-vs-OKR relationship via the car analogy ("KPIs are what you find on your car's dashboard, like your fuel gauge and temperature gauge."; "OKRs will help you map out a road toward your destination. They are like your landmarks."). OKR vendor. [vendor]

<a id="ref-23"></a>[23] ClearPoint Strategy. "[OKRs vs KPIs](https://www.clearpointstrategy.com/blog/okrs-vs-kpis)." clearpointstrategy.com (accessed 2026-07-22). Supports the cyclic KPI-OKR relationship ("a KPI tells you how you're doing; an OKR tells you where you're trying to get, and by when."; "A KPI that drifts red can become next quarter's Objective. An Objective you've hit settles into a KPI you monitor from then on."). Strategy-execution vendor; the "26.7% actively scored" figure is proprietary and unverified. [vendor]

<a id="ref-24"></a>[24] Sisense. "[Scorecard vs dashboard](https://www.sisense.com/blog/scorecard-vs-dashboard-adds-business-intelligence/)." sisense.com (accessed 2026-07-22). Supports the dashboard-vs-scorecard distinction and its dissolution ("scorecards aren't live, so data is not updated in real-time"; "used as a monitoring tool in real-time. Data is constantly updated"). BI vendor; the boundary drawn is cleaner than modern tools enforce. [vendor]

<a id="ref-25"></a>[25] Chin, Cedric (Commoncog). "[The Amazon Weekly Business Review](https://commoncog.com/the-amazon-weekly-business-review/)." commoncog.com (accessed 2026-07-22). Supports the exception-driven WBR and the input-vs-output discipline ("you are not allowed to discuss output metrics during the WBR, except in a reporting sense."; "If the metric shows only routine variation, the owner will say 'nothing to see here'."). A practitioner account based on *Working Backwards*, not Amazon primary docs. [practitioner]

<a id="ref-26"></a>[26] ISACA. "[Integrating KRIs and KPIs for effective technology risk management](https://www.isaca.org/resources/isaca-journal/issues/2018/volume-4/integrating-kris-and-kpis-for-effective-technology-risk-management)." ISACA Journal, 2018 vol. 4 (accessed 2026-07-22). Supports the KPI-vs-KRI distinction and the dashboard-and-register pairing ("While KPIs focus on business performance, KRIs focus on risk management performance."; "the enterprise is, or has a high probability of being, subject to a risk that exceeds the defined risk appetite"). [primary]

<a id="ref-27"></a>[27] Diligent. "[Measuring ERM performance: risk management KPIs](https://www.diligent.com/resources/blog/measuring-erm-performance)." diligent.com (accessed 2026-07-22). Supports the dashboard-vs-register asymmetry and the outcome-not-activity rule ("Risk management KPIs track historical performance and program effectiveness, while key risk indicators provide forward-looking signals about emerging threats."; "The biggest mistake is measuring activities instead of outcomes."). GRC vendor. [vendor]

<a id="ref-28"></a>[28] Ries, Eric. "[Vanity Metrics vs. Actionable Metrics](https://tim.blog/2009/05/19/vanity-metrics-vs-actionable-metrics/)." tim.blog (guest post), 2009 (accessed 2026-07-22). The original coinage of "vanity metrics" ("what I call Vanity Metrics"). The "10,000 hits, now what?" example is paraphrased in the companion, not quoted, as only this phrase was captured verbatim. [primary]

<a id="ref-29"></a>[29] Ries, Eric. "[Founder Stories: Eric Ries on Vanity Metrics and Success Theater](https://techcrunch.com/2011/09/24/founder-stories-eric-ries-vanity-metrics/)." TechCrunch, 2011 (accessed 2026-07-22). Supports the "success theater" framing ("The reason companies like to talk about vanity metrics is they both make your competitors feel bad about themselves and also reveal nothing about your business."). [primary]

<a id="ref-30"></a>[30] Yoskovitz, Ben. "[Lean Analytics: The One Metric That Matters and Other Provocations](https://medium.com/lean-stack/lean-analytics-the-one-metric-that-matters-and-other-provocations-fd3006aab17)." Medium (accessed 2026-07-22). Supports OMTM and the vanity-metric definition from a book co-author ("The One Metric That Matters is all about finding the right thing to track at the right time, based on the type of business you're in and the stage you're at."; "We call them vanity metrics, the numbers that make you feel good but seriously mislead."). The book *Lean Analytics* (O'Reilly, 2013) is the authoritative primary. [primary]

<a id="ref-31"></a>[31] Wikipedia contributors. "[Goodhart's Law](https://en.wikipedia.org/wiki/Goodhart%27s_law)." Wikipedia (accessed 2026-07-22). Supports both canonical formulations ("Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes."; "When a measure becomes a target, it ceases to be a good measure."). Strathern's phrasing is from her 1997 European Review paper, attributed via Wikipedia, not retrieved independently. [reference]

<a id="ref-32"></a>[32] Wikipedia contributors. "[Campbell's Law](https://en.wikipedia.org/wiki/Campbell%27s_law)." Wikipedia (accessed 2026-07-22). Supports Campbell's 1979 formulation ("The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor."). [reference]

<a id="ref-33"></a>[33] Gothelf, Jeff. "[In Defense of Vanity Metrics](https://jeffgothelf.com/blog/in-defense-of-vanity-metrics/)." jeffgothelf.com (accessed 2026-07-22). Supports the dissent from Ries - vanity metrics as scaffolding ("Value will come later. So will better metrics. For now, vanity metrics do help give us direction."). [practitioner]

<a id="ref-34"></a>[34] Amplitude. "[About the North Star Framework](https://amplitude.com/books/north-star/about-north-star-framework)." amplitude.com (accessed 2026-07-22). Supports the North Star Metric as a unifying value metric ("Bringing coherence to the work of everyone in your organization is what it's all about"). Amplitude formalized the North Star Playbook (2019); Sean Ellis is credited with popularizing the underlying concept earlier. [vendor]

<a id="ref-35"></a>[35] insightsoftware. "[Best practices for designing and building a great KPI dashboard](https://insightsoftware.com/blog/best-practices-for-designing-and-building-a-great-kpi-dashboard/)." insightsoftware.com (accessed 2026-07-22). Supports audience-typed dashboard design and the data-literacy caveat ("Should only serve users that are data literate to avoid overwhelming non-experts"). Combines "strategic/executive" where [[18]](#ref-18) splits them. [vendor]
