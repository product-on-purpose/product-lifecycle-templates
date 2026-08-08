---
id: acceptance-criteria-002
difficulty: messy
domain: "games platform / parental controls on in-app purchases"
title: "Parental Approval for In-App Purchases: Acceptance Criteria"
created: 2026-08-08
authored_blind: true
---

# Scenario: Parental Approval for In-App Purchases: Acceptance Criteria

> **Input brief for a blind efficacy eval.** Every arm receives the ask and the facts below and
> nothing else. Judges never see this file. Authored from the document type description alone by an
> agent instructed not to open this library's templates, per
> [the eval protocol](../../docs/internal/eval-protocol.md) section 6.

## The ask

We're finally building parental approval for in-app purchases, and I need acceptance criteria for the first story: a parent gets asked to approve or deny before their kid's purchase goes through. Support has been eating 340 refund tickets a quarter over surprise purchases, so this needs to actually hold up, but Finance and CS are fighting about whether small purchases should even trigger the prompt, and nobody has settled what happens when a parent just doesn't respond in time. Engineering already flagged that our original notification speed assumption doesn't hold on Android. Pull in what's true from Legal, Support, and both platforms, make a call where the team hasn't agreed yet, and write down your reasoning so whoever picks this up next isn't guessing. I'd rather you commit to an answer and flag it than leave a blank.

## What you know

- Support logged 340 refund requests last quarter tied to purchases a child made without a parent's knowledge, and Customer Support says 60 percent of those were purchases under $5.
- Finance wants purchases under $5 to skip the approval step entirely, arguing the extra tap causes cart abandonment on small "gem pack" buys.
- The CS lead is on record disagreeing with Finance, saying any dollar threshold undermines the whole feature and every purchase should require approval regardless of price.
- Product originally briefed a 30 second target for getting the approval prompt to the parent's phone, but the Android engineering lead says push delivery can lag up to 5 minutes because of battery-optimization throttling on many devices.
- There is no agreed answer yet for what happens if the parent never responds: one camp wants the purchase auto-denied after the timeout, another wants it auto-approved after 24 hours so carts don't just die.
- Apple's App Store review guidelines require iOS purchases to route through Apple's own Ask to Buy mechanism; this constraint does not apply on Android, where the team can build its own approval flow.
- 12 percent of parent accounts on the platform have more than one child profile linked to them, and an approval request needs to make clear which child triggered it.
- Legal flagged that COPPA requires verifiable parental consent for users under 13, and today the platform's age gate at signup is self-reported and not verified.
- Support wants each approval decision (approved, denied, timed out) retained for 90 days so they can resolve billing disputes.
- The design team's mockup uses the brand teal color #00B8A9 for the approve button.
- The payments backend team is separately planning to refactor the payment microservice from Java to Kotlin next quarter.
- Marketing has a "Family Pilot" campaign planned for the next quarterly release to promote parental controls generally.

## Retrieval probes

> Not shown to any writing arm. A judge answers these from the produced document alone.

| Question | Expected |
|---|---|
| What happens to a purchase if the parent never responds to the approval request within the timeout window? | It resolves to denied/blocked by default after the timeout (the document must explicitly pick this over auto-approve-after-24-hours and say why, e.g. child-safety over cart abandonment). |
| Is there a dollar amount below which a purchase skips parental approval? | No, there is no bypass threshold; all purchases require approval regardless of price, rejecting Finance's under-$5 exemption proposal. |
| What platform-specific requirement applies to iOS but not Android? | iOS purchases must go through Apple's native Ask to Buy mechanism per App Store review guidelines; Android does not have this constraint. |
| How long does an approval decision need to be retained after it is made? | 90 days, so Support can resolve billing disputes. |
| What is out of scope for this piece of work? | Redesigning or hardening the underlying age verification/COPPA consent flow is out of scope; this work only covers the purchase-approval interaction itself. |

## Distractors

> Not shown to any writing arm. Facts that are true of the situation and do not belong in a good
> document of this type. A document that includes them is not more complete, it is less disciplined.

- The design team's mockup uses the brand teal color #00B8A9 for the approve button.
- The payments backend team is separately planning to refactor the payment microservice from Java to Kotlin next quarter.
- Marketing has a "Family Pilot" campaign planned for the next quarterly release to promote parental controls generally.
