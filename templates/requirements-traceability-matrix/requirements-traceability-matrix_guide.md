# Guide: Requirements Traceability Matrix (operator card)

Fast reference for using the requirements-traceability-matrix bundle. For the full reasoning, the
disagreements between sources, and the citations, read
[`requirements-traceability-matrix_companion.md`](requirements-traceability-matrix_companion.md).

**Decide whether to keep a matrix before you fill one in.** This type is contested. Named practitioners
say it rarely repays its upkeep, this library's research found no named software team outside regulated
or safety-critical work that describes keeping one (high confidence that the search found none, medium
that none exists), and no source read shows that keeping one improves outcomes. The case this bundle can make is narrow: where a team has decided it owes a whole-set answer to
the question "which requirement has no verification", a table is one way to give it. Read When NOT to use
first. That recommendation is this library's position, not a measured finding.

## When to use

- The team has decided that someone, such as a release reviewer, an auditor or the team itself, is owed
  a single answer to "which requirement has no verification", and a requirement with no test must be
  visible in that answer. A table with one row per requirement shows it, and a test case's own
  traceability field cannot, because a requirement with no test has no test to hold the field. That
  reasoning is this library's inference, and no source states it.
- The requirement set is bounded: one feature, one release, or one product area. A bounded matrix is this
  library's way of applying NASA's value-based tracing.
- The work is regulated or safety-critical. The sources that say traceability is owed, or that publish a
  matrix, are regulated practices. Whether any standard requires a matrix was not read.
- No tracker already holds the requirement-to-test links, or you can state in one sentence what this file
  adds that the tracker does not.

## When NOT to use

- **The team is unregulated and cannot name a reason.** If the Purpose and Boundary section cannot say what
  you chose to trace, what you chose not to, and when you will stop, do not start. Companion section 6 gives
  the conditions Ambler names.
- **A tracker already holds the links.** Name the tracker as the record, and do not keep a copy. A table
  that restates links held elsewhere creates a second record that can disagree with the first. That
  reasoning is this library's own.
- **The situation is simple.** Ambler says that where people know the system, it is "much easier and cheaper
  to simply ask them to estimate the change". In this library's view, a solo or very small team should treat
  the lean size as the largest to consider, and no matrix may be the right answer.
- **You want NASA's requirements verification matrix.** It is scoped to "shall" statements and records how
  each is verified. It is a related artifact, and this bundle's template is not a copy of it.
- **You want proof that the matrix improves outcomes.** Nothing read supplies it. See companion section 6.

## Matrix, or somewhere else?

Several things a reader might expect in a traceability document already have a home elsewhere. The
matrix owns the current links, and it owns nothing else. Each line below is this library's position
unless noted.

| You want to record | It belongs in |
|---|---|
| The current link from each requirement to what verifies it, across the whole set | This matrix |
| The link from one test to what it verifies | The `test-case` bundle's own traceability field. The matrix reads it as input |
| The dated result of one test cycle | The `test-summary-report` bundle. A report is a dated result of one cycle, and a matrix row stays open. No source states this boundary directly |
| The decision to change a requirement, and who agreed | The `change-log` bundle. The change log records the decision, and the matrix records the current links |
| A risk's likelihood, impact and owner | The `risk-register` bundle. The full variant's Risk Control Trace links to it by identifier and copies no score |
| The requirement's own text | The source document, such as the `prd`, `user-stories` or `acceptance-criteria` bundle. NASA's handbook says "do not duplicate requirements in the traceability matrix" |

A matrix that starts carrying risk scores, issue status or metric definitions has begun to collapse into
a neighbouring governance-docs member, which the family contract warns against.

## Pick a variant

- **Lean** (default): Purpose and Boundary, Trace Conventions, The Matrix, Coverage Gaps, and Upkeep and
  Review Trigger. A requirement-to-test table read in both directions, the narrowest definition in the
  sources, with the rules that give its status words a meaning and the owner who keeps it current. Start
  here unless you owe an answer the lean table cannot give.
- **Full**: adds **Implementation Trace** (each requirement to its design reference and its code or task
  reference), **Risk Control Trace** (each risk to the requirement that controls it and the test that
  verifies the control) and **Baselines** (dated snapshots of what a release or an audit saw). Move to
  full when the team owes one of three answers: which design element implements this requirement, which
  control covers this risk, or what an auditor saw at a given release. Without such a question, lean is
  enough.

Grow lean into full by inserting the three sections after Coverage Gaps and before Upkeep and Review
Trigger; the five lean sections keep their name and order. Confidence that this split is right is
medium-low: no source read shows a template that carries every link type, so the split is this library's
hypothesis and not a sizing rule any source states.

Three cautions on the full sections:

- **Drop Implementation Trace when a tracker already holds the links.** Write "N/A" and one line saying
  which tracker is the record.
- **Risk Control Trace has the thinnest support of any section.** The only sources are one
  medical-device vendor and the FDA's reference to a trace to "risk analysis results". No general
  software source read asks for it. Use it only when a risk register already exists, and write "N/A, no
  risk register exists for this product" otherwise.
- **Baselines suits a team with audits or formal releases.** A snapshot of an out-of-date table keeps the
  out-of-date table, so reconcile the table before you snapshot it.

## Quality rubric (self-grade)

Score each row 0, 1, or 2. Below 17 out of 24, a reader who opens the matrix to learn which requirement
has no verification cannot trust the answer: a requirement may have no row, a status word may mean only
that a test exists, or the table may have drifted from its sources with nothing in the file to show it.
A lean matrix carries no Implementation Trace, Risk Control Trace or Baselines section to grade, so it is
scored, and cleared, against a smaller table; see the scope table below.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Reason to keep it** | Purpose and Boundary says what the matrix covers but gives no reason the team keeps one | A reason is given, but nothing says what was left untraced, or what ends the matrix | You can point at the sentence giving this team's reason, the sentence naming what was left untraced, and the stated event that ends it, so a reader could tell from the file alone when to delete it |
| 2 | **One named record** | Nothing says whether this file or a tracker holds the links | A record is named, but the file does not say what it adds beyond the tracker, or what the tracker holds instead | You can point at the sentence naming where the links are authoritative and, where a tracker holds any of them, the sentence saying what this file adds that the tracker does not |
| 3 | **Verified is defined** | No definition of verified or covered appears, or the status words are used undefined | A definition exists, but a row could meet it on a linked test alone, with no statement of what the test had to do or what evidence is kept | You can point at the sentence, and say what evidence a verified row rests on beyond a linked test, so two people reading the same row would mark it the same way |
| 4 | **Other means marked** | A requirement checked by inspection, analysis or demonstration is shown as a gap, or is marked verified with no record of the check | A status for other means exists, but names no record of the check | You can point at a requirement checked by other means, see its status and the record named, or point at the sentence saying no requirement here is checked that way |
| 5 | **Every requirement has a row** | A requirement you pick from the source document that has no test cannot be found in the table | Rows exist for the requirements you check, but no rule says which statements of the source count as requirements, so you cannot tell whether others are missing | A requirement you pick from the source document that has no test has its own row with an empty Verified by cell, and the scope rule tells you which statements were counted |
| 6 | **Links, not copies** | Rows copy the requirement's full text, or the Source cell is blank | Labels are short, but some Source cells point nowhere a reader can open | For any row you can open the Source cell's target and find the requirement's full text there, and the row carries only the source's own identifier and a short label |
| 7 | **Status follows definition** | A row marked verified has an empty Verified by cell, or names a test that has not run | Verified rows name a test, but the evidence the definition asks for cannot be found from the row | Pick any verified row: you can follow its Verified by cell to a test result or an other-means record, and confirm the condition in Trace Conventions is met, without asking the keeper |
| 8 | **Gaps have decisions** | Coverage Gaps is blank, or lists gaps with no owner and no decision | Requirements with no verification have owners and decisions, but nobody checked the tests against the requirements | You can point at the line showing the tests were checked against the requirements, naming each test with no requirement or stating none was found and when; every gap has a named owner and a recorded decision |
| 9 | **Current against changes** | No owner, no update events or no reconciliation date appears, or the section says only "updated as needed" | An owner, events and a date are given, but the date is older than the latest change to the requirements or tests, or the only trigger is a calendar interval | You can point at a named owner, the events that force an update and a date last reconciled, and comparing that date with the newest change in the source documents or test records shows the table was reconciled after it |
| 10 | **Implementation references open** *(full)* | Cells say "done" or "in code", or copy design text or ticket titles | References are present, but some point nowhere a reader can open, or a requirement with no reference is left unmarked | For any row you can open the design reference and the work reference; a requirement with neither is marked as a finding; or the section says N/A and names the tracker that is the record |
| 11 | **Risk links by ID** *(full)* | Risk likelihood or impact is copied into the table, or a risk has no register identifier | Register identifiers are used, but a risk with no controlling requirement, or a control with no verifying test, is left unmarked | Every risk row carries the register's own identifier, the controlling requirement and the verifying test, a missing link is listed as a finding, and no score appears; or the section says N/A because no risk register exists |
| 12 | **Dated baselines** *(full)* | A baseline is mentioned with no date and no location | A date and an event are given, but the location or the reviewer is missing, or the copy's own last-reconciled date is later than its snapshot date or is absent | For each snapshot you can open the copy at the stated location and see its date, the release or review, and who reviewed and approved it, and the copy's own last-reconciled date is on or before the snapshot date |

### Rubric scope by variant

| Variant | Rows scored | Maximum | Threshold |
|---|---|---|---|
| lean | 1-9 | 18 | 13 |
| full | 1-12 | 24 | 17 |

Lean ships no Implementation Trace, Risk Control Trace or Baselines section, so rows 10 through 12 grade
content it does not carry; score a lean matrix against rows 1 through 9 only. A lean matrix at 13 out of
18 clears a comparable bar to a full matrix at 17 out of 24.

## Named anti-patterns

Each of these is a failure mode a source describes or this library infers. None is measured for how
common it is.

1. **Copying requirement text into the matrix.** NASA's handbook says "do not duplicate requirements in
   the traceability matrix". In this library's reasoning, a copy that drifts from the source document turns one requirement into two.
   Fix: a short label and a link to the source, which owns the text.
2. **Treating a linked test as a verified requirement.** A test case identifier in the Verified by cell
   shows that a test exists. NASA ties the completion of verification to "documented objective evidence of
   compliance with requirements or waiver" and to closure of nonconformance reports. A table full of
   green rows can hide requirements nobody verified. Fix: define verified in Trace Conventions in terms
   of evidence, and mark a row only when its cell meets that definition.
3. **Filling rows only for requirements that already have a test.** The table then shows the team's
   tests and not its requirements, and the requirement nobody verified is the one missing from it. Fix:
   build the rows from the source document's requirements, and leave Verified by empty where nothing
   verifies the requirement.
4. **A forward-only matrix.** Orcanos, a vendor selling a medical-device platform, says "An RTM that only
   maps forward is incomplete." That is one vendor's claim, in an audit frame, and no source read
   measures how common it is. A row-per-requirement table cannot show a test with no requirement,
   because that test has no row. Fix: check the tests against the requirements and record each orphan test
   in Coverage Gaps.
5. **Flagging a gap and leaving it.** NASA's guidance is that orphans are discussed by the project team
   and assurance personnel, and that a missing requirement found to be necessary is added. A gap with no
   owner and no decision is a list of worries. Fix: an owner and one decision per gap, and a one-line
   statement with a date when the list is empty. An empty list is only as good as the rows and the
   definition of verified behind it.
6. **Letting the table go stale.** NASA warns that manual methods "do not include automatic updates", so
   the project has to be diligent about keeping traces current. No source gives a calendar interval, and
   none says how fast a hand-kept table goes stale. Fix: a named owner, a list of events that force an
   update, and a date last reconciled, compared against the last change to the requirements or tests.
7. **A matrix kept for its own sake.** A team that cannot say what it chose to trace, what it chose not
   to trace and when it will stop is keeping the table because tables are kept, and the file drifts into a
   second copy of whatever the tracker already says. Fix: write the three sentences in Purpose and
   Boundary, and if they cannot be written, drop the matrix.
8. **A requirement without an identifier.** A statement with no ID has no row, so nothing can trace to
   it. That the loss goes unseen is this library's inference. Fix: assign an identifier before the
   statement is traced, and record the decision in the table.
9. **Copying risk scores into Risk Control Trace** *(full)*. The score then lives in two places, and the
   copy goes stale the first time the risk register changes. Fix: reference the risk by its register
   identifier and leave likelihood, impact and owner in the register.
10. **Baselining a table that has not been reconciled** *(full)*. The snapshot preserves the stale
    table and gives it the weight of a reviewed record. Fix: reconcile first, record the reconciliation
    date, and then take the snapshot.

## What this guide does not settle

Whether a matrix pays for itself outside regulated work, who may mark a row verified, what review interval
to use, and what any standard requires are all unsettled by what was read. Companion sections 2, 3 and 6
state them.

## No paired skill (yet)

This bundle's family contract states plainly that no governance skill exists in pm-skills today for any of
its members, so every member adopts `pairs_with: []` until one does. Until a governance-side skill exists,
this template is filled by hand.
