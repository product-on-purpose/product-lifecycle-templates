---
title: "{{retrospective_title}}"
doc_type: project-milestone-retrospective
size: full
project: "{{project_name}}"
author: "{{author}}"
facilitator: "{{facilitator}}"
status: draft
doc_version: "{{doc_version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: project-milestone-retrospective
source_template_version: 0.1.0
---

<!--
FULL PROJECT MILESTONE RETROSPECTIVE. Everything the lean variant carries, in the same order and under the
same names, plus exactly two additions: a Previously Identified Issues section inserted between What Did Not
and Lessons for Others, and a quantification table inside What Happened in place of the lean variant's
single quantified line. Nothing is renamed or reordered, so lean remains a strict ordered subset and a
document can grow from lean to full in place: move the lean variant's quantified line into the first row of
the table, and add the new section. See project-milestone-retrospective_companion.md section 4.

THE TWO SIZES ARE TWO GENUINE GENRES, NOT TWO LENGTHS. The filled and blank documents this bundle's research
read split cleanly. Team-authored retrospectives are short, narrative and internal, written by the people
who did the work; accountability-grade reports are long, quantified, addressed to a named recipient, and
structurally track what a previous review already said. Lean serves the first. Full serves the second.
REACH FOR FULL when money, safety or a regulator is involved; when the document will be read by someone who
can stop or fund the next thing; when there is a prior review of the same work whose findings need checking;
or when the work is being closed formally against a baseline, which is the shape both the DOE closeout
report and ITU's post implementation review template take. See
project-milestone-retrospective_companion.md section 4 (Variants and sizing) and section 9 (Adaptations).

WHAT THIS DOCUMENT IS. It is the document a team writes when a bounded piece of work is over, for readers
who may not have been there. It is TERMINAL, and that is the whole design. Kerth's founding handbook states
the rationale directly: "the collective team wisdom acquired during the previous project is likely to be
lost as individuals are scattered across the organization to support new undertakings. If, at the end of a
project, the collective wisdom is discussed and documented, it becomes knowledge that survives the breakup
of the team." He adds the second reason nobody in the room can supply alone: "no one person knows all the
stories, and no one person knows how the pieces fit together to tell the tale of the entire project." See
project-milestone-retrospective_companion.md section 1 (Orientation).

THIS IS NOT A SPRINT RETROSPECTIVE, AND IT IS NOT AN INCIDENT POSTMORTEM. Those are the two siblings in this
family, and if a reader cannot tell the three apart, this document has failed.
  - A sprint retrospective looks back on a PERIOD, on a CADENCE, at how a team worked. Its canonical output
    is not a document at all: the Scrum Guide says the improvements "may even be added to the Sprint Backlog
    for the next Sprint." A retro tool draws the same line from the other side: "sprint retrospectives take
    place multiple times at a regular cadence throughout the course of a project. But the project post-mortem
    only takes place once." If the trigger is the calendar and the audience is a team that keeps working
    together, use sprint-retrospective-notes instead.
  - An incident postmortem is EVENT-TRIGGERED learning about one specific failure. As one vendor puts it,
    "Post-mortems attempt to understand what went wrong," while "Retrospectives, on the other hand, primarily
    engage and serve the team doing the work." If a specific thing failed and the question is why, use
    incident-postmortem, even if the project also just ended.
  See project-milestone-retrospective_companion.md section 8 (Relationships to other artifacts).

WHERE THE WRITTEN DOCUMENT IS ADMITTED, AND ONE CITATION TRAP. Two independent named lineages publish this
as a document. The Center for Army Lessons Learned, the Army's own lessons-learned proponent, names it
separately from the meeting: "After action report: A written report that is typically submitted after a
training, combat operation, or other mission that normally documents a unit's actions for historical
purposes but also provides key observations and LL." PMI's PMBOK Guide Sixth Edition lists "Lessons learned
register" as the first named output of process 4.4, Manage Project Knowledge. THE TRAP: the Army's older and
better known TC 25-20 (1993) defines the AAR as a conversation, "An AAR is a dynamic, candid, professional
discussion of training which focuses on unit performance against the Army standard for the tasks being
trained," and insists "An AAR is not a critique." Anyone citing TC 25-20 for a written after action report
is citing the wrong document. The PMBOK Guide's Eighth Edition restructured away from named artifacts, so
the register is cited here from the Sixth Edition and labelled as such. See
project-milestone-retrospective_companion.md sections 2 and 6.

THE CRITICISM OF THIS DOCUMENT TYPE IS REAL, AND NARROWER THAN IT SOUNDS. Every critic in this bundle's
research attacks one specific pattern. A PMI congress paper describes lessons that "get lost in some sort of
'lessons learned database' - as in, a 'black hole' (Dalton, 2013) - that nobody ever looks at"; a
knowledge-management authority reports that "all those repositories of lessons learned that we built in the
early days of KM just didn't work very well and lessons learned took on a bad name within organizations"; a
consultant titles his piece against retrospectives outright. AND EVERY ONE OF THEM STILL RECOMMENDS WRITING
SOMETHING DOWN. That same consultant argues these "should be kept in a repository so they can be used to
look at trends and provide evidence of improvement over time." The discriminator is whether retrieval is
wired into somebody's workflow, so the honest framing is anti-deposit-and-forget, not anti-documentation.
It is also why Scope and Period asks who reads this and what they decide with it before anything else. The
opposite failure is just as real: a 2026 study of engineers at a national space research centre found
"knowledge loss due to team turnover & fragmented documentation," with practitioners reporting of failure
knowledge that "I don't think they are documented, pretty much at all." See
project-milestone-retrospective_companion.md section 6 (Debates and contested boundaries).

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   project-milestone-retrospective_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and
   the TRAP to avoid. For tables, PRIORITY explains the ordering rule and ROW HINT says what a good row
   contains.
2. Replace each {{placeholder}} with your content. Fill Scope and Period first, and decide the circulation
   of this document BEFORE the discussion, not after: one peer-reviewed study of retrospectives found that
   "Having minutes public could also lead to critique being toned down or removed completely," which is a
   cost you pay before a word is written.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it silently. That
   applies squarely to Previously Identified Issues: a genuinely first-of-its-kind project has no prior
   review to check against, and "N/A, no prior review of this work exists" is a better answer than an
   invented row.
4. Before you share it: self-grade against project-milestone-retrospective_guide.md, then DELETE every HTML
   comment. They are guidance, not content.
-->

# {{retrospective_title}}

## Scope and Period

<!-- WHAT  Two things in one section: what is being looked back on and where its boundaries fall, and who
           reads this document and what they decide with it.
     WHY   The first half is what stops this document, a sprint retrospective and an incident postmortem
           blurring into each other, and it has direct template attestation: ITU gives Scope of Review its
           own numbered section, where "The paragraph provides a clear explanation of the scope of the
           review," and the VA's after action review template records whether the review ran during the
           project or after project completion. The second half is this bundle's strongest evidence-driven
           departure from the obvious shape. Naming the audience changed the CONTENT of every real filled
           document this research read, not just its cover page: the IRS relabelled its own findings,
           "We have labeled these lessons opportunities, because they will help both improve the tax filing
           ecosystem and inform the decision about Direct File's future." GAO-19-25 is literally an
           addressed letter. A naive what-went-well/what-did-not/actions shape has no field for any of this.
           Deep dive: project-milestone-retrospective_companion.md section 3 (Anatomy > Scope and Period).
     ASK   What exactly is being reviewed, as dates and deliverables rather than as a mood, and what is
           deliberately outside it? Who opens this document, and what are they about to decide with it?
           Who will be able to read it, and did everyone know that before they spoke? Who contributed, and
           who had already moved on and could not be reached?
     GOOD  "Work reviewed: the Larkspur payroll migration, contract signature to the first unassisted pay run
           (2026-01-12 to 2026-09-04), across all nine Northwind depots. Deliberately outside this review:
           the benefits module, which has not started. Who reads this: Marta Ilves and the programme board.
           What they decide with it: whether the benefits module reuses this vendor and the depot-by-depot
           rollout, at the November board. Circulation: the board and the delivery team, agreed before the
           session."
     WEAK  "A retrospective on the payroll project. All feedback welcome." (no boundary a later reader can
           check, no named reader, no decision this feeds, and no circulation agreed, so nobody in the room
           knew how freely they could speak)
     TRAP  Treating the audience line as a cover-page courtesy. If you cannot name a reader or a next use,
           that is a finding rather than a formatting problem: it is the exact condition every critic of
           this document type describes, a document written into a repository nobody has a reason to open.
           Decide whether to find the reader or to stop writing. -->

**Work reviewed:** {{work_reviewed}}
**Period:** {{period_start}} to {{period_end}}
**Deliberately outside this review:** {{out_of_scope}}
**Who reads this:** {{primary_audience}}
**What they decide with it:** {{next_use}}
**Circulation, agreed before the discussion:** {{circulation}}
**Who contributed, and who could not be reached:** {{contributors}}

## What Happened

<!-- WHAT  The factual record, kept separate from interpretation, plus the quantification table: the two or
           three measures this work was actually judged on, planned against actual.
     WHY   Published templates separate fact from judgement structurally: the DOE closeout report holds
           baseline and closeout status in their own numbered sections and puts narrative lessons in
           another, and ITU keeps Results Achievement, Financial Status, Findings and Lessons Learned as
           four separate sections. The Kubernetes Storage SIG retrospective opens by saying the record IS
           the job: "This document is intended to chronicle the decisions made by the Storage SIG near the
           end of the Kubernetes 1.3 release with the storage stack that were not well understood by the
           wider community." The table is the full variant's addition because the accountability genre
           leads with numbers and states plainly what they are for: DOE's closeout template says "The
           purpose for this request is to allow other projects to use historical cost data of a completed
           project." Note the limit this research found. Three government sources lead with money, but the
           Kubernetes retrospective quantifies engineering quantities and not money, and a schedule slip instead, so the rule is
           quantify something MATERIAL, not quantify in currency; demanding dollars would overfit this
           document to public-money accountability. Deep dive:
           project-milestone-retrospective_companion.md section 3 (Anatomy > What Happened).
     ASK   What would a reader be able to verify from a system of record, as distinct from what the team
           believes about it? What two or three measures was this work actually judged on? For each, what
           was the baseline and what actually happened? If the only number available is elapsed time, can
           you say so rather than manufacturing a metric to fill a row?
     PRIORITY  Put the measure the work was commissioned against first, whether that is cost, date, or a
           quality threshold. Measures the team found interesting go below the measures the sponsor will
           check.
     ROW HINT  A good row names one measure, its planned value, its actual value, and the system a reader
           could open to check it. A weak row has a number with no baseline, or a baseline nobody can
           locate.
     GOOD  | Parallel-run discrepancy rate | Under 10 per cycle before cutover | 41 in cycle one, 4 in
           cycle two | Payroll parallel-run log, cycles 1 and 2 |
     WEAK  | Quality | Good | Mostly fine | (no baseline, no actual, and nothing a reader can open)
     TRAP  Letting judgement leak into the record. *A key engineer left one week before code freeze* is a
           fact; *we were under-resourced* is an interpretation, and it belongs in What Did Not. The
           Kubernetes retrospective is a good model because it keeps the two in separate sentences. -->

{{what_happened}}

| Measure | Planned | Actual | Where a reader can check it |
|---|---|---|---|
| {{measure_name}} | {{measure_planned}} | {{measure_actual}} | {{measure_source}} |

## What Worked

<!-- WHAT  What actually went well, why it went well, and how somebody else would do it on purpose.
     WHY   This is the half of the retrospective shape every genre in this research carries. The VA's after
           action review template pairs a what-went-well-and-why table with a second column asking how to
           ensure that success in future, and the HSEEP after action report opens its executive summary with
           major strengths. The third column exists because this document is terminal: a strength with no
           mechanism attached is a compliment, and a compliment does not transfer to a reader who was not
           there. Deep dive: project-milestone-retrospective_companion.md section 3 (Anatomy > What Worked).
     ASK   Is each row a specific practice rather than a mood? Does it say WHY the practice worked, not only
           that something went well? Could a stranger copy the third column into their own project without
           asking anyone here a follow-up question?
     PRIORITY  Put the practices most likely to transfer to other work first. Rows that only made sense for
           this team, this quarter, belong lower or not at all.
     ROW HINT  A good row names one practice, the mechanism that made it work, and a repeatable instruction.
           A weak row is a compliment with no mechanism behind it.
     GOOD  | Two full parallel pay cycles before cutover | The second cycle caught four discrepancies the
           first had masked, because cycle one's fixes changed the data cycle two ran on | Budget two
           parallel cycles rather than one, and treat the second as a fresh test rather than a re-run |
     WEAK  | Great team | Everyone worked really hard | Keep it up |
     TRAP  Writing the mood rather than the practice. "Morale stayed high" is not something a reader who was
           not there can do anything with; "a daily one-line status went to all nine depot managers" is. -->

| What worked | Why it worked | How someone else repeats it |
|---|---|---|
| {{worked_item}} | {{worked_reason}} | {{worked_repeat}} |

## What Did Not

<!-- WHAT  What went wrong or fell short, with enough analysis that a reader can tell a cause from a
           symptom.
     WHY   The same cross-genre attestation as What Worked: the VA template pairs a what-can-be-improved
           table with a recommendations column, and HSEEP asks each observation to be labelled explicitly,
           "Begin this section with a heading indicating whether the observation is a 'Strength' or an 'Area
           for Improvement.'" The Kubernetes retrospective shows what a good entry reads like, separating
           the fact, "Near the end of 1.3 development, on May 13, 2016, approximately one week prior to code
           freeze, a key engineer for this effort left the project," from the judgement, "In the decision to
           move forward with coding beyond code freeze, not enough thought was invested in what could go
           wrong or how to mitigate that." Deep dive:
           project-milestone-retrospective_companion.md section 3 (Anatomy > What Did Not).
     ASK   For each row, is the middle column a cause or just a restatement of the symptom? Would the third
           column actually have prevented this, or does it only describe noticing it sooner? Is anything
           here softened because of who will read the document?
     PRIORITY  Order by what cost the most, in money, time, or trust, rather than by what the room felt most
           strongly about.
     ROW HINT  A good row names one shortfall, one cause a reader could act on, and one preventive change.
           A weak row names a category, a feeling, or a person.
     GOOD  | Depot data cleansing started after the build, not before | Nobody owned data readiness until
           the first parallel cycle exposed it, because the contract put cleansing in the depots' scope and
           no depot had capacity for it | Name a single data-readiness owner at contract signature and gate
           the build start on a sampled record quality check |
     WEAK  | Data was a mess | The depots let us down | Do better next time |
     TRAP  Softening this section because of who will read it. A peer-reviewed study of retrospectives found
           that "Having minutes public could also lead to critique being toned down or removed completely."
           That damage happens before the document exists, which is why circulation is a Scope and Period
           decision rather than a publishing one. If the sharpest material genuinely cannot be circulated,
           say in Scope and Period that a narrower account exists and who holds it, rather than letting this
           version imply it is the whole story. -->

| What did not work | Why it happened | What would have prevented it |
|---|---|---|
| {{shortfall_item}} | {{shortfall_cause}} | {{shortfall_prevention}} |

## Previously Identified Issues

<!-- WHAT  The things this retrospective is finding AGAIN: problems already named in an earlier review, and
           what actually happened to the corrective actions that were supposed to close them.
     WHY   This is the defining section of the accountability-grade genre, and it is full-only for an honest
           reason. GAO-19-25 names the pattern directly, reporting that "NNSA has had a long history of
           identifying corrective actions and declaring them successfully resolved, only to identify
           additional" problems of the same kind. The National Audit Office's report on the Emergency
           Services Network is built on it mechanically, marking the repeat in its own words: "How the ESN
           service will be governed and managed when it is a live service is still not clear, although we
           identified this risk in our report in 2016." The IRS does the same inside a self-authored
           document: "Each of the next three sections reassesses an operational challenge identified in the
           Report to Congress." THE LIMIT, STATED PLAINLY: this research found repeat-lesson tracking
           specifically in the external-audit genre and NOT in the team-authored retrospectives it read,
           which is why this section invites the content rather than demanding it. Deep dive:
           project-milestone-retrospective_companion.md section 3 (Anatomy > Previously Identified Issues).
     ASK   Is there a prior retrospective, readiness review, audit or assurance report covering this work?
           For each thing it raised, what was agreed, and what actually happened? Which of these is being
           found again right now, and does What Did Not repeat it without saying it is a repeat? If nothing
           prior exists, have you written "N/A" and one line rather than inventing a row?
     PRIORITY  Put the issues that were declared closed and were not first. An issue everyone knew was still
           open is a smaller finding than one somebody signed off.
     ROW HINT  A good row quotes the issue as the earlier document actually worded it, says where and when
           it was raised so a reader can go and look, and separates what was agreed from what happened. A
           weak row paraphrases the old issue into the new one and hides the fact that it is the same
           problem.
     GOOD  | "Depot record quality is not baselined and is a delivery risk" | Phase 1 readiness review,
           2026-02-20, item 4 | Each depot to sample 200 records before build start | Three of nine depots
           sampled; the gate was waived in March to hold the go-live date | Recurred, and now reported again
           in What Did Not |
     WEAK  | Data quality | Earlier | It was looked at | Fixed | (nothing checkable, and "fixed" is the
           claim the whole section exists to test)
     TRAP  Quietly dropping this section because filling it is uncomfortable. It is the easiest of the seven
           to lose under pressure, and losing it is precisely the failure GAO describes. If your
           organisation decides to remove it, say who removed it and why in Scope and Period rather than
           letting it vanish. -->

| Issue, as it was written then | Where and when it was raised | Action that was agreed | What actually happened | Status now |
|---|---|---|---|---|
| {{prior_issue}} | {{prior_issue_raised}} | {{prior_issue_action}} | {{prior_issue_outcome}} | {{prior_issue_status}} |

## Lessons for Others

<!-- WHAT  The terminal-handover section. Its entire reason for existing is a reader who was not there.
     WHY   This is where the two admission lineages converge. CALL states that one of the two key purposes
           of a written after action report is to "provide best practices and lessons in the
           observation-discussion-recommendation format that can be used to inform the Army's LL program."
           The VA template adds an explicit sharing step, "Share the AAR report with your project sponsor or
           other appropriate leader in your facility, VISN or national VHA offices," and says where the
           value lands: "The greatest benefit of an AAR comes from applying the lessons learned to future
           work and teams." ITU asks the transferability question on the page: "Could these lessons be
           utilized as best practices in other Regions?" Deep dive:
           project-milestone-retrospective_companion.md section 3 (Anatomy > Lessons for Others).
     ASK   Does each lesson parse for somebody with no context on this project? Who specifically is it for,
           by role or by team, rather than "the organisation"? Where a lesson is one your organisation
           already had, is it recorded as a repeat in Previously Identified Issues rather than presented
           here as new?
     PRIORITY  Lead with the lessons that transfer furthest from this project. A lesson only the next team
           on this same system can use goes lower.
     ROW HINT  A good row is a sentence a stranger could act on, a named audience, and a concrete change.
           A weak row only parses to people who were in the room, or quietly re-presents a known problem as
           a discovery; that one belongs in Previously Identified Issues.
     GOOD  | On a phased rollout, source-data quality sets the schedule rather than being a prerequisite to
           it | Whoever runs the benefits module, and any programme rolling out site by site | Gate each
           phase's build start on a sampled record quality check owned by one named person |
     WEAK  | Communication could have been better | Everyone | Communicate more |
     TRAP  Letting this section crowd out the part of the exercise that helps the people who lived it. A
           knowledge-management authority is blunt that "The greatest value of lessons learned is for those
           who took the action," and transfer to strangers is the harder and weaker claim. Write this
           section anyway, because it is what makes the document terminal rather than ceremonial, but do not
           let a lesson get vaguer as it gets more general. -->

| Lesson | Who it is for | What to do differently |
|---|---|---|
| {{lesson}} | {{lesson_audience}} | {{lesson_action}} |

## Actions and Owners

<!-- WHAT  What changes, who owns each change, by when, and where it is tracked. With owners and dates, or
           it is a feelings log.
     WHY   This is the process-docs family's shared obligation, and it is also the section where published
           practice is weakest, which this template says out loud. Of the templates this research read in
           full, exactly one gives an action both an owner and dates: HSEEP's Improvement Plan Matrix, whose
           columns run "Capability | Observation Title | Recommendation | Corrective Action Description |
           Capability Element | Primary Responsible Agency | Agency POC | Start Date | Completion Date." The
           VA template carries no owner or due-date field, ITU's Recommendations section offers only that
           "Priorities will be identified for the implementation of recommendations," and a reference
           describing PRINCE2's Lessons Log states the gap directly: "The document does not specify an
           'owner' field." So this section is the library's own insistence, backed by one published
           template and by the family contract, not a majority convention. HSEEP also puts its matrix in an
           APPENDIX, separate from the narrative, which is a real design signal: the narrative is for
           readers, the tracker is for tracking. Deep dive:
           project-milestone-retrospective_companion.md section 3 (Anatomy > Actions and Owners).
     ASK   Does every row name one person rather than a team? Does every row have a date? Does the work
           already exist in the tracker your organisation actually uses, and is its identifier in the row?
           If this project is closing, who inherits an action whose owner is about to move on?
     PRIORITY  List the actions that must survive the team's dispersal first. An action nobody will be
           around to do needs a new owner, not a lower place in the list.
     ROW HINT  A good row names one checkable change, one named person, one date, and a tracker identifier
           that lets the tracker own the status. A weak row is an intention with no owner and no
           destination.
     GOOD  | Name a data-readiness owner in the benefits module statement of work before build start | Tobi
           Adeyemi | 2026-10-17 | NWL-3312 |
     WEAK  | Improve data quality | The programme team | Soon | (no person, no date and no destination, so
           nothing here outlives the meeting that produced it)
     TRAP  Letting this document become a second, stale tracker. Put the identifier in the row and let the
           system own the status. This library's family contract also allows actions to land in the
           product-backlog, the risk-register or the raid-log; of those, only the ordinary ticket tracker
           reflects published practice, and the other two are this library's own convention rather than
           received retrospective practice. -->

| Action | Owner | Due | Tracked in |
|---|---|---|---|
| {{action}} | {{action_owner}} | {{action_due}} | {{action_tracked_in}} |
