---
title: "Saved Views Design Brief"
concept_name: "Saved Views"
author: "Priya Nair, PM, Reporting"
approver: "Dana Okoro, VP Product"
status: "in design"
last_updated: "2026-06-01"
doc_type: design-brief
size: full
source_template: design-brief
source_template_version: 0.1.0
---

> **Worked example.** A filled `design-brief`, full variant, for the same Acme Analytics product used
> throughout this library's examples. Per the discovery-docs family contract, this document hands the Saved
> Views concept to the people who will design it: it is dated 2026-06-01, after the 2026-05 Reporting
> friction study that surfaces the problem below, and before the
> [Saved Views PRD](../prd/prd_example.md) of 2026-06-12 that later specifies the concept this brief hands
> off. It also follows the [user persona](../user-persona/user-persona_example.md) that names the Recurring
> Analyst, dated 2026-01-05, well before either of those. Nothing in the body below names a screen, a
> button, or a flow; that belongs to the document this brief hands off to. Nothing below cites the PRD, or
> any later Saved Views document, as already existing, because none of them did yet when this was written.
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company.

# Saved Views Design Brief

## The Challenge

Analysts who track the same slice of data, one region, one product line, a trailing window, have to
re-apply that same filter set every time they come back to a dashboard, because the dashboard always opens
in its default state rather than where they left it. The 2026-05 Reporting friction study found this
re-filtering was the single most frequent repeated action on the dashboard, ahead of both exporting and
sharing. We have deferred addressing it twice before, because filtering itself "worked"; the study is what
reframed it from a feature gap into a recurring time tax paid on every visit. Nothing about the data model
blocks fixing it now, since per-user preferences storage shipped in Q1.

- What a good outcome would change: An analyst returns to a dashboard already looking the way they left it,
  without rebuilding anything first, so the time that currently goes into reconstructing a lens goes into
  reading what it shows instead.
- Problem statement already written, if one exists: None. This friction was not framed as its own problem
  statement; it surfaced directly from the 2026-05 friction study cited above, and this brief is the first
  document to frame it.
- Where success will be measured, if already defined elsewhere: Not yet defined for this concept
  specifically. The FY26 "Time to Insight" company goal (reduce the median time from opening a report to
  acting on it) is the measure this concept is meant to move, but no concept-level target has been set; that
  will follow once the concept below is designed and specified.

## Who It Is For and What We Learned

- Who the design serves: Primarily the **Recurring Analyst**, who returns to the same dashboards daily or
  weekly and works within a stable set of filters. Secondarily, a **Team Lead** who wants their team looking
  at one agreed view rather than each person's own reconstruction of it; this is Priya's own naming of a
  second audience from the friction study, not a separately documented persona. Not designed for the
  one-time explorer, who rarely returns often enough to benefit from saving anything.
- Existing persona, if one already describes this group: the
  [Recurring Analyst](../user-persona/user-persona_example.md#who-they-are), defined in the 2026-01-05 user
  persona built from twelve interviews held in November and December 2025. No persona document exists yet
  for the Team
  Lead; this brief carries that audience only as far as the friction study described it.
- Research insight the challenge rests on: The friction study interviewed 12 analysts; 9 of them described
  rebuilding filters by hand several times a day, and 3 kept a personal text file listing "the filters I
  always use" so they would not have to rely on memory (illustrative counts from the 12-person study). The
  cost is not only the minutes spent rebuilding: a filter set incorrectly from memory, after the dashboard
  resets to its default, risks an analysis of the wrong slice.

## The Chosen Concept

- Candidates weighed, and why each was set aside: Letting the dashboard silently remember and auto-restore
  each analyst's own last-used filters, set aside because it helps the person who set the filters but gives
  a Team Lead no way to hand teammates a consistent view, and because the study's own workaround, a named
  personal list of go-to filters, shows analysts already think of a good state as something worth naming and
  returning to deliberately, not something that should just happen invisibly. Encoding the current filter
  state into a shareable link, set aside because today's dashboards do not carry filter state in their URLs
  at all, so building this would mean rebuilding the dashboard's routing before touching the actual problem,
  a scope well past what this concept needs to answer.
- Chosen concept: Give an analyst a way to name, save, and reopen a dashboard's current lens, its filters,
  date range, and visible columns, and to share a named lens with a teammate or a team.
- Why this one: It answers both halves of the research insight above directly: an analyst gets back the
  exact slice they left, named rather than reconstructed from memory, and a Team Lead gets a lens they can
  hand to their team instead of describing it from scratch each time. It also builds on ground that already
  exists, per-user preferences storage, rather than requiring new infrastructure the way the link-based
  candidate above would have.
- What this concept deliberately leaves out: Automated or scheduled delivery of a saved lens by email or any
  other channel; someone hearing "share a lens" might assume it gets pushed to a teammate on a schedule, and
  this concept does not do that. One lens applying across more than one dashboard at once; someone who hears
  "save my view" might expect it to follow them everywhere, and this concept only ever saves a lens for the
  single dashboard it was captured from. Any change to what a dashboard itself measures or contains; someone
  might assume a saved lens could reshape the dashboard underneath it, and this concept only ever captures
  how an existing dashboard is being looked at, never what it reports.

## Constraints on the Design

| Constraint | Why it limits the design work |
|---|---|
| Lenses are saved and reopened inside the existing dashboard product | Acme ships one dashboard product today, and a separate place to keep lenses would mean most analysts learning and switching between two tools to do one job |
| A shared lens can never surface data to a teammate they could not already see on that dashboard themselves | The dashboard's existing permission boundaries are a given the design must work inside, not a question it gets to reopen |
| Must meet whatever accessibility standard Acme's dashboards already hold to | The persona interviews behind this brief already surfaced a colorblind hub lead who raised, unprompted, that the trend chart's two lines print in the same shade of blue on a handout; any new control this concept adds must not repeat that failure, though the exact pass or fail criteria are for the specification that follows to state |

## Open Questions for Design

- Open questions: Who owns a shared lens. If only the analyst who saved it can change it, a Team Lead's
  agreed view stays fixed; if any member of the team can update it, it stays current but can drift from what
  the Team Lead agreed. A second question is what a saved lens should do when the dashboard it came from
  changes later, for example when a column it shows is removed. The friction study asked neither question.
- Assumptions: Analysts will name their own lenses. The study's three analysts who kept a personal list of
  "the filters I always use" support this, but three people are not enough to settle it. If design finds
  that analysts would rather not name anything, naming is the first part of the concept to revisit.
- What could block the design work: Whether a dashboard's current filter state can be reliably read back and
  reapplied across every report type Acme ships, not only the small set the friction study happened to
  cover; the Reporting team has not yet confirmed this holds everywhere.

## The Handoff

- Who will design from this brief, and what they receive: Acme's Reporting product design team, led by
  Marcus Webb, Design Lead, Reporting. They receive this document plus the full interview notes behind the
  2026-05 Reporting friction study.
- Approved by, and when: Dana Okoro, VP Product, 2026-06-01. This records that design on the chosen concept
  may begin; it grants no project budget and no funding decision.
- How this brief stays current while design runs, and which review that means: Priya Nair keeps this
  document current. When design settles who owns a shared lens, or finds a report type where a lens cannot
  be restored, she records the answer here with its date, and Dana Okoro's approval above stands without a
  new signature. Marcus Webb's team reviews the design itself at its own critique every two weeks; this
  brief does not schedule that review.
- Who decides when feedback on the design conflicts: Marcus Webb, Design Lead, Reporting, distinct from Dana
  Okoro's approval above, which covers only whether design may begin.
- What takes over once the concept is specified: The Saved Views PRD that Priya Nair will write once the
  concept above is designed. It does not exist yet.

## The Handoff's Scope, Time Line and Budget

- Scope of the design work handed off: Saved Views as a designed concept that a specification can be
  written from. It covers what a lens holds, how an analyst gets back to one, and what a teammate receives
  when a lens is shared. Reading and restoring a dashboard's state is engineering work, and the Reporting
  team owns it, including the blocker named above.
- When this work should finish: By 2026-06-10, so a specification can be drafted against a finished concept
  rather than a moving one.
- Budget set for the design work alone, or a statement that none exists: None exists. The design time
  comes from the hours Marcus Webb's team already plans for Reporting this quarter, and no separate amount
  was requested.
