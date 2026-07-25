# History: Bug Report bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-07-25

- Initial Bug Report bundle. **Third member of the `qa-docs` family, completing it.** Catalog entry 107.
  Conforms to the [qa-docs contract](../../docs/internal/contracts/qa-docs.md) (`phase: develop`, `beta`,
  sizes `[lean, full]`); gate check K green
  ([ADR 0026](../../docs/internal/decisions/0026-adopt-qa-docs-family-contract.md)).
- **Scope: the bug report, framed as an anomaly report.** The framing is the bundle's central move and it
  comes from the standards themselves: IEEE 829-2008 renamed this document type an **anomaly report** on the
  stated reasoning that a discrepancy between expected and actual results can arise for reasons other than a
  fault in the system, and its successor calls it an **incident report**. At the moment of writing, the
  reporter does not know whether there is a defect. Every template instruction follows from that: report the
  observation, keep the diagnosis separate and labeled, and let the investigation decide.
- **The empirical anchor, and the number the whole bundle leans on.** Across roughly 3,000 real reports,
  observed behavior appeared in **93.5 percent**, steps to reproduce in **51.4 percent**, and **expected
  behavior in only 35.2 percent** (Chaparro et al., ESEC/FSE 2017). Two reports in three never say what should
  have happened. The bundle makes that its own section with its own guidance rather than a field in a list.
- **The problem the template exists to reduce**, from the landmark 466-respondent study (Bettenburg et al.,
  FSE 2008): what developers most want - steps to reproduce, stack traces, test cases - is precisely what
  reporters find hardest to supply. Thin reports are a friction problem, not a discipline problem, which is
  why the lean variant is the leanest in the family and why this bundle argues against putting the full
  variant in front of a user.
- **Severity and priority are separate fields with owners recorded, and two honest caveats stated.** ISTQB
  defines both terms and **assigns ownership to neither**; the familiar QA-sets-severity, PM-sets-priority
  rule is convention. And **there is no standard severity scale**: four, five and six-level scales are all in
  use, and S1-S4 numbering means different things in different sources. The template asks teams to pick one
  and define it where reporters can see it.
- **The tooling fact the bundle designs around:** **Jira had a Severity field and deliberately removed it**,
  on the reasoning that it confused business users, leaving Priority to carry both meanings. Jira therefore
  cannot express, out of the box, the distinction the discipline teaches. The guide tells teams with one field to decide what it means and write that down.
- **And the reason the defect lifecycle has no canonical states:** **IEEE 1044-2009 was inactivated on
  2020-03-05** after a decade without revision, with no replacement published. Every state list in
  circulation is convention. The bundle says so rather than presenting one as standard.
- **Variants: `lean` and `full`, split by author rather than by formality.** The catalog marks entry 107
  single-size (S); this bundle ships two, the third tested catalog size hypothesis after EC-2, and the split
  is unusual: **three of the four sections the full variant adds are filled in by someone other than the
  reporter, after filing.** Lean is the intake form (summary, steps, expected and actual, environment and
  reproducibility); full is what the record becomes as it moves through evidence, classification, triage and
  resolution. Nesting verified: lean's four H2 headings are a strict ordered subset of full's eight.
- **The sharpest teaching points**, carried through companion, guide and example: (1) **report the
  observation, not the conclusion**; (2) **expected behavior is the most-omitted element**, and it is not
  obvious to the reader; (3) **reproducibility is a count, not an adjective**; (4) **severity and priority are
  independent**, with both crossing cases worked; (5) **duplicate rates run from about 2 to 28 percent by
  project type**, so the widely quoted 30 percent is the top of a range rather than a fact; (6) **tone changes
  outcomes**, stated explicitly as craft wisdom with no study claimed; (7) **defect counts get gamed** in
  documented ways once they become targets; (8) **do not reopen a closed bug for a regression** - open a new
  one and link it.
- **Worked example closes the family chain.** `bug-report_example.md` is the defect found by
  [TC-047 step 4](../test-case/test-case_example.md), which was designed from the highest-tier risk in the
  [test plan](../test-plan/test-plan_example.md), which inherited it from the program risk register. The
  aggregate was computed before the entitlement row filter, so rows were correctly hidden while the total
  disclosed their magnitude - a defect a row-level assertion structurally cannot see. The report records the
  test plan's **suspension rule firing**, a **triage disagreement about priority left visible rather than
  overwritten** (reporter said P2 weighing current exposure, triage said P1 weighing the release gate), the
  full permission-matrix re-run the plan's resumption rule required, and the regression guard that now stops
  it recurring. A risk produced a plan, the plan produced a case, the case produced this report, and this
  report produced a test.
- **`pairs_with: [deliver-edge-cases]`.** pm-skills ships no testing or QA skill (finding EC-4 in `STATE.md`),
  and the fit is looser here than for the two siblings, because an edge-case catalog is written before the
  fact and a bug report after it. The guide states the honest connection rather than overselling it: a defect
  found in the wild is evidence the failure surface was under-mapped.
- Companion researched 2026-07-25 across five parallel dimensions and 42 tier-ranked, deduplicated sources
  (see `bug-report_research-log.md` for per-source retrieval status). Primary anchors include the IEEE SA
  pages for 829-2008 and 1044-2009, four peer-reviewed empirical studies of bug report quality and
  non-reproducibility, Simon Tatham's canonical essay, Spolsky, Fowler and Sinofsky on whether to track
  defects at all, and the Azure and Atlassian product documentation. **Both standards are paywalled and
  neither was read**; the ISTQB glossary is cited from community mirrors and labeled as such. **One source
  was not retrieved at all** and is listed carrying no claim, with its unverifiable author list called out.
  Twelve claims are flagged contested, including who assigns severity, whether to log bugs at all, and
  whether the bug/defect/issue distinction matters. An unverified attribution of the error-defect-failure
  chain to a named individual was found in the research and is deliberately unused.
- Status: `beta`. Gate-green, zero real usage by anyone other than the author.
