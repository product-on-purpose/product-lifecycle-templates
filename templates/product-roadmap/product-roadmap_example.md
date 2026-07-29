---
title: "Acme Analytics Product Roadmap FY26"
product: "Acme Analytics"
owner: "Dana Okoro, VP Product"
horizon: "FY26 (February 2026 to January 2027)"
audience: "internal (a stripped external version is published separately)"
status: "agreed"
last_updated: "2026-02-11"
doc_type: product-roadmap
size: full
format: now-next-later
source_template: product-roadmap
source_template_version: 0.1.0
---

> **Worked example.** A filled `product-roadmap`, full variant, now-next-later format, for the same Acme
> Analytics product used by the `product-vision`, `product-strategy`, `prd`, `test-plan`, `test-case` and
> `bug-report` examples. **It sits between two of them:** it implements the
> [FY26 product strategy](../product-strategy/product-strategy_example.md) agreed two weeks earlier, and its
> Now lane contains the work the [Saved Views PRD](../prd/prd_example.md) specifies.
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company.

# Acme Analytics Product Roadmap FY26

## The Outcome This Serves

Implements the [FY26 product strategy](../product-strategy/product-strategy_example.md), whose diagnosis is
that Acme requires expertise the unaccompanied analyst does not have, and whose guiding policy is to remove
the need for that expertise rather than make it cheaper to acquire.

**The measure everything below ladders to:** the share of new accounts that build a second view within 14
days, from a 31 percent baseline to 50 percent by the end of Q3 FY26. If an item on this roadmap cannot be
connected to that number, it does not belong here, and two items were removed during review for exactly that
reason.

## Now

**1. Question-first entry, first cohort.** New accounts start from a question in their own words rather than
a dataset picker. Shipping to 5 percent of new accounts from March, measuring how often the proposed dataset
is the one the user keeps.

**2. Saved Views.** Analysts who have built a useful view cannot return to it without rebuilding the filter
state, which is the second-view problem in its most literal form. Specified in the
[Saved Views PRD](../prd/prd_example.md); in build.

**3. Second-view instrumentation.** The leading indicator itself. Every team sees the same number on the same
dashboard weekly. Shipped first, deliberately, because the rest of this roadmap is unfalsifiable without it.

## Next

**4. Per-vertical modelling defaults.** A new account should have useful views on day one instead of a blank
canvas. Shaped once the services team has finished the two largest verticals, which is also what frees their
capacity. Expected to change: we do not yet know whether defaults generalise beyond those two.

**5. Override transparency for question-first entry.** When the system proposes the wrong dataset, we
currently learn nothing. Waiting on enough cohort data to know whether this is a real problem or a rare one.

## Later

**6. Collaborative analysis.** Analysts who answer a question are asked the same question again by someone
else. Unshaped; we do not know whether this is a product or a process.

**7. Scheduled delivery of saved views.** Direction only. Adjacent to Saved Views and frequently requested,
but no work has been done to size it.

## What Is Not On Here

**1. Mobile authoring.** Mobile is 4 percent of authoring sessions and competes for exactly the design
capacity question-first entry needs. Consumption on mobile keeps working. *Requested repeatedly by two of our
largest accounts; both have been told directly by their account teams.*

**2. The certification programme.** Funded in the FY25 plan and cancelled by this strategy, because it makes
expertise cheaper to acquire rather than unnecessary. The team of two moved to defaults.

**3. New connectors beyond the four already committed.** Connector count is where our competitors compete; it
is not where our users stop.

**4. Enterprise data-governance features.** Out of scope for FY26 per the strategy's non-target segment
decision. *Two open RFPs were declined; the CRO agreed the hold.*

## Confidence, and How It Decays

**Now** is committed capacity and we expect all three items to complete this half. Saved Views has a
specification and a test plan; the other two are shaped.

**Next** is directional. Historically about half of what sits in this lane changes shape before it starts,
and item 4 depends on a generalisation we have not yet demonstrated.

**Later** is a statement of interest only. We have moved more items out of Later than into Next, and nobody
should plan around it. If you are building a budget from this document, use Now.

## Dependencies and What Could Move It

| Dependency | Whose | What it would move |
|---|---|---|
| Labelled corpus of past sessions for question-first entry | Support team, competing with tier-1 ticket load | If it slips past March, item 5 moves ahead of item 4, because it does not need the corpus |
| Services capacity freed from custom modelling | Services, gated on the FY26 hold on enterprise RFPs | If the hold breaks, item 4 slips a quarter and the second-view target moves with it |
| Saved Views regression suite | QA, in progress, tracked on the [test plan](../test-plan/test-plan_example.md) | Slippage delays the Saved Views release but reorders nothing |

## Review Trigger

Reviewed when **any** of these happens, and on **15 October 2026** regardless:

- the second-view rate moves 8 points in either direction;
- the parent strategy changes, or its first assumption is contradicted by the lapsed-trial interviews;
- a Now item is invalidated by what we learn rather than delayed.

**Owner: Dana Okoro, VP Product.** A competitor announcement is explicitly **not** a trigger.

**Audience note.** This is the internal roadmap. The published version at acme.example/roadmap carries the
Now lane only, describes it in problem terms with no dates, and omits sections 3, 4 and this one entirely.
