---
status: accepted
date: 2026-09-23
decision-makers: [jprisant]
consulted: [claude]
---

# `issue-log` joins `governance-docs` as a fourth member, `classification: utility`

## TL;DR

- **Decision.** The `issue-log` bundle declares **`family: governance-docs`** and
  **`classification: utility`**. It becomes that family's fourth member, alongside `risk-register`,
  `raid-log` and `kpi-dashboard`, and the [contract](../contracts/governance-docs.md) moves to `0.2.0`.
- **Why a record is needed at all.** The contract's membership test admits the type in as many words
  ("a continuously-maintained register, **log**, or dashboard ... to track risk, **open items**, or
  performance"), but
  [ADR 0024 (adopt the governance-docs family contract)](0024-adopt-governance-docs-family-contract.md)
  was written for exactly three members and contains **no fourth-member clause**, and the contract's own
  prose says "the three planned roles" and "the other two". That is the shape
  [ADR 0050 (qa-docs admits a fourth member)](0050-qa-docs-admits-a-fourth-member.md) settled for
  `qa-docs`, and it is settled here the same way: stated, not assumed inside a build.
- **Why this family and not another.** The `standing-standards` contract routes the type here itself:
  "A candidate **revised on a cadence and valuable only while current** is `utility` and belongs to
  `governance-docs` or `strategy-docs`". An issue log is exactly that, and it is not a strategy
  document.
- **What this does NOT decide:** whether `issue-log` passes
  [ADR 0030](0030-templating-scope-markdown-documents.md)'s admission test. That is answered by
  retrieval in [`tier2-specs.md`](../tier2-specs.md), not by contract reading.
- **Status:** accepted 2026-09-23. The maintainer directed the build that day; the agent drafted the
  family reading against the contract and ADR 0024, and it is reviewable in the change that carries it.

## Context and Problem Statement

The library already sends readers to an issue log it does not ship. `risk-register` and `raid-log`
each carry a chooser table with an **Issue log** column (`risk-register_guide.md` "Register, RAID log,
or issue log?", `raid-log_guide.md` "RAID log, risk register, or issue log?"), `risk-register`'s rubric
and both its templates route a materialized risk "to the issue log", and its companion section 8 rules
that the two are separate instruments. The program's issues `ISS-11` and `ISS-12` appear across four
sibling examples: they live in the RAID log's Issues quadrant, and the risk register, status report and
project retrospective cite them there, with `risk-register_example.md` calling that quadrant "the program
issue log". No `future:` tag records any of it, which is why no gate
flagged it (GitHub issue #176, build-candidate 2).

A family is a contract, so the family decides the bundle's obligations and must be known before its
spec. The type is a candidate in the catalog (`id: issue-log`, `category: Governance / Compliance /
Audit`, `stage: governance`, `methodology: PMBOK`, `relationships: [RAID]`).

## Decision Drivers

- The membership test, not the list of members that happened to be planned in 2026-07, governs a
  candidate. ADR 0050 established that reading for `qa-docs`.
- A family's teaching value in `governance-docs` is the **relationship** between its instruments, which
  its contract says fail "by collapsing into each other". A new member must make that relationship
  clearer, not muddier.
- [ADR 0041](0041-maintainer-preference-sets-the-build-order.md) makes the maintainer's preference the
  build order. The maintainer directed this build on 2026-09-23.

## Considered Options

1. **`governance-docs`, `classification: utility`, as a fourth member.** Chosen.
2. **No bundle: the RAID log's Issues quadrant is the issue log.** The library's own shipped position
   rejects this. `risk-register_companion.md` section 8 says the two track conditions that "might happen"
   and "have happened" and should be logged separately, and `raid-log_guide.md` says "if that is all you
   have, an issue log is enough", which presumes one exists.
3. **`qa-docs`, beside `bug-report`.** Rejected: that contract admits documents that "plan, specify, or
   report the verification of a product increment". An issue log records project problems of any kind
   (a departed engineer, a missed budget) and verifies nothing.
4. **`standing-standards`.** Rejected by that contract's own routing sentence, quoted above: an issue log
   is revised continuously and is worthless once stale, which is `utility`, not "agreed once and applied
   every time".

## Decision Outcome

**Chosen: `governance-docs`, `classification: utility`, fourth member.**

### Why it fits, positively

1. **The membership test names it.** "A continuously-maintained register, log, or dashboard that a
   product or program manager uses to track risk, open items, or performance across the whole
   lifecycle". An issue log is a continuously-maintained log of open items.
2. **`utility` is the only value the contract allows, and it is also the right one.** The contract
   defines `utility` as "a standing operational instrument", "set up once and maintained indefinitely",
   distinct from "a `tool` that is executed procedurally". An issue log is maintained, not executed.
3. **It completes the family's existing relationship map rather than adding a new axis to it.** The
   contract already describes the RAID log as a "superset-container" around the risk register's subject.
   **An issue log stands to RAID's I exactly as the risk register stands to its R**: the deepened,
   standalone form of one quadrant. `raid-log_guide.md` already draws that system: "the RAID log's **R**
   is the summary the risk register deepens, and its **I** is where a materialized risk lands."

### Consequences

- **The contract moves to `0.2.0`.** Its Members line records a fourth member; "the three planned roles"
  gains the issue log's line; "state its position against the other two" becomes "against the other
  members". No obligation changes, and check K's registry entry
  (`FAMILY_CONTRACTS["governance-docs"]`) needs no edit, because it gates values, not a member count.
- **The relationship obligation grows by one edge per member, and two siblings owe it.** The new
  companion states its position against all three siblings. Of the siblings, only `risk-register`'s
  companion already places the issue log (its section 8). **`raid-log`'s Relationships section and
  `kpi-dashboard`'s companion do not mention it at all**, so the day this contract says "the other
  members", both are out of contract until each gains its position against the issue log. The build adds
  those two lines in the same change as the bundle.
- **The shared-scenario rule binds hard here.** The example must be the Reporting Platform Modernization
  program's issue log, and `ISS-11` and `ISS-12` already exist in four sibling examples with fixed dates,
  owners and targets. The example must carry them as they are. Because the scenario keeps them in the
  RAID log's Issues quadrant, the example is the **deepened record behind that quadrant**, the same
  relationship the risk register has to the R, not a second list competing with it.
- **`pairs_with: []`.** No pm-skills skill produces or consumes an issue log; the contract already says
  members adopt `[]` until one does.
- The bundle stays subject to ADR 0030. This decision removes the family objection only.

## More Information

- Family contract: [`governance-docs`](../contracts/governance-docs.md), adopted by
  [ADR 0024](0024-adopt-governance-docs-family-contract.md).
- The precedent: [ADR 0050](0050-qa-docs-admits-a-fourth-member.md), which settled the same absence of a
  fourth-member clause for `qa-docs`.
- The spec: [`tier2-specs.md`](../tier2-specs.md).
