# Guide: Announcement / Internal Comms (operator card)

The short card. Why the document is shaped this way, and the full argument behind every rule here, is in
[`announcement-internal-comms_companion.md`](announcement-internal-comms_companion.md). A fully worked
instance is [`announcement-internal-comms_example.md`](announcement-internal-comms_example.md).

**Read this before you reach for the template.** No standards body, government communication function, or
professional institute publishes this document by name. This bundle's admission rests on three sources, all
vendor or practitioner tier: a vendor's blog that names and defines the type with worked templates, a
company handbook that prescribes what a company-wide announcement must carry, and a practitioner's account
of one company's own named internal format. Its evidence on channel choice and timing is vendor and
practitioner tier only, nothing here rises to a standards-tier norm for a product launch. Treat any specific
number you see below (a notice window, a repetition count) as one organization's own house rule, never as a
convention every team follows.

## When to use

- A decision has already been made, and you need to tell the people who did not do the work, and were not
  in the room, what it means for them.
- You can state a single fact the reader could act on, or use to rule themselves out, without first reading
  the rest of the document.
- The change is real, live or about to go live, not a proposal still being vetted for whether it should
  happen at all.
- A known issue or open risk needs to reach the people who support the product before a customer surfaces
  it for them.
- This is one message about one event, not a recurring cadence update or the start of a standing
  communications program.

## When NOT to use

The type sits next to several better-documented practices, and it is easy to reach for the wrong one. Name
which one you actually need before you start filling this in.

| You actually need | Because |
|---|---|
| **A periodic status update** (a Basecamp-style Heartbeat) | This type is written once, for one event. A recurring digest of the last several weeks of work for a team or individual is a different, cadence-driven document. |
| **A PR/FAQ** | The PR/FAQ is written before the build decision, as a forcing function and a vetting device, as if the product already existed. This type fires after the decision is made, alongside or following the launch itself. |
| **Incident stakeholder communications** | Bound to the trigger of a live, ongoing incident, with its own status page and repeated per-incident updates. Not a purpose this type also serves. |
| **A change-management communications plan** | A plan (Prosci's sense) is a standing, multi-message strategy with its own senders, cadence, and channels across a change's whole life. This type is one message that plan might schedule, if a plan exists at all. |
| **Release notes** | The line is purpose, not audience: a release note is a curated, user-impact record of what changed. This type says what that change means for one specific reader and what they must do, then links to the release note rather than restating it. That boundary is this library's own; no source draws it in those words. |
| **A launch-readiness checklist** | A multi-workstream tracking artifact that produces announcement-like material as one of its outputs. No source in this bundle's research names the exact line between the checklist and the announcement it produces; this bundle infers the boundary rather than quoting it. |

**Who sends it is a choice this template asks you to make, not one it makes for you.** The sources
disagree: one holds that the project team is the wrong sender for any message and that a personal-impact
line should come from the reader's own manager; launch practice instead assumes the product team runs the
briefing; one company simply has whoever did the work write it directly. That disagreement is exactly why
Sender is a frontmatter field you fill in deliberately (see rubric row 8), not a default.

## Pick a variant

This bundle ships one size, and there is no second, heavier variant to choose between. That is a deliberate
call, not an unfinished one: the strongest source this research found ships seven worked templates for this
type, all sharing a single shape, a subject line, a salutation, and three or four sentences, and its two
highest-stakes examples (a security incident, a major restructuring) differ from the rest of the set by one
sentence, not an added section. The material a heavier variant might plausibly add, a leadership quote or a
linked FAQ, appears in that same source only as optional best practice, never as a section inside any
worked template. Building a full variant from that material would be this library inventing a shape no one
has documented, so none is offered. Treat this single size as provisional, following from the strongest
source found rather than from a wide survey of longer internal announcements.

## The rubric (self-grade)

Score each row 0, 1, or 2. **Under 11 out of 16, and a reader who was never in the room still cannot tell
whether this affects them or what, if anything, they are supposed to do about it, the exact gap this
document exists to close.**

All eight rows apply. This bundle ships one size, so there is no per-variant scoping decision to make here.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Actionable headline** | Names no fact a reader could act on (a label like "Product Update"), so the reader has to open the rest of the document to learn anything | States a real fact, but the reader still needs the rest of the document to know whether it applies to them or what to do about it | A reader can act on it, or confidently rule themselves out, without reading past the headline |
| 2 | **Honest what, who, when** | One of what, who, or when is missing entirely | All three are present, but an unconfirmed date reads as fixed, or "who it applies to" sweeps in people the change does not actually reach | What is changing, exactly who it applies to, and the effective date are all present, and if the date is not fixed yet, the document says so and names when it will be |
| 3 | **Reader's own stake** | The reason given only makes sense to someone on the team that shipped it, in that team's own vocabulary | Plain language, but the reason given is still the team's reason for doing the work, not the reader's own stake | States, in the reader's own terms, why this matters to them specifically, not why it mattered to the team that built it |
| 4 | **Explicit action and non-change** | No action is named, or a bare "let us know if you have questions" that leaves the reader guessing what is being asked of them | An action, or an explicit "nothing to do," is stated, but a deadline is missing, or what stays the same is never addressed | Names the reader's exact action and its deadline, or says plainly there is nothing to do, and separately says what does not change |
| 5 | **Known issues surfaced first** | Left blank or silent despite the team already tracking an open risk | An issue is named, but a reader cannot tell whether it is tracked anywhere or who owns it | Names a specific open issue, in words a front-line reader could repeat back to someone who asks, whether or not it is resolved yet |
| 6 | **Linked, not restated** | Detail that belongs to an upstream artifact (the PRD, the release notes, the checklist) is restated here in the announcement's own words | Links exist, but at least one significant fact is restated rather than pointed at its source | Every fact in the document traces to a named, linked source, and none of the underlying detail is restated in the announcement's own words |
| 7 | **Contact and next update** | Neither a specific person nor any sense of when the next update comes is given | One of the two is present; the other is missing | Names one specific person to ask, and either a date or a named trigger for when the next update comes |
| 8 | **Deliberate sender** | Sender is blank, or defaults to whoever happened to draft the message | A sender is named, but nothing shows the choice was deliberate | The named sender fits what is actually being said: who can credibly speak to the business reason, and, for a personal-impact message, why this sender rather than the reader's own manager |

Every cell above describes evidence, not a count. The test is the same one this library applies everywhere:
could someone satisfy the cell without actually making the document better? If yes, the cell is written
wrong, and that is a defect in the rubric, not a license to grade loosely.

## Named anti-patterns

1. **Burying the point.** The newsworthy fact arrives after the context and generic framing that should have
   followed it, not led it. A reader who has to read three paragraphs to find out what changed has already
   lost the thread.
2. **Jargon that does not travel.** Language that makes sense inside the team that shipped the change, but
   not past it. Left unchecked, this is not merely unclear, it leaves a reader who does not feel able to ask
   a clarifying question unsure what is actually being asked of them.
3. **A single channel carrying the whole announcement.** Posting once, in a low-visibility channel, so the
   message gets lost or muted rather than reaching the people it is for.
4. **Broadcasting instead of starting a conversation.** The announcement reads as a one-way telling plan,
   with no room for a reply, rather than something the reader could actually respond to.
5. **No call to action.** The document ends with a detailed update and no clear next step. A reader who
   finishes it feels informed, not activated, and information without action is a courtesy, not a catalyst.
6. **Telling customers before the people who support them.** A customer-facing colleague hears about a
   change from a customer instead of from this document. That is a failure of sequencing, not of knowledge,
   and it is exactly what the Known Issues section exists to prevent.
7. **Restating instead of linking.** Every fact copied into the announcement, rather than linked to its
   source, is a fact that can drift out of step with the upstream record over time. No source read for this
   bundle documents this as a named failure; it is this library's own reason for the link, do not restate
   rule, and it is labelled as that rather than as an established practice.
8. **Presenting a house rule as a general norm.** Stating one team's own notice window, sender choice, or
   repetition count as though it were an industry standard, when no source in this bundle's research
   supports a general norm for a product launch's timing. This includes coining or repeating "announcement
   fatigue": no source in this research uses that term. The sourced terms for the underlying failure are
   notification fatigue and message fatigue.

## No paired skill

`pairs_with: []`. No pm-skills skill produces this document today. The nearest, a foundation
stakeholder-update skill, translates the outcome of one meeting for people who were not there, which is a
narrower job than announcing a launch or a change.

## When it is good enough

When a reader who was never in the room can tell, from the headline alone, whether this affects them, when
the action they need to take (or the fact that none is needed) is stated with a deadline rather than
implied, when a known open risk is already visible here rather than waiting to be discovered by a customer,
and when every fact in the document points at its source instead of repeating it.

Then delete every HTML comment. If the honest answer to "who sends this" or "how much notice does this
window give" is a guess rather than a decision, that is worth settling before you send, not after.
