---
title: "dashboard-service Production Readiness Review: SRE Ownership Handoff"
service_name: "dashboard-service"
owner: "Ines Halvorsen (Engineer, SRE)"
status: "active"
last_updated: "2026-08-22"
doc_type: production-readiness-review
size: full
source_template: production-readiness-review
source_template_version: 0.1.0
---

> **Worked example.** A filled `production-readiness-review`, full variant, for Acme Analytics'
> dashboard-service, the same service the [`sdd`](../sdd/sdd_example.md),
> [`test-plan`](../test-plan/test-plan_example.md), [`bug-report`](../bug-report/bug-report_example.md) and
> [`runbook`](../runbook/runbook_example.md) examples describe. Per the `standing-standards` family
> contract, the chaining stays loose by design: this is the standing instrument belonging to the new SRE
> function, shown as it stood at one review, not a record only this handoff could
> have produced. It is dated **2026-08-22**, after every other date this thread already occupies:
> DEF-2291's discovery on 2026-07-13, the Saved Views Sharing exit review and launch on 2026-07-17, the
> Reporting Squad Definition of Done's amendment on 2026-07-24, the entitlement-audit runbook's first live
> use on 2026-07-28, and the dashboard-scoped kill switch acceptance's own expiry on 2026-08-15. Everything
> cited below had already happened.
>
> This review is the different scenario the family contract asks for: it is not the Saved Views Sharing
> launch itself, which
> [`launch-coordination-checklist_example.md`](../launch-coordination-checklist/launch-coordination-checklist_example.md)
> already covers. It asks whether dashboard-service, as a whole, can be run on a standing basis by whoever
> carries its pager next, not whether one change was safe to ship. Read it alongside
> [`production-readiness-review_guide.md`](production-readiness-review_guide.md), the rubric it was graded
> against. All names not already established in the library's Acme Analytics thread, and every threshold,
> date, and status not otherwise cited, are illustrative.

# dashboard-service Production Readiness Review: SRE Ownership Handoff

## Scope and Trigger

Production, for this review, means dashboard-service serving live Saved Views and dashboard traffic to Acme
Analytics' own customers, not a staging or internal-only environment. This review covers dashboard-service
as a whole: the ViewsController, the `saved_view` table, and every alert and on-call surface the Reporting
team currently owns, not only the Saved Views Sharing feature that shipped on 2026-07-17. Trigger: the
Reporting team wants Acme Analytics' newly formed SRE function to carry dashboard-service's pager from
here on, and this review decides whether SRE says yes. This is not the hardware-manufacturing
Production Readiness Review that NASA or the US Department of Defense would run; nothing here concerns
manufacturing or supplier readiness.

**This review does not cover:** the dashboard permissions service. The entitlement-audit alert reads the
`permission_check_passed` events that service emits, but Platform owns it (Dana Osei, per
[`runbook_example.md`](../runbook/runbook_example.md)) and this handoff does not move it, so Platform
reviews its readiness separately.

## Reviewer and Authority

**Blocking findings escalate to:** Dana Osei (Staff Engineer, Platform), who already holds decision
authority across every Tier 1 launch this thread has produced (see
[`launch-coordination-checklist_example.md`](../launch-coordination-checklist/launch-coordination-checklist_example.md)).
If Ines Halvorsen and Marcus Bell disagree about whether a finding below should block SRE's acceptance, Dana's
sign-off decides it.

| Role | Named Holder | Responsibility |
|---|---|---|
| Decision authority | Ines Halvorsen (Engineer, the new SRE function) | Says whether SRE accepts standing production ownership of dashboard-service, or declines; the outcome below cannot read Ready or Ready with conditions without Ines Halvorsen's signature |
| Second reviewer | Dana Osei (Staff Engineer, Platform) | Brings the outside-the-product-team perspective this review deliberately wants a second reviewer for, and holds the escalation authority named above |
| Reviewed team | Marcus Bell (Staff Engineer, Reporting) | Answers for dashboard-service's current state, and owns every finding below assigned to Reporting |

## Readiness Criteria

| Domain | Criterion | Evidence | Owner | Status | Blocks? | Tier |
|---|---|---|---|---|---|---|
| On-call and incident response | Can SRE actually be paged for dashboard-service today, not only Reporting? | The SavedViews-EntitlementAuditMismatch alert (`runbook_example.md`) routes only to Reporting's own PagerDuty schedule; SRE has not yet been added to that schedule or to any other dashboard-service alert | Ines Halvorsen | Not satisfied | Blocking | All tiers |
| Monitoring and alerting | Do dashboard-service's existing alerts cover the failure classes SRE would actually be paged for, once added to the rotation? | The entitlement-audit reconciliation job pages when a served shared view has no matching permission check inside its 5-minute window (`runbook_example.md`, Purpose and Trigger); the latency and error-rate panels for ViewsController already exist and are the same panels the Saved Views Sharing rollback triggers reference | Marcus Bell | Satisfied | Blocking | All tiers |
| Capacity and performance | Is dashboard-service's capacity sized against a stated ceiling SRE could alert against, not only against today's load? | No stated ceiling exists yet; the design record sets a p95 target for rendering a saved view and for the views list, but not a load ceiling to alert against before either target is missed | Dana Osei | Not satisfied | Advisory | All tiers |
| Deployment and rollback | Can dashboard-service's most recent class of production failure be rolled back by whoever is on call, without needing Reporting's own tribal knowledge? | The entitlement-audit runbook's own procedure disables sharing for one affected dashboard through a documented flag-console action, scoped and reversible without a Reporting engineer | Marcus Bell | Satisfied | Blocking | All tiers |
| Data and backup, disaster recovery | Does dashboard-service need its own backup and disaster-recovery plan, separate from the database it stores its rows in? | Not applicable; see the Not-Applicable Rule below | Dana Osei | Not Applicable | N/A | All tiers |
| Runbook existence | Does a runbook already exist for dashboard-service's known failure modes, one SRE could execute without Reporting on the call? | The entitlement-audit mismatch runbook (`runbook_example.md`, last updated 2026-07-28) already gives a step-by-step diagnostic and rollback procedure | Marcus Bell | Satisfied | Blocking | All tiers |

## Not-Applicable Rule

An item marked Not Applicable above carries the reason beside it here, not only a bare mark.

**Criteria marked not applicable in this review, and why:**

| Criterion Marked Not Applicable | Reason |
|---|---|
| Data and backup, disaster recovery: a dedicated recovery plan for dashboard-service's own storage | dashboard-service's `saved_view` table, and every other row it owns, lives in the shared main Postgres database. Backup and disaster recovery for that database is Platform's own standing responsibility, reviewed under Platform's own instrument, and is not duplicated here |

## Outcome and Sign-off

**Outcome:** Ready with conditions.

| Finding | Severity | Owner | Due Date | Exception (if any) |
|---|---|---|---|---|
| SRE has not yet been added to any dashboard-service PagerDuty schedule, so today only Reporting can actually be paged | High | Ines Halvorsen | 2026-09-05 | Accepted, dated: SRE shadows Reporting's on-call rotation for two full cycles before taking primary, tracked separately in the on-call rotation tool |
| dashboard-service has no stated load ceiling SRE could alert against ahead of missing its rendering or views-list latency target | Medium | Dana Osei | 2026-10-01 | Accepted, dated: Dana Osei owns setting a ceiling from the design record's existing p95 targets before SRE's first full quarter of ownership |

| Signatory | Role | Date |
|---|---|---|
| Ines Halvorsen | Decision authority, SRE | 2026-08-22 |
| Dana Osei | Second reviewer, Platform | 2026-08-22 |
| Marcus Bell | Reviewed team owner, Reporting | 2026-08-22 |

## Review Cadence

Event-driven, with a yearly backstop. dashboard-service's risk profile has already changed once without a
review: on 2026-07-17 Saved Views Sharing turned a private-only surface into a shared one, and nothing
standing looked at the service as a whole. So it comes back for another look whenever it gains a new
externally reachable surface or SRE's on-call footprint for it changes, and twelve months with neither
event brings it back anyway, to catch drift that no single event announces.

## When This Does Not Apply

| Service or Change Type | Lighter Check It Still Requires |
|---|---|
| A dashboard-service change that stays Tier 3 under the Platform team's own launch-coordination-checklist (reversible in a single deploy, reaches no account outside Reporting, touches no permission or billing boundary) | Readiness Criteria's on-call and monitoring rows stay current for whoever already owns the pager. Nothing else in this review applies until the change stops being Tier 3 |

## Review Trigger

| Event That Would Make This Wrong | Owner Who Notices | What They Do About It |
|---|---|---|
| An entitlement or permission-boundary incident recurs on dashboard-service after SRE has taken over its pager, and Readiness Criteria's on-call or monitoring domain should have caught it | Ines Halvorsen (SRE) | Check the incident's timeline against the on-call and monitoring rows first: did the SavedViews-EntitlementAuditMismatch page reach SRE, and did it fire inside the job's 5-minute window? Only if both rows held does the fix become a new row, agreed with Marcus Bell, who owns the job's configuration |
