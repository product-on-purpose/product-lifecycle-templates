---
title: "{{program_name}} Status Report - {{reporting_period}}"
program: "{{program_name}}"
reporting_period: "{{reporting_period}}"
prepared_by: "{{report_owner}}"
audience: "{{audience}}"
cadence: "{{cadence}}"
status: "{{status}}"
doc_type: status-report
size: lean
source_template: status-report
source_template_version: 0.1.0
---

<!--
LEAN STATUS REPORT. The smallest report that still says where things stand, what happened, what is at risk,
and what comes next: Summary, Status, Accomplishments, Risks and Issues, Next Steps. Use it for a routine
period read by an audience that only needs the headline and does not act on individual metrics or decisions
directly. To grow it into the governance-grade full variant (see status-report_template-full.md), ADD
sections; never rename or reorder the ones below, because the full variant is a strict superset of this one.

THIS DOCUMENT OWNS NONE OF ITS OWN FACTS. A status report narrates what already-authoritative sources mean
for one audience in one period; it does not originate numbers. Every figure below must be read from
something with more authority - a KPI dashboard, a risk register, a RAID log - never estimated or recalled
fresh for this report. Say plainly where a number comes from. This no-new-facts framing is this library's own
convention, not a rule any source read states outright; treat it as the discipline this document type needs,
not as recovered practice. See status-report_companion.md section 1.

A COLOUR WITHOUT A THRESHOLD IS AN OPINION, NOT A MEASUREMENT. Even the most detailed published RAG scheme
in existence defines Red, Amber and Green and then declines to define the two colours in between, leaving
the hardest calls to judgement. Every Status entry in this template must therefore carry the rule that
produced it, not just the colour. See status-report_companion.md sections 3 and 6.

REPORTS SKEW OPTIMISTIC. The one measured finding behind this bundle: experienced project managers write
biased reports more often than not, and the bias runs more than twice as often optimistic as pessimistic.
The Accomplishments section exists to be filled only with things that already happened, as the direct
counterweight. See status-report_companion.md section 1.

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
           2026-03-09. No action needed from this audience beyond staying aware."
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
           State which one produced the call. -->

| Dimension | Status | Threshold | What changed |
|---|---|---|---|
| {{status_dimension}} | {{status_rag}} | {{status_threshold}} | {{status_change}} |

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
           2026-03-09 | Escalated this period; awaiting sign-off |
     WEAK  | Various risks | See register | | |
     TRAP  Duplicating the register wholesale, or reporting the same underlying fact twice under two
           different names because it also sits in another log. -->

| Ref | Description | Status | What changed |
|---|---|---|---|
| {{item_ref}} | {{item_description}} | {{item_status}} | {{item_change}} |

## Next Steps

<!-- WHAT  What happens next, independent of whether it depends on anything raised above.
     WHY   Closes the report on forward motion rather than a list of problems; the most consistently
           attested section in the whole corpus - "The next steps", "Work Planned for Next Week", "Upcoming
           Work" and "Action Items", "Action items". Deep dive: status-report_companion.md section 3
           (Anatomy > Next Steps).
     ASK   What is planned for the next period? Does any of it depend on something raised above, and if so,
           is that dependency named?
     GOOD  "Complete the second merchant cohort rollout, targeting 99.5 percent checkout success by end of the
           next period."
     WEAK  "Continue work." (no specific action, nothing a reader could check next period)
     TRAP  A vague continuation with nothing to verify. Every next step should be checkable: did it happen,
           yes or no, by the next report. -->

- {{next_step_1}}
