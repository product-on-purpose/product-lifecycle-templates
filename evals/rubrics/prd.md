---
title: "prd eval rubric"
description: "Scoring criteria for the blind efficacy eval of prd documents, split into rubric criteria and held-out criteria"
audience: engineer
level: advanced
tags:
  - evals
  - measurement
---

# Eval rubric: `prd`

Scored on the hardened 1 to 5 anchor scale in
[the eval protocol](../../docs/internal/eval-protocol.md). **A 5 is reserved for work a senior
practitioner would not touch.** Solid, shippable-with-a-nitpick work is a 4. Score conservatively and
break ties downward.

## Rubric criteria

**The treatment arm has effectively been told these**, because they derive from the bundle's own guide.
A gap here is expected and is the least interesting number this eval produces.

| Key | Criterion | What a judge checks |
|---|---|---|
| `problem_weight_and_evidence` | Problem is evidenced and out-weighs the solution | A reader can point to a specific piece of evidence in the Problem section (a study, a count, a quote, an observed frequency) that says who hits the problem, how often, and what it costs them, and can confirm the Problem section reads as longer or more developed than the Solution overview section, not the reverse. |
| `goals_measurable_nongoals_explicit` | Goals are outcomes and non-goals are named | A reader can point to at least one Goal phrased as a user or business outcome rather than a shipped feature, and can point to a Non-goals entry that names something deliberately excluded with a stated reason, not a blank or placeholder line. |
| `target_user_specificity` | Target user is a named segment, not everyone | A reader can name the specific primary user segment or persona from the Target users section, including the situation they are in when they hit the problem, and confirm the document does not fall back to "all users" or an undifferentiated role. |
| `metrics_primary_and_guardrail` | Success is defined with a primary metric and a guardrail, before build | A reader can point to a named primary metric tied to a stated goal, a separate named guardrail metric that must not get worse, and a measurement window, all written as if defined before results exist rather than fitted to a foregone conclusion. |
| `open_questions_owned_and_dated` | Open questions carry a real owner and a real date | A reader can point to at least one Open questions row with a named owner (a person or team, not "TBD") and a needed-by date or milestone, and confirm the table is not empty or left as an unfilled placeholder to look finished. |
| `unhappy_paths_and_prioritized_requirements` | Full variant covers unhappy paths and prioritizes requirements | A reader can point to explicit empty, loading, and error state descriptions in UX and design (not happy-path-only), and can point to a MoSCoW priority marked on each Functional requirement row, so engineering can see what is cut first. |

## Held-out criteria

**These appear in neither the template nor the guide**, and that absence was searched for rather than
assumed. They are about decision-usefulness, and they are the circularity control: **a large rubric gap
beside a null held-out gap means the template is teaching its own rubric rather than teaching the
document.**

| Key | Criterion | What a judge checks | Absence evidence |
|---|---|---|---|
| `scopable_without_a_meeting` | An engineer could scope the work from the document alone | Pick any functional requirement, NFR target, or dependency row and check whether a reader could estimate its effort and identify its blockers from what's written, without needing to find the author and ask a clarifying question first; if any load-bearing row is too vague to size (no owner, no status, no measurable target), the document fails this on that row specifically. | Searched prd_guide.md and prd_template-full.md for meeting|sync|clarify|ambiguous|ambiguity|actionable without|self-contained|hand this to|hand it to and for estimate|effort|scope work|size the work|without a meeting|clarifying question: no matches in either file. The template's closest neighbor is the FR section's ASK "Could QA write a test from it as written?", which checks testability of one row, not whether the document as a whole lets someone size and sequence the work without a conversation. |
| `explicit_stop_or_kill_condition` | The document names what would make the team stop or kill this | Look across Success metrics, Risks and mitigations, and Rollout and release plan for a stated condition (a guardrail breach, a pilot result below a threshold, a missed date) that is explicitly tied to an action to halt, reverse, or not proceed; a document that only lists risks with mitigations but never says what result would stop the work fails this. | Searched prd_guide.md and prd_template-full.md for kill|stop this|stop building|halt|discontinue|sunset|abandon: the only hit is prd_template-full.md line 60, "A PRD that cannot name the strategy it serves is a candidate to kill, not to refine" - a meta-heuristic about whether the PRD itself should exist, not an in-document condition for stopping the initiative once underway. No other mentions of a stop or kill trigger tied to a metric, date, or result appear in either file. |
| `no_internal_contradiction` | Nothing in the document contradicts itself | Cross-check Goals against Non-goals, Functional requirements against NFRs and Rollout plan, and Target users against Solution overview for two statements that cannot both be true (e.g., a goal implying broad rollout while the rollout plan restricts to one segment indefinitely, or a non-goal excluding something a functional requirement then requires); a reader should be able to name the two conflicting sentences and their locations, or confirm none exist. | Searched prd_guide.md and prd_template-full.md for contradict|inconsistent|conflicts with: no matches in either file. Neither the self-grade rubric nor any section's WHAT/WHY/TRAP asks the author to cross-check sections against each other for consistency; each section is graded in isolation. |
| `decision_vs_input_traceable` | A reader can tell what the author decided from what the author was told | Pick any non-obvious choice in the document (a scope cut, a priority call, a target-user narrowing) and check whether the text distinguishes the author's own judgment from an instruction, request, or constraint handed to them by a stakeholder, sponsor, or prior decision; prose that reports conclusions in a flat, undifferentiated voice so a reader cannot tell whether the author chose it or was told to write it fails this. | Searched prd_guide.md and prd_template-full.md for decided|decision maker|stakeholder told|requested by|asked for: no matches in either file (the word "decided" appears only in prd_companion.md, a file outside the scope of this check, describing open questions as "the undecided," not authorship attribution). Neither file asks the author to mark which statements are their own call versus a directive received from someone else. |

## Authoring notes

Both source files were read in full: templates/prd/prd_guide.md (47 lines, contains the self-grade rubric and named anti-patterns) and templates/prd/prd_template-full.md (302 lines, the full-variant template with inline WHAT/WHY/ASK/GOOD/WEAK/TRAP guidance per section).

Rubric criteria (favor the treatment arm) were pulled directly from the guide's nine-item self-grade checklist, collapsing overlapping items (e.g., the two "load-bearing decision" and "guidance comments deleted" hygiene checks were folded into the full-variant criterion since they are structural rather than content-quality signals) down to six criteria that each name a specific, pointable piece of evidence rather than a count.

Held-out criteria use the exact four flavors given in the task prompt (scope without a meeting, stop/kill condition, internal contradiction, decided-vs-told), since each was independently confirmed absent from both files via targeted grep searches before being written up. One near-miss was found and documented: prd_template-full.md line 60 uses the word "kill" but in a different sense (a meta-heuristic for whether the PRD should exist at all, not an in-document trigger for halting in-flight work), so it does not disqualify that held-out criterion. A second near-miss: the word "decided" appears in prd_companion.md (a third file, out of scope for this task's two named files) describing open questions, not authorship attribution, so it also does not disqualify its held-out criterion.

All eight criteria are written as pointable evidence checks (name the sentence, name the row, name the two conflicting statements) rather than as satisfiable-by-counting checklist items, per the instruction that a criterion must not be satisfiable without actually improving the document.
