---
title: "{{product_name}} Product Strategy"
product: "{{product_name}}"
owner: "{{who_owns_this_strategy}}"
period: "{{period_this_covers}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
doc_type: product-strategy
size: full
format: kernel
source_template: product-strategy
source_template_version: 0.1.0
---

<!--
FULL PRODUCT STRATEGY (kernel format). Every section of product-strategy_template-lean.md, in the same order,
plus the four a strategy needs when it has to survive people who were not in the room: who it is and is not
for, how you will know it is working, what it assumes, and what brings you back to it.

USE FULL WHEN the strategy will be read by someone who was not in the argument that produced it: a new
leader, a board, a team in another function, or your own team in six months. Use lean
(product-strategy_template-lean.md) when a small group needs to settle what to work on and everyone already
shares the context.

THE TEST THIS DOCUMENT HAS TO PASS. Swap in a competitor's name. If it still reads true, you have described
an industry rather than made a choice. If nothing in it made anyone uncomfortable, it is a wish list.

WHAT THE EVIDENCE ACTUALLY SAYS, SO YOU ARE NOT MISLED. No study measures whether writing a product strategy
document improves product outcomes. The literature on strategic PLANNING as a process is mixed, and one
study of listed firms found no correlation with objective financial performance while finding one with what
managers believed. "Everyone felt it helped" is not evidence. See product-strategy_companion.md section 1.

THE KERNEL IS NOT THIS LIBRARY'S INVENTION. Diagnosis, guiding policy and coherent action come from Richard
Rumelt's Good Strategy Bad Strategy (2011).

THIS IS ONE OF TWO FORMATS. product-strategy_template-one-pager-full.md is a choice cascade for when the
problem is understood and the hard part is choosing where to compete. See
product-strategy_companion.md section 4.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   product-strategy_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to
   avoid.
2. Replace each {{placeholder}} with your content.
3. Write the diagnosis first and do not move on until it names ONE obstacle.
4. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
5. Before you share it: self-grade against product-strategy_guide.md, then DELETE every HTML comment.
-->

# {{product_name}} Product Strategy

## Diagnosis

<!-- WHAT  The one thing that makes the goal hard. Not a summary of the market, not a list of challenges:
           the single obstacle that, if it went away, would make the rest straightforward.
     WHY   This is the section that separates a strategy from a wish. Rumelt's test is that without an
           analysed obstacle you have "either a stretch goal, a budget, or a list of things you wish would
           happen". Deep dive: product-strategy_companion.md section 3 (Diagnosis).
     ASK   What is actually stopping us? If this obstacle disappeared overnight, would the goal become easy?
           Is this a cause or a symptom? Would a competitor recognise this as their obstacle too?
     GOOD  "Dispatchers build a route in under a minute, but only once someone has told them which jobs are
           genuinely urgent. Urgency lives in the free-text notes field: in the 200 jobs we sampled, three of
           every five emergencies were caught by a human reading it. Our scheduling engine is fast and it is
           scheduling the wrong things first."
     WEAK  "The market is increasingly competitive and customers expect more from field-service software."
           (true of every company in the category; names nothing that could be wrong)
     TRAP  Writing the goal here instead of the obstacle. "We need to grow self-serve revenue" is a target;
           the diagnosis is why that has not already happened. -->

{{the_diagnosis}}

## Target Segments, and Non-Targets

<!-- WHAT  Who this strategy is for, specifically, and who it is explicitly NOT for this period. A short
           table or two short lists.
     WHY   Naming non-targets is one of the few concrete tests practitioners publish for whether a strategy
           is real: a strategy that clearly identifies target AND non-target segments has made a choice a
           reader can check. Without it, "focus" is a word rather than a decision. Deep dive:
           product-strategy_companion.md section 3 (Target Segments) and section 7.
     ASK   Who do we win with today, and is that who we are aiming at? Which segment are we declining, and
           who inside the company will object? If we optimised entirely for the target, which current
           customer would be worse off?
     GOOD  "Target: dispatchers at 10-80 vehicle operators who schedule the same day work arrives.
           Non-target this period: national facilities-management contractors. They buy on compliance
           reporting, which pulls us back toward the forms-and-fields product we are trying to stop being."
           (both named, with the cost of the refusal stated)
     WEAK  "Target: growing service businesses that value operational efficiency."
           (excludes nobody, so it is not a segmentation)
     TRAP  Listing every segment you sell to. A target list that matches your customer list is a description
           of the past, not a choice about the future. -->

{{target_segments_and_non_targets}}

## Guiding Policy

<!-- WHAT  The approach you are taking to the obstacle. One paragraph. It should constrain: a reader should
           be able to name a reasonable option it rules out.
     WHY   A guiding policy is a direction, not a plan. Rumelt's image is guardrails: it directs and
           constrains action without fully defining it. If every option that was on the table last month
           survives it, it is a preamble. Deep dive: product-strategy_companion.md section 3 (Guiding
           Policy).
     ASK   What does this rule out? Which team's current plan changes because of this? If someone disagreed,
           what would they argue for instead?
     GOOD  "We will infer urgency from the job record rather than asking dispatchers to encode it. Given a
           choice between a better form for entering priority and a model that reads what is already
           written, we read what is already written."
     WEAK  "We will focus on delivering an excellent dispatcher experience and driving scheduling
           efficiency."
     TRAP  Listing several policies. If you have three, you have deferred the choice to whoever reads this
           next. -->

{{the_guiding_policy}}

## Coherent Action

<!-- WHAT  The moves that carry out the policy, and how they reinforce each other. Three to five kinds of
           work, not dated deliverables.
     WHY   The word doing the work is "coherent". Porter's argument is that fit is what makes a position
           durable: it "locks out imitators by creating a chain that is as strong as its strongest link".
           Deep dive: product-strategy_companion.md section 3 (Coherent Action).
     ASK   Does each action serve the policy, or just seem generally good? Which two make each other
           stronger? Are these kinds of work, or release dates wearing a disguise?
     GOOD  "1. Extract urgency signals from the notes field at ingest. 2. Show the inferred priority beside
           the dispatcher's own, so disagreement is visible. 3. Track the override rate as our leading
           indicator. The first two make the inference usable; the third is how we learn whether it works."
     WEAK  "Launch AI assistant in Q3. Redesign the intake form. Hire two data scientists."
           (a dated to-do list; nothing reinforces anything else)
     TRAP  Writing the roadmap. If a reader could build a Gantt chart from this section, it has stopped
           being strategy. -->

{{the_coherent_action}}

## What We Are Not Doing

<!-- WHAT  The things you are explicitly declining this period, and one line each on why. Two to five. Name
           real options.
     WHY   This is the section that makes the others usable, and the one every quality test
           in this bundle's research turns on. The test practitioners apply is whether the
           team can say "this is a really great idea... but we're not going to build it" and mean it. A
           strategy that makes nobody uncomfortable is a wish list. Deep dive:
           product-strategy_companion.md section 3 (What We Are Not Doing) and section 7.
     ASK   What has been asked for repeatedly that we are now refusing? Who will be unhappy when they read
           this, and have we told them? If nothing here costs us anything, have we chosen?
     GOOD  "We are not shipping the customer-facing arrival-window feature this year. It is the most
           requested item in our backlog and it depends on scheduling accuracy we do not yet have."
     WEAK  "We are not going to compromise on quality or lose focus on the customer."
     TRAP  Listing only things nobody wanted. A refusal that costs nothing proves nothing. -->

{{what_we_are_not_doing}}

## How We Will Know It Is Working

<!-- WHAT  The change you expect to see, the measure that would show it, and roughly when. Two or three
           lines. One leading indicator matters more than five lagging ones.
     WHY   This is where the strategy becomes falsifiable. It is NOT your OKRs: OKRs measure a period's
           execution, while the strategy decides which objectives were worth setting in the first place, and
           practitioners warn specifically against letting the former replace the latter. Deep dive:
           product-strategy_companion.md section 3 (How We Will Know) and section 8.
     ASK   What number moves first if this is working? What would we see in eight weeks, not eight months?
           What result would make us abandon this strategy rather than try harder at it?
     GOOD  "Leading: dispatcher override rate on inferred priority, from 48 percent to under 20 percent by
           the end of Q2. Lagging: emergency jobs completed within the promised window. If the override rate
           has not moved by the end of Q2 we treat the diagnosis as wrong, not the execution."
           (one leading, one lagging, and a stated falsifier)
     WEAK  "Increase engagement and drive revenue growth."
           (no baseline, no date, nothing that could come back negative)
     TRAP  Pasting in this quarter's OKRs. If this section could be lifted into a planning tool unchanged,
           you have written objectives, not a way to tell whether the strategy is right. -->

{{how_we_will_know}}

## Assumptions and Risks

<!-- WHAT  What has to be true for this to work, and what would falsify it. Three to five, each with the
           evidence you have and the evidence you lack.
     WHY   In uncertainty the useful discipline is writing down assumptions to be tested rather than
           projections to be met. Ramp's published strategy template makes risk an explicit section, asking
           "why would we fail and what should we do about it". Deep dive:
           product-strategy_companion.md section 3 (Assumptions and Risks) and section 6.
     ASK   What are we assuming about users that we have not checked? Which assumption, if wrong, breaks the
           whole strategy rather than one action? What is the cheapest test of that one?
     GOOD  "We assume urgency is recoverable from the notes field. Evidence: three of five sampled
           emergencies had it there in plain language. Counter-evidence: we never looked at the two that did
           not, and they may be the expensive ones. Test: read the 40 most costly late jobs by 15 March."
           (falsifiable, with the gap in the evidence stated)
     WEAK  "Risk: competitors may launch similar features."
           (generic, not tied to this strategy, and no test)
     TRAP  Listing risks you cannot act on. A risk register is a different document; here, keep the
           assumptions this strategy would die without. -->

{{assumptions_and_risks}}

## Review Trigger

<!-- WHAT  What brings the team back to this document. An event, plus a backstop date.
     WHY   Strategies do not usually fail loudly; they go stale quietly. Named practitioners recommend
           reviewing at least every three months even for a strategy nominally spanning a year, and one
           team ties its cadence to a measurement rather than a calendar. Distinguish scheduled REVIEW from
           reactive rewriting: quarterly review is healthy, quarterly pivots triggered by a competitor's
           announcement are a symptom. Deep dive: product-strategy_companion.md section 3 (Review Trigger).
     ASK   What would have to happen for this to be wrong? Who is responsible for noticing? What is the date
           we look again even if nothing happens?
     GOOD  "Reviewed when the override rate moves 10 points in either direction, when a target-segment
           renewal is lost on scheduling accuracy, or on 31 August, whichever comes first. Owner: the head
           of product."
           (an event, a backstop, and a name)
     WEAK  "Reviewed quarterly."
           (a calendar entry with nobody attached and no trigger)
     TRAP  Making the trigger a competitor's launch. That is how a strategy becomes a series of reactions.
           Trigger on your own evidence. -->

{{review_trigger}}
