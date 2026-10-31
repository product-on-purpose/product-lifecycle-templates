# lean-ux-canvas: research log

Research conducted 2026-10-30. The research stage stored its pages from 23:02 UTC on 2026-10-30, which is
2026-10-30 by local time. The research builds on admission sweep 7 of 2026-10-29, whose digest sits in a
gitignored folder under `_local/research/`, and on the placement research of 2026-10-30, which read and
raw-checked Gothelf's pages and the Atomic Object post. It builds on
[ADR 0082](../../docs/internal/decisions/0082-lean-ux-canvas-joins-discovery-docs-at-discover.md) (the Lean UX
Canvas joins discovery-docs at discover), on the family contract (`docs/internal/contracts/discovery-docs.md`,
0.6.0) and on the approved spec, the section of `docs/internal/tier2-specs.md` headed "discovery-docs (sixth
member, at `discover`): the Lean UX Canvas". The maintainer ruled all seven of that spec's choices as
recommended on 2026-10-30. They fix the id `lean-ux-canvas`, the title Lean UX Canvas with the alias Lean
Product Canvas, the 2019 box headings with the 2024 wording where it differs, one size, the ninth section, the
example and the build order. This bundle is issue #330 (bundle: lean-ux-canvas), and it adds catalog entry 211.

The build ran six dimensions: origins, structure, practice, debates, relationships and the gap question. The
working files are numbered by return order, not by dimension: `dim1.md` holds origins, `dim2.md` practice,
`dim3.md` the gap question, `dim4.md` debates, `dim5.md` structure and `dim6.md` relationships.

**19 sources are recorded below, and all 19 are fetched-and-verified.** By tier they are 11 primary, 7
practitioner and 1 vendor. Ten of the eleven primary entries are the originators' own: Gothelf's blog posts
[1], [2], [4], [6], [7], [10], [11] and [16], the 2024 canvas PDF [5], and the third edition of the Lean UX
book [19]. The eleventh is Ash Maurya's own page on his Lean Canvas [15]. Entry [19] is a copyrighted book read
from a text copy of chapters 3 to 13 that the maintainer supplied from their own copy; its text is never
committed, and it carries no URL for that reason. **168 Quotable lines remain: 139 from the 18 web entries and
29 from the book.** Quotable lines render long dashes as hyphens and keep curly apostrophes; copy them as they
stand.

## What the checks caught, and what was not read

**Every quotation was checked against raw text**, never against a retrieval tool's summary. The automated
recheck read 122 quotations across the web sources: 110 passed strictly, 3 passed as extraction artifacts and
9 failed. The generator then kept only quotations that pass against the cached page, and split three list-shaped
lines into their passing parts. It dropped three that failed outright: one bracketed paraphrase of the
Hypothesis Prioritization Canvas page [6], and two paraphrases of Gothelf's walkthrough [7]. Entry [7] was left
with no quotation at all, so the main loop added eight lines from it that the placement research had already
raw-checked, or that a grep of the cached page found. It added sixteen more to [2], [4] and [8] the same way,
among them seven of the 2019 box headings of [4]. All 29 book quotations pass against the maintainer's copy.

**The spec misquoted Gothelf's walkthrough, and this build corrects it.** The spec says the book is "structured
around" the canvas, as the walkthrough says. The walkthrough says the third edition is organized around the
canvas, and that "The backbone of the book is the Lean UX Canvas." [7]. Its phrase "structured around" describes a
self-paced video class [7]. The meaning stands; the wording does not.

**One agent attributed a phrase to the wrong source.** The practice dimension wrote that the book calls the
canvas a living document. The book uses that phrase for proto-personas, not for the canvas. Atomic Object's
post is the source that calls the canvas one [8]. No claim here rests on the misattribution.

**IdeaScale's page was read in error and withdrawn.** The gap-question agent read a vendor page on
ideascale.com before checking the site's terms, which forbid automated access. The main loop found the clause
after the research stage, removed the entry and lists it in the section on pages not read under the terms rule,
at the end of this log. The gap findings below rest on [13] and [18] alone.

**The terms of every newly read host were checked in the main loop.** InfoQ, Modern Analyst, UX Podcast,
Creately, Jeff Patton's site and SVPG carry no bar on reading; Patton's site, UX Podcast and SVPG publish no
terms page that a probe of common paths could find. jeffgothelf.com, leanspark.ai, Atomic Object and GitHub were
cleared in the placement research. Ten pages on barred sites were found and not read, and one was read in error; the closing section
lists them. None carried a claim this log needs.

**What could not be found.** No source prints the 2019 version's prompt questions and hints box by box; the
2019 post gives headings, the reason each box changed and one example per box [4]. No source compares Patton's
Opportunity Canvas with Maurya's Lean Canvas by name. No source read in full criticises the canvas for too many
boxes, for inviting solutions first, or for misuse as a requirements form; the one lead was on Atlassian's site.
No source gives a named owner, a decision date or a numeric confidence scale for the canvas.

## Findings

### 1. What the canvas is, and its three versions

Jeff Gothelf published the first version on 2016-12-15, written for a client: "I was asked by a client to
codify some of the product discovery training we had worked on together." [1]. He framed it as a codification
of the book's process [1]. Version 2 followed on 2019-09-09 [4], and on 2024-11-04 Gothelf and Josh Seiden
renamed it: "The canvas is now called the Lean Product Canvas." [2]. Their reason was scope, not a flaw: "fundamentally there
was nothing wrong with the canvas in its current state rather its positioning and prompts had to shift to
reflect a broader scope." [2]. The 2024 PDF calls itself version 3 ("Lean Product Canvas (v3) Title of initiative:"
[5]), while its download link names the file version 1 of the new name [2]. Both can be true: one counts the
lineage, the other the name. Confidence: high.

The third edition of the Lean UX book (2021) is organized around the canvas [7]. The book introduces it in
chapter 4 and gives each box a chapter, 5 to 12 [19]. It calls the canvas "one comprehensive facilitation tool we
call the Lean UX Canvas" [19], and a single page for framing "a feature, an epic or initiative, or even an entire
product" [19]. It also says the canvas is optional to the method: "Although you don’t have to use the canvas to do
Lean UX, we’ve found that the canvas is a great way to explain the process" [19]. The first edition dates to 2013
[2], three years before the canvas.

### 2. The eight boxes, in 2019 and in 2024

The 2019 headings, from Gothelf's own post [4]: Box 1, Business problem statement; Box 2, Business outcomes;
Box 3, Users; Box 4, User outcomes and benefits; Box 5, Solutions; Box 6, Hypotheses; Box 7, What's the most
important thing we need to learn first?; Box 8, What's the least amount of work to learn the next most
important thing? The 2024 PDF [5] keeps the eight boxes and their order, with three heading changes: Box 1
reads Business Problem, Box 4 reads "User Outcomes & Benefits (JTBD)" [5], and Box 8 reads "What's the least
amount of work we need to do to learn the next most important thing?" [5]. The 2024 PDF adds header fields, a
title, a date and an iteration ("Date: Iteration:" [5]). Confidence: high, read from the PDF text and the post.

**What each box asks, by the 2024 PDF and the book.** Box 2's 2024 hint asks for high-level key results in the
format of the OKR book's who-does-what-by-how-much [2], [5]. The book defines an outcome as "a change in human
behavior that creates value" [19]. Box 3's hint widens users beyond buyers to people who configure the product
or are affected by it [5]. Box 4 adds jobs to be done [2], [5]. Box 5 lists "product, feature, or enhancement
ideas" [5]; the 2019 version had widened it to "new systems or business models as well as non-technical
solutions" [4]. Box 6 combines Boxes 2 to 5 into one sentence: "We believe that [business outcome] will be
achieved if [user] attains [benefit] with [feature]." [5], with the hint "Each hypothesis should focus on one
feature only." [5]. Box 7 picks a hypothesis, lists the ways it might fail and chooses the riskiest assumption,
with the hint "In the early stages of a hypothesis focus on risks to value rather than feasibility." [5]. Box 8
designs the experiment: "Design experiments to learn as quickly as you can whether your riskiest assumption is
true or false." [5]. The book's MVP is "a small and fast way of learning something" ("When we say MVP, we are
talking about a small and fast way of learning something." [19]).

**The Hypothesis Prioritization Canvas sits between Box 6 and Box 7.** Gothelf says so in those terms [6]: it
is a two-by-two of risk against perceived value ("The HPC is a two-by-two matrix with the x-axis measuring risk,
and the y-axis measuring perceived value." [19]), and only high-value, high-risk hypotheses go on to Boxes 7 and
8 ("Box 1 - Test" [6]). High-value, low-risk ones are built and measured without discovery work ("High value, low
risk hypotheses don’t require discovery work." [6]), and low-value, high-risk ones are discarded [6]. The 2024
PDF's Box 7 points to it by link [5]; the 2019 post, two months older than the prioritization canvas, does not.

**The numbering is the filling order on a first pass, and only then.** Box 6 cannot be written before Boxes 2
to 5 exist ("We pull business outcomes from Box 2, personas from Box 3, benefits from Box 4, and solutions from
Box 5." [19]), and Gothelf's walkthrough starts at Box 1 ("We’ll start off with the business problem statement."
[7]). The book also says "you can absolutely use each box on the canvas as a standalone technique" [19].

**A design rationale overlay.** The 2019 PDF carried "an overlay page in the PDF version that provides the
rationale behind the design of the canvas" [4], and the 2024 PDF carries one too [5]: the canvas moves from a
current condition, now, to "its desired future state or target condition" [19], later.

### 3. Practice: who fills it, for how long, and when it stops

**It is written as an initiative starts, by the whole team.** The book: "We think that the canvas is a great way
to start an initiative." [19], and "the canvas is a great structure to use for your kickoff meeting" [19].
"So we believe that all team members should participate in the work on the canvas." [19], with stakeholders and
clients "as much as possible" ("We also think that stakeholders and clients should participate as much as
possible" [19]). Gothelf calls it a facilitation tool: "It's a facilitation tool for cross-functional teams
designed to create a customer-centric conversation" [4]. Atomic Object, a software consultancy, used it at the
start of software products [8].

**A first pass takes from half a day to a couple of weeks.** The book: "It’s hard to get through the whole thing
in less than a half-day session." [19], while "Other teams will choose to hold a series of meetings over the
course of a couple of weeks." [19]. A lead business analyst's team took about a day and filled it on brown paper
that they photographed [9]. The book's advice for an unknown: "When you don’t know something, put it in the
parking lot and move on." [19].

**It is revised while experiments run.** After Box 8, the loop returns to Box 7: "If we should, then we ask the
questions again in box number 7." [7]. When a test proves a hypothesis false, the team returns to its backlog
of hypotheses [19]. Discovery can also send a team back to Box 1, since "you may uncover evidence that you’re
working on the wrong problem or targeting the wrong audience or measuring success in the wrong way" [19].

**It ends when other tools take over.** Atomic Object: "On each project, there came a point where the canvas had
enough definition that it was essentially abandoned in favor of other tools" [8]. The same post calls it a
living document while it lasts [8], and names upkeep with clients who were not in the room as its hardest
practical problem ("Another challenge was the distribution and upkeep of the canvas" [8]). Confidence: medium;
this rests on one named team.

### 4. Debates

**Box 2 against Box 4.** Gothelf rewrote Box 4 in 2019 because "This has been the part of the canvas with the
most confusion." [4], and an independent podcast episode on the update reports the same [12]. His resolution
[10]: business outcomes are measured behaviour ("Business outcomes are measures of human behavior." [10]), while
user outcomes are the reasons users seek the product, often "not measurable goals" ("Often these are not
measurable goals. They are intangible states of being." [10]). Ideally the two align [10]. He has also called
Box 2 the most critical box, because its outcomes are the success criteria of Box 6's hypotheses [11]. A
minority reading treats Box 4 as an ethics box, a place to map what could go wrong for users [12]; Gothelf's
pages do not use that reading.

**Facilitation tool or document.** No source read in full argues either side by name, so this is not a debate
with camps; it is a tension the sources leave open. The originators call the canvas a facilitation tool [4],
[19], and the 2024 post says both canvases help teams "have the right conversations as they set out on new
initiatives together" ("We designed these two canvases to help teams have the right conversations as they set out
on new initiatives together." [2]). The book's own list of what canvases do includes one item for the written
form: "Communicate the challenge or work the team is undertaking broadly beyond the team." [19]. One team
photographed brown paper and moved on [9]; another kept the canvas as a living document until other tools took
over [8]. Confidence: medium.

**The new name.** Gothelf renamed the canvas in 2024 [2]. Creately's guide, written after the rename, still
leads with the old name and treats the new one as its latest evolution [13]. One source is not a measure of
adoption, so this log says only that the old name persists in at least one current third-party guide.

**The hypothesis sentence has two wordings.** The book's template is active ("We believe we will achieve") and
the 2024 PDF's is passive ("will be achieved if") [5], [19]. Both carry the same four slots. This is a
documented evolution, not an error.

### 5. Relationships

**The Hypothesis Prioritization Canvas** is a companion that ranks the hypotheses Box 6 produced; it is not an
alternative canvas [6]. **The Lean Strategy Canvas** (2024) is "a facilitation tool for teams designed to set up
better work using the Lean Product Canvas" ("This is a facilitation tool for teams designed to set up better work
using the Lean Product Canvas." [2]); it is not admitted to this library. **Ash Maurya's Lean Canvas** models a
whole business: "A Lean Canvas is a 1-page business modeling tool that helps you deconstruct an idea into key
assumptions or beliefs." [15]. Creately draws the line between the two in a vendor's words: the Lean UX Canvas
validates product or feature assumptions, and the Lean Canvas business-model and revenue assumptions [13].

**Jeff Patton's Opportunity Canvas** overlaps it most: "The opportunity canvas is the right abstraction level for
discussing a new feature idea for an existing product." [14]. Patton draws his line against the Business Model
Canvas, not against Gothelf's canvas [14]. **Marty Cagan's Opportunity Assessment** draws the same line between
canvases for new businesses and a lightweight tool for an existing product's features [17]. No source compares
the Lean UX Canvas with either of the two by name; the companion should name the overlap and say so.

**OKRs.** Gothelf maps an OKR onto the canvas: the objective comes out of Box 1 and the key results out of Box 2
[16]. The canvas does not add an OKR section; it produces both halves from boxes it already has [16].

**Experiment design and the PRD.** Box 8 sketches the least work that would test the riskiest assumption [5],
[19]. No source read here says which document takes over when that work is a full experiment, or when the team
commits to building. That sequence is the library's POSITION, as the spec records.

**Problem statements and personas.** No source read in full says that a problem statement or a persona feeds
Boxes 1 and 3. Gothelf's walkthrough starts from the business problem statement [7], and the book uses
proto-personas for Box 3, but the line between those documents and the canvas is the library's to draw.

### 6. The gap question: candidates, routed under decision procedure 12

The gap dimension did not read the spec, the ADR or the contract before searching. Two sources carry its
findings, both built on top of the canvas rather than by its originators: Creately's guide [13] and Dean Peters's
skill file [18]. Each candidate below is routed as decision procedure 12 requires: most become a guide rubric
row, and none adds a section by itself.

1. **A dated record of each pass.** The 2024 PDF's own header carries a date and an iteration [5]. Peters's
   output template carries "Iteration: 1" [18], and Creately advises "Use versioning and iteration to ensure the
   canvas reflects current knowledge." [13]. Peters says the canvas is "Not a one-time exercise: Re-visit as you
   learn; update assumptions" [18]. **Routing: this supports the spec's ninth section, Revisions and What Takes
   Over**, which the spec labelled the library's POSITION for want of a source. The canvas's own iteration field
   [5] is now that source for a dated pass; the successor half stays POSITION.
2. **A verdict on each experiment.** Creately asks for "Documented outcomes, insights, and next steps linked back
   to assumptions." [13], and Peters for "Document learnings - What did you learn? Was the assumption validated or
   invalidated?" [18]. **Routing: fold into the ninth section's rows**, as a column for what was learned and
   whether the assumption held, not a new section.
3. **Assumptions ranked by risk.** Both sources rank them [13], [18]. **Routing: already covered** by Box 7 and
   the Hypothesis Prioritization Canvas [5], [6]; a rubric row can test that Box 7 names one assumption, not a
   list.
4. **Named failure modes.** Peters lists six pitfalls, among them starting with solutions, vague business
   outcomes, too-broad user segments, confusing Boxes 2 and 4, one solution only in Box 5, and skipping Box 8
   [18]. **Routing: guide anti-patterns and template TRAP lines.**
5. **Null results.** No source gives a named owner, a decision date or a numeric confidence scale for the canvas,
   and nothing was found that the bundle should add as a section of its own.

## Claims flagged contested or time-bound

- **The name is time-bound.** The canvas has been the Lean Product Canvas since 2024-11-04 [2]. The bundle keeps
  the older name by the maintainer's ruling, with the new one as an alias.
- **The 2024 wording supersedes 2019 where they differ.** Box 1, Box 4 and Box 8 changed headings, and Box 2,
  Box 4 and Box 7 changed prompts [2], [5]. Box 5's breadth narrowed in wording between 2019 and 2024 [4], [5];
  whether the 2019 widening survives is not settled by the texts.
- **The hypothesis sentence has two wordings**, active in the book and passive in the 2024 PDF [5], [19].
- **Box 4's purpose** has a minority reading as an ethics box [12], which the originators do not use.
- **How long a first pass takes** spans half a day to a couple of weeks [19], [9]; scope explains the spread,
  not disagreement.
- **The Opportunity Canvas line** is drawn against the Business Model Canvas [14], and against Maurya's canvas
  only by chaining [14] and [15]. It is the library's inference, not a source's claim.

## Honest framing

This bundle frames one initiative on one page, in Gothelf and Seiden's eight boxes, before anyone commits to
building. It is honest about four things.

- **The canvas is a facilitation tool first.** Its originators call it one [4], [19], and its value is largely the
  conversation that fills it. The filled page is the record of that conversation and the place its revisions
  are kept; the companion must not claim that the filled canvas is the value.
- **Two of the bundle's lines are the library's POSITION, not sourced.** Where the canvas sits in the chain
  before `experiment-design-doc`, `design-brief` and the PRD, and the duplication answer in ADR 0082, are
  argued, not found. The guide must say so.
- **The ninth section is half sourced.** A dated pass is in the 2024 canvas's own header [5]; what takes over
  when the canvas is finished is the library's POSITION, from Atomic Object's account of the canvas being
  abandoned for other tools [8] and the family's successor obligation.
- **The canvas is copyrighted, and no open licence was found.** The bundle names the boxes, quotes briefly with
  attribution, and writes every guidance comment in its own words.

## Notes for the companion

**Load-bearing sections.** Box 2 and Box 4 (the confusion, and Gothelf's resolution [10], [11]); Box 6 (the
hypothesis grammar and one feature per hypothesis [5], [19]); Box 7 (one riskiest assumption, risks to value
first, the prioritization canvas [5], [6]); the ninth section (revisions and successor).

**Sharpest teaching points.**
- Business outcomes are measured behaviour change; user outcomes are why users come, and often are not
  measurable [10]. Writing a revenue target in Box 2 or a feature in Box 4 is the box's commonest error [18].
- One hypothesis tests one feature [5]. A hypothesis with several features cannot be tested cleanly.
- Box 7 names the single most important thing to learn right now [7], not every risk.
- Box 8 is the least work that would learn it: an MVP is a way of learning, not a small release [19].
- The canvas is revised: after Box 8 the team asks Box 7's question again [7], and it ends when other tools take
  over [8].

**Name both versions.** Record the 2019 headings [4] and the 2024 wording [5] in the companion, as choice C3
rules, and say which the template uses where they differ.

**The example.** The worked example is a canvas for the FY26 roadmap's Later item 6, Collaborative analysis
(`templates/product-roadmap/product-roadmap_example.md`, the Later section): analysts who answer a question get
asked the same question again by someone else, nobody has shaped it, and it may belong to the support team
rather than to the product. That is an unshaped initiative with no investment behind it, which is the canvas's
ground. Gothelf's Box 5 invites non-technical solutions [4], so the support-team option belongs in Box 5. The
example must carry these facts without contradiction. It is dated after the roadmap and before the roadmap's
review on 15 October 2026 (the roadmap's Review Trigger), so a date in September 2026 fits, and it cites no
later document. Box 2's outcome ladders to the roadmap's measure, the share of new accounts that build a second
view within 14 days, from a 31 percent baseline to 50 percent, or states why it does not. Box 3 names the
Recurring Analyst, by that name, as `templates/product-strategy/product-strategy_example.md` requires. Its
Hypotheses must not name Saved Views sharing as a new solution, because the internal announcement already tells
the Reporting squad it can share a saved view with a teammate today
(`templates/announcement-internal-comms/announcement-internal-comms_example.md`). The ninth section should show
at least one dated revision after an experiment returned, and name what takes over. All figures in the example
are illustrative and must be labelled so.

**Template GOOD and WEAK text must not reuse the example's scenario.** Use other initiatives and other
products in the guidance comments; grep for "collaborative", "Recurring Analyst" and "support team" before review.

## Sources

### Origins: three versions and a rename, 2016 to 2024

**[1] Jeff Gothelf, "The Lean UX Canvas" (v1 blog post).** primary. **fetched-and-verified.**
`https://jeffgothelf.com/blog/leanuxcanvas/`
Supports: Dates v1 to December 15, 2016 (page byline "Posted on December 15, 2016"); establishes sole/first-person authorship and the canvas's relationship to the Lean UX book and to other canvases; shows the page was later edited to add a V2 pointer
Quotable: "I was asked by a client to codify some of the product discovery training we had worked on together."
Quotable: "I created The Lean UX Canvas."
Quotable: "This canvas codifies the process we first introduced in the Lean UX book."
Quotable: "I prefer to pick and choose the assumptions that can be found on the Business Model Canvas, Lean Canvas and others as appropriate for the client, project or initiative I'm working on and weave them together to form testable hypotheses and experimentation plans."
Quotable: "( Lean UX Canvas V2 is now live and a brand new video showing how to use the Lean UX Canvas is now available . )"

**[2] Jeff Gothelf, "The Lean Product Canvas" (2024 rename post).** primary. **fetched-and-verified.**
`https://jeffgothelf.com/blog/the-lean-product-canvas/`
Supports: Dates the rename to November 4, 2024 (page byline). The originators' account of why the Lean UX Canvas became the Lean Product Canvas (its scope, not a flaw), what changed in the prompts (Box 2 gained the OKR book's 'who does what by how much' language, Box 4 jobs to be done, Box 7 a pointer to the Hypothesis Prioritization Canvas), and the companion Lean Strategy Canvas, a facilitation tool designed to set up work on the Lean Product Canvas. That both canvases help teams have the right conversations as they set out on new initiatives, and that the prompts are not specific to any one role. Corroborates a 2019 date for version 2 ('5 years since we last updated') and gives 2013 for the book's first edition. The download link names the file v1 of the renamed canvas, while the PDF itself reads v3
Quotable: "It's been 5 years since we last updated the Lean UX Canvas."
Quotable: "As Josh Seiden and I synthesized the feedback two things became clear - fundamentally there was nothing wrong with the canvas in its current state rather its positioning and prompts had to shift to reflect a broader scope."
Quotable: "The scope of Lean UX has grown significantly since the first edition of the book was published in 2013."
Quotable: "The canvas is now called the Lean Product Canvas."
Quotable: "We explicitly added in the language from our new book on OKRs, Who does what by how much?, in Box 2 so teams would write better business outcomes."
Quotable: "Box 4 now has explicit “jobs to be done” language-something we've been teaching for years but hadn't added to the canvas until now."
Quotable: "And Box 7 now makes an explicit reference to the Hypothesis Prioritization Canvas as the tool for deciding which hypothesis to test first."
Quotable: "Over the past 5 years Josh and I have been teaching a lot of product strategy and even more Objectives and Key Results."
Quotable: "LeanProduct_canvas_v1-nov2024_FINAL Download"
Quotable: "We designed these two canvases to help teams have the right conversations as they set out on new initiatives together."
Quotable: "These aren’t prompts specific to UX designers, product managers or software engineers."
Quotable: "This is a facilitation tool for teams designed to set up better work using the Lean Product Canvas."

**[3] InfoQ, "Lean UX Explained" (interview with Jeff Gothelf, by Harry Brumleve).** practitioner. **fetched-and-verified.**
`https://www.infoq.com/interviews/lean-ux-explained-jeff-gothelf/`
Supports: Checked for canvas-origin content; dated March 1, 2013 (page metadata and byline "Mar 01, 2013"), which predates the canvas's 2016 creation by over three years, so it supports only that this interview cannot be a source for canvas history, not any claim about the canvas itself
Quotable: "Mar 01, 2013 Interview with Jeff Gothelf by Harry Brumleve"

### Structure: the eight boxes in the 2019 and 2024 versions

**[4] Jeff Gothelf, "Lean UX Canvas V2", jeffgothelf.com, posted September 9, 2019.** primary. **fetched-and-verified.**
`https://jeffgothelf.com/blog/leanuxcanvas-v2/`
Supports: Gothelf's account of the 2019 version 2: its eight box headings; why Boxes 2, 3 and 4 changed (Box 2 needed a clearer line against Box 4, teams took a shortcut on Box 3, and Box 4 was the part of the canvas with the most confusion); that Box 6 saw no significant change; that Box 5 was widened to new systems, business models and non-technical solutions; an overlay page in the PDF giving the design rationale; one worked example per box, among them a hypothesis and a Box 8 experiment; that the canvas is a facilitation tool for cross-functional teams; and the later banner saying it became the Lean Product Canvas and the Lean Strategy Canvas
Quotable: "It's a facilitation tool for cross-functional teams designed to create a customer-centric conversation"
Quotable: "I noticed that teams were taking a bit of a shortcut with this box"
Quotable: "UPDATE: The Lean UX Canvas has been updated into the Lean Product Canvas and the Lean Strategy Canvas."
Quotable: "Box 6 - Hypotheses"
Quotable: "No significant change here."
Quotable: "We believe a 25% reduction in administration costs will be achieved if Rochelle the System Admin spends less time configuring users with a batch configuration tool."
Quotable: "value should be the main focus, not feasibility in most cases"
Quotable: "Interview 10 admins that match Rochelle’s profile to understand how they add users today."
Quotable: "new systems or business models as well as non-technical solutions"
Quotable: "The download links aren’t working"
Quotable: "This has been the part of the canvas with the most confusion."
Quotable: "The original goal here was to call these “outcomes” out as emotional goals but the language got confusing."
Quotable: "big, small, innovative and perhaps a bit “weird.”"
Quotable: "Box 1 - Business problem statement"
Quotable: "Box 2 - Business outcomes"
Quotable: "Box 3 - Users"
Quotable: "Box 4 - User outcomes and benefits"
Quotable: "Box 5 - Solutions"
Quotable: "Box 7 - What’s the most important thing we need to learn first?"
Quotable: "Box 8 - What’s the least amount of work to learn the next most important thing?"
Quotable: "A clearer distinction was needed between this box and Box 4."
Quotable: "One other thing you’ll note is an overlay page in the PDF version that provides the rationale behind the design of the canvas."

**[5] Jeff Gothelf, Lean Product Canvas (v3) and Lean Strategy Canvas (v1) PDF, Nov 2024 (jeffgothelf.com).** primary. **fetched-and-verified.**
`https://jeffgothelf.com/wp-content/uploads/2024/11/LeanProduct_canvas_v1-nov2024_FINAL.pdf`
Supports: The 2024 v3 canvas's exact box headings, prompt questions, hints, header fields, and the NOW/LATER overlay labels
Quotable: "Lean Product Canvas (v3) Title of initiative:"
Quotable: "Date: Iteration:"
Quotable: "We believe that [business outcome] will be achieved if [user] attains [benefit] with [feature]."
Quotable: "Each hypothesis should focus on one feature only."
Quotable: "What's the most important thing we need to learn first?"
Quotable: "In the early stages of a hypothesis focus on risks to value rather than feasibility."
Quotable: "refer to our Hypothesis Prioritization Canvas (https://bit.ly/hypo-canvas)"
Quotable: "What's the least amount of work we need to do to learn the next most important thing?"
Quotable: "Design experiments to learn as quickly as you can whether your riskiest assumption is true or false."
Quotable: "User Outcomes & Benefits (JTBD)"
Quotable: "List product, feature, or enhancement ideas here."

**[6] Jeff Gothelf, "The Hypothesis Prioritization Canvas" (jeffgothelf.com blog, Nov 8, 2019).** primary. **fetched-and-verified.**
`https://jeffgothelf.com/blog/the-hypothesis-prioritization-canvas/`
Supports: How Box 7 uses the Hypothesis Prioritization Canvas: its axes and its four quadrant outcomes; The exact line between the Lean UX Canvas and the Hypothesis Prioritization Canvas: the HPC is a companion tool, not an alternative canvas, and it slots in at a named point inside the Lean UX Canvas workflow (between Box 6 and Box 7), prioritizing hypotheses the Lean UX Canvas has already produced by risk and perceived value rather than re-deriving them
Quotable: "the Hypothesis Prioritisation Canvas (HPC) comes into play between Box 6 (writing hypotheses) and Box 7 (choosing the most important thing to learn next)"
Quotable: "The horizontal axis measures your assessment of the risk of each hypothesis."
Quotable: "The vertical axis measures perceived value."
Quotable: "Box 1 - Test"
Quotable: "Box 2 - Ship & Measure"
Quotable: "High value, low risk hypotheses don’t require discovery work."
Quotable: "Box 3 - Don’t test. Usually don’t build."
Quotable: "Box 4 - Discard"
Quotable: "Hypotheses that we deem to have low value and high risk are thrown away."
Quotable: "If you're familiar with the Lean UX Canvas, the Hypothesis Prioritisation Canvas (HPC) comes into play between Box 6 (writing hypotheses) and Box 7 (choosing the most important thing to learn next)."
Quotable: "The horizontal axis measures your assessment of the risk of each hypothesis. ... The vertical axis measures perceived value."
Quotable: "Box 1 - Test ... Box 2 - Ship & Measure ... Box 3 - Don't test. Usually don't build. ... Box 4 - Discard"

### Practice: how teams fill, revise and leave the canvas

**[7] Jeff Gothelf, "How to use the Lean UX Canvas" (video transcript), jeffgothelf.com, posted June 28, 2021.** primary. **fetched-and-verified.**
`https://jeffgothelf.com/blog/how-to-use-the-lean-ux-canvas/`
Supports: Gothelf's 2021 video walkthrough, as a transcript: that the third edition of the Lean UX book is organized around the canvas and that the canvas is the book's backbone (the page's phrase 'structured around' describes a self-paced video class, not the book); the walk through the boxes, starting from the business problem statement; that business outcomes are measurable changes in human behavior; that Box 7 names the one thing most important to learn right now; and the loop from Box 8 back to Box 7 as experiments return
Quotable: "We’ll start off with the business problem statement."
Quotable: "Most importantly, you should call them measurable changes in human behavior."
Quotable: "That’s great but your job is to identify the thing that’s most important right now."
Quotable: "If we should, then we ask the questions again in box number 7."
Quotable: "What’s the next most important thing we need to learn?"
Quotable: "The third edition of the Lean UX book is coming out soon and it’s organized around the Lean UX Canvas."
Quotable: "The backbone of the book is the Lean UX Canvas."
Quotable: "On top of that, we’re working on a self-paced video Lean UX class. Again, that’s structured around the Lean UX Canvas."

**[8] Bryan Elkus, "Intro to Lean UX Canvas - Defining a Software Solution", Atomic Object blog, posted October 2, 2019.** practitioner. **fetched-and-verified.**
`https://spin.atomicobject.com/lean-ux-canvas-intro/`
Supports: A named team's (Atomic Object, software design/development consultancy) multi-project experience: when in the lifecycle they used it, the point at which they stopped using it in favor of other tools, and the practical difficulty of distributing and maintaining a shared canvas (whiteboard vs. digital stickies vs. shareable spreadsheet vs. Miro board) with clients who were not in the room daily
Quotable: "On each project, there came a point where the canvas had enough definition that it was essentially abandoned in favor of other tools"
Quotable: "Another challenge was the distribution and upkeep of the canvas"
Quotable: "Your Lean UX Canvas can be a living document that shows where the project is in its progression"
Quotable: "can be leveraged at the beginning of new software products to help align the team around the problem"

**[9] Rohela Raouf, "UX Canvas", Modern Analyst Community Blog, posted October 26, 2017.** practitioner. **fetched-and-verified.**
`https://modernanalyst.com/Community/CommunityBlog/tabid/182/ID/3861/UX-Canvas.aspx`
Supports: A named lead business analyst's first-hand account of introducing the canvas to her team on a 100-day-delivery project (after a frantic 3-week discovery phase): who was in the room, that it took about a day to fill the whole canvas, where the team disagreed (Solution ideas, between the user researcher and service manager), and that they filled it on brown paper rather than a polished artifact
Quotable: "It took the team about a day to complete the canvas"
Quotable: "we completed ours on brown paper that we took a photo of"
Quotable: "this is one that caused us the most discussion in the team"

### Debates: business and user outcomes, tool or document, the new name

**[10] Jeff Gothelf, "What's the difference between a user outcome and a business outcome?" (jeffgothelf.com blog, Feb 6, 2023).** primary. **fetched-and-verified.**
`https://jeffgothelf.com/blog/difference-between-user-outcome-and-business-outcome/`
Supports: Q1 resolution: Gothelf's own explanation of the intended Box 2 (business outcomes) vs. Box 4 (user outcomes) split, written specifically to answer recurring confusion about it
Quotable: "In fact, we love this concept so much, we put it in the canvas twice. In Box 2 we refer to business outcomes. In Box 4 we refer to user outcomes."
Quotable: "Business outcomes are measures of human behavior."
Quotable: "These are examples of user outcomes. They are the reasons your users are seeking out, using and recommending your products and services."
Quotable: "Often these are not measurable goals. They are intangible states of being."
Quotable: "In an ideal world they are aligned so that when a user achieves their “user” outcome, they change their behavior in a positive way that is also beneficial to the business."

**[11] Jeff Gothelf, "Outcomes are the success criteria for your hypotheses" (jeffgothelf.com blog, Oct 17, 2022).** primary. **fetched-and-verified.**
`https://jeffgothelf.com/blog/outcomes-are-the-success-criteria-for-your-hypotheses`
Supports: Box 2's role as the canvas's most-load-bearing box (success criteria for Box 6 hypotheses), used as context for why the Box 2/Box 4 line matters rather than being a cosmetic labeling issue
Quotable: "Perhaps the most critical box in the entire canvas is Box 2 - Business Outcomes."
Quotable: "the outcomes we generate during this exercise serve as the success criteria for the hypotheses we write in Box 6 of the canvas"
Quotable: "An outcome is measure of human behavior. It tells us how the feature we shipped has impacted the people that consume it."

**[12] James Royal-Lawson and Per Axbom, "Positive user experience" (UX Podcast, episode 220, Sept 2019) - discussion of the 2019 Lean UX Canvas V2 update.** practitioner. **fetched-and-verified.**
`https://uxpodcast.com/positive-user-experience-2`
Supports: Q1: independent (non-Gothelf) confirmation that Box 4 (user outcomes and benefits) was, in the hosts' words, the single most confusing part of the canvas, worse than any other box including Box 2; also supplies a dissenting characterization of what Box 4 is really for (an "ethics box"), which is a reading Gothelf's own posts do not use
Quotable: "box number 4, which is where you want the users to be in the future, like the user outcomes and benefits. This was the part of the canvas with the most confusion."
Quotable: "when it comes to box number 3, which is users, he noted, he had noticed that teams were taking a bit of a shortcut with this box. So he needed a simplification clarification around that."
Quotable: "I actually wrote like box 4 is the the ethics box."
Quotable: "This is where you have the opportunity to like you were saying, map out what could go wrong, but also think about the indicators of what do I want for the users?"

**[13] Creately (Cinergix Pty Ltd) - "Lean UX Canvas: A Practical Tool for the Lean UX Process".** vendor. **fetched-and-verified.**
`https://creately.com/guides/lean-ux-canvas/`
Supports: A field-by-field 'Done looks like' completion bar, an explicit evidence-and-learnings step that logs each hypothesis as validated/invalidated and links it back to assumptions, assumptions ranked by risk, and an FAQ line on versioning/iteration so the canvas stays current; Q3: a third-party account of the v1 -> v2 -> Lean Product Canvas lineage, framing the rename as a shift away from the canvas being read as a static UX deliverable toward a broader, product-wide tool; corroborates that the newer name has NOT displaced the older one in general circulation (the guide itself still titles the page "Lean UX Canvas" while describing the Lean Product Canvas as its successor); A direct, independent two-canvas comparison (Lean UX Canvas vs. Lean Canvas) in the vendor's own words, plus independent description of the experiment-design/MVP-testing step that follows hypothesis-writing in the canvas flow, and of the canvas's version history (v1 -> v2 -> Lean Product Canvas) matching Gothelf's own account
Quotable: "A prioritized list of key assumptions, ranked by potential impact if wrong."
Quotable: "Documented outcomes, insights, and next steps linked back to assumptions."
Quotable: "“Users using the progress bar completed onboarding 20% more often; hypothesis validated.”"
Quotable: "Capture results from previous experiments. Note whether hypotheses were validated or invalidated, and highlight unexpected findings. Use these insights to refine assumptions and guide decisions."
Quotable: "Prioritize the next actions based on learnings. Decide which features, tests, or iterations to implement, assign owners, and ensure alignment on both immediate actions and longer-term roadmap priorities."
Quotable: "Use versioning and iteration to ensure the canvas reflects current knowledge."
Quotable: "Rank assumptions by risk and uncertainty. Focus on high-risk assumptions that, if proven wrong, would have the largest impact on product success."
Quotable: "The Lean Product Canvas, the latest evolution, broadens the focus from UX alone to full product discovery."
Quotable: "This evolution reflects a shift from creating static UX deliverables to using a dynamic, visual tool that accelerates learning, reduces wasted effort, and keeps teams focused on outcomes over outputs."
Quotable: "When should I use Lean UX Canvas instead of Lean Canvas (Ash Maurya)? Use Lean UX Canvas when your goal is to validate product or feature assumptions quickly and run experiments with real users. Lean Canvas by Ash Maurya is better suited for early-stage startups or business model validation, where the focus is on market viability and revenue assumptions."
Quotable: "Version 1 (v1) was the original canvas, focused on mapping assumptions and hypotheses to guide early experiments."
Quotable: "Version 2 (v2) refined the structure, adding clearer sections for business and user outcomes, prioritizing assumptions, and designing experiments that drive measurable learning."
Quotable: "Step 7. Design experiments ... Experiments can include prototypes, landing pages, concierge tests, interviews, or A/B tests. Define the scope, timeline, and success criteria for each experiment."
Quotable: "Common experiment types include qualitative interviews, prototype testing, concierge tests, and smoke tests (landing pages or minimal features)."

### Relationships: neighbouring canvases and documents

**[14] Jeff Patton - "Opportunity Canvas" (jpattonassociates.com).** practitioner. **fetched-and-verified.**
`https://jpattonassociates.com/opportunity-canvas/`
Supports: The line between the Opportunity Canvas and a whole-business canvas (Business Model Canvas, and by Maurya's own derivation chain, Lean Canvas): the Opportunity Canvas is scoped to a new feature or capability on an EXISTING product, where the business-model boxes (distribution, monetization, cost structure) are already settled and therefore irrelevant
Quotable: "An opportunity canvas is a one-pager that you'd use to unpack your beliefs about a new feature or capability you'd like to add to your product."
Quotable: "Yes, this looks like the business model canvas. But it's not. Osterwalder's Business Model Canvas is great for understanding and evaluating business model for a new business idea or product. But, if you're adding a new feature to an already existing product, that canvas doesn't quite make sense."
Quotable: "The opportunity canvas is the right abstraction level for discussing a new feature idea for an existing product."
Quotable: "For some organizations this canvas gets referred to as a lightweight business case."
Quotable: "Have discussions around an opportunity canvas for the big things - new features or capabilities. ... Because this big thing breaks down into small parts it's often called an epic canvas."
Quotable: "You could take every assumption you've made in this canvas and use David Bland's assumption mapping to help find riskiest assumptions."

**[15] Ash Maurya - "What is a Lean Canvas?" (LEANSpark / LEANSTACK).** primary. **fetched-and-verified.**
`https://leanspark.ai/learn/what-is-lean-canvas`
Supports: The Maurya boundary: the Lean Canvas is explicitly a whole-business modeling tool (an adaptation of the Business Model Canvas), not a feature-level tool, which is the line the lean-ux-canvas bundle needs against the feature-scoped Opportunity Canvas and the product/UX-scoped Lean UX Canvas
Quotable: "A Lean Canvas is a 1-page business modeling tool that helps you deconstruct an idea into key assumptions or beliefs."
Quotable: "Lean Canvas was created by me, Ash Maurya, and is an adaptation of Alexander Osterwalder's Business Model Canvas - optimized for the Lean Startup methodology."
Quotable: "My motivation for creating the Lean Canvas was not to create a better business model canvas but a different, more entrepreneur-focused one. I replaced these boxes: key partnerships, key resources, key activities, and customer relationships with these boxes: problem, solution, key metrics (KPIs), and unfair advantage (a defensible competitive advantage)."

**[16] Jeff Gothelf - "Creating OKRs with the Lean UX Canvas" (jeffgothelf.com, Oct 11, 2021).** primary. **fetched-and-verified.**
`https://jeffgothelf.com/blog/creating-okrs-with-lean-ux-canvas/`
Supports: The OKR line: the Lean UX Canvas does not add an OKR section: it produces an OKR's two halves from boxes it already has (the Objective from Box 1's 'how might we' extraction, the Key Results from Box 2's Business Outcomes), rather than treating OKRs as a separate, external artifact the canvas defers to
Quotable: "You're declaring your objectives as part of the work you and the team do in Box 1 - Business Problem Statement."
Quotable: "The objective statement comes out of the last part of the business problem statement template - from the "how might we" statement at the end."
Quotable: "So where are the key results? They aren't far away, on the other side of the canvas in Box 2 - Business Outcomes."
Quotable: "In Box 2 we ask you the question, "What will people be doing differently if we solve the business problem?" The answer is always a behavior of our target audience and is always quantifiable."
Quotable: "As you work your way through the canvas you'll also end up with proposed solution hypotheses that may help you achieve these OKRs."

**[17] Marty Cagan - "Lean Canvas vs. Opportunity Assessment" (Silicon Valley Product Group, June 22, 2013).** practitioner. **fetched-and-verified.**
`https://www.svpg.com/lean-canvas-vs-opportunity-assessment/`
Supports: A second, independent direct two-tool comparison that reinforces the same boundary Patton draws for the Opportunity Canvas, from a different named practitioner tool (the Opportunity Assessment, not Patton's own Opportunity Canvas): canvases (Business Model Canvas / Lean Canvas) suit a brand-new business or product line; a lightweight assessment tool suits an EXISTING product's new features, because the canvas's distribution/monetization/cost-structure boxes are already settled and so 'the majority of a Canvas is irrelevant.'
Quotable: "A Canvas is especially helpful when you are starting a new business, or creating an entirely new product line."
Quotable: "In contrast, when you have an existing product, we are constantly considering new projects, new designs, and new features, and an Opportunity Assessment is designed as a very lightweight tool for highlighting the risks of the new effort."
Quotable: "In the case of an existing product, the majority of a Canvas is irrelevant. You already have a distribution model. You already have a monetization strategy. There is already a well-defined cost structure."
Quotable: "The key questions in an opportunity assessment are: what problem are you trying to solve; who exactly are you solving this problem for; and how will you measure success?"
Quotable: "So if you're starting a company or even a new product line, consider a Canvas to highlight the key risks and frame your work. Once you have an existing product that you are investing in, consider using an Opportunity Assessment to highlight the key risks and frame the ongoing product discovery work."

### The gap question: what a good canvas does beyond the boxes

**[18] deanpeters/Product-Manager-Skills (GitHub) - lean-ux-canvas skill, SKILL.md.** practitioner. **fetched-and-verified.**
`https://raw.githubusercontent.com/deanpeters/Product-Manager-Skills/main/skills/lean-ux-canvas/SKILL.md`
Supports: A six-item 'Common Pitfalls' list naming the specific failure modes a plain eight-box form invites (solution-first framing, vague outcomes, broad segments, confusing the outcome boxes, single-solution thinking, skipping experiments), a hypothesis-testability rule, a named good-vs-bad example pair for the problem box, and an output template carrying Date and Iteration fields plus an explicit 'iterate until confidence is high enough to build' instruction
Quotable: "Not a one-time exercise: Re-visit as you learn; update assumptions"
Quotable: "Must be testable (you can design an experiment to validate/invalidate it)"
Quotable: ""Our checkout conversion rate dropped 15% after mobile traffic surpassed desktop. Our checkout flow wasn't designed for mobile, and competitors have one-tap checkout.""
Quotable: ""We need to increase revenue" (no context on what changed)"
Quotable: "Initiative: [Title]"
Quotable: "Date: [Today's date]"
Quotable: "Iteration: 1"
Quotable: "Document learnings - What did you learn? Was the assumption validated or invalidated?"
Quotable: "Update the canvas - Revise hypotheses based on learnings, choose next riskiest assumption"
Quotable: "Iterate - Repeat Box 7 → Box 8 until confidence is high enough to build"
Quotable: "### 1. **Starting with Solutions, Not Problems**"
Quotable: "### 2. **Vague Business Outcomes**"
Quotable: "### 3. **Too-Broad User Segments**"
Quotable: "### 4. **Confusing Box 2 and Box 4**"
Quotable: "### 5. **Only One Solution in Box 5**"
Quotable: "### 6. **Skipping Experiments (Box 8)**"

### A book read from the maintainer's own copy

**[19] Jeff Gothelf and Josh Seiden - Lean UX: Designing Great Products with Agile Teams, third edition (O'Reilly, 2021), chapters 3 to 13.** primary (book). **fetched-and-verified, read from the maintainer's own copy on 2026-10-30.**
No URL: a copyrighted book, read from a text copy of chapters 3 to 13 that the maintainer supplied from their own copy; a bookseller link would imply a retrieval that did not happen, and the text is never committed.
Supports: The originators' book, which presents the Lean UX process through the canvas: chapter 4 introduces it, and chapters 5 to 12 take one box each. That the canvas is a single-page way to frame a feature, an initiative or a product, and consolidates the earlier assumptions-declaration exercises into one facilitation tool. When to use it (to start an initiative, at a kickoff, for any big chunk of work), who works on it (the whole team, with stakeholders and clients as much as possible), and how long a pass takes (rarely under a half day; some teams spread it over meetings across a couple of weeks). That each box can be used as a standalone technique. The hypothesis grammar built from Boxes 2 to 5, the Hypothesis Prioritization Canvas as a risk and value two-by-two, the two key questions of Boxes 7 and 8, an MVP as a small and fast way of learning, and coming back to the hypothesis backlog when a test proves a hypothesis false. Chapter 13's case studies, one of which completed Box 4 by returning to feedback the team already held.
Quotable: "a change in human behavior that creates value"
Quotable: "We pull business outcomes from Box 2, personas from Box 3, benefits from Box 4, and solutions from Box 5."
Quotable: "We believe we will achieve [this business outcome] If [these personas] Attain [this benefit/user outcome] With [this feature or solution]"
Quotable: "a supposition or proposed explanation made on the basis of limited evidence"
Quotable: "The HPC is a two-by-two matrix with the x-axis measuring risk, and the y-axis measuring perceived value."
Quotable: "What’s the most important thing we need to learn first about this hypothesis?"
Quotable: "What’s the least amount of work we need to do to learn the next most important thing?"
Quotable: "When we say MVP, we are talking about a small and fast way of learning something."
Quotable: "you can absolutely use each box on the canvas as a standalone technique"
Quotable: "In order to complete Box 4, the team had to turn back to the feedback data that they had already collected from customers."
Quotable: "its desired future state or target condition"
Quotable: "It’s hard to get through the whole thing in less than a half-day session."
Quotable: "Other teams will choose to hold a series of meetings over the course of a couple of weeks."
Quotable: "We also think that stakeholders and clients should participate as much as possible"
Quotable: "Don’t get stuck in analysis paralysis."
Quotable: "We actually had the feedback. We just weren’t listening to it!"
Quotable: "We think that the canvas is a great way to start an initiative."
Quotable: "the canvas is a great structure to use for your kickoff meeting"
Quotable: "Generally, we think it’s a good idea to use it any time you’re planning a big chunk of work."
Quotable: "So we believe that all team members should participate in the work on the canvas."
Quotable: "It offers a single-page “at-a-glance” way of framing your work on a feature, an epic or initiative, or even an entire product."
Quotable: "one comprehensive facilitation tool we call the Lean UX Canvas"
Quotable: "Serve as an easy-to-follow facilitation tool for teams interested in having a specific kind of conversation."
Quotable: "When you don’t know something, put it in the parking lot and move on."
Quotable: "We’re simply moving forward with one and, if proven false, will come back to the backlog of hypotheses to do the process again."
Quotable: "you may uncover evidence that you’re working on the wrong problem or targeting the wrong audience or measuring success in the wrong way"
Quotable: "Create a shared language for the team to use."
Quotable: "Communicate the challenge or work the team is undertaking broadly beyond the team."
Quotable: "Although you don’t have to use the canvas to do Lean UX, we’ve found that the canvas is a great way to explain the process"

## Pages not read under the terms rule

The research agents found each page below and did not read it, because the site's terms of use forbid automated
access or the build treats the site as barred. The maintainer has not read any of them by hand. No claim in this
bundle rests on them. The excluded sites and their clauses are listed in `docs/internal/bundle-pipeline.md`,
under "The terms rule". The main loop read the terms pages of beehiiv, Tumblr and allo.io on 2026-10-30.

- `https://miro.com/templates/lean-product-canvas/`. Miro's terms bar scraping (runbook table). The page would
  have shown whether Miro's hosted template reproduces the 2024 box wording, and how it describes the rename.
- `https://miro.com/miroverse/the-hypothesis-prioritization-canvas/` and
  `https://miro.com/templates/the-hypothesis-prioritization-canvas/`. Miro, the same clause. The pages would have
  shown whether hosted copies keep Gothelf's quadrant labels. Gothelf's own page [6] settles the labels.
- `https://www.atlassian.com/blog/2013/10/fight-the-dark-side-of-lean-ux-with-the-experience-canvas`. Atlassian
  is treated as barred: admission sweep 7 reported a bar, and nobody has read its raw terms page. The post would
  have supported, by its title and search snippet, a 2013 critique of Lean UX practice and a companion canvas
  framed as something other than a requirements document. Two dimensions wanted it.
- `https://continuouslearning.beehiiv.com/p/september-9-2019-lean-ux-canvas-v2` and
  `https://continuouslearning.beehiiv.com/p/how-to-use-okrs-to-navigate-an-internal-crisis-b2b4bb8b99ec8429`.
  beehiiv's terms forbid "data mining, robots, crawling, scraping or data gathering or extraction methods". The
  pages would have supported an independent account of the 2019 update and of the 2024 rename.
- `https://engineering.kaptest.com/post/74879609264/lean-ux-workshop`. A Tumblr-hosted blog; Tumblr's terms
  forbid scraping the service and automated access outside its published interfaces. The page would have
  supported one team's account of running a Lean UX workshop.
- `https://allo.io/help/canvas/run-a-workshop`. allo.io's terms forbid "automated software or other means to
  access, 'scrape,' 'crawl' or 'spider' any pages". The page would have supported general canvas-workshop
  facilitation, an agenda ending in decisions and next steps.
- `https://uxplanet.org/one-year-of-lean-ux-68027e5a7214` and
  `https://medium.com/@jboogie/the-lean-ux-canvas-d4da53263c40`. Both are Medium-hosted. The agent treated
  Medium as barred, and Medium's terms page refused an automated read (HTTP 403) on 2026-10-30, so the clause is
  unchecked. The pages would have supported a solo practitioner's year of applying Lean UX across client
  engagements, and one practitioner's account of using the canvas.
- `https://ideascale.com/blog/what-is-lean-ux-canvas/`. **Read in error, then withdrawn.** The gap-question
  agent read this vendor page before checking IdeaScale's terms. Those terms forbid any "page-scrape," "robot,"
  "spider," or other automatic device used to access the services, which the main loop found on 2026-10-30 after
  the research stage. The entry was removed from this log. No claim rests on it, and nothing quoted from it
  appears anywhere in the bundle.
