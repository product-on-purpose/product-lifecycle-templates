---
title: "{{plan_title}}"
business_unit: "{{business_unit}}"
owner: "{{owner}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: business-continuity-plan
size: lean
source_template: business-continuity-plan
source_template_version: 0.1.0
---

<!--
LEAN BUSINESS CONTINUITY PLAN. The load-bearing core: who this plan covers, the team and the activation
authority, what each critical process needs to survive a disruption, how it keeps running without its
normal systems, how an activation unfolds, how the plan is tested, the records that keep it usable, and
what would make the plan itself wrong. Eight sections, because disaster recovery is documented in a
separate plan and Purpose and Scope points to it by name and location. When this plan must carry disaster
recovery itself, add the Disaster Recovery section from business-continuity-plan_template-full.md. ADD
the section, never rename or reorder the ones below, because the full variant is a strict superset of this
one.

THIS PLAN KEEPS BUSINESS PROCESSES GOING; A DISASTER RECOVERY PLAN RECOVERS THE SYSTEMS THOSE PROCESSES
USE. NIST defines the plan as "The documentation of a predetermined set of instructions or procedures that
describe how an organization's mission/business processes will be sustained during and after a
significant disruption," and FEMA's Ready Business program ships it as a fill-in template. Disaster
recovery is narrower: NIST scopes it to "an alternate facility." This lean variant points to a separate
disaster recovery plan, the shape FEMA's template allows when it lists "Information Technology Disaster
Recovery Plan (if not included in the business continuity plan)." See business-continuity-plan_companion.md
section 1 and section 6, item 1.

THIS PLAN IS A STANDING INSTRUMENT, NOT A RECORD OF ONE DISRUPTION. A team executes it under time
pressure once a disruption is declared or a drill begins. Update this file when the plan itself needs to
change, not every time it is activated. See business-continuity-plan_companion.md section 6, item 3.

WHAT THIS PLAN IS NOT
It is NOT a runbook, which is one operational procedure for a known, narrower situation; this plan can call
out to one. It is NOT a production readiness review, which checks a service's fitness for a routine
handoff. It is NOT an incident postmortem, written after one event has resolved. It is NOT a risk register,
which tracks events before they happen. And a high-availability design is not disaster recovery by itself.
See business-continuity-plan_companion.md section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   business-continuity-plan_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the
   TRAP to avoid. For tables, PRIORITY explains the ordering rule and ROW HINT says what a good row
   contains.
2. Replace each {{placeholder}} with your content. Fill Business Continuity Team and Roles and Business
   Impact Analysis Summary first; the rest depends on knowing who runs this plan and which processes it
   protects.
3. If a section, or one row inside a table, does not apply, write "N/A" and the reason beside it rather
   than leaving it blank or deleting the section. An unexplained "N/A" and a skipped item look identical
   to a later reader.
4. Before you ship it: self-grade against business-continuity-plan_guide.md, then DELETE every HTML
   comment. They are guidance, not content.
-->

# {{plan_title}}

## Purpose and Scope

<!-- WHAT  The business or unit this plan covers, what counts as a significant disruption in this plan's
           own scope, and where a separate disaster recovery plan lives if this plan does not carry one.
     WHY   NIST defines the type this plan fills: "The documentation of a predetermined set of
           instructions or procedures that describe how an organization's mission/business processes will
           be sustained during and after a significant disruption." FEMA's Ready Business template lists
           "Information Technology Disaster Recovery Plan (if not included in the business continuity
           plan)" among the related plans a complete program keeps, which is the source for the pointer
           below: where this plan does not carry its own Disaster Recovery section, this is where a reader
           is told a separate plan exists and where it is kept. Deep dive:
           business-continuity-plan_companion.md section 3 (Anatomy > Purpose and Scope) and section 6,
           item 1.
     ASK   What business or unit does this plan cover? What counts as a "significant disruption" here, in
           plain language? Does a separate disaster recovery plan already exist as its own document? If
           so, name it and say where it is kept.
     GOOD  "This plan covers Meridian Freight's claims-processing division. A significant disruption is
           any event, a facility loss, an extended system outage, a regional disaster, that prevents claims
           processing for more than four hours. A separate IT Disaster Recovery Plan is maintained by the
           Infrastructure team and is not duplicated here; see the Infrastructure team's internal wiki for
           the current copy."
     WEAK  "This is our business continuity plan." (no scope, no definition of a disruption, and no note
           on where disaster recovery lives)
     TRAP  Treating "disaster recovery plan" and "business continuity plan" as two names for one document.
           NIST and FEMA both treat disaster recovery as a narrower plan that may sit inside or beneath
           this one; neither source treats the two as equivalent. -->

{{continuity_scope_statement}}

**Separate disaster recovery plan, if one exists outside this document:** {{disaster_recovery_plan_pointer}}

## Business Continuity Team and Roles

<!-- WHAT  The team roster by job title, the person with authority to activate this plan, a named
           successor, and any delegation that takes effect when normal channels of direction are
           disrupted.
     WHY   FEMA's template carries its own "Business Continuity Organization" section naming the team.
           California's instructions ask that "job titles (rather than the names of individuals) should be
           used to assign responsibility as it lessens maintenance on procedures as personnel changes."
           NIST requires a single activation authority: "Only one individual should have this authority,
           and a successor should be clearly identified to assume that responsibility if necessary." FEMA's
           continuity guidance adds the delegation mechanism: "predetermined delegations of authority will
           take effect when normal channels of direction are disrupted and will terminate when these
           channels are reestablished," and asks that delegates also be named "by position title and not by
           name." Who actually writes, activates, and executes a plan like this is not settled across the
           sources this bundle read; name your own roles explicitly rather than assuming one pattern
           applies here. Deep dive: business-continuity-plan_companion.md section 3 (Anatomy > Business
           Continuity Team and Roles) and section 6, item 4.
     ASK   What roles does this plan depend on, by job title? Who currently holds each one? Who has
           authority to activate this plan, and who is that person's named successor? Does a delegation
           clause need to state what happens if neither is reachable?
     PRIORITY  List the activation authority and successor first, so a reader under time pressure finds the
           one answer they need before anything else on this page.
     ROW HINT  A good row names a job title, not only a person, and states what that role actually does
           when this plan runs. A weak row names a person with no title and no stated backup.
     GOOD  | Business Continuity Team Lead | Priya Shah, Director of Operations | Has authority to
           activate this plan; successor is the Deputy Director of Operations |
     WEAK  | Team Lead | Priya | (no title, no successor, nothing to fall back on if Priya is unreachable)
     TRAP  Naming individuals instead of job titles. California's own instructions give the reason
           directly: it "lessens maintenance on procedures as personnel changes." A plan that names only
           people goes stale the day one of them leaves. -->

| Role | Job Title and Current Holder | Responsibility |
|---|---|---|
| {{team_role}} | {{team_role_holder}} | {{team_role_responsibility}} |

**Authority to activate this plan:** {{activation_authority_title_and_holder}}
**Named successor if the activation authority is unreachable:** {{activation_successor_title_and_holder}}
**Delegation of authority, if normal channels of direction are disrupted:** {{delegation_of_authority_statement}}

## Business Impact Analysis Summary

<!-- WHAT  Each critical business process, its Recovery Time Objective and Recovery Point Objective, and
           the systems and suppliers it depends on, carried over from a separate Business Impact Analysis.
     WHY   NIST frames the analysis as upstream and prior: "The BIA is the first source for determining
           resiliency and contingency planning strategies," and its results "should be appropriately
           incorporated into" the plans that follow. FEMA's own template field reads "Insert results of
           Business Impact Analysis," and California requires that the recovery plan "must be derived
           from" the BIA. The two objectives are defined consistently across the sources this bundle read:
           a Recovery Time Objective is "the maximum acceptable delay between the interruption of service
           and restoration of service," and a Recovery Point Objective is "the maximum acceptable time
           after the last data recovery point." A supplier contract states the same obligation this table
           carries for suppliers: "Supplier shall ensure all Subcontractors have Business Continuity
           Programs and Disaster Recovery Plans sufficient to meet delivery of the Services during a
           Disruptive Event." Deep dive: business-continuity-plan_companion.md section 3 (Anatomy >
           Business Impact Analysis Summary).
     ASK   For each critical process: what is its Recovery Time Objective and Recovery Point Objective, in
           plain units of time? What systems does it depend on? What suppliers does it depend on?
     PRIORITY  List the process with the shortest Recovery Time Objective first, so the most time-critical
           process is visible without reading the whole table.
     ROW HINT  A good row states Recovery Time Objective and Recovery Point Objective in concrete time
           units and names specific systems and suppliers, not "various." A weak row writes "TBD" or
           leaves the dependency columns blank.
     GOOD  | Claims intake | 4 hours | 1 hour | Claims database; the regional scanning vendor |
     WEAK  | Claims intake | Fast | N/A | (no units, and the dependency columns are not actually filled
           in)
     TRAP  Deriving Recovery Time Objectives and Recovery Point Objectives from scratch in this table. This
           table carries a separate Business Impact Analysis's results; it is not the analysis itself. If
           you are deriving these figures for the first time, that work happens in a Business Impact
           Analysis, not here. -->

| Critical Process | Recovery Time Objective | Recovery Point Objective | Systems and Suppliers Depended On |
|---|---|---|---|
| {{critical_process}} | {{process_rto}} | {{process_rpo}} | {{process_dependencies}} |

## Continuity Strategies and Manual Workarounds

<!-- WHAT  How each critical process keeps running without the systems it normally depends on, and at what
           recovery level, chosen against cost.
     WHY   FEMA's template names this as its own section, "Manual Workarounds." The cost tradeoff that
           governs how far to invest in a workaround is stated most explicitly by AWS's own recovery
           strategies, ordered "in increasing order of cost and complexity, and decreasing order of RTO and
           RPO," with an explicit warning: "You should avoid implementing a strategy that is more stringent
           than it needs to be, as this incurs unnecessary costs." Google states the same tradeoff for the
           process as a whole: "Typically, the smaller your RTO and RPO values are... the more your
           application will cost to run." A high-availability technical design, by itself, is not a
           continuity strategy for the business process it supports: "HA doesn't entirely overlap with DR,
           but it's often necessary to take HA into account when you're thinking about RTO and RPO values."
           Deep dive: business-continuity-plan_companion.md section 3 (Anatomy > Continuity Strategies and
           Manual Workarounds).
     ASK   For each critical process, what do staff actually do by hand when the normal system is
           unavailable? What recovery level was chosen, and why, given what it costs against how fast the
           process actually needs to recover?
     PRIORITY  List the process with the shortest Recovery Time Objective, from Business Impact Analysis
           Summary above, first, since it is first in line for investment.
     ROW HINT  A good row states what staff actually do, step by step, not that a workaround "exists." A
           weak row asserts a workaround with no description of the steps.
     GOOD  | Claims intake | Staff log claims to a shared paper form and a backup laptop with offline
           storage, then enter them into the database once it is back | Manual, low cost, matches the
           process's own four-hour Recovery Time Objective |
     WEAK  | Claims intake | Manual workaround exists | (no description of what staff actually do, and no
           stated reason for the recovery level chosen)
     TRAP  Choosing a workaround faster than the process actually needs. AWS's own warning applies here even
           though it was written about technology recovery: a workaround that beats its process's own
           Recovery Time Objective is also one that costs more than it needs to. -->

| Critical Process | Manual Workaround | Recovery Level Chosen, and Why |
|---|---|---|
| {{workaround_process}} | {{workaround_description}} | {{workaround_recovery_level_rationale}} |

## Activation and Incident Management

<!-- WHAT  Stated activation criteria, who declares an activation, who is told and in what order, and the
           condition for standing the plan down.
     WHY   NIST requires that activation criteria be stated in advance and tied to a designated authority:
           "The designated authority... has the authority to activate the contingency plan," triggered
           when "one or more of the activation criteria for that system are met." California asks the plan
           to identify "individual(s) responsible for making the TRP activation decision." HMPPS separates
           who activates from who writes the plan: "A member of the nominated Business Continuity team will
           normally activate and stand down the plans." Where regulation requires it, notice extends past
           an organization's own staff: FINRA binds its member firms to "disclose to its customers how its
           business continuity plan addresses the possibility of a future significant business disruption."
           Deactivation is its own named step, not an afterthought: NIST's reconstitution phase "consists
           of two major activities: validating successful reconstitution and deactivation of the plan."
           Deep dive: business-continuity-plan_companion.md section 3 (Anatomy > Activation and Incident
           Management).
     ASK   What specific conditions trigger an activation? Who declares one? Who is notified, in what
           order, and by what method, including anyone outside the organization you owe notice to? What
           condition stands the plan down?
     PRIORITY  List notifications in the actual order they go out, so the first call someone makes during a
           real disruption is the first row on this page.
     ROW HINT  A good row names a specific role or entity and a method that still works if the usual
           channel is down. A weak row says "notify everyone" with no order and no method.
     GOOD  | 1 | Business Continuity Team Lead | Paged directly; confirms the activation decision |
     WEAK  | | Everyone | (no order, no method, and no way to tell who actually gets called first)
     TRAP  Treating a regulatory or customer notification duty as universal. FINRA's duty binds its own
           member firms specifically; fold a notification line like it in only where your own organization
           actually owes that notice. -->

**Activation criteria:** {{activation_criteria}}
**Who declares an activation:** {{activation_decision_maker}}

| Order | Who Is Notified | Method |
|---|---|---|
| {{notification_order}} | {{notification_recipient}} | {{notification_method}} |

**Condition for standing this plan down:** {{stand_down_condition}}

## Training, Testing and Exercising

<!-- WHAT  The exercise schedule and type, what each one validates, who observes it, and each finding as
           an owned, dated corrective action.
     WHY   The FFIEC names four test types, from lightest to heaviest: "Orientation/Walk-through,"
           "Tabletop/Mini-drill," "Functional Testing," and "Full-scale Testing," and names a specific
           insufficient test: "Unmanned recovery testing, where back-up tapes are sent to the recovery site
           to be run by service provider employees, is not a sufficient test." The same source asks that
           "the audit department or other independent party should directly observe tests." A test is
           judged against named criteria, not a bare pass or fail: Google names three, "data integrity,
           recovery time objective (RTO), and recovery point objective (RPO)." Microsoft adds that a test
           must exercise the people, not only the systems: "Include all of the human processes in your
           drills, and don't just focus on the technical processes." Findings become tracked, owned work:
           FEMA's continuity guidance names a standing "Corrective Action Program (CAP)," where
           "Deficiencies, actions to correct them, and a timeline for remedy are documented," and HMPPS
           requires that "Debrief sessions must be held following an exercise and lessons learnt log
           completed." A practitioner argues directly that these activities carry no pass or fail judgement
           at all, "these activities are an exercise, not a test"; this bundle keeps both words in this
           section's own title rather than choosing a side. Deep dive:
           business-continuity-plan_companion.md section 3 (Anatomy > Training, Testing and Exercising) and
           section 6, item 6.
     ASK   What type of exercise is scheduled? What is it meant to validate? Who observes it, independently
           of the team being exercised? For every finding, who owns the fix, and by what date?
     PRIORITY  List the most recent exercise first, so a reader can see immediately whether this plan has
           actually been tested recently.
     ROW HINT  A good row's finding carries a named owner and a due date, even for a minor gap. A weak row
           records a finding with neither, which leaves no one to ask about it later.
     GOOD  | Tabletop | 2026-03 | Activation and notification sequence | Internal audit | Notification to
           the regional scanning vendor took 40 minutes longer than planned | Ops Manager | 2026-04-15 |
     WEAK  | Drill | sometime | everything | the team | some gaps | | (no observer independent of the
           team, no owner, no date)
     TRAP  Letting an unmanned test, where someone else's staff run the recovery from backup tapes while
           your own team only watches, count as a sufficient test; or testing only the technical process
           and leaving out the people who would actually run it during a real disruption. -->

| Exercise Type | Date | What It Validates | Observer | Finding | Corrective Action Owner | Due Date |
|---|---|---|---|---|---|---|
| {{exercise_type}} | {{exercise_date}} | {{exercise_validates}} | {{exercise_observer}} | {{exercise_finding}} | {{corrective_action_owner}} | {{corrective_action_due_date}} |

## Plan Administration

<!-- WHAT  Vendors and contractors this plan depends on, a dated revision history, and where a reachable
           copy of the plan is kept, including who holds the master copy.
     WHY   FEMA names this cluster of sections directly: "Vendors & Contractors," "Revision History," and
           "Plan Distribution & Access," with its own distribution rule stated plainly: "A master copy of
           the document should be maintained by the business continuity team leader." The reason a plan
           needs a reachable, offline copy is sourced to the kind of event the plan exists to survive: a
           federal ransomware response guide asks that organizations "Ensure a hard copy of the plan and
           an offline version is available," and FEMA's continuity guidance asks organizations to "strongly
           consider multiple redundant media for storing their essential records." FINRA ties this section
           to an update trigger, not only a storage rule: "Each member must update its plan in the event of
           any material change to the member's operations, structure, business or location." Deep dive:
           business-continuity-plan_companion.md section 3 (Anatomy > Plan Administration).
     ASK   Which vendors and contractors does this plan depend on, and what do they each actually provide?
           Is there a dated revision history? Where is a copy of this plan kept that does not depend on
           the systems the plan protects? Who holds the master copy?
     PRIORITY  List vendors whose failure would stop a critical process, named in Business Impact Analysis
           Summary above, before ones that merely support it.
     ROW HINT  A good vendor row names what the vendor actually provides and a contact method that still
           works if the vendor's own portal is down. A weak row is a name with no service and no backup
           contact method. A good revision row says what changed and which event caused it, such as an
           exercise finding, an activation, or a change in people or suppliers; a weak one says only
           "updated".
     GOOD  | Regional scanning vendor | Scans and routes paper claims when the office is inaccessible |
           24-hour support line, not only the vendor's ticketing portal |
     WEAK  | Northline Scanning | (no service stated, and no contact method that works if their portal is
           down)
     TRAP  Keeping the only copy of this plan on the same network or in the same facility the plan exists
           to recover. That is a stated precaution in the sources this bundle read, not a measured failure,
           but the logic holds either way: a plan reachable only through the systems it protects is
           unreachable exactly when it is needed. -->

| Vendor or Contractor | What They Provide | Contact Method |
|---|---|---|
| {{vendor_name}} | {{vendor_service}} | {{vendor_contact_method}} |

| Version | Date | Changed By | Summary of Change |
|---|---|---|---|
| {{revision_version}} | {{revision_date}} | {{revision_author}} | {{revision_summary}} |

**Master copy held by:** {{master_copy_holder}}
**Where a reachable, offline copy of this plan is kept:** {{offline_copy_location}}

## Review Trigger

<!-- WHAT  A named owner and the conditions that would make this plan itself wrong: a change in people,
           suppliers, systems, facilities or the business; a change to the Business Impact Analysis; an
           activation; or an exercise or test finding. Not a calendar date alone.
     WHY   No source read for this bundle publishes a section with this name or job; it is required
           directly by this library's standing-standards family contract, and this bundle labels it as its
           own contribution rather than received practice. The conditions it names are drawn from sources
           that state a trigger without naming this section: NIST's narrative sets the general rule, "the
           plan should be reviewed for accuracy and completeness at an organization-defined frequency or
           whenever significant changes occur to any element of the plan," adding that "Certain elements,
           such as contact lists, will require more frequent reviews." The FFIEC ties a review to "any
           changes to key personnel, policies, procedures, facilities, equipment, outsourcing
           relationships, vendors, or other components that impact a critical business function." HMPPS
           ties a review to the same two events this section names, "annually or following an incident or
           exercise." Where a regulator or policy requires an annual exercise, it appears here as a floor
           under these conditions, not as the trigger itself. Deep dive:
           business-continuity-plan_companion.md section 3 (Anatomy > Review Trigger) and section 6, item
           3.
     ASK   Who is the single named owner of this section? What specific events would make you revise this
           plan, beyond a calendar date alone?
     PRIORITY  List event-based conditions before any calendar floor, so the floor reads as a minimum
           under them rather than as the headline rule.
     ROW HINT  A good row names a specific event, a named owner, and what they do about it. A weak row
           names only a calendar date.
     GOOD  | A failed finding from a tabletop or drill | Business Continuity Team Lead | Investigate which
           existing procedure should have caught it before writing a new one |
     WEAK  | Review this plan annually | The team | Update if needed |
     TRAP  Treating an annual exercise that a regulator or internal policy requires as the trigger itself,
           rather than as a floor layered under the condition-based trigger above it. -->

| Condition That Would Make This Plan Wrong | Owner Who Notices | What They Do About It |
|---|---|---|
| {{review_trigger_condition}} | {{review_trigger_owner}} | {{review_trigger_action}} |

**Annual exercise required by policy or regulation, if any (a floor under the conditions above, not a
substitute for them):** {{annual_exercise_floor_note}}
