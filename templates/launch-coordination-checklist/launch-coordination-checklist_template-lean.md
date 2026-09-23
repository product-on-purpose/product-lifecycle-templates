---
title: "{{checklist_title}}"
team_or_product: "{{team_or_product}}"
owner: "{{owner}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: launch-coordination-checklist
size: lean
source_template: launch-coordination-checklist
source_template_version: 0.1.0
---

<!--
LEAN LAUNCH COORDINATION CHECKLIST. The engineering-readiness core: what counts as a launch, the checks a
launch must clear, how it is staged and reversed, what blocks it, and what would make this checklist wrong.
Five sections, because a small launch needs the readiness discipline without a roster of named roles or a
communications plan. To add Roles and Decision Authority and Launch Communications, see
launch-coordination-checklist_template-full.md; ADD sections, never rename or reorder the ones below,
because the full variant is a strict superset of this one. One content difference travels with growing into
full: Go/No-Go Criteria below names the decision-maker directly; the full variant moves that naming into its
own Roles and Decision Authority section instead.

THIS CHECKLIST IS STANDING; WHAT YOU PRODUCE BY APPLYING IT IS NOT. The instrument you are filling in belongs
to a team and is reused launch after launch, the same way one Google Launch Coordination Engineer "ran 350
launches through the LCE Checklist" in 3.5 years. A single completed run of this checklist against one
specific launch is a per-launch record of applying the standing list, not a second kind of document. Update
this file when the checklist itself needs to change, not every time a launch happens. See
launch-coordination-checklist_companion.md section 1 and section 6.

LENGTH IS A DESIGN CONSTRAINT, NOT AN ACCIDENT. Google's own history records what happens when a checklist
grows unmanaged: "In an effort to curb its growth, at one point, adding new questions to Google's launch
checklist required approval from a vice president." Separately, aviation human-factors research on flight-
deck checklists found that "as the list of items grows, there may be a higher probability of overlooking any
given item". Both are named here as the discipline they come from, SRE practice and aviation design research,
because neither transfers automatically to software launches; a check earns its place by the failure it
prevents, and a check nobody can justify comes out. See launch-coordination-checklist_companion.md section 3
(Anatomy > Readiness Checks) and section 6.

THE READINESS CHECKS SECTION IS BUILT FROM CATEGORIES FOUND ACROSS SEVERAL SOURCES, NOT FROM GOOGLE'S OWN
APPENDIX. Google's Launch Coordination Checklist, the type's named origin, is licensed CC BY-NC-ND 4.0 with
no derivatives, so this template does not adapt its items or reproduce its structure. See
launch-coordination-checklist_companion.md section 2.

WHAT THIS CHECKLIST IS, AND IS NOT
It is the standing list a team consults before shipping an externally visible change, so readiness does not
depend on who happens to be asking the questions. It is NOT a per-launch to-do list invented fresh each time
(that is the record produced by applying it), NOT a runbook (a runbook responds to a situation that has
already happened and must encode branching judgment; this checklist prepares for an event that has not
happened yet), and NOT a definition of done (that is a standing, per-unit-of-work engineering quality gate,
necessary but not sufficient input to a full launch). See launch-coordination-checklist_companion.md
section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   launch-coordination-checklist_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the
   TRAP to avoid. For tables, PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Fill Scope and Launch Classes and Readiness Checks first;
   the rest depends on knowing what class of launch you are governing and what it must clear.
3. If a section does not apply to every launch class you named, say so inside that section rather than
   deleting the section; "N/A for Tier 3 launches, which skip this checklist entirely" is a legitimate,
   honest answer.
4. Before you ship it: self-grade against launch-coordination-checklist_guide.md, then DELETE every HTML
   comment. They are guidance, not content.
-->

# {{checklist_title}}

## Scope and Launch Classes

<!-- WHAT  What counts as a launch for this team, the classes of launch that exist, and which sections of
           this checklist each class actually requires, including whether the smallest class needs this
           checklist at all.
     WHY   Google's own working definition of the event this checklist governs is a useful default: "Google
           defines a launch as any new code that introduces an externally visible change to an application."
           Google's own history also tiers by risk rather than exempting by carve-out: low-risk launches
           "were faced with an almost trivial checklist, while higher-risk launches underwent the full gamut
           of checks and balances." Separately, by one point roughly a third of reviews were considered low
           risk. This section absorbs what an exemption section would otherwise carry, because exemption in
           the sources this bundle's research read is a property of the launch's class, not a standalone
           carve-out. Deep dive: launch-coordination-checklist_companion.md section 3 (Anatomy > Scope and
           Launch Classes) and section 6.
     ASK   What counts as a launch for this team? Follow Google's definition above if nothing narrower fits.
           What classes of launch exist, and what makes a launch fall into each one? Which sections of this
           checklist does each class actually require, and does the smallest class need this checklist at
           all?
     PRIORITY  Order classes from the one that requires the most of this checklist to the one that requires
           the least, so a reader scanning top to bottom sees the more demanding classes first.
     ROW HINT  A good row names a criterion someone else could check without asking the author who wrote it,
           and names required sections by their actual heading. A weak row has no distinguishing criterion,
           or lists sections as "everything" or "as needed."
     GOOD  | Tier 1 (new externally visible surface, or any change touching payment processing) | All
           sections in full |
     WEAK  | Standard launch | The usual checks | (no criterion anyone could check, and "the usual" names
           nothing)
     TRAP  If every launch your team has ever logged ends up in the same class, the class boundary is not
           doing any work and should be redrawn or dropped. -->

{{launch_definition}}

| Launch Class | Qualifying Criteria | Sections Required |
|---|---|---|
| {{launch_class}} | {{launch_class_criteria}} | {{launch_class_sections}} |

## Readiness Checks

<!-- WHAT  The checks a launch of this class must clear, grouped by area, each carrying the question, what
           actually answers it, the role that owns answering it, and why the check exists.
     WHY   Google's own unit for a checklist item is a question paired with an action, and its rule for
           which questions belong on the list at all is explicit: "Every question's importance must be
           substantiated, ideally by a previous launch disaster. Every instruction must be concrete,
           practical, and reasonable for developers to accomplish." What a completed check should say comes
           from the aviation human-factors literature on flight-deck checklists: "the response should always
           portray the actual status or the value of the item", not a bare "done." The WHO Surgical Safety
           Checklist's own design rule points the same way: "Every item on the Checklist must be linked to a
           specific, unambiguous action." This section's categories are built from structures found across
           several sources, never adapted from Google's own licensed appendix. Deep dive:
           launch-coordination-checklist_companion.md section 3 (Anatomy > Readiness Checks) and section 2.
     ASK   For each check: what is the question? What evidence actually answers it? Who owns answering it?
           Why is this check here, ideally pointing at a specific past failure it would have caught? If you
           cannot answer that last question, is this check earning its place?
     PRIORITY  Group areas in the order a reader would actually need them (dependencies and architecture
           before monitoring and rollout, for instance), and within an area, order checks by which would
           block the launch outright if unanswered.
     ROW HINT  A good row's "why" names the actual failure the check exists to prevent, not a generic reason
           like "best practice." A weak row has a plausible question with no evidence field and no owner,
           which makes it unanswerable by anyone but its author.
     GOOD  | Rollback capability | Can this change be reverted without a new deploy? | Feature flag exists
           and was toggled off in staging within the current release cycle | Feature owner | A prior release
           shipped with no flag and needed a full redeploy to revert |
     WEAK  | Rollback | Is it revertible? | Owner: Engineering. Status: Done. | (no name, and "done" is not
           an actual status)
     TRAP  Writing "done" instead of the item's current, actual status, or writing a check with a plausible
           question and no named owner. -->

| Area | Question | What Answers It | Owner | Why This Check Exists |
|---|---|---|---|---|
| {{readiness_area}} | {{readiness_question}} | {{readiness_evidence}} | {{readiness_owner}} | {{readiness_justification}} |

## Rollout and Rollback

<!-- WHAT  How the launch is staged, and the specific condition that reverses it, decided before the launch
           rather than argued during it.
     WHY   Google's own practice treats staged rollout as the default, not the exception: "Almost all
           updates to Google's services proceed gradually, according to a defined process, with appropriate
           verification steps interspersed." The same source adds, "Very few launches at Google are of the
           'push-button' variety". Where a staged rollout fails validation, the reversal is pre-decided: "If
           the change doesn't pass the validation period, it's automatically rolled back." A launch-day
           framework built around the same idea states the discipline directly: "Predeclare Rollback and
           Stop Triggers", with the instruction "Do not debate a clear hard trigger while impact grows.
           Abort first, then investigate". What happens without one is recorded in a real incident, where
           the emergency response itself made things worse: "As it turns out there was no kill switch". Deep
           dive: launch-coordination-checklist_companion.md section 3 (Anatomy > Rollout and Rollback) and
           section 7.
     ASK   How is this launch staged, all at once or gradually with verification steps between stages? What
           specific, measurable condition triggers a rollback, stated as a threshold you can check rather
           than a feeling that something is wrong? Who is authorized to pull it?
     PRIORITY  List the hardest, most automatic triggers first, the ones that should fire without a human
           deciding, then the triggers that require judgment.
     ROW HINT  A good row states a specific, measurable threshold and names who can act on it without further
           approval. A weak row is a feeling with no named authority.
     GOOD  | Error rate exceeds 2 percent of requests for 5 consecutive minutes on the launch dashboard |
           On-call engineer, no approval required |
     WEAK  | Roll back if things look bad | Whoever notices | (no threshold, no named authority)
     TRAP  A rollback trigger debated for the first time during an incident is functionally the same as
           having no trigger at all. A real incident's own retrospective conclusion on the risk of shipping
           without one: "Deployments need to be automated and repeatable and as free from potential human
           error as possible". -->

{{rollout_stages}}

| Rollback Trigger | Evidence Threshold | Authorized To Pull It |
|---|---|---|
| {{rollback_trigger}} | {{rollback_evidence}} | {{rollback_authority}} |

## Go/No-Go Criteria

<!-- WHAT  What blocks this launch outright, decided in advance, the current evaluation state of each
           criterion, how an accepted exception is recorded, and who makes the go/no-go call. This variant
           carries the decision-maker here directly rather than in a separate roles section, which is a
           reasonable compression once a launch is small enough not to need a named roster.
     WHY   The clearest sourced model for this section states four possible readings of a check rather than
           a binary pass or fail: "green: evidence is within the predeclared safe range; yellow: an accepted
           deviation requires explicit risk ownership; red: a hard gate failed; unknown: evidence is absent,
           delayed, or untrustworthy", with the explicit warning that "Unknown is not green." The same
           source states the rule for a missing prerequisite: "Either the prerequisite is met, an authorized
           time-bounded exception exists, or the decision is no-go", and names the anti-pattern this rule
           exists to prevent: "Executive override without ownership: a deadline silently replaces a hard
           gate." Where an exception is accepted, the instruction is to record it: "Record yellow-state
           acceptance, expiry, and decision authority." The decision-maker itself is named directly here
           because this variant has no separate roles section: the same source states "makes the go/no-go
           call for the current risk tier", with the instruction to "Name roles rather than inviting a large
           distribution list". Deep dive: launch-coordination-checklist_companion.md section 3 (Anatomy >
           Go/No-Go Criteria) and section 7.
     ASK   Who makes the go/no-go call for this launch, named by role rather than a distribution list? What
           conditions block this launch outright if unmet? For each one, what is the current state, green,
           yellow, red, or unknown, and what evidence supports that state? Where a deviation is accepted
           rather than blocking, who owns that acceptance and when does it expire?
     PRIORITY  List the criteria that would block the launch outright before the ones that could be waived
           with an accepted exception, so a reader sees the hard stops first.
     ROW HINT  A good row's evidence field names something a second person could go check themselves. A weak
           row's state is asserted with no evidence anyone else could verify.
     GOOD  | Load test against payment processing | Green | Load test run at 2x expected peak traffic,
           results attached | Platform lead |
     WEAK  | Load testing | Mostly fine | (no state, no evidence, no owner)
     TRAP  Treating an absent or delayed piece of evidence as a pass; "Unknown is not green." A deadline
           silently replacing a hard gate, with nobody owning that decision, is the named failure this
           section exists to prevent. -->

{{decision_maker}}

| Criterion | State | Evidence | Owner |
|---|---|---|---|
| {{gate_criterion}} | {{gate_state}} | {{gate_evidence}} | {{gate_owner}} |

{{exception_handling}}

## Review Trigger

<!-- WHAT  The event that would make this checklist wrong, and the named person or role expected to notice
           it. Not a calendar date alone.
     WHY   Google's own curation practice sets a floor, "Once or twice a year a team member reviews the
           entire checklist to identify obsolete items", and the same source records what happens when
           curation is neglected in the other direction: "In an effort to curb its growth, at one point,
           adding new questions to Google's launch checklist required approval from a vice president." A
           practitioner account of readiness-review practice warns against treating every incident as an
           automatic new line item: "With every incident that went awry, we would add a line item to our
           PRR process. Definitely do not do that, because you end up with this PRR process that's just
           monstrous and you cannot understand the underlying mechanisms." No structural source this
           bundle's research read publishes a section with this name or job; it is required directly by this
           family's contract, and this bundle labels it as its own contribution the way its sibling bundles
           in the same family label theirs. Deep dive: launch-coordination-checklist_companion.md section 3
           (Anatomy > Review Trigger) and section 6.
     ASK   What event would make this checklist wrong: a new failure class, a platform migration, a repeated
           near miss? Who owns noticing it? When an incident does prompt a look at this checklist, which
           specific mechanism failed, not merely that something went wrong, and is the fix a new check or
           something else?
     PRIORITY  Pair every date-based cadence with at least one event-based trigger. An event with no named
           owner is not a trigger, it is a hope.
     ROW HINT  A good row names a specific event, a named owner, and what they do about it: investigate
           which mechanism failed before deciding whether the fix is a new check. A weak row names only a
           calendar date.
     GOOD  | Two Tier 1 launches in one quarter needed an unplanned rollback for the same class of failure |
           Launch coordination lead | Investigate which existing check should have caught it before adding a
           new line item |
     WEAK  | Review this checklist annually | Team | Update if needed |
     TRAP  Adding a new checklist item for every incident without first asking which mechanism failed.
           Unmanaged, that growth is exactly what once required a vice president's approval to control. -->

| Event That Would Make This Wrong | Owner Who Notices | What They Do About It |
|---|---|---|
| {{review_event}} | {{review_owner}} | {{review_action}} |
