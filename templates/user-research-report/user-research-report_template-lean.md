---
title: "{{study_name}} Research Report"
study_name: "{{study_name}}"
author: "{{author}}"
plan_link: "{{plan_link}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: user-research-report
size: lean
source_template: user-research-report
source_template_version: 0.1.0
---

<!--
LEAN USER RESEARCH REPORT. The shortest form that still answers the plan's own questions, states what
the study found, and recommends what to do next, with Task Results carried at every size because the
catalog alias "usability test report" promises a reader it is there. Use it for one audience who
needs the decision and the evidence behind it, not the study's full background or its raw materials.
To add Background and Objectives, Open Questions, and Appendix, see
user-research-report_template-full.md. Never rename or reorder the sections below; the full variant is
a strict ordered superset of this one.

WHAT A USER RESEARCH REPORT IS, AND IS NOT
It is written after one study of the people a product serves, and it answers the questions a plan set
before the sessions ran. Dovetail: "A report packages several insights into a narrative for a specific
audience, with method, context, and recommendations." User Interviews: "A research report is a
document that summarizes all the details of a research study, including the research questions,
methodology, notable insights, and recommended next steps." IT IS NOT the plan: the plan sets the
questions before the study runs; this report answers them after. IT IS NOT a decision record: this
report recommends, and a recommendation names a change worth weighing, but it names no concept as
chosen and records no decision. That is a later document's job, such as `design-brief` or
`problem-statement`. IT IS NOT a QA test report: `test-summary-report` verifies a product increment
against an agreed specification and grades it; this report studies how people use a product and
records observations, not a verdict against a specification. Avoid the bare phrase "test report" or
"test results" for either document; name this one fully, as a usability study report or a user
research report. IT IS NOT an experiment readout: a usability study assigns no participant to a
variant and applies no decision rule against a baseline, which is the line this library draws between
a test and an experiment. IT STILL DECLARES DISCOVERY WORK FOR A SHIPPED PRODUCT: a study that asks
where people lose time with something they already have is still asking the generative question, not
the evaluative one, whatever the product's own age. See user-research-report_companion.md sections 1,
6, 7 and 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   user-research-report_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the
   TRAP to avoid. For a table, PRIORITY explains the ordering rule and ROW HINT says what a good row
   contains.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, including Task Results when this study is not a usability test, write
   "N/A" and one line of why, rather than deleting the section.
4. Before you share this report: self-grade against user-research-report_guide.md, then DELETE every
   HTML comment. They are guidance, not content.
-->

# {{study_name}} Research Report

## Summary

<!-- WHAT  The answer up front: what the study found and what it recommends, in a few lines. May also
           name the decision these findings inform and who makes it.
     WHY   Dovetail: "Put the headline finding in the first three sentences-don't make readers excavate
           it". Maze: "Lead with a short summary of key findings and recommendations, then add the
           context people need-such as why you conducted the study and the methods you used." NIST's
           template, customized for usability testing of Electronic Health Records (EHRs), opens the
           same way: "1 EXECUTIVE SUMMARY". No shipped source names this pairing as its own heading, but
           Dovetail's "End each finding with what the team should do about it, and who decides" and
           Useberry's "Lead with decisions, then show the evidence" both put the decision at or near the
           top, not buried in a methodology section. Deep dive: user-research-report_companion.md
           section 3 (Anatomy > Summary).
     ASK   What did the study find, and what does it recommend, in a few lines? What decision do these
           findings inform, and who makes it, if naming that helps the reader?
     GOOD  "Found: people delete duplicate photos one at a time because the bulk-select control reads
           as a filter toggle; 7 of 9 participants never used it. Recommend: make bulk-select the
           default view once duplicates are found. Decision this informs: whether to prioritize the
           redesign next sprint, decided by the mobile lead."
     WEAK  "Participants had some issues with duplicate photos and we have some ideas." (no answer
           stated, no recommendation, no decision named)
     TRAP  Opening with the method or the participant count instead of the answer. A reader who stops
           after one paragraph should already know what the study found. -->

- What the study found, and what it recommends: {{headline_summary}}
- Decision these findings inform, and who makes it: {{decision_and_owner}}

## Research Questions and Answers

<!-- WHAT  Each question the plan set, with a short answer and the findings behind it. Whether the
           answer confirms the plan's hypothesis, where it had one. A question the study could not
           answer says so.
     WHY   UserTesting's detailed report form carries "Research Questions" as its own item. User
           Interviews ties the section to the plan directly: "Actionable reports should relate back to
           the initial research question: How do your findings influence the decisions you mapped out
           in your research plan?" This library holds, as its own position drawn from this family's
           contract, that a report answers the questions the plan set out. Anderson-Stanier names the
           failure mode this row guards against: "There are questions out there that qualitative, and
           even quantitative, research simply cannot answer and we need to let our teams know when a
           question is unanswerable." Deep dive: user-research-report_companion.md section 3 (Anatomy >
           Research Questions and Answers).
     ASK   What was the question, in the plan's own words? What is the short answer, and which findings
           support it? If the plan stated a hypothesis, did the answer confirm or contradict it? Did the
           question stay open, and if so, why?
     PRIORITY  One row per question the plan set, in the plan's own order. Add no new questions here;
           a pattern the study turned up that the plan never asked belongs in Key Findings instead.
     ROW HINT  A good row restates the question, gives a short answer backed by a finding, and says
           plainly whether it confirmed a stated hypothesis or stayed open. A weak row answers a
           different, broader question than the one asked.
     GOOD  | What makes someone miss the bulk-select control? | It reads as a filter toggle; 7 of 9
           missed it on first use. | Confirmed the plan's hypothesis. | Answered |
     WEAK  | How do people feel about duplicate photos? | They find them annoying. | | Answered |
     TRAP  Summarizing the study's themes instead of answering the plan's own questions one by one,
           including a question nobody happened to raise in conversation but that the plan still
           asked. -->

| Research question (as the plan wrote it) | Answer | Confirms the plan's hypothesis? | Status |
|---|---|---|---|
| {{research_question}} | {{research_answer}} | {{confirms_hypothesis}} | {{question_status}} |

## What We Did

<!-- WHAT  The method, the participants, and the dates, the limits of the sample stated as a fraction
           with its denominator, and one line on anything that ran differently from the plan.
     WHY   Dovetail's own list carries "method and participants". NIST's template, inside the same
           EHR customization, structures the same content under "3 METHOD" and "3.1 PARTICIPANTS".
           UserTesting's detailed form carries "Methodology (e.g., unmoderated usability tests,
           surveys, etc.)". Sauro names the specific limit a small sample carries: "the key limitation
           is that you are limited to detecting large differences between designs or measures". The
           one-line deviation note is this library's own arrangement, the same device
           `experiment-readout` carries in its own Context and Setup section; no source instructs a
           report to note a deviation from its own plan. Deep dive: user-research-report_companion.md
           section 3 (Anatomy > What We Did).
     ASK   What method did the study use, and does it match the plan? Who took part, stated as a
           fraction of those recruited? When did sessions run? What does a sample this size let you
           claim, and what does it not let you claim? Did anything run differently from the plan, and if
           so, what and why, in one line?
     GOOD  "One-to-one moderated interviews with a walkthrough of each participant's own camera roll,
           2026-03-10 to 2026-03-14. 9 of 10 recruited completed a session; one dropped for a scheduling
           conflict. A sample this size can surface a large, frequent problem; it cannot rank two
           close icon designs against each other. Ran as planned, except two sessions moved to phone
           calls when video access failed."
     WEAK  "We talked to some users and took notes." (no method named, no participant count or
           denominator, no dates, no stated limit)
     TRAP  Reporting a participant count with no denominator, so a reader cannot tell how many actually
           ran against how many were recruited. -->

- Method, and whether it matches the plan: {{method_used}}
- Participants, as a fraction of those recruited: {{participant_summary}}
- Dates sessions ran: {{session_dates}}
- What this sample size lets you claim, and what it does not: {{sample_limits}}
- One line on anything that ran differently from the plan: {{plan_deviation_note}}

## Key Findings

<!-- WHAT  Each finding, stated as a pattern rather than a single anecdote, how many participants
           showed it as a fraction with its denominator, and the evidence, a quote or an observed
           action, a reader can check. Positive findings alongside problems, and a participant's own
           suggestion labelled as the participant's words.
     WHY   NN/g names the chain this section sits at the end of: "Data leads to findings, which build
           insights, which justify recommendations." Dovetail: "A one-page summary with linked evidence
           beats a forty-slide deck nobody opens." Dovetail, more bluntly: "A finding without evidence is
           an opinion with formatting." Sauro and Lewis prefer fractions over a bare percentage: "Unless
           this information appears elsewhere in your report, we recommend presenting fractions."
           Schade: "Don’t forget to include positive findings as well, letting the team know what’s
           already working." GOV.UK: "Whenever you can, you should fully anonymise the extracts you use
           so that the participants cannot be identified." User Interviews names the suggestion row
           directly: "Any specific recommendations brought up by users during interviews or in
           surveys." Deep dive: user-research-report_companion.md section 3 (Anatomy > Key Findings).
     ASK   What is the finding, as a pattern across sessions? How many participants showed it, as a
           fraction with the denominator stated? What evidence backs it, anonymised and within the
           consent given? Is this a problem, something that already works, or a participant's own
           suggestion? Have you included at least one thing that already works, not only what failed?
     PRIORITY  Most important finding first. State counts as fractions with the denominator next to
           every count, never as a bare percentage unless the denominator already appears beside it.
     ROW HINT  A good row names a pattern, gives a fraction with its denominator, and quotes or
           describes evidence a reader could go check. A weak row is an opinion with a number attached
           and no quote or observation behind it.
     GOOD  | Bulk-select reads as a filter toggle, so people delete duplicates one at a time | 7 of 9 |
           "I thought that button was for sorting, not for picking more than one." | Problem |
     WEAK  | Users don't like managing duplicates | Most of them | | Problem |
     TRAP  Reporting an opinion with a number attached instead of a pattern with a quote or an observed
           action a reader could go check. -->

| Finding | Participants (fraction) | Evidence | Positive, problem, or participant suggestion |
|---|---|---|---|
| {{finding}} | {{finding_count}} | {{finding_evidence}} | {{finding_type}} |

## Task Results

<!-- WHAT  For a usability test: each task's completion, errors and time against the measures the plan
           set, and the questionnaire scores the plan named. For any other method, one line saying so,
           with the table and the questionnaire line marked N/A.
     WHY   This block's content comes from usability-specific sources only; no general report list
           carries it. NIST's template, inside its own health-records customization, structures it
           under "3.9 USABILITY METRICS" and "4 RESULTS", and defines a success rate directly: "The
           total number of successes were calculated for each task and then divided by the total number
           of times that task was attempted." UserTesting instructs a report to "Include quantitative
           data where applicable (e.g., success rates, charts, QX Score visualizations)". Questionnaire
           thresholds, where NIST's template states them inside the same EHR customization, are NIST's
           own convention, not a general usability bar this library sets. Deep dive:
           user-research-report_companion.md section 3 (Anatomy > Task Results).
     ASK   Is this a usability test? If not, say so in one line and mark the table and the questionnaire
           line N/A. If so: did each participant complete each task, against the success criterion the
           plan set? How many errors, and how long did it take? What did any questionnaire score, and
           against what convention, if one applies?
     PRIORITY  List tasks in the plan's own order. A success rate is the count that actually succeeded
           divided by the count that attempted the task, never a rate scored after the fact against a
           looser bar.
     ROW HINT  A good row names the task, states completion as a fraction against the plan's success
           criterion, gives error and time figures where the plan collected them. A weak row gives a
           completion rate with no stated criterion behind it.
     GOOD  | Find and merge the duplicate pair in this album | 8 of 9 | 1 minor | avg 42s | Plan's
           success criterion: merges without opening the help menu |
     WEAK  | Duplicate task | 90% | | | |
     TRAP  Reporting a completion rate with no criterion stated, so a reader cannot tell what counted as
           success. -->

If this study is not a usability test, say so, name the method, and mark the table and the
questionnaire line below N/A: {{not_usability_test_note}}

| Task | Completion (fraction, against the plan's criterion) | Errors | Time on task | Notes |
|---|---|---|---|---|
| {{task_name}} | {{task_completion}} | {{task_errors}} | {{task_time}} | {{task_notes}} |

- Questionnaire scores the plan named, and the convention they are read against, if any: {{questionnaire_scores}}

## Recommendations

<!-- WHAT  What the team should do next, and why, with each recommendation tied to one or more
           findings above. It records no decision and names no chosen concept.
     WHY   Dovetail's list carries "recommendations". User Interviews names "Recommendations" as its
           own section, and UserTesting prioritises it: "Prioritized based on impact". Schade's own
           instruction keeps the section honest about what it is: "But present recommendations as
           recommendations." The sources pull this section toward the decision itself: Dovetail: "End
           each finding with what the team should do about it, and who decides". Usercall: "If your
           report doesn't end in a decision or a debate about a decision, you haven't written a report,
           you've written a diary." Against that pull, this family's contract states the line this
           bundle follows: "A member here may recommend, but it records no decision." Deep dive:
           user-research-report_companion.md section 3 (Anatomy > Recommendations), section 6.
     ASK   What should the team do next? Which finding or findings does this recommendation answer to?
           Why this change, rather than another? Have you stopped short of naming the decision itself,
           or the concept a team will build?
     PRIORITY  Highest-impact recommendation first. Every recommendation names the finding it answers
           to; a recommendation with no finding behind it is an opinion, not a conclusion.
     ROW HINT  A good row names a specific change, points at the finding it comes from, and says why
           that finding makes the change worth weighing. A weak row names a destination ("fix
           duplicates") with no finding and no reasoning behind it.
     GOOD  | Make bulk-select the default view once duplicates are found | Bulk-select reads as a
           filter toggle (7 of 9) | Removes the step where people have to notice a control they
           currently miss |
     WEAK  | Redesign the duplicates feature | | Seems like a good idea |
     TRAP  Naming the concept the team should build, or stating that the team has decided to build it.
           That is a later document's job; this section names what is worth weighing and why. -->

| Recommendation | Tied to finding(s) | Why |
|---|---|---|
| {{recommendation}} | {{tied_finding}} | {{recommendation_rationale}} |
