---
status: accepted
date: 2026-09-27
decision-makers: [jprisant]
consulted: [claude]
---

# `change-log-governance` joins `governance-docs` as a fifth member, `classification: utility`

## TL;DR

- **Decision.** The `change-log-governance` catalog candidate, shipped as bundle id **`change-log`**,
  declares **`family: governance-docs`** and **`classification: utility`**. It becomes that family's fifth
  member, alongside `risk-register`, `raid-log`, `kpi-dashboard` and `issue-log`, and the
  [contract](../contracts/governance-docs.md) moves to `0.3.0`.
- **Why a record is needed at all.** The contract's membership test admits the type in as many words ("a
  continuously-maintained register, **log**, or dashboard ... to track risk, **open items**, or
  performance"), and [ADR 0060 (change-request joins delivery-docs)](0060-change-request-joins-delivery-docs.md)
  states three times, while explicitly declining to decide it, that `governance-docs` "admits a standing
  register as written" if the type is ever built (lines 29, 84-86, 105-106). But
  [ADR 0024 (adopt the governance-docs family contract)](0024-adopt-governance-docs-family-contract.md)
  was written for three members, and even after
  [ADR 0057 (issue-log joins governance-docs as a fourth member)](0057-issue-log-joins-governance-docs-as-a-fourth-member.md)
  the contract's own prose still enumerates exactly four roles and says so in as many words: "The four
  roles are distinct but related." That gap is the same one ADR 0057 and
  [ADR 0050 (qa-docs admits a fourth member)](0050-qa-docs-admits-a-fourth-member.md)
  each closed by amending the roles list and adding a dated change note, and it is closed here the same
  way: stated, not assumed inside a future build.
- **Why this family and not another.** Every other family contract excludes the type on grounds
  ADR 0060 already argued for the per-occasion change request, applying at least as clearly to that
  request's standing register: `delivery-docs` names the exclusion by name ("it does not admit ... the
  standing register of such requests (a change log)"); `standing-standards` excludes anything continuously
  revised rather than agreed once; `decision-docs`, `qa-docs`, `process-docs`, `communication-docs`,
  `discovery-docs` and `strategy-docs` each exclude it on the same ground that excluded the request itself.
- **What this does NOT decide:** whether `change-log-governance` passes
  [ADR 0030 (templating scope: markdown documents)](0030-templating-scope-markdown-documents.md)'s
  admission test. That question is answered by retrieval in the spec, not by contract reading, and the
  spec's own admission evidence (five independently-verified named sources) is recorded separately from
  this family decision. Nor does this decide the bundle id beyond the reasoning the spec already carries;
  see "More Information."
- **Status:** accepted 2026-09-27. The maintainer ruled on the research the same day and accepted this
  record on reading the contract diff, as with [ADR 0059](0059-announcement-internal-comms-joins-delivery-docs.md)
  and [ADR 0060](0060-change-request-joins-delivery-docs.md).

## Context and Problem Statement

Two shipped bundles already send a reader to a standing change log the library does not ship.
`change-request_companion.md:369-373` states plainly, from its own side: "A standing change log, if this
library ever builds one, is a `governance-docs` candidate, not a variant of this bundle," and its lean and
full templates both tell a filler "this document is not the change log; it feeds one"
(`change-request_template-lean.md:45`). `issue-log_companion.md:358-361` and
`issue-log_template-full.md:224-244` both name "a separate change log for submitted change requests" as
the convention their own Links to Other Logs section records against. `docs/internal/contracts/delivery-docs.md:13`
excludes the type from that family by name: "it does not admit the standing register of such requests (a
change log), which is a `governance-docs` instrument if it is ever built." No `future:` tag records any of
this, because none of these references is a promise tag; they are boundary statements the library has
already shipped without a target to point at.

A family is a contract, so the family decides the candidate's obligations and must be settled before its
spec is finished. The type is a candidate in the catalog (`id: change-log-governance`, `category:
Governance / Compliance / Audit`, `stage: governance`, `methodology: PMBOK/ITIL`, `relationships: [Change
Requests]`). A research pass on 2026-09-27 found five named sources publishing the type as a written
document, and tested it against all nine family contracts with no family assumed. `governance-docs` admits
it as written; the other eight exclude it.

## Decision Drivers

- The membership test, not the list of members that happened to be planned when the contract was adopted,
  governs a candidate. ADR 0050 established that reading for `qa-docs`, and ADR 0057 confirmed it for
  `governance-docs` itself.
- A family's teaching value in `governance-docs` is the **relationship** between its instruments, which its
  contract says fail "by collapsing into each other." A new member must make that relationship clearer,
  not muddier, and its companion must state its position against every other member, not only the ones it
  most resembles.
- A family contract's own assertions about the world are tested against each new member's research log,
  per [decision-procedures.md section 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world).
  This candidate's own admission evidence surfaces one qualification the contract's prose does not yet
  carry (below).

## Considered Options

1. **`governance-docs`, `classification: utility`, as a fifth member.** Chosen.
2. **No bundle: the change request's own Implementation and Traceability section is the change log.**
   The library's own shipped position rejects this. `change-request_companion.md:369-373` and
   `change-request_template-lean.md:45` both state the request "feeds" a log rather than being one, and
   PM²'s own methodology guide documents the two as separate, paired artifacts throughout its process
   narrative.
3. **`delivery-docs`, beside `change-request`.** Rejected on the same reasoning `delivery-docs.md:13`
   already states from its own side: the family's chain carries one unit of product work from definition
   to delivery, and a standing register maintained across every unit of work indefinitely is not one link
   in that chain. `delivery-docs.md:13` names this exclusion explicitly, by the same document type, in the
   sentence that first names this candidate's own catalog id.
4. **`standing-standards`.** Rejected by that contract's own routing sentence: "A candidate revised on a
   cadence and valuable only while current is `utility` and belongs to `governance-docs` or
   `strategy-docs`." A change log is revised on every submitted request, not agreed once and applied every
   time, the same reasoning ADR 0057 already applied to `issue-log`.
5. **A new one-member family for standing change-control instruments.** Rejected on the same grounds ADR
   0060 rejected the parallel option for `change-request`: more machinery for one type, when an existing
   contract's own membership test already names it in as many words.

## Decision Outcome

**Chosen: `governance-docs`, `classification: utility`, fifth member.**

### Why it fits, positively

1. **The membership test names it, and a sibling family's own decision record says so three times.**
   `governance-docs.md:13`: "a continuously-maintained register, log, or dashboard that a product or
   program manager uses to track risk, open items, or performance across the whole lifecycle." A standing
   change log is a continuously-maintained log of requested and decided baseline changes, and
   `0060-change-request-joins-delivery-docs.md` states the resulting family call for the register three
   separate times (lines 29, 84-86, 106) while declining to make it, which this record now makes.
2. **`utility` is the only value the contract allows, and it is also the right one.** The contract defines
   `utility` as "a standing operational instrument," "set up once and maintained indefinitely," distinct
   from "a `tool` that is executed procedurally." A change log is maintained across the lifecycle of every
   change a project or program raises, not executed once per occasion the way the request that feeds it
   is.
3. **It completes the family's existing relationship map by the same pattern `issue-log` already set,
   rather than adding a new axis to it.** The risk register deepens the RAID log's R; the issue log deepens
   its I; **a change log stands in the same relationship to the delivery chain's own change request that
   the issue log stands in to the RAID log's Issues column**: the standing, cumulative record behind a
   document that is filed once per occasion and then archived
   (`change-request_template-full.md:242`: "PM2's own form is archived once logged").

### Consequences

- **The contract moves to `0.3.0`.** Its Members line records a fifth member; "The four roles are distinct
  but related" gains a fifth bullet and becomes "The five roles"; the enumeration's closing punctuation
  changes to admit it. No structural obligation changes, and check K's registry entry
  (`FAMILY_CONTRACTS["governance-docs"]`) needs no edit, because it gates values, not a member count, the
  same finding ADR 0057 made for the fourth member.
- **The relationship obligation grows by one edge per member, and every sibling owes it.** The new
  companion states its position against `risk-register`, `raid-log`, `kpi-dashboard` and `issue-log`
  alike, per contract section 1. Whether each sibling's own companion gains a reciprocal line about the
  change log is a build decision, not one this record settles, the same posture ADR 0057 took toward
  `kpi-dashboard`'s own gap at the time.
- **The contract's own POSITION needs one qualification this candidate's evidence adds, that ADR 0057 did
  not have to.** `governance-docs.md:23` states, as the library's own reasoning rather than a sourced
  claim, that these instruments "most often fail by collapsing into each other rather than by staying
  separate." PRINCE2 (via `prince2.wiki`, raw-checked) folds change-request tracking into the Issue
  Register **by design**: "should be documented in the issue register or change log," naming a standalone
  change log only as an interchangeable alternative. That is a named methodology choice, not a failure
  mode, and the change note below records the qualification with today's date, per
  [decision-procedures.md section 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world),
  so the sentence stays a POSITION the library owns rather than a CLAIM this candidate's own admission
  evidence would otherwise contradict.
- **The shared-scenario rule binds hard here, more specifically than for any earlier member.** The example
  must be the Reporting Platform Modernization program's change log, and it must carry `CR-SV-01` exactly
  as `change-request_example.md` states it, because that sibling's own worked example already treats this
  unbuilt log as the record its decision was made against ("this document is the record that process
  decided on," `change-request_example.md:113`). The full constraint set, including which facts the entry
  may not contradict, is in the spec.
- **`pairs_with: []`.** Checked 2026-09-27 against `pm-skills` `origin/main` directly; no skill produces or
  consumes this document type. One name, `utility-pm-changelog-curator`, targets the unrelated software
  CHANGELOG sense and is not a match.
- **The bundle id is `change-log`, not the catalog id verbatim.** The catalog id `change-log-governance`
  is unchanged and remains what `related_templates` and any future `future:` tag should resolve against;
  the shipped directory name is shorter, following the precedent `spike-report` and `test-summary-report`
  already set for a compound catalog id. The reasoning, including the one real near-miss this choice does
  not remove (`release-notes`' `changelog` alias), is argued in full in the spec, not repeated here.
- **The catalog entry needs correction on landing**, per
  [procedure 1](../decision-procedures.md#1-a-catalog-call-loses-to-research): its
  `methodology: "PMBOK/ITIL"` is contradicted by every source this pass actually read, and its
  `size_variant: "S"` undercounts the two-weight shape the sources themselves support. The spec states the
  exact corrections.
- The bundle stays subject to ADR 0030. This decision removes the family objection only, exactly as ADR
  0057 stated for its own admission.

## More Information

- Family contract: [`governance-docs`](../contracts/governance-docs.md), adopted by
  [ADR 0024](0024-adopt-governance-docs-family-contract.md); the
  previous amendment was ADR 0057.
- The precedent for a stated, not assumed, enumeration edit:
  [ADR 0050](0050-qa-docs-admits-a-fourth-member.md) and
  [ADR 0057](0057-issue-log-joins-governance-docs-as-a-fourth-member.md).
- The record this candidate's family question was deferred from:
  [ADR 0060 (change-request joins delivery-docs)](0060-change-request-joins-delivery-docs.md),
  "What this does NOT decide."
- The spec and the admission evidence: [`tier2-specs.md`](../tier2-specs.md), the `governance-docs` (fifth
  member) section.
- **One sibling sentence is corrected when the bundle lands.** `change-request_companion.md` says HHS's EPLC
  program "merges" the request form and the log. Re-reading the same HHS plan template shows it defines
  **one shared list of data elements** for "Change Request Form and Change Management Log", while keeping
  two artifacts: its process table has a "Log CR" step in which "The Change Manager enters the CR into the
  CR Log", and HHS ships the log as its own spreadsheet. The companion's sentence gets a dated correction to
  that reading in the landing PR.
