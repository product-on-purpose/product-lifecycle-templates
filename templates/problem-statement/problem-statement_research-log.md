# problem-statement: research log

Research conducted 2026-10-11, building on the Define admission sweep of the same day, whose verdicts are summarised
in [`tier2-specs.md`](../../docs/internal/tier2-specs.md) and recorded in
[ADR 0068 (the define phase means problem framing)](../../docs/internal/decisions/0068-define-means-problem-framing.md)
and [ADR 0069 (problem-statement joins discovery-docs)](../../docs/internal/decisions/0069-problem-statement-joins-discovery-docs.md).
The build's six-dimension fan-out covered the canon and definition, longer and sectioned forms, lineage and contested
practice, boundaries with this library's neighbours, failure modes and quality bars, and the standing gap question.
**43 sources are recorded below, all fetched-and-verified.** Sources [35] to [43] come from a gap-fill pass run
the same day, after drafting, and are described in the last section of this file. Only `fetched-and-verified` sources are quoted anywhere
in this bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a retrieval tool
returns. The agents returned 236 quotations from 38 sources. 202 passed as normalized substrings, and 8 more pass once
a rendering artifact is removed. Of the other 26, nine came from the five sources this log leaves out, for the reasons
given below. Eight pass once the HTML entities left undecoded in the cached text are decoded, such as `&#8217;` for an
apostrophe and `&nbsp;` for a space. Three were fields an agent had joined with a slash; each part was checked on its
own, all of them pass, and they are quoted separately. The remaining six are replaced below by the verbatim parts of
the same passages that pass, or dropped. Every page first cached during this build was fetched a second time with the
cache bypassed: 140 quotations on 24 pages were re-checked that way, and 128 pass. The 12 that do not sit on seven
pages whose fresh fetch was blocked or returned a different rendering, and each is accounted for above. Dashes inside
quotations are written as hyphens, as the house rule requires.

---

## What the checks caught, and what was not read

**The spec's lean-only finding stands as a finding, and the full variant has sourced sections anyway.** The admission
sweep found that every admitting source describes a short artefact, and this build's sources agree: [15] puts a
problem statement at "about 18 words long", [1] says "If you can condense your problem statement down to a few
sentences, others will quickly understand", and [6] says great points of view "can be compressed to fit on a bumper
sticker". The maintainer ruled for two sizes on 2026-10-11. This build's longer-forms dimension then found four
elements that recur across independent sectioned forms, which the full variant uses:

1. **Success measures**, in [12], [13], [8] and [16]. [12]'s formula closes on "these measurable changes in their
   behavior", [13] asks "if we solve it, how we will we know?", [8] has "Metric(s) and Baseline: Define how you'll
   evaluate success.", and [16]'s summary asks for "A summary of the primary success criteria."
2. **What is not part of the problem**, in [3], [16], [11] and [1]. [3] says "Reframing the problem also includes
   agreeing what is not part of the problem", [16] asks for the scope, "what is to be included and, perhaps more
   importantly, what isn't", [11] asks "In what circumstances does it not occur?", and [1] says a brief statement
   shows "what's out of scope".
3. **How people cope today and what has been tried**, in [8], [10] and [32]. [8] asks "How do people currently solve
   this problem?", [10] lists "how customers work around the problem", and [32] asks applicants to "Describe previous
   attempts to solve the problem and why they failed."
4. **Open questions and assumptions**, in [8], which has a literal "Open Questions" field, and [33], which says a
   statement written "before doing design research and consulting stakeholders should be considered as being based
   on assumptions". [1] adds that a team can refine the statement "if you've learned root causes or how much a
   problem costs your organization".

**Constraints are a sourced field elsewhere, and this bundle routes them on.** The first pass found no source that
labels a constraints section; [14]'s "Project Barriers" was the nearest, and a barrier met along the way is not a limit
accepted in advance. The gap-fill pass then found the field, in engineering design and in proposals. [36] teaches a
workflow in which need statements are "constrained by defining specifications", and reports that "ABET requires
problem statements to include "realistic constraints"". [41], a capstone proposal, labels "Constraints, Risks, and
Resources". In both, the constraint bounds a design, which is a solution, and this document names none. [36] still
puts constraints inside the statement, "The constraints need to be added to your problem statement", because its
problem statement opens a design; the engineering-design line dissents from this bundle's routing. [37]'s
"Limitations and Constraints on Analysis" is a different thing: limits on the evidence, such as "lack of data", which
the full variant's Open Questions and Assumptions already holds. **The bundle has no constraints section.** A limit
any answer must respect belongs in `project-brief`'s Constraints and Who Should Be Involved section, which carries it
at both sizes. That routing is this library's POSITION.

**A root cause stays out of the statement, and a suspected one has a place.** Two sources exclude causes from the
statement: [15] says "problem statements do not describe the solution or root causes", and [24] says a good statement
"does not attempt to diagnose the problem, nor assign blame". Two point the other way: [2]'s checklist asks "Do we
understand the root cause?", and [1] lets a team refine the statement once it has "learned root causes". [34]'s A3
template keeps the two apart, with the problem statement as step 1 and "What is your most likely root cause?" as a
later step. The bundle follows [34]: the statement names no cause, and a cause the team suspects goes under Open
Questions and Assumptions, labelled as a hypothesis. That placement is this library's POSITION.

**The opportunity statement is confirmed as an alias, with a dissent.** [1] says problem statements "can also capture
opportunities (in which case they are sometimes referred to as opportunity statements instead of problem statements,
although they are written and used in the same way)". [12] publishes a separate Business Opportunity Statement
formula for a new initiative, and advises "try the Business Problem Statement first". [28] argues the two are not the
same for projects: "many practitioners treat problems and opportunities interchangeably when developing Business
Cases and Project Charters". The alias stands on [1], and the companion reports [28]'s dissent.

> **Note added 2026-10-22.** The maintainer ruled on 2026-10-17, in decision sitting item D9, that the
> problem statement and the opportunity statement are different documents. The alias was removed in
> template version 0.1.1, and the opportunity statement became catalog entry 207, a candidate type. The
> evidence recorded above is unchanged. The same change added "point of view statement" as an alias, on
> [17], [18] and [33] (sitting item D6).

**The APM claim the spec repeated is narrower than it read.** The spec cited `project-brief`'s research log for an APM
Body of Knowledge passage that names "problem statement", "project brief" and "project charter" as names in common use
for one rationale. This build read APM's own online glossary [25], which draws on the fifth to eighth editions: it has
no "problem statement" entry, and its "Brief" and "Charter" entries define two different things ("The output of the
concept phase of a project or programme" and "A document that sets out the working relationships and agreed
behaviours within a project team"). The two readings do not contradict each other, since a body-of-knowledge passage
can mention a name its glossary does not define. The companion cites only what [25] says.

**PMI barely names the type.** [26] reports that the PMBOK Guide's only mention of "problem statement" in its fifth
edition sits under a cause-and-effect diagram, and in its sixth under data analysis for root-cause work. That is a
practitioner's report of two pages this build did not read, and the companion attributes it to [26].

**Not read.** McKinsey's problem statement worksheet: four attempts on mckinsey.com timed out, and the gap-fill pass's
four more (the article, two regional mirrors and a PDF asset) timed out too. The tool refused web.archive.org. No
McKinsey field name appears in this bundle. The gap-fill read the publisher's excerpt of Conn and McLean's
*Bulletproof Problem Solving* instead [35]; its appendix of blank worksheets is not in the excerpt. Atlassian's Confluence and Trello templates behind the Problem Framing play open inside
application shells, so only the play page [11] was read. Dwayne Spradlin's 2012 and Thomas Wedell-Wedellsborg's 2017
Harvard Business Review articles are paywalled. Alan Klement's job-story post and a Lean UX hypothesis-statement
excerpt could not be fetched. PMI's own problem-statement page returned HTTP 403.

**Five sources owned by a dimension are left out of this log.** The University of New Mexico's business-case template
is a `.docx`, which the raw-text checker cannot read, so neither of its quotations could be checked. A skills.cat page
is a third-party listing of an AI agent skill, not a publication; its failure-mode taxonomy is covered by [22], [23]
and [24]. A figr.design blog post's one quotation failed the check, and no other source rests on it. An exam-preparation
study guide for PMI-PBA is a third party's summary of a credential syllabus; [20] carries the same camp on success
criteria. A mutomorro.com page held none of the claim a search summary had attributed to it: the agent read it in full
and found no occurrence of "opportunity".

---

## The admission record

The type cleared [ADR 0030](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md)'s admission test
in the Define admission sweep on two named sources, either of which suffices under
[ADR 0048](../../docs/internal/decisions/0048-one-named-source-clears-the-admission-test.md). [1] defines it as "A
concise description of the problem that needs to be solved" and lists what "A problem statement should include". [2]
tells teams to "Use the evidence you gather to document your clearly defined problem", and closes on a five-question
review. This build re-read both pages in full, and every quotation above passed against their raw text.

Heap [8], [9] and [10] settle a narrower point. [9] calls its artefact "A worksheet for defining product problems", the
word [ADR 0035](../../docs/internal/decisions/0035-prototype-brief-fails-the-admission-test.md) used when refusing an
earlier candidate. [10]'s named author calls it "a document that lays out the problem to be solved and argues for why
we should choose to solve this particular problem". So the worksheet label alone does not decide form. [8] is not a
structural source for this bundle beyond its problem-framing fields: its later fields, "What are the jobs-to-be-done to
address?" and "Launch Plan", are delivery content.

---

## Claims flagged contested or time-bound

1. **Whether success measures belong in a problem statement.** Inside: [12], [13], [8], [16] and [20], whose template
   lists "Success Criteria: Specific, measurable indicators that will confirm the problem has been solved". Later and
   separate: [21], whose "Defining success" play assumes "You should already have a well-defined problem" and says "The
   outcome is not an output or a metric of your project". [39] sits with [21]: "Convert your problem statement into
   objectives you can actually measure", which then "go straight into your Project Charter". [15]'s 18-word statement
   has no room for one. The gap-fill added a reconciling test rather than a vote: [38] quotes Josh Seiden's definition of an
   outcome, "a change in human behavior that drives business results", and warns in its own words that "If you can achieve the metric without actually
   helping customers, it's probably an output in disguise". A measure of the problem's size passes that test, and a
   feature's adoption fails it. [40] is a dissent on targets: its success-metric example is "50% reduction in cycle
   time; zero compliance findings", a target this bundle's guide leaves to the document that proposes a solution. The
   bundle puts success measures in the full variant only and names this split in the companion.
2. **Written once, or revisited.** Once: [20] places it "at the very start of the project lifecycle, during the
   initiation phase, before the project charter is drafted". Revisited: [17] says "You revisit and reformulate as you
   learn by doing", and [1] says "Throughout the discovery process, you can return to your problem statement and add
   to it". The bundle follows `discovery-docs`' cadence clause: written once for a decision, and refined during the
   discovery it opens, until that decision is made.
3. **Whose problem it is.** The design-thinking line in [17] and [18] is user-centred: "[USER] needs to [USER'S NEED]
   because [SURPRISING INSIGHT]". The business line in [12] starts from a product that "isn't meeting our
   expectations". [1] carries both, since it requires "The people affected by the problem" and "The impact of the
   problem on the organization". The bundle carries both, on [1], in Who Is Affected and in Impact and Why Now.
4. **Root cause.** As recorded above: [15] and [24] exclude it, [2] and [1] invite it, and [34] separates it. The
   bundle's placement is a POSITION.
5. **The opportunity statement.** As recorded above: an alias on [1], a separate formula in [12], and not the same
   artefact according to [28].
6. **Atlassian's play is a workshop, not a document.** [11] runs on a whiteboard divided into who, what, why and where,
   and its output is one statement that "should include who is affected, what is affecting them, why it needs to be
   solved, and where the problem is happening". The companion cites [11] for those four elements, never for a
   document layout.
7. **Time-bound.** [1] was published on 2021-08-22 and records a review on 2026-09-02. [3] was last updated on
   2021-06-21. [16] is a 2003 course template. [18] states it was updated in 2026.

---

## Notes for the companion

### Honest framing

- **This is a short document at both sizes.** The full variant adds sections that recur in sourced longer forms. It
  does not turn the statement into a business case: options, a recommended solution, a cost estimate, a project scope
  and a funding request stay out at every size, as contract section 2 requires.
- **The duplication with `business-case` is real, and the companion says so.** `business-case`'s Problem and
  Opportunity section asks the same questions inside an investment case. The standalone statement comes earlier, asks
  for no money, and decides whether a problem is worth a project brief or a business case at all. [30] contrasts the
  two by name: "the business case argues why the problem matters financially; the problem statement describes what,
  where, and how much, without the persuasive framing". The order, statement first and case only if the problem is
  worth one, is this library's POSITION; no source read sets it. (The first draft of this note said no source
  contrasted the two. The build caught it against [30] on 2026-10-11, before merge.)
- **Component or precursor.** [27] embeds a problem statement inside a product brief, and `business-case`, `prd` and
  `project-brief` in this library each carry one as a section. [20] and [26] treat it as a document written first,
  which feeds the next. This bundle builds the precursor, and its companion says that the component form is common.

### The evidentiary spine, section by section

| Section | In lean | Sources |
|---|---|---|
| Problem Statement | yes | [1] "A concise description of the problem that needs to be solved"; [15] "about 18 words long"; [11] the statement names who, what, why and where; [2] and [3] each rewrite a solution-first sentence into a problem |
| Background | yes | [1] "The background of a problem. Which organization or department has the problem and what is the problem? Why has the problem arisen?"; [11] "What is the nature of the problem? What signs point to there being a problem?" |
| Who Is Affected | yes | [1] "The people affected by the problem. There could be multiple user groups affected by a specific problem in different ways."; [11] "Who is experiencing this problem? How do we know that they are experiencing it?"; [14] "Who The Problem Most Affects" |
| Impact and Why Now | yes | [1] "The impact of the problem on the organization. If the problem is not fixed, what will be the effect on the organization?"; [11] "What happens if we don't solve it?"; [3] "You should also consider quantifying the value of solving the problem" |
| Evidence | yes | [2] "Use the evidence you gather to document your clearly defined problem." and "Is this based on evidence rather than assumptions?"; [15] "without evidence of your problem, you are left with opinion"; [4]'s quantified example against its unquantified one |
| How People Cope Today | full | [8] "How do people currently solve this problem?"; [10] "how customers work around the problem"; [32] "Describe previous attempts to solve the problem and why they failed." |
| What Is Not Part of the Problem | full | [3] "agreeing what is not part of the problem"; [16] "what is to be included and, perhaps more importantly, what isn't"; [11] "In what circumstances does it not occur?"; [42] "what aspects it encompasses and what it does not cover"; [35] "the boundaries on problem definition are really important to agree on up front". Constraints route to `project-brief` |
| How We Will Know It Is Solved | full | [12] "as determined by [these measurable changes in their behavior]"; [13] "what customer behavior or metric shift will we see?"; [8] "Metric(s) and Baseline"; [16] "A summary of the primary success criteria."; [40] "Quantitative or measurable indicators of success."; [43] "Measurability"; [38]'s output-in-disguise test; contested by [21] and [39] |
| Open Questions and Assumptions | full | [8] "Open Questions"; [33] a pre-research statement "should be considered as being based on assumptions"; [34] a suspected root cause kept as a separate step; [37] "Limitations and Constraints on Analysis" |
| Decision This Informs | yes | [3] "Your discovery is finished when you've decided whether or not you want to move on to alpha." and "It's not a failure to stop at the end of the discovery phase"; [2] "Is the problem clear enough to investigate further?"; [26] reports that once approved, the next step is possible solutions; [37] labels the field "Decision sought"; [40] places its combined template "Before governance review to support go/no-go recommendations"; [39] and [28] name a project charter as a successor. Which document takes over is this library's POSITION, from the contract's successor obligation |

**Quality rules go to the guide's rubric and the TRAP lines**, under decision procedure 12. [2]'s five questions, [1]'s
three rules ("Not be a laundry list of unrelated problems", "Not contain a solution", "Be brief"), [4]'s "Do not
include solutions in your problem statement", and [22]'s balance ("broad enough to allow for creative thinking and
innovative solutions, but narrow enough") are rubric material.

### The gap question's result, and what this build does with it

The gap dimension searched without reading the library, and found six candidates. Each is routed under procedure 12:

1. **The cost of not solving, as a number.** [30] separates the problem statement, "what, where, and how much", from a
   business case that carries "a specific dollar estimate". [31] contrasts a vague impact with a quantified one. Routed
   to Impact and Why Now's ASK, as one question, and to a rubric row. Not a section.
2. **The extent of the problem.** [29] names a "To What Extent?" component. Routed to Evidence's ASK.
3. **Prior attempts and why they failed.** [32]. Adopted into the full variant's How People Cope Today, with [8] and
   [10], because a longer-forms source carries it as a field too.
4. **One statement per stakeholder.** [33] fills its point-of-view structure once per stakeholder. Routed to the
   guide, as an anti-pattern about smoothing disagreement into one voice.
5. **A root-cause hypothesis kept separate.** [34]. Adopted as the placement under Open Questions and Assumptions.
6. **A stated confidence level, and a falsifier.** Null. No source that publishes problem statements carries either.
   Recorded so the next author does not search again from scratch.

### What the bundle must not say

- That a problem statement is a required stage gate. [3] and [7] name no written deliverable for discovery or Define.
- That McKinsey's worksheet has any particular fields. It was not read.
- That Atlassian's template has any particular layout. Only the play page was read.
- That "Min Basadur" coined "How Might We". [18] calls that "rumoured".
- Any statistic about how often teams skip problem framing. No source read carries one.
- That this library's section order is the canon's. No two sources share an order.

### GOOD and WEAK illustrations use their own scenario

The worked example frames a problem at Acme Analytics in January 2026. GOOD and WEAK text in both templates must use a
different scenario, and must not use these nouns: Priya Nair, Dana Okoro, Elena Cho, Meridian Freight, Recurring
Analyst, dataset picker, second dashboard view, 31 percent.

### The example

[`tier2-specs.md`](../../docs/internal/tier2-specs.md) fixes it: a problem statement dated 2026-01-09, written by Priya
Nair, framing the problem that the project brief (2026-01-16) and the business case (2026-01-20) later answer. It cites
only facts older than itself, names no solution, and must not cite the vision, the brief, the case or anything later as
existing.

## Sources

### CANON: WHAT A PROBLEM STATEMENT IS AND WHAT IT CARRIES

**[1] Maria Rosala, Nielsen Norman Group - "Problem Statements in UX Discovery".** primary. **fetched-and-verified.**
`https://www.nngroup.com/articles/problem-statements/`
Supports: Definition, required components, the 5 Ws, length/brevity rule, no-solution rule, write-once-vs-revisited duality, and the opportunity-statement variant
Quotable: "Problem statement: A concise description of the problem that needs to be solved."
Quotable: "In the discovery phase of a UX project, a problem statement is used to identify and frame the problem to be explored and solved, as well as to communicate the discovery's scope and focus."
Quotable: "A problem statement should include:"
Quotable: "The background of a problem. Which organization or department has the problem and what is the problem? Why has the problem arisen?"
Quotable: "The people affected by the problem. There could be multiple user groups affected by a specific problem in different ways."
Quotable: "The impact of the problem on the organization. If the problem is not fixed, what will be the effect on the organization? Reputational damage? Paying unavoidable costs? Losing out-of-market share?"
Quotable: "To gather the relevant facts for your problem statement, you can use a simple technique called the 5 Ws"
Quotable: "Who is affected by the problem?"
Quotable: "What is the problem?"
Quotable: "Where does this problem occur?"
Quotable: "When does the problem occur?"
Quotable: "Why does the problem occur? Why is the problem important?"
Quotable: "Not be a laundry list of unrelated problems . A discovery effort should have one problem statement, and the problem statement should be focused on one problem."
Quotable: "Not contain a solution . Leave solutions out of your problem statement. At the beginning of discovery, there are too many unknowns, so the the best solution is not obvious."
Quotable: "Be brief . Problem statements are effective when they're concise. If you can condense your problem statement down to a few sentences, others will quickly understand what you focus on and why, and what's out of scope."
Quotable: "It's a good idea to write a problem statement as early as possible in your discovery, as it can help set discovery goals and objectives. Many teams will compose their problem statement in a discovery kick-off workshop."
Quotable: "Throughout the discovery process, you can return to your problem statement and add to it."
Quotable: "As you begin discovery, you can return to your problem statement and refine it - particularly if you've learned root causes or how much a problem costs your organization. Another reason to update your problem statement is if the discovery changes direction"
Quotable: "Finally, at the end of the discovery process, the problem statement can be communicated alongside your findings and recommendations to provide the full narrative of the discovery process."
Quotable: "However, problem statements can also capture opportunities (in which case they are sometimes referred to as opportunity statements instead of problem statements, although they are written and used in the same way)."
Quotable: "In an opportunity statement, we need to highlight the gap between where we are now (the present state) and where we want to be in the future (the desired state)."
Quotable: "August 22, 2021 · Last reviewed Sep. 2, 2026"

**[2] Digital NSW, NSW Government - "Define the problem" (Digital Service Toolkit, Plan a project).** practitioner. **fetched-and-verified.**
`https://digital.nsw.gov.au/delivery/digital-service-toolkit/resources/plan-a-project/define-problem`
Supports: Definition/purpose, framing-the-problem research scope, the no-solution rule with its worked solution-first-to-problem-first rewrite, and the full verbatim review checklist
Quotable: "Work to define the problem you are trying to solve before exploring solutions. Start by understanding user needs and gathering evidence. Avoid relying on assumptions."
Quotable: "Start by defining the problem you're working on. A clearly defined problem creates a stronger foundation for discovery, design and delivery."
Quotable: "You might be presented with a pre-defined solution or asked to build a specific thing. Instead, you should investigate that solution and reframe it as a problem you need to solve."
Quotable: "the current service, if you are making improvements to an existing one"
Quotable: "the broad service landscape and current services available to users"
Quotable: "real needs and problems faced by your users"
Quotable: "the users' end-to-end experience with your service including tools, transactions, support and offline touch points both government and non-government."
Quotable: "Use the evidence you gather to document your clearly defined problem."
Quotable: "Look to avoid solutions in your problem statement."
Quotable: "A problem statement is not: 'We need to build an app to show people where they can buy cheap fuel'."
Quotable: "It's probably something like: 'Drivers are spending more time and money than they're saving looking for cheap fuel. Our solution needs to find a way to guide them to the cheapest fuel location for their journey.'"
Quotable: "Before proceeding to the next step, ask:"
Quotable: "Is this based on evidence rather than assumptions?"
Quotable: "Does it focus on the user's need?"
Quotable: "Have we described a problem rather than a solution?"
Quotable: "Do we understand the root cause?"
Quotable: "Is the problem clear enough to investigate further?"
Quotable: "Copyright © 2026"

**[3] Government Digital Service, GOV.UK Service Manual - "How the discovery phase works" (Agile delivery community).** primary. **fetched-and-verified.**
`https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works`
Supports: No named Define-stage deliverable (the term 'problem statement' never appears); who/when problem-defining happens (before research starts, during discovery, team-led); the no-solution-first rule in GOV.UK's own words; end-of-discovery exit criteria; licence
Quotable: "Before you commit to building a service, you need to understand the problem that needs to be solved."
Quotable: "At the start of your discovery, you might be presented with a pre-defined solution or told you're building a specific thing."
Quotable: "Before you start your research, you'll need to interrogate that solution and reframe it as a problem to be solved. This will help you better understand what your team has been set up to achieve."
Quotable: "Break down assumptions and ask lots of questions. Reframing the problem also includes agreeing what is not part of the problem."
Quotable: "For example, a problem is not: "We need to build an interactive map to show people where our contact centres are". It's probably something like: "How can we make it easier for people to find their nearest contact centre if they need to book a face-to-face appointment?""
Quotable: "So start by defining the problem you're working on. The better you define it, the better the potential solutions you'll end up with if you move on to the alpha phase."
Quotable: "You should also consider quantifying the value of solving the problem you've been set up to address."
Quotable: "Your discovery is finished when you've decided whether or not you want to move on to alpha."
Quotable: "It's not a failure to stop at the end of the discovery phase if your research shows that's the best thing to do."
Quotable: "There's no set time period for a discovery, but around 4 to 8 weeks is typical."
Quotable: "You should not start building your service in discovery."
Quotable: "Published: 4 August 2016"
Quotable: "Last updated: 21 June 2021"
Quotable: "All content is available under the Open Government Licence v3.0, except where otherwise stated"
Quotable: "© Crown copyright"

**[4] Build for Good (Open Government Products, Government of Singapore), "Writing a good problem statement".** primary. **fetched-and-verified.**
`https://www.build.gov.sg/problem-statement-guide/`
Supports: Government service-design rule (outside NSW/GOV.UK): solution-in-disguise, no-evidence, named good/bad contrast pair
Quotable: "Do not include solutions in your problem statement."
Quotable: "60% of Singaporeans lack the knowledge of what can be recycled when disposing their trash. This results in them choosing not to recycle because of the additional effort required for research, resulting in low recycling rates."
Quotable: "Singaporeans find it too troublesome to recycle. Recycling bins are also not accessible to all residential areas. Creating a central portal will help make the recycling process easier."
Quotable: "Be concrete"
Quotable: "Be specific"

**[5] Digital.gov (U.S. General Services Administration), HCD Guide Series, "Reframing" (Discovery operations guide).** primary. **fetched-and-verified.**
`https://digital.gov/guides/hcd/discovery-operations/reframing`
Supports: Government guidance (US, outside NSW/GOV.UK) on problem framing shaping solutions, and a definitional note on root cause
Quotable: "Who is this project for? What are you trying to understand? Why is this a problem? What is the goal of the project?"
Quotable: "how we define a problem largely defines its solution, and typically design problems and solutions co-evolve"
Quotable: "The fundamental reason for the occurrence of a problem"

**[6] Stanford d.school, CS377 course handout - "Developing a Point of View" (Adventures in Design Thinking series).** primary. **fetched-and-verified.**
`https://hci.stanford.edu/courses/cs247/2011/readings/dschool-pov.pdf`
Supports: Equivalent discovery-era construct from design thinking (Point of View) as a separate but adjacent lineage to 'problem statement'; the User+Need formula; its own no-named-deliverable gap relative to the problem-statement canon; author/date; absence of an explicit licence statement
Quotable: "One of the most challenging creative leaps to make in design work is to move from the concrete world of observations to a concisely stated point of view."
Quotable: "User + Need = Point of View"
Quotable: "Great ones can be compressed to fit on a bumper sticker. Points of view are built out of two things, an understanding of a user group (hopefully a unique empathic understanding) and insight into a need that group has."
Quotable: "Most teams are handed a Point of View or a Problem Statement and never look back."
Quotable: "You know you're done with the observe phase when you have your Point of View."
Quotable: "Developing a Point of View (from CS377 course, Winter 2006)"
Quotable: "September 2006"

**[7] Design Council - "Framework for Innovation" (the Double Diamond).** primary. **fetched-and-verified.**
`https://www.designcouncil.org.uk/our-resources/framework-for-innovation/`
Supports: No named Define-stage deliverable (the page names four stages - Discover, Define, Develop, Deliver - and never names 'problem statement' as the artifact of the Define stage); licence
Quotable: "Discover. The first diamond helps people understand, rather than simply assume, what the problem is. It involves speaking to and spending time with people who are affected by the issues."
Quotable: "Define. The insight gathered from the discovery phase can help you to define the challenge in a different way."
Quotable: "Develop. The second diamond encourages people to give different answers to the clearly defined problem, seeking inspiration from elsewhere and co-designing with a range of different people."
Quotable: "Deliver. Delivery involves testing out different solutions at small-scale, rejecting those that will not work and improving the ones that will."
Quotable: "This is not a linear process as the arrows on the diagram show."
Quotable: "This work by the Design Council is licensed under a CC BY 4.0 license ."
Quotable: "Launched in 2004, the Double Diamond has become world-renowned with millions of references to it on the web."
Quotable: "© 2026 Design Council"

### LONGER AND SECTIONED FORMS: WHAT A FULL VARIANT CAN CARRY

**[8] Heap Inc., "Problem Brief" (downloadable PDF worksheet).** vendor. **fetched-and-verified.**
`https://assets.ctfassets.net/jicu8fwm4fvs/1AzbAw352qJOGUF42PmLeh/679f6fa198903ccb2d19fa2c5f44e188/heap-problem-brief.pdf`
Supports: A full, sectioned, multi-page written problem-statement document (not a canvas): page-by-page labelled fields beyond background/people-affected/impact
Quotable: "Hypothesis statement and metrics. To be filled out last."
Quotable: "Statement: Describe the hypothesis driving this project. Example: [user / account segment] experiences [negative outcome] because [reason], so we expect that solving this problem will cause [measurable, specific behavior change]."
Quotable: "Metric(s) and Baseline: Define how you'll evaluate success."
Quotable: "Business Impact: How does moving the metric above impact your business' revenue, cost, or risk?"
Quotable: "Problem Statement. What pain point(s) are we trying to address?"
Quotable: "What is the project type and our justification for doing this project? *See table at end."
Quotable: "How do people currently solve this problem?"
Quotable: "How do our competitors address this problem?"
Quotable: "What are the jobs-to-be-done to address? P0 "Must have"... P1 "Nice to have"..."
Quotable: "Launch Plan"
Quotable: "When do we expect to launch? Will there be several milestones, or one global launch?"
Quotable: "Open Questions"
Quotable: "Additional Resources"
Quotable: "Required Justification (link to any relevant source) • Number of votes in ProductBoard • Net impacted customer ARR across those votes • Frequency of running into this issue in a given account..."

**[9] Heap Inc., "The Problem Brief" landing page.** vendor. **fetched-and-verified.**
`https://heap.io/resources/product-management/problem-brief`
Supports: Confirms the Problem Brief is positioned as the first of a three-worksheet series (Problem Brief, then a Design Brief) and frames it around three guiding questions
Quotable: "A worksheet for defining product problems."
Quotable: "we've put together three worksheets to help you implement a repeatable process for getting to the why"
Quotable: "align your teams around the problem you're trying to solve before prescribing a solution for it"

**[10] Vijay Umapathy (Senior Director of Product Management, Heap), "PMs: Clarify the Problem, Not the Solution. Here's How." (heap.io/blog).** vendor. **fetched-and-verified.**
`https://heap.io/blog/pms-clarify-the-problem-not-the-solution-heres-how`
Supports: The authored rationale and exact fields behind the Problem Brief: the Product Hypothesis formula, the five justification types, prioritized user stories, baseline/target metrics, leading-vs-lagging metric distinction
Quotable: "a document that lays out the problem to be solved and argues for why we should choose to solve this particular problem"
Quotable: "[user / account segment] experiences [negative outcome] because [reason], so we expect that [specific product change] will cause [measurable, specific behavior change]"
Quotable: "Requested capability (justified by a number of customer requests and impacted revenue summed across those customers) Update to an existing workflow... New workflow... Operational improvement... Risk mitigation..."
Quotable: ""As a {persona}, I want to {do a job}, so that {my business has an outcome}.""
Quotable: "which capabilities are "must have" vs "nice to have""
Quotable: "It's important to make your hypothesis measurable."
Quotable: "is this a leading metric... Or is it a lagging metric that will only truly manifest over months"
Quotable: "framing a problem means codifying a set of customer context around that problem, including what matters to the customer... which segments of customers have the problem, how customers work around the problem, how our competitors solve the problem, and how we will know that we've successfully solved the problem"

**[11] Atlassian Team Playbook, "Problem Framing" play.** vendor. **fetched-and-verified.**
`https://www.atlassian.com/team-playbook/plays/problem-framing`
Supports: A board/workshop method (not a written document): structured by who/what/why/where, explicitly excludes root-cause or solution content, and final statement must name who/what/why/where
Quotable: "Let your team know that the goal today is to understand and define the problem, not to solve it."
Quotable: "Who is experiencing this problem? How do we know that they are experiencing it? What feedback have we received from them on it?"
Quotable: "What is the nature of the problem? What signs point to there being a problem?"
Quotable: "Why is the problem worth solving? What's the impact on the people experiencing the problem? What happens if we don't solve it?"
Quotable: "In what circumstances is this problem occurring? In what circumstances does it not occur?"
Quotable: "The problem statement should include who is affected, what is affecting them, why it needs to be solved, and where the problem is happening."

**[12] Jeff Gothelf, "Business Problem Statements vs Opportunity Statements".** practitioner. **fetched-and-verified.**
`https://jeffgothelf.com/blog/business-problem-statement-opportunity-statement/`
Supports: The verbatim Business Problem Statement formula (Lean UX Canvas Box 1) including the measurable-criteria clause requested by the task, plus the alternate Business Opportunity Statement formula for net-new initiatives
Quotable: "[Our product] was originally designed to [play in this space and win in this way]. We have observed [in these ways] that the product isn't meeting our expectations which is causing [this negative impact] to our business."
Quotable: "How might we [adjust our strategy & ways to win] so that our customers are more successful as determined by [these measurable changes in their behavior]?"
Quotable: "The current state of [domain] has focused mainly on [segments, pain points, etc.]"
Quotable: "What existing products / services fail to address is [this gap]."
Quotable: "Our product / service will address this gap by [vision / strategy]."
Quotable: "Our initial focus will be [this segment]."
Quotable: "We'll know we are successful when we see [these behaviors in our target audience.]"
Quotable: "My advice is to try the Business Problem Statement first. If it doesn't make sense after you've given it a shot, go for the Opportunity Statement."

**[13] Jeff Gothelf, "How to use the Lean UX Canvas" (video transcript).** practitioner. **fetched-and-verified.**
`https://jeffgothelf.com/blog/how-to-use-the-lean-ux-canvas/`
Supports: Confirms the business problem statement is one box of a larger canvas (board format, not a standalone sectioned document) and that it must end in a measurable customer-behavior question
Quotable: "We'll start off with the business problem statement. That's box number 1."
Quotable: "the final piece in here is if we solve it, how we will we know? In other words, what customer behavior or metric shift will we see?"
Quotable: "There's no solutions in here."

**[14] NHS National Services Scotland (hosted by HIS/Design Community), "Problem Framer" tool.** practitioner. **fetched-and-verified.**
`https://www.hisengage.scot/equipping-professionals/designing-person-centred-services/tool-directory/problem-framer/`
Supports: A public-sector canvas/board template (PowerPoint-based, used at the end of the first Double-Diamond diamond) with explicit labelled sections beyond background/who/impact: points of view, barriers, opportunities, how-might-we questions, vision, a breadth-check map, and project type
Quotable: "Problem Statement"
Quotable: "Why Is This A Problem?"
Quotable: "Points Of View"
Quotable: "Who The Problem Most Affects"
Quotable: "Who The Problem Benefits"
Quotable: "Project Barriers"
Quotable: "Project Opportunities"
Quotable: "How Might We Questions"
Quotable: "Project Vision"
Quotable: "Problem Map"
Quotable: "Project Type"

**[15] Improvement Cymru Academy (NHS Wales), "Understanding your Problem" toolkit guide (PDF).** practitioner. **fetched-and-verified.**
`https://performanceandimprovement.nhs.wales/functions/quality-safety-and-improvement/improvement/improvement-cymru-academy/resource-library/academy-toolkit-guides/understanding-your-problem-toolkit-guide/`
Supports: A written, deliberately short artefact (contrast case): an explicit rule that a problem statement is one short sentence that must NOT contain a solution or a root cause, which bears directly on what a longer form is adding beyond
Quotable: "It is typically about 18 words long and will often convey what the current 'pain' is and the consequences of the problem."
Quotable: "It is important to note that problem statements do not describe the solution or root causes."
Quotable: "A successful problem statement will contain context of what the problem is."
Quotable: "Doesn't indicate a solution or a cause."
Quotable: "Explains impact of the problem (e.g. `patients wait too long')"
Quotable: "Data plays a vital role in understanding your problem; without evidence of your problem, you are left with opinion."

**[16] Rose-Hulman Institute of Technology, CSSE 333 course, "Problem Statement Guide" / template (PDF, dated 3 September 2003).** practitioner. **fetched-and-verified.**
`https://www.rose-hulman.edu/class/csse/csse333/Project/Samples/problem_statement_template.pdf`
Supports: A university-authored, explicitly sectioned written problem statement with numbered headings covering scope, success criteria, a four-part detailed-requirements breakdown, a stakeholders table, and a revision-history table - directly answering what a longer/sectioned form can carry
Quotable: "1. High Level Problem Summary"
Quotable: "<"Elevator statement" describing the problem to be solved - a single sentence that captures the essence of the issue.> <A summary of the primary success criteria.> <A description of the scope of the project, what is to be included and, perhaps more importantly, what isn't.>"
Quotable: "2. Detailed Problem Statement"
Quotable: "2.1 FUNCTION"
Quotable: "2.2 FORM"
Quotable: "2.3 ECONOMY"
Quotable: "2.4 TIME"
Quotable: "3. Key Stakeholders"
Quotable: "4. Revision History"

### CONTESTED PRACTICE: MEASURES, CADENCE AND WHOSE PROBLEM

**[17] Stanford d.school, "bootcamp bootleg" (hosted copy, Kent CS).** primary. **fetched-and-verified.**
`https://www.cs.kent.ac.uk/people/staff/saf/patterns/gallery/BootlegBootcamp.pdf`
Supports: The original Design Thinking source for the POV/problem statement: its format, its explicitly user-centred composition, its revisability, and the Critical Reading Checklist's validity criteria
Quotable: "You revisit and reformulate as you learn by doing"
Quotable: "A point-of-view (POV) is your reframing of a design challenge into an actionable problem statement that will launch you into generative ideation. ... Use the following madlib to capture and harmonize three elements of a POV: user, need, and insight. [USER] needs to [USER'S NEED] because [SURPRISING INSIGHT]"
Quotable: "Is it User-centered, Need-based, and Insight-driven?"
Quotable: "Use this Checklist to ensure that your team's POV is valid, insightful, actionable, unique, narrow, meaningful, and exciting."

**[18] Interaction Design Foundation, "What is How Might We (HMW)?" (literature topic page, updated 2026).** reference. **fetched-and-verified.**
`https://ixdf.org/literature/topics/how-might-we`
Supports: The HMW/POV relationship, the HMW formula, and the two competing origin-lineage claims for the HMW phrase
Quotable: "How Might We (HMW) is a design thinking method that allows designers to reframe and open up their problem statements for efficient, targeted and innovative ideation sessions to help solve design challenges. HMW is the bridge between the Define and Ideate stages of the design thinking process."
Quotable: "“How might we” + Intended Action (as an action verb) + “for” + Potential User (as the subject) + “so that” + Desired Outcome."
Quotable: "Step 1: Clearly define the problem or challenge with a concise problem statement to capture the core of the problem. This sets the foundation for HMW questions."
Quotable: "In the Define mode, you should end up creating an actionable problem statement which is commonly known as the Point of View (POV) in Design Thinking."
Quotable: "Your POV should never contain any specific solution, nor should it contain any indication as to how to fulfill your users’ needs"
Quotable: "You should construct a narrowly-focused problem statement or POV as this will generate a greater quantity and higher quality solutions"
Quotable: "The Phrase is rumoured to have been popularized by Min Basadur at Proctor and Gamble, then on to IDEO, next at Google and later at Facebook in a viral breakout, that has since revolutionised how companies frame their innovation challenges. GK Van Platter of Humantific references a much earlier example in an article entitled, Origins of How Might We? (2012). The reframing technique has its roots all the way back in the mid-sixties, with a work by Sidney J. Parnes Ph.D "Creative Behavior Guidebook", which touches on the concept of "Invitation Stems" or "How Mights"."

**[19] IDEO.org, Design Kit, "How Might We" method page.** primary. **fetched-and-verified.**
`https://www.designkit.org/methods/how-might-we.html`
Supports: IDEO.org's own (shorter, non-attributing) description of HMW, confirming the problem-to-opportunity reframing logic without naming an origin
Quotable: "By defining themes and insights, you’ve identified problem areas that pose challenges to the people you’re designing for. Now, try reframing your insight statements as How Might We questions to turn those challenges into opportunities for design."
Quotable: "A properly framed How Might We doesn’t suggest a particular solution, but gives you the perfect frame for innovative thinking."

**[20] Institute of Project Management, "Problem Statement Template for Project Managers (2026)".** practitioner. **fetched-and-verified.**
`https://instituteprojectmanagement.com/blog/problem-statement-template/`
Supports: The PM-practice camp: success criteria belong inside the problem statement, and the statement is written once, at the earliest stage, before the charter
Quotable: "It typically includes a problem definition, background context, stakeholders affected, root cause analysis, business impact, desired outcome, and success criteria."
Quotable: "Desired Outcome: A clear statement of what success looks like once the problem is addressed. Success Criteria: Specific, measurable indicators that will confirm the problem has been solved."
Quotable: "The problem statement belongs at the very start of the project lifecycle, during the initiation phase, before the project charter is drafted and before the scope is defined. This timing is deliberate."
Quotable: "Used at the earliest stage of project initiation, a well-written problem statement ensures that everyone involved understands exactly what needs to be solved and why it matters, before a single resource is committed or a scope boundary is drawn."

**[21] Queensland Government, Digital Service Design Playbook, "Defining success" play (Digital Service Design Office, Dept. of Transport and Main Roads).** primary. **fetched-and-verified.**
`https://www.forgov.qld.gov.au/service-delivery-and-community-support/design-and-deliver-public-services/digital-service-design-playbook/all-plays/defining-success`
Supports: The opposing camp on (a): success criteria/metrics are deliberately a separate, later activity from writing the problem statement, and outcome is explicitly distinguished from metric
Quotable: "Make sure you have a clearly defined problem ... You should already have a well-defined problem."
Quotable: "The outcome is the impact of your project. The outcome is not an output or a metric of your project."
Quotable: "A metric is a measurement that indicates whether the impact of the project is being achieved."
Quotable: "Running Defining success in the discovery stage ensures that your project team has a clear understanding of what success means and how to measure it."

### FAILURE MODES AND QUALITY BARS

**[22] Cynthia Vinney, "What Is a Problem Statement in UX? (And How To Write One)", CareerFoundry blog.** practitioner. **fetched-and-verified.**
`https://careerfoundry.com/en/blog/ux-design/problem-statement-ux/`
Supports: Solution-in-disguise rule; too-broad/too-narrow scope heuristic; symptom-vs-root-cause via 5 Whys as a heuristic method, not a fixed rule
Quotable: "a user doesn't need to be able to use two-factor authentication to get into a banking app, they need to be able to access their banking information securely"
Quotable: "The problem statement should lay out the user's need (secure access) but leave out any possible solutions (two-factor authentication), which shouldn't be considered until further along in the design process."
Quotable: "if it's too broad, it will leave too many possible solutions open, making it challenging to arrive at the best one. ... it should be broad enough to allow for creative thinking and innovative solutions, but narrow enough that it can provide a direction for that solution."
Quotable: "While this technique is referred to as the 5 Whys, the number five is only a rule of thumb. ... you should stop asking why once your answers are no longer valuable in defining the problem."
Quotable: "make sure each answer to a "why" question is grounded in a real world issue so you can reach a concrete conclusion about the reason for the users' challenge"
Quotable: "the answer to each "why" question has more than one legitimate answer ... you should follow each branch of questioning because it could reveal your user has more than one problem"

**[23] Syed Balkhi, "7 Effective Ways to Craft Compelling Problem Statements for UX Design", UXmatters.** practitioner. **fetched-and-verified.**
`https://www.uxmatters.com/mt/archives/2024/02/7-effective-ways-to-craft-compelling-problem-statements-for-ux-design.php`
Supports: Vague-users rule, too-broad/vague-scope rule, no-evidence-asserted-without-source rule
Quotable: "Many people provide vague problem statements that can confuse UX designers. So try to avoid making vague or overly broad statements."
Quotable: "In defining a problem statement, specify the target audience, the platform, and the specific scenarios in which the problem occurs."
Quotable: "You should also try to provide data and evidence that supports the existence of the problem. If necessary, conduct user research and usability testing and gather analytics data to quantify the impacts of the issue."
Quotable: "Increase the credibility of your problem statement by combining quantitative and qualitative elements of the problem statement."

**[24] Epec Engineered Technologies, "5 Whys Root Cause Analysis Starts with a Problem Statement", Epec blog.** practitioner. **fetched-and-verified.**
`https://blog.epectec.com/5-why-root-cause-analysis-starts-with-a-problem-statement`
Supports: Root-cause method (5 Whys/A3/CAPA) explicitly tied to writing the statement; blame/predetermined-cause rule stated as a defining feature of a good statement
Quotable: "A problem is merely the difference between the way things are and the way things need to be."
Quotable: "The difficulty in writing a good problem statement often stems from knowing too much."
Quotable: "Both examples beg the question and infer a solution. This approach handicaps our problem-solving efforts."
Quotable: "“Workers are making mistakes because there is no work instruction.” “We need to perform 5S at the production work cells.”"
Quotable: "It describes the difference between the actual conditions and the desired conditions. It does not offer commentary on a proposed solution. It does not attempt to diagnose the problem, nor assign blame. It is objective and factual."
Quotable: "A great problem statement goes even further: It ties to company goals. It is measurable, not qualitative."
Quotable: "Withhold whatever else you believe to know about the source of the problem. Do not use the problem statement to propose a solution."

### BOUNDARIES: THE BUSINESS CASE, THE CHARTER AND THE PRODUCT BRIEF

**[25] Association for Project Management (APM UK), official online glossary (sourced from the 5th-8th editions of the APM Body of Knowledge).** primary. **fetched-and-verified.**
`https://www.apm.org.uk/glossary`
Supports: Refutes the premise that APM BoK lists 'problem statement', 'project brief' and 'project charter' as interchangeable common-usage names
Quotable: "Problem In project management terms these are concerns that the project manager has to deal with on a day-to-day basis."
Quotable: "Brief The output of the concept phase of a project or programme."
Quotable: "Charter A document that sets out the working relationships and agreed behaviours within a project team."
Quotable: "Project brief See Brief."
Quotable: "Project charter See Charter."

**[26] Deb Schaffer, "How to Write a Problem Statement", ProProject Manager Blog.** practitioner. **fetched-and-verified.**
`https://www.proprojectmanager.com/problem-statement/`
Supports: PMBOK's own treatment of 'problem statement' is marginal and not tied to a named initiation artifact; the author's own model hands the problem statement to a project plan's deliverables section, not to charter/brief/case
Quotable: "As important as the problem statement is in creating a plan that solves it, PMI doesn’t focus on problem statements."
Quotable: "On page 236 of the Project Management Book of Knowledge (PMBOK), 5th edition, the only reference to “problem statement” appears in the Project Quality Management section under Cause and Effect Diagrams: “The problem statement typically describes the problem as a gap to be closed or as an objective to be achieved.”"
Quotable: "In the 6th Edition of the PMBOK, we get even less direction. On page 415, under Data Analysis, the reference is to use a problem statement as part of a root cause analysis. “It can be used to identify threats by starting with a problem statement…”"
Quotable: "You’re not solving the problem here - just stating what the problem is and the ramifications of not solving it."
Quotable: "After the problem statement is created and approved, it’s time to move on to possible solutions."
Quotable: "The solution is found in the deliverables section of the project plan."

**[27] Productboard glossary, "Product Brief: Definition, Template & Best Practices".** vendor. **fetched-and-verified.**
`https://www.productboard.com/glossary/product-brief/`
Supports: In this source's model, 'Problem Statement' is one section inside a product brief, not a standalone document, and the chain runs brief -> PRD -> specs
Quotable: "1. Problem Statement A clear, concise description of the user problem or business opportunity. Avoid solution language; focus on the pain point or unmet need."
Quotable: "Unlike a PRD (Product Requirements Document) or product spec that details what to build and how to build it, a product brief focuses on the why: the problem worth solving, the users affected, and the business value at stake."
Quotable: "Product Brief: Problem-focused, created early in discovery to align on opportunity and validate assumptions. Answers "why should we work on this?""
Quotable: "The brief comes first, informing whether to proceed with a PRD. The PRD then guides creation of detailed specs."

**[28] ModernAnalyst.com, "Why Problems and Opportunities are NOT the same for projects".** practitioner. **fetched-and-verified.**
`https://www.modernanalyst.com/Resources/Articles/tabid/115/ID/5065/Why-Problems-and-Opportunities-are-NOT-the-same-for-projects.aspx`
Supports: Business-analysis practitioner source names Business Cases and Project Charters as the documents a clearly defined problem statement feeds into
Quotable: "Most professionals in project management understand that in order to successfully approach a project, the problem statement must be clearly defined. The problem is that many practitioners treat problems and opportunities interchangeably when developing Business Cases and Project Charters."
Quotable: "many practitioners treat problems and opportunities interchangeably when developing Business Cases and Project Charters"

### THE GAP QUESTION

**[29] Six Sigma DSI (Six Sigma Development Solutions, Inc.) - "Problem Statement".** practitioner. **fetched-and-verified.**
`https://sixsigmadsi.com/problem-statement/`
Supports: A named, explicit 'extent/magnitude' element distinct from a simple impact line - how big and how widespread the problem is, backed by cited evidence; also surfaces a contested point (this source recommends including a working-thesis solution inside the problem statement)
Quotable: "To emphasize the significance of the problem, it is essential to explain the extent or magnitude of the issue."
Quotable: "could include data or qualitative descriptions that reveal the seriousness and widespread nature of the problem"
Quotable: "evidence from existing research, case studies, or personal experience"
Quotable: "a claim or working thesis that presents a potential solution or approach"

**[30] Six Sigma DSI (Six Sigma Development Solutions, Inc.) - "Business Case".** practitioner. **fetched-and-verified.**
`https://sixsigmadsi.com/business-case/`
Supports: A quantified cost-of-the-problem figure, and a cost-of-not-acting framing, kept as a distinct element from the problem statement itself
Quotable: "the problem statement describes what, where, and how much, without the persuasive framing"
Quotable: "A specific dollar estimate, even a rough one, gives a sponsor something concrete to weigh"
Quotable: "Occurrence rate × cost per occurrence × annual volume = estimated annual cost"
Quotable: "is a distinct document with its own job"
Quotable: "the business case argues why the problem matters financially"

**[31] Tom McDowall, idtips (Instructional Design Tips newsletter) - "A Practical Guide to Defining Business Problems" (2025-10-01).** practitioner. **fetched-and-verified.**
`https://idtips.substack.com/p/a-practical-guide-to-defining-business`
Supports: A quantified impact/cost line distinct from a vague impact statement; contrast between vague and quantified problem framing
Quotable: "Our current situation is:"
Quotable: "This creates the following impact:"
Quotable: "Onboarding is too slow and people don't like it."
Quotable: "new starters take six weeks to complete onboarding"
Quotable: "we're spending £12,000 per cohort on travel and venue costs"

**[32] University of Waterloo, Co-operative Education - Velocity Co-op Problem Award submission form.** practitioner. **fetched-and-verified.**
`https://uwaterloo.ca/co-operative-education/co-op-student-awards/velocity-co-op-problem-award/submission-form`
Supports: A named field asking for prior attempts to solve the problem and why they failed, as its own section distinct from the problem description
Quotable: "Failure analysis"
Quotable: "Describe previous attempts to solve the problem and why they failed."

**[33] Canada School of Public Service / École Canada - "Point-of-View (POV) Problem Statement" job aid.** practitioner. **fetched-and-verified.**
`https://ecolecanada.gc.ca/tools/jobaids/pdfs/pov-statement-eng.pdf`
Supports: Writing one problem statement per stakeholder perspective, rather than a single neutral statement, so differing stakeholder framings are surfaced side by side instead of merged
Quotable: "Any POV problem statement done before doing design research and consulting stakeholders should be considered as being based on assumptions."
Quotable: "I am an inspector and I am trying to document a case of non-compliance, but I cannot take pictures because my device is not secure, which makes me feel vulnerable and inefficient."
Quotable: "Your POV problem statement should not contain any specific solutions, but rather be broad enough in scope to open opportunities for alleviating the users' and stakeholders' pain points."
Quotable: "frame a problem by identifying pre-research assumptions and focusing on the design goals"

**[34] University of South Carolina, Organizational Excellence office - "A3 Problem Solving" template (Version 2.0, landscape).** practitioner. **fetched-and-verified.**
`https://www.sc.edu/about/offices_and_divisions/organizational_excellence/documents/problem_solving_template_a3_landscape.pdf`
Supports: Root-cause analysis held as its own separately numbered, explicitly hypothesis-framed step, structurally distinct from the problem statement and from the goal statement
Quotable: "1. Problem Statement Describe the problem in 1-2 sentences."
Quotable: "2. Importance Why is it important to solve this problem?"
Quotable: "3. Current Condition What do you see that indicates a problem?"
Quotable: "4. Goal Statement What are you aiming for and by when? Be specific so you'll know when you're successful. Use numbers whenever possible."
Quotable: "5. Root-Cause Analysis What is your most likely root cause?"
Quotable: "6. Countermeasures What action(s) will you take to reduce or eliminate the root cause?"

### GAP-FILL, 2026-10-11: MEASURES, THE DECISION AND CONSTRAINTS

A three-dimension gap-fill pass ran after drafting, on four questions the first pass left thin: McKinsey's worksheet,
a constraints field, a field naming the decision, and success measures that name no solution. It returned 11 owned
sources and 65 quotations. Nine sources are recorded below. A Wiley product page carried no quotation, and a
University of Maryland course template restates what [42] shows; both are left out. 56 quotations passed against the
cached raw text on the first pass. Of the nine that did not, six were [35]'s, whose PDF had not been cached; [35] is
described below. One sat in [36]'s cached copy, which turned out to be truncated, so its full text layer was
re-extracted from the PDF, and every [36] quotation passes against it. One was [40]'s, which an agent wrote with
single quotes where the page has "better" in double quotes; it is quoted as the page has it. The last was the
University of Maryland source, which is left out. The pages whose fresh fetch returned a `.docx` or PDF the fetcher
could not render ([37] and [42]) are accounted for by their first-pass match, as in the header of this file.

[35] needs its own note. Its text layer was extracted from the publisher's PDF and checked like every other source.
The tests the authors apply to a problem definition sit in an exhibit on page 5 that is rendered as an image, which
no text check can reach. The main loop read that exhibit off the page. It is paraphrased in [35]'s Supports line and
is never quoted anywhere in this bundle.

**[35] Charles Conn and Robert McLean, *Bulletproof Problem Solving* (Wiley), chapter 1 "Learn the Bulletproof Problem Solving Approach", publisher's excerpt PDF.** primary. **fetched-and-verified.**
`https://media.wiley.com/product_data/excerpt/24/11195530/1119553024-191.pdf`
Supports: The first step of the authors' seven-step cycle is defining the problem, and its boundaries are agreed before analysis starts. The page-5 exhibit, read off the page image and paraphrased, not quoted: a problem definition is agreed by those involved in making the decision, and is tested for being specific, for clearly measurable success, for bounds of time frame and of the decision maker's values, and for leading to definitive action
Quotable: "As we'll see later, the boundaries on problem definition are really important to agree on up front."
Quotable: "Rob knows that constraining the scope of the problem with clear boundaries makes problem solving more accurate and speedy (step 1)."

**[36] Arif Sirinterlikci (Robert Morris University), "Developing Sound Problem Statements for Course and Capstone Projects", ASEE Annual Conference paper (2026), Paper ID #51928.** academic. **fetched-and-verified.**
`https://peer.asee.org/developing-sound-problem-statements-for-course-and-capstone-projects.pdf`
Supports: In engineering capstone teaching, constraints are a stage of their own after the need statement and the goals, and ABET requires an engineering problem statement to name realistic constraints. The constraints named bound a design, that is, a solution, and the paper puts them inside the problem statement: a dissent from this bundle's routing
Quotable: "The constraints need to be added to your problem statement"
Quotable: "the workflow of developing need statements, addressed by responsive goals and objectives, and constrained by defining specifications"
Quotable: "A design constraint is a limitation, a boundary beyond which the design should not go, including weight, size, cost, societal and political factors, and be realistic."
Quotable: "Identification of Constraints: ABET requires problem statements to include "realistic constraints" such as economic, environmental, social, political, ethical, health and safety, manufacturability, and sustainability factors."
Quotable: "present all relevant assumptions and constraints clearly before attempting a solution"

**[37] New Zealand Ministry for Regulation, "Regulatory Impact Statement" template (.docx).** primary. **fetched-and-verified.**
`https://regulation.govt.nz/assets/Uploads/regulatory-impact-statement-template.docx`
Supports: A government template whose coversheet labels the decision the document feeds, and whose body asks for the limits of the evidence and whether the decision can still be made. Its problem definition is one section of an options analysis, so the whole document is a neighbour of `business-case`, not a problem statement
Quotable: "Decision sought"
Quotable: "eg, analysis produced for the purpose of informing: final/in-principle Cabinet decisions, the release of a discussion document, etc."
Quotable: "Summary: Problem definition and options"
Quotable: "What is the policy problem?"
Quotable: "Limitations and Constraints on Analysis"
Quotable: "Outline all significant limitations and constraints e.g. lack of data, other forms of evidence, constraint on the range of options considered, lack of time or freedom to consult"
Quotable: "To what extent have any limitations or constraints impacted on the quality of the analysis and can Cabinet still make an informed decision?"

**[38] Teresa Torres, "Outcomes vs. Outputs: What's the Difference and Why Does It Matter?", Product Talk (2026), drawing on Josh Seiden.** practitioner. **fetched-and-verified.**
`https://www.producttalk.org/2026/03/outcomes-vs-outputs/`
Supports: A success measure describes a change in people's behaviour, not a feature's adoption; a test for an output disguised as an outcome
Quotable: "An outcome is a change in human behavior that drives business results."
Quotable: "it's what I call a traction metric - it measures adoption of a single feature, not value to the customer."
Quotable: "If you can achieve the metric without actually helping customers, it's probably an output in disguise."
Quotable: "When you measure success by what you ship, you get a feature factory."
Quotable: "Increase the number of course views that include reviews."

**[39] UC Berkeley, Business Process Management Office, "Define Objectives and Success Measures".** practitioner. **fetched-and-verified.**
`https://bpm.berkeley.edu/node/84`
Supports: Measurable objectives are derived from the problem statement as a later step, and go into a project charter; the later-and-separate camp on success measures, and one named successor document
Quotable: "Convert your problem statement into objectives you can actually measure."
Quotable: "Good objectives are specific and measurable. If you can't say how you'd measure it, it isn't an objective yet, it's a hope."
Quotable: "Your objectives and success measures go straight into your Project Charter."

**[40] University of Arkansas IT knowledge base (uark TeamDynamix), "Problem Statement & Business Case (Template + Field Definitions)".** practitioner. **fetched-and-verified.**
`https://uark.teamdynamix.com/TDClient/33/Portal/KB/ArticleDet?ID=1545`
Supports: A combined template, the component form, with a success-metrics field separate from expected outcomes, used before a governance go/no-go review; its success-metric example carries a target
Quotable: "Describe what is happening today and who it impacts."
Quotable: "What "better" looks like in operational terms."
Quotable: "Quantitative or measurable indicators of success."
Quotable: "50% reduction in cycle time; zero compliance findings."
Quotable: "used to support Discovery alignment, prioritization, and governance-ready decision-making"
Quotable: "Before governance review to support go/no-go recommendations"

**[41] University of Washington Bothell, School of STEM, "Guidelines for CSS Capstone Proposal" (2024).** practitioner. **fetched-and-verified.**
`https://www.uwb.edu/stem/wp-content/uploads/sites/31/2024/09/stem-ms-css-defense-proposal-guidelines-1.pdf`
Supports: A proposal, a project-level document written for a committee's decision, labels constraints beside risks and resources; constraints sit at the level of `project-brief`, not of a problem statement
Quotable: "Constraints, Risks, and Resources"
Quotable: "Key constraints"
Quotable: "The problem or opportunity you will be working on"
Quotable: "in order to enable your committee to evaluate, ask questions about, and guide your work over the coming weeks and months"

**[42] VinUni College of Engineering and Computer Science, Capstone Project Template (Overleaf).** practitioner. **fetched-and-verified.**
`https://da.overleaf.com/latex/templates/vinuni-cecs-capstone-project-template/tyxpkxytpwpn.pdf`
Supports: A document template with a labelled scope sub-field directly under its problem statement, naming what the problem does not cover
Quotable: "1.2.1 Problem Statement"
Quotable: "State the problem in a single sentence or a brief paragraph."
Quotable: "1.2.2 Context and Scope"
Quotable: "what aspects it encompasses and what it does not cover"

**[43] Boston University, CIDA, "Crafting Effective Problem Statements" (2024).** practitioner. **fetched-and-verified.**
`https://www.bu.edu/cida/2024/10/18/crafting-effective-problem-statements`
Supports: Measurability named as an element of a problem statement, independent of any solution
Quotable: "Measurability: Include quantifiable elements where possible"
