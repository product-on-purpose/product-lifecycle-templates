# announcement-internal-comms: research log

Research conducted 2026-09-25 in two passes: an admission sweep run while the spec was written (thirteen
agents across this type and `change-request`, covering named bodies, product and engineering practice,
boundaries and failure modes, and the library's own references), and the build's six-dimension fan-out
(canon, structure, boundaries, failure modes, audience and timing, and the standing gap question). **40
sources are recorded below, all fetched-and-verified.** Only `fetched-and-verified` sources are quoted
anywhere in this bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a
retrieval tool returns. Pages were read as downloaded (HTML decoded as UTF-8, PDFs through `pdftotext`
without `-layout`) and each quotation searched for as a normalized substring. Of 181 quotations the build's
agents returned, 161 passed as returned, 12 more passed once the spacing an HTML extraction inserts before
punctuation was normalized, and **8 were dropped**. Four quotations were added from the admission sweep's own
checks.

---

## What the checks caught, and what was not read

**Eight quotations did not survive the raw check and are not in this log.** Two were table rows stitched
together with separators that appear nowhere on the page (a LaunchNotes comparison table and a Prosci
table); three were paraphrases presented as quotations (from LogRocket, Ragan and a LaunchNotes timing
post); one was a Prosci sentence whose parenthesis did not match the page; and one, from Wendy Hirsch, carried
em-dashes this library cannot reproduce verbatim. The sources themselves stay where other quotations from
them passed.

**A search summary put numbers on a page that does not carry them, and a research agent caught it.** A search
engine's summary of [33] reported "two weeks" and "30 days" notice periods. The fetched body carries no day or
week figure at all. The only numeric notice guidance in this log is [32]'s, and it is about policy changes,
not product launches.

**"Bottom line up front" is not in the current US Army regulation it is usually credited to.** [39], AR 25-50
as revised in 2020 and 2024, contains neither the phrase nor the acronym; the superseded 2013 edition, [40], did. The
principle is sourced here to [6] (the inverted pyramid) and [7] (the buried lede).

**A paywalled article is represented only by its free lead paragraph.** [31], Larkin and Larkin in the Harvard
Business Review (1996), was readable only to its first paragraph. The claim usually attributed to it, that
front-line employees are best reached face to face and through their own supervisor, reaches this log only
through [30]'s restatement, and **nothing in this bundle may attribute it to [31] directly.**

**Two pages do not show their authors' names.** [9] and [11] are published on the authors' own site,
workingbackwards.com, but the names Colin Bryar and Bill Carr do not appear in the text as fetched. They are
recorded under the site's own attribution.

**Not read, and nothing in this bundle may rest on them:**

- **Two statistics [18] cites**, a McKinsey figure on failed change programmes and a Gallup figure on employees
  knowing what their company stands for. Neither primary source was read; neither number may appear.
- **Reforge's PR/FAQ page** (rendered only by script) and **a post on captainscodebook.com** (did not resolve).
- **A ScienceDirect paper on internal communication channels**, seen only as a search abstract.
- **Any standards-tier source on channel choice or notice periods.** Every source on those questions is a
  vendor's or a practitioner's. The companion says so.

---

## The admission record

**ADR 0030's bar, as [ADR 0048](../../docs/internal/decisions/0048-one-named-source-clears-the-admission-test.md)
reads it, is met by three named sources, all of them vendor or practitioner tier.** [1] Staffbase names and
defines the type ("An organizational announcement is an internal communication that shares important updates
with employees across a company.") and ships seven worked templates, one a product launch, with the caveat
"These templates are a starting point, not a one-size-fits-all solution." [2] GitLab's handbook prescribes what
a company-wide announcement must carry and where it goes. [3] Jason Fried describes Basecamp's internal
Deployment post, written when a feature ships, in which "one of the people who did the work also writes up a
message in the Deployment project that explains what's new, points out what could be an issue".

**No standards body, government or professional institute publishes the document.** [38], the UK government's
functional standard for communication, names announcements only as an activity: "Communication, in the context
of this functional standard, includes announcements, media management, coordinated communication activities".
[12] and [25], from Prosci, publish communication plans and checklists, never the announcement. [39] publishes
the memorandum, which the catalog lists as this type's alias; it is **not counted**, because admitting a type
on the strength of the library's own alias would be the library certifying itself.

**The family is `delivery-docs`, by
[ADR 0059](../../docs/internal/decisions/0059-announcement-internal-comms-joins-delivery-docs.md)**, not the
`communication-docs` family that forecast it: that family's only axis value describes a standing instrument,
and an announcement is written once.

---

## Claims flagged contested or time-bound

1. **Internal and external: one document, or two in sequence.** Three vendor and agency sources say two, internal
   first: [16] ("you should leave enough time between your internal and external launch so you can set realistic
   milestones for each department"), [18] ("Internal precedes external. It does not run alongside it.") and [23],
   for whom support hearing of a feature from a customer "is a failure of sequencing rather than of knowledge".
   [24] makes the same split for changelogs. The only combined form is the PR/FAQ ([9], [11]), which carries an
   internal FAQ, and it is written before the decision, not after. **No source above vendor or agency tier makes
   the internal-first claim**, and the companion must say so.
2. **Who should send it.** Prosci holds that the project team is the wrong sender ([12]: "One of the biggest and
   most common mistakes you can make is to have your project team sending all the communications"), and that
   the business reason should come from a leader and the personal impact from the reader's own manager ([25]).
   Launch practice assumes the product team runs the briefing ([23], [27]). [3] has "one of the people who did
   the work" write it. The sources do not reconcile these; they may describe different messages within one
   announcement, and the companion reports all three.
3. **Face to face or written first.** [12] and [25] favour face-to-face communication; [26] and [28] treat email
   and the intranet as the default for formal company-wide announcements. The difference may be one of scope
   (change management against routine channel choice) and no source reconciles it.
4. **How much notice.** [2]'s window ("Announcements should be made ideally 72 hours (at minimum 24 hours) in
   advance of a due date") is GitLab's house rule. [36]'s "at least one business day before the change goes live"
   is Salesforce's own practice. [32] gives weeks, for policy changes. **No general norm is sourced for a product
   launch**, and every figure must be labelled as the named organization's own.
5. **One Q&A section, or an internal FAQ split from an external one.** Only [9] splits them. [1] lists a linked
   FAQ as optional best practice, never as a section of its templates.
6. **Prosci's register is not consistent within one page.** [12] warns that skipping change management produces
   "a telling plan rather than a communications plan", while its own FAQ defines change communication as telling.
   Quote the warning, not the FAQ line.

---

## Notes for the companion

**The honest framing.** The internal announcement is among the most commonly written documents in any
organization and among the least often published as a named form by an authority. This bundle's admission
rests on three vendor and practitioner sources, and its evidence on channels and timing is vendor-only; the
`communication-docs` contract predicted exactly that of the category. **The library's own contributions are
two, and each is labelled as such**: the line drawn between this document and `release-notes` by purpose
rather than audience, and treating every fact in an announcement as something read from an upstream artifact.

**The evidentiary spine, in the order it should be used:**

- **What it is:** [1]'s definition, [2]'s prescribed content, [3]'s named format.
- **Where it ends:** [10] ("Curated user-impact summary for a release, written so customers and GTM teams know
  what changed and why it matters") and [15] ("Use 125 words or fewer, and no images or videos") for release
  notes; [11] ("Normally, writing a press release is the last step in launching a new product") for the PR/FAQ;
  [4] ("Heartbeats summarize the last ~6-weeks of work for a given team, department, or individual") for the
  periodic update; [12] for the communication plan; [13] for incident communication, bounded by its trigger, a
  live incident, rather than by purpose. **The boundary with a launch checklist is inferred, not sourced**: [14]
  describes launch readiness as a process that produces announcement-like material and never names the line.
- **How it reads:** [6] ("Start content with the most important piece of information so readers can get the main
  point, regardless of how much they read") and [7], for the lede only: its illustrations are sentence-level and
  it must not be cited for how an announcement's sections are ordered.
- **What it asks of the reader:** [5] ("What's changing?", "Why is this change important?", "What do they need to
  do next, and by when?") and [1] ("what they need to do (if anything)").

**How it fails, as sourced, and nothing more:**

- **Burying the point.** [7]; [16]: "avoid burying the most relevant information with the generic bits".
- **Jargon.** [1]: "Use plain language and avoid corporate jargon."; [16]; [19].
- **Posting where it gets lost.** [2]: "we recommend that you do not use #whats-happening-at-gitlab as a sole
  location for important announcements as information might get lost or muted".
- **Broadcasting instead of starting a conversation.** [1]: "internal announcements feel more like broadcasts than
  conversations"; [12]'s telling plan.
- **No call to action**, now a named failure rather than only a fix: [21], "Leaving Out The Call To Action",
  "information without action is a courtesy, not a catalyst".
- **Telling customers before the people who support them.** [23], above; [16].
- **Attention spent.** [17]: "Notification fatigue is the exhaustion and desensitisation people feel when they
  receive too many alerts"; [2]: "Be mindful of the attention economy." **"Announcement fatigue" is not a term
  any source uses**; [22] uses "message fatigue". Do not coin it.

**What this bundle must not say:** that contradicting the release notes is a documented failure (no source says
so; it is this library's reason for the link-do-not-restate rule, and labelled as that); that "announcement
fatigue" is established usage; any figure [18] cites; that [31] says supervisors are the best channel; that AR
25-50 prescribes "bottom line up front"; or that internal-first sequencing is settled practice beyond vendor and
agency sources.

**The section design, as the research moved it from the spec.** The spec's single size holds: [1]'s seven
templates share one short shape, and its two highest-stakes examples differ from the rest by one sentence, not a
section. Its six sections hold, with three additions that are **routed through decision procedure 12 as guidance,
not new sections**:

- **What It Means for You** also says what is not changing. [37] asks "What's not changing?" as part of describing
  a change, and [12] frames the same material around the reader's own stake.
- **Where to Learn More** also says when the next update comes. [37]: "Let people know when you will update them
  again".
- **Frontmatter carries the sender** alongside audience, channel and send date, because the sender is contested
  (above) and the choice should be deliberate.

Candidates from the gap question that stay in the guide or rubric rather than the template: acknowledging a
negative impact honestly ([37]), showing the change with a screenshot or short video ([36]), planned repetition and
a follow-up message ([12]: "Preferred senders should repeat key messages five to seven times"; [36]), and a named
person answering questions after it goes out ([36]). An FAQ section stays out: only [9] carries one as a section.

**Teaching points the template, guide and example must stay consistent with:**

- **Purpose, not audience, separates it from release notes.** `release-notes_companion.md` already recommends the
  full notes for internal readers; what distinguishes the announcement is that it says what the change means for
  its reader and what they must do.
- **Link, do not restate.** [2]: "The majority of information should still be in the Handbook which you include
  links to." Every fact is read from an upstream artifact and linked.
- **The point first**, in one line a reader can act on ([6], [7]).
- **The reader's action and its deadline**, or an explicit statement that there is nothing to do ([5], [1], [21]).
- **Known issues reach the front line here first** ([3], [23]).
- **House rules are labelled as house rules.** GitLab's notice window and Salesforce's one business day are theirs.

**The example.** The internal announcement of the **Saved Views Sharing** launch, sent by its communications
owner, Priya Nair (PM, Reporting), as `launch-coordination-checklist_example.md` names her. It must agree with
that example on every shared fact: Support (Jordan Ames, Support Lead) is briefed before the first rollout stage
opens, on what "shared" means for entitlement (the recipient's own permissions still gate what they see) and on
why a total can change after opening a shared view; a help center article on creating, sharing and setting a
default view is live before go-live; sharing rolls out in two stages behind the existing `saved_views` flag, stage
one enabling the `shared` scope for the Reporting squad's own dashboards only for 48 hours, stage two for every
Acme Analytics dashboard, each stage needing its own go from Dana Osei; the public announcement is a separate
`release-notes` entry. **It is dated after the exit review of 2026-07-17** and must agree with
`status-report_example.md`'s account of 14 to 28 July, which carries R-05 (a shared view could expose PII to a
recipient without the matching entitlement) as escalated and unresolved. It links to the checklist, the PRD and
the release notes rather than restating them.

**A pre-existing contradiction the example must not repeat.** `release-notes_example.md` (Acme Analytics 2.4.0,
2026-06-30) lists sharing as new, while the launch checklist puts the Sharing launch after the 2026-07-17 exit
review, and `project-milestone-retrospective_example.md` puts general availability on 2026-09-14. **The example
states no release number** and draws its launch facts from the checklist, the PRD, the test plan and the status
report. The contradiction is recorded for the maintainer, not fixed in this bundle.

**The pairing.** `pairs_with: []`. No pm-skills skill produces an internal launch announcement; the nearest,
`foundation-stakeholder-update`, translates one meeting's outcomes for people who were not there.

**The aliases.** `internal memo` and `launch announcement` are kept. `Slack canvas` is dropped: it names a surface,
not a document. **`release announcement` is never used**, because `release-notes` already carries it.

---

## Sources

**[1] Robert Grover / Staffbase - "Organizational Announcements: Best Practices, Examples & Templates".** vendor. **fetched-and-verified.**
`https://staffbase.com/blog/organizational-announcements`
Supports: Names and defines the document type by name; gives its purpose and audience; ships seven worked example templates (one a new-product-launch announcement) sharing a common shape; states author and publish/update dates; states licence in the page footer. The shared shape of all seven worked templates, counted in the raw text by the main loop on 2026-09-25: each has a subject line, an email copy and the same salutation, and each body runs three or four sentences.
Quotable: "An organizational announcement is an internal communication that shares important updates with employees across a company."
Quotable: "These templates are a starting point, not a one-size-fits-all solution."
Quotable: "Use plain language and avoid corporate jargon."
Quotable: "what they need to do (if anything)"
Quotable: "internal announcements feel more like broadcasts than conversations"
Quotable: "Involve leadership"
Quotable: "Link to FAQs or additional resources"
Quotable: "A short FAQ section, linked resource, or named contact can reduce confusion"
Quotable: "Launching [Product Name] - Now Available!"
Quotable: "We're proud to announce the official launch of [Product Name], a major milestone in our innovation roadmap."
Quotable: "Copyright © 2015 to present, Staffbase (or its affiliates). All rights reserved."

**[2] GitLab - GitLab Handbook, Communication page, section "How to make a company wide announcement".** vendor. **fetched-and-verified.**
`https://handbook.gitlab.com/handbook/communication/`
Supports: Prescribes announcement content (5 W's) and process rules (link to Handbook for detail, channel gating by reach, lead-time norm, attention-economy caution); page footer licence; no visible author byline or publish date on the page itself. The handbook keeps internal and external communication in separate sections and states no order between them (the page's own section list, read in the raw text by the main loop on 2026-09-25).
Quotable: "Keep it simple, brief and summarize what is important. Cover the 5 W's. What, Why, Who, When, Where (you can also add How, if required as a call to action). The majority of information should still be in the Handbook which you include links to."
Quotable: "Is this relevant to all team members globally?"
Quotable: "we recommend that you do not use #whats-happening-at-gitlab as a sole location for important announcements as information might get lost or muted"
Quotable: "Announcements should be made ideally 72 hours (at minimum 24 hours) in advance of a due date. This is to prevent APAC/EMEA team members missing important announcements posted outside their normal working hours."
Quotable: "Be mindful of the attention economy."
Quotable: "© 2026 GitLab All Rights Reserved"

**[3] Jason Fried (37signals) - "Deployments: How we announce new features and updates internally at Basecamp".** practitioner. **fetched-and-verified.**
`https://world.hey.com/jason/deployments-how-we-announce-new-features-and-updates-internally-at-basecamp-b709544e`
Supports: Names a real internal document format for a shipped feature/launch, its authorship and audience, and its purpose (explain what's new, flag issues, serve front-line staff); gives byline and date; states no explicit licence on the page.
Quotable: "one of the people who did the work also writes up a message in the Deployment project that explains what's new, points out what could be an issue"
Quotable: "they're wonderful for those on the front lines too"
Quotable: "Jason Fried"
Quotable: "January 6, 2022"

**[4] 37signals - Basecamp, "How we communicate" guide (Heartbeats and Kickoffs).** practitioner. **fetched-and-verified.**
`https://basecamp.com/guides/how-we-communicate`
Supports: Establishes the boundary case the spec calls for: Heartbeats and Kickoffs are periodic, recurring documents (every 6 weeks), not one-off launch/change announcements - used to distinguish this bundle's scope from an adjacent, non-qualifying internal document type. Page carries no byline or publish date; footer states licence/copyright holder as 37signals LLC.
Quotable: "Heartbeats summarize the last ~6-weeks of work for a given team, department, or individual"
Quotable: "Kickoffs are essentially the opposites of Heartbeats. Rather than reflect, they project."
Quotable: "© 37signals LLC. All rights reserved."

**[5] Atlassian Team Playbook, "Change Management Communication With Video" (Play).** vendor. **fetched-and-verified.**
`https://www.atlassian.com/team-playbook/plays/change-management-communication-with-video`
Supports: A concrete 7-step ordered structure for an internal change/launch announcement, delivered as a script rather than a written doc but decomposable into the same content elements: (1) optional kickoff/alignment step, (2) outline the message (what's changing / why now / why it matters / how it impacts the audience / feedback channel), (3) prepare visuals plus 'who/where/when/how' details and a call to action, (4) assemble into a natural flow with an intro-body-CTA-closing shape, (5) record/deliver, (6) distribute (audience mapping, channel choice, amplifiers, restating the ask and deadline), (7) close the loop with a feedback/reaction mechanism and a follow-up commitment.
Quotable: "Change management communication is the process of clearly conveying the purpose, benefits, and steps of a new initiative to ensure teams understand, align with, and confidently adopt the change."
Quotable: "What's changing? What will be different from the way it is today? Is there a new process or tool they need to adopt?"
Quotable: "Why is this change happening now? Why is this change important? How does it align with the company's goals or vision? What guided the decision to make this change?"
Quotable: "How will this change impact them? Give them a sense of the vision: "This is what will happen next." What does success look like? What impact or value will the change deliver? Is there an opportunity to give feedback? If so, how and by when?"
Quotable: "Details and expectations: Think about the "who," "where," "when," and "how" of this change."
Quotable: "Call to action: What do they need to do next, and by when?"
Quotable: "Who needs to see this? ... Where do they look for info? ... Who can help amplify the message?"
Quotable: "Reiterate what's required of team members and by when, keeping the message clear and actionable."
Quotable: "Follow through with the plan you outlined in the video and set reminders to update your audience at key milestones and/or at promised times."

**[6] Nielsen Norman Group (Kate Moran), "Inverted Pyramid: Writing for Comprehension".** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/inverted-pyramid/`
Supports: The ordering principle behind announcement structure generally: lead with the single most important/conclusive fact, then descend through supporting detail to background, so the piece is legible and truncatable at any point - directly informs where a 'what's changing' or 'bottom-line' element should sit relative to context/background elements in an announcement template.
Quotable: "Start content with the most important piece of information so readers can get the main point, regardless of how much they read."
Quotable: "the most important information (or what might even be considered the conclusion) is presented first. The who, what, when, where and why appear at the start of a story, followed by supporting details and background information."
Quotable: "The name "inverted pyramid" comes from picturing the broad facts at the top of the story, followed by smaller and smaller details, like a triangle balanced on one corner."
Quotable: "Frontload all elements of content with important information. The main headline should be descriptive. The story should start with the main point. Each heading or subheading should be descriptive. The first sentence of every paragraph should be the most important."
Quotable: "Consider adding a summary or list of highlights. Some sites go a step beyond and add a summary ... or a bulleted list of key points to further emphasize the main takeaways of the content."

**[7] MLA Style Center (Erika Suffern), "Don't Bury the Lede".** practitioner. **fetched-and-verified.**
`https://style.mla.org/dont-bury-the-lede/`
Supports: The 'lede' concept and the failure mode of burying it, illustrated at sentence level rather than document-section level; supports the general principle behind leading with the newsworthy fact but does NOT itself describe a multi-section announcement format - worth citing for the terminology/failure-mode ('burying the lede') rather than for a section list.
Quotable: "A lede is the most newsworthy part of a news story. Journalists are taught to keep it front and center: a story should lead with the lede."
Quotable: "A writer "buries the lede" when the newsworthy part of a story fails to appear at the beginning, where it's expected."
Quotable: "Say, for example, that two people die in a house fire. The lede is buried if the reporting mentions the location, time, or cause of the fire before the deaths."
Quotable: "You don't have to slavishly avoid burying the lede. Variety in your sentences keeps you and your readers from becoming bored."

**[8] Purdue OWL, "Parts of a Memo".** reference. **fetched-and-verified.**
`https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/memos/parts_of_a_memo.html`
Supports: A canonical, named, ordered segment structure for an internal memo - the closest analogue in the owned set to a full document template: Heading segment (TO/FROM/DATE/SUBJECT), Opening segment (purpose stated briefly up front), Context, Task segment (what the writer is doing about the problem), an optional Summary segment for longer memos (key recommendations, placed early), Discussion segment(s) ordered strongest-to-weakest/most-important-first, Closing segment (requested action, courteous close), and Necessary Attachments noted below the closing.
Quotable: "TO: (readers' names and job titles) FROM: (your name and job title) DATE: (complete and current date) SUBJECT: (what the memo is about, highlighted in some way)"
Quotable: "Before indulging the reader with details and the context, give the reader a brief overview of what the memo will be about."
Quotable: "The context is the event, circumstance, or background of the problem you are solving."
Quotable: "One essential portion of a memo is the task statement where you should describe what you are doing to help solve the problem."
Quotable: "If your memo is longer than a page, you may want to include a separate summary segment. ... This segment provides a brief statement of the key recommendations you have reached. These will help your reader understand the key points of the memo immediately."
Quotable: "The discussion segments are the longest portions of the memo ... Begin with the information that is most important. This may mean that you will start with key findings or recommendations. Start with your most general information and move to your specific or supporting facts."
Quotable: "After the reader has absorbed all of your information, you want to close with a courteous ending that states what action you want your reader to take."
Quotable: "Make sure you document your findings or provide detailed information whenever necessary. You can do this by attaching lists, graphs, tables, etc. at the end of your memo."

**[9] Colin Bryar & Bill Carr (Working Backwards LLC), "Working Backwards PR/FAQ Instructions & Template".** practitioner. **fetched-and-verified.**
`https://workingbackwards.com/resources/working-backwards-pr-faq/`
Supports: A named-practitioner (former Amazon VPs, authors of 'Working Backwards') published, ordered element list for Amazon's internal PR/FAQ format, the closest thing in the wider literature to a standing internal-announcement-style template with a fixed section order: Heading (one sentence naming the product), Subheading (customer + benefit, one sentence), Summary Paragraph (dateline + launch date + summary of product/benefit), Problem Paragraph (customer's problem, written from their POV), Solution Paragraph(s) (how the product solves it, with an explicit competitive-differentiation sentence), Quotes & Getting Started (a company quote, a hypothetical customer quote, a getting-started link), followed by an External FAQ section (press/customer questions) and then an Internal FAQ section (anticipates every internal department's questions: finance, marketing, support, ops, HR, legal, technical).
Quotable: "Its principal tool is a second form of written narrative called the PR/FAQ, short for Press Release and Frequently Asked Questions."
Quotable: "Heading: Name the product so the reader ... will understand - one sentence under the title."
Quotable: "Subheading: Describe the customer for the product and what benefits they will gain from using it - one sentence underneath the Heading."
Quotable: "Summary Paragraph: Start with the city, media outlet, and your proposed launch date. Give a summary of the product and its benefits."
Quotable: "Problem Paragraph: This is where you describe the problem(s) that your product is designed to solve. Make sure you write this paragraph from the customer's point of view."
Quotable: "Solution Paragraph(s): Describe your product in detail and how it simply and easily solves the customer's problem. ... the solution must acknowledge the competition and state how this new product is meaningfully differentiated."
Quotable: "Quotes & Getting Started: Add one quote from you or your company's spokesperson and a second from a hypothetical customer describing the benefit of using your new product."
Quotable: "The first section is devoted to External FAQs. This is where you provide detailed answers to the questions that you can expect the press and customers to ask."
Quotable: "The next section is the internal FAQs. A well-written internal FAQ section anticipates the most important questions that senior leaders and stakeholders in the company will ask after reading the PR. Anticipate questions from every department in the company: finance, marketing, customer support, operations, HR, etc."

**[10] LaunchNotes, "Release Notes vs. Changelog: Key Differences".** vendor. **fetched-and-verified.**
`https://www.launchnotes.com/release-notes/vs-changelog`
Supports: The release-notes/changelog boundary is drawn by PURPOSE and audience, not by internal-vs-external: a changelog is a technical ledger, release notes are a user-impact summary, and a well-run team keeps both regardless of who reads which.
Quotable: "Release notes and changelogs both document change. They differ in audience, purpose, and tone."
Quotable: "Changelog - Curated technical record of notable changes, usually by version, for developers, integrators, and operators."
Quotable: "Release notes - Curated user-impact summary for a release, written so customers and GTM teams know what changed and why it matters."
Quotable: "Same shipment, different job: outcomes, who is affected, and what to do next - without the full technical inventory."
Quotable: "Can one document serve both audiences? Sometimes for tiny products. Past a small team, mixed tone usually fails both sides. Prefer two tracks from one workflow."

**[11] Working Backwards (Colin Bryar and Bill Carr), "The Amazon Working Backwards PR/FAQ Process".** practitioner. **fetched-and-verified.**
`https://workingbackwards.com/concepts/working-backwards-pr-faq-process/`
Supports: PR/FAQ is separated from an announcement by PURPOSE and place in the timeline: PR/FAQ is a pre-build decision/vetting narrative used to decide WHETHER and WHAT to build, written as if the product already existed; an announcement communicates a decision already made about something real, live or about to go live.
Quotable: "Working Backwards is a systematic way to vet ideas and create new products. Its key tenet is to start by defining the customer experience, then iteratively work backwards from that point until the team achieves clarity of thought around what to build."
Quotable: "Normally, writing a press release is the last step in launching a new product. ... Writing a press release is a forcing function to ensure that the creator of the new product idea is focused on the customer."
Quotable: "The next section is the internal FAQs. A well-written internal FAQ section anticipates the most important questions that senior leaders and stakeholders in the company will ask after reading the PR."
Quotable: "The PR/FAQ process is used appropriately at the beginning of the new product development process. Once the PR/FAQ is finalized and approved, the Agile process can be employed to build the product."
Quotable: "At some point, a level of completion of the PR/FAQ document is reached, and a go, no-go decision can be made."

**[12] Prosci (Tim Creasey), "Communications Checklist for Change Management".** practitioner. **fetched-and-verified.**
`https://www.prosci.com/blog/communications-checklist-for-change-management`
Supports: A change-management communications PLAN is a different artifact than a single internal announcement by PURPOSE and SCOPE: the plan is the standing strategy (audiences, senders, cadence, channels across the whole change lifecycle) that governs and schedules many messages aimed at adoption; an announcement is one message. The dominant boundary the source itself draws is 'telling' (broadcasting what happened) versus 'communicating' (answering why the change is happening and what it means for the reader), which maps directly onto the announcement-vs-status-report distinction the bundle needs. Ten named practices a change-management communication should include beyond a bare announcement: preferred senders, leading with why/why-now/risk-of-inaction, WIIFM, repetition, avoiding project-team-only senders, multi-channel and face-to-face delivery, two-way feedback channels, and post-communication effectiveness evaluation. That the project team is the wrong sender for every message.
Quotable: "Use the checklist as a guide to develop your Communications Plan for new change initiatives and projects."
Quotable: "The first communications about a change should always focus on: 1) Why the change is happening, 2) Why it's happening now, and 3) The risk of not changing."
Quotable: "Communications serve an important purpose in project management and other processes, but change management communications differ from these communications in significant ways."
Quotable: "A communications plan that is not part of a bigger change management approach usually won't produce positive results toward managing the people side of change. Instead, such plans result in a telling plan rather than a communications plan."
Quotable: "Communicating during change is not a single event that ends when you press "send.""
Quotable: "The first communications about a change should always focus on: 1) Why the change is happening, 2) Why it’s happening now, and 3) The risk of not changing."
Quotable: "WIIFM stands for “What’s in it for me?” It’s a question people always ask during change, even when the change seems positive."
Quotable: "Preferred senders should repeat key messages five to seven times"
Quotable: "Create opportunities for two-way communications"
Quotable: "Evaluate the effectiveness of your communication messages"
Quotable: "One of the biggest and most common mistakes you can make is to have your project team sending all the communications"

**[13] PagerDuty, "Internal Stakeholder Communications Guide" (Definitions, Mechanisms, and Templatizing communications pages).** vendor. **fetched-and-verified.**
`https://stakeholders.pagerduty.com/`
Supports: PagerDuty's guide separates incident stakeholder comms from an announcement by SCOPE and TRIGGER, not by audience: it is explicitly bound to major incidents (an unplanned, ongoing, evolving event with an Internal Liaison role, incident-alert channels, and per-incident status pages), producing repeated status pushes over the life of one incident rather than a single message about a completed or scheduled change.
Quotable: "This term is used to encompass the communications and notifications sent only to your internal teams that provide proactive updates regarding the status of major incidents."
Quotable: "The Internal Liaison is the person responsible for managing internal stakeholder communication ... during a major incident."
Quotable: "In order to be effective during an incident, internal stakeholder communications must be both accurate and fast. Templatizing and automating notifications ahead of a major incident can help you move fast and minimize errors."
Quotable: "Incident detail placeholders may include things like: When the incident began ... What impact the incident is having on customers (if known)"
Quotable: "Status pages are used to inform stakeholders about any service disruption, whether it is an unplanned outage or regularly scheduled maintenance."

**[14] LogRocket (Aniket Parihar), "Don't ship blind: A practical checklist for internal launch readiness".** practitioner. **fetched-and-verified.**
`https://blog.logrocket.com/product-management/practical-checklist-internal-launch-readiness/`
Supports: Launch readiness is a PM-facing, multi-workstream PROCESS/tracking artifact (narrative + champions + training + pre-mortems + an owner/status checklist) that precedes and prepares for a launch; the checklist itself is a project-management tool with owners and statuses, not a communication sent to the org, and the 'shared narrative' one-pager it produces is raw material an announcement might draw on rather than the announcement itself.
Quotable: "Before launching an internal product, it's important that you do the groundwork to set your launch up for success. In my experience, there are four key pillars that signal you're ready for launch"
Quotable: "Talk to the users, understand their problems, prioritize the problems, pick the highest-impact one, and write a one-pager that explains the "why" in plain language."
Quotable: "Launching an internal product is more than flipping the switch. That's why I created this checklist that lists all the steps a PM should consider before, during, and after the launch"
Quotable: "Internal readiness is critical. You're not just shipping a tool; you're changing the workflow of people, affecting their daily work life."

**[15] GitLab Docs, "Release notes" (documentation contribution process).** vendor. **fetched-and-verified.**
`https://docs.gitlab.com/development/documentation/release_notes/`
Supports: Describes the release-note artifact's format constraints (125 words or fewer, one feature per note, no images) and its authorship path (product manager drafts, technical writer reviews, merged into a dated index tied to a specific numbered release). This is evidence of WHAT a release note structurally is, not a stated boundary against announcements; GitLab's page never contrasts release notes with an internal announcement, so no purpose-based boundary claim rests on it.
Quotable: "Use 125 words or fewer, and no images or videos."
Quotable: "Explain the value of this improvement with 125 words or fewer. Use phrases that start with, "In previous versions of GitLab, you couldn't... Now you can...""

**[16] Pete Winter (Partner, Tomorrow People) - "Product Launch Do's and Don'ts for Internal Teams".** vendor. **fetched-and-verified.**
`https://tomorrow-people.com/insights/internal-product-launch/`
Supports: Names, as explicit don'ts: burying the most relevant information ('avoid burying the most relevant information with the generic bits'), overusing jargon that other departments and eventually customers won't understand, relying on a single communication channel (broadcasting), and briefing stakeholders too late relative to the external launch.
Quotable: "avoid burying the most relevant information with the generic bits"
Quotable: "It's no secret - product marketing teams use a lot of jargon. Unfortunately, this doesn't necessarily translate well to other departments."
Quotable: "it's important to broadcast your message using a variety of communication channels"
Quotable: "you should leave enough time between your internal and external launch so you can set realistic milestones for each department"

**[17] tchop glossary - "Notification fatigue in internal communication".** vendor. **fetched-and-verified.**
`https://tchop.io/resources/glossary/internal-communication/notification-fatigue`
Supports: Names notification fatigue directly as a failure mode: too many alerts train people to ignore all of them, including the important ones; ties it to Herbert Simon's attention-scarcity framing and Gloria Mark's interruption-cost research.
Quotable: "Notification fatigue is the exhaustion and desensitisation people feel when they receive too many alerts. Once every message pings, none of them feel urgent, so people mute channels, swipe notifications away without reading, or miss the one update that actually mattered."
Quotable: "a wealth of information creates a poverty of attention"
Quotable: "after a single interruption a worker takes an average of 23 minutes and 15 seconds to return to the original task at full focus"
Quotable: "When people are fatigued, the important message, the safety alert, the deadline change, gets treated exactly like the noise around it."

**[18] Vicki Young (Founder/CCO, Nalla) - "Internal vs External Brand Launch: Why Order Matters".** vendor. **fetched-and-verified.**
`https://nalla.co.uk/internal-external-brand-launch-order/`
Supports: Directly argues internal-first sequencing as the load-bearing claim of the piece ('Internal precedes external. It does not run alongside it'), and separately names broadcasting-without-context as a failure mode distinct from message-carrying leadership. Cites McKinsey (70% of large-scale change programmes fail, commonly for lack of internal engagement) and Gallup (41% of employees can articulate what their company stands for) as backing, though I did not read those primary reports myself - they are this source's own citations, not independently verified by me.
Quotable: "Internal precedes external. It does not run alongside it."
Quotable: "This is the single most important sequencing decision, and most companies get it wrong."
Quotable: "Leadership act as messengers, not broadcasters. There's a difference between announcing a brand and carrying it. Broadcasting is a video and a slide deck."
Quotable: "They learn about the new brand at the same moment as the market, or worse, from a customer asking a question they can't answer."
Quotable: "roughly 70% of large-scale change programmes fail to meet their goals"
Quotable: "only 41% of employees strongly agree they know what their company stands for and what makes its brand different"

**[19] SHRM Online - "No More 'Tiger Teams' and 'Idea Showers': Nix the Business Jargon in Employee Communications" (quoting Eloise Leeson-Smith, linguist, and citing Robert Sutton, Stanford Graduate School of Business).** practitioner. **fetched-and-verified.**
`https://www.shrm.org/topics-tools/news/employee-relations/business-jargon-employee-communication-barriers`
Supports: A stronger-tier (HR professional association, not a marketing agency) source naming jargon as a named failure mode with a specific mechanism: it disempowers employees from asking clarifying questions and excludes them, and Sutton's term 'jargon monoxide' names vague/anesthetizing corporate language used to avoid being straightforward.
Quotable: "If employees do not feel empowered to ask questions, then they are left unsure of what is being asked of them and are not confident to have these conversations with their senior colleagues"
Quotable: "Corporate jargon is all too common in the workplace but can be exclusionary and leave employees feeling left out, creating barriers between them and their colleagues"
Quotable: "He called the “anesthetizing” language “jargon monoxide.”"
Quotable: "Business jargon does more than annoy workers. It obstructs communication and undermines productivity and culture at businesses."

**[20] Sean Devlin (editor, Ragan Communications), quoting Lisa Claybon (VP Corporate Affairs, unnamed global foodservice company) and Lauren Stephens (Executive Director of Internal Communications, MGM Resorts International) - "A practical guide to fatigue-proof internal comms cascades".** practitioner. **fetched-and-verified.**
`https://www.ragan.com/a-practical-guide-to-fatigue-proof-internal-comms-cascades/`
Supports: A trade-press source (stronger tier than a marketing-agency blog) directly naming the mechanism of internal-comms fatigue with a named practitioner quote: fatigue is caused by unintentional, uncontextualized cascading, not by volume per se, and applying an announcement cascade where none is warranted risks fatiguing the audience.
Quotable: "When everything feels like a major announcement, nothing feels important."
Quotable: "Comms fatigue usually builds in the background through ignored messaging and disengaged audiences."

**[21] ChangeEngine - "Top 10 Internal Communication Fails (and What You Can Learn From Them)" (article title undercounts; it lists 16 numbered fails).** vendor. **fetched-and-verified.**
`https://www.changeengine.com/articles/10-internal-comms-fails`
Supports: Closes a named gap from the earlier pass: 'no call to action' appears here as a NAMED FAILURE ('Fail 11: Leaving Out The Call To Action'), not only as a fix. Also independently names jargon/wall-of-text writing (Fail 3), announcing decisions without explaining why (Fail 4, a burying/context failure), and treating managers as forwarders rather than meaning-makers (Fail 9, a broadcast-vs-conversation failure), plus a closing line naming internal communication's function against pure broadcast.
Quotable: "Fail 11: Leaving Out The Call To Action"
Quotable: "What it looks like: a detailed update ends with no clear next step. People feel informed but not activated."
Quotable: "Why it hurts: information without action is a courtesy, not a catalyst."
Quotable: "Fail 9: Treating Managers As Forwarders, Not Meaning-Makers"
Quotable: "corporate sends a memo and asks managers to “cascade.” Managers forward the email and move on. Their teams ask peers for clarity instead."
Quotable: "Internal communication is not a broadcast function. It is how your organization coordinates attention and action."
Quotable: "a 600-word Slack post with acronyms in every sentence"

**[22] ChangeEngine glossary - "What is Message Fatigue?".** vendor. **fetched-and-verified.**
`https://www.changeengine.com/glossary/what-is-message-fatigue`
Supports: Used only to confirm the known gap: the industry's named term for this failure mode is 'message fatigue' (and, elsewhere, 'change fatigue'), not 'announcement fatigue' - I found no source using 'announcement fatigue' as a term of art.
Quotable: "Message fatigue is a state of weariness and resistance that builds when people feel overexposed to repetitive, frequent, or overly persistent messages."
Quotable: "Workplace comms: policy updates, security prompts, compliance training, tool notifications."

**[23] Jake Brereton (LaunchNotes) - "How to Time a Feature Announcement So Every Channel Reinforces the Last".** vendor. **fetched-and-verified.**
`https://www.launchnotes.com/blog/feature-announcement-timing`
Supports: A product-marketing vendor source (stronger than a generic marketing-agency post in that it is specific to product/feature announcements and prescribes an explicit internal-first sequence with a named failure mode and recovery step) naming 'announcing before the people who must support it are ready' as a sequencing failure, distinct from a knowledge failure, and prescribing internal briefing as step 1 of the announcement sequence before changelog, email, or in-product messaging. Sequencing rule that internal (support/CS/sales) briefing must precede any external/public channel; a briefing-content spec (outcome, segment, plans, known limitations); a rule that sales only gets briefed when the release has prospect-facing relevance; and tiering the announcement (breadth of impact, magnitude of workflow change, plan availability) to decide how much internal lead time and ceremony a release earns.
Quotable: "support, customer success, and sales know what shipped before any public channel fires, because a customer-facing team hearing about a feature from a customer is a failure of sequencing rather than of knowledge"
Quotable: "If internal teams were not briefed before the announcement went out, send the briefing now with an explicit note that inbound questions have already started, and give support a holding response they can use accurately while they read it."
Quotable: "The step is done when the teams have confirmed receipt, not when the message was posted."
Quotable: "The briefing is short and covers four things: the customer outcome in one sentence, the segment receiving the announcement, the plans the feature is available on, and the limitations you already know about."
Quotable: "Sales gets the briefing when the feature has prospect-facing relevance, which is a real filter rather than a courtesy, because a pipeline team that receives every release update stops reading them."
Quotable: "Three inputs decide the tier. Breadth of user impact tells you how much of the base is affected. Magnitude of workflow change tells you whether someone has to learn something new... Plan availability tells you how narrow the audience actually is"

**[24] AnnounceKit - "Internal vs. External Changelog: Why You Need Both".** vendor. **fetched-and-verified.**
`https://announcekit.app/blog/internal-vs-external-changelog-and-why-you-need-both/`
Supports: Supports the 'separate documents' position on the internal-vs-external debate for the closely related changelog/release-notes artifact: internal and external logs are treated as two artifacts with different audience, content, and language, each necessary and neither able to substitute for the other.
Quotable: "Most successful SaaS teams use both: the internal changelog keeps engineers aligned, while the external changelog builds customer trust and transparency."
Quotable: "A development team relying only on the external changelog loses the technical depth they need to debug and ship confidently. A customer reading only the internal changelog would be lost in jargon and irrelevant implementation details."
Quotable: "your internal changelog represents the “how” and your external changelog represents the “what” and “why” for your users"

**[25] Tim Creasey (Prosci Chief Innovation Officer) - "Why Some Communications Work and Others Don't".** vendor. **fetched-and-verified.**
`https://www.prosci.com/blog/understanding-why-some-communications-work-and-others-dont`
Supports: Preferred-sender principle: business-level change messages should come from senior leadership/the person in charge, personal-impact messages should come from the direct supervisor, and NOT from the project team. Also supports that face-to-face is Prosci's stated most-effective mode, and that people need to hear from these senders before they are receptive to the project team's 'what and when' details.
Quotable: "they don't want to hear about project changes from the project team. Instead, they prefer to receive specific messages from the person in charge and their direct supervisor."
Quotable: "When it comes to messages about change impacts on the business or the organization, people want to hear from the person in charge - typically a senior manager or executive."
Quotable: "People prefer to learn about change-related impacts to their own daily work from their manager"
Quotable: "communications from the project team about new processes, new systems, or the project schedule will fall on deaf ears until people have heard from preferred senders on the topics they care about most"
Quotable: "Prosci's research has shown that face-to-face communications are the most powerful and effective."

**[26] Interact Software (Sophie Hamblett, uncredited-byline blog) - "How to Choose the Best Internal Communication Channels".** vendor. **fetched-and-verified.**
`https://www.interactsoftware.com/blog/how-to-choose-the-best-internal-communication-channels/`
Supports: Channel selection is driven by five factors including audience size/scope: formality, urgency, confidentiality, size of audience, required response. Directly supports picking a broader-reach channel (digital signage, company-wide app) as scope/audience widens, and email/intranet for formal company-wide announcements.
Quotable: "The size of your audience significantly impacts the efficiency and reach of your chosen communication channels. For larger groups, employing communication platforms that can efficiently disseminate information to everyone simultaneously becomes crucial."
Quotable: "Digital signage and company-wide employee apps present themselves as excellent options in this scenario."
Quotable: "For those formal announcements or policy updates that require a corporate tone, consider leveraging internal communication channels such as email or the secure company intranet."
Quotable: "If a response is required from a smaller group, then you may wish to share it via a channel on which recipients can respond easily. If the recipient group is larger, you may wish to manage the incoming traffic ... by providing a link to a form"

**[27] Lauren Kersanske (Crayon) - "How to Master Internal Communication for Your Next Product Launch" (quoting Annum Munir, Product Marketing Manager, Google Cloud).** vendor. **fetched-and-verified.**
`https://www.crayon.co/blog/your-next-product-launch`
Supports: A stakeholder-tiered messaging model (sales gets scripts/soundbites, marketing gets external-comms detail, executives get high-level summary with drill-down option, product gets everything) and a channel rule that time-critical changes (e.g., launch-date slips) go by email first with chat as a supplement, not chat alone. Also supports staggered timing: sales briefed early at a lighter level (standup mention), then deeper training closer to launch.
Quotable: "sales doesn't need to know every single detail of the launch months in advance. Perhaps your initial sales communication is during a standup meeting, and then closer to launch, you conduct internal training where you dive into more detail"
Quotable: "Executives: High-level detail on features and messaging, and overall launch plan. Provide options to seek more detail if desired."
Quotable: "if you have something critical to communicate regarding the launch (e.g., change of launch date), it's best to use email and then Slack as a supplement to that communication"
Quotable: "Sales needs the most contextualized, explicit information out of any of your audiences... provide verbatim soundbites and scripts so sales can speak to prospects in an informed manner."

**[28] Cristina Hure (ContactMonkey) - "How To Create An Internal Comms Channel Matrix".** vendor. **fetched-and-verified.**
`https://www.contactmonkey.com/blog/internal-communication-channel-matrix`
Supports: A channel-matrix method that maps channel to purpose, audience segment (department, role level, location, deskless-vs-desk), owner, frequency and feedback direction, as the mechanism for deciding channel/sender/audience together rather than ad hoc, and an explicit warning against forgetting frontline/deskless employees.
Quotable: "the most effective internal communication channel matrix ensures that messages reach the right audience, through the right channel, at the right time"
Quotable: "Different roles, locations, and levels of digital access require different messaging approaches."
Quotable: "Forgetting frontline or non-desk employees: These groups often get left behind - ensure you have mobile-friendly, accessible channels."

**[29] Axios HQ Insights (unsigned) - "Reinforce, not repeat: Smart ways to cascade key internal updates".** vendor. **fetched-and-verified.**
`https://www.axioshq.com/insights/its-reinforce-not-repeat-a-smarter-way-to-cascade-essential-information-around-your-organization`
Supports: A role-by-role cascade model (founder/CEO -> executives/dept leaders -> team/people managers -> individual contributors) where each layer adds locally relevant context rather than repeating the message verbatim, i.e. the manager-cascade mechanism for reaching everyone after an initial announcement.
Quotable: "executives and managers cannot rest on merely repeating the same ideas and information verbatim at every level. It's about finding ways to harness top-level directives, reinforce key details about them, and infuse critical, custom details each area of the business needs"
Quotable: "Team and people managers communicate up to department leaders and down to the employees who report to them directly... Their communications need to translate department-level priorities into practical and actionable projects."
Quotable: "Don't merely repeat. Synthesize, customize, and reinforce."

**[30] Jamie Bell (Workshop) - "Reaching and changing frontline employees: the 2026 edition" (restating Larkin & Larkin, HBR 1996).** vendor. **fetched-and-verified.**
`https://useworkshop.com/blog/reaching-and-changing-frontline-employees/`
Supports: A secondary (vendor) restatement of the Larkin & Larkin HBR argument that the best ways to reach frontline employees during major change are face-to-face and through their own supervisor, plus a practical point that frontline/deskless staff often lack corporate email or intranet access, so email-first sequencing that assumes desk access misses them. This is a restatement, not a read of the original HBR argument (see referenced HBR entry below).
Quotable: "The best ways to reach a frontline employee during a big change is 1.) face-to-face, and 2.) through their supervisor. On this, we completely agree with the Harvard Business Review article"
Quotable: "A report by Atlanta-based communications agency, Tribe, indicated that 83% of "non-desk employees" don't have a corporate email address and 45% don't even have access to the company intranet when at work."
Quotable: "these kinds of changes are only really happening every 5-10 years"

**[31] T.J. Larkin and Sandar Larkin - "Reaching and Changing Frontline Employees", Harvard Business Review, May-June 1996.** primary. **fetched-and-verified.**
`https://hbr.org/1996/05/reaching-and-changing-frontline-employees`
Supports: Only the paywalled article's free lead paragraph was readable: it establishes the article's stance that conventional 'more communication from executives' advice is wrong. It does NOT itself supply the supervisor/face-to-face claim in readable form here - that claim is carried by the Workshop restatement above, and this entry exists to keep that attribution honest rather than to source the argument's substance.
Quotable: "Most advice given to executives about communicating change is wrong. The advice usually boils down to more: more values, missions, and vision; more videos, publications, and meetings; more executive road shows. This communication is not working. Why would anyone want more of it?"

**[32] Haystack (unsigned, company blog) - "How to Communicate New Policies to Employees".** vendor. **fetched-and-verified.**
`https://www.haystackteam.com/blog/how-to-communicate-new-policies-to-employees`
Supports: A specific, numeric general-practice notice-period claim for internal policy/process changes: at least two weeks for major changes affecting daily routines or benefits, one week for minor updates, up to 30 days for changes touching compensation or working conditions. This is offered as this vendor's general guidance, not a named company's house rule.
Quotable: "Give employees at least two weeks' notice for major policy changes, especially those affecting daily routines, benefits, or compensation. One week is reasonable for minor updates. Complex policies that affect pay or working conditions may warrant 30 days."
Quotable: "Timing and sequencing matter: managers need advance notice before the organization-wide announcement."

**[33] Hourly, Inc. (unsigned) - "How to Notify Employees of Policy Changes + Free Template".** vendor. **fetched-and-verified.**
`https://www.hourly.io/post/notifying-employees-of-policy-changes`
Supports: General practice that advance notice of policy changes is good HR practice, particularly for changes with direct employee impact (e.g., PTO), and that multi-channel notification plus a grace period before enforcement is recommended. Does NOT contain a specific day/week number - checked and confirmed absent from the body despite an initial search-engine summary suggesting one.
Quotable: "Providing advance notice of any changes to existing policies is a good HR practice, particularly for policies that have a direct impact on employees"
Quotable: "Keep in mind that certain policy changes can (and should!) require a grace period before they're fully enforced."
Quotable: "It's best to use multiple different channels to update your team members about changes so no one slips through the cracks."

**[34] Parsa Mohamadi (Manifestly) - "Preparing Sales Teams for a Successful Product Launch".** vendor. **fetched-and-verified.**
`https://www.manifest.ly/blog/preparing-sales-teams-for-a-successful-product-launch/`
Supports: Nothing specific in this bundle. Generic SEO content that mostly links out to other vendors' guides (Showpad, Alexander Group, Qualtrics, etc.) without itself stating a channel, sender, or timing rule beyond restating that customer-facing teams need training before launch. Listed because consulted.

**[35] Lawrence Chapman (Product Marketing Alliance) - "How to create a product launch internal communication plan", quoting Jasmine Jaume (Intercom) and Rene Kardtke (Ontic).** vendor. **fetched-and-verified.**
`https://www.productmarketingalliance.com/the-importance-of-internal-communication-plus-how-to-crush-it/`
Supports: Naming which specific teams/roles are affected and why it matters to each of them, plus a defined cross-functional distribution/notification list run through an owning process, as opposed to one undifferentiated company-wide blast.
Quotable: "knowing who that's going to impact, being able to consider which teams need to know about it, and then being able to communicate messages clearly and concisely to people so they know A) why it’s important to them, and B) why they should care about it"
Quotable: "We inform multiple teams, including marketing, revenue/sales, customer service team leadership, sales ops, sales enablement, support, and pro services, as well as finance."
Quotable: "we have a cross-functional NPI process - New Product Initiative led by a project management function. JIRA tracking and regular meetings. The NPI process clearly defines responsible parties and deliverables."

**[36] Brianna Susnak, Employee Communications Manager, Salesforce - "The Change Management Playbook for Major UI Rollouts" (Slack blog, 'How Salesforce's Internal Comms team turned skeptics into advocates when Slack's Activity tab got a redesign').** practitioner. **fetched-and-verified.**
`https://slack.com/blog/transformation/change-management-playbook-ui-rollouts`
Supports: A pre-existing trusted broadcast channel built before the change, advance heads-up timing, visual proof (screenshots/demo video/GIF/how-to guide), a named accountable person answering questions live in-thread, deliberately non-compliance tone, a planned follow-up message tied to a real use case, audience-segmented tips, and an explicit answer to 'can I revert/opt out' - versus a single one-shot text announcement.
Quotable: "We aim to communicate at least one business day before the change goes live. This gives employees enough time to absorb the information without so much time that they forget."
Quotable: "Visual previews, like screenshots, short demo videos, or GIFs, help people see what’s coming. We included a demo video from the product manager as well as a how-to guide."
Quotable: "The product manager jumped in thread to explain the reasoning, address the feedback, and continue building excitement."
Quotable: "Keep the tone conversational and reassuring. This isn’t a compliance mandate; it’s a helpful heads-up from a colleague."
Quotable: "Employees need more than “here’s what’s new.” They need “here’s why this matters to you.”"
Quotable: "Multiple entry points: We acknowledged different working styles. “Sidebar zero” people got tips on clearing notifications, while deep-focus workers discovered how to filter by specific channels or sections"
Quotable: "Managing change for internal product rollouts isn’t a one-time announcement. It’s an ongoing conversation."
Quotable: "your employees aren’t resistant to change. They’re resistant to unmanaged change."

**[37] Wendy Hirsch - "How to communicate change in an organization - six key practices".** practitioner. **fetched-and-verified.**
`https://wendyhirsch.com/blog/checklist-for-change-communication`
Supports: A five-message framework (need, change solution including what's NOT changing, organizational capability/support, commitment/priority, personal impact including negative impacts) drawn from change-readiness research, plus transparency about unknowns with a committed next-update date, matched messenger-to-message, multi-channel repetition, informal sense-making time, and post-hoc measurement of communication effectiveness.
Quotable: "What is “the change” (e.g., policy, org structure, system, practice, etc.)? Why have you chosen it? How was the decision made? What’s fixed and what’s flexible? What’s not changing?"
Quotable: "What is the plan for the change? Who is leading the effort? What support will be provided to individuals, teams, and managers?"
Quotable: "How high a priority is this change compared to other efforts? How is the change being resourced?"
Quotable: "Be transparent about what you don’t know (and be sure to confidently state what you do know.) Clarify what you are doing to get more information. Let people know when you will update them again."
Quotable: "Aligning the messenger to the message is a best practice change communications strategy."
Quotable: "It's not enough to share a lot of information as part of your change management approach. You also need to engage with staff who are impacted by change initiatives to understand their perspectives, hear their feedback and acknowledge their concerns."

**[38] UK Cabinet Office / Government Communication Service, "GovS 011: Communication", Version 2.1 (October 2023).** standards. **fetched-and-verified.**
`https://assets.publishing.service.gov.uk/media/6576d36c48d7b7000d57ca0d/GovS_011-_Communication_Version_2.1.pdf`
Supports: That the UK government functional standard names announcements only as an activity within the communication function and requires an internal communication strategy, not an announcement document. Crown copyright, Open Government Licence.
Quotable: "Communication, in the context of this functional standard, includes announcements, media management, coordinated communication activities"

**[39] Headquarters, Department of the Army, "AR 25-50: Preparing and Managing Correspondence" (major revision 10 October 2020, administrative revision 4 October 2024).** primary. **fetched-and-verified.**
`https://armypubs.army.mil/epubs/DR_pubs/DR_a/ARN42124-AR_25-50-007-WEB-13.pdf`
Supports: The memorandum form, which the catalog lists as an alias of this type ("internal memo"), opens with its purpose and then the main point. NOT counted for admission (it would be the library certifying itself through its own alias), and NOT a source for "bottom line up front": the current edition contains neither the phrase nor the acronym.
Quotable: "Begin the memorandum with a short, clear purpose sentence."
Quotable: "Put the recommendation, conclusion, or most important information (the main point) next."

**[40] Headquarters, Department of the Army, superseded 2013 edition of AR 25-50, "Preparing and Managing Correspondence" (major revision 17 May 2013, administrative revision 6 July 2015), mirrored by Fort Leonard Wood.** primary. **fetched-and-verified.**
`https://home.army.mil/wood/application/files/3015/5751/8343/AR_25_50_Army_Correspondence.pdf`
Supports: That the superseded 2013 edition of AR 25-50 did carry "bottom line up front", which the current edition [39] does not. Cited only for that history; this edition is not in force.
Quotable: "point at the beginning of the correspondence (bottom line up front) and using the active voice"
Quotable: "This administrative revision, dated 6 July 2015"
