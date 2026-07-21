---
title: "{{product_name}} Product Backlog"
product: "{{product_name}}"
product_owner: "{{product_owner}}"
last_refined: "{{date}}"
status: "{{status}}"
doc_type: product-backlog
size: lean
source_template: product-backlog
source_template_version: 0.1.0
---

<!--
LEAN PRODUCT BACKLOG. The smallest backlog that is still a real backlog: a goal, an ordered list of work,
the reason it is in that order, and a way to keep the top of the list sprint-ready. Use it for a single
team with one clear goal. To grow it into a full backlog (see product-backlog_template-full.md), ADD
sections; never rename or reorder the ones below, because the full variant is a strict superset of this one.

A PRODUCT BACKLOG IS A LIVING DOCUMENT, NOT A ONE-TIME DELIVERABLE. Unlike a PRD or a design doc, this is
never "done." Re-order it as you learn, refine the top continuously, and DELETE aggressively: a backlog
that only grows becomes a graveyard nobody trusts. Keep the last-refined date current.

WHAT A PRODUCT BACKLOG IS, AND IS NOT
It is the single ordered list the team draws its work from, in service of a Product Goal. It is NOT a
roadmap (that is strategic and outcome-focused; this is tactical and output-focused), NOT a requirements
document to complete, and NOT a wish list. If it has no goal above it, it is a feature factory with a sort
order. See product-backlog_companion.md sections 1 and 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   product-backlog_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid. For the table, PRIORITY explains the column legend and ROW HINT says
   what a good row contains.
2. Replace each {{placeholder}} with your content. The Backlog Items table is the heart; fill it top-down.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This document is never finished, but before you share it: self-grade against product-backlog_guide.md,
   then DELETE every HTML comment. They are guidance, not content.
-->

# {{product_name}} Product Backlog

## Product Goal

<!-- WHAT  The one measurable objective this backlog currently serves: a future state of the product the
           team is working toward. One goal at a time.
     WHY   Without a goal above it, an ordered list of features is just a feature factory with a sort
           order. The goal is the backlog's filter: an item that does not help meet it does not belong.
           Deep dive: product-backlog_companion.md section 3 (Anatomy > Product Goal).
     ASK   What future state of the product are we working toward? How will we measure it? Over what
           horizon (weeks to a few months)? What would let us declare it met or abandon it?
     GOOD  "Cut the median time from opening a report to acting on it by 30% for recurring analysts, by
           the end of Q3, measured on the Time to Insight panel."
     WEAK  "Ship more features and improve the dashboard." (not a measurable future state; nothing to
           order the backlog against)
     TRAP  Listing several goals at once. Scrum keeps one Product Goal in play; the team fulfills or
           abandons it before taking on the next. Many goals means no goal. -->

{{product_goal}}

## Backlog Items

<!-- WHAT  The ordered list of work, top to bottom, most valuable and most refined at the top. Items are
           typed (story, bug, tech, spike). Top items are small and sprint-ready; lower items are coarse.
     WHY   This is the backlog. Its order is the Product Owner's core decision, and its shape should follow
           the iceberg: a small, detailed, sprint-ready tip over larger, vaguer items below the waterline.
           Deep dive: product-backlog_companion.md section 3 (Anatomy > Backlog Items).
     ASK   What is the ordered work? What type is each item? What value or problem does each serve? What is
           the rough estimate? Are the top items small enough to finish in one sprint?
     PRIORITY  The Rank column is the order itself (1 = next). Keep it a true total order, not ties.
     ROW HINT  A good row: a rank, a short item title, a type, the value or problem it serves (not just a
           feature name), a rough estimate (top items only), and a status. Detail the top; leave the bottom
           coarse.
     GOOD  | 1 | Save current view as a named view | story | Recurring analysts stop rebuilding filters | 5 | Ready |
     WEAK  | 1 | Views | task | (no value stated, untyped work, no estimate; nobody can pull this) | | |
     TRAP  Detailing every item to the bottom. Refining work you may never build wastes effort and
           pretends at certainty you do not have. Refine the top; keep the rest coarse. -->

| Rank | Item | Type | Value / problem it serves | Estimate | Status |
|---|---|---|---|---|---|
| {{rank}} | {{item_title}} | {{item_type}} | {{item_value}} | {{estimate}} | {{item_status}} |

## Ordering Rationale

<!-- WHAT  How the list is ordered and why: the principle behind the sequence, in a sentence or two.
     WHY   Stating the ordering principle makes the order reviewable rather than arbitrary, and it is what
           separates a real backlog from a pile sorted by whoever pushed hardest. Deep dive:
           product-backlog_companion.md section 3 (Anatomy > Ordering Rationale).
     ASK   What do you order by (value, risk, learning, dependencies)? What goes first, and why? When two
           items compete, how do you break the tie?
     GOOD  "Ordered by risk and learning first (a spike to de-risk the sharing model leads), then by value
           toward the goal, respecting dependencies (storage before sharing)."
     WEAK  "Ordered by priority." (says nothing; every backlog claims to be ordered by priority)
     TRAP  Ordering purely by raw value and ignoring dependencies and risk, so a high-value item stalls
           because the low-value work it depends on was buried. "Ordered" beats "prioritized" for exactly
           this reason. -->

{{ordering_rationale}}

## Refinement and Readiness

<!-- WHAT  How the backlog is kept refined, and what makes an item ready to pull into a sprint. Cadence,
           who refines, and a lightweight readiness bar.
     WHY   A backlog is only useful if its top is continuously kept sprint-ready; refinement is an ongoing
           team activity, not a pre-planning panic. Keep readiness a light heuristic, not a stage-gate.
           Deep dive: product-backlog_companion.md section 3 (Anatomy > Refinement and Readiness).
     ASK   How often do you refine, and who takes part? What is the lightweight bar for "ready" (clear,
           testable, small enough for one sprint)? How do you keep the backlog from bloating?
     GOOD  "Refined continuously, roughly 10% of each sprint, as a team. An item is ready when it is clear,
           has acceptance criteria, and fits in one sprint. We archive anything untouched for two quarters."
     WEAK  "We groom the backlog before each sprint." (no readiness bar, no anti-bloat practice, and
           refinement crammed into one meeting)
     TRAP  A heavy Definition of Ready enforced as a checklist bouncer. A rigid readiness gate reintroduces
           the phase-gate bureaucracy agile removed; keep it a heuristic, not a wall. -->

{{refinement_and_readiness}}
