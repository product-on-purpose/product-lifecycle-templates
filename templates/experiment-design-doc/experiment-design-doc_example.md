---
title: "Saved Views Adoption Nudge Experiment Design Doc"
experiment_name: "Saved Views Adoption Nudge"
owner: "Priya Nair (PM, Reporting)"
reviewers: "Dana Osei (Engineering), Lee Zhang (Data Eng)"
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
weekly Saved Views adoption will rise against a no-prompt control, because most analysts who have not
yet tried the feature have simply not noticed that the Views control already sits above the filter bar.
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

Randomization unit: customer account, not individual analyst. FR-4, the PRD's requirement to let an
analyst share a view with a teammate or team, means a saved view a treatment analyst creates can become
visible to a colleague on the same account, and the KPI dashboard's own adoption panel already counts a
shared view for the viewer as well as its creator. Randomizing at the analyst level would let a treatment
analyst's share leak adoption into a colleague assigned to control on the same account, which breaks the
assumption that one account's assignment does not affect another's outcome. Keeping a whole account on
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
| Saved Views adoption (share of Recurring Analysts using a saved view weekly) | primary | 41% (KPI dashboard, last reviewed 2026-07-20) | At least 10 points above control by 2026-08-31 (this test's own MDE; see below, not KR2's full-quarter target of 60%) |
| Weekly active analysts | guardrail | 495 (KPI dashboard, same review date) | Must not fall below 480, the dashboard's own guardrail floor, at any point during the test |
| Dashboard load error rate | guardrail | No new baseline; the PRD's own guardrail already covers this | Must not rise above its pre-test level |
| Shared-view permission incidents | guardrail | None recorded; the PRD's own guardrail requires zero | Must stay at zero |

## Minimum Detectable Effect and Sample Size or Duration

MDE: 10 percentage points of weekly adoption share, treatment against control (illustrative). That is a
large ask next to KR2's own 19-point, full-quarter target (41% to 60%), and it is large on purpose: at
roughly 230 eligible accounts split 50/50, a four-week test cannot reliably resolve a smaller swing than
this. Statistical approach: a fixed-horizon test, at whatever power and significance the experimentation
platform's own standard setting uses; this test does not pick its own level. Sample: every eligible
account, roughly 230 (illustrative); there is no larger population to draw a smaller sample from, so the
"sample size" this test commits to is the whole eligible population, not a number a calculator trims down
to. Duration: four weeks, 2026-08-03 through 2026-08-31, chosen on its own grounds: long enough for an
account to cross its fifth dashboard view and then be observed across several weekly adoption windows,
not derived from the account count the way a duration would be on a higher-traffic surface.

The team will not review adoption numbers before 2026-08-31 except to confirm the prompt is firing (see
the Tracking and Instrumentation Note below); any look taken before then is informational only and
changes no decision. If the true effect on adoption is smaller than 10 points, this test returns a null
result rather than a confirmed loss, and the Decision Rule below, not a second look at the same data, is
what happens next.

## Decision Rule

Win (treatment's adoption share finishes the four weeks at least 10 points above control, with no
guardrail breach): roll the fifth-view prompt out to 100% of Recurring Analysts' accounts and retire the
control. Null (no detectable difference at the end of the full four weeks, the test having run at its
stated power): treat the fifth-view prompt as answered and shelve it rather than repeating it unchanged;
bring the null finding to the next Reporting Platform Modernization steering review and weigh a
different mitigation for R-04 against its cost, since a 10-point effect was already the edge of what this
population can detect. Guardrail breach (weekly active
analysts fall below 480, the dashboard load error rate rises above its pre-test level, or a shared-view
permission incident occurs on either arm): stop the test for every account immediately, regardless of the
adoption reading, and route any permission incident through the security review path the PRD already
names for shared views. Decision-maker: Priya Nair, PM for Reporting, the same name as the frontmatter
above.

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
| Sample ratio mismatch | Treat the split as mismatched once the account ratio departs from 50/50 by more than 5 points across 3 straight days (a wider band than a higher-traffic test would allow, since 230 accounts moves less per day) | Lee Zhang, Data Eng |
| Weekly active analysts guardrail | Stop the test early if the count falls below 480 on any day | Priya Nair |
| Dashboard load error rate and permission incidents | Stop the test early if the error rate rises above its pre-test level, or a single shared-view permission incident occurs on either arm | Dana Osei, Engineering |
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
