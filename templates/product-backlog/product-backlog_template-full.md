---
title: "{{product_name}} Product Backlog"
product: "{{product_name}}"
product_owner: "{{product_owner}}"
last_refined: "{{date}}"
status: "{{status}}"
related: ["{{related_docs}}"]
doc_type: product-backlog
size: full
source_template: product-backlog
source_template_version: 0.1.0
---

<!--
FULL PRODUCT BACKLOG. Every section, for a backlog that earns the weight: multiple teams or stakeholders
disputing the order, real cross-team dependencies, or a list large enough that its health must be measured.
Most single teams do not need this; reaching for it by reflex builds a bureaucracy around a list you could
order by conversation.

The full variant is a strict superset of the lean one: the shared sections keep their names and order, and
this file only ADDS (Prioritization Framework, Dependencies and Risks, Backlog Health and Metrics), plus a
richer Backlog Items table.

A PRODUCT BACKLOG IS A LIVING DOCUMENT, NOT A ONE-TIME DELIVERABLE. It is never "done." Re-order as you
learn, refine the top continuously, and DELETE aggressively. Keep the last-refined date current.

WHAT A PRODUCT BACKLOG IS, AND IS NOT
It is the single ordered list the team draws its work from, in service of a Product Goal. It is NOT a
roadmap (strategic, outcome-focused) and NOT a requirements document to complete. See
product-backlog_companion.md sections 1 and 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   product-backlog_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid. For tables, PRIORITY explains the legend and ROW HINT says what a good
   row contains.
2. Replace each {{placeholder}} with your content. The Backlog Items table is the heart.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This document is never finished, but before you share it: self-grade against product-backlog_guide.md,
   then DELETE every HTML comment.
-->

# {{product_name}} Product Backlog

## Product Goal

<!-- WHAT  The one measurable objective this backlog currently serves: a future state of the product the
           team is working toward. One goal at a time.
     WHY   Without a goal above it, an ordered list of features is just a feature factory with a sort
           order. The goal is the backlog's filter: an item that does not help meet it does not belong.
           Deep dive: product-backlog_companion.md section 3 (Anatomy > Product Goal).
     ASK   What future state of the product are we working toward? How will we measure it? Over what
           horizon? What would let us declare it met or abandon it?
     GOOD  "Cut the median time from opening a report to acting on it by 30% for recurring analysts, by
           the end of Q3, measured on the Time to Insight panel."
     WEAK  "Ship more features and improve the dashboard." (not a measurable future state)
     TRAP  Listing several goals at once. Scrum keeps one Product Goal in play; many goals means no goal. -->

{{product_goal}}

## Backlog Items

<!-- WHAT  The ordered list of work, top to bottom, most valuable and most refined at the top, each item
           typed (story, bug, tech, spike). Top items are small and sprint-ready; lower items are coarse.
     WHY   This is the backlog. Its order is the Product Owner's core decision, and its shape follows the
           iceberg: a small, detailed, sprint-ready tip over larger, vaguer items below the waterline. The
           full table adds an ID (for dependencies), a priority signal, and a depends-on column. Deep
           dive: product-backlog_companion.md section 3 (Anatomy > Backlog Items).
     ASK   What is the ordered work? What type and ID is each item? What value or problem does each serve?
           What is the estimate? What does each depend on? Are the top items sprint-ready?
     PRIORITY  Rank is the order itself (1 = next). The Priority column is an optional signal from your
           framework (e.g. MoSCoW Must/Should/Could, or a WSJF/RICE score); it informs the order but the
           Rank is the decision. See the Prioritization Framework section.
     ROW HINT  A good row: a rank, a stable ID, a short title, a type, the value or problem it serves, a
           priority signal, a rough estimate (top items), what it depends on, and a status.
     GOOD  | 1 | SV-3 | Save current view as a named view | story | Must | Analysts stop rebuilding filters | 5 | SV-1 | Ready |
     WEAK  | 1 | | Views | task | | (no value, no ID, no type discipline; unpullable) | | | |
     TRAP  Detailing every item to the bottom. Refine the top; keep the rest coarse. Refining work you may
           never build is waste dressed as diligence. -->

| Rank | ID | Item | Type | Priority | Value / problem it serves | Estimate | Depends on | Status |
|---|---|---|---|---|---|---|---|---|
| {{rank}} | {{item_id}} | {{item_title}} | {{item_type}} | {{item_priority}} | {{item_value}} | {{estimate}} | {{item_depends_on}} | {{item_status}} |

## Ordering Rationale

<!-- WHAT  How the list is ordered and why: the principle behind the sequence.
     WHY   Stating the ordering principle makes the order reviewable rather than arbitrary. Deep dive:
           product-backlog_companion.md section 3 (Anatomy > Ordering Rationale).
     ASK   What do you order by (value, risk, learning, dependencies)? What goes first, and why? How do you
           break ties?
     GOOD  "Ordered by risk and learning first (a spike to de-risk sharing leads), then by value toward the
           goal, respecting dependencies (storage before sharing)."
     WEAK  "Ordered by priority." (says nothing)
     TRAP  Ordering purely by raw value and ignoring dependencies and risk. "Ordered" beats "prioritized"
           for exactly this reason. -->

{{ordering_rationale}}

## Refinement and Readiness

<!-- WHAT  How the backlog is kept refined, and what makes an item ready to pull into a sprint: cadence,
           who refines, and a lightweight readiness bar.
     WHY   A backlog is only useful if its top is continuously kept sprint-ready; refinement is an ongoing
           team activity, not a pre-planning panic. Keep readiness light. Deep dive:
           product-backlog_companion.md section 3 (Anatomy > Refinement and Readiness).
     ASK   How often do you refine, and who takes part? What is the lightweight bar for "ready"? How do you
           keep the backlog from bloating?
     GOOD  "Refined continuously, roughly 10% of each sprint, as a team. Ready = clear, has acceptance
           criteria, fits one sprint. Archive anything untouched for two quarters."
     WEAK  "We groom before each sprint." (no readiness bar, no anti-bloat practice)
     TRAP  A heavy Definition of Ready enforced as a checklist bouncer, which reintroduces phase-gate
           bureaucracy. Keep it a heuristic. -->

{{refinement_and_readiness}}

## Prioritization Framework

<!-- WHAT  The explicit method, if any, the team uses to inform ordering (MoSCoW, WSJF, RICE, cost of
           delay), and how its output feeds the Rank. State the method and how you apply it.
     WHY   A framework makes trade-offs legible when the order is disputed or the list is too big to
           sequence by feel; but no framework is gospel, and the Rank stays a decision, not a formula
           output. Deep dive: product-backlog_companion.md section 3 (Anatomy > Prioritization Framework)
           and the debate in section 6.
     ASK   Do you use a framework, and which one? Why that one for this context? How does its score inform
           (not replace) the order? Who scores, and how often?
     GOOD  "MoSCoW for stakeholder alignment on the current goal, then WSJF within the Should tier to
           sequence time-sensitive work. Scores inform Rank; the PO owns the final order."
     WEAK  "We use RICE." (names a framework but not why, nor how it feeds the order; and RICE ignores time
           sensitivity, which may matter here)
     TRAP  Treating one framework as gospel and letting its score override judgment. The framework informs
           the order; it does not make the decision, and Must-inflation or ignored cost-of-delay will
           quietly corrupt it. -->

{{prioritization_framework}}

## Dependencies and Risks

<!-- WHAT  The cross-item and cross-team dependencies, and the risks, that shape the order. What blocks
           what, and which assumptions must be retired early.
     WHY   Dependencies are a primary reason "ordered" beats "prioritized": a high-value item that depends
           on a low-value one forces the low-value item up. Making them explicit keeps the backlog honest
           at scale. Deep dive: product-backlog_companion.md section 3 (Anatomy > Dependencies and Risks).
     ASK   Which items block which? What external dependencies (another team, a vendor) gate items? Which
           risky assumptions should a spike retire early? What could invalidate a chunk of the backlog?
     GOOD  "SV-4 (share a view) depends on SV-1 (storage) and on the Platform permissions service (external,
           confirmed). Risk: the sharing permission model is unproven, so SV-2 (spike) is ranked first."
     WEAK  "Some items depend on other items." (names no specific dependency or owner)
     TRAP  Leaving dependencies implicit, so the order looks value-optimal on paper but stalls in practice
           when a top item waits on buried work. -->

{{dependencies_and_risks}}

## Backlog Health and Metrics

<!-- WHAT  The signals that the backlog is a tool and not a graveyard: its size, the age of its items, how
           far down items actually get pulled from, and the archive/prune practice.
     WHY   Backlog bankruptcy is real and measurable: most backlogs bloat to multi-year lists where most
           items never ship. Measuring health is how you justify aggressive deletion. Deep dive:
           product-backlog_companion.md section 3 (Anatomy > Backlog Health and Metrics).
     ASK   How big is the backlog? How old are the oldest items near the top? How deep do you actually pull
           from? What is your archive rule? Is the list still orderable by a human?
     GOOD  "68 active items; nothing above Rank 20 older than one quarter; we pull from the top ~15. Archive
           rule: anything untouched two quarters moves to someday-maybe, recoverable but out of the way."
     WEAK  "The backlog has a lot of items." (no size, age, or pull-depth signal; no archive practice)
     TRAP  Letting the backlog only grow. An item you will realistically never reach is not an asset; it is
           lost focus. Archive is recoverable; focus is not. -->

{{backlog_health_and_metrics}}
