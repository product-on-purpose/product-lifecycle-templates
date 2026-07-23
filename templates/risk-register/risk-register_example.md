---
title: "Acme Analytics - Reporting Platform Modernization Risk Register"
project: "Reporting Platform Modernization"
register_owner: "Marta Reyes (Program Manager)"
risk_management_approach: "Acme Corporate Risk Management Approach v3 (internal)"
last_reviewed: "2026-07-20"
review_cadence: "Fortnightly with owners; residual 15+ escalated to the steering group monthly"
risk_appetite: "Up to a two-week schedule slip and up to GBP 100k of unplanned cost are acceptable; no PII-exposure or data-loss risk above residual 6"
status: active
related: ["../prd/prd_example.md (Saved Views for Dashboards PRD)", "../sdd/sdd_example.md (Saved Views design)", "raid-log (forthcoming: the program RAID log, whose R column is this register)", "kpi-dashboard (forthcoming: the program KPI dashboard, tracking the outcomes these risks threaten)"]
doc_type: risk-register
size: full
source_template: risk-register
source_template_version: 0.1.0
---

<!--
This is a worked example for the risk-register bundle: a realistic, fully filled full-variant risk register
for a fictional program at Acme Analytics. It is the governance-docs family's shared scenario - the same
Reporting Platform Modernization program whose risks appear as the R column of the raid-log example and whose
threatened outcomes are tracked on the kpi-dashboard example. The "Saved Views" work it delivers is the same
feature the delivery-docs family examples (PRD, SDD) cover.

All figures, scores, dates, and names are illustrative. A risk register is a living document; this is a
snapshot as of the last-reviewed date. Use it as a model of shape, scoring discipline, and tone, not as a
source of facts about real products.
-->

# Acme Analytics - Reporting Platform Modernization Risk Register

## Purpose and Scope

Risks to the **on-time, on-budget delivery and adoption** of the Reporting Platform Modernization program,
whose headline deliverable is the Saved Views capability (launch target: end of Q3). Owned by the program
manager (Marta Reyes) and maintained by the PMO; governed by the Acme Corporate Risk Management Approach v3,
which sets the categories, the 5x5 scale below, and the appetite.

**Out of scope:** business-as-usual IT and security risks (tracked in the corporate enterprise register), and
product-outcome risks such as whether the Time-to-Insight target is met (tracked as metrics on the program
KPI dashboard, a forthcoming sibling, not as risks here). This register tracks
threats to *delivering* the program; the dashboard tracks whether the delivered program *works*.

## Scoring Scale

**Likelihood (1-5), within the delivery window (now to launch):** 1 = Rare (<10%), 2 = Unlikely (10-30%),
3 = Possible (30-55%), 4 = Likely (55-80%), 5 = Almost certain (>80%).

**Impact (1-5), anchored to schedule, cost, and compliance:** 1 = Negligible (<3-day slip); 2 = Minor
(up to 1-week slip); 3 = Moderate (1-2 week slip, or <GBP 100k); 4 = Major (3-4 week slip, GBP 100k-1M, or a
reportable data incident); 5 = Severe (launch missed, >GBP 1M, or a PII breach).

**Score = Likelihood x Impact (1-25).** Zones (set to Acme's appetite, not a generic band): **15+ red**
(escalate), **8-14 amber** (actively managed), **<8 green** (monitored). Every risk is scored **inherent**
(before the listed controls) and **residual** (after they operate); residual is the figure reported to the
steering group, and the inherent-to-residual gap is the evidence a control is working. *(Illustrative scale;
a real program would ratify these anchors with its steering group.)*

## Risks

Ordered by **residual** score, highest first; the opportunity row (R-07) is listed last, since its "higher
is better" score does not sort against threat residuals. For an enhanced opportunity, residual **exceeds**
inherent, because the enhancement raises the odds of capture (the mirror of a threat, where controls pull
residual down). *(Illustrative entries.)*

| ID | Category | Risk (cause -> event -> consequence) | Inherent (LxI=S) | Response (strategy + action) | Residual (LxI=S) | Trigger / KRI | Owner / Actionee | Proximity | Status |
|---|---|---|---|---|---|---|---|---|---|
| R-01 | Vendor | Because the third-party charting library's licence renews mid-build, there is a risk its terms change and force a re-platform of every dashboard, delaying launch by a quarter | 3x5=15 | **Mitigate:** negotiate a locked 24-month licence before the renewal date; spike a fallback rendering path in parallel | 2x5=10 | Vendor circulates new licence terms, or renewal notice received | Dana Osei / Legal | Q3 (before renewal) | In Mitigation |
| R-05 | Security / PII | Because saved views can embed filter values (e.g. a named customer segment), there is a risk a shared view exposes PII to a viewer without entitlement, causing a reportable incident | 3x4=12 | **Escalate + reduce:** entitlement check on view load; PII-in-filter scan before share. These are preventive controls, so they cut likelihood, not impact. Escalated: residual (8) exceeds the PII appetite line (6) | 2x4=8 | Any saved view shared outside its source workspace | Sam Okafor / Security | Ongoing | Escalated |
| R-04 | Adoption | Because Recurring Analysts have deep habits in the legacy report flow, there is a risk they do not adopt Saved Views inside the program's 60-day launch-success window, so a remediation sprint is triggered that slips program close-out | 4x3=12 | **Reduce:** design-partner pilot with 6 analysts pre-launch; in-product nudge; adoption tracked on the KPI dashboard | 2x3=6 | Pilot adoption <50% at the two-week checkpoint | Priya Nair / UX Research | Launch-success window | In Mitigation |
| R-06 | Performance | Because a dashboard may accumulate many saved views, there is a risk view-list load exceeds the 500ms budget, degrading the very speed the program promises | 3x3=9 | **Reduce:** paginate and lazy-load the view list; load test at 3x the expected view count before launch | 2x3=6 | p95 view-list load >400ms in staging | Dana Osei | Pre-launch | In Mitigation |
| R-02 | Data | Because saved-view configs migrate from the legacy key-value store to the new schema, there is a risk of silent config loss, so analysts lose saved views on cutover | 3x4=12 | **Reduce:** dual-write and reconcile counts before cutover; keep the legacy store read-only for 30 days as rollback | 1x4=4 | Reconciliation count mismatch >0 in the migration dry run | Lee Zhang / Data Eng | Cutover week | In Mitigation |
| R-07 | Opportunity | Because the Saved Views feature emits rich usage telemetry, there is an opportunity to accelerate the planned Recommendations feature by reusing that signal, pulling its value forward a quarter | 3x4=12 (upside) | **Enhance:** instrument view-usage events to the Recommendations spec now, at near-zero extra cost | 4x4=16 (upside; residual > inherent) | Recommendations team confirms the telemetry meets their needs | Priya Nair | Next quarter | Open |

## Review and Ownership

Reviewed **fortnightly** by the PMO with each risk owner. Any risk whose **residual** score reaches 15+, or
any PII/data risk above the appetite line (residual 6), is escalated to the **steering group** at its monthly
meeting; the **board** sees only risks over appetite, quarterly, as an exception summary. Owners update their
own rows before each review; the register owner reconciles and re-orders.

A risk that **materializes** moves to the program issue log (the RAID log's Issues column, a forthcoming
sibling) the day its trigger fires, and its row here is marked **Materialized** with a link (see R-03 below).
Last reviewed **2026-07-20**; next review **2026-08-03**.

## Escalation and Risk Appetite

**Appetite (from the Risk Management Approach v3, illustrative):** the program will accept up to a **two-week
schedule slip** and up to **GBP 100k** of unplanned cost, but has **near-zero appetite for PII exposure or
data loss** - no such risk may sit above **residual 6** without steering-group sign-off.

**Escalation path:** owner -> program manager (fortnightly) -> steering group (monthly, for residual 15+ or
any over-appetite risk) -> board (quarterly, exceptions only).

**Currently escalated:** **R-05 (PII in saved views)**, residual **8**, is above the PII appetite line of 6.
It is with the steering group with a request to either fund a stronger entitlement control (to bring residual
to 6 or below) or formally accept the residual at board level. This is the one risk on the register that
appetite, not score alone, forces upward: at residual 8 it is only amber by the generic zones (8-14), but red
against the PII rule.

## Closed and Materialized Risks

Kept as the audit trail and the scoring feedback loop; not deleted.

| ID | Category | Outcome | Note and lesson |
|---|---|---|---|
| R-03 | Key-person | **Materialized 2026-06-14** -> issue ISS-11 (program issue log) | The engineer holding the query-engine knowledge left. Had been scored **residual 6** (amber-low) on an assumption of a long notice period; that was optimistic. Lesson: owner-departure risks are now floored at **residual 9** until a documented handover exists. The materialized issue is tracked on the RAID log, not here. |
| R-08 | Performance | **Closed 2026-05-30** | Early concern that the new query engine could not meet the 500ms budget at all. **Mitigated:** a load test at 3x target passed; the risk was retired and the residual concern narrowed to view-list rendering, which is now the active R-06. A closed risk that narrowed rather than vanished. |

*(All IDs, dates, scores, and names are illustrative.)*
