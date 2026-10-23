# design-brief: research log

Research conducted 2026-10-22; the stored copies written during the run carry fetch stamps of 2026-10-23 UTC. It
builds on the third Define sweep, whose digest is dated 2026-10-16, and on the Define re-score of 2026-10-20 (PR
#300). It also builds on the approved spec (`docs/internal/tier2-specs.md:6530-6959`), specced the same day with
ADR 0079. ADR 0077's line between a concept and a specification, and ADR 0080's software-audience check, bound the
questions asked. The build's six dimensions covered the canon, section structure, altitude, practice by software
teams, boundaries, and the gap question. The canon asked what a brief is for, who writes it and when. Altitude
asked whether a brief carries a concept or a specification, and where the Shape Up pitch sits. The working files are
numbered differently: `dim1.md` holds practice, `dim2.md` the canon, `dim3.md` boundaries, `dim4.md` structure,
`dim5.md` the gap question and `dim6.md` altitude.

**32 sources are recorded below: 30 fetched-and-verified and two confirmed to exist but not read.** The 30 are 7
primary, 4 academic, 9 vendor, 8 practitioner, 1 standards body and 1 reference. Six of the seven primary sources
are Basecamp's three Shape Up chapters [10], [12], [13] and the Design Council's three documents [14], [15], [22].
The seventh is the Design Commission for Wales [5]. The two not read are Peter Phillips's book [4], a primary
source, and Noric Dilanchian's article [27], a practitioner's. Neither carries a quotation. Three fetched sources are
negative results, each read for something it turned out not to contain. They are Intercom's design process [20],
GV's Design Sprint page [25] and Teresa Torres's opportunity solution trees [26]. **228 Quotable lines remain.**
Quotable lines render the sources' long dashes as hyphens and keep their curly apostrophes; copy them as they stand.

**Every quotation was checked against the source's raw text**, not against a retrieval tool's summary. The six
dimensions returned 200 quotations from web sources, from 35 owned-source rows covering 30 URLs. Heap and Figma
were each owned by two dimensions, Y Combinator by three under two hostnames, and Shape Up's chapter 6 by three.
Against the stored copies, 187 passed strictly, 5 passed after extraction artifacts were normalized, and 8 failed.
A fresh fetch cleared 5 of the 8 and confirmed 3.

**Quotations from the spec sweep were then carried in, in two steps.** First, four were added by hand: three from
the Design Commission for Wales [5] and one from Kaninsky [9]. Second, `carry_spec_quotes.py` carried 29 more from
the spec sweep's verified quotations, for sources already in this log. Phillips's and Dilanchian's quotations were
excluded from both steps, because neither body could be re-read. `gen_sources.py` re-tested all 233 candidates
against the stored copies. It merged 6 duplicates that two dimensions had both returned. It dropped 4 quotations
and split one long list into six parts, each of which passes. The arithmetic is 200 plus 4 plus 29, less 6, 4 and
1, plus 6, which leaves 228. Of the 29 carried, 28 passed; Kaninsky's line on how long he has used the template
failed. `sources-report.txt` reports `split 5, dropped 4`. The split figure counts every quotation that failed as a
whole span, so it includes the four drops; only one of the five survived as parts.

---

## What the checks caught, and what was not read

**This log now carries every external span the spec quotes, except Phillips's and Dilanchian's.** The spec's
admission and section tables quote Kuse, Heap, Jones and Askland, Kaninsky, Wikipedia, Figma, uxmagic.ai, Y
Combinator, the Design Council and Basecamp. Each of those spans is a Quotable line here, or a part of one. The
exceptions are **all three Phillips sentences** (`docs/internal/tier2-specs.md:6580`, `:6625-6627`, `:6648-6649`,
`:6814`) and **both Dilanchian spans** (`:6586`, `:6689-6690`, `:6790-6791`). No drafting stage may quote those.
This log checked that by matching every quoted span in the spec's section against the Quotable lines.

**Two newly carried spans carry less than the spec reads into them.** Both readings were made in the stored raw
text for this log. Both spans may be quoted, but only with the framing below.

- Kuse's "including problem statement, goals, target users, constraints, and deliverables" [6] sits inside a sample
  prompt for Kuse's own AI drafting tool. It is not Kuse's statement of what a brief contains, which the spec takes
  it to be (`:6582`). Kuse's own definition is the better citation: a brief "defines the problem a design needs to
  solve, the context in which it exists, and the constraints that shape the solution" [6]. Confidence: high.
- Jones and Askland share the observation that a brief has no set structure, and they find "little common guidance
  on how to write and structure such a vital document" [24]. But "there is no single or correct format for a design
  brief" [24] is their report of Phillips's anecdotal view, from industry's side. Cite it as their report of
  Phillips, not as their own finding (`:6579`). Confidence: medium.

**The spec's risk 3 keeps its conclusion and loses its reason.** It says to cite only Heap's goal sentence and its
Problem Brief pairing, because the section names were an agent's reading (`:6879-6880`). Now both are Quotable
lines [7], checked against the stored page: the headings and the goal sentence. The goal sentence strengthens the
conclusion that Heap is a sense collision. It reads "The goal of a Design Brief is to describe, holistically and at
a high level, your proposed design solution(s)" [7]. Its Foundations section "outlines the key details of your
solution and the constraints within which it exists." [7]. Drafters may quote Heap's headings and goal, always
labelled as the solution sense. Heap's 27 Quotable lines were checked against the stored copy and were not
re-fetched in this pass.

**Phillips [4] and Dilanchian [27] were not read, and nothing rests on either alone.** The PDF mirror for Phillips
refused connections, and the 2026-10-16 sweep had checked his sentences only through Open Library's search
snippets. Dilanchian's live page and its Wayback snapshot both returned no text on 2026-10-22. Neither may be
quoted. The spec's risk 4 tightens as a result: Phillips may not be quoted at all from this log (`:6881-6882`).

- **The commissioning sense is carried by six read sources instead.** Visser: "design briefs are a document written
  by the person or organization wanting the design completed" [1], and "Design briefs are part of the communication
  between the client and the designer" [1]. Wikipedia: "A design brief is a document for a design project developed
  by a designer in consultation with a client." [23]. The Design Commission for Wales: "The project brief should be
  the central reference document used in the appointment of a consultant team." [5]. Colombi and Nocek's design
  management sense is "a negotiation of preliminary knowledge and requirements between the designer and the client"
  [3]. Read and Bohemia: "Upon receiving the commission or contact, a further ‘design brief’ is often developed"
  [2]. Jones and Askland's pre-project brief "is the responsibility of the client" [24]. Wikipedia adds that "The
  brief outlines the deliverables and scope of the project" [23].
- **The cadence exception is carried without Phillips's project-tracking sentence.** ADR 0077 cites that sentence
  beside Jones and Askland's (`docs/internal/decisions/0077-define-ends-with-a-chosen-concept.md:157-163`). Only
  Jones and Askland's is a Quotable line: a brief "should be used as a validation tool periodically throughout the
  project when making key decisions." [24]. Four more read sources support revision: [1], [2], [5], [23] (see
  Finding 1).
- **Dilanchian's early placement now has no carried source.** The spec reconciles it with the chain
  (`:6689-6692`), and its overruled sizes argument quotes him too (`:6790-6791`). The nearest carried ordering
  signal is Y Combinator's questionnaire, which ends on "About Engagement with Designer" [8].

**Four quotations were dropped, and one was split.** Each drop leaves a claim that may only be paraphrased.

- **Visser's definition of the brief as a short statement of a project's goals and limitations** [1]. In the stored
  PDF text, a running page header interrupts the sentence. It failed a fresh fetch too.
- **Colombi and Nocek's argument that the brief carries established norms and frames problems in ways that suit
  dominant groups** [3]. It passed the fresh fetch, but the generator reads the stored copy. There, a line-break
  hyphen splits one of its words. `dim2.md` offers this as a caution for the companion; it may only be
  paraphrased, with [3].
- **Shape Up's glossary entry for the verb to shape** [12]. It failed against the stored copy and a fresh fetch.
  `dim6.md` leans on it to show that shaping aims at a defined solution. That reading must rest on chapter 2's own
  lines instead [12].
- **Kaninsky's line on how long he has used the template** [9]. It was carried from the spec sweep and failed against
  his blog's text. Nothing in this log needs it.
- **Figma's list of what a design brief might include** [16] failed as one span. It was split into six parts, and
  all six pass.

**Thinner checks are recorded rather than smoothed over.**

- **The Eleven Lessons report's stored copy is an excerpt** [14]. It holds 2,576 bytes of a 330-page PDF, with
  bracketed notes saying where in the report each passage sits. Three of its four Quotable lines also passed a
  fresh fetch of the PDF. The Define summary list, "Key activities during the Define stage are:", passed only
  against the excerpt; its double-hyphen bullets are the excerpt's rendering.
- **The archived Design Council page** [15] returned HTTP 429 to the fresh fetch, so its two lines rest on the
  stored copy alone. `dim6.md` reports that the page's Define paragraph repeats its Discover paragraph. Neither of
  its Quotable lines is that repeated paragraph.
- **72 of the dimensions' quotations, from 11 URLs, were not re-fetched in the second pass.** For Atlassian [19] and
  Intercom [20], the first pass had itself read the live page. The other 67 rest on the stored copy alone. They
  include every dimension line from Heap [7] and Kuse [6], and nearly every one from Y Combinator [8].
- **The 32 spec-sweep lines that passed were not re-fetched in this build either.** `gen_sources.py` tested them against
  the stored copies only. The spec sweep had checked them against raw page text on 2026-10-22 (`:6572-6574`).
- **Y Combinator's post is itself an excerpt of an interactive tool**, which was not read. The post says so: "Answer
  the questions below to create a design brief or try the interactive version on my site." [8].

**Spans the dimension files present that are not Quotable lines.** Drafters who read the dimension files will meet
these and must not quote them:

- `dim6.md`: Shape Up's labels for wireframes as too concrete and words as too abstract, which appear in its
  Supports line only, and the dropped glossary entry.
- `dim1.md`: the Atlassian poster's owner, team size and three sections. Only three poster lines are Quotable [19].
- `dim3.md`: its description of Heap's review as a joint product, engineering and design leadership review. The
  Quotable line says only "with leadership" [7].
- `dim4.md`: Kuse's sentence on describing the problem without prescribing its solution, and Heap's worked example
  under Discarded Alternatives. It also reads Shape Up's appetite as a time box on design work alone. The Quotable
  line says only "How much time we want to spend and how that constrains the solution" [10].
- `dim5.md`: Asana's, Figr's and UXPin's success-metric sentences; Figr's line naming approvers; UXPin's sentence on
  who has the final say; UXPin's sentence that many briefs include specs; Design Pickle's tone-and-mood section; and
  Canny's request for examples of work the client likes.
- `dim2.md`: Visser's interview sample, described as designers across several continents. Only the line "in many of
  the interviews the projects discussed started without a design brief" is Quotable [1].

**Where the dimensions contradict one another.**

- **The gap dimension's two null results are contradicted by other dimensions' Quotable lines.** It found no
  design-brief source with a risks section; Kaninsky's template carries "Dependencies" and "Risks" [9]. It found no
  assumptions section; Heap's template carries "Assumptions:" [7]. Kaninsky's is a kickoff brief written before
  research, a neighbour in the spec's terms (`:6585`). That weakens the transfer to this bundle but does not erase it.
- **The practice dimension reports no named team's own material using the term design brief.** Heap [7] is
  exactly that, but another dimension owned it. The practice dimension's gap is a scope artifact.
- **The structure dimension lists Figr as unread; the gap dimension read it** [29].
- **The canon dimension tags Visser, Read and Bohemia, and Colombi and Nocek as primary.** The boundaries dimension
  tags Jones and Askland as standards, and the Design Council's history page and Wikipedia as practitioner. This log
  follows the tiers `order.json` sets: academic for the four papers, primary for the history page, reference for
  Wikipedia.

**What was assigned and not read, or not usable:**

- **Phillips's book** [4], including the chapter on a brief's essential elements, of which `dim5.md` saw only a
  publisher's table of contents. **Dilanchian's article** [27].
- **Kaninsky's 2020 original on UX Collective** returned HTTP 403. [9] is his own blog's later version, which the
  original calls newer. Whether the two section lists match is unchecked. The spec's row names the UX Collective
  version (`:6585`).
- **Named software teams**, assigned to the practice dimension: GitLab's handbook returned only navigation in three
  fetches; Spotify, Shopify and IBM's Enterprise Design Thinking surfaced nothing primary. Nielsen Norman Group and
  the Interaction Design Foundation surfaced no design-brief article. None has an entry. **None of these is a
  confirmed absence.**
- **Leads seen only in search results:** Shopify's Partners guide, lanpdt.com, skills.sh, Atlassian's design-review
  template, a UX Collective article on accessibility in briefs (HTTP 403), an XML Press documentation plan, and a
  stoppress.co.nz piece warning that an over-open brief also fails. None has an entry, and no claim rests on any.
- **The Design Management Institute's own treatment of the brief** was searched for and not found.
- **Dani Nordin's article and nibusinessinfo.co.uk** were not re-read and may not be cited, as the spec rules
  (`:6603-6605`). Experience brief is not an alias.
- **One repository file was owned and is not a numbered source.** `docs/internal/prototype-brief-admission-evidence.md`
  records, from an earlier pass, that GV's own page names no separately published Sprint Brief. It corroborates
  [25] and may be cited by path.

---

## Findings

### 1. What the canon says a design brief is

**The term has no settled meaning, and the literature says so.** Colombi and Nocek: "There is no clear or univocal
definition in the literature." [3]. A brief is "commonly intended as a statement whose form may vary from a
sentence to a structured document, articulating a project’s objectives, requirements, and constraints" [3]. Jones
and Askland found "little common guidance on how to write and structure such a vital document" [24]. Confidence:
high.

**The sources use at least four senses, and more variants beside them.** The spec's four (`:6612-6622`) are its
own assembly, and they hold against the build's reading:

- **Commissioning.** Written by or for a client and a designer: [1], [2], [3], [5], [23], [24], as listed in the
  checks above. This is the most common sense in the canon read. Confidence: high.
- **Specification.** Colombi and Nocek's product and graphic design sense: "a set of assumed specifications to be
  respected by an artifact that is expected to be designed" [3]. Figma's design brief gives designers "the detailed
  specifications they need to execute that vision effectively" [16]. Jones and Askland lean this way once: "A
  written design brief will clearly articulate the product requirements to all parties involved in a project." [24].
- **Problem framing, the root of the concept-handoff sense.** Read and Bohemia: "The design brief is an early
  definition of the design problem and the possible descriptions of the strategy to solve it." [2]. Jones and
  Askland call it "essentially a question or definition of a problem" [24]. Their purpose sentence: "It is used to
  help the designer to understand the problem by defining the objectives and parameters of the project toward
  generating the most appropriate solution." [24]. Kuse's brief "defines the problem a design needs to solve, the
  context in which it exists, and the constraints that shape the solution" [6]. In design pedagogy, "a design brief
  is the description of a contextualized issue to be addressed" [3]. The Design Council places it at Define's
  close: "The result is to create a design brief which clearly defines the challenge based on these insights." [22].
- **Solution.** Heap: "The goal of a Design Brief is to describe, holistically and at a high level, your proposed
  design solution(s)" [7]. Its order: "After you’ve written the Problem Brief, use a Design Brief to outline and
  discuss your proposed solution." [7].

**Further variants sit beside the four, mostly on the commissioning side.** Read and Bohemia separate a
"‘creative brief’" from the "‘design brief’" developed after the commission [2]. Visser excludes "design
proposals, which are a document written by the designer explaining the process, timeframe, budget and deliverables
of the project" [1]. Jones and Askland describe a pre-project, a project and a post-project brief [24]. **The
concept-handoff sense this bundle builds is the problem-framing root plus a chosen concept and a handoff.** No source confines a brief to
those three parts, as the spec says (`:6596-6601`). The composition is the library's POSITION. Confidence: high.

**Who writes it varies by sense.** The commissioning party writes it [1]. Read and Bohemia say "the design or
project manager usually writes the design brief in close consultation with the client and the design team" [2]. A
designer develops it "in consultation with a client" [23]. uxmagic.ai gives it to the "Design lead" [21]. Jones and
Askland: "it can be generated by the designer, by the client or as a shared and agreed document between both
parties" [24]. **No Quotable line names a product manager as the author.** Kaninsky names product managers among the people the brief
aligns [9]. The example's author, a product manager (`:6914-6917`), is therefore the library's choice. Confidence:
medium.

**When it is written.** At Define's close, per the Design Council [22], after a sign-off of the concept at most
companies studied [14]. The Design Commission for Wales asks for the needs first: "Before drafting the project
brief, it is important to spend sufficient time clearly defining the needs that the project must satisfy" [5].
Kaninsky's kickoff brief comes earlier, "before any research and design activities even start" [9]. **Teams often
write none.** Visser: "in many of the interviews the projects discussed started without a design brief" [1].

**It changes while the work runs.** Visser: "design briefs are seldom fixed, static documents, but rather, they are
often dynamic and evolve as the project progresses" [1]. Read and Bohemia: "most of the research expresses clearly
that design briefs should not ever be set in stone and should always be able to adapt to suit each audience, as long
as there are mechanisms in place to keep all parties updated and involved in the changes" [2]. Wikipedia: "They
usually change over time and are adjusted as the project scope evolves." [23]. The Design Commission for Wales:
"Complex projects rarely have all aspects of the brief fully defined at inception." [5]. Jones and Askland's
validation-tool line [24] makes five. **This supports the contract's cadence exception** (`discovery-docs.md:77-83`)
at high confidence. **No source says when a brief is finished.** The bound, that it ends when the handed-off design
work is done, is the library's.

### 2. Altitude: a problem only, a concept, or a worked solution

**The sources split three ways, and the library's design brief sits between two of them.** Confidence: high that
they split; the library's altitude is its POSITION.

- **Camp A, no solution in the brief.** GANSW: "Focus on desired outcomes, but don't prescribe a solution." [18].
  Ignitec: "Say what and why, but not how" [17]. Y Combinator: "If you force a solution you risk creating a product
  that doesn't solve your problem - and maybe solves no problem at all." [8]. Kuse's second heading reads "2. Define
  the Problem-Not the Solution" [6]. **This is the stance ADR 0068 held and ADR 0077 superseded.** Against these
  sources, a brief that names a chosen concept is the library's POSITION.
- **Camp B, the brief as specification.** Figma's brief "builds on this foundation with specific technical and
  visual requirements" [16]. It may include "Brand guidelines like color palettes, fonts, and logos" and "Specific
  dimensions and file formats" [16].
- **Camp C, a worked solution.** Shape Up's pitch must carry one: "A problem without a solution is unshaped work."
  [10]. Shaped work is rough but "the overall solution is spelled out" [12]. Heap's brief outlines "your proposed
  solution" [7].

**Ignitec's line falls on both sides of ADR 0077's.** It forbids the how, as the library does. But "A good brief
should say what the solution needs to do, but not how it needs to do it." [17]. ADR 0077 puts `what it must do` on
the specification side (`0077-define-ends-with-a-chosen-concept.md:139-140`). So Ignitec's brief carries content
this bundle excludes, while excluding the concept this bundle carries. Confidence: medium, on this log's reading.

**What Shape Up calls a concept is a specification by ADR 0077's line.** "The shaped concept is an interaction
design viewed from the user's perspective. It defines what the feature does, how it works, and where it fits into
existing flows." [12]. That supports the altitude half of the spec's pitch line (`:6705-6708`) more strongly than
the spec knew. It also shows that the word concept is not shared vocabulary. The template must say what it means by
the word. Confidence: high.

**Shape Up and the library agree on one thing: no wireframes.** "We need more concreteness, but we don't want to
over-specify the design with wireframes or high-fidelity mocks. They'll box in the designers who do the work later."
[10]. Singer's own anecdote makes the same point about a wireframe handed to a designer [12].

**Failure runs in both directions.** Visser: "design briefs could be too broad as well as too narrow" [1]. Shape
Up describes the too-broad case: "You're solving a problem with no context. You have to be a mind reader." [12].
The too-narrow case is the specification creep that ADR 0077 bars.

**One concept or several.** The Eleven Lessons report says "At most of the companies we visited, the Define stage
would end with final sign-off of the concept and approval of work to begin on design and development." [14]. The
same report's Develop stage carries "the development of one or more concepts that have addressed the initial
problem" [14], [15]. The contract's define rule says `at most, on one concept chosen for design`
(`docs/internal/contracts/discovery-docs.md:7-8`). **The singular is the library's reading of the narrative
sentence, not the report's rule.** Read in the stored excerpt and not a Quotable line, the report's Define section
also has ideas for solutions pitched and prototyped. Confidence: medium.

### 3. What published briefs contain

**Six sources give a section list.** Two are literal templates: Heap [7] and Kaninsky [9]. Shape Up's pitch [10]
names five ingredients. Kuse [6] is a guide whose numbered steps act as headings. Y Combinator [8] and Eleken [11]
are question lists. Their headings, as Quotable lines:

| Source | Headings or questions |
|---|---|
| Heap [7] | "Foundations" (with "Behaviors:", "Assumptions:", "Key Constraints:", "Discarded Alternatives:"), "References", "Noteworthy Trade-Offs", "High-Level User Journey(s)", "Surfaces Affected", "Edge Cases & Idiosyncrasies", "Not Doing", "Open Questions" |
| Kaninsky [9] | "Background", "Objective", "Key results & Success criteria", "Target audience", "Data", "The team and stakeholder map", "Scope", "Dependencies", "Risks", "Deliverables", "Timings", "Ways of working", "Budget [if relevant]", "Additional notes" |
| Shape Up pitch [10] | Problem, Appetite, Solution, Rabbit holes, No-gos, each defined in its own line |
| Kuse [6] | "1. Establish Context Before Asking for Design" through "7. Define Stakeholders, Feedback Flow, and Decision Ownership" |
| Y Combinator [8] | "About Use Case", "About Market", "About Company", "About Engagement with Designer" |
| Eleken [11] | Seven numbered questions, ending "7. What are the project timeline and budget?" |

**What recurs.** These counts are this log's, across the six.

- **Something about scope or what is left out**, in five: Heap's "Not Doing" [7], Kaninsky's "What's not in scope"
  [9], Shape Up's no-gos [10], Kuse's "5. Set Scope and Boundaries Explicitly" [6], and Eleken's deliverables
  question [11]. Figr [29] and UXPin [31] add the same question outside these six.
- **The users**, in five: Kaninsky [9], Kuse's fourth heading [6], Y Combinator's use case [8], Eleken's third
  question [11], and Heap's user journeys [7], which sit at solution level.
- **Constraints**, in four: Heap's "Key Constraints:" [7], Kuse's "6. Surface Constraints Early and Honestly" [6],
  Kaninsky's limits the design team "should not challenge" [9], and Shape Up's appetite [10].
- **References**, in two of the six: Heap [7] and Eleken's "6. Do you have references?" [11].
- **Open questions**, in one: Heap [7].
- **A named approver**, in one template: Kaninsky's "Who is the ultimate decision-maker (sign-off)?" [9]. Kuse's
  guide asks "Who approves final designs" [6]. Heap's approval happens in a review outside the document [7].
- **No template carries both an approver field and an open-questions section.** The bundle's full size combines
  two sources' elements. Confidence: medium; the structure dimension found six lists.

**Every budget in these sources is a project's.** Kaninsky asks "What is your budget for this?" [9]. Eleken asks
for "the project timeline and budget" and says "Determine your project budget in advance." [11]. No source
scopes money to the design work alone. Confidence: medium. The search was capable of a negative result, but it read
few templates.

### 4. Boundaries and the chain

**Problem statement.** Only Heap pairs the two documents: "The Problem Brief describes the problem to be solved and
the reasons to prioritize it" [7], and the design brief follows it [7]. No other source times the handoff from
problem framing into a design brief. The spec's chain position (`:6678-6697`) stays a POSITION with one source.

**Creative brief.** Every source that orders the two puts the creative brief first. Figma: "In many design
workflows, the creative brief informs the design brief, ensuring visual decisions support broader project goals."
[16]. Figma's creative brief comes first because "A creative brief sets the strategic foundation for your
project." [16]. Read and Bohemia call an "initial request" a "‘creative brief’", and the design brief "a further
response to the client’s initial brief" [2]. Kuse has a section headed "Design Brief vs. Creative Brief" [6]. Confidence: high.

**Specification and PRD.** Ignitec: "The commercial considerations will come later when you write your product
design specification." [17]. Wikipedia lists "Product design specification , a document that describes design
specifications" as a separate entry [23]. UXPin: "A design brief outlines what designers must create, while the
specifications define specific details" [31]. uxmagic.ai treats the PRD as "the more detailed document that follows
once the idea is approved" [21], though it says this of a pitch or PR/FAQ. **One named team skips the PRD.** At
Heap, once the review clears, "the design brief allows engineers to start scoping and building at least the back
end." [7]. The spec's PRD handover (`:6814`) stays the library's POSITION. Confidence: medium.

**The Shape Up pitch: the act half of the line is weaker than the spec states.** The spec says a pitch exists for
the bet and a design brief does not commit it (`:6709-6712`). Shape Up confirms the pitch's side: comments come
"Not to say yes or no - that happens at the betting table" [10]. But Heap's design brief also feeds a go or no-go
review. Its reviews let the team "make critical decisions about project work (including and especially whether to
proceed)" [7]. **On this log's reading, the line holds only on timing.** Heap's brief precedes the approval to
proceed. The library's brief follows the concept's sign-off, as the Eleven Lessons report places it [14]. That
timing is the library's POSITION. Confidence: medium.

**Recording approval is not authorizing the project.** The Eleven Lessons report says the sign-off gave "the
corporate and financial backing to the development of one or more concepts" [14]. That backing is the investment
decision the define rule excludes (`discovery-docs.md:113`). ADR 0077's table permits a define document to say
`that design work may begin` (`0077-define-ends-with-a-chosen-concept.md:137`). So The Handoff may record that
design was approved, by whom and when. It may not be the record that grants the backing. This is the library's
reading. Confidence: medium.

**Design Sprint.** GV's own page describes "a five-day process" [25] and names no separately published Sprint
Brief, which the repository's earlier evidence file also records. ADR 0035 and the spec (`:6764-6766`) speak of
Google Ventures' Sprint Brief. On this log's evidence, that bullet should rest on ADR 0035 and pm-skills'
pre-sprint tool, not on GV's own page.

**Opportunity solution tree.** Torres's page never mentions a brief [26]. No ordering claim is possible.

**Project brief.** The Design Commission for Wales calls its document a project brief [5]. Kaninsky's UX project
brief is written "before any research and design activities even start" [9], which is `project-brief`'s timing, not
this bundle's. The spec already treats it as a neighbour (`:6585`).

**Business case and product vision.** No source read orders the design brief against either. The spec's low and
medium-low ratings stand (`:6694-6697`, `:6751-6753`).

### 5. The software-audience check (ADR 0080)

**The type passes, on Heap alone, by name.** Heap, a software product-analytics company, describes its own
practice: "Two documents are central to our approach: the Problem Brief and the Design Brief." [7]. ADR 0080
already rules that this passes alone (`docs/internal/decisions/0080-admission-gains-a-software-audience-check.md:197-199`).
Confidence: high.

**What the build adds, source by source:**

- **Kaninsky [9]**, a UX practitioner's template under a near name, written to "get designers, product managers and
  software engineers on the same page". It shows a software audience. Its sense is a kickoff brief, a neighbour.
  Its origin is a UX team outside software: "We developed the initial version of it while I was a UX designer at
  Which?, the UK consumer association." [9]. Confidence: medium-high on audience.
- **Y Combinator [8]**, a design-brief tool under the name, addressed to startup founders. It is advice to an
  audience, not a team's own practice. Confidence: medium.
- **Vendors writing for product and UX teams**: Kuse [6], Figr [29], UXPin [31] and uxmagic.ai [21]. They show the
  term in product tooling's vocabulary, not a team using it.
- **Same job, another name.** Basecamp's pitch [10], [12], [13] does a neighbouring job at a software company; this
  library treats it as a separate type. Atlassian's project poster [19] is a living kickoff document: "project
  posters are living documents" [19]. Its quoted lines point at a project plan, "This section is where your project
  plan will come into focus." [19]. On this log's reading, that is nearer `project-brief`'s job. Confidence: medium.
- **A negative.** Intercom's design team describes its process with no brief-shaped kickoff document [20]. Its two
  Quotable lines show only the page's iterative stance; the absence is the practice dimension's reading of the
  whole page.

**The practice dimension itself found no name match.** The name matches came from the structure and boundaries
dimensions. No named team beyond Heap was found writing a document it calls a design brief. ADR 0080's
name-versus-job question (`0080-...:134-145`) is not tested here, because Heap passes by name.

### 6. The gap question: candidates, routed under decision procedure 12

The gap dimension returns **candidates, never obligations**. Each is routed under decision procedure 12
(`docs/internal/decision-procedures.md:207-241`). E1 means a named source publishes briefs carrying the element. E2
means the library argues it with a falsifier. E3 names its home, and E4 fits it to lean or to full. A quality
property stops at step 1 and becomes a guide rubric row. **This log admits no element.**

1. **Success criteria. Supported, and already homed.** E1: Kaninsky's "Key results & Success criteria" [9],
   Kuse's "3. Clarify Goals and Success Metrics" [6], Canny's "success factors" [30]. The gap dimension's Asana,
   Figr and UXPin lines are not Quotable, so that leg is unsupported. E3: `problem-statement`'s full size carries
   the measures (`tier2-specs.md:6736-6737`), and ADR 0077 lets a define document say `how success will be judged`.
   **Route:** an ASK in The Challenge that points to those measures, or states them in one line where no statement
   exists, plus a rubric row. No new section.
2. **Decision rights and the approval path. Supported; homed in The Handoff.** E1: Kaninsky's sign-off question [9];
   Kuse's "Who approves final designs" and "How conflicts will be resolved" [6]; Figr's "Approval path: Who decides
   when feedback conflicts" [29]; UXPin's RACI model [31]; Canny's "lead point of contact" [30]. **Route:** an ASK
   in The Handoff on who decides when feedback on the design conflicts, plus a rubric row. A RACI table fails E4 for
   lean. Canny's weighted criteria for awarding an agency [30] belong to the commissioning sense and stay out.
3. **Tone and voice. Unsupported for a design brief.** The only Quotable support is Asana's guide [28], which is
   about creative briefs. Design Pickle's tone section is not a Quotable line. **Route:** out. The guide's
   creative-brief row already routes it.
4. **References and inspiration. Supported in name; fails E3 at this altitude.** E1: Heap's "References" [7],
   Eleken's "6. Do you have references?" [11], and Design Pickle's instruction to "Specify whether these should be
   replicated exactly or just used as inspiration." [32]. Design Pickle's example points at layout, colour scheme
   and typography [32], which Figma [16] and UXPin [31] place in a specification. **Route:** no element. A TRAP or
   rubric row says a reference may illustrate the kind of answer and never prescribe how it looks. The maintainer
   may prefer one guidance line in The Chosen Concept.
5. **Accessibility. Contested.** Design Pickle puts a compliance line in the brief [32]. UXPin lists "accessibility
   requirements" among a specification's details [31]. **Route:** guidance in Constraints on the Design (full): name
   an accessibility obligation as a limit, and leave its criteria to the PRD or a specification. No element.
6. **A design time line distinct from the project's. Partly supported; already homed.** E1 for the time line: UXPin's
   "Design handoff date" milestone [31] and Y Combinator's "1. When do you need the design?" [8]. No source gives the
   handoff its own budget. **Route:** supports the full-only Scope, Time Line and Budget section's time half, and
   the lean Handoff's record of when design was approved. No new element.
7. **Risks and dependencies. The gap dimension's null result is wrong.** E1, thin: Kaninsky's "Dependencies" and
   "Risks" [9], in a kickoff brief; Shape Up's rabbit holes [10], in a pitch. E3: project risks belong to
   `project-brief` and `risk-register`; unknowns that block design belong to Open Questions for Design. **Route:** an
   ASK in Open Questions for Design (full) on what could block the design work. No section.
8. **Assumptions. The gap dimension's null result is wrong.** E1: Heap's "Assumptions:" [7]. It supports the
   spec's existing clause, `what is assumed until they do`, in Open Questions for Design (`:6813`). No new element.

Candidates the structure and boundaries dimensions surfaced, routed the same way:

9. **What the concept leaves out. Strongly supported; already homed** in The Chosen Concept. E1: Heap's "Not Doing",
   "What's not in the solution that could be, and why?" [7]; Shape Up's no-gos [10] and "Lastly, shaped work
   indicates what not to do. It tells the team where to stop." [12]; Kaninsky [9]; Figr [29]; UXPin [31].
10. **The alternatives considered. Supported; already homed** in The Chosen Concept's candidates list. E1: Heap's
    "Discarded Alternatives:" and "To the extent they're useful for context, what alternate solutions did we
    consider but eliminate? Why?" [7]; Figr's "Decision history: What the team already tried, rejected, or deferred"
    [29]. Heap's alternatives are solutions, so the altitude caveat in Finding 7 applies.
11. **A self-check for ambiguity. A quality property.** Figr: "What phrase in this brief could two smart people
    interpret differently?" and "What constraint are we assuming someone else knows?" [29]. **Route:** rubric rows
    only, at step 1.
12. **Kinds of design limit. Supported; homed in Constraints on the Design.** E1: Kaninsky's "Describe what the
    design team should not challenge (e.g. hard technical constraints, change of CMS, major design overhauls during
    a platform migration project, etc.)" [9]. **Route:** the section's ASK.
13. **The design work's deliverables. Supported, at project scope.** E1: Kaninsky's "Deliverables" [9] and
    Eleken's "2. What tasks should the design solve? Describe the key deliverables." [11]. **Route:** an ASK in the
    full-only Scope, Time Line and Budget section, at the level of the kind of output. Naming screens or flows stays
    out (`:6819-6822`).
14. **How feedback runs while design proceeds. Supported, and ambiguous.** E1: Kuse's "Who provides feedback" and
    "When reviews happen" [6]; Figr's "Review pattern: Revision limits, feedback rounds, and approval owner" [29];
    UXPin's "Stakeholder feedback sessions" [31]. Canny's review is of the brief itself before it goes out: "Ensure
    that the design brief reaches the key decision-makers and individuals who can provide valuable insights and
    feedback" [30]. **Route:** guidance in The Handoff's clause on keeping the brief current, which must say which
    review it means.
15. **Solution detail. Out at any size.** Heap's "Behaviors:", "High-Level User Journey(s)", "Surfaces Affected",
    "Edge Cases & Idiosyncrasies" and "Noteworthy Trade-Offs" [7], and Shape Up's rabbit holes [10]. **Route:**
    TRAP rows, under the spec's list of what stays out (`:6819-6822`).

### 7. The seven proposed sections, against this research

The spec's section table (`docs/internal/tier2-specs.md:6807-6815`) binds; the maintainer ruled the sections and
sizes. The table records which sources now support each section and whether confidence moves. **Every movement is a
candidate for the maintainer; none is applied here.**

| Section | Size | Spec | Support in this log | Movement |
|---|---|---|---|---|
| **The Challenge** | lean | High | [22] "clearly defines the challenge"; [2] "an early definition of the design problem"; [24] "essentially a question or definition of a problem" and "to help the designer to understand the problem"; [6] "defines the problem a design needs to solve, the context in which it exists"; [8] "Good design briefs provide a clear context for a product."; [9] "Background", "Objective"; [5] on defining needs first | **Holds at high.** All three of the spec's spans for this row are now Quotable lines [6], [22], [24]. Success criteria enter by pointer (gap candidate 1) |
| **Who It Is For and What We Learned** | lean | Medium-high | [22] "understanding how user needs and the problem align" and "based on these insights"; [8] "Have you done any user observations?"; [9] "Target audience", "Data", "Prior UX experiences"; [6] "4. Describe Users and Real Use Contexts"; [11] "3. What is your target audience?" | **Holds.** The spec's Kuse span, "target users" [6], is now quotable, but it sits in a sample AI prompt; Kuse's fourth heading is the better citation. Kaninsky's fields sit in a brief written before research, so they support the users half more than the learnings half |
| **The Chosen Concept** | lean | Medium on the concept; low on the candidates list | Concept: [14] "final sign-off of the concept"; [7] "holistically and at a high level, your proposed design solution(s)". Candidates: [7] "Discarded Alternatives:"; [29] "Decision history". Leaves out: [7], [9], [10], [12], [29], [31]. Against naming any solution: [6], [8], [17], [18] | **Candidates list: low to medium-low.** The spec's `No source publishes a candidates list as a brief section` (`:6811`) is overturned by Heap's template [7], though Heap weighs solutions. **Leaves out: up to medium-high.** **Concept: holds at medium**, a POSITION against camp A. Heap's goal sentence, now quotable, supports the high-level altitude but names a solution, not a concept [7] |
| **Constraints on the Design** | full | Low | [6] "the constraints that shape the solution" and "6. Surface Constraints Early and Honestly"; [7] "the constraints within which it exists" and "Key Constraints:"; [9] its list of what the design team should not challenge; [3] "objectives, requirements, and constraints"; [10] the appetite; [29] its constraint question | **Low to medium.** The spec's Kuse and Heap spans are now Quotable lines [6], [7], and Heap's constrains a solution. Kaninsky's list names kinds of limit, which the spec said rested on an unread source (`:6812`). Distinctness from `project-brief` is still the library's reading |
| **Open Questions for Design** | full | Medium-low | [7] "Open Questions" and "This is a very early version of your design! All sorts of things are up in the air, or under debate. Capture them here."; [7] "Assumptions:" | **Medium-low to medium.** Heap's heading is now raw-checked, which retires the spec's caveat (`:6813`). It is still one source, at solution altitude |
| **The Handoff** | lean | Medium | Who designs: [9] "to get designers, product managers and software engineers on the same page". Approval: [9] its sign-off question, [14], [7], [6], [29], [31]. Kept current: [1], [2], [5], [23], [24]. What follows: [21], [17], [23], [7] | **Holds at medium, better sourced on approval and revision.** It loses Phillips's sentence. The PRD handover stays POSITION, because Heap's brief goes straight to engineering [7]. It records approval of design and never grants backing (Finding 4) |
| **The Handoff's Scope, Time Line and Budget** | full | Low | Time: [10] "Appetite - How much time we want to spend and how that constrains the solution"; [31] "Design handoff date"; [8] "1. When do you need the design?". Scope: [6] its fifth heading; [9] its scope fields; [11] its deliverables question. Budget: none at design scope; [9] and [11] are project budgets | **Time half: low to medium-low. Budget half: stays low, a POSITION.** The spec's `No source scopes a time line or a budget to the handoff alone` (`:6815`) holds for money and weakens for time. Whether Shape Up's appetite covers design alone is not in a Quotable line |

**Two findings bear on the ruled section set without overturning it.** Neither changes it.

- **Open Questions sits in Heap's core template** [7], beside its constraints and alternatives. That argues for
  lean placement, against the ruling of full. The evidence is one source at solution altitude. Confidence: low.
- **What the concept leaves out is the best-sourced element in the set** (gap candidate 9). The bundle carries it
  inside The Chosen Concept, in lean, which matches the evidence. No change is needed.

**Nothing argues for a new section.** Every candidate that clears E1 at concept altitude already has a home in the
seven, and the rest fail E3 or are quality properties.

### 8. Spec sentences this research weakens

These are candidates for a dated note in the spec, not a silent rewrite. Each is maintainer-vetoable.

- `:6811`, that no source publishes a candidates list as a brief section. Heap's template does [7].
- `:6812`, that the kinds of limit rest on an unread source. Kaninsky names kinds [9].
- `:6813`, that Heap's Open Questions rests on an unchecked reading. It is now a Quotable line [7].
- `:6815`, that no source scopes a time line to the handoff. Two partly do [8], [31].
- `:6879-6880`, risk 3's reason, that Heap's section names are unchecked. Its conclusion, that Heap is a sense
  collision, stands and is strengthened by the now-quotable goal sentence [7].
- `:6582`, Kuse's list of contents, which is a sample AI prompt. Also `:6579`, whose no-single-format wording Jones
  and Askland report from Phillips, though they share the observation.
- `:6709-6712`, the act half of the pitch line, which Heap's go or no-go review weakens [7].
- `:6764-6766`, the Sprint Brief bullet, as far as it relies on GV's own page [25].

---

## Claims flagged contested or time-bound

1. **What the term design brief means.** Commissioning [1], [5], [23]; specification [3], [16]; problem framing
   [2], [22], [24]; solution [7]. "There is no clear or univocal definition in the literature." [3].
2. **Altitude.** No solution [6], [8], [17], [18]; a specification [16]; a worked solution [7], [10], [12]. The
   library's concept sits between, as a POSITION.
3. **Who writes it.** The commissioning party [1]; the design or project manager [2]; a designer [23]; a design
   lead [21]. No source names a product manager.
4. **Fixed or living.** Every source that addresses it says living [1], [2], [5], [23], [24]. The point of finish is
   unsourced.
5. **One concept or several** at Define's close [14], [15].
6. **Whether the brief precedes or follows approval to proceed.** Heap's precedes its review [7]; the Eleven Lessons
   sign-off precedes design work [14].
7. **Whether accessibility belongs in the brief or the specification** [32], [31].
8. **What a feedback round is.** A review of the brief before it goes out [30], or of the design during the work
   [29], [31].
9. **Whether a same-job document counts for ADR 0080.** Atlassian [19] and Basecamp [10]; unresolved, and not
   needed here.
10. **Whether Heap is a structural source or a sense collision.** Its pairing reads as concept handoff; its sections
    reach into how the solution works, and its goal names "your proposed design solution(s)" [7]. The spec treats it
    as a collision (`:6879-6880`), and the goal sentence supports that reading.
11. **Whether a brief should list candidates at all.** Heap does [7]; Kuse's second heading argues the brief should
    leave solutions to the designer [6].
12. **Time-bound facts.** The Eleven Lessons report is from 2007 [14], and the archived page from 2010 [15]. Jones
    and Askland and Read and Bohemia are from 2012 [24], [2], and GANSW's note is V2 of 2018 [18]. Visser is from
    2023 [1], Colombi and Nocek from 2024 [3], and the Design Commission for Wales from 2025 [5]. Y Combinator's post
    is dated 2016 in its raw text [8]. The Design Council's history page [22], Wikipedia [23] and every vendor page
    are living pages.

---

## Honest framing

**What the bundle exists to say.** In this bundle's sense, a design brief is a short document. It hands a chosen
problem and one chosen concept to the people who will design it, before anyone specifies how the concept works.
Parts of that are sourced. A brief is Define's output [22], and at most companies studied, Define ends with a
concept signed off [14]. It frames a design problem [2], [24]. It is revised as the work runs [1], [2], [5], [23].
It is a different document from a specification [17], [23], [31]. **The whole is the library's composition.** No
source confines a brief to a challenge, a chosen concept and a handoff. Some sources forbid naming any solution
[8], [17], [18]; others demand a worked one [10], [12].

**What the bundle must not claim:**

- **That a design brief improves design or product outcomes.** No source in this log measured it.
- **That the narrow concept-handoff shape is received practice.** It is a POSITION.
- **That the commissioning sense is a misuse.** It is the canon's commonest sense [1], [5], [23].
- **That teams always write one.** Many projects start without one [1], and one named team describes none [20].
- **That Shape Up supports a solution-free brief.** "A problem without a solution is unshaped work." [10] describes
  the pitch, the rung above this brief.
- **That the Design Council requires exactly one concept** [14].
- **That a design brief authorizes a project or its budget.** It records that design may begin.
- **That the PRD always follows a design brief.** Heap's goes to engineering [7].
- **Anything quoted from Phillips [4] or Dilanchian [27]**, or Kuse's list of contents as Kuse's own account. Jones
  and Askland's no-single-format wording is their report of Phillips's view, not their own result.
- **That GV publishes a Sprint Brief on its own page** [25].
- **That experience brief is an alias**, or anything from Nordin's article.

---

## Notes for the companion

**The load-bearing sections.** Four of the skeleton's eleven (`templates/methodology.md:172-182`) carry this
bundle. **Origins** must teach the senses straight, with the canon's own admission that none is settled [3].
**Debates** must name the three altitude camps (Finding 2) and say where the library stands, as a POSITION.
**Relationships** must carry the chain, the creative-brief order [16], the specification boundary [17], [23], [31]
and the pitch line (Finding 4). **Anatomy** must label which parts of The Chosen Concept and The Handoff are
sourced and which are composed.

**The sharpest teaching points:**

1. **Say which sense this is.** The reader may have meant a commissioning brief or a specification [1], [16].
2. **Name the kind of answer, never how it works.** Ignitec's "Say what and why, but not how" [17] is close. But
   Ignitec lets a brief say what the solution must do, which ADR 0077 calls specification (Finding 2).
3. **Say what the concept leaves out.** It is the best-sourced element here [7], [9], [10], [12].
4. **Record that design was approved, and by whom.** The brief does not grant the backing [14].
5. **Keep everyone informed as the brief changes** [2]. Say which review the team means [29], [30].
6. **Too broad and too narrow both fail** [1], [12].
7. **Many teams skip the document** [1], [20]. The guide's when-not-to-use table can say so.

**Section design.** Finding 7 maps the research onto the seven ruled sections, and Finding 6 routes every gap
candidate under decision procedure 12. Every proposed change there is a candidate, and this log admits none. The
two strongest are guidance changes, not elements. One is an ASK in The Handoff on who settles conflicting feedback.
The other is an ASK in Open Questions for Design on what could block the design work.

**The traps:**

1. **Quoting anything that is not a Quotable line**: the four dropped quotations, or the dimension files' spans
   listed in the checks section. Kuse's contents list [6] and Jones and Askland's no-single-format sentence [24] are
   quotable, but only with the framing given there.
2. **Quoting Phillips or Dilanchian at all**, or Nordin; or making experience brief an alias; or repeating the
   unsourced ADR 0063 phrase (`:6607-6610`).
3. **Turning "A problem without a solution is unshaped work." [10] into support for this brief's altitude.** It
   describes the pitch.
4. **Treating Heap as a concept-sense source.** Its headings and goal are quotable, but its goal names "your
   proposed design solution(s)" and its alternatives are solutions [7]. Label every Heap citation as the solution
   sense.
5. **Presenting camp A as support for naming a concept** [17], [18]. Those sources forbid it; ADR 0077 departs
   from them inside this library.
6. **Importing creative-brief tone** [28], **visual references** [32] or **agency-award criteria** [30] as brief
   elements.
7. **Calling the singular concept the Design Council's rule** [14].
8. **Writing a budget section that holds a project budget** [9], [11].
9. **Claiming a GV Sprint Brief from GV's page** [25], or presenting Atlassian's poster as a design brief [19].
10. **Reusing the worked example's scenario in GOOD and WEAK text**, the risk the spec names (`:6886-6888`). Grep the
    drafted template and guide for Saved Views, Recurring Analyst, Priya Nair, friction study and Team Lead before
    review.

**The example.** The maintainer ruled the scenario on 2026-10-22 (`docs/internal/tier2-specs.md`, "The example:
Saved Views, by the maintainer's ruling"). It is a design brief for Saved Views, the Acme feature the delivery thread
already specifies. Priya Nair, PM, Reporting, writes it. It is dated 2026-06-01: after the 2026-05 Reporting
friction study, and before the Saved Views PRD of 2026-06-12. It hands the Saved Views concept to the people who
will design it, and the PRD later specifies that concept. The `discovery-docs` contract's section 4 binds the same
facts.

- **Facts it may carry, all of them Acme's own and older than the brief.** They come from `prd_example.md` lines
  34-48, 57-61 and 65-68. They include the FY26 Time to Insight goal and the friction study's finding about
  re-filtering. They include the study's illustrative interview counts and the two earlier deferrals. They include
  per-user preferences storage shipping in Q1. They name the Recurring Analyst as the primary user and the Team
  Lead as the secondary user, from `user-persona_example.md`. The PRD's three non-goals become what the concept
  leaves out.
- **What it must not cite or contain.** It cites no document of the Saved Views delivery thread as existing: the
  PRD, epic, user stories, acceptance criteria, design document and test plan are each dated 2026-06-12 or later.
  It says nothing about how the concept works: the PRD's Views control and its menu are the design's output, not
  the brief's input. It cites no prototype as existing. It carries no requirement IDs and no performance targets,
  which are `deliver` content. It names no Reporting Platform Modernization program unless a sibling dates one
  before the brief.
- **Check the siblings' own text, not this note.** Read `prd_example.md`, `user-persona_example.md` and
  `problem-statement_example.md` before writing, and make every carried fact match them exactly.

## Sources

### Canon: what a design brief is for, who writes it, and when

**[1] Steven C. Visser (Purdue University), "Design Briefs from the Real World" (IDSA 2023 Education Paper Submission).** academic. **fetched-and-verified.**
`https://idsa.org/wp-content/uploads/2023/09/Design-Briefs.pdf`
Supports: Design briefs are rarely fixed at handoff and routinely evolve through the project; many real projects proceed with no formal brief at all; the paper also draws a sharp line between a 'design brief' (written by the commissioning party, stating goals and limitations) and a 'design proposal' (written by the designer, covering process/timeframe/budget/deliverables) - the opposite direction of authorship from the bundle's own artifact
Quotable: "design briefs are a document written by the person or organization wanting the design completed"
Quotable: "this paper is not referring to design proposals, which are a document written by the designer explaining the process, timeframe, budget and deliverables of the project"
Quotable: "design briefs could be too broad as well as too narrow"
Quotable: "design briefs are seldom fixed, static documents, but rather, they are often dynamic and evolve as the project progresses"
Quotable: "Design briefs are part of the communication between the client and the designer"
Quotable: "in many of the interviews the projects discussed started without a design brief"

**[2] D. Read and E. Bohemia, "The Functions of the Design Brief" (International Design Conference, Design 2012, Dubrovnik; Design Society).** academic. **fetched-and-verified.**
`https://www.designsociety.org/download-publication/32128/THE+FUNCTIONS+OF+THE+DESIGN+BRIEF`
Supports: The literature uses at least three distinct, sequenced terms the bundle's single 'design brief' label collapses: a client's 'creative brief' (RFP-style initial statement of goals/budget/deadlines), a response 'design brief' the design team develops after the commission (reflecting the team's skills and how it will fulfil the client's objectives), and an in-house cross-functional 'project brief'. All are described as living documents that should adapt as the project proceeds provided parties stay informed of changes
Quotable: "The design brief is an early definition of the design problem and the possible descriptions of the strategy to solve it."
Quotable: "This initial request is often termed a ‘creative brief’ and is usually a creative response to the client’s initial briefing"
Quotable: "Upon receiving the commission or contact, a further ‘design brief’ is often developed and is typically a further response to the client’s initial brief"
Quotable: "the design or project manager usually writes the design brief in close consultation with the client and the design team"
Quotable: "most of the research expresses clearly that design briefs should not ever be set in stone and should always be able to adapt to suit each audience, as long as there are mechanisms in place to keep all parties updated and involved in the changes"

**[3] Chiara Colombi (Politecnico di Milano) and Adam Nocek (Arizona State University), "Design Heresy: The Problem of the Brief", diid disegno industriale industrial design, No. 84 (2024).** academic. **fetched-and-verified.**
`https://re.public.polimi.it/retrieve/7d41d429-57b0-43e0-89a5-930fcedfa09d/colombi_nocek.pdf`
Supports: Surveys materially different senses of 'design brief' across design sub-disciplines: in Product/Graphic Design it functions as a set of specifications the artifact must respect (citing Jones & Askland 2012) - the specification sense; in Design Management it is the output of a negotiation to build mutual understanding between designer and client (citing Paton & Dorst 2011) - the commissioning-agreement sense; in Design Pedagogy/metadesign it is a description of a contextualized issue to be addressed - closest to the bundle's own concept/problem-framing sense
Quotable: "the design brief is commonly intended as a statement whose form may vary from a sentence to a structured document, articulating a project’s objectives, requirements, and constraints"
Quotable: "There is no clear or univocal definition in the literature."
Quotable: "a design brief is referred to as a set of assumed specifications to be respected by an artifact that is expected to be designed (Jones & Askland, 2012; Meron, 2019)"
Quotable: "a project’s brief is the result of a briefing activity as a negotiation of preliminary knowledge and requirements between the designer and the client to build “a mutual understanding of what a project will be about” (Paton & Dorst, 2011, p. 575)"
Quotable: "in Design Pedagogy... a design brief is the description of a contextualized issue to be addressed"

**[4] Peter L. Phillips, "Creating the Perfect Design Brief: How to Manage Design for Strategic Advantage" (Allworth Press with the Design Management Institute, 2004), PDF excerpt.** primary (book). **url-confirmed-not-read.**
`https://www.portal.goodeyes.com/public/browse/Documents/creating_the_perfect_design_brief.pdf`
Supports: Its existence only. It is the genre's main book, named so a reader knows it exists, and nothing in this bundle rests on it. Its body could not be re-read on 2026-10-22: the PDF mirror refuses connections, and the 2026-10-16 sweep checked its sentences only through Open Library's search snippets

**[5] Design Commission for Wales, "Introduction to Brief Writing" (2025).** primary (public body). **fetched-and-verified.**
`https://dcfw.org/wp-content/uploads/2025/08/Introduction-to-brief-writing_ENG_2025.pdf`
Supports: Built-environment corroboration that a brief is the reference document for appointing a consultant team (commissioning sense), and that complex briefs are rarely fully defined at inception
Quotable: "The project brief should be the central reference document used in the appointment of a consultant team."
Quotable: "Complex projects rarely have all aspects of the brief fully defined at inception."
Quotable: "Before drafting the project brief, it is important to spend sufficient time clearly defining the needs that the project must satisfy"

### Structure: the sections published design briefs carry

**[6] Kuse Blog (Kuse Inc.) - 'How to Write a Solid Design Brief: Workflows & Real Examples'.** vendor. **fetched-and-verified.**
`https://www.kuse.ai/blog/tutorials/design-brief`
Supports: Section structure of a discursive (non-fill-in-blank) design-brief guide; its numbered guidance maps to headings rather than a literal template
Quotable: "What Is a Design Brief?"
Quotable: "Why Is a Design Brief Important?"
Quotable: "Design Brief vs. Creative Brief"
Quotable: "How to Write a Successful Design Brief (End-to-End)"
Quotable: "1. Establish Context Before Asking for Design"
Quotable: "2. Define the Problem-Not the Solution"
Quotable: "3. Clarify Goals and Success Metrics"
Quotable: "4. Describe Users and Real Use Contexts"
Quotable: "5. Set Scope and Boundaries Explicitly"
Quotable: "6. Surface Constraints Early and Honestly"
Quotable: "7. Define Stakeholders, Feedback Flow, and Decision Ownership"
Quotable: "Who provides feedback"
Quotable: "Who approves final designs"
Quotable: "How conflicts will be resolved"
Quotable: "When reviews happen"
Quotable: "defines the problem a design needs to solve, the context in which it exists, and the constraints that shape the solution"
Quotable: "including problem statement, goals, target users, constraints, and deliverables"

**[7] Heap (Dave Feldman, design leader), "Save Time and Get Aligned With a Design Brief".** practitioner. **fetched-and-verified.**
`https://heap.io/blog/save-time-and-get-aligned-with-a-design-brief`
Supports: Pairs the Problem Brief with the Design Brief and reviews both with leadership in a named approval gate ("PQ review"); also states what the design brief hands off to once approved; A literal, downloadable design-brief template with verbatim section headings, including a section that records discarded candidate solutions and a dedicated Open Questions section
Quotable: "Two documents are central to our approach: the Problem Brief and the Design Brief. The Problem Brief describes the problem to be solved and the reasons to prioritize it"
Quotable: "After you’ve written the Problem Brief, use a Design Brief to outline and discuss your proposed solution."
Quotable: "At Heap, our next step is a product quality review: the team goes over both Problem and Design Brief with leadership to get input. [...] the “PQ review” ensures we’re making good trade-offs among product quality, project scope, and timeline."
Quotable: "By doing product quality reviews, and by using such a low-fidelity artifact in them, we’re able to make critical decisions about project work (including and especially whether to proceed) at an early enough stage that neither design nor engineering is needlessly wasted."
Quotable: "Once a project clears PQ review, we’re off to the races! The designer starts the design in earnest, and the design brief allows engineers to start scoping and building at least the back end."
Quotable: "Foundations"
Quotable: "Behaviors:"
Quotable: "Assumptions:"
Quotable: "Key Constraints:"
Quotable: "Discarded Alternatives:"
Quotable: "To the extent they're useful for context, what alternate solutions did we consider but eliminate? Why?"
Quotable: "References"
Quotable: "Noteworthy Trade-Offs"
Quotable: "High-Level User Journey(s)"
Quotable: "Surfaces Affected"
Quotable: "Edge Cases & Idiosyncrasies"
Quotable: "Not Doing"
Quotable: "What's not in the solution that could be, and why?"
Quotable: "Open Questions"
Quotable: "This is a very early version of your design! All sorts of things are up in the air, or under debate. Capture them here."
Quotable: "Two documents are central to our approach: the Problem Brief and the Design Brief."
Quotable: "our next step is a product quality review"
Quotable: "The Problem Brief describes the problem to be solved and the reasons to prioritize it"
Quotable: "The goal of a Design Brief is to describe, holistically and at a high level, your proposed design solution(s)"
Quotable: "use a Design Brief to outline and discuss your proposed solution."
Quotable: "It outlines the key details of your solution and the constraints within which it exists."
Quotable: "the team goes over both Problem and Design Brief with leadership to get input."

**[8] Dominika Blackappl (Y Combinator Part-Time Partner), "Practical Design: Design Brief".** practitioner. **fetched-and-verified.**
`https://www.ycombinator.com/blog/practical-design-design-brief`
Supports: Its design-brief questionnaire ends on engaging a designer, placing the brief as the document that precedes, and sets terms for, the designer relationship rather than one that hands off to a PRD or spec; A question-based (not heading-structured in the usual sense) design-brief tool organized into four named blocks; one block scopes engagement/time with a designer, but not design work's own budget separate from a project budget; Startup-practitioner source warning that a design brief which forces a solution risks producing a product that solves nothing; reinforces the problem-not-solution camp with a distinct consequence framing (risk of building the wrong thing, not just a creativity cost)
Quotable: "About Engagement with Designer"
Quotable: "1. When do you need the design?"
Quotable: "2. Preferred form of engagement. (Contract, full-time, etc.)"
Quotable: "About Use Case"
Quotable: "About Market"
Quotable: "About Company"
Quotable: "3. Have you done any user observations? If yes, will you be able to share the process and the findings?"
Quotable: "Good design briefs provide a clear context for a product."
Quotable: "It will guide you toward providing concrete language around your product's context and away from forcing a solution onto a designer or yourself. If you force a solution you risk creating a product that doesn't solve your problem - and maybe solves no problem at all."
Quotable: "Have you done any user observations? If yes, will you be able to share the process and the findings?"
Quotable: "This tool will allow you to create a design brief in less than ten minutes."
Quotable: "Answer the questions below to create a design brief or try the interactive version on my site."

**[9] Matěj Káninský - 'The power of a UX project brief (template included)' (author's own updated blog version).** practitioner. **fetched-and-verified.**
`https://matejkaninsky.com/blog/ux-project-brief-template/`
Supports: A literal UX project-brief template with verbatim section headings, including an explicit sign-off/approver question and a general project Budget section (not scoped to design work alone)
Quotable: "Name of the project"
Quotable: "Background"
Quotable: "Prior UX experiences"
Quotable: "Business proposition and competition"
Quotable: "Objective"
Quotable: "Key results & Success criteria"
Quotable: "Target audience"
Quotable: "Data"
Quotable: "The team and stakeholder map"
Quotable: "Who is the ultimate decision-maker (sign-off)?"
Quotable: "Scope"
Quotable: "What's in scope"
Quotable: "What might be in scope"
Quotable: "What's not in scope"
Quotable: "Describe what the design team should not challenge (e.g. hard technical constraints, change of CMS, major design overhauls during a platform migration project, etc.)"
Quotable: "Dependencies"
Quotable: "Risks"
Quotable: "Deliverables"
Quotable: "Timings"
Quotable: "Ways of working"
Quotable: "Team routines"
Quotable: "Communication"
Quotable: "Design, collaboration and documentation tools"
Quotable: "Shared data"
Quotable: "Budget [if relevant]"
Quotable: "What is your budget for this?"
Quotable: "What does the approval process look like?"
Quotable: "Additional notes"
Quotable: "get designers, product managers and software engineers on the same page before any research and design activities even start"
Quotable: "put your initial assumptions, hard facts, goals, and other relevant information into a written form"
Quotable: "This helps to facilitate meaningful discussions and to get designers, product managers and software engineers on the same page before any research and design activities even start."
Quotable: "We developed the initial version of it while I was a UX designer at Which?, the UK consumer association."

**[10] Basecamp / 37signals, Shape Up, Chapter 6, "Write the Pitch".** primary. **fetched-and-verified.**
`https://basecamp.com/shapeup/1.5-chapter-06`
Supports: Contrasts the pitch's approval mechanism with the design brief's: the pitch itself is not where yes/no happens, and comments on it are explicitly not approval; A fifth 'further template,' published by a software product company's own team, whose five ingredients map closely to candidate-concepts, constraints, and a design-work-only time box distinct from a project budget; Confirms the two already-logged lines verbatim and establishes that a Shape Up pitch deliberately contains a worked (if rough) solution, not merely a direction - while also warning against over-specifying visually
Quotable: "the first step for presenting a pitch is posting the write-up with all the ingredients above somewhere that stakeholders can read it on their own time. This keeps the betting table short and productive."
Quotable: "People comment on the pitch asynchronously. Not to say yes or no - that happens at the betting table - but to poke holes or contribute missing information."
Quotable: "In the next chapter we’ll look at the betting process in more detail to see where pitches go and how we turn them into scheduled projects."
Quotable: "There are five ingredients that we always want to include in a pitch:"
Quotable: "Problem - The raw idea, a use case, or something we've seen that motivates us to work on this"
Quotable: "Appetite - How much time we want to spend and how that constrains the solution"
Quotable: "Solution - The core elements we came up with, presented in a form that's easy for people to immediately understand"
Quotable: "Rabbit holes - Details about the solution worth calling out to avoid problems"
Quotable: "No-gos - Anything specifically excluded from the concept: functionality or use cases we intentionally aren't covering to fit the appetite or make the problem tractable"
Quotable: "It's critical to always present both a problem and a solution together."
Quotable: "You can think of the appetite as another part of the problem definition."
Quotable: "if we only care enough to spend two weeks on this now, how does this specific solution look?"
Quotable: "A problem without a solution is unshaped work."
Quotable: "The purpose of the pitch is to present a good potential bet."
Quotable: "Diving straight into "what to build"-the solution-is dangerous. You don't establish any basis for discussing whether this solution is good or bad without a problem."
Quotable: "That's not ready to pitch or bet on. A problem without a solution is unshaped work."
Quotable: "If the solution isn't there, someone should go back and do the shaping work on the shaping track. It's only ready to bet on when problem, appetite, and solution come together."
Quotable: "We need more concreteness, but we don't want to over-specify the design with wireframes or high-fidelity mocks. They'll box in the designers who do the work later."
Quotable: "Designers should feel free to find a different design than the box divided with a vertical line. We'd add a disclaimer here in the pitch that reminds designers of the latitude they should take."
Quotable: "Rabbit holes"
Quotable: "No-gos"

**[11] Mariia Kasym / Maksym Chervynskyi (Eleken, a product design agency) - 'How to Create a Design Brief: Step-by-Step Guide with Examples'.** vendor. **fetched-and-verified.**
`https://eleken.co/blog-posts/design-brief-example-how-it-should-look-like-and-what-it-should-contain`
Supports: A sixth, weaker-fit 'further template' candidate: it is an agency-client brief (not a software product or UX team's own internal template) and bundles timeline and budget into one undifferentiated question rather than scoping either to design work alone
Quotable: "1. What does your company do?"
Quotable: "2. What tasks should the design solve? Describe the key deliverables."
Quotable: "3. What is your target audience?"
Quotable: "4. Who are the competitors, and what differentiates your product from them?"
Quotable: "5. What copy and images will this project include?"
Quotable: "6. Do you have references?"
Quotable: "7. What are the project timeline and budget?"
Quotable: "Determine your project budget in advance. This way, a designer can optimize the time and resources spent."

### Altitude: a concept, never a specification, and the Shape Up pitch

**[12] Ryan Singer / Basecamp (37signals), "Principles of Shaping" - Shape Up, Chapter 2.** primary. **fetched-and-verified.**
`https://basecamp.com/shapeup/1.1-chapter-02`
Supports: Names the altitude problem directly: wireframes are 'too concrete' (over-specifies, boxes in the designer), words are 'too abstract' (no context, can't make trade-offs). Shaped work is defined by three properties: rough, solved, bounded. The chapter explicitly puts the shaped concept at a middle altitude between a raw idea and a specification
Quotable: "I'll give a wireframe to my designer, and then I'm saying to her: "I know you're looking at this, but that's not what I want you to design. I want you to re-think it!" It's hard to do that when you're giving them this concrete thing."
Quotable: "You're solving a problem with no context. You have to be a mind reader. It's like: "we'll know it when we see it.""
Quotable: "Work in the shaping stage is rough. Everyone can tell by looking at it that it's unfinished. ... Work that's too fine, too early commits everyone to the wrong details."
Quotable: "Despite being rough and unfinished, shaped work has been thought through. All the main elements of the solution are there at the macro level and they connect together. The work isn't specified down to individual tasks, but the overall solution is spelled out."
Quotable: "Lastly, shaped work indicates what not to do. It tells the team where to stop."
Quotable: "The shaped concept is an interaction design viewed from the user's perspective. It defines what the feature does, how it works, and where it fits into existing flows."

**[13] Ryan Singer / Basecamp (37signals), "The Betting Table" - Shape Up, Chapter 8.** primary. **fetched-and-verified.**
`https://basecamp.com/shapeup/2.2-chapter-08`
Supports: Confirms what a pitch is used for at the betting table (a go/no-go decision on a shaped, solution-bearing concept) and that revisiting the shaping track - not writing a spec - is the response when a pitch's solution turns out wrong
Quotable: "The betting table is a meeting held during cool-down where stakeholders decide what to do in the next cycle. The potential bets to consider are either new pitches shaped during the last six weeks ... there's no "grooming" or backlog to organize."
Quotable: "The pitch defines a specific payout that makes the bet worth making."
Quotable: "if a project doesn't finish in the six weeks, it means we did something wrong in the shaping ... the circuit breaker pushes us to reframe the problem. We can use the shaping track on the next six weeks to come up with a new or better solution."

**[14] Design Council, "Eleven lessons: managing design in eleven global brands" (2007).** primary. **fetched-and-verified.**
`https://www.designcouncil.org.uk/fileadmin/uploads/dc/Documents/ElevenLessons_Design_Council%2520%25282%2529.pdf`
Supports: This is the actual 330-page 2007 study (not a secondary summary). Independently verified every quote ADR 0077 attributes to it, directly against the PDF text. It places formal concept sign-off at the end of Define, and states Develop is where 'one or more concepts' get taken forward - a plural that matters against ADR 0077's singular 'a chosen concept'
Quotable: "Key activities during the Define stage are: -- Project development -- Project management -- Project sign-off."
Quotable: "At the Develop stage the project has been taken through a formal sign-off, which has given the corporate and financial backing to the development of one or more concepts that have addressed the initial problem."
Quotable: "The Define stage ends with a clear definition of the problem(s) and a plan for how to address this through a design-led product or service. In practice, the Define stage ends in a project go-ahead through corporate level sign-off."
Quotable: "At most of the companies we visited, the Define stage would end with final sign-off of the concept and approval of work to begin on design and development."

**[15] Design Council, "The design process" (archived 2010 page, drawn from the Eleven Lessons study).** primary. **fetched-and-verified.**
`https://web.archive.org/web/20101008093406/http://www.designcouncil.org.uk/about-design/How-designers-work/The-design-process/`
Supports: The Design Council's own public restatement of the double-diamond stage breakdown from the same study; used here only for the summary list, not as a substitute for the report itself. Note: this page has a content bug - its own 'Define' detail paragraph beneath the summary repeats the 'Discover' paragraph verbatim, so that specific repeated sentence is not usable as a Define-stage quote; only the bulleted 'Key activities' list and the separate Develop-stage sentence are trustworthy here, and both are corroborated word-for-word by the primary PDF above
Quotable: "Define The second quarter of the double diamond model represents the definition stage, in which interpretation and alignment of these needs to business objectives is achieved. Key activities during the Define stage are: Project development Project management Project sign-off."
Quotable: "At the Develop stage the project has been taken through a formal sign-off, which has given the corporate and financial backing to the development of one or more concepts that have addressed the initial problem."

**[16] Figma (FigJam Resource Library), "How to write a creative brief: five steps for designers".** vendor. **fetched-and-verified.**
`https://www.figma.com/resource-library/how-to-write-a-creative-brief/`
Supports: Orders the creative brief before the design brief and contrasts their content: the creative brief sets vision/strategy, the design brief adds technical and visual specification; Explicitly defines 'design brief' (as distinct from 'creative brief') as technical and visual specification - the opposite altitude from ADR 0077's concept-only rule
Quotable: "A design brief, on the other hand, builds on this foundation with specific technical and visual requirements. It translates strategic goals into concrete design parameters for graphic designers, UX/UI designers, and other visual artists working on the project deliverables."
Quotable: "While creative briefs guide the overall project vision, writing a design brief gives designers the detailed specifications they need to execute that vision effectively. In many design workflows, the creative brief informs the design brief, ensuring visual decisions support broader project goals."
Quotable: "A design brief might include: Brand guidelines like color palettes, fonts, and logos"
Quotable: "Additional visual direction and mood boards"
Quotable: "Packaging designs"
Quotable: "Examples and mood boards"
Quotable: "Specific dimensions and file formats"
Quotable: "Other technical specifications and requirements."
Quotable: "While creative briefs guide the overall project vision, writing a design brief gives designers the detailed specifications they need to execute that vision effectively."
Quotable: "A design brief, on the other hand, builds on this foundation with specific technical and visual requirements."
Quotable: "It translates strategic goals into concrete design parameters for graphic designers, UX/UI designers, and other visual artists working on the project deliverables."
Quotable: "A creative brief sets the strategic foundation for your project."
Quotable: "In many design workflows, the creative brief informs the design brief, ensuring visual decisions support broader project goals."

**[17] Ben Mazur / Ignitec, "How to write an effective product design brief".** vendor. **fetched-and-verified.**
`https://ignitec.com/insights/how-to-write-an-effective-product-design-brief/`
Supports: A product-design-agency practitioner source that states the concept-versus-specification line explicitly and names the specification as a distinct, later document - the cleanest verbatim boundary line found in this research
Quotable: "Outline the problems to be solved but do not prescribe outcomes. Prescribing outcomes i.e. dictating specific features early on can be very limiting to creativity and prevent better solutions being found through research and ideation later."
Quotable: "The commercial considerations will come later when you write your product design specification."
Quotable: "Say what and why, but not how"
Quotable: "A good brief should say what the solution needs to do, but not how it needs to do it. It is important not to constrain the outcome or dictate too early what the product features need to be before sufficient research has been conducted."
Quotable: "The brief is a top level design document. It is meant to be open to interpretation and by definition, it is meant to be brief."

**[18] Government Architect New South Wales (GANSW), "How to develop a design brief" advisory note, V2, 12/09/2018.** standards. **fetched-and-verified.**
`https://www.planning.nsw.gov.au/sites/default/files/2023-10/how-to-develop-a-design-brief-advisory-note.pdf`
Supports: A government design-procurement standard stating plainly that a design brief must describe requirements and desired outcomes without prescribing the solution
Quotable: "As you are developing your brief, focus on describing your requirements without pre-empting a design solution. You will get better value if the brief is open to others' approaches and solutions - these may not be apparent when a project is conceived."
Quotable: "Focus on desired outcomes, but don't prescribe a solution."
Quotable: "Balance specific deliverables with opportunities for innovation."

### Practice: software product and UX teams that write design briefs

**[19] Atlassian Team Playbook - "Project Poster" play.** practitioner. **fetched-and-verified.**
`https://www.atlassian.com/team-playbook/plays/project-poster`
Supports: A named technology company (Atlassian) publishes a standing kickoff-document practice that does the same job as a design/UX brief - framing a problem before build work starts - even though the house name is 'poster,' not 'brief'
Quotable: "project posters are living documents"
Quotable: "This section is where your project plan will come into focus."
Quotable: "Project posters are best when you're solving complex problems or seizing an opportunity with a lot of unknowns."

**[20] Paul Adams (Intercom) - "How we design at Intercom".** practitioner. **fetched-and-verified.**
`https://www.intercom.com/blog/how-we-design-at-intercom/`
Supports: A named software product team (Intercom's design team) describes its end-to-end design process in detail and explicitly does NOT describe a discrete brief-style kickoff document; this is evidence of absence at a named, real team, not merely an unconfirmed guess
Quotable: "We're continually iterating this process, figuring out ways in which we can design better things faster."
Quotable: "Don't stop when something ships."

### Boundaries: the documents before and after a design brief

**[21] uxmagic.ai, "What is a PRD?".** vendor. **fetched-and-verified.**
`https://uxmagic.ai/blog/what-is-a-prd`
Supports: Puts the PRD, the technical spec/design doc, and the design brief side by side in one comparison table, and states explicitly that the PRD is the document that follows a pitch or PR/FAQ once an idea is approved
Quotable: "Technical spec / design doc How will engineering build it? Engineering lead System or component Build and maintenance"
Quotable: "Design brief How should it look and feel? Design lead Screen or flow One design task"
Quotable: "Amazon's "working backwards" PR/FAQ, a mock press release plus FAQ, is written earlier to test whether an idea is worth pursuing. Basecamp's Shape Up "pitch" is a shaped, time-boxed version of the same thinking. If your team already uses one of these, treat the PRD as the more detailed document that follows once the idea is approved."
Quotable: "A PRD, or product requirements document, is a written description of what a product or feature must do, for whom, and why, along with how success will be measured. It is written before building starts"
Quotable: "Leave the architecture itself to the engineering design doc."
Quotable: "the first PRD for a new product is usually the MVP's scope"
Quotable: "How should it look and feel?"
Quotable: "Screen or flow"
Quotable: "One design task"

**[22] Design Council, "History of the Double Diamond".** primary. **fetched-and-verified.**
`https://www.designcouncil.org.uk/our-resources/the-double-diamond/history-of-the-double-diamond/`
Supports: Places the design brief at the hinge between Define and Develop: it is the named output that closes Define and opens the Develop phase
Quotable: "The second phase is to make sense of the findings, understanding how user needs and the problem align. The result is to create a design brief which clearly defines the challenge based on these insights."
Quotable: "The result is to create a design brief which clearly defines the challenge based on these insights."

**[23] Wikipedia contributors, "Design brief".** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Design_brief`
Supports: Names the product design specification as a distinct, related-but-separate document in its See-also list, corroborating that the specification is a different artifact than the brief rather than a later section of it
Quotable: "A design brief is a document for a design project developed by a designer in consultation with a client."
Quotable: "They usually change over time and are adjusted as the project scope evolves."
Quotable: "Product design specification , a document that describes design specifications"
Quotable: "The brief outlines the deliverables and scope of the project"

**[24] Wyn M Jones and Hedda Haugen Askland, "Design Briefs: Is There a Standard?" (Design Society / EPDE 2012).** academic. **fetched-and-verified.**
`https://www.designsociety.org/download-publication/33176/design_briefs_is_there_a_standard`
Supports: Describes a named three-stage briefing structure (Blyth and Worthington) in which a pre-project brief, a project brief, and a post-project brief each belong to a different phase and author, with an approval step recorded at the project-brief stage; this is the clearest sourced account of how a brief's start gets approved and recorded, though it sits on the commissioning side the bundle routes away
Quotable: "A pre-project brief is the responsibility of the client. In narrative form this part of the brief will define the need of the project, the aims and expectations of the client, and expressions of their resources both in staffing and budget that will be applied to the project."
Quotable: "A project brief is developed by the design team on the basis of the pre-project brief, with the aim to propose alternatives to constraints and costs, to create a bulleted list of design activities and in general validate the project. This process could be seen as impersonal and the approval process has an implied evidential documentation for legal circumstances should they arise."
Quotable: "A post-project brief is generally authored by the designer and represents a reflection on the design process with the aim of providing some lessons for future projects."
Quotable: "A written design brief will clearly articulate the product requirements to all parties involved in a project."
Quotable: "The design brief, which is essentially a question or definition of a problem, should be used as a validation tool periodically throughout the project when making key decisions."
Quotable: "It is used to help the designer to understand the problem by defining the objectives and parameters of the project toward generating the most appropriate solution."
Quotable: "initial research shows that there is little common guidance on how to write and structure such a vital document"
Quotable: "there is no single or correct format for a design brief"
Quotable: "it can be generated by the designer, by the client or as a shared and agreed document between both parties"

**[25] GV (Google Ventures), "The Design Sprint".** vendor. **fetched-and-verified.**
`https://www.gv.com/sprint/`
Supports: Read in full for a named 'Sprint Brief' document to contrast against the design brief; none exists on this canonical page. The five-day process (Monday problem-mapping through Friday customer testing) is described as a single continuous week, not as separated by a brief document, and the storyboard produced mid-week is a prototyping plan, not a pre-commissioning brief
Quotable: "The sprint is a five-day process for answering critical business questions through design, prototyping, and testing ideas with customers."
Quotable: "By Wednesday morning, you and your team will have a stack of solutions. [...] you'll take the winning scenes from your sketches and weave them into a storyboard : a step-by-step plan for your prototype."

**[26] Teresa Torres (Product Talk), "Opportunity Solution Trees".** practitioner. **fetched-and-verified.**
`https://www.producttalk.org/opportunity-solution-trees/`
Supports: Read in full specifically to find a contrast with the design brief; none exists. The tree is described as a living, continuously updated map, not a document handed off at a point in time, and the word 'brief' does not appear on the page
Quotable: "Follow these steps to create an opportunity solution tree:"
Quotable: "Once you meet the prerequisites, you can follow these steps to create your first tree."

**[27] Noric Dilanchian (Dilanchian Lawyers & Consultants), "Use design briefs to shape your projects" (2007).** practitioner. **url-confirmed-not-read.**
`https://dilanchian.com.au/?p=789`
Supports: Nothing in this bundle rests on it alone. It places the design brief early, before the deal and the contract that commission design work. The live page and its Wayback snapshot both returned no text on 2026-10-22, so no quotation is carried

### The gap question

**[28] Julia Martins (Asana) - "The complete guide to writing creative briefs".** practitioner. **fetched-and-verified.**
`https://asana.com/resources/how-write-creative-brief-examples-template`
Supports: Names 'Messaging and tone' and 'Stakeholders' as standing elements distinct from goals/audience/deliverables; ties tone explicitly to existing brand guidelines when they exist
Quotable: "If you already have brand guidelines, be sure to include them in your creative brief or direct stakeholders to their location. Following brand guidelines ensures that the tone and voice of your messaging match your overall brand and remain consistent across marketing initiatives."
Quotable: "This is why it's so important to identify all key stakeholders up front. Each team member should know who is involved and what they're responsible for."
Quotable: "Think of your message as a person. It should have a voice (a personality) and a tone (a mood or attitude)."

**[29] Figr (vendor blog) - "How to Write a Design Brief: Actionable Guide".** vendor. **fetched-and-verified.**
`https://figr.design/blog/how-to-write-a-design-brief`
Supports: Names decision rights/approval path, out-of-scope/exclusions, decision history, and feedback-round/revision-limit review mechanics as elements a strong brief carries, and runs a named pre-mortem checklist against ambiguity
Quotable: "What's out of scope: Adjacent requests, future phases, unrelated cleanup"
Quotable: "Review pattern: Revision limits, feedback rounds, and approval owner"
Quotable: "Approval path: Who decides when feedback conflicts"
Quotable: "Decision history: What the team already tried, rejected, or deferred"
Quotable: "What phrase in this brief could two smart people interpret differently?"
Quotable: "What constraint are we assuming someone else knows?"

**[30] Canny Creative (branding agency) - "How to Write a Design Brief (Template Included!)".** practitioner. **fetched-and-verified.**
`https://www.canny-creative.com/how-to-write-a-design-brief/`
Supports: Names measurable success factors, a named lead contact, and a scored awarding/decision-criteria section (cost, quality, experience, alignment, suitability), plus a distinct internal stakeholder review-and-feedback pass on the brief itself before it goes out
Quotable: "Having a set of “success factors” can help all parties drive the correct response and results."
Quotable: "Cost/Value for Money Quality of Work Previous Experience Alignment to the Design Brief Suitability of the Agency"
Quotable: "Ensure that the design brief reaches the key decision-makers and individuals who can provide valuable insights and feedback"
Quotable: "There's nothing more frustrating than “design by committee.” However, it does happen, and it can be managed. But there always needs to be a lead point of contact in every design project."

**[31] UXPin - "How to Write a Good Design Brief? [+ Templates]".** vendor. **fetched-and-verified.**
`https://www.uxpin.com/studio/blog/design-brief`
Supports: Gives an explicit RACI model for decision rights, names 'what is not within the project's scope' as a required overview question, lists accessibility requirements as part of a companion 'design specification' (distinct from the brief itself), and gives the handoff its own named timeline milestone separate from the overall project timeline
Quotable: "A succinct way to include these key people in your design brief is by using the RACI project management model"
Quotable: "Responsible: who must do the work Accountable: the team leader who ensures the work gets done Consulted: stakeholders who provide input and feedback Informed: stakeholders designers must keep in the loop with high-level progress updates- they do not have any decision-making authority"
Quotable: "What is not within the project's scope?"
Quotable: "A design brief outlines what designers must create, while the specifications define specific details, including visual design elements, user flows, assets, file formats, accessibility requirements, brand guidelines, technical limitations, etc."
Quotable: "Key milestones and timelines-i.e., research, design, prototyping, testing, etc. Stakeholder feedback sessions Prototyping and testing schedule Design handoff date Task dependencies Final release Quality assurance"
Quotable: "Plan beyond the scope Thinking about the future is crucial. There might be a marketing campaign to promote the release or a possible future redesign."

**[32] Design Pickle Help Center (CJ Robles) - "How To Create A Successful Design Brief".** vendor. **fetched-and-verified.**
`https://intercom.help/design-pickle/en/articles/9532487-how-to-create-a-successful-design-brief`
Supports: Names a dedicated References/Inspiration section with instructions on whether images should be copied or just inspire, an annotation practice for pointing at specific liked elements, and places an accessibility-standards line inside general instructions rather than as its own section
Quotable: "Reference or Inspiration Images: Attach any reference images or inspiration for the design. Specify whether these should be replicated exactly or just used as inspiration."
Quotable: "We particularly like the layout of the first image, the color scheme of the second, and the typography of the third. These should be used as inspiration, not replicated exactly."
Quotable: "Ensure compliance with accessibility standards (e.g., sufficient color contrast)."
Quotable: "If you're attaching inspiration or reference images, you can use the annotation tool to add specific instructions where needed."
