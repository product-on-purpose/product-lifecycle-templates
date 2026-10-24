# use-case-specification: research log

Research conducted 2026-10-15, building on admission sweep 5 (2026-10-12), the spec research of 2026-10-14, and
the spec that merged on 2026-10-15 with ADR 0072 (use-case-specification joins delivery-docs, with the new verb
"elaborates"). The build's six-dimension fan-out covered Cockburn's canon (his templates, formality levels, goal
levels and writing rules), the other published templates, the lineage from Jacobson through UML to Use-Case 3.0,
the debates over stories, detail and the named failure modes, the library's own neighbours and the facts the worked
example must agree with, and the standing gap question. **27 sources are recorded below, all
fetched-and-verified**: 8 primary, 2 standards bodies, 15 practitioner and 2 vendor. Only fetched-and-verified
sources are quoted anywhere in this bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a retrieval tool
returns: pages as downloaded, and PDFs through a text extractor. The build's agents returned 212 quotations. 178
pass as normalized substrings, 7 more pass once whitespace the extractor broke is ignored, and 4 more pass once
markup is ignored. Two quotations ran list or table cells together and were split, keeping 14 passing parts.
Twenty-one failed, for the reasons the next section gives. Thirty-six quotations were added from raw text: 34
re-quotes of failed quotations, cut shorter to avoid extraction artifacts, and 2 that the spec relied on and no
agent returned, Wiegers' permission line [7] and the Otago mirror's "Sub-Variations" field name [1]. One of the
re-quotes repeats a quotation an agent had already returned for the same source [20], and the log keeps one copy.
**238 quotations remain.**

---

## What the checks caught, and what was not read

**Twenty-one quotations failed the raw-text check: nine because separate pieces of text were run together, eight
on extraction artifacts, three on small edits by the agents, and one on who wrote the words.** Nine ran text
together: the W3C template's seven quotations [9] joined each field heading to its description with `--`, which the
page prints on separate lines, and all seven were re-quoted as the description alone; two from the IRMUK slides [21]
ran bullet points together. Eight failed on an extraction artifact that the agent's quotation rightly left out or
that the raw text carries: curly apostrophes stored as replacement characters in *Use Cases, Ten Years Later* [6];
non-breaking spaces on Ambler's page [22]; dashes and curly quotation marks in the Use-Case 3.0 [13] and Use-Case
Foundation [14] PDFs; and rendering artifacts in two sentences of the RUP template [8]. In three, the agent changed
the text: straight for curly quotation marks on Brandenburg's page [20], single for double quotation marks in the
Rosenberg digest [18], and, on the OpenUP checklist [24], a typo in the page silently corrected with a bracketed
letter, which was re-quoted as two segments that leave the typo out.

**One failure was an attribution error, not an artifact.** The published book's preface reads "led to the
explanations in this book and to the Stakeholders and Interests model, which is a new idea presented here" [5], and
it passes against the Pearson sample pages. An agent had filed that sentence under the pre-publication draft. The
draft's own wording is different, and it passes against the draft: "led to the explanations in this book and the
Stakeholders & Interests model, which is new in this book" [3]. Both are now quoted under the right entry. The
spec's "new idea" sentence is therefore the 2001 book's, and the draft makes the same claim in its own words.

**The fully dressed field set no longer rests on reconstruction.** The spec says that the 2001 book's *Use Case 24
Fully Dressed Use Case Template*, on pages 119 to 120, was never read, and that is still true. Every Internet
Archive copy is lending-restricted, and the Pearson sample pages [5] carry the book's table of contents, preface and
index, including the index entry "Use Case 24 (Fully Dressed Use Case Tem-plate), 119-120" [5], but not the
template box. What has changed is that the pre-publication draft #3 [3], edit date 2000.02.21, prints its own fully
dressed template, and this build read it verbatim. Its header block, quoted in full under [3], opens "USE CASE 7:
FULLY DRESSED USE CASE TEMPLATE" [3] and names, in order: Context of use, Scope, Level, Primary Actor, Stakeholders
& Interests, Precondition, Minimal Guarantees, Success Guarantees and Trigger. The body that follows was read in the
same raw text and is named here without quotation marks, because it was not submitted as a quotation: Main Success
Scenario, Extensions, Technology and Data Variations List, and an open-ended Related Information block for whatever
a project needs [3]. **The full variant's field set now rests on three things read directly**: the draft's own
template, read in full [3]; the 1998 template [1], [2]; and the 2001 book's preface, table of contents and index
[5]. It no longer rests on converging secondary field lists. The practitioner reproduction [12] agrees with the
draft, and it is corroboration only, not a ground.

**What the draft does not settle: whether the published book's Use Case 24 differs from the draft's Use Case 7.**
The draft is an earlier edit state of the same manuscript. One provenance detail ties the two more closely without
settling the question: the draft's own table of contents already lists the fully dressed template as Use Case 24,
on page 120, while its body prints the same template as Use Case 7, on page 68 [3]. This log reads that as an
extract taken from a longer manuscript whose numbering had already moved; it says nothing about whether any field
changed. **Nothing in this bundle may say the published template was read, or that its fields match the
draft's.** The companion cites [3] for the field list and names it as the draft's.

**The spec's unsubmitted field names now pass.** The spec reported Scope, Level, Preconditions, the 1998 closing
block's field names, and Open Issues and Schedule as read but not submitted to the recheck. All of them now pass as
Quotable lines under [1]: the RELATED INFORMATION block with its Priority, Performance Target, Frequency,
Superordinate and Subordinate Use Case, Channel and Secondary Actors fields, "OPEN ISSUES (optional) <list of issues
about this use cases awaiting decisions>", and "SCHEDULE Due Date: <date or release of deployment>" [1].

**The draft's guideline bodies and six of its chapters could not be read.** Draft #3's chapters 6 to 9
(preconditions and guarantees, scenarios and steps, extensions, technology and data variations) and its closing
reminders, chapters 20 and 21, appear in the extracted text only as headings followed by an ellipsis. The bodies of
Guidelines 1 to 12 appear only as table-of-contents and index entries, in the draft [3] and in the Pearson pages
[5]. The titles drift between the two: the draft's "Guideline 11: The condition says what was detected." [3] is the
book's "Guideline 11: Make the Condition Say What Was Detected" [5]. The guide may name a guideline by its title,
and must not paraphrase a body nobody read.

**What was assigned and not read, or read only in part:**

- **The 2001 book's Use Case 24, pages 119 to 120.** Lending-restricted, as above.
- **The Use-Case 2.0 ebook from Ivar Jacobson International.** A Cloudflare block answered both the cache and a
  direct fetch. Use-Case 3.0 [13] stands in for the Jacobson lineage.
- **Jacobson's 1987 OOPSLA paper and the 1992 book.** Not fetched. They are known here only through the
  bibliography in [13], so the companion may cite [13] for the dates and must not describe either text.
- **Jacobson and Cockburn's *Use Cases are Essential* (ACM Queue, 2023), and Karl Wiegers' Medium article on use
  cases falling out of favour.** Both returned HTTP 403 to a direct fetch and to the retrieval tool. A search
  snippet suggests Wiegers makes that claim; no phrase of his is quoted, and the claim is not attributed to him.
- **Cockburn's own essay on why he still uses use cases.** HTTP 404. His distinction between a use case and a
  story is quoted only as Nettleton relays it [23].
- **Tyner Blain's earlier *Top five use case blunders* post.** Not fetched, so five of the ten mistakes in [19]
  are bare labels in this log.
- **IEC 62559-2:2015 and ISO/IEC/IEEE 29148.** Paywalled. Nothing in this bundle may describe either standard's
  fields or clauses.
- **Vendor and practitioner template pages.** Jama, Visure and ReqView's own documentation and Modern Analyst's
  template page were not located. ArgonDigital's field table sits behind a lead-capture form, so [11] supports only
  the prose around it. No government agency's use case template with an accessible field list was found.
- **The FHWA Systems Engineering Guidebook's stakeholder checklist.** Every URL tried returned 403 or redirected.
- **A CU Boulder lecture on stakeholders and interests.** Deliberately not fetched: it paraphrases Cockburn, and
  citing it would have passed his terminology off as independent corroboration.
- **A *Disciplined Use Case* paper pairing mockups with scenario steps.** It surfaced only in a search summary and
  was not fetched.
- **Strembeck and Zdun [27].** Only the abstract and record page were read.
- **BABOK.** Not cited in either direction, per the spec's risk 6 (the BABOK contradiction): one admission-sweep
  dimension flagged its Use Cases and Scenarios technique as publishing the type as a written document, another
  flagged it as not, and neither had read it.

---

## The admission record

The spec's admission section stands on four sources, and **every quotation it relied on is now a Quotable line in
this log**.

| Admitting source, as the spec names it | Entry | Quotation the spec relied on, and where it now sits |
|---|---|---|
| Cockburn, Basic Use Case Template (1998), Otago mirror | [1], with the Bentley mirror [2] confirming the same field set | "You have permission to copy and distribute the documents as long as you reference the source of the originals." Quotable under [1] |
| Wiegers, Use Case Template (1999) | [7] | "Permission is granted to use, modify, and distribute this document" [7]. No agent returned it; this build added it from raw text, and it passes |
| RUP, Use-Case Specification template, UFPE mirror | [8] | The headings, which pass with their section numbers: "2.1 Basic Flow", "2.2 Alternative Flows" and "6. Extension Points" [8] |
| Cockburn, *Writing Effective Use Cases*, draft #3 (2000.02.21) | [3] | "A casual use case is one written in simple, paragraph, prose style" and "A fully dressed use case is written with one of the full templates" [3], each the opening words of a longer Quotable line |

The spec's other quoted spans pass too. The 1998 field names "Goal in Context", "Success End Condition", "Failed
End Condition", "Primary Actor", "Trigger" and "Superordinate Use Case" are Quotable under [1], and
"Sub-Variations" was added from raw text [1]. The spec's "Minimal Guarantee" span passes only inside an editorial
note that appears on the Otago mirror [1] and not in the Bentley copy of the same template [2]; nothing read says
who wrote it. "The brief of a use case is a 2-6 sentence description of the use case behavior" passes under [3],
and the preface sentence and "6.2 Minimal Guarantees" pass under [5]. The spec's table-of-contents heading for Use
Case 24, at page 119, is present in the raw text of [5], but it is not a Quotable line here: what this log quotes
from [5] is the index entry for pages 119 to 120, and the companion quotes that entry.

**This build found two further templates and one false match.** A university course template, NYU's [10], and a
consultancy's, ArgonDigital's [11], both publish the type; neither is needed for admission. The W3C eGovernment
template [9] shares the name and not the type (see contested item 9).

---

## Claims flagged contested or time-bound

1. **Stories versus use cases: the sources agree that the shapes differ, and disagree about which to reach
   for.** For stories: Cohn says "User stories typically, but not always, and not in every case, are the best
   choice for teams using Scrum" [17], because "Use cases are often too large to estimate usefully." [17], and a
   story "is a placeholder for a future conversation" [17]. Nettleton reports a camp that "felt use cases were too
   heavyweight" [23]. For use cases alongside stories: Nettleton relays Cockburn's distinction, "A use case
   provides a contextual view of what is to be built, serving to bind the organization together, among other
   things." [23], and adds his own view that "their absence is a sign that a software project is in trouble" [23].
   Girvan lists "Use cases are the same as user stories" under a heading of myths [21], and quotes Cockburn in 2024:
   "Use Cases have structure and cease to be useful if at too low a level, whereas user stories can decompose
   forever" [21]. Use-Case 3.0 treats stories as one kind of work item a use case feeds: "user stories (for agile
   teams) and Tasks (for waterfall project teams)" [13]. The library already states the boundary from the story's
   side (`templates/user-stories/user-stories_companion.md:151-153`). The bundle takes neither camp; it is where
   `user-stories_guide.md:15` sends a reader who needs "exhaustive actor-system flows".

2. **Whether use cases are out of fashion. Time-bound, with dated camps, and settled by nothing measured.** Girvan's
   2024 slide headed "Why use cases have fallen out of favour" names "Over complicated use within UML" [21], then
   the Agile Manifesto and the popularisation of user stories; her timeline dates use cases to 1987, their
   incorporation into UML to 1997, the Agile Manifesto to 2001 and the popularisation of user stories to 2005 [21].
   The same deck records a counter-move: Jacobson and Cockburn's *Use Cases are Essential* in ACM Queue in 2023,
   which this build could not read, and a jointly published use case foundation in 2024 [21]. Use-Case 3.0, dated
   December 2024, confirms the second date: "The Use-Case Foundation principles were published in 2024" [13].
   Nettleton's push-back camp dates to 2014 [23]; Cohn's page says it was last updated April 23rd, 2026 [17]. No
   source measured how many teams write use cases at any date. **The bundle may say the claim is made and by whom,
   and must not state either decline or resurgence as a fact.**

3. **UI detail, business rules and data inside a use case: three questions, with different answers.**
   - **UI detail is contested.** Against it: Cockburn's step rule, "Highlight the actor's intention, not the user
     interface details." ([3], [4]); his own ranking, "The two most common and most costly to the project are
     including too many details and including UI specifics." [6]; Brandenburg's "By far the most common mistake we
     see in use cases is that they use the language of the user interface to talk about the user behavior." [20],
     and "Using user interface details leads to ambiguity." [20]; OpenUP's "Is each step technology-independent?"
     [24]; and Girvan's table, which limits a use case to behaviour and excludes UI (paraphrased; the cell is not a
     passing quotation) [21]. For it, in a qualified form: Rosenberg names interface objects, which "are identified
     by describing system usage from the user manual perspective" [18], and advises "write the user manual before
     you write the code" [18]; Ambler says "A formalized system use case refers to specific user interface
     components-such as screens, HTML pages, or reports" [22], which he would not do in an essential use case.
     Ambler's split is by kind of use case, and the other sources do not draw it, so the disagreement is live. Both
     "most common" claims are their authors' own, not measurements.
   - **Business rules: the sources converge on referring to a rule from the step, and keeping its text
     elsewhere.** Cockburn says two different things. His 2002 article says "The fully dressed use case features
     the long template with fields for stakeholders, minimum guarantees, postconditions, business rules,
     performance constraints, and so on." [6]. His draft says, in prose this build read in raw text but did not
     submit as a quotation, that use cases do not contain business rules, performance requirements, UI design or
     data descriptions, which belong in their own chapters of the requirements and are cross-linked from the use
     cases [3]. The draft's own template carries no business-rules field [3], and neither do the 1998 template
     [1], Wiegers [7], RUP [8] or NYU [10]. Ambler's formal use case refers to a rule by its identifier from the
     step that applies it, "because business rules reflect essential characteristics of your domain that your
     system must implement" [22], and he writes the rule inline only "For very simple systems without very many
     complex business rules" [22]. Girvan's worked example refers to a rule by identifier from an alternate flow
     and lists it below the use case: "BR1 - No more than 100 people allowed in library at any time" [21]. Notre
     Dame keeps rules in a catch-all section for "requirements that are not directly related to the actions" [25].
     See the section design below for what this does to the spec's omission.
   - **Data definitions belong elsewhere, and no source read says otherwise.** Brandenburg lists "Specific data
     elements or data tables" among the technical details to keep out [20], and says "When it comes to data
     elements, a best practice is to use a data dictionary or data map to analyze the data requirements." [20].
     Cockburn's draft excludes data descriptions [3], and Girvan's table excludes data [21]. The bundle routes a
     reader who needs field definitions to `data-dictionary`.

4. **Goal levels: named differently over time, and absent outside Cockburn's templates.** Cockburn's draft names
   three: "User-goals (blue, sea-level )", "Summary level (white, cloud / kite )" and "Subfunctions (indigo/black,
   underwater /clam )" [3]. Of the user goal he says "The user goal is the goal of greatest interest." and gives
   the size test "One person, one sitting (2-20 minutes)." [3]; of subfunctions, "Include them only as you have
   to." [3]. The 1998 template names the middle level differently, "Level: <one of: Summary, Primary task,
   Subfunction>" [1], where the draft has "Level: <one of: Summary, User-goal, Subfunction>" [3]. A marking
   convention appends a character to the name [4]. Design scope is a separate axis: "A business use case has the
   enterprise as its design scope." and "A system use case has a computer system as its design scope." [3]. The
   camps: Cockburn's templates carry a level field, while the Wiegers [7], RUP [8] and NYU [10] templates carry
   none. This log reads Ambler's essential-versus-system distinction [22] as a third axis, about how much
   technology a use case names, and it must not be merged with either. The guide uses the draft's names
   (user-goal, summary, subfunction).

5. **Include and extend: a relationship between use cases, not a section of one.** UML defines both as
   relationships between use cases: "Include is a DirectedRelationship between two UseCases" [15], and "An Extend
   is a relationship from an extending UseCase (the extension) to an extended UseCase (the extendedCase)" [15].
   UML leaves the location format open: "UseCases may be specified in various formats such as natural language,
   tables, trees, etc." [15]. RUP gives the extend relationship its own section, "6. Extension Points", for the
   "[Definition of the location of the extension point in the flow of events.]" [8]. NYU folds it into its
   extensions section, which "presents those use cases that have an extends relation with the current use case"
   [10]. Cockburn's extensions are branches inside one document, with "the numbering convention in the extensions
   sections involving combinations of digits and letters (e.g., 2a, 2a1, 2a2 and so on)" [3], and a branch may hand
   off to another use case: "<step altered> <condition> : <action or sub.use case>" [1]. Wiegers carries an
   Includes field [7]. No source read names overuse of include or extend as a failure. **The library's position**:
   one Extensions section in Cockburn's numbering; a link to another use case sits in the step that calls it or in
   Related Information; no Extension Points section.

6. **The methodology value (catalog correction 1). Recommendation: `methodology-agnostic`, as the spec
   proposes.** What each source ties use cases to:
   - **Waterfall:** no source ties the type to it. Use-Case 3.0 names waterfall teams only as one mode it supports,
     "Tasks (for waterfall project teams)" [13].
   - **RUP and the Unified Process:** RUP publishes its own use-case specification template [8], and its page sits
     inside RUP's requirements artifact set under the use-case model [8]. Jacobson is described as a father of "the
     Unified Modeling Language and the Rational Unified Process" [13], and his co-author Spence "specialized in the
     agile application of the Unified Process" [13]. Girvan's timeline records use cases being incorporated into
     IBM's RUP [21], and Cockburn's draft lists the RUP template as one format among several [3]. These are ties of
     lineage and authorship. No source says a use case specification requires RUP.
   - **Agile:** "This guide describes how to apply use cases to capture system requirements in an agile and
     scalable fashion." [13]; the foundation principles ask for use cases written "in some cases in a lightweight
     and agile way, in other cases in a rigorous way" [13]; Ambler writes from agile modeling and warns "It is very
     easy for use case modeling to become un-agile." [22]; and Notre Dame's inventory names a sprint "if using an
     Agile development methodology" [25].
   - **None:** "Use-Case 3.0 will support, focus and complement whatever planning, work management and development
     approaches your teams have selected." [13]. A text search of the raw pages found none of waterfall, agile,
     Unified Process, RUP or Scrum in the 1998 template [1], the Wiegers template [7] or the Use-Case Foundation
     [14], and the lineage dimension reports the same for UML [15]. The lineage dimension also read the
     foundation's first principle, "1. Use Cases apply to systems of all types and sizes" [14], as a methodology
     disclaimer; it is about kinds of system, not process, so this log rests the recommendation on [13] and on the
     silence of [1], [7], [14] and [15] instead.

   **Confidence: medium-high.** The catalog's `Waterfall/UP/RUP` has no ground for Waterfall and treats a lineage
   as a requirement. The companion names RUP as one lineage among Cockburn's, Wiegers' and Jacobson's later
   agile-facing work.

7. **The `use case model` alias and the UML diagram (catalog correction 4). Keep the alias; state the
   difference.** In the sources that use the phrase, a use case model is the whole set of a system's use cases and
   actors: RUP files its specification template inside its use-case model artifact [8], and Use-Case 3.0 defines a
   use-case model as a model that captures and visualizes all the useful ways to use a system [13] (both
   paraphrased). UML specifies the elements, "Actors, UseCases, and subjects" [15], and the diagram, "A UseCase is
   shown as an ellipse" [15], and allows the behaviour to be described by "natural language text where
   appropriate" [15]. Whether the diagram matters is contested: Fowler says "these diagrams are of little value -
   the key value of use cases lies in the text which is not standardized in UML" [16], while UML's own clause
   standardizes the diagram and not the text. Girvan lists "Use cases are models as in use case diagram" among her
   myths [21]. **The companion says that a use case model names a system's full set of use cases and actors, which
   UML draws as a use case diagram, and that this bundle templates the written specification of one use case
   inside such a model.**
   The diagram stays out of scope under ADR 0030 (templating scope: Markdown documents), as ADR 0072 records.

8. **Alternative and exception paths: one section or two.** Wiegers numbers them apart, alternative courses as
   X.Y.AC.1 and exceptions as X.Y.EX.1 [7], and NYU gives exceptions their own section, "Exceptions: {This section
   describes all error conditions that can arise in the use case.}" [10]. RUP folds both into "2.2 Alternative
   Flows" [8]; Cockburn folds both into Extensions, each of which ends "back in the MSS, at a separate success
   exit, or in failure" [3]; the foundation lists "all the special cases, alternative paths, optional steps, and
   errors that need to be handled" [14]. The spec's single Extensions section follows Cockburn, RUP and the
   foundation, and the guide names alternative flows and exceptions as the other templates' terms.

9. **The W3C template is a different genre that shares the name.** It asks the author to "Define the problem that
   the standard aims to solve and proposed benefits." and to reach "A conclusion on whether the use case has the
   critical mass for recommendation, and a justification" [9]. It has no actor field, no conditions and no steps.
   It must not count toward any claim about which sections use case templates carry.

10. **The provenance of the stakeholder model.** The preface's "a new idea presented here" [5] is new relative to
    the 1998 template, which never uses the word stakeholder ([1], [2]). It does not mean the model arrived late
    in the book's writing: the draft already carries "Stakeholders & Interests" in its template and in step 7 of
    its writing process [3], and *Use Cases, Ten Years Later* places the idea around 1997 [6].

11. **Distinctness from four siblings stays contested.** The spec draws the boundaries with `acceptance-criteria`,
    `epic`, `prd` and `test-case` from their headings and from the shipped boundary sentence in
    `user-stories_companion.md:151-153`, not from an audit of their content
    (`docs/internal/tier2-specs.md:4967-4972`). This build's check of the four examples found their shared facts
    consistent, which is narrower than a flow-by-flow audit. The companion must not claim a clean, settled
    boundary (the spec's risk 4, distinctness is contested). **One boundary the spec labelled as the library's own
    unsourced position, against `sdd` (`docs/internal/tier2-specs.md:4960-4964`), now has sources on both sides.**
    For keeping design out: Brandenburg says of technical detail, "These details are best saved for a technical
    design document." [20]; Cockburn's draft separates the two kinds, "a black-box use case does not discuss the
    internal structure of the system under discussion, while a white-box use case does." [3]; and both of his
    templates define Scope as the system "black-box under design" ([1], [3]). Against a clean line: Cockburn concedes
    the form can carry design, "As design documentation, the use case describes: the user does this; some first
    component does a set of things" [6]. The companion can now cite the black-box rule for the `sdd` boundary, and
    must say that a white-box use case written as design documentation is a use the form permits and this bundle
    does not template.

12. **Time-bound sources.** Cohn's page [17] is revised in place. Use-Case 3.0 [13] is v1.00 of December 2024. The
    practitioner reproduction [12] is a versioned package, 0.1.0. ArgonDigital's page [11] is a vendor page. The
    W3C template [9] is an archived wiki page last modified in December 2008.

---

## Notes for the companion

**The honest framing.** A use case specification writes down, for one primary actor and one goal, what the actor
and the system do, step by step, when everything goes right, and what happens at each point where something can go
another way. Cockburn's own definition is that "A use case captures a contract between the stakeholders of a system
about its behavior." [3]. Its numbered main scenario and its lettered extensions ([1], [3]) are what separate it
from a story's one sentence and from acceptance criteria's pass/fail checks. Cockburn puts its value in the
branches: "The greatest value of the use case does not lie in the main scenario, but in alternative behaviors."
[6], and Rosenberg adds that "you're not done when you've written the basic course" [18]. It states requirements,
not design ([3], [24]), and it is not a test: "Use cases are not test plans or test cases. They are missing the
data values needed for test cases." [6]. **Its family fit is the library's own chosen widening, not a reading of
the contract.** No family contract admitted the type as written. ADR 0072 widened `delivery-docs` with the verb
"elaborates", and the research that found even that fit said a maintainer could as reasonably have read the
contract as excluding the type (`docs/internal/tier2-specs.md:4880-4886`). The companion presents "elaborates" as
that choice (the spec's risk 3, family fit is strained), and states the chain position the contract gives it: after
the stories and before the acceptance criteria (`docs/internal/contracts/delivery-docs.md:11`).

**Evidence of effect, stated plainly.** No source in this research measured whether writing use cases improves an
outcome. Pratama et al. report that their protocol "successfully derived two-unit test cases with 100% basis path
coverage" [26]: that measures the protocol on its own worked case, not what use cases do for a project. Their
observation that "most students operate without granular traceability, standardized structures, or alternate flow
testing" [26] describes student work and is not tied to any outcome. Strembeck and Zdun [27] were read as an
abstract only. Cockburn's account of a team that, having listed stakeholders and interests after shipping, found
most of its first-year change requests in that list, and concluded that "had they simply written down the
stakeholders and interests for each use case early on, they would have avoided an entire category of mistakes" [6],
is one consultant's story as Cockburn relays it. The companion may cite each for what it is.

**The formality levels and the two sizes.** Cockburn names three: "In Writing Effective Use Cases, I name three
degrees of detail in writing use cases: brief, casual, and fully dressed." [6]. In his own definitions:

- **Brief:** "The brief of a use case is a 2-6 sentence description of the use case behavior, mentioning only the
  most significant activity and failures." [3]. The 2002 article gives a narrower range: "The use case brief
  consists of two to four sentences summarizing the use case." [6]. The guide must not fix a sentence count. The
  brief sits below anything this library templates.
- **Casual:** "A casual use case is one written in simple, paragraph, prose style. It is likely to be missing
  project information associated with the use case, and is likely to be less rigorous in its description than a
  fully dressed use case." [3]; and "The casual use case consists of a few paragraphs of text, covering the items
  mentioned above." [6].
- **Fully dressed:** "A fully dressed use case is written with one of the full templates, identifying actors,
  scope, level, trigger condition, precondition, and all the rest of the template header information, plus project
  annotation information." [3].

On when to use which, the draft argues that one template is not enough and asks for two, "a casual one for
low-ceremony projects" and a fully dressed one for higher-ceremony projects [3]. It shows one scenario written both
ways, "USE CASE 4: BUY SOMETHING (CASUAL VERSION)" and "USE CASE 5: BUY SOMETHING (FULLY DRESSED VERSION)" [3]. The
foundation says "The amount of detail and the format used will vary to match your circumstances" [14]. The
practitioner reproduction's advice, "Keep most UCs at brief or casual. Fully-dress only the important ones." [12],
is the reproduction's own and not Cockburn's text. The
library ships `lean` for casual and `full` for fully dressed, per ADR 0072. **That mapping is the library's own
position, and lean is casual in coverage, not in form.** Cockburn's casual form is prose paragraphs ([3], [6]). The
lean template keeps numbered steps, because the contract's verb admits "a main success scenario, stated as a
numbered sequence of steps" (`docs/internal/contracts/delivery-docs.md:15`). The guide therefore calls lean the
library's nearest equivalent of the casual form: it drops the project annotation and the separate extensions, as
casual does, and it keeps the numbered steps that casual would write as prose. The guide gives Cockburn's names
beside `lean` and `full`, and the draft's writing order, from "Precision Level 1: Primary actor's name and goal" to
"Precision Level 4: The extension handling steps" [4], as the way to grow one into the other.

**Build decisions, 2026-10-15, taken from the notes below and overrulable by the maintainer.** The drafting
stages follow this list. Lean carries five sections, in this order: Title and Actor; Goal in Context; Preconditions
and Trigger; Main Success Scenario; Minimal and Success Guarantees. Full carries ten, in this order: Title and Actor;
Goal in Context; Scope and Level; Stakeholders and Interests; Preconditions and Trigger; Main Success Scenario;
Extensions; Minimal and Success Guarantees; Related Information; Open Issues and Schedule. Three changes from the
spec's table follow from the research: the spec's "Postconditions (Success and Failed End Condition)" is renamed
Minimal and Success Guarantees and asks what stays true on every exit; Stakeholders and Interests is added, full
only; and the Title and Actor section asks for an identifier. RUP's "Extension Points" heading is no longer cited
for Extensions. No business-rules section is added. Lean's deviations are asked for in a line of prose each inside
the Main Success Scenario section, and the guide's rubric grades that.

**The section design, as the research moved it from the spec.** The spec's nine sections are taken in order below.
Eight stand, with their sourcing updated. One is renamed and asks a different question. One new full-only section
is recommended, and four smaller candidates are routed under decision procedure 12 (a property or section is
proposed for a template).

- **Title and Actor** (lean) stands. Its sources are "Use Case: <number> <the name should be the goal as a short
  active verb phrase>" and "Primary Actor: <a role name for the primary actor, or description>" [1], and the draft
  keeps both lines [3]. **Candidate, recommended (E1 [1], [7], [10], [25]; homed here; fits lean): the title line
  carries an identifier.** The 1998 header already has a number, and three other sources ask for one: "Give each
  use case a unique numeric identifier, in hierarchical form: X.Y." [7], "Use Case ID" [10], and "Each use case
  should have a unique identifier that can be used for quick reference and traceability." [25]. The goal-level
  marks of [4] are an optional guide convention.
- **Goal in Context** (lean) stands, and **the name stays**. The draft renames the field "Context of use: <a longer
  statement of the goal, if needed, its normal occurrence conditions>" [3]. Keeping the 1998 name, "Goal in
  Context: <a longer statement of the goal, if needed>" [1], is the library's own choice: it names the goal the
  contract's verb is organised around, and it is read verbatim. The guide gives "Context of use" as the draft's
  term, and the draft's added "normal occurrence conditions" becomes an ASK question.
- **Scope and Level** (full) stands, and **it is no longer reconstructed**: the draft prints "Scope: <design scope,
  what system is being considered black-box under design>" and "Level: <one of: Summary, User-goal, Subfunction>"
  [3]. The guide uses "user-goal", not the 1998 "Primary task" (contested item 4).
- **Stakeholders and Interests: a new candidate section, full only. Recommended for adoption, confidence medium.**
  The spec has no such section; it designed the full variant from the 1998 template, which never mentions
  stakeholders. The draft's template carries "Stakeholders & Interests: <list of stakeholders and key interests in
  the use case>" [3], and Cockburn's 2002 article lists "fields for stakeholders" first among the fully dressed
  template's fields [6]. The draft's writing process makes the rest of the document answer to it: "7. Capture
  stakeholders and interests, preconditions and guarantees. The system will ensure the preconditions and guarantee
  the interests." and "8. Write the main success scenario (MSS). Use 3 to 9 steps to meet all interests and
  guarantees." [3]. A stakeholder is "someone with a vested interest in the behavior of the use case, even if they
  never interact directly with the system" [3]. Under procedure 12: E1 (sourced) is met by [3] and [6]; every other
  source that carries the field ([12]) is Cockburn's lineage, and the gap dimension found no independent one. E3
  (homed): the only other home is the guarantees section, which defines the minimal guarantee in terms of these
  interests but cannot hold the list. E4 (sized): full only, since Cockburn's casual form is prose without the
  template's header fields [3], and lean stays the default. **Placement: between Scope and Level and Preconditions
  and Trigger**, which follows the draft's order and keeps lean a strict ordered subset of full. Adopting it makes
  full ten sections, which changes the spec; the build report names it for the maintainer.
- **Preconditions and Trigger** (lean) stands, on "Preconditions: <what we expect is already the state of the
  world>" and "Trigger: <the action upon the system that starts the use case, may be time event>" [1], the
  draft's "Precondition" and "Trigger: <what starts the use case, may be time event>" [3], Wiegers' "List any
  activities that must take place, or any conditions that must be true, before the use case can be started." [7],
  and RUP's definition [8].
- **Main Success Scenario** (lean) stands, on "<put here the steps of the scenario from trigger to goal delivery,
  and any cleanup after>" [1] and "2.1 Basic Flow" [8]. The writing rules the guide draws on are "For each step:
  Show a goal succeeding. Highlight the actor's intention, not the user interface details. Have an actor pass
  information, validate a condition, or update state." [3]; "Use 3 to 9 steps" [3], and Cockburn's report that he
  is "yet to write a main success scenario longer than nine steps" [6]; "Each use case step reflects one activity
  and one activity only." and "Use case steps are written in the active voice." [22]; and the alternation of actor
  and system, "like watching a tennis match" [19], since "just about every user step should have a corresponding
  user response or action" [20]. Cockburn prefers one column of numbered steps with no if statements [3].
  **Candidate for the lean variant (a guide rubric row, not a section):** the spec has lean fold "a short prose
  note of the most important exception" into this section (`docs/internal/tier2-specs.md:5004`). The research
  supports asking for each known deviation in a line of prose instead: the casual form covers "the items mentioned
  above" [6], the value lies in the alternatives ([6], [18]), and the contract admits a scenario "with the
  alternative and exception paths that branch off it" (`docs/internal/contracts/delivery-docs.md:15`).
- **Extensions** (full) stands as one section (contested item 8), on "<step altered> <condition> : <action or
  sub.use case>" [1], the draft's numbering convention [3], "9. Brainstorm and exhaustively list the extension
  conditions. Include all that the system can detect and must handle." and "10. Write the extension-handling
  steps. Each will ends back in the MSS, at a separate success exit, or in failure." [3], and "2.2 Alternative
  Flows" [8]. **One spec citation should be dropped**: the spec also cites RUP's "Extension Points" heading for
  this section, but RUP's extension points mark where another use case may extend this one ([8], [15]), which is
  the include-and-extend layer this bundle leaves out (contested item 5), not a branch inside the document.
- **Postconditions (Success and Failed End Condition)** (lean): **rename it Minimal and Success Guarantees, and
  change what it asks. Confidence: high on the change of meaning, and the name is the library's choice.** The 1998
  field is "Failed End Condition: <the state of the world if goal abandoned>" [1], a property of the failure exit
  alone. The draft replaces it with "Minimal Guarantees: <how the interests are protected under all exits>" beside
  "Success Guarantees: <the state of the world if goal succeeds>" [3], and a minimal guarantee holds on every exit,
  success included, as OpenUP's checklist puts it: "(A Minimal Guarantee represents a condition that will be true
  when the use case ends, regardless of how it terminates.)" [24]. The book's contents confirm the two names, "6.2
  Minimal Guarantees" and "6.3 Success Guarantee" [5], and an editorial note on the Otago mirror records the rename of
  Failed End Condition (spelled there "Condistion") to Minimal Guarantee [1]. The section's WHAT names
  postconditions as the term Wiegers [7], RUP [8] and NYU [10] use. This is the first gap the gap dimension found:
  a template that asks only for success and failure end conditions does not ask what must stay true however the
  case ends.
- **Related Information** (full) stands, and its 1998 field names now pass (see above). The draft turns the block
  into an open slot for whatever a project needs [3]. The same draft's prose says use cases do not contain
  performance requirements or priority [3], which sits awkwardly beside the 1998 block's Priority and Performance
  Target fields [1]. This log reads those fields as the "project annotation information" a fully dressed use case
  adds [3], and the guide's rubric carries OpenUP's placement rule: a performance target that applies to many use
  cases belongs in the shared requirements and is linked from here [24]. **Two candidates are homed here (E1 met;
  full only):** a **Technology and Data Variations** line, which the 1998 template carries as "SUB-VARIATIONS <put
  here the sub-variations that will cause eventual bifurcation in the scenario>" [1] and the draft as Technology
  and Data Variations List [3], and which gives a channel or device difference somewhere to go so the steps can
  stay at intention level (contested item 3; the home is the library's own position); and **Secondary Actors**,
  already in the 1998 block as "Secondary Actors: <list of other systems needed to accomplish use case>" [1], with
  Notre Dame's definition, "A Secondary actor is anyone or anything that is involved in achieving a use case but
  does not gain direct benefit from the use case." [25].
- **Open Issues and Schedule** (full) stands, on "OPEN ISSUES (optional) <list of issues about this use cases
  awaiting decisions>" and "SCHEDULE Due Date: <date or release of deployment>" [1], and Wiegers' "List any
  additional comments about this use case or any remaining open issues or TBDs (To Be Determineds) that must be
  resolved." [7]. The draft's template carries neither field [3], so this section rests on the 1998 template and
  Wiegers alone.

**Business rules: the omission stands, and the spec's stated reason needs a dated note.** The spec's risk 2 (a
business-rules section must not be attributed to Cockburn) says "No source supports it as a named field"
(`docs/internal/tier2-specs.md:5070-5071`). That is now too strong: Cockburn's 2002 article lists business rules
among the fully dressed template's fields [6]. The omission still holds, for three reasons this research supports.
No template read prints a business-rules section: not the 1998 template [1], [2], not the draft's Use Case 7 [3],
and not Wiegers [7], RUP [8] or NYU [10]. Cockburn's own draft places business rules outside the use case, in their
own chapter of the requirements [3]. And the practice read here refers to a rule from the step that enforces it and
keeps the rule's text elsewhere ([22], [21], [25]). Under procedure 12, E1 (sourced) rests on [6] alone, which
describes a template rather than printing one, and E3 (homed) names a better home than this document: the rule's
own record, which the draft places in its own chapter and which this library does not template. **The finding is
routed as a guide rubric row**: a step that enforces a business rule names the rule by an identifier and says where
its text lives, rather than restating or silently omitting it ([22], [21]). The spec's business-rules paragraph and
its risk 2 take a dated note at landing, and the build report names this finding for the maintainer.

**Gap-question candidates, routed by decision procedure 12:**

- **Recommended for the templates, each homed in an existing or proposed section above:** an identifier in the title
  line ([1], [7], [10], [25]); the minimal guarantee as a property of every exit ([3], [24]); Stakeholders and
  Interests in full ([3], [6]); and Technology and Data Variations and Secondary Actors as lines in Related
  Information ([1], [3], [25]).
- **To the guide, as a rubric row or anti-pattern:** minimal guarantees hold however the case ends, and success
  guarantees hold "when the use case ends successfully, regardless of which path it takes" [24]; a non-functional
  requirement that applies to many use cases is linked, not copied, since OpenUP asks "Are these nonfunctional
  requirements applicable to many use cases?" and says "consider capturing them in the supporting Requirements
  Specification to simplify maintenance" [24]; every actor step gets a system response ([19], [20]); each step is
  free of "technical details and inadvertent design decisions" [24]; an extension condition says what was
  detected (the title of Guideline 11, [3], [5]); a step outside the goal means the case should split, which
  Brandenburg puts as "This mistake is an indicator that the use case needs to be split into more than one use
  case." [20]; terms are used consistently, since "A final mistake that can cause significant confusion is when
  BAs use terms inconsistently." [20]; error conditions are not left out, Sehlhorst's "Unanticipated error
  conditions." [19]; actors are defined, his "Undefined actors." [19]; and a business rule is referred to by
  identifier (above).
- **To the companion, as the downstream hand-off, not a section:** each path through the flows can become a test.
  Pratama et al. derive tests with "one-to-one mapping between control flow paths and test cases" [26], and
  Strembeck and Zdun write that "Tests are derived from use case scenarios via continuous refinement." [27]. That
  is what `acceptance-criteria` and `test-case` do with this document; it belongs in the companion's
  Relationships section.
- **Declined, or left to the author:** a master inventory of a project's use cases [25], which lives outside any
  one specification and is the use case model this bundle does not template (contested item 7); a separate
  Assumptions field, which only Wiegers carries [7], so an assumption goes under Open Issues; an accessibility
  field, which no source read carries; data definitions, routed to `data-dictionary` [20]; and a business-rules
  section (above).

**Licences.** The 1998 template says "You have permission to copy and distribute the documents as long as you
reference the source of the originals." [1]; the same page, in a sentence read in raw text but not submitted as a
quotation, also allows a team to use and vary the template on its own projects without reference [1]. Wiegers'
template says "Permission is granted to use, modify, and distribute this document" [7], under his 1999 copyright.
This log quotes no reuse permission for the draft [3], the Pearson pages [5], RUP [8], W3C [9], NYU [10],
ArgonDigital [11], the practitioner reproduction [12], Use-Case 3.0 [13] or the foundation [14]. The templates' GOOD
and WEAK text must not adapt any source's wording or worked scenario, including Cockburn's Buy Something and Buy
Goods examples, Ambler's seminar enrolment, Girvan's library tracker, Brandenburg's new-account button and
Rosenberg's file save.

**The example.** It elaborates the "set a default saved view" story, as the acceptance criteria name it
(`templates/acceptance-criteria/acceptance-criteria_example.md:11`), and it is dated `created: "2026-06-20"` and
`updated: "2026-06-30"`. That places it after the story it elaborates (created 2026-06-18,
`templates/user-stories/user-stories_example.md:8`) and before the acceptance criteria it feeds (created
2026-06-22, `templates/acceptance-criteria/acceptance-criteria_example.md:8`), and its `updated` date matches both
(`user-stories_example.md:9`, `acceptance-criteria_example.md:9`). Its owner is Priya Nair (PM, Reporting), the
owner every chain sibling names (`user-stories_example.md:5`, `acceptance-criteria_example.md:5`,
`epic_example.md:4`, `prd_example.md:5`). The catalog names a business analyst as this type's owner, but no sibling
names one, and inventing a person would add a fact no sibling states. All paths below are under `templates/`.

| Fact the example must agree with | Where it is stated |
|---|---|
| Primary actor: the Recurring Analyst, "an internal or customer analyst who returns to the same dashboards daily or weekly and works within a stable set of filters" | `prd/prd_example.md:65-66` |
| The story, verbatim: "As a recurring analyst, I want to set one of my saved views as the default for a dashboard, so that the dashboard opens the way I work instead of in its generic default state." The PRD's wording differs and is not the one to quote | `user-stories/user-stories_example.md:50-51`; `acceptance-criteria/acceptance-criteria_example.md:28-29`; `prd/prd_example.md:84-85` |
| The goal's motive: "removes the daily re-filtering tax for recurring analysts" | `user-stories/user-stories_example.md:69` |
| The four functional criteria: "I can mark exactly one of my saved views as the default for a given dashboard."; "Marking a new view as default un-marks the previous default automatically."; "Opening the dashboard loads my default view instead of the generic default state."; "The default is mine alone; it does not change the default for any other user." | `acceptance-criteria/acceptance-criteria_example.md:33-36` |
| The two scenarios: "default view loads on open" (the "EMEA, last 30 days" view on the Sales dashboard) and "switching the default" (to "APAC, last 7 days") | `acceptance-criteria/acceptance-criteria_example.md:40-48` |
| Edge case, deleted filter: it "loads the still-valid filters and shows a clear message naming the missing filter, rather than failing to load". The literal message copy is the PRD's: a clear "some filters in this view no longer exist" message, "with a way to fix and re-save" | `acceptance-criteria/acceptance-criteria_example.md:52-54`; `prd/prd_example.md:119-120` |
| Edge case, no default set: it "loads the generic default state with no error" | `acceptance-criteria/acceptance-criteria_example.md:55-56` |
| FR-2 (list and switch saved views): "List a user's saved views for a dashboard and switch between them in one action" (Must). FR-3 (set a default): "Set one view as the user's default for a dashboard; that view loads on open" (Must) | `prd/prd_example.md:98-99` |
| Epic child stories SV-3, "List a user's own views and switch between them (FR-2)", and SV-4, "Set one view as the dashboard's default (FR-3)". Sharing is SV-5, "Share a view with a team, permission-checked (FR-4)" | `epic/epic_example.md:79-80, 82` |
| The Views control: "A "Views" control sits at the top of every dashboard", and its menu offers to "switch between saved views, set a default, and share"; the epic's dependency D-03 (an updated menu component) names the same control | `prd/prd_example.md:72-74`; `epic/epic_example.md:114` |
| The "set as default" control is "keyboard-operable and screen-reader labeled (WCAG 2.2 AA)" | `acceptance-criteria/acceptance-criteria_example.md:61` |
| Performance: loading a default view on open "completes within 1 second at p95 (illustrative target)" | `acceptance-criteria/acceptance-criteria_example.md:60` |
| Preconditions a sibling states: "Assumes per-user preference storage (shipped Q1)", and the save-view story "is a sequenced prerequisite" | `acceptance-criteria/acceptance-criteria_example.md:66`; `user-stories/user-stories_example.md:67` |
| The system under design, for Scope: "Dashboards in Acme Analytics" | `epic/epic_example.md:33` |
| The open issue: "should a Team Lead be able to set a team default, or only personal defaults? Owner: Priya, needed before Phase 2." The PRD carries the same question, owner and deadline | `user-stories/user-stories_example.md:85-86`; `prd/prd_example.md:168` |
| Schedule: Phase 1 ships "private views only (FR-1 to FR-3, FR-5) behind a feature flag" | `prd/prd_example.md:156` |

**The hand-off to the acceptance criteria, as the boundaries dimension mapped it:** the first three functional
criteria (`acceptance-criteria_example.md:33-35`) and both scenarios (`:40-48`) are steps of the main success
scenario; "The default is mine alone" (`:36`) is a success guarantee, not a step; the deleted-filter edge case
(`:52-54`) is an exception extension and the no-default edge case (`:55-56`) an alternative extension; the
performance criterion (`:60`) belongs in Related Information; and the accessibility criterion (`:61`) has no field
in any source's template, so the example must not invent one.

**Inconsistencies between the sibling examples.** The boundaries dimension found none among the four core examples
on names, IDs, dates, FR numbers or wording, and one difference of granularity: the PRD gives the error message's
literal copy (`prd_example.md:119-120`) where the acceptance criteria paraphrase it
(`acceptance-criteria_example.md:52-54`). The example quotes the PRD's copy and writes no new wording. **This log
adds two that the dimension did not raise.** First, the story card says "how "default" is surfaced in the UI is
open" (`user-stories_example.md:68`), while the acceptance criteria name a "set as default" control
(`acceptance-criteria_example.md:61`) and the PRD's Views menu offers to "set a default" (`prd_example.md:72-73`).
The example writes its steps at the level of intention, as [3] asks, and names only the Views control the PRD
names, which leaves that question where the siblings left it. Second, the two performance targets agree on 1 second
at p95 but measure different events: the acceptance criteria measure loading a default on open
(`acceptance-criteria_example.md:60`), and the PRD measures switching to a saved view (`prd_example.md:108`). The
example's performance target cites the acceptance criteria.

**Facts the example will need that no sibling states.** The build writes each as the example's own and the build
report lists them: the trigger event, for which the nearest sibling fact is the Views control
(`prd_example.md:72`); the goal level, where user-goal is this log's reading and no sibling states a level; a
minimal guarantee beyond what the edge cases imply, since the siblings say the dashboard still loads
(`acceptance-criteria_example.md:52-56`) but nowhere say whether the previous default survives a failed attempt to
set a new one; any stakeholder beyond the primary actor, where the only sibling facts are the Team Lead as
secondary persona (`prd_example.md:65-67`) and "any other user" whose default must not change
(`acceptance-criteria_example.md:36`); and a frequency of use, where the PRD gives only the persona's daily or weekly
visits (`prd_example.md:65-66`), not how often a default is set. Any number beyond those in the table is labelled
illustrative.

**What it must not do.**

- **It must not add a shared-view permission edge.** The acceptance criteria say the story "Does not cover sharing,
  which has its own story" (`acceptance-criteria_example.md:66-67`), and sharing is SV-5 (`epic_example.md:82`).
  The PRD's "Permission edge" state sits directly below the deleted-filter state the example uses
  (`prd_example.md:121-122`), and it belongs to sharing (FR-4, share a view, `prd_example.md:100`; Phase 2,
  `prd_example.md:157`). A drafter copying the PRD's states list will be tempted to take both.
- **It must not put team defaults in scope.** They are out of scope (`acceptance-criteria_example.md:65-66`) and
  appear only as the open issue.
- **It must not invent facts absent from the siblings**: no new message wording, persona, person, control, metric
  or target beyond the table and the list above.
- **It must not carry a business-rules section**, and the templates carry none (see the section design above).
- **The templates' guidance text must not use the shared scenario's proper nouns.** Keep these out of every WHAT,
  WHY, ASK, GOOD, WEAK and TRAP comment, and grep the drafted templates for them before review: Saved Views;
  Recurring Analyst; Team Lead; Priya Nair, Marcus Bell, Dana Osei and Elena Cho; the Views control and the "set as
  default" control; SV-0 to SV-7, FR-1 to FR-6 and D-01 to D-03; Time to Insight; "generic default"; and "EMEA,
  last 30 days" and "APAC, last 7 days". This log adds three that the boundaries dimension did not list: the Sales
  dashboard (`acceptance-criteria_example.md:41-42`), Acme Analytics (`epic_example.md:33`) and the re-filtering
  tax (`user-stories_example.md:69`). The same names recur across many other bundles' examples, so finding them
  elsewhere does not make them safe in a template.

---

## Sources

### CANON: COCKBURN'S TEMPLATE, FORMALITY LEVELS AND WRITING RULES

**[1] Alistair Cockburn, Basic Use Case Template (HaT TR.96.03a, v.2, 1998-10-26) - University of Otago mirror.** primary. **fetched-and-verified.**
`https://cs.otago.ac.nz/coursework/cosc461/uctempla.htm`
Supports: the 1998 field list, in order, in both the plain-text and table renderings, plus the worked 'Buy Goods' example
Quotable: "You have permission to copy and distribute the documents as long as you reference the source of the originals."
Quotable: "The template has the sections: name (which is the goal), goal in context, scope, level, trigger, pre- and postconditions, main course, extensions, sub-variations, and other characteristic data for the use case."
Quotable: "Use Case: <number> <the name should be the goal as a short active verb phrase>"
Quotable: "Goal in Context: <a longer statement of the goal, if needed>"
Quotable: "Scope: <what system is being considered black-box under design>"
Quotable: "Level: <one of: Summary, Primary task, Subfunction>"
Quotable: "Preconditions: <what we expect is already the state of the world>"
Quotable: "Success End Condition: <the state of the world upon successful completion>"
Quotable: "Failed End Condition: <the state of the world if goal abandoned>"
Quotable: "Primary Actor: <a role name for the primary actor, or description>"
Quotable: "Trigger: <the action upon the system that starts the use case, may be time event>"
Quotable: "<put here the steps of the scenario from trigger to goal delivery, and any cleanup after>"
Quotable: "<put here there extensions, one at a time, each refering to the step of the main scenario>"
Quotable: "<step altered> <condition> : <action or sub.use case>"
Quotable: "SUB-VARIATIONS <put here the sub-variations that will cause eventual bifurcation in the scenario>"
Quotable: "RELATED INFORMATION (optional) Priority: <how critical to your system / organization> Performance Target: <the amount of time this use case should take> Frequency: <how often it is expected to happen> Superordinate Use Case: <optional, name of use case that includes this one> Subordinate Use Cases: <optional, depending on tools, links to sub.use cases> Channel to primary actor: <e.g. interactive, static files, database> Secondary Actors: <list of other systems needed to accomplish use case> Channel to Secondary Actors: <e.g. interactive, static, file, database, timeout>"
Quotable: "OPEN ISSUES (optional) <list of issues about this use cases awaiting decisions>"
Quotable: "SCHEDULE Due Date: <date or release of deployment>"
Quotable: "3a. Company is out of one of the ordered items: 3a1. Renegotiate order. 4a. Buyer pays directly with credit card: 4a1. Take payment by credit card (use case 44) 7a. Buyer returns goods: 7a. Handle returned goods (use case 105)"
Quotable: "(Note: The book Writing Effective Use Cases made a couple of small changes to these templates, most notably renaming "Failed End Condistion" to the more correct "Minimal Guarantee" and "Subvariation" to the more correct "Technology and Data Variations List.""
Quotable: "Sub-Variations"

**[2] Alistair Cockburn, Use Case Template (same HaT TR.96.03a text) - Bentley University mirror, PDF.** primary. **fetched-and-verified.**
`https://cis.bentley.edu/lwaguespack/CS360_Site/Downloads_files/Use%20Case%20Template%20(Cockburn).pdf`
Supports: independent confirmation of the identical 1998 field set and field order, with no 'stakeholder' mentions and no post-2001 renaming note
Quotable: "Document: TR.96.03a This Version Date: October 26, 1998 Version: 2 Previous Version Date: April 26, 1996"
Quotable: "The template has the sections: name (which is the goal), goal in context, scope, level, trigger, pre- and postconditions, main course, extensions, sub-variations, and other characteristic data for the use case."
Quotable: "Use Case: <number> <the name should be the goal as a short active verb phrase> -------------------------------------------------CHARACTERISTIC INFORMATION Goal in Context: <a longer statement of the goal, if needed> Scope: <what system is being considered black-box under design> Level: <one of: Summary, Primary task, Subfunction> Preconditions: <what we expect is already the state of the world> Success End Condition: <the state of the world upon successful completion> Failed End Condition: <the state of the world if goal abandoned> Primary Actor: <a role name for the primary actor, or description> Trigger: <the action upon the system that starts the use case, may be time event>"

**[3] Alistair Cockburn, Writing Effective Use Cases, pre-publication draft #3, edit date 2000.02.21 (published by Addison-Wesley, c.2001).** primary. **fetched-and-verified.**
`https://kurzy.kpi.fei.tuke.sk/zsi/resources/CockburnBookDraft.pdf`
Supports: formality-level definitions, goal levels and design scope, the draft's own fully-dressed field list (its 'Use Case 7', not the final book's 'Use Case 24'), confirmation that Stakeholders & Interests / Minimal and Success Guarantees already exist in this pre-publication draft, and the Writing Process / Reminders step list
Quotable: "A casual use case is one written in simple, paragraph, prose style. It is likely to be missing project information associated with the use case, and is likely to be less rigorous in its description than a fully dressed use case."
Quotable: "A fully dressed use case is written with one of the full templates, identifying actors, scope, level, trigger condition, precondition, and all the rest of the template header information, plus project annotation information."
Quotable: "The brief of a use case is a 2-6 sentence description of the use case behavior, mentioning only the most significant activity and failures."
Quotable: "There must be at least two, a casual one for low-ceremony projects, and a fully dressed one for higherceremony projects."
Quotable: "USE CASE 7: FULLY DRESSED USE CASE TEMPLATE <NAME> <the name should be the goal as a short active verb phrase> Context of use: <a longer statement of the goal, if needed, its normal occurrence conditions> Scope: <design scope, what system is being considered black-box under design> Level: <one of: Summary, User-goal, Subfunction> Primary Actor: <a role name for the primary actor, or description> Stakeholders & Interests: <list of stakeholders and key interests in the use case> Precondition: <what we expect is already the state of the world> Minimal Guarantees: <how the interests are protected under all exits> Success Guarantees: <the state of the world if goal succeeds> Trigger: <what starts the use case, may be time event>"
Quotable: "the numbering convention in the extensions sections involving combinations of digits and letters (e.g., 2a, 2a1, 2a2 and so on)"
Quotable: "one column of text (not a table), * numbered steps, * no if statements"
Quotable: "Write something readable. Casual,readable use cases are still useful, whereas unreadable use cases won't get read."
Quotable: "For each step: Show a goal succeeding. Highlight the actor's intention, not the user interface details. Have an actor pass information, validate a condition, or update state. Write between-step commentary to indicate step sequencing (or lack of). Ask 'why'to find a next-higher level goal."
Quotable: "7. Capture stakeholders and interests, preconditions and guarantees. The system will ensure the preconditions and guarantee the interests."
Quotable: "8. Write the main success scenario (MSS). Use 3 to 9 steps to meet all interests and guarantees."
Quotable: "9. Brainstorm and exhaustively list the extension conditions. Include all that the system can detect and must handle."
Quotable: "10. Write the extension-handling steps. Each will ends back in the MSS, at a separate success exit, or in failure."
Quotable: "User-goals (blue, sea-level )"
Quotable: "The user goal is the goal of greatest interest. It is the goal the primary actor has in trying to get work done, or the user has in using the system at all. It corresponds to "elementary business process" in the business process engineering literature."
Quotable: "One person, one sitting (2-20 minutes)."
Quotable: "Summary level (white, cloud / kite )"
Quotable: "Summary1-level goals involve multiple user goals."
Quotable: "Subfunctions (indigo/black, underwater /clam )"
Quotable: "Subfunction-level goals are those required to carry out user goals. Include them only as you have to."
Quotable: "Design scope is the extent of the system - I would say "spatial extent" if software took up space. It is the set of systems, hardware and software, that you are charged with designing or discussing."
Quotable: "A business use case has the enterprise as its design scope."
Quotable: "A system use case has a computer system as its design scope."
Quotable: "Recall, in the following, that a black-box use case does not discuss the internal structure of the system under discussion, while a white-box use case does."
Quotable: "A stakeholder is someone with a vested interest in the behavior of the use case, even if they never interact directly with the system."
Quotable: "A stakeholder is someone or something with a vested interest in the behavior of the system under discussion (SuD)."
Quotable: "A use case captures a contract between the stakeholders of a system about its behavior."
Quotable: "Guideline 1: It uses simple grammar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94"
Quotable: "Guideline 11: The condition says what was detected. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106"
Quotable: "Guideline 12: Condition handling is indented. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111"
Quotable: "USE CASE 4: BUY SOMETHING (CASUAL VERSION)"
Quotable: "USE CASE 5: BUY SOMETHING (FULLY DRESSED VERSION)"
Quotable: "led to the explanations in this book and the Stakeholders & Interests model, which is new in this book"

**[4] Alistair Cockburn, Writing Effective Use Cases, pre-publication draft #3 - 'Reminders' cheat-sheet pages i and 2, Duke course extract.** primary. **fetched-and-verified.**
`https://courses.cs.duke.edu/spring23/compsci308/readings/cockburn_use_cases.pdf`
Supports: the condensed step-writing rules and the 12-step Writing Process list, the same draft as source 3, in a two-page extract on a different host (its front-matter Reminders pages), read in full
Quotable: "Work breadth-first, from lower precision to higher precision. Precision Level 1: Primary actor's name and goal Precision Level 2: The use case brief, or the main success scenario Precision Level 3: The extension conditions Precision Level 4: The extension handling steps"
Quotable: "For each step: Show a goal succeeding. Highlight the actor's intention, not the user interface details. Have an actor pass information, validate a condition, or update state. Write between-step commentary to indicate step sequencing (or lack of). Ask 'why'to find a next-higher level goal."
Quotable: "8. Write the main success scenario (MSS). Use 3 to 9 steps to meet all interests and guarantees."
Quotable: "10. Write the extension-handling steps. Each will ends back in the MSS, at a separate success exit, or in failure."
Quotable: "For Goal Level, alternatively, append one of these characters to the use case name: Append "+" to summary use case names. Append "!" or nothing to user-goal use case names. Append "-" to subfunction use case names."

**[5] Alistair Cockburn, Writing Effective Use Cases (Addison-Wesley, 2001, ISBN 0201702258) - Pearson free sample pages (table of contents, preface, index, and scattered body excerpts).** primary. **fetched-and-verified.**
`https://ptgmedia.pearsoncmg.com/images/9780201702255/samplepages/0201702258.pdf`
Supports: the book's chapter/section numbering and titles (6.1-6.4 Preconditions/Guarantees, 8.1-8.3 Extensions, the named Guidelines 1-18), the preface's statement that Stakeholders and Interests is new relative to the Actors-and-Goals model, and index confirmation of page locations for Minimal/Success guarantees and the pp.119-120 fully-dressed template heading - but NOT the pp.119-120 template body itself, which this PDF does not include
Quotable: "6.1 Preconditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81 6.2 Minimal Guarantees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83 6.3 Success Guarantee . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84"
Quotable: "Guideline 11: Make the Condition Say What Was Detected . . . . . . . . . . . . . . . . . . . . . 102"
Quotable: "Guideline 12: Indent Condition Handling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108"
Quotable: "Use Case 24 (Fully Dressed Use Case Tem-plate), 119-120"
Quotable: "led to the explanations in this book and to the Stakeholders and Interests model, which is a new idea presented here."
Quotable: "Casual use cases, 7-9, 97, 120, 218"
Quotable: "Minimal guarantees, 83-85, 248"
Quotable: "led to the explanations in this book and to the Stakeholders and Interests model, which is a new idea presented here"
Quotable: "Minimal Guarantees"

**[6] Alistair Cockburn, 'Use Cases, Ten Years Later' (STQE magazine, Mar/Apr 2002).** primary. **fetched-and-verified.**
`https://www.dsc.ufcg.edu.br/~garcia/cursos/ger_processos/seminarios/Crystal/Use%20Cases,%20Ten%20Years%20Later.htm`
Supports: what the formalist/informalist split did to use cases in practice, the standard mistakes (too much detail, UI specifics, oversized main scenarios), the use-case/test-case/design-doc boundary, and a second independent wording of brief/casual/fully-dressed
Quotable: "Jacobson replied, "Oh, I have a formal model for use cases, all right. The only problem is that no one wants to use it.""
Quotable: "In Writing Effective Use Cases, I name three degrees of detail in writing use cases: brief, casual, and fully dressed."
Quotable: "The use case brief consists of two to four sentences summarizing the use case."
Quotable: "The casual use case consists of a few paragraphs of text, covering the items mentioned above."
Quotable: "The fully dressed use case features the long template with fields for stakeholders, minimum guarantees, postconditions, business rules, performance constraints, and so on."
Quotable: "There are many kinds of mistakes a use case writer can make. The two most common and most costly to the project are including too many details and including UI specifics."
Quotable: "The greatest value of the use case does not lie in the main scenario, but in alternative behaviors."
Quotable: "Use cases are not test plans or test cases. They are missing the data values needed for test cases."
Quotable: "As design documentation, the use case describes: the user does this; some first component does a set of things; the component forwards a request to a second component; and so on."
Quotable: "People will misuse them, teach them incorrectly, warp the interpretation, and blame the resulting mess on the use case form."
Quotable: "had they simply written down the stakeholders and interests for each use case early on, they would have avoided an entire category of mistakes"
Quotable: "yet to write a main success scenario longer than nine steps"
Quotable: "by the time I get subgoals at a good level and remove the design specifics"

### STRUCTURE: THE OTHER PUBLISHED TEMPLATES

**[7] Karl E. Wiegers, "Use Cases for <Project>" / "Guidance for Use Case Template" (Process Impact, 1999), University of Kansas course mirror.** primary. **fetched-and-verified.**
`https://people.eecs.ku.edu/~saiedian/812/Lectures/UML/use-case-template1.pdf`
Supports: Full verbatim field list and field-by-field guidance for the Wiegers use case template
Quotable: "Give each use case a unique numeric identifier, in hierarchical form: X.Y."
Quotable: "An actor is a person or other entity external to the software system being specified who interacts with the system and performs use cases to accomplish tasks."
Quotable: "List any activities that must take place, or any conditions that must be true, before the use case can be started. Number each precondition."
Quotable: "Describe the state of the system at the conclusion of the use case execution. Number each postcondition."
Quotable: "Estimate the number of times this use case will be performed by the actors per some appropriate unit of time."
Quotable: "Number each alternative course using the Use Case ID as a prefix, followed by “AC” to indicate “Alternative Course”. Example: X.Y.AC.1."
Quotable: "Number each exception using the Use Case ID as a prefix, followed by “EX” to indicate “Exception”. Example: X.Y.EX.1."
Quotable: "List any other use cases that are included (“called”) by this use case."
Quotable: "Identify any additional requirements, such as nonfunctional requirements, for the use case that may need to be addressed during design or implementation."
Quotable: "List any assumptions that were made in the analysis that led to accepting this use case into the product description and writing the use case description."
Quotable: "List any additional comments about this use case or any remaining open issues or TBDs (To Be Determineds) that must be resolved."
Quotable: "Permission is granted to use, modify, and distribute this document"

**[8] Rational Unified Process, "Use-Case Specification: <Use-Case Name>" template, UFPE mirror of the RUP web templates.** primary. **fetched-and-verified.**
`https://cin.ufpe.br/~if682/RUP/webtmpl/templates/req/rup_ucspec.htm`
Supports: Full verbatim section list and in-section guidance for the RUP use-case specification template
Quotable: "1.1 Brief Description"
Quotable: "2.1 Basic Flow"
Quotable: "2.2 Alternative Flows"
Quotable: "A precondition of a use case is the state of the system that must be present prior to a use case being performed."
Quotable: "A postcondition of a use case is a list of possible states the system can be in immediately after a use case has finished."
Quotable: "6. Extension Points"
Quotable: "[Definition of the location of the extension point in the flow of events.]"
Quotable: "This use case starts when the actor does something."
Quotable: "An actor always initiates use cases."
Quotable: "A special requirement is typically a nonfunctional requirement that is specific to a use case, but is not easily or naturally specified in the text of the use case"

**[9] W3C eGovernment Interest Group, "Use Case Template" (archived W3C eGov Wiki, last modified 2 December 2008).** standards. **fetched-and-verified.**
`https://www.w3.org/egov/wiki/Use_Case_Template`
Supports: Full verbatim field list for the W3C eGovernment use case template, which is a different genre (standards-opportunity proposal) than an actor-scenario specification
Quotable: "A number we can use to reference the Use Case - just in case the Use Case Name is changed."
Quotable: "Define the problem that the standard aims to solve and proposed benefits."
Quotable: "Identification or description of the target population of the use case"
Quotable: "A description of the Use case, in terms of interactions of the different actors involved."
Quotable: "A set of problems or limitations that can be identified at this point."
Quotable: "Known related initiatives"
Quotable: "A conclusion on whether the use case has the critical mass for recommendation, and a justification"

**[10] NYU Courant CS, CSCI-GA.2440-001 (Spring 2018) course handout, "Use Case Specification" template.** practitioner. **fetched-and-verified.**
`https://cs.nyu.edu/~jcf/classes/CSCI-GA.2440-001_sp18/handouts/UseCaseTemplate.pdf`
Supports: Full verbatim one-page field list for a university software-engineering course's use case specification template, a fifth published template distinct from Wiegers, RUP, W3C and Cockburn
Quotable: "Use Case ID: {This should be coded to identify the owning team and the level of the use case}"
Quotable: "Relevant requirements: {Reference to other relevant requirements documents.}"
Quotable: "Primary Actor: {Main sub-system/entity that initiates use}"
Quotable: "Basic Flow or Main Scenario: {Numbered flow of events: 1 The user initiates an action by… 2 The system responds by...}"
Quotable: "Extensions or Alternate Flows: {This section presents variations on this use case. It presents those use cases that have an extends relation with the current use case.}"
Quotable: "Exceptions: {This section describes all error conditions that can arise in the use case.}"
Quotable: "Related Use Cases: {use cases that are either usually performed just before or after the current use.}"
Quotable: "Revision History Date Description By"

**[11] ArgonDigital (requirements-engineering consultancy/vendor), "RML Use Case Template" page.** vendor. **fetched-and-verified.**
`https://argondigital.com/resource/tools-templates/rml-use-case-template`
Supports: Confirms a sixth named organization publishing a use case template and its main/alternate/exception-course terminology; the actual field table itself sits behind a lead-capture download form and was not retrievable, so no field-list quote beyond the surrounding prose can be sourced to this page
Quotable: "The following use case template is the one we use when developing Use Cases. It contains all of the relevant information we need to capture in one handy table."
Quotable: "A common point of confusion in Use Cases is the difference between the main course, an alternate course, and an exception course."
Quotable: "Note that some of the alternate courses refer to another use case, because login and account creation are complicated enough to be their own use cases, and they aren’t unique to the wishlist process."

**[12] Practitioner reproduction of Alistair Cockburn's fully-dressed use case field list (not Cockburn's own text), distributed as a Claude skill guide "Cockburn use case writing guide".** practitioner. **fetched-and-verified.**
`https://cdn.jsdelivr.net/npm/usecases-skill@0.1.0/skills/usecases/use-case-guide.md`
Supports: Verbatim fully-dressed template field list, extension/alternative numbering convention, and stated lightest-usable forms, as reproduced by this practitioner guide -- never attributable to Cockburn's own book text
Quotable: "Title: <verb + goal, active form> - "Place an order""
Quotable: "Level: user-goal"
Quotable: "summary"
Quotable: "subfunction"
Quotable: "Scope: <what black box>"
Quotable: "Primary actor: <who wants the goal>"
Quotable: "Stakeholders and interests:"
Quotable: "- <Stakeholder>: <what they want from this UC>"
Quotable: "Preconditions: <what is guaranteed true BEFORE the start>"
Quotable: "Min. guarantees: <what the system promises even on failure>"
Quotable: "Success guarantees: <the state of the world at success>"
Quotable: "Trigger: <event that starts the UC>"
Quotable: "Brief - one paragraph, the essence of the scenario. Early stage or backlog."
Quotable: "Casual - several free-form paragraphs that cover the main path and the main deviations."
Quotable: "Fully dressed - the full template with every field (below). For critical or complex UCs."
Quotable: "Keep most UCs at brief or casual. Fully-dress only the important ones."
Quotable: "Notation: step number + letter. `3a`, `3b` - different conditions at step 3; `3a1`, `3a2` - steps inside condition `3a`."
Quotable: "**3 to 9 steps** per UC. More than that, and you probably want to move part into a subfunction."

### LINEAGE: JACOBSON, UML AND USE-CASE 3.0

**[13] Ivar Jacobson, Ian Spence, Keith de Mendonca - "Use-Case 3.0: The Guide to Succeeding with Use Cases" (v1.00, December 2024, Ivar Jacobson International).** practitioner. **fetched-and-verified.**
`https://ss-usa.s3.amazonaws.com/c/308454236/media/42906756d195e3bed93712764146367/Use-Case%203.0%20v1.0%20candidate%202.13.pdf`
Supports: Origin claim (a); use-case slices, lightweight/agile use (c); methodology ties to waterfall, Scrum, SAFe, and author biographies tying Jacobson to RUP (d)
Quotable: "They have been used to drive the development of software systems since their initial introduction by Ivar Jacobson at OOPSLA in 1987."
Quotable: "Object-oriented software development in an industrial environment Ivar Jacobson The first published paper to describe Use Cases. ● Publisher: In Conference Proceedings of Object-oriented Programming Systems, Languages, and Applications - OOPSLA 87 (1987)"
Quotable: "Object-Oriented Software engineering: A Use Case Driven Approach Ivar Jacobson, Magnus Christerson, Patrik Jonsson, Gunnar Overgaard. The original book that introduced use cases to the world. ● Publisher: Addison-Wesley Professional; revised edition (July 10, 1992)"
Quotable: "This guide describes how to apply use cases to capture system requirements in an agile and scalable fashion."
Quotable: "We define a Use-Case Slice as: A slice of a use case that provides clear value to the development stakeholders. It includes a requirements slice specifying the interaction with its actor(s) and the actions taken by the use case, and a test slice verifying the requirements."
Quotable: "The two most common types of work item we see in use now are user stories (for agile teams) and Tasks (for waterfall project teams). Regardless of the types of work item to be generated, the basic principle is the same. The important thing to note here is that Use-Case 3.0 will support, focus and complement whatever planning, work management and development approaches your teams have selected."
Quotable: "The Use-Case Foundation principles were published in 2024 to remind practitioners to capture "just-enough" detail, "just-in-time", and "deliver in stages"; the development of use cases should be done in a way that suits the circumstances - in some cases in a lightweight and agile way, in other cases in a rigorous way."
Quotable: "Dr. Ivar Jacobson is a father of components and component architecture, use cases, aspect-oriented software development, modern business engineering, the Unified Modeling Language and the Rational Unified Process."
Quotable: "As Chief Technology officer at Ivar Jacobson International, Ian Spence specialized in the agile application of the Unified Process. He is a certified RUP practitioner, ScrumMaster, SAFe Fellow..."
Quotable: "The Use-Case 3.0 Foundation extends the Use-Case Foundation to add the key Use-Case 3.0 concepts of the Use-Case Slice"

**[14] Ivar Jacobson and Alistair Cockburn - "Use-Case Foundation" (version 1.1, Ivar Jacobson International / Alistair Cockburn).** practitioner. **fetched-and-verified.**
`https://alistaircockburn.com/Use%20Case%20Foundation.pdf`
Supports: What the written narrative consists of (c); methodology-neutrality - Principle 1 (d)
Quotable: "1. Use Cases apply to systems of all types and sizes: businesses, IT systems, physical systems or any combinations thereof."
Quotable: "8. The amount of detail and the format used will vary to match your circumstances: start with a sketch of the sequence of events, and add detail as and when needed."
Quotable: "9. A use case can be implemented in stages: develop and put into place some key scenarios of a use case early to capture value and feedback, add less used or less critical scenarios over time strategically."
Quotable: "The basic scenario and extensions can be described in text, as above, or in some graphical form. What is important is the accuracy of the basic scenario and its extensions and not how detailed you write out the steps and extensions."
Quotable: "The normal, happy path to value often referred to as the"
Quotable: "A list of all the special cases, alternative paths, optional steps, and errors that need to be handled."
Quotable: "Extensions are also referred to as"

**[15] Object Management Group - OMG Unified Modeling Language (OMG UML), Version 2.5.1, Clause 18 "Use Cases" (formal/2017-12-05, December 2017).** standards. **fetched-and-verified.**
`https://www.omg.org/spec/UML/2.5.1/PDF`
Supports: What UML specifies about use cases, the model elements and diagram, and the absence of a mandated textual format (b); Include/Extend relationship definitions (e); confirms the spec never ties use cases to any methodology (d)
Quotable: "UseCases are a means to capture the requirements of systems, i.e., what systems are supposed to do. The key concepts specified in this clause are Actors, UseCases, and subjects. Each UseCase's subject represents a system under consideration to which the UseCase applies. Users and any other systems that may interact with a subject are represented as Actors."
Quotable: "A UseCase is a specification of behavior. An instance of a UseCase refers to an occurrence of the emergent behavior that conforms to the corresponding UseCase. Such instances are often described by Interactions."
Quotable: "The behaviors of a UseCase can be described by a set of Behaviors (through its ownedBehavior relationship), such as Interactions, Activities, and StateMachines, as well as by pre-conditions, post-conditions and natural language text where appropriate."
Quotable: "The specific manner in which the location of an ExtensionPoint is defined is intentionally unspecified. This is because UseCases may be specified in various formats such as natural language, tables, trees, etc."
Quotable: "An Extend is a relationship from an extending UseCase (the extension) to an extended UseCase (the extendedCase) that specifies how and when the behavior defined in the extending UseCase can be inserted into the behavior defined in the extended UseCase."
Quotable: "Include is a DirectedRelationship between two UseCases, indicating that the behavior of the included UseCase (the addition) is inserted into the behavior of the including UseCase (the includingCase)."
Quotable: "The Include relationship is intended to be used when there are common parts of the behavior of two or more UseCases. This common part is then extracted to a separate UseCase, to be included by all the base UseCases having this part in common."
Quotable: "A UseCase is shown as an ellipse, either containing the name of the UseCase or with the name of the UseCase placed below the ellipse."

**[16] Martin Fowler - bliki entry "Use Case" (martinfowler.com, 3 August 2004).** practitioner. **fetched-and-verified.**
`https://www.martinfowler.com/bliki/UseCase.html`
Supports: Origin claim corroboration (a); settling the 'use case model' alias and the diagram-vs-narrative split (b); disagreement camp on the value of the UML diagram
Quotable: "Use cases are a technique for organizing and eliciting requirements. They were originally popularized by Ivar Jacobson in the late 80's and early 90's."
Quotable: "People commonly ask questions about use cases, most of which can be answered by Alistair Cockburn's book, which is by far the best book on use cases. You should read this book before using or asking questions about use cases."
Quotable: "Use cases appear in the UML in the form of use case diagrams, but these diagrams are of little value - the key value of use cases lies in the text which is not standardized in UML. So when you do use cases put your energy into the text."
Quotable: "Use case are at their best when they are short and readable. You should not be spending weeks, let alone months, generating use case documents before you begin development."

### DEBATES: STORIES VERSUS USE CASES, DETAIL, AND THE COMMON FAILURES

**[17] Mike Cohn, 'Advantages of User Stories over Requirements and Use Cases' (Mountain Goat Software, page says 'Last updated April 23rd, 2026').** practitioner. **fetched-and-verified.**
`https://www.mountaingoatsoftware.com/articles/advantages-of-user-stories-for-requirements`
Supports: (a) when stories are preferable to use cases, and why, from the stories side of the debate
Quotable: "User stories typically, but not always, and not in every case, are the best choice for teams using Scrum because they offer several advantages over use cases, requirements documents, and other ways of describing product work."
Quotable: "A use case is a generalized description of interactions between a system and one or more actors."
Quotable: "A user story is a placeholder for a future conversation."
Quotable: "Use cases are often too large to estimate usefully."
Quotable: "Lists of requirements do not usually give the reader the same overall understanding of a product that user stories do."
Quotable: "Stories describe user goals. By focusing on those goals rather than a list of product attributes, teams are more likely to design a solution that fits the real need."

**[18] Doug Rosenberg, posting to otug@rational.com, reproduced as 'Use Cases vs Requirements vs Attributes/Methods' (ootips digest, dated 30-Aug-97).** practitioner. **fetched-and-verified.**
`https://ootips.org/use-cases-vs-requirements.html`
Supports: (c) whether UI/solution-space detail belongs in a use case - Rosenberg's own worked example and defense of including it; (e) where the complexity of a use case actually lives
Quotable: "Only the first one is a properly written use case."
Quotable: "it really isn't a good idea to be doing detailed design before we understand everything the system is supposed to do"
Quotable: "Notice also that more than half the complexity of the use case occurs in the alternative courses of action; you're not done when you've written the basic course."
Quotable: "Writing the use case completely and unambiguously describes the behavior of the system, without presuming any specific design."
Quotable: "write the user manual before you write the code"
Quotable: "are identified by describing system usage from the user manual perspective"

**[19] Scott Sehlhorst, 'Top Ten Use Case Mistakes' (Tyner Blain, posted January 26, 2006).** practitioner. **fetched-and-verified.**
`https://tynerblain.com/2006/01/26/top-ten-use-case-mistakes/`
Supports: (b) named failure modes 6-10 of this post's top-ten list, plus Susan Lilly's reported critique of screenshots-in-use-cases and CRUD use cases
Quotable: "Unanticipated error conditions. The error conditions are explicitly called out in a formal use case as exception courses. When we fail to think about how things can go wrong, we take a bad situation (an error) and make it worse by leaving our users with no reasonable way to deal with the errors."
Quotable: "Overlooking system responses. When people use computers, the computers respond. ... Reading a use case should be like watching a tennis match, with activities being performed alternately by the user and the system."
Quotable: "Undefined actors. Novice and expert users have different ways of using an application."
Quotable: "Impractical use cases."
Quotable: "Out of scope use cases. If we don't define the system boundaries, or scope of our effort, we risk wasting a lot of time and money documenting irrelevant processes."
Quotable: "Inconsistency. Incorrectness. Wrong priorities. Implementation cues. Broken traceability."

**[20] Laura Brandenburg, '7 Mistakes Even the Best Make When Writing Use Cases' (Bridging the Gap).** practitioner. **fetched-and-verified.**
`https://www.bridging-the-gap.com/7-use-case-writing-mistakes/`
Supports: (b) the seven named mistakes; (c) explicit position that UI and technical/data detail do not belong in a use case
Quotable: "Using user interface details leads to ambiguity."
Quotable: "In a use case, just about every user step should have a corresponding user response or action. If it doesn't, your development team isn't clear on what the system is supposed to do to hold up its part of the bargain."
Quotable: "Common examples of technical details include: Specific data elements or data tables. Names of system components that wouldn't be visible to an ordinary end user of the system. System-triggered processes or procedures that need to run."
Quotable: "Including too many technical details can clarify things for the technical team, but breaks the flow of the use case and makes it difficult for your business stakeholders to understand and your testers to test. These details are best saved for a technical design document."
Quotable: "When it comes to data elements, a best practice is to use a data dictionary or data map to analyze the data requirements."
Quotable: "A use case should be fairly discrete. It should describe the sequence of steps (and all necessary variations) for accomplishing one specific user goal"
Quotable: "A common mistake is to include steps that happen before the pre-conditions, after the post-conditions, or are otherwise unrelated to the user's goal in the use case. This mistake is an indicator that the use case needs to be split into more than one use case."
Quotable: "A final mistake that can cause significant confusion is when BAs use terms inconsistently."
Quotable: "By far the most common mistake we see in use cases is that they use the language of the user interface to talk about the user behavior."

**[21] Lyn Girvan, CMC Partnership Consultancy, 'So, you think you know use cases?' (IRMUK conference slides, 2024).** vendor. **fetched-and-verified.**
`https://irmuk.co.uk/wp-content/uploads/2024/08/Girvan_So_You_Think_You_Know.pdf`
Supports: (a) a side-by-side comparison of use case and user story properties, attributed to Girvan's own slide (one line is an explicit Cockburn quote); (d) naming the camps on 'use cases are out of fashion' and the 2023-2024 counter-move toward a joint foundation
Quotable: ""A use case is all the ways of using a system to achieve a goal of a particular user""
Quotable: ""Use Cases have structure and cease to be useful if at too low a level, whereas user stories can decompose forever" - Alistair Cockburn 2024"
Quotable: "Tells one story"
Quotable: "Are intended to be read and shared across the organisation"
Quotable: "BR1 - No more than 100 people allowed in library at any time"
Quotable: "Why use cases have fallen out of favour"
Quotable: "Over complicated use within UML"
Quotable: "Use cases are the same as user stories"
Quotable: "Use cases are models as in use case diagram"
Quotable: "Use cases are workflow scenarios"
Quotable: "Different techniques can be deployed at different levels"

**[22] Scott W. Ambler, 'System Use Cases: An Agile Introduction' (agilemodeling.com, excerpted from The Object Primer 3rd Edition).** practitioner. **fetched-and-verified.**
`https://agilemodeling.com/artifacts/systemusecase.htm`
Supports: (c) the explicit, graded position that UI references and business-rule references belong INSIDE a formal/concrete system use case (but not an essential/business use case); (e) three levels of elaboration and the agile stopping rule
Quotable: "A use case is a sequence of actions that provide a measurable value to an actor."
Quotable: "Each use case step reflects one activity and one activity only."
Quotable: "Use case steps are written in the active voice."
Quotable: "It is very easy for use case modeling to become un-agile. To prevent this from happening you need to focus on creating artifacts that are just barely good enough, they don't need to be perfect."
Quotable: "My use cases need to be just good enough."
Quotable: "You're not writing the Magna Carta!!!!!!!"
Quotable: "A formalized system use case refers to specific user interface components-such as screens, HTML pages, or reports"
Quotable: "because business rules reflect essential characteristics of your domain that your system must implement"
Quotable: "For very simple systems without very many complex business rules"

**[23] Carlton Nettleton, 'Why Use Cases Are Still Important...with User Stories' (Applied Frameworks blog, June 26, 2014) - relaying a quoted line from an Alistair Cockburn blog post Nettleton calls a 'rant'.** practitioner. **fetched-and-verified.**
`https://agile.appliedframeworks.com/applied-frameworks-agile-blog/why-use-cases-are-still-important-with-user-stories`
Supports: (a)/(d) one directly quoted Cockburn distinction between a use case and a user story, plus Nettleton naming the push-back camp that calls use cases too heavyweight
Quotable: "That naturally received a bunch of push back from people who felt use cases were too heavyweight. Many people claimed user stories are more than sufficient for most software teams."
Quotable: "While I agree with most of the sentiments expressed about why user stories are superior, I still believe use cases are the mark of professional software engineering and their absence is a sign that a software project is in trouble."
Quotable: "A user story is synonymous with "feature" as used in the 1990s, a marker for what is to be built, fine-grained enough to fit into modern iteration/sprint periods. A use case provides a contextual view of what is to be built, serving to bind the organization together, among other things."

### THE GAP QUESTION: WHAT GOOD PRACTICE ADDS BEYOND THE COMMONEST SECTIONS

**[24] Eclipse Process Framework / OpenUP - "Checklist: Use Case".** practitioner. **fetched-and-verified.**
`https://www.utm.mx/~caff/doc/OpenUPWeb/openup/guidances/checklists/use_case_C5362874.html`
Supports: A named review checklist for use case quality distinct from the RUP template itself, and the explicit minimal-guarantee vs. success-guarantee distinction as two separate, checkable postcondition properties, plus a rule for when nonfunctional requirements belong in the use case versus in a shared requirements specification
Quotable: "If Minimal Guarantees are present, do they always happen when the use case completes, regardless of success? (A Minimal Guarantee represents a condition that will be true when the use case ends, regardless of how it terminates.)"
Quotable: "If Success Guarantees are present, do they always happen when the use case completes successfully? (A Success Guarantee represents a condition that will be true when the use case ends successfully, regardless of which path it takes.)"
Quotable: "Are nonfunctional requirements (such as performance criteria) that are applicable to the use case captured in the use case?"
Quotable: "Does each step describe how the step helps the Actors achieve their goals?"
Quotable: "Is each step technology-independent? Is it free of technical details and inadvertent design decisions?"
Quotable: "Are these nonfunctional requirements applicable to many use cases?"
Quotable: "consider capturing them in the supporting Requirements Specification to simplify maintenance"

**[25] University of Notre Dame Business Analysis Process - "Use Case Guide".** practitioner. **fetched-and-verified.**
`https://sites.nd.edu/businessanalysis/?p=230`
Supports: A pre-authoring actor/goal index step distinct from the per-use-case document, a unique identifier field for traceability, and a catch-all 'Supplemental Requirements' section explicitly naming business rules and data limitations as content the numbered flow does not carry
Quotable: "After producing the initial list of basic flows, create a master inventory list to use for further definition of the use cases (requirements) for the project. Each use case will have various attributes relating both to the use case itself and to the project. These attributes typically contain information to identify and indicate the importance and effort of the use case (e.g., priority of the use case, actors involved, complexity to develop, whether the use case is in scope for the release or identification of the iteration/sprint, if using an Agile development methodology)."
Quotable: "Each use case should have a unique identifier that can be used for quick reference and traceability."
Quotable: "This section is used to document requirements that are not directly related to the actions but is important information (e.g., business rules, data limitations, constraints, etc.) that must be considered."
Quotable: "There are two kinds of actors - primary and secondary. A Primary actor is anyone or anything that interacts with the system to gain direct benefit. A Secondary actor is anyone or anything that is involved in achieving a use case but does not gain direct benefit from the use case."

**[26] Muhammad Ridho Kurniawan Pratama, Deni Utama & Rauhil Fahmi - "Test-First Protocol for Deriving Unit Tests from Use Case Specifications" (Jurnal Nasional Teknik Elektro dan Teknologi Informasi, vol. 15 no. 1, Feb 2026).** practitioner. **fetched-and-verified.**
`https://journal.ugm.ac.id/v3/JNTETI/article/view/24073`
Supports: A named, dated academic source arguing that use case specifications, as written in practice (including student work), typically lack granular traceability, standardized structure, and alternate-flow testing, and proposing that each control-flow path through a use case's flows be mapped one-to-one to a derived test case - evidence that 'tests derivable from this use case's flows' is a property good practice adds beyond narrating the flows
Quotable: "Graduate-level observations reveal that most students operate without granular traceability, standardized structures, or alternate flow testing."
Quotable: "This study explored a structured test-first protocol that transformed use case specifications into coverage-aware test scenarios by applying object-oriented analysis and design principles."
Quotable: "The protocol successfully derived two-unit test cases with 100% basis path coverage, demonstrating complete traceability from functional requirements to unit test scenarios with one-to-one mapping between control flow paths and test cases."
Quotable: "This protocol offers a lightweight, human-centric approach promoting testability, traceability, and strong semantic alignment between requirements and implementation."

**[27] Mark Strembeck & Uwe Zdun - "Scenario-based component testing using embedded metadata" (Testing of Component-Based Systems and Software Quality, Gesellschaft fur Informatik, 2004).** practitioner. **fetched-and-verified.**
`https://dl.gi.de/handle/20.500.12116/28495`
Supports: A second, independent academic source (2004, older and distinct in time from the 2026 Pratama paper) treating a test as a formalized, executable description of a use-case scenario, and proposing runtime traceability links from use cases and scenarios to test cases as embedded metadata - corroborating that deriving and tracing tests from the use case's own scenarios is a recurring good-practice addition, not a one-off idea. Only the abstract/record page was read; the full paper text (PDF) was not retrieved, so this entry supports the existence and framing of the idea, not any deeper methodological detail
Quotable: "In our approach, a test is defined as a formalized and executable description of a scenario. Tests are derived from use case scenarios via continuous refinement."
Quotable: "Our approach provides a model-based mapping of use cases and scenarios to test cases, as well as (runtime) traceability of these links."
