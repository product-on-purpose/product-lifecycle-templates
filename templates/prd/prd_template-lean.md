---
title: "{{title}}"
doc_type: prd
size: lean
owner: "{{owner}}"
status: draft
doc_version: "{{doc_version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: prd
source_template_version: 0.1.0
---

<!--
LEAN PRD. The minimum that is still genuinely useful. Use this for a single feature, a spike,
or an early idea. To grow it into a full PRD, ADD sections (see prd_template-full.md); never
rename or reorder the ones below (the full variant is a strict superset of this one).

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   prd_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you ship: self-grade against prd_guide.md, then DELETE every HTML comment. They are
   guidance, not content.
-->

# {{title}}

## Summary

<!-- WHAT  One short paragraph: what this is and the single outcome it should produce. The whole
           idea, graspable before any detail.
     WHY   The summary is the triage surface; a reviewer decides from it whether to read on. If you
           cannot write it, the work is not shaped enough to spec yet.
           Deep dive: prd_companion.md section 3 (Anatomy > Summary).
     ASK   What is it? Who is it for? What single outcome does it produce?
     GOOD  "Saved Views lets an analyst capture a dashboard's filters as a named, reopenable view,
           so they spend time reading data, not rebuilding the lens to see it."
     WEAK  "We will add a Views menu with a save button and a dropdown." (mechanics, not outcome)
     TRAP  Describing the solution's mechanics instead of the outcome for the user. -->

{{summary}}

## Problem

<!-- WHAT  The problem from the user's point of view, with evidence it is real and worth solving
           now: who hits it, how often, what it costs them.
     WHY   The problem is the highest-leverage part of the document; nailing it is the single most
           important step. Spend more time here than feels comfortable.
           Deep dive: prd_companion.md section 3 (Anatomy > Problem); anti-patterns in section 7.
     ASK   Who hits it? How often? What does it cost them (time, money, risk)? Why solve it now?
     GOOD  "Analysts who monitor the same slice re-apply filters several times a day; in a 12-person
           study, 9 rebuilt filters daily and 3 kept a text file of the ones they always use."
     WEAK  "Users cannot save filters." (a missing feature, not the problem beneath it)
     TRAP  Stating a missing feature instead of the underlying problem. -->

{{problem}}

## Goals and non-goals

<!-- WHAT  Goals: the outcomes this work must achieve, ideally measurable. Non-goals: what you are
           deliberately NOT doing, to keep scope honest.
     WHY   The non-goals list is the most-skipped and most-valuable line of scope-creep insurance.
           Deep dive: prd_companion.md section 3 (Anatomy > Goals and non-goals).
     ASK   What outcome must be true when this ships? What are we choosing not to do, and why?
     GOOD  Goal: "Let a user reopen a saved view in one action and set one as their default."
           Non-goal: "Scheduled email delivery of a view. Out of scope now; likely a fast follow."
     WEAK  A list of goals with no non-goals at all.
     TRAP  Omitting non-goals, the main entry point for scope creep. -->

**Goals**
- {{goal_1}}

**Non-goals**
- {{non_goal_1}}

## Target users

<!-- WHAT  Who this is for, specifically: the segment, role, or persona, plus the context they are
           in when they hit the problem.
     WHY   Design and tradeoffs depend on knowing the user; name the primary user when segments
           conflict. Deep dive: prd_companion.md section 3 (Anatomy > Target users).
     ASK   Which specific user? In what situation do they hit the problem? Who is this NOT for?
     GOOD  "Primary: the Recurring Analyst who returns to the same dashboards daily within a stable
           filter set. Not optimized for the one-time explorer."
     WEAK  "All users."
     TRAP  "All users" - if it is for everyone, it is designed for no one. -->

{{target_users}}

## Solution overview

<!-- WHAT  The shape of the proposed solution at a high level: the core idea and how a user
           experiences it. Link the prototype or mockup if one exists.
     WHY   It gives the team a shared mental model before detail. For many teams the prototype is
           the real spec and this prose is its companion, not its replacement.
           Deep dive: prd_companion.md section 3 (Anatomy > Solution overview) and the prose-vs-
           prototype debate in section 6.
     ASK   What is the core idea? How does a user experience it? Where does the prototype live?
     GOOD  "A Views control at the top of the dashboard shows the active view and opens a menu to
           save, switch, set a default, and share. The interactive prototype is the source of truth
           for the experience; this section carries the why and the scope."
     WEAK  Jumping straight to field-level UI or the data schema.
     TRAP  Implementation detail before the experience is clear. -->

{{solution_overview}}

## Success metrics

<!-- WHAT  How you will know it worked: one or two primary metrics tied to the goals, plus a
           guardrail metric you must not harm.
     WHY   It defines "did it work" before you are emotionally invested in the answer. Define before
           build. Deep dive: prd_companion.md section 3 (Anatomy > Success metrics).
     ASK   What primary number moves if this succeeds? What must NOT get worse (the guardrail)?
     GOOD  "Primary: median time from dashboard open to first meaningful interaction drops for
           Recurring Analysts. Guardrail: shared-view permission incidents stay at zero."
     WEAK  "Increase pageviews." (a vanity metric that can rise while the user outcome does not)
     TRAP  Defining metrics after results arrive, or picking a vanity metric with no guardrail. -->

- Primary: {{primary_metric}}
- Guardrail: {{guardrail_metric}}

## Open questions

<!-- WHAT  A living list of what is still undecided or unknown. Each row: a question, an owner, and
           a needed-by date.
     WHY   Surfaced unknowns are what make a PRD an honest living document rather than a frozen
           claim of certainty. Deep dive: prd_companion.md section 3 (Anatomy > Open questions).
     ASK   What is genuinely undecided? Who owns each answer? By when is it needed?
     GOOD  | What magnitude of time-to-insight gain counts as success? | Priya + Data | Before GA |
     WEAK  An empty table left to look finished.
     TRAP  Hiding unknowns to look more complete; a PRD with no open questions is usually hiding
           them, not finished. -->

| Question | Owner | Needed by |
|---|---|---|
| {{open_question_1}} | {{owner}} | {{date}} |
