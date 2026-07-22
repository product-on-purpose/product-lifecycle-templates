# Companion: The Sprint Backlog

> The deep explainer for the sprint-backlog bundle. Read this to understand what a Sprint Backlog is,
> where it came from, why it is shaped the way it is, and where practitioners disagree about it. The short
> operator card is [`sprint-backlog_guide.md`](sprint-backlog_guide.md); a fully worked instance is
> [`sprint-backlog_example.md`](sprint-backlog_example.md). Inline citations like [[1]](#ref-1) resolve to
> the [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A Sprint Backlog is **the Developers' living plan for a single Sprint**: the one objective they are
working toward, the items they have selected to get there, and the plan for doing the work. The 2020
Scrum Guide defines it as three things held together: *"the Sprint Goal (why), the set of Product Backlog
items selected for the Sprint (what), as well as an actionable plan for delivering the Increment (how)"*
[[1]](#ref-1). It is not a second copy of the product backlog, not a status report for management, and not
a fixed contract of deliverables: it is *"a plan by and for the Developers"* [[1]](#ref-1).

The honest first thing to know is that the Sprint Backlog is a **forecast, and its commitment is the
Sprint Goal, not the list of items.** The Scrum Guide deliberately says the Developers create a *forecast*
of work, and the one thing they commit to is the Sprint Goal, *"the single objective for the Sprint"*,
which *"provides flexibility in terms of the exact work needed to achieve it"* [[1]](#ref-1). A Sprint
Backlog read as a promise to ship exactly these items is the artifact misused.

**At a glance**
- It is **by and for the Developers** [[1]](#ref-1). The Product Owner owns the *product* backlog and
  proposes the goal; the Developers own *this* plan. A Sprint Backlog dictated by anyone else is not one.
- Its three parts are **why (Sprint Goal), what (selected items), and how (the plan)** [[1]](#ref-1). Drop
  the why and you have a task list; drop the how and you have a wish.
- It is a **forecast, not a contract.** The commitment is the Sprint Goal; the item list may be
  renegotiated as more is learned, without abandoning the goal [[1]](#ref-1)[[3]](#ref-3).
- It is **living and real-time**, *"updated throughout the Sprint as more is learned"* and detailed enough
  to inspect progress at the Daily Scrum [[1]](#ref-1).
- It is **drawn from the product backlog**, a Sprint-sized subset, and it produces an Increment that meets
  the Definition of Done ([section 8](#8-relationships-to-other-artifacts)).

If you read nothing else: a Sprint Backlog is **the Developers' forecast of how they will meet one Sprint
Goal.** The goal is the commitment; the plan is theirs; both stay alive for the length of the Sprint.

---

## 2. Origins and evolution

**The Sprint Backlog has been a Scrum artifact since the framework was named, but its definition sharpened
in 2020.** Two changes matter.

**From two parts to three.** The 2017 Scrum Guide defined the Sprint Backlog as the selected Product
Backlog items plus a plan for delivering them, a two-part composition; the Sprint Goal existed but was not
a named component of the artifact [[2]](#ref-2). The 2020 revision folded the **Sprint Goal into the
artifact itself** as the "why", making the composition explicitly three-part (why, what, how)
[[1]](#ref-1), and introduced a framework in which each of Scrum's three artifacts carries a commitment:
*"For the Product Backlog it is the Product Goal, the Sprint Backlog has the Sprint Goal, and the Increment
has the Definition of Done"* [[3]](#ref-3). The InfoQ Q&A with the authors reports the reintroduction was
done *"to provide greater focus for the Scrum Team"* [[4]](#ref-4).

**From "commitment" to "forecast" (and a careful walk-back).** The earliest Scrum Guides said the team
*committed* to the selected work. In 2011 that language was deliberately changed to *forecast*, so the
Guide now says the team creates *"a forecast of work it believes will be done, but that forecast will
change as more becomes known throughout the Sprint"* [[3]](#ref-3). The change is widely read as removing
a stick: a forecast treated as a promise turns velocity into a target and can punish a team for learning.
The 2020 Guide then reintroduced the word "commitment", but attached it precisely to the
**Sprint Goal**, not the item list [[3]](#ref-3)[[4]](#ref-4). Jake Calabrese's version-by-version history
traces this arc and the practitioner view that "commitment" still carries a legitimate, narrower meaning
(the team commits to one another) even after the official change [[12]](#ref-12).

**"Development Team" became "Developers."** The 2020 Guide eliminated the separate "Development Team" as a
sub-team and folded its members into the single Scrum Team as "Developers", to reduce the *"'us and them'
behavior"* a nested team invited [[4]](#ref-4). The Sprint Backlog is now *"by and for the
Developers"* in that sense [[1]](#ref-1).

The through-line: the artifact grew a clearer purpose (the Sprint Goal as its "why") and shed the
contract-like language ("commitment" on the item list) that made teams treat a forecast as a promise.

---

## 3. Anatomy (section by section)

The template's sections follow the Scrum Guide's three-part composition, with the heavier planning
apparatus in the full variant.

### Frontmatter and ownership

The document names the sprint, its dates, the team, and the status. **Ownership is the Developers'**: the
Scrum Guide is explicit that the Sprint Backlog is *"a plan by and for the Developers"* [[1]](#ref-1).

*Beginner note:* keep the last-updated stamp current. The Sprint Backlog is a *"highly visible, real-time
picture"* [[1]](#ref-1); a stale one has stopped being a Sprint Backlog.

*Expert note:* the ownership line is not bureaucratic. When a Product Owner or manager edits the plan, the
Developers stop owning their forecast, and the forecast stops being honest. The Product Owner shapes the
*what* by ordering the product backlog and proposing the goal; the *how* is the Developers' alone.

### Sprint Goal

The single objective for the Sprint: the "why" that gives the selected work coherence. The Scrum Guide
calls it *"the single objective for the Sprint"* that *"creates coherence and focus, encouraging the Scrum
Team to work together rather than on separate initiatives"* [[1]](#ref-1).

*Beginner note:* write one goal, as an outcome, not a list of items. Roman Pichler frames it as *"the
purpose of a sprint ... why it's worthwhile undertaking the sprint"* [[10]](#ref-10).

*Expert note:* the goal is selected *first*, and the items follow from it. Pichler's sequencing is
explicit: *"I first select the goal. Then I explore which epics have to contribute to it"* [[10]](#ref-10).
The goal is also the source of the artifact's flexibility: because the commitment is the objective, the
exact items can change mid-Sprint without breaking the commitment ([section 6](#6-debates-and-contested-boundaries)).

### Selected Items

The Product Backlog items the Developers pulled into this Sprint, ordered by their contribution to the
goal. This is the "what".

*Beginner note:* each item is a Sprint-sized piece of value with a clear owner or none (the team pulls).
The items are drawn from the top of the product backlog, not invented here.

*Expert note:* the selection is the Developers' forecast, informed by the goal and their capacity. The
Guide ties confidence to knowledge: *"The more the Developers know about their past performance, their
upcoming capacity, and their Definition of Done, the more confident they will be in their Sprint
forecasts"* [[1]](#ref-1). Pichler adds that the team may push back: *"the team has the right to push
back"* if not all the goal's items fit [[9]](#ref-9).

### Delivery Plan

The "how": the actionable plan for turning the selected items into a done Increment, at enough detail to
inspect progress daily.

*Beginner note:* break the work down enough to see movement day to day; many teams decompose items into
tasks of a day or less. The plan is a means, not a deliverable.

*Expert note:* the Guide requires only that the plan be *"actionable"* and detailed enough for the Daily
Scrum [[1]](#ref-1); it prescribes no task format. It is emergent: *"the Sprint Backlog is updated
throughout the Sprint as more is learned"* [[1]](#ref-1). The plan is where over-specification wastes the
most effort, because it is the part most certain to change.

### Capacity and Forecast *(full variant only)*

How much the Developers can take on, and the basis for the forecast: capacity, velocity, and the buffer
for the unplanned.

*Beginner note:* do not fill the Sprint to the brim. Mike Cohn advises leaving *"room at the top of the
rectangle for unplanned time"* [[7]](#ref-7).

*Expert note:* capacity and velocity are different measures and easy to confuse. Cohn: capacity is a
team's *"plannable time ... the vertical intercept on your sprint burndown chart ... distinct from
velocity, which should always be measured in the units used on a team's product backlog items, usually
story points"* [[7]](#ref-7). Two selection styles follow: **velocity-driven** (pull items until their
points equal the team's average velocity, on the premise that *"the amount of work a team will do in the
coming sprint is roughly equal to what they've done in prior sprints"* [[6]](#ref-6)) and
**capacity-driven** (task the work out in hours and stop when the hours are full, using velocity only as
an after-the-fact check), which Cohn now prefers [[5]](#ref-5). Whichever, it is a *forecast*: *"the
team's commitment not be viewed as a guarantee"* [[5]](#ref-5).

### Progress and Tracking *(full variant only)*

How the Developers make progress visible and re-plan daily.

*Beginner note:* pick one visualization (a board, a burndown) and keep it current; the point is to see
progress toward the goal, not to produce a chart.

*Expert note:* the 2020 Guide deliberately **deprescribed** the burndown: *"Various practices exist to
forecast progress, like burn-downs, burn-ups, or cumulative flows. While proven useful, these do not
replace the importance of empiricism"* [[1]](#ref-1). Tracking is in service of the Daily Scrum's
re-planning, not a management report ([section 6](#6-debates-and-contested-boundaries)).

### Risks and Carry-over *(full variant only)*

The dependencies and risks to the Sprint Goal, and what happens to unfinished work.

*Beginner note:* name what could stop the goal, and decide up front how you will handle work that does not
finish (it returns to the product backlog for re-ordering, not automatically into the next Sprint).

*Expert note:* carry-over is a signal, not a scheduling detail. Unfinished items go back to the product
backlog, where the Product Owner re-orders them against everything else, because a forecast that did not
land is new information, not a debt to be silently rolled forward.

---

## 4. Variants and sizing

**Lean is the default.** It carries the Sprint Goal, the Selected Items, and the Delivery Plan, which is
exactly the Scrum Guide's three-part composition (why, what, how) [[1]](#ref-1). For most teams running
most Sprints, that is the whole artifact: a goal, the items, and the plan, kept live on a board.

**Full adds the planning apparatus**: Capacity and Forecast, Progress and Tracking, and Risks and
Carry-over. The shared sections keep their names and order, so lean is a strict subset of full.

The signal to scale up is **planning weight**, not Sprint length:

- The team wants to make its **capacity and forecasting basis** explicit (velocity or hours), for example
  while it is still calibrating [[5]](#ref-5)[[7]](#ref-7).
- **Tracking and re-planning** need to be legible to more than the team (a scaled setting, a new team).
- The Sprint carries **real dependencies or carry-over risk** worth naming up front.

Otherwise, lean. A settled team with a clear goal and a task board does not need a capacity spreadsheet
and a risk section to run a Sprint; that is planning theater around a plan the team already holds in
common.

---

## 5. Methodology lineage

The Sprint Backlog is a **Scrum artifact**, and unlike the product backlog (a general agile concept), it
is genuinely specific to time-boxed iteration.

- **Scrum** owns and defines it: one of three artifacts, composed of Sprint Goal + selected items + plan,
  owned by the Developers, committed via the Sprint Goal [[1]](#ref-1)[[3]](#ref-3).
- **Kanban and flow-based methods** have no direct equivalent, because they do not batch work into a
  Sprint; work is pulled continuously against WIP limits rather than selected into a time-box. A Sprint
  Backlog only makes sense where there is a Sprint.
- **Scrumban and scaled frameworks** keep a Sprint Backlog where they keep Sprints, layering flow
  practices (a board, WIP limits) on top of the Scrum selection.

The planning *practices* around it, though, are not Scrum-prescribed and vary by school: velocity-driven
versus capacity-driven selection [[5]](#ref-5)[[6]](#ref-6), hours versus points versus no task estimates
[[8]](#ref-8), and burndown versus board versus nothing [[1]](#ref-1). The Scrum Guide
deliberately leaves these to the team; this template treats them as the full variant's optional apparatus,
not as required structure.

---

## 6. Debates and contested boundaries

### 6.1 Forecast or commitment (the live one)

The Scrum Guide says **forecast**; it changed away from "commitment" in 2011 [[3]](#ref-3), on the
widely-held reading that a forecast treated as a promise turns velocity into a target and punishes
learning. It then reintroduced
"commitment" in 2020, but only for the **Sprint Goal**, not the item list [[3]](#ref-3)[[4]](#ref-4). The
practitioner world has not fully followed. Mike Cohn keeps "commitment" but qualifies it hard: *"the
team's commitment not be viewed as a guarantee"* [[5]](#ref-5), a team-to-team promise rather than
a management deliverable, a reading Calabrese traces in detail [[12]](#ref-12). Atlassian, at the vendor
end, tells teams to *"get verbal approval from everyone in the room about what the team is actually
committing to shipping"* [[11]](#ref-11), which is squarely the contract framing the Guide moved away from.

*This bundle's reading:* use **forecast** as the canonical word and commit to the **Sprint Goal**. The
template's Sprint Goal section is the commitment; the Selected Items are the forecast. Where a team wants
the felt weight of "commitment", scope it as Cohn does (to one another, not a guarantee), never as a fixed
list owed to management.

### 6.2 Velocity as a measure, not a target

Velocity is a useful selection input and a corrosive target. Cohn's capacity-driven method uses velocity
only as an after-the-fact sanity check [[5]](#ref-5); the vendor guide uses it as the primary input to
"compile a suggested set of stories" [[11]](#ref-11). The failure mode is treating velocity as a goal to
push up, which drives teams to inflate estimates or cut quality. The template carries capacity and
velocity as *forecast inputs*, and the guide names velocity-as-a-target as an anti-pattern.

### 6.3 How to estimate the plan (or whether to)

At the Sprint Backlog level there are three camps: task-hours, task-points, and no task estimates. Cohn
argues against task-*points* specifically, because *"a more granular unit already exists ... hours"*, and
that *"those who will do the work should ultimately be the ones who establish the estimate"* [[8]](#ref-8);
the no-estimates camp drops even hours. The Scrum Guide prescribes no format, requiring only an
"actionable" plan [[1]](#ref-1). The template stays neutral: the plan needs enough detail to inspect daily
progress, and how you get there is the team's call.

### 6.4 Can scope change mid-Sprint

Older practice treated the Sprint's scope as locked once planned. The 2020 Guide took the other position:
*"Scope may be clarified and renegotiated with the Product Owner as more is learned"* [[1]](#ref-1). The
exact items can flex because the commitment is the objective, not the list: the goal is fixed, the items
are not. Teams trained on earlier editions sometimes still treat scope as locked once planning closes, so
this is settled in the Guide but not universally in practice.

### 6.5 Consent or commitment to the Sprint Goal

A smaller tension worth naming: the Scrum Guide frames the Sprint Goal as something the Developers
*commit* to by the close of Sprint Planning, while Roman Pichler frames the Product Owner's role as
*proposal and consent*, advising you *"never try to force a sprint goal onto the team"* [[10]](#ref-10).
These are not opposed so much as two ends of the same act: the goal is proposed and shaped
collaboratively, then committed to. Where they differ is emphasis, and a team that treats "commitment" as
imposition has missed the collaborative half.

---

## 7. Anti-patterns and failure modes

1. **The Product Owner's list.** A Sprint Backlog dictated or edited by the Product Owner or a manager,
   violating that it is *"by and for the Developers"* [[1]](#ref-1). The PO orders the product backlog and
   proposes the goal; the Developers own this plan.
2. **The forecast as a contract.** Treating the selected items as a promise to ship exactly those, which
   turns a forecast into a stick and punishes the team for learning [[3]](#ref-3)[[5]](#ref-5). Commit to
   the Sprint Goal; forecast the items.
3. **Velocity as a target.** Pushing velocity up as a goal, which inflates estimates and erodes quality;
   Cohn positions velocity as an after-the-fact check, not a number to hit [[5]](#ref-5). Velocity is a
   measure, not a target.
4. **The goalless sprint.** A Sprint Backlog that is a list of unrelated items with no Sprint Goal, so the
   work has no coherence and no basis for renegotiation [[1]](#ref-1)[[10]](#ref-10).
5. **Over-filling the Sprint.** Planning to 100% of capacity with no buffer for the unplanned, so any
   surprise blows the Sprint [[7]](#ref-7). Leave room.
6. **The frozen plan.** A Sprint Backlog written once at planning and never updated, so it stops being the
   *"real-time picture"* it is meant to be [[1]](#ref-1). Update it as you learn.

---

## 8. Relationships to other artifacts

The Sprint Backlog sits one level below the product backlog and one level above the running work.

- **Drawn from:** the **[product backlog](../product-backlog/product-backlog_companion.md)**. The Selected
  Items are a Sprint-sized subset pulled from the top of the ordered product backlog; the Sprint Backlog
  does not duplicate it, it draws from it [[1]](#ref-1).
- **Contains:** the selected **[user stories](../user-stories/user-stories_companion.md)** and other items,
  decomposed into the delivery plan.
- **Committed by:** the **Sprint Goal**, its formal Scrum commitment, which fixes the objective while the
  items stay a forecast [[1]](#ref-1)[[3]](#ref-3).
- **Produces:** the **Increment**, which must meet the team's Definition of Done; the Guide's
  artifact-commitment framework pairs the Increment with the Definition of Done just as it pairs the Sprint
  Backlog with the Sprint Goal [[3]](#ref-3).
- **Feeds:** the **Daily Scrum** (which re-plans the rest of the Sprint against it [[1]](#ref-1)) and,
  at the Sprint's end, the **retrospective** (unfinished items return to the product backlog for
  re-ordering, not silently into the next Sprint).

---

## 9. Adaptations

- **Settled Scrum teams.** The lean variant on a task board is the whole artifact: a goal, the items, the
  plan, kept live. Resist adding a capacity spreadsheet the team does not need.
- **New or calibrating teams.** The full variant's Capacity and Forecast section earns its place while the
  team is still learning its velocity and how full to fill a Sprint [[5]](#ref-5)[[7]](#ref-7).
- **Kanban and flow teams.** There is no Sprint Backlog without a Sprint. If you pull continuously against
  WIP limits, this artifact does not apply; use a flow board and forecast with cycle time instead.
- **Scaled settings.** Where multiple teams share a cadence, keep each team's Sprint Backlog its own
  (Developers own it) and make the cross-team dependencies explicit in the Risks and Carry-over section.
- **Product Owner's part.** Across all of these, the Product Owner prepares the backlog *before* planning
  and proposes the goal, but does not own the plan: *"carry out the necessary prep work prior to the sprint
  planning meeting"* and *"never try to force a sprint goal onto the team"* [[9]](#ref-9)[[10]](#ref-10).

---

## 10. Worked example

[`sprint-backlog_example.md`](sprint-backlog_example.md) is a full-variant Sprint Backlog for a sprint of
the same fictional **"Saved Views for Dashboards"** feature the `delivery-docs` family's examples chain on.
It draws its selected items from the top of the
[Saved Views product backlog](../product-backlog/product-backlog_example.md) (the storage enabler and the
first save-and-reopen stories), sets a Sprint Goal ("a Recurring Analyst can save a view and reopen it"),
lays out the delivery plan, and shows capacity as a forecast, a board-based tracking approach, and honest
carry-over. It demonstrates the Sprint Backlog as the tactical layer directly below the product backlog:
the product backlog is the ordered whole, and this is one Sprint's forecast against one goal.

---

## References

Tagged by reliability: `[primary]` standards body, regulator, or originating source; `[practitioner]`
recognized independent authority or canonical writing; `[vendor]` commercially motivated, reliable on
convention; `[reference]` consolidated secondary. Researched 2026-07-21; per-source retrieval status is
recorded in [`sprint-backlog_research-log.md`](sprint-backlog_research-log.md). Only sources fetched and
verified are quoted; the 2017 Scrum Guide was fetched through a paraphrasing layer and is cited for the
structural contrast only, not quoted.

<a id="ref-1"></a>[1] Schwaber, Ken and Sutherland, Jeff. "[The 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html)." scrumguides.org (accessed 2026-07-21). Supports the three-part composition (Sprint Goal + selected items + actionable plan), ownership by the Developers, the real-time living nature and Daily Scrum connection, the Sprint Goal as commitment and its flexibility, forecast language, mid-Sprint scope renegotiation, and burndown deprescribed. [primary]

<a id="ref-2"></a>[2] Schwaber, Ken and Sutherland, Jeff. "[The 2017 Scrum Guide](https://scrumguides.org/docs/scrumguide/v2017/2017-Scrum-Guide-US.pdf)." scrumguides.org (accessed 2026-07-21). Cited for the pre-2020 structural contrast only (a two-part composition; the Sprint Goal not yet a named component; the "Development Team" role): **the PDF was fetched through a paraphrasing layer and is not quoted.** [primary]

<a id="ref-3"></a>[3] Schwaber, Ken and Sutherland, Jeff. "[Scrum Guide Revisions](https://scrumguides.org/revisions.html)." scrumguides.org (accessed 2026-07-21). Supports the 2011 change from "commitment" to "forecast" and the 2020 introduction of artifact commitments ("the Sprint Backlog has the Sprint Goal"). [primary]

<a id="ref-4"></a>[4] Linders, Ben (with Ken Schwaber and Jeff Sutherland). "[Changes in the 2020 Scrum Guide: Q&A](https://www.infoq.com/articles/changes-2020-Scrum-guide/)." InfoQ, 2020-12 (accessed 2026-07-21). Supports the elimination of the separate Development Team role to reduce "us and them" behavior and the reintroduction of commitments to provide focus. [practitioner]

<a id="ref-5"></a>[5] Cohn, Mike. "[Capacity-Driven Sprint Planning](https://www.mountaingoatsoftware.com/blog/capacity-driven-sprint-planning)." Mountain Goat Software (accessed 2026-07-21). Supports capacity-based selection (task the work out, stop when full), velocity as an after-the-fact check, and the commitment-is-not-a-guarantee qualifier. [practitioner]

<a id="ref-6"></a>[6] Cohn, Mike. "[Velocity-Driven Sprint Planning](https://www.mountaingoatsoftware.com/blog/velocity-driven-sprint-planning)." Mountain Goat Software (accessed 2026-07-21). Supports velocity-driven selection and the principle that past output predicts the next Sprint's ("the amount of work a team will do in the coming sprint is roughly equal to what they've done in prior sprints"). The phrase "yesterday's weather" is a practitioner name for this principle and is not quoted from this page. [practitioner]

<a id="ref-7"></a>[7] Cohn, Mike. "[How Full to Fill a Sprint](https://www.mountaingoatsoftware.com/blog/how-full-to-fill-a-sprint)." Mountain Goat Software (accessed 2026-07-21). Supports the capacity (plannable hours) versus velocity (story points) distinction and leaving an unplanned-time buffer. [practitioner]

<a id="ref-8"></a>[8] Cohn, Mike. "[Don't Estimate the Sprint Backlog Using Task Points](https://www.mountaingoatsoftware.com/blog/dont-estimate-the-sprint-backlog-using-task-points)." Mountain Goat Software (accessed 2026-07-21). Supports the task-hours versus task-points versus no-estimate debate and that those doing the work should estimate it. [practitioner]

<a id="ref-9"></a>[9] Pichler, Roman. "[Sprint Planning Tips for Product Owners](https://www.romanpichler.com/blog/sprint-planning-tips-for-product-owners/)." romanpichler.com (accessed 2026-07-21). Supports backlog readiness before the event, a collaborative Sprint Goal, and the team's right to push back on scope. [practitioner]

<a id="ref-10"></a>[10] Pichler, Roman. "[The Product Owner's Guide to Effective Sprint Goals](https://www.romanpichler.com/blog/effective-sprint-goals/)." romanpichler.com (accessed 2026-07-21). Supports the Sprint Goal as the purpose of the Sprint, goal-first sequencing (select the goal, then the items that serve it), and consent over imposition ("never try to force a sprint goal onto the team"). [practitioner]

<a id="ref-11"></a>[11] Atlassian. "[4 Best Practices for Sprint Planning Meetings](https://www.atlassian.com/blog/agile/sprint-planning-atlassian)." atlassian.com (accessed 2026-07-21). Supports backlog grooming before planning and velocity as a selection input; its "committing to shipping" framing is cited as the vendor end of the forecast-versus-commitment debate. [vendor]

<a id="ref-12"></a>[12] Calabrese, Jake. "[Scrum Commitment or Forecast](https://helpingimprove.com/scrum-commitment-or-forecast/)." helpingimprove.com (accessed 2026-07-21). Supports the version-by-version history of the commitment-to-forecast shift and the practitioner view that "commitment" retains a narrower team-to-team meaning after the official change. [practitioner]
