---
title: "{{product_name}} Product Strategy"
product: "{{product_name}}"
owner: "{{who_owns_this_strategy}}"
period: "{{period_this_covers}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
doc_type: product-strategy
size: full
format: one-pager
source_template: product-strategy
source_template_version: 0.1.0
---

<!--
PRODUCT STRATEGY, ONE-PAGER FORMAT (choice cascade). A different opening question from the kernel format,
not a different size of it.

WHEN TO REACH FOR THIS INSTEAD OF THE KERNEL. The kernel (product-strategy_template-lean.md and
product-strategy_template-full.md) starts from the obstacle: use it when the hard part is that nobody agrees
what the problem is. This cascade starts from the choice: use it when the problem is understood and the hard
part is deciding where to compete and how to win there. If you find yourself unable to fill in "Where We
Will Play" because you are still arguing about what is wrong, you want the kernel.

WHERE THIS SHAPE COMES FROM, AND WHAT THIS BUNDLE ADDED. It is a Playing-to-Win-derived cascade as published
by a named practitioner: winning aspiration, how we will know we have won, where we will play, how we will
win, capabilities, and product principles. This bundle ships it because it is structurally distinct from the
kernel and genuinely in circulation, which is the bar this library sets before adding a format. ONE SECTION
IS THIS BUNDLE'S ADDITION and is not in the published cascade: "What We Are Not Doing". It is added because
every quality test the research found turns on naming refusals, and a cascade can otherwise state where it
will play without ever saying what it declines. Deep dive: product-strategy_companion.md section 4.

A NAMED REAL-WORLD VARIANT is described in product-strategy_companion.md section 9 rather than shipped as a
third file, because it is one company's document rather than a named reusable format. Its "right to win" and
"risks" questions are worth stealing whichever format you use.

THE TEST THIS DOCUMENT HAS TO PASS is the same for every format. Swap in a competitor's name; if it still
reads true, you have described an industry rather than made a choice.

ON LENGTH. One page is a position, not a finding. Amazon standardises on six narrative pages for major
decisions; other named practitioners argue one page forces focus. No study of document length was found.
Pick deliberately and say why. See product-strategy_companion.md section 4.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP.
2. Replace each {{placeholder}} with your content.
3. Fill "What We Are Not Doing" before you consider the draft finished. It is the section that makes the
   rest usable.
4. If a section does not apply, write "N/A" and one line of why.
5. Before you share it: self-grade against product-strategy_guide.md, then DELETE every HTML comment.
-->

# {{product_name}} Product Strategy

## Winning Aspiration

<!-- WHAT  What winning means for this product, in one or two sentences. Not the company mission, and not a
           revenue target on its own.
     WHY   The cascade only works if the aspiration is specific enough to make the later choices
           consequential. An aspiration that any competitor would also claim produces a cascade of choices
           that any competitor would also make. Deep dive: product-strategy_companion.md section 3 (Winning
           Aspiration).
     ASK   What does winning look like for the user, not just for us? Would our closest competitor write
           this same sentence? What are we willing to be worse at in order to win this way?
     GOOD  "Dispatchers at small fleets send the right van to the right job without reading a single note,
           and they trust the order the system proposes enough to stop rebuilding it by hand."
           (a specific state of the world, and it implies trade-offs)
     WEAK  "Be the market leader in field service." (a position, not an aspiration, and no user in it)
     TRAP  Writing the vision here. If your product has a vision document, this section is the part of it
           this strategy period is actually chasing, not the whole thing. -->

{{winning_aspiration}}

## How We Will Know We Have Won

<!-- WHAT  The evidence that the aspiration is being reached: one leading measure, one lagging, and roughly
           when you expect to see each.
     WHY   The published cascade puts this second, immediately after the aspiration and before any choice
           is made, and the ordering is the point: an aspiration you cannot tell you are reaching will be
           reinterpreted at the end of the period to match whatever happened. It is NOT your OKRs, which
           measure a period's execution rather than deciding which objectives were worth setting. Deep dive:
           product-strategy_companion.md section 3 (How We Will Know We Have Won) and section 8.
     ASK   What moves first if this is working? What would we see in eight weeks rather than eight months?
           What result would make us abandon this strategy rather than try harder at it?
     GOOD  "Leading: dispatcher override rate on inferred priority, from 48 percent to under 20 percent by
           the end of Q2. Lagging: emergency jobs completed inside the promised window. If the override rate
           has not moved by the end of Q2, the aspiration was wrong rather than under-resourced."
           (one leading, one lagging, and a stated falsifier)
     WEAK  "Increased adoption and improved customer satisfaction."
           (no baseline, no date, nothing that could come back negative)
     TRAP  Pasting in this quarter's OKRs. If this section could be lifted into a planning tool unchanged,
           you have written objectives rather than a way to tell whether the strategy is right. -->

{{how_we_will_know_we_have_won}}

## Where We Will Play

<!-- WHAT  The segments, use cases, channels and geographies you are competing in this period. Name what is
           in AND what is out.
     WHY   This is the choice that makes the strategy checkable. "Where to play" without a corresponding
           "where not to play" is a description of your current customer list. Deep dive:
           product-strategy_companion.md section 3 (Where We Will Play) and section 7.
     ASK   Which segment do we decline? Which use case do we leave to someone else? If we are strong
           somewhere we are not choosing to play, why are we keeping it?
     GOOD  "In: 10-80 vehicle operators in plumbing, HVAC and electrical, direct sales, UK and Ireland.
           Out: national facilities-management contractors, and the white-label channel we won two deals in
           last year."
           (explicit exclusions, including a profitable one)
     WEAK  "Mid-market and enterprise across all major verticals." (nothing excluded)
     TRAP  Choosing a market you have never sold into because it is large. Where you play should be where
           your right to win is real, not where the total addressable market is biggest. -->

{{where_we_will_play}}

## How We Will Win

<!-- WHAT  Why you win where you have chosen to play, against the specific alternatives available there.
           Name the alternatives.
     WHY   Porter's argument is that a position is durable when it rests on activities configured
           differently from rivals, not on doing the same activities better: "the essence of strategy is
           choosing to perform activities differently than rivals do". A "how we win" that is really "we
           will execute well" describes effort, not position. Deep dive: product-strategy_companion.md
           section 2 and section 3 (How We Will Win).
     ASK   Against whom, exactly? What would a competitor have to give up to copy this? Is this a difference
           in what we do, or only in how hard we try?
     GOOD  "We win by reading urgency out of the work that already exists rather than asking anyone to
           classify it. Competitors invest in richer intake forms and compliance reporting; we invest in
           inference and in showing our working. Copying us means giving up the structured-data story their
           enterprise contracts are sold on."
           (names the alternative and the cost of imitation)
     WEAK  "Superior user experience, faster performance, and better customer support."
           (three things every competitor claims)
     TRAP  Listing your feature advantages. Features get copied in a quarter. The question is what
           configuration of choices makes copying expensive. -->

{{how_we_will_win}}

## Capabilities and Systems

<!-- WHAT  What the team must be able to do, and what has to exist, for the above to be true. Three to five.
     WHY   This is where a cascade stops being aspirational: it names the gap between the strategy and the
           organisation you actually have. Deep dive: product-strategy_companion.md section 3 (Capabilities
           and Systems).
     ASK   Which of these do we not have today? What are we going to stop doing to build them? Which one, if
           we never build it, makes the strategy fail?
     GOOD  "1. Urgency inference we can run at ingest, prototyped once and never in production. 2. A labelled
           corpus of past jobs, which only the support team can produce. 3. Instrumentation good enough to
           see an override the moment it happens. We have none of the three, and building 2 means support
           stops taking tier-1 tickets for a quarter."
           (honest about the gap and its cost)
     WEAK  "Strong engineering, good design, and a data-driven culture."
           (generic, unmeasurable, and true of the company you already are)
     TRAP  Listing capabilities you already have. This section earns its place by naming what is missing. -->

{{capabilities_and_systems}}

## Product Principles

<!-- WHAT  Two to five rules that resolve recurring trade-offs the same way every time, so the team does not
           relitigate them.
     WHY   Principles are the strategy's delegation mechanism: they let people decide without asking. A
           principle that never rules anything out is decoration. Deep dive:
           product-strategy_companion.md section 3 (Product Principles).
     ASK   What argument keeps recurring? What does this principle cost us when it bites? Would anyone ever
           argue for the opposite, and if not, is it a principle?
     GOOD  "Propose, never impose: when we infer something, we show it beside what the user entered and let
           them overrule it in one action. Cost: more screen space and a slower path for the cases we get
           right."
           (a rule with a stated cost)
     WEAK  "Be customer-obsessed." (nobody argues for the opposite)
     TRAP  Writing values. Values describe how you want to behave; principles decide arguments. If it does
           not resolve a real disagreement, it belongs somewhere else. -->

{{product_principles}}

## What We Are Not Doing

<!-- WHAT  The things you are explicitly declining this period, and one line each on why. Two to five.
     WHY   The section that makes the rest usable, and the one every quality test in this bundle's
           research turns on. The practical test is
           whether the team can say "this is a really great idea... but we're not going to build it" and
           mean it; the sharper one is whether anyone was made uncomfortable. Deep dive:
           product-strategy_companion.md section 3 (What We Are Not Doing) and section 7.
     ASK   What has been asked for repeatedly that we are now refusing? Who will be unhappy, and have we
           told them? If nothing here costs us anything, have we chosen?
     GOOD  "We are not shipping the customer-facing arrival-window feature this year. It is the most
           requested item in our backlog and it depends on scheduling accuracy we do not yet have. Sales has
           been told."
     WEAK  "We are not going to lose focus." (refuses nothing)
     TRAP  Listing only things nobody wanted. A refusal that costs nothing proves nothing. -->

{{what_we_are_not_doing}}
