---
title: "Collaborative Analysis Lean UX Canvas"
initiative_name: "Collaborative Analysis"
facilitator: "Priya Nair, PM, Reporting"
status: "active"
date: "2026-09-24"
iteration: "2"
doc_type: lean-ux-canvas
size: lean
source_template: lean-ux-canvas
source_template_version: 0.1.0
---

> **Worked example.** A filled `lean-ux-canvas`, the bundle's only size, for the same Acme Analytics
> product used throughout this library's examples. It frames the FY26 product roadmap's Later-lane item
> 6, "Collaborative analysis" (`../product-roadmap/product-roadmap_example.md`), which that roadmap,
> dated 2026-02-11, carries unshaped and names as possibly not even a problem for this product to solve.
> This canvas's first pass is dated 2026-09-09; the row below records its one revision so far, dated
> 2026-09-24, well before the roadmap's own 15 October 2026 review trigger, and it cites no document
> dated after itself. It draws on the
> [FY26 product strategy](../product-strategy/product-strategy_example.md) (2026-01-28) for the
> Recurring Analyst and for the second-view metric this canvas's own outcome deliberately does not
> ladder to, and on the internal announcement
> (`../announcement-internal-comms/announcement-internal-comms_example.md`, 2026-07-18) for Saved Views
> sharing already being live for Acme's own Reporting squad. Per the `discovery-docs` family contract's
> second cadence exception, this canvas stays open while its own experiments run; it has not yet
> committed to building, changed course, or stopped the initiative.
>
> All figures are illustrative. They are internally consistent with the other examples in this library
> and are not drawn from a real company.

# Collaborative Analysis Lean UX Canvas

## Business Problem

Acme's FY26 roadmap has carried "Collaborative analysis" in its Later lane since February, unshaped,
with a line admitting it might not even be this product's problem to solve. Since then, Support has kept
bringing back the same pattern: an analyst at an account works out an answer, and weeks later a different
analyst at the same account asks Support the identical question, with neither one aware the other already
did the work. In a two-week sample Jordan Ames, Support Lead, pulled in late August, 9 of the
26 "how do I read this" tickets Support closed turned out, on a second look, to be a question
someone else at the same account had already answered on the same dashboard (illustrative counts from
that one sample). Nothing about any single dashboard causes this; it is the same quiet gap, repeated,
account after account, and nobody has owned finding out whether fixing it is worth the effort. How might
we let an analyst find out that a teammate already has their answer, before either one spends time on it
again?

## Business Outcomes

This outcome does not ladder to the roadmap's own headline measure, the share of new accounts that build
a second view within 14 days, from a 31 percent baseline to 50 percent: that number is about a new
account's first two weeks, and every account in Jordan Ames's sample above had already cleared 14 days,
most of them by months. The behavior this initiative wants instead: at an account where a fix has shipped,
an analyst who hits a question a teammate already answered reuses that earlier answer, rather than opening
a new Support ticket or redoing the analysis from scratch, in at least 70 percent of such repeats within 30
days of the fix going live (illustrative target; no fix exists yet to measure a baseline against).

## Users

The Recurring Analyst, the person the FY26 product strategy describes by what they lack, someone who owns
a number, answers questions about it weekly, and has no data team behind them, and whom documents after
it, this one included, name by behavior. Specifically, that analyst on the day they ask a
question a teammate at their own account already answered. And that teammate, also a Recurring Analyst,
whose earlier answer nobody currently surfaces to anyone else. Also affected: Acme's own Support team, who
field the escalation today when neither analyst finds the earlier answer on their own, and who absorb the
repeated work this initiative exists to remove.

## User Outcomes and Benefits

An analyst who half-recognizes a question wants one thing before anything else: to find out fast whether
this has already been worked out, so they can trust that earlier answer and move straight to acting on it,
rather than feel like they are starting from zero or interrupting a teammate to ask something that teammate
may not even remember answering. The job is not "get an answer" in the abstract; it is "stop redoing work
someone at my own company already did," and the small embarrassment of asking a colleague a question they
already answered once is, if anything, a bigger push toward checking first than the time it would save.

## Solutions

- A searchable log of previously answered questions, tied to the dashboard they came from, that an analyst
  can check before asking anyone else. Acme has no index like this today.
- A prompt inside the dashboard itself, shown when an analyst's typed question looks close to one already
  on file for that account, pointing at the earlier answer instead of letting the analyst start writing a
  new one from a blank state.
- Not duplicating Saved Views: that capability, live for Acme's own Reporting squad since July, lets one
  person hand a teammate their exact filter state, but it depends on the second analyst already knowing a
  saved view exists and going looking for it. The pattern Support brings us shows that second step is
  exactly the one that is not happening.
- Non-technical: route repeat questions through Support's own triage instead of building anything new.
  Jordan Ames's team already checks whether a question has come in before when they pick up a ticket; the
  gap is only that an analyst gets no benefit from that unless they go to Support first, which most of
  them do not.
- Non-technical: a standing monthly review between Support and the Reporting squad that simply tracks how
  often this pattern recurs, before either team commits engineering time to it.

## Hypotheses

| ID | Hypothesis (business outcome, user, benefit, one feature) |
|---|---|
| H-01 | We believe 70 percent of repeated questions will be reused rather than re-asked if the Recurring Analyst gets a fast way to trust an earlier teammate's answer from a searchable answer log tied to the dashboard. |
| H-02 | We believe 70 percent of repeated questions will be reused rather than re-asked if the Recurring Analyst gets that same trust, surfaced at the moment they start typing, from an in-dashboard prompt that flags a question close to one already on file. |
| H-03 | We believe 70 percent of repeated questions will be reused rather than re-asked if the Recurring Analyst gets that same trust, found for them by Support, from routing every repeat question through Support's existing triage process. |

The monthly Support and Reporting review in Box 5 has no hypothesis, because it would measure the
pattern rather than change it. *Added 2026-09-24:* H-03 alone cannot carry the outcome in Box 2, since
most repeats never reach Support (see the revision row). Support's triage keeps running as a stopgap.

## What We Need to Learn First

Now H-02. The first pass chose H-03, the cheapest to try because it builds nothing, and its test is in the
revision row below. That test showed most repeats happen before an analyst would ever think of Support,
so the in-dashboard prompt is the only candidate that reaches an analyst before they decide whom to ask.
Its riskiest assumption is not whether a close match can be found; Support already finds earlier answers
by hand. It is whether an analyst who is shown an earlier teammate's answer at the moment they start
typing will stop, read it and trust it enough to reuse it, rather than dismiss it and carry on writing.
That is a risk to whether analysts value the pointer when it interrupts them, not a risk to whether the
product can match questions.

## The Least Work to Learn It

Planned for two weeks from 2026-09-28, with no prompt built. At five accounts that agree to take part, a
Reporting squad member watches the questions analysts type into the product's existing help search. When
one looks close to a question a teammate at the same account already answered, they send that analyst an
in-app message within a few minutes, pointing at the earlier answer. The test counts how many analysts
open the pointer, and how many reuse the earlier answer rather than carry on building their own. The
pointer is sent by a person, so the test learns whether analysts value the interruption before anyone
builds the matching that would send it automatically.

## Revisions and What Takes Over

| Date | Assumption tested | What was learned | Boxes changed |
|---|---|---|---|
| 2026-09-24 | H-03's riskiest assumption: whether an analyst would detour to Support's pointer rather than rebuild an answer themselves. For two weeks from 2026-09-09, Support tagged every ticket Jordan Ames's team could identify as a likely repeat and replied with a one-line pointer to the earlier answer, with no new tooling. The same reply asked two questions: would you have checked here yourself first if you had known to, and how many times this month did you ask a teammate or redo work instead of opening a ticket? | Partly held and partly did not. Of the 11 analysts whose tickets were tagged as repeats, 9 said they would have checked a pointer first if they had known to look. But their answers to the second question put the repeats that never reach Support, asked of a teammate or silently redone, at several times the ones that did (illustrative counts). Routing through Support alone will not move most of the repeats this initiative cares about. | The prompt candidate, H-02, moved into Box 7, because it is the only candidate that reaches an analyst before they choose whom to ask. Box 8 now plans a test of it that builds nothing. Box 6 gained a dated note that H-03 alone cannot carry the outcome in Box 2. |

**What takes over when this canvas is finished**, because the team committed to building, changed course,
or stopped the initiative: not yet decided. The canvas stays open while the next test, on H-02's riskiest
assumption, runs. If that test holds up, a design brief would hand the chosen concept to the people who
design it. If it does not, Support's triage from the first test
is cheap enough to keep running on its own, which would count as the team changing course rather than
committing to build anything new.
