---
title: "{{program_name}} Status Report - {{reporting_period}}"
program: "{{program_name}}"
reporting_period: "{{reporting_period}}"
prepared_by: "{{report_owner}}"
audience: "{{audience}}"
cadence: "{{cadence}}"
status: "{{status}}"
doc_type: status-report
size: full
source_template: status-report
source_template_version: 0.1.0
---

<!--
FULL STATUS REPORT. The governance-grade report: everything in the lean variant, plus the specific numbers
behind the status colour (Metrics), the deliverable-and-date baseline progress is measured against
(Milestones), and the specific asks of the reader (Decisions Needed). Use it when the audience is empowered
to act on metrics and decisions directly, not just to know the headline - a steering committee, a sponsor, or
anyone who reads this instead of walking the board.

This is a STRICT SUPERSET of status-report_template-lean.md: Summary, Status, Accomplishments, Risks and
Issues, and Next Steps appear in the same relative order; full only inserts Metrics, Milestones, and
Decisions Needed in place. If you are growing from lean, add these; do not reorder.

THIS DOCUMENT OWNS NONE OF ITS OWN FACTS. A status report narrates what already-authoritative sources mean
for one audience in one period; it does not originate numbers. Every figure below must be read from
something with more authority - a KPI dashboard, a risk register, a RAID log - never estimated or recalled
fresh for this report. Say plainly where a number comes from. This no-new-facts framing is this library's own
convention, not a rule any source read states outright; treat it as the discipline this document type needs,
not as recovered practice. See status-report_companion.md section 1.

A COLOUR WITHOUT A THRESHOLD IS AN OPINION, NOT A MEASUREMENT. Even the most detailed published RAG scheme
in existence defines Red, Amber and Green and then declines to define the two colours in between, leaving
the hardest calls to judgement. Every Status entry in this template must therefore carry the rule that
produced it, not just the colour, and the Metrics section below is where that rule gets its numbers. See
status-report_companion.md sections 3 and 6.

REPORTS SKEW OPTIMISTIC. The one measured finding behind this bundle: experienced project managers write
biased reports more often than not, and the bias runs more than twice as often optimistic as pessimistic.
The Accomplishments section exists to be filled only with things that already happened, as the direct
counterweight. See status-report_companion.md section 1.

DECISIONS NEEDED IS NOT A SECOND STATUS TABLE. Keep it to rows with an actual decision attached, or a report
that surfaces every metric and asks for nothing is exactly the status-theatre failure this section exists to
prevent. See status-report_companion.md section 3 (Anatomy > Decisions Needed) and section 7.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   status-report_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid.
   Tables add PRIORITY and ROW HINT.
2. Replace each {{placeholder}} with your content. Every figure needs a named source; every Status row
   needs a threshold, not just a colour.
3. If a section does not apply this period, write "None this period" and one line of why, rather than
   deleting the section.
4. Never finished, but before you send it: self-grade against status-report_guide.md, then DELETE every HTML
   comment. They are guidance, not content.
-->

# {{program_name}} Status Report - {{reporting_period}}

## Summary

<!-- WHAT  One or two sentences carrying the headline: the overall direction this period, and the single
           thing the reader most needs to know. Written so a reader who opens only this section still
           leaves informed.
     WHY   The summary is the triage surface; most readers stop here. Attested across the corpus as "A
           summary of the project's current status", "Project Summary", and "Summary" preceded by an
           "Introductory note". Deep dive: status-report_companion.md section 3 (Anatomy > Summary).
     ASK   What is the headline for this period? Would someone who reads only this section know whether
           things are on track, and what (if anything) is needed from them?
     GOOD  "Amber this period: checkout success rate and settlement latency are both improving but still below
           their green thresholds, and the PII exposure risk was escalated to the steering group on
           2026-03-09. Two decisions below need this group's sign-off."
     WEAK  "Good progress this week." (no direction, no headline, nothing to act on)
     TRAP  Burying the one thing that matters past the first sentence. If the reader stops here, they should
           still know the headline. -->

{{summary}}

## Status

<!-- WHAT  The overall health call for the period, one row per dimension you report on, each carrying the
           threshold that produced its colour, not the colour alone.
     WHY   The fastest-read field in the whole document, and the one this document type gets wrong most
           often: a colour without a stated rule is an opinion wearing the costume of a measurement, and
           even the most careful public RAG scheme leaves its own middle colours undefined. Deep dive:
           status-report_companion.md section 3 (Anatomy > Status) and section 6 (the RAG-threshold debate).
     ASK   What is the status of each dimension you report on (overall, or split by schedule/scope/budget/a
           named metric)? What is the threshold - stated as a number or a named rule - that produced this
           colour? What changed since the last report?
     PRIORITY  One row per dimension the audience actually needs; do not invent dimensions to fill the
           table. State the threshold in the same row as the colour, not in a separate document only.
     ROW HINT  A good row names the dimension, states the colour, states the numeric or defined threshold
           that produced it, and says what changed. A weak row is a colour with nothing behind it.
     GOOD  | Overall | Amber | Green requires checkout success at or better than 99.5% AND settlement
           adoption at or above 55%; both metrics are still below their green line this period | Neither
           headline metric has crossed to green yet; no schedule slip |
     WEAK  | Overall | Amber | | Things are okay-ish |
     TRAP  Colouring against a target that is not the same number as the threshold that defines the colour.
           State which one produced the call; the Metrics table below carries both. -->

| Dimension | Status | Threshold | What changed |
|---|---|---|---|
| {{status_dimension}} | {{status_rag}} | {{status_threshold}} | {{status_change}} |

## Metrics

<!-- WHAT  The specific numbers behind the Status call above, one row per metric, each read from its named
           system of record rather than estimated or recalled for this report.
     WHY   This is where the no-new-facts rule stops being an aspiration and becomes a table: the Status
           colour above is only as honest as the numbers under it, and this section is where a reader who
           does not trust the colour can check the figure. Attested as "Key Performance Indicators (KPI's)"
           with named formulas, and "Project Metrics". Deep dive: status-report_companion.md section 3
           (Anatomy > Metrics).
     ASK   For each metric behind the Status call: what is the current value, and where did you read it (a
           KPI dashboard or another system of record, never memory)? What is the target, and is the green
           threshold the same number as the target or a different one? What does it read as against the
           threshold that produced the colour?
     PRIORITY  One row per metric that feeds the Status call above; do not introduce a number here that has
           no named source. Target and threshold are often different numbers - state both, not just one.
     ROW HINT  A good row names the metric, states current against target AND threshold separately, names
           the source, and states what it reads as. A weak row states a number with no named source.
     GOOD  | Checkout success | 98.9% | 99.6% by Q2 (target); green at 99.5% | kpi-dashboard,
           updated 2026-07-20 | Amber (below the green line, not the target) |
     WEAK  | Checkout success | Improving | | | Green |
     TRAP  Reading a colour against the target when a separate green threshold exists, or reporting a
           figure that is not traceable to a named source. Two different lines can produce two different
           honest colours for the same number. -->

| Metric | Current | Target / Threshold | Source of record | Reads as |
|---|---|---|---|---|
| {{metric_name}} | {{metric_current}} | {{metric_target_threshold}} | {{metric_source}} | {{metric_reads_as}} |

## Accomplishments

<!-- WHAT  What was actually completed this period, not what was planned, is in progress, or is hoped for.
     WHY   This is the direct counterweight to the optimism bias this document type has been measured to
           carry: a section that can only honestly be filled with things that already happened. Attested as
           "Specific accomplishments the team has achieved", "Work Completed Last Week", and "Key
           Accomplishments". Deep dive: status-report_companion.md section 3 (Anatomy > Accomplishments) and
           section 1 (the optimism-bias finding).
     ASK   What did the team actually finish this period? Would this line still be true if someone checked
           it today?
     GOOD  "Shipped the new checkout flow to the full merchant cohort; success rate is now tracked against real
           usage rather than a pilot group."
     WEAK  "Made good progress on checkout." (not a completion; could be written every period forever)
     TRAP  Reporting "in progress" or "on track" items here. If it is not finished, it belongs in Next
           Steps, not Accomplishments. -->

- {{accomplishment_1}}

## Milestones

<!-- WHAT  The deliverable-and-date structure this period's progress is measured against: the milestone,
           its target date, and its status against that date.
     WHY   Accomplishments without milestones have no baseline to be judged against. Attested as
           "Deliverables and Milestones", "Milestone Review" alongside "Project Deliverables", and "Upcoming
           tasks and milestones". Deep dive: status-report_companion.md section 3 (Anatomy > Milestones).
     ASK   What are the upcoming or recently passed milestones? What is the target date? Is each on track,
           at risk, or missed - and if not on track, why?
     PRIORITY  Order by date. State the reason for any at-risk or missed milestone in one line, not just
           the status word.
     ROW HINT  A good row names the milestone, the date, the status, and (if not on track) why. A weak row
           is a bare status with no date or reason.
     GOOD  | Platform query engine live | 2026-08-01 | At risk | Dependency confirmed by the owning team;
           see D-01 in the RAID log |
     WEAK  | Query engine | | At risk | |
     TRAP  A milestone with no date is not a milestone, it is an intention. -->

| Milestone | Target date | Status | Note |
|---|---|---|---|
| {{milestone_name}} | {{milestone_date}} | {{milestone_status}} | {{milestone_note}} |

## Risks and Issues

<!-- WHAT  What could still go wrong, and what has already gone wrong, that matters to THIS audience in
           THIS period - not the full risk register or RAID log, but what those sources mean for the reader
           right now, with a reference back to the authoritative entry.
     WHY   The sharpest-attested section in the corpus, and the one where the no-new-facts rule bites
           hardest: read the item and its status from the register by ID, do not re-score or re-describe it
           from scratch here. Deep dive: status-report_companion.md section 3 (Anatomy > Risks and Issues).
     ASK   What is the top risk or issue this reader needs to know about this period? What is its ID in the
           authoritative register or log? What changed since last period (escalated, closed, materialized)?
           Does it need anything from this reader?
     PRIORITY  Only what changed or still matters this period; this is not a re-listing of the whole
           register. Every row names the source register and its ID.
     ROW HINT  A good row states what it is, its current status, its register reference, and what changed.
           A weak row restates the entire register with no filter for relevance.
     GOOD  | R-11 (risk-register) | Card-network recertification may slip | Escalated to the steering group
           2026-03-09 | Escalated this period; awaiting sign-off, see Decisions Needed |
     WEAK  | Various risks | See register | | |
     TRAP  Duplicating the register wholesale, or reporting the same underlying fact twice under two
           different names because it also sits in another log. -->

| Ref | Description | Status | What changed |
|---|---|---|---|
| {{item_ref}} | {{item_description}} | {{item_status}} | {{item_change}} |

## Decisions Needed

<!-- WHAT  The specific asks of the reader: what they must decide, and by when. And the honest label:
           nothing in this document type's published corpus attests this title.
     WHY   It is this library's own addition, kept because a report that surfaces every metric and asks for
           nothing is exactly the status-theatre failure named elsewhere in this bundle: a document that
           satisfies the appearance of governance while producing no decision. A named practitioner source
           draws the sharpest line found between a status update (covers every metric) and a decision
           session (narrows to the evidence for one recommendation) - this section is the narrow decision
           slice, not a second status table. Deep dive: status-report_companion.md section 3 (Anatomy >
           Decisions Needed) and section 8.
     ASK   What decision does this report need from its reader? By when? What happens if it is not made?
           What is the minimum context they need to decide, not the full case?
     PRIORITY  Keep this short. Only rows with an actual decision attached belong here.
     ROW HINT  A good row names the decision, the decider, the deadline, and the one-line context needed to
           decide. A weak row states a problem with no decision attached.
     GOOD  | Approve emergency budget for a second query-engine contractor | Steering group | 2026-08-10 |
           Without it, the platform query engine milestone slips past go-live; see raid-log D-01 |
     WEAK  | Query engine is a risk | | | |
     TRAP  Turning this into a second Risks and Issues table. If there is nothing to decide, write "No
           decisions needed this period" rather than padding it with information, not asks. -->

| Decision | Decider | Needed by | Context |
|---|---|---|---|
| {{decision}} | {{decision_owner}} | {{decision_deadline}} | {{decision_context}} |

## Next Steps

<!-- WHAT  What happens next, independent of whether it depends on anything raised above.
     WHY   Closes the report on forward motion rather than a list of problems; the most consistently
           attested section in the whole corpus - "The next steps", "Work Planned for Next Week", "Upcoming
           Work" and "Action Items", "Action items". Deep dive: status-report_companion.md section 3
           (Anatomy > Next Steps).
     ASK   What is planned for the next period? Does any of it depend on a decision above, and if so, is
           that dependency named?
     GOOD  "Complete the second merchant cohort rollout, targeting 99.5 percent checkout success by end of the
           next period, pending the query-engine budget decision above."
     WEAK  "Continue work." (no specific action, nothing a reader could check next period)
     TRAP  A vague continuation with nothing to verify. Every next step should be checkable: did it happen,
           yes or no, by the next report. -->

- {{next_step_1}}
