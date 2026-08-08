---
title: "{{team_name}} Definition of Done"
doc_type: definition-of-done
size: lean
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
LEAN DEFINITION OF DONE. The minimum a team needs for an honest, usable Definition of Done: who it binds,
what it requires, and what would make it stale. To grow it into a full Definition of Done (see
definition-of-done_template-full.md), ADD sections; never rename or reorder the ones below, because the
full variant is a strict superset of this one.

A DEFINITION OF DONE IS A COMMITMENT ATTACHED TO THE INCREMENT, NOT A STANDALONE ARTIFACT. That is a 2020
Scrum Guide change from how a lot of circulating material still describes it. Where an organizational
standard exists the Guide binds every team to it "as a minimum"; where none exists, the team creates its
own. Treating that minimum as a floor the team may raise is this library's reading, not Guide wording. Nobody owns this document alone: conformance sits with the Developers collectively,
and no source this library checked names a single accountable role. See definition-of-done_companion.md
sections 1 and 3.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   definition-of-done_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This is a standing document, revisited on the Review Trigger below, not written once and forgotten.
   Before you first share it: self-grade against definition-of-done_guide.md, then DELETE every HTML
   comment. They are guidance, not content.
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
           states, not activities.
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

## Review Trigger

<!-- WHAT  The event that should prompt someone to revisit whether this Definition of Done is still
           right, and who notices it, not a calendar reminder.
     WHY   Every source behind this bundle that discusses keeping a Definition of Done current reaches
           for a cadence or a ceremony; none supplies a condition, an event that makes the document
           wrong, plus a named person who notices. A standing document fails by drifting quietly out of
           date while everyone still believes it is current. Deep dive: definition-of-done_companion.md
           section 3 (Anatomy > Review Trigger).
     ASK   What event would make this document wrong (a new deployment target, a criterion waived
           repeatedly, a changed compliance requirement)? Who is the named person or role who notices it
           and brings it back to the team?
     GOOD  "Trigger: a criterion has been waived three times in one quarter, or the team adds a new
           deployment target. Noticed by: whoever logs the waiver flags it at the next retrospective for
           the team to amend this document."
     WEAK  "Reviewed every quarter." (a calendar reminder, not a condition; it decays into a ritual nobody
           reads and says nothing about who is responsible for noticing drift)
     TRAP  Writing a date-based cadence instead of a condition. A date is easy to write and easy to
           ignore once it passes unremarked; a named event is what someone can actually notice and act
           on. -->

**Trigger:** {{review_trigger_event}}
**Noticed by:** {{review_trigger_owner}}
