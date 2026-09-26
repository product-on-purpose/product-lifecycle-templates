---
title: "{{change_title}}"
change_id: "{{change_id}}"
baseline_artifact: "{{baseline_artifact}}"
baseline_version: "{{baseline_version}}"
requester: "{{requester}}"
date_submitted: "{{date_submitted}}"
decider: "{{decider}}"
decision: "{{decision}}"
decision_date: "{{decision_date}}"
status: "{{status}}"
doc_type: change-request
size: full
source_template: change-request
source_template_version: 0.1.0
---

<!--
FULL CHANGE REQUEST. Everything in the lean variant, plus a documented set of alternatives (including doing
nothing), an explicit boundary on what the change does not touch, and what happens to the request once it is
decided: where it is logged and what it links back to. Use it when the decision needs a documented set of
alternatives, when the boundary of what the change touches is genuinely ambiguous, or when the project keeps
a change log this request must feed into cleanly. See change-request_companion.md section 4.

This is a STRICT SUPERSET of change-request_template-lean.md: the first four sections are identical in name
and order, with the same fields. If you are growing from lean, add the last three sections; do not reorder.

WHAT A CHANGE REQUEST IS. Four independently published bodies define it in close to the same words: a formal
proposal to alter something already agreed about a unit of product work, its scope, requirements, a
deliverable, or the schedule and cost attached to it. This bundle serves the project and product baseline
lineage. A change to a running production system, reviewed by a change advisory board, is the closest
neighbor and is described, never templated, here. See change-request_companion.md section 1 and section 8.

IT IS NOT A DEFECT REPORT. A change request alters an agreement; a defect fails one that was already
promised. Use bug-report for something wrong with what was delivered, and this template for something new
that nothing promised. See change-request_companion.md section 7 (anti-pattern 4) and section 8.

A TEAM CHANGING ITS OWN PRODUCT BACKLOG THROUGH ITS PRODUCT OWNER DOES NOT NEED THIS DOCUMENT. This bundle is
for a baseline that carries weight outside the team: a contract, a regulator, or a budget and scope a
steering group already signed off. See change-request_companion.md section 5 and section 6.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP; a
   section that records more than one entry adds PRIORITY and ROW HINT.
2. Replace each {{placeholder}}. Name the baseline this request changes, by artifact and version, in The
   Request; without it a reviewer cannot tell what "before" even means.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This document is not the change log; it feeds one. Before you share it: self-grade against
   change-request_guide.md, then DELETE every HTML comment. They are guidance, not content.
-->

# {{change_title}}

## The Request

<!-- WHAT  What should change, in one sentence, and the baseline it targets by artifact and version. Who is
           asking, on what date, and where the request came from.
     WHY   PM2's guide describes both routes a request can take: "A change request can be formally submitted
           via a Change Request Form, or can be identified and raised during meetings as a result of
           decisions, issues or risks, and should be documented in the Change Log." PM2's own form splits the
           description itself into two named fields, "Current Situation:" and "Desired Situation:". A vendor
           source argues for keeping a third thing separate from both: "Separate the underlying need from the
           requester's preferred implementation." Deep dive: change-request_companion.md section 3 (The
           Request).
     ASK   What should change, in one sentence? Which baseline does it target, by artifact and version (the
           PRD, the acceptance criteria, the release plan)? What is the current situation, and what is the
           desired one? Who is requesting it, and on what date? Did it come from a decision, an issue, a
           risk, or a meeting already logged elsewhere, and if so, what does it link to?
     GOOD  "Current situation: the permit-booking portal confirms an appointment by email only. Desired
           situation: an applicant can also opt in to a text-message reminder the day before. Targets
           Requirements Specification v2.1, signed off under the fixed-price contract. Requested by the
           permits service manager, 2026-03-02, raised in the fortnightly contract review."
     WEAK  "Add text reminders." (no baseline named, no current or desired split, no origin; a reviewer
           cannot tell what "before" even means)
     TRAP  Naming the change without naming the baseline it targets. Per PM2's guide, a request is an appeal
           to amend "an aspect of the agreed baseline of a project"; leave the baseline out and there is
           nothing on record to compare the change against. -->

**Baseline:** {{baseline_artifact}}, version {{baseline_version}}

**Current situation:** {{current_situation}}

**Desired situation:** {{desired_situation}}

**Requested by:** {{requester}}, {{date_submitted}}

**Where this came from:** {{origin}}

## Why

<!-- WHAT  The reason for the change, including what happens if it is not made.
     WHY   PM2's process instructs the reviewer to "consider the impact of not implementing the proposed
           change, c) estimate the size of the identified change based on its impact on the project
           objectives, schedule, cost and effort, and d) prioritise the implementation of the change request
           in relation to other change requests." A practitioner source treats the consequence of declining
           as decision-critical rather than optional: "In order to make an informed decision, you should
           include details of the consequence of not accepting the change." Deep dive: change-request_
           companion.md section 3 (Why).
     ASK   Why is this change wanted? What happens if it is not made, stated as a real consequence rather
           than an assumption? Is the case honest, without inflating the downside of saying no in order to
           win approval?
     GOOD  "Without a reminder, roughly one booking in eight is missed and the slot goes unused
           (illustrative). If declined, the missed-appointment rate stays where it is, and the contract's
           service levels are measured against that rate."
     WEAK  "This would be a nice improvement." (no consequence of declining stated; reads as upside only)
     TRAP  Overstating the consequence of declining in order to manufacture urgency. The same practitioner
           source warns against exactly this: "do not over state the impact in an attempt to gain approval." -->

{{why}}

## Impact

<!-- WHAT  What the change costs and touches, across the dimensions the baseline was agreed on: scope,
           requirements, deliverables, resources, cost, timeframe, and quality, each stated or marked "None".
     WHY   PM2's guide names exactly these seven dimensions as what a baseline can be amended on: "A change
           request logs an appeal to amend an aspect of the agreed baseline of a project (i.e. scope,
           requirements, deliverables, resources, costs, timeframe or quality characteristics)." A
           practitioner source names impact outside the project as worth a line even where a form gives it
           no field of its own: "it could have an adverse impact on an external project." Deep dive:
           change-request_companion.md section 3 (Impact).
     ASK   For each dimension, does this change touch it, and how much? Where a dimension is untouched, does
           the row say "None" rather than being left blank? Does the impact reach outside this project?
     PRIORITY  Every dimension gets a row, even "None"; a blank cell reads as forgotten, not assessed. One
           vendor source recommends keeping the risk of making the change separate from the risk of declining
           it: "Distinguish the risk of making the change from the risk of declining or delaying it." That
           distinction is vendor-tier guidance, not a settled convention; note it here rather than treating it
           as required.
     ROW HINT  A good row states the actual effect, a duration, a cost or a scope boundary, not just "Yes"
           or "Impacted". A weak row is a bare check mark with no
           magnitude.
     GOOD  | Timeframe | Adds three weeks of build and one of acceptance testing; go-live holds only if work starts before the next milestone (illustrative) |
     WEAK  | Timeframe | Impacted |
     TRAP  Leaving a dimension blank instead of writing "None". A blank cell reads as forgotten, not
           assessed, and the next reader cannot tell whether it was considered. -->

| Dimension | Impact if this change is made |
|---|---|
| Scope | {{impact_scope}} |
| Requirements | {{impact_requirements}} |
| Deliverables | {{impact_deliverables}} |
| Resources | {{impact_resources}} |
| Cost | {{impact_cost}} |
| Timeframe | {{impact_timeframe}} |
| Quality | {{impact_quality}} |

## Decision

<!-- WHAT  The outcome, chosen from a stated set, made by one named decider, by a stated date, with any
           conditions spelled out.
     WHY   PM2 names four possible decisions: "There are four possible decisions: approve, reject, postpone
           or merge the change request." PMI's Lexicon defines the deciding body: "A formally chartered group
           responsible for reviewing, evaluating, approving, delaying, or rejecting changes to the project,
           and for recording and communicating such decisions." PRINCE2 delegates the decision to a named
           change authority instead: "The change authority is a person or group to whom the project board may
           delegate responsibility for reviewing and approving change requests or off-specifications. This
           authority may be given a change budget and can approve changes within that budget," illustrated
           with a worked delegation of changes under 400 euros to the project manager. Deep dive:
           change-request_companion.md section 3 (Decision).
     ASK   Which decision was made: approve, reject, postpone, or merge? Who is the one named decider (a
           person or a named board), and by what date is the decision needed? If approved with conditions,
           what is each condition, who owns it, and by when?
     PRIORITY  Pick the decision from this stated set rather than inventing one; a bespoke choice leaves the
           next reader guessing what it meant. A decision deadline and a per-condition owner and deadline are
           included here on vendor and practitioner-tier evidence only, not a settled industry convention: a
           practitioner source states "you should include the deadline by when a decision is required on the
           change request", and a vendor source states "Approval with conditions must identify the owner and
           deadline for each condition." Label them as such if you keep them. Where more than one authority
           must sign off, repeat the Decision, Decider and Decision made on lines once per authority rather
           than one merged status; the same vendor source warns "do not collapse them into an overall green
           status before every mandatory approval is satisfied."
     ROW HINT  A good condition row names the condition, an owner, and a deadline. A weak row states a
           condition with no owner and no deadline, which in practice turns conditional approval into
           unconditional approval.
     GOOD  "Decision: approve, with one condition. Decider: the contract's change authority, the service's
           head of digital. Decision needed by: 2026-03-16. Condition: the supplier confirms the text
           provider's data-processing terms; owner the supplier's delivery lead, by 2026-03-30."
     WEAK  "Approved, I guess, whenever." (no named decider, no date, and not one of the stated decisions)
     TRAP  Recording a bare yes or no instead of one of the four stated decisions, or leaving the decision
           undated. One vendor source ties an undated decision directly to indefinite deferral: "A change
           request without a deadline gives the board permission to defer indefinitely." (vendor tier, thin
           evidence; label it as such if you cite the pattern) -->

**Decision:** {{decision}}

**Decider:** {{decider}}

**Decision needed by:** {{decision_deadline}}

**Decision made on:** {{decision_date}}

**Conditions (if approved with conditions):**

| Condition | Owner | Deadline |
|---|---|---|
| {{condition}} | {{condition_owner}} | {{condition_deadline}} |

## Options Considered

<!-- WHAT  The alternatives weighed, including doing nothing, and why the chosen option won.
     WHY   A widely distributed free template names this directly: "Options considered to implement the
           change", scored per option on "Cost, Scope, Schedule and Quality". A vendor source insists the
           no-change option itself belongs on the list: "Include the no-change option plus realistic
           alternatives." Texas DIR's form carries a plainer version of the same idea, an "Alternatives"
           field. Deep dive: change-request_companion.md section 3 (Options Considered).
     ASK   What alternatives were considered, including doing nothing? For each, what is its impact on cost,
           scope, schedule, and quality? Which option was chosen, and why did it win over the others?
     PRIORITY  Write the no-change option even when it obviously loses; a reviewer who cannot see it was
           considered cannot tell whether it was rejected or never asked.
     ROW HINT  A good option row names the option, its impact across cost, scope, schedule, and quality,
           whether it was chosen, and why it won or lost. A weak row is an option name with no impact
           assessment and no verdict.
     GOOD  | Do nothing | Keep email confirmation only | No cost; no schedule change; the missed-appointment
           rate stays as it is | No | Leaves the service-level gap the request exists to close |
     WEAK  | New feature | Good idea | | | |
     TRAP  Omitting the no-change option, or listing only the option that was chosen. Either way, the next
           reader cannot tell whether an alternative was weighed and rejected, or never considered. -->

| Option | Description | Impact (cost, scope, schedule, quality) | Chosen? | Why |
|---|---|---|---|---|
| {{option_name}} | {{option_description}} | {{option_impact}} | {{option_chosen}} | {{option_reason}} |

## Out of Scope

<!-- WHAT  A stated boundary naming what the change explicitly does not touch.
     WHY   PM2's own form carries this as a named section, "Out of Scope:", and a vendor source states the
           rule behind it: "Define what will be added, removed or modified and what remains explicitly out
           of scope." Deep dive: change-request_companion.md section 3 (Out of Scope).
     ASK   What does this change explicitly not touch, that a reader might otherwise assume is included?
     GOOD  "This change adds a day-before text reminder only. It does not add two-way texting or
           rescheduling by text, and it does not change how an appointment is booked or confirmed by
           email."
     WEAK  "Nothing else changes." (too vague to catch the specific thing a reader would otherwise assume)
     TRAP  Leaving the boundary unwritten. An unwritten boundary is not a boundary; the next reader assumes
           everything not explicitly excluded is included. -->

{{out_of_scope}}

## Implementation and Traceability

<!-- WHAT  What happens to the request once it is decided: where it is logged, what it links back to, and
           what it updates.
     WHY   PM2's own form is archived once logged: "Once the change request is logged into the Change Log,
           then this form is updated with the assigned Change ID and the form is archived." The PMBOK Guide's
           errata states the log's job in the same terms: "The change log is used to record all submitted
           change requests." A vendor source states the standard for what a full record should let a later
           reader do: "A sound record lets an authorized reviewer reconstruct the prior baseline, requested
           difference, evidence, options, authority, implementation and result." Deep dive:
           change-request_companion.md section 3 (Implementation and Traceability) and section 8
           (Relationships to other artifacts).
     ASK   Once decided, what is updated (which artifact, which new version)? What is this request's entry
           in the change log, or, if the project keeps none, where is the decision recorded instead? What
           does it link back to (the issue, risk, or decision it came from)? The request is not the log; it
           feeds one, and a good entry names the log ID, the artifact and version updated, and the origin.
     GOOD  "Change log: entry 14 in the contract's change log. Updated: Requirements Specification, v2.1
           to v2.2, and the contract's price schedule. Links back to: the fortnightly contract review of
           2026-03-02 (no issue or risk raised this)."
     WEAK  "Logged and updated." (no ID, no artifact or version, nothing a reader could follow)
     TRAP  Duplicating another log's own detail here instead of linking to it. This section is a
           cross-reference and an update record, not a second copy of the change log or the issue log. -->

{{implementation_and_traceability}}
