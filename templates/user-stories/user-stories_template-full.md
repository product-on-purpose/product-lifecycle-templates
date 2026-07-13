---
title: "{{title}}"
doc_type: user-stories
size: full
owner: "{{owner}}"
status: draft
doc_version: "{{doc_version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: user-stories
source_template_version: 0.1.0
---

<!--
FULL USER STORY. A story with quality scaffolding around it, and a strict superset of the lean card:
the same Story, Acceptance criteria, and Notes sections, with Description, INVEST, estimate, and
dependencies added between them. Use it for a story that carries risk, crosses teams, or must be sized
and de-risked before commitment. For a set, repeat this block per story under a shared epic heading.
Default to the lean card and scale up only when a section here earns its place.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   user-stories_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content. For the INVEST check, tick each box or note the gap.
3. Do not pre-fill a section out of diligence. Add a full-only section the moment a real question it
   answers comes up (a dependency appears, the story needs sizing, a sibling blocks it). If a section
   does not apply, write "N/A" and one line of why.
4. Before you ship: self-grade against user-stories_guide.md, then DELETE every HTML comment.
-->

# {{title}}

## Story

<!-- WHAT  The work as one user-centered sentence, Connextra format: "As a [type of user], I want
           [goal], so that [benefit]." Lead with who and why, not the UI.
     WHY   It keeps the work anchored to user value; the "so that" clause is the test of whether the
           work is worth doing at all. Where the user's situation matters more than their role, the
           job-story form ("When [situation], I want [motivation], so I can [outcome]") is often
           sharper. Deep dive: user-stories_companion.md section 3 (Anatomy > Story), and the
           user-story-vs-job-story debate in section 6.
     ASK   Whose goal is this? What outcome do they want? What real benefit does "so that" name? Would
           a job story frame the situation more sharply?
     GOOD  "As a recurring analyst, I want to set one of my saved views as the default for a
           dashboard, so that the dashboard opens the way I work instead of its generic default."
     WEAK  "As a user, I want a dropdown." (a solution in disguise; no real user, no benefit)
     TRAP  A UI task disguised as a story - stating a solution instead of the goal behind it. -->

As a {{user}}, I want {{goal}}, so that {{benefit}}.

## Description and context

<!-- WHAT  Background the one-liner cannot carry: the parent epic, the problem it serves, links to
           designs or the PRD.
     WHY   It orients the reader without bloating the card; kept thin, it points to where the detail
           lives instead of duplicating it. Deep dive: user-stories_companion.md section 3 (Anatomy >
           Description and context).
     ASK   What epic is this split from? What problem does it serve? Where do the design and PRD live?
     GOOD  "Follows from the Saved Views PRD. Depends on a view already existing (the save story). The
           default is per-user, not per-dashboard, per the Q1 storage decision."
     WEAK  "This story is about saving views." (restates the story; adds nothing the card lacks)
     TRAP  Piling in so much context the story becomes a mini-spec - a sign it is an epic to split. -->

{{description_and_context}}

## Acceptance criteria

<!-- WHAT  The conditions that confirm the story is done, from the user's view. List the rules; for
           behavior add Given/When/Then scenarios (or keep them in a paired acceptance-criteria doc).
           Cover the unhappy paths, not just the happy one.
     WHY   It makes the story testable (the T in INVEST); the unhappy paths are where the real work
           and real bugs live. Deep dive: user-stories_companion.md section 3 (Anatomy > Acceptance
           criteria).
     ASK   What must be observably true to call this done? What does the error or missing-data case
           do? Could QA write a test from each line?
     GOOD  "If my default view references a filter that no longer exists, the dashboard loads the
           valid parts and tells me which filter is missing."
     WEAK  "The default-view feature is implemented." (describes implementation, not observable
           behavior a tester can check)
     TRAP  Vague or absent criteria that leave "done" to interpretation (a failure of Testable). -->

- {{acceptance_criterion_1}}

## INVEST check

<!-- WHAT  A quick self-test of story quality against Wake's INVEST (Independent, Negotiable, Valuable,
           Estimable, Small, Testable). Tick each box or note the gap.
     WHY   It catches the two failures that most often wreck a sprint: a story that is not Independent
           and one that is not Small. Deep dive: user-stories_companion.md section 3 (Anatomy > INVEST
           check).
     ASK   Does it stand alone? Is only the how negotiable, not the need? Can the team size it? Does it
           fit one iteration?
     GOOD  "[x] Independent: depends only on the save-view story, a sequenced prerequisite, not a
           sibling." (ticks the box but names the real relationship)
     WEAK  Every box ticked with no note on the one that is actually shaky. (theater, not a self-test)
     TRAP  Skipping the check, then finding at sprint start that the story is not Independent or not
           Small. -->

- [ ] Independent: stands alone, not blocked by a sibling story
- [ ] Negotiable: the how is open, only the need is fixed
- [ ] Valuable: delivers value a user or customer would recognize
- [ ] Estimable: the team can size it
- [ ] Small: fits comfortably in one iteration
- [ ] Testable: the acceptance criteria are verifiable

## Estimate and sizing

<!-- WHAT  The team's relative estimate (story points, t-shirt size) and the confidence behind it.
     WHY   It informs planning, but an estimate is the output of a conversation, not a commitment; a
           precise number with no shared basis is theater. Deep dive: user-stories_companion.md
           section 3 (Anatomy > Estimate and sizing).
     ASK   What is the relative size? How confident is the team? What drives the uncertainty?
     GOOD  "3 story points (illustrative), high confidence; the storage and load paths already exist."
     WEAK  "42.5 hours." (false precision with no shared basis or confidence)
     TRAP  A precise-looking number with no shared basis; estimates are a conversation, not a
           contract. -->

{{estimate}}

## Dependencies

<!-- WHAT  What this story needs before it can be done: another story, a service, data, a design, an
           approval.
     WHY   The unlisted dependency is the classic mid-sprint blocker; many hard dependencies also flag
           a failure of the "I" in INVEST. Deep dive: user-stories_companion.md section 3 (Anatomy >
           Dependencies).
     ASK   What must exist or be approved first? Who owns it? Do the hard dependencies mean this story
           should be restructured?
     GOOD  "Save-view story must ship first (provides the view to set as default)."
     WEAK  "Depends on other things." (no specific blocker, nothing actionable)
     TRAP  An unlisted dependency that surfaces mid-sprint and blocks the story. -->

- {{dependency_1}}

## Notes and open questions

<!-- WHAT  Links, decisions, and anything still undecided - each open question with an owner and a
           needed-by.
     WHY   Refinement runs on surfaced unknowns; a story that hides them only looks ready.
           Deep dive: user-stories_companion.md section 3 (Anatomy > Notes and open questions).
     ASK   What is genuinely undecided? Who owns each answer, and by when? What links does a reader
           need to orient?
     GOOD  "Open: should a Team Lead set a team default, or only personal defaults? Owner: Priya,
           needed before Phase 2."
     WEAK  An empty notes block on a story that plainly has open questions (hides unknowns to look
           ready).
     TRAP  Hiding unknowns to look ready; surfaced questions are what refinement is for. -->

{{notes}}
