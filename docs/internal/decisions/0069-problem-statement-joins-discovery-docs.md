---
status: accepted
date: 2026-10-11
decision-makers: [jprisant]
consulted: [claude]
---

# `problem-statement` joins `discovery-docs` at `phase: define`, and the contract carries two phase values

## TL;DR

- **Decision.** `discovery-docs` admits a fourth member, **`problem-statement`**, at **`phase: define`**.
  The [contract](../contracts/discovery-docs.md) moves to `0.3.0` and carries a set of two phase values,
  `discover` and `define`. A member declares `define` when its whole document frames one problem and names
  no solution, option, project or investment. Every other member declares `discover`.
- **Why an amendment and not a new family.** The contract's cadence clause already fits a problem statement:
  "every member is written once for a decision, and is finished when that decision is made". Its membership
  clause admits it too. A new define-pinned contract would hold one member and repeat this contract's cadence
  clause nearly word for word.
- **Why build it at all, given the overlap with `business-case`.** `business-case`'s Problem and Opportunity
  section does part of the same job. The sources describe the problem statement in places where no business
  case follows: UX discovery, public-sector project planning and a product team's kickoff. The maintainer
  ruled on 2026-10-11 to build it.
- **Sizes: lean and full, by the maintainer's ruling.** The sweep recommended lean only, because every
  admitting source describes a short artefact. The maintainer ruled on 2026-10-11 for two sizes. What the
  full variant adds must be grounded in the build's own research, and anything it adds beyond that is
  labelled as this library's POSITION.
- **What this does not decide.** Whether `business-case` or `project-brief` should move to `define`. It
  decides nothing for `shape-up-pitch`, `lean-canvas` or `opportunity-solution-tree` either. None of the
  three is a Define candidate under
  [ADR 0068 (the define phase means problem framing)](0068-define-means-problem-framing.md).
- **Status:** accepted 2026-10-11. The maintainer chose this route on 2026-10-11, then directed that the
  spec and build merge on the agent's own judgment. That direction stands in for the read that
  [ADR 0063](0063-project-brief-reopens-discovery-docs.md) and
  [ADR 0066](0066-adopt-experimentation-docs-family-contract.md) each had. The agent checked the contract
  diff against ADR 0068 and against the draft amendment the maintainer had chosen, and found it states
  the decision as made. **Confirmed by the maintainer on 2026-10-12**, who reviewed the delegated acceptance
  and chose to keep it rather than reopen the record for a read.

## Context and Problem Statement

[ADR 0068](0068-define-means-problem-framing.md) reserves `define` for a document that frames a problem
before any solution is chosen. A Define admission sweep on 2026-10-11 tested four candidates against that
reading and against [ADR 0030](0030-templating-scope-markdown-documents.md)'s admission test. Two workflow
runs read 75 addresses. The main loop checked 311 returned quotations against raw page text, and 310 of them
passed.

**Only the problem statement cleared both tests.** Nielsen Norman Group (Maria Rosala, "Problem Statements in
UX Discovery") defines it as "A concise description of the problem that needs to be solved", requires its
background, the people affected and the impact, and sets the rule that it must "Not contain a solution".
Digital NSW tells teams to "Use the evidence you gather to document your clearly defined problem", and its
review checklist asks "Have we described a problem rather than a solution?". Each is a named source that
defines the artefact as written, which is all
[ADR 0048](0048-one-named-source-clears-the-admission-test.md) requires.

The other three failed the problem-framing test on their own sources' words. Basecamp's Shape Up chapter on
the pitch says "A problem without a solution is unshaped work". Ash Maurya, asked about the lean canvas's fill
order, answers "There is none", and its Solution block sits beside its Problem block from the first draft. No
named source publishes the opportunity solution tree as a written document.

So the question is where one problem-framing document lives. Every family contract pins its axis, and none
pins `define`. The 2026-10-10 session that recorded ADR 0068's decision noted that a Define bundle would need
a new contract pinned to `define`. That note assumed several Define candidates would need one home. The sweep
found one.

## Decision Drivers

- **Cadence decides the family, not the phase value.** `discovery-docs` section 1 closes: "This family is
  phase-bound by construction: every member is written once for a decision, and is finished when that
  decision is made." Digital NSW, Atlassian and Jeff Gothelf each describe a problem statement written once,
  at the start of an initiative. Nielsen Norman Group supports both readings: write it early, and return to
  it during discovery. No source read describes a standing document revised on a cadence.
- **The membership clause admits it without strain.** Section 1 admits a type that "exists to decide whether
  to build something, before anyone commits to building it." A problem statement settles which problem is
  worth pursuing, before any solution is named.
- **A contract written for one candidate is reverse-engineered from that candidate.** This library holds that
  this is the defect the contract-first rule exists to prevent. That sentence is a POSITION.
- **The duplication question has a precedent on both sides.** [ADR 0064](0064-deployment-plan-is-declined.md)
  and [ADR 0065](0065-steering-committee-pack-is-declined.md) declined two candidates that had cleared
  admission, because a shipped bundle already held their whole content. Here the overlap is one section of a
  larger document.

## Considered Options

1. **Amend `discovery-docs` to carry `discover` or `define`, and admit `problem-statement` at `define`.**
   Chosen by the maintainer on 2026-10-11.
2. **A new define-pinned contract, `problem-framing-docs`**, whose membership test is that the whole document
   frames one problem and names no solution, option, project or investment. Rejected: it would hold one member
   at adoption, its cadence clause would copy `discovery-docs`', and its membership test would need a
   whole-document test to exclude `business-case`, `project-brief` and the PRD, each of which frames a
   problem inside one section. It becomes the better route if a second problem-framing candidate clears
   admission and the maintainer wants Define bundles on a shelf of their own.
3. **Decline `problem-statement` on duplication**, in the ADR 0064 shape, and add one routing line to
   `business-case`'s guide for a reader who wants a standalone statement. Rejected on the maintainer's ruling.
   It remains defensible on the evidence, since `business-case`'s Problem and Opportunity section carries the
   same no-solution rule in its own WHAT and TRAP.

## Decision Outcome

**Chosen: option 1.** `problem-statement` joins `discovery-docs` as its fourth member, at `phase: define`.

### What the amendment costs, stated rather than smoothed over

1. **It breaks a precedent.** `discovery-docs` becomes the first `phase`-axis family to carry a set of
   values. Until now only `classification` families carried sets: `strategy-docs` and `standing-standards`.
   Check K already reads a list under either axis key (`axis_values` in `tools/check-bundles.py`), so the
   change is mechanical, and a fixture for a phase set is added to `tools/test-check-k.py`.
2. **It inverts the phase order inside the family.** ADR 0003 lists `define` after `discover`. A problem
   statement logically comes before a project brief and a business case, yet it carries the later phase value.
   Under ADR 0068's reading, a business case could itself be read as sitting at the close of Define. **This
   record does not move `business-case` or `project-brief`.** Moving them would reopen two built bundles, and
   it is a separate decision. The problem statement's companion says the order plainly.
3. **Check K cannot prove the right value.** It proves that a member declared a value from the set, never that
   the member declared the right one. That has been the limit on every set since
   [ADR 0023](0023-resolve-the-tier-1-family-taxonomy.md), and the assignment stays a review obligation
   against the contract's section 2.

### Consequences

- **The contract moves to `0.3.0`.** The header's Status line and Axis line, the Members line, a new
  section 1 bullet, the section 2 phase row, a new section 4 shared-scenario bullet, section 6's enforcement
  sentence and the change note all change in the same edit. The diff is in the PR that lands this record.
- **The section 2 rule is an OBLIGATION, the library's own, and needs no source.** `define` is reserved for a
  member whose whole document frames one problem and names no solution, option, project or investment.
- **Check K's `discovery-docs` entry gates `["discover", "define"]`**, and its comment no longer says the
  family is a single value by construction.
- **Section 1's successor obligation binds the new member.** Its companion must say which document takes over
  when the decision is made: `project-brief` when someone must authorise starting work, `business-case` when
  an investment must be justified, or a PRD when a team proceeds straight to specification.
- **The chronology obligation binds its example.** It must be dated before the documents it leads to and must
  not cite them as existing. [`tier2-specs.md`](../tier2-specs.md) fixes the example's date and the facts it
  may read.
- **No other built bundle changes family or phase.**

## More Information

- The phase decision this record applies: [ADR 0068](0068-define-means-problem-framing.md).
- The family contract: [`discovery-docs`](../contracts/discovery-docs.md), adopted by
  [ADR 0031](0031-adopt-discovery-docs-family-contract.md) and reopened by
  [ADR 0063](0063-project-brief-reopens-discovery-docs.md).
- The precedent for a set on an axis key: [ADR 0023](0023-resolve-the-tier-1-family-taxonomy.md) and
  `strategy-docs`.
- The spec and the admission evidence: [`tier2-specs.md`](../tier2-specs.md), the `discovery-docs` (fourth
  member, at `define`) section.
