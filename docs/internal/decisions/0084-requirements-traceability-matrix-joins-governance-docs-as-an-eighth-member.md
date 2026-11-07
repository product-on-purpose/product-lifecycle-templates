---
status: accepted
date: 2026-11-05
decision-makers: [jprisant]
consulted: [claude]
---

# `requirements-traceability-matrix` joins `governance-docs` as an eighth member

## TL;DR

- **Decision.** The catalog candidate `requirements-traceability-matrix` (entry 37, issue #261) declares
  **`family: governance-docs`** and **`classification: utility`**. It becomes that family's eighth member,
  and the [contract](../contracts/governance-docs.md) moves to `0.6.0`.
- **Why it is not declined like the deployment plan.**
  [ADR 0064 (deployment plan declined)](0064-deployment-plan-is-declined.md) rested on content that already
  ships and on a family none could offer. Here no shipped table maps requirements to their verification, and
  one contract fails on one phrase.
- **Why not `qa-docs`.** A `qa-docs` member is "produced at a stage and finished". A matrix is updated
  whenever its requirements or tests change, so `qa-docs` is the wrong axis, not merely a strained reading.
- **Who should not use it.** Named practitioners say the matrix rarely repays its upkeep outside regulated
  work. The guide must say so, and the build carries a stop rule if the worked example cannot justify itself.
- **Status:** accepted 2026-11-05. Given a plain-English summary of the choices, the maintainer answered "Build matrix,
  skip guide". The new contract clause was then put to the maintainer word for word before this record merged
  ([decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer)).

## Context and Problem Statement

Admission sweep 7 tested the type on 2026-10-29 and recommended admitting it at medium confidence. It left two
questions for the maintainer: which family holds it, and whether ADR 0064's reasoning controls. On 2026-11-04
the maintainer chose to take this candidate through admission second. A read on 2026-11-05 tested both
questions, and this record states the result.

## Decision Drivers

- **Cadence decides the axis before anything decides the family.**
  [ADR 0073 (data dictionary joins governance-docs)](0073-data-dictionary-joins-governance-docs-as-a-seventh-member.md)
  set this driver, and it settles the choice the sweep left open.
- **Admission and the build decision are separate questions.** ADR 0064 established this, so clearing admission
  does not oblige a build.
- **A widening must be the smallest honest one.**
  [ADR 0060 (change request joins delivery-docs)](0060-change-request-joins-delivery-docs.md) set that standard.
- **Build order is the maintainer's preference.**
  [ADR 0041 (maintainer preference sets the build order)](0041-maintainer-preference-sets-the-build-order.md)
  makes a contested but admissible type a legitimate choice.

## Considered Options

1. **`governance-docs`, `classification: utility`, eighth member, with one new clause in the purpose phrase.**
   Chosen.
2. **`qa-docs`, `phase: develop`, with no amendment.** Rejected on the axis, below.
3. **Decline on duplication and family fit, in ADR 0064's shape.** Rejected, because neither ground holds.
4. **Decline on efficacy, because the critics are right outside regulated work.** Rejected as a family or
   admission ground. This library ships contested types with their critics stated. It remains the maintainer's
   call under ADR 0041, and it is the realistic alternative to this record.

## Decision Outcome

**Chosen: option 1.**

### Admission clears, on vendor sources only

Each quotation passed a raw-text check on 2026-11-05.

- **Check 1, the written form.** TestDevLab: "A Traceability Matrix is a document that links and maps project
  requirements to their corresponding test cases." Jama Software: "A requirements traceability matrix is a
  structured information artifact". Visure Solutions: "a structured document or tool designed to establish and
  maintain traceability".
- **Check 2, phase fit.** Not applicable: the type takes a `classification`.
- **Check 3, written-form scope.** The type is a table, the shape `risk-register` and `raid-log` already ship.
- **Check 5, a software audience: a weak pass.** InfoQ's 2008 roundup opens "A formal traceability matrix often evokes
  strong response from the Agile community", and it reports software practitioners arguing from their own projects. Alistair
  Cockburn, for one, writes from "30 years in the business". Jama writes that the matrix "is widely used in regulated product
  development". No named software team's own matrix was read. TestDevLab's example of a development team is a hypothetical,
  and the sweep's claim about Orcanos' development team did not match that page's text.

**Every qualifying source is a vendor**, and three sell the live alternative. PMI's template sits behind a
membership wall and was not read. The Texas Department of Information Resources ships a standalone template, but
its page has no quotable prose.

### Check 4: no built bundle does its job (POSITION)

TestDevLab states the job: "Highlight any requirements that do not have a corresponding test case." That needs
every requirement in one view.

| Shipped text | Why it does not do that job |
|---|---|
| `test-case`, Identification and Traceability | It points one case at one thing, so a requirement with no case never appears |
| `test-summary-report`, the results table | Its row is an area or suite, and the report closes when a test cycle does |
| `test-plan`, test items | It names items by build or requirement ID and holds no mapping |
| `prd` and `acceptance-criteria` companions | They name the practice for regulated contexts and hold no table |
| `change-request` and `change-log`, Implementation and Traceability | They link a change to its follow-up, a different subject |

**ADR 0064 does not control.** The deployment plan's rollout and rollback tables shipped in
`launch-coordination-checklist`, and every family excluded it. Neither is true here.

### Why `governance-docs`, and why not `qa-docs`

**The cadence fits `governance-docs`.** Its members are "set up once and maintained indefinitely". Jama writes that
the matrix "should be updated whenever requirements, test cases, or linked lifecycle artifacts change, not just on a
calendar schedule." Ketryx calls it "a living artifact". The catalog's own stage is "throughout, audits".

**The cadence does not fit `qa-docs`.** That contract's axis note says each member is "produced at a stage and
finished", and it records "where the type is authored in the lifecycle". A matrix is authored throughout. The sweep
offered `qa-docs` as a reading that needs no amendment, but that saving would misdescribe the type.

**One wrinkle, stated plainly.** Jama also calls the matrix "a specific versioned artifact that captures those links
at a point in time." This library reads that as the standing register snapshotted for an audit, not as a document
written per occasion. That reading is a POSITION.

### What widens, and by how much

Only the purpose phrase changes. Section 1 gains one clause, "or to record how each requirement traces to the work
that implements and verifies it, so that a requirement with no verification can be seen", and no existing word
changes. The register noun, the lifecycle scope and the cadence are unchanged. The widening admits no document that
is produced once and finished.

### Consequences

**Good.**

- The library gains the one view its `test-case`, `prd` and `acceptance-criteria` text already names and does not
  provide.
- The boundary with `qa-docs` is stated on the axis, so later candidates can test against it.

**Bad, and stated plainly.**

- **This would be the library's first built Tier 3 bundle.** The catalog's closing recommendations say to treat
  regulated Tier 3 artifacts as a separate module. No ADR adopted that advice, but this record departs from it.
  *(Added 2026-11-06, at landing: this record missed a standing ruling. Decision D4 closed on 2026-08-14 as a
  deliberate no to Tier-3 regulated content, because a regulated template carries a duty to re-verify regulation text
  on a cadence, and [ADR 0039](0039-maintainer-discretion-replaces-the-pull-gate.md) says it does not unblock that.
  Neither this record nor the spec named D4 to the maintainer. This library's reading is that D4 does not reach this
  bundle. It states no regulation's requirements, declares `methodology: generic`, cites standards for existence only,
  and its example is unregulated, so it takes on no such duty. The catalog's Tier 3 for this row is also marked
  `tier_inferred`. A later version that states what a regulation requires would reopen D4.)*
- **The evidence is vendor-only.** The sources that call it a document also sell its replacement.
- **The named critics may be right for most readers.** Scott Ambler: "traceability matrices are highly overrated".
  Alistair Cockburn: "NEVER seen a traceability matrix pay off". Both quotations come from a 2008 InfoQ roundup. The
  guide states them, with Ambler's own regulated exception.
- **The relationship obligation grows by one edge per member.** The new companion states its position against all
  seven existing members, per contract section 1.
- **The family's shared-scenario rule is a real test.** Acme Analytics is not a regulated company, so the example
  must justify a matrix on other grounds. See the stop rule.

### The stop rule

The spec's example traces Saved Views requirements to their tests. If that example reads as overhead for an
unregulated team, the build stops and this decision returns to the maintainer with option 4 on the table.

### Confirmation

The maintainer's go on the contract clause confirms this record. Check K then gates the member's values. Its registry
entry needs no edit, because it gates values and not a member count.

## More Information

- The spec: [`tier2-specs.md`](../tier2-specs.md), section "governance-docs (eighth member, by amendment): the
  requirements traceability matrix".
- Family contract: [`governance-docs`](../contracts/governance-docs.md), adopted by
  [ADR 0024](0024-adopt-governance-docs-family-contract.md). The model for this record is ADR 0073.
- The read and the sweep are held locally, at `_local/research/2026-11-05_rtm-read/read.md` and
  `_local/research/2026-10-29_admission-sweep-7/digest.md`.
