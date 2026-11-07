# requirements-traceability-matrix: research log

Research conducted 2026-11-06. It builds on admission sweep 7 of 2026-10-29 and the placement read of 2026-11-05,
both held in gitignored folders under `_local/research/`. It also builds on
[ADR 0084](../../docs/internal/decisions/0084-requirements-traceability-matrix-joins-governance-docs-as-an-eighth-member.md)
(the requirements traceability matrix joins governance-docs as an eighth member), on the family contract
(`docs/internal/contracts/governance-docs.md`, 0.6.0) and on the approved spec, the section of
`docs/internal/tier2-specs.md` headed "governance-docs (eighth member, by amendment): the requirements traceability
matrix". The maintainer ruled that spec's four choices as recommended on 2026-11-05. They fix the classification
`utility`, the sizes lean and full, methodology `generic`, and the Saved Views example with a stop rule. This bundle
is issue #261 (bundle: requirements-traceability-matrix), and it fills catalog entry 37.

The build ran six dimensions: origins, structure, practice, debates, relationships and the gap question. The working
files are numbered by return order: `dim1.md` holds structure, `dim2.md` origins, `dim3.md` debates, `dim4.md` the gap
question, `dim5.md` practice and `dim6.md` relationships.

**22 sources are recorded below, and all 22 are fetched-and-verified.** By tier they are 9 primary, 5 vendor, 4
practitioner, 2 academic and 2 reference. Six of the primary entries are NASA pages. **Quotable lines render long
dashes as hyphens, so copy them as they stand.**

## What the checks caught, and what was not read

**Every quotation was checked against raw text**, never against a retrieval tool's summary. Of the 102 quotations the
agents returned, 99 passed on the first check. Two of the three failures were extraction artifacts or small edits at
a list boundary, and the main loop replaced them with exact wording from the raw page. The third, a sentence from
Ambler [10], has a formatting break that the check could not span, so it was dropped.

**The main loop added the quotations the spec and ADR 0084 rest on,** because the agents did not return all of them.
Each was tested against the same raw text. It also read NASA's SWE-059 [6] further, because the structure dimension
returned thin evidence. That page answers a question the vendor pages left open, whether one matrix or several is
the norm.

**Three sources an agent read were withdrawn, and no claim here rests on them.**

- **Texas Department of Information Resources, Software Requirements Specification Instructions.** The origins
  dimension read it, and it is the one government page found that specifies a matrix under the full name. A later raw
  fetch and the site's policies page both returned 403. The site's terms therefore could not be checked, and the agent
  had retrieved the file with a browser-style client string. The runbook bars an alternate client used to get past a
  block, so this log does not lean on it. It is listed for a hand read in the section after the sources.
- **Francisco Pinheiro's chapter on requirements traceability,** a PDF on a university faculty page. A raw re-fetch
  failed, and this research did not establish that the author or the publisher put out that copy. Its second-hand
  quotation of IEEE 830-1984 goes with it.
- **A task file in one npm package,** served through jsDelivr. That service's terms page did not render readable text,
  and the file is one package's convention. It was the only source for a graded full, partial and none coverage scale,
  so that candidate loses its source and is routed below.

**Terms were checked after the research ran, which was the wrong order.** The agents checked the runbook's table but
not every new site's own terms before reading. The main loop then read the terms page of each host first read in this
run, and none bars a read of this kind. NASA's and the FDA's policy pages carry no such clause. The Wikimedia terms bar
only automated uses that are abusive, disruptive or unapproved. The Linux Foundation's terms, the Read the Docs terms and
Ferrous Systems' imprint carry no clause on reading. arXiv's robots file bars "indiscriminate" automated downloads, and
this research read two single papers. **No terms page was found for `agilemodeling.com` or `nofluffjuststuff.com`** at
the usual paths, and neither article page shows a bar. That is absence and not clearance, at medium confidence.
Visure, TestDevLab and Jama were checked for the admission sweep, and InfoQ on 2026-11-05. The research agents read the
terms of Orcanos and Ketryx on 2026-11-06 and found no clause on automated access. Asana stayed unread.

**Not read.** ISO/IEC/IEEE 29148, 29119-3 and 24765, IEEE 829 and 830, 21 CFR 820.30 and the QMSR, DO-178C and the
INCOSE handbook. A standard may be cited for its existence and never for its content, as
[ADR 0050](../../docs/internal/decisions/0050-qa-docs-admits-a-fourth-member.md) requires. Also unread: Ruiz and
colleagues' 2023 paper in *Requirements Engineering*, because the publisher's page returned a client challenge, and
Brad Appleton's own posts, so Appleton appears only as InfoQ relays that work. PMI's template sits behind a
membership wall.

## Findings

### What the type is

**The narrow definition is a table linking requirements to tests.** TestDevLab: "A Traceability Matrix is a document
that links and maps project requirements to their corresponding test cases." [5] The wider definition reaches design and
tasks. Visure lists "Development Tasks and Deliverables" among its components [4], and Orcanos says "A minimal RTM maps
requirements to tests." and then adds more for a medical device [7]. Jama calls it "a structured information artifact"
[14].

**Traceability and the matrix are different things, and the sources say so.** NASA defines traceability as "A discernible
association among two or more logical entities such as requirements, system elements, verifications, or tasks." [2]
InfoQ reports Appleton: "Traceability matrix on the other hand is one of the possible implementations of traceability."
[13] NASA's own guidance calls matrices the usual method, not the only one: "While traceability matrices are not the
only method for capturing bidirectional traceability, they are the most common." [6] That sentence is NASA's
statement and not a measurement.

### Origins: the first use could not be established

**No source read shows where the phrase began, and a confident origin story would be invented.** The practice is
documented in NASA's software handbook, which requires that a project manager "shall perform, record, and maintain
bidirectional traceability between the software requirement and the higher-level requirement." [1] The FDA's 2002
guidance calls for an analysis "to trace software requirements to" system requirements and risk analysis results, and
it never uses the word matrix [3]. An account that places the origin in 1980s defence standards surfaced only in low-authority
pages, and those standards were not read, so it stays an unverified lead.

**NASA's verification matrix is related and not the same artifact.** Its Appendix D is scoped this way: "Only “shall”
requirements should be included in these matrices." [2] It records how each statement is verified and keeps validation
in a separate matrix. A bundle should not treat that verification matrix as the requirements traceability matrix.

### Structure: no template shows every link, and NASA settles the count

**Neither vendor page shows a table.** The structure dimension found no column-header row in the pages it owned. The
recurring pair is requirement and test. Visure adds "Requirements ID and Description", "Source of Requirements" and
"Development Tasks and Deliverables" [4]. **The spec's question of whether any one template carries design, code, test
and risk-control links has no direct answer in what was read.** NASA comes closest in prose, saying matrices "can be
combined into a single matrix covering higher level requirements, software requirements, design, code, and
verification" [6].

**One matrix or several is a stated choice.** NASA offers both: "Traceability matrices can be included in the documents
to which they apply" or combined into one [6]. Its systems handbook adds "This matrix could be divided into multiple
matrices (e.g., one for each requirements document)" [2].

**Forward and backward are read from one table, not kept as two.** NASA describes one matrix read in both directions
[6], and TestDevLab describes both checks on the same table: "every requirement is covered by at least one test case, and
conversely, that every test case is linked to a valid requirement" [5]. Orcanos says "An RTM that only maps forward is
incomplete." [7] Its frame is an audit of a medical device. How a gap is displayed is not shown by any source, so the
Coverage Gaps section's layout is the library's POSITION.

**The links need not be one-to-one.** NASA: "the relationships identified in the matrix are not required to be one-to-one"
[6]. It also warns "do not duplicate requirements in the traceability matrix" [1], which supports the spec's short-label
rule.

**The spec's sections, tested.**

| Section | Result |
|---|---|
| Purpose and Boundary | Purpose is supported. A boundary statement is the library's POSITION, drawn from Jama's live-view argument [14] |
| Trace Conventions | Supported: unique identification [6], scope [2], and what counts as verified [22] |
| The Matrix | Supported by [4], [5], [6] and [8] |
| Coverage Gaps | The purpose is supported by [4] and [5], and the disposition step by [6]. The layout is POSITION |
| Implementation Trace | Supported by [4] and [6] |
| Risk Control Trace | One vendor in a medical-device frame [7], and the FDA's trace to risk analysis results [3]. No general software source asks for it |
| Baselines | Supported by [7] and [14] |
| Upkeep and Review Trigger | Supported by [6] and [14]. The trigger's form is POSITION |

### Practice: a null result on the question that matters most

**No named software team outside regulated or safety-critical work was found describing its own matrix.** The practice
dimension searched for one because ADR 0084's admission check for a software audience was a weak pass, and it remains
weak. High confidence that this search found none, medium that none exists.

**The strongest named case is regulated.** The Ferrocene developers publish "A matrix that ties the specifics of the
Ferrocene Language Specification to the test suite." [8] Its report page, read raw on 2026-11-06, listed 331 linked and
21 informational sections out of 352, as the entry below records. That report is a live page, too large to cache, so those counts are dated. The
page exists to support compiler qualification for safety-critical use. Zephyr states an aim, and says "The tooling is in
evaluation" [9], so it shows intent and not a running matrix.

**Lightweight keeping is reported, second-hand.** Johanna Rothman reports "Some of my clients keep their index cards and
organize the traceability that way, with notes about where the tests are." and "Other folks use a spreadsheet for the
organizing." [11] InfoQ reports that Appleton gets traceability from commits: "When he does a commit he associates the name
or id of the story with the commit." [13]

**The one documented decision-by-default is anonymized.** Fucci and colleagues report on a large telecommunications
company: "traceability between high-level requirements, source code, and test suites is not maintained at COMPANY" [12].
They conclude "the situation we observed at COMPANY indicates that such requirements may have been overstated" and yet
"we encourage practitioners to be selective about the traceability links necessary for their organization" [12].

**The justifications for an unregulated team, as the sources state them.** Ambler gives four conditions, opening "The
quick answer is in some complex situations and when you have proper tooling support" [10]. They are automated tooling,
complex domains, large or distributed teams, and regulatory compliance. In simple situations he says "it is much easier
and cheaper to simply ask them to estimate the change" [10]. InfoQ reports Michael Bolton: "traceability matrix would
only be required when there is a danger of losing corporate memory that is genuinely valuable" [13]. NASA offers a
narrower route for small projects: "Value-based requirement tracing may be an option for projects with small budgets"
and "This can save a significant amount of effort by focusing traceability activities on the most important
requirements." [6] **No named source was found on a contractual obligation, a safety-critical subset in an otherwise
unregulated product, or a migration that kept a matrix.**

### Debates: three positions, and no measurement behind any of them

**The dispute has three positions, not two.** A hand-kept matrix, a tool-kept matrix, and no matrix at all. The sources
do not compare them on evidence.

- **No matrix (2008 agile practitioners, through InfoQ).** Ambler: "My experience is that traceability matrices are highly
  overrated because the total cost of ownership (TCO) to maintain such matrices, even if you have specific tools to do
  so, far outweigh the benefits." Cockburn: "I have, in 30 years in the business, in industry, research and a little bit
  in government, NEVER seen a traceability matrix pay off." [13] InfoQ also quotes Cockburn on one corporate IT project: "The cost was so
  staggeringly high that the client removed the traceability requirement from the contract." [13] All of it is testimony,
  and the roundup gives no figures.
- **Tool-kept (vendors who sell the tool).** Jama: "Trace links can drift out of sync within weeks." Ketryx: "An RTM is not a
  static document but rather a living artifact that evolves with the software development process." and "Excel can no
  longer manage RTMs for modern software." [14], [15] Each is a vendor's argument.
- **Hand-kept, where it is owed.** Ambler concedes "I'm a firm believer in traceability if you have actual regulatory
  compliance needs" [13]. Jama concedes "No major regulatory framework explicitly prohibits spreadsheets." [14] NASA
  accepts a spreadsheet for small projects and warns "It is very important that the project be diligent about keeping
  such traces up to date as these methods do not include automatic updates" [6].

**The nearest thing to evidence is a mapping study, and it says the evidence is weak.** Tian and colleagues synthesize 63
papers: "establishing and maintaining traceability links is the main cost of deploying traceability practices" and
"easing the process of change management is the main benefit of deploying traceability practices" [16]. They also say
"strong empirical evidence from industry is needed to validate the impact of traceability on maintenance and evolution"
and "most of the studies have provided the evidence using toy examples or academic studies" [16]. It studies traceability
in maintenance and evolution, not the matrix as a document. **No source read measures upkeep cost against defect
outcomes.** Treat that as an absence in what was read, at medium confidence.

**The newer voices are Fucci (2022), Tian (2021), Stowe (2023) and Maldari (republished 2026).** The first two answer the
spec's request for something newer than the 2008 roundup. The last two sell the replacement.

### Relationships

**The per-test field and the whole-set view both exist, and one may point at the other.** NASA says test procedures should
"include bidirectional traceability to the requirements or a reference to the document containing that trace." [18]
Wikipedia, a tertiary source, says "it is advisable to add the relationships to the source documents for both backward
and forward traceability" [19]. **That a per-test field cannot show a requirement with no test is this log's inference**,
not a quoted claim. No test exists to hold the field.

**A change is a reason to update the matrix.** Orcanos: "Every approved design change must include an RTM impact
assessment as part of the change package." [7] NASA suggests "Including a test team representative as part of the CCB or
other authorized group responsible for approving changes to requirements." and calls a matrix helpful for judging a
change's reach [17]. No source says whether the change log or the matrix is the record of what changed, so that boundary
is the library's POSITION.

**The test report is a dated result.** IEEE 829's set, as Wikipedia summarises it, has a report written "after test
execution has finished for the specific test level" and lists no traceability matrix [20]. No source states the boundary
directly, so it too is POSITION.

**Risk.** Orcanos names a failure, "The RTM has no column for risk controls." and says "The RTM is where risk management and
design control intersect." [7] Its frame may not transfer. The FDA's guidance traces to "risk analysis results" [3]. **No
external source read speaks to the boundary with acceptance criteria**, so that line rests on this library's own
examples.

### The gap question, routed under decision procedure 12

The gap dimension did not read this bundle's spec or rubric first. It returned candidates, and each is routed here. None
adds a section, because the spec's Trace Conventions and Upkeep sections already hold them.

| Candidate | Source | Route |
|---|---|---|
| A stated rule for what counts as verified, separate from a test existing | NASA: "documented objective evidence of compliance with requirements or waiver" and "closure of all discrepancy and nonconformance reports" [22]; jamb's status column [21] | A field in Trace Conventions, and a guide rubric row. Confidence medium-high |
| A way to mark a requirement verified by other means, so it does not read as a gap | jamb: "indicating they are verified by other means (inspection, analysis, demonstration)" [21] | A status value in Trace Conventions. Confidence medium |
| A way to show the matrix has gone stale | jamb's suspect links, "This mechanism ensures that no change propagates silently through the traceability chain." [21]; NASA's owner and review points [6] | The hand-kept form is an owner, a trigger list and a date last reconciled, in Upkeep. **No source read puts a last-confirmed field on a hand-kept row**, so that form is the library's POSITION. Also a rubric row |
| Scope and granularity rules | NASA on "shall" statements [2] and on one-to-many links [6] | A field in Trace Conventions. Confidence medium |
| Disposing of an orphan, not merely flagging it | NASA: "they need to be discussed by the project team and assurance personnel" and "If they are determined to be necessary, any missing source requirements are added to the project." [6] | Coverage Gaps, which already asks what each gap's owner decided. A rubric row |
| A graded coverage scale | Its one source was withdrawn | Not adopted. A team may add one in Trace Conventions, but no source read supports it as a norm. Low confidence |

**Not found:** any source saying who may mark a row covered, or requiring the verifier to differ from the author. The
template should not imply a rule on this.

## Claims flagged contested or time-bound

- **Whether the matrix repays its cost outside regulated work.** Contested, and not measured [12], [13], [14], [16].
- **Whether the answer is a better tool or no matrix.** The vendors say a tool, and the 2008 practitioners say derive
  traceability from tests and commits [13], [14], [15].
- **How far a matrix must reach.** Requirement to test [5], or a wider chain [4], [6], [7]. Orcanos' reach comes from
  medical-device duties.
- **A document or a live view.** Jama argues against the static form while also describing "a specific versioned artifact
  that captures those links at a point in time." [14] This library reads that as the standing register snapshotted for
  an audit, as ADR 0084 records. That reading is a POSITION.
- **Time-bound.** The InfoQ roundup is from 2008 and is a secondary report of mailing-list posts. Ferrocene's counts and
  Zephyr's tooling statement are as read on 2026-11-06. The FDA's copy carries a note that 21 CFR part 820 was amended, so
  the guidance predates the current rule.

## Honest framing

**This type is contested, its best evidence is regulated, and the guide must lead with who should not use it.** A reader on
an unregulated team should come away able to decide against a matrix. Named practitioners say it rarely repays its
upkeep, and no named unregulated team was found keeping one. In this library's reading, the strongest cases read for a
matrix come from regulated practices and from vendors selling its replacement. The case this bundle can honestly make is narrower. Where a team has
decided it owes a whole-set answer to "which requirement has no verification", a table is one way to give it. Where a
tracker already holds the links, that tracker is the record. **Nothing here shows that a matrix improves outcomes.**

## Notes for the companion

**Facts the companion must carry.**

- Traceability is a property, and the matrix is one implementation of it [2], [13], [6].
- The first use of the phrase is not established, and the companion must say so plainly.
- One table is read in both directions [5], [6], and one matrix or several is a stated choice [6], [2].
- Verified means more than a linked test [22], [21]. This is the bundle's sharpest teaching point.
- The whole-set view exposes what a per-test field cannot. That sentence is the library's inference, and the companion
  labels it as one.
- The dispute, stated with its camps, and the mapping study's statement that strong industrial evidence is still needed
  [16].

**Hazards.**

- **Vendor framing.** Entries [4], [5], [7], [14] and [15] are vendors. Attribute each claim to the vendor by name, and
  say that [7], [14] and [15] sell the fix for the failure they describe. Orcanos' "common FDA 483 observation" line is a
  vendor's unsupported frequency claim, so it may be quoted only as that vendor's claim, or left out.
- **Second-hand speech.** Ambler's, Cockburn's and Bolton's lines in [13] are reports of mailing-list posts. Ambler's own
  essay [10] may be quoted directly. Name the relay.
- **Standards.** Cite for existence only. NASA quotes ISO/IEC/IEEE 24765:2010 in [1], so that definition is NASA's
  quotation of it. Never say what ISO/IEC/IEEE 29148, 21 CFR 820.30 or DO-178C requires. Jama's list of frameworks is
  Jama's claim.
- **NASA's verification matrix** is not this type [2].
- **"Most common" is NASA's phrase** [6]. Attribute it, and do not restate it as a finding.
- **Who may mark a row covered is not established.** Do not imply a rule.
- **No invented cadence.** NASA gives "major phases/key reviews" [6], and Jama gives a change-driven rule. No source gives a
  calendar interval.
- **Do not quote the withdrawn sources,** and do not reintroduce the Texas name-specification claim or a graded coverage
  scale as sourced.
- **Example reuse.** Grep the template for `Saved Views`, `FR-`, `TC-047`, `R-05`, `DEF-2291` and `Permissions` before
  review.

**The example.** The matrix for Saved Views for Dashboards, on the Reporting Platform Modernization program at the fictional
Acme Analytics, full size. The family's shared-scenario rule requires that program, and the `qa-docs` thread supplies real
rows. Read `prd_example.md`, `test-plan_example.md`, `test-case_example.md`, `test-summary-report_example.md`,
`bug-report_example.md`, `risk-register_example.md`, `user-stories_example.md` and `acceptance-criteria_example.md` first, and
contradict none of them. **Date it after the test summary report's 2026-07-17 and before the sibling examples it would
otherwise contradict, and cite only documents that exist by that date.**

**Facts the example must carry, with no contradiction.**

- FR-1 to FR-6 come from `prd_example.md`: FR-1, FR-2 and FR-3 at Must, FR-4 and FR-5 at Should, FR-6 at Could.
- FR-6 is shown as deferred, with its reason: `test-plan_example.md` puts FR-1 to FR-5 in scope and defers FR-6 because it was
  not built.
- `TC-047` appears as a test that traces to risk R-05 and to no acceptance criterion, as `test-case_example.md` states.
- R-05 matches `risk-register_example.md` and the test plan, including its escalated status and residual score.
- DEF-2291 and its closure match `bug-report_example.md` and the test summary report.
- **Use only the case IDs the thread already holds:** TC-046, TC-047, TC-048, TC-052 and TC-053. Check what each one verifies
  before placing it. Where the thread names an area and no case ID, cite the test plan's area by name and do not invent IDs.
- No regulation is invented. Acme is not regulated.

**The gap the example must catch, which is what answers the stop rule.** `prd_example.md`'s non-functional table states
"Permissions | A shared view never exposes data the recipient could not already access on that dashboard", and that row
has no ID, so nothing can trace to it. TC-047 verifies exactly this and records only a risk link. The test plan's in-scope line
names FR-1 to FR-5, and the summary report separately lists non-functional coverage. So the most serious requirement in the
release has the strongest testing and no trace, and no single document shows that. Only a whole-set view does. **The matrix
should assign that requirement an ID, record the decision, and show TC-047 tracing to it.** Check the sibling files before
writing this, and if a sibling already links them, say what is actually missing. Do not manufacture a gap.

**The example must also justify itself plainly, in Purpose and Boundary.** Say why an unregulated team kept one for this
feature: R-05 was escalated above the PII appetite line, the matrix covers this one feature and not the whole product, and
it was kept by hand for one release. NASA's value-based tracing [6] is the honest frame. It must say what the team did not
trace, and when it will stop keeping the matrix. **If the example reads as overhead, the build stops,** per ADR 0084.

## Sources

### Origins and the standards lineage

**[1] NASA - Software Engineering Handbook (Ver B), SWE-052, Bidirectional Traceability Between Higher Level Requirements and Software Requirements.** primary. **fetched-and-verified.**
`https://swehb.nasa.gov/display/SWEHBVB/SWE-052+-+Bidirectional+Traceability+Between+Higher+Level+Requirements+and+Software+Requirements`
Supports: NASA's requirement to perform, record and maintain bidirectional traceability, the handbook's recommendation of a matrix, its warning against duplicating requirement text in the matrix, and ISO/IEC/IEEE 24765:2010's definition as NASA quotes it. The standard itself was not read
Quotable: "The project manager shall perform, record, and maintain bidirectional traceability between the software requirement and the higher-level requirement."
Quotable: "association among two or more logical entities that is discernible in either direction (to and from an entity)"
Quotable: "Full requirements test coverage is virtually impossible without some form of requirements traceability."
Quotable: "do not duplicate requirements in the traceability matrix"

**[2] NASA - Systems Engineering Handbook (NASA/SP-2016-6105 Rev2), web edition, Appendix page (glossary, Appendix D Requirements Verification Matrix, Appendix E Validation Requirements Matrix).** primary. **fetched-and-verified.**
`https://www.nasa.gov/reference/system-engineering-handbook-appendix/`
Supports: NASA's glossary definitions of traceability and bidirectional traceability, and a verification matrix scoped to "shall" statements with a separate validation matrix. This verification matrix is a related artifact and not the requirements-to-design matrix, and the page text does not reproduce the columns of Table D-1
Quotable: "The ability to trace any given requirement/expectation to its parent requirement/expectation and to its allocated children requirements/expectations."
Quotable: "A discernible association among two or more logical entities such as requirements, system elements, verifications, or tasks."
Quotable: "Only “shall” requirements should be included in these matrices."
Quotable: "The matrix should identify each “shall” by unique identifier and be definitive as to the source"
Quotable: "This matrix could be divided into multiple matrices (e.g., one for each requirements document)"

**[3] US FDA - General Principles of Software Validation; Final Guidance for Industry and FDA Staff, 11 January 2002.** primary. **fetched-and-verified.**
`https://www.fda.gov/media/73141/download`
Supports: The FDA's call for a software requirements traceability analysis, to system requirements and to risk analysis results. The guidance never uses the word matrix. It supports nothing about 21 CFR 820.30 or the QMSR, neither of which was read
Quotable: "A software requirements traceability analysis should be conducted to trace software requirements to"
Quotable: "(and from) system requirements and to risk analysis results."

### Structure and column sets

**[4] Visure Solutions - What is Requirements Traceability Matrix (RTM)?.** vendor. **fetched-and-verified.**
`https://visuresolutions.com/blog/software/traceability-matrix`
Supports: One vendor's list of matrix components, three trace directions defined in prose, and an audit habit. It is a vendor page that shows no table, and its risk and defect links appear only in a description of its product
Quotable: "Requirements ID: A unique identifier assigned to each requirement for easy tracking and reference."
Quotable: "Identifies where each requirement originated"
Quotable: "Links requirements to corresponding test cases to verify their implementation and functionality."
Quotable: "Maps each requirement to specific development tasks and deliverables"
Quotable: "Backward traceability links design elements, code, and test cases back to the original requirements."
Quotable: "Bidirectional traceability combines both directions"
Quotable: "Regularly audit the RTM to ensure that all requirements are fully traced"
Quotable: "configurable traceability matrices and end-to-end relationships across requirements, risks, tests, defects, source code, and other lifecycle artifacts"
Quotable: "detect missing links"
Quotable: "a structured document or tool designed to establish and maintain traceability"
Quotable: "Requirements ID and Description"
Quotable: "Source of Requirements"
Quotable: "Associated Test Cases"
Quotable: "Development Tasks and Deliverables"

**[5] TestDevLab - Traceability Matrix, Center of Excellence glossary.** vendor. **fetched-and-verified.**
`https://www.testdevlab.com/center-of-excellence/glossary/engineering-terms/traceability-matrix`
Supports: The narrowest definition, requirement to test case in both directions, and gap identification and change maintenance as purposes. It shows no columns beyond those two
Quotable: "links and maps project requirements to their corresponding test cases"
Quotable: "every requirement is covered by at least one test case, and conversely, that every test case is linked to a valid requirement"
Quotable: "Identify Gaps: Highlight any requirements that do not have a corresponding test case."
Quotable: "Streamline Maintenance: When a requirement changes, it is easy to identify which test cases need to be updated."
Quotable: "Requirement R1 is covered by Test Case TC-001"
Quotable: "every test case is linked to a valid requirement"
Quotable: "A Traceability Matrix is a document that links and maps project requirements to their corresponding test cases."
Quotable: "Highlight any requirements that do not have a corresponding test case."

**[6] NASA - Software Engineering Handbook, SWE-059, Bidirectional Traceability Between Software Requirements and Software Design.** primary. **fetched-and-verified.**
`https://swehb.nasa.gov/spaces/7150/pages/16449675/SWE-059+-+Bidirectional+Traceability+Between+Software+Requirements+and+Software+Design`
Supports: NASA's practical guidance: when to create the matrix, one matrix read in both directions, unique identification of elements, an assigned owner, review at major phases, one combined matrix or matrices inside each document, links that need not be one-to-one, orphans discussed and missing requirements added, the staleness risk of a spreadsheet, and value-based tracing for small budgets
Quotable: "Assign responsibility for creating and maintaining the matrix to a project team member"
Quotable: "the relationships identified in the matrix are not required to be one-to-one"
Quotable: "It is very important that the project be diligent about keeping such traces up to date as these methods do not include automatic updates"
Quotable: "Value-based requirement tracing prioritizes all of the requirements in the system"
Quotable: "Before starting the traceability activity, it is assumed that the documents being traced"
Quotable: "While traceability matrices are not the only method for capturing bidirectional traceability, they are the most common."
Quotable: "Traceability matrices can be included in the documents to which they apply"
Quotable: "they can be combined into a single matrix covering higher level requirements, software requirements, design, code, and verification"
Quotable: "Create the matrix at the beginning of the project."
Quotable: "Uniquely identify the elements in the matrix"
Quotable: "allows a single exercise to show traceability both forwards and backwards"
Quotable: "Keep the matrix maintained throughout the life of the project."
Quotable: "Ensure a review of the matrix at major phases/key reviews of the project."
Quotable: "can be manually created and maintained, or may be a by-product of a requirements management tool"
Quotable: "they need to be discussed by the project team and assurance personnel"
Quotable: "If they are determined to be necessary, any missing source requirements are added to the project."
Quotable: "Value-based requirement tracing may be an option for projects with small budgets"
Quotable: "This can save a significant amount of effort by focusing traceability activities on the most important requirements."

**[7] Zohar Peretz (Orcanos) - Requirements Traceability Matrix for Medical Devices: A Complete Compliance Guide, 4 June 2026.** vendor. **fetched-and-verified.**
`https://www.orcanos.com/blog/requirements-traceability-matrix-for-medical-devices-a-complete-compliance-guide`
Supports: A vendor's account for medical devices: forward-only called incomplete, a missing risk-control column named as a failure, baselining at design review gates, and an impact assessment with each design change. Orcanos sells the platform that fixes these failures, and its frame is stricter than general software
Quotable: "An RTM that only maps forward is incomplete. Auditors will run both directions."
Quotable: "The RTM has no column for risk controls."
Quotable: "The RTM is where risk management and design control intersect."
Quotable: "A minimal RTM maps requirements to tests."
Quotable: "Teams often maintain this in a separate development tool with no linkage to the QMS-level RTM."
Quotable: "Every approved design change must include an RTM impact assessment as part of the change package."
Quotable: "Untraced changes are a common FDA 483 observation."
Quotable: "At each formal design review gate, baseline the RTM."
Quotable: "Record which version of the RTM was reviewed and approved."
Quotable: "No orphaned requirements or orphaned tests exist in the matrix"
Quotable: "proves nothing was missed"
Quotable: "proves nothing untraceable was implemented"

### Practice: who keeps one and who declines

**[8] The Ferrocene Developers - Ferrocene documentation index, with its Traceability matrix report.** primary. **fetched-and-verified.**
`https://public-docs.ferrocene.dev/main`
Supports: The one named software team's own published matrix found: the Ferrocene Language Specification mapped to the test suite, for safety-critical qualification. Its report page, read raw on 2026-11-06 and too large to cache, listed 331 linked and 21 informational sections of 352, and 54 of 54 command-line options. It shows practice in regulated work only
Quotable: "A matrix that ties the specifics of the Ferrocene Language Specification to the test suite."
Quotable: "This was written to ensure that all documented requirements are covered."

**[9] Zephyr Project - Zephyr Safety Overview.** primary. **fetched-and-verified.**
`https://docs.zephyrproject.org/latest/safety/safety_overview.html`
Supports: A named open source project's stated aim to trace requirements to code for IEC 61508 certification. The page says the tooling and CI enforcement were still being worked on, so it shows intent and not a running matrix
Quotable: "tracing the requirements down to the code level is used"
Quotable: "The tooling is in evaluation"

**[10] Scott W. Ambler (Ambysoft) - Agile Requirements Best Practices, practice 11, Question Traceability.** practitioner. **fetched-and-verified.**
`https://agilemodeling.com/essays/agileRequirementsBestPractices.htm`
Supports: A named practitioner's position that in simple situations manually kept matrices rarely repay their cost, his simple-situation alternative, and the four conditions he says justify traceability. His basis is experience, not measurement
Quotable: "traceability matrices are highly overrated because the total cost of ownership (TCO) to maintain such matrices, even if you have specific tools to do so, far outweigh the benefits"
Quotable: "a traceability matrix is effectively a document and is therefore a business decision to be made by them"
Quotable: "In simple situations, which many agile teams find themselves in, my experience is that traceability matrices are highly overrated"
Quotable: "The quick answer is in some complex situations and when you have proper tooling support"
Quotable: "it is much easier and cheaper to simply ask them to estimate the change"
Quotable: "With automated tooling the TCO of traceability drops"
Quotable: "Sometimes you have actual regulatory compliance needs"

**[11] Johanna Rothman - Traceability Matrix and Agile, No Fluff Just Stuff blog, 11 July 2008.** practitioner. **fetched-and-verified.**
`https://nofluffjuststuff.com/blog/johanna_rothman/2008/07/traceability_matrix_and_agile`
Supports: A named consultant's report that some clients keep traceability on index cards and others in a spreadsheet under source control. It reports clients' practice, not a team's own matrix
Quotable: "Some of my clients keep their index cards and organize the traceability that way, with notes about where the tests are."
Quotable: "Other folks use a spreadsheet for the organizing. They use a source control system to manage the changes to the file."
Quotable: "The fewer artifacts, the better."

**[12] Davide Fucci, Emil Alegroth and Thomas Axelsson - When Traceability Goes Awry: an Industrial Experience Report, arXiv 2206.04462, 2022.** academic. **fetched-and-verified.**
`https://arxiv.org/pdf/2206.04462`
Supports: An experience report on a large, anonymized telecommunications company that lacks requirement-to-test and requirement-to-code traces, and the authors' advice to be selective. The company is unnamed, so it is not a named team's account
Quotable: "we found that such traces were generally lacking"
Quotable: "traceability between high-level requirements, source code, and test suites is not maintained at COMPANY"
Quotable: "the situation we observed at COMPANY indicates that such requirements may have been overstated"
Quotable: "we encourage practitioners to be selective about the traceability links necessary for their organization"

### Debates: upkeep, tools and the value outside regulated work

**[13] Vikas Hazrati - Traceability Matrix in an Agile Project, InfoQ news, 6 June 2008.** practitioner. **fetched-and-verified.**
`https://www.infoq.com/news/2008/06/agile-traceability-matrix`
Supports: The 2008 agile case against the matrix as a secondary report of mailing-list posts: Ambler on cost, Cockburn on never seeing one pay off, Appleton on traceability against the matrix, Bolton on corporate memory, and tests and commit links as substitutes. No figures appear in it
Quotable: "My experience is that traceability matrices are highly overrated because the total cost of ownership (TCO) to maintain such matrices, even if you have specific tools to do so, far outweigh the benefits."
Quotable: "I'm a firm believer in traceability if you have actual regulatory compliance needs"
Quotable: "The cost was so staggeringly high that the client removed the traceability requirement from the contract."
Quotable: "I have, in 30 years in the business, in industry, research and a little bit in government, NEVER seen a traceability matrix pay off."
Quotable: "manually creating, updating and maintaining traceability matrices is the most time consuming way of demonstrating traceability"
Quotable: "Within the agile paradigm traceability from code/design to requirements is done through unit and acceptance tests."
Quotable: "traceability matrix would only be required when there is a danger of losing corporate memory that is genuinely valuable"
Quotable: "When he does a commit he associates the name or id of the story with the commit."
Quotable: "A formal traceability matrix often evokes strong response from the Agile community"
Quotable: "Traceability matrix on the other hand is one of the possible implementations of traceability."
Quotable: "traceability comes with the ride automatically"

**[14] Mario Maldari (Jama Software) - Traceability Matrix 101: Why It's Not the Ultimate Solution for Managing Requirements, republished 29 May 2026.** vendor. **fetched-and-verified.**
`https://www.jamasoftware.com/?p=11155`
Supports: A vendor's argument for a live view over a static matrix: the update rule, drift, false confidence, the versioned snapshot, and its concession that no framework prohibits spreadsheets. Jama sells the live replacement
Quotable: "Trace links can drift out of sync within weeks."
Quotable: "A pervasive practitioner belief that traceability costs more than it delivers leads to deferred maintenance"
Quotable: "No major regulatory framework explicitly prohibits spreadsheets."
Quotable: "As long as a matrix stays current and complete, it remains useful for"
Quotable: "the same artifact that once created clarity can instead produce false confidence."
Quotable: "A requirements traceability matrix is a structured information artifact"
Quotable: "should be updated whenever requirements, test cases, or linked lifecycle artifacts change, not just on a calendar schedule."
Quotable: "a specific versioned artifact that captures those links at a point in time."
Quotable: "is widely used in regulated product development"
Quotable: "Systems engineering teams are shifting away from a document-centric approach"

**[15] Jake Stowe (Ketryx) - Best Practices for Maintaining a Requirement Traceability Matrix in Agile, 12 September 2023.** vendor. **fetched-and-verified.**
`https://www.ketryx.com/blog/best-practices-for-maintaining-a-requirement-traceability-matrix-in-agile`
Supports: A vendor's argument that the matrix is a living artifact and that manual upkeep in Excel should be avoided. Ketryx sells automated traceability, in an FDA-regulated setting
Quotable: "An RTM is not a static document but rather a living artifact that evolves with the software development process."
Quotable: "Excel can no longer manage RTMs for modern software."
Quotable: "error-prone, extremely time consuming, and difficult to maintain"

**[16] Fangchao Tian, Tianlu Wang, Peng Liang, Chong Wang, Arif Ali Khan and Muhammad Ali Babar - The Impact of Traceability on Software Maintenance and Evolution: A Mapping Study, arXiv 2108.02133, 2021.** academic. **fetched-and-verified.**
`https://arxiv.org/pdf/2108.02133`
Supports: A mapping study of 63 papers from 2000 to May 2020: link upkeep is the main cost, easier change management the main benefit, and strong industrial evidence is still needed. It studies traceability in maintenance and evolution, not the matrix as a document
Quotable: "establishing and maintaining traceability links is the main cost of deploying traceability practices"
Quotable: "easing the process of change management is the main benefit of deploying traceability practices"
Quotable: "strong empirical evidence from industry is needed to validate the impact of traceability on maintenance and evolution"
Quotable: "most of the studies have provided the evidence using toy examples or academic studies"

### Relationships with neighbouring documents

**[17] NASA - Software Engineering Handbook, SWE-071, Update Test Plans and Procedures.** primary. **fetched-and-verified.**
`https://swehb.nasa.gov/x/5gP7`
Supports: A traceability matrix as a change-impact aid for test plans and procedures, and a test representative on the change control board
Quotable: "3.4.7 The project shall update Software Test Plan(s) and Software Test Procedure(s) to be consistent with software requirements."
Quotable: "Using a traceability matrix which identifies the test plans, procedures, scripts, test cases and even test data associated with each requirement can be helpful"
Quotable: "Including a test team representative as part of the CCB or other authorized group responsible for approving changes to requirements."

**[18] NASA - Software Engineering Handbook, SWE-114, Software Test Procedures.** primary. **fetched-and-verified.**
`https://swehb.nasa.gov/x/mAD7`
Supports: Test procedures carrying their own traceability or pointing at the document that holds it, the closest external statement of how a per-test field relates to a trace held elsewhere
Quotable: "include bidirectional traceability to the requirements or a reference to the document containing that trace."
Quotable: "Verification that all requirements were tested."

**[19] Wikipedia - Traceability matrix, retrieved 2026-11-06.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Traceability_matrix`
Supports: A tertiary description of a matrix as a many-to-many comparison of two baselined documents, and advice to add the relationships to the source documents too. It carries no authority beyond the shape of the relationship
Quotable: "it is advisable to add the relationships to the source documents for both backward and forward traceability"
Quotable: "correlating any two baselined documents using a many-to-many relationship comparison"

**[20] Wikipedia - IEEE 829, retrieved 2026-11-06.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/IEEE_829`
Supports: A tertiary summary of the IEEE 829 document set, in which the test report summarises results after execution and no listed document is a traceability matrix. The standard was not read
Quotable: "To summarise the results of the designated testing activities and to provide evaluations and recommendations based on the results after test execution has finished for the specific test level."

### The gap question

**[21] Andrew Van - jamb documentation, Traceability Requirements (IEC 62304 Guide).** practitioner. **fetched-and-verified.**
`https://jamb.readthedocs.io/en/latest/iec-62304/traceability.html`
Supports: One tool's published matrix design: suspect links by content hash, a status column separating Passed, Failed, Not Covered and N/A, a header recording tester and version, and a flag for requirements verified by other means
Quotable: "the hash it recorded at link time no longer matches"
Quotable: "Once the SRS items are reviewed and updated (or confirmed unchanged), the links are re-acknowledged and the suspect flag clears."
Quotable: "This mechanism ensures that no change propagates silently through the traceability chain."
Quotable: "unlinked items (items that should have parent links but do not), broken links (references to items that no longer exist), and suspect links (where the upstream item has changed since the link was created)"
Quotable: "Tester : Who executed the tests"
Quotable: "indicating they are verified by other means (inspection, analysis, demonstration)"

**[22] NASA - Systems Engineering Handbook, web edition, section 5.3, Product Verification.** primary. **fetched-and-verified.**
`https://www.nasa.gov/reference/5-3-product-verification/`
Supports: NASA's statement of when verification is complete: objective evidence or a waiver, plus closure of nonconformance reports, with results recorded in a compliance or verification matrix
Quotable: "documented objective evidence of compliance with requirements or waiver"
Quotable: "closure of all discrepancy and nonconformance reports"
Quotable: "Verification results should be recorded in a requirements compliance or verification matrix"

## Pages not read under the terms rule

No page here is on the runbook's excluded table. These pages stayed unread, or were withdrawn, because the site's terms could not be checked or a template sits behind a wall. No claim rests on any of them, and the maintainer may read any of them by hand.

- `https://dir.texas.gov/sites/default/files/Requirements%20Traceability%20Matrix%20Template.doc`: the site's policies page and a raw fetch both returned 403. It would show a government template's real column set, which no page read here shows.
- `https://dir.texas.gov/sites/default/files/Requirements%20Traceability%20Matrix%20Instructions.pdf`: the same refusal. An agent read it with a browser-style client, and this log withdrew it. It would support a government page specifying a matrix under the full name.
- `https://www.projectmanagement.com/deliverables/614623/requirements-traceability-matrix-template`: PMI's template, behind a membership wall. It would add a standards-body column set.
- `https://link.springer.com/article/10.1007/s00766-023-00408-9`: Ruiz and colleagues, 2023, on why teams do not trace. The publisher's page returned a client challenge. It would add survey evidence on perceived cost and benefit.
