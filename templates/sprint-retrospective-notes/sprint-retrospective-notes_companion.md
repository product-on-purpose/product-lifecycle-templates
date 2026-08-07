# Companion: Sprint Retrospective Notes

> The deep explainer for the sprint-retrospective-notes bundle. Read this to understand what a sprint
> retrospective notes document actually is, why Scrum itself never asked a team to write one, and where the
> shape everyone uses actually comes from. The short operator card is
> [`sprint-retrospective-notes_guide.md`](sprint-retrospective-notes_guide.md); a fully worked instance is
> [`sprint-retrospective-notes_example.md`](sprint-retrospective-notes_example.md). Inline citations like
> [[1]](#ref-1) resolve to the [References](#references) at the bottom, tagged by source reliability. The
> full retrieval trail is
> [`sprint-retrospective-notes_research-log.md`](sprint-retrospective-notes_research-log.md).

---

## 1. Orientation

A sprint retrospective notes document is a written record of a Sprint Retrospective: what the team said
went well, what it said needed to improve, and which of those improvements someone actually owns. The
Scrum Guide itself names only an event, whose stated purpose is "to plan ways to increase quality and
effectiveness," and never names a document as its output [[1]](#ref-1). This bundle exists because
the discipline that makes a retrospective worth holding, converting a discussion into one owned, dated
change, is not the discipline the canon requires. It is the discipline a written notes template supplies.

At a glance:

- **The Scrum Guide defines an event, not an artifact.** A literal search of the full 2020 text returns
  zero occurrences of "action item," "retrospective notes," "notes," "root cause," and "blameless." "What
  went well" occurs once [[1]](#ref-1).
- **Scrum used to require the output to travel forward, and stopped.** The 2017 Guide required the Sprint
  Backlog to include "at least one high priority way in which the team works, identified in the previous
  Retrospective meeting" [[33]](#ref-33). The 2020 Guide softened that to "They may even be added to the
  Sprint Backlog for the next Sprint" [[1]](#ref-1). A requirement became a permission.
- **The document exists, but only at vendor tier.** Documentero [[2]](#ref-2), Smartsheet
  [[3]](#ref-3), and Atlassian's Confluence Retrospective Blueprint [[4]](#ref-4) each publish a real,
  fixed-heading document. No primary, standards, or academic source does. Two widely used
  practitioner resources, Retromat [[5]](#ref-5) and Fun Retrospectives [[6]](#ref-6), are catalogs of
  facilitation activities rather than documents. Both were confirmed to exist but not read, so nothing
  here rests on their contents and no claim is made about how widely they are cited.
- **The three-column shape nobody can trace.** "What Went Well / What To Improve / Action Items" has no
  originating publication [[7]](#ref-7)[[8]](#ref-8)[[9]](#ref-9). Even Start/Stop/Continue and Mad/Sad/Glad
  are untraceable at the vendors whose business is cataloguing retrospective techniques
  [[12]](#ref-12)[[13]](#ref-13).
- **Nothing measured shows a retrospective improves outcomes.** The three software-specific studies this
  research read in full measure content quality [[21]](#ref-21), participant perception
  [[22]](#ref-22), and practice [[23]](#ref-23), never velocity, defect rate, or predictability. The
  largest, 963 statements across 32 teams, found 84.1 percent were bare assertions with no justification
  and exactly one statement in 963 weighed a pro against a con [[21]](#ref-21).

---

## 2. Origins and evolution

**Scrum's own history moved in the direction of less obligation, not more.** The 2017 Guide tied
retrospective output to the next Sprint Backlog by requirement [[33]](#ref-33); the 2020 rewrite loosened
that language into a possibility [[1]](#ref-1). Scrum's own revision notes name the change directly,
describing the edition as less prescriptive [[33]](#ref-33).

**The word "retrospective" was not coined by Norman Kerth as a deliberate replacement for "postmortem."**
His own preface calls the ritual "called by many names - postmortem or postpartum, for example, or, my
preference, retrospective" [[14]](#ref-14). That is a stated preference among names already in
circulation, not an argued rebranding, and no source read in this research could verify the widespread
story that he replaced the term with a stated rationale. A reader's summary of the book attributes the
specific word to two fellow facilitators, Wayne and Eileen Strider, who "suggested that we call what we do
a retrospective" because it "didn't carry any loaded meanings" [[19]](#ref-19); this account is second-hand
rather than Kerth's own text, and is recorded as such (see [section 6](#6-debates-and-contested-boundaries)).

**Kerth's book does draw this family's central distinction, structurally.** Chapter 7, "Leading a
Postmortem," carries a section titled "Some Important Differences Between Retrospectives and Postmortems,"
and reserves "postmortem" for reviewing failed projects specifically, distinct from the general-purpose
retrospective [[14]](#ref-14). That structural anchor, read from the book's own table of contents, is a
stronger basis for the retro-versus-postmortem line than any framing this research could otherwise verify
(see [section 8](#8-relationships-to-other-artifacts)).

**The Prime Directive itself has an origin story distinct from the format debate.** Kerth traces it to a
sailing tragedy: "During one heavy-weather race a friend of mine capsized and drowned. Top sailors... led a
fearless review of every aspect of the race... for no other reason than to help the entire sailing
community learn how to prevent another death" [[15]](#ref-15). He wrote the Directive down only once he
began teaching the practice to others, not as part of running it himself [[15]](#ref-15).

**The book that popularized scaling the practice beyond Kerth's own scope is Derby and Larsen's.** Where
Kerth's handbook centers on end-of-project reviews, Agile Retrospectives explicitly extends the practice:
"you don't have to wait until the end of a project to do a retrospective... you can hold retrospectives at
releases, milestones, or at regular intervals" [[11]](#ref-11). Its own activities are written to scale by
occasion, "Use this to gather data in a longer iteration, release, or project retrospective" [[7]](#ref-7),
across a five-phase structure independently confirmed by a named reviewer: "Set the Stage," "Gather Data,"
"Generate Insights," "Decide What to do," "Close the Retrospective" [[8]](#ref-8).

**No format used today traces to a named origin.** Start/Stop/Continue and Mad/Sad/Glad are described by
Retrium, a vendor whose business is cataloguing these techniques, without attribution to any person, book,
or organization; Mad/Sad/Glad is called only "a classic exercise" [[12]](#ref-12)[[13]](#ref-13).

---

## 3. Anatomy (section by section)

This bundle ships one size, `lean`, in five sections: Sprint and Participants, Previous Actions, What Went
Well, What To Improve, Action Items (see [section 4](#4-variants-and-sizing) for why no second size ships).

### Sprint and Participants

**What it is.** The identifying header: which sprint this retrospective covers and who was in the room.

**Why it exists.** This renders Documentero's own "Meeting Information" heading [[2]](#ref-2) for a sprint
context. No source argues against recording this; it is the least contested section in the template.

*Beginner note:* name the sprint by its own identifier, not by a date range alone, so the notes stay
findable against the sprint backlog they discuss.

*Expert note:* record who was present, not who was invited. A retrospective's discussion is only as honest
as the room that held it, and a later reader needs to know whose account this is.

### Previous Actions

**What it is.** A check on the action items the last retrospective produced: done, in progress, or dropped.

**Why it exists. This section is this bundle's own contribution; no published template carries it**
[[2]](#ref-2)[[3]](#ref-3)[[4]](#ref-4). It exists for two reasons this research documents directly. First,
Wolpers names exactly this gap as a named anti-pattern: "The team does not check the status of the action
items from previous Retrospectives" [[26]](#ref-26). Second, the mechanism Scrum itself used to carry
retrospective output forward is now optional rather than required [[33]](#ref-33)[[1]](#ref-1). Nothing in
the field's own literature prescribes this section; it is this bundle's answer to a documented failure, not
a restatement of received practice.

*Beginner note:* pull last sprint's Action Items rows forward verbatim and mark each one done, in progress,
or dropped, with one line on why if dropped. Do not silently omit a row that was not finished.

*Expert note:* a Previous Actions section with nothing carried forward, sprint after sprint, is more
plausibly a sign that nobody is reading the section than that the team has run out of improvement work.
Nothing in this research measured how often that is true, so treat it as a prompt to go and check rather
than as a diagnosis. It is the exact failure the section exists to catch.

### What Went Well

**What it is.** The team's own account of what worked in the sprint.

**Why it exists.** This is the one phrase the Scrum Guide itself supplies: the Sprint Retrospective is where
the team discusses "what went well during the Sprint" [[1]](#ref-1). All three vendor templates carry a
version of this heading [[2]](#ref-2)[[3]](#ref-3).

*Beginner note:* write specific practices, not general morale ("pairing on the entitlement fix caught the
edge case before staging," not "good week").

*Expert note:* a notes template whose columns only ask *what* reproduces exactly the shallowness the
largest study of retrospective content measured: 84.1 percent of statements gave no reason at all
[[21]](#ref-21). Ask the author to say why something worked, not only that it did.

### What To Improve

**What it is.** What the team says did not work, and any idea for changing it.

**Why it exists.** This heading carries two separate vendor headings folded together: Documentero's "What
Didn't Go Well" and "Ideas for Improvement" [[2]](#ref-2), and Smartsheet's "What Went Poorly?" and "What
New Ideas Do We Have?" [[3]](#ref-3). Folding observation and proposed change into one section keeps a
problem attached to an idea rather than letting it float unaddressed.

*Beginner note:* for every problem named, write at least one candidate change, even a rough one. A problem
with no attached idea tends to become an Action Items row with no substance behind it.

*Expert note:* the same shallowness finding applies here with more force. Only 13 percent of the statements
in the largest study read gave a justification for a strategy to stop, start, or continue, and only one
statement in 963 weighed a pro against a con [[21]](#ref-21). Push past "what didn't work" to "why," which
is the difference between an observation and a diagnosis.

### Action Items

**What it is.** The commitments the retrospective actually produces: what will change, who owns it, and by
when.

**Why it exists.** This renders Smartsheet's "What Actions Will We Take?" [[3]](#ref-3) and Documentero's
"Action Items" [[2]](#ref-2). It is also the section this whole bundle exists to make binding, because
unowned action items are a failure mode that two independent sources name
[[26]](#ref-26)[[27]](#ref-27). Nothing read ranks the failure modes against each other, so this bundle
does not rank them either.

*Beginner note:* every row needs an owner and a date. A row with neither is an observation wearing an
action item's clothing.

*Expert note:* Cohn frames the discipline as a payback test: "Whatever improvement they identify needs to
be able to pay back 480 minutes of savings for that retrospective to have been worth the effort"
[[27]](#ref-27). An action item too small to be worth tracking is a candidate for cutting, not for writing
down and ignoring.

---

## 4. Variants and sizing

**One format, one size, `lean`.** No source read publishes two weights of a sprint retrospective notes
document [[2]](#ref-2)[[3]](#ref-3)[[4]](#ref-4). This is the first build spec this library's own research
has confirmed rather than corrected, and it is confirmed on evidence rather than by default.

The genuine counter-argument was tested and rejected. Derby and Larsen scope their activities to "an
iteration, release, or project retrospective," vary timing with "the length of the increment of work," and
give release and project retrospectives their own chapter [[7]](#ref-7)[[9]](#ref-9); InfoQ independently
confirms this was the book's explicit aim [[11]](#ref-11). That is real variation, but it is variation
across **occasions**, not weights of one document: a separate named source distinguishes a sprint
retrospective from a release retrospective as different things on scope and strategic framing, "Sprint
retrospectives are tactical... Release retrospectives are strategic" [[30]](#ref-30), not as two sizes of
one template. A team running a release or project retrospective is reaching for a different occasion, not
a `full` variant of this document.

The evidence that would have earned a second weight argues instead for a richer single template, which is
what the shallowness finding independently recommends [[21]](#ref-21): the fix for a thin retrospective is
not more headings, it is headings that ask for a reason.

**Format verdict.** Start/Stop/Continue, Mad/Sad/Glad, 4Ls, Starfish, and Sailboat circulate widely
[[3]](#ref-3)[[12]](#ref-12)[[13]](#ref-13), but they are facilitation activities, not document shapes, and
none is published by a named source as a notes template in its own right. Smartsheet repackages several as
fillable documents [[3]](#ref-3), which this bundle treats as a vendor's packaging decision rather than a
format in circulation with its own named source, consistent with ADR 0028 (the format-axis decision that
requires a shape be structurally distinct and independently attested before it ships as its own format,
[ADR 0028](../../docs/internal/decisions/0028-adopt-a-format-axis.md)).

---

## 5. Methodology lineage

| School | Treatment | What it optimizes for |
|---|---|---|
| **Scrum canon (2020)** | Names the event only; retrospective output "may even be added" to the next Sprint Backlog [[1]](#ref-1). | A team's own inspect-and-adapt discussion, undocumented by requirement. |
| **Scrum canon (2017, superseded)** | The same event, plus a structural requirement that at least one improvement travel into the next Sprint Backlog [[33]](#ref-33). | The same discussion, with a named mechanism forcing at least one change to persist. |
| **Kerth's project retrospectives** | An end-of-project review, structured around the Prime Directive, with "postmortem" reserved for failed projects specifically [[14]](#ref-14). | Learning from a project's whole arc, without inviting blame. |
| **Derby and Larsen's custom-fit retrospective** | A five-phase facilitation structure, Set the Stage through Close, with activities that scale to iteration, release, or project cadence [[7]](#ref-7)[[8]](#ref-8)[[10]](#ref-10)[[11]](#ref-11). | A retrospective sized and shaped to the team and the occasion, not one fixed script. |
| **Vendor template tier** | Fixed-heading, downloadable documents: Documentero, Smartsheet, Atlassian [[2]](#ref-2)[[3]](#ref-3)[[4]](#ref-4). | A written, filed record, the only tier that actually publishes one. |
| **Incident-response tier** | Uses "retrospective" for the incident-triggered review itself; Honeycomb prefers "blame-aware" to "blameless" [[31]](#ref-31), FireHydrant splits "retrospective" into an incident-triggered type and a post-project type [[32]](#ref-32). | Causal understanding of a specific failure, under a vocabulary that overlaps this family's own. |

---

## 6. Debates and contested boundaries

### 6.1 Is confusing a retrospective with a postmortem actually a documented failure mode?

This library's own family contract asserts that running a retro on an incident produces "a blameless
discussion of a thing that needed a causal analysis," and running a postmortem on a sprint "pathologises
ordinary work." **No source read in full states this.** Sources do draw the retro/postmortem line by
purpose and timing [[28]](#ref-28)[[29]](#ref-29), but none frames confusing the two as a named failure
mode anyone has observed. This companion carries the contract's framing as this library's own reasoning,
not as a sourced finding, and says so plainly here.

### 6.2 Do "retrospective" and "postmortem" even name distinct practices?

Agile-side sources draw a clean line: Parabol frames postmortems as attempts "to understand what went
wrong" after "a big milestone, a project, or an incident" [[28]](#ref-28), and Jonathan Hall states the
distinction directly, "postmortems serve to understand root causes of incidents" [[29]](#ref-29).
Incident-response-side sources use "retrospective" for exactly that same incident review: Honeycomb calls
its process an "incident retrospective" and never uses "postmortem" at all [[31]](#ref-31); FireHydrant
titles its own material "Blameless Retrospectives" and splits "retrospective" into an incident-triggered
type and a post-project type [[32]](#ref-32). Neither camp is wrong. They are using one word for different
referents, which this research treats as the most useful thing this companion can tell a reader (see
[section 8](#8-relationships-to-other-artifacts)).

### 6.3 The Prime Directive's exact wording is not stable

The wording splits three ways, not two. The commonly circulated version reads "we understand and truly
believe" with neutral pronouns [[17]](#ref-17)[[20]](#ref-20); a secondary account keeps "we understand"
but carries gendered pronouns [[15]](#ref-15); only the publisher blurb reads "we must understand"
[[18]](#ref-18). Chapter 1 of Kerth's book, where the Directive itself
lives, was outside the sample this research could retrieve. This companion quotes the commonly circulated
wording and says so.

### 6.4 Is the Prime Directive sound?

Philippe Kruchten challenges it directly: "The Prime Directive sounds pretty naive to me, in terms of the
reality of human nature" [[15]](#ref-15). Esther Derby answers pragmatically rather than rebutting the
critique, arguing it is "virtually impossible to learn from someone you've written off as stupid"
[[15]](#ref-15). A separate, independent practitioner piece rejects the Directive outright as "fairly empty"
and lacking authenticity [[16]](#ref-16). This is a live, two-sided argument among named people, not a
settled matter.

### 6.5 Did Kerth coin the word "retrospective"?

His own preface frames it as a preference among names already circulating, not a coinage [[14]](#ref-14).
The specific naming story, that facilitators Wayne and Eileen Strider suggested the word to him, appears
only in a reader's summary of the book [[19]](#ref-19); Kerth's acknowledgements do thank both people
[[14]](#ref-14), which is consistent, but the story itself could not be verified against his own text.

### 6.6 Is the reported trust-drop finding usable?

A 2025 paper reports, citing a separate industrial case study it does not itself name, that "the only
negative change was the level of trust in the relationship between team members dropped after the
retrospective" [[24]](#ref-24). This is a second-hand citation inside a fetched paper, not that paper's own
primary finding. It is recorded here and treated as weaker than the directly attributed failure modes from
Wolpers and Cohn [[26]](#ref-26)[[27]](#ref-27), not as an established fact on its own.

---

## 7. Anti-patterns and failure modes

1. **Action items nobody checks.** "The team does not check the status of the action items from previous
   Retrospectives" [[26]](#ref-26). This is exactly the gap Previous Actions exists to close (see
   [section 3](#3-anatomy-section-by-section)).
2. **No owner, no accountability.** "At the last Retrospective, the team members accepted action items.
   However, no one took responsibility for the delivery" [[26]](#ref-26).
3. **The retrospective as the first casualty of time pressure.** "The Scrum team cancels Retrospectives if
   more time is needed to accomplish the Sprint Goal" [[26]](#ref-26).
4. **Blame despite the Prime Directive.** "The Retrospective is an endless cycle of blame and
   finger-pointing" [[26]](#ref-26).
5. **Discussion with no follow-through.** "The Scrum team uses the Retrospective primarily to complain
   about the situation and assumes the victim's role... not moving on once you have identified critical
   issues and trying to change them defies the purpose" [[26]](#ref-26). Cohn names the same pattern from
   the other side: "Retrospectives can quickly feel worthless if people commitment to changes they don't
   deliver on" [[27]](#ref-27).
6. **Dishonesty in the room.** "People fail to bring up real issues or admit to their problems"
   [[27]](#ref-27).
7. **Monotony from an unvarying format.** Named directly by Cohn as a distinct, separate problem from the
   others above [[27]](#ref-27).
8. **Reflection without justification.** 84.1 percent of the statements in the largest study read gave no
   reason for a stop, start, or continue claim, and only one statement in 963 weighed a pro against a con
   [[21]](#ref-21). This is the failure the guidance for What Went Well and What To Improve is written
   against (see [section 3](#3-anatomy-section-by-section)).
9. **Perceived as a waste of time.** A surveyed team's own words: "Retros are important; however... the
   team's execution of retros right now is poor and... a waste of time" [[23]](#ref-23).
10. **Defensiveness during critique.** Surfacing a problem "can sometimes lead to what feels like a need
    for the team to 'defend' or 'explain' behaviour" [[23]](#ref-23), a strain on the same psychological
    safety the Prime Directive exists to protect.
11. **Data collected and never used.** "Although teams routinely collect project data, they seldom employ
    it systematically" [[23]](#ref-23); one team's own words: "Our retrospectives are mostly based on what
    people felt went right or wrong... It isn't very metric-centric" [[23]](#ref-23).

---

## 8. Relationships to other artifacts

- **Sibling in this family, opposite trigger: the incident postmortem.** This is this family's central
  teaching point, and it is worth stating precisely. A sprint retrospective notes document looks back on a
  **period**, on a cadence, at how the team worked. An incident postmortem looks back on an **event**,
  triggered by it, at why a specific thing failed. Kerth's own book draws this line structurally, reserving
  "postmortem" for reviewing failed projects and treating the general-purpose retrospective as the broader
  category [[14]](#ref-14). This library's family contract goes further and names the common real-world
  error, running a retro on an incident or a postmortem on a sprint, as a documented failure mode; this
  research could not independently confirm that framing (see
  [section 6](#6-debates-and-contested-boundaries)), and it is carried here as the library's own reasoning
  about why the boundary matters, not as a sourced finding.
- **The same word, used two ways, in the wild.** A reader who works incident response will meet
  "retrospective" meaning the incident review itself: Honeycomb's own incident process is called an
  "incident retrospective" [[31]](#ref-31), and FireHydrant's material, titled "Blameless Retrospectives,"
  splits "retrospective" into an incident-triggered type and a post-project type [[32]](#ref-32). These are
  live, named counterexamples to a clean vocabulary split, and this companion carries them rather than
  filtering them out, because teaching the boundary honestly means admitting the industry does not hold it
  consistently.
- **Feeds into: the Sprint Backlog.** Under the 2017 Guide, retrospective output was structurally required
  to travel into the next Sprint Backlog [[33]](#ref-33); the 2020 Guide made that optional
  [[1]](#ref-1). Previous Actions exists in part to compensate for that removed obligation (see
  [section 3](#3-anatomy-section-by-section)).
- **Adjacent, different occasion, not a bigger size: the release retrospective.** A named source
  distinguishes a sprint retrospective from a release retrospective on scope and framing, tactical against
  strategic [[30]](#ref-30). Reaching for a release or project retrospective is reaching for a different
  occasion this bundle does not cover, not for a `full` variant of this document (see
  [section 4](#4-variants-and-sizing)).
- **Historical relative, not the same evidence base: general debriefing research.** The widely circulated
  "25 percent improvement in performance" statistic traces to Tannenbaum and Cerasoli's meta-analysis of
  debriefs across military, aviation, and medical settings, a source that contains no claim about software
  teams at all [[25]](#ref-25). This companion cites it only as the substitution it is, not as evidence
  about sprint retrospectives.

---

## 9. Adaptations

- **A team just starting the practice.** The one lean template is the whole document; there is no fuller
  variant to grow into (see [section 4](#4-variants-and-sizing)). Previous Actions is the one section that
  compensates for the Scrum Guide's now-optional carry-forward of retrospective output
  [[33]](#ref-33)[[1]](#ref-1), so it is worth keeping even when a new team is tempted to trim the template
  down further.
- **A sprint that contained an incident.** Use the incident-postmortem member of this family for the
  causal analysis of the specific event, and keep this document scoped to the whole sprint's working
  pattern. Naming the incident and stating explicitly that its causal analysis belongs elsewhere is the
  honest move, not silence about it (see [section 8](#8-relationships-to-other-artifacts)).
- **A release, milestone, or project boundary.** This is a different occasion, covered by Derby and
  Larsen's own release and project retrospective material [[7]](#ref-7)[[9]](#ref-9), not a bigger size of
  this sprint-scoped template (see [section 4](#4-variants-and-sizing)).
- **A team resistant to the format.** The honest answer is that no primary or standards source requires
  this document at all; the Scrum Guide asks only for a discussion [[1]](#ref-1). What the discussion loses
  without a written record is exactly what the largest study of retrospective content measured missing:
  justification, and a place for a decision to be found again later [[21]](#ref-21).

---

## 10. Worked example pointer

[`sprint-retrospective-notes_example.md`](sprint-retrospective-notes_example.md) is the fully worked
instance. Per this family's own contract, it covers the same sprint as the `sprint-backlog` example's own
scenario, Sprint 24, without becoming an account of the DEF-2291 incident that also occurred in that
sprint. The example earns the family's distinction the honest way, by naming the incident and stating
plainly that its causal analysis belongs to the incident-postmortem member of this family, rather than by
staying silent about an event the team plainly lived through.

---

## References

Tagged by reliability, following this bundle's own four-way split (its research log records 9 primary,
3 standards, 11 practitioner, and 10 vendor sources among the 33 read, 31 fetched-and-verified and 2
url-confirmed-not-read): `[primary]` the originating or standards-body source itself; `[standards]` a
named professional body's own guidance page, distinct from an originating primary text; `[practitioner]`
a recognized independent authority; `[vendor]` commercially motivated, reliable on convention. Researched
2026-08-07. Retrieval status per source is recorded in
[`sprint-retrospective-notes_research-log.md`](sprint-retrospective-notes_research-log.md); only sources
marked fetched-and-verified there are quoted here.

<a id="ref-1"></a>[1] Ken Schwaber and Jeff Sutherland. "[The Scrum Guide](https://scrumguides.org/scrum-guide.html)" (2020 version). Scrum.org (accessed 2026-08-07). [primary]

<a id="ref-2"></a>[2] Documentero. "[Retrospective Meeting Notes - Document Template](https://documentero.com/templates/project-management/document/retrospective-meeting-notes/)." documentero.com (accessed 2026-08-07). [vendor]

<a id="ref-3"></a>[3] Smartsheet. "[Agile Retrospective Templates](https://www.smartsheet.com/content/agile-sprint-scrum-retrospective-templates)." smartsheet.com (accessed 2026-08-07). [vendor]

<a id="ref-4"></a>[4] Atlassian. "[Confluence Retrospective Blueprint](https://confluence.atlassian.com/doc/retrospective-blueprint-427623496.html)." confluence.atlassian.com (accessed 2026-08-07). [vendor]

<a id="ref-5"></a>[5] Corinna Baldauf and Timon Fiddike. "[Retromat](https://retromat.org/en/)." retromat.org (accessed 2026-08-07). URL confirmed live; body not read, existence only. [practitioner]

<a id="ref-6"></a>[6] FunRetrospectives.com. "[Retrospective activity category listing](https://www.funretrospectives.com/category/retrospective/)." funretrospectives.com (accessed 2026-08-07). URL confirmed live; body not read, existence only. [practitioner]

<a id="ref-7"></a>[7] Esther Derby and Diana Larsen. "[Agile Retrospectives: Making Good Teams Great](https://media.pragprog.com/titles/dlret/Activities.pdf)," official publisher excerpt. Pragmatic Bookshelf (accessed 2026-08-07). [primary]

<a id="ref-8"></a>[8] Johanna Rothman. "[Review of Agile Retrospectives: Making Good Teams Great](https://www.jrothman.com/mpd/2006/08/agile-retrospectives-making-good-teams-great/)." jrothman.com (accessed 2026-08-07). [practitioner]

<a id="ref-9"></a>[9] Goodreads. "[Agile Retrospectives: Making Good Teams Great](https://www.goodreads.com/book/show/721338.Agile_Retrospectives)," book page and table of contents. goodreads.com (accessed 2026-08-07). [standards]

<a id="ref-10"></a>[10] Agile Alliance. "[Agile Retrospectives: Making Good Teams Great](https://agilealliance.org/resources/books/agile-retrospectives-making-good-teams-great/)," book resource page. agilealliance.org (accessed 2026-08-07). [standards]

<a id="ref-11"></a>[11] InfoQ. "[New Agile Retrospectives Book](https://www.infoq.com/news/New-Agile-Retrospectives-Book)," news article. infoq.com (accessed 2026-08-07). [standards]

<a id="ref-12"></a>[12] Retrium. "['Start Stop Continue' technique page](https://www.retrium.com/retrospective-techniques/start-stop-continue)." retrium.com (accessed 2026-08-07). [vendor]

<a id="ref-13"></a>[13] Retrium. "['Mad Sad Glad' technique page](https://www.retrium.com/retrospective-techniques/mad-sad-glad)." retrium.com (accessed 2026-08-07). [vendor]

<a id="ref-14"></a>[14] Norman L. Kerth. "[Project Retrospectives: A Handbook for Team Reviews](https://ptgmedia.pearsoncmg.com/images/9780133488579/samplepages/0133488578.pdf)," official Pearson/InformIT free sample chapter PDF. Dorset House, 2001 (accessed 2026-08-07). [primary]

<a id="ref-15"></a>[15] InfoQ. "[Questioning the Retrospective Prime Directive](https://www.infoq.com/articles/retrospective-prime-directive/)," reported discussion including Philippe Kruchten, Esther Derby, Norm Kerth. infoq.com, 2008 (accessed 2026-08-07). [practitioner]

<a id="ref-16"></a>[16] The Scrum Academy. "[The Retrospective Prime Directive Is Kinda Silly](https://thescrumacademy.com/2015/04/07/the-retrospective-prime-directive-is-kinda-silly/)." thescrumacademy.com, 2015 (accessed 2026-08-07). [practitioner]

<a id="ref-17"></a>[17] Agile Retrospective Resource Wiki. "[The Prime Directive](https://retrospectivewiki.org/index.php?title=The_Prime_Directive)." retrospectivewiki.org (accessed 2026-08-07). [practitioner]

<a id="ref-18"></a>[18] Google Books. "[Project Retrospectives: A Handbook for Team Reviews](https://books.google.com/books/about/Project_Retrospectives.html?id=3VUUAAAAQBAJ)," about-the-book page. books.google.com (accessed 2026-08-07). [vendor]

<a id="ref-19"></a>[19] Goodreads. "[Project Retrospectives: A Handbook for Team Reviews](https://www.goodreads.com/book/show/1523368.Project_Retrospectives)," book page, reviewer Toni Tassani's summary. goodreads.com (accessed 2026-08-07). [vendor]

<a id="ref-20"></a>[20] FunRetrospectives. "[The Retrospective Prime Directive](https://www.funretrospectives.com/the-retrospective-prime-directive/)." funretrospectives.com (accessed 2026-08-07). [practitioner]

<a id="ref-21"></a>[21] Christopher Hundhausen, Phillip Conrad, Ahsun Tariq, Surya Pugal, and Bryan Zamora Flores. "[An Empirical Study of the Content and Quality of Sprint Retrospectives in Undergraduate Team Software Projects](https://dl.acm.org/doi/10.1145/3639474.3640074)." ICSE-SEET '24 (accessed 2026-08-07). [primary]

<a id="ref-22"></a>[22] Adam Przybylek and co-researchers. "[Game-based Sprint retrospectives: multiple action research](https://pmc.ncbi.nlm.nih.gov/articles/PMC8527976/)." Empirical Software Engineering, 2021 (accessed 2026-08-07). [primary]

<a id="ref-23"></a>[23] Alessandra Maciel Paz Milani, Margaret-Anne Storey, Vivek Katial, and Lauren Peate. "[Exploring Retrospective Meeting Practices and the Use of Data in Agile Teams](https://arxiv.org/html/2502.03570v1)." CHASE 2025, IEEE/ACM (accessed 2026-08-07). [primary]

<a id="ref-24"></a>[24] Maria Spichkova, Hina Lee, Kevin Iwan, Madeleine Zwart, Yuwon Yoon, and Xiaohan Qin. "[Agile Retrospectives: What went well? What didn't go well? What should we do?](https://arxiv.org/html/2504.11780v1)" arXiv preprint, 2025 (accessed 2026-08-07). Cites the trust-drop finding from a separate, unnamed industrial case study rather than originating it; see [section 6](#6-debates-and-contested-boundaries). [primary]

<a id="ref-25"></a>[25] Scott I. Tannenbaum and Christopher P. Cerasoli. "[Do Team and Individual Debriefs Enhance Performance? A Meta-Analysis](https://cdn.ymaws.com/www.odnetwork.org/resource/resmgr/2013_education/tannenbaum_using_debriefs_ha.pdf)." Human Factors, 2013 (accessed 2026-08-07). A meta-analysis of debriefs in general, not sprint retrospectives; cited only as the source of the "25 percent" figure this bundle declines to apply to software teams. [primary]

<a id="ref-26"></a>[26] Stefan Wolpers. "[21 Sprint Retrospective Anti-Patterns](https://age-of-product.com/sprint-retrospective-anti-patterns/)." age-of-product.com, cross-posted scrum.org (accessed 2026-08-07). [practitioner]

<a id="ref-27"></a>[27] Mike Cohn. "[Sprint Retrospectives: Solutions to 4 Common Problems](https://www.mountaingoatsoftware.com/blog/overcoming-four-common-problems-with-retrospectives)." Mountain Goat Software blog (accessed 2026-08-07). [practitioner]

<a id="ref-28"></a>[28] Parabol. "[Post-mortems vs Retrospectives: What's the Difference](https://www.parabol.co/blog/retrospectives-vs-post-mortems/)," unsigned company blog. parabol.co (accessed 2026-08-07). [vendor]

<a id="ref-29"></a>[29] Jonathan Hall. "[Retrospectives or Postmortems?](https://jhall.io/archive/2021/07/31/retrospectives-or-postmortems/)" jhall.io, also mirrored on DEV Community (accessed 2026-08-07). [practitioner]

<a id="ref-30"></a>[30] TeamRetro. "[Sprint retrospective vs. release retrospective](https://www.teamretro.com/blog/sprint-retrospective-vs-release-retrospective/)," unsigned company blog. teamretro.com (accessed 2026-08-07). [vendor]

<a id="ref-31"></a>[31] Honeycomb. "[The Incident Retrospective Best Practices](https://www.honeycomb.io/blog/incident-retrospective-ground-rules)," ground rules post, company engineering blog. honeycomb.io (accessed 2026-08-07). [practitioner]

<a id="ref-32"></a>[32] FireHydrant. "[What are Blameless Retrospectives? How Do You Run Them?](https://firehydrant.com/blog/what-are-blameless-retrospectives-do-they-work-how/)," company blog. firehydrant.com (accessed 2026-08-07). [vendor]

<a id="ref-33"></a>[33] Scrum.org / scrumguides.org editorial team. "[Changes between 2017 and 2020 Scrum Guides](https://scrumguides.org/revisions.html)," revision-history page. scrumguides.org (accessed 2026-08-07). [primary]
