# status-report research log

Researched 2026-08-07 across six parallel dimensions: whether a standard specifies this artifact at all,
the provenance and definition of RAG, structure in published templates, the empirical literature on
reporting honesty, boundaries against adjacent documents, and failure modes. **30 sources**, **all 30
fetched-and-verified**, carrying **143 verbatim quotable phrases**. Retrieval status is recorded per source
in the three-token vocabulary the library gates
([ADR 0029](../../docs/internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md)), and only
`fetched-and-verified` sources are quoted.

**How to read this log.** A `Supports:` clause says what the bundle is allowed to rest on that source for.
A `Quotable:` phrase was read verbatim on the page. If a claim in the companion is not covered by some
entry's `Supports:` clause here, the claim has no home and must be cut, not justified after the fact.

**Generated, then corrected by hand.** The entries below were produced by
[`tools/gen-research-log.py`](../../tools/gen-research-log.py) from the fan-out's own output, which is why
no quotation here was retyped. One correction the tool could not make: the PRINCE2 wiki's highlight-report
page is reachable at two different **paths**, and the tool normalises hosts, schemes and trailing slashes
but not path aliases, so it produced two entries for one page. They were merged by hand and the merge is
stated in the surviving entry. That limit is now known and worth a fixture if it recurs.

---

## Honest framing: the six things this bundle has to say

**1. Exactly one methodology specifies this document. Everything else is folk practice.** PRINCE2's
**Highlight Report** is a named management product with a defined producer, recipient, cadence rule and
section list: "The highlight report provides a regular update on stage progress, prepared by the project
manager for the project board" [5]. That is the only fully specified status-report artifact this research
found. It matters that the reachable text is a community mirror rather than AXELOS's own manual, which is
paywalled, and the entry says so.

**2. The UK government's own project standard deliberately declines to specify one.** GovS 002, the
cross-government functional standard for project delivery, states a principle rather than a document: a
reporting framework "should be defined and established to meet the needs of the identified report
recipients", and its illustrative list of report types is charts, not sections. Even its one mandatory
clause defers the format to a separate authority rather than fixing it. **A live, primary, public standard
looked at this document and chose not to define it**, which is a stronger finding than silence would be.

**3. PMBOK could not be retrieved, for the second time in this library.** The `business-case` bundle named
PMBOK a key source, could not retrieve it, and stated nothing about it. The same happened here: PMBOK sits
behind PMI membership and no free full text was reachable. A secondary definition of "work performance
reports" circulates [30][18] and **this bundle rests nothing on it**. Two bundles, same gap, same handling.

**4. The best-documented RAG scheme in existence defines the colours that are easy and refuses the ones
that are hard.** The Infrastructure and Projects Authority's Delivery Confidence Assessment [1], echoed
verbatim in its own annual report [2], gives prose criteria for Red, Amber and Green, separately across
seven contributing elements, so amber is not one definition but roughly eight. And then it says: "Definitions
have only been given for Red, Amber and Green; Amber-Red and Amber-Green can be used to reflect a status
that lies in between" [1]. **The two intermediate colours, which do the most delicate signalling work on a
five-point scale, are explicitly left undefined by the most detailed published scheme there is.** PRINCE2's
own highlight-report documentation carries no threshold definition either, only a caution to "be cautious
with traffic light indicators to ensure clarity" [5]. No source read establishes who invented the
convention; the honest trace is to current ownership, not to an inventing document.

**5. This document type has the strongest empirical evidence base of any bundle in this library, and it
says the reports are biased.** Keil, Smith, Iacovou and Thompson's "The Pitfalls of Project Status
Reporting" [12] synthesises 14 studies over 15 years. Its central number: "we reviewed the records of **56
experienced software project managers** and found that project managers write biased reports **60% of the
time** and that their bias is **more than twice as likely to be optimistic** than pessimistic" [12]. That
is a records review of practitioners, not a survey of students, and the distinction is preserved here
because the same research programme also includes a 60-student laboratory study and the bundle must not
flatten the two into one undifferentiated "research shows". **The 2007 primary paper behind that statistic
was not read**; it is attributed through the 2014 synthesis and the log says so rather than implying a
direct reading. This is the opposite of the position most bundles in this library are in, where every
circulating number turned out untraceable.

**6. Four of the six sections this bundle was specified to ship title nothing in any published template.**
Five vendor templates were read in full [6][7][8][9][10][11]. **No source uses the word "RAG" as a heading
at all**, nor the compound titles "Summary and RAG Status", "Risks and Next Steps", "Decisions Needed" or
"Detailed Breakdown". This is the third consecutive bundle where the spec's titles failed against the
corpus, and the sections are retaken from what templates actually title.

## The family contract's central claim, tested and not found

The `communication-docs` contract makes the **no-new-facts rule** this family's whole point: every figure
must be read from somewhere with more authority, and the document owns none of its own facts. **No source
found states it.** The search was deliberate and its terms are recorded in "Sought and not found" below.
PMBOK's work-performance chain supports "compiled from elsewhere" and stops well short of a prohibition.

**This is the third contract claim in three consecutive bundles that no source supports**, after the
`process-docs` contract's retro-versus-postmortem harm claim and its risk-register destination. The pattern
is now worth naming in its own right: **this library's family contracts are written before their members
are researched, and the research keeps finding their justifications unsourced.** The rule itself is good and
the bundle keeps it. It is presented as this library's own contribution, and section 4 of the companion says
so plainly.

**The dashboard boundary needs its own care inside this library.** The external framing distinguishes a
report from a dashboard as periodic narration versus a live visual instrument [15]. That does not survive
contact with this repository, because its `kpi-dashboard` bundle is itself a static markdown document that
**defines** a dashboard rather than being one [19]. The distinction that does survive: the dashboard bundle
specifies which metrics exist and how each is defined and owned; the status report narrates what happened
against those metrics in one period, for one audience, and draws its numbers from them rather than defining
new ones. That reframing is this library's synthesis, not a quotation, and the companion labels it.

## Format verdict (ADR 0028)

**One format.** PRINCE2's Highlight Report is a named artifact rather than a second shape of this one, and
admitting it as a format would repeat the mistake ADR 0028 exists to prevent: its author presents it as a
PRINCE2 management product, not as a status-report variant. It is taught as the canonical spine instead.

## Sources

### RAG: provenance, and whether anyone defines amber

**[1] Infrastructure and Projects Authority (UK government, reporting to HM Treasury and Cabinet Office) - "Project Assurance Reviews: Delivery Confidence Guide for Review Teams".** primary. **fetched-and-verified.**
`https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/638436/delivery_confidence_guide_for_review_teams.pdf`
Supports: The central question: this is the most detailed published definition of RAG thresholds found, and it explicitly declines to define the amber-adjacent categories.
Quotable: "Delivery Confidence is the confidence in the project or programme's ability to deliver its aims and objectives: within the timescales, within the cost envelope, and to the quality requirements including the delivery of benefits..."
Quotable: "the Review Team's professional judgement of the likelihood of the project or programme succeeding even though there may be no definitively clear evidence either way"
Quotable: "Green: Successful delivery of the project/programme to time, cost and quality appears highly likely and there are no major outstanding issues that at this stage appear to threaten delivery."
Quotable: "Amber: Successful delivery appears feasible but significant issues already exist requiring management attention. These appear resolvable at this stage and, if addressed promptly, should not present a cost/schedule overrun."
Quotable: "Red: Successful delivery of the project/programme appears to be unachievable. There are major issues which at this stage do not appear to be manageable or resolvable. The project/programme may need re-baselining and/or overall viability re-assessed."
Quotable: "Definitions have only been given for Red, Amber and Green; Amber-Red and Amber-Green can be used to reflect a status that lies in between."
Quotable: "Review Teams should remember that the Delivery Confidence assessment is not a calculation and these elements are not the only factors that should be considered when making an assessment of Delivery Confidence."
Quotable: "When making their Delivery Confidence assessment Review Teams are not expected to consider every scenario that might affect a project's progress but to reasonably extrapolate from the project's past progress, current status and declared plans whether a successful outcome will be achieved."

**[2] GOV.UK / Infrastructure and Projects Authority - "Infrastructure and Projects Authority Annual Report 2023-24" (Annex A).** primary. **fetched-and-verified.**
`https://www.gov.uk/government/publications/infrastructure-and-projects-authority-annual-report-2023-24/infrastructure-and-projects-authority-annual-report-2023-24-html`
Supports: Confirms the same five-point DCA scale (Green / Amber-Green / Amber / Amber-Red / Red) and the same prose definitions are still current government practice, and that a DCA is described as a snapshot judgement, not a calculation.
Quotable: "Successful delivery of the project on time, budget and quality appears highly likely and there are no major outstanding issues that at this stage appear to threaten delivery significantly."
Quotable: "Successful delivery appears feasible but significant issues already exist, requiring management attention. These appear resolvable at this stage and, if addressed promptly, should not present a cost/schedule overrun."
Quotable: "Successful delivery of the project appears to be unachievable. There are major issues with project definition, schedule, budget, quality and/or benefits delivery, which at this stage do not appear to be manageable or resolvable."

**[3] National Audit Office - "Delivering major projects in government: a briefing for the Committee of Public Accounts".** primary. **fetched-and-verified.**
`https://www.nao.org.uk/briefings/delivering-major-projects-in-government-a-briefing-for-the-committee-of-public-accounts/`
Supports: Published criticism (indirect): the UK's own spending watchdog flags that RAG/DCA ratings are hard to validate against outcomes because underlying measures are inconsistent, and that ratings do not reliably improve as projects mature.
Quotable: "it is difficult to tell whether performance is improving without reliable and consistent measures"
Quotable: "Uncertainty should reduce through the project lifecycle but not all project ratings improve over time"

**[4] Association for Project Management (APM, UK chartered body) - "RAG status: using the tool the best way".** practitioner. **fetched-and-verified.**
`https://www.apm.org.uk/blog/rag-status-using-the-tool-the-best-way/`
Supports: Direct confirmation that a named professional body treats RAG threshold definition as an organisational responsibility, not something the standard itself specifies, and documents that non-definition is a common, named failure mode. Also names several published RAG variants.
Quotable: "the status has not been defined or is not used consistently, either at a project or an organisational level"
Quotable: "the RAG needs to be clearly defined, it must be communicated and consistently applied"

**[5] PRINCE2 Wiki (unofficial community mirror of PRINCE2 management products) - "Highlight report".** practitioner. **fetched-and-verified.**
`https://prince2.wiki/management-products/reports/highlight-report/`
Supports: Negative finding: even in a page dedicated to describing PRINCE2's own highlight-report product (which carries RAG indicators), there is no threshold definition, only a caution to use traffic lights carefully. ALSO REACHED AT AN ALIAS PATH (/management-products/highlight-report/), merged by hand: Q2: names and defines the Highlight Report as a distinct, formally-specified PRINCE2 management product, separate from a generic status report or progress report - its audience is the project board, its cadence is set in the communication management approach, and its purpose is manage-by-exception, not raw activity narration.
Quotable: "be cautious with traffic light indicators to ensure clarity"

### Structure in published templates
Quotable: "The highlight report provides a regular update on stage progress, prepared by the project manager for the project board."
Quotable: "kept simple and focused, providing a clear one-page overview of the stage's progress"
Quotable: "manage by exception between stage boundaries, ensuring they stay informed without unnecessary intervention"
Quotable: "The frequency and format of this report are defined in the communication management approach."

**[6] Asana - "Status report template".** vendor. **fetched-and-verified.**
`https://asana.com/templates/status-report`
Supports: Verbatim section/field list for a status-report template, plus cadence variants (daily/weekly/monthly/quarterly) as a first-class distinction
Quotable: "The report name"
Quotable: "Specific project details"
Quotable: "A status tag indicating project health"
Quotable: "A summary of the project's current status"
Quotable: "Specific accomplishments the team has achieved"
Quotable: "Current project blockers"
Quotable: "The next steps"
Quotable: "Daily status reports"
Quotable: "Weekly status reports"
Quotable: "Monthly status reports"
Quotable: "Quarterly status reports"

**[7] ProjectManagementDocs.com - "Project Status Report" template.** practitioner. **fetched-and-verified.**
`https://www.projectmanagementdocs.com/template/project-monitoring-and-controlling/project-status-report/`
Supports: Full verbatim field structure of a fixed-format downloadable status report template, including the only 'Risks', 'Metrics'-adjacent (KPI), and change-request fields found in the corpus
Quotable: "Project Status Summary"
Quotable: "Percent Complete:"
Quotable: "Scope"
Quotable: "Schedule"
Quotable: "Cost"
Quotable: "Risks"
Quotable: "Quality"
Quotable: "Worked Planned Last Week"
Quotable: "Work Completed Last Week"
Quotable: "Work Planned for Next Week"
Quotable: "Open Issues"
Quotable: "Open Risks"
Quotable: "Deliverables and Milestones"
Quotable: "Open Change Requests"
Quotable: "Key Performance Indicators (KPI's)"
Quotable: "Schedule Variance (SV):"
Quotable: "Schedule Performance Index (SPI):"
Quotable: "Cost Variance (CV):"
Quotable: "Cost Performance Index (CPI):"

**[8] ProjectManager.com - status report guide and worked example.** vendor. **fetched-and-verified.**
`https://www.projectmanager.com/guides/status-report`
Supports: Verbatim core template sections plus a worked example's additional headings, including the only 'Key Accomplishments' and 'Action Items' matches in the corpus
Quotable: "General Project Info"
Quotable: "General Status Info"
Quotable: "Milestone Review"
Quotable: "Project Summary"
Quotable: "Issues and Risks"
Quotable: "Project Metrics"
Quotable: "Key Accomplishments"
Quotable: "Action Items"
Quotable: "Upcoming Work"
Quotable: "Project Deliverables"
Quotable: "Project Health"

**[9] TeamGantt - "Project Status Report Template".** vendor. **fetched-and-verified.**
`https://www.teamgantt.com/project-status-report-template`
Supports: Verbatim, fully-ordered section list for a single weekly status report template, including the only exact 'Summary' heading match in the corpus
Quotable: "Introductory note"
Quotable: "Summary"
Quotable: "Overall project timeline completion"
Quotable: "Budget status"
Quotable: "Upcoming tasks and milestones"
Quotable: "Action items"
Quotable: "Project risks, issues, and mitigation plans"

**[10] monday.com - "Project status report template" blog.** vendor. **fetched-and-verified.**
`https://monday.com/blog/project-management/project-status-report-template/`
Supports: Verbatim article/template structure showing audience-specific variants (executive dashboard vs department vs agile vs team) and their distinct field sets
Quotable: "Project summary and goals"
Quotable: "Timeline and milestone tracking"
Quotable: "Budget and resource status"
Quotable: "Risk and issue management"
Quotable: "Key achievements"
Quotable: "Upcoming activities"
Quotable: "Weekly status update templates"
Quotable: "Monthly project progress templates"
Quotable: "Executive status report templates"
Quotable: "Team status report templates"
Quotable: "Portfolio status report templates"
Quotable: "Executive dashboard report template"
Quotable: "Project health indicators"
Quotable: "Budget variance charts"
Quotable: "Milestone tracking"
Quotable: "Performance metrics"
Quotable: "Agile project status template"
Quotable: "Department status report template"

**[11] Smartsheet - "Weekly Status Report Templates" listicle.** vendor. **fetched-and-verified.**
`https://www.smartsheet.com/content/weekly-status-report-templates`
Supports: Evidence that published templates come in many named audience/team-specific variants (executive, IT, HR, agile sprint, scrum sprint), corroborating the sizes-vary-by-audience finding; does not supply a single template's field structure
Quotable: "Weekly Project Status Report Template"
Quotable: "Weekly Executive Status Report Template"
Quotable: "Weekly IT Status Report Template"
Quotable: "Weekly HR Status Report Template"
Quotable: "Weekly Agile Sprint Status Report Template"
Quotable: "Weekly Scrum Sprint Status Report Template"
Quotable: "What Is Included in a Weekly Status Report?"

### The empirical literature on status reporting honesty (Keil, Snow, Smith, and colleagues on the mum effect, deaf effect, and watermelon reporting)

**[12] Mark Keil, H. Jeff Smith, Charalambos L. Iacovou, Ronald L. Thompson, "The Pitfalls of Project Status Reporting," MIT Sloan Management Review, Spring 2014, Vol. 55 No. 3, pp. 56-64.** practitioner. **fetched-and-verified.**
`http://marketing.mitsmr.com/PDF/MITSMR-The-Pitfalls-of-Project-Status-Reporting.pdf?cid=1`
Supports: Synthesis of 14 empirical studies by Keil and collaborators (1999-2013) on IT/software project status misreporting; this is the single richest available source and names the primary studies with full citations. Two of those named citations are load-bearing for this bundle and are recorded here so nothing rests on this log's narrative alone. The 60 percent figure is credited in this synthesis to Snow, A.P., Keil, M., and Wallace, L., "The Effects of Optimistic and Pessimistic Biasing on Software Project Status Reporting", Information and Management 44, no. 2 (March 2007), 130-141, which THIS RESEARCH DID NOT READ; the attribution runs through the synthesis. The same synthesis also names a laboratory study of 60 students evaluating a hypothetical negative report (Cuellar, Keil, Johnson 2006), which is why this bundle keeps practitioner and student evidence distinct rather than flattening them.
Quotable: "In one study, we reviewed the records of 56 experienced software project managers and found that project managers write biased reports 60% of the time and that their bias is more than twice as likely to be optimistic (that is, to make things look better than they really are) than pessimistic."
Quotable: "I wrote a lot of reports. I escalated things as much as I could, but in the end they ... took me out to lunch and said, 'We really appreciate what you've done, but we really won't be needing you anymore.'"
Quotable: "We were trying to quantify and tell them, convey the seriousness of the situation. And, I don't think they believed that it would be that serious. ... It was very frustrating for me - a little demoralizing."
Quotable: "reporting negative status information would probably be "career suicide, to be honest. ... I'm going to go to the executive VP of the company and tell him that this is a worthless project and he should pull the plug on it?""
Quotable: "Many managers were not willing to accept the major problems transpiring in the project. ... But because this was such a high-level project, the pressure to go on with it was high."
Quotable: "our research suggests that the stronger the perceived power of the sponsor or the project leader, the less inclined subordinates are to report accurately"

**[13] Marc Löffler, "Watermelon Reporting in Project Management," PMHut, February 20, 2013.** vendor. **fetched-and-verified.**
`https://pmhut.com/watermelon-reporting-in-project-management`
Supports: Earliest dated, byline-attributed web use of 'watermelon reporting' found in this search; page itself does not claim to coin the term or cite an earlier origin

**[14] Rob Thomsett, "Thinking about Red Projects," LinkedIn, September 15, 2021.** practitioner. **fetched-and-verified.**
`https://www.linkedin.com/pulse/thinking-red-projects-rob-thomsett`
Supports: Shows a veteran consultant sometimes credited with coining 'watermelon' calling it 'the old joke about the Watermelon project' rather than claiming authorship, which undercuts the single-coiner attribution
Quotable: "Oh! The project is Green on the outside and Red on the Inside"
Quotable: "the old joke about the Watermelon project"

### DIMENSION 5: Where does a status report end and something else begin (comparative corpus vs. dashboard, progress/highlight report, executive summary, steering-group paper; cadence/audience guidance; the 'no new facts' claim)

**[15] PPM Express (vendor blog) - "Project Status Reports vs. Dashboards: Which is Right for You".** vendor. **fetched-and-verified.**
`https://www.ppm.express/blog/project-status-reports-vs-dashboards-which-is-right-for-you`
Supports: The status-report-vs-dashboard distinction (Q1): reports are periodic and comprehensive, dashboards are live/real-time and visual; reports double as an archive, dashboards support live monitoring.
Quotable: "Project status reports are comprehensive documents that detail a project's progress, challenges, and next steps."
Quotable: "A project status dashboard is a visual representation of real-time project data."
Quotable: "typically shared periodically (e.g., weekly or monthly)"
Quotable: "archive for project milestones and challenges"

**[16] winningpresentations.com - "Steering Committee Presentation: How to Drive Decisions Instead of Status Updates".** practitioner. **fetched-and-verified.**
`https://winningpresentations.com/steering-committee-presentation/`
Supports: Q2: draws an explicit structural line between a status update and a steering-committee/decision paper - status updates report what happened and cover every metric; decision sessions open with an ask and narrow to the evidence that supports one recommendation. This is the clearest named-source boundary found between status report and steering-group paper.
Quotable: "In a status update, the presenter opens with a report: 'Here's what happened since last time.' In a decision session, the presenter opens with a decision ask: 'I need approval for X by this date.'"
Quotable: "Status updates present every metric on every dimension - comprehensive coverage that creates decision paralysis. Decision sessions present focused proof: the three data points that support the recommendation."
Quotable: "A steering committee meeting that ends with polite nods and no decisions isn't a successful meeting. It's a failure disguised as information sharing."

**[17] The PM Professional (practitioner blog) - "Writing a Project Status Report That Actually Gets Read".** practitioner. **fetched-and-verified.**
`https://thepmprofessional.com/2025/03/project-status-reports/`
Supports: Q3: states plainly that a status report should be shaped by who reads it, not only by what happened - names three audience tiers (executives, functional leads, team members) with different content priorities and recommends tailoring format/intro per audience rather than sending one report to everyone.
Quotable: "Don't send the same report to everyone. Create a core report and tailor the intro or format slightly depending on the audience."
Quotable: "high-level progress, risks, and budget alignment"
Quotable: "dependencies and milestones"
Quotable: "clarity on tasks and priorities"

**[18] iZenBridge (PMP/PMBOK exam-prep practitioner blog) - "Work Performance Data, Work Performance Information, and Work Performance Report".** practitioner. **fetched-and-verified.**
`https://www.izenbridge.com/blog/work-performance-data-wpd-work-performance-information-wpi-work-performance-report-wpr/`
Supports: Q4 (the closest analog found, not a direct match): explains PMBOK's chain Work Performance Data (raw observations) -> Work Performance Information (analyzed) -> Work Performance Report (compiled, 'physical or electronic representation of work information compiled in project documents'). Supports a report being a COMPILATION of information gathered elsewhere in the monitoring process, but does not state a rule that every figure must be traceable to a system of record, nor prohibits new facts in a status report by name.
Quotable: "the raw observations and measurements as a result of work getting executed"
Quotable: "the physical or electronic representation of work information compiled in project documents, intended to generate decisions, actions, or awareness"

**[19] This library, internal - kpi-dashboard bundle companion (templates/kpi-dashboard/kpi-dashboard_companion.md).** standards. **fetched-and-verified.**
No URL, and none is possible: this is a file inside this repository, at
`templates/kpi-dashboard/kpi-dashboard_companion.md`, not a web source. It is recorded as a source
because framing point 6's boundary argument rests on what this library's own dashboard bundle says
about itself, and a claim about a sibling bundle needs a home here like any other.
Supports: Q1: this library's own already-shipped kpi-dashboard bundle defines a dashboard as a document that 'DEFINES a dashboard - not a live BI tool' - i.e. this library's dashboard bundle is itself a static specification document, not a live instrument, which complicates the report-vs-dashboard framing supplied by the external PPM Express source.
Quotable: "this bundle is a document that DEFINES a dashboard - not a live BI tool"

### Failure modes, and the critique of reporting itself

**[20] Craig Williams - "Why Nobody Reads Your Excellent Status Reports" (LinkedIn, June 2014).** practitioner. **fetched-and-verified.**
`https://www.linkedin.com/pulse/20140603150756-11371473-why-nobody-reads-your-excellent-status-reports`
Supports: Names the 'report nobody reads' failure mode directly (it is the article's title and thesis): shared-service teams (IT, HR, Legal) mistake the status report for their whole communications plan.
Quotable: "It's easy for shared service teams like IT, HR, Legal, etc. to stop at the status report and kid themselves into thinking that it's their communications plan."
Quotable: "A great communications plan, however, must also include a feedback loop."

**[21] TeamRetro - "Agile Theatre: how agile ceremonies fail" (field guide, org-authored, no individual byline).** practitioner. **fetched-and-verified.**
`https://www.teamretro.com/guides/agile-theatre/`
Supports: Names 'status-theatre stand-ups' directly: a ceremony run for appearance rather than function, whose real audience is the most senior person present rather than the team - the closest verified naming of the 'status theatre / satisfies governance not decisions' failure mode.
Quotable: "Agile theatre is what an agile ceremony becomes when it's run for appearance instead of function"
Quotable: "status-theatre stand-ups"
Quotable: "Everyone reports to the most senior person in the room"

**[22] Marty Cagan / Silicon Valley Product Group - "The Alternative to Roadmaps".** practitioner. **fetched-and-verified.**
`https://www.svpg.com/the-alternative-to-roadmaps/`
Supports: Supports 'reporting activity/output instead of outcome' as a named failure mode. Cagan's target is roadmap reporting specifically, not status reports by name, so the transfer to status reports is my inference, not his claim - flagged honestly rather than presented as a direct hit.
Quotable: "It is all about outcome rather than output."
Quotable: "the feature must actually work (as measured by the key results) otherwise the team needs to try a different approach"
Quotable: "the team is not off the hook just by delivering a requested feature or project"

**[23] Johanna Rothman - "Traffic Lights and Project Status" (jrothman.com, 2011).** practitioner. **fetched-and-verified.**
`https://www.jrothman.com/mpd/project-management/2011/03/traffic-lights-and-project-status/`
Supports: Adjacent evidence for numbers/status losing touch with reality: on serial/long projects the light stays yellow or red while senior managers expect it to 'turn green by itself with no outside intervention' - a report that stops corresponding to the actual state of the work. Does not use the phrase 'system of record'.
Quotable: "on serial lifecycle projects, or on long projects, the traffic light was always yellow or red"
Quotable: "It still doesn't help the color-blind people"

**[24] Adam Siegel (CEO, Cultivate Labs) - "The Traffic Light Metaphor for Project Status is a Disaster" (March 2018).** vendor. **fetched-and-verified.**
`https://www.cultivatelabs.com/posts/the-traffic-light-metaphor-for-project-status-is-a-disaster`
Supports: Strongest verified source for numbers becoming disconnected from ground truth: red-yellow-green status is gamed by managers protecting themselves, so decision-makers act on distorted numbers. This is the closest sourced analogue to 'the report whose numbers disagree with the system of record' - the mechanism here is political distortion of self-reported status, not a literal data-reconciliation gap, and that distinction should not be blurred.
Quotable: "The information they're getting is based on hopes and prayers."
Quotable: "Truly red projects rarely turn yellow or green unless there is intervention beyond what a manager can engineer."
Quotable: "Everyone working on a red project knows the project is on a path to failure. They discuss it...but in an official setting? Silence."

**[25] Bob Lewis, quoted/summarized via CIO.com - "Project management has a status problem".** practitioner. **fetched-and-verified.**
`https://www.cio.com/article/4142004/project-management-has-a-status-problem.html`
Supports: Names status meetings and status reports as 'deadly wastes of time' and documents the 'scarlet letter' effect where a project once marked Yellow/Red cannot recover its reputation regardless of a new plan - a distinct, sourced failure mode (status reporting punishes honesty) adjacent to but not identical to the six candidate failure modes in the brief.
Quotable: "project managers who spend an hour a week letting the project team know the project's status, well, their project status meetings - and for that matter the status meeting's close kin, the dreaded project status report - are deadly wastes of time"
Quotable: "new plan or no new plan, the project's degraded status - and with it the project manager's reputation - is a scarlet letter"
Quotable: "the original schedule is the schedule. If the project is going to slip, it's in the Yellow from that point forward"

**[26] Agile Alliance - Glossary entry, "Information Radiators".** standards. **fetched-and-verified.**
`https://agilealliance.org/glossary/information-radiators/`
Supports: Canonical definition of the information-radiator concept (coined by Alistair Cockburn). Note honestly: this specific page does NOT itself claim radiators replace status reports or status meetings - I checked and it makes no such assertion. The replacement argument comes from the ScrumPLoP pattern page and practitioner sources below, not from this glossary entry.
Quotable: ""Information radiator" is the generic term for any of a number of handwritten, drawn, printed, or electronic displays that a team places in a highly visible location, so that all team members, as well as passers-by, can see the latest information at a glance."

**[27] ScrumPLoP - "Information Radiator" published pattern (value-stream pattern language, community-authored).** practitioner. **fetched-and-verified.**
`https://sites.google.com/a/scrumplop.org/published-patterns/value-stream/information-radiator`
Supports: The clearest verified statement of the pull-based-radiator-replaces-status-reporting argument: formal status meetings are cumbersome overhead that a good radiator makes largely unnecessary.
Quotable: "Good information radiators both help the team organize their thinking and planning, and largely eliminate the need for formal status reporting meetings in an agile environment."
Quotable: "Such processes are cumbersome, intrusive, waste the time of most people involved and come with a discouraging overhead."

**[28] Martin Fowler - "It's Not Just Standing Up: Patterns for Daily Standup Meetings" (martinfowler.com, co-authored article; includes the 'Walk the Board' pattern, quoting Bret Pettichord).** practitioner. **fetched-and-verified.**
`https://martinfowler.com/articles/itsNotJustStandingUp.html`
Supports: Names 'Walk the Board' as the pull-based alternative to a person-by-person status round, and the 'All Hands' pattern explicitly proposes replacing separate status meetings and reports with the daily stand-up - while also honestly noting some reporting (e.g. burn-down charts for overall progress) is NOT covered by the stand-up format.
Quotable: "[S]tandups keep everyone busy. [W]alking the board keeps everyone focused on the most important things."
Quotable: "Replace some or all of the meetings and reports with the daily stand-up"
Quotable: "Not all forms of reporting will be, nor should be, covered by the stand-up format"

**[29] Todd Lankford (Agile coach) - "Surviving Agile Without a Status Report: Visualize the Work" (coachlankford.com, May 2019).** practitioner. **fetched-and-verified.**
`https://coachlankford.com/2019/05/12/surviving-agile-without-a-status-report-visualize-the-work/`
Supports: The single strongest, most quotable verified statement of the polemic itself: board-walking beats the status report outright. Also supplies a useful contrast term, 'Information Refrigerators', for reporting tools that require effort to access versus radiators that broadcast.
Quotable: "Engaging with your teams and visualizing the work outperforms the status report every time."
Quotable: "Big visual boards invite conversation."
Quotable: "An Information Radiator displays information in a place where passersby can see it"

**[30] PMBOK Guide communications-management content, as mirrored on Wikibooks ("Project Management/PMBOK/Communications Management").** standards. **fetched-and-verified.**
`https://en.wikibooks.org/wiki/Project_Management/PMBOK/Communications_Management`
Supports: The defence-of-written-reporting side: status reports are framed as deliberate push communication to stakeholders who cannot be present, whose function is to prevent surprises and give a documented, asynchronous record of progress. Honest caveat: this is a Wikibooks community mirror/paraphrase of PMBOK content, not the PMI standard document itself (PMI's own pages 403'd on fetch), and its prose is descriptive rather than a reasoned rebuttal of the radiator argument - it asserts status reporting's function, it does not argue against the pull-based alternative.
Quotable: "The report has the progress information of the project."
Quotable: "It can be mailed directly to them."
Quotable: "a clear understanding of what you are doing. There should be no surprises for them"

## Contested register

1. **Whether RAG has a definable threshold at all.** The IPA defines Red, Amber and Green in prose and
   declines to define Amber-Red and Amber-Green [1][2]; the APM publishes guidance on using the tool [4];
   PRINCE2's own product page defines nothing and only cautions [5]. Practitioners split: Rothman observes
   lights staying yellow or red while management expects them to "turn green by itself" [23], and Siegel
   argues the metaphor is broken outright [24]. There is no settled answer and the bundle does not invent one.
2. **Who owns the convention's origin.** Untraceable to an inventing document. The honest trace is to
   current institutional ownership, the IPA and the UK public sector [1][2][3], not to a coiner.
3. **Whether the Keil statistic may be stated as fact.** The 60 percent figure is quoted verbatim from the
   2014 synthesis [12], but the 2007 primary paper behind it was not read. Attribution runs through the
   synthesis, and the bundle says so rather than implying a direct reading of the original.
4. **Practitioner versus student evidence inside one research programme.** The same body of work includes
   a records review of 56 practising managers and a 60-student laboratory study [12]. The bundle keeps them
   distinct; collapsing them into "research shows" would overstate the practitioner evidence.
5. **Whether the report/dashboard line can rest on static-versus-live.** Externally it does [15]. Inside
   this library it cannot, because `kpi-dashboard` is itself a static document that defines a dashboard
   [19]. The surviving distinction is definition versus narration, and it is this library's synthesis.
6. **Whether written status reporting should exist at all.** A named lineage argues a pull-based
   information radiator replaces it [26][27][28][29]; Fowler's standup patterns and the Agile Alliance
   glossary are the strongest statements of that case. The counter-case is that governance bodies who do
   not attend the standup still need a record, which is what PRINCE2's manage-by-exception framing supplies
   [5]. One side is practitioner writing and pattern languages, the other is a methodology and a public
   standard. That asymmetry is recorded rather than smoothed.
7. **Whether Cagan's outcome-versus-output argument transfers.** Cagan writes about roadmaps, not status
   reports [22]. The transfer is a reasonable inference and is labelled as one, not as Cagan's claim.

## Sought and not found

- **Any source stating the no-new-facts rule.** Searched for "no surprises", "single source of truth" with
  status report, "traceable" with source of record, and "should not introduce new information". PMI's own
  status-report article was blocked by Cloudflare. PMBOK's work-performance chain supports "compiled from
  elsewhere" [30][18] and stops short of a prohibition. **The rule is this library's own.**
- **PMBOK itself**, for the second time in this library. Behind PMI membership; no free full text reachable.
  Nothing in this bundle rests on it.
- **AXELOS's own PRINCE2 manual.** Paywalled. Every PRINCE2 claim here comes from a community mirror and
  says so [5].
- **ISO 21502 and IEEE 1058.** The first is a paid standard and was not fetched; the second was fetched and
  returned a corrupted binary the agent could not extract text from. **Neither is claimed either way.**
- **An origin for red/amber/green.** No readable primary source establishes who first used it.
- **Three of six candidate failure modes.** "Takes longer to write than the work it describes", "restates
  the plan instead of the actuals", and "numbers disagree with the system of record" in its literal
  two-systems sense could not be tied to a quotable named source, and were **dropped rather than filled**.
  What was found instead is a different and better-sourced failure: status distorted by incentive, where
  being marked red carries a "scarlet letter" [25].

## Notes for the companion

**The honest core.** This is the one document type in this library whose central weakness is *measured*
rather than argued. Reports are biased 60 percent of the time and optimistically biased more than twice as
often as pessimistically [12]. Meanwhile the colour everyone reads first has no defined threshold where it
matters most, by the explicit admission of the most detailed scheme published [1]. **The bundle's job is not
to exhort honesty. It is to make the two mechanisms that produce dishonesty harder to operate:** an
undefined threshold, and a figure with no source.

**The sections, and every attested one is taken from what templates actually title.**

- **Lean:** Summary; Status; Accomplishments; Risks and Issues; Next Steps.
- **Full adds four, in place:** Summary; Status; **Metrics**; Accomplishments; **Milestones**; Risks and
  Issues; **Decisions Needed**; Next Steps.

Lean is a strict ordered subset of full. Attestation: Summary [6][8][9]; Status [6][7][8]; Metrics [7][8];
Accomplishments [6][7][8]; Milestones [7][8][9]; Risks and Issues [7][8][9]; Next Steps [6][7][8][9].
**"Decisions Needed" is attested by nothing and is this bundle's own contribution**, kept because a report
that surfaces no decision is the "status theatre" failure [21] in template form, and labelled as the
library's own rather than as practice.

**Every Status entry must carry its threshold.** This is the bundle's structural answer to finding 4: the
template does not accept a bare colour. A colour without the rule that produced it is an opinion wearing the
costume of a measurement, and the IPA's own guide is the evidence that even the most careful public scheme
leaves its middle undefined [1].

**The example is bound by the no-new-facts rule, and its figures are fixed in advance.** Every number below
already exists in a sibling example and must be reported as that sibling reports it:

| Figure | Value | Source of record | Reads as |
|---|---|---|---|
| Time to Insight | `-18%` against a `-30%` target | `kpi-dashboard` | **Amber**, against the 25 percent green line, NOT against the target |
| Saved Views adoption | `41%` against a `60%` target | `kpi-dashboard` | **Amber**, against the 55 percent green line, barely above red |
| View-list load p95 | `620ms` against `< 500ms` | `kpi-dashboard`, and the same fact as ISS-12 in the `raid-log` | **Amber** |
| Weekly active analysts | `495` against hold `>= 480` | `kpi-dashboard` | Green |
| Migration integrity | `n/a (pre-cutover)` | `kpi-dashboard` | **No colour.** Giving it one invents a fact |
| R-05, PII exposure | Escalated to the steering group 2026-07-14 | `risk-register`, via the `incident-postmortem` | Open, escalated |
| D-01 dependency | Platform query engine due 2026-08-01, critical path | `raid-log` | Live |

**Two traps the example must not fall into.** First, two metrics carry both a **target** and a **green
threshold** and they are different numbers, so the colour must be stated against the threshold. Second,
**ISS-12 and the View-list load KPI are one fact, not two**, and reporting them as separate problems would
double-count. Migration integrity has no colour because it has no measurement yet.
