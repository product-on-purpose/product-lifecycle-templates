# Research log: test-plan

Built for the `test-plan` bundle (qa-docs family, the first member) to the methodology section 6
honest-retrieval standard. Sources were gathered by a five-dimension research fan-out (standards lineage,
structure and criteria, agile and methodology lineage, debates and criticism, relationships and tooling),
each doing real WebSearch/WebFetch. Every source below is tagged with its tier and retrieval status; **only
sources marked fetched-and-verified may be quoted verbatim** in the companion, and each verbatim phrase used
is listed here.

Research date: 2026-07-25. Catalog ref: 102.

---

## Honest framing (the through-line for the companion)

The test plan is the document type where **the artifact and the activity have come apart**, and a bundle that
does not say so will teach the wrong thing. Almost everyone who says "IEEE 829" is naming a **superseded**
standard [1][2]; its replacement, ISO/IEC/IEEE 29119-3:2021, is **paywalled** [3], so the structure most
teams follow is absorbed second-hand from vendor templates rather than read. Meanwhile a credentialed body of
practitioners spent a decade arguing that the standard's documentation-first framing actively harms testing
[24][25][27]. And when a modern tool says "test plan" it means something else entirely: an execution
container whose only required field is a name [38][39][40].

So this bundle teaches the plan that survives all three problems: **short enough to be read, specific enough
to be checked, and risk-ranked so the reader can see why the coverage is shaped the way it is.** The value is
in the planning, not the page count [9], and the sharpest single line in the literature is Bach's: the test
plan document does not necessarily contain a test plan [14].

**The load-bearing honest-retrieval facts (do not get these wrong):**

1. **IEEE 829-2008 is "superseded," not "withdrawn."** The IEEE SA page uses the label *Superseded Standard*
   and names its four successors [1]. "Withdrawn" and "Inactive" are different IEEE status categories. A
   search-result synthesis claiming a 2024-10-28 withdrawal date **could not be confirmed from any read page**
   and is not used.
2. **Nobody in this research read 29119-3.** ISO, IEEE and BSI all sell it [3]. Every content-item list in
   circulation, including the ones here, is secondary. The companion says so rather than implying the
   standard was consulted.
3. **Sources disagree on how many sections IEEE 829 defines.** A vendor enumeration gives 16 [8]; Wikipedia
   says 15 [42]. The companion states "roughly sixteen" and does not assert a precise count, because the
   standard itself was not read.
4. **Bach is routinely misquoted as anti-test-plan.** He wrote a Test Plan Evaluation Model [16] and a
   seven-task guide to building one [17]. His argument is about the document, not the planning [15].
5. **Session-based test management is Jonathan Bach's paper**, co-credited with James Bach [18]. Attributing
   it to James alone is the common error. Michael Bolton is not an SBTM co-creator.
6. **The agile testing quadrants originate with Brian Marick (2003)**, not Crispin and Gregory, who extended
   and popularized them [20][21]. Crispin credits Marick herself [20].

**Sharpest teaching points:**
1. **The plan is not the document.** "The test plan document does not necessarily contain a test plan" [14].
   A plan nobody reads is not a safety net, it is accountability theater [31].
2. **"Features not to be tested" is the highest-value section.** It forces an explicit scope-out decision and
   creates a record of what was agreed to be left alone. **Authorial judgment, not a sourced finding:** the
   claim that it is also among the most commonly dropped sections appears in this project's own reasoning and
   in fan-out synthesis, but **no source in this log measures omission frequency**, so the companion states it
   as judgment. The same caveat applies to the suspension-and-resumption section.
3. **Risk ranks the coverage, and the plan has to show the ranking.** Risk-based testing steers effort and
   limits risk [12]; a weak approach section names test types, a strong one names which areas carry which
   risk and what depth each earns [13].
4. **Two different risks live in one plan.** Product risk (what could be broken) shapes coverage; project
   risk (what could stop the testing) shapes the schedule. The 29119-3 framing separates them, and merging
   them is why "risks" sections read as noise.
5. **Criteria are thresholds, not adjectives.** "Environment is ready" and "most tests passed" are not
   criteria [10]. ISTQB frames entry criteria functionally: they exist to stop work starting that would waste
   more effort than fixing the blocker [7].
6. **The ISTQB definition carries a rationale requirement** for criteria and technique choices [5]. **Do not
   extend this to a stakeholder-agreement requirement and attribute it to [5]:** the words "agreed with
   stakeholders" are not in the definition quoted here. That exit criteria need a named agreeing stakeholder
   and a date is **this library's own position**, and the companion says so in those terms.
7. **Pass rate and test-case count as exit criteria bake Goodhart's Law into the plan.** 98 percent of 200
   tests means four failed, and a test that checks whether a page loads is not equivalent to one that checks
   business logic [32].
8. **When a tool says "test plan," it means an execution container.** Azure Test Plans groups suites and
   cases, and the only required field on the work item is a title [38][39]; qTest models it as a release and
   build calendar [40]. That is not the document this bundle teaches, and readers who conflate the two write
   a plan with no approach in it.
9. **Test plan versus test strategy is genuinely unresolved.** ISTQB puts strategy at organization or
   programme level [6]; smaller teams carry it as a section inside the plan [35][36]. Name both usages; do
   not pick one silently.

---

## Sources (curated, deduplicated, contiguously numbered; one source per entry)

**[1] IEEE SA - IEEE 829-2008 Standard for Software and System Test Documentation.** primary.
**fetched-and-verified.**
`https://standards.ieee.org/ieee/829/3787/`
Supports: the current status label of IEEE 829-2008 ("Superseded Standard") and the named successor
standards. No withdrawal date appears on the page.
Quotable: "IEEE 829-2008 is superseded by ISO/IEC/IEEE 29119-1-2013, ISO/IEC/IEEE 29119-2-2013, ISO/IEC/IEEE
29119-3-2013 and ISO/IEC/IEEE 29119-4-2015"
Contested/time-bound: "Superseded" is a distinct IEEE category from "Withdrawn"/"Inactive". A claimed
withdrawal date of 2024-10-28 surfaced only in a search-engine synthesis and was **not** confirmed on any
read page; it is not used anywhere in this bundle.

**[2] Wikipedia - Software test documentation.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Software_test_documentation`
Supports: the supersession of IEEE 829-2008 by ISO/IEC/IEEE 29119-3:2013; the note that IEEE 829 was
influential in ISEB and ISTQB certification syllabi.
Quotable: "IEEE 829-2008 has been superseded by ISO/IEC/IEEE 29119-3:2013"

**[3] IEEE SA - IEEE/ISO/IEC 29119-3:2021, Software and systems engineering - Software testing - Part 3: Test
documentation.** primary. **fetched-and-verified (landing page only; the standard itself is paywalled).**
`https://standards.ieee.org/ieee/29119-3/7499/`
Supports: 29119-3:2021 is the current active edition, published 2021-10-28; its scope covers templates and
examples of test documentation arranged by the test processes of 29119-2; it supports dynamic, functional,
non-functional, manual, automated, scripted and unscripted testing.
Quotable: none. **No clause-level text was read.** ISO, IEEE Xplore and BSI all sell access; sample PDFs at
`cdn.standards.iteh.ai` were binary-encoded and yielded no readable text.

**[4] Wikipedia - ISO/IEC 29119.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/ISO/IEC_29119`
Supports: the series timeline (development began 2007; first parts 2013; revisions through 2021-2022; Part 5
in 2024); the existence of ISO/IEC TR 29119-6 for agile projects; a summary of the Stop 29119 campaign and
the fact that the standard was **not** withdrawn.
Quotable: "a series of five international standards for software testing"
Contested/time-bound: the article carries maintenance tags for citations and weasel words. Used for timeline
facts only, not for characterizing either camp's arguments.

**[5] ISTQB Glossary - test plan.** primary. **fetched-and-verified.**
`https://istqb-glossary.page/test-plan/`
Supports: the canonical definition of the document type, including the requirement that a plan record the
**rationale** for its choice of entry/exit criteria and test design techniques.
Quotable: "A document describing the scope, approach, resources and schedule of intended test activities. It
identifies amongst others test items, the features to be tested, the testing tasks, who will do each task,
degree of tester independence, the test environment, the test design techniques and entry and exit criteria
to be used, and the rationale for their choice, and any risks requiring contingency planning. It is a record
of the test planning process."
Contested/time-bound: no version date is displayed on the page; the glossary text descends from the IEEE
829-era vocabulary and has not been rewritten to the 29119 framing.

**[6] ISTQB Glossary - organizational test strategy.** primary. **fetched-and-verified.**
`https://istqb-glossary.page/organizational-test-strategy/`
Supports: ISTQB's org-or-programme-level definition of strategy, which is the line it draws between strategy
and a project-level plan.
Quotable: "A high-level description of the test levels to be performed and the testing within those levels
for an organization or programme (one or more projects)."
Contested/time-bound: the entry cites 2012-2014 syllabi. The glossary files the same definition under a
`test-strategy` slug, so the two terms are not distinguished there.

**[7] ISTQB Glossary - entry criteria.** primary. **fetched-and-verified.**
`https://istqb-glossary.page/entry-criteria/`
Supports: the definition of entry criteria and, more usefully, their **purpose**: to stop a task starting
when the waste of starting exceeds the cost of clearing the blocker. The page also records "Definition of
Ready" as the agile synonym.
Quotable: "The set of generic and specific conditions for permitting a process to go forward with a defined
task, e.g., test phase."; "prevent a task from starting which would entail more (wasted) effort compared to
the effort needed to remove the failed entry criteria"

**[8] Reqtest - How to Write a Test Plan with the IEEE 829 Standard.** vendor. **fetched-and-verified.**
`https://reqtest.com/en/knowledgebase/how-to-write-a-test-plan-2/`
Supports: a full enumeration of the IEEE 829 section list (test plan identifier, introduction, test items,
features to be tested, features not to be tested, approach, item pass/fail criteria, suspension and
resumption, deliverables, testing tasks, environmental needs, responsibilities, staffing and training,
schedule, risks and contingencies, approvals). This is the de facto reference most practitioners actually
read, because the standard is not free.
Quotable: "sources of test data, inputs and outputs, testing techniques and priorities"
Contested/time-bound: no author or date on the page; describes a superseded standard; enumerates **16**
sections where [42] says 15 (see contested claims).

**[9] Simon Knight - Test Planning Simplified.** practitioner. **fetched-and-verified.**
`https://sjpknight.com/post/test-planning-simplified/`
Supports: the lean-plan case; the five questions a plan must answer whatever its length (what, how, who, why,
when); three working formats (mind map, single page, testing canvas).
Quotable: "the value of the test plan is in the planning (i.e. the thinking), not the document"; "no plan
survives first contact with the enemy"
Contested/time-bound: no publication date displayed. The argument is framed for agile contexts and is not
claimed to generalize to regulated ones.

**[10] Yuri Kan - Entry and Exit Criteria in Software Testing.** practitioner. **fetched-and-verified.**
`https://yrkan.com/blog/entry-exit-criteria/`
Supports: the measurable-versus-vague contrast that makes criteria checkable ("most tests passed" against "95
percent of planned test cases executed with pass status"); applying SMART to entry and exit conditions.
Quotable: none recorded as verbatim.
Contested/time-bound: no publication date displayed.

**[11] LoadView - Performance Testing Planning: Entry and Exit Criteria.** vendor.
**fetched-and-verified.**
`https://www.loadview-testing.com/blog/performance-testing-planning-entry-and-exit-criteria/`
Supports: why criteria must exist before testing starts, stated in terms of what you cannot know without
them.
Quotable: "Teams should not begin performance testing until entry and exit criteria are defined. Without
clear criteria, it becomes difficult to know whether the test was valid, whether the results are acceptable,
or whether more testing is needed."
Contested/time-bound: vendor content from a load-testing company; its example criteria are
performance-specific and are not lifted into the template.

**[12] Michael Felderer and Ina Schieferdecker - A taxonomy of risk-based testing.** primary.
**fetched-and-verified.**
`https://arxiv.org/abs/1912.11519`
Supports: the academic framing of risk-based testing along three axes (risk drivers, risk assessment,
risk-based test process), and the purpose statement for the practice.
Quotable: "steer all phases of the test process in order to optimize testing efforts and limit risks"
Contested/time-bound: arXiv preprint submitted 2019-12-24; not confirmed as journal-published. The taxonomy
is descriptive of practice, not prescriptive.

**[13] Guru99 - Risk Based Testing: Approach, Matrix, Process and Examples.** vendor.
**fetched-and-verified.**
`https://www.guru99.com/risk-based-testing.html`
Supports: the probability-by-severity matrix and the practical consequence that risk tier selects technique
depth (decision tables and boundary analysis for high-risk areas, equivalence partitioning alone for low).
Quotable: none.
Contested/time-bound: no named author; the specific scoring formula it presents is one model among several,
not a standard.

**[14] James Bach - A Question About Test Strategy.** primary (the author's own statement of his position).
**fetched-and-verified.**
`https://www.satisfice.com/blog/archives/63`
Supports: the single sharpest distinction in this bundle, between the plan as a set of ideas and the plan as
a document; and Bach's three-way split of plan, strategy and logistics.
Quotable: "The test plan document does not necessarily contain a test plan"; "Test plan: the set of ideas
that guide a test project"; "Test strategy: the set of ideas that guide test design"; "Test logistics: the
set of ideas that guide the application of resources"
Contested/time-bound: published 2006-09-22. Bach's vocabulary (strategy as the ideas guiding test *design*)
differs from ISTQB's [6]; the companion reports both rather than harmonizing them.

**[15] James Bach - Fighting Bad Test Documentation.** primary (the author's own statement of his position).
**fetched-and-verified.**
`https://www.satisfice.com/blog/archives/19`
Supports: the "written once, never read" critique from inside the craft, and Bach's own report that testers
frequently do not follow their own documentation. This is a critique of heavyweight documentation, not of
planning.
Quotable: "Documenting is not testing. It is one of the chief distractions to testing."; "Test documentation
is often of such poor quality that it's better ignored than followed."
Contested/time-bound: published 2004-02-21, before wide agile adoption. Read alongside [16] and [17], which
are the same author building test plans.

**[16] James Bach - Test Plan Evaluation Model.** primary. **landing page fetched-and-verified; the model
PDF itself was not read.**
`https://www.satisfice.com/download/test-plan-evaluation-model`
Supports: the fact that the best-known critic of test documentation published a rubric for assessing test
plan quality, which is the evidence against reading him as anti-plan.
Quotable: "I developed this model to provide a basis to systematically assess the quality of test plans."
Contested/time-bound: originally published 1999-09-25. **The model's criteria are in the PDF and were not
read**, so no claim about its contents is made beyond its existence and purpose.

**[17] James Bach - How to Evolve a Context-Driven Test Plan.** primary. **landing page
fetched-and-verified; the guide PDF itself was not read.**
`https://www.satisfice.com/download/building-a-context-driven-test-plan`
Supports: an affirmative, iterative model for building a test plan (seven tasks, performable in any order),
which is the opposite of front-loaded waterfall planning.
Quotable: "a process guide for creating a good test plan within the RST methodology. It consists of seven
tasks. The tasks can be performed in any order, or simultaneously and iteratively."
Contested/time-bound: landing page confirmed 2021-07-07. The seven tasks are named only in the unread PDF, so
they are not enumerated anywhere in this bundle.

**[18] Jonathan Bach and James Bach - Session-Based Test Management.** primary. **landing page
fetched-and-verified; the paper itself was not read.**
`https://www.satisfice.com/download/session-based-test-management`
Supports: the test session and the charter as the lightweight unit of exploratory work, and SBTM's framing as
activity-based rather than artifact-based management.
Quotable: "activity-based test management which is an alternative to artifact-based management"
Contested/time-bound: originally published 2000-11-01. **Jonathan Bach is the primary author**; attributing
SBTM to James Bach alone is the common misattribution, and Michael Bolton is not a co-creator.

**[19] Lisa Crispin - The Agile Testing Quadrants.** primary. **fetched-and-verified.**
`https://lisacrispin.com/2024/10/11/the-agile-testing-quadrants/`
Supports: the quadrants as a planning aid, in the words of one of the two authors most associated with them.
Quotable: "a thinking tool that help teams plan and execute testing activities so that they can confidently
deliver customer value"
Contested/time-bound: published 2024-10-11.

**[20] Lisa Crispin - Agile Testing Quadrants version 3.** primary. **fetched-and-verified.**
`https://lisacrispin.com/agile-testing-quadrants-version-3-from-agile-testing-condensed/`
Supports: Crispin's own attribution of the model's origin to Brian Marick, which is the correction to the
common misattribution.
Quotable: "based on Brian Marick's agile testing matrix"
Contested/time-bound: no publication date visible; version 3 appears in *Agile Testing Condensed* (2019).

**[21] Wikipedia - Agile testing.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Agile_testing`
Supports: Brian Marick as the originator of the quadrant model, dated to his 2003-08-22 post "Agile testing
directions: tests and examples"; the two-axis structure (business-facing against technology-facing; support
programming against critique product).
Quotable: none.

**[22] Janet Gregory and Lisa Crispin - Agile Testing Condensed (Leanpub page).** primary. **book page
fetched-and-verified; the book itself was not read.**
`https://leanpub.com/agiletesting-condensed`
Supports: that test planning survives as a named practice in the agile canon. The table of contents carries a
chapter titled "Test Planning in Agile Contexts", covering the team, the product, planning across levels of
detail, and regression planning.
Quotable: none. **Only the chapter structure was read, not the chapter.**
Contested/time-bound: page last updated 2019-09-24.

**[23] Ben Linders (interviewing Eddy Bruin and Ray Oei), InfoQ - Agile Approaches to Test Planning.**
practitioner. **fetched-and-verified.**
`https://www.infoq.com/articles/agile-approaches-test-planning/`
Supports: the strongest practitioner form of the "no test plan in agile" position, useful precisely because
it is the end of the spectrum rather than the consensus.
Quotable: "Most test plans contain irrelevant and outdated information that does not contribute to quality."
(Eddy Bruin); "When test plans are required in agile projects, it is a clear sign that it is not an agile
environment to begin with." (Ray Oei)
Contested/time-bound: both are named practitioner opinions in an interview, **not** consensus positions, and
they are contradicted by [22]. Attribute each quote to its speaker, never to InfoQ or to "agile".

**[24] James Bach - How Not to Standardize Testing (ISO 29119).** primary (the author's own statement of his
position). **fetched-and-verified.**
`https://www.satisfice.com/blog/archives/1464`
Supports: the Stop 29119 argument at its sharpest: that the working group excluded the context-driven school
by design, and that the burden of proof sits with those claiming the craft can be standardized.
Quotable: "The reason they have excluded us is that they know we won't agree to any simplistic standard based
on templates or simple formulae."; "The burden is on those who claim that the craft can be standardized to
study the craft and recognize and resolve the deep differences among us."
Contested/time-bound: published 2014-08-25, at the campaign's peak. Explicitly adversarial, not a neutral
survey.

**[25] James Christie - Stop 29119 (tag archive).** practitioner. **fetched-and-verified.**
`https://clarotesting.wordpress.com/tag/iso29119-iso-29119-testing-software-testing-stop-29119-stop29119-testing-standards/`
Supports: the most actionable form of the critique for a template author: that a document can comply
completely and still say nothing.
Quotable: "The standard defines in great detail the process and the documents for testing, but fails to
clarify the purpose of testing, the outcomes that stakeholders expect."; "It would be simple to comply with
the ISO 29119 Test Completion Process, and produce a report that provided no worthwhile information at all."
Contested/time-bound: Christie initiated the campaign after CAST 2014; his Cynefin framing is disputed by
proponents of the standard.

**[26] James Christie - Has opposition to ISO 29119 really died down?** practitioner.
**fetched-and-verified.**
`https://clarotesting.wordpress.com/2018/07/21/has-opposition-to-iso-29119-really-died-down/`
Supports: that the opposition was never retracted, four years after the campaign's peak; the goal-displacement
argument (documentation compliance displacing useful testing).
Quotable: none.
Contested/time-bound: published 2018-07-21 by a named critic, not a neutral observer.

**[27] Huib Schoots, Association for Software Testing - The ISO29119 Debate.** practitioner.
**fetched-and-verified.**
`https://associationforsoftwaretesting.org/2014/09/05/the-iso29119-debate/`
Supports: the accessibility objection, which is the one a template author most needs to know, because it is
why almost nobody has read the standard they claim to follow.
Quotable: "The standard is not available publicly. How can I comply to or even discuss a standard that is not
publicly available?"
Contested/time-bound: published 2014-09-05. Stuart Reid's counter-statement, also September 2014, disputes
the commercial-interest framing.

**[28] Michael Bolton - Dramatis Personae.** practitioner. **fetched-and-verified.**
`https://developsense.com/blog/2014/09/dramatis-personae`
Supports: the conflict-of-interest strand of the critique (working-group editors affiliated with
consultancies and certification bodies that stood to benefit).
Quotable: none.
Contested/time-bound: published September 2014; the affiliations were disputed by Stuart Reid and **no
independent audit exists**. The companion reports that the dispute exists without adjudicating it.

**[29] Cem Kaner, James Bach and Bret Pettichord - Context-Driven Testing: Principles.** primary.
**fetched-and-verified.**
`https://context-driven-testing.com/`
Supports: the canonical statement of the school whose objection shapes this whole debate, and the specific
line that a standard is a suggestion rather than a prescription.
Quotable: "There are good practices in context, but there are no best practices."
Contested/time-bound: no publication date on the page. Proponents of 29119 dispute that these principles are
actually incompatible with the standard.

**[30] SD Times - The Software Testing Schism.** reference. **fetched-and-verified.**
`https://sdtimes.com/applause/software-testing-schism/`
Supports: a both-sides account naming the two camps and the gap the standard was meant to fill.
Quotable: "There was no definitive international set of software testing standards previously."; "Imposition
of a 'standard' by one faction has potential to control who calls themselves a tester."
Contested/time-bound: no date visible in the fetched body; covers the 2014 peak and not later developments.

**[31] Richard C Paterson, Ministry of Testing - How to Write a Software Test Plan.** practitioner.
**fetched-and-verified.**
`https://www.ministryoftesting.com/insights/how-to-write-a-software-test-plan`
Supports: the reformist position, which is where this bundle sits: the unread plan is waste, and the fix is a
better document rather than no document.
Quotable: "A test plan that no-one reads, which doesn't inform anyone about the testing to be done, is a
waste of your valuable time."; "A document that is not read has little value."
Contested/time-bound: published 2018-02-05.

**[32] Mykhailo Poliarush, Testomat.io - QA Metrics: The Software Testing Metrics That Actually Matter.**
vendor. **fetched-and-verified.**
`https://testomat.io/blog/qa-software-testing-metrics/`
Supports: the metrics trap in exit criteria, with the arithmetic that makes it concrete.
Quotable: "Test case count tells you almost nothing about quality. A test case that checks 'does the page
load' is not equivalent to one that checks complex business logic."; "Pass rate alone is misleading. A pass
rate of 98% in a suite of 200 tests means 4 tests failed."
Contested/time-bound: published 2026-06-11 by a vendor selling test management tooling; the critique is
consistent with independent practitioner literature, and the tier reflects the commercial interest.

**[33] BrowserStack - Test Plan vs Test Case: Core Differences.** vendor. **fetched-and-verified.**
`https://www.browserstack.com/guide/test-plan-vs-test-case`
Supports: the plan-versus-case boundary, including the audience difference that makes it practical.
Quotable: "Test plans target Testers, Test managers and any Stakeholders, whereas test cases are primarily
for the test team itself."
Contested/time-bound: vendor content.

**[34] Software Testing Magazine - Comparing Test Cases and Acceptance Criteria.** practitioner.
**fetched-and-verified.**
`https://www.softwaretestingmagazine.com/knowledge/comparing-test-cases-and-acceptance-criteria/`
Supports: that the acceptance-criteria-versus-test-case boundary is genuinely contested, with a named camp
arguing the two collapse into one artifact.
Quotable: "Based on all the definitions above, there's not a huge difference(if any) between test cases and
acceptance criteria."; "If we already have testable ACs, why should we duplicate work in creating TCs for the
same scenarios?"
Contested/time-bound: this is one side of a live disagreement, quoted here **as** a position, not as the
answer. The qa-docs family contract requires each member to place itself against acceptance criteria, and
this source is why that boundary needs stating rather than assuming.

**[35] AltexSoft - Test Plan vs Test Strategy: Structure, Goals and Differences.** practitioner.
**fetched-and-verified.**
`https://www.altexsoft.com/blog/test-plan-test-strategy/`
Supports: the admission, from a source that draws the distinction, that in many organizations the strategy is
simply a section of the plan; and the stability difference between the two.
Quotable: "in some organizations test strategy can be just a part of the test plan document, identifying the
test approach for the concrete project"; "the strategy does not change frequently if at all"

**[36] Software Testing Help - Test Plan Vs Test Strategy Vs Test Case Vs Test Scenario.** practitioner.
**fetched-and-verified.**
`https://www.softwaretestinghelp.com/difference-between-test-plan-test-strategy-test-case-test-script-test-scenario-and-test-condition/`
Supports: live practitioner disagreement about which document comes first, visible in the article and its
comments.
Quotable: "The difference between these two documents is subtle."; "In smaller projects, test strategy is
often found as a section of a test plan."
Contested/time-bound: a commenter directly contradicts the article's own framing, which is the evidence that
the boundary is unsettled rather than merely under-explained.

**[37] Yuri Kan - Test Plan vs Test Strategy: Key QA Documents.** practitioner. **fetched-and-verified.**
`https://yrkan.com/blog/test-plan-vs-strategy/`
Supports: the most usable one-line formulation of the distinction.
Quotable: "the strategy defines how you test, the plan defines what you test this time"
Contested/time-bound: the page also states that "only 42% of QA teams maintain a formal test strategy
document" **with no named source**. That figure is deliberately **not** used anywhere in this bundle.

**[38] Microsoft - Test objects and terms overview (Azure Test Plans).** primary (product documentation).
**fetched-and-verified.**
`https://learn.microsoft.com/en-us/azure/devops/test/test-objects-overview?view=azure-devops`
Supports: the terminology trap. In the tool, a "test plan" is a container that groups suites and cases, and
the only required field on the work item is a title.
Quotable: "Test plans: Group test suites and individual test cases."; "The only required field for all work
item types is Title."; "A test point is a unique combination of a test case, test suite, configuration, and
tester."

**[39] Microsoft - Create and manage test plans (Azure Test Plans).** primary (product documentation).
**fetched-and-verified.**
`https://learn.microsoft.com/en-us/azure/devops/test/create-a-test-plan?view=azure-devops`
Supports: what the tool actually asks for when you create a "test plan": a name, an area path and an
iteration, with optional dates. No approach, no risk, no criteria.
Quotable: "Create test plans and test suites to track manual testing for sprints or milestones."

**[40] Tricentis - Test Plan for Releases and Builds (qTest Manager documentation).** vendor (product
documentation). **fetched-and-verified.**
`https://docs.tricentis.com/qtest-saas/content/manager/test_plan/test_plan_for_releases_and_builds.htm`
Supports: a second, independent tool modeling "test plan" as a milestone calendar rather than a narrative
document, which is what makes the terminology trap general rather than a quirk of one vendor.
Quotable: "each project within qTest Manager has its own Test Plan in which you can define the high-level
milestones and testing objectives"

**[41] TestQuality - The Ultimate Test Plan Tools in Software Testing.** vendor.
**fetched-and-verified.**
`https://testquality.com/the-ultimate-test-plan-tools-in-software-testing-a-practical-guide/`
Supports: the vendor framing that the plan now "lives in the tool", which is the marketing claim the
companion answers.
Quotable: "They serve as living documents that guide the entire testing process from requirements gathering
through execution and reporting."
Contested/time-bound: vendor content with a direct commercial interest in the claim that the document belongs
inside a platform.

**[42] Wikipedia - Test plan.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Test_plan`
Supports: a general definition of the document type, and the observation that its three major elements
(coverage, methods, responsibilities) are also what a formal test strategy carries, which is corroborating
evidence that the two overlap.
Quotable: "a document detailing the objectives, resources, and processes for a specific test session for a
software or hardware product"; "These three elements are also used in a formal test strategy"
Contested/time-bound: states that IEEE 829-2008 specifies **15** required sections, against the **16** in
[8]. See contested claims.

---

## Claims flagged contested or time-bound

1. **IEEE 829's precise status.** Confirmed: "Superseded Standard" [1]. Unconfirmed and therefore unused: a
   2024 withdrawal date. Some practitioners still treat the 829 structure as a useful checklist even though
   it is formally superseded, which is a defensible position and not a factual dispute.
2. **How many sections IEEE 829 defines.** [8] enumerates 16; [42] says 15. Neither source is the standard.
   The companion says "roughly sixteen" and does not resolve it, because resolving it requires buying the
   document.
3. **What 29119-3 actually requires.** Every content-item list in circulation is secondary [3]. The
   shall/should/may conformance map is in an annex nobody in this research read. No claim in this bundle
   rests on the standard's normative text.
4. **Whether 29119 represents professional consensus.** The standardizers say an international working group
   produced it under ISO process [30]; the Association for Software Testing and the context-driven school say
   a group that excluded a major school cannot claim consensus [24][27]. Not adjudicated. The standard was
   **not** withdrawn and has been revised since [4].
5. **Whether the standard is compatible with context-driven testing.** Stuart Reid stated agreement with the
   context-driven principles; Bach and Kaner hold that a template-driven standard is incompatible whatever
   its preamble says [24][29]. This is an interpretive dispute, not a factual one.
6. **Whether a test plan document should exist in agile at all.** Ray Oei: its presence signals a non-agile
   environment [23]. Gregory and Crispin keep a chapter called "Test Planning in Agile Contexts" [22]. Bach
   publishes a guide to evolving one [17]. The camps disagree about the artifact, not about whether risk and
   coverage need thinking through.
7. **Whether test cases and acceptance criteria are distinct artifacts.** One camp argues testable acceptance
   criteria make test cases duplicate work [34]; the other treats them as different altitudes. Both have
   working practitioners behind them.
8. **Where the plan/strategy line sits.** ISTQB draws it at organizational scope [6]; IEEE 829 folds the
   approach into the plan [8]; practitioners openly disagree about which is written first [36]. Named as
   unsettled rather than resolved.
9. **The "42 percent of QA teams" statistic** [37] has no named source and is not used.
10. **The size of the dissenting faction.** Rex Black is reported to have put it near 1 percent; petition
    organizers cited more than a thousand signatures against a working group of a few dozen [30]. Neither
    figure has a reliable denominator, so the companion characterizes the dispute without sizing it.

---

## Notes for the companion

**Honest framing.** A test plan is worth exactly what it changes: the decisions it forces, the scope-out it
records, the criteria someone can hold you to. The bundle's job is to produce a plan short enough that it
gets read and specific enough that it can be checked, and to be candid that the formal lineage everyone cites
is superseded, paywalled, and contested.

**Load-bearing sections.** Scope and Non-Scope (the scope-out is the highest-value line in the document);
Risk-Ranked Approach (where risk-based planning actually lives, and the section vendor tools have no field
for); Entry and Exit Criteria (thresholds, agreed, with the metrics trap named).

**The two-risk split.** Product risk shapes coverage and belongs in the approach; project risk threatens the
test effort itself and belongs in its own section in the full variant. Keeping them apart is what stops the
risks section becoming a list of worries.

**What the full variant adds and why.** Test levels and types; suspension and resumption (the one that
matters when a security defect lands mid-cycle; see the omission-frequency caveat above); risks to the test
effort; approvals and change control. These are the sections a regulated or audited context needs and a two-week
feature does not.

**Relationships to state.** Upstream: the PRD and the acceptance criteria (the plan scopes what they
describe). Sideways: the test strategy, if the organization has one. Downstream: test cases (the plan's unit
of execution) and the bug report (what a failed case produces). Against acceptance criteria specifically: the
criteria say what must be true for a story to be done; the plan says how the whole effort will be organized,
at a different altitude. Against the tool: what Azure Test Plans or qTest calls a "test plan" is an execution
container, and this template is the narrative document, not that record.

**Tone.** Do not present the 16-section structure as professional consensus, and do not present the
context-driven critique as a licence to skip planning. Both errors are common; the bundle names both.
