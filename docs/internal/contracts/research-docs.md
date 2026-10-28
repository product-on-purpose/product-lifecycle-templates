# Family Contract: research-docs

Status: adopted 2026-10-23 ([ADR 0081](../decisions/0081-adopt-research-docs-family-contract.md)); proposed the same day and adopted after a maintainer read, per [decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer)
Applies to: every bundle declaring `family: research-docs` in its meta
Members at adoption: none built yet (the catalog candidates `user-research-plan`, entry 210, and `user-research-report`, entry 18, are the planned members, tracked as issues #316 and #317). `user-research-plan` was built on 2026-10-24, and `user-research-report` on 2026-10-27
Modeled on: the experimentation-docs and qa-docs family contracts, the two existing families that pair a plan with a report
Axis: `phase` (`discover`); see section 2 for the axis call and its stated cost
Version: 0.1.0 (changes to this contract require a decision record; see the change note at the end)

## 1. Membership

A bundle belongs to this family when its document type **plans or reports on one study of the people a product
serves**. A study here means research with participants: interviews, usability tests, diary studies, surveys and
field visits. This library holds, as its own POSITION, that analysing product telemetry alone is not a study in
this sense. Each member is written for one study, and it is finished when that study's findings are reported. That
finish line is also the library's POSITION, because no source read argues for one. Finished means the document
stops changing, not that it stops being read: Maze calls the report "an ongoing reference point".

The family's two roles are sequential rather than alternative, and that sequence is its teaching value:

- a **user research plan** sets out one study's goals, research questions, method, participants and logistics
  **before** the study runs. When the method is a usability test, it also carries the tasks and the metrics.
- a **user research report** records what the study found and what it recommends, **after** the study ends. It
  answers the questions the plan set out.

The sources tie the two together. MeasuringU's usability test plan says "If possible, try to outline how the
report will be structured in the test plan." Dovetail's plan template says "Findings stay traceable to the research
questions you started with." Maze's report guide lists "Research questions the report is hoping to answer" among
the things a report includes.

Each member must state its position against the other member in its companion's Relationships section. It must
also state its position against these neighbours:

- **The experiment pair** (`experimentation-docs`). An experiment "plans or reports on one discrete test of a
  hypothesis about the effect of a change to a product or its market". Itamar Gilad draws the line this family
  relies on: "Per this definition an A/B test is an experiment, but a usability test is not." This library holds,
  as its POSITION, that a study which allocates participants between variants and applies a decision rule is an
  experiment, whatever it is called. *(Note 2026-10-27: Gilad qualifies his own line in the next sentence: "I
  realize that this is not the common definition used in the industry". The boundary rests on his stricter
  definition, by his own account, which is why this paragraph states its version as a POSITION. Source:
  `user-research-plan_research-log.md` [19].)*
- **The QA pair** `test-plan` and `test-summary-report` (`qa-docs`). They report "the verification of a product
  increment" against a specification. A usability study asks how people use a product, and its report records
  observations, not a verdict against a specification. The shared words "test plan" are the collision, which is why
  entry 210 does not carry "test plan" alone as an alias.
- **The documents that use the findings** (`discovery-docs`). That family admits a type that exists "to decide whether
  to build something, or which concept to design, before anyone commits to building it". A member here may
  recommend, but it records no decision. The persona, the problem statement and the design brief take the findings
  and frame or decide.

**Three boundary sentences, because the research found the neighbours that would otherwise drift in.**

- **A standing research document is not a member.** A service-wide research plan, a research repository, a
  participant panel, and an aggregate of findings across many studies are maintained over time, so each belongs to a
  `classification` family. Catalog entry 17, the Voice of Customer report, aggregates signals "ongoing, quarterly".
  GOV.UK's Design System runs the same kind of aggregate: "we will usually investigate something if we hear similar
  findings from 4 or more different services."
- **A retrospective on how a study was run belongs to `process-docs`.** That family exists "to look back at what
  happened and change what happens next", and its members look back on how a team worked.
- **A test run before anything is built, to decide whether to build it, stays parked.** ADR 0066 excluded the concept
  test brief (entry 27) and placed it nowhere. This contract does not place it either. If a later sweep admits it,
  this family's membership test is the first one to test it against.

**Candidates this contract names but does not admit.** The interview guide (entry 25) and the survey instrument
(entry 26) are used during a study, so neither plans or reports on one. If a sweep admits either, adding that role
is an amendment with its own decision record. The diary study plan (entry 28) would plan one study, so this clause
would admit it if its own sweep finds it distinct from entry 210.

A candidate whose job is not to plan or report on one study of people belongs in another family.

## 2. Required catalog metadata and allowed values

Every member's `<type>_meta.yaml` carries the full field set defined by the
[metadata schema](../../../tools/meta.schema.json) (methodology B5), with these family-specific constraints:

| Field | Allowed values for this family |
|---|---|
| family | `research-docs` |
| phase | `discover` (if a candidate member's phase differs, it belongs in another family). This family declares `phase`, not `classification`; see the axis note below. |
| methodology | **Descriptive, not gated** (the [ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md) lesson, carried forward). The named sources span UX research vendors, government digital services and an ISO reporting standard, so a member declares what it honestly leans on. |
| sizes_available | `[lean, full]`, or `[lean]` for a type whose own research shows it does not earn a second weight. The catalog's size calls are hypotheses, not facts (finding EC-2 in `STATE.md`). |
| status | `beta` until the maintainer judges the bundle settled; then `stable` eligible ([ADR 0055](../decisions/0055-retire-the-zero-fills-disclosure.md)) |
| pairs_with | the pm-skills skill ID(s) this template serves, or `[]`; every value must resolve against the pinned skill-ID list. A member claims a pairing only where that claim is true of that member. |

**The axis call, made at contract time against the planned members.** This family is **`phase: discover`**. The
call is the library's own POSITION, per
[decision-procedures.md section 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world):
no source read argues for a family boundary at this phase. The reasons are these.

- **Neither member is a standing instrument.** Nielsen Norman Group: "Typically, a research plan is constructed for
  each study." A report covers the one study it reports. Each document is produced at a stage and finished, which
  is the definition of a `phase` artifact, the reasoning
  [ADR 0026](../decisions/0026-adopt-qa-docs-family-contract.md) applied to `qa-docs`. *(Note 2026-10-27: the
  same article allows that "sometimes, a research plan could include numerous studies or phases of research", so
  section 1's one-study membership test is this library's POSITION against a practice the source names. Source:
  `user-research-plan_research-log.md` [7].)*
- **The catalog agrees on coherence.** Both planned members carry the catalog `stage` `discovery`, and so do the
  named candidates 25 and 28.
- **A family could hold several phase values, but that buys nothing here.** Each bundle declares exactly one phase
  (`tools/meta.schema.json`), and the sources give each type one structure for every kind of study. A second value
  would need a rule for which value a one-structure type picks, and no source supplies such a rule.

**The cost is stated, not hidden.** The sources use both documents for any kind of study, including evaluation of
a shipped product. NIST's usability test report template exists to help "vendors demonstrate evidence of usability
in their final product", and it notes that "The ISO document is intended for the reporting of summative (i.e.,
quantitative) studies." GOV.UK's Design System takes findings from a service at any stage, including when "you
might be iterating the service after going live". A member that serves such a study still declares `discover`, and its companion must say why. This library holds, as its POSITION, that a study of
what people do, need or can do with a product is discovery work, whether it runs before a commitment or after a
release.

**When to revisit.** If a member's own research shows that its dominant use is measuring a shipped product, the
value is reopened at that member's contract amendment, per
[decision procedure 10](../decision-procedures.md#10-a-family-or-axis-assignment-is-uncertain).

**`discover` is shared.** `discovery-docs` also declares `discover`. Phase coherence constrains a family internally
and never claims a phase for one family, as the `qa-docs` contract records for `develop`.

## 3. Structural obligations (gate-checkable)

1. **The eight files.** Every member ships all eight roles: template-lean, template-full (where two sizes exist),
   companion, guide, example, meta.yaml, history, research-log; filenames prefixed `<type>_`.
2. **Nesting.** Where two sizes exist, the lean variant's H2 sections are a strict ordered subset of the full
   variant's; shared sections keep name and order. Single-size members are exempt from nesting, not from anything else.
3. **Guidance comments.** Every section of every variant carries the Approach A comment (WHAT, WHY with a companion
   pointer, ASK, GOOD, WEAK, TRAP; PRIORITY and ROW HINT for table sections), parseable under the comment grammar. A
   "How to fill this in" preamble sits inside each variant's opening comment block.
4. **Companion skeleton.** All 11 sections of methodology section 5, in order; an inapplicable section says so in one
   line rather than being dropped.
5. **Guide shape.** When to use; when NOT to use; pick a variant; a self-gradable quality rubric; at least two named
   anti-patterns.
6. **Citations.** Methodology section 6 in full: numbered, reliability-tagged, anchored, hyperlinked, cited inline, no
   padded entries, retrieval qualifiers on any source not directly fetched. This family has one live lineage trap:
   the sources span UX research vendors, government digital services, and the ISO/IEC 25062 Common Industry Format,
   which NIST adapted for testing electronic health records. A member that borrows a structure from a government
   form or from that standard says so, and does not present a regulatory reporting format as general product
   practice.
7. **Example.** One fully worked instance, no placeholders, illustrative figures labeled, provenance frontmatter
   stamped, and independent of the template's own GOOD and WEAK text per `tools/check-example-independence.py`. No
   member of this family is grandfathered.

## 4. The shared-scenario rule (family-specific)

Like `qa-docs` and `experimentation-docs`, `research-docs` members **chain their examples on one shared scenario**,
because the two roles compose on a single study: the plan plans it, and the report reports the same study against
the plan.

The examples chain **onto the existing Acme Analytics thread, at the 2026-05 Reporting friction study.** The library
cites that study and has never shown it. The PRD example cites "Discovery readout: Reporting friction study,
2026-05", and the design brief, epic and announcement examples cite the same study. The plan's example plans that
study and is dated before it runs. The report's example is its readout. Both precede the design brief of 2026-06-01
that cites the study.

**The obligation:** every fact the library's other worked examples state about the study holds in both examples.
The design brief's example says the study "interviewed 12 analysts; 9 of them described" the re-filtering pattern,
and the PRD example gives n=12. Figures that appear only in another bundle's template GOOD or WEAK text are
illustrations, not facts of the scenario, and they do not bind these examples. A member whose example contradicts a sibling example, or invents a different study, is out of
contract even if every file exists.

## 5. Shareable-boundary rule

Template body (headings, placeholders, tables) is the reusable shape; guidance lives only in comments; example content
never leaks into templates; meta describes the asset, never the filled instance. A member whose guide has grown
explanatory (companion material) or whose companion has grown procedural (guide material) is out of contract even if
every file exists.

## 6. Enforcement

The gate enforces section 2 and the mechanical part of section 3. **Family check letter K** validates section 2's
family-specific values for every declared member (`phase: discover`, a `beta`/`stable` status, and a `[lean, full]`
or `[lean]` size shape) and that this contract file resolves; methodology is descriptive and is not gated (see
section 2). A member declaring `classification: utility` instead of `phase: discover` fails check K with a message
naming the axis it should have used. Of section 3's obligations, the eight files (3.1), nesting (3.2), citations
(3.6), and the clean example (3.7) are enforced by checks A, C, E, and D respectively; the example-independence half
of 3.7 is enforced by `tools/check-example-independence.py`. Guidance comments (3.3), the companion skeleton (3.4),
and guide shape (3.5) have no mechanical check yet and are review obligations at authoring time. Sections 1, 4 and 5
are likewise review obligations at authoring time and audit obligations thereafter. A member failing this contract
is not "in the family with issues"; it is out of the family until green, and the catalog count reflects that.

## Change note

**0.1.0 (2026-10-23, [ADR 0081](../decisions/0081-adopt-research-docs-family-contract.md)):** proposed and adopted
2026-10-23 after a maintainer read, enforced by gate check K, the eleventh family contract. Drafted contract-first, before any member is built, so
the contract describes the set its two planned members must join rather than one that already exists. Two admission
sweeps on 2026-10-23 admitted the user research plan (entry 210) and the user research report (entry 18), and a
placement pass between them tested the plan against all ten existing contracts and a draft of this one. The
maintainer ruled the same day that entry 18 is swept first, and authorized this proposal once it cleared. The
maintainer then read the contract diff and accepted it, asking for one sentence in section 1 that separates a
finished document from one no longer read.
