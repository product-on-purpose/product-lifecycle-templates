# Companion: The Status Report

> The deep explainer for the status-report bundle. Read this to understand what a status report is, where
> the shape of one comes from, why it is structured the way it is, and where the evidence about it is thin
> or contested. The short operator card is [`status-report_guide.md`](status-report_guide.md); a fully
> worked instance is [`status-report_example.md`](status-report_example.md). Inline citations like
> [[1]](#ref-1) resolve to the [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A status report is **the periodic document that tells people who are not doing the work where a piece of
work stands: what changed, what is at risk, and what is needed from the reader.** It is not where facts
originate. Every number in it is read from something with more authority - a KPI dashboard, a risk
register, a RAID log - and its job is to narrate what those sources mean for one audience in one period.

**The load-bearing scope fact, stated first because it governs the whole template: this document owns none
of its own facts.** That no-new-facts framing is this library's own contribution, not a rule this research
found stated anywhere. The search for it was deliberate - "no surprises", "single source of truth", "should
not introduce new information" - and came back empty; the closest analog, PMBOK's chain from raw
observations through analysis to a compiled report, supports a report being *"the physical or electronic
representation of work information compiled in project documents"* [[18]](#ref-18), which is compilation,
not a prohibition on inventing figures. Say so plainly rather than dressing a library convention as
established practice.

**The honest second thing to know is that this is the one document type in this library whose central
weakness has actually been measured, not argued.** Keil, Smith, Iacovou and Thompson's synthesis of a
research programme running from 1999 to 2013 reports that *"we reviewed the records of 56 experienced
software project managers and found that project managers write biased reports 60% of the time and that
their bias is more than twice as likely to be optimistic... than pessimistic"* [[12]](#ref-12). That is a
records review of practising managers, not a survey of students - the same programme [[12]](#ref-12) also ran a 60-student
laboratory study, and this companion keeps the two distinct rather than flattening them into one
undifferentiated "research shows" claim.

**The honest third thing to know is that the colour everyone reads first is not fully defined even in the
most careful published scheme.** The UK Infrastructure and Projects Authority's Delivery Confidence
Assessment gives prose criteria for Red, Amber and Green [[1]](#ref-1), and then states outright:
*"Definitions have only been given for Red, Amber and Green; Amber-Red and Amber-Green can be used to
reflect a status that lies in between"* [[1]](#ref-1). The two intermediate colours, which do the most
delicate signalling work on a five-point scale, are left to judgement by the most detailed public scheme
there is.

**At a glance**
- Exactly one methodology specifies this document as a named artifact with a defined producer, recipient
  and cadence: PRINCE2's Highlight Report [[5]](#ref-5). Everything else in this file is folk practice.
- PMBOK itself could not be retrieved, as the `business-case` bundle also found, for the second time in this library; nothing here rests on it
  [[18]](#ref-18)[[30]](#ref-30).
- Every colour needs the threshold that produced it, because the threshold is exactly the part the best
  published scheme leaves undefined [[1]](#ref-1).
- Reports are optimistically biased far more often than the reverse, and the bias is measured, not assumed
  [[12]](#ref-12).

If you read nothing else: a status report **narrates what already-authoritative sources mean for one
audience in one period, and it is written by people whose incentives push toward optimism.** The template's
job is not to exhort honesty. It is to make the two mechanisms that produce dishonesty harder to operate: a
threshold-free colour, and a figure with no source.

---

## 2. Origins and evolution

**No source read establishes who invented the red/amber/green convention.** The honest trace is to current
institutional ownership, not to a coiner: the UK Infrastructure and Projects Authority defines and maintains
the scheme in current use, echoed verbatim between its assurance guidance and its own annual report
[[1]](#ref-1)[[2]](#ref-2), and the National Audit Office's oversight of that same scheme shows it is a live
government practice being actively scrutinised. No source read traces the convention to an inventing
document, so its provenance is current institutional ownership rather than a lineage anyone could follow
[[3]](#ref-3).

**The one artifact with a genuine specification lineage is PRINCE2's Highlight Report.** It is a named
management product, not a generic status update: *"The highlight report provides a regular update on stage
progress, prepared by the project manager for the project board"* [[5]](#ref-5), *"kept simple and focused,
providing a clear one-page overview of the stage's progress"* [[5]](#ref-5), with its cadence set
elsewhere - *"The frequency and format of this report are defined in the communication management
approach"* [[5]](#ref-5) - and its purpose stated as exception management rather than raw narration:
*"manage by exception between stage boundaries, ensuring they stay informed without unnecessary
intervention"* [[5]](#ref-5).

**The folk vocabulary has its own, similarly untraceable, origin story.** "Watermelon reporting" - green on
the outside, red inside - has no confirmed coiner. The earliest dated, byline-attributed use found does not
itself claim to originate the term [[13]](#ref-13), and a veteran consultant sometimes credited with coining
it instead calls it *"the old joke about the Watermelon project"* [[14]](#ref-14) when describing the
pattern, which undercuts rather than supports a single-coiner attribution.

---

## 3. Anatomy (section by section)

A status report is, at its core, a narrated summary of health plus the specific asks of its reader. This
section walks the parts; the template groups them into the sections you fill. None of the section titles
below are this bundle's invention except one, which is marked as such: five vendor templates were read in
full and not one used the words "RAG" as a heading, or the compound titles a document like this might be
expected to carry [[6]](#ref-6)[[7]](#ref-7)[[8]](#ref-8)[[9]](#ref-9)[[10]](#ref-10)[[11]](#ref-11). The
section titles below are retaken from what those templates actually title.

### Summary

**What it is:** a short, first-read overview of where the work stands. **Why it exists:** the reader who
opens only this section should still leave informed. Attested across the corpus as *"A summary of the
project's current status"* [[6]](#ref-6), *"Project Summary"* [[8]](#ref-8), and *"Summary"* preceded by an
*"Introductory note"* [[9]](#ref-9).

### Status

**What it is:** the overall health call for the period, typically a colour, plus the rule that produced it.
**Why it exists:** the fastest-read field in the whole document, attested as *"A status tag indicating
project health"* [[6]](#ref-6), *"Project Status Summary"* paired with *"Percent Complete:"* [[7]](#ref-7),
and *"Project Health"* [[8]](#ref-8). **Every Status entry in this template must carry its threshold, not
just a colour.** That is this bundle's structural answer to the finding above the fold: a colour without the
rule that produced it is an opinion wearing the costume of a measurement, and even the most careful public
scheme leaves its middle undefined [[1]](#ref-1). The Association for Project Management treats the
threshold itself as an organisational responsibility rather than something the RAG convention supplies on
its own - *"the RAG needs to be clearly defined, it must be communicated and consistently applied"*
[[4]](#ref-4) - and PRINCE2's own product documentation, which carries RAG indicators, defines no threshold
at all, only a caution to *"be cautious with traffic light indicators to ensure clarity"* [[5]](#ref-5).

### Metrics (full variant)

**What it is:** the specific numbers behind the status colour, read from a system of record rather than
estimated fresh. **Why it exists:** this is where the no-new-facts rule becomes concrete rather than
aspirational. Attested as *"Key Performance Indicators (KPI's)"* with named formulas - *"Schedule Variance
(SV):"*, *"Schedule Performance Index (SPI):"*, *"Cost Variance (CV):"*, *"Cost Performance Index (CPI):"*
[[7]](#ref-7) - and as *"Project Metrics"* [[8]](#ref-8).

### Accomplishments

**What it is:** what was actually completed in the period, not what was planned. **Why it exists:** this is
the counterweight to the optimism bias measured above - a section that can only be filled with things that
happened, not things that are hoped for. Attested as *"Specific accomplishments the team has achieved"*
[[6]](#ref-6), *"Work Completed Last Week"* [[7]](#ref-7), and *"Key Accomplishments"* [[8]](#ref-8).

### Milestones (full variant)

**What it is:** the deliverable and date structure the period's progress is measured against. **Why it
exists:** accomplishments without milestones have no baseline to be judged against. Attested as
*"Deliverables and Milestones"* [[7]](#ref-7), *"Milestone Review"* alongside *"Project Deliverables"*
[[8]](#ref-8), and *"Upcoming tasks and milestones"* [[9]](#ref-9).

### Risks and Issues

**What it is:** what could still go wrong, and what has already gone wrong, for this period's audience -
not the full risk register, but what that register means for them right now. **Why it exists:** the
sharpest-attested section in the whole corpus: *"Risks"*, *"Open Issues"*, *"Open Risks"* [[7]](#ref-7),
*"Issues and Risks"* [[8]](#ref-8), and *"Project risks, issues, and mitigation plans"* [[9]](#ref-9).

### Decisions Needed (full variant)

**What it is:** the specific asks of the reader - what they must decide, and by when. **Why it exists, and
the honest label: nothing in this research attests this title.** It is this bundle's own contribution, kept
deliberately because a report that surfaces every metric and asks for nothing is exactly the failure named
elsewhere in this file as status theatre: a document that satisfies the appearance of governance while
producing no decision [[21]](#ref-21). Kept here as the library's own addition, not as recovered practice.

### Next Steps

**What it is:** what happens next, independent of whether it depends on a decision above. **Why it exists:**
closes the report on forward motion rather than a list of problems. The most consistently attested section
in the corpus - *"The next steps"* [[6]](#ref-6), *"Work Planned for Next Week"* [[7]](#ref-7), *"Upcoming
Work"* and *"Action Items"* [[8]](#ref-8), and *"Action items"* [[9]](#ref-9).

---

## 4. Variants and sizing

**Lean** carries five sections: **Summary**, **Status**, **Accomplishments**, **Risks and Issues**, and
**Next Steps**. It is the smallest report that still says where things stand, what happened, what is at
risk, and what comes next.

**Full** is a strict superset, adding **Metrics**, **Milestones**, and **Decisions Needed** in place, for
eight sections total: Summary, Status, Metrics, Accomplishments, Milestones, Risks and Issues, Decisions
Needed, Next Steps.

**The scaling signal in the corpus is cadence and audience, not length.** Vendor templates split first on
frequency - *"Daily status reports"*, *"Weekly status reports"*, *"Monthly status reports"*, *"Quarterly
status reports"* [[6]](#ref-6) - and second on audience: *"Executive status report templates"* against
*"Team status report templates"* against *"Portfolio status report templates"* [[10]](#ref-10), with a
further named split by function - *"Weekly Executive Status Report Template"*, *"Weekly IT Status Report
Template"*, *"Weekly HR Status Report Template"*, *"Weekly Agile Sprint Status Report Template"*, *"Weekly
Scrum Sprint Status Report Template"* [[11]](#ref-11). No single one of those sources supplies this bundle's
exact eight-section structure; they corroborate that audience and cadence, not scope creep, is what drives
a report from lean to full. Move to full when the report reaches an audience empowered to act on the metrics
and decisions directly, rather than one that only needs to know the headline.

---

## 5. Methodology lineage

**This section is short because the finding is short: exactly one methodology specifies this document, and
everything else is unspecified folk practice.** PRINCE2's Highlight Report is a genuine management product
with a defined producer, recipient, cadence rule, and purpose [[5]](#ref-5), reachable here only through a
community mirror rather than AXELOS's own paywalled manual, and the log says so rather than implying a
direct reading of the primary text.

**PMBOK, the other major methodology this library expected to find something in, could not be retrieved.**
This is the second time in this library that PMBOK sat behind a membership wall unreachable to this
research. What is reachable is a secondary description of its work-performance chain - raw observation, to
analysed information, to a compiled report [[18]](#ref-18)[[30]](#ref-30) - and this bundle rests nothing on
PMBOK itself, only on that secondary account, labelled as such.

**Absent a specified template, the de facto standard is the vendor corpus.** Five vendor and practitioner
templates were read in full [[6]](#ref-6)[[7]](#ref-7)[[8]](#ref-8)[[9]](#ref-9)[[10]](#ref-10), and this
bundle's section titles are retaken from what they actually title rather than invented fresh, with the one
exception - Decisions Needed - named honestly in section 3.

**The RAG convention layered onto all of this traces to institutional ownership, not to a methodology.** The
UK Infrastructure and Projects Authority is the clearest current owner of a fully worked colour scheme
[[1]](#ref-1)[[2]](#ref-2), independent of PRINCE2 or PMBOK, and the National Audit Office's scrutiny of that
same scheme is evidence it is a live governance practice rather than a dormant one
[[3]](#ref-3).

---

## 6. Debates and contested boundaries

**Whether RAG has a definable threshold at all.** The IPA defines Red, Amber and Green in prose and declines
to define the two intermediate colours [[1]](#ref-1)[[2]](#ref-2); the Association for Project Management
publishes guidance on using the tool well, which presupposes the tool itself supplies no threshold
[[4]](#ref-4); PRINCE2's own product page defines nothing and only cautions [[5]](#ref-5). Practitioners
split further: Johanna Rothman observes lights staying yellow or red on long projects while management
expects them to *turn green on its own without anyone intervening* [[23]](#ref-23), and Adam Siegel
argues the metaphor is broken outright because *"the information they're getting is based on hopes and
prayers"* [[24]](#ref-24). There is no settled answer, and this bundle does not invent one; it answers by
structure instead, requiring the threshold beside every colour.

**Whether the report/dashboard line can rest on static versus live.** Externally, it can: a report is
*"comprehensive documents that detail a project's progress, challenges, and next steps"* shared
*"periodically"*, while a dashboard is *"a visual representation of real-time project data"*
[[15]](#ref-15). **That distinction does not survive contact with this library**, because its own
`kpi-dashboard` bundle is itself a static document that defines a dashboard rather than being a live
instrument - *"this bundle is a document that DEFINES a dashboard - not a live BI tool"*
[[19]](#ref-19). The distinction that does survive, and it is this library's own synthesis rather than a
quotation: the dashboard bundle specifies which metrics exist and how each is defined; the status report
narrates what happened against those metrics in one period, for one audience, drawing its numbers from them
rather than defining new ones.

**Whether written status reporting should exist at all.** A named lineage argues a pull-based information
radiator replaces it. The Agile Alliance's glossary defines the concept cleanly - *"any of a number of
handwritten, drawn, printed, or electronic displays that a team places in a highly visible location, so that
all team members, as well as passers-by, can see the latest information at a glance"* [[26]](#ref-26)
- but that page itself makes no replacement claim; the argument comes from elsewhere. ScrumPLoP states it
directly: *"Good information radiators... largely eliminate the need for formal status reporting meetings in
an agile environment"* [[27]](#ref-27). Martin Fowler's standup patterns propose the same move -
*"Replace some or all of the meetings and reports with the daily stand-up"* [[28]](#ref-28) - while honestly
noting *"Not all forms of reporting will be, nor should be, covered by the stand-up format"*
[[28]](#ref-28). Todd Lankford states the polemic most sharply: *"Engaging with your teams and visualizing
the work outperforms the status report every time"* [[29]](#ref-29). The counter-case is that governance
bodies who do not attend the standup still need a record, which is what PRINCE2's manage-by-exception
framing supplies [[5]](#ref-5); PMBOK's descriptive account of push reporting names the same need -
*"a clear understanding of what you are doing. There should be no surprises for them"* [[30]](#ref-30),
though that source is a Wikibooks mirror of PMBOK, not the standard itself, and states a function rather
than arguing against the radiator case. One side of this debate is practitioner writing and pattern
languages; the other is a methodology and a compiled standard summary. That asymmetry is recorded here
rather than smoothed over.

**Whether the Keil statistic may be stated as settled fact.** The 60 percent figure is quoted verbatim from
the 2014 synthesis [[12]](#ref-12), but the 2007 primary paper the synthesis credits it to [[12]](#ref-12) was not read in this research.
Attribution runs through the synthesis, not a direct reading of the original study.

**Whether Cagan's outcome-versus-output argument transfers to status reports.** Marty Cagan writes about
roadmaps, not status reports - *"It is all about outcome rather than output"* [[22]](#ref-22) - and the
transfer to status reporting in section 7 below is a reasonable inference, labelled as one, not presented as
Cagan's own claim.

---

## 7. Anti-patterns and failure modes

1. **Watermelon reporting.** Green on the outside, red inside - the status colour and the underlying reality
   have diverged [[13]](#ref-13)[[14]](#ref-14). Fix: require the threshold beside the colour, not just the
   colour.
2. **The report nobody reads.** Shared-service teams mistake the status report for their whole
   communications plan: *"It's easy for shared service teams like IT, HR, Legal, etc. to stop at the status
   report and kid themselves into thinking that it's their communications plan"* [[20]](#ref-20). Fix: pair
   the report with an actual feedback loop, not just distribution.
3. **Status theatre.** A ceremony or document run for appearance rather than function, whose real audience
   is *"the most senior person in the room"* [[21]](#ref-21) rather than the people meant to act on it. Fix:
   this bundle's own Decisions Needed section, which a report with nothing to decide cannot fill honestly.
4. **The gamed traffic light.** Status distorted to protect the reporter rather than inform the reader:
   *"The information they're getting is based on hopes and prayers"* [[24]](#ref-24), and *"Everyone working
   on a red project knows the project is on a path to failure. They discuss it... but in an official
   setting? Silence"* [[24]](#ref-24). Fix: name the threshold in advance, before the number that will be
   graded against it exists.
5. **The scarlet letter.** Once a project is marked yellow or red, its reputation, and its project manager's
   reputation, does not recover regardless of a new plan: *"new plan or no new plan, the project's degraded
   status... is a scarlet letter"* [[25]](#ref-25). This is a sourced account of exactly the incentive
   structure that produces the optimism bias measured in section 1 [[12]](#ref-12).
6. **Reporting activity instead of outcome.** An inference from roadmap practice, not a direct finding about
   status reports: the failure of reporting what shipped rather than what changed for the reader
   [[22]](#ref-22).

**Three candidate failure modes were sought and not found**, and are named here as an honest gap rather than
silently dropped: "takes longer to write than the work it describes", "restates the plan instead of the
actuals", and "numbers disagree with the system of record" in the literal sense of two systems showing two
different values. None could be tied to a quotable, named source in this research. What was found instead,
and is better sourced, is the scarlet-letter mechanism above [[25]](#ref-25): status distorted by the
incentive not to be marked red, rather than a literal reconciliation failure between two systems.

---

## 8. Relationships to other artifacts

**Status report vs PRINCE2 Highlight Report.** Not a variant of this template. The Highlight Report is a
distinct, formally specified management product with its own producer, recipient, and cadence rule
[[5]](#ref-5), and this bundle treats it as the canonical spine to learn from rather than folding it in as a
second format alongside lean and full.

**Status report vs dashboard.** The externally supplied distinction is periodic narration versus live visual
instrument [[15]](#ref-15). Inside this library the surviving distinction is narrower and sharper: the
dashboard defines which metrics exist and how each is measured; the status report narrates what those
metrics meant for one audience in one period, and must draw its figures from the dashboard rather than
define new ones [[19]](#ref-19). This is the family's no-new-facts rule applied concretely, and it is why
the worked example in section 10 reads its numbers from a sibling bundle rather than inventing them.

**Status report vs steering-committee or decision paper.** A named practitioner source draws the sharpest
line found in this research: *"In a status update, the presenter opens with a report: 'Here's what happened
since last time.' In a decision session, the presenter opens with a decision ask: 'I need approval for X by
this date'"* [[16]](#ref-16), and *"Status updates present every metric on every dimension - comprehensive
coverage that creates decision paralysis. Decision sessions present focused proof: the three data points
that support the recommendation"* [[16]](#ref-16). A status report that tries to be a decision paper on
every metric produces exactly the paralysis this source names; Decisions Needed exists to carry the narrow
subset that genuinely needs a decision, without turning the whole document into one.

**Status report vs information radiator.** Not a sibling artifact so much as a competing philosophy: a
radiator is a pull-based, always-current display [[26]](#ref-26) argued by its advocates to make formal
status reporting unnecessary in an agile setting [[27]](#ref-27)[[28]](#ref-28)[[29]](#ref-29). The status
report remains the push mechanism for the audience that cannot walk the board - a governance body, an
external stakeholder, anyone who was not in the room [[30]](#ref-30).

---

## 9. Adaptations

- **By cadence.** Vendor practice splits first on frequency, from *"Daily status reports"* through
  *"Quarterly status reports"* [[6]](#ref-6); the sections stay the same, the granularity of Accomplishments
  and Next Steps does not.
- **By audience.** Named variants split executive, department, agile, and team reporting with different
  field emphasis [[10]](#ref-10), and function-specific templates exist for IT, HR, and agile or scrum
  sprints [[11]](#ref-11). A named practitioner source recommends tailoring the intro or format per audience
  rather than sending one report to everyone: *"Don't send the same report to everyone. Create a core report
  and tailor the intro or format slightly depending on the audience"* [[17]](#ref-17), naming executives,
  functional leads, and team members as the three tiers with distinct content priorities.
- **Toward governance.** When the reader is a steering committee or a body that only convenes periodically,
  weight the report toward Status and Decisions Needed, on the reasoning in section 8 above
  [[16]](#ref-16).
- **Toward a team already walking the board.** Where a team already runs a live radiator, this template's
  natural home shrinks to the audience the radiator does not reach - anyone not in the room
  [[27]](#ref-27)[[28]](#ref-28).

---

## 10. Worked example

[`status-report_example.md`](status-report_example.md) is a full-variant status report for the Acme
Analytics **Reporting Platform Modernization** program, the same thread this family's sibling bundles
already cover. Every figure in it is read from an artifact that already exists in this library rather than
invented for the report, per the family's no-new-facts rule discussed in section 1: Time to Insight, Saved
Views adoption, view-list load latency, and weekly active analysts come from the `kpi-dashboard` example;
the PII exposure risk comes from the `risk-register`, escalated through the `incident-postmortem`; the
platform query engine dependency comes from the `raid-log`. It deliberately does not report an all-green
period. Time to Insight and Saved Views adoption both read amber against their defined green thresholds,
which are not the same numbers as their targets, and the view-list load latency issue is reported once, not
twice, even though it also appears as an open item in the RAID log for the same program. A status report
where everything is green would teach nothing, because the actual skill of the type is saying a bad thing
clearly to an audience that outranks the writer.

---

## References

<a id="ref-1"></a>[1] Infrastructure and Projects Authority (UK government). "[Project Assurance Reviews: Delivery Confidence Guide for Review Teams](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/638436/delivery_confidence_guide_for_review_teams.pdf)." gov.uk (fetched 2026-08-07). The most detailed published RAG threshold definition found; explicitly declines to define Amber-Red and Amber-Green ("Definitions have only been given for Red, Amber and Green; Amber-Red and Amber-Green can be used to reflect a status that lies in between."). [primary]

<a id="ref-2"></a>[2] GOV.UK / Infrastructure and Projects Authority. "[Infrastructure and Projects Authority Annual Report 2023-24](https://www.gov.uk/government/publications/infrastructure-and-projects-authority-annual-report-2023-24/infrastructure-and-projects-authority-annual-report-2023-24-html)", Annex A. gov.uk (fetched 2026-08-07). Confirms the same five-point Delivery Confidence scale and prose definitions are still current government practice. [primary]

<a id="ref-3"></a>[3] National Audit Office. "[Delivering major projects in government: a briefing for the Committee of Public Accounts](https://www.nao.org.uk/briefings/delivering-major-projects-in-government-a-briefing-for-the-committee-of-public-accounts/)." nao.org.uk (fetched 2026-08-07). The UK's spending watchdog on RAG/DCA reliability ("it is difficult to tell whether performance is improving without reliable and consistent measures"; "Uncertainty should reduce through the project lifecycle but not all project ratings improve over time"). [primary]

<a id="ref-4"></a>[4] Association for Project Management. "[RAG status: using the tool the best way](https://www.apm.org.uk/blog/rag-status-using-the-tool-the-best-way/)." apm.org.uk (fetched 2026-08-07). A named chartered body treating threshold definition as an organisational, not a standard-supplied, responsibility ("the RAG needs to be clearly defined, it must be communicated and consistently applied"). [practitioner]

<a id="ref-5"></a>[5] PRINCE2 Wiki (unofficial community mirror). "[Highlight report](https://prince2.wiki/management-products/reports/highlight-report/)." prince2.wiki (fetched 2026-08-07). The only fully specified status-artifact methodology found: named producer, recipient, cadence, and purpose ("The highlight report provides a regular update on stage progress, prepared by the project manager for the project board."; "manage by exception between stage boundaries, ensuring they stay informed without unnecessary intervention"; "The frequency and format of this report are defined in the communication management approach."), and a caution rather than a definition on traffic lights ("be cautious with traffic light indicators to ensure clarity"). AXELOS's own manual is paywalled; this is a community mirror. [practitioner]

<a id="ref-6"></a>[6] Asana. "[Status report template](https://asana.com/templates/status-report)." asana.com (fetched 2026-08-07). Verbatim section list and cadence variants ("A summary of the project's current status"; "A status tag indicating project health"; "Specific accomplishments the team has achieved"; "The next steps"; "Daily status reports"; "Weekly status reports"; "Monthly status reports"; "Quarterly status reports"). [vendor]

<a id="ref-7"></a>[7] ProjectManagementDocs.com. "[Project Status Report](https://www.projectmanagementdocs.com/template/project-monitoring-and-controlling/project-status-report/)" template. projectmanagementdocs.com (fetched 2026-08-07). Full verbatim field structure, including the corpus's only KPI-formula and change-request fields ("Project Status Summary"; "Percent Complete:"; "Risks"; "Work Completed Last Week"; "Work Planned for Next Week"; "Open Issues"; "Open Risks"; "Deliverables and Milestones"; "Key Performance Indicators (KPI's)"; "Schedule Variance (SV):"; "Schedule Performance Index (SPI):"; "Cost Variance (CV):"; "Cost Performance Index (CPI):"). [practitioner]

<a id="ref-8"></a>[8] ProjectManager.com. "[Status report guide and worked example](https://www.projectmanager.com/guides/status-report)." projectmanager.com (fetched 2026-08-07). Core sections plus the corpus's only exact matches for two headings ("Project Summary"; "Issues and Risks"; "Project Metrics"; "Key Accomplishments"; "Action Items"; "Upcoming Work"; "Project Deliverables"; "Milestone Review"; "Project Health"). [vendor]

<a id="ref-9"></a>[9] TeamGantt. "[Project Status Report Template](https://www.teamgantt.com/project-status-report-template)." teamgantt.com (fetched 2026-08-07). Fully ordered section list for a single weekly template, including the corpus's only exact "Summary" heading match ("Introductory note"; "Summary"; "Overall project timeline completion"; "Budget status"; "Upcoming tasks and milestones"; "Action items"; "Project risks, issues, and mitigation plans"). [vendor]

<a id="ref-10"></a>[10] monday.com. "[Project status report template](https://monday.com/blog/project-management/project-status-report-template/)." monday.com (fetched 2026-08-07). Audience-specific variants and their distinct field sets ("Executive status report templates"; "Team status report templates"; "Portfolio status report templates"; "Agile project status template"; "Department status report template"). [vendor]

<a id="ref-11"></a>[11] Smartsheet. "[Weekly Status Report Templates](https://www.smartsheet.com/content/weekly-status-report-templates)" listicle. smartsheet.com (fetched 2026-08-07). Evidence of many named audience/team-specific variants ("Weekly Executive Status Report Template"; "Weekly IT Status Report Template"; "Weekly HR Status Report Template"; "Weekly Agile Sprint Status Report Template"; "Weekly Scrum Sprint Status Report Template"). Does not supply a single template's field structure. [vendor]

<a id="ref-12"></a>[12] Keil, Mark; Smith, H. Jeff; Iacovou, Charalambos L.; Thompson, Ronald L. "[The Pitfalls of Project Status Reporting](http://marketing.mitsmr.com/PDF/MITSMR-The-Pitfalls-of-Project-Status-Reporting.pdf?cid=1)." MIT Sloan Management Review, Spring 2014, Vol. 55 No. 3, pp. 56-64 (fetched 2026-08-07). Synthesis of 14 empirical studies from 1999 to 2013; this bundle's richest source ("we reviewed the records of 56 experienced software project managers and found that project managers write biased reports 60% of the time and that their bias is more than twice as likely to be optimistic... than pessimistic"; "our research suggests that the stronger the perceived power of the sponsor or the project leader, the less inclined subordinates are to report accurately"). The 2007 primary paper behind the 60 percent figure was not read directly; attribution runs through this synthesis. [practitioner]

<a id="ref-13"></a>[13] Löffler, Marc. "[Watermelon Reporting in Project Management](https://pmhut.com/watermelon-reporting-in-project-management)." PMHut, February 20, 2013 (fetched 2026-08-07). Earliest dated, byline-attributed web use of "watermelon reporting" found; does not itself claim to coin the term. [vendor]

<a id="ref-14"></a>[14] Thomsett, Rob. "[Thinking about Red Projects](https://www.linkedin.com/pulse/thinking-red-projects-rob-thomsett)." LinkedIn, September 15, 2021 (fetched 2026-08-07). A veteran consultant sometimes credited with coining "watermelon" instead calling it "the old joke about the Watermelon project", which undercuts single-coiner attribution. [practitioner]

<a id="ref-15"></a>[15] PPM Express. "[Project Status Reports vs. Dashboards: Which is Right for You](https://www.ppm.express/blog/project-status-reports-vs-dashboards-which-is-right-for-you)." ppm.express (fetched 2026-08-07). The external report-vs-dashboard distinction ("Project status reports are comprehensive documents that detail a project's progress, challenges, and next steps."; "A project status dashboard is a visual representation of real-time project data."; "typically shared periodically (e.g., weekly or monthly)"). [vendor]

<a id="ref-16"></a>[16] winningpresentations.com. "[Steering Committee Presentation: How to Drive Decisions Instead of Status Updates](https://winningpresentations.com/steering-committee-presentation/)." winningpresentations.com (fetched 2026-08-07). The clearest named-source boundary between a status update and a decision paper ("In a status update, the presenter opens with a report... In a decision session, the presenter opens with a decision ask"; "Status updates present every metric on every dimension - comprehensive coverage that creates decision paralysis"). [practitioner]

<a id="ref-17"></a>[17] The PM Professional. "[Writing a Project Status Report That Actually Gets Read](https://thepmprofessional.com/2025/03/project-status-reports/)." thepmprofessional.com (fetched 2026-08-07). Names three audience tiers with distinct content priorities and recommends tailoring per audience rather than one report for everyone ("Don't send the same report to everyone. Create a core report and tailor the intro or format slightly depending on the audience."). [practitioner]

<a id="ref-18"></a>[18] iZenBridge. "[Work Performance Data, Work Performance Information, and Work Performance Report](https://www.izenbridge.com/blog/work-performance-data-wpd-work-performance-information-wpi-work-performance-report-wpr/)." izenbridge.com (fetched 2026-08-07). The closest analog to a no-new-facts rule found, and explicitly not a direct match: describes PMBOK's chain from raw observation to compiled report ("the physical or electronic representation of work information compiled in project documents, intended to generate decisions, actions, or awareness") without stating a traceability rule or prohibiting new facts by name. [practitioner]

<a id="ref-19"></a>[19] This library, internal. [`kpi-dashboard_companion.md`](../kpi-dashboard/kpi-dashboard_companion.md). Fetched 2026-08-07. This library's own kpi-dashboard bundle defines a dashboard as a document that "DEFINES a dashboard - not a live BI tool", which complicates the external static-versus-live report/dashboard framing. [standards]

<a id="ref-20"></a>[20] Williams, Craig. "[Why Nobody Reads Your Excellent Status Reports](https://www.linkedin.com/pulse/20140603150756-11371473-why-nobody-reads-your-excellent-status-reports)." LinkedIn, June 2014 (fetched 2026-08-07). Names the report-nobody-reads failure directly ("It's easy for shared service teams like IT, HR, Legal, etc. to stop at the status report and kid themselves into thinking that it's their communications plan."). [practitioner]

<a id="ref-21"></a>[21] TeamRetro. "[Agile Theatre: how agile ceremonies fail](https://www.teamretro.com/guides/agile-theatre/)" field guide. teamretro.com (fetched 2026-08-07). Names "status-theatre stand-ups" directly, whose real audience is the most senior person present rather than the team ("Everyone reports to the most senior person in the room"). [practitioner]

<a id="ref-22"></a>[22] Cagan, Marty / Silicon Valley Product Group. "[The Alternative to Roadmaps](https://www.svpg.com/the-alternative-to-roadmaps/)." svpg.com (fetched 2026-08-07). Argues for outcome over output in roadmap reporting specifically ("It is all about outcome rather than output."); the transfer to status reports elsewhere in this companion is this library's inference, not Cagan's claim. [practitioner]

<a id="ref-23"></a>[23] Rothman, Johanna. "[Traffic Lights and Project Status](https://www.jrothman.com/mpd/project-management/2011/03/traffic-lights-and-project-status/)." jrothman.com, 2011 (fetched 2026-08-07). Documents status lights that stay yellow or red on long projects while management expects improvement without intervention ("on serial lifecycle projects, or on long projects, the traffic light was always yellow or red"). [practitioner]

<a id="ref-24"></a>[24] Siegel, Adam (CEO, Cultivate Labs). "[The Traffic Light Metaphor for Project Status is a Disaster](https://www.cultivatelabs.com/posts/the-traffic-light-metaphor-for-project-status-is-a-disaster)." March 2018 (fetched 2026-08-07). Strongest verified source for status numbers becoming disconnected from ground truth through political self-protection ("The information they're getting is based on hopes and prayers."; "Everyone working on a red project knows the project is on a path to failure. They discuss it... but in an official setting? Silence."). [vendor]

<a id="ref-25"></a>[25] Lewis, Bob, quoted/summarized via CIO.com. "[Project management has a status problem](https://www.cio.com/article/4142004/project-management-has-a-status-problem.html)." cio.com (fetched 2026-08-07). Names the "scarlet letter" effect where a project once marked yellow or red cannot recover its reputation regardless of a new plan ("new plan or no new plan, the project's degraded status... is a scarlet letter"). [practitioner]

<a id="ref-26"></a>[26] Agile Alliance. "[Information Radiators](https://agilealliance.org/glossary/information-radiators/)" glossary entry. agilealliance.org (fetched 2026-08-07). The canonical definition of the information-radiator concept. This entry does not itself claim radiators replace status reporting; that argument comes from sources [[27]](#ref-27) through [[29]](#ref-29) below. [standards]

<a id="ref-27"></a>[27] ScrumPLoP. "[Information Radiator](https://sites.google.com/a/scrumplop.org/published-patterns/value-stream/information-radiator)" published pattern. scrumplop.org (fetched 2026-08-07). The clearest verified statement that a good radiator makes formal status reporting meetings largely unnecessary ("Good information radiators... largely eliminate the need for formal status reporting meetings in an agile environment."). [practitioner]

<a id="ref-28"></a>[28] Fowler, Martin (with co-authors, quoting Bret Pettichord). "[It's Not Just Standing Up: Patterns for Daily Standup Meetings](https://martinfowler.com/articles/itsNotJustStandingUp.html)." martinfowler.com (fetched 2026-08-07). Proposes replacing separate status meetings and reports with the daily stand-up, while noting the replacement is partial ("Replace some or all of the meetings and reports with the daily stand-up"; "Not all forms of reporting will be, nor should be, covered by the stand-up format"). [practitioner]

<a id="ref-29"></a>[29] Lankford, Todd. "[Surviving Agile Without a Status Report: Visualize the Work](https://coachlankford.com/2019/05/12/surviving-agile-without-a-status-report-visualize-the-work/)." coachlankford.com, May 2019 (fetched 2026-08-07). The sharpest verified statement of the polemic against written status reporting ("Engaging with your teams and visualizing the work outperforms the status report every time."). [practitioner]

<a id="ref-30"></a>[30] PMBOK Guide communications-management content, as mirrored on Wikibooks. "[Project Management/PMBOK/Communications Management](https://en.wikibooks.org/wiki/Project_Management/PMBOK/Communications_Management)." wikibooks.org (fetched 2026-08-07). The defence-of-written-reporting side: reports as deliberate push communication that prevents surprises ("a clear understanding of what you are doing. There should be no surprises for them"). A Wikibooks community mirror, not PMI's own text, which 403'd on fetch; descriptive rather than an argued rebuttal of the radiator case. [standards]
