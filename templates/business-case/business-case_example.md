---
title: "Question-First Entry and Modelling Defaults Business Case"
investment_name: "Question-First Entry and Modelling Defaults"
sponsor: "Dana Okoro, VP Product"
stage: "N/A - Acme has no staged case model (no SOC/OBC/FBC); a single sponsor-approval gate applies"
status: "pending decision"
last_updated: "2026-01-20"
financial_model_ref: "FY26 Planning workbook, Reporting tab (internal, not attached)"
doc_type: business-case
size: full
source_template: business-case
source_template_version: 0.1.0
---

> **Worked example.** A filled `business-case`, full variant, for Acme Analytics, the same product used
> throughout this library's examples. Per the discovery-docs family contract, this document sits near the
> **start** of the shared timeline, ahead of everything except its sibling
> [user persona](../user-persona/user-persona_example.md) and the product vision it builds on: it is dated
> 2026-01-20, six days before the leadership review it asks for and eight days before the
> [FY26 product strategy](../product-strategy/product-strategy_example.md) whose Guiding Policy and Coherent
> Action sections spend the investment argued for below. Nothing in the body cites the strategy, the
> [roadmap](../product-roadmap/product-roadmap_example.md), or any later document, because none of them
> existed yet when this was written; it cites only the
> [product vision](../product-vision/product-vision_example.md), agreed six days earlier, and Acme's own
> telemetry.
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company.

# Question-First Entry and Modelling Defaults Business Case

## Problem and Opportunity

Acme's own product telemetry shows exactly where new accounts stop: only 31 percent build a second dashboard
view within 14 days of signup, and session recordings put the drop at the dataset picker, the step where a
user already has to know which table, which join, and which measure answers their question, rather than at
sign-up or at sharing. Two-thirds of the accounts that stall there never return to authoring at all.

The consequence shows up in revenue, not only in usage. Accounts that do get past that step arrive either
with their own data analyst or by buying time from our services team; both convert well and neither scales,
and revenue per new account has been flat for five quarters while sign-ups have grown 40 percent over the
same period. The product requires knowledge a growing share of our new accounts does not have, and every
plan on the table for the last two years has tried to make that knowledge cheaper to acquire rather than
asking whether the product could do without it.

This matters now because the segment that stalls, an account owner who tracks a number weekly with no data
team behind them, is also the fastest-growing part of the signup base, so the flat-revenue trend gets worse
on its current trajectory rather than better. The
[product vision agreed on 2026-01-14](../product-vision/product-vision_example.md) commits Acme to a world
where that same person gets an answer in the time it takes to ask; this case is the first specific
investment decision that commitment requires. It is being brought forward now, ahead of the FY26 planning
cycle's usual schedule, because the flat revenue-per-account trend surfaced at the December leadership
review and finance asked for a funding decision rather than waiting for that cycle to reach it on its own.

## Options Considered

| ID | Option | What it would involve | Why accepted, carried forward, or rejected | Status |
|---|---|---|---|---|
| OPT-1 | Do nothing | Continue the current onboarding flow, documentation, and services investment at present levels | Telemetry shows five quarters of flat revenue per new account under this exact approach; nothing about the current trajectory reverses it on its own, and the fastest-growing signup segment is the one it fails | Rejected |
| OPT-2 | Expand documentation, in-product tutorials, a certification programme, and services capacity | Grow the services team, build a certification track, and add to tutorials and reference documentation so an account can acquire the missing expertise faster | Makes the expertise cheaper to acquire, not unnecessary; telemetry and session recordings show the drop-off happens at the dataset picker, before an account has engaged documentation, a tutorial, or a services contact at all. It is also the approach we have been running for two years without moving the revenue-per-account number | Rejected |
| OPT-3 | Build a natural-language, question-first entry point backed by per-vertical modelling defaults for the two largest verticals, funded in part by moving services capacity from custom per-account modelling to shipping those defaults | Replace the dataset picker with a question asked in the user's own words, which the system resolves to a proposed dataset and joins for the user to correct; back it with modelling work the services team already does per account, shipped instead as defaults so a new account has useful views on day one. An early internal prototype resolved 71 percent of held-out test questions to the right dataset, before any production traffic, which is signal enough to fund a build rather than another quarter of internal debate | Carried forward |

## Costs

| Category | Base estimate | Optimism-bias adjustment (and basis) | Adjusted estimate |
|---|---|---|---|
| Engineering build (question-first entry model, plus per-vertical defaults for the top two verticals) | $420,000 (14 engineer-weeks across two pods, loaded rate) | +20% (the two most recent cross-team model-integration efforts in this codebase both landed 18-24% over their initial estimate) | $504,000 |
| Ongoing run (inference hosting, monitoring, on-call) | $60,000/year | +15% (a newly added infrastructure category with no run-rate history behind the estimate) | $69,000/year |
| Services transition (backfill and training as two services engineers move from custom modelling to defaults) | $40,000 one-time | +10% (the last services reorg ran modestly, not dramatically, over its transition budget) | $44,000 |

## Benefits

| Benefit | Type (tangible / intangible) | Estimated range (and basis) | Measurement method |
|---|---|---|---|
| Second-view rate lift | Tangible | 6-11 percentage point increase in new accounts building a second view within 14 days, from the 31 percent baseline, based on the early prototype's 71 percent question-resolution rate against held-out test questions, not yet against production traffic | The existing second-view usage event, compared against the pre-launch cohort baseline, tracked monthly |
| Services capacity freed | Tangible | 1.5-2.5 FTE of custom-modelling time redeployed to shipped defaults within two quarters of the first vertical shipping | Services time-tracking system, quarterly, custom-modelling hours against the pre-transition baseline |
| Revenue-per-account movement | Intangible | Cannot be measured directly against this year's accounting close, so it is stated as a switching value instead: revenue per new account would need to move by roughly 8 percent for this line alone to clear zero. Management judges 8 percent plausible, since accounts that already have analyst support convert at a materially higher rate today | Compared against actual revenue-per-account 90 days after the first vertical default ships, per the post-go-live check below |

## Risks

| ID | Risk to the case | Mechanism (optimism bias / strategic misrepresentation / other) | Owner | Trigger to revisit the case |
|---|---|---|---|---|
| R-1 | The 14 engineer-week estimate depends on training against existing session transcripts. Legal's FY26 data-processing review has not yet cleared that use, and without clearance the team falls back to synthetic prompts, which this estimate does not price in | Optimism bias: an assumption nobody has checked yet, not a deliberate lowball | Lee Zhang (Data Eng) | The case reopens if the data-processing review still has not cleared consent once engineering capacity would otherwise be allocated |
| R-2 | Per-vertical defaults assume enough shared structure across verticals for most of the modelling work to be reusable. Services reports 4 of 6 recent account implementations were near-identical, but the other 2 were not, and the reason is not yet understood | Optimism bias: an assumption nobody has checked yet, not a deliberate lowball | Priya Nair | The case reopens if the second vertical's default fill rate lands materially below the first |
| R-3 | The revenue-per-account benefit rests on an 8 percent switching value that nobody has tested against a live cohort | Other: an untested estimation assumption, distinct from an optimism-biased cost or schedule figure | Dana Okoro | The case reopens if actual revenue-per-account movement in the first cohort differs from the stated switching value by more than 3 points in either direction |
| R-4 | This case was requested after the flat revenue-per-account trend surfaced at the December leadership review, which creates pressure for the comparison below to read as justification for a decision already favoured rather than as an independent one | Other: a decision-based-evidence-making risk to the case, distinct from optimism bias or strategic misrepresentation | Dana Okoro | The sponsor recuses from scoring Options Considered; Finance re-checks the comparison independently before the 2026-01-26 review |

## Financials

Acme's finance team applies a 12 percent hurdle rate to product-engineering investments of this size, set
annually by finance and used here without adjustment. No separate real-options premium is added, since the
recommendation below does not turn on the value of staging the build in a particular order.

| Metric | Value | Caveat |
|---|---|---|
| NPV | $410,000 over 3 years at a 12% discount rate | States whether the investment clears the hurdle in today's dollars; it says nothing about how quickly the return arrives, read it with payback below |
| IRR | 34% (3-year horizon) | Signals a rate of return, not a deal size; comparable in shape only to other investments of similar scale, not to a larger commitment carrying a structurally lower IRR |
| Payback | 14 months from the first vertical default shipping | Ignores cash flows after month 14 and does not discount for the time value of money; treat it as a liquidity check, not a profitability measure |
| ROI | 145% over 3 years, undiscounted | Says nothing about when the return arrives inside those 3 years; read alongside NPV and payback, not in place of them |

None of the four metrics above decides this case alone. The qualitative comparison in Options Considered and
the switching-value judgment in Benefits carry equal weight in the recommendation that follows.

## Recommendation

- Recommended option: OPT-3, the question-first entry point and per-vertical modelling defaults, funded in
  part by moving services capacity from custom modelling to defaults.
- Why: it is the only option that removes the knowledge requirement rather than making it cheaper to meet,
  which is exactly where OPT-2 has already failed to move the revenue-per-account number for two years. It
  reuses the services team's existing modelling skill instead of adding headcount, clears the 12 percent
  hurdle on both NPV and IRR before the revenue-per-account switching value is even counted, and the early
  prototype's 71 percent question-resolution result is strong enough to fund a build rather than spend
  another quarter debating it, while R-1 and R-2 above name precisely what would change that judgment.
- Decision requested: funding approval for the two-pod engineering allocation and the services capacity
  reallocation, at the 2026-01-26 leadership planning review.
- Post-go-live check: Dana Okoro (sponsor) measures the second-view rate and revenue-per-account movement 90
  days after the first vertical default ships, compares the result to the targets stated above, and reports
  the outcome at the same forum that approved the case.
