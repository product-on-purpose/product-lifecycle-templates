---
title: "{{review_title}}"
service_name: "{{service_name}}"
owner: "{{owner}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: production-readiness-review
size: full
source_template: production-readiness-review
source_template_version: 0.1.0
---

<!--
FULL PRODUCTION READINESS REVIEW. Everything the lean variant carries, plus Reviewer and Authority, Review
Cadence, and When This Does Not Apply. Use it once more than one plausible reviewer exists, once a service
is expected to be reviewed more than once, or once your review program covers enough services that treating
all of them identically would itself be a failure mode. To go back to the load-bearing core, see
production-readiness-review_template-lean.md.

THIS VARIANT IS A STRICT SUPERSET OF THE LEAN ONE. The five lean sections, Scope and Trigger, Readiness
Criteria, Not-Applicable Rule, Outcome and Sign-off, and Review Trigger, appear here in the same order with
the same headings and placeholders; full only adds Reviewer and Authority, Review Cadence, and When This Does
Not Apply. If you started lean and are growing into this, add the new sections; do not reorder or rename
anything you already filled in.

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

## Reviewer and Authority

<!-- WHAT  Who conducts the review, who the reviewed team is, and who is authorized to say a finding blocks.
     WHY   Two sourced positions disagree on who should hold the checklist at all. Pedro Alves argues for an
           outside reviewer: "To maximise the potential to identify risks, and remove biases, reviewers
           should be external to the team. Some degree of familiarity with the domain can be helpful,
           though," naming "two reviewers tends to be the sweet spot." Laura Nolan argues close to the
           opposite: "This is where I've very strongly argued that the team themselves should be the ones
           who define what their criteria are for production readiness, because they know that software
           best." Mercari sides with Nolan's position in practice: "Verify if each item is satisfied or not
           by your own team." Who decides a blocking finding is equally unsettled: AWS escalates by
           criticality, "Any high-criticality findings are escalated to leadership as input to a go or
           no-go launch decision"; Azure names a single accountable role instead, "The directly responsible
           individual (DRI) should make the final decisions with input from key stakeholders and technical
           decision-makers"; and Federal Student Aid raises the required signatory with the release's own
           risk, "based on the operational risk factors for the release, the CTO Enterprise Architecture and
           IT Planning Branch will indicate if additional sign-off by FSA Senior Management is required."
           Alves leaves the choice to the reviewed team itself: "It is generally up to the development team
           to decide whether and how to follow up on those risks." Deep dive:
           production-readiness-review_companion.md section 3 (Anatomy > Reviewer and Authority) and
           section 6.
     ASK   Who conducts this review, named by role: someone outside the reviewed team, the reviewed team
           itself, or both? Who is the reviewed team? Who is authorized to say a finding blocks, and does
           that authority rise with the risk of what is being reviewed? Who does a blocking finding escalate
           to when the reviewer and the reviewed team disagree?
     PRIORITY  List the decision authority first, then the reviewer or reviewers who feed evidence to that
           decision, so a reader sees immediately who can say no.
     ROW HINT  A good row names a role, not only a person, and states what that role is accountable for. A
           weak row is a distribution list, a channel, or "the team," with no one actually accountable for
           the decision.
     GOOD  | Decision authority | SRE guild lead | Can accept a finding as blocking; the only role
           authorized to sign the outcome as "Not ready" |
     WEAK  | Reviewer | Whoever is free | (no accountable role, and no way to tell who could say no) |
     TRAP  A review with no one authorized to say a finding blocks, so every finding is negotiable by
           default. Naming a reviewer with no way to escalate a disagreement is the same gap from the other
           side. -->

**Blocking findings escalate to:** {{escalation_authority}}

| Role | Named Holder | Responsibility |
|---|---|---|
| {{reviewer_role}} | {{reviewer_holder}} | {{reviewer_responsibility}} |

## Readiness Criteria

<!-- WHAT  The load-bearing section: criteria grouped by domain, each carrying the evidence that answers it,
           an owner, its current status, and, in this variant, whether it blocks outright and the tier that
           requires it.
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
           not provided the review process will take much longer." Whether a criterion blocks outright is
           genuinely disputed: "not all issues are blockers to SRE takeover (there might be design or
           architectural changes that SREs recommend for service robustness that could take many months to
           implement)," and one vendor's own gate model separates severity into "Blocking ... Conditional ...
           Advisory ..." The tier that requires a criterion follows the same logic Mercari applies to its own
           service levels: "The main factor of choosing a Service Level is the expected SLO." Deep dive:
           production-readiness-review_companion.md section 3 (Anatomy > Readiness Criteria) and section 5.
     ASK   For each criterion: what domain does it belong to? What evidence would actually satisfy it, not a
           bare confirmation? Who owns producing that evidence? What is its current status, honestly
           recorded? Does missing it block the outcome outright, or only start a conversation? What tier of
           service actually requires it? A worry-elicitation question worth asking directly: "What are you
           worried about?"
     PRIORITY  Order domains the way a reader would actually need them (dependencies and architecture before
           monitoring and rollout, for instance), and within a domain, list criteria that would block the
           outcome outright before ones that would only start a conversation.
     ROW HINT  A good row's evidence field names something a second person could go check themselves, not a
           bare "done." A weak row asserts a status with no evidence anyone else could verify.
     GOOD  | Monitoring and alerting | Does checkout-service have dashboards and alerts covering its golden
           signals? | Dashboard linked; alert routes to the on-call rotation and was tested against a
           synthetic failure last week | Payments on-call lead | Satisfied | Blocking | All tiers |
     WEAK  | Monitoring | Is it monitored? | Yes | Team | Done | | |  (no evidence anyone else could check,
           no tier, and "done" is not an actual status)
     TRAP  Copying one source's domain list wholesale instead of using the set that matches what has actually
           gone wrong for your own service, and writing a bare confirmation where the evidence field belongs. -->

| Domain | Criterion | Evidence | Owner | Status | Blocks? | Tier |
|---|---|---|---|---|---|---|
| {{criteria_domain}} | {{criterion}} | {{criterion_evidence}} | {{criterion_owner}} | {{criterion_status}} | {{criterion_blocks}} | {{criterion_tier}} |

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

## Review Cadence

<!-- WHAT  Whether this review repeats for a service that has already passed once, on what schedule, and
           why.
     WHY   Four camps disagree, and none read for this bundle is universal. One-time: Google's own SRE team
           "assumes its production responsibilities" once "sufficient improvements are made," and Grafana's
           early practice reads "Once the issues have been fixed, the product has passed the PRR," though
           Grafana was reconsidering that design even as it wrote it down: "We're looking into a periodic
           and/or incremental PRR as part of our continuous product improvements." Event-driven plus a fixed
           annual floor: AWS requires that "In addition to the ORR performed through the SDLC process, at
           least annually, teams are expected to perform an ORR on their full service using a checklist
           tailored to that event. This helps verify that they stay up to date with new or updated best
           practices, and also that nothing has changed within their systems." Continuous, tied to every
           change: Azure gates release promotion through staged approvals ("it's important to establish
           release promotion as a formal change control protocol before going live. This process progresses
           proposed changes through various stages with quality gates"), and Cortex's own Scorecard model
           can "block deployment based on Scorecard scores" on every attempt. Staged across the whole
           lifecycle rather than fixed to one cadence: a personal ORR template states the design goal
           outright, "The key is making ORR a continuous exercise rather than a one-time checklist." Deep
           dive: production-readiness-review_companion.md section 3 (Anatomy > Review Cadence) and
           section 6.
     ASK   Which of the four positions does this review take: one-time, event-driven plus an annual floor,
           continuous at every change, or staged across the lifecycle? Why that one, given how this service
           actually changes? If your team has never revisited a passed review, is that absence itself worth
           naming?
     GOOD  "Event-driven plus an annual floor: checkout-service is re-reviewed whenever its payment
           processor changes, and at minimum once a year even if nothing else has changed, following AWS's
           practice above. Chosen because the service's compliance obligations shift with its processor."
     WEAK  "We'll revisit this if it seems necessary." (names no camp, no schedule, and no reason; a reader
           cannot tell whether this service has ever actually been re-reviewed)
     TRAP  Defaulting to silence on cadence rather than taking a position. A one-time review is defensible
           for a first handoff; an unexamined one-time review years later is a gap worth naming, not a
           closed question. -->

{{review_cadence_position}}

## When This Does Not Apply

<!-- WHAT  Which services or changes get a lighter version of this review, and what that lighter version
           still requires. Not a blanket exemption.
     WHY   No source read for this bundle exempts a service from review outright; every source that speaks
           to scaling depth scales the review instead of skipping it. GitLab scales per section by maturity
           gate. Mercari scales per row by service level, chosen from the service's own target SLO: "The
           main factor of choosing a Service Level is the expected SLO." AWS scales per occasion and workload
           type, "AWS uses different checklists for different occasions and workload types," and deliberately
           keeps lesser risks out of the checklist entirely to stay usable: "Medium or low risks aren't
           included in the ORR to keep it a lightweight process that doesn't overburden teams and reduce
           their agility and ability to innovate." Even at its lightest, a review that has actually run is
           still a review: one practitioner describes having "seen people do PRRs that just consisted of
           filling in a template document over a couple of hours," which is minimal, not absent. Deep dive:
           production-readiness-review_companion.md section 3 (Anatomy > When This Does Not Apply) and
           section 7.
     ASK   Which of your services or change types would use a lighter path? What does that lighter path
           still require, rather than what it skips? If a service has never gone through even the lightest
           version of this review, is that a gap to name rather than a category to invent?
     PRIORITY  List the smallest, lightest-touch category first, and for each one, name the minimum it still
           requires before naming what it is excused from.
     ROW HINT  A good row names a specific, checkable criterion for the lighter category and states what it
           still requires. A weak row grants an exemption with nothing left to check.
     GOOD  | Internal batch job with no customer-facing traffic and no persistent data of its own | Still
           requires Readiness Criteria's monitoring and on-call rows filled in; exempt from the load-test
           criterion |
     WEAK  | Small services | Skip the review | (no criterion for "small," and no minimum kept) |
     TRAP  Treating any of this as license for a blanket exemption. No source read for this bundle supports
           one; every service gets some version of this review. -->

| Service or Change Type | Lighter Check It Still Requires |
|---|---|
| {{lighter_check_scope}} | {{lighter_check_requirement}} |

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
     PRIORITY  Pair every date-based cadence named in Review Cadence with at least one event-based trigger
           here. An event with no named owner is not a trigger, it is a hope.
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
