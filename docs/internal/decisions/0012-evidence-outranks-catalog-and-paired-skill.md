---
status: accepted
date: 2026-07-14
decision-makers: [jprisant, claude]
---

# Primary evidence outranks the catalog and the paired skill; conflicts are reported, not absorbed

## Context and Problem Statement

Authoring a bundle means reconciling three inputs that were never checked against each other:

1. **The master catalog** (`_local/initial-discovery/docs/deep-research_master-catalog.md`), which seeds every bundle with a doc-type spine, aliases, canonical sections, and a size call.
2. **The paired skill** in pm-skills, named in the bundle's `pairs_with`, which generates the artifact interactively and ships its own template.
3. **Primary evidence** about the document type: the originating source, the maintained standard, the live practitioner literature.

For the four `delivery-docs` bundles these never collided, so the precedence question never came up. Building the ADR bundle collided with two of them at once.

**Collision one, the catalog.** Catalog entry 64 marks the ADR **"S only"**, a single-size type. But MADR, the maintained standard for the format, ships a *minimal* template and a *full* template as two separate files. That is not an outside opinion about MADR; it is MADR's own maintainers declaring that the type comes in two weights.

**Collision two, the paired skill.** `pairs_with: [develop-adr]` resolves to a real skill, and that skill's bundled template follows **Nygard's** 2011 format. This organization, however, standardized on **MADR v4** for its own decision records: `jp-init-project` mandates `docs/internal/decisions/`, [0011](0011-madr-v4-at-docs-internal-decisions.md) adopted it here, and `agent-config-toolkit` and `thinking-framework-skills` both run it. So the skill and the org convention disagree, and a template that paired naively with the skill would emit records that violate the conventions of the very repos it is meant to serve.

The library needs a precedence rule. Without one, the answer to "which input wins" is decided fresh, and differently, by whoever authors the next bundle.

## Decision Drivers

* **The library's whole claim is that its content is researched rather than asserted.** An input that primary evidence contradicts cannot be allowed to win merely because it is upstream in the workflow.
* **A template must not manufacture the drift it exists to prevent.** This is the knockout criterion. A template that produces artifacts violating the adopting org's own conventions is worse than no template.
* **The catalog is a research artifact, not a specification.** It was produced by a deep-research pass, and nothing has ever verified it claim by claim.
* **Do not silently edit your neighbors.** This repo does not own pm-skills. Reaching across and "fixing" a sibling repo from inside a template-authoring task is how coordinated systems quietly desynchronize.

## Considered Options

* **Option A:** Primary evidence and the standing org convention win. Conflicts with the catalog and the paired skill are recorded as findings and reported to their owners.
* **Option B:** The catalog and the paired skill win. They are the upstream spec; conform to them and note the disagreement in the companion.
* **Option C:** Evidence wins, and the author immediately fixes the catalog and the sibling skill in the same change.

## Decision Outcome

Chosen option: **A. Evidence and the org convention win; the conflict is reported, not absorbed and not unilaterally patched.**

Concretely, as applied to this bundle:

- The ADR ships **`lean` + `full`**, overturning the catalog's "S only" call, on MADR's own two-template evidence.
- The ADR template follows **MADR v4**, not the paired skill's Nygard format, because MADR is what the org's tooling and conventions expect. `adr_guide.md` carries a one-to-one Nygard-to-MADR mapping table, so the skill's output still transfers into the template without loss and the pairing stays usable.
- Both conflicts are filed as findings **EC-1** (the `develop-adr` format divergence) and **EC-2** (the catalog's wrong size call) in `STATE.md`, owned by the maintainers of those artifacts.

Option B fails the knockout driver outright. Conforming to the skill would make this library ship a template whose output violates `jp-init-project`'s own rule, which is the precise failure the library exists to prevent. "The spec said so" is not a defense a researched library gets to use, and conforming while grumbling in the companion is the worst of both worlds: wrong artifact, plus a paper trail proving we knew.

Option C is the tempting one and it is wrong on ownership, not on correctness. The catalog fix and the skill fix are both probably right. But a bundle-authoring task that reaches into a sibling repository and rewrites it is an unreviewed cross-repo change smuggled inside unrelated work. The finding is the deliverable; the fix belongs to the artifact's owner, on their own review.

### Consequences

* Good, because the precedence question is now answered once instead of being re-decided per bundle.
* Good, because building a bundle becomes an **audit of its inputs**. EC-2 is the proof: one of the 27 Tier-1 catalog entries has now been checked against primary evidence and did not survive. That is a finding the library produced about itself, which is what a governed library is for.
* Good, because sibling repos keep sovereignty over their own contents. Findings arrive as reports their maintainers can reject.
* Bad, because **the catalog's authority is now formally downgraded**, and that has a cost beyond this one entry. The other 26 Tier-1 size calls are unverified hypotheses, and every one of them is now suspect until a bundle is built against it. This decision does not create that problem, but it is the first record to admit it.
* Bad, because reported findings can rot. EC-1 and EC-2 are open items in another team's queue with no SLA, and a finding nobody actions is indistinguishable from a finding nobody filed. The mitigation is that `STATE.md` carries them where they are visible, but the honest position is that this converts a code problem into a coordination problem, and coordination problems are harder.
* Accepted cost: a bundle may now legitimately disagree with the catalog that seeded it. Anyone reading a bundle's meta against the catalog will find mismatches, and must consult the bundle's `history.md` and research log to learn which is right. The bundle is the authority; the catalog is the hypothesis.

### Confirmation

Not automatable today, and saying so plainly is more useful than pretending otherwise. Nothing in the gate compares a bundle's `sizes_available` against its `catalog_ref`, and nothing verifies a `pairs_with` target's format. Both are human-verified at authoring time.

The enforceable half is that every such conflict must appear in two places before a bundle ships: the bundle's own `research-log.md` (under "Findings that changed the bundle") and the findings table in `STATE.md`. A conflict resolved silently, in either direction, is a review failure. Adding a machine check for catalog-versus-meta drift is a candidate for roadmap **WP-11 (gate hardening)**.

## More Information

Depends on [0011](0011-madr-v4-at-docs-internal-decisions.md), which established the MADR v4 convention that collision two is measured against, and which set the precedent of naming an error rather than quietly rewriting it. This record extends that instinct from *our own past records* to *our upstream inputs*.

Interacts with **TX-1** in `STATE.md` (does this library need a second taxonomy axis?). Both are cases of the library discovering that an inherited assumption does not survive contact with the evidence. Expect more.

Revisit if the catalog is ever verified entry by entry, at which point it earns a stronger claim on authorship than "hypothesis," or if the `develop-adr` skill converges on MADR, which would dissolve collision two entirely.
