---
title: "Acme Analytics - Reporting Platform Modernization Change Log"
project: "Reporting Platform Modernization"
log_keeper: "Marta Reyes (Program Manager, Reporting Platform Modernization)"
last_reviewed: "2026-07-20"
review_cadence: "Weekly with workstream leads, the same day as the RAID log and issue log review"
status: active
related: ["../change-request/change-request_example.md (CR-SV-01, the one request this log carries a row for)", "../issue-log/issue-log_example.md (the program issue log; its Purpose and Threshold section states that a change request never lands there)", "../raid-log/raid-log_example.md (the program RAID log)", "../risk-register/risk-register_example.md (the program risk register)", "../prd/prd_example.md (Saved Views for Dashboards PRD, the baseline CR-SV-01 targets)"]
doc_type: change-log
size: full
source_template: change-log
source_template_version: 0.1.0
---

> **Worked example.** A filled `change-log`, full variant, for the Reporting Platform Modernization program
> at the fictional Acme Analytics - the same program the
> [`prd`](../prd/prd_example.md), [`change-request`](../change-request/change-request_example.md),
> [`issue-log`](../issue-log/issue-log_example.md), [`risk-register`](../risk-register/risk-register_example.md),
> [`raid-log`](../raid-log/raid-log_example.md), and [`kpi-dashboard`](../kpi-dashboard/kpi-dashboard_example.md)
> examples already cover. `change-log` joined the `governance-docs` family as its fifth member on 2026-09-27
> under [ADR 0061](../../docs/internal/decisions/0061-change-log-joins-governance-docs-as-a-fifth-member.md),
> so this log is shown as it stood at the same 2026-07-20 review the risk register, the RAID log, the issue
> log, and the KPI dashboard were each last reviewed against. It carries one row, `CR-SV-01`, the change
> request [`change-request_example.md`](../change-request/change-request_example.md) already shows in full;
> this document is the standing register that request feeds, not a second copy of it. All names, figures,
> and dates not already established in the library's Acme Analytics thread are illustrative.

# Acme Analytics - Reporting Platform Modernization Change Log

## Purpose and Boundary

This log tracks requests to change any artifact the Reporting Platform Modernization program has already
baselined. Today that means one artifact: the [Saved Views for Dashboards PRD](../prd/prd_example.md),
currently at version 0.3.0. It is not the request document itself: each request, like
[CR-SV-01](../change-request/change-request_example.md), stands as a document of its own, and this log gets
exactly one row per request, whatever the eventual disposition turns out to be. It is not the program's
release notes either, which announce what actually shipped to the people using it and carry no requester,
decider, or decision field of their own; a release is a release, not a change against this program's
baseline. It is not a separate decision log: this program records a change's decision inside this log's own
Decision column rather than standing up a second artifact for it, a choice stated here rather than left for
a reader to guess at. And it is not where the [issue log](../issue-log/issue-log_example.md) sends anything:
that log's own Purpose and Threshold section already states that a request for change on this program is
handed straight to this log's process the day it is raised, so no row on the issue log ever carries one, and
no row here originates from a resolved issue either. Read by the program manager, the workstream leads who
need to know what was asked against their own baseline, and the steering group on the rare row that reaches
it.

## Status Vocabulary

**Status values:** Submitted, Under review, Approved, Postponed, Rejected, Implemented. This program folded
two stages of a published eight-value list into one Under review stage rather than tracking each assessment
step on its own, and has dropped a Merged value entirely: no two requests on this program have ever needed
to be combined into one, and the vocabulary does not carry a value nobody has used.

**Decision values (kept apart from status):** Approved, Rejected, Postponed. A closed row's status alone
never tells a reader which way a request went; the Decision column, right of Status in the table below,
always says so, along with the reason.

**Priority scale:** High, Medium, Low, or Not set. Not set applies when a request's priority has not actually
been set - not "Low" standing in for "we have not looked at this yet," but its own honest label, used below
on the program's one row so far.

## Change Log

No row on this log is ever removed, whatever was decided. Only one request has been raised against this
program's baseline since it was first agreed, and its disposition was not to approve it.

| ID | Category | Change | Baseline artifact | Baseline version | Requested by (date) | Priority | Status | Decision (and reason) | Decided by (date) |
|---|---|---|---|---|---|---|---|---|---|
| CR-SV-01 | Scope | Scheduled Email Delivery for Saved Views: a recurring scheduled-email send for a saved view a user has already captured, a piece of a non-goal the PRD named and set aside when the underlying feature shipped | Saved Views for Dashboards PRD | 0.3.0 | Priya Nair (PM, Reporting), 2026-07-08 | Not set - a real estimate, and the priority that would follow from it, was deliberately left for a cycle with room to do the work justice | Postponed | Postponed - building it this quarter would displace platform engineering work the program has already committed to; revisit once a release has room, rather than build it now or rule it out for good | Marta Reyes (Program Manager, Reporting Platform Modernization), 2026-07-18 |

## Authority and Escalation

**Authority:** the program manager, Marta Reyes, decides anything that commits no new cost and leaves the
program's own Q3 launch date exactly where it already sits.

**Escalation threshold:** a request that would either commit new cost or move the Q3 launch date needs the
steering group's own sign-off before it can be approved - the same body the risk register and the RAID log
escalate to when a risk or an issue outgrows the program manager's authority on its own.

**Currently escalated:** nothing on this log. CR-SV-01's postponement sat entirely inside Marta Reyes's own
authority: postponing a request neither commits new cost today nor moves the Q3 date, so nothing about the
decision needed to go above her.

## Implementation and Traceability

| ID | Target date | Actual date | Updated (artifact, version) | Links |
|---|---|---|---|---|
| CR-SV-01 | Not set - no release has been scoped yet that could carry this work | Not applicable - nothing has shipped | None. The [Saved Views for Dashboards PRD](../prd/prd_example.md) stays at version 0.3.0, unchanged by this request | [Change request CR-SV-01](../change-request/change-request_example.md), raised from account-management feedback, not from anything already on this program's other logs; it has not fed a row back onto any of them either |

## Cumulative Effect

Since the [Saved Views for Dashboards PRD](../prd/prd_example.md) was baselined at version 0.3.0, this log
has approved zero changes against it. Its one row, CR-SV-01, was postponed rather than approved, so it adds
nothing to that total: a request only counts toward the running figure once its Decision column reads
Approved, and this one does not. *(Illustrative: this program's baseline has not moved since it was first
agreed, and the total above is read straight off the single row in the table, not asserted on its own.)*

## Review and Ownership

Kept by Marta Reyes, the program manager, who also keeps this program's risk register, RAID log, and issue
log. This log's own review has not needed a cadence of its own: it joins the weekly workstream review the
RAID log and issue log already hold, on the same day, rather than pulling the workstream leads into a second
meeting for one artifact. A row closes once its status reaches Implemented and the artifact it named is
confirmed at the new baseline version named in the row above; CR-SV-01 has not reached that point, and is not
expected to until a later cycle takes the work back up. Last reviewed 2026-07-20; next review 2026-07-27,
the same date the RAID log and issue log return to.

*(All names, figures, and dates are illustrative.)*
