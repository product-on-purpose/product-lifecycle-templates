---
title: "Discovery readout: Reporting friction study, 2026-05"
study_name: "2026-05 Reporting Friction Study"
author: "Priya Nair, PM, Reporting"
plan_link: "../user-research-plan/user-research-plan_example.md"
status: "final"
last_updated: "2026-05-27"
doc_type: user-research-report
size: full
source_template: user-research-report
source_template_version: 0.1.0
---

> **Worked example.** A filled `user-research-report`, full variant, for the same Acme Analytics product
> used throughout this library's examples. Per the research-docs family contract's shared-scenario rule,
> this document reports out the 2026-05 Reporting friction study that the
> [research plan](../user-research-plan/user-research-plan_example.md) set out on 2026-04-20, and that four
> other shipped examples in this library cite and, before this one, none of them shows: the
> [Saved Views design brief](../design-brief/design-brief_example.md), the
> [Saved Views PRD](../prd/prd_example.md), the [Saved Views epic](../epic/epic_example.md), and the
> [Reporting squad sharing announcement](../announcement-internal-comms/announcement-internal-comms_example.md).
> It is dated 2026-05-27, within the two weeks of the last session, 2026-05-15, that the plan promised, and
> before the design brief of 2026-06-01 that first frames a concept from these findings, the PRD of
> 2026-06-12, and the epic of 2026-06-13. Nothing in the body below names a concept, a feature, or a product
> decision; this report answers the plan's own questions and recommends, and leaves framing and deciding to
> the documents that follow it.
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company.

# Discovery readout: Reporting friction study, 2026-05

## Summary

- What the study found, and what it recommends: Re-filtering, not exporting or sharing, is what analysts
  repeat most on every visit to their dashboard. 9 of 12 described rebuilding filters by hand several times
  a day, and 3 already keep a personal text file of "the filters I always use" to avoid relying on memory.
  We recommend funding work so that an analyst no longer rebuilds the same filters on every visit, and
  weighing whether that work should reach a teammate too.
- Decision these findings inform, and who makes it: Whether the Reporting team funds work next quarter on
  letting analysts avoid rebuilding their filters from scratch, a decision the Reporting team's own
  leadership makes.

## Background and Objectives

- Why this study ran: A request to let the dashboard hold onto an analyst's filters between visits had come
  up twice in the past year and been deferred both times, each time for lack of more than a handful of
  comments that it might be worth the engineering time. The January user persona interviews raised a
  version of the same friction independently, across a different set of accounts than either request came
  from, which was enough overlap to check properly before the request came up a third time.
- Decision it informs, restated for a reader who has not seen the plan: Whether the Reporting team funds
  work next quarter on letting analysts avoid rebuilding their filters from scratch.
- Link to the plan: [2026-05 Reporting Friction Study Research
  Plan](../user-research-plan/user-research-plan_example.md)
- If this studies something people already use, why it is still discovery work: This studies Acme's
  dashboard as customers use it today, not a concept that does not exist yet. It is still discovery work
  because the study looks for where an opportunity exists inside something already shipped, not for whether
  the dashboard meets a specification it was built against.

## Research Questions and Answers

| Research question (as the plan wrote it) | Answer | Confirms the plan's hypothesis? | Status |
|---|---|---|---|
| Where in a session does an analyst's time go to rebuilding something rather than reading what the dashboard already shows? | To rebuilding filters. Re-filtering was the single most frequent repeated action in the dashboard, ahead of export and share. | Confirmed | Answered |
| When an analyst rebuilds filters after the dashboard resets to its default, how often does what they rebuild actually match what they meant to be looking at? | Not always. Analysts described filters set incorrectly from memory, which risks an analysis of the wrong slice (Key Findings, row 2). The sessions did not count how often it happened. | N/A | Answered |
| What do analysts already do, inside the product or outside it, to avoid rebuilding filters from memory? | 3 of 12 already kept a personal text file listing "the filters I always use"; the rest rebuilt from memory each time. | N/A | Answered |
| Does this differ between an analyst who opens the dashboard several times a week and one who opens it about once a week? | Could not be answered from this study. See Open Questions, below. | N/A | Open |
| How often does rebuilding filters come up in a session compared with other repeated actions, like exporting a view or sharing one with a teammate? | More often than either. Re-filtering outranked both exporting and sharing as the most frequently repeated action logged across the sessions. | N/A | Answered |

## What We Did

- Method, and whether it matches the plan: One-to-one moderated interviews built around a walkthrough of
  the analyst's own live dashboard, about an hour each, matching the plan. Participants reacted to the
  dashboard as it shipped at the time. No prototype or mockup was shown, since nothing had been designed
  yet.
- Participants, as a fraction of those recruited: 12 of 15 recruited completed a session; the other three,
  held in reserve, were not needed.
- Dates sessions ran: 2026-05-04 to 2026-05-15, with a pilot session on 2026-05-01.
- What this sample size lets you claim, and what it does not: A study of this size is good at surfacing a
  problem shared by most of a screened group; it is not built to rank two slightly different ways of saving
  a filter set against each other. The sessions covered only the small set of report types these analysts
  happened to use, so nothing here shows the finding holds for every report type Acme ships.
- One line on anything that ran differently from the plan: Nothing. Sessions ran exactly as the plan
  described, including the pilot.

## Key Findings

| Finding | Participants (fraction) | Evidence | Positive, problem, or participant suggestion |
|---|---|---|---|
| Re-filtering was the single most frequent repeated action in the dashboard, ahead of export and share. | All 12 sessions, counted together | The note taker's log of repeated actions, totalled across the twelve sessions, as the plan set out. | Problem |
| 9 of 12 analysts described manually rebuilding filters several times a day. | 9 of 12 | "Every time it resets I'm building the same filters again, and every so often I get one wrong and don't notice until the numbers look off." | Problem |
| 3 of 12 already kept a personal text file listing "the filters I always use," so they would not have to rebuild from memory. These files were the only saved setups in the study, and no teammate could reach them. | 3 of 12 | Each of the three showed the moderator the file on their own screen partway through the walkthrough. | Problem |
| Analysts found and used Acme's existing filter controls without help; the trouble was remembering which filters to set, not setting them. | 12 of 12 | No participant asked the moderator how to apply a filter during the walkthrough. | Positive |

## Task Results

This study was not a usability test. Each session was a walkthrough of the analyst's own dashboard and
their own data, not a set of tasks handed to them, so the table below and the questionnaire line are both
N/A.

| Task | Completion (fraction, against the plan's criterion) | Errors | Time on task | Notes |
|---|---|---|---|---|
| N/A | N/A | N/A | N/A | Not a usability test; see the note above |

- Questionnaire scores the plan named, and the convention they are read against, if any: N/A, not a
  usability test.

## Recommendations

| Recommendation | Tied to finding(s) | Why |
|---|---|---|
| Fund work next quarter so that an analyst no longer rebuilds the same filters on every visit. Leave how to the design work that follows. | Re-filtering is the most frequent repeated action in the dashboard; 9 of 12 rebuild filters by hand several times a day; 3 of 12 already keep a personal text file to avoid it. | Removes the repeated action the study logged most often, and the risk that a filter set from memory is wrong and shows the wrong slice of data. |
| Weigh, in that same work, whether a teammate should be able to start from the filters someone else set up. | The only saved setups in the study were personal text files no teammate could reach; some participants who lead a team raised the same want (Open Questions). | Each analyst today rebuilds their own version of a shared slice, so two people can read different numbers for what they believe is the same view. |

## Open Questions

| Question the study raised | Why it stayed unanswered | What would answer it |
|---|---|---|
| Does re-filtering cost an analyst who opens the dashboard several times a week more time than it costs one who opens it about once a week? | Recruiting screened every participant only for the Recurring Analyst's minimum weekly cadence, not for this finer split, so the twelve sessions cannot be reliably divided along that line. | A follow-up study that screens and recruits specifically on opening frequency, rather than on the broader Recurring Analyst definition. |
| How many team leads want their team looking at one agreed view, rather than each person's own reconstruction of it? | Some participants who lead a team raised this unprompted, but none of the plan's questions asked about it, so the sessions cannot say how common the want is. | A future study that asks team leads directly whether they would hand their team one agreed view. |

## Appendix

- Session list, with dates: Linked in the UX Research function's shared drive: 12 sessions, 2026-05-04 to
  2026-05-15, one row per participant with the date their own session ran.
- Materials used: The screener used to recruit the twelve participants, linked in the same shared drive. No
  separate consent form; the spoken statement described in the plan's Consent, Privacy and Ethics section
  is what every session used.
- Where raw notes or recordings live, and whose retention policy governs them: In Acme's standard research
  storage, visible only to the UX Research function and the Reporting teammates who observed a session,
  under Acme's standing research-data retention policy, linked in the UX Research function's internal
  space, without restating that policy's length as a figure this report sets.
