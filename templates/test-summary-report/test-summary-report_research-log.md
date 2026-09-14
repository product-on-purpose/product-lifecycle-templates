# test-summary-report: research log

Research conducted 2026-09-14 across six dimensions (origins and admission, structure, methodology lineage,
debates and status, relationships and tooling, and the standing gap question). **94 source records merged to
72 unique sources**, of which **62 fetched-and-verified**, 5 url-confirmed-not-read and 5 not-retrieved.
Only `fetched-and-verified` sources are quoted anywhere in this bundle.

---

## What was read, what was not, and why that distinction carries this whole bundle

This bundle's governing standard is **sold, not published**, and the honest handling of that is the single
most important thing in this log. State the retrieval position precisely rather than letting a reader assume
the standard was consulted.

**READ, verbatim, from a legitimate free preview** (15 of ~93 pages, distributed by iTeh: front matter, the
complete Contents, Foreword, Introduction, the complete Clause 3 "Terms and definitions", and Clause 4.1):

- **ISO/IEC/IEEE 29119-3:2021's own definition**: *"3.9 test completion report / test summary report /
  report that provides a summary of the testing that was performed."*
- **Its table of contents**, showing *"7.4 Test completion report"* with ten subclauses - 7.4.1 Overview,
  7.4.2 Summary of testing performed, 7.4.3 Deviations from planned testing, 7.4.4 Test completion
  evaluation, 7.4.5 Factors that blocked progress, 7.4.6 Test measures, 7.4.7 Residual risks, 7.4.8 Test
  deliverables, 7.4.9 Reusable test assets, 7.4.10 Lessons learned - plus *"Annex G (informative) Test
  completion report"*.

**NOT READ, and nothing in this bundle may rest on it:**

- **The substantive text of Clause 7.4 or Annex G.** The subclause *headings* are read; what the standard
  *requires* under them, and what its worked example says, are not. The full standard is CHF 227.
- **IEEE 829, in any edition.** Every description of "IEEE 829's Test Summary Report structure" encountered
  in this research is second-hand, and those descriptions **disagree with each other**. This bundle
  therefore makes no claim about IEEE 829's section list.

**So the section design does NOT come from the standard.** It comes from **ISTQB's Certified Tester
Foundation Level syllabus**, published free by a named testing body, and **three editions of it were
fetched and read**: the current **v4.0.1** (2024-09-15), **v4.0** (2023-04-21), and the superseded **2018
v3.1.1**, which is kept only to show how the terminology changed. The current edition is the one the design
rests on and the one to cite; the superseded edition must not be cited for ISTQB's live position.

**An earlier version of this log named only v4.0.1 in this paragraph while its own Sources section carried
only the superseded v3.1.1.** That was a synthesis defect, not a research one - the de-duplication pass that
built the source list collapsed three distinct ISTQB syllabus editions into one entry because their author
and title strings agree for the first sixty characters, and it kept the wrong one. It also collapsed the
2013 and 2021 pages of the standard itself. All are restored and disambiguated. The four-lens review caught
the discrepancy by checking the prose against the entries rather than trusting either alone.

**A fact from ISO's own metadata, not from anyone's description:** the standard went from **127 pages (2013,
now withdrawn) to 84 pages (2021)**, with a rewritten abstract. The section design demonstrably changed
between editions, which is a further reason not to repeat a second-hand 2013-era section list.

---

## Claims flagged contested or time-bound

**This document type is actively contested by a named school of practitioners, and the bundle teaches that
rather than hiding it.**

- **Camp A, context-driven testing:** James Bach and Cem Kaner (who coined the term and co-authored its
  founding principles), Michael Bolton, and James Christie, whose 2014 conference talk triggered the
  **"Stop 29119"** campaign, organised by the International Society for Software Testing. **The petition
  asked ISO to suspend publication of Parts 4 and 5 and to withdraw Parts 1 to 3** - that is, to withdraw
  the very standard that defines this document. Its own framing: standards are *"political documents"*, and
  *"the imposition of a standard that imposes practices and views on a community that would not otherwise
  agree to them, is a political power play"*. Bolton's FAQ calls the standard *"an overstructured process
  model, focused on relentless, ponderous, wasteful bureaucracy and paperwork, with negligible content on
  actual testing"*.
- **Camp B:** the ISO/IEC/IEEE WG26 working group that wrote it, convened by Dr Stuart Reid, and the ISTQB
  certified-tester ecosystem. Rex Black is named as choosing to reform standards from inside rather than
  oppose them.

**A bundle that presented the test report as a settled genre would be making a claim this research
refutes.**

**IEEE 829-2008's status, verified at the source because this library has a standing obligation to get it
right.** The IEEE SA catalogue page reads **"Status: Superseded Standard"**, superseded by the 29119 parts.
**A WebSearch AI-synthesis separately claimed an "Inactive-Withdrawn" status dated 2024-10-28; that could
not be corroborated on a direct fetch of the page and is recorded here as unverified.** It is not used.

**IEEE 829-1998's abstract does not enumerate "Test Summary Report" by name**, so that source cannot be
used to confirm the document type even though it is frequently cited for it.

---

## Notes for the companion

**The honest framing.** This is a document type defined by a standard that a named school of practitioners
campaigned to have withdrawn. It is also a document type this library already promises four times over in
its own `test-plan` bundle. Both things are true and the companion carries both.

**The evidentiary spine, stated in the order it should be used:**

1. **That the document type exists** - from the standard's own Clause 3 definition, read verbatim.
2. **What it is called** - "test completion report" and "test summary report" are the standard's own
   synonyms, in the same definition.
3. **What sections it should carry** - from **ISTQB CTFL v4.0.1**, the current edition, read and free,
   *not* from the standard's unread normative text and *not* from the superseded 2018 syllabus.
4. **What the standard's own outline looks like** - citable only as a list of subclause *headings* from a
   table of contents, and labelled as such every time.

**The gap dimension's corpus, and an unusually honest note inside it.** Four filled, real reports were read
(an EAC/iBeta voting-system certification report, a Common Criteria certification report, an FDA 510(k)
summary, and a Trail of Bits security assessment), two in full and two partially with page ranges given. A
fifth candidate domain, DOT&E, **was searched twice and never fetched; zero documents retrieved** - recorded
as a null result rather than quietly dropped. **And an earlier fetch of one Kubernetes PDF returned garbled,
apparently invented quotations, which the researcher discarded and reported rather than using.** That is the
failure mode this library's reviews exist to catch, caught at source.

**The teaching point that distinguishes this document from its tooling.** A CI dashboard can produce every
number in a summary of execution. It cannot state what was **not** tested and why, what residual risk
someone is accepting, or whether to ship. The bundle's load-bearing sections are the ones a generated report
cannot fill.

---

## Sources

**[1] Michael Bolton, DevelopSense - Frequently-Asked Questions About the 29119 Controversy.** primary. **fetched-and-verified.**
`https://developsense.com/blog/2014/09/frequently-asked-questions-about-the-29119-controversy`
Supports: CDT camp's core objection to ISO 29119: documentation burden displaces actual testing work; names organizer role and Huib Schoots as resource curator
Quotable: "overstructured process model, focused on relentless, ponderous, wasteful bureaucracy and paperwork, with negligible content on actual testing" / "A moment that a tester spends on useless documentation is a moment in which she's not focused on identifying risks and finding problems" / "Huib Schoots is curating a collection of resources on the controversy"
Contested/time-bound: Bolton is a direct party to the dispute (opposition leader); this is his own advocacy FAQ, not a neutral account


**[2] James Bach, Satisfice - How Not to Standardize Testing (ISO 29119).** primary. **fetched-and-verified.**
`https://www.satisfice.com/blog/archives/1464`
Supports: CDT camp's legitimacy objection: WG26 excluded the context-driven school rather than resolving substantive disagreement
Quotable: "ISO 29119 is not a standard for testing. It cannot be a standard for testing" / "The burden is on those who claim that the craft can be standardized to study the craft and recognize and resolve the deep differences among us"
Contested/time-bound: Bach is the co-founder of the opposing school and a named target of the standard's exclusion claim; strongly partisan source


**[3] SD Times - The software testing schism.** practitioner. **fetched-and-verified.**
`https://sdtimes.com/applause/software-testing-schism/`
Supports: Trade-press account naming both camps directly: Stuart Reid/WG26 (standardizers) vs. James Bach/ISST (context-driven), and reports the petition exceeded its 1,000-signature goal within a month, reaching roughly 1,047 signatories.
Quotable: "The imposition of a 'standard' by one faction of the testing community, apart from being illegitimate, has the potential to allow them to control who gets to call themselves a tester." / "The standards require compliant testers to use risk-based testing, but do not restrict testers in how they perform this activity."
Contested/time-bound: Journalism from the height of the 2014 controversy; frames it explicitly as a 'schism,' i.e., an acknowledged, unresolved split.


**[4] Henrik Edgren, thetesteye.com - On ISO 29119 Content.** primary. **fetched-and-verified.**
`https://thetesteye.com/blog/2014/08/on-iso-29119-content/`
Supports: Most document-specific CDT critique found: documentation-for-its-own-sake, templates that obscure the substantive test content
Quotable: "The standard includes many documentation things and rules that are reasonable in some situations, but often will be just a waste of time. Good, useful documentation is good and useful, but following the standard will lead to documentation for its own sake." / "You have a document with many sections that looks good to non-testers, but doesn't say anything about the most important things (what are you trying to test, and how.)"
Contested/time-bound: Author claims direct familiarity with the standard's content; I have not independently verified he read the actual sold standard versus a draft


**[5] James Christie, clarotesting (WordPress) - Has opposition to ISO 29119 really died down?.** primary. **fetched-and-verified.**
`https://clarotesting.wordpress.com/2018/07/21/has-opposition-to-iso-29119-really-died-down/`
Supports: The controversy's status as of 2018: campaign visibility dropped from fatigue, not resolution; ISO did not substantively engage
Quotable: "there has been no change in the beliefs of the opposition" / "No, the opposition has not died down; it has not had anything credible to oppose" / "ISO have kept their collective heads down, tried to ride out the storm and emerged to claim that it was all a lot of fuss about nothing"
Contested/time-bound: Christie is the campaign's original instigator; this is a 2018 snapshot, not current (2026) status, which I could not verify


**[6] Context-Driven Testing (school's own site) - Principles - Context Driven Testing.** primary. **fetched-and-verified.**
`https://context-driven-testing.com/`
Supports: CDT's actual position on documentation: stakeholder-justified value, not blanket opposition to written artifacts
Quotable: "Standard 829 starts with a vision of good documentation and encourages the tester to modify what is created based on the needs of the stakeholders. Context-driven testing starts with the requirements of the stakeholders and the practical constraints and opportunities of the project." / "Test artifacts are worthwhile to the degree that they satisfy their stakeholders' relevant requirements."
Contested/time-bound: Undated principles page; represents the school's canonical self-description


**[7] Cem Kaner - What is context-driven testing?.** primary. **fetched-and-verified.**
`https://kaner.com/?p=49`
Supports: CDT co-founder's framing of documentation as one contextually-chosen deliverable among others, not a fixed requirement
Quotable: "Context-driven testers choose their testing objectives, techniques, and deliverables (including test documentation) by looking first to the details of the specific situation"
Contested/time-bound: Kaner is a CDT co-founder; self-description, not neutral


**[8] test-summary-repor, istqb-glossary.page (unofficial mirror of ISTQB Glossary content) - Test Summary Report - ISTQB Glossary (third-party mirror).** reference. **fetched-and-verified.**
`https://istqb-glossary.page/test-summary-report/`
Supports: Verbatim ISTQB Glossary definition of test summary report, and its sourcing to 'Glossary v1 (present in Advanced Test Manager 2012 syllabus)' - used for the naming-drift finding versus the current CTFL v4.0 syllabus's exclusive use of 'test completion report'.
Quotable: "A document summarizing testing activities and results. It also contains an evaluation of the corresponding test items against exit criteria."
Contested/time-bound: Third-party mirror, not the official glossary.istqb.org domain (which is a JS app this pass could not read directly) - downgraded from the 'primary' tier this library's existing test-plan bundle gave it.


**[9] TestRail (vendor) - How to Write a Test Summary Report: Template and Real Examples.** vendor. **fetched-and-verified.**
`https://www.testrail.com/blog/test-summary-report/`
Supports: Directly names the team-vs-audit-trail split, framing both as legitimate complementary purposes of the same document type
Quotable: "A test progress report communicates the status of testing while testing is still underway. A test completion or summary report communicates the outcome of a completed testing effort or significant testing milestone." / "A formal test summary becomes useful when teams need to share testing results beyond a single iteration or the immediate team. It's also useful for supporting external requirements, such as audits, customer sign-offs, regulatory reviews, and contractual obligations."
Contested/time-bound: TestRail sells test-management/reporting tooling, so has a commercial interest in the artifact's continued relevance


**[10] Wikipedia contributors - ISO/IEC 29119.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/ISO/IEC_29119`
Supports: Encyclopedic summary of the standard, the Stop29119 petition's organizers, and named objections including documentation-over-testing focus
Quotable: "heavy focus on documentation will detract from the actual process of software testing" / "lack of true consensus of content - as required by ISO/IEC - among professional testers"
Contested/time-bound: Wikipedia content can change; treat as a snapshot at time of fetch (2026-09-14), not a permanent record


**[11] Michael Bolton, DevelopSense - Braiding The Stories (Test Reporting Part 2).** primary. **fetched-and-verified.**
`https://developsense.com/blog/2012/02/braiding-the-stories`
Supports: CDT's model of what a test report is FOR: three-part narrative for decision-makers, explicitly contrasted against pass/fail-ratio compliance reporting
Quotable: "managers need to know about problems that threaten the value of the product and the on-time, successful completion of the project"
Contested/time-bound: Bolton's own methodology (Rapid Software Testing), not an industry consensus view


**[12] IEEE Standards Association / ISO/IEC JTC 1 - IEEE/ISO/IEC International Standard for Software testing  -  Part 3: Test documentation (29119-3-2021).** standards. **fetched-and-verified.**
`https://standards.ieee.org/ieee/29119-3/7499/`
Supports: The free scope statement for 29119-3 (2021 edition, active status)  -  confirms the standard's own stated purpose without reading the paywalled body text.
Quotable: "The purpose of the ISO/IEC/IEEE 29119 series of software testing standards is to define an internationally-agreed set of standards for software testing that can be used by any organization when performing any form of software testing." / "ISO/IEC/IEEE 29119-3 includes templates and examples of test documentation."
Contested/time-bound: This is the abstract only; the templates/examples themselves are not visible here and were never read in this research.


**[13] Michael Bolton, DevelopSense - Dramatis Personae.** primary. **fetched-and-verified.**
`https://developsense.com/blog/2014/09/dramatis-personae`
Supports: Names the WG26 editorial roster (Reid, Hass, Daigl, Veeraraghavan, Murnane, Kwon, Liu, Hagar) and the opposition's conflict-of-interest argument against them
Quotable: "if a handful of consultancies of any size were to use the ISO standards process to set the terms...it would raise a plausible perception of conflict of interest"
Contested/time-bound: Bolton's own characterization of the working group's composition and motives; partisan framing


**[14] International Society for Software Testing (ISST), hosted on context-driven-testing.com - Please sign the Petition to Stop ISO 29119.** primary. **fetched-and-verified.**
`https://context-driven-testing.com/please-sign-the-petition-to-stop-iso-29119/`
Supports: The petition's own stated ask (suspend Parts 4-5, withdraw Parts 1-3) and its framing of the dispute as a political/philosophical clash, not narrowly a documentation complaint
Quotable: "The imposition of a standard that imposes practices and views on a community that would not otherwise agree to them, is a political power play." / "Context-driven testing developed as the antithesis of what is being pushed through ISO. They represent opposite points of view."
Contested/time-bound: This is the advocacy document itself, organized by the opposition; not a neutral account of the standard's actual content


**[15] International Organization for Standardization (ISO) [2013] - ISO/IEC/IEEE 29119-3:2013 standard page (Withdrawn).** standards. **fetched-and-verified.**
`https://www.iso.org/standard/56737.html`
Supports: Confirms the 2013 edition's abstract, page count (127), and withdrawn status directly from ISO -- the only thing about this standard confirmed firsthand in this research; full text remains paywalled/preview-only.
Quotable: "ISO/IEC/IEEE 29119-3:2013 includes templates and examples of test documentation. The templates are arranged within clauses reflecting the overall test process description structure in ISO/IEC/IEEE 29119-2..." / "Annex A contains outlines of the contents of each document." / "Status: Withdrawn"
Contested/time-bound: Withdrawn 2021, superseded by the 2021 edition below; full text never read by anyone in this research.


**[16] International Organization for Standardization (ISO) [2021] - ISO/IEC/IEEE 29119-3:2021 standard page (current edition).** standards. **fetched-and-verified.**
`https://www.iso.org/standard/79429.html`
Supports: Confirms the current edition's shorter abstract, reduced page count (84, down from 127), Published status, and CHF 227 price -- direct evidence the standard's content changed between editions, from ISO's own metadata rather than a secondary description.
Quotable: "This document specifies software test documentation templates that can be used for any organization, project or testing activity." / "Number of pages : 84" / "PDF + ePub Paper CHF 227"
Contested/time-bound: Published 2021-10; full text never read by anyone in this research pass.


**[17] International Software Testing Qualifications Board (ISTQB) - ISTQB Glossary: "test summary report" and "test completion report".** standards. **not-retrieved.**
`https://glossary.istqb.org/en/term/test-summary-report-3`
Supports: ISTQB's own professional-body definitions of these terms should exist and would be a strong 'professional-body courseware' source, but the glossary is a client-side JavaScript application; two independent retrieval attempts (direct fetch and browser-emulated fetch) returned no body text. No definition text is used from this source.
Contested/time-bound: Pages return HTTP 200 but render no server-delivered content; genuinely could not be read this pass, as distinct from being blocked.


**[18] Keith Klain, Quality Remarks - The Petition to Stop ISO 29119.** practitioner. **not-retrieved.**
`https://qualityremarks.com/the-petition-to-stop-iso-29119/`
Supports: Would have added a third independent account of the petition's organization, but the page returned HTTP 404
Contested/time-bound: URL may have changed or been removed since indexing; not usable as a source


**[19] ipetitions.com host page - Petition Stop 29119.** reference. **url-confirmed-not-read.**
`https://www.ipetitions.com/petition/stop29119`
Supports: Confirms the petition's hosting URL exists (referenced consistently across multiple other fetched sources); the page itself returned HTTP 403 to automated fetch, so its exact live text/signature count was not read directly  -  signature figures used below are attributed to SD Times instead.
Contested/time-bound: Not read; do not treat any number attributed to 'the petition page' in this research as coming from this URL directly.


**[20] IEEE Standards Association - IEEE SA  -  IEEE 829-2008 standard catalog page.** standards. **fetched-and-verified.**
`https://standards.ieee.org/ieee/829/3787/`
Supports: Authoritative status determination for IEEE 829-2008, per the task's instruction to use the IEEE SA page itself rather than blogs.
Quotable: "Status: Superseded Standard" / "Superseding: ISO/IEC/IEEE 29119-1-2013, ISO/IEC/IEEE 29119-2-2013, ISO/IEC/IEEE 29119-3-2013, ISO/IEC/IEEE 29119-4-2015" / "PAR Approval: 2005-06-09" / "Board Approval: 2008-03-27"
Contested/time-bound: Fetched twice, both times the field read 'Superseded Standard' with no distinct withdrawal date shown. A WebSearch AI-synthesis (not this page) separately claimed an 'Inactive-Withdrawn' status dated 2024-10-28; that claim could not be corroborated on direct fetch of this page and is treated as unverified/contested (see contested_claims).


**[21] ANSI Webstore - ISO/IEC/IEEE 29119-3:2013 purchase listing.** vendor. **url-confirmed-not-read.**
`https://webstore.ansi.org/standards/iso/ISOIECIEEE291192013-1502466`
Supports: Independent confirmation that a second commercial reseller lists 29119-3 as a paid purchase, reinforcing the paywall finding; page returned HTTP 403 and was not read.
Contested/time-bound: Not contested; unread.


**[22] Wikipedia contributors - Software test documentation.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Software_test_documentation`
Supports: Describes IEEE 829-2008 (a different, later edition) as specifying TEN document types under Master/Level naming, never using the term 'Test Summary Report,' and states the standard did not mandate content adequacy.
Quotable: "Note: IEEE 829-2008 has been superseded by ISO/IEC/IEEE 29119-3:2013." / "Master Test Report (MTR): To summarise the results of the levels of the designated testing activities and to provide evaluations based on these results..." / "The standard specified the format of these documents, but did not stipulate whether they must all be produced, nor did it include any criteria regarding adequate content for these documents."
Contested/time-bound: Wikipedia; a tertiary source. Describes a different edition (2008) than the two practitioner sources above (1998), which is itself part of the disagreement, not a resolution of it.


**[23] ZetCode - IEEE 829 Tutorial: Test Documentation Standard Explained.** vendor. **fetched-and-verified.**
`https://zetcode.com/terms-testing/ieee-829/`
Supports: One data point in the demonstrated secondary-source disagreement over how many document types IEEE 829 defined (this page: eight).
Quotable: "It outlines eight key document types that cover the entire testing process from planning to execution and reporting."
Contested/time-bound: Directly contested by futureskill.blog (seven) and Wikipedia (ten)  -  used only to evidence the paywall-driven disagreement hazard, never as a factual claim about the standard's actual contents.


**[24] Future Skill (blog) - IEEE 829  -  Standard for Software Test Documentation.** vendor. **fetched-and-verified.**
`https://futureskill.blog/standards/ieee-829/`
Supports: Second data point in the secondary-source disagreement: this page lists seven main document types (Test Plan, Test Design Spec, Test Case Spec, Test Procedure Spec, Test Log, Test Incident Report, Test Summary Report), omitting the Test Item Transmittal Report that ZetCode includes.
Quotable: "The standard outlines a comprehensive set of documents that testers need to create at various stages of the testing process."
Contested/time-bound: Directly contradicts ZetCode's count of eight and Wikipedia's count of ten from the same never-read standard  -  the exact hazard flagged in the task brief.


**[25] microTOOL GmbH - Test Documentation with ISO/IEC/IEEE 29119-3:2021.** vendor. **fetched-and-verified.**
`https://www.microtool.de/en/document-management/test-documentation-with-iso-iec-ieee-29119-32021/`
Supports: Confirms supersession date and flags one specific conceptual shift (test model vs. test condition) between the two standards, plus that 29119-3:2021 provides a mapping table between old and new terminology for migration.
Quotable: "Since 2013, IEEE 829 has been replaced by ISO/IEC/IEEE 29119-3." / "The concept 'test model' replaces the concept 'test condition'."
Contested/time-bound: Vendor marketing content promoting document-management tooling; treated as corroborating detail, not sole evidence.


**[26] Reqtest - ISO/IEC/IEEE 29119: Creating a standard approach to test software.** vendor. **fetched-and-verified.**
`https://reqtest.com/en/knowledgebase/isoiecieee-29119-creating-a-standard-approach-to-test-software/`
Supports: Free-scope statement of 29119's stated intent: unify fragmented, conflicting testing vocabularies/processes industry-wide, and states 29119-3 explicitly supersedes and builds on IEEE 829.
Quotable: "ISO/IEC/IEEE 29119 is a new standard series that seeks to become the common language of software testing organisation." / "Unfortunately, software testing is plagued by many divergences in definitions, processes and procedures."
Contested/time-bound: Vendor content; the 'common language' framing is exactly what critics (see context-driven sources below) dispute as false consensus.


**[27] Jürgen Großmann, Michael Felderer, Johannes Viehmann, Ina Schieferdecker (Fraunhofer FOKUS / Univ. Innsbruck / TU Berlin) - A Taxonomy to Assess and Tailor Risk-based Testing in Recent Testing Standards.** academic. **fetched-and-verified.**
`https://arxiv.org/pdf/1905.10676`
Supports: Academic (peer-adjacent, arXiv preprint) confirmation of the 29119 series' five-part structure and its risk-based, process-integrated intent  -  read from a free paper, not the paywalled standard itself.
Quotable: "The new international series of software testing standards ISO/IEC/IEEE 29119 consists of five parts, which cover (1) Concepts & Definitions, (2) Test Processes, (3) Test Documentation, (4) Test Techniques, as well as (5) Keyword Driven Testing." / "ISO/IEC/IEEE 29119 explicitly specifies risk considerations to be an integral part of the test planning process."
Contested/time-bound: Describes only the outer structure of the series (which is publicly documented) and never claims to describe Part 3's internal document contents  -  consistent with the paywall rule.


**[28] Jannik Fischbach, Henning Femmer, Daniel Mendez, Davide Fucci, Andreas Vogelsang  -  ESEM '20 (ACM/IEEE) - What Makes Agile Test Artifacts Useful? An Activity-Based Quality Model from a Practitioners' Perspective.** academic. **fetched-and-verified.**
`https://arxiv.org/pdf/2009.01722`
Supports: Direct, empirical (18 practitioners, 12 companies, 7 domains, published ESEM 2020) evidence that test documentation/reporting is a live, named artifact in agile teams  -  used by a 'Test Lead' for Test Reporting and Estimation Planning  -  and that its absence causes real problems, with regulated industries (insurance) explicitly needing the durable, cross-level, historical record that a live CI dashboard does not by itself retain.
Quotable: "Test results and effort are not properly documented. The interviews revealed that there is a common problem that test results are not properly documented at all test levels." / "This poses a problem especially in regulatory environments... companies in the insurance industry need to document the functionality of the different software versions and prove which tests have been performed to verify that functionality." / "practitioners 'need the historic information of all test assets.'" / "Each test type needs to be linked to its respective test result. Specifically, the Test documentation needs to contain the corresponding result for each Unit test, Integration test, System test and Acceptance test to provide a comprehensive overview of all testing levels at any time during the life cycle of the software."
Contested/time-bound: A qualitative interview study (18 practitioners across 12 companies)  -  explicitly flagged by the authors themselves as not statistically generalizable, and specific to the practitioners' own agile contexts circa 2020.


**[29] John Ferguson Smart - Living Documentation: it's not just about test reports.** practitioner. **fetched-and-verified.**
`https://johnfergusonsmart.com/living-documentation-not-just-test-reports/`
Supports: Direct practitioner argument (BDD/living-documentation camp, 2018) that traditional post-hoc test reports are a 'legacy of Waterfall' poorly suited to collaborative agile work  -  but explicitly carves out regulated environments as still needing exhaustive, detailed documentation, which lines up with the academic paper's insurance-industry finding.
Quotable: "[Traditional test reports] force us to think in terms of tests that happen only post-implementation." / "Of course there are some exceptions to this rule. For example in regulated environments, living documentation will often be more exhaustive and detailed."
Contested/time-bound: A named, argued position within the still-live displacement debate, not a neutral finding  -  represents the 'living documentation replaces reports' camp.


**[30] Martin Fowler - Continuous Integration.** practitioner. **fetched-and-verified.**
`https://martinfowler.com/articles/continuousIntegration.html`
Supports: Canonical CI reference (rewritten Jan 2024) describing how CI dashboards/build radiators provide the continuous, always-on visibility that displaced the need to wait for a compiled end-of-cycle report for day-to-day status.
Quotable: "CI Services have dashboards that allow everyone to see the state of any builds they are running." / "Teams that share a physical space often have some kind of always-on physical display for the build." / "As well as the current state of the build, these displays can show useful information about recent history."
Contested/time-bound: Describes current-state and recent-history visibility, not a durable point-in-time audit artifact  -  the gap this research was asked to identify.


**[31] Carl Nygard (published on martinfowler.com) - Compliance in a DevOps Culture.** practitioner. **fetched-and-verified.**
`https://martinfowler.com/articles/devops-compliance.html`
Supports: Names the precise mechanism of displacement for compliance/audit-style reporting: continuous point-of-change validation plus a queryable 'System of Record' of evidence replaces periodic point-in-time reports for routine controls  -  while policy exceptions and decisions are the one thing that still gets written down as a document, not just logged.
Quotable: "Validation of Compliance is verified at the point of change, for example by Kubernetes operators which manage non-Kubernetes infrastructure components." / "Auditing the process also becomes a straightforward review of the logs of the deployment step." / "Each application has its own set of exceptions to the master list of controls, managed jointly by the team and the Office of Compliance."
Contested/time-bound: Published Nov 2021; describes a target-state DevOps compliance pattern the author advocates, not a universal empirical finding.


**[32] Keith Klain (Quality Remarks), moderating Iain McCowatt, Michael Bolton, James Christie, Griffin Jones, Ilari Aegerter - ISO 29119 Roundtable Discussion  -  Part III.** practitioner. **fetched-and-verified.**
`https://qualityremarks.com/iso-29119-roundtable-discussion-part-iii/`
Supports: Multi-voice primary transcript naming the organized opposition (International Society for Software Testing/ISST leadership) and its core claims: exclusionary drafting process, no cited evidence base, and innovation-stifling risk.
Quotable: "The mechanism for which its (29119) is created is odious." / "if we do so, what we will do is stifle innovation, and everybody's going to suffer." / "They aren't even pretending that there is any evidence."
Contested/time-bound: This particular installment is critics-only by the host's own selection; the standardizer side is represented elsewhere (SD Times) rather than in this transcript.


**[33] James Christie (Claro Testing blog) - Why ISO 29119 is a flawed quality standard.** practitioner. **fetched-and-verified.**
`https://clarotesting.wordpress.com/2016/04/07/why-iso-29119-is-a-flawed-quality-standard/`
Supports: Shows the controversy was not a one-off 2014 flashpoint: a substantive theoretical critique (citing regulatory-standards theory, Polanyi/Collins on tacit knowledge) published in 2016, two years after the petition, arguing rule-based prescription displaces the actual goal (quality) with compliance to the rule.
Quotable: "Give test managers a detailed standard, and they'll start to see the job as following the standard, not testing."
Contested/time-bound: Dated April 2016; author explicitly references his own history of 'attacking ISO 29119' publicly, i.e., a sustained campaign rather than a single event.


**[34] James Bach (Satisfice, Inc. blog) - Stuart Reid's Bizarre Plea.** practitioner. **fetched-and-verified.**
`https://www.satisfice.com/blog/archives/457`
Supports: Independent corroboration that the dispute between the standards camp (Stuart Reid, WG26 convener) and the context-driven camp was personal/direct, not only abstract  -  Bach characterizes Reid as unwilling to engage substantively with counterarguments.
Quotable: "he thought I was pretending to believe things that I don't believe, just to be difficult"
Contested/time-bound: Does not contain the specific Reid petition-response text this research went looking for; used only for the narrower claim about the Bach-Reid exchange dynamic.


**[35] TechWell Insights - How I Learned to Stop Worrying and Love ISO 29119.** practitioner. **url-confirmed-not-read.**
`https://www.techwell.com/techwell-insights/2014/09/how-i-learned-stop-worrying-and-love-iso-29119`
Supports: Title alone (from search index) suggests a third, more conciliatory position existed in trade press at the time; page returned HTTP 403 and was not read, so no claim in this research rests on its content.
Contested/time-bound: Unread  -  flagged so it is not mistaken for verified material.


**[36] iBeta Quality Assurance (EAC-accredited Voting System Test Laboratory), submitted to the U.S. Election Assistance Commission - Dominion Voting Systems Sequoia WinEDS 4.0  -  VSTL Certification Test Report (v2.0).** primary. **fetched-and-verified.**
`https://www.eac.gov/sites/default/files/voting_system/files/VSTL%20WinEDS%204.0%20Test%20Report%20v2.0%20package.pdf`
Supports: Requirement-level disposition taxonomy (Accept/Reject/NA/Pending/Out of Scope) with mandatory explanatory notes; explicit rule that unsupported-but-applicable requirements are marked Accept-with-comment rather than silently NA; exclusions list stating what was not tested and why; cover-page scope caveat on modified configurations; signed vendor warrant binding as-tested to as-deployed; per-unit serial-number reproducibility across initial and regression test matrices; named external subcontractors for out-of-accreditation-scope testing; self-trace table against the governing VSTL Program Manual; named, signed recommendation with a voluntary out-of-scope disclosure.
Quotable: "Test Results in this report apply to the voting system configuration tested. Testing of voting systems that have been modified may or may not produce the same test results. This report shall not be reproduced, except in full." / "The following functions are excluded from the WinEDS 4.0 voting system and therefore not tested in this certification effort: Access to incomplete election returns or interactive queries; Telecommunications: No voter authentication, ballot definition, individual vote records, or voter lists are transmitted via public telecommunications; and Shared Operating Environment: WinEDS 4.0 does not share an environment with other data processing functions." / "Non-core hardware environmental testing is outside iBeta's test accreditation scope as a VSTL. This testing was performed at the following subcontractors: Criterion Technology...Oracle Advanced Product Testing (APT)...Wyle Laboratories...Intertek Testing Services NA, Inc." / "Requirements are marked as follows: Accept: met the VSS 2002 requirement; Reject: did not meet the VSS 2002 requirement; NA: the requirement is not applicable to the voting system type submitted for Certification Testing; Pending: VSS 2002 requirements that cannot be completed by the VSTL until after Certification; Out of Scope: VSS 2002 requirements which are performed by entities other than the VSTL. Requirements marked Reject, NA, Pending or Out of Scope shall include an explanatory note."
Contested/time-bound: This is v2.0 of the report, submitted to EAC and pending acceptance; no final EAC certification number appears in the pages read (Appendix K, where it would appear, was not read).


**[37] Communications Security Establishment Canada, Canadian Common Criteria Evaluation and Certification Scheme (CCS) - Certification Report: EAL 3+ Evaluation of Extreme Networks ExtremeXOS Network Operating System v12.3.6.2.** primary. **fetched-and-verified.**
`https://www.commoncriteriaportal.org/files/epfiles/383-4-146%20CR%20v1.0e.pdf`
Supports: Explicit non-warranty disclaimer separating certification from endorsement; explicit threat-model scope boundary distinct from a pass/fail verdict; two-tier public-summary/private-evidence-record structure, disclosed via footnote; certification body's witnessing of a sample of testing as an independence check; named advisory recommendation surviving the pass verdict.
Quotable: "This certification report, and its associated certificate, apply only to the identified version and release of the product in its evaluated configuration... This report, and its associated certificate, are not an endorsement of the IT product by the Communications Security Establishment Canada... and no warranty for the IT product... is either expressed or implied." / "EXOS offers protection against inadvertent or casual attempts to breach system security by unsophisticated attackers possessing basic attack potential. EXOS is not intended for situations which involve determined attempts by hostile or well-funded attackers using sophisticated attack techniques." / "The ETR is a CCS document that contains information proprietary to the developer and/or the evaluator, and is not releasable for public review." / "The CCS Certification Body witnessed a portion of the independent testing. The detailed testing activities, including configurations, procedures, test cases, expected results and observed results are documented in a separate Test Results document."
Contested/time-bound: Dated 28 March 2012; applies only to EXOS v12.3.6.2 in the listed evaluated configuration.


**[38] United Orthopedic Corporation (submitter); U.S. Food and Drug Administration, Center for Devices and Radiological Health (clearance letter) - 510(k) Summary of Safety and Effectiveness Data  -  UTF Stem, reduced, #0, #00 (K163193).** primary. **fetched-and-verified.**
`https://www.accessdata.fda.gov/cdrh_docs/pdf16/K163193.pdf`
Supports: Even a minimal, naive-shaped report is structurally required to affirmatively state an absence (no clinical data) rather than stay silent about it; shows the floor case against which richer reports (EAC, CC) can be contrasted.
Quotable: "Non-clinical Performance: Tests as follows were conducted to evaluate the safety and effectiveness of the subjected device: a. Stem Fatigue Test b. Neck Fatigue Test c. Range of Motion d. Bacterial endotoxin testing was conducted and met the endotoxin limit as specified in USP <161>" / "Clinical Performance Data/Information: None provided as a basis for substantial equivalence." / "We have reviewed your Section 510(k) premarket notification... and have determined the device is substantially equivalent... Please be advised that FDA's issuance of a substantial equivalence determination does not mean that FDA has made a determination that your device complies with other requirements of the Act or any Federal statutes and regulations administered by other Federal agencies."
Contested/time-bound: Clearance letter dated June 8, 2017; applies to this specific size-extension device only, via predicate comparison, not independent clinical evidence.


**[39] Trail of Bits, prepared for the Kubernetes Security Working Group - Kubernetes Security Assessment.** practitioner. **fetched-and-verified.**
`https://raw.githubusercontent.com/magnologan/cncf-security-audits/main/K8s/Kubernetes%20Final%20Report.pdf`
Supports: Explicit breadth-vs-depth coverage disclosure warning readers not to read unaudited areas as cleared; 'Undetermined' as a first-class severity/difficulty value distinct from 'Low'; structured engagement-metadata dashboard paired with a chronological week-by-week narrative of the actual test campaign; version-pinned scope for reproducibility.
Quotable: "The scope of review for each component adhered to the guidelines outlined in the Kubernetes Bug Bounty documentation, focusing on Kubernetes-specific bugs and avoiding container- or networking-implementation-dependent bugs." / "Due to the scope of the assessment and size of the codebase, bug finding was focused on identifying component implementations which were 'obviously wrong.' Given this focus, codebase coverage emphasized breadth instead of depth. Portions of the codebase outside of the control areas received minimal to no coverage. Future assessments of those components will likely yield further findings and help produce more accurate models of the Kubernetes internals." / "Undetermined: The extent of the risk was not determined during this engagement." / "Undetermined: The difficulty of exploit was not determined during this engagement."
Contested/time-bound: Assessed Kubernetes v1.13.4 (May 2019); a third-party commissioned security assessment, not a release-qualification/QA test-summary report  -  stands in only loosely for the task's named open-source domain.


**[40] ISO/IEC/IEEE (joint publication); free-preview sample distributed by iTeh, Inc. - ISO/IEC/IEEE 29119-3:2021(E), Second edition  -  Software and systems engineering  -  Software testing  -  Part 3: Test documentation (free preview, 15 of ~93 pages).** standards. **fetched-and-verified.**
`https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf`
Supports: Directly settles the admission question for the standards tier. The standard's own Clause 3 (Terms and definitions, freely previewed) defines the term; the Table of Contents (freely previewed) shows it as a numbered clause with a worked example annex.
Quotable: "3.9 test completion report / test summary report / report that provides a summary of the testing that was performed" / "7.4 Test completion report ... 18" / "7.4.1 Overview / 7.4.2 Summary of testing performed / 7.4.3 Deviations from planned testing / 7.4.4 Test completion evaluation / 7.4.5 Factors that blocked progress / 7.4.6 Test measures / 7.4.7 Residual risks / 7.4.8 Test deliverables / 7.4.9 Reusable test assets / 7.4.10 Lessons learned" / "Annex G (informative) Test completion report ... 58"
Contested/time-bound: This is a legitimate FREE PREVIEW, not the full standard: it runs 15 pages (title page, copyright notice, full Contents, Foreword, Introduction, the complete Clause 3 'Terms and definitions,' and Clause 4.1 'Conformance') and stops there. The preview does NOT include the substantive text of Clause 7.4 or Annex G  -  I read the clause-3 definition and the table-of-contents structure verbatim, but I have NOT read what Annex G's worked example or clause 7.4's normative requirements actually say beyond their subclause headings. The full standard (all ~93 pages) is sold by ISO/IEC/IEEE, not freely published; no claim in this report rests on unread paywalled content.


**[41] IEEE Standards Association - IEEE SA  -  IEEE 829-1998 standard catalog page.** standards. **fetched-and-verified.**
`https://standards.ieee.org/ieee/829/1218/`
Supports: Confirms IEEE 829-1998 was itself superseded by 829-2008; its abstract does not name individual document types (so does not independently confirm a 'Test Summary Report' document by name).
Quotable: "Status: Superseded Standard" / "Superseding: 829-1998" / "A set of basic software test documents is described. This standard specifies the form and content of individual test documents. It does not specify the required set of test documents."
Contested/time-bound: The abstract text quoted is generic and does NOT enumerate 'Test Summary Report' or any other individual document name  -  so this source cannot itself be used to confirm IEEE 829 names that document type.


**[42] v3.1.1, International Software Testing Qualifications Board (ISTQB), hosted by ASTQB - Certified Tester Foundation Level (CTFL) Syllabus, Version 2018 v3.1.1 (released 2021-07-01)  -  superseded.** practitioner. **fetched-and-verified.**
`https://astqb.org/assets/documents/CTFL-2018-Syllabus.pdf`
Supports: A named testing body (ISTQB) publishing, freely, a written structure ('typical test summary reports may include') for the end-of-testing report, and explicitly cross-mapping its own term to 29119-3's term.
Quotable: "5.3.2 Purposes, Contents, and Audiences for Test Reports" / "Typical test summary reports may include: Summary of testing performed / Information on what occurred during a test period / Deviations from plan, including deviations in schedule, duration, or effort of test activities / Status of testing and product quality with respect to the exit criteria or definition of done / Factors that have blocked or continue to block progress / Metrics of defects, test cases, test coverage, activity progress, and resource consumption / Residual risks / Reusable test work products produced" / "ISO standard (ISO/IEC/IEEE 29119-3) refers to two types of test reports, test progress reports and test completion reports (called test summary reports in this syllabus), and contains structures and examples for each type." / "ISO/IEC/IEEE 29119 replaces IEEE Standard 829."
Contested/time-bound: SUPERSEDED as of 2023-04-21 by CTFL v4.0 (errata v4.0.1, 2024-09-15). Kept in this report only to show terminology history; the current syllabus (below) is the one a bundle should cite as ISTQB's live position.


**[43] v4.0.1, International Software Testing Qualifications Board (ISTQB), hosted by ASTQB - Certified Tester Foundation Level (CTFL) Syllabus v4.0.1 (2024-09-15)  -  current edition.** practitioner. **fetched-and-verified.**
`https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf`
Supports: THE READABLE NAMED SOURCE this bundle should actually rest on: current, free, official ISTQB syllabus, giving a full enumerated structure for 'test completion report' and explicitly naming ISO/IEC/IEEE 29119-3 as the standard with templates for it.
Quotable: "5.3.2. Purpose, Content and Audience for Test Reports" / "A test completion report is prepared during test completion, when a project, test level, or test type is complete and when, ideally, its exit criteria have been met. This report uses test progress reports and other data. Typical test completion reports include: Test summary / Testing and product quality evaluation based on the original test plan (i.e., test objectives and exit criteria) / Deviations from the test plan (e.g., differences from the planned test schedule, duration, and effort) / Testing impediments and workarounds / Test metrics based on test progress reports / Unmitigated risks, defects not fixed / Lessons learned that are relevant to the testing" / "Different audiences require different information in the reports and influence the degree of formality and the frequency of test reporting. Test progress reporting to others in the same team is often frequent and informal, while test completion reporting follows a set template and occurs only once." / "The ISO/IEC/IEEE 29119-3 standard includes templates and examples for test progress reports (called test status reports) and test completion reports."
Contested/time-bound: Notably: zero occurrences of the phrase 'test summary report' anywhere in this 78-page document (grep-confirmed)  -  v4.0.1 has fully retired that name in favor of 'test completion report,' matching 29119-3's primary term. This is a documented terminology change from the 2018 v3.1.1 edition above, not a disagreement.


**[44] ISO (committee.iso.org) - ISO/IEC/IEEE 29119 series page (ISO committee mirror).** standards. **fetched-and-verified.**
`https://committee.iso.org/es/sites/isoorg/contents/data/standard/07/94/79429.html`
Supports: Free ISO scope/abstract confirmation (the main iso.org/standard pages 403'd for this session) that 29119-3 defines test documentation templates generally.
Quotable: "This document specifies software test documentation templates that can be used for any organization, project or testing activity. It describes the test documentation that is an output of the processes specified in ISO/IEC/IEEE 29119-2."
Contested/time-bound: Does not itself name 'Test Completion Report'  -  that confirmation came from the iTeh preview's Clause 3 and Table of Contents instead.


**[45] Tricentis (guest contributor Inimfon Willie) - What is a test summary report and how do you write one?.** vendor. **fetched-and-verified.**
`https://www.tricentis.com/learn/test-summary-report`
Supports: Full body read directly: a tool vendor's own how-to guide for the human-authored document, distinguishing it explicitly from the 'customizable dashboards' its own tool (qTest) generates, and modeling the recommendation/exit-criteria-confirmation content a dashboard cannot produce.
Quotable: "A test summary report (TSR) is a document that explains what was tested, what passed, what failed, and how the application meets - or falls short of - the defined release goals." / "Summary and recommendations. Give a final view of the application's health. Highlight any blockers, critical concerns, and readiness for release. Include clear next steps." / "We should fix BUG-2031 before releasing... Based on the results, the team recommends moving forward with the release." / "Use tools like Tricentis qTest to centralize your testing - manage manual and automated runs, log defects, and generate clear, customizable dashboards that make your status and coverage easy to see and act on."
Contested/time-bound: Vendor content; treat 'when a test summary report is well written, it becomes a tool that helps teams... make confident release decisions' as vendor framing consistent with, but rhetorically stronger than, the primary/standards sources' 'contributes to' language.


**[46] Multiple independent commercial/blog authors - Various vendor/blog enumerations of IEEE 829's Test Summary Report sections (professionalqa.com, zetcode.com, pdf4pro.com, reqtest.com, StickyMinds, etc.).** vendor. **not-retrieved.**
`https://www.professionalqa.com/test-summary-report`
Supports: Illustrates exactly the hazard the task warned about: multiple named vendors independently claim to enumerate IEEE 829's Test Summary Report section list, and per the task's own prior finding these enumerations disagree with each other (e.g. one claims exactly 8 sections: identifier, executive summary, variances, comprehensiveness assessment, defect summary, evaluation, timeline, approvals). None of these lists were fetched and read in full in this pass, and none is treated as IEEE 829's actual content.
Contested/time-bound: These are the disagreeing secondary enumerations the task explicitly pre-flagged. Deliberately NOT adopted as IEEE 829's contents anywhere in this report.


**[47] v4.0, International Software Testing Qualifications Board (ISTQB), hosted by GASQ - ISTQB Certified Tester Foundation Level Syllabus v4.0 (2023-04-21).** standards. **fetched-and-verified.**
`https://www.gasq.org/files/content/gasq/downloads/certification/ISTQB/Foundation%20Level/ISTQB_CTFL_Syllabus-v4.0%20.pdf`
Supports: Primary sourcing for: test completion report vs test progress/status report definitions and contents (5.3.2), test monitoring/control/completion (5.3), work-product taxonomy separating test plan / defect reports / test completion report (1.4.1, 1.4.3), testing's contribution to the release decision (1.2.1), and dashboards-vs-formal-reports as separate communication channels (5.3.3). Freely available official syllabus, not paywalled.
Quotable: "Test progress reports support the ongoing control of the testing and must provide enough information to make modifications to the test schedule, resources, or test plan, when such changes are needed due to deviation from the plan or changed circumstances. Test completion reports summarize a specific stage of testing (e.g., test level, test cycle, iteration) and can give information for subsequent testing." / "A test completion report is prepared during test completion, when a project, test level, or test type is complete and when, ideally, its exit criteria have been met." / "Testing provides a means of directly evaluating the quality of a test object at various stages in the SDLC. These measures are used as part of a larger project management activity, contributing to decisions to move to the next stage of the SDLC, such as the release decision." / "Dashboards (e.g., CI/CD dashboards, task boards, and burn-down charts)"
Contested/time-bound: Uses 'test completion report' exclusively throughout; the string 'summary report' does not occur in the syllabus body at all, which is itself a finding about naming drift relative to the still-live ISTQB Glossary term.


**[48] ISO/IEC/IEEE, preview served by iTeh Standards - ISO/IEC/IEEE 29119-3:2021(E) - Software and systems engineering - Software testing - Part 3: Test documentation (free preview).** standards. **fetched-and-verified.**
`https://cdn.standards.iteh.ai/samples/79429/396e15090ac642008cc4ccbd10e89b7f/ISO-IEC-IEEE-29119-3-2021.pdf`
Supports: Read: front matter, full table of contents, Introduction and Figure 1 (document-relationship diagram), clauses 1-3 including definitions 3.1-3.26 (test completion report/test summary report synonym pair at 3.9, incident report at 3.4, test status report at 3.24). NOT read: clauses 4-8 normative prose, Annexes E-T (including the worked status-report and completion-report examples). This is the publisher's own sanctioned preview, not a pirated mirror.
Quotable: "test completion report / test summary report / report that provides a summary of the testing that was performed" / "incident report / documentation of the occurrence, nature, and status of an incident (3.3) / Note 1 to entry: Incident reports are also known as anomaly reports, bug reports, defect reports, error reports, issues, problem reports and trouble reports, amongst other terms." / "test status report / report that provides information about the status of the testing that is being performed in a specified reporting period" / "This document specifies software test documentation templates that can be used for any organization, project or testing activity. It describes the test documentation that is an output of the processes specified in ISO/IEC/IEEE 29119-2."
Contested/time-bound: Second edition, 2021-10, cancels and replaces the first edition (2013); lists 'test completion report' before 'test summary report' in its own defined-term head at 3.9.


**[49] ISO/IEC/IEEE / BSI, preview served by normsplash - BS ISO/IEC/IEEE 29119-3:2021 (free preview, Annex A information-items table and Annexes B-D).** standards. **fetched-and-verified.**
`https://www.normsplash.com/Samples/BSI/178579133/BS-ISO-IEC-IEEE-29119-3-2021-en-2.pdf`
Supports: Read: Annex A's requirement-conformance table listing every subclause of 7.3 Test status report and 7.4 Test completion report with its shall/should level, plus Annex B (overview of worked examples) and Annexes C-D (test policy / organizational test practices worked examples). This is where the clause-by-clause structural comparison of the status report vs completion report in this research comes from directly, not from a secondary enumeration.
Quotable: "7.3 Test status report ... Shall / 7.3.2 Test status ... Shall / 7.3.4 Progress against test plan ... Shall / 7.3.7 New and changed risks ... Shall / 7.3.8 Planned testing ... Shall" / "7.4 Test completion report ... Shall / 7.4.3 Deviations from planned testing ... Shall / 7.4.4 Test completion evaluation ... Shall / 7.4.7 Residual risks ... Shall / 7.4.9 Reusable test assets ... Should / 7.4.10 Lessons learned ... Shall"
Contested/time-bound: BSI edition's printed page numbers (38-48 in this preview) are offset from the ISO/IEC/IEEE edition's own numbering by several pages of national foreword; clause/annex references are used here rather than raw page numbers for that reason.


**[50] test-status-report, istqb-glossary.page (unofficial mirror of ISTQB Glossary content) - Test Status Report - ISTQB Glossary (third-party mirror).** reference. **fetched-and-verified.**
`https://istqb-glossary.page/test-status-report/`
Supports: Verbatim definition establishing test status report as a synonym of test progress report and distinct from test summary report - core evidence for the during-execution vs after-execution boundary.
Quotable: "A document summarizing testing activities and results, produced at regular intervals, to report progress of testing activities against a baseline (such as the original test plan) and to communicate risks and alternatives requiring a decision to management."


**[51] istqb-glossary.page (unofficial mirror of ISTQB Glossary content) - Test Progress Report - ISTQB Glossary (third-party mirror).** reference. **fetched-and-verified.**
`https://istqb-glossary.page/test-progress-report/`
Supports: Confirms test progress report and test status report are listed as synonyms of each other, both distinct from the completion/summary report.
Quotable: "A document summarizing testing activities and results, produced at regular intervals, to report progress of testing activities against a baseline (such as the original test plan) and to communicate risks and alternatives requiring a decision to management."


**[52] TestRail (Gurock/Idera) Support Center - Runs (Summary) report.** vendor. **fetched-and-verified.**
`https://support.testrail.com/hc/en-us/articles/9444425638292-Runs-Summary-report`
Supports: Full body read directly: establishes that TestRail's 'report,' despite the name, is entirely computed (pie charts, activity charts, forecast/estimate calculations, filtered test tables) with no narrative or evaluation field beyond the report's own Name/Description metadata.
Quotable: "The Run (Summary) report provides a high-level overview of all progress and testing activity for one or more test runs in your TestRail project." / "A pie chart showing a status-by-status breakdown of runs associated with the project." / "Forecast & Estimates give users a side-by-side hours estimate of progress, breaking down more details about completion ratios..."


**[53] Jenkins project (jenkinsci) - JUnit | Jenkins plugin.** vendor. **fetched-and-verified.**
`https://plugins.jenkins.io/junit/`
Supports: Full body read directly: establishes that the JUnit plugin's output is purely graphical/tabular visualization of XML test-result data, with no narrative-report feature in its documented configuration.
Quotable: "The JUnit plugin provides a publisher that consumes XML test reports generated during the builds and provides some graphical visualization of the historical test results... as well as a web UI for viewing test reports, tracking failures, and so on." / "When this option is configured, Jenkins can provide useful information about test results, such as trends."


**[54] Microsoft (Azure DevOps documentation) - Track test status in Azure Test Plans.** vendor. **fetched-and-verified.**
`https://learn.microsoft.com/en-us/azure/devops/test/track-test-status?view=azure-devops`
Supports: Full page read directly: establishes that Azure Test Plans' status-tracking is entirely chart/widget construction (pie, stacked bar, pivot table, stacked area) over test-point outcome data, pinnable to a dashboard - no document or narrative output.
Quotable: "Use test results charts to track how your testing is going. Choose from a fixed set of prepopulated fields related to results." / "Select the chart type, in this example, a pie chart. Based on the chart, configure the fields that you want to use to group by, or for the rows and columns." / "Pin a chart to your team's dashboard for all the team to view."


**[55] Xray (Idera/Getxray), Xray Cloud Documentation - Reporting using Gadgets.** vendor. **fetched-and-verified.**
`https://getxraydocs.atlassian.net/wiki/spaces/XRAYCLOUD/pages/44566250`
Supports: Full page read directly: catalogs all eleven Xray dashboard gadgets as computed visualizations of Jira/Xray execution data, explicitly framed as inputs to release-readiness judgment rather than the judgment itself.
Quotable: "Xray's gadgets empower users to monitor and analyze Test coverage, execution, and results directly from Jira dashboards." / "Monitor project health and readiness for release." / "Overall Test Results Gadget / Summarizes Test results (e.g., PASSED, FAILED, BLOCKED) across the project. Offers a high-level snapshot of Test outcomes, helping stakeholders evaluate project health and readiness for release."


**[56] Xray (Idera/Getxray), Xray Cloud Documentation - Document Generator.** vendor. **fetched-and-verified.**
`https://getxraydocs.atlassian.net/wiki/display/XRAYCLOUD/Document+Generator`
Supports: Full page read directly: the one tool feature among the four researched that generates a formatted document rather than a dashboard - established as template mail-merge over existing Jira field values, not synthesis or evaluation.
Quotable: "The Xray Document Generator... is a feature that allows you to create customized templates and generate documents based on your Jira data, including Xray Issues, Requirements, and Defects." / "Templates (Figure 3) are documents in DOCX (Microsoft Word) or XLSX (Microsoft Excel) formats. These templates allow you to include mappings that are dynamically replaced with data from Issue fields, custom fields, and other related information, such as comments, work logs, attachments, and more."


**[57] James Christie, Claro Testing - Do we want to be 'compliant' or valuable? (Stop 29119 tag archive).** practitioner. **fetched-and-verified.**
`https://clarotesting.wordpress.com/tag/iso29119-iso-29119-testing-software-testing-stop-29119-stop29119-testing-standards/`
Supports: Verbatim critique aimed specifically at 29119-3's test completion reports, used as the contested-claims counterweight to the 'mandatory judgment fields beat a dashboard' finding - a compliant report can still be an empty metrics dump if written carelessly.
Quotable: "The sample Test Completion Reports in the standard epitomise what is wrong. They summarise the testing process with a collection of metrics that say nothing about the quality of the product." / "It would be simple to comply with the ISO 29119 Test Completion Process, and produce a report that provided no worthwhile information at all."
Contested/time-bound: Explicitly adversarial, published 2017 at the tail of the Stop 29119 campaign; disputed by the standard's proponents (per this library's existing test-plan bundle sourcing of the same author elsewhere).


**[58] ASTQB (American Software Testing Qualifications Board, official ISTQB member board) - 5.3 Test Monitoring, Test Control and Test Completion.** standards. **fetched-and-verified.**
`https://astqb.org/5-3-test-monitoring-test-control-and-test-completion/`
Supports: Corroborates the CTFL syllabus's progress-report vs completion-report split and the exit-criteria monitoring purpose, from an independent official ISTQB member-board page.
Quotable: "Test completion reports summarize a specific test activity (e.g., test level, test cycle, iteration) and can give information for subsequent testing." / "Test progress reports support the ongoing test control and must provide enough information to make modifications to the test schedule, resources, or test plan, when such changes are needed due to deviation from the plan or changed circumstances." / "This information is used to assess test progress and to measure whether the exit criteria or the test tasks associated with the exit criteria are satisfied, such as meeting the targets for coverage of product risks, requirements, or acceptance criteria."


**[59] International Software Testing Qualifications Board - ISTQB Glossary (official site).** standards. **url-confirmed-not-read.**
`https://glossary.istqb.org/en_US/search?searchTerm=test+summary+report`
Supports: URL resolves (HTTP 200) but the site is a JavaScript single-page app; neither curl nor WebFetch could extract rendered content this pass. All ISTQB Glossary quotes in this research instead come from the istqb-glossary.page mirror, downgraded to 'reference' tier accordingly. Someone with a browser should verify against this official source before the bundle cites glossary definitions as primary.


**[60] Xray (Idera/Getxray), Xray Cloud Documentation - Document Generator Template: Test Report.** vendor. **url-confirmed-not-read.**
`https://docs.getxray.app/display/XRAYCLOUD/Document+Generator+Template:+Test+Report`
Supports: URL resolves (HTTP 200) but returned only a JavaScript-shell stub (meta tags, no rendered body) to direct fetch; would have shown the specific field list of Xray's pre-built 'test report' template, which the Document Generator claims in this research do not rest on.


**[61] CSG Government Solutions, Inc. (IV&V contractor to the State of Rhode Island) - UAT Summary Report - Phase 2 Cycle 3 and Cycle 4 (Rhode Island Unified Health Infrastructure Project).** primary. **fetched-and-verified.**
`https://transparency.ri.gov/uhip/documents/legislative-reports/status-reports/UAT%20Summary%20Report%20-%20Release%207%20Cycle3_4.pdf`
Supports: The one ACTUAL FILLED test report found: real section list (Introduction, Internet Browsers, Executive Summary, Overview, Test Case Execution Results, Defect Reporting incl. Defects by Root Cause, Issues Encountered, UAT Results Mapped to Exit Criteria, Recommendations); severity-by-root-cause defect tables; explicit 'Functionality Not Fully Tested' variance disclosure; no dedicated go/no-go section; no system build/version number anywhere.
Quotable: "This resulted in 74 defects being removed from Cycle 3, of which 63 have been resolved." / "The below functionality was either not tested or only partially tested." / "There was no formal sign off; however, verbal agreement was obtained during the UAT Exit meeting." / "It is the State's expectation to not go-live with any high or critical defects."
Contested/time-bound: Dated October 14, 2016, Version 1.0/Draft; an IV&V contractor's assessment of the State's UAT, not the testing team's own report.


**[62] Library of Congress, Office of the Chief Information Officer (OCIO) - Test Results and Analysis Report Template.** primary. **fetched-and-verified.**
`https://www.loc.gov/static/portals/about/doing-business-with-the-library/documents/Test_Results_and_Analysis_Report_Template.doc`
Supports: A real, unfilled US federal government test-report template read in full via antiword: Introduction/Purpose, Test Summary, Test Assessment, Test Results (with per-test-type subsections each carrying a 'Severity of Defect' table column), Recommendations, Appendix A References, Appendix B Key Terms.
Quotable: "Enter a comprehensive assessment of your interpretation of how adequate the test was in light of how thorough the test plan said it should be? What wasn't tested well enough?" / "Summarize the test results. Include a detailed description of any deviations from the original test plan, design, test case, or expected results." / "Describe what actions are suggested upon completion of this test. Provide any recommended improvements in the design, operation, or future testing of the business product that resulted from the testing being reported."
Contested/time-bound: Version 1.1, dated 09/2015.


**[63] Experimentus Ltd - iTM Test Completion Report (Template).** vendor. **fetched-and-verified.**
`https://www.experimentus.com/itm/04_Test_Completion_Report_Template.pdf`
Supports: A commercial UK testing-consultancy's published test completion report template. Full table of contents plus sections 1-2 read in full: Document Control, Introduction/Purpose (Management Summary: Assumptions, The Test Process, Quality and Product Risk, Recommendations), Test Summary (Schedule/Deliverables/Scope), Testing Closure Detail (Test Execution Summary, Defect Summary), Product Risks, Entry and Exit Criteria, Conclusions. Has the clearest explicit proceed/not-proceed language found in any source.
Quotable: "Based on the results of product risk mitigation activities outlined above and the final summary of KPI results, our recommendation is to <proceed/not proceed>." / "Briefly describe any KPIs not achieved and the resulting residual risks." / "Serve as the final release document, confirming the end of all test levels for the <Project name> project in scope of the test plan" / "Describe any variance from the planned scope of testing"
Contested/time-bound: iTM v6.0, dated 3 Mar 2017. Pages 6-12 of the published PDF (Test Execution Summary, Defect Summary, Product Risks, Entry/Exit Criteria, Conclusions bodies) are blank when rendered as images -- confirmed a defect in the published file, not an extraction failure -- so defect-severity and entry/exit-criteria content on this template could not be confirmed.


**[64] Hosted at ctqb.org; PDF footer text (garbled/font-subsetted) decodes under a consistent character-shift to what appears to read "Improve Quality Services BV" -- presented as an inference, not a confirmed read of the publisher's identity - Document Skeletons based on IEEE 829 Software Test Documentation.** practitioner. **fetched-and-verified.**
`https://www.ctqb.org/en/downloads/others.html?file=files/content/ctqb/downloads/others/Skeleton+test+documents+IEEE829.pdf&cid=33158`
Supports: Secondhand description of IEEE 829's 8 document types and its Test Summary Report's 8-item internal structure (Identifier, Summary, Variances, Comprehensive assessment, Summary of results, Evaluation, Summary of activities, Approvals) -- one camp in the IEEE 829 disagreement.
Quotable: "Identifier (and reference to test plan and test design)" / "Variances (against plan)" / "Report any variances of the tests executed from test plan, test designs or procedure. Specify the reason for each variance." / "Identify all resolved incidents and summarize their resolution. Identify all unresolved incidents."
Contested/time-bound: Undated training material; disagrees with professionalqa.com on both document count and TSR item count for the same claimed 1998 edition.


**[65] professionalqa.com - IEEE 829-1998.** practitioner. **fetched-and-verified.**
`https://www.professionalqa.com/ieee-standard-829-1998`
Supports: Secondhand description of IEEE 829-1998 giving only 6 document types and a 6-item Test Summary Report structure -- the rival camp to the ctqb.org/softwaretestinghelp-commenter 8-item version. Explicitly names severity as required content.
Quotable: "The documents that are covered by this standard are: Test Plan. Test Design Specification. Test Incident Report. Test Summary Report. Test Procedure/Script Specification. Test Case Specification." / "Hence, the format for test summary report defined by IEEE std 829-1998 is: Summary... Variances... Comprehensiveness Assessment..." / "Other details offered here includes: Total incidents. Resolved and unresolved defects and incidents. Defects pattern. Severity & priority of defects."
Contested/time-bound: Dated April 06, 2018; contradicts the ctqb.org camp on the same claimed edition.


**[66] softwaretestinghelp.com (Bhaskar; article author) - Test Summary Report Template (Example PDF) / How To Write An Effective Test Summary Report.** practitioner. **fetched-and-verified.**
`https://www.softwaretestinghelp.com/test-summary-report-template-download-sample/`
Supports: A practitioner-authored 12-step template (Purpose of the Document, Application Overview, Testing Scope, Metrics, Types of Testing Performed, Test Environment & Tools, Lessons Learned, Recommendations, Best Practices, Exit Criteria, Conclusion/Sign Off, Definitions/Acronyms/Abbreviations) that frames the whole document as a release gate, plus a reader comment quoting the ctqb.org-matching 8-item IEEE 829 list.
Quotable: "Software Testing is an important phase in SDLC and also it serves as the “Quality Gate” for the application to pass through and be certified as “Can Go Live” by the Testing Team." / "This is not a Test Summary Report. As per the IEEE 829 standard Test Summary Report Template is as follows: Test summary report identifier Summary Variances Comprehensive assessment Summary of results Evaluation Summary of activities Approvals"
Contested/time-bound: The article's own template and the commenter's cited IEEE-829 list are explicitly presented as different structures on the same page -- the disagreement is visible within a single source.


**[67] Apache Software Foundation / Apache CloudStack project (page credited to wiki user "Sudhap") - QA - 4.2 Test Execution Results (Apache CloudStack, Release QA).** primary. **fetched-and-verified.**
`https://cwiki.apache.org/confluence/spaces/CLOUDSTACK/pages/30756550/QA+-+4.2+Test+Execution+Results`
Supports: The one open-source example found: a live wiki dashboard, not a narrative document -- confirms open-source QA reporting uses a different genre (chart-headline index) than the government/vendor 'Test Summary Report' document.
Quotable: "Planned Vs Actual Test Execution Report:" / "Quality levels for features as well as Detailed Test plan execution:" / "Current Defect Status:" / "Weekly Defect Incoming Report:"
Contested/time-bound: Dated Sep 08, 2013; page content is essentially a set of chart captions with no narrative prose beneath them.


**[68] U.S. Food and Drug Administration, Center for Devices and Radiological Health (CDRH) - Content of Premarket Submissions for Device Software Functions - Guidance for Industry and Food and Drug Administration Staff.** primary. **fetched-and-verified.**
`https://www.fda.gov/media/153781/download`
Supports: A government regulatory body's binding-in-practice content requirements for software test reports: mandatory version-tested statement, mandatory pass/fail results, and the most rigorous residual-risk/unresolved-anomaly disclosure structure found in this research (description, discovery method/root cause, safety-impact evaluation, outcome, risk-based rationale for non-correction).
Quotable: "The summary description should include the software version tested and the overall pass/fail test results for all test protocols" / "The system level test report should demonstrate that the protocol has been acceptably executed with passing test results and any unresolved anomalies have been acceptably deferred based on a risk assessment for the candidate release version." / "Risk-based rationale for not correcting or fixing the anomaly in alignment with the sponsor's risk management plan or procedure(s)."
Contested/time-bound: Issued June 14, 2023; supersedes a 2005 guidance; 'Contains Nonbinding Recommendations' per its own header, though FDA guidance of this kind functions as de facto requirement for submissions.


**[69] John Watkins and Simon Mills; Cambridge University Press - Test Summary Report Template (Appendix J), in "Testing IT: An Off-the-Shelf Software Testing Process".** academic. **fetched-and-verified.**
`https://www.cambridge.org/core/books/testing-it/test-summary-report-template/EE7D4E42A47750DCEB17FAC30A0313AE`
Supports: Confirms an academic-press published book (not merely a blog) devotes a full appendix to a test summary report template intended for reuse; introductory framing read and verified verbatim, though the appendix's own section list is paywalled behind Cambridge Core and not visible on the abstract page.
Quotable: "The purpose of a test summary report is to summarize the result of a particular testing phase and to provide the basis for subsequent improvement of the testing process." / "As described in Chapter 4 (The Management and Planning of Testing), each testing project must generate a test summary report as one of the documents produced at the conclusion of any given testing phase."
Contested/time-bound: 2010 publication (online 2011); the template's own internal section list is not visible on this abstract/summary page -- only the book's framing text.


**[70] Dalhousie University, School / Department hosting CS3130 (course materials credited to "STL") - IEEE Standard for Software Test Documentation (ANSI/IEEE Standard 829-1983) -- course summary.** academic. **fetched-and-verified.**
`https://web.cs.dal.ca/~arc/teaching/CS3130/Templates/TestingTemplates/Test%20Plan%20Templates/IEEEStandardTestPlans.doc`
Supports: University courseware summarizing the earliest (1983) edition of IEEE 829; read in full via antiword. Covers only the Test Plan outline in detail but lists 'test summary reports' among 8 deliverable document types, agreeing with the ctqb.org camp's count under a third, earlier edition.
Quotable: "Identify the deliverable documents: test plan, test design specifications, test case specifications, test procedure specifications, test item transmittal reports, test logs, test incident reports, test summary reports" / "A document describing the scope, approach, resources, and schedule of intended testing activities."
Contested/time-bound: Course material dated 2001 (file metadata), describing the 1983 edition of the standard -- the third distinct edition referenced across sources in this research.


**[71] United States Air Force, 412th Test Wing (per search-index title only) - TEST REPORT AUTHOR'S GUIDE, 412th Test Wing, Office of the Technical Director.** primary. **not-retrieved.**
`https://apps.dtic.mil/sti/pdfs/AD1188696.pdf`
Supports: A genuine US defense test-and-evaluation body's guide to test report authorship appears to exist per DTIC's own index, but every retrieval attempt (direct curl and browser-emulated fetch) returned DTIC's own bot-blocking page ('The request is blocked'), not the document. No content from this source is used anywhere in this research.
Contested/time-bound: Blocked on every attempt this pass; content, date, and author beyond the search-index title string are unconfirmed.


**[72] UK Government (per Contracts Finder listing; publishing department not confirmed) - Test Completion Report (TCR) Template attachment, Digital Data and Technology Services procurement notice.** primary. **not-retrieved.**
`https://www.contractsfinder.service.gov.uk/Notice/Attachment/a830640d-e16c-4190-bb38-2a9f6e80a9f4`
Supports: A UK government test completion report template appears to exist per Contracts Finder's own listing, but the attachment returned HTTP 403 on fetch. No content confirmed; would have been a strong addition to the government-template category.
Contested/time-bound: Access blocked (403) this pass.
