---
title: "Saved Views Sharing: Entitlement Audit Mismatch"
service_or_system: "dashboard-service - Saved Views sharing path (ViewsController + entitlement audit job)"
triggering_alert: "SavedViews-EntitlementAuditMismatch (PagerDuty)"
owner: "Marcus Bell (Staff Engineer, Reporting)"
status: "active"
last_updated: "2026-07-28"
doc_type: runbook
size: full
source_template: runbook
source_template_version: 0.1.0
---

> **Worked example.** A filled `runbook`, full variant, for the Saved Views sharing path on Acme Analytics'
> dashboard-service, the same feature the [`sdd`](../sdd/sdd_example.md), [`test-plan`](../test-plan/test-plan_example.md)
> and [`bug-report`](../bug-report/bug-report_example.md) examples describe. Per the `standing-standards` family
> contract, a runbook chains onto the shared Acme Analytics thread only loosely, because it belongs to a team
> rather than to a moment in the story. This one is dated after the sharing rollout's exit review on
> 2026-07-17, after the entitlement defect it responds to was fixed and reverified on 2026-07-15, and after
> the risk register's last review on 2026-07-20, so everything it references had already happened.
>
> Read it alongside [`runbook_guide.md`](runbook_guide.md), the rubric it was graded against. Notice what the
> Procedure section does: it states plainly which of its steps are exact commands and which are judgment
> calls, rather than treating the whole thing as one style. All identifiers, thresholds and timestamps below
> are illustrative.

# Saved Views Sharing: Entitlement Audit Mismatch

## Purpose and Trigger

Triggered by the **SavedViews-EntitlementAuditMismatch** PagerDuty alert. This alert comes from the
entitlement-audit reconciliation job, a safeguard the Reporting and Platform teams added in build 2.4.0
(illustrative) after DEF-2291 (a shared view's aggregate total disclosed the size of a restricted region's
revenue to a recipient who could not see the underlying rows, closed 2026-07-15). The job compares two audit
streams every 5 minutes: `shared_view_served` events emitted by ViewsController, and `permission_check_passed`
events emitted by the dashboard permissions service. It pages when a `shared_view_served` event has no
matching `permission_check_passed` event for the same `request_id` inside the window.

Purpose: inside a 15-minute diagnostic window from page acknowledgment, determine whether a shared view was
actually served without a verified entitlement check. If confirmed, this is the same class of incident
DEF-2291's triage treated as a suspension event rather than a routine defect, not something to file and move
past.

## Prerequisites and Access

| Requirement | Why the Procedure needs it | How to get it before an incident |
|---|---|---|
| `audit-reader` role on the observability platform's Saved Views audit index | Steps 1 through 3 all query the two audit event streams | Requested through the internal access-request tool, group `reporting-saved-views-oncall`; auto-approved for anyone on the Reporting on-call schedule |
| Read access to the permissions service's decision log, via `permsvc-cli` | Step 4 confirms the recipient's actual entitlement scope before Security is paged | Granted with the audit-reader role above; Dana Osei co-signs the initial grant for anyone new to the Reporting rotation |
| Write access to the `saved_views.sharing` flag console | Step 6 disables sharing for one dashboard only, without touching phase 1 (private views) or any other dashboard | Already part of the standard Reporting on-call access bundle; nothing separate to request |
| The permission-persona mapping for the affected dashboard | Step 4 needs to know what the recipient was entitled to see, to size the exposure, not just that a check was missing | Query the permissions service directly with `permsvc-cli`; there is no separate document listing this |

## Procedure

Written **STEP-BY-STEP** for steps 1 through 4, the diagnostic path: a misread log line here has security
consequences, and unlike a restart-and-watch procedure, a responder who is not a permissions-service expert
cannot safely improvise the query. Step 5 is stated as a decision rather than a command on purpose: whether
to declare a security incident is a judgment call with a named owner, not a step to automate away. Step 6
acts on the view already identified in step 1 and leaves no room for improvisation.

| Step | Action | Expected result |
|---|---|---|
| 1 | Note the `request_id`, `view_id` and `recipient_id` from the alert payload. Query the audit index for `event_type:shared_view_served AND request_id:<id>` | Exactly one matching event, timestamped within 5 minutes of the page |
| 2 | Query the same index for `event_type:permission_check_passed AND request_id:<id>` | Zero matching events, which is the anomaly the alert exists to catch |
| 3 | If step 2 returns zero, search for a `permission_check_passed` event on the same `view_id` and recipient, any `request_id`, timestamped within 2 seconds before the served event | If one is found in that window, this is almost certainly a false positive from audit-pipeline lag, not a real mismatch; skip to Validation. If nothing appears in that window, the mismatch is confirmed |
| 4 | Run `permsvc-cli decision --view <view_id> --user <recipient_id>` and compare its output against the view's `config` filters in the `saved_view` table | The comparison names exactly which fields and rows the recipient was, and was not, entitled to see |
| 5 | Page Sam Okafor's Security on-call rotation and declare a P1 security incident, stating the confirmed mismatch and the exposure from step 4 | Security acknowledges inside the standard P1 SLA and takes ownership of the incident record |
| 6 | Disable sharing for the affected dashboard only, by setting `saved_views.sharing` to false scoped to that dashboard ID | The dashboard's Views control shows shared views as unavailable to recipients within 60 seconds |

## Validation

| Check | What counts as pass | Where to verify it |
|---|---|---|
| No further EntitlementAuditMismatch page for the same dashboard | Zero recurrences in the 30 minutes following step 6 | PagerDuty incident timeline for the alert |
| The affected dashboard's sharing flag is off | `saved_views.sharing` reads false for that dashboard ID | Flag console, Saved Views section |
| Security has bounded the exposure | The incident record states which recipient and which rows were affected, and confirms no read has occurred since step 6 | Incident record in the security tracker |
| The cause is either fixed or explained | A ticket exists against the entitlement-check code path, or the step 3 false-positive finding is recorded with both timestamps compared | Incident record |

## Remediation and Cleanup

| Item to undo | Why it must be undone | Owner | Trigger or deadline |
|---|---|---|---|
| `saved_views.sharing` disabled for the affected dashboard | Sharing on this one dashboard stays off until the cause is understood; private views and every other dashboard's sharing are unaffected and stay on | Marcus Bell | Re-enable only once Security signs off and the Validation record is complete, not on a fixed date |
| Recipient sessions active during the exposure window | A session token issued before containment could still hold the disclosed values client-side | Marcus Bell | Force-expire the affected sessions within 4 hours of step 6 |
| Incident record and timeline | The DEF-2291 triage record is what let the next reporter understand Acme's severity scale for entitlement issues; this incident should leave the same kind of record | Sam Okafor | Before the incident is closed |

## When This Does Not Apply

| Symptom that looks like this trigger | What it actually is | What to do instead |
|---|---|---|
| The alert fires for a **private** (non-shared) view | The reconciliation job only audits `shared_view_served` events, so a private view triggering it means the job has misclassified that view's scope, not that an entitlement check was skipped | File a defect against the reconciliation job itself, and notify Marcus Bell; this is not a security incident |
| The alert fires within about 2 seconds of a permissions-service deploy | The two audit streams briefly fall out of order during deploy; this is what step 3's window exists to catch | Wait for the next 5-minute cycle before escalating. If the mismatch is still present after that cycle, treat it as real and continue at step 4 |
| ViewsController's overall error rate rises with no EntitlementAuditMismatch page | A general availability problem, unrelated to entitlement | Hand off to the dashboard-service reliability on-call as a standard incident; this runbook has nothing further to add |

## Review Trigger

| Event that would make this wrong | Owner who notices | What they do about it |
|---|---|---|
| The permissions service changes its audit event schema (for example, `permission_check_passed` is renamed, or its `request_id` field moves) | Dana Osei (Platform, owns the permissions service) | Re-verify the queries in steps 1 through 3 against the new schema and update this runbook before Reporting's on-call baton next changes hands |
| The entitlement-audit reconciliation job's 5-minute window is changed | Marcus Bell (Reporting, owns the job's configuration) | Re-time the 30-minute steady-state check in Validation to at least six times the new window, and update this runbook |
