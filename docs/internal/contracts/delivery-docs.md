# Family Contract: delivery-docs

Status: adopted 2026-07-20 ([ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md); fulfills plan AC-12 and design spec section 11; audit finding B-01)
Applies to: every bundle declaring `family: delivery-docs` in its meta
Members at adoption: prd, user-stories, acceptance-criteria, release-notes
Modeled on: the pm-skills family-contract pattern
Version: 0.1.1 (changes to this contract require a decision record; see the change note at the end)

## 1. Membership

A bundle belongs to this family when its document type is a delivery-chain artifact: it defines, decomposes, verifies, or announces a unit of product work. The family's artifacts form a traceable chain (a PRD leads to user stories, which lead to acceptance criteria, which ship in a release note), and each member must state its position in that chain in its companion's Relationships section.

## 2. Required catalog metadata and allowed values

Every member's `<type>_meta.yaml` carries the full field set defined by the metadata schema (methodology B5; machine-metadata spec once adopted), with these family-specific constraints:

| Field | Allowed values for this family |
|---|---|
| family | `delivery-docs` |
| phase | `deliver` (if a candidate member's phase differs, it belongs in another family) |
| methodology | **Descriptive, not gated (amended 2026-07-20, see change note).** Each member declares the methodology it honestly leans on (`generic`, `agile-scrum-xp`, `agile-bdd`, `methodology-agnostic`, ...). Some delivery artifacts are inherently methodology-bound (a user story is an agile/XP form), so a single required value would be a fiction. Methodology-specific *collections* (a Scrum pack, an XP pack) are a future **Tier-2** concept, a separate family, not a variant of a member here. |
| sizes_available | `[lean, full]`, or `[lean]` for types the catalog marks single-size |
| status | `beta` until one real usage cycle is recorded; then `stable` eligible |
| pairs_with | the pm-skills skill ID(s) this template serves, or `null`; every non-null value must resolve against the pinned skill-ID list |

## 3. Structural obligations (gate-checkable)

1. **The eight files.** Every member ships all eight roles: template-lean, template-full (where two sizes exist), companion, guide, example, meta.yaml, history, research-log; filenames prefixed `<type>_`.
2. **Nesting.** Where two sizes exist, the lean variant's H2 sections are a strict ordered subset of the full variant's; shared sections keep name and order. Single-size members are exempt from nesting, not from anything else.
3. **Guidance comments.** Every section of every variant carries the Approach A comment (WHAT, WHY with a companion pointer, ASK, GOOD, WEAK, TRAP; PRIORITY and ROW HINT for table sections), parseable under the comment grammar. A "How to fill this in" preamble opens each variant.
4. **Companion skeleton.** All 11 sections of methodology section 5, in order; an inapplicable section says so in one line rather than being dropped.
5. **Guide shape.** When to use; when NOT to use; pick a variant; a self-gradable quality rubric; at least two named anti-patterns (family practice is six).
6. **Citations.** Methodology section 6 in full: numbered, reliability-tagged, anchored, hyperlinked, cited inline, no padded entries, retrieval qualifiers on any source not directly fetched.
7. **Example.** One fully worked instance, no placeholders, illustrative figures labeled, provenance frontmatter stamped.

## 4. The shared-example rule (family-specific)

Members' examples chain on a common scenario so the family demonstrates traceability end to end: personas, scope, metrics, and open questions must be consistent across the family's examples, and each example links its upstream and downstream siblings. Amendment pending from the 2026-07-11 content review (CR-5): each example must either fully map its requirements to stories at Must/Should priority, or carry an explicit "representative, not exhaustive" note. A second-domain example set (content review CR-6 context, idea CT-1) extends a member without replacing the shared chain.

## 5. Shareable-boundary rule

Template body (headings, placeholders, tables) is the reusable shape; guidance lives only in comments; example content never leaks into templates; meta describes the asset, never the filled instance. A member whose guide has grown explanatory (companion material) or whose companion has grown procedural (guide material) is out of contract even if every file exists.

## 6. Enforcement

The gate enforces section 2 and the mechanical part of section 3. **Family check letter K** validates section 2's family-specific values for every declared member (`phase`, `status`, and size shape) and that this contract file resolves; methodology is descriptive and is not gated (see section 2). Of section 3's obligations, the eight files (3.1), nesting (3.2), citations (3.6), and the clean example (3.7) are enforced by checks A, C, E, and D respectively; guidance comments (3.3), the companion skeleton (3.4), and guide shape (3.5) have no mechanical check yet and are review obligations at authoring time. Sections 4 and 5 are likewise review obligations at authoring time and audit obligations thereafter. A member failing this contract is not "in the family with issues"; it is out of the family until green, and the catalog count reflects that.

## Change note

**0.1.1 (2026-07-20, [ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md)):** adopted (was "draft for adoption") and enforced by new gate check K. Two corrections were made in the same pass. The enforcement letter was **M** in the 0.1.0 draft, a forward-guess made before the gate alphabet was settled; the family check landed at **K** (the next free letter after J, the metadata schema), and the reference is corrected. And the `methodology` field, which the 0.1.0 draft required to be `generic`, is now descriptive: on first enforcement, check K found that three of the four members honestly declared methodology-specific values (`agile-scrum-xp`, `agile-bdd`, `methodology-agnostic`), because some delivery artifacts are inherently methodology-bound. Forcing `generic` would have made the metadata less true, so the constraint was dropped rather than the values changed.
