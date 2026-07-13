<!--
SAMPLE: Approach C (hybrid). Open in a Markdown preview to see how it renders: one italic
prompt line per section survives (with a clickable companion link); the heavier guidance in
the comment disappears. This file shows three PRD sections only. Not a shipping template.
-->

# {{title}}

## Summary

_What is it, who is it for, and the single outcome it produces? One short paragraph._
_Deep dive: [companion section 1 (Orientation)](../prd/prd_companion.md#1-orientation)._

<!-- GOOD "Saved Views lets an analyst capture a dashboard's filters as a named, reopenable
          view, so they spend time reading data, not rebuilding the lens to see it."
     WEAK "We will add a Views menu with a dropdown and a save button." (mechanics, not outcome)
     TRAP describing solution mechanics instead of the user outcome. -->

{{summary}}

## Problem

_Who hits it, how often, what it costs them, and why solve it now? State the problem, not a feature._
_Deep dive: [companion section 3 (Anatomy > Problem)](../prd/prd_companion.md#3-anatomy-section-by-section)._

<!-- GOOD "Analysts who monitor the same slice re-apply filters several times a day; in a
          12-person study, 9 rebuilt filters daily and 3 kept a text file of the ones they use."
     WEAK "Users cannot save filters." (a missing feature, not the problem beneath it)
     TRAP stating a missing feature instead of the underlying problem; spend real time here. -->

{{problem}}

## Functional requirements

_One verifiable behavior per row, each prioritized (MoSCoW: Must / Should / Could / Won't)._
_Deep dive: [companion section 3](../prd/prd_companion.md#3-anatomy-section-by-section)._

<!-- ROW HINT  ID = FR-n (stable, referenced by acceptance criteria); Requirement = one
              verifiable behavior, not a UI detail.
     GOOD | FR-1 | Save the current dashboard state (filters, date range, columns) as a named view | Must |
     WEAK | FR-1 | Add a dropdown to the toolbar | Must |  (UI detail, not testable)
     TRAP many equally-weighted requirements with no priority; engineering cannot triage. -->

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | {{functional_requirement_1}} | {{priority}} |
