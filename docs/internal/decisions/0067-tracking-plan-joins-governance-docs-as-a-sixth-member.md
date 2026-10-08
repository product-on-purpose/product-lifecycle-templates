---
status: accepted
date: 2026-10-06
decision-makers: [jprisant]
consulted: [claude]
---

# `tracking-plan` joins `governance-docs` as a sixth member, and the membership test's purpose phrase widens

## TL;DR

- **Decision.** The `tracking-plan` catalog candidate declares **`family: governance-docs`** and
  **`classification: utility`**. It becomes that family's sixth member, alongside `risk-register`, `raid-log`,
  `kpi-dashboard`, `issue-log` and `change-log`, and the [contract](../contracts/governance-docs.md) moves to
  `0.4.0`.
- **Why this record is different from ADR 0057 and ADR 0061.** Those records admitted a type the membership test
  already named. This one does not fit as written. The test admits an instrument "that a product or program manager
  uses to track risk, open items, or performance". A tracking plan specifies what the product records, so that
  performance can be tracked; it does not itself track performance. **Admitting it widens the test's purpose phrase**,
  which is a contract change in substance. It is the second admission to widen a test, after
  [ADR 0060 (change-request joins delivery-docs)](0060-change-request-joins-delivery-docs.md).
- **What settled it.** The rest of the test fits. A tracking plan is a register of events, and the vendor sources
  describe it as maintained for the product's whole life. Amplitude calls it "a living document". The
  `standing-standards` contract routes exactly this cadence to `governance-docs` or `strategy-docs`. The new
  `experimentation-docs` family excludes it in its own boundary sentence, because a standing instrument is never
  finished.
- **What this does NOT decide:** admission, which retrieval settled on five named vendors (see
  [`tier2-specs.md`](../tier2-specs.md)); and two neighbours the research named but this record does not place: the
  per-feature measurement plan (catalog id `analytics-requirements-measurement-plan`) and the data dictionary.
- **Status:** accepted 2026-10-08. The record was proposed 2026-10-06 and held until the maintainer read the
  contract diff, as ADR 0060 was, because a family contract is "adopted only after a maintainer read"
  ([decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer)).

## Context and Problem Statement

The shipped library already names the tracking plan, from inside another document. The PRD's full template asks for an
"Analytics and instrumentation" section, and its guidance says: "if the tracking plan is not in the PRD, the launch
usually cannot measure its own success criteria" (`prd_template-full.md:213-214`; the companion repeats it at
`prd_companion.md:66`). That sentence treats a feature's slice of tracking as part of the PRD. No shipped bundle
covers the product-wide plan that those slices add up to.

A research pass on 2026-10-05 tested the type against ADR 0030's admission test and against all nine family contracts,
with a draft of the `experimentation-docs` contract as a tenth. Five named vendors publish the tracking plan as a
written document and ship a template for it: Avo, Twilio Segment, Mixpanel, Amplitude and mParticle. Twilio Segment
defines it as "a document or spreadsheet used across an organization to standardize how it tracks data". Avo
describes its plan as definitions "that can be used to generate code from and validate your data against". The
library's own POSITION is that the written plan is the primary form and a schema enforced inside a tool derives from
it, which is what ADR 0030 requires of a templated type.

No contract admitted it as written. `governance-docs` came closest, failing on one phrase only.

## Decision Drivers

- The membership test, not the list of members planned at adoption, governs a candidate. ADR 0050 (qa-docs admits a
  fourth member) established that reading, and ADR 0057 confirmed it for this family.
- **A widening must be the smallest honest one.** ADR 0060 set the standard: widen the one family whose chain already
  carries the type's job, by the fewest words, and say so in the record rather than reading the type in.
- A family declares `phase` or `classification`, never both
  ([ADR 0015](0015-second-taxonomy-axis-phase-xor-classification.md)). The type's cadence decides its axis before
  anything decides its family.
- The family's teaching value is the relationship between its instruments. A new member must make that map clearer,
  not muddier.

## Considered Options

1. **`governance-docs`, `classification: utility`, as a sixth member, widening the purpose phrase.** Chosen.
2. **`experimentation-docs`, as the third member the July 2026 plan proposed.** Rejected. That family is
   `phase: measure`, and its members are finished when a test's decision is recorded. A tracking plan is never
   finished, and the contract's own boundary sentence excludes "a standing measurement instrument". Admitting it would
   need the family to declare both axes, which ADR 0015 forbids.
3. **`standing-standards`.** Rejected by that contract's routing sentence: "A candidate revised on a cadence and
   valuable only while current is `utility` and belongs to `governance-docs` or `strategy-docs`." A tracking plan
   gains events with every feature; it is not agreed once and applied every time.
4. **`delivery-docs`, as a per-feature instrumentation plan.** Rejected. A per-feature plan is a different catalog
   candidate, `analytics-requirements-measurement-plan`, and its content already ships inside the PRD's "Analytics and
   instrumentation" section. The type this record places is the standing, product-wide plan.
5. **A new `classification` family for measurement instruments.** Rejected on the grounds ADR 0060 gave for the
   parallel option: more machinery for one type, when an existing contract fails on one phrase.
6. **No bundle: the PRD section is the tracking plan.** Rejected, as the library's own POSITION, since no source in the
   research addresses this boundary. The PRD section records one feature's events at one moment. A product-wide plan
   accumulates every feature's events, and the vendor sources describe it as versioned and maintained. The PRD
   sentence quoted above is read here as the feature's slice of that plan.

## Decision Outcome

**Chosen: `governance-docs`, `classification: utility`, sixth member, with the purpose phrase widened.**

### Why it fits, positively

1. **The noun and the cadence already fit.** `governance-docs` section 1 admits "a continuously-maintained register,
   log, or dashboard", used "across the whole lifecycle", and "set up once and maintained indefinitely". A tracking plan
   is a register of events and their properties, kept for the life of the product.
2. **`utility` is the only value the contract allows, and it is the right one.** The contract defines `utility` as "a
   standing operational instrument", distinct from "a `tool` that is executed procedurally".
3. **It deepens the family's map rather than adding an axis to it.** The KPI dashboard defines the metrics the family
   tracks against targets. A tracking plan defines the events those metrics are computed from. It stands upstream of
   the dashboard, as the change log stands behind the change requests it records. This relationship is the library's
   own POSITION.

### What widens, and by how much

Only the purpose phrase changes. The phrase "uses to track risk, open items, or performance" gains one clause, "or
to specify what the product records so that performance can be tracked", and no existing word changes. The register, log or dashboard noun, the lifecycle scope and the maintained-indefinitely
cadence are unchanged, so the widening admits no document that is produced once and finished.

### Consequences

- **The contract moves to `0.4.0`.** Its Members line records a sixth member, the roles list gains a sixth bullet and
  becomes "The six roles", the purpose phrase widens, and a dated change note records all three. No structural
  obligation changes, and check K's registry entry needs no edit, because it gates values rather than a member count.
- **The relationship obligation grows by one edge per member.** The new companion states its position against all five
  existing members, per contract section 1.
- **The PRD boundary is a POSITION, and the build must say so.** No source in the research addresses how a PRD's
  analytics section relates to a standing tracking plan, so the companion presents that boundary as the library's own
  reasoning. Whether the PRD's guidance gains a pointer to the new bundle is a build decision, not one this record
  settles.
- **The catalog entry may need correction on landing**, per
  [procedure 1](../decision-procedures.md#1-a-catalog-call-loses-to-research). The research questioned the `owner` and
  `stage` fields; the spec states which corrections the evidence supports.
- **`pairs_with: []`.** No pairing is claimed.
- **The bundle id is `tracking-plan`, the catalog id unchanged.**
- **The bundle stays subject to ADR 0030.** This decision removes the family objection only, as ADR 0057 and ADR 0061
  stated for their own admissions.

## More Information

- Family contract: [`governance-docs`](../contracts/governance-docs.md), adopted by
  [ADR 0024](0024-adopt-governance-docs-family-contract.md); the previous amendment was
  [ADR 0061 (change-log joins governance-docs as a fifth member)](0061-change-log-joins-governance-docs-as-a-fifth-member.md).
- The precedent for widening a membership test: [ADR 0060](0060-change-request-joins-delivery-docs.md).
- The sibling record from the same research:
  [ADR 0066 (adopt the experimentation-docs family contract)](0066-adopt-experimentation-docs-family-contract.md),
  whose contract excludes standing measurement instruments.
- The spec and the admission evidence: [`tier2-specs.md`](../tier2-specs.md#governance-docs-sixth-member-by-amendment-the-tracking-plan),
  the `governance-docs` (sixth member) section.
- **Build order.** The maintainer ruled on 2026-10-06 that this bundle is built after the two experimentation-docs
  members.
