---
title: "Reporting Platform Modernization Status Report - 14-28 July 2026"
program: "Reporting Platform Modernization (Acme Analytics)"
reporting_period: "14-28 July 2026"
prepared_by: "Marta Reyes (Program Manager)"
audience: "Program steering group"
cadence: "Fortnightly, timed to the program steering group's review"
status: "Amber"
related:
  - "../kpi-dashboard/kpi-dashboard_example.md (source of every Metrics row below)"
  - "../risk-register/risk-register_example.md (source of R-05, and the register's escalation and appetite language)"
  - "../raid-log/raid-log_example.md (source of ISS-11, ISS-12, D-01, A-01 and A-02, and the escalation aging)"
  - "../incident-postmortem/incident-postmortem_example.md (DEF-2291; the trigger for R-05's 2026-07-14 escalation)"
  - "../definition-of-done/definition-of-done_example.md (the 2026-07-24 amendment reported under Accomplishments)"
  - "../product-roadmap/product-roadmap_example.md (the Now-lane commitment Saved Views work reports against)"
  - "../okrs/okrs_example.md (the FY26 Q3 objective the Metrics section's two headline rows already feed)"
doc_type: status-report
size: full
source_template: status-report
source_template_version: 0.1.0
---

> **Worked example.** A filled `status-report`, full variant, for the **Reporting Platform Modernization**
> program at Acme Analytics, the same program the `kpi-dashboard`, `risk-register`, `raid-log`,
> `product-roadmap` and `okrs` examples already cover. Per the `communication-docs` family contract, this
> document owns none of its own facts: every number and every reference ID below is read from one of those
> five siblings, or from the `incident-postmortem` and `definition-of-done` examples, and the table below
> states where each one comes from rather than restating it as if this report discovered it.
>
> **Read the dates.** It covers 14-28 July 2026 and is written as though prepared on the last of those days,
> one day after the [FY26 Q3 OKRs](../okrs/okrs_example.md) were agreed on 27 July and three days after the
> [Definition of Done](../definition-of-done/definition-of-done_example.md) amendment on 24 July. Everything
> it cites, the [KPI dashboard](../kpi-dashboard/kpi-dashboard_example.md), the
> [risk register](../risk-register/risk-register_example.md) and the
> [RAID log](../raid-log/raid-log_example.md), all last reviewed 20 July, the
> [DEF-2291 postmortem](../incident-postmortem/incident-postmortem_example.md), dated 16 July, already existed
> by then. Nothing below cites a document dated after 28 July.
>
> All figures, names and dates are illustrative and drawn from documents that already exist elsewhere in this
> library, not invented for this report.

# Reporting Platform Modernization Status Report - 14-28 July 2026

## Summary

This fortnight reads amber. The program's two headline numbers are Time to Insight and Saved Views adoption,
both of which the kpi-dashboard already calls amber and improving, and neither has crossed into green yet. The
item most worth this group's attention is the PII-exposure gap tracked as R-05: a shared saved view can expose
a viewer to revenue data outside their region, and the ask raised at triage two weeks ago, fund a stronger
entitlement control or accept the residual formally, still has no answer. Both decisions below sit with this
group; neither is optional this period.

## Status

| Dimension | Status | Threshold | What changed |
|---|---|---|---|
| Overall | Amber | The green bar sits at a 25 percent Time to Insight improvement and 55 percent Saved Views adoption together; a single metric crossing its own line is not enough on its own to move the overall call | R-05's steering-group ask has now been open 14 days without a decision; the query-engine dependency (D-01) stayed confirmed, so no schedule slip followed from it this period |

## Metrics

| Metric | Current | Target / Threshold | Source of record | Reads as |
|---|---|---|---|---|
| Time to Insight | 18 percent faster than the FY26 baseline | 30 percent by Q3 is the target; 25 percent is the separate green line | kpi-dashboard, last reviewed 20 Jul 2026 | Amber. It clears neither line, though it sits closer to the green line than to the target |
| Saved Views adoption | 41 percent of Recurring Analysts weekly | 60 percent by end Q3 is the target; 55 percent is the separate green line | kpi-dashboard, last reviewed 20 Jul 2026 | Amber, and only one point clear of the 40 percent floor below which the same table calls it red |
| View-list load, p95 | 620ms | Green sits under 500ms; red starts past 700ms | kpi-dashboard, last reviewed 20 Jul 2026 | Amber. This is the identical figure carried as ISS-12 on the RAID log; see Risks and Issues, not reported twice |
| Weekly active analysts | 495 distinct analysts | Hold at 480 or more | kpi-dashboard, last reviewed 20 Jul 2026 | Green |
| Migration integrity | Not yet measurable; cutover has not happened | 100 percent required at cutover | kpi-dashboard, last reviewed 20 Jul 2026 | No colour assigned. Scoring a pre-cutover metric would manufacture a result nobody has measured |

## Accomplishments

- Reverified the DEF-2291 fix and re-ran the entire twelve-combination permission matrix from the start, not
  only the failing case, resuming Phase 2 sharing testing on 15 July after a two-day suspension.
- Closed the twin gap the postmortem named: TC-053 now asserts the same aggregate-before-filter defect class
  against the dashboard's row-count badge, the other element on that computation path.
- Amended the squad's Definition of Done on 24 July so any future change touching entitlement logic requires
  the full permission matrix re-run as a Sprint-level criterion, not left to a risk-tier test to catch.

## Milestones

| Milestone | Target date | Status | Note |
|---|---|---|---|
| Query engine handoff from the Platform team | 1 Aug 2026 | Open, and confirmed | RAID log dependency D-01: still an open handoff, not yet delivered, but confirmed by Lee Zhang's team rather than left unconfirmed like D-03 below. Saved Views build cannot begin without it, which is why it stays on this list even while it reads green |
| Design-partner pilot readout | 5 Aug 2026 | Upcoming | Tests RAID log assumption A-02, that analysts want saved views enough to abandon a habitual workflow. A weak readout here is the likelier reason Saved Views adoption stalls amber than anything in the build |
| Charting vendor licence terms locked | 15 Aug 2026 | Unconfirmed | RAID log dependency D-03, Legal's sign-off, still unconfirmed. It rests on assumption A-01, that the vendor renews on current terms; if that assumption fails, register risk R-01 hardens from a watched item into a live re-platform |

## Risks and Issues

| Ref | Description | Status | What changed |
|---|---|---|---|
| R-05 (risk-register) | A shared saved view can disclose PII to a recipient without the matching entitlement | Escalated, residual 8, above the register's PII appetite line of 6 | 14 days with the steering group, counted from the 14 July escalation raised at the DEF-2291 postmortem's triage; still no funding decision or formal residual acceptance. The RAID log's own ageing column reads 6 days because it was last reviewed earlier in this period: the age is recomputed here from the same escalation date, not restated from the log |
| ISS-11 (raid-log) | Query-engine lead departed with no documented handover; the materialized form of register risk R-03 | Open, escalated | Past the RAID log's own two-week aging line; the backfill-contractor budget is the second row in Decisions Needed below |
| ISS-12 (raid-log) | Staging p95 view-list load recorded over the 500ms budget | In progress | Same reading as the View-list load row above, not a second problem. Its 24 July resolution target has passed with no fresher number logged; the next reading falls due at the dashboard's August review |

## Decisions Needed

| Decision | Decider | Needed by | Context |
|---|---|---|---|
| Fund a platform-level entitlement-aggregate control for shared saved views, or formally accept R-05's residual at board level | Steering group | No formal date is on record; the ask has sat open since 14 July | Raised at the DEF-2291 postmortem's triage and carried onto the risk register as R-05's live action. The longer it stays undecided, the harder the residual becomes to defend at a board review |
| Approve a GBP 45,000 backfill contractor to cover the departed query-engine lead (ISS-11) | Steering group | 31 Jul 2026, the issue's own resolution target | Without it, nobody is driving the handover behind milestone D-01 past the current team's existing bandwidth |

## Next Steps

- Read the design-partner pilot out on 5 August against assumption A-02; treat a weak result as the leading
  explanation for Saved Views adoption if it stays amber into the next report.
- Confirm the charting vendor's licence terms by 15 August; if they move, bring forward the fallback rendering
  spike R-01 already has planned rather than waiting for the licence to actually change.
- Keep paginating and lazy-loading the view list under the R-06 mitigation, and re-test at three times today's
  view count before the dashboard's next scheduled review closes ISS-12 out.
- Carry Saved Views from its current specification into general availability, the same initiative the FY26 Q3
  OKRs already hold against their second key result's 60 percent adoption target.
