# Research log: test-case

Built for the `test-case` bundle (qa-docs family, second member) to the methodology section 6 honest-retrieval
standard. Sources were gathered by a five-dimension research fan-out (standards and definitions, design
techniques, the acceptance-criteria boundary, debates, relationships and tooling), each doing real
WebSearch/WebFetch. Every source below is tagged with its tier and retrieval status; **only sources marked
fetched-and-verified may be quoted verbatim** in the companion, and each verbatim phrase used is listed here.

Research date: 2026-07-25. Catalog ref: 104.

---

## Honest framing (the through-line for the companion)

A test case is **the specification of one verification**: what must be true before, what you do, and what must
happen as a result. It is the smallest unit in the qa-docs family and the most argued-about artifact in
testing, because two named schools disagree about whether writing them down helps or harms.

The framing this bundle takes: **a test case is a design artifact, not a record of a run, and not a substitute
for a tester's judgment.** Both of those confusions are common and both are expensive. The first produces
templates with an "actual result" column that quietly turn a reusable specification into a one-shot form. The
second produces the deskilling that the context-driven school objects to, in Bolton's words: the test case is
not the test [32].

**The load-bearing honest-retrieval facts (do not get these wrong):**

1. **ISTQB gives "test procedure" and "test script" identical definitions**, word for word [7]. And the same
   glossary defines **"test scenario" as a synonym for test script** [39], which contradicts the near-universal
   practitioner usage in which a scenario is the high-level *what* and a case is the detailed *how*. This is a
   real, checkable trap, and the companion reports it rather than repeating the folk taxonomy.
2. **Two ISTQB definitions of "test case" are in circulation.** The older one is input-values-first [5]; the
   CTFL 4.0-aligned one adds "actions (where applicable)" and anchors the case to test conditions [6]. The
   official glossary at `glossary.istqb.org` **blocks automated retrieval and was not read**; both texts here
   come from mirrors, and the companion says so.
3. **IEEE 829 specified format without adequacy criteria.** It said what the documents should look like but
   not whether they had to be produced or what good content was [2]. Templates descended from it inherit that
   gap, which is precisely what this bundle's guidance has to fill.
4. **Myers (1979) systematized equivalence partitioning and boundary value analysis for software** [13].
   Calling him their inventor overstates it, and **this research did not establish who did originate
   equivalence classes as a concept**, so no claim is made about that. Related: BVA without prior
   partitioning is not BVA as Myers described it [13].
5. **Given/When/Then and Gherkin are different things with different dates.** JBehave started in 2003 and
   "Introducing BDD" was published in 2006 [19][21]; **"Gherkin" is a 2008 name**, coined with Cucumber [22].
   The widely repeated claim that North and Matts formalized GWT **in 2004 could not be confirmed** from any
   page read here and is **not used**.
6. **Adzic's own 2020 retrospective walks back the living-documentation promise** [24]: most teams did not put
   specifications in version control, and a third of teams using examples abandoned automation. The
   unification of specs and tests is a real proposal that largely did not happen.

**Sharpest teaching points:**
1. **A test case answers one question.** ISO/IEC/IEEE 24765 defines it as specifying "a single test" for "a
   particular software testing objective" [8]. One objective, not one assertion: a single outcome may need
   several checks to confirm.
2. **Design fields and execution fields are different.** ID, preconditions, steps, expected results and
   postconditions are the specification. Actual result, status and the run date belong to an execution record.
   Vendor templates merge them [16][8], which is why so many test cases can only be used once.
3. **Expected results are written before execution, or they are not expected results.** Filling them in
   afterwards is rationalization with extra steps [16].
4. **Preconditions are what make a case repeatable by someone other than its author** [11].
5. **Acceptance criteria do not exhaust test design.** BDD deliberately collapsed the two [19], and the
   collapse is partial: negative inputs, boundaries, regression cases from past defects, and non-functional
   checks are territory no product owner signed off on. The bundle teaches the boundary rather than picking a
   side, because both camps have working practitioners [26][27].
6. **Test-case count is a vanity metric, and both camps agree.** "We have 5,000 tests" says nothing [34], and
   count-based targets get gamed: shallow coverage outscores risky-path coverage [33].
7. **The context-driven objection is not "do not document".** It is that documenting is not testing [30], that
   testing is a performance rather than an artifact [31], and that hard-to-document work gets skipped [30].
8. **The strongest case for scripted cases is regulatory, not philosophical.** In audited contexts, linking
   every requirement to its test is not optional [35].
9. **Understandability is what practitioners rank first**, and different roles want different things from the
   same document: executors want clarity and completeness, architects want traceability and maintainability
   [12]. A template must serve both.

---

## Sources (curated, deduplicated, contiguously numbered; one source per entry)

**[1] IEEE SA - IEEE 829-2008 Standard for Software and System Test Documentation.** primary.
**fetched-and-verified.**
`https://standards.ieee.org/ieee/829/3787/`
Supports: the three editions of IEEE 829 (1983, 1998, 2008), its current status as a superseded standard, and
the named successor standards.
Quotable: "Superseded Standard"
Contested/time-bound: "Superseded" is a distinct IEEE status from "Withdrawn" or "Inactive".

**[2] Wikipedia - Software test documentation.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Software_test_documentation`
Supports: the critical limitation of IEEE 829 for a template author, and the supersession by 29119-3.
Quotable: "the standard specified the format of these documents, but did not stipulate whether they must all
be produced, nor did it include any criteria regarding adequate content"

**[3] ISO - ISO/IEC/IEEE 29119-3:2021, Test documentation.** primary. **url-confirmed-not-read (paywalled).**
`https://www.iso.org/standard/79429.html`
Supports: the existence and currency of the 2021 edition only.
Quotable: none. **The standard was not read and is not quoted anywhere in this bundle.**

**[4] Wikipedia - ISO/IEC 29119.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/ISO/IEC_29119`
Supports: the series timeline (development from 2007, first release 2013, revision 2021), the predecessor
standards it drew on (IEEE 829 among them), and the industry controversy since 2014.
Quotable: none.
Contested/time-bound: the controversy section is itself contested; used for timeline facts only.

**[5] ISTQB Glossary (mirror) - test case.** reference (mirror of a primary source).
**fetched-and-verified.**
`https://istqb-glossary.page/test-case/`
Supports: the pre-CTFL-4.0 ISTQB definition of a test case.
Quotable: "A set of input values, execution preconditions, expected results and execution postconditions,
developed for a particular objective or test condition, such as to exercise a particular program path or to
verify compliance with a specific requirement."
Contested/time-bound: **a mirror, not the official glossary**, which returned 403 and could not be read. No
version number or date is shown on the mirror page. Tiered `reference` rather than `primary` for that reason.

**[6] ISTQB Lexicon (missionwares.com) - test case.** reference (aggregator of a primary source).
**fetched-and-verified.**
`https://istqb.missionwares.com/glossary/test-case.html`
Supports: the newer CTFL 4.0-aligned definition, which differs from [5] by naming actions explicitly and
anchoring the case to test conditions.
Quotable: "A set of preconditions, inputs, actions (where applicable), expected results and postconditions,
developed based on test conditions."
Contested/time-bound: an aggregator; no glossary version number shown. Which of [5] and [6] is current could
not be settled from a readable authoritative page, and the companion presents both.

**[7] ISTQB Glossary (mirror) - test condition, test procedure, test script, test procedure specification.**
reference (mirror). **fetched-and-verified.**
`https://istqb-glossary.page/test-condition/`
Supports: the definitions of the terms most often conflated with a test case, and the fact that **test
procedure and test script carry identical definitions**.
Quotable: "An item or event of a component or system that could be verified by one or more test cases, e.g., a
function, transaction, feature, quality attribute, or structural element."; "A sequence of test cases in
execution order, and any associated actions that may be required to set up the initial preconditions and any
wrap up activities post execution."; "A document specifying a sequence of actions for the execution of a test.
Also known as test script or manual test script."
Contested/time-bound: mirror pages; the test-procedure-specification entry is attributed to an older glossary
version, so the vocabulary here has moved over time.

**[8] Wikipedia - Test case (software), carrying the ISO/IEC/IEEE 24765:2010 definition.** reference.
**fetched-and-verified.**
`https://en.wikipedia.org/wiki/Test_case_(software)`
Supports: the vocabulary-standard definition of a test case and the commonly used field set (ID, description,
steps, expected result, actual result, prerequisites, category, author, automation status, pass/fail).
Quotable: "a specification of the inputs, execution conditions, testing procedure, and expected results that
define a single test to be executed to achieve a particular software testing objective"
Contested/time-bound: the definition is quoted here from Wikipedia's citation of ISO/IEC/IEEE 24765:2010;
**the vocabulary standard itself was not read**.

**[9] microTOOL - Test Documentation with ISO/IEC/IEEE 29119-3:2021.** vendor. **fetched-and-verified.**
`https://www.microtool.de/en/document-management/test-documentation-with-iso-iec-ieee-29119-32021/`
Supports: that 29119-3 covers a large set of document types and classifies content items as mandatory,
recommended or possible, which is the shall/should/may tiering IEEE 829 lacked.
Quotable: none.
Contested/time-bound: vendor content from a company selling test documentation tooling; the author states they
read the standard, which this project could not verify.

**[10] ASTQB / ISTQB Foundation Level Syllabus 4.2 - Black-Box Test Techniques.** primary.
**fetched-and-verified.**
`https://astqb.org/4-2-black-box-test-techniques/`
Supports: the canonical enumeration and definitions of the black-box design techniques a test case is derived
from.
Quotable: "Equivalence Partitioning divides data into partitions (known as equivalence partitions) based on the
expectation that all elements of a given partition are processed the same way."; "Boundary Value Analysis is a
test technique based on exercising the boundaries of equivalence partitions."; "Decision tables are used for
testing requirements that specify how different combinations of conditions result in different outcomes."
Contested/time-bound: the current syllabus lists four techniques; earlier versions included use-case testing
as a fifth.

**[11] Lidström, Borg and colleagues - Test-case quality: understanding practitioners' perspectives.**
primary. **fetched-and-verified.**
`https://arxiv.org/html/2309.16801`
Supports: an empirical ranking of eleven test-case quality attributes, with **understandability ranked first**
and repeatability close behind; **simplicity**, meaning cases that do not bundle several verifications
together, among the attributes participants valued; and the finding that **different roles want different
things from the same document** - those executing cases prioritized understandability and completeness, while
those maintaining the suite prioritized traceability and maintainability.
Quotable: "straightforward, understandable description, clear steps, clear objective, clear precondition";
"run any time, tested repeatedly"
Contested/time-bound: six practitioners at one company. Directionally useful, **not statistically
generalizable**, and the companion says so wherever it is used.

**[12] Cem Kaner - What Is a Good Test Case?** practitioner. **url-confirmed-not-read (PDF).**
`https://www.kaner.com/pdfs/GoodTest.pdf`
Supports: the existence of Kaner's 2003 STAR East paper arguing that test-case quality is relative to the
testing objective.
Quotable: none. **The PDF was not read**; no claim rests on its internal argument beyond the framing that
"good" is context-dependent, which is independently supported by [29].

**[13] Mike Harris - A thought regarding boundary value analysis.** practitioner.
**fetched-and-verified.**
`https://testandanalysis.home.blog/2023/02/14/a-thought-regarding-boundary-value-analysis/`
Supports: the attribution of EP and BVA to Myers' *The Art of Software Testing* (1979), and the argument that
BVA without prior equivalence partitioning is not BVA as Myers described it.
Quotable: "Test cases that explore boundary conditions have a higher payoff than cases that do not"
Contested/time-bound: published 2023-02-14. The quoted line is Harris reproducing Myers; **Myers' book itself
was not read**, so it is attributed through Harris rather than directly.

**[14] Kuhn, Lei and Kacker (NIST) - Practical Combinatorial Testing: Beyond Pairwise.** primary.
**fetched-and-verified.**
`https://www.nist.gov/publications/practical-combinatorial-testing-beyond-pairwise`
Supports: pairwise and t-way combinatorial testing as the technique for multi-parameter cases, and the failure
class it targets.
Quotable: "All possible pairs of parameter values are covered by at least one test"; "elusive failures that
occur only when multiple components interact"
Contested/time-bound: published in IEEE IT Professional, 2008. Pairwise has roots in design of experiments;
the NIST authors formalized and tooled it for software rather than originating the idea.

**[15] SmartBear - Test Case Best Practices.** vendor. **fetched-and-verified.**
`https://smartbear.com/learn/test-management/test-case-best-practices/`
Supports: the mainstream vendor position on independence, repeatability and traceability, and, more usefully,
an explicit vendor warning against over-specification.
Quotable: "A test case is a set of conditions or variables under which a tester will determine whether a
system under test satisfies requirements or works correctly."
Contested/time-bound: vendor content with no named author.

**[16] Qase - How to Write Test Cases.** vendor. **fetched-and-verified.**
`https://www.qase.io/blog/how-to-write-test-cases/`
Supports: the nine-field structure vendor tooling enforces (ID, title, preconditions, steps, test data,
expected result, **actual result, status**, comments), which is the evidence for the design-versus-execution
conflation this bundle warns about.
Quotable: "Define the measurable outcome that should occur after the steps are executed"; "Specify required
system state, configurations, or dependencies before execution"
Contested/time-bound: vendor blog.

**[17] BugBug - Atomic Test Cases.** vendor. **fetched-and-verified.**
`https://bugbug.io/blog/software-testing/atomic-test-cases-the-ultimate-guide/`
Supports: the atomicity and independence principles as applied in practice.
Quotable: "Each test should be self-contained and not rely on the success or failure of other tests."
Contested/time-bound: attributes atomicity to no named practitioner. The FIRST acronym often cited alongside
it is **commonly credited to Robert C. Martin but that attribution was not verified** in this research, so it
is not used.

**[18] Dan North - Introducing BDD.** primary. **fetched-and-verified.**
`https://dannorth.net/blog/introducing-bdd/`
Supports: the original and strongest statement that acceptance criteria and behavior are the same thing, and
the Given/When/Then formulation.
Quotable: "A story's behaviour is simply its acceptance criteria: if the system fulfils all the acceptance
criteria, it's behaving correctly."; "Given some initial context (the givens), When an event occurs, Then
ensure some outcomes."
Contested/time-bound: published in Better Software in March 2006 and posted to North's site in September 2006.
The commonly cited **2004** date for the formalization of Given/When/Then **could not be verified** and is not
used.

**[19] Martin Fowler - GivenWhenThen.** practitioner. **fetched-and-verified.**
`https://martinfowler.com/bliki/GivenWhenThen.html`
Supports: the most careful available characterization of what Given/When/Then *is*, including Fowler's
explicit signal that the specification framing is an advocate's claim rather than a neutral description.
Quotable: "a style of representing tests - or as its advocates would say - specifying a system's behavior
using SpecificationByExample"
Contested/time-bound: the page carries a 2013 date which may be a last-edited rather than first-published
date.

**[20] Cucumber - History of BDD.** vendor. **fetched-and-verified.**
`https://cucumber.io/docs/bdd/history/`
Supports: the BDD timeline (JBehave from 2003, Liz Keogh writing from 2004, the article in 2006) and the claim
that Given/When/Then was designed to capture acceptance criteria in executable form.
Quotable: none.
Contested/time-bound: vendor-produced history from the company that owns Cucumber; it gives no date for the
formalization of the GWT template itself.

**[21] InfoQ - Cucumber and BDD, ten years on.** practitioner. **fetched-and-verified.**
`https://www.infoq.com/news/2018/04/cucumber-bdd-ten-years/`
Supports: that **Cucumber was released in 2008** as a rewrite of RSpec's Story Runner and that **"Gherkin" was
named at that point**, which separates the 2008 DSL from the older GWT style.
Quotable: none.
Contested/time-bound: accounts differ on incidental details of the naming story; nothing material rests on
them.

**[22] Agile Alliance - Acceptance Test Driven Development (glossary).** reference.
**fetched-and-verified.**
`https://agilealliance.org/glossary/atdd/`
Supports: ATDD's lineage and, more usefully, the canonical warning that the tooling can displace the purpose.
Quotable: "facilitating conversation between developers and product owners about product requirements"

**[23] Gojko Adzic - Specification by Example, 10 years later.** primary. **fetched-and-verified.**
`https://gojko.net/2020/03/17/sbe-10-years.html`
Supports: the author of the unification proposal reporting, ten years on, that it largely did not happen.
Quotable: "conversations are more important than capturing conversations is more important than automating
conversations"; "We believe the concept of Living Documentation is a yet unrealized key benefit for large
organizations."
Contested/time-bound: the survey percentages in the post have no described methodology and are **not used**;
only the qualitative conclusion and the quoted lines are.

**[24] Gojko Adzic - Specification by Example (book page).** primary. **book page fetched-and-verified; the
book was not read.**
`https://gojko.net/books/specification-by-example/`
Supports: the existence, date (2011) and central proposal of the book.
Quotable: none. **Only the book's page was read.**
Contested/time-bound: Adzic synthesized and popularized the term; the research did not establish that he
coined it, so the companion does not say he did.

**[25] Ovidiu Donciu, Software Testing Magazine - Comparing Test Cases and Acceptance Criteria.**
practitioner. **fetched-and-verified.**
`https://www.softwaretestingmagazine.com/knowledge/comparing-test-cases-and-acceptance-criteria/`
Supports: the clearest practitioner statement of the merge-them position.
Quotable: "Based on all the definitions above, there's not a huge difference(if any) between test cases and
acceptance criteria."; "If we already have testable ACs, why should we duplicate work in creating TCs for the
same scenarios?"
Contested/time-bound: a minority position, quoted **as** a position and not as the answer. It is also the
source the qa-docs contract points at when it requires each member to place itself against acceptance
criteria.

**[26] Andy Knight - BDD 101: Writing Good Gherkin.** practitioner. **fetched-and-verified.**
`https://automationpanda.com/2017/01/30/bdd-101-writing-good-gherkin/`
Supports: the specification-first framing of scenarios and the one-behavior rule that parallels test-case
atomicity.
Quotable: "behavior scenarios are more than tests - they also represent requirements and acceptance
criteria"; "One Scenario, One Behavior!"
Contested/time-bound: published 2017-01-30. The framing assumes scenarios are written collaboratively before
development, which is often not how teams use them.

**[27] Andy Knight - BDD 101: Manual Testing.** practitioner. **fetched-and-verified.**
`https://automationpanda.com/2017/10/08/bdd-101-manual-testing/`
Supports: the warning that mechanically converting existing manual test cases into Gherkin produces
incomprehensible scenarios plus automation code to maintain.
Quotable: "Manual testing has a place and a purpose, even in BDD"; "Automation is not a silver bullet - it
doesn't satisfy all testing needs"
Contested/time-bound: published 2017-10-08.

**[28] Aslak Hellesoy, interviewed by Semaphore - on TDD and BDD.** primary. **fetched-and-verified.**
`https://semaphore.io/blog/aslak-hellesoy-cucumber`
Supports: Cucumber's creator stating the design-first intent behind BDD.
Quotable: "BDD and TDD are not about testing existing code. They are about designing a code that hasn't yet
been written."
Contested/time-bound: no interview date confirmed on the page.

**[29] Cem Kaner, James Bach and Bret Pettichord - Context-Driven Testing: Principles.** primary.
**fetched-and-verified.**
`https://context-driven-testing.com/`
Supports: the founding principles of the school that objects to scripted test cases, including the two lines
that decide most of the argument.
Quotable: "The value of any practice depends on its context."; "There are good practices in context, but there
are no best practices."; "Metrics that are not valid are dangerous."
Contested/time-bound: no publication date on the page.

**[30] James Bach - Fighting Bad Test Documentation.** primary. **fetched-and-verified.**
`https://www.satisfice.com/blog/archives/19`
Supports: the specific and most actionable form of the context-driven objection: that hard-to-document testing
gets skipped.
Quotable: "But documenting is not testing. It is one of the chief distractions to testing."; "certain kinds of
testing isn't done at all just because it is hard to document (exploratory testing and complex scenario tests
often fall in this category)."
Contested/time-bound: published 2004-02-21.

**[31] James Bach - A Test is a Performance.** primary. **fetched-and-verified.**
`https://www.satisfice.com/blog/archives/1346`
Supports: the philosophical core of the objection, and Bach's characterization of the opposing school.
Quotable: "Testing is a performance, not an artifact."
Contested/time-bound: published 2014-01-06. Bach's description of the "Factory" school is a critique written
by an opponent, not a neutral summary, and the companion labels it as such.

**[32] Michael Bolton - The Test Case Is Not The Test.** primary. **fetched-and-verified.**
`https://developsense.com/blog/2017/02/the-test-case-is-not-the-test`
Supports: the single sharpest line available on what a test case is and is not.
Quotable: "The test case is not the test. The test is what you think and what you do."; "A recipe is not
cooking. An itinerary is not a trip. A score is not a musical performance, and a file of PowerPoint slides is
not a conference talk."; "The test case may have a role, but you, the tester, are at the centre of your
testing."
Contested/time-bound: published 2017-02-16.

**[33] Vitaly Sharovatov, Qase - Why per-tester QA KPIs backfire.** practitioner.
**fetched-and-verified.**
`https://www.qase.io/blog/why-qa-testing-kpis-backfire/`
Supports: the mechanism by which counting test cases corrupts the work, with the Goodhart framing.
Quotable: "One hundred percent coverage of shallow checks outscores eighty percent coverage of risky paths.";
"you are no longer observing your process, but rather measuring your people's creativity in defeating the
observation."
Contested/time-bound: published 2026-07-17 on a test-management vendor's blog.

**[34] Asad Abrar - Test coverage metrics that actually tell you something.** practitioner.
**fetched-and-verified.**
`https://www.drizz.dev/post/test-coverage-metrics`
Supports: test-case count named explicitly as a vanity metric, with the comparison that makes it concrete.
Quotable: "Number of test cases. 'We have 5,000 tests' tells you nothing. A team with 500 focused tests beats
5,000 trivial ones."
Contested/time-bound: published 2026-07-08.

**[35] Chris Faraglia, TestRail - Software testing in regulated industries.** vendor.
**fetched-and-verified.**
`https://www.testrail.com/blog/testing-regulated-industries/`
Supports: the strongest case for fully specified, traceable test cases, which is regulatory rather than
philosophical.
Quotable: "Full traceability via linkage of all tests to corresponding requirement artifacts"; "The bar
doesn't lower just because a machine wrote it, either. AI-generated test cases must also be version-controlled
and traceable."
Contested/time-bound: published 2026-03-03 by a test-management vendor with a commercial interest in
traceability tooling.

**[36] Agile Alliance - Exploratory Testing (glossary).** reference. **fetched-and-verified.**
`https://agilealliance.org/glossary/exploratory-testing/`
Supports: a balanced reference statement of the exploratory position that stops short of rejecting scripted
testing outright.
Quotable: "These skills will be deployed more effectively in the exploratory style on an Agile team, as this
style is more consistent with an Agile approach than the 'scripted testing' style."

**[37] ISTQB Glossary (mirror) - test scenario, test suite, test script, test run.** reference (mirror).
**fetched-and-verified.**
`https://istqb-glossary.page/test-scenario/`
Supports: the boundary terms around a test case, and **the trap**: the glossary defines "test scenario" as a
synonym for test script, not as the high-level description practitioners mean by it.
Quotable: "A set of several test cases for a component or system under test, where the post condition of one
test is often used as the precondition for the next one."; "The execution of a test suite on a specific
version of the test object."
Contested/time-bound: mirror pages. The scenario definition **directly contradicts** common practitioner
usage; that contradiction is reported, not resolved.

**[38] Microsoft - Test objects and terms overview (Azure Test Plans).** vendor (product documentation).
**fetched-and-verified.**
`https://learn.microsoft.com/en-us/azure/devops/test/test-objects-overview?view=azure-devops`
Supports: how a major tool models a test case, including the separation of the case from its executions and
the reuse mechanisms.
Quotable: "The only required field for all work item types is Title."; "Test cases by themselves aren't
executable. When you add a test case to a test suite, you generate test points."; "Test result: The recorded
outcome of a single test case execution within a test run."; "Test step: An individual action within a test
case, consisting of an Action (what the tester does) and an Expected Result (the anticipated behavior)."
Contested/time-bound: page documented as updated 2026-04-17.

**[39] Microsoft - Associate automated tests with test cases (Azure Test Plans).** vendor (product
documentation). **fetched-and-verified.**
`https://learn.microsoft.com/en-us/azure/devops/test/associate-automated-test-with-test-case?view=azure-devops`
Supports: what actually changes when a case is automated, including the trap that manual parameters do not
carry over.
Quotable: "Test case parameters are for manual test iterations only. Automated tests don't use parameters
defined on the test case work item."; "You can associate a test method with multiple test cases, but you can't
associate more than one test method with a single test case."
Contested/time-bound: page documented as updated 2026-05-08.

**[40] Tricentis - Test Case APIs (qTest documentation).** vendor (product documentation).
**fetched-and-verified.**
`https://docs.tricentis.com/qtest-saas/content/apis/apis/test_case_apis.htm`
Supports: a second independent tool's data model, and how little it requires: a name and a set of properties.
Quotable: none.

**[41] Shreya Bose, TestRail - Requirements Traceability Matrix: a how-to guide.** practitioner.
**fetched-and-verified.**
`https://www.testrail.com/blog/requirements-traceability-matrix/`
Supports: what traceability means operationally and the standard column set of a traceability matrix.
Quotable: "a tool or document commonly used to ensure that all the requirements established for a testing
project are mapped to corresponding tests."

**[42] TestBuggy - Test cases versus bug reports.** practitioner. **fetched-and-verified.**
`https://testbuggy.com/blog/test-cases-vs-bug-reports`
Supports: the boundary to the third qa-docs member, stated in terms of direction and timing.
Quotable: "Bug reports are reactive, created after discovering a problem in existing software. Test cases are
proactive, written 'before or during development' to define correct behavior."
Contested/time-bound: no named author or date on the page.

---

## Claims flagged contested or time-bound

1. **Which ISTQB definition of "test case" is current.** [5] and [6] differ; the official glossary blocks
   retrieval. Both are presented; neither is called authoritative.
2. **"Test scenario".** The ISTQB glossary makes it a synonym for test script [37]; practitioners overwhelmingly
   use it to mean a high-level description that a case implements. Reported as a live vocabulary conflict.
3. **Test procedure versus test script.** Identical definitions in the current glossary [7], despite training
   material that distinguishes them.
4. **Who originated equivalence partitioning and boundary value analysis.** Myers (1979) systematized them for
   software [13]. "Inventor" is not claimed, and **this research did not establish the origin of equivalence
   classes as a concept**, so the bundle asserts nothing about it.
5. **Whether BVA requires EP first.** Harris argues yes on a strict reading of Myers [13]; standard teaching
   presents them as separately applicable [10].
6. **The origin date of Given/When/Then.** The 2004 date circulates widely and **was not verified**. What is
   verified: JBehave from 2003, the article in 2006 [18][20], Gherkin named with Cucumber in 2008 [21].
7. **Whether acceptance criteria and test cases are one artifact or two.** The unification camp [18][24][26]
   against the coverage camp; Adzic's own retrospective [23] reports the unification largely did not happen.
   Genuinely unresolved and presented as such.
8. **Whether scripted cases help or harm in non-regulated contexts.** Context-driven [29][30][31][32] against
   the standards tradition [10][35]. No controlled study settles it; the regulatory case [35] is the strongest
   ground for the pro-scripting side and is not disputed by the other camp.
9. **The FIRST principles' authorship** is commonly given as Robert C. Martin; **not verified**, so not used.
10. **The "70 percent of QA effort goes to test maintenance" figure** surfaced in vendor content with no
    identified source; **not used**.
11. **Empirical weight of [11]** is six practitioners at one company. Used for direction, never as a general
    finding.

---

## Notes for the companion

**Honest framing.** A test case specifies one verification, and it is a design artifact rather than a record.
The bundle teaches the case that stays reusable: one objective, preconditions that make it repeatable by a
stranger, expected results written before execution, and execution state kept somewhere else.

**Load-bearing sections.** Identification and Traceability (what it verifies and what it traces to);
Preconditions and Test Data (the repeatability lever); Steps and Expected Results (the case itself).

**The boundary that defines the family.** Acceptance criteria versus test cases must be argued, not asserted:
give the unification camp its strongest form (North, Adzic) and then name the territory it does not cover
(negative, boundary, regression, non-functional). The worked example should *be* an instance of that
territory, so the argument is demonstrated rather than claimed.

**What the full variant adds and why.** Design rationale (which technique produced the case and why these
values), environment and configuration, automation status, and version and approval. These are what audited
and multi-team contexts need [35] and what a two-week feature does not.

**Tone.** Do not present scripted cases as universally correct, and do not present the context-driven critique
as permission to write nothing. Both camps have working practitioners, and the deciding variable is context,
which is itself the first context-driven principle [29].
