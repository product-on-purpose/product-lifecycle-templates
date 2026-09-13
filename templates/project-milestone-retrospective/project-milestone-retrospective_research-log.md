# project-milestone-retrospective: research log

Research conducted 2026-09-12 across six dimensions (origins and admission, structure, methodology lineage,
debates and status, relationships and tooling, and the standing gap question). **93 source records merged to
80 unique sources**, of which **63 fetched-and-verified**, 8 url-confirmed-not-read and 9 not-retrieved. Only
`fetched-and-verified` sources are quoted anywhere in this bundle.

**One research pass covered two candidate types, and only one of them ships.** The pass was designed to
serve both `project-milestone-retrospective` and `pi-release-retrospective`, because they share almost their
whole source base. The second **failed** ADR 0030's admission test and does not ship; the evidence for that
refusal is preserved in this log rather than discarded, because the boundary between the two is one of this
bundle's teaching points. See
[`pi-release-retrospective-admission-evidence.md`](../../docs/internal/pi-release-retrospective-admission-evidence.md).

---

## Admission, and why this one is unusually well founded

**ADMITTED, by two independent named-source lineages.** This is the strongest admission any Tier-2 candidate
in this library has had, and it is worth contrasting with the bundle built the day before: `spike-report` was
admitted on **one** source against its own canon, under
[ADR 0048](../../docs/internal/decisions/0048-one-named-source-clears-the-admission-test.md). This type
needed no such ruling.

1. **The Center for Army Lessons Learned (CALL)**, the US Army's own lessons-learned proponent, publishes it
   as a written document and names it separately from the discussion: *"After action review: A verbal,
   professional discussion..."* against *"After action report: A **written report** that is typically
   submitted after a training, combat operation, or other mission that normally documents a unit's actions
   for historical purposes but also provides key observations and LL."* It ships a formal template whose two
   stated purposes are historical documentation and Army-wide dissemination.
2. **PMI**, via the PMBOK Guide Sixth Edition, lists **"Lessons learned register"** as the named output of
   process 4.4 Manage Project Knowledge, and the register recurs as a named input across roughly a dozen
   other processes. Retrieved from a freely published PMI errata PDF on pmi.org, not inferred from a
   consultancy blog.

**The caveat that matters, and it inverts an assumption.** The obvious strongest source is the Army's
foundational **TC 25-20 (1993)**, and it is the **weaker** one: it defines the AAR as a *verbal* discussion
(*"An AAR is not a critique"*) and prescribes a written record only for the observer's own preparation
notes, not for the session's output. The written-report admission comes from CALL's later, more explicit
doctrine. Anyone citing "the Army mandates a written AAR" to TC 25-20 is citing the wrong document.

**Time-bound, and flagged for the next reader.** The PMBOK Guide's **Eighth Edition** restructured around
principles rather than named ITTO artifacts, and its freely published table of contents contains no
"Lessons Learned" heading at all. Whether the register survives **by that name** in the current edition
could not be confirmed: the full 8th-edition text is paywalled and was not read. This bundle therefore cites
the Sixth Edition for the artifact and says so.

---

## Claims flagged contested or time-bound

**The central finding, and it is narrower and more useful than the obvious version.** Every
fetched-and-verified source that criticises lessons-learned practice criticises **a specific pattern** - an
inert repository, or minutes that get filed and never consulted - **and not the act of writing**. Every one
of those critics still recommends writing something down; their fix is always a *different kind of
document*, never "stop documenting". **The discriminator is whether retrieval is wired into someone's
workflow** (a kickoff presentation, a deliverable-specific checklist, a mandatory field) rather than dumped
into a general archive nobody has a reason to open.

**So the honest framing is anti-deposit-and-forget, not anti-documentation**, and a bundle that reported
"retrospective documents are widely criticised" without that distinction would be overstating its own
sources.

**Two peer-reviewed findings pull in opposite directions, and both are kept.**

- **Dingsøyr et al. (2018)** find the document can be *actively harmful*: publishing retrospective minutes
  may cause participants to tone down or remove real critique before it is ever written. That is a genuine
  "the document damages the practice" result, not merely "the document is inert".
- **Anandayuvaraj et al. (2026)**, at a DLR/NASA JPL-affiliated site, find the opposite failure at a
  different organisation: elite aerospace engineers explicitly **want** a lessons-learned database, do not
  have one, and knowledge dies with staff turnover.

Both are cited. A bundle that carried only the first would be arguing against its own artifact; one that
carried only the second would be ignoring a real harm.

---

## Notes for the companion

**The honest framing.** This document type is well founded in named doctrine and **widely criticised in
practice for the same reason** - not because writing is wrong, but because writing without a retrieval path
is. The companion should make "who reads this, and when" a first-class design question rather than a
courtesy.

**The load-bearing sections, and the evidence for each.** The blinded gap dimension read four real filled
documents substantially or in full (IRS Direct File After Action Report, the NAO's Emergency Services
Network report, GAO-19-25 on DOE/NNSA, and the Kubernetes 1.3 Storage SIG retrospective) and confirmed five
candidates. Three are strong enough to shape sections:

1. **Naming the audience and what happens to the document next**, which **changed the content and not just
   the cover page**. The IRS report relabelled its own findings as "opportunities" rather than "lessons"
   *because* they fed a specific pending decision. GAO-19-25 is literally a letter to a named senator. The
   NAO report ends in lettered recommendations aimed at one named body. **A naive
   what-went-well/what-did-not/actions template has no field for this**, and these documents show the answer
   changes what gets written.
2. **Quantifying the cost of what it names.** All three government sources lead with numbers before prose.
   But note the discrimination: the Kubernetes retrospective quantifies a **defect rate and a schedule
   slip**, not money. So the general pattern is *quantify something material*; quantifying in **dollars** is
   a feature of public-money accountability documents, not a universal requirement. A bundle that demanded
   currency would be overfitting to one genre.
3. **Recording a lesson that was already known and not acted on.** This appeared **specifically in the
   external-audit genre** and not in team-authored retros, which is a real limit on how far to push it.
   GAO-19-25: *"NNSA has had a long history of identifying corrective actions and declaring them
   successfully resolved, only to identify additional [problems]"*. The NAO report does it mechanically,
   citing its own 2016 report paragraph by paragraph.

**The boundary this bundle must teach, sourced.** A `sprint-retrospective-notes` looks back on a **period,
on a cadence**, at how a team worked. This document looks back on **a bounded piece of work that has
ended** - it is terminal, the team may disperse, and part of its audience was not there. That is why its
aliases are `lessons learned` and `post-project review`. An `incident-postmortem` is **event-triggered**
learning about a failure, not cadence-triggered learning about how work went.

**The negative result worth carrying.** The cadence-retrospective line - sprint and PI alike - has a
structural signature: the Scrum Guide describes the Sprint Retrospective's output as changes that *"may even
be added to the Sprint Backlog"*, and SAFe's own facilitator guide describes Inspect & Adapt's output as
improvement backlog items. **Feeds a backlog, produces no document.** The AAR and lessons-learned lineage is
different in kind, and that difference is why this type ships and `pi-release-retrospective` does not.

---

## Sources

**[1] Internal Revenue Service / U.S. Department of the Treasury - IRS Direct File Pilot Program: Filing Season 2024 After Action Report (Pub. 5969).** primary. **fetched-and-verified.**
`https://www.irs.gov/pub/irs-pdf/p5969.pdf`
Supports: Type A (project/milestone) retrospective for a completed, bounded pilot. Read cover through Section I in detail (~14 of 48 pages: Commissioner's message, executive summary, intro, pilot design/phases table).
Quotable: "The conclusion of the 2024 tax filing season marks the closure of the Direct File pilot, a year-long effort to study the interest in  -  and feasibility of  -  creating a direct e-filing system as a new option for taxpayers to file federal income tax returns." / "The cost to develop the Direct File pilot came in much lower than initial estimates. Through the end of the pilot, the total amount spent by IRS was $24.6 million, including the Report to Congress. Direct File's operational costs  -  including customer service, cloud computing and user authentication  -  were just $2.4 million." / "We have labeled these lessons opportunities, because they will help both improve the tax filing ecosystem and inform the decision about Direct File's future. We anticipate making a decision about the future of Direct File later this Spring." / "Each of the next three sections reassesses an operational challenge identified in the Report to Congress."
Contested/time-bound: Written mid-decision: IRS had not yet decided Direct File's future when this was published (decision explicitly deferred to 'later this Spring'), so this is a retrospective written to feed a pending go/no-go decision, not a closed-book account.

**[2] National Audit Office (UK) - Progress delivering the Emergency Services Network (HC 2140, Session 2017 - 2019).** primary. **fetched-and-verified.**
`https://www.nao.org.uk/wp-content/uploads/2019/05/Progress-delivering-the-Emergency-Services-Network.pdf`
Supports: Type A-adjacent: an external programme review that is explicitly a FOLLOW-UP to the auditor's own prior review of the same programme. Read cover, key facts, full Summary (paragraphs 1-22), and lettered recommendations a-d.
Quotable: "This report builds on our 2016 report on the Home Office's project to provide a new mobile communications service for the emergency services. We examined the progress made in delivering the Emergency Services Network (ESN) and the implications of the 2018 reset." / "We reported on ESN in September 2016 and concluded that the Home Office was underrating the risks to delivering ESN successfully." / "How the ESN service will be governed and managed when it is a live service is still not clear, although we identified this risk in our report in 2016. This leads to a continuing risk that users' requirements will not be met." / "To date, the Home Office's management of this critical programme has represented poor value for money."
Contested/time-bound: This is an oversight-body audit of a still-live, troubled programme, not a self-authored team retrospective  -  its content (external recommendations, a value-for-money verdict) reflects that genre position and may not generalize to team-written retros.

**[3] U.S. Government Accountability Office - Project Management: DOE and NNSA Should Improve Their Lessons-Learned Process for Capital Asset Projects (GAO-19-25).** primary. **fetched-and-verified.**
`https://www.gao.gov/assets/gao-19-25.pdf`
Supports: A meta-level review of an organization's lessons-learned PROCESS across capital projects, using a terminated project (MOX) as the driving case. Read Highlights, TOC, the addressed letter and background (pp.1-3), the staffing/oversight history (pp.24-26), and the lessons-documentation findings (pp.33-35).
Quotable: "As we found in April 2015, NNSA has had a long history of identifying corrective actions and declaring them successfully resolved, only to identify additional" / "We have also found that relying on person-to-person discussions to share lessons learned can be problematic because personal networks can dissolve - for example, through attrition or retirement - and informal information sharing does not ensure everyone is benefiting from the lessons that are gleaned." / "DOE Order 413.3B's requirements for project management lessons learned do not require that all lessons learned be submitted routinely or in a timely manner... Consequently, DOE and NNSA staff are not required to submit lessons learned during the CD-0, CD-1, and CD-2 phases of a project. These earlier phases, which involve upfront planning and design for the selected project, often occur many years before the approval and start of construction." / "GAO is making three recommendations, including that DOE and NNSA develop requirements for defining how and where project management lessons learned for capital asset projects should be documented and shared routinely and in a timely manner, and for evaluating the effectiveness of corrective actions taken in response to lessons learned."

**[4] Kubernetes Storage SIG (Brad Childs, Michael Rubin, et al.) - Kubernetes 1.3 Storage Retrospective.** practitioner. **fetched-and-verified.**
`https://github.com/kubernetes/community/tree/main/sig-storage/1.3-retrospective`
Supports: A real, filled, team-authored engineering retrospective for one release cycle of one component (borderline Type A / small-scale Type B: bounded, but sits inside a recurring release cadence). Full document text retrieved and read.
Quotable: "This document is intended to chronicle the decisions made by the Storage SIG near the end of the Kubernetes 1.3 release with the storage stack that were not well understood by the wider community. This document should explain those decisions, why the SIG made the exception, detail the impact, and offer lessons learned for the future." / "Near the end of 1.3 development, on May 13, 2016, approximately one week prior to code freeze, a key engineer for this effort left the project." / "In the decision to move forward with coding beyond code freeze, not enough thought was invested in what could go wrong or how to mitigate that." / "The Storage SIG decisions were not advertised widely enough outside of the SIG early on."
Contested/time-bound: Single-SIG account of a release, not a cross-team synthesis  -  evidence for Type B (breadth across many teams in one cadence) is weaker than for Type A.

**[5] 18F / U.S. General Services Administration - 18F practices in action (spoiler: this stuff works).** primary. **not-retrieved.**
`https://18f.gsa.gov/2024/04/03/18f-practices-in-action/`
Supports: Candidate Type A retrospective on a completed government digital project (CISA .gov registry); found via search but could not be fetched (persistent DNS resolution failure against 18f.gsa.gov from the fetch tool). Not used for any claim.

**[6] Columbia Accident Investigation Board (NASA-commissioned, independent) - Columbia Accident Investigation Board Report, Volume I.** primary. **url-confirmed-not-read.**
`https://s3.amazonaws.com/akamai.netstorage/anon.nasa-global/CAIB/CAIB_lowres_full.pdf`
Supports: Widely-cited canonical case for the 'repeat lesson / normalization of deviance' candidate (foam-strike risk documented on 65 of 79 prior missions and normalized rather than acted on). URL located and confirmed to exist; content described only via WebSearch synthesis, not independently read, so no claim here rests on it alone  -  the GAO-19-25 and NAO findings (both fetched-and-verified) carry that finding instead.

**[7] Maximilian von Zedtwitz, R&D Management (2002) - Organizational learning through post-project reviews in R&D.** academic. **not-retrieved.**
`https://onlinelibrary.wiley.com/doi/abs/10.1111/1467-9310.00258`
Supports: Peer-reviewed study (27 R&D-manager interviews, 1997-2001) reportedly finding that most post-project reviews 'focus mostly on technical output and bureaucratic measurements; process-related factors such as project management are rarely discussed'  -  a named-camp signal for the 'process vs technical-output' gap. Both the publisher page and an academia.edu mirror returned HTTP 403; content is from WebSearch synthesis only, not verified firsthand, and no finding here is asserted on its authority alone.

**[8] NASA - NASA Lessons Learned Information System, entry 6856.** primary. **not-retrieved.**
`https://llis.nasa.gov/lesson/6856`
Supports: Candidate example of an atomic 'lesson record' format (as distinct from a full retrospective narrative); page requires JS rendering the fetch tool could not execute, so no content was retrieved.

**[9] US Army, Headquarters Department of the Army (Training Circular) - TC 25-20: A Leader's Guide to After-Action Reviews.** standards. **fetched-and-verified.**
`https://nick.groenen.me/attachments/public/gitignored/TC%2025-20%20A%20Leader's%20Guide%20to%20After-Action%20Reviews.pdf`
Supports: Establishes that the foundational 1993 Army AAR doctrine defines the AAR itself as a VERBAL discussion, explicitly not a critique, and does not itself prescribe a written retrospective report as the session's output artifact. The only 'written record' it mandates is the observer/controller's private prep notes taken before the session, not a published retrospective document.
Quotable: "An AAR is a dynamic, candid, professional discussion of training which focuses on unit performance against the Army standard for the tasks being trained." / "An AAR is not a critique. No one, regardless of rank, position, or strength of personality, has all of the information or answers." / "He should keep an accurate written record of what he sees and hears and record events, actions, and observations by time sequence to prevent loss of valuable information and feedback. He can use any recording system (notebook, prepared forms, 3-by-5 cards) that fits his needs"
Contested/time-bound: 1993 training circular; content on written products is thin/implicit here, superseded in practice by later CALL and TC 7-0.1 doctrine which is more explicit about a separate written AAR report.

**[10] Center for Army Lessons Learned (CALL), US Army, June 2011 - CALL Handbook 11-33: Establishing a Lessons Learned Program  -  Appendix C: Military After Action Reports/Reviews.** standards. **fetched-and-verified.**
`https://www.globalsecurity.org/military/library/report/call/call_11-33-appc.htm`
Supports: ADMISSION EVIDENCE for Project/Milestone Retrospective: CALL, the Army's own lessons-learned proponent organization, explicitly names two distinct forms of 'AAR'  -  a verbal review and a WRITTEN REPORT  -  and gives a formal written-AAR template (Figure C-2: cover page, classification, mission overview, phases, appendices) whose two stated purposes are historical documentation and disseminating lessons learned Army-wide.
Quotable: "After action review: A verbal, professional discussion of a unit's actions that typically occurs immediately after a training event, combat operation, or other mission..." / "After action report: A written report that is typically submitted after a training, combat operation, or other mission that normally documents a unit's actions for historical purposes but also provides key observations and LL." / "Written After Action Report Format The template below (Figure C-2) serves as an excellent guide to what a commander may elect to cover in his unit's written AAR... The format is flexible; however, two key purposes of the written AAR should be to (1) document the operations conducted by the unit for historical purposes and (2) provide best practices and lessons in the observation-discussion-recommendation format that can be used to inform the Army's LL program"

**[11] Project Management Institute (PMI), September 2017 - PMI Lexicon of Project Management Terms, Version 3.2.** standards. **fetched-and-verified.**
`https://vets2pm.com/wp-content/uploads/2024/10/pmi-lexicon-pm-terms.pdf`
Supports: PMI's own free ~200-term glossary defines 'Lessons Learned' only as knowledge/experience, NOT as a named document, and has no 'Lessons Learned Register' entry  -  even though it defines the structurally analogous 'Risk Register' as a document. Read here via a third-party mirror hosting the identical, verbatim PMI-copyrighted PDF, because PMI's own URL for this exact file (pmi.org/-/media/pmi/documents/registered/...) returned HTTP 403 in this session (a 'registered'/login-gated PMI path). Content authenticity verified from the document's own PMI copyright/preface page.
Quotable: "Lessons Learned. The knowledge gained during a project which shows how project events were addressed or should be addressed in the future for the purpose of improving future performance." / "Risk Register. A repository in which outputs of risk management processes are recorded."
Contested/time-bound: This is the free PMI Lexicon (curated 'foundational terms' list, per its own preface, not exhaustive of every PMBOK-defined document)  -  its silence on 'Lessons Learned Register' does not by itself refute the PMBOK Guide defining that register elsewhere (see PMBOK 6th Ed. Errata below). A PMI Lexicon v5.0 (Jan 2026) exists at pmi.org but was not retrieved (403).

**[12] Project Management Institute (PMI) - A Guide to the Project Management Body of Knowledge (PMBOK Guide)  -  Sixth Edition, Errata (3rd Printing).** standards. **fetched-and-verified.**
`https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-6th-errata.pdf`
Supports: DECISIVE ADMISSION EVIDENCE for Project/Milestone Retrospective (Lessons Learned lineage): this is PMI's own freely published (no login/paywall) corrected-page reprint of the PMBOK Guide Sixth Edition, fetched directly from pmi.org. It reproduces Figure 4-8 'Manage Project Knowledge: Inputs, Tools & Techniques, and Outputs' verbatim, listing 'Lessons learned register' as the process's #1 named OUTPUT document, and shows it recurring as an input project document across nearly a dozen other PMBOK processes (Collect Requirements, schedule processes, risk processes, etc.).
Quotable: "4.4 MANAGE PROJECT KNOWLEDGE ... Outputs .1 Lessons learned register .2 Project management plan updates  -  Any component .3 Organizational process assets updates" / "Figure 4-8. Manage Project Knowledge: Inputs, Tools & Techniques, and Outputs" / "Project documents • Lessons learned register • Project team assignments • Resource breakdown structure • Stakeholder register"
Contested/time-bound: This is the 6th Edition (2017) process-based structure. The PMBOK Guide 8th Edition table of contents (also pmi.org, fetched-and-verified, no 'lessons learned' text found in the ToC) shows PMI has since moved to a principles-based structure that does not surface named process-output documents like this in its ToC  -  so whether 'Lessons Learned Register' survives as a named artifact in the current (8th) edition could not be confirmed from freely available material; the full 8th Edition body is paywalled and was not read.

**[13] Project Management Institute (PMI) - PMBOK Guide, Eighth Edition  -  Table of Contents.** standards. **fetched-and-verified.**
`https://www.pmi.org/-/media/pmi/documents/public/pdf/publications/pmbok-guide-eighth-edition_table-of-contents.pdf`
Supports: Confirms the PMBOK Guide has moved away from the 6th Edition's named-artifact/ITTO structure; no 'Lessons Learned' heading appears in the current edition's table of contents. Read only as a negative check (absence in ToC), not as proof the concept was dropped, since full text is paywalled.

**[14] Published by Project Management Institute (PMI) Learning Library; individually authored practitioner paper - "Lessons Learned  -  Do it Early, Do it Often" (PMI conference paper).** practitioner. **fetched-and-verified.**
`https://www.pmi.org/learning/library/lessons-learned-early-often-6746`
Supports: Corroborating context: shows PMI's own library hosting practitioner literature that (as of PMBOK 4th Ed., 2008) treated lessons learned only as a closing-process activity, not yet a named living register  -  consistent with the 'Lessons Learned Register' being a 6th-Edition (2017) addition.
Quotable: "The PMBOK® Guide (Project Management Institute, 2008) states that lessons learned can be collected at any time during the project and identifies the process specifically in the closing process at the end of the project phases and reviewed during planning."

**[15] Scaled Agile, Inc. - SAFe Inspect and Adapt  -  Facilitator's Guide.** vendor. **fetched-and-verified.**
`https://framework.scaledagile.com/wp-content/uploads/2026/03/SAFe-Inspect-and-Adapt-Facilitators-Guide.pdf`
Supports: DECISIVE evidence for PI/Release Retrospective: Scaled Agile's own official, freely downloadable (no login gate) facilitator guide states the I&A event's outcomes are (1) an accountability-loop assessment/predictability score, (2) an understanding of where the ART needs to improve, and (3) 'a set of improvement backlog items (Enablers, Features, or Stories) that go into the ART Backlog.' No written retrospective report, record, or narrative document is named anywhere in the 4-page guide (purpose, agenda, prep checklist, inputs, post-event actions all read in full).
Quotable: "A successful I&A event delivers the following: ... A set of improvement backlog items (Enablers, Features, or Stories) that go into the ART Backlog for consideration in the next PI Planning event." / "The Inspect and Adapt (I&A) is a significant event held at the end of each PI, where the current state of the Solution is demonstrated and evaluated. It engages all ART stakeholders alongside the Agile Teams in reflecting on progress and identifying systemic improvement backlog items." / "Inputs: Integrated Solution Demonstration, PI Objectives (Planned vs. Actual Business Value), ART Performance Metrics (e.g., Flow Metrics, Predictability Measure), and a list of proposed problem statements."

**[16] Scaled Agile, Inc. - Inspect and Adapt  -  Scaled Agile Framework (main article page).** vendor. **fetched-and-verified.**
`https://framework.scaledagile.com/Inspect-and-Adapt/`
Supports: Confirms the framework's own site marks the deep-dive body of this article as gated: its embedded schema.org metadata explicitly sets 'isAccessibleForFree': false around the full article body (only the short definition/summary/key-takeaways are open), with a visible 'Login' / 'Other ways to access' prompt for the rest. The freely visible summary matches the Facilitator's Guide: output is 'improvement backlog items,' not a document.
Quotable: "The Inspect and Adapt (I&A) is a significant event held at the end of each PI, where the current state of the Solution is demonstrated and evaluated. Teams then reflect and identify improvement backlog items via a structured problem-solving workshop." / "'isAccessibleForFree': false"
Contested/time-bound: Some deeper how-to detail on this specific page is behind a SAFe Studio login and was not read; the free Facilitator's Guide PDF above was used as the fuller primary source instead.

**[17] Ken Schwaber and Jeff Sutherland - The Scrum Guide  -  The Definitive Guide to Scrum: The Rules of the Game (November 2020).** primary. **fetched-and-verified.**
`https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf`
Supports: Boundary evidence versus the already-built, out-of-scope Sprint Retrospective: the Scrum Guide itself (the originating authors' own document) describes the Sprint Retrospective's output the same way SAFe describes I&A's  -  as backlog items, not a written record. This shows the 'backlog items, no document' pattern is shared across the whole Scrum/SAFe cadence-retrospective family, at both the team-sprint and ART-PI scales, and is NOT specific to SAFe.
Quotable: "The Scrum Team identifies the most helpful changes to improve its effectiveness. The most impactful improvements are addressed as soon as possible. They may even be added to the Sprint Backlog for the next Sprint." / "The Sprint Retrospective concludes the Sprint. It is timeboxed to a maximum of three hours for a one-month Sprint."

**[18] Norman L. Kerth / Dorset House, via Pearson/InformIT - Project Retrospectives: A Handbook for Team Reviews (free sample: front matter, Ch.3 in full, TOC, Index).** primary. **fetched-and-verified.**
`https://ptgmedia.pearsoncmg.com/images/9780133488579/samplepages/0133488578.pdf`
Supports: Founding primary text for the project-retrospective document type: terminal/team-disperses rationale, incomplete-shared-memory rationale, 3-day duration and 1-3-week-post-project timing (vs. a sprint retro's timebox), and the book's own two-tier Report/Secure-Location structure. NOTE: only front matter, Chapter 3 in full, the table of contents, and the index were actually present in this 49-page sample file and read; Chapters 7 and 10 are known to exist and their section titles were read from the TOC/Index, but their body content was NOT in the file and is not quoted.
Quotable: "this ritual, called by many names - postmortem or postpartum, for example, or, my preference, retrospective - is important to our practice of software" / "the collective team wisdom acquired during the previous project is likely to be lost as individuals are scattered across the organization to support new undertakings. If, at the end of a project, the collective wisdom is discussed and documented, it becomes knowledge that survives the breakup of the team." / "no one person knows all the stories, and no one person knows how the pieces fit together to tell the tale of the entire project" / "Simply stated, effective retrospectives require about three days."

**[19] Scaled Agile, Inc. - Iteration Retrospective (official SAFe extended guidance page).** primary. **fetched-and-verified.**
`https://framework.scaledagile.com/iteration-retrospective`
Supports: Confirms SAFe treats the team-level iteration retrospective as a distinct event from PI-level I&A, and roots it in the Agile Manifesto rather than citing Kerth or Derby/Larsen by name.
Quotable: "a regular event held at the end of each iteration during which Agile Teams review their results to identify improvements for future work" / "a distinct event, separate from the Team Review"

**[20] PRINCE2 Wiki (third-party community wiki describing the AXELOS/PeopleCert PRINCE2 standard) - Lessons Report.** reference. **fetched-and-verified.**
`https://prince2.wiki/management-products/reports/lessons-report/`
Supports: Describes PRINCE2's terminal, per-occasion Lessons Report as distinct from its continuous Lessons Log - one leg of the register/report triangulation. Not the official AXELOS text (paywalled, not read).
Quotable: "the project manager produces a lessons report using information from the lessons log. This report is shared with the project board and is designed to help future projects avoid common mistakes and replicate successful practices"

**[21] prince2.wiki (third-party practitioner reference site; describes AXELOS's PRINCE2 method) - Lessons log (PRINCE2 management product).** reference. **fetched-and-verified.**
`https://prince2.wiki/management-products/project-log/lessons-log/`
Supports: TYPE A discriminator on owner/date. Lessons Log fields as described: unique identifier, lesson/recommendation, type, priority, date recorded, relevant stage, lesson status  -  explicitly NO owner field (project manager maintains the log, but individual lessons aren't assigned to a person).
Quotable: "a repository for lessons that may benefit current and future projects" / "The document does not specify an 'owner' field."
Contested/time-bound: AXELOS's own PRINCE2 manual and official templates (publications.axelos.com, axelos.com/resource-hub) are paywalled/membership-gated  -  every direct attempt returned 403. This wiki is a third-party reproduction; PRINCE2's own wording is url-confirmed-not-read, not fetched-and-verified.

**[22] BrainSensei (PMP/CAPM exam-prep training company, describing PMBOK) - Mastering the Lessons Learned Register for PMP and CAPM Exams.** vendor. **fetched-and-verified.**
`https://brainsensei.com/mastering-the-lessons-learned-register/`
Supports: PMBOK-derived register (project-level, continuous) vs. repository (organizational, closure-transferred) distinction - independent naming convention converging on the same shape as PRINCE2's log/report split. Not PMI's own text (PMBOK is paywalled; pmi.org itself returned 403 and was not read).
Quotable: "Project-level documentation, updated throughout the project or phase, used primarily by the immediate team to make timely adjustments." / "An organizational repository, updated at project or phase closure, accessible to future teams and stakeholders."

**[23] Atlassian (Confluence) - Retrospective Blueprint documentation.** vendor. **fetched-and-verified.**
`https://confluence.atlassian.com/doc/retrospective-blueprint-427623496.html`
Supports: The one tool surveyed whose native retrospective artifact is explicitly a persisted wiki page rather than a board, and which auto-generates an index page across occasions - the strongest tooling evidence for a document-shaped retrospective, though it does not itself distinguish sprint from project/PI scope.
Quotable: "Retrospective pages help you track team successes and opportunities after projects or at the end of a sprint." / "The first time you create a retrospective page in a space, Confluence will automatically create an 'index' page, which will list all retrospectives in the space."

**[24] Atlassian Community (named forum participants, e.g. Bill Sheboy, Nikola Perisic) - Community thread: "Retrospective board - Jira".** practitioner. **fetched-and-verified.**
`https://community.atlassian.com/forums/Jira-questions/Retrospective-board/qaq-p/2628537`
Supports: Confirms Jira (core/Software product) has no native retrospective feature; teams repurpose a Kanban board, use an external whiteboard tool, or install a marketplace plugin instead.
Quotable: "Has anyone set up a retrospective board in Jira without a plugin?" / "try a whiteboard, sticky notes, and conversation"

**[25] Microsoft (Azure DevOps / Microsoft Garage) - vsts-extension-retrospectives README.** vendor. **fetched-and-verified.**
`https://github.com/microsoft/vsts-extension-retrospectives/blob/main/README.md`
Supports: Azure DevOps's dedicated retro tool is a persistent feedback board with history/archive that turns feedback into work items and offers only an in-app summary view, not a standalone exportable document.
Quotable: "Retrospectives is an Azure DevOps extension to perform smart and efficient retrospectives from within the Azure DevOps."

**[26] EasyRetro - The Project Post-Mortem Retrospective Template.** vendor. **fetched-and-verified.**
`https://easyretro.io/templates/post-mortem-retrospective/`
Supports: A dedicated retro tool's own vocabulary reserves 'post-mortem' for the once-only, full-roadmap project occasion versus the repeating sprint retrospective - confirmed identically word-for-word across two independent fetches.
Quotable: "sprint retrospectives take place multiple times at a regular cadence throughout the course of a project. But the project post-mortem only takes place once." / "The scope of a project post-mortem is a bit more all-encompassing too, covering the entire project roadmap from start to finish."

**[27] EasyRetro - Release Retrospective Template.** vendor. **fetched-and-verified.**
`https://easyretro.io/templates/release-retrospective/`
Supports: Shows vendor tooling's 'release retrospective' as a single-team, project-scoped, one-time occasion, NOT a multi-team ART-scale event - contrasts with SAFe's breadth-based definition of the PI retrospective.
Quotable: "A Release Retrospective is a critical event because it captures all the lessons learned and improvements made during the project." / "Document findings to make an action plan - improvements needed for future releases."

**[28] EasyRetro - Project Retrospective Template Template.** vendor. **fetched-and-verified.**
`https://easyretro.io/templates/project-retrospective-template/`
Supports: Confirms the delivered artifact is a three-column board (What worked? / What needs improvement? / Actions), not a formal document, despite marketing language elsewhere describing 'documenting' findings.
Quotable: "A Project Retrospective meeting serves the purpose of reviewing a completed project and learning from both successes and shortcomings to improve future projects."

**[29] EasyRetro - Retrospective Templates (100+ Free Sprint Retrospective Formats).** vendor. **fetched-and-verified.**
`https://easyretro.io/retrospective-templates/`
Supports: General confirmation that EasyRetro frames its product as boards ('start your free retrospective board in seconds') with no built-in document-export path described.
Quotable: "start your free retrospective board in seconds"

**[30] Parabol (company blog) - Post-mortems vs Retrospectives: What's the Difference.** vendor. **fetched-and-verified.**
`https://www.parabol.co/blog/retrospectives-vs-post-mortems/`
Supports: Names a purpose/audience-based boundary against the incident postmortem (causation/leadership-facing vs. ongoing/team-facing) and references 'lessons learned meetings' and 'after-action reviews' as adjacent, related formats without merging them into retrospectives.
Quotable: "Post-mortems attempt to understand what went wrong" / "Retrospectives, on the other hand, primarily engage and serve the team doing the work."

**[31] TeamRetro (company blog) - Sprint retrospective vs. release retrospective.** vendor. **fetched-and-verified.**
`https://www.teamretro.com/blog/sprint-retrospective-vs-release-retrospective/`
Supports: Explicit vendor-sourced boundary against the sprint retrospective on scope, cadence and strategic-vs-tactical framing - directly answers the sprint-boundary ask, though it treats 'release retrospective' as one team's longer-cadence retro, not an ART-scale event.
Quotable: "Sprint retrospectives are tactical. They emphasize short-term process improvements, collaboration, and delivery within a sprint cycle." / "Release retrospectives are strategic. They look at the broader picture, including the product's success, alignment with business goals, and long-term process improvements." / "Scope: Sprint Retrospective focuses on a single sprint (1-4 weeks); Release Retrospective focuses on the entire release cycle (multiple sprints)."

**[32] Jonathan Hall (jhall.io) - Retrospectives or Postmortems?.** practitioner. **fetched-and-verified.**
`https://jhall.io/archive/2021/07/31/retrospectives-or-postmortems/`
Supports: Named individual practitioner distinguishing the two by purpose and event-vs-cadence trigger, and explicitly framing them as complementary rather than a confusable pair - cuts against any 'common error to conflate them' claim.
Quotable: "Retrospectives exist to encourage regular retrospection, whereas postmortems serve to understand root causes of incidents and prevent future reoccurences."

**[33] FireHydrant (company blog) - What are Blameless Retrospectives? How Do You Run Them?.** vendor. **fetched-and-verified.**
`https://firehydrant.com/blog/what-are-blameless-retrospectives-do-they-work-how/`
Supports: A named incident-management vendor splits the single word 'retrospective' into an incident-triggered type and a post-project type - live counterexample to a clean retrospective/postmortem vocabulary split.
Quotable: "The first type of retrospective meeting is held after a DevOps or IT incident such as data corruption or website crash." / "The second type of retrospective takes place after project completion where the team looks at the project from the start to the end to determine what went smoothly and what can be improved."

**[34] Honeycomb (company engineering blog) - The Incident Retrospective Ground Rules.** practitioner. **fetched-and-verified.**
`https://www.honeycomb.io/blog/incident-retrospective-ground-rules`
Supports: A named organization uses 'retrospective'/'incident review' for its incident process, never 'postmortem,' and prefers 'blame-aware' to 'blameless' - further evidence the industry vocabulary split is unsettled.
Quotable: "We're going for blame-aware incident reviews; we are here to assume people wanted to do a good job"

**[35] Goodreads (community book database, describing the primary work by Esther Derby and Diana Larsen) - Agile Retrospectives: Making Good Teams Great - book page.** reference. **fetched-and-verified.**
`https://www.goodreads.com/book/show/721338.Agile_Retrospectives`
Supports: Confirms the book's own chapter-level table of contents gives 'Releases and project retrospectives' a distinct chapter (9), separate from the iteration-level activity chapters (4-8) - evidence release/project retrospectives are an occasion-class of their own in the founding practitioner text, not a bigger size of one document. Chapter body itself was not read (O'Reilly preview 403'd).
Quotable: "Releases and project retrospectives"

**[36] Parabol - Templates.** vendor. **fetched-and-verified.**
`https://www.parabol.co/templates`
Supports: A dedicated retro tool's own navigation files 'Lessons Learned' and 'Post Mortems' as named templates under 'Project management,' alongside its ordinary sprint retro templates - the project-retrospective alias survives in the board-tool world as a template/menu choice, not as a distinct document artifact.
Quotable: "Lessons Learned" / "Post Mortems"

**[37] Jira Align Help Center (Atlassian) - Inspect and adapt for SAFe.** vendor. **url-confirmed-not-read.**
`https://help.jiraalign.com/hc/en-us/articles/115004289273-Inspect-and-adapt-for-SAFe`
Supports: Existence only; page returned HTTP 403 on direct fetch. A WebSearch synthesis (not a page-body read) suggested its wording largely mirrors SAFe's own framework language rather than defining a distinct Jira Align PI-retrospective artifact - not asserted as fact, and no quote is used from it.

**[38] Project Management Institute - A Guide to Project Management Body of Knowledge (PMBOK Guide).** standards. **not-retrieved.**
`https://www.pmi.org/`
Supports: Not accessed - paywalled. All PMBOK-derived register/repository claims in this report rest on a secondary training-company summary (BrainSensei), not PMI's own text; pmi.org's own library article also returned HTTP 403 and was not read.

**[39] AXELOS / PeopleCert - Managing Successful Projects with PRINCE2 (official manual).** standards. **not-retrieved.**
`https://www.prince2.com/`
Supports: Not accessed - paywalled per the task's own caution about paywalled standards. All PRINCE2 content in this report comes from prince2.wiki, a third-party community wiki, not the official manual.

**[40] Esther Derby and Diana Larsen / O'Reilly - Agile Retrospectives: Making Good Teams Great, Chapter 9 preview.** primary. **url-confirmed-not-read.**
`https://www.oreilly.com/library/view/agile-retrospectives/9781680500295/f_0060.html`
Supports: Existence and title of Chapter 9 ('Releases and Project Retrospectives') confirmed via Goodreads' TOC; the chapter's own content on how it defines/distinguishes release vs. project retrospectives was NOT read (403) and no claim rests on it beyond the title.

**[41] Retrium (press page) - How to Lead a Successful Project Retrospective Meeting.** vendor. **url-confirmed-not-read.**
`https://www.retrium.com/press/how-to-lead-a-successful-project-retrospective-meeting`
Supports: Fetch returned only navigation/promotional shell, not the article body. Confirms only that Retrium markets a 'project retrospective' as a named category; no content claim rests on it.

**[42] Esther Derby and Diana Larsen (The Pragmatic Bookshelf, 2006) - Agile Retrospectives: Making Good Teams Great (full text: front matter, Preface, Introduction, Ch.1, Ch.3 excerpt, Ch.9, Bibliography).** primary. **fetched-and-verified.**
`https://agile.2ia.net/Agile%20Retrospectives.pdf`
Supports: Confirms the five-stage structure (Set the Stage/Gather Data/Generate Insights/Decide What to Do/Close), that it describes a facilitated session (not a document), that the book's default scope is iteration-level (1 week-1 month), and that Ch.9 explicitly and separately treats 'Releases and Project Retrospectives' as wider-scope/cross-organizational, citing Kerth directly [Ker01] twice. This is the single most important source for the core research question.
Quotable: "When we say retrospective, here's what we have in mind: a special meeting where the team gathers after completing an increment of work to inspect and adapt their methods and teamwork." / "And, in contrast to traditional postmortems or project reviews, retrospectives focus not only on the development process, but on the team and team issues." / "Our main focus in this book is short retrospectives - retrospectives that occur after one week to one month of work." / "It may seem silly to gather data for an iteration that lasted a week or two."
Contested/time-bound: Hosted at a third-party PDF mirror, not the official publisher; content cross-verified against the legitimate Agile Alliance and Pragmatic Bookshelf pages below, which independently corroborate the 'post-mortems...too late to help' framing and the Kerth co-founding fact.

**[43] retrospectivewiki.org (community-maintained) - The Prime Directive (Agile Retrospective Resource Wiki).** reference. **fetched-and-verified.**
`https://retrospectivewiki.org/index.php?title=The_Prime_Directive`
Supports: Gives the exact wording of the Prime Directive with attribution to Kerth's book; used because the legitimate Kerth sample PDF did not include p.7 itself.
Quotable: "Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand."

**[44] Agile Alliance - Agile Retrospectives: Making Good Teams Great! (book resource page).** practitioner. **fetched-and-verified.**
`https://agilealliance.org/resources/books/agile-retrospectives-making-good-teams-great/`
Supports: Independently corroborates the book's own framing of 'post-mortems' as 'only held at the end of the project - too late to help,' matching what I read directly in the book's Preface.
Quotable: "retrospectives (also known as 'post-mortems') are only held at the end of the project - too late to help"

**[45] The Pragmatic Bookshelf / Esther Derby, Diana Larsen - Agile Retrospectives: Making Good Teams Great (publisher page).** vendor. **fetched-and-verified.**
`https://pragprog.com/titles/dlret/agile-retrospectives/`
Supports: Confirms Kerth co-founded the Retrospective Facilitators Gathering with Derby and Larsen (author bio), corroborating the lineage claim.
Quotable: "With Norm Kerth, Esther and Diana are founders of the annual Retrospective Facilitators Gathering."

**[46] Wikipedia contributors - Lessons learned (Wikipedia).** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Lessons_learned`
Supports: General, cross-domain definition of 'lessons learned' (NASA/ESA/JAXA and OECD framings); explicitly does NOT connect to PMBOK or Kerth, which is itself a finding (no bridge available here).
Quotable: "A lesson learned is knowledge or understanding gained by experience."

**[47] Torgeir Dingsøyr, Marius Mikalsen, Anniken Solem, Kathrine Vestues (SINTEF / NTNU); XP2018, Springer LNBIP vol. 314 - Learning in the Large: An Exploratory Study of Retrospectives in Large-Scale Agile Development.** academic. **fetched-and-verified.**
`https://arxiv.org/pdf/1805.10310`
Supports: Type B (PI/release-scale, multi-team). Peer-reviewed. Directly tests whether scaled retrospection produces cross-team learning: only 17/109 issues and 6/36 action items were 'large-scale' (project/other-teams) categories  -  most retrospective content, even inside a large multi-team project, stayed team-internal. Also the strongest evidence that WRITING IT DOWN can be actively harmful, not just inert.
Quotable: "A common critique of retrospectives is that teams meet and talk, but little of what is talked about is acted upon." / "Given the short time spent on retrospectives, they do not seem to facilitate 'deep' learning ('double loop' learning in Argyris and Schön's framework)." / "Having minutes public could also lead to critique being toned down or removed completely." / "We find, however, that teams mainly deal with team-internal issues in retrospectives."
Contested/time-bound: 2018 postprint (published version DOI 10.1007/978-3-319-91602-6_13); studies Scrum team-level retrospective minutes, not a SAFe I&A event specifically  -  evidence is adjacent to Type B, not a direct study of it.

**[48] Jake Calabrese, Helping Improve LLC - Lessons-Learned vs Project Retrospectives.** practitioner. **fetched-and-verified.**
`https://helpingimprove.com/lessons-learned-vs-project-retrospectives/`
Supports: Practitioner-tier characterization contrasting blame-prone, end-of-project 'lessons-learned' meetings with psychologically-safe retrospectives; cites Kerth's Prime Directive by name.
Quotable: "try telling a group of people you are scheduling a lessons-learned meeting and look for the eye-rolls!"

**[49] Marc Loeffler (Pearson/InformIT, 2018) - Improving Agile Retrospectives: Helping Teams Become More Efficient (excerpt, 'The Retrospective Phase Model').** practitioner. **fetched-and-verified.**
`https://www.informit.com/articles/article.aspx?p=2916288&seqNum=3`
Supports: Independently confirms the five (or, in Loeffler's expanded version, six) phase model is built on Derby & Larsen's original and describes it as a facilitated meeting, not a document.
Quotable: "These form the structure of a retrospective and are based on the original phase model in Esther Derby and Diana Larsen's book."

**[50] retroflow.org (retrospective-tool vendor blog) - The History of Agile Retrospectives: From Deming to Modern Sprints.** vendor. **fetched-and-verified.**
`https://www.retroflow.org/blog/post/agile-retrospective-history`
Supports: Secondary corroboration that Kerth's book addresses 'post-project reflection' while Derby & Larsen shifted the practice to 'iterative/sprint-based' retrospectives.
Quotable: "Structured approach to post-project reflection"

**[51] Google Books (publisher-sourced synopsis) - Project Retrospectives: A Handbook for Team Reviews (Google Books catalog/about page).** reference. **fetched-and-verified.**
`https://books.google.com/books/about/Project_Retrospectives.html?id=BxROAQAAIAAJ`
Supports: Independent corroboration of publisher, year (2001), page count, and a publisher-style synopsis emphasizing organizational preservation of project-end lessons.
Quotable: "project retrospectives offer organizations a formal method for preserving the valuable lessons learned from the successes and failures of every project"

**[52] Mike Griffiths and Johanna Rothman (Agile Alliance experience report, 2017) - Bridging Mindsets: Creating the PMI Agile Practice Guide.** practitioner. **fetched-and-verified.**
`https://agilealliance.org/resources/experience-reports/bridging-mindsets-creating-the-pmi-agile-practice-guide/`
Supports: Confirms PMI co-authored the 2017 Agile Practice Guide with Agile Alliance (a real bridging document between PMBOK-lineage and agile-retrospective-lineage thinking), though this report itself does not compare 'lessons learned' to 'retrospective' in depth.
Quotable: "We maintained our writing cadence and ability to pair. However, we did not successfully establish a regular cadence for retrospectives."

**[53] Project Management Institute - PMI Lexicon of Project Management Terms (Version 5.0, Jan. 2026)  -  'lessons learned register' definition.** standards. **not-retrieved.**
`https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf`
Supports: PMI's own semi-official glossary would be the best available free stand-in for PMBOK's 'lessons learned' definition, but every attempt to fetch it (two different URLs, plus the lexicon landing page) returned HTTP 403. Reported here as a documented access failure, not as a source of any verified quote.
Contested/time-bound: Search-indexed snippets (not independently verified) describe a 'Version 5.0, last updated January 2026' entry; this could not be confirmed by reading the document.

**[54] Project Management Institute - PMBOK Guide (7th ed. and lessons-learned process guidance generally).** standards. **not-retrieved.**
`https://www.pmi.org/pmbok-guide-standards/lexicon`
Supports: Named here explicitly as a NULL RESULT: the standard is paywalled/membership-gated and every PMI.org URL attempted (lexicon page, two learning-library articles) returned 403. No PMBOK sentence in this research is a verified primary quote; the organizational-memory characterization rests entirely on convergent secondary/practitioner sources, which is disclosed throughout key_findings.

**[55] Project Management Institute and Agile Alliance - PMI Agile Practice Guide (2017, co-published with Agile Alliance).** standards. **not-retrieved.**
`https://www.pmi.org/standards/agile`
Supports: Cited secondhand (via the Dingsøyr et al. 2018 academic paper's own reference list) as calling retrospectives 'the single most important practice in agile development.' I could not fetch the guide itself (ANSI preview returned 403) or the PMI standards page, so this specific characterization is flagged PLAUSIBLE/NOT CONFIRMED in contested_claims, not presented as a verified quote.

**[56] Susanne Salem-Schatz, Diana Ordin, Brian Mittman  -  VA Center for Implementation Practice and Research Support / VA Office of Quality and Performance (v1.1, Oct 2010) - Guide to the After Action Review.** practitioner. **fetched-and-verified.**
`https://cebma.org/assets/Uploads/Salem-Schatz-Guide-to-the-After-Action-Review.pdf`
Supports: TYPE A. Full 'After Action Review Report Template' read page-by-page: Background (Team/Project Name, Project/Event Reviewed, Date of Review, During/After Project Completion checkbox, Participants table with a Facilitator role, project summary) then two paired tables  -  'What went well and why?' (Successes | How to Ensure Success in the Future) and 'What can be improved and how?' (What can be improved | Recommendations)  -  with NO owner or due-date field anywhere. Explicit 'Sharing the AAR Results' step for audiences beyond the team.
Quotable: "First used by the Army on combat missions, the AAR is a structured approach for reflecting on the work of a group" / "When review was completed: ☐ During Project ☐ After Project Completion" / "Share the AAR report with your project sponsor or other appropriate leader in your facility, VISN or national VHA offices." / "The greatest benefit of an AAR comes from applying the lessons learned to future work and teams."

**[57] US Department of Energy, Office of Science - Template for Closeout Report (Project Closeout Report, v6).** primary. **fetched-and-verified.**
`https://science.osti.gov/-/media/opa/word/SC_Project_Closeout_Report_v6.docx`
Supports: TYPE A. Verified by direct extraction of word/document.xml (not tool summarization). Full TOC: 1 Executive Summary; 2 Introduction; 3 Acquisition Approach; 4 Project Organization; 5 Project Baseline at Completion (5.1 Scope Baseline...5.8 Safety Record); 6 Closeout Status; 7 Lessons Learned; 8 Photos; 9 Project Document Archives and Locations; Appendices. Cleanly separates factual baseline/closeout-status sections (6, with a dated activity table) from the narrative Lessons Learned (7, organized by topical area, no owner/date fields).
Quotable: "5.PROJECT BASELINE ... This section documents the project Performance Baseline (PB) that consists of the scope, cost (Total Project Cost or TPC), schedule (Critical Decision or CD-4 date)..." / "7. LESSONS LEARNED The section should discuss good work practices, innovative approaches, negative experiences, subcontractor performance, deviations from what was planned versus what was performed..." / "The purpose for this request is to allow other projects to use historical cost data of a completed project."

**[58] US Department of Homeland Security / FEMA, Homeland Security Exercise and Evaluation Program - After Action Report/Improvement Plan (AAR/IP) Template (HSEEP).** primary. **fetched-and-verified.**
`https://www.rac-g.org/docs/AARIP_Template.pdf`
Supports: TYPE A (bounded exercise/event, not a software project, but explicitly named 'after action report' and government-published). Full TOC read: Handling Instructions; Contents; Executive Summary (Major Strengths / Primary Areas for Improvement); Section 1 Exercise Overview (Exercise Details incl. Start/End Date, Duration, Location; Planning Team; Participating Orgs); Section 2 Exercise Design Summary; Section 3 Analysis of Capabilities (per observation: Observation [Strength/Area for Improvement] → References → Analysis → Recommendations); Section 4 Conclusion; Appendix A Improvement Plan; Appendix B Lessons Learned [Optional]; C Participant Feedback; D Events Summary Table; E Performance Ratings; F Acronyms. THIS IS THE ONE TYPE-A TEMPLATE THAT DOES GIVE ACTIONS AN OWNER AND DATES  -  but only in Appendix A's Improvement Plan Matrix, not in the AAR narrative itself.
Quotable: "Table A.1 Improvement Plan Matrix" / "Capability | Observation Title | Recommendation | Corrective Action Description | Capability Element | Primary Responsible Agency | Agency POC | Start Date | Completion Date" / "Observation 1.1: [Begin this section with a heading indicating whether the observation is a 'Strength' or an 'Area for Improvement.']"

**[59] International Telecommunication Union (ITU), ITU-D projects documentation - Post Implementation Review Template.** standards. **fetched-and-verified.**
`https://www.itu.int/en/itu-d/projects/documents/templatepostimplementationreview.pdf`
Supports: TYPE A. Full 9-section template read verbatim: 1 Executive Summary; 2 Scope of Review; 3 Results Achievement (Result|Description|KPI|Initial Target|Achieved|Remarks); 4 Financial Status; 5 Findings; 6 Lessons Learned; 7 Conclusions; 8 Recommendations; 9 Attached Documents. Cleanest example found of Scope as its own numbered section, and of Findings/Lessons/Conclusions/Recommendations kept as four separate sections. No owner/date field on Recommendations.
Quotable: "2. Scope of Review  -  The paragraph provides a clear explanation of the scope of the review." / "6. Lessons Learned ... Could these lessons be utilized as best practices in other Regions?" / "8. Recommendations ... Priorities will be identified for the implementation of recommendations"
Contested/time-bound: This is ITU's own internal project-management template, not an ITU-T Recommendation  -  tiered 'standards' for the organisation, not for this specific document's formal status.

**[60] UK Government Digital Service (GDS), GOV.UK - Agile tools and techniques (Service Manual).** primary. **fetched-and-verified.**
`https://www.gov.uk/service-manual/agile-delivery/agile-tools-techniques`
Supports: Boundary evidence between SPRINT retro (out of scope) and TYPE A. Page lists 'Retrospective meetings' and 'End-of-phase retrospectives' as two DIFFERENT, separately headed items. The phase-end version is explicitly the terminal/outside-audience one.
Quotable: "usually include people who've been involved in the work from outside the team, too, like procurement or policy colleagues" / "This can help identify what could be improved in the next phase of the project" / "ONS ran an end-of-phase retro"

**[61] Rebecca Refoy, Ashley Owens, Omid Ghaffari-Tabrizi, Michelle McNellis  -  18F / GSA Technology Transformation Services (published 18 Mar 2020) - An Acquisition Retrospective.** practitioner. **fetched-and-verified.**
`https://18f.gsa.gov/2020/03/18/an-acquisition-retrospective/`
Supports: The ONE genuine worked/filled retrospective example found in this research (not a blank template). Notably it does NOT use any of the standard headings (no Background/Scope/Lessons-Learned/Action-Items)  -  it is organised entirely around the project's own three named aims (Healthy competition, Robust evaluation, Speed). Evidence that real published retrospective narratives often abandon template structure entirely.
Quotable: "TTS continuously iterates on our acquisition practices to incorporate lessons learned and what we have seen in previous acquisitions" / "Below are the aims that we hoped to achieve: Healthy competition ... Robust evaluation ... Speed"
Contested/time-bound: 18F was shut down by GSA in March 2025; the live URL no longer resolves (checked this session)  -  retrieved via the Wayback Machine mirror of the same page, so treat the content as historical/archival, not a currently maintained page.

**[62] prince2.wiki (third-party practitioner reference site) - End Project Report (PRINCE2 management product).** reference. **fetched-and-verified.**
`https://prince2.wiki/management-products/reports/end-project-report/`
Supports: TYPE A. The report's stated Contents (per this page) mix factual items (PM's summary, business case review, evaluation of objectives, team performance, product status) with a single 'Lessons learned' content item  -  i.e. lessons are ONE item inside a general report, not pulled into their own report the way ITU/DOE/HSEEP do it.
Quotable: "A summary of key insights that can benefit future projects."

**[63] Adrian Abramovici, PMP  -  published by Project Management Institute, PM Network, Oct 1999, 13(10):61-63 - Gathering and using lessons learned.** practitioner. **fetched-and-verified.**
`https://www.pmi.org/learning/library/gathering-using-lessons-learned-5116`
Supports: The only PMI-hosted lessons-learned content I could read in full (fetched raw HTML directly; every other PMI/PMBOK page and downloadable template returned HTTP 403). Confirms PMI's own published stance rests on facilitator process guidance and audience-segmented templates rather than one universal named-section template.
Quotable: "The template should achieve two goals: group data by areas of interest and in a standard format that allows comparison with other similar projects, and segregate data by target audiences." / "Lessons learned should be maintained on a database or on the company intranet, with access to their various parts given in accordance with the type of data they contain."
Contested/time-bound: PMI's PMBOK Guide and PMI's own downloadable 'Lessons Learned Template'/'Lessons Learned Form' (pmi.org, projectmanagement.com) are members-only  -  repeated direct fetches returned 403. We could not verify PMBOK's own section structure and have not inferred it; PMBOK content here is url-confirmed-not-read / not-retrieved, and no claim in this report rests on it.

**[64] Craig Larman & Bas Vodde  -  LeSS (Large-Scale Scrum) official framework site - Overall Retrospective.** primary. **fetched-and-verified.**
`https://less.works/less/framework/overall-retrospective`
Supports: TYPE B (scaled, cross-team) evidence: an entire named event exists solely for cross-team/organisational findings  -  the clearest 'cross-team as its own thing' evidence found, though it's whole-event framing, not a subsection within a larger single retro document.
Quotable: "Its purpose is to discuss cross-team, organizational and systemic problems within the organization." / "An Overall Retrospective is attended by the Product Owner, Scrum Masters, Team representatives, and managers (if any)."

**[65] Ken Schwaber and Scrum.org - The Nexus Guide: The Definitive Guide to Scaling Scrum with Nexus (January 2021).** primary. **fetched-and-verified.**
`https://scrumorg-website-prod.s3.amazonaws.com/drupal/2021-01/NexusGuide%202021_0.pdf`
Supports: BOUNDARY evidence, read in full (10 pages). The Nexus Sprint Retrospective is cross-team (all Scrum Teams) but runs at SPRINT cadence, not PI/release cadence  -  proof that 'cross-team' and 'PI/release-level' are independent axes, and that a cross-team retro is not automatically a Type-B PI/release retrospective.
Quotable: "The purpose of the Nexus Sprint Retrospective is to plan ways to increase quality and effectiveness across the whole Nexus." / "The Nexus Sprint Retrospective concludes the Sprint."

**[66] Aha! Labs Inc. (roadmapping software vendor) - Create a SAFe PI retrospective.** vendor. **fetched-and-verified.**
`https://www.aha.io/roadmapping/guide/templates/create/pi-retrospective`
Supports: TYPE B vendor template: 4-column board (What went well / What could have been better / What you will do differently / Action items with owners) plus a shoutouts section. Only Type-B source besides SAFe's own that puts an explicit owner on actions; still no due-date field.
Quotable: "Action items with owners" / "a shoutouts section"

**[67] Smartsheet Inc. - Free Project Management Lessons Learned Templates.** vendor. **fetched-and-verified.**
`https://www.smartsheet.com/content/lessons-learned-template`
Supports: TYPE A vendor roundup. Section list confirms the vendor-template pattern: Project Overview, Project Highlights, Project Challenges, Post-Project Tasks/Future Considerations, Planning Phase, Execution, Human Factors, Overall, Project Close Acceptance  -  and explicitly no owner/due-date fields and no reference to PMI's own framework.

**[68] ProjectManager.com (Ganttic/ProjectManager.com, PM software vendor) - Project Retrospective Template for Word.** vendor. **fetched-and-verified.**
`https://www.projectmanager.com/templates/project-retrospective-template`
Supports: TYPE A vendor template confirming the pattern again: Identify Key Project Roles; Describe Goals/Objectives; Document the Lessons Learned (three-column: what worked / what to improve / recommendations); Gather Feedback; Define the Scope Overview; Visualize Timeline; Budget Summary. No owner/due-date fields.

**[69] Government Technical Advisory Centre (GTAC), South African National Treasury - CLO4 Project Close Out Report Template.** primary. **url-confirmed-not-read.**
`https://www.gtac.gov.za/wp-content/uploads/2022/01/CLO4.Project-Close-Out-Report_Template_v5.0.doc`
Supports: Confirmed to be a real South African National Treasury PPM-toolkit template (file metadata shows author, PPM Toolkit taxonomy tags, 'Close-out' category) but I could not reliably extract the body text myself (old binary .doc format; my own extraction attempt only recovered style/metadata, not section prose), and an automated tool's earlier section-list summary of the same binary is not independently verified  -  so no section claims from this file are used in the findings.

**[70] Marco Negri & Mustafa Dülgerler, presented at PMI Global Congress 2016 - EMEA (Barcelona) - Lessons (Really) Learned? How to Retain Project Knowledge and Avoid Recurring Nightmares.** practitioner. **fetched-and-verified.**
`https://www.pmi.org/learning/library/knowledge-management-lessons-learned-10161`
Supports: Type A (project retrospective / lessons-learned). Direct statement of the 'captured and never retrieved' critique, with the traditional 3-step process (collect/document/communicate) named as 'highly ineffective'; also quotes PMBOK Guide 5th ed.'s definition of lessons learned and cites Li (2002) on NASA's lessons-learned repository being underused because it was too broad to search.
Quotable: "even when lessons are correctly identified, documented, and communicated, they often get lost in some sort of 'lessons learned database' - as in, a 'black hole' (Dalton, 2013) - that nobody ever looks at, preventing companies to really learn from experience and running the risk to repeat the same mistakes again and again." / "The traditional process of identifying and documenting lessons learned has proven to be highly ineffective, because most of the time companies fail to 'assimilate' the lessons they have identified, so people don't change their ways of doing things" / "one reason why the NASA 'official' agency-wide repository for lessons learned was not widely used, was because its lessons covered so many topics that it was difficult to search for an applicable lesson ... (Li, 2002)" / "One could say that 'if a lesson is not into the right checklist, you have not learned it!'"
Contested/time-bound: 2016 practitioner paper; PMI Congress papers are not blind-peer-reviewed academic literature.

**[71] Nancy Dixon (author, Common Knowledge; conversationmatters/nancydixonblog) - The Value of Lessons Learned.** practitioner. **fetched-and-verified.**
`https://web.archive.org/web/2015id_/http://www.nancydixonblog.com/2010/02/the-value-of-lessons-learned.html`
Supports: Type A. A recognized KM authority explicitly saying repositories 'didn't work very well'; the real value is in-team sense-making, not the transferable artifact; also gives timing guidance (hold before memory fades / before team disperses) directly relevant to the terminal-team problem.
Quotable: "So all those repositories of lessons learned that we built in the early days of KM just didn't work very well and lessons learned took on a bad name within organizations." / "The greatest value of lessons learned is for those who took the action." / "Meetings to construct lessons are held as soon as possible after the outcome because memory fades quickly" / "It is framed as a meeting to learn, not to judge  -  so no recriminations"
Contested/time-bound: Published Feb 2010 (16 years old). The live nancydixonblog.com domain has since expired and is now a parked/reseller page (confirmed directly  -  title reads 'Typepad | Network Solutions'); content only survives via Wayback Machine.

**[72] John Carter, TCGen (product-development consultancy) - Why Retrospectives are a Waste of Time.** practitioner. **fetched-and-verified.**
`https://www.tcgen.com/blog/why-retrospectives-are-a-waste-of-time/`
Supports: Straddles Type A/B ('performed after the conclusion of a release'). This is the cleanest example of 'the DOCUMENT is criticised even where the PRACTICE is endorsed': the author explicitly wants retrospectives kept (recommends timelines, data, root-cause analysis, and  -  critically  -  still recommends a repository), and condemns only the specific pattern of an unread Word doc emailed and filed/deleted.
Quotable: "these flip charts are written up in Microsoft Word document and sent to the team with a cc to some managers. The team members & managers get the email and either file them or delete them. And life goes on." / "Retrospectives performed at this level are less beneficial than a celebration dinner." / "these should be kept in a repository so they can be used to look at trends and provide evidence of improvement over time" / "every and I mean EVERY project kick off meeting should have a presentation of the most recent retrospective"
Contested/time-bound: Published May 28, 2023; updated Jul 1, 2024.

**[73] Dharun Anandayuvaraj, Tanmay Singla, Zain A. H. Hammadeh, Andreas Lund (German Aerospace Center/DLR), Alexandra Holloway (NASA JPL), James C. Davis; ICSE 2026 - Learning From Software Failures: A Case Study at a National Space Research Center.** academic. **fetched-and-verified.**
`https://arxiv.org/pdf/2509.06301`
Supports: Adjacent to Type A (incident/failure postmortem at a high-reliability engineering org, DLR + NASA JPL affiliation). This is the counter-evidence: here the failure mode is ABSENCE of documentation, not an unread repository  -  practitioners explicitly wish they had 'a lessons learned page or database.' Complicates a flat 'documentation is the problem' reading.
Quotable: "knowledge loss due to team turnover & fragmented documentation" / "I didn't know where to find stuff...I didn't know what was documented in GitLab...in the wiki...on the team [channel]...And people don't know that it's there and don't look at it. So it doesn't really help." / "failure knowledge was 'not referenced once [the project] is closed.'" / "I don't think they are documented, pretty much at all."
Contested/time-bound: 2026, ICSE'26 (Apr 2026), preprint (arXiv v3, Feb 2026)  -  very recent, not yet in final published form.

**[74] Enrico Teotti (practitioner blog) - Analyze Kerth prime directive.** practitioner. **fetched-and-verified.**
`https://teotti.com/analyze-kerth-prime-directive/`
Supports: Type A origin. Gives the full verbatim text of Kerth's Prime Directive and a defender's response to pushback; also reports (secondhand) live audience resistance ('that is a lie!'), which is the closest thing to documented skepticism I could find.
Quotable: "Regardless of what we discover, we must understand and truly believe that everyone did the best job he or she could given what was known at the time, his or her skills and abilities, the resources available, and the situation at hand." / "a person in the audience shouted to me 'that is a lie!'" / "The prime directive doesn't mean there isn't accountability. It simply tells us to stop looking for blame and accept that there are factors we need to gather a fuller picture." / "If when you have the full picture some actions are proven to be grave work misconducts they should be addressed by HR outside of a retrospective."
Contested/time-bound: Published July 10, 2018.

**[75] Amy Edmondson, Administrative Science Quarterly 44(2), 1999 - Psychological Safety and Learning Behavior in Work Teams.** academic. **fetched-and-verified.**
`https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Organizational_Learning_and_Change/Edmondson_1999_Psychological_safety.pdf`
Supports: Background theory for Kerth's Prime Directive (does NOT itself discuss retrospectives  -  this link is my inference). Useful because it pre-empts the 'toxic positivity / no-accountability' reading of blameless retros.
Quotable: "Team psychological safety is defined as a shared belief that the team is safe for interpersonal risk taking." / "The term is meant to suggest neither a careless sense of permissiveness, nor an unrelentingly positive affect but, rather, a sense of confidence that the team will not embarrass, reject, or punish someone for speaking up."
Contested/time-bound: 1999, foundational and still heavily cited; not about retrospectives specifically.

**[76] "Gowtham", AgileSeekers (practitioner/content-marketing blog) - Why Inspect and Adapt Events Fail to Drive Real Change.** practitioner. **fetched-and-verified.**
`https://agileseekers.com/blog/why-inspect-and-adapt-events-fail-to-drive-real-change`
Supports: Type B ceremony-vs-genuine-improvement critique: names 'ceremony theater' as a specific failure mode and ties failure to lack of reserved capacity/funding and leadership follow-through, not to the event's documentation.
Quotable: "most Inspect and Adapt sessions don't fail because people don't care. They fail because the system doesn't convert insights into action." / "Most Inspect and Adapt events focus on talking about improvement. Very few focus on funding improvement." / "If you don't allocate capacity, you're not serious about change. You're just collecting ideas."
Contested/time-bound: Published ~Aug 2026 (roughly one month before this research pass); author identified by first name only on a site that reads as SEO/content marketing  -  weak provenance, treat as corroborating color, not an authoritative camp leader.

**[77] Norman L. Kerth (Dorset House, 2001) - Project Retrospectives: A Handbook for Team Reviews.** primary. **not-retrieved.**
`https://www.oreilly.com/library/view/project-retrospectives-a/9780133488753/`
Supports: Origin of both the Prime Directive AND the term 'project retrospective' itself  -  i.e., this book is arguably the naming source for Type A. I could not access the book text directly; the Prime Directive wording is corroborated verbatim via Teotti (2018, fetched-and-verified above) and is reproduced identically across many secondary retro sites I did not fetch (TeamRetro, Parabol, EasyRetro, Scrum.org)  -  consistent enough to trust the wording, but I have not read Kerth's own text.
Contested/time-bound: 2001; 25 years old, still the uncontested origin point cited by every secondary source found.

**[78] Richard Skinner, Lesley Land, Wynne Chin, R. Ryan Nelson; International Research Workshop on IT Project Management 2015 (AIS eLibrary) - Reviewing the Past for a Better Future: Reevaluating the IT Project Retrospective.** academic. **url-confirmed-not-read.**
`https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1008&context=irwitpm2015`
Supports: Directly on-topic for Type A (explicitly 'reevaluating' the IT project retrospective construct) but blocked (403) on fetch. Flagging as a paper worth another dimension pursuing with authenticated access.
Contested/time-bound: 2015.

**[79] Abheeshta Putta, Maria Paasivaara, Casper Lassenius; PROFES 2018 / ACM - Adopting Scaled Agile Framework (SAFe): A Multivocal Literature Review.** academic. **url-confirmed-not-read.**
`https://dl.acm.org/doi/pdf/10.1145/3234152.3234164?download=true`
Supports: Potentially relevant academic evidence on SAFe adoption challenges (52 organizations, mixed grey+peer-reviewed literature) but blocked (403) on fetch  -  I cannot say whether it specifically addresses Inspect & Adapt.
Contested/time-bound: 2018.

**[80] U.S. Government Accountability Office - NASA: Better Mechanisms Needed for Sharing Lessons Learned (GAO-02-195) / Survey of NASA's Lessons Learned Process (GAO-01-1015R).** primary. **url-confirmed-not-read.**
`https://www.gao.gov/products/gao-02-195`
Supports: A government primary source independently corroborating the NASA lessons-learned-repository-underuse claim also cited (via Li 2002) in Negri & Dulgerler above  -  but I was blocked (403) fetching the PDF directly, so I'm not counting it as independent verification, only as a plausible corroborating title confirmed to exist on gao.gov.
Contested/time-bound: GAO-01-1015R (2001) / GAO-02-195 (Jan 2002); 24-25 years old.
