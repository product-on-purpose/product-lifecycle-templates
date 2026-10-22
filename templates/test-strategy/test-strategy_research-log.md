# test-strategy: research log

Research conducted 2026-10-20. It builds on admission sweep 5 (2026-10-12), the prep research of 2026-10-14, the
sitting follow-up of 2026-10-15 that settled the scope, and the approved spec
(`docs/internal/tier2-specs.md:5698-6161`), specced on 2026-10-19 with ADR 0075
(`docs/internal/contracts/standing-standards.md:17-19`). The build's seven-dimension fan-out covered the canon
(ISTQB's glossary and syllabi, and secondary accounts of ISO/IEC/IEEE 29119); the structure of published program
and organization test strategies; governance, inheritance and cadence; the debates and failure modes; the
library's own neighbours and the Acme Analytics thread; true technical facts for a program-level strategy at a
SaaS analytics platform; and the gap question. The working files are numbered differently from the dimensions:
`dim1.md` holds the boundaries dimension, `dim2.md` the gap question, `dim3.md` structure, `dim4.md` the canon,
`dim5.md` the debates, `dim6.md` the example-domain facts and `dim7.md` governance.

**43 sources are recorded below: 42 fetched-and-verified and one not retrieved.** The 42 are 8 primary, 10
standards bodies, 3 reference, 14 vendor and 7 practitioner. The one not retrieved is the ISO preview of
ISO/IEC/IEEE 29119-3 [9], which returned HTTP 403 and supports no claim. Three of the 42 need a caveat before
anyone counts them. The official glossary page [2] carries no Quotable line; it is recorded because it shows the
page is an empty shell. Ofgem's two documents [10], [11] are one paper at two drafting stages, so they count as
one structural example. Playcode [22] is a negative result: read in full, it does not say what a search summary
claimed. **291 Quotable lines remain.** Only `fetched-and-verified` sources are quoted anywhere in this bundle.
In this log, quotation marks hold a source's words and backticks hold repository text.

---

## What the checks caught, and what was not read

**Every quotation was checked against the source's raw text**, not against a retrieval tool's summary: pages as
downloaded, and PDFs through a text extractor. The seven research agents returned 261 quotations. 195 passed as
returned: 190 as normalized substrings, and 5 after extraction artifacts were normalized. 66 failed.

**The main loop rescued 52 of the 66 mechanically.** All 20 Process Street steps [13] carried list numbers the
agent had prefixed. The six ISTQB definitions [1] carried glossary labels naming each term, its id and its
version in front of the definition text. Long quotations were split into sentences or table cells that pass, as
with the HNG-X heading runs [15], BrowserStack's comparison table [23], OPG's metric lists [41] and a CTAL-TM
paragraph [4]. **Twelve more were re-quoted by hand:** six k6 load-test-type sentences interrupted by Markdown
link syntax [32], one k6 opening sentence [32], four Fujitsu and Post Office document-control fields [15], and
the Pact sentence an agent had edited with a bracketed insertion [35]. **Every re-quoted span also passed against
a fresh fetch of its page, so no cache body behind them is an agent-written summary.** These counts are of spans.
A split quotation yields several Quotable lines, so the counts do not add up to the 291 that remain.

**What the drops mean for the bundle.** Three Ofgem document-control fields were dropped and not re-quoted. The
extractor scattered the form's cells, so its labels and values sit apart in the raw text. No Ofgem owner,
approver or date field is therefore a Quotable line, and the companion must not present any of them as a field
of the document. The mirror's list of
syllabi was dropped, so the finding that the mirror's text is not current rests on comparing its text [3] with
the official text [1], not on that list. A sibling companion separately records that the mirror's entry cites
2012 to 2014 syllabi (`templates/test-plan/test-plan_companion.md:506`). The official glossary page's HTML shell
[2] was dropped as a quotation; its emptiness is the finding and needs no quotation. From the HNG-X Testing
Strategy [15], the names of its approval authorities and its version-history line failed and were not
re-quoted. The four hand re-quotes from its document control are "This is a joint Fujitsu Services/Post Office
document", "describing the strategic approach to be applied for all testing", "Whole HNG-X Programme" and
"Approval Authorities". None names a person, so the companion must not name its approvers. Its 2006 date is in the
raw text and is not a Quotable line.

**Two thinner checks are recorded rather than smoothed over.** The W3C Quickref's three Quotable lines [34]
passed against the stored copy, but the fresh fetch returned HTTP 403, so the stored copy is their only check.
That copy is 133 KB of rendered page text, filter controls included, which fits a raw capture rather than an
agent's summary. The HNG-X text [15] is OCR of a scanned PDF, read through a third-party site that republishes
the Post Office Horizon IT Inquiry's evidence. The structure dimension reports its sections 4.0 and 5.0 as partly
garbled, so no subheading of 4.0 after 4.1, and no subheading of 5.0, is reported here.

**Spans the dimension files present as verbatim that are not Quotable lines.** Drafters who read the dimension
files will meet these and must not quote them: Ofgem's control-sheet fields and section headings [10]; DCC's
section headings, its whole out-of-scope sentence and its whole approval table [14]; TfL's lettered list of a
strategy's required contents [12]; the CTAL-TM sentence on how the organizational strategy influences a project's
strategy [4]; Wikipedia's sentence introducing its list of 29119-3 documents [6]; the k6 test-type names [32];
the wording of ISTQB's definition of test practice [1]; and the HNG-X approvers' names [15]. Where this log
reports any of them, it says they were read in raw text. For this log, the Ofgem, DCC and TfL headings, the k6
name pairings and the glossary's term list were checked against the stored raw text.

**What was assigned and not read, or not usable:**

- **ISO/IEC/IEEE 29119-3's own clause text** [9]: HTTP 403 on the one attempt. No sentence in this bundle may
  cite the standard's own words. Wikipedia [6] and imbus [7], [8] are secondary accounts, and imbus cites the 2013
  edition [8].
- **The official ISTQB glossary page** [2]: a JavaScript single-page app whose HTML is an empty shell. The research
  found the page's backing API in its bundled JavaScript and read the official definitions there [1].
- **The unofficial mirror**, `istqb-glossary.page` [3]: read in full, and usable only as a mirror of older text.
  Its definition is not the official glossary's current wording (Findings 1 and 2), and its FAQ's provenance is
  unverified.
- **ICO anonymisation guidance**: only its contents page resolved. It has no entry here.
- **Montclair State University's test-strategy template**: a 404. **Aarhus University's planning document**: seen
  only in a search snippet, never fetched. **A Post Office quality assurance strategy** (inquiry evidence
  POL00337565) that mentions quality gates: partial and garbled, not read in full. None has an entry, and no claim
  rests on any of them.
- **No Australian, New Zealand or Canadian government test strategy, and no NHS- or GOV.UK-branded one**, was found
  as a retrievable document.
- **Candidate prevalence figures** (a Bangladesh case study, a 2006 TechRepublic poll, a 2008 Seapine survey, a 2013
  PractiTest report and a 2023 slide compilation) appeared only in search summaries and were never fetched. None
  has an entry. **No Quotable line carries a prevalence statistic for how many organizations keep a test strategy,
  so none may appear in this bundle.**
- **The normative WCAG 2.2 Recommendation** was not read; only the Quickref [34] was.
- **No context-driven text states its disagreement with ISTQB's definition in those words.** Bach's model page
  [27] shows a contrast in kind, not a quoted exchange.
- **Sources the spec cited that this build did not re-read**: the 2009 academic slide deck, the vendor guide
  asserting organization-wide scope, the HMRC blog claim, and PMI's and APM's definitions
  (`docs/internal/tier2-specs.md:5798-5822`). They have no entry here, so the companion cannot cite them from this
  log.

---

## Findings

### 1. Definitions, and the hierarchy of test policy, organizational strategy and project plan

**ISTQB's current official glossary defines the organization-level artefact, and that definition does not
mention a program.** It defines organizational test strategy as "A strategy that describes the generic
requirements for testing and how to perform testing within an organization." [1]. Test policy sits above it:
"High-level documentation describing the principles, approach and major objectives of the organization regarding
testing." [1]. The plain
term test strategy is generic: "A description of how to perform testing to reach test objectives under given
circumstances." [1]. Test approach is a separate, narrower term, "The manner of implementing test tasks." [1]. A
master test plan is a plan: "A test plan that is used to coordinate multiple test levels or test types." [1].
Verified for this log against the stored API body, which holds 1,128 terms in one array: no definition in it
contains "organization or programme" or "one or more projects". The official definition also calls the artefact
"A strategy" [1], not documentation, while the policy definition says "documentation" [1]. Confidence: high.

**The mirror's text is older, and it is the only source of the program wording.** `istqb-glossary.page` serves
the same definition under its test strategy and its organizational test strategy entries: "A high-level
description of the test levels to be performed and the testing within those levels for an organization or
programme (one or more projects)." [3]. That is not the current official wording of either term [1]. The spec's
admission section quoted this mirror as ISTQB's glossary, and it said a build should fetch the official page
rather than carry the citation forward (`docs/internal/tier2-specs.md:5748-5756`). This build did, and the two
texts differ.

**The hierarchy, as ISTQB's syllabi describe it.** The Advanced Test Management syllabus treats the
organizational strategy as an input it does not teach: "Throughout this syllabus, the organizational test
strategy is taken as given." [4]. It "focuses on test management at the project level and not test management at
the organizational level" [4]. It says understanding "the test policy and the organizational test strategy" is
critical to test planning [4]. Its project test strategy covers "a project, a release, a product, or any other
type of system development or acquisition initiative" [4]. That strategy "is typically documented in a test plan
or as part of other documents" [4], and "Documentation of the test strategy is recommended, but not necessarily
in the form of a formal test plan." [4]. The Foundation syllabus puts the deviation inside the plan: a test plan
"Demonstrates that testing will adhere to the existing test policy and test strategy (or explains why the testing
will deviate from them)" [5]. Its list of a plan's test approach contents includes "deviations from the test
policy and test strategy" [5].

**Secondary accounts of ISO/IEC/IEEE 29119, labelled as such.** Wikipedia's article names "Organizational Test
Strategy" and "Test Plan (including a Test Strategy)" as separate items in its account of Part 3 [6]. It says
Part 2's processes sit at "the organizational level, test management (project) level, and dynamic test process
levels" [6]. The sentence introducing its Part 3 list did not pass as one span, so the companion may name the
items and must paraphrase the framing. imbus's entry for the organizational artefact cites "ISO/IEC/IEEE
29119-1:2013-09" [8]. It calls the artefact a "document that expresses the generic requirements for the testing
to be performed on all the projects run within the organization" and says "It is aligned with the Organizational
Test Policy" [8]. It adds: "An organisation could have more than one Organizational Test Strategy to cover
markedly different project contexts." [8]. imbus's separate test strategy entry says "The test strategy is a
distinct entity from the Organizational Test Strategy." [7]. Yet that entry's first sense, "Documentation aligned
with the test policy that describes the generic requirements for testing and details how to perform testing
within an organization" [7], reads as the organizational artefact. The page draws a line it does not hold, and
this log flags the tension rather than resolving it.

**The rename question is open, and nothing read settles it.** The CTAL-TM syllabus says the organizational test
strategy is considered in the context of ISO/IEC/IEEE 29119-3, where it is called an "organizational test
practice" [4]. No other source read uses that phrase. The official glossary has no entry by that name: its only
terms containing the word practice are community of practice and test practice, verified for this log against the
stored API body [1]. Wikipedia [6] and both imbus entries [7], [8] still say "Organizational Test Strategy". The
Foundation syllabus's change log renames a neighbouring term, "organizational test policy -> test policy" [5];
that is the policy, not the strategy. The standard's own text was not retrieved [9]. **Nothing read settles
whether the current 29119-3 calls the artefact an organizational test strategy, an organizational test practice,
or both.** One point cuts against the spec's worry (`docs/internal/tier2-specs.md:5784-5789`): ISTQB's current
glossary still lists organizational test strategy as its own term [1]. A rename in the standard, if real, has not
reached ISTQB's glossary. Confidence: high that the question is open; low on which way it resolves.

### 2. Scope: what the organization-or-program ruling now rests on

**The program half of the 2026-10-15 ruling no longer rests on ISTQB's current glossary text.** The spec read
ISTQB's text as hedging between organization and program (`docs/internal/tier2-specs.md:5808-5811`). ADR 0075
calls it `ISTQB's own hedge`
(`docs/internal/decisions/0075-test-strategy-joins-standing-standards-as-a-foundation.md:241-243`). That hedge is
the mirror's older text [3]. The current official definition says "within an organization" and nothing more [1].
Three repository records rest on the mirror for the program wording: the spec's admission section
(`docs/internal/tier2-specs.md:5748-5756`), ADR 0075's admission paragraph (`0075-...:60-62`), and the `test-plan`
companion, which quotes the mirror's definition as ISTQB's and tags the mirror primary
(`templates/test-plan/test-plan_companion.md:379-382` and `:506`).

**The organization half rests on** ISTQB's current definition [1] and syllabus [4], imbus's secondary account [7],
[8], and OPG's baseline, a published standing strategy "that we expect applications to adhere to" [41]. Vendor
sources describe a company-level document: QATestLab says "it is developed at the level of the whole company, and
it can be used for different projects" [24], and TestRail calls it "A long-term document that evolves with the
organization's needs and growth." [20]. The IRS's IT testing procedure binds every "system, program, or test plan"
in its scope [42].

**The program half now rests on published program-level strategies**, each the parent of more detailed plans
inside one named program:

- Ofgem's testing strategy calls itself "an enduring document for use within the programme by all parties" [10]
  and says it "will be followed by a more detailed programme level Testing Management Plan" [11].
- DCC's joint test strategy for the smart metering program sets out how the DSP, the CSPs "and all other Service
  Providers" will test [14]. Its testing "will be further elaborated in the Test Approach and Test Plan documents"
  [14].
- The HNG-X Testing Strategy is a "joint Fujitsu Services/Post Office document" [15]. It covers "all the testing
  and integration activities required across the whole HNG-X programme" [15], and leaves detail to "a series of
  subordinate documents" [15]. It excludes the parallel and later release trains, which "will be covered in
  separate testing strategy documents specific to those Horizon releases" [15].
- TfL's schedule is a contract, not a filled strategy. It requires the supplier to "prepare and submit to TTL a
  Test Strategy" [12]. Each test plan must state where it "differs from the Test Strategy, together with the
  reasons and rationale for such differences" [12].
- A recruiter's posting for a "Program Test Manager" lists the Test Strategy among that role's artefacts and ties
  the role to "program testing activities" [19].

**Two cautions belong with that list.** First, the sources are not all independent. Ofgem's paper names SMIP
among the projects it examined for lessons learned (read in raw text; not a Quotable line). Reading that
abbreviation as DCC's smart metering program is the structure dimension's reading, so [10] and [14] are probably
related. Second, none of these documents uses the ruling's phrase, `more than one project`
(`docs/internal/tier2-specs.md:5809`). Each governs several phases, parties, test phases or releases inside one
program. Reading that as more than one project is this library's interpretation, the same reading the ruling
made. ADR 0075 names only Ofgem and TfL as the program evidence (`0075-...:240-241`); DCC [14] and HNG-X [15]
widen it.

**HNG-X is cited for its shape, not as a model of practice.** It was disclosed as evidence to the Post Office
Horizon IT Inquiry [15]. This log uses it only for its structure and its program scoping. The companion must say
so wherever it cites it, and must not present it as an example of good testing.

**Portfolio stays out.** No source in this log uses the word. The exclusion rests on the 2026-10-15 follow-up the
spec records (`docs/internal/tier2-specs.md:5808-5822`), which this build did not re-read and cannot quote.

**What this does to the ruling.** The ruling stands, and its ground has moved. ISTQB now supports the organization
half only. The program half rests on primary program documents rather than on a certification body's wording.
Confidence: high that the current official definition lacks the program wording, since the research found it and
this log re-verified it against the stored body; medium that the program documents show use across more than one
project, since that is an interpretation.

### 3. What published program and organization strategies contain

**The HNG-X Testing Strategy is the only filled strategy whose headings are Quotable lines** [15]: "0.0 Document
Control", "0.1 Document History", "0.2 Review Details", "0.4 Abbreviations/Definitions", "1.0 Introduction", "1.2
Purpose of Document", "1.4 Context", "2.0 Rationale & Outline Approach", "2.2 Implications for Testing &
Integration", "3.0 Goals & Objectives", "4.0 Strategic Approach", "4.1 Objective Driven Testing", "5.0 Testing
Coverage", "6.0 People, Skills & Responsibilities", "7.0 Assumptions, Dependencies, Risks & Constraints", "7.2
Dependencies", "7.3 Risks" and "7.4 Constraints". The other headings in its runs, its scope heading among them,
did not pass.

**All twenty Process Street steps are now Quotable lines** [13], which retires the spec's risk 4
(`docs/internal/tier2-specs.md:6058-6060`). In order: "Identify objectives of the test strategy document",
"Determine target audience for the document", "Outline scope of the tests", "Identify necessary test levels",
"Identify types of testing to be performed", "Select test techniques", "Establish test environment and tools
requirements", "Approval: Test Environment Specifications", "Determine resource requirements", "Define test
deliverables", "Develop test schedule and estimation", "Identify test entry and exit criteria", "Identify risks
and dependencies", "Develop risk mitigation strategy", "Approval: Risk Mitigation Strategy", "Compile all
information into the test strategy document", "Conduct initial review of test strategy document", "Approval: Test
Strategy Document", "Revise and finalize test strategy document based on feedback" and "Distribute finalized test
strategy document to relevant stakeholders". The page states no licence (`docs/internal/tier2-specs.md:5762-5763`),
so the steps may inform section naming and may not be copied into a template.

**Ofgem's, DCC's and TfL's contents were read in raw text, not as Quotable lines.** Checked for this log against
the stored raw text, Ofgem's paper has sections on the scope of testing, key risks, testing roles, testing
deliverables and documentation, test issue, change and configuration management, test coverage and
prioritisation, and testing entry and exit criteria [10]. DCC's contents list runs from change forecast, reviews
and approvals, terminology and out of scope, through test strategy objectives, test governance and management,
progress reporting, and test entry and exit criteria, to test data, stubs, environments, labs and tools, and test
issue management [14]. TfL's clause 3.1 sets a strategy's minimum contents, among them a high-level test plan and
schedule, entry and exit criteria for each test stage, and the roles of everyone involved [12]. Only the clause's
opening sentence, and the test-plan clause on differences, are Quotable lines [12].

**What recurs** across the four independently structured documents (Ofgem, TfL, DCC and HNG-X, with Ofgem's two
drafts counted once):

- **Roles and responsibilities**, in all four ([10], [12] and [14] in raw text; "6.0 People, Skills &
  Responsibilities" [15]).
- **Entry and exit criteria**, in three ([10], [12], [14], all raw text), in the Process Street step "Identify test
  entry and exit criteria" [13], and in QATestLab's account of what a strategy includes [24]. The spec's section
  table has no home for them (`docs/internal/tier2-specs.md:5966-5974`).
- **Risks, dependencies or assumptions**, in three: Ofgem's table of key risks with their mitigations [10] and
  DCC's dependencies section [14], both raw text, and HNG-X's "7.0 Assumptions, Dependencies, Risks & Constraints"
  [15]. Two Process Street steps cover risk [13].
- **An explicit scope with named exclusions**, in DCC, whose out-of-scope items include "Certification of Comms
  Hubs" [14], and in HNG-X, which excludes named release trains [15]. Ofgem places itself inside one workstream:
  "This testing strategy forms part of the Delivery Strategy workstream within the Blueprint Phase of the Switching
  Programme." [10].
- **Document control and named approval**, in DCC, whose approval rows name the approver by role, "DCC Design &
  Assurance Director" [14], and in HNG-X ("0.1 Document History", "0.2 Review Details", "Approval Authorities"
  [15]). Process Street makes approval a step [13].
- **Terminology**, in DCC (raw text) [14] and in HNG-X's "0.4 Abbreviations/Definitions" [15].
- **Test data and environments** as a headed section in DCC only (raw text) [14], and in Process Street's step
  "Establish test environment and tools requirements" [13].
- **Defect or issue management**, in Ofgem and DCC, both raw text [10], [14].

**The tier beneath the strategy has a different name in every source**: a "programme level Testing Management
Plan" [11], "Test Approach and Test Plan documents" [14], "a series of subordinate documents" [15], and Test Plans
[12]. ISTQB uses test approach for a plan-level term [1], [4]. No source's naming is canonical, and in this
library the subordinate document is `test-plan`.

**No standards-tier Quotable line names the classic four test levels.** The only Quotable line naming
"component, integration, system, and acceptance testing" is the mirror's illustration [3]. Process Street asks the
author to "Identify necessary test levels" without naming them [13]. The Foundation syllabus lists "test levels"
among a plan's approach contents [5]. Vocke's article gives Cohn's three layers: unit, service and user interface
tests [29]. Inside the library, `templates/test-plan/test-plan_template-full.md:101-102` names unit, integration,
system and end-to-end levels. The spec's Test Levels and Types row sources its list to the catalog and to imbus's
structural listing (`docs/internal/tier2-specs.md:5969`), and that listing is not a Quotable line. imbus's content
list [7] also sits on the entry that its own first note separates from the organizational artefact.

### 4. How project plans inherit or deviate, and who approves

**Inheritance is the relationship every program source describes.** Ofgem [10], [11], DCC [14], HNG-X [15] and
TfL [12] each put a more detailed document beneath the strategy. The CTAL-TM syllabus describes the project side:
the test approach is defined "Based on the organizational test strategy, regulatory standards, any constraints
given by the project, and the risk treatment approaches" [4]. Where the organizational strategy is missing or
silent, "test management must seek to clarify the missing details with the relevant stakeholders" [4]. TestRail
says a strategy "should be tailored to the specific context rather than copied unchanged between projects" [20].
Edana describes formalizing the organizational strategy first and tailoring it into a project-specific test plan
[21].

**Ofgem shows what the strategy leaves to the plan.** Its plan defines "the detailed testing approach for each
test phase, entry and exit criteria, detailed roles and responsibilities, reporting arrangements, etc." [10]. In
raw text, the same paper also sets generic entry criteria for all test phases [10]; that passage is not a Quotable
line. So the strategy states the generic rule and the plan states the detail. That reading is this log's.

**A deviation is recorded in the plan, with its reason.** Four sources say so in their own words. The Foundation
syllabus's plan "explains why the testing will deviate" [5]. TfL's plan states the "reasons and rationale for such
differences" [12]. OPG's local variance "should be a conscious choice and be able to be explained and preferably
documented e.g. in an ADR" [41]. The mirror's FAQ says "The test plan records the rationale for any deviation"
[3], with unverified provenance. `test-plan`'s `test_strategy_ref` field is already the seam
(`templates/test-plan/test-plan_template-full.md:7`).

**A named approver for a deviation appears in one source, and it is not a test strategy.** The IRS manual has two
levels: "Any waivers or deviations of this Directive require written approval from the ACIO, Enterprise
Services." [42], and "Test Case Deferral and Waiver Requests are initiated within the test team and are approved by
the PM" [42]. The IRS manual is a directive over every test plan, not a strategy document. The governance
dimension found no source stating a sign-off step for a deviation from a standing strategy. The gap dimension
found the IRS directive. The two agree once the directive's kind is stated, and OPG [41] names no approver.

**Who owns and approves the strategy itself: the sources disagree on granularity.**

- TestRail: "Created and maintained by QA managers, test leaders, and strategic teams overseeing testing
  processes." [20].
- Edana: "The strategy is overseen by a QA board or a cross-functional committee including IT, business and
  architecture representatives." [21]. Each version is "approved by the QA committee and distributed to project
  teams" [21].
- QATestLab: "Project Manager prepares Test Strategy." [24].
- The job posting: a "Program Test Manager" who will "Manage, define, approve and plan test artefacts" [19].
- DCC: "The DSP will keep this document up to date." [14]. The document is then "issued to the DCC Licensee's
  Design Assurance Board (DAB) for approval" [14].
- HNG-X: "Approval Authorities" spanning both organizations [15], whose names are not Quotable lines.
- Process Street: "Approval: Test Strategy Document" and a final distribution step [13].
- The mirror's FAQ: "Typically the organization's test management or QA function." [3], provenance unverified.

The audience is wider than the owners. Software Testing Help says "Test strategy is intended for the complete
project team" and lists sponsors, business experts, developers, integration partners and release teams [17].

**This moves the catalog's owner value.** The spec says the catalog's `QA Manager` owner is not contradicted
(`docs/internal/tier2-specs.md:6006-6013`). QATestLab now contradicts it [24], while TestRail [20] and the mirror
[3] support it. The value can stand with the disagreement recorded; the reviewer decides.

### 5. Living document or stable document

**Three camps, named.**

- **Stable once approved.** Software Testing Help's comparison table: "Test strategy usually will not change once
  approved." [17]. QATestLab: "Test Strategy is a static long-term plan." [24]. BrowserStack: a strategy "usually
  remains stable across multiple projects or releases" [23].
- **Living and evolving.** ReqTest: "The test strategy is a living document and evolves over time" [16]. Tricentis:
  "A good testing strategy isn't static." [18]. TestRail: "A long-term document that evolves with the
  organization's needs and growth." [20].
- **Stable, and changed on named events.** Edana: "As a stable, long-term document, it is updated when major
  changes occur in technology, tools or team maturity." [21]. Ofgem: "an enduring document" that "should be updated
  again in DLS and periodically thereafter to ensure continued relevance" [10]. DCC: "Each new version supersedes
  the previous version in its entirety." [14].

**One source names two camps itself.** Software Testing Help's body text says "The test strategy document is a
living document" [17]. Its note attributes the other view to others: "Some people believe that once defined, the
test strategy should never be changed." [17].

**Read against the contract**, the third camp is the fit. Section 1 says members are `not revised on a calendar`
(`docs/internal/contracts/standing-standards.md:27-28`). A strategy that stays stable and changes when a named
event makes it wrong satisfies that. This is the library's reading; no source frames it against a contract.

### 6. Review triggers and cadence

**Condition-based triggers, in the sources' words.** TestRail: "There is no universal review schedule." [20], and
"A strategy should be reconsidered when changes to the product, architecture, risks, technology, development
model, regulations, or organizational objectives make the existing approach less appropriate." [20]. TestRail also
says "Project-level strategies may need more frequent adjustment than long-lived organizational guidance." [20].
Edana names technology, tools and team maturity [21], and says the strategy changes "only during major QA process
or tool revisions" [21]. Tricentis says a good strategy "incorporates feedback from past releases" [18]. GOV.UK
says browser-support decisions "cannot be something you specify at the start of your project and then forget
about" [38].

**Calendar cadence is contested.** TestRail denies a universal schedule [20]. Edana says the strategy "is reviewed
during annual or semi-annual assessments, incorporating lessons learned, technological innovations and regulatory
updates" [21]. Ofgem says "periodically thereafter" [10]. Edana describes one governance model, and no source says
an annual review is common practice.

**The spec's four candidate conditions, mapped to the research** (`docs/internal/tier2-specs.md:5944-5955`):

1. **A project's plan records a deviation.** The deviation mechanism is sourced [3], [5], [12], [41]. That a
   recorded deviation should prompt a review of the strategy is the library's synthesis; no source says so.
2. **The test policy changes.** The alignment rests on imbus's secondary account [7], [8], and the trigger is the
   library's synthesis. TestRail's "organizational objectives" and "regulations" are the nearest sourced
   conditions [20].
3. **A test summary report shows a mandated level or type was skipped.** The nearest source is the IRS's waiver of
   a planned test case, which means "departing from the course established in the test plan" [42], together with
   the lessons-learned language in [18] and [21]. The condition as the spec states it is the library's synthesis.
4. **A new level, tool or environment is adopted across projects without the document changing.** Sourced by
   TestRail's "technology" [20] and Edana's "tool revisions" [21].

**Not found:** the governance dimension found no source naming an escaped defect or an organizational restructure
as a trigger. **No source in this log names who notices**, which the contract requires
(`docs/internal/contracts/standing-standards.md:146-147`). The owners in Finding 4 own the document; none is named
as the watcher of a condition.

### 7. The plan-versus-strategy boundary, and the context-driven meaning of "test strategy"

**Where most sources draw the line.** BrowserStack: a plan "defines how testing will be executed for a specific
project, release, feature, or sprint" [23], and a strategy "is broader in scope and usually remains stable across
multiple projects or releases" [23]. Its table marks the plan "Derived from the test strategy" and the strategy
"Independent of individual projects" [23]. QATestLab draws the same line with a size condition: "Test Strategy
can be a part of the Test Plan if a project is small." [24].

**Where the direction of dependency flips.** Wikipedia's test plan article: "A test plan documents the strategy
that will be used to verify and ensure that a product or system meets its design specifications and other
requirements." [26]. It says the plan's three major elements "are also used in a formal test strategy" [26], and
never puts the strategy above the plan. ISTQB agrees that a project's strategy usually lives in its plan [4]. That
is the per-project sense, which `test-plan` already covers (`templates/test-plan/test-plan_guide.md:41-45`).

**The context-driven sense is a thinking tool, not a standing document.** Bach's Heuristic Test Strategy Model is
"a set of guideword heuristics designed to help you think better about test strategy" [27]. Bach encourages
readers to "modify this to fit the context of your own organization" [27]. Crispin's quadrants rebuild the
strategy per iteration: "Repeat this process as you plan each iteration." [28]. Crispin calls them "simply a
taxonomy that helps teams plan their testing" [28]. The CTAL-TM syllabus concedes that the generic term "can be
used in any context (project, organization, product)" [4]. No source read states the context-driven disagreement
with ISTQB as a quoted exchange; the contrast is in what each treats as a test strategy.

**Terminology itself is unsettled.** Vocke: "The software development community simply hasn't managed to settle
on well-defined terms around testing." [29]. On consistency within a team or organization, Vocke says "that's
really all you should care about" [29]. The library already holds the boundary as unsettled
(`templates/test-plan/test-plan_guide.md:41-43`), and spec risk 9 requires this companion to say so
(`docs/internal/tier2-specs.md:6074-6078`).

### 8. Failure modes

**BrowserStack names six**, each a labelled mistake [23]: "Treating Both Documents as the Same", "Overdocumenting
Everything", "Not Updating Documentation", "Missing Clear Ownership", "Ignoring Agile and CI/CD Workflows" and
"Prioritizing Documentation Over Execution". On overdocumenting: "Excessively detailed documents increase
maintenance effort and are rarely followed during actual testing." [23].

**Shelfware, in a practitioner's words.** Kolarov opens with the image most readers hold: "A big document of 40+
pages with ton of theory, no one reads and is not up to date." [25]. The same abstract answers it: "each Agile
project needs Test Strategy as a guidance how testing is done." [25], and "one strategy cannot fit all" [25]. It
also asks the question this bundle must answer: "Why you cannot have a template and just fill it in?" [25].

**Copying instead of tailoring.** TestRail warns against a strategy "copied unchanged between projects" [20].

**A standing strategy with a blank where an obligation sits.** OPG's published baseline leaves one shared term
undefined: "Accessibility To be defined" [41]. GDS states that "Government services are legally required to be
accessible." [43]. A published standing strategy can therefore omit what a binding obligation requires. One
instance says nothing about how common that is.

**Levels out of balance.** Vocke warns against "a test ice-cream cone that will be a nightmare to maintain and
takes way too long to run" [29].

**The family's own failure mode.** The contract says members fail `by going quietly out of date`
(`docs/internal/contracts/standing-standards.md:145`). BrowserStack's "Not Updating Documentation" [23] and
Kolarov's "not up to date" [25] are the same failure in the sources' words.

### 9. Example-domain facts

These are facts the example may state, each from a Quotable line, for a program-level strategy at a SaaS
analytics platform with a web app, an API and data pipelines. The example labels every figure illustrative.

- **Test types for a web service.** GOV.UK lists capacity and performance testing, vulnerability and penetration
  testing, exploratory testing, accessibility testing and functional testing [39]. It says "You should aim to
  automate as much of your testing as possible and run your test suite as part of continuous integration" [39].
- **Level balance.** "Write lots of small and fast unit tests. Write some more coarse-grained tests and very few
  high-level tests that test your application from end to end." [29].
- **Data tests in pipelines.** dbt's singular tests are "one-off assertions usable for a single purpose" [30]. dbt
  ships "four generic data tests already defined: unique, not_null, accepted_values, and relationships" [30]. A
  test passes on "zero rows" of failing records [30], and dbt recommends testing "any assumptions on your source
  data" [30]. Great Expectations: "An Expectation is a verifiable assertion about data." [31], and "A Checkpoint is
  the primary means for validating data in a production deployment of GX." [31]. Neither introduction carries a
  caution about cost or false positives.
- **Load testing of dashboard queries.** k6: "Start with smoke tests, then progress to higher loads and longer
  durations." [32]. It describes six load-test types. Their names (smoke, average-load, stress, soak, spike and
  breakpoint) sit inside link syntax and were paired with their descriptions in raw text, not as Quotable lines
  [32]. One type exists to "gradually increase load to identify the capacity limits of the system" [32]. k6's API
  guide: "Use Checks to assert system responses and use Thresholds to ensure that the system performs within your
  SLOs." [33]. GOV.UK: "You need to do capacity planning before you can set up realistic performance tests for your
  service." [40]. Load rises "until the service breaks in some way" [40], and the team records "the load at which
  the service broke" [40].
- **Accessibility.** GDS says UK government services "must comply with the international WCAG 2.2 AA accessibility
  standard" [43]; the example must not present a UK legal duty as binding on a fictional company. The W3C's
  contrast criterion requires "a contrast ratio of at least 4.5:1" for text, with large text at 3:1 [34]. No
  Quotable line states that criterion's number or level, so the example must not state them as sourced. GDS adds
  "Automated testing can only find around 30% of likely accessibility problems" [43], a figure whose method this
  log does not carry. The Saved Views test plan already targets WCAG 2.2 AA
  (`templates/test-plan/test-plan_example.md:72`, `:84`).
- **Contract testing between services.** Pact: "Contract tests assert that inter-application messages conform to a
  shared understanding that is documented in a contract." [35]. In Pact's consumer-driven pattern, "The contract is
  generated during the execution of the automated consumer tests." [35]. Pact's caution, that a pattern "does not
  provide any test based assurance that the consumers are calling the provider in the correct manner" [35],
  concerns provider-side contract testing used alone; that antecedent was read in raw text.
- **Environments.** GOV.UK's ladder runs from development environments to "an integration environment" and "a
  staging environment" [37], and "you must test it thoroughly in a staging environment that replicates the
  production environment as closely as possible" [37].
- **Test data and personal data.** AEPD's post quotes the European Data Protection Supervisor's guidelines for EU
  institutions; that attribution was read in raw text and is not a Quotable line [36]. In testing, "sampling of
  real personal data should be avoided" [36]; "artificially created test data" is preferred [36]; and where it
  cannot suffice, the decision to use real data "must be taken and documented" [36]. Pre-production risk "may also
  be higher" than production risk [36]. The IRS: "If live data is used, prepare live data waiver, and ensure all
  testers have complete live data training." [42].
- **Browser support.** GOV.UK: services "do not have to look perfect in every browser" [38]. Its table "represents
  approximately 98% of the most popular browsers used on GOV.UK" [38], a figure tied to GOV.UK's own traffic.
  Internal services should "look at your analytics data and check which browsers your users are using" [38].

### 10. The gap question: what a good standing strategy does that the common sections do not ask for

The commonest sections are purpose and scope, levels and types, tools and environments, governance, roles, entry
and exit criteria, and risk. The gap dimension found these leads, each resting first on a primary public-sector
source:

1. **A standing regression rule.** OPG: "Regression should be built into automation at the unit and integration
   level" and "An automated regression test should be added whenever you find a bug." [41]. A types list names
   regression; it does not make a found bug create an obligation.
2. **Shared metrics every project reports.** OPG requires every suite to measure coverage, as a whole and "As a
   delta introduced by each pull request" [41], plus execution time and reliability, "For example tracking how
   often particular tests fail to highlight flaky tests" [41]. It tracks ticket time to release under the question
   "Is our strategy improving the team workflow" [41]. The IRS: "The EST Test Report is an aggregated status report
   of all active projects in EST" [42], counting test cases "completed, passed, failed, deferred, or waived" [42].
   Edana names "performance indicators to evaluate testing effectiveness across the enterprise" [21].
3. **A named deviation mechanism at two levels.** OPG's documented variance [41], and the IRS's directive-level
   and test-case-level approvals [42] (Finding 4).
4. **Non-functional types made mandatory by an external obligation.** The IRS: "All system, program, or test plans
   must include verification strategies addressing system integration, acceptance, regression, privacy, and
   security" [42]. GDS makes accessibility a legal requirement [43], retested "especially when you introduce a
   significant feature or make any major change" [43].
5. **Test data as a governed activity.** The IRS's live-data waiver [42], and its data-use form that documents "the
   movement or replication of SBU data between environments" [42]. AEPD's regulator guidance [36] is the
   data-protection counterpart; it is guidance, not a strategy.
6. **Traceability as a maintained artefact.** The IRS's tooling ensures requirements can be "mapped to specific
   business processes, systems development documents, test cases and test results" [42].
7. **Evidence that the strategy itself is followed.** The IRS names a check that is "EST's primary pre-audit
   process to ensure compliance with IT Testing Process and Procedures" [42]. That artefact's name is in the gap
   dimension's reading of the raw text, not in a Quotable line.
8. **A shared glossary of terms.** OPG: "we have undertaken an exercise in agreeing common testing terms and their
   meaning in the OPG context" [41]. HNG-X has "0.4 Abbreviations/Definitions" [15], and Vocke says the terms are
   unsettled [29]. The gap dimension did not number this lead; this log adds it from the same sources' Quotable
   lines.

**Leads looked for and not found**: who maintains a shared automation framework; how a strategy onboards new team
members; a cross-project quality gate distinct from per-project entry and exit criteria (the one candidate,
POL00337565, was not read); and a named environment-booking system in a qualifying source. These are research
gaps, not confirmed absences. **Each lead's primary source is a government body bound by law and audit** ([41],
[42], [43]). Whether each fits a SaaS company's program is the library's judgment.

---

## The library's own boundaries and landing sites

### What the standing-standards contract obliges

From `docs/internal/contracts/standing-standards.md`, re-read for this log. Several of `dim1.md`'s line numbers
were off by one to five lines; the numbers below are the corrected ones.

- **Section 3** (`:121-138`): the eight files (`:123`); nesting, from which single-size members are exempt but
  `not from anything else` (`:124-125`); Approach A guidance comments in every section, with a `How to fill this
  in` preamble stating the N/A rule and the self-grade step (`:126-128`); the 11-section companion skeleton
  (`:129-130`); the guide shape, with at least six named anti-patterns (`:131-132`); citations, with this family's
  hazard named as folklore presented as standard (`:133-136`); and one example independent of the template's own
  GOOD and WEAK text, with no member grandfathered (`:137-138`).
- **Section 4** (`:140-158`): every member's template carries a review trigger with a named owner and a
  condition, not a calendar reminder (`:146-147`). The shared-scenario posture is weaker by design, because a
  standing standard belongs to a team rather than to a moment in a story (`:154-158`).
- **Section 5** (`:160-164`): example content never leaks into templates.
- **Section 2** (`:72`, `:74`): `sizes_available: [lean]` where research shows no second weight; `pairs_with`
  verified per member. The spec checked it as empty (`docs/internal/tier2-specs.md:6034-6041`), and nothing here
  changes that.
- **Section 6** (`:174-178`): example independence is enforced by `tools/check-example-independence.py`; the review
  trigger is a review obligation.

**What the example checker tests.** `tools/check-example-independence.py` compares a bundle's own GOOD and WEAK
snippets (`guidance_snippets`, `:56`) with the same bundle's example prose (`example_prose`, `:69`). A shared run
of 6 words warns and 8 fails (`:45-46`). `test-strategy` cannot enter its `GRANDFATHERED` map (`:174`). It cannot
catch a fully reworded illustration (`:251`). It does not check the reverse leak, the example's nouns copied into
guidance; that is the manual grep spec risk 8 names (`docs/internal/tier2-specs.md:6071-6073`).

### The Acme Analytics names and dates

**Reuse**, as the spec directs (`docs/internal/tier2-specs.md:6090-6111`):

- The program: Reporting Platform Modernization (`templates/kpi-dashboard/kpi-dashboard_example.md:2-3`,
  `templates/risk-register/risk-register_example.md:2-3`, `templates/raid-log/raid-log_example.md:2-3`).
- Marta Reyes (Program Manager), who owns the KPI dashboard, the risk register and the RAID log
  (`kpi-dashboard_example.md:5`, `risk-register_example.md:4`, `raid-log_example.md:5`): a plausible approver.
- Anjali Rao (QA Lead, Reporting), the test plan's owner and the summary report's author
  (`templates/test-plan/test-plan_example.md:4`, `templates/test-summary-report/test-summary-report_example.md:6`):
  the natural owner.
- The governing bodies the thread already names: a `Program steering group` (`kpi-dashboard_example.md:4`), and a
  `program board` with `workstream leads` (`raid-log_example.md:7`).
- Others: Priya Nair (PM, Reporting), who owns the Definition of Done
  (`templates/definition-of-done/definition-of-done_example.md:6`); Marcus Bell (Staff Engineer, Reporting) and Sam
  Okafor (Security) (`test-summary-report_example.md:8`); Sofia Marino (Design Systems) (`test-plan_example.md:84`);
  Lee Zhang (Data Eng) (`test-plan_example.md:81`); and Dana Osei (Staff Engineer, Platform)
  (`test-plan_example.md:95`, `templates/business-continuity-plan/business-continuity-plan_example.md:4`; `dim1.md`
  cites `:5`). The Definition of Done belongs to the Reporting Squad (`definition-of-done_example.md:5`).
- The release: Saved Views for Dashboards, phases 1 and 2, builds 2.3.1 and 2.3.2
  (`test-summary-report_example.md:3-4`).
- The environments: Staging, Migration sandbox, Pre-prod replica and CI (`test-plan_example.md:77-86`).

**Dates already committed, in order:** the test plan, last updated 2026-07-06 (`test-plan_example.md:6`); the
summary report, test period 2026-07-06 to 2026-07-17 and last updated 2026-07-17
(`test-summary-report_example.md:7`, `:10`); the KPI dashboard, risk register and RAID log, each last reviewed
2026-07-20 (`kpi-dashboard_example.md:6`, `risk-register_example.md:6`, `raid-log_example.md:6`); the Definition of
Done, updated 2026-07-24 (`definition-of-done_example.md:10`; `dim1.md` cites `:9`, which is its 2026-02-02
created date); and the business continuity plan, 2026-09-15 (`business-continuity-plan_example.md:6`). The spec
requires a date after 2026-07-06 and, without a stated reason, not before 2026-07-17; the window up to 2026-07-24
is one coherent placement, not a rule (`docs/internal/tier2-specs.md:6098-6106`). No sibling example mentions a
test strategy, so the example must not claim that any sibling cites it.

**Avoid:** restating any row of the test plan's Risk-Ranked Approach (`test-plan_example.md:58-73`, seven areas)
or its Test Levels and Types (`:75-86`, eight rows), and any defect row of the summary report
(`docs/internal/tier2-specs.md:6113-6120`). No shipped example read for this log names a second project inside
the program, so any other project the example names is its own fiction and should be labelled as such.

### What `test-plan_example.md` already says and names

Its only sentence about a standing strategy is the frontmatter field, which says Acme Reporting has no standing
test strategy document and that the Risk-Ranked Approach is the strategy for this release
(`templates/test-plan/test-plan_example.md:7`). It stays true at its own date and is not edited
(`docs/internal/tier2-specs.md:6084-6088`). The guide routes a reader who wants to say how the organization tests
across projects to a test strategy, marked as standing and rarely changing
(`templates/test-plan/test-plan_guide.md:36`). The test
plan names a 500ms view-list budget (`test-plan_example.md:70`), WCAG 2.2 AA (`:72`, `:84`), the CI unit and
component gate as an entry criterion (`:85`, `:93`), and the environments above. A program default that
contradicts any of these would retcon the test plan. One that restates them as rows would duplicate it.

### Neighbours

The spec's six boundaries stand (`docs/internal/tier2-specs.md:5901-5932`). The research adds one. ISTQB's master
test plan is "A test plan that is used to coordinate multiple test levels or test types." [1]. Ofgem's "programme
level Testing Management Plan" [11] is that kind of plan, sitting beneath a program strategy. A program-level plan
is a plan, and this bundle must not absorb it.

### Sentences this research contradicts or weakens

These are not landing staleness. They are already wrong or weakened. Each is a candidate edit for the landing PR,
and each is maintainer-vetoable. A decision record gets a dated note, not a silent rewrite.

- `templates/test-plan/test-plan_companion.md:379-382` and `:506` attribute the mirror's definition to ISTQB and tag
  the mirror primary. The current official definition differs [1].
- `templates/test-plan/test-plan_guide.md:41-42` says the certification bodies put strategy at the organization or
  program level. ISTQB's current glossary says "within an organization" [1], and its syllabus applies the generic
  term at any scope [4].
- `docs/internal/tier2-specs.md:5748-5756` and `:5808-5811`, and ADR 0075 (`0075-...:60-62`, `:239-241`): the
  hedge they attribute to ISTQB is the mirror's text [3].
- `docs/internal/tier2-specs.md:5959-5961` and `:5970`, and risk 4 (`:6058-6060`): only four Process Street steps
  were raw-checked. All twenty now are [13].
- `docs/internal/tier2-specs.md:6006-6013`: the owner value is `not contradicted`. QATestLab contradicts it [24].

### Sentences that go stale at landing

From `dim1.md`, with lines re-checked:

- `README.md:239`, the heading `(complete, six bundles)`; `:241`, `All six members`; `:243`, the `foundation` list,
  which names two bundles; and `:245-252`, the six-row table.
- `templates/README.md:91-97`, the standing-standards list. It also lacks `business-continuity-plan`, which is filed
  at `:106` under strategy-docs, a defect that predates this bundle.
- `STATE.md:278`, the Bundles cell: `Forty-seven bundles` and the standing-standards member list.
- `docs/internal/contracts/standing-standards.md:17-19`, the Members line's `not yet built`. This bookkeeping edit
  stops for the maintainer's read (`docs/internal/tier2-specs.md:6138-6142`).
- `templates/test-plan/test-plan_guide.md:36`, the routing row, which may gain a link as a build decision
  (`docs/internal/tier2-specs.md:6143-6144`).

**Added for this log; `dim1.md` missed them:**

- `docs/reference/choosing-a-template.md:155`, the standing-standards row of its family table.
- `AGENTS.md:61-62`: 28 bundles carry a `phase` and the other 19 a `classification`. A `foundation` member makes
  the second number 20.
- `library.json:4`: `for 43 of the 47, a full one`. A single-size bundle changes the total, not the 43.
- The bundle count is retyped across live files, among them `README.md:15`, `:146`, `:158` and `:357`,
  `AGENTS.md:27` and `:75`, `docs/how-to/installing.md:20`, `docs/reference/choosing-a-template.md:14`,
  `.claude-plugin/plugin.json:4` and `site/src/content/docs/index.mdx:6`. The landing number depends on whether
  `positioning-statement` lands first. `STATE.md` and `tools/check-counts.py` are the authority, and the landing
  sweep should grep rather than work from this list.

---

## Claims flagged contested or time-bound

1. **Living or stable.** Three camps (Finding 5): stable once approved [17], [23], [24]; living [16], [18], [20];
   stable and changed on named events [10], [14], [21]. Software Testing Help states two camps itself [17]. The
   contract's `not revised on a calendar` (`docs/internal/contracts/standing-standards.md:27-28`) fits the third.
2. **Whether a calendar cadence exists.** TestRail: "There is no universal review schedule." [20]. Edana: annual or
   semi-annual assessments [21]. Ofgem: "periodically thereafter" [10]. Edana's is one model, not a measured norm.
3. **Who owns and approves the strategy.** A role ([19], [24]), a function ([3], [20]), a committee ([21]), a board
   ([14]), or named approval authorities ([15]). No source ties a role to a committee. The catalog's QA Manager is
   supported by [20] and [3] and contradicted by [24].
4. **Which document is the parent.** The plan derives from the strategy ([23], [24]); the plan documents the
   strategy ([26]); a project's strategy lives in its plan ([4]). The library's per-project answer is the
   Risk-Ranked Approach (`templates/test-plan/test-plan_guide.md:44-45`).
5. **What "test strategy" means.** A standing organizational document ([1], [24]); a heuristic thinking tool for
   one effort ([27]); a per-iteration practice ([28]); a generic term usable at any scope ([4]).
6. **What ISO/IEC/IEEE 29119-3 calls the artefact.** "organizational test practice", per one syllabus sentence [4],
   against "Organizational Test Strategy" in every other source read [1], [6], [7], [8]. Unresolved; the standard
   was not retrieved [9].
7. **Whether imbus's two senses are one artefact or two** [7]. Its note separates them; its first sense reads as
   the organizational artefact. Unresolved.
8. **Whether a standing strategy is waterfall legacy.** Kolarov voices the shelfware critique and answers it in one
   abstract [25]; BrowserStack names overdocumenting and ignoring CI/CD as mistakes [23]. The sources agree a
   strategy can be tailored and short; none says it is unnecessary.
9. **Whether the program documents show use across more than one project** (Finding 2). They show several phases,
   parties, test phases or releases inside one program [10], [12], [14], [15]. Counting those as more than one
   project is the library's reading.
10. **Figures inside Quotable lines.** GDS's "around 30%" [43] and GOV.UK's "approximately 98%" [38] are the
    sources' own claims, with no method in this log. Quote them attributed or not at all. Neither is a prevalence
    figure for test strategies, and the ban on such figures stands.
11. **Time-bound facts.** The official glossary is live data, read on 2026-10-20 (2026-10-21 UTC) [1], so any
    citation to it carries a date. The mirror is a stale snapshot [3]. The syllabi are CTAL-TM v3.0 [4] and CTFL
    v4.0.1 [5]. Product documentation changes with the product: k6 v2.3.x [32], [33], GX Core v1.24.0 [31],
    dbt's four built-in tests [30] and Pact [35]. WCAG 2.2 is the version cited [34], [43]. GOV.UK's browser
    table [38] and its service manual pages [37], [39], [40] are living pages, and so are both Wikipedia
    articles [6], [26]. The IRS manual is the revision of 01-03-2025 [42]. Edana's article is dated 2026-01-14 by
    its URL [21]. The program documents are historical: Ofgem's papers from 2016 by their URLs [10], [11], DCC's
    v3.5 [14], TfL's schedule dated August 2009 in its raw text [12], and HNG-X from 2006 in its raw text [15].
    imbus cites the 2013 edition of 29119-1 [8].

---

## Honest framing

**What this bundle exists to say.** In this bundle's sense, a test strategy is a standing document. It sets the
default testing approach, meaning levels, types, tools, environments and governance, for every project in an
organization or program. It also sets the rule by which each project's own test plan inherits that default or
states a reasoned deviation. The sources that define or publish one agree on that shape. ISTQB's definition
speaks of "the generic requirements for testing" [1]. The program documents put the strategy above more detailed
plans [10], [11], [12], [14], [15]. The plan "explains why the testing will deviate" [5], states "reasons and
rationale for such differences" [12], or records variance as "a conscious choice" [41]. The value claimed for it
is consistency across teams: "A documented strategy helps multiple teams test in a consistent way" [18]. That is a
vendor's claim, not a measurement.

**The admission no longer leans on the word document in ISTQB's definition.** The official definition calls the
artefact "A strategy" [1]. The written-document case rests on documents published as such: Ofgem [10], DCC [14],
HNG-X [15], OPG [41], TfL's required deliverable [12] and Process Street's template [13].

**What it must not claim:**

- That ISTQB's current glossary scopes the strategy to a program, or says "one or more projects" [1], [3].
- That any sentence is ISO/IEC/IEEE 29119-3's own wording [9]. Wikipedia and imbus are secondary [6], [7], [8].
- That the rename question is settled either way [4], [9].
- That the mirror is ISTQB, or that its two entries are independently defined terms [3].
- That every organization needs a standing strategy. QATestLab folds it into the plan on a small project [24].
  ISTQB recommends documenting a strategy "but not necessarily in the form of a formal test plan" [4]. The
  `test-plan` guide calls the Risk-Ranked Approach a legitimate answer where no strategy exists
  (`templates/test-plan/test-plan_guide.md:43-45`).
- That the plan-versus-strategy boundary is settled [23], [24], [26].
- Any prevalence statistic, including the unsourced 42-percent figure `test-plan` already excluded
  (`templates/test-plan/test-plan_companion.md:568`).
- That a standing strategy improves testing or outcomes. No source here measured an effect. GDS's 30% figure [43]
  concerns automated accessibility testing, not strategies.
- That a calendar cadence is standard practice [20], [21].
- That the HNG-X document is a model of practice [15]. It is cited for its shape.
- That anything here supports a portfolio scope. No source in this log uses the word.
- That the per-project sense is this bundle's subject. `test-plan` covers it.

**Spelling.** Program, in the library's own voice. The British spelling appears only inside quotations, including
quoted document titles.

---

## Notes for the companion

**The load-bearing sections.** Four of the skeleton's 11 sections (`templates/methodology.md:172-182`) carry this
bundle. **Origins** must tell the ISTQB story straight: the current official definition [1], the mirror's older
text [3], the open rename [4], and the secondary 29119 accounts [6], [7], [8]. **Debates** must name the camps of
Findings 5 to 7 and recommend without flattening. **Relationships** must place the strategy above `test-plan`
through `test_strategy_ref`, beside `definition-of-done`, and apart from a master test plan [1]. **Anatomy** must
carry the inheritance section and the Review Trigger, the two sections where this bundle's content is its own:
`test-plan` holds the per-project levels and risks, and no sibling sets a testing default for other projects.

**The sharpest teaching points.**

1. **The strategy sets defaults; the plan states deviations, with reasons** [5], [12], [41].
2. **Generic in the strategy, detailed in the plan.** Ofgem leaves "the detailed testing approach for each test
   phase, entry and exit criteria, detailed roles and responsibilities, reporting arrangements, etc." to its plan
   [10].
3. **Name what it does not cover.** DCC lists out-of-scope items [14]; HNG-X names the release trains it excludes
   [15].
4. **More than one strategy can be right.** imbus: "An organisation could have more than one Organizational Test
   Strategy to cover markedly different project contexts." [8]. HNG-X sits beside separate strategies for other
   release trains [15].
5. **Keep it short.** Kolarov's 40-page image [25]; BrowserStack's "Overdocumenting Everything" [23]; HNG-X keeps
   detail out, since "it is not intended to expand this document to define the detailed testing coverage and
   methods required" [15].
6. **Stable, and changed on a named event** (Finding 5's third camp), with any periodic review as a floor, as the
   contract's change note reads it (`docs/internal/contracts/standing-standards.md:202-207`).
7. **A blank where an obligation sits** is a failure mode a template can prevent by asking [41], [43].

**Section design, as the research moves it.** Every proposed section, field or prompt below is a **candidate**
under decision procedure 12 (`docs/internal/decision-procedures.md:207-241`). None is an obligation, and this log
admits none. E1 means sourced, E2 labelled as the library's own with a falsifier, E3 homed and E4 sized for lean.

- **Purpose and Scope** stands, and already asks which projects the strategy binds. *Candidate ASK:* what it
  excludes, by name, such as other release trains or out-of-scope items. E1 [14], [15]; E3 here; E4 lean.
- **Test Levels and Types** stands. *Candidate ROW HINT:* mark a type mandatory by an external obligation and name
  the obligation. E1 [42], [43]; E3 here; E4 lean. *Candidate:* a standing regression rule. E1 [41]; E3 here.
  Source any named level list to the mirror's illustration [3], labelled, or to Vocke [29]; no standards-tier
  Quotable line names the four classic levels. Never restate `test-plan`'s rows.
- **Standard Tooling and Environments** stands, now sourced by the Process Street step "Establish test environment
  and tools requirements" [13] and DCC's test data and environments heading, read in raw text [14]. *Candidate:* a
  rule for personal or production data in test. E1 [42], with [36] as regulator guidance; E3 here; E4 lean.
- **Governance and Policy Alignment** stands. Policy alignment rests on imbus's secondary account [7], [8] and
  ISTQB's policy definition [1]. *Candidate:* the metrics every project reports. E1 [41], [42], [21]. E3: here
  rather than in a `kpi-dashboard`, which displays metrics and does not oblige projects to report them; E4 lean if
  the list is short.
- **How Project Test Plans Inherit or Deviate** stands and is better sourced than the spec knew: [3], [5], [12],
  [41]. *Candidate:* generic entry and exit criteria as program defaults. E1 from [13], [24] and three published
  strategies read in raw text [10], [12], [14]. E3: per-release criteria already live in `test-plan`'s Entry and
  Exit Criteria (`templates/test-plan/test-plan_example.md:88-99`), so the defaults belong here or as a Test Levels
  and Types row hint; E4 lean. *Candidate:* a named approver for a deviation. It fails E1 as stated: its one
  source is a directive [42], and OPG's published strategy records variance without naming an approver [41].
  Under E2 it would need the library's own argument and a falsifier, which this log does not supply. This log
  recommends an ASK on who may accept a deviation, not a required approver field.
- **Roles and Responsibilities Across Projects** stands, and recurs in all four published documents (Finding 3).
  The guidance should show the owner disagreement (Finding 4) rather than pick a winner.
- **Review Trigger** is contract-mandated, as a table of condition, owner and action
  (`docs/internal/tier2-specs.md:5934-5942`). Source each condition as Finding 6 maps it, and label the synthesized
  ones. The owner column is the contract's own obligation, since no source names who notices.
- **Not in the spec's table, and proposed as candidates:** document control (version, approver, effective date and
  review history) in frontmatter, E1 [13], [14], [15], [21], E3 frontmatter, E4 lean; and a short shared glossary,
  E1 [41], [15], with DCC's terminology section read in raw text [14], E3 Purpose and Scope, E4 lean only if short.
- **Proposed for decline or routing:** a risk section, since specific risks belong in `test-plan`'s Risk-Ranked
  Approach and in `risk-register`, though Process Street [13] and HNG-X [15] carry one; deliverables, which belong
  with the qa-docs family, so at most a row hint; defect management, which belongs in `bug-report`; and
  traceability, which rests on one source [42] and belongs in `test-plan` and `test-case`.

**Size.** Single size stands. No source describes a short form and a long form of one template. Kolarov's range,
"a collection of few stickers on the wall" to "quite long document(s)" [25], is evidence of variety, not of two
sizes. QATestLab's small-project case folds the strategy into the plan [24], which is `test-plan`'s territory.

**Aliases.** *Add* `organizational test strategy`, ISTQB's own term [1]. *Remove* `test approach` here: ISTQB
defines it as a separate term [1], CTAL-TM uses it at plan level [4], and DCC puts Test Approach documents beneath
its strategy [14]. That adds evidence for the spec's correction 3 (`docs/internal/tier2-specs.md:5991-5998`).
`QA strategy` still has no Quotable line. *Never alias* `master test plan`, which ISTQB defines as a plan [1].
*Candidate alias:* `testing strategy`, the word several sources use [10], [15], [16], [18].

**The example.** A program-level standing strategy for Reporting Platform Modernization, owned by Anjali Rao and
approved by Marta Reyes or the program steering group, dated in the spec's window
(`docs/internal/tier2-specs.md:6080-6120`). It may set program defaults from Finding 9: data tests [30], [31],
load tests [32], [33], [40], contract tests [35], accessibility at WCAG 2.2 AA [43], an environment ladder
consistent with the thread's names [37], and a test-data rule [36], [42]. It may point at the summary report as
the motivating event, by pointer only. Any second project is its own fiction. **It must not assert** the k6
type names as quotations [32], the contrast criterion's number or level [34], a UK legal duty as binding on Acme
[43], any price, any prevalence figure, or anything a sibling's rows already state.

**The traps.**

- Quoting the mirror as ISTQB, or writing "one or more projects" as ISTQB's words [1], [3].
- Presenting Wikipedia or imbus as the standard [6], [7], [8].
- Presenting imbus's content list [7] as the organizational strategy's contents; it sits on the entry that imbus
  separates from the organizational artefact.
- Quoting any span listed above as not a Quotable line: Ofgem's control fields, DCC's tables and headings, TfL's
  lettered contents, the k6 names, the HNG-X approvers.
- Copying Process Street's steps verbatim into the template; no licence is stated [13].
- Citing HNG-X as good practice [15].
- Quoting GDS's 30% or GOV.UK's 98% as facts rather than attributed claims [38], [43].
- Writing the British spelling in the library's own voice, or scoping anything to a portfolio.
- GOOD and WEAK text that reuses the example's scenario. Before review, grep the drafted template for Reporting
  Platform Modernization, Saved Views, Acme, Anjali Rao, Marta Reyes, dbt, Great Expectations, k6, Pact and the
  example's own project names (`docs/internal/tier2-specs.md:6071-6073`).
- Restating `test-plan`'s Test Levels and Types or Risk-Ranked Approach (`docs/internal/tier2-specs.md:6064-6066`).

## Sources

### CANON: ISTQB'S GLOSSARY AND SYLLABI, AND SECONDARY ACCOUNTS OF ISO/IEC/IEEE 29119

**[1] ISTQB (International Software Testing Qualifications Board) - Official Glossary, live data endpoint.** standards. **fetched-and-verified.**
`https://api.glossary.istqb.org/v1/terms`
Supports: The current, official ISTQB glossary definitions of 'test strategy', 'organizational test strategy', 'test policy', 'test approach', 'test plan', and 'master test plan', as served live by the backing JSON API of glossary.istqb.org (the glossary.istqb.org page itself is a JavaScript single-page app whose server-rendered HTML is an empty shell - confirmed separately below - so this API, found by inspecting the page's bundled JavaScript for its fetch target, is the only way to read the official glossary's raw text; nothing here is a summary)
Quotable: "A strategy that describes the generic requirements for testing and how to perform testing within an organization."
Quotable: "High-level documentation describing the principles, approach and major objectives of the organization regarding testing."
Quotable: "A description of how to perform testing to reach test objectives under given circumstances."
Quotable: "The manner of implementing test tasks."
Quotable: "Documentation that describes test objectives, means and schedule for achieving test coordination."
Quotable: "A test plan that is used to coordinate multiple test levels or test types."

**[2] ISTQB Glossary, official rendering page (glossary.istqb.org).** standards. **fetched-and-verified.**
`https://glossary.istqb.org/en_GB/search?term=test+strategy`
Supports: Confirms the official glossary page itself returns an empty HTML shell (<div id="root"></div> plus module script tags) with no server-rendered term text - it is a client-side single-page app, consistent with the 2026-10-14 critic's finding that every automated fetch of ISO sites hit a JS-rendered empty page. I located and read the page's actual content by finding its backing API call (https://api.glossary.istqb.org/v1) inside its bundled JavaScript (index.21d8c286.js) and querying that endpoint directly (see the api.glossary.istqb.org/v1/terms entry above)

**[3] istqb-glossary.page (unofficial ISTQB glossary mirror) - "Test Strategy" and "Organizational Test Strategy" entries.** reference (mirror). **fetched-and-verified.**
`https://istqb-glossary.page/test-strategy/`
Supports: The mirror's current definition text for 'test strategy' and 'organizational test strategy' (identical on both pages), to compare against the official glossary's current text pulled from api.glossary.istqb.org above
Quotable: "A high-level description of the test levels to be performed and the testing within those levels for an organization or programme (one or more projects)."
Quotable: "An organization that develops and maintains an e-commerce platform defines a test strategy stating that all projects will perform component, integration, system, and acceptance testing; that regression testing is automated and runs on every build; and that risk-based testing guides where effort is invested. Each project then writes a test plan that applies this strategy to its own scope, schedule, and resources."
Quotable: "Who owns the test strategy? Typically the organization's test management or QA function. Because it spans multiple projects, it is agreed at the organizational or programme level."
Quotable: "Can a project deviate from the strategy? Yes, with justification. The test plan records the rationale for any deviation, such as skipping a level for a small maintenance release."

**[4] ISTQB - Certified Tester Advanced Level Test Management (CTAL-TM) Syllabus, Version 3.0.** standards. **fetched-and-verified.**
`https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TM_Syllabus_v3.0_zKjKsaN.pdf`
Supports: How ISTQB's current syllabus relates test policy, organizational test strategy, project test strategy, and ISO/IEC/IEEE 29119-3's own terminology; the rename question (part e)
Quotable: "Throughout this syllabus, the organizational test strategy is taken as given. The development and maintenance of an organizational test strategy is considered in the context of ISO/IEC/IEEE 29119-3 (where it is referred to as an "organizational test practice") and the syllabi for the ISTQB® Expert Level Test Management, and the ISTQB® Certified Tester Agile Test Leadership at Scale."
Quotable: "If an organizational test strategy does not exist or does not cover the required aspects, test management must seek to clarify the missing details with the relevant stakeholders."
Quotable: "In the context of this section the definition of a project test strategy is an example of any type of a detailed test strategy for a project, a release, a product, or any other type of system development or acquisition initiative. A project test strategy (referred to as a "test strategy" in the ISO/IEC/IEEE 29119-3) describes the approach to testing in a specific context so that the organization's objectives can be met, particularly those relating to product quality and test activities."
Quotable: "The project test strategy is the main outcome of the test planning for a project and is typically documented in a test plan or as part of other documents. Documentation of the test strategy is recommended, but not necessarily in the form of a formal test plan."
Quotable: "The generic term "test strategy" can be used in any context (project, organization, product)."
Quotable: "An important point about the perspective that the syllabus provides is the fact that it focuses on test management at the project level and not test management at the organizational level."
Quotable: "Understanding the context of the organization (e.g., the test policy and the organizational test strategy), the scope of the test, and the test item ... is critical to test planning."
Quotable: "Based on the organizational test strategy, regulatory standards, any constraints given by the project, and the risk treatment approaches, the test approach is defined for the current scope of testing (see Section 1.4, The Project Test Strategy)."
Quotable: "According to this syllabus and the Glossary, a test strategy is a description of how testing will be performed in order to achieve test objectives under given circumstances."
Quotable: "A test strategy defines the overall scope, approach, and resources for testing a system or a product."
Quotable: "It is typically documented in a test plan or as part of other documents, depending on the context of the testing."

**[5] ISTQB - Certified Tester Foundation Level (CTFL) Syllabus, Version 4.0.1.** standards. **fetched-and-verified.**
`https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf`
Supports: What a test plan contains relative to test policy and test strategy, the deviation language, and a confirmed glossary terminology change from the Foundation syllabus's own change log (part e evidence)
Quotable: "A test plan: ... Demonstrates that testing will adhere to the existing test policy and test strategy (or explains why the testing will deviate from them)"
Quotable: "Test approach (e.g., test levels, test types, test techniques, test deliverables, entry criteria and exit criteria, independence of testing, metrics to be collected, test data requirements, test environment requirements, deviations from the test policy and test strategy) • Budget and schedule More details about the test plan and its content can be found in the ISO/IEC/IEEE 29119-3 standard."
Quotable: "organizational test policy -> test policy"
Quotable: "Three keywords added (test process and traceability in Chapter 1, test strategy in Chapter 5)"

**[6] Wikipedia - "ISO/IEC 29119" article.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/ISO/IEC_29119`
Supports: A secondary (non-ISTQB, non-ISO-primary) account of how 29119-3 structures Test Policy, Organizational Test Strategy, and Test Plan (including a Test Strategy) as separate documents (parts b, c, d) - labeled secondary throughout per the task's instruction, since the standard's own clause text was never reached
Quotable: "Part 2 defines a generic test process model for software testing that is intended for use by organizations when performing software testing. It comprises test process descriptions that define the software testing processes at the organizational level, test management (project) level, and dynamic test process levels"
Quotable: "Organizational Test Strategy"
Quotable: "Test Management Process Documentation"
Quotable: "Test Plan (including a Test Strategy)"
Quotable: "Dynamic Test Process Documentation"
Quotable: "Test Design Specification"
Quotable: "Test Case Specification"
Quotable: "Test Procedure Specification"

**[7] imbus - Glossary of software testing terms, "test strategy" entry.** vendor. **fetched-and-verified.**
`https://www.imbus.de/en/glossar/term/test-strategy`
Supports: A secondary (vendor) account of ISO 29119's two senses of 'test strategy' and its contrast with 'Organizational Test Strategy' (parts c, d), labeled secondary since it cites '[Reference: After ISO 29119]' rather than being the standard itself
Quotable: "1. Documentation aligned with the test policy that describes the generic requirements for testing and details how to perform testing within an organization. [Reference: After ISO 29119]"
Quotable: "2. part of the Test Plan that describes the approach to testing for a specific test project or test sub-process or sub-processes"
Quotable: "NOTE1: The test strategy is a distinct entity from the Organizational Test Strategy."
Quotable: "NOTE2: The test strategy usually describes some or all of the following; the test practices used; the test sub-processes to be implemented; the retesting and regression testing to be employed; the test design techniques and corresponding test completion criteria to be used; test data; test environment and testing tool requirements; and expectations for test deliverables."
Quotable: "Documentation aligned with the test policy that describes the generic requirements for testing and details how to perform testing within an organization. [Reference: After ISO 29119]"
Quotable: "part of the Test Plan that describes the approach to testing for a specific test project or test sub-process or sub-processes"

**[8] imbus - Glossary of software testing terms, "Organizational Test Strategy" entry.** vendor. **fetched-and-verified.**
`https://www.imbus.de/en/glossar/term/Organizational-Test-Strategy`
Supports: A secondary (vendor) account of the organizational-level artefact, explicitly cited to the 2013 edition of the standard (part c, d), labeled secondary
Quotable: "document that expresses the generic requirements for the testing to be performed on all the projects run within the organization; it provides detail on how the testing is to be performed. It is aligned with the Organizational Test Policy"
Quotable: "NOTE: An organisation could have more than one Organizational Test Strategy to cover markedly different project contexts."
Quotable: "ISO/IEC/IEEE 29119-1:2013-09"

**[9] ISO - Online Browsing Platform, ISO/IEC/IEEE 29119-3 preview.** primary. **not-retrieved.**
`https://www.iso.org/obp/ui/#iso:std:iso-iec-ieee:29119:-3:ed-2:v1:en`
Supports: Attempted, once, to reach the standard's own current clause text directly, per the task's instruction. The server returned HTTP 403 Forbidden with no body retrieved. This is recorded as a gap, not filled with any reconstructed or remembered text: no ISO/IEC/IEEE 29119 clause text appears anywhere in this report's quotable fields

### STRUCTURE: PUBLISHED PROGRAM AND ORGANIZATION TEST STRATEGIES

**[10] Ofgem (David Liversidge, author) - "Switching Programme Testing Strategy" (Design Authority issue paper, da_testing_strategy_da280916.pdf).** primary. **fetched-and-verified.**
`https://www.ofgem.gov.uk/sites/default/files/docs/2016/10/da_testing_strategy_da280916.pdf`
Supports: scope statement, owner/approver fields, 'followed by a more detailed plan' statement, section structure of a program-level testing strategy
Quotable: "This Testing |Strategy will be followed by a more detailed programme level Testing Management Plan which will be produced at the Detailed Level Specification (DLS) phase of the Switching Programme and will define the detailed approach to be taken, entry and exit criteria and individual roles and responsibilities for each test phase outlined in this strategy."
Quotable: "This Testing Strategy needs to be an enduring document for use within the programme by all parties. It should be updated again in DLS and periodically thereafter to ensure continued relevance."
Quotable: "This testing strategy forms part of the Delivery Strategy workstream within the Blueprint Phase of the Switching Programme."
Quotable: "a detailed, programme level Testing Management Plan should be developed during DLS to define the detailed testing approach for each test phase, entry and exit criteria, detailed roles and responsibilities, reporting arrangements, etc."

**[11] Ofgem (David Liversidge, author; James Crump, issue owner) - "Switching Programme Testing Strategy" (second Ofgem document, ds_testing_strategy_final_product_blueprint_phase_edag.pdf - the earlier-stage draft-control-sheet version of the same paper).** primary. **fetched-and-verified.**
`https://www.ofgem.gov.uk/system/files/docs/2016/09/ds_testing_strategy_final_product_blueprint_phase_edag.pdf`
Supports: confirms the same scope/owner/'followed by' content appears across both Ofgem documents (near-duplicate drafts of the same paper at different approval stages, not two independently structured documents)
Quotable: "This testing strategy will be followed by a more detailed programme level Testing Management Plan which will be produced at the DLS phase of the Switching Programme and will define the detailed approach to be taken, entry and exit criteria and individual roles and responsibilities for each test phase outlined in this strategy."

**[12] Transport for London - "Schedule 4 - Testing Regime" (London Cycle Hire Service Agreement, redacted contract schedule).** primary. **fetched-and-verified.**
`https://content.tfl.gov.uk/lchs-schedule4-testing-regime-redacted.pdf`
Supports: section structure and the contents-list form of a 'Test Strategy' clause inside a procurement schedule; shows the strategy is a deliverable the Service Provider must produce and TTL approves, sitting above Test Plans/Test Specifications
Quotable: "3.1 The Service Provider shall, in accordance with Schedule 3 (Milestones and Deliverables), prepare and submit to TTL a Test Strategy."
Quotable: "(D) any specific Testing requirements or objectives where this differs from the Test Strategy, together with the reasons and rationale for such differences;"
Quotable: "(D) any specific Testing requirements or objectives where this differs from the Test Strategy, together with the reasons and rationale for such differences"

**[13] Process Street - "Test Strategy Document Template".** vendor. **fetched-and-verified.**
`https://www.process.st/templates/test-strategy-document-template/`
Supports: all 20 of the template's steps, verbatim and in order (reported in full below per the task's instruction, since the earlier research raw-checked only four of them)
Quotable: "Identify objectives of the test strategy document"
Quotable: "Determine target audience for the document"
Quotable: "Outline scope of the tests"
Quotable: "Identify necessary test levels"
Quotable: "Identify types of testing to be performed"
Quotable: "Select test techniques"
Quotable: "Establish test environment and tools requirements"
Quotable: "Approval: Test Environment Specifications"
Quotable: "Determine resource requirements"
Quotable: "Define test deliverables"
Quotable: "Develop test schedule and estimation"
Quotable: "Identify test entry and exit criteria"
Quotable: "Identify risks and dependencies"
Quotable: "Develop risk mitigation strategy"
Quotable: "Approval: Risk Mitigation Strategy"
Quotable: "Compile all information into the test strategy document"
Quotable: "Conduct initial review of test strategy document"
Quotable: "Approval: Test Strategy Document"
Quotable: "Revise and finalize test strategy document based on feedback"
Quotable: "Distribute finalized test strategy document to relevant stakeholders"

**[14] DCC (Dave Norman, author) - "Smart Metering Implementation Programme Joint Test Strategy" v3.5.** primary. **fetched-and-verified.**
`https://www.smartdcc.co.uk/media/1091/joint_test_strategy_v35.pdf`
Supports: a second, independently structured, publicly published UK program-level test strategy - full section headings, scope/out-of-scope statement, owner/approver/version detail, and the 'further elaborated in Test Approach and Test Plan documents' relationship statement
Quotable: "This document sets out how the DSP (CGI), the CSPs (Arqiva and Telefonica) and all other Service Providers (e.g. BT, Critical Software Solutions, Capita IT ES) will conduct testing for the Smart Metering Implementation Programme."
Quotable: "The testing described in this document will be further elaborated in the Test Approach and Test Plan documents shown on the diagram."
Quotable: "The DSP will keep this document up to date. Each new version supersedes the previous version in its entirety."
Quotable: "The document will be updated with relevant review comments and then issued to the DCC Licensee's Design Assurance Board (DAB) for approval."
Quotable: "The DCC Licensee will publish the DAB-approved version of this document on its website."
Quotable: "This document is primarily for internal DCC consumption but published online for the purposes of transparency and clarity of the DCC testing strategy."
Quotable: "Certification of Comms Hubs"
Quotable: "testing of Meter Device Models other than..."
Quotable: "2.3 27/02/14 M Roderick DCC Design & Assurance Director"

**[15] Fujitsu Services Ltd / Post Office Ltd (joint document) - "HNG-X Testing Strategy" TST/GEN/STG/0001 v1.0, disclosed as evidence FUJ00232570 to the UK Post Office Horizon IT Inquiry.** primary. **fetched-and-verified.**
`https://postofficeinquiry.dracos.co.uk/projects/evidence/FUJ00232570/`
Supports: a third, independently structured program-scope test strategy, this one with an explicit joint-organization scope boundary (a named programme, explicitly excluding both the preceding and the following release trains) and a named subordinate-document relationship (High Level Test Plans, Low Level Test Scripts)
Quotable: "This is a joint Fujitsu Services/Post Office document describing the strategic approach to be applied for all testing and integration activities performed for the HNG-X Programme."
Quotable: "This strategy covers all the testing and integration activities required across the whole HNG-X programme, for both Fujitsu Services and Post Office Limited. It spans from initial involvement in the Requirement Analysis stage, through Design and Build, up to and including pre-Live Operational Proving, and also covers the testing and integration of the XP release"
Quotable: "It is not concerned with the testing and integration required for the succession of Horizon releases continuing in parallel with and in preparation for the HNG-X programme - this will be covered in separate testing strategy documents specific to those Horizon releases."
Quotable: "Similarly, it is not concerned with the ongoing testing and integration of the HNG-X solution to take place for possible future releases following the completion of the HNG-X programme. Again, that will be covered in separate documents."
Quotable: "it is not intended to expand this document to define the detailed testing coverage and methods required. Such material (aimed at a much narrower audience) should be defined separately in a series of subordinate documents"
Quotable: "0.0 Document Control"
Quotable: "0.1 Document History"
Quotable: "0.2 Review Details"
Quotable: "0.4 Abbreviations/Definitions"
Quotable: "1.0 Introduction"
Quotable: "1.2 Purpose of Document"
Quotable: "1.4 Context"
Quotable: "2.0 Rationale & Outline Approach"
Quotable: "2.2 Implications for Testing & Integration"
Quotable: "3.0 Goals & Objectives"
Quotable: "4.0 Strategic Approach"
Quotable: "4.1 Objective Driven Testing"
Quotable: "5.0 Testing Coverage"
Quotable: "6.0 People, Skills & Responsibilities"
Quotable: "7.0 Assumptions, Dependencies, Risks & Constraints"
Quotable: "7.2 Dependencies"
Quotable: "7.3 Risks"
Quotable: "7.4 Constraints"
Quotable: "This is a joint Fujitsu Services/Post Office document"
Quotable: "describing the strategic approach to be applied for all testing"
Quotable: "Whole HNG-X Programme"
Quotable: "Approval Authorities"

### GOVERNANCE, INHERITANCE AND CADENCE

**[16] ReqTest (vendor knowledgebase), "Test Documentation in Agile Projects".** vendor. **fetched-and-verified.**
`https://reqtest.com/en/knowledgebase/test-documentation-in-agile-projects/`
Supports: (a) relationship between a test strategy and per-sprint test plans; (b) the 'living document' camp
Quotable: "The test strategy is a living document and evolves over time"
Quotable: "it is highly advisable to supplement it with a testing strategy"
Quotable: "A test strategy that describes how the system is usually tested."

**[17] Software Testing Help, "Difference Between Test Plan, Test Strategy, Test Case, Test Script, Test Scenario And Test Condition".** practitioner. **fetched-and-verified.**
`https://www.softwaretestinghelp.com/difference-between-test-plan-test-strategy-test-case-test-script-test-scenario-and-test-condition/`
Supports: (b) both camps named in the same article's own text, plus the audience the strategy is intended for
Quotable: "Test plan will change over the course of the project. Test strategy usually will not change once approved."
Quotable: "The test strategy document is a living document and will be updated** when we get more clarity on requirements, SLA parameters, test environment build management approach, etc."
Quotable: "** Some people believe that once defined, the test strategy should never be changed. Testing projects generally undergo updates as the project advances."
Quotable: "Test strategy is intended for the complete project team that comprises Project Sponsors, Business SMEs, Application/ Integration Development, System Integration Partners, Data Conversion Teams, Build/Release Management Teams such as technical leads, architecture leads, and deployment and infrastructure teams."

**[18] Tricentis, "Software Test Strategy" (Learn resource page).** vendor. **fetched-and-verified.**
`https://www.tricentis.com/learn/software-test-strategy`
Supports: (b) living-document camp; context for standardizing practices across teams
Quotable: "A good testing strategy isn't static. It evolves with your product, incorporates feedback from past releases, and continuously improves based on outcomes."
Quotable: "Keep documentation living: Update your strategy as systems evolve and priorities shift."
Quotable: "Standardizing practices across teams: A documented strategy helps multiple teams test in a consistent way, even across distributed geographies."

**[19] SoftTest Pays Pty Ltd (recruiter) job posting for "Program Test Manager" (Canberra, ACT).** practitioner. **fetched-and-verified.**
`https://careers-page.com/softtest-pays-pty-ltd/job/L688Y59W`
Supports: (d) the named individual role that manages, defines, approves and plans the Test Strategy artefact at program scope
Quotable: "Program Test Manager"
Quotable: "Manage, define, approve and plan test artefacts using appropriate tools, not limited to Test Estimation, Test Schedule, Test Strategy, Test Plan, Test Execution Reports, Defect Modelling Reports, and Test Summary Reports."
Quotable: "Manage program testing activities that are correctly prioritised to deliver outcomes that align to the Departments priorities."

**[20] TestRail (Idera), "Test Plan vs Test Strategy: When to Use Each".** vendor. **fetched-and-verified.**
`https://www.testrail.com/blog/test-plan-vs-test-strategy/`
Supports: The TestRail source the earlier research quoted; independently covers (a) tailoring, (b) the 'long-term document' framing alongside 'living documents', (c) named review conditions plus an explicit denial of a universal calendar, (d) roles that create/maintain vs. roles consulted
Quotable: "A long-term document that evolves with the organization's needs and growth."
Quotable: "Created and maintained by QA managers, test leaders, and strategic teams overseeing testing processes."
Quotable: "Organizational leadership and QA managers responsible for setting long-term testing strategies."
Quotable: "Test plans and strategies should be living documents, updated throughout the project lifecycle to reflect changes in requirements, priorities, and business goals."
Quotable: "The strategy should be tailored to the specific context rather than copied unchanged between projects."
Quotable: "There is no universal review schedule."
Quotable: "A strategy should be reconsidered when changes to the product, architecture, risks, technology, development model, regulations, or organizational objectives make the existing approach less appropriate."
Quotable: "Project-level strategies may need more frequent adjustment than long-lived organizational guidance."

**[21] Edana (Jonathan Massa), "Test Plan vs Software Test Strategy: Structure, Objectives and Key Differences Explained".** practitioner. **fetched-and-verified.**
`https://edana.ch/en/2026/01/14/test-plan-vs-software-test-strategy-structure-objectives-and-key-differences-explained/`
Supports: A second named tailoring/deviation source: (a) the formalize-then-tailor flow and who approves what, (c) a named calendar cadence and named trigger condition, (d) the governing body versus the plan's author/approver
Quotable: "Solution: formalize the organizational testing strategy → tailor a project-specific test plan → centralize tracking and KPIs in a common repository."
Quotable: "The project manager approves the plan in terms of budget and timeline. The QA team implements and updates it, while IT may validate infrastructure needs and access to test environments."
Quotable: "As a stable, long-term document, it is updated when major changes occur in technology, tools or team maturity."
Quotable: "It also defines governance (steering committee, involved roles, review cycles) and performance indicators to evaluate testing effectiveness across the enterprise."
Quotable: "In contrast, the strategy applies continuously, changing only during major QA process or tool revisions."
Quotable: "The strategy is overseen by a QA board or a cross-functional committee including IT, business and architecture representatives."
Quotable: "The strategy, by contrast, is reviewed during annual or semi-annual assessments, incorporating lessons learned, technological innovations and regulatory updates."
Quotable: "A configuration management process ensures each strategy version is approved by the QA committee and distributed to project teams."
Quotable: "A QA committee or a cross-functional body (IT department, business units, architecture) oversees the test strategy. The test lead, in collaboration with the project manager, developers, and business analysts, writes and updates the test plan."

**[22] Playcode.io blog, "Test Plan vs Test Strategy" (in substance, a test-case-template guide).** vendor. **fetched-and-verified.**
`https://playcode.io/blog/test-plan-vs-test-strategy`
Supports: Checked as a candidate second tailoring/deviation source on a WebSearch lead; read in full and found NOT to support the deviation-approval/exception claim the search summary implied
Quotable: "Test-strategy objectives, risk model, coverage-selection rules, automation policy, environment and data policy, evidence policy, governance, or cross-release exceptions"

### DEBATES AND FAILURE MODES

**[23] BrowserStack (vendor guide) - "Test Plan vs Test Strategy: Purpose & Differences".** vendor. **fetched-and-verified.**
`https://www.browserstack.com/guide/test-plan-vs-test-strategy`
Supports: Where the plan/strategy line is drawn (scope, ownership, stability); a named list of failure modes for standing test documentation
Quotable: "A test plan is a detailed document that defines how testing will be executed for a specific project, release, feature, or sprint."
Quotable: "A test strategy is a high-level document that defines the overall testing approach, objectives, standards, and methodologies followed throughout the software testing lifecycle."
Quotable: "Unlike a test plan, a test strategy is broader in scope and usually remains stable across multiple projects or releases."
Quotable: "Test Strategy"
Quotable: "Dependency"
Quotable: "Independent of individual projects ... Test Plan"
Quotable: "Derived from the test strategy"
Quotable: "Treating Both Documents as the Same: Using test plan and test strategy interchangeably creates confusion around testing scope, execution, and ownership."
Quotable: "Overdocumenting Everything: Excessively detailed documents increase maintenance effort and are rarely followed during actual testing."
Quotable: "Not Updating Documentation: Outdated test plans and strategies can lead to incorrect test coverage, missed risks, and execution gaps."
Quotable: "Missing Clear Ownership: Without defined ownership, testing responsibilities and reporting processes become inconsistent across teams."
Quotable: "Ignoring Agile and CI/CD Workflows: Static documentation often fails to keep pace with rapid release cycles and continuous testing practices."
Quotable: "Prioritizing Documentation Over Execution: Test documents are effective only when they actively support testing, risk management, and release validation."
Quotable: "In larger environments, teams often keep test strategies relatively stable while updating test plans more frequently for individual releases, sprints, or projects."
Quotable: "Independent of individual projects"

**[24] QATestLab (vendor knowledge center) - "Difference between Test Plan and Test Strategy".** vendor. **fetched-and-verified.**
`https://qatestlab.com/resources/knowledge-center/test-plan-vs-strategy/`
Supports: The organization-level, standing-document meaning of 'test strategy' (ISTQB-aligned camp), including who authors it and how it relates to a test plan
Quotable: "Test Plan and Test Strategy are documentation used for the arrangement and execution of QA (Quality Assurance) activities. These documents are not similar ones, but they are interrelated."
Quotable: "Test Strategy can be a part of the Test Plan if a project is small."
Quotable: "Test Strategy is high-level test documentation. Its main purpose is to describe how to conduct testing activities."
Quotable: "But in the majority of cases, it is developed at the level of the whole company, and it can be used for different projects. Test Strategy is a static long-term plan. It specifies general approaches of the company to software testing. Project Manager prepares Test Strategy."
Quotable: "Test Strategy includes the section about entry criteria that predefine what activities should be done before the start of testing. It also specifies exit criteria that define when to stop testing."
Quotable: "Test Plan defines what steps should be done in order to ensure proper quality assessment and to reach the testing goals."

**[25] Mirjana Kolarov (Test Architect / Test Department Manager, LeviNine), via Agile Testing Days 2019 session page - "Test Strategy - waterfall legacy or game changer in Agile".** practitioner. **fetched-and-verified.**
`https://agiletestingdays.com/2019/session/test-strategy-waterfall-legacy-or-game-changer-in-agile/`
Supports: The agile critique of a standing test strategy document as waterfall-legacy shelfware, and the same source's own reply to that critique (strategy still needed, but tailored and lightweight)
Quotable: "What is the first thing you think about when someone mentions Test Strategy? A big document of 40+ pages with ton of theory, no one reads and is not up to date. Usually it represent those big Waterfall projects, where you first needed to write a Test Strategy and then start with tests cases and later with testing."
Quotable: "each Agile project needs Test Strategy as a guidance how testing is done. It provides common understanding of testing processes, deliveries and expectations."
Quotable: "why it must be tailor-made, because one strategy cannot fit all"
Quotable: "Some of those Strategies were just a collection of few stickers on the wall and some were represented as quite long document(s)."
Quotable: "Why you cannot have a template and just fill it in?"

**[26] Wikipedia contributors - "Test plan".** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Test_plan`
Supports: A plan/strategy boundary statement from a general reference source, and confirmation that the two documents share the same three structural elements (coverage, methods, responsibilities)
Quotable: "A test plan is a document detailing the objectives, resources, and processes for a specific test session for a software or hardware product."
Quotable: "A test plan documents the strategy that will be used to verify and ensure that a product or system meets its design specifications and other requirements."
Quotable: "There are three major elements that should be described in the test plan: test coverage, test methods, and test responsibilities. These are also used in a formal test strategy."
Quotable: "A complex system may have a high-level test plan to address the overall requirements and supporting test plans to address the design details of subsystems and components."
Quotable: "Test plan document formats can be as varied as the products and organizations to which they apply."

**[27] James Bach (Satisfice, Inc.) - "Heuristic Test Strategy Model" download page.** practitioner. **fetched-and-verified.**
`https://www.satisfice.com/download/heuristic-test-strategy-model`
Supports: The context-driven school's per-project, heuristic sense of 'test strategy' (thinking tool for one test effort, not a standing org-level document), establishing the ambiguity named in question (c)
Quotable: "The HTSM (v.6.3) is a set of guideword heuristics designed to help you think better about test strategy. It includes four focus areas: test techniques, project elements, product factors, and quality criteria categories."
Quotable: "You can use it casually or rigorously. It is pretty generic to any kind of software. I'd encourage you to modify this to fit the context of your own organization."

**[28] Lisa Crispin (Pivotal Labs), via TechTarget IT Infrastructure - "Agile testing quadrants: Guiding managers and teams in test strategies".** practitioner. **fetched-and-verified.**
`https://www.techtarget.com/it-infrastructure/tip/Agile-testing-quadrants-Guiding-managers-and-teams-in-test-strategies`
Supports: Crispin and Gregory's agile testing quadrants as a frame for building a test strategy iteration-by-iteration rather than as one fixed standing document; the quadrants' origin and non-sequential use
Quotable: "Agile expert Lisa Crispin explains the four Agile testing quadrants and how they can guide managers and development teams in creating a test strategy."
Quotable: "The quadrants originated with Brian Marick's original posts on his Agile testing matrix. With his permission, Janet Gregory and I adapted this into the Agile testing quadrants, which form the heart of our Agile Testing book."
Quotable: "The quadrant numbering system does not imply any order. You don't work through the quadrants from Q1 to Q4 in a Waterfall style."
Quotable: "Repeat this process as you plan each iteration. For each user story, think through the testing requirements in each quadrant."
Quotable: "The quadrants are simply a taxonomy that helps teams plan their testing."
Quotable: "Mike Cohn's Test Automation Pyramid is a good complement to help teams focus their automation efforts for maximum return on investment."

**[29] Ham Vocke (Thoughtworks), via martinfowler.com - "The Practical Test Pyramid".** practitioner. **fetched-and-verified.**
`https://martinfowler.com/articles/practical-test-pyramid.html`
Supports: The widely-cited statement of how test levels should be balanced (pyramid shape), and an explicit statement that the discipline has not settled on consistent test-type terminology; note this article never uses the term 'test strategy' itself
Quotable: "Mike Cohn's original test pyramid consists of three layers that your test suite should consist of (bottom to top): Unit Tests Service Tests User Interface Tests"
Quotable: "Write tests with different granularity The more high-level you get the fewer tests you should have"
Quotable: "Write lots of small and fast unit tests. Write some more coarse-grained tests and very few high-level tests that test your application from end to end."
Quotable: "Watch out that you don't end up with a test ice-cream cone that will be a nightmare to maintain and takes way too long to run."
Quotable: "The software development community simply hasn't managed to settle on well-defined terms around testing."
Quotable: "If you get this consistent within your team (or maybe even within your organisation) that's really all you should care about."

### EXAMPLE-DOMAIN FACTS FOR THE WORKED EXAMPLE

**[30] dbt Labs - "Data tests" (dbt Docs).** vendor. **fetched-and-verified.**
`https://docs.getdbt.com/docs/build/data-tests`
Supports: Topic 2 - testing data correctness in analytics pipelines
Quotable: "There are two ways of defining data tests in dbt:"
Quotable: "The simplest way to define a data test is by writing the exact SQL that will return failing records. We call these "singular" data tests, because they're one-off assertions usable for a single purpose."
Quotable: "generic data tests tend to be much more common-they should make up the bulk of your dbt data testing suite"
Quotable: "Out of the box, dbt ships with four generic data tests already defined: unique, not_null, accepted_values, and relationships."
Quotable: "You can use data tests to improve the integrity of the SQL in each model by making assertions about the results generated."
Quotable: "We also recommend that you test any assumptions on your source data. For example, if you believe that your payments can only be one of three payment methods, you should test that assumption regularly - a new payment method may introduce logic errors in your SQL."
Quotable: "rows where your assertion is not true; if the test returns zero rows, your assertion passes"

**[31] Great Expectations (GX) - "GX Core overview" (Introduction to GX Core, GX Docs v1.24.0).** vendor. **fetched-and-verified.**
`https://docs.greatexpectations.io/docs/core/introduction/gx_overview`
Supports: Topic 2 - testing data correctness in analytics pipelines (Great Expectations side)
Quotable: "Great Expectations (GX) is a framework for describing data using expressive tests and then validating that the data meets test criteria."
Quotable: "An Expectation is a verifiable assertion about data. Similar to assertions in traditional Python unit tests, Expectations provide a flexible, declarative language for describing expected data qualities."
Quotable: "An Expectation Suite is a collection of Expectations. Expectation Suites can be used to validate a Batch of data using multiple Expectations, streamlining the validation process."
Quotable: "A Checkpoint is the primary means for validating data in a production deployment of GX. Checkpoints enable you to run a list of Validation Definitions with shared parameters."
Quotable: "Actions provide a mechanism to integrate Checkpoints into your data pipeline infrastructure by automatically processing Validation Results."
Quotable: "This workflow, when integrated with and triggered by an orchestrator, could enable automated, scheduled data quality testing on an essential data table."

**[32] Grafana Labs - "Load test types" (k6 Documentation, v2.3.x).** vendor. **fetched-and-verified.**
`https://grafana.com/docs/k6/v2.3.x/testing-guides/test-types.md`
Supports: Topic 3 - performance/load testing of dashboard queries: the six load-test-type taxonomy and sequencing
Quotable: "Many things can go wrong when a system is under load. The system must run numerous operations simultaneously and respond to different requests from a variable number of users."
Quotable: "Start with smoke tests, then progress to higher loads and longer durations."
Quotable: "validate that your script works and that the system performs adequately under minimal load"
Quotable: "assess how your system performs under expected normal conditions"
Quotable: "assess how a system performs at its limits when load exceeds the expected average"
Quotable: "assess the reliability and performance of your system over extended periods"
Quotable: "validate the behavior and survival of your system in cases of sudden, short, and massive increases in activity"
Quotable: "gradually increase load to identify the capacity limits of the system"

**[33] Grafana Labs - "API load testing" (k6 Documentation, v2.3.x).** vendor. **fetched-and-verified.**
`https://grafana.com/docs/k6/v2.3.x/testing-guides/api-load-testing.md`
Supports: Topic 3 - performance/load testing of dashboard queries: a program-level procedure for scoping and maturing API load tests
Quotable: "An API load test generally starts with small loads on isolated components. As your testing matures, your strategy can consider how to test the API more completely."
Quotable: "When you design your API tests, first consider why you want to test the API at all"
Quotable: "Script the test. Write user flows, parameterize test data, and group URLs."
Quotable: "Assert performance and correctness. Use Checks to assert system responses and use Thresholds to ensure that the system performs within your SLOs."
Quotable: "Model and generate load. Choose the executors to correctly model the workload that's appropriate to your test goals."
Quotable: "Before you start testing, identify the components you want to test. Do you want to test a single endpoint or an entire flow?"

**[34] W3C Web Accessibility Initiative - "How to Meet WCAG (Quickref Reference)", WCAG 2.2.** standards. **fetched-and-verified.**
`https://www.w3.org/WAI/WCAG22/quickref/`
Supports: Topic 4 - accessibility testing against WCAG 2.2 Level AA
Quotable: "The visual presentation of text and images of text has a contrast ratio of at least 4.5:1, except for the following: Large Text: Large-scale text and images of large-scale text have a contrast ratio of at least 3:1"
Quotable: "Logotypes: Text that is part of a logo or brand name has no contrast requirement."
Quotable: "Levels Select all Level A only Level AA only Level AAA only"

**[35] Pact Foundation - "Introduction" (Pact Docs).** vendor. **fetched-and-verified.**
`https://docs.pact.io/`
Supports: Topic 5 - contract testing between services
Quotable: "Pact is a code-first tool for testing HTTP and message integrations using contract tests."
Quotable: "Contract tests assert that inter-application messages conform to a shared understanding that is documented in a contract."
Quotable: "Without contract testing, the only way to ensure that applications will work correctly together is by using expensive and brittle integration tests."
Quotable: "Contract testing is a technique for testing an integration point by checking each application in isolation to ensure the messages it sends or receives conform to a shared understanding that is documented in a "contract"."
Quotable: "Contract testing is immediately applicable anywhere where you have two services that need to communicate - such as an API client and a web front-end. ... contract testing really shines in an environment with many services (as is common for a microservice architecture)."
Quotable: "Pact is a code-first consumer-driven contract testing tool ... The contract is generated during the execution of the automated consumer tests. A major advantage of this pattern is that only parts of the communication that are actually used by the consumer(s) get tested. This in turn means that any provider behaviour not used by current consumers is free to change without breaking tests."
Quotable: "a Pact contract is enforced by executing a collection of test cases, each of which describes a single concrete request/response pair - Pact is, in effect, "contract by example""
Quotable: "On its own, however, it does not provide any test based assurance that the consumers are calling the provider in the correct manner, or that the provider can meet all its consumers' expectations, and hence, it is not as effective in preventing integration bugs."

**[36] Agencia Española de Protección de Datos (AEPD, the Spanish data-protection regulator) - "Personal Data Breaches: Development and Pre-Production Environments".** standards. **fetched-and-verified.**
`https://www.aepd.es/en/prensa-y-comunicacion/blog/data-breaches-development-and-pre-production-enviroments`
Supports: Topic 6 - test environments and test data, including production data in test environments under data-protection rules
Quotable: "In general, it is advisable to work in the development environment, test in the pre-production environment and finally deploy applications and services in the production environment. From a data protection point of view, this differentiation must be taken into account and the exposure of actual personal data (and/or data in production systems) in the development and testing phases should be limited due to the risk it may pose to the rights and freedoms of individuals."
Quotable: "80 In the testing phase, sampling of real personal data should be avoided, as such data cannot be used for purposes for which it was not collected and using it in testing environments may result in making personal data available to unauthorised individuals."
Quotable: "81 Where possible, artificially created test data should be used, or test data which is derived from real data so that its structure is preserved but no actual personal data is contained in it."
Quotable: "82 Where thorough and cautious analysis shows that generated test data cannot provide sufficient assurance for the validity of the tests, a comprehensive decision must be taken and documented, which defines which real data shall be used in the test, as limited as possible, the additional technical and organisational safeguards which are established in the testing environment. Special categories of data can only be used in real data testing with the explicit consent of the individuals concerned."
Quotable: "Example: In case of bugs in system operation, the use of actual personal data for code debugging should be avoided. In any case, if needed, an authorisation from the data controller needs to be obtained and both the authorisation process and the debugging actions need to be recorded and auditable. The amount of personal data used for testing should anyhow be minimised and a strict "need to know" policy applied."
Quotable: "According to the principle of data minimisation and the principle of data protection by design and by default, the use of personal data in development and pre-production environments, or any other testing environment, should be avoided where possible."
Quotable: "Although not always possible, in many cases the use of synthetic data avoids the processing of personal data in development testing."
Quotable: "The risk in the pre-production environment could be the same as the risk of processing in the production environment. However, this risk may also be higher because it is common to have additional processors in development work, to use cloud systems from different providers than in production environments, to have greater uncertainty about the reliability of the code, to carry out tests with new technologies, etc."

**[37] GOV.UK Service Manual (Technology community, web operations) - "Working in pre-production environments".** standards. **fetched-and-verified.**
`https://www.gov.uk/service-manual/technology/working-in-pre-production-environments`
Supports: Topic 6 - test environments: the dev/integration/staging environment ladder
Quotable: "Pre-production environments are where your team builds and tests software for the digital service."
Quotable: "one or more development environments where your developers can build and experiment with new software"
Quotable: "an integration environment where you can combine all the code from your development environments and see if it works as intended"
Quotable: "a staging environment where you can do most of your testing in an environment that closely mimics the live site (or 'production environment')"
Quotable: "Before you deploy any software to a live environment, you must test it thoroughly in a staging environment that replicates the production environment as closely as possible."

**[38] GOV.UK Service Manual (Technology community, frontend development) - "Designing for different browsers and devices".** standards. **fetched-and-verified.**
`https://www.gov.uk/service-manual/technology/designing-for-different-browsers-and-devices`
Supports: Topic 7 - browser and device support policy
Quotable: "Your service must be universally accessible. This means building it to work on every browser or device that your users access it on."
Quotable: "Services do not have to look perfect in every browser. But users must be able to access and use all the information and features they need, regardless of which browser they use."
Quotable: "The list in the table represents approximately 98% of the most popular browsers used on GOV.UK."
Quotable: "If your service is aimed at internal users rather than the general public you should look at your analytics data and check which browsers your users are using. Then you can then make an informed decision about which browsers to test with."
Quotable: "Decisions about compatibility cannot be something you specify at the start of your project and then forget about. Digital services need to reflect and adapt to the changing digital behaviour of their users."

**[39] GOV.UK Service Manual (Standards and assurance community) - "Quality assurance: testing your service regularly".** standards. **fetched-and-verified.**
`https://www.gov.uk/service-manual/technology/quality-assurance-testing-your-service-regularly`
Supports: Topic 1 - test levels/types balance for a web app with an API and data pipelines (the named test-type list a program-level strategy enumerates)
Quotable: "You should aim to automate as much of your testing as possible and run your test suite as part of continuous integration (where your tests form part of your codebase)."
Quotable: "capacity and performance testing - to check how much traffic your service can handle, and how stable and responsive it is"
Quotable: "vulnerability and penetration testing - to check how secure your system is"
Quotable: "exploratory testing - to manually check for bugs and defects"
Quotable: "accessibility testing - to check that everyone, including disabled people, can use your service"
Quotable: "functional testing - to check that your code works as it should do and you expect it to"
Quotable: "You need to test your service regularly as part of quality assurance (QA) to make sure that it: is easy to use for anyone who needs to use it, regardless of the device they're using"
Quotable: "is stable, secure and works quickly, regardless of how many people need to use it"
Quotable: "can be iterated quickly to meet changes to user needs or the political environment"

**[40] GOV.UK Service Manual (contributed) - "Test your service's performance".** standards. **fetched-and-verified.**
`https://www.gov.uk/service-manual/technology/test-your-services-performance`
Supports: Topic 3 - performance/load testing (government-manual counterpart to the k6 taxonomy, with capacity planning and a caution about recording results)
Quotable: "You need to do capacity planning before you can set up realistic performance tests for your service."
Quotable: "One of the most valuable forms of performance testing is 'load testing'. This is when you test your site or application to see how much traffic it can handle while still being able to function properly."
Quotable: "When you load test your service, you should gradually increase the load until the service breaks in some way and your monitoring tools alert you to an issue."
Quotable: "You should carry out regular load testing against your pre-production environments with: realistic traffic loads"
Quotable: "loads in excess of your expected traffic levels, for example by simulating a distributed denial-of-service (DDoS) attack"
Quotable: "When testing your service, you should record: the load at which the service broke"
Quotable: "how the service broke and what went wrong"

### THE GAP QUESTION

**[41] UK Ministry of Justice, Office of the Public Guardian (OPG) Digital Team - "Baseline Testing Standards" (OPG Technical Guidance).** primary. **fetched-and-verified.**
`https://docs.opg.service.justice.gov.uk/documentation/guides/baseline_testing_standards.html`
Supports: A real standing (cross-project) test strategy for a UK government digital organization: mandatory automation baseline, an explicit regression policy, mandatory shared metrics every team must track, and an explicit deviation/local-variance mechanism
Quotable: "The intent here is to document a baseline test strategy that we expect applications to adhere to in order to ensure a minimal level of quality assurance."
Quotable: "Different applications and teams will also have different needs so there should be room for local variance. However that should be a conscious choice and be able to be explained and preferably documented e.g. in an ADR."
Quotable: "Regression should be built into automation at the unit and integration level"
Quotable: "An automated regression test should be added whenever you find a bug."
Quotable: "All suites must measure: Test coverage ... As a whole"
Quotable: "As a delta introduced by each pull request"
Quotable: "Time test suites take to execute ( Feedback ) ... As a whole suite"
Quotable: "Reliability. For example tracking how often particular tests fail to highlight flaky tests"
Quotable: "The time it takes for a ticket to move across the board from finished development to release (Is our strategy improving the team workflow)"
Quotable: "Defect density and other measures to approach introducing coverage on a risk basis"
Quotable: "In order to make conversations clearer and aid our shared understanding we have undertaken an exercise in agreeing common testing terms and their meaning in the OPG context."
Quotable: "Accessibility To be defined"
Quotable: "All suites must measure: Test coverage ..."
Quotable: "All suites must measure: Test coverage"
Quotable: "Time test suites take to execute ( Feedback ) ..."
Quotable: "Time test suites take to execute ( Feedback )"

**[42] US Internal Revenue Service, Internal Revenue Manual 2.127.2 - "IT Testing Process and Procedures" (revised 01-03-2025).** primary. **fetched-and-verified.**
`https://www.irs.gov/irm/part2/irm_02-127-002`
Supports: A detailed, mandatory federal IT testing procedure that a standing strategy document sits above: it independently supplies answers for test data management, defect/problem severity and reporting, mandatory non-functional testing tied to law/policy, test environment request process, requirements traceability, deviation/waiver approval, and standing cross-project metrics reporting
Quotable: "All system, program, or test plans must include verification strategies addressing system integration, acceptance, regression, privacy, and security as required by Cybersecurity and Section 508 of the 1973 Rehabilitation Act as currently amended."
Quotable: "Any waivers or deviations of this Directive require written approval from the ACIO, Enterprise Services."
Quotable: "If live data is used, prepare live data waiver, and ensure all testers have complete live data training."
Quotable: "The purposes of Sensitive But Unclassified Data use Request - Form 14665 are to ensure thorough consideration is given to the privacy and security of SBU data prior to use in non-production environments, and that risk is adequately mitigated. It is also used to document the use of SBU data (or use replacement of SBU data with synthetic and/or sanitized data), to document the movement or replication of SBU data between environments, and to document the request to use SBU data."
Quotable: "The purpose of a PCLIA is to demonstrate that PMs, system owners, and developers have consciously incorporated privacy and civil liberties protections throughout the entire lifecycle of a system."
Quotable: "Tickets opened should reflect Priority 3 status for a documentation error. The Problem Reporting Procedure contains information regarding the prioritization of problems in IRWorks."
Quotable: "The Test Plan (TP) is a requirement for all testing. ... The Test Plan containing the traceability of the project's business/technical requirements to specific test cases can be used in lieu of Requirements Traceability Verification Matrix (RTVM)."
Quotable: "The ELM suite of tools ensures that a traceability is developed to confirm that all requirements can be mapped to specific business processes, systems development documents, test cases and test results within the ELM."
Quotable: "A deferral requests that the verification of a test case be moved to another test release. A waiver requests that the obligation to execute a test case be eliminated, thereby departing from the course established in the test plan."
Quotable: "Test Case Deferral and Waiver Requests are initiated within the test team and are approved by the PM, to request exemption from executing test cases planned for the test step."
Quotable: "The EOTCR is a OneSDLC requirement for all delivery approaches. The EOTCR is a summarization of all testing for the project's release and must be maintained in the organization's authorized repository for audit purposes."
Quotable: "The EST Test Report is an aggregated status report of all active projects in EST and is found in EST SharePoint site."
Quotable: "The TSR for all EST projects includes start and end dates for test preparation and test execution; number of test cases completed, passed, failed, deferred, or waived."
Quotable: "EST's primary pre-audit process to ensure compliance with IT Testing Process and Procedures"
Quotable: "Submit Request for Testing Services through UWR Process"

**[43] UK Government Digital Service / Cabinet Office - "Building accessible services" (The GDS Way engineering manual).** primary. **fetched-and-verified.**
`https://gds-way.digital.cabinet-office.gov.uk/manuals/accessibility.html`
Supports: A published engineering organization's standard making one non-functional test type (accessibility) mandatory, legally grounded, and continuous across every service/project, with named mandatory testing methods and a named compliance channel (information assurance lead / privacy team) distinct from the project team
Quotable: "Government services are legally required to be accessible. This means services must comply with the international WCAG 2.2 AA accessibility standard. This requirement applies to all new and existing public sector websites and mobile applications."
Quotable: "You cannot achieve accessibility by adding some final touches - it must be considered at all stages of a project. You should review designs for possible issues, write and run tests throughout development, and test services with accessibility in mind."
Quotable: "Automated testing can only find around 30% of likely accessibility problems . Automated testing shouldn't be the only accessibility testing carried out on a service, it should also be tested with real users."
Quotable: "Test your service with assistive technologies throughout development, especially when you introduce a significant feature or make any major change."
Quotable: "You should also make sure you understand how using Assistiv Labs affects any other requirements for your service, such as PCI (Payment Card Industry) compliance, and assess any additional risks. You can speak to your service's information assurance lead or the GDS Privacy Team for specific guidance."
Quotable: "If a service is built using an existing or third party system, such as a content management system or JavaScript framework, it should be tested for accessibility. Accessibility compliance cannot be guaranteed by any system, as even small changes can introduce accessibility barriers."
