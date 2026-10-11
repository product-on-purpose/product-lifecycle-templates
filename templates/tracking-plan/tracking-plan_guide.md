# Guide: Tracking Plan (operator card)

Fast reference for using the tracking-plan bundle. For the full reasoning, origins, and sources, read
[`tracking-plan_companion.md`](tracking-plan_companion.md).

## When to use

- The product already records, or is about to record, more than a handful of events, and nobody has one
  place that lists what those events are, why each one is collected, and who answers for it.
- More than one person will add, change, or simply go looking for an event over the product's life, not
  just during one feature's build. A tracking plan is the standing catalog that outlives any single launch.
- A feature's own PRD has already proposed events in its "Analytics and instrumentation" section, and that
  feature is shipping. This plan is what every feature's own slice merges into once it ships, a reading this
  library states as its own position rather than any source's claim (see
  [`tracking-plan_companion.md`](tracking-plan_companion.md#8-relationships-to-other-artifacts), section 8).
- Someone, eventually, will ask what an event's properties are, where it comes from, or whether it is still
  live, and the honest answer today is "ask the person who built it," which is the owner-departure failure
  this bundle's research names as its most fully sourced failure mode (section 7 of the companion).

## When NOT to use

- **No event has been proposed yet, and the team is choosing between autocapture and a hand-built plan.**
  Exactly one source in this bundle's research argues from the autocapture side, and even it does not call a
  plan unnecessary: it names the choice itself "a false choice" and still advises a team to manually capture
  a small, named set of core events to start. Route a team with nothing yet to that short, hand-picked start,
  not to a full catalog it cannot yet fill in honestly.
- **A single feature is proposing its own launch metrics.** That belongs in that feature's own PRD, in its
  "Analytics and instrumentation" section, first. This plan is what the feature's slice merges into once it
  ships, not the place a feature's launch is first drafted.
- **The question is what the data means once it lands in the warehouse.** That is the data dictionary's job,
  stated in the opposite tense from this plan's forward-looking "what you intend to track."
- **The question is why the business tracks a number at all, or what the reporting cadence is.** That is
  the broader measurement plan, which contains a tracking plan but also covers business objectives, KPI
  definitions, and reporting logic this plan does not carry.
- **The question is a metric's own formula or target.** That is the KPI dashboard's Metric Definitions
  section. This plan defines the events a metric is computed from; it does not lock the formula itself.
- **The question is a risk, an open item, or a problem that has already happened.** Those belong in the
  risk register, the RAID log, or the issue log. A tracking-plan failure, such as an event that silently
  stops firing, becomes a row in one of those once someone notices it; it is not a second home for the
  problem inside this plan's own catalog.

### Tracking plan, or one of its three neighbors?

| | **Tracking plan** | **Data dictionary** | **Measurement plan** | **KPI dashboard** |
|---|---|---|---|---|
| Tense | Forward-looking: what you intend to track | Backward-looking: what the data means once implemented | Forward-looking, broader | Defines a metric's own formula and target |
| Scope | Events, properties, traits | Implemented warehouse structure | Business objectives, KPIs, reporting logic, and tracking | One metric at a time |
| Relationship to this plan | N/A | Fed by this plan once implemented | Contains this plan as one part | Consumes the events this plan defines |

A single feature's own launch metrics are not a fourth neighbor on this table: they are this plan's own
future content, first drafted in that feature's PRD and merged here once it ships.

## Pick a variant

- **Lean** (default): Purpose and Boundary, Naming Conventions, Event and Property Catalog, User and Account
  Properties, Review and Ownership. A complete, working plan for a product starting out or a small event
  set, following the research's own framing that a team can start with a document when the event set is
  small, and the advice not to try to track everything at once.
- **Full**: adds **Privacy, Sensitivity and Retention** (which event or property might carry personal data,
  how long it is kept, and what happens to it before storage) and **Change Process and Version History**
  (how a change to the standing plan is proposed and approved, how an event is formally removed, and the
  running record of what changed and who approved it). Move to full once more than one team changes this
  plan, once it holds personal or sensitive data, or once someone will later need to ask what changed and
  who approved it.

Grow lean into full by inserting Privacy, Sensitivity and Retention as the fifth section, before Review and
Ownership, and appending Change Process and Version History last; the first four keep their name, order,
and tables. The
scaling signal is whether the plan holds sensitive data or needs a defined change procedure, not how many
events it lists.

## Quality rubric (self-grade)

Score each row 0, 1, or 2. Below 11 out of 16, the first person who tries to add an event, trace why one
exists, or find out who to ask about it will fail to do so from the plan alone, and will end up asking
around instead of reading the document. A lean plan carries no privacy or change-process section to trace,
so it is scored, and cleared, against a smaller table; see the scope table below.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Boundary rules out neighbors** | No line says what this plan does not cover | A boundary line exists, but it names no specific neighboring document | You can point at the sentence naming at least one neighbor by name (a feature's own PRD slice, the data dictionary, the measurement plan, or the KPI dashboard) and at what it hands that neighbor instead of carrying it here |
| 2 | **Naming convention stated** | No tense, case, or cross-platform answer is given anywhere | A tense and case are named, but nothing says what happens when a platform's own automatic tracking would otherwise produce a different name for the same action | You can point at the stated tense and case, and at the specific fallback for a platform whose automatic tracking would otherwise diverge from it |
| 3 | **Every row answers "why"** | Rows exist with the reason cell blank, or filled with the event name restated | A reason is given for most rows, but at least one event's business question cannot be stated back by a non-analyst | You can point at any row and repeat its business question back in one sentence, because the reason cell answers it rather than restating the event name |
| 4 | **Owner and status named** | An event has no owner, or "owner" is a team name rather than a person | Owners and statuses are present, but the status values are invented per row rather than drawn from one stated vocabulary | You can point at any row's owner (a person) and its status, and the status comes from the vocabulary stated once at the top of the table |
| 5 | **Traits kept apart** | A persistent fact about a user or account is listed as though it were a property of one event | The User and Account Properties table exists, but at least one row leaves the subject (user or account) or the source blank | Every trait names its subject, its type and allowed values, and where it is set, and no persistent fact has leaked into the event catalog above |
| 6 | **Sensitivity at property level** *(full)* | No property is flagged, or a whole event is flagged with no property named | A property is flagged, but the retention period or the handling step before storage is missing | You can point at a specific flagged property, its retention period, and its handling step, and nothing here is presented as settled legal advice |
| 7 | **Change roles named** *(full)* | No one is named as able to propose or approve a change, or "the team decides" is the only statement | A proposer and an approver are named, but nothing says what a reviewer checks before a change ships | You can point at the named role that proposes a change, the named role that approves it, and what a reviewer checks before it ships |
| 8 | **Removal is a procedure** *(full)* | An event's status flips to removed with no record of when or why | A version history exists, but at least one row names no event, no approver, or no date | You can point at a removed event's own row in the version history, naming the event, who approved the removal, and when, rather than a quiet status flip with nothing recorded |

### Rubric scope by variant

| Variant | Rows scored | Maximum | Threshold |
|---|---|---|---|
| lean | 1-5 | 10 | 7 |
| full | 1-8 | 16 | 11 |

Lean ships no Privacy, Sensitivity and Retention or Change Process and Version History section, so rows 6
through 8 grade content it does not carry; score a lean plan against rows 1 through 5 only. A lean plan at
7 out of 10 clears a comparable bar to a full plan at 11 out of 16.

## Named anti-patterns (the usual wrecks)

1. **Owner departure.** The most fully sourced failure mode in this bundle's research: an event with no
   accountable person decays once its author leaves, and nobody left can explain what it means or whether it
   still fires correctly. Fix: a named person, not a team, behind every event, recorded in the catalog's
   owner column from the day the event ships.
2. **Governance treated as a one-time setup.** Writing the plan once and never reopening it is named
   directly in this bundle's research as a primary reason governance programs fail; a plan that is set up,
   documented, and left alone decays the same way an unowned event does. Fix: a stated review interval in
   the Review and Ownership section, actually kept, not written once and forgotten.
3. **Unclear, team-level ownership.** "The analytics team owns it" is named in the research as functionally
   the same as no owner at all, because no single person can be asked when something breaks. Fix: one named
   person per event, full stop, not a team name in the owner column.
4. **No gate before an event ships.** Where no one checks a new or changed event against what the plan
   says before it reaches production, the plan and the live data drift apart silently. Fix: a named
   validation step in the Change Process section, run before an event ships, not only after someone notices
   it is wrong.
5. **A status flip standing in for a removal procedure.** Marking an event "removed" with no record of when
   or who approved it erases exactly the information a later reader needs to know whether the removal was
   deliberate or accidental. Fix: a removal procedure with its own steps, and a version history row naming
   the event, the approver, and the date, every time.
6. **A naming convention with no cross-platform answer.** A convention that states a tense and a case but
   says nothing about what happens when a platform's own automatic screen-tracking produces a different name
   for the same user action lets the same action quietly become two different events. Fix: name the
   fallback in the Naming Conventions section itself, not as a decision made silently per platform later.
7. **The plan outgrowing a spreadsheet, or outgrowing its own boundary with a neighbor.** A plan that has
   scaled past what a spreadsheet can hold reliably is one named, sourced failure shape in this bundle's
   research. A plan that has quietly started carrying a feature's own launch metrics, a metric's formula, or
   a risk is a second, in this library's own reading of where those contents belong; no source names it. Fix: move to a validated tool once the spreadsheet itself becomes the risk, and route
   each neighbor's own content back to its own document rather than letting this plan absorb it.

## No paired skill (yet)

This bundle's family contract states plainly that no governance skill exists in pm-skills today for any of
its six members, so every member adopts `pairs_with: []` until one does. Until a governance-side skill
exists, this template is filled by hand.
