---
title: "Acme Analytics Competitive Analysis"
product: "Acme Analytics"
owner: "Dana Okoro, VP Product"
customer_segment: "the Recurring Analyst"
current_version: "v2"
status: "agreed"
last_updated: "2026-03-12"
doc_type: competitive-analysis
size: full
source_template: competitive-analysis
source_template_version: 0.1.0
---

> **Worked example.** A filled `competitive-analysis`, full variant, for the same Acme Analytics product
> used throughout this library's examples. Per [ADR 0091 (competitive analysis joins strategy-docs as an
> eighth member)](../../docs/internal/decisions/0091-competitive-analysis-joins-strategy-docs-as-an-eighth-member.md),
> this type sits after the [FY26 product strategy](../product-strategy/product-strategy_example.md) and
> immediately before the [positioning statement](../positioning-statement/positioning-statement_example.md).
> That place is this library's own position, and no source states the sequence. The first version is
> dated 2026-01-29, one day after the strategy (2026-01-28) whose segment it takes and one day before the
> positioning statement (2026-01-30), so the positioning statement was built on a current analysis. The
> version shown is v2, dated 2026-03-12, a refresh prompted by a release of the kind the positioning
> statement's revisit list names. Dana Okoro, VP Product, owns the strategy, the positioning statement
> and this document, which is why the three speak in one voice.
>
> Its customer evidence is the interview set recorded in the
> [user persona](../user-persona/user-persona_example.md). Its two named rivals, Brackenfield BI and
> Plumline, are fictional, and the library names no real vendor here: the positioning statement example
> records that no single alternative recurs often enough in lost deals to name by brand, so the rivals
> are stand-ins that give each rating a page to read. No published, filled-in competitive analysis was
> read while this bundle was built, so this example demonstrates the template's shape and is not copied
> from observed practice.
>
> All figures are illustrative. They are internally consistent with the other examples in this library and
> are not drawn from a real company. Any figure shared with an earlier example, the 31 percent baseline
> and the persona's interview counts above all, repeats that example's own number exactly.

# Acme Analytics Competitive Analysis

## Purpose and Scope

- The customers this covers, and the strategy segment they come from: the Recurring Analyst, the target
  segment of the FY26 product strategy. This is someone at a 50-500 person company who owns a number,
  answers questions about it weekly, and has no data team behind them. The strategy names the same
  person the unaccompanied analyst. Downstream documents use one name, so this one says Recurring
  Analyst throughout. The strategy's two non-targets, enterprise data-platform teams and the
  embedded-analytics OEM channel, are outside this analysis.
- The decisions this analysis informs, and who makes them: Dana Okoro makes all three. The first was v1's
  only job: which alternatives the positioning statement may name, and what it may claim against each.
  The second is whether the roadmap's order still holds once rivals are rated on what this segment
  values. The third is whether any finding is strong enough to go to the strategy as a proposal. If a
  rival were ahead on something this segment weights heavily, we would first check whether the roadmap
  already covers it. We would not reopen the strategy's guiding policy on the strength of a rival's page.
- Who reads it, and what they will do with it: Dana Okoro reads all of it before each decision above.
  Product marketing and sales leadership read the competitor set and the status quo row when they use
  the positioning statement. Priya Nair (PM, Reporting) reads comparison rows 1 to 3 when she shapes
  work on the reporting surface. No talk track for sales is derived here.

## The Competitor Set

Tier 1 is what a Recurring Analyst reaches for when a question comes up, as the persona interviews and
the sales team's lost-deal notes show. A Tier 2 would be a rival we watch and no customer yet weighs.
There is none in v2.

| Competitor or alternative | Kind | Tier | Why it is in the set |
|---|---|---|---|
| The shared analytics inbox, a copied spreadsheet and a colleague's favour, taken together | Status quo | Tier 1 | What the Recurring Analyst does today when a question comes up and nothing has been bought. The product vision calls it the real incumbent, and 8 of 12 persona interviewees named asking an analyst and waiting as the only path when the dashboard cannot answer |
| Brackenfield BI (fictional, illustrative) | Direct | Tier 1 | A general-purpose BI tool, read as a stand-in for the category the positioning statement names. It appears once in the last two quarters' lost-deal notes, as Plumline does, so neither earns a name in the positioning statement. We read it so that each rating has a page and a demo behind it |
| Plumline (fictional, illustrative) | Direct | Tier 1 | A second general-purpose BI tool, lighter than the first, read so that one vendor's habits do not stand for the whole category |

- Rivals looked at and left out of the set, each with the reason:
  - **Enterprise data-platform vendors.** The strategy's first non-target. They sell on governance,
    lineage and modelling depth, which this segment does not buy.
  - **Embedded-analytics vendors.** The strategy's second non-target, the OEM channel. They sell to the
    software vendor and not to the operator. Acme's separate embedded-analytics canvas, dated
    2026-01-21, holds that line of business as its own product.
  - **SQL-first tools and warehouse consoles.** Read on 2026-01-29 and left out, because the persona
    interviews describe people with no query background. They come back in if the lost-deal notes start
    naming one.

## Competitor Profiles

| Competitor | Customers it serves | What it offers | How it charges | Where it wins | Where it falls short | How it differentiates |
|---|---|---|---|---|---|---|
| Status quo: inbox, spreadsheet, favour | Every Recurring Analyst, before anything is bought | A shared analytics inbox where questions queue, a spreadsheet copied from an export, and whichever colleague can build the view | No licence fee. The cost is the wait and a favour owed. Hours lost per question: unknown, because nobody has timed it | Nothing to learn and nothing to approve. The asker works in columns she already knows | The copy diverges from its source, and every new question waits on someone else's free time. It is also a workaround for the dashboard's reset, a pain and not a win: 6 of 12 interviewees keep a personal spreadsheet of last week's filter values to rebuild the view | It does not differentiate. It is already there |
| Brackenfield BI (fictional) | Companies with someone who models data for everyone else (its customer pages, read 2026-01-29) | Dashboards, scheduled reports, saved views, a long connector list and a modelling layer. Since 2026-03-03, a guided mode for that layer | By annual contract. Its pricing page shows a quote form and no figure, so the price of every tier is unknown (read 2026-01-29 and 2026-03-05) | Saved views that persist, the longer of the two connector lists, and, by the vendor's own claim, a wide choice of charts | Data is copied into its own store and modelled by someone first. The guided mode proposes a join, and both testers stalled at deciding what one row of the result should mean (tested 2026-03-10) | Breadth: any source, any chart (its home page, read 2026-01-29) |
| Plumline (fictional) | Small teams (its home page, read 2026-01-29) | Dashboards from an uploaded file or from one of a few connectors, with saved views | A free tier, and a paid tier priced by the number of uploaded rows (its pricing page, read 2026-01-29, not re-read for v2). The paid price at the data volume of a 50-500 person company: unknown | A first chart from one file soon after upload, which its page states and we did not time | A question across two sources needs a manual join, and the data must be uploaded or connected before any question | Speed to a first chart (its home page, read 2026-01-29) |

## Competitor Briefs

### The status quo: inbox, spreadsheet, favour

- The rival: the shared analytics inbox, a copied spreadsheet and a colleague's favour, taken together.
- The three things it does that the chosen customers value: it asks nothing of the person who starts,
  since she already knows her own columns. It needs no approval and no purchase. It lets a person with a
  half-formed question begin the moment she has an export.
- The three needs it leaves unmet: a new question answered without waiting on a person. A number that
  stays tied to its source, because the copy diverges. An answer inside the session in which the
  question came up.
- When a chosen customer would reasonably pick it over us: when the question is a one-off, the data is
  already in a file on her desk, and nobody's time has to be borrowed.

### Brackenfield BI

- The rival: Brackenfield BI (fictional, illustrative), standing in for general-purpose BI tools.
- The three things it does that the chosen customers value: a view she builds stays built, and reopens
  with its filters set. Standing reports that reopen the same way each week. And, labelled as what it
  leads with and not shown to be valued, a long connector list.
- The three needs it leaves unmet: a new question without waiting for someone to model the data. A start
  that does not ask her to decide what one row of the result means. An answer from data left where it
  lives, since its data is copied in first.
- When a chosen customer would reasonably pick it over us: when the company already has a person who
  models data, the reports are standing ones asked the same way every week, and the views must survive
  untouched from one Monday to the next.

### Plumline

- The rival: Plumline (fictional, illustrative), the lighter of the two BI stand-ins.
- The three things it does that the chosen customers value: a view that persists. A quick path from
  one file to one chart, on its own account of itself. And, labelled as what it leads with and not
  shown to be valued, a free tier.
- The three needs it leaves unmet: a question across two sources without a manual join. Data kept where
  it lives, since it must be uploaded or connected first. A first answer to a question nobody has
  framed as a file yet.
- When a chosen customer would reasonably pick it over us: when her question lives in a single export,
  she wants it kept on screen week after week, and she has no wish to connect anything.

## Comparison on What Customers Value

| What customers value | Weight | Where the weight came from | Us | Brackenfield BI | Plumline | Status quo |
|---|---|---|---|---|---|---|
| Get an answer to a new question without asking anyone | High | 8 of 12 persona interviewees named asking an analyst and waiting as the only path when the dashboard cannot answer | Part-way | Blocked (tested) | Part-way (page) | Part-way (her own spreadsheet only) |
| Start without learning how the data is laid out | High | The session recordings behind the 31 percent figure: 9 of 14 reviewed went back to documentation before abandoning | Part-way | Blocked (tested) | Part-way (page) | Alone |
| Return to a view with the filters still set | High | 9 of 12 persona interviewees wanted last week's filters kept. A six-month review found 34 support tickets using wording about a view resetting or filters gone | Blocked | Alone (page) | Alone (page) | Part-way |
| Ask the question where the work already is, without copying the data out first | Medium | 8 of 12 interviewees named the wait, and the persona records its cost as questions that go unasked. That the wait comes from copying data out is Acme's reading and not something interviewees said, so the weight is Medium and not High | Alone | Blocked (page) | Blocked (page) | Blocked |
| Connect to every system the company uses | Low | Nobody was asked. The weight rests on where the recordings put the drop, at the dataset picker and not at connecting a system, so it may be wrong | Part-way | Alone (page) | Part-way (page) | Part-way |
| Trust a number without checking it somewhere else | unknown | The strategy names trust as its alternative diagnosis, and the lapsed-trial interviews it commits to for 2026-03-20 have not reported | unknown | unknown | unknown | unknown |

- The rating scale, stated once. For a row of the comparison, **Alone**: a Recurring Analyst finishes it in
  one session with nobody's help, on the questions we tried. **Part-way**: she finishes it alone on some
  of the questions tried or in some set-ups, and not on all. **Blocked**: she finishes it alone on none
  of the questions tried, even if she completes some of its steps. **unknown**: not tried, and not found
  on any page. For a job in the scorecard below, the levels count steps instead: Alone is every step
  done alone, Part-way is at least one step alone and at least one not, and Blocked is no step alone.
  "Tested" marks a cell resting on the 2026-03-10 trial of Brackenfield BI. "Page" marks a rival's cell
  that rests on its public pages only and was not tried: the vendor's page claims that level and
  nobody tried it. Every other cell is Acme's own reading of its
  own product, or of the status quo as the interviewees described it.
- Criteria on which a rival leads and the chosen customers weight lightly, and what you decided about
  them: Brackenfield BI leads on connecting to systems (row 5), the weight is Low, and Plumline is level
  with us. We keep the row, so the reason stays visible, and we hold the strategy's line of four
  committed connectors and no more. Row 3 is a different case. Both BI tools lead there, but the weight
  is High, so it is a finding and not a decision to leave alone. The status quo also leads us on row 2,
  a High-weight row. That is the strategy's own diagnosis (self-serve begins at the schema), and the
  roadmap already holds that work. See Implications.

## Jobs-Based Scorecard

| Job the customer is trying to get done | Importance to the customer | How well we help | How well Brackenfield BI helps | How well Plumline helps | How well the status quo helps |
|---|---|---|---|---|---|
| Answer a question about my own number in the session where it came up, then act on the answer (steps: get the data in place, ask, read, act) | High: 8 of 12 interviewees named asking an analyst and waiting as the only path | Part-way, 3 of 4 steps alone. Helps with getting the data in place, since it is read where it lives, with reading, and with acting. Misses asking, which still begins at the schema | Part-way, 2 of 4. Helps with reading and acting (page). Misses getting the data in and asking, since it is copied and modelled first (tested) | Part-way, 3 of 4 on a one-file question. Helps with getting one file in, reading and acting (page). Misses asking across two sources | Part-way, 2 of 4. Helps with asking, in her own columns, and with reading. Misses current data, since the export is a copy, and acting when it needs someone else's time |
| Run the Monday review from last week's setup, and say why a number moved before the VP asks (steps: reopen the view, refresh it, set it beside last week, find the cause) | High: 11 of 12 wanted the number ready before the Monday review without asking anyone for it, 9 of 12 wanted last week's filters kept, and 7 of 12 raised being first to name a drift | Part-way, 1 of 4, with 1 unknown. Refreshes with current data. Misses reopening, since the view resets. Setting it beside last week: unknown, not checked. Finding the cause is a new question, so it meets the limit in row 1 | Part-way, 2 of 4, with 1 unknown. Helps with reopening and refreshing (page). Setting it beside last week: unknown, not found on its pages. Misses finding the cause, which meets its modelling limit | Part-way, 2 of 4, with 1 unknown. Helps with reopening and refreshing (page). Setting it beside last week: unknown. Misses finding the cause across two sources, which meets its manual join | Part-way, 2 of 4. Helps with reopening, since a file keeps its filters (Acme's reading, with no interview count), and with comparing by hand. Misses refreshing, which is a new export, and finding the cause, which is asking someone |

Each job spans two comparison rows and adds a step that no comparison row holds. The first job ends in
acting on the answer, and the second asks for a comparison against last week. That is why neither is a
criterion renamed.

## Implications for Our Direction

| Finding | Routes to | The move | Owner | By when |
|---|---|---|---|---|
| How much the segment weights trust in the number is unknown (row 6), and the strategy's alternative diagnosis rests on it | Strategy | Read the lapsed-trial interviews for what people said about trust, and set row 6's weight. Send the strategy a proposal only if that weight turns out High | Dana Okoro | 2026-03-27 |
| Both BI tools lead on returning to a view, a High-weight row on which we are Blocked (row 3) | Roadmap | Keep Saved Views in the Now lane, and ask that its specification cite this row, so that the work stands on what the segment weights and not on the fact that two rivals have it | Priya Nair (PM, Reporting) | 2026-05-01, the start of Q2 |
| Brackenfield BI leads on connecting to systems, and the weight is Low (row 5). This confirms the current direction | Strategy | No proposal. The four committed connectors stand. We would change our view if the lapsed-trial interviews show people stopping at connecting a system, so the same read settles it | Dana Okoro | 2026-03-27 |
| Brackenfield BI's guided mode, released 2026-03-03, is not yet a modelling layer "that a non-analyst can complete alone": neither of two testers finished a two-table model (rows 1 and 2). Had either finished alone, we would have opened the positioning statement's because-clause | Positioning statement | No change to the statement. Record the check as "not met", and run the same two-table test again after the vendor's next modelling release | Dana Okoro | 2026-09-15, a month before the strategy review, or sooner if a release lands |
| We lead on one row only, row 4, and it carries the positioning statement's differentiator. Its weight is our reading and not something customers said. The status quo leads us on row 2, which the comparison section explains | Positioning statement | No change to the statement, because no row contradicts it. Plumline needs no modelling step for a one-file question, so the statement's "unlike" clause rests on the copy-out difference (row 4) for that rival, not on modelling. Read the lapsed-trial interviews for any mention of exporting or copying data, and set row 4's weight from what people said | Dana Okoro | 2026-03-27, a week after the interviews are due |

## Evidence and Sources

| Claim, and where it appears | Source | Source date | Note, including any gap |
|---|---|---|---|
| Weights for rows 1 and 3 (the 8 of 12 who named asking an analyst and waiting feed row 1, and the 9 of 12 on filters feed row 3), the 8 of 12 behind row 4, the importance of job 1 (the same 8 of 12), and the importance of job 2 (11 of 12, 9 of 12 and 7 of 12) | Persona interviews: 12 operations, fulfilment and finance managers across 9 customer accounts, recorded in the Elena Cho persona. The 34-ticket count comes from the six-month support-ticket review recorded there | Interviews in November and December 2025; persona last updated 2026-01-05 | All 12 are existing customers, so nobody who never bought is heard. Counts are used as the persona records them |
| Weight for row 2 | The session recordings behind the 31 percent figure, read for the FY26 strategy: 9 of 14 reviewed returned to documentation before abandoning | Read before 2026-01-28 | The recordings are of Acme's own new accounts. Nothing in them says where a rival's users stop |
| Weight for row 4 | The persona interviews, as above | As above | That the wait comes from copying data out is our reading. No interviewee was recorded saying it |
| Weight for row 5 | The same recordings, and the strategy's diagnosis | Read before 2026-01-28 | Nobody was asked about connectors. The Low weight is a reading and not a finding |
| Weight for row 6, and every cell in that row | None | | unknown. No interview or recording tested trust. The lapsed-trial interviews are due 2026-03-20 |
| Every rating in the "Us" column, in the comparison and the scorecard | The FY26 strategy's diagnosis (self-serve begins at the schema) and its four committed connectors; the persona interviews and ticket review (the view resets); the product vision (integrations read the data where it lives) | 2026-01-28; 2026-01-05; 2026-01-14 | Our own reading of our own product, the most interested source in the table. Nobody outside Acme re-rated these cells |
| Rivals' saved views, connector lists, copy-in of data, and Plumline's manual two-source join | Each vendor's product pages | Brackenfield BI read 2026-01-29 and 2026-03-05, unchanged. Plumline read 2026-01-29 | Pages say what a vendor claims, and none was tried apart from the two-table test below. Plumline lists "a few" connectors with no number: unknown |
| The status quo takes three forms: inbox, copied spreadsheet, favour | The Acme product vision, and the persona interviews | Vision agreed 2026-01-14; interviews as above | Both are Acme's own documents, so this is one team's view of its customers |
| Both BI tools appear once each in lost deals, and neither recurs | Sales lost-deal notes, last two quarters | Read 2026-01-29 | One input only, and it is the reps' wording. A loss that never reached a rep's notes cannot show here |
| Brackenfield BI is sold by annual contract, with no published price | Its pricing page, which shows a quote form and no figure | Read 2026-01-29 and again 2026-03-05, unchanged | The price of every tier is unknown. No quote was requested, since no row needed a price to be rated |
| Plumline has a free tier and a paid tier priced by uploaded rows | Its pricing page | Read 2026-01-29 | Not re-read for v2, so the page is six weeks old at this version. The paid price at our segment's data volume: unknown |
| Brackenfield BI released a guided mode for its modelling layer | The vendor's own release notes | Published 2026-03-03, read 2026-03-05 | The vendor's words about its own product, so the test below carries the weight |
| The guided mode did not let a non-analyst finish a two-table model alone (rows 1 and 2, Implication 4) | Acme's trial of the vendor's product on its own demo dataset: two members of the product team who do not write queries, each given the same two-table question, a number by hub by week | Tested 2026-03-10 | Two testers is one observation and not a measure. The two testers are Acme product staff, not members of the segment. No customer data was used. The re-test in Implication 4 is the follow-up |
| Hours lost per question under the status quo | None | | unknown. Nobody has timed it |
| Enterprise data-platform vendors and embedded-analytics vendors are out of scope | The FY26 product strategy, the section on non-targets | 2026-01-28 | A scope decision recorded there, not a finding of this analysis |

- Use of rivals' products, and the legal check on their terms: v1 read public pages only and used no
  product. For v2, the product team opened a trial of Brackenfield BI after reading its acceptable use
  terms on 2026-03-06. Those terms allow internal evaluation and bar publishing results. This document
  is internal and no result leaves the company. Plumline's product was not used.

## Refresh Trigger and Versions

- The one named owner, and who they consult: Dana Okoro, VP Product. She consults sales leadership, who
  hold the lost-deal notes, and the services team lead, who sees how accounts are set up.
- The events that call for a refresh before the floor:
  - a general-purpose BI vendor ships a modelling layer that a non-analyst can complete alone, the
    positioning statement's own revisit event, which v2 checked once;
  - the lost-deal notes begin naming one alternative repeatedly, which would give that rival a brief and
    reopen the positioning statement;
  - a rival's release touches a High-weight row, or moves a rating that a finding rests on;
  - the strategy changes its target segment or its non-targets at a review.

  A rival's release calls for a refresh here and does not call for one of the strategy. The strategy
  treats a competitor announcement as no trigger of its own, and a change to the strategy that follows
  from this document goes to Dana Okoro as a proposal, never as an edit.
- The interval floor your team chose, and why: a refresh no later than 1 October each year, two weeks
  before the strategy's review on 15 October 2026. The positioning statement keeps its check-in alongside
  that review, and this analysis feeds both, so it should be no older than they are. Nothing measures
  that this length is right. It follows the review that the documents downstream already keep.

| Version | Date | What triggered it | What changed | Where the earlier version is kept |
|---|---|---|---|---|
| v2 | 2026-03-12 | Brackenfield BI released a guided mode for its modelling layer on 2026-03-03, the kind of event the positioning statement lists as a reason to look again | Checked, and no rating moved: both Brackenfield BI cells on rows 1 and 2 stay Blocked, now from a test and not from its pages. The positioning statement was not reopened. Added the release to its profile, the test to Evidence and Sources, Implication 4, and the Saved Views row, which routes to the roadmap, a document that did not exist at v1. Dates on the trust and connector rows were reset to follow the lapsed-trial interviews. Plumline was not re-read | A frozen copy of v1, dated 2026-01-29, stored beside this document and not edited since |
| v1 | 2026-01-29 | The FY26 strategy, agreed 2026-01-28, chose the segment, and the positioning statement due the next day needed alternatives that someone had compared | First version: the set, the profiles, the comparison rows, and the findings on copying data out, on trust and on connectors, from pages and notes read on the day | None. This is the first version |
