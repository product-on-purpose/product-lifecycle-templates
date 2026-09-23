---
status: proposed
date: 2026-09-23
decision-makers: [jprisant]
consulted: [claude]
---

# `definition-of-ready` joins `standing-standards` as a `foundation`, not a `tool`

## TL;DR

- **Decision.** The `definition-of-ready` bundle declares **`family: standing-standards`** and
  **`classification: foundation`**. It becomes that family's fourth member, beside `definition-of-done`
  (`foundation`), `runbook` (`tool`) and `launch-coordination-checklist` (`tool`), and the
  [contract](../contracts/standing-standards.md) moves to `0.3.0`.
- **Why a record is needed.** The contract forecast this type in 2026-08, before any member was built, but
  it never said which of its two classification values the type would take. Both have been used, and
  [ADR 0053 (launch-coordination-checklist joins standing-standards as a tool)](0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md)
  shows the value is a judgment the gate cannot check.
- **What settled it:** the contract's own cut, applied to the type's mechanics rather than its cadence. A
  Definition of Ready is **a standard items are judged against**, agreed and applied by the same team at a
  scheduled conversation. Nobody executes it under time pressure.
- **The consequence worth recording:** its documented failure mode is the **inverse** of the one the
  contract names for `foundation`, so its review trigger must fire in both directions.
- **What this does NOT decide:** whether the type passes
  [ADR 0030](0030-templating-scope-markdown-documents.md)'s admission test, which is answered by retrieval
  in [`tier2-specs.md`](../tier2-specs.md). **Nor does it endorse keeping a Definition of Ready.** The
  library's own `definition-of-done` and `product-backlog` bundles report the dispute over whether one should
  exist, and this bundle carries that dispute rather than settling it.
- **Status:** **proposed** 2026-09-23, awaiting one word from the maintainer. The instruction that day was
  "complete issue log and delivery ready"; this record reads "delivery ready" as `definition-of-ready`
  (build-candidate 4, GitHub issue #178), and that reading is unconfirmed. The agent drafted the
  classification argument against the contract and ADR 0032. It becomes accepted, and the bundle is built,
  only when the reading is confirmed.

## Context and Problem Statement

[The `standing-standards` contract](../contracts/standing-standards.md) section 1 lists "Likely future
members, if pulled: `definition-of-ready`, and a coding-standards or engineering-handbook document." The
catalog entry (`id: definition-of-ready`, catalog 40, `category: Requirements`, `size_variant: S`) is a
candidate. Under [ADR 0041](0041-maintainer-preference-sets-the-build-order.md) the maintainer's direction
sets the build order; whether the 2026-09-23 instruction ("delivery ready") directed this type is the open
question above (GitHub issue #178).

The contract's axis is a set, `foundation` or `tool`, and its section 2 states the cut: "is it a standard
you judge against, or an instrument you execute?" Check K can verify a member picked a value from the set,
never that it picked the right one. The first three members split two to one the other way, so the
assignment has to be argued.

## Decision Drivers

- The classification must follow what the document **does**, because that is what the contract's cut
  tests, and what the family's review obligations are written against.
- ADR 0053 settled family membership with the family's falsifier (is it consulted at the moment of
  action?) and classification with the cut. Those are two different questions, and conflating them is the
  easiest way to get this one wrong.

## Considered Options

1. **`standing-standards`, `classification: foundation`.** Chosen.
2. **`standing-standards`, `classification: tool`.** The case for it: a DoR is applied at a recurring
   moment, refinement or sprint planning, and ADR 0053 admitted the launch checklist because it is
   "consulted at the moment of action". Rejected below.
3. **`delivery-docs`, beside `product-backlog` and `sprint-backlog`.** Rejected: that contract's members
   carry one unit of product work, and a DoR is written once and applied to every item. The
   `standing-standards` contract's own sentence places it: "A candidate written **once per unit of work**
   belongs to `delivery-docs` or `qa-docs`."

## Decision Outcome

**Chosen: `standing-standards`, `classification: foundation`.**

### Why `foundation`, against each of the contract's markers

The contract gives each value three markers. A DoR matches all three of `foundation`'s and none of
`tool`'s:

| Marker | `foundation` (contract section 2) | `tool` (contract section 2) | A Definition of Ready |
|---|---|---|---|
| What it is | "a standard you are judged against" | "an instrument you execute" | Conditions an item is judged against before entry. It contains no steps |
| When and by whom | "argued to, agreed by a team, and changed deliberately and rarely" | "usually under time pressure and often by someone who did not write it" | Applied by the team that agreed it, in a scheduled refinement or planning conversation |
| Where authority comes from | "from having been agreed" | "from being correct right now" | From the team's agreement. Nothing about it depends on the current state of a system |

**Why option 2 does not carry.** Being consulted at the moment of action is the family's **membership**
falsifier, not its classification test. A Definition of Done is also consulted at a moment, when deciding
whether work is finished, and it is `foundation`. A DoR is that document's entry-side mirror.

### Consequences

- **The contract moves to `0.3.0`.** Its Members line gains the type, and the "likely future members"
  forecast entry moves to Members rather than being deleted, as the `0.2.0` change note did for the launch
  checklist. No obligation changes, and check K's registry entry needs no edit.
- **The review trigger must fire in both directions, and this is the family's sharpest new teaching
  point.** The contract names `foundation`'s failure mode as "being agreed once and never honoured". A
  Definition of Ready's documented failure is the opposite: **being honoured too hard**, as a gate. Mountain
  Goat Software's warning is that a DoR requiring anything "100 percent finished" before entry "becomes a
  huge step towards a sequential, stage-gate approach". So section 4's trigger fires both when an item the
  DoR let through stalls on something it should have caught and when an item it blocked turns out to have
  been ready enough. The second direction is this library's own contribution and is labelled as such in the
  bundle.
- **The citation hazard binds hardest here.** The contract names this family's hazard as "folklore
  presented as standard". The 2020 Scrum Guide never uses the phrase "Definition of Ready", and the Scaled
  Agile Framework's glossary has no entry for it. The bundle's admission rests on practitioner and pattern
  sources and must say so.
- **`pairs_with: []`.** The one pm-skills candidate, `iterate-refinement-notes`, never mentions a definition
  of ready.

## More Information

- Family contract: [`standing-standards`](../contracts/standing-standards.md), adopted by
  [ADR 0032](0032-adopt-standing-standards-family-contract.md).
- The classification precedent this follows: `definition-of-done`, `foundation`, in ADR 0032. The one it
  does not: [ADR 0053](0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md), `tool`.
- The spec: [`tier2-specs.md`](../tier2-specs.md).
