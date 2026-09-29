# change-log: research log

Research conducted 2026-09-28, building on an admission sweep run on 2026-09-27 while the spec was written (five
candidate types, one of them this one). The build's six-dimension fan-out covered definitions and names, published
change logs field by field, the neighbours that share the name, keeping the log, where a log earns its keep and where
it does not, and the standing gap question. **40 sources are recorded below, all fetched-and-verified.** Only
`fetched-and-verified` sources are quoted anywhere in this bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a retrieval tool
returns. Pages were read as downloaded (HTML decoded as UTF-8, PDFs through `pdftotext` without `-layout`,
spreadsheets from their cells, 1997-format `.doc` and `.xls` files through `antiword` and a cell reader), and each
quotation was searched for as a normalized substring. Of 139 quotations the build's agents returned, 129 passed as
returned. Of the other ten, six are verbatim on the rendered page and failed only because an inline link or an HTML
entity sits inside the sentence in the raw download; two fused a heading onto the paragraph beneath it and survive as
the paragraph alone; one wraps a table cell and was dropped; and one is verbatim but was dropped because it is an
author's claim about a PMBOK edition this research did not read. Five passing quotations were changed where an
elision, a duplicate or a PDF glyph made them misleading (two cut, three trimmed or restored in full), and ten
quotations were added from the main loop's own checks. **145
quotations remain, and every one passes.**

---

## What the checks caught, and what was not read

**The source cache was corrupting sources on this machine, and the fix ships with this bundle.** On Windows,
`tools/source-cache.py get` crashed on any cached page holding a character outside cp1252 and exited 1, the code that
means "not cached", so an agent re-fetched pages it already had. A `put` from standard input had the mirror fault and
stored text garbled: [3] and [4], the two APM pages, carried 2,090 garbled sequences between them and were repaired
before this build read them, keeping their original fetch dates. [13], the UCOP template, held the spreadsheet's raw
bytes rather than its text; the research agent that owns it re-fetched and parsed it.

**Two agents' findings, and one line of the spec, were corrected by another dimension's source.** The keeping-the-log dimension reported that no source
names a Change Manager as the log's keeper; [12] does ("The Change Manager enters the CR into the CR Log."), and [13]
names a Change Request Coordinator. The neighbours dimension reported that no read source states the boundary between
a decision log and a change log; [28] does, though it is one practitioner, read from a free preview. The spec placed
PM²'s Target Delivery Date in the Change Approval group; [7] places it in Change Assessment and Action.

**The spec misnamed APM's two glossary entries.** "A record of all proposed changes to scope." is the entry "Change
register (or log)", and the entry "Change log" reads "A record of all project changes: proposed, authorised, rejected
or deferred." ([3]). The landing corrects `tier2-specs.md` accordingly.

**Two published sources disagree with themselves.** [7] lists the change log's statuses once with "Investigating" and
once, in Appendix B.7 itself, with "Assessing". [11]'s instructions say of Priority "Valid options include the
following: High, Medium, Low." and then define a fourth value, Critical.

**One published log is another's copy.** [14], San Francisco State University's template, repeats [11]'s fifteen
columns, drop-down values and instructions nearly word for word. It is counted as evidence that the federal template
travels, not as a sixth independent design.

**The HHS files were read from the Internet Archive.** hhs.gov refuses scripted requests with HTTP 403. [11], [12],
[26] and [27] were requested as `https://web.archive.org/web/2025id_/` followed by the hhs.gov address; each request
resolved to a capture taken on 26 February 2026, and each entry cites that capture's own address. [12]'s capture is
the one `change-request`'s research log already cites. One sentence in [12] wraps a table cell and is usable only as its
fragment "A submitter completes a CR Form and sends the".

**Not read, and nothing in this bundle may rest on them:**

- **The PMBOK Guide itself**, sixth or eighth edition. Only its openly hosted errata [1] was read. [28] makes a claim
  about PMBOK 8; it was dropped.
- **ISO 21502:2020**, a paid standard, and **AXELOS's PRINCE2 manual**. PRINCE2 is read through prince2.wiki ([5], [6]),
  practitioner tier.
- **The CDC Unified Process newsletter**, which the spec already set aside (HTTP 403, not recovered).
- **Wikipedia's "Changelog" article**, not retrieved; the software-changelog boundary rests on [15] alone.
- **The University of Illinois PPMO change request log, the FFIEC IT Examination Handbook, the UK Model Services
  Contract's change control schedule, a University of Michigan change log and audit trail page, and a Digital Project
  Manager decision-log page**, each blocked by a bot challenge or HTTP 403.
- **The paywalled part of [28]**, including a section its outline titles as what turns a log into a graveyard.
- **Vendor pages that title a template "Change Control Log"** (ProjectManagement.com, the Institute of Project
  Management and others), seen only as search-result titles.
- **Review-cadence figures** ("weekly 30-minute meetings" and similar) that a search tool's summary attributed to
  vendor pages nobody read. None may appear in this bundle.

---

## The admission record

**ADR 0048's bar is met by five named bodies.** [1] PMI: "The change log is used to record all submitted change
requests." [3] APM: "A record of all project changes: proposed, authorised, rejected or deferred." [7] the European
Commission's PM²: "A Change Log is used to document, monitor and control all project changes (see Appendix B)." and a
17-field template in Appendix B.7. [10] Connecticut DSS ships an 11-column log, "Also known as Project Change Register".
[26] HHS: "All projects, regardless of type or size, should maintain a change log and regularly manage requested
changes." with a 15-column log [11]. [13] UCOP ships a seven-column change request log.

**[7] is licensed CC BY 4.0** ("Document licensed under CC BY 4.0 license") **and is the only source whose wording this
bundle may adapt.** The public-sector templates state no licence and are structure evidence.

**PRINCE2 is the named exception** ([5]): requests for change are one of its issue types, "Issues must be recorded in
the issue register", and a change log appears only as an alternative place to record the decision ("should be
documented in the issue register or change log.").

**The family is `governance-docs`, by
[ADR 0061](../../docs/internal/decisions/0061-change-log-joins-governance-docs-as-a-fifth-member.md).**

---

## Claims flagged contested or time-bound

1. **Is the request one document with the log, or two?** Two in [7] (the log ships as its own artifact, [8]: "This
   template is part of the Monitor & Control Logs.") and [13] ("Transfer the Date of Request, Change Request #, Change
   Request Title, the resource assigned to the change request, the description of the change requested, current
   status and implementation date from the change request form for each specific change request."). [12] defines one
   shared list of data elements for both ("LIST AND DEFINE THE DATA ELEMENTS THE PROJECT TEAM NEEDS TO INCLUDE ON THE
   CHANGE REQUEST FORM AND IN THE CHANGE MANAGEMENT LOG.") yet keeps two artifacts and a separate logging step ("The
   Change Manager enters the CR into the CR Log."). [10] does not say whether a form feeds it. **This bundle follows
   the two-document convention, and it does not describe HHS as merging them.**
2. **Is the decision a status?** Only [7] keeps them apart: a Status field, and a Decision field with "four possible
   decisions: approve, reject, postpone or merge the change request." [10], [11] and [13] carry status alone, and [11]'s
   "Closed" is explicitly ambiguous: "The change request is no longer considered an active project threat and can be
   closed with or without resolution." **This bundle keeps Decision distinct from Status, following [7], and says so as
   a choice.**
3. **What the log covers.** [3] carries two entries: the change log records "all project changes: proposed, authorised,
   rejected or deferred", and the change register (or log) records "all proposed changes to scope". **This bundle takes
   the first, broader sense**, the one [1] and [7] share.
4. **Which statuses.** [7] offers eight, and names one of them two ways (see above). [10] offers seven: "Submitted, In
   Review, Approved, Denied, Deferred, Withdrawn, or Closed." [11] offers three core values and three optional ones;
   [12] a different five. [12] leaves the choice to the project ("THE LIST OF ELEMENTS IS AT THE DISCRETION OF THE
   PROJECT MANAGER."). **No source claims its list is universal.**
5. **Does work without a fixed baseline need one?** [31] routes change through one person ("Those wanting to change the
   Product Backlog can do so by trying to convince the Product Owner.") and has no change-log vocabulary at all; [35]
   rejects standing lists outright ("Backlogs are a big weight we don't need to carry."), though its subject is the
   backlog, not a change log. Against that, [33] requires a documented adjustment when a fixed-price contract changes,
   and [34] requires "the identification, documentation, validation or where appropriate verification, review, and
   approval of design changes before their implementation." **The split is by whether an agreed baseline exists, not a
   disagreement within one context; the companion reports both.**
6. **What DORA's finding is about.** [32] concerns approval of production changes by an external body ("no evidence
   was found to support the hypothesis that a more formal, external review process was associated with lower change
   fail rates"). **It never mentions a project baseline or a change log, and this bundle must not apply it to one.**
7. **Who keeps the log.** [12]: the Change Manager enters requests and assigns their numbers ("Assigned by the Change
   Manager"). [13]: "The Change Request Coordinator is responsible for maintaining the Change Request Log on behalf of the
   Change Management Lead." [29]: "The project manager is responsible to monitor the change process from the very
   beginning to the very end." **No source separates the person who decides from the person who writes the row as a
   rule; the template asks for a named keeper and leaves the title to the team.**
8. **How often it is reviewed.** One figure is sourced: [26], "at least weekly for even the simplest projects", and it
   concerns reviewing change requests, not the log as an artifact. [30] says only "Regularly review the implementation
   of approved changes". **Any other cadence is the team's choice, and the template must not suggest one as practice.**
9. **The decision log boundary rests on one practitioner.** [28]: "A decision log tracks what was decided. A Change
   Control Log tracks what changed, why it changed, who approved it, and what the impact was on the baseline." [7] keeps
   a separate Decision Log beside the Change Log and links the two through the Traceability and Comments field. No
   standards body states the boundary in a read source; the companion attributes it to [28] by name.

---

## Notes for the companion

**The honest framing.** The definition is settled: PMI [1], APM [3] and PM² [7] all describe a cumulative register of
every submitted change request and its disposition, and five public bodies ship one. What varies is everything a log
needs in order to govern rather than narrate: whether the decision is recorded apart from the status, whether
escalation is a field, whether planned and actual dates are kept apart, and whether a row links to anything. The name
also collides twice: with the software changelog [15], and with ITIL's narrower Change Record and Change Schedule [16].
PRINCE2 [5] keeps the whole function in its issue register, by design.

**The evidentiary spine, in the order it should be used:**

- **Definition:** [1], [3], [7], [26], quoted above; [4] places the log as the first step of change control ("Log change
  request in a change register (or log).").
- **Published structure:** [7]'s four groups and seventeen fields; [10]; [11] (with [14] as its copy); [12]'s shared
  data elements; [13].
- **The authority:** [6] ("The change authority is a person or group to whom the project board may delegate
  responsibility for reviewing and approving change requests or off-specifications."), [26]'s threshold example ("a
  project manager (PM) may be authorized to personally approve changes with a project impact of less than $5,000"),
  [7]'s escalation field ("Escalation to the Directing or Steering layer is needed? (Yes or No).").
- **Keeping it:** [26] ("Unique Entries - Each change request should be recorded as a single line item. Do not combine
  multiple requests under one change request ID."), [27] ("Update the Change Management Log."), [12], [13], [29].
- **Where it earns its keep:** [31], [35], [33], [34], [28].
- **The neighbours:** [15], [16], [17], [18], [19]; [32] bounded as above.

**How it fails, as sourced, and nothing more:**

- **Decisions made and never written down.** [28]: "Changes happen. Decisions get made informally. Nobody writes it
  down. And eventually, the project is living in a reality that the plan never accounted for and nobody officially
  approved." One practitioner, and the companion says so.
- **A date that records the wrong event.** [39], an Inspector General's review of a real change-order system: "the
  approval date in eBuilder represents the date that the staff finalized the approval process for a change order and
  not the Governing Boards authorization date." The source is construction change orders, not a project change log;
  cite it as an auditor's finding about a change register, by analogy.
- **Drift that no single row shows.** [37] describes the register as showing "the additional time/cost/scope that has
  been approved since the project scope was first agreed"; [39] computed approved change as a percentage of the
  original contract; [40] gives a practitioner's illustration ("By week eight, the cumulative impact of those small
  changes had shifted the schedule by two weeks."), which is an illustration, not a measurement.
- **A rejected request that comes back.** [40]: keeping rejected requests "prevents the same request from being
  resubmitted without understanding why it was declined." Vendor tier.

**What this bundle must not say:** that DORA's finding applies to project change logs; that ITIL defines a change log;
that HHS merges the request and the log; that a Change Manager is the standard keeper; any review cadence other than
[26]'s; that change logs commonly fail in any stated way, since nothing measured a frequency; anything about PMBOK 7 or
8; and anything from the vendor "Change Control Log" pages seen only as titles.

**The section design, as the research moved it from the spec.** Four sections in lean, three more in full:

- **Purpose and Boundary** (lean): which baseline or baselines the log tracks, by artifact and version, and what does
  not go in. The first line names the software-changelog collision ([15]) and PRINCE2's issue-register alternative ([5]).
- **Status Vocabulary** (lean): the status values and the decision values, stated once. Offer [7]'s as the sourced
  default (CC BY 4.0), name [10]'s and [11]'s as alternatives, and say plainly that a team adapts them ([12]). **Keep
  Decision distinct from Status** (contested item 2).
- **Change Log** (lean, the load-bearing table): one row per request ([26]), and **no row is ever deleted**, including
  rejected, withdrawn and postponed ones ([3]'s "proposed, authorised, rejected or deferred"; [10]'s Withdrawn and
  Deferred; [40]). The core that three or more published logs share is identifier, description, date raised and
  status; four of the five carry requester and priority. The research adds **the baseline each request would change,
  by artifact and version** ([12]'s Product and Version elements: "The product version that the suggested change is
  for"), and **the decision with its reason** ([11]'s "Final Resolution & Rationale", [10]'s Resolution/Comments column,
  [40]). Decided by and decision date belong in lean. The table may be narrower in lean than in full.
- **Authority and Escalation** (lean; the spec's "Escalation", renamed because its sources are about authority): who
  may decide which changes, and when a change goes above them ([6], [26]'s threshold, [7]'s escalation field, [11]'s
  "Escalation Required (Y/N)" column). GAO's audit criteria [36] ("A rebaselining policy should identify the authority
  who decides whether the rebaselining is warranted") transfer by analogy only; the source audits rebaselining
  policies.
- **Implementation and Traceability** (full): the target date and the actual date, kept apart from the decision date
  ([7]: "The target date for the change to be delivered." and "The date on which the change was actually delivered.";
  [11]'s Expected and Actual Resolution Dates; [40]; [39]); what was updated and to which version; and links to the
  change request document and to related issues, risks and decisions ([7]: "The ID(s) of the tasks (in the Project
  Work Plan) that implement the change, and/or the IDs of related issues, risks or decisions."; [11]'s Assoc ID).
  [7]'s Implemented status is the sourced close ("the work implementing this change has been incorporated into the
  Project Work Plan"), and [29]'s "Date Request Integrated into Project Plan" column is a second.
- **Cumulative Effect** (full; **new, from the gap question**): the running total of approved change against the
  baseline as first agreed ([37], [39], [40]). It passes decision procedure 12: E1 on [37], a named source describing
  the register as carrying exactly this; E3 because the total is computed from this log's own rows; E4 as full only.
- **Review and Ownership** (full): the named keeper (contested item 7), the review cadence ([26] only), and closing
  each approved row against its baseline. **Anything beyond [7]'s Implemented status and [29]'s integration column,
  such as a periodic reconciliation duty, is the library's POSITION and must be labelled so.**

Candidates from the gap question that go to the guide's rubric rather than the template: a rejected row carries its
reason; each date names the event it records ([39]); the approving authority is named, not implied ([36], [37]'s
"Ensure that the owner or originator of the change signs off on the impact assessment."); and the log is watched for
patterns across rows ([37]: "more seasoned projects managers will be looking for patterns of change to identify
trends", a typo in the source).

**Teaching points the templates, guide and example must stay consistent with:**

- **The request is not the log.** A change request is one document; the log is the register with one row for it ([1],
  [4], [7], [13]).
- **Every request gets a row, and no row is deleted** ([3], [10], [26], [40]).
- **A decision is not a status.** A closed row still says what was decided and why ([7], [11]).
- **Each row names the baseline it would change** ([12]).
- **Someone named decides, within a stated authority, and a change above it is escalated** ([6], [7], [26]).
- **The decision date is not the delivery date** ([7], [11], [39]).
- **Small approved changes add up, and only the log can show the total** ([37], [39]).
- **PRINCE2 keeps this in its issue register, by design, and that is not a failure** ([5]).
- **It is not the software changelog, not ITIL's change record or schedule, and not a decision log** ([15], [16],
  [28], [7]).
- **A team changing its own backlog does not need one** ([31]); a baseline that carries weight outside the team does:
  a contract ([33]), a regulator ([34]), or scope and budget a sponsor signed off ([4], [26]). A small project needs a
  small one ([28]: "It needs a lightweight log and a clear agreement between the project manager and the sponsor about
  what requires formal approval versus what can be handled directly.").

**The example.** The Reporting Platform Modernization program's change log, the change-control process that both
`change-request_example.md` and `issue-log_example.md` name without showing. It carries **one row, CR-SV-01**, exactly
as `change-request_example.md` states it: title "Scheduled Email Delivery for Saved Views"; baseline the Saved Views for
Dashboards PRD, version 0.3.0; requested by Priya Nair (PM, Reporting), submitted 2026-07-08; decided by Marta Reyes
(Program Manager, Reporting Platform Modernization); decision **Postponed**, 2026-07-18; origin account-management
feedback, not an issue, a risk or a decision already on a program log. **Nothing was updated**: the PRD stays at 0.3.0,
no target date or release is set, and no delivery date exists. The request states no priority and no estimate, so the
row records them as not set and says why (the estimate was deliberately deferred), rather than inventing them. The
decision was within the program manager's authority, so the row is not escalated. The log states the program's
cumulative approved change to date, which is none. Its keeper is Marta Reyes, as for the program's issue log, and its
review joins the weekly workstream review the program's other logs already hold. `last_reviewed` is **2026-07-20**,
the date all four governance siblings carry. **It carries no row for ISS-11 or ISS-12** (`issue-log_example.md` says
neither raised a request) **and states no release or build number**, because the thread's numbering is already
inconsistent between `release-notes_example.md` and the runbook and postmortem examples. **The templates' GOOD and WEAK
text must use a different scenario entirely**; the build's templates agent has copied the example's scenario before.

**The pairing.** `pairs_with: []`. The one pm-skills name that suggests a match, `utility-pm-changelog-curator`, drafts
software changelog entries from git history.

**The aliases.** Keep `change register`: [3], [4] and [10] ("Also known as Project Change Register"). Keep `change
control log` on [28], practitioner tier; no public body uses it. Add `change management log` ([11], [26], [27]) and
`change request log` ([13]; [29]'s "Project Change Request Tracking Log").

**Catalog corrections for the landing:** methodology `generic`, not `PMBOK/ITIL`, since ITIL defines no change log
([16], [17]); relationships read "feeds Change Requests" and should read that the change request feeds the log; owner
"PM / Change Manager" is supported in part by [12], [13] and [29] and can stay; `size_variant` S understates a
two-weight type.

---

## Sources

### CANON: definitions, names and lineage - change-log (governance-docs, catalog id change-log-governance)

**[1] Project Management Institute (PMI), "Errata: A Guide to the Project Management Body of Knowledge (PMBOK Guide) - Sixth Edition (Fifth Printing)".** standards. **fetched-and-verified.**
`https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-6th-edition-5th-printing.pdf?v=5ec5b4d9-abb5-4d42-8542-8af75be7de3b`
Supports: The change-log sentence, and every place the change log appears as an input or output of Perform Integrated Change Control (section 4.6).
Quotable: "The change log is used to record all submitted change requests."
Quotable: "Figure 4-12. Added bullet under .2 Project documents for Change log."
Quotable: "Figure 4-13. (1) Added bullet under input .2 Project documents for Change log; (2) Added process box for 6.5 Develop Schedule with the input Change requests."
Quotable: "Outputs .1 Approved change requests .2 Project management plan updates • Any component .3 Project documents updates • Change log"
Quotable: "Issue log. Described in Section 4.3.3.3. New issues raised as a result of this process are recorded in the issue log."

**[2] Project Management Institute (PMI), "PMI Lexicon of Project Management Terms", Version 5.0 (last updated January 2026).** standards. **fetched-and-verified.**
`https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf?rev=447328d841c249af985d14177ddd5f95`
Supports: Whether the Lexicon has a standalone 'change log' entry (it does not), and what it does define: change control, change control board, change control system, change management plan, and change request.
Quotable: "change control. A process whereby modifications to documents, deliverables, or baselines associated with the project are identified, documented, approved, or rejected. See also change control board (CCB) and change control system."
Quotable: "change control board (CCB). A formally chartered group responsible for reviewing, evaluating, approving, delaying, or rejecting changes to the project, and for recording and communicating such decisions. See also change control and change control system."
Quotable: "change control system. A set of procedures that describes how modifications to the project deliverables and documentation are managed and controlled. See also change control and change control board (CCB)."
Quotable: "change management plan. A component of the project management plan that establishes the change control board, documents the extent of its authority, and describes how the change control system will be implemented. See also project management plan."
Quotable: "change request. A formal proposal to modify a document, deliverable, or baseline."
Quotable: "issue log. A project artifact where information about issues is recorded and monitored."

**[3] Association for Project Management (APM), "APM glossary of project management terms" (sourced from the 5th-8th editions of the APM Body of Knowledge).** standards. **fetched-and-verified.**
`https://www.apm.org.uk/resources/glossary/`
Supports: The 'Change log (or log)' entry and the 'change register' wording, read verbatim, plus the glossary's separate change-control and issue-log entries.
Quotable: "Change log A record of all project changes: proposed, authorised, rejected or deferred."
Quotable: "Change register (or log) A record of all proposed changes to scope."
Quotable: "Change control The process through which all requests to change the approved baseline of a project, programme or portfolio are captured, evaluated and then approved, rejected or deferred."
Quotable: "Change control board A formally constituted group of stakeholders responsible for approving or rejecting changes to the project baselines."
Quotable: "Change authority An organisation or individual with power to authorise changes on a project."
Quotable: "Change request A request to obtain formal approval for changes to the approved baseline."
Quotable: "Change freeze A point after which no further changes to scope will be considered."
Quotable: "Issue A problem that is now breaching, or is about to breach, delegated tolerances for work on a project or programme. Issues require support from the sponsor to agree a resolution."
Quotable: "Issue log A log of all issues raised during a project or programme, showing details of each issue, its evaluation, what decisions were made and its current status."
Quotable: "Issue register See Issue log."

**[4] Association for Project Management (APM), "What is change control?".** standards. **fetched-and-verified.**
`https://www.apm.org.uk/resources/what-is-project-management/what-is-change-control/`
Supports: Where the standing register sits inside the change-control process, and that APM's own process step names it 'a change register (or log)'.
Quotable: "Change control is the process through which all requests to change the approved baseline of a project, programme or portfolio are captured, evaluated and then approved, rejected or deferred."
Quotable: "Log change request in a change register (or log)."
Quotable: "It is important to differentiate change control from the wider discipline of change management ."

**[5] prince2.wiki (EMPII Group, written by Frank Turley), "Issues" practice page.** practitioner. **fetched-and-verified.**
`https://prince2.wiki/practices/issues/`
Supports: How PRINCE2 folds a request for change into the Issue Register, and the exact wording that names a change log as an alternative destination for the decision record.
Quotable: "Request for change : It is a proposal for a change to a baselined product, i.e., a product that has already been approved."
Quotable: "Issues must be recorded in the issue register ."
Quotable: "the recommendation, along with any supporting rationale and the decision-making process, should be documented in the issue register or change log."

**[6] prince2.wiki (EMPII Group, written by Frank Turley), "Change authority" people page.** practitioner. **fetched-and-verified.**
`https://prince2.wiki/people/change-authority/`
Supports: What the change authority role is and how the project board delegates it, corroborating the issues page's account of PRINCE2's change-control mechanics.
Quotable: "The change authority is a person or group to whom the project board may delegate responsibility for reviewing and approving change requests or off-specifications."
Quotable: "The use and composition of the change authority are documented in the issue management approach ."

### DIMENSION 2: Published change logs - field-level structure and status vocabularies

**[7] European Commission / PM² Alliance, PM² Project Management Methodology Guide v3.1 (Appendix B.7 Change Log and Appendix B.10 Decision Log).** primary. **fetched-and-verified.**
`https://www.pm2alliance.eu/wp-content/uploads/2024/02/pm%C2%B2-project-management-methodology-NO0523520ENN.pdf`
Supports: The 17-field, four-group Change Log in Appendix B.7 (Change Identification and Description; Change Assessment and Action; Change Approval; Change Implementation), its 8-value Status vocabulary, the separate 4-value Decision vocabulary, the Manage Project Change process, the licence, and PM2's four separate logs (Change, Risk, Issue, Decision) linked by the Traceability and Comments field.
Quotable: "B.7 Change Log"
Quotable: "A Change Log is used to document, monitor and control all project changes (see Appendix B)."
Quotable: "There are four possible decisions: approve, reject, postpone or merge the change request."
Quotable: "The status of a change request is logged in the Change Log. It may have the following values: Submitted, Investigating, Waiting for approval, Approved, Rejected, Postponed, Merged or Implemented."
Quotable: "Submitted: This is the initial status."
Quotable: "Assessing: Use this status to initiate an assessment."
Quotable: "Waiting for approval: Use this to initiate approval."
Quotable: "Merged: This status indicates that the change has been merged into some other change, so it is no longer being actively handled."
Quotable: "Escalation to the Directing or Steering layer is needed? (Yes or No)."
Quotable: "The ID(s) of the tasks (in the Project Work Plan) that implement the change, and/or the IDs of related issues, risks or decisions."
Quotable: "Issue Log, Risk Log, Change Log, Decision Log"
Quotable: "Document licensed under CC BY 4.0 license"
Quotable: "Implemented: This status indicates that the work implementing this change has been incorporated into the Project Work Plan."
Quotable: "Postponed: This status is set if the change is postponed indefinitely."
Quotable: "Person or committee that denied or approved the change."
Quotable: "The target date for the change to be delivered."
Quotable: "The date on which the change was actually delivered."

**[8] PM² Alliance, pm2.eu Artefacts listing, "Change Log" page.** vendor. **fetched-and-verified.**
`https://www.pm2.eu/change-log/`
Supports: The Change Log ships as its own downloadable artefact under Monitor & Control Logs, separate from the Change Request Form artefact listed alongside it
Quotable: "Use this as a template for Change Log document."
Quotable: "This template is part of the Monitor & Control Logs."
Quotable: "Free, downloadable and easy to edit .xlsx file."

**[9] PM² Alliance / European Commission, PM²-Project Artefacts Change Note (v3.0.1 to v3.1).** primary. **fetched-and-verified.**
`https://pm2.europa.eu/document/download/005bb253-3e7e-4299-bd5d-f7cc26e9f8cc_en?filename=PM2-Project%20Artefacts.ChangeNote.from_.v3.0.1%20to%203.1.pdf`
Supports: Confirms the Change Log's field structure did not change between v3.0.1 and v3.1; only cross-cutting guidance (sustainability, data protection, IT security, UX) was added, and the Change Log is listed among the Monitoring & Controlling logs updated
Quotable: "The new templates do not introduce any changes to the template structure or core content."
Quotable: "Monitoring & Controlling (Logs and Checklists): • Decision Log • Risk Log • Issue Log • Change Log"

**[10] Connecticut Department of Social Services, Enterprise PMO, Project Change Log v1.1.** primary. **fetched-and-verified.**
`https://portal.ct.gov/-/media/Departments-and-Agencies/DSS/CT-METS/Library/General/CTDSSChangeLogv11.pdf`
Supports: An 11-column per-row log (ID, Type, Description, Requested By, Date Created, Priority, Status, Cost Expectations, Assigned To, Date Resolved, Resolution/Comments), its 7-value Status list, and its 2-value Priority scale
Quotable: "Also known as Project Change Register"
Quotable: "The audience for the Project Change Log includes the project team, project sponsor, business owner, steering committee, and may include key project stakeholders."
Quotable: "Status - Assign a status to the change request; Submitted, In Review, Approved, Denied, Deferred, Withdrawn, or Closed."
Quotable: "Priority - Assign a level of priority to the change request of Material or Non-Material"
Quotable: "Material - A critical change that has significant impacts to the Cost, Schedule, Scope and/or Quality of the project"
Quotable: "Date Resolved - The date the change request becomes a change control"

**[11] US Department of Health and Human Services, EPLC, Change Management Log spreadsheet (Internet Archive raw copy).** primary. **fetched-and-verified.**
`https://web.archive.org/web/20260226151501id_/https://www.hhs.gov/sites/default/files/ocio/eplc/EPLC%20Archive%20Documents/07%20-%20Change%20Management%20Plan/eplc_change_management_log.xls`
Supports: The 15-column spreadsheet's field list, its Current Status vocabulary (3 core + 3 optional), its Priority vocabulary (which names 4 terms while its own instructions claim only 3 valid options), and its explicit Escalation column
Quotable: "CR#: A unique ID number used to identify the change request in the change management tracking log."
Quotable: "Open: The change request is currently open but has not yet been addressed."
Quotable: "Work In Progress: The change request is being actively worked to develop a resolution."
Quotable: "Closed: The change request is no longer considered an active project threat and can be closed with or without resolution."
Quotable: "Valid options include the following: High, Medium, Low."
Quotable: "Critical: change request will stop project progress if not resolved."
Quotable: "Escalation Required (Y/N): This column should be populated with “Yes” if the change request needs to be escalated"
Quotable: "CR# | Current Status | Priority | Change Request Description | Assigned To Owner | Expected Resolution Date | Escalation Required (Y/N)? | Action Steps | Impact Summary | Change Request Type | Date Identified | Assoc ID | Entered By | Actual Resolution Date | Final Resolution & Rationale"

**[12] US Department of Health and Human Services, EPLC, Change Management Plan template (Internet Archive raw copy).** primary. **fetched-and-verified.**
`https://web.archive.org/web/20260226151438id_/https://www.hhs.gov/sites/default/files/ocio/eplc/EPLC%20Archive%20Documents/07%20-%20Change%20Management%20Plan/eplc_change_management_plan_template.doc`
Supports: The one shared 10-element data-element list HHS specifies for BOTH the Change Request Form and the Change Management Log, and the Generate CR / Log CR process step split that nonetheless keeps request-submission and logging as two distinct actions
Quotable: "A submitter completes a CR Form and sends the"
Quotable: "The Change Manager enters the CR into the CR Log."
Quotable: "LIST AND DEFINE THE DATA ELEMENTS THE PROJECT TEAM NEEDS TO INCLUDE ON THE CHANGE REQUEST FORM AND IN THE CHANGE MANAGEMENT LOG."
Quotable: "Assigned by the Change Manager"
Quotable: "The product version that the suggested change is for"
Quotable: "THE LIST OF ELEMENTS IS AT THE DISCRETION OF THE PROJECT MANAGER."

**[13] University of California Office of the President (UCOP), Information Technology Services, Change Request Log Template.** primary. **fetched-and-verified.**
`https://www.ucop.edu/information-technology-services/_files/itlc/3.5-supporting-change-request-log-template.xlsx`
Supports: A 7-column log (Date of Request, CR#, Change Request Title, Assigned To, Description of Change, Current Status, Implementation Date) with no Priority, no Requested-by, no Escalation and no dedicated traceability field, and its own statement that the log is populated by transferring data out of a separate change request form
Quotable: "The Change Request Log Template provides a centralized view of the current status of project change requests."
Quotable: "The Change Request Coordinator is responsible for maintaining the Change Request Log on behalf of the Change Management Lead."
Quotable: "Transfer the Date of Request, Change Request #, Change Request Title, the resource assigned to the change request, the description of the change requested, current status and implementation date from the change request form for each specific change request."
Quotable: "Submitted - The change request has been developed and submitted for consideration"
Quotable: "Rework - The Change Request has been sent back to a previous step for additional information"
Quotable: "Date of Request | CR# | Change Request Title | Assigned To | Description of Change | Current Status | Implementation Date"

**[14] San Francisco State University, IT Services, Change Management Log Template.** primary. **fetched-and-verified.**
`https://its.sfsu.edu/sites/default/files/documents/Change_Management_Log_Template.xlsx`
Supports: A 15-column log whose field names, drop-down vocabularies and instructional prose are effectively a verbatim copy of the HHS EPLC Change Management Log spreadsheet, found by independent search rather than assigned
Quotable: "ID: A unique ID number used to identify the change request in the change management tracking log."
Quotable: "Escalation Required (Y/N): This column should be populated with “Yes” if the change request needs to be escalated"
Quotable: "ID | Current Status | Priority | Change Request Description | Assigned To Owner | Expected Resolution Date | Escalation Required (Y/N)? | Action Steps | Impact Summary | Change Request Type | Date Identified | Assoc ID | Entered By | Actual Resolution Date | Final Resolution & Rationale"

### DIMENSION 3: Neighbours under the same or a similar name (change-log bundle boundaries)

**[15] Keep a Changelog project - "Keep a Changelog", version 1.1.0.** practitioner. **fetched-and-verified.**
`https://keepachangelog.com/en/1.1.0/`
Supports: What a software changelog records, and the absence of requester/decider/decision/status fields
Quotable: "A changelog is a file which contains a curated, chronologically ordered list of notable changes for each version of a project."
Quotable: "To make it easier for users and contributors to see precisely what notable changes have been made between each release (or version) of the project."
Quotable: "Added for new features. Changed for changes in existing functionality. Deprecated for soon-to-be removed features. Removed for now removed features. Fixed for any bug fixes. Security in case of vulnerabilities."
Quotable: "Changelogs are for humans, not machines."

**[16] IT Process Maps (IT Process Wiki) - "ITIL Glossary / ITIL Terms C".** vendor. **fetched-and-verified.**
`https://wiki.en.it-processmaps.com/index.php/ITIL_Glossary/_ITIL_Terms_C`
Supports: ITIL's two named change artifacts (Change Record, Change Schedule) and the absence of any 'change log' entry in ITIL's own glossary
Quotable: "The Change Record contains all the details of a Change, documenting the lifecycle of a single Change."
Quotable: "It is usually created on the basis of a preceding Request for Change (RFC)."
Quotable: "A Document that lists all approved Change Proposals and Changes and their planned implementation dates."
Quotable: "A Change Schedule is sometimes called a Forward Schedule of Changes (FSC)."

**[17] IT Process Maps (IT Process Wiki) - "Change Management" (ITIL process page).** vendor. **fetched-and-verified.**
`https://wiki.en.it-processmaps.com/index.php/Change_Management`
Supports: Confirms the same two named ITIL artifacts (Change Record, Change Schedule) on the process page and the continued absence of 'change log' wording
Quotable: "The Change Record contains all the details of a Change, documenting the lifecycle of a single Change. It is usually created on the basis of a preceding Request for Change (RFC)."
Quotable: "A Document that lists all approved Change Proposals and Changes and their planned implementation dates. A Change Schedule is sometimes called a Forward Schedule of Change (FSC)."

**[18] Wikipedia - "Change-advisory board".** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Change-advisory_board`
Supports: What the CAB oversees (requested/approved changes in production) and confirmation it names no cumulative change log artifact
Quotable: "A change-advisory board (CAB) delivers support to a change-management team by advising on requested changes, assisting in the assessment and prioritization of changes."
Quotable: "A CAB is an integral part of a defined change-management process designed to balance the need for change with the need to minimize inherent risks."

**[19] NIST - Special Publication 800-128, "Guide for Security-Focused Configuration Management of Information Systems".** primary. **fetched-and-verified.**
`https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-128.pdf`
Supports: Whether NIST 800-128 distinguishes a configuration-change record from a project change log (it does not use 'change log' wording at all)
Quotable: "Configuration Change Control - process for managing updates to the baseline configurations"
Quotable: "Configuration change control is the documented process for managing and controlling changes to the configuration of a system or its constituent CIs."
Quotable: "Help Desk Procedures - Describes how change requests originating through the help desk are recorded, submitted, tracked, and integrated into the configuration change control process."

**[20] Lucid Meetings glossary - "What is a Decision Log?".** vendor. **fetched-and-verified.**
`https://www.lucidmeetings.com/glossary/decision-log`
Supports: Negative evidence for sub-dimension 4: the page defines a decision log but contains zero occurrences of "change log" or "changelog," so it cannot be the source that states the boundary

**[21] ProjectManager.com blog - "How to Use a Decision Log for Optimal Results for Your Project".** vendor. **fetched-and-verified.**
`https://www.projectmanager.com/blog/project-decision-log`
Supports: Negative evidence for sub-dimension 4: the page's one occurrence of "change log" is a marketing list of log types the software supports ("decision log, change log, issue log, risk log..."), not a stated distinction
Quotable: "Keep your project decision log, change log, issue log, risk log, action log, raid log, risk register or any log you use on the task list view of our software."

**[22] Lark Suite library - "Change Log Project Management: A Comprehensive Guide".** vendor. **fetched-and-verified.**
`https://www.larksuite.com/library/project-management/project-management-concepts/change-log-project-management`
Supports: Negative evidence for sub-dimension 4: raw body text contains zero occurrences of "decision log," so it does not draw the boundary either

**[23] Project Management Knowledge - "Change Log" definition entry.** practitioner. **fetched-and-verified.**
`https://project-management-knowledge.com/definitions/c/change-log/`
Supports: Negative evidence for sub-dimension 4: raw body text contains zero occurrences of "decision log"

**[24] meetjamie.ai blog - "What is a Decision Log?".** vendor. **fetched-and-verified.**
`https://www.meetjamie.ai/blog/decision-log`
Supports: Negative evidence for sub-dimension 4: describes decision logs at length but never states a boundary against a named change log artifact

**[25] Plane blog - "Decision log: What it is, why teams use it, and template".** vendor. **fetched-and-verified.**
`https://plane.so/blog/decision-log-what-it-is-why-teams-use-it-and-template`
Supports: Negative evidence for sub-dimension 4: the only sentences pairing 'decision' with 'change' describe change AS AN INPUT to a decision ("teams can quickly understand what changed... and how the [decision followed]"), never a stated boundary between two named log artifacts
Quotable: "A decision log centralizes decision documentation in a single searchable location, enabling teams to review past decisions with full context."

### DIMENSION 4: Keeping the log - ownership, cadence, reconciliation, and how it fails (change-log bundle)

**[26] US Department of Health and Human Services, EPLC, "Change Management Practices Guide" (Internet Archive raw copy).** primary. **fetched-and-verified.**
`https://web.archive.org/web/20260226151357id_/https://www.hhs.gov/sites/default/files/ocio/eplc/EPLC%20Archive%20Documents/07%20-%20Change%20Management%20Plan/eplc_change_management_practices_guide.pdf`
Supports: Review cadence for change requests, the change-control-board approval threshold, and the general tie between change management and baseline tracking
Quotable: "All projects, regardless of type or size, should maintain a change log and regularly manage requested changes."
Quotable: "Document - Change requests should be centrally documented using some type of log. A change request log template is provided at the end of this guide and should be used in the absence of something more sophisticated available to the project team."
Quotable: "Unique Entries - Each change request should be recorded as a single line item. Do not combine multiple requests under one change request ID."
Quotable: "Review - A regular review of change requests is good project management practice. Depending on the complexity of the project the review process may happen daily but should happen at least weekly for even the simplest projects."
Quotable: "A CCB is a formally constituted group of stakeholders responsible for reviewing, evaluating, approving, delaying, or rejecting changes to the project. All decisions and recommendations related to change requests are recorded."
Quotable: "The change management process establishes an orderly and effective procedure for tracking the submission, coordination, review, evaluation, categorization, and approval for release of all changes to the project’s baselines."
Quotable: "a project manager (PM) may be authorized to personally approve changes with a project impact of less than $5,000"

**[27] US Department of Health and Human Services, EPLC, "Change Management Checklist" v1.0 (Internet Archive raw copy).** primary. **fetched-and-verified.**
`https://web.archive.org/web/20260226151616id_/https://www.hhs.gov/sites/default/files/ocio/eplc/EPLC%20Archive%20Documents/07%20-%20Change%20Management%20Plan/eplc_change_management_checklist.pdf`
Supports: Confirms the log's update is the checklist's one named ongoing/iterative activity, with no named role attached
Quotable: "Change Management Checklist (Ongoing/Iterative Activities) Update the Change Management Log. Communicate status updates to any change requests to the project team and to stakeholders."

**[28] William Meller, Project Management Compass (Substack), "How to Handle Every Project Change Without Becoming the Person Everyone Hates".** practitioner. **fetched-and-verified.**
`https://projectmanagementcompass.substack.com/p/how-to-handle-every-project-change`
Supports: The change-log-versus-decision-log boundary as one named practitioner states it, the log's audit-trail function, the failure of undocumented informal decisions, and proportion for a small project. Read from the free preview only; the article is paywalled after its outline.
Quotable: "A decision log tracks what was decided. A Change Control Log tracks what changed, why it changed, who approved it, and what the impact was on the baseline."
Quotable: "The decision log answers: what did we decide and when? The Change Control Log answers: what is different now compared to what we agreed at the start, and is that difference officially sanctioned?"
Quotable: "Changes happen. Decisions get made informally. Nobody writes it down. And eventually, the project is living in a reality that the plan never accounted for and nobody officially approved."
Quotable: "That is not bureaucracy. That is institutional memory. And it is worth its weight in gold the first time your sponsor says “I never approved that” and you can show them the date, the email chain, and their own name in the Approved By column."
Quotable: "A two-person project running for eight weeks does not need a Change Control Board with quarterly meetings. It needs a lightweight log and a clear agreement between the project manager and the sponsor about what requires formal approval versus what can be handled directly."

**[29] Abdullah Oguz, Ph.D., "Project Management: Navigating the Complexity" (Cleveland State University Pressbook, open textbook), Ch. 11.4 "Change Control Process".** academic. **fetched-and-verified.**
`https://pressbooks.ulib.csuohio.edu/project-management-navigating-the-complexity/chapter/11-4-change-control-process/`
Supports: Names the project manager as the end-to-end owner of the change process, and ships a named field for reconciling an approved change to the plan/baseline
Quotable: "The change requests are generally submitted to the project sponsor by the project manager for review and approval. The project manager is responsible to monitor the change process from the very beginning to the very end."
Quotable: "Project Change Request Tracking Log Project Name: Project Manager Submission Data Impact Analysis PM Review and Approval Request# Submitted By: Date Date Assigned to Analyst Assigned to Date Analysis Completed Date Reviewed Committee Decision Date Approved Date Request Integrated into Project Plan"
Quotable: "Change requests are made to modify documents, deliverables, and baselines. They are issued to expand, adjust, or reduce project scope, product scope, or quality requirements and schedule or cost baselines."

**[30] Mohammad Fahad Usmani, PMP, PMI-RMP, PM Study Circle, "What is the Change Control Board in Project Management?".** practitioner. **fetched-and-verified.**
`https://pmstudycircle.com/change-control-board/`
Supports: Names the CCB as the reviewing body that meets on a recurring basis and formally re-reviews implementation of approved changes
Quotable: "A Change Control Board (CCB) is a group of stakeholders (e.g., management, experts, and project sponsors) who meet regularly to discuss project changes and approve and reject change requests."
Quotable: "The change control board reviews every change request received from the project manager. They determine the change’s impact on every project objective, such as cost, schedule, scope, quality, etc."
Quotable: "Monitor and Review Changes: Regularly review the implementation of approved changes to ensure that they are executed as planned and to address any issues."

### Dimension 5: where a change log earns its keep, and where it does not

**[31] Scrum.org / Ken Schwaber and Jeff Sutherland - The 2020 Scrum Guide.** primary. **fetched-and-verified.**
`https://scrumguides.org/scrum-guide.html`
Supports: Scrum's own mechanism for handling change to scope, and the absence of any change-log or change-control vocabulary in the canonical text.
Quotable: "The Product Backlog is an emergent, ordered list of what is needed to improve the product. It is the single source of work undertaken by the Scrum Team."
Quotable: "Those wanting to change the Product Backlog can do so by trying to convince the Product Owner."
Quotable: "The Product Owner is one person, not a committee."
Quotable: "Product Backlog may also be adjusted to meet new opportunities."

**[32] DORA (Google Cloud) - "Streamlining change approval" (Capabilities).** practitioner. **fetched-and-verified.**
`https://dora.dev/capabilities/streamlining-change-approval/`
Supports: What the page's finding is actually about (production-change approval by external bodies such as CABs), used to state precisely what it does NOT say about project baseline change logs.
Quotable: "Research by DORA... finds that change approvals are best implemented through peer review during the development process, supplemented by automation to detect, prevent, and correct bad changes early in the software delivery life cycle."
Quotable: "no evidence was found to support the hypothesis that a more formal, external review process was associated with lower change fail rates"
Quotable: "Do production changes need to be approved by an external body before deployment or implementation? The amount of time changes spend waiting for approval from external bodies."

**[33] U.S. General Services Administration / Acquisition.gov - FAR 52.243-1, Changes - Fixed-Price.** primary. **fetched-and-verified.**
`https://www.acquisition.gov/far/52.243-1`
Supports: The contracted, fixed-price camp: a formal, unilaterally-ordered change mechanism against a fixed scope baseline (drawings/designs/specifications), with an equitable-adjustment record - the shape a change log formalizes as contractual evidence.
Quotable: "The Contracting Officer may at any time, by written order, and without notice to the sureties, if any, make changes within the general scope of this contract in any one or more of the following: (1) Drawings, designs, or specifications..."
Quotable: "If any such change causes an increase or decrease in the cost of, or the time required for, performance of any part of the work under this contract, whether or not changed by the order, the Contracting Officer shall make an equitable adjustment in the contract price, the delivery schedule, or both, and shall modify the contract."
Quotable: "The Contractor must assert its right to an adjustment under this clause within 30 days from the date of receipt of the written order."

**[34] Cornell Law School Legal Information Institute (mirror of the U.S. Code of Federal Regulations) - 21 CFR 820.30(i), Design controls.** primary (mirror). **fetched-and-verified.**
`https://www.law.cornell.edu/cfr/text/21/820.30`
Supports: The regulated-industry camp (medical device): a legal requirement that every design change be identified, documented, reviewed, and approved before implementation, i.e. an auditable change record.
Quotable: "(i) Design changes. Each manufacturer shall establish and maintain procedures for the identification, documentation, validation or where appropriate verification, review, and approval of design changes before their implementation."

**[35] Ryan Singer / Basecamp - Shape Up: "Bets, Not Backlogs" (chapter 7).** practitioner. **fetched-and-verified.**
`https://basecamp.com/shapeup/2.1-chapter-07`
Supports: The product-team-with-no-fixed-baseline camp: a named, published methodology that deliberately rejects a standing backlog/register in favor of fixed-time, variable-scope betting, with the reasoning stated.
Quotable: "Backlogs are a big weight we don't need to carry. Dozens and eventually hundreds of tasks pile up that we all know we'll never have time for."
Quotable: "Backlogs are big time wasters too. The time spent constantly reviewing, grooming and organizing old ideas prevents everyone from moving forward on the timely projects that really matter right now."
Quotable: "There's no one backlog or central list and none of these lists are direct inputs to the betting process."

### Dimension 6 (the gap question) for change-log: what does a GOOD project/program change log do that a naive one (a list of changes with dates) omits?

**[36] U.S. Government Accountability Office - "Information Technology: Agencies Need to Establish Comprehensive Policies to Address Changes to Projects' Cost, Schedule, and Performance Goals" (GAO-08-925, 31-JUL-08).** primary. **fetched-and-verified.**
`https://www.govinfo.gov/content/pkg/GAOREPORTS-GAO-08-925/html/GAOREPORTS-GAO-08-925.htm`
Supports: An auditor's stated criteria for what a documented baseline-change decision must contain, applied by analogy to a change-log row (this report audits agency REBASELINING POLICIES, not change logs directly, so every claim is 'GAO's audit criteria for a documented change decision,' never 'GAO says a change log must')
Quotable: "Require management review. A rebaselining policy should identify the authority who decides whether the rebaselining is warranted and the rebaselining plan is acceptable. In addition, the policy should outline decision criteria used by the decision authority to determine if the rebaseline plan is acceptable."
Quotable: "Require that the process is documented. A rebaselining policy should identify and document rebaselining decisions, including the reasons for rebaselining; changes to the approved baseline cost, schedule, and scope; management review of the rebaseline request; and approval of new baseline."
Quotable: "discuss measures in place to prevent recurrence"
Quotable: "Require validating the new baseline. A rebaselining policy should identify who can validate the new baseline and how the validation is to be done."

**[37] Association for Project Management (APM) blog - Mike Wild FAPM ChPP (senior programme manager) - "How do project managers control the decision to make a change?".** practitioner. **fetched-and-verified.**
`https://www.apm.org.uk/blog/how-do-project-managers-control-the-decision-to-make-a-change/`
Supports: Names the change register's audit-history function (cumulative time/cost/scope shown against the original baseline), requester sign-off on impact assessment, and use of the log to spot trend patterns across entries - read from the body, not the excluded APM glossary
Quotable: "Log the request in the change register (or log). This is a working document that allows the project manager to capture change and track it throughout the project until it has been resolved. It provides an audit history of how the change has been managed and shows the additional time/cost/scope that has been approved since the project scope was first agreed."
Quotable: "Ensure that the owner or originator of the change signs off on the impact assessment."
Quotable: "on larger projects, programmes and portfolios, more seasoned projects managers will be looking for patterns of change to identify trends that might suggest certain aspects of the project are more vulnerable to change"

**[38] Advisera 20000Academy - "ITIL/ISO20000 Change Management: Remediation and back-out".** vendor. **fetched-and-verified.**
`https://advisera.com/20000academy/blog/2017/06/13/what-is-the-remediation-procedure-and-back-out-in-the-itiliso-20000-change-management-process/`
Supports: A third, adjacent domain (IT operational change management, not project governance or software CHANGELOG). Transfers by analogy the idea that a change record names a specific person/role empowered to authorize (not just 'approved: yes'), and that reverting a change depends on a recorded baseline/configuration state to restore to. Sells an ISO 20000 toolkit, so read as vendor-tier, not standards-tier
Quotable: "the change authority (the person or group who is empowered to authorize change of a particular type) needs to ensure that there is a plan to revert to the initial state if change implementation is unsuccessful"
Quotable: "a configuration baseline that will enable the restoration of a known configuration"

**[39] Office of Inspector General, South Florida Water Management District - "Monitoring Review of Construction Change Orders from April 1, 2024 through September 30, 2024" (Project #25-04), J. Timothy Beirnes, CPA, Inspector General.** primary. **fetched-and-verified.**
`https://www.sfwmd.gov/sites/default/files/documents/FINAL_Change_Order_Review_Sep_2024.pdf`
Supports: A real auditor's review of an organization's actual change-order log/system (eBuilder), giving three directly on-point findings: (1) the system's single 'approval date' field conflates two genuinely different events - staff finalization vs. the governing board's authorization; (2) the auditor computed cumulative approved change as a percentage of the original contract value precisely because a list of individual changes does not itself show the compounding effect against baseline; (3) the auditor cross-checked the log against an external decision record (Governing Board resolutions) to confirm every authorized change actually appears in the system of record
Quotable: "It should be noted that the approval date in eBuilder represents the date that the staff finalized the approval process for a change order and not the Governing Boards authorization date."
Quotable: "identifying all construction contract change orders that the Governing Board authorized through resolutions during the Reporting Period to ensure that all authorized change orders were included in the eBuilder system"
Quotable: "Percent of Original Contract 24.5% 4.5%"

**[40] Project Management Formula - "Change Log Template".** vendor. **fetched-and-verified.**
`https://projectmanagementformula.com/change-log-template/`
Supports: Two directly on-point, verbatim practitioner statements: rejected/deferred change requests are kept in the log rather than removed, with a reason attached; and 'date approved' and 'implementation start date' are named as two distinct fields precisely because they can diverge when an approved change is queued behind other work
Quotable: "Keep them in the log with a clear “Rejected” status and a note explaining why. This provides a record for future reference and prevents the same request from being resubmitted without understanding why it was declined."
Quotable: "When work on the approved change actually begins. This may be different from the approval date if the change is queued behind other work."
Quotable: "By week eight, the cumulative impact of those small changes had shifted the schedule by two weeks."
