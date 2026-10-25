---
title: "2026-05 Reporting Friction Study Research Plan"
study_name: "2026-05 Reporting Friction Study"
author: "Priya Nair, PM, Reporting"
approver: "Dana Okoro, VP Product"
status: "approved"
last_updated: "2026-04-20"
doc_type: user-research-plan
size: full
source_template: user-research-plan
source_template_version: 0.1.0
---

> **Worked example.** A filled `user-research-plan`, full variant, for the same Acme Analytics product used
> throughout this library's examples. Per the research-docs family contract's shared-scenario rule, this
> document plans the 2026-05 Reporting friction study, which the
> [Saved Views design brief](../design-brief/design-brief_example.md) and
> [Saved Views PRD](../prd/prd_example.md) both cite and neither shows. It is dated 2026-04-20, before the
> sessions run (2026-05-04 to 2026-05-15), before this family's own report counterpart,
> `user-research-report` (catalog entry 18, not yet built in this library), would read out the same study
> around 2026-05-27, and well before the design brief of 2026-06-01 that later frames the concept this
> study's findings feed. Nothing in the body below names a concept, a feature, or a finding, because the
> study has not run yet, and nothing below cites a document dated after 2026-04-20 as already existing,
> because none of them did yet when this was written.
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company.

# 2026-05 Reporting Friction Study Research Plan

## Why This Study, and the Decision It Informs

- Why this study runs now: A request to let the dashboard hold onto an analyst's filters between visits
  has come up twice in the last year and been deferred both times, each time for lack of anything beyond a
  handful of comments that it might be worth the engineering time. The interviews behind the January user
  persona, held in November and December 2025, raised a version of the same friction independently, across
  a different set of accounts than either request came from, which is enough overlap to be worth checking properly before the request comes up a
  third time.
- Decision the findings will inform, and what would change it: Whether the Reporting team funds work next
  quarter on letting analysts avoid rebuilding their filters from scratch. If the sessions show analysts
  losing real, recoverable time to this on most visits, that is enough to fund it. If the sessions show
  analysts adapting quickly, or losing more time elsewhere in the same workflow, the request stays deferred
  and the team looks at whatever the sessions show costs more time instead.
- If this studies something people already use, why it is still discovery work: This studies Acme's
  dashboard as customers use it today, not a concept that does not exist yet. It is still discovery work
  because we are looking for where an opportunity exists inside something already shipped, not grading the
  dashboard against a specification it was built to meet.

## Goals and Research Questions

- Goal(s): Find out where, across a full session, a Recurring Analyst's attention goes to rebuilding
  something rather than reading it. Learn whether rebuilding filters is a meaningful part of that lost time
  or a minor annoyance that gets mentioned mainly because it is the one thing people remember being
  irritated by.
- Research questions (three to five):
  1. Where in a session does an analyst's time go to rebuilding something rather than reading what the
     dashboard already shows?
  2. When an analyst rebuilds filters after the dashboard resets to its default, how often does what they
     rebuild actually match what they meant to be looking at?
  3. What do analysts already do, inside the product or outside it, to avoid rebuilding filters from
     memory?
  4. Does this differ between an analyst who opens the dashboard several times a week and one who opens it
     about once a week?
  5. How often does rebuilding filters come up in a session compared with other repeated actions, like
     exporting a view or sharing one with a teammate?
- Hypothesis, if one stands in for a question: We believe rebuilding filters costs analysts real, recoverable
  time on most visits, not only the visits they happen to complain about afterward; the sessions will tell
  us we are right if most of them show the analyst spending a noticeable stretch rebuilding a filter set
  before getting to anything they actually came to look at.

## What We Already Know

- What the team already knows: The interviews behind the user persona of 2026-01-05 (n=12, held in November
  and December 2025 across 9 mid-market customer accounts) raised a version of this friction independently
  of either deferred request. Nine of the twelve raised wanting to see the same filters they left last week
  without rebuilding them from memory. A separate six-month review of dashboard support tickets, done for
  that same persona work, found 34 tickets using wording like "view reset" or "filters gone." None of that
  prior work watched an analyst actually do the rebuilding; it only asked them about it afterward.
- Assumption this study tests: That the friction the persona interviews raised across nine customer accounts
  generalizes to Recurring Analysts more broadly, and that it costs real time in a session rather than being
  an annoyance people mention when asked but barely notice while working.
- Links to earlier materials: The [Recurring Analyst persona](../user-persona/user-persona_example.md),
  dated 2026-01-05. The FY26 "Time to Insight" company goal, named in the
  [FY26 product strategy](../product-strategy/product-strategy_example.md), dated 2026-01-28, which is the
  company-level goal this study's findings would ultimately serve if the request is funded.

## Method

- Method(s), and why they fit the questions: One-to-one moderated interviews, each built around a walkthrough
  of the analyst's own live dashboard rather than a scripted scenario, because we want to see what an
  analyst actually does with their own data on a day they would normally open it, not how they perform a
  task we hand them. The note taker logs every repeated action the analyst takes during the walkthrough,
  rebuilding a filter included, so the sessions can compare how often each one actually comes up rather
  than relying on what the analyst remembers afterward. This is generative work: the aim is to find where
  the time actually disappears in a session, not to test a fix, since none has been chosen yet.
- Session format and length: About an hour each, over video, with the analyst sharing their own screen and
  walking through whatever they would ordinarily do in a session, narrating as they go.
- What participants will see or use: Their own live Acme Analytics dashboard, in whatever state it happens
  to be in when the session starts. No prototype and no mockup; nothing has been designed yet.
- Generative or evaluative, qualitative or quantitative: Generative, qualitative.
- Where the session guide and screener live: Both are linked under Related Documents, below.

## Participants and Recruiting

- Who qualifies: A Recurring Analyst, using the term as the January persona defines it: looks at the same
  Acme Analytics dashboard on at least a weekly cadence, with no dedicated data-analyst role and no query
  background of their own.
- Who does not qualify: Anyone who took part in the January persona interviews, since this study tests
  whether what they said holds beyond them, and anyone who mainly builds dashboards for other people rather
  than reading one themselves.
- How many participants, and how many recruited as backup: 12 sessions, recruiting 15 to cover anyone who
  drops out or turns out not to qualify once we talk to them.
- How participants are recruited: Direct outreach through the customer success team, to named accounts
  whose usage pattern already matches the persona's weekly-cadence profile.
- How participants are thanked or paid: A 50-dollar account credit, arranged through customer success,
  since participants are customers rather than a paid recruiting panel.
- Access needs you ask about: Whether the analyst needs anything other than a standard video call, including
  a phone-only option, asked at scheduling for every participant.
- How consent is taken: A short spoken statement at the start of each call; what it covers is in Consent,
  Privacy and Ethics, below.

## Tasks and Measures

If this study is not a usability test, say so, name the method, and mark the table and the two lines below
N/A: This is not a usability test. Each session is a walkthrough of the analyst's own dashboard and their
own data, not a set of tasks we hand them, so this section does not apply.

| # | Task (as a scenario) | Success criterion |
|---|---|---|
| N/A | Not a usability test; see the note above | N/A |

- Measures this session will collect: N/A, not a usability test.
- When questions run (before, between tasks, after, or both): N/A, not a usability test.

## Schedule and Logistics

- Dates and session times: Sessions run 2026-05-04 through 2026-05-15, about an hour each, scheduled across
  both weeks to cover analysts in different time zones.
- Place or tool: Video call, on Acme's standard conferencing tool, with the analyst sharing their own
  screen.
- How sessions are recorded and noted: Recorded with consent; a member of Acme's UX Research function takes
  notes live during the call in addition to the recording.
- Pilot session, and with whom: A pilot on 2026-05-01, with a Reporting teammate who has not been part of
  planning this study and is not one of the analysts recruited for it, so the walkthrough format gets tried
  once before it runs on an actual customer.
- Time scheduled for analysis: Two days blocked immediately after the last session, before the readout
  below is drafted.

## Roles and Observers

- Moderator: A member of Acme's UX Research function moderates every session.
- Note taker, if separate: Also from UX Research, live on the call.
- Observers, and how they watch: Priya Nair and a Reporting designer sit in on two calls apiece through a
  shared video link. Any other Reporting teammate may watch a later session live, after reading the session
  guide, and the moderator names everyone watching to the participant at the start of the call.

## Consent, Privacy and Ethics

- How consent is taken, and what participants are told: A short spoken statement at the start of each call,
  covering that the session is recorded, that a UX Research team member is taking notes in addition to the
  recording, who is watching the call, and who will see the recording and the notes afterward.
- What personal data is captured and how it is stored: Recordings and notes are kept in Acme's standard
  research storage, visible only to the UX Research function and the Reporting teammates who observe a
  session.
  No account or billing data is captured as part of the session.
- Legal, accessibility, bias, or power concerns, and how they are addressed: Participants are customers, not
  employees, so no one on the call has authority over their account or contract; sessions are framed to
  participants as separate from their relationship with their own account team. Access needs are asked at
  scheduling for every participant, per Participants and Recruiting, above.
- Organization's retention policy, linked: Acme's standing research-data retention policy, linked in the
  UX Research function's internal space; this plan sets no retention period of its own.

## What Happens to the Findings

- Report or readout, for whom, and roughly when: A short written readout to the Reporting product and
  design team, within two weeks of the last session.
- How it will be structured, if known yet: Not locked yet. It will likely follow where the time went in a
  session, with rebuilding filters counted beside the other repeated actions the note taker logs, but that
  may change once we see what the sessions actually turn up.
- Which decision(s) named above the findings will feed: The funding decision named in Why This Study, and
  the Decision It Informs, above: whether to fund work on this friction next quarter.

## Related Documents

- Session guide: Linked in the UX Research function's shared drive; not reproduced in this plan.
- Screener: Linked in the same shared drive, alongside the session guide.
- Consent form: No separate signed form for this study; the spoken statement in Consent, Privacy and
  Ethics, above, is what each session uses.
- Prototype or test environment: N/A. This study walks through each analyst's own live dashboard, not a
  prototype or a test account.
- Earlier report(s) this follows up on: None. This friction has never been the subject of its own research
  before; What We Already Know, above, names everything the team has on it so far.
