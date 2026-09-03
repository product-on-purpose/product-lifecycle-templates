---
title: "{{epic_name}} Epic"
epic_name: "{{epic_name}}"
owner: "{{owner}}"
status: "{{status}}"
target_timeframe: "{{target_timeframe}}"
related: ["{{related_docs}}"]
doc_type: epic
size: full
source_template: epic
source_template_version: 0.1.0
---

<!--
FULL EPIC. Every section, for a body of work that crosses teams, carries real dependencies, or needs a
stated (or explicitly absent) position above it. Most single-team, single-tool epics do not need this; the
lean five sections are the whole artifact for them.

The full variant is a strict superset of the lean one: the first five sections keep their names and order,
and this file only ADDS Out of Scope, Dependencies, and Link Upward, the three places this research found
prose doing work a tracker's own fields do not do for it: a named exclusion, a two-sided owned dependency,
and a stated position in a hierarchy that even the vendors who publish one cannot agree on. If you are
growing from lean, add these three; do not reorder anything already there.

AN EPIC IS A TRACKER RECORD FIRST, AND A DOCUMENT ONLY SECOND. Every tracker this library's research
examined (Jira, Azure Boards, GitLab, Linear, Aha!) already ships titles, dates, parent-child links, and
rollups, as typed fields on a work-item panel. Keep using those fields for what they already do well. Write
this document only for what those fields cannot carry: the context, the exclusions, the owned dependencies,
and the position above it. See epic_companion.md section 1 and section 8.

YOUR FRAMEWORK PROBABLY DOES NOT DEFINE THIS WORD, AND THE WORD HAS DRIFTED FROM ITS FOUNDING MEANING. Four
of the five methodologies this library's research surveyed (Scrum, XP, the Kanban Method, LeSS Huge) have no
epic concept at all; SAFe is the outlier, and it formalizes the artifact heavily, including an MVP, a Lean
business case, and a named accountable Epic Owner role. The founding published definition (Cohn, 2004) is a
single oversized story destined to be split and then to disappear, not a group; every tracker examined now
implements the container sense instead, a drift Cohn himself names but did not author. This template teaches
the container, because that is what a reader actually has open in front of them. See epic_companion.md
section 2 and section 5.

THE SHARPEST BOUNDARY IS AGAINST A BUSINESS CASE, AND SAFe'S OWN LEAN BUSINESS CASE IS THE CLEAREST EVIDENCE
WHY. When an epic is written as a genuine multi-section document, the strongest documented case of it is
SAFe's Lean Business Case, which wraps a Scope Definition and an In Scope / Out of Scope pair around a Cost
Estimate, a Value Return, and a Go/No-Go Recommendation. Those three, costing, value return, and a
go/no-go call, belong to the `business-case` artifact, not here. This document groups the work and states
what it is in service of; it does not argue for the investment. See epic_companion.md section 4 and
section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   epic_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK example, and the
   TRAP to avoid. For a table, PRIORITY explains the row order and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Write Scope before Out of Scope; the exclusions should
   answer questions the boundary actually raised, not restate it in the negative.
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

## Out of Scope

<!-- WHAT  What this epic deliberately does not cover: the boundary partner to Scope, named as its own
           step rather than left implicit.
     WHY   The sharpest teaching point this research returned for this document: write the exclusions, not
           just the scope. ProductPlan frames the boundary step as writing what is deliberately left out;
           no tracker examined ships a dedicated field for it. A scope section that never states an
           exclusion is the likeliest single reason an epic never closes. Deep dive: epic_companion.md
           section 3 (Anatomy > Out of Scope) and section 7 (Anti-patterns).
     ASK   What has come up that this epic will not cover? What adjacent work looks related but belongs to
           a different epic? What would you refuse if someone tried to fold it in here?
     GOOD  "Out of scope: sharing a view with another user (a separate epic); team-level default views
           (needs a permissions model this epic does not build); exporting a view's data (already covered
           by the existing export feature)."
     WEAK  "Everything else is out of scope." (names nothing; the next person to propose scope creep has
           nothing to point at)
     TRAP  Treating Out of Scope as an afterthought copied from Scope's negative space. Name specific
           things that have actually come up, ideally something a reasonable colleague would argue for
           including. -->

{{out_of_scope}}

## Dependencies

<!-- WHAT  What this epic needs from outside its own team, or owes to someone else, each classified by
           type and severity, with a named owner on both sides.
     WHY   Agility at Scale's dependencies guidance is the named source for asking more than a link:
           "Classify each dependency by type (knowledge, technical, process) and severity (blocking versus
           informational)." And, more pointedly: "Every dependency gets an owner on both sides - the
           requesting team and the providing team. Unowned dependencies are invisible dependencies in
           disguise." This is more structure than a tracker's own linked-item field carries on its own.
           Deep dive: epic_companion.md section 3 (Anatomy > Dependencies) and section 7 (Anti-patterns >
           Unowned dependencies).
     ASK   What does this epic need from outside itself, or owe to someone else? What kind of dependency is
           it (knowledge, technical, process)? How severe if it slips (blocking versus informational)? Who
           owns it on each side?
     PRIORITY  Order rows by severity, blocking first. Every row needs an owner on both sides; a dependency
           with only one named owner is not yet tracked.
     ROW HINT  A good row names the specific thing needed, its type and severity, and both owners. A weak
           row is a bare link with no owner.
     GOOD  | D-01 | Platform team delivers the change-capture hook the history feed reads from | Technical | Blocking | Dana Osei (Audit Trail) | Lee Zhang (Platform) | Confirmed |
     WEAK  | D-01 | Waiting on platform | | | | | |
     TRAP  Recording a dependency as a bare link with no owner on each side. A dependency without a named
           owner on the providing side is not meaningfully tracked at all, whatever the tracker's own link
           field suggests. -->

| ID | Dependency | Type | Severity | Owner (this side) | Owner (other side) | Status |
|---|---|---|---|---|---|---|
| {{dependency_id}} | {{dependency}} | {{dependency_type}} | {{severity}} | {{owner_this_side}} | {{owner_other_side}} | {{dependency_status}} |

## Link Upward (Initiative, Theme, or nothing)

<!-- WHAT  Whatever sits above this epic in your own organization's hierarchy, named in your own
           vocabulary: an Initiative, a Theme, or nothing at all.
     WHY   Three hierarchies disagree with each other and none claims the others are wrong: Jira and
           Atlassian place an Initiative above the epic, Aha! places its own Initiative above Epic above
           Feature, and SAFe has no initiative tier, running Epic above Feature above Story. No source
           claims one of these is correct, so this field is a pointer to your own hierarchy, not an
           assertion of a named tier. Deep dive: epic_companion.md section 3 (Anatomy > Link Upward) and
           section 6 (Debates > What sits above the epic?).
     ASK   Does your organization have a tier above the epic? What is it actually called there? If there
           is none, say so rather than inventing a name.
     GOOD  "Initiative: 'Enterprise Readiness' (Jira Initiative INIT-4). No Theme is tracked separately for this
           epic."
     WEAK  "Theme: Analytics." (Theme is not established as a hierarchy level by the sources this bundle
           checked; naming it here as if it were a settled rung asserts more than the evidence supports)
     TRAP  Naming Theme as if it were a settled rung in the hierarchy. The Agile Alliance glossary records
           that themes are "typically not used as a level in a backlog hierarchy," and Cohn defines a theme
           as a collection of stories sharing a topic, not a tier above one. If your organization genuinely
           uses Theme as a rung, say so, and say that is your organization's own convention rather than a
           documented standard. -->

{{link_upward}}
