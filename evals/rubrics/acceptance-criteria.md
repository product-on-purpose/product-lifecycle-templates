---
title: "acceptance-criteria eval rubric"
description: "Scoring criteria for the blind efficacy eval of acceptance-criteria documents, split into rubric criteria and held-out criteria"
audience: engineer
level: advanced
tags:
  - evals
  - measurement
---

# Eval rubric: `acceptance-criteria`

Scored on the hardened 1 to 5 anchor scale in
[the eval protocol](../../docs/internal/eval-protocol.md). **A 5 is reserved for work a senior
practitioner would not touch.** Solid, shippable-with-a-nitpick work is a 4. Score conservatively and
break ties downward.

## Rubric criteria

**The treatment arm has effectively been told these**, because they derive from the bundle's own guide.
A gap here is expected and is the least interesting number this eval produces.

| Key | Criterion | What a judge checks |
|---|---|---|
| `observable-verifiable` | Criteria are observable and pass/fail, not implementation | For every checklist item under Acceptance criteria, Edge cases, and Non-functional criteria, a reader can point to the exact clause naming what a user or system state shows, and none require reading source code or infrastructure choices (e.g., 'uses a queue', 'stored in Redis') to know whether it holds. |
| `unhappy-paths-named` | Edge cases name specific failure conditions with stated outcomes | The Edge cases and negative paths section names concrete failure conditions (empty, denied, conflicting, missing, timeout, or similar) and states an observable outcome for each; a reader can point to which specific failure each line addresses, not a single generic line like 'handle errors gracefully.' |
| `no-dod-duplication` | Criteria are story-specific, not restated universal standards | For each criterion, a reader can point to what is specific to this story's behavior; none read as a generic bar that would apply unchanged to any other story in the backlog (the kind of thing a team-wide Definition of Done already covers). |
| `measurable-nonfunctional` | Non-functional criteria carry a measurable bar | Each entry under Non-functional criteria states a number or a checkable standard (a time limit, an accessibility conformance level, an error-rate ceiling) that a reader could test against; none rest on an unquantified adjective like 'fast' or 'accessible' alone. |
| `single-behavior-scenarios` | Each Given/When/Then scenario tests exactly one behavior | In every scenario, 'When' names a single action and 'Then' names a single outcome; a reader can point to any scenario and confirm it does not chain multiple actions or assertions with 'and' to cover several behaviors at once. |
| `scope-boundary-stated` | Out of scope is stated with specific exclusions, and the document is clean | The Out of scope and notes section names specific exclusions and the assumptions behind them rather than being left blank or vague, and no HTML guidance comments or unfilled {{placeholder}} tokens remain anywhere in the shipped document. |

## Held-out criteria

**These appear in neither the template nor the guide**, and that absence was searched for rather than
assumed. They are about decision-usefulness, and they are the circularity control: **a large rubric gap
beside a null held-out gap means the template is teaching its own rubric rather than teaching the
document.**

| Key | Criterion | What a judge checks | Absence evidence |
|---|---|---|---|
| `scopeable-without-meeting` | An engineer could scope work from this alone | A reader could take this document and produce a task breakdown or rough size estimate without a clarifying conversation with the author; point to the specific criteria or out-of-scope text that gives real boundaries (what's touched, what's excluded) for the central piece of the story, rather than boundaries a reader would have to infer or ask about. | Searched acceptance-criteria_guide.md and acceptance-criteria_template-full.md for 'meeting', 'estimat', 'story points?', 'size the work', 'plan the work' (regex, case-insensitive not needed since terms are lowercase in source). No matches in either file. Neither the self-grade rubric nor the template's WHAT/WHY/ASK/GOOD/WEAK/TRAP guidance mentions whether a reader can act on the document without further conversation, or estimating/sizing work from it. |
| `stop-kill-signal` | The document says what would make the team stop or kill this | Somewhere in the document, a condition is stated under which the team would stop, reconsider, or kill the story, not only conditions under which it is accepted as done; point to the sentence, and it must name something concrete (a metric miss, a blocked dependency, a finding that invalidates the approach), not a vague 'if problems arise.' | Searched both files for 'kill', 'stop\b', 'abandon', 'cancel', 'go/no-go', 'halt'. No matches in acceptance-criteria_guide.md or acceptance-criteria_template-full.md. The template's sections (Story reference, Acceptance criteria, Scenarios, Edge cases, Non-functional criteria, Out of scope) are all oriented around confirming a story is 'done and correct'; none asks what would cause the team to stop or kill the work. |
| `internal-consistency` | Nothing in the document contradicts anything else in it | No acceptance criterion, scenario, edge case, or non-functional criterion asserts something another section rules out or excludes (for example, a criterion assuming a case the Out of scope section later excludes, or a Then that a stated edge case contradicts); point to the two clauses in tension, or confirm the document is clean of any. | Searched both files for 'contradict', 'inconsisten', 'conflict', 'internally'. acceptance-criteria_guide.md: no matches. acceptance-criteria_template-full.md: 'conflict' appears once, in the Edge cases section's guiding question ('What happens on empty, denied, conflicting, or missing input?') as a category of system-state conflict (e.g., two users editing the same record) to consider as an edge case, not as an instruction to check the document for self-contradiction across its own sections. No form of a cross-section consistency check appears in either file. |
| `decision-vs-told` | A reader can tell what the author decided from what the author was told | For a load-bearing claim in the document (a threshold, an exclusion, a behavior choice), a reader can tell whether it reflects a constraint or fact handed to the author (a platform limit, a stakeholder mandate) versus a choice the author made among live options; point to language marking that distinction, not a flat declarative list where a mandate and a personal call read identically. | Searched both files for 'decided', 'was told', 'told\b', 'input from', 'distinguish'. No matches in acceptance-criteria_template-full.md; acceptance-criteria_guide.md's only related hit under a broader 'decision' search is line 33, 'Out of scope is stated, so omissions are not mistaken for decisions,' which addresses telling a scope omission from a scope decision, not telling the author's own decisions apart from constraints handed to them elsewhere in the document. The template's WHY fields (lines 39, 58-59, 75, 98, 117, 133-134) explain why each section matters but never instruct marking a claim's provenance as author-decided versus given. |

## Authoring notes

Read templates/acceptance-criteria/acceptance-criteria_guide.md (the operator-card self-grade rubric and named anti-patterns) and templates/acceptance-criteria/acceptance-criteria_template-full.md (the full-variant scaffold with its per-section WHAT/WHY/ASK/GOOD/WEAK/TRAP comments) as the two governing files.

Rubric criteria were derived directly from the guide's six self-grade bullets and six named anti-patterns, collapsed to six non-overlapping evidence cells: observable/verifiable phrasing, named unhappy paths, no Definition-of-Done duplication, measurable non-functional bars, single-behavior Given/When/Then scenarios, and a stated scope boundary plus a clean (comment-free, placeholder-free) final document. Each cell is phrased as something a reader points at, not a count, so a document can't satisfy the cell by padding rather than improving.

Held-out criteria were built from the four example flavors given in the task (scope without a meeting, stop/kill signal, internal contradiction, decided-vs-told) since all four turned out to be genuinely absent from both files on targeted search, so all four are reported rather than trimming to three. Every held-out search was run against only the two named files (guide and template-full); the one near-miss worth flagging is 'conflict', which appears once in the template but denotes a system-state edge case category (concurrent edits, etc.), not document self-contradiction, so it does not disqualify the internal-consistency criterion. Note that a companion doc, example doc, and research log also exist in this bundle directory but were out of scope for the absence search per the task's framing ('the template or the guide'); if the evaluator wants the held-out set checked against the full bundle rather than just these two files, that would be worth a follow-up pass, particularly against acceptance-criteria_companion.md which does use the word 'decision' twice in an unrelated context (source citations).
