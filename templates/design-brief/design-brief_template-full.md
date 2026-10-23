---
title: "{{concept_name}} Design Brief"
concept_name: "{{concept_name}}"
author: "{{author}}"
approver: "{{approver}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: design-brief
size: full
source_template: design-brief
source_template_version: 0.1.0
---

<!--
FULL DESIGN BRIEF. Everything the lean variant carries, plus Constraints on the Design and Open
Questions for Design, inserted between The Chosen Concept and The Handoff, and The Handoff's Scope,
Time Line and Budget, inserted after The Handoff.

THIS VARIANT IS A STRICT ORDERED SUPERSET OF THE LEAN ONE. The four lean sections appear here under
the same headings, in the same order, with the same placeholders; three sections are inserted among
them. If you started lean, grow into this without rewriting anything you already filled in.

THE THREE ADDED SECTIONS REST MORE ON THIS LIBRARY'S OWN CONSTRUCTION THAN THE FOUR LEAN ONES DO. No
source this bundle's research read publishes a design-only constraints section, a time line or a
budget scoped to the handoff alone, or this exact Open Questions field, at this document's own
altitude. Each section below says so, at its own confidence, rather than presenting it as received
practice. Use this variant when a separate design team needs those limits, open questions, or a
design-scoped time and budget stated in writing, not only a chosen concept and a handoff; that
guidance is this library's own judgment. See design-brief_companion.md section 4.

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
   avoid. For the table, PRIORITY explains the ordering rule and ROW HINT says what a good row
   contains.
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

## Constraints on the Design

<!-- WHAT  Limits the design work itself must respect, that a project brief would not already
           carry.
     WHY   Kuse's guide gives constraints a numbered step, "6. Surface Constraints Early and
           Honestly," and its own definition names "the constraints that shape the solution."
           Heap's template carries a dedicated field too, "Key Constraints:" (cited here for its
           field name only, in its own solution sense); Kaninsky's own field asks the design team
           to describe what it should not challenge, such as a hard technical constraint or a
           platform change. This section rests on thin evidence: no source read publishes a
           design-only constraints section at this bundle's own altitude, and Kaninsky's list is
           the closest match, sitting in a kickoff brief written before research runs, a neighbour
           document rather than this one. Whether an accessibility obligation belongs here or in a
           later specification is contested: Design Pickle puts a compliance line directly in its
           own brief instructions, "Ensure compliance with accessibility standards (e.g.,
           sufficient color contrast)," while UXPin lists "accessibility requirements" among what a
           companion specification document carries. This template follows UXPin's split: name an
           accessibility obligation here as a limit the concept must respect, and leave its
           pass-or-fail criteria to the specification or PRD that follows. Deep dive:
           design-brief_companion.md section 3 (Anatomy > Constraints on the Design), section 6.
     ASK   What limit must the design work itself respect, that a project brief would not already
           carry? Is it a platform the team must not change, an existing flow the concept must not
           break, or an accessibility obligation the concept must meet? Name the kind of limit, not
           a project budget or deadline; those belong elsewhere.
     PRIORITY  List the constraint most likely to rule out an entire direction first, ahead of a
           smaller, local one.
     ROW HINT  A good row names a specific limit on the design work itself and says why it applies
           to design rather than to the whole project. A weak row restates a project limit already
           captured elsewhere, or states a goal rather than a limit.
     GOOD  | Must work within the existing transit app's notification settings screen, not a new
           app | The agency will not fund a second app this year, so any concept must live inside
           the current one |
     WEAK  | Should be user-friendly | | (a goal, not a limit, and no reason given)
     TRAP  Naming a limit that actually belongs to the whole project, such as a launch date or a
           total budget; those belong to a project brief or to this bundle's own Scope, Time Line
           and Budget section, never here. -->

| Constraint | Why it limits the design work |
|---|---|
| {{design_constraint}} | {{why_it_limits_design}} |

## Open Questions for Design

<!-- WHAT  What the design team still needs to find out, what is assumed true until they do, and
           what could block the design work itself, as distinct from what could block the whole
           project.
     WHY   Heap's template carries both named fields: "Open Questions," introduced by "This is a
           very early version of your design! All sorts of things are up in the air, or under
           debate. Capture them here," and a separate "Assumptions:" field. No other source read
           names either field at this bundle's own altitude, so this section rests on one
           practitioner template, at medium-low confidence; label this citation of Heap, like every
           other, as its own solution sense. What could block the design work is thinner still:
           Kaninsky's kickoff brief names "Dependencies" and "Risks" as fields of their own, and
           Basecamp's pitch carries "Rabbit holes - Details about the solution worth calling out to
           avoid problems"; both sit in neighbouring documents, a kickoff brief and a pitch, so
           treat them as weak corroboration rather than this bundle's own structural source. Deep
           dive: design-brief_companion.md section 3 (Anatomy > Open Questions for Design).
     ASK   What does the design team still need to find out before it can finish? What is being
           assumed true until they do? What could block the design work itself, separate from what
           could block the whole project?
     GOOD  "Open question: whether the notification channel the rider already uses for the app can
           fire fast enough after a schedule deviation is detected; the design cannot be finished
           until engineering confirms the latency. Assumption, held until design says otherwise:
           riders who opted into one saved route will accept a second opt-in for a different route,
           rather than expecting every route to notify by default. Could block design: the agency's
           own delay-detection feed updates on a schedule the design team does not yet have
           documented."
     WEAK  "There might be some open questions." (names no specific question, nothing a designer
           could act on)
     TRAP  Restating a constraint already named in Constraints on the Design, under a different
           label here. An open question is something nobody yet knows the answer to; a constraint
           is a limit already known and already fixed. Treating Heap's own structure as proof this
           document's sense may reach into solution detail is a related trap: Heap's headings are
           real, but its content is the solution sense throughout. -->

- Open questions: {{open_questions_design}}
- Assumptions: {{design_assumptions}}
- What could block the design work: {{design_blockers}}

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
           is updated, not the design itself, whenever a constraint or an open question above is
           resolved; design review happens separately, in the team's own weekly critique. The
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

## The Handoff's Scope, Time Line and Budget

<!-- WHAT  The scope of the design work handed off, when that work should finish, and any budget
           already set for the design work alone. Never a project's whole budget, a funding
           request, or commissioning terms.
     WHY   Basecamp's appetite is the clearest sourced time box, though it is a pitch's ingredient,
           not a brief's: "Appetite - How much time we want to spend and how that constrains the
           solution." UXPin gives the design work its own milestone, separate from the project's, a
           "Design handoff date," and Y Combinator asks the question directly: "1. When do you need
           the design?" This section's budget half rests on no source at all: every budget this
           research found scopes to the whole project, Kaninsky asking plainly, "What is your
           budget for this?" and Eleken bundling timeline and budget into one undifferentiated
           question, "7. What are the project timeline and budget?" Treat any figure placed here as
           the library's own construction, at low confidence, and never as this bundle's rule;
           where a team has no design-scoped budget at all, this field should say so rather than
           carry a project figure. Deep dive: design-brief_companion.md section 3 (Anatomy > The
           Handoff's Scope, Time Line and Budget).
     ASK   What is the scope of the design work handed off, named at the level of a kind of
           deliverable rather than a specific screen or flow? When should that work finish? Is
           there a budget set for the design work alone? If not, say so rather than carrying a
           project figure.
     GOOD  "Scope: a notification concept ready for a specification, covering how a rider opts in
           and what a notification says, not the delay-detection engineering behind it. Deadline:
           design complete by the end of the next sprint. Budget: none set for design work alone;
           the agency's quarterly design capacity covers it."
     WEAK  "Budget: $40,000 for the whole project." (a project figure standing in for a
           design-scoped one, which this section explicitly excludes)
     TRAP  Letting the whole project's budget or a funding request stand in for this section's own
           figure. Every sourced budget question this research found scopes to the whole project;
           this field, where it carries a number at all, holds the design work's own figure or says
           plainly that none exists. -->

- Scope of the design work handed off: {{design_scope}}
- When this work should finish: {{design_deadline}}
- Budget set for the design work alone, or a statement that none exists: {{design_budget}}
