# Guide: RAID Log (operator card)

Fast reference for using the raid-log bundle. For the full reasoning, history, and sources, read
[`raid-log_companion.md`](raid-log_companion.md).

## When to use

- You are running a **project or program** and need one place to hold everything open: risks, assumptions,
  issues, and dependencies.
- The work has **more than one kind of open item** and you want to see them together, so you can catch an
  assumption becoming an issue or a dependency becoming a risk.
- You need a **weekly working document** the delivery team actually reviews, not a one-time governance filing.
- You want **shared, owned visibility** of what could derail delivery, with one named owner per item.

## When NOT to use

- **The item has already happened and is the only thing you track.** A single realized problem is an
  **issue**; if that is all you have, an issue log is enough. RAID earns its keep when you track all four
  kinds together.
- **You need audit-grade risk scoring.** The RAID log's R is a summary. For inherent-versus-residual scoring,
  triggers, and appetite, use a standalone [risk register](../risk-register/risk-register_guide.md) and let
  the RAID R point to it.
- **You will not review it.** A RAID log nobody reviews is documentation theater. If you cannot commit to a
  cadence, do not create one; a stale log is worse than none because it misleads.
- **You are writing the status report itself.** The RAID log is the raw material for a status report, not the
  report. Draw on it; do not send the whole log.

## RAID log, risk register, or issue log? (the question people actually have)

| | **RAID log** | **Risk register** | **Issue log** |
|---|---|---|---|
| Tracks | Risks + Assumptions + Issues + Dependencies | Risks only, deeply | Realized problems only |
| Depth | Working summary | Audit-grade (inherent/residual, triggers, appetite) | Resolution-focused |
| Cadence | Weekly working review | Weekly-to-quarterly by scale | Near-daily |
| Audience | The delivery team | Steering group, board, auditors | Whoever resolves it now |
| Relationship | The consolidation layer | The deepened "R" of RAID | Where a materialized risk goes |

They are a system: the RAID log's **R** is the summary the [risk register](../risk-register/risk-register_guide.md)
deepens, and its **I** is where a materialized risk lands. Promote strategic risks up into the register;
migrate materialized risks into issues.

## Pick a variant

- **Lean** (default): Purpose and Scope, Risks, Assumptions, Issues, Dependencies, Review and Ownership. A
  complete working log for one team, often a single combined table.
- **Full**: adds richer per-quadrant fields (validation dates, severity-vs-priority, dependency direction and
  type), an Escalation and Aging section, and a Cross-Quadrant Summary. Use it for a larger or multi-team
  program, a steering-group escalation view, or when aging and migration tracking matter. Large logs split
  the four quadrants onto four tabs.

Grow lean into full by adding sections and columns; never reorder the shared six. The scaling signal is
**volume and governance**, not project length.

## Quality rubric (self-grade)

- [ ] The scope line **states which expansion of RAID** you are using (Assumptions or Actions; Dependencies
      or Decisions).
- [ ] There is **one named log owner** and **one named owner per item** (never a team).
- [ ] **Risks** are cause-event-consequence statements, not theme labels, and point to the risk register if
      you keep one (no duplicated scoring).
- [ ] **Assumptions** each have an impact-if-false and a validate-by date, not just a description.
- [ ] **Issues** describe things that have **already happened**, with a raised date for aging (nothing
      not-yet-happened is filed here).
- [ ] **Dependencies** mark **direction** (inbound/outbound) and name the specific party and a needed-by date.
- [ ] There is a **stated review cadence** and the last-reviewed date is current.
- [ ] Migrations are handled deliberately: a failed assumption or a materialized risk **becomes an issue**,
      not a stale row in its old quadrant.
- [ ] (Full) Escalated items show their **aging**, and escalation is used to get a decision, not to assign
      blame.
- [ ] (Full) The Cross-Quadrant Summary **interprets** the migration pattern, not just counts rows.

## Named anti-patterns (the usual wrecks)

1. **Documentation theater.** Set up at kickoff, abandoned by week three. The signature failure. Fix: a
   stated weekly cadence and a named owner; a log is only as good as its review rhythm.
2. **The undeclared acronym.** The team never says whether A is Assumptions or Actions, so half of them track
   one and half the other. Fix: declare the expansion in scope and stop relitigating it.
3. **The bloated log.** Every tiny detail logged until nobody can find anything and reviews cause decision
   paralysis. Fix: scope what belongs; escalate and archive.
4. **Ownerless items.** A row owned by "the team" is owned by no one. Fix: a named person per item.
5. **The mislabeled quadrant.** A not-yet-happened problem filed as an issue, or a present problem filed as a
   risk. Fix: a risk might happen, an issue has happened; migrate deliberately between them.
6. **The blame register.** Using escalation to assign fault instead of to get a decision, which makes people
   stop logging honestly. Fix: escalate to resolve, never to target.

## No paired skill (yet)

There is **no `deliver-raid-log` or `govern-raid-log` skill** in the product-on-purpose org today, so this
bundle's `pairs_with` is empty. Until one exists, this template is filled by hand.
