# change-request: research log

Research conducted 2026-09-25 in two passes: an admission sweep run while the spec was written (thirteen
agents across this type and `announcement-internal-comms`, covering IT service management, project change
control, boundaries and the library's own references), and the build's six-dimension fan-out (definitions and
process, published forms, the IT service neighbour, the agile position, boundaries and failure modes, and the
standing gap question). **48 sources are recorded below, all fetched-and-verified.** Only
`fetched-and-verified` sources are quoted anywhere in this bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a
retrieval tool returns. Pages were read as downloaded (HTML decoded as UTF-8, PDFs through `pdftotext` without
`-layout`, `.docx` files from their `word/document.xml`, 1997-format `.doc` files through `antiword`) and each
quotation searched for as a normalized substring. Of 246 quotations the build's agents returned, 225 passed as
returned. Of the other 21, thirteen were composites (a glossary term fused to its definition, several sentences
run together across a page break, a list flattened into one line) and survive here **only as the separate
sentences that are verbatim on the page**; eight were dropped. Ten salvaged fragments too short to mean anything
were removed, and eight quotations were added from the main loop's own checks.

---

## What the checks caught, and what was not read

**A research agent overwrote a cached source with an extraction that broke every sentence in it.** The source
cache held the raw text of [20], the 2019 DORA report, from the admission sweep. During this build it was
replaced with a layout-preserving extraction that interleaves the report's two columns, and every quotation from
it then failed. The raw text was restored (`pdftotext` without `-layout`) and re-checked. Two quotations survive
only as their first sentence, because in the raw text a footnote falls between that sentence and the next.

**The spec recorded prince2.wiki's licence too narrowly.** Its footer carries two statements that answer
different questions: the wiki's own text is offered "with a Creative Commons Attribution license" ([5]), while
the PRINCE2 name is an AXELOS trade mark. The spec's admission table gave only the second.

**Three sources were read from the Internet Archive**, and each entry below carries the address actually read.
[9], the CDC Unified Process form, and [11], the HHS EPLC plan, return 404 and 403 at their live addresses. [35],
Larson and Larson's PMI Global Congress paper, is refused to scripted requests by pmi.org and was read from the
Archive's snapshot of 14 April 2021; its entry carries the pmi.org address under which that copy was cached.

**Eight quotations were dropped:** one from [4] that ran two sentences together (its verbatim clause survives),
[8]'s placeholder text, [9]'s option for approval with conditions (the form's table cell breaks the phrase across lines,
so the option is described rather than quoted), a status value from [11], two sentences from [45] and [47]
that are not on their pages, and parts of [38] and [39] that were not verbatim.

**ITIL's own vocabulary moved between editions.** [17], the ITIL 2011 glossary, defines a normal change; [16],
the ITIL 4 Foundation glossary, has no entry for it. This touches only the neighbour this bundle does not
template.

**Not read, and nothing in this bundle may rest on them:**

- **The PMBOK Guide itself.** Only its openly hosted errata [2] was read.
- **ISO 21502:2020 and ISO/IEC 20000-1:2018** beyond their catalog pages and a redline sample's contents list.
- **AXELOS's PRINCE2 manuals and the ITIL 4 Change Enablement practice guide**, behind subscriptions.
- **A Scrum.org forum thread and a remark attributed to Mary Poppendieck**, seen earlier only as search
  snippets and deliberately not pursued. Neither may be quoted.
- **Ward Cunningham's wiki page on fixed-price contracts with change control**, which renders only with a script.

---

## The admission record

**ADR 0030's bar is met many times over, in the project and product baseline lineage this bundle serves.** The
definition is agreed across four bodies: [1] PMI ("change request. A formal proposal to modify a document,
deliverable, or baseline."), [3] APM ("A request to obtain formal approval for changes to the approved
baseline."), [7] the European Commission's PM² guide ("A change request logs an appeal to amend an aspect of the
agreed baseline of a project (i.e. scope, requirements, deliverables, resources, costs, timeframe or quality
characteristics).") and [5] PRINCE2 ("It is a proposal for a change to a baselined product"). Four named public
bodies publish the form itself: PM² [8], the CDC Unified Process [9], the US GSA [10] and the Texas Department of
Information Resources [12]. **[7] is licensed CC BY 4.0 and is the only source whose wording this bundle may
adapt**; [1] is licensed "for personal use only", and the forms state no licence, so they are structure evidence.

**The IT service lineage is equally well published and is the named neighbour, not the subject:** NIST's sample
change request in [14], Prairie View A&M's form [48], and IT Process Wiki's checklist [18].

**The family is `delivery-docs`, by
[ADR 0060](../../docs/internal/decisions/0060-change-request-joins-delivery-docs.md)**, which widened that
contract's membership test with the verb "changes" after no contract admitted a per-occasion change request as
written.

---

## Claims flagged contested or time-bound

1. **Is a change request an issue?** PRINCE2 says yes: "There are five types of issues" and a request for change is
   one ([5]). PMI ([1], [2]), APM ([3], [4]) and PM² ([7]) treat it as its own document with its own log. **This
   library's ruling**, from `issue-log`'s spec: the request records where it came from and links back to the issue
   log when there is one. PRINCE2's own page concedes the overlap ("The issues practice is not solely about
   handling change requests").
2. **Does the decision belong on the form?** [8] carries no decision; its decision is made after the form is logged.
   [9] and [10] carry a decision section ("CHANGE CONTROL BOARD - DECISION", "Change Control Board Approval
   Information"). [12] puts per-approver checkboxes under a column headed Recommendation.
3. **Is the request separate from the log?** [8] archives the form once it is logged ("Once the change request is
   logged into the Change Log, then this form is updated with the assigned Change ID and the form is archived");
   [2] says "The change log is used to record all submitted change requests." [11] merges the two into one field
   list ("AT A MINIMUM, THE FOLLOWING DATA SHOULD BE INCLUDED ON THE PROJECT'S CHANGE REQUEST FORM AND CHANGE
   MANAGEMENT LOG").
4. **Are defects change requests?** [10] offers Defect as a type of change and [9] offers Enhancement or Defect.
   [31] draws the opposite line: a bug is "something is wrong with the delivered code", a change request is "new
   and additional to what was delivered". This library's `bug-report` guide follows [31].
5. **What the decision can be.** [7]: "There are four possible decisions: approve, reject, postpone or merge the
   change request". [4]: "captured, evaluated and then approved, rejected or deferred". [1]'s change control board
   is "responsible for reviewing, evaluating, approving, delaying, or rejecting changes". [9] adds approval with
   conditions and a request for more information; [10] has three outcomes.
6. **Does agile work need one?** The 2020 Scrum Guide routes change through one person ([21]: "Those wanting to
   change the Product Backlog can do so by trying to convince the Product Owner"), and the Manifesto values
   "Responding to change over following a plan" ([22]). Against that, [26] reports that fixed contracts carry
   change-control provisions anyway, [27] writes change into the contract itself ("Change for Free", at Sprint
   boundaries), and [25] shows change control surviving as a required design-control procedure in an
   FDA-regulated project. [26] also records Allen Holub's contrary view verbatim. **Genuinely unresolved; the
   companion reports both camps.**
7. **What DORA's finding is about.** [20] and [19] concern approval of **production changes** by an external body:
   "We found that formal change management processes that require the approval of an external body such as a
   change advisory board (CAB) or a senior manager for significant changes have a negative impact on software
   delivery performance." [20] also holds that "there is still an important role for the CAB". **No source applies
   the finding to a project baseline change board**, and this bundle must not.
8. **Change boards as bottlenecks or rubber stamps.** Sourced only for IT service change boards, by named
   consultants quoted in [36] ("CABs belong in history as an example of how ITSM put a straightjacket around agility
   and innovation"). No project-management source for the same claim was found.
9. **How much a request needs.** Lean templates ([44], [45]) stop at requester, description, reason, impact and
   approval; [43] adds options with their impact and the reason one was chosen; [40] and [41] argue that without
   options, conditions, a deadline and a decision record the process degrades. All of these are vendor or
   practitioner tier. *(Corrected 2026-09-25, during review: this item grouped [43] with the lean templates,
   which its own entry contradicts.)*

---

## Notes for the companion

**The honest framing.** Unlike most types in this library, a change request's definition is settled: four bodies
state it in nearly the same words. What is contested is where it lives (an issue type or its own document; a form
with the decision on it or without), whether a team working from a backlog needs one at all, and which of two
lineages the name means. This bundle serves the project and product baseline lineage because the library's own
routing already used that sense; IT service change is its closest neighbour, described and not templated.

**The evidentiary spine, in the order it should be used:**

- **Definition:** [1], [3], [7], [5], quoted above.
- **Process and decision:** [7]'s five steps and four decisions; [2] ("Perform Integrated Change Control is the
  process of reviewing all change requests; approving changes and managing changes to deliverables, project
  documents, and the project management plan; and communicating the decisions."); [4]; [1]'s change control board.
- **The authority:** [6]: "The change authority is a person or group to whom the project board may delegate
  responsibility for reviewing and approving change requests or off-specifications. This authority may be given a
  change budget and can approve changes within that budget." Its worked example delegates a change under EUR 400
  to the project manager, which makes a named authority concrete.
- **Published forms:** [8], [9], [10], [12]; [11] as the merged case; [13] as a PMO's completion guidance.
- **The agile position:** [21], [22], [23], [26], [27], [25].
- **The neighbour:** [14], [18], [48], [16], [17]; DORA [19], [20], bounded as above.

**How it fails, as sourced, and nothing more:**

- **Change that is never authorized.** [35] defines scope creep by authorization, not by size: "The key part is
  whether changes are authorized or not."
- **Decisions that never get made.** [37] names change requests among the things whose postponement goes untracked
  ("the cost of decisions not made"), and [41] traces board deferral to a missing deadline ("A change request
  without a deadline gives the board permission to defer indefinitely."). **Both are thin**: one 2026 personal blog
  post and one vendor post. The companion says the failure is described, not measured.
- **Overstating the case to win approval.** [39], as practitioner testimony: "do not over state the impact in an
  attempt to gain approval".
- **Calling a request a bug, or a bug a request.** [31].

**What this bundle must not say:** that DORA's finding applies to project change boards; that project change boards
are commonly bottlenecks or rubber stamps as a documented fact; anything from Prosci's writing on change fatigue, which is
about organizational change; any claim resting on the Scrum.org thread or the Poppendieck remark; any scope-creep
statistic.

**The section design, as the research moved it from the spec.** The spec's seven sections hold (four in lean: The
Request, Why, Impact, Decision; full adds Options Considered, Out of Scope, Implementation and Traceability), and
every one now has a published form behind it:

- **The Request:** [8]'s "Current Situation" and "Desired Situation"; [40]: "Separate the underlying need from the
  requester's preferred implementation."; where it came from, in [7]'s words ("identified and raised during meetings
  as a result of decisions, issues or risks").
- **Why**, including what happens if the change is not made: [7] ("consider the impact of not implementing"), [12]'s
  "Impact of Not Implementing" field, and [39] ("you should include details of the consequence of not accepting the
  change").
- **Impact:** [7]'s baseline list, [9]'s hour, duration, schedule and cost impact, [10]'s estimates, [12]'s
  schedule-impact table. [39]'s impact outside the project is a row hint, not a section.
- **Decision:** [7]'s four decisions, one named decider, the date, and conditions. **The research adds two things the
  spec did not have, and the lean variant should carry both**: a date by which the decision is needed ([39]: "you
  should include the deadline by when a decision is required on the change request"; [41]), and conditions that each
  carry an owner and a deadline ([40]: "Approval with conditions must identify the owner and deadline for each
  condition"). Both sources are practitioner or vendor tier and the guidance says so.
- **Options Considered:** [43] ("Options considered to implement the change", "For each option, explain the impact on
  Cost, Scope, Schedule and Quality"), [40] ("Options, including no change"), [12]'s Alternatives field.
- **Out of Scope:** [8]'s section of that name; [40]: "Define what will be added, removed or modified and what remains
  explicitly out of scope."
- **Implementation and Traceability:** [8]'s archive-once-logged rule, [2]'s change log, and [40]'s standard for the
  record ("A sound record lets an authorized reviewer reconstruct the prior baseline, requested difference, evidence,
  options, authority, implementation and result").

Candidates from the gap question that go to the guide or rubric rather than the template: separating the risk of
making the change from the risk of declining it ([40]: "Distinguish the risk of making the change from the risk of
declining or delaying it."), reversibility, recording each approving authority separately, and watching cumulative
change across requests, which is a property of the log, not of one request.

**Teaching points the templates, guide and example must stay consistent with:**

- **A change request alters an agreement; a defect fails one** ([31]). The template offers no Defect type, and the
  companion reports that [9] and [10] do.
- **It names the baseline it changes**, by artifact and version.
- **It says what happens if the change is not made** ([7], [12], [39]).
- **One named decider, and a decision chosen from a stated set** ([7], [1], [6]).
- **A decision date**, so a request cannot wait forever ([39], [41]; practitioner and vendor tier, labelled).
- **Conditions carry an owner and a date** ([40]).
- **The request is not the log.** It links to the change log entry and back to its origin ([2], [8]).
- **A team changing its own backlog through its product owner does not need one** ([21]); the bundle is for
  baselines that carry weight outside the team: a contract ([26], [27], [24]), a regulator ([25]), or a budget and
  scope a steering group signed off.

**The example.** A change request against the **Saved Views PRD** (`prd_example.md`: owner Priya Nair (PM, Reporting),
doc version 0.3.0, created 2026-06-12, updated 2026-06-30), chained onto the delivery-docs scenario. The PRD lists as a
non-goal "Scheduled delivery of a view by email or Slack. Out of scope now; likely a fast follow." The request asks to
bring it into scope, and the decision **postpones** it to a follow-on release, one of [7]'s four decisions. It must be
dated inside the PRD's life and agree with every later sibling: `release-notes_example.md` ships no scheduled delivery,
and nothing in the thread says one shipped. **It must not attach a request to ISS-11 or ISS-12**: `issue-log_example.md`
states that neither raised one. **It assigns no release to the postponed work**, and cites no release beyond the
2.4.0 notes that shipped Saved Views, because the thread's release numbering is already
inconsistent between `release-notes_example.md` and the runbook and postmortem examples, a contradiction recorded for
the maintainer and not fixed here. Its requester and decider should be people the thread already names, in roles the
thread already gives them.

**The pairing.** `pairs_with: []`. No pm-skills skill produces or consumes a change request.

**The aliases.** `change record` is kept. `RFC (ITIL)` is dropped because it collides with this library's `rfc` bundle, a
request for comments ([34]: "Request for Comments"); the guide names that collision on its first line. `change ticket`
is dropped as service-desk vocabulary for the lineage not served.

---

## Sources

**[1] PMI, Lexicon of Project Management Terms v5.0.** primary. **fetched-and-verified.**
`https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf?rev=447328d841c249af985d14177ddd5f95`
Supports: Canonical definitions of change request, change control, change control board (CCB) and change control system, cross-referenced to each other and to baseline Its licence: personal use only.
Quotable: "change request. A formal proposal to modify a document, deliverable, or baseline."
Quotable: "change control. A process whereby modifications to documents, deliverables, or baselines associated with the project are identified, documented, approved, or rejected. See also change control board (CCB) and change control system."
Quotable: "change control board (CCB). A formally chartered group responsible for reviewing, evaluating, approving, delaying, or rejecting changes to the project, and for recording and communicating such decisions."
Quotable: "change control system. A set of procedures that describes how modifications to the project deliverables and documentation are managed and controlled."
Quotable: "change management plan. A component of the project management plan that establishes the change control board, documents the extent of its authority, and describes how the change control system will be implemented."
Quotable: "baseline. The approved version of a work product that can be changed using formal change control procedures and is used as the basis for comparison to actual results."
Quotable: "This material is being provided under license to you for personal use only"

**[2] PMI, PMBOK Guide 6th edition, errata (fifth printing).** primary. **fetched-and-verified.**
`https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-6th-edition-5th-printing.pdf?v=5ec5b4d9-abb5-4d42-8542-8af75be7de3b`
Supports: The Perform Integrated Change Control process definition and the change log's role as the register of submitted change requests; the Guide's own body was not read, only this errata document
Quotable: "The change log is used to record all submitted change requests."
Quotable: "Perform Integrated Change Control is the process of reviewing all change requests; approving changes and managing changes to deliverables, project documents, and the project management plan; and communicating the decisions."
Quotable: "This process reviews all requests for changes to project documents, deliverables, or the project management plan and determines the resolution of the change requests."
Quotable: "The key benefit of this process is that it allows for documented changes within the project to be considered in an integrated manner while addressing overall project risk, which often arises from changes made without consideration of the overall project objectives or plans."

**[3] APM (Association for Project Management), Body of Knowledge glossary.** standards. **fetched-and-verified.**
`https://www.apm.org.uk/resources/glossary/`
Supports: APM's definitions of change request and change control board, both anchored to 'approved baseline'
Quotable: "A request to obtain formal approval for changes to the approved baseline."
Quotable: "A formally constituted group of stakeholders responsible for approving or rejecting changes to the project baselines."

**[4] APM, "What is change control?".** standards. **fetched-and-verified.**
`https://www.apm.org.uk/resources/what-is-project-management/what-is-change-control/`
Supports: The change-control process definition (capture, evaluate, then approve/reject/defer) and the claim that change requests commonly arise from issues The three outcomes of change control in APM's account.
Quotable: "Change requests may arise as a result of issues that occur from the management of work or external sources. Issues that result in changes to scope or any other part of the baseline plan are progressed through change control."
Quotable: "captured, evaluated and then approved, rejected or deferred"

**[5] prince2.wiki (Frank Turley / EMPII Group), "Issues" practice page.** practitioner. **fetched-and-verified.**
`https://prince2.wiki/practices/issues/`
Supports: PRINCE2's taxonomy that files a change request ('request for change') as one of five types of issue, not as a standalone document category, plus its baseline/approval mechanics and the four PRINCE2 management-product names for issue and change handling The wiki's own content licence, distinct from the AXELOS trademark notice on the same footer.
Quotable: "There are five types of issues; they are: Request for change : It is a proposal for a change to a baselined product, i.e., a product that has already been approved."
Quotable: "PRINCE2 categorizes proposals to change a baseline as either a request for change or off-specification."
Quotable: "Request for change: A proposal to change a baseline."
Quotable: "Change control: The process of identifying, assessing, approving, rejecting, or deferring changes that may affect the project baseline."
Quotable: "The issues practice is not solely about handling change requests; it also focuses on addressing issues that arise during the project. In fact, it is better to think of the issues practice as providing a unified approach to both issues and change control."
Quotable: "Once a change request or off-specification is approved, the project manager is responsible for ensuring it is recorded in the project log (issue register) and updated in the relevant management products."
Quotable: "A request for change must specify the management products to be changed and provide justification. If the change has a cost, it must be funded by the approved change budget or additional funds."
Quotable: "PRINCE2 wiki is provided by EMPII Group with a Creative Commons Attribution license"

**[6] prince2.wiki (Frank Turley / EMPII Group), "Change authority" page.** practitioner. **fetched-and-verified.**
`https://prince2.wiki/people/change-authority/`
Supports: The definition of PRINCE2's change authority as the delegated decision-maker for change requests, distinct from the project board
Quotable: "The change authority is a person or group to whom the project board may delegate responsibility for reviewing and approving change requests or off-specifications. This authority may be given a change budget and can approve changes within that budget."
Quotable: "For example, with a level 2 issue (change request), The project manager could approve a change if only one product is affected and the change is under €400, provided it is within the agreed tolerance."

**[7] European Commission, PM² Project Management Methodology Guide v3.1 (2023).** standards. **fetched-and-verified.**
`https://www.pm2alliance.eu/wp-content/uploads/2024/02/pm%C2%B2-project-management-methodology-NO0523520ENN.pdf`
Supports: PM²'s change-request definition against the agreed baseline, its five-step Manage Project Change process, its four decisions, the Project Change Management Plan artefact, the Change Log, and the document's CC BY 4.0 licence
Quotable: "A change request logs an appeal to amend an aspect of the agreed baseline of a project (i.e. scope, requirements, deliverables, resources, costs, timeframe or quality characteristics)."
Quotable: "A change request can be formally submitted via a Change Request Form, or can be identified and raised during meetings as a result of decisions, issues or risks, and should be documented in the Change Log."
Quotable: "The status of a change request is logged in the Change Log. It may have the following values: Submitted, Investigating, Waiting for approval, Approved, Rejected, Postponed, Merged or Implemented."
Quotable: "Change control is an activity in the PM² Change Management Process that aims to evaluate, accept or reject project changes using a Change Log. The Change Control Board (CCB) or Change Advisory Board (CAB) is a designated group of stakeholders that is responsible for reviewing, evaluating, approving or rejecting change requests for the project. In an organisation, this role may be performed by the Project Steering Committee (PSC)."
Quotable: "The Change Log is a register of project changes used for recording, assessing, monitoring, controlling and tracking change requests and respective decisions."
Quotable: "The purpose of this step is to identify and document change requests."
Quotable: "The Project Manager (PM) ensures that a Change Request is appropriately documented (i.e."
Quotable: "b) consider the impact of not implementing the proposed change, c) estimate the size of the identified change based on its impact on the project objectives, schedule, cost and effort, and d) prioritise the implementation of the change request in relation to other change requests."
Quotable: "There are four possible decisions: approve, reject, postpone or merge the change request."
Quotable: "The decision details are documented in the Change Log and communicated to the requestor."
Quotable: "For approved or merged changes, the Project Manager (PM) should incorporate all related actions into the Project Work Plan and update the related documentation and logs (i.e."
Quotable: "The purpose of this step is to monitor and control project changes so they can be easily communicated to the various project layers for approval or status updates."
Quotable: "The Project Change Management Process can be tailored and customised to a project’s needs and can be documented either in a Project Change Management Plan or in the Project Handbook."
Quotable: "© European Union, 2023 Reproduction and reuse is authorised provided the source is acknowledged. Document licensed under CC BY 4.0 license (https://creativecommons.org/licenses/by/4.0/)."

**[8] PM2 Alliance - PM2 Change Request Form template v3.0.1.** primary. **fetched-and-verified.**
`https://www.pm2.center/wp-content/uploads/2022/02/21.I.PM2-Template.v3.Change_Request_Form.ProjectName.dd-mm-yyyy.vx_.x-1.docx`
Supports: Field-level structure of the PM2 Change Request Form: header/identity fields, description fields, no decision section, explicit separation from a change log. That the request form and the change log are two artifacts, the form archived once logged.
Quotable: "Change Request Form"
Quotable: "Current Situation:"
Quotable: "Desired Situation:"
Quotable: "Impact or Risks:"
Quotable: "Out of Scope:"
Quotable: "Change ID:"
Quotable: "Once the change request is logged into the Change Log, then this form is updated with the assigned Change ID and the form is archived"

**[9] CDC Unified Process - Change Request Form (example), by Daniel Vitek, consultant to CDC NCPHI.** primary. **fetched-and-verified.**
`http://web.archive.org/web/20240601190446id_/https://www2a.cdc.gov/cdcup/library/templates/CDC_UP_Change_Request_Form_Example.doc`
Supports: Three-section field structure (Submitter / PM Analysis / CCB Decision), Type of CR offering Defect, four-state decision vocabulary including 'Approved with Conditions', and a project manager's initial analysis carrying hour, duration, schedule and cost impact fields (checked against the raw text by the main loop, 2026-09-25).
Quotable: "Hour Impact"
Quotable: "Duration Impact"
Quotable: "Schedule Impact"
Quotable: "Cost Impact"
Quotable: "1.) SUBMITTER - GENERAL INFORMATION"
Quotable: "Type of CR"
Quotable: "Enhancement"
Quotable: "Defect"
Quotable: "2.) PROJECT MANAGER - INITIAL ANALYSIS"
Quotable: "3.) CHANGE CONTROL BOARD - DECISION"
Quotable: "Approved"
Quotable: "Rejected"
Quotable: "More Info"
Quotable: "Priority"
Quotable: "Mandatory"

**[10] GSA (U.S. General Services Administration) - M3 Playbook Change Request Form Template.** primary. **fetched-and-verified.**
`https://ussm.gsa.gov/assets/files/M3-Playbook-Change-Request-Form-Template.docx`
Supports: Field structure of the Requirements Change Request Form: Type of Change offering Defect, Change Control Board decision vocabulary, and a distinct document-certification block that is not the CR decision, and estimated hours, cost, schedule and scope impact fields. Its two section headings, read from word/document.xml.
Quotable: "Requirements CHANGE REQUEST FORM"
Quotable: "Type of Change"
Quotable: "New Requirement, Change to Existing Requirement, Defect"
Quotable: "Change Control Board Approval Information"
Quotable: "Board Decision"
Quotable: "Approved, Rejected, More information"
Quotable: "MANAGEMENT CERTIFICATION"
Quotable: "Requirements Change Request Information"

**[11] HHS (U.S. Dept. of Health & Human Services) EPLC - Change Management Plan template.** primary. **fetched-and-verified.**
`http://web.archive.org/web/20260226151438id_/https://www.hhs.gov/sites/default/files/ocio/eplc/EPLC%20Archive%20Documents/07%20-%20Change%20Management%20Plan/eplc_change_management_plan_template.doc`
Supports: The change request form's field list is presented merged into the change log's data elements, plus separate priority, type, and status taxonomies with no Defect option. That it merges the request form and the log into one field list.
Quotable: "Change Request Form and Change Management Log"
Quotable: "Priority"
Quotable: "Type"
Quotable: "Status"
Quotable: "Scope"
Quotable: "Time"
Quotable: "Duration"
Quotable: "Cost"
Quotable: "Resources"
Quotable: "Deliverables"
Quotable: "Product"
Quotable: "Processes"
Quotable: "Quality"
Quotable: "Open"
Quotable: "In Review"
Quotable: "Testing"
Quotable: "Closed"
Quotable: "AT A MINIMUM, THE FOLLOWING DATA SHOULD BE INCLUDED ON THE PROJECT'S CHANGE REQUEST FORM AND CHANGE MANAGEMENT LOG"

**[12] Texas DIR (Dept. of Information Resources) - PM Essentials Project Change Request Template.** primary. **fetched-and-verified.**
`https://dir.texas.gov/sites/default/files/2021-08/PM%20Essentials%20Change%20Request%20Template_ver01%20(1).docx`
Supports: Field structure of the PCR: approval block placed above the definition fields, Approve/Reject checkbox vocabulary under a 'Recommendation' column, an Alternatives field, an Impact of Not Implementing field, a table of milestone finish dates against the original and new baseline, and the form doubling as the retained change record (the last three checked against the raw text by the main loop, 2026-09-25).
Quotable: "Impact of Not Implementing"
Quotable: "Project Change Request"
Quotable: "Recommendation"
Quotable: "Approve"
Quotable: "Reject"
Quotable: "Alternatives"
Quotable: "retained to memorialize any changes or denial of changes"

**[13] University of Iowa Health Care, Health Care Information Systems PMO - Change Request page.** practitioner. **fetched-and-verified.**
`https://hcis.healthcare.uiowa.edu/pmo/changerequest.html`
Supports: Completion guidance describing the sections a change request form should carry (project info, change description, reason, impact analysis, recommendation, supporting documentation, project updates, comments, approval/sign-off) and that the request 'will be logged and reviewed' separately.
Quotable: "Project Information"
Quotable: "Project Change Request Information"
Quotable: "Project Impact Analysis"
Quotable: "Recommendation"
Quotable: "Supporting Documentation"
Quotable: "Project Updates Required"
Quotable: "Approval and Sign Off"
Quotable: "the change request form will be logged and reviewed by the Project Core Team"

**[14] NIST, SP 800-128 "Guide for Security-Focused Configuration Management of Information Systems".** primary. **fetched-and-verified.**
`https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf`
Supports: Appendix E's sample Change Request template fields, and Appendix H's CCB Charter template sections; both are for a Configuration Control Board (CCB) governing a running information system's SecCM program, not a project baseline change board.
Quotable: "The following is a sample template for a Change Request artifact that can be used within a SecCM program."
Quotable: "1. Date Prepared: 2. Title of Change Request: 3. Change Initiator/Project Manager: 4. Change Description: 5. Change Justification: 6. Urgency of Change: {Scheduled/Urgent/Unscheduled} 7. System Components/CIs to be Changed: 8. Other System Components, CIs, or Systems to Be Affected by Change: 9. Personnel involved with the Change: 10. Expected Security Impact of Change: 11. Expected Functional Impact of Change: 12. Expected Impact of Not Doing Change: 13. Potential Interface/Integration Issues: 14. Required Changes to Existing Applications: 15. Project work plan including change implementation date, deliverables, and back-out plan: 16. Funding Required to Implement Change:"
Quotable: "Change Approved/Disapproved (include justification and/or further action to be taken if disapproved): Authorized Signature(s):"
Quotable: "The following is a sample template for a CCB charter that can be used within a SecCM program."
Quotable: "PURPOSE ... "The Configuration Control Board (CCB) represents the interests of program and project management by ensuring that a structured process is used to consider proposed changes and incorporate them into a specified release of a product. The CCB shall request that impact analysis of proposed changes be performed, review change requests, make decisions, and communicate decisions made to affected groups and individuals.""
Quotable: "SCOPE OF AUTHORITY ... This scope boundary separates decisions that this CCB can make from those that it must escalate to a higher-level CCB or manager for resolution."
Quotable: "MEMBERSHIP ... The CCB typically includes representatives from program management, project management, software engineering, hardware engineering, testing, documentation, customer support, and marketing. One individual is designated as the CCB Chair."
Quotable: "DECISION-MAKING PROCESS ... Indicate whether voting, consensus, unanimity, delegation to a specific individual, or some other decision rule is used to make decisions. State whether the CCB Chair or another manager is permitted to overrule the CCB's collective decision."
Quotable: "Configuration Control Board (CCB) - Establishment of and charter for a group of qualified people with responsibility for the process of controlling and approving changes throughout the development and operational lifecycle of products and systems; may also be referred to as a change control board;"

**[15] NIST, SP 800-53 Rev. 5 "Security and Privacy Controls for Information Systems and Organizations", control CM-3 (Configuration Change Control).** primary. **fetched-and-verified.**
`https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf`
Supports: CM-3's control text and discussion define configuration change control (review, approve/disapprove, document, implement, retain records, monitor, and provide oversight through a change control element) for organizational systems, explicitly naming Configuration Control Boards / Change Advisory Boards as the review-and-approve mechanism -- this is control-system change governance, distinct from a one-time project's baseline scope change.
Quotable: "b. Review proposed configuration-controlled changes to the system and approve or disapprove such changes with explicit consideration for security and privacy impact analyses;"
Quotable: "g. Coordinate and provide oversight for configuration change control activities through [Assignment: organization-defined configuration change control element] that convenes [Selection (one or more): [Assignment: organization-defined frequency]; when [Assignment: organization-defined configuration change conditions]]."
Quotable: "Processes for managing configuration changes to systems include Configuration Control Boards or Change Advisory Boards that review and approve proposed changes."
Quotable: "For new systems or major upgrades, organizations consider including representatives from the development organizations on the Configuration Control Boards or Change Advisory Boards."

**[16] PeopleCert (copyright), "ITIL 4 Foundation Glossary", redistributed by iGEN.** vendor. **fetched-and-verified.**
`https://igen.nl/wp-content/uploads/2024/10/ITIL-4-Foundation_Glossary_Digital.pdf`
Supports: ITIL 4's terminology for change enablement: standard change, emergency change, change authority, request for change; and the confirmed absence of a 'normal change' entry.
Quotable: "emergency change A change that must be introduced as soon as possible."
Quotable: "request for change (RFC) A description of a proposed change used to initiate change enablement."
Quotable: "standard change A low-risk, pre-authorized change that is well understood and fully documented, and which can be implemented without needing additional authorization."
Quotable: "change authority A person or group responsible for authorizing a change."
Quotable: "change enablement practice The practice of ensuring that risks are properly assessed, authorizing changes to proceed and managing a change schedule in order to maximize the number of successful service and product changes."
Quotable: "change model A repeatable approach to the management of a particular type of change."

**[17] AXELOS/OGC-derived, "ITIL Glossary and Abbreviations" (ITIL 2011 edition), mirrored by Boston University IT.** vendor. **fetched-and-verified.**
`https://www.bu.edu/tech/files/2018/10/ITIL%C2%AE-glossary-and-abbreviations.pdf`
Supports: The ITIL 2011 glossary's definitions of normal change, standard change, emergency change, and change advisory board (CAB) -- the vocabulary and CAB structure that the 2019 Accelerate report's critique targets, and that ITIL 4's later glossary drops the 'normal change' term from.
Quotable: "(ITIL Service Transition) A change that is not an emergency change or a standard change. Normal changes follow the defined steps of the change management process."
Quotable: "(ITIL Service Transition) A group of people that support the assessment, prioritization, authorization and scheduling of changes. A change advisory board is usually made up of representatives from: all areas within the IT service provider; the business; and third parties such as suppliers."

**[18] Stefan Kempter / IT Process Maps, "Checklist Request for Change (RFC)", IT Process Wiki.** practitioner. **fetched-and-verified.**
`https://wiki.en.it-processmaps.com/index.php/Checklist_Request_for_Change_RFC`
Supports: A practitioner-level RFC content checklist (13 sections: unique ID, date, change owner, initiator, priority, proposed-change reference, description/business case, risks and back-out plan, time schedule, resource/cost estimate, budget, supporting documents, approval/rejection) and its statement that non-standard changes route through Change Management for CAB/ECAB approval -- again the ITSM production-service-change context, not a project's baseline change board.
Quotable: "The Request for Change (RFC) is formal request for the implementation of a Change. The RFC is a precursor to the 'Change Record' and contains all information required to approve a Change."
Quotable: "A Request for Change is to be submitted to Change Management for any non-standard Change (a set of standard/ routine Changes is usually defined by Change Management; these are minor Changes which do not require submission to the Change Management process)."
Quotable: "Person/ body in charge of the approval (Change Manager / CAB / ECAB)"
Quotable: "(e.g. "Very High (Emergency Change)", "High", "Normal", "Low" - may be overruled by Change Management during Change assessment)"

**[19] DORA (Google Cloud program), Capability guide "Streamlining change approval".** practitioner. **fetched-and-verified.**
`https://dora.dev/capabilities/streamlining-change-approval/`
Supports: DORA's current-form statement of the finding: heavyweight, externally-approved change management (CAB or senior-manager sign-off) for production/customer-facing IT service changes correlates with worse software delivery performance and no better change-fail rate; the recommended fix is peer review plus automated testing/CI/monitoring, with the CAB's role shifting to strategic facilitation rather than gatekeeping. Nowhere does this page mention project baseline change control, scope/schedule/cost baselines, or PMO governance boards -- it is scoped entirely to IT service/production changes.
Quotable: "Most IT organizations have change management processes to manage the life cycle of changes to IT services, both internal and customer-facing."
Quotable: "Change management processes often include approvals by external reviewers or change approval boards (CABs) to promote changes through the system."
Quotable: "Research by DORA, presented in the 2019 State of DevOps Report, finds that change approvals are best implemented through peer review during the development process, supplemented by automation to detect, prevent, and correct bad changes early in the software delivery life cycle."
Quotable: "Traditionally, these goals have been met through a heavyweight process involving approval by people external to the team proposing the change: a change advisory board (CAB) or a senior manager. However, DORA’s research shows that these approaches have a negative impact on software delivery performance. Further, no evidence was found to support the hypothesis that a more formal, external review process was associated with lower change fail rates."
Quotable: "In the continuous delivery paradigm the CAB still has a vital role, which includes: Facilitating notification and coordination between teams. Helping teams with process improvement work to increase their software delivery performance. Weighing in on important business decisions that require a trade-off and sign-off at higher levels of the business, such as the decision between time-to-market and business risk."
Quotable: "Reliance on a centralized Change Approval Board (CAB) to catch errors and approve changes. This approach can introduce delay and often error."
Quotable: "Do production changes need to be approved by an external body before deployment or implementation? The amount of time changes spend waiting for approval from external bodies."

**[20] Forsgren, N., Humble, J., et al. (DORA / Google Cloud), "Accelerate: State of DevOps 2019" report.** primary. **fetched-and-verified.**
`https://dora.dev/research/2019/dora-report/2019-dora-accelerate-state-of-devops-report.pdf`
Supports: The primary research behind the capability page: the study measured change approval processes for changes 'to production systems' and found the heavyweight/external-approval construct (CAB or senior-manager approval for significant changes) negatively correlated with software delivery performance, with a specific 2.6x low-performer odds ratio, and found no evidence linking formal external approval to lower change fail rates. The report frames its recommendation entirely around production release risk management, never mentions project baseline management, scope/cost/schedule change control, or PMBOK-style change control boards. The measured size of the external-approval finding. In the raw PDF text a footnote interrupts this sentence after "organization"; the words that follow it are "had this kind of formal approval process in place".
Quotable: "This can be combined with automated thresholds that bound changes."
Quotable: "Using code review to implement segregation of duties requires that all changes to production systems should be recorded in a change management system that lists the change along with the person or people who authored it, and logs authenticated approval events."
Quotable: "We found that formal change management processes that require the approval of an external body such as a change advisory board (CAB) or a senior manager for significant changes have a negative impact on software delivery performance."
Quotable: "The motivation behind the heavyweight change management processes proposed by ITSM frameworks is reducing the risk of releases. To examine this, we investigated whether a more formal approval process was associated with lower change fail rates and we found no evidence to support this hypothesis, consistent with earlier research."
Quotable: "We recommend that organizations move away from external change approval because of the negative effects on performance. Instead, organizations should "shift left" to peer review-based approval during the development process."
Quotable: "Continuous delivery offers a superior risk management approach compared to traditional change management processes, but there is still an important role for the CAB."
Quotable: "Since approving each individual change is impossible in practice in the continuous paradigm, the CAB should focus instead on helping teams with"
Quotable: "Survey respondents were 2.6 times more likely to be low performers if their organization"

**[21] Ken Schwaber and Jeff Sutherland, "The 2020 Scrum Guide" (scrumguides.org).** primary. **fetched-and-verified.**
`https://scrumguides.org/scrum-guide.html`
Supports: Change in Scrum enters through exactly one channel and one accountable person: the Product Backlog, ordered and owned by the Product Owner, not a change-request record or board. There is no artifact named a change request anywhere in the Guide.
Quotable: "A Product Owner orders the work for a complex problem into a Product Backlog."
Quotable: "Those wanting to change the Product Backlog can do so by trying to convince the Product Owner."
Quotable: "The Product Owner is one person, not a committee."
Quotable: "No changes are made that would endanger the Sprint Goal;"
Quotable: "Scope may be clarified and renegotiated with the Product Owner as more is learned."
Quotable: "Only the Product Owner has the authority to cancel the Sprint."
Quotable: "The Product Backlog may also be adjusted to meet new opportunities."
Quotable: "The Product Backlog is an emergent, ordered list of what is needed to improve the product."

**[22] Agile Manifesto authors (Beck, Beedle, van Bennekum, Cockburn, Cunningham, Fowler, et al.), "Manifesto for Agile Software Development".** primary. **fetched-and-verified.**
`https://agilemanifesto.org/`
Supports: The Manifesto's fourth value statement places responding to change above following a plan, and customer collaboration above contract negotiation, framing a formal change-control artifact as a second-best mechanism the Manifesto's own values are wary of.
Quotable: "Individuals and interactions over processes and tools"
Quotable: "Customer collaboration over contract negotiation"
Quotable: "Responding to change over following a plan"
Quotable: "That is, while there is value in the items on the right, we value the items on the left more."

**[23] Agile Alliance authors (Beck et al.), "Principles behind the Agile Manifesto" (agilemanifesto.org/principles.html).** primary. **fetched-and-verified.**
`https://agilemanifesto.org/principles.html`
Supports: The single most load-bearing sentence for a change-request bundle: agile explicitly welcomes late requirement change as a competitive weapon rather than something to gate through a control board, and names 'responding to change' via short delivery cycles and self-organizing teams as the mechanism, not a document.
Quotable: "Welcome changing requirements, even late in development. Agile processes harness change for the customer's competitive advantage."
Quotable: "Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale."
Quotable: "The best architectures, requirements, and designs emerge from self-organizing teams."
Quotable: "At regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly."

**[24] Wikipedia contributors, "Agile contracts".** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Agile_contracts`
Supports: Names the contract families that formalize where change enters an agile engagement outside a single team's Product Backlog: capped time-and-materials, target-cost, and incremental-delivery contracts, each with its own change/exit mechanism (risk share, checkpoint phase, exit points). Note: this schema's tier enum has no 'reference' slot; the pipeline's own tier vocabulary (bundle-pipeline.md) lists 'reference' as legal and Wikipedia would normally sit there. It is filed here as 'practitioner' only because the enum forces a choice; the synthesizer should re-tier it 'reference' in the research log.
Quotable: "The Agile fixed price is a contractual model agreed upon by suppliers and customers of IT projects that develop software using Agile methods. The model introduces an initial test phase after which budget, due date, and the way of steering the scope within the framework is agreed upon."
Quotable: "In Agile contracts, the supplier and the customer collaboratively define their common assumptions regarding business value, implementation risks, expenses (effort), and costs."
Quotable: "Further aspects of an Agile contract are risk share (both parties divide the additional expenses for unexpected changes equally amongst themselves) or the option of either party leaving the contract at any stage (exit points)."
Quotable: "Incremental Delivery Contracts allow customers to review contracts at designated points in the contract life cycle. These points are negotiated into contracts and allow customers to make changes, continue, or terminate the project."
Quotable: "In contrast to traditional fixed-price projects, projects with an Agile contract can run out early if the customer believes to have gained the expected value through the already delivered features."

**[25] Certified Compliance Solutions / Agiletek (Tim Hughes, John Skach, J.R. Jenks, Rod Rasmussen), "Moving to Agile in an FDA Environment: An Experience Report" (Agile Alliance, 2009).** practitioner. **fetched-and-verified.**
`https://www.agilealliance.org/wp-content/uploads/2017/05/Moving-to-Agile-in-an-FDA-Environment.pdf`
Supports: In an FDA-regulated design-control environment, 'Design changes' is a named, numbered element of the mandated Design History File (QSR 820.30(i) / ISO 7.3.7), with 'Change control procedures' as its required document -- i.e., in this camp a change record survives because a regulator requires it, not because a team chooses to keep it. The same report shows agile absorbing that requirement rather than dropping it: change is managed but not eliminated, and the report's own philosophy toward paperwork is to keep only what earns its keep.
Quotable: "Design changes"
Quotable: "Change control procedures"
Quotable: "Comparing two FDA-regulated medical device projects"
Quotable: "Accommodated change"
Quotable: "Manage scope and limit feature creep"
Quotable: "Negotiate scope and tradeoffs with key stakeholders"
Quotable: "If it is not adding value, and it is not required, do not do it"
Quotable: "The design history files should contain the minimum set of documentation that satisfies the regulatory requirements"
Quotable: "It is a myth that you can predict in detail your end product requirements up-front"

**[26] Ron Jeffries, "Fixed-Everything: Agile?" (ronjeffries.com).** practitioner. **fetched-and-verified.**
`https://ronjeffries.com/articles/019-01ff/fixed-everything-agile/`
Supports: The clearest named-practitioner statement of the contested claim: fixed-price/fixed-scope contracts already contain 'change control' provisions and are not actually static, and agile's mechanisms (working software, ATDD, retrospectives) manage that variability better than the alternative rather than pretending it away. Directly quotes and rebuts Allen Holub's opposing claim that fixed-scope work cannot be done in an Agile way.
Quotable: "I hear: the real world is fixed-scope projects, how can I do that in an Agile way. You can’t. Agile exists because scope always changes as work progresses. It’s central. Fixed objectives? Sure. Fixed time? Sure. But we learn as we work. Your contract must reflect that."
Quotable: "Most such contracts, in my experience, include “change control” provisions. One of the standard tropes used between the parties to such contracts is that the vendor will build something, the buyer will object that it doesn’t meet the scope definition, they’ll argue, with the intention of the vendor being to extract more money when it is finally determined that the original scope wasn’t clear and this is a change."
Quotable: "This trick is used quite cynically by a number of famous fixed-price bidders. They bid low, fully intending to make their money on changes."
Quotable: "It was contract negotiation that got us into this mess, and even given the best change control clauses in history, it’s not going to get us out."
Quotable: "Fixed contracts are notorious for missing their deadline. Let’s face it: that’s a change."
Quotable: "OK, I’ll level with you. I think Agile works as well as anything, better than most, in such situations, and I don’t agree with what Allen said."

**[27] Jeff Sutherland, "Agile Contracts: Money for Nothing and Your Change for Free" (Scrum Log Jeff Sutherland, jeffsutherland.com, Oct 25, 2008).** practitioner. **fetched-and-verified.**
`http://jeffsutherland.com/scrum/2008/10/agile-contracts-money-for-nothing-and.html`
Supports: The primary-source text of Sutherland's actual contract clauses, found by tracing a link inside a secondary blog post rather than trusting the search-snippet paraphrase. Gives the real clause language: the customer may terminate at any Sprint boundary for 20% of remaining contract value against an 80%-scope delivery commitment (Money for Nothing), and may swap scope for equal scope at Sprint boundaries at no added cost (Change for Free) -- both conditional on sustained customer participation in the Scrum Team.
Quotable: "Clause: Early Termination (Money for Nothing)"
Quotable: "The Customer may terminate the contract at the end of any Sprint. The standard metric for termination is when the Customer perceives the cost of continuing the project is higher than the additional value received. The Customer will pay Company 20% of the remaining contract value to exercise early termination."
Quotable: "Company commits to delivering 80% of the project scope as high quality by the agreed upon delivery date. High quality is defined by the agreed upon Definition of Done."
Quotable: "This clause can only be enacted if the Customer maintains Participation in the Team Scrum during the project."
Quotable: "Clause: Change For Free"
Quotable: "If the Customer maintains Participation in Scrum Team during the entire project, Customer shall be able to make changes to the Scope without incurring any additional cost if total Scope of contracted work is not changed. New features may be added for free at Sprint boundaries if items of equal scope are removed from the contract."
Quotable: "In the event that both parties cannot mutually agree on work item estimates or that the Customer does not maintain participation in the Scrum Team, the contract shall revert to a time and materials billing."
Quotable: "Jeff Sutherland: Vendor assumes the risk of late delivery."

**[28] Boris Gloger, "Money for nothing | Change for free | Jeff Sutherland" (Scrum 4 You blog, April 2, 2008).** practitioner. **fetched-and-verified.**
`https://scrum4you.wordpress.com/2008/04/02/money-for-nothing-change-for-free-jeff-sutherland/`
Supports: Earliest dated public sighting found of the concept name and its purpose (escaping the fixed-price/fixed-date trap), naming Sutherland's collaboration with James Coplien. Contains no clause mechanics itself -- corroborated by the primary Sutherland post above and the secondary Dubbel explainer, not used alone for the 20/80 figures.
Quotable: "The other new idea of Jeff was to show the audience the way to leave the Fix Price / Fix Date trap, by follow the Money for Nothing, Change for Free escape."
Quotable: "It is a very intuitive way of convincing customers, especially people who are in charge of budget to use an agile development approach."

**[29] Richard Kronfält, "Fixed price contracts: Money for nothing, Change for free" (Scrum FTW blog, Oct 28, 2008).** practitioner. **fetched-and-verified.**
`http://scrumftw.blogspot.com/2008/10/fixed-price-contracts-money-for-nothing.html`
Supports: Nothing in this bundle directly; consulted because its outbound link led to the primary Sutherland post used above. Its own tags ('Change Control Board', 'Change Management') confirm contemporary practitioners were already framing fixed-price agile work in change-control vocabulary.

**[30] Daniel Dubbel, "Money for nothing, change for free" (INSPECT&ADAPT blog, Aug 31, 2011; German).** practitioner. **fetched-and-verified.**
`https://www.inspectandadapt.de/money-for-nothing-change-for-free/`
Supports: Independent secondary corroboration (in German) of the 20%-termination / 80%-delivery mechanics attributed to Sutherland and Coplien, translated here rather than quoted in English -- the English figures rest on the primary Sutherland post above, not on this source.
Quotable: "Bricht der Kunde die Entwicklung ab, fallen noch 20% des restlichen Vertragsbestandteils an Kosten für die Durchführung des Abbruchs und den finalen Projektabschluss an."
Quotable: "Der Dienstleister verpflichtet sich, mindestens 80% des Projektumfangs in der durch die Definition Of Done festgelegten Qualität zu liefern."

**[31] Ian Devlin, "Bugs and Change Requests" (personal blog, 8 June 2015).** practitioner. **fetched-and-verified.**
`https://iandevlin.com/blog/2015/06/opinion/bugs-and-change-requests/`
Supports: The bug-vs-change-request boundary: a bug is something wrong with delivered code that must be fixed, a change request is something new and additional that was never part of the original delivery; misclassifying one as the other causes friction because it implies the delivered work was defective.
Quotable: "For me, a bug means one thing, something is wrong with the delivered code, be it a website’s backend or frontend, and it needs to be identified and fixed."
Quotable: "Change requests however, are something different. These are things that are new and additional to what was delivered, things that you cannot have known about and therefore did’t deliver them initially."
Quotable: "But mixing up the two, i.e. reporting a change request as a bug (the opposite is less likely to happen), drives me crazy, as I feel that the person reporting it, be it a project manager or the customer, thinks that what was delivered is wrong in some way, because it doesn’t contain this new thing that they never told me about."

**[32] Designing Buildings Wiki, "Variations in construction contracts" (last edited 19 Aug 2026).** reference. **fetched-and-verified.**
`https://www.designingbuildings.co.uk/wiki/Variations_in_construction_contracts`
Supports: The construction-industry equivalent of a change request is a "variation" (also called a variation instruction, variation order, or change order): a formally instructed alteration to the contracted scope of works, requiring express contractual authority to issue, valued and time-adjusted through defined mechanisms, and a recurring source of dispute when scope, valuation, or whether a variation occurred at all is contested.
Quotable: "In the construction industry, a variation (sometimes referred to as a variation instruction, variation order or change order), is an alteration to the scope of works, in the form of an addition, substitution or omission, from the works described in the contract."
Quotable: "No power to order variation is implied, and so there must be express terms in contracts which gives the power to instruct variations. In the absence of such express terms the contractor may reject instructions for variations without any legal consequences."
Quotable: "Change can be a source of conflict, either because the client does not believe that a change has been instructed, the work instructed is unreasonable or undeliverable, the valuation of the changes is disputed and so on."
Quotable: "Variations are often sources of dispute, either in valuing the variation, or agreeing whether part of the works constitute a variation at all, and can cost a lot of time and money during the course of a contract."

**[33] Wikipedia, "Engineering change order".** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Engineering_change_order`
Supports: The manufacturing/hardware-engineering equivalent of a change request is the Engineering Change Order (ECO, also ECN/EC/ERN): a formally approved document authorizing an already-designed product's configuration to be altered, distinct from a change request in that it presumes an approved baseline configuration under formal configuration control, names required contents (what changes, why, before/after description, affected documents/departments, approval, and timing of introduction), and in chip design has a specialized meaning (post-synthesis or post-mask logic edits) and a telecom-industry cousin, the Product Change Notice (PCN).
Quotable: "An engineering change order (ECO), also called an engineering change notice (ECN), engineering change (EC), or engineering release notice (ERN), is an artifact used to implement changes to components or end products. The ECO is utilized to control and coordinate changes to product designs that evolve over time."
Quotable: "An ECO is defined as "[A] document approved by the design activity that describes and authorizes the implementation of an engineering change to the product and its approved configuration documentation"."
Quotable: "An ECO must contain at least this information"
Quotable: "Identification of what needs to be changed..."
Quotable: "Reason(s) for the change."
Quotable: "Description of the change..."
Quotable: "List of documents and departments affected by the change..."
Quotable: "Approval of the change..."
Quotable: "The telecommunications industry has a formal process that takes elements of the ECO and other considerations and combines them into the "product change notice" (PCN)."

**[34] S. Bradner, RFC 2026, "The Internet Standards Process -- Revision 3" (IETF, October 1996).** primary. **fetched-and-verified.**
`https://datatracker.ietf.org/doc/html/rfc2026`
Supports: Confirms the name collision the bundle must disambiguate: in the IETF's vocabulary "RFC" means "Request for Comments," the archival document series (drafts, standards-track specifications, BCPs like this one) through which the Internet community publishes and discusses protocol specifications -- an entirely different artifact from ITIL's "RFC" (Request for Change), even though both compress to the identical three-letter acronym.
Quotable: "This memo documents the process used by the Internet community for the standardization of protocols and procedures."
Quotable: "Each distinct version of an Internet standards-related specification is published as part of the "Request for Comments" (RFC) document series. This archival series is the official publication channel for Internet standards documents and other publications of the IESG, IAB, and Internet community."
Quotable: "The RFC series of documents on networking began in 1969 as part of the original ARPA wide-area networking (ARPANET) project."

**[35] Richard Larson & Elizabeth Larson, "Top Five Causes of Scope Creep... and What to Do About Them" (PMI Global Congress 2009 -- North America; PMI conference paper library).** practitioner. **fetched-and-verified.**
`https://www.pmi.org/learning/library/top-five-causes-scope-creep-6675`
Supports: The scope-creep failure mode: scope creep is defined as unauthorized expansion of scope, distinguished from legitimate change by whether it went through authorization; one of the paper's five named root causes, "Scope and Requirements Not Managed," is fixed by including a formal change-management process in the scope management plan and following it -- i.e., scope creep is what happens when change bypasses (or there is no) documented change-request/change-control discipline.
Quotable: "Scope creep: Adding additional features or functions of a new product, requirements, or work that is not authorized (i.e., beyond the agreed-upon scope)."
Quotable: "The key part is whether changes are authorized or not. If an expansion of scope is approved, then it is not scope creep."
Quotable: "Scope and Requirements Not Managed Solutions: Project managers: Include a change management process in the scope management plan and follow them both Business analysts: Create a requirements management plan to be included in the overall scope management plan and follow it, including the use of requirements traceability."

**[36] Sophie Danby (InvGate), "Change Advisory Board Best Practices: 15+ Industry Leaders Weigh In" (InvGate blog, 27 October 2022), quoting named ITSM practitioners Kevin Holland, Barclay Rae, and Ken Wendle.** practitioner. **fetched-and-verified.**
`https://blog.invgate.com/do-we-still-need-the-change-advisory-board`
Supports: The change-control-board-as-bottleneck/rubber-stamp failure mode, sourced to a named practitioner rather than an unattributed vendor claim: ITSM/SIAM consultant Kevin Holland's on-the-record view that the CAB (change advisory board, ITIL's standing review body for change requests) belongs in history because it constrained agility, and consultant Barclay Rae's corroborating note that a 'kill the CAB' sentiment exists among teams frustrated with the board.
Quotable: "You never need a CAB as described in ITIL. Ask the development community what they think about CABs! CABs belong in history as an example of how ITSM put a straightjacket around agility and innovation."
Quotable: "The 'kill the cab' lobby was symbolic, but most organizations and sensible teams still need to meet and support change and assess risk, impact, etc."
Quotable: "In the DevOps world, it is considered wrong that a bunch of people in a room offering their considered opinion on a change could ever be as effective as a resilient toolchain with inherent safety checks."

**[37] Valerio Pianella, "PM Tales #29: The Decisions We Didn't Make" (personal blog, 30 June 2026).** practitioner. **fetched-and-verified.**
`https://www.valeriopianella.it/pm-tales/pm-tales-29-the-decisions-we-didnt-make/`
Supports: The failure mode of change requests (named explicitly, alongside risks, issues, and dependencies) that never receive a decision: the article names this 'decision debt,' the accumulated cost of choices postponed or blurred rather than made, and argues a postponed decision is not neutral because everyone downstream (team, supplier, customer) waits with it while the cost compounds silently.
Quotable: "In project management, we are very good at tracking visible things. Budget. Milestones. Risks. Issues. Deliverables. Dependencies. Change requests. ... But there is one thing we often track poorly: the cost of decisions not made."
Quotable: "A postponed decision looks harmless at first. It does not explode. It does not send an error message. It does not turn red in the dashboard immediately. It simply waits. And while it waits, everyone else waits with it."
Quotable: "Decision debt is the accumulated cost of choices postponed, avoided, blurred, delegated upward, or hidden behind fake alignment."

**[38] Float (float.com), "How to Manage a Change Request Without Derailing Projects" (Float resource/blog, 6 September 2024, no named individual author -- corporate byline).** vendor. **fetched-and-verified.**
`https://www.float.com/resources/manage-change-request`
Supports: A second, weaker (vendor-tier, unattributed) source corroborating the same failure mode Pianella names: change requests left in an undecided 'pending or purgatory status' erode team confidence, and the fix is to make a timely, clear decision rather than let the request idle.
Quotable: "Make decisions about them, tell everyone involved about the change, and get to work!"
Quotable: "Being clear and timely about decisions regarding change requests will build confidence across the team that things are being worked out and managed well."

**[39] PM Majik (PMO-focused practitioner blog) - "Impact assessment of project change requests".** practitioner. **fetched-and-verified.**
`https://www.pmmajik.com/impact-assessment-of-project-change-requests/`
Supports: Naming 'impact of not making the change' as its own required field, distinct from impact-of-making-it; naming a 'change deadline' field; naming impact 'external to project' as a category; and an explicit ethical caution against overstating impact/urgency to manufacture approval.
Quotable: "Impact of not making change"
Quotable: "In order to make an informed decision, you should include details of the consequence of not accepting the change."
Quotable: "For example, if not including the requested change means that an audit point cannot be closed, the sponsor and stakeholders need to fully understand that they accept the consequence of this by not approving the change."
Quotable: "When considering the change, you should include the deadline by when a decision is required on the change request and, if known, the date the change should be implemented."
Quotable: "When capturing the impact of not making the change and the deadline, do not over state the impact in an attempt to gain approval."
Quotable: "If the sponsor realises this, 1. they will not be happy and 2. they will not trust future requests."
Quotable: "It is possible to have a change that does not impact or even assists the project. However, it could have an adverse impact on an external project."

**[40] kiolo (product blog, editorial) - "Project Change Request Template: Scope, Impact and Approval".** vendor. **fetched-and-verified.**
`https://kiolo.com/en/blog/project-change-request-template/`
Supports: The richest single source found for gap elements: the no-change option, explicit out-of-scope boundaries, conditions of approval with owner/deadline, distinguishing risk of making vs. declining, separating underlying need from requester's preferred fix, reversibility/exit cost, a decision log capturing who/authority/options/evidence/dissent, treating rejection as not closing the underlying need, tracking cumulative change, and not collapsing multiple approval authorities into one status.
Quotable: "Write the current condition, evidence and consequence before proposing a solution. Separate the underlying need from the requester's preferred implementation."
Quotable: "Define what will be added, removed or modified and what remains explicitly out of scope."
Quotable: "Update the risk register template for changed exposure, including implementation and transition risk. Distinguish the risk of making the change from the risk of declining or delaying it."
Quotable: "Record residual uncertainty and conditions. Approval with conditions must identify the owner and deadline for each condition; otherwise it is too easy to treat conditional authority as unconditional."
Quotable: "Include the no-change option plus realistic alternatives. Compare each against the same dimensions: objective fit, time, cost, resources, benefits, risk, reversibility and operational burden."
Quotable: "Include reversibility and exit cost. A pilot, phased release or time-limited approval may reduce uncertainty, but only if success, stop and rollback criteria are defined."
Quotable: "Capture the final choice in a decision log when the project maintains one. Record who decided, their authority, options considered, evidence, dissent or conditions where appropriate, and review date."
Quotable: "A sound record lets an authorized reviewer reconstruct the prior baseline, requested difference, evidence, options, authority, implementation and result. That traceability is more important than making every request look favorable."
Quotable: "Resolve conflicting approvals through the governance model. ... Record each authority's decision and conditions; do not collapse them into an overall green status before every mandatory approval is satisfied."
Quotable: "Rejection of one proposed solution does not remove the underlying need, risk or contractual question. Transfer any continuing item to the correct owned record, state the next trigger and notify the requester."
Quotable: "Monitor cumulative change, not only individual requests. Several small approvals can collectively alter the business case, delivery date or operating model beyond original tolerance."
Quotable: "State urgency with a concrete latest useful decision date and consequence of delay. "Executive request" or "urgent" does not replace analysis or establish authority."
Quotable: "OPTIONS AND DECISION"
Quotable: "Options, including no change:"
Quotable: "Recommendation and rationale:"

**[41] Onplana (PM software vendor blog) - "What a Change Control Board Should Actually Do".** vendor. **fetched-and-verified.**
`https://onplana.com/blog/change-control-board-that-works`
Supports: A named three-artifact submission standard (impact statement, recommendation-with-rationale-and-conditions, decision deadline); the point that a recommendation must state a specific option and does not have to be 'approve'; decision-log discipline (owner + date per approved item, no verbal approvals); and a named failure mode ('the oracle') where approvals are made without accountability for consequences.
Quotable: "Every change request submitted to a CCB needs exactly three artifacts. ... Artifact 1: Impact statement. ... Artifact 2: Recommendation. ... Artifact 3: Decision deadline."
Quotable: "A recommendation states a specific decision option (approve, reject, defer to phase 2, or approve with modified scope), a rationale in two to three sentences, and any conditions on approval. The recommendation does not have to be "approve.""
Quotable: "A change request without a deadline gives the board permission to defer indefinitely. Most CCB deferral patterns trace back to this single omission."
Quotable: "After each meeting, the decision log is updated and circulated within 24 hours. Every approved change gets an owner and a date. Every rejected change gets a formal rationale the sponsor can review. No verbal approvals, no implied consent from silence."
Quotable: "The oracle. The board approves changes but does not own their consequences. ... The board approved without establishing accountability, so there is no feedback loop between the board's decisions and the project's outcomes."
Quotable: "Decision reversal rate is the secondary indicator. Approved changes that get reversed within one project cycle (because conditions were not properly evaluated) indicate the recommendation artifact is missing or ignored."

**[42] Wikipedia - "Change management (engineering)".** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Change_management_(engineering)`
Supports: A CHANGE REQUEST document is defined as describing 'why it is important' (not just what), carries a 'go/no-go decision' as an attribute, and closes into a CHANGE LOG ENTRY as the traceable record; and a real-world consequence example (Flixborough) of an undocumented, unassessed change causing a disaster, grounding why traceability/documentation is a distinguishing property rather than paperwork.
Quotable: "Document that describes the requested change and why it is important; ..."
Quotable: "is the change going to be executed or not?"
Quotable: "Distinct entry in the collection of all changes (e.g."
Quotable: "The change had not been properly thought out, documented and risk-assessed, so that the event of breach of containment had not been identified."
Quotable: "Besides just 'changes', one can also distinguish deviations and waivers. ... These two approaches can be viewed as minimalistic change request management (i.e. no real solution to the problem at hand)."

**[43] StakeholderMap.com (Tam M., project-templates library) - "Change Request Template".** practitioner. **fetched-and-verified.**
`https://www.stakeholdermap.com/project-templates/change-request-template.html`
Supports: A widely-distributed free template that DOES include 'options considered' and per-option impact and a stated rationale for the chosen option - useful as a mid-point baseline between the naive minimum and the fuller kiolo/onplana artifact sets.
Quotable: "Options considered to implement the change"
Quotable: "Document the options that have been considered and reviewed by the team."
Quotable: "Impact of each option (Cost, Scope, Schedule, Quality)"
Quotable: "For each option, explain the impact on Cost, Scope, Schedule and Quality."
Quotable: "Explain which option has been chosen and why."

**[44] PM Study Circle (Fahad Usmani, PMP) - "Understanding Change Request: How to Manage Scope Changes".** practitioner. **fetched-and-verified.**
`https://pmstudycircle.com/change-request/`
Supports: The naive baseline itself: a widely-read PMP-prep blog's list of what a change request 'should include' is requestor/date, description, reason, impact analysis, proposed resolution, and an approval-signature block - none of which is a no-change option, an out-of-scope statement, approval conditions, a decision deadline, or a post-decision traceability record. Used as the contrast case, not as a source of gap elements.
Quotable: "Your request should include: Requestor and date. ... Description of the change. ... Reason for the change. ... Impact analysis. ... Proposed resolution. ... Approval section."
Quotable: "After assessing these factors, decide whether to approve, reject, or defer the request. Document your decision and communicate it clearly."

**[45] Tallyfy (Amit Kothari, CEO) - "How to manage change requests without the chaos".** vendor. **fetched-and-verified.**
`https://tallyfy.com/change-request/`
Supports: A second naive-baseline data point: a five-step process (document, assess scope impact, evaluate priority, approve/reject, update and communicate) that never names a no-change option, an out-of-scope statement, approval conditions, or a decision deadline, though it does gesture at an 'audit trail' for who-approved-what.
Quotable: "The three questions that matter for any change request: What's the change? What's the benefit? How important is it relative to everything else?"
Quotable: "Tallyfy was built around this exact insight: every approval has a clear owner, a deadline, and a complete audit trail. No more guessing who approved what and when."

**[46] DeeProjectManager (Tuyota Manuwa) - "Understanding the Role of a Change Control Board in Project Management".** practitioner. **fetched-and-verified.**
`https://deeprojectmanager.com/change-control-board/`
Supports: Governance-layer corroboration that documented rationale, an audit trail, and monitoring of implementation (not just the approve/reject moment) are named CCB best practices and that their absence is a named failure mode ('poor tracking and documentation').
Quotable: "Document all CCB Decisions: To maintain visibility, all CCB change decisions must be properly documented with context and rationale."
Quotable: "Institute formal documentation practices for CCB decisions, meeting minutes, and change logs. Maintain an audit trail."
Quotable: "Poor Tracking and Documentation: Without proper record-keeping, decisions can get lost leading to misalignment."
Quotable: "Not Monitoring Implementation: The CCB cannot assess effectiveness without monitoring the execution of approved changes."

**[47] ROSEMET (Alvin Villanueva, PMP) - "Understanding Alternative Analysis: A Project Manager's Guide to Smarter Decision-Making".** practitioner. **fetched-and-verified.**
`https://www.rosemet.com/project-management-alternative-analysis/`
Supports: General confirmation that structured alternatives comparison (not a single proposed fix) is a recognized PM technique explicitly applied to change management, independent of any one template's wording. Weak/tangential: the article is about alternative analysis generally, not change requests specifically, and does not itself describe a change-request document.
Quotable: "Change Management - Weighing different ways to implement change with minimal disruption"

**[48] Prairie View A&M University, Information Technology Services Change Management Request Form (2010, modified 2013).** primary. **fetched-and-verified.**
`https://www.pvamu.edu/its/wp-content/uploads/sites/46/change-management-request-form_fill.pdf`
Supports: A university IT change form in the IT service lineage, carrying a rollback description and a change control committee sign-off: the neighbour's fields, which this bundle does not template.
Quotable: "Rollback Description"
Quotable: "Change Control Committee Sign off"
