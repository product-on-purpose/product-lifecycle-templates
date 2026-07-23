# History: RAID Log bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-07-22

- Initial RAID Log bundle. **Second member of the `governance-docs` family** (classification axis), alongside
  `risk-register`. Catalog entry 151. Conforms to the
  [governance-docs contract](../../docs/internal/contracts/governance-docs.md) (`classification: utility`,
  `beta`, sizes `[lean, full]`); gate check K green.
- **Scope: the RAID log, framed honestly.** The companion's sections 1, 2, and 6 make the case: RAID is a
  **consolidation convention, not a standard** - no documented inventor, no governing body (PRINCE2 7th does
  not name it, PMBOK does not define it), and a **genuinely contested acronym** (the A is Assumptions or
  Actions, the D is Dependencies or Decisions; the APM and the IRM use different expansions in their own
  materials). The bundle teaches the RAID log that survives its two defining failures: the acronym ambiguity
  (the fix is "pick one expansion, write it down, stop relitigating it") and "documentation theater" (set up
  at kickoff, abandoned by week three; the fix is a real review cadence and one named owner per item).
- **The load-bearing honest-retrieval discipline:** do not assert a single canonical RAID expansion or a
  founding source, because there is none. The companion states the ambiguity and attributes it to the bodies
  that exhibit it, rather than manufacturing a clean origin story. The widely-circulated "78% of UK government
  projects" origin statistic could not be verified and is used nowhere in the bundle.
- **Variants: `lean` and `full`.** The catalog lists S/M; the two-weight split fits. Lean is the six sections
  every RAID log needs: Purpose and Scope, the four quadrant tables (Risks, Assumptions, Issues,
  Dependencies), and Review and Ownership. Full adds richer per-quadrant fields (validation dates,
  severity-vs-priority, dependency direction and type), an Escalation and Aging section, and a Cross-Quadrant
  Summary. Nesting verified: lean's six H2 headings are a strict ordered subset of full's eight.
- **The sharpest teaching points**, carried through companion, guide, and example: (1) the four quadrants are
  **genuinely different kinds of thing** with different fields and cadences (a risk might happen; an
  assumption is believed true without proof; an issue has happened; a dependency is a relationship); (2) the
  unifying insight is **quadrant migration** (an assumption that fails becomes an issue; a dependency that
  slips becomes a risk, then an issue; a risk that materializes becomes an issue); (3) the RAID log is the
  **weekly working consolidation** while the `risk-register` is the **deepened R** for governance; (4) an
  assumption is a **latent risk in disguise**; (5) a **dependency has a direction** (inbound/outbound) that
  drives its escalation path.
- **Worked example demonstrates quadrant migration and chains within the family.** `raid-log_example.md` is a
  full-variant RAID log for the same Acme Analytics **Reporting Platform Modernization** program as the
  `risk-register` example. Its Risks quadrant summarizes and links to the register (not duplicating the
  scoring); issue **ISS-11 is the materialized key-person risk R-03** from the register, migrated into an
  issue; its Assumptions are the beliefs those risks rest on; and its Dependencies connect the inbound
  query-engine delivery and the outbound Recommendations telemetry (the register's R-07 opportunity). The
  Cross-Quadrant Summary reads the migration pattern rather than re-listing rows.
- **`pairs_with: []`.** There is no `deliver-raid-log` or `govern-raid-log` skill in pm-skills (checked
  against `tools/known-skills.txt`, 2026-07-22). Recorded as context in `raid-log_guide.md`.
- Companion researched 2026-07-22 across four parallel dimensions and 25 tier-ranked, deduplicated sources
  (see `raid-log_research-log.md` for per-source retrieval status). The "R" quadrant overlaps the
  `risk-register` bundle's research, so this fan-out focused on the A/I/D quadrants and the RAID-specific
  framing. Primary anchors include the IRM Short Guide to RAID, the APM blog (showing the Actions/Decisions
  expansion in a primary body's own writing), and the PRINCE2 7th coverage. Claims flagged contested: the
  acronym expansion, whether agile needs RAID, whether Assumptions and Dependencies deserve their own
  quadrants, severity-vs-priority, and one-table-vs-four-tabs. Nothing not fetched-and-verified is quoted.
- Status: `beta`. Gate-green, zero real usage by anyone other than the author.
