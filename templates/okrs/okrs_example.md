---
title: "Acme Analytics OKRs, FY26 Q3"
owner: "Dana Okoro, VP Product"
period: "FY26 Q3 (August to October 2026)"
parent: "FY26 product strategy, and the FY26 Time to Insight company goal"
audience: "internal, shared with the whole product and data organisation"
status: "agreed"
last_updated: "2026-07-27"
doc_type: okrs
size: full
source_template: okrs
source_template_version: 0.1.0
---

> **Worked example.** A filled `okrs`, full variant, for the same Acme Analytics product used by the
> `product-vision`, `product-strategy`, `product-roadmap`, `prd`, `test-plan`, `test-case` and `bug-report`
> examples. **This is where the library's direction layer and its measurement layer meet:** the Objective is
> the FY26 "Time to Insight" company goal that the [PRD](../prd/prd_example.md) cites as its parent, and every
> number below is read off the [KPI dashboard](../kpi-dashboard/kpi-dashboard_example.md) that already tracks
> it.
>
> **Read the dates.** This set was agreed on 27 July 2026, before Q3 opens in August. Everything it
> references already existed: the strategy (January), the roadmap (February), the Saved Views PRD (June) and
> its test plan (July). An OKR set is the one document in this family that can legitimately cite all of its
> siblings, because it is the last one written.
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company.

# Acme Analytics OKRs, FY26 Q3

## The Period and What This Serves

Covers **FY26 Q3, August to October 2026**. Serves the
[FY26 product strategy](../product-strategy/product-strategy_example.md), specifically its guiding policy of
removing the need for analyst expertise rather than making it cheaper to acquire, and the FY26 **"Time to
Insight"** company goal that the strategy names as one of its two lagging indicators.

This is the cycle in which that goal either lands or does not. It was set at a 30 percent reduction by Q3 and
sits at 18 percent, which the dashboard reads as amber and improving. The
[product roadmap](../product-roadmap/product-roadmap_example.md)'s Now lane is the work behind it.

## Objective

**Analysts act on what they see, on the day they see it.**

## Key Results

| # | Key Result (a measurable outcome) | Baseline today | Target by end of period | Owner | Committed or aspirational |
|---|---|---|---|---|---|
| 1 | Time to Insight: median minutes from opening a report to the first logged action on it | -18% against the FY26 baseline | -30% against the FY26 baseline | Priya Nair | committed |
| 2 | Share of Recurring Analysts using a saved view weekly | 41% | 60% | Priya Nair | committed |
| 3 | Share of new accounts that build a second view within 14 days | 31% | 50% | Dana Okoro | aspirational |

**On the numbers.** Every definition and target here is lifted from an artifact that already exists, so
nobody has to reconcile two versions of the same measure. KR1 is the Time to Insight panel on the
[KPI dashboard](../kpi-dashboard/kpi-dashboard_example.md), refreshed daily from the product analytics event
stream at roughly six hours of latency. KR2 is that dashboard's Saved Views adoption panel, which refreshes
nightly from the entitlements database and the same event stream at roughly twelve hours, and its 60 percent
target is the dashboard's own. KR3 is the [roadmap](../product-roadmap/product-roadmap_example.md)'s outcome
measure rather than a dashboard panel, which is why its cadence is the roadmap's review rather than a nightly
job.

**On the owner concentration.** Priya Nair owns two of the three. That is a real risk and it is recorded
rather than hidden: if the reporting team's capacity moves, two thirds of this set moves with it.

## What This Set Is Not Committing To

**1. Enterprise data-governance features.** Out of scope for FY26 per the strategy's non-target segment
decision. Two enterprise RFPs remain open and on hold, agreed with sales leadership; the CRO reviews the hold
at the Q3 renewal cycle. If that hold breaks mid-quarter, KR3 is the first thing to move.

**2. Mobile authoring.** Four percent of authoring sessions, and it competes for exactly the design capacity
question-first entry needs. Consumption on mobile keeps working. Two of our largest accounts have asked
repeatedly and have been told directly by their account teams.

**3. A Time to Insight improvement bought by changing the metric.** The definition is fixed for this cycle:
median minutes from report open to first logged action, as specified on the dashboard. If we decide the
definition is wrong, that is a separate conversation with the steering group, and it does not happen inside
a quarter we are being measured on.

**4. Per-vertical modelling defaults.** On the roadmap's Next lane, deliberately not here. It rests on a
generalisation across verticals that nobody has demonstrated, so committing to a number for it this quarter
would be inventing one.

## Initiatives

| Initiative | Serves | Owner | Status |
|---|---|---|---|
| Take Saved Views from the in-review specification to general availability | KR2 | Priya Nair | in build, spec at 0.3.0 |
| Reduce the report-open to first-action path from four steps to two for the ten most-opened report types | KR1 | Lee Zhang | starting week 1 of Q3 |
| Run the question-first entry cohort to 5 percent of new accounts and read the correction rate | KR3 | Dana Okoro | cohort live, first read due mid-September |

**KR1 is served by one initiative and that is a known weakness.** If the step-count work turns out not to be
the constraint on Time to Insight, we have no second lever this quarter and the Key Result will miss. The
alternative lever, per-vertical defaults, is explicitly excluded above. This was argued and accepted rather
than overlooked.

## Confidence and Check-in

These are opening forecasts, set the day the cycle was agreed and not yet tested by a single check-in. The
Monday stand-up carries them from week one of August, and any figure still sitting where it started after a
month gets argued about rather than copied forward.

- **KR1 opens at 3 of 10, the lowest number on this page.** Time to Insight has been flat since May and we
  are betting on a single hypothesis about why. If reducing the step count turns out not to be what is
  slowing analysts down, there is no second lever available inside this quarter.
- **KR2 opens at 8 of 10.** Saved Views has a written specification, a test plan and a regression suite
  behind it. What can go wrong here is the calendar, not the feature.
- **KR3 opens at 5 of 10.** The cohort is running and the correction rate is readable, but 31 to 50 percent
  inside one quarter is a large ask, which is precisely why it carries the aspirational label.

## Scoring and Close-out

Close-out lands in the first product review of November. Whoever holds a Key Result reads its final number
aloud and puts a grade beside it on the 0.0 to 1.0 scale the dashboard already uses, so the measurement and
the grade come from one place rather than two. Committed Key Results are expected to arrive at 1.0, and
anything short of that owes a sentence explaining the gap; the aspirational one is expected nearer 0.7, where
a low grade is a finding and not a miss.

**Grades from this cycle reach no performance review and no compensation decision, and everyone on the team
has that from their manager in writing.** It is spelled out because an unanswered version of this question
answers itself, and the answer people assume is the one that makes them write an easier set next time.

Anything closing red is written up as what we learned, and none of it becomes a remediation plan. KR1 is the
likeliest to land there. If it does, the write-up owes exactly one answer: was the step-count hypothesis
wrong, or was it right and simply not enough on its own?
