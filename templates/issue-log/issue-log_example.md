---
title: "Acme Analytics - Reporting Platform Modernization Issue Log"
project: "Reporting Platform Modernization"
log_owner: "Marta Reyes (Program Manager)"
issue_management_approach: "Reporting Platform Modernization Issue Management Plan v1 (internal)"
last_reviewed: "2026-07-20"
review_cadence: "Weekly with workstream leads, same day as the RAID log review; escalated rows also go to the monthly program board"
status: active
related: ["../raid-log/raid-log_example.md (the program RAID log; ISS-11 and ISS-12 here are the deepened record behind its Issues quadrant)", "../risk-register/risk-register_example.md (the program risk register; R-03's materialization becomes ISS-11, R-06's partial materialization becomes ISS-12)", "../kpi-dashboard/kpi-dashboard_example.md (the program KPI dashboard; its view-list load metric is the one ISS-12's fix must bring under budget)", "../prd/prd_example.md (Saved Views for Dashboards PRD)", "../sdd/sdd_example.md (Saved Views design)"]
doc_type: issue-log
size: full
source_template: issue-log
source_template_version: 0.1.0
---

> **Worked example.** A filled `issue-log`, full variant, for the Reporting Platform Modernization program at
> the fictional Acme Analytics - the same program the
> [`risk-register`](../risk-register/risk-register_example.md) and
> [`raid-log`](../raid-log/raid-log_example.md) examples cover, and the deepened record behind the RAID log's
> Issues quadrant that the
> [`governance-docs` family contract](../../docs/internal/contracts/governance-docs.md) calls for. It is
> shown as it stood at the program's 2026-07-20 review, the same date the RAID log and the risk register were
> last reviewed: `ISS-11` and `ISS-12` are the same two open issues the RAID log's Issues quadrant already
> lists, carried here with the closure audit trail and cross-log links a standalone issue log adds. Read this
> alongside [`issue-log_guide.md`](issue-log_guide.md), the rubric it was graded against. All names, figures,
> and dates not already established in the library's Acme Analytics thread are illustrative.

# Acme Analytics - Reporting Platform Modernization Issue Log

## Purpose and Threshold

An issue on this log is a problem that has **already surfaced** against the Reporting Platform Modernization
program, not something that merely might occur, and either the accountable workstream lead cannot close it
within two working days without help from outside their own team, or it touches the program's committed Q3
launch date, its budget, or a compliance boundary regardless of how quickly it might close. That second
clause is why a fast-moving problem can still land here: speed of resolution does not excuse a program-level
threat from being written down.

**Out of scope, and where it goes instead.** Anything that has not yet happened stays on the
[risk register](../risk-register/risk-register_example.md); this log sits downstream of it, and a register row
marked **Materialized** is exactly the one that graduates onto this log (see Links to Other Logs). A defect in
already-shipped or shipping code, with no open program-management question riding on it, belongs to the
reporting team's own defect tracker, not here. A request for change on this program does not route through
this log either: this program hands every change request straight to its own change-control process the day
it is raised, so no row below carries one; a program that instead folds change requests into its issues would
record that choice here and log them.

**Status values used on this log:** Open, Postponed, Resolved, Closed, the four the program's Issue
Management Plan defines; it does not add a fifth. An open issue that is being worked stays Open here, which
the RAID log's working summary writes as In Progress. Resolved and Closed are kept distinct deliberately (see
Closed Issues): a row is not Closed until someone other than whoever fixed it has checked the fix.

**Owner and governing document.** Marta Reyes, the program manager, owns this log. Its threshold, priority
scale, and escalation rule are set out in the *Reporting Platform Modernization Issue Management Plan v1*
(internal), summarized in the three sections below rather than restated there in full.

## Priority Scale

This program scores an issue on a single three-level scale, anchored to the same schedule, cost, and compliance
dimensions the risk register already uses, so a reader moving between the two documents is not learning a
second vocabulary.

- **High** - threatens the committed Q3 launch date, the program's budget, or a compliance boundary that would
  need steering-group sign-off; or the workstream affected has no accepted workaround today. Escalate under
  the rule below without waiting for the next weekly review.
- **Medium** - affects one workstream's own plan, inside a slip or a quality gap that team can absorb without
  the program noticing, but is not yet a program-level threat.
- **Low** - local and already absorbed in the normal course of work; kept on the log for the record, not for
  attention.

Both issues open below are High: one blocks a critical-path handover, the other threatens the launch's own
performance promise. *(Illustrative scale; a real program would set these anchors with its own steering
group.)*

## Issues

Ordered by priority, then by age within it. *(Illustrative entries.)*

| ID | Category | Issue (cause and impact) | Raised (by, date) | Priority | Owner | Next action (target date) | Status | Last updated |
|---|---|---|---|---|---|---|---|---|
| ISS-11 | Key-person | Because the engineer who held the undocumented knowledge of the new query engine left the program on two weeks' notice, no one else on the team can safely extend or debug it, putting the platform team's 2026-08-01 delivery to the Saved Views workstream at risk of slipping | Marta Reyes, 2026-06-14 | High | Marta Reyes | Steering-group approval of a backfill-contractor budget (requested 2026-07-04); meanwhile pair a second engineer with the platform team to document the engine; target 2026-07-31 | Open (escalated) | 2026-07-20 |
| ISS-12 | Performance | Because the saved-view list ships with no pagination, its 95th-percentile load time measured 620ms in staging against the program's 500ms budget; unfixed, the launch breaks the speed promise the program exists to make | Dana Osei, 2026-07-10 | High | Dana Osei | Paginate and lazy-load the view list, then re-test at three times the expected view count; target 2026-07-24 | Open | 2026-07-19 |

## Escalation

**Rule.** Nothing escalates on age alone. An issue goes up to the steering group when fixing it takes
something the program manager cannot give: money, a change to scope, or a move of the committed Q3 launch
date. Once a row is up, it ages from the day it went up, on the same two-week line the RAID log applies to
its escalated items: a decision still outstanding after two weeks is called out at the weekly review as
stuck above the team.

**Currently escalated.** ISS-11 went up on 2026-07-04, once its resolution plan needed a GBP 45k
backfill-contractor budget that only the steering group can approve. At this review that decision has been
outstanding for 16 days, past the two-week line; the team's own part, a costed plan, is done. ISS-12 has
not gone up: paginating the view list is inside the team's own authority, and its 2026-07-24 target is the
next check.

## Review and Ownership

The program manager reviews this log every Monday with the workstream leads, on the same day and with the
same audience as the RAID log's working review; escalated and High-priority rows are looked at before anything
else on the agenda. The program manager, Marta Reyes, owns the log day to day; each row above keeps its own
named owner, separate from her. Last reviewed 2026-07-20; next review 2026-07-27, following the same weekly
cycle the RAID log uses.

## Closed Issues

Kept for the life of the log; not deleted. *(Illustrative entries.)*

**ISS-06.** The load-test harness used for the program's June dry run shared a compute cluster with an
unrelated batch job, which put noise into every p95 number it produced. Identified by Dana Osei on 2026-06-10.
Fixed by Ravi Patel (Platform engineering), who moved the harness onto its own dedicated node pool, isolated
from other workloads. The row sat as **Resolved** for two days while Lee Zhang, who did not do the fix,
re-ran the numbers on the isolated harness before confirming them; closed by Lee Zhang on 2026-06-20. Lesson:
no p95 figure leaves the platform team's own dashboards until it has been reproduced on the dedicated harness;
this is why the 620ms figure behind ISS-12 above is trusted.

**ISS-09.** The event-log export used for the design-partner pilot's first dry run silently stopped at
10,000 rows, dropping roughly a third of the six pilot analysts' recorded dashboard events. Identified by
Priya Nair on 2026-07-02. Fixed by Lee Zhang's team, who removed the row cap and re-ran the export.
Confirmed by Priya Nair, who raised it and is not the person who fixed it, on 2026-07-15. Lesson: validate
the row limit of any export before trusting a number it produces for a program metric.

## Links to Other Logs

Linked by ID; no other log's detail is copied here. The risk register's own R-03 row still points to the
RAID log's Issues quadrant, the summary this log deepens. *(Illustrative.)*

**ISS-11.** Originated from the risk register's key-person risk,
[R-03](../risk-register/risk-register_example.md), which the register now shows under Closed and Materialized
Risks: the register marked that row Materialized on 2026-06-14, the day the engineer left. No request for
change came out of it. No decision has closed it yet: the steering group's approval of the
backfill-contractor budget, requested 2026-07-04, is still awaited (see Escalation above). Implementing
tasks: TASK-241 (contractor onboarding, once the budget is approved), TASK-242 (pair a second engineer and
write the handover documentation).

**ISS-12.** Originated from the performance risk
[R-06](../risk-register/risk-register_example.md), which the register still carries open at the launch level;
this row is the slice of it that has already materialized in staging. No request for change; no decision
needed beyond the remediation already underway. Implementing tasks: TASK-243 (paginate and lazy-load the view
list), TASK-244 (re-test at three times the expected view count before launch).

**ISS-06 and ISS-09 (closed).** Neither began as a risk, raised a request for change, or needed a governance
decision; both were found, fixed, and confirmed inside the team. No links to record for either.

*(All IDs, dates, figures, and names are illustrative.)*
