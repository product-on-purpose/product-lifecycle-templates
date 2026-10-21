---
title: "Acme Analytics Positioning Statement"
product: "Acme Analytics"
owner: "Dana Okoro, VP Product"
target_customer: "the Recurring Analyst"
status: "agreed"
last_updated: "2026-01-30"
doc_type: positioning-statement
size: lean
source_template: positioning-statement
source_template_version: 0.1.0
---

> **Worked example.** A filled `positioning-statement`, lean variant, for the same Acme Analytics product
> used throughout this library's examples. Per [ADR 0076](../../docs/internal/decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md),
> this type sits third in the `strategy-docs` chain: it is dated 2026-01-30, two days after the
> [FY26 product strategy](../product-strategy/product-strategy_example.md) (2026-01-28) whose target
> segment it carries forward, and it will sit just ahead of the North Star metric still to come. Dana
> Okoro, VP Product, owns the vision, the strategy, and this document, which is why the three speak in one
> voice. Nothing below is messaging, a battlecard, or a competitive map; those are a different document and
> this library has not yet admitted the first of them.
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company. The 31 percent figure below repeats the FY26 product strategy
> example's own baseline exactly, because both documents describe the same account behavior.

# Acme Analytics Positioning Statement

## Purpose and Boundary

This document states how Acme Analytics stands against the spreadsheet-and-a-favour status quo and against
general-purpose BI tools, for the Recurring Analyst, as of 2026-01-30. It is internal, written for the
people who make product, marketing and sales decisions about Acme Analytics, not for customers or the
press.

This document deliberately does not state:

- **Messaging**: the external language and talking points a team builds on top of this positioning, once
  it is settled. This library has not yet admitted a messaging-framework bundle.
- **A battlecard**: sales-facing competitive responses, downstream of and reinforcing this positioning,
  never an input to it.
- **A positioning map**: a two-axis competitive chart. A different artifact, out of this library's scope.
- **Acme Analytics's product vision**: the long-term, aspirational, future-facing destination this product
  is working toward. That document already names the spreadsheet and the favour as the real incumbent; this
  one is present-day and competitive, not aspirational, and does not repeat the vision's horizon or its
  leaps of faith.

## The Statement

For the Recurring Analyst, who needs an answer to an operational question inside the same working session
in which it came up, Acme Analytics is the in-context analytics product that answers a question without
copying the data anywhere else first, unlike the spreadsheet and the favour or a general-purpose BI tool,
because Acme already sits inside the operational systems where the work happens.

## The Components

**Named alternative.** What the Recurring Analyst does today without Acme Analytics, named specifically
rather than as a category of competitor: the question goes to a shared analytics inbox, or into a
spreadsheet that gets copied and then diverges, or to whichever colleague currently knows how to build the
view, as a favour. A second, named alternative exists for the same target: general-purpose BI tools, which
can answer the harder questions but require a modeling step the Recurring Analyst cannot perform alone, so
adoption stalls at the same point, now behind a purchase order instead of a favour.

**Target.** Who this statement is written for, named by what they need rather than by a demographic label
alone: the Recurring Analyst, someone at a mid-market company who owns a number, answers questions about it
weekly, and has no data team behind them.

**Need.** The specific problem or job this target has that sends them looking for a solution at all: an
answer to a question about their own operating number, inside the working session in which the question
came up, without filing a request, waiting for a sprint, or learning a query language first.

**Category.** The frame of reference this target customer will use to understand what kind of thing Acme
Analytics is: an analytics product that lives inside the operational systems where the work already
happens, not a destination the Recurring Analyst travels to with a question.

**Benefit.** What this target customer gets from Acme Analytics that matters to the need above: a question
asked in plain language returns an answer inside the same operational system where it came up, without
copying the data anywhere else first and without a favour owed to anyone.

**Differentiation.** What makes that benefit genuinely different from what the named alternative delivers,
not just differently described: Acme already sits inside the operational systems where the work happens,
because that is where the product began and where its integrations already live, an arrangement that
started as an accident of history rather than a deliberate strategy. A general-purpose BI tool and the
spreadsheet both require the data to be copied out to a separate place before anyone can ask it a
question, and a BI tool then requires a modeling step this target customer cannot perform alone.

## Why This Positioning

Only 31 percent of new accounts today build a second view within 14 days of signing up, and the session
recordings behind that number put the drop at the dataset picker, the step where a user who does not
already know the schema has to construct one before asking anything. Acme's own self-serve path still
begins there today; the differentiation above is about the step before that one. A general-purpose BI tool
cannot reach that screen at all until someone has copied the account's data in and modeled it, a step this
target customer cannot perform alone, while Acme's integrations already read the data where it lives, so
the account starts inside the operational system on day one instead of waiting on a modeling project. If a
general-purpose BI tool's name were substituted for Acme Analytics in the statement above, the claim would
stop being credible at the word "unlike": a BI tool has nothing to read until an account tells it what to
model, which is the exact gap this positioning is built on.

## When We Revisit It

- Last reviewed: 2026-01-30
- Check-in interval: alongside the annual strategy review each October, the same cadence the product
  vision already keeps, not on a shorter calendar of its own
- Who notices a trigger event and brings the team back to this document: Dana Okoro, VP Product
- Named triggers that call for an earlier look, beyond the scheduled check-in: a general-purpose BI vendor
  ships a modeling layer that a non-analyst can complete alone; the strategy's planned per-vertical
  modeling defaults ship and the second-view rate still does not move, which would say the dataset picker
  was never the gap this positioning's because-clause assumes; a lost-deal pattern starts naming the same
  alternative repeatedly, where today no single alternative recurs often enough to name by brand; or a
  senior sales or product leadership change, the same trigger the vision already watches for itself.
