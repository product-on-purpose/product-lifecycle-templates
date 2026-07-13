<!--
SAMPLE: Approach B (visible on-page scaffolding). Open in a Markdown preview to see how it
renders: the guidance blockquotes stay visible until the author deletes them. This file shows
three PRD sections only. Not a shipping template.
-->

# {{title}}

## Summary

> **Fill in:** what is it, who is it for, and the single outcome it produces? One paragraph.
> **Strong:** "Saved Views lets an analyst capture a dashboard's filters as a named, reopenable
>   view, so they spend time reading data, not rebuilding the lens to see it."
> **Weak:** "We will add a Views menu with a dropdown and a save button." (mechanics, not outcome)
> **Why / deep dive:** [companion section 1 (Orientation)](../prd/prd_companion.md#1-orientation).
> _Delete this block before shipping._

{{summary}}

## Problem

> **Fill in:** who hits this, how often, what it costs them, and why solve it now?
> **Strong:** "Analysts who monitor the same slice re-apply filters several times a day; in a
>   12-person study, 9 rebuilt filters daily and 3 kept a text file of the ones they always use."
> **Weak:** "Users cannot save filters." (a missing feature, not the problem beneath it)
> **Why / deep dive:** [companion section 3 (Anatomy > Problem)](../prd/prd_companion.md#3-anatomy-section-by-section).
> _Delete this block before shipping._

{{problem}}

## Functional requirements

> **Fill in:** one verifiable behavior per row, each prioritized. Could QA write a test from it?
> **Priority (MoSCoW):** Must (ship-blocking) / Should / Could / Won't (out this release).
> **Strong row:** `| FR-1 | Save the current dashboard state as a named view | Must |`
> **Weak row:** `| FR-1 | Add a dropdown to the toolbar | Must |` (UI detail, not testable)
> **Trap:** many equally-weighted requirements with no priority. _Delete this block before shipping._

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | {{functional_requirement_1}} | {{priority}} |
