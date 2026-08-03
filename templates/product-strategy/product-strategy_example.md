---
title: "Acme Analytics Product Strategy FY26"
product: "Acme Analytics"
owner: "Dana Okoro, VP Product"
period: "FY26 (February 2026 to January 2027)"
status: "agreed"
last_updated: "2026-01-28"
doc_type: product-strategy
size: full
format: kernel
source_template: product-strategy
source_template_version: 0.1.0
---

> **Worked example.** A filled `product-strategy`, full variant, kernel format, for the same Acme Analytics
> product used by the `product-vision`, `prd`, `test-plan`, `test-case` and `bug-report` examples. **It sits
> between two of them:** it is the strategy for the [product vision](../product-vision/product-vision_example.md)
> agreed two weeks earlier, and it is the document under which the
> [Saved Views PRD](../prd/prd_example.md) was written. The FY26 "Time to Insight" company goal that the PRD
> and the `kpi-dashboard` example both cite appears below as the objective this strategy serves.
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company.

# Acme Analytics Product Strategy FY26

## Diagnosis

Acme can answer almost any question an unaccompanied analyst has, but only if they already know how to ask it. Every
self-serve path we have shipped begins at the schema: pick a dataset, pick a join, pick a measure. Our own
telemetry says that is where new users stop: **only 31 percent of new accounts build a second view within
14 days**, and session recordings put the drop
at the dataset picker rather than at sign-up or at sharing. Of the accounts that stall there, two thirds
never return to authoring at all.

The consequence is that our growth depends on a resource we cannot ship: expertise. Accounts that succeed
either arrive with a data analyst or buy our services team's time. Both convert well and neither scales,
which is why revenue per new account has been flat for five quarters while sign-ups have grown 40 percent.

**The obstacle is not acquisition, and it is not feature coverage. It is that the product requires knowledge
the user does not have, and we have been treating that as a documentation problem.**

## Target Segments, and Non-Targets

**Target: the unaccompanied analyst.** Someone at a 50-500 person company who owns a number, answers
questions about it weekly, and has no data team behind them. This strategy names them by what they lack;
downstream delivery documents should call the same person the **Recurring Analyst**, by behaviour, and one
name per person is the point. They are 61 percent of new accounts and 22 percent of revenue, and the gap between those two numbers is this strategy's whole subject.

**Non-target this period: enterprise data-platform teams.** They buy on governance, lineage and modelling
depth. We win some of these deals and they are profitable. They are still out of scope for FY26, because
every one of them pulls product and services capacity toward the expertise-heavy product we are trying to
stop being. Sales leadership has agreed to hold the two enterprise RFPs currently open and not to source
more this year.

**Also non-target: the embedded-analytics OEM channel.** Two deals last year, both delivered by the services
team, both requiring a different product than the one above.

## Guiding Policy

**We will make the product usable without data expertise, rather than making expertise easier to acquire.**
Where we face a choice between teaching the user what they need to know and removing the need to know it, we
remove the need.

This rules out the approach we took for the last two years, and which is still the most popular internal
proposal: better documentation, in-product tutorials, a certification programme, and a larger services
practice. Those make expertise cheaper to acquire. They do not remove it from the path, and the drop-off
happens before anyone reads anything.

## Coherent Action

1. **Question-first entry.** The first interaction with a dashboard or a dataset is a question in the user's
   own words, not a schema. The system proposes the dataset and the joins; the user corrects rather than
   constructs.
2. **Ship our modelling work as defaults.** The semantic modelling our services team currently does per
   account becomes shipped, per-vertical defaults, so a new account has useful views on day one instead of a
   blank canvas.
3. **Instrument the second view.** The moment a user builds their second view is our leading indicator.
   Every team sees the same number, on the same dashboard, weekly.
4. **Move services capacity from custom modelling to defaults.** The same people, the same skill, applied
   once per vertical instead of once per account.

All four serve the vision's claim that Acme belongs **inside the operational context where the question
occurred** rather than being a destination people travel to. Question-first entry is that claim made
concrete: the question arrives where the work is, not after a modelling step.

Actions 1 and 2 reinforce each other directly: question-first entry is only credible if there is a modelled
default underneath it to answer against, and defaults are only discoverable if the user does not have to
name them. Action 4 is what pays for action 2. Action 3 is what tells us whether the diagnosis was right,
which is why it ships first.

## What We Are Not Doing

1. **We are not building a mobile authoring experience this year.** Mobile is 4 percent of authoring
   sessions and it competes for exactly the design capacity question-first entry needs. Consumption on
   mobile continues to work and is not being removed. *(Requested repeatedly by two of our largest accounts;
   both have been told.)*
2. **We are not pursuing enterprise data-governance RFPs.** Winnable and profitable, and they pull us toward
   the product this strategy exists to move away from.
3. **We are not shipping the certification programme.** It was funded in the FY25 plan and is the clearest
   example of making expertise cheaper rather than unnecessary. The team of two moves to defaults.
4. **We are not adding new connectors this year** beyond the four already committed. Connector count is the
   metric our competitors compete on; it is not where our users stop.

## How We Will Know It Is Working

**Leading indicator:** share of new accounts that build a second view within 14 days. Baseline 31 percent
(Q4 FY25), target **50 percent by the end of Q3 FY26**.

**Lagging:** self-serve net revenue retention, and the FY26 "Time to Insight" company goal, which the PRD
states as the median time
from opening a report to **acting on it** and the KPI dashboard operationalises as a logged action. Those
are deliberate narrowings of the same goal, not three different goals; this strategy is its product half.

**The falsifier, stated in advance:** if the second-view rate has not moved by the end of Q3, we treat the
diagnosis as wrong rather than the execution as insufficient. The alternative diagnosis we would test next is
that the drop-off is about trust in the numbers, not about how they are constructed.

## Assumptions and Risks

| Assumption | Evidence we have | Evidence we lack | Test |
|---|---|---|---|
| Analysts stop at the schema because they lack context, not intent | 9 of 14 session recordings show a return to documentation before abandoning | We have not spoken to anyone who abandoned and never returned | 12 interviews with lapsed trials, by 20 March |
| A question-first entry point can be accurate enough to be trusted | Prototype resolved 71 percent of test questions to the right dataset | No production data; no measure of what happens after a wrong answer | Ship to 5 percent of new accounts in Q2, measure correction rate |
| Per-vertical defaults generalise | Services team reports 4 of 6 recent implementations were near-identical | The other 2 were not, and we do not know why | Build defaults for the 2 largest verticals first and measure fill rate |
| Holding enterprise does not break the number | Enterprise is 31 percent of revenue and under contract through FY26 | We do not know the renewal impact of two years of no governance investment | Reviewed at the Q3 renewal cycle, with the CRO |

**The assumption this strategy would die without is the first one.** If analysts abandon because they do not
trust the data rather than because they cannot construct the query, every action above is aimed at the wrong
obstacle.

## Review Trigger

Reviewed when **any** of these happens, and on **15 October 2026** regardless:

- the second-view rate moves 8 points in either direction;
- the lapsed-trial interviews contradict the first assumption;
- a target-segment win rate drops in two consecutive quarters;
- the services team reports that per-vertical defaults are not generalising.

**Owner: Dana Okoro, VP Product.** A competitor announcement is explicitly *not* a trigger. If we rewrite
this document every time someone else ships something, we will have a series of reactions rather than a
strategy.
