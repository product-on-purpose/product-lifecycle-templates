---
title: "{{concept_name}} Design Brief"
concept_name: "{{concept_name}}"
author: "{{author}}"
approver: "{{approver}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: design-brief
size: lean
source_template: design-brief
source_template_version: 0.1.0
---

<!--
LEAN DESIGN BRIEF. The shortest form that still hands one chosen problem and one chosen concept to
the people who will design it: The Challenge, Who It Is For and What We Learned, The Chosen Concept,
and The Handoff, in that order. Use it when a team's own designers are already close to the work and
need no separate limits, open questions, or a design-scoped time and budget stated in writing. To
grow it into a form that also carries design constraints, open questions, and the design work's own
scope, time line and budget, see design-brief_template-full.md. ADD sections between The Chosen
Concept and The Handoff, and after The Handoff; never rename or reorder the sections below, because
the full variant is a strict ordered superset of this one.

WHAT A DESIGN BRIEF IS, AND IS NOT, IN THIS BUNDLE'S SENSE
The term has no settled meaning in the wider literature: "There is no clear or univocal definition
in the literature." At least four senses recur across the sources this bundle's research read: a
commissioning agreement between a client and a designer; a technical and visual specification; a
chosen problem framed for design; and a worked solution. THIS DOCUMENT BUILDS A CHOSEN PROBLEM PLUS
A CHOSEN CONCEPT: it hands a chosen problem and the one concept chosen for design to the people who
will design it, at Define's close, per the Design Council's own placement, "The result is to create
a design brief which clearly defines the challenge based on these insights." No single source
publishes exactly this shape; the composition is this library's own, and every section below says
so honestly rather than claiming received practice.

A CONCEPT NAMES THE KIND OF ANSWER, NEVER HOW IT WORKS. "Concept" is not shared vocabulary: Shape
Up's own description of a shaped concept reads, by this library's own line, as a specification
already, "It defines what the feature does, how it works, and where it fits into existing flows."
This document stops one altitude short of that: name the kind of answer the team will pursue, and
leave what a screen shows, what a button does, or how a flow proceeds to the document this brief
hands off to.

IT IS NOT a problem statement (this library's own `problem-statement` bundle already names the
chosen problem; where one exists, point to it rather than reframing it here). IT IS NOT a project
brief (which asks a named approver for authority to start finding out whether and how to proceed;
this document asks for no authority, and names a concept already chosen). IT IS NOT a business case
(no source read orders the two against each other; a brief may hand on a concept the case later
weighs as one option, at medium-low confidence). IT IS NOT a specification, a product design
specification, or the PRD (Ignitec's own line draws it cleanly, "The commercial considerations will
come later when you write your product design specification," and UXPin agrees, "A design brief
outlines what designers must create, while the specifications define specific details"). IT IS NOT
the Shape Up pitch (catalog entry 45, unbuilt): a pitch arrives shaped, "A problem without a
solution is unshaped work," and exists to be bet on, "The purpose of the pitch is to present a good
potential bet"; this document hands over a concept and asks for no bet. IT IS NOT a Design Sprint
brief (Google Ventures' own page names a five-day process and publishes no separate Sprint Brief).
IT PRECEDES a creative brief where a team already writes one: "In many design workflows, the
creative brief informs the design brief, ensuring visual decisions support broader project goals."
RECORDING APPROVAL IS NOT GRANTING INVESTMENT BACKING: The Handoff section may record that design
was approved, by whom and when; it is never the record that authorizes a project or its budget. And
MANY TEAMS WRITE NONE OF THIS AT ALL: "in many of the interviews the projects discussed started
without a design brief." See design-brief_companion.md sections 6 and 8.

THIS DOCUMENT IS REVISED WHILE DESIGN RUNS, UNLIKE MOST OF ITS `discovery-docs` SIBLINGS. "design
briefs are seldom fixed, static documents, but rather, they are often dynamic and evolve as the
project progresses," and a brief "should be used as a validation tool periodically throughout the
project when making key decisions." It is finished when the design work it hands off is done, not
on a standing cadence. See design-brief_companion.md section 2.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   design-brief_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to
   avoid.
2. Replace each {{placeholder}} with your content. Name no screen, no flow, no requirement, and no
   project budget or authorization anywhere in this document; those belong to a later document.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you hand this to the people who will design from it: self-grade against
   design-brief_guide.md, then DELETE every HTML comment. They are guidance, not content.
-->

# {{concept_name}} Design Brief

## The Challenge

<!-- WHAT  The chosen problem, restated for the people who will design it, and what a good outcome
           would change. Points to a problem statement and to success measures if either already
           exists, rather than restating them.
     WHY   The Design Council's own phrase anchors this section: a brief "clearly defines the
           challenge based on these insights." Jones and Askland describe the same job from the
           reader's side: a brief exists "to help the designer to understand the problem by
           defining the objectives and parameters of the project toward generating the most
           appropriate solution." Kuse's own definition agrees: a brief "defines the problem a
           design needs to solve, the context in which it exists, and the constraints that shape
           the solution." Deep dive: design-brief_companion.md section 3 (Anatomy > The Challenge).
     ASK   What is the chosen problem, in the fewest words that still say it accurately? What would
           a good outcome change for the people who have it? Does a problem statement already
           exist for this problem? If measures of success already exist somewhere, where do they
           live?
     GOOD  "Riders of the regional bus system have no way to see a delay until they are already
           standing at the stop, and the October rider survey named this the top reason for missed
           transfers. A good outcome lets a rider learn about a delay before they leave home.
           Problem statement: see the Delay Visibility problem statement, dated 2026-03-02. Success
           measures: see that document's success-measures section."
     WEAK  "Build a notification feature for delays." (names a solution instead of restating the
           problem, and gives a designer nothing to design against)
     TRAP  Restating the problem in language that already describes a specific solution. If the
           sentence names a screen, a button, or a channel, it has moved from the challenge into
           the chosen concept, a section below. -->

{{challenge}}

- What a good outcome would change: {{good_outcome}}
- Problem statement already written, if one exists: {{problem_statement_reference}}
- Where success will be measured, if already defined elsewhere: {{success_measures_reference}}

## Who It Is For and What We Learned

<!-- WHAT  Who the design serves, named specifically enough to design for, and the one research
           insight the challenge above rests on.
     WHY   Kuse's guide gives users their own numbered step, "4. Describe Users and Real Use
           Contexts." The Design Council frames the insight half of the job directly, closing on
           "understanding how user needs and the problem align." Y Combinator asks the evidence
           question plainly: "Have you done any user observations? If yes, will you be able to
           share the process and the findings?" Deep dive: design-brief_companion.md section 3
           (Anatomy > Who It Is For and What We Learned).
     ASK   Who does this design serve? Does an existing persona already describe this group? What
           is the single research insight the challenge rests on?
     GOOD  "Commuters who board at an unstaffed stop, mostly during the morning and evening peak.
           Insight: the October rider interviews found that riders check a transit app before
           leaving home, but stop checking once they are already walking to the stop, so a delay
           that appears only in-app after departure is invisible exactly when it matters most."
     WEAK  "Our riders." (no group named specifically enough to design for, no insight stated)
     TRAP  Re-running the whole research study in this section. One insight, stated in a sentence
           or two, is enough; the rest belongs to the research itself, not to this brief. -->

- Who the design serves: {{who_it_serves}}
- Existing persona, if one already describes this group: {{persona_reference}}
- Research insight the challenge rests on: {{research_insight}}

## The Chosen Concept

<!-- WHAT  The candidate concepts weighed, at the level of the kind of answer; the one chosen and
           why; and what the chosen concept deliberately leaves out.
     WHY   The Eleven Lessons report places the moment: "the Define stage would end with final
           sign-off of the concept." What the concept leaves out is this section's best-sourced
           element: Heap's own template (cited here for its field name only, never for its
           solution-level content) carries a dedicated field for it, "Not Doing," and Basecamp's
           pitch carries the same move under a different name: "shaped work indicates what not to
           do. It tells the team where to stop." Deep dive: design-brief_companion.md section 3
           (Anatomy > The Chosen Concept), section 6.
     ASK   What candidate concepts did the team weigh, at the level of the kind of answer? Which
           one was chosen, and why that one over the others? What does the chosen concept
           deliberately leave out?
     GOOD  "Candidates weighed: a home-screen widget showing the next scheduled delay, set aside
           because most riders do not add a transit widget and support calls showed riders check
           inside the app already. Chosen: a notification triggered by a schedule deviation on the
           rider's saved routes, delivered through the channel the rider already uses for the app.
           Chosen because it reaches a rider before departure, the moment the insight above names
           as the one that matters, and because it needs no new habit from the rider. Leaves out:
           the exact wording, how far in advance it fires, and whether it appears on a lock screen
           or inside the app alone; those are for the design work to resolve."
     WEAK  "A push notification that says 'Bus 14 delayed 6 minutes' and appears on the lock screen
           with a snooze button." (names exact wording and a specific interface element, how the
           concept works rather than what kind of answer it is)
     TRAP  Writing the chosen concept at the level of a shaped solution. If the sentence says what
           a screen shows, what a button does, or how a flow proceeds, it has crossed from a
           concept into a specification; that content belongs to the document this brief hands off
           to, never here. -->

- Candidates weighed, and why each was set aside: {{concept_candidates}}
- Chosen concept: {{chosen_concept}}
- Why this one: {{why_chosen}}
- What this concept deliberately leaves out: {{concept_excludes}}

## The Handoff

<!-- WHAT  Who will design from this brief and what they receive; who approved design to begin and
           when; how the brief stays current while design runs; who decides when feedback on the
           design conflicts; and which document takes over once the concept is specified.
     WHY   Kaninsky states the audience-alignment job directly: his brief exists "to get designers,
           product managers and software engineers on the same page before any research and
           design activities even start." Recording approval is this section's clearest sourced
           content: Kaninsky's template asks "Who is the ultimate decision-maker (sign-off)?," and
           the Eleven Lessons report places the moment this bundle's own record points back to,
           "the Define stage would end with final sign-off of the concept." Recording approval is
           not the same as granting it: the same report describes what the sign-off actually buys,
           "the corporate and financial backing to the development of one or more concepts that
           have addressed the initial problem." That backing is the investment decision the
           `discovery-docs` family contract excludes from every `define` member; this section may
           record that design was approved, by whom and when, and it is never the record that
           grants the backing itself. Which document takes over is this bundle's own POSITION:
           Ignitec names the boundary cleanly, "The commercial considerations will come later when
           you write your product design specification," and UXPin agrees, "A design brief outlines
           what designers must create, while the specifications define specific details." One named
           team skips that step: at Heap, once its own review clears (its own solution sense, cited
           for this one fact alone), "the design brief allows engineers to start scoping and
           building at least the back end." Who settles a conflict in design feedback is supported
           but unhomed in any single published template: Kuse's guide asks "Who approves final
           designs" and "How conflicts will be resolved," and Figr names an "Approval path: Who
           decides when feedback conflicts." Deep dive: design-brief_companion.md section 3
           (Anatomy > The Handoff), section 6.
     ASK   Who will design from this brief, and what exactly do they receive? Who approved design
           to begin, and when? How will this brief stay current while design runs, and does that
           mean reviewing the brief itself or reviewing the design as it proceeds? Who decides when
           feedback on the design disagrees? Which specific document takes over once the concept is
           specified?
     GOOD  "The in-house design team designs from this brief, receiving this document plus the
           October rider-interview notes. Approved by the Head of Product, 2026-03-10. This brief
           is updated, not the design itself, whenever the challenge or the chosen concept
           changes; design review happens separately, in the team's own weekly critique. The
           design lead settles any disagreement in rider feedback. The design specification takes
           over once the concept is designed."
     WEAK  "Design will figure it out, and we'll check in eventually." (no named team, no approver,
           no date, no named decider, no named next document)
     TRAP  Treating the sign-off recorded here as the decision that funds or authorizes the
           project. The brief may record that design was approved, by whom and when; it is never
           the record that grants a project its backing. -->

- Who will design from this brief, and what they receive: {{design_team}}
- Approved by, and when: {{approver}}, {{approval_date}}
- How this brief stays current while design runs, and which review that means: {{revision_process}}
- Who decides when feedback on the design conflicts: {{feedback_decision_owner}}
- What takes over once the concept is specified: {{next_document}}
