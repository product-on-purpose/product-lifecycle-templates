# Companion: The User Research Plan

> The deep explainer for the user-research-plan bundle. Read this to understand what the document is,
> where its sections come from, and where the sources genuinely disagree. The short operator card is
> [`user-research-plan_guide.md`](user-research-plan_guide.md); a fully worked instance is
> [`user-research-plan_example.md`](user-research-plan_example.md). Inline citations like
> [[7]](#ref-7) resolve to the [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A user research plan is written before one study of the people a product serves. It says why the study
runs and which decision its findings will inform. It says what the team needs to learn, from whom, how,
and when. Two sources converge on nearly the same sentence for what the document is. Nielsen Norman
Group: "A research plan is a document that outlines the goals, methods, and logistical details of a
research study." [[7]](#ref-7). User Interviews: "A user research plan is a document (or less commonly,
a slide deck or internal wiki page) that outlines the goals, objectives, and logistical considerations of
a research project for your internal stakeholders and team." [[9]](#ref-9). 18F supplies the catalog's
alias: "A research plan (sometimes also called a research protocol), describes the design of your
research." [[2]](#ref-2).

For a usability test, the plan also sets the tasks and the measures. One publisher states the identity
in words: "A research plan is a document that outlines the goals, methods, and logistical details of a
research study. (When planning a usability test, the research plan is often referred to as a test
plan.)" [[7]](#ref-7). No second source states the identity in a sentence, so this companion treats it as
a single publisher's naming. The nesting of tasks and measures inside the general plan, separately, has
structural support from three more sources, covered in section 3.

**At a glance**

- It is written **before** the study. Digital NSW: "When: Before you’ve started any research"
  [[5]](#ref-5). Its job is to get agreement before sessions are booked, not to report what happened.
- Nielsen Norman Group ties it to **one study**, most of the time: "Typically, a research plan is constructed for each study." [[7]](#ref-7), with its own qualifier that "sometimes, a research plan could include numerous studies or phases of research" [[7]](#ref-7). Other sources draw the line differently; section 6, item 4 covers the disagreement.
- **Two lengths are published, never as a stated pair.** A short form carries a named minimum; a long
  form, from government digital services, runs nine to eleven headings. No source names a short and a
  long form of the same plan. The lean and full sizes this bundle ships are this library's own
  construction from those two lengths, not a documented split. Section 4 covers this fully.
- For a usability test, it carries **tasks and measures** set before the sessions run: a success
  criterion per task, and the metrics the sessions will collect. For any other method, that block says so
  in one line and marks its task table and measure lines N/A.
- **No source measured whether writing a plan improves a study's outcome, or a product's.** The case for
  the document rests on practitioner testimony about what a plan is for, not on a controlled comparison
  of planned against unplanned studies.

## 2. Origins and evolution

The research log carries no single founder and no founding date for this document type. What it carries
is two sources for its shape: government digital services, which publish the long form, and UX research
vendors and practitioners, who publish the short form and its minimum.

**Government digital services publish the long form, in the US and the UK.** 18F
ships a fill-in template on GitHub: a title, ten second-level headings running from Introduction through
Opening script (EDIT BASED ON PROJECT), and a per-task block [[1]](#ref-1). 18F's own UX Guide names a
nine-item list from "Background" to "Outputs and outcomes" [[2]](#ref-2), and it carries a notice this
companion must repeat whenever it cites that guide: "Archived as of January 20, 2025" [[2]](#ref-2).
Digital.gov, GSA's own site, publishes its own numbered model, with
eleven named sections running from "Title of research plan" to Important links, in the page as read for
this research [[3]](#ref-3). GOV.UK's Service Manual publishes a page for planning one round of research
under a standing service-level plan, with its own nine steps from "Set your research objectives" to
"Plan time for analysis" [[4]](#ref-4). Defra, a UK government department, makes a research plan
"mandatory for all DDTS user researchers" [[22]](#ref-22) and adds a review step this companion covers in
section 3.

**Vendors and practitioners publish the short form, with a named minimum.** Nielsen Norman Group states
one: "all plans should cover the following:" four items from "Purpose and goals of the research study" to
"Relevant documents" [[7]](#ref-7). User Interviews states a six-item minimum running from "What: Your
research question(s) and goals" through "Next steps" [[9]](#ref-9). Dovetail answers its own question,
"How long should a research plan be?" with "One to two pages." [[8]](#ref-8), over seven named sections.
Maze lists eight steps [[10]](#ref-10), and dscout seven parts [[11]](#ref-11).

**The lineage trap this family's contract names.** This plan borrows section structure from government
digital services in the US and the UK: 18F's template and guide [[1]](#ref-1)
[[2]](#ref-2), digital.gov's model [[3]](#ref-3), GOV.UK's round-planning page [[4]](#ref-4), and the
retired usability.gov template read through a Wayback Machine snapshot dated 2024-02-21 [[18]](#ref-18).
None of these is a regulatory form. Each is guidance, or a fill-in template, that a digital service team
published for its own and others' use. Defra's mandate binds Defra's own researchers, not product teams
generally [[22]](#ref-22). A reader who adapts this plan's full variant is borrowing a government team's
own working template, not a standard a regulator requires.

**Two published lengths, never a documented pair.** No source in this research names a short and a long
form of the same document, at medium-high confidence. Three sources come close without closing the gap.
User Interviews: "It still needs a plan, but it can be a brief one." [[9]](#ref-9) states one short plan,
not a pair of sizes. MeasuringU calls the retired usability.gov template comprehensive, "(which you'll
need to trim down to suit your needs)" [[13]](#ref-13), which names trimming, not a second published
size. DHS scales the test rather than the plan, from "Testing in the Office: Quick Usability Feedback from
Colleagues" to "Testing in the Conference Room: Thorough, Structured Testing with Real Users"
[[6]](#ref-6). The lean and full variants this bundle ships are this library's own construction from the
short and long forms the sources actually publish. Section 4 states what that construction does and does not rest on.

## 3. Anatomy (section by section)

The full variant carries eleven sections. The lean variant carries the seven marked lean below, in the
same name and order. Tasks and Measures is one of those seven: it is present at every size, and filled in
only when the study is a usability test. The remaining four sections are full-variant only.

### Why This Study, and the Decision It Informs (lean)

Why the study runs now, and which decision its findings will inform.

Two separate ideas sit in this section, and sourcing differs for each. The why-now half is the
better-evidenced one: User Interviews' "Why: Business goals" [[9]](#ref-9), dscout's "Part 1: Background"
[[11]](#ref-11), and digital.gov's "Context" [[3]](#ref-3) all give it a place near the top of the plan.
Dovetail ties the two halves together directly: "Background explains why the study exists and what
decision it informs." [[8]](#ref-8). The decision half gains three more sources, none of them a
government or NN/g source. Coleman: "Start with the decision, not the question." and "What would change
their choice." [[29]](#ref-29). Koji: "Specifying the downstream decision in your plan creates
accountability" [[33]](#ref-33). unitQ's worksheet opens with "What decision will this inform?"
[[34]](#ref-34).

**This section carries the shipped-product clause.** The family's own contract declares every member of
this family `discover`, even one that studies a product customers already use, and asks each companion
to say why. The sources treat a study of a live product as ordinary research work. GOV.UK's Design
System: "Your service might be in the alpha or beta phases, or you might be iterating the service after
going live." [[20]](#ref-20). DHS calls usability testing "most useful" first "Before you start
redesigning something" [[6]](#ref-6), which assumes something already exists to redesign. This library's
own reasoning, not any one source's claim, is that a study asking where people lose time with a product
they already use is still discovery work: it looks for an opportunity before any concept exists, the way
Torres frames generative research as helping "teams discover what matters to customers" [[24]](#ref-24).
No source in this research names a study of a shipped product as discovery work, in those words.

### Goals and Research Questions (lean)

One or two goals, and the questions the study must answer, stated as what the team needs to learn.

Four sources give this section its name and its shape: Nielsen Norman Group's "Purpose and goals of the
research study" [[7]](#ref-7), digital.gov's "Research goals and questions" [[3]](#ref-3), User
Interviews' "What: Your research question(s) and goals" [[9]](#ref-9), and Dovetail's distinction,
"Research questions describe what you need to learn, not what you'll ask participants." [[8]](#ref-8).
18F gives the same distinction its own wording: "Research questions are different from interview
questions." [[2]](#ref-2). Dovetail limits the count: "limited to three to five per study" [[8]](#ref-8).

**Research questions are not interview questions, and this is a load-bearing distinction.** A question
the plan can answer is "Why do trial users abandon setup?"; "Walk me through your setup" is an interview
question that helps answer it, by Dovetail's own pairing [[8]](#ref-8). 18F instructs a team to write
goals with verbs that specify the output, naming describe, evaluate, quantify, and identify, and to avoid
vague words such as understand or explore [[2]](#ref-2). A goal that only says a team wants to understand
users has not yet named what it needs to learn.

**A hypothesis can stand in for a question, and two sources outside government and NN/g name this
directly.** Askwhy's Lee gives a hypothesis its own numbered step, with a worked example [[27]](#ref-27).
unitQ's worksheet frames it as a belief with a confirming condition: "Hypothesis We believe… [the belief
you’re testing about your users and their problem.] We’ll know we’re right if… [the observable evidence
that would confirm it - tie this to your success criteria below.]" [[34]](#ref-34). Nielsen Norman Group
names the same alternative inside its own general section: "Usually, research plans will have a section
that lists the relevant research questions, research goals, or hypotheses." [[7]](#ref-7).

### What We Already Know (full only)

Earlier research, existing data, and the assumptions this study tests.

Four sources name this element, and none of the short-form lists carries it as a stated minimum.
digital.gov's heading is "Past research", and it asks a team to "Provide a summary and links to any
available assets from past related research." [[3]](#ref-3). 18F's template carries the heading
"Assumptions" [[1]](#ref-1), and its guide asks a team to "Review and summarize any relevant secondary
sources" [[2]](#ref-2). unitQ's worksheet carries the same idea as a hypothesis to test rather than a
fact to summarize: "Hypothesis We believe… [the belief you’re testing about your users and their
problem.]" [[34]](#ref-34). User Interviews lists gathering existing data as an authoring step rather
than a minimum item: "3. Gather available data and existing insights" [[9]](#ref-9), so this research
does not count it among the four. Boag argues the opposite emphasis for a lean plan rather than against
the element: "start by collating what the organization already knows about the user and their needs"
[[25]](#ref-25), which argues for pointing to what is known even in a short plan, not for dropping the
section from the full one.

### Method (lean)

The method or methods, why they fit the questions, the session format and length, and what participants
will see.

Eight of the ten section lists this research read carry a method element, across both the short and the
long forms; GOV.UK's round-planning steps and unitQ's worksheet name none.
User Interviews: "How: Methodology" [[9]](#ref-9). Nielsen Norman Group: "Method and procedure"
[[7]](#ref-7). digital.gov: "Note the method or methods of research you will be using, such as
contextual inquiry or usability testing." [[3]](#ref-3). Maze: "4. Choose the right research method"
[[10]](#ref-10).

**Which kind of study this is matters here, even without a dedicated field for it.** Torres distinguishes
two kinds by what they are for: "Generative research helps teams discover opportunities through
story-based customer interviews. Evaluative research helps teams test which solutions will best address
those opportunities." [[24]](#ref-24). GOV.UK's Design System asks, when findings are shared, "whether it
was a qualitative or quantitative study" [[20]](#ref-20). A method section that does not say which kind
of study this is leaves a reader to guess at what the findings can and cannot settle.

### Participants and Recruiting (lean)

Who qualifies and who does not, how many, how they are recruited, and how they are thanked or paid.

Nine of the ten section lists this research read, across both lengths, name participants. Nielsen Norman
Group: "Participants" [[7]](#ref-7). User Interviews: "Who: Participants" [[9]](#ref-9). Dovetail: "Your
plan should state who qualifies, who doesn't, and how many sessions you need" [[8]](#ref-8). digital.gov:
"Participants and recruiting" [[3]](#ref-3). GOV.UK adds access needs and budget in the same breath:
"which kinds of participants you need to include", "how you’ll cater for any access needs", and "how
you’ll find them within your budget" [[4]](#ref-4).

**Thanking or paying participants belongs here.** Maze has the step "5.1. Determine how you'll pay them" [[10]](#ref-10), and 18F's roster
tracks whether participants have been "contacted, interviewed, thanked, etc." [[2]](#ref-2). AnswerLab
argues for asking about access needs by default: "It’s very important to ask if participants need any
accommodations to participate in a study, whether conducted in-person or remotely." [[28]](#ref-28), and
for recruiting a demographic mix: "We recommend including a mix of participants with a range of genders,
ethnicities, ages, income, education, and more in every study you conduct." [[28]](#ref-28). DHS argues
the opposite for a usability test specifically: "Don’t worry about demographics like age, education, or
income" [[6]](#ref-6). Both views stand, and no source this research read reconciles them.

**A recruiting fallback is a named practice, not a late fix.** Nielsen Norman Group's Pernice names
"intentional overrecruiting" [[30]](#ref-30), for the reason that "each lost participant represents a
fairly substantial proportion of your potential insights" [[30]](#ref-30).

**Participant numbers are contested, and no single figure is a standard.** For qualitative studies,
Nielsen Norman Group recommends "5 participants for the best return on investment" [[12]](#ref-12); Maze
reports the marginal benefit falling "past four or five participants" [[14]](#ref-14); DHS asks for "at
least four people" per type of user [[6]](#ref-6); Dovetail suggests "five to eight participants per
segment" [[8]](#ref-8). For quantitative studies, Nielsen Norman Group suggests "at least 20-30
participants in each target user group" [[12]](#ref-12), and Maze names "30+ participants" as ideal
[[14]](#ref-14). MeasuringU reports its own mixed practice, "usually 5-10 moderated" and "between 50 and
300 unmoderated users" [[13]](#ref-13). This research names the ranges with their sources and does not
set one number.

### Tasks and Measures (lean, usability tests only)

The tasks as scenarios, a success criterion for each task, the task and session measures, and the
questions before and after the test. A study that is not a usability test writes one line saying so, naming
its method, and marks the task table and the measure lines N/A.

This block's content is well evidenced; where it sits inside the plan is the library's own arrangement,
at medium confidence. Nielsen Norman Group's general-purpose plan already carries "Tasks, prompts, or
interview questions that will be provided to participants" inside its method section [[7]](#ref-7), while
its own usability checklist and Maze's usability chapter give tasks and metrics their own named items,
"Tasks" and "Metrics, questionnaires" [[12]](#ref-12), beside Maze's own named items: Aims and goals,
Test participants and methodologies, Analyzing results, and Outcomes and next steps [[14]](#ref-14). That
shape is a general plan's shape with the method fixed, not a separate document.

**Tasks are written as scenarios and kept free of priming.** Nielsen Norman Group: tasks "are usually
written in the form of scenarios and should match the goals of the study" [[12]](#ref-12), and "Strong
tasks are concrete and free from clues that might prime people's behavior." [[12]](#ref-12). Tasks split
into two kinds in two independent sources: "Exploratory tasks" with no fixed answer and "Specific tasks"
with one, in both Nielsen Norman Group's [[12]](#ref-12) and Maze's [[14]](#ref-14) wording.

**A success criterion is set for each task before the sessions run.** MeasuringU: "Task Completion:
Determine an objective success criteria for each task." [[13]](#ref-13). The retired usability.gov
template sets a target directly in the document: "A completion rate of [100%/enter completion rate] is
the goal for each task in this usability test." [[18]](#ref-18), and the same for an error-free rate
[[18]](#ref-18). That template is retired, read through a 2024-02-21 Wayback Machine snapshot, and this
companion names that status wherever it cites it.

**Measures split into completion and error, and two independent sources both name them.** Nielsen Norman
Group names four: "Common usability metrics are: time on task, satisfaction ratings, success rate,
and error rate." [[12]](#ref-12). The usability.gov template defines two rates of its own: "Completion
rate is the percentage of test participants who successfully complete the task without critical
errors." [[18]](#ref-18), and "Error-free rate is the percentage of test participants who complete the
task without any errors (critical or non-critical errors)." [[18]](#ref-18). MeasuringU adds a
session-level question after each task, "a single ease question" [[13]](#ref-13), and a session-level
instrument chosen from "SUS, SUPR-Q or NPS" [[13]](#ref-13), with a caution: "Users tend to be
overconfident when completing tasks" [[13]](#ref-13).

**Questions run before, between, and after.** The usability.gov template schedules three points:
"Participants will complete a pretest demographic and background information questionnaire."
[[18]](#ref-18), then a post-task questionnaire after each task, then "the post-test satisfaction
questionnaire" once every task is attempted [[18]](#ref-18). Nielsen Norman Group leaves the timing open:
"decide on when you will give the questionnaires: after each task, at the end of the session, or both."
[[12]](#ref-12).

**Formative and summative are named in only one source, and it is a 1997 course page.** Saul Greenberg's
Calgary course page: "There must be a decision made on the goal of the usability test." [[16]](#ref-16),
and the two are hard to swap mid-study: "it is extremely difficult to shift gears from a design iteration
formative test to a more controlled summative test." [[16]](#ref-16). This companion treats the words
themselves as one source's vocabulary from 1997, not current practitioner usage. The distinction they
draw still has an echo in a second source: the retired usability.gov template's own goals include
"establishing a baseline of user performance, establishing and validating user performance measures, and
identifying potential design concerns" [[18]](#ref-18), and on this research's own reading the first two
of those read as summative goals, though usability.gov never uses either word itself.

### Schedule and Logistics (lean)

The dates, the session times, the place or tool, and how sessions are recorded and noted.

User Interviews: "When and where: Research schedule and logistics" [[9]](#ref-9). Nielsen Norman Group:
"Logistics: time, dates, location, and format of study" [[12]](#ref-12). digital.gov: "Timeline"
[[3]](#ref-3). GOV.UK: "Plan the session times" and "Arrange recording and note-taking" [[4]](#ref-4).

**A pilot session sits here, and it is strongly supported across this research.**
MeasuringU's own sample timeline schedules "Conduct Pilot Test & Report on Recommended Changes 8/23 -
8/25" [[13]](#ref-13). GOV.UK's round plan has "Run a practice session" [[4]](#ref-4). Michigan Tech: "The
usability test plan is produced and the protocols are pilot-tested before the actual tests are
conducted." [[17]](#ref-17). Nielsen Norman Group's own pilot video states the reason plainly: "Running a
pilot test for a user research study enables you to assess the study's effectiveness and avoid common
problems in the main study." [[31]](#ref-31). Maze adds a specific caution for who the pilot participant
should not be: "Make sure your pilot participant has had no part in the usability testing process so far,
otherwise you risk enacting false-consensus bias" [[14]](#ref-14).

**Time for analysis is scheduled here, and the sources disagree on how much.** digital.gov: "a safe
estimate is twice as long as you give to data collection" [[3]](#ref-3). GOV.UK: "For every 2 hours of
research, you should do 1 hour of analysis." [[4]](#ref-4). The two figures may not measure the same
thing: one speaks of a timeline, the other of hours. This research treats both as
reported practice, not as a convention either source claims the other should follow.

### Roles and Observers (full only)

Who moderates, who takes notes, and how the wider team watches sessions.

digital.gov: "Roles and responsibilities" [[3]](#ref-3). 18F: "Team participation" [[2]](#ref-2). GOV.UK:
"Invite people to watch the sessions" [[4]](#ref-4). Nielsen Norman Group's usability checklist: "9.
Motivate Team Members to Observe Sessions" [[12]](#ref-12). GOV.UK's own roles are not credentialed ones:
"Anyone who understands the aims of the research and is willing to help can do
these roles - it does not need to be another researcher or member of the team." [[4]](#ref-4). 18F's own
observer slot in the template is just as plain, a name field: "NAME (Lead moderator)" [[1]](#ref-1). DHS
names a note taker in its description of what a usability test looks like: "A note taker may support the
moderator by logging observations and discussion." [[6]](#ref-6).

**Good research is collaborative work, not a researcher working alone.** 18F: "Good research is
collaborative. People who help accomplish the research are more likely to agree with its outputs."
[[2]](#ref-2).

### Consent, Privacy and Ethics (full only)

How consent is taken, what personal data is captured and how it is kept, and any legal, accessibility, or
power concerns.

18F's guide heading is "Ethical considerations" [[2]](#ref-2); its template carries the operating lines
directly: "Participants will need to sign a consent form (see attached)." and "Research team should
ensure that no PII data is captured." [[1]](#ref-1). digital.gov's heading is "Issues for awareness",
asking a team to "Note any legal, ethical, accessibility, bias, or power concerns raised by the research
plan and how the team will mitigate them." [[3]](#ref-3). GOV.UK's dedicated consent page makes the
requirement plain:
"Whenever you do user research, you must get the participant's 'informed consent'. This means getting a
record from them to show they understand your research and agree to take part." [[21]](#ref-21), and
names what participants must be told, including "whether and how the session is being recorded"
[[21]](#ref-21) and "whether the session is being observed (and who's watching)" [[21]](#ref-21).

**Data retention belongs here, and the sources split between a plan-level instruction and a standing
policy.** 18F's template's own instruction is inside the plan: "Destroy this roster at the end of the
engagement." [[2]](#ref-2). A standing retention policy sits outside any one plan. Westminster's privacy
statement names fixed periods for one program: "Personal information and audio recordings will be
retained for 12 months from the date of the interview and then deleted. Notes will be retained for 36
months from the date of the interview and then deleted." [[36]](#ref-36). Great Question, a vendor product
page, frames the same work as something a team automates to "comply with your company’s data retention
policies" [[35]](#ref-35). This companion treats a fixed retention period as the organization's own
policy, which the plan points to rather than restates as its own figure.

### What Happens to the Findings (lean)

Which report the study produces, for whom and by when, how the report will be structured, and which
decisions the findings feed.

User Interviews: "Next steps" [[9]](#ref-9), and its authoring step "7. Be ready to share your research
findings" [[9]](#ref-9). Dovetail's "share-out plan" [[8]](#ref-8). Maze: "8. Decide how you'll present
your findings" [[10]](#ref-10), and "In your plan, mention how you'll share insights with the product
team." [[10]](#ref-10). 18F: "Outputs and outcomes" [[2]](#ref-2). MeasuringU: "If possible, try to
outline how the report will be structured in the test plan." [[13]](#ref-13).

**Two qualifiers travel with this section, and both argue against over-specifying what the study will
produce.** 18F: "Avoid over-specifying your outputs, because you don't know what you’ll find until the
research is underway." [[2]](#ref-2). DHS, for its quickest approach: "This approach may or may not
result in a formal report." [[6]](#ref-6). A plan that locks in the shape of a deck or a document before
the sessions run is promising a form the findings may not fit.

**What this section does not carry.** Several sources ask the plan to address analysis in general terms:
User Interviews asks a team to "Consider how you will analyze and report on your research findings. Good
research analysis begins at the planning stage, before research actually begins." [[9]](#ref-9); Maze
asks "Analyzing results: how are you going to derive insights from your research?" [[14]](#ref-14); GOV.UK
tells a team to "Plan time for analysis" [[4]](#ref-4). None of them asks the plan to name a specific
coding or analysis method; the nearest this research found to that narrower claim is a tutorial on
thematic analysis that teaches coding transcripts after collection and never frames naming a method as
something a plan should do
[[37]](#ref-37). The plan also does not record a build-or-drop recommendation or a decision. unitQ's
worksheet routes that step to a later synthesis stage, "Share the readout and a clear recommendation:
build, iterate, keep exploring, or drop. Log the decision and rationale where your team will find it."
[[34]](#ref-34), which is a report's job and a decision document's job, not this one.

### Related Documents (full only)

Links to the session guide, the screener, the consent form, the prototype, and earlier reports.

Nielsen Norman Group's own minimum names "Relevant documents such as consent form, screener, study
protocol" [[7]](#ref-7), and spells out what that can include: "consent forms, recruitment documentation,
and facilitator guides" [[7]](#ref-7). digital.gov's heading is "Important links", asking a team to "Keep
a running list of links to key research documents, including shared folders or assets." [[3]](#ref-3). dscout:
"Part 7: Resources/Links to Documentation" [[11]](#ref-11).

**The session script is excluded from this plan at every size, and the exclusion is this library's own
position.** Of the sources that take a position on where the script lives, most put it inside the plan
rather than linking it: dscout's "Part 5: Interview Guide" [[11]](#ref-11), 18F's "Opening script (EDIT
BASED ON PROJECT)" [[1]](#ref-1), Maze's session brief, prepared as its own step [[10]](#ref-10), and User
Interviews, which places "a moderator guide for interviews" inside the methodology section [[9]](#ref-9).
Two sources link out instead: Dovetail instructs a team to "Link out to supporting material like
discussion guides and screeners rather than embedding them." [[8]](#ref-8), and Nielsen Norman Group does
both, carrying facilitator guides among its relevant documents [[7]](#ref-7) while also listing interview
questions inside its method section [[7]](#ref-7). Counting the sources that address this, five embed the
script and two link it, with Nielsen Norman Group doing both. This library links the script rather than
holding it, because the interview guide is a separate, unbuilt candidate in this family's own catalog,
covered in section 8.

## 4. Variants and sizing

**Lean holds the seven sections marked lean above.** It is this bundle's default. Six of the seven match
User Interviews' six-item minimum in substance; the seventh, Tasks and Measures, carries the usability
block the alias "usability test plan" promises a reader it will carry, filled in only for a usability
test.

**Full holds all eleven sections, in the order section 3 states.** It adds What We Already Know, Roles
and Observers, Consent, Privacy and Ethics, and Related Documents. Its length sits near digital.gov's
eleven sections and 18F's ten headings, without copying either one's exact wording.

**The split itself is this library's own construction, not a documented pair.** Section 2 already states
why: no source names a short and a long form of the same plan. What tips the balance toward shipping two
sizes rather than one is that every full-only section in this plan has its own named source, so the full
variant is sourced content, not an invented one.

**Length is a named concern on the vendor side of the research, independent of which size a team
picks.** Dovetail: "One to two pages. A plan is a working agreement, not a thesis-if stakeholders can't
read it in five minutes, they won't." [[8]](#ref-8). Nielsen Norman Group's usability checklist: a test
plan "doesn't need to be lengthy" [[12]](#ref-12). MeasuringU warns against the opposite outcome: "Test
plans, like many documents, can take on a life of their own and become bloated and unnecessarily
complex." [[13]](#ref-13).

**How to choose.** Lean already carries the usability block, so a small usability test does not by itself
call for full; that is the point of placing Tasks and Measures in both sizes. What tips a study to full is
the four full-only sections: a study that needs prior research and assumptions summarized, several
stakeholders briefed as roles and observers, consent and data handling documented in full, or related
documents linked out in their own section.

## 5. Methodology lineage

This document type is not claimed by one named software-delivery framework; nothing in this research
looked at which such frameworks favor or originate it, and no claim is made about any of them here. What
this research did find are three sectors that each publish their own version of the same document.

**Government digital services** publish the long form [[1]](#ref-1) [[2]](#ref-2) [[3]](#ref-3)
[[4]](#ref-4), and treat it as a step a team is expected to take before fieldwork, not an optional
artifact. Section 2 covers this lineage and its one live trap: none of these is a regulatory form, and
Defra's own mandate binds only Defra's own researchers [[22]](#ref-22).

**UX research vendors and independent practitioners** publish the short form and its stated minimum, and
treat the document as a working agreement a team writes for itself, scaled to the study.

**Academic teaching** treats the usability test plan as a course deliverable. A University of Washington
page frames a template as something that "walks students through the process of planning a study through
a series of questions and planning materials" [[15]](#ref-15), though its own template and materials were
not reached from this research and are not cited here beyond that framing. Michigan Tech's course
assignment treats "the usability test plan and usability report" as the two documents a usability-testing
course concentrates on [[17]](#ref-17).

**No sector argues to reject the document outright.** The live argument is over how light a plan can be,
not whether to write one. Section 6 covers that debate in full.

## 6. Debates and contested boundaries

None of these questions is settled by the sources read for this bundle. Each is named here with its
camps, because flattening a live disagreement into a false convention is the dominant way this kind of
document goes wrong.

**1. Whether the session script belongs inside the plan or linked from it.** Five of the sources read
embed it, and Nielsen Norman Group both embeds and links at once; two sources link it out. Section 3's
Related Documents subsection carries the count and the library's own position on which side this bundle
takes.

**2. What the word brief means.** It carries four different senses across this research, and none is a
synonym for the research plan itself. Dovetail uses it for the stakeholder's request: "A brief is the
request-what a stakeholder wants to learn and why it matters to them." [[8]](#ref-8). Maze uses it for
the session guide: "The next component of a research plan is to create a brief or guide for your
research sessions." [[10]](#ref-10). Anderson uses it for the study's whole document: "A link to the
intake document or research brief, which has all the relevant information for the study, including
script, deliverables, and a report." [[26]](#ref-26). Koji uses it as an analogy rather than a name:
"Think of a research plan as a project brief for research." [[33]](#ref-33). A reader who writes research
brief meaning this document has picked a word that already means something else to at least one other
source.

**3. Whether to write a plan at all, and how light it can be.** Paul Boag argues a team should scope
down rather than write a full one: "it is better to conduct user research only when there is a specific
question that needs answering" [[25]](#ref-25), while hedging his own recommendation: "The results you
get back will be far from perfect and could possibly lead to false conclusions." [[25]](#ref-25). Teresa
Torres argues from a continuous-discovery stance that project-based research, plan and all, "it's not
sufficient for teams who continuously ship value to customers" [[23]](#ref-23) who "engage with customers
at least weekly" [[23]](#ref-23). Against them, Defra makes a plan mandatory for its own researchers
[[22]](#ref-22), and User Interviews allows a plan to be brief but never absent: "It still needs a plan,
but it can be a brief one." [[9]](#ref-9). The dispute is over how light a plan can be, not over whether planning matters at
all.

**4. One study per plan, or several.** Nielsen Norman Group states the common case and its own exception
in the same breath: "Typically, a research plan is constructed for each study." and "sometimes, a
research plan could include numerous studies or phases of research", naming "interviews and a diary
study" as an example pairing [[7]](#ref-7). 18F's guide instead multiplies plans by audience: "You may
need multiple research plans to account for the variety of ways people may experience or navigate your
design." [[2]](#ref-2). GOV.UK runs a third pattern, a round planned under a standing service-level plan
[[4]](#ref-4), which this family's contract excludes as a standing document rather than a per-study one.

**5. Participant numbers.** Covered fully in section 3's Participants and Recruiting subsection. No
single figure is a standard across the sources read.

**6. Time scheduled for analysis.** Covered fully in section 3's Schedule and Logistics subsection.
digital.gov and GOV.UK give different ratios, and they may not measure the same thing.

**7. Whether to recruit for a demographic mix.** AnswerLab argues for a default mix across every study
[[28]](#ref-28); DHS argues against worrying about it for a usability test specifically [[6]](#ref-6).
No source this research read reconciles the two.

**8. Whether and how the plan changes once the study runs.** Nielsen Norman Group: "Update the plan after
the research study is over." and, separately, "In moderated studies, it's common to make adjustments
during the study to get better data." [[7]](#ref-7). Digital NSW: "Regularly review and update your
research plan as the project progresses." [[5]](#ref-5). Maze frames the document itself as changeable
mid-study: "Seeing the UX research plan as a living document makes it much easier to edit based on team
comments." [[10]](#ref-10). dscout reports the opposite in practice: "It's not always used extensively
after the project has started." [[11]](#ref-11). This family's own contract fixes the finish
line at the report, as its position; NN/g's after-the-study update fits inside that line only if the
update is made before the report, not after it.

**9. Whether a usability test is an experiment.** Itamar Gilad draws the line this family's contract
relies on: "Per this definition an A/B test is an experiment, but a usability test is not."
[[19]](#ref-19). Gilad's own next sentence must travel with that line whenever it is cited: "I realize
that this is not the common definition used in the industry - in many cases the words test and experiment
are used interchangeably. I chose this definition because it’s closer to how scientists think of
experiments." [[19]](#ref-19). The boundary this family draws from Gilad's line is this library's own
position, built on a definition its own author calls uncommon.

**10. Who writes the plan.** dscout's researcher writes it, then shares the draft "with the product team
to ensure you're interpreting their aims correctly." [[11]](#ref-11). Defra names user researchers
specifically [[22]](#ref-22). Torres instead gives discovery work to the product trio, a product
manager, a designer, and an engineer, together: "The product trio should interview customers together."
[[23]](#ref-23). No source read for this research names a product manager alone as a plan's author. This
library's choice to let either role write it is its own, not a sourced convention.

**11. Who agrees the plan before fieldwork starts.** Defra's sequence runs from a scoping workshop to
"Capture the agreed scope in the research plan template and make sure the approach represents all
users." [[22]](#ref-22), then "Submit the research plan to your lead user researcher (if your delivery
group has one) for review or approval." [[22]](#ref-22), then "Share the approved plan with your team so
everyone is aligned." [[22]](#ref-22). Koji: "Get sign-off on the research questions from the stakeholders
who will act on findings." [[33]](#ref-33). Dovetail names agreement the same way, as something a plan
should carry in writing: "One or two decisions this research will inform-written down, agreed with
stakeholders" [[8]](#ref-8). The retired usability.gov template documents sign-off inside the plan
itself: tasks' "acceptance is to be documented prior to usability test." [[18]](#ref-18). No source read
names an approval authority outside government and two vendors' guidance, so this stays practice this
research found rather than a universal step.

**12. Whether the usability-test-plan identity is received vocabulary.** Covered fully in section 1 and
section 3's Tasks and Measures subsection. One publisher states the identity in a sentence; three more
give it structural support without naming it.

## 7. Anti-patterns and failure modes

**Treating "test plan" as this document's own name, unqualified.** This document and `test-plan`, a
separate bundle in this library, share the words "test plan." NN/g's usability checklist itself uses the
phrase for this document: "document your approach in a test plan and share it" [[12]](#ref-12), and the
retired usability.gov template opens, "This document describes a test plan for conducting a usability
test" [[18]](#ref-18). `test-plan` verifies a product increment against a specification; this document
studies how people use a product. Fix: name the document fully as a usability test plan, or as the
research plan it is, and never as a bare "test plan."

**Calling a usability test an experiment.** Section 6, item 9 covers the sourcing. Fix: reserve
"experiment" for a study that allocates participants between variants and applies a decision rule, and
call a usability test a test, as Gilad's own definition does [[19]](#ref-19).

**Writing a recommendation or a build-or-drop decision into the plan.** Section 3's What Happens to the
Findings subsection names unitQ's recommendation step [[34]](#ref-34) as a later stage's job. Fix: let the
plan name which decision the findings will inform, and leave the recommendation itself to the report.

**Carrying a programme budget, a reserve, or a standing retention policy as though it were this study's
own figure.** CleverX frames a reserve as a programme-level cushion: "Research programs always encounter
urgent or reactive studies that were not planned." [[32]](#ref-32), which is a programme's concern, not
one study's line item. A fixed retention period, like Westminster's twelve and thirty-six months
[[36]](#ref-36), belongs to an organization's standing policy. Fix: this plan names how participants are
thanked or paid for this study, and points to the organization's retention policy rather than restating
one program's figures as its own.

**Repeating a participant count, an analysis-to-fieldwork ratio, or an aggregation threshold as a
standard.** Section 3 and section 6 name the contested figures. Fix: state the range with its sources, as
this companion does, and let the plan's own author pick a number for the study at hand rather than
quoting someone else's figure as a rule.

**Using the words research brief as though they meant this document.** Section 6, item 2 names the
word's four senses. Fix: say plainly which study informs which decision, and leave brief for whichever
of the four senses the team already uses it for.

**Presenting the usability block as an optional extra for a usability test.** For a usability test, the
tasks and measures are the heart of the plan, not a supplement to it. Nielsen Norman Group's and
MeasuringU's own section lists put "Tasks" and "Task Metrics" among their named items, not an appendix
[[12]](#ref-12) [[13]](#ref-13). Fix: for a usability test, fill Tasks and Measures before most of the
rest of the plan, not after.

**Citing the two retired government sources without their dates.** 18F's guide carries "Archived as of
January 20, 2025" [[2]](#ref-2); the usability.gov template was read through a Wayback Machine snapshot of
2024-02-21 [[18]](#ref-18). Fix: name the date whenever either is cited, so a reader knows the source is a
snapshot of a retired page, not a current one.

## 8. Relationships to other artifacts

**The other family member, the not-yet-built `user-research-report`.** Per the family's contract, the
plan states the questions before the study runs; the report answers the same questions after the study
ends, and links back to the plan. MeasuringU's own plan carries the seam between them: "If possible, try
to outline how the report will be structured in the test plan." [[13]](#ref-13).

**The experiment pair (`experimentation-docs`).** Section 6, item 9 covers Gilad's line and its qualifier
in full [[19]](#ref-19). This family's contract holds, as its own position, that a study which allocates
participants between variants and applies a decision rule is an experiment, whatever it is called. A
usability test, run under this plan, assigns no participant to a variant and applies no decision rule
against a baseline.

**The QA pair, `test-plan` and `test-summary-report` (`qa-docs`).** Section 7 names the shared-words
anti-pattern directly. A QA test plan verifies a product increment against an agreed specification and
grades it. This document studies how people use a product and records observations, not a verdict against
a specification.

**The documents that use the findings (`discovery-docs`).** The family's own contract states the boundary
directly: "The persona, the problem statement and the design brief take the findings and frame or
decide." (`docs/internal/contracts/research-docs.md`, section 1). This plan plans a study; it frames no
problem and chooses no concept.

**`project-brief`.** Digital NSW places the research plan "After you have been given an initial project
brief, but before you commence any official research activities." [[5]](#ref-5). A project brief asks for
authority to start; this plan sets out one study inside the authority the project brief already granted.

**`spike-report` (`decision-docs`).** A spike tests technical feasibility, a different question from
whether and how people use a product. That bundle's own guide already routes a case where "the
exploration was user research rather than technical feasibility" to a pm-skills skill, not to itself
(`templates/spike-report/spike-report_guide.md:112`).

**Unbuilt candidates in this family's own catalog.** The interview guide and the survey instrument are
used during a study rather than planning or reporting on one, so neither is admitted to this family yet.
A diary study plan is a method-specific sibling this plan's structure could extend, if a later sweep finds
it distinct enough to stand on its own. This plan links to an interview guide where one exists, under
Related Documents, rather than holding the script itself, per section 3.

**Standing documents this family excludes by name.** A service-wide research plan, like the one GOV.UK's
round page presupposes [[4]](#ref-4), is maintained over time rather than written for one study. A
research roadmap or backlog is the same kind of standing artifact from a different angle: Anderson's own
roadmap tracks "the project's name, those involved, and the approximate study dates" across many studies
at once [[26]](#ref-26), which this one study's plan does not do.
GOV.UK's Design System aggregates findings across services on its own threshold, "we will usually
investigate something if we hear similar findings from 4 or more different services" [[20]](#ref-20),
which is likewise a standing instrument, not a single study's plan.

**A retrospective on how a study was run** belongs to a different family (`process-docs`), which looks
back at how a team worked rather than planning or reporting what a study found.

## 9. Adaptations

**A usability test on a shipped product.** Section 3's Tasks and Measures subsection carries the content
this adaptation needs: tasks written as scenarios, a success criterion per task, and measures set before
sessions run.

**A continuous-discovery team on a weekly interview cadence.** Section 6, item 3 names the argument for a
lighter plan. A team already meeting customers weekly, in Torres's sense [[23]](#ref-23), may write no
separate plan per interview; this is a when-not-to-use case that belongs in the guide, not a reason to
drop any section from the template itself.

**A study with access or inclusion needs.** Section 3's Participants and Recruiting subsection, and
section 6 item 7, name both views on demographic recruiting. GOV.UK's consent page adds a legal dimension
when the participant is a child or a vulnerable adult, requiring consent "both from the participant and
from a parent, guardian, carer or other responsible adult" [[21]](#ref-21).

**A government or other regulated team.** Defra's own sequence, scoping workshop to approval to sharing
[[22]](#ref-22), is a heavier version of the same plan this bundle ships, not a different document. A team
in that setting can treat Roles and Observers and Consent, Privacy and Ethics as mandatory rather than
optional; where a named approver belongs is a build-time choice this family leaves open, covered in the
guide.

**A study of a product customers already use.** Section 3's Why This Study subsection carries the
shipped-product reasoning this family's contract requires. The plan still declares a discovery study, by
this library's own position, when it asks where people lose time or need help with something they
already have, rather than grading that thing against a specification.

## 10. Worked example

[`user-research-plan_example.md`](user-research-plan_example.md) is a full-variant plan for the 2026-05
Reporting friction study at Acme Analytics, written by Priya Nair, PM, Reporting, and dated 2026-04-20.
Acme's UX Research function runs the sessions: one-to-one interviews of about an hour, each with a
walkthrough of the analyst's own dashboard, running from 2026-05-04 to 2026-05-15 with twelve analysts.
Because a walkthrough of a participant's own work is not a usability test, the example marks Tasks and
Measures not applicable: one line naming the method, with the task table and the measure lines marked N/A.
That is the arrangement section 3 describes for any study that is not a usability test. The study it plans is the same one four other shipped examples in this library cite
as a document that exists; this plan's own readout follows in the not-yet-built `user-research-report`'s
worked example.

---

## References

The stored copies behind these citations carry fetch stamps of 2026-10-23 for seventeen of the thirty-seven
sources and 2026-10-24 for the other twenty; the research log does not say which source carries which
stamp, so every entry below is dated 2026-10-24, the day this research closed. Every source was checked
against its own stored text rather than a search summary or a retrieval tool's summary, except
[[15]](#ref-15), which this research read only as an abstract; its own template and materials were not
reached.

<a id="ref-1"></a>[1] 18F. "[Draft Web Design Standards Research Plan](https://raw.githubusercontent.com/18F/web-design-standards-ux/master/Background%20and%20Process/research-plan-template.md)." web-design-standards-ux repository (accessed 2026-10-24). Supports the full verbatim section-by-section structure of a blank fillable research plan, the day-of-testing consent and PII language, the opening script, and the observer name field ("* NAME (Lead moderator)"). [practitioner]

<a id="ref-2"></a>[2] 18F. "[Writing a research plan](https://guides.18f.org/ux-guide/research/plan/)." UX Guide, Research > Plan (accessed 2026-10-24). Supports the nine-item section list, the archived-as-of-2025-01-20 banner, the goal-verb guidance, the roster-destruction instruction, and the multiple-plans-per-audience statement ("A research plan (sometimes also called a research protocol), describes the design of your research."). [practitioner]

<a id="ref-3"></a>[3] Digital.gov (GSA). "[How to write a research plan](https://digital.gov/resources/how-write-research-plan)." digital.gov (accessed 2026-10-24). Supports the eleven-section numbered model as stored, the roles table, the sample timeline, and the twice-as-long analysis estimate ("a safe estimate is twice as long as you give to data collection"). [practitioner]

<a id="ref-4"></a>[4] GOV.UK Service Manual. "[Plan a round of user research](https://www.gov.uk/service-manual/user-research/plan-round-of-user-research)." User research community (accessed 2026-10-24). Supports the nine-step round-planning list, the standing-service-plan prerequisite, access needs and budget in recruiting, the loosened observer-role language, and the analysis-to-research hour ratio. [standards]

<a id="ref-5"></a>[5] Digital NSW (Department of Customer Service). "[Research plan](https://www.digital.nsw.gov.au/delivery/digital-service-toolkit/activities-and-templates/research-plan)." Digital Service Toolkit (accessed 2026-10-24). Supports the before-research-starts timing, the project-brief boundary, and the regular-review practice ("After you have been given an initial project brief, but before you commence any official research activities."). [practitioner]

<a id="ref-6"></a>[6] U.S. Department of Homeland Security. "[DHS Usability Testing Kit](https://dhs.gov/cx/dhs-usability-testing-kit)." dhs.gov/cx (accessed 2026-10-24). Supports the four usability-testing approaches, moderator and note-taker roles, the minimum-four-participants guidance, the against-demographic-worry line, and the maybe-no-formal-report caveat. [practitioner]

<a id="ref-7"></a>[7] Maria Rosala (Nielsen Norman Group). "[Research Plans: Organize, Document, Inform](https://www.nngroup.com/articles/pm-research-plan/)." Nielsen Norman Group (accessed 2026-10-24). Supports the four-item minimum, the plan-vs-interview-guide distinction, sharing with stakeholders, the typically-one-study line with its own "sometimes" qualifier, and the usability-test-plan identity statement. [practitioner]

<a id="ref-8"></a>[8] Dovetail. "[UX research plan template](https://dovetail.com/ux-research-plan-template/)." Dovetail (accessed 2026-10-24). Supports the seven-section list, the one-to-two-page length, the research-question-versus-interview-question distinction, and the brief-versus-plan distinction ("A brief is the request-what a stakeholder wants to learn and why it matters to them."). [vendor]

<a id="ref-9"></a>[9] User Interviews. "[How to Create a User Research Plan](https://www.userinterviews.com/ux-research-field-guide-chapter/create-user-research-plan)." UX Research Field Guide (accessed 2026-10-24). Supports the six-item minimum, the seven-step authoring process, and the still-needs-a-plan-but-brief line. [vendor]

<a id="ref-10"></a>[10] Maze. "[Essential Elements to Create a UX Research Plan](https://maze.co/guides/ux-research/plan/)." Maze (accessed 2026-10-24). Supports the eight-step section list, the plan-versus-strategy distinction, the brief-as-session-guide usage, and the living-document framing. [vendor]

<a id="ref-11"></a>[11] Nikki Anderson-Stanier (dscout). "[How to Write a User Research Plan That Sets Your Project Up for Success](https://dscout.com/people-nerds/how-to-write-a-user-research-plan-that-sets-your-project-up-for-success)." dscout People Nerds (accessed 2026-10-24). Supports the seven-part list that holds the interview guide inside the plan, who drafts and reviews it, and the goal-switching-prevention framing. [practitioner]

<a id="ref-12"></a>[12] Nielsen Norman Group. "[Checklist for Planning Usability Studies](https://www.nngroup.com/articles/usability-test-checklist/)." Nielsen Norman Group (accessed 2026-10-24). Supports exploratory-versus-specific task framing, pilot-study guidance, the four named metrics, participant-count ranges, and the test-plan-and-share instruction. [practitioner]

<a id="ref-13"></a>[13] Jeff Sauro (MeasuringU). "[What Goes into a Usability Test Plan?](https://measuringu.com/usability-test-plan/)" MeasuringU (accessed 2026-10-24). Supports task-scenario wording, task- and session-level measures, the pilot-dated timeline, the mixed moderated-and-unmoderated practice, and the bloat warning. [practitioner]

<a id="ref-14"></a>[14] Maze. "[The 10-step checklist to create a usability testing plan](https://maze.co/guides/usability-testing/plan/)." A Beginner's Guide to Usability Testing (accessed 2026-10-24). Supports task types, time-on-task and error-rate definitions, the pilot-participant caution, and participant-count guidance for qualitative and quantitative studies. [vendor]

<a id="ref-15"></a>[15] University of Washington UX Pedagogy. "[Usability Testing Template](https://sites.uw.edu/uxpedagogy/learn-teach/usability-testing-template)." UW UX Pedagogy (accessed 2026-10-24). Supports the existence of a teaching template that walks students through planning a study; its own materials were not reached from this research. [academic]

<a id="ref-16"></a>[16] Saul Greenberg. "[Usability Testing - Developing a Test Plan](https://grouplab.cpsc.ucalgary.ca/saul/681/1997/jas/plan.html)." CPSC 681 course page, University of Calgary GroupLab (1997; accessed 2026-10-24). Supports the formative-versus-summative test-goal decision and the task-list framing, dated to a 1997 course page. [academic]

<a id="ref-17"></a>[17] Robert Pastel. "[Project Evaluation and Usability Test Assignment 3 - Test Plan](https://cs4760.csl.mtu.edu/2020/eval-usability-test-assignment-3-test-plan/)." Michigan Tech CS4760/HU4628/CS5760 (2020; accessed 2026-10-24). Supports pilot testing before the actual sessions and the plan's place among the course's own usability-test documents. [academic]

<a id="ref-18"></a>[18] Usability.gov (U.S. GSA/Digital.gov). "[Usability Test Plan Template](http://web.archive.org/web/20240221184353/https://www.usability.gov/how-to-and-tools/resources/templates/usability-test-plan-template.html)." retired template, read via Wayback Machine snapshot dated 2024-02-21 (accessed 2026-10-24). Supports the task-acceptance, completion-rate, and error-free-rate wording and the three scheduled questionnaire points. [practitioner]

<a id="ref-19"></a>[19] Itamar Gilad. "[Idea Validation Using the AFTER model](https://itamargilad.com/idea-validation-much-more-than-just-a-b-experiments/)." itamargilad.com (accessed 2026-10-24). Supports the test-versus-experiment distinction, quoted with its own qualifier that the definition is not the common industry usage. [practitioner]

<a id="ref-20"></a>[20] GOV.UK Design System community team. "[Share findings about your users](https://design-system.service.gov.uk/community/share-research-findings/)." GOV.UK Design System (accessed 2026-10-24). Supports findings taken from services at any stage including after going live, and the four-or-more-services aggregation threshold. [standards]

<a id="ref-21"></a>[21] GOV.UK Service Manual. "[Getting informed consent for user research](https://www.gov.uk/service-manual/user-research/getting-users-consent-for-research)." User research community (accessed 2026-10-24). Supports the informed-consent requirement, what participants must be told, and the added consent requirement for children and vulnerable adults. [standards]

<a id="ref-22"></a>[22] Defra Digital Service Manual. "[Research scoping and planning](https://digital.defra.gov.uk/user-research/scoping-research)." Defra (accessed 2026-10-24). Supports the mandatory-plan rule, the scoping-workshop-to-approval-to-sharing sequence, and the lead-researcher review step. [standards]

<a id="ref-23"></a>[23] Teresa Torres (Product Talk). "[Product Discovery Basics: Everything You Need to Know](https://www.producttalk.org/2021/09/continuous-discovery/)." Product Talk (2021; accessed 2026-10-24). Supports the product-trio framing of discovery work and the case against project-based research for continuously shipping teams. [practitioner]

<a id="ref-24"></a>[24] Teresa Torres (Product Talk). "[Evaluative Research](https://www.producttalk.org/glossary-discovery-evaluative-research/)." Discovery Glossary (accessed 2026-10-24). Supports the generative-versus-evaluative distinction. [practitioner]

<a id="ref-25"></a>[25] Paul Boag. "[A Pragmatist's Guide To Lean User Research](https://mobile.smashingmagazine.com/2023/03/pragmatists-guide-lean-user-research)." Smashing Magazine (2023; accessed 2026-10-24). Supports the argument for scoping research down to a specific question, with its own hedge about the risk of doing so. [practitioner]

<a id="ref-26"></a>[26] Nikki Anderson (The User Research Strategist). "[Research Roadmaps: A Tactic for Greater Org-Wide Alignment](https://dscout.com/people-nerds/research-roadmap)." dscout People Nerds (accessed 2026-10-24). Supports the research roadmap as a standing, cross-study artifact distinct from one study's plan, and "brief" used for a study's whole intake document. [practitioner]

<a id="ref-27"></a>[27] Anna Lee. "[The best way to get your UX Research project started](https://askwhy.substack.com/p/the-best-way-to-get-your-ux-research?s=w)." Askwhy (accessed 2026-10-24). Supports a hypothesis section as a plan element and sorting stakeholders into those involved versus those merely informed. [practitioner]

<a id="ref-28"></a>[28] AnswerLab. "[Inclusive UX Recruiting: How to Get a Diverse Mix of Participants for Every UX Research Study](https://www.answerlab.com/insights/inclusive-ux-recruiting-how-to-get-a-diverse-mix-of-participants-for-every-ux-research-study)." AnswerLab (accessed 2026-10-24). Supports asking about accommodations and recruiting a demographic mix by default. [practitioner]

<a id="ref-29"></a>[29] Shannon L. Coleman. "[The Difference Between a Finding and a Decision](https://byshannoncoleman.substack.com/p/the-difference-between-a-finding)." Ground Truth (accessed 2026-10-24). Supports naming the decision a study informs before specifying a research question, and stating what the study cannot answer. [practitioner]

<a id="ref-30"></a>[30] Kara Pernice (Nielsen Norman Group). "[How and Why to Recruit Backup Participants in User Research](https://www.nngroup.com/articles/recruit-backup-users-in-research/)." Nielsen Norman Group (accessed 2026-10-24). Supports intentional overrecruiting as a planned response to no-shows and cancellations. [practitioner]

<a id="ref-31"></a>[31] Kim Flaherty (Nielsen Norman Group). "[Always Pilot Test User Research Studies](https://www.nngroup.com/videos/pilot-test/)." Nielsen Norman Group video (accessed 2026-10-24). Supports a pilot session as recommended practice before the main fieldwork runs. [practitioner]

<a id="ref-32"></a>[32] CleverX Team. "[Research budget template for product and UX teams](https://cleverx.com/blog/research-budget-template-product-ux-teams)." CleverX Blog (accessed 2026-10-24). Supports a programme-level budget reserve as distinct from one study's own costing. [vendor]

<a id="ref-33"></a>[33] Koji Docs. "[UX Research Plan Template: How to Structure Any Research Project](https://www.koji.so/docs/ux-research-plan-template)." Koji (accessed 2026-10-24). Supports stakeholder sign-off before fieldwork, naming the downstream decision, and the project-brief analogy. [vendor]

<a id="ref-34"></a>[34] unitQ Research Hub. "[Research planning worksheet](https://www.unitq.com/research/templates/research-planning-worksheet.docx)." Feature Validation Research Kit (accessed 2026-10-24). Supports naming the decision a study informs, a falsifiable hypothesis form, success criteria set in advance, a risks table, and a post-fieldwork recommendation step. [practitioner]

<a id="ref-35"></a>[35] Great Question. "[Data Governance for UX Research](https://cms.greatquestion.co/features/data-governance)." product feature page (accessed 2026-10-24). Supports data retention and deletion as a controllable, policy-tied feature rather than a single study's own figure. [vendor]

<a id="ref-36"></a>[36] University of Westminster. "[Website user experience testing and research privacy statement](https://westminster.ac.uk/about-us/our-university/corporate-information/information-compliance-records-management-and-information-security/personal-data-protection/website-user-experience-testing-and-research-privacy-statement)." University of Westminster (accessed 2026-10-24). Supports a concrete, stated retention period for recordings and notes from one research program. [primary]

<a id="ref-37"></a>[37] CleverX Team. "[Qualitative coding: a thematic analysis tutorial](https://cleverx.com/blog/qualitative-coding-thematic-analysis-tutorial-for-user-research/)." CleverX Blog (accessed 2026-10-24). Supports a null result: the article teaches post-collection coding and never frames stating an analysis method as something a plan should do. [vendor]
