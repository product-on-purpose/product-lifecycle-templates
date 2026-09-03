---
title: "{{epic_name}} Epic"
epic_name: "{{epic_name}}"
owner: "{{owner}}"
status: "{{status}}"
target_timeframe: "{{target_timeframe}}"
doc_type: epic
size: lean
source_template: epic
source_template_version: 0.1.0
---

<!--
LEAN EPIC. The five sections a tracker's own fields cannot carry: what this body of work is and who it
serves (Title and Narrative Summary), the larger effort it ladders up to (Goal and Context), its boundaries
(Scope), the maintained list of stories it splits into (Child Stories), and the high-level bar for calling
it done (Acceptance Criteria). Use it for a single-team epic living inside one tool's own record. To grow it
into a full epic (see epic_template-full.md), ADD sections; never rename or reorder the ones below, because
the full variant is a strict superset of this one.

AN EPIC IS A TRACKER RECORD FIRST, AND A DOCUMENT ONLY SECOND. Every tracker this library's research
examined (Jira, Azure Boards, GitLab, Linear, Aha!) already ships titles, dates, parent-child links, and
rollups, as typed fields on a work-item panel. Keep using those fields for what they already do well. Write
this document only for what those fields cannot carry. At the lean size that is the context: what this work
is in service of, and why now. The exclusions, the owned dependencies, and the position above the epic are
the three sections the full variant adds; grow into it when you need them. See epic_companion.md section 1
and section 8.

YOUR FRAMEWORK PROBABLY DOES NOT DEFINE THIS WORD, AND THE WORD HAS DRIFTED FROM ITS FOUNDING MEANING. Four
of the five methodologies this library's research surveyed (Scrum, XP, the Kanban Method, LeSS Huge) have no
epic concept at all; SAFe is the outlier, and it formalizes the artifact heavily. The founding published
definition (Cohn, 2004) is a single oversized story destined to be split and then to disappear, not a group;
every tracker examined now implements the container sense instead, a drift Cohn himself names but did not
author. This template teaches the container, because that is what a reader actually has open in front of
them. See epic_companion.md section 2 and section 5.

THE SHARPEST BOUNDARY IS AGAINST A BUSINESS CASE. A cost estimate, a value-return figure, or a go/no-go
recommendation belongs to the `business-case` artifact, not here. This document groups the work and states
what it is in service of; it does not argue for the investment. See epic_companion.md section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   epic_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK example, and the
   TRAP to avoid. For the table, PRIORITY explains the row order and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Write Scope before Child Stories; the boundary should
   produce the story list, not the other way around.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you share it: self-grade against epic_guide.md, then DELETE every HTML comment. They are
   guidance, not content.
-->

# {{epic_name}} Epic

## Title and Narrative Summary

<!-- WHAT  A short, clear name; then one sentence on the goal; then a persona-form narrative naming who
           this serves and what they get: "As the [persona], I want to [objective] so that [value]."
     WHY   A tracker's title field forces brevity; it does not force a stated audience or a stated value.
           ProductPlan is the named source for asking for more than a title: a title, a short description
           of the goal, and a persona-form narrative. Deep dive: epic_companion.md section 3 (Anatomy >
           Title and Narrative Summary).
     ASK   What is the epic called? In one sentence, what are you trying to achieve? Who is this for, and
           what do they get?
     GOOD  "Audit Trail. Let a Compliance Officer answer who changed a record, and when, without asking
           an engineer to run a query. As a Compliance Officer, I want a searchable history of changes to
           any record, so that I can answer an auditor's question the same day it is asked."
     WEAK  "Audit Trail." (a title alone; states no audience and no value, and repeats what the tracker's
           own title field already carries)
     TRAP  Stopping at the title. A tracker's title field already forces brevity; writing nothing past it
           wastes the one thing this section can do that the field cannot. -->

{{goal_description}}

As a {{persona}}, I want {{objective}}, so that {{value}}.

## Goal and Context

<!-- WHAT  The larger effort this epic ladders up to, and why it matters now: what it is in service of,
           stated in whatever form the reader actually has above them.
     WHY   This is the section the rest of the document answers to, and the reason to write an epic as
           prose rather than open a ticket: everything a tracker's fields already do well, keep doing;
           this is where prose earns a place they cannot fill. What the larger effort is called is itself
           unsettled: SAFe formalizes an Epic Hypothesis Statement naming a target customer, a need, and a
           measurable outcome, while three tool hierarchies disagree on what sits above an epic at all.
           Deep dive: epic_companion.md section 3 (Anatomy > Goal and Context) and section 6 (Debates).
     ASK   What larger goal, initiative, or theme does this serve? Why now? What would make this epic
           worth having done, a quarter after it ships?
     GOOD  "Serves the FY26 'Enterprise Readiness' goal: two deals stalled last quarter on our inability
           to evidence who changed what, and Audit Trail is the largest lever we have on that this half."
     WEAK  "Because the roadmap says so." (names no goal and no reason, and gives a reviewer nothing to
           check the epic against)
     TRAP  Stating the goal as a feature list ("build views, sharing, defaults") rather than the effort
           above the epic. If Goal and Context reads like Scope, you have written the same thing twice
           under two headings. -->

{{goal_and_context}}

## Scope

<!-- WHAT  The boundaries of the work this epic covers: what is included, described as an edge rather
           than a feature list.
     WHY   ProductPlan names this step directly: "jot down the scope of work for this epic - in other
           words, the boundaries." No tracker examined ships a dedicated scope-boundary field; the closest
           tracker fields describe priority and timing, not boundaries. Deep dive: epic_companion.md
           section 3 (Anatomy > Scope).
     ASK   What is included in this body of work? Where does it start and stop? What would make you say
           "that belongs to a different epic"?
     GOOD  "Covers saving, naming, listing, and reopening a dashboard's current filter and view state, for
           one user's own views: the storage and retrieval mechanics, and the UI to manage a personal
           list."
     WEAK  "Saved views and related work." (no boundary; "related work" could mean anything, and nothing
           here tells you what is out)
     TRAP  Writing scope as a feature list with no edge. A scope with no boundary reads the same whether
           the epic is nearly done or barely started. -->

{{scope}}

## Child Stories

<!-- WHAT  The maintained list of stories this epic splits into: the founding relation itself.
     WHY   Cohn's founding relation states the direction: "Epics can be split into two or more stories of
           smaller size." Aha!'s present-day description keeps the same shape from the grouping side:
           "Epics are used to group features that often share a common business objective." This
           document's version is a maintained, intentional list; the tracker's version is what that list
           later feeds into a rollup such as Jira's Epic Burndown. Deep dive: epic_companion.md section 3
           (Anatomy > Child Stories).
     ASK   Which stories does this epic split into? Is the list current? What is each story's status?
     PRIORITY  Order rows by the sequence the stories will actually be pulled, top first.
     ROW HINT  A good row names the story's id (from user-stories or the backlog), a short title, and a
           status you keep current. A weak row is a bare feature name with no id and no status.
     GOOD  | SV-1 | Persist a saved view (storage) | In progress |
     WEAK  | | "Views stuff" | |
     TRAP  Letting this list silently drift from the tracker's own child links, so the document and the
           epic's real children disagree. The tracker computes its rollup from these children; a list that
           has stopped matching them stops being useful for anything. -->

| ID | Story | Status |
|---|---|---|
| {{story_id}} | {{story_title}} | {{story_status}} |

## Acceptance Criteria

<!-- WHAT  The high-level list of requirements the team will need to approve before this epic is
           considered done.
     WHY   ProductPlan frames this as the completion gate: "a clear set of acceptance criteria - the
           high-level list of requirements your team will need to approve." This is not the only published
           answer to how an epic closes: SAFe substitutes a falsifiable hypothesis for acceptance criteria
           instead, and the Cohn lineage has no closure artifact for an epic at all, because an epic there
           is not distinct enough from a story to need one. This template follows ProductPlan's convention;
           treat the alternative as a live, unresolved debate, not a settled one. Deep dive:
           epic_companion.md section 3 (Anatomy > Acceptance Criteria) and section 6 (Debates).
     ASK   What must be true, overall, for this body of work to be considered done? Is each item something
           the team can actually check, rather than a restatement of the scope?
     GOOD  "- [ ] A user can save the current dashboard state as a named view. - [ ] A user can reopen a
           saved view in one click. - [ ] Saved views persist across sessions."
     WEAK  "- [ ] Views work." (not checkable, and restates the epic rather than gating it)
     TRAP  Writing story-level detail here. This is the high-level gate for the whole epic; the
           story-by-story detail belongs in each story's own acceptance criteria (see the
           acceptance-criteria artifact), not duplicated here. -->

- [ ] {{criterion_1}}
- [ ] {{criterion_2}}
