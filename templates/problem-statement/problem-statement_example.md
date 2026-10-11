---
title: "New-Account Second-View Stall Problem Statement"
problem_name: "New-Account Second-View Stall"
author: "Priya Nair, PM, Reporting"
decider: "Dana Okoro, VP Product"
status: "pending decision"
last_updated: "2026-01-09"
doc_type: problem-statement
size: full
source_template: problem-statement
source_template_version: 0.1.0
---

> **Worked example.** A filled `problem-statement`, full variant, for the same Acme Analytics product used
> throughout this library's examples. Per the discovery-docs family contract, this document extends the
> shared timeline **backward**, to before any of the documents it leads to: it is dated 2026-01-09, four
> days after the [user persona](../user-persona/user-persona_example.md) that names the Recurring Analyst
> (2026-01-05), five days before the product vision (2026-01-14), seven days before the project brief
> (2026-01-16), and eleven days before the business case (2026-01-20) that the project brief and this
> statement together lead to. Nothing in the body below names a solution, an option, a project, or an
> investment, and nothing cites a document dated after this one as already existing, because none of them
> did yet when this was written.
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company.

# New-Account Second-View Stall Problem Statement

## Problem Statement

New accounts to Acme Analytics' Reporting product that have no dedicated data analyst and no query
background cannot get past the step where they must already know which table, which join, and which
measure answers their question, and most of them never build a second dashboard view within the first two
weeks after signup.

## Background

Dana Okoro, VP Product, raised Acme's flat revenue-per-account trend at the December 2025 leadership
review, after finance confirmed the trend had held for five straight quarters and asked for a funding
decision on it rather than letting it wait for the FY26 planning cycle to reach it on its own schedule. The
Reporting team reviewed its own product telemetry in the first week of January and located where the
trend actually starts: not at signup, and not at sharing, but at the single step where a new account first
has to pick which table, which join, and which measure answers the question it opened the product to
answer, before it has had any chance to see value from Reporting at all.

## Who Is Affected

- Who is affected: New Acme accounts that reach that step within their first two weeks after signup and
  have no dedicated data analyst and no query background of their own to draw on. This is the newest slice
  of a segment Acme already has a name for, and it is also the fastest-growing part of the signup base,
  which is why finance is asking about it now rather than treating it as something to monitor at leisure.
- Existing persona, if one already describes this group: the
  [Recurring Analyst](../user-persona/user-persona_example.md#who-they-are), named in the 2026-01-05 user
  persona built from interviews with operations, fulfilment, and finance managers across 9 mid-market
  accounts (n=12): a person who looks at the same numbers on the same schedule because there is nobody
  else to do it, with no dedicated analyst and no query background. The accounts that stall at the
  dataset-picker step are the newest members of that same segment, not a different one.

## Impact and Why Now

- Impact: Revenue per new account has stayed flat for five straight quarters even as sign-ups grew 40
  percent over the same period, so the share of new accounts the product is failing to convert into
  continued use is growing, not holding steady. Two years of incremental investment in documentation, in
  tutorials, and in services capacity has not moved that number.
- Why now: The segment that stalls at the dataset-picker step is the fastest-growing part of the signup
  base, so the flat trend worsens on its current trajectory rather than correcting on its own. Finance
  wants a funding decision ahead of the FY26 planning cycle's own schedule, which is why this statement is
  being written now rather than waiting for that cycle to raise the same question again.

## Evidence

| Evidence | What it shows | Strength |
|---|---|---|
| Reporting-team review of product telemetry, first week of January 2026 | Only 31 percent of new accounts build a second dashboard view within 14 days of signup, and the drop concentrates at the dataset-picker step rather than at signup or at sharing | Direct measurement |
| Session recordings reviewed alongside the telemetry | Two-thirds of the accounts that stall at the dataset-picker step never return to authoring at all | Direct measurement |
| Finance's revenue reporting, reviewed at the December 2025 leadership review | Revenue per new account has been flat for five straight quarters while sign-ups grew 40 percent over the same period | Direct measurement |
| Reporting-team record of documentation, tutorial, and services-capacity investment over the last two years | Incremental investment of this kind has not moved the 31 percent figure above over that period | Direct measurement, but weaker: it shows an absence of movement, not the mechanism behind it |

## How People Cope Today

- How people cope today: An account that stalls at the dataset-picker step either pays for time from
  Acme's services team to get a working view built for it, or settles for whatever single view it landed
  on during onboarding and does not come back to build a second one.
- Prior attempts, and why they fell short: Acme's documentation library and in-product tutorial content
  for the dataset-picker step both grew substantially over the last two years, and services capacity was
  added alongside them. None of that moved the 31 percent figure in the Evidence section above. The
  Reporting team's working read, not yet confirmed, is that the accounts who stall are not failing to find
  the documentation; they are failing before they would know what to search for.

## What Is Not Part of the Problem

Not part of this problem: accounts that already have a dedicated analyst or a query background of their
own, who pass the dataset-picker step today without the telemetry showing any comparable drop. Also not
part of this problem: the rest of the onboarding flow before that step, which the telemetry does not show
losing accounts, and the quality or design of the dashboard view itself once an account succeeds in
building one, which is a separate, already-tracked product area with its own support-ticket history.

## How We Will Know It Is Solved

| Measure | Current level | Direction needed |
|---|---|---|
| Share of new accounts that build a second dashboard view within 14 days of signup | About 31 percent, per the Evidence section above | Up |
| Share of new accounts whose first substantive interaction with Reporting is a request to a data analyst or to the services team for help choosing what to look at | Not yet tracked as its own number; today's support-ticket tagging does not separate this reason from other requests | Down, once tracked |
| Revenue per new account | Flat for five straight quarters | Up |

## Open Questions and Assumptions

- Open questions: Whether accounts stall because the dataset-picker step is hard to find or operate, or
  because it requires knowledge, which table, which join, which measure, that this segment does not have
  at all. Whether the fastest-growing segment's current growth rate continues or levels off. Whether the
  two years of documentation and services investment actually reached the accounts that stall, or whether
  those accounts never engaged it in the first place.
- Assumptions: That an account which stalls at the dataset-picker step would, in fact, go on to build a
  second view if that step itself were easier to get past, an assumption not yet tested against real
  account behavior. That the segment's recent growth rate is representative of its near-term trajectory
  rather than a temporary spike.
- Suspected root cause, labeled as a hypothesis: Hypothesis, not yet confirmed: the dataset-picker step
  requires knowledge this segment does not have, rather than being present but merely hard to find or
  awkward to operate. The Reporting team has not yet tested this against the accounts that actually stall.

## Decision This Informs

- Decider: Dana Okoro, VP Product.
- Decide by: As soon as practical, given finance's request for a funding decision on this trend ahead of
  the FY26 planning cycle's own schedule.
- Next document if pursued: If Dana Okoro's answer is yes, a project brief follows, requesting the
  Reporting team's authority to look into the problem further. This statement does not describe what that
  brief would contain, who would write it, or when it would arrive; that is its own job, not this one's.
