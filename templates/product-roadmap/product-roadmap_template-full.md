---
title: "{{product_name}} Product Roadmap"
product: "{{product_name}}"
owner: "{{who_owns_this_roadmap}}"
horizon: "{{period_this_covers}}"
audience: "{{internal_or_customer_facing}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
doc_type: product-roadmap
size: full
format: now-next-later
source_template: product-roadmap
source_template_version: 0.1.0
---

<!--
FULL PRODUCT ROADMAP (now-next-later format). Every section of product-roadmap_template-lean.md, in the same
order, plus the three a roadmap needs when it has to survive people who were not in the room: how confidence
decays across the lanes, what could move things, and what brings the team back to it.

USE FULL WHEN the roadmap will be read by someone outside the team: a leader, another function, a board, or
a customer. Use lean (product-roadmap_template-lean.md) when the team shares the context and needs a shared
view of what is in flight.

WHAT NOW / NEXT / LATER ACTUALLY MEANS. The lanes are levels of CONFIDENCE, not dates in disguise. Now is
work in progress, shaped and understood. Next is being sharpened and is expected to change. Later is a
problem area nobody has shaped yet. Its creators are explicit that the point is varying certainty: "No one is
100% sure all the time." If your Later lane reads like a dated plan, you have rebuilt the thing this format
exists to replace.

THE ONE SENTENCE THAT SETTLES MOST ARGUMENTS about this document, from the same source: "The roadmap shows
the plan. The OKRs carry the commitment." When someone asks this roadmap for a delivery guarantee, they are
asking the wrong artifact.

THE TEST THIS DOCUMENT HAS TO PASS. Could a reader build a Gantt chart from it? Then it stopped being a
roadmap. The distinction that survives even when a roadmap carries dates is that a project plan details how
work gets done, while a roadmap communicates why it is worth doing.

WHAT THE EVIDENCE ACTUALLY SAYS, SO YOU ARE NOT MISLED. No study links any roadmap format, cadence or
confidence device to product or business outcomes. What exists is a strong convergence of PRESCRIPTION: four
named practitioners, arguing independently, all arrive at "express less certainty, further out". That is
worth following and it is not proof. See product-roadmap_companion.md section 1.

A NOTE ON WHOSE PROCESS THIS IS. The word "roadmap" does not appear anywhere in the Scrum Guide. Whatever
framework you run, this artifact sits outside it and you are choosing to have one.

THIS IS ONE OF THREE FORMATS, AND THE CHOICE IS REAL.
- This one sorts by confidence. Reach for it when the honest answer to "when" is "it depends".
- product-roadmap_template-go-full.md is a goal-and-metric grid tied to named releases. Reach for it when
  releases are real and each one needs a measurable goal.
- product-roadmap_template-themes-full.md carries vision and business objectives alongside the themes.
  Reach for it when the roadmap has to argue for itself, not just list.
See product-roadmap_companion.md section 4.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   product-roadmap_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to
   avoid.
2. Replace each {{placeholder}} with your content.
3. Fill "The Outcome This Serves" FIRST. A roadmap whose items do not ladder to a stated outcome is a
   backlog someone reformatted.
4. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
5. If this roadmap will be seen by customers, read the external-audience rules in
   product-roadmap_companion.md section 9 BEFORE you fill it in. A public roadmap is a different document
   with different obligations, whatever the disclaimer says.
6. Before you share it: self-grade against product-roadmap_guide.md, then DELETE every HTML comment. They
   are guidance, not content.
-->

# {{product_name}} Product Roadmap

## The Outcome This Serves

<!-- WHAT  The measurable change this roadmap exists to produce, and the strategy or goal it descends from.
           Two or three sentences. Name the document above this one.
     WHY   This is what makes the lanes below judgeable. Without it a reader cannot tell whether an item
           belongs, and the roadmap drifts into a list of whatever accumulated. The failure has a name and a
           mechanism: when work is assembled bottom-up, "the intent behind the work has been quietly
           replaced by the gravity of the backlog itself." Deep dive: product-roadmap_companion.md section 3
           (The Outcome This Serves).
     ASK   What does the strategy above this say we are trying to change? How would we know this roadmap
           worked? If someone proposed an item that served no outcome, what would we point at to refuse it?
     GOOD  "Serves the FY26 goal of cutting emergency-job response time by a third. The dispatch strategy
           diagnosed the obstacle as urgency living in free-text notes, so everything below is aimed at
           getting priority out of prose and into the schedule."
           (names the parent, the measure, and the diagnosed obstacle)
     WEAK  "Improve the dispatch experience and deliver customer value."
           (nothing here could exclude any item)
     TRAP  Naming a goal nobody above you agreed to. If the strategy document does not say this, you are
           writing strategy in a roadmap, which is how a roadmap ends up being negotiated by people who
           never read it. -->

{{the_outcome_this_serves}}

## Now

<!-- WHAT  Work actually in progress, shaped and understood. Three to six items. Say what problem each one
           solves, not which feature ships.
     WHY   Now is the only lane where certainty is high enough to be worth stating, and even here the
           honest framing is a problem being solved rather than a feature being delivered. Themes exist for
           exactly this: "Instead of promising to build a specific feature, the team commits to solving a
           specific customer problem." Deep dive: product-roadmap_companion.md section 3 (Now).
     ASK   Is someone working on this today? Do we know what "done" looks like well enough to recognise it?
           Is this a problem or a solution, and if it is a solution, do we know it is the right one?
     GOOD  "Urgency inference at intake. Dispatchers should not have to read notes to find the emergency.
           In progress, first cohort of 20 accounts."
           (a problem, its current state, and a scope)
     WEAK  "Ship v2.4 of the scheduler." (a release, not a problem, and nobody outside the team can judge it)
     TRAP  Putting everything here because it all feels urgent. If Now has twelve items, it is a backlog. -->

{{now}}

## Next

<!-- WHAT  Problems being sharpened, expected to change. Two to five. Less detail than Now, deliberately.
     WHY   Next is where most roadmaps quietly become dishonest, because it is close enough that people
           want dates and far enough that estimates do not hold. The whole reason to sort by confidence is
           that "the further away something is, the more uncertain it is. Your roadmap should reflect
           that." Deep dive: product-roadmap_companion.md section 3 (Next).
     ASK   What would we have to learn before this could move to Now? Is this shaped, or just agreed to be
           important? Would we bet a quarter's capacity on it today?
     GOOD  "Override transparency. Dispatchers who disagree with an inferred priority currently have no way
           to say why, so we cannot learn from the disagreement. Shape after the first cohort reports."
           (says what has to happen before it becomes Now)
     WEAK  "Q3: Reporting improvements." (a date and a category, which is a timeline roadmap wearing a
           three-lane costume)
     TRAP  Letting Next become a promise. If a stakeholder can quote this lane back to you as a
           commitment, the lanes have collapsed and the format has stopped working. -->

{{next}}

## Later

<!-- WHAT  Problem areas nobody has shaped yet. Two to five, deliberately coarse. One line each.
     WHY   Later exists to show direction without implying a plan, and it is the lane that most often gets
           deleted by people who find it too vague. That vagueness is the honest content: a roadmap that
           looks equally certain at every horizon is claiming knowledge it does not have. Deep dive:
           product-roadmap_companion.md section 3 (Later).
     ASK   Is this a direction or a decision? Would we be embarrassed if this never happened? Is it here
           because we believe in it, or because someone senior mentioned it?
     GOOD  "Multi-day scheduling for planned maintenance work. We do not know whether this is the same
           product or a different one."
           (a direction with the open question stated)
     WEAK  "AI-powered predictive dispatch platform (Q4 2027)." (a date on a thing nobody has shaped is
           the exact false precision this lane exists to avoid)
     TRAP  Using Later as a graveyard for requests you do not want to refuse. Say no in the section below
           instead; a Later item nobody intends to do is a lie with a longer fuse. -->

{{later}}

## What Is Not On Here

<!-- WHAT  Things asked for, considered, and deliberately excluded this horizon, with one line each on why.
           Two to five. Name real requests.
     WHY   This is the section that makes the lanes usable, and the one most often missing. A roadmap
           without exclusions cannot be used to refuse anything, which means it settles no arguments and
           changes no behaviour. It is also what stops Later becoming a graveyard. Deep dive:
           product-roadmap_companion.md section 3 (What Is Not On Here) and section 7.
     ASK   What has been asked for repeatedly that we are not doing? Who will be unhappy, and have they
           been told? Is anything in Later actually a refusal we have not made yet?
     GOOD  "Customer-facing arrival windows. The most requested item we have, and it depends on scheduling
           accuracy we do not yet have. Revisit when the override rate is under 20 percent. Sales knows."
           (a real request, a reason, a condition for revisiting, and who was told)
     WEAK  "We are not doing anything that does not align with our strategy." (refuses nothing specific)
     TRAP  Listing only things nobody wanted. If every exclusion is uncontroversial, the hard refusals are
           still hiding in Later. -->

{{what_is_not_on_here}}

## Confidence, and How It Decays

<!-- WHAT  A plain statement of how certain each lane is, and what that means for anyone planning around it.
           Three or four lines, or a short table.
     WHY   The lanes already imply a gradient; this section makes it explicit so nobody has to infer it.
           One published rule of thumb puts the current quarter at around 90 percent accuracy with
           "decreasing accuracy for future quarters", which is a vendor's heuristic rather than a measured
           figure and should be presented as such. State your own gradient rather than borrowing a number
           you cannot defend. Deep dive: product-roadmap_companion.md section 3 (Confidence).
     ASK   What would we bet on each lane? If a customer planned their year around our Later lane, would we
           stop them? Have we ever moved an item backwards, and did anyone notice?
     GOOD  "Now is committed capacity and we expect to finish it. Next is directional: roughly half of what
           sits here in any quarter changes shape before it starts. Later is a statement of interest only;
           we have moved items out of Later more often than into Now."
           (honest, specific, and admits the direction of travel is not one-way)
     WEAK  "This roadmap is subject to change." (true of every roadmap ever written; tells a reader nothing)
     TRAP  Attaching percentages you have never measured. A made-up confidence number is worse than none,
           because it invites planning against it. -->

{{confidence_and_how_it_decays}}

## Dependencies and What Could Move It

<!-- WHAT  The things outside this team that the Now and Next lanes rest on, and the events that would
           reorder them. Three to five.
     WHY   Most roadmap slippage is not estimation error, it is a dependency nobody wrote down. Naming them
           converts an eventual surprise into a tracked risk, and it is the section that makes a roadmap
           useful to the functions who have to plan around it. Deep dive:
           product-roadmap_companion.md section 3 (Dependencies).
     ASK   What are we waiting on that we do not control? Which item dies if that dependency slips? What
           would we reorder first if capacity halved?
     GOOD  "Urgency inference needs the labelled job corpus, which only the support team can produce and
           which competes with their ticket load. If it slips past March, override transparency moves ahead
           of it, because it does not depend on the corpus."
           (a named dependency, an owner, and the reordering it would trigger)
     WEAK  "Dependencies: engineering capacity, third-party APIs, market conditions."
           (a category list; nothing here names a thing that could actually happen)
     TRAP  Listing dependencies without saying what they would move. A dependency with no consequence
           attached is decoration. -->

{{dependencies_and_what_could_move_it}}

## Review Trigger

<!-- WHAT  What brings the team back to this roadmap. An event, plus a backstop date and a named owner.
     WHY   Cadence is genuinely contested: some published guidance gives fixed intervals, at least once a
           year for planning and as often as weekly for feature-level views, while others argue a roadmap
           is a living document to be updated the moment anything is invalidated. Both positions are named
           and neither is measured, so choose one deliberately and write down which. Deep dive:
           product-roadmap_companion.md section 3 (Review Trigger) and section 6.
     ASK   What would tell us this roadmap is wrong rather than late? Who notices? What is the date we look
           again even if nothing happens?
     GOOD  "Reviewed when any Now item is invalidated by what we learn, when the parent strategy changes,
           or on 30 September, whichever comes first. Owner: the head of product. A competitor announcement
           is explicitly not a trigger."
           (an event, a backstop, an owner, and a named non-trigger)
     WEAK  "Reviewed quarterly." (a calendar entry with nobody attached)
     TRAP  Triggering on competitor activity. That is how a roadmap becomes a series of reactions, and it
           is listed elsewhere as a symptom rather than a practice. -->

{{review_trigger}}
