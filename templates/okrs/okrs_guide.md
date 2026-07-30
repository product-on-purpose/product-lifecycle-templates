# OKRs: guide

An operator card. Read it before you fill the template and again before you agree the set. The reasoning
behind every rule here lives in [`okrs_companion.md`](okrs_companion.md).

## Before you start: is this the right document at all?

An OKR set answers **what measurable change do we expect this period, and did we get it.** If your actual
question is something else, write something else.

| If the real question is | Write this instead |
|---|---|
| Where are we trying to get to, over years? | [`product-vision`](../product-vision/) |
| Which problems will we solve, and which will we not? | [`product-strategy`](../product-strategy/) |
| In what order will we work on them? | [`product-roadmap`](../product-roadmap/) |
| What is the standing health of the system, watched continuously? | [`kpi-dashboard`](../kpi-dashboard/). A KPI is a steady-state metric; a Key Result is a metric you are deliberately trying to move. A KPI can become a Key Result for one cycle and then revert |
| Who does what by when? | A project plan. OKRs are the compass, the plan is the turn-by-turn |
| What are we building, in detail? | [`prd`](../prd/) |

**Write nothing at all if** the team has no autonomy to change the number, or if the answer to "what would
we do differently if this went red" is "nothing." A goal nobody can act on is a report.

## The one test that outranks the rest

**Could you complete every piece of work on this list and still have failed?**

If the answer is no, you have written a task list with a scoring rubric attached. The fastest check is
Google's own word list: a Key Result containing **consult, help, analyze, or participate** is describing an
activity. Rewrite it as the change you would see in the world.

The second test is about honesty rather than form: **is there a number in here that nobody has actually
read this month?** A baseline nobody can source is a target nobody can miss.

## Picking a variant

**lean** is the Objective, the Key Results, the parent it serves, and what you are deliberately not doing.
That is the whole artifact, and it is enough for a team that shares context and reviews it together.

**full** adds Initiatives, Confidence and check-in, and Scoring and close-out. Reach for it when the set will
be read by people who were not in the room, when more than one team's work feeds the same measure, or when
this is the first cycle and the operating rules genuinely need writing down.

**One format ships**, and that is a finding rather than an omission. Six candidates were examined
individually and five rejected, including V2MOM, which is genuinely structurally distinct but which
Salesforce does not present as an OKR variant; nine further named goal-setting frameworks were checked for a
counterexample and none qualified. If someone brings you an "OKR canvas," it is a layout, not a different
document.

## The rubric

Score each 0, 1 or 2. **Under 12 out of 18 and this set will be scored on whether the work happened rather
than on whether anything changed**, which is the exact failure OKRs exist to prevent.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Serves a named parent** | No parent named | Names a document, but you cannot say which part of it this advances | Names the parent, and you can point at the specific policy or goal this Objective moves |
| 2 | **Objective is qualitative** | Contains a number | Qualitative, but names the mechanism, so it forecloses other routes | Someone could achieve it by a route you had not considered and you would be pleased |
| 3 | **Key Results are outcomes** | They describe work | Mixed, or a milestone Key Result with no stated reason for the exception | You could finish every initiative and still score badly, and the team knows that |
| 4 | **Baselines are readable** | No baseline | A baseline is stated but nobody has read it this month | Someone can name where each number comes from and when it last updated |
| 5 | **Each measure is owned** | Team names or blanks | A person per Objective, but not per Key Result | A named person per Key Result, and each of them knows it |
| 6 | **Exclusions with a cost** | Nothing excluded | Excludes things nobody asked for | You can point at the sentence, name who asked, and say who told them no |
| 7 | **Work serves a measure** *(full)* | No initiatives, or initiatives that serve "all of them" | Each initiative names a Key Result, but some Key Results have no work behind them | Every initiative serves exactly one Key Result, and any Key Result with no work is deliberate and says so |
| 8 | **Confidence moves** *(full)* | No confidence recorded | Recorded once and unchanged since | At least one has moved, and someone can say what moved it |
| 9 | **Pay question answered** *(full)* | Silent on it | Mentioned, but not in a form anyone could quote back | States in writing whether scores touch reviews or pay, and the team has been told |

**Which rows apply to what.** Every threshold is two thirds of the available points, rounded down.

| Document | Rows | Maximum | Score against |
|---|---|---|---|
| full | all 9 | 18 | **12** |
| lean | 1-6 | 12 | **8** |

**Rows 7 to 9 are scored only against `full`.** The lean variant ships no Initiatives, Confidence or Scoring
section, so grading it on them would penalise the choice of size rather than the quality of the document.

## Failure signals to look for in the draft

**Key Results that are tasks in disguise.** The one the word test catches in seconds. A vendor's analysis of
its own platform put it at roughly half of all Key Results, which is that vendor's own data rather than a
measurement of the world. Nothing ranks the signals in this list against each other, so read it as a list
rather than an order.

**Sandbagging.** A target the team already knows it will hit. Treat it as a predictable response to the
incentive rather than a description of the people: the named practitioners who write about it all tie it to
scores touching something that matters to someone's career. If you find it, look at your Scoring section
before you look at the team.

**Watermelon reporting.** Green on the outside, red inside. It is the same mechanism as sandbagging arriving
one step later, and the tell is a confidence column that has not moved since week one.

**OKR theatre.** A complete cycle of writing, scoring and reviewing that changed nobody's priorities. The
diagnostic question: name one thing the team stopped doing because of this document. If nothing, the set is
decorative and the cycle cost you real hours.

**Cascading as copy-paste.** Key Results copied downward to become the next level's Objectives. Every named
practitioner rejects this, though note that almost all of them still want leadership to set direction first,
so the useful rule is narrower than "never cascade": direction flows down, objectives get negotiated locally.

**Too many Objectives.** Focus is the mechanism this document has and no other document in the family has.
Three Objectives with four Key Results each is twelve numbers nobody will look at twice.

**An unanswered compensation question.** Silence is read as yes. If the team suspects the score feeds a
review, you will get sandbagging next cycle and you will not be told why.

## Before you agree the set

- [ ] Every Key Result has a baseline someone has read in the last month.
- [ ] Every Key Result has one named person, not a team.
- [ ] Someone outside the team has read the Objective and said it back correctly.
- [ ] You have written down whether the score touches pay or reviews.
- [ ] You can name one thing this set means the team will stop doing.
