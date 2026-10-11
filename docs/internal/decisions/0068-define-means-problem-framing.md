---
status: accepted
date: 2026-10-11
decision-makers: [jprisant]
consulted: [claude]
---

# The `define` phase means problem framing

## TL;DR

- **Decision.** The `define` value of the phase vocabulary ([ADR 0003](0003-phase-vocabulary.md)) is
  reserved for a document that frames a problem before any solution is chosen. `prd`, `epic`,
  `user-stories` and `acceptance-criteria` stay on `phase: deliver`, where
  [ADR 0020 (adopt the delivery-docs family contract)](0020-adopt-delivery-docs-family-contract.md) put them.
- **What this records.** The maintainer made this call on 2026-10-10, and no file in the repository held it.
  This record is written so that a family contract can rest on it, as
  [decision procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world)
  requires.
- **The option not chosen.** The requirements reading, which would have moved the four delivery bundles
  above to `define` by letting `delivery-docs` carry a phase set. It was recommended at medium confidence
  and declined.
- **What this does not decide.** Which family carries a `define` bundle, and which bundles are built.
  [ADR 0069](0069-problem-statement-joins-discovery-docs.md) answers the first question for the one
  candidate that cleared admission.
- **Status:** accepted 2026-10-11. The maintainer confirmed that the draft in the 2026-10-11 Define
  admission sweep states the decision as it was made.

## Context and Problem Statement

ADR 0003 adopted six phase values, `discover`, `define`, `develop`, `deliver`, `measure` and `iterate`, to
match the `phase:` field that pm-skills uses. It fixed the six words, and it did not say what kind of
document belongs at each one. Every family contract then pinned its own axis value, and none pinned
`define`. Until 2026-10-11, no bundle in this library carried `phase: define`, and none could, because check K
gates each member to its family's declared value.

Two readings of `define` were available.

- **The requirements reading.** Define is where a team writes down what it will build. On this reading the
  PRD, the epic, the user stories and the acceptance criteria are Define documents. The catalog's free-text
  `stage: definition` on the PRD looks like support for this.
- **The problem-framing reading.** Define is where a team settles which problem it is solving, before any
  solution is chosen. On this reading the delivery bundles stay where ADR 0020 put them, and `define` waits
  for a document whose job is framing a problem.

The question this record answers is which reading the library uses, because the answer decides which
candidates a Define admission sweep should even look at.

## Decision Drivers

- **A phase value has to mean one thing.** A reader filtering bundles by phase, through `manifest.json` or
  the MCP server's `search_templates`, should get documents that share a job, not documents that share a word.
- **Moving four built bundles is expensive and changes what they claim.** The requirements reading would
  move `prd`, `epic`, `user-stories` and `acceptance-criteria` off `phase: deliver`, and it would make
  `delivery-docs` the first phase family to carry a set of values.
- **The catalog's `stage` field is not a phase.** It was called `lifecycle_phase` until 2026-07-17, when
  finding TX-2 renamed it to `stage` because its values, `definition` among them, were colliding with the
  six-value phase vocabulary ([`catalog.md`](../catalog.md), the note above the table). So
  `stage: definition` is weak evidence for either reading.

## Considered Options

1. **The problem-framing reading.** Chosen by the maintainer on 2026-10-10.
2. **The requirements reading.** Move the four delivery bundles to `define` and let `delivery-docs` carry a
   phase set. Recommended at medium confidence and declined.
3. **Leave `define` undefined.** Keep the value in the vocabulary with no stated meaning. Not recommended:
   a Define admission sweep cannot be scoped against a value that means nothing.

## Decision Outcome

**Chosen: option 1, the problem-framing reading.** `define` is reserved for a document that frames one
problem before any solution is chosen. The PRD and the rest of the `delivery-docs` chain stay on
`phase: deliver`.

**Why.** It is the maintainer's call. This library holds that the problem-framing reading matches the Double
Diamond's own use of the word, in which Define closes the problem space before Develop opens the solution
space. That sentence is the library's POSITION. The Define admission sweep of 2026-10-11 read the Design
Council's own Double Diamond pages and found no named written deliverable for the Define stage, so the
framework supports the position about the stage's purpose, not about any document.

### Consequences

- **The catalog's `stage: definition` is not evidence for `phase: define`.** It appears on `prd` and on the
  `shape-up-pitch` candidate, and neither is a problem-framing document. A future sweep must not admit a
  candidate to `define` on that field.
- **A Define candidate must frame a problem and name no solution.** The 2026-10-11 sweep tested four
  candidates on this reading. Only the problem statement passed. The Shape Up pitch carries a chosen
  solution, the lean canvas carries a Solution block beside its Problem block from the first draft, and the
  opportunity solution tree carries solutions and assumption tests, and has no source that publishes it as
  a written document.
- **No built bundle moves.** `prd`, `epic`, `user-stories` and `acceptance-criteria` keep `phase: deliver`,
  and `delivery-docs` keeps its single value.
- **Do not reopen the requirements reading without a new reason.** A reader who wants it back needs evidence
  this record did not weigh, not the catalog's `stage` field.

## More Information

- The phase vocabulary: [ADR 0003](0003-phase-vocabulary.md).
- The family that holds the delivery chain: [ADR 0020](0020-adopt-delivery-docs-family-contract.md).
- The family question this decision opened, answered for the one candidate that cleared admission:
  [ADR 0069](0069-problem-statement-joins-discovery-docs.md).
- The sweep's candidates and verdicts are summarised in the [`tier2-specs.md`](../tier2-specs.md) progress
  table, in the rows dated 2026-10-11.
