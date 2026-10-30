---
status: accepted
date: 2026-10-30
decision-makers: [jprisant]
consulted: [claude]
---

# `lean-ux-canvas` joins `discovery-docs` as a sixth member, at `phase: discover`

## TL;DR

- **Decision.** Jeff Gothelf's Lean UX Canvas, issue #330 (bundle: lean-ux-canvas), is specced as the bundle
  **`lean-ux-canvas`**. It declares **`family: discovery-docs`** and **`phase: discover`**. The
  [contract](../contracts/discovery-docs.md) moves to `0.6.0`. It ships in one size, `[lean]`, recommended.
- **Why now.** The maintainer chose on 2026-10-30 to put the canvas in the library and to give it priority P2,
  under [ADR 0041](0041-maintainer-preference-sets-the-build-order.md) (maintainer preference sets the build
  order). Admission sweep 7 had recommended a decline at medium confidence on 2026-10-29. This record says why
  that recommendation's two grounds do not control.
- **Why an amendment, and how small.** The membership sentence admits the canvas as written. What blocks it is
  the cadence clause, because Gothelf describes a team returning to the canvas after each experiment. Section 1
  gains a member bullet and a second bounded exception to the cadence clause. Section 4 gains an example bullet.
  Sections 2, 3, 5 and 6 do not change, and check K does not change.
- **What this admits, and what it does not.** It admits the eight-box canvas that frames one initiative. It
  does not admit Gothelf's Lean Strategy Canvas, Jeff Patton's Opportunity Canvas or Ash Maurya's Lean Canvas.
  [ADR 0083](0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md) (lean-canvas joins strategy-docs)
  places Maurya's canvas separately.
- **Status:** proposed 2026-10-30, **accepted 2026-10-30 after the maintainer's read** of this record and its
  contract diff. The maintainer added a reading of the cadence clause: it states "the spirit of the tools and
  resource", not "a hard-lined law". This record's exception is written in that spirit, bounded by the end the
  sources describe. The spec's choices C1 to C7 are still open.

## Context and Problem Statement

Issue #330 opened on 2026-10-27, from the PM resources run of 2026-10-23. Admission sweep 7 ran on 2026-10-29.
Its quotations were checked against raw page text in the main loop, and all of them pass on their correct pages.

**The sweep found the type admissible.** Gothelf's own pages publish the canvas box by box, with a prompt and
a worked example for each box. Under
[ADR 0078](0078-maps-canvases-and-session-records-are-templatable-through-their-written-form.md) (maps,
canvases and session records are templatable through their written form), that is the written form. A second
named source, the `template.md` file in Dean Peters's Product-Manager-Skills repository, renders it as
Markdown: "Use this template to capture the eight Lean UX Canvas boxes." The canvas also clears
[ADR 0080](0080-admission-gains-a-software-audience-check.md) (the software-audience check). An Atomic Object
post says it "can be leveraged at the beginning of new software products to help align the team around the
problem".

**The sweep recommended a decline on two grounds.**

1. **Duplication, the load-bearing ground.** Its internal reader mapped each box onto a shipped bundle. The
   business problem maps to `problem-statement`, the outcomes to `product-vision`, the users to `user-persona`,
   the solutions to `design-brief` and the PRD, and the hypotheses and experiment to `experiment-design-doc`.
2. **Phase fit, the weaker ground.** The sweep tested the canvas at `phase: define` only. It failed there by
   analogy to the Lean Canvas paragraph in [`backlog.md`](../backlog.md) section 4, because the canvas
   carries a Solutions box.

The maintainer read the recommendation and chose to include the canvas. Two questions then remain. Which
family and phase admit it, and does the duplication finding stand in the way?

**The canvas has been renamed.** On 2024-11-04 Gothelf wrote: "The canvas is now called the Lean Product
Canvas." He also wrote that "fundamentally there was nothing wrong with the canvas in its current state rather
its positioning and prompts had to shift to reflect a broader scope". The same post introduced a second
canvas, the Lean Strategy Canvas.

## Decision Drivers

- **The admission bar does not move.** One named source must publish the type's written form, under
  [ADR 0048](0048-one-named-source-clears-the-admission-test.md) (one named source clears the admission test).
  The canvas clears it on the originator's own pages.
- **A phase value has to mean one thing.** The canvas lists candidate solutions and hypotheses about them, and
  it chooses no concept. `define` excludes that, so the honest phase is `discover`.
- **A widening must be the smallest honest one.** The cadence exception must be bounded the way
  [ADR 0077](0077-define-ends-with-a-chosen-concept.md) (define ends with a chosen concept)'s exception for `design-brief` is bounded: revised while
  one piece of work runs, and finished when that work ends.
- **A new member must carry a job no built member carries.** The duplication ground has to be answered on the
  document's job, not on its boxes.

## Considered Options

1. **Decline**, as sweep 7 recommended. The canvas's content stays spread across five bundles.
2. **A canvas format of an existing bundle**, such as `design-brief`, mirroring `product-vision`'s formats
   under [ADR 0028](0028-adopt-a-format-axis.md) (the format axis). `design-brief` sits at `define` and hands
   off one chosen concept, so a canvas that lists many solutions would break its phase rule.
3. **A new type in `experimentation-docs`.** That contract admits a document that "plans or reports on one
   discrete test of a hypothesis". It also excludes "a test run before anything is built, to decide whether to
   build it". The canvas frames many hypotheses and plans no single test in detail, so it fails on both counts.
4. **A new type in `discovery-docs` at `phase: discover`, with a second bounded cadence exception.** Chosen.

## Decision Outcome

**Chosen: option 4.** `lean-ux-canvas` joins `discovery-docs` as its sixth member, at `phase: discover`.

### Why it fits

1. **The membership sentence fits as written.** A member exists "to decide whether to build something, or which
   concept to design, before anyone commits to building it." Gothelf's Box 7 asks "What's the most important
   thing we need to learn first?" Box 8 asks "What's the least amount of work to learn the next most important
   thing?" Both questions come before any commitment to build.
2. **It is written at the start of an initiative.** Gothelf wrote in 2024: "We designed these two canvases to
   help teams have the right conversations as they set out on new initiatives together." His how-to page opens
   the walkthrough with the business problem: "We'll start off with the business problem statement."
3. **It does a job the contract once reserved and never filled.** Section 4 records that `prototype-brief` would
   have "commissioned a cheap test of an unproven assumption". ADR 0035 (prototype-brief fails the admission
   test) found no source publishing that document. ADR 0078 said a card or worksheet with its own written form
   "would be a different candidate type, tested on its own evidence". The Lean UX Canvas is such a candidate.
   This record does not reopen `prototype-brief`.

### Why `discover`, not `define`

The `define` rule admits a document that converges on one chosen problem and, at most, one chosen concept. The
canvas does neither. Gothelf says Box 5 "provides the opportunity to offer up solutions big, small, innovative
and perhaps a bit “weird.”" His hypothesis grammar names a solution: "We believe a 25% reduction in
administration costs will be achieved if Rochelle the System Admin spends less time configuring users with a
batch configuration tool." The 2026-10-20 Define re-score failed the canvas's hypothesis box at `define` on the
same text. Every other member of this family declares `discover`, so the canvas does too.

### The second cadence exception

**The cadence clause says every member "is written once for a decision, and is finished when that decision is
made."** The canvas is revised while its experiments run. Gothelf's how-to page closes the loop after Box 8: "If
we should, then we ask the questions again in box number 7." Its next sentence reads: "Then we start the process
again." His 2019 post calls the canvas "a kind of “insurance policy” to ensure learning takes place in every
sprint".

**It is still finished.** The Atomic Object post calls the canvas "a living document that shows where the
project is in its progression towards a fully baked concept". It also reports that "On each project, there came
a point where the canvas had enough definition that it was essentially abandoned in favor of other tools that
fit the team’s changing needs."

**So the exception is bounded as `design-brief`'s is.** A `discover` member that frames one initiative's
hypotheses may be revised while the team's experiments on them run. It is finished when the team commits to
building, changes course or stops the initiative. It never becomes a standing instrument revised on a cadence.
`lean-ux-canvas` is the one member that takes this exception.

### The duplication ground, answered on the document's job

**The box map is accurate.** Each of the eight boxes asks a question that a shipped bundle also asks. This record
does not dispute that.

**The declines it was compared to rested on whole jobs, not boxes.** ADR 0064 (deployment-plan is declined)
found that its job is already done by documents in other shapes: a shipped `launch-coordination-checklist`
holds its rollout and rollback, and an IT change record holds the rest. ADR 0074 (the per-feature measurement
plan is declined) found that its content already ships inside the PRD. In both, a shipped or named neighbour
already did most of the declined type's job.

**No shipped document does this canvas's job.** Its job is to link a business outcome, a user, a benefit and a
candidate solution in one hypothesis. It then picks the riskiest of those hypotheses and the least work that
would test it, on one page, for one initiative. A team would need five documents to assemble the same view, and
none of them holds the link:

- `problem-statement` frames a problem "before anyone names a solution", so it cannot hold a hypothesis.
- `experiment-design-doc` plans one test, after the riskiest assumption is chosen. The canvas is where that
  choice is made, and Box 8 hands off to it. Gothelf says experiment design "can’t really be boiled down into a
  box on a canvas".
- `design-brief` hands off one chosen concept. The canvas has not chosen one.
- `user-persona` and `product-vision` define who and why for a whole product, not for one initiative.

**The library already ships box-level overlap in a canvas.** `product-vision`'s default `canvas` format has a
section titled "Who It Is For, and What They Need", which is ground `user-persona` covers in depth. The library
ships both, because the canvas's job is the one-page view and the persona's is the researched portrait.

This answer is the library's POSITION, labelled so under
[procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world). No source
read compares the canvas with these five documents.

### The size

**`[lean]`, one size, recommended at medium-high confidence.** Gothelf publishes one shape, eight boxes on one
page, and no source read splits a short canvas from a long one. The contract permits `[lean]` for a type whose
own research shows it does not earn a second weight. The build's research may find otherwise.

### What widens, and by how much

- **Section 1's member list** gains a sixth bullet for the Lean UX Canvas.
- **Section 1's cadence clause** gains a second bounded exception, naming `lean-ux-canvas` as the one member
  that takes it. The first exception's closing words, "no other member takes this exception", stay true,
  because they refer to that first exception.
- **Section 4** gains the canvas's shared-scenario bullet.
- **The header's Members line** and the change note record the new member and version `0.6.0`.

The membership sentence, the header's Axis line, section 2, section 3, section 5 and section 6 do not change.
Check K does not change: it already gates `["discover", "define"]`, and `[lean]` is already an allowed size
shape. The exact text is in the contract diff that accompanies this record.

### What the decision costs, stated rather than smoothed over

1. **The cadence clause loosens a second time.** Each exception weakens the family's "written once" rule a
   little. This one stays bounded by an end the sources describe, abandonment once the concept is defined
   enough.
2. **The duplication answer is the library's position.** A reader who weighs the box map most heavily would
   decline the type, as sweep 7 did.
3. **The name is in transition.** The originator now calls it the Lean Product Canvas. A reader who searches
   for the new name must still find this bundle, so that name must be an alias.
4. **The prompts are Gothelf's, and no licence was found.** Sweep 7 found no Creative Commons licence on his
   pages. The bundle may name the boxes and quote them briefly with attribution. Its guidance comments must be
   the library's own words.
5. **The unproven surface grows.** The library's efficacy runs found that documents written with these
   templates score no better than a strong generic-prompt control on decision-usefulness criteria. A
   facilitation canvas keeps much of its value in the conversation, which widens that surface faster.

### Consequences

- **The contract moves to `0.6.0`.** Check K does not change.
- **The bundle id is `lean-ux-canvas`**, the id of issue #330. "Lean Product Canvas" is an alias, recommended.
  The spec states the alternative of building under the new name.
- **The catalog gains entry 211 when the bundle lands**, as entry 209 arrived with `design-brief`'s build.
  No catalog row is added by this record.
- **The successor obligation binds the new member.** Section 1 requires its companion to name the document that
  takes over. That document is `experiment-design-doc`, for the riskiest assumption's test. When the team
  commits to building, the successor is `design-brief` or the PRD. The choice is the library's POSITION.
- **No built bundle changes family or phase.** Existing members are not swept for a reciprocal mention, the
  precedent [ADR 0076](0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md) recorded.
- **`pairs_with: []`.** No skill in `tools/known-skills.txt` addresses a Lean UX Canvas, checked on 2026-10-30.
- **The Lean Strategy Canvas and Patton's Opportunity Canvas stay unadmitted.** Each would be its own candidate,
  tested on its own evidence.
- **The bundle stays subject to [ADR 0030](0030-templating-scope-markdown-documents.md) (templating scope).** This record removes the family objection only.

## More Information

- The family contract: [`discovery-docs`](../contracts/discovery-docs.md), adopted by
  [ADR 0031](0031-adopt-discovery-docs-family-contract.md) (adopt the discovery-docs family contract). ADR 0063
  (project-brief reopens discovery-docs), ADR 0069 (problem-statement joins discovery-docs), ADR 0077 and
  ADR 0079 (design-brief joins discovery-docs at define) amended it.
- The cadence precedent: ADR 0077's exception, which ADR 0079 named for `design-brief`.
- The spec: [`tier2-specs.md`](../tier2-specs.md), the `discovery-docs` (sixth member, at `discover`) section.
- The sources, each terms-checked before it was read, and every quotation in this record raw-checked on
  2026-10-30: Gothelf's
  [Lean UX Canvas V2](https://jeffgothelf.com/blog/leanuxcanvas-v2/) (2019-09-09),
  [How to use the Lean UX Canvas](https://jeffgothelf.com/blog/how-to-use-the-lean-ux-canvas/) and
  [The Lean Product Canvas](https://jeffgothelf.com/blog/the-lean-product-canvas/) (2024-11-04); Atomic
  Object's [Intro to Lean UX Canvas](https://spin.atomicobject.com/lean-ux-canvas-intro/); and Dean Peters's
  [`template.md`](https://raw.githubusercontent.com/deanpeters/Product-Manager-Skills/main/skills/lean-ux-canvas/template.md).
- The research, in gitignored working files: `_local/research/2026-10-29_admission-sweep-7/` and
  `_local/research/2026-10-30_canvases-placement/`.
