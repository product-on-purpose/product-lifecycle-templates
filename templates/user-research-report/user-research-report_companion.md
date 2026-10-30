# Companion: The User Research Report

> The deep explainer for the user-research-report bundle. Read this to understand what the document
> is, where its sections come from, and where the sources genuinely disagree. The short operator card
> is [`user-research-report_guide.md`](user-research-report_guide.md); a fully worked instance is
> [`user-research-report_example.md`](user-research-report_example.md). Inline citations like
> [[10]](#ref-10) resolve to the [References](#references) at the bottom, tagged by source
> reliability.

---

## 1. Orientation

A user research report records what one study of the people a product serves found, and what it
recommends, after the study ends. It answers the questions a plan set before the sessions ran. Two
vendors converge on nearly the same sentence for what the document is. User Interviews: "A research
report is a document that summarizes all the details of a research study, including the research
questions, methodology, notable insights, and recommended next steps." [[14]](#ref-14). Maze: "A user
research report is an easy-to-digest summary of a user research project that aims to update product
stakeholders on results, inform product decisions with user data, and harmoniously guide a product
build or iteration." [[13]](#ref-13). Dovetail separates the report from its smallest unit: "A report
packages several insights into a narrative for a specific audience, with method, context, and
recommendations." [[10]](#ref-10). NIST's own format is "a standard method for reporting usability
test findings" [[2]](#ref-2).

For a usability test, the report also carries the tasks' results against the measures the plan set.
That block is conditional: any other method writes one line saying so.

**At a glance**

- It is written **after** the study, and it reports on **one** study. User Interviews names "a
  research study" [[14]](#ref-14); Dovetail builds every depth "from the same project-same findings,
  same citations, different depth" [[10]](#ref-10).
- **This bundle ships two depths, not three, at medium confidence.** This is where the report
  differs from the plan: no source in this research names a short and a long form of one plan, but
  several vendors name a short and a long form of one report. Section 4 covers this in full.
- **The answer comes first.** Dovetail: "Put the headline finding in the first three
  sentences-don't make readers excavate it" [[10]](#ref-10). Maze: "Lead with a short summary of key
  findings and recommendations, then add the context people need-such as why you conducted the study
  and the methods you used." [[13]](#ref-13).
- **Every finding carries a count and evidence a reader can check.** Dovetail: "Every claim cites a
  quote, a clip, or a number a reader can check" [[10]](#ref-10).
- **It recommends, and it does not decide.** A finding may say what costs people time; it does not
  frame that as the chosen problem, and it does not name the concept a team will build. The sources
  themselves pull toward recording the decision too; section 6 names that disagreement in full.
- **No source in this research measured whether writing a report changes a study's outcome, or a
  product's.** The sources that argue most reports go unread are practitioner testimony about their
  own reports, not a count across many teams. Section 6 covers this claim and its limits.

## 2. Origins and evolution

**Government and standards bodies publish the long, formal lineage.** The American National Standards
Institute "approved the CIF December 12, 2001 as the standard for reporting usability test results"
[[2]](#ref-2), and NIST's own page on it names the purpose: "to encourage incorporation of usability
as an element in decision making for software procurement" [[2]](#ref-2). The page itself carries a
retirement notice: "This page is no longer being updated and the information may be out of date."
[[2]](#ref-2). NIST's own fillable report template, NISTIR 7742, dated "15-Nov-10", "Version 0.2"
[[1]](#ref-1), states its own scope directly: it is a template for "the Common Industry Format (CIF)
usability test report. This version of the CIF has been customized for use in usability testing of
Electronic Health Records (EHRs) by usability administrator(s) and data logger(s)." [[1]](#ref-1).
Every citation of this template's headings in this companion carries that customization in the same
sentence, because the headings were written for electronic health records, not for product teams in
general. DHS publishes its own kit, "Last Updated: 02/27/2025" [[3]](#ref-3). GOV.UK's Service Manual
publishes a sharing page, "Published: 24 May 2016" [[4]](#ref-4), and a separate page on data and
consent [[49]](#ref-49). Two further US sources are retired. Digital.gov's starter kit, from "May
2014" [[6]](#ref-6), was read through a Wayback Machine snapshot of 2026-04-17; its live page now
returns HTTP 404. Usability.gov's template page states its own status: "Usability.gov is archived
and no longer updated." [[8]](#ref-8), and "External links may not function and information on the
site may be out of date. Visit Digital.gov for current information." [[8]](#ref-8); it was read
through a Wayback Machine snapshot of 2024-02-21, since its live page now redirects to digital.gov.
A filled instance of the digital.gov/usability.gov kit survives from a 2013 test at Employee Express:
"Test date: July 22, 2013 Users tested: 3 Method: Formal Usability Test"
[[7]](#ref-7), read from its stored copy as extracted paragraph text after a network fetch of the
`.docx` corrupted the stored bytes.

**UX research vendors and independent practitioners publish the shorter, recommendation-forward
lineage.** Dovetail, UserTesting, Maze, and User Interviews each name a section list and treat the
document as a working deliverable a team writes for its own stakeholders, scaled by audience rather
than by regulatory requirement. Condens frames the same shape as a tool feature rather than a named
template: "Instead of a one-size-fits-all report, you can create tailored content - concise summaries
for executives who need quick takeaways, and in-depth reports for product and design teams looking
for detailed insights." [[15]](#ref-15); this research found no section list on Condens's own site, so
nothing here cites it for a structure. User Interviews' own report chapter carries a dated caveat
this companion repeats wherever its content could be mistaken for current: "Note to the reader: This
part of the field guide comes from our 2019 version of the UX Research Field Guide. Updated content
for this chapter is coming soon!" [[14]](#ref-14).

**The lineage trap this family's contract names.** This report borrows section structure from US
government templates and from the Common Industry Format: NIST's NISTIR 7742 [[1]](#ref-1), NIST's
own CIF page [[2]](#ref-2), and the retired usability.gov and digital.gov templates
[[6]](#ref-6)[[8]](#ref-8)[[9]](#ref-9). No source read for this research calls NISTIR 7742 a
regulatory format, and none says a regulator requires it. What NIST's own pages say is narrower: an
ANSI standard meant to inform procurement decisions [[2]](#ref-2), and a template customized for
testing electronic health records [[1]](#ref-1). A reader who adapts this report's full variant is
borrowing a government team's own fill-in template, not a form a regulator requires of a software
product generally.

## 3. Anatomy (section by section)

The full variant carries nine sections. The lean variant carries the six marked **lean** below, in
the same name and order. Task Results is one of those six: it sits in both sizes and is filled in
only when the study is a usability test. The remaining three sections are full-variant only.

### Summary (lean)

The answer up front: what the study found and what it recommends, in a few lines.

Dovetail's own section list opens this way: "a summary that states the answer up front, background
and objectives (two or three sentences on why the study ran), method and participants, key findings,
recommendations, and open questions." [[10]](#ref-10). NIST's template, inside the health-records
customization its own first line states [[1]](#ref-1), opens the same way: "1 EXECUTIVE SUMMARY"
[[1]](#ref-1). UserTesting's executive form carries "Key Takeaways (3-5 bullet points)"
[[11]](#ref-11), and MeasuringU's usability form opens with "Study Overview" then "Findings Summary"
[[22]](#ref-22). O'Neill names the device directly: "The other is a TLDR." [[46]](#ref-46).

**One team's account names the executive summary as the hardest part to write, and the part that
decides whether the rest gets attention.** Mozilla's own account of its Firefox user research
team: "An executive summary is a few sentences, maybe one slide (if it’s in slide format) that
summarizes a research study." [[51]](#ref-51), and "I’ll tell you - it is the hardest part of a
research study." [[51]](#ref-51). A Firefox VP of Product is quoted on the stakes: "In short, without
a good executive summary, the document will likely not get the attention it deserves." [[51]](#ref-51).
The same team's own fix was to shorten it: "We try to be more succinct with our executive summaries
than before, with clear takeaways and calls to action for each report." [[51]](#ref-51).

**This section can also carry the decision the findings inform, and who makes it.** No shipped source
lists that pairing as its own heading, but several name it as content a report should give its reader
early: Dovetail's "End each finding with what the team should do about it, and who decides"
[[10]](#ref-10) and Useberry's "Lead with decisions, then show the evidence." [[37]](#ref-37) both put
the decision at or near the top of the document, not buried in a methodology section.

### Background and Objectives (full only)

Why the study ran, the decision it informs, and a link to the plan.

Dovetail's list carries "background and objectives (two or three sentences on why the study ran)"
[[10]](#ref-10). UserTesting's detailed form names "Background & Objectives" [[11]](#ref-11), and its
shorter forms carry the same idea under a different name: "Objective of the Study" [[11]](#ref-11)
and "Study Goal" [[11]](#ref-11). Dovetail's debrief, a lighter sibling document, opens the same way:
"Research objective" [[44]](#ref-44). Maze's own instruction is to keep this brief: "Your introduction
should lay out your research goals, plan, and scope." [[13]](#ref-13).

**Every short form that names an objective at all puts it near the top of the document.** That is a
tension with shipping this section full-only: a team on the lean size still needs the objective
somewhere, and this bundle's answer is that Summary carries it briefly in lean, while Background and
Objectives expands it in full with a link back to the plan.

**This is where the report says why a study of a product people already use is still discovery
work.** The family's contract requires every member to declare the discovery phase even when it
serves a study of a shipped product, and asks each companion to say why
(`docs/internal/contracts/research-docs.md`, section 2). This research found no source that calls
a study of a shipped product discovery work in those words. What distinguishes a discovery study from
an evaluative one is purpose, not product age: Maze defines "Generative research helps identify user
needs and opportunities before design begins" [[47]](#ref-47) against "Evaluative research assesses
and validates existing designs for improvements" [[47]](#ref-47), and UserTesting draws the same line:
"Generative research dives into 'What problem might we solve?' while evaluative research asks, 'How
well is our solution working?'" [[48]](#ref-48). A study that asks where people lose time with
something they already have, rather than grading that thing against a target, is still asking the
generative question. This library's own reasoning, not any one source's claim, treats that study as
discovery work.

### Research Questions and Answers (lean)

Each question the plan set, with a short answer and the findings behind it. A question the study
could not answer says so.

UserTesting's detailed form carries "Research Questions" as its own item [[11]](#ref-11). User
Interviews ties the section to the plan directly: "Actionable reports should relate back to the
initial research question: How do your findings influence the decisions you mapped out in your
research plan?" [[14]](#ref-14), and names the question's own origin: "The research questions you'd
asked as the catalyst for your study." [[14]](#ref-14). Dovetail's debrief, a lighter sibling document
rather than a full report, carries the same element: "The research questions the study aimed to
answer" [[43]](#ref-43).

**No short report form in this research carries research questions as a named item.** Only the two
detailed forms do [[11]](#ref-11)[[14]](#ref-14). That a report answers the plan's own questions is
this library's own position, drawn from this family's contract: "It answers the questions the plan
set out." (`docs/internal/contracts/research-docs.md`, section 1). A report with no written plan
behind it still fills this section from what the study set out to learn, because the sources tie a
report to a plan only where one exists.

**A question the study could not answer belongs here, not hidden.** Anderson-Stanier names the
failure mode directly: "There are questions out there that qualitative, and even quantitative,
research simply cannot answer and we need to let our teams know when a question is unanswerable."
[[27]](#ref-27). O'Neill describes closing a report the same way: "the next session needs to test
these open questions. We still don't know X, Y, and Z." [[46]](#ref-46).

### What We Did (lean)

The method, the participants and the dates, the limits of the sample, and one line on anything that
ran differently from the plan.

Dovetail's list carries "method and participants" [[10]](#ref-10). NIST's template structures the
same content under "3 METHOD" and "3.1 PARTICIPANTS" [[1]](#ref-1), each inside the health-records
customization the template itself declares [[1]](#ref-1). UserTesting's detailed form carries
"Methodology (e.g., unmoderated usability tests, surveys, etc.)" [[11]](#ref-11).

**The limits of the sample belong in this section, and three sources name them beside the method.**
Dovetail's debrief: "The method used and any important limitations" [[43]](#ref-43). Userfeel:
"Discuss any concerns you have about your methods" [[38]](#ref-38). Sauro names the specific limit of
a small sample: "the key limitation is that you are limited to detecting large differences between
designs or measures" [[24]](#ref-24).

**One line on anything that ran differently from the plan is this library's own arrangement**, the
same device `experiment-readout` already carries in its own Context and Setup section. No sentence
this research verified instructs a report to note a deviation from its own plan, and NIST's
instruction to report irregularities was read in its stored copy but never confirmed as verbatim.

**Participant counts are reported against a convention, not a rule this bundle sets.** NN/g's own
reading list names the figure this convention rests on: "Why we recommend conducting qualitative
usability testing with about 5 participants per user group" [[18]](#ref-18); the page is a curated
reading list rather than a prose guide, so it carries the convention's existence and nothing more.

**Who ran and analysed the sessions is thinly supported, and this bundle does not make it a named
field.** Sauro proposes a section "on the interviewer or principal investigator’s background and how
it might influence their conclusions" [[25]](#ref-25) as one way to disclose researcher bias. GitLab's
own practice names a role rather than a disclosure: "The Research DRI, and their UX Researcher
partner if applicable, synthesise findings, validate key takeaways, and create the report."
[[28]](#ref-28).

**Which version of the product the participants saw is an ASK here, on one vendor's word.** Koji tags
each insight at publication with "Product version / state: what the participants were actually
reacting to" [[52]](#ref-52), and says of usability findings that "a redesign invalidates them
instantly" [[52]](#ref-52). Koji writes for a research repository rather than one report, so this
bundle asks the question in What We Did and adds no field for it. A review-by date stays out.

### Key Findings (lean)

Each finding, how many participants showed it, and the evidence a reader can follow.

NN/g names the chain this section sits at the end of: "Data leads to findings, which build insights,
which justify recommendations." [[20]](#ref-20), and a second NN/g page gives the same chain its own
short definitions: "Data refers to unanalyzed user observations, findings capture patterns among data
points, and insights are the actionable opportunities based on research and business goals."
[[21]](#ref-21). Dovetail's list names "key findings" [[10]](#ref-10) directly, and names the limit:
"A one-page summary with linked evidence beats a forty-slide deck nobody opens." [[10]](#ref-10).
Maze's own list carries "Key findings" [[13]](#ref-13), and User Interviews' "Key learnings"
[[14]](#ref-14). UserTesting instructs: "Use direct quotes or clips to support findings"
[[11]](#ref-11).

**Every claim a reader can check, not an opinion with formatting.** Dovetail: "Every claim cites a
quote, a clip, or a number a reader can check" [[10]](#ref-10), and more bluntly: "A finding without
evidence is an opinion with formatting." [[10]](#ref-10). Krause names the risk in relying on a quote
alone: "Anecdotes can lead to narrative bias, so it’s best to use them to illustrate or support your
data." [[19]](#ref-19).

**State counts as fractions, with the denominator, not a bare percentage.** Sauro: "We start with the
most important findings, and then note the number of participants that supported these findings and
some good quotes to support what we concluded." [[25]](#ref-25). Sauro and Lewis argue that a small
sample is still worth reporting, if the reader can see its size: "it’s completely permissible from a
statistical perspective to report numbers when studies have very small sample sizes (fewer than ten
people)" [[23]](#ref-23), and prefer fractions over a bare percentage: "Unless this information
appears elsewhere in your report, we recommend presenting fractions." [[23]](#ref-23). Their formats
run from "5 (simple count)" [[23]](#ref-23) to "5/7 (71%) (fraction + percentage)" [[23]](#ref-23).

**Say what already works, not only what failed.** Schade: "Don’t forget to include positive findings
as well, letting the team know what’s already working." [[16]](#ref-16). Sauro: "Don’t forget the
positives" [[26]](#ref-26). Userfeel adds a sequencing note: "although it can help to start with a
positive finding even if it's less important" [[38]](#ref-38).

**Anonymise quotations, and use them only within consent.** GOV.UK: "Whenever you can, you should
fully anonymise the extracts you use so that the participants cannot be identified." [[49]](#ref-49).
CleverX's own consent language separates uses: "I consent to anonymized quotes being used in internal
reports" [[40]](#ref-40), and names a narrower bar for a specific clip: "If you want to use a specific
quote or clip, get explicit permission referencing the exact content" [[40]](#ref-40).

**A participant's own suggestion belongs here, labelled as the participant's words, not the team's
recommendation.** User Interviews: "Any specific recommendations brought up by users during interviews
or in surveys." [[14]](#ref-14). Maze adds a reminder not to discard offhand remarks: "make special
notes of 'offhand' comments users make. Often, it's the random comments that provide the most
insight-they must not be forgotten about when writing the report." [[13]](#ref-13).

### Task Results (lean, usability tests only)

Each task's completion, errors and time, and the questionnaire scores the plan named. Any other
method writes one line saying so.

This block's content is well evidenced, and all three lists that carry it are usability formats; no
general report list carries it. NIST's template, inside its own health-records customization
[[1]](#ref-1), structures this content under "3.9 USABILITY METRICS" and "4 RESULTS" [[1]](#ref-1),
and defines a success rate directly: "The total number of successes were calculated for each task
and then divided by the total number of times that task was attempted." [[1]](#ref-1).
usability.gov's retired template, read through a Wayback Machine snapshot of 2024-02-21, carries
"Task Completion Success Rate" [[9]](#ref-9), "Time on Task" [[9]](#ref-9), and "Errors"
[[9]](#ref-9), and defines a non-critical error: "A non-critical
error is an error that does not prevent successful completion of the scenario." [[9]](#ref-9).
MeasuringU gives "Task Metrics" [[22]](#ref-22) its own named item. UserTesting instructs a report to
"Include quantitative data where applicable (e.g., success rates, charts, QX Score visualizations)"
[[11]](#ref-11).

**Questionnaire thresholds appear in NIST's own template, and this companion cites them as NIST's
convention, not as a standard this library sets.** Inside the same health-records customization
[[1]](#ref-1): "Broadly interpreted, scores under 60 represent systems with poor usability; scores
over 80 would be considered above average." [[1]](#ref-1), and "Common convention is that average
ratings for systems judged easy to use should be 3.3 or above." [[1]](#ref-1).

**NIST's own two pages disagree on whether this section fits a qualitative test.** The template
itself: "The modifications here allow for the reporting of qualitative findings (i.e., formative) but
strongly recommend and encourage the collection of quantitative measures of user performance."
[[1]](#ref-1). NIST's separate CIF page takes a narrower view: "The CIF is designed for summative
testing rather than formative testing." [[2]](#ref-2). A small qualitative test can still report
counts as fractions [[23]](#ref-23) rather than only a summative table.

**For a quantitative usability test, a prior belief can be stated and then updated against the
data.** Sauro and Lewis work through one twenty-participant test this way, ending in a stated
confidence level rather than a bare point estimate: "A 95% credible interval runs from roughly 72% to
96%" [[50]](#ref-50). A small qualitative test instead carries its own limits, as the paragraph above
states, through the fraction and its denominator rather than a credible interval.

**A study that is not a usability test writes one line here, naming its method, and marks the task
table and the measure lines N/A.** An interview study, a diary study, or a survey has no tasks to
score.

### Recommendations (lean)

What the team should do next and why, each recommendation tied to findings. It records no decision.

Dovetail's list carries "recommendations" [[10]](#ref-10). User Interviews names "Recommendations"
[[14]](#ref-14) as its own section, and UserTesting prioritises it: "Prioritized based on impact"
[[11]](#ref-11). Maze's list closes on "Next steps" [[13]](#ref-13). usability.gov's retired template
pairs each recommendation with a rating: "Each recommendation includes a severity rating."
[[9]](#ref-9). Schade's own instruction keeps the section honest about what it is: "But present
recommendations as recommendations." [[16]](#ref-16).

**The sources pull this section toward the decision itself, and this family's contract draws the line
the other way.** Dovetail: "End each finding with what the team should do about it, and who decides"
[[10]](#ref-10). Usercall goes further: "If your report doesn't end in a decision or a debate about a
decision, you haven't written a report, you've written a diary." [[30]](#ref-30). Useberry: "Lead
with decisions, then show the evidence." [[37]](#ref-37). Against that pull, the contract states: "A
member here may recommend, but it records no decision."
(`docs/internal/contracts/research-docs.md`, section 1). This bundle follows the contract: a
recommendation names a change worth weighing, and recording the decision itself, or naming the
concept a team will build, is a later document's job.

**Where a recommendation sits, relative to its finding, is contested, and this bundle keeps the
sections separate.** Condens prefers one after each finding: "Rather than listing them all at the end,
include a recommendation after each finding throughout the report, while still including the summary
at the conclusion." [[15]](#ref-15). MeasuringU organises by task instead: "Usability Issues by Task
and Recommendations" [[22]](#ref-22). usability.gov [[9]](#ref-9), UserTesting [[11]](#ref-11), and
User Interviews [[14]](#ref-14) each put recommendations at the end, in their own section, as this
bundle does. The guide names both practices rather than picking one as correct.

### Open Questions (full only)

What the study raised and did not answer, and what research would answer it.

Dovetail's list names "open questions" [[10]](#ref-10) as its closing section. Dovetail's debrief, a
lighter sibling document, carries the same element: "Open questions for the team" [[44]](#ref-44). A
second list carrying this element argues that a lean placement is defensible, but this bundle ships it
full-only and lets lean's Research Questions and Answers section note which questions stayed open
instead.

User Interviews names the device directly: "Compelling insights that illuminate unanswered questions"
[[14]](#ref-14). O'Neill describes closing a live readout the same way: "I'm like, okay, the next
session needs to test these open questions. We still don't know X, Y, and Z." [[46]](#ref-46).
Userfeel asks for "further questions that arose from the test and how they could be investigated in
the future" [[38]](#ref-38). Anderson-Stanier names the underlying discipline: "we need to let our
teams know when a question is unanswerable" [[27]](#ref-27).

### Appendix (full only)

The session list, the materials used, and where the raw notes live.

Maze names the device plainly: "It's easy to overlook the appendix after putting together a detailed
report, but all that glorious research data needs to be accounted for and referenced clearly."
[[13]](#ref-13). UserTesting's detailed form closes on "Appendices" [[11]](#ref-11), carrying "Full
responses, session details, additional data" [[11]](#ref-11). MeasuringU's own closing item is
"Appendix & Verbatims" [[22]](#ref-22). NIST's template, inside its own health-records customization
[[1]](#ref-1), closes on six named appendices from "SAMPLE RECRUITING SCREENER" [[1]](#ref-1) to
"INCENTIVE RECEIPT AND ACKNOWLEDGMENT FORM" [[1]](#ref-1), by way of "NON-DISCLOSURE AGREEMENT AND
INFORMED CONSENT FORM" [[1]](#ref-1) and "EXAMPLE MODERATOR'S GUIDE" [[1]](#ref-1). usability.gov's
retired template leaves attachments as fields to fill: "Attachment A - Background Questionnaire,
Attachment B - Post-Task Questionnaire, Attachment C - Post-session Overall Subjective Questionnaire,
Attachment D - Task Scenarios" [[9]](#ref-9).

**Where the raw session notes live belongs here, and a fixed retention period does not.** GOV.UK:
"Keep your research data only in places that your organisation has approved for storing personal
data." [[49]](#ref-49). CleverX's own repository guidance names retention periods, but at the level of
a standing repository rather than one study's own report: "identifiable participant data (names,
emails) deleted within 12 months; transcripts and recordings retained for 24 months"
[[39]](#ref-39). This report points to the organisation's own retention policy rather than restating
one programme's figures as its own.

## 4. Variants and sizing

**Lean holds the six sections marked lean above.** It is this bundle's default. **Full holds all nine
sections, in the order section 3 states**, adding Background and Objectives, Open Questions, and
Appendix.

**Two depths of one study's findings is the better-evidenced of this family's two size calls.**
Dovetail states the two audiences directly: "Executives want one page with the decision;
your product team wants the detail behind it." [[10]](#ref-10). UserTesting names them as named
products: "Executive summary report (For Stakeholders and Leadership)" [[11]](#ref-11) and "Detailed
research report (For UX and Product teams)" [[11]](#ref-11). Condens frames the same idea as a tool
feature: "concise summaries for executives who need quick takeaways, and in-depth reports for product
and design teams looking for detailed insights." [[15]](#ref-15). DHS scales the write-up to the test
rather than naming two sizes of one document: a quick office test needs no report at all, "There's no
need to formalize your findings; just use your rough notes on usability issues to revise the
materials or start developing a prototype." [[3]](#ref-3), while a fuller test "may or may not result
in a formal report." [[3]](#ref-3).

**Two sizes, not three, at medium confidence.** UserTesting itself names a third, shortest form, a
"Quick feedback snapshot (For Agile teams)" [[11]](#ref-11), that lists four items: "Study Goal"
[[11]](#ref-11), "Key Insights (Bullet Points)" [[11]](#ref-11), "Supporting Data (Screenshots,
Videos, Metrics)" [[11]](#ref-11), and "Next Steps & Prioritized Action Items" [[11]](#ref-11). Each
of the four maps onto a lean section this bundle already ships, which is why this research treats
the snapshot as a restatement of lean rather than a third size, not as a settled fact. DHS's own
lightest level is no report at all [[3]](#ref-3), which is likewise not a third size.

**Against length.** Dovetail answers its own question on format with "As short as the decision
allows." [[10]](#ref-10). User Interviews states what a report is not: "A UX research report is not:
A lengthy, dissertation-style paper" [[14]](#ref-14), and names the same weakness in the CIF itself:
"However, this format tends to be quite lengthy, making it less-than-ideal for sharing with
stakeholders." [[14]](#ref-14). Maze names the common failure directly: common mistakes include
"focusing too much on methodology, burying the main insights" [[13]](#ref-13).

**How to choose.** A short, decision-forward readout for one audience is lean. A study that needs the
decision restated with its own background, the questions the study could not answer named in their
own section, and the raw materials pointed to in an appendix is full.

## 5. Methodology lineage

**This research found no material tying this document to a named software-delivery framework.**
Nothing in this research looked at how Scrum, SAFe, Shape Up, or a similar framework treats a research
report, and no claim is made about any of them here.

What this research did find are two sectors, not three. The academic teaching material this family's
other member cites was not re-tested here, and this report's own research found no academic source
for the report itself.

**Government and standards bodies** publish the long, formal lineage: NIST's ANSI-approved Common
Industry Format [[2]](#ref-2), its health-records-specific customization [[1]](#ref-1), DHS's own kit
[[3]](#ref-3), and GOV.UK's sharing and data pages [[4]](#ref-4)[[49]](#ref-49). Section 2 covers this
lineage and its one live trap in full: none of it is a regulatory mandate on a product team, and the
health-records customization travels with every citation of NIST's headings.

**UX research vendors and independent practitioners** publish the shorter, recommendation-forward
lineage: Dovetail, UserTesting, Maze, and User Interviews each name a section list, and treat the
document as a working deliverable scaled to its audience rather than a compliance artifact.

**This bundle's own methodology field is deliberately agnostic to any one lineage**, because the
sources it draws on span UX research vendors, government digital services, and an ISO-derived
reporting format; naming one of those lineages as the document's methodology would misdescribe the
others.

## 6. Debates and contested boundaries

None of these questions is settled by the sources read for this bundle. Each is named here with its
camps, because flattening a live disagreement into a false convention is the dominant way this kind
of document goes wrong.

**1. Whether to write a written report at all.** GOV.UK: "researchers on an agile team won't have
time to write research reports (though they might produce brief research summaries)" [[4]](#ref-4).
Humble argues further, to stop writing one altogether: "if you're bringing the team into research
activities, you don't have to make a research report ever again." [[35]](#ref-35), closing with "stop
reporting and start inspiring!" [[35]](#ref-35). Against them, User Interviews reports that "some
researchers always create them for the research repository" [[14]](#ref-14), and Usercall keeps "a
full report for the record" [[30]](#ref-30) even while arguing most reports fail. This bundle does not
claim every study ends in a written report.

**2. Whether reports go unread, and how widely.** The sources here are practitioner testimony, not a
measured rate across teams. Usercall: "Most customer research reports are built to prove that research
happened, not to actually change anything." [[30]](#ref-30). Humble: "We do that because we know the
truth… nobody reads. At best, people skim" [[35]](#ref-35). User Interviews: "many researchers
complain that stakeholders don't read them or are overwhelmed by the sheer volume of information."
[[14]](#ref-14). O'Neill: "If you write a report that people don't want to read and don't read, it
doesn't have any impact, even if it had the best possible insights in it." [[46]](#ref-46). This
companion treats these as testimony about practice, not as a measured finding this library can repeat
as fact.

**3. Where a recommendation sits, relative to its finding.** Covered fully in section 3's
Recommendations subsection. After each finding [[15]](#ref-15)[[10]](#ref-10); by task
[[22]](#ref-22); in a separate section at the end [[9]](#ref-9)[[11]](#ref-11)[[14]](#ref-14).

**4. Whether the report should end in a decision.** Covered fully in section 3's Recommendations
subsection. A decision or a debate about one [[30]](#ref-30); who decides, named beside the finding
[[10]](#ref-10); lead with decisions [[37]](#ref-37). This family's contract draws the boundary the
other way, and this bundle follows the contract.

**5. Format: written report, slide deck, or something else.** GitLab's own practice: "Though Google
Slides is the most popular format, the report can really be in any form, for example, a doc, an
issue, a board, or an diagram." [[28]](#ref-28). Maze names the tradeoff of a written report directly:
"These types of reports often come as a PDF or a Word document, making them static, reluctant to
change, and resulting in low engagement or re-reads." [[13]](#ref-13), against its own case for one:
"Written UX reports enable people to go through things in their own time-and come back to them when
they need to." [[13]](#ref-13). Whether a deck has a structure distinct from the written sections is
itself unsettled: GOV.UK's own slide list maps onto this bundle's written sections
[[4]](#ref-4), while Maze names a presenting frame that does not, "Problem: State the problem you set
out to overcome" [[13]](#ref-13), then "Agitate" [[13]](#ref-13), then "Solution: Offer a route forward
from the research findings and insights, the next steps, and likely outcomes by solving the problem"
[[13]](#ref-13). This library ships no deck format, and the guide may note that a deck can carry the
same sections this document names.

**6. Count formats.** Covered fully in section 3's Key Findings subsection. Sauro and Lewis name five
formats, from "5 (simple count)" [[23]](#ref-23) to "5/7 (71%) (fraction + percentage)"
[[23]](#ref-23), and prefer the fraction unless the denominator already appears elsewhere
[[23]](#ref-23). No other source in this research names its own preferred format.

**7. Formative and summative testing.** NIST's own two pages disagree. The template allows both:
"The modifications here allow for the reporting of qualitative findings (i.e., formative) but
strongly recommend and encourage the collection of quantitative measures of user performance."
[[1]](#ref-1). The separate CIF page narrows the scope: "The CIF is designed for summative testing
rather than formative testing." [[2]](#ref-2).

**8. How much depth the method section needs.** Maze cautions against dwelling on it: "while
methodology is important, it's the results that most people are here for." [[13]](#ref-13). User
Interviews asks only for "A brief explanation of why you chose those methods." [[14]](#ref-14). Against
brevity, User Interviews' own CIF framing names the opposite reader: "If your audience is other
researchers... then the CIF format works great" [[14]](#ref-14). This bundle treats the method section
as brief for most readers, by the weight of this count.

**9. Severity scales for usability findings.** No single scale is a standard across the sources read.
Nielsen's own scale runs five levels, from "0 = I don’t agree that this is a usability problem at
all" [[17]](#ref-17) to "4 = Usability catastrophe: imperative to fix this before product can be
released" [[17]](#ref-17), rated on frequency, impact, and persistence [[17]](#ref-17). Nielsen's own
caution travels with the scale: "My experience indicates that severity ratings from a single
evaluator are too unreliable to be trusted." [[17]](#ref-17). Sauro cuts the same idea to three
levels plus one: "we reduced our severity scale to just three levels, along with one for insights,
user suggestions or positive attributes." [[26]](#ref-26). Schade ranks findings "as low, medium or
high severity" [[16]](#ref-16) instead. This bundle names severity as a property of usability
findings, in Task Results, without picking one scale as the library's own.

**10. What the smallest unit of a finding is called, and how it is defined.** UserTesting's own tool
calls it a "nugget": "Each nugget represents a single insight, observation, or piece of data, which
can be tagged and organized for easy retrieval and combination in future analyses." [[11]](#ref-11).
Its own help centre, in a different product area, calls the same-sized unit a "story": "You can think
of stories as individual findings or insights." [[12]](#ref-12). Maze names the same word for a
different, four-part model, credited to its originators, Tomer Sharon and Daniel Pidcock, as "the
concept of breaking UX research down into its constituent parts" [[13]](#ref-13), split into four
labelled steps running from what was done to what follows next. A UX studio blog names a third
definition again: "A nugget is a labelled observation supported by evidence." [[33]](#ref-33). Three
different definitions share one word, and this bundle avoids the word nugget rather than pick among
them.

**11. Whether a usability test is an experiment.** Gilad draws the line this family's contract relies
on: "Per this definition an A/B test is an experiment, but a usability test is not."
[[29]](#ref-29). His own next sentence qualifies it, and the qualifier travels with the line whenever
it is cited: "I realize that this is not the common definition used in the industry - in many cases
the words test and experiment are used interchangeably. I chose this definition because it's closer
to how scientists think of experiments." [[29]](#ref-29). The boundary this family draws from Gilad's
line is this library's own position, built on a definition its own author calls uncommon.

**12. Who writes the report.** GitLab names the role, not the credential: "In GitLab, anyone can be
the DRI of a UX Research project. If the Research DRI is not a UX Researcher, they are partnered with
a UX Researcher acting in a supporting role." [[28]](#ref-28), and names other roles explicitly:
"Other roles, such as Product Managers and Product Designers, frequently conduct research with
guidance from the UX Research team." [[28]](#ref-28). User Interviews names the researcher alone:
"As the researcher who led the project from start to finish, you're in the best position to interpret
the data and make recommendations for how it should be used." [[14]](#ref-14). Humble, a designer,
wrote his own: "Ironically, I was a designer doing research, and my research report was completely
undesigned." [[35]](#ref-35). Mind the Product frames a toolkit for a fourth role: "Julia offers a
toolkit for those product managers who don't have a UX designer or researcher in their team, and want
to do user research themselves." [[34]](#ref-34). No source in this research gives a share across
these roles; this bundle lets either a researcher or a product person write it, without claiming a
product manager usually does.

## 7. Anti-patterns and failure modes

**Citing NIST's headings without the health-records customization in the same sentence.** NISTIR 7742
was "customized for use in usability testing of Electronic Health Records (EHRs)" [[1]](#ref-1); every
citation of its section headings in this bundle, and in any document built from it, carries that
customization alongside the heading, not in a footnote a reader can skip past.

**Calling NISTIR 7742, or the Common Industry Format it customizes, a regulatory format.** No source
read for this research supports the word. NIST names an ANSI standard meant to inform procurement
decisions [[2]](#ref-2); it names no regulator that requires it. Fix: call it a government team's own
fill-in template, dated and attributed, never a compliance requirement.

**Repeating NIST's questionnaire thresholds as this library's own standards.** The 60/80 score bands
and the 3.3 rating convention are NIST's own, stated inside a template built for electronic health
records [[1]](#ref-1). Fix: cite them as NIST's convention within that scope, not as a general
usability bar.

**Presenting the no-decision line as settled industry practice.** This family's contract draws that
line as its own position, against sources that pull toward recording the decision
[[10]](#ref-10)[[30]](#ref-30)[[37]](#ref-37). Fix: state the line as this library's own boundary when
explaining it, not as a convention the sources agree on.

**Treating "reports go unread" as a measured fact.** The sources that make this claim are practitioner
testimony about their own experience
[[14]](#ref-14)[[30]](#ref-30)[[35]](#ref-35)[[46]](#ref-46), not a study of many teams' reports. Fix:
attribute the claim to the practitioner who made it, and never state it as this library's own
measured finding.

**Treating User Interviews' report chapter as current guidance.** The chapter itself carries a notice
that it is unrevised 2019 content, despite a later-dated update stamp on the page [[14]](#ref-14).
Fix: name the chapter's own vintage whenever its content could be mistaken for a current claim.

**Writing "test report" or "test results" without a qualifier.** This document and `test-summary-report`,
a separate bundle in this library's QA family, can both be shortened to words that collide. Fix: name
this document fully, as a usability study report or a user research report, never as a bare "test
report" or "test results."

**Claiming a product manager usually writes the report.** GitLab shows that one may [[28]](#ref-28);
no source in this research gives a share across roles. Fix: say either role writes it, and name no
majority.

## 8. Relationships to other artifacts

**The other family member, `user-research-plan`.** Per the family's contract, the plan states the
questions before the study runs; this report answers the same questions after the study ends, and
links back to the plan. MeasuringU's own plan carries the seam between them: "If possible, try to
outline how the report will be structured in the test plan." [[22]](#ref-22).

**The experiment pair (`experimentation-docs`).** Gilad's line, and the qualifier that must travel
with it, are stated in full in section 6, item 11 [[29]](#ref-29). This family's contract holds, as
its own position, that a study which allocates participants between variants and applies a decision
rule is an experiment, whatever it is called. A usability study, reported here, assigns no participant
to a variant and applies no decision rule against a baseline.

**The QA pair, `test-plan` and `test-summary-report` (`qa-docs`).** Section 7 names the shared-words
anti-pattern directly. A QA test report verifies a product increment against an agreed specification
and grades it. This report studies how people use a product and records observations, not a verdict
against a specification. NIST's own CIF is built for comparative, summative testing
[[2]](#ref-2)[[1]](#ref-1); that is the nearest edge to the QA pair's own territory, and it is named
here rather than left for a reader to notice on their own.

**The documents that use the findings (`discovery-docs`).** The family's own contract states the
boundary directly: "The persona, the problem statement and the design brief take the findings and
frame or decide." (`docs/internal/contracts/research-docs.md`, section 1). This report may recommend;
it frames no problem and chooses no concept.

**The debrief, which sits beside the report rather than replacing it.** Dovetail distinguishes the two
genres directly: "A debrief is not a research report for peer review." [[44]](#ref-44), and says a
debrief can still ground later work: "In these cases, the async debrief still serves as the
foundation." [[44]](#ref-44). A separate Dovetail article prefers a frequent debrief to a rare report:
"A weekly or biweekly 45-minute session where the trio reviews recent evidence together can be more
valuable than a quarterly research readout." [[43]](#ref-43). Mozilla separates the two by what each
one does: "Notably, debriefs are not analysis. They may start the analysis juices going, but analysis
is much more in-depth and complex." [[51]](#ref-51). This family's own spec names no debrief among its
boundaries, and this companion adds it here because two Dovetail articles and Mozilla's own account
each draw the line a report-writer needs.

**The research repository, which fails this family's one-study test.** A repository holds findings
from many studies, tagged and re-used, rather than reporting one study's own result. A UX studio
blog's own definition: "A nugget is a labelled observation supported by evidence." [[33]](#ref-33),
re-used "to form findings that lead to certain conclusions" [[33]](#ref-33) across studies. Dovetail's
own deprecation-policy article treats a finding as a standing entry rather than a one-time result,
"valuable for trend analysis, longitudinal comparison, and institutional memory" [[42]](#ref-42) once
archived. Usercall's operations article describes the cost of running without one: "No shared
repository, no consistent screener, no synthesis process." [[31]](#ref-31). User Intuition argues a
report should still reference one: "Each report should reference prior findings - confirming,
contradicting, or extending what the organization learned previously." [[32]](#ref-32). Dovetail's
own comparison of synthesis methods ties this bundle's report to a single study rather than a
repository: "The output is typically a report or presentation tied to a specific study."
[[45]](#ref-45). A fixed
retention period belongs to a standing repository's own policy [[39]](#ref-39), not to this document's
own figure, as section 3's Appendix subsection states.

**Standing documents this family excludes by name.** Catalog entry 17 (the Voice of Customer report)
aggregates signals "ongoing, quarterly", which the family's contract excludes as a standing instrument
rather than a single study's report. GOV.UK's Design System community page runs a different standing
aggregation on its own threshold: "we will usually investigate something if we hear similar findings
from 4 or more different services" [[5]](#ref-5); that page is itself not a user-research-report
template, and no section list in this research comes from it.

## 9. Adaptations

**A study of a product people already use.** Section 3's Background and Objectives subsection carries
the reasoning this family's contract requires. The shipped-product clause is this library's own
position: a study that asks where people lose time with something they already have is still asking
the generative question, not the evaluative one, whatever the product's own age.

**A report with no written plan behind it.** Research Questions and Answers still fills from what the
study set out to learn, because the sources tie a report to a plan only where one exists, and no
source in this research was asked how often a report runs without a plan behind it.

**A usability test.** Task Results carries this adaptation's content: tasks scored against a success
criterion, errors and time, and the questionnaire scores the plan named, inside NIST's own
health-records-specific thresholds where NIST is cited [[1]](#ref-1).

**A deck or presentation instead of a written document.** Section 6, item 5 names the disagreement in
full. On this research's own reading, GOV.UK's own slide list maps onto the written sections this
bundle ships [[4]](#ref-4); Maze's PAS framework is a different structure this library does not adopt
[[13]](#ref-13). A team presenting instead of writing can still carry this bundle's sections onto its
slides.

## 10. Worked example

[`user-research-report_example.md`](user-research-report_example.md) is a full-variant report for the
2026-05 Reporting friction study at Acme Analytics, written by Priya Nair, PM, Reporting, and dated
2026-05-27. It is the readout of the same study `user-research-plan_example.md` plans. Acme's UX
Research function ran the sessions: one-to-one interviews of about an hour, each with a walkthrough of
the analyst's own dashboard, running from 2026-05-04 to 2026-05-15 with twelve analysts. Because a
walkthrough of a participant's own work is not a usability test, the example marks Task Results not
applicable in one line, the same arrangement section 3 describes for any study that is not a usability
test. The report must be findable by the citation the PRD example already uses for it, "Discovery
readout: Reporting friction study, 2026-05", so the example carries that citation as its title.

---

## References

Every entry below was checked against its own stored text, except the two the maintainer read by
hand and pasted into a working copy. The stored copies carry fetch stamps across five dates:
[[4]](#ref-4) on 2026-10-17; [[13]](#ref-13), [[14]](#ref-14), and [[22]](#ref-22) on 2026-10-23;
[[1]](#ref-1), [[2]](#ref-2), [[3]](#ref-3), [[5]](#ref-5), [[10]](#ref-10), [[11]](#ref-11),
[[12]](#ref-12), [[19]](#ref-19), [[28]](#ref-28), and [[29]](#ref-29) on 2026-10-24; [[7]](#ref-7)
on 2026-10-27, re-stored during a quotation recheck; every other source cited below carries a
2026-10-26 stamp. [[51]](#ref-51) and [[52]](#ref-52) were read by hand by the maintainer on
2026-10-27 and carry no fetch stamp at all.

<a id="ref-1"></a>[1] Robert M. Schumacher and Svetlana Z. Lowry (NIST). "[NISTIR 7742: Customized
Common Industry Format Template for Electronic Health Record Usability
Testing](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7742.pdf)." v0.2, Nov 2010 (accessed
2026-10-26). Supports the full CIF-derived report template: every section heading, its guidance
text, the results-reporting mechanics, and the formative/summative and EHR-specific scope
statements. [primary]

<a id="ref-2"></a>[2] NIST, Information Technology Laboratory. "[What is the
CIF?](https://www.nist.gov/itl/iad/human-centered-technologies/what-cif)" Human-Centered
Technologies page (accessed 2026-10-24). Supports the CIF's lineage, its two named audiences, and
NIST's own caution that the CIF is designed for summative rather than formative testing. [standards]

<a id="ref-3"></a>[3] U.S. Department of Homeland Security. "[DHS Usability Testing
Kit](https://www.dhs.gov/cx/dhs-usability-testing-kit)." dhs.gov/cx (accessed 2026-10-24). Supports
DHS's scaled approach to reporting across four testing methods, from no formal report to a full
report using a provided template. [primary]

<a id="ref-4"></a>[4] GOV.UK Service Manual, User research community. "[Sharing user research
findings](https://www.gov.uk/service-manual/user-research/sharing-user-research-findings)."
Published 24 May 2016 (accessed 2026-10-17). Supports GOV.UK's scaling of the write-up toward slide
decks, and its own statement that agile-team researchers will not have time to write one.
[standards]

<a id="ref-5"></a>[5] GOV.UK Design System community team. "[Share findings about your
users](https://design-system.service.gov.uk/community/share-research-findings/)." GOV.UK Design
System (accessed 2026-10-24). Supports a negative finding: this page is not a user-research-report
template, and its own four-or-more-services threshold for a standing aggregation. [standards]

<a id="ref-6"></a>[6] GSA Digital.gov. "[Usability Starter
Kit](https://digital.gov/resources/digitalgov-user-experience-resources/digitalgov-user-experience-program-usability-starter-kit)."
read via Wayback Machine snapshot of 2026-04-17; the live page now returns HTTP 404 (accessed
2026-10-26). Supports the kit's two separate report templates, a PowerPoint and a Word document,
dated May 2014. [primary]

<a id="ref-7"></a>[7] GSA Digital.gov / Usability.gov. "[Usability Test Summary: Employee
Express](https://s3.amazonaws.com/digitalgov/_legacy-img/2014/01/EmployeeExpressfinalreport-2.docx)."
filled instance of Usability Report Template 2, read as extracted paragraph text after a network
fetch corrupted the stored copy (accessed 2026-10-27). Supports a leaner, filled report shape: a
one-page problem/solution table plus a short narrative with named sections. [primary]

<a id="ref-8"></a>[8] Usability.gov (GSA). "[Report Template: Usability
Test](https://www.usability.gov/how-to-and-tools/resources/templates/report-template-usability-test.html)."
read through a Wayback Machine snapshot of 2024-02-21; the live page now redirects to digital.gov
(accessed 2026-10-26). Supports the retired page's own archival status and summary line. [primary]

<a id="ref-9"></a>[9] Usability.gov (GSA). "[\[Name of Web Application/Site\]
Test](https://www.usability.gov/sites/default/files/report-template-usability-test_0.docx)." the
full retired report template docx, read via Wayback Machine (accessed 2026-10-26). Supports the
complete section-by-section structure and instruction text of the usability.gov report template.
[primary]

<a id="ref-10"></a>[10] Dovetail. "[Research report
template](https://dovetail.com/research-report-template/)." Dovetail (accessed 2026-10-24). Supports
the six-section list, summary-first framing, finding as claim plus evidence plus why it matters,
length guidance, and audience tailoring. [vendor]

<a id="ref-11"></a>[11] UserTesting Knowledge Base. "[Create a good
report](https://help.usertesting.com/hc/en-us/articles/25142550337565-Create-a-good-report)." help
article dated January 22, 2026 (accessed 2026-10-24). Supports three named templates at three
depths, with explicit section lists, evidence types, and audience tailoring. [vendor]

<a id="ref-12"></a>[12] UserTesting Knowledge Base (EnjoyHQ product docs). "[Research
Projects](https://help.usertesting.com/hc/articles/11880311177117)." help article dated January 14,
2026 (accessed 2026-10-24). Supports the written-report-versus-deck framing and "stories" as the
individual-finding unit inside the EnjoyHQ tool's own workflow. [vendor]

<a id="ref-13"></a>[13] Maze. "[How to Create Effective UX Research Reports (+ Free
Templates)](https://maze.co/guides/ux-research/report/)." field-guide chapter 11 (accessed
2026-10-23). Supports the five-item section list, the report-versus-deck formats list, audience
tailoring, and the PAS presenting frame. [vendor]

<a id="ref-14"></a>[14] User Interviews. "[Writing UX Research Reports and
Presentations](https://www.userinterviews.com/ux-research-field-guide-chapter/how-to-write-effective-reports-and-presentations)."
UX Research Field Guide, chapter 09.i, carrying its own notice that the chapter is unrevised 2019
content (accessed 2026-10-23). Supports the six-item section list, per-section guidance, and the
report-versus-presentation tradeoff. [vendor]

<a id="ref-15"></a>[15] Condens. "[How to work with Condens
Artifacts](https://condens.io/help/how-to-guides/best-practices/how-to-work-with-condens-artifacts)."
help guide (accessed 2026-10-26). Supports audience-depth tailoring and recommendation placement
relative to findings; carries no report section list of its own. [vendor]

<a id="ref-16"></a>[16] Amy Schade (Nielsen Norman Group). "[Making Usability Findings Actionable: 5
Tips for Writing Better Reports](https://www.nngroup.com/articles/actionable-usability-findings/)."
Nielsen Norman Group (accessed 2026-10-26). Supports how a finding should be phrased, ranking
findings by severity, and including positive findings. [practitioner]

<a id="ref-17"></a>[17] Jakob Nielsen (Nielsen Norman Group). "[Severity Ratings for Usability
Problems](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/)."
Nielsen Norman Group (accessed 2026-10-26). Supports the 0-4 severity scale and its own caution that
a single evaluator's ratings are unreliable. [practitioner]

<a id="ref-18"></a>[18] Kate Moran (Nielsen Norman Group). "[Qualitative Usability Testing: Study
Guide](https://www.nngroup.com/articles/qual-usability-testing-study-guide/)." Nielsen Norman Group
(accessed 2026-10-26). Supports the existence of a roughly-five-participants convention for
qualitative usability testing; the page is a curated reading list, not a prose guide. [practitioner]

<a id="ref-19"></a>[19] Rachel Krause (Nielsen Norman Group). "[Creating Engaging Reports &
Asynchronous Presentations](https://www.nngroup.com/articles/engaging-reports-presentations/)."
Nielsen Norman Group (accessed 2026-10-24). Supports using quotes and video clips as evidence, and
the caution that anecdotes must illustrate data rather than replace it. [practitioner]

<a id="ref-20"></a>[20] Brian Utesch and Tammi Fitzwater (Nielsen Norman Group). "[Insights Aren't
Outcomes: Research Recommendation
Breakage](https://www.nngroup.com/articles/research-recommendation-breakage/)." Nielsen Norman Group
(accessed 2026-10-26). Supports the chain from data to finding to insight to recommendation.
[practitioner]

<a id="ref-21"></a>[21] Sara Paul (Nielsen Norman Group). "[Data vs. Findings vs.
Insights](https://www.nngroup.com/videos/data-findings-insights/)." Nielsen Norman Group video page
(accessed 2026-10-26). Supports a one-sentence definition distinguishing data, findings, and
insights; the video itself is not transcribed, so only the summary line is verified text.
[practitioner]

<a id="ref-22"></a>[22] Jeff Sauro, PhD (MeasuringU). "[What Goes into a Usability Test
Plan?](https://measuringu.com/usability-test-plan/)" MeasuringU, report-outline section (accessed
2026-10-23). Supports MeasuringU's own recommended report outline, verbatim and in order.
[practitioner]

<a id="ref-23"></a>[23] Jeff Sauro, PhD and Jim Lewis, PhD (MeasuringU). "[You Can Report
Percentages with Small Samples, but Should
You?](https://measuringu.com/should-you-avoid-reporting-percentages-from-small-sample-studies/)"
MeasuringU (accessed 2026-10-26). Supports whether and how to report percentages from small samples,
including the fraction-versus-percentage format question. [practitioner]

<a id="ref-24"></a>[24] Jeff Sauro, PhD (MeasuringU). "[Best Practices for Using Statistics on Small
Sample Sizes](https://measuringu.com/small-n/)." MeasuringU (accessed 2026-10-26). Supports the
generalization limits of small-sample usability data and the use of confidence intervals rather than
bare point estimates. [practitioner]

<a id="ref-25"></a>[25] Jeff Sauro, PhD (MeasuringU). "[7 Steps to Conducting Better Qualitative
Research](https://measuringu.com/qualitative-steps/)." MeasuringU (accessed 2026-10-26). Supports
reporting counts of supporting participants alongside findings and disclosing researcher bias as a
limitation. [practitioner]

<a id="ref-26"></a>[26] Jeff Sauro, PhD (MeasuringU). "[Rating the Severity of Usability
Problems](https://measuringu.com/rating-severity/)." MeasuringU (accessed 2026-10-26). Supports
multiple named severity-scale traditions, treating frequency separately from severity, and including
positive findings. [practitioner]

<a id="ref-27"></a>[27] Nikki Anderson-Stanier (dscout). "[To Ask or Not to Ask? How to Design
Research for Difficult Questions](https://dscout.com/people-nerds/difficult-question-methods)."
dscout People Nerds (accessed 2026-10-26). Supports naming a research question as unanswerable by
the chosen method. [practitioner]

<a id="ref-28"></a>[28] GitLab (UX Research Operations team). "[Resources for Research
DRIs](https://handbook.gitlab.com/handbook/product/ux/ux-research/resources-for-research-dris/)."
The GitLab Handbook (accessed 2026-10-24). Supports who writes a report at GitLab, its format, its
peer-review step, and the follow-up expected of stakeholders. [practitioner]

<a id="ref-29"></a>[29] Itamar Gilad. "[Idea Validation Using the AFTER
Model](https://itamargilad.com/idea-validation-much-more-than-just-a-b-experiments/)."
itamargilad.com (accessed 2026-10-24). Supports the test-versus-experiment distinction, quoted with
its own qualifier that the definition is not the common industry usage. [practitioner]

<a id="ref-30"></a>[30] Junu Yang (Usercall). "[Customer Research Reports Nobody Reads (And How to
Fix That)](https://www.usercall.co/post/customer-research-reports-guide)." Usercall blog (accessed
2026-10-26). Supports why reports go unread, what makes a report change a decision, and a reported
practice of shipping two formats from every study. [vendor]

<a id="ref-31"></a>[31] Junu Yang (Usercall). "[Research Operations Is the Reason Your Insights Team
Either Ships Fast or Falls Apart](https://www.usercall.co/post/research-operations-guide)." Usercall
blog (accessed 2026-10-26). Supports product managers running unsynthesized interviews with no
shared report or repository. [vendor]

<a id="ref-32"></a>[32] Kevin (User Intuition). "[Consumer Insights Reports: What Executives
Actually
Read](https://www.userintuition.ai/reference-guides/consumer-insights-report-structure-what-executives-read/)."
User Intuition Reference Deep-Dive (accessed 2026-10-26). Supports why reports go unread and the
case for connecting a report to a cumulative intelligence base rather than treating it as a
standalone snapshot. [vendor]

<a id="ref-33"></a>[33] Bence Mozer, Tamas Viragh, Dan Damsa (UX studio). "[Atomic research
principles for building a sustainable research
repository](https://www.uxstudioteam.com/ux-blog/atomic-research-principles-for-building-a-sustainable-research-repository)."
UX studio blog (accessed 2026-10-26). Supports atomic research nuggets as the alternative unit to a
one-study report, re-used across multiple studies in a repository. [vendor]

<a id="ref-34"></a>[34] Chris Massey, writing up a talk by Julia Shalet. "[DIY User Research for
Product People](https://www.mindtheproduct.com/diy-user-research-for-product-people/)." Mind the
Product (accessed 2026-10-26). Supports product managers running their own user research without a
UX designer or researcher on the team. [practitioner]

<a id="ref-35"></a>[35] Jeff Humble (The Fountain Institute). "[This could have been
shorter](https://pages.thefountaininstitute.com/posts/this-could-have-been-shorter)." The Fountain
Institute newsletter (accessed 2026-10-26). Supports a designer writing their own research report,
and a practitioner's argument for abandoning the static-report format. [practitioner]

<a id="ref-37"></a>[37] Useberry. "[Stakeholder Buy-In for UX Research: Templates, Timelines, and
Talking
Points](https://www.useberry.com/blog/stakeholder-buy-in-for-ux-research-templates-timelines-and-talking-points/)."
Useberry blog (accessed 2026-10-26). Supports naming the decision a report supports and who owns it,
and stating in advance what happens if findings are inconclusive. [vendor]

<a id="ref-38"></a>[38] Userfeel. "[Optimizing Your Usability Testing Process with Report
Templates](https://www.userfeel.com/blog/optimizing-your-usability-testing-process-with-report-templates)."
Userfeel blog (accessed 2026-10-26). Supports opening with a positive finding and naming questions a
future study should investigate. [vendor]

<a id="ref-39"></a>[39] CleverX. "[Research Repository Template: Build Your Own in
2026](https://cleverx.com/blog/research-repository-template-build-your-own-in-2026/)." CleverX blog
(accessed 2026-10-26). Supports a named retention period and participant de-identification at the
level of a standing repository, not one study's report. [vendor]

<a id="ref-40"></a>[40] CleverX. "[Research Participant Consent Best
Practices](https://cleverx.com/guides/research-participant-consent-best-practices-a-practical-guide-for-user-research-teams)."
CleverX guide (accessed 2026-10-26). Supports granular consent for quoting a participant, and
explicit permission for a specific quote or clip. [vendor]

<a id="ref-42"></a>[42] Dovetail. "[How to create a research findings deprecation
policy](https://dovetail.com/research/research-findings-deprecation-policy-insight-repository/)."
Dovetail (accessed 2026-10-26). Supports a repository-level, multi-study deprecation policy; it
fails this family's one-study test for a single report's own dating question. [vendor]

<a id="ref-43"></a>[43] Dovetail. "[How to run effective research debriefs with product
trios](https://dovetail.com/product-development/research-debriefs-product-trios-shared-understanding/)."
Dovetail (accessed 2026-10-26). Supports the debrief-versus-report question, and a pre-read element
list that maps onto a report's own front matter. [vendor]

<a id="ref-44"></a>[44] Dovetail. "[How to document and share research debriefs
asynchronously](https://dovetail.com/research/async-research-debriefs-distributed-teams/)." Dovetail
(accessed 2026-10-26). Supports a direct distinction between a debrief and "a research report for
peer review", and a debrief's own suggested section list. [vendor]

<a id="ref-45"></a>[45] Dovetail. "[Comparing research synthesis
methods](https://dovetail.com/research/atomic-research-vs-thematic-analysis-vs-affinity-mapping/)."
Dovetail (accessed 2026-10-26). Supports that an output tied to a significant decision is typically
a report tied to one specific study. [vendor]

<a id="ref-46"></a>[46] Caitria O'Neill, interviewed on Awkward Silences #172 (User Interviews
podcast). "[Summer Throwback: On the Problems of Research
Reports](https://podcast.userinterviews.com/episodes/throwback-no-one-reads-your-reports/transcript)."
transcript (accessed 2026-10-26). Supports that an unread report has no impact regardless of its
insight quality, and what makes a report actionable. [practitioner]

<a id="ref-47"></a>[47] Maze. "[Evaluative Research: Key Methods &
Examples](https://maze.co/blog/evaluative-specialization/)." chapter 5 of "What is UX Research: The
Ultimate Guide" (accessed 2026-10-26). Supports the generative-versus-evaluative distinction by
purpose and timing. [vendor]

<a id="ref-48"></a>[48] UserTesting blog. "[Generative vs. evaluation
research](https://www.usertesting.com/blog/generative-vs-evaluation-research)." UserTesting
(accessed 2026-10-26). Supports the same distinction, with its own labelled comparison sentences.
[vendor]

<a id="ref-49"></a>[49] GOV.UK Service Manual. "[Managing user research data and participant
privacy](https://www.gov.uk/service-manual/user-research/managing-user-research-data-participant-privacy)."
published 5 November 2018 (accessed 2026-10-26). Supports anonymising quotes before sharing, where
raw data should live, and how long it should be kept. [standards]

<a id="ref-50"></a>[50] Jeff Sauro, PhD and Jim Lewis, PhD (MeasuringU). "[An Intro to Bayesian
Thinking for UX Research](https://measuringu.com/intro-to-bayesian-thinking-in-ux-research)."
MeasuringU, February 24, 2026 (accessed 2026-10-26). Supports a worked prior-belief/posterior-belief
pattern for one usability test's result, with a stated confidence level. [practitioner]

<a id="ref-51"></a>[51] Jennifer Davidson, with Julia Starkov, Jim Thomas, Marissa (Reese) Wood and
Michael Verdi (Mozilla UX blog). "[Reflecting on 'It's Our Research' at
Mozilla](https://blog.mozilla.org/ux/2019/12/reflecting-on-its-our-research-at-mozilla/)." December
18, 2019. Read by hand by the maintainer on 2026-10-27, after an automated fetch returned a
Cloudflare challenge page. Supports the Firefox user research team's own account of its executive
summaries, and that debriefs are not analysis. [practitioner]

<a id="ref-52"></a>[52] Koji (docs). "[How Long Is User Research Valid? Insight Decay and When to
Re-Run a Study](https://www.koji.so/docs/research-refresh-cadence)." Read by hand by the maintainer
on 2026-10-27. Supports tagging an insight with its fieldwork date, population, and product version
at publication, and the claim that evaluative findings do not survive a material product change; its
own repository-level review cadence fails this family's one-study test. [vendor]