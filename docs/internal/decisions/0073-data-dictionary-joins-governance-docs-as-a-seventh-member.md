---
status: proposed
date: 2026-10-15
decision-makers: [jprisant]
consulted: [claude]
---

# `data-dictionary` joins `governance-docs` as a seventh member, scoped to what a dataset's fields mean

## TL;DR

- **Decision.** The catalog candidate `data-dictionary` (issue #255, bundle: data-dictionary) declares
  **`family: governance-docs`** and **`classification: utility`**. It becomes that family's seventh
  member, alongside `risk-register`, `raid-log`, `kpi-dashboard`, `issue-log`, `change-log` and
  `tracking-plan`, and the [contract](../contracts/governance-docs.md) moves to
  `0.5.0`.
- **The scope is narrow, by the maintainer's own ruling.** This bundle documents what the fields of a
  dataset or table mean. It excludes, by name, event cataloguing (the tracking plan's job, ADR 0067:
  tracking-plan joins governance-docs as a sixth member) and metric-formula locking (the KPI dashboard's
  own Metric Definitions section).
- **Why this record differs from ADR 0067, on the boundary's own basis.** ADR 0067 widened the family's
  purpose phrase on cadence: a tracking plan is a register, maintained indefinitely, that does not itself
  track performance. This record widens the same phrase a second time, but the boundary it draws against
  the tracking plan rests on subject, not on timing. See the boundary subsection below.
- **What changed since the maintainer's own sitting answer of 2026-10-13.** The sitting approved a
  tense-based scope condition: a tracking plan says what will be recorded, a data dictionary says what
  recorded data means. Research run the next day found that line contested. This record replaces it with
  a subject-based line and says so plainly, rather than let the maintainer discover the change unlabeled
  in a diff.
- **Status:** proposed 2026-10-15. Held for the maintainer's read of the contract diff and this record,
  as every family contract amendment stops for that read
  ([decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer)).

## Context and Problem Statement

A 2026-10-12 admission sweep of five queued candidates tested `data-dictionary` against
[ADR 0030 (templating scope: Markdown documents)](0030-templating-scope-markdown-documents.md)
and against all ten family contracts. Admission cleared easily: Amplitude calls a data dictionary "a
document that lays out the project's taxonomy," and Docsie ships a downloadable template, "completely
free to download in Word (DOCX), PDF, and Markdown formats." Several more sources corroborate (see the
spec's Admission section). No contract admitted the type as written. `governance-docs` came closest,
because its sixth member, `tracking-plan`, already names the data dictionary as a neighbour it does not
cover: "What the warehouse tables mean once these events reach them is the data dictionary's job"
(`templates/tracking-plan/tracking-plan_template-lean.md`, the Purpose and Boundary section's GOOD text).
[ADR 0067 (tracking-plan joins governance-docs as a sixth member)](0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md)
itself named this gap and declined to close it: "two neighbours the research named but this record does
not place: the per-feature measurement plan... and the data dictionary."

**The maintainer's sitting answered the placement question on 2026-10-13, on a tense-based scope
condition.** The recommendation presented to the sitting read the tracking-plan/data-dictionary boundary
as a matter of when each document is written: a tracking plan says what will be recorded, a data
dictionary says what already-recorded data means, each citing Wizbrand's own account, "A tracking plan
describes what you intend to track," against "A Data Dictionary documents what the data means and how it
is structured once implemented." The maintainer approved an amendment carrying that condition ("Amend
with the scope condition") and, after a chat follow-up resolved an inconsistency with the build answer,
approved the build itself at the narrow scope ("Build, narrow scope"). One open item from that sitting,
logged under "Confidence work for data-dictionary," asked for a second, independent source on the tense
line before the record was written, because Wizbrand was the only source for it.

**Research run on 2026-10-14 answered that open item, and the tense line did not hold.** Two independent
passes looked for a second source on the tense boundary, excluding Wizbrand. They found that sources
split on timing. The US National Institute of Mental Health's own grant-management guidance treats a
"data dictionary" as a forward-looking instrument: it names "data collection instruments (also known as
data dictionaries)" that hold "data structures that awardees are expected to use for new data collection."
Temple University Libraries defines one the same way, as "a record of each variable and data field that
you are going to collect in your project." Against that, CASRAI's research-data-management guide defines
a data dictionary as a document that explains a dataset's variables "so that anyone other than the person
who collected the data can interpret it correctly," which presupposes the data already exists. Buchanan et
al. (2021), in a peer-reviewed workflow tutorial, places the data dictionary at the end of "the entire
process from source data... to an openly shared dataset accompanied by a data dictionary or codebook."
Nazabal et al. (2020) and Phillips et al. (2024) each describe building a data dictionary from data a team
already has, the latter placing it last in a ten-step pipeline, after collection, cleaning and quality
assurance. **The sources agree on subject, not on timing.** Every source above, on either side of the
timing question, names the same thing as what a data dictionary defines: the variables or fields of a
dataset. None of them describes a data dictionary as specifying the events and properties a product will
emit, which is what every tracking-plan source (Avo, Twilio Segment, Amplitude, Mixpanel, mParticle)
describes a tracking plan as doing instead. NIMH and Temple write a dictionary before collection; CASRAI
and Buchanan et al. write one after; so timing is no part of this boundary.

## Decision Drivers

- The membership test, not the list of members planned at adoption, governs a candidate. ADR 0050
  (qa-docs admits a fourth member) established that reading, and ADR 0057, ADR 0061, ADR 0067 and ADR 0070
  each confirmed it for a widening.
- **A widening must be the smallest honest one**, and it must rest on the boundary the research actually
  supports, not the one a prior sitting approved before that research ran. ADR 0060 set the standard for
  the smallest honest widening; this record adds that the boundary itself must survive a second look.
- A family declares `phase` or `classification`, never both
  ([ADR 0015](0015-second-taxonomy-axis-phase-xor-classification.md)). The type's cadence decides its axis
  before anything decides its family.
- The family's teaching value is the relationship between its instruments. A seventh member must make
  that map clearer, not muddier, and must not quietly readmit the event-and-metric content two shipped
  bundles already carry.

## Considered Options

1. **`governance-docs`, `classification: utility`, as a seventh member, widening the purpose phrase a
   second time, on subject.** Chosen.
2. **`governance-docs`, on the tense-based scope condition the sitting approved 2026-10-13.** Rejected.
   The 2026-10-14 research found the tense line contested by primary and peer-reviewed sources on both
   sides; a widening that rests on a line two of the six sources contradict is not the smallest honest one
   available once a sounder line exists.
3. **No amendment: build to the catalog's own wider framing (its purpose field, "Document the meaning
   and usage of events and metrics").** Rejected on duplication. The catalog's own purpose field and two vendor sources (Wizbrand's
   calculation-logic language and Basedash's metric field) describe a metrics half that duplicates
   `kpi-dashboard`'s own shipped Metric Definitions section: formula, inclusions and exclusions, owner, and
   data steward. A bundle built to that framing would re-ship content from two families at once.
4. **Decline, in the shape of [ADR 0064 (deployment-plan declined)](0064-deployment-plan-is-declined.md)
   and [ADR 0065 (steering-committee pack declined)](0065-steering-committee-pack-is-declined.md).**
   Rejected on the evidence: that shape needs zero qualifying sources, and this type clears admission on
   several. `tracking-plan`'s own shipped text names an unfilled gap rather than claiming to fill it, which
   is a weaker case for decline than either precedent had.
5. **A new `classification` family for data-meaning documents.** Rejected on the grounds ADR 0060 and ADR
   0067 both gave for the parallel option: more machinery for one type, when an existing contract fails on
   one phrase.

## Decision Outcome

**Chosen: `governance-docs`, `classification: utility`, seventh member, with the purpose phrase widened a
second time, on subject.**

### Why it fits, positively

1. **The noun and the cadence already fit, exactly as they did for `tracking-plan`.** `governance-docs`
   section 1 admits "a continuously-maintained register, log, or dashboard," used "across the whole
   lifecycle" and "set up once and maintained indefinitely." A data dictionary is a reference document that
   is revised as a schema changes, not authored once and archived. Basedash states the maintenance
   obligation directly: "Update definitions whenever the schema changes, as part of the change itself
   rather than as a separate task," and Wizbrand states a review cadence, "review it on a cadence (monthly
   or quarterly)."
2. **`utility` is the only value the contract allows, and it is the right one.** The contract defines
   `utility` as "a standing operational instrument," distinct from "a `tool` that is executed
   procedurally." A data dictionary is consulted repeatedly by whoever needs to know what a field means; it
   is not executed under time pressure the way a runbook or a business continuity plan is.
3. **It deepens the family's map rather than adding an axis to it.** The tracking plan specifies the
   events and properties a product emits. The KPI dashboard's Metric Definitions section locks one
   dashboard's metric formulas. The data dictionary documents what the fields of a dataset or table mean,
   so that different teams compute the same number from them. Wizbrand names exactly this failure mode
   without the document: "Fewer metric disputes and fewer... two versions of the truth."

### The boundary changed since the sitting, and why

**What the sitting approved, 2026-10-13.** The record presented for approval drew the line against
`tracking-plan` on tense: forward-looking for the tracking plan, backward-looking for the data dictionary,
on Wizbrand's own account. The maintainer approved the amendment on that basis and, after a same-day chat
exchange, approved the build at narrow scope.

**What the 2026-10-14 research found.** A targeted search for a second, independent source on that tense
line, run specifically because the sitting's own open item asked for one, found the line contested rather
than confirmed. The US National Institute of Mental Health and Temple University Libraries both use "data
dictionary" for a forward-looking collection instrument. CASRAI, Buchanan et al. (2021), Nazabal et al.
(2020) and Phillips et al. (2024) all describe one written from data a team already holds. Both camps
include sources with no connection to Wizbrand or to each other's lineage, so this is not one contested
source; it is a genuine split in how the term is used across research-data-management and data-engineering
writing.

**What replaces it, and why.** Every source above, regardless of which side of the timing question it
takes, agrees that a data dictionary defines the variables or fields of a dataset. No source on either side
describes a data dictionary as specifying the events and properties a product will emit; every
tracking-plan source describes the tracking plan as doing exactly that. The boundary this record draws is
therefore on **subject**: a tracking plan specifies the events and properties a product emits; a data
dictionary documents what the fields of a dataset or table mean. Timing is not part of either definition.
This is a sounder basis for the same narrow scope the sitting already chose, not a reopening of the scope
decision itself. The maintainer's "Build, narrow scope" answer stands; only the reason the narrow scope is
correct has changed.

**Why this is recorded here, plainly, rather than folded into the spec alone.** The maintainer approved a
specific argument on 2026-10-13. That argument no longer holds as stated. A maintainer reading only the
contract diff and the spec would see a narrow-scope bundle that matches what they approved, with no sign
that the reasoning underneath it moved. This paragraph exists so the maintainer reads this as a change from
what they approved, not as a diff that happens to agree with their decision for reasons they were never
shown.

### What widens, and by how much

Only the purpose phrase changes, a second time. The phrase, after ADR 0067's first widening, reads "...or
to specify what the product records so that performance can be tracked." It gains a second clause, "or to
document what the fields of a dataset or table mean, so that different teams compute the same number from
them," and no existing word changes. The register, log or dashboard noun, the lifecycle scope and the
maintained-indefinitely cadence are unchanged, so this widening, like ADR 0067's, admits no document that
is produced once and finished.

### Consequences

- **The contract moves to `0.5.0`.** Its Members line records a seventh member, the roles list gains a
  seventh bullet and becomes "The seven roles," the purpose phrase widens a second time, and a dated
  change note records all three, mirroring ADR 0067's own change note.
- **The relationship obligation grows by one edge per member.** The new companion states its position
  against all six existing members, per contract section 1.
- **Product-analytics usage of the term is wider than this bundle, and the spec must route around it.**
  Mixpanel's own documentation states "Lexicon is a data dictionary that stores descriptions of events and
  their properties," and the same page imports Segment, Avo and mParticle tracking plans directly into that
  "data dictionary." A reader who works in product analytics and types "data dictionary" often means the
  event list this library already ships as `tracking-plan`. The spec's Boundaries section and its catalog
  corrections address this; whether `tracking-plan` should gain an alias such as "event dictionary" is a
  build-time recommendation this record does not settle on its own authority.
- **The catalog entry needs correction on landing**, per
  [decision-procedures.md procedure 1](../decision-procedures.md#1-a-catalog-call-loses-to-research).
  The spec states which corrections the evidence supports.
- **`pairs_with: []`.** Checked against pm-skills `origin/main` on 2026-10-14 (68 skill names); none names a
  data dictionary, a glossary, or a catalog.
- **The bundle id is `data-dictionary`, the same as the catalog id.**
- **The bundle stays subject to ADR 0030.** This decision removes the family objection only, as ADR 0057,
  ADR 0061, ADR 0067 and ADR 0070 each stated for their own admissions.
- **A stop rule governs the build**, stated in full in the spec: if the worked example's field-level
  dictionary reads as thin, or reads as a document for a data team rather than a product manager, the build
  stops and the decline alternative (Considered Option 4, above) returns to the maintainer.

## More Information

- Family contract: [`governance-docs`](../contracts/governance-docs.md), adopted by
  [ADR 0024](0024-adopt-governance-docs-family-contract.md); the previous amendment was
  [ADR 0067 (tracking-plan joins governance-docs as a sixth member)](0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md),
  this record's MODEL for structure and for how a widening is argued and recorded.
- The precedent for widening a membership test on cadence rather than subject:
  [ADR 0067](0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md). The precedent for widening a
  different family's list of questions: [ADR 0070 (north-star-metrics joins strategy-docs as a fifth
  member)](0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md).
- The refusal-record shape considered and not used:
  [ADR 0049 (pi-release-retrospective fails the admission test)](0049-pi-release-retrospective-fails-the-admission-test.md),
  and the duplication-ground refusals
  [ADR 0064](0064-deployment-plan-is-declined.md) and [ADR 0065](0065-steering-committee-pack-is-declined.md).
- The admission standard for new types:
  [ADR 0030 (templating scope: Markdown documents)](0030-templating-scope-markdown-documents.md), and
  [ADR 0048 (one named source clears the admission test)](0048-one-named-source-clears-the-admission-test.md).
- The spec, the admission evidence, the boundary argument in full, and the section design:
  [`tier2-specs.md`](../tier2-specs.md#governance-docs-seventh-member-by-amendment-the-data-dictionary-scoped-to-what-a-datasets-fields-mean).
- **Build order.** Not yet scheduled; this record and its contract diff stop for the maintainer's read
  before any build begins.
