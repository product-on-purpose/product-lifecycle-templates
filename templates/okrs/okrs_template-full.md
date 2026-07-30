---
title: "{{team_or_company_name}} OKRs, {{period}}"
owner: "{{who_is_accountable_for_this_whole_set}}"
period: "{{the_cycle_this_covers}}"
parent: "{{the_strategy_or_roadmap_this_serves}}"
audience: "{{who_reads_this}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
doc_type: okrs
size: full
source_template: okrs
source_template_version: 0.1.0
---

<!--
HOW TO FILL THIS IN

1. Read each section's comment: what it is, why it exists, the questions to ASK, a GOOD and a WEAK example,
   and the TRAP to avoid.
2. Work top to bottom. The Objective is the easy part and the Key Results are the whole job. Initiatives come
   AFTER the Key Results, never before: if you write the work first and then invent measures for it, you have
   produced a project plan with a scoring rubric attached.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you share it: self-grade against okrs_guide.md, then DELETE every comment block. They are
   guidance, not content.

ONE OBJECTIVE PER DOCUMENT. This template holds a single Objective at both sizes. If a team genuinely has
two, write two documents; a second Objective sharing one Key Result table is how a set stops being readable.

THE ONE TEST THAT OUTRANKS EVERY OTHER. Read each Key Result and ask: could we do all of this and still
have failed? If yes, you have written activities. Google's own check is a word list: if a Key Result
contains "consult," "help," "analyze," or "participate," it describes an activity rather than an outcome.
Rewrite it as the change you would see in the world.

WHAT THE EVIDENCE ACTUALLY SAYS, SO YOU ARE NOT MISLED. Goal-setting science is real and well replicated:
specific difficult goals outperform "do your best." But NO study measures whether the OKR format itself,
the quarterly cycle, the 0.0 to 1.0 scoring, or public visibility improves product or business outcomes.
The transfer from one to the other is assumed by vendor content and demonstrated by nobody. Use this
document because it makes a team say out loud what would count as success, not because it is proven.
See okrs_companion.md section 1.

A NOTE ON WHOSE METHOD THIS IS. Unlike a vision, a strategy or a roadmap, this artifact IS a method. Filling
it in adopts commitments that are contested rather than settled: the cadence is convention, the scoring
scale is convention, and the visibility default is a choice. okrs_companion.md section 6 argues each one.

THREE MEASUREMENT DEVICES, THREE DIFFERENT AUTHORS, AND THEY ARE NOT THE SAME THING. Vendor writing merges
them constantly, so this template keeps them in separate sections. Confidence (1 to 10) is a weekly
FORECAST and is Christina Wodtke's device. Scoring (0.0 to 1.0, red/yellow/green) is an AFTER-THE-FACT grade
and is Google's. Committed versus aspirational names WHICH TARGET you were aiming at, and is also Google's,
reported by John Doerr rather than invented by him. See okrs_companion.md section 3.
-->

# {{team_or_company_name}} OKRs, {{period}}

## The Period and What This Serves

<!-- WHAT  One short paragraph: which cycle this covers, and which parent document it serves. Name the
           parent by title and link it.
     WHY   An OKR set with no parent is a wish list with arithmetic. The point of naming the parent is that
           it makes the next question answerable: if this Objective is met, does the strategy move? OKRs are
           "a complement to strategy, not a substitute for strategy," and a set of objectives with no
           where-to-play choice behind it is not one. Deep dive: okrs_companion.md section 8.
     ASK   Which document decided this was worth doing? If we hit every Key Result, what does the parent get?
           Is anyone else's OKR set counting on ours?
     GOOD  "Covers FY27 Q1 (January to March). Serves the hiring-platform strategy's second guiding policy,
           that a hiring manager should trust the shortlist without re-screening it themselves."
           (a period, a named parent, and the specific part of it this serves)
     WEAK  "Q1 OKRs for the platform team." (a date and a team; nothing above it, so nothing can be traded
           off against anything)
     TRAP  Naming a parent nobody has read. If the strategy is stale or contested, this section inherits the
           problem rather than fixing it, and the OKR set will be argued about as though it were the
           strategy. -->

{{the_period_and_what_this_serves}}

## Objective

<!-- WHAT  One qualitative sentence: what you are trying to achieve this period. Not a number. One Objective
           per document, at both sizes; if you genuinely have two, write two documents.
     WHY   The Objective is the part people repeat from memory a month later, which is its entire job. It
           carries the meaning; the Key Results carry the measurement. Published guidance is to "Pick just
           three to five objectives..." across a whole organisation, so one to three for a team is normal
           rather than thin. Deep dive: okrs_companion.md section 3 (Objective).
     ASK   Could someone on the team say this back without reading it? Does it describe a change in the world
           rather than a change in our backlog? Would we be pleased if it happened by a route we have not
           thought of?
     GOOD  "Hiring managers trust the shortlist enough to stop re-screening it."
           (qualitative, memorable, and it names whose behaviour changes)
     WEAK  "Improve the candidate matching algorithm by 15 percent." (a Key Result wearing an Objective's
           clothes; it names a mechanism and a number, so it forecloses every other route)
     TRAP  Writing an Objective that is really a project. If the Objective names the thing you are building
           rather than the change you expect, the Key Results underneath it will only ever measure whether
           you built it. -->

{{objective}}

## Key Results

<!-- WHAT  Two to four measurable outcomes per Objective that would tell you it happened. Each with a
           baseline, a target, one named person, and whether it is committed or aspirational. A table.
     WHY   This is where the document lives or dies, and the commonest way this section goes wrong is a Key
           Result that describes work rather than a result. Google's own instruction is that Key Results "must describe
           outcomes, not activities," with a rewrite example, "publish average and tail latency measurements
           from six Colossus cells by March 7," rather than "assess Colossus latency." The rule is dominant
           but not unanimous: milestone Key Results are defended for work with genuine phases, such as a
           release, and one named coach argues that work whose outcome cannot yet be measured, like
           compliance, belongs on due dates instead of in an OKR. Deep dive: okrs_companion.md section 3
           (Key Results).
     ASK   Could we hit all of these and still have failed the Objective? What is the number today, and do we
           actually have a way to read it? Who reads it, and how often? Is any of these really a task?
     PRIORITY  A baseline is not optional. Without one, the target is unfalsifiable and the close-out
           conversation becomes an argument about what the number used to be. Mark committed against
           aspirational HERE, before the cycle starts, not afterwards when the score is known.
     ROW HINT  GOOD  | 1 | Share of shortlists a hiring manager accepts without re-screening | 34% | 60% | Priya (PM) | committed |
               WEAK  | 1 | Ship the new matching model | n/a | Done | Eng | committed |
               (the first names a change in behaviour with a number you can read today; the second is an
               initiative with a checkbox, and a team rather than a person)
     GOOD  "Median days from role opening to a shortlist the manager accepts: 9 today, 5 by the end of the
           quarter."
           (a real number, a real target, and it moves only if something actually changed)
     WEAK  "Improve shortlist quality." (nothing to read, nothing to disagree with, nothing to close out)
     TRAP  Writing Key Results you already know you will hit. That is sandbagging, and it is the predictable
           consequence of scoring being attached to anything that matters to someone's career. Google names
           it as a trap in its own playbook. -->

| # | Key Result (a measurable outcome) | Baseline today | Target by end of period | Owner | Committed or aspirational |
|---|---|---|---|---|---|
| 1 | {{key_result_1}} | {{baseline_1}} | {{target_1}} | {{owner_1}} | {{commitment_1}} |
| 2 | {{key_result_2}} | {{baseline_2}} | {{target_2}} | {{owner_2}} | {{commitment_2}} |
| 3 | {{key_result_3}} | {{baseline_3}} | {{target_3}} | {{owner_3}} | {{commitment_3}} |

## What This Set Is Not Committing To

<!-- WHAT  Two to four things that were asked for, considered, and deliberately left out of this cycle, each
           with one line on why. Name real requests.
     WHY   This is the section that makes the Objective usable, and the one most often left out. An OKR set
           without exclusions cannot be used to refuse anything, which means it settles no arguments and
           changes nobody's week. It is also the honest place to put the work that is genuinely happening
           but is not what this cycle is about. Deep dive: okrs_companion.md section 3 (What This Set Is Not
           Committing To) and section 7.
     ASK   What has been asked for repeatedly that we are not doing this cycle? Who will be disappointed, and
           have they been told by a person rather than by this document? Is anything here actually a refusal
           we have not made yet?
     GOOD  "Agency-recruiter access. Asked for by two of our largest accounts. Not this cycle, because it
           competes for the same review capacity the shortlist work needs. Both accounts have been told by
           their account manager, and it is the first candidate for next cycle."
           (a real request, a reason, who was told, and what would change)
     WEAK  "Anything not aligned to the objective." (refuses nothing in particular, so it protects nothing)
     TRAP  Listing only things nobody wanted. If every exclusion is uncontroversial, the hard refusals are
           still hiding, and they will arrive mid-cycle as an interruption nobody agreed to. -->

{{what_this_set_is_not_committing_to}}

## Initiatives

<!-- WHAT  The work you currently believe will move the Key Results, with the Key Result each one serves. A
           table. Three to six.
     WHY   This section is a CONVENTION, not part of the original method, and this template says so rather
           than pretending otherwise: the three-layer Objective, Key Result, Initiative structure is asserted
           by OKR tooling vendors, one of which attributes it to John Doerr's book without citing a page, and
           Google's own published guide never names an initiatives layer at all. It earns its place for one
           reason only: it makes the link from work to outcome visible, so a Key Result that no work serves
           becomes obvious in the same glance. Deep dive: okrs_companion.md section 3 (Initiatives).
     ASK   Which Key Result does each of these move, and by roughly how much? Is any Key Result served by
           nothing? Is anything here happening regardless of this OKR set, and if so why is it listed?
     PRIORITY  Every initiative names exactly one Key Result. An initiative that serves "all of them" is
           either the whole strategy or nothing, and it is usually nothing.
     ROW HINT  GOOD  | Rebuild the screening rubric with three hiring managers | KR1 | Priya | in progress |
               WEAK  | Improve the platform | KR1, KR2, KR3 | Team | ongoing |
               (the first is a specific piece of work against one measure; the second cannot be finished,
               cannot be owned, and cannot fail)
     GOOD  "Rebuild the screening rubric with three hiring managers, serving KR1. If it works, manager
           acceptance moves; if it does not, we learn that the rubric was not the constraint."
           (names the work, the measure, and what a failure would teach)
     WEAK  "Continue platform improvements." (not an initiative, a description of having a job)
     TRAP  Writing this section first. If the initiatives existed before the Key Results, the Key Results
           were reverse-engineered to fit the work, and the whole document is a project plan in costume. -->

| Initiative | Serves | Owner | Status |
|---|---|---|---|
| {{initiative_1}} | {{serves_1}} | {{initiative_owner_1}} | {{initiative_status_1}} |
| {{initiative_2}} | {{serves_2}} | {{initiative_owner_2}} | {{initiative_status_2}} |
| {{initiative_3}} | {{serves_3}} | {{initiative_owner_3}} | {{initiative_status_3}} |

## Confidence and Check-in

<!-- WHAT  A forward-looking confidence level per Key Result, and the rhythm at which you will revisit it.
           Three or four lines, or a short table.
     WHY   Confidence is a FORECAST, distinct from the score you will give at the end, and it is Christina
           Wodtke's named device rather than Google's or Doerr's: "set a confidence level of five of ten on
           the OKR. A confidence level of one means 'never gonna happen my friend.' A confidence level of ten
           is also known as sandbagging." She recommends adjusting it "every single week." Its value is that
           a confidence that never moves is not a forecast, it is a formality. Deep dive:
           okrs_companion.md section 3 (Confidence and check-in).
     ASK   What would have to be true for this to reach 8 out of 10? Which one are we least sure of, and does
           anyone outside the team know that? When did each of these last change, and if never, why are we
           recording it?
     GOOD  "KR1 at 6 of 10 and falling: manager acceptance has not moved in three weeks and we do not yet
           know whether the rubric is the constraint. KR2 at 8. Reviewed every Monday in the team meeting;
           the number moves in the meeting or it does not get recorded."
           (specific, decaying, and it says where the update actually happens)
     WEAK  "We are on track." (a status, not a forecast; it cannot be wrong, so it cannot be useful)
     TRAP  Recording confidence and never moving it. A column of 7s that has not changed since week one is
           the same as no column at all, and it is worse, because it looks like a control. -->

{{confidence_and_check_in}}

## Scoring and Close-out

<!-- WHAT  How this set will be scored at the end, and what happens to the result. Three or four lines. Fill
           the intent at the start of the cycle and the outcome at the end.
     WHY   Scoring is an after-the-fact grade and is Google's device: "0.0-0.3 is red, 0.4-0.6 is yellow,
           0.7-1.0 is green," with an expected 1.0 on a committed OKR and an expected average of 0.7 on an
           aspirational one. NONE of those numbers is measured; they are stated as internal convention, so
           adopt them deliberately rather than inheriting them. The decision that actually matters here is
           whether scores touch anyone's pay: the practitioner position is close to one-sided against it,
           with sales quotas as the named exception, because scoring that affects a career reliably produces
           targets people already know they will hit. Deep dive: okrs_companion.md section 6.
     ASK   Who scores this, and in front of whom? Does the score touch anyone's review or bonus, and have we
           said so out loud? What happens to a Key Result that lands at 0.3, and who decides?
     GOOD  "Scored at the end of March by the owner of each Key Result, in the team review, on 0.0 to 1.0.
           Scores are not used in performance reviews and the team has been told that in writing. A red Key
           Result gets a written note on what we learned, not a remediation plan."
           (says who, where, on what scale, and what the score does and does not do)
     WEAK  "We will grade at the end of the quarter." (no scale, no owner, no consequence, and no statement
           on the one thing everyone actually wants to know)
     TRAP  Leaving the compensation question unanswered. Silence is read as yes, and a team that suspects the
           score affects their review will sandbag the next set before you get to ask them why. -->

{{scoring_and_close_out}}
