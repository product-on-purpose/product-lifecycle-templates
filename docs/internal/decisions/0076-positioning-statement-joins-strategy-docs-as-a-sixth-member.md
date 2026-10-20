---
status: accepted
date: 2026-10-19
decision-makers: [jprisant]
consulted: [claude]
---

# `positioning-statement` joins `strategy-docs` as a sixth member, placed third in the chain

## TL;DR

- **Decision.** The catalog candidate `positioning-statement` (#256) is specced as the bundle
  **`positioning-statement`**. It declares **`family: strategy-docs`** and **`classification: foundation`**
  (recommended), and the [contract](../contracts/strategy-docs.md) moves to `0.3.0`.
  Section 1's members now answer six questions, not five. The positioning statement is third, between the
  product strategy and the North Star metric, which moves from third place to fourth. That place is
  argued, not sourced, and this record states the alternative a maintainer could choose instead.
- **Why an amendment.** The contract's membership sentence admits the type on its face: a positioning
  statement "sets or tracks product direction above the level of any single deliverable." What blocked it
  was the closed list of five questions that follows the sentence. This is the second widening of this
  contract's own list of questions, after
  [ADR 0070 (north-star-metrics joins strategy-docs)](0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md).
- **What this amendment admits, and what it does not.** It admits one type, read as the internal-facing
  document stating how this product stands against a named alternative, for a specific target customer,
  now. **It does not admit a messaging framework, a battlecard, a positioning map, or go-to-market documents
  generally.** `messaging-framework` (#258) is held, per the maintainer's 2026-10-15 sitting decision 7 and
  [decision procedure 10](../decision-procedures.md#10-a-family-or-axis-assignment-is-uncertain).
- **Why build it, given the ownership split the research found.** Two independent product-marketing
  sources place ownership of the positioning statement with product marketing, one of them (Blackblot) by
  name. This library places the type in `strategy-docs` anyway, on Aha!'s own catalog split (a
  strategy-side template filed separately from a marketing-side one) and on one named product-management
  practitioner's framing, not because those sources outnumber the product-marketing ones. This record
  states that placement as the library's own argued position, not as a majority reading of the sources.
- **What this does not decide.** The exact field labels inside the single template, which the build's own
  drafting settles against the Admission sources' copyrighted formula text. Whether `product-vision`'s
  companion gains more than the one dated note this record requires. The build order relative to any other
  queued candidate.
- **Status:** proposed 2026-10-19, drafted 2026-10-16, **accepted 2026-10-19 on the maintainer's
  delegation**. The contract read stops for the maintainer, per
  [decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer),
  which states that a family contract is "adopted only after a maintainer read." This record was written
  for that read. Told that the PR amends two family contracts and that nothing would merge before the
  read, the maintainer directed a merge on the agent's best judgment. That direction stands in for the
  read for this PR only, as similar ones did for
  [ADR 0070](0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md) and
  [ADR 0078](0078-maps-canvases-and-session-records-are-templatable-through-their-written-form.md).
  The standing rule is not repealed. The scope and the owner are the maintainer's own rulings of
  2026-10-15 and 2026-10-17. **Three parts were accepted without a read.** The first is the contract
  diff, including third place in the chain, which is argued here, not ruled. The second is the spec's
  suggested ownership default: product management owns the statement, and product marketing drafts or
  co-writes it. That default is the agent's reasoning, and no source states it. The third is the pair of
  contract edits added after the 2026-10-16 drafts: section 4's example obligation and the axis note's
  count of six. The maintainer may strike or change any of them by a dated note, and has not yet
  confirmed this delegated acceptance.

## Context and Problem Statement

Admission sweep 6 (2026-10-14) tested four candidates, among them `positioning-statement` (#256) and
`messaging-framework` (#258), against [ADR 0030](0030-templating-scope-markdown-documents.md)'s admission
test and against all ten family contracts. `positioning-statement` cleared admission on five sources and
found no contract that admitted it as written; `strategy-docs` was the only plausible candidate for
amendment, excluded on an argument rather than a quoted clause, the same exclusion pattern ADR 0070 found
for the North Star metric. The
sweep raised, and did not answer, a scope question: whether the library takes on go-to-market documents at
all. The maintainer answered on 2026-10-15 (sitting decisions 7 and 8): positioning only, as product
direction, specced next in `strategy-docs` by amendment, in a single size, with more research first to
raise confidence. That research ran the same day
(`_local/research/2026-10-15_sitting-followup/positioning.json`, gitignored) and is folded
into [the spec](../tier2-specs.md) this record accompanies, not added later as a dated note.

**Admission.** Five sources ship the positioning statement as a standalone written document or template:
MIT's Orbit Knowledgebase, HubSpot, Doug Stayman/eCornell, Yesware, and Product Marketing Alliance. Every
quotation below was checked against raw page text in
`_local/research/2026-10-14_admission-sweep-6/recheck-out.json` or, for the 2026-10-15 follow-up,
`_local/research/2026-10-15_sitting-followup/positioning-recheck-out.json` (both gitignored). MIT: "forces you to use a one
page format." HubSpot: "For [your target market] who [target market need], [your brand name] provides
[main benefit that differentiates your offering from competitors] because [reason why target market should
believe your differentiation statement.]" [ADR 0048](0048-one-named-source-clears-the-admission-test.md)
holds that one named source clears the test; this candidate clears it five times over.

**The admission does not rest on Geoffrey Moore.** Three independent research passes could not locate the
"for/who/that" wording inside *Crossing the Chasm* itself, by edition, chapter, or page. The follow-up found
a readable-source quote (a Goodreads reader-highlight note) matching the known template, and an independent
blog citing the 3rd edition (Harper Business, 2014) and page 186, a citation not itself verified against the
book. The chapter remains unfound. This record credits admission to the five sources above and treats Moore
as a named, unverified attribution, the same strength the spec states.

## Decision Drivers

- The membership test, not the list of members planned at adoption, governs a candidate.
  [ADR 0050](0050-qa-docs-admits-a-fourth-member.md) established that reading.
- **A widening must be the smallest honest one.** ADR 0060 set the standard: widen the one family whose
  chain already carries the type's job, by the fewest words, and say so in the record.
- A family declares `phase` or `classification`, never both
  ([ADR 0015](0015-second-taxonomy-axis-phase-xor-classification.md)). The type's cadence decides its axis
  before anything decides its family.
- **Scope stops for the maintainer when it crosses into a new kind of reader.** Positioning and messaging
  would be this library's first documents a product marketer, not a product manager, might author. The
  maintainer's 2026-10-15 ruling (take on positioning only, as product direction) is the scope boundary this
  decision operates inside; it is not reopened here.
- A family's teaching value is the relationship between its members. A new member must make that map
  clearer, not blur the boundary with an already-shipped neighbour.

## Considered Options

1. **`strategy-docs`, `classification: foundation`, as a sixth member, with the list of questions widened.**
   Chosen.
2. **Hold, pending the go-to-market scope question.** This was the state the sweep left the candidate in.
   Rejected for this record, because the maintainer's 2026-10-15 ruling already answered the scope question
   (positioning only, as product direction) and directed a spec.
3. **A new family for `positioning-statement` and `messaging-framework` together.** Rejected. The
   maintainer's sitting decision 7 answered "B" (positioning only), not "C" (a new family); building one
   around a single admitted member and one held candidate would design a family no second built member
   tests, the same reasoning ADR 0070 used to reject a one-member family for the North Star metric.
4. **`discovery-docs` or `standing-standards`.** Rejected on the sweep's own family-fit material: the sweep
   reported verdicts for exactly these three families (`strategy-docs`, `discovery-docs`,
   `standing-standards`), and all three excluded the type as written. Only `strategy-docs`'s exclusion
   rested on an argued rather than quoted clause, the gap this record closes by amendment, the same reading
   ADR 0070 gave for the North Star metric's own exclusion from the same two alternative families.
5. **Decline, in the shape of [ADR 0064](0064-deployment-plan-is-declined.md) and
   [ADR 0065](0065-steering-committee-pack-is-declined.md).** Rejected. Those records rested on duplication
   with an already-shipped bundle. `product-vision`'s own companion routes positioning content **out**
   ("competitive material sits separately as context") rather than absorbing it, so a decline here would
   rest on the no-family-fits ground alone, which ADR 0070's own amendment already shows is not a sufficient
   ground once the smallest-honest-widening standard is available.

## Decision Outcome

**Chosen: `strategy-docs`, `classification: foundation` (recommended), sixth member, placed third in the
chain.**

### Why it fits, positively

1. **The membership sentence fits as written.** A positioning statement states how this product is
   understood against a named alternative, for a specific customer, now, and that stance sits above any
   single deliverable's own scope.
2. **The axis needs no change.** The contract already gates the set `foundation` or `utility`, and this
   type's own shape, argued and revisited at a repositioning event rather than maintained on a calendar, is
   the `foundation` reading already applied to `product-vision`, `product-strategy` and
   `north-star-metrics`. **No source read states a review cadence for this type directly**; this record
   names that gap rather than papering over it, and names `classification: utility` as the considered
   alternative. See the spec's own Classification subsection for the full argument.
3. **The chain has a slot this type can fill.** The strategy chooses which segments and problems to pursue;
   positioning takes that choice and states the external-facing stance it implies, before the North Star
   metric asks whether that stance is working.

### Where it sits in the chain, and why

**Third, between the product strategy and the North Star metric, which moves from third place to fourth.**
The position is argued from what positioning depends on: a target segment and a set of problems the
strategy has already chosen. **No source states this exact sequence.** The 2026-10-15 follow-up found one
named source that pulls the other way: Devika Nair (Director of Product Management, Oracle), read and
raw-checked: "While product management is also responsible for the positioning, they are looking at it as
part of the vision" (continuing, per the fetch tool's truncation note, "and decision making"). A reader who
weights Nair's framing most heavily would place positioning second, between the vision and the strategy,
closer to where a vision-level stance is set rather than where a strategy-level choice is operationalized.

**The chain link is the library's POSITION**, labelled so under
[procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world).
No source read states the failure this link would name, and no source states the sequence itself, the same
posture ADR 0070 recorded for the North Star metric's own placement.

### What widens, and by how much

- **Section 1's list.** "five questions" becomes "six questions," and a new third bullet names the
  positioning statement's question. The bullet originally third (the North Star metric) becomes the new
  list's fourth bullet with no wording change beyond its new position; the roadmap and OKR bullets move
  from fourth and fifth to fifth and sixth, with no wording change.
- **Section 1's chain sentence** gains a second link, also labelled POSITION.
- **Section 1's relationship obligation.** Unchanged in wording ("against the other members"); it already
  covers a sixth member without amendment, the same reading ADR 0070 recorded when it widened the sentence
  from "other three" to "other members."
- **Section 2.** The classification row and the axis note name the positioning statement as `foundation`
  (recommended), the methodology row names it as methodology-agnostic, and the axis note's "All five
  members" becomes "All six members". The sizes_available row needs no change; `[lean]` alone is already an
  allowed value.
- **Section 4.** The shared-scenario obligation gains the positioning statement's example.

The membership sentence, the axis set, the structural obligations and the enforcement section are
unchanged. The exact text is in the [contract](../contracts/strategy-docs.md) and its `0.3.0` change note.

### Consequences

- **The contract moves to `0.3.0`.** Its header gains an updated amended-by note, and a dated change note
  records the widening.
- **The bundle id is `positioning-statement`, the same as the catalog id.** No reason was found for it to
  differ, the same bare-name convention `north-star-metrics`' own spec names for `tracking-plan`,
  `risk-register`, `raid-log`, `kpi-dashboard` and `issue-log`.
- **`product-vision`'s companion carries a required dated note, not a rewrite.** Lines 276 to 280 state "No
  product management source read draws this boundary." That sentence becomes false once this bundle's own
  admission evidence ships: the 2026-10-15 follow-up found one practitioner source, Sharebird, that draws
  the same boundary on time horizon and audience. Per the correction-versus-supersession rule in
  `docs/internal/decisions/README.md`, this is a factual correction, dated and named, not a silent rewrite,
  and it is listed as a required landing-site edit in the spec's own closing subsection.
- **`product-strategy`, `north-star-metrics` and `okrs`' companions gain no line.** This follows the
  precedent ADR 0070, ADR 0067 and ADR 0069 each set: an amendment's new member states its position against
  every existing member, but existing members are not swept for a reciprocal mention.
- **The boundary with `messaging-framework` is a division the library is not yet building, not a division
  of content inside one bundle.** `messaging-framework` stays held under decision procedure 10, and this
  record's own "What this amendment admits" clause states plainly that nothing here reopens that hold.
- **Single size, under the sweep's own finding, reconfirmed by the follow-up.** Every source that states a
  size points short, and the follow-up's own Q4 did not find evidence for a second, longer variant. The
  spec's Sizes subsection gives the full reasoning.
- **`pairs_with: []`.** No pm-skills skill addresses the type, checked against `tools/known-skills.txt` on
  2026-10-16.
- **The catalog entry's aliases, owner, and named-source fields need correction on landing**, per
  [procedure 1](../decision-procedures.md#1-a-catalog-call-loses-to-research). Both
  aliases change: "positioning map" is dropped, and "positioning framework (Geoffrey Moore)" loses its
  unverified attribution. **The owner becomes `PMM / PM`, by the maintainer's ruling of 2026-10-17.** `PMM`
  is sourced, but the sources split on ownership, so the catalog records both camps. The guide shows both
  camps with their sources, and labels its suggested default as this library's own reasoning, never as a
  sourced finding. The spec states each correction and the evidence behind it.
- **The bundle stays subject to ADR 0030.** This decision removes the family objection only.

## More Information

- Family contract: [`strategy-docs`](../contracts/strategy-docs.md), adopted by
  [ADR 0027](0027-adopt-strategy-docs-family-contract.md), amended once already by
  [ADR 0070](0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md).
- The precedents for widening a membership test:
  [ADR 0060](0060-change-request-joins-delivery-docs.md),
  [ADR 0067](0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md), and
  [ADR 0070](0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md).
- The admission sweep and the maintainer's sitting decisions, in gitignored working files:
  `_local/research/2026-10-14_admission-sweep-6/family-question.md` and
  `_local/research/2026-10-15_spec-integration/sitting-answers/answers/d7.json` and `d8.json`.
- The follow-up research that raised confidence per the maintainer's own request, also gitignored:
  `_local/research/2026-10-15_sitting-followup/positioning.json`.
- The spec and the full admission evidence: `docs/internal/tier2-specs.md`, the `strategy-docs` (sixth
  member) section.
- **Build order.** Not yet set by the maintainer; this record does not propose one.
