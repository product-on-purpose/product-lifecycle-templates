---
title: "Saved Views Epic"
epic_name: "Saved Views"
owner: "Priya Nair (PM, Reporting)"
status: active
target_timeframe: "By the end of Q3 2026, the close of the FY26 roadmap's Now lane"
related: ["../prd/prd_example.md (Saved Views for Dashboards PRD, created 2026-06-12)", "../product-strategy/product-strategy_example.md (FY26 product strategy, agreed 2026-01-28)", "../product-roadmap/product-roadmap_example.md (FY26 product roadmap, agreed 2026-02-11; this epic fills its Now lane)"]
doc_type: epic
size: full
created: "2026-06-13"
updated: "2026-06-17"
source_template: epic
source_template_version: 0.1.0
---

> **Worked example.** A filled `epic`, full variant, for the same "Saved Views" work later covered by the
> [Saved Views PRD](../prd/prd_example.md) it groups, and by the
> [product backlog](../product-backlog/product-backlog_example.md), the
> [user stories](../user-stories/user-stories_example.md), the acceptance criteria, the release notes, and
> the [Saved Views design document](../sdd/sdd_example.md) that follow it. It is dated one day after the PRD
> entered review, before any of those five documents existed and before a single story had been written up:
> the Child Stories table below reserves the `SV-*` numbering the product backlog later assigns real statuses
> to, and the Acceptance Criteria section states the same four-item gate (save, load, default, share) that
> the [DEF-2291 postmortem](../incident-postmortem/incident-postmortem_example.md) later finds a gap in, at
> the aggregate level, when it is triaged on 2026-07-13. Reading this example after those siblings shows
> where their facts came from; reading it first is closer to what the team actually had in hand when the
> epic was opened. Figures marked "illustrative" are made up for the example.

# Saved Views Epic

## Title and Narrative Summary

Dashboards in Acme Analytics always reopen in the same blank default state, so anyone who checks the same
slice of data every day pays a small setup tax before they can do anything useful with it. This epic groups
the work needed to let a person capture that setup once, under a name, and get it back without redoing it: a
saved combination of filters, date range, and visible columns that survives between visits and, for a Team
Lead, can be handed to a whole team so everyone starts from the same numbers.

As a Recurring Analyst, I need my usual filters to survive between visits, so that opening a dashboard puts
me back where I left off instead of back at zero.

## Goal and Context

This epic exists because of the 2026-05 Reporting friction study, which turned a long-standing assumption
("re-filtering just works") into a measured cost: across the twelve analysts interviewed, reassembling a
filter set was the single most frequent repeated action inside a dashboard, ahead of both export and share,
and three kept a personal note of "the filters I always use" rather than trust the dashboard to remember
them. The request had been deferred twice before as a nice-to-have; the study is what reframed it as a
recurring tax on exactly the people the product exists to serve.

It ladders up to the FY26 "Time to Insight" company goal, which the
[FY26 product strategy](../product-strategy/product-strategy_example.md) set out in January and the
[FY26 product roadmap](../product-roadmap/product-roadmap_example.md) placed in its Now lane the following
month: cutting the time between opening a report and doing something with it. A quarter after this epic
ships, the honest test is whether a Recurring Analyst's first move on opening a dashboard is reading the
data in front of them, not reassembling the lens they need to see it through.

## Scope

Scope is everything the PRD's six functional requirements ask for on top of the dashboard's existing filter
engine, plus one enabling piece none of them can ship without. In pull order: a durable place for a saved
view to live; letting a user capture the dashboard's current filters, date range, and columns under a name
(FR-1); switching between that user's own saved views in one action (FR-2); marking one view a default that
loads automatically (FR-3); making a view visible to a teammate who already has access to the same dashboard
(FR-4); letting the owner rename or retire a view (FR-5); and, lowest priority, flagging a shared view when
the dashboard underneath it has since changed (FR-6, a Could). Everything above operates on state the
dashboard already holds; nothing in this epic touches how the dashboard itself is built.

## Child Stories

The rows below reserve the `SV-*` numbering this epic expects to use once each is written up in full; the
product backlog and the story set will carry the same IDs forward rather than renumbering them later.
Ordered by the sequence each is expected to be pulled, not by the FR list above.

| ID | Story | Status |
|---|---|---|
| SV-1 | Give a saved view somewhere durable to live | Not started |
| SV-2 | Save the dashboard's current state under a name (FR-1) | Not started |
| SV-3 | List a user's own views and switch between them (FR-2) | Not started |
| SV-4 | Set one view as the dashboard's default (FR-3) | Not started |
| SV-0 | Spike: confirm the sharing permission model holds before building on it | Not started |
| SV-5 | Share a view with a team, permission-checked (FR-4) | Not started |
| SV-6 | Let an owner rename or retire their own view (FR-5) | Not started |
| SV-7 | Flag a shared view whose dashboard has since changed (FR-6, Could) | Not started |

## Acceptance Criteria

- [ ] Saving captures the dashboard's current filters, date range, and visible columns under a name the
      owner chooses.
- [ ] Loading a saved view restores that exact configuration in one action, with nothing left to rebuild
      by hand.
- [ ] Marking a view as the default means the dashboard opens already in that configuration, with no
      extra step.
- [ ] A teammate who already has access to the dashboard can pick a view its owner marked shared and see
      the same slice of data.

## Out of Scope

Three things came up during discovery and are staying out on purpose, each traceable to a non-goal already
named in the PRD rather than invented for this document. Scheduling a view for delivery by email or Slack
is deferred; it sits as a parked backlog idea rather than a story inside this epic, and would only move in
if that non-goal were lifted. A "global" view spanning more than one dashboard is deliberately not being
built either, because it opens permissions questions this epic has no reason to answer yet. And nothing
here touches a dashboard's own structure: a view remembers how someone looked at a dashboard, not what the
dashboard is built from, so changing chart types, available columns, or the underlying query stays entirely
outside this epic.

## Dependencies

| ID | Dependency | Type | Severity | Owner (this side) | Owner (other side) | Status |
|---|---|---|---|---|---|---|
| D-01 | Read access to the per-user preferences store the Platform team shipped in Q1 | Technical | Blocking (resolved) | Marcus Bell (Staff Engineer, Reporting) | Dana Osei (Staff Engineer, Platform) | Done |
| D-02 | A permissions check the sharing story (SV-5) can call before it ships | Technical | Blocking | Marcus Bell (Staff Engineer, Reporting) | Dana Osei (Staff Engineer, Platform) | Confirmed, integration pending |
| D-03 | An updated menu component from the shared design system for the Views control | Technical | Informational | Priya Nair (PM, Reporting) | Elena Cho (Design Systems) | In progress |

## Link Upward (Initiative, Theme, or nothing)

Acme's own tracker does offer an Initiative tier above Epic, but Reporting has never populated one for this
body of work. The answer that actually gets used when someone asks what this ladders up to is the FY26
roadmap's Now lane and the "Time to Insight" company goal underneath it; those are the documents a person
would be pointed at, not a tracker field nobody keeps current. So: no Initiative record for this epic, by
choice rather than oversight.
