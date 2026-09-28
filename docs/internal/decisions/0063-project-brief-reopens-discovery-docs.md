---
status: proposed
date: 2026-09-27
decision-makers: [jprisant]
consulted: [claude]
---

# `project-brief` joins `discovery-docs`, reopening a family ADR 0035 recorded as closed at two members

## TL;DR

- **Decision:** `discovery-docs` reopens to admit a third member, **`project-brief`** - `phase: discover`,
  built on the PRINCE2/UK BIS lightweight, pre-project sense of the name, with the NSW Health/Treasury Board
  of Canada heavyweight sense named and put out of scope. The [contract](../contracts/discovery-docs.md) moves
  to `0.2.0`.
- **Why this is a reopening, not a widening.** `discovery-docs`'s own membership test, "exists to decide
  whether to build something, before anyone commits to building it" (`discovery-docs.md:24-26`), already
  admits a project brief without argument. What stood in the way was the contract's closure statement, "the
  family is closed at two" (`discovery-docs.md:6`), which recorded [ADR 0035](0035-prototype-brief-fails-the-admission-test.md)'s
  **outcome** for a different candidate, `prototype-brief`, whose own admission test failed. This record
  changes no membership language; it retires a closure statement whose reason for existing (a different
  type's negative result) does not apply to this type.
- **What settled it.** At least four independently named bodies, including AXELOS itself, publish the type as
  a written document. The shipped `business-case` bundle already names PRINCE2's version of it as a
  neighbour (`business-case_guide.md:17`, and its companion's reference 32).
- **What this does NOT decide:** `project-charter` (catalog alias PID), which shares this type's catalog
  category and purpose and must pass ADR 0030's admission test on its own evidence, per the method
  [ADR 0049](0049-pi-release-retrospective-fails-the-admission-test.md) already established.
- **Status:** proposed 2026-09-27. **Held proposed until the maintainer reads the contract diff**, the way
  [ADR 0059](0059-announcement-internal-comms-joins-delivery-docs.md) and
  [ADR 0060](0060-change-request-joins-delivery-docs.md) were before their own acceptance.

## Context and Problem Statement

A research sweep on 2026-09-27 (admission sweep 3) tested five queued candidate types against ADR 0030's
admission test and, for each that cleared it, against every family contract's own membership language.
`project-brief` cleared the admission test on several independent named sources. The AXELOS
Limited *PRINCE2 Glossary of Terms English* (v.1.1, 2012, read via the Internet Archive because the live host
no longer serves the file) defines it in one paragraph as "Statement that describes the purpose, cost, time
and performance requirements, and constraints for a project," created "pre-project during the Starting up a
Project process" and "superseded by the Project Initiation Documentation and not maintained." The UK
Government's own *Guidelines for Managing Projects* (BIS, 2010, Crown copyright, Open Government Licence)
independently confirms the type and adds that "Approval of the Project Brief is the official start of the
project." NSW Health and the Treasury Board of Canada Secretariat both mandate a document under the same name,
in a heavier, gate-adjacent sense this record does not adopt.

Tested against every family contract's own membership language, with no family assumed, eight of nine exclude
the type as written, several by direct analogy to the already-shipped `business-case` bundle (`strategy-docs`
and `governance-docs` both name `business-case` as their own worked exclusion example). Only `discovery-docs`
admits it, and admits it on the contract's own words: "exists to decide whether to build something, before
anyone commits to building it" (`discovery-docs.md:24-26`) describes a project brief without needing to be
stretched.

**The obstacle is not the membership test. It is the contract's header, "the family is closed at two"
(`discovery-docs.md:6`), and the reopening question this record must answer honestly is whether that sentence
was ever a rule against a fourth candidate, or only a record of what happened to a third.**

### What ADR 0035 actually decided, and what it did not

[ADR 0035](0035-prototype-brief-fails-the-admission-test.md) applied ADR 0030's admission test to
`prototype-brief`, a **different candidate type**, and found no named source publishing it as a written
document: "every candidate examined turned out to be a neighbouring document type (a code-based prototyping
kit, a sprint-wide brief, a hypothesis card, or vendor blog content) presented under another name" (`0035:17-19`).
Its decision outcome states: "`prototype-brief` does not ship. It is not added to
the catalog. `discovery-docs` is complete at two members, `business-case` and `user-persona`" (`0035:123-124`).

[ADR 0031](0031-adopt-discovery-docs-family-contract.md), ratifying the contract in advance of that research,
had already named a negative result as an acceptable outcome of testing that specific candidate: "if no named
source is found, the type does not ship and this family has two members, which is a legitimate outcome and not
a failure of the contract" (`0031:53-54`). **That sentence is conditional on the research finding no named
source. It says nothing about a future candidate for which a named source is found.** ADR
0035 itself lists four conditions that would reopen its own finding (`0035:149-160`), and every one of them is
about `prototype-brief` specifically: a named source publishing a prototype-commissioning document, a
publisher converting a canvas into a document, a different type name for the same job passing its own
evidence, or a real team asking for one. None of the four contemplates a wholly different catalog candidate,
`project-brief`, whose own evidence was never examined in 2026-08-05 because it was never the type under test.

`process-docs.md:23-24` supplies the corroborating signal from a contract that was never in question: "A
candidate that looks forward belongs elsewhere: `discovery-docs` before a decision, `strategy-docs` for
direction, `delivery-docs` for the work itself." That sentence already assumes `discovery-docs` is where a
forward-looking, pre-commitment candidate belongs, independent of how many members it currently has.

## Decision Drivers

- **The admission evidence is unusually strong, not marginal.** Unlike `prototype-brief`'s single contested
  source, `project-brief` clears ADR 0048's one-source reading on at least four independently named bodies,
  one of them the standards body itself (AXELOS), and one of its citations already sits inside a shipped
  bundle's research trail (`business-case_companion.md:420`, reference 32).
- **A closed family is a recorded outcome, not a standing prohibition, unless the contract says otherwise.**
  Nothing in `discovery-docs.md` or ADR 0031 states that no further candidate may ever be tested; ADR 0035's
  own reopening conditions are scoped to the candidate it actually tested.
- **The smallest honest move is to reopen the existing family, not build a new one or force a fit elsewhere.**
  Eight of nine contracts exclude the type on their own membership language; only `discovery-docs`'s test
  admits it, and it admits it cleanly, not by strain on the membership sentence itself. The strain is
  elsewhere (below).
- **Every honest option must confront the one source that argues against reopening**, not route around it.

## Considered Options

1. **Reopen `discovery-docs` for `project-brief` by decision record.** Chosen.
2. **A new one-member family**, on the `communication-docs` precedent ADR 0060 considered and rejected for
   `change-request`. Rejected for the same reason that record gave: it draws a family boundary around a single
   document and invites the question that record had to answer about itself, when an existing contract's own
   membership test already admits the type without amendment.
3. **Do not build.** `discovery-docs` stays closed at two, and `project-brief` is declined the way
   `deployment-plan` ([ADR 0064](0064-deployment-plan-is-declined.md)) and the periodic steering pack
   ([ADR 0065](0065-steering-committee-pack-is-declined.md)) were declined in this same research run.
   Rejected on the maintainer's 2026-09-27 ruling, not on this record's own reasoning alone: this option
   remains legitimate on the evidence (ADR 0031 and ADR 0035 both frame a closed family as a valid outcome),
   and it would leave a type that clears admission on four named bodies stranded, with `business-case`
   already naming it as a neighbour it does not build.

## Decision Outcome

**Chosen: option 1.** `discovery-docs` reopens. Its Members line becomes `business-case`, `user-persona`,
`project-brief`, and its closure statement is replaced with a note that the family was closed at two from
2026-08-05 to 2026-09-27, closed on `prototype-brief`'s own negative result, and reopened on `project-brief`'s
own positive one. The membership clause in section 1 does not change; the type was always admitted by it.

### The strain this record must state in its own body, not smooth over

The UK BIS guide's own sentence, "Approval of the Project Brief is the official start of the project," reads
as the commitment trigger itself. `discovery-docs`'s membership clause is written the other way: a document
that exists "before anyone commits to building it." **This library's own POSITION, adopted here because the
sources do not settle it**: approval of a project brief commits to *initiating*, to spending organized effort
finding out whether and how to proceed, not to *building* the product itself. The document that commits to
building is a project charter, a PID, or, once the investment is approved, a PRD. This is the same
distinction PRINCE2's own comparison source draws against PMBOK's charter: "The main difference in purpose is
that the approved Project Brief gives the project manager the authority and resources to complete the work
necessary for the Initiation Stage" and "does not give authorization to complete the project activities"
(prince2.ca). The companion for the built bundle must carry this same POSITION, not report it as an external,
settled fact, because the sources genuinely split on it (Asana treats brief and charter as parallel-purpose
rather than sequenced; Smartsheet collapses them into one document at different weights; APM's own Body of
Knowledge lists "project brief" as one of three interchangeable common-usage names for an undifferentiated
project rationale, not a separately defined artefact).

### `project-charter` inherits nothing from this ruling

`project-charter` (catalog alias PID) sits in the same catalog category ("Planning / Roadmapping") and shares
this type's "decide/authorize before commitment" purpose. [ADR 0049](0049-pi-release-retrospective-fails-the-admission-test.md)
is the precedent for treating that proximity as no argument at all: it refused `pi-release-retrospective` on
its own evidence while its catalog sibling `project-milestone-retrospective` shipped, in the same catalog
category, on the strength of its own admission test rather than its neighbour's outcome. This record's
reopening of `discovery-docs` says nothing about whether `project-charter` clears ADR 0030's admission test,
whether it fits `discovery-docs`'s membership clause, or whether the family would need to reopen a second time
for it. That research has not been run.

### Consequences

- **The contract moves to `0.2.0`.** Its Members line gains `project-brief`; its closure statement becomes a
  dated history note rather than a present-tense claim; section 1's three-question membership list gains a
  fourth line for the new member (the `prototype-brief` line is kept, dated, as the record of a type that was
  tested and did not ship, not deleted, so the contract does not erase its own history).
- **Every place in the repository asserting the family is closed or complete at two carries a dated
  correction**, landed with this record: `docs/internal/buildout-specs.md`, `README.md` (the family heading and
  its narrative), `STATE.md`'s per-family list, and a pointer at the top of ADR 0035.
- **The chronology and no-grandfathering obligations bind the build exactly as they bound `business-case` and
  `user-persona`.** The new member's example must be dated before whatever it leads to, and it earns no
  exemption from `tools/check-example-independence.py`.
- **The catalog entry is corrected when the bundle lands**, per
  [procedure 1](../decision-procedures.md#1-a-catalog-call-loses-to-research): the methodology credit
  "PMBOK 7 (new)" is unsupported by the PMI Lexicon (versions 5.0 and 3.2, both raw-checked to lack the term),
  and PRINCE2 is the methodology this research actually confirmed.
- **`business-case`'s own boundary text needs no edit.** It already states the boundary the new member must
  agree with (`business-case_guide.md:17`, `business-case_companion.md:315-317`), and the new companion agrees
  with it rather than restating it differently.

## More Information

- Family contract: [`discovery-docs`](../contracts/discovery-docs.md), adopted by
  [ADR 0031](0031-adopt-discovery-docs-family-contract.md); the closure this record reopens is
  [ADR 0035](0035-prototype-brief-fails-the-admission-test.md).
- The precedent this record follows for stating a strain as a named POSITION rather than smoothing it over:
  [ADR 0060](0060-change-request-joins-delivery-docs.md)'s own treatment of the agile position and the DORA
  finding.
- The precedent this record does not repeat: [ADR 0060](0060-change-request-joins-delivery-docs.md) widened a
  membership test because no contract admitted the type as written. Here, one contract already did; this
  record removes an obstacle the membership test never raised.
- The spec and the admission evidence: [`tier2-specs.md`](../tier2-specs.md), the `discovery-docs` (reopened,
  third member) section.
