# Guide: Business Continuity Plan (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`business-continuity-plan_companion.md`](business-continuity-plan_companion.md). A fully worked instance is
[`business-continuity-plan_example.md`](business-continuity-plan_example.md).

## When to use

- A named set of critical business processes needs to keep running through a significant disruption, and
  recover afterward, and you want that response agreed and rehearsed before the disruption happens, not
  argued out while it is already underway.
- More than one person might have to activate or run this plan, so the activation authority, a named
  successor, and the team's own roles need to be written down rather than carried in one person's head.
- A Business Impact Analysis already exists, or is being built alongside this plan, and you need a place to
  carry its Recovery Time Objectives and Recovery Point Objectives into concrete continuity strategies, and,
  in the full variant, a recovery strategy for each critical system.
- You want the plan rehearsed on a schedule, with an observer independent of the team being exercised, and
  every finding turned into an owned, dated fix rather than a note nobody revisits.
- You want a document that states the specific events that would make it wrong, with a named owner, instead
  of a calendar reminder nobody actually reads before renewing it.
- Your organization is regulated, or contracts with suppliers who are, and the plan's own update and
  disclosure triggers need to be stated rather than assumed.

## When NOT to use

- **You need the procedure for one known alert or operational situation, not the standing plan for a
  significant business disruption.** That is a runbook: one operational procedure for a known, narrower
  situation. This plan's Disaster Recovery section can call out to a runbook; it is not a bigger
  runbook itself.
- **You are checking a service's standing fitness to be handed off and run day to day.** That is a
  production readiness review, which starts at a routine handoff. This plan starts once a disruption is
  declared or a drill begins, not at a routine handoff.
- **You are writing up what happened after one disruption that has already resolved.** That is an incident
  postmortem, or the dated record of one activation of this plan. A plan that only describes one real event
  after it happened is a narrower artifact than the standing plan this bundle templates.
- **You are tracking potential future events on an ongoing basis, before any of them has actually
  happened.** That is a risk register. This plan is the designed response once a tracked, or untracked, risk
  actually crystallizes into a disruption.
- **Your "disaster recovery" need is really a technical high-availability design.** High availability and
  disaster recovery are related but not the same thing, and a technical high-availability design, by itself,
  is not this plan's Disaster Recovery section.
- **You want a standard every increment of work is judged against, on a cadence.** That is a definition of
  done. Both are standing-standards siblings, but a definition of done governs whether an increment of work
  is finished, and this plan governs whether the organization can keep operating through a disruption.

## Pick a variant

**Lean (eight sections)** is Purpose and Scope, Business Continuity Team and Roles, Business Impact Analysis
Summary, Continuity Strategies and Manual Workarounds, Activation and Incident Management, Training, Testing
and Exercising, Plan Administration, and Review Trigger. Use it when a separate, standalone disaster
recovery plan already exists: Purpose and Scope points to it by name and location, the shape FEMA's own
template allows, rather than this plan duplicating it.

**Full (nine sections)** adds Disaster Recovery immediately before Review Trigger: the recovery strategy for
each critical system, backup and offsite storage including at least one offline copy, recovery procedures
written so another trained person could follow them, the recovery order across dependent systems, restore
verification, and the recovery test. Use it once no separate disaster recovery plan exists and this plan
needs to carry that detail itself.

No source read for this bundle states a sizing signal more specific than that one choice, whether a separate
disaster recovery plan already exists. Every lean heading appears in full unchanged, in the same order, so
growing from lean to full is additive. You never reorder or rename a section you already filled in.

## Quality rubric (self-grade)

Score each 0, 1 or 2. Full below 12 out of 18 ships a plan that reads complete on the page but fails exactly
when a disruption actually happens: an authority nobody can reach, a workaround nobody has described, or a
recovery nobody has tested. Lean is scored on 8 of these 9 rows only (row 8, Disaster Recovery, applies only
to full; see the scope table below), and below 11 of 16 the same failure applies to the smaller shape.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Scope is bounded** | No disruption is defined, or the plan reads as though it covers everything with no stated boundary | A disruption is defined, but a reader cannot tell whether disaster recovery detail lives in this document or elsewhere | A significant disruption is defined in plain language for this specific business, and the document says, by name, whether disaster recovery detail lives in this plan's own section or in a separate, named document |
| 2 | **Authority named and succeeded** | No one is named with authority to activate this plan | An authority is named, but with no successor, or the successor has no stated title | One named job title has authority to activate, a named successor is stated, and the document says what happens if normal channels of direction are themselves disrupted |
| 3 | **Impacts and dependencies concrete** | Recovery Time Objective or Recovery Point Objective rows read "TBD" or carry no unit of time | Some rows state concrete time units, but dependencies are left as "various" or blank | Every critical process states its Recovery Time Objective and Recovery Point Objective in concrete time units, and names the specific systems and suppliers it depends on |
| 4 | **Workarounds describe actual steps** | A workaround is asserted to exist, with no description of what anyone actually does | Some workarounds describe steps; others stop at asserting one exists, or no recovery level is explained | Every workaround states what staff actually do, step by step, and the recovery level chosen and why, weighed against its cost |
| 5 | **Activation sequence is checkable** | No stated activation criteria, no notification order, or no stand-down condition | Criteria and a notification list exist, but the order is unclear, or no method is stated for a channel that might be down | Specific activation criteria are stated in advance, notifications go out in a stated order by a method that still works if the usual channel is down, and a stand-down condition is named |
| 6 | **Findings owned and observed** | No exercise is recorded, or the only observer is the team being exercised | An exercise is recorded, but at least one finding carries no owner, no date, or the observer is not independent of the team | An exercise type and date are recorded, observed by someone independent of the team being exercised, and every finding carries a named owner and a due date |
| 7 | **Plan reachable offline** | No location is stated for a copy of the plan, or the only copy sits on the network the plan exists to recover | A location is stated, but it is not clearly outside the systems this plan protects, or no master-copy holder is named | A master-copy holder is named, and a reachable, offline copy is kept somewhere that does not depend on the systems this plan protects |
| 8 | **Recovery actually tested** *(full)* | A system is listed with "we have backups" and nothing else | A recovery strategy is named for some systems, but no dependency order is stated, or no restore test has actually been run | Every critical system names a recovery strategy, its position in the recovery order relative to what it depends on, and the result of an actual restore test, not only a scheduled one |
| 9 | **Trigger names events** | Only a calendar date is named, or nothing at all | An event is named, but with no owner, or an annual exercise requirement stands in as the only trigger | Specific conditions are named (a change in people, suppliers, systems, facilities, the business, or the Business Impact Analysis; an activation; an exercise or test finding), each paired with a named owner, with any required annual exercise stated as a floor under those conditions rather than as the trigger itself |

**Which rows apply to what.**

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| full | all 9 | 18 | **12** |
| lean | 1-7 and 9 | 16 | **11** |

Row 8 is scored only against full. Lean ships no Disaster Recovery section of its own, carrying a pointer to
a separate plan instead, so grading it on that row would penalize the choice of variant rather than the
quality of the document.

The test behind every cell above: could someone satisfy it without improving the document? A row that
counted workaround rows, vendor rows, or exercise findings would reward padding. Every cell instead asks
whether a specific piece of evidence exists, and whether a second person, not the author, could check it
without asking who wrote the document.

## Named anti-patterns (the usual wrecks)

1. **Neglect, because disasters are rare.** SANS's disaster recovery policy template says it plainly:
   management often ignores the planning process because disasters happen so rarely. The same rarity is why
   nobody notices the plan going stale until the day it is needed.
2. **Disaster recovery bolted on late.** A system grows complex and interdependent first, and only once it is
   already load-bearing does anyone ask how it would recover, by which point the honest answer is "with
   difficulty."
3. **Backups nobody has restored.** Having backups is not the same claim as having a recovery. A backup
   schedule with no restore test behind it is a belief, not a capability, and the gap stays invisible until
   the restore is the only option left.
4. **The rarely used path breaks first.** The parts of a system that only run during a disaster get no
   routine exercise, so, as Google engineer Tanya Reilly says in an interview on disaster recovery plans,
   they need the most deliberate testing. Left untested, they fail at the moment they are needed.
5. **A test that does not exercise the people who will recover.** Watching someone else's staff run a
   recovery from backup tapes, or testing only the technical process, confirms nothing about whether your own
   team could actually execute it under pressure.
6. **Dependency deadlock during recovery.** Two systems that each wait on the other to start can strand a
   recovery indefinitely if the order of recovery was never written down and checked against what each
   system actually depends on.
7. **Stale contacts and documentation.** The people, numbers, and procedures a plan names need more frequent
   review than the rest of its content, and a recovery exercise is one way to find out that a contact list
   or a procedure has quietly gone out of date.
8. **The plan itself unreachable during the outage.** Keeping the only copy of this plan on the network, or
   in the facility, it exists to recover means it is unreachable at exactly the moment someone needs to read
   it. This is a stated precaution in the sources this bundle read, not a measured failure, and it is named
   here on that honest footing.

## Pairing with your process

This bundle ships in the `standing-standards` family alongside `definition-of-done`, `definition-of-ready`,
`launch-coordination-checklist`, `production-readiness-review` and `runbook`, as a **tool**: a plan a team
executes under time pressure once a disruption is declared or a drill begins, not a standard the team is
judged against on a cadence. A runbook is the procedure for a known, narrower operational situation;
this plan is the procedure for a significant disruption to the business itself, and its Activation and
Incident Management section is the seam where an organization's own incident response runbook picks up. A
production readiness review checks a service's standing fitness to be handed off and run day to day; this
plan does not duplicate that check, and a service's own backup and disaster recovery responsibility can sit
entirely inside this plan instead, named rather than re-derived. Update this file when the plan itself needs
to change, not every time it is activated or drilled.
