---
title: "{{announcement_title}}"
doc_type: announcement-internal-comms
size: lean
audience: "{{audience}}"
channel: "{{channel}}"
send_date: "{{send_date}}"
sender: "{{sender}}"
status: draft
doc_version: "{{doc_version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: announcement-internal-comms
source_template_version: 0.1.0
---

<!--
LEAN ANNOUNCEMENT / INTERNAL COMMS. This bundle ships one size, deliberately. Staffbase's seven worked
templates for this type share a single shape, a subject line, a salutation, and three or four sentences, and
its two highest-stakes examples, a security incident and a major restructuring, differ from the rest of the
set by one sentence, not a section. The material a heavier variant might plausibly add, a leadership quote or
a linked FAQ, appears on that same page only as optional best practice, "Involve leadership" and "Link to
FAQs or additional resources", never as a section inside any of the seven templates themselves. A full
variant built from that material would be an invention of this library rather than a documented practice, so
none is proposed. Treat this single size as provisional, not settled: it follows from the strongest source
this research found, not from a wider survey of longer internal announcements. See
announcement-internal-comms_companion.md section 4 (Variants and sizing).

READ THIS BEFORE YOU FILL IT IN, BECAUSE IT CHANGES WHAT THIS TEMPLATE CLAIMS.
No standards body, government communication function, or professional institute publishes this document by
name. This bundle's admission rests on three sources, all vendor or practitioner tier, and its evidence on
channel choice and timing is vendor and practitioner tier only. A window you see named elsewhere, GitLab's
"ideally 72 hours (at minimum 24 hours) in advance of a due date" or Salesforce's "at least one business day
before the change goes live", is that company's own house rule, never a general norm for a product launch.
If your own team keeps a window, state it the same way, as your own practice, not as a convention everyone
follows. See announcement-internal-comms_companion.md section 1 (Orientation) and section 6 (Debates).

WHO SENDS THIS IS A DELIBERATE CHOICE, NOT A DEFAULT THIS TEMPLATE MAKES FOR YOU. The sources disagree, and
this template does not pick a winner among them. Prosci holds that the project team is the wrong sender for
any message, "One of the biggest and most common mistakes you can make is to have your project team sending
all the communications", and that a personal-impact message should instead come from the reader's own
manager, "People prefer to learn about change-related impacts to their own daily work from their manager".
Launch practice instead assumes the product or product-marketing team runs the briefing. Basecamp has "one of
the people who did the work" write the message directly. That disagreement is why Sender is a frontmatter
field you choose, not a role this template assumes for you. See announcement-internal-comms_companion.md
section 6 (Debates: Who should send it).

LINK, DO NOT RESTATE. Every fact below should trace to an upstream artifact, the PRD, the release notes, or
the launch checklist, rather than being restated here from memory. GitLab's own instruction is direct: "The
majority of information should still be in the Handbook which you include links to." Keeping the detail in
the linked source is also what stops this announcement from drifting out of step with the record it
summarizes over time. See announcement-internal-comms_companion.md section 3 (Anatomy).

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   announcement-internal-comms_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a
   WEAK example, and the TRAP to avoid.
2. Fill the frontmatter first. Audience, Channel, Send Date, and Sender are the author's own decisions, not
   the reader's content, and every body section below assumes they are already set.
3. Replace each {{placeholder}} with your content.
4. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
5. Before you send it: self-grade against announcement-internal-comms_guide.md, then DELETE every HTML
   comment. They are guidance, not content.
-->

# {{announcement_title}}

## Headline

<!-- WHAT  One line a reader can act on without opening the rest of the document.
     WHY   NN/g's own reason is direct: "readers can get the main point, regardless of how much they
           read." Every one of Staffbase's seven worked templates opens with a subject line playing
           exactly this role. Deep dive: announcement-internal-comms_companion.md section 3 (Anatomy >
           Headline).
     ASK   What is the single most important fact here? Could a reader act on this line alone, without
           reading anything below it?
     GOOD  "Customers can pay invoices by direct debit from Monday 3 March; the billing support queue will
           see the first questions that morning."
     WEAK  "Product Update" (names no fact a reader could act on; could be about anything)
     TRAP  Burying the lede: a writer "buries the lede" when the newsworthy part of a story fails to
           appear at the beginning, where it's expected. A marketing agency names the same failure
           plainly: "avoid burying the most relevant information with the generic bits". -->

{{headline}}

## What Is Changing, and When

<!-- WHAT  The launch or change itself, who it applies to, and the date it takes effect.
     WHY   A company handbook's prescribed content for an announcement covers "What, Why, Who, When,
           Where", and a structured internal-comms play opens the same way, asking "What's changing? What
           will be different from the way it is today?" Deep dive:
           announcement-internal-comms_companion.md section 3 (Anatomy > What Is Changing, and When).
     ASK   What exactly is changing? Who does it apply to? On what date does it take effect, and is that
           date confirmed or still to be decided?
     GOOD  "The customer portal adds direct debit as a payment method for monthly invoices. It opens for new
           sign-ups on 3 March and for existing customers on 17 March, once the first month's collections
           have run cleanly."
     WEAK  "We're rolling out some payment improvements soon." (no mechanism, no date, no named audience)
     TRAP  Leaving out When, one of the handbook's own 5 Ws: a reader who cannot tell whether a change is
           live yet cannot act on the rest of the announcement either. -->

{{what_is_changing}}

**Who this applies to:** {{who_it_applies_to}}

**Effective date:** {{effective_date}}

## Why It Matters

<!-- WHAT  The reason for the change, in terms the reader can use, not the reason it mattered to the team
           that shipped it.
     WHY   The same internal-comms play asks "Why is this change happening now? Why is this change
           important?" Deep dive: announcement-internal-comms_companion.md section 3 (Anatomy > Why It
           Matters).
     ASK   Why now? Why does this matter to this specific reader, not to the team that built it?
     GOOD  "Card payments fail for roughly one invoice in twenty when a card expires (illustrative). Direct
           debit removes that failure for customers who choose it, without changing what anyone is billed."
     WEAK  "This aligns with our platform strategy for driving engagement." (a reason that matters to the
           team, not to the reader)
     TRAP  Jargon that travels within the team that shipped the change but not past it. A vendor's
           guidance is direct, "Use plain language and avoid corporate jargon", and so is a marketing
           agency's: "product marketing teams use a lot of jargon. Unfortunately, this doesn't necessarily
           translate well to other departments." A stronger-tier source names the cost of ignoring this:
           a reader who does not feel able to ask questions is left "unsure of what is being asked of
           them". -->

{{why_it_matters}}

## What It Means for You

<!-- WHAT  What changes for this specific audience, what does not change, and what they must do and by
           when, or an explicit statement that there is nothing to do.
     WHY   The same play asks "How will this change impact them?"; a vendor's checklist names "what they
           need to do (if anything)" as content a reader needs; and Basecamp's Deployment post is written
           so it is useful to "those on the front lines too". What is not changing belongs here too, on a
           practitioner's own checklist question, "What’s not changing?", and on Prosci's framing of
           communication around the reader's own stake, "What’s in it for me?" Deep dive:
           announcement-internal-comms_companion.md section 3 (Anatomy > What It Means for You).
     ASK   What changes for this reader specifically? What stays the same that they might otherwise
           assume has changed? What must they do, and by when, or is there genuinely nothing to do?
     GOOD  "If you work the billing support queue, expect questions about setting up a mandate from 3 March.
           Nothing changes for card payments. Read the linked set-up guide before your next shift, and pass
           any mandate that fails to the payments team the same day."
     WEAK  "Let us know if you have questions." (no specific action, no deadline; leaves the reader to
           guess what, if anything, they are supposed to do)
     TRAP  No call to action, now a named failure rather than only a missing best practice: "information
           without action is a courtesy, not a catalyst." Saying nothing is also a valid answer here, but
           it has to be said, not implied by omission. -->

{{what_changes_for_you}}

**What is not changing:** {{what_stays_the_same}}

**What you need to do:** {{required_action}}

**By when:** {{action_deadline}}

## Known Issues

<!-- WHAT  What could go wrong, or is not finished yet, stated here first, before a customer-facing
           colleague hears it from a customer.
     WHY   A Deployment post exists partly to explain what shipped and "points out what could be an
           issue", and a sequencing failure this research names directly is a customer-facing team hearing
           about a feature from a customer, "a failure of sequencing rather than of knowledge". Where this
           overlaps release-notes' own Known Issues content, link there rather than restating it (see the
           preamble's link-do-not-restate rule). Deep dive: announcement-internal-comms_companion.md
           section 3 (Anatomy > Known Issues).
     ASK   What is not finished yet, or could go wrong? Has the team that supports customers heard this
           before a customer could raise it? Is there a tracked issue to link to instead of restating the
           detail here?
     GOOD  "The first collection under a new mandate can take up to ten working days to clear
           (illustrative). A customer who asks why an invoice still shows as unpaid in that window has not
           been charged twice."
     WEAK  (section left blank, with an unresolved risk already known to the team) - silence here is what
           turns a known issue into a support ticket a customer opens first.
     TRAP  Staying silent because nothing is confirmed yet. A known risk stated plainly, even unresolved,
           is what this section exists for; the failure this research names is a customer-facing colleague
           learning about it from a customer instead of from this document. -->

{{known_issues}}

## Where to Learn More

<!-- WHAT  The source of truth, a named person to ask, and when the next update comes.
     WHY   A company handbook's own instruction is direct: "The majority of information should still be
           in the Handbook which you include links to." A vendor's checklist names both as reducing
           confusion, "linked resource, or named contact can reduce confusion". A practitioner's checklist
           adds the other half:
           "Let people know when you will update them again." Deep dive:
           announcement-internal-comms_companion.md section 3 (Anatomy > Where to Learn More).
     ASK   Which upstream artifact carries the full detail: the PRD, the launch checklist, the release
           notes? Who is the one named person to ask? When does the next update come, even if it is only
           "when stage two opens"?
     GOOD  "Full detail: the payments PRD and the release notes entry. Set-up guide: Paying by direct
           debit. Questions: the payments team's support channel. Next update: when existing customers are
           switched on, or by 17 March, whichever comes first."
     WEAK  Restating the PRD's requirements or the release notes' change list here instead of linking to
           them, so this document can drift out of step with the record it is supposed to summarize.
     TRAP  A link with no named contact. A vendor's own guidance treats the two as a pair, "linked
           resource, or named contact can reduce confusion", not as substitutes for each other. -->

{{source_of_truth_links}}

**Questions:** {{named_contact}}

**Next update:** {{next_update_date}}
