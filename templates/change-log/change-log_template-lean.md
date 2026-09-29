---
title: "{{project_name}} Change Log"
project: "{{project_name}}"
status: "{{status}}"
doc_type: change-log
size: lean
source_template: change-log
source_template_version: 0.1.0
---

<!--
LEAN CHANGE LOG. The smallest change log that is still a real one: the baseline (or baselines) it tracks
and what does not belong in it, the status and decision vocabulary stated once, the load-bearing table
itself (one row per change request, and no row is ever deleted), and the authority that decides plus the
point at which a change goes above it. Use it when the team decides and closes its own changes without a
formal delivery hand-off, a standing cumulative figure anyone asks for, or more than one person who could
plausibly be asked to keep the log. To grow it into the governance-grade form (see
change-log_template-full.md), ADD sections; never rename or reorder the ones below, because the full
variant is a strict superset of this one.

WHAT A CHANGE LOG IS. Three named bodies describe the same job in close to the same words. PMI's own
errata to the PMBOK Guide states it plainly: "The change log is used to record all submitted change
requests." The European Commission's PM² guide adds the verb the log actually serves: "A Change Log is
used to document, monitor and control all project changes (see Appendix B)." The Association for Project
Management's glossary states the outcome named: "A record of all project changes: proposed, authorised,
rejected or deferred." It is a standing, cumulative register, kept apart from the request document itself
and from the decision recorded about each row. See change-log_companion.md section 1.

IT IS NOT THE CHANGE REQUEST, AND IT IS NOT A SOFTWARE CHANGELOG. A change request is one document, filed
to describe and justify a single proposed change; this log is the standing register that gets one row per
request, whatever its eventual disposition. A software changelog is a different artifact under the
identical word: "A changelog is a file which contains a curated, chronologically ordered list of notable
changes for each version of a project." It is written for users and contributors, with no requester,
decider, decision, or status field at all. See change-log_companion.md section 1 and section 8.

PRINCE2 KEEPS THIS INSIDE ITS ISSUE REGISTER, BY DESIGN. A team already running PRINCE2 records a request
for change as one of its issue types ("Issues must be recorded in the issue register") and names a change
log only as an alternative place to write the eventual decision. This is a named methodology choice, not a
gap this template is filling. See change-log_companion.md section 1 and section 5.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP; the
   status list and the table also carry PRIORITY and ROW HINT.
2. Replace each {{placeholder}}. The Change Log table is the heart; no row is ever deleted, including a
   rejected, withdrawn, or postponed one, and each row names the baseline it would change, by artifact and
   version.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This document is never finished, but before you share it: self-grade against change-log_guide.md, then
   DELETE every HTML comment. They are guidance, not content.
-->

# {{project_name}} Change Log

## Purpose and Boundary

<!-- WHAT  A short statement of which baseline, or baselines, this log tracks, by artifact and version,
           and what does not belong in it.
     WHY   The name collides with two other documents a reader will meet under similar words, and the
           first job of this section is to rule them out before the table starts. A software changelog
           exists for a different purpose, stated in its own governing convention: "To make it easier for
           users and contributors to see precisely what notable changes have been made between each
           release (or version) of the project." It carries no requester, decider, or decision field at
           all. PRINCE2 is the named exception on the methodology side: it keeps a request for change
           inside its issue register and names a change log only as an alternative place the decision
           "should be documented in the issue register or change log." Deep dive:
           change-log_companion.md section 3 (Purpose and Boundary).
     ASK   Which baseline, or baselines, does this log track, by artifact and version? What does not
           belong here: the change request document itself (a separate document that feeds one row into
           this log), a software changelog, or, if this team runs PRINCE2, its issue register? Who is
           expected to read this log?
     GOOD  "This log tracks change requests against the Business License Renewal Requirements
           specification, currently version 2.0. It is not the change request form itself (each request
           is filed as its own document; this log gets one row per request) and not a software changelog
           (no code releases are tracked here)."
     WEAK  "Tracks changes to the project." (no baseline named by artifact or version, and does not say
           what is deliberately left out)
     TRAP  Treating a single request document as though it were this log, or letting this log absorb a
           software release's changelog. Name the baseline and rule the neighbors out before the table
           starts. -->

{{purpose_and_boundary}}

## Status Vocabulary

<!-- WHAT  The status values a change request can hold on this log, and, kept apart from status, the
           decision values that record what was actually decided.
     WHY   No two published sources use the same status list, and naming both up front is what keeps the
           table itself short. PM²'s guide offers "Submitted, Investigating, Waiting for approval,
           Approved, Rejected, Postponed, Merged or Implemented" as one sourced default (its own appendix
           names the second value "Assessing: Use this status to initiate an assessment" instead, an
           inconsistency in the source itself, not a choice this template is making for you); Connecticut
           DSS offers "Submitted, In Review, Approved, Denied, Deferred, Withdrawn, or Closed" as an
           alternative. Decision is kept distinct from status, following PM²'s own field: "There are four
           possible decisions: approve, reject, postpone or merge the change request." HHS's own "Closed"
           value shows why the split matters: "The change request is no longer considered an active
           project threat and can be closed with or without resolution." That sentence never says which
           way it went. Deep dive: change-log_companion.md section 3 (Status Vocabulary) and section 6 (which
           statuses, and is the decision a status).
     ASK   What status values does this log use, stated once so every row is comparable? What decision
           values are possible, kept apart from status? What priority scale does the Change Log table
           below assume?
     PRIORITY  State the list here, once, rather than letting each row invent its own values. If a
           published source you are borrowing from is internally inconsistent about a value's name (as
           PM²'s own guide is), say so rather than silently picking one and hiding the source's own
           disagreement.
     ROW HINT  A good status value says what triggers moving into it. A weak one is a bare word with
           nothing to distinguish it from its neighbors, or a status like "Closed" that never says which
           way the decision went.
     GOOD  "Status: Submitted, Investigating, Waiting for approval, Approved, Rejected, Postponed,
           Merged, Implemented. Decision, kept apart from status: Approve, Reject, Postpone, or Merge.
           Priority: Critical, High, Medium, Low."
     WEAK  "Open or Closed." (two values, no decision field, and Closed hides whether the request was
           approved or rejected)
     TRAP  Treating "Closed" as though it says what was decided. A closed row still needs its own Decision
           field stated, or a reader cannot tell an approved change from a rejected one. -->

**Status values:** {{status_values}}

**Decision values (kept apart from status):** {{decision_values}}

**Priority scale:** {{priority_scale}}

## Change Log

<!-- WHAT  The load-bearing table, one row per change request: an identifier, its category, a one-line
           description of the change, the baseline it would change (by artifact and version), who
           requested it and when, its priority, its status, the decision made and the reason for it, and
           who decided it and when.
     WHY   HHS states the rule the whole table exists to keep: "Each change request should be recorded as
           a single line item. Do not combine multiple requests under one change request ID." No row is
           ever deleted for having gone the wrong way: APM's own definition already names rejected and
           deferred outcomes as part of what the log records, not exceptions to it ("proposed, authorised,
           rejected or deferred"), and Connecticut carries "Withdrawn" and "Deferred" as ordinary statuses,
           not removals. Keeping a rejected row on record "prevents the same request from being
           resubmitted without understanding why it was declined." Three or more of the published field
           lists checked for this bundle share an identifier, a description, the date raised, and a status;
           most also carry a requester and a priority. This template adds two fields beyond that shared spine: the
           baseline each request would change, following HHS's own shared data element: "The product
           version that the suggested change is for." The second is the decision with its reason, kept
           beside the row (HHS's own spreadsheet carries this as a field named "Final Resolution &
           Rationale", and Connecticut's own log carries a Resolution/Comments column). Who decided a
           change and when belong here, in lean; the full variant adds the surrounding delivery detail
           without adding a new field's worth of judgment to this table. Deep dive:
           change-log_companion.md section 3 (Change Log).
     ASK   For each change request: what is its identifier and category? What is the change, in one line?
           Which baseline does it change, by artifact and version? Who requested it, and when? What is its
           priority and current status? What was decided, and why? Who decided it, and when?
     PRIORITY  No row is ever deleted, including a rejected, withdrawn, or postponed one. Decision is a
           distinct field from status, never folded into it. Baseline is named by artifact and version,
           never left as "the plan."
     ROW HINT  A good row names the baseline by artifact and version, states the decision and its reason
           in the same cell, and names one person as decider. A weak row leaves the decision blank because
           the status column looks like it already says enough.
     GOOD  | CHG-014 | Scope | Add a 10-day grace-period reminder email before a business license lapses |
           Business License Renewal Requirements | 2.0 | Dana Okafor, 2026-04-03 | Medium | Approved, with
           a condition | Reduces late-renewal calls to the service desk; condition is a confirmed sender
           identity for the reminder email | Luis Ferreira, 2026-04-15 |
     WEAK  | CHG-014 | | Reminder email | | | | | Approved | | |
     TRAP  Recording only a status and leaving the decision cell blank, or deleting a row once a request
           is rejected. Both leave the next reader unable to tell what actually happened to that
           request. -->

| ID | Category | Change | Baseline artifact | Baseline version | Requested by (date) | Priority | Status | Decision (and reason) | Decided by (date) |
|---|---|---|---|---|---|---|---|---|---|
| {{change_id}} | {{category}} | {{change_description}} | {{baseline_artifact}} | {{baseline_version}} | {{requested_by_date}} | {{priority}} | {{status}} | {{decision_and_reason}} | {{decided_by_date}} |

## Authority and Escalation

<!-- WHAT  Who may decide which changes on this log, and the point at which a change goes above that
           person or group.
     WHY   Every source found on this subject is actually about who holds the authority to decide;
           escalation is simply what happens when a change exceeds it, which is why this section carries
           this name rather than the more common "Escalation" alone. PRINCE2's practitioner literature
           states the role plainly: "The change authority is a person or group to whom the project board
           may delegate responsibility for reviewing and approving change requests or off-specifications."
           HHS supplies a worked threshold from its own program: "a project manager (PM) may be authorized
           to personally approve changes with a project impact of less than $5,000" (HHS's own figure,
           reported here as its example, not as a rule this template sets for every project). PM² carries
           the same idea as a per-row flag rather than a policy statement: "Escalation to the Directing or
           Steering layer is needed? (Yes or No)." Deep dive: change-log_companion.md section 3 (Authority
           and Escalation).
     ASK   Who decides a change on this log, by default? At what point does a change go above that person
           or group, stated as a threshold rather than left to a judgment call each time? What is
           currently escalated, to whom, and what decision is being waited on?
     PRIORITY  State the threshold before it is needed, not the first time a change tests it. Escalate to
           get a decision, never to assign fault for the change itself.
     ROW HINT  A good escalation entry names the change, who it went to, the date, and the decision being
           waited on. A weak entry says only "escalated," with nothing else a reader could follow up on.
     GOOD  "Authority: Luis Ferreira, licensing program manager, decides any change to the renewal
           service's own screens, wording, or reminder schedule. A change to a fee, an eligibility rule, or
           a statutory deadline goes to the licensing board, because those are set outside the service.
           Currently escalated: CHG-017, to the licensing board on 2026-04-22, waiting on whether a late
           fee may be waived after a service outage."
     WEAK  "Whoever is around approves it." (no named authority, no threshold, and nothing to check an
           escalation against)
     TRAP  Naming a board as the decider without stating which changes it actually decides. Without a
           threshold, every row becomes its own judgment call about whether to ask. -->

**Authority:** {{authority}}

**Escalation threshold:** {{escalation_threshold}}

**Currently escalated:** {{escalation_record}}
