---
title: "{{team_name}} Definition of Done"
doc_type: definition-of-done
size: full
team: "{{team_name}}"
owner: "{{owner}}"
status: draft
doc_version: "{{doc_version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: definition-of-done
source_template_version: 0.1.0
---

<!--
FULL DEFINITION OF DONE. Every section, for when this Definition of Done has to gate more than one level
(feature, sprint, and release), has neighbors worth disclaiming explicitly because they keep getting
conflated with it, or the cost of an ambiguous "does not meet it" moment is high enough to write down in
advance. Most teams do not need this: reach for definition-of-done_template-lean.md first, and scale up
only when the scope in front of you actually earns it.

The full variant is a strict superset of the lean one: Scope and Ownership, Done Criteria, and Review
Trigger keep their names and order, and this file only ADDS Criteria by Level, What This Excludes, and
When Work Does Not Meet It, inserted between Done Criteria and Review Trigger.

A DEFINITION OF DONE IS A COMMITMENT ATTACHED TO THE INCREMENT, NOT A STANDALONE ARTIFACT. An
organizational standard, where one exists, is a floor: the team may strengthen it and may never weaken it.
Nobody owns this document alone: conformance sits with the Developers collectively, and no source this
library checked names a single accountable role. See definition-of-done_companion.md sections 1 and 3.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   definition-of-done_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid. For the table, PRIORITY explains the ordering and ROW HINT says what a
   good row contains.
2. Replace each {{placeholder}} with your content.
3. Do not pre-fill a full-only section out of diligence. Add one the moment a real question it answers
   comes up: the document has to gate more than one cadence, a neighbor keeps getting conflated with it,
   or an ambiguous failure moment is worth settling in advance. If a section does not apply, write "N/A"
   and one line of why.
4. This is a standing document, revisited on the Review Trigger below, not written once and forgotten.
   Before you first share it: self-grade against definition-of-done_guide.md, then DELETE every HTML
   comment.
-->

# {{team_name}} Definition of Done

## Scope and Ownership

<!-- WHAT  What this Definition of Done applies to (a story, a feature, a release) and who is bound by
           it. Whether it inherits an organizational standard, and if so, that it only adds to that
           standard and never subtracts from it.
     WHY   The Guide places conformance with "the Developers," not with a named role above them, and
           makes authorship contingent: an organizational standard, where one exists, binds every team as
           a minimum; where none exists, the team creates its own. For multiple teams sharing a product,
           there is one shared Definition of Done. Deep dive: definition-of-done_companion.md section 3
           (Anatomy > Scope and Ownership).
     ASK   Who is bound by this document? Does an organizational standard exist, and is it named here? If
           it exists, does everything below only add to it, never weaken it? If multiple teams share this
           product, is this the one Definition of Done they all use?
     GOOD  "Binds every Developer on the Saved Views team. Inherits the org-wide Engineering Definition of
           Done (linked) as a floor; the criteria below add two Saved-Views-specific checks and weaken
           none of the inherited ones."
     WEAK  "The team's quality bar." (names no one as bound, does not say whether an organizational
           standard exists, and gives a reviewer nothing to check the rest of the document against)
     TRAP  Naming a single owner, such as "the Product Owner owns this document." No source behind this
           bundle names a sole accountable role; conformance is collective, and authorship is contingent
           on whether an organizational standard exists. -->

{{scope_and_ownership}}

## Done Criteria

<!-- WHAT  The concrete conditions an increment must meet before it counts as done, written as verifiable
           states, not activities. If your list mixes feature-, sprint-, and release-cadence items, sort
           them in Criteria by Level below instead of flattening them here.
     WHY   This is the baseline shape every source behind this bundle carries in some form. "Code is good
           quality" and "testing done" are not verifiable on their own terms; write what someone can mark
           pass or fail. Deep dive: definition-of-done_companion.md section 3 (Anatomy > Done Criteria).
     ASK   Is each item a state someone can check, not an activity someone performs? Could a teammate who
           was not in the room mark each item pass or fail without asking you what you meant?
     GOOD  "- [ ] Unit tests pass on CI for every changed line. - [ ] Feature deployed to staging and
           verified by someone other than the author."
     WEAK  "- [ ] Code is good quality. - [ ] Testing done." (impressions, not checkable states; two
           different reviewers could disagree about whether either one is true)
     TRAP  Writing activities instead of states: "write tests," "do a review," rather than "tests pass on
           CI," "reviewed and approved." An activity can be performed badly and still get checked off; a
           state cannot. -->

- [ ] {{criterion_1}}
- [ ] {{criterion_2}}

## Criteria by Level

<!-- WHAT  The criteria from Done Criteria above, sorted by the cadence at which each one actually
           applies: feature, sprint, or release. A sorting rule, not a separate list of new criteria.
     WHY   A single flat list breaks down once a Definition of Done has to gate more than one cadence. The
           sorting rule is a decision tree: can this be done for every single feature? If not, every
           sprint? If not, it is a release-level activity. Leaving a release-only item at feature level
           does not make it happen more often; it makes the document one nobody can actually satisfy. Deep
           dive: definition-of-done_companion.md section 3 (Anatomy > Criteria by Level).
     ASK   For each criterion: can it realistically be done for every feature? If not, every sprint? If
           neither, is it recorded at release level, honestly, rather than left where it is convenient?
     PRIORITY  List rows in level order (feature, then sprint, then release), so the escalation is visible
           at a glance. This is a sorting rule, not a ranking of importance.
     ROW HINT  A good row names the criterion as a checkable state and the level it actually belongs at,
           not the level it was originally written at.
     GOOD  | Unit tests pass on CI | Feature | ... | Full regression suite passes | Sprint | ... | Third-
           party security audit completed | Release |
     WEAK  | Full regression suite passes | Feature | (promoted to a cadence the team cannot realistically
           meet on every feature; it will get waived quietly instead of gating anything)
     TRAP  Defaulting every criterion to feature level because that reads as the strictest option. It does
           not make the criterion happen more often; it makes the whole document infeasible. -->

| Criterion | Level |
|---|---|
| {{criterion_by_level}} | {{level}} |

## What This Excludes

<!-- WHAT  The boundary against the documents and mechanisms most often confused with a Definition of
           Done: Definition of Ready, a quality gate, coding conventions, and "done done."
     WHY   These four neighbors get conflated with the Definition of Done often enough to need a dedicated
           section rather than a footnote. A Definition of Ready gates entry into work, not exit from it.
           A quality gate is an automated, tool-checked pipeline checkpoint; a Definition of Done may cite
           one as a criterion without being one. Coding conventions are human-facing style guidance,
           unenforced by a compiler. "Done done" carries the same idea as an XP-era phrase, not a
           document. Deep dive: definition-of-done_companion.md section 3 (Anatomy > What This Excludes)
           and section 8 (Relationships to other artifacts).
     ASK   Have you named what this document is not? If your team also keeps a Definition of Ready, a CI
           quality gate, or a coding-conventions guide, does this section point to each one rather than
           silently absorbing or duplicating it?
     GOOD  "Not a Definition of Ready (that gates entry into a sprint; linked separately if your team
           keeps one). Not the CI quality gate (coverage and complexity checks feed 'CI green' as one
           criterion above; the gate itself lives in the pipeline config). Not our coding-conventions
           guide (style, unenforced by the compiler; linked separately)."
     WEAK  Leaving this section blank. (silence lets a reader assume this document is whichever neighbor
           they already know, which is exactly the conflation this section exists to prevent)
     TRAP  Folding a quality gate or a coding-conventions guide wholesale into this document instead of
           citing it as one line item above, or treating a Definition of Ready as the same artifact under
           a different name. -->

{{what_this_excludes}}

## When Work Does Not Meet It

<!-- WHAT  What happens to an increment that fails this Definition of Done: where the work goes and who
           decides it did not meet the bar.
     WHY   Partial completion is not partial credit. Work that does not meet the Definition of Done cannot
           be released or presented at the Sprint Review; it returns to the Product Backlog for future
           consideration, and it is normally not counted toward that sprint's velocity. Agreeing to the
           consequence before anyone has a stake in the answer is cheaper than agreeing to it during a
           disagreement. Deep dive: definition-of-done_companion.md section 3 (Anatomy > When Work Does
           Not Meet It).
     ASK   Where does unfinished work actually go? Who decides it does not meet the bar? Is that decision
           written down before it is ever contested?
     GOOD  "Work that does not meet this Definition of Done is not released and is not presented at the
           Sprint Review. It returns to the Product Backlog for future consideration, and is not counted
           toward this sprint's velocity."
     WEAK  "We will figure it out case by case." (no rule, which means the decision gets relitigated under
           pressure, exactly when it is hardest to agree on)
     TRAP  Skipping this section because the team has never yet failed its own Definition of Done. That is
           exactly backwards: the sentence is cheapest to write before anyone has a stake in the
           answer. -->

{{when_work_does_not_meet_it}}

## Review Trigger

<!-- WHAT  The event that should prompt someone to revisit whether this Definition of Done is still
           right, and who notices it, not a calendar reminder.
     WHY   Every source behind this bundle that discusses keeping a Definition of Done current reaches
           for a cadence or a ceremony; none supplies a condition, an event that makes the document wrong,
           plus a named person who notices. A standing document fails by drifting quietly out of date
           while everyone still believes it is current. Deep dive: definition-of-done_companion.md section
           3 (Anatomy > Review Trigger).
     ASK   What event would make this document wrong (a new deployment target, a criterion waived
           repeatedly, a changed compliance requirement)? Who is the named person or role who notices it
           and brings it back to the team?
     GOOD  "Trigger: a criterion has been waived three times in one quarter, or the team adds a new
           deployment target. Noticed by: whoever logs the waiver flags it at the next retrospective for
           the team to amend this document."
     WEAK  "Reviewed every quarter." (a calendar reminder, not a condition; it decays into a ritual nobody
           reads and says nothing about who is responsible for noticing drift)
     TRAP  Writing a date-based cadence instead of a condition. A date is easy to write and easy to ignore
           once it passes unremarked; a named event is what someone can actually notice and act on. -->

**Trigger:** {{review_trigger_event}}
**Noticed by:** {{review_trigger_owner}}
