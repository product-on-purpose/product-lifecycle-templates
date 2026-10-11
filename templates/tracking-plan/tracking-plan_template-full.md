---
title: "{{product_name}} Tracking Plan"
product: "{{product_name}}"
plan_owner: "{{plan_owner}}"
data_steward: "{{data_steward}}"
sources_and_destinations: "{{sources_and_destinations}}"
plan_version: "{{plan_version}}"
last_reviewed: "{{date}}"
status: "{{status}}"
doc_type: tracking-plan
size: full
source_template: tracking-plan
source_template_version: 0.1.0
---

<!--
FULL TRACKING PLAN. Everything in the lean variant, plus a place to flag a sensitive event or property with
its retention and its handling before storage, and a section for how a change to the standing plan is
proposed, approved, and recorded, with removal run as its own procedure rather than a quiet status flip.
Use it when several teams change this plan, when it holds personal or sensitive data, or when someone will
later ask what changed and who approved it, following Amplitude's own named approval roles, Snowplow's
named owner and audit trail, and Mozilla's formal data-collection review.

This is a STRICT SUPERSET of tracking-plan_template-lean.md: every lean section appears here in the same
relative order, and the first four are identical in name, position and tables. If you are growing from lean,
insert Privacy, Sensitivity and Retention before Review and Ownership, and append Change Process and Version
History last.

WHAT A TRACKING PLAN IS. Amplitude puts the job in one sentence: "A tracking plan defines every event and
property you collect, why you collect each one, and which source emits it." Countly adds what the document
does across teams: "It translates product questions into an implementation contract for product,
engineering, analytics, privacy, and marketing teams." The sources that define the type are mostly vendors,
and most of them sell the tool the plan is later enforced in, so this template treats their shared
definition as the convergent core and does not present any one vendor's case for its own product as a
finding. See tracking-plan_companion.md section 1.

NO SOURCE READ FOR THIS BUNDLE MEASURED WHETHER KEEPING ONE IMPROVES DATA QUALITY OR DECISIONS. What exists
is practitioner testimony about what goes wrong without one: a named failure taxonomy and one
practitioner's own claim that an ungoverned plan is "a document that's wrong within 60 days of shipping."
This template's reason to exist rests on that testimony and on the failure modes it names, not on a
measurement. See tracking-plan_companion.md section 1 and section 7.

IT IS NOT A SINGLE FEATURE'S INSTRUMENTATION SLICE, A DATA DICTIONARY, A MEASUREMENT PLAN, OR THE ENFORCED
SCHEMA IN A TOOL. A single feature's own events are first proposed in that feature's own PRD, in its
"Analytics and instrumentation" section; this plan is what every feature's slice merges into over the
product's life, a reading this library states as its own position rather than as any source's claim. A
data dictionary "documents what the data means and how it is structured once implemented," the opposite
tense from this plan's forward-looking "what you intend to track." A measurement plan contains this plan
but also covers business objectives, KPI definitions, and reporting logic. And several vendors keep a live
copy of this plan inside their own product and check incoming data against it; this template is the
document, not that enforced copy. See tracking-plan_companion.md section 1, section 3 (Purpose and Boundary), and section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP; the
   four table sections also carry PRIORITY and ROW HINT.
2. Replace each {{placeholder}}. The Event and Property Catalog is the heart; no event is listed without a
   named owner and a stated reason, and the naming convention, the status vocabulary, and the catalog's
   columns stay consistent with each other.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it. The Privacy,
   Sensitivity and Retention section in particular may be "N/A, no event here carries personal or sensitive
   data yet" for a small plan, rather than being deleted outright.
4. This document is never finished, but before you share it: self-grade against tracking-plan_guide.md,
   then DELETE every HTML comment. They are guidance, not content.
-->

# {{product_name}} Tracking Plan

## Purpose and Boundary

<!-- WHAT  A short statement of what this plan covers, product-wide, and what does not belong in it.
     WHY   The name sits beside four neighbors a reader will meet under similar words, and the first job
           of this section is to rule them out before the catalog starts. Wizbrand's own account draws the
           plan forward-looking: "A tracking plan describes what you intend to track (events, triggers,
           parameters) and why," against the opposite tense for a data dictionary, "A Data Dictionary
           documents what the data means and how it is structured once implemented." Against a broader
           measurement plan, the same source states containment directly: "the measurement plan explains
           why you track; the tracking plan explains how." This library reads this plan as what every
           feature's own PRD instrumentation slice merges into over the product's life, and reads the KPI
           dashboard's own metric formula as a separate concern this plan does not lock, each stated here
           as this library's own position rather than any source's claim. Deep dive:
           tracking-plan_companion.md section 3 (Purpose and Boundary) and section 8.
     ASK   What product, or which part of it, does this plan cover? What four neighbors does it rule out,
           by name: a single feature's own instrumentation slice, a data dictionary, a broader measurement
           plan, and a tool's own enforced schema? Where does a single feature's own instrumentation
           request go before it merges into this standing plan?
     GOOD  "This plan covers every event Shiftwell's worker app and manager console record. A new
           feature's events are proposed in that feature's own PRD and land here when it ships. What the
           warehouse tables mean once these events reach them is the data dictionary's job. The schema
           Shiftwell's analytics tool enforces is generated from this plan and is never edited ahead of
           it."
     WEAK  "This plan tracks what we track." (names no neighbor it rules out, and a reader cannot tell a
           single feature's own slice from the standing plan)
     TRAP  Treating this plan as the place to write a single feature's launch metrics, or trying to lock a
           KPI's own formula here instead of in the KPI dashboard's own Metric Definitions section. -->

{{purpose_and_boundary}}

## Naming Conventions

<!-- WHAT  A short statement of the convention this catalog's event names follow: tense, case, and whether
           the same name holds up across every platform this product ships on.
     WHY   Countly names the obligation generally: "A strong plan defines naming conventions," among other fields. The
           object-then-past-tense-action form is attributed to the practitioners who state it, not to any
           vendor's own specification: a consultancy's engineering handbook reports Segment's own
           object-action framework and states the rule, "Action: defines how users can interact with the
           objects in the application. An action must be in the past." An independent newsletter states
           the same preference in its own voice, "I recommend using the object+action framework because
           it's easy to visualise what object your user is interacting with and what action has taken
           place," and explicitly declines to settle casing, "Choose one case and stick with it," while the
           same engineering handbook requires snake_case outright. One source names the exact failure a
           plan without a cross-platform answer invites: "the screen names differ per platform, which
           makes it hard to actually use the data." This section asks for a convention and picks none of
           these forms for you. Deep dive: tracking-plan_companion.md section 3 (Naming Conventions) and
           section 6, item 3.
     ASK   What tense do event names follow? What capitalization and casing? Does the same event name hold
           up across every platform this product ships on, and if not, what is the fallback when a
           platform's own automatic tracking would otherwise diverge?
     GOOD  "Shiftwell event names are object-then-past-tense-action, snake_case: shift_claimed,
           shift_released, worker_onboarded. The same name is used on iOS, Android, and web; where a
           platform's own automatic screen-tracking would otherwise produce a different name for the same
           action, that automatic event is excluded from this catalog and the matching manual event is
           used instead."
     WEAK  "Name events clearly." (no tense, no case, and no answer for what happens when two platforms
           disagree)
     TRAP  Naming a convention without saying what happens when a platform's own automatic tracking, such
           as a default screen-view event, would otherwise produce a different name for the same user
           action. -->

{{naming_convention}}

## Event and Property Catalog

<!-- WHAT  The load-bearing table, one row per event: its name, when it fires, why it is collected, its
           properties with type and allowed values, where it comes from and where it goes, its owner, and
           its status.
     WHY   Amplitude's own one-sentence definition names every column this table carries: "A tracking plan
           defines every event and property you collect, why you collect each one, and which source emits
           it." Countly's field list adds triggering conditions and sensitivity to the same spine. When it
           fires is a worked example's own LOCATION column, "the location and time at which the event is
           being tracked." Why it is collected is the same worked example's WHY column, "a short
           description of the business purpose that justifies tracking the event," and Avo's own
           instruction to "Summarize the reason for tracking each event and property." Properties, with
           type and allowed values, follow Avo's "Property value types" and Twilio Segment's "Permitted
           Values" fields. The owner column is convergent, not single-sourced: Amplitude's blog ties the
           source field directly to an owner, "the person responsible for the implementation of that
           event," and Amplitude's own event-taxonomy page asks for "central documentation listing every
           event, property, data type, and owner." Status is likewise convergent: Amplitude's taxonomy page
           asks teams to "Track all taxonomy changes with version labels like 'proposed,' 'active,'
           'deprecated,' and 'removed.'" An event's own owner is a separate question from the plan's own
           owner and from the approval path; this template keeps the three apart rather than collapsing
           them into one column. Deep dive: tracking-plan_companion.md section 3 (Event and Property
           Catalog) and section 6, item 5.
     ASK   For each event: what is its name, following the convention above? When does it fire? What
           business question does it answer? What properties does it carry, with type and allowed values?
           What source emits it, and what destination receives it? Who is its owner? What is its current
           status?
     PRIORITY  No event ships without a named owner and a one-sentence reason. Status uses a stated
           vocabulary, proposed, active, deprecated, and removed, or the team's own list named once rather
           than invented per row.
     ROW HINT  A good row answers "why it is collected" in one sentence a non-analyst could repeat back. A
           weak row names the event and leaves the reason blank because the name alone looks
           self-explanatory.
     GOOD  | shift_claimed | A worker taps Claim on an open shift | Measures how fast open shifts fill,
           feeding the fill-rate metric | shift_id (string), worker_id (string), claimed_at (datetime),
           source_channel (enum: push, email, in_app) | Worker app -> event pipeline -> warehouse | Jordan
           Ruiz | active |
     WEAK  | shift_claimed | | | | | | active |
     TRAP  Treating the event name as self-explanatory and leaving the "why it is collected" cell blank; a
           plan nobody can re-justify is the owner-departure failure mode this bundle's research names. -->

**Status vocabulary used below:** {{status_vocabulary}}

| Event | Fires when | Why (business question) | Properties | Source -> Destination | Owner | Status |
|---|---|---|---|---|---|---|
| {{event_name}} | {{event_trigger}} | {{event_reason}} | {{event_properties}} | {{event_source_destination}} | {{event_owner}} | {{event_status}} |

## User and Account Properties

<!-- WHAT  A table of the traits kept about a user or an account, apart from any event.
     WHY   Five independent sources keep this list separate from the event catalog rather than folding it
           in. Twilio Segment defines traits by what they are not: events, but persistent facts, "Objects
           persist over time, so traits can change over time." Amplitude's documentation splits the idea in
           two: "User properties capture traits about the user", and, as a parallel field for a group,
           "Group properties make it easy to associate a user with a particular account". Mixpanel's own
           best-practice checklist names "user profile properties" alongside event properties as a distinct
           line item, and mParticle's platform guide groups "an event, user attributes, or user identities"
           as the three kinds of thing a single data point can be. Deep dive: tracking-plan_companion.md
           section 3 (User and Account Properties).
     ASK   What traits are kept about a user? About an account or group? What is each trait's type and
           expected values? Where is each one set, or updated?
     PRIORITY  A trait is a persistent fact, not a property of one event; if it changes independently of
           any single action, it belongs here, not in the catalog above.
     ROW HINT  A good trait row names where the value is set, such as a signup form or an admin console,
           so a reader can tell a fact kept about a person from an event that merely mentions them. A weak
           row leaves the subject (user, or account) and the source blank.
     GOOD  | plan_tier | user | string: free, pro, team | Set at signup in the billing service, updated on
           upgrade or downgrade |
     WEAK  | plan_tier | | string | |
     TRAP  Folding a trait into the event catalog as though it were a property of one event, when it is
           really a fact that persists across many events and many sessions. -->

| Trait | Subject (user or account) | Type and allowed values | Source (where it is set) |
|---|---|---|---|
| {{trait_name}} | {{trait_subject}} | {{trait_type_values}} | {{trait_source}} |

## Privacy, Sensitivity and Retention

<!-- WHAT  A place to flag an event or property as sensitive, state how long it is kept, and name what
           happens to it before it reaches storage.
     WHY   The sourcing here is thinner and more varied than the catalog's core columns, so this section
           presents the shapes different sources use rather than choosing one; it is full-only because a
           lean plan for a small event set may carry nothing sensitive yet. Countly lists "sensitivity,
           retention, and validation" among what a strong plan carries. One practitioner source makes the
           flag itself a column with a defined downstream effect, "pii_flag: true or false; routes the
           event through masking or exclusion pipelines." A data-governance guide frames the same need at
           the policy level, "Your policies must include strict controls to prevent the accidental
           collection of Personally Identifiable Information (PII)." Mozilla's own telemetry process
           attaches sensitivity and an expiry directly to each metric's own definition, "data_sensitivity:"
           and, separately, "expires:," and its data-collection policy ties consent to how sensitive the
           category is rather than to a single yes-or-no answer. No regulator was read for this bundle, so
           this section gives no legal advice on consent or retention. Deep dive:
           tracking-plan_companion.md section 3 (Privacy, Sensitivity and Retention) and section 9.
     ASK   Which events or properties might carry personal or sensitive data? What flag marks them? How
           long is each one kept? What happens to it before storage, such as masking, hashing, or
           exclusion? Has anyone with legal authority over this team's data confirmed the retention and
           consent rules named here?
     PRIORITY  Name the specific property that is sensitive, not only the event that carries it. A
           retention period or a consent rule stated here is this team's own placeholder until legal
           confirms it, never presented as settled.
     ROW HINT  A good row names the exact property, the flag, the duration, and the handling step in the
           same row. A weak row says "handle carefully" with no flag, no duration, and no step.
     GOOD  | worker_onboarded | home_address property | pii_flag: true | 90 days, then purged | Masked
           before reaching the warehouse; legal has not yet confirmed this duration |
     WEAK  | worker_onboarded | | | | |
     TRAP  Writing a retention duration or a consent rule as though this section had settled it. No
           regulator was read for this bundle, so this section names shapes only, and any figure entered
           here is this team's own choice pending legal confirmation. -->

| Event or property | What is sensitive | Flag | Retention | Handling before storage |
|---|---|---|---|---|
| {{privacy_item}} | {{sensitivity_detail}} | {{sensitivity_flag}} | {{retention_period}} | {{handling_before_storage}} |

## Review and Ownership

<!-- WHAT  The plan's own named owner, apart from any event's owner, how often the whole plan is reviewed,
           and what else, beyond the calendar, should trigger an earlier review.
     WHY   Snowplow states the plan-level role directly: "An explicit owner; that is responsible for
           maintaining and updating the data over time". How often the whole plan is reviewed is contested
           outright: one practitioner states a fixed ninety-day cadence and credits it to a named third
           party, a monitoring vendor rejects any fixed interval, and Countly instead ties review to an
           event, "It should be versioned and reviewed whenever the product or measurement strategy
           changes." No interval is a convention here; this section asks the author to name one and to say
           plainly whether it is this team's own choice or a borrowed figure. Deep dive:
           tracking-plan_companion.md section 3 (Review and Ownership) and section 6, item 2.
     ASK   Who is the plan's own owner, apart from any event's owner? How often is the whole plan reviewed?
           What, besides the calendar, should trigger an earlier review? Is the stated interval this team's
           own choice, or a figure borrowed from somewhere else?
     GOOD  "Owned by Jordan Ruiz, Analytics Lead, apart from any individual event's own owner. Reviewed
           every ninety days; this interval is this team's own choice, not a sourced norm. A major
           navigation redesign also triggers an off-cycle review."
     WEAK  "Reviewed periodically." (no owner named, no interval, and nothing a reader could check the plan
           against)
     TRAP  Confusing the plan's own owner with an individual event's owner, or borrowing a cadence figure
           and presenting it as an industry norm rather than naming it as a borrowed figure or a team's own
           choice. -->

**Plan owner (apart from any event's owner):** {{plan_owner}}

**Review interval:** {{review_interval}}

**Other review triggers:** {{review_triggers}}

## Change Process and Version History

<!-- WHAT  How a change to the standing plan is proposed, reviewed, and recorded, and how an event is
           removed as a defined procedure rather than a quiet status flip, plus the running record of what
           changed, when, and who approved it.
     WHY   A plan that several teams change, that carries personal data, or that someone will later ask
           "what changed and who approved it" needs this section; a lean plan for a small, stable event
           set may not yet. Avo's branched workflow is the fullest sourced version of the proposal
           mechanism: "A branch allows you to draft changes to the tracking plan in isolation, without
           impacting the main branch, which contains the single source of truth of what's currently being
           tracked," reviewed before it ships, and merged alongside its matching code change, "As soon as
           the git branch is merged into the git main branch, they merge their Avo branch in the Avo main
           branch." A distinct, independently sourced approval path names three roles: Amplitude's
           event-taxonomy page states, "Event requesters propose new events with clear use cases," "Data
           stewards review naming and check for duplicates," and "Domain owners approve events within
           their product areas," and Mozilla's data-collection policy names an overlapping pair for data
           requests specifically, a "Data requester" and a "Data steward" who "ensures the data collection
           process is followed." The record of a change is Snowplow's own stated element, "Change history;
           a complete audit log of the changes that have been made to the tracking plan," matched by one
           practitioner's instruction to "Document what changed, when, why, and who approved it." Removal
           is sourced as a defined procedure, not a status flip: GitLab's event-lifecycle guide gives it
           explicit steps, including updating "the event definition file to set the status field to
           removed." A validation gate before an event ships is sourced independently twice: GitLab's own
           handbook has an engineer "Verify test events match properties defined in the Issue," and Mozilla
           requires that "Data reviews are needed on all patches that add new telemetry or modify existing
           telemetry." Deep dive: tracking-plan_companion.md section 3 (Change Process and Version
           History).
     ASK   How does someone propose a change to this plan? Who reviews and approves it, by role? How is an
           event formally removed, as a procedure rather than a status flip? What validation happens before
           a new or changed event ships? What is the running record of what changed, when, why, and who
           approved it?
     PRIORITY  Removal is its own procedure, never a silent status flip. Every row in the version history
           names the event affected and the person who approved the change, not only that "a change was
           made."
     ROW HINT  A good version-history row names the event, the status transition it underwent (for
           example proposed to active, or active to deprecated to removed), who approved it, and when. A
           weak row says "updated" with no event named and no approver.
     GOOD  "Propose a change on its own branch, isolated from the standing plan; a data steward reviews
           naming and checks for duplicates; a domain owner approves it within their own product area; the
           change merges into the plan alongside its matching code change." Version history row: | v1.3 |
           2026-03-02 | shift_released added (proposed -> active) | Reviewed by the data steward, approved
           by the domain owner for Scheduling |
     WEAK  Version history row: | v1.3 | | updated some events | |
     TRAP  Flipping an event's status straight to removed without running the removal procedure, or
           recording only that "a change was made" without naming which event, who approved it, and
           when. -->

{{change_process}}

| Version | Date | What changed | Approved by |
|---|---|---|---|
| {{version_number}} | {{version_date}} | {{version_change_summary}} | {{version_approved_by}} |
