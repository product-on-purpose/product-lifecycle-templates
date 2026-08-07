---
title: "{{sprint_id}} Retrospective Notes"
doc_type: sprint-retrospective-notes
size: lean
sprint: "{{sprint_id}}"
team: "{{team_name}}"
facilitator: "{{facilitator}}"
status: draft
doc_version: "{{doc_version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: sprint-retrospective-notes
source_template_version: 0.1.0
---

<!--
LEAN SPRINT RETROSPECTIVE NOTES. The whole artifact: which sprint this covers and who was in the room, what
last retrospective's action items actually became, what worked, what did not, and what will change. This
bundle ships one size. No primary, standards, or academic source publishes a heavier version of this
document, and the real variation in the literature this research read is across occasions, a release or
project retrospective is a different document, not a bigger size of this sprint-scoped one. See
sprint-retrospective-notes_companion.md section 4 (Variants and sizing).

A SPRINT RETROSPECTIVE NOTES DOCUMENT EXISTS TO MAKE ONE IMPROVEMENT OWNED, DATED, AND FINDABLE AGAIN. The
Scrum Guide names an event, never a document, and in its 2020 rewrite it downgraded the one mechanism that
used to carry retrospective output forward: what the 2017 Guide required, the current Guide only permits.
The largest study of retrospective content this research read found that the large majority of statements
gave no reason at all, and unowned, unchecked action items are the single most-named failure mode in the
practitioner literature behind this bundle. Every section below answers one of those two problems. See
sprint-retrospective-notes_companion.md sections 1, 2, and 7.

THIS IS NOT AN INCIDENT POSTMORTEM. If this sprint contained an incident, name it here and record its causal
analysis in the incident-postmortem member of this family instead; keep this document scoped to how the team
worked across the whole sprint, not to why one specific thing failed. See sprint-retrospective-notes_companion.md
section 8 (Relationships to other artifacts).

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   sprint-retrospective-notes_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a
   WEAK example, and the TRAP to avoid. For each table, PRIORITY explains the ordering and ROW HINT says
   what a good row contains.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it. An empty Previous
   Actions table on a team's first retrospective is not an N/A: write "First retrospective for this team, no
   prior actions to check" as the row instead.
4. Before you share it: self-grade against sprint-retrospective-notes_guide.md, then DELETE every HTML
   comment. They are guidance, not content.
-->

# {{sprint_id}} Retrospective Notes

## Sprint and Participants

<!-- WHAT  The identifying header: which sprint this retrospective covers, when it was held, who
           facilitated it, and who was actually in the room.
     WHY   This renders Documentero's own "Meeting Information" heading for a sprint context. No source
           this research read argues against recording this; it is the least contested section in the
           document. Deep dive: sprint-retrospective-notes_companion.md section 3 (Anatomy > Sprint and
           Participants).
     ASK   Which sprint does this cover, named by its own identifier rather than a date range alone, so
           the notes stay findable against the sprint backlog they discuss? Who was actually present, not
           who was invited?
     GOOD  "Sprint 24 (2026-06-08 to 2026-06-19). Facilitator: Priya Nair. Present: Priya Nair, Sam Osei,
           the full Developer group (4), Product Owner Dana Ruiz."
     WEAK  "Sprint retro, June." (no identifier a later reader can match against the sprint backlog, and no
           record of who actually spoke for the team)
     TRAP  Recording who was invited instead of who showed up. A retrospective's discussion is only as
           honest as the room that actually held it, and a later reader needs to know whose account this
           is. -->

**Sprint:** {{sprint_id}} ({{sprint_start_date}} to {{sprint_end_date}})
**Facilitator:** {{facilitator}}
**Present:** {{participants_present}}

## Previous Actions

<!-- WHAT  A check on the action items the previous retrospective produced: done, in progress, or dropped,
           with one line of why for anything not done.
     WHY   This section is this bundle's own contribution; no published vendor template carries it. It
           exists because unchecked action items from a previous retrospective are a named anti-pattern in
           the practitioner literature this research read, and because the Scrum Guide's 2020 rewrite
           downgraded the one mechanism that used to carry retrospective output forward: what the 2017
           Guide required, the current Guide only permits. Deep dive:
           sprint-retrospective-notes_companion.md section 3 (Anatomy > Previous Actions) and section 2
           (Origins and evolution).
     ASK   For every action item the previous retrospective produced, is its status recorded here: done,
           in progress, or dropped? Does every row that is not done carry one honest line on why?
     PRIORITY  List rows in the order the previous retrospective's Action Items table had them, so a
           reader can check this table against that one, line for line.
     ROW HINT  A good row names the action exactly as the previous retrospective wrote it, its status, and,
           if not done, one honest line on why.
     GOOD  | Add a staging smoke test before merge | Sam Osei | Done | Landed 2026-06-11, running on every
           merge to main. |
     WEAK  (a finished action left off the table entirely) (a finished action left off looks the same as
           one nobody tracked, and an unfinished one left off looks the same as one that never existed)
     TRAP  Silently dropping a row that was not finished instead of carrying it forward as "in progress" or
           "dropped, because...". An empty Previous Actions table, sprint after sprint, is usually not
           evidence the team has nothing outstanding. It is usually evidence nobody is reading this
           section, which is the exact failure it exists to catch. -->

| Action from previous retrospective | Owner | Status | Note |
|---|---|---|---|
| {{previous_action}} | {{previous_action_owner}} | {{previous_action_status}} | {{previous_action_note}} |

## What Went Well

<!-- WHAT  The team's own account of what worked in the sprint, and why it worked, not only that it did.
     WHY   "What went well" is the one phrase the Scrum Guide's own text supplies for the Sprint
           Retrospective's content, and every vendor template this research read carries a version of this
           heading. The "why" column exists because the largest study of retrospective content this
           research read found that the large majority of statements gave no justification at all. Deep
           dive: sprint-retrospective-notes_companion.md section 3 (Anatomy > What Went Well).
     ASK   Is each row a specific practice, not general morale? Does it say why the practice worked, not
           only that something went well?
     PRIORITY  No ranking; list rows in the order they came up in discussion.
     ROW HINT  A good row names a specific practice and the reason it helped, concrete enough that someone
           who was not in the room could repeat the practice on purpose next sprint.
     GOOD  | Pairing on the entitlement fix | Caught the edge case before it reached staging; a second set
           of eyes on the filter logic found the gap a solo review had missed twice. |
     WEAK  | Good week | (no practice named, no reason given, and nothing here is repeatable on purpose)
     TRAP  Writing one-word morale entries, "good," "solid sprint," instead of specific practices with a
           reason attached. A column that only asks what reproduces exactly the shallowness this bundle's
           own research measured. -->

| What went well | Why it worked |
|---|---|
| {{went_well_item}} | {{went_well_reason}} |

## What To Improve

<!-- WHAT  What the team says did not work, and at least one candidate idea for changing it.
     WHY   This section folds two headings vendor templates this research read publish separately, "what
           didn't go well" and "ideas for improvement", into one, so a named problem stays attached to a
           proposed change instead of floating unaddressed. Deep dive: sprint-retrospective-notes_companion.md
           section 3 (Anatomy > What To Improve).
     ASK   For every problem named, is there at least one candidate idea attached, even a rough one? Does
           the row say why the problem happened, not only that it did?
     PRIORITY  No ranking; list rows in the order they came up in discussion.
     ROW HINT  A good row names a specific problem and a concrete idea for changing it, not a diffuse
           complaint.
     GOOD  | Code review queue backed up for two days mid-sprint | One reviewer was out and nobody
           covered; rotate a designated backup reviewer into the on-call rotation. |
     WEAK  | Reviews are slow | (no cause named, no candidate idea attached; reads the same every sprint
           and nothing changes)
     TRAP  Naming a problem with nothing attached to it. A problem with no idea beside it tends to become
           an Action Items row with no substance behind it, or nothing at all. -->

| What did not work | Idea to change it |
|---|---|
| {{improve_item}} | {{improve_idea}} |

## Action Items

<!-- WHAT  The commitments this retrospective actually produces: what will change, who owns it, and by
           when.
     WHY   This renders the "Action Items" heading every vendor template this research read carries in
           some form, and it is the section the whole document exists to make binding: an unowned action
           item is the single most-named failure mode in the practitioner literature behind this bundle.
           Deep dive: sprint-retrospective-notes_companion.md section 3 (Anatomy > Action Items).
     ASK   Does every row have a named owner and a date? Is the change worth the retrospective time it
           took to identify, or is it small enough to cut rather than track?
     PRIORITY  List rows in the order the team intends to act on them.
     ROW HINT  A good row names the change as something that can be checked done or not, the owner, a
           person rather than a team, and a date.
     GOOD  | Add a designated backup reviewer to the on-call rotation | Dana Ruiz | 2026-06-26 |
     WEAK  | Improve code review | | (no owner, no date; an observation wearing an action item's clothing)
     TRAP  Writing an action item too small to be worth tracking, or one so large it will never be checked
           done. A commitment worth writing down should be able to justify the time this retrospective
           spent finding it. -->

| Action | Owner | Due |
|---|---|---|
| {{action_item}} | {{action_owner}} | {{action_due}} |
