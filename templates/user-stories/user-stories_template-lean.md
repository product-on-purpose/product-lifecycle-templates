---
title: "{{title}}"
doc_type: user-stories
size: lean
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
LEAN USER STORY. One story card: the statement, how you will confirm it, and any notes. The minimum
that is still genuinely useful. Use it for a single backlog item; for a set of stories, copy the card
per story. To grow a card into a fully scaffolded story, ADD sections (see
user-stories_template-full.md); never rename or reorder the ones below (the full variant is a strict
superset of this one). A story is a placeholder for a conversation, not a complete spec; keep it short
and talk.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   user-stories_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you ship: self-grade against user-stories_guide.md, then DELETE every HTML comment. They are
   guidance, not content.
-->

# {{title}}

## Story

<!-- WHAT  The work as one user-centered sentence, Connextra format: "As a [type of user], I want
           [goal], so that [benefit]." Lead with who and why, not the UI.
     WHY   It forces the user, the goal, and the benefit into one line and keeps the work anchored to
           value; the "so that" clause is the test of whether the work is worth doing at all.
           Deep dive: user-stories_companion.md section 3 (Anatomy > Story).
     ASK   Whose goal is this? What outcome do they want? What real benefit does "so that" name? Is
           this an outcome, not a UI task?
     GOOD  "As a recurring analyst, I want to save my current dashboard filters as a named view, so
           that I can return to exactly this slice tomorrow without rebuilding it."
     WEAK  "As a user, I want a dropdown." (a solution in disguise; no real user, no benefit)
     TRAP  A UI task disguised as a story - stating a solution instead of the goal behind it. -->

As a {{user}}, I want {{goal}}, so that {{benefit}}.

## Acceptance criteria

<!-- WHAT  How you will know this story is done, from the user's point of view - the "Confirmation" of
           the story. Keep it short here; for richer criteria use the acceptance-criteria artifact.
     WHY   It makes the story testable (the T in INVEST) and gives "done" an objective meaning both
           sides read the same way. Deep dive: user-stories_companion.md section 3 (Anatomy >
           Acceptance criteria).
     ASK   What must be observably true for this to be done? Would a tester read it the same way you
           do? What does the unhappy path look like?
     GOOD  "I can name and save the current filters, date range, and visible columns as a view."
     WEAK  "It works well." (not observable; nothing a tester could verify)
     TRAP  No criteria at all, which leaves "done" to interpretation. -->

- {{acceptance_criterion_1}}

## Notes and open questions

<!-- WHAT  Context, links (designs, the parent epic), decisions, and anything still undecided - each
           open question with an owner and a needed-by.
     WHY   Refinement runs on surfaced unknowns; a story that hides them only looks ready.
           Deep dive: user-stories_companion.md section 3 (Anatomy > Notes and open questions).
     ASK   What is genuinely undecided? Who owns each answer, and by when? What links does a reader
           need to orient?
     GOOD  "Open: should a Team Lead set a team default, or only personal defaults? Owner: Priya,
           needed before Phase 2."
     WEAK  An empty notes block on a story that plainly has open questions (hides unknowns to look
           ready).
     TRAP  Cramming a full spec here; if it needs that much, the work is probably an epic to split. -->

{{notes}}
