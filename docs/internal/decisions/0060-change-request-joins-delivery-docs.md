---
status: accepted
date: 2026-09-25
decision-makers: [jprisant]
consulted: [claude]
---

# `change-request` joins `delivery-docs`, and the family's membership test gains the verb "changes"

## TL;DR

- **Decision.** The `change-request` bundle declares **`family: delivery-docs`** and **`phase: deliver`**, and
  serves the **project and product baseline** sense of the type: a formal request to alter something already
  agreed about a unit of product work (its scope, requirements, acceptance criteria, or agreed schedule and
  cost), assessed and then approved, rejected or deferred by a named authority. The
  [contract](../contracts/delivery-docs.md) moves to `0.2.0`, together with
  [ADR 0059 (announcement-internal-comms joins delivery-docs)](0059-announcement-internal-comms-joins-delivery-docs.md).
- **Why this record is different from every earlier admission.** ADRs 0042, 0050, 0053, 0057 and 0058 each
  admitted a type that some contract's membership test **already** said yes to. **This one does not exist.**
  A research pass on 2026-09-25 tested a per-occasion change request against all nine contracts, and every
  one excluded it as written. Admitting it therefore **widens a membership test**, which is a contract change
  in substance, not a clarification.
- **What settled it.** `delivery-docs` is the smallest honest widening: its chain already carries one unit of
  product work from definition to delivery, and a change request is how that unit's agreed definition moves.
  The library's own routing already used the type in exactly this sense.
- **What this does NOT decide:** admission, which retrieval settled with the widest named-source base of any
  Tier-2 candidate (see [`tier2-specs.md`](../tier2-specs.md)); and the standing **change log**, a separate
  catalog candidate (`change-log-governance`) that this record neither builds nor places, beyond noting that
  `governance-docs` admits a standing register as written.
- **Status:** accepted 2026-09-25. The maintainer chose `delivery-docs` and the baseline lineage on
  2026-09-25, after the research, and accepted the record the same day after reading the contract diff,
  because a family contract is "adopted only after a maintainer read".

## Context and Problem Statement

Two shipped bundles send readers to a change request, and the library does not ship one:
`bug-report_guide.md` ("It is a request, not a defect. If nothing promised the behavior you want, that is a
change request."), and `issue-log`, whose full template links each issue to "a change request it raised".
A third, `test-plan`, uses the term in passing. *(GitHub issue #179 also named `release-notes_companion.md`;
it does not mention one.)*
The maintainer directed its build on 2026-09-24 under
[ADR 0041](0041-maintainer-preference-sets-the-build-order.md) (GitHub issue #179, build-candidate 5), with
the family left open.

Two questions had to be answered before the family could be.

**Which change request.** Two lineages share the name, and the readable sources support them about equally.
IT service management treats it as a request to change a running system: NIST SP 800-128 ships a sample
change request with a back-out plan and the configuration items affected, reviewed by a change advisory
board. Project management treats it as a request to change an agreed baseline: PMI's Lexicon defines it as
"A formal proposal to modify a document, deliverable, or baseline", and the European Commission's PM² guide
as a request to "amend an aspect of the agreed baseline of a project". **The library's routing had already
chosen the second**: a bug-report reader asking for behavior nothing promised is asking to change what the
PRD and acceptance criteria agreed, not to deploy a change to production.

**Which family.** Tested against all nine membership tests, with no family assumed:

| Contract | Why it excludes a per-occasion change request |
|---|---|
| `governance-docs` | Admits standing registers, and names "An event-driven or phase-bound artifact (an incident postmortem, a business case)" as out. A change request is filed once per change |
| `standing-standards` | "agreed once and applied every time"; its own text routes "a candidate written once per unit of work" to `delivery-docs` or `qa-docs` |
| `decision-docs` | "a technical decision-or-design artifact of the develop phase"; a baseline change is not a technical design choice |
| `delivery-docs` (as it stood at 0.1.3) | "defines, decomposes, verifies, or announces"; a change request does none of the four |
| `qa-docs` | Plans, specifies or reports a verification; a change request verifies nothing |
| `communication-docs`, `process-docs`, `discovery-docs`, `strategy-docs` | Summarizes for an outside audience; looks back; decides whether to build; sets direction. None fits |

## Decision Drivers

- **Do not bend a contract's identity to fit one type.** `governance-docs` admitted `issue-log` two days
  earlier ([ADR 0057](0057-issue-log-joins-governance-docs-as-a-fourth-member.md)) precisely because it is a
  standing instrument, and `utility` would misdescribe a per-occasion form.
- **Prefer the smallest widening**, and state it as a widening rather than a reading.
- **Follow the library's own routing and audience**: product management and software delivery, not IT
  operations.

## Considered Options

1. **Widen `delivery-docs` with a fifth verb, "changes".** Chosen.
2. **A new one-member family** for per-occasion decision-control requests, with its own contract and check K
   entry, on the `communication-docs` precedent. Cleaner boundary; more machinery for one type, and a family
   drawn around a single document invites the question that contract had to answer about itself.
3. **Widen `governance-docs`** to admit the per-occasion forms that feed its registers. Rejected: it inverts
   the membership test that admitted `issue-log`, and `classification: utility` would misdescribe the type.
4. **Build the change log instead**, which `governance-docs` admits as written, with the request's fields as
   its row schema. Rejected: it builds a different document from the one three bundles route to, and two
   field-level sources (PM², CDC UP) keep the request form and the log as separate, linked artefacts.

## Decision Outcome

**Chosen: option 1.** The membership test becomes "defines, decomposes, verifies, changes, or announces a
unit of product work", and the chain sentence places the change request: it "alters what was agreed about
it once that agreement exists".

### What the widening admits, and what it does not

The contract states the boundary so the new verb cannot become a door for everything with "change" in its
name. It admits a document that proposes altering an **agreed unit of product work**. It does **not** admit:

- **A change to a running production system.** IT service change enablement is a real, well-sourced practice
  with its own vocabulary (standard, normal and emergency changes; a change authority), and this library
  names it as the bundle's closest neighbour rather than templating it. DORA's research is part of why it
  stays a neighbour and not a variant: its 2019 report found that requiring approval from "an external body
  such as a change advisory board (CAB) or a senior manager" had "a negative impact on software delivery
  performance".
- **The standing change log.** A register of requests is a standing instrument; if it is ever built, it is a
  `governance-docs` candidate as written.

### Consequences

- **The contract moves to `0.2.0`** (with ADR 0059), with the widening recorded in its change note and the
  boundary above in section 1. Check K's registry entry needs no edit: the member declares `phase: deliver`.
- **The catalog entry must be corrected when the bundle lands**, per
  [procedure 1](../decision-procedures.md#1-a-catalog-call-loses-to-research): it frames the type as IT
  service change ("Formally request and authorize a production change", owner Change Manager, related to CAB
  review, methodology ITIL). Its alias `RFC (ITIL)` collides with this library's shipped `rfc` bundle (a
  request for comments), and the bundle must name that collision on its first line rather than inherit it.
- **The example chains onto the delivery-docs scenario, not the governance one.** The Saved Views PRD lists
  scheduled delivery "by email or Slack" as a non-goal and "likely a fast follow", which is exactly what a
  change request against an agreed baseline looks like. `issue-log`'s example states that neither of its two
  canonical issues raised a change request, so the new example must not attach one to them.
- **The agile position is part of the bundle, not an objection to it.** The 2020 Scrum Guide routes change
  through the Product Backlog: "Those wanting to change the Product Backlog can do so by trying to convince
  the Product Owner." A team working that way needs no change request, and the guide's When NOT to use must
  say so; the audience is work where an agreed baseline has contractual, regulatory or budget weight.
- **`pairs_with: []`.** No pm-skills skill produces or consumes a change request.

## More Information

- Family contract: [`delivery-docs`](../contracts/delivery-docs.md), adopted by
  [ADR 0020](0020-adopt-delivery-docs-family-contract.md); the previous amendment was
  [ADR 0042 (epic joins delivery-docs)](0042-epic-joins-delivery-docs.md).
- The exclusion this record could not use: [`governance-docs`](../contracts/governance-docs.md) section 1.
- The fork this record inherits: `tier2-specs.md`'s issue-log section, "The change-request fork, which also
  bears on build-candidate 5".
- The spec and the admission evidence: [`tier2-specs.md`](../tier2-specs.md).
