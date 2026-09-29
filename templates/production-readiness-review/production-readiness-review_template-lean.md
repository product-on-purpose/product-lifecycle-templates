---
title: "{{review_title}}"
service_name: "{{service_name}}"
owner: "{{owner}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: production-readiness-review
size: lean
source_template: production-readiness-review
source_template_version: 0.1.0
---

<!--
LEAN PRODUCTION READINESS REVIEW. The load-bearing core: what this review covers, the criteria a service
must clear, the rule that keeps a not-applicable answer honest, the outcome and who signed it, and what
would make this checklist itself wrong. Five sections, because a small review program needs the readiness
discipline without a named reviewer roster, a stated cadence, or a documented lighter path. To add Reviewer
and Authority, Review Cadence, and When This Does Not Apply, see
production-readiness-review_template-full.md; ADD sections, never rename or reorder the ones below, because
the full variant is a strict superset of this one.

THIS CHECKLIST IS STANDING; A COMPLETED REVIEW OF ONE SERVICE IS NOT. The instrument you are filling in
belongs to a reviewing team and is reused across services and across handoffs: "the Production Readiness
Review can be started at any point of the service lifecycle, but the stages at which SRE engagement is
applied have expanded over time." A single completed run of this document against one service, at one
handoff, is the record of applying the standing questionnaire, not a second kind of document. Update this
file when the questionnaire itself needs to change, not every time a service is reviewed. See
production-readiness-review_companion.md section 1 and section 4.

THIS IS A SERVICE'S STANDING READINESS TO BE RUN, NOT ONE LAUNCH'S READINESS TO SHIP. A production readiness
review and a launch coordination checklist share engineering-scoped roots, but they ask different questions:
"a PRR is considered a prerequisite for an SRE team to accept responsibility for managing the production
aspects of a service," evaluated against a service that already exists, while a launch checklist evaluates
one specific launch before it ships. In practice a service handoff and a launch can land on the same
calendar date, and some adopters run this review at every release; that does not collapse the two documents
into one, because what each one asks about still differs. See production-readiness-review_companion.md
section 6 and section 8.

THE NAME COLLIDES WITH AN UNRELATED HARDWARE-MANUFACTURING REVIEW. NASA and the US Department of Defense
both publish a "Production Readiness Review" that determines whether a manufacturer is ready to produce
hardware at scale, judged by production planning and supplier management rather than service reliability.
It shares only the name with this document and no lineage. See production-readiness-review_companion.md
section 2 and section 8.

THE READINESS CRITERIA DOMAINS ARE BUILT ACROSS SEVERAL SOURCES, NOT FROM ANY ONE SOURCE'S TAXONOMY. Google's
own account of this review's evaluation domains ("System architecture and interservice dependencies,"
"Instrumentation, metrics, and monitoring," "Emergency response," "Capacity planning," "Change management,"
"Performance: availability, latency, and efficiency") is licensed CC BY-NC-ND 4.0 with no derivatives, so this
template does not adapt that list as its own. The evidence-and-status mechanics below are adapted, with
attribution, from Mercari's MIT-licensed Production Readiness Check instead. See
production-readiness-review_companion.md section 3 (Anatomy > Readiness Criteria) and section 5.

WHAT THIS REVIEW IS, AND IS NOT
It is the standing questionnaire a reviewing team consults before, or during, an ownership handoff or a
periodic re-check of a service already running. It is NOT a launch coordination checklist (that reviews one
launch, not a service's standing ability to be run). It is NOT a definition of done ("a formal description
of the state of the Increment," a per-work-item bar the team judges itself against every sprint, not a
service-level, often externally reviewed instrument). It is NOT a change advisory board ("delivers support to
a change-management team by advising on requested changes," a portfolio-wide standing panel reviewing many
changes, not one service's readiness). It checks that a runbook exists ("Link to the troubleshooting
runbooks."; "It has OnCall playbooks.") without producing one. And it is NOT the hardware-manufacturing
Production Readiness Review named above, which shares nothing but the name. See
production-readiness-review_companion.md section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   production-readiness-review_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the
   TRAP to avoid. For tables, PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Fill Scope and Trigger and Readiness Criteria first; the
   rest depends on knowing what this review covers and what it found.
3. If a section, or one row inside a table, does not apply, write "N/A" and the reason beside it rather than
   leaving it blank or deleting the section. See Not-Applicable Rule below; this is the same rule applied to
   the whole document.
4. Before you ship it: self-grade against production-readiness-review_guide.md, then DELETE every HTML
   comment. They are guidance, not content.
-->

# {{review_title}}

## Scope and Trigger

<!-- WHAT  What "production" means for this review, which service or services it covers, what event starts
           a review, and what this review deliberately does not cover, with a pointer to where that is
           reviewed instead.
     WHY   No source read for this bundle agrees on what starts a review. Google's own account is a request:
           "When a development team requests that SRE take over production management of a service, SRE
           gauges both the importance of the service and the availability of SRE teams." Mercari's is a hard
           gate before traffic: "This documentation describes the steps to do Production Readiness Check
           (PRC), which is required for all services before receiving real production traffic." AWS's
           Operational Readiness Review ties the trigger to a proposed change rather than a running service
           at all: "the ORR Lifecycle for New Service and Iterations is initiated when a new service, new
           feature, or architecture change is proposed." Because no trigger read here is universal, this
           section asks you to name your own rather than adopting any one source's. This is also where a
           reader who has met "Production Readiness Review" as a hardware-manufacturing milestone at NASA or
           the Department of Defense is told plainly that this is a different document with the same name.
           This section absorbs the exclusion a security review needs: "Security must have its own,
           in-depth, review." Deep dive: production-readiness-review_companion.md section 3 (Anatomy > Scope
           and Trigger) and section 6.
     ASK   What does "production" mean for this service, in this context? Which service or services does
           this review cover? What event starts a review here: an ownership handoff request, a hard gate
           before traffic, a maturity-level promotion, a proposed architecture change, or something else? If
           your real trigger does not match any of these, write your own. What does this review deliberately
           not cover, and where is that reviewed instead?
     GOOD  "Production means serving live customer traffic on checkout-service. This review covers
           checkout-service only, not its upstream inventory dependency. Trigger: the Payments team has asked
           the SRE guild to take over standing production ownership. This review does not cover a dedicated
           security assessment; that is tracked separately by the security team's own review."
     WEAK  "This is our production readiness review for the service." (states no trigger, no scope boundary,
           and no exclusion; a reader cannot tell what this review actually covers or when it applies)
     TRAP  Assuming this document is the hardware-manufacturing Production Readiness Review used in aerospace
           or defense contexts, which shares nothing but the name; or treating a per-release trigger as
           interchangeable with a standing-service trigger without saying which one this review actually
           uses. -->

{{production_scope_and_trigger}}

**This review does not cover:** {{out_of_scope_note}}

## Readiness Criteria

<!-- WHAT  The load-bearing section: criteria grouped by domain, each carrying the evidence that answers it,
           an owner, and its current status.
     WHY   No single source's domain list is copied wholesale; the starting set is drawn across sources.
           Monitoring appears across several checklists; capacity and performance across several more;
           architecture and dependencies, change management, and emergency response are named directly in
           Google's own account of what a PRR evaluates: "System architecture and interservice
           dependencies," "Instrumentation, metrics, and monitoring," "Emergency response," "Capacity
           planning," "Change management," "Performance: availability, latency, and efficiency." AWS groups
           its own questions under "Architecture," "Release quality," and "Event management." The
           evidence-and-status mechanics are adapted, with attribution, from Mercari's MIT-licensed
           checklist: "If it is satisfied, check the item in the list and provide evidence (e.g. links to
           tickets, screenshots, documents, test results, ...) showing that it is satisfied. If evidence is
           not provided the review process will take much longer." A full-size review may add whether a
           criterion blocks outright and the service tier that requires it; this variant keeps the smaller
           question, whether the evidence actually answers it. Deep dive:
           production-readiness-review_companion.md section 3 (Anatomy > Readiness Criteria) and section 5.
     ASK   For each criterion: what domain does it belong to? What evidence would actually satisfy it, not a
           bare confirmation? Who owns producing that evidence? What is its current status, honestly
           recorded? A worry-elicitation question worth asking directly: "What are you worried about?"
     PRIORITY  Order domains the way a reader would actually need them (dependencies and architecture before
           monitoring and rollout, for instance).
     ROW HINT  A good row's evidence field names something a second person could go check themselves, not a
           bare "done." A weak row asserts a status with no evidence anyone else could verify.
     GOOD  | Monitoring and alerting | Does checkout-service have dashboards and alerts covering its golden
           signals? | Dashboard linked; alert routes to the on-call rotation and was tested against a
           synthetic failure last week | Payments on-call lead | Satisfied |
     WEAK  | Monitoring | Is it monitored? | Yes | Team | Done | (no evidence anyone else could check, and
           "done" is not an actual status)
     TRAP  Copying one source's domain list wholesale instead of using the set that matches what has actually
           gone wrong for your own service, and writing a bare confirmation where the evidence field belongs. -->

| Domain | Criterion | Evidence | Owner | Status |
|---|---|---|---|---|
| {{criteria_domain}} | {{criterion}} | {{criterion_evidence}} | {{criterion_owner}} | {{criterion_status}} |

## Not-Applicable Rule

<!-- WHAT  An item marked not applicable in Readiness Criteria always carries a written reason beside it,
           never a bare mark.
     WHY   This rule is sourced three times independently, in near-identical words. GitLab: "Leave all
           non-applicable items intact and add 'N/A' or reasons for why in place of the response." Mercari,
           MIT-licensed and adaptable with attribution: "If a specific item is not applicable to your service
           check the item and explain, as evidence, why it's not applicable." Federal Student Aid states the
           same rule as a prohibition: "No item in the PRR should only be marked "N/A" or "Not Applicable;"
           instead an explanation should be provided as to why a particular item does not apply." Deep dive:
           production-readiness-review_companion.md section 3 (Anatomy > Not-Applicable Rule).
     ASK   Does every criterion marked "Not Applicable" in the Readiness Criteria table carry a reason beside
           it in this document, not only in someone's memory? If a reason is missing, is that item actually
           not applicable, or was it skipped?
     PRIORITY  List the items in the order they appear in Readiness Criteria, so each reason sits
           beside its row.
     ROW HINT  A good row names the criterion and a reason a later reader could check, such as where
           the thing it covers is reviewed instead. A weak row repeats "N/A" in the reason column.
     GOOD  "Data recovery: marked Not Applicable in Readiness Criteria. Reason: checkout-service holds no
           persistent data of its own; all state lives in the shared payments ledger, reviewed under that
           service's own PRR."
     WEAK  "Data recovery: N/A" (no reason; a later reader cannot tell this apart from an item nobody
           checked)
     TRAP  Leaving a "Not Applicable" mark with nothing beside it. An unexplained N/A and a skipped item are
           indistinguishable to a later reader, which is exactly what this rule exists to prevent. -->

{{not_applicable_policy}}

**Criteria marked not applicable in this review, and why:**

| Criterion Marked Not Applicable | Reason |
|---|---|
| {{na_criterion}} | {{na_reason}} |

## Outcome and Sign-off

<!-- WHAT  The outcome of the review, each finding not fully met, and who signed.
     WHY   No outcome vocabulary read for this bundle is an industry standard. One practitioner's own
           four-state model says so directly: "These states are a recommended governance model, not a
           Google, AWS, or Kubernetes platform behavior." This template borrows three of that model's states,
           "Ready with conditions" and "Not ready," alongside an unconditional Ready state, and drops the
           model's fourth state, which concerns a launch whose scope or date moved rather than a service's
           own readiness. Each finding not met carries its own record: "For each finding, capture: severity
           and customer or business consequence; exact affected scope; evidence that produced the finding;
           remediation and named owner; due date and verification method; whether it blocks launch;
           exception record, if the risk is accepted temporarily." A condition accepted at sign-off is
           listed, owned, and dated rather than implied: "When FSA Management signs-off on the PRR, they are
           approving implementation even with the issues listed"; "When gaps are identified, teams either
           address them before launch or document an exception with an expiration date and a plan to
           remediate." Deep dive: production-readiness-review_companion.md section 3 (Anatomy > Outcome and
           Sign-off) and section 6.
     ASK   What is the outcome: Ready, Ready with conditions, or Not ready? For every finding not fully met,
           what is its severity, its owner, and its due date? Where a condition is accepted rather than
           blocking, is that recorded with an owner and a date, or only implied? Who signed, and in what
           role?
     PRIORITY  List findings that block the outcome outright before ones accepted as a time-bounded
           exception, so a reader sees the hard stops first.
     ROW HINT  A good row's owner and due date name someone who could actually be asked for a status update
           later. A weak row states severity with no owner and no date, which nobody can be held to.
     GOOD  | Missing load test against peak checkout traffic | High | Payments on-call lead | Two weeks from
           sign-off | Accepted as a time-bounded exception, tracked separately |
     WEAK  | Some gaps | Medium | | | (no owner, no date, nothing anyone could be held to) |
     TRAP  Reading an empty findings table as an all-clear. If no risks were identified, write "No Risks
           Identified" in the first row; there are always unknown risks. -->

**Outcome:** {{outcome_state}}

| Finding | Severity | Owner | Due Date | Exception (if any) |
|---|---|---|---|---|
| {{finding_description}} | {{finding_severity}} | {{finding_owner}} | {{finding_due_date}} | {{finding_exception}} |

| Signatory | Role | Date |
|---|---|---|
| {{signatory_name}} | {{signatory_role}} | {{signatory_date}} |

## Review Trigger

<!-- WHAT  The event that would make this checklist itself wrong, and the named person or role expected to
           notice it. Not a calendar date alone.
     WHY   Unlike this family's first two members, a condition for revising this checklist is genuinely
           sourced here rather than supplied by this library alone. AWS names three sources for a new
           question: "Real incidents that you've had in the past," "Near-misses that you've had in the
           past," and "The failure modes that haven't occurred, but that you're concerned about," and ties
           incident review directly to the checklist through a named question: "Would any ORR recommendations
           have reduced or avoided the impact of this event?" That question is curated by a standing role,
           the Ops Champion, who "challenges the team on their answers to the checklist, provides
           context on the adoption and prioritization of best practices, and ends up influencing everything
           from workload architecture to operational culture in the team." One vendor's own gate model
           tempers how loosely that trigger should be read: "Do not add a question merely because something
           once went wrong. State the failure it prevents, the evidence that answers it, and the launch
           types for which it applies." Deep dive: production-readiness-review_companion.md section 3
           (Anatomy > Review Trigger) and section 6.
     ASK   What specific kind of event, an incident, a near miss, or a named worry that turned out to be
           real, would make you revise this checklist? Who owns noticing it? When an incident does prompt a
           look at this checklist, which criterion should have caught it, and why did it not, before deciding
           the fix is a new row rather than something else entirely?
     PRIORITY  An event with no named owner is not a trigger, it is a hope; do not list one without the
           other.
     ROW HINT  A good row names a specific event, a named owner, and what they do about it: investigate which
           existing criterion should have caught it before deciding whether the fix is a new row. A weak row
           names only a calendar date.
     GOOD  | checkout-service had an incident that Readiness Criteria's monitoring domain should have caught
           earlier | SRE guild lead | Investigate which specific criterion should have caught it before
           adding a new one |
     WEAK  | Review this checklist annually | Team | Update if needed |
     TRAP  Adding a new criterion for every incident without first asking which existing one should have
           caught it. That growth is exactly what this rule exists to prevent. -->

| Event That Would Make This Wrong | Owner Who Notices | What They Do About It |
|---|---|---|
| {{review_event}} | {{review_owner}} | {{review_action}} |
