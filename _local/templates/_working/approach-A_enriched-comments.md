<!--
SAMPLE: Approach A (enriched comments, clean shape). Open in a Markdown preview to see how
it renders: every guidance comment disappears, leaving a clean blank shape. This file shows
three PRD sections only. Not a shipping template.
-->

# {{title}}

## Summary

<!-- WHAT  One short paragraph: what this is and the single outcome it should produce.
           The whole idea, graspable before any detail.
     WHY   The summary is the triage surface; reviewers decide from it whether to read on.
           Deep dive: prd_companion.md, section 1 (Orientation) and section 3 (Anatomy > Summary).
     ASK   What is it? Who is it for? What single outcome does it produce?
     GOOD  "Saved Views lets an analyst capture a dashboard's filters as a named, reopenable
           view, so they spend time reading data, not rebuilding the lens to see it."
     WEAK  "We will add a Views menu with a dropdown and a save button." (mechanics, not outcome)
     TRAP  Describing the solution's mechanics instead of the outcome for the user. -->

{{summary}}

## Problem

<!-- WHAT  The problem from the user's point of view, with evidence it is real and worth
           solving now: who hits it, how often, what it costs them.
     WHY   The problem is the highest-leverage part of the PRD; nail it and the rest follows.
           Deep dive: prd_companion.md, section 3 (Anatomy > Problem).
     ASK   Who hits it? How often? What does it cost them (time, money, risk)? Why solve it now?
     GOOD  "Analysts who monitor the same slice re-apply filters several times a day; in a
           12-person study, 9 rebuilt filters daily and 3 kept a text file of the ones they
           always use."
     WEAK  "Users cannot save filters." (a missing feature, not the problem beneath it)
     TRAP  Stating a missing feature instead of the underlying problem. Spend more time here
           than feels comfortable. -->

{{problem}}

## Functional requirements

<!-- WHAT  What the system must do, as testable statements, each prioritized.
     WHY   Engineering needs must-have vs nice-to-have to make tradeoffs when time runs short.
           Deep dive: prd_companion.md, section 3 (Anatomy > Functional requirements).
     ASK   Is each row one verifiable behavior? Could QA write a test from it as written?
     PRIORITY  MoSCoW: Must (ship-blocking) / Should (important, not blocking) /
               Could (nice to have) / Won't (explicitly out this release).
     ROW HINT  ID = FR-n, stable so acceptance criteria can reference it.
               Requirement = one verifiable behavior, not a UI detail.
     GOOD  | FR-1 | Save the current dashboard state (filters, date range, columns) as a named view | Must |
     WEAK  | FR-1 | Add a dropdown to the toolbar | Must |  (UI detail, not a testable requirement)
     TRAP  Many equally-weighted requirements with no priority; engineering cannot triage. -->

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | {{functional_requirement_1}} | {{priority}} |
