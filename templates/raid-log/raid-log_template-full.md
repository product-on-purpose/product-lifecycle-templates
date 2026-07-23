---
title: "{{project_name}} RAID Log"
project: "{{project_name}}"
raid_expansion: "Risks, Assumptions, Issues, Dependencies"
log_owner: "{{log_owner}}"
last_reviewed: "{{date}}"
review_cadence: "{{cadence}}"
status: "{{status}}"
doc_type: raid-log
size: full
source_template: raid-log
source_template_version: 0.1.0
---

<!--
FULL RAID LOG. The governance-grade log: everything in the lean variant, plus richer per-quadrant fields, an
Escalation and Aging section, and a Cross-Quadrant Summary. Use it for a larger or multi-team program, when a
steering group consumes an escalation view, or when you need aging and migration tracking. Larger programs
often split the four quadrants onto four tabs; the sections below map to those tabs.

This is a STRICT SUPERSET of raid-log_template-lean.md: the first six sections are identical in name and
order; full only adds columns and the last two sections. If you are growing from lean, add these; do not
reorder.

A RAID LOG IS A LIVING DOCUMENT. Its defining failure is being set up at kickoff and abandoned; a RAID log is
only as good as its review cadence. State your acronym (this template uses Risks, Assumptions, Issues,
Dependencies). The four quadrants are different kinds of thing and MIGRATE between each other (an assumption
that fails becomes an issue; a dependency that slips becomes a risk, then an issue). See
raid-log_companion.md sections 1, 3, 6, and 7.

THE POINT OF THE FULL VARIANT IS SEEING THE WHOLE PICTURE AND WHAT IS STUCK. The Escalation and Aging section
surfaces items that have sat too long (aging is the single best measure of whether governance is actually
deciding anything); the Cross-Quadrant Summary shows counts and the migrations between quadrants. See
raid-log_companion.md section 4.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP; tables
   add PRIORITY and ROW HINT.
2. Replace each {{placeholder}}. Give every item a unique ID and one named owner.
3. If a quadrant is empty, keep the heading and write "None open" rather than deleting it.
4. Never finished, but before you share it: self-grade against raid-log_guide.md, then DELETE every HTML
   comment.
-->

# {{project_name}} RAID Log

## Purpose and Scope

<!-- WHAT  What program this log covers, WHICH expansion of RAID it uses, who owns it, the review cadence, and
           its relationship to any standalone risk register.
     WHY   The acronym is ambiguous, so state what its letters mean here; scope also says what does not belong
           so the log does not bloat into clutter. At program scale, name where the deep risk detail lives.
           Deep dive: raid-log_companion.md section 3 (Purpose and Scope), section 6 (the acronym debate),
           and section 8.
     ASK   What program does this cover? Is the A Assumptions or Actions, the D Dependencies or Decisions?
           Who owns the log? How often is it reviewed and by whom? Where does the audit-grade risk detail
           live?
     GOOD  "RAID log for the Reporting Platform Modernization program. RAID = Risks, Assumptions, Issues,
           Dependencies. Owned by the program manager, populated by workstream leads, reviewed weekly with a
           monthly deep dive. The R quadrant summarizes the separate risk register; deep scoring lives there."
     WEAK  "Program RAID." (no expansion, owner, cadence, or register relationship)
     TRAP  Leaving the acronym undeclared at scale, where multiple teams populate the log and each assumes a
           different expansion. -->

{{purpose_and_scope}}

## Risks

<!-- WHAT  Things that MIGHT happen, as a summary that points to the risk register: a risk statement,
           likelihood/impact, response, owner, status, and the register ID.
     WHY   At program scale the RAID R is the weekly dashboard; the deepened record (inherent/residual
           scoring, triggers, appetite) is the standalone risk register. Keep them linked, not duplicated. A
           risk that materializes closes here and opens as an Issue. Deep dive: raid-log_companion.md section
           3 (Risks) and section 8.
     ASK   What might happen and what would it do? Likelihood and impact? Response? Owner? Which register
           entry holds the detail?
     PRIORITY  Order by severity. Owner is one named person. Register ref links to the authoritative entry;
           do not duplicate its scoring here.
     ROW HINT  A good row is a cause-event-consequence statement linked to a register ID. A weak row is a
           theme label duplicating half the register.
     GOOD  | R-01 | Charting-library licence may change and force a re-platform, slipping launch a quarter | H (register residual 10) | Mitigate: lock a 24-month licence | Dana Osei | Open | RR-01 |
     WEAK  | R-01 | Vendor risk | High | fix | team | | |
     TRAP  Letting the RAID R and the register drift apart. Link by ID and keep the register authoritative. -->

| ID | Risk (cause -> event -> consequence) | Severity | Response | Owner | Status | Register ref |
|---|---|---|---|---|---|---|
| {{risk_id}} | {{risk_statement}} | {{severity}} | {{response}} | {{owner}} | {{status}} | {{register_ref}} |

## Assumptions

<!-- WHAT  Things treated as TRUE without proof, with source, confidence, impact if false, a validation action
           and date, and status.
     WHY   Assumptions are latent risks; the validate-by date catches decay before it becomes an issue. At
           program scale, record who was consulted so a failed assumption can be traced. This is the quadrant
           agile programs most often lose. Deep dive: raid-log_companion.md section 3 (Assumptions).
     ASK   What are we taking on faith? Who asserted it? How confident? Impact if false? What validates it,
           by when? Has it since been validated or invalidated?
     PRIORITY  Order by impact-if-false. High-impact, low-confidence assumptions are the most dangerous.
           Status includes Invalidated (which should trigger a new issue or risk).
     ROW HINT  A good row names a specific belief, its consequence if wrong, a validate-by date, and a
           source. A weak row is a vague hope.
     GOOD  | A-01 | The charting vendor will renew on current licence terms | Vendor mgmt | Low | Forces a re-platform (feeds R-01) | Confirm with vendor by 2026-08-15 | Dana Osei | Open |
     WEAK  | A-01 | It'll be fine | | | | | | |
     TRAP  Never revisiting assumptions. An invalidated assumption that is not migrated to an issue is a
           silent failure. -->

| ID | Assumption | Source | Confidence | Impact if false | Validate by | Owner | Status |
|---|---|---|---|---|---|---|---|
| {{assumption_id}} | {{assumption}} | {{source}} | {{confidence}} | {{impact_if_false}} | {{validate_by}} | {{owner}} | {{status}} |

## Issues

<!-- WHAT  Things that HAVE happened, with severity AND priority, cause, resolution plan, raised date, target
           date, owner, and status.
     WHY   An issue has no probability; it carries a raised date for aging and a target date for resolution.
           Separating severity (how bad) from priority (how urgent) lets a low-severity blocker still be
           high-priority. When a risk materializes, close it and open a matching issue. Deep dive:
           raid-log_companion.md section 3 (Issues).
     ASK   What happened? How bad (severity) and how urgent (priority)? What caused it? Plan and target date?
           When was it raised? Did it come from a materialized risk or a failed assumption?
     PRIORITY  Order by priority. Owner is one named person. Raised date drives aging; target date drives
           the resolution deadline.
     ROW HINT  A good row records what happened, severity and priority, the plan, and both dates. A weak row
           is a symptom with no plan or dates.
     GOOD  | ISS-11 | Query-engine lead left; handover incomplete (materialized R-03) | High | High | Key-person dependency | Pair a second engineer; document the engine | 2026-06-14 | 2026-07-31 | Marta Reyes | Open |
     WEAK  | ISS-11 | Staffing | | | | fixing | | | | |
     TRAP  Logging a not-yet-happened problem as an issue. If it might happen, it is a risk; migrate
           deliberately. -->

| ID | Issue | Severity | Priority | Cause | Resolution plan | Raised | Target | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| {{issue_id}} | {{issue}} | {{severity}} | {{priority}} | {{cause}} | {{resolution_plan}} | {{raised_date}} | {{target_date}} | {{owner}} | {{status}} |

## Dependencies

<!-- WHAT  Structural relationships, with direction (inbound/outbound), type, the party, needed-by date,
           impact if missed, critical-path flag, and status.
     WHY   Direction and type drive the escalation path: an inbound external dependency is one you cannot
           control and must escalate; an outbound one is a risk you own for someone else. Critical-path
           dependencies gate the schedule. Deep dive: raid-log_companion.md section 3 (Dependencies).
     ASK   What does the project depend on or owe? Inbound or outbound? Type (third-party, cross-team,
           customer)? Party? By when? Impact if missed? On the critical path?
     PRIORITY  Mark direction and type. Name the specific party. Flag critical-path items. Order by
           needed-by date within direction.
     ROW HINT  A good row names direction, party, date, and impact. A weak row is "waiting on another team."
     GOOD  | D-01 | In | Cross-team | Platform team delivers the new query engine | 2026-08-01 | Delays all Saved Views work; on critical path | Platform team (Lee Zhang) | Confirmed |
     WEAK  | D-01 | | | backend | | | | |
     TRAP  Tracking only inbound. Outbound dependencies are risks you created for others; a missed one
           damages a partner and your credibility. -->

| ID | Direction | Type | Dependency | Needed by | Impact if missed | Party | Status |
|---|---|---|---|---|---|---|---|
| {{dependency_id}} | {{direction}} | {{type}} | {{dependency}} | {{needed_by}} | {{impact_if_missed}} | {{party}} | {{status}} |

## Review and Ownership

<!-- WHAT  The review cadence (whole-log and per-quadrant), the owner, the audience tiers, and the escalation
           and issue-handoff rules.
     WHY   Cadence is the operative variable; a basic log reviewed weekly beats a rich one reviewed monthly.
           At program scale, the delivery team sees the full log weekly and the steering group sees only the
           escalated rows, pre-read. Deep dive: raid-log_companion.md section 3 (Review and Ownership) and
           section 7.
     ASK   How often is the whole log reviewed, and by whom? Which quadrants move faster? Who owns the log?
           What does each audience see? When does an item escalate?
     GOOD  "Reviewed weekly by the PMO with workstream leads (full log), monthly deep dive at the program
           board. Issues updated as they move; risks and assumptions monthly. The program manager owns the
           log; each item has a named owner. The steering group sees only escalated rows, pre-read. Last
           reviewed 2026-07-20."
     WEAK  "Reviewed at meetings." (no cadence, tiering, or owner)
     TRAP  Handing a steering group the whole log. A committee given 60 rows reads none of them; give them
           the escalation view. -->

{{review_and_ownership}}

## Escalation and Aging

<!-- WHAT  The items currently escalated (needing a decision above the team), how long they have been
           escalated (aging), and the escalation path.
     WHY   Aging - how long an item has sat in "escalated" without a decision - is the single best measure of
           whether governance is actually deciding anything. A stale escalation is a governance failure, not
           a team failure. Deep dive: raid-log_companion.md section 4 and section 7 (the blame-register
           anti-pattern).
     ASK   Which items are escalated, and to whom? How long has each been escalated? What decision is each
           waiting on? What is the escalation path (team -> PM -> steering -> board)?
     PRIORITY  List only items needing a decision above the team. Show the age of each escalation. Escalate
           to RESOLVE, never to assign blame.
     ROW HINT  A good row names the item, the decision needed, who it is with, and how long it has waited. A
           weak row escalates without stating the decision required.
     GOOD  | ISS-11 | Decision: approve backfill contractor budget | Steering group | Escalated 12 days | Blocking the query-engine handover |
     WEAK  | ISS-11 | Escalated | | | |
     TRAP  Using the escalation list to target individuals. Escalation is for getting a decision, not
           assigning fault; the moment it is used to blame, people stop logging honestly. -->

{{escalation_and_aging}}

## Cross-Quadrant Summary

<!-- WHAT  The at-a-glance counts by quadrant and priority, and the MIGRATIONS between quadrants (assumptions
           that became issues, risks that became issues, dependencies that became risks).
     WHY   The migrations are the log's unique value: they show where the project's uncertainty is actually
           moving. A cluster of assumptions turning into issues means the team is planning on shaky ground.
           Deep dive: raid-log_companion.md section 3 (migration) and section 4.
     ASK   How many open items in each quadrant, by priority? Which items migrated this period (A->I, R->I,
           D->R)? What does the migration pattern tell you?
     PRIORITY  Keep it a summary, not a re-listing. The migration lines are the insight; the counts are
           context.
     ROW HINT  A good summary states counts plus a sentence on the migration pattern. A weak one is just
           totals with no interpretation.
     GOOD  "Open: 6 risks (1 high), 3 assumptions (1 low-confidence high-impact), 2 issues (1 high), 3
           dependencies (1 critical-path). Migrations this month: R-03 -> ISS-11 (key-person risk
           materialized). Watch: A-01 (vendor renewal) is the assumption most likely to migrate next."
     WEAK  "6 risks, 3 assumptions, 2 issues, 3 dependencies." (counts with no insight)
     TRAP  Turning the summary into a fifth copy of every item. It is a lens on the four quadrants, not a
           re-list of them. -->

{{cross_quadrant_summary}}
