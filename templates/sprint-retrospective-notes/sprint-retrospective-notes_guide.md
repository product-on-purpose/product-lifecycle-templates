# Guide: Sprint Retrospective Notes (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`sprint-retrospective-notes_companion.md`](sprint-retrospective-notes_companion.md). A fully worked instance
is [`sprint-retrospective-notes_example.md`](sprint-retrospective-notes_example.md).

## When to use

- A sprint just ended, or is about to end, and the team is holding its retrospective. Write these notes to
  make one improvement owned, dated, and findable again, not to produce a transcript of the meeting.
- The team has run a retrospective before and produced action items last time. This document is where those
  items get checked against what actually happened, not only where this sprint's items get written down.
- More than one person needs to find the outcome later: a teammate who missed the meeting, someone who joins
  the team next quarter, or the same team three sprints from now wondering whether an idea was ever tried.
- The team works on a Scrum or agile-lineage cadence and is looking back on a period, on a schedule, at how
  it worked, not reacting to one specific thing that broke.

## When NOT to use

- **The sprint contained an incident and you want to analyze why it happened.** That is causal analysis of
  one event, not a look back at how the team worked across a whole sprint. Use the incident-postmortem member
  of this family for the analysis, and use this document only to name that the incident happened and point at
  where its analysis lives.
- **You are reviewing a release, a milestone, or a whole project, not one sprint.** That is a different
  occasion with its own literature, not a bigger size of this sprint-scoped document. Reach for a release or
  project retrospective instead.
- **Nothing from this retrospective will actually be revisited.** If the team will not reopen the Previous
  Actions table next time, this document records a discussion that commits nobody to anything, which is the
  exact failure this family of documents exists to prevent.
- **You need to run the retrospective itself.** This is the written record of, or during, that discussion,
  not a facilitation guide, an icebreaker, or a set of exercises for structuring the conversation.
- **The team is not going to write anything down at all.** A board that gets erased at the end of the meeting
  with no persisting record is not a smaller version of this document. If the outcome never gets written down,
  nothing here helps.

## Pick a variant

There is, honestly, no choice to make here. This bundle ships **one file**, and that is a finding rather
than a shortcut, because no primary, standards, vendor, or academic source this research found publishes a
second, heavier weight of a sprint retrospective notes document. The genuine variation the research did find
is across **occasions** (a release or project retrospective is a different document with its own chapter in
the literature), not across sizes of this sprint-scoped one. See
[section 4 of the companion](sprint-retrospective-notes_companion.md#4-variants-and-sizing) for the case that
was tested and rejected.

Use `sprint-retrospective-notes_template-lean.md`. There is no second file to reach for. The evidence that
would have earned a heavier weight argues instead for a better single template, one whose columns ask for a
reason and not only an observation, which is what this one does.

## Quality rubric (self-grade)

Score each 0, 1, or 2. Below 11 out of 16 and the document records what the team felt without producing a
change anyone can be held to, the exact failure this family of documents exists to prevent.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Room named honestly** | No sprint identifier, or the list names who was invited | Sprint named by its own identifier, but attendance conflates invited with present | Sprint named by its own identifier, not just a date range, and the present list is distinct from who was invited |
| 2 | **Previous actions checked** | Table missing or blank, or marked N/A without the one honest reason (a true first retrospective) | Some rows from the previous Action Items table carried forward, but at least one is silently missing | Every row from the previous retrospective's Action Items table appears here with a status, and every not-done row carries one honest line on why |
| 3 | **Went well says why** | Entries are morale words with no practice named ("good week") | A specific practice is named, but with no stated reason it helped | Every practice entry states why it worked, concrete enough that someone who was not in the room could repeat it on purpose |
| 4 | **Problems carry an idea** | A problem is stated with nothing attached to it | An idea is attached to some problems, others are left floating | Every problem names both why it happened and at least one candidate idea for changing it |
| 5 | **Actions are owned** | A row has no owner, no date, or names a team rather than a person | Owner and date are present, but the row does not connect to a problem or idea named above | Every row names a person, a date, and traces back to a specific problem or idea named earlier in the document |
| 6 | **Actions pass payback** | An action too small to be worth tracking, or so large it will never be checked done | Sized right, but not stated in a way anyone could check done or not | Every action is checkable done-or-not and could plausibly justify the retrospective time spent finding it |
| 7 | **Scope stays in-sprint** | The notes narrate the causal analysis of a specific failure, why one thing broke, rather than how the team worked | An incident is mentioned but not explicitly pointed at the postmortem, or the boundary is implied rather than stated | If the sprint contained an incident, it is named plainly and its causal analysis is pointed explicitly at the incident-postmortem member of this family; if none occurred, nothing here reads like one anyway |
| 8 | **Specific without assigning blame** | A row names a person as the cause of a problem, or is vague enough to say nothing checkable | The practice or problem is specific, but the wording still reads as pointed at a person | Every entry is specific about what happened and stays aimed at the practice or the system, never at a person |

The test behind every cell above: **could someone satisfy it without improving the document?** A row that
counted rows in a table, or counted how many action items were listed, would reward padding. Every cell
instead asks whether a specific piece of evidence exists, and whether a second person, not the author, could
find it and check it.

## Named anti-patterns (the usual wrecks)

1. **Action items nobody checks.** A failure named independently by two of the sources behind this bundle: an
   action item lands in one retrospective's notes and nobody looks at it again. Previous Actions exists precisely to
   catch this; leaving it blank or perfunctory reopens the exact gap it was built to close.
2. **An action item with no owner.** A row with no name attached is an observation wearing an action item's
   clothing. The team can agree something should change and still produce nothing, because nobody owns doing
   it.
3. **The retrospective as the first casualty of time pressure.** Cutting the retrospective whenever the
   sprint runs long teaches the team that this document is optional, and it stops being read the moment it
   stops being reliably written.
4. **Blame despite the intent to be blameless.** A retrospective that turns into whose fault something was,
   instead of what pattern the team wants to change, costs the willingness to speak honestly next time, and
   the notes read as a grievance list rather than a working document.
5. **Discussion with no follow-through.** Naming a problem and then not acting on it, sprint after sprint,
   teaches the team that raising an issue changes nothing. This is distinct from an unowned action item: the
   item may even have an owner and a date and still never get done.
6. **Reflection without a reason.** A "what went well" or "what to improve" entry that states only what
   happened, never why, cannot be repeated on purpose or avoided on purpose. This is the dominant pattern the
   research behind this bundle found in real retrospective content, and it is the specific failure the Why
   columns in this document are built to answer.
7. **Retrospective and postmortem, run on the wrong occasion.** Running this document's discussion on an
   incident produces a discussion of a thing that needed causal analysis; running a postmortem's causal
   analysis on an ordinary sprint pathologizes normal work. Keep the trigger straight: a period, on a
   cadence, against an event, triggered by it.
8. **An unvarying format, sprint after sprint.** The same three questions asked the same way stop producing
   new information once the team can predict its own answers before the meeting starts. If what comes back
   has stopped changing, the format is due for a change, not the team.

## Pairing with your process

This bundle ships in the `process-docs` family alongside the incident postmortem. The two exist to be told
apart by trigger, not by tone: this document looks back on a **period**, on a cadence, at how the team
worked; the postmortem looks back on an **event**, triggered by it, at why one specific thing failed. If a
sprint contained an incident, write it up once, in the postmortem, and point to it from here rather than
duplicating the causal analysis in both places.
