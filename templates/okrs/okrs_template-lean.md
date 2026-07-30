---
title: "{{team_or_company_name}} OKRs, {{period}}"
owner: "{{who_is_accountable_for_this_whole_set}}"
period: "{{the_cycle_this_covers}}"
parent: "{{the_strategy_or_roadmap_this_serves}}"
audience: "{{who_reads_this}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
doc_type: okrs
size: lean
source_template: okrs
source_template_version: 0.1.0
---

<!--
HOW TO FILL THIS IN

1. Read each section's comment: what it is, why it exists, the questions to ASK, a GOOD and a WEAK example,
   and the TRAP to avoid.
2. Work top to bottom. The Objective is the easy part and the Key Results are the whole job: if you find
   yourself writing a list of things you will do, stop, because those are Initiatives and they belong in the
   full variant, not here.
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
           three to five objectives..." across a whole organisation, so one for a team is normal rather than
           thin. Deep dive: okrs_companion.md section 3 (Objective).
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

<!-- WHAT  Two to four measurable outcomes that would tell you the Objective happened. Each with a baseline,
           a target, and one named person. A table.
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
           conversation becomes an argument about what the number used to be.
     ROW HINT  GOOD  | 1 | Share of shortlists a hiring manager accepts without re-screening | 34% | 60% | Priya (PM) |
               WEAK  | 1 | Ship the new matching model | n/a | Done | Eng |
               (the first names a change in behaviour with a number you can read today; the second is an
               initiative with a checkbox, and a team rather than a person)
     GOOD  "Median days from role opening to a shortlist the manager accepts: 9 today, 5 by the end of the
           quarter."
           (a real number, a real target, and it moves only if something actually changed)
     WEAK  "Improve shortlist quality." (nothing to read, nothing to disagree with, nothing to close out)
     TRAP  Writing Key Results you already know you will hit. That is sandbagging, and it is the predictable
           consequence of scoring being attached to anything that matters to someone's career. Google names
           it as a trap in its own playbook. -->

| # | Key Result (a measurable outcome) | Baseline today | Target by end of period | Owner |
|---|---|---|---|---|
| 1 | {{key_result_1}} | {{baseline_1}} | {{target_1}} | {{owner_1}} |
| 2 | {{key_result_2}} | {{baseline_2}} | {{target_2}} | {{owner_2}} |
| 3 | {{key_result_3}} | {{baseline_3}} | {{target_3}} | {{owner_3}} |

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
