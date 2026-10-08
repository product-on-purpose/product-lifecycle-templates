---
status: accepted
date: 2026-10-06
decision-makers: [jprisant]
consulted: [claude]
---

# Adopt the experimentation-docs family contract at `phase: measure`, with two founding members

## TL;DR

- **Decision.** Adopt [`docs/internal/contracts/experimentation-docs.md`](../contracts/experimentation-docs.md)
  (version 0.1.0), the tenth family contract, enforced by gate check K at **`phase: measure`**. Its two planned members
  are the catalog candidates `experiment-design-doc` and `experiment-readout-results-report`, which ship as **two
  bundles**: one plans a test of a hypothesis, and the other reports it. Their bundle ids, fixed in the spec, are
  `experiment-design-doc` and `experiment-readout`.
- **Why a new family.** A research pass on 2026-10-05 tested both types against all nine existing contracts. None
  admits either type as written, and each near-fit would have to be widened until it stopped constraining anything.
- **Why two bundles, not one.** The named sources split evenly between one merged experiment document and two separate
  documents. The maintainer ruled for two on 2026-10-06, following this library's own precedent: `qa-docs` ships
  `test-plan` and `test-summary-report` as separate bundles for the same before-and-after pair.
- **What this does NOT decide:** whether either type passes ADR 0030's admission test, which retrieval settles in the
  specs; the bundle ids, which the specs fix; and where any standing measurement instrument lives. The tracking plan,
  which the July 2026 plan proposed as a third member, joins `governance-docs` instead, by
  [ADR 0067 (tracking-plan joins governance-docs as a sixth member)](0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md).
- **Status:** accepted 2026-10-08. The record was proposed 2026-10-06 and held until the maintainer read the
  contract diff, as [ADR 0059](0059-announcement-internal-comms-joins-delivery-docs.md) and
  [ADR 0060](0060-change-request-joins-delivery-docs.md) were, because a family contract is "adopted only after a
  maintainer read" ([decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer)).

## Context and Problem Statement

The library's catalog carries a cluster of measurement documents, and none of them is built. On 2026-10-04 a ranking
of the product-management candidates found that the Analytics / Measurement category had one built bundle,
`kpi-dashboard`, against ten unbuilt candidates. The maintainer approved founding an experimentation family the same
day.

The idea is older than that approval. A July 2026 planning document, kept outside the repository, proposed an
"experimentation-docs" family of an experiment brief, an experiment review and an instrumentation plan. The
`governance-docs` contract had also anticipated the family when it refused `phase: measure` for the KPI dashboard: "If
a future measurement family with genuinely phase-bound members is built, that is where a phase-axis metrics artifact
would live" ([`governance-docs.md`](../contracts/governance-docs.md), section 2, the kpi-dashboard note).

A research pass on 2026-10-05 tested five measurement candidates against ADR 0030's admission test and against all
nine family contracts, with a draft of this contract as a tenth. Both experiment types cleared admission on several
named sources, including GrowthBook, LaunchDarkly, Optimizely, Amplitude, Eppo and the CONSORT 2010 statement. The
evidence is held in the specs in [`tier2-specs.md`](../tier2-specs.md). What it could not settle was the family.

Every new family gets a contract before its members are built, following the
[ADR 0020](0020-adopt-delivery-docs-family-contract.md) pattern, so that a member is born into an enforced family.
This record adopts that contract.

## Decision Drivers

- **The axis call must be honest, not convenient.** It is decided by what the two documents are, not by what keeps
  the family map tidy, as [ADR 0026 (adopt the qa-docs family contract)](0026-adopt-qa-docs-family-contract.md)
  required.
- **A membership test must constrain.** A family that admits anything with the word "experiment" in it would admit
  spike reports, retrospectives and experiment logs, and would teach nothing.
- **Contract-first, so membership is mechanical from the first member.**
- **The check should generalize, not grow machinery.** A tenth family should be one `FAMILY_CONTRACTS` entry and no new
  check code.
- **The family's teaching value is two boundaries.** The design doc partly overlaps the PRD's success metrics, and
  both members share vocabulary with the spike report and the QA test pair. A contract that does not force each member
  to place itself against those neighbours has skipped the reason a reader needs the family.

## Considered Options

- **Option A: adopt an experimentation-docs contract at `phase: measure`, with two members, methodology descriptive,
  examples chained onto the existing Saved Views thread, and enforcement through a new check K registry entry.**
  Chosen.
- **Option B: no new family; place the two types in an existing one.** Rejected, because each candidate home fails on
  its own membership test. `decision-docs` admits a technical decision or design, and a test of how users respond to a
  change is neither, although the spike report already shares its vocabulary. `qa-docs` verifies a product increment
  against an agreed specification, while an experiment tests an open hypothesis against a baseline. `process-docs`
  looks back on how a team worked or on a failure in production, not on whether a change worked. `delivery-docs`
  carries one unit of product work from definition to delivery. Admitting either type to any of these would widen a
  test until it stopped constraining, which is the failure contracts exist to prevent.
- **Option C: one member, a single experiment document with a results section filled in later.** Rejected by the
  maintainer on 2026-10-06. The merged form has real sources: Optimizely's Confluence template "Experiment plan and
  results", Adam Fishman's experiment document, and Amplitude's experiment brief. So does the separate form: GrowthBook,
  Eppo, the AsPredicted and OSF preregistration templates, CONSORT and HM Treasury's Magenta Book. With the evidence
  split, the library's own `qa-docs` precedent decides it, and two documents give each member a clean finish.
- **Option D: a `classification` family for experimentation.** Rejected. The `classification` axis describes a
  document set up once and maintained indefinitely. A design doc is finished when its test launches, and a readout is
  finished when its decision is recorded.
- **Option E: the July plan's trio, with the tracking plan as a third member.** Rejected. The vendor sources describe the
  tracking plan as a single source of truth maintained as the product changes, and Amplitude calls it "a living
  document". That is the `classification` behaviour. A family declares `phase` or `classification`, never both
  ([ADR 0015](0015-second-taxonomy-axis-phase-xor-classification.md)), so the trio cannot share one contract. The
  tracking plan goes to `governance-docs` by ADR 0067.
- **Option F: include the concept test brief.** Rejected for now. It is a test run before anything is built, to
  decide whether to build it, and its admission evidence is contested. The maintainer parked it on 2026-10-06, and
  this contract states the exclusion without placing the type anywhere.

## Decision Outcome

**Adopt [docs/internal/contracts/experimentation-docs.md](../contracts/experimentation-docs.md) (version 0.1.0),
enforced by the existing gate check K through a new `FAMILY_CONTRACTS` entry keyed on `phase`.** For every bundle
declaring `family: experimentation-docs`, check K requires `phase: measure`, a `beta` or `stable` status, a size shape
of `[lean, full]` or `[lean]`, and that the contract file resolves. Methodology is descriptive and is not gated.

**The membership test is "plans or reports on one discrete test of a hypothesis about the effect of a change to a
product or its market", written once per test and finished when the decision it informs is recorded.** The draft the
research tested read "plans, runs, or reports on" and "finished when the result is read". The research changed both
phrases. No source found a document that runs a test. The finish line moved to the recorded decision as the
library's own position, because a decision can follow the result in a later meeting rather than coincide with it.

**The family is `phase: measure`, and this is the library's own position.** Neither member is a standing instrument.
Being written before a test runs does not move the design doc out of the phase it serves, exactly as a test plan
written before testing is still `phase: develop`. Both planned members carry the same catalog stage, `growth`, which
the phase vocabulary lacks, and `measure` is its nearest value. No source argues for a family boundary at this phase,
so the contract labels the call a POSITION, per
[decision-procedures.md section 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world).

**Two boundary sentences carry the research's findings.** A standing measurement instrument is not a member, however
closely it serves experiments. A test run before anything is built is not this family's job, and the contract places
no such document anywhere.

**Each member must place itself against three neighbours,** in its companion's Relationships section: the other
member, the spike report, and the QA pair `test-plan` and `test-summary-report`. This is a review obligation, not
gate-checkable.

### Consequences

* Good: membership is enforced in CI from the first member, and the tenth family is one registry entry with no new
  check code.
* Good: the axis question is closed before drafting starts, against both planned members.
* Good: the library gains its first family on `phase: measure`, the one phase value no contract used.
* Neutral: the contract is adopted with no members, so check K has nothing to gate for this family until the first
  member lands. The gate stays green in the meantime, and the enforcement is latent, not absent.
* Neutral: prose that counts **contracts** moves from nine to ten with this record. Prose that counts the **families of
  built bundles** does not move until a member lands, and `tools/check-counts.py` derives that number from the tree.
* Bad: demand is thin. The 2026-10-04 ranking found almost no shipped bundle that routes a reader to either type, so
  this family is built on the maintainer's preference under
  [ADR 0041 (maintainer preference sets the build order)](0041-maintainer-preference-sets-the-build-order.md), not on
  an inbound gap the library created.
* Bad: chaining onto the Saved Views thread couples both examples to `delivery-docs`, `governance-docs` and
  `strategy-docs` files. A rewrite of the PRD's success metrics or the KPI dashboard's baselines would leave both
  examples stale. The link gate catches a moved file, but not a changed number.

### Confirmation

Enforced by check K in `tools/check-bundles.py`, run in CI by `.github/workflows/ci.yml`, with branch protection on
`main` requiring the `gate` job.

Because no member exists yet, confirmation has two parts, as ADR 0026's did. **Now:** the registry entry is in place
and the gate is green, and `tools/test-check-k.py` section 5 asserts over the live `FAMILY_CONTRACTS` that every entry,
now including `experimentation-docs`, declares exactly one axis and a contract path that resolves. **When the first
member lands:** it becomes the live confirmation, reporting conformance to the contract. A member declaring
`classification: utility`, a wrong phase, a `draft` status or an out-of-shape size fails check K with a message naming
what it required.

## More Information

- The contract: [`experimentation-docs.md`](../contracts/experimentation-docs.md), modelled on
  [`qa-docs.md`](../contracts/qa-docs.md).
- The precedent for the axis reasoning: [ADR 0026](0026-adopt-qa-docs-family-contract.md). The precedent for a
  contract adopted with no members: [ADR 0024](0024-adopt-governance-docs-family-contract.md).
- The sibling record from the same research: [ADR 0067](0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md).
- The specs and the admission evidence: [`tier2-specs.md`](../tier2-specs.md#experimentation-docs-founding-members-the-experiment-design-doc-and-the-experiment-readout), the `experimentation-docs` section.
- Two other candidates from the same research are not recorded here. The north star metric definition was deferred
  with no record, and the concept test brief was parked; both catalog rows stay `candidate`.
