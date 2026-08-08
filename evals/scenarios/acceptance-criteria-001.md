---
id: acceptance-criteria-001
difficulty: standard
domain: "consumer mobile banking app, spending limit control"
title: "Spending limit control - card story acceptance criteria"
created: 2026-08-08
authored_blind: true
---

# Scenario: Spending limit control - card story acceptance criteria

> **Input brief for a blind efficacy eval.** Every arm receives the ask and the facts below and
> nothing else. Judges never see this file. Authored from the document type description alone by an
> agent instructed not to open this library's templates, per
> [the eval protocol](../../docs/internal/eval-protocol.md) section 6.

## The ask

We are shipping the story "As a cardholder, I can set a monthly spending limit on my debit card so I stop overspending." Design and engineering have already agreed on the flow, I just need this one story locked down before sprint planning tomorrow so QA and engineering are not guessing at what "done" means. Write me the acceptance criteria for this single story. Support has been getting complaints for months about people blowing past what they thought they capped, so I want this airtight on the edge cases, not just the happy path. Keep it scoped to this one story, do not let it balloon into the whole limits feature.

## What you know

- Support logged 340 tickets in Q2 from customers who said a transaction went through after they had already hit their self-set spending limit
- Product wants the limit to be settable in increments of $50, minimum $100 and maximum $10,000 per month
- The limit resets on the customer's monthly statement date, not the calendar month, and that date varies per account
- Engineering flagged that card-present transactions at gas pumps and hotels can authorize for an estimated amount before the final amount is known, which can push a customer over their limit after the fact
- Compliance requires that a hard decline for exceeding a limit still allow the transaction to be manually overridden by the customer within the app within 5 minutes, per the existing dispute-resolution policy
- The mobile app currently supports iOS 16+ and Android 12+, older OS versions are explicitly unsupported for this release
- Design wants a push notification sent when the customer reaches 90 percent of their limit
- The customer support team lead said the number one complaint after a decline is not understanding why, so the decline reason needs to be visible in transaction history within 2 minutes of the decline
- The card product team is separately evaluating whether to support per-category limits (groceries, travel, etc.) but that work has not been scoped or funded yet
- Marketing wants to promote this feature in a Q4 email campaign to reduce churn among budget-conscious customers
- The engineering team uses a microservices architecture with the limits service owned by the Payments platform team, separate from the Notifications team that owns the push alert pipeline
- Legal has not raised any objection to the feature but has asked to be looped in if limits are ever extended to joint accounts

## Retrieval probes

> Not shown to any writing arm. A judge answers these from the produced document alone.

| Question | Expected |
|---|---|
| What is the minimum and maximum monthly spending limit a customer can set, and in what increments? | Minimum $100, maximum $10,000, in $50 increments |
| How does the system handle a card-present transaction, like a gas pump or hotel hold, that authorizes for an estimated amount and later pushes the customer over their limit? | The document should specify treatment of estimated/pending authorizations against the limit, an explicit edge case called out for this story |
| If a transaction is declined for exceeding the limit, how long does the customer have to manually override it, and how quickly must the decline reason appear in transaction history? | Override window of 5 minutes per dispute-resolution policy; decline reason visible in transaction history within 2 minutes |
| Is per-category spending limiting (e.g., groceries, travel) in scope for this story? | No, explicitly out of scope, it is a separate unscoped and unfunded initiative |
| What date does the spending limit reset on, and is it the same for every customer? | It resets on the customer's monthly statement date, which varies per account, not a fixed calendar date |

## Distractors

> Not shown to any writing arm. Facts that are true of the situation and do not belong in a good
> document of this type. A document that includes them is not more complete, it is less disciplined.

- The mobile app currently supports iOS 16+ and Android 12+, older OS versions are explicitly unsupported for this release
- Marketing wants to promote this feature in a Q4 email campaign to reduce churn among budget-conscious customers
- The engineering team uses a microservices architecture with the limits service owned by the Payments platform team, separate from the Notifications team that owns the push alert pipeline
- Legal has not raised any objection to the feature but has asked to be looped in if limits are ever extended to joint accounts
