---
title: "2026-05 Reporting Friction Study Research Report"
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

# 2026-05 Reporting Friction Study Research Report

## Summary

- What the study found, and what it recommends: Re-filtering, not exporting or sharing, is what analysts
  repeat most on every visit to their dashboard. 9 of 12 described rebuilding it by hand several times a
  day, and 3 already keep a personal file of "the filters I always use" to avoid relying on memory. We
  recommend funding work that lets an analyst save a named filter setup and reopen it later, and that lets
  a saved setup be handed to a teammate.
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
| When an analyst rebuilds filters after the dashboard resets to its default, how often does what they rebuild actually match what they meant to be looking at? | Not always. A filter set rebuilt from memory sometimes left out a field, so the dashboard showed the wrong slice of data for part of the session before the analyst noticed. | N/A | Answered |
| What do analysts already do, inside the product or outside it, to avoid rebuilding filters from memory? | 3 of 12 already kept a personal text file listing "the filters I always use"; the rest rebuilt from memory each time. | N/A | Answered |
| Does this differ between an analyst who opens the dashboard several times a week and one who opens it about once a week? | Could not be answered from this study. See Open Questions, below. | N/A | Open |
| How often does rebuilding filters come up in a session compared with other repeated actions, like exporting a view or sharing one with a teammate? | More often than either. Re-filtering outranked both exporting and sharing as the most frequently repeated action logged across the sessions. | N/A | Answered |

## What We Did

- Method, and whether it matches the plan: One-to-one moderated interviews built around a walkthrough of
  the analyst's own live dashboard, matching the plan. No prototype or mockup was shown, since nothing had
  been designed yet.
- Participants, as a fraction of those recruited: 12 of 15 recruited completed a session; the other three,
  held in reserve, were not needed.
- Dates sessions ran: 2026-05-04 to 2026-05-15, with a pilot session on 2026-05-01.
- What this sample size lets you claim, and what it does not: A study of this size is good at surfacing a
  problem shared by most of a screened group; it is not built to rank two slightly different ways of saving
  a filter set against each other.
- One line on anything that ran differently from the plan: Nothing. Sessions ran exactly as the plan
  described, including the pilot.

## Key Findings

| Finding | Participants (fraction) | Evidence | Positive, problem, or participant suggestion |
|---|---|---|---|
| Re-filtering was the single most frequent repeated action in the dashboard across every session, ahead of both exporting a view and sharing one. | 12 of 12 | Logged by the note taker in every session, as the action an analyst returned to before anything else they did that day. | Problem |
| 9 of 12 analysts described rebuilding their filters by hand several times in a single day. | 9 of 12 | "I rebuild the same four filters most mornings before I can even look at anything." | Problem |
| 3 of 12 already kept a personal text file listing "the filters I always use," so they would not have to rebuild from memory. | 3 of 12 | Each of the three showed the moderator the file on their own screen partway through the walkthrough. | Participant suggestion |
| Once an analyst located Acme's existing filter controls, picking the right field and operator gave nobody any trouble. | 12 of 12 | Every participant who adjusted a filter during the walkthrough picked the right field and operator on the first try. | Positive |
| 2 of 12, without being asked, said they wanted their whole team looking at the same filtered slice, rather than each person rebuilding their own. | 2 of 12 | "I don't want my teammate explaining a different number than mine because he filtered it differently." | Participant suggestion |

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
| Fund work that lets an analyst save their current filters, date range, and visible columns under a name, and reopen that same setup on a later visit. | Re-filtering is the most frequent repeated action in the dashboard; 9 of 12 rebuild it by hand several times a day; 3 of 12 already keep a personal file to avoid it. | Removes the one step every analyst in this study repeated before they could do anything else, and removes the chance that a filter set rebuilt from memory leaves out a field and shows the wrong slice of data. |
| Let a saved setup be handed to a teammate, not only kept for its owner. | 2 of 12 wanted their team looking at one agreed slice rather than each person's own rebuild. | A teammate who opens a shared setup starts from the same numbers, instead of rebuilding a close but not identical version from memory. |

## Open Questions

| Question the study raised | Why it stayed unanswered | What would answer it |
|---|---|---|
| Does re-filtering cost an analyst who opens the dashboard several times a week more time than it costs one who opens it about once a week? | Recruiting screened every participant only for the Recurring Analyst's minimum weekly cadence, not for this finer split, so the twelve sessions cannot be reliably divided along that line. | A follow-up study that screens and recruits specifically on opening frequency, rather than on the broader Recurring Analyst definition. |
| How many analysts, beyond the two who raised it unprompted, would actually use a filtered view that a teammate set up and shared? | Only two of the twelve volunteered this without being asked, and none of the plan's own questions asked about team-level sharing directly, so the sessions cannot say how common the want is. | A future study that asks every participant directly whether they would use a view someone else set up for them. |

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
