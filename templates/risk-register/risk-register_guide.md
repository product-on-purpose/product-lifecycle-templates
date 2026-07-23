# Guide: Risk Register (operator card)

Fast reference for using the risk-register bundle. For the full reasoning, history, and sources, read
[`risk-register_companion.md`](risk-register_companion.md).

## When to use

- You have an **objective, project, or program** with uncertain events that could threaten (or help) it, and
  you need one owned, ordered record of them.
- You need to **track risk over time** and show what you are doing about each one and whether it is working.
- Risk visibility must be **shared and auditable** across a team, a steering group, or a regulator, not held
  in one person's head.
- You are managing risk that **spans the whole lifecycle**, not a single phase: a register is a standing
  instrument, maintained continuously.

## When NOT to use

- **The problem has already happened.** That is an **issue**, not a risk. Track it in an issue log; the
  register is for potential future events. A row describing a present problem is misfiled.
- **You also need to track assumptions and dependencies.** Use a RAID log (Risks, Assumptions, Issues,
  Dependencies) as the one working document; the risk register is the deepened "R", worth splitting out only
  when the R has outgrown the RAID. (`raid-log` is the next governance-docs bundle to be built.)
- **You are a single agile team and the overhead exceeds the value.** For small-to-medium agile work, short
  iterations retire risk continuously; a lightweight lean register refreshed each iteration may be all you
  need, or a risk-burndown chart instead. Scale and regulation are what make the full register worth it.
- **You are setting the rules for risk, not listing risks.** That is a risk management plan / approach (your
  categories, scales, appetite, roles), which governs the register but is a different document.

## Register, RAID log, or issue log? (the question people actually have)

| | **Risk register** | **RAID log** | **Issue log** |
|---|---|---|---|
| Tracks | Risks (potential future events) | Risks + Assumptions + Issues + Dependencies | Problems that have already happened |
| Time frame | Might happen | Mixed | Has happened |
| Cadence | Weekly to quarterly, by scale | Weekly working document | Near-daily |
| Audience | Owners, steering group, board | The delivery team | Whoever must resolve it now |
| Relationship | The deepened "R" of RAID | The consolidated working log | Where a materialized risk goes |

They are a system, not a choice: a risk that materializes **leaves** the register for the issue log, and a
strategic risk surfaced in the weekly RAID review **gets promoted up** into the register. Pre-decide the
trigger that moves a risk to the issue log; that is what the trigger/KRI column is for.

## Pick a variant

- **Lean** (default): Purpose and Scope, Scoring Scale, Risks, Review and Ownership. A complete working
  register for one team acting on its own risks, with a single score per risk.
- **Full**: adds dual (inherent and residual) scoring and columns (category, trigger, owner/actionee,
  proximity), an Escalation and Risk Appetite section, and a Closed and Materialized Risks audit trail. Use
  it when a steering committee, auditor, or board consumes the register, when you must demonstrate control
  effectiveness, or when regulation prescribes fields.

Grow lean into full by adding sections and columns; never reorder the shared four. The scaling signal is
**governance and audience**, not project size.

## Quality rubric (self-grade)

- [ ] The register **names the objective** the risks threaten, and who owns the register.
- [ ] The **scoring scale is anchored** (each likelihood level a frequency, each impact level a consequence),
      not bare High/Medium/Low.
- [ ] Every risk is a **cause -> event -> consequence** statement, not a theme label.
- [ ] Every risk has **one named owner** (a person, never a team) and a **specific response** (strategy +
      action).
- [ ] Risks are **ordered by score**, highest first, and the score is treated as a triage signal, not a
      precise measurement.
- [ ] There is a **stated review cadence** and an event trigger for off-cycle updates; the last-reviewed date
      is current.
- [ ] No row describes something that **has already happened** (that belongs in the issue log).
- [ ] (Full) Each risk has **inherent and residual** scores, and the gap is your response-effectiveness
      evidence. For threats, residual < inherent (controls reduce it); for opportunities being **enhanced**,
      residual > inherent (the action raises the odds of capture). In both directions the gap shows the
      response is working.
- [ ] (Full) There is a **measurable risk appetite** and a clear **escalation** threshold and path.
- [ ] (Full) Closed and materialized risks are **kept as an audit trail**, with reasons and dates, not
      deleted.

## Named anti-patterns (the usual wrecks)

1. **Risk theater (set-and-forget).** Created at kickoff, filed, never revisited until the next audit. The
   signature failure. Fix: a stated cadence and event triggers, and a last-reviewed date you keep current.
2. **Unanchored ratings.** "High" and "low" with no scale behind them, so two people score the same risk
   differently. Fix: anchor every level to a frequency and a consequence.
3. **Theme labels, not risk statements.** A row that says "security" or "budget" cannot be scored, owned, or
   closed. Fix: write cause -> event -> consequence.
4. **Ownerless risks.** A risk owned by "Engineering" is owned by no one. Fix: name an individual; split
   owner and actionee only when the owner cannot execute personally.
5. **Inherent-only scoring.** Recording risk before controls but never after, so the register cannot show
   whether its mitigations work. Fix: carry the residual score and keep it below inherent where controls act.
6. **The register that became an issue log.** Rows describing things that already happened, mixed in with
   genuine risks, hiding what needs action now. Fix: move materialized risks to the issue log the day their
   trigger fires.

## No paired skill (yet)

There is **no `deliver-risk-register` or `govern-risk-register` skill** in the product-on-purpose org today,
so this bundle's `pairs_with` is empty. Until one exists, this template is filled by hand.
