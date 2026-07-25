# History: Test Plan bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-07-25

- Initial Test Plan bundle. **First member of the `qa-docs` family.** Catalog entry 102. Conforms to the
  [qa-docs contract](../../docs/internal/contracts/qa-docs.md) (`phase: develop`, `beta`, sizes
  `[lean, full]`); gate check K green
  ([ADR 0026](../../docs/internal/decisions/0026-adopt-qa-docs-family-contract.md)).
- **Scope: the test plan, framed honestly, in a field that is openly split about whether it should exist.**
  The companion's sections 1, 2 and 6 carry the argument. Three verifiable and uncomfortable facts shape the
  whole bundle: the standard everyone cites (IEEE 829) is **superseded**; its replacement
  (ISO/IEC/IEEE 29119-3:2021) is **paywalled**, so most teams follow a structure they have never read; and a
  decade-long campaign by named practitioners argued that standardized test documentation harms testing. The
  bundle teaches the plan that survives all three: short enough to be read, specific enough to be checked,
  risk-ranked so the shape of the coverage is visible.
- **The load-bearing distinction**, from the best-known critic of test documentation: *"The test plan document
  does not necessarily contain a test plan"* (James Bach, 2006). The plan is the set of ideas; the document
  may or may not carry them. Every criticism in section 6 targets documents that carry none, and none of it is
  an argument against planning.
- **Four attribution corrections the research forced**, each a defect this bundle would otherwise have
  shipped: (1) IEEE labels 829-2008 **"Superseded"**, not "Withdrawn"; a claimed 2024 withdrawal date could
  not be confirmed on any read page and is not used. (2) **Bach is not anti-test-plan**: he published a Test
  Plan Evaluation Model (1999) and a seven-task guide to building one. (3) **Session-based test management is
  Jonathan Bach's paper**, co-credited with James Bach; Michael Bolton is not a co-creator. (4) **The agile
  testing quadrants originate with Brian Marick (2003)**, not Crispin and Gregory, who extended and
  popularized them and who credit Marick themselves.
- **Variants: `lean` and `full`.** The catalog lists M/L; the two-weight split fits. Lean is the five sections
  that answer the questions no plan can skip: Scope and Non-Scope, Risk-Ranked Approach, Entry and Exit
  Criteria, Environment/Data/Ownership, Schedule and Deliverables. Full adds what formality earns: Test Levels
  and Types, Suspension and Resumption Criteria, Risks to the Test Effort, and Approvals and Change Control.
  Nesting verified: lean's five H2 headings are a strict ordered subset of full's nine.
- **The sharpest teaching points**, carried through companion, guide and example: (1) **the plan is not the
  document**, and a plan nobody reads is not a safety net; (2) **"features not to be tested" is the
  highest-value section and the most commonly dropped** - if nothing is out of scope, nothing can be found
  missing; (3) **risk ranks the coverage and the plan must show the ranking**, with the highest-risk areas
  tested first; (4) **product risk and project risk are two lists**, one shaping coverage and one shaping the
  schedule, and merging them is why risk sections read as noise; (5) **criteria are thresholds, not
  adjectives**, and exit criteria are supposed to be agreed with named stakeholders; (6) **pass rate and
  test-case count as exit criteria bake Goodhart's Law into the plan**; (7) **when a tool says "test plan" it
  means an execution container**, not this document.
- **Worked example opens the first cross-family chain in the library.** Per the qa-docs contract's
  shared-scenario rule, `test-plan_example.md` chains onto the **delivery-docs** thread rather than a new
  scenario: a full-variant plan for Acme Analytics' "Saved Views for Dashboards", drawing scope from the
  [PRD](../prd/prd_example.md), technical surface from the [design document](../sdd/sdd_example.md),
  functional coverage from the [acceptance criteria](../acceptance-criteria/acceptance-criteria_example.md),
  and product risks from the [program risk register](../risk-register/risk-register_example.md) (R-05
  entitlement, R-06 view-list performance, R-02 config migration are inherited rather than invented). It
  demonstrates an explicit non-scope with reasons, a risk ranking that drives both depth and order, exit
  criteria that deliberately refuse a pass-rate line, a suspension rule with a named decider, and the
  distinction between product risk and risk to the test effort.
- **`pairs_with: [deliver-edge-cases]`.** pm-skills ships **no testing or QA skill at all** (all 68 tracked
  skills enumerated 2026-07-25; recorded as finding EC-4 in `STATE.md`). `deliver-edge-cases` is the one
  honest pairing: its own description names QA planning and preparing test plans among its uses, and the
  edge-case catalog it produces is a direct input to the Risk-Ranked Approach section.
- Companion researched 2026-07-25 across five parallel dimensions and 42 tier-ranked, deduplicated sources
  (see `test-plan_research-log.md` for per-source retrieval status). Primary anchors include the IEEE SA
  pages for 829-2008 and 29119-3:2021, the ISTQB glossary entries for test plan, organizational test strategy
  and entry criteria, four Satisfice publications, Crispin's own quadrant posts, the context-driven testing
  principles, and Microsoft's Azure Test Plans documentation. Four sources are **landing-page-only** (the two
  Bach PDFs, the SBTM paper, and *Agile Testing Condensed*) and no claim rests on their unread contents;
  29119-3 itself was **not read** and is not quoted. Claims flagged contested: 829's exact status, how many
  sections it defined (15 versus 16, unresolved here), whether 29119 represents consensus, whether a test plan
  belongs in agile at all, whether test cases and acceptance criteria are distinct artifacts, and where the
  plan/strategy line sits. An unsourced "42 percent of QA teams" statistic found in the research is
  deliberately unused. Nothing not fetched-and-verified is quoted.
- Status: `beta`. Gate-green, zero real usage by anyone other than the author.
