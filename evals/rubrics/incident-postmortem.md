---
title: "incident-postmortem eval rubric"
description: "Scoring criteria for the blind efficacy eval of incident-postmortem documents, split into rubric criteria and held-out criteria"
audience: engineer
level: advanced
tags:
  - evals
  - measurement
---

# Eval rubric: `incident-postmortem`

Scored on the hardened 1 to 5 anchor scale in
[the eval protocol](../../docs/internal/eval-protocol.md). **A 5 is reserved for work a senior
practitioner would not touch.** Solid, shippable-with-a-nitpick work is a 4. Score conservatively and
break ties downward.

## Rubric criteria

**The treatment arm has effectively been told these**, because they derive from the bundle's own guide.
A gap here is expected and is the least interesting number this eval produces.

| Key | Criterion | What a judge checks |
|---|---|---|
| `summary_stands_alone` | Summary stands alone | A reader who reads only the Summary section, and nothing else, can state what happened, roughly how bad it was, and whether it is over. Cause, duration, and resolution state are all present in that section, not scattered elsewhere and not deferred to Root Causes. |
| `impact_is_measured` | Impact is measured with checkable numbers | Every impact statement names an affected system or population, a duration, and a magnitude a reader could verify against a dashboard or support queue. No row reads as a category with no number ("some users," "a while"). |
| `timeline_is_checkable` | Timeline is checkable against a record | Every timeline entry carries a timestamp precise enough to check against a log, alert, or chat transcript without needing to ask the author, and gaps are left visible rather than smoothed into a single bundled line. |
| `root_causes_evidenced` | Root causes are evidenced, not blamed | Every listed cause is a specific, checkable condition backed by named evidence (a log line, a config diff, a metric), more than one cause is offered where the incident plausibly had more than one, and no cause is a person's name. |
| `trigger_is_own` | Trigger names the team's own pre-published criterion | The document names the specific criterion that made this a postmortem and points to where that criterion was published before the incident, rather than restating a generic borrowed list as though it were the team's own. |
| `actions_are_tracked` | Action items are owned and tracked outside the document | Every action item names one owner and a real ticket ID in the team's tracker with a status a reader could check, not a bulleted intention with no owner and no ticket. |

## Held-out criteria

**These appear in neither the template nor the guide**, and that absence was searched for rather than
assumed. They are about decision-usefulness, and they are the circularity control: **a large rubric gap
beside a null held-out gap means the template is teaching its own rubric rather than teaching the
document.**

| Key | Criterion | What a judge checks | Absence evidence |
|---|---|---|---|
| `scopable_without_meeting` | An engineer could scope the follow-up work without a meeting | Pick any single action item. Between the Root Causes evidence, the action's own description, and the Resolution narrative, is there enough specificity (what component, what condition, what already exists versus what needs building) that an engineer could size and start the ticket cold? Or does satisfying it require picking a vague action and inferring the missing technical context from nowhere in the document? | Searched both files for '(?i)(\bkill\b|\bstop\b|\bhalt\b|scope|clarify|ambiguous|actionable without|self-contained|standalone|internally|reconcile)'. The only hit in either file is 'scope table' in the guide's rubric-applicability table (row-scope, an unrelated sense of the word), and the template returned no matches at all. Neither file states or implies a criterion about whether a reader could size or start work from the document without further clarification. |
| `names_a_stop_kill_condition` | The document says what would make the team stop, roll back, or kill this fix | Is there a stated condition under which the shipped fix, or a planned action item, would be abandoned, rolled back, or escalated, e.g. a stated threshold, a named check, or a decision not to pursue an option and why? Or is every action item a one-way commitment with no stated condition for reversing course? | Searched both files for '(?i)(decide|decision|kill switch|stop doing|contradict|inconsisten|meeting|scope the work|without asking|conflicting|trade-?off|would.?ve stopped|halt|abort)'. Guide hits are: 'decisions' in a throwaway phrase about what a postmortem is written after looking at ('logs, code changes, and decisions'), 'decision' describing the bundle's own two-size packaging choice, a rubric cell using 'without asking the author' about timeline verifiability, and 'contradicts' describing how naming a person as cause contradicts the blameless framing. Template hits are the same 'decision' packaging note and the same 'contradicts' phrase. None of these is a criterion about the document stating a stop, rollback, or kill condition for its own proposed work. |
| `no_internal_contradiction` | The document does not contradict itself across sections | Cross-read Summary, Resolution, and Action Items together: does the resolution status claimed in one section match the others (e.g. Summary calls it 'fully resolved' while an Action Item is still fixing the same failure mode with no distinction drawn), and do Root Causes and Lessons Learned describe the same mechanism consistently rather than one implying a cause the other rules out? | Searched both files for '(?i)(decide|decision|kill switch|stop doing|contradict|inconsisten|meeting|scope the work|without asking|conflicting|trade-?off|would.?ve stopped|halt|abort)' and separately for 'cross-read|cross-section|consisten' (checked by inspection of the same grep pass). The only 'contradict' hits in either file are the anti-pattern about naming a person as root cause contradicting the blameless framing, a single-sentence rule about one specific field, not a general instruction to check consistency across the Summary, Resolution, Root Causes, and Lessons Learned sections against each other. |
| `decision_vs_information_distinguishable` | A reader can tell what the author decided from what the author was merely told | In Trigger, Root Causes, and Resolution, can a reader separate the raw inputs the author received (an alert fired, a customer said X, a colleague suggested Y) from the judgment call the author actually made on top of those inputs? Or does the prose flatten reported facts and the author's own conclusion into one undifferentiated narrative voice, so a reader cannot tell whether a claim is something that was observed or something the author decided to believe? | Searched both files for '(?i)(was told|reported by|attribut|distinguish.*(told|decided)|author.?s judgment|what the author)'. The guide's only hit is 'attributed to' inside anti-pattern 7, about an unmeasured percentage figure being attributed to a source document, a citation-honesty point, not a distinction between the author's inputs and the author's own decision. The template returned no matches at all. |

## Authoring notes

Rubric criteria are drawn directly from six of the nine guide self-grade rows (Summary, Impact, Timeline, Root Causes, Trigger, Action Items); I dropped Detection, Resolution, and Lessons Learned only to stay within the 4 to 6 range and kept the ones most central to what the guide itself calls out as make-or-break (rows 1, 2, 3, 4, 6, 9 in the guide's numbering). All four held-out criteria target decision-usefulness (scopability without a meeting, stated kill/rollback conditions, internal consistency across sections, and separability of reported fact from author judgment) and none of these concepts appear anywhere in the guide's rubric, anti-patterns list, or the template's inline WHAT/WHY/ASK/GOOD/WEAK/TRAP guidance, confirmed by targeted grep passes over both files with the search terms and results logged in each absenceEvidence field.
