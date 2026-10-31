# lean-canvas: history

Change log for the `lean-canvas` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-10-30

**Initial release.** Researched 2026-10-30, building on the 2026-10-11 Define sweep, the 2026-10-20
re-score and the placement research of 2026-10-30, which raw-checked the admission quotations on Ash
Maurya's own pages. The build's six-dimension fan-out covered origins (the 2010 post and its lineage from
Osterwalder's Business Model Canvas), structure (the nine boxes, three sub-blocks and fill order), practice
(who fills it and how it changes), debates (startup against established company, canvas against business
plan, the solution-first trap, the dropped boxes), relationships (the Business Model Canvas and the Product
Vision Board) and the gap question.
[`lean-canvas_research-log.md`](lean-canvas_research-log.md) records **15 sources**, all fetched and
verified: 10 primary, 3 practitioner and 2 vendor. Eleven of the fifteen are Maurya's own pages or his
company's. Every quotation was checked against the source's raw text rather than a retrieval summary,
leaving **107 Quotable lines**, 83 from the fourteen web entries and 24 from a copyrighted 40-page
walkthrough PDF read from the maintainer's own copy and never committed.

**The seventh `strategy-docs` member, added by amendment**, admitted by
[ADR 0083 (lean-canvas joins strategy-docs as a seventh member)](../../docs/internal/decisions/0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md),
which also amended the family contract to 0.4.0 and placed this type second in the chain, between the
product vision and the product strategy. That placement is this library's own POSITION, not a sequence any
one source states; Roman Pichler's sequencing of his Product Vision Board before business-model detail
weakly supports it, and a reader who treats the canvas as the strategy's business model, kept current
beside the roadmap, would place it after the strategy instead.

### One size only, by the research's own finding

This bundle ships `lean` and no `full`. Every source that addresses length agrees the canvas is meant to be
compact, not offered in a longer form: "Embrace a 1-page constraint," and "Sketch a canvas in one sitting."
A second customer segment is handled by sketching a second canvas, not by widening one canvas to hold both:
"Sketch a Lean Canvas for each customer segment."

### classification: utility, not foundation

The maintainer's ruling of 2026-10-30 fixes `utility`. Maurya calls a canvas "a snapshot" and teaches that
"you start with a best guess and then iterate from there"; its revisions follow test results, not a
calendar, which is the same argued-and-periodic shape the family contract already applies to
`product-roadmap` and `okrs`. No source read states a calendar interval for revising a canvas, which the
research log records as an absence within the sources read, not as a wider claim.

### Two sections are the library's own POSITION, not sourced practice

Section 10 (Riskiest Beliefs and Next Tests) and section 11 (Versions) are not boxes any source publishes on
a Lean Canvas. Maurya teaches the underlying practices, naming the riskiest assumption and testing it, and
versioning a canvas as it changes, as disciplines layered on top of the nine-box canvas, not as fields the
canvas itself asks for; his own tool versions a canvas automatically, which is a software feature rather
than founder practice. The template and companion label both sections the library's POSITION rather than
Maurya's.

### The Leaner Canvas question is resolved, reversing an earlier "unresolved" finding

An earlier pass searched Maurya's and his company's pages for a "Leaner Canvas" and reported the question
open. This research found and read his 2024-09-07 post directly: the "Leaner Lean Canvas" is his own narrowing
exercise onto the two outer boxes, Customer Segment and Problem, for the earliest stage of belief-grounding,
not a separate or alternate canvas. The guide and companion present it as a focusing exercise on this same
canvas, never as a variant template.

### Misattribution is this type's named hazard

The canvas is copyrighted, with no open licence found on Maurya's own pages. Every direct quotation in this
bundle is drawn only from entries [1] to [8], [11], [13] and [15] of the research log, each marked
fetched-and-verified; the one trade-press entry [10] reporting Maurya's "innovator's bias" framing is
attributed as reported speech, never quoted as his own words. The template and companion also name, once,
the unrelated collision with `product-vision`'s own lean-size `canvas` format, which this library's guide
calls "the lean canvas" in an unrelated sense.

### What the document does not carry

Nothing in the template carries a multi-year financial forecast (`business-case`'s job), a decision about
which problems to pursue (`product-strategy`'s job), or one initiative's hypotheses in isolation
(`lean-ux-canvas`'s job). The Revenue Streams and Cost Structure boxes ask for a near-term milestone, three
to six months out, never a multi-year model.

### pairs_with and related_templates

`pairs_with` ships `[foundation-lean-canvas]`. [`tools/known-skills.txt`](../../tools/known-skills.txt) was
checked on 2026-10-30 and carries `foundation-lean-canvas`, verified present in
`product-on-purpose/pm-skills` at `skills/foundation-lean-canvas/SKILL.md`; its own description names
"framing a new product thesis, stress-testing an existing strategy," which this bundle's job matches
directly.

`related_templates` names `product-vision`, `product-strategy`, `positioning-statement`,
`north-star-metrics`, `business-case`, `user-persona` and `lean-ux-canvas`, the siblings the guide's own
"Is this the right document at all?" table and the companion's Relationships section name as the boundaries
this type draws. `product-vision` and `product-strategy` are also the two sources the worked example is
dated and scoped against: the example's canvas is sketched five days after the dated `product-vision`
example, and its opening blockquote dates the revision a week before the `product-strategy` example, which
names this same OEM channel a non-target; the body of the example makes no forward reference to that later document.
