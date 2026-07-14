# Family Contract: delivery-docs

Status: draft for adoption (fulfills plan AC-12 and design spec section 11; audit finding B-01)
Applies to: every bundle declaring `family: delivery-docs` in its meta
Members at adoption: prd, user-stories, acceptance-criteria, release-notes
Modeled on: the pm-skills family-contract pattern
Version: 0.1.0 (changes to this contract require a decision record)

## 1. Membership

A bundle belongs to this family when its document type is a delivery-chain artifact: it defines, decomposes, verifies, or announces a unit of product work. The family's artifacts form a traceable chain (a PRD leads to user stories, which lead to acceptance criteria, which ship in a release note), and each member must state its position in that chain in its companion's Relationships section.

## 2. Required catalog metadata and allowed values

Every member's `<type>_meta.yaml` carries the full field set defined by the metadata schema (methodology B5; machine-metadata spec once adopted), with these family-specific constraints:

| Field | Allowed values for this family |
|---|---|
| family | `delivery-docs` |
| phase | `deliver` (if a candidate member's phase differs, it belongs in another family) |
| methodology | `generic` (methodology-specific delivery variants belong in Tier-2 packs, not this family) |
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

The gate enforces sections 2 and 3 mechanically (checks per the gate alphabet; family check letter M validates this contract's constraints for every declared member). Sections 4 and 5 are review obligations at authoring time and audit obligations thereafter. A member failing this contract is not "in the family with issues"; it is out of the family until green, and the catalog count reflects that.
