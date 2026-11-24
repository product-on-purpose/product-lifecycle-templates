# Competitive Analysis: the guide

How to decide whether to write one, which variant to use, how to tell whether the draft is any good,
and what to delete before you share it. The reasoning behind each call is in
[`competitive-analysis_companion.md`](competitive-analysis_companion.md). This guide is the procedure.

**Read this first.** Twenty-three of the 56 sources are vendor writing, and nearly every refresh
interval and template structure the research found comes from a vendor. Most of those vendors sell
competitive-intelligence or product-management software. The research read no published,
filled-in competitive analysis, and it found no measurement of any refresh interval or of the harm
a feature checklist does. The section set is largely this library's own reading, and this guide says so
wherever a rule is the library's and not a source's.

## Before you start: is this the right document at all?

Write a competitive analysis when a decision about your product's direction depends on how other
options serve the customers your strategy already chose. Calven, a vendor of an AI product-marketing
platform, gives the test for scope: "Define the decision it serves." If you cannot name the decision
and the person who makes it, stop here. A comparison with no decision behind it has nothing to be
judged against, and the next reader cannot tell what to leave out.

The analysis takes its customers from a product strategy that has already chosen them. If no strategy
has chosen a segment, write the strategy first. That ordering is this library's reading, not a
source's. It places the analysis after the product strategy and immediately before the positioning
statement, and no source states that sequence (companion section 8).

**Write something else if:**

| You actually need | Because |
|---|---|
| a **product strategy** | you are choosing which problems to solve. Pragmatic Institute writes "Competitors can provide useful market intelligence, but they shouldn’t define your product strategy." The analysis informs the strategy and does not set it |
| a **positioning statement** | you are stating how you stand against one named alternative for one customer. Dunford works from competitive alternatives, and says "Not Every Competitor is an Alternative". This document maps the wider field, and the statement takes its real alternatives from it. That split is this library's inference, at medium confidence |
| a **sales battlecard** | the reader is a salesperson in a live conversation. Pragmatic Institute writes "Battle cards are internal documents", built for sales. No source read says a battlecard is not a competitive analysis, so treating it as downstream of the analysis is this library's inference |
| a **SWOT of your own company** | the subject is you. SWOT recurs across vendors' templates, and this library keeps it out because a SWOT assesses us and this document is about the others. That reason is this library's, not any source's |
| a **competitive usability study** | you want to learn why design elements work, with users or with an expert review. NN/g writes "Competitive testing is not the same as a competitive review." A study is research, and this analysis may cite its findings |
| **market trend analysis, market sizing or win/loss analysis** | the question is about the market's direction, its size, or why recent buyers chose or declined. Pragmatic Institute separates these from the competitive landscape and says of trend analysis that "they answer different questions". No source read says whether sizing belongs inside a competitive analysis, so this library keeps it out |
| a **trade study** | you are choosing among options for one of your own decisions, such as which vendor to buy or which technical approach to take. A trade study weighs your options against criteria and picks one. This document compares rivals' products and decides nothing; a decision it informs is written elsewhere. That boundary is this library's own, drawn between its two bundles |
| a **benchmarking report** | you want a recurring measurement. NN/g uses the word for a recurring UX measurement: "Benchmarking is often a program rather than a one-time activity." This bundle does not use it as an alias |

**Write nothing at all if** you only want a spreadsheet of rivals' features to feel informed. That is
the feature checklist, the failure this document is built around (see the first anti-pattern below).

## Picking a variant

**Lean is the default.** It carries the seven sections that name the set, profile it, compare it on what
the chosen customers value, draw the implications, record the evidence and say when to refresh. Start
here, and use it when the team shares the context and one comparison can inform the decision.

**Full adds two sections.** Competitor Briefs, a short narrative on each main rival, sits after the
profiles. Jobs-Based Scorecard, which rates each rival on how well it helps the customers get a job
done, sits after the comparison.

**Move to full when either signal fires.** First, a major choice rests on how a few main rivals differ,
so a table is not enough and the reader needs the reason a customer would pick each. Second, the
lean comparison keeps ending in an argument about which criteria the customers truly care about, and
the jobs view could settle it. Both signals are this library's reading, not a measured one: the
research found no measurement of when the second weight pays for itself. Aha! asks for two weights of
work: "Conduct a high-level competitive analysis on a regular basis." and "Perform a more detailed
analysis to inform major strategic decisions." That is a vendor's framing, and it is the nearest
published source.

**Do not choose full to look thorough.** A full document with a brief per rival and a scorecard
copied from the comparison table is longer and no better. The rubric below penalizes that in rows 9 and 10.

## The order that works

This is this library's order of work. It is not a procedure any source prescribes.

1. Copy the customer segment from the product strategy. Write the decision the analysis informs, and
   who makes it.
2. Build the competitor set from what those customers compare you with and what they do if they buy
   nothing. Add the status quo as a row. Name the rivals you looked at and left out, with a reason.
3. Fill the profiles, and record each claim's source and date in Evidence and Sources while you write
   it, not afterward. Write "unknown" where you do not know.
4. Take each criterion from what the chosen customers said or did. Do not copy a criterion from a
   rival's feature page. Then weight them, and write down where each weight came from.
5. Rate each rival and the status quo on the one scale you stated.
6. On the full variant only, write the briefs and the jobs scorecard.
7. Write the implications last. Each row traces to a comparison row that the customers' weights support.
8. Name the owner, the events that call for a refresh, and the floor, and add the first version row.

## Two tests that outrank the rest

Both are this library's tests, not a source's.

**Swap the segment.** Replace the chosen customers with a neighbouring segment. If the set, the
criteria and the weights still read true, the analysis was scoped to a market and not to the customers
the strategy chose. The set only means something for a stated customer.

**Cover the rivals' names in Implications.** Read each row against the comparison table. If a row exists
because a rival announced something, and not because the chosen customers weight a criterion on which
you trail, a rival's move is setting your direction. Cagan wrote "So stop chasing your competitors and
start focusing on providing real value for your customers". He also asks a product leader to find the
things each competitor does that customers value, so the test is about where a row comes from, not
about whether to study rivals at all.

## The rubric

Score each 0, 1 or 2. **Under 14 out of 20 on full, or under 11 of 16 on lean, and the owner of the strategy cannot use this analysis to
choose or to refuse anything**, because its set, its criteria or its weights were not drawn from the
customers the strategy chose. The thresholds are 14 of 20 on full and 11 of 16 on lean (see the
scope table below). The cut-offs of 14 and 11 are this library's choice. They were not calibrated
against scored real analyses, because none was read. This library also holds that a positioning
statement built on it then names an alternative nobody has compared (companion section 8). That link
is the library's own position, not a sourced one.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Named customers and decision** | A market or a product category is named, and no decision | A segment is named, or a decision is named, but not both | The segment is the one the strategy chose, and you can point at the sentence naming a decision, the person who makes it, and a rival or a criterion that decision lets you leave out |
| 2 | **Set follows the buyer** | A list of the category's products, with no row for what customers do today | Reasons are given, or the status quo has a row, but the other is missing | Every row has a reason, either what the chosen customers compare or do, or, for a watched rival, the stated reason it is watched. The status quo row says what a customer does and what it costs them, and you can point at a rival that was looked at and left out, with the reason |
| 3 | **Traceable profiles** | Adjectives, and figures nobody can trace | Facts are present, but some cells are unsourced or hold a guess | Pick any cell and you can find its entry in Evidence and Sources and open that source. Every cell without a source says "unknown" and why |
| 4 | **Criteria from the customers** | Criteria are feature names copied from rivals' pages | Criteria read in customers' language, but nothing shows the customers said or did them | You can point at a criterion and the thing the customers said or did that produced it. Where a rival leads on a criterion the customers weight lightly, the row is kept and the decision about it is written down |
| 5 | **Sourced weights and ratings** | No weights, or yes and no in place of levels | Weights are present, and their source is a general phrase such as "customer research" | Every weight says where it came from, an unknown weight says "unknown", every rating uses the scale stated once, and someone who did not write it could re-rate one cell from the cited evidence |
| 6 | **Findings ending in moves** | Facts about rivals, with no move | Moves are named, but one lacks an owner or a date, or none says which document it changes | Every row names a finding, the document it routes to, one move, an owner and a date. You can trace each row to a comparison row, and none rests only on what a rival announced |
| 7 | **Auditable evidence** | Sources such as "online research", with no dates | Sources are named, but dates are missing, or a claim rests on a single input | For each claim a decision rests on, a reader can open the source and see its date. Every gap is a row marked "unknown" with the reason, and the document states whether rivals' products were used and what the legal check found |
| 8 | **Refresh that can fire** | "Reviewed regularly", with no owner | An owner and an interval, but no event that would call for an earlier refresh | One named owner and who they consult, events that call for a refresh before the floor, and the team's own reason for the length of the floor, not a vendor's. The version table shows where each earlier version can be opened |
| 9 | **Customer-side briefs** *(full only)* | Each brief is a verdict on whether the rival is good | Strengths and weaknesses are listed, and nothing a customer values is named | Each brief names what the chosen customers value in that rival and what it leaves unmet, taken from evidence in the document, and says when a chosen customer would reasonably pick it over you |
| 10 | **Jobs beyond criteria** *(full only)* | Features in the job column | Jobs are in the customers' words, but each maps one to one onto a comparison row | You can point at a job that no single comparison row covers, and say which step of it each rival helps with and which it misses |

**Which rows apply to what.** The rubric is written for the full variant. The lean variant has no
Competitor Briefs section and no Jobs-Based Scorecard section, so rows 9 and 10 grade a section it
does not ship. Scope, in full:

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| lean | 1-8 (it has no briefs and no jobs scorecard to grade) | 16 | **11** |
| full | all 10 | 20 | **14** |

Each threshold is about the same share of the available points. **Under 11 of the 16 on lean, and the
strategy's owner has the same problem as on full**: the comparison cannot be used to choose or refuse,
because the set, the criteria or the weights did not come from the chosen customers. Rows 9 and 10 do
not apply to lean on purpose and not by oversight. Choosing the default variant must never cost points
for sections it does not ship.

**A 0 on row 6 or row 8 fails the document whatever the total.** Row 6 is what makes the analysis part
of the strategy chain: without a move, an owner and a date, nothing downstream changes. Row 8 is what
keeps a standing document current: without an owner and an event that fires, it goes stale unnoticed.
Without this rule, a document scoring 0 on both rows and 2 on every other row would total 12 of 16 on
lean and 16 of 20 on full, and pass. The rule, like the thresholds, is this library's judgement and is
not measured.

**How to score honestly.** For each row, find the sentence or cell that earns the score and point at it.
If you cannot, score the lower number. Ask someone who did not write the document to re-rate one cell
in row 5 from the evidence you cite. If they cannot, the weight or the rating was not traceable.

## Variant-specific checks

**Lean.** Read Purpose and Scope and then Implications for Our Direction alone. Does each implication
follow from a decision the first section named? If a reader could not tell which decision the
analysis informed, the two were written independently.

**Full.** Read one brief and the matching column of the comparison table side by side. Do they agree on
what customers value in that rival? A brief that praises what the table rates low, or the reverse, was
written without the table.

## Anti-patterns

The research recorded no measurement of how often any of these occurs. Each is named by a source or is
this library's reading, and each line says which.

1. **The feature checklist.** Rivals are compared on the features they chose, and not on what the
   chosen customers value. Steve Blank argues that "a competitive analysis drives a maximum feature
   set". Strategyn says "feature-to-feature comparisons is no guarantee of success", and THRV writes
   "Feature catch-up with your competitors is a race". Strategyn and THRV both sell a
   jobs-to-be-done method, and THRV's page shows no author, so this library reads them as one voice. As
   far as this research found, nobody measured the harm. *Catch it:* the criteria in the table are
   names from a rival's feature page, and no weight says where it came from (row 4).
2. **Leaving out the status quo.** The set has no row for what the customer does if they buy nothing.
   Customer Impact writes "The status quo is your largest competitor. Most teams forget it." Dunford and
   Pragmatic Institute also place it among the alternatives. Customer Impact and Calven both sell in
   this area, and placing it in this document is this library's position. *Catch it:* every row in the
   set is a product (row 2).
3. **The set from the whole shelf.** The set lists every product in the category. Dunford asks "What
   would a customer do if your offering didn't exist?" and says "Not Every Competitor is an
   Alternative". *Catch it:* a row's only reason is that it is in the category, with no watched
   reason stated (row 2).
4. **The guessed cell.** A figure the author did not read, entered so that the table looks complete.
   Calven writes "A cell with an invented number in it is worse than an empty one, because it looks
   like knowledge." and "Every field needs a source you can name, and a blank field beats a guessed
   one." It is a vendor's line, and it is a good rule for any row here. *Catch it:* a cell has no entry
   in Evidence and Sources and does not say "unknown" (rows 3 and 7).
5. **The weight that is a guess.** A weight with no source reads as a finding. GitLab says the
   comparison "should be completely data/evidence driven". *Catch it:* the "where the weight came from"
   cell is empty or reads "judgment" (row 5).
6. **The rival's move as strategy.** An implication exists because a rival announced something. The
   Pragmatic Institute sentence in the first table applies here. *Catch it:* no comparison row supports
   the finding (row 6).
7. **The finding with no move.** A fact about a rival, with no document it changes, no owner and no
   date. Customer Impact advises "Let every finding end in one concrete move with an owner and a
   date", and Calven gives the same advice in other words. Both sell in this area. *Catch it:* the
   owner or the date cell is empty (row 6).
8. **The comparison nobody refreshes.** A document built once and left. Dovetail lists "failing to
   update or spot-check data" as a common mistake. Calven writes "A profile built once is usually wrong
   within a quarter." The quarter is an unmeasured vendor claim. *Catch it:* the version table has one
   row and the refresh section names no owner (row 8).
9. **The vendor's interval as consensus.** The floor is copied from a vendor's advice. No source read
   measures an interval, and every interval except GitLab's comes from a vendor (companion section 6).
   *Catch it:* the floor's reason is another publisher's name (row 8).
10. **The jobs table that renames the criteria** (full only). Each job is a comparison row in different words. A
    job spans several steps and can be met or missed as a whole. That distinction is this library's
    reading, taken from GitLab's scorecard, which is built on jobs to be done, and Strategyn's
    job-based comparison. *Catch it:* every job maps onto exactly one comparison row (row 10).
11. **The brief as a verdict** (full only). A brief says whether the rival is good. Cagan's frame is what customers
    value in the rival and where their needs go unmet, so a brief is a view from the customer's side.
    *Catch it:* no brief names a need the rival leaves unmet (row 9).
12. **Relying on one input.** Every profile rests on the rival's own website, or on one internal
    system. Klue warns "Don't just rely on CRM data". GitLab names websites, documentation, demo
    videos, customers and competitors as inputs to accuracy. *Catch it:* a claim's only source is a
    single page the rival wrote (row 7).

## Where the sources disagree, so you can say so in your own document

Your reader may ask why you chose a floor, or why the comparison is a table and not a living feed.
Each of these is contested, and the research settled none of them. The sources and the reasoning are
in companion section 6.

- **Living document or dated snapshot.** Vendor voices sit on both sides. This library treats each
  refresh as a dated snapshot and the document as the series.
- **Features or customer value.** This library takes the customer-value side for the comparison.
- **How often to refresh.** None of the intervals is measured (anti-pattern 9).
- **Who owns it.** The owner's function differs by source. Name one owner either way.

## When it is good enough

When the strategy's owner can use it to settle a decision the first section named, and when someone who
did not write it can re-rate one comparison cell from the evidence cited. A comparison that has never
been used to choose or to refuse something is not finished, however complete the table looks.

Then delete every HTML comment. They are guidance, not content. Keep the `source_template` and
`source_template_version` fields in the frontmatter, because they are the only record of which
bundle and which version produced the document. Add the first version row, and put the owner's name
beside the refresh events.

## Sources and limits

Every quotation above comes from a page recorded as fetched and verified in
[`competitive-analysis_research-log.md`](competitive-analysis_research-log.md). A quotation from a
vendor is a vendor's position, and it is labelled so where the vendor sells in this area. For the
neighbouring documents see the [positioning statement
guide](../positioning-statement/positioning-statement_guide.md) and the [product strategy
guide](../product-strategy/product-strategy_guide.md). For what each section is for, and where its
sources disagree, read the companion.

**What this guide does not know.** It does not know who first wrote a competitive analysis for a
product team. It does not know any interval at which a refresh pays for itself, or how often any
anti-pattern above occurs. It did not read a published, filled-in competitive analysis, so every row
of the rubric rests on guidance and on this library's reading, and not on an observed pattern in
documents that worked.
