---
title: "{{study_name}} Research Plan"
study_name: "{{study_name}}"
author: "{{author}}"
approver: "{{approver}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: user-research-plan
size: lean
source_template: user-research-plan
source_template_version: 0.1.0
---

<!--
LEAN USER RESEARCH PLAN. The shortest form that still says why one study runs, what it must learn,
who takes part, and what the sessions will do, with the usability block (Tasks and Measures) carried
at every size because the alias "usability test plan" promises a reader it is there. Use it for a
study with no need to document earlier assumptions, roles, consent detail, or related links in their
own sections. To add What We Already Know, Roles and Observers, Consent, Privacy and Ethics, and
Related Documents, see user-research-plan_template-full.md. Never rename or reorder the sections
below; the full variant is a strict ordered superset of this one.

WHAT A USER RESEARCH PLAN IS, AND IS NOT
It is written before one study of the people a product serves. It says why the study runs, which
decision its findings will inform, what the team needs to learn, from whom, how, and when. Nielsen
Norman Group: "A research plan is a document that outlines the goals, methods, and logistical details
of a research study. (When planning a usability test, the research plan is often referred to as a
test plan.)" No second source states that identity in a sentence; three more give it structural
support without naming it. IT IS NOT a bare "test plan": this document and a separate bundle,
`test-plan`, share those two words, but `test-plan` verifies a product increment against a
specification, and this document studies how people use a product. IT IS NOT an experiment: Itamar
Gilad draws the line this library relies on, "Per this definition an A/B test is an experiment, but a
usability test is not," and his own next sentence must travel with that line wherever it is cited: "I
realize that this is not the common definition used in the industry - in many cases the words test and
experiment are used interchangeably. I chose this definition because it’s closer to how scientists
think of experiments." IT IS NOT the report: this plan names which decision the findings will inform
and stops; the recommendation itself is the not-yet-built `user-research-report`'s job. IT IS NOT the
session script: the moderator's opening, consent wording, and probes live in a linked session guide,
never pasted into this plan (catalog entry 25, an unbuilt candidate). IT IS NOT a "research brief":
that word carries at least four senses across the sources this bundle's research read, and none of
them is a synonym for this document. IT USUALLY COVERS ONE STUDY: Nielsen Norman Group states the
common case and its own exception together, "Typically, a research plan is constructed for each
study," though "sometimes, a research plan could include numerous studies or phases of research,"
naming interviews and a diary study as one pairing. IT STILL DECLARES DISCOVERY WORK FOR A SHIPPED
PRODUCT: a study that asks where people lose time or need help with something they already have is
still discovery work, by this library's own position; no source names a study of a shipped product as
discovery work in those words. See user-research-plan_companion.md sections 1, 6 and 7.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   user-research-plan_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP
   to avoid. For the Tasks and Measures table, PRIORITY explains the ordering rule and ROW HINT says
   what a good row contains.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, including Tasks and Measures when this study is not a usability test,
   write "N/A" and one line of why, rather than deleting the section.
4. Before you share this plan with stakeholders: self-grade against user-research-plan_guide.md, then
   DELETE every HTML comment. They are guidance, not content.
-->

# {{study_name}} Research Plan

## Why This Study, and the Decision It Informs

<!-- WHAT  Why the study runs now, and which decision its findings will inform. If this studies a
           product people already use, says why that is still discovery work.
     WHY   Dovetail ties the two together: "Background explains why the study exists and what
           decision it informs." Coleman sharpens it: "Start with the decision, not the question," and
           asks "What would change their choice." unitQ opens the same way: "What decision will this
           inform?" This library holds, as its own position, that a study of a product people already
           use is still discovery work when it looks for an opportunity rather than grading the
           product against a specification; no source names a shipped-product study as discovery work
           in those words. Deep dive: user-research-plan_companion.md section 3 (Anatomy > Why This
           Study, and the Decision It Informs), section 8.
     ASK   Why does this study run now? What decision will the findings inform, and what result would
           change that decision? If this studies something people already use, why is this still
           discovery work rather than a check against a specification?
     GOOD  "This study runs because the delivery-slot step has been proposed for redesign twice and
           deferred twice for lack of evidence. Decision it informs: whether to fund a redesign next
           quarter. If shoppers complete the step without confusion, the redesign drops off the
           roadmap."
     WEAK  "We want to understand how people feel about checkout." (no decision named, no reason the
           study runs now)
     TRAP  Naming a goal to understand or explore without naming the decision the findings would
           change. If nothing the study finds would change a decision, the study has no reason to
           run. -->

- Why this study runs now: {{why_now}}
- Decision the findings will inform, and what would change it: {{decision_informed}}
- If this studies something people already use, why it is still discovery work: {{shipped_product_note}}

## Goals and Research Questions

<!-- WHAT  One or two goals, and the three to five research questions the sessions must answer, stated
           as what the team needs to learn, not what a moderator will ask. A hypothesis may stand in
           for a question.
     WHY   Nielsen Norman Group: "Purpose and goals of the research study." Dovetail draws the
           load-bearing line: "Research questions describe what you need to learn, not what you'll ask
           participants," limited to "three to five per study." 18F agrees: "Research questions are
           different from interview questions." unitQ frames a hypothesis as a belief with a
           confirming condition. Deep dive: user-research-plan_companion.md section 3 (Anatomy > Goals
           and Research Questions).
     ASK   What is the one or two goals of this study? What three to five questions must the sessions
           answer? Could a hypothesis, a belief with a confirming condition, stand in for one of them?
     GOOD  "Goal: find where shoppers lose time choosing a delivery slot. Question: what makes a
           shopper hesitate before picking a slot? Hypothesis: we believe shoppers skip the cheapest
           slot because they distrust it will hold; we will know we are right if more than half
           mention price when they hesitate."
     WEAK  "Understand the delivery-slot experience." (a vague verb, not a question the sessions can
           answer)
     TRAP  Writing an interview question instead of a research question. "Walk me through picking a
           slot" belongs to the session guide; "What makes a shopper hesitate" is what the plan needs
           to learn. -->

- Goal(s): {{goals}}
- Research questions (three to five): {{research_questions}}
- Hypothesis, if one stands in for a question: {{hypothesis}}

## Method

<!-- WHAT  The method or methods, why they fit the questions, the session format and length, what
           participants will see, whether the study is generative or evaluative, and where the
           session guide and screener live.
     WHY   User Interviews: "How: Methodology." Nielsen Norman Group: "Method and procedure."
           digital.gov: "Note the method or methods of research you will be using, such as contextual
           inquiry or usability testing." Torres names the distinction this section carries:
           "Generative research helps teams discover opportunities... Evaluative research helps teams
           test which solutions will best address those opportunities." Nielsen Norman Group lists
           interview materials inside its own method section while also naming relevant documents
           separately; this plan follows the same pattern, naming the session guide here and, in the
           full variant, listing it again under Related Documents. Deep dive:
           user-research-plan_companion.md section 3 (Anatomy > Method).
     ASK   Which method fits these questions, and why? Is this generative or evaluative, qualitative
           or quantitative? What will participants see or use? Where do the session guide and screener
           live?
     GOOD  "One-to-one moderated sessions, about 30 minutes, on the live delivery-slot screen with a
           sample cart. Generative: we are looking for where shoppers lose time, not testing a
           specific redesign. Session guide: linked below."
     WEAK  "We'll talk to some users." (no method named, no format, no sense of generative or
           evaluative)
     TRAP  Naming a method without saying whether it is generative or evaluative. A reader cannot tell
           what the findings can and cannot settle without that distinction. -->

- Method(s), and why they fit the questions: {{method_and_fit}}
- Session format and length: {{session_format}}
- What participants will see or use: {{what_participants_see}}
- Generative or evaluative, qualitative or quantitative: {{study_kind}}
- Where the session guide and screener live: {{session_guide_link}}

## Participants and Recruiting

<!-- WHAT  Who qualifies and who does not, how many (with a backup count), how they are recruited and
           thanked or paid, what access needs you ask about, and how consent is taken.
     WHY   Nielsen Norman Group: "Participants." Dovetail: "Your plan should state who qualifies, who
           doesn't, and how many sessions you need." GOV.UK adds "how you'll cater for any access
           needs" and "how you'll find them within your budget." Maze names paying participants its
           own step, "Determine how you'll pay them." Pernice names a planned fallback, "intentional
           overrecruiting," because "each lost participant represents a fairly substantial proportion
           of your potential insights." Participant counts are contested across the sources, from
           NN/g's five for a qualitative study to its own 20 to 30 for a quantitative one; state the
           number chosen for this study, not a source's figure as a rule. AnswerLab argues for a
           demographic mix by default; DHS argues against worrying about it for a usability test.
           Deep dive: user-research-plan_companion.md section 3 (Anatomy > Participants and
           Recruiting), section 6.
     ASK   Who qualifies, and who explicitly does not? How many participants, and how many will you
           recruit as backup? How are they recruited and thanked or paid? What access needs will you
           ask about? How is consent taken (full detail lives in Consent, Privacy and Ethics, where
           this plan uses it)?
     GOOD  "Qualifies: placed 3 or more grocery orders this month, uses delivery. Does not qualify:
           anyone on the design team. 6 sessions, recruiting 8 for drop-outs. Recruited through the
           in-app panel, thanked with a 40-dollar gift card. Every participant is asked about access
           needs before scheduling."
     WEAK  "We need about 5 to 10 users, TBD." (no qualifying or disqualifying criteria, no recruiting
           channel, no incentive)
     TRAP  Quoting a participant count from a guide as a rule. The sources disagree widely; state the
           number chosen for this study and why. -->

- Who qualifies: {{who_qualifies}}
- Who does not qualify: {{who_does_not_qualify}}
- How many participants, and how many recruited as backup: {{participant_count}}
- How participants are recruited: {{recruiting_channel}}
- How participants are thanked or paid: {{incentive}}
- Access needs you ask about: {{access_needs}}
- How consent is taken: {{consent_summary}}

## Tasks and Measures

<!-- WHAT  For a usability test: each task as a scenario, a success criterion set before the sessions
           run, the measures the sessions will collect, and when questions run. For any other method,
           one line saying so, with the task table and the two lines under it marked N/A.
     WHY   The usability-test-plan identity is stated in a sentence by one publisher, Nielsen Norman
           Group: "A research plan is a document that outlines the goals, methods, and logistical
           details of a research study. (When planning a usability test, the research plan is often
           referred to as a test plan.)" For a usability test this is the heart of the plan, not a
           supplement: NN/g's own task guidance, "Strong tasks are concrete and free from clues that
           might prime people's behavior," and MeasuringU's, "Determine an objective success criteria
           for each task," both put it among their named items. Deep dive:
           user-research-plan_companion.md section 3 (Anatomy > Tasks and Measures), section 1.
     ASK   Is this a usability test? If not, name the method actually used and mark the rest N/A. If so:
           what is each task, as a scenario free of priming clues? What is its success criterion, set
           now? Which measures (time on task, success rate, error rate, satisfaction) will the
           sessions collect? When do questions run, before, between tasks, or after?
     PRIORITY  List tasks in the order participants attempt them. A success criterion is set now,
           before the sessions run, never scored after the fact.
     ROW HINT  A good row states the task as a scenario a participant could act on, with no clue to the
           right path, and a success criterion stated as an observable outcome. A weak row names a
           feature instead of a scenario, or leaves the criterion blank.
     GOOD  | 1 | You want produce delivered tomorrow evening. Find a delivery slot and confirm it. |
           Confirms a slot without asking for help, in under 90 seconds |
     WEAK  | 1 | Test the delivery-slot picker. | (blank) |
     TRAP  Treating this block as optional detail. For a usability test it is the core of the plan,
           not an appendix to it. -->

If this study is not a usability test, say so, name the method, and mark the table and the two lines below N/A: {{not_usability_test_note}}

| # | Task (as a scenario) | Success criterion |
|---|---|---|
| {{task_number}} | {{task_scenario}} | {{success_criterion}} |

- Measures this session will collect: {{measures}}
- When questions run (before, between tasks, after, or both): {{questionnaire_timing}}

## Schedule and Logistics

<!-- WHAT  Dates and session times, place or tool, how sessions are recorded and noted, the pilot
           session, and time scheduled for analysis.
     WHY   User Interviews: "When and where: Research schedule and logistics." GOV.UK: "Plan the
           session times" and "Arrange recording and note-taking." A pilot is strongly supported:
           GOV.UK's own "Run a practice session," Michigan Tech's "the protocols are pilot-tested
           before the actual tests are conducted," and Maze's caution that "your pilot participant has
           had no part in the usability testing process so far." Analysis time is contested:
           digital.gov suggests "twice as long as you give to data collection," GOV.UK "For every 2
           hours of research, you should do 1 hour of analysis"; the two figures may not measure the
           same thing, so state what you scheduled rather than either ratio as a rule. Deep dive:
           user-research-plan_companion.md section 3 (Anatomy > Schedule and Logistics), section 6.
     ASK   When and where do sessions run? How are they recorded and noted? Is a pilot scheduled, with
           someone who has had no part in the study so far? How much time is scheduled for analysis?
     GOOD  "Sessions run 2026-03-10 to 2026-03-14, 30 minutes each, over video, recorded with consent.
           Pilot: 2026-03-07, with a teammate from a different team who has not seen this work.
           Analysis: two days blocked after the last session."
     WEAK  "We'll schedule sessions sometime next month." (no dates, no recording plan, no pilot, no
           analysis time)
     TRAP  Skipping the pilot, or running it with someone already close to the work. -->

- Dates and session times: {{schedule}}
- Place or tool: {{location_or_tool}}
- How sessions are recorded and noted: {{recording_plan}}
- Pilot session, and with whom: {{pilot_plan}}
- Time scheduled for analysis: {{analysis_time}}

## What Happens to the Findings

<!-- WHAT  Which report or readout the study produces, for whom and by roughly when, how it will be
           structured if known, and which decisions the findings feed. Never a recommendation or a
           decision.
     WHY   User Interviews: "Next steps." Dovetail's "share-out plan." MeasuringU: "If possible, try to
           outline how the report will be structured in the test plan." Two qualifiers travel with
           this section: 18F warns, "Avoid over-specifying your outputs, because you don't know what
           you'll find until the research is underway," and DHS notes one of its own approaches "may
           or may not result in a formal report." What this section does not carry: unitQ's own next
           step, "a clear recommendation: build, iterate, keep exploring, or drop," belongs to the
           report, not this plan. Deep dive: user-research-plan_companion.md section 3 (Anatomy > What
           Happens to the Findings).
     ASK   What report will this produce, for whom, and roughly when? How will it be structured, if
           you can say now? Which decision named above will the findings feed? (Name no recommendation
           here; that is the report's job.)
     GOOD  "A short readout to product and design within a week of the last session, one section per
           research question. Feeds the go or no-go decision on funding the redesign. The exact shape
           is not locked, since we do not know what we will find."
     WEAK  "We'll write something up and recommend building the redesign." (names a recommendation
           before the study runs)
     TRAP  Writing the recommendation or the build-or-drop decision into this section. That is the
           report's job, once the sessions have run. -->

- Report or readout, for whom, and roughly when: {{findings_output}}
- How it will be structured, if known yet: {{findings_structure}}
- Which decision(s) named above the findings will feed: {{decisions_fed}}
