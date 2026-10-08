# Family Contract: experimentation-docs

Status: adopted 2026-10-08 ([ADR 0066](../decisions/0066-adopt-experimentation-docs-family-contract.md)); proposed 2026-10-06 and adopted after a maintainer read, per [decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer)
Applies to: every bundle declaring `family: experimentation-docs` in its meta
Members at adoption: none built yet (the catalog candidates `experiment-design-doc` and `experiment-readout-results-report` are the planned members; their bundle ids are fixed in their specs in [`tier2-specs.md`](../tier2-specs.md))
Modeled on: the qa-docs family contract, the closest existing family: a phase-bound pair that plans a test and then reports it
Axis: `phase` (`measure`); see section 2 for why this family is not on the `classification` axis
Version: 0.1.0 (changes to this contract require a decision record; see the change note at the end)

## 1. Membership

A bundle belongs to this family when its document type **plans or reports on one discrete test of a hypothesis about
the effect of a change to a product or its market**. Each member is written once per test, and it is finished when the
decision it exists to inform is recorded. The family's two roles are sequential rather than alternative, and that
sequence is its teaching value:

- an **experiment design doc** states the hypothesis, the variants, the population and allocation, the primary and
  guardrail metrics, the sample size or duration, and the decision rule, **before** the test runs;
- an **experiment readout** reports what ran, the results with their uncertainty, the validity checks, and the decision
  the results drove (ship, iterate or stop), **after** the test ends.

The verb list is "plans or reports on", not "plans, runs, or reports on". Running a test is an activity, and no source
in the 2026-10-05 research found a document that runs one. The finish line is the recorded decision, not the reading of
the result. That choice is the library's own POSITION: a decision can follow the result in a later meeting rather
than coincide with it.

Each member must state its position against the other member in its companion's Relationships section. It must also
state its position against two neighbours this family is most easily confused with, the way `qa-docs` members state
their position against acceptance criteria:

- the **spike report** (`decision-docs`), which already uses "hypothesis" as working vocabulary ("A refuted hypothesis
  is a successful spike," `spike-report_guide.md`). A spike reduces uncertainty about a technical question; it has no
  control group, no allocation and no statistical decision rule.
- the **test plan** and **test summary report** (`qa-docs`). They verify a product increment against an agreed
  specification and grade it pass or fail. This family tests an open hypothesis and estimates an effect against a
  baseline. The shared word "test" is the collision, and this contract states that boundary as the library's own
  POSITION.

**Two boundary sentences, because the research found the neighbours that would otherwise drift in.**

- **A standing measurement instrument is not a member, however closely it serves experiments.** A tracking plan, a
  set of metric definitions, a data dictionary or an experiment log is maintained across many tests and is never
  finished, so it belongs to a `classification` family. The tracking plan joins `governance-docs` by
  [ADR 0067](../decisions/0067-tracking-plan-joins-governance-docs-as-a-sixth-member.md).
- **A test run before anything is built, to decide whether to build it, is not this family's job.** This contract
  states the exclusion only and places no such document in any family.

A candidate whose job is not to plan or report one test of a hypothesis belongs in another family. In particular, a
review that looks back on how a team worked (a retrospective) or on a failure in production (an incident postmortem)
belongs to `process-docs`, even when it uses the word "experiment".

## 2. Required catalog metadata and allowed values

Every member's `<type>_meta.yaml` carries the full field set defined by the
[metadata schema](../../../tools/meta.schema.json) (methodology B5), with these family-specific constraints:

| Field | Allowed values for this family |
|---|---|
| family | `experimentation-docs` |
| phase | `measure` (if a candidate member's phase differs, it belongs in another family). This family declares `phase`, not `classification`; see the axis note below. |
| methodology | **Descriptive, not gated** (the [ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md) lesson, carried forward). The named sources span product experimentation, public-sector evaluation and academic preregistration, so a member declares what it honestly leans on rather than having the truth bent to a rule. |
| sizes_available | `[lean, full]`, or `[lean]` for a type whose own research shows it does not earn a second weight. The catalog's size calls are hypotheses, not facts (finding EC-2 in `STATE.md`). |
| status | `beta` until the maintainer judges the bundle settled; then `stable` eligible ([ADR 0055](../decisions/0055-retire-the-zero-fills-disclosure.md)) |
| pairs_with | the pm-skills skill ID(s) this template serves, or `[]`; every value must resolve against the pinned skill-ID list. A member claims a pairing only where that claim is true of that member. |

**The axis call, made at contract time against the planned members.** This family is **`phase: measure`**. The call
is the library's own POSITION, per [decision-procedures.md section 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world):
no source in the research argues for a family boundary at this phase. The reasons are these.

- **Neither member is a standing instrument.** The `classification` axis describes a document set up once and
  maintained indefinitely, which is what earned `governance-docs` its `classification: utility`
  ([ADR 0024](../decisions/0024-adopt-governance-docs-family-contract.md)). A design doc is finished when the test
  launches, and a readout is finished when the decision is recorded. Each is produced at a stage and finished, which is
  the definition of a `phase` artifact, the same reasoning [ADR 0026](../decisions/0026-adopt-qa-docs-family-contract.md)
  applied to `qa-docs`.
- **Being written before the test runs does not move the design doc out of `measure`.** A test plan is written before
  any testing is done and is still `phase: develop`. The axis records the phase a document serves, not the hour it is
  drafted.
- **The library forecast this family.** The `governance-docs` contract's kpi-dashboard note says that "If a future
  measurement family with genuinely phase-bound members is built, that is where a phase-axis metrics artifact would
  live." That note refused `phase: measure` for a standing dashboard. This family is the phase-bound case it described.
- **The catalog agrees on coherence, not on the word.** Both planned members carry the same catalog `stage`, `growth`,
  which the phase vocabulary does not contain. `measure` is the nearest of its six values (`discover`, `define`,
  `develop`, `deliver`, `measure`, `iterate`). `iterate` belongs to `process-docs`, whose members look back on how a
  team worked rather than on whether a change worked.

**No other family uses `measure`.** This family is the first to declare it. Phase coherence constrains a family
internally and never claims a phase for one family, as the `qa-docs` contract records for `develop`.

## 3. Structural obligations (gate-checkable)

1. **The eight files.** Every member ships all eight roles: template-lean, template-full (where two sizes exist),
   companion, guide, example, meta.yaml, history, research-log; filenames prefixed `<type>_`.
2. **Nesting.** Where two sizes exist, the lean variant's H2 sections are a strict ordered subset of the full
   variant's; shared sections keep name and order. Single-size members are exempt from nesting, not from anything else.
3. **Guidance comments.** Every section of every variant carries the Approach A comment (WHAT, WHY with a companion
   pointer, ASK, GOOD, WEAK, TRAP; PRIORITY and ROW HINT for table sections), parseable under the comment grammar. A
   "How to fill this in" preamble sits inside each variant's opening comment block. Both members carry metric tables,
   so ROW HINT discipline carries real weight here.
4. **Companion skeleton.** All 11 sections of methodology section 5, in order; an inapplicable section says so in one
   line rather than being dropped.
5. **Guide shape.** When to use; when NOT to use; pick a variant; a self-gradable quality rubric; at least two named
   anti-patterns.
6. **Citations.** Methodology section 6 in full: numbered, reliability-tagged, anchored, hyperlinked, cited inline, no
   padded entries, retrieval qualifiers on any source not directly fetched. This family has one live lineage trap: the
   sources span three traditions (product experimentation, public-sector evaluation, academic preregistration and trial
   reporting). A member that borrows a structure from one tradition says which, and does not present a clinical or
   academic reporting standard as product-management practice.
7. **Example.** One fully worked instance, no placeholders, illustrative figures labeled, provenance frontmatter
   stamped.

## 4. The shared-scenario rule (family-specific)

Like `qa-docs` and unlike `decision-docs`, `experimentation-docs` members **chain their examples on one shared
scenario**, because the two roles compose on a single test: the design doc plans it, and the readout reports the same
test against the plan.

The examples chain **onto the existing Acme Analytics "Saved Views for Dashboards" thread**, as `qa-docs` does. The
readout must report the experiment the design doc planned, with the same hypothesis, metrics and decision rule. Every
baseline, metric and date either example uses must agree with the example it reads from, and an experiment on a shipped
feature post-dates the 2.4.0 release that `release-notes_example.md` records. A member whose example invents an
unrelated feature or contradicts a sibling example is out of contract even if every file exists.

## 5. Shareable-boundary rule

Template body (headings, placeholders, tables) is the reusable shape; guidance lives only in comments; example content
never leaks into templates; meta describes the asset, never the filled instance. A member whose guide has grown
explanatory (companion material) or whose companion has grown procedural (guide material) is out of contract even if
every file exists.

## 6. Enforcement

The gate enforces section 2 and the mechanical part of section 3. **Family check letter K** validates section 2's
family-specific values for every declared member (`phase: measure`, a `beta`/`stable` status, and a `[lean, full]` or
`[lean]` size shape) and that this contract file resolves; methodology is descriptive and is not gated (see section 2).
A member declaring `classification: utility` instead of `phase: measure` fails check K with a message naming the axis
it should have used. Of section 3's obligations, the eight files (3.1), nesting (3.2), citations (3.6), and the clean
example (3.7) are enforced by checks A, C, E, and D respectively; guidance comments (3.3), the companion skeleton (3.4),
and guide shape (3.5) have no mechanical check yet and are review obligations at authoring time. Sections 1, 4 and 5
are likewise review obligations at authoring time and audit obligations thereafter. A member failing this contract is
not "in the family with issues"; it is out of the family until green, and the catalog count reflects that.

## Change note

**0.1.0 (2026-10-06, [ADR 0066](../decisions/0066-adopt-experimentation-docs-family-contract.md)):** adopted
2026-10-08 after a maintainer read, to be enforced by gate check K, the tenth family contract and the **first on `phase: measure`**. The maintainer approved
founding the family on 2026-10-04 and ruled on 2026-10-06 that its two planned members ship as two bundles, following
the `qa-docs` pair `test-plan` and `test-summary-report`. Drafted contract-first, before any member is built, so the
contract describes the set its two planned members must join rather than one that already exists. The membership test,
both boundary sentences and the axis call come from a research pass on 2026-10-05 that tested five measurement
candidates against all nine existing contracts and a draft of this one.
