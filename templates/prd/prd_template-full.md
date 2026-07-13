---
title: "{{title}}"
doc_type: prd
size: full
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
FULL PRD. The comprehensive variant, and a strict superset of the lean PRD: every lean section
appears here unchanged in name and order, and this file only adds sections between them. Use it for
a multi-team initiative, a regulated context, or anything where the cost of a misunderstanding is
high. Default to the lean variant and scale up only when a section here earns its place.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   prd_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK example,
   and the TRAP to avoid.
2. Replace each {{placeholder}} with your content. For tables, follow the ROW HINT.
3. Do not pre-fill a section out of diligence. Add a full-only section the moment a real question it
   answers comes up (a dependency appears, an NFR gets contested, a rollout needs a flag). If a
   section does not apply, write "N/A" and one line of why.
4. Before you ship: self-grade against prd_guide.md, then DELETE every HTML comment.
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

## Context and background

<!-- WHAT  Why this, why now. The strategic thread the work hangs from (the goal, OKR, or bet it
           serves), relevant history, and what changed to make it timely.
     WHY   Without it, reviewers cannot judge whether the work should be built at all, only whether
           it is well-described. Deep dive: prd_companion.md section 3 (Anatomy > Context).
     ASK   What goal or bet does this serve? What changed to make now the right time?
     GOOD  "Serves the FY26 Time to Insight goal; the 2026-05 friction study reframed re-filtering
           from a feature gap to a recurring time tax. Nothing in the data model blocks it now that
           per-user preferences shipped in Q1."
     WEAK  A description of the feature with no link to any strategy.
     TRAP  A PRD that cannot name the strategy it serves is a candidate to kill, not to refine. -->

{{context_and_background}}

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
           deliberately NOT doing.
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

<!-- WHAT  The specific segments, roles, or personas this serves, and the context they are in when
           they hit the problem. Reference a persona artifact if one exists.
     WHY   Design and tradeoffs depend on knowing the user; name the primary user when segments
           conflict. Deep dive: prd_companion.md section 3 (Anatomy > Target users).
     ASK   Which specific user? In what situation do they hit the problem? Who is this NOT for?
     GOOD  "Primary: the Recurring Analyst who returns to the same dashboards daily within a stable
           filter set. Secondary: the Team Lead. Not optimized for the one-time explorer."
     WEAK  "All users."
     TRAP  "All users" - if it is for everyone, it is designed for no one. -->

{{target_users}}

## Solution overview

<!-- WHAT  The proposed solution at a high level: the core idea and how a user experiences it. Link
           the prototype or high-fidelity mockup.
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

## User stories

<!-- WHAT  The work expressed as user-centered stories ("As a [user], I want [goal], so that
           [benefit]"), grouped by theme or flow.
     WHY   It keeps requirements anchored to user value and feeds the backlog. Keep acceptance
           criteria out of here; they live in their own artifact (pairs_with deliver-acceptance-
           criteria). Deep dive: prd_companion.md section 3 (Anatomy > User stories).
     ASK   Whose goal is this? What benefit do they get? Is it an outcome, not a UI task?
     GOOD  "As a Recurring Analyst, I want to save my current filters as a named view, so that I can
           return to exactly this slice tomorrow without rebuilding it."
     WEAK  "As a user, I want a dropdown." (a task in disguise, with no benefit)
     TRAP  Stories that are tasks in disguise, or that smuggle in acceptance criteria. -->

- As a {{user}}, I want {{goal}}, so that {{benefit}}.

## Functional requirements

<!-- WHAT  What the system must do, as testable statements, each prioritized.
     WHY   Engineering needs must-have vs nice-to-have to make tradeoffs when time runs short.
           Deep dive: prd_companion.md section 3 (Anatomy > Functional requirements).
     ASK   Is each row one verifiable behavior? Could QA write a test from it as written?
     PRIORITY  MoSCoW: Must (ship-blocking) / Should (important, not blocking) / Could (nice to
               have) / Won't (explicitly out this release).
     ROW HINT  ID = FR-n, stable so acceptance criteria can reference it. Requirement = one
               verifiable behavior, not a UI detail.
     GOOD  | FR-1 | Save the current dashboard state (filters, date range, columns) as a named view | Must |
     WEAK  | FR-1 | Add a dropdown to the toolbar | Must |  (UI detail, not a testable requirement)
     TRAP  A flat list of equally-weighted requirements with no priority; engineering cannot triage. -->

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | {{functional_requirement_1}} | {{priority}} |

## Non-functional requirements

<!-- WHAT  Quality attributes: performance, scalability, security, accessibility, reliability,
           privacy, and any compliance targets, with measurable thresholds.
     WHY   These qualities are expensive to retrofit; the most common production surprise is an NFR
           that was implicit until launch. Deep dive: prd_companion.md section 3 (Anatomy > NFRs).
     ASK   What is the measurable bar for each attribute? How will you verify it?
     ROW HINT  Attribute = the quality; Target = a number or a testable condition, not an adjective.
     GOOD  | Performance | Switching to a saved view renders under 1s at p95 on a standard dashboard |
     WEAK  | Performance | Must be fast |  (no measurable threshold)
     TRAP  Leaving NFRs implicit, then discovering the latency or accessibility bar after launch. -->

| Attribute | Target |
|---|---|
| {{nfr_attribute}} | {{nfr_target}} |

## UX and design

<!-- WHAT  The experience: key flows, all states (empty, loading, error), and edge cases, with links
           to wireframes or the interactive prototype.
     WHY   The unhappy paths are where real work and real bugs live. Deep dive: prd_companion.md
           section 3 (Anatomy > UX and design).
     ASK   What are the key flows? What does empty, loading, error, and each edge case look like?
     GOOD  "Design all states: empty (a one-line prompt explaining views), loading (non-blocking, no
           flash to default), error (a view references a deleted filter: load the valid parts, flag
           the rest), and the permission edge."
     WEAK  Describing the happy path only.
     TRAP  Leaving empty and error states for engineering to invent during build. -->

{{ux_and_design}}

## Success metrics

<!-- WHAT  How you will know it worked: primary metric(s) tied to the goals, a guardrail metric you
           must not harm, and the measurement window.
     WHY   It defines "did it work" before you are emotionally invested in the answer. Define before
           build. Deep dive: prd_companion.md section 3 (Anatomy > Success metrics).
     ASK   What primary number moves if this succeeds? What must NOT get worse? Over what window?
     GOOD  "Primary: median time from dashboard open to first meaningful interaction drops for
           Recurring Analysts. Guardrail: shared-view permission incidents stay at zero. Window:
           4 weeks post-rollout vs the 4 weeks prior."
     WEAK  "Increase pageviews." (a vanity metric that can rise while the user outcome does not)
     TRAP  Defining metrics after results arrive, or picking a vanity metric with no guardrail. -->

- Primary: {{primary_metric}}
- Guardrail: {{guardrail_metric}}
- Measurement window: {{measurement_window}}

## Analytics and instrumentation

<!-- WHAT  The events, properties, and dashboards needed to actually measure the success metrics
           above, and what must be instrumented before launch.
     WHY   Metrics without instrumentation ship blind; if the tracking plan is not in the PRD, the
           launch usually cannot measure its own success criteria.
           Deep dive: prd_companion.md section 3 (Anatomy > Analytics and instrumentation).
     ASK   Which events and properties capture each metric? Which dashboard shows them?
     GOOD  "Instrument view_saved, view_switched, view_set_default, view_shared, view_load_error
           (with reason), each with dashboard ID and view scope; wire the primary metric to the
           Time to Insight panel."
     WEAK  Success metrics defined with no tracking plan to capture the data.
     TRAP  Shipping the launch blind because the events were never instrumented. -->

{{analytics_and_instrumentation}}

## Dependencies

<!-- WHAT  What this depends on to ship: other teams, services, data, approvals, third parties, with
           the status of each.
     WHY   The unwritten dependency is the classic mid-build blocker. Deep dive: prd_companion.md
           section 3 (Anatomy > Dependencies).
     ASK   What must exist or be approved before this can ship? Who owns it? What is its status?
     ROW HINT  Name the dependency, its owner, and a real status (Done / Confirmed / In progress /
               Blocked), not a hope.
     GOOD  | Dashboard permissions service (for shared-view access checks) | Platform | Confirmed, integration pending |
     WEAK  | Permissions | ? | ? |  (no owner, no status)
     TRAP  Discovering a blocking dependency mid-build because it was never written down. -->

| Dependency | Owner | Status |
|---|---|---|
| {{dependency_1}} | {{owner}} | {{status}} |

## Risks and mitigations

<!-- WHAT  What could go wrong (technical, market, adoption, compliance) and how you will reduce or
           detect each.
     WHY   A risk with no mitigation and no owner is decoration, not risk management. Deep dive:
           prd_companion.md section 3 (Anatomy > Risks and mitigations).
     ASK   What could go wrong? How likely, how bad? How will you reduce or detect it?
     ROW HINT  Every risk row needs a concrete mitigation, not "monitor it."
     GOOD  | Shared views leak data via mismatched permissions | Low | High | Per-recipient permission checks at load; security review before GA |
     WEAK  | Something breaks | Medium | High | We will keep an eye on it |
     TRAP  Listing risks with no mitigation or owner. -->

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| {{risk_1}} | {{likelihood}} | {{impact}} | {{mitigation}} |

## Rollout and release plan

<!-- WHAT  How this reaches users: phasing, feature flags, target dates, rollback plan, and the
           comms. Tie to the release-notes and launch-checklist artifacts.
     WHY   How it reaches users is part of what to build. Deep dive: prd_companion.md section 3
           (Anatomy > Rollout and release plan).
     ASK   In what phases? Behind a flag? What is the rollback path? Who is told, and when?
     GOOD  "Phase 1: private views behind a flag, internal dogfood one week. Phase 2: sharing after
           the security review. Phase 3: GA via gradual rollout (10 / 50 / 100 percent). Rollback:
           the flag disables the control and retains saved-view data."
     WEAK  "Turn it on for everyone at launch."
     TRAP  A big-bang launch with no flag and no rollback path. -->

{{rollout_and_release_plan}}

## Open questions

<!-- WHAT  A living list of what is still undecided or unknown. Each row: question, owner, needed-by
           date.
     WHY   Surfaced unknowns are what make a PRD an honest living document rather than a frozen claim
           of certainty. Deep dive: prd_companion.md section 3 (Anatomy > Open questions).
     ASK   What is genuinely undecided? Who owns each answer? By when is it needed?
     GOOD  | What magnitude of time-to-insight gain counts as success? | Priya + Data | Before GA |
     WEAK  An empty table left to look finished.
     TRAP  Hiding unknowns to look more complete; a PRD with no open questions is usually hiding
           them, not finished. -->

| Question | Owner | Needed by |
|---|---|---|
| {{open_question_1}} | {{owner}} | {{date}} |

## Appendix

<!-- WHAT  Supporting material: research links, competitive notes, glossary, prior decisions (ADRs),
           and any detail that would clutter the body.
     WHY   Keeps the body readable without losing the supporting record. Deep dive: prd_companion.md
           section 3 (Anatomy > Appendix).
     ASK   What supporting material do reviewers need available but not inline?
     GOOD  "Discovery readout (friction study, 2026-05); prior decision: per-user preferences storage
           chosen over per-dashboard in Q1 (ADR-014); glossary of 'view'."
     WEAK  Pasting the full research transcript with no structure.
     TRAP  Burying a load-bearing decision here where reviewers miss it. -->

{{appendix}}
