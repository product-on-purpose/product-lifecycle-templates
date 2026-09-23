---
title: "{{project_name}} Issue Log"
project: "{{project_name}}"
log_owner: "{{log_owner}}"
issue_management_approach: "{{approach_doc_link}}"
last_reviewed: "{{date}}"
review_cadence: "{{cadence}}"
status: "{{status}}"
doc_type: issue-log
size: full
source_template: issue-log
source_template_version: 0.1.0
---

<!--
FULL ISSUE LOG. The governance-grade log: everything in the lean variant, plus a closed-issues audit trail
(resolution, confirmer, closed date, lesson learned) and a links-to-other-logs block tracing each issue back
to a risk it materialized from, a change request it raised, or a decision that closed it. Use it when issues
start resolving into other artifacts often enough that losing the trail matters, or when a governance board
will ask, weeks later, what was actually decided and why.

This is a STRICT SUPERSET of issue-log_template-lean.md: the first five sections are identical in name and
order, with the same table; full adds a governing-document field, fuller guidance in the shared sections,
and the last two sections. If you are growing from lean, add these; do not reorder.

WHAT AN ISSUE LOG IS, AND WHY THE FIRST SECTION MATTERS MOST. Published sources define "issue" four
different ways: PM2 and PRINCE2's 2009 glossary require something that has already happened; APM requires a
breach of delegated tolerance; PRINCE2 7 widens the definition to anything that could affect the project;
PMI's Lexicon requires neither an event nor a tolerance breach, only a current condition with impact. This
template does not pick a winner. It requires you to state your own threshold in the first section, because
two people keeping the same log will disagree about what belongs in it unless the team writes the line
down. See issue-log_companion.md section 6.

IT IS NOT A RISK REGISTER. A risk might happen; an issue already has, or is judged close enough to certain
to require action now. When a risk materializes, it becomes an issue, and the risk register entry closes as
occurred, linked both ways, never deleted; the link itself lives in Links to Other Logs below. See
issue-log_companion.md section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP; a
   scale or a record section adds PRIORITY and ROW HINT.
2. Replace each {{placeholder}}. The Issues table is the heart; give every row one named owner, never a
   role and never "the team".
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This document is never finished, but before you share it: self-grade against issue-log_guide.md, then
   DELETE every HTML comment. They are guidance, not content.
-->

# {{project_name}} Issue Log

## Purpose and Threshold

<!-- WHAT  A short statement of what counts as an issue on this project, the threshold that separates a
           logged issue from something the team just fixes in passing, what is explicitly out of scope
           (risks go to the risk register, software defects to the bug tracker, a boundary this library
           draws itself since no source read compares the two, and approved changes to change control),
           and which document governs the log's own rules.
     WHY   The sources genuinely disagree about what an issue even is, and none of the four positions is
           wrong: an event that has already happened, a tolerance breach, anything that could affect the
           project, or a current condition with impact. At governance scale, also name the plan that sets
           your threshold and escalation rules, since one methodology guide separates that plan from the
           register itself. Deep dive: issue-log_companion.md section 3 (Purpose and Threshold), section 5
           (the plan-and-register split), and section 6 (what an issue even is, stated four ways).
     ASK   Which threshold does this team use: already happened, a tolerance breach, or something else
           stated plainly? What size or duration moves a problem from "just fix it" to a logged issue?
           What is explicitly out (risks, defects, approved changes), and where does each of those live
           instead? Who owns the log itself? Which Issue Management Plan or equivalent document governs
           this log's threshold and escalation rules, and where does it live?
     GOOD  "An issue is any unplanned event that has already happened and cannot be resolved at the team
           level within three days. Something that might happen goes on the risk register; a software
           defect goes to the bug tracker; an approved change goes to change control. Owned by the program
           manager, governed by the Issue Management Plan linked above."
     WEAK  "Problems and blockers." (no threshold, no owner, no boundary against the other logs, no
           governing plan, so every row is a judgment call)
     TRAP  Borrowing PRINCE2 7's forward-looking definition, anything that could affect the project,
           without saying so. It pulls the concept toward the risk register's territory, and a reader
           comparing the two logs cannot tell which convention you used unless you state it. -->

{{purpose_and_threshold}}

## Priority Scale

<!-- WHAT  However this project ranks issues for attention, stated in words a second person would apply
           the same way to the same issue.
     WHY   The published sources split the scale three different ways: one methodology guide scores
           urgency and impact separately on parallel one-to-five scales; a government template instead
           names five impact levels outright plus a separate Material or Non-Material split; a third
           published log assesses impact against named cost, schedule, and quality dimensions directly.
           Deep dive: issue-log_companion.md section 3 (Priority Scale).
     ASK   Do you score urgency and impact separately, use named impact levels, or assess against named
           dimensions (cost, schedule, quality)? What does each level mean, concretely enough that two
           people would apply it the same way? Where do you draw the line for "escalate now"?
     PRIORITY  This is this template's own field, not a literal field name every source carries. One
           methodology guide's own plan text refers to a "priority" scale, but its log fields carry no
           field literally named priority, only urgency, impact, and size; do not claim a source names a
           field this template does not find in it.
     ROW HINT  A good scale level is anchored to something observable, for example "5 = Very high" paired
           with what that means for this project, or "5 = Catastrophic, affects cost, schedule, or scope
           enough to threaten the project." A weak scale level is a bare number with no anchor.
     GOOD  "Urgency 1 to 5 and Impact 1 to 5 (5=Very high, 4=High, 3=Medium, 2=Low, 1=Very low), scored
           separately; either scoring 4 or 5 triggers the escalation rule below."
     WEAK  "High / Medium / Low." (no anchors; two people will rate the same issue differently)
     TRAP  Naming a column "Priority" and citing a methodology guide for it, when that guide's own field
           list carries no field by that name. State your scale as your own choice. -->

{{priority_scale}}

## Issues

<!-- WHAT  The load-bearing table, one row per issue: an ID, an optional category, the issue itself
           (cause and impact, not a theme label), when and by whom it was raised, its priority, one named
           owner, the next action and its target date, its status, and when the row was last touched.
     WHY   Every published field list agrees on a small spine, ID, description, owner, and status, and
           diverges on everything else. This template gains a Last updated column beyond the fullest
           published field list, a field three independently published sources carry that it does not.
           Deep dive: issue-log_companion.md section 3 (Issues).
     ASK   For each issue: what happened, its cause, and its impact? Who raised it and when? What is its
           priority on the scale above? Who is the one named owner? What is the next action and its target
           date? What is its status (Open, Postponed, Resolved, Closed)? When was the row last updated?
           If it began as a category (problem, concern, opportunity, request for change, or
           off-specification), which one?
     PRIORITY  Order by priority, highest first, then by age within a priority. Owner is one named person,
           never a role and never "the team". Status is a small, stated set; keep it the same set you use
           in Escalation and Closed Issues below. When a status moves to Closed, move the row to Closed
           Issues rather than leaving it here.
     ROW HINT  A good row states cause and impact, not a theme; carries a named owner and a next action
           with a date; and its Last updated column moves every time someone touches it. A weak row is a
           one-word label with no owner, no action, and a Last updated column nobody has touched in months.
     GOOD  | ISS-07 | Supplier | Because the payroll vendor withdrew support for the file format our
           interface sends, February's payroll run needed a manual workaround and March's will fail without
           one | Priya Shah, 2026-02-17 | High | Tom Reid | Agree a format change or a support extension with
           the vendor; target 2026-03-06 | Open | 2026-02-24 |
     WEAK  | ISS-07 | Supplier | Payroll file broken | | High | IT | fixing it | Open | |
     TRAP  Logging a theme instead of a cause-and-impact statement, or leaving the owner as a team. An
           issue owned by "Engineering" is owned by no one. -->

| ID | Category | Issue (cause and impact) | Raised (by, date) | Priority | Owner | Next action (target date) | Status | Last updated |
|---|---|---|---|---|---|---|---|---|
| {{issue_id}} | {{category}} | {{issue}} | {{raised_by_date}} | {{priority}} | {{owner}} | {{next_action_target}} | {{status}} | {{last_updated}} |

## Escalation

<!-- WHAT  The rule that decides when an issue goes up, decided before it is needed, and the record of
           what has actually been escalated: to whom, when, and what decision is awaited.
     WHY   Every source that discusses escalation agrees it should happen and disagrees completely about
           the trigger: a role ladder with no timer, an aging clock that starts the day the issue is first
           logged, or a per-issue Yes/No flag against thresholds fixed in advance. No source reconciles
           these three shapes, so this template asks you to name the one you use rather than picking for
           you. Deep dive: issue-log_companion.md section 3 (Escalation) and section 6 (the escalation
           trigger debate).
     ASK   Which shape governs here: a role ladder, an aging clock, or a per-issue flag against a stated
           threshold? Who does an escalated issue go to next? What has actually been escalated, on what
           date, and what decision is the team waiting on?
     PRIORITY  State the rule once, in prose, before listing current escalations. Every escalated item
           needs a decision awaited, not just a status of "escalated"; escalate to get a decision, never to
           assign fault.
     ROW HINT  A good entry names the issue, who it went to, the date, and the decision awaited. A weak
           entry says "escalated" with nothing else.
     GOOD  "An issue goes to the program board when its resolution needs a decision above the project
           manager's authority. Currently escalated: ISS-07, to the program board on 2026-03-02, awaiting a
           decision to extend the vendor's support contract by one quarter."
     WEAK  "Escalated when needed." (no rule, no record, no decision named)
     TRAP  Using the escalation record to name who caused the issue rather than what decision is needed.
           That turns a request for a decision into an accusation, and the decision is what the board can
           give. -->

{{escalation}}

## Review and Ownership

<!-- WHAT  The stated review cadence, who owns the log itself, and which issues get looked at first.
     WHY   Practitioners genuinely disagree on cadence: two authors of the same article disagree with each
           other, one reviewing weekly and the other saying issues should be discussed almost every day. A
           government issue-management plan instead settles on weekly with severity-first triage. This
           template reports the disagreement rather than resolving it; state your own cadence instead of
           assuming one. Deep dive: issue-log_companion.md section 3 (Review and Ownership) and section 6
           (review cadence).
     ASK   How often is the log reviewed, and by whom? Which issues get looked at first (severity,
           escalated status, age)? Who owns the log day to day, separate from who owns any one issue?
     GOOD  "Reviewed weekly by the PMO; review priority goes to high-severity and escalated issues first.
           Log owned by the program manager. Last reviewed 2026-07-20."
     WEAK  "Reviewed regularly." (no cadence, no owner, no triage order; this is how a log quietly stops
           being read)
     TRAP  Treating the review as a calendar formality nobody actually does. One source names exactly this
           failure: the review "gets neglected when project managers get busy." -->

{{review_and_ownership}}

## Closed Issues

<!-- WHAT  The audit trail: issues that have been resolved and then closed, who confirmed the closure,
           when it closed, and any lesson worth keeping. Keep them; do not delete.
     WHY   Resolved and Closed are not the same state, and conflating them is one of this artifact's live
           definitional gaps. One methodology guide defines Closed as "all work is completed and verified";
           a government issue-management plan puts a second person, the issue's originator, in the loop to
           verify a resolved issue before it can be closed. This template defines both terms itself and
           says so, rather than presenting the split as settled industry consensus. Deep dive:
           issue-log_companion.md section 3 (Closed Issues) and section 6 (Resolved and closed).
     ASK   For each closed issue: what was the resolution? Who confirmed it, and is that person different
           from who did the fix? When did it close? Is there a lesson worth recording, and where does the
           procedure for capturing it live?
     PRIORITY  Keep closed rows for the life of the log; do not delete them. The confirmer is a person
           different from whoever did the fix, per this template's own definition of Closed. A lesson is
           optional per row, but note its absence rather than omitting the row.
     ROW HINT  A good closed entry names the fix, a confirmer distinct from the fixer, a closed date, and
           a lesson if one exists. A weak entry is a status flip with no confirmer and no date.
     GOOD  "ISS-07: vendor support extended one quarter and the interface moved to the new file format;
           March payroll ran without a workaround. Confirmed by Priya Shah (who raised it, not who fixed it),
           closed 2026-03-31. Lesson: supplier contracts now require notice before a format is withdrawn."
     WEAK  "ISS-07: closed." (no resolution, no confirmer, no date, no lesson)
     TRAP  Letting the person who did the fix also confirm the closure. That collapses Resolved and Closed
           into one step and defeats the reason this section exists. -->

{{closed_issues}}

## Links to Other Logs

<!-- WHAT  Each issue's origin and hand-offs: the risk it materialized from, if any; the change request it
           raised and to which convention; the decision that closed it; and the tasks that implement its
           fix.
     WHY   This is one methodology guide's Traceability field made explicit as its own block. A risk that
           materializes into an issue closes its register entry as occurred, which is what preserves the
           evidence that the event was foreseen, rather than being deleted or quietly marked withdrawn; the
           link runs both ways. Separately, whether a request for change is an issue is a live,
           unreconciled split: one method folds it into the issue concept outright (not all issues result
           in changes, but all changes start as issues), another names a separate change log for submitted
           change requests and states no rule for the overlap. This template records whichever convention
           your team follows. Deep dive: issue-log_companion.md section 3 (Links to Other Logs), section 6
           (whether a request for change is an issue), and section 8 (Relationships to other artifacts).
     ASK   Did this issue start as a risk? If so, which register entry, and has that entry been closed as
           occurred with a link back here? Did it raise a request for change, and under which convention
           (recorded here, or handed to a separate change log)? What decision, if any, closed it, and where
           is that decision recorded? Which tasks implement its fix?
     PRIORITY  Link by ID in both directions; never duplicate another log's detail here. An issue with no
           origin risk, no change request, and no decision link simply says "None" in each column rather
           than being left blank.
     ROW HINT  A good entry names the origin risk (or "None"), the change request raised (or the
           convention followed if none was raised here), the decision that closed it, and the implementing
           tasks. A weak entry leaves every link blank.
     GOOD  "ISS-07 originated from risk register entry R-12, which closed as occurred on 2026-02-17 with a
           link back to ISS-07. Raised change request CR-05 (move cutover by two weeks). Closed by decision
           D-09 (program board, 2026-03-16). Implementing tasks: T-41, T-42."
     WEAK  "ISS-07: linked to some other stuff." (no IDs, no direction, nothing a reader could follow)
     TRAP  Duplicating the risk register's or change log's own detail here instead of linking to it. This
           section is a cross-reference, not a second copy of another log's record. -->

{{links_to_other_logs}}
