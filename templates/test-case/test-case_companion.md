# Companion: The Test Case

> The deep explainer for the test-case bundle. Read this to understand what a test case is, where it came
> from, why it is shaped the way it is, and where practitioners disagree about it. Two named schools of
> testing disagree about whether this document should exist at all, and section 6 gives both their strongest
> form. The short operator card is [`test-case_guide.md`](test-case_guide.md); a fully worked instance is
> [`test-case_example.md`](test-case_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A test case is **the specification of one verification**: what must be true before it runs, what is done, and
what must happen as a result. The vocabulary standard puts it as *"a specification of the inputs, execution
conditions, testing procedure, and expected results that define a single test to be executed to achieve a
particular software testing objective"* [[8]](#ref-8). The two phrases doing the work there are **single test**
and **a particular objective**.

**At a glance**
- It verifies **one thing**, and says which thing, so a failure points somewhere specific [[8]](#ref-8).
- Its **preconditions** are what let someone who is not its author run it and get the same answer
  [[11]](#ref-11).
- Its **expected results are written before it runs**. Filled in afterwards, they are not expectations
  [[16]](#ref-16).
- It is a **design artifact**. Actual result, status and run date belong to an execution record, not here
  [[38]](#ref-38).
- It **traces** to something: an acceptance criterion, a requirement, a risk [[41]](#ref-41).

If you read nothing else: a test case is a question you have decided to ask of the system, written so that
someone else can ask it the same way tomorrow.

**The honest first thing to know** is that this artifact is genuinely contested. One tradition treats test
cases as the primary deliverable of testing; another argues that writing them in detail deskills testers and
crowds out the work that finds real problems. Michael Bolton's formulation is the sharpest: *"The test case is
not the test. The test is what you think and what you do."* [[32]](#ref-32) This bundle takes that seriously
rather than dismissing it, and section 6 sets out both cases.

**The second thing to know is a vocabulary warning**, because the received taxonomy is not what the ISTQB
glossary appears to say. On the community mirrors read for this bundle, **test procedure** and **test script**
carry word-for-word identical definitions [[7]](#ref-7), and **test scenario** is defined as a synonym for
test script [[37]](#ref-37) rather than the high-level "what to test" that most practitioners mean by it. (The
official glossary blocks automated retrieval and was not read; see section 2.) If your team
uses these words as though they were a clean hierarchy, you are using a folk taxonomy. That is fine, as long
as everyone uses the same one; section 8 sets out both.

## 2. Origins and evolution

Test documentation was standardized long before agile. **IEEE 829** went through three editions, in 1983, 1998
and 2008 [[1]](#ref-1), and defined a family of documents in which the test case specification was one member.
It is now a **superseded standard** [[1]](#ref-1).

The most useful thing to know about 829 is not its structure but its gap. As Wikipedia's summary of the
standard records: *"the standard specified the format of these documents, but did not stipulate whether they
must all be produced, nor did it include any criteria regarding adequate content"* [[2]](#ref-2). It said what
the form looked like and nothing about what filling it in well meant. **Every template descended from it
inherits that gap**, and closing it is most of what the guidance in this bundle is for.

**ISO/IEC/IEEE 29119** replaced it, developed from 2007, first published in 2013 and revised in 2021
[[4]](#ref-4). Part 3, the documentation part, introduced something 829 lacked: a tiering of content items
into mandatory, recommended and possible [[9]](#ref-9), which is at least a partial answer to "which of these
fields do I actually need?"

**A disclosure, because it changes how you should read the rest of this section.** 29119-3 is paywalled and
**was not read** in the research behind this bundle [[3]](#ref-3). Nothing here reports its internal
structure or its normative field list. Where this companion describes a field set, it is describing what the
vocabulary standard defines [[8]](#ref-8), what practitioner research finds valuable [[11]](#ref-11), and what
tools actually require [[38]](#ref-38)[[40]](#ref-40) - not what any paywalled standard mandates.

## 3. Anatomy (section by section)

The full variant carries eight sections; the lean variant carries the first four, unchanged in name and order.

### Identification and Traceability

A stable identifier, a title that says what is being verified, what the case traces to, and its priority.

The identifier matters because a test case is referenced from elsewhere: from a run, from a defect, from a
coverage report. The **traceability** matters more. A traceability matrix exists to *"ensure that all the
requirements established for a testing project are mapped to corresponding tests"* [[41]](#ref-41), and in
audited contexts it is not optional. One account of regulated practice puts the bar at *"Full traceability
via linkage of all tests to corresponding requirement artifacts"* [[35]](#ref-35).

Trace to whatever your context actually has: an acceptance criterion, a requirement ID, a risk in the test
plan, or a defect this case now guards against. **A case that traces to nothing is a case nobody can decide to
delete**, which is how suites become landfill.

The title should name the behavior and the condition, not the click path. "Restricted viewer cannot see
out-of-entitlement rows through a shared view" survives a UI redesign; "Click Views menu, click share" does
not.

### Preconditions and Test Data

The system state, configuration, accounts and data that must exist before the first step, and the specific
data this case uses.

This is the section that decides whether anyone but the author can run the case. Practitioner research on
test-case quality ranks understandability first and describes it concretely as a *"straightforward,
understandable description, clear steps, clear objective, clear precondition"*, with repeatability - the
ability to *"run any time, tested repeatedly"* - close behind [[11]](#ref-11). Vendor guidance says the same
in operational terms: *"Specify required system state, configurations, or dependencies before execution"*
[[16]](#ref-16).

Keep preconditions and test data distinguishable even if you put them together. Preconditions are the state
of the world; test data are the values this case feeds in. Parameterizing a case over its data is
straightforward; parameterizing it over its preconditions usually is not, which is the practical reason to
keep the two separable.

### Steps and Expected Results

The actions, in order, each paired with what should happen.

The pairing is the point. A tool's data model puts it plainly: a test step is *"An individual action within a
test case, consisting of an Action (what the tester does) and an Expected Result (the anticipated behavior)"*
[[38]](#ref-38). A step with no expected result is not a verification, it is navigation.

**Write expected results before execution.** The instruction is to *"Define the measurable outcome that should
occur after the steps are executed"* [[16]](#ref-16) - and "should" is doing the work. An expected result
filled in after the run is a description of what happened, which cannot fail.

**How much detail?** This is genuinely contested and section 6 covers the argument. The practical middle: give
enough that a competent tester unfamiliar with the feature can execute it, and no more. Even vendor guidance
warns against over-specifying procedural detail [[15]](#ref-15), and the same practitioner study that ranks
understandability first also records simplicity - cases that do not bundle several verifications together -
among the attributes participants valued [[11]](#ref-11).

**One objective, not one assertion.** A case should be atomic in purpose: *"Each test should be self-contained
and not rely on the success or failure of other tests."* [[17]](#ref-17) A single outcome may still need
several checks to confirm it, and that is fine. What is not fine is a case that verifies three unrelated
things, because its failure tells you almost nothing.

### Postconditions and Teardown

The state the system is left in, and anything that must be cleaned up.

Both ISTQB definitions of a test case include postconditions [[5]](#ref-5)[[6]](#ref-6), and there is a
practical reason: a suite is defined as a set of cases *"where the post condition of one test is often used as
the precondition for the next one"* [[37]](#ref-37). A case that leaves state behind quietly becomes a
dependency for whatever runs next, which is a common cause of tests that pass alone and fail in a
suite.

If the case leaves no residue, say so in one line rather than deleting the section. "No state change; read-only"
is information.

### Design Rationale (full variant only)

Which technique produced this case, and why these values rather than others.

This is what makes a case reviewable rather than merely runnable. The canonical black-box techniques are the
vocabulary here: **equivalence partitioning**, which *"divides data into partitions (known as equivalence
partitions) based on the expectation that all elements of a given partition are processed the same way"*;
**boundary value analysis**, *"a test technique based on exercising the boundaries of equivalence partitions"*;
and **decision tables**, which *"are used for testing requirements that specify how different combinations of
conditions result in different outcomes"* [[10]](#ref-10). For cases with many interacting parameters,
combinatorial testing targets *"elusive failures that occur only when multiple components interact"*, and its
pairwise form guarantees that *"All possible pairs of parameter values are covered by at least one test"*
[[14]](#ref-14).

**Two attribution notes**, because both errors are common. Glenford Myers' *The Art of Software Testing* (1979)
is the source that systematized partitioning and boundary analysis for software, and the heuristic everyone
repeats - *"Test cases that explore boundary conditions have a higher payoff than cases that do not"* - traces
to it [[13]](#ref-13). Calling him their **inventor** overstates it; the research behind this bundle did not
establish who originated equivalence classes as a concept, so it makes no claim about that either way. And on
a strict reading, **boundary value analysis presupposes partitioning**: testing boundaries without first
establishing the partitions they bound is not the technique Myers described [[13]](#ref-13), though standard
teaching presents the two as separately applicable [[10]](#ref-10).

### Environment and Configuration (full variant only)

The environment, build, browser or device matrix, and configuration this case is valid for.

Lean cases omit this because the team has one environment and knows it. It earns its place when a case is
valid only under a configuration, when a matrix must be covered, or when an auditor will ask where the
evidence came from.

### Automation Status (full variant only)

Whether this case is automated, and what it is linked to.

Automation changes the case's role rather than retiring it. In one tool, the automation status field simply
records whether an automated method is associated, and **a method may serve several cases but a case may have
only one method** [[39]](#ref-39). There is also a trap worth writing into the template: *"Test case parameters
are for manual test iterations only. Automated tests don't use parameters defined on the test case work
item."* [[39]](#ref-39) Teams that parameterize a manual case and then automate it are frequently surprised.

### Version and Approval (full variant only)

The version of the case, who reviewed it, and when.

This exists for regulated and audited work, where the test case is evidence. The bar applies regardless of
authorship: *"The bar doesn't lower just because a machine wrote it, either. AI-generated test cases must also
be version-controlled and traceable."* [[35]](#ref-35) Everywhere else, delete this section and let version
control do its job.

## 4. Variants and sizing

**Lean (four sections)** is the default, and it should stay the default. A test case is written many times over
a project, so every field you add is paid for hundreds of times. Lean carries Identification and Traceability,
Preconditions and Test Data, Steps and Expected Results, and Postconditions and Teardown.

**Full (eight sections)** adds Design Rationale, Environment and Configuration, Automation Status, and Version
and Approval. Use it when the work is regulated or audited [[35]](#ref-35), when cases are reviewed as
artifacts rather than just executed, when a configuration matrix is in play, or when a suite is large enough
that knowing *why* a case exists is what lets you delete it later.

**A note on the catalog.** The master catalog marks this type single-size. This bundle ships two weights
anyway, on the same grounds that corrected the ADR entry (finding EC-2 in `STATE.md`): the regulated case for
design rationale, versioning and approval is documented [[35]](#ref-35), and it is a genuinely different weight
of document from a case a developer writes in five minutes. The catalog's size calls are hypotheses, and this
is one more of them tested against evidence.

**Choosing by role, not just by context.** Practitioner research found that different roles want different
things from the same document: those executing cases prioritized understandability and completeness, while
those maintaining the suite prioritized traceability and maintainability [[11]](#ref-11). That study is six
practitioners at one company and proves nothing on its own, but the tension it names is real and a template
cannot resolve it by picking a side. Lean serves the executor; full serves the architect and the auditor.

## 5. Methodology lineage

**The standards tradition** treats the test case as the unit of planned verification, derived from a
specification by a named technique [[10]](#ref-10) and traceable to a requirement [[41]](#ref-41). This is the
lineage that produces test management tools and coverage matrices.

**The context-driven school** rejects the primacy of the artifact. Its founding principles are that *"The
value of any practice depends on its context"* and *"There are good practices in context, but there are no
best practices"* [[29]](#ref-29). Its position on test cases specifically is section 6.

**The BDD and specification-by-example tradition** proposes a third path: write the example once, in a form
both the business and the machine can read, and stop maintaining separate specifications and tests. Dan
North's original claim is the strongest statement of it: *"A story's behaviour is simply its acceptance
criteria: if the system fulfils all the acceptance criteria, it's behaving correctly."* [[18]](#ref-18), with
the familiar formulation *"Given some initial context (the givens), When an event occurs, Then ensure some
outcomes."* [[18]](#ref-18) Cucumber's creator frames the intent as design rather than verification: *"BDD and
TDD are not about testing existing code. They are about designing a code that hasn't yet been written."*
[[28]](#ref-28) Gojko Adzic's *Specification by Example* (2011) extended this into living documentation
[[24]](#ref-24), and ATDD's canonical framing keeps the purpose in view as *"facilitating conversation between
developers and product owners about product requirements"* [[22]](#ref-22).

**Dates, carefully, because this lineage is routinely misdated.** JBehave began in 2003 and the "Introducing
BDD" article appeared in 2006 [[20]](#ref-20)[[18]](#ref-18). **Gherkin is a 2008 name**, coined when Cucumber
was released as a rewrite of RSpec's Story Runner [[21]](#ref-21). The frequently repeated claim that
Given/When/Then was formalized in 2004 could not be verified from any source read here, and this bundle does
not assert it.

**The exploratory tradition** replaces the pre-written case with a chartered session. The balanced reference
statement is that exploratory skills *"will be deployed more effectively in the exploratory style on an Agile
team, as this style is more consistent with an Agile approach than the 'scripted testing' style"*
[[36]](#ref-36) - a preference, note, not a prohibition.

## 6. Debates and contested boundaries

### Do detailed test cases help or harm?

**The case against.** James Bach's objection is not to documentation as such but to what it displaces:
*"But documenting is not testing. It is one of the chief distractions to testing."* And the sharper form,
which is an empirical claim rather than a philosophical one: *"certain kinds of testing isn't done at all just
because it is hard to document (exploratory testing and complex scenario tests often fall in this
category)."* [[30]](#ref-30) A decade later he put the principle as *"Testing is a performance, not an
artifact."* [[31]](#ref-31) Michael Bolton's essay is the most quotable version: *"The test case is not the
test. The test is what you think and what you do."*, and by analogy, *"A recipe is not cooking. An itinerary is
not a trip. A score is not a musical performance, and a file of PowerPoint slides is not a conference talk."*
[[32]](#ref-32) The practical charge is that step-by-step scripts ask a skilled tester to behave like a machine.

Two honest qualifiers. Bach's characterization of the opposing school is written by an opponent, not a neutral
observer. And Bolton's conclusion is not that the artifact is worthless: *"The test case may have a role, but
you, the tester, are at the centre of your testing."* [[32]](#ref-32)

**The case for.** The strongest argument is not philosophical but regulatory. In audited domains, linking every
requirement to its test is a condition of shipping, not a preference [[35]](#ref-35). Beyond compliance,
written cases give repeatability across testers of varying experience, a basis for review, and a way to
onboard. Kaner's framing dissolves some of the argument: what makes a case good depends on the objective it
serves [[12]](#ref-12), which is the first context-driven principle applied to the artifact its own school is
most sceptical of [[29]](#ref-29).

**Where this bundle stands.** With context, explicitly. A pacemaker firmware team omitting traceable cases has
a regulatory problem; a two-person startup writing three hundred scripted cases for a CRUD app has a different
one. The template is a scaffold for the cases you decide to write, and the guide says which sections to drop.

### Do acceptance criteria make test cases redundant?

This is the sharpest boundary in the qa-docs family, and it is unresolved.

**The unification camp** says the two are the same artifact seen twice. North's claim is above [[18]](#ref-18).
Andy Knight puts the practitioner form as *"behavior scenarios are more than tests - they also represent
requirements and acceptance criteria"*, with a rule that echoes test-case atomicity exactly: *"One Scenario,
One Behavior!"* [[26]](#ref-26). The clearest statement of the merge position comes from a test lead: *"Based
on all the definitions above, there's not a huge difference(if any) between test cases and acceptance
criteria."*, therefore *"If we already have testable ACs, why should we duplicate work in creating TCs for the
same scenarios?"* [[25]](#ref-25)

**The coverage camp** answers that acceptance criteria stop where agreement stops. A product owner accepting
"a user can share a view" has agreed to a behavior; they have not agreed to what happens when the recipient's
entitlement is revoked mid-session, when the filter value contains ten thousand characters, or when a defect
from March recurs. Negative paths, boundaries, regression cases accumulated from defect history, and
non-functional checks are test design, not acceptance. **The strength of this argument scales with risk**: for
low-risk internal tooling the merge is pragmatic, and for anything where a failure is expensive it is not.

**Two pieces of evidence worth weighing.** Martin Fowler describes Given/When/Then as *"a style of representing
tests - or as its advocates would say - specifying a system's behavior using SpecificationByExample"*
[[19]](#ref-19) - and the hedge is deliberate, marking the specification framing as an advocate's claim rather
than a settled fact. And Adzic, ten years after proposing the unification, reported that it largely had not
happened; the community's own summary of what mattered turned out to be that *"conversations are more important
than capturing conversations is more important than automating conversations"*, with living documentation still
*"a yet unrealized key benefit for large organizations"* [[23]](#ref-23).

**The resolution this bundle recommends**, offered as a judgment rather than a finding: write criteria
collaboratively with a tester in the room so the criteria get better, then treat test design as the activity
that exhausts what the criteria imply. The criterion is the contract; the case is how you find out whether the contract holds
under conditions nobody discussed.

Whatever you choose, do not adopt Gherkin as a file format and believe the question is answered. Knight warns
that mechanically converting old manual cases into scenarios produces scenarios that are no more
comprehensible than the cases were, with automation code to maintain on top of them [[27]](#ref-27).

### Is counting test cases ever useful?

No, and this is the one thing both camps agree on. A metrics analysis lists it among vanity metrics outright:
*"Number of test cases. 'We have 5,000 tests' tells you nothing. A team with 500 focused tests beats 5,000
trivial ones."* [[34]](#ref-34) And when the count becomes a target the mechanism is predictable: *"One hundred
percent coverage of shallow checks outscores eighty percent coverage of risky paths."*, at which point *"you are
no longer observing your process, but rather measuring your people's creativity in defeating the
observation."* [[33]](#ref-33) The context-driven principles reach the same place from the other direction:
*"Metrics that are not valid are dangerous."* [[29]](#ref-29)

## 7. Anti-patterns and failure modes

**The case that can only be run once.** An "actual result" and a "status" field baked into the specification,
so the reusable artifact and the record of one run are the same file. Vendor templates encourage this
[[16]](#ref-16), and tools that get it right keep them apart: the case is the specification, and *"Test result:
The recorded outcome of a single test case execution within a test run."* [[38]](#ref-38) Fix: keep execution
state in the tool or the run record.

**Expected results written after the fact.** They cannot fail, so the case verifies nothing [[16]](#ref-16).

**The case that verifies three things.** One failure, no information about which of the three broke. Fix: one
objective per case [[17]](#ref-17).

**Order dependence.** A case that only passes if another ran first, usually because a predecessor left state
behind [[37]](#ref-37). Fix: real preconditions and real teardown.

**Over-specification.** Every click enumerated, so the case breaks on a UI change that broke nothing. Even
vendor guidance warns about this [[15]](#ref-15). Fix: specify behavior and data, not the path.

**Under-specification.** "Log in and check it works." Not repeatable by anyone but the author, which is exactly
what the quality research ranks first among the things testers value [[11]](#ref-11).

**The untraceable case.** Traces to nothing, so nobody can tell whether it still matters, and it is never
deleted [[41]](#ref-41). Fix: every case names what it covers.

**Counting cases as progress.** Covered above; it converts a coverage question into a production quota
[[34]](#ref-34)[[33]](#ref-33).

**Documenting instead of testing.** The failure the critics name: the day is spent producing artifacts, and the
testing that is hard to write down never happens [[30]](#ref-30).

## 8. Relationships to other artifacts

**Test case and acceptance criteria.** Different altitude, different author, different moment. Criteria are
agreed with the business before the work and say what must be true; a case is designed by whoever tests and
says how you find out, including under conditions nobody agreed to. See section 6 for the argument that they
are the same artifact [[25]](#ref-25), which is a real position held by real practitioners.

**Test case and test plan.** The plan scopes and ranks; the case is the unit the plan schedules. The plan
should never contain cases, and the case should not restate the plan's risk reasoning beyond a traceability
reference.

**Test case and bug report.** Opposite directions in time: *"Bug reports are reactive, created after
discovering a problem in existing software. Test cases are proactive, written 'before or during development'
to define correct behavior."* [[42]](#ref-42) A failing case is often what produces a report, and a closed
defect frequently produces a new regression case pointing back at it.

**Test case, test suite and test run.** A suite is *"A set of several test cases for a component or system
under test, where the post condition of one test is often used as the precondition for the next one."*, and a
run is *"The execution of a test suite on a specific version of the test object."* [[37]](#ref-37) The case is
the specification; the run is the event.

**Test case, test procedure, test script and test scenario: the vocabulary trap.** On the ISTQB glossary
mirrors read for this bundle, **test procedure and test script have identical definitions**, both *"A sequence of test cases in
execution order, and any associated actions that may be required to set up the initial preconditions and any
wrap up activities post execution."* [[7]](#ref-7). A **test procedure specification** is separately defined as
*"A document specifying a sequence of actions for the execution of a test. Also known as test script or manual
test script."* [[7]](#ref-7). And **test scenario** is given the same definition as test script
[[37]](#ref-37), which flatly contradicts the common practitioner usage in which a scenario is a high-level
statement of what to test and a case is the detailed how. Both readings are in daily use. The practical advice
is not to adopt one and correct everyone else, but to write down which your team means, because the words will
not settle it for you.

**Test case and the tool.** Tools model a case as a work item that is not itself executable: *"Test cases by
themselves aren't executable. When you add a test case to a test suite, you generate test points."*
[[38]](#ref-38) They also require far less than any standard suggests. One tool's only mandatory field on the
work item is a title [[38]](#ref-38); another requires a name and a set of properties [[40]](#ref-40). As with
the test plan, the tool's minimum is not the artifact's minimum, and the fields that make a case reusable are
mostly the ones the tool does not force.

**Test case and automation.** Automating a case does not delete it; it changes what the case is for. The status
field records the link, one automated method can serve several cases but not the reverse, and manual
parameters do not carry into automation [[39]](#ref-39). The BDD tradition offers the alternative of writing the
specification once in an executable form [[26]](#ref-26), with the caveat in section 6.

**Within the qa-docs family.** The plan says what will be verified and how deeply; this document specifies one
of those verifications; the bug report records one that failed. The three chain on one feature, and this
member is where the family's boundary with `delivery-docs` is drawn.

## 9. Adaptations

**Regulated and audited work** needs the full variant, and needs the Version and Approval section to be real
rather than decorative. Traceability from requirement to test is the audit's spine [[35]](#ref-35).

**Exploratory-heavy teams** should write few cases and write them for the things that must be re-verified
identically: regression guards, entitlement boundaries, calculations. Everything else goes into charters. This
is the context-driven position applied rather than argued [[29]](#ref-29), and it is compatible with this
template as long as the cases you do write are worth their maintenance.

**Automation-first teams** should treat the case as the specification and the code as the implementation of it,
resisting the temptation to convert existing manual cases mechanically [[27]](#ref-27).

**BDD teams** may find their Gherkin scenarios cover the agreed behaviors and use this template only for the
territory the scenarios do not reach: negative paths, boundaries, regression, and non-functional checks. That
is a legitimate division of labor.

**Teams with no test management tool** can keep cases in the repository beside the code, which makes the
version question answer itself and keeps traceability reviewable in a pull request.

**And the general rule** that governs all of these: what makes a case good depends on what it is for
[[12]](#ref-12).

## 10. Worked example

[`test-case_example.md`](test-case_example.md) is a full-variant case for the "Saved Views for Dashboards"
feature at the fictional Acme Analytics, continuing the thread from the
[PRD](../prd/prd_example.md), the [design document](../sdd/sdd_example.md), the
[acceptance criteria](../acceptance-criteria/acceptance-criteria_example.md) and the
[test plan](../test-plan/test-plan_example.md).

**The example was chosen to make section 6's argument concrete rather than to be typical.** It verifies that a
restricted viewer opening a shared view does not receive rows outside their entitlement - the highest-risk area
in the test plan, traceable to a program risk, and **traceable to no acceptance criterion at all**. Nobody
agreed to it, because nobody thought to. That is what "test design continues past the agreed criteria" means
when it stops being a slogan: the case exists because a tester asked what happens at a boundary the criteria
never mentioned.

---

## References

<a id="ref-1"></a>[1] IEEE Standards Association. "[IEEE 829-2008: IEEE Standard for Software and System Test Documentation](https://standards.ieee.org/ieee/829/3787/)." IEEE SA (accessed 2026-07-25). Supports the three editions of IEEE 829 (1983, 1998, 2008) and its current status ("Superseded Standard"). Note that "Superseded" is a distinct IEEE status from "Withdrawn" or "Inactive". [primary]

<a id="ref-2"></a>[2] Wikipedia contributors. "[Software test documentation](https://en.wikipedia.org/wiki/Software_test_documentation)." Wikipedia (accessed 2026-07-25). Supports the central limitation of IEEE 829 for a template author ("the standard specified the format of these documents, but did not stipulate whether they must all be produced, nor did it include any criteria regarding adequate content"). [reference]

<a id="ref-3"></a>[3] International Organization for Standardization. "[ISO/IEC/IEEE 29119-3:2021, Software and systems engineering - Software testing - Part 3: Test documentation](https://www.iso.org/standard/79429.html)." ISO (accessed 2026-07-25). Supports the existence and currency of the 2021 edition only. **Not read: the standard is paywalled**, and no claim in this bundle rests on its contents. [primary]

<a id="ref-4"></a>[4] Wikipedia contributors. "[ISO/IEC 29119](https://en.wikipedia.org/wiki/ISO/IEC_29119)." Wikipedia (accessed 2026-07-25). Supports the series timeline (development from 2007, first release 2013, revision 2021) and the predecessor standards it drew on. Used for timeline facts only. [reference]

<a id="ref-5"></a>[5] ISTQB. "[Test case](https://istqb-glossary.page/test-case/)." ISTQB Glossary, community mirror (accessed 2026-07-25). Supports the earlier ISTQB definition of a test case ("A set of input values, execution preconditions, expected results and execution postconditions, developed for a particular objective or test condition, such as to exercise a particular program path or to verify compliance with a specific requirement."). **A mirror, not the official glossary**, which blocked automated retrieval; no version date is shown on the page. [reference]

<a id="ref-6"></a>[6] missionwares.com. "[Test case](https://istqb.missionwares.com/glossary/test-case.html)." ISTQB Lexicon (accessed 2026-07-25). Supports the newer CTFL 4.0-aligned definition ("A set of preconditions, inputs, actions (where applicable), expected results and postconditions, developed based on test conditions."), which differs from [[5]](#ref-5) by naming actions and anchoring the case to test conditions. An aggregator; no glossary version number shown, and which of the two definitions is current could not be settled from an authoritative readable page. [reference]

<a id="ref-7"></a>[7] ISTQB. "[Test condition](https://istqb-glossary.page/test-condition/)." ISTQB Glossary, community mirror (accessed 2026-07-25). Supports the definitions of test condition, test procedure, test script and test procedure specification, and the fact that test procedure and test script carry identical definitions ("An item or event of a component or system that could be verified by one or more test cases, e.g., a function, transaction, feature, quality attribute, or structural element."; "A sequence of test cases in execution order, and any associated actions that may be required to set up the initial preconditions and any wrap up activities post execution."; "A document specifying a sequence of actions for the execution of a test. Also known as test script or manual test script."). Mirror pages; the vocabulary has changed across glossary versions. [reference]

<a id="ref-8"></a>[8] Wikipedia contributors. "[Test case (software)](https://en.wikipedia.org/wiki/Test_case_(software))." Wikipedia, citing ISO/IEC/IEEE 24765:2010 (accessed 2026-07-25). Supports the vocabulary-standard definition of a test case ("a specification of the inputs, execution conditions, testing procedure, and expected results that define a single test to be executed to achieve a particular software testing objective") and the field set in common use. **The vocabulary standard itself was not read**; the definition is attributed through this citation. [reference]

<a id="ref-9"></a>[9] microTOOL GmbH. "[Test Documentation with ISO/IEC/IEEE 29119-3:2021](https://www.microtool.de/en/document-management/test-documentation-with-iso-iec-ieee-29119-32021/)." microTOOL (accessed 2026-07-25). Supports that 29119-3 classifies content items as mandatory, recommended or possible, the tiering IEEE 829 lacked. Vendor content from a test documentation tool company; its author states they read the standard, which this project could not verify. [vendor]

<a id="ref-10"></a>[10] ASTQB / ISTQB. "[4.2 Black-Box Test Techniques](https://astqb.org/4-2-black-box-test-techniques/)." ISTQB Foundation Level Syllabus (accessed 2026-07-25). Supports the canonical definitions of the black-box design techniques ("Equivalence Partitioning divides data into partitions (known as equivalence partitions) based on the expectation that all elements of a given partition are processed the same way."; "Boundary Value Analysis is a test technique based on exercising the boundaries of equivalence partitions."; "Decision tables are used for testing requirements that specify how different combinations of conditions result in different outcomes."). Earlier syllabus versions listed a fifth technique. [primary]

<a id="ref-11"></a>[11] Lidström, Borg and colleagues. "[Test-case quality: understanding practitioners' perspectives](https://arxiv.org/html/2309.16801)." arXiv (accessed 2026-07-25). Supports the practitioner ranking of test-case quality attributes, with understandability first, and the finding that roles disagree about what matters ("straightforward, understandable description, clear steps, clear objective, clear precondition"; "run any time, tested repeatedly"). **Six practitioners at one company**: directionally useful, not statistically generalizable, and cited that way throughout. [primary]

<a id="ref-12"></a>[12] Cem Kaner. "[What Is a Good Test Case?](https://www.kaner.com/pdfs/GoodTest.pdf)" Florida Institute of Technology, presented at STAR East 2003 (accessed 2026-07-25). Supports the framing that test-case quality is relative to the objective the case serves. **The PDF was not read**; only the existence and central framing of the paper are claimed, and the framing is independently supported by [[29]](#ref-29). [practitioner]

<a id="ref-13"></a>[13] Mike Harris. "[A thought regarding boundary value analysis](https://testandanalysis.home.blog/2023/02/14/a-thought-regarding-boundary-value-analysis/)." TestAndAnalysis (published 2023-02-14; accessed 2026-07-25). Supports the attribution of equivalence partitioning and boundary value analysis to Myers' *The Art of Software Testing* (1979), the heuristic itself ("Test cases that explore boundary conditions have a higher payoff than cases that do not"), and the argument that BVA presupposes partitioning. **Myers' book was not read**; the quotation is Harris reproducing it. [practitioner]

<a id="ref-14"></a>[14] D. Richard Kuhn, Yu Lei and Raghu Kacker. "[Practical Combinatorial Testing: Beyond Pairwise](https://www.nist.gov/publications/practical-combinatorial-testing-beyond-pairwise)." NIST, published in IEEE IT Professional (2008; accessed 2026-07-25). Supports pairwise and t-way combinatorial testing and the failure class it targets ("All possible pairs of parameter values are covered by at least one test"; "elusive failures that occur only when multiple components interact"). Pairwise has roots in design of experiments; the NIST authors formalized and tooled it for software. [primary]

<a id="ref-15"></a>[15] SmartBear. "[Test Case Best Practices](https://smartbear.com/learn/test-management/test-case-best-practices/)." SmartBear (accessed 2026-07-25). Supports the mainstream position on independence, repeatability and traceability, and an explicit vendor warning against over-specification ("A test case is a set of conditions or variables under which a tester will determine whether a system under test satisfies requirements or works correctly."). No named author. [vendor]

<a id="ref-16"></a>[16] Torben Robertson. "[How to Write Test Cases](https://www.qase.io/blog/how-to-write-test-cases/)." Qase (accessed 2026-07-25). Supports the nine-field structure vendor tooling enforces, including the actual-result and status fields this companion argues do not belong in a specification, and the rule that expected results are defined before execution ("Define the measurable outcome that should occur after the steps are executed"; "Specify required system state, configurations, or dependencies before execution"). [vendor]

<a id="ref-17"></a>[17] BugBug. "[Atomic Test Cases: The Ultimate Guide](https://bugbug.io/blog/software-testing/atomic-test-cases-the-ultimate-guide/)." BugBug (accessed 2026-07-25). Supports the atomicity and independence principles in practice ("Each test should be self-contained and not rely on the success or failure of other tests."). Attributes atomicity to no named practitioner; the FIRST acronym often cited alongside it is commonly credited to Robert C. Martin, an attribution this research did not verify and this bundle does not make. [vendor]

<a id="ref-18"></a>[18] Dan North. "[Introducing BDD](https://dannorth.net/blog/introducing-bdd/)." dannorth.net (published in Better Software, March 2006; posted September 2006; accessed 2026-07-25). Supports the original unification claim and the Given/When/Then formulation ("A story's behaviour is simply its acceptance criteria: if the system fulfils all the acceptance criteria, it's behaving correctly."; "Given some initial context (the givens), When an event occurs, Then ensure some outcomes."). The commonly cited 2004 date for the formalization of Given/When/Then could not be verified and is not used. [primary]

<a id="ref-19"></a>[19] Martin Fowler. "[GivenWhenThen](https://martinfowler.com/bliki/GivenWhenThen.html)." martinfowler.com (accessed 2026-07-25). Supports the most careful available characterization of Given/When/Then, including the explicit marking of the specification framing as an advocate's claim ("a style of representing tests - or as its advocates would say - specifying a system's behavior using SpecificationByExample"). The page's date may be a last-edited rather than first-published date. [practitioner]

<a id="ref-20"></a>[20] Cucumber. "[History of BDD](https://cucumber.io/docs/bdd/history/)." cucumber.io (accessed 2026-07-25). Supports the BDD timeline: JBehave from 2003, Liz Keogh writing about BDD from 2004, the introductory article in 2006. Vendor-produced history from the company that owns Cucumber; it gives no date for the formalization of the Given/When/Then template itself. [vendor]

<a id="ref-21"></a>[21] InfoQ. "[Cucumber and BDD, Ten Years On](https://www.infoq.com/news/2018/04/cucumber-bdd-ten-years/)." InfoQ (published April 2018; accessed 2026-07-25). Supports that Cucumber was released in 2008 as a rewrite of RSpec's Story Runner and that "Gherkin" was named at that point, which separates the 2008 DSL from the older Given/When/Then style. [practitioner]

<a id="ref-22"></a>[22] Agile Alliance. "[Acceptance Test Driven Development (ATDD)](https://agilealliance.org/glossary/atdd/)." Agile Alliance glossary (accessed 2026-07-25). Supports ATDD's lineage and the canonical warning that tooling can displace the practice's purpose ("facilitating conversation between developers and product owners about product requirements"). [reference]

<a id="ref-23"></a>[23] Gojko Adzic. "[Specification by Example, 10 years later](https://gojko.net/2020/03/17/sbe-10-years.html)." gojko.net (published 2020-03-17; accessed 2026-07-25). Supports the author of the unification proposal reporting that it largely did not happen ("conversations are more important than capturing conversations is more important than automating conversations"; "We believe the concept of Living Documentation is a yet unrealized key benefit for large organizations."). The survey percentages in the post have no described methodology and are not used here. [primary]

<a id="ref-24"></a>[24] Gojko Adzic. "[Specification by Example](https://gojko.net/books/specification-by-example/)." gojko.net (book published 2011; accessed 2026-07-25). Supports the existence, date and central proposal of the book. **Book page only: the book was not read.** Adzic synthesized and popularized the term; this research did not establish that he coined it. [primary]

<a id="ref-25"></a>[25] Ovidiu Donciu. "[Comparing Test Cases and Acceptance Criteria](https://www.softwaretestingmagazine.com/knowledge/comparing-test-cases-and-acceptance-criteria/)." Software Testing Magazine (accessed 2026-07-25). Supports the clearest practitioner statement of the merge-them position ("Based on all the definitions above, there's not a huge difference(if any) between test cases and acceptance criteria."; "If we already have testable ACs, why should we duplicate work in creating TCs for the same scenarios?"). Quoted as one side of a live disagreement, not as the answer. [practitioner]

<a id="ref-26"></a>[26] Andy Knight. "[BDD 101: Writing Good Gherkin](https://automationpanda.com/2017/01/30/bdd-101-writing-good-gherkin/)." Automation Panda (published 2017-01-30; accessed 2026-07-25). Supports the specification-first framing of scenarios and the one-behavior rule ("behavior scenarios are more than tests - they also represent requirements and acceptance criteria"; "One Scenario, One Behavior!"). Assumes scenarios are written collaboratively before development, which is often not how teams use them. [practitioner]

<a id="ref-27"></a>[27] Andy Knight. "[BDD 101: Manual Testing](https://automationpanda.com/2017/10/08/bdd-101-manual-testing/)." Automation Panda (published 2017-10-08; accessed 2026-07-25). Supports the warning against mechanically converting manual test cases into Gherkin ("Manual testing has a place and a purpose, even in BDD"; "Automation is not a silver bullet - it doesn't satisfy all testing needs"). [practitioner]

<a id="ref-28"></a>[28] Aslak Hellesoy, interviewed by Semaphore. "[Cucumber Founder Aslak Hellesoy on TDD and BDD](https://semaphore.io/blog/aslak-hellesoy-cucumber)." Semaphore (accessed 2026-07-25). Supports Cucumber's creator stating BDD's design-first intent ("BDD and TDD are not about testing existing code. They are about designing a code that hasn't yet been written."). No interview date confirmed on the page. [primary]

<a id="ref-29"></a>[29] Cem Kaner, James Bach and Bret Pettichord. "[Context-Driven Testing: Principles](https://context-driven-testing.com/)." context-driven-testing.com (accessed 2026-07-25). Supports the founding principles of the school that objects to scripted test cases ("The value of any practice depends on its context."; "There are good practices in context, but there are no best practices."; "Metrics that are not valid are dangerous."). No publication date on the page. [primary]

<a id="ref-30"></a>[30] James Bach. "[Fighting Bad Test Documentation](https://www.satisfice.com/blog/archives/19)." Satisfice, Inc. (published 2004-02-21; accessed 2026-07-25). Supports the most actionable form of the objection: that hard-to-document testing goes undone ("But documenting is not testing. It is one of the chief distractions to testing."; "certain kinds of testing isn't done at all just because it is hard to document (exploratory testing and complex scenario tests often fall in this category)."). [primary]

<a id="ref-31"></a>[31] James Bach. "[A Test is a Performance](https://www.satisfice.com/blog/archives/1346)." Satisfice, Inc. (published 2014-01-06; accessed 2026-07-25). Supports the philosophical core of the context-driven objection ("Testing is a performance, not an artifact."). Bach's characterization of the opposing school is written by an opponent and is labeled as such where used. [primary]

<a id="ref-32"></a>[32] Michael Bolton. "[The Test Case Is Not The Test](https://developsense.com/blog/2017/02/the-test-case-is-not-the-test)." DevelopSense (published 2017-02-16; accessed 2026-07-25). Supports the sharpest available statement of what a test case is and is not, and the qualifier that the artifact still has a role ("The test case is not the test. The test is what you think and what you do."; "A recipe is not cooking. An itinerary is not a trip. A score is not a musical performance, and a file of PowerPoint slides is not a conference talk."; "The test case may have a role, but you, the tester, are at the centre of your testing."). [primary]

<a id="ref-33"></a>[33] Vitaly Sharovatov. "[Why Per-Tester QA KPIs Backfire](https://www.qase.io/blog/why-qa-testing-kpis-backfire/)." Qase (published 2026-07-17; accessed 2026-07-25). Supports the mechanism by which count-based targets corrupt testing ("One hundred percent coverage of shallow checks outscores eighty percent coverage of risky paths."; "you are no longer observing your process, but rather measuring your people's creativity in defeating the observation."). Vendor-hosted. [practitioner]

<a id="ref-34"></a>[34] Asad Abrar. "[Test Coverage Metrics That Actually Tell You Something](https://www.drizz.dev/post/test-coverage-metrics)." drizz.dev (published 2026-07-08; accessed 2026-07-25). Supports test-case count named explicitly as a vanity metric ("Number of test cases. 'We have 5,000 tests' tells you nothing. A team with 500 focused tests beats 5,000 trivial ones."). [practitioner]

<a id="ref-35"></a>[35] Chris Faraglia. "[Software Testing in Regulated Industries: From Traceability to AI Governance](https://www.testrail.com/blog/testing-regulated-industries/)." TestRail (published 2026-03-03; accessed 2026-07-25). Supports the regulatory case for fully specified, traceable, version-controlled cases ("Full traceability via linkage of all tests to corresponding requirement artifacts"; "The bar doesn't lower just because a machine wrote it, either. AI-generated test cases must also be version-controlled and traceable."). Published by a test-management vendor with a commercial interest in traceability tooling. [vendor]

<a id="ref-36"></a>[36] Agile Alliance. "[Exploratory Testing](https://agilealliance.org/glossary/exploratory-testing/)." Agile Alliance glossary (accessed 2026-07-25). Supports a balanced statement of the exploratory position that stops short of rejecting scripted testing ("These skills will be deployed more effectively in the exploratory style on an Agile team, as this style is more consistent with an Agile approach than the 'scripted testing' style."). [reference]

<a id="ref-37"></a>[37] ISTQB. "[Test scenario](https://istqb-glossary.page/test-scenario/)." ISTQB Glossary, community mirror (accessed 2026-07-25). Supports the definitions of test suite and test run, and the vocabulary trap that the glossary defines test scenario as a synonym for test script ("A set of several test cases for a component or system under test, where the post condition of one test is often used as the precondition for the next one."; "The execution of a test suite on a specific version of the test object."). Mirror pages; the scenario definition directly contradicts common practitioner usage, a contradiction this companion reports rather than resolves. [reference]

<a id="ref-38"></a>[38] Microsoft. "[Test objects and terms overview](https://learn.microsoft.com/en-us/azure/devops/test/test-objects-overview?view=azure-devops)." Azure DevOps documentation (page updated 2026-04-17; accessed 2026-07-25). Supports how a major tool models a test case and separates specification from execution ("The only required field for all work item types is Title."; "Test cases by themselves aren't executable. When you add a test case to a test suite, you generate test points."; "Test result: The recorded outcome of a single test case execution within a test run."; "Test step: An individual action within a test case, consisting of an Action (what the tester does) and an Expected Result (the anticipated behavior)."). [vendor]

<a id="ref-39"></a>[39] Microsoft. "[Associate automated tests with test cases](https://learn.microsoft.com/en-us/azure/devops/test/associate-automated-test-with-test-case?view=azure-devops)." Azure DevOps documentation (page updated 2026-05-08; accessed 2026-07-25). Supports what changes when a case is automated, including the parameter trap ("Test case parameters are for manual test iterations only. Automated tests don't use parameters defined on the test case work item."; "You can associate a test method with multiple test cases, but you can't associate more than one test method with a single test case."). [vendor]

<a id="ref-40"></a>[40] Tricentis. "[Test Case APIs](https://docs.tricentis.com/qtest-saas/content/apis/apis/test_case_apis.htm)." qTest SaaS documentation (accessed 2026-07-25). Supports a second independent tool's data model and how little it requires to create a case: a name and a set of field-value properties. [vendor]

<a id="ref-41"></a>[41] Shreya Bose. "[Requirements Traceability Matrix (RTM): A How-To Guide](https://www.testrail.com/blog/requirements-traceability-matrix/)." TestRail (accessed 2026-07-25). Supports what traceability means operationally ("a tool or document commonly used to ensure that all the requirements established for a testing project are mapped to corresponding tests."). [practitioner]

<a id="ref-42"></a>[42] TestBuggy. "[Test Cases vs. Bug Reports: What's the Difference and When to Use Each](https://testbuggy.com/blog/test-cases-vs-bug-reports)." TestBuggy (accessed 2026-07-25). Supports the boundary to the third qa-docs member in terms of direction and timing ("Bug reports are reactive, created after discovering a problem in existing software. Test cases are proactive, written 'before or during development' to define correct behavior."). No named author or date on the page. [practitioner]
