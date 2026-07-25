---
status: accepted
date: 2026-07-25
decision-makers: [jprisant]
consulted: [claude]
---

# Adopt the strategy-docs family contract (product-vision, product-strategy, product-roadmap, okrs), the first to gate a set of axis values

## Context and Problem Statement

The Tier-1 floor build-out ([ADR 0021](0021-complete-the-tier-1-floor.md)) turns next to `strategy-docs`: the
family that sets and tracks product direction above the level of any single deliverable. Every new family gets
a ratified contract before its members are built ([ADR 0020](0020-adopt-delivery-docs-family-contract.md)
pattern), so a member is born into an enforced family rather than joining an honour system.

Three things make this contract different from the four before it.

**It is the first family whose members do not share one axis value.** delivery-docs and decision-docs gate a
single `phase`; governance-docs and qa-docs each gate a single value on their axis. This family spans
`classification: foundation` (vision, strategy) and `classification: utility` (roadmap, OKRs).
[ADR 0023](0023-resolve-the-tier-1-family-taxonomy.md) ratified that split in principle and added set support
to check K specifically because this family was known to be coming; `tools/test-check-k.py` has carried a
`strategy-docs` fixture asserting the behaviour ever since. **This contract is the first live use of a
capability built ahead of its subject.**

**It is the family where a gated `methodology` field would most obviously break.** `okrs` is
methodology-bound in a way no previous member has been: the artifact *is* the method. The other three are
methodology-agnostic. Any single required value would force one of the four to misdescribe itself.

**And it is the family that closes the library's worked thread upward.** `qa-docs` extended the Acme Analytics
scenario downward into verification. The hooks for extending it upward already exist and predate this family:
the PRD example cites an FY26 "Time to Insight" company goal, and the kpi-dashboard example wires its primary
metric to that goal's panel. Nothing has ever pointed back at those references.

## Decision Drivers

- **Contract-first, so membership is mechanical from the first member.**
- **The axis assignment must be argued against the real members**, which is what ADR 0023 deferred to this
  step rather than settling in the abstract.
- **Do not re-learn the ADR 0020 lesson.** Methodology is descriptive, not a membership rule.
- **The check should generalize, not grow machinery.** A fifth family, and the first with a value set, should
  be one `FAMILY_CONTRACTS` entry and no new check code.
- **The family's teaching value is a cascade**, so the contract must protect the cascade, not just the shapes.

## Considered Options

- **Option A: adopt a strategy-docs contract now, `classification: [foundation, utility]`, methodology
  descriptive, examples chained onto the existing Acme Analytics thread, enforced by check K via a registry
  entry.** Chosen.
- **Option B: split into two families**, one `foundation` (vision, strategy) and one `utility` (roadmap,
  OKRs). Rejected. It would satisfy single-value purity at the cost of the thing the family is for: the
  cascade from vision to measurement is the teaching content, and a family boundary drawn through the middle
  of it would make each half's Relationships section point mostly outside its own family. ADR 0023 already
  rejected drawing families by axis value rather than by job, and set support in check K exists so that this
  choice does not have to be made.
- **Option C: make all four `foundation`**, on the argument that direction-setting artifacts underpin the
  work. Rejected: it misdescribes the roadmap and the OKR set, whose entire value is being *current*. A
  foundation artifact that is out of date is a historical record; a utility instrument that is out of date is
  broken. The two failure modes are different, and the classification should say which one applies.
- **Option D: defer the contract until the first member is built**, as decision-docs did. Rejected for the
  same reason as governance-docs and qa-docs: it would build the first member into an unenforced family, and
  it would leave the two-class split unargued while drafting begins.

## Decision Outcome

**Adopt [docs/internal/contracts/strategy-docs.md](../contracts/strategy-docs.md) (version 0.1.0), enforced by
the existing gate check K via a new `FAMILY_CONTRACTS` entry keyed on `classification` with a two-value set.**
For every bundle declaring `family: strategy-docs`, check K requires a `classification` of either `foundation`
or `utility`, a `beta` or `stable` `status`, a size shape of `[lean, full]` or `[lean]`, and that the contract
file resolves. Methodology is descriptive and is not gated.

**The two-class split is argued on what the artifacts are.** `product-vision` and `product-strategy` are
`foundation`: argued rather than maintained, changing on a timescale of years, and underpinning everything
below them. `product-roadmap` and `okrs` are `utility`: standing operational instruments revised on a cadence,
whose value comes from being current. The distinction is **argued-and-durable versus maintained-and-periodic**,
the same distinction that earned `governance-docs` its `utility` claim.

**`business-case` is confirmed out of this family**, as ADR 0023 decided: it is written once to justify an
investment and is then finished, which is a `phase: discover` artifact, and it belongs to `discovery-docs`.

**The family-specific rule is a shared scenario that chains onto the existing thread**, in the direction
opposite to qa-docs. The OKR example takes "Time to Insight" as its objective and the roadmap example contains
the work the PRD describes, so that on completion the library holds one continuous worked thread from a
product vision down to a bug report.

**Real skill pairings exist here, unlike in qa-docs.** `foundation-okr-writer` and `measure-okr-grader` both
address `okrs` directly, and `foundation-lean-canvas` describes itself as serving strategy framing and
stress-testing. All three are verified present in pm-skills and pinned to `tools/known-skills.txt`. This is
worth recording next to finding EC-4 (pm-skills covers no testing or QA work at all): the org's skill library
is strong at the strategy end and absent at the verification end, which is a coverage shape rather than a
uniform gap.

### Consequences

* Good: strategy-docs membership is enforced in CI from its first member, and the fifth family is one registry
  entry with no new check code, now demonstrating that the registry generalizes across axes **and** across
  cardinality.
* Good: a capability built ahead of its subject (set-valued axis gating, ADR 0023) gets its first live use,
  and the fixture that has been guarding it acquires a real counterpart.
* Good: the two-class split is argued against real members at the step ADR 0023 designated for it, rather than
  inherited unexamined.
* Good: the library gains, on completion, a single worked thread spanning vision to bug report, which is the
  strongest available demonstration that the bundles are one library rather than fifteen documents.
* Neutral: the contract is adopted with zero members, so check K has nothing to gate for this family until
  `product-vision` lands. Enforcement is latent, not absent.
* Bad, and worth stating plainly: **because the contract accepts either value, check K cannot tell you a
  specific member picked the right one.** Nothing mechanical stops `product-vision` declaring `utility`. This
  is the cost of set support, it applies to any multi-value family, and the mitigation is that section 2 of
  the contract argues the split explicitly so review has a standard to check against.
* Bad: chaining upward couples four more examples to the Acme Analytics scenario. The blast radius of ever
  rewriting that scenario now spans four families. Accepted for the same reason qa-docs accepted it, and
  recorded here so a future rewrite knows the scale.

### Confirmation

Enforced by check K in `tools/check-bundles.py`, run in CI by `.github/workflows/ci.yml`, with branch
protection on `main` requiring the `gate` job.

Because no strategy-docs member exists yet, confirmation has two parts. **Now:** the registry entry is in
place and the gate is green (nothing to gate yet, and the contract file resolves); `tools/test-check-k.py`
section 4 already asserts that a `strategy-docs`-shaped set-valued family accepts `foundation` and `utility`,
rejects `tool` with a message listing the allowed set, and rejects a member bringing `phase` with a message
naming the set rather than a bare value; and section 5 asserts over the live registry that every ratified
entry declares exactly one axis and a contract that resolves. **When product-vision lands:** it becomes the
live confirmation, reporting "conforms to strategy-docs contract (classification, status, sizes)"; a member
declaring `phase`, a classification outside the set, a `draft` status, or an out-of-shape size will each fail.

## More Information

This is the fifth family contract, after [delivery-docs](../contracts/delivery-docs.md)
([ADR 0020](0020-adopt-delivery-docs-family-contract.md)), [decision-docs](../contracts/decision-docs.md)
([ADR 0022](0022-adopt-decision-docs-family-contract.md)), [governance-docs](../contracts/governance-docs.md)
([ADR 0024](0024-adopt-governance-docs-family-contract.md)) and [qa-docs](../contracts/qa-docs.md)
([ADR 0026](0026-adopt-qa-docs-family-contract.md)). Its four members are built next through the per-bundle
pipeline ([docs/internal/bundle-pipeline.md](../bundle-pipeline.md)); the build-out stops at the strategy-docs
family boundary for maintainer batch review.

One citation hazard is named in the contract's section 3.6 because it differs from the previous two families':
where `qa-docs` had to guard against citing superseded standards, this family's canonical sources are largely
**books and named practitioners**, so the likely failure mode is **misattribution** rather than staleness. The
qa-docs build found four separate misattributions circulating as fact; the same discipline applies here, and
the research must verify who said what before anything is quoted.
