# Family Contract: delivery-docs

Status: adopted 2026-07-20 ([ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md); fulfills plan AC-12 and design spec section 11; audit finding B-01)
Applies to: every bundle declaring `family: delivery-docs` in its meta
Members at adoption: prd, user-stories, acceptance-criteria, release-notes
Modeled on: the pm-skills family-contract pattern
Version: 0.2.0 (changes to this contract require a decision record; see the change note at the end)

## 1. Membership

A bundle belongs to this family when its document type is a delivery-chain artifact: it defines, decomposes, verifies, changes, or announces a unit of product work. This library treats the family's artifacts as forming a traceable chain that carries one unit of product work from definition to delivery: a PRD or a Product Backlog opens it (the family's own research into the Scrum Guide found that Scrum recognizes no PRD at all and routes requirement capture through the Product Backlog instead, so which one opens the chain depends on methodology), an epic groups a body of work large enough to need decomposing before it can be worked, user stories and the Sprint Backlog decompose and sequence it, acceptance criteria confirm it, a change request alters what was agreed about it once that agreement exists, a release note records and announces what changed, and an internal announcement tells the people who did not do the work what the change means for them and what they must do, and each member must state its position in that chain in its companion's Relationships section.

**What "changes" admits, and what it does not** (added in 0.2.0, [ADR 0060](../decisions/0060-change-request-joins-delivery-docs.md)). The verb admits a document that proposes altering an **agreed unit of product work**: its scope, requirements, acceptance criteria, or the schedule and cost agreed for it. It does not admit a change to a running production system (IT service change enablement, reviewed by a change advisory board), which this library names as a neighbour and does not template, and it does not admit the standing register of such requests (a change log), which is a `governance-docs` instrument if it is ever built.

## 2. Required catalog metadata and allowed values

Every member's `<type>_meta.yaml` carries the full field set defined by the metadata schema (methodology B5; machine-metadata spec once adopted), with these family-specific constraints:

| Field | Allowed values for this family |
|---|---|
| family | `delivery-docs` |
| phase | `deliver` (if a candidate member's phase differs, it belongs in another family) |
| methodology | **Descriptive, not gated (amended 2026-07-20, see change note).** Each member declares the methodology it honestly leans on (`generic`, `agile-scrum-xp`, `agile-bdd`, `methodology-agnostic`, ...). Some delivery artifacts are inherently methodology-bound (a user story is an agile/XP form), so a single required value would be a fiction. Methodology-specific *collections* (a Scrum pack, an XP pack) are a future **Tier-2** concept, a separate family, not a variant of a member here. |
| sizes_available | `[lean, full]`, or `[lean]` for types the catalog marks single-size |
| status | `beta` until the maintainer judges the bundle settled; then `stable` eligible ([ADR 0055](../decisions/0055-retire-the-zero-fills-disclosure.md)) |
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

**0.2.0 (2026-09-25, [ADR 0059](../decisions/0059-announcement-internal-comms-joins-delivery-docs.md) and [ADR 0060](../decisions/0060-change-request-joins-delivery-docs.md)):** two members admitted in one amendment, and **one of them widens the membership test**, which no earlier change to this contract did.

- **`change-request` (ADR 0060) needed a new verb.** A 2026-09-25 research pass tested a per-occasion change request against all nine family contracts and **every one excluded it as written**; the closest, `governance-docs`, names "an event-driven or phase-bound artifact" as out of its family. This contract is the smallest honest home: the type proposes altering an agreed unit of product work, which is the chain this family already carries. Tested against research rather than asserted, per [procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world): PMI's *Lexicon of Project Management Terms* (v5.0, fetched and raw-checked) defines a change request as "A formal proposal to modify a document, deliverable, or baseline", and the European Commission's PM² guide (CC BY 4.0) defines one as a request to "amend an aspect of the agreed baseline of a project". The library's own routing already used the type in this sense: `bug-report_guide.md` sends a request for behavior nothing promised to "a change request".
- **`announcement-internal-comms` (ADR 0059) needed no new verb.** The membership test already admitted it ("announces a unit of product work"). What needed a record is the chain sentence, which enumerates positions and which the 0.1.2 note established a member may not be missing from: the release note records and announces what changed, and the internal announcement tells the people who did not do the work what it means for them and what they must do. **The line is drawn by purpose, not audience**, because `release-notes_companion.md` already recommends shipping the full notes internally; a split by audience would contradict a shipped bundle. That split is this library's own boundary, drawn from the research rather than quoted from it.
- **No obligation changed**, and check K's registry entry needs no edit: both members declare `phase: deliver`, which is what the check gates.

**0.1.3 (2026-09-01, [ADR 0042](../decisions/0042-epic-joins-delivery-docs.md)):** admitted `epic` as the family's seventh member and placed it in the section 1 chain sentence, between the artifact that opens the chain and the stories that decompose it. The membership test in section 1 already admitted it; what required a record was the chain sentence, which enumerates positions and which the 0.1.2 note established a member may not be missing from. **No obligation changed**, and no gate changed: `epic` is validated by check K against the same section 2 values as every other member. Tested against research already in this repository rather than newly asserted, per [procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world): `sprint-backlog_research-log.md` entry 10 (Pichler, fetched and verified) fixes the position, *"I first select the goal. Then I explore which epics have to contribute to it, and I break out small detailed stories from the epics"*, and `product-backlog_research-log.md` entries 31 and 32 (Atlassian and Microsoft, both fetched and verified) support the grouping relation.

**Corrected in the same pass, 2026-09-01:** the version field in this file's header read `0.1.1` while the note below documented a `0.1.2` revision, so the header had been stale since 2026-08-07. The field is now `0.1.3`. Nothing about the 0.1.2 change was wrong; only the header failed to move with it. No check reads a contract's version field, which is the same ungated-document drift that left `STATE.md`'s "Last updated" ten days behind its own content.

**2026-08-07, research confirmation and correction**, per
[procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world). This contract's assertions about the world were tested against the research logs of the members
actually built. One was unsupported and is corrected in place; **no obligation changed**.

**0.1.2 (2026-08-07):** corrected the membership section's chain claim under decision procedure 11 (docs/internal/decision-procedures.md, "A family contract asserts something about the world"). The 0.1.1 text asserted "a PRD leads to user stories, which lead to acceptance criteria, which ship in a release note." No research log supports that four-step sequence, and the family's own research contradicts it: prd_research-log.md entry 1 (Scrum Guide 2020, fetched and verified) and prd_companion.md section 5 both state Scrum recognizes no PRD at all and routes requirement capture through the Product Backlog; user-stories_research-log.md entry 8 confirms stories are Product Backlog items, not PRD output. The sentence also omitted product-backlog and sprint-backlog, two of the family's six declared members, leaving them outside the sentence that justifies membership. Rewritten as this library's own position on how the six members chain, naming the methodology-dependent entry point. No obligation changed: members still declare their position in the chain in the companion's Relationships section.


**0.1.1 (2026-07-20, [ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md)):** adopted (was "draft for adoption") and enforced by new gate check K. Two corrections were made in the same pass. The enforcement letter was **M** in the 0.1.0 draft, a forward-guess made before the gate alphabet was settled; the family check landed at **K** (the next free letter after J, the metadata schema), and the reference is corrected. And the `methodology` field, which the 0.1.0 draft required to be `generic`, is now descriptive: on first enforcement, check K found that three of the four members honestly declared methodology-specific values (`agile-scrum-xp`, `agile-bdd`, `methodology-agnostic`), because some delivery artifacts are inherently methodology-bound. Forcing `generic` would have made the metadata less true, so the constraint was dropped rather than the values changed.
