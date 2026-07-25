# Companion: The Test Plan

> The deep explainer for the test-plan bundle. Read this to understand what a test plan is, where it came
> from, why it is shaped the way it is, and where practitioners disagree about it - and they disagree more
> sharply about this document than about almost any other in the library. The short operator card is
> [`test-plan_guide.md`](test-plan_guide.md); a fully worked instance is
> [`test-plan_example.md`](test-plan_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A test plan is **the document that says what you are going to test, what you are deliberately not going to
test, how deeply and in what order, and how everyone will know when testing is done.** ISTQB's definition is
the canonical long form: *"A document describing the scope, approach, resources and schedule of intended test
activities. It identifies amongst others test items, the features to be tested, the testing tasks, who will
do each task, degree of tester independence, the test environment, the test design techniques and entry and
exit criteria to be used, and the rationale for their choice, and any risks requiring contingency planning"*
[[5]](#ref-5). Note the clause most templates drop: *the rationale for their choice*. A plan that lists
criteria without saying why those criteria is half a plan.

**At a glance**
- It **scopes**: what is being tested, and explicitly what is not, with a reason for each exclusion
  [[8]](#ref-8).
- It **ranks by product risk**, and the ranking drives both how deeply each area is tested and the order it
  is tested in [[12]](#ref-12)[[13]](#ref-13).
- It sets **entry and exit criteria that can be checked** - thresholds and states, not adjectives
  [[7]](#ref-7)[[10]](#ref-10).
- It names **one person per area**, and where testing runs and on what data.
- It is **prospective**. Results, status and the verdict live in the test report and the test tool, not here
  [[38]](#ref-38).

If you read nothing else: a test plan is worth exactly what it changes. The decisions it forces, the
scope-out it records, and the criteria someone can hold you to are the product; the document is just where
they are written down.

The honest first thing to know is that **this document type has a credibility problem, and pretending
otherwise produces bad templates.** Three facts, all verifiable, all uncomfortable:

- The standard nearly everyone cites, IEEE 829, is **superseded** [[1]](#ref-1)[[2]](#ref-2).
- The standard that replaced it is **paywalled**, so most people who claim to follow it have never read it
  [[3]](#ref-3)[[27]](#ref-27).
- A decade-long, credentialed campaign argued that standardized test documentation actively **harms** testing
  [[24]](#ref-24)[[25]](#ref-25).

The second thing to know is the distinction that makes all of this navigable, and it comes from the
best-known critic of test documentation. James Bach: *"The test plan document does not necessarily contain a
test plan"* [[14]](#ref-14). The **plan** is the set of ideas guiding a test effort. The **document** is an
artifact that may or may not carry those ideas. Every criticism in section 6 is aimed at documents that carry
none, and none of it is an argument against thinking about risk and coverage before you test.

So the target this bundle aims at, borrowed from a practitioner who argues for test plans rather than against
them: a plan that someone reads. *"A test plan that no-one reads, which doesn't inform anyone about the
testing to be done, is a waste of your valuable time"* [[31]](#ref-31). Or, put positively, *"the value of
the test plan is in the planning (i.e. the thinking), not the document"* [[9]](#ref-9) - which is a reason to
make the document short and sharp, not a reason to skip it.

**One terminology warning before you go further.** If your team uses Azure Test Plans, TestRail, Xray, Zephyr
or qTest, the thing those tools call a "test plan" is not this document. It is an execution container that
groups test suites and runs [[38]](#ref-38). This template scaffolds the narrative document: scope, approach,
risk and criteria. Section 8 covers the trap in full, because writing one when you needed the other is the
most common structural mistake around this artifact.

## 2. Origins and evolution

Test documentation was standardized early. **IEEE 829** defined a family of test documents, of which the test
plan was the flagship, and went through several editions before the last one, 829-2008 [[1]](#ref-1). Its
section list is the mental model most practitioners still carry: test plan identifier, introduction, test items, features to be
tested, features **not** to be tested, approach, item pass/fail criteria, suspension and resumption
requirements, deliverables, testing tasks, environmental needs, responsibilities, staffing and training,
schedule, risks and contingencies, and approvals [[8]](#ref-8).

**IEEE 829-2008 is superseded.** The IEEE Standards Association page for it carries the status label
*Superseded Standard* and states plainly: *"IEEE 829-2008 is superseded by ISO/IEC/IEEE 29119-1-2013,
ISO/IEC/IEEE 29119-2-2013, ISO/IEC/IEEE 29119-3-2013 and ISO/IEC/IEEE 29119-4-2015"* [[1]](#ref-1).
Wikipedia's software-test-documentation article records the same transition [[2]](#ref-2). Two honest
qualifiers. First, *superseded* is a distinct IEEE status from *withdrawn* or *inactive*, and this bundle does
not claim the stronger word. Second, sources disagree on how many sections 829 defined: a widely used vendor
enumeration lists sixteen [[8]](#ref-8), Wikipedia says fifteen [[42]](#ref-42). Since neither is the
standard, this companion says "roughly sixteen" and leaves it there.

**ISO/IEC/IEEE 29119** is the successor series, developed from 2007, first published in 2013, and revised
through 2021 and 2022, with a fifth part added in 2024 [[4]](#ref-4). Part 3 is the test documentation part;
its current edition, 29119-3:2021, was published on 2021-10-28 and covers templates and examples arranged by
the test processes defined in Part 2 [[3]](#ref-3).

**Here is the part that matters for how you read any test plan advice, including this bundle's.** Nobody
writing this companion has read 29119-3. ISO, IEEE and BSI all sell it [[3]](#ref-3), and the accessibility
objection was one of the loudest in the professional argument about it: *"The standard is not available
publicly. How can I comply to or even discuss a standard that is not publicly available?"* [[27]](#ref-27).
Every content-item list for 29119-3 in circulation, including the shape of this template, is secondary. What
can be said from the published scope alone is that Part 3 supplies documentation templates arranged around
the test processes defined in Part 2 [[3]](#ref-3), which is a reorganization rather than a reinvention. What
this companion deliberately does **not** do is describe the standard's internal structure or its
shall/should/may conformance map, because that would mean reporting an unread document as if it had been
read.

The practical consequence is that **the sixteen-section model persists as folk practice**, transmitted
through vendor templates and training material rather than through the standards themselves. A template that
reproduces it uncritically is reproducing a copy of a copy. This bundle keeps the sections that earn their
place and says why the others are optional.

## 3. Anatomy (section by section)

The full variant carries nine sections; the lean variant carries five of them, unchanged in name and order.
The argument for each is below.

### Scope and Non-Scope

What this release or feature is being tested for, and **what is explicitly excluded**.

IEEE 829 gave the exclusion its own section, "features not to be tested" [[8]](#ref-8). In this library's
judgment it is the most valuable content in the document and, in practice, among the first things cut - a
judgment stated here as such rather than as a sourced finding, because no source in the research log measures
how often it is dropped. Dropping it is how a plan becomes unfalsifiable: if nothing is out of scope, nothing can be found missing. Writing it forces the scope-out
conversation to happen while it is cheap, and it creates the record of what was agreed to be left alone. A
tester who is later asked "why didn't you test that?" has an answer that was signed off in advance.

Name the test items concretely (the build, the services, the flag states), because "the feature" is not a test
item.

### Risk-Ranked Approach

Which areas carry which risk, why, and what depth of testing each earns.

This is where risk-based testing lives, and it is the section that separates a plan from a table of contents.
The purpose of risk-based testing is to *"steer all phases of the test process in order to optimize testing
efforts and limit risks"* [[12]](#ref-12), and the mechanism is concrete: risk tier selects technique depth
and execution order, so high-risk areas get exhaustive techniques such as decision tables and boundary
analysis while low-risk areas get lighter treatment [[13]](#ref-13). Highest-risk areas are also tested
**first**, so that if time runs out, what is missing is the least important coverage rather than a random
sample of it.

A weak approach section names test types ("functional, regression, performance"). A strong one names the
areas, ranks them, and justifies the ranking, which is exactly the *rationale* ISTQB's definition asks for
[[5]](#ref-5). The product risks here usually come from somewhere: the PRD's own risk table, the risk
register, or a team risk-storming session. Reuse them rather than inventing a parallel list.

### Test Levels and Types (full variant only)

Which levels (unit, integration, system, end-to-end) and which types (functional, performance, security,
accessibility) are in play, and who owns each.

Lean plans omit this because a small team already knows. It earns its place when more than one group tests,
when a level is someone else's responsibility, or when a non-functional type needs its own environment and
schedule.

### Entry and Exit Criteria

The conditions that must hold before testing starts, and the conditions that define done.

ISTQB's framing of entry criteria is unusually useful because it is functional rather than definitional: they
exist to *"prevent a task from starting which would entail more (wasted) effort compared to the effort needed
to remove the failed entry criteria"* [[7]](#ref-7). That is the test for whether a criterion belongs: if
failing it would not actually stop you, it is not an entry criterion.

**Criteria are thresholds, not adjectives.** "Environment is ready" and "most tests passed" cannot be checked;
"the v2.3.1 build is deployed to staging, seeded with the three permission personas, and the smoke suite
passes" and "95 percent of planned cases executed with pass status" can [[10]](#ref-10). One vendor source
puts the consequence plainly: without defined criteria *"it becomes difficult to know whether the test was
valid, whether the results are acceptable, or whether more testing is needed"* [[11]](#ref-11).

**Two traps here.** The first concerns who agreed. ISTQB's definition requires the **rationale** for a plan's
criteria and technique choices to be recorded [[5]](#ref-5), and this library adds a second requirement on
its own authority, not on ISTQB's: exit criteria are a commitment about when to stop, so they need a named
stakeholder who agreed to them and a date. Nearly every template omits both. Name who agreed and when. The second is the metrics trap: pass rate and test-case count are the
easiest exit criteria to write and the most misleading. *"Pass rate alone is misleading. A pass rate of 98% in
a suite of 200 tests means 4 tests failed"*, and *"a test case that checks 'does the page load' is not
equivalent to one that checks complex business logic"* [[32]](#ref-32). Pair any count-based criterion with a
coverage-of-risk criterion, or you have written a criterion that a team can satisfy by writing more trivial
tests.

### Suspension and Resumption Criteria (full variant only)

What stops testing mid-cycle, and what has to be true to restart.

It is one of the sections teams cut first from the 829 list [[8]](#ref-8) - again a judgment rather than a
measured finding - and the one people wish they had written when a blocking defect lands on a Thursday. It
matters most when a gate exists (a security review, a compliance
sign-off) or when an environment is shared, because "should we keep testing?" then has an answer that was
decided calmly in advance.

### Environment, Data, and Ownership

Where testing runs, what data it needs, and who is accountable for each part.

Test data is where plans quietly fail: the data needed to exercise a permission boundary or an error path
rarely exists by accident, and manufacturing it is often the longest lead-time item in the plan. Name the
data, name who provides it, and name what is anonymized. Ownership is one named person per area, never a team.

### Schedule and Deliverables

The timebox, the milestones, and what testing will hand over.

Deliverables are worth listing explicitly because they set expectations about what exists at the end: executed
cases, a defect list, a test summary or report, and any sign-off artifact. The plan is prospective; the report
is retrospective. Keeping them separate is what stops the plan turning into an execution tracker (section 8).

### Risks to the Test Effort (full variant only)

The risks that threaten the **testing**, as distinct from the product risks that shape coverage.

These are two different lists and merging them is why "risks" sections read as noise. Product risk: the
permission check might leak data. Project risk: the staging environment is shared with another team and might
be unavailable in week two. The first shapes what you test and how deeply; the second shapes the schedule and
the contingency. Separating them is what makes both usable, and it is why this template gives them separate
homes rather than one "risks" heading.

### Approvals and Change Control (full variant only)

Who signed off, when, and how the plan changes once agreed.

This is the section that exists for regulated, audited and multi-team contexts and can be cut everywhere else.
Its honest purpose is not ceremony: a plan that changes silently after sign-off is worse than one that was
never signed, because it carries borrowed authority.

## 4. Variants and sizing

**Lean (five sections)** is the default. It carries Scope and Non-Scope, Risk-Ranked Approach, Entry and Exit
Criteria, Environment, Data and Ownership, and Schedule and Deliverables. That set answers the five questions
a plan cannot skip whatever its length: what is in and out, how it will be tested, who is responsible, why the
coverage is shaped that way, and when it starts and stops [[9]](#ref-9). It fits on a page or two and is
meant to be revised in place as the release moves.

**Full (nine sections)** adds Test Levels and Types, Suspension and Resumption, Risks to the Test Effort, and
Approvals and Change Control. Use it when the context genuinely demands it: regulated or audited work, several
teams or vendors testing the same release, a formal gate in the middle of the cycle, or an organization whose
process requires an approvable artifact.

The nesting is strict: every lean heading appears in full, with the same name in the same order. Growing a
lean plan into a full one is additive, so you never rewrite what you already agreed.

**How to choose.** Ask what would change if a section were missing. If the answer is "nothing, everyone
already knows", cut it. Length is not rigor: a five-section plan that records real decisions beats a
nine-section plan padded to look complete, and the padding is precisely what the critics in section 6 are
attacking.

## 5. Methodology lineage

The test plan is **methodology-agnostic in origin** and heavily contested in agile practice, so its lineage is
worth getting right - especially since two of its most-cited pieces are routinely misattributed.

**Standards lineage (waterfall-adjacent).** IEEE 829 and its ISO successor assume a project with phases, a
plan written before execution, and documents as deliverables [[8]](#ref-8)[[3]](#ref-3). This is the lineage
that produces thirty-page plans, and the one the agile tradition reacted against.

**Risk-based testing** is the cross-cutting practice that survives every methodology. Its academic framing
organizes it along three axes - risk drivers, risk assessment, and the risk-based test process - and its
purpose is to steer effort rather than to distribute it evenly [[12]](#ref-12).

**Agile lineage.** The **agile testing quadrants** are the best-known planning aid here, and their origin is
commonly reported wrong. Brian Marick created the original matrix in 2003 [[21]](#ref-21); Lisa Crispin and
Janet Gregory extended, named and popularized it, and Crispin credits *"Brian Marick's agile testing matrix"*
explicitly [[20]](#ref-20). Crispin describes the quadrants today as *"a thinking tool that help teams plan
and execute testing activities so that they can confidently deliver customer value"* [[19]](#ref-19). That is
a planning instrument, not a replacement for planning.

Crispin and Gregory did not abolish test planning. Their condensed guide carries a chapter titled "Test
Planning in Agile Contexts", covering the team, the product, planning across levels of detail, and regression
planning [[22]](#ref-22). What dissolves in agile is the heavyweight upfront artifact; what remains is
iterative, just-in-time planning.

**Exploratory lineage.** Session-based test management introduced the time-boxed session and the **charter**
as the unit of chartered exploratory work, framed as *"activity-based test management which is an alternative
to artifact-based management"* [[18]](#ref-18). Two attribution corrections, because both errors are common:
the SBTM paper is **Jonathan Bach's**, co-credited with James Bach, and Michael Bolton is not a co-creator.
Charters replace scripted cases for exploratory sessions; they do not replace the plan, which still has to say
which areas get chartered and why.

**The context-driven answer to "so what replaces the plan?"** is: a lighter plan, built differently. James
Bach's own guide describes *"a process guide for creating a good test plan within the RST methodology. It
consists of seven tasks. The tasks can be performed in any order, or simultaneously and iteratively"*
[[17]](#ref-17). Iterative and order-independent is the opposite of the waterfall artifact, and it is still a
test plan.

## 6. Debates and contested boundaries

This document type sits on the most public rupture in the testing profession. A bundle that presented the
standard structure as settled best practice would be lying by omission.

**The Stop 29119 campaign.** In 2014 James Christie launched a petition to withdraw ISO/IEC/IEEE 29119,
after speaking at the Association for Software Testing's conference; the AST hosted the debate that followed
[[27]](#ref-27). The argument was not that testing needs no thought but that a template-driven standard
cannot capture a
cognitively demanding craft, and that the working group had excluded the practitioners most likely to object.
James Bach put it bluntly: *"The reason they have excluded us is that they know we won't agree to any
simplistic standard based on templates or simple formulae."* And on where the burden of proof sits: *"The
burden is on those who claim that the craft can be standardized to study the craft and recognize and resolve
the deep differences among us."* [[24]](#ref-24)

**The sharpest version of the critique, and the one most useful to a template author,** is Christie's: a
document can comply completely and say nothing. *"The standard defines in great detail the process and the
documents for testing, but fails to clarify the purpose of testing, the outcomes that stakeholders expect."*
And therefore: *"It would be simple to comply with the ISO 29119 Test Completion Process, and produce a
report that provided no worthwhile information at all."* [[25]](#ref-25) Completeness of fields is not completeness of
thought. That single sentence is the reason this template's guidance asks what each section **decides** rather
than what it contains.

**Where it landed.** The standard was **not** withdrawn. Parts were revised in 2021 and 2022, a fifth part
arrived in 2024, and a technical report for agile projects was added, which is a direct response to one line
of criticism [[4]](#ref-4). Opposition was not retracted either [[26]](#ref-26). Institutionally the
standardizers won; intellectually the argument is open.

**The other side deserves its case.** The gap the standard was meant to fill was real. As one account of the
dispute puts it: *"There was no definitive international set of software testing standards previously."*
[[30]](#ref-30) And the counter to
the exclusion charge is that the standard requires risk-based testing and does not dictate how practitioners
execute within it.

**The conflict-of-interest strand** is contested and unresolved. Michael Bolton documented working-group
editors' affiliations with consultancies and certification bodies that stood to benefit from adoption
[[28]](#ref-28); the standard's convenor disputed that characterization. No independent audit exists. It is
recorded here because it explains why critics were skeptical of claims to neutral consensus, not because this
bundle adjudicates it.

**The underlying philosophical position** of the critics is worth reading directly, because it is more
moderate than its reputation: *"There are good practices in context, but there are no best practices"*
[[29]](#ref-29). That is an argument against universality, not against documents.

**"Written once, never read."** Bach's 2004 critique is the origin of the phrase most people repeat:
*"Documenting is not testing. It is one of the chief distractions to testing."* And on the documents
themselves: *"Test documentation is often of such poor quality that it's better ignored than followed."*
[[15]](#ref-15) This is the criticism to
take most seriously, because it is empirical rather than philosophical, and because reformists inside the
pro-plan camp concede it [[31]](#ref-31).

**But Bach is not anti-test-plan, and citing him as if he were is a misreading.** He published a Test Plan
Evaluation Model in 1999 *"to provide a basis to systematically assess the quality of test plans"*
[[16]](#ref-16) and a guide to building one iteratively [[17]](#ref-17). His distinction, again, is between
the ideas and the artifact [[14]](#ref-14).

**Does a test plan belong in agile at all?** The strongest practitioner position says no: *"When test plans
are required in agile projects, it is a clear sign that it is not an agile environment to begin with"* (Ray
Oei), alongside *"most test plans contain irrelevant and outdated information that does not contribute to
quality"* (Eddy Bruin) [[23]](#ref-23). Those are two named practitioners in one interview, not a consensus,
and they are contradicted by the agile canon itself, which keeps a test-planning chapter [[22]](#ref-22).
Report the spectrum; do not flatten it.

**This bundle's position, stated openly.** It sits with the reformists. Plan, keep it short, make every
section decide something, and cut any section that would change nothing if deleted. The structure here is a
scaffold, not a compliance cage, and the guide says which sections are safe to drop.

## 7. Anti-patterns and failure modes

**The plan nobody reads.** Written for a kickoff, filed, never reopened. The tell is that no decision in the
last month traces back to it. *"A document that is not read has little value"* [[31]](#ref-31), and the
research on practitioners not following their own documentation is decades old [[15]](#ref-15). Fix: shorten
it until it is worth reading, and put the criteria where the team already looks.

**Completeness theater.** Every section filled, nothing decided, because the template demanded a heading. This
is precisely the compliance-without-content failure the critics name [[25]](#ref-25). Fix: delete sections
that decide nothing; a lean plan that records real choices outranks a padded full one.

**Adjective criteria.** "Environment is ready", "testing is complete", "quality is acceptable". None can be
checked, so none is a criterion [[10]](#ref-10). Fix: a number, a state, or a named artifact for every
criterion.

**Pass-rate exit criteria.** "95 percent pass" as the sole gate, which a team can satisfy by adding trivial
tests, and which hides four failures in two hundred [[32]](#ref-32). Fix: pair every count criterion with a
risk-coverage criterion and a severity rule (for example, no open Sev-1 or Sev-2 in scope).

**The merged risk list.** Product risks and project risks in one table, so neither drives anything. Fix: risks
that shape coverage go in the approach; risks that threaten the effort go in their own section.

**The scope with no non-scope.** Nothing excluded, so nothing can be found missing, and the scope-out argument
happens after the release instead of before it [[8]](#ref-8). Fix: write the exclusions and get them agreed.

**The plan that became a tracker.** Results columns and status fields creep in, and the prospective document
turns into a retrospective one. Fix: keep execution status in the tool or the report, and keep the plan about
intent.

**The tool-shaped plan.** A "test plan" created in a test management tool, containing a name and a date range,
mistaken for the planning document [[38]](#ref-38)[[39]](#ref-39). Fix: know which artifact you are producing;
they are complements, not substitutes.

## 8. Relationships to other artifacts

**Test plan and test strategy: genuinely unsettled, so know both usages.** ISTQB draws the line at
organizational scope, defining an organizational test strategy as *"a high-level description of the test
levels to be performed and the testing within those levels for an organization or programme (one or more
projects)"* [[6]](#ref-6). The most usable one-liner from practice: *"the strategy defines how you test, the
plan defines what you test this time"* [[37]](#ref-37). But IEEE 829 folds the approach into the plan
[[8]](#ref-8), and practitioners openly admit that *"in some organizations test strategy can be just a part of
the test plan document, identifying the test approach for the concrete project"* [[35]](#ref-35). Another
concedes the point twice over: *"The difference between these two documents is subtle."* and *"In smaller
projects, test strategy is often found as a section of a test plan."* [[36]](#ref-36) Wikipedia notes the same overlap from the other side:
the plan's major elements *"are also used in a formal test strategy"* [[42]](#ref-42). Practical rule: if your
organization has a standing strategy document, this plan inherits from it and should say so in one line; if it
does not, the Risk-Ranked Approach section **is** your strategy for this release.

**Test plan and test case: a clean boundary.** The plan is the governing document for an effort; a test case
is one executable verification. The audience difference is the practical version: *"Test plans target Testers,
Test managers and any Stakeholders, whereas test cases are primarily for the test team itself."*
[[33]](#ref-33) Cases are what the plan schedules; they are not part of it.

**Test plan and bug report.** The plan is written before and governs; a bug report is produced during
execution and records one verification that failed. The plan is what decides how a given failure is handled:
its severity rule determines whether a defect merely enters triage, its exit criteria determine whether the
release can proceed with it open, and its suspension rule determines whether one particular class of defect
stops the cycle outright. A bug report is not a test result in the plan's sense; it is the artifact
downstream of a failed case, and the plan should never accumulate them.

**Test plan and acceptance criteria: different altitudes, and the boundary is contested.** Acceptance criteria
are conditions on one story, agreed with the business, saying what must be true for that story to be done. A
test plan says how the whole verification effort is organized. They meet where criteria generate cases, and
one practitioner camp argues that testable criteria make separate test cases duplicated work: *"based on all
the definitions above, there's not a huge difference(if any) between test cases and acceptance criteria"*, so
*"if we already have testable ACs, why should we duplicate work in creating TCs for the same scenarios?"*
[[34]](#ref-34). That position is real and worth knowing; the counter is that criteria stop at the agreed
behavior while test design continues into negative, boundary and regression cases nobody wrote a criterion
for. Either way, the plan is not the place to restate criteria - it is the place to say which criteria are in
scope for this cycle.

**Test plan and test report: opposite directions.** The plan is prospective and prescriptive; the report is
retrospective and descriptive. They were separate deliverables in the standards lineage [[8]](#ref-8), and
keeping them separate is what prevents the tracker anti-pattern in section 7.

**Test plan and definition of done: different scopes.** A definition of done is a standing, team-level
invariant applied to every increment. A test plan is scoped to one release or feature. A DoD may include "the
test plan's exit criteria are met" as a line; the plan does not contain the DoD.

**Test plan and the tool called Test Plans: not the same object, and this is the trap.** In Azure Test Plans,
*"test plans: group test suites and individual test cases"*, and *"the only required field for all work item
types is Title"* [[38]](#ref-38); creating one asks for a name, an area path and an iteration, so that the
team can *"create test plans and test suites to track manual testing for sprints or milestones"*
[[39]](#ref-39). qTest models it as a milestone calendar in which you *"define the high-level milestones and
testing objectives"* per release and build [[40]](#ref-40). None of these tools requires an approach, a risk
ranking, or an exit criterion. Vendors describe the shift as the plan becoming a living thing inside the
platform - tools *"serve as living documents that guide the entire testing process from requirements gathering
through execution and reporting"* [[41]](#ref-41) - but that framing elides the difference. The document did
not move into the tool; it **split**. The narrative half (scope, approach, risk, criteria) is what this
template scaffolds. The execution half (suites, runs, configurations, results) is what the tool holds. Teams
that believe the tool replaced the document end up with an execution container and no recorded thinking, which
is the failure this bundle exists to prevent.

**Within the qa-docs family.** This is the family's planning member: the test plan scopes and prioritizes, the
test case specifies one verification, and the bug report records one that failed. The three chain on one
feature. Upstream, the plan draws its scope from the PRD and its functional coverage from the acceptance
criteria; sideways, it should reuse the product risks already recorded in a risk register rather than
inventing a parallel list.

**And one relationship outside this library.** The `pm-skills` skill `deliver-edge-cases` produces a
catalog of failure modes, boundary conditions and recovery paths for a feature, and its own description names
QA planning and preparing test plans among its uses. That output is a direct input to the Risk-Ranked
Approach section here, because a documented failure surface is exactly the raw material risk ranking needs:
it converts "what could go wrong" from a brainstorm into a list somebody already enumerated. It is also the
only pm-skills skill any qa-docs member can honestly pair with, because that library has no testing or QA
skill at all.

## 9. Adaptations

**Regulated and audited contexts** (medical devices, aerospace, finance) need the full variant, and the
Approvals and Change Control section stops being ceremony: completeness is a compliance requirement, and the
sign-off record is part of the evidence.

**Continuous delivery.** When releases are continuous, a per-release plan makes no sense. Write one standing
plan per product area, revised in place, whose Entry and Exit Criteria are encoded in the pipeline (coverage
thresholds, required checks, gates) and whose Risk-Ranked Approach explains what is automated, what is
explored, and why.

**Exploratory-heavy teams** should state chartered exploration as a first-class part of the approach, naming
the areas to be chartered and the time budget, rather than pretending the plan enumerates every case
[[18]](#ref-18).

**Small teams with no strategy document** should treat the Risk-Ranked Approach section as their strategy and
say so, rather than creating a second document to satisfy a distinction their organization does not make
[[35]](#ref-35).

**Vendor or outsourced testing** raises the stakes on Environment, Data and Ownership and on Approvals: the
plan is functioning as a contract, and every ambiguity is a change request later.

**A note on context-driven adaptation.** The principle that *"there are good practices in context, but there
are no best practices"* [[29]](#ref-29) applies to this template too. If a section does not fit your context,
the honest move is to cut it and say why, not to fill it to satisfy the shape.

## 10. Worked example

[`test-plan_example.md`](test-plan_example.md) is a full-variant plan for the "Saved Views for Dashboards"
feature at the fictional Acme Analytics, the same feature the delivery-docs bundles use. It is deliberately
chained to its neighbors: scope comes from the [PRD](../prd/prd_example.md), the technical surface (the views
endpoints, the shared-view permission re-check, the stale-field degradation path) comes from the
[design document](../sdd/sdd_example.md), and the functional coverage traces to the
[acceptance criteria](../acceptance-criteria/acceptance-criteria_example.md).

Three things in it are worth studying. Its **non-scope** is explicit and named (the Could-priority stale-view
indicator). Its **risk ranking** is inherited from the PRD's own risk table rather than invented, which is why
the shared-view permission boundary gets the deepest coverage and tests first. And its **exit criteria** are
deliberately not a pass-rate line: they pair execution coverage with a severity rule and a named,
dated stakeholder agreement, which is the shape section 3 argues for.

---

## References

<a id="ref-1"></a>[1] IEEE Standards Association. "[IEEE 829-2008: IEEE Standard for Software and System Test Documentation](https://standards.ieee.org/ieee/829/3787/)." IEEE SA (accessed 2026-07-25). Supports the current status of IEEE 829-2008 as a superseded standard and names its successors ("IEEE 829-2008 is superseded by ISO/IEC/IEEE 29119-1-2013, ISO/IEC/IEEE 29119-2-2013, ISO/IEC/IEEE 29119-3-2013 and ISO/IEC/IEEE 29119-4-2015"). Note that IEEE labels this "Superseded", which is a distinct status from "Withdrawn" or "Inactive"; no withdrawal date appears on the page. [primary]

<a id="ref-2"></a>[2] Wikipedia contributors. "[Software test documentation](https://en.wikipedia.org/wiki/Software_test_documentation)." Wikipedia (accessed 2026-07-25). Corroborates the supersession of IEEE 829-2008 and notes 829's influence on certification syllabi ("IEEE 829-2008 has been superseded by ISO/IEC/IEEE 29119-3:2013"). [reference]

<a id="ref-3"></a>[3] IEEE Standards Association. "[IEEE/ISO/IEC 29119-3:2021, Software and systems engineering - Software testing - Part 3: Test documentation](https://standards.ieee.org/ieee/29119-3/7499/)." IEEE SA (accessed 2026-07-25). Supports that 29119-3:2021 is the current edition, published 2021-10-28, and that it provides templates and examples arranged by the test processes of Part 2. **Landing page only: the standard itself is paywalled and was not read**, so no claim here rests on its normative text. [primary]

<a id="ref-4"></a>[4] Wikipedia contributors. "[ISO/IEC 29119](https://en.wikipedia.org/wiki/ISO/IEC_29119)." Wikipedia (accessed 2026-07-25). Supports the series timeline (development from 2007, first parts 2013, revisions 2021-2022, Part 5 in 2024, a technical report for agile projects) and that the standard was not withdrawn following the petition campaign ("a series of five international standards for software testing"). Used for timeline facts only; the article carries maintenance tags. [reference]

<a id="ref-5"></a>[5] ISTQB. "[Test plan](https://istqb-glossary.page/test-plan/)." ISTQB Glossary (accessed 2026-07-25). Source of the canonical definition, including the requirement to record the rationale for criteria and technique choices ("A document describing the scope, approach, resources and schedule of intended test activities. It identifies amongst others test items, the features to be tested, the testing tasks, who will do each task, degree of tester independence, the test environment, the test design techniques and entry and exit criteria to be used, and the rationale for their choice, and any risks requiring contingency planning. It is a record of the test planning process."). No version date is displayed on the page. [primary]

<a id="ref-6"></a>[6] ISTQB. "[Organizational test strategy](https://istqb-glossary.page/organizational-test-strategy/)." ISTQB Glossary (accessed 2026-07-25). Supports ISTQB's organizational-scope definition of test strategy, which is the line it draws against a project-level plan ("A high-level description of the test levels to be performed and the testing within those levels for an organization or programme (one or more projects)."). The entry cites 2012-2014 syllabi. [primary]

<a id="ref-7"></a>[7] ISTQB. "[Entry criteria](https://istqb-glossary.page/entry-criteria/)." ISTQB Glossary (accessed 2026-07-25). Supports the definition and, more usefully, the functional purpose of entry criteria ("The set of generic and specific conditions for permitting a process to go forward with a defined task, e.g., test phase."; "prevent a task from starting which would entail more (wasted) effort compared to the effort needed to remove the failed entry criteria"). [primary]

<a id="ref-8"></a>[8] Reqtest. "[How to Write a Test Plan with the IEEE 829 Standard](https://reqtest.com/en/knowledgebase/how-to-write-a-test-plan-2/)." Reqtest knowledge base (accessed 2026-07-25). Supports the IEEE 829 section enumeration used throughout this companion, including "features not to be tested", suspension and resumption, deliverables, and approvals ("sources of test data, inputs and outputs, testing techniques and priorities"). A vendor restatement of a superseded standard, used because the standard is not freely readable; it lists sixteen sections where reference [[42]](#ref-42) says fifteen, and this companion does not resolve the discrepancy. [vendor]

<a id="ref-9"></a>[9] Simon Knight. "[Test Planning Simplified](https://sjpknight.com/post/test-planning-simplified/)." sjpknight.com (accessed 2026-07-25). Supports the lean-plan case and the five questions any plan must answer regardless of length ("the value of the test plan is in the planning (i.e. the thinking), not the document"; "no plan survives first contact with the enemy"). No publication date displayed; the argument is framed for agile contexts. [practitioner]

<a id="ref-10"></a>[10] Yuri Kan. "[Entry and Exit Criteria in Software Testing: When to Start and Stop Testing](https://yrkan.com/blog/entry-exit-criteria/)." yrkan.com (accessed 2026-07-25). Supports the measurable-versus-vague contrast for criteria and the application of SMART to entry and exit conditions. No publication date displayed; no verbatim quotation is used from this source. [practitioner]

<a id="ref-11"></a>[11] LoadView Testing. "[Performance Testing Planning: Entry and Exit Criteria](https://www.loadview-testing.com/blog/performance-testing-planning-entry-and-exit-criteria/)." LoadView (accessed 2026-07-25). Supports the consequence of having no defined criteria ("Teams should not begin performance testing until entry and exit criteria are defined. Without clear criteria, it becomes difficult to know whether the test was valid, whether the results are acceptable, or whether more testing is needed."). Vendor content; its example criteria are performance-specific and are not carried into the template. [vendor]

<a id="ref-12"></a>[12] Michael Felderer and Ina Schieferdecker. "[A taxonomy of risk-based testing](https://arxiv.org/abs/1912.11519)." arXiv (submitted 2019-12-24; accessed 2026-07-25). Supports the purpose and framing of risk-based testing ("steer all phases of the test process in order to optimize testing efforts and limit risks"). arXiv preprint, not confirmed as journal-published; the taxonomy describes practice rather than prescribing it. [primary]

<a id="ref-13"></a>[13] Guru99. "[Risk Based Testing: Approach, Matrix, Process and Examples](https://www.guru99.com/risk-based-testing.html)." Guru99 (accessed 2026-07-25). Supports the practical mechanism by which risk tier selects test technique depth and execution order. No named author; the specific scoring model it presents is one approach among several, not a standard. [vendor]

<a id="ref-14"></a>[14] James Bach. "[A Question About Test Strategy](https://www.satisfice.com/blog/archives/63)." Satisfice, Inc. (published 2006-09-22; accessed 2026-07-25). Source of the plan-versus-document distinction that this companion is built around, and of Bach's three-way split ("The test plan document does not necessarily contain a test plan"; "Test plan: the set of ideas that guide a test project"; "Test strategy: the set of ideas that guide test design"; "Test logistics: the set of ideas that guide the application of resources"). Bach's use of "strategy" differs from ISTQB's [[6]](#ref-6); both are reported rather than harmonized. [primary]

<a id="ref-15"></a>[15] James Bach. "[Fighting Bad Test Documentation](https://www.satisfice.com/blog/archives/19)." Satisfice, Inc. (published 2004-02-21; accessed 2026-07-25). Supports the written-once-never-read critique from inside the craft ("Documenting is not testing. It is one of the chief distractions to testing."; "Test documentation is often of such poor quality that it's better ignored than followed."). This is a critique of heavyweight documentation, not of planning; read alongside [[16]](#ref-16) and [[17]](#ref-17). [primary]

<a id="ref-16"></a>[16] James Bach. "[Test Plan Evaluation Model](https://www.satisfice.com/download/test-plan-evaluation-model)." Satisfice, Inc. (originally published 1999-09-25; accessed 2026-07-25). Supports the fact that the best-known critic of test documentation published a rubric for assessing test plan quality ("I developed this model to provide a basis to systematically assess the quality of test plans."). **Landing page only: the model PDF was not read**, so no claim is made about its criteria. [primary]

<a id="ref-17"></a>[17] James Bach. "[How to Evolve a Context-Driven Test Plan](https://www.satisfice.com/download/building-a-context-driven-test-plan)." Satisfice, Inc. (landing page dated 2021-07-07; accessed 2026-07-25). Supports an iterative, order-independent model for building a test plan ("a process guide for creating a good test plan within the RST methodology. It consists of seven tasks. The tasks can be performed in any order, or simultaneously and iteratively."). **Landing page only: the guide PDF was not read**, so the seven tasks are not enumerated here. [primary]

<a id="ref-18"></a>[18] Jonathan Bach and James Bach. "[Session-Based Test Management](https://www.satisfice.com/download/session-based-test-management)." Satisfice, Inc. (originally published 2000-11-01; accessed 2026-07-25). Supports the session and charter as the unit of chartered exploratory work, and SBTM's activity-based framing ("activity-based test management which is an alternative to artifact-based management"). **Landing page only: the paper was not read.** Jonathan Bach is the primary author; attributing SBTM to James Bach alone is a common misattribution, and Michael Bolton is not a co-creator. [primary]

<a id="ref-19"></a>[19] Lisa Crispin. "[The Agile Testing Quadrants](https://lisacrispin.com/2024/10/11/the-agile-testing-quadrants/)." lisacrispin.com (published 2024-10-11; accessed 2026-07-25). Supports the quadrants' purpose as a planning aid, in the words of one of the two authors most associated with them ("a thinking tool that help teams plan and execute testing activities so that they can confidently deliver customer value"). [primary]

<a id="ref-20"></a>[20] Lisa Crispin. "[Agile Testing Quadrants version 3: From Agile Testing Condensed](https://lisacrispin.com/agile-testing-quadrants-version-3-from-agile-testing-condensed/)." lisacrispin.com (accessed 2026-07-25). Supports Crispin's own attribution of the model to Brian Marick ("based on Brian Marick's agile testing matrix"). No publication date visible on the page. [primary]

<a id="ref-21"></a>[21] Wikipedia contributors. "[Agile testing](https://en.wikipedia.org/wiki/Agile_testing)." Wikipedia (accessed 2026-07-25). Supports Brian Marick as the originator of the quadrant model, dated to his 2003-08-22 post, and the model's two-axis structure. [reference]

<a id="ref-22"></a>[22] Janet Gregory and Lisa Crispin. "[Agile Testing Condensed](https://leanpub.com/agiletesting-condensed)." Leanpub (page last updated 2019-09-24; accessed 2026-07-25). Supports that test planning survives as a named practice in the agile canon: the table of contents carries a chapter titled "Test Planning in Agile Contexts". **Book page only: the book itself was not read**, so only the chapter's existence and title are claimed. [primary]

<a id="ref-23"></a>[23] Ben Linders. "[Agile Approaches to Test Planning](https://www.infoq.com/articles/agile-approaches-test-planning/)." InfoQ, interviewing Eddy Bruin and Ray Oei (accessed 2026-07-25). Supports the strongest practitioner form of the no-test-plan-in-agile position ("Most test plans contain irrelevant and outdated information that does not contribute to quality." - Eddy Bruin; "When test plans are required in agile projects, it is a clear sign that it is not an agile environment to begin with." - Ray Oei). These are two named individuals' opinions in an interview, not a consensus position. [practitioner]

<a id="ref-24"></a>[24] James Bach. "[How Not to Standardize Testing (ISO 29119)](https://www.satisfice.com/blog/archives/1464)." Satisfice, Inc. (published 2014-08-25; accessed 2026-07-25). Supports the Stop 29119 argument at its sharpest ("The reason they have excluded us is that they know we won't agree to any simplistic standard based on templates or simple formulae."; "The burden is on those who claim that the craft can be standardized to study the craft and recognize and resolve the deep differences among us."). Explicitly adversarial, written at the campaign's peak. [primary]

<a id="ref-25"></a>[25] James Christie. "[Stop 29119 (tag archive)](https://clarotesting.wordpress.com/tag/iso29119-iso-29119-testing-software-testing-stop-29119-stop29119-testing-standards/)." Claro Testing (accessed 2026-07-25). Supports the compliance-without-content critique, the most actionable criticism for a template author ("The standard defines in great detail the process and the documents for testing, but fails to clarify the purpose of testing, the outcomes that stakeholders expect."; "It would be simple to comply with the ISO 29119 Test Completion Process, and produce a report that provided no worthwhile information at all."). Christie initiated the campaign; his framing is disputed by the standard's proponents. [practitioner]

<a id="ref-26"></a>[26] James Christie. "[Has opposition to ISO 29119 really died down?](https://clarotesting.wordpress.com/2018/07/21/has-opposition-to-iso-29119-really-died-down/)." Claro Testing (published 2018-07-21; accessed 2026-07-25). Supports that the opposition was not retracted four years after the campaign's peak. Written by a named critic, not a neutral observer. [practitioner]

<a id="ref-27"></a>[27] Huib Schoots. "[The ISO29119 Debate](https://associationforsoftwaretesting.org/2014/09/05/the-iso29119-debate/)." Association for Software Testing (published 2014-09-05; accessed 2026-07-25). Supports the accessibility objection, which explains why so few practitioners have read the standard they follow ("The standard is not available publicly. How can I comply to or even discuss a standard that is not publicly available?"). The standard's convenor published a counter-statement the same month. [practitioner]

<a id="ref-28"></a>[28] Michael Bolton. "[Dramatis Personae](https://developsense.com/blog/2014/09/dramatis-personae)." DevelopSense (published September 2014; accessed 2026-07-25). Supports the conflict-of-interest strand of the critique regarding working-group editors' commercial affiliations. The affiliations were disputed and no independent audit exists; this companion reports the dispute without adjudicating it. [practitioner]

<a id="ref-29"></a>[29] Cem Kaner, James Bach and Bret Pettichord. "[Context-Driven Testing: Principles](https://context-driven-testing.com/)." context-driven-testing.com (accessed 2026-07-25). Supports the canonical statement of the school behind the critique ("There are good practices in context, but there are no best practices."). No publication date on the page; proponents of 29119 dispute that these principles are incompatible with the standard. [primary]

<a id="ref-30"></a>[30] SD Times. "[The software testing schism](https://sdtimes.com/applause/software-testing-schism/)." SD Times (accessed 2026-07-25). Supports a both-sides account of the dispute and the gap the standard was intended to fill ("There was no definitive international set of software testing standards previously."; "Imposition of a 'standard' by one faction has potential to control who calls themselves a tester."). No date visible in the fetched body; covers the 2014 peak. [reference]

<a id="ref-31"></a>[31] Richard C Paterson. "[How to Write a Software Test Plan](https://www.ministryoftesting.com/insights/how-to-write-a-software-test-plan)." Ministry of Testing (published 2018-02-05; accessed 2026-07-25). Supports the reformist position that the unread plan is waste and the fix is a better document rather than none ("A test plan that no-one reads, which doesn't inform anyone about the testing to be done, is a waste of your valuable time."; "A document that is not read has little value."). [practitioner]

<a id="ref-32"></a>[32] Mykhailo Poliarush. "[QA Metrics: The Software Testing Metrics That Actually Matter](https://testomat.io/blog/qa-software-testing-metrics/)." Testomat.io (published 2026-06-11; accessed 2026-07-25). Supports the metrics trap in exit criteria, with the arithmetic that makes it concrete ("Test case count tells you almost nothing about quality. A test case that checks 'does the page load' is not equivalent to one that checks complex business logic."; "Pass rate alone is misleading. A pass rate of 98% in a suite of 200 tests means 4 tests failed."). Vendor-authored by a test management tool company; the critique is consistent with independent practitioner literature. [vendor]

<a id="ref-33"></a>[33] BrowserStack. "[Test Plan vs Test Case: Core Differences](https://www.browserstack.com/guide/test-plan-vs-test-case)." BrowserStack (accessed 2026-07-25). Supports the plan-versus-case boundary and the audience difference that makes it practical ("Test plans target Testers, Test managers and any Stakeholders, whereas test cases are primarily for the test team itself."). [vendor]

<a id="ref-34"></a>[34] Software Testing Magazine. "[Comparing Test Cases and Acceptance Criteria](https://www.softwaretestingmagazine.com/knowledge/comparing-test-cases-and-acceptance-criteria/)." Software Testing Magazine (accessed 2026-07-25). Supports that the acceptance-criteria-versus-test-case boundary is genuinely contested, quoted here as one side of a live disagreement rather than as the answer ("Based on all the definitions above, there's not a huge difference(if any) between test cases and acceptance criteria."; "If we already have testable ACs, why should we duplicate work in creating TCs for the same scenarios?"). [practitioner]

<a id="ref-35"></a>[35] AltexSoft. "[Test Plan vs Test Strategy: Structure, Goals and Differences](https://www.altexsoft.com/blog/test-plan-test-strategy/)." AltexSoft (accessed 2026-07-25). Supports the admission, from a source that draws the distinction, that many organizations carry the strategy as a section of the plan ("in some organizations test strategy can be just a part of the test plan document, identifying the test approach for the concrete project"; "the strategy does not change frequently if at all"). [practitioner]

<a id="ref-36"></a>[36] Software Testing Help. "[Test Plan Vs Test Strategy Vs Test Case Vs Test Scenario](https://www.softwaretestinghelp.com/difference-between-test-plan-test-strategy-test-case-test-script-test-scenario-and-test-condition/)." Software Testing Help (accessed 2026-07-25). Supports live practitioner disagreement about the plan/strategy ordering, visible in the article and contradicted in its own comments ("The difference between these two documents is subtle."; "In smaller projects, test strategy is often found as a section of a test plan."). [practitioner]

<a id="ref-37"></a>[37] Yuri Kan. "[Test Plan vs Test Strategy: Key QA Documents](https://yrkan.com/blog/test-plan-vs-strategy/)." yrkan.com (accessed 2026-07-25). Supports the most usable one-line formulation of the distinction ("the strategy defines how you test, the plan defines what you test this time"). The same page carries an unsourced "42% of QA teams" statistic which is deliberately not used in this bundle. [practitioner]

<a id="ref-38"></a>[38] Microsoft. "[Test objects and terms overview](https://learn.microsoft.com/en-us/azure/devops/test/test-objects-overview?view=azure-devops)." Azure DevOps documentation (accessed 2026-07-25). Supports the terminology trap: in the tool, a test plan is an execution container ("Test plans: Group test suites and individual test cases."; "The only required field for all work item types is Title."; "A test point is a unique combination of a test case, test suite, configuration, and tester."). [primary]

<a id="ref-39"></a>[39] Microsoft. "[Create and manage test plans](https://learn.microsoft.com/en-us/azure/devops/test/create-a-test-plan?view=azure-devops)." Azure DevOps documentation (accessed 2026-07-25). Supports what the tool actually requires to create a "test plan": a name, an area path and an iteration ("Create test plans and test suites to track manual testing for sprints or milestones."). No approach, risk or criteria fields are required. [primary]

<a id="ref-40"></a>[40] Tricentis. "[Test Plan for Releases and Builds](https://docs.tricentis.com/qtest-saas/content/manager/test_plan/test_plan_for_releases_and_builds.htm)." qTest Manager documentation (accessed 2026-07-25). Supports a second, independent tool modeling a "test plan" as a milestone calendar ("each project within qTest Manager has its own Test Plan in which you can define the high-level milestones and testing objectives"). [vendor]

<a id="ref-41"></a>[41] TestQuality. "[The Ultimate Test Plan Tools in Software Testing: A Practical Guide](https://testquality.com/the-ultimate-test-plan-tools-in-software-testing-a-practical-guide/)." TestQuality (accessed 2026-07-25). Supports the vendor framing that the plan now lives inside the platform ("They serve as living documents that guide the entire testing process from requirements gathering through execution and reporting."). Vendor content with a direct commercial interest in that claim. [vendor]

<a id="ref-42"></a>[42] Wikipedia contributors. "[Test plan](https://en.wikipedia.org/wiki/Test_plan)." Wikipedia (accessed 2026-07-25). Supports a general definition of the document type and the observation that its major elements overlap with a formal test strategy ("a document detailing the objectives, resources, and processes for a specific test session for a software or hardware product"; "These three elements are also used in a formal test strategy"). States that IEEE 829-2008 specifies fifteen required sections, against the sixteen enumerated in [[8]](#ref-8). [reference]
