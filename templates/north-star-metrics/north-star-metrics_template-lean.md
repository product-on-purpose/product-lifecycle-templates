---
title: "{{product_name}} North Star Metric"
product: "{{product_name}}"
owner: "{{who_owns_this_metric}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
doc_type: north-star-metrics
size: lean
source_template: north-star-metrics
source_template_version: 0.1.0
---

<!--
LEAN NORTH STAR METRIC. The shortest form that still names the metric, the case for it, its input
metrics, what it serves, and the signal that would bring you back to it. Use it to settle what your
product's single measure of customer value is and why, before anyone asks what was rejected or what
would change it. To grow it into a form that also names rejected candidates, standing guardrails, the
metric's own blind spots, and a change log, see north-star-metrics_template-full.md. ADD sections
after When We Revisit It; never rename or reorder the five below, because the full variant is a strict
ordered superset of this one.

ADMISSION, AND WHAT IT MEANS FOR THIS TEMPLATE. This type is admitted on one publisher, Amplitude,
across two documents that both reserve all rights. Every field name, section name and layout choice
below is this library's own wording, never Amplitude's worksheet, its checklist text, or its sidebar
heuristic. Where a sentence below is attributed to Amplitude or another source, it is reported as that
source's own words, never offered as this template's own field label.

WHAT A NORTH STAR METRIC IS, AND IS NOT. It names the single measure of customer value that shows a
product's strategy is working, states the case for it, and names the inputs a team can actually move.
It is NOT the product vision (that names the destination; this names the number that shows the
strategy is getting you there). It is NOT the product strategy (that chooses which problems to solve;
in this library's chain, drawn from sources that describe a North Star as measuring the current
strategy, the North Star comes after it; one source orders the two the other way, and
north-star-metrics_companion.md section 6 names both camps). It is NOT OKRs (those reset each period;
a North Star persists and is revisited on a trigger, not a calendar). And it is NOT kpi-dashboard
(that carries the formula, the data source, the refresh schedule, the target and the threshold; this
document carries one definition and the case for choosing it). See north-star-metrics_companion.md
section 8 for the fuller set of boundaries.

WHAT STAYS OUT, AT EVERY SIZE. No formula, no data source, no refresh schedule, no target, no
threshold, no dashboard layout, and no tree of metrics below the inputs. All of that belongs to
kpi-dashboard, except the metric tree, which the catalog lists as its own document type with the North
Star at its top node. If you find yourself writing a calculation here, stop and open kpi-dashboard
instead.

ONE NORTH STAR, PER PRODUCT OR PER PRODUCT LINE. The default is one North Star metric for the whole
product. The named exception is a company with genuinely separate product lines, each with its own
customers and its own profit and loss; that company may need one North Star per line, not one per team
or one per feature. A direct competitor to the admitting publisher disputes the one-metric premise as
"mostly rhetorical"; this bundle follows the one-per-product rule with the product-line exception. See
north-star-metrics_companion.md section 6.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   north-star-metrics_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP
   to avoid. For the table, PRIORITY explains the ordering rule and ROW HINT says what a good row
   contains.
2. Replace each {{placeholder}} with your content. Name no formula, data source, refresh schedule,
   target, or threshold anywhere in this document; those belong to kpi-dashboard.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you share it: self-grade against north-star-metrics_guide.md, then DELETE every HTML
   comment. They are guidance, not content.
-->

# {{product_name}} North Star Metric

## The North Star

<!-- WHAT  The metric's name and its definition in one statement: the behavior it counts, who does
           it, and over what time window. The product it covers, if your company runs more than one.
     WHY   Cut the SaaS states the window directly: "Pick a metric that counts that action across a
           sensible time window, like weekly." Ballpark adds the bar for the definition itself:
           "Prefer a definition people can explain, inspect and reproduce." Amplitude's own fill-in
           exercise, reported here and not reproduced as this template's own field, asks for the
           metric's name and a one-sentence definition; this section asks for the same two things in
           the library's own wording. Deep dive: north-star-metrics_companion.md section 3 (The North
           Star).
     ASK   What behavior does this metric count? Who performs it, and over what window, weekly or
           some other sensible period? Could someone outside your team read the definition and
           reproduce the count themselves? Does your company run more than one product, and if so,
           which one does this North Star belong to?
     GOOD  "Our North Star is weekly closed expense reports: the count of expense reports that reach
           Approved or Reimbursed status, per active finance team, each week, with no manual nudge
           from a success manager."
           (names the behavior, the actor, and the window, and leaves the calculation out)
     WEAK  "Our North Star is engagement."
           (no behavior, no actor, no window; nobody could reproduce a count from this)
     TRAP  Writing the calculation instead of the definition. A column for exclusions, a query
           snippet, or a refresh schedule belongs in kpi-dashboard's Metric Definitions section, not
           here. -->

{{north_star_definition}}

- Product this North Star belongs to, if your company has more than one: {{product_scope}}

## Why This Metric

<!-- WHAT  The case for this metric over another: the customer value it expresses, why it leads
           revenue rather than reporting it, why it is not a vanity metric, and what shows it
           predicts retention or revenue in this product's own data.
     WHY   Amplitude's own checklist asks, among other things, "Does it express customer value?" and
           "Is it a leading indicator of success?" A second Amplitude article adds the instruction to
           check the claim against your own evidence: "Validate that it predicts retention and
           revenue in your own data." Koji states where that evidence has to come from: "You cannot
           write this sentence by staring at a dashboard." Deep dive: north-star-metrics_companion.md
           section 3 (Why This Metric).
     ASK   What does this metric say about the value a customer actually gets? Why does it move
           before revenue rather than after? Could it rise forever even if the business got no
           healthier, the doubling test one source proposes? What shows, in your own data or your own
           customer conversations, that this metric predicts retention or revenue, and if nothing
           does yet, how will you find out?
     GOOD  "Closed expense reports measures the moment a finance team gets what it pays us for: an
           expense submitted, reviewed and settled without chasing anyone. It is not revenue, which
           only tells us the deal closed, not whether the team is getting value every week. We have
           not yet run the correlation against renewal; that test is scheduled for next quarter."
           (states the value, the leading-versus-lagging case, and labels the missing validation
           honestly)
     WEAK  "This metric matters because it's the number that matters most."
           (restates the question; names no customer value, no leading-indicator case, no validation)
     TRAP  Treating "it predicts revenue" as self-evident. The admitting source's own instruction is
           to validate the claim in your own data, not to assume a metric is a leading indicator
           because it sounds like one. -->

- The customer value case: {{customer_value_case}}
- Why it leads rather than lags revenue: {{leading_indicator_case}}
- Why it is not a vanity metric: {{not_vanity_metric_case}}
- What shows it predicts retention or revenue in your own data, or how you will find out:
  {{validation_evidence}}

## Input Metrics

<!-- WHAT  Three to five measures a team can actually move, that combine to drive the North Star,
           each with a named owner.
     WHY   Amplitude defines inputs as "a set of three to five influential, complementary factors
           that you believe most directly affect your North Star Metric and that your team can
           directly influence through your product." Basedash states the ownership rule: "Each input
           is something a specific team can own and affect directly." A reference source goes
           further, naming six to ten input metrics across a customer journey with each team owning
           one to three of them; this bundle keeps Amplitude's three to five as its default and
           reports the larger count as that one source's own. Amplitude's own breadth, depth,
           frequency and efficiency heuristic for finding inputs is reported here as one vendor's
           own, never prescribed; a competing vendor structures inputs as a hierarchy instead, and
           this bundle prescribes neither. Deep dive: north-star-metrics_companion.md section 3
           (Input Metrics), section 6 (How input metrics are organized).
     ASK   What three to five measures, if your team moved them, would move the North Star? Who owns
           each one, specifically enough that they would notice it slipping? Could the North Star
           move without any of these moving, in which case is something missing? Is any row really
           the North Star itself, counted a different way?
     PRIORITY  Three to five is this bundle's default. One reference source allows six to ten across
           a longer customer journey, with one to three per team. Past five rows, every one still
           needs an owner who can actually move it, or it has not earned its place.
     ROW HINT  A good row names one measurable behavior, one owning team, and why moving that
           behavior should move the North Star. A weak row names a team with no measure, or restates
           the North Star's own definition under a different label.
     GOOD  | Receipt-capture completion rate | Mobile team | A report cannot close until its
           receipts are attached; this is the most common place a report stalls |
     WEAK  | Customer happiness | Everyone | |
     TRAP  Adding a row because a team wants one, not because moving it would move the North Star. A
           row with no real lever behind it is the same failure Amplitude's own playbook names for
           the North Star itself: insisting on more than real boundaries support. -->

| Input Metric | Owning Team | Why It Drives the North Star |
|---|---|---|
| {{input_metric_name}} | {{input_metric_owner}} | {{input_metric_rationale}} |

## What It Serves

<!-- WHAT  The product strategy this metric measures, the vision that strategy serves, and the
           business outcome this metric is expected to predict.
     WHY   Amplitude names one part of a good North Star as "a metric that serves as a key measure
           of your current product strategy." This library places the North Star after the strategy
           it measures; one practitioner orders the two the other way, putting the North Star first.
           Both camps are named in north-star-metrics_companion.md section 6 (The chain position is
           contested); this section states this library's position and asks you to name your
           strategy, not to settle the debate. Deep dive: north-star-metrics_companion.md section 3
           (What It Serves).
     ASK   Which product strategy does this number show is working? How does that strategy serve the
           product vision? What business outcome, revenue, retention, or expansion, is this metric
           expected to predict, and does it correlate with that outcome without being that outcome?
     GOOD  "Closed expense reports measures whether our strategy, becoming the system finance teams
           trust enough to stop keeping a shadow spreadsheet, is working. It serves the vision of a
           finance team that never reconciles a paper receipt by hand. It is expected to predict
           renewal, not replace it as the renewal number itself."
     WEAK  "This metric supports our overall goals."
           (names no strategy, no vision, no outcome)
     TRAP  Copying the strategy's own language in here unexamined. If this section could be lifted
           straight out of the strategy document with no change, ask whether the metric actually
           measures the strategy or is simply repeating it. -->

- The product strategy this metric measures: {{strategy_it_measures}}
- The product vision that strategy serves: {{vision_it_serves}}
- The business outcome it is expected to predict, and how it differs from that outcome:
  {{business_outcome_expected}}

## When We Revisit It

<!-- WHAT  The signal that would bring the team back to this definition, not a calendar date.
     WHY   Amplitude's own playbook asks, "What will be your signal to revisit this metric?" A
           reference source states the trigger from the other side: "Only change the NSM when
           strategy or product fundamentally shifts." Spotify's experimentation glossary names the
           stakes: "Changing the north star is a significant organizational decision." Sources
           disagree sharply on cadence, by stage, by a flat yearly rule, or on a fixed quarterly
           calendar; this section asks for the trigger because no source read agrees on a number. Deep
           dive: north-star-metrics_companion.md section 3 (When We Revisit It), section 6 (How often
           it changes).
     ASK   What change in the product, the market, or the strategy would make you look at this
           definition again? Who notices that signal first? What would have to be true for the
           metric itself, not just its target, to change?
     GOOD  "We revisit this definition if we start selling to teams that approve travel budgets
           rather than individual expense reports; closed expense reports would no longer describe
           the value those teams get. The head of product owns watching for that shift."
     WEAK  "We'll review this every quarter."
           (a calendar entry, naming no event and nobody responsible for noticing one)
     TRAP  Confusing a trigger with a target miss. A quarter where the number does not move is a
           signal to investigate the input metrics, not, on its own, a reason to redefine the North
           Star itself. -->

- The signal that would bring you back to this definition, not a date: {{revisit_trigger}}
- Who is responsible for noticing that signal: {{revisit_owner}}
