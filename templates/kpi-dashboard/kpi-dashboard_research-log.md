# Research log: kpi-dashboard

Built for the `kpi-dashboard` bundle (governance-docs family) to the methodology section 6 honest-retrieval
standard. Sources were gathered by a five-dimension research fan-out (origins/canon, structure/anatomy,
frameworks/lineage, debates/criticism, relationships/tooling), each doing real WebSearch/WebFetch. Every
source below is tagged with its tier and retrieval status; **only sources marked fetched-and-verified may be
quoted verbatim** in the companion, and each verbatim phrase used is listed here.

Research date: 2026-07-22. Catalog ref: 139.

---

## Honest framing (the through-line for the companion)

A KPI dashboard is the standing instrument for **monitoring progress toward objectives** - and it is the
artifact most vulnerable to **Goodhart's Law** (*"when a measure becomes a target, it ceases to be a good
measure"*) and to **vanity metrics** (numbers that feel good but drive no decision). This bundle teaches the
dashboard that survives: metrics that are **actionable** (they change behavior), **defined precisely** (locked
definitions so every dashboard is not a new version of the truth), **owned**, and **reviewed on a cadence**.

**The load-bearing scope fact:** this bundle is a **document that DEFINES a dashboard** (its metrics, formulas,
targets, owners, data sources, thresholds, and review cadence), **platform-agnostic** - not a live BI tool.
The definition precedes the Tableau/Looker/Power BI/Amplitude build; *"a good metric therefore always has a
clear, practical meaning. If a metric's meaning is unclear, it is useless."* The spec is what keeps a
dashboard from being rebuilt on every stakeholder disagreement or orphaned when its owner leaves.

**Sharpest teaching points:**
1. **KPI vs metric vs measure:** a metric becomes a KPI *"when it's paired with a specific business objective
   and target."* Not every metric is a KPI.
2. **Definition discipline:** *"if KPI definitions aren't locked then every dashboard becomes a new version of
   the truth."* The most dispute-generating omission is inclusions/exclusions.
3. **Leading vs lagging:** leading indicators predict and can be acted on; lagging confirm after the fact
   (*"by the time you determine last month's MRR, it's too late to change it"*). Use both.
4. **Vanity vs actionable:** a good metric *"changes the way you behave"*; a vanity metric *"makes you feel
   good but seriously mislead[s]."*
5. **Goodhart / Campbell:** the honest tension. A measure under target-pressure gets gamed. Present both
   camps.
6. **Audience tiers and cognitive limit:** executive (3-5 headline), operational (real-time), analytical
   (drill-down); *"humans can effectively process 5-9 pieces of information at once."*
7. **One named owner per metric** (distinct from the data steward who owns data integrity).
8. **Governance sibling:** the dashboard tracks **progress toward** objectives; the risk register tracks
   **threats to** them (*"while KPIs focus on business performance, KRIs focus on risk management"*).

---

## Sources (curated, deduplicated, contiguously numbered; one source per entry)

**[1] Wikipedia - Performance indicator.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Performance_indicator`
Supports: the canonical KPI definition and the indicator-vs-goal distinction.
Quotable: "a type of performance measurement used to evaluate the success of an organization, activity,
project, or process in achieving defined objectives"; "An indicator is a measurable variable used to show
whether progress is being made towards a goal, rather than the goal itself."

**[2] KPI.org - KPI Basics.** primary. **fetched-and-verified.**
`https://www.kpi.org/kpi-basics/`
Supports: an authority-site definition emphasizing "critical" and "progress toward a desired result."
Quotable: "Key Performance Indicators (KPIs) are the critical, quantifiable measures of progress toward a
desired result."; "good KPIs truly reflect and measure strategic priorities"; "Effective KPIs are not
off-the-shelf - they must be thoughtfully developed to reflect your organization's unique strategy, goals,
and context."

**[3] Klipfolio - KPI vs Metric vs Measure.** practitioner. **fetched-and-verified.**
`https://www.klipfolio.com/blog/kpi-metric-measure`
Supports: the measure -> metric -> KPI hierarchy and the exact criterion elevating a metric to a KPI.
Quotable: "Key performance indicators are the end goals. Metrics are what you track along the way to
determine whether the goal will be met."; "A metric becomes a KPI when it's paired with a specific business
objective and target."; "A Measure: A number or value that can be summed, counted, or averaged".

**[4] Wikipedia - Dashboard (business).** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Dashboard_(business)`
Supports: the business definition of a dashboard and its executive-information-system-to-BI lineage.
Quotable: "a type of graphical user interface which often provides at-a-glance views of data relevant to a
particular objective or process through a combination of visualizations and summary information"; "it was
soon realized that the approach wasn't practical as information was often incomplete, unreliable, and spread
across too many disparate sources".

**[5] The Hog Ring - Where did the term 'dashboard' come from?** reference. **fetched-and-verified.**
`https://thehogring.com/2012/11/25/where-did-the-term-dashboard-come-from/`
Supports: the etymology - a carriage mud-guard that migrated to the automobile instrument panel.
Quotable: "The word 'dashboard' was originally used to describe the wooden board carriage makers attached to
the front of carriages to prevent mud and rocks from being splashed (or 'dashed') onto drivers and their
passengers by the horses that pulled them about."; "It wasn't until the early 1900's...that 'dashboards'
were repurposed to house vehicle instruments, like speedometers and gas gauges."

**[6] Kaplan, Robert S. and Norton, David P. - The Balanced Scorecard: Measures that Drive Performance (HBR, 1992).** primary. **fetched-and-verified (introduction only).**
`https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2`
Supports: the foundational Balanced Scorecard article and its critique of financial-only measurement.
Quotable: "What you measure is what you get."; "traditional financial accounting measures like return on
investment and earnings per share can give misleading signals for continuous improvement and innovation".
Contested/time-bound: full text paywalled; only the introduction was read. The four perspectives are
corroborated by [7] and secondary sources but were not read verbatim from this page.

**[7] Balanced Scorecard Institute - Balanced Scorecard Basics / The Four Perspectives.** reference. **fetched-and-verified.**
`https://balancedscorecard.org/bsc-basics-overview/`
Supports: the four BSC perspectives and the BSC-as-management-system (not a dashboard) point.
Quotable: "The balanced scorecard retains traditional financial measures. But financial measures tell the
story of past events...financial measures are inadequate...for guiding and evaluating the journey that
information age companies must make to create future value."
Contested/time-bound: BSI is the official BSC methodology body; the quoted Kaplan-Norton line is from the
1992 HBR article.

**[8] Rockart, J.F. - Chief executives define their own data needs (HBR, 1979).** primary. **fetched-and-verified (PubMed record).**
`https://pubmed.ncbi.nlm.nih.gov/10297607/`
Supports: Critical Success Factors as the framework for choosing which metrics executives need - the
intellectual root of the "key" in KPI.
Quotable: "Critical success factors are those performance factors which must receive the on-going attention
of management if the company is to remain competitive."

**[9] GoPractice - What are metrics: a guide for product managers.** practitioner. **fetched-and-verified.**
`https://gopractice.io/product/what-are-metrics-a-guide-for-product-managers/`
Supports: that a metric must have a clear practical meaning, and that a dashboard is a visual display of
metrics (definition precedes visualization).
Quotable: "A good metric therefore always has a clear, practical meaning. If a metric's meaning is unclear,
it is useless."; "A dashboard is a visual display of different metrics".

**[10] Impact Insights Hub - Metric ownership and data governance.** practitioner. **fetched-and-verified.**
`https://impactinsightshub.com/blogs/news/metric-ownership-and-data-governance-making-assurance-dashboards-reliable-enough-for-oversight`
Supports: the full KPI-definition field list; the owner-vs-data-steward distinction; the decision-grade bar.
Quotable: "purpose, numerator, denominator, inclusion rules, exclusion rules, data source, refresh frequency,
threshold, owner, data steward, known limitations, and review cadence."; "Metric ownership is not a title on
a chart. It is a working agreement that one named role is accountable for performance and interpretation,
while another named role is accountable for data integrity and reproducibility."; "A dashboard is only
decision-grade when the organization can explain what each metric means, who owns it, how the data is
produced, and what happens when the number changes."; "teams debate which dataset is 'right,' and governance
meetings drift into arguments about data quality rather than action."

**[11] FastSlowMotion - Analytics governance: metric definitions and single source of truth.** practitioner. **fetched-and-verified.**
`https://www.fastslowmotion.com/salesforce-analytics-governance-metrics/`
Supports: the metric-definition discipline and the locked-definitions argument.
Quotable: "Analytics governance is the system for defining metrics, assigning owners, and controlling how
KPIs are calculated so everyone uses the same numbers."; "If KPI definitions aren't locked then every
dashboard becomes a new version of the truth."; "Inclusions and exclusions (critical!)"; "Single source of
truth is a governance decision, not a slogan."

**[12] Data Never Lies - Metrics and definitions standardization.** practitioner. **fetched-and-verified.**
`https://data-never-lies.com/metrics-definitions-standardization/`
Supports: that metric inconsistency undermines trust and decisions.
Quotable: "Metric inconsistencies are one of the most common causes of confusion in analytics
environments."; "When departments rely on different definitions for the same KPI, dashboards become
difficult to trust and strategic discussions become unproductive."

**[13] Intrafocus - Lead and lag indicators.** practitioner. **fetched-and-verified.**
`https://www.intrafocus.com/lead-and-lag-indicators/`
Supports: the definitions of leading and lagging indicators and the need for both.
Quotable: "A predictive measurement that can influence change."; "An output measurement that can only record
what has happened."; "after-the-event measurement, essential for charting progress but useless when
attempting to influence the future."; "a combination of indicators results in enhanced business performance
overall."
Contested/time-bound: notes leading indicators are "always more challenging to determine" and do not
"guarantee success" - a caveat many sources omit.

**[14] Amplitude - Leading vs lagging indicators.** vendor. **fetched-and-verified.**
`https://amplitude.com/blog/leading-lagging-indicators`
Supports: SaaS leading/lagging examples and why lagging metrics cannot be acted on retrospectively.
Quotable: "predict future performance and help drive your daily initiatives."; "reflect past performance to
assess success and shape long-term strategy."; "by the time you determine last month's MRR, it's too late to
change it".
Contested/time-bound: Amplitude sells product analytics tooling.

**[15] SimpleKPI - SMART and SMARTER KPIs explained.** vendor. **fetched-and-verified.**
`https://www.simplekpi.com/Blog/smart-and-smarter-kpis-explained`
Supports: the SMART criteria and the (vendor-proposed) SMARTER extension.
Quotable: "Be specific as to what you wish to achieve. What is the actual objective? Do not use jargon.";
"When should the objective be achieved? Setting deadlines creates urgency and aids planning."; "Regularly
assess your KPIs and their associated SMART goals".
Contested/time-bound: SMARTER (adding Evaluate and Revise) is SimpleKPI's proposal; most sources stop at
SMART.

**[16] AgencyAnalytics - What are SMART KPIs?** vendor. **fetched-and-verified.**
`https://agencyanalytics.com/blog/what-are-smart-kpis`
Supports: SMART with concrete before/after examples and a recommended ceiling of fewer than ten KPIs.
Quotable: "focus on what a campaign aims to achieve, leaving no room for vague intentions"; "success is
tracked through quantifiable metrics"; "directly contribute to the bigger picture and deliver insights into
areas that matter most".

**[17] ClearPoint Strategy - KPI dashboard best practices.** practitioner. **fetched-and-verified.**
`https://www.clearpointstrategy.com/blog/kpi-dashboard-best-practices`
Supports: the design-not-data failure mode, the cognitive limit, the three-tier metric hierarchy, and the
manual-entry warning.
Quotable: "most KPI dashboards fail on design, not data"; "humans can effectively process 5-9 pieces of
information at once"; "A dashboard that requires manual data entry is a dashboard with an expiration date."
Contested/time-bound: the 5-9 limit extrapolates Miller's Law (working-memory chunks) to dashboard panels;
directionally valid, not a dashboard-specific measurement.

**[18] Yellowfin BI - Types of dashboards: operational, strategic, analytical.** vendor. **fetched-and-verified.**
`https://www.yellowfinbi.com/blog/operational-strategic-or-analytical-dashboard-which-type-best-for-bi`
Supports: the three-tier audience framework.
Quotable: "A strategic dashboard tracks long-term company performance against enterprise-wide goals."; "The
operational dashboard is your real-time data command center. It monitors short-term performance and daily
operations."; "Analytical dashboards are designed for deep analysis, using complex and historical datasets
to uncover trends, comparisons, and predictions."

**[19] Talento HR - KPI Card Template.** practitioner. **fetched-and-verified.**
`https://talento-hr.com/en/knowledge-kit/kpi-card-template`
Supports: the KPI-card fields including RAG thresholds and escalation rules.
Quotable: "red / yellow / green zones"; "Escalation or corrective action when deviation occurs"; "metrics
into actionable responsibilities rather than just data".

**[20] Databox - Gathering and understanding dashboard requirements.** vendor. **fetched-and-verified.**
`https://databox.com/dashboard-requirements`
Supports: the dashboard-specification-as-pre-build-artifact process (work backward from the goal).
Quotable: "We work with stakeholders to determine a common end goal and work backward from there, making
metric suggestions that can all help keep the story on track."; "coming up with the right dashboard as a
team is much easier if we decide on the right layout ahead of time."
Contested/time-bound: Databox is a dashboard vendor; the quoted practitioners are anonymous survey
respondents.

**[21] Delivering Data Analytics - Dashboard Requirements Kit.** practitioner. **fetched-and-verified.**
`https://deliveringdataanalytics.com/product/dashboard-requirements-kit/`
Supports: the dashboard spec as a platform-independent pre-build artifact, explicitly separate from
Tableau/Power BI/Qlik.
Quotable: "It doesn't matter if you are not a data pro. The kit allows you to quickly communicate ideas and
test concepts without having to touch a line of code."
Contested/time-bound: a paid-product landing page; the framework doubles as marketing.

**[22] Perdoo - OKRs vs KPIs.** vendor. **fetched-and-verified.**
`https://www.perdoo.com/resources/blog/okr-vs-kpi`
Supports: the KPI-vs-OKR relationship via the car-dashboard-and-landmarks analogy.
Quotable: "KPIs are what you find on your car's dashboard, like your fuel gauge and temperature gauge."; "OKRs
will help you map out a road toward your destination. They are like your landmarks."
Contested/time-bound: Perdoo is an OKR vendor.

**[23] ClearPoint Strategy - OKRs vs KPIs.** vendor. **fetched-and-verified.**
`https://www.clearpointstrategy.com/blog/okrs-vs-kpis`
Supports: the cyclic KPI-OKR relationship.
Quotable: "a KPI tells you how you're doing; an OKR tells you where you're trying to get, and by when."; "A
KPI that drifts red can become next quarter's Objective. An Objective you've hit settles into a KPI you
monitor from then on."
Contested/time-bound: ClearPoint is a strategy-execution vendor; the "26.7% of KPIs actively scored" figure
is proprietary and unverified.

**[24] Sisense - Scorecard vs dashboard.** vendor. **fetched-and-verified.**
`https://www.sisense.com/blog/scorecard-vs-dashboard-adds-business-intelligence/`
Supports: the dashboard-vs-scorecard distinction (live monitoring vs periodic target-comparison snapshot).
Quotable: "scorecards aren't live, so data is not updated in real-time"; "used as a monitoring tool in
real-time. Data is constantly updated".
Contested/time-bound: Sisense is a BI vendor; the boundary they draw is cleaner than modern tools enforce
(see contested claims).

**[25] Commoncog (Cedric Chin) - The Amazon Weekly Business Review.** practitioner. **fetched-and-verified.**
`https://commoncog.com/the-amazon-weekly-business-review/`
Supports: the exception-driven WBR and the input-vs-output-metric discipline.
Quotable: "you are not allowed to discuss output metrics during the WBR, except in a reporting sense."; "If
the metric shows only routine variation, the owner will say 'nothing to see here'."
Contested/time-bound: a practitioner account based on *Working Backwards*, not Amazon primary docs.

**[26] ISACA Journal - Integrating KRIs and KPIs for effective technology risk management (2018).** primary. **fetched-and-verified.**
`https://www.isaca.org/resources/isaca-journal/issues/2018/volume-4/integrating-kris-and-kpis-for-effective-technology-risk-management`
Supports: the KPI-vs-KRI distinction and the dashboard-and-register governance pairing.
Quotable: "While KPIs focus on business performance, KRIs focus on risk management performance."; "the
enterprise is, or has a high probability of being, subject to a risk that exceeds the defined risk appetite".

**[27] Diligent - Measuring ERM performance: risk management KPIs.** vendor. **fetched-and-verified.**
`https://www.diligent.com/resources/blog/measuring-erm-performance`
Supports: the dashboard-vs-register asymmetry (backward vs forward-looking) and the outcome-not-activity rule.
Quotable: "Risk management KPIs track historical performance and program effectiveness, while key risk
indicators provide forward-looking signals about emerging threats."; "The biggest mistake is measuring
activities instead of outcomes."
Contested/time-bound: Diligent sells GRC software.

**[28] Ries, Eric - Vanity Metrics vs. Actionable Metrics (guest post, 2009).** primary. **fetched-and-verified.**
`https://tim.blog/2009/05/19/vanity-metrics-vs-actionable-metrics/`
Supports: the original coinage of "vanity metrics" and the actionable-vs-vanity distinction.
Quotable: "what I call Vanity Metrics".
Contested/time-bound: the hits example ("Let's say you have 10,000. Now what?") is paraphrased in the
companion, not quoted, as only "what I call Vanity Metrics" was captured verbatim.

**[29] Ries, Eric - Founder Stories: on vanity metrics and success theater (TechCrunch, 2011).** primary. **fetched-and-verified.**
`https://techcrunch.com/2011/09/24/founder-stories-eric-ries-vanity-metrics/`
Supports: the "success theater" framing.
Quotable: "The reason companies like to talk about vanity metrics is they both make your competitors feel bad
about themselves and also reveal nothing about your business."

**[30] Yoskovitz, Ben - Lean Analytics: The One Metric That Matters (Medium).** primary. **fetched-and-verified.**
`https://medium.com/lean-stack/lean-analytics-the-one-metric-that-matters-and-other-provocations-fd3006aab17`
Supports: the OMTM concept from a book co-author; the vanity-metric definition.
Quotable: "The One Metric That Matters is all about finding the right thing to track at the right time, based
on the type of business you're in and the stage you're at."; "We call them vanity metrics, the numbers that
make you feel good but seriously mislead."
Contested/time-bound: a Medium post; the book *Lean Analytics* (O'Reilly, 2013) is the authoritative primary.

**[31] Wikipedia - Goodhart's Law.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Goodhart%27s_law`
Supports: both canonical formulations (Goodhart 1975; Strathern 1997).
Quotable: "Any observed statistical regularity will tend to collapse once pressure is placed upon it for
control purposes."; "When a measure becomes a target, it ceases to be a good measure."
Contested/time-bound: Strathern's phrasing is from her 1997 European Review paper, which was not retrieved
independently; it is attributed via Wikipedia.

**[32] Wikipedia - Campbell's Law.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Campbell%27s_law`
Supports: Campbell's 1979 formulation on corruption pressures on quantitative social indicators.
Quotable: "The more any quantitative social indicator is used for social decision-making, the more subject it
will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is
intended to monitor."

**[33] Gothelf, Jeff - In Defense of Vanity Metrics.** practitioner. **fetched-and-verified.**
`https://jeffgothelf.com/blog/in-defense-of-vanity-metrics/`
Supports: the dissent from Ries - vanity metrics as scaffolding for organizations building measurement
capability.
Quotable: "Value will come later. So will better metrics. For now, vanity metrics do help give us direction."

**[34] Amplitude - About the North Star Framework.** vendor. **fetched-and-verified.**
`https://amplitude.com/books/north-star/about-north-star-framework`
Supports: the North Star Metric as a unifying value metric with input metrics beneath it.
Quotable: "Bringing coherence to the work of everyone in your organization is what it's all about".
Contested/time-bound: Amplitude formalized the North Star Playbook (2019); Sean Ellis is credited with
popularizing the underlying concept earlier, not from a single dated publication.

**[35] Yellowfin / insightsoftware - Best practices for a KPI dashboard.** vendor. **fetched-and-verified.**
`https://insightsoftware.com/blog/best-practices-for-designing-and-building-a-great-kpi-dashboard/`
Supports: the audience-typed dashboard design and the data-literacy caveat for analytical dashboards.
Quotable: "Should only serve users that are data literate to avoid overwhelming non-experts".
Contested/time-bound: combines "strategic/executive" into one category where [18] splits them.

---

## Claims flagged contested or time-bound

- **Single headline metric (NSM/OMTM) vs multi-perspective (BSC/HEART)** [30][34][7]. A genuine, unresolved
  debate: radical focus on one number vs balanced coverage. Kaplan and Norton argued against the one-number
  temptation; NSM advocates for it. Present both.
- **Goodhart vs Campbell: same phenomenon?** [31][32]. Both describe measurement corrupting what it measures;
  Campbell emphasizes institutional corruption, Goodhart statistical collapse. Noted as related, not
  identical.
- **Are vanity metrics always harmful?** [28][33]. Ries: yes (success theater); Gothelf: they scaffold a team
  building measurement capability. Both agree the goal is actionable metrics. Present both.
- **KPI vs OKR: competing or complementary?** [22][23]. Vendors say complementary; some OKR purists argue KPI
  watching crowds out OKR ambition. Presented as complementary with the tension noted.
- **Dashboard vs scorecard boundary is dissolving** [24]. Modern BI tools blur it (target lines, RAG on any
  dashboard); whether the conceptual distinction still matters for governance is unresolved.
- **The 5-9 item limit** [17] extrapolates Miller's Law to dashboards; directional, not measured.
- **NSM attribution** [34]: widely credited to Sean Ellis but not citable to one dated publication.
- **The Balanced Scorecard's own origin** [6]: Art Schneiderman's 1987 Analog Devices scorecard is an
  acknowledged precursor Kaplan and Norton incorporated; noted, not overclaimed.

## Notes for the companion

- **Honest framing:** the dashboard that survives Goodhart and the vanity-metric trap (actionable,
  precisely-defined, owned, reviewed). Emphasize this is a **spec/definition document**, not a live BI tool.
  Mirror the risk-register "canonical but under pressure" structure.
- **Load-bearing sections:** Anatomy (the KPI definition record; the KPI-vs-metric distinction), Debates
  (Goodhart/Campbell and vanity-vs-actionable), Relationships (dashboard vs OKRs vs scorecard; the risk
  register as governance sibling).
- **Shared scenario (governance-docs family rule):** the dashboard tracks the OUTCOMES the same Acme
  **Reporting Platform Modernization** program's risks threaten. Its headline metric is **Time to Insight**
  (the program's value goal); **Saved Views adoption** is the outcome the register's R-04 adoption risk
  threatens and the RAID log's A-02 assumption underlies; **view-list load** is what R-06 / ISS-12 affects.
  This closes the family loop: the register tracks threats, the RAID log tracks open items, the dashboard
  tracks whether the delivered program works.
- **Do not overquote or overclaim:** Kaplan-Norton [6] full text is paywalled (only the intro was read);
  Strathern's exact phrasing [31] is attributed via Wikipedia; the Ries hits example [28] is paraphrased, not
  quoted. Never fabricate a framework attribution or a date.
