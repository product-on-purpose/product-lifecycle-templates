---
status: proposed
date: 2026-11-05
decision-makers: [jprisant]
consulted: [claude]
---

# `manager-user-guide` opens a one-member `personal-docs` family

## TL;DR

- **Decision.** The candidate `manager-user-guide` (issue #329, no catalog row yet) is admitted, scoped to a
  manager, and placed in a new family, [`personal-docs`](../contracts/personal-docs.md), at
  **`classification: utility`**. That family has this one member and says so.
- **The scope question comes first.** This would be the first bundle about one person rather than about a
  product or its delivery. What the library will template stops for the maintainer, and declining is the
  realistic alternative.
- **Why no existing family.** `communication-docs` excludes it on two defining clauses. `standing-standards` fits
  on cadence, but its classification cut, which its adopting record calls "the substance", has no place for a
  disclosure of working style. Calling the guide a standard would tell readers that reports are judged against it.
- **Admission now rests on one readable source.** The issue names First Round Review. firstround.com's terms bar
  crawling, and this library reads them as covering The Review. GitLab's handbook carries admission on its own.
- **Status:** proposed 2026-11-05. A new family contract is "adopted only after a maintainer read"
  ([decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer)). Check K registers
  the family only on acceptance.

## Context and Problem Statement

The maintainer queued the type for an admission sweep on 2026-10-25. Admission sweep 7 recommended admitting it on
2026-10-29 and found that no family fits without a contract change. It listed four options: amend
`standing-standards`, amend `communication-docs`, open a new family, or decline.

A read on 2026-11-05 tested those options and found two problems with the sweep's account. First, firstround.com's
terms say: "You may not “crawl,” “scrape,” or “spider” any portion of the Site (through use of manual or automated
means)." They define the Site as that domain and "its associated services", and its navigation lists The Review. This
library reads the clause as covering `review.firstround.com`, so that page cannot carry admission under the terms rule.
The maintainer may rule otherwise. Second, the sweep's ranking of `standing-standards` as the smaller strain tested
authorship and left the classification cut untested.

## Decision Drivers

- **The operative sentence governs.** [ADR 0050 (qa-docs admits a fourth member)](0050-qa-docs-admits-a-fourth-member.md)
  set that reading method for a family's membership text.
- **A widening must be the smallest honest one.** ADR 0060, ADR 0067 and ADR 0073 each rejected a new family as extra
  machinery when an existing contract fails on one phrase. The test is therefore how much of a contract fails.
- **Admission and the build decision are separate.**
  [ADR 0064 (deployment plan declined)](0064-deployment-plan-is-declined.md) established this, and it applies in both
  directions.
- **Build order is the maintainer's preference**
  ([ADR 0041](0041-maintainer-preference-sets-the-build-order.md)).

## Considered Options

1. **A new one-member family, `personal-docs`, at `classification: utility`.** Chosen.
2. **Amend `standing-standards`, at `foundation`.** Rejected, below.
3. **Amend `communication-docs`.** Rejected: the guide's audience is inside the team, and it originates every fact it
   states. Those are the family's two defining clauses.
4. **Decline, because a document about one person is outside this library's scope, or because no family fits.** This
   is the realistic alternative, and the maintainer's scope ruling decides it. ADR 0064's first ground is not available,
   since no shipped bundle holds this content.
5. **Defer until a team charter and a working agreement are built.** Rejected. Neither is scheduled, and each would
   state its boundary against this one just as well.

## Decision Outcome

**Chosen: option 1, subject to the maintainer's scope ruling.**

### Admission clears, on one readable source

- **Check 1, the written form.** Amy Shiel's README in the GitLab handbook is a sectioned page, described as "Personal
  readme page for Amy Shiel, Engineering Manager, GitLab". It states its purpose: "This page is intended to help others
  understand what it might be like to work with me, especially people who haven't worked with me before."
  [ADR 0048 (one named source clears admission)](0048-one-named-source-clears-the-admission-test.md) makes one sufficient.
- **Check 2, phase fit.** Not applicable: the type takes a `classification`.
- **Check 3, written-form scope.** The page is ordinary prose.
- **Check 4, no built bundle does its job.** No shipped bundle is written by one person about themselves. An alias scan
  in sweep 7 found no collision.
- **Check 5, a software audience.** The author is an engineering manager at a software company, writing for the people on that manager's team.

**First Round Review stays citable through a hand read.** Its reproduction of Jay Desai's guide would add a second source
and a fuller structure. The maintainer may read it by hand, under the terms rule's procedure. No agent reads it again.

### Why not `standing-standards`

**Authorship is the weaker ground, and this record does not rest on it.** The sweep's objection was that one person
writes the guide. But [ADR 0032 (adopt standing-standards)](0032-adopt-standing-standards-family-contract.md) says
"Agreed once, applied every time" is "closer to a cadence than to a job", and a runbook's authority "comes from being
correct right now", not from agreement. On cadence alone, the guide fits, and the family's staleness obligation suits it.
The contract's lines "written when the team decides how it will work" and "written by a team for its own future self"
would still need editing, but those edits are small.

**The classification cut is the deciding ground.** ADR 0032 says "The axis question is the substance", and its test is
whether a document is "a standard you judge against, or an instrument you execute". A disclosure of working style is
not an instrument anyone executes. Filing it as `foundation` means calling it a standard that its readers are judged
against. The contract also sends a document "valuable only while current" to a `utility` family, and it does not allow
`utility` itself. So this option means either the `foundation` reading or a third value on the axis.

**The placement would also teach the wrong thing (POSITION).** `foundation` would tell readers that reports are judged
against their manager's stated preferences. Ed Batista writes: "Expecting employees to conform to your preferences
without making an effort to understand and adapt to theirs isn't management, it's coercion."

**The family's falsifier is not the deciding ground.** The sweep said a guide read once at onboarding is not "consulted at
the moment of action". That claim was its critic's inference, and no readable source tests it. This record does not rest
on it. If the maintainer's hand read shows later use, and the maintainer accepts the `foundation` reading, this option
becomes the smaller change. **That is why the placement sits at medium-low confidence.**

### Why `utility`

**`utility` describes a standing document that is valuable only while current.** The guide has no lifecycle phase, and
Camille Fournier's central objection is about currency: "your documentation is out of date the minute you write it down".
**`foundation`** implies an argued, agreed basis that other work is measured against, and **`tool`** implies an instrument
someone executes. Confidence: medium. No readable source states how often a guide is revised.

### Scope: a manager (POSITION)

Diwaker Gupta argues "There's nothing "manager"-specific about them", and this record does not dispute the form. But
Shiel writes partly "to reduce the anxiety of people who might be on my team", and Fournier's hazard is authority: "you
have a huge power differential to the person who reports to you". A generic template would lose the prompts that deal
with that. A person who is not a manager can use a manager's template by marking one section not applicable. So the bundle
is scoped to a manager, and the aliases and the guide name the wider use.

### The family's shape, stated so it can be judged

A one-member family is legal: `communication-docs` is one, and ADR 0064's objection was to a family around content that
already shipped. **The forecast is weak, and the contract says so.** A team charter and a working agreement are agreed by a
team, so they fit `standing-standards` as written, and no other catalog row is written by one person about themselves. This
family may stay at one member permanently.

### Consequences

**Good.**

- A document with a real audience in software practice gets a home that does not bend a contract's definition.
- Two standing warnings become obligations: the contract requires a staleness trigger and a two-way feedback channel.

**Bad, and stated plainly.**

- **The library's scope widens.** Every other bundle concerns a product or its delivery.
- **A twelfth family costs real maintenance.** It adds a contract, a check K entry and a test fixture, and the "eleven
  families" prose moves at adoption.
- **All three critics question the genre.** The sweep's "high" was about admission and not about whether to build. Fournier
  writes "there is no way to write these and not be self-serving", and the guide must state this.
- **The boundaries are stated against unbuilt neighbours.** The team charter (entry 80), the working agreement (entry 100)
  and the onboarding guide (entry 195) do not exist yet. The claim that a charter is collectively written rests on catalog
  prose.
- **Admission is thinner than the sweep reported**, with one readable source.

### What would change this

1. **The maintainer rules that a document about one person is out of scope.** The candidate is then declined, and this record
   is rewritten as that decline.
2. **A hand read of First Round Review shows a different shape or cadence.** Sections and `utility` would be revisited,
   and the `standing-standards` option would strengthen if the guide is shown in use at the moment of action.
   **The maintainer may also rule that the terms do not cover The Review.** The page then returns as a second admitting
   source that agents may read.
3. **A hand read of Atlassian's Working Agreements play contradicts the boundary with a working agreement.**

### Confirmation

The maintainer reads the contract and this record. On acceptance, `tools/check-bundles.py` registers the family at
`classification: utility`, `tools/test-check-k.py` gains a fixture if the family's shape needs one, and the family counts
move.

## More Information

- The spec: [`tier2-specs.md`](../tier2-specs.md), section "personal-docs (founding member): the manager user guide".
- The nearest one-member precedent: [ADR 0034 (adopt communication-docs)](0034-adopt-communication-docs-family-contract.md).
  The latest new-family precedent: [ADR 0081 (adopt research-docs)](0081-adopt-research-docs-family-contract.md).
- The read and the sweep are held locally, at `_local/research/2026-11-05_manager-guide-read/read.md` and
  `_local/research/2026-10-29_admission-sweep-7/digest.md`.
