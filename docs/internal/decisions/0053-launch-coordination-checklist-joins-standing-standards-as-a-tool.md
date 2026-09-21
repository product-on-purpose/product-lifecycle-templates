---
status: accepted
date: 2026-09-20
decision-makers: [jprisant]
consulted: [claude]
---

# `launch-coordination-checklist` joins `standing-standards` as a `tool`, not `delivery-docs`

## TL;DR

- **Decision.** The `launch-coordination-checklist` bundle declares
  **`family: standing-standards`** and **`classification: tool`**. It becomes that family's third member,
  alongside `definition-of-done` (`foundation`) and `runbook` (`tool`).
- **Why it was blocked:** a family is a contract, not a folder, so the family assignment decides which
  structural and review obligations the bundle must satisfy. A spec cannot be written before it is known.
  Blocked since 2026-09-11.
- **What settled it:** not the contract on its own, which is genuinely ambiguous here, but
  [ADR 0032 (adopt the standing-standards family contract)](0032-adopt-standing-standards-family-contract.md)'s
  **self-supplied falsifier**: a candidate that matches the cadence but is **not consulted at the moment
  of action** means the family was drawn around an axis rather than a job. A launch coordination
  checklist is consulted at the moment of action. It passes the falsifier rather than tripping it.
- **A second-order find, and the more urgent one.** The promise tag is `future:launch-checklist` while the
  catalog id is `launch-coordination-checklist`. `tools/check-bundles.py` resolves `future:` targets **by
  bundle id**, so building the bundle under the catalog id would leave the tag promising an id that never
  arrives, **with the gate still green**. The tag is corrected in this change.
- **Status:** accepted 2026-09-20. The maintainer directed that the decision be taken and recorded; the
  agent determined the mechanics against the contracts and the gate source.

## Context and Problem Statement

[`tier2-specs.md`](../tier2-specs.md) records `launch-coordination-checklist` as **not specced,
deliberately**:

> its catalog category straddles two families (`release-notes` is `delivery-docs`, `runbook` is
> `standing-standards`) and **a family assignment is not a spec-writer's call**.

The straddle is real. `atlas/catalog-data.json` gives the type `category: "Release / Deployment /
Runbooks"`, which names both families' territory in one string. It is also `stage: release`,
`methodology: SRE`, `owner: "Launch Coordinator / SRE"`, `tier: 2`, `state: candidate`, and it
relates to `PRR` (Production Readiness Review).

It is promised to readers today. `templates/release-notes/release-notes_meta.yaml` line 17 carries
`related_templates: [prd, user-stories, acceptance-criteria, future:launch-checklist]`.

## Decision Drivers

- A family assignment fixes the bundle's structural obligations, so it gates the spec and therefore the
  build. This is the next Tier-2 bundle candidate on evidence.
- Family membership should track **what kind of document this is**, because that is what the contracts
  gate. It should not track workflow position, which is a different axis.
- [ADR 0021 (complete the Tier-1 floor)](0021-complete-the-tier-1-floor.md) leaves Tier 2 strictly
  grow-by-pull, so admitting a member must be argued, never assumed.
- A promise made to readers by a `future:` tag must be **resolvable**, or the gate that exists to keep
  promises honest is decorative.

## Considered Options

1. **`standing-standards`, `classification: tool`.** Chosen.
2. **`delivery-docs`.** The `future:` tag lives in a `delivery-docs` member's metadata, and the catalog
   `stage` is `release`.
3. **Defer again** until the bundle is researched. Rejected: the research cannot start without the
   contract, so deferring is circular.

## Decision Outcome

**Chosen: `standing-standards` with `classification: tool`.**

### Why not `delivery-docs`

That contract's section 1 admits a bundle when its type is **a delivery-chain artifact**: it "defines,
decomposes, verifies, or announces a unit of product work", and members form "a traceable chain that
carries one unit of product work from definition to delivery". The contract then obliges every member to
**state its position in that chain** in its companion's Relationships section.

A launch coordination checklist carries no unit of product work. It coordinates cross-team readiness for
an event. It has no position in the PRD to stories to acceptance-criteria to release-note chain, so it
cannot satisfy an obligation that family places on every member.

The `future:` tag's location is weak evidence here. `related_templates` asserts that two types are
**related**, not that they share a family.

### Why `standing-standards`, positively

1. **The contract already names this type.** Section 1's "likely future members, if pulled" list reads
   "`definition-of-ready`, a coding-standards or engineering-handbook document, **a release checklist**."
   Written before any member was built.
2. **It satisfies the membership test.** "Agreed once and applied every time. Not written per increment
   ... written when the team decides how it will work, and then consulted repeatedly without being
   rewritten." A launch checklist written for one launch is a launch plan, which is the same move the
   contract makes with "a runbook written for one incident is an incident report."
3. **It passes the family's own falsifier, which is the decisive point.** ADR 0032 concedes this family's
   coherence is thinner than its siblings': "agreed once, applied every time" is closer to a cadence than
   to a job, and grouping by rhythm is weaker than grouping by function. It therefore supplies a test:

   > if a candidate arrives that matches the cadence but is **not consulted at the moment of action**,
   > this family was drawn around the axis rather than around a job, and it should split rather than
   > absorb.

   Being consulted at the moment of action is a launch coordination checklist's entire function. The
   candidate that would have forced the family to split is the opposite of this one.
4. **`tool`, not `foundation`, on the contract's own cut.** `foundation` is "a standard you are judged
   against"; `tool` is "an instrument you execute, usually under time pressure and often by someone who
   did not write it." The second describes a launch checklist exactly, and it makes the type a sibling of
   `runbook`, with which it already shares SRE lineage, an SRE owner, and a PRR relationship.

### The counter-argument, recorded rather than omitted

**pm-skills classifies its paired `launch-checklist` skill under the `deliver` phase**, visible in that
repository's own phase flow (`/acceptance-criteria` to `/launch-checklist` to `/release-notes`). A reader
who expects family assignment to track the pm-skills pairing would expect `delivery-docs`.

It does not change the outcome, because this library's families classify **document type** while
pm-skills phases classify **workflow position**. The same artifact can be executed during the deliver
phase and still be a standing instrument rather than a delivery-chain link. But the tension is real and
is recorded so a future reader sees it was weighed rather than missed.

### Consequences

- `standing-standards` grows from two members to three. Its contract's Members line and its "likely
  future members" list are updated in this change, as that contract requires a decision record for
  changes to itself.
- Check K gates `classification` membership of the set `{foundation, tool}`. Per ADR 0032 it **cannot**
  verify that a member picked the *right* value; that stays a review obligation, and the argued split
  above is the standard this member is reviewed against.
- `tier2-specs.md` stops recording this type as un-speccable. The spec is now unblocked.
- **The `future:` tag is corrected from `future:launch-checklist` to
  `future:launch-coordination-checklist`,** so the bundle id and the promise agree.

  This matters more than it looks. `tools/check-bundles.py` (lines 805 to 811) resolves a `future:`
  target by **bundle id** against the directories on disk, and raises a *stale* failure only when that
  exact id appears. Building the bundle as `launch-coordination-checklist` while the tag said
  `launch-checklist` would have left a promise pointing at an id that never arrives, and **the gate would
  have stayed green**, because an unresolvable `future:` target is indistinguishable from a
  not-yet-built one. The bundle id is set to the catalog id rather than the tag's short form, because the
  catalog id is the more precise name and avoids colliding with the pm-skills skill name.
- The bundle stays unbuilt. This decision unblocks the spec, not the build, and Tier 2 remains
  grow-by-pull.

## More Information

- Family contract: [`standing-standards`](../contracts/standing-standards.md), adopted by
  [ADR 0032](0032-adopt-standing-standards-family-contract.md).
- The family it does not join: [`delivery-docs`](../contracts/delivery-docs.md), adopted by
  [ADR 0020](0020-adopt-delivery-docs-family-contract.md).
- Where the spec will go: [`tier2-specs.md`](../tier2-specs.md).
- The admission standard for new types:
  [ADR 0030 (templating scope: markdown documents)](0030-templating-scope-markdown-documents.md), and
  [ADR 0048 (one named source clears the admission test)](0048-one-named-source-clears-the-admission-test.md).
