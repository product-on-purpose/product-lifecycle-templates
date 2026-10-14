---
title: "Platform Team Business Continuity Plan"
business_unit: "Platform, Acme Analytics"
owner: "Dana Osei (Staff Engineer, Platform)"
status: "active"
last_updated: "2026-09-15"
doc_type: business-continuity-plan
size: full
source_template: business-continuity-plan
source_template_version: 0.1.0
---

> **Worked example.** A filled `business-continuity-plan`, full variant, for Acme Analytics' Platform
> team: the standing plan that keeps the shared main Postgres database available through a significant
> disruption, the instrument the
> [`production-readiness-review`](../production-readiness-review/production-readiness-review_example.md)
> example names without showing, when it marks its own "Data and backup, disaster recovery" criterion Not
> Applicable on the ground that this plan already covers it. Per the `standing-standards` family
> contract, the chaining stays loose by design: this is the standing instrument a team agrees once and
> consults repeatedly, not a record written for one disruption. It is dated **2026-09-15**, after every
> document it cites: the [`sdd`](../sdd/sdd_example.md) and
> [`definition-of-done`](../definition-of-done/definition-of-done_example.md) examples' Saved Views work,
> the [`definition-of-ready`](../definition-of-ready/definition-of-ready_example.md) example, the
> [`runbook`](../runbook/runbook_example.md) example's entitlement-audit incident, and the
> [`production-readiness-review`](../production-readiness-review/production-readiness-review_example.md)
> example's decision, on 2026-08-22, that Acme Analytics' new SRE function takes standing on-call
> ownership of dashboard-service. Everything cited below had already happened. This plan's own first
> version predates all of it: its revision history carries an entry from 2026-03-02, months before the
> review that first names it. Read it alongside
> [`business-continuity-plan_guide.md`](business-continuity-plan_guide.md), the rubric it was graded
> against. All names not already established in the library's Acme Analytics thread, and every figure,
> date, and status not otherwise cited, are illustrative. That includes billing-service and
> notifications-service, the two further dependents of the shared database this plan names: no earlier
> example enumerates the database's dependents beyond `saved_view`, so this one introduces them.

# Platform Team Business Continuity Plan

## Purpose and Scope

This plan covers Acme Analytics' Platform team and the one piece of shared infrastructure every other
team's service ultimately sits on top of: the shared main Postgres database that dashboard-service's
`saved_view` table, among other teams' tables, lives in. A significant disruption, for this plan, is any
event that leaves that database unreachable, or returning errors, for any dependent service for more than
ten minutes, or that makes the cloud region it runs in unavailable. A disruption to one dependent team's
own application code, with the database itself healthy, is that team's own incident and does not activate
this plan.

**Separate disaster recovery plan, if one exists outside this document (otherwise, see the Disaster
Recovery section below):** None. No separate disaster recovery plan exists for the shared database; this
variant's own Disaster Recovery section below carries that detail, because Platform decided, when this
plan was first written, that the database's recovery strategy belongs next to the business impact it
protects rather than in a document of its own.

## Business Continuity Team and Roles

| Role | Job Title and Current Holder | Responsibility |
|---|---|---|
| Business Continuity Team Lead | Dana Osei, Staff Engineer, Platform | Owns this plan, has authority to activate it, and is the single person every dependent team escalates a shared-database disruption to |
| Database Reliability Lead | Rosa Chen, Senior Engineer, Platform | Executes the recovery procedures named in Disaster Recovery below, and owns the corrective actions this plan's own exercises produce |
| Dependent-Team Liaison | Whoever is currently on call for the affected dependent service (see Activation and Incident Management for who that includes today) | Confirms to the Business Continuity Team Lead which of their own team's critical processes are actually affected, so this roster does not have to name every dependent team's engineer in advance |

**Authority to activate this plan:** Dana Osei, Staff Engineer, Platform
**Named successor if the activation authority is unreachable:** Rosa Chen, Senior Engineer, Platform
**Delegation of authority, if normal channels of direction are disrupted:** If neither Dana Osei nor Rosa
Chen is reachable within fifteen minutes (illustrative) of a declared disruption, the Platform engineer
currently on call for the shared database may activate this plan directly, and must notify Dana Osei and
Rosa Chen as soon as normal channels of direction are reestablished.

## Business Impact Analysis Summary

| Critical Process | Recovery Time Objective | Recovery Point Objective | Systems and Suppliers Depended On |
|---|---|---|---|
| Serving reads and writes to the shared primary Postgres database | 30 minutes (illustrative) | 5 minutes (illustrative) | dashboard-service (Reporting, see [`sdd_example.md`](../sdd/sdd_example.md)); billing-service (Finance Engineering, illustrative); notifications-service (Growth, illustrative) |
| Platform's internal admin console, used to triage and declare a disruption | 8 hours (illustrative) | Not applicable; the console holds no data of its own | The shared primary Postgres database above, for its own audit log only |

## Continuity Strategies and Manual Workarounds

| Critical Process | Manual Workaround | Recovery Level Chosen, and Why |
|---|---|---|
| Serving reads and writes to the shared primary Postgres database | Platform posts a status-page entry asking every dependent team to degrade to its own read-only or cached behavior while Platform executes the Disaster Recovery section's recovery strategy; Platform does not attempt to serve writes from anywhere other than the recovered database | Warm standby, not a faster multi-region active-active setup: the database's own Recovery Time Objective above is thirty minutes (illustrative), and a warm standby already meets it without the added cost and operational complexity an active-active setup would add |
| Platform's internal admin console | Platform engineers on the Database Reliability rotation operate directly against the database through command-line tooling, bypassing the console entirely | Manual: the console is a convenience for declaring and tracking a disruption, not part of serving any dependent team, so an eight-hour (illustrative) objective leaves room to work without it, and a second console would buy nothing the command line does not already give |

## Activation and Incident Management

**Activation criteria:** The shared primary Postgres database is unreachable, or returning errors, for
any dependent service for more than ten minutes, or the cloud region it runs in is declared unavailable.
**Who declares an activation:** Dana Osei, Staff Engineer, Platform, or Rosa Chen as named successor.

| Order | Who Is Notified | Method |
|---|---|---|
| 1 | The Platform engineer currently on call for the shared database | Paged directly through Platform's own on-call tool |
| 2 | Dependent-team liaisons for dashboard-service, billing-service and notifications-service | Paged through each team's own on-call tool, plus the shared status page, so a dependent team still learns of the disruption if its own paging channel is itself the thing that is down |
| 3 | Acme Analytics' SRE on-call rotation (added in version 1.2.0 on 2026-08-25, after the 2026-08-22 production readiness review decided SRE would carry dashboard-service's own pager; dashboard-service depends on the database this plan protects, so SRE now needs the same notice a dependent team gets) | Paged through the same on-call tool dashboard-service's own on-call already uses |
| 4 | Acme Analytics' internal status page, for any team not named above that also reads from the shared database | A status-page entry, updated at each stage of recovery |

**Condition for standing this plan down:** The Database Reliability Lead confirms the database is serving
reads and writes within the Recovery Time and Recovery Point Objectives stated in Business Impact
Analysis Summary above, and thirty minutes (illustrative) pass with no recurrence.

## Training, Testing and Exercising

| Exercise Type | Date | What It Validates | Observer | Finding | Corrective Action Owner | Due Date |
|---|---|---|---|---|---|---|
| Tabletop | 2026-09-05 (illustrative) | The delegation of authority in Business Continuity Team and Roles above: neither Dana Osei nor Rosa Chen can be reached, so the Platform engineer on call for the shared database must activate this plan and begin recovery alone | Ines Halvorsen (Engineer, SRE), observing independently of Platform, the team being exercised: dashboard-service, which SRE now carries the pager for, depends on the database this plan protects, which is why SRE asked to observe this exercise rather than only receive its finding afterward | The on-call engineer could activate the plan but lacked the hosting provider permission needed to promote the standby replica, so recovery would have waited until one of the two leads was reached | Rosa Chen | 2026-10-01 (illustrative) |
| Full-scale failover test | 2026-06-10 (illustrative) | An actual failover of the shared primary Postgres database to its standby region, judged on data integrity, Recovery Time Objective and Recovery Point Objective | Acme Analytics' internal audit function | Failover itself completed inside the stated Recovery Time Objective, but verifying the restored data's integrity on the standby copy took long enough to come close to breaching the Recovery Point Objective | Rosa Chen | 2026-06-24 (illustrative; closed in version 1.1.0 by writing the restore verification criteria now stated in Disaster Recovery below) |

## Plan Administration

| Vendor or Contractor | What They Provide | Contact Method |
|---|---|---|
| Platform's managed Postgres hosting provider | Hosts the primary database and its standby replica across two regions | The enterprise support phone line printed in the on-call binder. The provider's web console is assumed unreachable during a regional outage, which is exactly when this line is needed |
| The offsite backup storage vendor | Stores the nightly encrypted snapshot named in Disaster Recovery below, in a third region separate from both the primary and standby database regions | A named account representative's direct line, confirmed quarterly rather than assumed current |

| Version | Date | Changed By | Summary of Change |
|---|---|---|---|
| 1.0.0 | 2026-03-02 (illustrative) | Dana Osei | Initial plan: the shared primary Postgres database's business impact analysis, activation criteria and recovery strategy |
| 1.1.0 | 2026-06-24 (illustrative) | Rosa Chen | Added the restore verification criteria to Disaster Recovery, closing the 2026-06-10 failover test's finding |
| 1.2.0 | 2026-08-25 | Dana Osei | Added SRE as a notified stakeholder in Activation and Incident Management, following the 2026-08-22 production readiness review's decision that SRE takes standing on-call ownership of dashboard-service |
| 1.3.0 | 2026-09-15 | Dana Osei | Recorded the 2026-09-05 tabletop exercise and its finding in Training, Testing and Exercising, and the trigger that watches for its recurrence in Review Trigger |

**Master copy held by:** Dana Osei, Business Continuity Team Lead.
**Where a reachable, offline copy of this plan is kept:** A printed copy in Platform's on-call binder,
plus an offline PDF on the laptop issued to whoever currently holds the Platform on-call pager, neither of
which depends on the database this plan exists to recover.

## Disaster Recovery

| Critical System | Recovery Strategy | Recovery Order (What It Depends On) |
|---|---|---|
| Shared primary Postgres database | An existing read replica in the standby region is promoted to primary; if promotion itself fails, a fresh instance is restored from the most recent automated snapshot named in the backup statement below | Recovers first. Every dependent system named in Business Impact Analysis Summary above, dashboard-service, billing-service and notifications-service, waits on this database before attempting its own recovery |

**Backup and offsite storage, including at least one offline copy:** Continuous write-ahead log shipping
keeps the standby region's replica current to within the Recovery Point Objective stated above; a nightly
encrypted snapshot is additionally copied to offline storage in a third region, the one copy the hosting
vendor's own production credentials cannot reach.
**Recovery procedures (written so another trained person could follow them):** The Database Reliability
Lead's own step-by-step failover procedure, kept with the vendor contact information named in Plan
Administration above, written so a trained database engineer from outside Platform could carry it out.
**Restore verification criteria (data integrity, Recovery Time Objective, Recovery Point Objective):** A
promoted or restored database is not declared back in service until a Database Reliability engineer
confirms three things: the row counts on the three largest tables, including dashboard-service's own
`saved_view`, match the last known-good count within an explainable delta; write latency returns to its
normal range; and any data actually lost stays inside the five-minute Recovery Point Objective stated
above. This criterion exists because the 2026-06-10 exercise above found the failover itself fast but its
restore verification slow enough to risk breaching that objective.
**Recovery test schedule and type, and when it was last run:** A full-scale failover test at least once a
year, last run 2026-06-10 (see Training, Testing and Exercising above), with a tabletop exercise in
between.

## Review Trigger

| Condition That Would Make This Plan Wrong | Owner Who Notices | What They Do About It |
|---|---|---|
| A service begins depending on the shared primary Postgres database, or an existing dependent stops using it | Dana Osei | Update Business Impact Analysis Summary and Continuity Strategies and Manual Workarounds with the added or removed dependency before the next scheduled exercise, not only at the next annual review |
| The 2026-09-05 tabletop's finding above recurs: the next activation or exercise still finds the on-call engineer unable to promote the standby without one of the two leads | Dana Osei | Treat it as the corrective action from that finding not actually having worked, and escalate directly to the Database Reliability Lead, rather than opening it again as a new finding |
| The hosting provider changes the replication, snapshot or region arrangement the Disaster Recovery section relies on | Rosa Chen | Re-run the failover test against the changed arrangement before the old procedure is trusted again, and update the backup and offsite storage statement to match what is actually running |

**Annual exercise required by policy or regulation, if any (a floor under the conditions above, not a
substitute for them):** Platform runs the full-scale failover test described in Disaster Recovery at
least once a year as this plan's own floor under the conditions above, not as a substitute for them. The
2026-09-05 tabletop is additional exercise, not the annual test itself.
