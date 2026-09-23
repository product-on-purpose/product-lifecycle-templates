# Guide: Launch Coordination Checklist (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`launch-coordination-checklist_companion.md`](launch-coordination-checklist_companion.md). A fully worked
instance is
[`launch-coordination-checklist_example.md`](launch-coordination-checklist_example.md).

## When to use

- You are about to ship a change that is externally visible, and you want readiness to depend on the
  checklist, not on which engineer happens to be asking the questions that day.
- More than one launch will consult this same list. It is a standing instrument, reused launch after launch,
  the same way one Google Launch Coordination Engineer ran 350 launches through one checklist over 3.5
  years, not a document invented fresh for this one launch.
- You want the conditions that block a launch, and the condition that reverses it, settled before the launch
  rather than argued while it is happening.
- The launch reaches past one team, support, documentation, or a public announcement, and you need to name
  who is prepared before those audiences learn about it.
- You are not sure yet what counts as a launch for your team, or whether every launch needs the same amount
  of scrutiny. Scope and Launch Classes exists to answer exactly that.

## When NOT to use

- **The change is small and stays inside one team.** The paired pm-skills skill for this type names the
  failure mode directly: "a launch checklist adds ceremony without value; track it in the sprint instead."
  If nothing here would change what you check, you are paying ceremony for no readiness gain.
- **You are responding to a situation that has already happened, not preparing for one that has not.** A
  checklist is linear: it verifies known, named prerequisites before a decision point. A runbook has to
  encode branching judgment instead, what to check first, what to avoid, when to branch, and when to
  escalate. If the document you are writing needs that kind of branching, write a runbook.
- **You want a standing quality bar every unit of work is judged against, not a readiness gate for one
  external launch.** That is a definition of done, an agreed-upon set of items that must be completed before
  a project or user story can be considered complete. A definition of done is necessary but not sufficient
  input to a launch; it is not a substitute for this document, and this document is not a substitute for it.
- **You need a dated, per-launch execution document with owners and target dates for one specific release.**
  That is what applying this standing checklist produces, not the checklist itself. If your team already
  tracks that per-launch work in an issue tracker, owners, deadlines, and status per task, adding a second,
  parallel document duplicates what the tracker already shows rather than adding readiness.
- **You only need to draft the customer-facing announcement of what shipped.** That belongs in a release
  notes document. This checklist tracks that the right people saw the announcement before it went out, it
  does not draft it.

## Pick a variant

**Lean (five sections)** is the default: Scope and Launch Classes, Readiness Checks, Rollout and Rollback,
Go/No-Go Criteria, Review Trigger. It keeps the engineering-readiness core intact and carries the launch's
decision-maker inside Go/No-Go Criteria rather than giving roles their own section. The type's own origin,
Google's launch checklist, is engineering-only, and a small launch needs to know who decides more than it
needs a roster.

**Full (seven sections)** adds Roles and Decision Authority and Launch Communications. Both additions are
cross-functional rather than engineering-internal. Move to full when at least one of these is true:

- more than one role could plausibly make the go/no-go call, so naming a single decision authority in
  writing, separate from Go/No-Go Criteria, is worth its own section;
- the launch reaches support, documentation, or a public announcement, not just engineering, so someone
  needs to be told what to prepare before the public is;
- the launch is regulated or cross-functional enough that legal, compliance, or marketing stakeholders need
  a named place in the document rather than an assumption that someone told them.

Every lean heading appears in full unchanged, in the same order. Growing from lean to full is additive; you
never reorder or rename a section you already filled in. The one content change that travels with the move:
Go/No-Go Criteria stops naming the decision-maker itself once Roles and Decision Authority exists to carry
that role.

## Quality rubric (self-grade)

Score each 0, 1 or 2. Full below 10 out of 14 ships a checklist that a launch can clear while still carrying
the exact kind of gap a 2012 trading-system deployment failure exposed: no named second reviewer, no
rollback trigger decided in advance, or a go/no-go call nobody in particular owns. Lean is scored on five of
these rows only (see the scope table below), and below 7 of 10 a lean checklist can still clear a launch
with no rollback trigger decided in advance, or with a go/no-go call nobody in particular owns.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Launch class criteria** | No classes named, or every launch this team has ever logged lands in the same one | Classes are named, but the criterion for landing in one is a feeling, "standard launch," nobody else could check | Each class has a criterion a second person could apply without asking the author, and names which sections of this checklist that class actually requires |
| 2 | **Named decision authority** *(full)* | No decision-maker named, or a channel or distribution list stands in for one | A role is named, but no other reviewer is required in writing before that role's call | A specific role is named as the one who calls go or no-go, and a separate reviewer is required in writing, so no single unreviewed person can approve the launch alone |
| 3 | **Actual-status evidence** | Rows carry a question and nothing else, or the evidence field just says "done" or "complete" | Some rows name what evidence answers the question and who owns it; others stop at a bare status word | Every row names what actually answers the question, who owns answering it, and the specific failure the check exists to catch |
| 4 | **Advance communications** *(full)* | Section missing, or it only describes the public announcement | An audience is named, but not what they are told before the launch, or the timing is "at launch" | Support and documentation are told what they need before the launch, with a stated timing, and the customer-facing announcement is explicitly pointed at release notes instead |
| 5 | **Measurable rollback trigger** | No trigger stated, or "roll back if it looks bad" | A trigger is named, but as a description rather than a number, or no one is named who can pull it without asking | A specific, measurable threshold is stated, and a named role can pull it without further approval |
| 6 | **Owned, expiring exceptions** | Criteria are pass or fail only, with no way to record an accepted exception | Exceptions can be recorded, but absent or delayed evidence is treated the same as a pass, or an exception carries no expiry | Absent evidence is explicitly not counted as a pass, and every accepted exception names who owns it and when it expires |
| 7 | **Event-based review trigger** | Only a calendar cadence, or nothing at all | An event is named, but with no owner, or no stated next action | A specific event is paired with a named owner, whose first move is to investigate which check should have caught it, before deciding whether the fix is a new line item |

**Which rows apply to what.**

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| full | all 7 | 14 | **10** |
| lean | 1, 3, 5, 6, 7 | 10 | **7** |

Rows 2 and 4 are scored only against full. Lean ships neither Roles and Decision Authority nor Launch
Communications, it folds the decision-maker into Go/No-Go Criteria instead, so grading it on those two rows
would penalise the choice of variant rather than the quality of the document.

The test behind every cell above: **could someone satisfy it without improving the document?** A row that
counted readiness-check rows, named audiences, or listed classes would reward padding. Every cell instead
asks whether a specific piece of evidence exists, and whether a second person, not the author, could check
it without asking who wrote the document.

## Named anti-patterns (the usual wrecks)

1. **No named second reviewer.** A 2012 trading-system deployment failure shipped because no written
   procedure required a second technician to review the deployment, so nobody caught that old code had not
   been removed from one of the servers. Roles and Decision Authority exists to make that requirement
   explicit rather than assumed.
2. **No rollback trigger decided in advance.** The same incident's emergency response made things worse
   because there was no kill switch decided ahead of time. A trigger argued for the first time during an
   incident is functionally the same as having no trigger at all.
3. **Unbounded checklist growth.** Left uncurated, a checklist can grow to the point that Google's own
   history records: at one point, adding a new question to its launch checklist required approval from a
   vice president just to control the list's size.
4. **A per-incident append loop.** Adding a new checklist line item for every incident that goes wrong, with
   no check on whether the mechanism actually failed, produces a checklist so large nobody can trace a given
   line back to the reason it exists. The fix is to ask which specific check should have caught the
   incident, not whether an incident happened at all.
5. **A response that says "done" instead of the actual status.** Aviation checklist design exists precisely
   against this failure: a completed item's response should portray its actual current status or value, not
   a bare confirmation that something was attempted.
6. **Treating an absent or delayed piece of evidence as a pass.** Missing evidence is not the same thing as
   a satisfied check. A criterion with no evidence yet is unknown, and unknown is not the same as green.
7. **An executive override with no owner.** A deadline silently replacing a hard gate, with nobody named as
   the one who accepted that tradeoff, is the specific failure Go/No-Go Criteria's exception field exists to
   prevent.
8. **Readiness treated as permanent once granted.** A service, or a launch, that was ready three months ago
   might no longer be ready. Readiness is version-bound: a change to the product, the environment, or a
   dependency can invalidate an earlier answer without anyone updating the record.

## Pairing with your process

This bundle ships in the `standing-standards` family alongside `definition-of-done`, `definition-of-ready`
and `runbook`. All four are agreed once and consulted repeatedly rather than authored per occasion, but they
answer different questions: a definition of done is a standard a team is judged against, a definition of
ready is the agreement on when a backlog item can be pulled into a sprint, a runbook is a procedure executed
once a known situation has already happened, and this checklist is consulted at the moment of a launch
decision that has not happened yet. Keep the boundaries where they belong: this document does not certify
that a unit of work is finished, and it does not tell a responder what to type once something has gone
wrong. Where your team already runs the paired pm-skills `deliver-launch-checklist` skill for one specific
release, this standing list is what that per-launch document draws its Go/No-Go Criteria and Rollback Plan
from; update this file when the checklist itself needs to change, not every time a launch happens.
