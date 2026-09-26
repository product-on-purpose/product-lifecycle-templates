---
title: "Scheduled Email Delivery for Saved Views"
change_id: "CR-SV-01"
baseline_artifact: "Saved Views for Dashboards PRD"
baseline_version: "0.3.0"
requester: "Priya Nair (PM, Reporting)"
date_submitted: "2026-07-08"
decider: "Marta Reyes (Program Manager, Reporting Platform Modernization)"
decision: "Postponed"
decision_date: "2026-07-18"
status: "Postponed"
doc_type: change-request
size: full
source_template: change-request
source_template_version: 0.1.0
---

> **Worked example.** A filled `change-request`, full variant, for the Reporting Platform Modernization
> program at the fictional Acme Analytics - the same program the
> [`prd`](../prd/prd_example.md), [`release-notes`](../release-notes/release-notes_example.md), and
> [`issue-log`](../issue-log/issue-log_example.md) examples cover. `change-request` joined the
> `delivery-docs` family on 2026-09-25 under
> [ADR 0060](../../docs/internal/decisions/0060-change-request-joins-delivery-docs.md), so this is the
> family's newest member's first turn through the shared thread. It targets the Saved Views for Dashboards
> PRD at the same v0.3.0 baseline the PRD example carries, asking to bring one piece of a stated non-goal
> into scope after the feature it excluded had already shipped. The decision reached here is Postponed,
> not Approved: nothing about the PRD, the 2.4.0 release, or the issue log changes because of this
> document, which is itself part of what the decision means. All names, figures, and dates not already
> established in the library's Acme Analytics thread are illustrative.

# Scheduled Email Delivery for Saved Views

## The Request

**Baseline:** [Saved Views for Dashboards PRD](../prd/prd_example.md), version 0.3.0

**Current situation:** [Saved Views](../prd/prd_example.md) shipped in
[Acme Analytics 2.4.0](../release-notes/release-notes_example.md) on 2026-06-30. A user can capture a
dashboard's filters, date range, and columns as a named view, reopen it, and set a default - but every one
of those views still has to be opened in the product before anyone sees it. The
PRD lists a non-goal that covers exactly this gap: "Scheduled delivery of a view by email or Slack. Out of
scope now; likely a fast follow."

**Desired situation:** A user who has already saved a view can turn on a recurring email send for it,
choosing how often it goes out, with no change to how a view is captured, opened, or shared. Slack
delivery, named in the same non-goal, is not part of this ask.

**Requested by:** Priya Nair, submitted 2026-07-08

**Where this came from:** Not from an issue, a risk, or a decision already sitting on a program log. Two
enterprise accounts told their account manager, inside the first two weeks after the 2.4.0 launch, that
someone on their side still runs a manual weekly export because Saved Views does not send anything on its
own. Account management raised it with Priya Nair, the PM who owns the Saved Views PRD, and she is
submitting it as a written request rather than folding it back into the PRD without a record of who asked
or why.

## Why

The two accounts that raised this keep running the same manual weekly export for as long as scheduled
delivery stays out of scope, and account management is already flagging it going into each account's next
renewal conversation - not as a threat to leave, but as the one open item from launch that keeps coming back
up. Declining does not close the topic. It stays the known, named gap in an otherwise well-received release
and resurfaces in the same two conversations until it is either built or someone tells those accounts
plainly that it is not coming.

## Impact

| Dimension | Impact if this change is made |
|---|---|
| Scope | Adds one new delivery channel, scheduled email, to a feature that already shipped; does not change how a view is captured, opened, or shared. |
| Requirements | Adds a requirement for a user-set send frequency and a requirement for what a user sees when a scheduled send fails partway through. |
| Deliverables | A new setting on the existing Views menu, plus a send-scheduling path that the shipped 2.4.0 build does not have. |
| Resources | The same platform engineers who built Saved Views; no new team is needed to scope or build it. |
| Cost | None beyond the engineering time to build and test it; no new infrastructure spend has been scoped. |
| Timeframe | Starting this now would compete with the platform team's other committed work on this program this quarter; Priya and Marta agreed a real estimate should wait for a cycle that has room for it rather than force one today. |
| Quality | None on the Saved Views feature as already shipped; a send-scheduling path is new surface area that would need its own failure-handling and test coverage before release. |

## Decision

**Decision:** Postponed

**Decider:** Marta Reyes (Program Manager, Reporting Platform Modernization)

**Decision needed by:** 2026-07-18

**Decision made on:** 2026-07-18

**Conditions (if approved with conditions):** N/A - the decision was to postpone, not to approve, so no
conditions attach to it. If a later cycle approves the change, conditions would be set at that point.

## Options Considered

| Option | Description | Impact (cost, scope, schedule, quality) | Chosen? | Why |
|---|---|---|---|---|
| Do nothing | Leave scheduled delivery as a non-goal indefinitely | No cost, no scope change, no schedule risk; the two accounts keep exporting by hand | No | Leaves a gap two paying accounts have named, with no record that it was weighed |
| Build email delivery now | Add the scheduled-email path inside the current quarter | Real engineering cost that competes with the platform team's other committed work; no quality risk to what already shipped | No, not this quarter | It would displace work the platform team has already committed to |
| Build email and Slack together now | Bring the whole non-goal into scope in one pass | Higher cost and schedule risk than email alone; no account has asked for Slack specifically | No | Adds cost for a channel nobody has asked for |
| Revisit once a release has room | Build email delivery when a future release can carry it without displacing committed work | Cost and schedule become real once that release is scoped; no quality risk today | Yes - this is what postponing means | Serves the accounts once a release can carry it, without displacing committed work |

## Out of Scope

This request is only about adding a scheduled email path to a view a user has already saved. It does not
touch Slack delivery, which the PRD names alongside email in the same non-goal and which stays deferred on
its own, separately from this decision. It does not touch how a view is created, edited, or shared,
and it does not touch cross-dashboard views, a second PRD non-goal kept closed for an unrelated reason.
Nothing about the underlying dashboard, its filters, or its permissions model changes as a result of this
request.

## Implementation and Traceability

This request went through the Reporting Platform Modernization program's change-control process, the one
the program's [issue log](../issue-log/issue-log_example.md) says every change request is handed to the day
it is raised, and CR-SV-01 is its identifier there; this document is the record that process decided on.
Nothing was updated, because the decision was to postpone: the
[Saved Views PRD](../prd/prd_example.md) stays at its 0.3.0 baseline, and no target version or release is
set, because the release that would carry the work has not been scoped. If a later release takes it on, the
PRD moves past 0.3.0 and this request is reopened rather than replaced. It did not come from, and does not
link to, anything on the issue log; its origin is the two accounts' feedback, which lives in account
management's own notes and is not restated here beyond what the Why and Options sections carry.

*(All names, figures, and dates are illustrative.)*
