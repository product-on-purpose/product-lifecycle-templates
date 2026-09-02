---
status: accepted
date: 2026-09-01
decision-makers: [jprisant]
consulted: [claude]
---

# `epic` joins delivery-docs, and the first Tier-2 build finds the gate that two records did not remove

## TL;DR

- **Decision:** `epic` is admitted to the **delivery-docs** family; the contract's membership chain sentence is amended to place it between the opening artifact and the stories that decompose it; and the build is recorded as `queued` in [`atlas/state-overrides.json`](../../../atlas/state-overrides.json), which is where a Tier-2 build backlog lives.
- **Why:** [ADR 0039](0039-maintainer-discretion-replaces-the-pull-gate.md) removed the gate on *whether* a Tier-2 type may be built. [ADR 0041](0041-maintainer-preference-sets-the-build-order.md) removed the rule that ordered it. **Neither touched family membership, which is enumerated and which the contract says may only change by decision record.** The first attempt to actually start a Tier-2 build stopped on that, and it will stop every future one until each receiving family has admitted its first new member.
- **Status:** drafted 2026-09-01, **accepted 2026-09-02** after the maintainer read. It was held rather than landed for a day because the choice it presented was real: the section 1 chain sentence can be read as enumerating membership (which makes this record necessary) or as describing current members (which would not), and reading it either way is a maintainer call rather than an agent's. **Amends [`contracts/delivery-docs.md`](../contracts/delivery-docs.md) to 0.1.3.** Changes nothing about the standard a bundle is built to, nothing about the gate, and nothing about the eight-file obligation. Adds no new rule; it applies an existing membership test to one type and records the result.

## Context and Problem Statement

The build order is now the maintainer's to set. On 2026-09-01 the maintainer set it: build `epic`, on the stated rationale that it closes the requirements spine between `product-roadmap` and `user-stories`, and that it is the type most likely to arrive in WP-33 wedge outreach.

**The build stopped before phase 0.** The `build-bundle` command lists three preconditions, and two of the three exposed something:

| Precondition | Result |
|---|---|
| The catalog entry exists (ADR 0030's admission test) | **Passes.** `epic` is catalogued: Tier 2, `rarity: common`, stage `requirements`, owner Product Owner / PM |
| The family contract exists | **Passes.** `delivery-docs` is adopted, at 0.1.2 |
| **The type is on the build backlog** | **Fails, and there was no backlog it could be on** |

The only build-backlog document is [`buildout-specs.md`](../buildout-specs.md), whose title is *"Tier-1 floor build-out: per-type specs and progress"*. That floor is complete. **No Tier-2 backlog was ever created**, because until 2026-08-14 Tier 2 was demand-gated and there was nothing to put in one.

Underneath that sat the harder problem. The delivery-docs contract's section 1 does not merely define a membership test; it **enumerates a chain and requires each member to state its position in it**. The 0.1.2 change note is explicit that a member left out of that sentence is a defect worth correcting: it rewrote the sentence precisely because it *"omitted product-backlog and sprint-backlog, two of the family's six declared members, leaving them outside the sentence that justifies membership."*

So admitting `epic` is a contract change, and the contract header states that **changes to it require a decision record**. The `build-bundle` command says the same thing from the other side: family contracts are *"drafted then read by the maintainer, never self-approved."*

**This is the third time in three weeks that a blocker attributed to one thing has been sitting somewhere else.** The eval harness was recorded as awaiting a spend decision and was actually a CRLF checkout. The build order was recorded as demand-driven and was actually ranking on an always-zero input. Here, "Tier 2 is unblocked" was recorded as true after two records removed two gates, and a third gate neither of them named stopped the first build attempt.

## Decision Drivers

* **The membership test already admits `epic`, so this record applies a rule rather than making one.** Section 1 admits a type that *"defines, decomposes, verifies, or announces a unit of product work."* An epic groups a body of work large enough to need decomposing. Nothing here widens the family's definition.
* **Procedure 11 requires the chain claim to be tested against research, not asserted.** It is tested below, and the sources are already in this repository, fetched and verified.
* **The one-time cost should be paid once per family, not once per type.** Recording this as a general finding, rather than a special case for `epic`, is what makes the next delivery-docs admission cheap.
* **A backlog mechanism should not be invented when one already exists.** [PR 115](https://github.com/product-on-purpose/product-lifecycle-templates/pull/115) shipped `state-overrides.json` with a `queued` block defined as *"a build the maintainer intends"*. It has been empty since it shipped. Writing a second backlog document would be the drift this repository keeps closing.

## Considered Options

1. **Admit `epic` by amending the chain sentence, and use `queued` as the backlog.** Chosen.
2. **Create a Tier-2 equivalent of `buildout-specs.md`.** Rejected. It duplicates `queued`, and a hand-maintained progress table is the exact artifact `STATE.md` exists to replace after audit finding G-01.
3. **Treat the chain sentence as illustrative and build `epic` without amending it.** Rejected. The 0.1.2 change note establishes that an unlisted member is a defect, and this repository corrected that defect once already rather than reading the sentence loosely.
4. **Put `epic` in a new family.** Rejected. Its phase is `deliver` and its neighbours are all delivery-docs; a family of one built to avoid an amendment is worse than the amendment.

## Decision Outcome

`epic` is admitted to delivery-docs. The chain sentence in section 1 gains one clause placing it between the opening artifact and the stories, and the contract goes to **0.1.3** with a change note. `epic` is written into `state-overrides.json` under `queued` with a reason naming ADR 0041.

### The chain claim, tested against research already in this repository

Procedure 11 asks what supports the assertion. Four sources, all already `fetched-and-verified` in existing members' research logs, none newly claimed:

| Source | Log entry | What it supports |
|---|---|---|
| Pichler, *The Product Owner's Guide to Effective Sprint Goals* | `sprint-backlog_research-log.md` entry 10 | Epics sit between the goal and the stories: *"I first select the goal. Then I explore which epics have to contribute to it, and I break out small detailed stories from the epics."* |
| Atlassian, *Enable the backlog (Jira Software Cloud)* | `product-backlog_research-log.md` entry 31 | *"Epics represent a group of smaller, related tasks, bugs and user stories."* |
| Microsoft, *Use backlogs to manage projects (Azure Boards)* | `product-backlog_research-log.md` entry 32 | The `Epic > Feature > Product Backlog Item` hierarchy; *"Epic: A long-running initiative that spans multiple features."* |
| Wikipedia, *User story* | `user-stories_research-log.md` entry 7 | The epic / theme / initiative hierarchy, matching the catalog entry's own `relationships: [Stories, Initiative, Theme]` |

The Pichler quotation is the one that fixes the position rather than merely the existence: stories are broken out **of** epics, so the epic precedes decomposition and follows the goal. That is where the amended sentence places it.

**These sources are cited here as evidence for a membership claim. They are not a research pass for the bundle**, which still owes its own log under the six-phase runbook.

### Consequences

* **Good:** the first Tier-2 build can start, and the next delivery-docs admission needs no record at all, because this one establishes that the chain sentence is amendable by ordinary contract revision.
* **Good:** the `queued` block gets its first entry, so a mechanism shipped two weeks ago stops being untested.
* **Bad, and named rather than argued away:** eight other families have contracts, and **each will hit this same gate on its first Tier-2 admission**. This record makes that cost visible but does not remove it. A future record could generalise the membership test so that admission stops needing a decision per family; that is deliberately not attempted here, because generalising a rule on one instance is how the demand rule got written.
* **Bad:** `epic` will be the seventh member of a family whose examples must chain on a common scenario (section 4). Admitting it obliges the bundle's example to join that chain, which is real work the build must not skip.
* **Neutral:** no gate changes. Check K validates `epic` against the same section 2 values as every other member once its meta exists.

### Falsifier

If two further families are admitted through this path and neither amendment surfaces a real question about membership, then the per-family decision record is ceremony rather than a check, and the rule should be generalised. **Re-open at the third family admission.**
