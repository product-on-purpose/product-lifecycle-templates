---
title: "Saved Views Adoption Nudge Experiment Design Doc"
experiment_name: "Saved Views Adoption Nudge"
owner: "Priya Nair (PM, Reporting)"
reviewers: "Dana Osei (Staff Engineer, Platform), Lee Zhang (Data Eng)"
decision_maker: "Priya Nair (PM, Reporting)"
status: "approved"
planned_start_date: "2026-08-03"
planned_duration: "4 weeks (2026-08-03 through 2026-08-31)"
last_updated: "2026-07-30"
doc_type: experiment-design-doc
size: full
source_template: experiment-design-doc
source_template_version: 0.1.0
---

> **Worked example.** A filled `experiment-design-doc`, full variant, for the Saved Views adoption-nudge
> test at Acme Analytics, chained onto the same [Saved Views for Dashboards PRD](../prd/prd_example.md),
> [KPI dashboard](../kpi-dashboard/kpi-dashboard_example.md), [OKRs](../okrs/okrs_example.md) and
> [risk register](../risk-register/risk-register_example.md) that the rest of this library's thread
> already uses. Dated 2026-07-30, four days before the test itself launches on 2026-08-03. Its second
> half, the `experiment-readout` bundle's own example, is not yet built; when it ships, it reports this
> same test against the commitments fixed below.
>
> All figures, account counts, and event names are illustrative.

# Saved Views Adoption Nudge Experiment Design Doc

## Hypothesis

If we show a one-time in-app prompt to a Recurring Analyst after their fifth dashboard view since the
2.4.0 release, suggesting they save their current filter, date range, and column setup as a view, then
weekly Saved Views adoption will rise against a no-prompt control, because analysts who have not yet
tried the feature may simply not have noticed the Views menu.
Supporting evidence: adoption sits at 41% (the KPI dashboard, last reviewed 2026-07-20), and the risk
register already carries R-04, the risk that Recurring Analysts do not
adopt Saved Views inside the program's 60-day launch-success window because they have deep habits in the
legacy report flow, with an in-product nudge named as that risk's own mitigation (risk register, same
review date). The hypothesis fails if, at the end of the four-week window, weekly adoption among
prompted accounts matches or trails the no-prompt control's own figure.

## Population, Variants, and Allocation

Eligible: accounts with at least one Recurring Analyst active in the trailing 7 days, the same segment
the KPI dashboard already counts (495 analysts as of 2026-07-20), where that analyst reaches their fifth
dashboard view on or after 2026-08-03. Excluded: the six analysts already enrolled in the Saved Views
design-partner pilot, and their accounts, so a pilot account cannot land on either side of this test and
double up the R-04 mitigation on itself. Two variants: control (current behavior, no prompt) and
treatment (the fifth-view prompt), 50/50 split.

Randomization unit: customer account, not individual analyst. FR-4, the PRD's requirement to share a
view so that "other permitted users of that dashboard can select it", means a saved view a treatment
analyst creates can become visible to a colleague on the same account, and the KPI dashboard's own
adoption panel counts a shared view for the viewer, not the creator. Randomizing at the analyst level
would let a treatment analyst's share count as adoption for a colleague assigned to control on the same
account, which breaks the assumption that one unit's assignment does not affect another's outcome. Keeping a whole account on
one side of the test, including everyone who shares its dashboards, avoids that spillover.

**The eligible population is small, and the test is sized against that, not against a bigger number we
wish we had.** Acme's entitlements database counts roughly 230 accounts behind the 495 weekly active
Recurring Analysts the KPI dashboard tracks (illustrative; this test's own effective sample, once
randomization moves from analysts to accounts, is nearer that account count than the analyst count). The
Minimum Detectable Effect section below is sized against accounts of that order, not a population this
test does not have.

## Primary and Guardrail Metrics

The primary metric is KR2, the OKRs' own Saved Views adoption key result, not the PRD's stated primary
metric (median time from dashboard open to first meaningful interaction): the nudge is built to move
adoption directly, and time-to-insight is read on the KPI dashboard's own panel instead. Weekly active
analysts and shared-view permission incidents need no new baseline beyond what the KPI dashboard and the
PRD already carry; this test adds only the adoption row's own margin, sized in the next section.

| Metric | Type (primary or guardrail) | Baseline | Target or guardrail margin |
|---|---|---|---|
| Saved Views adoption (share of Recurring Analysts using a saved view weekly) | primary | 41% (KPI dashboard, last reviewed 2026-07-20) | A statistically significant lift over control by 2026-08-31; the test is sized to detect a lift of about 18 points (this test's own MDE, see below; not KR2's full-quarter target of 60%) |
| Weekly active analysts | guardrail | 495 (KPI dashboard, same review date) | Must not fall below 480, the dashboard's own guardrail floor, at any point during the test |
| Dashboard load error rate | guardrail | No new baseline; the PRD's own guardrail already covers this | Must not rise above its pre-test level |
| Shared-view permission incidents | guardrail | None recorded; the PRD's own guardrail requires zero | Must stay at zero |

## Minimum Detectable Effect and Sample Size or Duration

Statistical approach: a fixed-horizon test at the experimentation platform's standard setting, 80% power
and a 5% significance level (illustrative); this test does not pick its own level. MDE: about 18
percentage points of weekly adoption share, treatment against control. The arithmetic uses Evan Miller's
rule of thumb, n = 16 σ²/δ² per arm, where σ² for a proportion is p(1 - p). At the 41% baseline, σ² is
0.41 x 0.59, about 0.24. With about 115 accounts per arm, δ is the square root of 16 x 0.24 / 115, about
0.18. Counting analysts instead of accounts would give about 12.5 points, but that overstates what the
test can resolve, because analysts on one account share its assignment. An 18-point MDE is a large ask
next to KR2's own 19-point, full-quarter target (41% to 60%). It is large because the population is
small: this test can detect a big effect and nothing subtler. Sample: every eligible
account, roughly 230 (illustrative); there is no larger population to draw a smaller sample from, so the
"sample size" this test commits to is the whole eligible population, not a number a calculator trims down
to. Duration: four weeks, 2026-08-03 through 2026-08-31, chosen on its own grounds: long enough for an
account to cross its fifth dashboard view and then be observed across several weekly adoption windows,
not derived from the account count the way a duration would be on a higher-traffic surface.

The team will not review adoption numbers before 2026-08-31 except to confirm the prompt is firing (see
the Tracking and Instrumentation Note below); any look taken before then is informational only and
changes no decision. If the true effect on adoption is well below 18 points, this test will most likely
return a null result rather than a confirmed loss, and the Decision Rule below, not a second look at the
same data, is what happens next.

## Decision Rule

Win (treatment's adoption share finishes the four weeks above control by a statistically significant
margin at the platform's standard setting, with no guardrail breach): roll the fifth-view prompt out to
100% of Recurring Analysts' accounts and retire the control. Null (no significant difference at the end of
the full four weeks): this makes a lift of about 18 points or more unlikely, and says nothing about a
smaller real lift, which may still exist. Shelve the fifth-view prompt rather than rerunning it unchanged, because the same population
cannot resolve a smaller effect the second time either. Bring the null finding to the next Reporting
Platform Modernization steering review and weigh a different mitigation for R-04 against its cost.
Guardrail breach (weekly active analysts fall below 480, the dashboard load error rate rises above its
pre-test level, or a shared-view permission incident occurs on either arm): stop the test for every
account immediately, regardless of the adoption reading, and send any permission incident to Dana Osei,
who owns the permissions service. Decision-maker: Priya Nair, PM for Reporting, the same name as the
frontmatter above.

## Tracking and Instrumentation Note

Weekly adoption and the guardrails read from the existing `view_saved`, `view_switched`,
`view_set_default`, `view_shared`, and `view_load_error` events; none of them change for this test. New
exposure event: `nudge_variant_assigned`, firing the moment an eligible account crosses its fifth
dashboard view, carrying the variant id and the account id as properties. Checked in the staging
environment on 2026-07-29: each arm fired as expected, and the control side emits no visible prompt, so
the adoption panel can still attribute control accounts to the right side of the test.

## Validity Pre-Commitments

| Check | Threshold or trigger | Owner |
|---|---|---|
| Sample ratio mismatch | Run the platform's chi-squared sample-ratio check on assigned account counts every day; if it flags the split as off 50/50, nobody reads the result until the cause is found | Lee Zhang, Data Eng |
| Weekly active analysts guardrail | Stop the test early if the count falls below 480 on any day | Priya Nair |
| Dashboard load error rate and permission incidents | Stop the test early if the error rate rises above its pre-test level, or a single shared-view permission incident occurs on either arm | Dana Osei, Platform |
| Ramp-up | N/A. A 50/50 split across the full eligible account population is already as large as this test gets before the next steering review; there is no larger traffic tier to ramp into first. | N/A |
| Novelty effect | Compare week-1 adoption lift against weeks 2 through 4; a lift that decays toward zero by week 4 is flagged as novelty rather than counted as the finding | Priya Nair |
| Segments fixed in advance | None beyond the account-level control and treatment split; the eligible population is too small to slice further without turning each slice into its own underpowered test | N/A |

**Overlap with concurrent experiments.** No other experiment runs on the dashboard surface during this
window. The design-partner pilot already excludes its own six analysts and their accounts from the
eligible population above, so there is no overlap between the two to design around.

**Risks, and who else must be told.** The Reporting Platform Modernization steering group already watches
R-04 and the KPI dashboard's adoption panel, so this test adds no new escalation line to them. Support is
told before launch: a prompt appearing mid-session is the kind of change that generates a ticket if
nobody warns the team that answers it, and Marta Reyes, the program manager, owns that notification
before 2026-08-03.
