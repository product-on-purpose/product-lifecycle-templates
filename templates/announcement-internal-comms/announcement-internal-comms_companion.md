# Companion: Announcement / Internal Comms

> The deep explainer for the Announcement / Internal Comms bundle. Read this to understand what an
> internal announcement is, where its shape comes from, and where the evidence runs thin. The short
> operator card is `announcement-internal-comms_guide.md`; a worked instance is
> `announcement-internal-comms_example.md`. Inline citations like [[1]](#ref-1) resolve to the
> [References](#references), tagged by source reliability.

---

## 1. Orientation

An internal announcement tells the people in an organization who did not do the work that something is
launching or changing: an organizational announcement "shares important updates with employees across a
company" [[1]](#ref-1). Its one job is to translate a decision already made into what it means for a
reader who was not in the room: what is changing, why, what it means for them, and what, if anything, they
must do, then point them at the artifact that carries the underlying facts rather than restate those facts
itself.

**Read this honestly.** No standards body, government communication function, or professional institute
publishes this document by name. This bundle's admission rests on three sources, all vendor or
practitioner tier: a vendor's blog that names and defines the type with worked templates [[1]](#ref-1), a
company handbook that prescribes what a company-wide announcement must carry [[2]](#ref-2), and a
practitioner's account of one company's named internal format for a shipped feature [[3]](#ref-3). Its
evidence on channel choice and timing is vendor and practitioner sources only; nothing here rises to a
standards-tier norm for a product launch.

**At a glance**
- Lead with the point a reader can act on, not with the surrounding context [[6]](#ref-6)[[7]](#ref-7).
- Say what changes for this specific reader, including what does not change, and what they must do and by
  when, or say plainly that there is nothing to do [[5]](#ref-5)[[1]](#ref-1)[[21]](#ref-21).
- Put a known issue in front of the people who support the product before a customer surfaces it for them
  [[3]](#ref-3)[[23]](#ref-23).
- Link to the source of truth rather than restating it, so the announcement cannot drift from the record it
  summarizes [[2]](#ref-2).
- Its sibling by purpose is `release-notes`, not the reader's employment status: the line between them is
  what the message is for, not who reads it, and that line is this library's own (see
  [§6](#6-debates-and-contested-boundaries) and [§8](#8-relationships-to-other-artifacts)).

---

## 2. Origins and evolution

This type has no traceable formal origin and no standards-tier pedigree to trace. The UK government's own
communication function names announcements only as an activity within a broader function, never as a
document: "Communication, in the context of this functional standard, includes announcements, media
management, coordinated communication activities" [[38]](#ref-38). Prosci, the source this research found
most developed on the surrounding practice, publishes communication *plans* and *checklists* for change
initiatives, never the announcement itself [[12]](#ref-12)[[25]](#ref-25).

What exists instead is a small set of named, current practice: a vendor's blog defines the type by name and
ships seven worked templates sharing one shape, one of them a product launch, with its own caveat: "These
templates are a starting point, not a one-size-fits-all solution." [[1]](#ref-1) A company handbook
prescribes what a company-wide announcement covers and where it lives [[2]](#ref-2); and a named
practitioner describes a real internal format, Basecamp's "Deployment" post, written by one of the people
who did the work when a feature ships [[3]](#ref-3).

**The type's alias points at an older written form this research did not count toward admission.** The
catalog lists "internal memo" as an alias, and the closest thing to a canonical shape for an internal memo
is Purdue OWL's segmented structure: a heading, an opening that states the purpose briefly up front, context,
a task statement, an optional summary for a longer memo, discussion ordered from most to least important,
and a closing that states the requested action [[8]](#ref-8). The US Army's current correspondence
regulation opens a memorandum with "a short, clear purpose sentence" and puts "the recommendation,
conclusion, or most important information" next [[39]](#ref-39). Neither is counted toward this bundle's
admission: crediting a source only for matching the catalog's own alias would be this library certifying
itself. And the regulation is **not** the source of "bottom line up front", a phrase and acronym often
attributed to it: the current 2020/2024 edition of AR 25-50 contains neither [[39]](#ref-39); the superseded 2013 edition did
[[40]](#ref-40). The lead-first principle here is sourced instead to the inverted pyramid [[6]](#ref-6) and to the
newspaper "lede" [[7]](#ref-7).

---

## 3. Anatomy (section by section)

The template is a single size. Frontmatter, not a body section, carries the audience, the channel, and the
send date: a company handbook gates its company-wide channel by reach ("Is this relevant to all team
members globally?") and states a lead-time norm, "ideally 72 hours (at minimum 24 hours) in advance of a due
date" [[2]](#ref-2), which is that company's own house rule, not a general norm (see
[§6](#6-debates-and-contested-boundaries)). Frontmatter also carries the sender, because who sends the
message is contested (below) and the bundle asks the author to choose deliberately rather than default to
whoever is drafting.

**Headline.** One line a reader can act on without opening the rest of the document. *Why:* readers should
get the main point "regardless of how much they read" [[6]](#ref-6), and every one of the vendor's seven
worked templates opens with a subject line playing this role [[1]](#ref-1). *The trap this section exists
to prevent:* burying the lede, so that "the newsworthy part of a story fails to appear at the beginning,
where it's expected" [[7]](#ref-7), and the related instruction to "avoid burying the most relevant
information with the generic bits" [[16]](#ref-16).

**What Is Changing, and When.** The launch or change itself, who it applies to, and the date it takes
effect. *Why:* a company handbook's prescribed content covers "What, Why, Who, When, Where" [[2]](#ref-2),
and a structured internal-comms play opens the same way, asking "What's changing? What will be different
from the way it is today?" [[5]](#ref-5).

**Why It Matters.** The reason for the change, in terms the reader can use, not the reason it mattered to
the team that shipped it. *Why:* the same play asks "Why is this change happening now? Why is this change
important?" [[5]](#ref-5). *The trap:* jargon that travels within the team that built the change but not
past it. A vendor's guidance is direct, "Use plain language and avoid corporate jargon" [[1]](#ref-1), and
so is a marketing agency's: "product marketing teams use a lot of jargon. Unfortunately, this doesn't
necessarily translate well to other departments" [[16]](#ref-16).

**What It Means for You.** What changes for this specific audience, what does not change, and what they
must do and by when, if anything. *Why:* the same play asks "How will this change impact them?"
[[5]](#ref-5); the vendor's checklist names "what they need to do (if anything)" as content a reader needs
[[1]](#ref-1); and Basecamp's Deployment post is written so that it is useful to "those on the front lines
too" [[3]](#ref-3). This section also carries what is *not* changing, on a practitioner's checklist question
"What's not changing?" asked as part of describing a change [[37]](#ref-37), and Prosci's framing of
communication around the reader's own stake, “What’s in it for me?” [[12]](#ref-12).

**Known Issues.** What could go wrong, or is not finished yet, stated here before a customer-facing
colleague hears it from a customer. *Why:* a Deployment post exists partly to explain what shipped and
"points out what could be an issue" [[3]](#ref-3), and a sequencing failure this research names directly is
a customer-facing team
"hearing about a feature from a customer", which is "a failure of sequencing rather than of knowledge"
[[23]](#ref-23). Where this overlaps `release-notes`' own Known Issues content, this section links there
rather than restating it, following the link-do-not-restate design rule below.

**Where to Learn More.** The source of truth, and a named person to ask. *Why:* the handbook's own
instruction is direct: "The majority of information should still be in the Handbook which you include links
to." [[2]](#ref-2) The vendor's checklist names a linked resource and a named contact as ways to reduce
confusion [[1]](#ref-1). This section also carries a commitment to when the next update comes, on the same
practitioner's instruction: "Let people know when you will update them again." [[37]](#ref-37)

**The rule the whole shape owes the most to its sources: link, do not restate.** The instruction is
GitLab's: keep the detail in the linked source rather than in the announcement [[2]](#ref-2). That doing so
also stops an announcement drifting out of step with the release notes or the PRD it summarizes is this
library's own reasoning; no source read for this bundle names that drift as a failure. That every fact in the
document should trace to an upstream artifact is this library's own extension of that instruction, not a
sentence any source states in those words.

---

## 4. Variants and sizing

**One size, and the evidence argues against a second.** The vendor's seven worked templates share a single
shape, a subject line, a salutation, and three or four sentences, and its highest-stakes examples differ
from the rest of the set by one sentence rather than by an added section [[1]](#ref-1). The material a full variant might plausibly add, a leadership quote or a
linked FAQ, appears on that same page only as optional best practice, "Involve leadership" and "Link to
FAQs or additional resources" [[1]](#ref-1), never as a section inside any of the seven templates
themselves. A full variant built from that material would be an invention of this library rather than a
documented practice, so none is proposed here. Treat the single size as provisional rather than settled: it
follows from the strongest source this research found, not from a wider survey of longer internal
announcements.

---

## 5. Methodology lineage

This research found no school of practice, agile, regulated, or otherwise, that treats the internal
announcement as its own named artifact with its own doctrine. The type reads as methodology-agnostic:
nothing in the sources ties its form to Scrum, SAFe, or any other named process. What the sources do show is
several adjacent, better-documented practices that this document is not:

- **Change management's communications plan.** Prosci treats communication during a change as an ongoing,
  multi-message program with its own senders, cadence, and channels across the life of the change
  [[12]](#ref-12)[[25]](#ref-25), of which a single announcement is one message, not the whole plan (see
  [§8](#8-relationships-to-other-artifacts)).
- **Amazon's Working Backwards.** The PR/FAQ borrows the announcement's press-release form for the opposite
  purpose in time: it is written before the decision, as "a forcing function to ensure that the creator of
  the new product idea is focused on the customer" [[11]](#ref-11). As its own guidance states, "Normally,
  writing a press release is the last step in launching a new product." [[11]](#ref-11) An internal
  announcement fires after the decision, not before it.
- **Incident response.** PagerDuty's internal stakeholder communications are bound to "the status of major
  incidents" [[13]](#ref-13); the boundary there is the trigger, an ongoing incident, not the purpose of the
  message.

---

## 6. Debates and contested boundaries

**Internal first, or one document for both audiences.** No source above vendor or agency tier settles this.
Three positions appear in the research. One document, in two parts: Amazon's PR/FAQ carries an External FAQ
followed by an Internal FAQ within a single document, but that document is written before the decision, not
after it [[9]](#ref-9)[[11]](#ref-11). Two documents, order unstated: a company handbook keeps internal and
external communication in separate sections without prescribing which comes first [[2]](#ref-2). Two
documents, internal first: a marketing agency argues "you should leave enough time between your internal
and external launch so you can set realistic milestones for each department" [[16]](#ref-16); a brand
consultancy states flatly, "Internal precedes external. It does not run alongside it" [[18]](#ref-18); and a
product-marketing vendor treats a customer-facing team "hearing about a feature from a customer" as "a
failure of sequencing rather than of knowledge" [[23]](#ref-23). The related changelog question splits the
same way: one vendor argues internal and external changelogs are two necessary, non-substitutable artifacts
[[24]](#ref-24). **No source above vendor or agency tier makes the internal-first claim,** and this
companion states that limit rather than resolve it.

**Who should send it.** The sources do not reconcile this, and may simply describe different messages
within one announcement. Prosci holds that the project team is the wrong sender for any message: "One of
the biggest and most common mistakes you can make is to have your project team sending all the
communications" [[12]](#ref-12). The business reason should come from a senior leader while the
personal-impact message should come from the reader's own manager: "People prefer to learn about
change-related impacts to their own daily work from their manager" [[25]](#ref-25). Launch practice instead
assumes the product or product-marketing team runs the briefing, tiered by audience: sales gets a script,
executives get a summary with room to drill down [[27]](#ref-27), and support and sales are briefed before
any public channel fires [[23]](#ref-23). Basecamp has "one of the people who did the work" write the
message directly [[3]](#ref-3). This is why frontmatter carries the sender as a deliberate choice rather
than a default (see [§3](#3-anatomy-section-by-section)).

**Face to face, or written first.** Prosci favors face-to-face delivery as its most effective mode
[[25]](#ref-25) and builds its checklist around change-management delivery generally [[12]](#ref-12); two
channel-selection sources instead treat email and the intranet as the default surface for a formal,
company-wide announcement [[26]](#ref-26). The difference may be one of scope, a change
management program against a routine channel choice, and no source in this research reconciles it.

**How much notice.** No general norm is sourced for a product launch, and every figure here is one
organization's or one vendor's own practice, not an established convention. A company handbook's window,
"ideally 72 hours (at minimum 24 hours) in advance of a due date" [[2]](#ref-2), is that company's house
rule, stated to protect team members outside its home time zone. A UI-rollout account from another company
states: "We aim to communicate at least one business day before the change goes live." [[36]](#ref-36) That,
too, is one company's own practice. A vendor's general guidance for policy changes, a different context from
a product launch, recommends roughly two weeks of notice for a major change, one week for a minor one, and
up to 30 days for a change touching pay or working conditions [[32]](#ref-32); this is offered as that
vendor's own general advice, not a named organization's practice, and it does not address product launches
at all. A second vendor, also writing about policy changes rather than launches, agrees only at the level of
principle: "Providing advance notice of any changes to existing policies is a good HR practice, particularly
for policies that have a direct impact on employees" [[33]](#ref-33), and separately recommends a grace
period before a change is enforced and multiple channels so no one misses the notice [[33]](#ref-33).

**One FAQ section, or a split internal and external FAQ.** Only the PR/FAQ carries a section split this way
[[9]](#ref-9). The vendor's templates list a linked FAQ only as optional best practice, never as a section
inside a template [[1]](#ref-1), which is why this bundle's own shape links to a source of truth
(§3's "Where to Learn More") rather than shipping a dedicated FAQ section.

**Two library boundaries, drawn here rather than quoted from a source.** First, the line between this type
and `release-notes` is purpose, not audience: `release-notes_companion.md` already recommends shipping the
full release notes to internal readers, so who reads it cannot be what separates the two. What separates
them is purpose: a release note is, in the source's own words, "Curated user-impact summary for a release,
written so customers and GTM teams know what changed and why it matters" [[10]](#ref-10), while this type
exists to say what a change
means for a specific reader and what they must do. No source draws that line in those words; it is this
library's own, made necessary by a shipped decision elsewhere in the family. Second, that an announcement
contradicting the release notes it summarizes is a documented failure mode is **not established by any
source read for this bundle**; it is this library's own reason for the link-do-not-restate rule in
[§3](#3-anatomy-section-by-section), not a practice anyone else has named as a failure.

---

## 7. Anti-patterns and failure modes

- **Burying the point.** The newsworthy fact arrives after the context that should have followed it
  [[7]](#ref-7), and the instruction to "avoid burying the most relevant information with the generic bits"
  names the same failure directly [[16]](#ref-16).
- **Jargon.** Language that travels within the team that shipped the change but not past it
  [[1]](#ref-1)[[16]](#ref-16). A stronger-tier source ties a specific mechanism to this failure: a reader
  who does not "feel empowered to ask questions" is left "unsure of what is being asked of them"
  [[19]](#ref-19), and jargon can leave employees "feeling left out, creating barriers between them and
  their colleagues" [[19]](#ref-19).
- **Posting where it gets lost.** A company handbook warns against relying on one low-visibility channel as
  "a sole location for important announcements", because "information might get lost or muted"
  [[2]](#ref-2).
- **Broadcasting instead of starting a conversation.** A vendor names the failure directly, "internal
  announcements feel more like broadcasts than conversations" [[1]](#ref-1); Prosci's parallel failure is
  producing "a telling plan rather than a communications plan" [[12]](#ref-12).
- **No call to action.** Named as its own failure, not only as a missing best practice: "Leaving Out The
  Call To Action", where "information without action is a courtesy, not a catalyst" [[21]](#ref-21).
- **Telling customers before the people who support them.** A customer-facing team hearing about a feature
  from a customer is named directly as "a failure of sequencing rather than of knowledge" [[23]](#ref-23),
  and echoed in the instruction to brief internally before broadcasting widely [[16]](#ref-16).
- **Spending the reader's attention carelessly.** Named directly as "notification fatigue", "the exhaustion
  and desensitisation people feel when they receive too many alerts" [[17]](#ref-17), and as the
  "attention economy" a company handbook asks authors to be mindful of [[2]](#ref-2). A related, distinctly
  named failure for repeated messaging is "message fatigue", "a state of weariness and resistance that
  builds when people feel overexposed to repetitive, frequent, or overly persistent messages" [[22]](#ref-22).
  A trade-press source ties the mechanism specifically to treating too much as equally urgent: "When
  everything feels like a major announcement, nothing feels important." [[20]](#ref-20)
  **"Announcement fatigue" is not a term any source in this research uses**, and this bundle does not coin
  it.

---

## 8. Relationships to other artifacts

- **Upstream.** The PRD or unit of product work whose launch or change this announces, and, when a launch
  is coordinated, the launch checklist that confirms the right people were told. This bundle's own worked
  example (below) reads its facts from both rather than restating them.
- **Sibling by purpose, distinct by purpose alone.** `release-notes` records and describes what changed,
  under its own format constraints (GitLab's own process caps an entry at "125 words or fewer, and no images
  or videos" [[15]](#ref-15)); this type tells a specific internal reader what that change means for them
  and what to do. The boundary is drawn in [§6](#6-debates-and-contested-boundaries), and the family's shared
  instrument, its research log and companion, treats both as legitimate ways to talk about the same
  underlying change to different ends, not as competing descriptions of it.
- **Not a communications plan.** Prosci's plan is a standing, multi-message strategy across a change's
  lifecycle; this type is one message that plan might schedule, if a plan exists at all
  [[12]](#ref-12)[[25]](#ref-25).
- **Not incident communication.** PagerDuty's guide is bound to the trigger of a live, ongoing incident, not
  to a purpose this type could also serve; a status page and repeated per-incident updates are a different
  shape entirely [[13]](#ref-13).
- **Not a periodic update.** Basecamp's Heartbeats "summarize the last ~6-weeks of work for a given team,
  department, or individual" on a recurring cadence [[4]](#ref-4); this type is written once, for one event.
- **Not the PR/FAQ.** The PR/FAQ is written before a build decision, as a vetting device; this type is
  written after the decision, alongside or following the launch itself [[11]](#ref-11).
- **The boundary with a launch checklist is inferred, not sourced.** A launch-readiness checklist is a
  multi-workstream tracking artifact that produces announcement-like material as one of its outputs, but no
  source in this research names the line between the checklist and the announcement it produces
  [[14]](#ref-14); this bundle infers it rather than quotes it.
- **No pm-skills skill produces this document.** The nearest, a foundation stakeholder-update skill,
  translates the outcome of one meeting for people who were not there, which is a narrower job than
  announcing a launch or change.

---

## 9. Adaptations

The evidence here is thinner than for the anatomy itself, and this section states what it supports rather
than extrapolating past it.

- **Audience size and formality.** Channel choice tracks audience scope: a broader, formal, company-wide
  announcement favors email or the intranet, while a wide-reach live event favors digital signage or a
  company-wide app [[26]](#ref-26). A channel-and-audience matrix approach maps channel, purpose, and
  audience segment (department, role, location, desk versus deskless) together rather than choosing a
  channel in isolation [[28]](#ref-28).
- **Cross-functional launches.** Where a change touches several departments, one source recommends an
  explicit distribution list run through an owning process rather than a single undifferentiated blast
  [[35]](#ref-35). A layered cascade, where each level of management adds locally relevant context instead
  of repeating the message verbatim, is one documented way to reach an entire organization from one initial
  announcement [[29]](#ref-29).
- **Frontline or deskless employees.** A named risk is forgetting this group in channel choice: "These
  groups often get left behind" [[28]](#ref-28). A restated finding also notes that many deskless employees
  lack a corporate email address or intranet access at all [[30]](#ref-30). Face to face and through the
  reader's own supervisor are named as effective channels for this group, though this claim traces only
  through a secondary restatement of a 1996 Harvard Business Review article; the original was readable only
  to its lead paragraph, which itself argues that more executive-authored communication is not the answer
  [[30]](#ref-30)[[31]](#ref-31).
- **Time-critical changes.** For something as consequential as a launch-date slip, one practitioner
  recommends email first with chat as a supplement, not chat alone [[27]](#ref-27).

---

## 10. Worked example

See `announcement-internal-comms_example.md` for the internal announcement of the Saved Views Sharing
launch, sent by its communications owner. It reads its facts, the rollout stages, the entitlement behavior,
the escalated and unresolved risk, and the linked help-center article, from the PRD, the launch checklist,
the test plan, and the status report rather than restating them, and it links out to the separate
`release-notes` entry for the public-facing record of the same change.

---

## References

Tagged by reliability, following the tags this bundle's research log itself assigns: `[primary]`
originating or governing source; `[practitioner]` recognized independent authority; `[vendor]` tool vendor
or commercially motivated source; `[standards]` a standards or government body. Researched 2026-09-25;
every entry below was fetched and its quotations checked against the raw retrieved text.

<a id="ref-1"></a>[1] Robert Grover / Staffbase. "[Organizational Announcements: Best Practices, Examples & Templates](https://staffbase.com/blog/organizational-announcements)." staffbase.com (accessed 2026-09-25). [vendor]

<a id="ref-2"></a>[2] GitLab. "[GitLab Handbook, Communication](https://handbook.gitlab.com/handbook/communication/)," "How to make a company wide announcement." handbook.gitlab.com (accessed 2026-09-25). [vendor]

<a id="ref-3"></a>[3] Jason Fried (37signals). "[Deployments: How we announce new features and updates internally at Basecamp](https://world.hey.com/jason/deployments-how-we-announce-new-features-and-updates-internally-at-basecamp-b709544e)." world.hey.com, 2022-01-06 (accessed 2026-09-25). [practitioner]

<a id="ref-4"></a>[4] 37signals. "[How we communicate](https://basecamp.com/guides/how-we-communicate)," Heartbeats and Kickoffs. basecamp.com (accessed 2026-09-25). [practitioner]

<a id="ref-5"></a>[5] Atlassian. "[Change Management Communication With Video](https://www.atlassian.com/team-playbook/plays/change-management-communication-with-video)." Team Playbook (accessed 2026-09-25). [vendor]

<a id="ref-6"></a>[6] Kate Moran / Nielsen Norman Group. "[Inverted Pyramid: Writing for Comprehension](https://www.nngroup.com/articles/inverted-pyramid/)." nngroup.com (accessed 2026-09-25). [practitioner]

<a id="ref-7"></a>[7] Erika Suffern / MLA Style Center. "[Don't Bury the Lede](https://style.mla.org/dont-bury-the-lede/)." style.mla.org (accessed 2026-09-25). [practitioner]

<a id="ref-8"></a>[8] Purdue OWL. "[Parts of a Memo](https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/memos/parts_of_a_memo.html)." owl.purdue.edu (accessed 2026-09-25). [reference]

<a id="ref-9"></a>[9] Colin Bryar & Bill Carr. "[Working Backwards PR/FAQ Instructions & Template](https://workingbackwards.com/resources/working-backwards-pr-faq/)." workingbackwards.com (accessed 2026-09-25). [practitioner]

<a id="ref-10"></a>[10] LaunchNotes. "[Release Notes vs. Changelog: Key Differences](https://www.launchnotes.com/release-notes/vs-changelog)." launchnotes.com (accessed 2026-09-25). [vendor]

<a id="ref-11"></a>[11] Working Backwards (Colin Bryar and Bill Carr). "[The Amazon Working Backwards PR/FAQ Process](https://workingbackwards.com/concepts/working-backwards-pr-faq-process/)." workingbackwards.com (accessed 2026-09-25). [practitioner]

<a id="ref-12"></a>[12] Tim Creasey / Prosci. "[Communications Checklist for Change Management](https://www.prosci.com/blog/communications-checklist-for-change-management)." prosci.com (accessed 2026-09-25). [practitioner]

<a id="ref-13"></a>[13] PagerDuty. "[Internal Stakeholder Communications Guide](https://stakeholders.pagerduty.com/)." stakeholders.pagerduty.com (accessed 2026-09-25). [vendor]

<a id="ref-14"></a>[14] Aniket Parihar / LogRocket. "[Don't ship blind: A practical checklist for internal launch readiness](https://blog.logrocket.com/product-management/practical-checklist-internal-launch-readiness/)." blog.logrocket.com (accessed 2026-09-25). [practitioner]

<a id="ref-15"></a>[15] GitLab Docs. "[Release notes](https://docs.gitlab.com/development/documentation/release_notes/)," documentation contribution process. docs.gitlab.com (accessed 2026-09-25). [vendor]

<a id="ref-16"></a>[16] Pete Winter / Tomorrow People. "[Product Launch Do's and Don'ts for Internal Teams](https://tomorrow-people.com/insights/internal-product-launch/)." tomorrow-people.com (accessed 2026-09-25). [vendor]

<a id="ref-17"></a>[17] tchop. "[Notification fatigue in internal communication](https://tchop.io/resources/glossary/internal-communication/notification-fatigue)." tchop.io glossary (accessed 2026-09-25). [vendor]

<a id="ref-18"></a>[18] Vicki Young / Nalla. "[Internal vs External Brand Launch: Why Order Matters](https://nalla.co.uk/internal-external-brand-launch-order/)." nalla.co.uk (accessed 2026-09-25). [vendor]

<a id="ref-19"></a>[19] SHRM Online, quoting Eloise Leeson-Smith and citing Robert Sutton. "[No More 'Tiger Teams' and 'Idea Showers': Nix the Business Jargon in Employee Communications](https://www.shrm.org/topics-tools/news/employee-relations/business-jargon-employee-communication-barriers)." shrm.org (accessed 2026-09-25). [practitioner]

<a id="ref-20"></a>[20] Sean Devlin / Ragan Communications, quoting Lisa Claybon and Lauren Stephens. "[A practical guide to fatigue-proof internal comms cascades](https://www.ragan.com/a-practical-guide-to-fatigue-proof-internal-comms-cascades/)." ragan.com (accessed 2026-09-25). [practitioner]

<a id="ref-21"></a>[21] ChangeEngine. "[Top 10 Internal Communication Fails (and What You Can Learn From Them)](https://www.changeengine.com/articles/10-internal-comms-fails)." changeengine.com (accessed 2026-09-25). [vendor]

<a id="ref-22"></a>[22] ChangeEngine. "[What is Message Fatigue?](https://www.changeengine.com/glossary/what-is-message-fatigue)." changeengine.com glossary (accessed 2026-09-25). [vendor]

<a id="ref-23"></a>[23] Jake Brereton / LaunchNotes. "[How to Time a Feature Announcement So Every Channel Reinforces the Last](https://www.launchnotes.com/blog/feature-announcement-timing)." launchnotes.com (accessed 2026-09-25). [vendor]

<a id="ref-24"></a>[24] AnnounceKit. "[Internal vs. External Changelog: Why You Need Both](https://announcekit.app/blog/internal-vs-external-changelog-and-why-you-need-both/)." announcekit.app (accessed 2026-09-25). [vendor]

<a id="ref-25"></a>[25] Tim Creasey / Prosci. "[Why Some Communications Work and Others Don't](https://www.prosci.com/blog/understanding-why-some-communications-work-and-others-dont)." prosci.com (accessed 2026-09-25). [vendor]

<a id="ref-26"></a>[26] Sophie Hamblett / Interact Software. "[How to Choose the Best Internal Communication Channels](https://www.interactsoftware.com/blog/how-to-choose-the-best-internal-communication-channels/)." interactsoftware.com (accessed 2026-09-25). [vendor]

<a id="ref-27"></a>[27] Lauren Kersanske / Crayon, quoting Annum Munir (Google Cloud). "[How to Master Internal Communication for Your Next Product Launch](https://www.crayon.co/blog/your-next-product-launch)." crayon.co (accessed 2026-09-25). [vendor]

<a id="ref-28"></a>[28] Cristina Hure / ContactMonkey. "[How To Create An Internal Comms Channel Matrix](https://www.contactmonkey.com/blog/internal-communication-channel-matrix)." contactmonkey.com (accessed 2026-09-25). [vendor]

<a id="ref-29"></a>[29] Axios HQ Insights. "[Reinforce, not repeat: Smart ways to cascade key internal updates](https://www.axioshq.com/insights/its-reinforce-not-repeat-a-smarter-way-to-cascade-essential-information-around-your-organization)." axioshq.com (accessed 2026-09-25). [vendor]

<a id="ref-30"></a>[30] Jamie Bell / Workshop. "[Reaching and changing frontline employees: the 2026 edition](https://useworkshop.com/blog/reaching-and-changing-frontline-employees/)." useworkshop.com (accessed 2026-09-25). [vendor]

<a id="ref-31"></a>[31] T.J. Larkin and Sandar Larkin. "[Reaching and Changing Frontline Employees](https://hbr.org/1996/05/reaching-and-changing-frontline-employees)." Harvard Business Review, 1996-05 (accessed 2026-09-25; paywalled beyond the lead paragraph). [primary]

<a id="ref-32"></a>[32] Haystack. "[How to Communicate New Policies to Employees](https://www.haystackteam.com/blog/how-to-communicate-new-policies-to-employees)." haystackteam.com (accessed 2026-09-25). [vendor]

<a id="ref-33"></a>[33] Hourly, Inc. "[How to Notify Employees of Policy Changes + Free Template](https://www.hourly.io/post/notifying-employees-of-policy-changes)." hourly.io (accessed 2026-09-25). [vendor]

<a id="ref-35"></a>[35] Lawrence Chapman / Product Marketing Alliance, quoting Jasmine Jaume (Intercom) and Rene Kardtke (Ontic). "[How to create a product launch internal communication plan](https://www.productmarketingalliance.com/the-importance-of-internal-communication-plus-how-to-crush-it/)." productmarketingalliance.com (accessed 2026-09-25). [vendor]

<a id="ref-36"></a>[36] Brianna Susnak (Salesforce). "[The Change Management Playbook for Major UI Rollouts](https://slack.com/blog/transformation/change-management-playbook-ui-rollouts)." Slack blog (accessed 2026-09-25). [practitioner]

<a id="ref-37"></a>[37] Wendy Hirsch. "[How to communicate change in an organization, six key practices](https://wendyhirsch.com/blog/checklist-for-change-communication)." wendyhirsch.com (accessed 2026-09-25). [practitioner]

<a id="ref-38"></a>[38] UK Cabinet Office / Government Communication Service. "[GovS 011: Communication](https://assets.publishing.service.gov.uk/media/6576d36c48d7b7000d57ca0d/GovS_011-_Communication_Version_2.1.pdf)," version 2.1, 2023-10. assets.publishing.service.gov.uk (accessed 2026-09-25). [standards]

<a id="ref-39"></a>[39] Headquarters, Department of the Army. "[AR 25-50: Preparing and Managing Correspondence](https://armypubs.army.mil/epubs/DR_pubs/DR_a/ARN42124-AR_25-50-007-WEB-13.pdf)," major revision 2020-10-10, administrative revision 2024-10-04. armypubs.army.mil (accessed 2026-09-25). [primary]

<a id="ref-40"></a>[40] Headquarters, Department of the Army. "[AR 25-50: Preparing and Managing Correspondence](https://home.army.mil/wood/application/files/3015/5751/8343/AR_25_50_Army_Correspondence.pdf)," major revision 2013-05-17, administrative revision 2015-07-06, superseded; mirrored by Fort Leonard Wood (accessed 2026-09-25). Cited only for what the earlier edition said. [primary]
