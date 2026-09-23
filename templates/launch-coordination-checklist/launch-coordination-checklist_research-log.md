# launch-coordination-checklist: research log

Research conducted 2026-09-22 across six dimensions (origins and admission, structure, methodology lineage,
debates and status, relationships and tooling, and the standing gap question). **46 source records merged to
39 unique sources, all 39 fetched-and-verified.** Only `fetched-and-verified` sources are quoted anywhere in
this bundle.

**Every quotation in this log was then checked against the source's raw text**, not against the summary the
retrieval tool returned. The research agents read pages through a tool that hands back a model's summary of
the page, and a summary can put words in a source's mouth. Each page was downloaded again and every quotation
searched for in it. **19 of the 193 quotations the agents returned were not in their sources and were
removed**, and exact wording was taken from the page wherever a removed quotation was load-bearing. The 199
quotations below all passed that check.

---

## What the check caught, and what was not read

Four kinds of failure, each of the kind this library's reviews exist to find, caught here at source rather
than in review:

- **An invented specific inside quotation marks.** One agent quoted [9] as saying a checklist was designed to
  tackle the infection "that nearly killed the girl in Austria". The article names a different patient.
  Plausible, specific and wrong, which is the library's dominant defect class.
- **A quotation attributed to a file that does not contain it.** One agent quoted the paired pm-skills skill
  [5] as calling its output a "Per-launch document (created 1-2 weeks before significant releases)", and
  added that this corroborated the build spec. The phrase is not in the skill.
- **A field that does not exist.** A Keptn release-checklist field was quoted as "Assignee: Firstname
  Lastname". The page [17] has a release-manager line instead.
- **Paraphrase presented as quotation.** Several quotations of the NASA report [7] had words changed, such as
  "checklist responses should" for the report's own "the response should". The report's wording replaces
  them.

The four quoted phrases in that list are recorded as failures and are **not** quotable from any source.

**Not read, and nothing in this bundle may rest on them:**

- **Gawande's book *The Checklist Manifesto*.** It is where the widely cited distinction between two ways of
  running a checklist comes from. No primary text was read, only secondary summaries, so this bundle does not
  quote that terminology or attribute it in quoted form. [7] supplies an older, readable version of the same
  distinction from aviation.
- **Pronovost et al. (NEJM, 2006) and Haynes et al. (NEJM, 2009)**, the studies behind the outcome figures
  that travel with checklist advocacy. Neither was read, so no outcome figure appears in this bundle.
- **The SEC order on Knight Capital**, read only through [19]'s analysis of it.
- **A GitLab handbook page on new product introduction and an Atlassian definition-of-done page.** Both
  returned no readable body on two attempts.
- **An AWS page said to describe ORR review meetings feeding a go or no-go launch decision.** Seen only in a
  search snippet, never fetched. [4] is read; that sentence is not in it.

---

## The admission record

**ADR 0030's test is met by the source the catalog already credits.** [1] is titled "Launch Coordination
Checklist", the type's catalog name verbatim, and presents itself as "This is Google's original Launch
Coordination Checklist, circa 2005, slightly abridged for brevity". Counted from its page, it has ten areas
and 31 items. Every item is a noun phrase; none carries an owner, a pass condition or a response.

**The practice around it is recorded in [2], and it answers the question the family contract left open.** A
launch is "any new code that introduces an externally visible change to an application". The checklist is an
instrument of qualification ("LCE employs a launch checklist for launch qualification"); it "helps an LCE
assess the launch and provides the launching team with action items and pointers to more information"; and
its unit is a question paired with an action item, as in "Do you need a new domain name?" paired with
"Coordinate with marketing on your desired domain name, and request registration of the domain."

**It is standing, by direct statement rather than inference**: "In 3.5 years, one LCE ran 350 launches
through the LCE Checklist." One list, hundreds of launches. The `standing-standards` membership test, which
the contract itself called ambiguous for this type, is met by the type's own origin.

**The licence governs reuse.** [1] and [2] both print "Licensed under CC BY-NC-ND 4.0". This bundle cites
them and quotes them briefly. **Its templates must not adapt the appendix's items, and its example must not
reproduce them.**

**Second sources, neither needed for admission.** [4], AWS's ORR whitepaper, is a published written document
describing a program in which "We generate different checklist templates from these questions based on the
workload being reviewed and the outcome we want to achieve". It is a readiness review rather than a launch
checklist, so counting it as a second admission source is a judgement, recorded as one. [3] shows the lineage
continuing inside Google, where a production readiness review's SRE team "establishes and maintains a PRR
checklist explicitly for the Analysis phase".

---

## Claims flagged contested or time-bound

1. **Standing or per launch: resolved, and both halves are true.** [2] ran one checklist through 350 launches.
   Vendor tooling frames the same thing from the other side: [27] presents its template as a reusable
   checklist, and [28] and [31] describe revising a checklist rather than replacing it. The per-launch camp
   is real too: the paired skill [5] and its template [6] produce a document tied to one launch, down to a
   check-in schedule dated around that launch, and [37] argues that readiness evidence expires with the
   version it was gathered for. **The reading adopted:** the standing instrument is the list and its rules,
   and a per-launch record is what applying it produces. No single source states that resolution; it is this
   bundle's synthesis of sources that each hold one half, and it is labelled as such. **The build's stop
   condition, evidence that no standing launch checklist exists in practice, was not triggered.**
2. **What an incident should do to the checklist: the two most direct sources disagree.** [2] holds that
   "Every question's importance must be substantiated, ideally by a previous launch disaster." [22], quoting
   Nora Jones on production readiness reviews, warns against adding a line item for every incident, because
   the result is a process nobody can trace back to its reasons. [21] tells teams to update the launch
   playbook after every launch. The sources agree that incidents inform the list; they disagree about whether
   an incident alone justifies a new item. [2]'s own history records the cost of the permissive reading:
   "In an effort to curb its growth, at one point, adding new questions to Google's launch checklist required
   approval from a vice president."
3. **Gate or guide.** [28] defends the deployment checklist as a forcing function rather than bureaucracy.
   [35] and [29] describe good readiness review as collaborative guidance rather than box-checking. [23]
   argues the late, discrete review is the wrong pattern altogether and should start with the design.
4. **Tiering: a lighter list, or the same bar with a different assessor.** In [2], low-risk launches "were
   faced with an almost trivial checklist, while higher-risk launches underwent the full gamut of checks and
   balances", and "By 2008, 30% of reviews were considered low-risk." [20] tiers the smallest launches down to
   a changelog entry. [15] instead keeps one standard for every service and changes who assesses it. The
   bundle teaches the question, not an answer.
5. **Scope: engineering readiness only, or cross-functional.** [1] and the scorecard vendors [29] to [34] are
   engineering and operations only. The paired skill [5] and [6], [36] and [35] reach into marketing,
   support and legal. [2] itself routes one of its sample questions to marketing.
6. **A per-check owner and evidence field is the exception in published lists, not the norm.** Of the
   published structures read, [12] carries both; the GitLab template [10], its filled instance [11], [16],
   [17] and [18] carry neither. This bundle's per-check design is argued from [2]'s question-plus-action unit
   and from [7]'s rule on responses, not from a count of practitioner templates.
7. **Time-bound.** [1] dates from about 2005 and describes one company's infrastructure. [12] and [13] are
   dated 2026-08-06; [36] is titled for 2026.
8. **The design evidence comes from aviation and medicine, and no source read asserts that it transfers to
   software launches.** [2] cites aviation preflight and surgical checklists as the reason checklists are used
   at all; it does not adopt their specific rules. Every use of [7], [8] or [9] in this bundle names its
   domain.
9. **A count error in the fan-out, corrected.** One agent described [1] as organised into nine categories. The
   page has ten.

---

## Notes for the companion

**The honest framing.** This document type has a named origin, and the origin is unusual three times over: it
is one company's internal instrument, it is published as a historical artifact, and it is licensed so that it
may not be adapted. **The bundle therefore teaches the practice around the checklist**, which [2] records in
detail, **rather than the checklist itself.**

**The evidentiary spine, in the order it should be used:**

1. **That the type exists:** [1], under its catalog name.
2. **That it is a standing instrument:** [2], one list through 350 launches.
3. **What a good check looks like:** [2]'s question paired with an action item, and its rule that "Every
   instruction must be concrete, practical, and reasonable for developers to accomplish"; [7]'s rule that
   "the response should always portray the actual status or the value of the item"; [8]'s demand that every
   item be linked to an action.
4. **How it stays short and current:** [2]'s curation history, including a review of the whole list "Once or
   twice a year"; [7]'s finding that "as the list of items grows, there may be a higher probability of
   overlooking any given item"; [8]'s brevity and collaboration rules. Aviation and medical evidence is
   labelled by domain every time.
5. **What it is not:** a runbook [24]; release notes, which the paired skill [5] routes elsewhere; a readiness
   review [3] [4]; a definition of done [25].

**The section design, as the research moved it from the spec.** Seven sections in full, five in lean:

| Section | Lean | What the research did to it |
|---|---|---|
| **Scope and Launch Classes** | yes | **Absorbs the spec's "When This Does Not Apply".** Exemption is decided with the launch class ([2]'s low-risk classes, [20], [15]), and the one published template that handles inapplicability does it per item [10], so a separate section would duplicate this one |
| **Roles and Decision Authority** | no | **Renamed from "Roles and Sign-off".** [1] and [2] name no sign-off at all; [12] names a single decision authority, and [19] shows what the absence of even a second reviewer cost. Lean carries the decision-maker inside Go/No-Go Criteria |
| **Readiness Checks** | yes | The load-bearing table. Each row carries the area, the question, what answers it (the actual status, per [7]), the owning role, and why the check is there (per [2]'s substantiation rule). Built from categories found across sources, **never from [1]'s items** |
| **Launch Communications** | no | Weakly evidenced as a separate section: no structure source read carries one. Kept for full because the paired skill [6] and [36] carry the content, and because the boundary with release notes lives here |
| **Rollout and Rollback** | yes | **Promoted to lean.** [2] describes automatic rollback on failed validation and independent revert through feature flags; [12] declares rollback triggers in advance; [19]'s failure had no kill switch. The gap dimension found this the element a naive list most reliably omits |
| **Go/No-Go Criteria** | yes | [12]'s states for a check and its rule that an accepted deviation needs a named owner and an expiry, plus its named anti-pattern of an override nobody owns. Carries the decision-maker in lean |
| **Review Trigger** | yes | Contract-mandated (section 4). No published structure carries one as a section. Bounded by [2]'s continuous curation, [21]'s update after each launch and [22]'s warning. **Labelled as this family's contribution, as `definition-of-done` and `runbook` label theirs** |

**Teaching points the templates, guide and example must stay consistent with:**

- **A launch checklist is standing; a launch plan is what applying it produces.**
- **A check earns its place by the failure it prevents**, and a check nobody can justify comes out.
- **An incident is a question for the list, not an automatic new item.** The trigger asks which mechanism
  failed, which is the resolution between [2] and [22].
- **A response states the actual status, not "done".**
- **Rollback triggers and go/no-go criteria are decided before the launch, by a named person.**
- **Length is a design constraint**, on aviation and medical evidence that is labelled as such.

**What this bundle must not say:** that checklists save lives or reduce failures by any figure; that Google's
checklist has a sign-off or approval gate; that production readiness reviews replaced launch checklists, which
no source read says; that an ORR meeting feeds a go or no-go decision, which is unverified; and anything
quoted from *The Checklist Manifesto*.

**The example.** Acme Analytics' platform team's standing checklist, as it stood when the Saved Views launch
consulted it. It must not reproduce [1]'s items.

**The pairing.** `deliver-launch-checklist` pairs honestly under the reading adopted above: the skill's
template [6] is a per-launch copy whose Go/No-Go Criteria and Rollback Plan are exactly what this standing
checklist supplies.

---

## Sources

**[1] Google, "Site Reliability Engineering" (O'Reilly Media; web edition at sre.google, copyright 2017 Google), Appendix E: "Launch Coordination Checklist".** primary (book). **fetched-and-verified.**
`https://sre.google/sre-book/launch-checklist/`
Supports: The library's admission requirement (ADR 0030/0048: a named source publishes the document type as a written document) - this is a full published checklist, reproduced verbatim as an appendix of a named source (Google) via a major technical publisher. The verbatim text of Google's original (circa 2005) Launch Coordination Checklist -- its structure (nine categories, each a cluster of prompting questions rather than yes/no items) as the direct ancestor artifact this bundle is named after.
Quotable: "This is Google's original Launch Coordination Checklist, circa 2005, slightly abridged for brevity" / "Architecture sketch, types of servers, types of requests from clients" / "Machine dies, rack fails, or cluster goes offline" / "How to detect when backends die, and what to do when they die" / "Monitoring internal state, monitoring end-to-end behavior, managing alerts" / "Release process, repeatable builds, canaries under live traffic, staged rollouts" / "Copyright © 2017 Google, Inc. Published by O'Reilly Media, Inc. Licensed under CC BY-NC-ND 4.0"
Contested/time-bound: Self-described as Google's checklist "circa 2005, slightly abridged". A historical artifact of one company's infrastructure, not a current standard. Licensed CC BY-NC-ND 4.0: cite and quote briefly, never adapt its items.

**[2] Rhandeev Singh and Sebastian Kirsch with Vivek Rau, edited by Betsy Beyer - "Reliable Product Launches at Scale", chapter 27 of Google, "Site Reliability Engineering" (O'Reilly Media; web edition at sre.google, copyright 2017 Google).** primary (book). **fetched-and-verified.**
`https://sre.google/sre-book/reliable-product-launches/`
Supports: Google's operational definition of a launch, what Launch Coordination Engineering (LCE) is and who does it, how the checklist is used and has changed over time, and Google's stance on rollout/rollback/gradual launches and go/no-go framing. The explicit SRE lineage claim (this chapter cites Gawande's checklist work as a named influence), the history of the Launch Coordination Engineering (LCE) team and its checklist (founded 2004, formalized from ad hoc 'Launch Engineer' consulting into 'Production Reviews'), and design rules the LCE team adopted to keep the checklist from decaying into an unmanageable list (curation cadence, per-item justification requirement, risk-tiering).
Quotable: "Google defines a launch as any new code that introduces an externally visible change to an application." / "Google approached the challenges inherent to launches by creating a dedicated consulting team within SRE tasked with the technical side of launching a new product or feature." / "Auditing products and services for compliance with Google's reliability standards and best practices, and providing specific actions to improve reliability" / "Acting as a liaison between the multiple teams involved in a launch." / "LCE now uses the following guidelines: Every question's importance must be substantiated, ideally by a previous launch disaster. Every instruction must be concrete, practical, and reasonable for developers to accomplish." / "The checklist needs continuous attention in order to remain relevant and up-to-date: recommendations change over time, internal systems are replaced by different systems, and areas of concern from previous launches become obsolete." / "Almost all updates to Google's services proceed gradually, according to a defined process, with appropriate verification steps interspersed." / "Very few launches at Google are of the 'push-button' variety, in which we launch a new product at a specific time for the entire world to use." / "Copyright © 2017 Google, Inc. Published by O'Reilly Media, Inc. Licensed under CC BY-NC-ND 4.0" / "Checklists are used to reduce failure and ensure consistency and completeness across a variety of disciplines. Common examples include aviation preflight checklists and surgical checklists [Gaw09]." / "In practice, there is a near-infinite number of questions to ask about any system, and it is easy for the checklist to grow to an unmanageable size. Maintaining a manageable burden on developers requires careful curation of the checklist. In an effort to curb its growth, at one point, adding new questions to Google's launch checklist required approval from a vice president." / "Every question's importance must be substantiated, ideally by a previous launch disaster. Every instruction must be concrete, practical, and reasonable for developers to accomplish." / "The checklist needs continuous attention in order to remain relevant and up-to-date... LCEs curate the checklist continuously and make small updates when team members notice items that need to be modified. Once or twice a year a team member reviews the entire checklist to identify obsolete items." / "To mitigate the repetition of such mistakes by capturing the lessons learned from past launches, a small band of experienced engineers, called the 'Launch Engineers,' volunteered to act as a consulting team. The Launch Engineers developed checklists for new product launches" / "To mitigate this scenario from the engineering perspective, SRE staffed a small, full-time team of LCEs in 2004... Their consulting sessions were formalized as Production Reviews." / "LCEs identified categories of low-risk launches that were highly unlikely to face or cause mishaps... Such launches were faced with an almost trivial checklist, while higher-risk launches underwent the full gamut of checks and balances. By 2008, 30% of reviews were considered low-risk." / "While each question on the LCE Checklist is simple, much complexity is built in to what prompted the question and the implications of its answer. In order to fully understand this degree of complexity, a new LCE hire requires about six months of training." / "Similarly, LCE employs a launch checklist for launch qualification." / "helps an LCE assess the launch and provides the launching team with action items and pointers to more information" / "Do you need a new domain name?" / "Coordinate with marketing on your desired domain name, and request registration of the domain." / "who are either hired directly into this role, or are SREs with hands-on experience running Google services" / "In 3.5 years, one LCE ran 350 launches through the LCE Checklist." / "In an effort to curb its growth, at one point, adding new questions to Google's launch checklist required approval from a vice president." / "Once or twice a year a team member reviews the entire checklist to identify obsolete items" / "Such launches were faced with an almost trivial checklist, while higher-risk launches underwent the full gamut of checks and balances." / "If the change doesn't pass the validation period, it's automatically rolled back." / "Independently revert each such change immediately in the event of serious bugs or side effects" / "Their consulting sessions were formalized as Production Reviews." / "LCEs might work with the owners of a particularly arduous approval process to simplify their criteria and implement automatic approvals for common cases." / "as the Launch Engineers' consulting sessions came to be called, became a common practice days to weeks before the launch of many new products." / "By 2008, 30% of reviews were considered low-risk."
Contested/time-bound: Describes Google practice as the book records it. Licensed CC BY-NC-ND 4.0. Says nothing about a formal sign-off or approval gate for a launch.

**[3] Acacio Cruz and Ashish Bhambhani, edited by Betsy Beyer and Tim Harvey - "The Evolving SRE Engagement Model", chapter 32 of Google, "Site Reliability Engineering" (O'Reilly Media; web edition at sre.google, copyright 2017 Google).** primary (book). **fetched-and-verified.**
`https://sre.google/sre-book/evolving-sre-engagement-model/`
Supports: How Production Readiness Review (PRR) relates structurally to a checklist: the Simple PRR Model still centers on a maintained checklist for its Analysis phase, and PRR itself grew out of LCE's launch-checklist consulting practice (per Ch. 27's 'formalized as Production Reviews').
Quotable: "Usually, the SRE team establishes and maintains a PRR checklist explicitly for the Analysis phase. The checklist is specific to the service and is generally based on domain expertise, experience with related or similar systems, and best practices from the Production Guide." / "The most typical initial step of SRE engagement is the Production Readiness Review (PRR), a process that identifies the reliability needs of a service based on its specific details."
Contested/time-bound: Licensed CC BY-NC-ND 4.0.

**[4] Amazon Web Services - "Operational Readiness Reviews (ORR)", AWS Well-Architected Framework whitepaper (June 30, 2022).** vendor (whitepaper). **fetched-and-verified.**
`https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html`
Supports: Candidate second admission source: whether AWS ORR is a published written checklist document (vs. a process or tool feature only). This page's own text is verbatim-quotable; one operational-process claim below (review meeting / go-no-go escalation) came from a search snippet, not this fetch, and is marked accordingly. AWS's own definition of an ORR: curated best-practice questions distilled from AWS's own operational incidents; teams review the appropriate checklist 'throughout the complete lifecycle of their service, from inception to post-release operations' (so ORR spans more than a single pre-launch moment, unlike this bundle's narrower launch-window scope); high-criticality findings from the review meeting are escalated to leadership 'as input to a go or no-go launch decision' - the same go/no-go vocabulary the launch checklist bundle uses, which is the clearest sign the two document types share a decision mechanism even though ORR's scope is broader and recurring (yearly re-reviews cited). Sells: the Well-Architected Framework / AWS's own operational tooling and consulting posture.
Quotable: "Amazon Web Services (AWS) created the Operational Readiness Review (ORR) to distill the learnings from AWS operational incidents into curated questions with best practice guidance." / "This document is intended to help you understand how the AWS ORR program was built and guide you in creating your own ORR program as part of the AWS Well-Architected Framework." / "We generate different checklist templates from these questions based on the workload being reviewed and the outcome we want to achieve." / "Teams perform self-assessments on operational risks to achieve operational excellence by reviewing the appropriate ORR checklist throughout the complete lifecycle of their service, from inception to post-release operations." / "ORR is a complementary process to Well-Architected, using a data-driven approach to ensure a consistent review of operational readiness, with a specific focus on eliminating known, common causes of impact in your workloads." / "We generate different checklist templates from these questions based on the workload being reviewed and the outcome we want to achieve. Teams perform self-assessments on operational risks to achieve operational excellence by reviewing the appropriate ORR checklist throughout the complete lifecycle of their service, from inception to post-release operations."
Contested/time-bound: Describes AWS's own program. A sentence about ORR review meetings feeding a go or no-go launch decision was seen only in a search snippet and is NOT verified; nothing may rest on it.

**[5] product-on-purpose - pm-skills, "deliver-launch-checklist" SKILL.md (skill version 2.2.0).** internal. **fetched-and-verified.**
`https://raw.githubusercontent.com/product-on-purpose/pm-skills/main/skills/deliver-launch-checklist/SKILL.md`
Supports: What the paired pm-skills launch-checklist skill produces: 13 sections (Launch Overview, Engineering Readiness, QA & Testing, Design & UX, Marketing & Communications, Customer Support, Legal & Compliance, Operations & Infrastructure, Analytics & Monitoring, Go/No-Go Criteria, Rollback Plan, Check-in Schedule, Open Issues); every item requires an owner and target date; distinguishes blockers from nice-to-haves; intended use window is 1-2 weeks before significant/cross-functional launches; explicitly NOT for small single-team changes ('adds ceremony without value') or for generating customer-facing announcements. The clearest per-launch-camp evidence: this skill frames the artifact explicitly as a 'per-launch document' created 1-2 weeks before significant releases, and separately gives a tiering/skip rule for small changes. Confirms and extends the quote already logged in docs/internal/tier2-specs.md (which I did not re-derive, only corroborate).
Quotable: "adds ceremony without value" / "clear criteria for making the launch decision" / "prevent launch-day surprises" / "a launch checklist adds ceremony without value; track it in the sprint instead"
Contested/time-bound: A sibling project from the same organisation; Apache 2.0. The phrase "Per-launch document (created 1-2 weeks before significant releases)" was returned by one research agent as a quotation and does NOT appear in this file; it was removed.

**[6] product-on-purpose - pm-skills, "deliver-launch-checklist" references/TEMPLATE.md.** internal. **fetched-and-verified.**
`https://raw.githubusercontent.com/product-on-purpose/pm-skills/main/skills/deliver-launch-checklist/references/TEMPLATE.md`
Supports: Confirms the template's per-domain content (9 domains: Engineering, QA, Design/UX, Marketing, Support, Legal/Compliance, Ops/Infra, Analytics/Monitoring) and its go/no-go framing (blocker / should-have / nice-to-have), a rollback-plan section with trigger conditions/steps/owner/time estimate, and a fixed check-in cadence (T-7, T-2, launch day, T+1). This is a per-launch authored document (built around a specific launch's check-in dates), not a standing reused list.

**[7] Asaf Degani and Earl L. Wiener - "Human Factors of Flight-Deck Checklists: The Normal Checklist", NASA Contractor Report 177549 (May 1990).** academic (NASA contractor report). **fetched-and-verified.**
`https://ntrs.nasa.gov/api/citations/19910017830/downloads/19910017830.pdf`
Supports: Item wording/phraseology, list length, pause points and initiation, who reads vs. who confirms (challenge-response vs. do-list), checklist-vs-procedure distinction, and the specific failure modes that cause checklists to decay or be abandoned.
Quotable: "Challenge-Response... the checklist is a backup for the initial configuration of the plane. Here, the pilots use their memory and other techniques to configure the plane. After completing the initial configuration, the pilots use the checklist to verify that several critical items have been correctly accomplished." / "Do-list. This method can be better termed 'call-do-response.' ... the checklist is used to 'lead' and direct the pilot in configuring the aircraft using a step-by-step, 'cook book' approach." / "Most do-list checklists of transport aircraft are generally very detailed and time-consuming. In addition, due to the elimination of the configuration redundancy, a mistake can easily pass unnoticed once the sequence is interrupted." / "The matter of which items should be presented on the checklist is a cardinal question in checklist philosophy... only the critical and most important items should be presented on the checklist." / "The estimated probability of error (per-item) for a checklist with no check-off provision was one in a hundred, while the probability of error for a checklist with some kind of a check-off provision was much lower, only three in a thousand." / "The completion call of a task-checklist should be written as the last item on the checklist, allowing all crew members to move mentally from the checklist to other activities with the assurance of all pilots that the task-checklist has been completed." / "A long checklist should be subdivided to smaller task-checklists or chunks that can be associated with systems and functions within the cockpit." / "The most critical items on the task-checklist should be listed as close as possible to the beginning of the task-checklist, in order to increase the likelihood of completing the task before interruptions may occur." / "Checklist distractions and interruptions lead to the following consequences: 1. Elimination of the vital cross-checking of the other crew member. 2. Disruption of the sequential flow of the checklist. 3. Committing to memory the location of the interruption in the checklist sequence." / "Every effort should be made to avoid using the checklist as a 'site' for resolving discipline problems." / "Flight crews should be made aware that the checklist procedure is highly susceptible to production pressures. These pressures 'set the stage' for errors by encouraging substandard performance, and later may lead some to relegate checklist procedures to second level of importance, or not use them at all." / "In several instances during night operation, the checklist card was drawn out of the slot (above the glare shield), but no light was turned on to allow reading. Consequently, the checklist was performed from memory." / "Several pilots deviated from the challenge-and-response method to a faster technique. This technique was to call several challenge items together in one 'chunk,' while the other pilot would reply with a series of chunked responses. This technique of conducting the checklist undermines the concept behind the step-by-step challenge-and-response procedure." / "FAR 121.315... (b) The approved procedures must include each item necessary for flight crew-members to check for safety before starting engines, taking off, or landing, and in engine and system emergencies. The procedure must be designed so that a flight crewmember will not need to rely upon his memory for items to be checked." / "the response should always portray the actual status or the value of the item" / "Only procedural steps which, if omitted, would have a direct and adverse impact on normal operation are included." / "as the list of items grows, there may be a higher probability of overlooking any given item"
Contested/time-bound: Aviation evidence. No source read for this bundle asserts that its design rules transfer to software launches.

**[8] World Health Organization - "Implementation Manual: WHO Surgical Safety Checklist" (2009), hosted by the Leapfrog Group.** standards (WHO implementation manual). **fetched-and-verified.**
`https://www.leapfroggroup.org/sites/default/files/Files/Implementation%20manual%20WHO%20surgical%20safety%20checklist%202009.pdf`
Supports: The three-pause-point structure, the designated-coordinator/team-confirms model, and the explicit design principles (Focused, Brief, Actionable, Verbal, Collaborative, Tested, Integrated) for keeping a checklist short and used rather than decayed into paperwork.
Quotable: "In order to implement the Checklist during surgery, a single person must be made responsible for performing the safety checks on the list. This designated Checklist coordinator will often be a circulating nurse, but it can be any clinician participating in the operation." / "The Checklist divides the operation into three phases, each corresponding to a specific time period in the normal flow of a procedure--the period before induction of anaesthesia, the period after induction and before surgical incision, and the period during or immediately after wound closure but before removing the patient from the operating room." / "All steps should be checked verbally with the appropriate team member to ensure that the key actions have been performed." / "Focused The Checklist should strive to be concise, addressing those issues that are most critical and not adequately checked by other safety mechanisms. Five to nine items in each Checklist section are ideal." / "Brief The Checklist should take no more than a minute for each section to be completed. While it may be tempting to try to create a more exhaustive Checklist, the needs of fitting the Checklist into the flow of care must be balanced with this impulse." / "Actionable Every item on the Checklist must be linked to a specific, unambiguous action. Items without a directly associated action will result in confusion among team members regarding what they are expected to do." / "Verbal The function of the Checklist is to promote and guide a verbal interaction among team members. Performing this team Checklist is critical to its success--it will likely be far less effective if used solely as a written instrument." / "In order to ensure brevity, the WHO Surgical Safety Checklist was not intended to be comprehensive." / "It will take practice for teams to learn to use the Checklist effectively. Some individuals will consider it an imposition or even a waste of time. The goal is not rote recitation or to frustrate workflow." / "removing safety steps because they cannot be accomplished in the existing environment or circumstances is strongly discouraged." / "Prior to any rollout of a modified Checklist, it should be tested in a limited setting." / "Any effort to modify the Checklist should be in collaboration with representatives from groups who might be involved in using it"
Contested/time-bound: Medical evidence; same caution on transfer. The manual cites Haynes et al. (NEJM 2009) for outcome effects and does not restate a figure; that paper was not read, so no outcome number may appear.

**[9] Atul Gawande - "The Checklist", The New Yorker (December 10, 2007), course-reading copy hosted at lchc.ucsd.edu.** practitioner (magazine). **fetched-and-verified.**
`https://lchc.ucsd.edu/cogn_150/Readings/gawande_checklist.pdf`
Supports: The aviation origin story of the checklist (Boeing Model 299), the design philosophy of Pronovost's ICU checklists (narrow scope, memory-recall + explicit-standard functions), and the organizational/cultural resistance that causes checklists to fail in practice. Also the primary source through which the widely-cited '1,500 lives' checklist statistic traces to the Keystone Initiative (central-line/ICU checklists), not the WHO surgical checklist.
Quotable: "The Boeing model was deemed, as a newspaper put it, 'too much airplane for one man to fly.'... came up with an ingeniously simple approach: they created a pilot's checklist, with step-by-step checks for takeoff, flight, landing, and taxiing." / "With the checklist in hand, the pilots went on to fly the Model 299 a total of 1.8 million miles without one accident." / "The checklists provided two main benefits, Pronovost observed. First, they helped with memory recall... A second effect was to make explicit the minimum, expected steps in complex processes." / "Some physicians were offended by the suggestion that they needed checklists." / "In the Keystone Initiative's first eighteen months, the hospitals saved an estimated hundred and seventy-five million dollars in costs and more than fifteen hundred lives." / "In December, 2006, the Keystone Initiative published its findings in a landmark article in The New England Journal of Medicine." / "He didn't attempt to make the checklist cover everything; he designed it to tackle just one problem"
Contested/time-bound: Journalism. The widely repeated lives-saved figure it reports belongs to the Keystone ICU central-line program, not to surgical or launch checklists; the underlying study was not read. One agent-returned quotation altered a named patient and was removed.

**[10] GitLab - ".gitlab/issue_templates/Operational Readiness.md", issue template in the gitlab-org/gitlab repository.** practitioner. **fetched-and-verified.**
`https://gitlab.com/gitlab-org/gitlab/-/raw/df973a6d104cd94a9fb3f8172696a4944fdbcc46/.gitlab/issue_templates/Operational%20Readiness.md`
Supports: Real, in-repo readiness-review template. Heading order: Links, Type of new component, Review process, Checklist, then item groups Common, New GitLab service, New data store/third party dependency, New programming language/dev/test framework, New database. Items are yes/no checkboxes grouped by area (matches 'Readiness Checks grouped by area'). No owner, pass-condition, evidence, or sign-off field on any individual item; the footer assigns the issue to a PM/EM but that is issue-tracker metadata, not a template field.
Quotable: "Common" / "New GitLab service" / "New data store, third party dependency" / "New programming language, development, and testing framework" / "New database"

**[11] GitLab infrastructure - gl-infra/readiness issue #13, "ActionCable readiness review" (a filled instance of the template).** practitioner. **fetched-and-verified.**
`https://gitlab.com/gitlab-com/gl-infra/readiness/-/issues/13`
Supports: A filled, real readiness review. Section order: Summary, Architecture, Documentation, Performance (with Database Concerns and Memory subsections), Scalability, Availability, Durability (with Backups subsection), Security/Compliance, Monitoring. Items are yes/no checkboxes with parenthetical guidance, grouped by area - supports 'Readiness Checks grouped by area' as a real pattern. No section in this instance carries an owner, pass/fail, evidence, or sign-off field.
Quotable: "Summary" / "Architecture" / "Documentation" / "Performance" / "Scalability" / "Availability" / "Durability" / "Security/Compliance" / "Monitoring"

**[12] Nawaz Dhandala, OneUptime - "Run a Launch-Day Go/No-Go Decision" (2026-08-06).** vendor (blog). **fetched-and-verified.**
`https://oneuptime.com/blog/post/2026-08-06-launch-day-go-no-go/view`
Supports: Named-author practitioner piece from an open-source observability company, the strongest structural match to the proposed design. Sections in order: Separate Readiness from Immediate Launch Conditions; Assign Decision Roles (a role/responsibility table); Use Green/Yellow/Red/Unknown (a pass-condition framework); Build the Launch-Day Scorecard (checks grouped by area: artifact control, user/service health, capacity, dependencies, operational control); Predeclare Rollback and Stop Triggers (machine-evaluable abort conditions plus manual triggers); Launch in Bounded Stages; Keep a Live Decision Record (a markdown template with Time/Gate/State/Evidence/Owner/Decision columns); Avoid Common Failure Patterns; Launch Gate Example (YAML schema); Official Documentation; Conclusion. This is the one source that carries all four of owner, pass-condition (RAG), evidence, and sign-off-equivalent (the Decision column) together, and it is also the one source with an explicit rollback/stop-trigger section and a named decision-role for communications (mentioned inside the roles table, not as its own section). Named single decision authority per risk tier; a four-state (green/yellow/red/unknown) evaluation instead of a binary pass/fail; pre-declared, machine-evaluable rollback/abort triggers; exceptions must be explicit, owned, and time-bounded rather than silent; naming the 'executive override without ownership' anti-pattern; a live decision record of what was observed, who decided, and why.
Quotable: "Assign Decision Roles" / "Keep a Live Decision Record" / "Predeclare Rollback and Stop Triggers" / "Name roles rather than inviting a large distribution list" / "makes the go/no-go call for the current risk tier" / "green: evidence is within the predeclared safe range; yellow: an accepted deviation requires explicit risk ownership; red: a hard gate failed; unknown: evidence is absent, delayed, or untrustworthy" / "Unknown is not green" / "Do not debate a clear hard trigger while impact grows. Abort first, then investigate" / "Either the prerequisite is met, an authorized time-bounded exception exists, or the decision is no-go" / "Executive override without ownership: a deadline silently replaces a hard gate" / "a short live record to show what was observed, who decided, and why" / "Record yellow-state acceptance, expiry, and decision authority." / "Unknown is not green." / "Executive override without ownership: a deadline silently replaces a hard gate."
Contested/time-bound: Vendor source dated 2026-08-06, prescriptive rather than a record of observed practice.

**[13] OneUptime - "Run a Post-Launch Readiness Review" (2026-08-06).** vendor (blog). **fetched-and-verified.**
`https://oneuptime.com/blog/post/2026-08-06-post-launch-readiness-review/view`
Supports: A launch is not verified once at cutover: review timing should follow evidence windows keyed to the service's own workload cycle (immediate/early/representative, e.g. a weekly peak or month-end close); rollback-compatible schema/config should be deliberately preserved until that observation window closes rather than cleaned up early; the review should reconstruct the operator's actual experience (interviews) to surface undocumented runbook gaps, not just check dashboards.
Quotable: "For one service, that might mean reviews after 24 hours and after one weekly peak. For another, it may require a month-end close." / "Keep rollback-compatible schema, artifacts, and configuration until the agreed observation window ends." / "runbook gaps"
Contested/time-bound: Vendor source, prescriptive.

**[14] Government Digital Service - GOV.UK Service Manual, "How the live phase works".** primary (government service manual). **fetched-and-verified.**
`https://www.gov.uk/service-manual/agile-delivery/how-the-live-phase-works`
Supports: Government service-manual guidance for going live, but NOT checklist-shaped: it is prose organized under topic headings (Running your service during live; Meeting the standard to move into live; Solving a whole problem for users; Providing a joined up experience across channels; Other things to consider before you move into live; When you need to retire your service). Confirms topics (information security, accessibility, uptime, vulnerability testing, performance testing) as pre-live considerations, phrased as topics/conditions, not questions or checks. No owner, sign-off, rollback, or go/no-go decision-gate language found on this page. Notably carries a lifecycle-adjacent section ('When you need to retire your service') that our proposed design has no equivalent for.

**[15] Government Digital Service blog - "Meeting the standard regardless of size" (2014).** primary (government blog). **fetched-and-verified.**
`https://gds.blog.gov.uk/2014/06/17/meeting-the-standard-regardless-of-size/`
Supports: A real, published government go-live gate: every new or redesigned service must be assessed against all 26 points of the Service Standard before going live on GOV.UK (explicit, published criteria for not launching) - deliberately applied 'no matter how small the transaction is' rather than being waived for small services. The scaling mechanism is who assesses, not whether: GDS itself assesses higher-volume services, while departmental Digital Leaders and a departmental panel assess and certify lower-volume ones (under 100,000 transactions/year) against the same 26 criteria. This is a real precedent for a named, accountable sign-off role and a volume-based routing of assessment authority, without lowering the bar for smaller launches.
Quotable: "all new or redesigned services have had to be assessed against all 26 points in the standard" / "it ensures that no matter how small the transaction is a service will be built to the same standards" / "Digital Leaders from across government departments agreed that they would be responsible for assessing, using a panel from their department, services with under" / "Digital Leader to certify that the service has been assessed and meets the Digital by Default criteria"
Contested/time-bound: Dated 2014; describes the GOV.UK Service Standard as it stood then.

**[16] Consumer Financial Protection Bureau - open-source-project-template, "opensource-checklist.md".** practitioner. **fetched-and-verified.**
`https://github.com/cfpb/open-source-project-template/blob/main/opensource-checklist.md`
Supports: A US-government-published, real pre-release checklist, CC0-1.0 licensed (confirmed via the repo). 14 items, each phrased as a yes/no question ('Has PII been removed?', 'Are there unit tests?'), no section grouping beyond a single flat list under one heading ('Open Source Check List'), no owner, pass-condition, evidence, or sign-off field on any item.
Quotable: "Has PII been removed?" / "Have security vulnerabilities been remediated?" / "Is our `TERMS.md` included?"
Contested/time-bound: Licensed CC0 1.0. An open-source publication checklist, narrower than a launch checklist.

**[17] Keptn project (CNCF) - "Release Checklist" wiki page.** practitioner. **fetched-and-verified.**
`https://github.com/keptn/keptn/wiki/Release-Checklist`
Supports: Real open-source project release runbook. Structured as sequential numbered steps (Versioning scheme, Select semantic versions, GitHub Issues/Milestone, Step 1-10 covering component releases, Final steps) rather than topic sections. Items are action-item imperatives ('Choose', 'Define a release manager', 'Double check the content'), several carrying an explicit 'Assignee: Firstname Lastname' field per step - the closest of my sources to a per-item owner field, though there is still no formal pass/fail, evidence, or sign-off field.
Quotable: "Define a release manager"
Contested/time-bound: One agent-returned quotation ("Assignee: Firstname Lastname") does not appear on the page and was removed.

**[18] Radek Pietruszewski - "Open-source project release checklist".** practitioner. **fetched-and-verified.**
`https://radek.io/posts/release-checklist/`
Supports: Named-practitioner published checklist. Sections: Licensing, Landing page, Accessibility, Documentation, Bug tracker, Tools. All items phrased as yes/no questions ('Does your project...', 'Is...'). No owner, pass-condition, evidence, or sign-off fields anywhere - a pure self-assessment checklist. No license statement found on the page itself for the checklist content. Nothing for this dimension; consulted. It is a personal, advisory checklist ('you can use some, you can use all,' 'don't worry if you can't do all of them') with a single hard blocker (an open-source license) and no go/no-go gate, no named decision-maker, no rollback discipline, and no statement of how it updates itself - i.e. it is itself close to the naive flat-list this dimension is looking past, and confirms by contrast what the stronger sources above add.
Quotable: "Licensing" / "Landing page" / "Accessibility" / "Documentation" / "Bug tracker" / "Tools" / "Without a licence, your project isn't open source." / "You can use some, you can use all." / "every little helps"
Contested/time-bound: A personal, optional checklist; useful only as a contrast case.

**[19] Doug Seven - "Knightmare: A DevOps Cautionary Tale" (2014).** practitioner. **fetched-and-verified.**
`https://dougseven.com/2014/04/17/knightmare-a-devops-cautionary-tale/`
Supports: A real, named incident showing the cost of a naive checklist: no written requirement for a second person to review the deployment (so a partial rollout onto one of eight servers went uncaught), and no rollback plan decided or tested in advance (so the emergency rollback itself made the incident worse by leaving the broken code active on the untouched servers). Directly evidences 'rollback triggers decided in advance' and post-deploy cross-instance verification as gap elements a flat task list omits.
Quotable: "Knight did not have a second technician review this deployment and no one at Knight realized that the Power Peg code had not been removed" / "Knight had no written procedures that required such a review" / "As it turns out there was no kill switch" / "Deployments need to be automated and repeatable and as free from potential human error as possible"
Contested/time-bound: Secondary analysis of Knight Capital's August 2012 deployment failure, drawing on the SEC's findings; the SEC order itself was not read.

**[20] GTM Playbook - "Launch Tiering Framework for Product Marketing Teams".** practitioner. **fetched-and-verified.**
`https://discover.gtmplaybook.co/launch-tiering-framework`
Supports: Which launches get the full checklist is itself a decision made in advance, on a scored rubric, before launch planning starts, not left to whoever asks loudest; a named 'changelog only' tier exists for launches that explicitly do not warrant the full coordination process; tier is a joint, scored decision, not a unilateral PM call.
Quotable: "Tiering should be a joint decision with clear scoring criteria, not a negotiation where the loudest voice wins." / "Tier 3: Minor Release (Changelog Only)" / "score of 8-10 = Tier 1" / "Tiering decisions must happen upstream"
Contested/time-bound: A marketing-side framework, prescriptive.

**[21] GTM Playbook - "Launch Postmortem Template".** practitioner. **fetched-and-verified.**
`https://discover.gtmplaybook.co/launch-postmortem-template`
Supports: How the checklist/process itself gets updated after a launch: postmortem findings are meant to accumulate into a living 'Launch Playbook' document, updated after every launch, that becomes the reference before the next one; a failed launch's postmortem is explicitly named as the most valuable input to that update; every learning is required to carry an owner, due date, and target metric so it converts into an actual process change rather than a note nobody acts on.
Quotable: "Launch Playbook" / "Update it after each launch." / "A failed launch postmortem is the most valuable. You'll learn the most." / "Every learning needs an owner, due date, and target metric"

**[22] InfoQ - article on incidents, production readiness reviews and psychological safety, quoting Nora Jones.** practitioner. **fetched-and-verified.**
`https://www.infoq.com/articles/incidents-prr-psychological-safety/`
Supports: The clearest sourced answer on the postmortem-feeds-checklist loop found in this research: Nora Jones states organizations should study past incidents to shape and give meaning to PRR requirements, but explicitly warns against a naive per-incident append loop: 'With every incident that went awry, we would add a line item to our PRR process. Definitely do not do that, because you end up with this PRR process that's just monstrous and you cannot understand the underlying mechanisms.' The recommended loop is indirect - extract the reasoning behind an incident, not a new checklist line - not a mechanical postmortem-to-checklist pipeline.
Quotable: "Incidents are catalysts to understanding the difference between how your organization is structured in theory versus how it operates in practice." / "I've certainly been in organizations where we've been a bit too reactive to incidents. With every incident that went awry, we would add a line item to our PRR process. Definitely do not do that, because you end up with this PRR process that's just monstrous and you cannot understand the underlying mechanisms."

**[23] Jos Visser - "The Continuous Production Readiness Review" (Substack).** practitioner. **fetched-and-verified.**
`https://josvisser.substack.com/p/the-continuous-production-readiness`
Supports: Direct, named argument that traditional PRRs happen 'right before the launch' and surface non-functional gaps that are by then too late to fix; proposes starting the PRR document alongside the design doc and filling it out through development, turning the artifact 'from a checklist to a to-do list that is used during development' - i.e., collapsing the distinction between a standing readiness list and a per-launch checklist by making the checklist itself live earlier in the lifecycle. On the postmortem loop specifically: argues teams should design-in known best practices up front rather than rediscover them via postmortems, since a postmortem finding that merely restates an industry-standard practice the team skipped is 'a miss' rather than a genuine new lesson.
Quotable: "Start doing the production readiness review in parallel with writing your design doc and continue filling out the production readiness review document during software development." / "from a checklist to a to-do list that is used during development"
Contested/time-bound: An argument for changing practice, not a description of it.

**[24] Dunya Kirkali - "Runbooks are not checklists".** practitioner. **fetched-and-verified.**
`https://blog.incrementalforgetting.tech/p/runbooks-are-not-checklists`
Supports: Sharpest sourced statement of the runbook/checklist boundary: a checklist is linear and prescriptive (a launch checklist's native shape - verify known prerequisites); a runbook must instead encode judgment and branching ('what to check first, what to avoid, when to branch, and when to escalate') for handling variation under pressure. Maps directly onto this bundle: launch-coordination-checklist legitimately IS a linear checklist (verifying known, named prerequisites before a decision point); an operational runbook is a different document because it must carry decision logic a checklist format cannot hold.
Quotable: "what to check first, what to avoid, when to branch, and when to escalate"

**[25] ProductPlan - "The Definition of Done: What Product Managers Need to Know".** practitioner. **fetched-and-verified.**
`https://www.productplan.com/learn/agile-definition-of-done`
Supports: Definition of Done (DoD) is a standing, universal engineering quality gate ('an agreed-upon set of items that must be completed before a project or user story can be completed') applied to every unit of work, distinct in scope and cadence from a launch checklist, which is a one-time, cross-functional, per-launch coordination document. ProductPlan explicitly frames DoD as engineering-owned and narrower than a PM's full launch responsibility ('you're not done with a product... until you've put it out to pasture'), i.e., DoD is necessary-but-not-sufficient input to a launch checklist rather than a synonym for one.
Quotable: "an agreed-upon set of items that must be completed before a project or user story can be considered complete" / "you're not done with a product (or feature) until you've put it out to pasture"

**[26] incident.io - "Why Do Post-Mortem Action Items Fail?".** vendor (blog). **fetched-and-verified.**
`https://incident.io/blog/why-do-post-mortem-action-items-fail-how-to-make-incident-follow-ups-actually-get-done`
Supports: A negative/absence finding: this vendor's own treatment of postmortem action items does NOT describe a systematic postmortem-to-launch-checklist (or postmortem-to-readiness-checklist) feedback mechanism. Runbooks appear only once, as an example of a single tracked action item ('update the runbook for auth service failover procedure by next Friday'), treated as an ordinary task, not as evidence of a structured feedback loop into a standing checklist. Sells: an incident-management/postmortem tracking product.
Quotable: "Alex: update the runbook for auth service failover procedure by next Friday" / "actions survive on rhythm, not good intentions"
Contested/time-bound: Vendor source.

**[27] Asana - "Software Deployment Template".** vendor. **fetched-and-verified.**
`https://asana.com/templates/software-deployment`
Supports: Direct, explicit vendor statement that a deployment/launch checklist template is meant to be reused across multiple launches, with improvements carried forward as a new version of the same standing template.
Quotable: "It works as a reusable checklist, so your team can follow a proven process from planning to post-launch monitoring without having to start over each time." / "Once you've completed a deployment, save your updated project as a new template so you can carry forward any improvements for next time."
Contested/time-bound: Vendor template page.

**[28] DeployHQ - "The Ultimate Deployment Checklist".** vendor (blog). **fetched-and-verified.**
`https://www.deployhq.com/blog/the-ultimate-deployment-checklist-ensuring-smooth-and-successful-releases`
Supports: Gate-as-forcing-function (not bureaucracy) framing, explicit rubber-stamp critique, standing/pinned-template reuse instruction, and an explicit staleness/review-cadence rule for keeping the checklist current.
Quotable: "A deployment checklist is not bureaucracy. It is a forcing function that catches the mistakes your brain glosses over when you are eager to ship." / "Not just rubber-stamped. Reviewers should run the code locally or, at minimum, read the diff carefully." / "Copy this checklist and pin it to your deployment runbook. Adapt it to your stack, but do not skip sections." / "Review it quarterly or whenever you change your deployment infrastructure. Add items when you encounter a new failure mode and remove items that are fully automated and no longer need manual verification."
Contested/time-bound: Vendor source; a deployment checklist rather than a launch checklist.

**[29] Cortex - "Production Readiness Review Checklist & Best Practices".** vendor (blog). **fetched-and-verified.**
`https://www.cortex.io/post/how-to-create-a-great-production-readiness-checklist`
Supports: Vendor framing that a PRR checklist should be living/tiered by service type and re-validated over time rather than a one-off document ('production ready three months ago might no longer be ready'); pitches moving from manual per-review checklists to Cortex's automated continuous evaluation. Standing/living-checklist framing; PRR-as-gate definition; tiering by service type; staleness language (readiness decays over months) and continuous-validation remedy.
Quotable: "production ready three months ago might no longer be ready" / "A production readiness checklist should be at the core of any PRR, but it needs to be living and adaptable rather than static." / "A Production Readiness Review is the formalized checkpoint that ensures services meet your readiness standards before launch." / "What matters for a customer-facing API is different from what matters for an internal batch job. Your checklist should be tailored to the type of service being launched." / "Treat readiness as a continuous process, not a milestone." / "A service that was production ready three months ago might no longer be ready." / "Exceptions are necessary to avoid blocking launches when circumstances require flexibility."
Contested/time-bound: Vendor source; the vendor sells automated scorecards as a replacement for manual checklist reviews.

**[30] Cortex - "Standardize: Scorecards: Create" (product documentation).** vendor (documentation). **fetched-and-verified.**
`https://docs.cortex.io/standardize/scorecards/create`
Supports: Cortex Scorecards are continuous evaluation frameworks (default re-evaluation every 4 hours), structured either as Bronze/Silver/Gold level progression or point-weighted rules; 'Production Readiness' ships as a pre-built template. Confirms Cortex's explicit self-positioning: standing/continuous, not a one-time launch gate. Sells: a paid internal developer portal / service catalog with a Scorecard product.
Quotable: "establish best practices, track migration, promote accountability among teams, enforce standardization across entities, or define maturity standards"
Contested/time-bound: Vendor product documentation.

**[31] OpsLevel - "Production readiness checklist: An in-depth guide".** vendor (blog). **fetched-and-verified.**
`https://www.opslevel.com/resources/production-readiness-in-depth`
Supports: Standing-but-evolving template framing (revised as org learns, not rewritten from scratch); tiering by application criticality; iterate-and-revise staleness discipline. Explicitly silent on comms/legal/marketing scope and on any PRR-vs-launch-checklist relationship.
Quotable: "As your organization learns more about its applications and your tech stack's specific needs, you'll want to revise the checklist." / "you may have different production readiness needs based on your application tier" / "a small internal service that's not mission-critical" / "a customer-facing application that pays the bills" / "As with code, you should iterate and revise the checklist to ensure that it meets your company's changing needs."
Contested/time-bound: Vendor source.

**[32] OpsLevel - "Scorecards" (product documentation).** vendor (documentation). **fetched-and-verified.**
`https://docs.opslevel.com/docs/scorecards`
Supports: OpsLevel Scorecards are team-level, lightweight rubrics distinct from the org-wide Rubric; both represent a standing, continuously-evaluated framework per service (Maturity Report shows ongoing health, not a point-in-time snapshot). A Scorecard literally named 'Production Readiness' is offered as an example. Sells: a paid internal developer portal (service catalog + scorecards).
Quotable: "measure and track service health against their own unique goals, separate from the organizational standards" / "lightweight Rubrics that are set by individual"
Contested/time-bound: Vendor product documentation.

**[33] OpsLevel - "Getting Started with Rubrics" (product documentation).** vendor (documentation). **fetched-and-verified.**
`https://docs.opslevel.com/docs/getting-started-with-rubrics`
Supports: The org-wide Rubric structures checks into Bronze/Silver/Gold Levels x Categories; a component's level is continuously recomputed from live check results, not authored once per launch. Confirms the standing-list model and explicit tie to 'production readiness.'
Quotable: "Each level is broken down into categories of checks, which must all be passed before the level is achieved." / "If a component passes all of the checks in the Silver column, in addition to the checks in the Bronze column, then it would be a Silver component."
Contested/time-bound: Vendor product documentation.

**[34] Spotify - Backstage Soundcheck documentation, "Core concepts: Tracks".** vendor (documentation). **fetched-and-verified.**
`https://backstage.spotify.com/docs/plugins/soundcheck/core-concepts/tracks`
Supports: Soundcheck (a Backstage plugin, sold by Spotify) models readiness as Tracks composed of Levels composed of Checks, evaluated continuously/on-schedule against every service - a standing, always-on list, never a per-launch document. Certification history is retained (120 days default). Sells: a paid Backstage plugin for continuous tech-health/readiness scoring.
Quotable: "Tracks encourage alignment to architectural best practices and standards and are analogous to an organization's long-term tech health initiatives." / "the highest certified levels for every entity and their applicable tracks over time"
Contested/time-bound: Vendor product documentation for a paid plugin.

**[35] DX (getdx) - "Production readiness checklist for dependable releases".** vendor (blog). **fetched-and-verified.**
`https://getdx.com/blog/production-readiness-checklist/`
Supports: Standing-template framing for PRR checklists; gate-vs-guide (collaborative problem-solving over box-checking); tiered rigor by change type; cross-functional PRR ownership including legal/compliance for regulated industries; and (second fetch) that this specific article treats 'product readiness' (should we ship) vs 'production readiness' (can we support it) but never discusses launch checklists as a separate document from PRR - a gap.
Quotable: "Instead of just checking boxes, they use reviews to surface risks and align on solutions." / "Don't apply the same rigor to a marketing page update as you would to payment processing changes. Create different readiness tiers." / "effective PRRs are cross-functional by design" / "Include legal and compliance stakeholders in readiness reviews." / "Product readiness asks: 'Should we ship this?' Production readiness asks: 'Can we safely support this in production?'" / "Use Notion, Confluence, or Google Docs to standardize your readiness checklist and review format."
Contested/time-bound: Vendor source.

**[36] Userpilot - "Product Launch Checklist for 2026: The Execution Playbook".** vendor (blog). **fetched-and-verified.**
`https://userpilot.com/blog/product-launch-checklist/`
Supports: The strongest single source on tiering by launch magnitude, on standing-template reuse ('lessons outlive the people who ran it'), and on cross-functional scope naming PM/design/marketing/support/sales explicitly, with support training named as a pre-launch item.
Quotable: "Right-size the launch before you plan it. A major feature earns the full pre-launch sweep, an enhancement needs a marketing announcement and a sales heads-up, and a minor update needs little more than release notes and support awareness." / "Matching effort to scope is what keeps a Tier 3 update from eating a Tier 1 amount of time." / "Copy these checklists into your project tool, give every item an owner, and work through them as you ship." / "Each launch should make the next one faster, which only happens when the lessons outlive the people who ran it." / "The core roster is a product manager to steer, a designer to make it usable, a marketer for research and the GTM, a customer success or support lead for resources, and a salesperson to actually sell." / "Train customer support on the technical details and common questions"
Contested/time-bound: Vendor source; titled for 2026.

**[37] Playcode - "Product Launch Checklist: Evidence Before Go-to-Market".** vendor (blog). **fetched-and-verified.**
`https://playcode.io/blog/product-launch-checklist`
Supports: The most direct evidence for the 'reusable model, per-instance record' resolution the maintainer's spec proposes: a fixed evidence/authority model scaled across three launch shapes, with each launch's evidence explicitly version- and candidate-bound and reviewed by a stated future date - i.e. the structure is standing, the filled record is per-launch.
Quotable: "Readiness is version-bound. A change to the product, configuration, environment, pricing, message, channel, support coverage, policy boundary, or dependency invalidates the affected evidence and can change the decision." / "Evidence reviewed August 1, 2026. Review time-sensitive guidance and source facts again by November 1, 2026." / "Give each required gate one owner, status, evidence reference, expected observation, and blocker relationship." / "Keep the same evidence and authority model while scaling the number of gates, owners, channels, and observation windows to the launch scope and risk."
Contested/time-bound: Vendor source.

**[38] Studio Red - "Production Readiness: A Practical Guide for Real Launches".** vendor (blog). **fetched-and-verified.**
`https://www.studiored.com/blog/design/production-readiness/`
Supports: Distinguishes deployment readiness (the release moment) from production readiness (long-term operability), a nearby but not identical claim to 'launch checklist vs PRR'; does not use either term, so it cannot carry that specific claim.
Quotable: "Deployment readiness focuses on the moment a product is released to manufacturing or the market. Production readiness covers the broader question of whether the product can be produced, scaled, supported, and maintained over time."
Contested/time-bound: Vendor source.

**[39] Atlassian - Jira "Product Launch Timeline" template page.** vendor. **fetched-and-verified.**
`https://www.atlassian.com/software/jira/templates/product-launch-timeline`
Supports: Confirms an issue-tracker launch template exists as a first-party Jira template: timeline/calendar/dashboard views over launch tasks with owners, deadlines, and status - functionally an issue-tracker rendering of the same content a launch-coordination checklist holds (owner + date + status per item), applied per-launch (adapted per product) rather than a standing readiness scorecard. Sells: Jira project templates.
Quotable: "assign ownership to individual team members and track the progress each team member has made on the tasks they've been assigned"
Contested/time-bound: Vendor template page.
