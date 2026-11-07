# Companion: The Requirements Traceability Matrix

> The deep explainer for the requirements-traceability-matrix bundle. Read this to understand what the
> matrix is, why this bundle draws its boundary where it does, and where the sources disagree about
> whether it is worth keeping at all. The short operator card is
> `requirements-traceability-matrix_guide.md`; a fully worked instance is
> `requirements-traceability-matrix_example.md`. Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation + TL;DR

A requirements traceability matrix is a table that lists a product's requirements and shows, for each
one, what verifies it and, in the wider form, what implements it. Its job is to make a requirement with
no verification visible. The narrowest definition in the sources is TestDevLab's: "A Traceability Matrix
is a document that links and maps project requirements to their corresponding test cases." [[5]](#ref-5)
Visure, a tool vendor, defines it more widely as "a structured document or tool designed to establish and
maintain traceability" [[4]](#ref-4). Jama, another vendor, calls it "a structured information artifact"
[[14]](#ref-14). In this library's reading, it is a standing register, edited as requirements and tests
change, not a record filed once at the end of a phase.

- **Traceability is a property, and the matrix is one way to hold it.** NASA defines traceability as "A
  discernible association among two or more logical entities such as requirements, system elements,
  verifications, or tasks." [[2]](#ref-2) InfoQ reports Brad Appleton making the same split: "Traceability
  matrix on the other hand is one of the possible implementations of traceability." [[13]](#ref-13) NASA's
  own guidance says "While traceability matrices are not the only method for capturing bidirectional
  traceability, they are the most common." [[6]](#ref-6) That is NASA's statement, and this research
  found no measurement behind it.
- **This type is contested, and its best evidence comes from regulated work.** Named practitioners say it
  rarely repays its upkeep, and Ambler says so of simple situations in particular [[10]](#ref-10). This
  research found no named software team outside regulated or safety-critical work that describes keeping
  one. In this library's reading, the strongest cases read for a matrix come from regulated practices and
  from vendors who sell a live replacement for it. Confidence: high that this search found no such
  team, medium that none exists.
- **Nothing read shows that keeping a matrix improves outcomes.** The nearest thing to evidence is a
  mapping study of 63 papers, and its authors say that "strong empirical evidence from industry is needed
  to validate the impact of traceability on maintenance and evolution" [[16]](#ref-16).
- **A linked test is not the same as a verified requirement.** NASA ties completion of verification to
  "documented objective evidence of compliance with requirements or waiver" and to "closure of all
  discrepancy and nonconformance reports" [[22]](#ref-22). This is the bundle's sharpest teaching point,
  and Trace Conventions below carries it.
- **The first use of the phrase is not established.** Section 2 says so plainly and does not offer an
  origin story.
- **The honest case for the matrix is narrow.** Where a team has decided it owes a whole-set answer to
  the question of which requirement has no verification, a table is one way to give it. Where a tracker already holds
  the links, that tracker is the record. The guide leads with who should not keep one.

---

## 2. Origins and evolution

No source read for this bundle shows where the phrase "requirements traceability matrix" began, who first
used it, or which field published the first one. This companion does not supply an origin, because a
confident story here would be invented. Leads that surfaced only on low-authority pages were not
verified, and this companion does not repeat them. Confidence that the origin is unestablished in what
was read: high.

What the sources do show is the practice, in a government engineering handbook, in a regulator's
guidance, and in tertiary summaries of standards.

**The practice appears in NASA's software handbook as a requirement.** NASA states that the project
manager "shall perform, record, and maintain bidirectional traceability between the software requirement
and the higher-level requirement." [[1]](#ref-1) The handbook gives its definition of traceability by
quoting ISO/IEC/IEEE 24765:2010: an "association among two or more logical entities that is discernible
in either direction (to and from an entity)" [[1]](#ref-1). That definition is NASA's quotation of the
standard. This research did not read the standard itself. NASA also states a reason in plain terms: "Full
requirements test coverage is virtually impossible without some form of requirements traceability."
[[1]](#ref-1)

**The practice appears in the FDA's 2002 software validation guidance, without the word matrix.** The
guidance says "A software requirements traceability analysis should be conducted to trace software
requirements to" and continues "(and from) system requirements and to risk analysis results."
[[3]](#ref-3) The document never uses the word matrix. The copy read carries a note that 21 CFR part 820
was amended, so the guidance predates the current rule. This research did not read 21 CFR 820.30 or the
rule that replaced it, and this companion says nothing about what either requires.

**Standards are cited for existence only.** Wikipedia's summary of the IEEE 829 test documentation set
lists no document that is a traceability matrix [[20]](#ref-20), and Wikipedia describes a matrix
generally as "correlating any two baselined documents using a many-to-many relationship comparison"
[[19]](#ref-19). Both are tertiary summaries. The standards themselves were not read, and so nothing here
says what IEEE 829, IEEE 830, ISO/IEC/IEEE 29148 or DO-178C requires.

**The conversation changed over time, and the dates are the only evolution the sources support.** The
earliest dated source here is the FDA's 2002 guidance [[3]](#ref-3). In 2008 a group of agile
practitioners argued against the matrix, and InfoQ reported it [[13]](#ref-13). Johanna Rothman wrote
about lighter ways of keeping traceability the next month [[11]](#ref-11). From 2021 onward the voices change. Tian and colleagues mapped the research literature
[[16]](#ref-16), Fucci and colleagues published an industrial experience report in 2022 [[12]](#ref-12),
and a vendor argued in 2023 that the matrix should be a living artifact [[15]](#ref-15). Jama republished
its version of the argument in 2026 [[14]](#ref-14), and says "Systems engineering teams are shifting away
from a document-centric approach" [[14]](#ref-14). That is Jama's description of its field, offered in
support of its own product, and nothing read measures the shift.

**One related artifact is not this one.** NASA's Systems Engineering Handbook has a requirements
verification matrix in its Appendix D, scoped this way: "Only “shall” requirements should be included in
these matrices." [[2]](#ref-2) It records how each statement is verified and keeps validation in a
separate matrix. This bundle does not treat that verification matrix as the requirements traceability
matrix. It shares the name's second half and part of the job, and a reader who finds it should not read
it as this type's template.

---

## 3. Anatomy (section by section)

The template's full variant carries eight sections. The lean variant carries five of them: Purpose and
Boundary, Trace Conventions, The Matrix, Coverage Gaps, and Upkeep and Review Trigger, in that order, as
a strict ordered subset of the full variant's eight. The full variant adds Implementation Trace, Risk
Control Trace and Baselines between Coverage Gaps and Upkeep and Review Trigger.

**A caution about the section design.** Neither the Visure page [[4]](#ref-4) nor the TestDevLab page
[[5]](#ref-5) shows a table beyond the requirement and test pair, and this research found no column-header
row in the pages it read. The recurring pair is requirement and test.
Visure adds "Requirements ID and Description", "Source of Requirements" and "Development Tasks and
Deliverables" [[4]](#ref-4). The question of whether any single template carries design, code, test and
risk-control links has no direct answer in what was read. The columns below are this library's assembly
from several partial lists, and not any one source's shipped layout.

### Purpose and Boundary

**What it is:** a short statement of the product and the requirement set the matrix covers, who keeps it,
and whether this file or a tool is the record. **Why it exists:** because the sources disagree on what
the matrix is. TestDevLab describes a requirement-to-test table [[5]](#ref-5), Visure describes a
structure reaching "Development Tasks and Deliverables" [[4]](#ref-4), and Jama argues that a static
document is the wrong form and a live view of tool data is the right one [[14]](#ref-14). A reader needs
to know which of these the file claims to be. The boundary statement is this library's POSITION, drawn
from Jama's live-view argument. No source read asks for such a statement.

*Beginner note.* Write down which product and which requirements the table covers, then name the one
place that is the record. If the team's tracker holds the links, say that, and say what this file adds.
NASA says a matrix "can be manually created and maintained, or may be a by-product of a requirements
management tool" [[6]](#ref-6), so both are recognised forms.

*Expert note.* This section is also where an unregulated team justifies the matrix to itself. Ambler,
writing in his own essay, says a traceability matrix "is effectively a document and is therefore a
business decision to be made by them" [[10]](#ref-10). NASA offers a narrower route for projects with
limited budgets: "Value-based requirement tracing may be an option for projects with small budgets", which
"can save a significant amount of effort by focusing traceability activities on the most important
requirements." [[6]](#ref-6) An honest Purpose section therefore says what the team chose to trace, what
it chose not to, and when it will stop keeping the matrix. If those three sentences cannot be written, the
matrix may not be worth keeping.

### Trace Conventions

**What it is:** the identifier schemes for requirements and tests, the scope rule for what counts as a
requirement, a statement of what counts as verified, and the status vocabulary. **Why it exists:**
because a table of links is only as meaningful as the rules that decide what a link means. In this
library's reading, the other sections depend on it, and no source read gives a template for it. The section's form
is this library's POSITION, assembled from the supports below.

- **Unique identification.** Visure lists "Requirements ID: A unique identifier assigned to each
  requirement for easy tracking and reference." [[4]](#ref-4) NASA says of its verification matrix that
  it "should identify each “shall” by unique identifier and be definitive as to the source"
  [[2]](#ref-2). That sentence is about the verification matrix, and it is cited here for the idea and
  not as a rule for this type.
- **Scope.** NASA's verification matrix includes only "shall" statements [[2]](#ref-2). A requirement
  matrix has to decide which statements count as requirements, and the section records the decision.
- **What counts as verified.** NASA's verification guidance says that verification is complete with
  "documented objective evidence of compliance with requirements or waiver", together with "closure of all
  discrepancy and nonconformance reports", and that "Verification results should be recorded in a
  requirements compliance or verification matrix" [[22]](#ref-22). A linked test case is therefore a
  claim that a test exists, and not a claim that the requirement was verified. The section should say
  which of these the status column means.
- **A way to mark other means of verification.** The jamb documentation, a practitioner's tool guide,
  keeps a flag for requirements "indicating they are verified by other means (inspection, analysis,
  demonstration)" [[21]](#ref-21). In this library's reading, a requirement verified by inspection would
  otherwise read as a gap.
- **Status vocabulary.** The same documentation separates Passed, Failed, Not Covered and N/A in a status
  column [[21]](#ref-21). It is one tool's design and is cited as an example, not as a standard.
- **Cardinality.** NASA says "the relationships identified in the matrix are not required to be
  one-to-one" [[6]](#ref-6), so one requirement may have several tests and one test may serve several
  requirements.

*Beginner note.* Decide the ID schemes first, then decide what the status words mean in one sentence
each. If the team says covered, define that word first: it can mean a linked test or a verified
requirement.

*Expert note.* **Who may mark a row covered is not established by any source read.** No source says the
person who marks a row must differ from the person who wrote the requirement or the test. The template
should not imply a rule, and a team that wants one should state it as its own. A graded scale of coverage,
such as full, partial and none, is also available to a team that wants it, but no source read supports it
as a norm.

### The Matrix

**What it is:** one row per requirement, with its identifier, a short label for the requirement, its
source, what verifies it, its status, and notes. **Why it exists:** because this table is the artifact.
The other sections explain it, bound it or extend it. The columns draw on Visure's component list:
"Requirements ID and Description", "Source of Requirements" and "Associated Test Cases"
[[4]](#ref-4). The section is supported by [[4]](#ref-4), [[5]](#ref-5), [[6]](#ref-6) and
[[8]](#ref-8).

The row holds a short label and not the requirement's full text. NASA's handbook says "do not duplicate
requirements in the traceability matrix" [[1]](#ref-1). In this library's reasoning, a copy of the text
drifts from the original. The source document owns the text, and the matrix owns the links.

One matrix or several is a stated choice. NASA says "Traceability matrices can be included in the
documents to which they apply", or "they can be combined into a single matrix covering higher level
requirements, software requirements, design, code, and verification" [[6]](#ref-6). Its systems handbook
adds: "This matrix could be divided into multiple matrices (e.g., one for each requirements document)"
[[2]](#ref-2). This template ships one table for the covered set, and a team with several requirement
documents can split it.

*Beginner note.* Fill one row per requirement, including the requirements with nothing in the verified-by
cell. Those empty cells are the reason for the table. A row for a requirement that has no verification is
a finding, not an error.

*Expert note.* The table is read in both directions and is not kept as two tables. NASA describes one
matrix read both ways [[6]](#ref-6), and TestDevLab describes both checks on the same table: that "every
requirement is covered by at least one test case, and conversely, that every test case is linked to a valid
requirement" [[5]](#ref-5). A row-per-requirement table cannot show a test with no requirement, because
such a test has no row, and so Coverage Gaps below is where that half of the check lives. That reading is
this library's inference.

### Coverage Gaps

**What it is:** the requirements with no test, the tests with no requirement, and what each gap's owner
decided. **Why it exists:** both vendor sources name finding gaps as a purpose. TestDevLab lists
"Identify Gaps: Highlight any requirements that do not have a corresponding test case." [[5]](#ref-5)
Visure's product description includes the ability to "detect missing links" [[4]](#ref-4). The backward
half matters too. Orcanos,
a vendor selling a medical-device quality platform, says "An RTM that only maps forward is incomplete."
[[7]](#ref-7) Its frame is an audit of a medical device, and the claim is one vendor's.

A gap that is only flagged has not been dealt with. NASA says the orphans "need to be discussed by the
project team and assurance personnel", and that "If they are determined to be necessary, any missing
source requirements are added to the project." [[6]](#ref-6) So the section asks what each gap's owner
decided. How a gap is displayed is not shown by any source read, and the section's layout is this
library's POSITION.

*Beginner note.* List each gap on its own line, with an owner and a decision: add a test, add a
requirement, mark as verified by other means, or remove the orphan.

*Expert note.* Do not mistake an empty section for a clean bill of health. An empty gap list is only as
good as the rows and the definition of verified behind it. That caution is this library's inference.

### Implementation Trace (full only)

**What it is:** each requirement mapped to its design reference and its code or task reference. **Why it
exists:** because the wider definitions reach past tests. Visure's component list includes "Development
Tasks and Deliverables" [[4]](#ref-4), and describes backward traceability as linking "design elements,
code, and test cases back to the original requirements." [[4]](#ref-4) NASA's guidance allows a single
matrix to cover design, code and verification [[6]](#ref-6). The section is supported by [[4]](#ref-4) and
[[6]](#ref-6). Visure's page is a vendor page that shows no table, so the column set is this library's
assembly.

*Beginner note.* Add one reference per row to where the design lives and one to where the work lives, such
as a ticket or a module. Reference them; do not copy their text.

*Expert note.* Drop this section when a tracker already holds the links. InfoQ reports Appleton gaining
traceability from commits: "When he does a commit he associates the name or id of the story with the
commit." [[13]](#ref-13) A table that restates links the tracker already holds creates a second record that
can disagree with the first, and Section 6 returns to this argument.

### Risk Control Trace (full only)

**What it is:** each risk, the requirement that controls it, and the test that verifies the control.
**Why it exists:** to show whether a control is stated by a requirement and checked by a test, which
is this library's reasoning and not a sourced claim. This is the section with the thinnest general
support, and the guide should say so. Orcanos
names a failure, "The RTM has no column for risk controls.", and says "The RTM is where risk management and
design control intersect." [[7]](#ref-7) That is one vendor in a medical-device frame, and its claims may
not transfer to other software. The FDA's guidance asks for a trace to "risk analysis results"
[[3]](#ref-3). **No general software source read asks for a risk-control trace.** The section is
therefore optional by design, in the full variant only.

*Beginner note.* Use it only when a risk register already exists and a specific risk depends on a specific
requirement and test. Reference the risk by its register identifier, and leave the scoring to the register.

*Expert note.* The matrix owns no risk scoring. The `risk-register` bundle holds likelihood, impact and
owner, and this section only links a risk to the requirement and test that control it. That line is this
library's POSITION.

### Baselines (full only)

**What it is:** dated snapshots of the matrix, recording what a release or an audit saw. **Why it
exists:** because a standing register changes, and a reviewer sometimes needs the state at one moment.
Orcanos says "At each formal design review gate, baseline the RTM." and "Record which version of the RTM
was reviewed and approved." [[7]](#ref-7) Jama, while arguing that the matrix should be live, describes
"a specific versioned artifact that captures those links at a point in time." [[14]](#ref-14)

**This library reads the two together as a standing register that is snapshotted for an audit.** That
reading follows
[ADR 0084 (the requirements traceability matrix joins governance-docs as an eighth member)](../../docs/internal/decisions/0084-requirements-traceability-matrix-joins-governance-docs-as-an-eighth-member.md)
and is a POSITION, not something either vendor states. Wikipedia's description of a matrix as comparing
"baselined documents" [[19]](#ref-19) is consistent with it, though a tertiary source carries little
weight.

*Beginner note.* Record the date, the release or review the snapshot belongs to, and where the snapshot
file is kept.

*Expert note.* The section is full-only because a team without audits or formal releases has little use
for it, and a snapshot of an out-of-date table preserves the out-of-date table. That reasoning is this
library's own.

### Upkeep and Review Trigger

**What it is:** the events that require an update, the owner who makes it, and the date the matrix was
last reconciled. **Why it exists:** because a matrix that nobody maintains turns from a record into a
false assurance. NASA's guidance is "Assign responsibility for creating and maintaining the matrix to a
project team member", "Keep the matrix maintained throughout the life of the project." and "Ensure a
review of the matrix at major phases/key reviews of the project." [[6]](#ref-6) It also warns, of manual
and spreadsheet methods, "It is very important that the project be diligent about keeping such traces up
to date as these methods do not include automatic updates" [[6]](#ref-6).

The update rule comes from Jama: the matrix "should be updated whenever requirements, test cases, or
linked lifecycle artifacts change, not just on a calendar schedule." [[14]](#ref-14) **No source read
gives a calendar interval**, and this template does not invent one. A change to an approved requirement is
a reason to update the matrix. Orcanos says "Every approved design change must include an RTM impact
assessment as part of the change package." [[7]](#ref-7) NASA suggests "Including a test team
representative as part of the CCB or other authorized group responsible for approving changes to
requirements." [[17]](#ref-17)

The staleness mechanism that tools use is documented by jamb: a link is flagged when "the hash it
recorded at link time no longer matches", and a flagged link clears when the items are "reviewed and
updated (or confirmed unchanged)" [[21]](#ref-21). That tool's design aims, in its words, to ensure "that
no change propagates silently through the traceability chain." [[21]](#ref-21) A hand-kept table has no
hash, so this template's stand-in is an owner, a list of trigger events and a date last reconciled.
**No source read puts a last-confirmed field on a hand-kept row**, so that form is this library's
POSITION.

*Beginner note.* Name one owner, list the events that force an update, and write the date the
table was last checked against its sources.

*Expert note.* Treat a date older than the last trigger event as a warning that the table may be stale.
Jama's phrase for the risk is that "the same artifact that once created clarity can instead produce false
confidence." [[14]](#ref-14) It is a vendor's phrase, and it describes a real hazard of any stale table.

---

## 4. Variants and sizing

The bundle ships two sizes, lean and full, and lean is the default.

- **Lean** carries what TestDevLab describes: requirement to test, in both directions [[5]](#ref-5). It
  has five sections: Purpose and Boundary, Trace Conventions, The Matrix, Coverage Gaps, and Upkeep and
  Review Trigger.
- **Full** adds the wider links. Implementation Trace follows Visure's "Development Tasks and
  Deliverables" [[4]](#ref-4). Risk Control Trace follows the failure Orcanos names [[7]](#ref-7).
  Baselines follows Jama's "at a point in time" [[14]](#ref-14).

**Confidence in this split is medium-low.** No source read shows a template with every link type, so the
division between lean and full is this library's hypothesis. The signal to scale up is a question the team
owes an answer to that the lean table cannot give: which design element implements this requirement, which
control covers this risk, or what an auditor saw at a given release. Without such a question, the lean
size is enough. That signal is this library's POSITION.

Neither size makes the matrix mandatory. Section 6 describes the sources that argue a team should keep none.

---

## 5. Methodology lineage

The sources fall into four groups. They differ less in how the table looks than in whether the team owes
one at all. The sources read are not organised by named delivery framework, so this section groups them by
setting instead. The bundle declares its methodology as generic, because the sources that keep a matrix and the sources that decline one span safety-critical,
medical, open-source and agile work.

**Safety-critical and government engineering.** NASA's handbooks treat bidirectional traceability as
required for software and give practical guidance on keeping it [[1]](#ref-1)[[6]](#ref-6). They also
accept lighter forms, such as value-based tracing for small budgets [[6]](#ref-6). NASA's test-planning
guidance treats a matrix as an aid for judging a change: "Using a traceability matrix which identifies the
test plans, procedures, scripts, test cases and even test data associated with each requirement can be
helpful" [[17]](#ref-17).

**Regulated product development.** The FDA's 2002 guidance asks for a traceability analysis
[[3]](#ref-3). Orcanos builds the matrix out for medical devices, with baselining at review gates, a
risk-control column and an impact assessment on every design change [[7]](#ref-7). Jama says the matrix
"is widely used in regulated product development" [[14]](#ref-14), which is Jama's claim and not a
measurement. The Ferrocene developers publish "A matrix that ties the specifics of the Ferrocene Language
Specification to the test suite." [[8]](#ref-8) They wrote it "to ensure that all documented requirements
are covered" [[8]](#ref-8). The matrix supports qualification for safety-critical use, and it is the
strongest named case this research found of a software team publishing its own matrix. Zephyr states a similar aim for
IEC 61508 certification: "tracing the requirements down to the code level is used", while "The tooling is
in evaluation" [[9]](#ref-9). Zephyr's page shows intent and not a running matrix.

**Agile practice, which mostly argues against the document.** InfoQ's 2008 roundup reports Ambler, Cockburn,
Appleton and Bolton, and it records that "A formal traceability matrix often evokes strong response from
the Agile community" [[13]](#ref-13). The roundup also carries the line "Within the agile paradigm
traceability from code/design to requirements is done through unit and acceptance tests."
[[13]](#ref-13) Ambler's own essay makes the case with an alternative for simple situations: "it is much
easier and cheaper to simply ask them to estimate the change" [[10]](#ref-10). Rothman reports lighter
forms in use among her clients, and offers her own rule of thumb: "The fewer artifacts, the better."
[[11]](#ref-11)

**Tooling vendors, who argue for a live view.** Jama says "Trace links can drift out of sync within
weeks." [[14]](#ref-14) Ketryx says "An RTM is not a static document but rather a living artifact that
evolves with the software development process." [[15]](#ref-15) Each is a vendor's argument for a product
that keeps the links automatically. Orcanos also sells a platform [[7]](#ref-7), so its account of
failures belongs in the same category.

---

## 6. Debates and contested boundaries

The dispute has three positions, not two: a hand-kept matrix, a tool-kept matrix, and no matrix at all.
**The sources do not compare the three on evidence.** The positions below are stated with their camps, and
the recommendation at the end of the section is this library's.

**1. Does the matrix repay its upkeep outside regulated work?**

- *No, from 2008 agile practitioners, through InfoQ.* Ambler: "My experience is that traceability matrices
  are highly overrated because the total cost of ownership (TCO) to maintain such matrices, even if you
  have specific tools to do so, far outweigh the benefits." Cockburn: "I have, in 30 years in the
  business, in industry, research and a little bit in government, NEVER seen a traceability matrix pay
  off." [[13]](#ref-13) InfoQ also quotes Cockburn on one corporate IT project: "The cost was so
  staggeringly high that the client removed the traceability requirement from the contract."
  [[13]](#ref-13) These are second-hand reports of mailing-list posts, and the roundup gives no figures.
  Ambler's own essay limits the claim: "In simple situations, which many agile teams find themselves in, my
  experience is that traceability matrices are highly overrated" [[10]](#ref-10).
- *Only where the loss would be real, from Bolton through InfoQ.* The matrix "would only be required when
  there is a danger of losing corporate memory that is genuinely valuable" [[13]](#ref-13).
- *Yes, where traceability is owed.* Ambler concedes "I'm a firm believer in traceability if you have actual
  regulatory compliance needs" [[13]](#ref-13), and his essay gives four conditions: tooling, complex
  domains, large or distributed teams and regulatory compliance. It opens "The quick answer is in some
  complex situations and when you have proper tooling support" [[10]](#ref-10).
- *The newest independent evidence points two ways.* Fucci and colleagues describe a large, anonymized
  telecommunications company where "traceability between high-level requirements, source code, and test
  suites is not maintained at COMPANY" [[12]](#ref-12). They conclude that "the situation we observed at
  COMPANY indicates that such requirements may have been overstated", and yet "we encourage practitioners
  to be selective about the traceability links necessary for their organization" [[12]](#ref-12). The
  company is unnamed, so it is not a named team's account.
- *The mapping study.* Tian and colleagues find "establishing and maintaining traceability links is the
  main cost of deploying traceability practices" and "easing the process of change management is the main
  benefit of deploying traceability practices". They also say "most of the studies have provided the
  evidence using toy examples or academic studies" [[16]](#ref-16). The study covers traceability in
  maintenance and evolution, and not the matrix as a document. **No source read measures upkeep cost
  against defect outcomes.** That is an absence in what was read, at medium confidence.

**2. Is the answer a better tool, or no matrix?** The vendors say a tool. Ketryx goes furthest, saying
"Excel can no longer manage RTMs for modern software." [[15]](#ref-15) The 2008 practitioners say to derive
traceability from tests and commits [[13]](#ref-13). The hand-kept form is left standing by some of the
same sources. Jama writes "No major regulatory framework explicitly prohibits spreadsheets."
[[14]](#ref-14) NASA accepts a manual matrix and warns about its upkeep [[6]](#ref-6). Rothman reports
clients using index cards and spreadsheets [[11]](#ref-11).

**3. A document or a live view?** Jama argues against the static form while also describing "a specific
versioned artifact that captures those links at a point in time." [[14]](#ref-14) This library reads that
as the standing register snapshotted for an audit, as ADR 0084 records. That reading is a POSITION, and it
is why the Purpose and Boundary section asks which place is the record.

**4. How far must a matrix reach?** To tests only [[5]](#ref-5), or along a wider chain of design, code,
tasks and risk controls [[4]](#ref-4)[[6]](#ref-6)[[7]](#ref-7). Orcanos' reach comes from medical-device
duties. The two sizes of this bundle take both sides of this question.

**5. What counts as verified?** The sources do not define it the same way. NASA ties completion to
evidence and closed nonconformance reports [[22]](#ref-22), and jamb separates passed, failed, not
covered and N/A in a status column and flags requirements verified by other means [[21]](#ref-21). In this library's reading, a matrix that treats the existence of a
test case as verification is making a claim that these sources do not make.

**What this library recommends.** Keep a matrix only where the team has decided it owes a whole-set answer
to the question of which requirement has no verification, and say so in the document. NASA's value-based tracing
focuses the effort on the most important requirements [[6]](#ref-6), and Fucci and colleagues advise being
selective about which links to keep [[12]](#ref-12). Where a tracker already holds the links, name the tracker as the record and do not keep
a copy. This recommendation is a POSITION. It is not an evidence-based finding, because none of the
sources compared the options.

---

## 7. Anti-patterns and failure modes

1. **Copying requirement text into the matrix.** NASA says "do not duplicate requirements in the
   traceability matrix" [[1]](#ref-1). In this library's reasoning, a copy that drifts from the source
   document creates two requirements.
2. **Treating a linked test as a verified requirement.** A test case ID in the verified-by cell shows a
   test exists. NASA ties verification to documented evidence and closed nonconformance reports
   [[22]](#ref-22). This is the subtle failure, and a table full of green rows can hide it.
3. **A forward-only matrix.** Orcanos says "An RTM that only maps forward is incomplete." [[7]](#ref-7)
   A table that never checks the tests against the requirements cannot show a test with no requirement.
   Whether this failure is frequent is not measured by any source read.
4. **Flagging a gap and leaving it.** NASA's guidance is that orphans are discussed and, where necessary,
   the missing requirement is added [[6]](#ref-6). A gap with no owner and no decision is a list of
   worries.
5. **Letting the table go stale.** NASA's warning is that manual methods "do not include automatic
   updates" [[6]](#ref-6). Jama's, in a vendor's words, is that "Trace links can drift out of sync within
   weeks." [[14]](#ref-14) The sources do not say how fast a hand-kept table goes stale, and no calendar
   interval is established.
6. **A matrix kept for its own sake.** Jama describes "A pervasive practitioner belief that traceability
   costs more than it delivers leads to deferred maintenance" [[14]](#ref-14). That is a vendor's
   description of how a neglected table fails.
7. **Confusing the verification matrix with this one.** NASA's Appendix D matrix is scoped to "shall"
   statements and records how each is verified [[2]](#ref-2). It is a related artifact and not a
   template for this one.
8. **A matrix with no reason to exist.** A team that cannot say what it chose to trace, what it chose not
   to trace and when it will stop is keeping the table because tables are kept. Ambler calls the matrix "a
   business decision" [[10]](#ref-10), and Section 3's Purpose and Boundary asks for that decision.
9. **A requirement without an identifier.** A statement that has no ID has no row, and so nothing can trace
   to it. NASA's guidance supports unique identification [[6]](#ref-6). That the loss goes unseen is this
   library's inference.

---

## 8. Relationships to other artifacts

The matrix draws on documents that state requirements and on documents that verify them. It owns neither.
Each line below is this library's POSITION unless a citation follows it.

**Upstream, the documents that state requirements.** `prd`, `use-case-specification`, `user-stories` and
`acceptance-criteria` each state what the product must do. The matrix states where each requirement went.
The line against `acceptance-criteria` rests on this library's own examples, and **no external source read
speaks to that boundary**.

**The `test-case` bundle.** A test case's own traceability field points one case at one thing. NASA's
guidance says test procedures should "include bidirectional traceability to the requirements or a
reference to the document containing that trace." [[18]](#ref-18) Wikipedia advises: "it is advisable to
add the relationships to the source documents for both backward and forward traceability" [[19]](#ref-19).
So both a per-document field and a whole-set view exist, and one may point at the other. **A per-test field
cannot show a requirement that has no test, because there is no test to hold the field.** That sentence is
this library's inference and not a quoted claim. The per-test field remains the matrix's input.

**The `test-plan` and `test-summary-report` bundles.** A test plan plans verification for one release, and
the matrix outlives the release. NASA's guidance says the project shall update test plans and
procedures "to be consistent with software requirements" [[17]](#ref-17). IEEE 829's set, as Wikipedia
summarises it, has a report written "after test execution has finished for the specific test level"
[[20]](#ref-20) and lists no traceability matrix. A report is a dated result of one cycle, and a matrix row
stays open. No source states this boundary directly.

**The `change-request` and `change-log` bundles.** A change to a requirement is a reason to update the
matrix [[7]](#ref-7)[[17]](#ref-17). No source says whether the change log or the matrix is the record of
what changed, so the line between them is this library's POSITION: the change log records the decision, and
the matrix records the current links.

**The `risk-register` bundle.** The register tracks risks. The full variant's Risk Control Trace links a
risk to the requirement and test that control it [[7]](#ref-7)[[3]](#ref-3), and owns no scoring.

**The other governance-docs members.** The family contract's position is that these instruments most often
fail by collapsing into each other. The `raid-log` consolidates risks, assumptions, issues and dependencies,
and the `issue-log` records problems that have already happened. The `kpi-dashboard` defines performance
targets. The `data-dictionary` and the `tracking-plan` are standing registers with a different subject,
fields and events, not requirements. The matrix is a standing register of requirements and their
verification, and it stands to the `test-case` traceability field as the `change-log` stands to the
`change-request`, per
[the family contract](../../docs/internal/contracts/governance-docs.md). A matrix that begins carrying risk scores, issue
status or metric definitions has started to collapse into a neighbour.

---

## 9. Adaptations

**Regulated and safety-critical work.** This is where the sources say traceability is owed: Ambler concedes
it where regulatory compliance needs exist [[13]](#ref-13), and NASA and the FDA ask for it
[[1]](#ref-1)[[3]](#ref-3). The FDA's guidance never uses the word matrix, and NASA calls matrices "not the
only method" [[6]](#ref-6). Orcanos'
medical-device account adds baselining, an impact assessment on each design change and a risk-control
column [[7]](#ref-7), and Ferrocene publishes its matrix for qualification [[8]](#ref-8). The full variant
fits these cases best, in this library's view. This research did not read the standards that govern these cases,
and nothing here says what any of them requires.

**An unregulated team with one risky area.** NASA's value-based tracing is the honest frame:
prioritise the requirements and trace the most important ones [[6]](#ref-6). Keep the matrix to one
feature or one release, say what it does not cover, and state when it will be dropped. Fucci and colleagues
separately advise being selective about which links to keep [[12]](#ref-12).

**Solo or very small teams.** Rothman reports lightweight forms among clients, such as index cards "with
notes about where the tests are." [[11]](#ref-11) The source does not give their team sizes, so the match to
small teams is this library's. Ambler's alternative for a simple situation is to ask the people familiar with
the system to estimate the change [[10]](#ref-10). This library's view is that the lean variant is the largest a team this size should consider, and that no matrix may be the right
answer.

**Large or distributed teams.** Ambler lists large or distributed teams among the conditions that justify
traceability [[10]](#ref-10). In this library's view, a team in that position needs the single-record
rule in Purpose and Boundary, so that one place is the authority.

**Tool-held links.** NASA says a matrix may be "a by-product of a requirements management tool"
[[6]](#ref-6), and the vendors argue for that route [[14]](#ref-14)[[15]](#ref-15). In that case the
file becomes a snapshot and a statement of conventions, and the Baselines section carries its value. Each
tool-vendor claim in this research is a vendor's argument and should be read as one.

**Agile teams.** Appleton's commit linking and the unit and acceptance tests that the roundup describes
[[13]](#ref-13) are the alternatives to a separate table. A team that already links work to requirement IDs in
its commits can use the matrix as a periodic check on the whole set, rather than as the primary record.
That use is this library's POSITION.

---

## 10. Worked example

`requirements-traceability-matrix_example.md` is a full-size matrix for a single fictional product
feature, Saved Views for Dashboards, on the Reporting Platform Modernization program at the fictional Acme
Analytics. It demonstrates the case the type exists for: a whole-set view that shows a requirement no
single document connects to its verification. Acme is not regulated, and the example's Purpose and
Boundary section says why its team kept the matrix anyway and when it will stop.

---

## References

<a id="ref-1"></a>[1] NASA. "[Software Engineering Handbook (Ver B), SWE-052, Bidirectional Traceability Between Higher Level Requirements and Software Requirements](https://swehb.nasa.gov/display/SWEHBVB/SWE-052+-+Bidirectional+Traceability+Between+Higher+Level+Requirements+and+Software+Requirements)."
swehb.nasa.gov (accessed 2026-11-06). The requirement to perform, record and maintain bidirectional
traceability, the warning against duplicating requirement text in the matrix, and ISO/IEC/IEEE 24765:2010's
definition as NASA quotes it. [primary]

<a id="ref-2"></a>[2] NASA. "[Systems Engineering Handbook (NASA/SP-2016-6105 Rev2), web edition, Appendix page](https://www.nasa.gov/reference/system-engineering-handbook-appendix/)."
nasa.gov (accessed 2026-11-06). The glossary definition of traceability, and a verification matrix scoped
to "shall" statements with a separate validation matrix; a related artifact and not this type. [primary]

<a id="ref-3"></a>[3] US Food and Drug Administration. "[General Principles of Software Validation; Final Guidance for Industry and FDA Staff](https://www.fda.gov/media/73141/download)."
fda.gov, 11 January 2002 (accessed 2026-11-06). The call for a software requirements traceability
analysis to system requirements and to risk analysis results; the guidance never uses the word matrix. [primary]

<a id="ref-4"></a>[4] Visure Solutions. "[What is Requirements Traceability Matrix (RTM)?](https://visuresolutions.com/blog/software/traceability-matrix)."
visuresolutions.com (accessed 2026-11-06). One vendor's list of matrix components, three trace directions
defined in prose, and an audit habit; the page shows no table. [vendor]

<a id="ref-5"></a>[5] TestDevLab. "[Traceability Matrix, Center of Excellence glossary](https://www.testdevlab.com/center-of-excellence/glossary/engineering-terms/traceability-matrix)."
testdevlab.com (accessed 2026-11-06). The narrowest definition, requirement to test case in both
directions, with gap identification and change maintenance as purposes. [vendor]

<a id="ref-6"></a>[6] NASA. "[Software Engineering Handbook, SWE-059, Bidirectional Traceability Between Software Requirements and Software Design](https://swehb.nasa.gov/spaces/7150/pages/16449675/SWE-059+-+Bidirectional+Traceability+Between+Software+Requirements+and+Software+Design)."
swehb.nasa.gov (accessed 2026-11-06). Practical guidance: when to create the matrix, an assigned owner,
review at major phases, one combined matrix or matrices inside each document, links that need not be
one-to-one, orphans discussed, the staleness risk of manual methods, and value-based tracing. [primary]

<a id="ref-7"></a>[7] Zohar Peretz (Orcanos). "[Requirements Traceability Matrix for Medical Devices: A Complete Compliance Guide](https://www.orcanos.com/blog/requirements-traceability-matrix-for-medical-devices-a-complete-compliance-guide)."
orcanos.com, 4 June 2026 (accessed 2026-11-06). A vendor's medical-device account: forward-only called
incomplete, a missing risk-control column named as a failure, baselining at review gates, and an impact
assessment with each design change. [vendor]

<a id="ref-8"></a>[8] The Ferrocene Developers. "[Ferrocene documentation index, with its Traceability matrix report](https://public-docs.ferrocene.dev/main)."
public-docs.ferrocene.dev (accessed 2026-11-06). The one named software team's own published matrix
found: the language specification mapped to the test suite, for safety-critical qualification. [primary]

<a id="ref-9"></a>[9] Zephyr Project. "[Zephyr Safety Overview](https://docs.zephyrproject.org/latest/safety/safety_overview.html)."
docs.zephyrproject.org (accessed 2026-11-06). A named open source project's stated aim to trace
requirements to code for IEC 61508 certification, with tooling still in evaluation. [primary]

<a id="ref-10"></a>[10] Scott W. Ambler (Ambysoft). "[Agile Requirements Best Practices, practice 11, Question Traceability](https://agilemodeling.com/essays/agileRequirementsBestPractices.htm)."
agilemodeling.com (accessed 2026-11-06). A named practitioner's position that manually kept matrices
rarely repay their cost, his simple-situation alternative, and four conditions that justify traceability.
His basis is experience, not measurement. [practitioner]

<a id="ref-11"></a>[11] Johanna Rothman. "[Traceability Matrix and Agile](https://nofluffjuststuff.com/blog/johanna_rothman/2008/07/traceability_matrix_and_agile)."
No Fluff Just Stuff blog, 11 July 2008 (accessed 2026-11-06). A consultant's report that some clients keep
traceability on index cards and others in a spreadsheet under source control. [practitioner]

<a id="ref-12"></a>[12] Davide Fucci, Emil Alegroth and Thomas Axelsson. "[When Traceability Goes Awry: an Industrial Experience Report](https://arxiv.org/pdf/2206.04462)."
arXiv 2206.04462, 2022 (accessed 2026-11-06). An experience report on a large, anonymized
telecommunications company that lacks requirement-to-test and requirement-to-code traces, and the
authors' advice to be selective. [academic]

<a id="ref-13"></a>[13] Vikas Hazrati. "[Traceability Matrix in an Agile Project](https://www.infoq.com/news/2008/06/agile-traceability-matrix)."
InfoQ news, 6 June 2008 (accessed 2026-11-06). The 2008 agile case against the matrix, as a secondary
report of mailing-list posts by Ambler, Cockburn, Appleton and Bolton. No figures appear in it. [practitioner]

<a id="ref-14"></a>[14] Mario Maldari (Jama Software). "[Traceability Matrix 101: Why It's Not the Ultimate Solution for Managing Requirements](https://www.jamasoftware.com/?p=11155)."
jamasoftware.com, republished 29 May 2026 (accessed 2026-11-06). A vendor's argument for a live view over
a static matrix: the update rule, drift, false confidence and the versioned snapshot. Jama sells the live
replacement. [vendor]

<a id="ref-15"></a>[15] Jake Stowe (Ketryx). "[Best Practices for Maintaining a Requirement Traceability Matrix in Agile](https://www.ketryx.com/blog/best-practices-for-maintaining-a-requirement-traceability-matrix-in-agile)."
ketryx.com, 12 September 2023 (accessed 2026-11-06). A vendor's argument that the matrix is a living
artifact and that manual upkeep in Excel should be avoided. Ketryx sells automated traceability. [vendor]

<a id="ref-16"></a>[16] Fangchao Tian, Tianlu Wang, Peng Liang, Chong Wang, Arif Ali Khan and Muhammad Ali Babar. "[The Impact of Traceability on Software Maintenance and Evolution: A Mapping Study](https://arxiv.org/pdf/2108.02133)."
arXiv 2108.02133, 2021 (accessed 2026-11-06). A mapping study of 63 papers: link upkeep is the main cost,
easier change management the main benefit, and strong industrial evidence is still needed. [academic]

<a id="ref-17"></a>[17] NASA. "[Software Engineering Handbook, SWE-071, Update Test Plans and Procedures](https://swehb.nasa.gov/x/5gP7)."
swehb.nasa.gov (accessed 2026-11-06). A traceability matrix as a change-impact aid for test plans and
procedures, and a test representative on the change control board. [primary]

<a id="ref-18"></a>[18] NASA. "[Software Engineering Handbook, SWE-114, Software Test Procedures](https://swehb.nasa.gov/x/mAD7)."
swehb.nasa.gov (accessed 2026-11-06). Test procedures carrying their own traceability or pointing at the
document that holds it. [primary]

<a id="ref-19"></a>[19] Wikipedia. "[Traceability matrix](https://en.wikipedia.org/wiki/Traceability_matrix)."
en.wikipedia.org (accessed 2026-11-06). A tertiary description of a matrix as a many-to-many comparison
of two baselined documents; no authority beyond the shape of the relationship. [reference]

<a id="ref-20"></a>[20] Wikipedia. "[IEEE 829](https://en.wikipedia.org/wiki/IEEE_829)."
en.wikipedia.org (accessed 2026-11-06). A tertiary summary of the IEEE 829 document set; the standard
itself was not read. [reference]

<a id="ref-21"></a>[21] Andrew Van. "[jamb documentation, Traceability Requirements (IEC 62304 Guide)](https://jamb.readthedocs.io/en/latest/iec-62304/traceability.html)."
jamb.readthedocs.io (accessed 2026-11-06). One tool's published matrix design: suspect links by content
hash, a status column, and a flag for requirements verified by other means. [practitioner]

<a id="ref-22"></a>[22] NASA. "[Systems Engineering Handbook, web edition, section 5.3, Product Verification](https://www.nasa.gov/reference/5-3-product-verification/)."
nasa.gov (accessed 2026-11-06). When verification is complete: objective evidence or a waiver, plus closure
of nonconformance reports, with results recorded in a compliance or verification matrix. [primary]
