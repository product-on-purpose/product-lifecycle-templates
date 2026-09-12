# `spike-report`: the admission-test evidence

**Supporting evidence for a decision that is NOT YET MADE.** This file records what a six-dimension research
pass found when it applied [ADR 0030](decisions/0030-templating-scope-markdown-documents.md)'s admission test
to `spike-report`, and it stops there, because **whether a type is in scope at all is a maintainer decision**
and this evidence does not settle itself.

It is written in the same format a research log uses, following
[`prototype-brief-admission-evidence.md`](prototype-brief-admission-evidence.md), so the question can be
reopened without re-fetching. The bundle is not built, so there is no `templates/spike-report/`.

**72 unique sources**, of which **61 fetched-and-verified**, 5 url-confirmed-not-read and 6 not-retrieved,
across six research dimensions (90 source records before de-duplication; the source-ownership rule saved 18
re-reads). Only `fetched-and-verified` sources may be quoted, and the same honest-retrieval contract applies
here as in any bundle.

---

## The verdict: ADMITTED, barely, and not at the origin

**One named source publishes a spike report as a written document, and the term's own inventors publish the
opposite.**

**For admission.** Microsoft's public, actively maintained **Code with Engineering Playbook** states:
"Generally the deliverable from a Technical Spike should be a document detailing what was evaluated and the
outcome of that evaluation" - and links a fill-in **Template: Technical Spike** with concrete sections
(*Goal / Method / Evidence / Conclusions / Next Steps*, plus *Conducted by*, *Backlog Work Item*, *Sprint*).
Both pages were verified **against the raw markdown in the GitHub repository**, not just the rendered site,
confirming they are live maintained files rather than an archived curiosity. That is a named source
publishing the artifact, which is exactly what ADR 0030 asks for.

**Against admission, and it is the canon.** Ward Cunningham's own c2 wiki account - the primary source,
where he credits Kent Beck with coining the term on the Chrysler C3 project - describes a spike solution
purely as **code**: *"Write the smallest possible code that could be said to perform a function independent
of existing mechanism,"* with Ron Jeffries quoted there as *"We plan to throw away the code, although
sometimes something is salvaged."* Neither core c2 page mentions writing anything down. **Mike Cohn**, the
most-cited living practitioner on the subject, describes spikes purely as a knowledge-producing activity
with no mention of a report, summary or template. Don Wells' 1999 ExtremeProgramming.org page prescribes no
report format either.

**What is not evidence, checked and discarded.** SAFe's Enabler Story framing implies an inspectable
artifact, but the publicly readable page **never uses the words "document" or "report"** and the deeper
content is behind a login, so it cannot support admission. The widely repeated phrase *"documented finding,
a decision, a proof-of-concept, or an architecture recommendation"* traces **not** to SAFe or to a notable
practitioner but to **training-vendor content marketing**. One individual's GitHub repository does maintain
`spike_plan_template.md` and `spike_outcome_template.md`, proving the practice exists informally, but that
author is not a named practitioner and does not meet the bar this library applies.

**So the honest shape is: exactly one qualifying named source, standing against the term's inventors, 25
years downstream, without citing or reconciling the canon it descends from.** It should not be reported as a
clean admission backed by multiple independent sources. Whether one engineering-playbook page clears the bar
that rejected `prototype-brief` is the maintainer's call.

### How this compares to the precedent

`prototype-brief` failed because prototyping practice was everywhere and a commissioning **document** was
nowhere - zero qualifying sources. `spike-report` is **not** that shape. Spike practice is everywhere **and
there is one verified, named, current source publishing the document with a template.** The question is
whether one is enough, which is a different question from the one ADR 0035 answered.

---

## The finding that would shape the bundle, if it is built

**Every template omits it. Every good filled report includes it anyway.**

Two dimensions searched different populations and appeared to contradict each other. They do not, and the
difference is the most useful thing in this research.

- **Blank templates (8 read in full).** *Not one* uses a heading meaning "what we deliberately did not
  investigate" or "out of scope." The near-null is real.
- **Filled, real spike reports (14 read in full, raw bytes fetched and verified line by line).** An
  explicit, named non-scope section is **the single most consistent element the naive four-part shape
  omits.** Four independent, unrelated projects supply it under their own headings:
  `## Out of scope for this spike`, `Non-goals for now`, `## Not covered here`, and `Follow-ups (deferred,
  not in v1)` - the last distinguished from a separate `## Limitations` section, because *deferred* means
  not built at all and *limitation* means a known weakness of what was.

This is precisely what [ADR 0038](decisions/0038-what-the-circularity-signature-obliges.md)'s standing gap
dimension exists to surface: **a property real practice supplies that no template asks for.** It is a
candidate, not an obligation, and it routes through
[decision procedure 12](decision-procedures.md#12-a-property-or-section-is-proposed-for-a-template).

**It also independently vindicates the section this library's own spec was least sure about.**
[`tier2-specs.md`](tier2-specs.md) proposed a sixth section, *"What This Does Not Settle,"* and flagged it as
a departure from the paired skill's four-part shape, "to be defended or dropped on research evidence like
any other." The evidence defends it - **and the spec was written before this research ran and without
sight of it**, since the gap dimension is deliberately blinded to the library's own section design.

### Three caveats on that finding, which the research raised itself

1. **Selection bias.** The filled corpus was found by GitHub code search for `## Findings` and `# Spike:`
   headers, which pre-selects for reports that already have structure. Searches of engineering blogs, Medium
   and gov.uk turned up templates and process descriptions but **never a filled instance** - practitioners
   describe documenting a spike far more often than they publish the document.
2. **Provenance.** A large share of that corpus shows signs of **AI-agent-assisted or agent-authored
   drafting**. An element that recurs across agent-drafted documents is weaker evidence about human practice
   than the raw count suggests.
3. **Genre.** Real write-ups split three ways - human-facing blank templates, AI-coding-agent workflow
   templates, and actual filled examples - and pooling them into one frequency count would overstate the
   evidence. One AI-agent template literally addresses "llm coding agents"; its greater exhaustiveness is a
   genre effect, not evidence about typical practice.

### One section the evidence weakens

The spec proposed **Time Box** as its own section. Across the outcome-stage templates actually read, a
dedicated time-box heading is **usually absent** - it appears in the *pre-spike* planning artifacts (a Jira
ticket's `TIME-BOX` field, a spike *plan*'s "Deadline") rather than in the *report* of a completed spike. If
the bundle is built, that section has to be argued from evidence or folded into Scope.

---

## Contested, and named

**The central dispute is whether a spike's output is code or a document**, and it is not a matter of
emphasis.

- **Camp 1, throwaway code, no report:** Ward Cunningham (crediting Kent Beck), Ron Jeffries, Mike Cohn.
  The spike's product is code or knowledge, never a written artifact.
- **Camp 2, the output is a written deliverable:** Microsoft's Code with Engineering Playbook (explicit, with
  a template); SAFe's Enabler Story framing (implied, and its own accessible text stops short of the word
  "document"); and a large secondary layer of agile-training-vendor content repeating "documented finding /
  decision record / proof-of-concept" as settled doctrine **without a named-source citation**.

**A second dispute, inside the tooling.** Atlassian's own community forum shows practitioners disagreeing
about whether a Jira "Spike" issue type can carry acceptance criteria or a Definition of Done at all -
*"Spike issue types cannot have testing and user acceptance criteria applied... since spikes are not part of
the actual product increment"* against teams that apply exactly such criteria. Even the tooling ecosystem
has no consensus that a spike terminates in an evaluable written artifact.

---

## What would settle this

Three things would turn a thin admission into a solid one, and none of them requires rebuilding the research:

1. **A second qualifying named source** publishing a spike report as a written document - a standard, a
   methodology body, a book, or a named practitioner's published template. None was found in 72 sources.
2. **Readable SAFe text** using the words document or report for a spike's output. The relevant SAFe content
   is behind a login; a maintainer with access could check it directly and close the question either way.
3. **A maintainer ruling that one named source is sufficient**, which is a legitimate reading of ADR 0030 as
   written - it says "a named source", singular - and which would also be a precedent worth recording
   deliberately rather than setting by accident.

**Two notes on fidelity.** Em-dashes and en-dashes inside quoted source material have been normalised to hyphens, because this repository's gate forbids them in any tracked file; the wording is otherwise verbatim. And one quoted excerpt contained a relative Markdown link into its own repository, which has been rendered as plain text so it does not resolve as a link from here.

---

## Sources

**[1] Spike Solution - Ward Cunningham (c2 wiki / Portland Pattern Repository).** primary. **fetched-and-verified.**
`https://c2.com/ppr/wiki/ExtremeProgrammingRoadmap/SpikeSolution.html`
Supports: Origin of the term (Cunningham crediting Beck) and the canonical output: CODE, explicitly throwaway. No mention anywhere on this page of writing a document, report, or summary. Evidence AGAINST admission at the origin.
Quotable: "I would often ask Kent, 'What is the simplest thing we can program that will convince us we are on the right track?' Kent dubbed this a Spike." / "Write the smallest possible code that could be said to perform a function independent of existing mechanism." / "We plan to throw away the code, although sometimes something is salvaged."
Contested or time-bound: This is the founding definition (mid-1990s XP/C3 project era) and has not been revised; later sources (see Microsoft below) diverge from it without citing it.

**[2] Extreme Programming - Ward Cunningham et al. (c2 wiki).** primary. **fetched-and-verified.**
`https://c2.com/xp/ExtremeProgramming.html`
Supports: Confirms spike solutions appear in the primary XP canon only as a risk-reduction coding technique, with no deliverable/document described.
Quotable: "The development group identifies which stories are risky to complete on time (mainly because of a lack of experience with that type of coding) and does WorstThingsFirst based on a SpikeSolution."

**[3] Spike (software development) - Wikipedia contributors.** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Spike_(software_development)`
Supports: Encyclopedic summary corroborates code-centric origin; describes output as 'shared and discussed,' not published as a written artifact. No named source for a spike-report template is cited on this page.
Quotable: "A spike is a product development method originating from extreme programming that uses the simplest possible program to explore potential solutions." / "Following a spike, the results (a new design, a refined workflow, etc.) are shared and discussed with the team."
Contested or time-bound: Page itself flagged (per its own maintenance banner) as thin/under-sourced.

**[4] Spikes - Scaled Agile, Inc. (SAFe framework site).** vendor. **fetched-and-verified.**
`https://framework.scaledagile.com/spikes/`
Supports: Named methodology body treats spikes as backlog items with acceptance criteria, which implies some artifact to accept against, but the publicly accessible text I actually read does NOT use the words 'document' or 'report,' and the deeper 'Technical and Functional Spikes' section is gated behind login. Cannot be used alone to support ADMITTED.
Quotable: "Spikes are a type of SAFe Enabler Story. Defined initially in Extreme Programming (XP), spikes represent activities such as exploration, architecture, infrastructure, research, design, and prototyping." / "Like other stories, spikes are estimated, implemented and demonstrated."
Contested or time-bound: Widely paraphrased on secondary/vendor sites as 'output is a documented finding, a decision, a proof-of-concept, or an architecture recommendation' - I could not verify that exact phrase on SAFe's own accessible page.

**[5] Agile Spikes Deliver Knowledge So Teams Can Deliver Products - Mike Cohn / Mountain Goat Software.** practitioner. **fetched-and-verified.**
`https://www.mountaingoatsoftware.com/agile/what-are-agile-spikes`
Supports: Well-known named practitioner (Mike Cohn) describes spikes purely as an information-producing activity; no mention whatsoever of a written report, spike summary, or template. Evidence AGAINST admission from a major named practitioner source.
Quotable: "a spike refers to a time-boxed research activity that helps teams make better decisions & deliver better products" / "Spikes give agile teams the technical and functional information they need to make decisions about the best approach to certain user stories."

**[6] Technical Spike - Microsoft (Code with Engineering Playbook / Engineering Fundamentals Playbook, CSE/ISE).** practitioner. **fetched-and-verified.**
`https://microsoft.github.io/code-with-engineering-playbook/design/design-reviews/recipes/technical-spike/`
Supports: THE ADMISSION EVIDENCE. A named source (Microsoft, via its public, actively maintained open-source engineering playbook) explicitly states the deliverable of a spike IS a document, and prescribes its structure (problem statement/goals, repeatability, fact-finding, evidence with appendix, organization with headers/TOC). This directly contradicts the XP-origin 'throwaway code' framing without citing or reconciling it.
Quotable: "Generally the deliverable from a Technical Spike should be a document detailing what was evaluated and the outcome of that evaluation." / "The goal of a spike should be fact-finding, not decision-making or recommendation." / "Generally sections towards the beginning of the document should summarize data and use one or more appendices for more details."
Contested or time-bound: Represents a specific organization's (Microsoft CSE) house convention, not the XP originators' own view - flagged as contested below.

**[7] Template: Technical Spike - Microsoft (Code with Engineering Playbook / Engineering Fundamentals Playbook, CSE/ISE).** practitioner. **fetched-and-verified.**
`https://microsoft.github.io/code-with-engineering-playbook/design/design-reviews/recipes/templates/template-technical-spike/`
Supports: A concrete, fill-in-the-blank written template for recording a completed spike, published by a named source and linked directly from the playbook's spike-practice page. This is the artifact-level admission: a document type, not just a practice description.
Quotable: "# Template: Technical Spike" / "## Spike: [Spike Name]" / "- **Conducted by:** {Names and at least one email address for follow-up questions}" / "- **Backlog Work Item:** {Link to the work item to provide more context}"
Contested or time-bound: Retrieved verbatim from the raw markdown source in the microsoft/code-with-engineering-playbook GitHub repo, confirming it is a real, current, maintained file (not a dead or archived page).

**[8] Spike (Enabler Story) - Radu Marinescu / AgileSM.net.** practitioner. **fetched-and-verified.**
`https://agilesm.net/spike-enabler-story.html`
Supports: A minor, non-notable named individual's coaching-content page lists 'Decision record' among spike output types and talks about 'captured findings,' but never names a 'spike report' document or shows a template. Weak, secondary evidence at best; does not meet the bar of a widely recognized named practitioner.
Quotable: "Spike (Enabler Story) is a time-boxed backlog item used to learn enough to reduce uncertainty before committing to build." / "Define learning acceptance criteria - Specify what evidence is needed to decide, such as benchmark numbers, a prototype demo, a contract test, or a recommendation."
Contested or time-bound: Author is not established as a notable figure in the agile/XP literature; treat as thin evidence, not a qualifying named source.

**[9] _spike-templates repository - GitHub user "Tooramvale" (individual, not a notable named practitioner).** practitioner. **fetched-and-verified.**
`https://github.com/Tooramvale/_spike-templates`
Supports: Concrete proof that individual practitioners informally build spike-outcome templates (spike_plan_template.md, spike_outcome_template.md) - i.e. the practice of writing such documents exists in the wild - but the author is anonymous/non-notable, so this does NOT satisfy the task's 'named source' bar on its own.
Quotable: "This repository is to be used to generate new Spikes by reusing the existing Spike Plan and Spike Outcome templates"
Contested or time-bound: Explicitly logged as an example of what exists short of admission, not as admission evidence.

**[10] What Is a Spike in Agile? Examples, Types & SAFe Guide (2026) - Anuj Ojha / NextAgile (agile training/consulting vendor).** vendor. **fetched-and-verified.**
`https://nextagile.ai/blogs/agile/what-is-a-spike-in-agile/`
Supports: Traces the widely-repeated 'documented finding, a decision, a proof-of-concept, or an architecture recommendation' phrasing (seen echoed across many SEO blogs) to generic training-vendor content marketing, not to SAFe itself or any notable named practitioner. Used here to show that boilerplate does NOT constitute admission.
Quotable: "the output of a spike is knowledge. Specifically, the knowledge needed to estimate, design, or confidently commit"
Contested or time-bound: Content-marketing genre; attributes claims to 'established Agile practice' without citing a primary source.

**[11] Spike Solution (XP wiki / WikiWikiWeb) - Ward Cunningham's wiki (c2.com), with attributed contributions from Kent Beck and Ron Jeffries.** primary. **fetched-and-verified.**
`https://c2.com/xp/SpikeSolution.html`
Supports: The founding XP definition: a spike is minimal, end-to-end throwaway code used to resolve a technical unknown when the team is 'knowledge-limited, not time-limited,' kept tightly timeboxed (Ron Jeffries: 'no more than a couple of days, and a half day is ideal') and normally discarded after use.
Quotable: "the smallest possible code that could be said to perform a function independent of existing mechanism" / "end to end, but very thin" / "Spikes are good when you are knowledge-limited, not time-limited" / "We like a SpikeSolution to take no more than a couple of days, and a half day is ideal"

**[12] Spike solution (Create a Spike Solution) - Don Wells, extremeprogramming.org.** practitioner. **fetched-and-verified.**
`http://extremeprogramming.org/rules/spike.html`
Supports: One of the earliest (c. 2000) canonical public XP-practices references, corroborating the wiki definition almost verbatim and adding the pairing/duration guidance ('a week or two') for tougher spikes; confirms disposability as the default expectation.
Quotable: "A spike solution is a very simple program to explore potential solutions." / "Most spikes are not good enough to keep, so expect to throw it away." / "The goal is reducing the risk of a technical problem or increase the reliability of a user story's estimate." / "put a pair of developers on the problem for a week or two and reduce the potential risk"

**[13] Spike Solutions (from The Art of Agile Development) - James Shore and Shane Warden.** practitioner. **fetched-and-verified.**
`http://www.jamesshore.com/Agile-Book/spike_solutions.html`
Supports: Shows the XP-lineage definition held essentially unchanged into an influential 2007-era practitioner reference book: still framed as disposable technical investigation, tied explicitly to XP's preference for 'concrete data over speculation.'
Quotable: "A spike solution, or spike, is a technical investigation. It's a small experiment to research the answer to a problem." / "When you finish, throw it away, check it in as documentation, or share it with your colleagues, but don't treat it as anything other than an experiment."

**[14] The 2020 Scrum Guide (US) - Ken Schwaber and Jeff Sutherland / scrumguides.org.** primary. **fetched-and-verified.**
`https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf`
Supports: Direct, verified null result: the full text of the official 2020 Scrum Guide (Scrum Team, Events, Artifacts, etc.) was checked and the word 'spike' does not appear anywhere in the document. This is a real finding, not an inference from silence elsewhere.

**[15] Spikes in Scrum: The Exception, Not the Rule (Agile Atlas Commentaries, May 2014) - Scrum Alliance.** vendor. **fetched-and-verified.**
`https://web.archive.org/web/20180712125321/https://scrumalliance.org/learn-about-scrum/agile-atlas/agile-atlas-commentaries/may-2014/spikes-in-scrum-the-exception,-not-the-rule`
Supports: Scrum Alliance's own commentary (not the Scrum Guide, which never mentions spikes) explicitly credits XP as the origin and frames spikes as a supplementary, last-resort practice layered onto Scrum, not a core Scrum mechanism - while also showing the term being folded into ordinary story accounting (estimated, timeboxed to one sprint, demonstrated, accepted by the PO like any other story). Note: the live URL now 404s and scrumalliance.org's current site structure redirects away from it - this piece has since been removed from Scrum Alliance's active navigation, retrieved only via a 2018 Wayback Machine capture.
Quotable: "Spikes are an invention of Extreme Programming (XP), are a special type of story that is used to drive out risk and uncertainty in a user story or other project facet." / "Spikes, by definition, have a maximum time-box size of one sprint." / "Like other stories, spikes are put in the backlog, estimable and sized to fit in an iteration." / "A spike story...should be reserved for the more critical and larger unknowns...Use a spike as a last option."
Contested or time-bound: Article itself argues spikes should be rare/exceptional in Scrum, contrasting with SAFe's routinized treatment of the same term (see SAFe source below).

**[16] Enablers - Scaled Agile, Inc..** vendor. **fetched-and-verified.**
`https://framework.scaledagile.com/enablers`
Supports: Cross-check on SAFe's Spikes page: the four named Enabler categories are Exploration, Architecture, Infrastructure, and Compliance - Spikes are not listed as a fifth category, so in SAFe's current taxonomy a Spike is a technique that cuts across those categories (most naturally under Exploration) rather than a distinct type. Page carries its own 'Last Update: 24 February 2025' stamp, confirming SAFe's spike-related material is current, not legacy/abandoned content.
Quotable: "Last Update: 24 February 2025"

**[17] The Practice of Sizing Spikes with Story Points - Gregory Engel, Agile Alliance.** practitioner. **fetched-and-verified.**
`https://agilealliance.org/the-practice-of-sizing-spikes-with-story-points/`
Supports: A named practitioner explicitly arguing against the Scrum Alliance/SAFe-style practice of story-pointing spikes, on the grounds that it re-institutionalizes exactly what XP's disposable framing was meant to avoid - direct evidence of live, ongoing disagreement about how far spikes should be absorbed into normal estimation accounting.
Quotable: "A task aimed at answering a question or gathering information, rather than at producing a shippable product." / "Estimating spikes with story points is a vanity metric and teams are better served with time-boxed spikes that are unsized"
Contested or time-bound: Directly contests Scrum Alliance's 2014 guidance and SAFe's practice of sizing/estimating spikes like ordinary stories.

**[18] To spike or not to spike? - Matthew Hodgson, Zen Ex Machina.** practitioner. **fetched-and-verified.**
`https://zenexmachina.com/to-spike-or-not-to-spike/`
Supports: A practitioner/agile coach stating flatly that spikes have no place in official Scrum and that teams reaching for them are often reverting to Waterfall-style upfront analysis habits - the strongest 'not methodology-native to Scrum' claim found, consistent with the Scrum Guide's actual silence on the term.
Quotable: "the term Spike comes from eXtreme Programming (XP)" / "In Scrum there is no such thing as a Spike" / "Spikes aren't a bad thing when used for their intended purpose, but I don't encourage new Scrum Teams to mix XP with Scrum"
Contested or time-bound: Directly contests any framing of the spike as a core/official Scrum practice.

**[19] Why is a Spike called a Spike? - John Clapham.** practitioner. **fetched-and-verified.**
`https://johnclapham.wordpress.com/2016/02/23/why-is-a-spike-called-a-spike/`
Supports: Disputes the tidy, widely-repeated etymology story (Cunningham asking Beck a question, Beck naming it 'Spike'); shows Beck himself later avoided the term ('architectural prototype') due to its unwanted connotations, and the author concludes the term's true origin is not actually well-established - a genuine minor contested point about the practice's history, separate from its substance.
Quotable: "Kent Beck is generally recognized for introducing 'spike' to software development parlance, as part of the XP movement." / "Because people variously associate 'spike' with volleyball, railroads, or dogs, I have begun using 'architectural prototype' to describe this implementation." / "it is entirely possible that little thought was given to the term, the wrong word was used, it is an in joke, or that the reference is something only the author would understand"
Contested or time-bound: Contests the standard Cunningham-coined-it-for-Beck origin narrative repeated on Wikipedia and elsewhere.

**[20] The Spike Dilemma / Spikes are So... Ugh / Spike in Scrum? (forum) / Difference between Spike and Enablers (forum) - Scrum.org.** practitioner. **url-confirmed-not-read.**
`https://www.scrum.org/resources/blog/spike-dilemma`
Supports: Titles and search-index snippets indicate Scrum.org has published recurring content specifically debating/cautioning against spike misuse in Scrum, which would corroborate the 'live, contested practice' finding - but scrum.org's site is protected by an AWS WAF bot-challenge (confirmed directly via curl: every fetch attempt returned a JavaScript challenge page, not article content, e.g. 'window.awsWafCookieDomainList'), so no body text could be read this session. No claim in this record rests on quoted content from these URLs.
Contested or time-bound: Titles alone ('The Spike Dilemma', 'Spikes are So... Ugh') suggest Scrum.org's practitioner community treats spikes as a recurring source of friction/debate, consistent with findings from Scrum Alliance, Agile Alliance, and Zen Ex Machina - but this is circumstantial, not a verified quote.

**[21] SpikeSolution (original XP community wiki) - c2.com wiki  -  signed comments by Ron Jeffries, Ward Cunningham, Kent Beck, Katy Mulvey, Eric Newhuis.** primary. **fetched-and-verified.**
`http://c2.com/xp/SpikeSolution.html`
Supports: The foundational definition of a spike, and the primary-source origin of the throw-away-vs-keep disagreement (Jeffries vs. Newhuis vs. Mulvey) and of the 'couple of days / half-day' time-box guidance.
Quotable: "We plan to throw away the code, although sometimes something is salvaged." / "Write the smallest possible code that could be said to perform a function independent of existing mechanism." / "Spikes are good when you are knowledge-limited, not time-limited." / "We like a spike solution to take no more than a couple of days, and a half day is ideal."
Contested or time-bound: Undated wiki page, part of the original XP community wiki tradition (practice traces to the Chrysler C3 project, c. late-1990s). This is the OLDEST/orthodox position ('throw away the code') and is directly contested, on the same page, by Eric Newhuis (keep and integrate spike code into the build like a unit test) and softened by Katy Mulvey (treat 'throw away' as 'keep the first attempt small,' not a literal mandate to delete). Not superseded so much as never resolved  -  later frameworks (SAFe) formalize spikes in ways the original wiki authors did not anticipate.

**[22] Agile Spikes Deliver Knowledge So Teams Can Deliver Products - Mike Cohn, Mountain Goat Software.** practitioner. **fetched-and-verified.**
`https://www.mountaingoatsoftware.com/blog/spikes`
Supports: Documents the estimate/backlog-placement split as a live team-by-team disagreement, and frames the time-box as a soft checkpoint rather than a hard cutoff.
Quotable: "Because spikes are time-boxed, the investment is fixed." / "After the predetermined number of hours, a decision is made. But that decision may be to invest more hours in gaining more knowledge." / "Some agile software development teams opt to put a spike story on the product backlog along with user stories. Other teams take the approach that a spike is really part of some other product backlog item and will only expose spikes as sprint backlog items."
Contested or time-bound: Published August 6, 2024  -  current. Cohn deliberately stays descriptive/neutral on the backlog-placement question rather than resolving it, documenting the split as a live disagreement between teams rather than picking a side.

**[23] Don't Estimate A Spike In Agile - Andrew Fuqua, LeadingAgile (site now rebranded LiminalArc).** practitioner. **fetched-and-verified.**
`https://liminalarc.co/dont-estimate-spike-in-agile/`
Supports: Names and argues the 'time-box, don't estimate' camp, directly opposed to SAFe's 'estimate spikes like stories' position.
Quotable: "Spikes are, like defects, generally harder to estimate correctly relative to user stories. It's best to time-box them." / "It's very difficult to correctly relatively compare to a 1 point story a spike that is time-boxed in terms of hours or days." / "all spikes must be completed in 12 hours or less, each must have one explicit question to answer, we must know who the answer goes to, and there must be a 'demo'"
Contested or time-bound: Originally published April 2014, addendum Aug 4 2015  -  roughly 11 years old, and the article does not address what happens if the timebox expires without an answer. Now hosted at a rebranded URL (liminalarc.co) but the content itself doesn't appear updated. Directly contradicts SAFe's later, still-current guidance that spikes ARE estimated and story-pointed.

**[24] Spikes (SAFe glossary/practice page) - Scaled Agile, Inc. (SAFe framework).** primary. **fetched-and-verified.**
`https://framework.scaledagile.com/spikes`
Supports: The 'formalize-and-estimate' camp: SAFe's own definition explicitly requires spikes to be estimated and treated as stories, contradicting XP-orthodox and Fuqua/Iqbal informal treatments.
Quotable: "estimated, implemented and demonstrated"
Contested or time-bound: No specific article date visible; site footer shows '© 2010-2026 Scaled Agile, Inc.', implying continuously maintained/current guidance as of access on 2026-09-11. This is the clearest counter-position to XP orthodoxy and to Fuqua: SAFe treats a spike as an Enabler Story that IS estimated and sits in the iteration backlog like any other story  -  the opposite of 'don't estimate, don't formalize.'

**[25] Spike Antipatterns: How Not to Use Spikes - Miranda Dulin, Agile Ambition (self-identified in page footer, 'Unpuzzled in Winchester, KY').** practitioner. **fetched-and-verified.**
`https://www.agileambition.com/Essays/Spike-Antipatterns`
Supports: Names the 'dumping ground' / sprint-backlog-bloat failure mode directly, quoting published Scrum author Mitch Lacey.
Quotable: "Everyone doesn't get a spike because one isn't always warranted." / "Development teams should discuss the expiration of a timebox in the Daily Scrum." / "If your team has a Sprint that is entirely consumed with spikes...this is a sign that something is wrong." / "The team should not have committed to the tasks that would come out of that spike"
Contested or time-bound: Published Oct 20, 2025  -  current. The last two quotes are the author quoting Mitch Lacey (published Scrum author, 'The Scrum Field Guide') specifically on the 'dumping ground' failure mode  -  spikes generating follow-on tasks that jump the backlog priority queue. I was unable to independently corroborate the site owner's identity via search, so treat authorship attribution as self-reported by the page rather than externally confirmed.

**[26] No Spikes - Mark Blandford, personal blog on dev.to.** practitioner. **fetched-and-verified.**
`https://dev.to/markblandford/no-spikes-547m`
Supports: The most radical named camp: spikes as a practice should almost never be used at all.
Quotable: "First off, let me be clear I'm not 100% against completing Spikes. Perhaps 99% against them though."
Contested or time-bound: Published Jan 21, 2025  -  current. This is the most radical named position found: not a critique of HOW spikes are run but of whether the practice should exist at all, arguing story-point estimates should already absorb uncertainty and that spikes mostly add context-switching cost and decayed findings without proportionate risk reduction. A genuine minority/contrarian camp, not mainstream, but explicitly and personally argued rather than manufactured.

**[27] What Is an Agile Spike and When to Time-Box One - Giora Morein, CST  -  ThinkLouder.** practitioner. **fetched-and-verified.**
`https://thinklouder.com/blog/what-is-an-agile-spike-and-when-to-time-box-one/`
Supports: Supports the 'soft checkpoint, not hard stop' reading of time-boxing, aligned with Cohn.
Quotable: "A spike is a time-boxed research experiment that answers one specific question fast." / "If you need more time, that's a new conversation with the team."
Contested or time-bound: Updated May 19, 2026  -  current. Does not spell out a specific protocol for an unanswered spike beyond 'have a new conversation,' consistent with Cohn's softer framing and implicitly against a hard-stop reading of the timebox.

**[28] Spikes are so... ugh (mirrored republication) - Mary Iqbal, originally published on Scrum.org's resources blog.** practitioner. **fetched-and-verified.**
`https://www.rebelscrum.site/post/spikes-are-so-ugh`
Supports: The most extreme 'anti-formalization' camp: most spikes should not be Product Backlog items at all, and formalizing them is often performative.
Quotable: "Most so-called 'spikes' do not belong on the Product Backlog." / "creating tickets to prove that the team is working is counterproductive because creating those tickets takes time and focus away from maximizing value delivery."
Contested or time-bound: Original published June 14, 2024, updated Jan 10, 2025  -  current. I could not get the original scrum.org/resources/blog/spikes-are-so-ugh page to render via fetch (see the url-confirmed-not-read entry below for that URL); this is a third-party mirror republication of the same piece, used because it returned readable body text. Content should match the original but was not cross-verified word-for-word against scrum.org directly.

**[29] Spikes are So... Ugh (original) - Mary Iqbal / Scrum.org.** practitioner. **url-confirmed-not-read.**
`https://www.scrum.org/resources/blog/spikes-are-so-ugh`
Supports: Same claim as the mirror above; listed separately only to document that the canonical URL could not be read directly.
Contested or time-bound: Confirmed to exist via search indexing and cited by the mirror above; WebFetch returned an empty body on three attempts (likely JS-rendered page blocking scraping). No claim rests on this URL alone  -  the mirror above carries the actual quotes.

**[30] Misusing Spikes vs. Tasks for Research Items (forum thread) - Scrum.org community forum, multiple unnamed/handle-only posters.** practitioner. **url-confirmed-not-read.**
`https://www.scrum.org/forum/scrum-forum/52933/misusing-spikes-vs-tasks-research-items`
Supports: A lead (not a verified finding) toward the 'spike vs research task are structurally distinct' debate; explicitly flagged in key_findings as unsubstantiated.
Contested or time-bound: Could not be fetched (empty body on repeated attempts). Search-snippet paraphrases suggest some posters treat 'spike' as structurally distinct from a 'research task' while others don't, but since I never read the actual posts or confirmed poster identities, this does NOT count as a verified finding of named disagreement.

**[31] How We Do Spikes - Sophie Déziel, Medium.** practitioner. **not-retrieved.**
`https://medium.com/@sophiedeziel/how-we-do-spikes-4a43f0d19967`
Supports: Not used to support any claim; listed to document a failed retrieval attempt.
Contested or time-bound: WebFetch returned HTTP 403 Forbidden (Medium paywall/bot-block). Not used for any claim.

**[32] 6 Common Mistakes When Using Spikes - Maarten Dalmijn, Serious Scrum (Medium).** practitioner. **not-retrieved.**
`https://medium.com/serious-scrum/6-common-mistakes-when-using-spikes-9a4186c3cc29`
Supports: Not used to support any claim; listed to document a failed retrieval attempt.
Contested or time-bound: WebFetch returned HTTP 403 Forbidden. Not used for any claim.

**[33] Spikes, they're sharp - Lagerweij Consulting and Coaching.** practitioner. **not-retrieved.**
`https://www.lagerweij.com/2013/04/12/spikes-theyre-sharp/`
Supports: Not used to support any claim; listed to document a failed retrieval attempt.
Contested or time-bound: WebFetch returned HTTP 403 Forbidden. Published April 2013 per URL if it were retrievable  -  would be one of the oldest secondary sources found, but content could not be verified. Not used for any claim.

**[34] Spike: custom stickers (#2476)  -  feasibility - IsmaelMartinez/teams-for-linux (real OSS Electron Teams client).** practitioner. **fetched-and-verified.**
`https://github.com/IsmaelMartinez/teams-for-linux/blob/7657aa8bf884aede24b3211e1f46277c29f9bd6a/spike/2476-stickers/SPIKE.md`
Supports: Explicit 'Out of scope for this spike' section; pre-registered decision tree (if Phase1/Phase2/neither); preserved-but-unrun Phase 2 kept as future reference; negative-evidence framing ('the absence of prior art is a yellow flag').
Quotable: "## Out of scope for this spike" / "Not run. Phase 1 succeeded, so the spike's fallback path ... is not needed. The Phase 2 design in this document is preserved as a future-proofing reference in case Teams ever changes its editor framework and the synthetic-paste path regresses." / "If Phase 1 works: proceed with renderer-only implementation." / "The absence of prior art is a yellow flag."
Contested or time-bound: Likely AI-assisted drafting (harness-driven phase structure) though the investigation is of a real, dated GitHub issue in a well-known OSS project.

**[35] Spike: driving host dvui state from a prebuilt plugin dylib - fizzyedit/fizzy.** practitioner. **fetched-and-verified.**
`https://github.com/fizzyedit/fizzy/blob/c325818488ad9897625a41ea47304fd133610d22/spikes/shared-globals/README.md`
Supports: Environment/version pinning for reproducibility; explicit deferred-scope section distinct from findings.
Quotable: "## Findings (macOS/arm64, Zig 0.16.0)" / "## Not covered here (validate in-fizzy at Phase 4)" / "Globals are NOT auto-shared."
Contested or time-bound: References a Claude plan file path (~/.claude/plans/...), indicating AI-agent-assisted authorship.

**[36] Rust host shell  -  feasibility spike report - kungfu-systems/kungfu.** practitioner. **fetched-and-verified.**
`https://github.com/kungfu-systems/kungfu/blob/a025fe8fd3063175a263c481b42b0b34f63fa91c/docs/research/rust-host-spike.md`
Supports: Machine-readable self-rated confidence/evidence-grade/review-state frontmatter; measured cost of status quo; risk register with per-item resolution; conditional 'if exercised/if not exercised' recommendation; link to a downstream ADR ID.
Quotable: "confidence: medium" / "evidence_grade: B" / "review_state: unreviewed" / "Technically de-risked; not forced."
Contested or time-bound: 2026-07-10 dated; formal internal doc-metadata schema suggests deliberate but possibly AI-assisted documentation tooling.

**[37] Spike: Parse / render auto-memory (issue #192) - daaain/claude-code-log.** practitioner. **fetched-and-verified.**
`https://github.com/daaain/claude-code-log/blob/4031f87cd7dd4992a0b7e065db4d703e89118248/work/parse-memory-spike.md`
Supports: Named-maintainer attribution for scope decisions; original investigation preserved unedited beneath a later status update; open scope questions posed with the investigator's own recommended default attached, pending confirmation.
Quotable: "Scope confirmed by cboos:" / "## Original investigation (kept for reference)" / "## Scope questions (confirm before I implement)" / "Recommend **no for v1**"
Contested or time-bound: Named contributors (cboos, daaain) are real GitHub handles on a real maintained tool  -  one of the strongest human-provenance sources in this sample.

**[38] Spike Findings: Progressive Effect Migration via oRPC Integration - coder/xum.** practitioner. **fetched-and-verified.**
`https://github.com/coder/xum/blob/b9bc3949cffb231787c9e9fc669672a3bc486aef/rfc/20260831_effect-orpc-spike.md`
Supports: Reproducible evidence anchors (exact test counts, micro-benchmark numbers); staged/gated recommendation with explicit prerequisite phase; 'Non-goals for now' as distinct from risks.
Quotable: "Non-goals for now: full `Layer`-based dependency graph" / "bun test src/node/orpc/effectSpike.test.ts` → 9/9" / "Effect v4 RC churn  -  APIs may still shift before stable; don't merge v4 to main yet." / "Recommendation: adopt in narrow slices, gated on Effect v4 stable."
Contested or time-bound: Coder is a real company; mentions a 'codex review' gate, suggesting AI-assisted review of the spike itself.

**[39] SPIKE: PR Context Warm Cache - backnotprop/plannotator.** practitioner. **fetched-and-verified.**
`https://github.com/backnotprop/plannotator/blob/0f2bd6051c66d26f2d776a2a521d856627b3316c/adr/research/SPIKE-pr-context-warm-cache-20260630-110258.md`
Supports: Precise file:line citations anchoring claims to code; explicit 'Open Considerations' distinguished from what's required for the fix.
Quotable: "packages/server/review.ts:219"
Contested or time-bound: Second-precision timestamped filenames in a dedicated adr/research/ pipeline strongly suggest agent/automation-generated documents, not organic human write-ups.

**[40] Spike: Source Edit Race and Conflict Recovery - backnotprop/plannotator.** practitioner. **fetched-and-verified.**
`https://github.com/backnotprop/plannotator/blob/0f2bd6051c66d26f2d776a2a521d856627b3316c/adr/research/SPIKE-source-edit-race-and-conflict-20260618-095558.md`
Supports: A clean negative instance: a real, well-structured filled spike report with NO time/effort, confidence, decision-maker, or explicit out-of-scope fields  -  evidence these candidates are not universal even among otherwise thorough reports.
Contested or time-bound: Same agent-pipeline provenance caveat as the sibling SPIKE file in this repo.

**[41] Phase 4b gadget-inventory spike report - dbugom/rop-finder.** practitioner. **fetched-and-verified.**
`https://github.com/dbugom/rop-finder/blob/3228b1abdc8ceb180edfc1e1a80d16e52548198a/tests/spike-report.md`
Supports: A tracked, ID'd retraction of an earlier finding preserved in the document; framing a negative result about the target as a successful validation of the system's own error-handling path.
Quotable: "**Retracted (CHWIN-09, v0.1.1):** the gadget inventory above is accurate, but this is NOT a success-path demo." / "the design survives it by failing cleanly, not by emitting a DOA chain."
Contested or time-bound: Solo/small exploit-tooling project; document structure suggests an adversarial-review-driven (possibly AI-assisted) development process.

**[42] AUDIT-FINDINGS.md - dbugom/rop-finder.** practitioner. **fetched-and-verified.**
`https://github.com/dbugom/rop-finder/blob/3228b1abdc8ceb180edfc1e1a80d16e52548198a/docs/AUDIT-FINDINGS.md`
Supports: Independent adversarial re-verification of findings as a confidence practice adjacent to spike reporting; confirms a referenced spike-report artifact exists as a plan exit criterion.
Quotable: "32 of these findings were re-tested by independent adversarial verifiers instructed to refute them; none were refuted."
Contested or time-bound: Describes an adversarial-review pipeline that itself sounds AI-agent-driven; corroborating, not primary, evidence for spike-report content.

**[43] witness-at-team-lead.md (condensing an AT spike report) - gastownhall/gastown.** practitioner. **fetched-and-verified.**
`https://github.com/gastownhall/gastown/blob/649b832b7672bc7a2dbef26f5983aba6198b819b/docs/design/witness-at-team-lead.md`
Supports: Per-criterion GO/CONDITIONAL decision matrix with a roll-up count; conditional recommendation; quantified payoff estimate tied to the decision; a downstream document citing a spike report by stable ID+date+author.
Quotable: "Condensed from the AT spike report (gt-3nqoz, 2026-02-08, author: nux)." / "**Recommendation: CONDITIONAL GO for Phase 1 experiment.**" / "5/8 clear GO. 2 require workarounds (viable mitigations). 1 conditional on Phase 1 cost validation." / "AT's file-locked task claiming eliminates Dolt write contention (estimated 80-90% reduction). This is the strongest argument for adoption."
Contested or time-bound: This document is itself real and read in full, but it condenses a separate spike report (gt-3nqoz) that was NOT independently retrieved; 'author: nux' is plausibly an agent identity in a product about orchestrating agent teams, not a confirmed human  -  downgrade this as evidence for 'names who decided' specifically.

**[44] Final Model Validation  -  SPIKE-007 Summary - cristoslc/architecture-reference.** practitioner. **fetched-and-verified.**
`https://github.com/cristoslc/architecture-reference/blob/0b7dd9fd64e6df5145ac9376bb89746a379ea614/docs/research/Complete/(SPIKE-007)-Final-Model-Validation/(SPIKE-007)-Final-Model-Validation.md`
Supports: Pre-registered go/no-go criteria with numeric thresholds, scored afterward; pre-written pivot plan for the failure case; explicit lineage reuse of prior spikes instead of re-running; a 'why not other alternatives' section; a lifecycle table tying document status to dates and git commits.
Quotable: "## Go / No-Go Criteria" / "## Pivot Recommendation" / "No additional model runs were performed. The SPIKE-006 improved prompt subsumes SPIKE-004's prompt, so SPIKE-006 results serve as the post-improvement validation run." / "**Overall gate: GO with pivot on confidence.** Four of five criteria pass outright."
Contested or time-bound: Whole SPIKE-004→007 series dated the same day (2026-03-08) with heavy dependency-graph YAML frontmatter  -  strongly suggests an automated/agentic research-evaluation harness rather than a human team working over days; still a real artifact of a real repo's decision process.

**[45] CORTEX v5 Spike Results: Hermes Agent Core Integration - hansikadev/Jarviss.** practitioner. **fetched-and-verified.**
`https://github.com/hansikadev/Jarviss/blob/cb584897d1e03c16e37c50b6158964c295384b7c/SPIKE_RESULTS.md`
Supports: The one real, filled instance in this sample of a report recording actual time spent per task against the investigation itself; per-question feasibility verdict table (YES/PARTIAL); staged-priority list of known gaps (hard prerequisite for a later phase vs. not a blocker for the current one).
Quotable: "## 2. Time Spent (Task by Task)" / "*(Estimated time spent during the spike phase)*" / "**Total** | | **~5h 15m**" / "This is a hard prerequisite for Phase 2 (the LEARNING path)... It is not a Phase 1 blocker."
Contested or time-bound: Solo personal agent-framework project; ambiguous whether a human or the agent itself logged the time  -  the only 'time spent' instance found is also the lowest-confidence provenance for organic human practice.

**[46] Claude Code Session Naming  -  Availability Spike - miethe/CCDash.** practitioner. **fetched-and-verified.**
`https://github.com/miethe/CCDash/blob/04286f5cc9ac22c1f6ce98dc440b778ef8f55b90/docs/project_plans/exploration/automatic-session-naming/spikes/tech-claude-spike.md`
Supports: A hypothesis stated and then explicitly declared refuted, not silently replaced; a naive/misleading topline statistic reported alongside the correctly segmented one, with an explicit warning about which to trust; open questions given durable IDs.
Quotable: "The hypothesised `summary` record does not exist" / "The charter's compaction-summary theory is refuted." / "The segmented 87.2% figure is the one that matters." / "**OQ-C1**: What triggers `ai-title` generation?"
Contested or time-bound: Real tool project (a Claude Code session dashboard) investigating Claude Code's own internals; empirical/data-driven, likely AI-assisted analysis of a large real corpus (7,531 files).

**[47] class-based-codec-design.spec.md (citing a spike report) - prisma/orm.** practitioner. **fetched-and-verified.**
`https://github.com/prisma/orm/blob/f2e3590ff2d446304e7b7af55b9a0277afb0f43e/projects/codec-registration-completion/specs/class-based-codec-design.spec.md`
Supports: A downstream spec resolving five separate open questions by citing one spike report's specific named sub-sections (Q-A..Q-E); confirms a spike is expected to capture friction items and negative-test error output, not just the positive result.
Quotable: "**Resolved by spike** (wip/class-based-codec-spike.md, section Q-A)" / "The Pattern E spike report (six ACs validated end-to-end on the `spike/class-based-codecs` branch). Captured TS error messages from negative tests, friction items, and resolved spec questions (Q-A..E)."
Contested or time-bound: Prisma is a well-known real company/OSS project  -  strong human-team provenance for the citing document; the underlying spike file itself (wip/class-based-codec-spike.md) was not retrieved, so its own content is not-retrieved, only this spec's citations of it.

**[48] _spike-templates: spike_outcome_template.md - Tooramvale (GitHub template repo, apparent academic/dev-team origin).** practitioner. **fetched-and-verified.**
`https://github.com/Tooramvale/_spike-templates/blob/master/spike_outcome_template.md`
Supports: Real post-hoc spike report template. Findings ('What we found out') and 'Recommendations' are separate, independently-optional sections; 'Open issues/risks' is the closest analogue to an open-items section but is framed as unresolved risk, not scope exclusion; no time-box section appears in the outcome document itself.
Quotable: "## What we found out" / "#### Describe (sentences), + graphs/screenshots/outcomes as needed" / "## Open issues/risks _[Optional  -  remove heading/section if not used!]_:" / "## Recommendations _[Optional  -  remove heading/section if not used!]_:"

**[49] _spike-templates: spike_plan_template.md - Tooramvale (GitHub template repo).** practitioner. **fetched-and-verified.**
`https://github.com/Tooramvale/_spike-templates/blob/master/spike_plan_template.md`
Supports: Companion pre-spike template: shows the time box living here as 'Planned start date' / 'Deadline', not in the outcome report half of the pair.
Quotable: "**Planned start date:**  Example: 13/08/2017" / "**Deadline:**  Example: 20/08/2017" / "## Goals/Deliverables:"

**[50] _spike-templates: README.md - Tooramvale (GitHub template repo).** practitioner. **fetched-and-verified.**
`https://github.com/Tooramvale/_spike-templates/blob/master/README.md`
Supports: Cites the two sources the template author drew on (XP's 'Spike solution' and SAFe's spikes page), corroborating those as the field's two most-cited reference points.
Quotable: "Create spike solutions to figure out answers to tough technical or design problems." / "Most spikes are not good enough to keep, so expect to throw it away."

**[51] Technical Exploration ("Spike") Guidelines - GitLab Inc. (public company handbook, Growth engineering).** primary. **fetched-and-verified.**
`https://handbook.gitlab.com/handbook/engineering/development/growth/technical_spikes/`
Supports: Real, currently-used org process, not a blank template. The report artifact IS the tracking issue, closed out with one free-text comment; findings and recommendation are explicitly combined in that single comment rather than split into headed sections. No time-box section (a due date is negotiated informally with the PM). No explicit 'not investigated' section.
Quotable: "Technical spikes are fundamentally different than our typical work items as the result is more commonly a recommendation on a technical direction or solution rather than code" / "Provide a summary comment with detailed learnings of your investigation and recommended path(s) for the solution in the spike issue." / "Include an outline of the recommended next step issues and/or epics to be created for the next phase of work."
Contested or time-bound: Describes GitLab's own current internal process as of retrieval; the handbook is a living document and this could change.

**[52] Spike solution - Don Wells, ExtremeProgramming.org.** primary. **fetched-and-verified.**
`http://www.extremeprogramming.org/rules/spike.html`
Supports: The originating XP definition of a 'spike solution' (1999-era rules page). Contains zero report-format or section-structure guidance of any kind  -  the strongest evidence that documentation templates for spikes are an entirely later, team-invented layer, not part of the original practice.
Quotable: "Create spike solutions to figure out answers to tough technical or design problems." / "A spike solution is a very simple program to explore potential solutions. Build the spike to only addresses the problem under examination and ignore all other concerns." / "Most spikes are not good enough to keep, so expect to throw it away." / "When a technical difficulty threatens to hold up the system's development put a pair of developers on the problem for a week or two and reduce the potential risk."

**[53] Spikes for uncertainties in Scrum - Vibhor Chandel (named practitioner).** practitioner. **fetched-and-verified.**
`https://www.vibhorchandel.com/p/spikes-for-uncertainties-in-scrum`
Supports: A real pre-spike ticket template (shown via Jira screenshot) with PROBLEM / SCOPE / ACCEPTANCE CRITERIA / TIME-BOX / ADDITIONAL INFORMATION as its own headings. The clearest instance found of time-box as a dedicated section  -  but it lives on the planning/ticket side, not in an outcome report (this template doesn't reach a findings/recommendation stage).
Quotable: "PROBLEM" / "SCOPE" / "ACCEPTANCE CRITERIA" / "TIME-BOX"

**[54] gitban spike template (.gitban/templates/spike.md) - PeonPing (open-source git-based kanban tool).** practitioner. **fetched-and-verified.**
`https://github.com/PeonPing/peon-ping/blob/main/.gitban/templates/spike.md`
Supports: The richest real template found: Spike Overview (Investigation Question, Time Box, Success Criteria) / Context & Background Research / Initial Hypotheses & Questions / Investigation Log / Spike Findings & Recommendation (nested: Summary of Findings, Recommendation, Alternative Approaches Considered) / Follow-up & Lessons Learned / Completion Checklist. Caveat: this is explicitly a template for an AI coding agent to fill in ('Note to llm coding agents...'), a different genre from a human-facing template, and its unusual exhaustiveness likely reflects that.
Quotable: "## Spike Overview" / "**Investigation Question:**" / "**Time Box:**" / "## Investigation Log"
Contested or time-bound: Genre caveat: authored for an LLM coding agent, not a human team filling the doc directly  -  its section count should not be read as typical of human practice.

**[55] nw-spike task template (nWave/tasks/nw/spike.md) - nWave-ai (open-source AI agent development framework).** practitioner. **fetched-and-verified.**
`https://github.com/nWave-ai/nWave/blob/main/nWave/tasks/nw/spike.md`
Supports: Another AI-agent-workflow spike template (same genre caveat as PeonPing). Defines two output docs, findings.md and wave-decisions.md, the latter headed Assumption Tested / Verdict / Design Implications / Constraints Discovered  -  findings (Verdict) and recommendation (Design Implications) kept as distinct headings. Time box is a hard 1-hour cap enforced in prose and a checklist item, not a titled section.
Quotable: "Execute a timeboxed spike (max 1 hour) to validate a single core assumption before investing in architecture design." / "## Assumption Tested" / "## Verdict" / "## Design Implications"
Contested or time-bound: Same AI-agent-genre caveat as the PeonPing template.

**[56] parse-memory-spike.md (real worked spike write-up, issue #192) - daaain (maintainer, claude-code-log open-source project).** practitioner. **fetched-and-verified.**
`https://github.com/daaain/claude-code-log/blob/main/work/parse-memory-spike.md`
Supports: The single best real, actually-filled-in worked spike write-up found (not a blank template). Order: status line / 'What v1 ships' / 'Follow-ups (deferred, not in v1)' / 'Original investigation (kept for reference)' / 'The question (issue #192)' / 'Findings' (numbered) / 'Proposed approach' / 'Scope questions (confirm before I implement)' / 'Limitations'. The only source with a genuinely explicit not-fully-investigated apparatus, and it's split three ways rather than under one heading.
Quotable: "## The question (issue #192)" / "## Findings" / "## Follow-ups (deferred, not in v1)" / "## Scope questions (confirm before I implement)"

**[57] E2EE Phase 0 spike: KEM decision, KAT sources, and the isolate-budget gate - unredacted (freesocks-control-plane open-source project).** practitioner. **fetched-and-verified.**
`https://github.com/unredacted/freesocks-control-plane/blob/main/docs/e2ee-phase0-spike.md`
Supports: A real, filled-in engineering spike write-up using NO named-section convention at all  -  bespoke numbered headings (0 through 7) driven purely by content, ending in a 'Decision record' whose 'Pending before production sealing' line functions as the only open-items marker. Evidence that real practitioner spike write-ups often diverge entirely from any named template.
Quotable: "## 0. Headline gate finding (RUNTIME REQUIREMENT)" / "## 5. The gate (results)" / "## 7. Decision record" / "Pending before production sealing (P0d): vendor the X-Wing draft-10 + FIPS 203 KATs into CI; assert single-use-context in the wrapper"

**[58] Finding spikes in your plans - kelebeklabs (dev.to).** practitioner. **fetched-and-verified.**
`https://dev.to/kelebeklabs/finding-spikes-in-your-plans-1lof`
Supports: Third corroborating null result: no explicit documentation template; timeboxing mentioned only informally inside a worked mini-example.
Quotable: "you timebox it for 2 hours"

**[59] Spikes (team wiki page) - University of Bath, Digital Content and Development team wiki.** practitioner. **not-retrieved.**
`https://wiki.bath.ac.uk/display/webservices/Spikes`
Supports: Would have been direct evidence of a real wiki-hosted spike template (search snippet suggested fields: story estimated, time boxed, acceptance criteria including thought process/outcomes/recommendations documented)  -  but the host refused the connection on two independent attempts (direct and via web.archive.org), so nothing here is used as evidence.

**[60] Navigating Uncertainty: Crafting Effective Spikes in Scrum - Serious Scrum (Medium).** practitioner. **not-retrieved.**
`https://medium.com/serious-scrum/navigating-uncertainty-crafting-effective-spikes-in-scrum-600656734865`
Supports: Blocked with HTTP 403; not read, not used as evidence.

**[61] What's a Spike, Who Should Enter It, and How to Word It? - LeadingAgile / LiminalArc.** practitioner. **not-retrieved.**
`https://liminalarc.co/2016/09/whats-a-spike-who-should-enter-it-how-to-word-it/`
Supports: Original URL redirected (301) to this address; the redirected page itself was never fetched, so nothing here is used as evidence.

**[62] SpikeSolution (Ward Cunningham's wiki, 2016 snapshot) - Ward Cunningham (WardCunningham).** primary. **fetched-and-verified.**
`https://web.archive.org/web/20160105154555/http://c2.com/cgi/wiki?SpikeSolution`
Supports: The originating author's own account of coining 'spike' within Extreme Programming - it names a code exploration, not a documentation artifact, and predates any ADR/RFC framing entirely.
Quotable: "I would often ask Kent, 'What is the simplest thing we can program that will convince us we are on the right track?' Such stepping outside the difficulties at hand often led us to simpler and more compelling solutions. Kent dubbed this a Spike." / "'Spike' because TopDown is typically BreadthFirst, but a Spike is DepthFirst." / "So-called because a spike is 'end to end, but very thin', like driving a spike all the way through a log."
Contested or time-bound: The live c2.com wiki no longer serves this content directly (JS shell / cert mismatch on the current domain); only the Internet Archive snapshot was readable.

**[63] Why I don't write ADRs - Dan Leech (dantleech.com).** practitioner. **fetched-and-verified.**
`https://www.dantleech.com/blog/2024/03/10/why-i-dont-write-adrs/`
Supports: The clearest named source that directly draws the spike-to-ADR line asked for in the brief, while also arguing the spike's own artifact should stay 'the notes', not a decision - the strongest single quote for what a spike report is NOT (a finished decision).
Quotable: "It follows that the spike can act as a supporting document for an ADR. That a spike will evolve to an ADR." / "they are basically the same picture" / "Spikes are done before the implementations are made." / "the main artifact of the spike should be the notes"
Contested or time-bound: Dated March 10, 2024; the author's stated position is that ADRs and spike documents largely overlap and that spikes are the lower-friction alternative - this is an argued opinion piece, not a standard.

**[64] About work items and work item types - Azure Boards - Microsoft (Azure DevOps official documentation).** primary. **fetched-and-verified.**
`https://learn.microsoft.com/en-us/azure/devops/boards/work-items/about-work-items?view=azure-devops`
Supports: Official confirmation that NONE of Azure DevOps's four default processes (Agile, Basic, Scrum, CMMI) includes a native Spike work item type. Grepped the raw page text myself: zero occurrences of 'spike'.
Quotable: "Use user stories and tasks to track work." / "Use bugs to track code defects." / "Use epics and features to group work under larger scenarios." / "The Issue (Agile and CMMI) and Impediment (Scrum) work item types track nonwork project elements that can affect work delivery."
Contested or time-bound: Page dated (ms.date) 2026-06-16; last updated 2026-07-23 per its own metadata.

**[65] What are work types? (Jira Cloud Administration docs) - Atlassian (official support documentation).** primary. **fetched-and-verified.**
`https://support.atlassian.com/jira-cloud-administration/docs/what-are-issue-types/`
Supports: Official confirmation Jira ships with no native Spike issue type by default. Grepped the raw page text myself: zero occurrences of 'spike'.
Quotable: "By default, software spaces come with three standard work types: Bug A bug is a problem which impairs or prevents the functions of a product. Story A user story is the smallest unit of work that needs to be done."
Contested or time-bound: No caveat.

**[66] Managing issue types in an organization - GitHub (official documentation).** primary. **fetched-and-verified.**
`https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/managing-issue-types-in-an-organization`
Supports: Official confirmation GitHub Issues' native Issue Types feature ships with only three defaults (task, bug, feature) - no Spike. Grepped raw page text myself: zero occurrences of 'spike'.
Quotable: "Default issue types are included in every organization, but these can edited, disabled, or deleted. The default types are task, bug, and feature."
Contested or time-bound: No caveat.

**[67] About the issue type field - GitHub (official documentation).** primary. **fetched-and-verified.**
`https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-the-issue-type-field`
Supports: Independent confirmation (second GitHub docs page) of the same no-native-Spike finding.
Quotable: "how the issue is classified in your organization, such as a bug, task, or feature"
Contested or time-bound: No caveat.

**[68] Issues: Issue Types (roadmap #837) - GitHub product team (github-product-roadmap).** primary. **fetched-and-verified.**
`https://github.com/github/roadmap/issues/837`
Supports: GitHub's own roadmap announcement names 'spike' as the paradigm example of a CUSTOM, org-defined issue type - confirming spike is convention, not a shipped default, directly from the vendor that built the feature. Verified via authenticated `gh` CLI read of the issue body.
Quotable: "Users will be able to define issue types (ex. bug, feature request, spike) at the org level and apply this syntax to an issue in a repo."
Contested or time-bound: Posted 2023-11-08, describing a then-upcoming feature; GitHub Issue Types later shipped with task/bug/feature as the actual defaults per the docs pages above - 'spike' remained an example, not a default.

**[69] Functional Stories, Spikes, Technical Stories! Help (Atlassian Community) - Atlassian Community practitioners (forum thread).** practitioner. **fetched-and-verified.**
`https://community.atlassian.com/forums/Agile-discussions/Functional-Stories-Spikes-Technical-Stories-Help/td-p/1913069`
Supports: Real-world evidence of the 'convention, not native type' pattern in practice, and a practitioner directly linking a Jira Spike ticket's outcome to 'a design doc' - the closest thing found to a spike-to-RFC/design-doc bridge, though informal.
Quotable: "From my experiences, we use issue type 'Spike' for any research tickets which outcome might be a design doc, planning, or other stuff. We use Story for real functionality from the user's perspective, we use tasks to track any engineering works." / "these may be separate issue types or a custom field describing the type of story"
Contested or time-bound: Unofficial community forum discussion (dated around Jan 19, 2022), not vendor documentation; individual usernames could not be reliably confirmed from the rendered page's markup.

**[70] Companies Using RFCs or Design Docs and Examples of These - Gergely Orosz, The Pragmatic Engineer.** practitioner. **fetched-and-verified.**
`https://blog.pragmaticengineer.com/rfcs-and-design-docs/`
Supports: A comprehensive, well-known practitioner survey of RFC/design-doc practice across major tech companies (Google, Meta, Microsoft, Amazon, etc.) that never mentions 'spike' at all (confirmed via direct grep of raw fetched text: zero occurrences) - strong evidence the spike and RFC/design-doc literatures are two separate traditions that rarely cite each other by name.
Contested or time-bound: Negative finding (absence of a term) used to support the null result on spike-vs-RFC.

**[71] How to use spikes as a foundation for ADRs - Cat Morris (Medium).** practitioner. **url-confirmed-not-read.**
`https://medium.com/@cat-mo/how-to-use-spikes-as-a-foundation-for-adrs-92bc1617617b`
Supports: Title and URL suggest a second named source drawing the spike-to-ADR line, but the page returned HTTP 403 on fetch; no claim in this report rests on its content.
Contested or time-bound: Could not be retrieved (403 Forbidden); not used as evidence.

**[72] What about spikes? are they official in Scrum? - Scrum.org forum.** practitioner. **url-confirmed-not-read.**
`https://www.scrum.org/forum/scrum-forum/6203/what-about-spikes-are-they-official-scrum`
Supports: Title alone corroborates that practitioners actively debate spike's non-official status in Scrum, but the page rendered blank (JS-driven) on fetch; the actual 'not in Scrum Guide' finding in this report is sourced instead to a direct read of the Scrum Guide PDF itself.
Contested or time-bound: Page content could not be extracted; not used as evidence.
