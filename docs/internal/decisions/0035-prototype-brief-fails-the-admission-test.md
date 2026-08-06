---
status: accepted
date: 2026-08-05
decision-makers: [jprisant]
consulted: [claude]
---

# `prototype-brief` fails ADR 0030's admission test and does not ship, closing `discovery-docs` at two members

## Context and Problem Statement

[ADR 0030 (templating scope)](0030-templating-scope-markdown-documents.md) admits a candidate type when
**a named source publishes it as a written document**. That test was applied to reject two catalog entries:
`wireframe`, because designers annotate inside the design tool and no named source publishes a written
wireframe specification, and `interactive-prototype`, because its artifact is executable. The same record
then added `prototype-brief` as a **new type**, on the reasoning that the artifact is out of scope but *the
brief that commissions it* is a document.

**That addition was made without applying the test to it.** ADR 0030 says so in its own text, and set the
order of work explicitly: build the bundle, run its research pass against the admission test, and add the
catalog entry only then. [ADR 0031 (the discovery-docs contract)](0031-adopt-discovery-docs-family-contract.md)
ratified the family with `prototype-brief` as a **provisional member** and pre-committed to the outcome:

> If the research finds no named source, the type does not ship and this family has two members, which is a
> legitimate outcome and not a failure of the contract.

This record applies the test and reports the result.

## Decision Drivers

* **The test must bite symmetrically.** A rule that rejects `wireframe` and admits `prototype-brief` without
  the same scrutiny is not a rule, it is a preference with a citation attached.
* **The V2MOM precedent.** This library has already rejected presenting one artifact under another type's
  name. Relabelling an adjacent document to fill an empty slot is the specific defect that rejection named.
* **The catalog is a claim about the world.** Adding an entry for a document type nobody publishes would
  make the library assert something false in machine-readable form.
* **A two-member family was pre-authorised**, so nothing downstream is blocked by a negative answer.

## The research pass

Six parallel dimensions, **29 unique sources of which 23 were fetched and verified** and 6 were
URL-confirmed but not read, plus 20 further sources referenced without being read. The first dimension was
written to be falsifiable, stating that a negative answer was a legitimate and expected outcome, so that it
was not a search for confirmation.

**Searched:** "prototype brief" template, prototype specification document, design sprint brief, experiment
brief, assumption test card, prototype plan. **Publishers checked directly:** GOV.UK Service Manual and
Design System, Digital Scotland Service Manual, Google Ventures and Jake Knapp's Design Sprint canon
(`gv.com/sprint` and its current `character.vc/sprint` host), AJ&Smart / Workshopper, IDEO and IDEO.org
Design Kit, Stanford d.school, Nielsen Norman Group, Interaction Design Foundation, Strategyzer, and Maze.

**All six dimensions converged independently on the same answer**, which is the strongest form the evidence
could have taken, because only the first was asked the admission question directly:

| Dimension | What it reported |
|---|---|
| Admission test | **FAILS.** No named source publishes a prototype brief as a written document |
| Structure in practice | "No named source found in this search publishes a document called a 'prototype brief' with a concrete, ordered section list. That is the headline finding" |
| Purpose and fidelity | "No source gathered here names a 'prototype brief' as a named artifact in its own right" |
| Assumption-test lineage | "none of them publish a written brief with a defined document structure ... every one of those ancestors stops short of the 'written brief' form" |
| Boundaries | Every **neighbour** has a named source defining it. The prototype brief itself has none |
| Failure modes | Strong controlled evidence exists about the **prototype artifact**, none about a document commissioning it |

### The four candidates, and why each fails

1. **GOV.UK prototyping guidance is a code toolkit.** It is built around the GOV.UK Prototype Kit, which
   produces an interactive prototype in code. There is no written commissioning document beside it. This is
   the exact structural analogue of the `wireframe` rejection: **the artifact lives in the tool, not on
   paper.**

2. **Google Ventures' Sprint Brief is real, named, and scoped to the wrong thing.** It orients a team for
   the entire five-day sprint: problem framing, sketching, deciding, prototyping and customer testing. The
   document that plans the prototype specifically is the **storyboard**, and the canonical page places it
   mid-sprint on day three, described as "a step-by-step plan for your prototype". A storyboard produced on
   Wednesday is an output of the sprint, not a brief that commissions it. Calling the Sprint Brief a
   prototype brief would be the V2MOM defect precisely.

3. **Strategyzer's Test Card is a card, not a brief.** It is named and structured, asking "What needs to be
   true for your idea(s) to work", but it is a compact hypothesis-test format for business-model assumptions
   generally, in which a prototype is only one possible test vehicle.

4. **"Experiment brief" is vendor content.** What exists (Amplitude, Houseware, Miroverse, ClickUp) is blog
   posts and template-marketplace listings describing informal internal practice, with no named
   methodological authority behind a defined structure, and it targets growth experiments rather than
   prototype commissioning.

**And the ancestry stops one step short, consistently.** Lean UX publishes a one-sentence hypothesis formula
and an eight-box **canvas** worked through collaboratively, which Gothelf's own how-to contrasts with
producing "a formal written brief". Teresa Torres publishes the opportunity solution tree, "a simple way of
visually representing the paths you might take". The riskiest assumption test is a practice. Stanford
d.school publishes a worksheet. **Every ancestor produces a canvas, a card, a worksheet or a diagram.** None
produces the document a template bundle would inherit.

## Considered Options

* **Ship it, synthesised from the adjacent artifacts.** Rejected. It would require inventing a section
  design no publisher uses and borrowing authority from documents that answer different questions. The
  bundle's own companion would have to say that no source publishes this document, which is an argument
  against shipping it, not a caveat to ship it with.
* **Re-scope the type under a different name** (`experiment-brief`, `assumption-test`). Rejected **for now**
  rather than on principle: the research already looked there, and found canvases, cards and vendor blog
  posts. Reopening is defined below.
* **Defer the decision.** Rejected. Deferring leaves a false claim standing in the catalog and holds the
  family open indefinitely, and the evidence is not going to improve by waiting.
* **Accept the negative result.** Chosen.

## Decision Outcome

**`prototype-brief` does not ship. It is not added to the catalog. `discovery-docs` is complete at two
members, `business-case` and `user-persona`.**

The provisional membership ADR 0031 created is resolved as *not admitted*, which that record named in
advance as a legitimate outcome. **This is the second time the admission test has changed an outcome rather
than ratified one**, after `wireframe`, and the first time it has removed a type the library had already
written into a family contract and a build backlog.

### Consequences

* The build backlog drops from 6 bundles to **5**, all of them original Tier-1 types. The Tier-1 floor
  figure is unchanged at 20 of 25, because `prototype-brief` was never one of the 27.
* **Catalog entry 54 is corrected.** Its note asserted that the commissioning brief "ships instead, as
  `prototype-brief` in `discovery-docs`". That was true as an intention and is now false as a fact. Both
  `catalog.md` and `atlas/catalog-data.json` are corrected with a dated note pointing here.
* The `discovery-docs` contract is updated to record a **closed** two-member family, with the provisional
  member resolved.
* **`discovery-docs` is now at its family boundary**, so the batch review it was always going to get covers
  two members rather than three.
* Nothing else is blocked. No other family, contract or bundle depended on this type.

### What would reopen this, stated so it is falsifiable

This is a finding about the world as searched on 2026-08-05, not a judgment that the document could never
exist. **Any one of the following reopens it**, and none requires re-litigating the rule:

1. **A named source publishes a document whose defined purpose is to commission a prototype**, with a
   structure, under any title. A design consultancy, a government service manual, a university design
   programme or an established practitioner would all qualify. The test is the document, not the publisher's
   prestige.
2. **Scaled Agile, Strategyzer or a comparable publisher converts a canvas or card into a document.** The
   gap found here is precisely one of *form*: the content exists, the written artifact does not.
3. **A different type name passes on its own evidence.** `experiment-brief` and `assumption-test` were
   searched and found only in vendor content, but a targeted pass against a specific named methodology (for
   instance Bland and Osterwalder's *Testing Business Ideas*, whose Test Card was reached here but whose book
   text was not) could settle it properly rather than by search snippet.
4. **A real team asks for one.** Grow-by-pull governs Tier-2 and Tier-3, and a documented request from a real
   team is evidence of circulation that a web search cannot produce.

## More Information

**The research is not wasted, and two findings from it are worth keeping.**

**A controlled study exists on prototyping practice, and it has a direct template implication.** Dow et al.
(2010, ACM TOCHI, N=33) found that teams exploring **multiple prototypes in parallel** outperformed teams
iterating serially on one, on click-through rate, expert ratings and self-reported confidence, and that
nearly half of the serial group reacted defensively to critique against none of the parallel group. Camburn
et al. corroborate that "teams iterating on a design significantly outperform teams without iteration". If a
prototype-commissioning section is ever added to another bundle, that is the evidence it should rest on.

**The boundary tests are sound and reusable.** The research anchored each neighbouring document to a named
source that defines it: design brief, PRD, test plan, A/B experiment, SAFe spike, statement of work and
creative brief. Those tests would serve any future bundle in this area, and they are the reason this record
can say with confidence that every candidate found *was* one of those neighbours under a different name.

**On method.** The first dimension was deliberately written to make a negative answer safe to report, and
five other dimensions reached the same conclusion without being asked the question. The pattern is worth
repeating whenever an admission test is run against a type the library has already committed to on paper,
because by that point every incentive points toward confirming it.

**The evidence is preserved.** All 29 sources, with their retrieval status, `Supports:` clauses and verbatim
quotables, are recorded in
[`prototype-brief-admission-evidence.md`](../prototype-brief-admission-evidence.md), in the format a research
log uses. The bundle was never built, so there is no `templates/prototype-brief/` to hold them. Anyone
reopening this question should start there rather than re-fetching.

Related records: [ADR 0030 (templating scope and the admission test)](0030-templating-scope-markdown-documents.md),
[ADR 0031 (the discovery-docs contract and the provisional member)](0031-adopt-discovery-docs-family-contract.md),
[ADR 0028 (the format-axis rule the admission test generalises)](0028-adopt-a-format-axis.md).
