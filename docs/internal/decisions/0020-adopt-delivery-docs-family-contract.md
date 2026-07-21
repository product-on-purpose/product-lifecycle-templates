---
status: accepted
date: 2026-07-20
decision-makers: [jprisant]
consulted: [claude]
---

# Adopt the delivery-docs family contract, enforced by gate check K; methodology is descriptive, not a membership rule

## Context and Problem Statement

The `delivery-docs` family contract has existed as a complete document marked "draft for adoption"
([docs/internal/contracts/delivery-docs.md](../contracts/delivery-docs.md)): it defines what qualifies a
bundle as a family member, the family-specific metadata values its members must carry, structural
obligations, and review-time rules. Its own Enforcement section said the gate "enforces sections 2 and 3
mechanically" - but nothing did. That was a Definition-of-Done-style claim with no automation behind it,
the same shape of gap ADR 0014 (frontmatter YAML) and WP-10 (citations) each closed. Roadmap WP-24
adopts the contract and wires the enforcement.

Wiring the check surfaced a second problem. On its first run, the family check found that three of the
four members violated the contract's rule that `methodology` must be `generic`.

## Decision Drivers

- **A contract nobody enforces is a suggestion.** Family membership should be a mechanical gate, not an
  honor system, so a bundle that drifts out of the family is caught in CI.
- **The metadata must stay honest.** The values members carry (`phase`, `methodology`, and so on) should
  describe reality, not be bent to satisfy a rule.
- **Adding a family should not break the gate before that family has a contract.** decision-docs has no
  contract yet; its members must not fail a family check.

## Considered Options

For adoption: **wire a gate check (K)** that enforces the contract's mechanical constraints for declared
members.

For the methodology conflict the check surfaced:
* **Option A: make methodology descriptive, not a membership rule.** Drop it from the enforced
  constraints; each member declares what it honestly leans on. Chosen.
* **Option B: change the members to `methodology: generic`** to satisfy the contract as written.
* **Option C: allow a curated set of methodology values** and gate membership in the set.

## Decision Outcome

**Adopt the contract (status draft to adopted, version 0.1.1), enforced by new gate check K.** For every
bundle declaring `family: delivery-docs`, check K requires `phase: deliver`, a `beta` or `stable`
`status`, a size shape of `[lean, full]` or `[lean]`, and that the contract file resolves. A bundle in a
family with no ratified contract (decision-docs today) passes with a note. The check is pure standard
library and lands at letter **K**, the next free letter after J (the metadata schema); the draft's
Enforcement section had guessed "M" before the gate alphabet was settled, and that reference is corrected.

**Methodology is descriptive, not a membership rule (Option A).** Check K's first run found `user-stories`
declaring `agile-scrum-xp`, `acceptance-criteria` declaring `agile-bdd`, and `release-notes` declaring
`methodology-agnostic`; only `prd` was `generic`. These are honest: some delivery artifacts are inherently
methodology-bound (a user story is an agile/XP form, there is barely such a thing as a "generic user
story"). Forcing `generic` would have laundered true information out of the metadata to satisfy a rule, so
the rule was dropped, not the values. Membership is defined by the delivery-chain role and `phase:
deliver`, which every member genuinely shares.

Option B was rejected because it trades truthful metadata for uniformity, the wrong trade for a library
whose whole claim is honesty. Option C was rejected because it keeps methodology gated at the cost of a
standing curation chore (every new member with a new methodology edits the contract) for a field that is
descriptive anyway; the set would be an allow-list of adjectives.

**Location.** The contract stays at `docs/internal/contracts/delivery-docs.md`, where the repo's other
internal governance documents live. The roadmap's `_families/` path was a nod to pm-skills' layout;
relocating would be churn for no functional gain, since check K references the contract by a stable
tracked path either way.

### Consequences

* Good: family membership is enforced in CI. A delivery-docs bundle that drifts to the wrong phase,
  status, or size shape now fails the gate instead of quietly misrepresenting the family.
* Good: the metadata stays honest; a member says what it actually leans on.
* Neutral: methodology-specific **collections** (a Scrum pack, an XP pack, a SAFe pack) remain a reserved
  **Tier-2** direction, a separate future family with its own metadata, not built here and not blocked.
* Accepted cost: check K's constraints are declared per family in a small registry
  (`FAMILY_CONTRACTS`), currently only delivery-docs. A second family adds an entry; the check generalizes
  without new machinery.

### Confirmation

Enforced by check K in `tools/check-bundles.py`, run in CI by `.github/workflows/ci.yml`, with branch
protection on `main` requiring the `gate` job. Check K is the fitness function for this decision.

Adversarially tested at authoring time (2026-07-20): a delivery-docs member with the wrong `phase`, a
disallowed `status`, or a size shape outside `[lean, full]` / `[lean]` each fails check K with a located
message; a missing contract file fails; a bundle in a family with no contract (decision-docs) passes with
a note; and all four delivery-docs members conform, their differing `methodology` values correctly not
flagged. The gate is green at eleven checks on all six bundles.

## More Information

The contract's own change note (version 0.1.1) records the same amendment from the contract's side. This
is the first family contract adopted; `decision-docs` (rfc, adr) will get its own when the pair earns one.
The Tier-2 methodology-pack idea it reserves is tracked as a future direction, not scheduled work.
