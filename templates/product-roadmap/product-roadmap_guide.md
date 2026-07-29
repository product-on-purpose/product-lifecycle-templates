# Product Roadmap: the guide

How to pick a format and a size, how to tell whether the draft is any good, and when to stop.

## Before you start: is this the right document at all?

Write a roadmap when people outside the team need to know what is coming and in what order, and when the
honest answer varies by how far out you look. Do **not** write one because a planning cycle asked for one.

**Write something else if:**

| You actually need | Because |
|---|---|
| a **product strategy** | you are still arguing about which problems are worth solving. The roadmap orders choices; it does not make them |
| a **product backlog** | you need the specific work items. The roadmap scopes the backlog, it is not a higher-resolution version of it |
| a **release plan** | you are planning one release in detail. That is a project plan, by the account of the person who named both artifacts |
| **OKRs** | you need the measurable commitment for this period. "The roadmap shows the plan. The OKRs carry the commitment" |
| a **Plan of Record** | you have a genuine date commitment. Track it separately and deliberately, so it stays scarce |

**Write nothing at all if** nobody outside the team reads it and the team already knows what it is doing. A
roadmap maintained for an audience that does not exist is a recurring cost with no reader.

**Two warnings worth taking seriously.** First, no study links any roadmap format, cadence or confidence
device to product or business outcomes. What exists is a strong convergence of practitioner *prescription*,
which is worth following and is not proof. Second, **the word "roadmap" appears nowhere in the Scrum Guide**.
Whatever process you run, having one is a choice you are making, not a requirement you are meeting.

## Picking a format and a size

**Format** is the organising principle, and it is a real choice:

- **now-next-later** (`product-roadmap_template-lean.md`, `product-roadmap_template-full.md`) sorts by
  **confidence**. Use it when the honest answer to "when" is "it depends". This is the default, and the only
  one showable to a customer without implying a schedule.
- **go** (`product-roadmap_template-go-full.md`) sorts by **release**, with a measurable goal per release.
  Use it when releases are real events in your world and each needs to answer what it was for.
- **themes** (`product-roadmap_template-themes-full.md`) carries **vision and objectives inside the
  document**. Use it when the roadmap has to travel and argue for itself.

If nobody can name your next release, you do not want the GO format. If the reader already knows the
strategy, you do not need the themes format.

**Size** is how much context the reader lacks: **lean** for a team that shares it, **full** for anyone
outside the room.

## The one test that outranks the rest

**Could a reader build a Gantt chart from this?** Then it stopped being a roadmap. A project plan details
how work gets done; a roadmap communicates why it is worth doing.

The second test is about honesty rather than form: **does this document look equally certain about next
month and next year?** If so, it is claiming knowledge nobody has.

## The rubric

Score each 0, 1 or 2. **Under 12 out of 18, and a now-next-later full roadmap will be read as a commitment
you did not make.** The other variants score against fewer rows; see the scope table below.
That is the failure that costs trust, and it is not recoverable by explaining afterwards that it was only
ever indicative.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Serves a stated outcome** | No parent named | Names a goal, but no item ladders to it | Names the parent document, and you can say which item serves which outcome |
| 2 | **Problems, not features** | Named features throughout | A mix, with features dominant | Someone could solve an item a completely different way and the entry would still be satisfied |
| 3 | **Confidence decays** | Equal precision at every horizon | Later items vaguer, but not deliberately | The furthest items are visibly coarser, and the document says so in words |
| 4 | **Exclusions with a cost** | Nothing excluded | Excludes things nobody asked for | Excludes a named request someone wanted, with a reason, and they have been told |
| 5 | **Not a Gantt chart** | Bars, dependencies, dated features | Some dated deliverables leak in | No delivery commitment could be lifted from it, or the ones that exist are marked as commitments |
| 6 | **Not a backlog** | Assembled from accumulated requests | Mostly top-down, some drift | Every item traces to the outcome above, and you can name something in the backlog that is deliberately absent here |
| 7 | **Dependencies named** *(full, now-next-later only)* | None | Categories listed ("engineering capacity") | Named dependencies, each with the reordering it would trigger |
| 8 | **Owned and triggered** *(full, now-next-later only)* | No review, no owner | "Reviewed quarterly" | An event that triggers review, a backstop date, and a named person |
| 9 | **Audience-honest** *(full)* | Same document for everyone | Vaguely aware it may be shared | States who reads it, and if external, has been stripped and coarsened deliberately |

**Which rows apply to what.** Every threshold is two thirds of the available points, rounded down.

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| now-next-later, full | all 9 | 18 | **12** |
| now-next-later, lean | 1-6 | 12 | **8** |
| go, full | 1-6 and 9 (row 5 judged on whether dates are marked as commitments, not on their presence) | 14 | **9** |
| themes, full | 1-6 and 9 | 14 | **9** |

**Rows 7 and 8 are scored only against now-next-later.** Neither the GO format nor the themes format ships a
Dependencies section or a Review Trigger section, so grading either on those rows would penalise the choice
of format rather than the quality of the document. Row 9 does apply to all three, because every format's
frontmatter carries an `audience` field.

## Format-specific checks

**now-next-later.** Read only the Later lane. Does it read like a plan? If someone could build a budget from
it, the lanes have collapsed and you have a timeline roadmap in three columns.

**go.** Read the goal and metric columns alone, ignoring features. Could a stranger decide, three months
after each release, whether it worked? If not, the metrics are decoration and the features are doing the
work, which is backwards.

**themes.** Read the objectives and themes alone. Does every theme serve a stated objective, and is there an
objective no theme serves? Both mismatches matter, and the second is the one authors miss.

## Failure signals to look for in the draft

- **The feature list.** Named features pinned to dates.
- **The Gantt in disguise.** It started as themes and drifted into bars.
- **Lane collapse.** Stakeholders quote your Next lane back as a commitment.
- **The backlog reformatted.** Assembled from what accumulated rather than from the outcome.
- **False precision.** Q1, Q2, Q3, Q4, all equally confident.
- **Later as a graveyard.** Requests you did not want to refuse, parked where they will quietly rot.
- **The sales leak.** An internal roadmap that will end up in a prospect's inbox, because internal roadmaps
  do.
- **Nothing excluded.** Which means it cannot be used to say no to anything.

## When it is good enough

When someone can use it to refuse a request, when the person whose request it refuses has been told, and when
a reader can tell from the document alone which parts they may plan around. A roadmap that has never been
cited in a decision is not finished, however tidy it looks.

Then delete every HTML comment, put the review trigger in a calendar with a name attached, and decide
deliberately whether anyone outside the company should see it.
