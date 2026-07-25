# Family Contract: qa-docs

Status: adopted 2026-07-25 ([ADR 0026](../decisions/0026-adopt-qa-docs-family-contract.md))
Applies to: every bundle declaring `family: qa-docs` in its meta
Members at adoption: none built yet (test-plan, test-case, bug-report are the planned members)
Modeled on: the delivery-docs, decision-docs and governance-docs family contracts, on the pm-skills family-contract pattern
Axis: `phase` (`develop`); see section 2 for why this family is not on the `classification` axis
Version: 0.1.0 (changes to this contract require a decision record; see the change note at the end)

## 1. Membership

A bundle belongs to this family when its document type is a **verification artifact of the develop phase**: it plans the verification of a product increment, specifies one unit of that verification, or reports a verification that failed. The family's three roles are sequential rather than alternative, and that sequence is its teaching value:

- a **test plan** defines the scope, approach, and entry/exit criteria for verifying a release or feature, before the testing is done;
- a **test case** specifies one executable verification (preconditions, steps and data, expected result), the unit the plan schedules;
- a **bug report** records one verification that failed, with the reproduction and severity an engineer needs to act on it.

Each member must state its position against the other two in its companion's Relationships section, and must also state its position against **acceptance criteria** (the `delivery-docs` member), because that is the sharpest and most common confusion this family exists to resolve. Acceptance criteria are the story-level contract of doneness, agreed with the business before work starts; a test case is the executable verification of behavior, which typically derives from acceptance criteria but extends past them into negative, boundary, and regression cases the criteria never named. A member that treats the two as synonyms is out of contract even if every file exists.

A candidate type whose job is not to plan, specify, or report the verification of a product increment belongs in another family. In particular, an artifact about a **failure in production** rather than in verification (an incident postmortem) is not a qa-docs member: it is event-driven learning after release, which [ADR 0023](../decisions/0023-resolve-the-tier-1-family-taxonomy.md) assigned to `process-docs` at `phase: iterate`.

## 2. Required catalog metadata and allowed values

Every member's `<type>_meta.yaml` carries the full field set defined by the [metadata schema](../../../tools/meta.schema.json) (methodology B5), with these family-specific constraints:

| Field | Allowed values for this family |
|---|---|
| family | `qa-docs` |
| phase | `develop` (if a candidate member's phase differs, it belongs in another family). This family declares `phase`, not `classification`; see the axis note below. |
| methodology | **Descriptive, not gated** (the [ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md) lesson, carried forward). All three planned members are expected to declare `generic`, since a test plan, a test case, and a bug report are methodology-agnostic instruments, but a future member is free to declare otherwise rather than have the truth bent to a rule. |
| sizes_available | `[lean, full]`, or `[lean]` for a type whose own research shows it does not earn a second weight. The catalog marks entry 102 `M/L` and entries 104 and 107 `S`, but those calls are hypotheses, not facts (finding EC-2 in `STATE.md`), and each member settles its own size contract against evidence at build time. |
| status | `beta` until one real usage cycle is recorded; then `stable` eligible |
| pairs_with | the pm-skills skill ID(s) this template serves, or `[]`; every value must resolve against the pinned skill-ID list. **pm-skills ships no testing or QA skill** (finding EC-4 in `STATE.md`, verified 2026-07-25 across all 68 tracked skills), so the only honest pairing available today is [`deliver-edge-cases`](https://github.com/product-on-purpose/pm-skills/blob/main/skills/deliver-edge-cases/SKILL.md), whose own description names "during QA planning to identify boundary and limit scenarios to test" and "when preparing QA test plans" as its use. A member claims it only where that claim is true of that member; the rest declare `[]`. |

**The axis call, made at contract time against the real members.** [`buildout-specs.md`](../buildout-specs.md) marked this family `phase: develop` with the flag *TBD (QA may be utility)*. It is resolved here as **`phase: develop`**, on the merits of the three members:

- **None of the three is a standing instrument.** The `classification` axis describes a document that is set up once and maintained indefinitely across the lifecycle, which is what earned `governance-docs` its `classification: utility` ([ADR 0024](../decisions/0024-adopt-governance-docs-family-contract.md)). A test plan is written per release and closed at its exit criteria; a test case is authored once for one behavior; a bug report is opened, triaged, and closed. Each is produced at a stage and finished, which is the definition of a `phase` artifact.
- **Being an instance artifact does not make a type standing, and it does not make it phase-less either.** This objection was already settled by `decision-docs`: an ADR is one-per-decision and event-driven, and it is `phase: develop`. What the axis records is where the type is authored in the lifecycle, not how long the artifact is read afterward. A regression suite is re-run for years, exactly as an ADR is read for years; the test case is still written during develop.
- **The stage evidence is in the machine data, not in this contract's judgment.** All three carry the same catalog `stage` value, `testing/QA` (entries 102, 104, 107). A family whose members already share one stage in the catalog is the clearest case of phase coherence the build-out has met.

**Two families may share a phase value.** `decision-docs` is also `phase: develop`. This is not a collision: `phase` and `family` are separate fields, check K gates per declared family, and the two membership rules do not overlap (a test plan neither proposes, records, nor describes a technical decision). Phase coherence is a rule about a family's internal consistency, never a claim that a family owns a phase.

## 3. Structural obligations (gate-checkable)

1. **The eight files.** Every member ships all eight roles: template-lean, template-full (where two sizes exist), companion, guide, example, meta.yaml, history, research-log; filenames prefixed `<type>_`.
2. **Nesting.** Where two sizes exist, the lean variant's H2 sections are a strict ordered subset of the full variant's; shared sections keep name and order. Single-size members are exempt from nesting, not from anything else.
3. **Guidance comments.** Every section of every variant carries the Approach A comment (WHAT, WHY with a companion pointer, ASK, GOOD, WEAK, TRAP; PRIORITY and ROW HINT for table sections), parseable under the comment grammar. A "How to fill this in" preamble opens each variant. Two of the three members are step-and-table artifacts (test steps, defect fields), so ROW HINT discipline carries real weight here.
4. **Companion skeleton.** All 11 sections of methodology section 5, in order; an inapplicable section says so in one line rather than being dropped.
5. **Guide shape.** When to use; when NOT to use; pick a variant; a self-gradable quality rubric; at least two named anti-patterns.
6. **Citations.** Methodology section 6 in full: numbered, reliability-tagged, anchored, hyperlinked, cited inline, no padded entries, retrieval qualifiers on any source not directly fetched. This family has one live standards-recency trap: **IEEE 829 is superseded by ISO/IEC/IEEE 29119-3** (catalog entry 102), so a member citing 829 as current practice is citing a superseded standard. Its exact status and date are to be verified against the standards bodies by the member that cites it, not inherited from the catalog.
7. **Example.** One fully worked instance, no placeholders, illustrative figures labeled, provenance frontmatter stamped.

## 4. The shared-scenario rule (family-specific)

Like `delivery-docs` and `governance-docs` and unlike `decision-docs`, `qa-docs` members **chain their examples on one shared scenario**, because the three roles compose on a single feature rather than standing as alternatives: the plan schedules the case, and the case that fails produces the report.

This family carries the rule one step further than its predecessors. Its examples chain **onto the existing `delivery-docs` thread** rather than onto a new scenario: Acme Analytics' "Saved Views for Dashboards" feature, whose PRD, user stories, and acceptance criteria are already worked examples in this repository. The reason is section 1's boundary. The acceptance-criteria-versus-test-case distinction cannot be taught in the abstract; it is taught by showing the actual acceptance criteria for "set a default saved view" beside the actual test cases derived from them, and then showing which test cases exist that no acceptance criterion called for. A member whose example invents an unrelated feature forfeits that, and is out of contract even if every file exists.

The chain a reader should be able to follow end to end: PRD to user story to acceptance criteria (`delivery-docs`), then to test plan to test case to bug report (`qa-docs`). Where a member's example points back across the family boundary, it links to the real file.

## 5. Shareable-boundary rule

Template body (headings, placeholders, tables) is the reusable shape; guidance lives only in comments; example content never leaks into templates; meta describes the asset, never the filled instance. A member whose guide has grown explanatory (companion material) or whose companion has grown procedural (guide material) is out of contract even if every file exists.

## 6. Enforcement

The gate enforces section 2 and the mechanical part of section 3. **Family check letter K** validates section 2's family-specific values for every declared member (`phase: develop`, a `beta`/`stable` status, and a `[lean, full]` or `[lean]` size shape) and that this contract file resolves; methodology is descriptive and is not gated (see section 2). A member declaring `classification: utility` instead of `phase: develop` fails check K with a message naming the axis it should have used, because the check reads whichever axis the contract names ([ADR 0023](../decisions/0023-resolve-the-tier-1-family-taxonomy.md)). Of section 3's obligations, the eight files (3.1), nesting (3.2), citations (3.6), and the clean example (3.7) are enforced by checks A, C, E, and D respectively; guidance comments (3.3), the companion skeleton (3.4), and guide shape (3.5) have no mechanical check yet and are review obligations at authoring time. Sections 4 and 5 are likewise review obligations at authoring time and audit obligations thereafter. A member failing this contract is not "in the family with issues"; it is out of the family until green, and the catalog count reflects that.

## Change note

**0.1.0 (2026-07-25, [ADR 0026](../decisions/0026-adopt-qa-docs-family-contract.md)):** adopted, enforced by gate check K, the fourth family contract after `delivery-docs`, `decision-docs`, and `governance-docs`. Adopted before any member is built (contract-first, per the build-out plan and the ADR 0020 pattern), so the contract describes the set its three planned members must join rather than one that already exists. Methodology descriptive from the start. The axis question [`buildout-specs.md`](../buildout-specs.md) flagged as *TBD (QA may be utility)* is settled here as `phase: develop` (see section 2), which makes this the second family on that phase value and the first cross-family example chain (section 4).
