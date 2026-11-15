---
status: accepted
date: 2026-11-14
decision-makers: [jprisant]
consulted: [claude]
---

# `competitive-analysis` joins `strategy-docs` as an eighth member, at `classification: utility`

## TL;DR

- **Decision.** The competitive analysis, catalog entry 11 and issue #361 (bundle: competitive-analysis), is admitted
  as the bundle **`competitive-analysis`**. It declares **`family: strategy-docs`** and **`classification: utility`**.
  The [contract](../contracts/strategy-docs.md) moves to `0.5.0`.
- **What the type is.** It says who else serves the customers we chose, how they compare on what those customers
  value, and what that means for our direction. It is kept current, not written once.
- **Why an amendment.** The family's list of questions is closed. This is its fourth widening, after
  [ADR 0070](0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md),
  [ADR 0076](0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md) and
  [ADR 0083](0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md). The new bullet sits immediately before the
  positioning statement, because `positioning-statement`'s guide names "the competitive analysis such language would
  be built on" as upstream work.
- **Why `utility`.** The contract's cut is "argued-and-durable versus maintained-and-periodic". The sources describe a
  maintained document: Aha! says "Assign a point person to keep the report updated throughout the year", and the
  GitLab handbook says the comparison "should be done at least annually".
- **Status:** accepted 2026-11-14. The maintainer read sweep 8's batched decisions, with the new bullet quoted
  verbatim, and chose this option. Asked whether the type belonged in strategy, foundation or opportunity, the
  maintainer read the recommendation and answered "d5 ok". **One change from what was read:** the G1 draft placed
  the bullet after the positioning statement. This record places it before, for the reason above. The maintainer
  reads the contract diff in this PR before it merges.

## Context and Problem Statement

Catalog entry 11 was reached by the 2026-10-04 ranking, the 2026-10-20 Define re-score and the 2026-10-23 Standard
run, and backlog section 9.3 listed it for a sweep. Admission sweep 8 ran on 2026-11-14 with three Sonnet readers and
one Sonnet critic. All 65 quotes for this candidate passed a fresh raw read. The working files are gitignored, at
`_local/research/2026-11-14_admission-sweep-8/`.

**All five admission checks pass or do not apply.**

1. **Written document.** It passes, at high confidence. Aha! ships a competitive analysis template, with a
   six-column table, a scorecard and an example. SVPG, the GitLab handbook and HubSpot also qualify.
2. **Phase fit.** Not applicable: the type left `define` in the 2026-10-20 re-score, and takes a `classification`.
3. **Written form.** It passes: a table of competitors by criteria, the shape `trade-study` and
   `platform-device-support-matrix` already ship in Markdown. A two-axis chart stays out.
4. **Not duplicated.** It passes, at medium-high confidence. No shipped bundle holds competitor profiles, a
   comparison table or a SWOT. Five bundles carry a fragment. `positioning-statement` takes one named alternative
   for one customer; this type maps many.
5. **Software audience.** It passes, at medium confidence. The GitLab handbook says "A Product Manager will lead
   their quad team", and Aha! writes "for product managers and product marketers".

## Decision Drivers

- The sources describe a maintained document, so the family must admit one kept current.
- `discovery-docs` admits documents "written once for a decision", and ADR 0081 rejected widening its "decide" to
  "inform".
- The maintainer's go-to-market scope question, which the positioning statement's spec left open, is answered for
  this type by admitting it. It is not answered for battlecards, win-loss analysis or messaging frameworks.

## Considered Options

1. **`strategy-docs`, `utility`, by an eighth question.** Chosen.
2. **`strategy-docs`, `foundation`.** Rejected. A competitive analysis changes when competitors move, not when our
   strategy changes. "A dated snapshot, refreshed on triggers" fits the same quotes, which is why this was the
   considered alternative.
3. **`discovery-docs`, as a dated snapshot.** Rejected. The analysis informs a decision and decides nothing.
4. **An opportunity document.** There is no opportunity family. The opportunity statement is parked (#298), and the
   product opportunity assessment was declined by
   [ADR 0086](0086-product-opportunity-assessment-is-declined.md). Those documents consume a competitive analysis; the
   analysis outlives any single go-or-no-go decision.
5. **Park until the go-to-market scope is ruled**, as #258 (messaging framework) was parked. Rejected by the
   maintainer's choice.

## Decision Outcome

**Chosen: `strategy-docs`, `classification: utility`, with an eighth question.** The new bullet reads:

> a **competitive analysis** says who else serves the customers we chose, how they compare on what those customers
> value, and what that means for our direction (added 2026-11-14, ADR 0091);

**Membership, honestly read.** The membership sentence admits a type that "sets or tracks product direction above the
level of any single deliverable". A competitive analysis tracks the market our direction answers to, and its last
part states what that means for the direction. That is a reading of "tracks", recorded here, not a certainty.

**The chain place is the library's POSITION.** No source states the sequence. It rests on the positioning guide's
line naming the analysis as upstream work.

### The counter-arguments this record keeps

- **The cadence evidence rests on vendors.** Nearly every cadence source sells tooling or monitoring, so the weight
  may overstate how often teams revise. The build should look for a practitioner source.
- **The name may cover several documents.** Aha! ships ten templates under the name, and HubSpot a ten-template kit.
  One Aha! template still passes check 1, and the bundle templates one document. It should link to a sales
  battlecard (catalog 196), not hold one.

### Consequences

- `strategy-docs` grows from seven members to eight and moves to `0.5.0`.
- Catalog entry 11 is corrected at the build by procedure 1: its stage "market/discovery" is not a phase value, and
  its note cites a BABOK technique, which cannot count under ADR 0030.
- Sizing evidence for the spec: two sizes. Lean holds Aha!'s six columns per competitor (mission, pricing, top
  features, strengths, weaknesses, differentiators), a comparison table and an implications section. Full adds
  per-competitor brief sections and a jobs-based rating like GitLab's. The frontmatter carries a last-refreshed date
  and a review trigger. Aha! and Productboard carry no reuse licence, so the template describes their structure and
  copies none of it.

## More Information

- Family contract: [`strategy-docs`](../contracts/strategy-docs.md), adopted by
  [ADR 0027](0027-adopt-strategy-docs-family-contract.md).
- The previous widening: [ADR 0083](0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md).
- The plan that ran the sweep: [`section9-candidates-plan.md`](../section9-candidates-plan.md).
