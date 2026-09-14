# Guide: Test Summary Report (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`test-summary-report_companion.md`](test-summary-report_companion.md). A fully worked instance is
[`test-summary-report_example.md`](test-summary-report_example.md).

## When to use

**Read this first, because it changes what the card is claiming.** The international standard that defines
this document type is one a named school of practitioners campaigned to have withdrawn. In 2014 a petition
organised by the International Society for Software Testing,,
asked ISO to suspend publication of Parts 4 and 5 of ISO/IEC/IEEE 29119 and to **withdraw Parts 1 to 3** -
which includes the part that defines this report. Michael Bolton, a leading voice of the opposition,
described that standard as an *"overstructured process model, focused on relentless, ponderous, wasteful
bureaucracy and paperwork, with negligible content on actual testing"*. So nothing on this card says the test
report is settled practice. It says how to write one worth reading if you are writing one, and it takes the
opposition's sharpest charge as the thing to design against rather than the thing to ignore. Both camps:
[companion section 6](test-summary-report_companion.md#6-debates-and-contested-boundaries).

**And one thing about where the section list came from.** That standard is sold, not published. What this
bundle read of it is its Clause 3 definition and its table of contents, which is a list of subclause
*headings* and not the requirements underneath them. The sections you are about to fill come from ISTQB's
freely published foundation-level syllabus, from real filled reports, and from published templates - not
from the standard's unread text. The full retrieval position is
[companion section 1](test-summary-report_companion.md#1-orientation), and it is worth two minutes before
you cite anything from this bundle to anyone.

Write one when:

- **A testing effort has ended** - a release, a cycle, a level, a milestone - and someone has to say whether
  the bar the test plan set was cleared.
- **The result has to travel** past the people who watched it happen: to another team, to a sponsor, to a
  customer, to the version of your own team that exists in six months.
- **A sign-off, an audit, a certification or a regulatory submission** is downstream, and this report is part
  of the evidence rather than a courtesy.
- **Something was not tested**, and a reader who is not told will assume it passed.
- **Residual risk is going to production** and somebody needs to be on record accepting it, by name.
- **The engagement is closing or the team is dispersing**, so this is the durable record of what was actually
  verified and on which build.

## When NOT to use

**Write something else if:**

| You actually need | Because |
|---|---|
| a **[test plan](../test-plan/test-plan_guide.md)** | **the testing has not happened yet.** The plan is prospective: scope, approach, entry and exit criteria, agreed before the work starts. This report is its closing bookend and is retrospective. The dependency runs one way and it is structural: this report's Evaluation Against Exit Criteria section has content only because a plan wrote criteria. Reaching for this template before the cycle means you wanted that one |
| a **[bug report](../bug-report/bug-report_guide.md)** | **one verification failed** and an engineer needs to reproduce it. That is one document per defect, carrying steps, environment, and expected against actual. This report counts and characterizes defects by severity and says which remain open; it links to them and never accumulates their reproductions |
| a **test status or progress report** | **testing is still running.** A progress report is produced at regular intervals against the plan's baseline so that somebody can intervene while intervening is still possible; this document is produced once, at the end, and judges. If you are writing the same document every Friday you are writing progress reports, and the completion report is still owed at the end. This library ships no template for one, and its [`status-report`](../status-report/status-report_guide.md) is not it: that is the project-level periodic update for a different reader |
| **nothing** | **a pipeline already publishes the numbers and nobody needs a judgment on top of them.** If the dashboard is live, the readers watched it all cycle, and nobody will be asked later to defend the release decision, then a message carrying the exit-criteria call and the residual-risk list does the entire job. A report that only restates the dashboard is strictly worse than the dashboard, because it is also out of date the moment you send it |

**The threshold, stated plainly.** A tool vendor's own framing of when the formal document earns its cost is
the one this bundle adopts: it becomes useful when results need to be shared *"beyond a single iteration or
the immediate team"*, or to support an audit, a customer sign-off, a regulatory review or a contract. Below
that line, do not write one. Writing it anyway is how the document type earned its reputation.

## The ship call has no section of its own

If you are looking for a **Release Recommendation** heading, it is deliberately not here, and knowing where
the call went is the difference between filling this template correctly and thinking a section is missing.

**The ship sentence goes at the end of Evaluation Against Exit Criteria**, underneath the criteria it rests
on, in this shape: which criteria were met, which were not, and *therefore* ship, do not ship, or ship with
these named conditions carried by this named person. One line on why: a recommendation with nothing above it
is an opinion, and the same sentence under a graded criteria table is a conclusion.

This library considered a standalone section, tested the idea against its own research, and dropped it -
neither readable structural source carries one, and the real filled reports in the corpus do not either, with
one certification-lab exception the companion explains. The evidence and the change of mind are in
[companion section 3](test-summary-report_companion.md#3-anatomy-section-by-section).

What this does not change: the [test plan](../test-plan/test-plan_guide.md) card promises that what you found
and whether you are shipping belong in a report written afterwards. They do. The verdict simply does not get
a heading of its own.

## Pick a variant

**Lean (six sections)** is the default: Scope and What Was Tested, Execution Summary, Defects, Deviations
from Planned Testing, Evaluation Against Exit Criteria, and Residual Risk and What Was Not Tested. That is
what closing a release actually takes - what it was, what ran, what broke, what did not happen as planned,
whether the bar was cleared, and what is being carried forward.

**Full (nine sections)** adds Impediments and Blocked Progress, Test Deliverables and Reusable Assets, and
Lessons Learned. Reach for it when at least one of these is true:

- the reader is an auditor, a regulator, a customer or an accreditation body, and completeness is part of the
  evidence rather than a style preference;
- testing was done by a vendor, a lab, or more than one team, so who tested what belongs in the record;
- the assets outlive the release and the next team inherits the suites, harnesses, fixtures and environments;
- the reader was not there, and this report is the durable record rather than a step in a conversation that
  continues;
- no retrospective is going to happen, so this is the only place the learning survives.

Nesting is strict: every lean heading appears in the full variant with the same name in the same order, and
full only adds. A lean report grows into a full one without rewriting a line of what is already there.

**Two sections are never the ones you cut**, whichever variant you pick: **Evaluation Against Exit Criteria**
and **Residual Risk and What Was Not Tested**. Those are the two your tooling cannot produce, and they are
the reason the document exists at all. If the whole budget is one paragraph, write those two and link the
dashboard for the rest.

## Quality rubric (self-grade before you send it)

Score each 0, 1 or 2. Under 13 out of 18 and what you have is a dashboard with a cover page: the reader gets
counts they already had, and none of the three judgments only a person can make - what was not tested, what
risk is being accepted, and whether the bar was cleared.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Build is named** | No version, build or commit anywhere in the document | A version, but no environment and no reference to the plan it answers | A reader six months from now can name the build, the environment and configuration, the period tested, and the plan whose criteria this grades |
| 2 | **Claim is bounded** | Nothing says what the result does not cover | A scope line that restates the feature name and stops | The report says what configuration and version the result applies to, and names at least one thing a reader must not read it as covering |
| 3 | **Coverage claim honest** | "Coverage" is a pass percentage wearing a different word | Coverage is stated, but only against the cases in your own suite | Coverage is stated against something outside the suite - risks, requirements, areas, code - and where breadth was traded for depth, the report says which |
| 4 | **Defects are summarized** | A tracker export pasted in, or a single total | Counts by severity | Severity and pattern, what is still open, who owns each open item, and links out to the reports rather than their reproductions retyped here |
| 5 | **Deviations are filled** | Empty, or "none" on a cycle that visibly slipped | Says the plan changed | Names what was planned and not done, what was done instead, and why - enough that the counts above can be read correctly rather than taken at face value |
| 6 | **Criteria graded individually** | Prose about how the cycle went | One summary judgment covering all criteria at once | Every exit criterion the plan set appears with met or not met and the evidence for it, including the ones that were not met |
| 7 | **Conclusion follows criteria** | No conclusion, or one that contradicts the grades above it | A conclusion is stated, with nothing tying it to any criterion | The ship sentence sits under the graded criteria, names its conditions and who is accepting them, and a reader can point at the grade that would flip it |
| 8 | **Residual risk owned** | Not mentioned, or written as an apology for running out of time | Untested areas listed, with no consequence attached | Each item says what could go wrong, who is accepting it and on what basis, and Undetermined appears wherever that is the honest answer |
| 9 | **Adds beyond the dashboard** | Everything here was already in the tool | One section carries something the tool could not compute | A reader who had the dashboard open all cycle still learns something, and could point at where |

The test behind every cell above: **could someone satisfy it without improving the report?** A row that
counted defects, or counted exclusions, would reward padding, and a forty-row defect table nobody triaged
would score the same as one honest paragraph. Every cell instead asks whether a specific piece of evidence is
there and whether a second person, not the author, could find it.

## Named anti-patterns (the usual wrecks)

1. **The dashboard with a cover page.** Execution Summary filled in, everything else thin or absent. The tell
   is that a reader could have learned more by opening the tool, and that your document was out of date
   before it was sent. This is the failure the whole document type stands accused of, so it is the one to
   check for first. Fix: write only what the tool cannot compute, and if that leaves nothing, do not write
   the report.
2. **Coverage claimed, pass rate measured.** "96 percent coverage" where what was measured is the proportion
   of executed tests that passed. These are two different claims about two different things: pass rate is a
   property of the tests you chose to run, and coverage is a claim about the system, stated against risks,
   requirements, areas or code. A suite exercising a tenth of the product can post a perfect pass rate, and a
   reader who reads that as coverage treats untested ground as cleared. The security assessment in this
   bundle's research shows the honest form: it discloses that *"codebase coverage emphasized breadth instead
   of depth"* and that portions outside the control areas received minimal to no coverage. Fix: name the
   denominator, and where the denominator is your own suite, say so in the same sentence.
3. **Silence read as coverage.** Areas nobody tested go unmentioned, so a reader assumes they passed. Related
   to the one above and not the same: that one overclaims, this one omits, and omission is the easier of the
   two to commit by accident. Fix: an explicit not-tested list with a reason against each item, sitting in
   the same section as the residual risk it creates.
4. **Complete and empty.** Every heading present, nothing decided, because the template asked for a heading.
   James Christie's critique aimed squarely at this document type describes the result as *"a collection of
   metrics that say nothing about the quality of the product"*, and he is describing reports that complied
   with the standard rather than reports that ignored it. Fix: delete any section that decides nothing, and
   make the exit-criteria evaluation carry an actual "therefore".
5. **The verdict with nothing above it.** A confident release call resting on numbers that do not support it,
   or on no criteria at all. This is exactly the failure that the missing Release Recommendation heading is
   designed to prevent, and moving the sentence does not prevent it by itself. Fix: grade the criteria first;
   the call is the last line of that section, never the first line of the report.
6. **Residual risk written as apology.** "Unfortunately we ran out of time for the migration path." That is a
   schedule confession, not a risk statement: it explains why a gap exists and says nothing about what the
   gap could cost or who is carrying it. Fix: name the exposure, the person accepting it, and the basis for
   accepting it. The regulated form of this is a written risk-based rationale for every defect left unfixed,
   and it is a good shape to borrow even when nobody is making you use it.

## Pairing with a skill

`pairs_with: []`, and the empty list is a finding rather than an omission. There is **no testing or QA skill
in the `pm-skills` library**: none of its tracked skills produces a test plan, a test case, a bug report or a
test report, recorded as finding EC-4 (pm-skills covers no testing or QA work) in this repository's
`STATE.md`. The [test plan](../test-plan/test-plan_guide.md) bundle can honestly claim
`deliver-edge-cases`, because an edge-case catalog is an input to planning coverage. A report of testing
already finished has no such input to take, so this bundle declines the pairing rather than borrowing its
sibling's. Everything here is filled by hand, from your test plan, your defect tracker and your tool's run
data.
