---
status: proposed
date: 2026-10-23
decision-makers: [jprisant]
consulted: [claude]
---

# Adopt the research-docs family contract at `phase: discover`, with two founding members

## TL;DR

- **Decision.** Adopt [`docs/internal/contracts/research-docs.md`](../contracts/research-docs.md) (version 0.1.0),
  the eleventh family contract, enforced by gate check K at **`phase: discover`**. Its two planned members are the
  catalog candidates `user-research-plan` (entry 210) and `user-research-report` (entry 18). One plans a study of
  the people a product serves, and the other reports it.
- **Why a new family.** Admission sweeps on 2026-10-23 admitted both types, and a placement pass tested the plan
  against all ten existing contracts. No contract admits either type as written. The nearest home,
  `discovery-docs`, admits only by an amendment that would drop part of what each type does.
- **Why two bundles, not one.** Dovetail, User Interviews and Maze each publish the plan and the report as
  separate templates or guides. The library's own `qa-docs` and `experimentation-docs` pairs set the same pattern.
- **What this does NOT decide:** the bundle ids and sizes, which the specs fix; whether the interview guide, the
  survey instrument or the diary study plan join; and the priority of issues #316 and #317, which the maintainer
  sets.
- **Status:** proposed 2026-10-23, and held until the maintainer reads the contract diff, because a family contract
  is "adopted only after a maintainer read"
  ([decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer)).

## Context and Problem Statement

On 2026-10-22 the maintainer asked for an admission sweep of the user research plan and the usability test plan,
expecting two bundles. The sweep found one type. Nielsen Norman Group says "When planning a usability test, the
research plan is often referred to as a test plan". The maintainer accepted that reading on 2026-10-23, and the plan
became catalog entry 210, with "usability test plan" as an alias (PR #315).

A placement pass the same day tested entry 210 against all ten family contracts and a draft of this one. No
contract admitted it as written. `discovery-docs` came closest. Its membership clause admits a type that exists "to
decide whether to build something, or which concept to design, before anyone commits to building it". A research
plan decides nothing, and much usability testing runs after a product ships. The pass recommended a sequence: sweep
the user research report (entry 18) next, and found a family if it cleared. The maintainer chose that sequence.

The entry 18 sweep cleared on 2026-10-23. NIST's NISTIR 7742 publishes an ungated report template built on
ISO/IEC 25062: "Reports delivered using this template should conform to the major headings and content areas
outlined below." UserTesting, User Interviews, Maze, Dovetail and the DHS usability testing kit publish sectioned
reports too. Of 277 quotations and headings the sweep returned, 273 matched raw page text. None of the four
failures is load-bearing. The sweep's evidence is held locally, at
`_local/research/2026-10-23_user-research-report-sweep/digest.md`.

Every new family gets a contract before its members are built, following the
[ADR 0020](0020-adopt-delivery-docs-family-contract.md) pattern. This record proposes that contract.

## Decision Drivers

- **A membership test must constrain.** A family that admits anything about users would absorb the persona, the
  problem statement and the Voice of Customer report, and it would teach nothing.
- **The axis call must be honest, not convenient,** as
  [ADR 0026 (adopt the qa-docs family contract)](0026-adopt-qa-docs-family-contract.md) required.
- **An alias the maintainer accepted is a scope promise.** "Usability test plan" names a document that often runs
  on a shipped product. A home that excludes that use breaks the promise.
- **The check should generalize, not grow machinery.** An eleventh family should be one `FAMILY_CONTRACTS` entry and
  no new check code.

## Considered Options

- **Option A: found a `research-docs` contract at `phase: discover`, with two members, methodology descriptive,
  examples chained onto the 2026-05 Reporting friction study, and enforcement through a new check K entry.**
  Chosen.
- **Option B: place both types in `discovery-docs` by a narrow amendment.** The amendment would widen "decide" to
  "inform", on the `user-persona` precedent, and keep evaluative research on built products out of scope. Rejected.
  It drops the usability test of a shipped product, which the accepted alias names. It also drops the report's
  summative case: NIST's template exists to help "vendors demonstrate evidence of usability in their final product".
- **Option C: place both types in `discovery-docs` by a wide amendment** that also drops "before anyone commits to
  building it". Rejected. That contract would then admit any document that informs a decision, which is the failure
  ADR 0066 named: a near-fit "would have to be widened until it stopped constraining anything."
- **Option D: place them in `experimentation-docs` or `qa-docs`.** Rejected. Itamar Gilad: "Per this definition an
  A/B test is an experiment, but a usability test is not." `qa-docs` reports "the verification of a product
  increment" against a specification, and a usability study records how people use a product.
- **Option E: one bundle, a plan with its report filled in later.** Rejected. EnjoyHQ keeps a plan and a report as
  two sections of one project record, and MeasuringU puts the report's outline inside the plan. Dovetail, User
  Interviews and Maze publish the two as separate templates or guides. With most sources separate, the `qa-docs` and
  `experimentation-docs` precedent decides it, and two documents give each member a clean finish.
- **Option F: a `classification` family.** Rejected. Nielsen Norman Group: "Typically, a research plan is
  constructed for each study." A report covers one study. Neither is maintained indefinitely.
- **Option G: three roles now, adding the session instruments** (the interview guide, entry 25, and the survey
  instrument, entry 26). Rejected for now. Neither has had its own admission sweep, and a clause written for
  unswept types would be fitted to a guess. The contract names both and says that adding the role is an amendment.

## Decision Outcome

**Adopt [docs/internal/contracts/research-docs.md](../contracts/research-docs.md) (version 0.1.0), enforced by the
existing gate check K through a new `FAMILY_CONTRACTS` entry keyed on `phase`.** For every bundle declaring
`family: research-docs`, check K requires `phase: discover`, a `beta` or `stable` status, a size shape of
`[lean, full]` or `[lean]`, and that the contract file resolves. Methodology is descriptive and is not gated.

**The membership test is "plans or reports on one study of the people a product serves", written for one study
and finished when that study's findings are reported.** Two parts of it are the library's own POSITION: that
analysing product telemetry alone is not a study, and the finish line.

**The family is `phase: discover`, and this is the library's own POSITION, with its cost stated.** The sources use
both documents for any kind of study, including evaluation of a shipped product. A family could hold several phase
values, but each bundle declares exactly one, and no source supplies a rule for which value a one-structure type
picks. The contract therefore holds that a study of what people do, need or can do with a product is discovery
work, whenever it runs. NIST's summative reports and GOV.UK's findings from services "after going live" are recorded
beside the call as the evidence that would reopen it.

**Each member must place itself against three neighbours** in its companion's Relationships section: the experiment
pair, the QA pair, and the `discovery-docs` documents that use its findings. This is a review obligation, not
gate-checkable.

### Consequences

* Good: membership is enforced in CI from the first member, and the eleventh family is one registry entry with no new
  check code.
* Good: the alias "usability test plan" keeps its whole meaning, because the family admits evaluative studies.
* Good: the shared scenario gains a document it has cited and never shown. The PRD example cites "Discovery readout:
  Reporting friction study, 2026-05 (n=12 analysts, illustrative)."
* Neutral: the contract is adopted with no members, so check K has nothing to gate for this family until the first
  member lands. The enforcement is latent, not absent.
* Neutral: prose that counts **contracts** moves from ten to eleven with this record. Prose that counts the
  **families of built bundles** does not move until a member lands.
* Bad: the axis call is a POSITION with named counter-evidence. A member built for a shipped-product study declares
  a phase that does not describe that study, and its companion must say why.
* Bad: demand is thin. No shipped guide or companion routes a reader to either type. The spike report's guide sends
  user research to `discover-interview-synthesis`, a pm-skills skill, not a bundle here. Four examples cite the
  Reporting friction study, but none points to a document type. This family is built on the maintainer's preference under
  [ADR 0041 (maintainer preference sets the build order)](0041-maintainer-preference-sets-the-build-order.md).
* Bad: chaining onto the Reporting friction study couples both examples to the PRD, design brief, epic and
  announcement examples. A rewrite of what those examples say about the study would leave both examples stale, and
  no gate checks that.

### Confirmation

Enforced by check K in `tools/check-bundles.py`, run in CI by `.github/workflows/ci.yml`, with branch protection on
`main` requiring the `gate` job.

Because no member exists yet, confirmation has two parts, as ADR 0066's did. **Now:** the registry entry is in place
and the gate is green, and `tools/test-check-k.py` section 5 asserts over the live `FAMILY_CONTRACTS` that every
entry, now including `research-docs`, declares exactly one axis and a contract path that resolves. **When the first
member lands:** it becomes the live confirmation.

## More Information

- The contract: [`research-docs.md`](../contracts/research-docs.md), modelled on
  [`experimentation-docs.md`](../contracts/experimentation-docs.md) and [`qa-docs.md`](../contracts/qa-docs.md).
- The precedent for founding a family with two planned members:
  [ADR 0066](0066-adopt-experimentation-docs-family-contract.md).
- The precedent for a contract adopted with no members: [ADR 0024](0024-adopt-governance-docs-family-contract.md).
- The build-candidate issues: #316 (bundle: user-research-plan) and #317 (bundle: user-research-report).
- The evidence is held locally: the plan's sweep at
  `_local/research/2026-10-23_research-plan-and-usability-test-plan-sweep/digest.md`, the placement pass at
  `_local/research/2026-10-23_research-plan-placement/placement-digest.md`, and the report's sweep at
  `_local/research/2026-10-23_user-research-report-sweep/digest.md`.
