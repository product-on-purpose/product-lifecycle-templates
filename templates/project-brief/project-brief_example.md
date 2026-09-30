---
title: "Question-First Entry and Modelling Defaults Project Brief"
project_name: "Question-First Entry and Modelling Defaults"
author: "Priya Nair, PM, Reporting"
approver: "Dana Okoro, VP Product"
status: "pending decision"
last_updated: "2026-01-16"
doc_type: project-brief
size: full
source_template: project-brief
source_template_version: 0.1.0
---

> **Worked example.** A filled `project-brief`, full variant, for the same Acme Analytics product used
> throughout this library's examples. Per the discovery-docs family contract, this document extends the
> shared timeline **backward**, to before the investment decision the business case later justifies: it is
> dated 2026-01-16, two days after the
> [product vision](../product-vision/product-vision_example.md) agreed on 2026-01-14, eleven days after the
> [user persona](../user-persona/user-persona_example.md) that names the Recurring Analyst, and four days
> before the [business case](../business-case/business-case_example.md) it asks Dana Okoro to authorize.
> Nothing in the body below cites the business case's own comparison of options, its costs, its benefits, or
> its financial metrics, because none of that analysis existed yet when this brief was written; it carries
> only an outline justification and a request to develop that outline into the full case.
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company.

# Question-First Entry and Modelling Defaults Project Brief

## Background and Mandate

- Mandate and background: Dana Okoro, VP Product, raised Acme's flat revenue-per-account trend at the
  December 2025 leadership review, after finance confirmed it had held for five straight quarters. Finance
  asked for a funding decision on it rather than letting it wait for the FY26 planning cycle to reach it on
  its own schedule. Acme's own product telemetry locates where the trend actually starts: only 31 percent of
  new accounts build a second dashboard view within 14 days of signup, and the drop concentrates at the step
  where a new account first has to pick which table, which join, and which measure answers their question,
  before they have had any chance to see the value the
  [2026-01-14 product vision](../product-vision/product-vision_example.md) promises them.
- Why now: The segment that stalls at that step, an account with no dedicated analyst and no query
  background, of exactly the kind the
  [Recurring Analyst](../user-persona/user-persona_example.md#who-they-are) names, is also the fastest-growing
  part of the signup base, so the flat trend worsens on its current trajectory rather than improving on its
  own. Finance wants a funding decision before the FY26 planning cycle would otherwise reach this question,
  and two years of incremental investment in documentation, tutorials, and services capacity has not moved
  the number. This brief asks for authority to develop the vision's commitment into a funded proposal now,
  rather than wait for the next planning cycle to raise the same question again.

## Objectives

| ID | Objective | How you will know it succeeded |
|---|---|---|
| OBJ-1 | Raise the share of new accounts that build a second dashboard view within 14 days of signup, meaningfully above the 31 percent baseline (an illustrative planning figure; the business case now being asked for will set the exact target against real cost and benefit data) | The existing second-view usage event, tracked monthly against the pre-initiative cohort |
| OBJ-2 | Reduce how often a new account's first substantive interaction with Reporting is a request to a data analyst or the services team for help choosing what to look at, rather than something the product resolves on its own | Services and support ticket tagging for "which table" or "which dataset" requests from accounts in their first 14 days, tracked monthly against the pre-initiative baseline |

## Scope and Exclusions

- In scope and deliverables: Investigating an alternative to today's dataset-picker step for new accounts,
  one that does not require a new account to already know which table, join, and measure answers its
  question before it sees any value. This includes exploring modelling defaults, built the way the services
  team's per-account modelling already works today but shipped as a product default instead of custom
  per-account output, for Acme's two largest verticals, where the team has the deepest existing modelling
  experience to draw on. If the investigation is promising, the deliverable is a working version for those
  two verticals.
- Explicitly out of scope: Any change to how an existing account, already past the dataset-picker step,
  uses Reporting today; this project targets only the new-account stall the telemetry above identifies. This
  brief does not decide how the investigated approach compares against continuing today's approach or
  against further investment in documentation, tutorials, and services capacity; that comparison, including
  the option of doing nothing, is the business case's job, not this one's.

## Outline Business Justification

- Why this is worth doing: The revenue-per-account trend has stayed flat for five straight quarters even as
  sign-ups have grown, and the stall concentrates at one identifiable step in the product rather than being
  spread evenly across onboarding. Two years of investment in documentation, tutorials, and services capacity
  has not moved that number, which is why this brief proposes addressing the stall point itself rather than
  making the existing step easier to learn. A working version for two verticals would give finance concrete
  evidence, ahead of the next planning cycle, on whether the approach actually shifts new-account behavior.
- Outline estimate, illustrative and not final: roughly 10 to 20 engineer-weeks from one or two engineering
  pods over a quarter, plus some services-team time; an envelope that the business case below will cost.
- Full comparison of options deferred to: The business case Priya Nair will bring to the 2026-01-26
  leadership review, including continuing today's approach and further investment in documentation,
  tutorials, and services capacity as alternatives.

## Constraints and Who Should Be Involved

- Constraints and dependencies: No new headcount is planned for this investigation, so it draws on the
  Reporting team's existing sprint capacity. It also depends on Legal's ongoing data-processing review
  clearing the use of existing session data for any model training; if that clearance has not landed by the
  time the business case is ready to size an approach, the estimate above may need a more conservative,
  slower-ramping alternative. It further depends on the services team's willingness to free time from
  per-account custom modelling to support the investigation, which has not yet been agreed with Services
  leadership.
- Known risks and assumptions: Untested assumption: the two pilot verticals share enough structure that most
  of the modelling groundwork built for them will transfer to a third vertical later; if it does not, the
  return on the work looks different than planned. Untested assumption: an alternative entry point can
  actually resolve a new account's own question often enough to replace, rather than merely supplement, the
  dataset picker; this has not yet been tried against real account data at any scale.

| Name | Role | Why involved |
|---|---|---|
| Dana Okoro | VP Product | Owns the funding decision this brief, and the business case it leads to, both ask Dana Okoro to make |
| Priya Nair | PM, Reporting | Leads the investigation and will bring the business case to the leadership review |
| Lee Zhang | Data Engineering | Owns the dependency on existing session data for model training, which Legal's data-processing review must clear and the estimate above rests on |
| Services leadership | Services | Must agree to free services-team time from per-account custom modelling; the constraints above record that this is not yet agreed |

## Decision Requested

- Decision requested: Authorize Priya Nair to develop this initiative into a full business case, comparing
  it against continuing today's approach and against further investment in documentation, tutorials, and
  services capacity, for decision at the 2026-01-26 leadership review.
- Approver: Dana Okoro, VP Product
- Next document once decided: A business case, due at the 2026-01-26 leadership review.

## Project Approach

- Approach: Build in house within the existing Reporting team, reusing the modelling approach the services
  team already applies per account. Commissioning an outside team to build the entry point was considered and
  set aside: the modelling defaults depend on per-account knowledge that sits with Acme's own services team,
  which an outside team would first have to rebuild. This is the working assumption the investigation starts
  from, not a settled choice, and the business case will cost it before anyone commits to it.

## Relationship to Other Documents

- Relationship to other documents: Triggered by Dana Okoro's mandate at the December 2025 leadership review,
  carrying forward the commitment the
  [2026-01-14 product vision](../product-vision/product-vision_example.md) made two days before this brief.
  This document carries only the outline justification above; the full comparison of options develops in the
  business case Priya Nair brings to the 2026-01-26 leadership review. Once that business case is approved,
  this brief is superseded by whatever delivery documentation the approved investment requires, and it is not
  consulted again after that point.
