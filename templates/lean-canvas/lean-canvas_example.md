---
title: "Acme Embedded Analytics Lean Canvas"
product: "Acme Embedded Analytics (exploratory, inside Acme)"
owner: "Noor Siddiqui, Product Lead"
status: "draft"
last_updated: "2026-01-21"
doc_type: lean-canvas
size: lean
source_template: lean-canvas
source_template_version: 0.1.0
---

> **Worked example.** A filled `lean-canvas`, the bundle's only size, for a new embedded-analytics OEM line
> of business inside Acme, the company behind the `product-vision`, `product-strategy`,
> `positioning-statement`, `north-star-metrics`, `prd`, `test-plan`, `test-case` and `bug-report` examples
> elsewhere in this library. Per [ADR 0083](../../docs/internal/decisions/0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md),
> this type sits second in the `strategy-docs` chain, between the vision and the strategy: the first sketch
> below is dated 2026-01-19, five days after the
> [product vision](../product-vision/product-vision_example.md) (2026-01-14), and the revision is dated
> 2026-01-21, a week before the
> [FY26 product strategy](../product-strategy/product-strategy_example.md) (2026-01-28). That strategy
> names this same embedded-analytics OEM channel a non-target for Acme's core self-serve product, "both
> requiring a different product than the one above." This canvas is a first sketch of that different
> product, tested as its own business model rather than folded into the core strategy's scope.
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company.

# Acme Embedded Analytics Lean Canvas

## Customer Segments

Mid-market software vendors who already sell to the same operations, fulfilment and finance buyers Acme's
own core product serves, and whose customers have started asking them for charts and dashboards inside
their product instead of a separate login somewhere else. These vendors do not want to be in the analytics
business themselves; reporting is a feature their customers expect, not the product they set out to build.

**Early Adopters.** The specific subset of customers you target first: the two vendors our services team
already built one-off embedded dashboards for in 2025, plus the four vendors on the core sales team's
running list of deals that were marked "needs a different product" and routed away over the last two
quarters without ever being offered anything.

## Problem

1. Their own customers keep asking for dashboards inside the vendor's product, not a separate Acme login,
   and the vendor has no good answer for that request today.
2. Building and maintaining a charting and data-modelling layer well enough to ship is a second product
   their engineering team did not sign up to build, and it competes for the same roadmap slots as their
   actual product.
3. Every time one of these vendors scopes building it themselves, the estimate grows, because the first
   pass always undercounts what query performance and data freshness actually take to get right.

**Existing Alternatives.** How customers solve these problems today: bolt an open-source charting library
onto their own database and hand-roll the queries, or tell their own customers to export a CSV and build
the view somewhere else entirely. Both of the two vendors we built for in 2025 tried the open-source route
first and stalled for more than six months before either one called Acme's services team.

## Unique Value Proposition

An analytics engine already proven against real customer data, available to drop inside another company's
own product under their own navigation and their own brand, rather than a from-scratch integration project
their engineering team has to staff and maintain.

**High-Level Concept.** The X for Y analogy that makes the idea instantly understandable: a payment
processor, but for analytics. The vendor keeps the login screen, the brand and the customer relationship;
the dashboard rendering underneath it is ours.

## Solution

License API access to the same modelling and query engine the core product already runs in production,
returned as embeddable chart components that the vendor's own front end renders inside their existing
navigation. Nothing new to build from zero: the two 2025 integrations become the first reference
implementation, generalized into one API instead of two separate one-off builds.

## Channels

Direct outreach to the four vendors already sitting on the sales team's "needs a different product"
referral list, plus one warm introduction from each of the two 2025 clients into their own vendor network.
Nothing is bought or listed anywhere: every lead so far reaches Acme through a person who already knows it,
which is how both 2025 deals began.

## Revenue Streams

A monthly platform fee plus a per-active-end-user usage charge, priced with the two 2025 deals' actual
invoiced total as a floor rather than a guess from zero. Milestone: one paying design partner signed on the
usage-based contract, not the old flat project-fee arrangement, by the end of Q1 FY26.

## Cost Structure

One engineer pulled from the services team for the quarter to generalize the two existing one-off
integrations into a single reusable API, plus the hosting cost of running embedded dashboards for a small
number of design partners. Enough to reach the one-design-partner milestone above; not a budget for a
separate standing product team yet.

## Key Metrics

Design partners signed on the usage-based contract; weekly active end users inside each partner's embedded
dashboard; dollars billed on usage against the flat-fee floor named above; and the share of support tickets
that land on Acme's own team rather than the vendor's, which tells us whether we are still selling a service
instead of shipping a product.

## Unfair Advantage

Empty, honestly. The two 2025 integrations show the engine can run inside another vendor's product, and any
embedded-analytics specialist could pitch the same four referral-list vendors tomorrow. Something would
belong here only once the overlap with Acme's own buyers proved real: if a vendor's customers already run
Acme's core product, an embedded view could reuse the metric definitions they have agreed there, which a
newcomer could not copy quickly.

## Riskiest Beliefs and Next Tests

| Box | Belief | Evidence So Far | Next Test |
|---|---|---|---|
| Customer Segments | A mid-market software vendor will pay an ongoing usage fee for an embedded dashboard rather than keep building their own charting layer | Two vendors paid a flat project fee for a one-off custom build in 2025; neither has yet been offered the usage-based version | Offer the usage-based contract to those same two vendors first, since they are the only ones who have already paid once |
| Problem | The real blocker for these vendors is engineering cost, not something else such as branding control or data residency | Both 2025 deals surfaced engineering cost in a single kickoff call each, not from a structured round of interviews | Run structured interviews with the four referral-list vendors before assuming the two prior deals generalize to the rest of the list |
| Revenue Streams | Usage-based pricing is viable at a number this market will actually pay, not just a number we can invoice | None yet. Both 2025 deals were flat fees negotiated case by case, so there is no usage-pricing data point at all | Price the first design-partner contract on usage and watch whether the pushback lands on the metering itself or only on the number |

## Versions

| Date | What Changed | Why |
|---|---|---|
| 2026-01-21 | Narrowed Customer Segments to mid-market vendors already selling to Acme's own operations and finance buyers, after sharing the first sketch with the services lead who ran both 2025 deals | The services lead pointed out that the two actual deals were never "any software company": both were vendors already selling into the same buyers Acme's core product already understands, and the broader market claim had no evidence behind it at all |
| 2026-01-19 | Sketched the first version alone. Customer Segments read "any software company wanting embedded analytics" | Written straight from the two 2025 deals, without checking whether a broader market exists beyond those two accounts |
