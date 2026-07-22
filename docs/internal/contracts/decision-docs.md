# Family Contract: decision-docs

Status: adopted 2026-07-21 ([ADR 0022](../decisions/0022-adopt-decision-docs-family-contract.md))
Applies to: every bundle declaring `family: decision-docs` in its meta
Members at adoption: rfc, adr, sdd
Modeled on: the delivery-docs family contract (the first adopted), on the pm-skills family-contract pattern
Version: 0.1.0 (changes to this contract require a decision record; see the change note at the end)

## 1. Membership

A bundle belongs to this family when its document type is a **technical decision-or-design artifact of the develop phase**: it proposes a technical decision, records one, or describes the design that implements it. The family's three roles are distinct and complementary:

- an **RFC** proposes a decision and gathers feedback, before the decision is made;
- an **ADR** records a decision and its consequences, after it is made and immutably;
- an **SDD** (software design document) describes how a system will be built.

Each member must state its position against the other two in its companion's Relationships section, because the most common real-world failure around these artifacts is conflating them (writing an RFC and calling it a design doc, or burying an architecturally significant decision in a design doc instead of recording it as an ADR). A candidate type whose job is not to propose, record, or describe a technical decision or design belongs in another family.

## 2. Required catalog metadata and allowed values

Every member's `<type>_meta.yaml` carries the full field set defined by the [metadata schema](../../../tools/meta.schema.json) (methodology B5), with these family-specific constraints:

| Field | Allowed values for this family |
|---|---|
| family | `decision-docs` |
| phase | `develop` (if a candidate member's phase differs, it belongs in another family) |
| methodology | **Descriptive, not gated** (the delivery-docs / [ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md) lesson, adopted here from the start). Each member declares what it honestly leans on; all three current members are `generic` (an RFC, an ADR, and a design doc are methodology-agnostic instruments), but a future member is free to declare otherwise rather than have the truth bent to a rule. |
| sizes_available | `[lean, full]`, or `[lean]` for a type the catalog marks single-size |
| status | `beta` until one real usage cycle is recorded; then `stable` eligible |
| pairs_with | the pm-skills skill ID(s) this template serves, or `[]`; every value must resolve against the pinned skill-ID list. Only `adr` pairs with a skill today (`develop-adr`); `rfc` and `sdd` are `[]` because no `develop-rfc` or `develop-sdd` skill exists (findings EC-3 and its sdd sibling in `STATE.md`). |

## 3. Structural obligations (gate-checkable)

1. **The eight files.** Every member ships all eight roles: template-lean, template-full (where two sizes exist), companion, guide, example, meta.yaml, history, research-log; filenames prefixed `<type>_`.
2. **Nesting.** Where two sizes exist, the lean variant's H2 sections are a strict ordered subset of the full variant's; shared sections keep name and order. Single-size members are exempt from nesting, not from anything else.
3. **Guidance comments.** Every section of every variant carries the Approach A comment (WHAT, WHY with a companion pointer, ASK, GOOD, WEAK, TRAP; PRIORITY and ROW HINT for table sections), parseable under the comment grammar. A "How to fill this in" preamble opens each variant.
4. **Companion skeleton.** All 11 sections of methodology section 5, in order; an inapplicable section says so in one line rather than being dropped.
5. **Guide shape.** When to use; when NOT to use; pick a variant; a self-gradable quality rubric; at least two named anti-patterns.
6. **Citations.** Methodology section 6 in full: numbered, reliability-tagged, anchored, hyperlinked, cited inline, no padded entries, retrieval qualifiers on any source not directly fetched.
7. **Example.** One fully worked instance, no placeholders, illustrative figures labeled, provenance frontmatter stamped.

## 4. The distinct-jobs rule (family-specific)

Unlike the `delivery-docs` family, whose members chain on one shared scenario to demonstrate traceability, `decision-docs` members' examples are **deliberately independent**, each a different real decision or design, because the family's teaching value is the *distinction* between the three roles rather than a single thread running through them. RFC-0001 is a real (accepted) proposal in this repo, the ADR examples are real repository decisions, and the SDD example is a worked design. What the family requires instead is a **cross-reference rule**: each member's companion must correctly place it against the other two (RFC proposes, ADR records, SDD describes), and must not overstate the boundaries (much of the industry uses "RFC" and "design doc" interchangeably, which is honest; only the ADR is categorically distinct). An accepted RFC's outcome is what an ADR is written from; a significant decision inside an SDD belongs also in an ADR. A member that blurs these roles is out of contract even if every file exists.

## 5. Shareable-boundary rule

Template body (headings, placeholders, tables) is the reusable shape; guidance lives only in comments; example content never leaks into templates; meta describes the asset, never the filled instance. A member whose guide has grown explanatory (companion material) or whose companion has grown procedural (guide material) is out of contract even if every file exists.

## 6. Enforcement

The gate enforces section 2 and the mechanical part of section 3. **Family check letter K** validates section 2's family-specific values for every declared member (`phase: develop`, a `beta`/`stable` status, and a `[lean, full]` or `[lean]` size shape) and that this contract file resolves; methodology is descriptive and is not gated (see section 2). Of section 3's obligations, the eight files (3.1), nesting (3.2), citations (3.6), and the clean example (3.7) are enforced by checks A, C, E, and D respectively; guidance comments (3.3), the companion skeleton (3.4), and guide shape (3.5) have no mechanical check yet and are review obligations at authoring time. Sections 4 and 5 are likewise review obligations at authoring time and audit obligations thereafter. A member failing this contract is not "in the family with issues"; it is out of the family until green, and the catalog count reflects that.

## Change note

**0.1.0 (2026-07-21, [ADR 0022](../decisions/0022-adopt-decision-docs-family-contract.md)):** adopted, enforced by gate check K, the second family contract after `delivery-docs`. Adopted with methodology descriptive from the start, carrying forward the [ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md) lesson rather than re-learning it: a field that describes what a template leans on is not a membership criterion. The family grew to three members (`sdd` landed the same week as this contract) before the contract was written, so the contract describes a set that already exists rather than constraining one yet to be built.
