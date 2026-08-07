# Guide: Incident Postmortem (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`incident-postmortem_companion.md`](incident-postmortem_companion.md). A fully worked instance is
[`incident-postmortem_example.md`](incident-postmortem_example.md).

## When to use

- A specific criterion your team published in advance actually fired: user-visible downtime past a
  threshold, data loss, an on-call engineer having to intervene, a resolution time past a threshold, or a
  monitoring gap that meant the incident was found by hand rather than by an alert. The canon's own list of
  triggers is in `incident-postmortem_companion.md` section 1; write your own team's version of it before
  you need this document, not while you are filling one in.
- One specific event failed, and you need to explain why, not how a period of work went in general.
- The event is over, or at least stable enough to analyze; a postmortem is written after, not during.
- Follow-up work will need to be tracked somewhere your team already tracks work: the product backlog, a
  risk register, or a RAID log. If nothing here is going to produce a ticket, this document will not do its
  job. See "Leaving action items only in this document" under anti-patterns below.

## When NOT to use

- **The trigger is a date on the calendar, not an event.** If what happened is "two weeks passed," reach
  for `sprint-retrospective-notes` instead. That document looks back on a period, on a cadence, at how the
  team worked; this one is event-triggered, about one specific thing that failed. Running a retrospective on
  an incident produces a blameless discussion of a thing that needed a causal analysis; running a postmortem
  on an ordinary sprint pathologizes normal work. Neither substitutes for the other. See
  `incident-postmortem_companion.md` section 8.
- **You only need a live record of what happened, not an analysis of why.** A postmortem is written after
  the fact, once there is time to look at logs, code changes, and decisions; a live incident record kept
  during the event is a different artifact. One captures what happened; this one explains why and what
  changes so it does not happen the same way again.
- **You need a facilitator-led discussion, not a document.** The "after-action review" label sometimes
  attached to this document type in other catalogs literally means a live, facilitated conversation running
  something like 30 minutes to 2 hours about a single training event, not a written artifact. The spirit
  matches; the format does not.
- **You are inside an ITIL or ITSM practice tracking a Problem Record.** Expect this document to feed that
  record, not replace it. A Problem Record documents a problem's full history from detection to closure; a
  postmortem is the analysis of one incident that record may reference.
- **Nothing changed, and nothing needs to.** If the honest content of every section would be "this was
  normal operation," you do not have an incident that cleared your team's own trigger criteria. Writing one
  anyway trains the team to treat postmortems as routine paperwork rather than as a signal that something
  worth investigating actually happened.

## Pick a variant

**Lean (five sections)** is Summary, Impact, Timeline, Root Causes, and Action Items. It is the sections
attested across the widest span of published practice, and it is what a reader still needs even from a
one-off, freeform incident report with no fixed template at all.

**Full (nine sections)** adds Detection, Trigger, Resolution, and Lessons Learned, inserted in place rather
than appended, so lean stays a strict ordered subset of full. Notice what the four additions have in common:
none of them is content a reader needs to just know what happened and what is being done about it. Detection
and Trigger are about how the team found out and why this counted; Resolution and Lessons Learned separate
what already happened from what the team now believes differently. Move to full when at least one of these
is true:

- the incident is severe enough, cross-team enough, or novel enough that skipping straight from Impact to
  Root Causes, or from Root Causes to Action Items, would leave a reader unable to tell how it was found,
  which of your team's own criteria made it a postmortem at all, what specifically ended it, or what changed
  about how the team believes it works;
- more than one team could plausibly need to understand the trigger and the resolution, so naming both
  explicitly matters more than it would for a single-team incident;
- the incident revealed something the team wants to remember beyond the specific fix, which belongs in
  Lessons Learned rather than folded into Root Causes.

**The two-size packaging is this bundle's own decision, and it is labeled as such.** No published postmortem
template this bundle's research read ships two sizes; each vendor ships exactly one. What the research does
support is that depth genuinely varies in practice: one vendor's product ships configurable templates keyed
to incident severity, and a real published postmortem from a named organization used no fixed template
structure at all. This library packages that real variation as two sizes; it is not a discovered industry
standard. See `incident-postmortem_companion.md` section 4.

## Quality rubric (self-grade)

Score each 0, 1 or 2. Full below 13 out of 18 has produced exactly what the `process-docs` family contract
warns against: a document that records feelings or a timeline and commits nobody to anything. Lean is scored
on five of these rows only (see the scope table below), and below 7 of 10 the same failure applies to the
smaller shape.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Summary stands alone** | No cause, no duration, no resolution state; a reader who stops here learns nothing | Some of cause, duration, or resolution state is present, but not all three | A reader who stops after this section alone knows what happened, roughly how bad it was, and whether it is over |
| 2 | **Impact is measured** | A category with no number ("some users," "a while") | A number is given for one dimension (duration or magnitude) but not both | Every impact row names an affected system or population, a duration, and a magnitude someone could check against a dashboard or a support queue |
| 3 | **Timeline is checkable** | Vague times ("that afternoon") or several events bundled into one line | Timestamps are present but could not be checked against a log, alert, or chat transcript without asking the author | Every entry has a timestamp precise enough to verify against a real record, and gaps in the timeline are left visible rather than smoothed over |
| 4 | **Root causes are evidenced** | One vague category ("human error") or a person named as the cause | More than one cause is named, but at least one has no evidence behind it | Every listed cause is a specific, checkable condition with evidence (a log line, a config diff, a metric), and none of them is a person's name |
| 5 | **Detection reveals the gap** *(full)* | "We noticed a problem," no named signal, no delay stated | A signal is named, but the delay between failure and detection is not | A named signal (alert, page, customer report) and the delay between the failure starting and someone finding out, stated as a number someone could check |
| 6 | **Trigger is your own** *(full)* | No named criterion, or a borrowed list (the canon's own example list, restated as though it were the team's own) | A criterion is named, but it is not one the team could point to in a document that predates the incident | Names the specific, previously published criterion that fired, and where a reader could go check that it was in fact published before this event |
| 7 | **Resolution is distinct** *(full)* | "We fixed it," no action named, no timestamp | An action is named, but it is not clear whether it already happened or is still planned | Names the specific action that ended the incident, who took it, and when, cross-checkable against the Timeline; work still to come lives in Action Items, not here |
| 8 | **Lessons learned change something** *(full)* | "We should be more careful," indistinguishable from what any postmortem could say | Restates the Root Cause in different words rather than stating a changed belief | States what the team now believes differently about how it works, distinct from the specific fix, in language specific enough to apply to a future, different incident |
| 9 | **Actions are tracked** | A bulleted intention with no owner and no ticket | An owner or a ticket is present, not both, or the ticket has no visible status | Every action names one owner and a ticket in the team's actual tracker, with a status a reader could check, not a wish written down and left in this document |

**Which rows apply to what.**

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| full | all 9 | 18 | **13** |
| lean | 1-4 and 9 | 10 | **7** |

Rows 5, 6, 7 and 8 are scored only against full. Lean ships none of Detection, Trigger, Resolution, or
Lessons Learned, so grading it on those rows would penalize the choice of variant rather than the quality of
the document.

The test behind every cell above: **could someone satisfy it without improving the document?** A row that
counted the number of root causes, timeline entries, or action items would reward padding. Every cell
instead asks whether a specific piece of checkable evidence exists, and whether a reader who was not in the
room could verify it.

## Named anti-patterns (the usual wrecks)

1. **Writing the Summary as a preview of Root Causes.** The Summary is a synopsis for someone who may never
   read past it, not a teaser for the analysis below. If a reader who stops at Summary cannot say what
   happened, how bad it was, and whether it is over, the section has not done its job.
2. **Naming a person as a root cause.** A root cause can never be a person. A postmortem that lands on an
   individual has produced blame, not analysis, and directly contradicts the blameless framing this document
   type is named for.
3. **Restating a borrowed list of trigger criteria as though it were your team's own.** Naming a trigger
   your team never actually published before the incident is inventing a rule retroactively, which defeats
   the entire point of agreeing criteria in advance rather than arguing them during one.
4. **Leaving action items only inside this document.** The moment a postmortem is published, every action
   item needs a ticket in the tracker the team already uses. A postmortem that ends in a bulleted list at
   the bottom of the page rather than tickets in a real tracker has produced a wish list, not follow-up
   work.
5. **Describing a fix as already resolving the incident when the underlying condition is still present and
   only masked.** If the real fix has not shipped yet, say so, and put it in Action Items rather than
   Resolution.
6. **Restating the Root Cause in different words under Lessons Learned.** A lesson is what the team now
   believes about how it works; a root cause is what happened this time. Repeating one under the other's
   heading wastes the section that is supposed to generalize past this specific incident.
7. **Citing an unmeasured percentage as though it were a finding.** Every specific MTTR-reduction or
   recurrence-reduction figure this bundle's research chased traced to a headline with no method, a single
   customer testimonial, or a claim absent from the very document it was attributed to. State the value case
   honestly as an assertion, not as a number nothing behind it supports.
8. **Running a retrospective on an incident, or a postmortem on a sprint.** These are the two members of the
   `process-docs` family, and they exist to be told apart, not blended. A retrospective on an incident
   produces a blameless discussion of something that needed causal analysis; a postmortem on a sprint
   pathologizes ordinary work. If the trigger is a date, it is the other document.

## Pairing with your process

This bundle ships in the `process-docs` family alongside `sprint-retrospective-notes`, and the distinction
between them is this family's central teaching point rather than an incidental note: a retrospective is
cadence-triggered and looks back on a period, at how the team worked; a postmortem is event-triggered and
looks back on one specific thing that failed and why. Before you start either document, name which trigger
you actually have. Once you have written this one, make sure every Action Items row lands somewhere your
team already tracks work: the product backlog, a risk register, or a RAID log. An action recorded and never
done is a real failure mode for this document type, distinct from the analysis itself being wrong, and it
is the one the family contract names explicitly: owned actions with a place they are tracked, not a list of
observations.
