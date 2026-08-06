---
title: "Elena Cho User Persona"
persona_name: "Elena Cho"
persona_role: "Regional Operations Manager, Meridian Freight (an Acme Analytics customer account)"
product_or_team: "Acme Analytics - Reporting"
owner: "Priya Nair (PM, Reporting)"
status: "active"
last_updated: "2026-01-05"
evidence_tier: "qualitative"
doc_type: user-persona
size: full
source_template: user-persona
source_template_version: 0.1.0
---

> **Worked example.** A filled `user-persona`, full variant, for the same Acme Analytics product used
> throughout this library's examples. Per the discovery-docs family contract, this document sits at the
> **start** of the shared timeline, ahead of even the product vision: it is dated 2026-01-05, nine days
> before the [product vision](../product-vision/product-vision_example.md) agreed on 2026-01-14. It defines
> the **Recurring Analyst**, the person the vision's own reader aside names, the
> [`kpi-dashboard`](../kpi-dashboard/kpi-dashboard_example.md) metric definitions track, and the
> [`acceptance-criteria`](../acceptance-criteria/acceptance-criteria_example.md) example's story assumes,
> without any of those documents ever having defined her. Nothing in the body below cites the vision, the
> [PRD](../prd/prd_example.md), the acceptance criteria, or the KPI dashboard, because none of them existed
> yet when this was written; it rests only on interviews and a support-ticket review conducted before this
> date.
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company.

# Elena Cho User Persona

## Who They Are

- Name: Elena Cho
- Role: Regional Operations Manager, Meridian Freight (an Acme Analytics customer account: mid-market
  ground freight, four regional hubs)
- Quote: "I don't need a better chart. I need the same three filters still there on Monday, not gone again."
- Background: Runs the Monday morning performance review for four regional hubs, and the on-time delivery
  number she reports there is the one her VP tracks every week. She has no dedicated analyst and no query
  background; the dashboard she uses was built by IT eighteen months ago and has not changed since. (Quote
  and detail from interviews conducted across November and December 2025, n=12.)
- The label this document establishes: the **Recurring Analyst**. She is defined by cadence, not by job
  title. The same person, looking at the same numbers, on the same schedule, because there is nobody else
  to do it. The name matters because a team that hears "analyst" builds for someone who can write a query,
  and she cannot. Every downstream document that assumes this reader should point here rather than
  re-describe her.

## Goals and Motivations

| Goal | Why it matters | Evidence (how you know) |
|---|---|---|
| Have the four-hub on-time delivery number ready before the 9am Monday review, without asking anyone for it | A number she has to chase in front of her VP costs her credibility for the rest of the week, not just that meeting | Interviews (n=12), raised by 11 of 12 |
| See the same three filters she left last week without rebuilding them from memory | The filters, not the underlying data, are what she actually has to reconstruct every time she opens the dashboard | Interviews (n=12), raised by 9 of 12; corroborated by the support-ticket review below |
| Notice which hub is drifting off trend before her VP asks about it | Being the one who raises it changes the conversation from defending a number to proposing a plan | Interviews (n=12), raised by 7 of 12 |

## Pains and Barriers

| Pain or Barrier | Impact | Evidence (how you know) |
|---|---|---|
| The dashboard opens to the company-wide default view, not her four hubs, every single time | Spends the first 5 to 10 minutes of nearly every session reapplying region, week, and hub filters before she can look at anything | Interviews (n=12); a six-month review of dashboard support tickets found 34 tickets using wording like "view reset" or "filters gone" |
| When the dashboard cannot answer a question, the only path is asking a data analyst and waiting for a reply | The question is often not worth the wait, so it goes unasked and the Monday number gets explained on judgment instead of evidence | Interviews (n=12), raised by 8 of 12 |
| The trend chart's on-time and delayed lines print in the same shade of blue on the handout her VP reads from | She has learned to say "top line, bottom line" out loud in the review rather than trust the room can tell them apart; one of her hub leads is colorblind and named this unprompted | Interviews (n=12), named unprompted by 2 of 12, including the hub lead it affects |

## Context of Use

| Factor | Detail | Evidence (how you know) |
|---|---|---|
| Device and setting | Laptop mirrored to the conference room screen for the Monday review; the same laptop, alone, for the two or three off-cycle checks she runs most weeks | Interviews (n=12) |
| Frequency | Opens the dashboard 3 to 4 times a week; the heaviest and highest-stakes use is 8:40 to 9:00am Monday, right before the review starts | Interviews (n=12) |
| Workaround already built | Keeps a personal spreadsheet listing last week's exact filter values, so she can rebuild the view from a checklist instead of from memory | Interviews (n=12), independently described by 6 of 12 with only minor variation |

## Scenarios

**Scenario: rebuilding Monday's view before the review starts**

- Beginning: Elena needs the four-hub on-time delivery numbers ready before her 9am Monday review, and she
  has twenty minutes before the room fills.
- Middle: She opens the dashboard at 8:40 and it loads the company-wide default, not her four hubs. She
  pulls up her personal spreadsheet and reapplies region, week, and hub filters one at a time, checking each
  one against the list so she does not miss the fourth hub the way she did in October, when she presented
  three hubs' numbers and had to correct herself in front of her VP.
- End: She has the numbers rebuilt by 8:56, four minutes to spare, but the four minutes she meant to spend
  deciding what she would say if South Hub's number had moved are gone, spent on the filters instead. It
  moved. She finds out in the room.

## Evidence Basis

- Evidence tier: Qualitative
- Basis: 12 semi-structured interviews with operations, fulfilment, and finance managers across 9 mid-market
  customer accounts, conducted across November and December 2025, plus a review of six months of dashboard
  support tickets tagged with filter- or view-reset language.
- Last updated: 2026-01-05
- Revisit when: Acme's dashboard default-view behavior changes, or this segment's usage pattern shifts away
  from the weekly review cadence this persona is built around.
