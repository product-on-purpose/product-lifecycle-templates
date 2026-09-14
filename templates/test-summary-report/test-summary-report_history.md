# History: Test Summary Report bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-09-14

- **The four-lens review found no fabricated quotation and no blocker, and found a defect in this log's own
  synthesis that no other check could have caught.** The log's prose stated twice that the section design
  rests on ISTQB CTFL **v4.0.1, read in full**, while its own Sources section carried only the **superseded
  2018 v3.1.1**. Both editions had in fact been fetched and verified by the research; the de-duplication pass
  that built the source list **collapsed three distinct ISTQB syllabus editions into one entry**, because
  their author and title strings agree for the first sixty characters, and it kept the wrong one. The same
  pass also collapsed the **2013 and 2021 pages of the standard itself**, which matters because the
  difference between those editions is a cited finding. Four dropped sources are restored and every
  same-publisher collision is now disambiguated at the front of its entry rather than merged. The source
  count moves from 68 to **72 unique, 62 fetched-and-verified**.
  **The mechanism is worth naming: a verification pass over source entries does not verify the prose that
  cites them, and a pass over prose does not verify the entries.** The review caught this only by checking
  one against the other.
- **Five further claims overstated the evidence and were narrowed rather than re-sourced.** "The single most
  skipped field" ranked field omission across reports on a sample of one. "Military test and evaluation
  almost certainly has the most developed test-report doctrine of any of these" ranked a domain whose
  documents were **never retrieved** - the disclosed gap now speaks for itself. The Stop 29119 campaign was
  attributed to "a conference talk by James Christie" where the log's source entry supports only that he is
  the campaign's original instigator. And the example attributed a defect to "the PRD's view-list
  performance requirement" when the PRD example contains no such requirement - the budget lives in the test
  plan, carried as register risk R-06.


- **Initial test-summary-report bundle. The fourth member of the `qa-docs` family, and its closing one.**
  Catalog entry 106, `test-report-test-summary-report`. The family's three built members carry three roles -
  the test plan scopes a verification effort, the test case specifies one unit of it, the bug report records
  one verification that failed - and this is the fourth: it **closes** the effort. It also keeps a promise
  the library had already made and could not honour: `templates/test-plan/` sends a reader to a test report
  in **four separate places** - its guide's "when NOT to use" list opens a bullet *"You need a test
  report."*, its routing table sends *"What we found, and whether we are shipping"* to *"A test report"*,
  its companion says results, status and the verdict *"live in the test report and the test tool, not here"*,
  and both template variants say the plan is *"NOT a test report (that is retrospective, written after)"* -
  and until today no such bundle existed. No `future:` tag recorded that promise, which is why no gate ever
  flagged it.

- **Two admissions, and they are separate questions answered by separate evidence.** The **family**
  admission is a judgment call and belongs to the maintainer, because the
  [qa-docs family contract](../../docs/internal/contracts/qa-docs.md) admits a type whose job is to
  *"report the verification of a product increment"* in its exclusion clause while assigning the reporting
  role specifically to the bug report in its role list, and
  [ADR 0026 (adopt the qa-docs family contract)](../../docs/internal/decisions/0026-adopt-qa-docs-family-contract.md)
  contains no fourth-member clause of the kind
  [ADR 0022 (adopt the decision-docs family contract)](../../docs/internal/decisions/0022-adopt-decision-docs-family-contract.md)
  wrote for `decision-docs`. That judgment is recorded in
  [ADR 0050 (qa-docs admits a fourth member)](../../docs/internal/decisions/0050-qa-docs-admits-a-fourth-member.md).
  The **document-type** admission is not a judgment call at all: the governing international standard
  defines this document in its own Clause 3, read verbatim from the publisher's free preview -
  *"3.9 test completion report / test summary report / report that provides a summary of the testing that
  was performed"* - and gives it a numbered clause and a worked-example annex in its table of contents. A
  named source does not get more named than that.

- **The retrieval position is the defining fact about this bundle, and the guide and the companion both
  state it before anything else.** The governing
  standard, ISO/IEC/IEEE 29119-3:2021, is **sold, not published**. What this research read is a legitimate
  free preview of 15 of roughly 93 pages (front matter, the complete Contents, Foreword, Introduction, the
  complete Clause 3 and Clause 4.1), plus a second free preview of the BSI edition carrying Annex A's
  conformance table. So three things are readable and everything else is not:
  1. **The Clause 3 definition**, quoted above, which settles that the document type exists and that
     "test completion report" and "test summary report" are the standard's own synonyms in one defined-term
     head.
  2. **The table of contents**, which shows *"7.4 Test completion report ... 18"* with ten subclause
     headings - *"7.4.1 Overview / 7.4.2 Summary of testing performed / 7.4.3 Deviations from planned
     testing / 7.4.4 Test completion evaluation / 7.4.5 Factors that blocked progress / 7.4.6 Test measures
     / 7.4.7 Residual risks / 7.4.8 Test deliverables / 7.4.9 Reusable test assets / 7.4.10 Lessons
     learned"* - plus *"Annex G (informative) Test completion report ... 58"*. **This is a list of subclause
     headings from a table of contents and is labelled as such everywhere it appears in this bundle**, never
     as the standard's requirements.
  3. **Annex A's conformance table**, which attaches a requirement level to each of those subclauses:
     *"7.4.3 Deviations from planned testing ... Shall"*, *"7.4.4 Test completion evaluation ... Shall"*,
     *"7.4.7 Residual risks ... Shall"*, *"7.4.9 Reusable test assets ... Should"*, *"7.4.10 Lessons
     learned ... Shall"*.

  **Not read, and nothing in this bundle rests on it: the substantive text of Clause 7.4, and Annex G's
  worked example.** The headings are read; what the standard requires under them is not.

- **So the section design does not come from the standard, and the bundle says so plainly rather than
  borrowing the standard's authority for a structure nobody here read.** It rests on **ISTQB's freely
  published Certified Tester Foundation Level syllabus**, whose contents list for this document was read and
  quoted verbatim - *"Typical test summary reports may include: Summary of testing performed / Information
  on what occurred during a test period / Deviations from plan, including deviations in schedule, duration,
  or effort of test activities / Status of testing and product quality with respect to the exit criteria or
  definition of done / Factors that have blocked or continue to block progress / Metrics of defects, test
  cases, test coverage, activity progress, and resource consumption / Residual risks / Reusable test work
  products produced"* - and it is tested against real filled reports and real published templates. **One
  qualifier travels with that source and is stated in companion section 1 rather than buried here: the
  syllabus edition actually fetched and read is the 2018 v3.1.1 release, which ISTQB superseded on
  2023-04-21 with CTFL v4.0 (errata v4.0.1).** The current edition is **not** among this research's
  fetched-and-verified sources. ISTQB's live position on the same material is corroborated instead through
  an official ISTQB member board's current page, and **where a structural claim could only come from the
  current syllabus edition, the bundle does not make it**.

- **This bundle makes no claim about IEEE 829's section list, in any edition, and that is deliberate.** IEEE
  829 was not read either, and every second-hand description of "IEEE 829's Test Summary Report structure"
  this research met **disagrees with the others**: the logged sources variously give the standard six, seven,
  eight and ten document types, and give its Test Summary Report six or eight internal items, for editions
  dated 1983, 1998 and 2008. Those sources are logged to evidence the disagreement and are never adopted as
  the standard's contents. The one 829 fact this bundle does assert is its status, verified at the IEEE
  Standards Association's own catalogue page rather than inherited from the catalog or from a blog:
  **"Status: Superseded Standard"**. **An "Inactive-Withdrawn" status dated 2024-10-28 appeared in a search
  result, could not be corroborated on a direct fetch of that page, and is not used anywhere.** The
  1998 catalogue page's abstract was also read and **does not enumerate "Test Summary Report" by name**, so
  it cannot be, and is not, cited to confirm the document type.

- **The bundle teaches the dispute over its own governing standard rather than presenting a settled genre.**
  In 2014 a petition organised by the **International Society for Software Testing**, following a conference
  talk by James Christie, asked ISO to suspend publication of Parts 4 and 5 of ISO/IEC/IEEE 29119 and to
  **withdraw Parts 1 to 3** - which is to say, to withdraw the very part that defines this document. James
  Bach, Cem Kaner and Michael Bolton are the named figures of the context-driven school on one side; the
  ISO/IEC/IEEE WG26 working group convened by Stuart Reid and the ISTQB certified-tester ecosystem are on the
  other. Bolton's characterisation of the standard is quoted in the guide and the companion because it is the
  charge the template is designed against, not one to be waved past: an *"overstructured process model,
  focused on relentless, ponderous, wasteful bureaucracy and paperwork, with negligible content on actual
  testing"*. The standard was not withdrawn and Part 3 was revised in 2021; the opposition was not retracted
  either. **A bundle presenting the test report as settled practice would be making a claim this research
  refutes**, so the dispute opens the guide's "When to use", opens companion section 1, has its own section 6
  with both camps named, and shapes the templates: the lean variant's preamble tells the author not to retype
  what the dashboard already says and that sometimes the honest answer is not to write one at all, and the
  full variant's opens on the same charge, that nine filled headings are not a report.

- **The spec's load-bearing section was put under test against the evidence and did not survive.** The
  pre-research spec in [`tier2-specs.md`](../../docs/internal/tier2-specs.md) called a standalone
  **Release Recommendation** section - ship, do not ship, or ship with named conditions - *"the load-bearing
  section"*, and the one thing separating this document from a tool's exported test run. It is
  **not in either variant**, and this is recorded as a first-class outcome because the alternative is a
  template shape defended by nothing but an earlier draft of itself:
  - neither readable structural source has one (not ISTQB's eight-item contents list, not the standard's ten
    subclause headings); both have an **evaluation against exit criteria**, which is a different act;
  - the real filled reports overwhelmingly do not have one either. The most on-genre document in the corpus,
    a government UAT summary report, carries *Recommendations* and *UAT Results Mapped to Exit Criteria* and
    **no dedicated go/no-go section**; a Common Criteria certification report explicitly declines the role;
    an FDA 510(k) summary carries no recommendation at all; a third-party security assessment issues findings
    and severities rather than a verdict. **One does**, and it is not the counter-example it looks like: the
    voting-system certification report carries a named, signed recommendation to an accreditation body under
    a certification scheme, which is not a QA team's call on a release;
  - explicit proceed-or-not-proceed language does appear, but it appears in **vendor templates and vendor
    how-to content**, which is the weakest tier in this library's citation standard;
  - the *Recommendations* sections that do appear in real documents are about process improvement, not
    release, and that content is in Lessons Learned here.

  **So the act stays and the heading goes.** The ship call lives at the end of **Evaluation Against Exit
  Criteria**, underneath the graded criteria that justify it, and the templates say why in their preamble: a
  recommendation with nothing above it is an opinion, and the same sentence under a graded criteria table is
  a conclusion. The `test-plan` bundle's four-times-over promise that the verdict lives in a report written
  afterwards is kept; what is declined is giving that verdict a heading floating free of its evidence.

- **Four further departures from the same spec, all forced by the research.** The spec was written before the
  research pass and said outright it expected to be wrong somewhere. These are where.
  1. **`Quality Assessment` ships as `Evaluation Against Exit Criteria`.** The renaming is the point: the act
     both readable sources describe is grading against a bar the plan set, not issuing a general opinion on
     quality. The standard's heading is *"7.4.4 Test completion evaluation"*, ISTQB's item covers the status
     of testing and product quality with respect to the exit criteria or definition of done, and the one real
     filled report in the corpus names its section *UAT Results Mapped to Exit Criteria*.
  2. **`Variances from Plan` ships as `Deviations from Planned Testing` and is promoted from full-only into
     lean.** Annex A marks *"7.4.3 Deviations from planned testing ... Shall"*, and the section is what makes
     the execution numbers above it interpretable.
  3. **`Residual Risk` ships as `Residual Risk and What Was Not Tested` and is likewise promoted into lean.**
     Annex A marks *"7.4.7 Residual risks ... Shall"*. It is also the section this bundle argues a generated
     report cannot produce, which makes full-only placement indefensible.
  4. **Three sections the spec did not have are added, full-variant only**: Impediments and Blocked Progress,
     Test Deliverables and Reusable Assets, and Lessons Learned. All three have a subclause heading in the
     standard's table of contents and an entry in ISTQB's contents list; all three are accountability-grade
     rather than everyday. Lessons Learned is full-only for a reason stated in companion section 8: a team
     that runs retrospectives should keep the learning there.

  The result is **lean six, full nine, strictly nested**: every lean heading appears in the full variant with
  the same name in the same order, and full only adds.

- **`pairs_with: []`, and the empty list is a finding rather than an omission.** **pm-skills ships no testing
  or QA skill at all** - finding EC-4 in [`STATE.md`](../../STATE.md), verified 2026-07-25 across all 68
  tracked skills. The family contract permits exactly one honest pairing, `deliver-edge-cases`, and permits
  it only "where that claim is true of that member": an edge-case catalog is an input to **planning**
  coverage, which is why `test-plan` claims it. A report of testing already finished has no such input to
  take, so this bundle declines the pairing rather than borrowing its sibling's, and the guide says so in as
  many words.

- **The worked example closes the family chain, as the contract requires.** `qa-docs` examples chain on one
  shared scenario, and onto the existing `delivery-docs` thread: Acme Analytics' "Saved Views for Dashboards".
  This example is a full-variant report of the effort the
  [test plan example](../test-plan/test-plan_example.md) scoped, running the cases the
  [test case example](../test-case/test-case_example.md) specifies, accounting for DEF-2291, the defect the
  [bug report example](../bug-report/bug-report_example.md) records. It completes the end-to-end thread from
  PRD to a shipping verdict, which is the most valuable thing this bundle adds. Every figure in it is
  illustrative and the load-bearing ones are marked so inline; its pass rate sits above a criteria table with
  one criterion graded **Not met** and left that way, because the total and the judgement disagreeing is the
  whole lesson.

- **Researched 2026-09-14** across six dimensions: origins and admission, structure, methodology lineage,
  debates and status, relationships and tooling, and the standing gap question read against real filled
  documents. [`test-summary-report_research-log.md`](test-summary-report_research-log.md) records **94 source
  records merged to 68 unique sources**, of which **58 are fetched-and-verified**, 5 are
  url-confirmed-not-read and 5 were not retrieved. Only fetched-and-verified sources are quoted anywhere in
  this bundle. Two null results are recorded there rather than quietly dropped: a fifth gap-dimension domain,
  DOT&E, was searched twice and returned **zero documents**, and an earlier fetch of one Kubernetes PDF
  returned garbled, apparently invented quotations, which the researcher discarded and reported rather than
  using. A defense-doctrine branch stayed out of reach entirely - a US Air Force test report author's guide
  was blocked on every retrieval attempt - and companion section 5 says to read that absence as a gap in the
  research, not as evidence the domain has nothing to say.

- **Status `beta`**, with zero real usage by anyone other than the author, per the family contract's rule that
  `beta` holds until one real usage cycle is recorded.
