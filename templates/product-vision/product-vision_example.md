---
title: "Acme Analytics Product Vision"
product: "Acme Analytics"
owner: "Dana Okoro, VP Product"
horizon: "2029 (about three years)"
status: "agreed"
last_updated: "2026-01-14"
next_review: "October 2026, or immediately if either leap of faith below is disproven"
doc_type: product-vision
size: full
format: canvas
source_template: product-vision
source_template_version: 0.1.0
---

> **Worked example.** A filled `product-vision`, full variant, canvas format, for the same Acme Analytics
> product used by the `prd`, `test-plan`, `test-case` and `bug-report` examples. **This document is the top of
> that chain:** the FY26 "Time to Insight" company goal those examples cite descends from the vision below,
> so the library now holds one continuous thread from a product vision down to a defect report and the
> regression that guards it.
>
> Read it alongside [`product-vision_guide.md`](product-vision_guide.md), which is the rubric it was graded
> against. Notice what it does **not** contain: no feature names, no dates other than the horizon, and no
> numeric targets. Those belong to the strategy, the roadmap and the OKR set.

# Acme Analytics Product Vision

## The Vision

By 2029, anyone at a company running Acme can answer a question about their own operations in the time it
takes to ask it out loud, in the place where the question occurred to them.

Priya runs fulfilment. She notices that the north-east region slipped last week, asks why in the same screen
where she noticed it, and has an answer before the thought has gone. She does not file a request, does not
wait for a sprint, and does not learn a query language. Dev, who is currently the only person who could have
answered her, is no longer a queue. He is doing the harder work of deciding what the company should measure
at all.

The change we are trying to create is not faster reporting. It is the end of the waiting period between
noticing something and understanding it.

## Who It Is For, and What They Need

Operations, fulfilment and finance managers at mid-market companies: people who **own a number**, are measured
on it weekly, and today cannot get at it without asking someone else. There are a few dozen of them in a
company the size of Priya's and a few hundred thousand across our market.

What they need is an answer inside the working session in which they had the question. Not within a sprint,
not by Thursday. The cost of the current gap is not the analyst's time, it is the decisions that never get
made because the question was not worth the wait.

**This is not for professional analysts**, meaning people whose job is analysis and who already have
dedicated query tools. They are not blocked on anyone, and building for them is how products like this
quietly become something else. We will keep saying this, because the request to serve them arrives about
twice a year and always from someone senior.

*A note for readers following the sibling examples:* the Saved Views PRD serves a **Recurring Analyst**
persona, which is a different group and is not the exclusion above. A Recurring Analyst returns to the same
dashboards on a cadence and is exactly who this vision is for; a professional analyst writes queries on
other people's behalf and is not.

## Why Us

The reason nobody has solved this is structural. Answering a question in context requires already being in
the context, and every general-purpose analytics product begins by copying the data somewhere else. By the
time the data has arrived in the analytics tool, the context in which the question was asked is gone, and so
is the person who asked it.

We start from inside the operational systems, because that is where Acme began and where our integrations
already live. That is an accident of history rather than a strategy, but it is the one thing a
general-purpose competitor cannot adopt without becoming a different company.

The window opened because operational systems now expose APIs rich enough to read in context. That was not
true five years ago.

## Market and Competitive Context

Today the question goes to a shared analytics inbox, or into a spreadsheet that gets copied and then
diverges. **The real incumbent is the spreadsheet and the favour**, not a product.

General-purpose BI tools can answer these questions and are better at the hard ones. They require a modelling
step our users cannot perform, so adoption reliably stalls at the analyst, which is the same bottleneck in a
more expensive form. Embedded-analytics vendors are closer to us, but they sell to the software vendor rather
than to the operator, so the questions they answer are the ones the vendor anticipated.

Two things could close this window: operational vendors restricting API access, or a general-purpose tool
solving the modelling problem well enough that non-analysts can use it directly. We watch both.

## What This Rules Out

- **We are not building a general-purpose query builder.** Every roadmap conversation eventually produces a
  request for one. It serves analysts, and we have just said analysts are not who this is for.
- **We are not entering enterprise compliance reporting.** It needs audit and retention guarantees this
  future does not require, and pursuing it would reshape the product around a different buyer within two
  years.
- **We would decline a bespoke warehouse integration for a single large account**, even at a price that looks
  good in a quarter, because each one moves us toward being a services business.
- **We are not building a mobile app** while the questions we serve are asked at a desk, in a working
  session, with the operational system already open.

The first of these has been argued for twice by the sales leadership, most recently in November, and declined
on the strength of this section. That is the only evidence that matters for whether this document works.

## Business Goals

Removing the analytics team as a bottleneck is the constraint on how fast the rest of the portfolio can move.
Every other product decision at Acme currently queues behind the same two people.

Commercially, this changes what we are. A reporting add-on is a feature that competes on price at renewal. A
system where the operational questions get asked and answered is where the work happens, and that is a
different conversation with a different person at a different point in the contract.

The strategic option we are buying is the right to be the place operators go first. We do not need to own the
warehouse to be that.

## Horizon and Review

**Horizon: 2029, about three years out.** Long enough that we cannot see the whole path, short enough that
the people reading this expect to still be here.

Reviewed each October alongside annual planning, and immediately if either leap of faith below is disproven.

**A strategy change does not trigger a rewrite.** We expect the strategy to change several times on the way
here, and it already has once: the FY26 plan pivoted from breadth of integrations to depth in two verticals
without changing a word of this document. If we find ourselves rewriting the vision every planning cycle, the
problem is that it was a roadmap.

## Leaps of Faith

**The one that keeps me up: that someone who did not derive an answer will act on it.** Everything above
depends on it, and we cannot know in advance. The early signal is cheap and we are watching it in the pilot:
if users take our answers to Dev to check them, we have not removed a bottleneck, we have built a faster way
to create work for it. Three of eleven pilot users currently do this. We need to understand whether that
number falls with familiarity or is a floor.

**That operational APIs stay open enough to read in context.** Signal: vendor rate-limit and licensing
changes, reviewed quarterly. Two vendors tightened limits in 2025 and both were negotiable, which is
reassuring but not evidence.

**That the mid-market will not simply hire the analyst.** If the cost of analytical headcount falls far
enough, the problem we are solving becomes cheaper to solve with people. We think this is unlikely within the
horizon and we are not currently monitoring it, which is a gap worth naming.
