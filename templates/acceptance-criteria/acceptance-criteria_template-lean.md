---
title: "{{title}}"
doc_type: acceptance-criteria
size: lean
owner: "{{owner}}"
status: draft
doc_version: "{{doc_version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: acceptance-criteria
source_template_version: 0.1.0
---

<!--
LEAN ACCEPTANCE CRITERIA. A short, rule-based checklist for one story: the conditions that must be
true for it to be accepted. Use this for a straightforward story. To grow it into full criteria, ADD
sections (see acceptance-criteria_template-full.md); never rename or reorder the ones below (the full
variant is a strict superset of this one). Write criteria as observable outcomes, from the user's
point of view, not as implementation steps.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   acceptance-criteria_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a
   WEAK example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you ship: self-grade against acceptance-criteria_guide.md, then DELETE every HTML comment.
   They are guidance, not content.
-->

# {{title}}

## Story reference

<!-- WHAT  Which user story or backlog item these criteria gate: a link, or the story statement
           itself. Name the user and the goal.
     WHY   AC are meaningless without the story they accept; "accepted into what" must be
           unambiguous. Deep dive: acceptance-criteria_companion.md section 3 (Anatomy > Story
           reference).
     ASK   Which story do these gate? Is it linked or quoted so a reviewer can find it? Are the user
           and goal clear?
     GOOD  "As a recurring analyst, I want to set one of my saved views as the default for a
           dashboard, so that the dashboard opens the way I work instead of in its generic default
           state. (See user-stories_example.md.)"
     WEAK  "Saved views feature." (no user, no goal, no link; a reviewer cannot tell what is being
           accepted)
     TRAP  Free-floating criteria with no parent story. -->

{{story_reference}}

## Acceptance criteria

<!-- WHAT  The rule-based conditions that must hold for the story to be accepted, as a checklist of
           observable, pass/fail outcomes.
     WHY   Discrete rules are clearest as a list, and each must be markable pass or fail; a criterion
           you cannot mark is not finished. Deep dive: acceptance-criteria_companion.md section 3
           (Anatomy > Acceptance criteria).
     ASK   Is each row a single verifiable claim? Could QA mark it pass or fail as written? Is it what
           the user observes, not how it is built?
     GOOD  "Marking a new view as default un-marks the previous default automatically."
     WEAK  "Defaults are stored efficiently in a Redis cache." (implementation detail, not an
           observable outcome the user can verify)
     TRAP  Implementation, not behavior: criteria that describe how it is built rather than what the
           user can observe. -->

- [ ] {{criterion_1}}
- [ ] {{criterion_2}}

## Out of scope and notes

<!-- WHAT  What these criteria deliberately do not cover, plus assumptions and links to adjacent
           stories.
     WHY   It lets a reviewer tell an omission from a decision. Deep dive:
           acceptance-criteria_companion.md section 3 (Anatomy > Out of scope and notes).
     ASK   What did you choose not to cover? What assumptions do the criteria rest on? Where do
           adjacent concerns live?
     GOOD  "Out of scope: team-level defaults (a Team Lead setting a default for everyone) are a
           separate, open decision. Assumes per-user preference storage (shipped Q1)."
     WEAK  Leaving this blank. (silence on scope makes an omission read as a deliberate decision)
     TRAP  No scope statement, so omissions read as decisions. -->

{{out_of_scope_and_notes}}
