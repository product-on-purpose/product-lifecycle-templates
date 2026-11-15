---
status: accepted
date: 2026-11-14
decision-makers: [jprisant]
consulted: [claude]
---

# `design-principles` joins `standing-standards` as a `foundation`, and the membership sentence widens to admit it

## TL;DR

- **Decision.** A `design-principles` bundle (issue #359, bundle: design-principles) declares
  **`family: standing-standards`** and **`classification: foundation`**. It becomes that family's ninth member, and the
  [contract](../contracts/standing-standards.md) moves to `0.8.0`, together with
  [ADR 0090 (product principles joins standing-standards)](0090-product-principles-joins-standing-standards-as-a-foundation.md).
- **What the type is.** It is a short list of value statements a team agrees once and then uses to frame and settle
  design decisions about its product's experience. It is not a style guide or a design system's component rules.
- **What changes in the contract.** Section 1's sentence "written when the team decides how it will work" gains a
  second case: "or what every decision about its product must honour". Without it, the family admits standards for
  how a team works and not standards its product decisions are judged against.
- **What settled classification:** the contract's cut, "a standard you judge against, or an instrument you
  execute". USWDS calls its principles an "evaluative lens for design and implementation decisions".
- **Status:** accepted 2026-11-14. The maintainer read sweep 8's batched decisions, including the widened sentence
  quoted verbatim, and answered "d3 a". The contract diff is read again in this PR before it merges.

## Context and Problem Statement

Backlog section 9.2 listed design principles as a type the 2026-10-20 Define re-score sent to a sweep outside
`define`, with no catalog row. Admission sweep 8 ran on 2026-11-14: two web readers, one internal reader across all
eleven family contracts, and two Sonnet critics. A second round read GitLab's Pajamas design system and handbook, the
NHS service manual and Monzo. The main loop re-checked every returned quotation against raw page text, and discarded
the six that failed; none was load-bearing. The working files are gitignored, at
`_local/research/2026-11-14_admission-sweep-8/`.

**All five admission checks pass or do not apply.**

1. **Written document** (ADR 0030 as read by ADR 0048). Nielsen Norman Group defines design principles as "value
   statements that frame design decisions" and gives a method for writing them. GOV.UK, USWDS, GitLab Pajamas, the
   NHS service manual, IBM and Microsoft publish maintained sets.
2. **Phase fit** (ADR 0077). Not applicable: the type takes a `classification`.
3. **Written form** (ADR 0078). It passes: a short prose list.
4. **Not duplicated.** It passes. No shipped bundle, section, alias or id holds design principles.
5. **Software audience** (ADR 0080). It passes: GitLab, IBM, Microsoft, USWDS and GOV.UK are software and digital
   service teams.

## Decision Drivers

- The family must follow what the document does: it is consulted at the moment a design decision is made.
- There is no design family to place it in. ADR 0030 says "design-docs is therefore never created" (line 84).
- A widening of a membership clause is a contract amendment, so the maintainer reads it before it merges.

## Considered Options

1. **`standing-standards`, `classification: foundation`, with section 1 widened.** Chosen.
2. **`standing-standards` without the widening.** Rejected: principles describe what the product's decisions must
   honour, not how the team works, so the unwidened sentence would admit the type only by a strained reading.
3. **`strategy-docs`.** Rejected: its question list is closed, design principles answer none of its questions, and
   admitting them would need an eighth question.
4. **Park.** Rejected on the evidence: seven named publishers clear admission.

## Decision Outcome

**Chosen: `standing-standards` with `classification: foundation`, and section 1 widened.**

### Why the family question tracks the falsifier

The falsifier reads: "if a candidate arrives that matches the cadence but is not consulted at the moment of action,
this family has been drawn around the axis rather than around a job". Design principles pass it. They are consulted
when a designer or a team chooses between two designs, and they exist for that moment: NN/g's phrase is "frame design
decisions". GitLab Pajamas calls its principles a "reusable standard for teams to measure their work".

### Why `foundation`

A design review, a disputed choice and a proposed pattern are each judged against the principles. Nobody executes
them under time pressure, so the `tool` marker fails. They are agreed by a team and changed deliberately and rarely,
which is the `foundation` description in section 2. The sweep's readers reported no revision interval from any
source, so the cadence tension ADR 0088 recorded has not arisen. The build's research should look for one, and this
record is where to reopen the classification if it finds a calendar.

### The widened sentence

Section 1 now reads: "written when the team decides how it will work, or what every decision about its product must
honour, and then consulted repeatedly without being rewritten." The cut at section 2 and the falsifier are unchanged.
The widening admits a standard a team's product decisions are judged against. It does not admit a document revised on
a cadence or one written for a single decision, which section 1 still routes elsewhere.

### The counter-arguments this record keeps

- **The widening could invite more.** A broad reading of "what every decision about its product must honour" could
  admit a brand guide or a content style guide. Each still needs its own admission sweep and its own record.
- **Two principles types sit side by side.** [ADR 0090](0090-product-principles-joins-standing-standards-as-a-foundation.md)
  admits product principles to the same family. The two bundles will have similar skeletons, so each guide must state
  the difference in decision domain: design principles frame experience decisions, product principles resolve
  product trade-offs.

### Consequences

- `standing-standards` grows from eight members to ten, with ADR 0090, and moves to `0.8.0`.
- The catalog row lands at the build, numbered after entry 212, as entries 209 to 212 did.
- Sizing evidence for the spec: published sets run from four to eleven principles, and principles.design says "The
  most effective examples use 3-5 principles." A single lean size is plausible. Section 4 requires a named owner and
  a condition-based review trigger in every variant.

## More Information

- Family contract: [`standing-standards`](../contracts/standing-standards.md), adopted by
  [ADR 0032](0032-adopt-standing-standards-family-contract.md).
- The previous member: [ADR 0088](0088-platform-device-support-matrix-joins-standing-standards-as-a-foundation.md).
- The admission standard: [ADR 0030](0030-templating-scope-markdown-documents.md),
  [ADR 0048](0048-one-named-source-clears-the-admission-test.md) and
  [ADR 0080](0080-admission-gains-a-software-audience-check.md).
- The plan that ran the sweep: [`section9-candidates-plan.md`](../section9-candidates-plan.md).
