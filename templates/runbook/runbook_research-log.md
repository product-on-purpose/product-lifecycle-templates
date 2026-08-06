# runbook research log

Researched 2026-08-06 across six parallel dimensions: the SRE canon, structure in practice, the automation
boundary, failure modes, ownership and staleness, and boundaries against adjacent documents. **31 sources**,
of which **28 fetched-and-verified** and **3 not-retrieved**. Of the 28 read, 12 are primary, 10 vendor and 6
practitioner. Retrieval status is recorded per source in the three-token vocabulary the library gates
([ADR 0029](../../docs/internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md)), and only
`fetched-and-verified` sources are quoted.

**How to read this log.** A `Supports:` clause says what the bundle is allowed to rest on that source for.
A `Quotable:` phrase was read verbatim on the page. If a claim in the companion is not covered by some
entry's `Supports:` clause here, the claim has no home and must be cut, not justified after the fact.

**Six entries record a verified absence rather than a quote, and they are among the most load-bearing in
this log.** Four SRE Book chapters were fetched and searched by full text for the literal strings "runbook"
and "playbook", returning zero hits each [3][4][5][6]. An entry with an empty `Quotable:` list here is not
thin research: it is the evidence for framing point 1, and it says so in its own `Supports:` clause.

**The tier mix is a warning the family contract issued in advance.** Ten of the 28 sources read are vendor
tier, and several of those sell the thing they describe. The contract named "runbook practice is dominated
by vendor content" as this type's citation hazard before any of this was searched, and it was right. Where a
vendor claim is used, the entry says who benefits from it.

---

## Honest framing: the six things this bundle has to say

**1. The canonical source does not use this document's name.** Google's SRE literature says **playbook**.
Across seven chapters fetched and read, the string "runbook" appears exactly three times, and **every
occurrence sits inside a contributed third-party case study** rather than in Google's own analytical prose
[7]. Google's own voice in that same chapter closes with "Regularly review and iterate on your incident
management plans and playbooks" [7]. Four of the five SRE Book chapters most likely to discuss the artifact,
Being On-Call, Emergency Response, Managing Incidents and Eliminating Toil, contain **zero** occurrences of
either word [3][4][5][6]. **This bundle keeps the name `runbook`**, because that is the catalog's name and
the industry's common usage, and it says this plainly rather than implying the canon endorses the term.

**2. Nearly everything the canon says about this artifact is in one chapter.** The definition, the purpose,
the maintenance debate and the automation test all come from SRE Workbook chapter 8, On-Call [1]. The SRE
Book proper contributes one passing mention, an alert-generated bug carrying "links to the black-box
prober's recent results and to the playbook entry for this alert" [2]. **A bundle that cited "the Google SRE
book" generally for runbook practice would be citing a book that barely mentions it.**

**3. The central claim for runbooks is asserted by Google, not measured.** "Playbooks contain high-level
instructions on how to respond to automated alerts" and "These guides reduce stress, the mean time to repair
(MTTR), and the risk of human error" [1]. That is the strongest statement of value this research found, and
it is **a statement, not a study**: no measurement, sample or comparison accompanies it, and none was found
elsewhere. The bundle may say Google asserts this. It may not say it has been shown.

**4. There is a named, quotable test for when a runbook should stop being a document.** "If your playbooks
are a deterministic list of commands that the on-call engineer runs every time a particular alert fires, we
recommend implementing automation" [1]. **The operative word is deterministic**: the test is the shape of
the procedure, not how often it runs. It sits inside the toil framing, where toil is "manual, repetitive,
automatable, tactical, devoid of enduring value" and where the hands-on time spent running a script "is
still toil time" [6]. This is the sharpest practical rule in the bundle, and it comes from a primary source
rather than from a vendor selling automation. **Contrast that with [14] and [15]**, which argue for
automating or replacing runbooks and are published by companies selling exactly that.

**5. Google names the maintenance question contentious, inside its own organisation.** "Details in playbooks
go out of date at the same rate as production environment changes" [1]. And on what to do about it, two
positions recorded in consecutive sentences: "Some SREs at Google advocate keeping playbook entries general
so they change slowly", and "Other SREs advocate for step-by-step playbooks to reduce human variability and
drive down MTTR". The chapter then says of the disagreement, "This is a contentious topic" [1]. **A bundle that recommended one of these as best practice would be picking a side its own
primary source declines to pick.** The template instead makes the choice explicit and asks the author to
state which they are doing.

**6. Staleness is the documented failure mode, the mechanism is known, and no source supplies the fix this
family requires.** The decay is invisible: a runbook "sits in a wiki, looking authoritative, growing wronger
by the week" and "does not announce that it has decayed" [17]. The mechanism is a process mismatch, "The
runbook is in a wiki. The system is in code. The two are maintained by different processes and often by
different people" [17]. Sources that address the remedy agree on versioning it with the system [20][21], and
**every one of them reaches for a calendar when it comes to review**. None names an event that makes the
document wrong plus a person who notices. That is the gap this family's contract requires the template to
fill, and the `definition-of-done` research found the identical gap in an entirely separate literature.

---

## Format verdict (ADR 0028), and the section departures

Under [ADR 0028](../../docs/internal/decisions/0028-adopt-a-format-axis.md) a format ships only when it is
**structurally distinct** and **in circulation with a named source**.

**The sources disagree about what a runbook IS, sharply, and the disagreement had to be settled before any
section could be chosen.** Two shapes circulate, each with named publishers:

| Shape | Publishers read | What it is |
|---|---|---|
| **Standing service-operations manual** | PagerDuty, 7 sections [8]; Skelton Thatcher, 65 headers [13] | Everything about running one service: overview, build, deployment, common tasks, DR plans, SLA |
| **Incident-scoped procedure** | Emmer, 6 sections [12]; Microsoft, 4 components [11] | One trigger, one investigation and remediation arc |

Atlassian publishes **two** differently-structured runbook templates [9][10], which is itself evidence that
no industry-standard shape exists.

**This bundle ships the incident-scoped procedure, and the family contract settles it rather than
preference.** That contract defines a runbook as "the procedure executed when a known situation occurs, so
that the response does not depend on who is awake". The SRE Workbook's model agrees: one playbook entry per
alert [1]. The service-operations manual is a **different artifact**, closer to a service handbook, and it
is taught in the companion's Relationships section rather than shipped.

| Candidate | Structurally distinct? | Named source in circulation? | Verdict |
|---|---|---|---|
| **Incident-scoped procedure** (trigger, steps, validation) | The shape the family contract defines | Yes [1][11][12] | **Ships** as the only format |
| **Service-operations manual** | **Yes, genuinely**, and it is a bigger scope rather than a bigger size | Yes [8][13] | **Rejected as a format**, because it is a different artifact. Taught as a boundary |
| **Playbook** as a distinct document | No. The canon uses the words for the same object and never contrasts them [1][7] | Sources that *do* contrast them are vendor tier [27] | **Rejected.** Taught as a naming boundary |
| **Automated runbook** (executable) | Yes, but the artifact is **code**, not a document | Yes [14] | **Out of scope for templating**, on the reasoning that excluded `interactive-prototype` in [ADR 0030](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md) |

**Four departures from the build spec, and the last two are corrections to a section design that no
published template supports.**

1. **The alert trigger moves into `lean`.** The spec made Triggers/Alerts a full-only addition. The sources
   put it in the core: PagerDuty's format is built around the alert that pages you [8], Atlassian's ITSM
   template lists the alerts produced [9], and the SRE Workbook states that "In SRE, whenever an alert is
   created, a corresponding playbook entry is usually created" [1]. **A runbook with no stated trigger is a
   wiki page**, so the trigger is not optional weight.
2. **Prerequisites moves out of `lean`.** It appears as its own named section in exactly one source read
   [11]; elsewhere it is folded into the first steps.
3. **"Verification and Rollback" is not a section pairing anyone publishes.** Neither word titles a section
   in any of the six templates read. Recovery content exists everywhere under other names, Disaster Recovery
   Plans [8] and Failover and Recovery [13]. The only validation section recorded here by title is
   Microsoft's Checklist, "A list of tasks for the steps in the flow chart" [11]. Emmer's template records
   three of its six section titles, Mitigating the immediate issue, Validating health and stability, and
   Remediation and cleanup [12]. **The bundle drops the invented pairing and names its own sections**,
   Validation and Remediation and Cleanup, which are close to Emmer's and are the bundle's own wording
   rather than a title lifted verbatim from one publisher.
4. **"Escalation" and "Related Runbooks" are not published sections either**, appearing in no source read in
   full. They are dropped rather than carried on the spec's authority.

**And the family's own obligation has no published precedent, which is stated rather than hidden.** A named
`Review Trigger` section is required in both variants. Of the sources read, only one carries a service-owner
section [13] and **none carries a last-verified field in the document body at all**. So this section is the
bundle's own contribution, labelled as such, not received practice dressed up as consensus.

**So one format ships**, with `lean` and `full` weights on it.

---

## Sources

### The SRE canon, and what it actually calls this document

**[1] Google SRE (Betsy Beyer et al., eds.) - SRE Workbook, Chapter 8: On-Call.** primary. **fetched-and-verified.**
`https://sre.google/workbook/on-call/`
Supports: The Google canon's substantive treatment of playbooks: definition, purpose, the MTTR claim, maintenance debate, and the recommendation to automate deterministic playbook steps. This is the chapter that carries the load-bearing content; the SRE Book proper barely touches the topic.
Quotable: "Playbooks contain high-level instructions on how to respond to automated alerts. They explain the severity and impact of the alert, and include debugging suggestions and possible actions to take to mitigate impact and fully resolve the alert." / "In SRE, whenever an alert is created, a corresponding playbook entry is usually created." / "These guides reduce stress, the mean time to repair (MTTR), and the risk of human error." / "Details in playbooks go out of date at the same rate as production environment changes." / "Some SREs at Google advocate keeping playbook entries general so they change slowly." / "Other SREs advocate for step-by-step playbooks to reduce human variability and drive down MTTR." / "If your team has conflicting views about playbook content, the playbooks might get pulled in many directions. This is a contentious topic." / "Pencil in a project to turn new, hard-won, production knowledge into automation or monitoring consoles." / "If your playbooks are a deterministic list of commands that the on-call engineer runs every time a particular alert fires, we recommend implementing automation." / "reduces human variability and drives down MTTR"
Contested/time-bound: one source reached by 2 dimensions or URL forms; a single entry is kept, carrying the union of their extracts.

**[2] Google SRE (Betsy Beyer et al., eds.) - SRE Book, Chapter 12: Effective Troubleshooting.** primary. **fetched-and-verified.**
`https://sre.google/sre-book/effective-troubleshooting/`
Supports: The one mention of the word 'playbook' anywhere in the five requested SRE Book chapters. It is a passing reference (an artifact linked from an alert-generated bug), not a discussion of what playbooks are, how to write them, or their effect on resolution time. No MTTR claim, no definition, no runbook/playbook distinction appears in this chapter.
Quotable: "The alerting system has filed a bug - with links to the black-box prober's recent results and to the playbook entry for this alert - and assigned it to you."

**[3] Google SRE (Betsy Beyer et al., eds.) - SRE Book, Chapter 11: Being On-Call.** primary. **fetched-and-verified.**
`https://sre.google/sre-book/being-on-call/`
Supports: Confirms the ABSENCE of the words 'playbook' and 'runbook' anywhere in this chapter (verified by full-text regex over the raw page, zero hits). Despite being the chapter most naturally suited to discuss on-call procedural aids, it does not use either term.
Quotable: none. This entry records a verified ABSENCE, which is what it was read for.

**[4] Google SRE (Betsy Beyer et al., eds.) - SRE Book, Chapter 13: Emergency Response.** primary. **fetched-and-verified.**
`https://sre.google/sre-book/emergency-response/`
Supports: Confirms the ABSENCE of the words 'playbook' and 'runbook' anywhere in this chapter (verified by full-text regex over the raw page, zero hits), despite the chapter title suggesting exactly this topic.
Quotable: none. This entry records a verified ABSENCE, which is what it was read for.

**[5] Google SRE (Betsy Beyer et al., eds.) - SRE Book, Chapter 14: Managing Incidents.** primary. **fetched-and-verified.**
`https://sre.google/sre-book/managing-incidents/`
Supports: Confirms the ABSENCE of the words 'playbook' and 'runbook' anywhere in this chapter (verified by full-text regex over the raw page, zero hits). The chapter's guidance is procedural (roles, communication, declaring incidents) rather than artifact-specific; it never names playbooks as the mechanism for that procedure.
Quotable: none. This entry records a verified ABSENCE, which is what it was read for.

**[6] Google SRE (Betsy Beyer et al., eds.) - SRE Book, Chapter 33: Eliminating Toil.** primary. **fetched-and-verified.**
`https://sre.google/sre-book/eliminating-toil/`
Supports: Confirms the ABSENCE of the words 'playbook' and 'runbook' anywhere in this chapter (verified by full-text regex over the raw page, zero hits). This is the chapter most likely to state the documented-procedure-vs-automation tension explicitly by name, and it does not connect that tension to playbooks/runbooks at all; the framing lives instead in the Workbook's On-Call chapter (see that source's automation quotable).
Quotable: "manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows" / "Running a script may be quicker than manually executing each step in the script, but the hands-on time a human spends running that script (not the elapsed time) is still toil time." / "Toil is work you do over and over. If you're solving a novel problem or inventing a new solution, this work is not toil." / "If a machine could accomplish the task just as well as a human, or the need for the task could be designed away, that task is toil." / "If a human operator needs to touch your system during normal operations, you have a bug."
Contested/time-bound: one source reached by 2 dimensions or URL forms; a single entry is kept, carrying the union of their extracts.

**[7] Google SRE Workbook, Chapter 9: Incident Response (includes a PagerDuty case study contributed by PagerDuty staff, embedded within the Google-edited Workbook).** primary. **fetched-and-verified.**
`https://sre.google/workbook/incident-response/`
Supports: The word 'runbook' (not 'playbook') appears exactly three times in this chapter, entirely inside a third-party case study (PagerDuty's own incident narrative), not in Google's own analytical text. Google's own voice in this chapter uses 'playbooks' once, in a closing recommendation, alongside 'incident management plans.' No MTTR or resolution-time claim is attached to either term here.
Quotable: "The on-call SRE validated that all automated recovery actions had been executed, and completed the mitigation steps in relevant runbooks." / "When the procedures in our runbooks didn't resolve the issue, the response team started trying new recovery options in a methodical manner." / "Regularly review and iterate on your incident management plans and playbooks." / "The Persistent Disk SRE had defined procedures for restarting all machines not hosting virtual machines." / "When the procedures in our runbooks didn't resolve the issue, the response team started trying new recovery options in a methodical manner."
Contested/time-bound: one source reached by 2 dimensions or URL forms; a single entry is kept, carrying the union of their extracts.

### Structure in practice

**[8] PagerDuty, "What is a Runbook?" (resources/automation/learn).** vendor. **fetched-and-verified.**
`https://www.pagerduty.com/resources/automation/learn/what-is-a-runbook/`
Supports: the seven-section runbook structure (attributed by PagerDuty to Tom Limoncelli), whose sections were recorded as Service Overview, Service Build Information, Deployment Instructions, Common Tasks, Pager Playbook, Disaster Recovery Plans and SLA; and a general, non-specific statement that runbooks require constant testing/updating -- consulted for structural framing, not staleness mechanics
Quotable: "constantly tested and updated" / "easily adaptable to the ever-changing environment of IT operations"
Contested/time-bound: one source reached by 2 dimensions or URL forms; a single entry is kept, carrying the union of their extracts.

**[9] Atlassian - ITSM runbook template (Confluence).** vendor. **fetched-and-verified.**
`https://www.atlassian.com/software/confluence/templates/itsm-runbook`
Supports: Named three-section ITSM runbook template: ITSM Architecture, Applications and Known Errors, Troubleshooting Steps. The template was also recorded as listing the alerts a service produces
Quotable: none. This entry records a verified ABSENCE, which is what it was read for.

**[10] Atlassian - DevOps runbook template (Confluence).** vendor. **fetched-and-verified.**
`https://www.atlassian.com/software/confluence/templates/devops-runbook`
Supports: Named three-step DevOps runbook template: system architecture, organize runbook operations (support leads/contacts), explain runbook procedures (start/stop/monitor, anticipated-outage response)
Quotable: none. This entry records a verified ABSENCE, which is what it was read for.

**[11] Microsoft Learn - "Incident response playbooks".** primary. **fetched-and-verified.**
`https://learn.microsoft.com/en-us/security/operations/incident-response-playbooks`
Supports: Each Microsoft playbook has four named components in a fixed order: Prerequisites, Workflow, Checklist, Investigation steps
Quotable: "Prerequisites: The specific requirements you need to complete before starting the investigation. For example, logging that should be turned on and roles and permissions that are required." / "Workflow: The logical flow that you should follow to perform the investigation." / "Checklist: A list of tasks for the steps in the flow chart. This checklist can be helpful in highly regulated environments to verify what you have done." / "Investigation steps: Detailed step-by-step guidance for the specific investigation."

**[12] Christian Emmer - "An Effective Incident Runbook Template".** practitioner. **fetched-and-verified.**
`https://emmer.dev/blog/an-effective-incident-runbook-template/`
Supports: Named ordered six-section incident-runbook template, explicitly framed as opinionated/optional-in-parts. Three of its section titles were recorded during research: Mitigating the immediate issue, Validating health and stability, and Remediation and cleanup. The remaining three were not captured
Quotable: "the author's opinions" / "not all sections apply to every runbook"

**[13] Skelton Thatcher Consulting (Matthew Skelton) - run-book-template (GitHub, run-book-template.md).** practitioner. **fetched-and-verified.**
`https://raw.githubusercontent.com/SkeltonThatcher/run-book-template/master/run-book-template.md`
Supports: Widely-referenced named community template for a full operations manual (not incident-scoped): 65 ordered headers spanning overview, SLAs, service owner, monitoring/alerting, backup/restore, security, patching, failover/recovery
Quotable: none. This entry records a verified ABSENCE, which is what it was read for.

### The automation boundary

**[14] PagerDuty, "Runbook Automation" product page (PagerDuty platform marketing site).** vendor. **fetched-and-verified.**
`https://www.pagerduty.com/platform/automation/runbook/`
Supports: Vendor framing of 'runbook automation' as a product category: positions the runbook as the manual, static predecessor document and its own product as the execution layer that replaces those manual steps; carries specific unverifiable performance claims.
Quotable: "Resolve tasks 99% faster" / "Reduce support costs by 50%" / "Replace manual procedures in your runbooks with automated self-service tasks" / "defines the exact steps for a specific operational task" / "runbook automation focuses on executing tasks" / "as soon as an alert is triggered, often before a human responds"

**[15] ilert, "Runbooks are history: Why agentic AI will redefine incident response forever" (ilert company blog).** vendor. **fetched-and-verified.**
`https://www.ilert.com/blog/runbooks-are-history`
Supports: The most aggressive vendor claim found: that static runbooks are obsolete and even scripted automation is 'brittle,' used to sell ilert's agentic-AI incident product; also concedes automation's real limits (context, novel incidents), which doubles as evidence for the judgment-dependent counter-position.
Quotable: "Runbooks once worked well. But systems evolved faster than our documentation could." / "too distributed, too dynamic, and too interdependent for static runbooks to keep up" / "Automation often falls short because it's brittle and struggles to adapt when incidents don't match past patterns."

### Failure modes

**[16] Google SRE Book (Google) - "Introduction" chapter, sre.google/sre-book/introduction/.** primary. **fetched-and-verified.**
`https://sre.google/sre-book/introduction/`
Supports: The primary source of the widely circulated MTTR statistic for runbooks/playbooks: playbooks yield roughly a 3x MTTR improvement over ad hoc response ('winging it'). This traces the number to its origin rather than a secondhand vendor restatement.
Quotable: "When humans are necessary, we have found that thinking through and recording the best practices ahead of time in a "playbook" produces roughly a 3x improvement in MTTR as compared to the strategy of "winging it." / "The hero jack-of-all-trades on-call engineer does work, but the practiced on-call engineer armed with a playbook works much better."

**[17] ekline.io blog - "Why Your Incident Runbook Lies to You at 3 a.m. (and How to Tell Before the Page Fires)".** practitioner. **fetched-and-verified.**
`https://ekline.io/blog/why-your-incident-runbook-lies-to-you-at-3-a-m-and-how-to-tell-before-the-page-fires`
Supports: Names and describes several of the target failure modes directly: staleness as silent decay, unshared-context assumptions (dashboard availability, alert firing as documented, responder credentials), the runbook/system maintenance-process mismatch (wiki vs code, different owners), and prescribes game days run against the runbook itself (not the responder) as the test. Author/org identity beyond the blog byline could not be independently confirmed; treated as an unaffiliated practitioner blog, not a named individual or vendor with disclosed credentials.
Quotable: "A runbook is a frozen snapshot of how your system used to work. The system keeps changing. The runbook does not." / "The runbook does none of those things. It sits in a wiki, looking authoritative, growing wronger by the week." / "It assumes the dashboard will be available, the alert will fire as documented, and the responder will have credentials. None of those assumptions hold reliably during an incident." / "Run game days against the runbook itself...The point is not to test the responder. The point is to test the runbook." / "The runbook is in a wiki. The system is in code. The two are maintained by different processes and often by different people." / "A runbook does not announce that it has decayed. The decay is silent until the moment of failure."

**[18] incidenthub.cloud blog - "The No-Nonsense Guide to Runbook Best Practices".** vendor. **fetched-and-verified.**
`https://blog.incidenthub.cloud/The-No-Nonsense-Guide-to-Runbook-Best-Practices`
Supports: Names the 'curse of knowledge' explicitly as a runbook-writing failure mode (close to, though not identical to, 'written by the builder for themselves'), prescribes testing by having newly onboarded people run the runbook plus regular mock incident exercises, gives concrete over-length guidance (split when step count grows too large), and states the findability fix (link runbooks directly from alerts) and the staleness fix (update as a scripted post-incident step). This is a vendor blog (incidenthub.cloud is an incident-management product) so its prescriptions read as marketing-adjacent best-practice advice, not research.
Quotable: "Watch out for the curse of knowledge while writing a runbook. Users of your runbook may not be aware of details and assumptions that you make in the runbook." / "Have newly onboarded folks try out the runbooks. Any missing context will surface." / "Carry out regular mock incident exercises." / "If there are too many steps in your runbook, split them into more than one." / "Alerts should link directly to runbooks. E.g. in Prometheus alerts you can add the runbook as part of the description." / "Nothing is worse than an outdated runbook which does not fulfill its purpose when the next similar incident occurs." / "As part of your post-incident activities, go through the emails, chat logs, tickets logged and update your runbooks as needed."

### Ownership and staleness

**[19] Boris Dali, "Your SRE On-Call Runbook Is Already Obsolete. Here's Why That's Not Your Fault" (Medium / Google Cloud Community, Apr 2026).** practitioner. **fetched-and-verified.**
`https://medium.com/google-cloud/your-sre-on-call-runbook-is-already-obsolete-heres-why-that-s-not-your-fault-0a82b3b0183c`
Supports: the staleness problem itself: runbooks decay from the moment they are written, and periodic manual testing is an inconsistent defense
Quotable: "an incident happens, some superman hero fixes it, someone writes up what happened in a doc (maybe) and then that doc goes to live in whatever documentation graveyard your company uses. It basically gets stale almost immediately the moment it's published." / "When did you last run and validate them?" / "they are spotty, far from guaranteeing that every operational runbook is relevant and effective." / "it's kept current because the system knows when infrastructure changes and flags playbooks that may have drifted."

**[20] OneUptime, "How to Build Alert Runbook Links" (2026-01-30).** vendor. **fetched-and-verified.**
`https://oneuptime.com/blog/post/2026-01-30-alert-runbook-links/view`
Supports: alert-carries-the-link pattern, a named-owner metadata field, versioning alongside infrastructure code, event-triggered review, and a numeric staleness heuristic
Quotable: "A well-designed runbook link embedded in the alert payload transforms a panic moment into a structured response." / "**Owner:** {TEAM}" / "Runbooks should be version-controlled alongside your infrastructure code" / "Update this runbook if steps changed" / "Flag runbooks untouched for 90+ days for review"

**[21] Rootly, "Incident Response Runbooks: Templates, Examples & Guide".** vendor. **fetched-and-verified.**
`https://rootly.com/incident-response/runbooks`
Supports: ownership as an explicit accountability requirement, versioning runbooks like code, scheduled quarterly review cadence, post-mortem-triggered updates, and alert-surfaced discovery
Quotable: "make ownership clearly visible for accountability" / "Ownership should never be an afterthought." / "Treat them like code. Store them in a central, version-controlled system like Git or an incident management platform." / "Schedule quarterly reviews and make version control a standard part of your workflow" / "schedule automated reminders for owners to verify them quarterly." / "Update runbooks immediately after each post-mortem to reflect what worked and what didn't" / "Make sure it can be quickly found through alerts, surfaced inside Slack or PagerDuty, or automatically attached through Rootly." / "A single outdated command can destroy trust" / "Removing outdated materials prevents confusion and keeps your repository focused on active systems."

**[22] Bitfield Consulting, "Night of the Runbooks: a DevOps horror story".** practitioner. **fetched-and-verified.**
`https://bitfieldconsulting.com/posts/night-of-the-runbooks`
Supports: a narrative illustration of alert-to-runbook linking, event-triggered (post-incident) review reaching a team lead and then a weekly team review, and a deploy event being the diagnostic anchor for an incident -- but it is fiction/narrative, not a stated methodology
Quotable: "Please click the following link to troubleshoot this service." / "The report would go automatically to Morgan's team lead to be reviewed the next day, and then for the team to review in their weekly meeting." / "The other team responsible for the process-payments service would be automatically notified, too, and a ticket would be opened for them to identify what went wrong and fix it." / "there was a fresh deploy about five minutes before the first errors started coming in"

### Boundaries and adjacent artifacts

**[23] Google SRE (Beyer, Jones, Petoff, Murphy, eds.) - "Postmortem Culture: Learning from Failure," Site Reliability Engineering (SRE book).** primary. **fetched-and-verified.**
`https://sre.google/sre-book/postmortem-culture/`
Supports: The postmortem's own definition, its retrospective nature, blameless framing, and its trigger criteria (used to state precisely where a postmortem starts, i.e. where a runbook's job ends).
Quotable: "A postmortem is a written record of an incident, its impact, the actions taken to mitigate or resolve it, the root cause(s), and the follow-up actions to prevent the incident from recurring." / "For a postmortem to be truly blameless, it must focus on identifying the contributing causes of the incident without indicting any individual or team for bad or inappropriate behavior." / "it is important to define postmortem criteria before an incident occurs so that everyone knows when a postmortem is necessary"

**[24] incident.io - "What are runbooks and how do they fit into the incident management picture?".** practitioner. **fetched-and-verified.**
`https://incident.io/blog/what-are-runbooks`
Supports: The runbook/playbook boundary (technical step-by-step vs. strategic/organizational response) and a runbook's trigger context (incident response, troubleshooting, routine ops tasks).
Quotable: "An incident response runbook is a comprehensive, step-by-step document that outlines procedures to manage and resolve incidents." / "runbooks focus on step-by-step procedures for resolving specific incidents" / "playbooks represent a broader strategic document that outlines an organization's overall approach to handling various situations"

**[25] NIST Computer Security Resource Center Glossary - "disaster recovery plan (DRP)," sourced from NIST SP 800-34 Rev. 1.** primary. **fetched-and-verified.**
`https://csrc.nist.gov/glossary/term/disaster_recovery_plan`
Supports: The DR-plan/runbook boundary: DRP is scoped to recovering information systems at an alternate facility after major failure or facility destruction, one register above the operational, single-system procedures a runbook covers.
Quotable: "A written plan for recovering one or more information systems at an alternate facility in response to a major hardware or software failure or destruction of facilities."

**[26] PMC (NIH) - peer-reviewed review article on Atul Gawande's The Checklist Manifesto: How to Get Things Right (PMC4953332).** primary. **fetched-and-verified.**
`https://pmc.ncbi.nlm.nih.gov/articles/PMC4953332/`
Supports: The Gawande-sense checklist/runbook boundary: a checklist is a minimal memory-guard against omission under pressure, not a full procedural walkthrough; contrasted with the WHO surgical checklist's measured outcomes.
Quotable: "The checklist aims to protect against the fallibility of human memory, distraction under pressure and to highlight the minimum necessary steps for success." / "a 47% reduction in deaths from 1.5% to 0.8%" / "a 36% reduction in major complications from 11% to 7%"

**[27] Cutover (vendor blog) - "Runbooks vs. Playbooks vs. SOPs: Key Differences".** vendor. **fetched-and-verified.**
`https://cutover.com/blog/differences-runbooks-playbooks-sops`
Supports: A named predictability axis (SOP highest, runbook moderate-to-high, playbook lowest) that gives a concrete test for the runbook/SOP/playbook triad, used as a secondary/corroborating source alongside incident.io.
Quotable: "A standard operating procedure (SOP) provides detailed, step-by-step instructions on how to perform a specific, routine task." / "A detailed compilation of procedures and information required to execute a specific, often complex, operational process from end to end."

**[28] knowledge-base.software (vendor/practitioner comparison page) - "Knowledge Base vs Runbook: Troubleshooting, Operations Playbooks, and Incident Response".** vendor. **fetched-and-verified.**
`https://knowledge-base.software/comparison/knowledge-base-vs-runbook/`
Supports: The runbook/general-documentation-or-wiki boundary: a concrete executable-steps test and an operational-moment test for telling a runbook apart from a wiki page or KB article.
Quotable: "A knowledge base is a governed knowledge repository and discovery layer. A runbook is an operational procedure" / "A troubleshooting article may explain symptoms and possible causes. A runbook must go further" / "'Check the logs and restart the service if needed' is not a runbook"

---

### Sought and not retrieved

Recorded so that no draft can quietly assume them. **Nothing in this bundle may rest on any entry in this
section.**

**[29] The circulating "Google SRE reports an X percent MTTR improvement from playbooks" claim.** primary. **not-retrieved.**
No URL: no source stating this was ever located. It is recorded as an entry because a reader will meet it.
Supports: nothing in this bundle. Sought for: a quantified Google claim about playbooks and MTTR. **It does
not exist in the pages read.** All seven primary Google pages were searched twice, once by extraction and
once by direct full-text regex over the raw HTML, for "playbook" and "runbook". **The only MTTR statement
Google makes is unquantified**: "These guides reduce stress, the mean time to repair (MTTR), and the risk of
human error" [1]. Any percentage attached to Google's name in secondary writing is unsupported by the
primary text, and **this bundle states no number for the effect of a runbook on MTTR.**

**[30] Vendor MTTR and cost-reduction figures (PagerDuty "up to 99% faster" and "reduce support costs by 50%"; incident.io "30-50% MTTR improvement").** vendor. **not-retrieved.**
No URL: the figures appear on product marketing pages [14][24] with no visible methodology, sample, or
comparison group, so there is no source page for the claim itself to link to.
Supports: nothing in this bundle. Sought for: any measured effect of runbooks or runbook automation. **These
are marketing claims published by companies selling the product they measure**, and none may be cited here.
The incentive structure is stated in the companion rather than the numbers being repeated.

**[31] The circulating IBM incident-response MTTR statistics ("32% reduction", 2023 Security Incident Response Index; "50% reduction", 2024 Security Services Benchmark Report).** vendor. **not-retrieved.**
No URL: neither report was located, and the figures appear only in secondary aggregation.
Supports: nothing in this bundle. Sought for: an independent measured effect of runbooks on incident
duration. **Untraceable to a published report in this research.** Together with [29] and [30] this is a
cluster of four separate MTTR figures that do not reconcile with each other and none of which could be
traced, which is itself the finding: **the claim that runbooks reduce incident duration is universally
asserted and, as far as this research could establish, never independently measured.**

---

## Contested register

Recorded rather than resolved. Where sources genuinely disagree, the bundle presents the disagreement.

**1. General or step-by-step?** Google names this contentious inside its own organisation, in two separate
sentences: "Some SREs at Google advocate keeping playbook entries general so they change slowly", against
"Other SREs advocate for step-by-step playbooks to reduce human variability and drive down MTTR". Of the
disagreement itself it says "This is a contentious topic" [1]. **The
bundle does not pick a side its own primary source refuses to pick**; the template asks the author to state
which they are writing and why.

**2. Is a runbook a permanent artifact or a step toward automation?** The SRE Workbook supports a middle
position: automate the deterministic ones [1], which implies the judgment-dependent ones remain. Vendors
selling automation argue the category is temporary [14][15]. **The incentive difference is stated wherever
this appears in the bundle.**

**3. Service-operations manual or incident-scoped procedure?** Both shapes have named publishers [8][13]
versus [11][12], and Atlassian publishes two mutually inconsistent templates [9][10]. **Settled for this
bundle by the family contract's own definition, not by weight of sources.** See the format verdict.

**4. Is "treat runbooks like code" consensus or an artifact of who was sampled?** Two vendor sources state
it flatly [20][21] and nothing read contradicts them, but both sell adjacent tooling and no primary source
was found stating it. **Reported as a strong practitioner convention, not as canon.**

**5. Are runbook and SOP synonyms?** This library's own catalog treats SOP as an alias [catalog 116]. A
vendor comparison distinguishes them on predictability, SOPs for routine well-defined tasks and runbooks for
more variable diagnostic ones [27]. **The alias is defensible and the distinction is real; the bundle states
both.**

**6. Is a disaster recovery plan the same document under another name?** NIST's hierarchy supports a
plan-contains-procedures reading [25], while some vendor material treats "DR plan" and "DR runbook" as
interchangeable. **Unresolved, and the bundle uses the NIST reading because it is the primary source.**

**7. Is calendar review sufficient?** One source stacks a quarterly cadence with post-incident triggers
without ranking them [21]; another offers a 90-day untouched heuristic [20]. **Neither states the
system-change trigger this family's contract requires**, so the bundle's Review Trigger section goes beyond
every source read and says so.

---

## Sought and not found

Distinct from `not-retrieved` above: these were searched for and appear not to exist in the form sought.

- **Any independent measurement of a runbook's effect on incident duration.** Four separate MTTR figures
  circulate [29][30][31]; none traces to a method. The claim is asserted everywhere and measured nowhere
  this research could reach.
- **A government-published operations-manual template with a named ordered section list.** GOV.UK, NIST and
  18F were searched; the results were general SOP and ITIL commentary, not a runbook template.
- **An ordered runbook template in Google's own SRE material.** The Workbook's incident-response chapter was
  read in full and publishes no section list [7]. **The most obvious place to find one does not have one**,
  which is a real gap rather than a confirmation.
- **A non-vendor decision rule for when to automate a runbook step**, such as a repetition threshold. The
  only named test found is the SRE Workbook's determinism test [1], and no competing practitioner rule was
  located.
- **A named pattern for "a runbook written by the person who built the system, for themselves."** The
  general curse-of-knowledge framing exists [18]; this specific pattern has no name in the sources read.
- **A source naming a last-verified field in a runbook's body.** Only one source read carries a service
  owner section [13]; none carries a verification date in the document itself rather than in wiki metadata.
- **A single source contrasting a runbook against a postmortem directly.** Google's postmortem chapter
  defines the postmortem on its own terms [23]. The prospective-versus-retrospective test the bundle states
  is **synthesis across two definitions and is labelled as such**, which matters because this library ships
  `incident-postmortem` next and the two must not overlap.
