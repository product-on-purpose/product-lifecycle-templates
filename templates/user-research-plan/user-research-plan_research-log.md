# user-research-plan: research log

Research conducted 2026-10-24. The stored copies carry fetch stamps of 2026-10-23 for 17 sources, the day of the
admission sweeps, and 2026-10-24 UTC for the other 20. The research builds on the two admission sweeps of
2026-10-23, the plan's and the report's, whose digests sit in gitignored folders under `_local/research/`. It builds
on ADR 0081 (adopt the research-docs family contract) and on the approved spec
(`docs/internal/tier2-specs.md:6963-7397`). The maintainer's ten rulings of 2026-10-24 (`:7376-7393`) fix the
sizes, the eleven sections and the example. This bundle is the plan only, catalog entry 210 (the user research
plan), tracked as issue #316 (bundle: user-research-plan). The report, entry 18, is a later build. The build ran
six dimensions. Three read published plans: government digital services' long form, vendors' and practitioners'
short form, and the usability block. Two read practice and its debates, and the gap question. One read the
library's own neighbours and the Acme Analytics chain. The working files are numbered differently. `dim1.md` holds
government services, `dim2.md` the library chain and `dim3.md` vendors. `dim4.md` holds the usability block,
`dim5.md` practice and `dim6.md` the gap question. The headers inside the files carry yet other numbers, so go by
file name.

**37 sources are recorded below, and all 37 are fetched-and-verified.** By tier they are 21 practitioner, 8
vendor, 4 standards, 3 academic and 1 primary. The four standards sources are GOV.UK's two Service Manual pages
[4], [21], the GOV.UK Design System [20] and Defra's Digital Service Manual [22]. The three academic sources are
course pages from the University of Washington [15], the University of Calgary [16] and Michigan Tech [17]. The
primary source is the University of Westminster's privacy statement for its UX research [36]. Two fetched sources
carry little. Washington's page is an abstract that links to a template nobody opened [15]. CleverX's
thematic-analysis tutorial is a negative result, read for something it did not contain, and carries no quotation
[37]. **473 Quotable lines remain.** Quotable lines render the sources' long dashes as hyphens and keep their curly
apostrophes; copy them as they stand.

**Every quotation was checked against the source's raw text**, not against a retrieval tool's summary. Five
dimensions returned 344 quotations from 36 web sources. Government services returned 122, vendors 82 and the
usability block 61. Practice returned 52 and the gap question 27. The library-chain dimension owns no web source; it
cites repository files by line, and this log does the same. The check files on disk record 315 strict passes, 9
passes as extraction artifacts and 20 failures (`recheck2-out.json`). Five of the 315 are unitQ worksheet lines
[34]. The worksheet had first been stored as raw Word XML, so the main loop downloaded the `.docx`, extracted its
paragraphs and stored the text. Before that step the counts were 310 strict and 25 failed, as the main loop
reports.

**A fresh fetch was tried for 79 quotations, from the 17 quoted sources this build's own run first stored.** 56
passed. Fourteen from the usability.gov template [18] drew HTTP 429 from the Wayback Machine, so that source rests
on its stored copy alone. Nine failed. Five are unitQ lines, whose live form is a binary file. One is from Nikki Anderson's
roadmap article [26]. Three had already failed against the stored copy. The other 265 quotations, from 19
sources, were checked against the stored copies only in this build.

**The failures were repaired in three steps, and then the generator re-tested everything.**

- **Splitting.** Most failures joined a heading to its paragraph or dropped list separators. `gen_sources.py`
  split 18 such quotations. Eight survived as 30 passing parts, and 10 were dropped whole. Two more strict
  failures passed the generator's relaxed test and stand: Torres's product-trio sentence [23] and Koji's
  sign-off sentence [33].
- **Re-quoting.** The main loop re-quoted 20 passages verbatim from the stored text. They are 13 from the
  usability.gov template [18], 2 from GOV.UK's consent page [21], 3 from Defra [22] and 2 from DHS [6]. It added
  3 more it found in the stored text: NN/g's step heading "Write a Test Plan" [12], a Koji line [33] and a unitQ
  line [34].
- **Carrying.** `carry_spec_quotes.py` carried 104 quotations from the two admission sweeps, for sources already
  in this log. It carried a heading only where the spec quotes it. The sweeps had checked those lines against raw
  page text on 2026-10-23 (`tier2-specs.md:7015-7020`); this build re-tested them against the stored copies only.

The arithmetic is 344 returned plus 127 extra lines, which makes 471. Taking away the 18 that failed whole and
adding the 30 surviving parts gives 483. The generator merged 10 duplicates, which leaves 473. `sources-report.txt`
reports `split 18, dropped 10`. The split figure counts every quotation that failed as a whole span, so it includes
the 10 drops. Every line in sources.md passed a check against the stored raw body.

---

## What the checks caught, and what was not read

**This log carries every external span the spec quotes for the plan.** The spec's tables, sizes reasoning,
exclusions and boundaries quote eleven external sources. They are 18F, digital.gov, GOV.UK, NSW, NN/g, Dovetail,
User Interviews, Maze, dscout, MeasuringU and Gilad. Each of those spans is a Quotable line here, or part of one. This
log checked that by matching every quoted span in the spec's section against the Quotable lines. The spans that did
not match are repository text, catalog labels, or the report's own sources: Dovetail's executive-summary line,
UserTesting's three report forms, DHS's short-report line and NIST's final-product phrase. Those belong to the
report's log.

**The spec's count for digital.gov does not match this log's stored copy.** The spec counts twelve sections
(`:7024`, `:7109-7110`). The stored copy names eleven, from "Title of research plan" to "Important links" [3]. Its
sample timeline adds rows for analysis and report delivery, which may explain the twelfth, but those rows are not
Quotable lines. Nothing in the section design turns on the number. Confidence: medium, because the stored copy is a
text extraction that drops any list numbering. The spec's eleven headings for 18F's template hold if the title
counts. The stored copy has a title, ten second-level headings and a per-task block [1].

**Two spans the contract and spec quote carry a qualifier they do not quote.** Both qualifiers are Quotable lines.
Each must travel with the span it qualifies.

- **Gilad's test-and-experiment line.** The contract and spec quote "Per this definition an A/B test is an
  experiment, but a usability test is not." [19] (`research-docs.md:35-36`, `tier2-specs.md:7183-7184`). Gilad's
  next sentences read: "I realize that this is not the common definition used in the industry - in many cases the
  words test and experiment are used interchangeably. I chose this definition because it’s closer to how scientists
  think of experiments." [19]. The experiment boundary therefore rests on Gilad's own stricter definition, by his
  own account. The contract already states its version as the library's POSITION (`research-docs.md:37-38`).
  Confidence: high.
- **NN/g's one-study line.** The contract quotes "Typically, a research plan is constructed for each study." [7]
  for its axis call (`research-docs.md:90-91`). The same article allows that "sometimes, a research plan could
  include numerous studies or phases of research" [7], and its example pairs "interviews and a diary study" [7].
  The one-study membership test (`research-docs.md:12-15`) is therefore the library's POSITION against a minority
  practice the source names. Confidence: high.

**What the ten drops lost.** The re-quotes recovered most of each dropped passage. These clauses were not
recovered and may only be paraphrased, with the source number:

- **The usability.gov template [18]:** four clauses. One says the tasks are the commonest and relatively complex
  functions. One makes reporting a wrong data value a critical error. One names time on task. One describes
  severity as a combination of impact and frequency.
- **DHS [6]:** the sentence placing the moderator near the participant, to ask follow-up questions but not to
  teach or help.
- **GOV.UK's consent page [21]:** the lead-in telling researchers what participants must be told. Its two items
  survive.
- **Defra [22]:** the lead-in naming Defra's user researchers. Its two clauses survive.
- **Calgary [16]:** the labels for its performance and preference measures, and its preference item on how well
  the product matched expectations. Its other measure items survive.

**Spans the dimension files present that are not Quotable lines.** Drafters who read the dimension files will meet
these and must not quote them. This list came from matching every quoted span in the six files against the
Quotable lines.

- `dim1.md` quotes 18F's per-task block and sample timeline, and digital.gov's role table and timeline rows. It
  quotes GOV.UK's step on agreeing which assumptions to test, and its participant-host role. It quotes DHS's
  helper role and optional observers, and the name of NSW's unopened example file.
- `dim3.md` quotes dscout's question prompts, its three-to-five rule for interview questions, and its Part 7
  sentence. It quotes User Interviews' sample research question and its kickoff sentence. It quotes three Maze
  lines: objectives guiding questions, stakeholders as active participants, and stakeholders signing off product
  changes. It quotes Dovetail's heading on three things to settle before the first session. Its attribution of
  Maze's alignment line [10] to Paige Bennett is its own reading; the Quotable line does not name her.
- `dim4.md` quotes NN/g's lead-in naming tasks as activities, and NN/g's closing sentence on preparation. It quotes
  Calgary's phrase on frequency and importance. From the usability.gov template it quotes the severity
  thresholds, the rule that help from another role scores a critical error, and the setup sentences.
- `dim5.md` quotes the GOV.UK consent page's items on who runs the research and what data is collected. It also
  quotes Anderson's intake form and roadmap fields.
- `dim6.md`: a figure on undocumented research decisions that Koji attributes to NN/g. The dimension could not
  find it on NN/g's site and excluded it. It may not be cited.

**Where the dimensions contradict one another.**

- **The gap dimension's pilot claim is wrong as stated.** It found no common section that names a pilot. GOV.UK's
  round plan has "Run a practice session" [4], and DHS has "Holding a Practice Test" [6]. MeasuringU's sample
  timeline schedules "Conduct Pilot Test & Report on Recommended Changes 8/23 - 8/25" [13]. NN/g [12], [31], Maze
  [14] and Michigan Tech [17] name a pilot too. Other dimensions owned those sources.
- **The gap dimension's analysis null result holds only narrowly.** No source asks a plan to name a coding method.
  But User Interviews says "Good research analysis begins at the planning stage, before research actually begins."
  [9]. Maze's usability plan asks "Analyzing results: how are you going to derive insights from your research?"
  [14]. GOV.UK has "Plan time for analysis" [4].
- **The usability dimension found no sentence pairing a research plan with a test plan.** NN/g's "(When planning a
  usability test, the research plan is often referred to as a test plan.)" [7] is exactly that. Another dimension
  owned the article, and the line came in from the admission sweep.
- **The vendors dimension found no approval authority for the plan.** Defra names one: "Submit the research plan
  to your lead user researcher (if your delivery group has one) for review or approval." [22]. The usability.gov
  template says of the tasks: "acceptance is to be documented prior to usability test." [18].
- **The practice dimension found no source on paying participants.** Maze has the step "5.1. Determine how you'll
  pay them" [10], and CleverX counts an "incentive per session" [32].
- **Tiers.** `dim4.md` tags the three course pages as practitioner and the usability.gov template as primary. This
  log follows the tiers `order.json` sets: academic for [15], [16] and [17], and practitioner for [18].
- **A title.** `dim3.md` notes that the name the task gave NN/g's article [7] is a subheading, not its title.
  Cite the title as the source entry gives it.

**What was assigned and not read, or not usable:**

- **NSW's Word template and its paired example** [5]. The stored text stripped the download link, so only the
  guide page around the template was read. NSW corroborates timing and purpose, not sections.
- **DHS's per-approach downloads** [6]: the moderator's guide, note-taking guide, consent form, demographic
  questionnaire and report template.
- **18F's linked consent form**, and whether the 18F repository [1] carries an archive banner on GitHub. The raw
  file shows none; the UX Guide shows "Archived as of January 20, 2025" [2].
- **Washington's template itself** [15]. Its PDF and its zip of materials were not reached.
- **Defra's research plan template and scoping workshop template** [22], named on the page and not opened.
- **GOV.UK's page on a service-level research plan**, which the round page [4] presupposes. Not fetched.
- **Chapter 5 of the Handbook of Usability Testing**, which MeasuringU recommends [13]. Not read.
- **GSA's Office of Evaluation Sciences analysis-plan template**, which returned HTTP 404.
- **Koji's pilot-study guide**, seen only in search results.
- **Any prevalence figure** for studies run by product managers or designers. None rests on a read body.
- **A filled sample plan, end to end.** None was read. The nearest are digital.gov's role and timeline fragments
  [3] and the usability.gov boilerplate [18].

---

## Findings

### 1. What a user research plan is, and its two published lengths

**The definition is settled across sources.** NN/g: "A research plan is a document that outlines the goals,
methods, and logistical details of a research study." [7]. User Interviews: "A user research plan is a document (or
less commonly, a slide deck or internal wiki page) that outlines the goals, objectives, and logistical
considerations of a research project for your internal stakeholders and team." [9]. 18F supplies the catalog's
alias: "A research plan (sometimes also called a research protocol), describes the design of your research." [2].
Confidence: high.

**It is written before the study, and usually for one study.** NSW: "When: Before you’ve started any research"
[5]. NN/g: "All UX-research studies should start with a plan." [7], and "Typically, a research plan is constructed
for each study." [7]. 18F: "You may need multiple research plans to account for the variety of ways people may
experience or navigate your design." [2]. NN/g's qualifier allows one plan to cover "numerous studies or phases of
research" [7], as the checks above record.

**Its job is agreement before sessions are booked.** NN/g: "Share your research plan with relevant stakeholders to
get buy-in." [7]. NSW: "It lays out the path ahead, identifies key activities and gaps in your thinking, and aligns
teams and stakeholder on the intended outcomes of the research." [5]. dscout says plans stop a team "from switching
the goal of the research in the middle by mistake." [11]. Dovetail: "A research plan turns a vague request into a
study you can actually run-and defend." [8].

**Two lengths are published, but never as two forms of one plan.** The short form has named minimums. User
Interviews: "At a minimum, your research plan should include:" [9], six items from "What: Your research question(s)
and goals" to "Next steps" [9]. NN/g says "all plans should cover the following:" [7] and lists four. Dovetail:
"One to two pages." [8]. The long form is government's: 18F's template with ten headings [1], 18F's guide with
nine sections [2] and digital.gov's eleven [3]. NN/g softens its own minimum: "Since each research study is a
little different, your research plans can differ in structure, content, and format from one study to the next."
[7].

**The spec's sentence that no source names a short and a long form of one plan holds** (`:6992-6993`,
`:7071-7072`). Three lines come closest without contradicting it. User Interviews: "It still needs a plan, but it
can be a brief one." [9]. That is one short plan, not a pair. MeasuringU calls usability.gov's template
comprehensive, "(which you'll need to trim down to suit your needs)" [13]. DHS scales the test, not the plan, from
"Testing in the Office: Quick Usability Feedback from Colleagues" to "Testing in the Conference Room: Thorough,
Structured Testing with Real Users" [6]. The lean and full pair stays the library's construction from two published
lengths. Confidence: medium-high, as the spec rated it.

**Against length.** MeasuringU: "Test plans, like many documents, can take on a life of their own and become
bloated and unnecessarily complex." [13]. NN/g's test plan "doesn't need to be lengthy" [12]. Dovetail: "A plan is
a working agreement, not a thesis-if stakeholders can't read it in five minutes, they won't." [8].

### 2. Sections, source by source

**Ten sources give a section list.** Two are a fill-in template and a worksheet: 18F's [1] and unitQ's [34]. The
rest are guides whose lists act as headings. The usability-only lists, usability.gov's template [18] among them,
are in Finding 4.

| Source | Sections, steps or headings | Form |
|---|---|---|
| 18F template [1] | "Introduction", "Assumptions", "Target audiences", "Research goals", "What methods will we use?", "Recruitment needs", "Logistics checklist", "Day of testing protocol", "What will we do when?", "Opening script (EDIT BASED ON PROJECT)" | Long; a fill-in template |
| 18F guide [2] | "Background", "Goals", "Research questions", "Methods", "Team participation", "Timeline", "Participants and recruiting", "Ethics considerations", "Outputs and outcomes" | Long; archived |
| digital.gov [3] | "Title of research plan", "Authors and stakeholders", "Context", "Past research", "Research goals and questions", "Research methods", "Roles and responsibilities", "Timeline", "Participants and recruiting", "Issues for awareness", "Important links" | Long |
| GOV.UK round [4] | "Set your research objectives", "Find participants", "Plan the session times", "Arrange recording and note-taking", "Prepare the prototype or beta service", "Run a practice session", "Invite people to watch the sessions", "Get the team to help out", "Plan time for analysis" | Steps for one round, under a standing service plan |
| NN/g [7] | "Purpose and goals of the research study", "Participants", "Method and procedure", "Relevant documents such as consent form, screener, study protocol" | A stated minimum |
| Dovetail [8] | "background and problem statement, objectives, research questions, method, participants and recruitment criteria, timeline and milestones, and a share-out plan" | Seven; "One to two pages." |
| User Interviews [9] | "What: Your research question(s) and goals", "Why: Business goals", "How: Methodology", "Who: Participants", "When and where: Research schedule and logistics", "Next steps" | A stated minimum of six |
| Maze [10] | "1. Define the problem statement" through "8. Decide how you'll present your findings", with "5.1. Determine how you'll pay them" | Eight steps |
| dscout [11] | "Part 1: Background" through "Part 7: Resources/Links to Documentation", with "Part 5: Interview Guide" | Seven parts |
| unitQ [34] | "What decision will this inform?", "Hypothesis", "Success criteria", "Risks", and a synthesis step | A one-study worksheet |

**What recurs.** These counts are this log's, across the ten lists.

- **Goals or objectives**, in nine. unitQ's quoted lines name a decision and a hypothesis instead.
- **Participants and recruiting**, in nine; unitQ's quoted lines name none.
- **Method**, in eight; GOV.UK's round steps and unitQ's quoted lines name none.
- **A timeline or schedule**, in eight; NN/g's minimum and unitQ's worksheet name none.
- **What happens to the findings**, in six: 18F's guide, Dovetail, User Interviews, Maze, dscout's timeline line
  "and when a report could be expected" [11], and unitQ's synthesis step.
- **Ethics or consent**, in five. Four are government lists: 18F's template and guide, digital.gov, and GOV.UK's
  consent bullet [4]. The fifth is NN/g's consent form among relevant documents [7].
- **Earlier knowledge or assumptions**, in four: 18F's template, 18F's guide inside Background, digital.gov and
  unitQ's hypothesis. User Interviews has it as an authoring step, "3. Gather available data and existing
  insights" [9], not in its minimum.
- **Roles**, in three, all long-form: 18F's guide, digital.gov and GOV.UK.
- **Related documents or links**, in three: digital.gov, NN/g and dscout. Dovetail adds "Link out to supporting
  material like discussion guides and screeners rather than embedding them." [8].
- **The session script as its own section**, in three: 18F's template, Maze's step 6 and dscout's Part 5. Two
  more put it inside the plan's text (Finding 3).
- **A problem statement inside the plan**, in two: Dovetail and Maze. See Finding 3.

**The pattern supports the spec's split.** Short and long lists share goals, questions, method, participants and
timing. The long lists add earlier knowledge, roles, ethics and links. That is the lean and full split the
maintainer ruled. Two exceptions run the other way: NN/g's minimum and dscout's seven both carry links (Finding 10).
Confidence: medium-high.

### 3. The boundaries the sources draw around the plan

**The request, and the word brief, which has three senses.** Dovetail: "A brief is the request-what a stakeholder
wants to learn and why it matters to them. A plan is the response-how you'll actually study it, with method,
participants, and timeline." [8]. Maze uses the word for the session guide: "The next component of a research plan
is to create a brief or guide for your research sessions." [10]. Anderson uses it for the study's whole document:
"A link to the intake document or research brief, which has all the relevant information for the study, including
script, deliverables, and a report." [26]. Koji uses it as an analogy: "Think of a research plan as a project brief
for research." [33]. **The guide must say which sense it means, and research brief cannot be an alias.** The spec's
exclusion of the request (`:7122-7123`) holds in Dovetail's sense. Confidence: high that the word is contested.

**The strategy and the standing service plan.** Maze: "While your UX research plan should be based on strategy,
it's not the same thing." [10]. GOV.UK: "You can only plan specific rounds of research when you’ve created a
research plan for your service." [4]. GOV.UK's round plan is this bundle's analogue; its service plan is the
standing document the contract excludes (`research-docs.md:53-57`). Anderson's research roadmap [26] is a second
standing document of the same kind. The spec's exclusion holds (`:7119-7121`). Confidence: high.

**The session script: most sources put it in the plan.** Inside the plan:

- dscout's "Part 5: Interview Guide" [11] and 18F's "Opening script (EDIT BASED ON PROJECT)" [1].
- Maze's session brief, quoted above [10].
- User Interviews: "In the methodology section of your research plan, you'll also need to include the details of
  your study, like a moderator guide for interviews, or the wireframe you're using for a usability testing study."
  [9].
- Michigan Tech, for the usability case: "The scenario descriptions, tasks, and pre- and post-questionnaires
  should be fully fleshed out in sentences appropriate for reading to the participant." [17].

Linked from the plan: Dovetail's instruction to link out [8], and NN/g's relevant documents, which name "consent
forms, recruitment documentation, and facilitator guides" [7]. NN/g does both, because its method section also
lists "Tasks, prompts, or interview questions that will be provided to participants" [7]. **Five sources embed, two
link, and NN/g does both.** The maintainer ruled that the plan links the guide (ruling 5, `:7386`). The spec's
reason is that catalog entry 25, the interview guide, is a separate candidate (`:7114-7118`). That ruling stands.
The companion must label the exclusion the library's POSITION. Confidence: high on the count across these sources.

**Where the tasks end and the script begins.** Michigan Tech puts task wording in the plan [17], and the spec keeps
tasks in the plan's usability block. On this log's reading, the task scenarios, their success criteria and the
measures stay in the plan. The moderator's opening, the consent wording and the follow-up probes go to the linked
guide. The guide must draw that line, because no source draws it. Confidence: medium.

**The project brief.** NSW places the plan "After you have been given an initial project brief, but before you
commence any official research activities." [5]. `project-brief`'s own guide names no research document
(`templates/project-brief/project-brief_guide.md:18-25`, read in `dim2.md`). The spec's boundary (`:7194-7196`)
therefore rests on NSW alone. Koji's analogy [33] blurs it.

**The QA test plan: the shared words are the sources' own.** NN/g tells teams to "document your approach in a test
plan and share it" [12]. usability.gov's template opens "This document describes a test plan for conducting a
usability test" [18]. MeasuringU [13], Michigan Tech [17] and Calgary [16] say test plan throughout.
`test-plan`'s guide names no research or usability document (`templates/test-plan/test-plan_guide.md:17-30`, read
in `dim2.md`). The guide's first line must separate them, as the spec's risk 8 requires (`:7345-7346`).
Confidence: high.

**The experiment.** Gilad: "Experiments are tests that include a control element to guard against false results
caused by random chance." [19]. His qualifier travels with his line (see the checks above).
`experiment-design-doc`'s guide already names a user interview as a cheaper method for the easy cases
(`templates/experiment-design-doc/experiment-design-doc_guide.md:30-31`, read in `dim2.md`).

**A problem statement inside the plan is the study's problem, not the product's.** Dovetail opens with
"background and problem statement" [8], and Maze with "1. Define the problem statement" [10]. In this library,
`problem-statement` frames a product problem for a decision. The plan's first section says why research is needed
and does not frame the product problem itself. That is the library's reading. It matters for the example, which
must not borrow a sibling problem statement (see the example note).

### 4. The usability block

**The identity is still stated in words by one publisher.** NN/g: "(When planning a usability test, the research
plan is often referred to as a test plan.)" [7]. No second source says it in a sentence. MeasuringU writes about
the usability test plan without calling it a research plan, and points to "The folks at Usability.gov have a
comprehensive template" [13]. **The nesting has more support in structure than in words.** Maze's usability testing plan lists "Aims and
goals", "Test participants and methodologies", "Analyzing results" and "Outcomes and next steps" [14]. That is
the general plan's shape with the method fixed. NN/g's usability list adds "Tasks" and "Metrics, questionnaires" to
"Study goals", "Participant profiles" and "Logistics: time, dates, location, and format of study" [12]. Three
general plans name usability testing as one method among others. digital.gov: "Note the method or methods of
research you will be using, such as contextual inquiry or usability testing." [3]. User Interviews names "the
wireframe you're using for a usability testing study" [9]. Maze's research plan chapter says "you can run
usability tests to get actionable feedback" [10]. Confidence: medium-high that the usability test plan nests in the
research plan; medium that the alias identity is stated, since it rests on one publisher.

**Tasks.** NN/g: tasks "are usually written in the form of scenarios and should match the goals of the study" [12],
and "Strong tasks are concrete and free from clues that might prime people's behavior." [12]. NN/g [12] and Maze
[14] both split tasks into exploratory and specific. MeasuringU: "For each task scenario you'll want to define at a
minimum what information you'll give the user (the scenario) and the starting URL or screen." [13]. usability.gov:
"The tasks are identical for all participants of a given user role in the study." [18]. Calgary: "The tasks in
this list should consist of tasks that will ordinarily be performed by the eventual user." [16].

**A success criterion for each task.** MeasuringU: "Task Completion: Determine an objective success criteria for
each task." [13]. usability.gov sets a target per task: "A completion rate of [100%/enter completion rate] is the
goal for each task in this usability test." [18], and "An error-free rate of [80%/enter error-free rate] is the
goal for each task in this usability test." [18]. Maze: "It's essential you consider what success looks like
before you begin usability studies." [14]. Calgary: "A detailed description should be made as to which actions or
behaviours are required for each successful task." [16]. Confidence: high.

**Measures.** NN/g: "Common usability metrics are: time on task, satisfaction ratings, success rate, and error
rate." [12]. usability.gov defines both rates: "Completion rate is the percentage of test participants who
successfully complete the task without critical errors." [18], and "Error-free rate is the percentage of test
participants who complete the task without any errors (critical or non-critical errors)." [18]. Maze calls the
error-free rate "a north star metric" [14]. MeasuringU asks "a single ease question" after each task and uses
"SUS, SUPR-Q or NPS" for the session [13]. It warns that "Users tend to be overconfident when completing tasks"
[13].

**Questions before and after.** usability.gov names three points. "Participants will complete a pretest
demographic and background information questionnaire." [18]. Then: "After each task, the participant will complete
the post-task questionnaire and elaborate on the task session with the facilitator. After all task scenarios are
attempted, the participant will complete the post-test satisfaction questionnaire." [18]. NN/g asks the planner to
"decide on when you will give the questionnaires: after each task, at the end of the session, or both." [12].
MeasuringU's plan carries "Pre-Test Questions" and "Post-Test Questions" [13].

**The pilot.** Michigan Tech: "The usability test plan is produced and the protocols are pilot-tested before the
actual tests are conducted." [17]. NN/g's checklist [12] and video [31], Maze [14], MeasuringU [13], GOV.UK [4]
and DHS [6] all name one. Maze adds: "Make sure your pilot participant has had no part in the usability testing
process so far, otherwise you risk enacting false-consensus bias" [14]. Confidence: high.

**Participant numbers are contested.** For qualitative tests: NN/g, "For traditional qualitative studies, we
generally recommend 5 participants for the best return on investment." [12]; Maze, "the marginal benefit of each
research participant decreases dramatically past four or five participants" [14]; DHS, at least four per type of
user [6]; Dovetail, "five to eight participants per segment is enough for most qualitative studies" [8]. For
quantitative tests: NN/g, "You may need at least 20-30 participants in each target user group" [12]; Maze, "This
is the time that having 30+ participants is ideal." [14]. MeasuringU's own mixed practice runs "(usually 5-10
moderated) and between 50 and 300 unmoderated users" [13]. The guide may quote the ranges with their sources; it
must not set one number.

**Formative and summative.** Only Calgary's 1997 course page uses the words [16]. "There must be a decision made on
the goal of the usability test." [16], and "it is extremely difficult to shift gears from a design iteration
formative test to a more controlled summative test." [16]. The usability.gov template's goals include
"establishing a baseline of user performance, establishing and validating user performance measures, and
identifying potential design concerns" [18]. On this log's reading, the first two goals are summative. A test that
compares variants under a decision rule crosses the contract's experiment line (`research-docs.md:37-38`).
Confidence: medium that the guide needs the distinction; low that the 1997 words are current vocabulary.

### 5. Practice: who writes it, who agrees it, and whether teams write one at all

**Who writes it.** dscout's researcher writes it, then shares the draft "with the product team to ensure you're
interpreting their aims correctly." [11]. Defra makes plans "mandatory for all DDTS user researchers" [22]. NSW
writes it "With: Your research team" [5]. digital.gov's authors are the "people designing your research" [3].
Torres gives discovery to the product trio: "The product trio should interview customers together." [23].
**No Quotable line names a product manager as a plan's author.** The example's author, a PM, is the library's
choice (`:7258-7260`). The companion should say either role writes it, as the spec recommends (`:7324-7325`).
Confidence: medium.

**Who agrees it.** Defra's sequence runs from a scoping workshop to "Capture the agreed scope in the research plan
template and make sure the approach represents all users." [22]. Then comes review or approval by the lead user
researcher [22], and then "Share the approved plan with your team so everyone is aligned." [22]. Koji: "Get
sign-off on the research questions from the stakeholders who will act on findings." [33]. Dovetail: "One or two
decisions this research will inform-written down, agreed with stakeholders" [8]. NSW: "Step 2: Present back to
your wider team and stakeholders so you can get buy-in for your research and your team’s next steps." [5]. Maze
has "3. Get stakeholders buy-in" [10]. Confidence: high that agreement before fieldwork is common practice;
medium that a named approver belongs in the document.

**Changing the plan once the study runs.** NN/g: "Update the plan after the research study is over." [7], and "In
moderated studies, it's common to make adjustments during the study to get better data." [7]. NSW: "Regularly
review and update your research plan as the project progresses." [5]. Maze: "Seeing the UX research plan as a
living document makes it much easier to edit based on team comments." [10]. dscout: "It's not always used
extensively after the project has started." [11]. The contract's finish line, finished when the findings are
reported, is the library's POSITION (`research-docs.md:14-17`). NN/g's update fits inside it if it is made before
the report. The report's spec records the same change from the other side, as a deviation line (`:7153`). **The
guide must say which document records a mid-study change.** Confidence: medium.

**Whether to write one at all is contested.** Boag: "it is better to conduct user research only when there is a
specific question that needs answering" [25]. He hedges: "The results you get back will be far from perfect and
could possibly lead to false conclusions." [25]. Torres: "While there's nothing inherently wrong with project-based
research, it's not sufficient for teams who continuously ship value to customers." [23]. Her teams meet customers
weekly: "Good product discovery teams engage with customers at least weekly" [23]. Against them stand Defra's
mandate [22] and User Interviews' "It still needs a plan, but it can be a brief one." [9]. The dispute is over how
light, not whether. A team on a weekly interview cadence may write no plan per study, which is a when-not-to-use
row. Confidence: medium.

**Generative and evaluative.** Torres: "Generative research helps teams discover opportunities through
story-based customer interviews. Evaluative research helps teams test which solutions will best address those
opportunities." [24]. Anderson shows the cost of not tracking the difference: "This information was a massive
signal that we were over-indexing evaluative research and not leaving enough time for generative research." [26].

**Studies of shipped products are ordinary.** GOV.UK's Design System: "Your service might be in the alpha or beta
phases, or you might be iterating the service after going live." [20]. DHS says usability testing is "most
useful" [6], first "Before you start redesigning something" [6]. The contract already cites the Design System
line for the cost it states (`research-docs.md:103-109`). DHS adds a second source for that cost; it does not
change the axis. See Finding 8.

### 6. The software-audience check (ADR 0080)

ADR 0080 (admission gains a software-audience check) asks for one named source. That source must show a software
product, UX or technology team writing or using the document
(`docs/internal/decisions/0080-admission-gains-a-software-audience-check.md:125-126`). **The type passes by name,
on several teams' own practice.** Confidence: high.

- **18F** publishes its own fill-in research plan template [1], and its guide describes what "Typical 18F research
  plans include:" [2]. The guide speaks for "18F’s UX team" [2].
- **Defra's digital service** mandates the plan for its user researchers [22].
- **MeasuringU** describes its own practice: "While each plan will vary based on the organization and test
  situation, here are the sections we use most often." [13].
- **dscout's practitioner** writes the plan for "the product team" [11], and her sample timeline carries "Research
  plan creation and review: Wednesday, August 7th" [11].
- **NN/g**, a UX consultancy, writes for UX teams [7], [12].
- **Vendors writing for product and UX teams**: Dovetail [8], User Interviews [9], Maze [10], Koji [33] and unitQ,
  which calls its worksheet a way to "treat it like a lightweight PRD for your study" [34]. Maze's chapter title
  names research managers at Affirm and Workday, but no Quotable line attributes words to either.

The name-versus-job question in ADR 0080 (`0080-...:134-145`) does not arise, because the name matches.

### 7. Lineage: what the plan borrows from government digital services

Contract section 3.6 (citations, with the family's lineage trap) requires a member that borrows a structure from a
government form to say so (`research-docs.md:132-136`). **This plan borrows section structure from US and UK
government digital services.**

- **18F** (US): the template [1] and the UX Guide [2]. The guide is "Archived as of January 20, 2025" [2].
- **digital.gov** (US, GSA): its page on how to write a research plan [3].
- **GOV.UK** (UK): the round-planning page [4], "Published: 16 March 2016" and "Last updated: 23 May 2016" [4], and
  the consent page [21].
- **The retired usability.gov template** (US), read through a Wayback Machine snapshot of 2024-02-21, for the
  usability block's measures and questionnaires [18].
- **DHS's usability kit** (US), for roles and participant counts [6].
- **NSW** (Australia) corroborates timing only [5], and **Defra** (UK) the review step [22].

**None is a regulatory form.** Each is guidance or a fill-in template that a digital service team published for
its own and others' use. Defra's mandate binds Defra's own researchers, not product teams in general. No plan
source in this log cites ISO/IEC 25062; that lineage is the report's (`tier2-specs.md:7028-7031`). The companion's
Origins section should name the government lineage and date the two retired sources, 18F's guide and
usability.gov. Confidence: high on the list. This log did not trace whether the usability.gov template derives
from a standard.

### 8. The shipped-product clause

The friction study studies a dashboard customers already use (`tier2-specs.md:7267-7269`). Contract section 2
requires a member that serves such a study to declare `discover` anyway, with its companion saying why
(`research-docs.md:107`). What this research gives the companion:

- **The sources treat studies of live products as ordinary research work** [20], [6]. That is the cost the
  contract names, now with DHS's line [6] behind it as well.
- **The friction study is generative in Torres's sense.** It asks where analysts lose time, which is how
  "Generative research helps teams discover what matters to customers." [24]. It tests no solution, which is what
  evaluative research does [24]. On this log's reading, that is the companion's best reason: the study looks for
  an opportunity in a shipped product before any concept exists. The design brief, dated after the study, picks
  the concept. Confidence: medium, because the reason remains the library's POSITION, as the contract labels it
  (`research-docs.md:107-109`).
- **What the companion must not say:** that any source calls a study of a shipped product discovery work. None
  does.

### 9. The gap question: candidates, routed under decision procedure 12

The gap dimension returns **candidates, never obligations**. Each is routed under decision procedure 12 (a
property or section proposed for a template) (`docs/internal/decision-procedures.md:207-254`). E1 means a named
source publishes documents of this type carrying the element. E2 means the library argues it in its own voice with
a falsifier. E3 names its home, and E4 fits it to lean or to full. A quality property stops at step 1 and becomes a
guide rubric row. **This log admits no element and proposes no section.**

**Weigh the gap dimension's sources honestly.** Six of its ten are vendors or Substack newsletters: Askwhy [27],
Coleman [29], CleverX [32], Koji [33], unitQ [34] and Great Question [35]. unitQ's worksheet is the richest single
source, and it is a company's kit, tiered practitioner here. Where a candidate also has a government or NN/g
source, that source carries it.

1. **The decision the study informs, and what would change it. Supported; already homed.** E1: Dovetail's
   "Background explains why the study exists and what decision it informs." [8]; Coleman's "Start with the
   decision, not the question." and "What would change their choice." [29]; Koji's "Specifying the downstream
   decision in your plan creates accountability" [33]; unitQ's "What decision will this inform?" [34]. **Route:**
   an ASK in Why This Study, and the Decision It Informs, on what result would change the decision. unitQ's "If
   nothing changes based on the result, reconsider running it." [34] becomes a TRAP line. Plus a rubric row.
2. **A hypothesis.** E1: Askwhy's "2. Hypothesis" [27]; unitQ's worksheet [34]; NN/g's "Usually, research plans
   will have a section that lists the relevant research questions, research goals, or hypotheses." [7]; 18F's
   "Assumptions" heading [1]. **Route:** an ASK in Goals and Research Questions, as an alternative to a question.
   Assumptions stay in What We Already Know (full), as the spec homes them. A TRAP names a hypothesis worded so the
   study can only confirm it. A hypothesis plus allocation and a decision rule is an experiment by the contract's
   POSITION.
3. **Success criteria set before fieldwork. Homed for usability tests.** E1: [13], [18], [14], in Tasks and
   Measures. For other methods: unitQ's "Success criteria Define these before you start so you don’t rationalize
   the result afterward." [34], and Koji's "what constitutes a good answer" [33]. **Route:** an ASK in Goals and
   Research Questions on what answer would be enough. A threshold field for an interview study fails E1 outside one
   company's kit, and it edges toward the experiment line.
4. **Risks, limits and bias.** E1: unitQ's risk table [34]; digital.gov asks for "bias" concerns and "how the team
   will mitigate them" [3]; Coleman: "Define what you cannot answer." [29]. E3: the full Consent, Privacy and
   Ethics section already carries digital.gov's line. **Route:** an ASK in Method on what this study cannot answer.
   No table.
5. **A pilot session. Strongly supported.** E1: MeasuringU's dated pilot line [13]; GOV.UK [4]; Michigan Tech
   [17]; NN/g [12], [31]; Maze [14]; DHS [6]. E3: Schedule and Logistics. E4: lean. **Route:** an ASK in Schedule
   and Logistics, and in Tasks and Measures for a usability test. A GOOD line can show a pilot date. No section.
6. **A recruiting fallback.** E1: NN/g's "intentional overrecruiting" [30], and unitQ's "over-recruit for
   no-shows" [34]. NN/g gives the reason: "each lost participant represents a fairly substantial proportion of your
   potential insights" [30]. **Route:** an ASK in Participants and Recruiting.
7. **Access needs and inclusion. Access needs supported; demographic mix contested.** E1: GOV.UK's "how you’ll
   cater for any access needs" [4]; AnswerLab's "It’s very important to ask if participants need any accommodations
   to participate in a study, whether conducted in-person or remotely." [28]; digital.gov's accessibility concern
   [3]. On the mix, AnswerLab says "We recommend including a mix of participants with a range of genders,
   ethnicities, ages, income, education, and more in every study you conduct." [28]. DHS says "Don’t worry about
   demographics like age, education, or income" [6]. **Route:** access needs as an ASK in Participants and
   Recruiting, in lean. The mix becomes guidance that states both views, not a field.
8. **Paying participants and costing the study. Payment homed; a budget fails E3.** E1 for payment: Maze [10],
   CleverX's "incentive per session" [32], and GOV.UK's "how you’ll find them within your budget" [4]. The spec's
   row already carries how participants are thanked or paid. A full cost breakdown fails E3. Maze puts budget in the
   strategy: "Your UX strategy is a high-level document that contains goals, budget, vision, and expectations."
   [10]. CleverX's reserve is a programme's: "Research programs always encounter urgent or reactive studies that
   were not planned." [32]. CleverX sells recruiting, so its cost framing is a vendor's. **Route:** incentive per
   session as an ASK in Participants and Recruiting; nothing more.
9. **Data retention and deletion.** E1 inside a plan: 18F's "Destroy this roster at the end of the engagement."
   [2], and its script's "We keep the list of people we interviewed, our notes, and the recording in a secure place
   where only team members can access it." [1]. Outside a plan: Westminster's fixed periods [36], a standing privacy
   statement, and Great Question's "comply with your company’s data retention policies" [35], a product page. E3:
   the full Consent, Privacy and Ethics section; the periods themselves belong to the organisation's policy.
   **Route:** an ASK there on how long recordings and notes are kept and who deletes them, pointing to the policy.
10. **Analysis judged against what the plan set out.** E1: unitQ's synthesis step [34]; User Interviews [9]; Maze
    [14]; GOV.UK [4]. **Route:** an ASK in What Happens to the Findings, on how the data will be analysed against
    the questions. Time for analysis goes in Schedule and Logistics. unitQ's "build, iterate, keep exploring, or drop"
    [34] is a recommendation, which is the report's job. Logging the decision is a decision document's job
    (`research-docs.md:47-49`). Both stay out of the plan.

Candidates the other dimensions surfaced, routed the same way:

11. **A named approver. Supported.** E1: Defra's review or approval [22]; usability.gov's documented acceptance of
    the tasks [18]; Koji's sign-off [33]; Dovetail's "the day it's approved" [8]. E3: the template's frontmatter, if
    it carries an approver field as the design brief's does (`templates/design-brief/design-brief_example.md:5`).
    **Route:** frontmatter or an ASK in Why This Study, plus a rubric row that the plan was agreed before
    recruiting began. The build chooses the home.
12. **Stakeholders involved versus informed.** E1, thin: Askwhy separates those involved from "those who simply
    need to be informed" [27]. **Route:** an ASK in Roles and Observers (full), or in What Happens to the Findings
    for lean. One newsletter source.
13. **Which kind of study this is: generative or evaluative, formative or summative.** E1 is weak: Calgary's
    decision on the test goal [16], and GOV.UK's Design System asking "whether it was a qualitative or quantitative
    study" when findings are shared [20]. **Route:** an ASK in Method, with Torres's definitions [24] in the
    companion. Not a field.
14. **Consent in the lean plan.** E1: GOV.UK lists "how you’ll collect their informed consent" under finding
    participants [4]; NN/g's minimum names the consent form [7]; GOV.UK's consent page makes consent compulsory
    [21]. **Route:** an ASK in lean Participants and Recruiting on how consent is taken, pointing to the full
    section. This is the route the spec's one-size fallback already names (`:7075-7076`).
15. **A link to the session guide in the lean plan.** E1: [7], [8], [11]. With the script excluded at every size,
    the link matters more in lean, where Related Documents is absent. **Route:** an ASK in lean Method that links
    the session guide and the screener.
16. **The session script itself. Out at any size**, by ruling 5 (Finding 3). **Route:** TRAP rows, under the
    spec's list of what stays out (`:7112-7123`).
17. **A coding or analysis method. Unsupported.** No Quotable line asks a plan to name one; CleverX's tutorial is
    the negative [37]. **Route:** out.

### 10. The eleven proposed sections, against this research

The spec's section table (`docs/internal/tier2-specs.md:7094-7106`) is headed as proposed, for the build's research
to test (`:7092`). The maintainer's rulings of 2026-10-24 close the spec's section (`:6979-6980`), so its sections
and sizes bind. The table below records which sources now support each section and whether confidence moves. **Every movement is
a candidate for the maintainer; none is applied here.**

| Section | Size | Spec | Support in this log | Movement |
|---|---|---|---|---|
| **Why This Study, and the Decision It Informs** | lean | High | [8] "Background explains why the study exists and what decision it informs."; [9] "Why: Business goals"; [11] "Part 1: Background"; [3] "Context", "What led to the study"; [2] "Design research is fundamentally about reducing risk and informing decisions."; the decision: [29], [33], [34]; [5] on drafting the problem first | **Holds at high.** All four of the spec's spans are Quotable lines. The decision half gains three sources. Gap candidates 1 and 11 enter as ASKs |
| **Goals and Research Questions** | lean | High | [7] "Purpose and goals of the research study"; [3] "Research goals and questions"; [9] "What: Your research question(s) and goals"; [8] "Research questions describe what you need to learn, not what you'll ask participants." and "limited to three to five per study"; [2] "Research questions are different from interview questions." and its goal verbs; [16] "These should be not be vague but specific." | **Holds at high.** 18F is a second source for the research-question and interview-question line. 18F's verbs give the GOOD and WEAK lines |
| **What We Already Know** | full | Medium-high | [3] "Past research" and "Provide a summary and links to any available assets from past related research."; [9] "3. Gather available data and existing insights"; [1] "Assumptions"; [2] "Review and summarize any relevant secondary sources"; [25] "Instead, start by collating what the organization already knows about the user and their needs."; [29] "What they already know." | **Up to high on the element.** Full placement holds, because no short minimum carries it [7], [8], [9]. Boag's line argues that a lean plan should still point to what is known; that is an ASK in the first section |
| **Method** | lean | High | [7] "A research plan should list the user-research method(s) employed in the study and how the study will be conducted."; [9] "How: Methodology"; [3] "Note the method or methods of research you will be using, such as contextual inquiry or usability testing."; [10] "4. Choose the right research method"; [12] the format choices; [24] | **Holds at high.** Gap candidates 4, 13 and 15 enter as ASKs |
| **Participants and Recruiting** | lean | High | [7] "Participants"; [9] "Who: Participants"; [8] "Your plan should state who qualifies, who doesn't, and how many sessions you need"; [3] "Participants and recruiting"; [4] "which kinds of participants you need to include", "how you’ll cater for any access needs", "how you’ll find them within your budget"; [10] "5.1. Determine how you'll pay them"; [2] the roster; [6] counts; [30] | **Holds at high.** The clause on thanking or paying participants, unsourced in the spec's row, now rests on [10] and [2]. Gap candidates 6, 7, 8 and 14 enter as ASKs |
| **Tasks and Measures** *(usability tests only)* | both | High on content; medium on placement | Content: [12], [13], [14], [16], [17], [18]. Placement: NN/g's general plan holds "Tasks, prompts, or interview questions that will be provided to participants" inside its method [7]; [12] and [14] give the usability plan its own task and metrics items | **Content holds at high**, with usability.gov's per-task targets and three questionnaire points as the fullest model [18]. **Placement holds at medium**: the conditional section is the library's arrangement |
| **Schedule and Logistics** | lean | High | [9] "When and where: Research schedule and logistics"; [12] "Logistics: time, dates, location, and format of study"; [3] "Timeline"; [4] "Plan the session times" and "Arrange recording and note-taking"; [11] "An approximate timeline of when the research will take place, and when a report could be expected."; [13] the pilot line | **Holds at high.** Two ASKs enter: the pilot (gap candidate 5), and time for analysis, on which the sources disagree (contested item 6) |
| **Roles and Observers** | full | Medium-high | [3] "Roles and responsibilities"; [2] "Team participation" and "Good research is collaborative. People who help accomplish the research are more likely to agree with its outputs."; [4] "Invite people to watch the sessions" and its room roles; [12] "9. Motivate Team Members to Observe Sessions"; [6] "A note taker may support the moderator by logging observations and discussion."; [1] "NAME (Lead moderator)" | **Up to high.** GOV.UK loosens its own roles: "Anyone who understands the aims of the research and is willing to help can do these roles - it does not need to be another researcher or member of the team." [4]. DHS names a note taker even in its quickest test [6]; lean Schedule and Logistics already says how sessions are noted |
| **Consent, Privacy and Ethics** | full | Medium-high | [2] "Ethical considerations"; [1] "Participants will need to sign a consent form (see attached)." and "Research team should ensure that no PII data is captured."; [3] "Issues for awareness"; [21] the whole consent page; [4] the consent bullet; [20] consent before sharing findings; [2] the roster's destruction | **Up to high on the element.** Full placement holds as ruled, with gap candidate 14 as a lean ASK |
| **What Happens to the Findings** | lean | High | [9] "Next steps" and "7. Be ready to share your research findings"; [8] "share-out plan"; [10] "8. Decide how you'll present your findings" and "In your plan, mention how you'll share insights with the product team."; [2] "Outputs and outcomes"; [13] "If possible, try to outline how the report will be structured in the test plan."; [14] "Outcomes and next steps" | **Holds at high**, with two qualifiers to carry. 18F: "Avoid over-specifying your outputs, because you don't know what you’ll find until the research is underway." [2]. DHS: "This approach may or may not result in a formal report." [6] |
| **Related Documents** | full | Medium-high | [7] "Relevant documents" and "consent forms, recruitment documentation, and facilitator guides"; [3] "Important links" and "Keep a running list of links to key research documents, including shared folders or assets."; [11] "Part 7: Resources/Links to Documentation"; [8] the link-out line; [26] | **Holds at medium-high.** Two short lists carry it (below). Gap candidate 15 enters lean Method as an ASK |

**Three findings bear on the ruled section set without overturning it.** None changes it.

- **Related documents sits in NN/g's minimum [7] and in dscout's seven [11].** Two of the four short lists carry a
  links section; User Interviews' [9] and Dovetail's [8] do not. That argues for lean placement, against the ruling
  of full. Confidence: low to medium. The route is an ASK, not a move.
- **Consent reaches the short lists only as a linked form [7] or a recruiting bullet [4].** That supports the
  full-only section, with a lean ASK.
- **The session script is excluded at every size against most sources read** (Finding 3). The ruling stands as a
  labelled POSITION.

**Nothing argues for a new section.** Every candidate that clears E1 already has a home in the eleven. The rest
fail E3, are quality properties, or are unsupported.

### 11. Spec sentences this research tests

These are candidates for a dated note in the spec, not a silent rewrite. Each is maintainer-vetoable.

**Weakened:**

- `:7114-7118`, the session-script exclusion at medium confidence. Five sources embed the script and two link it
  (Finding 3). The ruling stands; the spec's own reasoning, catalog entry 25, carries it, not the sources.
- `:7024` and `:7109-7110`, digital.gov's twelve sections. The stored copy names eleven [3].
- `:7183-7186` and `research-docs.md:35-36`, Gilad's line quoted without his qualifier [19].
- `research-docs.md:90-91`, NN/g's one-study line quoted without its "sometimes" [7].
- `:7194-7196`, the project-brief boundary, which rests on NSW alone [5].
- `:7231-7234`, the facts older than the plan. Each is right, but two carry a trap the spec does not name. The
  strategy's goal sentence goes on to name the PRD's and the KPI dashboard's versions of the goal
  (`templates/product-strategy/product-strategy_example.md:110-113`). The roadmap's Saved Views line calls it the
  second-view problem (`templates/product-roadmap/product-roadmap_example.md:50-51`). See the example note.

**Tested and holding:**

- `:6992-6993` and `:7071-7072`, that no source names a short and a long form of one plan (Finding 1).
- `:7025`, the usability-test-plan identity. Still one publisher in words; the nesting now has structural support
  from three more sources (Finding 4).
- `:7119-7123`, the exclusions of a standing plan and of the request (Finding 3).

**Strengthened:**

- `:7097`, the research-question line, which gains 18F's "Research questions are different from interview
  questions." [2].
- `:7100`, Participants and Recruiting's payment clause, now sourced [10], [2].
- `:7103-7104`, Roles and Observers and Consent, Privacy and Ethics, toward high (Finding 10).

---

## Claims flagged contested or time-bound

1. **Whether the session script belongs in the plan.** Inside [1], [9], [10], [11], [17]; linked [7], [8]; NN/g
   does both [7].
2. **What a brief is.** The request [8]; the session guide [10]; the study's whole document [26]; an analogy [33].
3. **Whether a written plan is needed for small or continuous research.** Lighter or none [23], [25]; always,
   however brief [9], [22].
4. **One study or several per plan.** Typically one, sometimes several [7]; several plans per audience [2]; a
   round under a standing service plan [4].
5. **Participant numbers** [6], [8], [12], [13], [14]. No single figure.
6. **Time for analysis.** digital.gov: "a safe estimate is twice as long as you give to data collection" [3].
   GOV.UK: "For every 2 hours of research, you should do 1 hour of analysis." [4]. They may not measure the same
   thing: one speaks of a timeline, the other of hours.
7. **Whether to recruit for a demographic mix.** For [28]; against [6].
8. **Whether the plan changes during the study.** Updated after [7]; reviewed as the project progresses [5]; a
   living document before the study [10]; held steady [11].
9. **Test versus experiment.** Gilad's line is his own definition, by his own account [19].
10. **Who writes it.** A researcher [11], [22]; the product trio runs discovery [23]. No source names a product
    manager.
11. **Formative and summative.** One 1997 source uses the words [16].
12. **Time-bound facts.** 18F's guide is archived as of 2025-01-20 [2]. The usability.gov template is retired and
    was read through a 2024-02-21 snapshot [18]. GOV.UK's round page dates from 2016 [4], and Calgary's page from
    1997 [16]. Michigan Tech's assignment is from 2020 [17], Torres's article from 2021 [23] and Boag's from 2023
    [25]. GOV.UK's "4 or more different services" [20] is an operating rule that may change. MeasuringU's and
    dscout's sample dates carry no year [11], [13]. Every vendor page is a living page.
13. **An unverified figure.** Koji's statistic attributed to NN/g is excluded and may not be cited.

---

## Honest framing

**What the bundle exists to say.** A user research plan, as this bundle builds it, is a short document written
before one study of people runs. It says why the study runs and which decision it informs. It says what the team
needs to learn, how, from whom and when. For a usability test, it also sets the tasks and the measures. Each part is
sourced: the definition [7], [9]; the timing [5], [7]; the minimum [7], [9]; the decision [8], [29], [33]; the
usability block [12], [13], [18]; the share-out [8], [9], [10]. **The lean and full pair is the library's
construction** from two published lengths, and the conditional usability section is the library's arrangement.

**What the bundle must not claim:**

- **That a plan improves research or product outcomes.** No source in this log measured it.
- **That every team writes one.** Continuous-discovery teams may not [23], and Boag argues for less [25].
- **That linking rather than embedding the session script is received practice.** It is a POSITION (Finding 3).
- **That a plan covers exactly one study by any source's rule.** NN/g says typically, and sometimes not [7].
- **That telemetry analysis is not research by any source's definition, or that the finish line is sourced.** Both
  are the contract's POSITION (`research-docs.md:14-17`).
- **That any source calls a study of a shipped product discovery work** (Finding 8).
- **That a product manager usually writes the plan.** No source says so.
- **That a second publisher states the usability-test-plan identity in words.** Only NN/g does [7].
- **That Gilad's test-and-experiment line is industry usage.** He says it is not [19].
- **That formative and summative are current practitioner vocabulary** [16].
- **That any participant count is the standard** [6], [8], [12], [13], [14].
- **That 18F's guide or the usability.gov template is current federal guidance** [2], [18].
- **That a plan records a recommendation or a decision.** unitQ's four outcomes [34] belong to the report and to
  the decision documents.
- **That a programme budget, a reserve or a fixed retention period belongs in one study's plan** [32], [36].

---

## Notes for the companion

**The load-bearing sections.** Four of the skeleton's eleven (`templates/methodology.md:172-182`) carry this
bundle. **Origins** must teach the two published lengths and the government lineage, with the two retired sources
dated (Findings 1 and 7). **Debates** must name the disputes over the session script, the word brief, whether to
plan at all, and participant counts (Findings 3 to 5). **Relationships** must carry the experiment pair with
Gilad's qualifier, and the QA pair's shared words. It must also place the documents that use the findings, the
project brief, the standing service plan and the other member. **Anatomy** must label which parts are sourced and
which are the library's arrangement: the size split, the conditional usability block and the script's exclusion.
Wherever the companion explains the phase, it carries the shipped-product paragraph (Finding 8).

**The sharpest teaching points:**

1. **Name the decision before the questions** [8], [29].
2. **Research questions are not interview questions** [2], [8].
3. **Write goals with verbs that name an output.** 18F: "use verbs that specify the output like “describe,”
   “evaluate,” “quantify,” or “identify.” Avoid vague words like “understand” or “explore.”" [2].
4. **Pilot the sessions before they count** [4], [12], [13], [17].
5. **For a usability test, set a success criterion for each task before the sessions** [13], [18].
6. **Agree the plan before recruiting starts** [8], [22], [33].
7. **Do not over-specify the outputs** [2]. A formal report is not always the result [6].
8. **Keep it short** [8], [12], [13].

**Section design.** Finding 10 maps the research onto the eleven ruled sections, and Finding 9 routes every gap
candidate under decision procedure 12. Every proposed change there is a candidate, and this log admits none. The
strongest are five ASKs. Schedule and Logistics asks about a pilot, and the first section asks what would change
the decision. Lean Participants and Recruiting asks about consent and access needs. Lean Method links the session
guide.

**The traps:**

1. **Quoting anything that is not a Quotable line**: the clauses lost in the ten drops, and the dimension-file
   spans listed in the checks section.
2. **Quoting Gilad without his qualifier** [19], or NN/g's one-study line without its "sometimes" [7].
3. **Presenting the script's exclusion as what the sources do.** Most embed it.
4. **Using test plan alone where `test-plan` collides**, or calling a usability test an experiment.
5. **Importing unitQ's build-or-drop recommendation, or a decision log, into the plan** [34].
6. **Importing a programme budget or reserve** [32], **or a standing policy's retention periods** [36], as the
   plan's own figures.
7. **Repeating bare figures as standards**: participant counts, analysis ratios, and the Design System's "4 or more
   different services" [20].
8. **Using brief without saying which sense** (Finding 3).
9. **Citing 18F's guide or usability.gov without their dates** [2], [18].
10. **Reusing the worked example's scenario in GOOD and WEAK text**, the risk the spec names (`:7337-7339`). Grep
    the drafted templates and guide for Saved Views, Recurring Analyst, Priya Nair, friction study, Team Lead and
    re-filter before review. The usability block's GOOD text uses a usability test unrelated to the example
    (`:7142-7143`).

**The example.** The maintainer ruled the scenario on 2026-10-24 (ruling 7,
`docs/internal/tier2-specs.md:7389-7390`). The plan plans the 2026-05 Reporting friction study, which four shipped examples cite and none shows. It uses the
full variant (`:7089-7090`). Priya Nair, PM, Reporting, writes it, dated 2026-04-20. Acme's UX Research function
runs the sessions. That is a function, not a person. No individual researcher is named anywhere in the thread
(`dim2.md`). A build that adds one greps every example for the name first (`:7258-7260`). The method is
one-to-one interviews of about an hour, each with a walkthrough of the analyst's own dashboard. The sessions run
from 2026-05-04 to 2026-05-15 with 12 analysts. The report follows on 2026-05-27, and the design brief on
2026-06-01. Tasks and Measures is marked not applicable in one line, because a walkthrough of a participant's own
work is not a usability test (`:7262-7265`).

- **Facts dated on or before 2026-04-20 that the plan may cite, each with its own date.**
  - **The user persona**, dated 2026-01-05 (`templates/user-persona/user-persona_example.md:8`) and owned by Priya
    Nair (`:6`). Its study is its own: interviews held in November and December 2025, n=12 (`:42`, `:90-91`). Its
    figures: 9 of 12 raised re-filtering (`:54`), and 6 of 12 kept a personal spreadsheet (`:71`). What We Already
    Know may cite them as the persona study's figures, never as the friction study's.
  - **The FY26 product strategy**, dated 2026-01-28
    (`templates/product-strategy/product-strategy_example.md:7`), and its `Time to Insight` goal (`:110`). The same
    sentence goes on to name the PRD's and the KPI dashboard's versions of the goal (`:110-113`). Both documents
    postdate the plan, so cite the goal by name and not those versions.
  - **The FY26 roadmap**, dated 2026-02-11 (`templates/product-roadmap/product-roadmap_example.md:8`). Saved Views
    sits in its Now lane, `Being specified now` (`:50-52`), and shared views across a team sit in its Next lane
    (`:63-65`). Both lines frame their items in second-view terms (`:50-51`, `:64-65`), which belong to a different
    problem. Cite the placement, not that framing.
- **Not to conflate.** The problem statement of 2026-01-09
  (`templates/problem-statement/problem-statement_example.md:7`) frames a different problem, the new-account
  second-view stall (`:2`), measured by telemetry (`:74`). Dovetail's and Maze's habit of opening a plan with a
  problem statement [8], [10] makes the borrowing tempting. The plan must not cite it as its own problem.
- **Not citable.** The risk register is dated 2026-07-20 (`templates/risk-register/risk-register_example.md:6`),
  after the plan. Its R-04 row, the risk that analysts do not adopt Saved Views, names `Priya Nair / UX Research`
  (`:69`). That row is the build's evidence for the UX Research function, not something the plan cites.
- **Not carried.** The per-user preferences storage that shipped in Q1 appears only in the PRD
  (`templates/prd/prd_example.md:38`), which postdates the plan. No document dated on or before 2026-04-20 states it, so the plan leaves it out.
- **Trap 1: two 12-person studies.** Never merge their figures (`:7238-7243`). No `6 of 12` and no spreadsheet
  appears as a friction-study fact. The review greps both examples for both strings (risk 2, `:7334`). On this
  log's reading, the plan is safer citing the persona's re-filtering figure and leaving its spreadsheet figure out.
  Both studies also report a `9 of 12` about filters (`user-persona_example.md:54`, `prd_example.md:44`), so each
  use must name its study. The study's analysts are customers' analysts, since it studies a dashboard customers
  already use (`:7267`). But the nine customer accounts (`user-persona_example.md:90-91`) belong to the persona's
  study and must not be reused.
- **Trap 2: the plan must not presuppose its own finding.** Its questions ask where analysts lose time between
  opening a report and acting on it. They may name the twice-deferred request as one thing to probe
  (`:7244-7247`). 18F's goal verbs fit: a goal to identify or quantify where time goes, never to confirm a known
  cost [2].
- **The Team Lead is at most a hypothesis to probe.** The design brief says the study surfaced that audience
  (`templates/design-brief/design-brief_example.md:53-55`, `:60-61`).
- **Make relative frequency countable.** The PRD later reports re-filtering as `ahead of export and share`
  (`templates/prd/prd_example.md:35-36`). The method should let the sessions count re-filtering against exporting
  and sharing. Otherwise the report's claim has no design behind it (`dim2.md`).
- **What it must not contain.** No minutes-per-day figure (`:7279-7281`). No concept and no decision. No document
  dated after 2026-04-20 cited as existing: not the report, the design brief, the PRD, the epic, the risk register
  or the announcement. The plan may name the readout it intends to produce, as a plan. The opening Worked example
  blockquote may mention later documents, as sibling examples do
  (`templates/product-strategy/product-strategy_example.md:14-20`).
- **Check the siblings' own text, not this note.** Read the persona, strategy, roadmap, problem statement, PRD and
  design brief examples before writing, and make every carried fact match them exactly.

## Sources

### Government services: the long form

**[1] 18F, "Draft Web Design Standards Research Plan: DATE" (research-plan-template.md, web-design-standards-ux repository).** practitioner. **fetched-and-verified.**
`https://raw.githubusercontent.com/18F/web-design-standards-ux/master/Background%20and%20Process/research-plan-template.md`
Supports: Full verbatim section-by-section structure of a blank fillable research plan, including the day-of-testing consent and PII language and the moderator opening script
Quotable: "## Introduction"
Quotable: "## Assumptions"
Quotable: "## Target audiences"
Quotable: "## Research goals"
Quotable: "## What methods will we use?"
Quotable: "## Recruitment needs"
Quotable: "## Logistics checklist"
Quotable: "## Day of testing protocol"
Quotable: "## What will we do when?"
Quotable: "## Opening script (EDIT BASED ON PROJECT)"
Quotable: "3. Participants will need to sign a consent form (see attached). Scan and forward the signed ones to ."
Quotable: "4. Research team should ensure that no PII data is captured. Participants should input fake data if needed."
Quotable: "Your participation in this activity is completely voluntary, and we will not ask for more than 45 minutes of your time. If at any time you'd like to end our session, that is your right and we will gladly wrap things up."
Quotable: "With your permission, we will be audio taping these sessions. The information that is captured will only be used for evaluation, research and training purposes and will not be shared outside of the project team. Is it OK for me to begin recording now?"
Quotable: "We will **not** write your name on our interview notes"
Quotable: "We will **not** label our recordings of our interview with your name."
Quotable: "We keep the list of people we interviewed, our notes, and the recording in a secure place where only team members can access it."
Quotable: "We will **not** ask for, or collection, any information that easily identifies you."
Quotable: "At the bottom, you can choose whether we may share quotes from your interview. Unless you give us permission, we will not share any quotes from your interview (even anonymized ones) outside our project team."
Quotable: "* NAME (Lead moderator)"
Quotable: "1. (If in person) Research team should wear their government-issued badge and have it visible to the participant at all times."
Quotable: "Research team should ensure that no PII data is captured."
Quotable: "Participants will need to sign a consent form (see attached)."
Quotable: "Research goals"

**[2] 18F, "Writing a research plan" (UX Guide, Research > Plan).** practitioner. **fetched-and-verified.**
`https://guides.18f.org/ux-guide/research/plan/`
Supports: Full section list for a research plan, verbatim Background/Goals/Ethical considerations/Research questions/Team participation/Timeline/Participants and recruiting/Outputs and outcomes text, the archived-as-of banner, and the explicit multiple-plans-per-audience statement
Quotable: "Archived as of January 20, 2025"
Quotable: "A research plan (sometimes also called a research protocol), describes the design of your research. Typical 18F research plans include:"
Quotable: "Background"
Quotable: "Goals"
Quotable: "Research questions"
Quotable: "Methods"
Quotable: "Team participation"
Quotable: "Timeline"
Quotable: "Participants and recruiting"
Quotable: "Ethics considerations"
Quotable: "Outputs and outcomes"
Quotable: "Describe factors that the research will need to account for, including any shared beliefs or forces motivating the research itself. Review and summarize any relevant secondary sources (like websites, reports, case studies, presentations); or link to prior research plans or earlier versions of the concepts you’re testing."
Quotable: "Design research is fundamentally about reducing risk and informing decisions. When writing your goals, use verbs that specify the output like “describe,” “evaluate,” “quantify,” or “identify.” Avoid vague words like “understand” or “explore.”"
Quotable: "Research affords your team powerful opportunities to interact with people and to explore what’s possible. While 18F’s UX team agrees on our own ethical principles for design research , these are just our own. Discuss and clarify ethical principles with your team and your partners. Note any ethical dilemmas or concerns. Identify potential hazards in your product/service and ensure that your research will not bring harm to participants."
Quotable: "Research questions are high-level questions that reflect what you want to learn to make better evidence-based decisions. Research questions are different from interview questions."
Quotable: "Good research is collaborative. People who help accomplish the research are more likely to agree with its outputs."
Quotable: "You may need multiple research plans to account for the variety of ways people may experience or navigate your design. The audience you're designing for may be very broad."
Quotable: "Outputs are the documents, diagrams, etc. you will make to share the research with a broad audience. Will you produce a report, useful insights, validated design hypotheses, or something else?"
Quotable: "Outcomes are the changes you expect to see through doing the research. Outcomes should tie back to the goals and subgoals listed earlier."
Quotable: "We follow a lean, iterative process, which allows the team to be more responsive and flexible to redefine outputs based on what the process finds. Avoid over-specifying your outputs, because you don't know what you’ll find until the research is underway."
Quotable: "A roster is a spreadsheet to collect participants’ names, titles, contact information, and to track whether they’ve been contacted, interviewed, thanked, etc."
Quotable: "Destroy this roster at the end of the engagement."
Quotable: "A research plan (sometimes also called a research protocol), describes the design of your research."
Quotable: "You may need multiple research plans to account for the variety of ways people may experience or navigate your design."
Quotable: "Ethical considerations"

**[3] Digital.gov (GSA), "How to write a research plan".** practitioner. **fetched-and-verified.**
`https://digital.gov/resources/how-write-research-plan`
Supports: Full verbatim numbered model of research-plan sections, the single worked title example, the roles table, and the sample timeline table
Quotable: "Title of research plan"
Quotable: "Include the name of the effort, the method of research, and the target user participants. For example, a GSA.gov redesign effort using readability interviews with senior citizens would be titled: GSA.gov redesign readability interviews with senior citizens"
Quotable: "Authors and stakeholders"
Quotable: "Context"
Quotable: "What led to the study"
Quotable: "The history of the project"
Quotable: "Any details about the partner or stakeholders"
Quotable: "Past research"
Quotable: "Provide a summary and links to any available assets from past related research."
Quotable: "Research goals and questions"
Quotable: "Document why you are doing research and the questions the research will answer."
Quotable: "Research methods"
Quotable: "Roles and responsibilities"
Quotable: "Outline team roles and responsibilities for the research effort. An activity can be assigned to an individual, or led by an individual with team participation."
Quotable: "Timeline"
Quotable: "Provide a rough estimate for your timeline to help manage expectations around the study execution. Remember to give more time than you think you need for analysis and synthesis (a safe estimate is twice as long as you give to data collection)."
Quotable: "Participants and recruiting"
Quotable: "Document who you are hoping to talk to during the research. This can include information about the participants, how you are planning to recruit, and logistical considerations."
Quotable: "Issues for awareness"
Quotable: "Note any legal, ethical, accessibility, bias, or power concerns raised by the research plan and how the team will mitigate them."
Quotable: "Important links"
Quotable: "Keep a running list of links to key research documents, including shared folders or assets."
Quotable: "Include a short description of relevant helpful context and background, such as:"
Quotable: "Note the method or methods of research you will be using, such as contextual inquiry or usability testing."
Quotable: "Remember, an interdisciplinary research team leads to better research outcomes."
Quotable: "An example from a moderated usability test is below."
Quotable: "people designing your research"

**[4] GOV.UK Service Manual, "Plan a round of user research" (User research community).** standards. **fetched-and-verified.**
`https://www.gov.uk/service-manual/user-research/plan-round-of-user-research`
Supports: Full verbatim contents list and body text for the round-of-research planning page, including the explicit statement that a round can only be planned once a service-level research plan already exists, informed consent, and observer/role definitions
Quotable: "You can only plan specific rounds of research when you’ve created a research plan for your service ."
Quotable: "Set your research objectives"
Quotable: "Find participants"
Quotable: "Plan the session times"
Quotable: "Arrange recording and note-taking"
Quotable: "Prepare the prototype or beta service"
Quotable: "Run a practice session"
Quotable: "Invite people to watch the sessions"
Quotable: "Get the team to help out"
Quotable: "Plan time for analysis"
Quotable: "Related guides"
Quotable: "which kinds of participants you need to include"
Quotable: "how you’ll cater for any access needs"
Quotable: "how you’ll find them within your budget"
Quotable: "how you’ll collect their informed consent"
Quotable: "Your observation room manager is in charge of: making sure observers are comfortable and understand what’s happening"
Quotable: "making sure that observers are paying attention and taking notes"
Quotable: "answering observers’ questions"
Quotable: "coordinating discussion and analysis immediately after sessions"
Quotable: "Anyone who understands the aims of the research and is willing to help can do these roles - it does not need to be another researcher or member of the team."
Quotable: "You need to have a research assistant with you when you visit participants. They are responsible for: taking notes and photographs"
Quotable: "managing recordings"
Quotable: "asking additional questions"
Quotable: "For every 2 hours of research, you should do 1 hour of analysis."
Quotable: "Published: 16 March 2016"
Quotable: "Last updated: 23 May 2016"
Quotable: "You can only plan specific rounds of research when you’ve created a research plan for your service."
Quotable: "You can only plan specific rounds of research when you've created a research plan for your service."

**[5] Digital NSW (Department of Customer Service), "Research plan" (Digital Service Toolkit, Activities and templates).** practitioner. **fetched-and-verified.**
`https://www.digital.nsw.gov.au/delivery/digital-service-toolkit/activities-and-templates/research-plan`
Supports: The guide-page framing of the research plan (when/why/what-you-get) and the per-effort, before-research-starts positioning of the document; the downloadable Word template itself was not reached from this cached text
Quotable: "Use this template to document your plan for conducting research."
Quotable: "Use for: Defining your plan for research"
Quotable: "When: Before you’ve started any research"
Quotable: "With: Your research team"
Quotable: "A good research plan helps you plan and define your research goals."
Quotable: "Your team, stakeholders and participants benefit from a clear research plan. It lays out the path ahead, identifies key activities and gaps in your thinking, and aligns teams and stakeholder on the intended outcomes of the research."
Quotable: "What’s it for"
Quotable: "Documenting your plan for research, enabling alignment and visibility for your team and stakeholders."
Quotable: "When to do it"
Quotable: "After you have been given an initial project brief, but before you commence any official research activities."
Quotable: "You should have workshopped or drafted the problem you’re trying to solve or the opportunity space to explore."
Quotable: "You have a goal for the research."
Quotable: "Step 1: Go through the template filling out the sections of the research plan. Keep it clear and in plain English."
Quotable: "Step 2: Present back to your wider team and stakeholders so you can get buy-in for your research and your team’s next steps."
Quotable: "Regularly review and update your research plan as the project progresses."

**[6] U.S. Department of Homeland Security, "DHS Usability Testing Kit" (dhs.gov/cx).** practitioner. **fetched-and-verified.**
`https://dhs.gov/cx/dhs-usability-testing-kit`
Supports: Verbatim section headings and body text for the four usability-testing approaches, including moderator/note-taker/observer role definitions, consent-form steps, recruiting instructions, participant counts, and the softening caveat on whether a formal report results
Quotable: "Usability testing is a way to learn how easy or difficult it is for people to use something by observing them actually using it."
Quotable: "Someone to run the test"
Quotable: "Someone to help observe and take notes"
Quotable: "Someone who might use what you’re testing"
Quotable: "Something you want to test"
Quotable: "In a usability test, you show materials to individuals, one at a time. You ask each person to use what you’ve given them, and you watch and listen without teaching or training."
Quotable: "Try to test at least four people who normally might use the material you’re testing. If you think there might be different behaviors for different types of users, include four of each type."
Quotable: "Don’t worry about demographics like age, education, or income . Think more about what experience participants might have doing the tasks you want to observe, and simply recruit a range."
Quotable: "You don’t need a large sample of participants . Don’t worry about “statistical significance.”"
Quotable: "Getting Familiar with Usability Testing"
Quotable: "Planning Your Usability Test"
Quotable: "Holding a Practice Test"
Quotable: "Four Approaches to Usability Testing"
Quotable: "Testing in the Office: Quick Usability Feedback from Colleagues"
Quotable: "Testing Out of the Office: Catch Real Users in the Field"
Quotable: "Testing in the Conference Room: Thorough, Structured Testing with Real Users"
Quotable: "Testing by Videoconference with Remote Users"
Quotable: "Who to Test With"
Quotable: "What You’ll Need"
Quotable: "Where to Do It"
Quotable: "How to Do It"
Quotable: "Recruiting - Walk down the hall or to the next department to find someone who’s not familiar with the material."
Quotable: "Testing - When they’ve agreed to help you out, have each participant complete the consent form and demographic questionnaire."
Quotable: "This approach may or may not result in a formal report."
Quotable: "Reporting - Using the report template provided, compile your results into a report, highlighting all stages of the usability test (i.e., participant data, testing locations, material tested, findings, and recommendations)."
Quotable: "You can do usability testing almost any time, but it's most useful:"
Quotable: "Before you start redesigning something"
Quotable: "While you're still working on a draft"
Quotable: "Make sure to use the moderator's guide and note taking guide provided."
Quotable: "A usability test is made up of one-on-one sessions with one moderator and one user or participant."
Quotable: "A note taker may support the moderator by logging observations and discussion."

### Vendors and practitioners: the short form and its minimum

**[7] Maria Rosala (Nielsen Norman Group) - "Research Plans: Organize, Document, Inform".** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/pm-research-plan/`
Supports: Section list and minimum, length (absent), plan vs. interview/facilitator guide, sharing with stakeholders, updating the plan after the study
Quotable: "A research plan can come in many forms and formats. However, all plans should cover the following:"
Quotable: "Purpose and goals of the research study"
Quotable: "Participants"
Quotable: "Method and procedure"
Quotable: "Relevant documents such as consent form, screener, study protocol"
Quotable: "A research plan will often contain details about the study's purpose, who will be recruited and participate in the research, how the research will be conducted, and where relevant study collateral is stored."
Quotable: "Usually, research plans will have a section that lists the relevant research questions, research goals, or hypotheses."
Quotable: "A research plan should list the user-research method(s) employed in the study and how the study will be conducted."
Quotable: "Tasks, prompts, or interview questions that will be provided to participants"
Quotable: "Share your research plan with relevant stakeholders to get buy-in. Research plans help stakeholders understand what's in scope and why the research is being performed. They also set expectations on what will be learned. You can ask stakeholders to provide input on draft research plans. Involving stakeholders in the planning process can ensure that the outcomes are understood and accepted when reporting the study findings."
Quotable: "Update the plan after the research study is over. In moderated studies, it's common to make adjustments during the study to get better data. For example, tasks or interview questions may be removed, changed, or added. Update anything that changed so that the research plan accurately reflects what you did."
Quotable: "Since each research study is a little different, your research plans can differ in structure, content, and format from one study to the next."
Quotable: "A research plan is a document that outlines the goals, methods, and logistical details of a research study."
Quotable: "Typically, a research plan is constructed for each study."
Quotable: "A research plan is a document that outlines the goals, methods, and logistical details of a research study. (When planning a usability test, the research plan is often referred to as a test plan.)"
Quotable: "Relevant documents"
Quotable: "sometimes, a research plan could include numerous studies or phases of research"
Quotable: "interviews and a diary study"
Quotable: "consent forms, recruitment documentation, and facilitator guides"
Quotable: "All UX-research studies should start with a plan."
Quotable: "outlines the goals, methods, and logistical details of a research study"

**[8] Dovetail - "UX research plan template".** vendor. **fetched-and-verified.**
`https://dovetail.com/ux-research-plan-template/`
Supports: Explicit seven-section list in a stated order, an explicit page-length minimum, an explicit RQ-vs-interview-question distinction, an explicit plan-vs-brief distinction
Quotable: "A complete plan has seven sections: background and problem statement, objectives, research questions, method, participants and recruitment criteria, timeline and milestones, and a share-out plan."
Quotable: "Background explains why the study exists and what decision it informs. Objectives narrow that to one or two outcomes, and research questions break each objective into things you can answer with evidence. The rest-method, participants, timeline, share-out-is the logistics that make the study real."
Quotable: "Seven sections: background and problem statement, objectives, research questions, method, participants and recruitment criteria, timeline and milestones, and a share-out plan. The first three carry the most weight-they define why the study exists and what it must answer. The rest covers logistics so the study can start without another round of meetings."
Quotable: "One to two pages. A plan is a working agreement, not a thesis-if stakeholders can't read it in five minutes, they won't. Link out to supporting material like discussion guides and screeners rather than embedding them."
Quotable: "A brief is the request-what a stakeholder wants to learn and why it matters to them. A plan is the response-how you'll actually study it, with method, participants, and timeline. In practice, a good plan starts by restating the brief as objectives. That's the moment to catch misalignment, before any sessions are booked."
Quotable: "Research questions describe what you need to learn, not what you'll ask participants. "Why do trial users abandon setup?" is a research question; "Walk me through your setup" is an interview question that helps answer it. Keep them answerable with evidence, tied to your objectives, and limited to three to five per study."
Quotable: "One or two decisions this research will inform-written down, agreed with stakeholders"
Quotable: "What you need to learn, phrased as questions evidence can answer-not interview questions"
Quotable: "Your plan should state who qualifies, who doesn't, and how many sessions you need-five to eight participants per segment is enough for most qualitative studies. Write screener criteria into the plan so recruitment can start the day it's approved."
Quotable: "Yes. The plan lives in your project alongside everything it produces-recordings, transcripts, highlights, and insights. ... Findings stay traceable to the research questions you started with."
Quotable: "A research plan turns a vague request into a study you can actually run-and defend."
Quotable: "Participants"
Quotable: "How long should a research plan be?"
Quotable: "One to two pages."
Quotable: "Insight templates give your share-outs the same structure every time, so findings always trace back to the questions you set out with."
Quotable: "Background explains why the study exists and what decision it informs."
Quotable: "Findings stay traceable to the research questions you started with."
Quotable: "Research questions"

**[9] User Interviews - "How to Create a User Research Plan" (UX Research Field Guide chapter).** vendor. **fetched-and-verified.**
`https://www.userinterviews.com/ux-research-field-guide-chapter/create-user-research-plan`
Supports: A six-label minimum list in a stated order, a seven-step authoring process in a stated order, sharing/using findings, no stated length, moderator guide treated as a sub-detail inside the plan rather than a separate document
Quotable: "At a minimum, your research plan should include:"
Quotable: "What: Your research question(s) and goals"
Quotable: "Why: Business goals"
Quotable: "How: Methodology"
Quotable: "Who: Participants"
Quotable: "When and where: Research schedule and logistics"
Quotable: "Next steps"
Quotable: "Research goals state what you're trying to learn or accomplish with your research."
Quotable: "Your research questions should reflect the goals of your study and should be: Specific enough that you'll know when you've reached an answer ... Practical in that you could answer them within the scope of a study ... Actionable, meaning you could act on your findings once you've completed your research study"
Quotable: "In the methodology section of your research plan, you'll also need to include the details of your study, like a moderator guide for interviews, or the wireframe you're using for a usability testing study."
Quotable: "Your study is super quick and easy and doesn't need a plan? It still needs a plan, but it can be a brief one."
Quotable: "Consider how you will analyze and report on your research findings. Good research analysis begins at the planning stage, before research actually begins."
Quotable: "Think about the kinds of artifacts your study will produce, and how you'll present them to internal stakeholders. Will you share findings as you go or wrap it all up in a final report? ... Share research results in the format(s) that will be most relevant to your stakeholders."
Quotable: "1. Identify your research goals"
Quotable: "2. Develop your research question(s)"
Quotable: "3. Gather available data and existing insights"
Quotable: "4. Choose the right research method(s)"
Quotable: "5. Design your study"
Quotable: "6. Have a recruiting strategy"
Quotable: "7. Be ready to share your research findings"
Quotable: "A user research plan is a document (or less commonly, a slide deck or internal wiki page) that outlines the goals, objectives, and logistical considerations of a research project for your internal stakeholders and team."
Quotable: "It still needs a plan, but it can be a brief one."
Quotable: "ensuring that your inquiry remains focused on answering the key research questions defined at the outset"
Quotable: "they are also useful tools for effectively reporting on the results of your research"

**[10] Maze - UX research plan chapter, "Essential Elements to Create a UX Research Plan" (quoting Paige Bennett, Senior User Research Manager at Affirm, and Sinéad Davis Cochrane, Research Manager at Workday).** vendor. **fetched-and-verified.**
`https://maze.co/guides/ux-research/plan/`
Supports: An eight-step section list in a stated order, an explicit plan-vs-strategy-vs-design distinction, 'brief' used to mean the session guide/script (not the stakeholder request), 'living document' framing for changing the plan, no stated length
Quotable: "1. Define the problem statement"
Quotable: "2. Identify your objectives"
Quotable: "3. Get stakeholders buy-in"
Quotable: "4. Choose the right research method"
Quotable: "5. Determine how to recruit participants"
Quotable: "5.1. Determine how you'll pay them"
Quotable: "6. Prepare the brief"
Quotable: "7. Establish the timeline"
Quotable: "8. Decide how you'll present your findings"
Quotable: "A UX research plan-not to be confused with a UX research strategy or research design-is a plan to guide individual user experience (UX) research projects."
Quotable: "While your UX research plan should be based on strategy, it's not the same thing. Your UX strategy is a high-level document that contains goals, budget, vision, and expectations. Meanwhile, a plan is a detailed document explaining how the team will achieve those strategic goals. Research design is the form your research itself takes."
Quotable: "In short, a strategy is a guide, a plan is what drives action, and design is the action itself."
Quotable: "The difference between a UX research plan and a UX research strategy is that they cover different levels of scope and detail. A UX research plan is a document that guides individual user experience (UX) research projects. UX research plans are shared documents that everyone on the product team can and should be familiar with. A UX research strategy, on the other hand, outlines the high-level goals, expectations, and demographics of the organization's approach to research."
Quotable: "The next component of a research plan is to create a brief or guide for your research sessions. The kind of brief you need will vary depending on your research method, but for moderated methods like user interviews, field studies, or focus groups, you'll need a detailed guide and script. The brief is there to remind you which questions to ask and keep the sessions on track."
Quotable: "It's good practice to involve stakeholders at early stages of plan creation to get everyone on board. Sharing your UX research plan with relevant stakeholders means you can gather context, adjust based on comments, and gauge what's truly important to them."
Quotable: "Seeing the UX research plan as a living document makes it much easier to edit based on team comments."
Quotable: "In your plan, mention how you'll share insights with the product team."
Quotable: "It's important to make sure your stakeholders are on the same page with regards to scope, timeline, and goals before you start."
Quotable: "While your UX research plan should be based on strategy, it's not the same thing."
Quotable: "A detailed list of expectations including deliverables, timings, and type of results"
Quotable: "A broad outline of the entire research project"
Quotable: "test tasks you'll ask participants to perform during unmoderated sessions"
Quotable: "you can run usability tests to get actionable feedback"
Quotable: "Usability test sample with Maze:"

**[11] Nikki Anderson-Stanier (dscout) - "How to Write a User Research Plan That Sets Your Project Up for Success".** practitioner. **fetched-and-verified.**
`https://dscout.com/people-nerds/how-to-write-a-user-research-plan-that-sets-your-project-up-for-success`
Supports: A seven-part section list in a stated order that puts the Interview Guide INSIDE the plan, who writes/reviews it, sharing/using findings, 'switching the goal in the middle' as the thing a plan prevents, no stated document length
Quotable: "The 7 core components of a user research plan"
Quotable: "The background of the research project detailing why we are conducting this study. This can also include the internal stakeholders involved."
Quotable: "The objectives and goals of the research, what the teams want to learn from the research, or what they would like the outcome to be."
Quotable: "A breakdown of the participants we are recruiting and how we are recruiting them."
Quotable: "How we are conducting the research, which includes the chosen research method."
Quotable: "An interview guide as a cheat sheet of instructions/questions to follow during the research session. This includes components within itself, such as the introduction, interview questions and conclusion."
Quotable: "An approximate timeline of when the research will take place, and when a report could be expected."
Quotable: "Resources for people to find, such as links to any other documentation."
Quotable: "Part 1: Background"
Quotable: "Part 2: Objectives"
Quotable: "Part 3: Participants"
Quotable: "Part 4: Methodology"
Quotable: "Part 5: Interview Guide"
Quotable: "Part 6: Approximate Timeline"
Quotable: "Part 7: Resources/Links to Documentation"
Quotable: "A user research plan is a concise reference point for your project's timeline, goals, main players, and objectives. It's not always used extensively after the project has started."
Quotable: "Research plans keep the entire team focused on an outcome and provide an easy reference to keep “need-to-know” stakeholders in the know. They prevent everyone from getting bogged down in the details and from switching the goal of the research in the middle by mistake."
Quotable: "With the project in hand, you're ready to sit down and write a plan. Then you can share the first draft with the product team to ensure you're interpreting their aims correctly."
Quotable: "Research plan creation and review: Wednesday, August 7th"
Quotable: "This walk-through will teach you how to write a plan in 15 minutes that'll save you hours of work down the road."
Quotable: "Some researchers stay away from this timeline, as it can solidify a deadline that may prove more difficult to meet than expected. I always stress that it is a basic approximation."
Quotable: "If you'll be talking to your users in real time, an interview guide is a valuable cheat sheet. It reminds you of which questions will help you meet your objectives, and can keep your discussions on track."
Quotable: "A user research plan is a concise reference point for your project’s timeline, goals, main players, and objectives."
Quotable: "serve as a kick-off document for a project"
Quotable: "A user research plan is a concise reference point for your project's timeline, goals, main players, and objectives."

### The usability case: tasks, success criteria and measures

**[12] Nielsen Norman Group - "Checklist for Planning Usability Studies".** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/usability-test-checklist/`
Supports: task framing (exploratory vs. specific tasks), pilot sessions, metrics, moderated/unmoderated and in-person/remote choices, participant counts, and the relation of a usability test to general user research goals
Quotable: "Meet with the stakeholders to determine what they want to learn. Identify the questions, concerns, areas of interest, and purpose for the research. The goals will determine which UX research methodology to choose."
Quotable: "In lab or in field : Should you conduct the study at your facility or go to the participant's location?"
Quotable: "Moderated or unmoderated : Moderated studies tend to provide you with richer design insights and opportunities to probe and ask for clarification... unmoderated studies can be cheaper, quicker, and may provide better access to hard-to-recruit participants."
Quotable: "In-person or remote : In general, we recommend in-person studies whenever possible... However, sometimes in-person testing may not be feasible."
Quotable: "For traditional qualitative studies, we generally recommend 5 participants for the best return on investment."
Quotable: "Quantitative studies and eyetracking require a larger sample size to obtain meaningful conclusions. Expect to increase the number of participants by at least 4 times. You may need at least 20-30 participants in each target user group"
Quotable: "Exploratory tasks : These open-ended tasks answer broad, research-oriented goals and may or may not have a correct answer... they are not appropriate for quantitative testing."
Quotable: "Specific tasks : These tasks are much more focused and usually have a correct answer or end point. They are used for both qualitative and quantitative testing."
Quotable: "Writing solid tasks is critical in conducting a valid study. Strong tasks are concrete and free from clues that might prime people's behavior."
Quotable: "After you have written your tasks, make sure to run a pilot study to help you fine-tune the task wording, anticipate the number of tasks you can give per session, and determine the order in which to present them."
Quotable: "Note : Pilot studies are especially important when conducting online unmoderated studies because you are not present to give clarification or make corrections if study participants misinterpret the instructions or task descriptions."
Quotable: "Common usability metrics are: time on task, satisfaction ratings, success rate, and error rate."
Quotable: "If you decide to collect subjective measurements (e.g., ease of use or satisfaction questions about the task, satisfaction about the system), decide on when you will give the questionnaires: after each task, at the end of the session, or both."
Quotable: "Once you've figured out how you're going to conduct the research, document your approach in a test plan and share it. This document serves as a communication tool among team members and a record for future studies. The document doesn't need to be lengthy, but should contain key information such as: Name of the product or site being testing"
Quotable: "Study goals"
Quotable: "Logistics: time, dates, location, and format of study"
Quotable: "Participant profiles"
Quotable: "Tasks"
Quotable: "Metrics, questionnaires"
Quotable: "Description of the system"
Quotable: "document your approach in a test plan and share it"
Quotable: "a communication tool among team members and a record for future studies"
Quotable: "are usually written in the form of scenarios and should match the goals of the study"
Quotable: "time on task, satisfaction ratings, success rate, and error rate"
Quotable: "doesn't need to be lengthy"
Quotable: "Checklist for Planning Usability Studies"
Quotable: "9. Motivate Team Members to Observe Sessions"
Quotable: "Write a Test Plan"

**[13] Jeff Sauro, MeasuringU - "What Goes into a Usability Test Plan?".** practitioner. **fetched-and-verified.**
`https://measuringu.com/usability-test-plan/`
Supports: task-scenario wording, task-level and session-level measures (SEQ, SUS, SUPR-Q, NPS), pre/post questions, pilot timeline, moderated/remote mix, participant numbers
Quotable: "For each task scenario you'll want to define at a minimum what information you'll give the user (the scenario) and the starting URL or screen."
Quotable: "Task Completion: Determine an objective success criteria for each task."
Quotable: "Task Difficulty: Some of the most salient times during a usability test occur immediately after each task. You'll therefore want to include at least one question on the perception of task difficulty. We use the we use a single ease question."
Quotable: "Confidence: Users tend to be overconfident when completing tasks, meaning they think they completed the task successfully more often than they actually did"
Quotable: "We usually collect standard demographic data prior to users attempting any tasks. This is also an opportunity to ask attitudinal and brand questions before users know what the study is about."
Quotable: "In addition to the test-metrics like SUS, SUPR-Q or NPS, we also like to include a few open-ended questions about what the users would improve and comments or issues they had"
Quotable: "Identify the services you'll use to collect the data. Will it be a moderated remote, moderated in-person, mobile or a mix of in-person and unmoderated studies. Many usability studies we conduct use a mix-method approach (usually 5-10 moderated) and between 50 and 300 unmoderated users."
Quotable: "The folks at Usability.gov have a comprehensive template (which you'll need to trim down to suit your needs) and Chapter 5 of the Handbook of Usability Testing has a detailed discussion about building a test plan."
Quotable: "Conduct Pilot Test & Report on Recommended Changes 8/23 - 8/25"
Quotable: "Nevertheless, it's a good idea to spell out a few sections in each test plan."
Quotable: "It's both good practice and often necessary to have a test plan before beginning a usability test."
Quotable: "For each task scenario you'll want to define at a minimum what information you'll give the user"
Quotable: "Many organizations are “document factories,”"
Quotable: "Test plans, like many documents, can take on a life of their own and become bloated and unnecessarily complex."
Quotable: "What Goes into a Usability Test Plan?"
Quotable: "Task Metrics"
Quotable: "Test Metrics"
Quotable: "Pre-Test Questions"
Quotable: "Post-Test Questions"
Quotable: "While each plan will vary based on the organization and test situation, here are the sections we use most often."
Quotable: "The folks at Usability.gov have a comprehensive template"
Quotable: "If possible, try to outline how the report will be structured in the test plan."

**[14] Maze - "The 10-step checklist to create a usability testing plan" (A Beginner's Guide to Usability Testing, Ch. 4).** vendor. **fetched-and-verified.**
`https://maze.co/guides/usability-testing/plan/`
Supports: task types (exploratory/specific), evaluation metrics, pilot test, moderated/unmoderated and in-person/remote, participant numbers
Quotable: "Exploratory tasks: these are open-ended tasks that don't have a right or wrong answer... Specific tasks: these tasks usually have a right or wrong answer, and look at how to perform a specific task."
Quotable: "Time-on-task: how long does it take for participants to complete a usability task?"
Quotable: "Critical errors: these are errors that impact the success of the usability task... Non-critical errors: these are minor deviations from the usability test goal..."
Quotable: "Error-free rate: the percentage of participants that complete the usability task with no errors whatsoever; think of this as a north star metric."
Quotable: "Successful task completion: this is the percentage of tasks that are successfully completed by participants overall, regardless of how they got there."
Quotable: "It's a good idea to plan a pilot usability test-a rehearsal with someone from your organization. Make sure your pilot participant has had no part in the usability testing process so far, otherwise you risk enacting false-consensus bias"
Quotable: "Moderated or unmoderated: finally, decide whether researchers will be present during testing (moderated) or whether the participants will be alone (unmoderated)."
Quotable: "In-person or remote: both in-person and remote usability testing have their advantages and disadvantages-in-person testing takes participants out of their natural environment, but gives you more control over the testing conditions. Remote testing provides real-life context, but can make it harder to control environment-based biases."
Quotable: "the marginal benefit of each research participant decreases dramatically past four or five participants"
Quotable: "most quantitative research methods benefit from more research participants... This is the time that having 30+ participants is ideal."
Quotable: "A usability testing plan is an overview of the steps you'll take and methodologies you'll use when conducting usability testing."
Quotable: "Aims and goals: outline why you're conducting the research and what you're looking to achieve."
Quotable: "Test participants and methodologies: include information on the specifics of who and how."
Quotable: "Analyzing results: how are you going to derive insights from your research?"
Quotable: "Outcomes and next steps: finally, include details on what happens next."
Quotable: "Error-free rate: the percentage of participants that complete the usability task with no errors whatsoever"
Quotable: "Successful task completion: this is the percentage of tasks that are successfully completed by participants overall"
Quotable: "6. Write tasks that match your goals"
Quotable: "Your usability tasks are the actions you'll get research participants to perform during usability testing."
Quotable: "It's essential you consider what success looks like before you begin usability studies."
Quotable: "it's the often overlooked, but essential first step to conducting usability testing"

**[15] University of Washington UX Pedagogy - "Usability Testing Template" page (citing Emma Rose, 2023, EngageCSEdu).** academic. **fetched-and-verified.**
`https://sites.uw.edu/uxpedagogy/learn-teach/usability-testing-template`
Supports: existence of a flexible usability-testing-plan template for teaching, but only as an abstract page
Quotable: "This usability testing plan template gives individual students or teams a structure to help plan, conduct, and analyze data from a study. The template walks students through the process of planning a study through a series of questions and planning materials."
Quotable: "gives individual students or teams a structure to help plan, conduct, and analyze data from a study."
Quotable: "The template walks students through the process of planning a study through a series of questions and planning materials."
Quotable: "PDF from ACM Digital Library is available via open access."
Quotable: "Download the Zip file of the materials + template + consent."

**[16] Saul Greenberg's CPSC 681 course page (University of Calgary GroupLab), 1997 - "Usability Testing - Developing a Test Plan".** academic. **fetched-and-verified.**
`https://grouplab.cpsc.ucalgary.ca/saul/681/1997/jas/plan.html`
Supports: formative vs. summative test goals, task list framing, performance/preference measures, purpose and problem statements
Quotable: "There must be a decision made on the goal of the usability test. If the test goal is formative then one of the four formative usability type tests can be persued. If the test is goal is summative then a controlled experiment can be undertaken."
Quotable: "Formative testing can be exploratory, assessment oriented, validation oriented or comparative."
Quotable: "Task List. A representative list of tasks to be performed by the users is essential to maintain a high degree of professionalism during the test and avioding confusion and headaches for both the test experimenter as well as the participant."
Quotable: "Number and percent of tasks completed (within the alloted time) correctly"
Quotable: "incorrectly"
Quotable: "Time needed to recover from errors"
Quotable: "Number of errors made"
Quotable: "Ease of use"
Quotable: "learning"
Quotable: "installation"
Quotable: "Comparison to other products"
Quotable: "Problem statements / Test objectives. These statements are most important in defining the issues and questions to be resolved as well as finalizing the type of usability test to use. These should be not be vague but specific."
Quotable: "The tasks in this list should consist of tasks that will ordinarily be performed by the eventual user."
Quotable: "A detailed description should be made as to which actions or behaviours are required for each successful task."
Quotable: "Time to complete task"
Quotable: "Number and percent of tasks completed (within the alloted time) correctly / incorrectly"
Quotable: "This decision process will be relatively easy to make, dependent on the present design phase."
Quotable: "it is extremely difficult to shift gears from a design iteration formative test to a more controlled summative test."

**[17] Robert Pastel, Michigan Tech CS4760/HU4628/CS5760 - "Project Evaluation and Usability Test Assignment 3 - Test Plan".** academic. **fetched-and-verified.**
`https://cs4760.csl.mtu.edu/2020/eval-usability-test-assignment-3-test-plan/`
Supports: scenario/task structure, pre/post questionnaires, pilot testing before the actual test, and the test plan's role among other usability-test documents
Quotable: "The goal of the test plan is to describe the tasks that the participant will perform, how you will observe their interactions with the product, and the questions you will ask or other feedback you will elicit from the participants."
Quotable: "A test plan serves as an outline or checklist for the test, so that the testing personnel don't forget any details."
Quotable: "The usability test plan is produced and the protocols are pilot-tested before the actual tests are conducted."
Quotable: "A test protocol consists of one or more test scenarios, which may or may not be identical to the scenarios you produced earlier in the semester. Each scenario may have multiple tasks associated with it."
Quotable: "The scenario descriptions, tasks, and pre- and post-questionnaires should be fully fleshed out in sentences appropriate for reading to the participant."
Quotable: "Pre- and post-test interview or questionnaire questions (see below for required questions; you should also include some questions specific to your app and your test)."
Quotable: "Several documents are generated during the development, analysis, and reporting of a usability test; for this course you will concentrate on the usability test plan and usability report."
Quotable: "usability testing will be accomplished by observing representative users performing defined tasks on a prototype."
Quotable: "Each test scenario should be about two pages (roughly 500 words) long"
Quotable: "The test scenarios should evaluate unique and critical aspects of the app design."
Quotable: "A customizable test plan template is available here:"

**[18] Usability.gov (U.S. GSA/Digital.gov) - "Usability Test Plan Template" (.docx), retrieved via Wayback Machine snapshot of 2024-02-21.** practitioner. **fetched-and-verified.**
`http://web.archive.org/web/20240221184353/https://www.usability.gov/how-to-and-tools/resources/templates/usability-test-plan-template.html`
Supports: the full canonical federal usability-test-plan headings and boilerplate: task description, usability metrics (completion rate, error-free rate, time on task), subjective evaluations, roles, severity classification, pre/post questionnaires, remote vs. lab procedure
Quotable: "This document describes a test plan for conducting a usability test during the development of [web site name or application name]. The goals of usability testing include establishing a baseline of user performance, establishing and validating user performance measures, and identifying potential design concerns"
Quotable: "The task descriptions below are required to be reviewed by the application owner, business-process owner, development owner, and/or deployment manager to ensure that the content, format, and presentation are representative of real use and substantially evaluate the total application. Their acceptance is to be documented prior to usability test."
Quotable: "Usability metrics refers to user performance measured against specific performance goals necessary to satisfy usability requirements. Scenario completion success rates, adherence to dialog scripts, error rates, and subjective evaluations will be used. Time-to-completion of scenarios will also be collected."
Quotable: "Participants will complete a pretest demographic and background information questionnaire."
Quotable: "After each task, the participant will complete the post-task questionnaire and elaborate on the task session with the facilitator. After all task scenarios are attempted, the participant will complete the post-test satisfaction questionnaire."
Quotable: "[Usability Lab Testing] Participants will take part in the usability test at [put the name of the testing lab here]... [For Remote Testing] Participants will take part in the usability test via remote screen-sharing technology."
Quotable: "Subjective evaluations regarding ease of use and satisfaction will be collected via questionnaires, and during debriefing at the conclusion of the session."
Quotable: "The usability tasks were derived from test scenarios developed from use cases and/or with the assistance of a subject-matter expert."
Quotable: "The tasks are identical for all participants of a given user role in the study."
Quotable: "Usability metrics refers to user performance measured against specific performance goals necessary to satisfy usability requirements."
Quotable: "Completion rate is the percentage of test participants who successfully complete the task without critical errors."
Quotable: "A completion rate of [100%/enter completion rate] is the goal for each task in this usability test."
Quotable: "Error-free rate is the percentage of test participants who complete the task without any errors (critical or non-critical errors)."
Quotable: "An error-free rate of [80%/enter error-free rate] is the goal for each task in this usability test."
Quotable: "It is measured from the time the person begins the scenario to the time he/she signals completion."
Quotable: "Critical errors are deviations at completion from the targets of the scenario."
Quotable: "Non-critical errors are errors that are recovered from by the participant or, if not detected, do not result in processing problems or unexpected results."
Quotable: "To prioritize recommendations, a method of problem severity classification will be used in the analysis of the data collected during evaluation activities."

### Practice: who writes a plan, when, and where practice disagrees

**[19] Itamar Gilad - "Idea Validation Using the AFTER model".** practitioner. **fetched-and-verified.**
`https://itamargilad.com/idea-validation-much-more-than-just-a-b-experiments/`
Supports: (g) how Gilad separates a usability test from an experiment, and the Tests-vs-Experiments taxonomy that frames a usability test as a lower rung than an experiment
Quotable: "Experiments are tests that include a control element to guard against false results caused by random chance."
Quotable: "Per this definition an A/B test is an experiment, but a usability test is not."
Quotable: "I realize that this is not the common definition used in the industry - in many cases the words test and experiment are used interchangeably. I chose this definition because it’s closer to how scientists think of experiments."
Quotable: "Usability Tests - In Usability Tests we ask users to try using the product under the supervision and guidance of a tester."
Quotable: "There are four types, or levels, of idea validation methods: Assessment, Fact Finding, Tests, and Experiments."
Quotable: "While experiments are the gold standard, of validation, there are many other, far cheaper and more immediate ways to test an idea. By fixating on experiments many companies set the bar too high, miss out on easier opportunities, and often give themselves an excuse to keep doing things the old way."

**[20] GOV.UK Design System community team - "Share findings about your users".** standards. **fetched-and-verified.**
`https://design-system.service.gov.uk/community/share-research-findings/`
Supports: (f) what the Design System says about taking findings from services at any stage, after going live included, and about findings aggregated across services
Quotable: "Your service might be in the alpha or beta phases, or you might be iterating the service after going live."
Quotable: "Feedback from any phase helps us iterate the Design System in line with evolving user needs."
Quotable: "summaries of user research you’ve done"
Quotable: "We do not usually act immediately on feedback - we need to grow a clear body of evidence before we can be sure that something is a problem."
Quotable: "we will usually investigate something if we hear similar findings from 4 or more different services"
Quotable: "Even if your findings do not lead to a change to the Design System, it’s really useful to share anyway. People across government read the discussions on GitHub to see how others have approached things and what they’ve learned."
Quotable: "You must get informed consent from your participants before you can share findings of any research they’ve participated in."
Quotable: "whether it was a qualitative or quantitative study"
Quotable: "We want to hear how users experience styles, components and patterns in your service."
Quotable: "Use this template to give the community useful context about your findings."
Quotable: "we need to grow a clear body of evidence before we can be sure that something is a problem."
Quotable: "we will usually investigate something if we hear similar findings from 4 or more different services."
Quotable: "Give us some context and briefly explain how you gathered the findings."

**[21] GOV.UK Service Manual, User research community - "Getting informed consent for user research".** standards. **fetched-and-verified.**
`https://www.gov.uk/service-manual/user-research/getting-users-consent-for-research`
Supports: (d) consent, recording permission, and personal data in practice: what informed consent requires, how it is obtained and evidenced, legal/data-protection review of the information sheet, and withdrawal
Quotable: "Whenever you do user research, you must get the participant's 'informed consent'. This means getting a record from them to show they understand your research and agree to take part."
Quotable: "You need to get consent from all research participants, even if they work for your organisation."
Quotable: "You must also tell participants how you'll handle their personal data, including: which organisation is responsible for their data (known as the 'data controller')"
Quotable: "We recommend that you provide participants with an 'information sheet' during recruitment."
Quotable: "Check with your organisation's data protection expert or legal adviser that your document complies with the law."
Quotable: "For face-to-face research sessions, the simplest way to collect evidence of consent is to have the participant sign a paper consent form."
Quotable: "If a participant withdraws their consent during a research session, you must stop and delete any research data you've collected."
Quotable: "If you want to do research with children or vulnerable adults (people who are unable to take care of themselves or are at risk of harm or exploitation), you need to get informed consent both from the participant and from a parent, guardian, carer or other responsible adult."
Quotable: "whether the session is being observed (and who's watching)"
Quotable: "whether and how the session is being recorded"

**[22] Defra (Department for Environment, Food and Rural Affairs) Digital Service Manual - "Research scoping and planning".** standards. **fetched-and-verified.**
`https://digital.defra.gov.uk/user-research/scoping-research`
Supports: (e) review/sign-off of a plan by stakeholders and a research operations/lead-researcher function, as a mandated government workflow
Quotable: "Research plans are mandatory for all DDTS user researchers."
Quotable: "Run a research scoping workshop with key stakeholders and colleagues using the research scoping workshop template."
Quotable: "Capture the agreed scope in the research plan template and make sure the approach represents all users."
Quotable: "Submit the research plan to your lead user researcher (if your delivery group has one) for review or approval."
Quotable: "Share the approved plan with your team so everyone is aligned."
Quotable: "run scoping workshops to build a shared understanding of the problem"
Quotable: "create and agree research plans so research meets programme and stakeholder needs before delivery starts"

**[23] Teresa Torres (Product Talk) - "Product Discovery Basics: Everything You Need to Know".** practitioner. **fetched-and-verified.**
`https://www.producttalk.org/2021/09/continuous-discovery/`
Supports: (a) who writes/runs research in practice - the product trio (PM, designer, engineer) leading discovery and interviewing together, not a dedicated researcher
Quotable: "The product trio-comprised of a product manager, design lead, and tech lead-is responsible for product discovery."
Quotable: "A product trio-typically comprised of a product manager, a designer, and a software engineer-leads product discovery. However, that doesn't mean other members of the team don't contribute."
Quotable: "The product trio should interview customers together. They should collaborate on and execute assumption tests together. These are the key inputs to good product discovery decisions."
Quotable: "Good product discovery teams engage with customers at least weekly, minimizing the number of decisions they make without customer input."
Quotable: "If we are continuously making decisions about what to build, we need to stay continuously connected to our customers, so that we can ensure that our product discovery decisions will work for our customers."
Quotable: "While there's nothing inherently wrong with project-based research, it's not sufficient for teams who continuously ship value to customers."

**[24] Teresa Torres (Product Talk) - "Evaluative Research" (Discovery Glossary).** practitioner. **fetched-and-verified.**
`https://www.producttalk.org/glossary-discovery-evaluative-research/`
Supports: (c) generative vs. evaluative research, defined by one of the field's most-cited continuous-discovery practitioners, and why a plan needs to say which kind a study is
Quotable: "Evaluative research is when teams test their solutions through assumption testing-evaluating whether their ideas will work before fully building them."
Quotable: "Generative research helps teams discover opportunities through story-based customer interviews. Evaluative research helps teams test which solutions will best address those opportunities."
Quotable: "Both types of research are essential for continuous discovery. Generative research helps teams discover what matters to customers. Evaluative research helps teams discover which solutions will best create value for customers while driving business outcomes."

**[25] Paul Boag - "A Pragmatist's Guide To Lean User Research" (Smashing Magazine).** practitioner. **fetched-and-verified.**
`https://mobile.smashingmagazine.com/2023/03/pragmatists-guide-lean-user-research`
Supports: (b) whether a written plan is worth writing for small/fast research - an explicit named source arguing a team can skip a full discovery phase and keep research very light, with its own qualifier about scope
Quotable: "if time is tight, don't feel like you have to do a full-blown discovery phase just because articles like this tell you to"
Quotable: "Instead, start by collating what the organization already knows about the user and their needs."
Quotable: "Your focus should be on answering specific questions, not improving your general understanding of the user."
Quotable: "it is better to conduct user research only when there is a specific question that needs answering"
Quotable: "Many little bits of user research are easier to insert than a single significant discovery phase."
Quotable: "Of course, this is only true if the types of user research you do are lightweight."
Quotable: "Yes, a discovery phase is best practice. It is our chance to challenge our assumptions about the users and their needs. However, we don't always get to do what we should, and not every discovery phase needs to take a lot of work."
Quotable: "I know this post will make user researchers uncomfortable, and I can fully understand why. The results you get back will be far from perfect and could possibly lead to false conclusions. However, it is better than the alternative."

**[26] Nikki Anderson (Founder, The User Research Strategist) - "Research Roadmaps: A Tactic for Greater Org-Wide Alignment" (Dscout People Nerds).** practitioner. **fetched-and-verified.**
`https://dscout.com/people-nerds/research-roadmap`
Supports: (f) the difference between one study's plan and a standing research roadmap/backlog, and (c) the generative-vs-evaluative imbalance a roadmap can surface. This is a different dscout.com page from the 'research plan' article named as owned by another dimension
Quotable: "Creating a shareable roadmap of your research efforts can help you better prioritize your work and better demonstrate that work's value."
Quotable: "After creating my first roadmap, I saw a long list of evaluative research studies-usability test after usability test. This information was a massive signal that we were over-indexing evaluative research and not leaving enough time for generative research."
Quotable: "When I had mapped out the current and upcoming studies, I went to my manager and showed him that we weren't incorporating enough discovery research. We also discussed the long list of projects in the backlog and decided to create a rolling research program."
Quotable: "At first, my roadmap and backlog were incredibly simple. They included the project's name, those involved, and the approximate study dates. But, over time, they evolved and became much more robust."
Quotable: "A link to the intake document or research brief, which has all the relevant information for the study, including script, deliverables, and a report."
Quotable: "My backlog is essentially a stripped-down version of the roadmap"

### The gap question: what good plans add

**[27] Anna Lee, "The best way to get your UX Research project started" (Askwhy, Substack).** practitioner. **fetched-and-verified.**
`https://askwhy.substack.com/p/the-best-way-to-get-your-ux-research?s=w`
Supports: A good plan has a dedicated hypothesis section with a worked example, and a stakeholder section that sorts people into those who must be involved versus merely informed
Quotable: "2. Hypothesis By having this clear and understood, as a researcher, you can suggest the right approach."
Quotable: "An example of a hypothesis could look like this. People want to use messaging for all kinds of situations to communicate to others, there’s no situation where messaging isn’t useful."
Quotable: "6. Stakeholders List out all your stakeholders to ensure there are those that are involved in kicking this off and are aware of the efforts and will wait and those who simply need to be informed."

**[28] AnswerLab, "Inclusive UX Recruiting: How to Get a Diverse Mix of Participants for Every UX Research Study".** practitioner. **fetched-and-verified.**
`https://www.answerlab.com/insights/inclusive-ux-recruiting-how-to-get-a-diverse-mix-of-participants-for-every-ux-research-study`
Supports: Accessibility and inclusion belong in the recruiting/screener design for one study: ask about accommodations, recruit a demographic mix by default, and track it
Quotable: "It’s very important to ask if participants need any accommodations to participate in a study, whether conducted in-person or remotely."
Quotable: "Make sure your researcher is prepared to adjust the session questions or prototypes if necessary to accommodate these participants’ needs."
Quotable: "We recommend including a mix of participants with a range of genders, ethnicities, ages, income, education, and more in every study you conduct."

**[29] Shannon L. Coleman, PhD, "The Difference Between a Finding and a Decision" (Ground Truth, Substack).** practitioner. **fetched-and-verified.**
`https://byshannoncoleman.substack.com/p/the-difference-between-a-finding`
Supports: A good plan names, before fieldwork, the decision the study is meant to inform and what would change that decision -- and states what the study cannot answer
Quotable: "Start with the decision, not the question. Before specifying a research question, name the decision it is meant to inform. Who is making it. What the options are. What would change their choice. What they already know. What the research needs to add that they don’t already have."
Quotable: "Define what you cannot answer. A research design that is honest about its own limitations is more useful for decisions than one that presents findings with false completeness."

**[30] Kara Pernice, "How and Why to Recruit Backup Participants (aka “Floaters”) in User Research" (Nielsen Norman Group).** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/recruit-backup-users-in-research/`
Supports: A fallback for when recruiting falls short (no-shows, cancellations) is a planned, costed element: overrecruiting floaters or extra sessions, decided in advance
Quotable: "“No-show” participants or last-minute cancelations can thwart the project schedule, make stakeholders lose interest in the research, and waste money."
Quotable: "To ensure that you have enough participants when you need them, you can practice “intentional overrecruiting.”"
Quotable: "each lost participant represents a fairly substantial proportion of your potential insights, and thus reduces the profitability of your design project."

**[31] Kim Flaherty, "Always Pilot Test User Research Studies" (Nielsen Norman Group video).** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/videos/pilot-test/`
Supports: A pilot session (run before the real sessions, data discarded) is recommended practice for assessing a study's effectiveness before the main fieldwork
Quotable: "Running a pilot test for a user research study enables you to assess the study's effectiveness and avoid common problems in the main study."
Quotable: "Pilot testing (a session or two before the real test) helps fine-tune usability studies, leading to more reliable results. It provides an opportunity to validate the wording of the tasks, understand the time necessary for the session, and, if all goes well, may even supply an additional data point for your study."

**[32] CleverX Team, "Research budget template for product and UX teams" (CleverX Blog).** vendor. **fetched-and-verified.**
`https://cleverx.com/blog/research-budget-template-product-ux-teams`
Supports: A budget/cost line is a standard plan element, broken into participant incentives, recruitment platform fees, tool costs, researcher hours, plus an explicit reserve
Quotable: "A research budget template for product and UX teams should map every method you plan to run to four cost components: participant count, incentive per session, platform or recruitment fee, and researcher hours."
Quotable: "A line item labeled “user research: $40,000” gives a finance reviewer nothing to validate."
Quotable: "Step 4: Add a 15% reserve. Research programs always encounter urgent or reactive studies that were not planned."

**[33] Koji Docs, "UX Research Plan Template: How to Structure Any Research Project".** vendor. **fetched-and-verified.**
`https://www.koji.so/docs/ux-research-plan-template`
Supports: Stakeholder sign-off on the plan before fieldwork is a named step, explicitly tied to defining what counts as a good answer; the plan also names the downstream decision each study feeds
Quotable: "Share it before fieldwork begins: Get sign-off on the research questions from the stakeholders who will act on findings. This prevents scope creep and ensures alignment on what constitutes a good answer."
Quotable: "Specifying the downstream decision in your plan creates accountability - and increases the chance that research actually changes something."
Quotable: "Getting stakeholder sign-off on it before fieldwork begins prevents the dreaded "but we wanted to know about X" conversation after the fact."
Quotable: "Think of a research plan as a project brief for research."

**[34] unitQ Research Hub, "Research planning worksheet" (Feature Validation Research Kit, .docx template).** practitioner. **fetched-and-verified.**
`https://www.unitq.com/research/templates/research-planning-worksheet.docx`
Supports: A single worksheet for one study names the decision the study feeds, a falsifiable hypothesis with a stated confirming-evidence condition, pre-set success-criteria thresholds, a risks/bias/mitigation table, and a synthesis step that checks data against those thresholds before recommending build/iterate/drop
Quotable: "What decision will this inform? [Name the specific go/no-go or design decision this study feeds. If nothing changes based on the result, reconsider running it.]"
Quotable: "Hypothesis We believe… [the belief you’re testing about your users and their problem.] We’ll know we’re right if… [the observable evidence that would confirm it - tie this to your success criteria below.]"
Quotable: "Success criteria Define these before you start so you don’t rationalize the result afterward."
Quotable: "Risks Risk Mitigation Confirmation bias [Ask open, non-leading questions; let them react before you explain.] Small sample size [Treat findings as directional; look for strong, repeated signals.] Recruiting delays [Line up more sources than you need; over-recruit for no-shows.] Prototype quality [Make sure the concept is clear enough to react to; note where fidelity limits feedback.]"
Quotable: "Synthesize notes against your success criteria - did you hit the thresholds? Share the readout and a clear recommendation: build, iterate, keep exploring, or drop. Log the decision and rationale where your team will find it."
Quotable: "treat it like a lightweight PRD for your study"

**[35] Great Question, "Data Governance for UX Research" (product feature page).** vendor. **fetched-and-verified.**
`https://cms.greatquestion.co/features/data-governance`
Supports: Vendor evidence that data retention/deletion of recordings and transcripts is treated as a planned, controllable element of a study, tied to company retention policy
Quotable: "Automate how you delete recordings and transcripts with one click. Reduce your data footprint and comply with your company’s data retention policies."

**[36] University of Westminster, "Website user experience testing and research privacy statement".** primary. **fetched-and-verified.**
`https://westminster.ac.uk/about-us/our-university/corporate-information/information-compliance-records-management-and-information-security/personal-data-protection/website-user-experience-testing-and-research-privacy-statement`
Supports: A concrete, non-vendor example of a stated data retention/deletion period for one research program's recordings, notes, and personal data
Quotable: "Access to any personal information collected during your participation in website User Experience (UX) testing and research is limited by permissions to only those authorised staff within the University who need to access and manage your data"
Quotable: "Personal information and audio recordings will be retained for 12 months from the date of the interview and then deleted. Notes will be retained for 36 months from the date of the interview and then deleted."

**[37] CleverX Team, "Qualitative coding: a thematic analysis tutorial" (CleverX Blog).** vendor. **fetched-and-verified.**
`https://cleverx.com/blog/qualitative-coding-thematic-analysis-tutorial-for-user-research/`
Supports: NULL RESULT: read in full looking for an analysis/synthesis method stated as a pre-fieldwork plan element; the article teaches how to code and theme transcripts after collection but never frames stating an analysis approach as something that belongs in the plan written before the study runs
