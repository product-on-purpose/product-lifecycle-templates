# production-readiness-review: research log

Research conducted 2026-09-28, building on an admission sweep run on 2026-09-27 while the spec was written. The
build's six-dimension fan-out covered the Google canon, the published checklists counted item by item, cadence and the
cloud frameworks, the neighbours that share the ground or the name, running the review, and the standing gap question.
**39 sources are recorded below, all fetched-and-verified.** Only `fetched-and-verified` sources are quoted anywhere in
this bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a retrieval tool
returns: pages as downloaded, PDFs through a text extractor, and GitHub and GitLab files from their raw Markdown. Of 260
quotations the build's agents returned from external sources, 233 passed as returned. Of the other 27, 22 are verbatim
on the rendered page and failed only because the raw download carries Markdown bold or link syntax, a space before
punctuation where a link closed, a PDF line-end hyphen or an HTML entity inside the sentence. One was a real misquote
and is corrected: [38] reads "Slide 6 describes the business impact of delaying implementation of the release.", and
the agent had written "This slide". Two "[sic]" fragments of a GitLab template were dropped as trivia, a four-row table
in [37] that an agent flattened into prose is quoted cell by cell, and a list in [21] whose separators came from a text
conversion is quoted as its lead sentence and items. One of the 22 was dropped although verbatim: a vendor survey
percentage in [36] whose method nobody read. Twenty-six quotations were added from the main loop's own checks, eighteen of them section headings and outcome-state names that the companion must be able to cite by source. **288 quotations remain: 267 pass as normalized substrings and 21 are verbatim apart from the rendering artifacts above.**

---

## What the checks caught, and what was not read

**The neighbours dimension miscounted Appendix E.** It reported nine section headings; the page has ten, and the one it
missed is "Machines and datacenters" ([28]). The spec's count of ten areas stands. The page itself describes what it
is: "This is Google's original Launch Coordination Checklist, circa 2005, slightly abridged for brevity:".

**The spec's claim that no source publishes an outcome vocabulary is revised.** [37] publishes four states and says
plainly whose they are: "These states are a recommended governance model, not a Google, AWS, or Kubernetes platform
behavior." [36] publishes a binary ("criteria are either passed or flagged for follow-up"). Neither is a standard, and
the companion must say so.

**The spec's three sourced failure modes are now eight.** Alves [34] adds a third to Alves's own two, Nolan [35] names three
antipatterns in the talk's own headings, and [36] names drift after a one-time review. See "How it fails" below.

**The spec's boundary with the launch checklist rested on Google's two chapters, and adopters blur its trigger.**
[1] and [29] separate the two by trigger, team and timing. But [9] requires its check "for all services before
receiving real production traffic", [6] gates each maturity level of a new service, [4] names a "pre-launch PRR", and
[38] runs a PRR on every release before implementation. So in practice a PRR and a launch checklist can meet at the same
launch. The companion states Google's separation as Google's, reports the adopters' practice beside it, and says what
still differs: the object each asks about. See contested item 10.

**[38] is a PRR by name and a go-live review for each release by function.** Its content (roll-back criteria, the
business cost of delay, a configuration check after implementation, a workforce-relations review) belongs to the
release moment, which this library's `launch-coordination-checklist` covers. It is a second name collision, milder than
the hardware one, and the gap question's candidates drawn from it are routed accordingly below.

**The runbook question went unanswered by the dimension that asked it**, because the sources that answer it belonged to
another dimension. The main loop read them: every published checklist checks for a runbook and none produces one ([5]
"instructions on how to triage, mitigate, and resolve the alert should also be added to the service's on-call runbook";
[6] "Link to the troubleshooting runbooks."; [12] "It has OnCall playbooks."; [27] "Scorecards automate the process of
checking whether services meet criteria such as ownership, on-call coverage, runbooks, monitoring, and security
requirements."; [39] "When did you last execute each runbook end-to-end?"). Those five quotations, Alves's two
failure-mode sentences the spec cites, and the Appendix E heading were added to their entries after a raw-text check.

**GitLab's two pages disagree about whether its process is live.** [7]: "This project is archived and preserved for
historical reference only. No new reviews should be opened here." [8], a current page: "Create an issue using Runway
template in the readiness project." This bundle follows [7] and describes [6] as a historical artifact.

**Not read, and nothing in this bundle may rest on them:**

- **AWS's appendix pages on building an ORR checklist, creating guidance from an incident, and example questions.** Two
  resolved to 59-byte stubs; two were not fetched. The incident-to-question method rests on [20] alone.
- **The Cortex docs' own category and item breakdown**, which failed a raw-text check in the admission sweep. Only
  [27]'s general description is used.
- **A ProjectManagement.com go/no-go checklist, an OpsLevel guide and an AWS blog post on scaling ORRs**, seen only in
  search results.
- **The practitioner source `launch-coordination-checklist`'s companion cites for its own boundary** (Studio Red), not
  re-verified here and not requoted.
- **[38]'s Section 3 risk-rating table**, read by the gap agent but not returned as a quotation. Its existence may be
  mentioned; its categories may not be.

---

## The admission record

**[ADR 0048](../../docs/internal/decisions/0048-one-named-source-clears-the-admission-test.md)'s bar is met by three
bodies that publish the document**: [5], Fowler's Appendix A ("This will be a checklist to run over all microservices -
manually or in an automated way."); [6], GitLab's issue template, three maturity gates and 69 items; and [9] to [12],
Mercari's Production Readiness Check, "which is required for all services before receiving real production traffic".
[1] describes a checklist Google maintains without publishing it; [3], [4], [17] to [24], [25] and [27] describe the
practice.

**[38] is not counted toward admission, and this is the rule for what the bundle takes from it.** [38] publishes a
document named PRR, but it reviews each release before implementation, which is the launch moment. **This bundle
takes from [38] only what any readiness review needs**: evidence for each item, a reason for every not-applicable
answer, a sign-off that names the open issues it accepts, and a signatory that rises with risk. **It leaves [38]'s
release-moment content** (roll-back activation criteria, the business cost of delay, the configuration check after
implementation, the workforce-relations review) **to `launch-coordination-checklist` and `runbook`.** The companion
must cite [38] only for the first list.

**Licences decide what this bundle may adapt.** [14] is MIT ("MIT License", "Copyright (c) 2020 Mercari, Inc."), so
Mercari's evidence rule and not-applicable rule may be adapted with attribution. [1] and [2] are CC BY-NC-ND 4.0, which
forbids derivatives: quote them, never adapt their wording. [5] is "Copyright © 2017 Susan Fowler. All rights
reserved." [16] records that GitLab's project states no licence. The rest state none on the pages read.

**The family is `standing-standards`, `classification: tool`, by
[ADR 0062](../../docs/internal/decisions/0062-production-readiness-review-joins-standing-standards-as-a-tool.md).**
The bundle is the standing questionnaire; the worked example is one filled review.

---

## Claims flagged contested or time-bound

1. **What starts a review.** [1]: "When a development team requests that SRE take over production management of a
   service, SRE gauges both the importance of the service and the availability of SRE teams." [9]: before a service
   receives real production traffic. [6]: each maturity level ("It is only required to fill in the items up to and
   including the corresponding maturity level and lower."). [21]: "the ORR Lifecycle for New Service and Iterations is
   initiated when a new service, new feature, or architecture change is proposed". [38]: each release. **No trigger is
   universal; the template asks the team to name its own.**
2. **How often.** One-time: [1] ("After sufficient improvements are made and the service is deemed ready for SRE
   support, an SRE team assumes its production responsibilities.") and [4] ("Once the issues have been fixed, the
   product has passed the PRR."), though [4] is reconsidering ("We're looking into a periodic and/or incremental PRR as
   part of our continuous product improvements."). Event-driven plus annual: [21] ("at least annually, teams are
   expected to perform an ORR on their full service using a checklist tailored to that event"). Continuous, at every
   deployment: [25] and [27] ("you could create a Workflow that blocks deployment based on Scorecard scores"). Staged
   across the lifecycle: [39] ("The key is making ORR a continuous exercise rather than a one-time checklist.").
   **Four camps; the full template's Review Cadence section asks the team to take a position and say why.**
3. **Who reviews.** Outside the team: [4] ("an experienced engineer, ideally outside of the product team"), [34] ("To
   maximise the potential to identify risks, and remove biases, reviewers should be external to the team."), [1] ("Usually
   one to three SREs are selected or self-nominated to conduct the PRR process."), [3]. The team itself: [35] ("the team
   themselves should be the ones who define what their criteria are for production readiness, because they know that
   software best"), [9] ("Verify if each item is satisfied or not by your own team."), and [17]'s self-assessments,
   reviewed at a meeting ([22]). **Two named practitioners in the same magazine disagree; the companion reports both.**
4. **What the outcome is called.** [37]'s four states are one author's "recommended governance model"; [36]'s binary is
   a vendor's; [4]'s is "passed"; [3] asks the document to "state clearly whether the service merits SRE takeover, and if
   so, why (or why not)". **No vocabulary is standard. The template offers Ready, Ready with conditions and Not ready,
   attributed to [37], and drops [37]'s fourth state, which concerns a launch whose scope or date moved.**
5. **Who decides a blocking finding.** [22]: "Any high-criticality findings are escalated to leadership as input to a
   go or no-go launch decision." [25]: "The directly responsible individual (DRI) should make the final decisions with
   input from key stakeholders and technical decision-makers." [38] raises the signatory with the risk ("based on the
   operational risk factors for the release, the CTO Enterprise Architecture and IT Planning Branch will indicate if
   additional sign-off by FSA Senior Management is required"). [34] leaves follow-up to the reviewed team ("It is
   generally up to the development team to decide whether and how to follow up on those risks.").
6. **Whether every finding blocks.** [3]: "not all issues are blockers to SRE takeover (there might be design or
   architectural changes that SREs recommend for service robustness that could take many months to implement)". [20]
   keeps lesser risks out of the checklist entirely ("Medium or low risks aren't included in the ORR to keep it a
   lightweight process that doesn't overburden teams and reduce their agility and ability to innovate."). [37] grades
   gates ("A practical gate model has three levels: Blocking ... Conditional ... Advisory ...").
7. **How depth is tiered.** Per section by maturity gate ([6]); per row by service level, chosen by target SLO ([13]:
   "The main factor of choosing a Service Level is the expected SLO."); per occasion ([21]: "AWS uses different
   checklists for different occasions and workload types."). [12] carries one row that a higher level drops rather than
   keeps (Manual Scale, replaced by Auto Scale). **No source exempts a service from review outright**; every source that
   speaks to it scales the review instead ([35]: "I've seen people do PRRs that just consisted of filling in a template
   document over a couple of hours.").
8. **Is GitLab's process live?** See above: [7] against [8].
9. **The name.** "SRE entrance review" ([3]: "During an SRE entrance review (SER), also referred to as a Production
   Readiness Review (PRR), the SRE team takes the measure of a service currently running in production."), Production
   Readiness Check ([9]), Operational Readiness Review ([17]). NASA and the US DoD use "Production Readiness Review" for a
   hardware-manufacturing milestone ([32], [33]), and [38] uses it for a per-release go-live review.
10. **The boundary with the launch checklist.** Google's own chapters separate them: a PRR starts when a team asks SRE
    to take over a running service ([1]), while "Most audits are conducted before a new product or service launches."
    ([29]). Both founding checklists are engineering-scoped: Appendix E's ten headings ([28]) name no marketing, legal,
    communications or pricing area. The cross-functional reach of launch coordination lives in the team's role, not the
    checklist: "As a nonpartisan advisor, an LCE plays a balancing and mediating role between stakeholders including
    SRE, product developers, product managers, and marketing." ([29]). **Adopters blur the trigger** (item 1), so
    trigger alone does not separate the two in practice. **What differs in every source read is the object**: a PRR
    reviews a service's standing ability to be run ([1]: "a process that identifies the reliability needs of a service
    based on its specific details"; [9]: "required for all services"), and the launch checklist reviews one launch. That
    reading is this library's, drawn from the sources' own wording, and the companion labels it so.
11. **The domains.** No two sources agree on a taxonomy. Monitoring is a heading in all four of [1], [5], [6] and [12];
    capacity or performance is a heading in [1], [5] and [6]; architecture and dependencies in [1] and [20]; change or
    deployment in [1], [6] and [20]; emergency response or event management in [1], [5] and [20]; security in [6], [11],
    [12] and [28]; data recovery in [6], [12] and [20]; documentation in [5] and [12]'s Accessibility section.

---

## Notes for the companion

**The honest framing.** A production readiness review asks whether a service can be run, before someone who did not
build it takes on running it. Google named it and made it the first step of SRE engagement ([1]: "A PRR is considered a
prerequisite for an SRE team to accept responsibility for managing the production aspects of a service."). Three bodies
publish the document ([5], [6], [9] to [12]); everything past the core varies: when it runs, how often, who
reviews, what the outcome is called, and how depth is tiered. The name collides with a hardware milestone ([32], [33])
and, in one agency's use, with a release go-live review ([38]).

**The evidentiary spine, in the order it should be used:**

- **Definition and goals:** [1], [3], [4], quoted above; [2] places passing it at general availability ("In this phase,
  the service has passed the Production Readiness Review (see Chapter 32 in Site Reliability Engineering for more
  details) and is accepting all users.").
- **Published structure:** [5]'s five headings; [6]'s three gates; [11] and [12]'s phase checklists with per-row levels;
  [20]'s groupings ("Architecture", "Release quality", "Event management"); [38]'s required content.
- **Evidence and not-applicable, sourced three times:** [9] ("If it is satisfied, check the item in the list and provide
  evidence (e.g. links to tickets, screenshots, documents, test results, ...) showing that it is satisfied."; "If a
  specific item is not applicable to your service check the item and explain, as evidence, why it's not applicable."),
  [6] ("Leave all non-applicable items intact and add 'N/A' or reasons for why in place of the response."), and [38]
  ("No item in the PRR should only be marked “N/A” or “Not Applicable;” instead an explanation should be provided as to
  why a particular item does not apply."). [9] is MIT and may be adapted.
- **Findings and conditions:** [34] ("That list should include: what risks were identified; their criticality;
  recommendations on how to address the risk"), [37]'s finding record, [36] ("When gaps are identified, teams either
  address them before launch or document an exception with an expiration date and a plan to remediate."), [38] ("When
  FSA Management signs-off on the PRR, they are approving implementation even with the issues listed."), [3].
- **Keeping the checklist itself current:** [20]'s three sources of questions ("Real incidents that you've had in the
  past", "Near-misses that you've had in the past", "The failure modes that haven't occurred, but that you're concerned
  about"), [22]'s incident review question ("Would any ORR recommendations have reduced or avoided the impact of this
  event?"), [23], [4]'s organic updates, [37] ("Do not add a question merely because something once went wrong. State
  the failure it prevents, the evidence that answers it, and the launch types for which it applies."), [34] ("Keep the
  template current, relevant, usable, and no more complex than absolutely necessary.").
- **The neighbours:** [28], [29] for the launch checklist; [30] for the Definition of Done ("The Definition of Done is a
  formal description of the state of the Increment when it meets the quality measures required for the product."); [31]
  for the change advisory board ("A change-advisory board (CAB) delivers support to a change-management team by advising
  on requested changes, assisting in the assessment and prioritization of changes."); the runbook quotations above;
  [32], [33] and [38] for the name.

**How it fails, as sourced, and nothing more:**

- **Engagement that starts too late to change the design.** [1]: "the main limitations of the PRR Model stem from the
  fact that the service is launched and serving at scale, and the SRE engagement starts very late in the development
  lifecycle". The model's own stated limitation.
- **No goal, so no priority.** [34]: "Running a PRR without any specific goal means that the PRR can drop to the bottom
  of the development team's priority list."
- **A defensive team hides risk.** [34]: "If the development team feels threatened by the review, or that the team
  itself is under review, they can go on the defensive, and actively hide any potential risk in the system".
- **A template too heavy to fill.** [34]: "Keep the template current, relevant, usable, and no more complex than
  absolutely necessary."
- **Shallowness.** [35]: "You can't do another team's PRR for them."
- **The template as law.** [35]: "We should not build a PRR template and then make that a hard and fast rule, like a set
  of hoops that a team has to jump through to launch their service."
- **Forgetting the humans.** [35]: "This is one of the biggest antipatterns: forgetting the humans." The talk's point is
  that the time the owning team spends with the system is the value, not the filled form.
- **Drift after a one-time review.** [39] names it outright: "**Periodically** (approximately once per year) -
  Ensure operations haven't drifted but improved over time". [21]'s annual review exists for the same reason, and [4]
  is reconsidering its one-time design. [36]'s survey figure is not used.

**What this bundle must not say:** that the launch checklist is cross-functional and the PRR engineering-only (Appendix
E [28] refutes it); that chapter 32 calls the launch coordination team a "lighter-weight alternative" (not on the page);
that any outcome vocabulary is an industry standard; that any service is exempt from review (no source says so); any
percentage from [36]; Cortex's category breakdown; that GitLab's process is current; that [38]'s release-moment content
is part of an SRE-lineage PRR; any build or release number for `dashboard-service`.

**The section design, as the research moved it from the spec.** Five sections in lean, three more in full, in this order
(lean is the ordered subset marked):

- **Scope and Trigger** (lean): what "production" means here, which service or services this review covers, what event
  starts a review (item 1's triggers as options, none as the default), and **what this review deliberately does not
  cover and where that is reviewed instead**, from the gap question ([39]: "Security must have its own, in-depth,
  review."). Name the hardware collision in the WHY.
- **Reviewer and Authority** (full): who reviews and who decides, with contested item 3 stated in the WHY; **when a
  blocking finding goes above the reviewer, and to whom**, from the gap question ([22], [25], [38]).
- **Readiness Criteria** (lean, the load-bearing table): criteria grouped by domain, each with the evidence that answers
  it, an owner, and a status. The domain rows are a starting set drawn from item 11, not one source's taxonomy, and the
  WHY says which sources carry which. Evidence and status follow [9] (MIT). A full-size table may add whether a criterion
  blocks ([3], [37]) and the tier that requires it ([6], [13]). The ASK may include [39]'s open question "What are you
  worried about?", attributed. Carries PRIORITY and ROW HINT.
- **Not-Applicable Rule** (lean): an item marked not applicable carries a written reason, sourced three times ([6],
  [9], [38]).
- **Outcome and Sign-off** (lean, a table section): the outcome (Ready, Ready with conditions, Not ready, attributed to
  [37]), the findings not met, each with its criticality ([34]), owner and due date ([36], [37]), and who signed. **A
  condition accepted at sign-off is listed, owned and dated, never implied** ([38], [36]). The TRAP: an empty findings
  list read as an all-clear ([38]: "If no risks are identified, then the IPT should indicate “No Risks Identified” in
  the first row of the risk table - there are always unknown risks.").
- **Review Cadence** (full): one-time, periodic, event-driven or continuous, and why (contested item 2). This is about
  re-reviewing a service.
- **When This Does Not Apply** (full): which services get a smaller check, and what that check is (contested item 7).
  The TRAP: a blanket exemption, which no source supports.
- **Review Trigger** (lean, contract-mandated): when **the checklist itself** must be revised, with a named owner and a
  condition. **For this member the condition is sourced, not the library's own**: an incident or near miss whose cause
  a criterion should have caught ([20], [22], [23]), tempered by [37]'s rule that a new question states the failure it
  prevents and the evidence that answers it. This differs from the contract's 2026-08-07 finding for its first two
  members, where no source supplied a condition, and the companion should say so.

**Gap-question candidates, routed by decision procedure 12:**

- **Admitted to the template, each homed in an existing section and sized:** conditions listed at sign-off with an
  owner and a due date (Outcome and Sign-off, lean; E1 on [36], [37], [38]); escalation of a blocking finding to a
  named decider (Reviewer and Authority, full; E1 on [22], [38]); a named scope exclusion (Scope and Trigger, lean; E1
  on [39]).
- **To the guide, as a rubric row or anti-pattern:** an empty findings list is not an all-clear ([38]); each signature
  says what it certifies ([38]'s Test Lead and Information Owner attestations), as a rubric cell rather than a field;
  reviewers chosen for different perspectives ([39]: "The more diversity, the better. We want to avoid confirmation bias
  and surface different perspectives on how the system might behave.").
- **Declined, because they belong to the release moment, not to a service's readiness to be run:** [38]'s roll-back
  activation criteria, business cost of delay, post-implementation configuration check, workforce-relations review and
  Pre-PRR rehearsal. `launch-coordination-checklist` and `runbook` are their homes, and the companion says so in one
  sentence.
- **Declined as out of scope for a review document:** [39]'s normalization-of-deviance and organizational-learning
  prompts, which assess an operating culture over time rather than one service's readiness.

**Teaching points the templates, guide and example must stay consistent with:**

- **A PRR asks whether a service can be run by whoever will carry its pager** ([1], [3]), not whether one launch is
  coordinated.
- **Every criterion has evidence, and every "not applicable" has a reason** ([6], [9], [38]).
- **Not every finding blocks, and every accepted condition has an owner and a date** ([3], [36], [37], [38]).
- **The reviewers are named, and who decides a blocking finding is named** ([1], [22], [25], [34]).
- **The checklist is standing, and incidents are what revise it** ([20], [22], [23], [4]).
- **A runbook is checked for, not produced** ([5], [6], [12], [27], [39]).
- **It is not the launch checklist, a Definition of Done, a CAB, or a hardware production review** ([28], [29], [30],
  [31], [32], [33]).

**The example.** Acme Analytics' Reporting team, which owns `dashboard-service` (`runbook_example.md` names Marcus
Bell, Staff Engineer, Reporting, as its owner), asks a newly formed SRE function to take over its production
ownership, and the review on **2026-08-22** decides whether SRE accepts. *(The spec says the Platform team asks; the
service belongs to Reporting, so Reporting asks.)* **Two reviewers, both outside Reporting**, following [34]'s "two
reviewers tends to be the sweet spot" and satisfying both reviewer models in contested item 3: **Ines Halvorsen**, an
engineer in the new SRE function, which is the team [1] says conducts the review, and **Dana Osei** (Staff Engineer,
Platform), the experienced outside engineer of [4]. Marcus Bell answers as the service owner. The example states this
choice in its Reviewer and Authority section rather than leaving it implied. It may cite
that DEF-2291 happened on 2026-07-13 and that a regression guard and an entitlement-audit reconciliation job exist as a
result (`runbook_example.md`), as evidence for monitoring and on-call rows. **It must not repeat the launch checklist
example's own checks** (the permission matrix, the dashboard-scoped kill switch), **and it cites no build or release
number.** A "Ready with conditions" outcome, with each condition owned and dated, demonstrates the section the research
most changed. **The templates' GOOD and WEAK text must use a different service and a different incident**: grep the
drafted templates for Acme, Dana Osei, Marcus Bell, Sam Okafor, Anjali Rao, Priya Nair, DEF-2291 and
`dashboard-service` before review.

**The pairing.** `pairs_with: []`, per the spec's check of pm-skills on 2026-09-27.

**The aliases.** Keep `PRR`. Add `production readiness checklist` and `PRC` ([9]'s own name, "Production Readiness
Check (PRC)"), `SRE entrance review` and `SER` ([3]), and `operational readiness review` and `ORR` ([17]), which names
AWS's version of the practice. AWS never calls it a PRR, and [17] describes it as "a complementary process to
Well-Architected", not to a PRR; the companion says so. The catalog has no separate ORR entry for the alias to collide
with. Drop `launch readiness review`, which no source read uses.

**Catalog corrections for the landing:** aliases as above; relationships gain `Launch Coordination Checklist` and
`Runbook`, and `runbook`'s gain `PRR`; timing reads "before go-live", which [1] contradicts ("can be started at any point
of the service lifecycle") and [21] widens, so it should read `before production traffic or an ownership handoff; may
recur`; the notes column's "Google SRE practice" should name that NASA and the US DoD use the name for a
hardware-manufacturing review.

---

## Sources
### CANON: DEFINITION, LINEAGE, AND THE REVIEW AS GOOGLE DESCRIBES IT

**[1] Google, Site Reliability Engineering (O'Reilly, 2016), ch. 32, "The Evolving SRE Engagement Model" (Written by Acacio Cruz and Ashish Bhambhani).** primary. **fetched-and-verified.**
`https://sre.google/sre-book/evolving-sre-engagement-model/`
Supports: Definition, goals, trigger, team, timing, evaluation-domain list, outcome mechanics, model limitations, and the licence footer; also the source that refutes the 'lighter-weight alternative' claim about the LCE team.
Quotable: "The most typical initial step of SRE engagement is the Production Readiness Review (PRR), a process that identifies the reliability needs of a service based on its specific details."
Quotable: "A PRR is considered a prerequisite for an SRE team to accept responsibility for managing the production aspects of a service."
Quotable: "Verify that a service meets accepted standards of production setup and operational readiness, and that service owners are prepared to work with SRE and take advantage of SRE expertise."
Quotable: "Improve the reliability of the service in production, and minimize the number and severity of incidents that might be expected. A PRR targets all aspects of production that SRE cares about."
Quotable: "When a development team requests that SRE take over production management of a service, SRE gauges both the importance of the service and the availability of SRE teams."
Quotable: "Usually one to three SREs are selected or self-nominated to conduct the PRR process."
Quotable: "The Production Readiness Review can be started at any point of the service lifecycle, but the stages at which SRE engagement is applied have expanded over time."
Quotable: "System architecture and interservice dependencies"
Quotable: "Instrumentation, metrics, and monitoring"
Quotable: "Emergency response"
Quotable: "Capacity planning"
Quotable: "Change management"
Quotable: "Performance: availability, latency, and efficiency"
Quotable: "After sufficient improvements are made and the service is deemed ready for SRE support, an SRE team assumes its production responsibilities."
Quotable: "Improvements are prioritized based upon importance for service reliability. The priorities are discussed and negotiated with the development team, and a plan of execution is agreed upon."
Quotable: "the main limitations of the PRR Model stem from the fact that the service is launched and serving at scale, and the SRE engagement starts very late in the development lifecycle"
Quotable: "Microservices also imply an expectation of lower lead time for deployment, which was not possible with the previous PRR model (which had a lead time of months)."
Quotable: "The Launch Coordination Engineering (LCE) team (see Reliable Product Launches at Scale) spends a majority of its time consulting with development teams."
Quotable: "Copyright © 2017 Google, Inc. Published by O'Reilly Media, Inc. Licensed under CC BY-NC-ND 4.0"

**[2] Google, The Site Reliability Workbook (O'Reilly, 2018), Chapter 18 "SRE Engagement Model" (By Michael Wildpaner, Gráinne Sheerin, Daniel Rogers, and Surya Prashanth Sanagavarapu, with Adrian Hilton and Shylaja Nukala).** primary. **fetched-and-verified.**
`https://sre.google/workbook/engagement-model/`
Supports: Confirms chapter 32 as the PRR's own defining source, names the sibling ARR instrument, frames PRR completion as a GA-phase gate, and confirms the CC BY-NC-ND 4.0 licence on this book too.
Quotable: "Chapter 32 in our first SRE book describes technical and procedural approaches that an SRE team can take to analyze and improve the reliability of a service. These strategies include Production Readiness Reviews (PRRs), early engagement, and continuous improvement."
Quotable: "In this phase, the service has passed the Production Readiness Review (see Chapter 32 in Site Reliability Engineering for more details) and is accepting all users."
Quotable: "The engagements may involve Application Readiness Reviews (ARRs) and Production Readiness Reviews (PRRs), as described in Chapter 32 of Site Reliability Engineering. Proposed changes from ARR and PRR must be prioritized jointly by the developers and the SREs."
Quotable: "Conduct Production Readiness Reviews."
Quotable: "Copyright © 2018 Google, Inc. Published by O'Reilly Media, Inc. Licensed under CC BY-NC-ND 4.0"

**[3] Google Cloud, "How SREs at Google find the landmines in a service" (CRE Life Lessons, part 2), by Adrian Hilton et al..** vendor. **fetched-and-verified.**
`https://cloud.google.com/blog/products/gcp/how-sres-find-the-landmines-in-a-service-cre-life-lessons/`
Supports: Independent definition of the same review under the name SER/PRR, its trigger and team framed as negotiated, its four evaluation axes, and its outcome/documentation rule for both takeover and decline cases.
Quotable: "During an SRE entrance review (SER), also referred to as a Production Readiness Review (PRR), the SRE team takes the measure of a service currently running in production."
Quotable: "Assess how the service would benefit from SRE ownership"
Quotable: "Identify service design, implementation and operational deficiencies that could be a barrier to SRE takeover"
Quotable: "And if SRE ownership is determined to be beneficial, identify the bug fixes, process changes and necessary service behavior needed before onboarding the service"
Quotable: "the service owner and SRE team must agree to a process for the SRE team to understand and assess the service, and identify critical issues to be resolved upfront"
Quotable: "An SRE team typically designates a single person or a small subset of the team to familiarize themselves with the service, and evaluate it for fitness for takeover."
Quotable: "There are four main axes of improvement for a service in an onboarding process: extant bugs, reliability, automation and monitoring/alerting."
Quotable: "not all issues are blockers to SRE takeover (there might be design or architectural changes that SREs recommend for service robustness that could take many months to implement)"
Quotable: "an SRE entrance review should produce guidance that's useful to developers even if the SRE team declines to onboard the service"
Quotable: "the SRE entrance review document should also state clearly whether the service merits SRE takeover, and if so, why (or why not)"

**[4] Grafana Labs, "How we're building a production readiness review process at Grafana Labs" (company blog, 2021).** practitioner. **fetched-and-verified.**
`https://grafana.com/blog/2021/10/13/how-were-building-a-production-readiness-review-process-at-grafana-labs/`
Supports: Independent adopter's definition and goal statement, its own trigger/team mechanics, a binary outcome ('passed the PRR'), a find-then-fix process split, and stated limitations/future work; confirms no licence is stated in its footer.
Quotable: "Production readiness review (PRR) is a process that originated at Google, described as the first step of site reliability engineering engagement in the company's famous SRE book."
Quotable: "we've built production readiness review as a completely separate process that strives to add value by having the product in question reviewed by an experienced engineer, ideally outside of the product team. The output is a list of identified issues, which in the long run should reduce toil and risks that the product might face."
Quotable: "A member of a product team chosen to lead the process reaches out to the PRR team, asking for a review. The PRR team chooses a reviewer from the reviewer pool who will become the primary point of contact for this review."
Quotable: "During the meetings, we sometimes found it useful to have the reviewer assume the role of an attacker who tries to break the system in review. Any issues we identify are filed as product bugs."
Quotable: "Once the whole checklist is reviewed, the focus changes from finding to fixing issues."
Quotable: "Once the issues have been fixed, the product has passed the PRR."
Quotable: "We're looking into a periodic and/or incremental PRR as part of our continuous product improvements."
Quotable: "we've only started doing PRR, but both the checklist and the products are continuously evolving even while PRR is running"
Quotable: "As of now, any updates to the PRR checklist happen organically (i.e., when an issue is discovered during the review process). Figuring out ways to be more systematic with processing the feedback and updating the PRR could make a huge improvement."
Quotable: "The total duration of the PRR shouldn't be too long - as the product evolves, the checklist answers might start changing rapidly. This is especially true for pre-launch PRR."
Quotable: "Copyright 2026 © Grafana Labs"

### STRUCTURE: THE PUBLISHED CHECKLISTS, COUNTED

**[5] Susan Fowler - Production-Ready Microservices (O'Reilly, 2016), Appendix A, via the F5-sponsored free-chapters excerpt.** primary. **fetched-and-verified.**
`https://cdn.studio.f5.com/files/k6fem79d/production/fa24cb335b342add5e3b21a77efaa71462e7d6de.pdf`
Supports: the five-pillar checklist structure, item counts per pillar, licence (proprietary, no open licence), and that the appendix carries no per-item metadata fields
Quotable: "This will be a checklist to run over all microservices - manually or in an automated way."
Quotable: "A Production-Ready Service Is Stable and Reliable"
Quotable: "A Production-Ready Service Is Scalable and Performant"
Quotable: "A Production-Ready Service Is Fault Tolerant and Prepared for Any Catastrophe"
Quotable: "A Production-Ready Service Is Properly Monitored"
Quotable: "A Production-Ready Service Is Documented and Understood"
Quotable: "Copyright © 2017 Susan Fowler. All rights reserved."
Quotable: "(see Appendix A for a summary checklist containing the production-readiness standards and their general requirements)"
Quotable: "give each microservice a productionreadiness score measuring how production-ready their service is, require businesscritical services to have a high minimum production-readiness score, and gate deployments"
Quotable: "instructions on how to triage, mitigate, and resolve the alert should also be added to the service’s on-call runbook"

**[6] GitLab Inc. - gl-infra/readiness project, issue template `production_readiness.md` (archived project).** primary. **fetched-and-verified.**
`https://gitlab.com/gitlab-com/gl-infra/readiness/-/raw/master/.gitlab/issue_templates/production_readiness.md`
Supports: the three-gate (Experiment/Beta/GA) structure, per-gate subsection and item counts, the N/A rule, the [Security Compliance] item tag, the mandatory/optional reviewer roles, and how the outcome is recorded via labels
Quotable: "Create the first draft of the readiness review by copying the template below and submitting an MR. Do not remove any items or section in the template. It is only required to fill in the items up to and including the corresponding maturity level and lower."
Quotable: "While it is encouraged for parts of this document to be filled out, not all of the items below will be relevant. Leave all non-applicable items intact and add 'N/A' or reasons for why in place of the response."
Quotable: "This Guide is just that, a Guide. If something is not asked, but should be, it is strongly encouraged to add it as necessary."
Quotable: "Runway Team: {+ reviewer name +}"
Quotable: "InfraSec: {+ reviewer name +}"
Quotable: "Cells Infrastructure: {+ reviewer name +}"
Quotable: "Once the MR has been sent out for review, add a `~"Readiness::*` scoped label for the corresponding target maturity level"
Quotable: "If the feature will remain at the current maturity level for an uncertain amount of time, close the issue and add a `~"workflow-infra::done"` label to the issue."
Quotable: "Link to the troubleshooting runbooks."
Quotable: "Link to an example of an alert and a corresponding runbook."
Quotable: "Experiment"
Quotable: "Beta"
Quotable: "General Availability"
Quotable: "Monitoring and Alerting"
Quotable: "Deployment"
Quotable: "Backup, Restore, DR and Retention"
Quotable: "Performance, Scalability and Capacity Planning"
Quotable: "Security Considerations"
Quotable: "Operational Risk"

**[7] GitLab Inc. - gl-infra/readiness project README (archived).** primary. **fetched-and-verified.**
`https://gitlab.com/gitlab-com/gl-infra/readiness/-/raw/master/README.md`
Supports: that the project is archived, and what superseded it
Quotable: "This project is archived and no longer active."
Quotable: "The Production Readiness Review process has been superseded by PREP (Platform Readiness Enablement Process)."
Quotable: "If you are looking to get a change reviewed for production readiness, please use PREP instead:"
Quotable: "This project is archived and preserved for historical reference only. No new reviews should be opened here."
Quotable: "The readiness process has been consolidated into PREP (Platform Readiness Enablement Process), which provides a more comprehensive path to production."

**[8] GitLab Inc. - Runway platform documentation, "Production Readiness Review" guide.** vendor. **fetched-and-verified.**
`https://docs.runway.gitlab.com/guides/production-readiness/`
Supports: that this page is a thin pointer to the same readiness-project issue template, not an independent checklist, and that it contradicts the README's archived status by directing users to create an issue in that project
Quotable: "A guide for streamlining production readiness review for Runway services."
Quotable: "SaaS Platforms uses production readiness review process for new services."
Quotable: "Create an issue using Runway template in the readiness project."
Quotable: "Follow the Readiness Checklist in the Runway template."

**[9] Mercari, Inc., guide "Check Production Readiness" (production-readiness-checklist repository).** practitioner. **fetched-and-verified.**
`https://github.com/mercari/production-readiness-checklist/blob/master/docs/guides/check-production-readiness.md`
Supports: the four-step process, the evidence field and N/A rule verbatim, and the sign-off routing to architect team / merpay SRE
Quotable: "This documentation describes the steps to do Production Readiness Check (PRC), which is required for all services before receiving real production traffic."
Quotable: "Verify if each item is satisfied or not by your own team."
Quotable: "If it is satisfied, check the item in the list and provide evidence (e.g. links to tickets, screenshots, documents, test results, ...) showing that it is satisfied. If evidence is not provided the review process will take much longer."
Quotable: "If a specific item is not applicable to your service check the item and explain, as evidence, why it's not applicable."
Quotable: "If it's a Mercari microservice, please ask architect team"
Quotable: "If it's a Merpay microservice, please ask merpay SRE"

**[10] Mercari, Inc., index page `production-readiness-checklist.md` (production-readiness-checklist repository).** practitioner. **fetched-and-verified.**
`https://raw.githubusercontent.com/mercari/production-readiness-checklist/master/docs/references/production-readiness-checklist.md`
Supports: that the file the task named is an index, not the checklist itself, pointing to two phase files, and the Level A/B/C tiering definition and icon conventions
Quotable: "The checklists are divided into 2 phases:"
Quotable: "Design checklist (the checklist you must meet before beginning development of your microservice)"
Quotable: "Pre-production checklist (the checklist you must meet before production deployment)"
Quotable: "Level A - for a critical microservice"
Quotable: "Level B - for a standard microservice"
Quotable: "Level C - for an experimental microservice"
Quotable: "indicates that passing the first check is required to meet the level."

**[11] Mercari, Inc., `design-checklist.md` (production-readiness-checklist repository).** practitioner. **fetched-and-verified.**
`https://raw.githubusercontent.com/mercari/production-readiness-checklist/master/docs/references/design-checklist.md`
Supports: the design-phase checklist's three sections and per-row Level A/B/C tiering, and that the file is machine-generated
Quotable: "<!-- File generated by script/update_prc_docs. DO NOT EDIT. -->"
Quotable: "This checklist contains items are things that must be considered during the design phase and verified before the start of implementation."
Quotable: "General"
Quotable: "Security"
Quotable: "Sustainability"

**[12] Mercari, Inc., `pre-production-checklist.md` (production-readiness-checklist repository).** practitioner. **fetched-and-verified.**
`https://raw.githubusercontent.com/mercari/production-readiness-checklist/master/docs/references/pre-production-checklist.md`
Supports: the pre-production checklist's eight sections/subsections and per-row Level A/B/C tiering, including the one non-monotonic row
Quotable: "This checklist contains points that must be satisfied during implementation and verified prior to release."
Quotable: "Please note that all items in the design checklist that were verified at the end of the design phase, must still be satisfied at release time"
Quotable: "Manual Scale | It can be manually scaled horizontally to handle changes in workload. | :white_check_mark: | | |"
Quotable: "Auto Scale ... | | :white_check_mark: | :white_check_mark: |"
Quotable: "It has OnCall playbooks."
Quotable: "Maintainability"
Quotable: "Observability"
Quotable: "Reliability"
Quotable: "Security"
Quotable: "Accessibility"
Quotable: "Data Storage"

**[13] Mercari, Inc., `production-readiness-level.md` (production-readiness-checklist repository).** practitioner. **fetched-and-verified.**
`https://raw.githubusercontent.com/mercari/production-readiness-checklist/master/docs/references/production-readiness-level.md`
Supports: the SLO basis for choosing a level and the level definitions
Quotable: "The main factor of choosing a Service Level is the expected SLO."
Quotable: "A | > 99.9%"
Quotable: "B | 99% ~ 99.9%"
Quotable: "C | 95% ~ 99%"
Quotable: "Level A is for critical microservices."
Quotable: "Level B is for standard microservices."
Quotable: "Level C is for experimental microservices"

**[14] Mercari, Inc., `LICENSE` file (production-readiness-checklist repository).** practitioner. **fetched-and-verified.**
`https://raw.githubusercontent.com/mercari/production-readiness-checklist/master/LICENSE`
Supports: the licence, cross-checked against the GitHub API's repository metadata
Quotable: "Copyright (c) 2020 Mercari, Inc."
Quotable: "MIT License"

**[15] GitHub API - repository metadata for mercari/production-readiness-checklist.** reference. **fetched-and-verified.**
`https://api.github.com/repos/mercari/production-readiness-checklist`
Supports: confirmation that GitHub's own detection reports the licence as MIT, matching the LICENSE file text
Quotable: ""key": "mit""
Quotable: ""name": "MIT License""
Quotable: ""spdx_id": "MIT""

**[16] GitLab API - project metadata for gitlab-com/gl-infra/readiness.** reference. **fetched-and-verified.**
`https://gitlab.com/api/v4/projects/gitlab-com%2Fgl-infra%2Freadiness?license=true`
Supports: that the GitLab readiness project states no licence: the API's license field returns null and no raw LICENSE file exists at the repo root (confirmed 404)

### DIMENSION 3: Cadence, gating, and the cloud frameworks (AWS ORR whitepaper, Azure Well-Architected operational excellence, Cortex production-readiness Scorecard)

**[17] Amazon Web Services - "Operational Readiness Reviews (ORR)" whitepaper, landing page (Abstract and introduction).** vendor. **fetched-and-verified.**
`https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html`
Supports: Whitepaper purpose, publication date, and framing of ORR as a data-driven, complementary process to Well-Architected; establishes it is not a one-off audit but reused across a service's lifecycle.
Quotable: "Publication date: June 30, 2022"
Quotable: "Amazon Web Services (AWS) created the Operational Readiness Review (ORR) to distill the learnings from AWS operational incidents into curated questions with best practice guidance."
Quotable: "Teams perform self-assessments on operational risks to achieve operational excellence by reviewing the appropriate ORR checklist throughout the complete lifecycle of their service, from inception to post-release operations."
Quotable: "ORR is a complementary process to Well-Architected, using a data-driven approach to ensure a consistent review of operational readiness, with a specific focus on eliminating known, common causes of impact in your workloads."

**[18] AWS - "Building mechanisms" (ORR whitepaper section).** vendor. **fetched-and-verified.**
`https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/building-mechanisms.html`
Supports: Frames ORR explicitly as a recurring mechanism rather than a one-off checklist, feeding the cadence camp.
Quotable: "The cyclic nature of a mechanism makes it best suited for solving recurring problems or opportunities, as opposed to one-off challenges."
Quotable: "The ORR is a mechanism with a tool, an adoption process, and an inspection process that operates in a complete cycle."

**[19] AWS - "The ORR mechanism" (ORR whitepaper section).** vendor. **fetched-and-verified.**
`https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/the-orr-mechanism.html`
Supports: States the desired outcomes (fewer, shorter, smaller incidents) that motivate ORR and points to its four component sections.
Quotable: "the desired business result was higher levels of availability and resilience in our systems by decreasing the frequency of incidents (fewer), decreasing the duration of incidents (shorter), and decreasing the scope of impact of an incident (smaller)"

**[20] AWS - "The ORR tool" (ORR whitepaper section).** vendor. **fetched-and-verified.**
`https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/the-orr-tool.html`
Supports: Question grouping headings, per-question risk marking, the incident/near-miss/failure-mode question-generation method, and the checklist's deliberate scope limit to critical risks (bearing on exemption for lower-risk items).
Quotable: "Question: Do any of your hosts pin certificates?"
Quotable: "☐ Yes | High Risk"
Quotable: "☐ No | No Risk"
Quotable: "If you haven't had an incident related to certificate pinning, or it's not a high-priority item to address across your enterprise, then don't include this question. The ORR checklist is most effective when it's focused on incidents that present critical risks. These are the types of risks that would prevent a General Availability (GA) launch of a service. Medium or low risks aren't included in the ORR to keep it a lightweight process that doesn't overburden teams and reduce their agility and ability to innovate."
Quotable: "Real incidents that you've had in the past"
Quotable: "Near-misses that you've had in the past"
Quotable: "The failure modes that haven't occurred, but that you're concerned about"
Quotable: "Architecture"
Quotable: "Release quality"
Quotable: "Event management"
Quotable: "Deployment safety"
Quotable: "Defense against customers"
Quotable: "Defense against dependencies"
Quotable: "Data recovery"
Quotable: "Operator safety"
Quotable: "Blast radius containment"
Quotable: "Event detection"
Quotable: "Service restart"
Quotable: "Forensics"
Quotable: "Escalation"

**[21] AWS - "Gaining adoption" (ORR whitepaper section).** vendor. **fetched-and-verified.**
`https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/gaining-adoption.html`
Supports: Direct textual basis for cadence: ORR is SDLC-embedded (event-triggered per launch/change) AND separately required at least annually for live services; also shows checklists vary by workload size/type, the closest AWS analog to a lighter review.
Quotable: "While the ORR name may imply on the surface that it is a "pre-launch" checklist, the process is actually built into the entire Software Development Lifecycle (SDLC)."
Quotable: "the ORR Lifecycle for New Service and Iterations is initiated when a new service, new feature, or architecture change is proposed"
Quotable: "The ORR Cycle Start phase begins during the Design phases of the SDLC process."
Quotable: "During the Mid-Cycle Check-in phase teams start to answer Development and Testing related questions."
Quotable: "in the ORR Conclusion and Follow-up phase, the team wraps up the ORR checklist and develops their risk mitigation and follow-up plan"
Quotable: "In addition to the ORR performed through the SDLC process, at least annually, teams are expected to perform an ORR on their full service using a checklist tailored to that event. This helps verify that they stay up to date with new or updated best practices, and also that nothing has changed within their systems."
Quotable: "AWS uses different checklists for different occasions and workload types."
Quotable: "Launching a new public service"
Quotable: "Recurring annual review"

**[22] AWS - "Inspect the process" (ORR whitepaper section).** vendor. **fetched-and-verified.**
`https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/inspect-the-process.html`
Supports: Directly answers who performs the review, who attends the outcome meeting, and what happens to a high-criticality finding.
Quotable: "AWS holds a weekly operational metrics meeting attended by thousands of engineers and leadership up to the Senior Vice President (SVP) level"
Quotable: "The results of the ORR are reviewed during a scheduled meeting with an audience including the engineering team, principal engineers in their organization, leadership and management, and any stakeholders from dependencies or customers of the service."
Quotable: "During the meeting, attendees review the completed checklist and provide feedback on the findings. Any high-criticality findings are escalated to leadership as input to a go or no-go launch decision."
Quotable: "the effectiveness of the ORR mechanism is inspected during the COE process. The COE template asks questions like "When was your last ORR performed?" and "Would any ORR recommendations have reduced or avoided the impact of this event?""

**[23] AWS - "Iteration" (ORR whitepaper section).** vendor. **fetched-and-verified.**
`https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/iteration.html`
Supports: How the question set is grown/maintained over time, and the dedicated 'Ops Champion' role in both performing reviews and curating the checklist.
Quotable: "AWS constantly seeks feedback on the ORR mechanism from its users, the AWS service teams. This drives the creation of new checklists for different occasions or different types of workloads"
Quotable: "a specialist engineering community called "Operational Champions" or "Ops Champion" for short"
Quotable: "The Ops Champion challenges the team on their answers to the checklist, provides context on the adoption and prioritization of best practices, and ends up influencing everything from workload architecture to operational culture in the team."
Quotable: "They review the outcomes of COEs and create new lessons learned and new best practices. There is a tight coupling between the COE process and ORR, we use the lessons learned to continually generate new content to deal with evolving risks in distributed systems."

**[24] AWS - "Conclusion" (ORR whitepaper section).** vendor. **fetched-and-verified.**
`https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/conclusion.html`
Supports: Restates the ORR as a cyclical mechanism (tool -> adopt -> inspect -> iterate), reinforcing the recurring framing.
Quotable: "The ORR mechanism consists of a tool that builders are driven to adopt, and then the results of the process are inspected. Based on the inspection, the mechanism is iterated and improved upon so that its effectiveness in achieving the desired results can be measured."

**[25] Microsoft - "Operational Excellence maturity model", Azure Well-Architected Framework, Microsoft Learn.** vendor. **fetched-and-verified.**
`https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/maturity-model`
Supports: Cadence camp 2: readiness is enforced continuously via staged-environment approval gates on every release, not as a discrete periodic or one-off review; shows who decides (a named DRI plus stakeholders) and how the approval path differs for regular vs. emergency changes.
Quotable: "it's important to establish release promotion as a formal change control protocol before going live. This process progresses proposed changes through various stages with quality gates. Each stage undergoes thorough testing, and changes advance only if they pass these checks and receive approval."
Quotable: "Approval for regular releases: When it comes to regular releases, moving from staging to production requires a different set of criteria. Decisions about releases, like moving to production, need approval from stakeholders, clear documentation, or both. The workload team should define who is part of the approval process and their responsibilities. In some regulatory cases, auditors might also be included in the decision-making process."
Quotable: "Have a separate process for hotfixes: For critical situations like deploying security patches, you might need an improvised deployment process. Create an emergency process to accelerate these high-priority fixes."
Quotable: "The directly responsible individual (DRI) should make the final decisions with input from key stakeholders and technical decision-makers."
Quotable: "Establish deployment frequency. Determine deployment frequency based on feature development. Agree on a schedule, whether it's daily, weekly, quarterly, or another suitable approach."

**[26] Microsoft - "Design review checklist for Operational Excellence", Azure Well-Architected Framework, Microsoft Learn.** vendor. **fetched-and-verified.**
`https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/checklist`
Supports: The question-set grouping on this page: a flat numbered list (OE:01-OE:11), not grouped under topical headings the way AWS's ORR groups by Architecture/Release quality/Event management; includes the safe-deployment-practices recommendation that is the closest analog to a gating item.
Quotable: "This checklist presents a set of recommendations to help you build a culture of operational excellence."
Quotable: "OE:01 Define your standard practices to develop and operate your workload."
Quotable: "OE:11 Clearly define your workload's safe deployment practices. Focus on small, incremental releases with quality gates. Use modern deployment patterns and progressive exposure to manage risk. Plan for both routine and emergency deployments."

**[27] Cortex - "Standardize and automate production readiness", Cortex Docs, Solutions > Production readiness > Configure.** vendor. **fetched-and-verified.**
`https://docs.cortex.io/solutions/production-readiness/configure`
Supports: General Scorecard description only (per instruction, no category/item breakdown reported): cadence is continuous/automated rather than periodic or one-time; gating happens per deployment event via Workflow automation with an optional manual sign-off step; readiness is a tiered score rather than a pass/fail review.
Quotable: "Scorecards automate the process of checking whether services meet criteria such as ownership, on-call coverage, runbooks, monitoring, and security requirements."
Quotable: "It is structured into three levels - Bronze, Silver, and Gold - with each representing increasing levels of production readiness."
Quotable: "You can add manual approval steps in a Workflow to require sign-off from specific team members before a service is considered production-ready, ensuring accountability and providing an audit trail."
Quotable: "you could create a Workflow that blocks deployment based on Scorecard scores, ensuring that a deployment is blocked if the entity has not met your standards for Production Readiness."
Quotable: "When the Workflow runs, it checks whether the entity has achieved the "Gold" level standard in the Scorecard. If it has, the deployment continues. If it has not, the Workflow automatically sends a Slack message to notify the entity owner."
Quotable: "Data verification is critical for ensuring the accuracy, consistency, and completeness of data before it is used in a production system."
Quotable: "Follow the Data Verification documentation to define verification periods for your entities."

### Dimension 4: neighbours and the boundary - production-readiness-review vs. launch-coordination-checklist

**[28] Google SRE Book, Appendix E - "Launch Coordination Checklist".** primary. **fetched-and-verified.**
`https://sre.google/sre-book/launch-checklist/`
Supports: The checklist's own section headings, used to test the engineering-only-PRR-vs-cross-functional-checklist claim
Quotable: "This is Google's original Launch Coordination Checklist, circa 2005, slightly abridged for brevity:"
Quotable: "Architecture"
Quotable: "Volume estimates, capacity, and performance"
Quotable: "System reliability and failover"
Quotable: "Monitoring and server management"
Quotable: "Security"
Quotable: "Automation and manual tasks"
Quotable: "Growth issues"
Quotable: "External dependencies"
Quotable: "Schedule and rollout planning"
Quotable: "Hard deadlines, external events, Mondays or Fridays"
Quotable: "Standard operating procedures for this service, for other services"
Quotable: "Machines and datacenters"

**[29] Google SRE Book, Chapter 27 - Rhandeev Singh, Sebastian Kirsch, Vivek Rau (ed. Betsy Beyer), "Reliable Product Launches at Scale".** primary. **fetched-and-verified.**
`https://sre.google/sre-book/reliable-product-launches/`
Supports: Trigger, team and timing for the LCE's launch reviews, and the LCE team's composition and cross-functional role
Quotable: ""Launch Reviews," as the Launch Engineers' consulting sessions came to be called, became a common practice days to weeks before the launch of many new products."
Quotable: "Their consulting sessions were formalized as Production Reviews."
Quotable: "Members of the LCE team audit services at various times during the service lifecycle. Most audits are conducted before a new product or service launches."
Quotable: "Staffed by software engineers and systems engineers - some with experience in other SRE teams - this team specializes in guiding developers toward building reliable and fast products"
Quotable: "As a nonpartisan advisor, an LCE plays a balancing and mediating role between stakeholders including SRE, product developers, product managers, and marketing."
Quotable: "External requirements from teams like marketing and PR might add further complications."
Quotable: "When to consult with the legal department"
Quotable: "To mitigate this scenario from the engineering perspective, SRE staffed a small, full-time team of LCEs in 2004."

**[30] Ken Schwaber and Jeff Sutherland, Scrum Guide (2020 revision).** primary. **fetched-and-verified.**
`https://scrumguides.org/scrum-guide.html`
Supports: The Definition of Done's object (the Increment) and who is accountable for conforming to it
Quotable: "Work cannot be considered part of an Increment unless it meets the Definition of Done."
Quotable: "The Definition of Done is a formal description of the state of the Increment when it meets the quality measures required for the product."
Quotable: "The moment a Product Backlog item meets the Definition of Done, an Increment is born."
Quotable: "If a Product Backlog item does not meet the Definition of Done, it cannot be released or even presented at the Sprint Review. Instead, it returns to the Product Backlog for future consideration."
Quotable: "The Developers are required to conform to the Definition of Done."
Quotable: "If it is not an organizational standard, the Scrum Team must create a Definition of Done appropriate for the product."
Quotable: "Instilling quality by adhering to a Definition of Done"

**[31] Wikipedia, "Change-advisory board".** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Change-advisory_board`
Supports: The CAB's unit of review (a requested change, not a launch or a program)
Quotable: "A change-advisory board (CAB) delivers support to a change-management team by advising on requested changes, assisting in the assessment and prioritization of changes."
Quotable: "As such, it has requests coming in from management, customers, users and IT. Plus the changes may involve hardware, software, configuration settings, patches, etc."
Quotable: "The CAB is tasked with reviewing and prioritizing requested changes, monitoring the change process and providing managerial feedback."
Quotable: "External approvals were negatively correlated with lead time, deployment frequency, and restore time, and had no correlation with change fail rate."

**[32] NASA, NASA Systems Engineering Handbook - Appendix (Definitions of Terms).** primary. **fetched-and-verified.**
`https://www.nasa.gov/reference/system-engineering-handbook-appendix/`
Supports: NASA's own definition of a Production Readiness Review
Quotable: "Production Readiness Review (PRR): A review for projects developing or acquiring multiple or similar systems greater than three or as determined by the project. The PRR determines the readiness of the system developers to efficiently produce the required number of systems. It ensures that the production plans, fabrication, assembly, integration-enabling products, operational support, and personnel are in place and ready to begin production."

**[33] AcqNotes, "Production Readiness Review (PRR)".** practitioner. **fetched-and-verified.**
`https://acqnotes.com/acqnote/acquisitions/production-readiness-review`
Supports: The DoD/hardware-manufacturing definition of PRR, and the roles that judge it (Technical Review Chair, PM, Systems Engineer)
Quotable: "The Production Readiness Review (PRR) determines if a systems design is ready for production and if the system developer has accomplished adequate production planning to enter Low-Rate Initial Production (LRIP) and Full-Rate Production (FRP)."
Quotable: "PRRs are normally performed as a series of reviews toward the end of the Engineering, Manufacturing, and Development (EMD) Phase."
Quotable: "The Technical Review Chair determines the successful completion of the PRR."
Quotable: "The manufacturing readiness process"
Quotable: "Quality management system"
Quotable: "Production planning"
Quotable: "System requirements compliance"
Quotable: "Inventory management"
Quotable: "Supplier management"

### Dimension 5: Running the review - reviewer, outcome, follow-up, and how it fails (production-readiness-review bundle)

**[34] Pedro Alves, "Production Readiness Reviews: A Surprisingly Versatile Practice" (USENIX ;login: online, April 28, 2025, shepherded by Laura Nolan).** practitioner. **fetched-and-verified.**
`https://www.usenix.org/publications/loginonline/production-readiness-reviews-surprisingly-versatile-practice`
Supports: Reviewer independence/seniority/count (a); tracking ownership (c); two named failure modes beyond buy-in/defensiveness (d); scope-vs-exemption discussion (e, null result)
Quotable: "To maximise the potential to identify risks, and remove biases, reviewers should be external to the team. Some degree of familiarity with the domain can be helpful, though."
Quotable: "In terms of review team size, two reviewers tends to be the sweet spot."
Quotable: "If there are Staff+, then these would be good candidates to review PRRs. In the absence of Staff+, or if the number of Staff+ engineers is also low, look for Senior Engineers with an operational mindset."
Quotable: "It is generally up to the development team to decide whether and how to follow up on those risks."
Quotable: "That list should include: what risks were identified; their criticality; recommendations on how to address the risk"
Quotable: "On very rare occasions - but it has happened - it should be made abundantly clear to the development team that the system under review should not go live at all, until a considerable redesign has taken place."
Quotable: "Finally, the work involved in filling in the PRR template needs to be acceptable to the development team. Keep the template current, relevant, usable, and no more complex than absolutely necessary."
Quotable: "A PRR should only rely on a single document, regardless of the number of services included."
Quotable: "Running a PRR without any specific goal means that the PRR can drop to the bottom of the development team’s priority list."
Quotable: "If the development team feels threatened by the review, or that the team itself is under review, they can go on the defensive, and actively hide any potential risk in the system"

**[35] Laura Nolan, "Why Don't We Have a Fire Code for Software?" (QCon Plus, April 14, 2022, transcript published on InfoQ).** practitioner. **fetched-and-verified.**
`https://www.infoq.com/presentations/fire-code-software/`
Supports: Reviewer model / who runs a PRR (a); three named PRR antipatterns as failure modes (d); implicit calibration of review depth to criticality (e)
Quotable: "Typically, SREs, or another owning team would do a Production Readiness Review, at the start of an engagement with a service."
Quotable: "This is where I've very strongly argued that the team themselves should be the ones who define what their criteria are for production readiness, because they know that software best."
Quotable: "If that's a really critical service that cannot fail, that cannot lose data, I think the best thing is to embed engineers in, and have those engineers work with that team for a quarter or maybe two quarters, or maybe longer depending on the size and the complexity and the criticality of it."
Quotable: "Shallowness is a PRR antipattern. ... A big part of a PRR is just giving the team that's going to be owning that system, time and space to spend with it, to think about the failure modes, and what it needs, and what it's missing. You can't do another team's PRR for them."
Quotable: "We should not build a PRR template and then make that a hard and fast rule, like a set of hoops that a team has to jump through to launch their service."
Quotable: "This brings me on to our third PRR antipattern. This is one of the biggest antipatterns: forgetting the humans."
Quotable: "For my part, I think that for any complex or critical service, I think a PRR should take at least one person a quarter."
Quotable: "I've seen people do PRRs that just consisted of filling in a template document over a couple of hours."

**[36] Cortex, "Production readiness review checklist & best practices" (Cortex engineering blog, January 14, 2026).** vendor. **fetched-and-verified.**
`https://www.cortex.io/post/how-to-create-a-great-production-readiness-checklist`
Supports: Reviewer composition (a); explicit binary outcome vocabulary (b); exception-with-expiration closure tracking (c); tailoring review weight by service type (e)
Quotable: "In a typical PRR, a service owner walks through their readiness checklist with stakeholders from platform engineering, SRE, security, and sometimes product."
Quotable: "Think of it as a structured gate where service owners validate their work against a shared checklist, cross-functional stakeholders review potential risk areas, and criteria are either passed or flagged for follow-up."
Quotable: "When gaps are identified, teams either address them before launch or document an exception with an expiration date and a plan to remediate."
Quotable: "Cortex provides an exception-handling workflow with built-in expiration dates. Teams can ship on time while staying accountable for closing gaps after launch, which prevents exceptions from becoming permanent technical debt."
Quotable: "What matters for a customer-facing API is different from what matters for an internal batch job. Your checklist should be tailored to the type of service being launched while still maintaining organizational consistency."

**[37] Nawaz Dhandala, "Run a Production Readiness Review with Evidence and Real Gates" (OneUptime engineering blog, August 6, 2026).** vendor. **fetched-and-verified.**
`https://oneuptime.com/blog/post/2026-08-06-production-readiness-review-evidence-owners-launch-gates/view`
Supports: Explicit four-state outcome vocabulary (b); per-finding closure tracking with named owner/due date/verification method (c); owner-vs-reviewer role separation (a); risk-tiered evidence/gate levels as a lighter-review mechanism (e)
Quotable: "The decision should have one of four states:"
Quotable: "all blocking controls have acceptable evidence"
Quotable: "approved, time-bounded exceptions cover every open blocker"
Quotable: "one or more blocking findings remain unresolved"
Quotable: "These states are a recommended governance model, not a Google, AWS, or Kubernetes platform behavior."
Quotable: "For each finding, capture: severity and customer or business consequence; exact affected scope; evidence that produced the finding; remediation and named owner; due date and verification method; whether it blocks launch; exception record, if the risk is accepted temporarily."
Quotable: "The service owner owns readiness. Reviewers challenge evidence and apply policy; they should not become the default owners of every remediation item. An approval meeting with no accountable service owner is itself a readiness gap."
Quotable: "A practical gate model has three levels: Blocking ... Conditional ... Advisory ..."
Quotable: "Tailor this list to the change. ... Requiring the same evidence from a text-only user-interface change and a cross-region data migration makes teams route around the process."
Quotable: "Do not add a question merely because something once went wrong. State the failure it prevents, the evidence that answers it, and the launch types for which it applies."
Quotable: "Ready with conditions"
Quotable: "Not ready"
Quotable: "Withdrawn"

### Dimension 6: The gap question - production-readiness-review

**[38] Federal Student Aid (U.S. Department of Education, Chief Technology Office) - "Production Readiness Review (PRR) Process Description," Version 26.0, 7/31/2026.** primary. **fetched-and-verified.**
`https://studentaid.gov/sites/default/files/fsawg/static/gw/docs/ciolibrary/PRR_Process.pdf`
Supports: Multiple candidate elements beyond the obvious structure: (1) sign-off that explicitly accepts disclosed open issues rather than requiring their resolution; (2) role-differentiated sign-off where each signatory certifies a distinct substantive claim, not one generic approval; (3) a graduated/escalating second sign-off tier triggered by the release's risk rating; (4) pre-committed rollback-activation criteria as their own artifact, distinct from the readiness-criteria table; (5) a documented business-cost-of-delay narrative alongside readiness criteria; (6) a built-in Lessons Learned section tied to an organization-wide knowledge database; (7) a post-implementation verification step that re-checks configuration/scan state after go-live, closing the loop rather than stopping at sign-off; (8) explicit instruction that reviewers state 'no risks identified' rather than leave the item blank, paired with the caveat that unknown risks always remain; (9) workforce/labor-relations impact as a named readiness dimension distinct from technical domains; (10) a formal rehearsal step (Pre-PRR) of the readiness review itself, separate from the review that carries the sign-off.
Quotable: "When FSA Management signs-off on the PRR, they are approving implementation even with the issues listed."
Quotable: "If no risks are identified, then the IPT should indicate “No Risks Identified” in the first row of the risk table - there are always unknown risks."
Quotable: "In addition, based on the operational risk factors for the release, the CTO Enterprise Architecture and IT Planning Branch will indicate if additional sign-off by FSA Senior Management is required."
Quotable: "The determination for second-level sign-off by FSA Senior Management should be discussed at the Pre-PRR to make sure that all parties are aware of the need to brief their Executive Committee members."
Quotable: "This slide should identify specific criteria for the conditions when a roll-back plan will be activated. The goal of this slide is to communicate the roll-back criteria to all stakeholders in advance of implementation; if those roll-back criteria are met during implementation activities, then the team will know that they should roll-back the release and re-plan the implementation. This advance planning prevents confusion and indecision during implementation activities."
Quotable: "This slide describes the process that the project is using for identifying lessons learned. This slide also describes how the lessons learned will be captured and maintained. Federal Student Aid has established a Lessons Learned Database for teams to enter lessons learned and share those lessons across the enterprise."
Quotable: "After the release is implemented, the System Technical Lead should repeat the CMDB request and update described in Step 9. Another copy of the CMDB report is reviewed to ensure that changes have been applied to the CMDB and that the version numbers are correct for items that were implemented in production (after implementation, the CMDB versions should match production)."
Quotable: "Test Lead - The Test Lead’s signature certifies that test results have been accurately reported at the PRR and there are no known outstanding test defects that will adversely impact the system or end-users."
Quotable: "Information Owner (Business Owner) - The information owner's signature certifies acceptance of business risks associated with implementation of the system or release."
Quotable: "Lastly, this slide includes a section for the evaluation of how the release impacts FSA employees. Particularly, the system owner needs to communicate the changes and technical details of the release to FSA Workforce Relations to be evaluated for changes to work processes and work conditions for federal staff... In some situations, FSA Workforce Relations Division may determine that union negotiations are required prior to implementing a release that has a substantial employee impact."
Quotable: "Slide 6 describes the business impact of delaying implementation of the release. This provides context to PRR participants throughout the rest of the presentation, so that it is understood if there is a legislative deadline or other business driver that would conflict with possible corrective actions."
Quotable: "No item in the PRR should only be marked “N/A” or “Not Applicable;” instead an explanation should be provided as to why a particular item does not apply."

**[39] adhorn (GitHub handle; repo description self-identifies as an AWS-experience-derived personal template, author's legal name not confirmed) - "Operational Readiness Review Template," operational-excellence repository.** practitioner. **fetched-and-verified.**
`https://github.com/adhorn/operational-excellence/blob/main/ORRtemplate.md`
Supports: Multiple candidate elements: (1) explicit worry-elicitation and risk-acceptance questions distinct from a pass/fail criteria table (what are you NOT worrying about, what will catch fire first, what did you cut to meet deadline); (2) a deliberately continuous, multi-touchpoint cadence across the whole lifecycle rather than a single trigger for re-review (design time, ongoing development workshops, pre-launch gate, after major changes, annual cadence); (3) a standing 'Organizational Learning' section inside the readiness document itself, covering blameless post-incident review and cross-team sharing mechanisms, not just a follow-up action; (4) explicit instruction to diversify reviewer composition to counter confirmation bias; (5) 'normalization of deviance' probes asking what degraded behavior the team has started accepting as normal; (6) an explicit named exclusion telling the reader what this document deliberately does not cover (security gets its own review).
Quotable: "This is not THE template - it is A template."
Quotable: "The key is making ORR a continuous exercise rather than a one-time checklist."
Quotable: "**At the beginning of service/feature design** - Start the ORR process early so teams understand operational requirements during development, not as a last-minute surprise before launch"
Quotable: "**Periodically** (approximately once per year) - Ensure operations haven't drifted but improved over time"
Quotable: "What are you worried about?"
Quotable: "What are you NOT worrying about?"
Quotable: "What are the top three things that you believe will catch fire first?"
Quotable: "What features did you cut to meet your deadline?"
Quotable: "The more diversity, the better. We want to avoid confirmation bias and surface different perspectives on how the system might behave."
Quotable: "_NOTE: Security must have its own, in-depth, review._"
Quotable: "What system behaviors have you started accepting as 'okay' that weren't happening 6 months ago?"
Quotable: "How do you conduct blameless post-incident reviews that focus on learning?"
Quotable: "What forums exist for sharing near-miss stories and surprising system behaviors across teams?"
Quotable: "When did you last execute each runbook end-to-end?"
