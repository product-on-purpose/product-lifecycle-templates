---
status: proposed
date: 2026-10-12
decision-makers: [jprisant]
consulted: [claude]
---

# `north-star-metrics` joins `strategy-docs` as a fifth member, placed second in the chain

## TL;DR

- **Decision.** The catalog candidate `north-star-metric-definition` is built as the bundle **`north-star-metrics`**.
  It declares **`family: strategy-docs`** and **`classification: foundation`**, and the
  [contract](../contracts/strategy-docs.md) moves to `0.2.0`. Section 1's members now answer five questions, not
  four. The North Star metric is the second, between the product vision and the product strategy.
- **Why an amendment.** The contract's membership sentence admits the type on its face: a North Star metric "sets or
  tracks product direction above the level of any single deliverable". What blocked it was the closed list of four
  questions that follows the sentence. This is the third admission to widen a contract, after
  [ADR 0060 (change-request joins delivery-docs)](0060-change-request-joins-delivery-docs.md) and
  [ADR 0067 (tracking-plan joins governance-docs)](0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md).
- **Why build it, given the overlap with `kpi-dashboard`.** A headline metric's formula, scope and exclusions already
  ship in `kpi-dashboard`'s Metric Definitions section. The case for choosing the metric, and the input metrics that
  drive it, ship nowhere in the library. This bundle owns those two, and routes the operational formula to
  `kpi-dashboard`.
- **What this does not decide.** The bundle's section design, which its spec and research settle. The example's North
  Star, which cannot be "Time to Insight" for reasons the spec gives. Whether the three existing companions that never
  mention a North Star gain a line: they do not, and this record states the gap.
- **Status:** proposed 2026-10-12. The maintainer chose the route, the chain position, the sizes, the boundary and the
  companion question on 2026-10-12. The record is held until the maintainer reads the contract diff, because a family
  contract is "adopted only after a maintainer read"
  ([decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer)).

## Context and Problem Statement

The `strategy-docs` chain runs from a product vision to a product strategy, a roadmap and OKRs. None of the four names
the single measure of customer value that shows the product is moving toward its vision. Two shipped companions
already point at that measure from outside the chain:

- `product-vision_companion.md:271-273` separates the "north star" metaphor from the **North Star Metric** artifact,
  citing Tim Herbig's description of the metric as "the quantified sibling of the Product Vision".
- `kpi-dashboard_companion.md:185` names the North Star Metric as one way to frame a dashboard's headline value metric.

The shared Acme Analytics scenario shows the same gap. "Time to Insight" acts as the headline metric in the `okrs`,
`kpi-dashboard`, `product-strategy` and `product-vision` examples, and no example calls it a North Star.

**Admission.** A research pass on 2026-10-05 tested the type against
[ADR 0030](0030-templating-scope-markdown-documents.md)'s admission test. One named publisher, Amplitude, ships the
type as a written document in two of its own publications. "The North Star Playbook" says: "When you define the
metric, you complete this template: Our North Star Metric is called X, which we define as Y." Amplitude's workshop
guide carries blank fields, among them "What's your product's North Star?" and rows for input metrics. Both quotations
were checked against the raw text of the live documents.
[ADR 0048](0048-one-named-source-clears-the-admission-test.md) holds that one named source clears the test.

**The admission rests on one publisher, and a second read did not change that.** On 2026-10-12, Reforge's North Star
Metric artifact page was read in a browser, because a plain fetch returns only the word "Reforge". The page lists two
member-submitted documents: one cascades goal targets through a leadership team, and one is a brand concept document.
Neither is a North Star metric template, and the page shows no field names. Other sources the pass read, among them
Mixpanel, Herbig and Sean Ellis, explain the practice without publishing a document of their own.

**Licence.** Both Amplitude documents are all rights reserved. The bundle needs its own field names and its own
layout, not a copy of Amplitude's worksheet, its sidebar heuristics or its worked examples.

## Decision Drivers

- The membership test, not the list of members planned at adoption, governs a candidate.
  [ADR 0050](0050-qa-docs-admits-a-fourth-member.md) established that reading.
- **A widening must be the smallest honest one.** ADR 0060 set the standard: widen the one family whose chain already
  carries the type's job, by the fewest words, and say so in the record.
- A family declares `phase` or `classification`, never both
  ([ADR 0015](0015-second-taxonomy-axis-phase-xor-classification.md)). The type's cadence decides its axis before
  anything decides its family.
- A family's teaching value is the relationship between its members. A new member must make that map clearer.

## Considered Options

1. **`strategy-docs`, `classification: foundation`, as a fifth member, with the list of questions widened.** Chosen.
2. **`standing-standards`, as written.** Rejected. The contract's test, "agreed once and applied every time", fits the
   surface: a North Star metric is agreed once and consulted repeatedly. But every member of that family is either a
   bar an increment is judged against or a procedure that is executed. A North Star metric is neither. It would be that
   family's only member about product direction, and it would sit in a different family from the vision, strategy and
   OKRs it relates to.
3. **`governance-docs`.** Rejected. Its test admits "a continuously-maintained register, log, or dashboard", at
   `classification: utility` only. A North Star metric is chosen, argued and revisited when the strategy shifts, which
   is the `foundation` shape. It also does not "specify what the product records", the clause
   [ADR 0067](0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md) added: it names a metric, and a tracking
   plan specifies the events the metric is computed from.
4. **A new family for this one type.** Rejected. It would write a contract no second candidate tests. The
   `experimentation-docs` contract also excludes this shape: "A standing measurement instrument is not a member,
   however closely it serves experiments."
5. **Decline, in the shape of [ADR 0064](0064-deployment-plan-is-declined.md) and
   [ADR 0065](0065-steering-committee-pack-is-declined.md).** Rejected. The duplication with `kpi-dashboard` covers the
   formula only. The case for the metric and its input metrics ship in no bundle, and Amplitude's workshop guide
   evidences both as blank fields.

## Decision Outcome

**Chosen: `strategy-docs`, `classification: foundation`, fifth member, placed second in the chain.**

### Why it fits, positively

1. **The membership sentence fits as written.** A North Star metric is the one number a product organization steers
   by, and it sits above every deliverable.
2. **The axis needs no change.** The contract already gates the set `foundation` or `utility`, and its own distinction
   is "argued-and-durable versus maintained-and-periodic". Amplitude says to revisit the metric "whenever there's a
   significant shift in your product, market, or business strategy". Mixpanel says companies should "reevaluate their
   North Star metrics to make sure they still point the right direction". Neither describes a calendar reset, which is
   the OKR shape. So the type is `foundation`, beside the vision and the strategy, and check K's registry entry needs
   no edit.
3. **The shared scenario already has a slot for its example.** Contract section 4 requires every member's example to
   be an Acme Analytics artifact, and the scenario has a headline metric that no document has yet named as its North
   Star.

### Where it sits in the chain, and why

**Second, between the product vision and the product strategy.** Tim Herbig gives this order: "North Star Metrics
are persistent goals that influence Product Strategy", whereas "OKRs are point-in-time goals that implement that
Strategy".

**The order is contested, and the build's research found it so after the choice was made.** On sequence, Adam Farren
describes the opposite: vision, then strategy, then goals, and only then the question "So how do you bring all of that
- vision, strategy, tactics - into alignment?", which a North Star answers. On dependency, Amplitude, Swiss Post, Spotify's Confidence glossary and Umbrex
each describe the North Star as measuring the current strategy, and Amplitude and Umbrex tie a change of North Star to
a change of strategy. No source places it third, between the strategy and the roadmap, as a sequence. Every source
that relates it to OKRs puts it above them. The spec's "The chain position is contested" subsection quotes each camp.

**The chain link is the library's POSITION, whichever order stands.** It is labelled so under
[procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world). No source read states
the failure that link names as a documented real-world failure.

### What widens, and by how much

- **Section 1's list.** "four questions" becomes "five questions", and a new second bullet names the North Star
  metric's question.
- **Section 1's chain sentence** gains one link, labelled POSITION.
- **Section 1's relationship obligation.** "against the other three" becomes "against the other members".
- **Section 2.** The classification row and the axis note name the North Star metric as `foundation`. The
  methodology row names it as methodology-bound, beside `okrs`.
- **Section 4.** The shared-scenario obligation gains the North Star metric's example.

The membership sentence, the axis set, the structural obligations and the enforcement section are unchanged.

### Consequences

- **The contract moves to `0.2.0`.** Its header gains a Members line, and a dated change note records the widening.
- **The bundle id is plural, and the catalog id is unchanged.** The maintainer ruled on 2026-10-11 that the bundle is
  `north-star-metrics`, while catalog entry 8 stays `north-star-metric-definition`. The two differ in the shape
  [ADR 0061](0061-change-log-joins-governance-docs-as-a-fifth-member.md) set for `change-log`. The document still
  defines one North Star per product, with its input metrics beneath it. Amplitude: "An obvious characteristic of the
  North Star Framework is that there's only one North Star Metric." The spec answers the plural in advance, so that a
  review lens does not file it as a defect.
- **Three existing companions fall short of the relationship obligation's letter.** `product-vision`'s companion
  already has its "Versus north star" paragraph. The `product-strategy`, `product-roadmap` and `okrs` companions never
  mention a North Star, and none of them gains a line. This follows the precedent of ADR 0067 and
  [ADR 0069](0069-problem-statement-joins-discovery-docs.md), whose amendments swept no existing member's companion.
  The new member states its position against all four existing members.
- **The boundary with `kpi-dashboard` is a division of content.** This bundle carries one statement line naming the
  metric and what it measures. The operational formula, scope, exclusions and known limitations stay in
  `kpi-dashboard`'s Metric Definitions section, and the templates route there.
- **Sizes: lean and full, under the rule the maintainer set for `problem-statement`.** Every full-only section must
  rest on a source the build reads. If the research cannot support a full variant, the build stops and reports rather
  than padding one.
- **`pairs_with: []`.** No pm-skills skill addresses the type.
- **The catalog entry's methodology may need correction on landing**, per
  [procedure 1](../decision-procedures.md#1-a-catalog-call-loses-to-research). It reads "growth/OKR", and the research
  found no source placing the North Star metric inside the OKR method.
- **The bundle stays subject to ADR 0030.** This decision removes the family objection only.

## More Information

- Family contract: [`strategy-docs`](../contracts/strategy-docs.md), adopted by
  [ADR 0027](0027-adopt-strategy-docs-family-contract.md). This is its first amendment of substance; its 0.1.1 change
  was a relabelling under procedure 11.
- The precedents for widening a membership test: [ADR 0060](0060-change-request-joins-delivery-docs.md) and
  [ADR 0067](0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md).
- The spec and the admission evidence: [`tier2-specs.md`](../tier2-specs.md#strategy-docs-fifth-member-by-amendment-north-star-metrics),
  the `strategy-docs` (fifth member) section.
- **Build order.** The maintainer queued the type on 2026-10-08 to follow `tracking-plan`, and approved starting it on
  2026-10-11.
