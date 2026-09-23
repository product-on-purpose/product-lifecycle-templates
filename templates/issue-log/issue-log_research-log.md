# issue-log: research log

Research conducted 2026-09-23 in two passes: an admission sweep run while the spec was written (sixteen
agents across the named standards, open frameworks, practice and boundaries), and the build's six-dimension
fan-out (definitions and standards, published structures, lifecycle and escalation, boundaries, failure
modes, and the standing gap question). **41 sources are recorded below: 38 fetched-and-verified, two
url-confirmed-not-read and one not-retrieved.** Only `fetched-and-verified` sources are quoted anywhere in this
bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a
retrieval tool returns. Pages were downloaded directly (HTML decoded as UTF-8, PDFs through `pdftotext`
without `-layout`, a `.DOC` through `antiword`, a `.xls` by string extraction) and each quotation searched for
as a normalized substring. The build's research agents ran the same check before returning a quotation, and
every quotation was checked again here. Where a cached copy was the only evidence, because a site now refuses
scripted requests, the cached copy was inspected to confirm it is a raw page extraction and not a summary.

---

## What the checks caught, and what was not read

**A research dimension misreported the one openly licensed template source, and the raw text caught it.**
The published-structures dimension reported that "No source carries a dedicated escalation field" and that
PM²'s Issue Log "has no such field" for cross-references. Both are false. [1]'s Appendix B.9 lists an
**Escalation** field ("Whether or not the issue is to be escalated to the Directing or Steering Layers (Yes or
No).") and a **Traceability/Comments** field linking an issue to "related changes, risks or decisions". The
admission sweep had read them correctly; the build dimension had not. The template follows [1] as printed.

**A section said to be paywalled was readable.** One dimension recorded APM's *Body of Knowledge* section 4.3.5
as unreadable, having found only its title in a publisher's sample [6]. APM hosts the full seventh edition as
a consultation copy [5], and section 4.3.5 is in it. [5] marks itself "For use by APM individual and corporate
members only", so this bundle quotes it briefly and adapts nothing from it.

**A page titled for the current edition describes the previous one.** [14] is titled and addressed as PRINCE2 7
material, is dated 3 April 2023, before PRINCE2 7's release, and uses sixth-edition apparatus throughout. It
supports nothing here and is recorded so nobody cites it for PRINCE2 7.

**Four failure modes a reader would expect were searched for and not found.** No source read describes an
issue log that became a dumping ground, duplicated a ticket tracker, was used to assign blame, or never closed
anything, as an observed failure. Audit and inspector-general reports were searched specifically and named no
issue log. **This bundle does not assert any of the four as a documented failure.** What was found instead is
recorded under "Notes for the companion".

**Not read, and nothing in this bundle may rest on them:**

- **AXELOS's own PRINCE2 manuals** (sixth edition 2017, PRINCE2 Agile 2016, PRINCE2 7 2023), which sit behind a
  subscription [40]. PRINCE2 enters this bundle through its 2009 glossary reproduced with AXELOS's permission
  [8], PeopleCert's account of PRINCE2 7 [10], and prince2.wiki [11]-[13].
- **ISO 21502:2020 beyond its official free preview** [7]. The preview carries the definition of an issue and
  the contents line "7.9 Issues management"; the clause body is past it. **Nothing here says ISO names an issue
  log**, because nothing readable says so.
- **The UK government's Teal Book chapter on issue management** [39], which refused every raw fetch.
- **A PMI article on escalating project problems** [41], which returned 403 to every attempt.

---

## The admission record

**ADR 0030's test is met four times over by name.** PMI's *Lexicon* defines the artifact: "issue log. A project
artifact where information about issues is recorded and monitored." [2], and the *PMBOK Guide* lists it as a
project document [3]. APM's glossary defines "Issue log" and points "Issue register" to it [4]. PRINCE2's
2009 glossary defines the Issue Register [8]. The European Commission's PM² guide publishes the artifact with
its full field list, and under CC BY 4.0: "The Issue Log is a register (log file) used to capture and maintain
information on all issues that are being formally managed." [1]

**Four public bodies publish working templates** [16] [17] [18] [20], one of which says it is "based on the
PRINCE2 recommended issue log" [16]. None states a reuse licence, so they are structure evidence only.

**[1] is the source this bundle may adapt**: "Reproduction and reuse is authorised provided the source is
acknowledged." It is the reverse of the hazard in an earlier bundle: `launch-coordination-checklist`'s origin
forbade derivatives.

---

## Claims flagged contested or time-bound

**What an issue is: four positions, and the template must make a team choose one.**

1. **Anything that has happened and needs someone to act.** [1]: "An issue is any unplanned event related to
   the project that has already happened and requires the intervention of the Project Manager (PM) or higher
   management". PRINCE2 2009 [8]: "A relevant event that has happened, was not planned, and requires management
   action." [15]: "an issue is something that already has happened."
2. **Only what breaches a tolerance.** APM [4]: "A problem that is now breaching, or is about to breach,
   delegated tolerances for work on a project or programme." [5] draws the consequence: issues "are
   differentiated from problems that are dealt with on a day-to-day basis by the project manager and team."
3. **Anything that could affect the project.** PRINCE2 7, as PeopleCert states it [10]: "the broad definition
   of issues is "anything that could affect the project"". This is a change from the 2009 definition and pulls
   the concept toward risk.
4. **A current condition that may have an impact.** PMI's *Lexicon* [2]: "A current condition or situation that
   may have an impact on one or more objectives." It requires neither that something happened nor that a
   tolerance broke.

prince2.wiki [11] states two of these on one page ("Any expectation different from the baselines" and "an
event relevant to the project that requires project management consideration") without reconciling them.

**Whether a request for change is an issue.** PRINCE2 says yes: an issue can be "a problem, a concern, a
business opportunity, a request for change, or something off-specification" [10], and "Not all issues result
in changes. But all changes start as issues." [10] The Northern Ireland template records changes on the issue
log [16]. PMI names a separate change log, "used to record all submitted change requests" [3], and states no
rule for where the two overlap. A practitioner [28]: "Some people also manage changes to the project as issues,
but personally, I don't". **Live and unresolved**; the bundle names both and records the hand-off.

**Review cadence.** The two authors of [15] disagree inside one article: "We review the open issues on the
issue log every week." against "Issues recorded in the issues register should be discussed almost every day".
[19] reviews weekly with high-severity and escalated issues first.

**Escalation trigger: a role ladder or a clock.** [21] escalates by role when the current holder cannot
resolve, with no timer. [19] escalates on stated conditions, including an issue "In Review" for ten business
days. [24] (a vendor) runs a clock that "starts on the day the issue is first logged". [1] escalates by a Yes
or No per issue against thresholds set in its plan. **No source reconciles these.**

**Resolved and closed.** [1] defines them as separate states, Closed being "all work is completed and
verified". [19] has a second person verify ("the issue originator reviews a resolved issue and verifies it can
be closed") but then sets the status to "Resolved" with a "Closed Date". [21]'s glossary does not separate
them. **The bundle defines both terms itself and says so.**

**What the register is called.** The two authors of [15] disagree in print ("I call the issue register the
"issue log""); APM treats the names as synonyms [4]; PRINCE2 uses "register" [8].

**PRINCE2 7 moved the register.** A training provider [14] and prince2.wiki [12] place the PRINCE2 7 issue
record inside a single project log rather than a standalone register. [14] is unreliable on edition; this
bundle states only that PRINCE2 7 changed the definition [10], not where it files the record.

---

## Notes for the companion

**The honest framing.** An issue log is one of the most widely published project documents there is, and its
sources agree on almost nothing except that it is not a risk register. **The bundle's job is to make a team
decide, in writing, the three things the sources leave open**: what counts as an issue here, when an issue
goes up, and what "closed" means.

**The evidentiary spine, in the order it should be used:**

1. **That the type exists:** [2], [4], [8], [1].
2. **What it holds:** [1]'s B.9 field list, corroborated by [16] [17] [18] [20] [9] [15].
3. **Where it ends:** the risk boundary, sourced everywhere ([15], [5], [27]); the RAID relationship [28]
   [29]; the change fork [10] [3] [28]; the impediment backlog [31] [32].
4. **How it runs:** [19]'s lifecycle and weekly review, [21]'s ladder, [1]'s plan-held thresholds.
5. **How it fails:** only what the sources say (below).

**How it fails, as sourced, and nothing more:**

- **No owner.** [38]: "If the issue doesn't have an owner, it's likely never to get resolved." [26] names why:
  "Nobody wants to create conflict at kickoff by assigning ownership of something potentially difficult".
- **Nobody reviews it.** [12]: "This task often gets neglected when project managers get busy".
- **Issues raised late, and decided badly above the team.** [5] names both barriers: "a lack of time or
  reluctance from project professionals to identify and escalate issues early", and "an inability of the
  governance board to make an informed decision that addresses the root cause of the issue rather than treating
  the symptoms".
- **Aging.** [26]: "Never let a RAID item go more than two reviews without movement". [25]: "Unresolved issues
  will damage the project". Both are prescriptions, not measured incidents.
- **Blame**, as a warning only: [25] "adding additional layers of complexity by introducing conflict, blame or
  other emotions will not help the resolution of the issue".

**The section design, as the research moved it from the spec.** Seven sections in full, five in lean. **The
spec's shape held**; the research moved columns, not sections.

| Section | Lean | What the research did to it |
|---|---|---|
| **Purpose and Threshold** | yes | **Strengthened.** The four positions above are the choices. [5] supplies the reason a threshold matters (issues are not day-to-day problems), [19] a worked threshold ("cannot be resolved at the project team level within three days"), and [12] PRINCE2's split between formal issues and the informal ones kept elsewhere |
| **Priority Scale** | yes | [1]'s separate 1-to-5 urgency and impact scales and [18]'s named impact levels plus a two-value materiality split are the published shapes. [5] ties prioritisation to "the relative priorities of scope, quality, time, cost and benefits". **[1] has no field literally named priority**, despite its plan text [1] referring to one; the template does not claim otherwise |
| **Issues** | yes | The load-bearing table. **Gains "Last updated"**, which the gap dimension found missing from naive logs and three sources carry ([9], [16], [37]). Description carries cause and impact, per [5] ("the nature of the issue, its causes and impacts"). One named owner per row |
| **Escalation** | yes | Stays in lean. The table records what went up, to whom, when, and the decision awaited, which is the record [24] describes and the RAID example already keeps. The rule may be a ladder [21], a clock [24] or a per-issue flag [1]; the guidance offers all three |
| **Review and Ownership** | yes | [19]'s weekly review with priority triage; [15]'s disagreement on cadence is reported, not resolved |
| **Closed Issues** | no | Resolution, **who confirmed it** ([19], [1]), closed date, and **a lesson, if any**, which [1] B.4 ("Specify the procedure for updating the Lessons Learned after an issue is resolved") and [12] ("Capture lessons learned from resolved issues") support |
| **Links to Other Logs** | no | Origin risk ([27]: the risk "closes as occurred"), change request raised ([10], [3]), decision that closed it, and the tasks implementing it, all from [1]'s Traceability field |

**Teaching points the templates, guide and example must stay consistent with:**

- **State the threshold, because the standards disagree about what an issue is.**
- **One named person owns each issue**; a role or "the team" is not an owner.
- **A materialized risk becomes an issue, and the risk entry closes as occurred, linked both ways.**
- **Escalation is decided before it is needed**, and what is escalated is recorded with its date and the
  decision awaited.
- **Resolved is not closed**: closure is confirmed by someone who did not do the fix. The term definitions are
  this bundle's, drawn from [1] and [19].
- **A change request starts as an issue in PRINCE2 and is handed to change control**; the log records the
  hand-off either way.

**What this bundle must not say:** that issue logs commonly become dumping grounds, duplicate ticket trackers,
are used for blame, or never close, which no source read documents; any failure frequency; that ISO names an
issue log; that [1] has a priority field; anything quoted from the AXELOS manuals or the Teal Book; that an
issue log and a bug tracker are divided by any source, which none of the sources read does ([33] divides tool
categories, not documents): **that boundary is labelled as this library's own judgment**. The boundaries with
an action log and a decision log are likewise this library's reasoning from [30]'s definitions of those two
logs, which never mention an issue log.

**The example.** The Reporting Platform Modernization program's issue log, the deepened record behind the RAID
log's Issues quadrant, dated 2026-07-20 to match the RAID log's last review. `ISS-11` and `ISS-12` exactly as
the RAID log records them; `ISS-11` escalated on 2026-07-04, which is what makes it 16 days old on that date.
**The two are the only open issues**, because the RAID log counts two. Any closed issue it shows must have
closed before 2026-07-20 and must not contradict a sibling.

**The pairing.** `pairs_with: []`: no pm-skills skill produces or consumes an issue log.

---

## Sources

**[1] European Commission - "PM² Project Management Methodology Guide", Open Edition v3.1 (Publications Office of the European Union, 2023), Appendix B.4 Issue Management Plan and Appendix B.9 Issue Log.** primary (methodology guide). **fetched-and-verified.**
`https://www.pm2alliance.eu/wp-content/uploads/2024/02/pm%C2%B2-project-management-methodology-NO0523520ENN.pdf`
Supports: A named public body publishing the issue log as a written document with its full field list (ID, category, title, description, status, identified by, identification date, action details, urgency, impact and size on 1-to-5 scales, target date, issue owner, escalation, traceability/comments); the four-value status vocabulary with Resolved and Closed distinct; the separation of rules (the Issue Management Plan) from the register; escalation thresholds set in the plan; lessons learned after resolution; and the licence permitting adaptation with attribution.
Quotable: "The Issue Log is a register (log file) used to capture and maintain information on all issues that are being formally managed." / "An issue is any unplanned event related to the project that has already happened and requires the intervention of the Project Manager (PM) or higher management." / "An Issue Log is used to document the identification, evaluation and assignment of issues and to trace all key decisions and planned actions." / "The structure of the Issue Log is defined in the Issue Management Plan." / "Create it as a standalone document or as a section within the Project Handbook." / "Customise the Issue Log to reflect any changes to the scales of urgency, impact and priority." / "Define which issues (depending on their category, urgency and impact) can be handled at the (Project) Management Layer and which ones need to be escalated." / "Specify the procedure for updating the Lessons Learned after an issue is resolved." / "Open: The issue has been identified and requires attention and, if possible, a resolution." / "Postponed: This status is set if resolving the issue is postponed due to other priorities." / "Resolved: This status indicates that all necessary actions are completed, and the issue is resolved." / "Closed: This status indicates that all work is completed and verified." / "The person accountable for resolving the issue." / "Whether or not the issue is to be escalated to the Directing or Steering Layers (Yes or No)." / "The ID(s) of the tasks (in the Project Work Plan) that implement the issue actions, and/or the IDs of related changes, risks or decisions (Log entries)." / "5=Very high, 4=High, 3=Medium, 2=Low, 1=Very low" / "Reproduction and reuse is authorised provided the source is acknowledged." / "Document licensed under CC BY 4.0 license"
Contested/time-bound: Its plan text (B.4) refers to a scale of "priority" that its log (B.9) does not carry as a field; B.9's scales are urgency, impact and size. Licensed CC BY 4.0; the PM² logo is excluded from reuse.

**[2] Project Management Institute - "Lexicon of Project Management Terms", Version 5.0 (last updated January 2026).** standards (glossary). **fetched-and-verified.**
`https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf`
Supports: PMI's definitions of an issue and of the issue log, the admission by name, and the broadest of the four definitional positions (a current condition that may have an impact).
Quotable: "issue. A current condition or situation that may have an impact on one or more objectives." / "issue log. A project artifact where information about issues is recorded and monitored."
Contested/time-bound: Licensed for personal use only, with an explicit no-AI-training notice: quoted briefly, never adapted.

**[3] Project Management Institute - "A Guide to the Project Management Body of Knowledge (PMBOK Guide)", Sixth Edition, errata (fifth printing).** standards (errata). **fetched-and-verified.**
`https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-6th-edition-5th-printing.pdf?v=5ec5b4d9-abb5-4d42-8542-8af75be7de3b`
Supports: That the PMBOK Guide names the issue log as a project document and, separately, a change log for change requests, without stating a rule for where the two overlap.
Quotable: "Issue log. Described in Section 4.3.3.3." / "New issues raised as a result of this process are recorded in the issue log." / "The change log is used to record all submitted change requests."
Contested/time-bound: The errata only. The PMBOK Guide itself is sold and was not read.

**[4] Association for Project Management - Glossary.** standards (glossary). **fetched-and-verified.**
`https://www.apm.org.uk/resources/glossary/`
Supports: APM's tolerance-based definition of an issue, its definition of the issue log, and that it treats "issue register" as a synonym.
Quotable: "A problem that is now breaching, or is about to breach, delegated tolerances for work on a project or programme. Issues require support from the sponsor to agree a resolution." / "A log of all issues raised during a project or programme, showing details of each issue, its evaluation, what decisions were made and its current status." / "The process by which issues can be identified and addressed to remove the threats that they pose." / "Issue register  See Issue log."
Contested/time-bound: No licence stated on the page.

**[5] Association for Project Management - "APM Body of Knowledge", 7th edition (consultation copy hosted by APM), section 4.3.5 Issue management.** standards (body of knowledge). **fetched-and-verified.**
`https://www.apm.org.uk/media/qpyau3pc/apm-body-of-knowledge-7th-edition-for-supporting-2025-consultation.pdf`
Supports: APM's issue-management process (log and analyse, escalate to the sponsor, assign actions, route baseline changes through change control, track to resolution); that issues differ from day-to-day problems; that prioritisation weighs scope, quality, time, cost and benefits; and two named barriers to issue management working.
Quotable: "Issues are differentiated from problems that are dealt with on a day-to-day basis by the project manager and team." / "There is often a tendency to mix up the identification, analysis and management of risks with issues. They are related but are not the same thing." / "When an issue is detected, it is logged in an issue register and analysis is performed quickly to understand the nature of the issue, its causes and impacts if it is not resolved." / "the relative priorities of scope, quality, time, cost and benefits" / "Issues are escalated to the sponsor, who may, in turn, escalate them to the governance board for resolution." / "Issues that result in changes to scope or any other part of the baseline plan are progressed through change control." / "a lack of time or reluctance from project professionals to identify and escalate issues early" / "an inability of the governance board to make an informed decision that addresses the root cause of the issue rather than treating the symptoms"
Contested/time-bound: The document marks itself "For use by APM individual and corporate members only": quoted briefly with attribution, adapted nowhere.

**[6] Association for Project Management - "APM Body of Knowledge", 7th edition, publisher's sample.** standards (sample). **fetched-and-verified.**
`https://www.apm.org.uk/media/k2zga0pa/ampbok7-sample.pdf`
Supports: nothing beyond [5]. Consulted; its contents list shows section 4.3.5 exists, and its excerpt stops before it, which is how one dimension concluded, wrongly, that the section was unreadable.

**[7] International Organization for Standardization - "ISO 21502:2020 Project, programme and portfolio management - Guidance on project management", first edition 2020-12, official free preview.** standards (preview). **fetched-and-verified.**
`https://cdn.standards.iteh.ai/samples/74947/d2f2b2e60a8249ab88240adc92be71ad/ISO-21502-2020.pdf`
Supports: ISO's definition of an issue, and that ISO treats issues management as a practice clause beside risk management. Nothing about whether ISO names an issue log, which is past the preview.
Quotable: "event that arises during a project (3.20) requiring resolution for the project to proceed" / "7.9 Issues management" / "7.9.2 Identifying issues" / "7.9.3 Resolving issues"
Contested/time-bound: The clause body is paywalled. Read once on 2026-09-23; a second fetch the same day returned 403.

**[8] AXELOS - PRINCE2 (2009 edition) Glossary of Terms, entries "Issue", "Issue Register" and "Issue Report", reproduced with AXELOS's permission by stakeholdermap.com.** standards (glossary reproduction). **fetched-and-verified.**
`https://www.stakeholdermap.com/prince2/prince2-glossary-I-impact.html`
Supports: PRINCE2's 2009 definitions: an issue as an event that has happened, the Issue Register, the register-and-report split, and request for change inside the issue concept.
Quotable: "A relevant event that has happened, was not planned, and requires management action." / "It can be any concern, query, request for change, suggestion or off-specification raised during a project." / "A register used to capture and maintain information on all of the issues that are being managed formally. The Issue Register should be monitored by the Project Manager on a regular basis." / "Copyright © AXELOS Limited 2012. All rights reserved. Material is reproduced with the permission of AXELOS"
Contested/time-bound: 2009 edition, superseded twice. AXELOS copyright; permission extends to that site, not to adaptation here.

**[9] stakeholdermap.com - "PRINCE2 Issue Register" template page, reproducing AXELOS material.** reference (template page). **fetched-and-verified.**
`https://www.stakeholdermap.com/project-templates/prince-2-issue-register.html`
Supports: The PRINCE2 Issue Register's column headers, including a date of last update distinct from the closure date, and its stated purpose.
Quotable: "The Purpose of the Issue Register is to capture and maintain information on all of the issues that are being formally managed." / "Copyright © AXELOS Limited 2009. All rights reserved."
Contested/time-bound: Headers only; no field definitions on the page. AXELOS copyright.

**[10] PeopleCert - "PRINCE2 7 Issues: not every issue equals a change".** vendor (examination institute). **fetched-and-verified.**
`https://www.peoplecert.org/news-and-announcements/prince2-7-issues`
Supports: PRINCE2 7's forward-looking definition of an issue, its issue types, and the rule that every change starts as an issue.
Quotable: "In PRINCE2 7, the broad definition of issues is “anything that could affect the project”." / "for example, issues can be either a problem, a concern, a business opportunity, a request for change, or something off-specification." / "Not all issues result in changes. But all changes start as issues."
Contested/time-bound: PRINCE2 7 (2023). PeopleCert owns PRINCE2 and examines it, so this is the method owner describing its own change.

**[11] Frank Turley (EMPII Group) - "Issues", prince2.wiki.** practitioner. **fetched-and-verified.**
`https://prince2.wiki/practices/issues/`
Supports: Two PRINCE2 definitions stated on one page, and the rule that an uncertain issue belongs on the risk register.
Quotable: "Any expectation different from the baselines is called an issue in PRINCE2." / "An issue is an event relevant to the project that requires project management consideration." / "When categorizing issues, it’s helpful to check if the issue is actually a risk. Risks are uncertain, and if this is the case, the issue should be transferred to the risk register."
Contested/time-bound: Licensed Creative Commons Attribution per the site's footer; PRINCE2 trademarks used with AXELOS's permission.

**[12] Frank Turley (EMPII Group) - "Issue register", prince2.wiki.** practitioner. **fetched-and-verified.**
`https://prince2.wiki/management-products/project-log/issue-register/`
Supports: The register holds formal issues; a risk becomes an issue when it materializes; review of the register is neglected under load; lessons from resolved issues; and linking an issue to its risk.
Quotable: "The primary purpose of the issue register is to capture and maintain information about all formal issues that require attention or decision-making." / "A risk becomes an issue once it materializes. Some issues may even introduce new risks." / "This task often gets neglected when project managers get busy" / "Capture lessons learned from resolved issues" / "connecting an issue report to a specific risk"
Contested/time-bound: Creative Commons Attribution.

**[13] Frank Turley (EMPII Group) - "Issue report", prince2.wiki.** practitioner. **fetched-and-verified.**
`https://prince2.wiki/management-products/issue-report/`
Supports: The issue report as the detailed assessment of an issue needing formal handling, distinct from the register row, and its impact analysis across performance aspects.
Quotable: "An issue report provides a detailed description and impact assessment of one or more issues that require formal handling." / "Not all entries in the issue register require a standalone issue report"
Contested/time-bound: Creative Commons Attribution. Its list of performance aspects is PRINCE2 7's.

**[14] Projex Academy - "PRINCE2 7 Issues and Change Control" (dated 3 April 2023).** vendor (training provider). **fetched-and-verified.**
`https://www.projex.com/prince2-7-issues/`
Supports: nothing in this bundle. Consulted, and recorded as an attribution hazard: titled for PRINCE2 7, dated before its release, and written in sixth-edition terms.

**[15] Duraideivamani Sankararajan and N. K. Shrivastava - "Risks vs. issues", PM Network 26(6), pp. 28-29 (Project Management Institute, June 2012).** practitioner (professional magazine). **fetched-and-verified.**
`https://www.pmi.org/learning/library/risks-vs-issues-project-failure-2328`
Supports: Two practitioners' account of the risk and issue boundary, what the register tracks, moving a materialized risk to the log, and their disagreement on cadence and on the register's name.
Quotable: "Risk is an event that has not happened yet but may; an issue is something that already has happened." / "Issues are recorded separately from risks in the issues register. In it, we track the issue, issue owner, open date, target date for closure, with whom the issue is pending, intermediate updates available on issue closure, criticality of the issue and its impact." / "I call the issue register the “issue log” because it denotes logging of something that already has happened." / "When a risk is materialized, I move it to the issue log and the person who was assigned to the risk now works on the issue." / "There is no such thing as “mitigating an issue.” Rather, issues are resolved." / "We review the open issues on the issue log every week." / "Issues recorded in the issues register should be discussed almost every day"
Contested/time-bound: The site refused scripted requests after the first read; the cached copy was confirmed to be a raw page extraction.

**[16] Northern Ireland Civil Service, Centre of Expertise for Programme and Project Management (Department of Finance) - "Issue Log", Generic PPM Templates, V1.0.** primary (government template). **fetched-and-verified.**
`https://www.finance-ni.gov.uk/sites/default/files/publications/dfp/Programme%20and%20project%20management%20templates%20-%20issue%20log.DOC`
Supports: A public body's issue log derived from PRINCE2, with a date of last update among its columns and changes recorded on the issue log.
Quotable: "based on the PRINCE2 recommended issue log" / "The purpose of the project issue log is to summarise all of the project Issues, their analysis and status." / "Whereas risks may occur, issues have already happened, are in the 'here and now' and need to be dealt with" / "Issues, including those raised as changes under the project change control mechanism, should be recorded on the issue log."
Contested/time-bound: No licence stated in the document. Structure evidence only.

**[17] Tasmanian Government, Department of Premier and Cabinet (Office of eGovernment) - "Project Management Guidelines", Version 7.0 (July 2011), section 6 Issues management.** primary (government guidelines). **fetched-and-verified.**
`https://www.dpac.tas.gov.au/__data/assets/pdf_file/0029/108992/Tasmanian_Government_Project_Management_Guidelines_V7_0_July_2011_2.pdf`
Supports: A government issues register structure and the rule that an unresolvable issue may become a risk.
Quotable: "A Project Issues Register is basically a form, often a table, for systematically recording issues." / "status, usually open or closed" / "If an issue cannot be resolved, it could become a risk"
Contested/time-bound: 2011. Carries a disclaimer limiting reliance to Tasmanian Government agencies and no reuse licence. Structure evidence only.

**[18] Connecticut Department of Social Services, Enterprise Program Management Office - "Project Issue Log", v1.13.** primary (government template). **fetched-and-verified.**
`https://portal.ct.gov/-/media/Departments-and-Agencies/DSS/CT-METS/Library/General/CTDSSIssueLogv113.pdf`
Supports: A five-level named impact scale, a Material/Non-Material priority, and an Escalated status value.
Quotable: "The Issue Log is used in the identification, evaluation, management, and tracking to resolution of issues that could have an impact on the success of a project" / "1 - Low; easily mitigated by an individual or team." / "5 - Catastrophic; Impact to Cost/Schedule/Scope resulting in project failure." / "The issue has a block that the project team cannot overcome and has been escalated to the Project Sponsor and/or Executive Leaders for assistance."
Contested/time-bound: No licence stated. Structure evidence only.

**[19] Connecticut Department of Social Services (CT-METS) - "Issue Management Plan", v1.1.** primary (government plan template). **fetched-and-verified.**
`https://portal.ct.gov/-/media/Departments-and-Agencies/DSS/CT-METS/Library/General/CTDSSIssueManagementPlanv11.pdf`
Supports: The fullest published lifecycle (identify and assess, plan and verify, monitor, confirm and close); a worked logging threshold; a weekly review with priority triage; and closure verified by the issue's originator.
Quotable: "The event cannot be resolved at the project team level within three days" / "Issue reviews are scheduled weekly" / "Review priority is given to high severity and escalated issues" / "As notified by the issue owner, team or Project Manager, the issue originator reviews a resolved issue and verifies it can be closed"
Contested/time-bound: Sets the final status to "Resolved" with a separate closed date, rather than a Closed status. No licence stated.

**[20] Washington State Office of Financial Management - "Issue Management Log" template.** primary (government template). **fetched-and-verified.**
`https://results.wa.gov/sites/default/files/issueTrackingTemplate.xls`
Supports: An audit-context issue log that handles escalation by changing a Decision-Maker column rather than a status.
Quotable: "This person is responsible for identifying issues, assigning for resolution, monitoring for completion, and closing issues." / "Change this column if the issue is escalated to the deputy" / "Note whether the issue is open or closed."
Contested/time-bound: Written for performance-audit issue tracking. No licence stated.

**[21] Colorado College, Office of Information Technology Services - "ITS Project Management Office (PMO) Playbook", 2024-2025.** practitioner (university PMO). **fetched-and-verified.**
`https://www.coloradocollege.edu/offices/its/PMO-Playbook-2024.pdf`
Supports: An escalation ladder by role, triggered by inability to resolve, with no timer.
Quotable: "If the delay cannot be resolved through the Project Manager's direct engagement, the Project Manager should then escalate the issue to the Functional Lead" / "If the issue remains unresolved after the Director of PMO's involvement and if there is no response from the Functional Lead, the Director of PMO will escalate the issue to the CIO" / "Issue Log: A documented list of project issues, tracking their status and resolution"

**[22] University of Essex, Strategic Project Delivery - "Risk and issue management".** practitioner (university PMO). **fetched-and-verified.**
`https://www.essex.ac.uk/staff/strategic-project-delivery/risk-issue-management`
Supports: Logging an issue at once, and reviewing issues through existing governance rather than a separate meeting.
Quotable: "Issues should be logged immediately" / "an issue is either a risk with near 100% probability, or one that has already happened" / "Progress of the issue should be reviewed regularly through the project board or steering group"

**[23] Elizabeth Harrin - "5 Scenarios where you should escalate a project issue", Rebel's Guide to Project Management.** practitioner. **fetched-and-verified.**
`https://rebelsguidetopm.com/issue-escalation/`
Supports: Escalation as a request for help, presented factually with a proposed solution.
Quotable: "Stay factual, talk about the implications for the project" / "Go to them with a solution in mind"

**[24] Onplana (Devsoft Solutions) - "An Escalation Framework Project Managers Can Actually Use".** vendor (software company blog). **fetched-and-verified.**
`https://onplana.com/blog/escalation-framework-pm`
Supports: A worked model of escalation by aging clock, and what an escalation record holds. Cited as a vendor's model, adopted by no named organization.
Quotable: "The aging clock starts on the day the issue is first logged, not the day the PM decides it's serious" / "The issue, the date first logged, the date escalated, the decision made, the authority who made it, and the outcome"

**[25] Mosaic Projects - "Issues Management", White Paper WP1089.** practitioner. **fetched-and-verified.**
`https://mosaicprojects.com.au/WhitePapers/WP1089_Issues_Management.pdf`
Supports: A warning against blame in resolving issues, and escalation of issues the team cannot resolve.
Quotable: "adding additional layers of complexity by introducing conflict, blame or other emotions will not help the resolution of the issue" / "if the issue cannot be resolved by the project team in a reasonable timeframe, it should be escalated to the appropriate management level for resolution" / "Unresolved issues will damage the project"
Contested/time-bound: Prescriptive. Not an account of a log actually misused.

**[26] Rocketlane - "RAID Management: Complete Guide for PS Teams".** vendor (software company blog). **fetched-and-verified.**
`https://www.rocketlane.com/blogs/raid-management`
Supports: Why ownership goes missing, and an aging rule for items that stop moving.
Quotable: "Nobody wants to create conflict at kickoff by assigning ownership of something potentially difficult" / "Never let a RAID item go more than two reviews without movement"
Contested/time-bound: A vendor's prescription, not a measured finding.

**[27] Project Management Pathways - "Risk register versus issue log: what goes in each, and the moment one becomes the other".** practitioner. **fetched-and-verified.**
`https://projectmanagementpathways.com/articles/risk-register-vs-issue-log/`
Supports: The moment a risk becomes an issue, closing the risk as occurred rather than deleting it, and linking the two entries.
Quotable: "A risk becomes an issue the moment it happens" / "not deleted and not quietly marked withdrawn" / "keeps a link back to the risk it came from, and writes a note on both entries recording the conversion" / "it closes as occurred, which is what preserves the evidence that the event was foreseen"

**[28] Elizabeth Harrin - "RAID logs in project management: How to actually use one", Rebel's Guide to Project Management.** practitioner. **fetched-and-verified.**
`https://rebelsguidetopm.com/raid-in-project-management/`
Supports: That a RAID log's issues are the same thing an issue log holds, and that practitioners split on whether changes are managed as issues.
Quotable: "Things that have happened and are causing a problem on your project get added to the issue log, which is one part of the RAID log" / "Risks are potential issues, so if they come to pass, you'll create a new entry on the Issues log" / "Some people also manage changes to the project as issues, but personally, I don't"

**[29] Asana - "RAID Log: Track Risks, Assumptions, Issues & Decisions".** vendor (resource page). **fetched-and-verified.**
`https://asana.com/resources/raid-log`
Supports: RAID's definition of an issue, and a standalone issue log as the formalized form of RAID's issues.
Quotable: "Issues are problems that occur during a project that you did not anticipate. Unlike risks, which you plan for in advance, issues pop up unexpectedly and require immediate attention" / "An issue log can help formalize this tracking"

**[30] Eleco (PM3) - "What Is A Decision Log? The Essential Tool For Project Managers".** vendor (knowledge centre). **fetched-and-verified.**
`https://eleco.com/pm3/knowledge-centre/decision-log/`
Supports: What a decision log and an action log each hold. It never mentions an issue log, so any boundary drawn from it is this library's reasoning.
Quotable: "A decision log records what decisions were made, why they were made, and who made them" / "decision logs capture choices, whereas action logs track execution"

**[31] BrainBOK - "Impediments Backlog", Agile artifacts guide.** practitioner (study guide). **fetched-and-verified.**
`https://www.brainbok.com/guide/agile/agile-artifacts/impediments-backlog`
Supports: The difference in scope between an agile team's impediments backlog and a project issue log.
Quotable: "An impediments backlog is a list of impediments, obstacles, or blockers that hinder progress in a project" / "The impediments backlog is more specific to immediate team impediments, while the issue log is a comprehensive record of all project-related problems"

**[32] Ken Schwaber and Jeff Sutherland - "The 2020 Scrum Guide".** primary (framework definition). **fetched-and-verified.**
`https://scrumguides.org/scrum-guide.html`
Supports: That Scrum names impediments only as something the Scrum Master causes to be removed, and prescribes no log of them.
Quotable: "The Scrum Master serves the Scrum Team in several ways, including" / "Causing the removal of impediments to the Scrum Team's progress"
Contested/time-bound: Licensed CC BY-SA 4.0.

**[33] Wikipedia contributors - "Issue tracking system".** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Issue_tracking_system`
Supports: A distinction between categories of software tracking tool. It does not compare a tracker with a project issue log, so the bundle's bug-tracker boundary is labelled as its own judgment.
Quotable: "In bug trackers, issues are generally quality or feature related to the software codebase"

**[34] Rosemet - "Issue Log Instructions".** practitioner (training provider). **fetched-and-verified.**
`https://www.rosemet.com/issue-log-instructions/`
Supports: A published field list with no risk-origin, confirmer or last-updated field, and lessons learned named as a use of the log rather than a field in it.
Quotable: "lessons-learned database"

**[35] Plane - "What is an issue log? How to maintain one in project management".** vendor (software company blog). **fetched-and-verified.**
`https://plane.so/blog/what-is-an-issue-log-how-to-maintain-one-in-project-management`
Supports: A second published field list with free-text resolution notes and no confirmer or last-updated field.
Quotable: "A unique identifier for referencing the issue in meetings, reports, and communications without ambiguity" / "A brief record of what was done to fix the issue"

**[36] Mastt - "Issue Log (Word, Excel)".** vendor (template page). **fetched-and-verified.**
`https://www.mastt.com/resources/issue-log`
Supports: One published field list that assesses impact against named dimensions, and a category field.
Quotable: "A summary of how the issue affects time, cost, or project quality" / "Classification such as design, contract, safety, scheduling, or quality"

**[37] Smartsheet - "Free Issue Tracking Templates".** vendor (template page). **fetched-and-verified.**
`https://www.smartsheet.com/content/issue-tracking-templates`
Supports: A published template carrying a last-updated date distinct from open and close dates.
Quotable: "fields to enter the project name, manager, application or site, and the last updated date"

**[38] Jason Westland - "What Is an Issue Log? Templates, Tips and More", ProjectManager.com (10 April 2025).** vendor (software company blog). **fetched-and-verified.**
`https://www.projectmanager.com/blog/what-is-an-issue-log`
Supports: The failure of an issue with no owner.
Quotable: "If the issue doesn't have an owner, it's likely never to get resolved." / "a simple list or spreadsheet that helps managers track the issues that arise in a project and prioritize a response to them"

**[39] UK Government, Government Project Delivery - "The Teal Book", Part E, Chapter 21: Issue management.** primary (government guidance). **url-confirmed-not-read.**
`https://projectdelivery.gov.uk/teal-book/home/part-e-planning-and-control/chapter-21-issue-management/`
Supports: nothing in this bundle. The page exists and is relevant; it refused every raw fetch, and a retrieval tool's summary of it is not evidence.

**[40] AXELOS - PRINCE2 manuals (PRINCE2 6th edition 2017, PRINCE2 Agile 2016 Appendix A.12 and A.13, PRINCE2 7 2023).** primary (method manuals). **not-retrieved.**
`https://publications.axelos.com/PRINCE2Agile2016/content.aspx?page=pra_191&showNav=true&expandNav=true`
Supports: nothing in this bundle. Subscription-gated; PRINCE2 enters through [8], [10] and [11]-[13].

**[41] Project Management Institute - "Take it to the top", PMI learning library article on escalating project problems.** practitioner. **url-confirmed-not-read.**
`https://www.pmi.org/learning/library/escalate-issue-successful-solution-team-4345`
Supports: nothing in this bundle. Returned 403 to every attempt.
