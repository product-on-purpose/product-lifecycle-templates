# User Research Plan: the guide

This document plans one study of how people use a product, whether nothing is built yet or the product
already ships. It is not a **test plan**, the `test-plan` bundle that verifies a product increment
against a specification. Nor is it an **A/B test plan**, the `experiment-design-doc` bundle that
allocates participants between variants. The words "test plan" overlap only because a usability test's
plan is sometimes called that - see Picking a variant, below. The deep explainer behind every rule here is
[`user-research-plan_companion.md`](user-research-plan_companion.md); a fully worked instance is
[`user-research-plan_example.md`](user-research-plan_example.md).

## Before you start: is this the right document at all?

Write a user research plan when one study of the people a product serves is about to run, and you need
to agree, before it starts, why it runs, which decision its findings will inform, what the sessions must
learn, from whom, and when. Nielsen Norman Group states the identity directly: "A research plan is a
document that outlines the goals, methods, and logistical details of a research study." When the study
is a usability test, the plan also carries the tasks and the measures, which is why the alias "usability
test plan" exists at all.

**Write something else if:**

| You actually need | Because |
|---|---|
| a **user research report** | the not-yet-built sibling to this bundle; it answers, after the study ends, the same questions this plan sets out before the study runs |
| a **test plan** (`test-plan`) | that document verifies a product increment against an agreed specification and grades it; this document studies how people use a product and records observations, never a verdict |
| an **experiment design document** | Itamar Gilad draws the line this library relies on: "Per this definition an A/B test is an experiment, but a usability test is not," with his own qualifier attached, "I realize that this is not the common definition used in the industry - in many cases the words test and experiment are used interchangeably." A study that allocates participants between variants and applies a decision rule is an experiment, whatever it is called |
| a **problem statement** or a **design brief** | this family's own contract draws the line: those documents take the findings and frame or decide; this plan plans the study that produces the findings, and frames no problem and chooses no concept |
| a **project brief** | Digital NSW places this plan "After you have been given an initial project brief, but before you commence any official research activities." A project brief asks for authority to start; this plan sets out one study inside the authority the project brief already granted |
| an **interview guide or a screener** | those are the session script, catalog entry 25, an unbuilt candidate in this family. This plan links to it under Related Documents (full) or in Method (lean); it never holds the moderator's opening, the consent wording, or the probes itself |
| a **standing service-level research plan, or a research roadmap** | GOV.UK's round-planning page presupposes exactly that standing document: "You can only plan specific rounds of research when you've created a research plan for your service." A roadmap tracking many studies at once is the same kind of standing artifact from a different angle. Both are maintained over time; this plan is written for, and finished with, one study |

**Write a lighter version, or none at all, if your team already meets customers every week.** Teresa
Torres argues that project-based research, plan and all, "it's not sufficient for teams who continuously
ship value to customers," because "Good product discovery teams engage with customers at least weekly."
Against her, User Interviews holds that even a quick study "still needs a plan, but it can be a brief
one," and Paul Boag, who argues for scoping research down to a specific question, hedges his own
recommendation: "The results you get back will be far from perfect and could possibly lead to false
conclusions." Treat this as a real dispute over how light a plan can be, not a rule either way: a team on
a weekly cadence may write no separate plan per interview, but that is a judgment call for that team, not
a default this guide sets for every reader.

**One more sense to rule out.** The word "brief" is not this document's name under any sense this
research found. Dovetail uses it for the stakeholder's request that comes before the plan: "A brief is
the request - what a stakeholder wants to learn and why it matters to them. A plan is the response - how
you'll actually study it, with method, participants, and timeline." Maze uses it for the session guide.
A third source uses it for the study's whole intake document. Whichever sense your own team already uses
"brief" for, do not call this plan a "research brief" and expect a reader to know which of those three
things you mean.

**Who writes it, and who agrees it before recruiting starts.** No source read for this bundle names one
role as the plan's only legitimate author; a researcher, a product manager, or the pair writing together
all appear in practice, and this library lets either role write it. Agreement before fieldwork is better
supported: Defra's own sequence runs from a scoping workshop to "Submit the research plan to your lead
user researcher (if your delivery group has one) for review or approval," then to "Share the approved
plan with your team so everyone is aligned." Koji is blunter still: "Get sign-off on the research
questions from the stakeholders who will act on findings." This template's frontmatter carries that
agreement as the `approver` field, filled in with a name, not a team, before the dates in Schedule and
Logistics begin.

**If the study changes while it runs, this plan records the change.** Nielsen Norman Group: "Update the
plan after the research study is over. In moderated studies, it's common to make adjustments during the
study to get better data." This family's contract fixes the plan's finish line at the report, as this
library's own position. Until the findings are reported, revise this plan in place to say what changed.
Once the report is written, this plan stops changing.

## Picking a variant

**Lean** carries the seven sections every size ships: Why This Study and the Decision It Informs, Goals
and Research Questions, Method, Participants and Recruiting, Tasks and Measures, Schedule and Logistics,
and What Happens to the Findings. **Full** adds four, in this order: What We Already Know, Roles and
Observers, and Consent, Privacy and Ethics, each inserted among the lean seven, then Related Documents,
appended after them.

Use full when at least one of these is true: earlier research or assumptions are worth summarizing
before the sessions run; more than one person will moderate, take notes, or observe, and that needs
writing down rather than assumed; consent, data handling, or retention needs its own section rather than
one line inside Participants and Recruiting; or related materials, the session guide, the screener, the
consent form, the prototype, are worth linking in their own place rather than folded into Method. Use
lean when none of those is true: one moderator, consent handled the way the team always handles it, and
nothing to link beyond the session guide itself.

**Tasks and Measures ships at every size, filled in only for a usability test.** For any other method,
the section is one line naming the method actually used, with the task table and the two measure lines
marked N/A. That is a complete answer, not a placeholder waiting to be filled. The usability-test-plan
identity rests on one publisher's sentence: "When planning a usability test, the research plan is often
referred to as a test plan." So this block is the clause that makes the alias true when it applies, never
an optional extra once it does.

**The session script stays out of this plan at every size, and that exclusion is this library's own
position, not a documented convention.** Most sources this bundle's research read put the moderator's
opening, the consent wording, and the follow-up probes inside the plan itself; this library links them
instead, because the interview guide is a separate, unbuilt candidate in this family's own catalog. The
line this plan draws is: task scenarios, their success criteria, and the measures stay here; the
moderator's opening, the consent script, and the probes go to the linked guide. No source draws that
exact line; it is this library's own arrangement, stated here so a reader does not mistake it for
received practice.

## The rubric

Below 16 out of 22 on a full plan, a stakeholder reading it cannot tell what decision the study serves,
whether the sessions will actually answer the questions set for them, or who is accountable for what
happens once the findings come in, without asking the author questions this document should have
answered on its own. Below 10 out of 14 on a lean plan, the same gap opens with four fewer sections
standing between a weak answer and the people the plan is meant to align.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **A falsifiable decision** | No decision named, or the goal is to "understand" or "explore" | A decision is named, but nothing says what result would change it | You can name the decision and the specific result that would change it |
| 2 | **Agreed before recruiting starts** | No approver named anywhere in the document | An approver is named, but the status does not read as agreed, or the plan's date falls after sessions in Schedule and Logistics begin | A named approver appears, the status reads as agreed, and the plan's date comes before the first recruiting or session date |
| 3 | **Answerable research questions** | A question restates the goal ("understand the experience") | A question is phrased as something to learn, but reads like something a moderator would say aloud to a participant | Every question is phrased as something the study must learn, none could be read aloud to a participant as it stands, and the questions a moderator would ask are left to the linked session guide |
| 4 | **Method fits the questions** | A method is named with no reason it fits these questions | Method and a reason are both named, but a reader cannot tell whether it is generative or evaluative | Method, fit, and a stated generative-or-evaluative (or qualitative-or-quantitative) label together tell a reader what the findings can and cannot settle |
| 5 | **Screenable participant criteria** | "Some users," with no criterion for who qualifies | A criterion is named but vague enough that two readers would screen different people | A reader who has never met the team could use the qualifying and disqualifying lines alone to screen a real person in or out, and the chosen count carries a reason stated for this study |
| 6 | **Tasks set before fieldwork** | The study is a usability test and the table is blank, or the N/A line names no actual method | Tasks exist, but a success criterion is missing, vague, or set after the sessions ran | For a usability test, every task is a scenario with a success criterion set now and a named measure; for any other method, one line names the method actually used and the table and measure lines read N/A, which scores the same as a full usability block |
| 7 | **Findings feed a decision** | The section names a build, iterate, or drop decision, or any other verdict | Output and audience are named, but nothing ties back to the decision named in row 1 | Output, audience, rough timing, and the decision it feeds are all named, and nothing in the section reads as the study's own conclusion |
| 8 | **A named earlier signal** *(full only)* | "No prior research exists," or the section is blank | Something earlier is named, but no assumption is stated for this study to test | A specific earlier signal is named with where it came from, and the assumption this study tests is distinguishable from something the team already knows |
| 9 | **Roles are named people** *(full only)* | "The researcher will handle it," with no note taker or observer named | A moderator is named, but note-taking or observing is unaccounted for | Moderator and note taker are named (even as the same person, stated as such), and observers are named with how they watch, open to anyone willing and informed |
| 10 | **Retention points to policy** *(full only)* | "Participants will sign something," with no mention of how long anything is kept | Consent is described, but a retention period is stated as this study's own figure rather than a pointer to policy | Consent and what participants are told are both concrete, and retention points to the organization's standing policy rather than restating a number as this study's own |
| 11 | **Linked documents resolve** *(full only)* | "See the shared drive," or similar | Items are named, but not as something a reader could click through to | The session guide, screener, consent form, and test environment each resolve to a real link or an explicit "not applicable," and no moderator script is pasted in here instead of linked |

**Which rows apply to what.** Full ships all eleven rows, because a reader of a full plan can ask about
earlier knowledge, named roles, consent and retention, and linked materials, as well as the seven every
size must get right. Lean ships the first seven, every row the lean variant has a section to support.

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| lean | 1-7 | 14 | **10** |
| full | all 11 | 22 | **16** |

The test behind every row above: could someone satisfy the cell by adding words without the plan
actually telling a reader more? Row 5's count, for instance, is never graded by how many participants are
listed; the sources disagree too widely for any one number to be a standard, so the row grades whether
the chosen number carries its own stated reason, not what that number is.

## Named anti-patterns

**Treating "test plan" as this document's own name, unqualified.** Nielsen Norman Group's own usability
checklist uses the phrase for this document too, which is exactly how the collision happens. The tell:
the word "test" appears with no "research," "usability," or "user" beside it. Fix by naming the document
fully, a usability test plan or a research plan, and never a bare "test plan."

**Calling a usability test an experiment.** The tell: a decision rule compares two variants, or
participants are assigned to a condition. Fix by reserving "experiment" for a study that allocates
participants between variants and applies a decision rule, and calling a usability test a test, as
Gilad's own definition does.

**Writing a recommendation or a build-or-drop decision into the plan.** The tell: a sentence in What
Happens to the Findings reads like a conclusion rather than a plan for producing one. Fix by naming which
decision the findings will inform and stopping there; the recommendation itself is the report's job,
once the sessions have run.

**Carrying a programme budget, a reserve, or a standing retention policy as though it were this study's
own figure.** The tell: a specific number of months, or a dollar reserve, that reads like it was copied
from somewhere else. Fix by naming how this study's own participants are thanked or paid, and pointing to
the organization's retention policy rather than restating one program's figures as this plan's own.

**Repeating a participant count, an analysis-to-fieldwork ratio, or an aggregation threshold as though it
were a standard.** The tell: a bare number with no reason attached to this study. Fix by stating the
number chosen, with the reason it was chosen for this study, and leaving someone else's figure as
background rather than a rule.

**Using the words "research brief" as though they meant this document.** The tell: "brief" appears with
no qualifier, anywhere in the plan or in conversation about it. Fix by saying plainly which study informs
which decision, and leaving "brief" for whichever of its several senses your own team already uses it
for.

**Presenting the usability block as an optional extra for a usability test.** The tell: Tasks and
Measures is filled in last, or thinly, while every other section is detailed. Fix by filling Tasks and
Measures before most of the rest of the plan when the study is a usability test; it is the heart of the
plan at that point, not an appendix to it.

**Pasting the session script into this plan instead of linking it.** The tell: a moderator's opening, a
consent script, or a list of probe questions sitting inside Method or Related Documents rather than
behind a link. Fix by linking the session guide and the screener, and keeping only the task scenarios,
their success criteria, and the measures inside this document.

## When it is good enough

When the decision the study serves is named with what would change it, when every research question
reads as something the sessions can answer rather than something a moderator would say aloud, when the
participants named are falsifiable by a stranger reading the plan, and when a named approver has agreed
the plan before recruiting began, by a real date.

Then self-grade against the rubric above, and delete every HTML comment. A plan that reads well but
names no decision, or that quietly carries a recommendation before the sessions have run, has not
finished the job it exists to do, whatever else it contains.
