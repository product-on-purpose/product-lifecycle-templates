# Research log: bug-report

Built for the `bug-report` bundle (qa-docs family, third member) to the methodology section 6
honest-retrieval standard. Sources were gathered by a five-dimension research fan-out (standards and
definitions, report quality, severity and priority, debates, relationships and tooling), each doing real
WebSearch/WebFetch. Every source below is tagged with its tier and retrieval status; **only sources marked
fetched-and-verified may be quoted verbatim** in the companion, and each verbatim phrase used is listed here.

Research date: 2026-07-25. Catalog ref: 107.

---

## Honest framing (the through-line for the companion)

A bug report is **the document that gets one defect fixed**, and it is the only artifact in this family
written by people who are not testers: support agents, salespeople, users, whoever hit the thing. That is why
its central problem is not structure but **the gap between what a reader needs and what a reporter finds easy
to supply**, which is exactly what the landmark study measured [11][12].

**The deepest fact about this document type, and the one that shapes the whole template:** the standards
deliberately do **not** call it a bug report. IEEE 829-2008 named it an **anomaly report**, on the explicit
reasoning that *"a discrepancy between expected and actual results can occur for a number of reasons other
than a fault in the system"* [2], and its successor calls it an **incident report** [3][4]. ISTQB defines an
incident as any event requiring investigation [5]. At the moment you write this document, **you do not yet
know whether there is a defect**, and a report written as though you do is what produces the "works for me"
reply. The template therefore asks for what was observed and what was expected, and keeps the diagnosis
separate from the observation.

**The load-bearing honest-retrieval facts (do not get these wrong):**

1. **Expected behavior is the most-omitted element in real reports.** Across roughly 3,000 reports, observed
   behavior appeared in 93.5 percent, steps to reproduce in 51.4 percent, and **expected behavior in only
   35.2 percent** [13]. This is the single most useful number in the whole bundle.
2. **What developers most want is what reporters find hardest.** The 2008 study of 466 respondents across
   Apache, Eclipse and Mozilla found the same items at the top of both lists [11][12]. The template's job is
   to reduce that friction, not to scold.
3. **ISTQB defines severity and priority but assigns ownership to neither** [20][21]. The familiar rule that
   QA sets severity and the product manager sets priority is a widely followed **convention**, visible across
   practitioner and vendor sources [22][23][27][28], not a standards requirement. The companion says so.
4. **There is no standard severity scale.** Four-level, five-level and six-level named scales are all in use
   [23][26][27], and S1-S4 numbering is tooling convention that different sources map to different labels
   [22]. Pick one and define it.
5. **IEEE 1044-2009, the classification standard everyone cites for defect taxonomy, was inactivated on
   2020-03-05 and has no replacement** [38]. Every defect-lifecycle state list in circulation is therefore
   convention, not standard.
6. **Jira deliberately removed its Severity field** because *"it was confusing to business users"* [40], so it
   cannot express the distinction the discipline teaches without a custom field. That is a fact about the
   world a template must account for rather than ignore. (**No source here establishes Jira's market
   position**, so the bundle does not call it the most-used tracker.)
7. **The "30 percent of reports are duplicates" figure is not a finding.** Measured rates across 150,000-plus
   reports run from 2.0 percent to 28.2 percent, tracking how consumer-facing a project is [19]. The high end
   is quoted as if it were universal.
8. **Zero defects has two unrelated ancestries** and they are routinely conflated. The software practice is
   documented from a 1989 Microsoft memo [29]; Crosby's 1964 manufacturing programme is a different thing.
   This bundle does not attribute one to the other.

**Sharpest teaching points:**
1. **Report the observation, not the conclusion.** You are reporting an anomaly; whether it is a defect is
   determined afterwards [2][5].
2. **Steps to reproduce are the deliverable.** Tatham's formulation is the best one-liner available: the aim
   is *"to enable the programmer to see the program failing in front of them"* [18].
3. **Write the expected result even when it feels obvious.** It is the most-skipped field [13], and the reader
   often does not know the intended behavior [9].
4. **Severity and priority are independent axes**, which is why both crossing cases exist: a crash in a rarely
   used path is high severity and low priority; a cosmetic error on a launch homepage is low severity and high
   priority [23].
5. **Reproducibility and frequency are fields, not adjectives.** Intermittent bugs are a studied category, and
   non-reproducibility is a large real problem rather than an edge case [15][16].
6. **Tone changes outcomes.** Blaming language produces defensiveness and worse fixes; describe the system's
   behavior, not the developer's [36].
7. **Defect counts get gamed the moment they become targets**, in specific documented ways: splitting one bug
   into several tickets, filing trivial bugs to hit quotas, relabeling to stay under severity caps [35].
8. **Whether to log at all is a real question.** The break point is whether the fix will outlive the
   developer's working memory [30][31][32][33].

---

## Sources (curated, deduplicated, contiguously numbered; one source per entry)

**[1] IEEE SA - IEEE 829-2008 Standard for Software and System Test Documentation.** primary.
**fetched-and-verified (status page only).**
`https://standards.ieee.org/ieee/829/3787/`
Supports: that IEEE 829-2008 is superseded and by what.
Quotable: "IEEE 829-2008 is superseded by ISO/IEC/IEEE 29119-1-2013, ISO/IEC/IEEE 29119-2-2013, ISO/IEC/IEEE
29119-3-2013 and ISO/IEC/IEEE 29119-4-2015."
Contested/time-bound: the standard text itself is paywalled and was not read.

**[2] Wikipedia - Software test documentation.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Software_test_documentation`
Supports: **the most important fact in this bundle** - that IEEE 829-2008 renamed the test incident report to
an *anomaly report*, and the stated reason.
Quotable: "a discrepancy between expected and actual results can occur for a number of reasons other than a
fault in the system."; "all details of the incident such as actual and expected results, when it failed, and
any supporting evidence that will help in its resolution"
Contested/time-bound: a summary of a paywalled standard; the standard text was not independently read.

**[3] Wikipedia - ISO/IEC 29119.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/ISO/IEC_29119`
Supports: that Part 3's document set includes a *Test Incident Report*, and the series' part versions.
Quotable: "Test Incident Report"
Contested/time-bound: a synthesis of a paywalled standard. Part version dates are not relied on here beyond
what [1] independently confirms.

**[4] microTOOL - Test Documentation with ISO/IEC/IEEE 29119-3:2021.** vendor.
**fetched-and-verified.**
`https://www.microtool.de/en/document-management/test-documentation-with-iso-iec-ieee-29119-32021/`
Supports: that the successor standard's naming obscures the everyday term, and that IEEE 829 was replaced in
2013.
Quotable: "Since 2013, IEEE 829 has been replaced by ISO/IEC/IEEE 29119-3."; "the term 'incident report' hides
the commonly known 'bug report' is introduced late in the descriptive chapters."
Contested/time-bound: vendor content; the author states they read the paywalled standard, which this project
could not verify.

**[5] ISTQB Glossary (community mirror) - defect, bug, error, failure, incident, defect report.** reference
(mirror of a primary source). **fetched-and-verified.**
`https://istqb-glossary.page/`
Supports: the canonical vocabulary, including that **bug and defect share a definition** while **error does
not**, and that **incident is much broader than defect**.
Quotable: "A flaw in a component or system that can cause the component or system to fail to perform its
required function, e.g., an incorrect statement or data definition."; "A human action that produces an
incorrect result."; "Deviation of the component or system from its expected delivery, service or result.";
"Any event occurring that requires investigation."; "A document reporting on any flaw in a component or system
that can cause the component or system to fail to perform its required function."
Contested/time-bound: the page carries a "no affiliation" disclaimer and shows **no glossary version number**.
Tiered `reference` rather than `primary` for that reason.

**[6] istqb.guru - Defect vs Failure vs Error vs Mistake.** practitioner. **fetched-and-verified.**
`https://www.istqb.guru/defect-vs-failure-vs-error-vs-mistake-istqb/`
Supports: the causal chain in its teaching form, and that **root cause is a distinct fourth concept** rather
than a synonym for error.
Quotable: "A person makes a mistake (error). This produces a defect (fault) in the work product. Executing the
work product produces a failure."; "defects can exist without producing failures, which is why exhaustive
testing is impossible"
Contested/time-bound: no byline; page states a 2026 update. A practitioner summary of a syllabus whose PDF
returned 403 and **was not read**.

**[7] ToolsQA - Error, Defect and Failure.** practitioner. **fetched-and-verified.**
`https://www.toolsqa.com/software-testing/istqb/error-defect-failure/`
Supports: the two legitimate breaks in the chain: dormant defects that never produce a failure, and failures
with non-code causes.
Quotable: "Not all Defects result in Failures; some remain inactive in the code, and we may never notice them."
Contested/time-bound: no date visible. The page attributes a quotation to a named individual that **could not
be verified**, so that attribution is not used.

**[8] ProfessionalQA - IEEE 829-1998 overview.** practitioner. **fetched-and-verified.**
`https://www.professionalqa.com/ieee-standard-829-1998`
Supports: the section list attributed to the 1998 edition's test incident report (identifier, summary,
description, impact).
Quotable: none used.
Contested/time-bound: a secondary summary of a paywalled edition; the four-section list is sparse relative to
practitioner templates and **may understate the standard**. Not relied on for any field-level claim.

**[9] TechTarget - What details to include on a software defect report.** practitioner.
**fetched-and-verified.**
`https://www.techtarget.com/searchsoftwarequality/tip/What-details-to-include-on-a-software-defect-report`
Supports: the practitioner field list, and specifically the argument for stating the expected result and for
recording reproduction frequency.
Quotable: "Developers might not know how the application works from end to end...Including the expected
outcome -- in addition to the actual outcome -- provides crucial information."; "Knowing how frequently a bug
reproduces is important. Many bugs are random."
Contested/time-bound: no publication date visible.

**[10] BrowserStack - How to write a good defect report.** vendor. **fetched-and-verified.**
`https://www.browserstack.com/guide/how-to-write-a-good-defect-report`
Supports: a representative vendor field list and the severity-versus-priority framing as tools present it.
Quotable: "Unique identifier for tracking (e.g., DEF-0012)"
Contested/time-bound: vendor content, no named author, no date, and no citation for its severity/priority
framing.

**[11] Bettenburg, Just, Schroeter, Weiss, Premraj and Zimmermann - What makes a good bug report?**
primary. **fetched-and-verified (publication record; the paper body was not read).**
`https://research.vu.nl/en/publications/what-makes-a-good-bug-report/`
Supports: the existence, authorship, venue (ACM SIGSOFT FSE 2008) and scope of the landmark study: 466
respondents across Apache, Eclipse and Mozilla.
Quotable: none from this page.
Contested/time-bound: the study covers open-source projects on Bugzilla-style trackers and may not generalize
to proprietary or mobile contexts. The 466 figure covers developers **and** users.

**[12] Jorge Aranda, It Will Never Work in Theory - summary of Bettenburg et al.** practitioner.
**fetched-and-verified.**
`https://neverworkintheory.org/2011/08/30/what-makes-a-good-bug-report.html`
Supports: the study's central mismatch finding, in a directly quotable form, and the CUEZILLA accuracy figure.
Quotable: "Most developers consider steps to reproduce, stack traces, and test cases as helpful, which are at
the same time most difficult to provide for users."
Contested/time-bound: a secondary summary. It is cited **for the summary**, with [11] carrying the study's
bibliographic weight.

**[13] Chaparro, Lu, Zampetti, Moreno, Di Penta, Marcus, Bavota and Ng - Detecting Missing Information in
Bug Descriptions.** primary. **fetched-and-verified.**
`https://ojcchar.github.io/publications/8-fse17`
Supports: **the key measurement**: across approximately 3,000 reports, observed behavior appears in 93.5
percent, expected behavior in 35.2 percent, and steps to reproduce in 51.4 percent.
Quotable: none needed; the figures are the finding.
Contested/time-bound: ESEC/FSE 2017. The corpus is open-source bug trackers.

**[14] Chaparro, Bernal-Cardenas, Lu, Moran, Marcus, Di Penta, Poshyvanyk and Ng - Assessing the Quality of
the Steps to Reproduce in Bug Reports.** primary. **fetched-and-verified.**
`https://arxiv.org/abs/1906.07107`
Supports: that steps to reproduce are treated by the research community as the primary quality lever, and that
automated assessment of them is now partly tractable.
Quotable: "identify and assess the quality of the steps to reproduce in a bug report, providing feedback to
the reporters"
Contested/time-bound: ESEC/FSE 2019.

**[15] Joorabchi, Mirzaaghaei and Mesbah - Works For Me! Characterizing Non-reproducible Bug Reports.**
primary. **url-confirmed-not-read.**
`https://dl.acm.org/doi/10.1145/2597073.2597098`
Supports: the existence and scale of the non-reproducibility problem (MSR 2014; 32,000 non-reproducible
reports across six repositories).
Quotable: none. **The ACM page returned 403 and the paper was not read**; the scale figure comes from the
authors' own publication listing and from [16], not from the paper body.

**[16] Rahman, Castelluccio and Khomh - Works for Me! Cannot Reproduce.** primary.
**fetched-and-verified.**
`https://www.mozillafoundation.org/en/research/library/works-for-me-cannot-reproducea-large-scale-empirical-study-of-non-reproducible-bugs/`
Supports: a large-scale study of non-reproducible reports (576 from Firefox and Eclipse), the finding that
many distinct factors drive non-reproducibility, and that links to related reports help.
Quotable: "11 key factors that might lead a reported bug to non-reproducibility"; "links to existing bug
reports might help improve the reproducibility of a reported bug"
Contested/time-bound: Empirical Software Engineering, 2022.

**[17] Soltani, Hermans and Back - The significance of bug report elements.** primary. **not retrieved.**
`https://link.springer.com/article/10.1007/s10664-020-09882-z`
Supports: nothing on its own. Listed because it is the modern replication of [11] and a reader may expect it.
Quotable: none. **The page was not retrieved (paywalled), and the author list could not be confirmed from a
read page**; an AI-generated search summary gave a different and apparently incorrect set of authors. **No
claim in this bundle rests on this entry**, and the companion does not cite it as evidence for any finding.

**[18] Simon Tatham - How to Report Bugs Effectively.** practitioner. **fetched-and-verified.**
`https://www.chiark.greenend.org.uk/~sgtatham/bugs.html`
Supports: the canonical practitioner statement of what a bug report is *for*, and the observed-versus-expected
instruction, both of which predate the empirical work by roughly fifteen years.
Quotable: "the aim of a bug report is to enable the programmer to see the program failing in front of them.";
"Tell them exactly what you saw. Tell them why you think what you saw is wrong; better still, tell them
exactly what you expected to see."
Contested/time-bound: no publication date visible on the page. An argumentative essay, not research; its
authority is that it is right and famous, not that it is measured.

**[19] Patil, Tao and Jadon - GitBugs.** reference. **fetched-and-verified.**
`https://arxiv.org/html/2504.09651`
Supports: **measured duplicate rates**, which vary enormously by project: roughly 28 percent for VS Code and
22 percent for Firefox down to about 2 percent for Spark and HBase, across more than 150,000 reports.
Quotable: "over 150,000 bug reports"
Contested/time-bound: an arXiv preprint, not confirmed peer-reviewed. Rates reflect one dataset window. The
point taken from it is the **spread**, not any single figure.

**[20] ISTQB Glossary (community mirror) - severity.** reference (mirror). **fetched-and-verified.**
`https://istqb-glossary.page/severity/`
Supports: the canonical definition of severity.
Quotable: "The degree of impact that a defect has on the development or operation of a component or system."
Contested/time-bound: no version number on the page, and **the entry specifies no owner and no scale**.

**[21] ISTQB Glossary (community mirror) - priority.** reference (mirror). **fetched-and-verified.**
`https://istqb-glossary.page/priority/`
Supports: the canonical definition of priority, and its business framing.
Quotable: "The level of (business) importance assigned to an item, e.g., defect."
Contested/time-bound: as above. **Neither glossary entry says who assigns either value.**

**[22] Software Testing Help - Defect severity and priority, with the triage process.** practitioner.
**fetched-and-verified.**
`https://www.softwaretestinghelp.com/how-to-set-defect-priority-and-severity-with-defect-triage-process/`
Supports: the S1-S4 and P1-P4 convention and the ownership convention.
Quotable: "the Product Manager or the triage team mainly assesses the priority parameter."
Contested/time-bound: no date visible. Its claim that the lowest priority level "doesn't have to be fixed to
match exit criteria" is that source's convention, not a standard.

**[23] BrowserStack - Bug severity versus priority.** vendor. **fetched-and-verified.**
`https://www.browserstack.com/guide/bug-severity-vs-priority`
Supports: the ownership convention and, most usefully, **both crossing examples** in worked form.
Quotable: "Bug Severity is primarily determined by the development or testing team."; "Bug Priority, on the
other hand, is usually decided by product managers, stakeholders, or the business team."
Contested/time-bound: vendor content, no date. Its attribution of severity to "the development or testing
team" is broader than other sources' "QA".

**[24] Software Testing Help - Defect triage process and meeting.** practitioner.
**fetched-and-verified.**
`https://www.softwaretestinghelp.com/defect-triage-process-meeting/`
Supports: what a triage meeting does: review new defects, correct severity and priority, assign to a release.
Quotable: "sets the priority based on all the inputs and assigns the defect to the correct release."
Contested/time-bound: no date. Its attendee list is longer than many organizations use and is presented as
typical rather than required.

**[25] TestRail - Exit criteria: advanced strategies for agile QA teams.** vendor.
**fetched-and-verified.**
`https://www.testrail.com/blog/exit-criteria-strategies/`
Supports: how severity connects to a release gate, which is where the test plan and this bundle meet.
Quotable: "No open critical bugs: All critical bugs that impact core functionality must be resolved to meet
exit criteria."; "No blocking bugs: Any bugs that prevent further testing or development (blockers) must be
resolved to allow the project to proceed."
Contested/time-bound: vendor content describing convention, not a standard; thresholds vary.

**[26] QATestLab - Bug severity levels explained.** practitioner. **fetched-and-verified.**
`https://blog.qatestlab.com/2015/03/10/software-bugs-severity-levels/`
Supports: a five-level named scale (Blocker, Critical, Major, Minor, Trivial) with definitions, and that such
scales are convention with no formal standard behind them.
Quotable: "Completely prevents the use or testing of the system"
Contested/time-bound: published 2015-03-10. No standard is cited for the scale, which is the point.

**[27] Plane - Bug severity versus priority in testing.** vendor. **fetched-and-verified.**
`https://plane.so/blog/bug-severity-vs-priority-in-testing-key-differences`
Supports: a current cross-functional statement of the ownership convention, which adds engineering leads
alongside product managers.
Quotable: "Typically assigned by QA engineers or testing teams"; "Typically aligned by product managers,
engineering leads, and delivery stakeholders"
Contested/time-bound: vendor blog, no date. Its broader ownership model is evidence that the convention itself
varies.

**[28] Joel Spolsky - The Joel Test.** primary. **fetched-and-verified.**
`https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/`
Supports: the canonical argument for tracking defects at all, and the original software framing of fixing
before building.
Quotable: "If you are developing code, even on a team of one, without an organized database listing all known
bugs in the code, you are going to ship low quality code."; "if you have a schedule with a lot of bugs
remaining to be fixed, the schedule is unreliable."
Contested/time-bound: published 2000-08-09; the mandatory-database advice is contested by short-cycle teams
(see [31][33]).

**[29] Steven Sinofsky - Hardcore Software: Zero Defects.** practitioner. **fetched-and-verified.**
`https://hardcoresoftware.learningbyshipping.com/p/006-zero-defects`
Supports: the documented origin of the software zero-defects practice at Microsoft in 1989, and the incentive
failure it was created to break.
Quotable: "The cycle of trying to complete a feature by finding bugs could never really end - this was called
infinite bugs."; "Your goal should be to have a working, nearly-shippable product every day."
Contested/time-bound: a participant's memoir, credible as an insider account rather than independent research.
**Note:** Crosby's 1964 manufacturing Zero Defects programme is a different thing; this bundle does not
attribute one to the other.

**[30] Martin Fowler - VeryLowDefectProject.** primary. **fetched-and-verified.**
`https://www.martinfowler.com/bliki/VeryLowDefectProject.html`
Supports: that very low defect rates are achievable, and the crucial qualifier that they do not follow
automatically from adopting practices.
Quotable: "you should not assume you are going to get super-low bug rates by just adopting XP"
Contested/time-bound: Fowler is describing observed outcomes among experienced teams, not a controlled study.

**[31] Mitch Lacey - Managing bugs in Scrum and agile projects.** practitioner.
**fetched-and-verified.**
`https://www.mitchlacey.com/blog/managing-bugs-in-scrum-and-agile-projects/`
Supports: the strongest case against logging bugs onto a backlog at all, and the reason: a backlog is a
mechanism for deprioritizing quality.
Quotable: "Don't put bugs on the product backlog. Just fix them or mark them as won't fix."; "Having the
ability to file a bug and have it on the product backlog means there is a way to deprioritize quality by
moving bugs farther down the product backlog."
Contested/time-bound: a practitioner position, not a study. It is harder to operationalize across teams or
with externally reported defects.

**[32] Peter Hilton - Implement a zero-bug policy.** practitioner. **fetched-and-verified.**
`https://hilton.org.uk/blog/zero-bug-policy`
Supports: the observation that the bug-versus-feature classification dispute is itself the signal.
Quotable: "if product managers and developers don't agree on what to call a bug, you probably need to address
other problems"
Contested/time-bound: no readable publication date. A practitioner observation.

**[33] InfoQ, reporting Simone Colosimo (Dashlane) - Zero bug policy.** practitioner.
**fetched-and-verified.**
`https://www.infoq.com/news/2021/11/zero-bug-policy`
Supports: the operational classification rule that makes a zero-bug policy decidable at intake.
Quotable: "If you can live with it, it's not a bug, it's an improvement."
Contested/time-bound: a single-organization case reported by an internal advocate. Its outcome figures are
self-reported with no independent verification and are **not used**.

**[34] Adrian Bryant, ProductPlan - Backlog bankruptcy.** vendor. **fetched-and-verified.**
`https://www.productplan.com/backlog-bankruptcy/`
Supports: the case for mass-closing an aged defect backlog, and the assumption it rests on.
Quotable: "If an idea has high enough value for customers, it will come back. It will bubble up to the top."
Contested/time-bound: vendor content by an advocate. The argument holds **only if intake still works**, which
the source does not stress and the companion does.

**[35] Qase - Why per-tester QA KPIs backfire.** vendor. **fetched-and-verified.**
`https://www.qase.io/blog/why-qa-testing-kpis-backfire/`
Supports: the specific documented forms defect-count gaming takes.
Quotable: "When a measure becomes a target, it ceases to be a good measure"
Contested/time-bound: vendor content; the gaming examples are illustrative rather than measured.

**[36] Software Testing Help - How to write a good bug report.** reference.
**fetched-and-verified.**
`https://www.softwaretestinghelp.com/how-to-write-good-bug-report/`
Supports: the tone guidance, which is rarely stated explicitly anywhere else.
Quotable: "The most important point that a tester should keep in mind is not to use an authoritative tone in
the report. This breaks morale and creates an unhealthy work relationship. Use a suggestive tone."
Contested/time-bound: no named author. Presented as craft wisdom; **no study is cited** linking tone to fix
rates, and the companion does not claim one.

**[37] Iris Classon (host) and community respondents - Bug, issue or defect?** practitioner.
**fetched-and-verified.**
`https://www.irisclasson.com/2013/02/19/stupid-question-154-bug-issue-or-defect-what-is-the-correct-term/`
Supports: documented evidence that practitioners draw these lines in **incompatible** places, which is why a
template must declare its own working term.
Quotable: "A bug is a defect of undetermined cause"; "An issue is a very broad term that encompasses bugs and
defects, but also things such as new feature requests"
Contested/time-bound: 2013, community Q&A. The absence of consensus is itself the durable finding.

**[38] IEEE SA - IEEE 1044-2009, Standard Classification for Software Anomalies.** primary.
**fetched-and-verified (status page).**
`https://standards.ieee.org/ieee/1044/4607/`
Supports: **that the most-cited defect classification standard was inactivated on 2020-03-05** after ten years
without revision, with no replacement published.
Quotable: none used.
Contested/time-bound: this is why every defect lifecycle state list in circulation is convention. Citing 1044
as current is incorrect.

**[39] Microsoft - Define, capture, triage and manage bugs in Azure Boards.** vendor.
**fetched-and-verified.**
`https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/manage-bugs?view=azure-devops`
Supports: what a major tracker requires and what it advises about regressions.
Quotable: "By default, only the Title field is required."; "Don't reopen closed bugs for regressions. Instead,
open a new bug and link it to the original with a Related link."

**[40] Atlassian - Why doesn't Jira have a Severity field like Bugzilla?** vendor.
**fetched-and-verified.**
`https://confluence.atlassian.com/jira061/jira-administrators-faq/usage-faq/why-doesn-t-jira-have-a-severity-field-like-bugzilla`
Supports: **the single most consequential tooling fact in this bundle**: Jira had a Severity field and removed
it deliberately, on the reasoning that it confused business users, leaving Priority to carry both meanings.
Quotable: "JIRA succeeds so well because business users can actually use it."
Contested/time-bound: vendor documentation on an older Jira version's FAQ; the architectural consequence
(severity as a custom field) persists.

**[41] incident.io - Incident versus bug.** vendor. **fetched-and-verified.**
`https://incident.io/blog/incident-vs-bug`
Supports: the boundary between a defect report and incident management, in terms of what each optimizes for.
Quotable: "incident management focuses on restoring service as quickly as possible after an incident occurs,
while bug management focuses on identifying and fixing the root cause"
Contested/time-bound: vendor content from an incident-management company.

**[42] Rod Hilton - Enhancement versus defect.** practitioner. **fetched-and-verified.**
`https://www.rodhilton.com/2012/03/29/enhancement-vs-defect-more-than-pedantry/`
Supports: the sharpest available test for the defect-versus-change-request boundary: a defect means the
software does not work the way it says it will; an enhancement means it does not work the way someone wants.
Quotable: none used verbatim.
Contested/time-bound: a practitioner argument. The boundary remains genuinely contested in gray areas such as
an undocumented performance regression.

---

## Claims flagged contested or time-bound

1. **What the document is called.** Standards say anomaly report [2] or incident report [3][4]; ISTQB says
   defect report [5]; practitioners say bug report; tools say issue, work item or bug [39][40]. Nothing
   resolves this, and the bundle declares its own usage rather than pretending otherwise [37].
2. **Who assigns severity and priority.** Convention, consistently reported [22][23][27] but **absent from the
   standard definitions** [20][21].
3. **Severity scales.** Four, five and six-level scales are all in use [23][26][27]; S1-S4 numbering is a
   tooling convention whose labels differ between sources [22].
4. **Defect lifecycle states.** No current standard: IEEE 1044-2009 was inactivated in 2020 with no
   replacement [38].
5. **Duplicate rates.** Measured spread is roughly 2 percent to 28 percent [19]; the widely quoted "30
   percent" is not a general finding.
6. **Whether to log bugs at all.** Spolsky's mandatory-database position [28] against Lacey's do-not-backlog
   position [31], with Fowler's data showing low defect rates are real but not transferable by imitation
   [30].
7. **Whether zero-bug policies deliver their claimed gains.** The available case is single-organization and
   self-reported [33]; its outcome figures are not used here.
8. **Zero defects' ancestry.** The software practice is documented from 1989 [29]; Crosby's 1964 manufacturing
   programme is separate, and conflating them is a common error this bundle avoids.
9. **Whether the bug/defect/issue distinction matters in practice.** Formally argued yes; practitioners
   demonstrably disagree [37].
10. **Tone and fix outcomes.** The guidance is craft wisdom [36]; **no study is cited** connecting tone to
    resolution speed, and the companion does not imply one.
11. **[17] was not retrieved at all** and supports nothing.
12. **The error-defect-failure chain's attribution to a named individual** appeared in one source [7] and
    **could not be verified**; it is not used.

---

## Notes for the companion

**Honest framing.** A bug report exists to get one defect fixed by someone who was not there. Its central
difficulty is measured, not theoretical: the elements the reader most needs are the ones the writer finds
hardest to produce [11][12], and the single most-omitted element is the one that says what should have
happened [13].

**Load-bearing sections.** Summary (one line that survives a triage queue); Steps to Reproduce; Expected
versus Actual; Environment and Reproducibility; Severity and Priority as **separate** fields.

**The framing move that distinguishes this bundle.** Teach the report as an **anomaly** report: you observed
something, you expected something else, and whether that difference is a defect is determined afterwards
[2][5]. This dissolves several arguments at once, including the terminology dispute [37] and the awkwardness
of reporting something you cannot fully explain.

**What the full variant adds and why.** Triage and classification (the severity/priority pair with owners
named), root cause and fix reference, and the regression-guard link back to a test case. These serve triage
and audit, not the person hitting the bug at 5pm.

**Tone.** Say plainly that blaming language costs you fixes [36], and say equally plainly that no study is
being cited for it.
