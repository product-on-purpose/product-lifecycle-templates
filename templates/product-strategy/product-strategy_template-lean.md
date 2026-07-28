---
title: "{{product_name}} Product Strategy"
product: "{{product_name}}"
owner: "{{who_owns_this_strategy}}"
period: "{{period_this_covers}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
doc_type: product-strategy
size: lean
format: kernel
source_template: product-strategy
source_template_version: 0.1.0
---

<!--
LEAN PRODUCT STRATEGY (kernel format). The smallest strategy that can still do a strategy's job: the
obstacle you have diagnosed, the approach you are taking to it, the action that follows, and what that rules
out. Four sections, one page. To grow it into a strategy that has to survive people who were not in the room
(see product-strategy_template-full.md), ADD sections; never rename or reorder the ones below, because the
full variant is a strict superset of this one.

THE TEST THIS DOCUMENT HAS TO PASS. Swap in a competitor's name. If it still reads true, you have described
an industry rather than made a choice. The second test is shorter: if nothing in it made anyone
uncomfortable, it is a wish list. Both come from practitioners, not from theory, and they are the reason
"What We Are Not Doing" is in the LEAN variant and not an optional extra.

WHAT THE EVIDENCE ACTUALLY SAYS, SO YOU ARE NOT MISLED. No study measures whether writing a product strategy
document improves product outcomes. There is a mixed literature on whether strategic PLANNING as a process
correlates with firm performance, and one study of listed firms found no correlation with objective
financial results while finding one with what managers BELIEVED. So "everyone felt it helped" is not
evidence. This template earns its place by making choices explicit, not by a proven effect. See
product-strategy_companion.md section 1.

THE KERNEL IS NOT THIS LIBRARY'S INVENTION. Diagnosis, guiding policy and coherent action come from Richard
Rumelt's Good Strategy Bad Strategy (2011). The headings are his; the guidance below is this bundle's.

THIS IS ONE OF TWO FORMATS, AND THE CHOICE IS REAL.
- This kernel starts from the obstacle. Reach for it when the hard part is that nobody agrees what the
  problem is.
- product-strategy_template-one-pager-full.md is a choice cascade (winning aspiration, where we will play,
  how we will win). Reach for it when the problem is understood and the hard part is choosing between
  places to compete.
They are different opening questions, not two sizes of one document. See product-strategy_companion.md
section 4.

WHAT A PRODUCT STRATEGY IS, AND IS NOT
It is the set of choices that gets you from where you are to the vision. It is NOT a vision (that is the
destination), NOT a roadmap (that is sequence and timing), NOT OKRs (those measure a period's execution),
and NOT a business strategy (that decides where the company invests). The strategy/roadmap boundary is the
one teams get wrong most often: the moment dates and feature names appear, you are writing the next document
down. See product-strategy_companion.md section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   product-strategy_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to
   avoid.
2. Replace each {{placeholder}} with your content.
3. Write the diagnosis first and do not move on until it names ONE obstacle. Every other section depends on
   it, and a strategy with a vague diagnosis fails quietly rather than loudly.
4. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
5. Before you share it: self-grade against product-strategy_guide.md, then DELETE every HTML comment. They
   are guidance, not content.
-->

# {{product_name}} Product Strategy

## Diagnosis

<!-- WHAT  The one thing that makes the goal hard. Not a summary of the market, not a list of challenges:
           the single obstacle that, if it went away, would make the rest straightforward. Two or three
           sentences.
     WHY   This is the section that separates a strategy from a wish. Rumelt's test is that if you fail to
           identify and analyse the obstacle you do not have a strategy, you have "either a stretch goal, a
           budget, or a list of things you wish would happen". Everything downstream is an answer to this
           paragraph, so a vague diagnosis produces a document that cannot be wrong and therefore cannot be
           useful. Deep dive: product-strategy_companion.md section 3 (Diagnosis).
     ASK   What is actually stopping us? If this obstacle disappeared overnight, would the goal become easy?
           Is this a cause or a symptom? Would a competitor recognise this as their obstacle too, and if so,
           have we named ours?
     GOOD  "Analysts can answer any question we support, but only by asking us. Every self-serve path we
           have shipped assumes the user already knows which table to start from, and 70 percent of new
           accounts never build a second view. Our growth problem is not acquisition, it is that the product
           requires expertise we cannot ship."
           (one obstacle, evidenced, and it rules some responses out)
     WEAK  "The market is increasingly competitive and customers expect more from analytics tools. We need
           to keep innovating to stay ahead."
           (true of every company in the category; names nothing that could be wrong)
     TRAP  Writing the goal here instead of the obstacle. "We need to grow self-serve revenue" is a target.
           The diagnosis is why that has not already happened. -->

{{the_diagnosis}}

## Guiding Policy

<!-- WHAT  The approach you are taking to the obstacle above. One paragraph. It should constrain: a reader
           should be able to name a reasonable option it rules out.
     WHY   A guiding policy is a direction, not a plan. Rumelt's image is guardrails: it directs and
           constrains action without fully defining it. If every option that was on the table last month
           still survives this paragraph, it is not a policy, it is a preamble. Deep dive:
           product-strategy_companion.md section 3 (Guiding Policy).
     ASK   What does this rule out? Which team's current plan changes because of this? If someone disagreed
           with us, what would they be arguing for instead? Is this an approach, or a restatement of the
           goal?
     GOOD  "We will make the product usable without product expertise, rather than making expertise easier
           to acquire. Where we have a choice between teaching the user and removing the need to know, we
           remove the need to know."
           (an approach with a real alternative it rejects: better documentation and training)
     WEAK  "We will focus on delivering an excellent user experience and driving self-serve growth."
           (names no alternative, so it forbids nothing)
     TRAP  Listing several policies. If you have three, you have not chosen; you have deferred the choice to
           whoever reads this next, and they will pick the one that suits them. -->

{{the_guiding_policy}}

## Coherent Action

<!-- WHAT  The moves that carry out the policy, and how they reinforce each other. Three to five, as prose
           or a short list. Each should be a kind of work, not a dated deliverable.
     WHY   The word doing the work is "coherent". Porter's argument is that fit is what makes a position
           durable, because it "locks out imitators by creating a chain that is as strong as its strongest
           link": actions that each make sense alone but do not reinforce each other are a list, not a
           strategy. Deep dive: product-strategy_companion.md section 3 (Coherent Action).
     ASK   Does each action serve the policy, or just seem generally good? Which two of these make each
           other stronger? If we dropped one, would the others still work? Are these kinds of work, or
           are they release dates wearing a disguise?
     GOOD  "1. Ship question-first entry points, so the first interaction is a question rather than a
           schema. 2. Move our modelling work into defaults, so a new account has useful views on day one.
           3. Instrument the second-view moment as our leading indicator, so every team can see the same
           obstacle we diagnosed. The first two remove the need for expertise; the third keeps us honest
           about whether we did."
           (each serves the policy, and they compound)
     WEAK  "Launch AI assistant in Q3. Redesign onboarding. Hire two designers. Improve documentation."
           (a dated to-do list; nothing here reinforces anything else)
     TRAP  Writing the roadmap. If a reader could build a Gantt chart directly from this section, it has
           stopped being strategy. Sequence and timing belong in the roadmap, which is downstream of this
           document. -->

{{the_coherent_action}}

## What We Are Not Doing

<!-- WHAT  The things you are explicitly declining this period, and one line each on why. Two to five. Name
           real options, not straw ones.
     WHY   This is the section that makes the other three usable, and the one most often missing. The test
           practitioners actually apply is whether the team can say "this is a really great idea... but
           we're not going to build it" and mean it. A strategy that makes nobody uncomfortable is a wish
           list. Deep dive: product-strategy_companion.md section 3 (What We Are Not Doing) and section 7.
     ASK   What has been asked for repeatedly that we are now refusing? Which of these would a competitor
           happily do? Who will be unhappy when they read this, and have we told them? If nothing here
           costs us anything, have we actually chosen?
     GOOD  "1. We are not building a mobile authoring experience this year. Mobile is 4 percent of authoring
           sessions and it competes for the same design capacity as question-first entry. 2. We are not
           pursuing the enterprise data-governance RFPs. They are winnable but they pull us toward the
           expertise-heavy product we are trying to stop being."
           (both were live options; both have a named cost)
     WEAK  "We are not going to compromise on quality or lose focus on the customer."
           (nobody was proposing either; refusing nothing)
     TRAP  Listing only things nobody wanted. A refusal that costs nothing proves nothing. If every item
           here is uncontroversial, the hard choice is still hiding somewhere else in the document. -->

{{what_we_are_not_doing}}
