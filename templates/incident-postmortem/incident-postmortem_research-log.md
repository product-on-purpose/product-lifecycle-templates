# incident-postmortem research log

Researched 2026-08-07 across six parallel dimensions: the SRE canon, structure in published templates, the
attribution of the field's folklore, the root-cause argument, empirical evidence, and boundaries against
adjacent documents. **37 sources**, **all 37 fetched-and-verified**, carrying **139 verbatim quotable
phrases**. By tier: 14 vendor, 11 primary, 9 practitioner, 3 standards. Retrieval status is recorded per
source in the three-token vocabulary the library gates
([ADR 0029](../../docs/internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md)), and only
`fetched-and-verified` sources are quoted.

**How to read this log.** A `Supports:` clause says what the bundle is allowed to rest on that source for.
A `Quotable:` phrase was read verbatim on the page. If a claim in the companion is not covered by some
entry's `Supports:` clause here, the claim has no home and must be cut, not justified after the fact.

**The tier mix is the warning this type deserves.** Fourteen of the 37 sources are vendor tier, and most of
those vendors sell incident-management software. Where a vendor claim is used below, the entry says who
benefits from it. The four entries carrying no `Quotable:` list are not thin research: each records a
verified absence, and each says so in its own `Supports:` clause.

---

## Honest framing: the six things this bundle has to say

**1. The canon publishes trigger criteria, and the chapter everyone cites never uses the word "timeline".**
Google's SRE book chapter 15 publishes an explicit list of what should trigger a postmortem [1], and holds
that teams should agree those criteria before an incident rather than argue them during one. But a full-text
search of that chapter returns **zero occurrences of "timeline"** [1]. The word exists only as a heading in
the separately linked Appendix D [3]. This is the same shape as the two zeros this library found in the
`definition-of-done` and `runbook` research: a section label universally assumed to be canon prose turns out
to be a heading in a document most readers of the chapter never open.

> **This count was re-verified independently on 2026-08-07**, by fetching both pages and counting over the
> stripped visible text rather than trusting the research pass. Chapter 15 carries 15,770 characters of
> visible text, says "postmortem" 89 times, and says "timeline" **0** times; Appendix D says it 3 times.
> The same re-count found **"contributing factor" is also 0 in chapter 15** and 1 in Appendix D. It also
> found the research pass's other term counts slightly off in both directions ("blameless" 10 rather than 6,
> "action item" 2 rather than 4), which is why only the zeros, which are robust to how you extract the text,
> are used as teaching points here. A count that changes with your parser is not a finding; a zero is.

**2. There is no single canonical section set, because the canon disagrees with itself.** Appendix D's
worked example runs Summary, Impact, Root Causes, Trigger, Resolution, Detection, Action Items, Lessons
Learned, Timeline, Supporting information [3]. The Workbook's two worked examples use a different set again,
including Executive Summary, Problem Summary, Background and Glossary [2]. Any claim that "the canon" has
one settled template is not supportable, and this bundle does not make it.

**3. Five of the six sections this bundle was specified to ship title nothing in any published template.**
Five genuinely published documents were read in full: PagerDuty [4], Atlassian [5], GitLab [6], incident.io
[7], and a real Elastic incident report [9]. Only **Timeline** is attested, in 4 of 5. The sharpest result
is that the concept everyone calls "action items" is written **three different ways and never converges**:
"Action Items" (PagerDuty [4], Elastic [9]), "Corrective actions" (Atlassian [5], GitLab [6]), and
"Follow-up actions" (incident.io [7]). The bundle picks the canon's own word [3] and says that it is a pick.

**4. Every circulating statistic about postmortems is untraceable, and two are demonstrably fabricated.**
No controlled, quasi-experimental or correlational study linking postmortems to recurrence or MTTR was found
on arXiv [21][22], in DORA's 2021, 2023 and 2024 reports [27][28][29], or in general search. Google's own
two chapters are **number-free** [1][2]. The MTTR percentages in circulation (24, 30, 35, 37, 40, 50
percent) trace to vendor headlines with no methodology in the body [23][24], or to a single customer
testimonial [25]. Two go further: a "24 percent reduction in repeat incidents" attributed to a vendor guide
[26], and a "35 percent mean incident reduction (SD=18.0 percent), statistically significant" attributed to
a named paper [30], are **absent from the documents themselves**, both of which were fetched and read in
full. The second carried a standard deviation and a significance claim, and came from a search-engine
summary. It is this library's dominant defect class caught in the wild, and it is worth more to this bundle
than any statistic would have been.

**5. "Root cause" is argued against by a named, cross-citing community and defended by almost nobody by
name.** Richard Cook's "How Complex Systems Fail" states it flatly: "Post-accident attribution to a 'root
cause' is fundamentally wrong" [17]. The critique is carried by Cook, Allspaw, Hollnagel, Woods, Dekker and
Leveson, who cite one another and are treated as canon in resilience engineering [17][12][18][19]. The
clearest **named** defence found is one CTO's blog post [20], which concedes that "sometimes you won't find
a root cause. It happens." **The asymmetry is itself the finding** and the bundle states it: this is not two
evenly matched schools, it is an organised critique of an entrenched default that is rarely defended by
name. The bundle still ships a Root Causes section, plural, because 4 of 5 published templates carry one
and the canon's own example does [3], and it teaches the argument rather than resolving it.

**6. Published practice puts action items in the ticket tracker, and names no risk register.** Two
independent sources say the same thing in nearly the same words: actions belong in the tracker the team
already uses, and explicitly not in the postmortem document [35][36]. ITOC360: "The postmortem document is
where action items are born. It is not where they should live" [35]. **Neither names a risk register or a
RAID log.** The `process-docs` family contract offers those as destinations alongside the product backlog;
the backlog option is what practice describes, and the bundle says plainly that the risk-register route is
this library's own convention rather than received postmortem practice.

## Two claims this bundle was told to make, and could not source as canon

Recorded here rather than quietly dropped, because both come from documents this repository has adopted.

- **"Postmortem (learning) versus incident report (live record)" is called the sharpest distinction by this
  bundle's build spec.** The only source found that draws it that cleanly is a vendor blog [31]. It is a real
  source and it is quoted, but it is not a standard, and the bundle does not present the distinction as
  canonical. Parabol [37] draws the postmortem-versus-retrospective line separately and in more detail.
- **The five whys has a contested origin that practitioner folklore treats as settled.** Wikipedia
  attributes original creation to Sakichi Toyoda [13] while practitioner writing overwhelmingly credits
  Taiichi Ohno [14]. Ohno's 1988 book could not be read directly. Most usefully, **Allspaw's "The Infinite
  Hows", the essay most responsible for making "five whys is dangerous" into folklore, does not itself trace
  the technique to Ohno or Toyota anywhere in its own text** [12].

## One source read through a mirror, flagged rather than laundered

The founding text for "blameless postmortem" is John Allspaw's May 2012 Etsy post [11]. Its canonical URL
returns HTTP 403 to automated retrieval, so the body was read through a full-text mirror. The entry says so.
Allspaw does not claim to have coined the phrase, and no earlier dated use was found, so the bundle says
"the earliest attributable use" rather than "coined by".

## Format verdict (ADR 0028)

**One format.** No second shape is in circulation with a named source publishing it *as a postmortem*: the
corpus varies in section names, not in structure. Elastic's report [9] is freeform rather than templated,
which is a real observation about practice but is the absence of a format, not a second one.

## Sources

### The SRE canon, and what it does and does not publish

**[1] Google SRE, "Postmortem Culture: Learning from Failure" (Site Reliability Engineering, ch.15).** primary. **fetched-and-verified.**
`https://sre.google/sre-book/postmortem-culture/`
Supports: Section 2/3/4 answers: no on-page template, term counts, no P0/P1 sentence, trigger criteria list. The canonical Google source on postmortem culture states its purpose and a qualitative outcome claim, but supplies no percentage, MTTR figure, or recurrence statistic anywhere in the chapter.
Quotable: "Common postmortem triggers include: User-visible downtime or degradation beyond a certain threshold; Data loss of any kind; On-call engineer intervention (release rollback, rerouting of traffic, etc.); A resolution time above some threshold; A monitoring failure (which usually implies manual incident discovery)"
Quotable: "thanks to our continuous investment in cultivating a postmortem culture, Google weathers fewer outages and fosters a better user experience"
Quotable: "ensure that the incident is documented, that all contributing root cause(s) are well understood, and, especially, that effective preventive actions are put in place to reduce the likelihood and/or impact of recurrence"

**[2] Google SRE, "Postmortem Culture: Beyond Blameless" (The Site Reliability Workbook, ch.10).** primary. **fetched-and-verified.**
`https://sre.google/workbook/postmortem-culture/`
Supports: Location of the P0/P1 action-item statement, term counts, worked-example headings, and the chapter's deferral to SRE-book ch.15 on trigger criteria. Google's own follow-up chapter, the most likely place a real Google MTTR/recurrence statistic would live, contains only a narrative case example, no number.
Quotable: "To our users, a postmortem without subsequent action is indistinguishable from no postmortem. Therefore, all postmortems which follow a user-affecting outage must have at least one P[01] bug associated with them."
Quotable: "For a comprehensive discussion on blameless postmortem philosophy, see Chapter 15 in our first book, Site Reliability Engineering."
Quotable: "The action items implemented from the original postmortem dramatically reduced the blast radius and rate of the second incident."
Quotable: "Ongoing investment in cultivating a postmortem culture pays dividends in the form of fewer outages, a better overall experience for users, and more trust"

**[3] Google SRE, "Example Postmortem" (Site Reliability Engineering, Appendix D).** primary. **fetched-and-verified.**
`https://sre.google/sre-book/example-postmortem/`
Supports: The canon's one actual worked template/example document: its exact section headings, its Action Items format (no P0/P1 labels), and its Lessons Learned subsections.
Quotable: "Plug file descriptor leak in search ranking subsystem | prevent | agoogler | Bug 5554825 DONE"

### Structure in published templates

**[4] PagerDuty, Inc. - "Postmortem Template" (PDF).** vendor. **fetched-and-verified.**
`https://postmortems.pagerduty.com/assets/pdf/PostmortemTemplate.pdf`
Supports: Full verbatim section list of PagerDuty's own published postmortem template (linked from postmortems.pagerduty.com/resources/post_mortem_template/, whose HTML page only carries a download link, so the PDF is the actual template body).
Quotable: "Overview:"
Quotable: "What Happened:"
Quotable: "Root Causes:"
Quotable: "Resolution:"
Quotable: "Impact"
Quotable: "Timeline"
Quotable: "Responders"
Quotable: "Who was the Incident Commander?"
Quotable: "How'd we do?"
Quotable: "What went well?"
Quotable: "What didn't go so well?"
Quotable: "Action Items"
Quotable: "Messaging"
Quotable: "Internal Email"
Quotable: "External Message"

**[5] Atlassian - "A Guide to the Incident Postmortem Process" (postmortem/templates page).** vendor. **fetched-and-verified.**
`https://www.atlassian.com/incident-management/postmortem/templates`
Supports: Full verbatim, in-order h2/h3 heading list of Atlassian's postmortem template, extracted from the page's server-rendered HTML (WebFetch's markdown conversion dropped body content, so headings were pulled directly from <h2 id=...> tags in the raw HTML).
Quotable: "Incident summary"
Quotable: "Leadup"
Quotable: "Fault"
Quotable: "Impact"
Quotable: "Detection"
Quotable: "Response"
Quotable: "Recovery"
Quotable: "Timeline"
Quotable: "Root cause identification: The Five Whys"
Quotable: "Root cause"
Quotable: "Backlog check"
Quotable: "Recurrence"
Quotable: "Lessons learned"
Quotable: "Corrective actions"

**[6] GitLab.org - GitLab project's public RCA issue template (.gitlab/issue_templates/rca.md).** vendor. **fetched-and-verified.**
`https://gitlab.com/gitlab-org/gitlab/-/raw/master/.gitlab/issue_templates/rca.md`
Supports: GitLab's own actual root-cause-analysis/postmortem issue template as used in the GitLab project itself (the handbook's Incident Review page, by contrast, no longer publishes a template body and instead defers to a proprietary incident.io settings page).
Quotable: "## Summary"
Quotable: "## Impact & Metrics"
Quotable: "## Detection & Response"
Quotable: "## MR Checklist"
Quotable: "## Timeline"
Quotable: "## Root Cause Analysis"
Quotable: "### Example of the usage of "5 whys""
Quotable: "## What went well"
Quotable: "## What can be improved"
Quotable: "## Corrective actions"
Quotable: "## Guidelines"
Quotable: "A root cause can **never be a person**"

**[7] incident.io - "Our incident post-mortem template" (hub page).** vendor. **fetched-and-verified.**
`https://incident.io/hubs/post-mortem/incident-post-mortem-template`
Supports: Full verbatim, in-order heading list of incident.io's published postmortem template, extracted directly from h1-h4 tags in the fetched HTML.
Quotable: "Key information"
Quotable: "Team"
Quotable: "Useful Links"
Quotable: "Key Timestamps"
Quotable: "Incident summary"
Quotable: "Incident timeline"
Quotable: "Contributors"
Quotable: "Mitigators"
Quotable: "Learnings and risks"
Quotable: "Follow-up actions"
Quotable: "Post-mortem meeting notes"

**[8] incident.io - "Post-mortem templates" (product docs, docs.incident.io).** vendor. **fetched-and-verified.**
`https://docs.incident.io/post-incident/postmortem-templates`
Supports: Confirms incident.io's product supports multiple, configurable templates and 'Dynamic template selection' (picking a template per incident type/severity), plus names five 'preset sections' distinct from the hub page's single published example.
Quotable: "Preset sections"
Quotable: "Summary: a high-level overview of the incident."
Quotable: "Timeline: embeds the incident timeline directly in the post-mortem. This section can't be removed."
Quotable: "Follow-ups: shows the follow-up items associated with the incident."
Quotable: "Key information: a block of incident metadata (severity, duration, roles, etc.)."
Quotable: "Dynamic template selection"

**[9] Elastic - "Elastic Cloud Incident Report: February 4, 2019" (elastic.co blog).** practitioner. **fetched-and-verified.**
`https://www.elastic.co/blog/elastic-cloud-incident-report-feburary-4-2019`
Supports: A real, named-org published post-incident report (not a blank template) whose heading structure was read verbatim; used as the fifth/sixth independent data point for the matrix and to show that a genuinely published postmortem need not use a fixed reusable template at all.
Quotable: "Background"
Quotable: "What Happened"
Quotable: "Root Cause"
Quotable: "Resolution"
Quotable: "Impact"
Quotable: "Coordination layer"
Quotable: "Proxy layer"
Quotable: "Kibana"
Quotable: "Action Items"
Quotable: "Engineering and Architecture"
Quotable: "Process and Communications"

**[10] GitLab - "Incident Review" handbook page.** vendor. **fetched-and-verified.**
`https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/incident-review/`
Supports: Confirms the handbook's own 'Template' subsection no longer states section headings and instead directs incident leads to a proprietary incident.io settings page (app.incident.io/gitlab/settings/post-mortem), which is why rca.md (a different, still-public file in the same repo) was used as GitLab's actual template evidence instead.
Quotable: "The incident lead will open an incident review issue in the Production Tracker using the incident_review template"
Quotable: "Incident review template can be edited here:"

### The folklore, traced to its authors

**[11] John Allspaw - "Blameless PostMortems and a Just Culture" (Code as Craft / Etsy Engineering, May 22, 2012).** primary. **fetched-and-verified.**
`https://www.etsy.com/codeascraft/blameless-postmortems/ (canonical, returns HTTP 403 to automated fetch; read via full-text mirror at https://jaytaylor.com/notes/node/1498058768000.html)`
Supports: Coinage/date of 'blameless postmortem' as a named practice; whether Allspaw credits anyone for 'just culture'
Quotable: "Having a 'blameless' Post-Mortem process means that engineers whose actions have contributed to an accident can give a detailed account of: what actions they took at what time, what effects they observed, expectations they had, assumptions they had made, and their understanding of timeline of events as they occurred...and that they can give this detailed account without fear of punishment or retribution."
Quotable: "Having a Just Culture means that you're making effort to balance safety and accountability."
Quotable: "That's why we have blameless Post-Mortems at Etsy, and why we're looking to create a Just Culture here."

**[12] John Allspaw - "The Infinite Hows (or, the Dangers Of The Five Whys)" (Kitchen Soap, November 14, 2014).** primary. **fetched-and-verified.**
`https://www.kitchensoap.com/2014/11/14/the-infinite-hows-or-the-dangers-of-the-five-whys/`
Supports: Whether Allspaw's own critique of Five Whys traces the technique to Ohno/Toyota in his own text (it does not) The direct, named criticism of the Five Whys technique specifically, the proposed why-to-how vocabulary swap, and the Learning-From-Incidents-adjacent lineage (Dekker, Hollnagel, Woods, Leveson, Klein, Conklin).
Quotable: "In the worst case, it can re-affirm a faulty worldview of causal simplification and set up a structure where individuals don't feel safe."
Quotable: "What-You-Look-For-Is-What-You-Find"

**[13] Wikipedia - "Five whys" article (accessed 2026-08-06).** standards. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Five_whys`
Supports: Whether five whys traces to Ohno/Toyota in a readable text, and the contested attribution to Sakichi Toyoda vs. Ohno
Quotable: "the basis of Toyota's scientific approach by repeating why five times the nature of the problem as well as its solution becomes clear."
Quotable: "Ask 'why' five times about every matter."

**[14] Lean Enterprise Institute (John Shook) - "Clarifying the '5 Whys' Problem-Solving Method" (lean.org, The Lean Post).** practitioner. **fetched-and-verified.**
`https://www.lean.org/the-lean-post/articles/five-whys-animation/`
Supports: Corroborates the Ohno machine-breakdown example and confirms the article does not itself quote Ohno's book verbatim, only paraphrases it
Quotable: "To look at this part of the problem-solving process, the five whys or a causal chain, let's look at the famous example from Taiichi Ohno of Toyota and the one he used starting in the 1950s of a machine breaking down."
Quotable: "In this example, he looked at a machine that had stopped working and identified with the first why that it had blown a fuse in the control box because it was overloaded."

**[15] missinfogeek.net - "'Just Culture': an introduction" (practitioner blog post, undated).** practitioner. **fetched-and-verified.**
`https://missinfogeek.net/just-culture-an-introduction/`
Supports: Attribution of 'just culture' to James Reason's aviation-safety work in the late 1990s/early 2000s
Quotable: "the term 'Just Culture' arose from the work on aviation safety by Professor James Reason in the late 90s and early 00s."

**[16] Sidney Dekker - author page for "Just Culture" book (sidneydekker.com).** primary. **fetched-and-verified.**
`https://sidneydekker.com/just-culture`
Supports: Confirms Dekker's own site describes his 'Just Culture' book (now in a third edition) but does NOT itself state a coinage date or credit an origin for the term on this page

### The root-cause argument, and who is on each side

**[17] Richard I. Cook, MD - "How Complex Systems Fail" (18-point document, Cognitive Technologies Laboratory, University of Chicago, originally 1998).** primary. **fetched-and-verified.**
`https://how.complexsystems.fail/`
Supports: The founding statement of the anti-root-cause position in the resilience-engineering canon, plus the hindsight-bias mechanism that explains why single causes feel findable after the fact.
Quotable: "Post-accident attribution to a 'root cause' is fundamentally wrong."
Quotable: "Because overt failure requires multiple faults, there is no isolated 'cause' of an accident."
Quotable: "Hindsight bias remains the primary obstacle to accident investigation, especially when expert human performance is involved."
Quotable: "Knowledge of the outcome makes it seem that events leading to the outcome should have appeared more salient to practitioners at the time than was actually the case."
Quotable: "All practitioner actions are gambles, that is, acts that take place in the face of uncertain outcomes."
Quotable: "After an accident, practitioner actions may be regarded as 'errors' or 'violations' but these evaluations are heavily biased by hindsight and ignore the other driving forces, especially production pressure."

**[18] Lorin Hochstein (Netflix resilience engineer) - "Root cause of failure, root cause of success", Surfing Complexity blog (2021-08-13).** practitioner. **fetched-and-verified.**
`https://surfingcomplexity.blog/2021/08/13/root-cause-of-failure-root-cause-of-success/`
Supports: The 'root cause of success' symmetry argument (attributed in-text to Allspaw's 2018 tweets) used to show why singling out one failure cause is incoherent, and the 'boulder held up by active processes, not passive supports' framing.
Quotable: "It doesn't make sense to ask what the 'root cause of success' is for an effort like this, because it's a collaboration that requires the work of many different people to succeed."
Quotable: "What's keeping the complex system boulder balanced is not a collection of passive supports. Instead, there are a number of active processes...constantly watching the boulder to see if it starts to slip, and applying force to keep it balanced."
Quotable: "When the boulder falls, it means that the collection of processes weren't able to compensate for the disturbance. But there's no single problem, no root cause, that you can point to."

**[19] Kitchen Soap (John Allspaw) - "There is no Root Cause" / "Each necessary, but only jointly sufficient", republished on SafetyRisk.net.** practitioner. **fetched-and-verified.**
`https://safetyrisk.net/there-is-no-root-cause/`
Supports: The explicit naming of the camp's shared vocabulary (Hollnagel, Woods, Dekker, Cook together) and Cook's 'necessary but only jointly sufficient' formulation as the alternative to a singular root cause.
Quotable: "For complex socio-technical systems... there is a single unifying event that triggers a chain of events... [is] actually a fallacy, because for complex systems: there is no root cause."
Quotable: "Failures in complex systems require multiple contributing causes, each necessary but only jointly sufficient."
Quotable: "Accidents emerge from a confluence of conditions and occurrences... each necessary but only jointly sufficient."

**[20] Leon Chism (CTO, DialogTech) - "In Defense of The Root Cause Analysis Process", Medium.** practitioner. **fetched-and-verified.**
`https://medium.com/@leonc/in-defense-of-the-root-cause-analysis-process-a849c4a9d570`
Supports: The strongest defense of root-cause analysis found for this dimension: a named practitioner, writing in direct response to the anti-RCA critique, arguing the label and the disciplined process still serve a generative learning culture when done without single-cause or single-person blame.
Quotable: "I think the criticism is ill considered and I don't really recognize the RCA process they describe, and then take down."
Quotable: "Punishment is the surest way to shut off the honesty and transparency any high functioning team requires."
Quotable: "sometimes you won't find a root cause. It happens."

### Empirical evidence, and the statistics that do not trace

**[21] arXiv preprint - "Failures and Fixes: A Study of Software System Incident Response" (2008.11192).** standards. **fetched-and-verified.**
`https://arxiv.org/abs/2008.11192`
Supports: Establishes that the closest arXiv paper to this topic is a qualitative study of 30 incidents (15 interviews, 15 published postmortems) analyzing how failures occur, are detected, investigated and mitigated. It does not measure recurrence rates or MTTR before/after postmortem adoption.
Quotable: "failures can cascade through a system leading to major outages; and that often engineers do not understand the scaling limits of systems they are supporting until those limits are exceeded"

**[22] arXiv preprint - case study of postmortem practices at a national space research center (2509.06301).** standards. **fetched-and-verified.**
`https://arxiv.org/pdf/2509.06301`
Supports: A qualitative interview-based case study of how postmortems are conducted and the organizational barriers to learning from them. No recurrence or MTTR quantification is attempted.
Quotable: "we conducted semi-structured interviews with software engineers and technical managers"
Quotable: "we explore the technical, managerial difficulties organizations face when conducting postmortems"

**[23] Rootly (vendor blog) - "Rootly vs Blameless: Which Cuts MTTR Faster by Up to 40%".** vendor. **fetched-and-verified.**
`https://rootly.com/sre/rootly-vs-blameless-cuts-mttr-faster-up-40-today`
Supports: Traces and disqualifies the '40% MTTR reduction' figure that circulates in postmortem-tooling marketing: the number appears only in the page title/headline, with no methodology, study, survey, or customer data anywhere in the article body.

**[24] Rootly (vendor blog) - "AI-Generated Postmortems that Cut MTTR by 30% in Minutes".** vendor. **fetched-and-verified.**
`https://rootly.com/sre/aigenerated-postmortems-cut-mttr-30-minutes`
Supports: Traces and disqualifies the '30% MTTR reduction' figure: it appears only in the hero/headline text, with the only supporting detail being a single anecdotal comparison (a five-hour analysis becoming a ten-minute review at Razorpay), not a study or aggregate measurement.
Quotable: "what if you could turn a five-hour analysis into a ten-minute review"

**[25] incident.io (vendor blog) - "Incident post-mortem software ROI: quantifying MTTR reduction and engineer time savings".** vendor. **fetched-and-verified.**
`https://incident.io/blog/postmortem-software-roi-calculator`
Supports: Traces the '37% MTTR reduction' figure to a single named customer (Favor) reported in a separate incident.io blog post, i.e. a self-referential vendor customer anecdote, not an independent or methodologically described study. The '90 minutes to 10-15 minutes' postmortem-writing time saving is the article's own arithmetic, not sourced data.
Quotable: "customers report 37% faster resolution"
Quotable: "Ninety minutes later, they have an incomplete, probably inaccurate post-mortem."

**[26] Hyperping (vendor blog) - "Incident post-mortems: the complete, blameless guide".** vendor. **fetched-and-verified.**
`https://hyperping.com/blog/incident-post-mortem`
Supports: Full-body read found NO '24%+ reduction in repeat incidents from systems thinking' claim anywhere in the article, despite that exact claim being returned by a WebSearch tool summary as if quoted from this page -- the search tool's synthesis fabricated a citation that does not exist in the source. The page does contain a psychological-safety statistic attributed to DORA 2021 ('47% more likely to engage in process improvements and 64% more likely to report near-misses'), plus an aspirational unsourced target ('90-day recurrence < 5%').
Quotable: "Teams with high psychological safety are 47% more likely to engage in process improvements and 64% more likely to report near-misses"

**[27] DORA - Accelerate State of DevOps Report 2021.** primary. **fetched-and-verified.**
`https://dora.dev/research/2021/dora-report/`
Supports: Checked as the primary source for the '47%/64% psychological safety' figure Hyperping attributes to DORA 2021. The fetched page content contains no such percentages and no mention of postmortems, blameless retrospectives, or near-miss reporting at all -- only a general statement linking generative culture to reduced burnout. The attribution could not be confirmed against the primary text as retrieved.
Quotable: "A generative team culture, where individuals feel included and a sense of belonging, is crucial for reducing burnout, particularly during remote work."

**[28] DORA - Accelerate State of DevOps Report 2023.** primary. **fetched-and-verified.**
`https://dora.dev/research/2023/dora-report/`
Supports: Checked for any postmortem/post-incident-review measurement; the fetched content contains none. Confirms DORA does not report postmortems as a measured practice in the 2023 edition (as retrieved).

**[29] DORA - Accelerate State of DevOps Report 2024.** primary. **fetched-and-verified.**
`https://dora.dev/research/2024/dora-report/`
Supports: Checked for any postmortem/post-incident-review measurement; the fetched content discusses AI adoption, user-centricity, platform engineering, and MTTR/change-failure-rate only in the abstract, with no postmortem-specific finding.

**[30] Lalith Sriram Datla, "Postmortem Culture in Practice: What Production Incidents Taught Us about Reliability in Insurance Tech," International Journal of Emerging Research in Engineering and Technology (Pearl Blue Research Group), vol. 3, issue 3, pp. 40-49, 2022.** practitioner. **fetched-and-verified.**
`https://ijeret.org/index.php/ijeret/article/download/135/124`
Supports: Read in full (10-page PDF). This is a single-author practitioner narrative published in a non-peer-reviewed, article-processing-charge journal (no methods section, no dataset, one anecdotal case study of a single outage). It contains NO statistic resembling '35% mean incident reduction (SD=18%), statistically significant paired pre/post comparison' -- that figure was produced by a WebSearch tool summary that claimed to be quoting this source and was not. The actual article's closest empirical-sounding claim is qualitative.
Quotable: "Post-mortem analyses have improved the dependability of the infrastructure supporting insurance technologies. CI/CD techniques, dependability awareness, and resilience testing all show notably superior results from retroactive insights."
Quotable: "Mean time to recovery (MTTR) became the most crucial statistic because it led to real-time alarm correlation and increased infrastructure spending on self-healing."

### Boundaries, and where the action items go

**[31] COEhub - "Why Both Incident Reports and Postmortems Matter".** vendor. **fetched-and-verified.**
`https://www.coehub.ai/blog/incident-reports-vs-postmortems`
Supports: Q1: the postmortem (learning) vs incident report (live record) distinction, drawn explicitly and by name
Quotable: "The incident report is the factual snapshot of what happened. It is created during or shortly after the incident while evidence is still fresh in the minds of responders."
Quotable: "If the incident report answers the question what happened, the postmortem answers why it happened and what will prevent this from happening again."
Quotable: "Think of it as the black box recorder. It captures events but does not explain them."
Quotable: "A strong postmortem is analytical and introspective. It is written after investigators have had time to explore logs, code changes, architecture diagrams, team workflows, and human decision paths."
Quotable: "One captures reality. The other interprets it. One provides accountability. The other provides improvement."

**[32] US Army Combined Arms Center - Training (CAC-T), Training Management Directorate - "The Leader's Guide to After-Action Reviews (AAR)", December 2013.** primary. **fetched-and-verified.**
`https://pinnacle-leaders.com/wp-content/uploads/2018/02/Leaders_Guide_to_AAR.pdf`
Supports: Q2: what the Army primary material actually prescribes for After Action Review, since 'after-action review' is a catalog alias for this bundle type
Quotable: "An AAR is a professional discussion of a training event that enables Soldiers/units to discover for themselves what happened and develop a strategy for improving performance. Facilitators provide an overview of the event plan (what was supposed to happen) and facilitate a discussion of what actually happened during execution."
Quotable: "a guided analysis of an organization's performance, conducted at appropriate times during and at the conclusion of a training event or operation with the objective of improving future performance. It includes a facilitator, event participants, and other observers"
Quotable: "Leaders avoid creating the environment of a critique during AARs. Because Soldiers and leaders participating in an AAR actively self-discover what happened and why, they learn and remember more than they would from a critique alone. A critique only gives one viewpoint and frequently provides little opportunity for discussion of events by participants. The climate of the critique, focusing only on what is wrong, prevents candid and open discussion of training events and stifles learning and team building."
Quotable: "AARs are a professional discussion of a training event that enables Soldiers/units to discover for themselves what happened and develop a strategy for improving performance. They provide candid insights into strengths and weaknesses from various perspectives and feedback, and focus directly on the commander's intent, training objectives and standards."
Quotable: "approximately 30-45 minutes for platoon-level AARs, 1 hour for company-level AARs, and about 2 hours for battalion-level and above, but training to standard takes priority over training to time"

**[33] IT Process Wiki (IT Process Maps GbR) - "Problem Management" (ITIL reference).** practitioner. **fetched-and-verified.**
`https://wiki.en.it-processmaps.com/index.php/Problem_Management`
Supports: Q3: whether ITIL's 'problem record' is the same artifact as a postmortem
Quotable: "The Problem Record contains all details of a Problem, documenting the history of the Problem from detection to closure"
Quotable: "To review the resolution of a Problem in order to prevent recurrence and learn any lessons for the future"

**[34] itil.org.uk (Purple Griffon) - "Incident Management vs Problem Management" blog.** vendor. **fetched-and-verified.**
`https://www.itil.org.uk/blog/incident-management-vs-problem-management`
Supports: Q3: an ITSM-tradition source that itself uses the word 'Postmortem Review' as a step inside Problem Management, rather than treating problem record and postmortem as synonyms
Quotable: "Postmortem Review: Teams conduct an open, blame-free review to discuss incidents, root causes, and responses."
Quotable: "When problems are identified, they are recorded and tracked over time."

**[35] ITOC360 - "Postmortem Action Items: How to Track Them to Closure".** practitioner. **fetched-and-verified.**
`https://www.itoc360.com/postmortem-action-items/`
Supports: Q4: named practitioner source stating action items belong in the team's existing backlog/ticket tracker, not the postmortem document itself
Quotable: "The moment the meeting ends, every item needs a ticket in the same backlog your team already uses for planned work -- Jira, Linear, or whatever tool your sprint planning runs through."
Quotable: "The postmortem document is where action items are born. It is not where they should live."
Quotable: "A postmortem that produces five well-written tickets in the team's actual backlog has done its job. A postmortem that produces a bulleted list at the bottom of a report has produced a wish list."

**[36] incident.io - "Why Do Post-Mortem Action Items Fail? How to Make Incident Follow-Ups Actually Get Done".** vendor. **fetched-and-verified.**
`https://incident.io/blog/why-do-post-mortem-action-items-fail-how-to-make-incident-follow-ups-actually-get-done`
Supports: Q4: a second, independent named source corroborating that action items must live in the team's actual task-management system, explicitly ruling out spreadsheets, standalone boards, and the postmortem document itself
Quotable: "Post-mortem actions must live in your team's existing task management system -- not in the post-mortem document, not in a separate spreadsheet."
Quotable: "Linear, Jira, Asana, or whatever tool your team actually opens every day."
Quotable: "They should not live in: (1) The post-mortem document itself (2) A separate spreadsheet (3) A standalone tracking board that nobody visits (4) Meeting notes from the debrief"

**[37] Parabol - "Post-mortems vs Retrospectives: What's the Difference".** vendor. **fetched-and-verified.**
`https://www.parabol.co/blog/retrospectives-vs-post-mortems/`
Supports: Q5: a named source explicitly distinguishing postmortem from sprint retrospective on timing, trigger, participants, and output
Quotable: "typically take place after something is completed"
Quotable: "often coming at the end of each sprint, or approximately every 2 weeks"
Quotable: "after a big milestone, project or feature"
Quotable: "Only direct team members are typically involved in sprint retrospectives"
Quotable: "a report for leaders, who may or may not be part of the team implementing the work"

## Contested register

Genuine disagreements between sources, recorded with the camps named rather than resolved by picking one.

1. **Who originated the five whys.** Wikipedia credits Sakichi Toyoda with original creation and Taiichi
   Ohno with championing and formalising it inside Toyota [13]; practitioner writing overwhelmingly credits
   Ohno alone [14]. Ohno's 1988 book was not readable, so this is recorded unresolved.
2. **Where "just culture" comes from.** A practitioner introduction credits James Reason's aviation-safety
   work of the late 1990s [15]; Sidney Dekker's own author page states no coinage date or credit chain [16].
   Allspaw uses the term as already established, crediting nobody in the body read [11].
3. **Whether Allspaw coined "blameless postmortem".** No source claims he invented the phrase and no earlier
   dated use was found [11], but absence of an earlier use in this search is not proof none exists.
4. **Whether root-cause language should be abolished or used carefully.** The strong position is that there
   is no root cause at all [17][19]; a softer position within the same camp distinguishes live anomaly
   response from retrospective analysis [18]. The critics do not fully agree with each other.
5. **Whether the critique attacks a straw man.** Chism explicitly does not recognise the RCA process being
   attacked [20], which implies the argument may be against a careless version of RCA rather than a
   disciplined one. Recorded because it is the strongest form of the counter-argument found.
6. **Which canon heading set is canonical.** The SRE book appendix [3] and the Workbook [2] use materially
   different section sets for their worked examples. Treating either as "the" template is a choice.
7. **Which GitLab template is live.** The public `rca.md` in the GitLab repository was read [6], but the
   handbook now directs incident leads to a proprietary incident.io settings page instead [10], so `rca.md`
   may be legacy rather than what GitLab fills in today.
8. **Whether Elastic's report counts as a template at all** [9]. It is a genuinely published post-incident
   document from a named organisation, but it reads as one-off and hand-structured rather than reusable.
9. **Whether a risk register is ever a postmortem action destination.** No source found names one
   [35][36]. The family contract offers it. Flagged as a convention gap, not as an error in either.
10. **A DORA-attributed statistic that could not be located.** A vendor guide attributes "47 percent more
    likely to engage in process improvements and 64 percent more likely to report near-misses" to DORA 2021
    [26]. Neither percentage appears in the DORA 2021 report as retrieved [27]. This is flagged as
    unverified rather than fabricated, because the fetch may have been incomplete, which is a weaker
    accusation than the two statistics in framing point 4 that were checked against fully read documents.

## Sought and not found

Each of these was searched for deliberately. An absence established by a described search is a finding; an
absence assumed is not, and this library has recorded being wrong about that before.

- **Any controlled, quasi-experimental or correlational study measuring postmortems against incident
  recurrence or MTTR.** Searched arXiv by multiple phrasings, general web search standing in for Semantic
  Scholar and Google Scholar, and the DORA reports for 2021, 2023 and 2024 directly [21][22][27][28][29].
  DORA measures MTTR as a core metric but does not decompose it by whether or how teams write postmortems.
- **Any Google-attributed postmortem percentage.** Both SRE chapters were read in full and contain no
  number [1][2]. The nearest claims are one narrative case and the qualitative "Google weathers fewer
  outages" [1].
- **Taiichi Ohno's 1988 primary text**, beyond the single sentence Wikipedia reproduces [13]. No fetchable
  mirror was found.
- **James Reason's 1997 book**, which lives on archive.org, which the retrieval tooling cannot fetch. The
  widely circulated "what is needed is a just culture" sentence is therefore **not** quoted anywhere in this
  bundle.
- **Etsy's July 2014 "Just Culture resources" post**, which would be the most direct evidence of whether
  Allspaw's circle credits Dekker. HTTP 403.
- **A standards-tier source drawing the postmortem-versus-incident-report line.** Only a vendor blog was
  found [31]. ITIL's problem record is a different artifact by its own reference's account [33].

## Notes for the companion

**The honest core.** A postmortem is a learning document whose trigger is a decision the team publishes in
advance, not a punishment that follows an outage. The canon supplies the trigger criteria [1] and supplies
no evidence that the practice works [1][2], and the field's most repeated numbers are untraceable or absent
from their claimed sources [23][24][25][26][30]. What survives is an argued case, not a measured one, and
the bundle says so.

**The sections, and every one of them is attested.** The build spec proposed six titles of which five title
nothing in any published template. They are replaced by the section **set** the canon's own worked example
uses [3], reordered for reading rather than kept in Appendix D's order, and cross-checked against the vendor
matrix so that each title appears in a primary source and at least one template.

- **Lean:** Summary; Impact; Timeline; Root Causes; Action Items.
- **Full adds four, in place:** Summary; Impact; **Detection**; Timeline; **Trigger**; Root Causes;
  **Resolution**; **Lessons Learned**; Action Items.

Lean is a strict ordered subset of full, as the nesting rule requires. Attestation, per title: Summary
[3][5][6][7]; Impact [3][4][5][6][9]; Detection [3][5][6]; Timeline [3][4][5][6][7]; Trigger [3][5]; Root
Causes, plural, [3][4]; Resolution [3][4][9]; Lessons Learned [3][5]; Action Items [3][4][9].

**The two-size packaging is this bundle's own decision and must be labelled as such.** All five published
templates are single-size [4][5][6][7][9]. What the corpus does support is that depth varies: incident.io
ships configurable templates and dynamic template selection by incident type or severity [8], and Elastic
published a freeform report with no fixed template at all [9]. This bundle packages that real variation as
two sizes. No vendor publishes a named lean/full pair, and the companion says so rather than implying one
does.

**The sharpest teaching points.** The trigger criteria are canon and most teams never write theirs down [1].
"Timeline" is a heading nobody's canon prose uses [1][3]. The three-way split on what to call an action item
[4][5][6][7][9] is a small fact that tells a reader why their vendor's template looks different from their
neighbour's. And the root-cause argument [17][20] is the one place this document type has a live
intellectual fight worth showing rather than settling.

**What the example must not do.** It must not invent a statistic, because this log establishes that every
one in circulation is untraceable. It must not claim customer impact, because the event it analyses had
none, and that is the point: the trigger was Acme's own published criterion, not Google's list [1].
