---
title: "{{project_name}} RAID Log"
project: "{{project_name}}"
raid_expansion: "Risks, Assumptions, Issues, Dependencies"
log_owner: "{{log_owner}}"
last_reviewed: "{{date}}"
review_cadence: "{{cadence}}"
status: "{{status}}"
doc_type: raid-log
size: lean
source_template: raid-log
source_template_version: 0.1.0
---

<!--
LEAN RAID LOG. The smallest real RAID log: what it covers and which expansion of RAID it uses, the four
quadrant tables (Risks, Assumptions, Issues, Dependencies), and the cadence that keeps it alive. Use it for
one team on one project. Often kept as one combined table; here the quadrants are separate sections because
they hold genuinely different fields. To grow it into a governance-grade log (see raid-log_template-full.md),
ADD sections and columns; never rename or reorder the ones below, because the full variant is a strict
superset of this one.

A RAID LOG IS A LIVING DOCUMENT, NOT A KICKOFF DELIVERABLE. Its defining failure is being set up at kickoff
and abandoned by week three ("documentation theater"). A RAID log is only as good as its review cadence.
Keep the last-reviewed date current. See raid-log_companion.md sections 1 and 7.

STATE YOUR ACRONYM. The A is Assumptions or Actions; the D is Dependencies or Decisions. Different teams mean
different things. This template uses Risks, Assumptions, Issues, Dependencies (stated in the frontmatter and
the scope line). Pick one expansion, write it down, and stop relitigating it. See raid-log_companion.md
section 6.

THE FOUR QUADRANTS ARE DIFFERENT KINDS OF THING. A Risk MIGHT happen; an Assumption is believed true without
proof; an Issue HAS happened; a Dependency is a structural relationship. They migrate: an assumption that
fails becomes an issue; a dependency that slips becomes a risk, then an issue; a risk that materializes
becomes an issue. See raid-log_companion.md section 3.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a companion pointer), guiding
   questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid. Tables add PRIORITY and ROW HINT.
2. Replace each {{placeholder}}. Give every item a unique ID and one named owner.
3. If a quadrant is empty, keep the heading and write "None open" - an empty Assumptions section is a claim,
   not an omission.
4. Never finished, but before you share it: self-grade against raid-log_guide.md, then DELETE every HTML
   comment.
-->

# {{project_name}} RAID Log

## Purpose and Scope

<!-- WHAT  What project this log covers, WHICH expansion of RAID it uses (say so), who owns the log, and the
           review cadence. One short block.
     WHY   The acronym is genuinely ambiguous, so the most useful line in a RAID log states what its letters
           mean here. Scope also says what does NOT belong, because an over-detailed log becomes clutter
           nobody can search. Deep dive: raid-log_companion.md section 3 (Purpose and Scope) and section 6.
     ASK   What project or program does this cover? Is the A Assumptions or Actions, the D Dependencies or
           Decisions? Who owns the log? How often is it reviewed? What is out of scope?
     GOOD  "RAID log for the Reporting Platform Modernization program. RAID = Risks, Assumptions, Issues,
           Dependencies. Owned by the program manager; reviewed weekly with workstream leads. Deep risk
           detail lives in the separate risk register."
     WEAK  "Project RAID log." (no expansion stated, no owner, no cadence, no scope; the team will track four
           different things under 'A')
     TRAP  Leaving the acronym undeclared. Half the team logs Assumptions under A and half logs Actions, and
           the log quietly means nothing. -->

{{purpose_and_scope}}

## Risks

<!-- WHAT  Things that MIGHT happen: a short risk statement, likelihood, impact, a response, an owner, a
           status. This is the summary view; deep scoring lives in a risk register if you keep one.
     WHY   The RAID log's R is the weekly working summary, not the audit-grade record. Keep it light and let
           it point to the risk register for detail. A risk that materializes is closed here and reopened as
           an Issue. Deep dive: raid-log_companion.md section 3 (Risks) and section 8 (vs the risk register).
     ASK   What might happen, and what would it do to the project? How likely and how bad (H/M/L or 1-5)?
           What is the response? Who owns it? Is there a fuller entry in the risk register?
     PRIORITY  Order by severity (likelihood x impact). Owner is one named person. If you keep a risk
           register, put its ID in the Ref column and do not duplicate the detail here.
     ROW HINT  A good row is a real cause-event-consequence statement with an owner and a response, not a
           theme label. A weak row is "vendor risk" with no owner.
     GOOD  | R-01 | Charting-library licence terms may change and force a re-platform, slipping launch | H | Mitigate: lock a 24-month licence | Dana Osei | Open | RR-01 |
     WEAK  | R-01 | Vendor | H | watch it | team | | |
     TRAP  Duplicating the whole risk register here. If you keep a register, the RAID R is a pointer, not a
           second copy that will drift out of sync. -->

| ID | Risk (cause -> event -> consequence) | Severity | Response | Owner | Status | Register ref |
|---|---|---|---|---|---|---|
| {{risk_id}} | {{risk_statement}} | {{severity}} | {{response}} | {{owner}} | {{status}} | {{register_ref}} |

## Assumptions

<!-- WHAT  Things the team is treating as TRUE without proof, each with the impact if it turns out false, a
           confidence level, and how/when it will be validated.
     WHY   An assumption is a latent risk in disguise: when it fails it becomes an issue (it has happened),
           and if merely thrown into doubt it first becomes a risk. The
           "impact if false" and "validate by" fields exist to catch that decay before it bites. This is the
           quadrant agile teams most often drop. Deep dive: raid-log_companion.md section 3 (Assumptions).
     ASK   What are we taking on faith? How confident are we? What happens to the project if it is wrong?
           Who validates it, and by when?
     PRIORITY  Order by impact-if-false. An assumption with high impact and low confidence is your most
           dangerous row. Give each a validate-by date, not just an owner.
     ROW HINT  A good row names a specific belief, the consequence if it is wrong, and a date by which you
           will know. A weak row is a vague hope with no validation.
     GOOD  | A-01 | The charting vendor will renew on current licence terms | Low confidence | Forces a re-platform (feeds R-01) | Validate by 2026-08-15 | Dana Osei | Open |
     WEAK  | A-01 | Everything will be fine | | | | | |
     TRAP  Logging assumptions once and never revisiting them. Assumptions decay; an unvalidated assumption
           is an issue waiting to happen. -->

| ID | Assumption | Confidence | Impact if false | Validate by | Owner | Status |
|---|---|---|---|---|---|---|
| {{assumption_id}} | {{assumption}} | {{confidence}} | {{impact_if_false}} | {{validate_by}} | {{owner}} | {{status}} |

## Issues

<!-- WHAT  Things that HAVE already happened and are affecting the project now: a description, a priority, an
           owner, a resolution plan, a raised date, and a status.
     WHY   An issue is not a maybe; the event has occurred, so it has no probability. It carries a RAISED
           DATE so you can measure how long it has been open (aging). When a risk materializes, close it and
           open a matching issue here. Deep dive: raid-log_companion.md section 3 (Issues).
     ASK   What has gone wrong? How bad and how urgent is it? Who owns the fix? What is the plan and the
           target date? When was it raised (for aging)?
     PRIORITY  Order by priority/urgency. Owner is one named person. The raised date is not decoration - a
           high-priority issue open for three weeks is a governance signal.
     ROW HINT  A good row describes what happened, the plan, the owner, and when it was raised. A weak row is
           a symptom with no owner or plan.
     GOOD  | ISS-11 | Query-engine lead left; handover incomplete (materialized R-03) | High | Pair a second engineer; document the engine | 2026-06-14 | Marta Reyes | Open |
     WEAK  | ISS-11 | Staffing problem | | fixing it | | |
     TRAP  Logging a potential future problem as an issue. If it has not happened yet, it is a risk. Mixing
           the two hides what needs action now. -->

| ID | Issue | Priority | Resolution plan | Raised | Owner | Status |
|---|---|---|---|---|---|---|
| {{issue_id}} | {{issue}} | {{priority}} | {{resolution_plan}} | {{raised_date}} | {{owner}} | {{status}} |

## Dependencies

<!-- WHAT  Structural relationships the project cannot proceed without: what you are waiting on (or owe),
           from/to whom, by when, and the direction (inbound or outbound).
     WHY   A dependency is not itself a threat; it is a relationship that can become a risk (if the other
           party is unreliable) or an issue (if a delivery is missed). Direction drives escalation: you can
           chase an inbound; an outbound is a risk you created for someone else. Deep dive:
           raid-log_companion.md section 3 (Dependencies).
     ASK   What does the project depend on, or owe? Is it inbound (you wait on it) or outbound (others wait
           on you)? Who is the party? By when? What if it is not delivered?
     PRIORITY  Mark direction (In/Out). Name the specific party, never "another team." Give a needed-by date.
           Flag critical-path dependencies.
     ROW HINT  A good row names the party, the direction, the date, and the impact if missed. A weak row is
           "waiting on backend" with no party or date.
     GOOD  | D-01 | In | Platform team delivers the new query engine | 2026-08-01 | Delays all Saved Views work | Platform team (Lee Zhang) | Confirmed |
     WEAK  | D-01 | | backend stuff | | | | |
     TRAP  Recording only inbound dependencies. Your outbound dependencies (what others wait on you for) are
           risks you own for someone else; track them too. -->

| ID | Direction | Dependency | Needed by | Impact if missed | Party | Status |
|---|---|---|---|---|---|---|
| {{dependency_id}} | {{direction}} | {{dependency}} | {{needed_by}} | {{impact_if_missed}} | {{party}} | {{status}} |

## Review and Ownership

<!-- WHAT  How often the log is reviewed, who owns it, and how items escalate. A few lines.
     WHY   Abandonment is the log's defining failure; a stated cadence and a named owner are what keep it a
           living tool. The consensus is a weekly working review plus a fuller monthly or stage-gate sweep,
           with different quadrants moving at different speeds. Deep dive: raid-log_companion.md section 3
           (Review and Ownership) and section 7.
     ASK   How often is the whole log reviewed, and by whom? Do any quadrants get updated more often (issues
           daily, risks monthly)? Who owns the log? When does an item escalate, and to whom?
     GOOD  "Reviewed weekly by the program manager with workstream leads; issues updated as they move, risks
           monthly. The program manager owns the log; each item has a named owner. Anything blocked or
           over-appetite is escalated to the steering group. Last reviewed 2026-07-20."
     WEAK  "Reviewed regularly." (no cadence, no owner, no escalation; this is how a RAID log dies)
     TRAP  A review that only reads the log aloud. The point is to move items - validate assumptions, chase
           dependencies, close issues - not to confirm the spreadsheet still exists. -->

{{review_and_ownership}}
