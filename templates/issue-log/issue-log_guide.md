# Guide: Issue Log (operator card)

Fast reference for using the issue-log bundle. For the full reasoning, history, and sources, read
[`issue-log_companion.md`](issue-log_companion.md).

## When to use

- Something has **already happened** on your project or program, is not resolving itself in the normal
  course of work, and needs a named person to own getting it fixed.
- You need **one written record** of what the problem is, who owns it, whether it has gone up to someone
  above the day-to-day work, and when it is genuinely closed rather than just quiet.
- More than one person needs to see the same status: a team lead, a sponsor, a steering group, or whoever
  picks it up next if the current owner leaves.
- Issues are starting to **resolve into other artifacts** often enough that losing the trail matters: one
  began as a risk that materialized, one raised a change request, one needs a governance decision on
  record. That is the signal to move from lean to full (see Pick a variant, below).

## When NOT to use

- **The problem has not happened yet.** Something that might happen belongs on the risk register, not
  here; an issue log tracks things that have occurred or are close enough to certain that waiting no
  longer makes sense. A row describing a future possibility is misfiled.
- **You also need to track assumptions and dependencies alongside issues.** Use a RAID log as the one
  working document; the issue log is the deepened, standalone form of its Issues quadrant, worth splitting
  out only once that quadrant has outgrown the RAID log's single row per item.
- **It is a software defect with no project-management dimension.** Route it to the bug or ticket tracker
  instead. No source this bundle read compares a project issue log with a software tracker directly, so
  that boundary is this library's own judgment, not a sourced rule; if your team already manages defects
  as issues on purpose, say so in Purpose and Threshold rather than silently mixing populations.
- **The problem resolves inside the team well under your stated threshold.** Logging every small thing a
  team fixes in passing turns the log into noise nobody reads. The Purpose and Threshold section exists
  precisely so the team can say where that line sits, rather than every reader guessing at it.

## Issue log, risk register, or RAID log? (the question people actually have)

| | **Issue log** | **Risk register** | **RAID log** |
|---|---|---|---|
| Tracks | Problems that have already happened | Risks: things that might happen | Risks + Assumptions + Issues + Dependencies |
| Time frame | Has happened, or close enough to certain | Might happen | Mixed |
| Cadence | Near-daily to weekly, by severity | Weekly to quarterly, by scale | Weekly working document |
| Audience | Whoever must resolve it now | Owners, steering group, board | The delivery team |
| Relationship | The deepened, standalone form of RAID's Issues quadrant | The deepened, standalone form of RAID's Risks quadrant | The consolidation layer |

They are a system, not a competing choice. When a risk materializes, it becomes an issue: the register
entry closes as occurred rather than being deleted, and the new issue-log row links back to it. A RAID
log's Issues column is the same population an issue log holds, formalized; move to a standalone issue log
once that quadrant needs its own escalation history, closure audit trail, and links to the logs it started
from or fed into.

**The change-control fork is worth naming on its own**, because the sources genuinely split on it. One
convention treats a request for change as a kind of issue: every change starts as an issue, though not
every issue becomes a change, and the change stays on this log. The other convention keeps a separate
change log for submitted change requests and states no rule for where the two overlap. Either is
defensible; record which one your team follows in Links to Other Logs (full) so a reader does not have to
guess.

## Pick a variant

- **Lean** (default): Purpose and Threshold, Priority Scale, Issues, Escalation, Review and Ownership. A
  complete working log a team can populate and review from week one. It is enough for a project whose
  issues resolve inside the team, without a change-control hand-off or a lessons-learned record to keep.
- **Full**: adds **Closed Issues** (resolution, a confirmer distinct from the fixer, closed date, lesson
  learned) and **Links to Other Logs** (origin risk, change request, decision, implementing tasks). Move to
  full once issues start resolving into other artifacts often enough that losing the trail matters: a
  materialized risk whose register entry needs to close as occurred, a request for change your convention
  routes through this log, or a governance board that will ask, weeks later, what was actually decided.

Grow lean into full by adding the two sections; the first five sections keep their name and order. The
scaling signal is **how often issues hand off to another artifact**, not how large the project is.

## Quality rubric (self-grade)

Score each row 0, 1, or 2. Below 13 out of 18, the log will not survive its first real review: the first
person who reads it closely will find a row with no owner, no threshold, or no decision behind an
escalation.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **States its own threshold** | No line saying what counts as an issue here | A line exists, but it is too vague for two people to apply the same way | A stated threshold (an event, a tolerance breach, or a condition) with a size or duration test, plus what is explicitly out and where it goes instead |
| 2 | **Priority scale is anchored** | Bare High / Medium / Low, or a number with no meaning attached | Named levels exist, but two people would still rate the same issue differently | Every level is anchored to something observable for this project, and the scale states what triggers escalation |
| 3 | **One named owner** | No owner column, or owner is a role or "the team" | A person is named on some rows, a role or team on others | A specific individual is named on every open row, and is the person actually accountable for resolving it |
| 4 | **States cause and impact** | A one-word label ("Vendor", "Export broken") | Cause or impact is present, not both | A reader who was not there can tell what broke, why, and what it threatens, from the row alone |
| 5 | **Rows stay current** | No Last updated column, or every row carries its creation date regardless of activity | Some rows are current, others are stale with no way to tell which | A reviewer can open the table and find no row whose real status changed more recently than its recorded update |
| 6 | **Escalation has a rule** | No rule stated; escalations, if any, have no decision named | A rule is named in general terms, but current escalations do not say what is being decided | The shape (a role ladder, an aging clock, or a per-issue flag) is named, and every escalated row shows who it went to and the decision awaited |
| 7 | **Review is current** | No cadence and no named log owner | A cadence is named, but the last-reviewed date is older than the stated cadence allows | Cadence, triage order, and log owner are all named, and the last-reviewed date is inside that cadence window |
| 8 | **Closure is confirmed independently** *(full)* | Closed rows show a status flip with no confirmer and no date | A confirmer or a date is recorded, but the confirmer is the person who did the fix | Every closed row names a confirmer distinct from the fixer, a closed date, and either a lesson or a stated reason none applies |
| 9 | **Links are traced** *(full)* | The section is blank or missing | Links are named but lack a direction or an ID, or another log's own detail is copied in here | Every issue's origin risk (or "None"), change request, closing decision, and implementing tasks are named by ID, and a reader can follow each one back to its own log |

### Rubric scope by variant

| Variant | Rows scored | Maximum | Threshold |
|---|---|---|---|
| lean | 1-7 | 14 | 10 |
| full | all 9 | 18 | 13 |

Lean ships no Closed Issues or Links to Other Logs section, so rows 8 and 9 grade content it does not
carry; score lean against rows 1 through 7 only. A lean log at 10 out of 14 clears a comparable bar to a
full log at 13 out of 18.

## Named anti-patterns (the usual wrecks)

1. **No owner.** A row assigned to "Engineering" or "the team" is assigned to no one, and an issue with no
   owner is unlikely ever to get resolved. Fix: one named individual, on every row, before it goes further.
2. **Nobody reviews it.** The review is the task that quietly gets skipped when the people running the
   project get busy, so the log keeps existing while it stops being read. Fix: a stated cadence, and a
   named person who runs the review and records its date.
3. **Raised late.** Reluctance, or simply a lack of time, keeps an issue off the log until it is already
   serious. Fix: log it the moment it meets your stated threshold.
4. **Decided badly once it arrives.** Getting an issue to governance is not the same as getting a good
   decision from it; a board can still fail to address the root cause and treat only the symptom in front
   of it. Fix: escalate with a proposed solution, not a bare problem, so the decision has something to act
   on.
5. **Aging without movement.** A row nobody has touched in months is a row nobody is actually working, no
   matter what its status says. Fix: the Last updated column this template carries beyond some published
   field lists, and a review that actually looks at stale rows rather than only new ones.
6. **Escalation used to assign blame.** An escalation record that names who caused a problem, instead of
   what decision is needed, has stopped being a request for a decision. Fix: escalate to get a decision,
   never to assign fault.
7. **Resolved treated as Closed.** These are not the same state: Resolved means the work is done, Closed
   means someone other than the person who did the fix has verified it. Collapsing them into one step
   removes the check the second state exists for. Fix: keep the states distinct, and name who confirms
   closure separately from who performed it.

## No paired skill (yet)

There is **no `deliver-issue-log` or `govern-issue-log` skill** in the product-on-purpose org today, so
this bundle's `pairs_with` is empty. Until one exists, this template is filled by hand.
