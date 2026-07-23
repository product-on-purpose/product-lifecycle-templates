# History: KPI Dashboard bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-07-22

- Initial KPI Dashboard bundle. **Third member of the `governance-docs` family** (classification: utility),
  completing the family alongside `risk-register` and `raid-log`. Catalog entry 139. Conforms to the
  [governance-docs contract](../../docs/internal/contracts/governance-docs.md); gate check K green on the
  classification axis. Its axis (`classification: utility`) was resolved at contract time in
  [ADR 0024](../../docs/internal/decisions/0024-adopt-governance-docs-family-contract.md): a KPI dashboard is
  a standing measurement instrument, not a `phase: measure` output.
- **Scope: a dashboard DEFINITION, not a live BI tool** (the catalog's "dashboards-as-spec edge case", EC-2).
  The bundle is the platform-agnostic specification - which metrics matter, how each is calculated, the
  target, owner, data source, thresholds, and cadence - that precedes and outlives the build in Tableau,
  Looker, Power BI, or Amplitude. The companion (sections 1 and 8) makes this the load-bearing framing.
- **The honest core:** a KPI dashboard is the artifact most exposed to the corrupting power of measurement.
  The companion (section 6) states both named laws - Goodhart's ("when a measure becomes a target, it ceases
  to be a good measure") and Campbell's - and the vanity-vs-actionable-metrics debate (Eric Ries's coinage vs
  Jeff Gothelf's scaffolding dissent), then takes the constructive synthesis: choose actionable metrics, lock
  their definitions, pair lagging targets with leading indicators, and treat an all-green dashboard with
  suspicion.
- **Variants: `lean` and `full`.** The catalog lists S/M/L; the two-weight split fits. Lean is the three
  sections a team needs: Purpose and Audience, the KPI table, and Review and Ownership. Full adds the
  governance-grade layers: Metric Definitions (formula, inclusions/exclusions, owner vs data steward), Layout
  and Thresholds (RAG bands and escalation), and Data Sources and Refresh. Nesting verified: lean's three H2s
  are a strict ordered subset of full's six (the three detail sections insert between KPIs and Review).
- **The sharpest teaching points**, carried through companion, guide, and example: (1) a **KPI is not just
  any metric** - it is a metric paired with an objective and a target; (2) this is a **definition, not the
  live tool** (definition precedes visualization); (3) **metric-definition discipline** - unlocked
  definitions mean "every dashboard becomes a new version of the truth"; (4) **leading vs lagging**
  indicators; (5) **vanity vs actionable** and **Goodhart's Law**; (6) one **named owner** per metric
  (distinct from the data steward). These run through the guide's four-way comparison table and six named
  anti-patterns.
- **Worked example closes the governance-docs family loop.** `kpi-dashboard_example.md` is a full-variant
  dashboard spec for the same Acme Analytics **Reporting Platform Modernization** program as the
  `risk-register` and `raid-log` examples. Where the register tracks threats and the RAID log tracks open
  items, the dashboard tracks whether the delivered program works: **Saved Views adoption** is the outcome the
  register's R-04 adoption risk threatens and the RAID log's A-02 assumption underlies; **view-list load** is
  the metric the RAID log's ISS-12 issue (from register risk R-06) moved. It reads explicitly beside the risk
  register, demonstrating the dashboard-and-register governance pairing.
- **`pairs_with: []`.** There is no `deliver-kpi-dashboard` or `govern-kpi-dashboard` skill in pm-skills
  (checked against `tools/known-skills.txt`, 2026-07-22). Recorded as context in `kpi-dashboard_guide.md`.
- Companion researched 2026-07-22 across five parallel dimensions and 35 tier-ranked, deduplicated sources
  (see `kpi-dashboard_research-log.md` for per-source retrieval status). Primary anchors include KPI.org, the
  Balanced Scorecard Institute, Rockart's 1979 Critical Success Factors, ISACA on KRIs vs KPIs, and the
  Goodhart/Campbell law pages. Several strong sources are partial-access (Kaplan and Norton's 1992 HBR article
  is paywalled - only the introduction was read; Strathern's exact Goodhart phrasing is attributed via
  Wikipedia; the Ries hits example is paraphrased, not quoted); those carry the honest-retrieval qualifier and
  no fabricated quote. Claims flagged contested: single-metric (NSM/OMTM) vs multi-perspective (BSC),
  Goodhart-vs-Campbell equivalence, whether vanity metrics are always harmful, KPI-vs-OKR complementarity, the
  dissolving scorecard/dashboard boundary, and the 5-9 cognitive limit. Nothing not fetched-and-verified is
  quoted.
- Status: `beta`. Gate-green, zero real usage by anyone other than the author.
