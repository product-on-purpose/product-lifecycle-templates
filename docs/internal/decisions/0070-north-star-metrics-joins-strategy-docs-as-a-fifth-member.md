---
status: accepted
date: 2026-10-12
decision-makers: [jprisant]
consulted: [claude]
---

# `north-star-metrics` joins `strategy-docs` as a fifth member, placed third in the chain

## TL;DR

- **Decision.** The catalog candidate `north-star-metric-definition` is built as the bundle **`north-star-metrics`**.
  It declares **`family: strategy-docs`** and **`classification: foundation`**, and the
  [contract](../contracts/strategy-docs.md) moves to `0.2.0`. Section 1's members now answer five questions, not
  four. The North Star metric is the third, between the product strategy and the product roadmap. That place
  is inferred from what the metric depends on, and no source states it as a sequence.
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
- **Status:** accepted 2026-10-12, on the maintainer's delegation. The maintainer chose the route, the sizes, the
  boundary and the companion question on 2026-10-12. The chain position was chosen as second earlier that day and
  moved to third the same day, when the maintainer accepted the recommendation that followed the build's research.
  A family contract is "adopted only after a maintainer read"
  ([decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer)). Told that the read
  was the next stop, the maintainer twice replied "Continue based on your best recommendations". That direction
  stands in for the read, as it did for [ADR 0069](0069-problem-statement-joins-discovery-docs.md). The agent
  checked the contract diff against each of the maintainer's decisions and found nothing they do not cover.
  **Confirmed by the maintainer on 2026-10-21**, in one batch covering ADRs 0070, 0074,
  0075, 0076 and 0078. Offered the choice to confirm all five, to reopen any of them for a read, or
  to leave the question parked, the maintainer confirmed all five.
  *(Note added 2026-10-19: [ADR 0076](0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md)
  places `positioning-statement` between the product strategy and the North Star metric, so the North Star
  metric is now fourth in the chain, not third. It still follows the strategy, which is the dependency this
  record argued; only its number changed.)*

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

**Chosen: `strategy-docs`, `classification: foundation`, fifth member, placed third in the chain.**

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

**Third, between the product strategy and the product roadmap.** The position is inferred from what a North Star
depends on. Four publishers describe it as measuring the current strategy:

- Amplitude asks for "A metric that serves as a key measure of your current product strategy".
- Swiss Post: "It represents the core of the product strategy."
- Spotify's Confidence glossary: "The north star should reflect the current strategic question".
- Umbrex: "Only change the NSM when strategy or product fundamentally shifts".

This library's reasoning is that a measure of the strategy cannot come before the strategy it measures. Every
source that relates the North Star to OKRs puts it above them, and third place keeps that.

**No source states this sequence, and the two sources that state a sequence disagree with each other.** Tim Herbig
puts the North Star first: "...first defining your North Star Metric, then articulating a Strategy and finally
establishing OKRs ensures each gets the attention it deserves." Adam Farren puts it after the vision, the strategy
and the goals, as the answer to "So how do you bring all of that - vision, strategy, tactics - into alignment?" The
spec's "The chain position is contested" subsection quotes each camp, and the companion names both.

**The position changed once, on the day it was decided.** The maintainer first chose second place, between the
vision and the strategy, on Herbig's order. The recommendation behind that choice said Herbig's was the only order a
source supported. The build's research, run the same day, showed that premise was wrong. Re-presented with the
evidence above, the maintainer accepted the recommendation of third place, which was given at low confidence. A
reader who holds that a North Star should outlast any one strategy has Herbig on their side. Second place remains
the considered alternative.

**The chain link is the library's POSITION, whichever order stands.** It is labelled so under
[procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world). No source read states
the failure that link names as a documented real-world failure.

### What widens, and by how much

- **Section 1's list.** "four questions" becomes "five questions", and a new third bullet names the North Star
  metric's question. The roadmap bullet's "work on them" becomes "work on those problems", because the new bullet
  now sits between it and the strategy.
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
- **The example sits between the strategy's example and the roadmap's.** It is dated after the product strategy
  example (2026-01-28) and before the product roadmap example (2026-02-11). It must reconcile with the leading
  indicator the strategy example already names.
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
