# Companion: The Test Summary Report

> The deep explainer for the test-summary-report bundle. Read this to understand what a test summary report
> is, where it came from, why it is shaped the way it is, and why a named school of practitioners campaigned
> to have the standard that defines it withdrawn. The short operator card is
> [`test-summary-report_guide.md`](test-summary-report_guide.md); a fully worked instance is
> [`test-summary-report_example.md`](test-summary-report_example.md). Inline citations like [[1]](#ref-1)
> resolve to the [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A test summary report is **the document written after a testing effort that says what was tested, what the
testing found, what was deliberately or accidentally not tested, and whether the result clears the bar the
test plan set.** The international standard that defines it gives the shortest honest definition, and gives
the document two names in the same breath: *"test completion report / test summary report / report that
provides a summary of the testing that was performed"* [[1]](#ref-1)[[2]](#ref-2). ISTQB's glossary adds the
act that one-liner leaves implicit: *"A document summarizing testing activities and results. It also contains
an evaluation of the corresponding test items against exit criteria."* [[8]](#ref-8)

**At a glance**
- It is **retrospective**. The test plan is written before and is prospective; this is its closing bookend.
- It **evaluates against the exit criteria the plan set**, which is the act that makes it a report rather
  than an export [[8]](#ref-8)[[7]](#ref-7).
- It states **what was not tested**, and real reports treat that as mandatory content rather than a courtesy
  [[51]](#ref-51)[[55]](#ref-55).
- It names **residual risk that somebody is accepting**, which in regulated contexts carries a written
  rationale for each unfixed defect [[54]](#ref-54)[[3]](#ref-3).
- It is **not what your CI dashboard produces**. See section 6; this is the distinction the whole bundle
  turns on [[43]](#ref-43)[[44]](#ref-44)[[45]](#ref-45)[[46]](#ref-46).

If you read nothing else: **a generated report can tell you what happened. Only a written one can tell you
what it means and what you are choosing to live with.**

### What this bundle read, and what it did not

This section is not a disclaimer. It is the most important thing on the page, because the governing standard
for this document type is **sold, not published**, and a bundle that quietly implied otherwise would be doing
exactly what its own critics accuse the standards world of doing.

**Read, verbatim, from the publisher's own free preview** (15 of roughly 93 pages): the standard's Clause 3
definition quoted above, and its table of contents, which shows *"7.4 Test completion report"* with ten
subclause headings - Overview, Summary of testing performed, Deviations from planned testing, Test completion
evaluation, Factors that blocked progress, Test measures, Residual risks, Test deliverables, Reusable test
assets, Lessons learned - plus *"Annex G (informative) Test completion report ... 58"* [[1]](#ref-1). A second
free preview, of the BSI edition, carries Annex A's conformance table, which records the requirement level
attached to each of those subclauses [[3]](#ref-3).

**Not read, and nothing here rests on it:** the substantive text of Clause 7.4, and Annex G's worked example.
The headings are read; what the standard *requires* under them is not. The full document is sold by ISO, IEEE
and BSI [[4]](#ref-4).

**Also not read: IEEE 829, in any edition.** Every description of "IEEE 829's Test Summary Report structure"
this research met is second-hand, and those descriptions **disagree with each other** (section 2). This
companion therefore makes **no claim about IEEE 829's section list**, and the one 829 fact it does assert -
its status - comes from the IEEE Standards Association's own catalog page [[11]](#ref-11).

**So the section design in section 3 does not come from the standard.** It comes from ISTQB's freely
published Certified Tester Foundation Level syllabus [[6]](#ref-6), corroborated against an official ISTQB
member board's current page [[7]](#ref-7), and tested against real filled reports and real published
templates [[48]](#ref-48)[[49]](#ref-49)[[50]](#ref-50)[[51]](#ref-51)[[52]](#ref-52)[[55]](#ref-55). One
honest qualifier on the ISTQB source too: the syllabus edition this bundle fetched and read is the 2018
v3.1.1 release, which ISTQB itself superseded in 2023 [[6]](#ref-6). Its verbatim contents list is quoted
throughout; ISTQB's live position on the same material is corroborated through ASTQB [[7]](#ref-7). Where a
structural claim could only come from the current syllabus edition, it is not made.

**The second thing to know** is that this document type is contested. In 2014 a petition organised by the
International Society for Software Testing asked ISO to suspend Parts 4 and 5 of this standard and to
**withdraw Parts 1 to 3** [[22]](#ref-22) - which is to say, to withdraw the very part that defines this
document. The campaign is covered in section 6, with both camps named, because a bundle that presented the
test report as a settled genre would be making a claim its own research refutes.

## 2. Origins and evolution

**The lineage everyone cites, and nobody can check.** The ancestor of this document is IEEE 829, the standard
for software test documentation, whose editions run from 1983 through 1998 to 2008. It is **superseded**. The
IEEE Standards Association's catalog page for the 2008 edition reads *"Status: Superseded Standard"*, and
names the successors: *"Superseding: ISO/IEC/IEEE 29119-1-2013, ISO/IEC/IEEE 29119-2-2013, ISO/IEC/IEEE
29119-3-2013, ISO/IEC/IEEE 29119-4-2015"* [[11]](#ref-11). ISTQB's syllabus records the same transition in one
line: *"ISO/IEC/IEEE 29119 replaces IEEE Standard 829."* [[6]](#ref-6)

**Superseded is the correct word, and this bundle does not reach for a stronger one.** A search result
circulating at the time of this research asserted an "Inactive-Withdrawn" status with a 2024 date. It could
not be corroborated against the IEEE SA page on a direct fetch, which showed no withdrawal date at all
[[11]](#ref-11), and it is therefore **not used anywhere in this bundle**. That is a small discipline with a
large payoff: the family contract this bundle joins names IEEE 829's status as its one live standards-recency
trap, and the trap is sprung by rounding a status up, not by citing 829 at all.

**And 829 cannot be used to confirm this document type by name either, which is a move almost everyone
makes.** The IEEE SA page for the 1998 edition carries only a generic abstract: *"A set of basic software
test documents is described. This standard specifies the form and content of individual test documents. It
does not specify the required set of test documents."* [[12]](#ref-12) It enumerates nothing. So citing IEEE
829 as the origin of the phrase "Test Summary Report" is a claim this bundle's sources do not support, and it
is not made here; the confirmation comes from 29119-3's Clause 3 instead [[1]](#ref-1).

**Now the part that matters for anyone who has ever seen a "per IEEE 829" test report template.** Because the
standard is sold and superseded, its contents reach practitioners entirely through second-hand enumerations,
and those enumerations do not agree. Counting document types in the same standard: Wikipedia says ten, under
Master and Level naming that never uses the phrase "Test Summary Report" at all [[13]](#ref-13); one vendor
tutorial says *"It outlines eight key document types that cover the entire testing process from planning to
execution and reporting."* [[14]](#ref-14); another lists seven [[15]](#ref-15); a practitioner reference site
lists six, naming them outright: *"The documents that are covered by this standard are: Test Plan. Test Design
Specification. Test Incident Report. Test Summary Report. Test Procedure/Script Specification. Test Case
Specification."* [[16]](#ref-16); and university courseware summarizing the 1983 edition lists eight
[[18]](#ref-18). The disagreement reaches inside the document too: one training deck gives the Test Summary
Report eight items [[17]](#ref-17), the six-item camp gives it six [[16]](#ref-16), and a widely read
practitioner article carries a reader comment correcting the article's own template with the eight-item list,
so the disagreement is visible **within a single page** [[20]](#ref-20). Several more vendor enumerations
exist and were deliberately left unfetched, because reading a sixth disagreeing list would not settle
anything [[19]](#ref-19).

**That is a claim about the sources, not about the standard.** This companion cannot tell you what IEEE 829
says. It can tell you that the confident-sounding lists in circulation are copies of copies, and that
Wikipedia's own note on 829 undercuts the whole genre of "compliant" templates built from them: *"The standard
specified the format of these documents, but did not stipulate whether they must all be produced, nor did it
include any criteria regarding adequate content for these documents."* [[13]](#ref-13) A format with no
adequacy criteria is a shape, not a quality bar.

**The successor.** ISO/IEC/IEEE 29119 is a five-part series covering *"(1) Concepts & Definitions, (2) Test
Processes, (3) Test Documentation, (4) Test Techniques, as well as (5) Keyword Driven Testing"*
[[36]](#ref-36). Part 3 is the documentation part, and its published scope says it *"specifies software test
documentation templates that can be used for any organization, project or testing activity"* [[2]](#ref-2)
and *"includes templates and examples of test documentation"* [[4]](#ref-4). The stated ambition of the series
is broad: *"The purpose of the ISO/IEC/IEEE 29119 series of software testing standards is to define an
internationally-agreed set of standards for software testing that can be used by any organization when
performing any form of software testing."* [[4]](#ref-4)

**The edition change is itself a reason not to trust old section lists.** The 2013 edition of Part 3 is
withdrawn: ISO's own page for it reads *"Status: Withdrawn"* [[5]](#ref-5), and the 2021 preview states that
the 2021 edition is a second edition that cancels and replaces the first, per the preview's own record
[[2]](#ref-2). A section list copied from a
2013-era blog post is a description of a document that no longer exists, written by someone who may not have
read it either.

**A naming drift worth knowing.** The standard's own defined term leads with *"test completion report"* and
gives *"test summary report"* as its synonym [[1]](#ref-1)[[2]](#ref-2). ISTQB's syllabus cross-maps the two
explicitly: *"ISO standard (ISO/IEC/IEEE 29119-3) refers to two types of test reports, test progress reports
and test completion reports (called test summary reports in this syllabus), and contains structures and
examples for each type."* [[6]](#ref-6) If your organization says "test completion report" and your tool says
"test summary", they are the same artifact. What is **not** the same artifact is the *test status* or *test
progress* report, which the standard defines separately as a *"report that provides information about the
status of the testing that is being performed in a specified reporting period"* [[2]](#ref-2), and which
ISTQB's glossary describes as produced *"at regular intervals"* against a baseline [[9]](#ref-9). A vendor
puts the boundary most usably: *"A test progress report communicates the status of testing while testing is
still underway. A test completion or summary report communicates the outcome of a completed testing effort or
significant testing milestone."* [[41]](#ref-41)

**The document also survives outside the standards lineage.** A Cambridge University Press book on testing
process devotes a full appendix to a reusable template, and frames the purpose in a way no standard does:
*"The purpose of a test summary report is to summarize the result of a particular testing phase and to provide
the basis for subsequent improvement of the testing process."* [[57]](#ref-57)

## 3. Anatomy (section by section)

The full variant carries nine sections; the lean variant carries six of them, unchanged in name and order.
Each section below says where it came from.

The two readable structural sources agree more than they differ. ISTQB's syllabus, read in full and free,
lists what *"Typical test summary reports may include: Summary of testing performed / Information on what
occurred during a test period / Deviations from plan, including deviations in schedule, duration, or effort of
test activities / Status of testing and product quality with respect to the exit criteria or definition of
done / Factors that have blocked or continue to block progress / Metrics of defects, test cases, test
coverage, activity progress, and resource consumption / Residual risks / Reusable test work products
produced"* [[6]](#ref-6). The standard's table of contents lists ten subclause headings under 7.4, given in
section 1 [[1]](#ref-1). Where this bundle's design departs from either, it says so.

### Scope and What Was Tested

What this report covers: the build or version, the environment, the test plan it answers to, and the boundary
of the effort.

**Name the version.** Without it every other number is meaningless. The one real filled
report in this research that omits a version is the harder document to use for exactly that reason. The FDA's guidance on software in device submissions makes it explicit: *"The summary
description should include the software version tested and the overall pass/fail test results for all test
protocols"* [[54]](#ref-54). The counter-example is instructive: the one real filled UAT summary report this
research found carries no system build or version number anywhere [[48]](#ref-48), which means nobody reading
it later can tell what it was about.

**Name the boundary, and be blunt about what the result does and does not cover.** Certification reports do
this in their front matter as a matter of course: *"Test Results in this report apply to the voting system
configuration tested. Testing of voting systems that have been modified may or may not produce the same test
results."* [[51]](#ref-51) A Common Criteria certification report goes further, disclaiming endorsement
outright: *"This report, and its associated certificate, are not an endorsement of the IT product by the
Communications Security Establishment Canada"* [[52]](#ref-52). You are not writing a certification report,
but the instinct is the right one to borrow: a report that does not bound itself gets read as covering
everything.

### Execution Summary

The counting section: planned, executed, passed, failed, blocked, not run, with coverage stated against
something meaningful.

This is the standard's *Test measures* heading [[1]](#ref-1) and ISTQB's *"Metrics of defects, test cases,
test coverage, activity progress, and resource consumption"* [[6]](#ref-6). It is also, and this is the
point, **the only section your tooling can fill for you.** TestRail's summary report is *"a high-level
overview of all progress and testing activity for one or more test runs"* [[43]](#ref-43); Jenkins' JUnit
plugin *"consumes XML test reports generated during the builds and provides some graphical visualization of
the historical test results"* [[44]](#ref-44); Azure invites you to *"Use test results charts to track how
your testing is going"* [[45]](#ref-45). If this section is the whole of your report, you have written a
dashboard screenshot with a cover page.

**Expert note.** Pass rate on its own is the weakest number you can lead with, and the evidence for treating
it carefully sits in the next section, not this one. Put the counts here; put the judgment where the criteria
are.

### Defects

What was found, at what severity, what is fixed, and what is open at the moment of writing.

The two structural sources both carry defect metrics [[6]](#ref-6)[[1]](#ref-1), and the real artifacts add
shape to it. The US federal test-report template carries a Severity of Defect column in every per-test-type results
table [[49]](#ref-49). The filled UAT report goes one level further and breaks defects down by root
cause, which is what turns a defect count into something a team can act on [[48]](#ref-48). And the strongest
requirement found anywhere on the open ones comes from the FDA, which asks for a *"Risk-based rationale for
not correcting or fixing the anomaly in alignment with the sponsor's risk management plan or procedure(s)."*
[[54]](#ref-54)

**Beginner note.** Open defects are the ones that matter here. A list of what you fixed is history; a list of
what you did not fix, with severity and a reason, is a decision that somebody is making whether or not they
write it down.

**This section is not a bug tracker.** Summarize and link. The individual reproduction steps live in the bug
reports (section 8).

### Deviations from Planned Testing

What the plan said would happen, what actually happened, and why the difference.

The standard marks this a requirement: Annex A's conformance table records *"7.4.3 Deviations from planned
testing ... Shall"* [[3]](#ref-3). ISTQB lists it, specifically including *"deviations in schedule, duration,
or effort of test activities"* [[6]](#ref-6). The US federal template asks for it in the results section:
*"Summarize the test results. Include a detailed description of any deviations from the original test plan,
design, test case, or expected results."* [[49]](#ref-49) A commercial completion-report template asks the
author to *"Describe any variance from the planned scope of testing"* [[50]](#ref-50). And the one real filled
report gives it a named subsection and a flat declarative sentence: *"The below functionality was either not
tested or only partially tested."* [[48]](#ref-48)

**This library moves this section into the lean variant**, against its own earlier internal spec, which had it
as full-only. The evidence is one-sided: it is a *shall* in the standard, it is in ISTQB's list, it is in both
real templates, and it is filled in the real report. A lean report that drops it is a lean report whose
numbers cannot be interpreted.

### Impediments and Blocked Progress (full variant only)

What got in the way: environment outages, missing test data, unavailable dependencies, access that arrived
late.

This is the standard's *"7.4.5 Factors that blocked progress"* heading [[1]](#ref-1) and ISTQB's *"Factors
that have blocked or continue to block progress"* [[6]](#ref-6); the real filled report calls its version
*Issues Encountered* [[48]](#ref-48). It is full-variant only here for a practical reason rather than an
evidential one: on a small team the impediments were lived through by everyone who will read the report. It
earns its place the moment the reader was not in the room - a steering group, a client, an auditor, or the
team that inherits the area next quarter.

### Evaluation Against Exit Criteria

Take the exit criteria the test plan set, state for each one whether it is met, and say what the testing
concludes about releasing. **This is the load-bearing section of the document, and it is where the ship
judgment lives.**

Both readable structural sources put this act here rather than in a section of its own. ISTQB's list carries
*"Status of testing and product quality with respect to the exit criteria or definition of done"* - one item,
covering both the testing and the product [[6]](#ref-6). The standard's heading is *"7.4.4 Test completion
evaluation"*, and Annex A marks it *"7.4.4 Test completion evaluation ... Shall"* [[1]](#ref-1)[[3]](#ref-3).
ISTQB's glossary definition of the whole document ends on the same act: *"It also contains an evaluation of
the corresponding test items against exit criteria."* [[8]](#ref-8) An official ISTQB member board explains
what the monitoring data is *for*: *"This information is used to assess test progress and to measure whether
the exit criteria or the test tasks associated with the exit criteria are satisfied, such as meeting the
targets for coverage of product risks, requirements, or acceptance criteria."* [[7]](#ref-7) The real filled
report names its section almost identically: *UAT Results Mapped to Exit Criteria* [[48]](#ref-48).

**Why there is no separate "Release Recommendation" section, and how this library got there.**

This bundle's own internal spec asserted that a standalone *Release Recommendation* section - ship, do not
ship, or ship with named conditions - was **the** load-bearing section of a test report. That assertion was
put under test against the evidence, and it did not survive. Recorded here as a first-class outcome, because
the alternative is a template shape defended by nothing but an earlier draft of itself.

- **Neither readable structural source has one.** Not ISTQB's eight-item list [[6]](#ref-6), not the
  standard's ten subclause headings [[1]](#ref-1). Both have an evaluation against exit criteria, which is a
  different act: it reports whether an agreed bar was cleared, rather than issuing an opinion about release.
- **The real filled reports do not have one either.** The most on-genre document in the corpus, a
  government UAT summary report, carries *Recommendations* and *UAT Results Mapped to Exit Criteria* and **no
  dedicated go/no-go section**; its nearest thing to a release rule is a sentence attributed to the customer,
  not to the testers: *"It is the State's expectation to not go-live with any high or critical defects."*
  [[48]](#ref-48) The Common Criteria certification report explicitly declines the role: *"This report, and
  its associated certificate, are not an endorsement of the IT product by the Communications Security
  Establishment Canada"* [[52]](#ref-52). The FDA 510(k) summary carries no recommendation at all; the
  determination is the regulator's, and even that determination disclaims its own reach [[53]](#ref-53). The
  Trail of Bits security assessment issues findings and severities, not a verdict [[55]](#ref-55). Only the
  voting-system certification report carries a named, signed recommendation, and that is a recommendation to
  an accreditation body under a scheme, not a QA team's call on a release [[51]](#ref-51).
- **Where explicit proceed language does appear, it appears in vendor templates**, which is the weakest tier
  in this library's citation standard. A consultancy's published completion-report template offers the
  literal fill-in: *"Based on the results of product risk mitigation activities outlined above and the final
  summary of KPI results, our recommendation is to <proceed/not proceed>."* [[50]](#ref-50) A tool vendor's
  how-to asks for *"Summary and recommendations. Give a final view of the application's health. Highlight any
  blockers, critical concerns, and readiness for release. Include clear next steps."* [[42]](#ref-42) A
  practitioner article frames the whole document as a gate: testing *"serves as the “Quality Gate” for the
  application to pass through and be certified as “Can Go Live” by the Testing Team."* [[20]](#ref-20)
- **The *Recommendations* sections that do appear in real documents are a different thing.** The US federal
  template's is about process, not release: *"Describe what actions are suggested upon completion of this
  test. Provide any recommended improvements in the design, operation, or future testing of the business
  product that resulted from the testing being reported."* [[49]](#ref-49) That content belongs in Lessons
  Learned, and that is where this template puts it.

**So the act stays and the heading goes.** The `test-plan` bundle promises, in four separate places, that
results and *the verdict* belong in a report written after; that promise is kept here. What this bundle
declines to do is give the verdict a heading of its own, floating free of the criteria that justify it,
because a recommendation with nothing above it is an opinion and a recommendation underneath a criteria table
is a conclusion. Write the criteria table, then write the sentence: met, not met, and therefore.

**Beginner note.** If your test plan set no exit criteria, this section is where you find that out. Say so
plainly and state the bar you are applying instead; do not invent criteria after the fact and grade against
them.

### Residual Risk and What Was Not Tested

What remains untested, what remains unfixed, and what that exposes - stated as risk somebody is accepting,
not as a gap somebody forgot.

Annex A marks this a requirement: *"7.4.7 Residual risks ... Shall"* [[3]](#ref-3), and ISTQB lists *"Residual
risks"* in its contents [[6]](#ref-6). **This is the section a generated report cannot produce**, and the real
artifacts show how much work it does.

The voting-system certification report enumerates exclusions by name and says why: *"The following functions
are excluded from the WinEDS 4.0 voting system and therefore not tested in this certification effort"*, and
its requirement-disposition rules make the explanation mandatory rather than optional: *"Requirements marked
Reject, NA, Pending or Out of Scope shall include an explanatory note."* [[51]](#ref-51) The Common Criteria
report states a threat-model boundary that is distinct from its pass verdict: *"EXOS is not intended for
situations which involve determined attempts by hostile or well-funded attackers using sophisticated attack
techniques."* [[52]](#ref-52) The Trail of Bits assessment warns the reader not to read silence as clearance:
*"Due to the scope of the assessment and size of the codebase, bug finding was focused on identifying
component implementations which were 'obviously wrong.' Given this focus, codebase coverage emphasized breadth
instead of depth. Portions of the codebase outside of the control areas received minimal to no coverage."*
[[55]](#ref-55) It also promotes uncertainty to a first-class value rather than rounding it down: *"Undetermined:
The extent of the risk was not determined during this engagement."* [[55]](#ref-55) And even the thinnest
document in the corpus, a 510(k) summary, is required to state an absence affirmatively: *"Clinical Performance
Data/Information: None provided as a basis for substantial equivalence."* [[53]](#ref-53)

The commercial template ties the two halves together in one instruction: *"Briefly describe any KPIs not
achieved and the resulting residual risks."* [[50]](#ref-50)

**Expert note.** "Undetermined" and "not covered" are answers. A report that has no unknowns in it is either
describing a trivial system or hiding something, and this bundle cannot tell you which.

### Test Deliverables and Reusable Assets (full variant only)

What testing produced and handed over, and what of it survives this release: suites, harnesses, fixtures,
data sets, environments.

These are the standard's *"7.4.8 Test deliverables"* and *"7.4.9 Reusable test assets"* headings
[[1]](#ref-1), and ISTQB's *"Reusable test work products produced"* [[6]](#ref-6). They are full-variant only
here, and for the reusable half there is direct evidence for the call: Annex A marks it *"7.4.9 Reusable test
assets ... Should"*, the only *should* among the completion-report subclauses whose level this research could
read [[3]](#ref-3). A standard's conformance level is not this library's sizing rule, but where the standard
itself softens an obligation, a lean variant is on safe ground leaving it out.

The empirical case for keeping it in the full variant comes from practitioners rather than standards. An
interview study across twelve companies found that *"Test results and effort are not properly documented. The
interviews revealed that there is a common problem that test results are not properly documented at all test
levels."* [[37]](#ref-37) and that teams *"need the historic information of all test assets."* [[37]](#ref-37)

### Lessons Learned (full variant only)

What the testing effort itself taught, and what should change next time.

*"7.4.10 Lessons learned"* is a subclause heading in the standard's contents and Annex A marks it *"7.4.10
Lessons learned ... Shall"* [[1]](#ref-1)[[3]](#ref-3), which makes this the one place where this library
deliberately makes a *shall* item full-variant only. The reason is a relationship rather than a doubt: this
library ships dedicated retrospective bundles, and a team that runs a retrospective is already doing this work
somewhere it will actually be read (section 8). A report that duplicates the retrospective badly serves
nobody. Where no retrospective exists, or where the report is the durable record because the team is about to
disband or the contract is about to close, this section is the only place the learning survives - which is
exactly the purpose the Cambridge text names: *"to provide the basis for subsequent improvement of the testing
process."* [[57]](#ref-57)

The US federal template's *Recommendations* section is this content: *"Provide any recommended improvements in
the design, operation, or future testing of the business product that resulted from the testing being
reported."* [[49]](#ref-49)

## 4. Variants and sizing

**Lean (six sections)** is the default: Scope and What Was Tested, Execution Summary, Defects, Deviations
from Planned Testing, Evaluation Against Exit Criteria, and Residual Risk and What Was Not Tested. That is the
set a team needs to close a release: what it was, what ran, what broke, what did not happen as planned,
whether the bar was cleared, and what is being carried forward. Every one of those six is present in ISTQB's
contents list [[6]](#ref-6), and three of the six map to subclauses the standard's own conformance table
marks *Shall*: Deviations (7.4.3), Evaluation (7.4.4) and Residual Risk (7.4.7) [[3]](#ref-3).

**Full (nine sections)** adds Impediments and Blocked Progress, Test Deliverables and Reusable Assets, and
Lessons Learned. These are the accountability-grade additions: they matter when the reader was not present,
when the assets outlive the release, or when the report is the durable record rather than a step in a
continuing conversation. Regulated submissions, certification, vendor and outsourced testing, and any report
destined for an audit file want the full variant (section 9).

The nesting is strict: every lean heading appears in the full variant, with the same name in the same order,
and full only adds. A lean report can be grown into a full one without rewriting a line of what is already
there.

**How to choose.** Ask who reads it and whether they were there. If the readers sat in the same standup all
cycle, the lean six carry everything they do not already know. If the reader is an auditor, a customer, a
regulator, or the team that inherits this area in six months, write the full nine and expect the extra three
to be the sections they read first.

**One warning about length.** The critics in section 6 are not attacking long reports; they are attacking
empty ones. A six-section report where every section decides something outranks a nine-section report padded
to look complete, and the padding is the exact failure mode the sharpest critique names [[27]](#ref-27).

## 5. Methodology lineage

**Standards lineage (waterfall-adjacent in origin).** The document arrives from a world of phases and
deliverables: IEEE 829 defined a document set [[13]](#ref-13), and 29119-3 reorganized it around the test
processes of Part 2 [[2]](#ref-2)[[4]](#ref-4). This is the lineage that produces the long, sectioned,
sign-off-bearing report, and it is the lineage the agile tradition reacted against.

**The certification and regulatory lineage** is separate and much stronger than most software teams realize,
because there the report is the deliverable. A voting-system test lab reports to an accreditation body
[[51]](#ref-51); a Common Criteria scheme publishes a certification report over a private evaluation technical
report, disclosed in its own footnote: *"The ETR is a CCS document that contains information proprietary to
the developer and/or the evaluator, and is not releasable for public review."* [[52]](#ref-52); an FDA
submission carries a system-level test report that *"should demonstrate that the protocol has been acceptably
executed with passing test results and any unresolved anomalies have been acceptably deferred based on a risk
assessment for the candidate release version."* [[54]](#ref-54) None of these is a QA team writing to its own
product manager, but all of them are the same genre doing its hardest job, and they are where this bundle's
section design got its sharpest content.

**One branch of that lineage this research could not reach.** Military test and evaluation doctrine
stayed out of reach: the US Air Force
412th Test Wing's test report author's guide was blocked on every retrieval attempt, and a second defense
candidate returned no documents at all [[58]](#ref-58). Read the absence of defense practice from this
companion as a gap in the research, not as evidence the domain has nothing to say.

**Agile lineage: contested, not absent.** One camp argues the post-hoc report is a relic. John Ferguson Smart
makes the case directly: traditional test reports *"force us to think in terms of tests that happen only
post-implementation."* [[38]](#ref-38) The same author immediately carves out the exception: *"Of course there
are some exceptions to this rule. For example in regulated environments, living documentation will often be
more exhaustive and detailed."* [[38]](#ref-38) The empirical study cited in section 3 lands in the same place
from the other direction, finding undocumented test results a common problem, one that *"poses a problem
especially in regulatory environments"*, with insurance named as its example [[37]](#ref-37).

**Context-driven lineage.** The school that opposed the standard did not oppose written artifacts. Its
principles page states the test directly: *"Test artifacts are worthwhile to the degree that they satisfy
their stakeholders' relevant requirements."* [[32]](#ref-32) Cem Kaner, a co-founder, frames documentation as
one contextually chosen deliverable among many: context-driven testers *"choose their testing objectives,
techniques, and deliverables (including test documentation) by looking first to the details of the specific
situation"* [[33]](#ref-33). And the school's own model of what a report is *for* is arguably the most useful
single line in this companion's research: *"managers need to know about problems that threaten the value of
the product and the on-time, successful completion of the project"* [[34]](#ref-34). Read that as the test for
every sentence you write: does it help a decision-maker see a threat to the value of the product?

**The DevOps compliance lineage** is the newest and the most likely to displace this document for routine
work. Where validation happens at the point of change and the evidence is queryable, *"Auditing the process
also becomes a straightforward review of the logs of the deployment step."* [[40]](#ref-40) What survives that
shift is the part that is a decision rather than a record: in that same account, the thing still written down
as a document is the set of exceptions to the controls, managed jointly rather than logged automatically
[[40]](#ref-40).

## 6. Debates and contested boundaries

### The campaign to withdraw the standard that defines this document

In 2014 a petition organised by the **International Society for Software Testing** asked ISO to suspend
publication of Parts 4 and 5 of 29119 and to **withdraw Parts 1 to 3** [[22]](#ref-22). Its framing was not a
narrow complaint about templates: *"The imposition of a standard that imposes practices and views on a
community that would not otherwise agree to them, is a political power play."* and *"Context-driven testing
developed as the antithesis of what is being pushed through ISO. They represent opposite points of view."*
[[22]](#ref-22)

**Camp A, context-driven testing.** James Bach, a co-founder of the school, put the objection at its
sharpest: *"ISO 29119 is not a standard for testing. It cannot be a standard for testing"*, and on where the
burden of proof sits, *"The burden is on those who claim that the craft can be standardized to study the craft
and recognize and resolve the deep differences among us"* [[24]](#ref-24). Michael Bolton, a leading voice of
the opposition, described the standard as *"an overstructured process model, focused on relentless, ponderous,
wasteful bureaucracy and paperwork, with negligible content on actual testing"*, with the cost stated as
displacement rather than mere volume: *"A moment that a tester spends on useless documentation is a moment in
which she's not focused on identifying risks and finding problems"* [[25]](#ref-25). Cem Kaner, a
co-founder of the school, supplies its positive position rather than its attack [[33]](#ref-33)[[32]](#ref-32).
James Christie has published sustained critiques across the following years [[28]](#ref-28)[[27]](#ref-27)[[29]](#ref-29).
A roundtable of the opposition's leadership recorded the process objection in one line: *"The mechanism for
which its (29119) is created is odious."* and the fear behind it, *"if we do so, what we will do is stifle
innovation, and everybody's going to suffer."* [[30]](#ref-30) Wikipedia summarizes the two headline
objections as a *"heavy focus on documentation will detract from the actual process of software testing"* and
a *"lack of true consensus of content - as required by ISO/IEC - among professional testers"* [[21]](#ref-21).

**Camp B, the standardizers.** The ISO/IEC/IEEE working group WG26, convened by Stuart Reid, and the ISTQB
certified-tester ecosystem. Trade press covering the dispute named both sides directly and reported that the
petition passed its thousand-signature goal within a month [[23]](#ref-23). The standardizers' case is that
the gap was real and that the standard constrains less than critics claim: *"The standards require compliant
testers to use risk-based testing, but do not restrict testers in how they perform this activity."*
[[23]](#ref-23) A vendor account of the series' intent puts the motivation plainly: *"Unfortunately, software
testing is plagued by many divergences in definitions, processes and procedures."* [[35]](#ref-35)

**A conflict-of-interest strand** was raised and never independently resolved: the opposition documented
working-group editors' commercial affiliations and argued that *"if a handful of consultancies of any size
were to use the ISO standards process to set the terms...it would raise a plausible perception of conflict of
interest"* [[26]](#ref-26). It is recorded here because it explains why critics distrusted claims of neutral
consensus, not because this bundle adjudicates it.

**Where it landed.** The standard was not withdrawn. Part 3 was revised in 2021, and the 2013 edition is the
one that carries the *"Status: Withdrawn"* label [[5]](#ref-5)[[2]](#ref-2). The opposition was not retracted
either: four years on, its instigator wrote that *"there has been no change in the beliefs of the opposition"*
and that the quiet was not agreement, *"No, the opposition has not died down; it has not had anything credible
to oppose"* [[29]](#ref-29). Institutionally the standardizers prevailed; intellectually the argument is open,
and this bundle reports the split rather than flattening it.

### The critique aimed squarely at this document

Most of the campaign was about the standard as a whole. One strand is about **this document type
specifically**, and it is the one a template author has to answer. James Christie, reviewing the standard's
own worked examples: *"The sample Test Completion Reports in the standard epitomise what is wrong. They
summarise the testing process with a collection of metrics that say nothing about the quality of the
product."* And the conclusion: *"It would be simple to comply with the ISO 29119 Test Completion Process, and
produce a report that provided no worthwhile information at all."* [[27]](#ref-27) A second critic describes
the resulting artifact from the reader's side: *"You have a document with many sections that looks good to
non-testers, but doesn't say anything about the most important things (what are you trying to test, and
how.)"* [[31]](#ref-31) The same critic frames the general hazard: *"The standard includes many documentation things
and rules that are reasonable in some situations, but often will be just a waste of time."* [[31]](#ref-31)
Christie elsewhere names the mechanism: *"Give test managers a detailed standard, and they'll start to see the
job as following the standard, not testing."* [[28]](#ref-28)

**This bundle takes that criticism as its design brief rather than its opponent.** It is the reason the
guidance in each template section asks what the section *decides* rather than what it contains, the reason
Execution Summary is explicitly labeled the section a tool can fill, and the reason the two sections a tool
cannot fill - Evaluation Against Exit Criteria and Residual Risk - are the ones the guide tells you never to
cut. **A report that is complete and empty is the failure mode. Completeness of fields is not completeness of
thought.**

### Has the CI dashboard replaced this document?

**For day-to-day status, largely yes, and pretending otherwise is how you get an unread report.** Continuous
integration gave teams always-on visibility: *"CI Services have dashboards that allow everyone to see the
state of any builds they are running."* [[39]](#ref-39) Nobody waits for a compiled document to learn that the
build is red.

**For the three things this bundle treats as load-bearing, no, and the tool vendors' own documentation is the
cleanest evidence.** Look at what four widely used tools actually produce. TestRail's Runs (Summary) report is
computed: pie charts, activity charts, and *"Forecast & Estimates"*, with no narrative or evaluation field
beyond the report's own name and description [[43]](#ref-43). Jenkins' JUnit plugin is *"graphical
visualization of the historical test results"* over XML [[44]](#ref-44). Azure's test tracking is chart
construction over test-point outcomes, and you *"Pin a chart to your team's dashboard for all the team to
view."* [[45]](#ref-45) Xray's gadgets are framed by their own vendor as inputs to a judgment rather than the
judgment: they help *"Monitor project health and readiness for release."* and offer *"a high-level snapshot
of Test outcomes, helping stakeholders evaluate project health and readiness for release."* [[46]](#ref-46)
Even the one feature in the set that emits a document rather than a dashboard turns out to be mail merge:
Xray's Document Generator *"is a feature that allows you to create customized templates and generate documents
based on your Jira data, including Xray Issues, Requirements, and Defects."*, where *"Templates (Figure 3) are
documents in DOCX (Microsoft Word) or XLSX (Microsoft Excel) formats."* [[47]](#ref-47) A mail merge over
existing field values cannot synthesize a judgment that nobody has typed.

**So the honest split.** A CI dashboard can produce every number in Execution Summary and most of Defects. It
cannot say **what was not tested and why**, **what residual risk someone is accepting**, or **whether to
ship**. Those three are judgments made by people, and a report that omits them in favor of the numbers is
strictly worse than the dashboard it duplicates, because it is also out of date.

The open-source world supplies a neat illustration of the same split from the other end: the one open-source
release-QA artifact this research found is a wiki page of chart captions - *"Planned Vs Actual Test Execution
Report:"*, *"Current Defect Status:"* - with no narrative prose beneath them [[56]](#ref-56). That is a
dashboard that has been given a document's URL.

### When a formal report is worth it at all

The most useful vendor framing of the threshold: *"A formal test summary becomes useful when teams need to
share testing results beyond a single iteration or the immediate team. It's also useful for supporting
external requirements, such as audits, customer sign-offs, regulatory reviews, and contractual obligations."*
[[41]](#ref-41) Below that threshold, a message in the channel and a link to the run is the honest artifact.

## 7. Anti-patterns and failure modes

**The dashboard with a cover page.** Execution Summary filled, everything else thin or absent. The tell is
that a reader could have learned more by opening the tool [[43]](#ref-43)[[45]](#ref-45). Fix: if the report
adds nothing to the dashboard, do not write it - or write only the three sections the dashboard cannot fill.

**Complete and empty.** Every heading present, nothing decided, because the template asked for a heading. This
is the criticism aimed at the standard's own worked examples: metrics *"that say nothing about the quality of
the product"* [[27]](#ref-27). Fix: delete any section that decides nothing, and make the exit-criteria
evaluation carry an actual "therefore".

**The report with no version.** No build number, no environment, no commit. The real filled UAT report in this
bundle's research has exactly this defect [[48]](#ref-48), and the FDA's guidance exists partly to prevent it
[[54]](#ref-54). Fix: version, environment and plan reference in the first section, always.

**Silence read as coverage.** Areas nobody tested are simply not mentioned, so a reader assumes they passed.
The security assessment in the corpus warns against precisely this reading [[55]](#ref-55). Fix: an explicit
not-tested list, with a reason per item, in the same style as the certification report's exclusions
[[51]](#ref-51).

**Pass rate as the verdict.** "98 percent passed, shipping." A percentage is an input to the exit-criteria
evaluation, never a substitute for it [[8]](#ref-8)[[7]](#ref-7). Fix: grade each criterion, and let the
severity of what failed do the work the average is hiding.

**The bug tracker pasted in.** Full reproduction steps and comment threads for forty defects. Fix: summarize
by severity and root cause, and link out; the reproduction lives in the bug report [[48]](#ref-48).

**Residual risk written as apology.** "Unfortunately we ran out of time for the migration path." That is a
schedule confession, not a risk statement. Fix: name what could go wrong, who is accepting it, and on what
basis - the FDA's *"Risk-based rationale"* framing is the model [[54]](#ref-54).

**The verdict with nothing above it.** A confident release recommendation sitting on top of numbers that do
not support it, or on no criteria at all. This is the failure that removing the standalone recommendation
heading is designed to prevent (section 3). Fix: the criteria table comes first and the sentence comes second.

**Written for nobody.** No named reader, so no decision. The context-driven test applies: an artifact is
worthwhile *"to the degree that they satisfy their stakeholders' relevant requirements"* [[32]](#ref-32). Fix:
name the reader in the first paragraph, and cut everything that reader already knows.

## 8. Relationships to other artifacts

**Test summary report and test plan: the closing bookend.** The plan is prospective and prescriptive; the
report is retrospective and descriptive. The relationship is not merely sequential, it is structural: **the
report's Evaluation Against Exit Criteria section has content only because the plan wrote criteria.** The
`test-plan` bundle in this library promises this document in four separate places - its guide routes "What we
found, and whether we are shipping" to a test report, its companion says results, status and the verdict live
in the report rather than the plan, and both of its template variants say the plan is "NOT a test report (that
is retrospective, written after)". This bundle exists to keep that promise. See
[`test-plan_companion.md`](../test-plan/test-plan_companion.md).

**Test summary report and test case.** A test case is one executable verification; the report summarizes the
outcome of many. The report should never restate case steps. Where a case is worth naming individually, name
it and link it. See [`test-case_companion.md`](../test-case/test-case_companion.md).

**Test summary report and bug report.** A bug report records one verification that failed, with the
reproduction an engineer needs; the report's Defects section counts and characterizes them and says which
remain open. The vocabulary is worth watching: the standard's term is *incident report*, and it lists the
synonyms explicitly - *"Incident reports are also known as anomaly reports, bug reports, defect reports, error
reports, issues, problem reports and trouble reports, amongst other terms."* [[2]](#ref-2) One failing case
produces one bug report; the summary report never accumulates them. See
[`bug-report_companion.md`](../bug-report/bug-report_companion.md).

**Test summary report and acceptance criteria.** The `qa-docs` family contract requires every member to state
its position against acceptance criteria, because that is the confusion the family exists to resolve, and the
answer for this member is the cleanest in the family. **Acceptance criteria are the story-level contract of
doneness, agreed with the business before work starts. Exit criteria are the effort-level contract of
stopping, set by the test plan.** They are different instruments at different altitudes, and this report
grades against the second, not the first. They meet in one place: criteria coverage can be one of the exit
criteria the report evaluates, which is exactly how ISTQB's ecosystem describes the monitoring data being used -
to measure whether exit criteria are satisfied, *"such as meeting the targets for coverage of product risks,
requirements, or acceptance criteria."* [[7]](#ref-7)

Two consequences a reader should take away. First, **a report that lists acceptance criteria and ticks them
off has reported on the stories, not on the testing**: test design continues past the agreed criteria into
negative, boundary, regression and non-functional cases nobody signed off, and the coverage and defects found
there belong in this report with everything else. Second, **a defect does not have to violate an acceptance
criterion to count in the Defects section**, for the same reason. See
[`acceptance-criteria_companion.md`](../acceptance-criteria/acceptance-criteria_companion.md).

**Test summary report and test status or progress report.** Different documents, and the standard defines them
separately [[2]](#ref-2)[[1]](#ref-1). A progress report is *"produced at regular intervals"* against a
baseline [[9]](#ref-9); this one is produced once, at the end of a defined effort. If you are writing the same
document every Friday, you are writing progress reports, and the completion report is still owed at the end
[[41]](#ref-41)[[7]](#ref-7).

**Test summary report and retrospective.** The overlap is real and it is the reason Lessons Learned is
full-variant only here (section 3). A retrospective is a team practice about how the work went; this report's
lessons section is a written record for readers who were not there. If your team runs retrospectives, keep the
learning there and keep this section short or absent. If it does not, or if the report is the durable artifact
because the engagement is ending, this is where the learning survives [[57]](#ref-57). This library ships
[`sprint-retrospective-notes`](../sprint-retrospective-notes/) and
[`project-milestone-retrospective`](../project-milestone-retrospective/) for the first case.

**Test summary report and incident postmortem.** Different phases of the lifecycle and different families: a
postmortem covers a failure in production, this report covers verification before release. A postmortem may
cite a test report to establish what was and was not covered; it never replaces one. See
[`incident-postmortem`](../incident-postmortem/).

**Test summary report and the tool.** Covered at length in section 6. The short version: the tool owns the
counts and the charts, this document owns the judgment, and the two are complements. Teams that believe the
tool's export is the report end up with numbers and no decision [[43]](#ref-43)[[47]](#ref-47).

**Within the qa-docs family.** This is the family's fourth member and its closing one: the plan scopes, the
case specifies, the bug report records one failure, and this report closes the effort. The family contract
requires the examples to chain on one shared scenario, and this bundle's example completes that chain. The
family's membership rule and its obligations live in
[the qa-docs family contract](../../docs/internal/contracts/qa-docs.md), adopted by
[ADR 0026 (adopt the qa-docs family contract)](../../docs/internal/decisions/0026-adopt-qa-docs-family-contract.md);
the judgment admitting this fourth member is recorded in
[ADR 0050 (qa-docs admits a fourth member)](../../docs/internal/decisions/0050-qa-docs-admits-a-fourth-member.md).

## 9. Adaptations

**Regulated submissions.** Use the full variant and expect the residual-risk section to be the most scrutinized
page in it. The FDA's expectation is the model: version tested and overall pass/fail stated up front
[[54]](#ref-54), and every unresolved anomaly carrying a description, a safety evaluation, an outcome and a
*"Risk-based rationale for not correcting or fixing the anomaly"* [[54]](#ref-54). Nothing about this is
ceremonial; each of those fields is a decision someone will be asked to defend.

**Third-party certification and independent assessment.** Two habits from that world are worth borrowing even
when you are not certifying anything. First, **bound the claim**: say what configuration and version the
result applies to, and say what the report is not [[51]](#ref-51)[[52]](#ref-52). Second, **separate the public
summary from the evidence record** where the detail is sensitive or simply enormous, and say in the report that
you have done so rather than leaving a reader to wonder [[52]](#ref-52).

**Vendor and outsourced testing.** The report is functioning as a contract deliverable, so the disposition
rules matter more than the prose. The voting-system lab's rule is the pattern to copy: every requirement
carries a disposition, and anything other than a clean pass *"shall include an explanatory note"*
[[51]](#ref-51). Also name who tested what, including any subcontracted work [[51]](#ref-51).

**Continuous delivery.** Do not write one of these per deploy. Either drop the document and rely on the
pipeline's evidence trail, which is the DevOps compliance pattern [[40]](#ref-40), or write one per release
train or per significant milestone, which is the threshold the vendor framing names [[41]](#ref-41). A
per-deploy report is the unread-artifact failure with extra steps.

**Small teams and single iterations.** Often the honest answer is not to write one. If the readers were in the
room all cycle, a short message with the exit-criteria call and the residual-risk list carries the entire
value. The context-driven test applies with full force here: the artifact is worth what it does for its
stakeholders [[32]](#ref-32)[[33]](#ref-33).

**User acceptance testing.** UAT reports are their own dialect and the real one in this research shows the
shape: execution results, defects by root cause, issues encountered, results mapped to exit criteria, and
recommendations [[48]](#ref-48). One thing to fix relative to that example: it records that *"There was no
formal sign off; however, verbal agreement was obtained during the UAT Exit meeting."* [[48]](#ref-48) If
sign-off matters in your context, get it in writing and record who gave it and when.

**Open source.** The genre barely exists; release QA is generally a dashboard or a wiki page of charts
[[56]](#ref-56). If you want the judgment recorded, the lean variant on the release issue is a good fit, and
Residual Risk is the section your downstream consumers will actually thank you for.

## 10. Worked example

[`test-summary-report_example.md`](test-summary-report_example.md) is a full-variant report for the "Saved
Views for Dashboards" feature at the fictional Acme Analytics, closing the `qa-docs` chain on the same
scenario its siblings use. It reports the cycle that the
[test plan](../test-plan/test-plan_example.md) scoped, running the
[test cases](../test-case/test-case_example.md) that plan scheduled, and it accounts for the defect that the
[bug report](../bug-report/bug-report_example.md) records.

Three sections in it are the ones worth studying, because they are the three this companion argues a
generated report cannot produce. Its **Evaluation Against Exit Criteria** grades the plan's own criteria one
by one and reaches its release conclusion underneath them rather than above them, which is the structure
section 3 argues for. Its **Residual Risk and What Was Not Tested** names coverage that was not attempted and
says who is carrying the consequence. And its **Deviations from Planned Testing** is filled rather than waved
at, which is what makes the execution numbers above it interpretable.

---

## References

<a id="ref-1"></a>[1] ISO/IEC/IEEE. "[ISO/IEC/IEEE 29119-3:2021(E), Software and systems engineering - Software testing - Part 3: Test documentation](https://cdn.standards.iteh.ai/samples/79429/27623aa24dba41a2876884c0ec57f5d7/ISO-IEC-IEEE-29119-3-2021.pdf)." Free preview distributed by iTeh, Inc. (accessed 2026-09-14). **FREE PREVIEW ONLY: 15 of roughly 93 pages** (title page, copyright notice, full Contents, Foreword, Introduction, the complete Clause 3 "Terms and definitions" and Clause 4.1). Supports the Clause 3 definition ("3.9 test completion report / test summary report / report that provides a summary of the testing that was performed") and the table-of-contents structure ("7.4 Test completion report ... 18"; "7.4.1 Overview / 7.4.2 Summary of testing performed / 7.4.3 Deviations from planned testing / 7.4.4 Test completion evaluation / 7.4.5 Factors that blocked progress / 7.4.6 Test measures / 7.4.7 Residual risks / 7.4.8 Test deliverables / 7.4.9 Reusable test assets / 7.4.10 Lessons learned"; "Annex G (informative) Test completion report ... 58"). **The substantive text of Clause 7.4 and of Annex G is not in the preview and was not read; every reference to the standard's "outline" in this companion is a list of subclause headings from a table of contents, and nothing here claims what the standard requires under them.** [primary]

<a id="ref-2"></a>[2] ISO/IEC/IEEE. "[ISO/IEC/IEEE 29119-3:2021(E), Software and systems engineering - Software testing - Part 3: Test documentation](https://cdn.standards.iteh.ai/samples/79429/396e15090ac642008cc4ccbd10e89b7f/ISO-IEC-IEEE-29119-3-2021.pdf)." Free preview served by iTeh Standards (accessed 2026-09-14). A second sanctioned preview of the same edition. Supports the scope statement ("This document specifies software test documentation templates that can be used for any organization, project or testing activity. It describes the test documentation that is an output of the processes specified in ISO/IEC/IEEE 29119-2."), the definitions of test status report ("report that provides information about the status of the testing that is being performed in a specified reporting period") and incident report ("Incident reports are also known as anomaly reports, bug reports, defect reports, error reports, issues, problem reports and trouble reports, amongst other terms."), and that the second edition "cancels and replaces the first edition". **Clauses 4 to 8 and Annexes E to T, including the worked completion-report example, were not read.** [primary]

<a id="ref-3"></a>[3] ISO/IEC/IEEE / BSI. "[BS ISO/IEC/IEEE 29119-3:2021](https://www.normsplash.com/Samples/BSI/178579133/BS-ISO-IEC-IEEE-29119-3-2021-en-2.pdf)." Free preview served by normsplash (accessed 2026-09-14). **FREE PREVIEW ONLY**, covering Annex A's requirement-conformance table and Annexes B to D. Supports the conformance level attached to individual subclauses ("7.4 Test completion report ... Shall / 7.4.3 Deviations from planned testing ... Shall / 7.4.4 Test completion evaluation ... Shall / 7.4.7 Residual risks ... Shall / 7.4.9 Reusable test assets ... Should / 7.4.10 Lessons learned ... Shall"). **This is a conformance table, not the normative text of Clause 7.4: it records which subclauses are required, not what they require.** BSI printed page numbers are offset from the ISO/IEC/IEEE edition, so clause references are used here rather than pages. [primary]

<a id="ref-4"></a>[4] IEEE Standards Association / ISO/IEC JTC 1. "[IEEE/ISO/IEC International Standard for Software testing - Part 3: Test documentation (29119-3-2021)](https://standards.ieee.org/ieee/29119-3/7499/)." IEEE SA (accessed 2026-09-14). Supports the series' stated purpose and that Part 3 supplies templates and examples ("The purpose of the ISO/IEC/IEEE 29119 series of software testing standards is to define an internationally-agreed set of standards for software testing that can be used by any organization when performing any form of software testing."; "ISO/IEC/IEEE 29119-3 includes templates and examples of test documentation."). **Abstract and catalog page only; the standard itself is sold and was not read.** [primary]

<a id="ref-5"></a>[5] International Organization for Standardization. "[ISO/IEC/IEEE 29119-3:2013](https://www.iso.org/standard/56737.html)." ISO (accessed 2026-09-14). Supports the withdrawn status of the first edition of Part 3 ("Status: Withdrawn"; "Annex A contains outlines of the contents of each document."). Catalog page only; the 2013 text was not read by anyone in this research. [primary]

<a id="ref-6"></a>[6] International Software Testing Qualifications Board. "[Certified Tester Foundation Level Syllabus, Version 2018 v3.1.1](https://astqb.org/assets/documents/CTFL-2018-Syllabus.pdf)." Hosted by ASTQB (released 2021-07-01; accessed 2026-09-14). The structural spine of this bundle's section design, read in full and free. Supports the contents list ("Typical test summary reports may include: Summary of testing performed / Information on what occurred during a test period / Deviations from plan, including deviations in schedule, duration, or effort of test activities / Status of testing and product quality with respect to the exit criteria or definition of done / Factors that have blocked or continue to block progress / Metrics of defects, test cases, test coverage, activity progress, and resource consumption / Residual risks / Reusable test work products produced"), the cross-mapping of terms ("ISO standard (ISO/IEC/IEEE 29119-3) refers to two types of test reports, test progress reports and test completion reports (called test summary reports in this syllabus), and contains structures and examples for each type.") and the supersession of IEEE 829 ("ISO/IEC/IEEE 29119 replaces IEEE Standard 829."). **This edition is superseded**, per its own record in this bundle's research log, by CTFL v4.0 (2023-04-21, errata v4.0.1 2024-09-15); the current edition was not fetched as a separate source in this research, and ISTQB's live position is corroborated through [[7]](#ref-7). [practitioner]

<a id="ref-7"></a>[7] ASTQB (American Software Testing Qualifications Board, an official ISTQB member board). "[5.3 Test Monitoring, Test Control and Test Completion](https://astqb.org/5-3-test-monitoring-test-control-and-test-completion/)." ASTQB (accessed 2026-09-14). Supports the progress-versus-completion split and the exit-criteria purpose from a current official member-board page ("Test completion reports summarize a specific test activity (e.g., test level, test cycle, iteration) and can give information for subsequent testing."; "This information is used to assess test progress and to measure whether the exit criteria or the test tasks associated with the exit criteria are satisfied, such as meeting the targets for coverage of product risks, requirements, or acceptance criteria."). [primary]

<a id="ref-8"></a>[8] ISTQB Glossary content, third-party mirror. "[Test Summary Report](https://istqb-glossary.page/test-summary-report/)." istqb-glossary.page (accessed 2026-09-14). Supports the glossary definition, including the evaluation-against-exit-criteria clause ("A document summarizing testing activities and results. It also contains an evaluation of the corresponding test items against exit criteria."). **Unofficial mirror, not the official glossary domain**, which could not be read (see [[10]](#ref-10)); tagged reference rather than primary for that reason. [reference]

<a id="ref-9"></a>[9] ISTQB Glossary content, third-party mirror. "[Test Progress Report](https://istqb-glossary.page/test-progress-report/)." istqb-glossary.page (accessed 2026-09-14). Supports that test progress report and test status report are synonyms of each other and distinct from the completion report ("A document summarizing testing activities and results, produced at regular intervals, to report progress of testing activities against a baseline (such as the original test plan) and to communicate risks and alternatives requiring a decision to management."). Same mirror caveat as [[8]](#ref-8). [reference]

<a id="ref-10"></a>[10] International Software Testing Qualifications Board. "[ISTQB Glossary (official site)](https://glossary.istqb.org/en_US/search?searchTerm=test+summary+report)." ISTQB (checked 2026-09-14). **NOT READ: the URL resolves with HTTP 200 but the site is a client-side JavaScript application, and neither direct fetch nor browser-emulated fetch returned rendered body text.** Cited here only to disclose why the glossary definitions in this companion come from a mirror ([[8]](#ref-8), [[9]](#ref-9)) rather than from the official source. A human with a browser should confirm those definitions against this page. [primary]

<a id="ref-11"></a>[11] IEEE Standards Association. "[IEEE 829-2008 standard catalog page](https://standards.ieee.org/ieee/829/3787/)." IEEE SA (accessed 2026-09-14). The sole source for IEEE 829's status in this bundle ("Status: Superseded Standard"; "Superseding: ISO/IEC/IEEE 29119-1-2013, ISO/IEC/IEEE 29119-2-2013, ISO/IEC/IEEE 29119-3-2013, ISO/IEC/IEEE 29119-4-2015"). Fetched twice; both times the status field read "Superseded Standard" with no withdrawal date shown. **A separate search-result synthesis asserting an "Inactive-Withdrawn" status dated 2024-10-28 could not be corroborated against this page and is not used anywhere in this bundle.** [primary]

<a id="ref-12"></a>[12] IEEE Standards Association. "[IEEE 829-1998 standard catalog page](https://standards.ieee.org/ieee/829/1218/)." IEEE SA (accessed 2026-09-14). Supports that the 1998 edition is itself superseded and, importantly, that its abstract does **not** enumerate individual document types ("Status: Superseded Standard"; "A set of basic software test documents is described. This standard specifies the form and content of individual test documents. It does not specify the required set of test documents."). **This source therefore cannot be used to confirm that IEEE 829 names a "Test Summary Report", and it is not used for that here.** [primary]

<a id="ref-13"></a>[13] Wikipedia contributors. "[Software test documentation](https://en.wikipedia.org/wiki/Software_test_documentation)." Wikipedia (accessed 2026-09-14). One data point in the second-hand disagreement over IEEE 829's contents: describes the 2008 edition as specifying ten document types under Master and Level naming, never using the phrase "Test Summary Report" ("Master Test Report (MTR): To summarise the results of the levels of the designated testing activities and to provide evaluations based on these results..."), and records that the standard set no content-adequacy bar ("The standard specified the format of these documents, but did not stipulate whether they must all be produced, nor did it include any criteria regarding adequate content for these documents."). Tertiary source, describing a standard nobody in this research read. [reference]

<a id="ref-14"></a>[14] ZetCode. "[IEEE 829 Tutorial: Test Documentation Standard Explained](https://zetcode.com/terms-testing/ieee-829/)." ZetCode (accessed 2026-09-14). Second data point in the same disagreement: eight document types ("It outlines eight key document types that cover the entire testing process from planning to execution and reporting."). Used only as evidence that the second-hand descriptions conflict, never as a claim about the standard's actual contents. [vendor]

<a id="ref-15"></a>[15] Future Skill. "[IEEE 829 - Standard for Software Test Documentation](https://futureskill.blog/standards/ieee-829/)." futureskill.blog (accessed 2026-09-14). Third data point: seven document types, omitting the Test Item Transmittal Report that [[14]](#ref-14) includes ("The standard outlines a comprehensive set of documents that testers need to create at various stages of the testing process."). Same caveat as [[14]](#ref-14). [vendor]

<a id="ref-16"></a>[16] professionalqa.com. "[IEEE 829-1998](https://www.professionalqa.com/ieee-standard-829-1998)." professionalqa.com (published 2018-04-06; accessed 2026-09-14). Fourth data point, and the one that gives the Test Summary Report six internal items ("The documents that are covered by this standard are: Test Plan. Test Design Specification. Test Incident Report. Test Summary Report. Test Procedure/Script Specification. Test Case Specification."). Directly contradicts [[17]](#ref-17) on the same claimed edition. [practitioner]

<a id="ref-17"></a>[17] "[Document Skeletons based on IEEE 829 Software Test Documentation](https://www.ctqb.org/en/downloads/others.html?file=files/content/ctqb/downloads/others/Skeleton+test+documents+IEEE829.pdf&cid=33158)." Hosted at ctqb.org; the PDF's footer is font-subsetted and its decoding to a publisher name is an inference rather than a confirmed read (accessed 2026-09-14). Fifth data point: eight document types and an eight-item Test Summary Report ("Identifier (and reference to test plan and test design)"; "Variances (against plan)"; "Report any variances of the tests executed from test plan, test designs or procedure. Specify the reason for each variance."). Undated training material; **publisher identity unconfirmed**, and it disagrees with [[16]](#ref-16) about the same edition. [practitioner]

<a id="ref-18"></a>[18] Dalhousie University, CS3130 course materials (credited to "STL"). "[IEEE Standard for Software Test Documentation (ANSI/IEEE Standard 829-1983)](https://web.cs.dal.ca/~arc/teaching/CS3130/Templates/TestingTemplates/Test%20Plan%20Templates/IEEEStandardTestPlans.doc)." Dalhousie University (file metadata dated 2001; accessed 2026-09-14). Sixth data point, and a third distinct edition: eight deliverable documents for the 1983 edition ("Identify the deliverable documents: test plan, test design specifications, test case specifications, test procedure specifications, test item transmittal reports, test logs, test incident reports, test summary reports"). Courseware summarizing a standard from two decades before the page was written. [academic]

<a id="ref-19"></a>[19] Various commercial and blog authors. "[Test Summary Report](https://www.professionalqa.com/test-summary-report)" and comparable pages on zetcode.com, pdf4pro.com, reqtest.com and StickyMinds. **NOT RETRIEVED: deliberately left unfetched in this research.** Cited only to record that further disagreeing second-hand enumerations of IEEE 829's Test Summary Report exist, and that reading another one would not resolve the conflict among [[13]](#ref-13) through [[18]](#ref-18). No content from these pages is used anywhere in this bundle. [vendor]

<a id="ref-20"></a>[20] Bhaskar, softwaretestinghelp.com. "[Test Summary Report Template (Example PDF) / How To Write An Effective Test Summary Report](https://www.softwaretestinghelp.com/test-summary-report-template-download-sample/)." Software Testing Help (accessed 2026-09-14). Supports the release-gate framing of the document ("Software Testing is an important phase in SDLC and also it serves as the “Quality Gate” for the application to pass through and be certified as “Can Go Live” by the Testing Team.") and, in a reader comment contradicting the article's own template, an eight-item IEEE 829 list ("This is not a Test Summary Report. As per the IEEE 829 standard Test Summary Report Template is as follows: Test summary report identifier Summary Variances Comprehensive assessment Summary of results Evaluation Summary of activities Approvals"). The article and its comment disagree on the same page, which is the point it is cited for. [practitioner]

<a id="ref-21"></a>[21] Wikipedia contributors. "[ISO/IEC 29119](https://en.wikipedia.org/wiki/ISO/IEC_29119)." Wikipedia (accessed 2026-09-14). Supports an encyclopedic summary of the named objections to the standard ("heavy focus on documentation will detract from the actual process of software testing"; "lack of true consensus of content - as required by ISO/IEC - among professional testers"). Wikipedia content changes; treat as a snapshot at the fetch date. [reference]

<a id="ref-22"></a>[22] International Society for Software Testing. "[Please sign the Petition to Stop ISO 29119](https://context-driven-testing.com/please-sign-the-petition-to-stop-iso-29119/)." Hosted on context-driven-testing.com (accessed 2026-09-14). The petition document itself, supporting its stated ask (suspend Parts 4 and 5, withdraw Parts 1 to 3) and its framing ("The imposition of a standard that imposes practices and views on a community that would not otherwise agree to them, is a political power play."; "Context-driven testing developed as the antithesis of what is being pushed through ISO. They represent opposite points of view."). This is the advocacy document, organized by the opposition; not a neutral account of the standard's contents. [primary]

<a id="ref-23"></a>[23] SD Times. "[The software testing schism](https://sdtimes.com/applause/software-testing-schism/)." SD Times (accessed 2026-09-14). Trade-press account naming both camps directly - Stuart Reid and WG26 on the standardizing side, James Bach and ISST on the context-driven side - and reporting that the petition passed its thousand-signature goal within a month. Supports both the opposition's framing ("The imposition of a 'standard' by one faction of the testing community, apart from being illegitimate, has the potential to allow them to control who gets to call themselves a tester.") and the standardizers' reply ("The standards require compliant testers to use risk-based testing, but do not restrict testers in how they perform this activity."). Journalism from the height of the 2014 controversy; frames the split as unresolved. [reference]

<a id="ref-24"></a>[24] James Bach. "[How Not to Standardize Testing (ISO 29119)](https://www.satisfice.com/blog/archives/1464)." Satisfice, Inc. (accessed 2026-09-14). Supports the context-driven camp's core objection at its sharpest ("ISO 29119 is not a standard for testing. It cannot be a standard for testing"; "The burden is on those who claim that the craft can be standardized to study the craft and recognize and resolve the deep differences among us"). Bach is a co-founder of the opposing school and a named party; strongly partisan. [primary]

<a id="ref-25"></a>[25] Michael Bolton. "[Frequently-Asked Questions About the 29119 Controversy](https://developsense.com/blog/2014/09/frequently-asked-questions-about-the-29119-controversy)." DevelopSense (accessed 2026-09-14). Supports the documentation-displaces-testing objection in the opposition's own words ("overstructured process model, focused on relentless, ponderous, wasteful bureaucracy and paperwork, with negligible content on actual testing"; "A moment that a tester spends on useless documentation is a moment in which she's not focused on identifying risks and finding problems"). Bolton is a direct party to the dispute and a leader of the opposition; this is his advocacy FAQ, not a neutral account. [primary]

<a id="ref-26"></a>[26] Michael Bolton. "[Dramatis Personae](https://developsense.com/blog/2014/09/dramatis-personae)." DevelopSense (accessed 2026-09-14). Supports the conflict-of-interest strand of the critique regarding working-group editors' commercial affiliations ("if a handful of consultancies of any size were to use the ISO standards process to set the terms...it would raise a plausible perception of conflict of interest"). Bolton's own characterization of the working group's composition and motives; disputed, never independently audited, and reported here without adjudication. [primary]

<a id="ref-27"></a>[27] James Christie. "[Do we want to be 'compliant' or valuable? (Stop 29119 tag archive)](https://clarotesting.wordpress.com/tag/iso29119-iso-29119-testing-software-testing-stop-29119-stop29119-testing-standards/)." Claro Testing (accessed 2026-09-14). The one critique in this research aimed squarely at this document type ("The sample Test Completion Reports in the standard epitomise what is wrong. They summarise the testing process with a collection of metrics that say nothing about the quality of the product."; "It would be simple to comply with the ISO 29119 Test Completion Process, and produce a report that provided no worthwhile information at all."). Explicitly adversarial, published 2017 at the tail of the campaign, and disputed by the standard's proponents. [practitioner]

<a id="ref-28"></a>[28] James Christie. "[Why ISO 29119 is a flawed quality standard](https://clarotesting.wordpress.com/2016/04/07/why-iso-29119-is-a-flawed-quality-standard/)." Claro Testing (published 2016-04-07; accessed 2026-09-14). Supports that the critique was sustained rather than a single 2014 flashpoint, and names the displacement mechanism ("Give test managers a detailed standard, and they'll start to see the job as following the standard, not testing."). The author references his own continuing campaign against the standard. [practitioner]

<a id="ref-29"></a>[29] James Christie. "[Has opposition to ISO 29119 really died down?](https://clarotesting.wordpress.com/2018/07/21/has-opposition-to-iso-29119-really-died-down/)." Claro Testing (published 2018-07-21; accessed 2026-09-14). Supports that the opposition was not retracted ("there has been no change in the beliefs of the opposition"; "No, the opposition has not died down; it has not had anything credible to oppose"). Written by the campaign's original instigator; a 2018 snapshot, **not a current (2026) status**, which this research could not establish. [practitioner]

<a id="ref-30"></a>[30] Keith Klain (moderator), with Iain McCowatt, Michael Bolton, James Christie, Griffin Jones and Ilari Aegerter. "[ISO 29119 Roundtable Discussion - Part III](https://qualityremarks.com/iso-29119-roundtable-discussion-part-iii/)." Quality Remarks (accessed 2026-09-14). Multi-voice primary transcript naming the organized opposition and its process objection ("The mechanism for which its (29119) is created is odious."; "if we do so, what we will do is stifle innovation, and everybody's going to suffer."). This installment is critics-only by the host's own selection; the standardizing side is represented in [[23]](#ref-23) and [[35]](#ref-35) instead. [practitioner]

<a id="ref-31"></a>[31] Henrik Edgren. "[On ISO 29119 Content](https://thetesteye.com/blog/2014/08/on-iso-29119-content/)." thetesteye.com (accessed 2026-09-14). The most document-specific critique found: documentation for its own sake, and templates that look complete while saying nothing ("The standard includes many documentation things and rules that are reasonable in some situations, but often will be just a waste of time. Good, useful documentation is good and useful, but following the standard will lead to documentation for its own sake."; "You have a document with many sections that looks good to non-testers, but doesn't say anything about the most important things (what are you trying to test, and how.)"). The author claims direct familiarity with the standard's content; this research did not independently verify whether he read the sold standard or a draft. [primary]

<a id="ref-32"></a>[32] Context-Driven Testing (the school's own site). "[Principles](https://context-driven-testing.com/)." context-driven-testing.com (accessed 2026-09-14). Supports the school's actual position on documentation, which is stakeholder-justified value rather than blanket opposition ("Test artifacts are worthwhile to the degree that they satisfy their stakeholders' relevant requirements."; "Standard 829 starts with a vision of good documentation and encourages the tester to modify what is created based on the needs of the stakeholders."). Undated principles page; the school's canonical self-description. [primary]

<a id="ref-33"></a>[33] Cem Kaner. "[What is context-driven testing?](https://kaner.com/?p=49)." kaner.com (accessed 2026-09-14). Supports the co-founder's framing of documentation as one contextually chosen deliverable ("Context-driven testers choose their testing objectives, techniques, and deliverables (including test documentation) by looking first to the details of the specific situation"). Kaner is a co-founder of the school; self-description, not a neutral account. [primary]

<a id="ref-34"></a>[34] Michael Bolton. "[Braiding The Stories (Test Reporting Part 2)](https://developsense.com/blog/2012/02/braiding-the-stories)." DevelopSense (published February 2012; accessed 2026-09-14). Supports the context-driven model of what a test report is for ("managers need to know about problems that threaten the value of the product and the on-time, successful completion of the project"). Bolton's own methodology, not an industry consensus view. [primary]

<a id="ref-35"></a>[35] Reqtest. "[ISO/IEC/IEEE 29119: Creating a standard approach to test software](https://reqtest.com/en/knowledgebase/isoiecieee-29119-creating-a-standard-approach-to-test-software/)." Reqtest (accessed 2026-09-14). Supports the standardizers' stated motivation, the gap the series was meant to fill ("ISO/IEC/IEEE 29119 is a new standard series that seeks to become the common language of software testing organisation."; "Unfortunately, software testing is plagued by many divergences in definitions, processes and procedures."). Vendor content, and the "common language" framing is exactly what the critics dispute. [vendor]

<a id="ref-36"></a>[36] Jürgen Großmann, Michael Felderer, Johannes Viehmann and Ina Schieferdecker. "[A Taxonomy to Assess and Tailor Risk-based Testing in Recent Testing Standards](https://arxiv.org/pdf/1905.10676)." arXiv (accessed 2026-09-14). Supports the five-part structure of the series from a freely readable academic source rather than the sold standard ("The new international series of software testing standards ISO/IEC/IEEE 29119 consists of five parts, which cover (1) Concepts & Definitions, (2) Test Processes, (3) Test Documentation, (4) Test Techniques, as well as (5) Keyword Driven Testing."). Describes the series' outer structure only and never claims to describe Part 3's internal contents. [academic]

<a id="ref-37"></a>[37] Jannik Fischbach, Henning Femmer, Daniel Mendez, Davide Fucci and Andreas Vogelsang. "[What Makes Agile Test Artifacts Useful? An Activity-Based Quality Model from a Practitioners' Perspective](https://arxiv.org/pdf/2009.01722)." ESEM '20 (ACM/IEEE), via arXiv (accessed 2026-09-14). Supports that undocumented test results are a recurring, named problem in agile teams and that regulated industries need the durable record ("Test results and effort are not properly documented. The interviews revealed that there is a common problem that test results are not properly documented at all test levels."; "This poses a problem especially in regulatory environments"; practitioners "need the historic information of all test assets."). A qualitative interview study of 18 practitioners across 12 companies, flagged by its own authors as not statistically generalizable and specific to 2020-era agile contexts. [academic]

<a id="ref-38"></a>[38] John Ferguson Smart. "[Living Documentation: it's not just about test reports](https://johnfergusonsmart.com/living-documentation-not-just-test-reports/)." johnfergusonsmart.com (accessed 2026-09-14). Supports the living-documentation camp's argument against post-hoc reports, and its own regulated-context carve-out ("[Traditional test reports] force us to think in terms of tests that happen only post-implementation."; "Of course there are some exceptions to this rule. For example in regulated environments, living documentation will often be more exhaustive and detailed."). A named, argued position in a live debate, not a neutral finding. [practitioner]

<a id="ref-39"></a>[39] Martin Fowler. "[Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html)." martinfowler.com (rewritten January 2024; accessed 2026-09-14). Supports the always-on visibility that displaced the compiled end-of-cycle status document ("CI Services have dashboards that allow everyone to see the state of any builds they are running."; "As well as the current state of the build, these displays can show useful information about recent history."). Describes current-state and recent-history visibility, which is precisely not a durable point-in-time artifact. [practitioner]

<a id="ref-40"></a>[40] Carl Nygard. "[Compliance in a DevOps Culture](https://martinfowler.com/articles/devops-compliance.html)." martinfowler.com (published November 2021; accessed 2026-09-14). Supports the displacement mechanism for compliance-style reporting, and the one thing that still gets written down ("Auditing the process also becomes a straightforward review of the logs of the deployment step."; "Each application has its own set of exceptions to the master list of controls, managed jointly by the team and the Office of Compliance."). Describes a target-state pattern the author advocates, not a universal empirical finding. [practitioner]

<a id="ref-41"></a>[41] TestRail. "[How to Write a Test Summary Report: Template and Real Examples](https://www.testrail.com/blog/test-summary-report/)." TestRail (accessed 2026-09-14). Supports the progress-versus-completion boundary and the threshold at which a formal report earns its cost ("A test progress report communicates the status of testing while testing is still underway. A test completion or summary report communicates the outcome of a completed testing effort or significant testing milestone."; "A formal test summary becomes useful when teams need to share testing results beyond a single iteration or the immediate team. It's also useful for supporting external requirements, such as audits, customer sign-offs, regulatory reviews, and contractual obligations."). The vendor sells test-management and reporting tooling and has a commercial interest in the artifact's relevance. [vendor]

<a id="ref-42"></a>[42] Inimfon Willie, for Tricentis. "[What is a test summary report and how do you write one?](https://www.tricentis.com/learn/test-summary-report)." Tricentis (accessed 2026-09-14). Supports the vendor how-to's recommendation content, quoted in this companion as the weakest evidential tier for a release verdict rather than as the basis for one ("A test summary report (TSR) is a document that explains what was tested, what passed, what failed, and how the application meets - or falls short of - the defined release goals."; "Summary and recommendations. Give a final view of the application's health. Highlight any blockers, critical concerns, and readiness for release. Include clear next steps."). Vendor content whose framing is rhetorically stronger than the standards and primary sources support. [vendor]

<a id="ref-43"></a>[43] TestRail (Gurock/Idera) Support Center. "[Runs (Summary) report](https://support.testrail.com/hc/en-us/articles/9444425638292-Runs-Summary-report)." TestRail (accessed 2026-09-14). Supports that a tool's "report", despite the name, is entirely computed, with no narrative or evaluation field ("The Run (Summary) report provides a high-level overview of all progress and testing activity for one or more test runs in your TestRail project."; "Forecast & Estimates give users a side-by-side hours estimate of progress, breaking down more details about completion ratios..."). [vendor]

<a id="ref-44"></a>[44] Jenkins project. "[JUnit plugin](https://plugins.jenkins.io/junit/)." Jenkins (accessed 2026-09-14). Supports that the plugin's output is visualization of XML result data with no narrative feature ("consumes XML test reports generated during the builds and provides some graphical visualization of the historical test results"). [vendor]

<a id="ref-45"></a>[45] Microsoft. "[Track test status in Azure Test Plans](https://learn.microsoft.com/en-us/azure/devops/test/track-test-status?view=azure-devops)." Azure DevOps documentation (accessed 2026-09-14). Supports that Azure's test status tracking is chart and widget construction over test-point outcome data, with no document output ("Use test results charts to track how your testing is going. Choose from a fixed set of prepopulated fields related to results."; "Pin a chart to your team's dashboard for all the team to view."). [vendor]

<a id="ref-46"></a>[46] Xray (Idera/Getxray). "[Reporting using Gadgets](https://getxraydocs.atlassian.net/wiki/spaces/XRAYCLOUD/pages/44566250)." Xray Cloud Documentation (accessed 2026-09-14). Supports that dashboard gadgets are explicitly framed by their own vendor as inputs to a release-readiness judgment rather than the judgment itself ("Monitor project health and readiness for release."; "Summarizes Test results (e.g., PASSED, FAILED, BLOCKED) across the project. Offers a high-level snapshot of Test outcomes, helping stakeholders evaluate project health and readiness for release."). [vendor]

<a id="ref-47"></a>[47] Xray (Idera/Getxray). "[Document Generator](https://getxraydocs.atlassian.net/wiki/display/XRAYCLOUD/Document+Generator)." Xray Cloud Documentation (accessed 2026-09-14). Supports that the one tool feature in this research that emits a document rather than a dashboard is template mail-merge over existing field values ("is a feature that allows you to create customized templates and generate documents based on your Jira data, including Xray Issues, Requirements, and Defects."; "Templates (Figure 3) are documents in DOCX (Microsoft Word) or XLSX (Microsoft Excel) formats."). [vendor]

<a id="ref-48"></a>[48] CSG Government Solutions, Inc. (IV&V contractor to the State of Rhode Island). "[UAT Summary Report - Phase 2 Cycle 3 and Cycle 4, Rhode Island Unified Health Infrastructure Project](https://transparency.ri.gov/uhip/documents/legislative-reports/status-reports/UAT%20Summary%20Report%20-%20Release%207%20Cycle3_4.pdf)." State of Rhode Island transparency portal (dated 2016-10-14; accessed 2026-09-14). The one actual filled test summary report in this research. Supports its real section list (Introduction, Internet Browsers, Executive Summary, Overview, Test Case Execution Results, Defect Reporting including defects by root cause, Issues Encountered, UAT Results Mapped to Exit Criteria, Recommendations), its variance disclosure ("The below functionality was either not tested or only partially tested."), its sign-off note ("There was no formal sign off; however, verbal agreement was obtained during the UAT Exit meeting.") and the customer-stated release rule ("It is the State's expectation to not go-live with any high or critical defects."). **It carries no dedicated go/no-go section and no system build or version number anywhere**, both of which this companion cites it for. Version 1.0/Draft; an IV&V contractor's assessment of the State's UAT, not the testing team's own report. [primary]

<a id="ref-49"></a>[49] Library of Congress, Office of the Chief Information Officer. "[Test Results and Analysis Report Template](https://www.loc.gov/static/portals/about/doing-business-with-the-library/documents/Test_Results_and_Analysis_Report_Template.doc)." Library of Congress (Version 1.1, dated 09/2015; accessed 2026-09-14). A real, unfilled US federal government test-report template, read in full. Supports its section list (Introduction/Purpose, Test Summary, Test Assessment, Test Results with a per-test-type "Severity of Defect" column, Recommendations, References, Key Terms) and its instructions ("Enter a comprehensive assessment of your interpretation of how adequate the test was in light of how thorough the test plan said it should be? What wasn't tested well enough?"; "Summarize the test results. Include a detailed description of any deviations from the original test plan, design, test case, or expected results."; "Describe what actions are suggested upon completion of this test. Provide any recommended improvements in the design, operation, or future testing of the business product that resulted from the testing being reported."). [primary]

<a id="ref-50"></a>[50] Experimentus Ltd. "[iTM Test Completion Report (Template)](https://www.experimentus.com/itm/04_Test_Completion_Report_Template.pdf)." Experimentus (iTM v6.0, dated 2017-03-03; accessed 2026-09-14). A UK testing consultancy's published completion-report template, with the clearest explicit proceed language found anywhere in this research ("Based on the results of product risk mitigation activities outlined above and the final summary of KPI results, our recommendation is to <proceed/not proceed>."; "Briefly describe any KPIs not achieved and the resulting residual risks."; "Describe any variance from the planned scope of testing"). Table of contents and sections 1 to 2 read in full; **pages 6 to 12 of the published PDF render blank, a confirmed defect in the published file**, so its defect-severity and entry/exit-criteria content could not be read. [vendor]

<a id="ref-51"></a>[51] iBeta Quality Assurance (an EAC-accredited Voting System Test Laboratory), submitted to the U.S. Election Assistance Commission. "[Dominion Voting Systems Sequoia WinEDS 4.0 - VSTL Certification Test Report (v2.0)](https://www.eac.gov/sites/default/files/voting_system/files/VSTL%20WinEDS%204.0%20Test%20Report%20v2.0%20package.pdf)." U.S. EAC (accessed 2026-09-14). A real filled certification test report. Supports the scope caveat ("Test Results in this report apply to the voting system configuration tested. Testing of voting systems that have been modified may or may not produce the same test results."), the named exclusions list ("The following functions are excluded from the WinEDS 4.0 voting system and therefore not tested in this certification effort"), the mandatory-explanation disposition rule ("Requirements marked Reject, NA, Pending or Out of Scope shall include an explanatory note.") and the naming of subcontracted testing outside the lab's accreditation scope. This is v2.0 submitted to the EAC and pending acceptance; the appendix carrying a final certification number was not read. [primary]

<a id="ref-52"></a>[52] Communications Security Establishment Canada, Canadian Common Criteria Evaluation and Certification Scheme. "[Certification Report: EAL 3+ Evaluation of Extreme Networks ExtremeXOS Network Operating System v12.3.6.2](https://www.commoncriteriaportal.org/files/epfiles/383-4-146%20CR%20v1.0e.pdf)." Common Criteria Portal (dated 2012-03-28; accessed 2026-09-14). A real filled certification report. Supports the explicit non-endorsement disclaimer ("This report, and its associated certificate, are not an endorsement of the IT product by the Communications Security Establishment Canada"), the threat-model scope boundary distinct from the pass verdict ("EXOS is not intended for situations which involve determined attempts by hostile or well-funded attackers using sophisticated attack techniques.") and the public-summary-over-private-evidence structure ("The ETR is a CCS document that contains information proprietary to the developer and/or the evaluator, and is not releasable for public review."). Applies only to the named version in its evaluated configuration. [primary]

<a id="ref-53"></a>[53] United Orthopedic Corporation (submitter), with the U.S. Food and Drug Administration, Center for Devices and Radiological Health (clearance letter). "[510(k) Summary of Safety and Effectiveness Data - UTF Stem, reduced, #0, #00 (K163193)](https://www.accessdata.fda.gov/cdrh_docs/pdf16/K163193.pdf)." FDA (clearance letter dated 2017-06-08; accessed 2026-09-14). The floor case in this research's corpus: a minimal report still required to state an absence affirmatively ("Clinical Performance Data/Information: None provided as a basis for substantial equivalence."). Applies to one size-extension device via predicate comparison, not independent clinical evidence. [primary]

<a id="ref-54"></a>[54] U.S. Food and Drug Administration, Center for Devices and Radiological Health. "[Content of Premarket Submissions for Device Software Functions](https://www.fda.gov/media/153781/download)." FDA (issued 2023-06-14; accessed 2026-09-14). The most rigorous residual-risk disclosure structure found in this research, and the source of this bundle's version-tested and unresolved-anomaly guidance ("The summary description should include the software version tested and the overall pass/fail test results for all test protocols"; "The system level test report should demonstrate that the protocol has been acceptably executed with passing test results and any unresolved anomalies have been acceptably deferred based on a risk assessment for the candidate release version."; "Risk-based rationale for not correcting or fixing the anomaly in alignment with the sponsor's risk management plan or procedure(s)."). Marked "Contains Nonbinding Recommendations" by the FDA, though guidance of this kind functions as a de facto requirement for submissions. [primary]

<a id="ref-55"></a>[55] Trail of Bits, prepared for the Kubernetes Security Working Group. "[Kubernetes Security Assessment](https://raw.githubusercontent.com/magnologan/cncf-security-audits/main/K8s/Kubernetes%20Final%20Report.pdf)." Trail of Bits (assessed Kubernetes v1.13.4, May 2019; accessed 2026-09-14). Supports the breadth-versus-depth coverage disclosure ("Due to the scope of the assessment and size of the codebase, bug finding was focused on identifying component implementations which were 'obviously wrong.' Given this focus, codebase coverage emphasized breadth instead of depth. Portions of the codebase outside of the control areas received minimal to no coverage.") and "Undetermined" as a first-class severity value ("Undetermined: The extent of the risk was not determined during this engagement."). A commissioned third-party security assessment rather than a release-qualification test report; it stands in for the open-source domain only loosely. [practitioner]

<a id="ref-56"></a>[56] Apache Software Foundation / Apache CloudStack project (page credited to wiki user "Sudhap"). "[QA - 4.2 Test Execution Results](https://cwiki.apache.org/confluence/spaces/CLOUDSTACK/pages/30756550/QA+-+4.2+Test+Execution+Results)." Apache CloudStack wiki (dated 2013-09-08; accessed 2026-09-14). The one open-source release-QA artifact found: a live wiki dashboard rather than a narrative document ("Planned Vs Actual Test Execution Report:"; "Current Defect Status:"; "Weekly Defect Incoming Report:"). The page is essentially a set of chart captions with no narrative prose beneath them, which is the point it is cited for. [primary]

<a id="ref-57"></a>[57] John Watkins and Simon Mills. "[Test Summary Report Template (Appendix J), in *Testing IT: An Off-the-Shelf Software Testing Process*](https://www.cambridge.org/core/books/testing-it/test-summary-report-template/EE7D4E42A47750DCEB17FAC30A0313AE)." Cambridge University Press, 2010 (online 2011; accessed 2026-09-14). Supports that an academic-press book devotes a full appendix to a reusable template, and its framing of the document's purpose ("The purpose of a test summary report is to summarize the result of a particular testing phase and to provide the basis for subsequent improvement of the testing process."; "each testing project must generate a test summary report as one of the documents produced at the conclusion of any given testing phase."). **The appendix's own section list sits behind Cambridge Core and was not read**; only the framing text on the abstract page was verified. [academic]

<a id="ref-58"></a>[58] United States Air Force, 412th Test Wing, Office of the Technical Director (per DTIC search-index title only). "[Test Report Author's Guide](https://apps.dtic.mil/sti/pdfs/AD1188696.pdf)." Defense Technical Information Center (checked 2026-09-14). **NOT RETRIEVED: every attempt, by direct fetch and by browser-emulated fetch, returned DTIC's bot-blocking page ("The request is blocked"), not the document.** Recorded here so the defense test-and-evaluation domain is visibly a gap rather than silently absent; a second candidate in that domain, DOT&E, was searched twice and returned zero documents, which is logged as a null result in [`test-summary-report_research-log.md`](test-summary-report_research-log.md). No content from this source is used anywhere in this bundle. [primary]
