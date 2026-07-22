---
status: accepted
date: 2026-07-22
decision-makers: [jprisant]
consulted: [claude]
---

# Resolve the Tier-1 family taxonomy: definition-of-done, strategy-docs, and ops-docs

## Context and Problem Statement

[ADR 0015](0015-second-taxonomy-axis-phase-xor-classification.md) gave every bundle exactly one taxonomy
axis: a lifecycle artifact declares `phase`, a standing artifact declares `classification`, never both.
[ADR 0020](0020-adopt-delivery-docs-family-contract.md) then made family membership mechanical, with check K
gating a family's declared values. Together these imply a rule that was never written down: **a family must
be coherent on one axis**, because its contract can only gate one.

The Tier-1 floor build-out ([ADR 0021](0021-complete-the-tier-1-floor.md)) surfaced three places where the
proposed families break that rule. They were recorded as D-A and D-B in
[buildout-specs.md](../buildout-specs.md) and marked provisional, because building bundles on a wrong family
call is expensive to unwind: the metadata, the contract, the ADR, and the cross-references all encode it.

- **D-A: `definition-of-done` sits in delivery-docs**, a `phase: deliver` family. A DoD is a standing quality
  standard: one DoD applies to every increment, in every sprint, indefinitely. That is
  `classification: foundation`. Keeping it required either dishonest metadata or amending the contract to
  accept a classification member, which is precisely the anti-pattern ADR 0020 warns against.
- **D-B (strategy-docs): `business-case` is phase-bound** (built once, to decide whether to proceed) while
  `product-vision`, `product-strategy`, `product-roadmap` and `okrs` are standing artifacts maintained
  across the whole lifecycle.
- **D-B (ops-docs): `runbook` is a standing operational tool** (`classification: tool`) while
  `incident-postmortem` is an event-driven learning artifact produced after a specific incident
  (`phase: iterate`). They share a domain, not an axis.

These three blocked all remaining bundle work: 19 of the 27 Tier-1 types sit in families whose shape depends
on them.

## Decision Drivers

- **Honest metadata outranks a tidy grouping.** ADR 0020's lesson was that a contract must describe what its
  members actually are. A family that only coheres if one member lies is not a family.
- **Domain intuition is not an axis.** "These are all ops documents" is a true statement about subject
  matter and says nothing about whether they are standing or phase-bound.
- **Prefer moving a member to inventing a family.** Each new family costs a contract, an ADR, and a registry
  entry. A member that already fits an existing family should move there.
- **Do not weaken check K to fit a grouping.** The alternative to resolving these was a mixed-axis contract,
  which would have made the gate unable to prove the thing family membership is supposed to mean.

## Considered Options

**D-A (definition-of-done):** (a) move it to a new standing family; (b) fold it into governance-docs;
(c) keep it in delivery-docs and amend that contract.

**D-B (strategy-docs):** (a) make strategy-docs classification-coherent and move `business-case` out;
(b) split into a standing strategy family and a periodic planning family; (c) declare all five
`phase: discover`.

**D-B (ops-docs):** (a) split by axis, dissolving ops-docs; (b) keep ops-docs as a domain family and extend
check K to permit mixed-axis contracts; (c) keep ops-docs with a contract that gates only status and sizes,
leaving the axis ungated.

## Decision Outcome

**D-A: option (a).** `definition-of-done` leaves delivery-docs and anchors a new **standing-standards**
family as `classification: foundation`. delivery-docs completes at six `phase: deliver` members.

**D-B (strategy-docs): option (a).** strategy-docs becomes a **classification** family holding
`product-vision` and `product-strategy` (`foundation`) plus `product-roadmap` and `okrs` (`utility`).
`business-case` moves to **discovery-docs**, which is already `phase: discover`, and which stops being a
one-member family as a result.

**D-B (ops-docs): option (a).** ops-docs dissolves. `incident-postmortem` joins **process-docs** with
`sprint-retrospective-notes` (both `phase: iterate`, both blameless learning artifacts, and the
postmortem-versus-retrospective distinction becomes a teaching point inside one family rather than a
cross-family footnote). `runbook` joins **standing-standards** as `classification: tool`.

**standing-standards is defined by what its members are, not by their subject.** A DoD and a runbook are
both *agreed once, applied every time*: the DoD applies to every increment, the runbook to every occurrence
of its procedure. That is the same standing relationship, which is why they gate on the same axis despite
one being a quality standard and the other an operational procedure. The name is provisional; if the family
grows past a handful it may split by domain, which would be a contract change and not a taxonomy change.

**The resulting Tier-1 family map** (19 remaining types, which independently reproduces the count D-D
reconciled):

| Family | Axis | Members |
|---|---|---|
| delivery-docs | `phase: deliver` | prd, user-stories, product-backlog, sprint-backlog, acceptance-criteria, release-notes (**complete**) |
| decision-docs | `phase: develop` | adr, rfc, sdd (**complete**) |
| governance-docs | `classification: utility` | risk-register, raid-log, kpi-dashboard |
| qa-docs | `phase: develop` | test-plan, test-case, bug-report |
| strategy-docs | `classification: foundation` or `utility` | product-vision, product-strategy, product-roadmap, okrs |
| discovery-docs | `phase: discover` | user-persona, business-case |
| design-docs | `phase: develop` | wireframe, interactive-prototype |
| process-docs | `phase: iterate` | sprint-retrospective-notes, incident-postmortem |
| standing-standards | `classification: foundation` or `tool` | definition-of-done, runbook |
| communication-docs | `classification: utility` | status-report |

**A family contract may now gate a SET of axis values, not only one.** Ratifying the taxonomy exposed a
limitation in check K, which had shipped hours earlier ([PR #31](https://github.com/product-on-purpose/product-lifecycle-templates/pull/31),
D-C): it compared the axis to a single string. Two of the ratified families span two classification values,
so both would have failed. Axis coherence was always the claim that a family uses **one axis**, never one
value on it; the single-value comparison was an over-narrowing that went unnoticed because both existing
families happened to be single-valued. `FAMILY_CONTRACTS` entries now accept either a string or a list on
the axis key, exactly as `status` has since ADR 0020.

### Consequences

* Good: every Tier-1 family is coherent on one axis, so every member can declare honest metadata and check K
  can gate all of them. No contract needs a mixed-axis exception.
* Good: two families are removed from the plan rather than added. ops-docs dissolves, and `business-case`
  and `incident-postmortem` join families that already existed and were thin, so discovery-docs and
  process-docs both reach two members without new machinery.
* Good: the map's member count is **19**, independently reproducing the figure D-D reconciled from a
  different direction (27 Tier-1 types minus the 8 built). Two derivations agreeing is weak evidence, but it
  is better than one.
* Neutral: `standing-standards` groups a quality standard with an operational procedure. Coherent on the
  axis, mixed on domain; flagged above, revisited if the family grows.
* Bad: `kpi-dashboard` is still unresolved (`classification: utility` versus `phase: measure`). It is
  deliberately left to governance-docs' contract-writing step, where it is decided against real members
  rather than in advance. If it lands as `phase: measure`, governance-docs is a two-member family and
  kpi-dashboard moves, most likely to a measurement family or to communication-docs.
* Bad: three catalog-derived groupings in the build-out plan are now superseded. `buildout-plan.md`'s family
  table no longer matches this map, and is a dated projection rather than truth.

### Confirmation

The axis-set capability is enforced by check K in `tools/check-bundles.py` and covered by
`tools/test-check-k.py`, which runs in CI. Six assertions cover it specifically: a spanning family accepts
each of its allowed values, rejects a value outside the set with a message listing the set, and still
rejects a wrong axis. The test was mutation-checked by collapsing the value set to its first element, which
failed three assertions, so it is known to fail when the code is wrong.

Each family's taxonomy is finally confirmed when its contract is written against its real members, per the
ADR 0020 pattern. This ADR settles the shape; a contract settles the values.

## More Information

D-A and D-B were raised in [buildout-specs.md](../buildout-specs.md) during the build-out kickoff and are
marked resolved there, with this ADR as the record. D-C (check K's classification axis) landed separately;
D-D (the floor count reconciliation) is arithmetic, not a decision, and is recorded in the same file.

The options considered here, with their trade-offs and the reasoning behind each choice, are expanded in the
maintainer's decision-options record for this session (untracked, `_local/`).
