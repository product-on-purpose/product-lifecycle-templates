---
title: "{{initiative_name}} Lean UX Canvas"
initiative_name: "{{initiative_name}}"
facilitator: "{{facilitator}}"
status: "{{status}}"
date: "{{date}}"
iteration: "{{iteration}}"
doc_type: lean-ux-canvas
size: lean
source_template: lean-ux-canvas
source_template_version: 0.1.0
---

<!--
LEAN UX CANVAS. This bundle ships one size, deliberately: Gothelf publishes the canvas as a single
one-page shape in both the 2019 and 2024 versions, and this research found no source that splits a
short form of the canvas from a longer one. See lean-ux-canvas_companion.md section 4 (Variants and
sizing).

WHAT THIS DOCUMENT IS, AND IS NOT. A Lean UX Canvas frames one initiative's business problem, the
outcomes the business wants, the users affected, the outcomes those users want, and candidate
solutions, then turns those links into testable hypotheses. It closes on the single most important
thing the team needs to learn right now and the smallest piece of work that would learn it. It is a
facilitation tool first: its originators call it a facilitation tool for cross-functional teams
designed to create a customer-centric conversation, and the filled page is the record of that
conversation, not the thing of value by itself. See lean-ux-canvas_companion.md section 1
(Orientation).

It is NOT a problem statement (that names which problem is worth solving, before anyone names a
solution; this canvas names candidate solutions in Box 5 and links them to outcomes in Box 6 - a
problem statement, where one exists, can feed Box 1, but nothing this research read makes that a
rule). It is NOT an experiment-design-doc (that plans one test of one hypothesis, with variants,
allocation, metrics and a decision rule; this canvas only picks which hypothesis to test next and
sketches the least work in a single box, Box 8). It is NOT a design-brief (that hands one chosen
concept to the people who will design it; this canvas has not chosen a concept, only named
candidates in Box 5). It is NOT a product-vision (that states a whole product's direction for
years; this canvas frames one initiative for weeks). It is NOT a user-persona (Box 3 names the
users in a line and may point to a persona; it is not the researched portrait itself). It is NOT
Ash Maurya's lean-canvas (that models a whole business - channels, revenue, cost structure - while
this canvas frames one initiative's hypotheses and asks nothing about revenue or cost). Where this
canvas sits relative to each of these neighbors is this library's own POSITION in places, not a
sourced sequence; see lean-ux-canvas_companion.md section 8 (Relationships to other artifacts) for
which lines are sourced and which are not.

THIS DOCUMENT IS REVISED WHILE THE INITIATIVE'S EXPERIMENTS RUN. After the smallest experiment in
Box 8 returns a result, the team asks Box 7's question again, and the evidence can even send the
team back to Box 1 if it shows the wrong problem, the wrong audience, or the wrong measure of
success was in play. It is finished when the team commits to building, changes course, or stops the
initiative, not on a calendar. Box 9 below exists to keep that history visible, rather than letting
the canvas go stale with no record of what changed. See lean-ux-canvas_companion.md section 3 (Box
9: Revisions and What Takes Over).

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   lean-ux-canvas_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP
   to avoid. For the two table sections, PRIORITY explains how to use the table and ROW HINT says
   what a good row contains.
2. Fill the boxes roughly in the order below on a first pass: Gothelf's own walkthrough starts at
   Box 1, and Box 6 cannot be written before Boxes 2 through 5 exist. Once the canvas is underway,
   any box can be revisited on its own.
3. If a section does not apply to this initiative, write "N/A" and one line of why, rather than
   deleting it.
4. This canvas is not finished when you first fill it; it is revised as experiments return results
   (see above). Before you first share a pass: self-grade against lean-ux-canvas_guide.md, then
   DELETE every HTML comment. They are guidance, not content.
-->

# {{initiative_name}} Lean UX Canvas

## Business Problem

<!-- WHAT  What changed in the world and why it makes this a problem worth the organization's
           attention right now, closing on a "how might we" question. Not a solution or a feature
           idea.
     WHY   Gothelf's own walkthrough of how to use the canvas starts here, naming the business
           problem statement before touching any other box. The box's closing "how might we"
           question also supplies the objective half of an OKR built from the canvas, with Box 2
           supplying the key results half. Deep dive: lean-ux-canvas_companion.md section 3 (Box 1)
           and section 8 (Relationships to other artifacts).
     ASK   What changed in the world that makes this worth the organization's attention now? What
           evidence shows this is a real problem rather than an assumption? If you ended this
           statement with "how might we," what question would it ask?
     GOOD  "Dispatchers at single-site depots phone every driver each morning to confirm status,
           after three depots reported drivers marked absent in error last quarter. How might we
           confirm a driver's status without a phone call?"
           (names what changed, cites evidence, ends on a how-might-we question)
     WEAK  "We should build an automated check-in feature."
           (a solution, not a problem, and no evidence of what changed)
     TRAP  Writing a solution or a feature idea into this box instead of the problem it would
           solve. That is Box 5's job, not Box 1's, and starting from a solution rather than a
           problem is the first of a community skill file's named pitfalls. -->

{{business_problem_statement}}

## Business Outcomes

<!-- WHAT  The measurable change in human behavior the business wants, stated as who does what, by
           how much. Not a revenue figure or an output count.
     WHY   Gothelf defines a business outcome as a measure of human behavior, not a number on a
           report, and has separately called this box perhaps the most critical one in the whole
           canvas, because its outcomes become the success criteria Box 6's hypotheses are later
           tested against. The 2024 prompt made that discipline more explicit by asking for the
           same who-does-what-by-how-much format his and Seiden's OKR book uses. Deep dive:
           lean-ux-canvas_companion.md section 3 (Box 2) and section 6 (Business outcomes against
           user outcomes).
     ASK   What will people do differently if this business problem is solved? Can you state it as
           who does what, by how much, and by when? Is this a behavior you can actually measure,
           not a sentiment or a revenue figure?
     GOOD  "Dispatchers who use the check-in feature make 80% fewer manual confirmation calls
           within 60 days of rollout."
           (a measured behavior, a magnitude, a timeframe)
     WEAK  "Dispatchers feel more confident in their fleet's status."
           (a feeling, not a measured change in behavior)
     TRAP  Writing a revenue figure or an output count here instead of a behavior change. Confusing
           this box with Box 4 is the canvas's best-documented point of confusion, and Gothelf's
           own revision of both boxes exists to draw that line. -->

{{business_outcome}}

## Users

<!-- WHAT  Who the team is solving for, named specifically enough that someone unfamiliar with the
           initiative could picture them, including anyone who configures the product or is
           affected by it, not only the person who buys or approves it.
     WHY   The 2024 wording widens this box past paying customers to anyone who configures the
           product or is affected by its use, and Gothelf tightened the box in 2019 because teams
           were taking a shortcut on it, treating it too casually. The book's own practice fills
           this box with proto-personas where the team has them. Deep dive:
           lean-ux-canvas_companion.md section 3 (Box 3).
     ASK   Who specifically uses or is affected by this, beyond whoever buys or approves it? Could
           someone outside the team picture this user from your description? Does a researched
           persona already exist that this box should point to, rather than inventing a thinner
           sketch for the canvas?
     GOOD  "Dispatchers at single-site depots who coordinate 15-40 drivers each morning, and the
           drivers themselves, who are affected by the check-in process even though they do not
           choose it."
           (names more than one affected group, specific enough to picture)
     WEAK  "Fleet managers."
           (too broad to act on, and skips the affected drivers entirely)
     TRAP  Naming only the buyer and skipping everyone else who configures or is affected by the
           product. Treating this box as a formality is exactly the shortcut Gothelf tightened the
           wording to stop. -->

{{users}}

## User Outcomes and Benefits

<!-- WHAT  What users want to achieve and how they want to feel, in language a user would
           recognize, not a restatement of the business outcome in different words. The 2024 prompt
           adds jobs-to-be-done language.
     WHY   Gothelf names this box as the part of the canvas with the most confusion, and resolves
           it directly against Box 2: business outcomes are measured behavior, while user outcomes
           are the reasons users seek out a product in the first place, often not measurable goals
           at all but intangible states of being. Deep dive: lean-ux-canvas_companion.md section 3
           (Box 4) and section 6, which also records a minority "ethics box" reading that Gothelf's
           own pages do not use.
     ASK   Why does this user actually seek this out, independent of what the business wants from
           them? What job are they trying to get done? How do they want to feel afterward, in
           language they would recognize?
     GOOD  "Dispatchers want to trust that a driver's status is accurate without double-checking it
           themselves, so they can start the day's routing without delay."
           (a reason to seek the product out, in the user's own language, distinct from the
           business's measured behavior)
     WEAK  "Dispatchers make 80% fewer calls."
           (this restates Box 2's business outcome, not a user outcome)
     TRAP  Writing the business outcome again in different words. Box 2 against Box 4 is the
           canvas's best-documented point of confusion, and filling either box with language that
           belongs in the other is, by Gothelf's own account, the single most common way a team's
           canvas becomes hard for anyone else to read. -->

{{user_outcomes_and_benefits}}

## Solutions

<!-- WHAT  Candidate solutions, listed as widely as the box invites, including at least one
           non-technical option, before narrowing to anything specific.
     WHY   The 2019 widening explicitly admits new systems, business models, and non-technical
           solutions, not only software features, and Gothelf's own guidance calls for ideas that
           can be big, small, innovative, or even a little unconventional. Naming a solution here
           does not commit the team to building it. Deep dive: lean-ux-canvas_companion.md section
           3 (Box 5).
     ASK   What candidate solutions, technical and non-technical, could address the user and
           business outcomes above? Have you listed more than one, or stopped at the first idea?
           Does at least one candidate not involve building new software?
     GOOD  "An automated SMS check-in; a geofence that logs arrival automatically; or,
           non-technically, a shared paper log the depot's shift lead photographs each morning."
           (more than one candidate, including a non-technical option)
     WEAK  "Build an automated check-in app."
           (a single idea; the box's own widening to several, non-technical candidates goes unused)
     TRAP  Stopping at one solution. A single idea in this box undercuts the box's own 2019
           widening and is one of six pitfalls a community skill file names. -->

{{candidate_solutions}}

## Hypotheses

<!-- WHAT  A table, one row per candidate hypothesis, each combining the business outcome, the
           user, the benefit, and the feature into a single sentence.
     WHY   This box combines Boxes 2 through 5 into one sentence carrying four slots: the business
           outcome, the user, the benefit the user attains, and the feature or solution that
           attains it. Each hypothesis should address exactly one feature; a hypothesis spanning
           several cannot be tested cleanly. Deep dive: lean-ux-canvas_companion.md section 3 (Box
           6) and section 7 (Anti-patterns and failure modes).
     ASK   For each candidate solution, what single hypothesis sentence links it to one business
           outcome and one user benefit? Does each row name exactly one feature, or has more than
           one been bundled into the same sentence?
     PRIORITY  One row per feature, never one row bundling several features into a single sentence;
           a bundled hypothesis cannot be tested cleanly. Rows are candidates, not ranked by this
           table; Box 7 is where the team picks one to test first.
     ROW HINT  A good row names the business outcome, the user, the benefit, and exactly one
           feature. A weak row omits a slot, or bundles two features into one sentence.
     GOOD  | H-01 | We believe 80% fewer manual confirmation calls will follow if dispatchers get confidence in driver status from an automated SMS check-in. |
     WEAK  | H-01 | We believe check-ins will improve if we build the SMS feature and the geofence feature. |
           (two features bundled into one sentence that cannot be tested cleanly)
     TRAP  Bundling more than one feature into a single hypothesis. The canvas's own rule is one
           feature per hypothesis, and a sentence spanning several features cannot be tested
           cleanly. -->

| ID | Hypothesis (business outcome, user, benefit, one feature) |
|---|---|
| {{hypothesis_id}} | We believe {{hypothesis_business_outcome}} will follow if {{hypothesis_user}} gets {{hypothesis_benefit}} from {{hypothesis_feature}}. |

## What We Need to Learn First

<!-- WHAT  One hypothesis chosen from the table above, the ways it might fail, and the single
           riskiest assumption behind it. Not a list of everything that could go wrong.
     WHY   Gothelf is pointed about scope here: the job is not to list every risk a hypothesis
           carries, but to identify the one thing that matters most to learn right now. In a
           hypothesis's early stages, the guidance favors risks to value over risks to feasibility.
           This box is revisited, not answered once: after an experiment from Box 8 returns, the
           team asks this box's question again. Deep dive: lean-ux-canvas_companion.md section 3
           (Box 7).
     ASK   Of all the ways this hypothesis could fail, which one matters most to learn about right
           now? Is this risk about whether users value the outcome, or only about whether the team
           can build it? After the last experiment returned, has this answer changed?
     GOOD  "The riskiest assumption behind the SMS check-in hypothesis is that dispatchers would
           actually trust a text reply over a phone call, not whether the SMS platform is
           technically feasible."
           (one named assumption, about value rather than feasibility)
     WEAK  "There are a lot of risks: cost, timeline, driver adoption, SMS reliability, and whether
           dispatchers like it."
           (a list, not a single named priority)
     TRAP  Listing every risk a hypothesis carries instead of naming the one thing most important
           to learn right now. That is exactly the shortcut Gothelf's own guidance warns against. -->

{{riskiest_assumption}}

## The Least Work to Learn It

<!-- WHAT  The smallest experiment that would show whether the riskiest assumption named above is
           true or false. Not a smaller version of the finished product.
     WHY   "MVP" in this context means a small and fast way of learning something, not a
           stripped-down release meant to ship. This box sketches the shape of a test; it does not
           plan one in the detail an experiment-design-doc would. Deep dive:
           lean-ux-canvas_companion.md section 3 (Box 8) and section 8 (Relationships to other
           artifacts).
     ASK   What is the cheapest, fastest way to learn whether the assumption above holds? Does this
           design actually test the assumption, or does it quietly become a smaller version of the
           final feature? If this needs a full test plan with variants and a decision rule, does
           experiment-design-doc need to take over from here?
     GOOD  "Ask five dispatchers to try replying to one manual SMS check-in for a week, with no app
           built, and track how many replies come back and whether dispatchers say they would
           trust it."
           (a fast way of learning, not a smaller release)
     WEAK  "Build a stripped-down version of the SMS app with only the core check-in feature."
           (a smaller release, not a fast way of learning)
     TRAP  Designing a smaller version of the eventual product instead of the fastest way to learn
           the answer. The originators are explicit that MVP here means a way of learning, not a
           release. -->

{{smallest_experiment}}

## Revisions and What Takes Over

<!-- WHAT  A dated row for each pass through the two boxes above, recording what was learned,
           whether the assumption held, and which boxes changed as a result. Then, once the canvas
           stops changing, the document that takes over.
     WHY   This section is this library's own addition. Its dated, iterative half is sourced: the
           canvas's own header carries date and iteration fields, and a community skill file treats
           the canvas explicitly as not a one-time exercise, to be revisited as the team learns.
           The successor half is this library's POSITION, not sourced: no source this research read
           names which document takes over once a canvas has served its purpose. This library names
           one, informed by one named consultancy's account of the canvas being abandoned in favor
           of other tools once a project reached enough definition, together with this family's own
           successor obligation. Deep dive: lean-ux-canvas_companion.md section 3 (Box 9) and
           section 8 (Relationships to other artifacts).
     ASK   What did the last experiment tell you, and did the assumption it tested hold?
           Which boxes did you change because of it, and what does Box 7 name now?
           Has the canvas stopped changing, and if so, did the team commit, change course or stop?
     PRIORITY  Add one row every time the team loops back through the two boxes above; do not
           overwrite an earlier row. Fill "What takes over" only once the canvas stops changing, not
           on a first pass.
     ROW HINT  A good row names the date, which assumption was tested, whether it held, and which
           boxes changed as a result. A weak row says only "tested" with no stated outcome.
     GOOD  | 2026-04-10 | Tested whether dispatchers would trust an SMS reply over a phone call | Held: 5 of 5 dispatchers replied within the pilot week and said they trusted it more than expected | Box 7 now names geofence reliability as the next riskiest assumption |
     WEAK  | | Tested the SMS idea | Went fine | |
           (no date, no clearly stated outcome, nothing named as having changed)
     TRAP  Leaving this section blank because a first pass feels finished. A canvas revised without
           a record cannot show what the team actually learned, which is exactly why this family's
           cadence exception requires one. -->

| Date | Assumption tested | What was learned | Boxes changed |
|---|---|---|---|
| {{revision_date}} | {{assumption_tested}} | {{outcome_learned}} | {{boxes_changed}} |

**What takes over when this canvas is finished**, because the team committed to building, changed
course, or stopped the initiative: {{successor_document}}.
