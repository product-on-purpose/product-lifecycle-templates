# sprint-retrospective-notes research log

Researched 2026-08-07 across six parallel dimensions: whether the artifact exists at all, the Scrum Guide by
full text, the structure's real provenance, Kerth and the Prime Directive, evidence and failure modes, and
the boundary against the incident postmortem. **33 sources**, of which **31 fetched-and-verified** and **2
url-confirmed-not-read**, carrying **104 verbatim quotable phrases**. By tier: 11 practitioner, 10 vendor, 9
primary, 3 standards. Retrieval status is recorded per source in the three-token vocabulary the library
gates ([ADR 0029](../../docs/internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md)), and
only `fetched-and-verified` sources are quoted.

**How to read this log.** A `Supports:` clause says what the bundle is allowed to rest on that source for.
A `Quotable:` phrase was read verbatim on the page. If a claim in the companion is not covered by some
entry's `Supports:` clause here, the claim has no home and must be cut, not justified after the fact.

**The canon check for this bundle ran twice.** The first attempt was blocked by a content filter for trying
to reproduce a copyrighted document in full. The re-run asked for short quotations and literal string counts
instead, which is what carried the finding anyway. Both runs are merged into this log, and the Scrum Guide
[1] is one entry rather than three because three separate dimensions claimed it.

---

## Honest framing: the five things this bundle has to say

**1. The Scrum Guide does not ask you to write this down.** Literal case-insensitive counts across the whole
2020 Guide [1]: `action item` **0**, `retrospective notes` **0**, `notes` **0**, `Start Stop Continue` **0**,
`root cause` **0**, `blameless` **0**. `what went well` occurs **once**. All four occurrences of `document`
are unrelated to the retrospective: a Google Tag Manager script reference, a self-reference to the Guide,
and two describing how Scrum's own history was recorded. The Guide names an event and an outcome, never an
artifact. This is the same result the `definition-of-done` research produced against the same source, and it
is the honest starting point for a bundle whose entire subject is a document.

**2. And Scrum removed the one obligation that made retrospective output binding.** The 2017 Guide required
the Sprint Backlog to include "at least one high priority way in which the team works, identified in the
previous Retrospective meeting" [33]. The 2020 edition softened that to "They **may** even be added to the
Sprint Backlog for the next Sprint" [1]. Scrum's own revision notes describe the edition as less
prescriptive and name this softening explicitly [33]. **A requirement became a permission.** That is the
sharpest single fact in this log, and it is the argument for the document: the discipline that Scrum stopped
mandating has to live somewhere, and a written, owned action item is where it lives.

**3. The artifact exists, but only at vendor tier, and the field's centre of gravity is elsewhere.** Three
named sources publish an actual fill-in document with fixed headings: Documentero [2], Smartsheet [3], and
Atlassian's Confluence Retrospective Blueprint [4]. **No primary, standards or academic source publishes
one.** Meanwhile two widely used practitioner resources, Retromat [5] and Fun Retrospectives [6], are catalogs
of facilitation *activities* rather than documents. Both are url-confirmed-not-read, so nothing rests on
their contents, and this log makes no claim about how widely either is cited. This bundle admits under
ADR 0030 because named sources do publish the document, and it says plainly that they are template vendors
rather than authorities. This is a thinner base than `prd` or `test-plan` rest on, and the bundle says so.

**4. The three-part shape this bundle was specified to ship has no traceable origin.** "What Went Well /
What To Improve / Action Items" traces to no primary source. Derby and Larsen's book is organised as five
phases and roughly thirty activities, not three columns [7][8][9]. The Scrum Guide supplies "what went well"
and nothing else [1]. **Start/Stop/Continue and Mad/Sad/Glad are untraceable even to the vendors whose
business is cataloguing retrospective techniques**: Retrium's own pages attribute neither format to any
person, book or organisation, and describe Mad/Sad/Glad only as "a classic exercise" [12][13]. The bundle
ships the shape anyway, because it is what practitioners actually use, and labels it convention rather than
canon.

**5. There is no evidence retrospectives improve outcomes, and the famous number is about something else.**
Three software-specific empirical studies were read in full and none measures outcomes [21][22][23]. The
largest, Hundhausen et al. at ICSE-SEET 2024, analysed 963 statements from 32 teams and found **84.1 percent
were bare assertions with no justification, 13 percent gave a reason, and exactly one statement in 963
weighed a pro against a con** [21]. That is a finding about the practice's shallowness, and it is a direct
argument for a notes template that asks *why*. Separately, the widely circulated "25 percent improvement in
performance" traces to Tannenbaum and Cerasoli's 2013 meta-analysis of **debriefs in general** across
military, aviation and medical settings [25], which contains no claim about software teams at all. It is
cited in this bundle only as the substitution it is. Amy Edmondson's psychological-safety research is
adjacent and genuinely relevant, was **not** retrievable, and is therefore quoted nowhere.

## What Kerth actually said, against what he is said to have said

Two corrections that matter to this family, both from the primary text [14].

- **Kerth did not rebrand "postmortem" as "retrospective".** His preface calls the ritual "called by many
  names - postmortem or postpartum, for example, or, my preference, retrospective" [14]. That is a
  preference among names already in circulation, not a coinage and not an argued replacement. The widespread
  story that he deliberately replaced the term, with a stated rationale, could not be verified in his own
  words anywhere in this research.
- **But his book draws this family's distinction structurally, which is better.** Chapter 7 is titled
  "Leading a Postmortem" and contains a section titled "Some Important Differences Between Retrospectives
  and Postmortems" at page 186 [14]. Kerth reserves "postmortem" for reviewing *failed projects*, distinct
  from the general-purpose retrospective. This was read from the book's own table of contents, and it is a
  stronger anchor for the family's contrast than the contract's own framing.

**The Prime Directive's exact wording is not stable** across the sources that reproduce it [15][17][18][20],
differing on "must understand" versus "understand" and on gendered versus neutral pronouns. Chapter 1, where
it lives, was outside the accessible sample. The bundle quotes the commonly circulated wording and says it
is the circulated wording. It is also **criticised by name**, twice and independently: Philippe Kruchten
calls it "pretty naive to me, in terms of the reality of human nature" [15], and a 2015 practitioner piece
finds it "fairly empty" and lacking authenticity [16].

## The family's own claim, tested and not confirmed

The `process-docs` contract states that the common real-world error is running a retro on an incident, which
"produces a blameless discussion of a thing that needed a causal analysis", or running a postmortem on a
sprint, which "pathologises ordinary work". **No source read in full states this.** Sources do draw the
retro/postmortem line by purpose and timing [28][29], but none frames confusing them as a named failure
mode. The bundle presents the claim as this library's own reasoning.

**And named organisations do the opposite.** Honeycomb calls its incident process an "incident
retrospective", uses "retrospective" and "incident review" interchangeably, never uses "postmortem", and
declines even "blameless" in favour of "blame-aware" [31]. FireHydrant, an incident-management vendor,
titles its material "Blameless Retrospectives" and splits *retrospective* into an incident-triggered type
and a post-project type [32]. These are current, named counterexamples to the family's assumed vocabulary
split, and the bundle carries them rather than filtering them out.

## Size verdict, and why the spec survives this time

**One size, `[lean]`, as specified.** This is the first build spec in five bundles that the research
confirms rather than corrects, and it is confirmed on evidence rather than by default. No source publishes
two weights of a *sprint* retrospective notes document [2][3][4]. The genuine counter-argument was tested:
Derby and Larsen scope their activities to "an iteration, release, or project retrospective", vary timing
with "the length of the increment of work", give release and project retrospectives their own chapter, and
InfoQ records that extending beyond Kerth's end-of-project cadence was the book's explicit aim
[7][9][10][11]. That is real variation, but it is variation across **occasions**, not weights of one
document, and a source in the same corpus distinguishes sprint from release retrospectives as different
things rather than sizes of one [30]. The evidence that would have earned a second weight instead argues for
a richer single template, which is what the Hundhausen finding [21] independently recommends.

## Format verdict (ADR 0028)

**One format.** Start/Stop/Continue, Mad/Sad/Glad, 4Ls, Starfish and Sailboat circulate widely [3][12][13]
but they are **facilitation activities**, not document shapes, and none is published by a named source *as a
notes template*. Smartsheet repackages several as fillable documents [3], which is a vendor's packaging
decision rather than a format in circulation with a named source, and admitting it would repeat the mistake
ADR 0028 exists to prevent.

## Sources

### Does the artifact exist: document, board, or activity catalog

**[1] Scrum Guides (Ken Schwaber, Jeff Sutherland), The Scrum Guide.** primary. **fetched-and-verified.**
`https://scrumguides.org/scrum-guide.html`
Supports: The Scrum Guide defines the Sprint Retrospective as an event/discussion, not a document; no notes template or written artifact is named as its output Establishes that the official Scrum canon uses 'what went well' verbatim but does not use the fixed 'what to improve' / 'action items' phrasing found in folk templates - evidence against a clean canonical origin for the three-column WWW/WTI/AI format. Full-text of the Sprint Retrospective section (purpose, timebox, discussion content, output) and the literal string counts for the required search terms across the entire 2020 Guide
Quotable: "The purpose of the Sprint Retrospective is to plan ways to increase quality and effectiveness."
Quotable: "inspects how the last Sprint went with regards to individuals, interactions, processes, tools, and their Definition of Done"
Quotable: "discuss what went well during the Sprint, what problems it encountered, and how those problems were (or were not) solved"
Quotable: "The Scrum Team identifies the most helpful changes to improve its effectiveness. The most impactful improvements are addressed as soon as possible. They may even be added to the Sprint Backlog for the next Sprint."
Quotable: "The Scrum Team discusses what went well during the Sprint, what problems it encountered, and how those problems were (or were not) solved."
Quotable: "to a maximum of three hours for a one-month Sprint"
Quotable: "what went well during the Sprint, what problems it encountered"
Quotable: "identifies the most helpful changes to improve its effectiveness"
Quotable: "They may even be added to the Sprint Backlog for the next Sprint."
Quotable: "timeboxed to a maximum of three hours for a one-month Sprint"

**[2] Documentero, "Retrospective Meeting Notes - Document Template".** vendor. **fetched-and-verified.**
`https://documentero.com/templates/project-management/document/retrospective-meeting-notes/`
Supports: A named source that publishes an actual downloadable document (not a board) with fixed section headings for retrospective notes
Quotable: "Meeting Information"
Quotable: "What Went Well"
Quotable: "What Didn't Go Well"
Quotable: "Ideas for Improvement"
Quotable: "Action Items"
Quotable: "Additional Notes"

**[3] Smartsheet, "Agile Retrospective Templates" (agile-sprint-scrum-retrospective-templates).** vendor. **fetched-and-verified.**
`https://www.smartsheet.com/content/agile-sprint-scrum-retrospective-templates`
Supports: A named vendor publishing multiple genuinely downloadable document templates (Word/Excel/PDF/PowerPoint, not board-only) for retrospective note-taking, with explicit section headings per template
Quotable: "What Went Well?"
Quotable: "What Went Poorly?"
Quotable: "What New Ideas Do We Have?"
Quotable: "What Actions Will We Take?"
Quotable: "Start"
Quotable: "Stop"
Quotable: "Continue"
Quotable: "Liked"
Quotable: "Learned"
Quotable: "Longed For"
Quotable: "Lacked"

**[4] Atlassian, Confluence "Retrospective Blueprint" documentation.** vendor. **fetched-and-verified.**
`https://confluence.atlassian.com/doc/retrospective-blueprint-427623496.html`
Supports: Confluence ships a page-template (document, not whiteboard) blueprint for retrospectives that persists as written record, distinct from Atlassian's whiteboard-based retro tooling
Quotable: "what went well, what needed improvement, and assign actions for the future"

**[5] Corinna Baldauf and Timon Fiddike, Retromat.** practitioner. **url-confirmed-not-read.**
`https://retromat.org/en/`
Supports: Retromat is confirmed (via search-result synthesis, not full body read) to be a random activity-plan generator across five phases, not a notes document; existence only, no quotable body text

**[6] FunRetrospectives.com, activity category listing.** practitioner. **url-confirmed-not-read.**
`https://www.funretrospectives.com/category/retrospective/`
Supports: Fun Retrospectives is confirmed (via search-result synthesis, not full body read) to be a catalog of named facilitation activities (FLAT, WWW, 3Ls, etc.), not a notes document; existence only, no quotable body text

### Where the structure actually comes from

**[7] Esther Derby and Diana Larsen, Agile Retrospectives: Making Good Teams Great (official publisher excerpt, Pragmatic Bookshelf).** primary. **fetched-and-verified.**
`https://media.pragprog.com/titles/dlret/Activities.pdf`
Supports: Direct primary-text evidence: activity descriptions from chapters 5 (Gather Data) and 6 (Generate Insights) confirming the phase structure and confirming activities scale by iteration/release/project rather than one fixed size.
Quotable: "Use this to gather data in a longer iteration, release, or project retrospective."
Quotable: "Time Needed: Thirty to ninety minutes, depending on the size of the group and the length of the increment of work."
Quotable: "(For a release or project, prep the timeline with a few time markers such as project milestones, months, or seasons.)"
Quotable: "When you have only an hour or so for the entire retrospective session, choose a timeline variation that will help to display just enough data. Include both facts and feelings, for sure, but no more than one kind of each. Consult the retrospective goal as a guide for what's most important this time. Keep it simple."
Quotable: "Use this to gather data or as part of the Decide What to Do phase in an iteration, release, or project retrospective."
Quotable: "Use this in conjunction with an activity that suggests possible changes while generating insights for a release or project retrospective. Use this as part of a planning exercise while deciding what to do."
Quotable: "Use this activity to generate insights in a longer iteration, release, or project retrospective."
Quotable: "Use the results in the next phase, Decide What to Do."

**[8] Johanna Rothman, review of Agile Retrospectives: Making Good Teams Great.** practitioner. **fetched-and-verified.**
`https://www.jrothman.com/mpd/2006/08/agile-retrospectives-making-good-teams-great/`
Supports: Independent confirmation of the book's exact five-phase list, quoted directly from the book by a named reviewer (a peer of the authors), plus confirmation of the activities/timeboxing structure.
Quotable: "Set the Stage"
Quotable: "Gather Data"
Quotable: "Generate Insights"
Quotable: "Decide What to do"
Quotable: "Close the Retrospective"
Quotable: "30 activities with instructions on how to use those activities (and which stage(s) in which to use them)"
Quotable: "Esther and Diana explain how to timebox a retrospective so the team uses the time most effectively."

**[9] Goodreads, book page for Agile Retrospectives: Making Good Teams Great.** standards. **fetched-and-verified.**
`https://www.goodreads.com/book/show/721338.Agile_Retrospectives`
Supports: Full chapter-level table of contents, confirming chapter titles including 'A retrospective custom-fit for your team' (ch.2) and a separate 'Releases and project retrospectives' chapter (ch.9), distinct from the core iteration-level activity chapters 4-8.
Quotable: "See how to mine the experience of your software development team continually throughout the life of the project."
Quotable: "A retrospective custom-fit for your team"
Quotable: "Releases and project retrospectives"

**[10] Agile Alliance, book resource page for Agile Retrospectives.** standards. **fetched-and-verified.**
`https://agilealliance.org/resources/books/agile-retrospectives-making-good-teams-great/`
Supports: Corroborates the book's explicit custom-fit, scalable-by-team framing rather than a single fixed structure.
Quotable: "how to architect retrospectives in general, how to design them specifically for your team and organization, how to run them effectively, how to make the needed changes, and how to scale these techniques up"

**[11] InfoQ, news article on the Agile Retrospectives book launch.** standards. **fetched-and-verified.**
`https://www.infoq.com/news/New-Agile-Retrospectives-Book`
Supports: Confirms the book's explicit departure from Kerth's end-of-project-only cadence, extending retrospectives to multiple cadences (release, milestone, regular interval) - direct evidence against a single fixed size.
Quotable: "you don't have to wait until the end of a project to do a retrospective. Even if you aren't on an Agile team, you can hold retrospectives at releases, milestones, or at regular intervals to improve the way the team is working."

**[12] Retrium, 'Start Stop Continue' technique page.** vendor. **fetched-and-verified.**
`https://www.retrium.com/retrospective-techniques/start-stop-continue`
Supports: Confirms the format's origin is untraceable even to a retrospective-industry vendor that catalogs the technique.

**[13] Retrium, 'Mad Sad Glad' technique page.** vendor. **fetched-and-verified.**
`https://www.retrium.com/retrospective-techniques/mad-sad-glad`
Supports: Confirms the format is presented only as 'a classic exercise' with no attributed source, even by a vendor whose business is cataloging retrospective techniques.
Quotable: "a classic exercise"

### Kerth, the Prime Directive, and the naming history

**[14] Norman L. Kerth - Project Retrospectives: A Handbook for Team Reviews (Dorset House, 2001) - official Pearson/InformIT free sample chapter PDF.** primary. **fetched-and-verified.**
`https://ptgmedia.pearsoncmg.com/images/9780133488579/samplepages/0133488578.pdf`
Supports: Primary-text confirmation of book structure, page numbers for the Prime Directive and naming sections, and Kerth's own preface framing of 'retrospective' as his personal preference among existing names, not a claimed invention.
Quotable: "this ritual, called by many names - postmortem or postpartum, for example, or, my preference, retrospective - is important to our practice of software. In fact, I believe that it is the single most important step toward improving the software process!"
Quotable: "If a project fails, holding a retrospective provides a way for project members to learn from the failure and move beyond it. Its structure helps team members discuss how to improve, without eliciting accusations of blame or implications of shame."

**[15] InfoQ - "Questioning the Retrospective Prime Directive" (reported discussion including Philippe Kruchten, Esther Derby, Norm Kerth, Mary Poppendieck, Linda Rising), 2008.** practitioner. **fetched-and-verified.**
`https://www.infoq.com/articles/retrospective-prime-directive/`
Supports: The Prime Directive's origin story in Kerth's own words (sailboat racing tragedy, not Star Trek framing), his own account of why he had to write it down, Kruchten's named critique and proposed reword, Derby's counter-framing, and the documented relationship to older 'post-project reviews or postmortems'.
Quotable: "The Prime Directive was developed late in my retrospective facilitator's career. It wasn't until I started to teach how to lead retrospectives that I found it necessary to scribe the Prime Directive."
Quotable: "During one heavy-weather race a friend of mine capsized and drowned. Top sailors, for whom I had a great deal of respect, led a fearless review of every aspect of the race, of every person's actions, and of every decision made, for no other reason than to help the entire sailing community learn how to prevent another death."
Quotable: "As I developed my course, I realized I couldn't say: 'there will be no fault-finding, no judging, etc.' because by saying it, I'd bring those concepts into focus."
Quotable: "Regardless of what we discover, we understand and truly believe that everyone did the best job he or she could, given what was known at the time, his or her skills and abilities, the resources available, and the situation at hand."
Quotable: "Really? I have met subversive, obnoxious, really destructive people during my career as a developer and consultant."
Quotable: "The Prime Directive sounds pretty naive to me, in terms of the reality of human nature."
Quotable: "I am willing to get started with people with giving them full credit, but they have to prove their worth."
Quotable: "I try to stand in this space as a matter of my personal values. It's not always easy...It is much easier to influence someone if you haven't written them off, and it's virtually impossible to learn from someone you've written off as stupid."
Quotable: "Other similar processes are post-project reviews or postmortems (why don't I like that word?) where teams examine what happened over the duration of an activity."

**[16] The Scrum Academy - "The Retrospective Prime Directive Is Kinda Silly" (2015 practitioner opinion piece).** practitioner. **fetched-and-verified.**
`https://thescrumacademy.com/2015/04/07/the-retrospective-prime-directive-is-kinda-silly/`
Supports: A second, independent named criticism of the Prime Directive, distinct from the Kruchten/Derby exchange, arguing it lacks authenticity and oversimplifies human motivation.
Quotable: "I am not a huge fan of the Retrospective Prime Directive since I find it to be fairly empty and lacks authenticity."

**[17] Agile Retrospective Resource Wiki - "The Prime Directive" (community-maintained reference page).** practitioner. **fetched-and-verified.**
`https://retrospectivewiki.org/index.php?title=The_Prime_Directive`
Supports: A second-hand rendering of the Prime Directive text and its attribution to Kerth's book, useful as corroboration but explicitly carrying no page or chapter citation.
Quotable: "Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand."

**[18] Google Books - "Project Retrospectives: A Handbook for Team Reviews" about-the-book page (publisher/Google-supplied synopsis).** vendor. **fetched-and-verified.**
`https://books.google.com/books/about/Project_Retrospectives.html?id=3VUUAAAAQBAJ`
Supports: A publisher-synopsis-level rendering of the Prime Directive text that varies in wording ('must understand' vs. 'understand') from the commonly circulated version, evidence that the exact wording is not stable across secondary sources.
Quotable: "Regardless of what we discover, we must understand and truly believe that everyone did the best job he or she could, given what was known at the time, his or her skills and abilities, the resources available, and the situation at hand."
Quotable: "Whether your shop calls them postmortems or postpartums or something else, project retrospectives offer organizations a formal method for preserving the valuable lessons learned"

**[19] Goodreads - "Project Retrospectives: A Handbook for Team Reviews" book page, reviewer Toni Tassani's summary.** vendor. **fetched-and-verified.**
`https://www.goodreads.com/book/show/1523368.Project_Retrospectives`
Supports: The specific claim that facilitators Wayne and Eileen Strider suggested the word 'retrospective' to Kerth - sourced here only to a reader's summary of the book, not to text I could read directly in the primary source.
Quotable: "Wayne and Eileen Strider, two fellow facilitators, suggested that we call what we do a retrospective. The word seemed appropriate; it didn't carry any loaded meanings and it could be applied to projects without implication of success or failure."

**[20] FunRetrospectives - "The Retrospective Prime Directive" (practitioner blog).** practitioner. **fetched-and-verified.**
`https://www.funretrospectives.com/the-retrospective-prime-directive/`
Supports: Independent corroboration of the commonly circulated Prime Directive wording and its attribution to Kerth, again without page or chapter citation.
Quotable: "Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand."

### Evidence, and what actually goes wrong

**[21] Christopher Hundhausen, Phillip Conrad, Ahsun Tariq, Surya Pugal, Bryan Zamora Flores - "An Empirical Study of the Content and Quality of Sprint Retrospectives in Undergraduate Team Software Projects" (ICSE-SEET '24).** primary. **fetched-and-verified.**
`https://dl.acm.org/doi/10.1145/3639474.3640074`
Supports: The largest-scale empirical study of retro CONTENT AND QUALITY to date (963 statements, 32 teams, n=182 students, 4 courses at 2 North American universities, 2021-2022). It measures what teams reflect on and how deeply, not whether retros change outcomes. Central finding: 84.1% of retro statements were mere 'Strategy' (a stop/start/continue claim with no justification); only 13% were 'Justified Strategy' (gave a reason); only 0.1% (one statement) reached 'Critiqued Strategy' (weighed a pro and a con); zero statements reached the deepest level ('Discussed Strategy', comparing alternatives). 95% of statements clustered in three concern categories: Work Practices (50%), Communication Practices (27%), Collaboration Practices (18%).
Quotable: "Our study analyzed a corpus of 963 statements documented in the retros of 32 undergraduate software teams (n = 182 students) enrolled in four software engineering courses at two North American universities."
Quotable: "An analysis of the quality of teams' retro reflections showed that only 13% provided justification for a strategy to be stopped, continued, or started."
Quotable: "The dominant level of reflection exhibited in retro statements was Strategy (84.1%), which simply stated a practice to start, stop, or continue, without providing any justification."
Quotable: "Only one statement (0.1%) exhibited a higher form of reflection (Critiqued Strategy) by identifying at least one pro and one con. ... no retro statements considered the pros and cons of alternative strategies (Discussed Strategy)."
Quotable: "As the figure illustrates, 95% of all retro statements focused on three concerns: Work Practices (50%), Communication Practices (27%), and Collaboration Practices (18%)."

**[22] Adam Przybyłek and co-researchers - "Game-based Sprint retrospectives: multiple action research" (Empirical Software Engineering, 2021).** primary. **fetched-and-verified.**
`https://pmc.ncbi.nlm.nih.gov/articles/PMC8527976/`
Supports: An action-research study across 6 Scrum teams (two teams each at 3 companies: OKE Poland, Dynatrace, SentiOne) that had experienced 'common retrospective problems.' It measured PERCEPTIONS of retrospective games via a 7-item Likert questionnaire and focus groups (6 predefined questions), not objective performance/productivity/defect outcomes. Feedback indicated the games helped teams mitigate 'accidental difficulties' of the Sprint Retrospective such as lack of structure, dullness, too many complaints, and unequal participation, and made meetings feel more productive to some degree, but different participants perceived different games' benefits (communication, motivation-and-involvement, creativity) differently.
Quotable: "we adopted the joint replication approach"
Quotable: "Two Scrum teams from each company participated in the project"
Quotable: "During the diagnosing phase, the data originated from interviewing. Then, during the action-taking phase...researchers wrote field notes on observations."
Quotable: "While questionnaire results revealed team members' perceptions of retrospective games, focus group discussions allowed in-depth exploration of the reasons why the participants thought the way they did."

**[23] Alessandra Maciel Paz Milani, Margaret-Anne Storey, Vivek Katial, Lauren Peate - "Exploring Retrospective Meeting Practices and the Use of Data in Agile Teams" (CHASE 2025, IEEE/ACM).** primary. **fetched-and-verified.**
`https://arxiv.org/html/2502.03570v1`
Supports: A 19-team survey (recruited from ~100 teams using the Multitudes engineering-insights platform, 19% response rate, March-April 2024; 14 mixed-format questions, thematic coding into 12 themes) measuring how teams RUN retros and whether they use project data in them; it does not measure whether retros improve team or product outcomes. Directly supports two failure modes: retros perceived as low-value/poorly executed ('poor and...a waste of time'), and defensiveness/psychological-safety strain during critique. Also documents a collect-but-don't-use data gap: most teams collect project data but don't systematically bring it into the retro.
Quotable: "Although teams routinely collect project data, they seldom employ it systematically"
Quotable: "We've been doing retros for years but really haven't done a great job of integrating metrics into our processes"
Quotable: "Retros are important; however...the team's execution of retros right now is poor and...a waste of time"
Quotable: "This can sometimes lead to what feels like a need for the team to 'defend' or 'explain' behaviour"
Quotable: "Our retrospectives are mostly based on what people felt went right or wrong...It isn't very metric-centric"

**[24] Maria Spichkova, Hina Lee, Kevin Iwan, Madeleine Zwart, Yuwon Yoon, Xiaohan Qin (RMIT University & Shine Solutions) - "Agile Retrospectives: What went well? What didn't go well? What should we do?" (arXiv preprint, 2025).** primary. **fetched-and-verified.**
`https://arxiv.org/html/2504.11780v1`
Supports: Primarily an LLM-categorization-accuracy study (ChatGPT-4 Turbo classifying 200 hand-labeled retro comments into went-well/did-not-go-well/neutral/irrelevant, 41-74% accuracy across three prompts) -- NOT a study of retrospective outcomes. It is cited here only for one embedded finding it quotes from a separate industrial case study it references, on a failure mode: trust dropping after a retrospective. This is a claim this paper cites from elsewhere, not one it originated; flagged as such rather than treated as this paper's own primary finding.
Quotable: "the only negative change was the level of trust in the relationship between team members dropped after the retrospective"

**[25] Scott I. Tannenbaum and Christopher P. Cerasoli - "Do Team and Individual Debriefs Enhance Performance? A Meta-Analysis" (Human Factors, 2013).** primary. **fetched-and-verified.**
`https://cdn.ymaws.com/www.odnetwork.org/resource/resmgr/2013_education/tannenbaum_using_debriefs_ha.pdf`
Supports: TRACES the widely circulating '25% performance improvement' statistic. This is a meta-analysis of 46 studies of DEBRIEFS / after-action reviews broadly (military, aviation, medical, and business/corporate teams per multiple secondary summaries) -- it is NOT a study of Agile sprint retrospectives, and the source itself contains no statement equating debriefs with sprint retrospectives. The 25% figure appears in the source, confirmed by direct fetch, but the underlying construct-substitution (debrief-in-general standing in for Scrum retrospective-specifically) is exactly the kind of overstatement this dimension was asked to catch.
Quotable: "a 25% improvement in performance"

**[26] Stefan Wolpers - "21 Sprint Retrospective Anti-Patterns" (age-of-product.com, cross-posted scrum.org).** practitioner. **fetched-and-verified.**
`https://age-of-product.com/sprint-retrospective-anti-patterns/`
Supports: Named, source-backed failure modes for the failure-modes half: recurring unaddressed action items ('What improvement?'), no owner on action items ('#NoAccountability'), retro cancellation under time pressure ('Dispensable buffer'), blame despite the prime directive ('No psychological safety'), and discussion with no follow-through ('Extensive whining').
Quotable: "The team does not check the status of the action items from previous Retrospectives."
Quotable: "At the last Retrospective, the team members accepted action items. However, no one took responsibility for the delivery."
Quotable: "The Scrum team cancels Retrospectives if more time is needed to accomplish the Sprint Goal."
Quotable: "The Retrospective is an endless cycle of blame and finger-pointing."
Quotable: "The Scrum team uses the Retrospective primarily to complain about the situation and assumes the victim's role...not moving on once you have identified critical issues and trying to change them defies the purpose."

**[27] Mike Cohn - "Sprint Retrospectives: Solutions to 4 Common Problems" (Mountain Goat Software blog).** practitioner. **fetched-and-verified.**
`https://www.mountaingoatsoftware.com/blog/overcoming-four-common-problems-with-retrospectives`
Supports: Independently corroborates the discussion-with-no-change failure mode via a time-payback framing, and names two additional named failure modes not in the brief's candidate list: dishonesty in retros, and monotony from an unvarying format.
Quotable: "people fail to bring up real issues or admit to their problems"
Quotable: "Whatever improvement they identify needs to be able to pay back 480 minutes of savings for that retrospective to have been worth the effort."
Quotable: "Retrospectives can quickly feel worthless if people commitment to changes they don't deliver on."

### The boundary against the incident postmortem

**[28] Parabol (unsigned company blog) - "Post-mortems vs Retrospectives: What's the Difference".** vendor. **fetched-and-verified.**
`https://www.parabol.co/blog/retrospectives-vs-post-mortems/`
Supports: Q1: a named source that explicitly distinguishes the two by purpose and timing. Q3: names 'project retrospectives' as a recognized adjacent category, with a linked guide covering pre-mortems, post-mortems, lessons-learned meetings, and after-action reviews.
Quotable: "Post-mortems attempt to understand what went wrong"
Quotable: "typically take place after something is completed, and attempt to understand why it turned out the way it did"
Quotable: "As the name implies, typically, post-mortems happen after something - a big milestone, a project, or an incident like an outage, hack or other failure"
Quotable: "Retrospectives are a standard part of the agile development cycle, often coming at the end of each sprint, or approximately every 2 weeks"
Quotable: "Because the name implies understanding what went wrong, post-mortems sometimes only happen when that 'something' is negative, which means there's not as much reflection when things go well"

**[29] Jonathan Hall - "Retrospectives or Postmortems?" (jhall.io, also mirrored on DEV Community).** practitioner. **fetched-and-verified.**
`https://jhall.io/archive/2021/07/31/retrospectives-or-postmortems/`
Supports: Q1: a named individual practitioner source distinguishing the two by purpose. Q2 (negative finding): this source frames the two as complementary, not as a common-error pairing - it recommends postmortems as an easier entry point for teams resistant to retrospectives, which cuts against any claim that conflating them is a well-known failure mode.
Quotable: "Retrospectives exist to encourage regular retrospection, whereas postmortems serve to understand root causes of incidents and prevent future reoccurences."

**[30] TeamRetro (unsigned company blog) - "Sprint retrospective vs. release retrospective".** vendor. **fetched-and-verified.**
`https://www.teamretro.com/blog/sprint-retrospective-vs-release-retrospective/`
Supports: Q3: a named source distinguishing sprint-level from release-level retrospectives on scope and strategic vs. tactical framing. Does not connect this to incident postmortems at all, so it does not itself place a release retrospective 'between' sprint retro and postmortem - that positioning is not made by any source found.
Quotable: "Sprint retrospectives are tactical. They emphasize short-term process improvements, collaboration, and delivery within a sprint cycle."
Quotable: "Release retrospectives are strategic. They look at the broader picture, including the product's success, alignment with business goals, and long-term process improvements."
Quotable: "Scope: Sprint Retrospective focuses on a single sprint (1-4 weeks); Release Retrospective focuses on the entire release cycle (multiple sprints)."

**[31] Honeycomb (company engineering blog) - "The Incident Retrospective Best Practices" (ground rules post).** practitioner. **fetched-and-verified.**
`https://www.honeycomb.io/blog/incident-retrospective-ground-rules`
Supports: Q4: an SRE-adjacent named source that calls its incident-side process an 'incident retrospective' and explicitly declines the word 'blameless' in favor of 'blame-aware,' defending a stance close to blameless discussion applied to an incident, deliberately. It uses 'retrospective,' 'incident retrospective,' and 'incident review' interchangeably and never uses 'postmortem,' which undercuts a clean naming split between the two communities rather than supporting one.
Quotable: "It's worth noting that we don't say 'blameless' directly. Instead, we use 'blame-aware.'"
Quotable: "everyone is assuming they made the best choice they could at the time based on the information they had"

**[32] FireHydrant (company blog) - "What are Blameless Retrospectives? How Do You Run Them?".** vendor. **fetched-and-verified.**
`https://firehydrant.com/blog/what-are-blameless-retrospectives-do-they-work-how/`
Supports: Q4: a named incident-management vendor uses 'retrospective' as its own term for the incident-side review (title: 'blameless retrospectives'), and its body explicitly splits 'retrospective' into an incident-triggered type and a post-project type, treating the word as covering both. This is a live, named counterexample to any clean split where 'retrospective' means sprint-cadence and 'postmortem'/'review' means incident.
Quotable: "Retrospectives usually fall into two categories. The first type of retrospective meeting is held after a DevOps or IT incident such as data corruption or website crash. The second type of retrospective takes place after project completion where the team looks at the project from the start to the end to determine what went smoothly and what can be improved."

### The Scrum Guide, by full text

**[33] Scrum.org / scrumguides.org editorial team, "Changes between 2017 and 2020 Scrum Guides" (revision-history page), scrumguides.org.** primary. **fetched-and-verified.**
`https://scrumguides.org/revisions.html`
Supports: What changed about the Sprint Retrospective / retrospective-derived Sprint Backlog language between the 2017 and 2020 editions, since the standalone 2017 Guide page returned 404
Quotable: "soften language around retro items in Sprint Backlog"
Quotable: "it includes at least one high priority way in which the team works, identified in the previous Retrospective meeting"

## Contested register

1. **The Prime Directive's exact wording, which splits three ways rather than two.** The circulated
   version says "we understand and truly believe" with neutral pronouns [17][20]; the InfoQ account keeps
   "we understand" but carries gendered pronouns [15]; only the publisher blurb reads "we must understand"
   [18]. An earlier draft of this log paired [15] with [18] and was corrected by the review. Chapter 1 of the book was not in the accessible sample [14], so which is the page text
   is unresolved. The bundle quotes one and says it is the circulated one.
2. **Whether Kerth was given the word "retrospective" by Wayne and Eileen Strider.** This appears only in a
   reader's summary of the book [19]. Kerth's acknowledgements do thank both people [14], which is
   consistent, but the naming story itself could not be verified against his own text.
3. **Whether the Prime Directive is sound.** Kruchten challenges it directly and proposes softening "truly
   believe" to "assume"; Esther Derby answers pragmatically rather than rebutting, arguing it is
   "virtually impossible to learn from someone you've written off as stupid" [15]. A separate practitioner
   piece rejects it outright [16].
4. **Whether "retrospective" and "postmortem" name distinct practices at all.** Agile-side sources draw a
   clean line [28][29][30]; incident-response-side sources use "retrospective" for the incident review
   [31][32]. Neither camp is wrong. They are using one word for different referents, which is itself the
   most useful thing this bundle can tell a reader.
5. **Whether a vendor's downloadable Word template counts as precedent for a document type** [2][3], or is
   a board's column structure repackaged as a file. Recorded because the bundle's admission under ADR 0030
   rests on these sources.
6. **Whether the trust finding is usable.** A 2025 paper reports, citing a separate industrial case study it
   does not name, that "the only negative change was the level of trust in the relationship between team
   members dropped after the retrospective" [24]. This is a second-hand citation inside a fetched paper. It
   is recorded, and the bundle treats it as weaker than the Wolpers and Cohn material [26][27].

## Sought and not found

- **Any study measuring retrospectives against team or product outcomes.** Searched arXiv, Semantic Scholar,
  Google Scholar and the general web. The three software-specific studies found measure content quality
  [21], participant perception [22], and practice [23]. None measures velocity, defect rate, predictability
  or any downstream outcome, and none isolates the retrospective from the rest of the agile bundle.
- **An originating publication for "What Went Well / What To Improve / Action Items".** None found.
- **An origin for Start/Stop/Continue or Mad/Sad/Glad.** None found, including at the vendors who catalog
  them [12][13]. One search summary asserted a 1970s origin for Start/Stop/Continue; no source
  substantiating that date could be located or read, so it is not carried.
- **Kerth's chapter 1**, where the Prime Directive and the naming discussion live [14]. The accessible
  sample began at chapter 3. Kerth's own site did not resolve, and the archive could not be fetched.
- **Esther Derby's own elaborations** on the Kruchten exchange. HTTP 403 on two attempts.
- **Amy Edmondson's 1999 paper.** HTTP 403. It is therefore quoted nowhere in this bundle, and where
  psychological safety is discussed the bundle says the research is adjacent rather than about
  retrospectives.
- **The standalone 2017 Scrum Guide.** Returned 404. The 2017-to-2020 change is sourced from
  scrumguides.org's own revision-history page instead [33], which quotes the superseded language directly.

## Notes for the companion

**The honest core.** Scrum defines the event and not the document, counts zero occurrences of "action item"
[1], and in 2020 downgraded the one requirement that retrospective output reach the next Sprint [33][1]. The
notes exist because a discussion that commits nobody to anything is the practice's documented failure mode
[26][27], and because the largest study of retrospective content found reflection is overwhelmingly
unjustified assertion [21]. The document's job is to make one improvement owned, dated and findable.

**The sections, one size, in this order:** Sprint and Participants; Previous Actions; What Went Well; What
To Improve; Action Items.

Three are attested as document headings, one is attested in a different form, and one is this bundle's own
contribution, which the guidance comments must say plainly rather than implying a source prescribes it.

- **Sprint and Participants** renders Documentero's "Meeting Information" [2] for a sprint context.
- **What Went Well** [1][2][3] is the one phrase the Scrum Guide itself supplies [1].
- **What To Improve** carries Documentero's "What Didn't Go Well" and "Ideas for Improvement" [2] and
  Smartsheet's "What Went Poorly?" and "What New Ideas Do We Have?" [3] under one heading.
- **Action Items** [2], Smartsheet's "What Actions Will We Take?" [3]. Every row needs an owner and a date,
  because unowned actions are a failure mode two independent sources name [26][27]. Nothing read ranks the
  failure modes against one another, so neither this log nor the bundle ranks them.
- **Previous Actions is this bundle's own contribution.** No published template carries it [2][3][4]. It
  exists because Wolpers names "the team does not check the status of the action items from previous
  Retrospectives" as a distinct anti-pattern [26], and because Scrum removed the obligation that carried
  them forward [33][1]. It is labelled as the bundle's answer to a documented failure mode, not as practice.

**The template must prompt for a reason, not only an observation.** Hundhausen et al. found 84.1 percent of
retrospective statements were bare assertions with no justification [21]. A notes template whose columns
only ask *what* reproduces exactly the shallowness that study measured, so the guidance for What Went Well
and What To Improve asks the author to say why, and the rubric grades it.

**The sharpest teaching points.** The 2017-to-2020 softening [33]. The zero counts [1]. The untraceable
provenance of every format everyone uses [12][13]. Kerth's chapter 7 as the real anchor for the
retro-versus-postmortem line [14]. And the counterexamples [31][32], which stop the bundle from teaching a
vocabulary rule the industry does not follow.

**What the example must not do.** It must not be about the incident. Sprint 24 contains DEF-2291 and the
temptation is real, but the two members of this family exist to be contrasted, and the example earns the
distinction by naming the postmortem and saying why the incident is out of scope, not by ignoring it.
