---
status: proposed
date: 2026-10-30
decision-makers: [jprisant]
consulted: [claude]
---

# `lean-canvas` joins `strategy-docs` as a seventh member, at `classification: utility`

## TL;DR

- **Decision.** Ash Maurya's Lean Canvas, catalog entry 5 and issue #337 (bundle: lean-canvas), is specced as the
  bundle **`lean-canvas`**. It declares **`family: strategy-docs`** and **`classification: utility`**
  (recommended). The [contract](../contracts/strategy-docs.md) moves to `0.4.0`. It ships in one size,
  `[lean]`, recommended.
- **Why now.** The maintainer chose on 2026-10-30 to put the canvas in the library and to give it priority P2,
  under [ADR 0041](0041-maintainer-preference-sets-the-build-order.md) (maintainer preference sets the build
  order). The canvas was never declined. The 2026-10-20 Define re-score kept it out of `phase: define` only, and
  no record tested it in any other family.
- **Admission now rests on Maurya's own page.** His "What is a Lean Canvas?" teaches each box in prose. Under
  [ADR 0078](0078-maps-canvases-and-session-records-are-templatable-through-their-written-form.md) (maps,
  canvases and session records are templatable through their written form), that is the written form. The
  2026-10-11 sweep's one clean source, Atlassian's Confluence template, sits on a site whose terms bar
  automated reading, and this record does not rely on it.
- **Why an amendment.** The membership sentence admits the canvas as written. What blocks it is the closed list
  of six questions that follows the sentence. This is the third widening of that list, after
  [ADR 0070](0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md) and
  [ADR 0076](0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md).
- **What this does not admit.** It does not admit Osterwalder's Business Model Canvas, catalog entry 4, or Jeff
  Gothelf's Lean Strategy Canvas. Gothelf's Lean UX Canvas is placed separately, by
  [ADR 0082](0082-lean-ux-canvas-joins-discovery-docs-at-discover.md) (lean-ux-canvas joins discovery-docs).
- **Status:** proposed 2026-10-30. This record amends a family contract, so it stops for the maintainer's own
  read, under [decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer). Nothing
  in it takes effect before that read.

## Context and Problem Statement

**The Lean Canvas was researched once, for the wrong question.** The Define admission sweep of 2026-10-11
asked whether it was a `define` document. It found the canvas a business-model snapshot, not problem framing,
and its row in [`tier2-specs.md`](../tier2-specs.md) reads "Not now, and not a Define candidate." The Define
re-score of 2026-10-20 kept it out of `define` on the same grounds. Neither tested a `classification` family.
[`backlog.md`](../backlog.md) section 4's phrase "stay out" has since been read as a library-wide verdict,
which it never was.

**Admission was contested inside that sweep.** Its two research dimensions disagreed about whether Maurya's
own site serves "a document template" or "a board". Admission survived on Atlassian's Confluence template page
alone. Two things have changed since:

1. **ADR 0078 retired the stricter test.** On 2026-10-17 it ruled that a canvas is in scope through "The
   structured written form a named source publishes, such as fields, sections or a table". The "document or
   board" dispute was argued under the test that record retired.
2. **Atlassian's site is treated as barred.** On 2026-10-29, admission sweep 7's agents reported that its
   Acceptable Use Policy bars automated access. That clause has not yet been checked against the raw terms
   page, but no agent reads the page while the report stands. The maintainer may read it by hand.

**Maurya's own page now carries admission.** "What is a Lean Canvas?", on leanspark.ai and dated 2024-09-07,
is bylined Ash Maurya. It defines the canvas as a tool that "helps you deconstruct an idea into key assumptions
or beliefs." It states the origin: "Lean Canvas was created by me, Ash Maurya, and is an adaptation of
Alexander Osterwalder’s Business Model Canvas - optimized for the Lean Startup methodology." It then teaches
each box in turn, with the sub-blocks inside them: "List existing alternatives", "Home in on early adopters"
and "Create a high-concept pitch." Its terms page, read on 2026-10-30, carries no bar on automated reading.

**The block count is not a contradiction.** The 2026-10-11 sweep flagged the site for claiming "12 blocks" in
one place and "nine empty boxes" in another. Maurya's product page lists "The 12 blocks of a Lean Canvas". They
are the nine boxes plus three sub-blocks: "Existing Alternatives", "Early Adopters" and "High-Level Concept".
The teaching page treats each of those three inside its parent box.

**The canvas clears the software-audience check.** ADR 0080 (the software-audience check) asks for one named
source showing a software, UX or technology team using the document. Maurya's teaching page lists "Typical
SaaS metrics" as examples for the Key Metrics box.

## Decision Drivers

- **The admission bar does not move.** One named source must publish the written form, under
  [ADR 0048](0048-one-named-source-clears-the-admission-test.md) (one named source clears the admission test).
- **The family's own test decides placement, not a skill pairing.** This contract's metadata row already names
  a pm-skills `foundation-lean-canvas` skill. That is a `pairs_with` fact and carries no weight here.
- **The axis call follows the contract's own distinction**, "argued-and-durable versus maintained-and-periodic".
- **A new member must carry content no built member carries.**

## Considered Options

1. **Leave it out.** The canvas's boxes stay spread across `business-case`, `product-vision`, `product-strategy`
   and `user-persona`.
2. **`discovery-docs` at `phase: discover`.** That contract's cadence clause requires every member to be
   "written once for a decision" and finished when the decision is made. Maurya teaches the opposite: "Like
   everything on the canvas, you start with the best guess and iterate from there." The canvas is a standing
   model, which that contract sends to "a `classification` family".
3. **A canvas format of `business-case` or `product-strategy`**, under
   [ADR 0028](0028-adopt-a-format-axis.md) (the format axis). `business-case` is written once to justify one
   investment, so a format revised as tests arrive would break its cadence. `product-strategy` is
   `foundation`, argued and changed on a timescale of years. A canvas revised as each assumption is tested
   would break its class.
4. **A new type in `strategy-docs`, at `classification: utility`, as a seventh member.** Chosen.

## Decision Outcome

**Chosen: option 4.** `lean-canvas` joins `strategy-docs` as its seventh member, at `classification: utility`
(recommended).

### Why it fits, positively

1. **The membership sentence fits as written.** A member "sets or tracks product direction above the level of
   any single deliverable". A Lean Canvas states the business model a product is betting on: its customers and
   their problems, its value proposition, how it reaches and earns from them, what it costs and how its
   progress is measured. That sits above any single deliverable.
2. **The axis needs no change.** The contract already gates the set `foundation` or `utility`.
3. **Its content is distinct where it matters.** No shipped member or neighbour carries Channels, Revenue
   Streams, Cost Structure and Unfair Advantage together as one model under test. `product-strategy` chooses
   problems and segments and states no revenue model. `business-case` costs one investment once.

### Why `utility`, not `foundation`

**The contract's test is "argued-and-durable versus maintained-and-periodic".** A `utility` member's "value
comes precisely from being kept current". Maurya describes a canvas kept current in that way:

- "Unlike a business plan, the goal with a Lean Canvas isn’t to achieve perfection but to take a snapshot."
- "Like everything on the canvas, you start with the best guess and iterate from there."
- On costs: "First, model the runway you will need to define, build, and launch your MVP. Then, revise after
  you get there."
- His product page says "Your canvas is versioned automatically" and "Variants are alternative versions of your
  business model."

**No originator page read states a calendar interval.** The revisions are event-driven: a test result, a
changed problem, a new stage. `utility` is the closer reading, at medium confidence. `foundation` is the
considered alternative. A reader who treats the canvas as a founder's argued thesis would choose it.

### Where it sits in the chain, and why

**Second, between the product vision and the product strategy (recommended).** The vision says where the
product is trying to get to. The Lean Canvas states the business model that could get it there, as beliefs to
test. The strategy then commits to the problems and segments those beliefs support. Maurya's teaching page
frames the canvas the same way: "Based on your current stage and what you know, what are the next hypotheses you
need to test to move your product forward?"

**No source states this sequence.** The placement is argued from what the canvas depends on and what depends on
it. A reader who sees the canvas as the strategy's business model, kept current beside the roadmap, would place
it after the strategy instead. The chain link is the library's POSITION, labelled so under
[procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world).

### The duplication ground, answered on the document's job

The 2026-10-20 re-score found that "Most of its content already ships, split across other bundles". It named
`business-case`'s Problem and Opportunity section, `product-vision`'s Why Us section and `user-persona`. The
box map is accurate. It does not show that any shipped document does the canvas's job:

- **`business-case`** justifies one investment and is then finished. The canvas models the whole business and
  is revised as its assumptions are tested.
- **`product-vision`** is `foundation`, changed on a timescale of years. Its Why Us section asks the
  Unfair Advantage question once. The canvas asks it again whenever the model changes.
- **`product-strategy`** chooses problems and segments and names no revenue stream, channel or cost structure.
- **`user-persona`** portrays a user from research. The canvas names a segment and its early adopters in a line.

This answer is the library's POSITION. No source read compares the canvas with these four bundles.

### The size

**`[lean]`, one size, recommended at medium-high confidence.** Maurya publishes one page, and he says "Embrace a
1-page constraint". No source read splits a short canvas from a long one.

### What widens, and by how much

- **Section 1's list.** "six questions" becomes "seven questions", and a new second bullet names the Lean
  Canvas's question. The strategy, positioning, North Star, roadmap and OKR bullets each move down one place,
  with no wording change.
- **Section 1's chain sentences** gain a third POSITION link, for a strategy that contradicts the current
  canvas. Two sentences that counted places lose their ordinals, because the list grew at second place. The
  North Star metric's place becomes "after the strategy", and Nair's reading of the positioning statement
  pulls "toward an earlier place" rather than toward second place.
- **Section 2.** The classification row and the axis note name the Lean Canvas as `utility` (recommended). The
  methodology row names it as methodology-bound, to Lean Startup. The axis note's "All six members" becomes
  "All seven members". The `sizes_available` row needs no change, since `[lean]` alone is already allowed.
- **Section 4.** The shared-scenario obligation gains the Lean Canvas's example.

The membership sentence, the axis set, the structural obligations and the enforcement section are unchanged.
The exact text is in the contract diff that accompanies this record.

### What the decision costs, stated rather than smoothed over

1. **The canvas was built for startups.** Maurya's product page says it "adapts Alexander Osterwalder's
   Business Model Canvas for startups operating under conditions of extreme uncertainty." The shared-scenario
   rule puts the example inside Acme Analytics, an established company. The spec recommends an example that
   models a new line of business inside Acme, which is the closest honest fit.
2. **The chain position is argued, not sourced.** The alternative position is stated above.
3. **The name collides inside the library.** `product-vision_guide.md:69` uses "the lean canvas" for that
   bundle's lean-size `canvas` format. A reader could take it for this bundle.
4. **No licence was found on Maurya's pages.** A Creative Commons licence appears only on third-party mirrors.
   The bundle may name the boxes and quote Maurya briefly with attribution. Its guidance comments must be the
   library's own words.
5. **The unproven surface grows.** The library's efficacy runs found that documents written with these
   templates score no better than a strong generic-prompt control on decision-usefulness criteria. This bundle
   joins that surface.

### Consequences

- **The contract moves to `0.4.0`.** Its header gains an updated amended-by note, and a dated change note
  records the widening. Check K does not change.
- **The bundle id is `lean-canvas`, the same as the catalog id.**
- **The catalog row needs corrections on landing**, per
  [procedure 1](../decision-procedures.md#1-a-catalog-call-loses-to-research). Its only alias, "(Maurya
  adaptation of BMC)", is a note, not a name. Its purpose, "Problem-focused one-pager for startups",
  understates the solution and business-model content, as the 2026-10-11 sweep found. Its `stage: ideation`
  is free text, not a phase.
- **`product-vision`'s guide carries a dated clarification at landing**, so that its line 69 reads as the
  lean-size canvas format and not this bundle.
- **`pairs_with: [foundation-lean-canvas]`, recommended.** The skill is pinned in `tools/known-skills.txt`, and
  `product-strategy` already claims it. Both claims can stand.
- **Existing members gain no line.** They are not swept for a reciprocal mention, the precedent ADR 0076
  recorded.
- **The Business Model Canvas stays a separate candidate.** Maurya's page names the four boxes he replaced:
  "key partnerships, key resources, key activities, and customer relationships". That list is the boundary the
  companion draws.
- **The bundle stays subject to ADR 0030.** This record removes the family objection only.

## More Information

- The family contract: [`strategy-docs`](../contracts/strategy-docs.md), adopted by
  [ADR 0027](0027-adopt-strategy-docs-family-contract.md) (adopt the strategy-docs family contract) and amended
  by ADR 0070 and ADR 0076.
- The spec: [`tier2-specs.md`](../tier2-specs.md), the `strategy-docs` (seventh member) section.
- The sources, each terms-checked before it was read, and every quotation in this record raw-checked on
  2026-10-30: Maurya's [What is a Lean Canvas?](https://leanspark.ai/learn/what-is-lean-canvas) (2024-09-07),
  [Lean Canvas](https://leanspark.ai/leancanvas) and [the canvas guide](https://leanspark.ai/guides/canvas),
  all on leanspark.ai, where Maurya's leanstack.com now redirects.
- The research, in gitignored working files: `_local/research/2026-10-11_define-sweep/`,
  `_local/research/2026-10-20_define-rescore/` and `_local/research/2026-10-30_canvases-placement/`.
