---
title: "Saved Views Adoption Nudge Experiment Readout"
experiment_name: "Saved Views Adoption Nudge"
design_doc: "../experiment-design-doc/experiment-design-doc_example.md"
author: "Priya Nair (PM, Reporting)"
decision_maker: "Priya Nair (PM, Reporting)"
start_date: "2026-08-03"
end_date: "2026-08-31"
decision: "Null (stop): shelve the fifth-view prompt rather than rerun it unchanged."
readout_date: "2026-09-04"
doc_type: experiment-readout
size: full
source_template: experiment-readout
source_template_version: 0.1.0
---

> **Worked example.** A filled `experiment-readout`, full variant, reporting the same Saved Views
> adoption-nudge test that
> [the experiment-design-doc example](../experiment-design-doc/experiment-design-doc_example.md) planned
> for Acme Analytics, chained onto that same [PRD](../prd/prd_example.md),
> [KPI dashboard](../kpi-dashboard/kpi-dashboard_example.md), [OKRs](../okrs/okrs_example.md) and
> [risk register](../risk-register/risk-register_example.md) thread. Dated 2026-09-04, four days after the
> test's own end date of 2026-08-31. Its recommended outcome is a null, with the point estimate finishing
> above control, chosen so that every commitment the design doc made (the daily sample-ratio check, the
> week-by-week novelty read, the guardrail thresholds, and the decision rule's own null branch) is actually
> exercised by this readout rather than skipped past on an easy win.
>
> All figures, account counts, and event names are illustrative.

# Saved Views Adoption Nudge Experiment Readout

## Executive Summary

Decision: stop. The fifth-view prompt did not raise weekly Saved Views adoption against the no-prompt
control by a margin the platform calls statistically significant over the four weeks. Treatment finished
two points above control, and that gap sits inside an interval wide enough to still reach zero, which reads
as inconclusive rather than as either side winning outright. The finding worth keeping is narrow: the
prompt tested the design doc's explanation that analysts had not noticed the Views menu, and a nudge large
enough to matter for that explanation did not show up. The risk register's own explanation for R-04, deep
habits in the legacy report flow, was not what this test measured. The fifth-view prompt is shelved rather
than rerun unchanged, and a different mitigation for R-04 goes to the next Reporting Platform Modernization
steering review.

## Context and Setup

Ran 2026-08-03 through 2026-08-31, the full four weeks the design doc specified, with no early stop.
Control (no prompt) and treatment (the fifth-view prompt) ran 50/50, randomized by customer account rather
than by individual analyst, exactly as the design doc fixed. 231 accounts were assigned over the window,
117 to control and 114 to treatment, against the roughly 230 accounts the design doc estimated as the
eligible population; the six design-partner pilot analysts and their accounts stayed excluded throughout,
as planned. Full plan:
[Saved Views Adoption Nudge Experiment Design Doc](../experiment-design-doc/experiment-design-doc_example.md).

**What ran differently from the design doc.** Nothing. Eligibility, allocation, the prompt's own
trigger condition, and the four-week duration all matched the design doc exactly; no mid-test change was
made to any of them.

## Key Results: Primary Metrics

| Metric | Control | Test | Change (abs) | Change (rel) | CI | Sig? |
|---|---|---|---|---|---|---|
| Saved Views adoption (share of Recurring Analysts using a saved view weekly) | 43% | 45% | +2 pts | +5% | -11 to +15 pts (95% CI) | No |

The interval is at 95%, the counterpart of the 5% significance level the design doc fixed as the platform's
standard setting, with 80% power, rather than a level this test chose for itself. At that level the lift is not significant, and the
interval's own width, 26 points end to end, is the real story: it is wide enough to contain both a
meaningful loss and a meaningful gain, which is the direct consequence of sizing this test against roughly
230 accounts rather than a larger population.

## Key Results: Supporting Metrics

| Guardrail | Design-doc threshold | Control | Test | Status |
|---|---|---|---|---|
| Weekly active analysts | Not below 480 at any point during the test | 495 (pre-test) | lowest daily reading, either arm combined: 487 | Held |
| Dashboard load error rate | Not above its pre-test level | pre-test baseline | stayed at the pre-test level throughout | Held |
| Shared-view permission incidents | Zero, either arm | 0 | 0 | Held |

No guardrail came close to its threshold at any point in the four weeks, so none of the three triggered the
design doc's early-stop rule.

## Validity Checks

| Check | Result | Notes |
|---|---|---|
| Sample ratio mismatch | Checked daily, no flag raised | The realized 117/114 split stayed under the platform's chi-squared threshold on all 29 scheduled daily reads |
| Novelty effect (week-1 lift against weeks 2 through 4) | Flagged | Week-1 lift was +9 points, falling to +4, +3, and +2 over weeks 2 through 4; a decay toward zero, per the design doc's own pre-commitment, so the early lift is not counted as the finding and the week-4 read above governs instead |
| Early look | Not applicable | No decision-bearing look was taken before 2026-08-31, as pre-committed; the only reads before then confirmed the `nudge_variant_assigned` event was firing |
| Metric observation-unit mismatch | Passed | The adoption metric's denominator, Recurring Analysts in each arm's accounts, stayed balanced between the arms, and neither it nor the weekly-active-analysts count changed shape during the run |
| Telemetry change mid-test | Passed | `view_saved`, `view_switched`, `view_set_default`, `view_shared`, `view_load_error`, and `nudge_variant_assigned` were unchanged for the full window |
| Interaction with other live experiments | Not applicable | No other experiment ran on the dashboard surface during this window; the design-partner pilot's own accounts were already excluded from the eligible population above |

## Deep-Dive

The design doc pre-committed to no segment beyond the account-level control and treatment split itself; the
eligible population was judged too small to slice further without turning each slice into its own
underpowered test. No segment analysis beyond that two-arm split was run here, consistent with that
pre-commitment, and the business question the decision actually turns on is answered directly by the
primary-metric table above: does the prompt move adoption enough, at this population's size, to justify
retiring the no-prompt control? It does not, at the level the platform uses.

**Estimated business impact.** N/A. The design doc fixed no revenue or cost baseline for Saved Views
adoption; the metric itself, not a dollar figure, is what the decision rule above reads against.

## Decision: Ship, Iterate or Stop

Null, per the design doc's own decision rule: no statistically significant difference between the arms at
the end of the full four weeks. Worth stating plainly, because the design doc's two commitments disagree on
this exact outcome: its hypothesis said it would fail only if treatment matched or trailed the no-prompt
control's own figure, and treatment finished two points above control, so the hypothesis, read on its own
terms, did not fail. The difference was not significant, though, and the decision rule, not the hypothesis's
own failure condition, is what governs this document's decision: a null result is shelve-and-reconsider, not
re-run-unchanged. That gap between the two commitments is recorded here as a lesson for the next design doc
to close, rather than resolved quietly in either commitment's favor.

**What this result rules out, and what it does not.** The interval's upper end, +15 points, is the largest
lift this result leaves plausible, so anything larger is ruled out, including the 18-point lift the test was
sized to detect. What it leaves open is a smaller real lift, anywhere up to that +15, which this population
was too small to resolve.

**Reversibility.** Reversible. The fifth-view prompt is a client-side flag with no stored state beyond the
`nudge_variant_assigned` event and no migration behind it; removing it costs nothing and nothing has to be
unwound. That is part of why the decision rule calls for shelving the idea rather than treating this as a
one-way door that needs a slower, more deliberative process.

## Decision Owner

Priya Nair (PM, Reporting) called the stop at the 2026-09-03 experiment review. That is the same name and
role the design doc's heading fields already carry for this test, so planning and readout stayed with one
person rather than handing off between them.

## Next Steps and Owners

| Action | Owner | Status |
|---|---|---|
| Shelve the fifth-view prompt; no re-run of this exact test | Priya Nair (PM, Reporting) | Done |
| Bring the null finding to the next Reporting Platform Modernization steering review and weigh a different mitigation for R-04 | Priya Nair (PM, Reporting) | Not started |
| Mark `nudge_variant_assigned` for retirement in the tracking plan | Lee Zhang (Data Eng) | Not started |

## Implementation Details and Analysis Notes

Cohort: every account carrying a `nudge_variant_assigned` event, joined to the entitlements database on
`account_id`. Adoption is read from `view_saved`, `view_switched`, and `view_set_default`, attributed to the
viewing account rather than the authoring one, matching the KPI dashboard's own adoption formula and its
own known limitation that a shared view counts for the viewer, not the creator. Each test week's
adoption is read on the dashboard's own trailing-7-day window, taken on that week's last day, so the readout
and the dashboard count a weekly user the same way. No account was dropped
from either arm after assignment, and no refund, downgrade, or account-merge event touched either arm during
the run.

## Further Analysis

Accounts with ten or more Recurring Analysts showed a larger raw gap between arms (treatment ahead of
control by roughly 4 points) than accounts with fewer analysts (roughly 1 point). Neither slice was
pre-registered in the design doc, and neither one changes the decision above; raised here only because it is
a plausible lead for whoever designs the next mitigation for R-04, not a finding this readout rests on. An
account-size segment pre-registered in advance would be the honest way to chase it, rather than reopening
this test's own data for a closer look.
