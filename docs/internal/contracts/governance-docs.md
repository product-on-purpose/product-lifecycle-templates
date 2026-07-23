# Family Contract: governance-docs

Status: adopted 2026-07-22 ([ADR 0024](../decisions/0024-adopt-governance-docs-family-contract.md))
Applies to: every bundle declaring `family: governance-docs` in its meta
Members at adoption: none built yet (risk-register, raid-log, kpi-dashboard are the planned members)
Modeled on: the delivery-docs and decision-docs family contracts, on the pm-skills family-contract pattern
Axis: `classification` (this is the first classification-axis family; see [ADR 0015](../decisions/0015-second-taxonomy-axis-phase-xor-classification.md) and [ADR 0023](../decisions/0023-resolve-the-tier-1-family-taxonomy.md))
Version: 0.1.0 (changes to this contract require a decision record; see the change note at the end)

## 1. Membership

A bundle belongs to this family when its document type is a **standing governance instrument**: a continuously-maintained register, log, or dashboard that a product or program manager uses to track risk, open items, or performance **across the whole lifecycle**, not as the output of one phase. This is why the family is `classification`-axis, not `phase`-axis: none of its members is produced at a single lifecycle stage and then finished. They are set up once and maintained indefinitely, which is what `classification: utility` means (a standing operational instrument, distinct from a `foundation` artifact that underpins the work and a `tool` that is executed procedurally).

The three planned roles are distinct but related, and their relationship is the family's teaching value:

- a **risk register** tracks risks alone (likelihood, impact, owner, response, status);
- a **RAID log** consolidates Risks, Assumptions, Issues, and Dependencies, so its Risks column is a superset-container around the risk register's whole subject;
- a **KPI dashboard** (as a document that *defines* the dashboard, not a live one) tracks performance against targets, a different subject from risk and open items.

Each member must state its position against the other two in its companion's Relationships section, because the most common real-world confusion here is running a standalone risk register and a RAID log that duplicate each other, or conflating a risk log with a performance dashboard. A candidate type whose job is not to stand up and maintain a governance instrument across the lifecycle belongs in another family. An event-driven or phase-bound artifact (an incident postmortem, a business case) does not, however operational it feels.

## 2. Required catalog metadata and allowed values

Every member's `<type>_meta.yaml` carries the full field set defined by the [metadata schema](../../../tools/meta.schema.json) (methodology B5), with these family-specific constraints:

| Field | Allowed values for this family |
|---|---|
| family | `governance-docs` |
| classification | `utility` (a standing operational instrument). This family declares `classification`, not `phase`; a candidate whose honest axis is `phase` (produced at one stage and finished) belongs in another family. See the kpi-dashboard note below. |
| methodology | **Descriptive, not gated** (the [ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md) lesson, carried forward). Each member declares what it honestly leans on; the register and log lean PMBOK/methodology-agnostic, the dashboard is methodology-agnostic (NSM/OKR-derived), but a future member may declare otherwise rather than have the truth bent to a rule. |
| sizes_available | `[lean, full]`, or `[lean]` for a type the catalog marks single-size |
| status | `beta` until one real usage cycle is recorded; then `stable` eligible |
| pairs_with | the pm-skills skill ID(s) this template serves, or `[]`; every value must resolve against the pinned skill-ID list. No governance skill exists in pm-skills today, so members adopt `[]` until one does. |

**The kpi-dashboard axis call, made at contract time against the real members ([ADR 0023](../decisions/0023-resolve-the-tier-1-family-taxonomy.md) deferred it here).** A KPI dashboard is `classification: utility`, not `phase: measure`. The catalog (entry 139) marks it "measurement / ongoing," a standing instrument maintained continuously, and it sits beside the risk register and RAID log as an always-on governance surface rather than a deliverable produced once at a measure phase. Declaring it `phase: measure` would misstate what it is to keep it in a phase family it does not belong to. If a future measurement family with genuinely phase-bound members is built, that is where a phase-axis metrics artifact would live; this dashboard is not one.

## 3. Structural obligations (gate-checkable)

1. **The eight files.** Every member ships all eight roles: template-lean, template-full (where two sizes exist), companion, guide, example, meta.yaml, history, research-log; filenames prefixed `<type>_`.
2. **Nesting.** Where two sizes exist, the lean variant's H2 sections are a strict ordered subset of the full variant's; shared sections keep name and order. Single-size members are exempt from nesting, not from anything else.
3. **Guidance comments.** Every section of every variant carries the Approach A comment (WHAT, WHY with a companion pointer, ASK, GOOD, WEAK, TRAP; PRIORITY and ROW HINT for table sections), parseable under the comment grammar. A "How to fill this in" preamble opens each variant. Governance members are table-heavy (risk rows, RAID quadrants, KPI rows), so ROW HINT discipline matters more here than in prose-heavy families.
4. **Companion skeleton.** All 11 sections of methodology section 5, in order; an inapplicable section says so in one line rather than being dropped.
5. **Guide shape.** When to use; when NOT to use; pick a variant; a self-gradable quality rubric; at least two named anti-patterns.
6. **Citations.** Methodology section 6 in full: numbered, reliability-tagged, anchored, hyperlinked, cited inline, no padded entries, retrieval qualifiers on any source not directly fetched.
7. **Example.** One fully worked instance, no placeholders, illustrative figures labeled, provenance frontmatter stamped.

## 4. The shared-scenario rule (family-specific)

Like `delivery-docs` and unlike `decision-docs`, `governance-docs` members **chain their examples on one shared project scenario**. The reason is the inverse of decision-docs': there the teaching value is the *distinction* between three mutually-exclusive roles, so the examples are deliberately independent; here the members genuinely *overlap on the same project*, and showing them together is what teaches the relationship. The same project's top risks should appear as the Risks (R) quadrant of that project's RAID log, and that project's KPI dashboard should track the health of the very thing those risks threaten. A reader who sees one project's risk register, RAID log, and dashboard side by side learns why you do not maintain a standalone risk register *and* a RAID log (the register is the RAID's R), and why the dashboard is a different instrument, not a fourth column. A member whose example invents an unrelated scenario is out of contract even if every file exists.

## 5. Shareable-boundary rule

Template body (headings, placeholders, tables) is the reusable shape; guidance lives only in comments; example content never leaks into templates; meta describes the asset, never the filled instance. A member whose guide has grown explanatory (companion material) or whose companion has grown procedural (guide material) is out of contract even if every file exists.

## 6. Enforcement

The gate enforces section 2 and the mechanical part of section 3. **Family check letter K** validates section 2's family-specific values for every declared member (`classification: utility`, a `beta`/`stable` status, and a `[lean, full]` or `[lean]` size shape) and that this contract file resolves; methodology is descriptive and is not gated (see section 2). This is the first family to be gated on the `classification` axis rather than `phase`; the check reads whichever axis the contract names ([ADR 0023](../decisions/0023-resolve-the-tier-1-family-taxonomy.md)), so a member that declares `phase: measure` instead of `classification: utility` fails check K with a message naming the axis it should have used. Of section 3's obligations, the eight files (3.1), nesting (3.2), citations (3.6), and the clean example (3.7) are enforced by checks A, C, E, and D respectively; guidance comments (3.3), the companion skeleton (3.4), and guide shape (3.5) have no mechanical check yet and are review obligations at authoring time. Sections 4 and 5 are likewise review obligations at authoring time and audit obligations thereafter. A member failing this contract is not "in the family with issues"; it is out of the family until green, and the catalog count reflects that.

## Change note

**0.1.0 (2026-07-22, [ADR 0024](../decisions/0024-adopt-governance-docs-family-contract.md)):** adopted, enforced by gate check K, the third family contract after `delivery-docs` and `decision-docs` and the **first on the `classification` axis**. Adopted before any member is built (contract-first, per the build-out plan and the ADR 0020 pattern), so the contract describes the set its three planned members must join rather than one that already exists. Methodology descriptive from the start. The kpi-dashboard axis question, which [ADR 0023](../decisions/0023-resolve-the-tier-1-family-taxonomy.md) deferred to this contract, is settled here as `classification: utility` (see section 2).
