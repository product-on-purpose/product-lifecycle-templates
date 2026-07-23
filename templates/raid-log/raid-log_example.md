---
title: "Acme Analytics - Reporting Platform Modernization RAID Log"
project: "Reporting Platform Modernization"
raid_expansion: "Risks, Assumptions, Issues, Dependencies"
log_owner: "Marta Reyes (Program Manager)"
last_reviewed: "2026-07-20"
review_cadence: "Weekly with workstream leads; monthly deep dive at the program board"
status: active
related: ["../risk-register/risk-register_example.md (the program risk register; this log's R quadrant summarizes it)", "../prd/prd_example.md (Saved Views for Dashboards PRD)", "../sdd/sdd_example.md (Saved Views design)", "../kpi-dashboard/kpi-dashboard_example.md (the program KPI dashboard, tracking the outcomes these items threaten)"]
doc_type: raid-log
size: full
source_template: raid-log
source_template_version: 0.1.0
---

<!--
This is a worked example for the raid-log bundle: a realistic, fully filled full-variant RAID log for the
same Acme Analytics Reporting Platform Modernization program that the risk-register example covers. It is
built to demonstrate QUADRANT MIGRATION and the register-is-the-R relationship:
- the Risks quadrant summarizes the risk register and links to it by ID (it does not duplicate the scoring);
- issue ISS-11 IS the materialized key-person risk (R-03) from the register, migrated into an issue;
- the Assumptions are the beliefs the register's risks rest on (A-01 feeds R-01, A-02 feeds R-04, A-03 feeds R-02);
- the Dependencies connect the inbound query-engine delivery and the outbound Recommendations telemetry
  (the R-07 opportunity) to the risks they carry.
It uses the Risks, Assumptions, Issues, Dependencies expansion, declared in the scope line.

All figures, dates, and names are illustrative. A RAID log is a living document; this is a snapshot as of the
last-reviewed date. Use it as a model of shape, migration discipline, and tone, not as a source of facts.
-->

# Acme Analytics - Reporting Platform Modernization RAID Log

## Purpose and Scope

RAID log for the **Reporting Platform Modernization** program (headline deliverable: the Saved Views
capability; launch target end of Q3). **RAID = Risks, Assumptions, Issues, Dependencies** (this program uses
the Assumptions/Dependencies expansion, not Actions/Decisions). Owned by the program manager (Marta Reyes),
populated by workstream leads, reviewed weekly.

The **Risks** quadrant is a summary that points to the standalone
[risk register](../risk-register/risk-register_example.md), which holds the authoritative inherent/residual
scoring, triggers, and appetite; this log does not duplicate that detail. Out of scope: business-as-usual IT
risks (corporate register) and product-outcome metrics (the program KPI dashboard, a forthcoming sibling).

## Risks

Summary view; the [risk register](../risk-register/risk-register_example.md) is authoritative. Severity here
is the register's residual band. *(Illustrative.)*

| ID | Risk (cause -> event -> consequence) | Severity | Response | Owner | Status | Register ref |
|---|---|---|---|---|---|---|
| R-01 | Charting-library licence may change mid-build and force a re-platform, slipping launch a quarter | Amber (residual 10) | Mitigate: lock a 24-month licence before renewal | Dana Osei | In Mitigation | [register R-01](../risk-register/risk-register_example.md) |
| R-05 | A shared saved view may expose PII to a viewer without entitlement, causing a reportable incident | Amber, over PII appetite (residual 8) | Escalate + reduce: entitlement check, PII scan | Sam Okafor | Escalated | [register R-05](../risk-register/risk-register_example.md) |
| R-04 | Analysts may not adopt Saved Views in the launch-success window, triggering a remediation sprint | Green (residual 6) | Reduce: design-partner pilot; in-product nudge | Priya Nair | In Mitigation | [register R-04](../risk-register/risk-register_example.md) |
| R-06 | View-list load may exceed the 500ms budget as saved views accumulate (partially materialized in staging as ISS-12; launch-level risk remains open) | Green (residual 6) | Reduce: paginate and lazy-load; load test at 3x view count | Dana Osei | In Mitigation | [register R-06](../risk-register/risk-register_example.md) |
| R-02 | Saved-view configs may suffer silent loss during migration from the legacy store to the new schema | Green (residual 4) | Reduce: dual-write and reconcile counts; legacy store read-only 30 days | Lee Zhang | In Mitigation | [register R-02](../risk-register/risk-register_example.md) |

## Assumptions

The beliefs the risks above rest on. Each links to the risk it feeds. *(Illustrative.)*

| ID | Assumption | Source | Confidence | Impact if false | Validate by | Owner | Status |
|---|---|---|---|---|---|---|---|
| A-01 | The charting vendor will renew on current licence terms | Vendor management | Low | Forces a re-platform; this is the driver of R-01 | Confirm with vendor by 2026-08-15 | Dana Osei | Open |
| A-02 | Recurring Analysts want saved views enough to change a deeply-held workflow | Discovery interviews | Medium | Adoption stalls; this is the driver of R-04 | Design-partner pilot readout 2026-08-05 | Priya Nair | Open |
| A-03 | The legacy saved-view config schema is fully documented | Data Eng | Low | Silent config loss on migration; drives R-02 | Migration dry-run 2026-07-25 | Lee Zhang | Open |

## Issues

Things that have already happened. ISS-11 is the materialized key-person risk (R-03) from the register,
migrated here. *(Illustrative.)*

| ID | Issue | Severity | Priority | Cause | Resolution plan | Raised | Target | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| ISS-11 | Query-engine lead left; handover incomplete (materialized from register risk R-03) | High | High | Key-person dependency, no documented handover | Backfill contractor + pair a second engineer; document the engine | 2026-06-14 | 2026-07-31 | Marta Reyes | Open (escalated) |
| ISS-12 | Staging p95 view-list load measured at 620ms, over the 500ms budget | Medium | High | Unpaginated view list under load (the R-06 watch item materialized in staging) | Paginate and lazy-load; re-test at 3x view count | 2026-07-10 | 2026-07-24 | Dana Osei | In Progress |

## Dependencies

Structural relationships. D-02 is the outbound side of the register's R-07 opportunity. *(Illustrative.)*

| ID | Direction | Type | Dependency | Needed by | Impact if missed | Party | Status |
|---|---|---|---|---|---|---|---|
| D-01 | In | Cross-team | Platform team delivers the new query engine | 2026-08-01 | Delays all Saved Views work; on the critical path | Platform team (Lee Zhang) | Confirmed |
| D-02 | Out | Cross-team | Recommendations team consumes our saved-views telemetry | 2026-09-30 | Their feature slips; this is the outbound side of the R-07 opportunity | Recommendations team (Priya Nair liaises) | Confirmed |
| D-03 | In | Third-party | Legal sign-off on the charting-vendor licence | 2026-08-15 | Blocks the R-01 mitigation (the locked licence) | Legal | Unconfirmed |

## Review and Ownership

Reviewed **weekly** by the program manager with workstream leads (the full log), with a **monthly deep dive**
at the program board. Issues are updated as they move; risks and assumptions are reviewed monthly (with
event-driven exceptions). The **program manager owns** the log; **each item has a named owner**. The steering
group sees only the **escalated rows** (below), pre-read before the monthly meeting, not the full log. Last
reviewed **2026-07-20**; next review **2026-07-27**.

## Escalation and Aging

Items needing a decision above the team. Aging is measured from the escalation date. *(Illustrative.)*

| Item | Decision needed | With | Age | Why it is escalated |
|---|---|---|---|---|
| ISS-11 | Approve the backfill-contractor budget (GBP 45k) | Steering group | 16 days | Blocks the query-engine handover; over the two-week aging line |
| R-05 | Fund a stronger entitlement control, or formally accept the residual | Steering group | 6 days | Residual 8 is above the near-zero PII appetite line (6); appetite, not score, forces it up |

**Aging note:** ISS-11 has now been escalated 16 days without a decision, past the program's two-week line.
This is a governance signal, not a team failure: the team has done its part (a plan exists); the decision is
stuck above them.

## Cross-Quadrant Summary

**Open items:** 5 risks summarized (1 escalated), 3 assumptions (2 low-confidence), 2 issues (both
high-priority, 1 escalated), 3 dependencies (1 critical-path, 1 unconfirmed).

**Migrations this period:**
- **R-03 -> ISS-11.** The key-person risk materialized (the engineer left) and became an issue. Its register
  row is now marked Materialized; the live work is here as an issue. This is the canonical risk-to-issue
  migration.
- **R-06 -> ISS-12.** The performance risk partially materialized in staging (load over budget) and is now a
  tracked issue, while the launch-level performance risk remains open on the register.

**Watch (most likely to migrate next):** **A-01** (the vendor will renew on current terms) is a
low-confidence assumption with high impact; if it invalidates, it becomes an issue and hardens R-01. It is
the row to validate first. This is what a RAID log is for: seeing, in one place, that the program's next
problem is most likely to arrive through an unvalidated assumption, not through a risk already on the
register.

*(All IDs, dates, figures, and names are illustrative.)*
