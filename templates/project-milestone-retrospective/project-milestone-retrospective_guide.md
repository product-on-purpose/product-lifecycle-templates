# Guide: Project Milestone Retrospective (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`project-milestone-retrospective_companion.md`](project-milestone-retrospective_companion.md). A fully
worked instance is
[`project-milestone-retrospective_example.md`](project-milestone-retrospective_example.md).

This document looks back on **a bounded piece of work that has ended**. It is terminal: the work is over,
the team may disperse, and part of the audience was not there. That is the whole design, and it is why the
type travels under the aliases `lessons learned`, `post-project review` and `after-action review`.

## When to use

- A bounded piece of work has finished. A project, a migration, a pilot, a milestone with a date on it. Not
  a period that ended because the calendar said so, and not one thing that broke.
- Part of the audience was not in the room, and some of them never will be. This is the case the document
  exists for: the team scatters onto new work, and what the group knew together goes with it unless it is
  written down.
- You can name a reader and say what they decide with this. That is not a cover-page courtesy. In every
  real filled document this bundle's research read, the answer changed the content: one federal pilot
  report relabelled its own findings as opportunities rather than lessons because they fed a specific
  decision that had not been taken yet.
- A prior review, audit, readiness gate or earlier retrospective covered this same work, and somebody needs
  to know what happened to the things it raised. That is the `full` variant's reason for existing.
- Your organisation keeps a running lessons log or register. This document is written **from** it at the
  end, not instead of it. Both major project methodologies split continuous capture from the terminal
  report, and this is the terminal half.
- The work is being closed formally against a baseline: scope, cost, schedule, safety record. Government
  closeout templates are built this way, and `full` follows them.

## When NOT to use

Where a row below describes what you actually have, **you need something else**, and the something else is
specific. The first three rows are the boundary this bundle exists to teach: get them wrong and you have
three documents nobody can tell apart.

| What you actually have | What you need instead | Why |
|---|---|---|
| A sprint or iteration ended, on a cadence, and the same team keeps working together | `sprint-retrospective-notes` | A cadence retrospective looks back on a **period**, at how the team worked, and its canonical output is not a document at all: Scrum's own guide describes the improvements as changes that may travel into the next Sprint Backlog. A retro tool draws the same line from the other side, noting that sprint retrospectives happen repeatedly through a project while the project post-mortem happens once. Cadence retrospectives feed a backlog; terminal retrospectives produce a document. |
| One specific thing failed, and the question is why | `incident-postmortem` | A postmortem is **event-triggered** causal analysis of a failure. Named sources split the two by purpose: postmortems set out to understand what went wrong, while retrospectives serve the team doing the work. Reach for the postmortem even if the project also just ended, and point at it from here rather than analysing the failure twice. |
| Nobody will open it. You cannot name a reader, a decision, or anything downstream of this document | **Nothing at all**, or go and find the reader first | This is the criticism this document type actually attracts, and it is narrower than it sounds. Every critic behind this bundle attacks one pattern, the repository nobody consults, and **every one of them still recommends writing something down**: their fix is a different kind of document with a retrieval path, never no document. The opposite failure is equally real and equally documented, engineers at a national space research centre losing failure knowledge to team turnover and fragmented documentation and explicitly wishing for a lessons database they did not have. So look for the reader before you conclude there is none. If there genuinely is none, that is a finding about your organisation, not a formatting problem. |
| Your organisation mandates a formal closeout or end-project report | This document's content, **inside** that report | Both PRINCE2's end project report and the US DOE closeout template carry lessons as one section among baseline, closeout status and archive sections. Where a closeout report is mandated, write these sections as its lessons content rather than as a competing artifact. |
| You need to run the session, not record it | A facilitation guide | The founding project-retrospective handbook describes a multi-day facilitated review, and Derby and Larsen's five-stage model (set the stage, gather data, generate insights, decide what to do, close) describes a **meeting**, not a document. This file is the written record that survives the meeting, not the agenda for one. |

## Pick a variant

The two sizes are two genuinely different genres, not two lengths of one reader's need. The corpus behind
this bundle split cleanly in half.

**Lean (six sections)** is the **team-authored retrospective**: Scope and Period, What Happened, What
Worked, What Did Not, Lessons for Others, Actions and Owners. Short, narrative, written by the people who
did the work, read by the team, its neighbours and whoever comes next. Use it by default.

**Full (seven sections)** is the **accountability-grade report**. It adds **Previously Identified Issues**
in place, and a planned-against-actual quantification table inside What Happened. Nothing is renamed and
nothing is reordered, so lean stays a strict ordered subset of full. Reach for full when any of these is
true:

- money, safety or a regulator is involved;
- the reader can stop the next thing or fund it;
- a prior review of this same work exists and its findings need checking against what happened;
- the work is being closed formally against a baseline, which is the shape government closeout and
  post-implementation templates both use.

**One honest counter-signal before you commit to either.** The strongest worked retrospective this
bundle's research found uses none of these headings. It is organised entirely around the three aims the
project set for itself. These sections are what the research found missing from real documents, not proof
that no good retrospective was ever written without them.

## Quality rubric (self-grade)

Score each 0, 1 or 2. Full below **14 out of 20**, or lean below **13 out of 18**, and you have produced
the document every critic of this type describes: a record filed where nobody has a reason to open it,
committing nobody to anything.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Checkable boundaries** | The work is named but not bounded, so a later reader cannot tell what is inside this review | Dates or deliverables fix the period, but nothing is named as deliberately outside it | Start and end are fixed to dates or deliverables, and at least one thing a reader would reasonably expect is named as deliberately out of scope |
| 2 | **Audience and next use named** | No reader named, or the reader is an archive, a wiki space, or "the organisation" | A person or body is named, but nothing says what they do with this document | Names the person or body who opens this **and** the specific decision or next piece of work it feeds, concrete enough that a second person could check that decision is real and still ahead |
| 3 | **Circulation settled** | Nothing recorded about who can read this | Circulation is recorded, but it was settled after the discussion, or the document does not say when | States who can read this and records that the people who spoke knew it before they spoke, not after |
| 4 | **Record before interpretation** | What Happened argues why things went the way they did | Mostly factual, but at least one judgement is written as though it were a fact | Every line in What Happened could be checked against a system of record by someone who was not there, and every judgement waits for the two sections built to hold it |
| 5 | **Something material counted** | No quantity anywhere, or a number with nowhere to check it | A number is present, but in units this work was not judged on, or with no source named | At least one measure the work was actually judged on, planned against actual, with a named place a reader can go and verify it. Currency only where money is how this work was judged; a defect rate or a schedule slip counts just as much |
| 6 | **Successes carry mechanism** | Entries are compliments, morale words with no practice named | A specific practice is named, with no stated reason it worked | Every entry names the practice, why it worked, and what a different team would have to do to get the same result |
| 7 | **Causes, not people** | A person is named as the reason something failed, or the entry is too vague to act on | A cause is named, but nothing is said about what would have prevented it | Every entry names what happened, why it happened, and what would have prevented it, aimed at the decision or the system and never at a person |
| 8 | **Repeats marked** *(full)* | The section is missing or blank in work that does have a prior review | Prior issues are listed, but what was agreed is not separated from what actually happened | Each row carries the issue as the earlier document worded it, where and when it was raised so a reader can go and look, and the agreed action kept separate from the outcome. Where no prior review exists, "N/A" plus one honest line |
| 9 | **Lessons for absent readers** | Lessons only parse to people who were in the room | Lessons would travel, but name no audience and no change | Every lesson names who it is for and what they should do differently, and reads correctly to someone with no context on this project |
| 10 | **Actions owned and dated** | A bulleted intention with no name attached, or an action owned by a team | An owner and a date, but the action exists only inside this document | Every row names one person, a date, and an identifier in the tracker your team already uses, so this document does not quietly become a second, stale tracker |

**Which rows apply to what.**

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| full | all 10 | 20 | **14** |
| lean | 1-7, 9 and 10 | 18 | **13** |

Row 8 is scored only against full. Lean ships no Previously Identified Issues section, and grading it there
would penalise the choice of variant rather than the quality of the document. That row is also the one this
bundle is least dogmatic about: repeat-lesson tracking was found specifically in the external-audit genre
and not in the team-authored retrospectives read, so the template invites it rather than demanding it.

The test behind every cell above: **could someone satisfy it without improving the document?** A row that
counted lessons, action items or table rows would reward padding, and a threshold that can be cleared by
adding items will be cleared by adding items. Every cell instead asks whether a specific piece of evidence
exists, and whether a reader who was not there could go and check it.

## Named anti-patterns (the usual wrecks)

1. **Deposit and forget.** The document is written, filed in a general archive, and never consulted again.
   This is the single failure that the entire critical literature behind this bundle is actually about, and
   the named fix is never less writing: it is a retrieval path somebody has a reason to walk. One critic who
   titled his piece against retrospectives outright still wants them kept in a repository for trend
   evidence, and wants the most recent one presented at every project kickoff. Decide the retrieval path
   before you write, not after.
2. **The sanitised retrospective.** A peer-reviewed study of retrospectives in large-scale agile
   development found that making minutes public can get real critique toned down, or removed before it is
   ever written down. That failure happens **before the document exists**, which is why circulation is a
   Scope and Period decision taken ahead of the discussion rather than a publishing question settled
   afterwards. If it must be public, say so in advance and accept that the sharpest material may need a
   narrower channel.
3. **Writing for an archive instead of a person.** A document with no named reader and no next use has
   already lost, and a naive what-went-well / what-did-not / actions shape has no field to catch it. The
   opposite, done deliberately, is visible in the real filled reports: findings reframed, and the register
   of the whole document changed, because a specific decision was pending.
4. **Not writing it at all.** The mirror failure, and it is just as well evidenced. At a national space
   research centre, engineers reported failure knowledge fragmented across a wiki, a repository and a chat
   channel, or simply not documented, and wanted a lessons database they did not have. The complaint that
   nobody reads these is a reason to fix retrieval, not a licence to skip the record when the team is about
   to disperse.
5. **Held so late that the memory and the team have both gone.** The timing argument runs two ways: memory
   fades quickly after the outcome, and the people scatter onto new work. A retrospective held when half
   the contributors have moved on produces the half of the story the survivors remember.
6. **Corrective actions declared closed, and the same problem met again.** A government audit of one
   agency's project management found a long history of identifying corrective actions and declaring them
   successfully resolved, only to meet the same class of problem again. Previously Identified Issues exists
   to catch exactly this, and it is the easiest section to lose under pressure. If it is dropped, say who
   dropped it and why in Scope and Period rather than letting it vanish.
7. **Actions with no owner and no date.** The `process-docs` family's shared failure, and this document type
   is where published practice is weakest: of the templates read in full for this bundle, exactly one gives
   an action both a responsible party and dates, and several prominent ones give neither. An action owned by
   a team is owned by nobody, and a document that ends in unowned intentions is a feelings log.
8. **Scope that never leaves the team.** Even inside a large multi-team programme, retrospective content
   stays overwhelmingly team-internal. For a cadence retrospective that is a limitation. For a terminal
   document whose whole point is a reader who was not there, it is fatal: Lessons for Others becomes a
   second copy of What Did Not, written in the team's private vocabulary.
9. **Running the wrong one of the three.** A cadence retrospective on work that has ended loses the
   handover; a postmortem on ordinary work pathologises it; this document run on a sprint produces a
   terminal report about a team that is still there on Monday. **Treat this as this library's own reasoning
   rather than received practice**: the `process-docs` family contract's own change note records that no
   source read frames the confusion as a documented failure mode, and named organisations deliberately use
   the words differently, one calling its incident process an incident review and another splitting
   "retrospective" into an incident type and a post-project type. Name the trigger you actually have before
   you pick a file.

## Pairing with your process

This bundle is the third member of the `process-docs` family, and the family is meant to be told apart by
**trigger**. A sprint retrospective is triggered by the calendar and looks back on a period, at how a team
worked. An incident postmortem is triggered by an event and looks back on one failure, at why. This document
is triggered by an ending and looks back on a bounded piece of work, for readers who may not have been
there. Name the trigger first; the file follows from it.

Around the document, three connections matter. **Upstream**, if your organisation keeps a running lessons
log or register, write this from it rather than in competition with it. **Alongside**, if a formal closeout
or end-project report is mandated, these sections are its lessons content. **Downstream**, every row in
Actions and Owners needs somewhere it is really tracked: the `product-backlog`, the `risk-register` or the
`raid-log`. Of those three, only the `product-backlog`, the team's ordinary ticket tracker, reflects
published practice; the other two are this library's own convention, and the family contract says so.

One last thing, and it is the cheapest fix for the failure this document type is criticised for. Give these
documents an index. The one surveyed tool whose native retrospective artifact is a persisted page rather
than a board builds that index automatically, listing every retrospective in the space, which is precisely
the retrieval affordance the critics say is missing.
