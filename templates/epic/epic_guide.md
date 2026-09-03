# Guide: Epic (operator card)

Fast reference for the Epic bundle. For the full reasoning, history, and sources, read
[`epic_companion.md`](epic_companion.md).

## When to use

- To carry what a tracker's own epic record cannot: why this body of work exists, who it serves, what is
  deliberately left out, and what larger effort it ladders up to.
- When a body of work is large enough that it needs to be split into stories and something has to say why
  those stories belong together.
- When the work crosses teams, carries real dependencies, or needs a stated (or explicitly absent) answer
  to what sits above it. That is the point to grow lean into full, not to open a second document type.

## When NOT to use

- Your team lives entirely inside one tool's epic record, with short-lived, single-team work. The
  tracker's own fields for title, dates, parent-child links, and rollups already do that job; write only
  the narrative summary a field cannot carry, at the lean size. If you need the exclusions, the owned
  dependencies, or a stated position above the epic, that is the signal to use full.
- You need a cost estimate, a value-return figure, or a go/no-go recommendation. That is `business-case`
  territory. This document groups the work and states what it is in service of; it does not argue for the
  investment.
- You need one story's own detailed, checkable conditions. That is `acceptance-criteria` at the story
  level. This document's own Acceptance Criteria section is the high-level gate for the whole epic, not a
  place to duplicate a single story's criteria.

## Pick a variant

- **Lean** (default): Title and Narrative Summary, Goal and Context, Scope, Child Stories, and Acceptance
  Criteria. Enough to state what the work is, why it exists, and what closes it, for a single-team epic
  living inside one tool.
- **Full**: adds Out of Scope, Dependencies, and Link Upward. For work that crosses teams, carries real
  dependencies, or needs a stated position above it. Grow lean into full by adding these three sections;
  the first five keep their name and order.

## The rubric

Score each 0, 1 or 2. **Under 12 out of 16 and a reader still has to go ask someone what this epic
actually excludes, depends on, or sits under, which is exactly the information this document exists to
carry instead of the tracker's fields.**

**Which rows apply to what.** This bundle ships two variants, and three rows grade sections only the full
variant carries, so scoring lean against all eight would penalise the choice of variant rather than the
quality of the epic.

| Variant | Rows that apply | Maximum | Score against |
|---|---|---|---|
| full | all 8 | 16 | **12** |
| lean | 1-5 (it carries none of the three full-only sections) | 10 | **7** |

Both thresholds sit above two-thirds of the available points; neither is a bare pass mark. **Under 7 out
of 10 on the lean rows and this document is not doing anything the tracker's own title and status fields
do not already do.**

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Audience and value named** | Title alone, or a persona sentence with no stated audience and no stated value | A persona sentence exists, but it is generic enough to paste onto any epic in the backlog | A reader who has never met the author can say who benefits and what they get, from the sentence alone |
| 2 | **Goal points upward** | No larger effort named, and no reason given for why now | A larger effort is named, but the section restates Scope's feature list under a different heading | You could point at the sentence that names the larger effort, and say which lever it loses if this epic is cut |
| 3 | **Scope has an edge** | A feature list with no stated boundary | Some items suggest a boundary, but a reader has to infer where scope actually stops | A reader can point at the sentence that says where scope stops, not only what it includes |
| 4 | **Child list stays current** | List absent, or stories with no status and no id a reader could look up | IDs and statuses are present, but nothing ties this list to what the tracker actually rolls up | Every row names a real story id and a status a reader could go verify in the tracker right now |
| 5 | **Criteria are checkable gates** | Criteria restate the goal or the scope in different words | Some criteria are checkable, but at least one restates scope or duplicates a single story's own criteria | Every criterion could be marked pass or fail by someone who did not write it, and none belongs to one story alone |
| 6 | **Exclusions are specific** *(full only)* | No Out of Scope section, or "everything else is out of scope" | Exclusions are listed, but they are generic enough to belong to any epic | You can point at a specific thing that came up, was refused, and say which other epic it belongs to instead |
| 7 | **Dependencies are owned** *(full only)* | Dependencies recorded as bare links, with no type, severity, or owner | Type or severity is given, but at least one dependency has no named owner on one side | Every dependency names its type, its severity, and a person on each side who would confirm they own it |
| 8 | **Position stated or absent** *(full only)* | The field is blank, or it names a tier your own organization does not actually use | Something is named above the epic, but the section does not say whether that is your own organization's convention or a documented standard | The field names the real tier in your organization's own vocabulary, or states plainly that none exists, without asserting a tier borrowed from a vendor |

## Named anti-patterns (the usual wrecks)

1. **The epic that never closes.** Scope keeps absorbing new work and nothing ever marks it done. The
   published fixes disagree: dissolve the artifact, or hold it to an evidence-based Done rather than a
   completion checklist.
2. **Scope with no stated exclusions.** A Scope section that never says what is out invites the drift that
   later makes the epic hard to close. Write the exclusions as their own step, not as an afterthought.
3. **Unowned dependencies.** A dependency recorded as a bare link, with no named owner on each side, is not
   meaningfully tracked at all, whatever the tracker's own link field suggests.
4. **Writing an epic that only repeats field values.** Every tracker surveyed already does titles, dates,
   parent-child links, and rollups well. This document earns its place only where it says something none of
   those fields say.
5. **Crossing into a business case's territory.** A cost estimate, a value-return figure, or a go/no-go
   recommendation belongs to `business-case`, not here.
6. **Treating one vendor's hierarchy as the only correct one.** Three published hierarchies disagree with
   each other, and none claims the others are wrong. Asserting one as universal will read as wrong to a
   reader using either of the other two.
