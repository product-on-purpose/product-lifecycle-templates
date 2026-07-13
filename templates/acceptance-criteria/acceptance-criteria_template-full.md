---
title: "{{title}}"
doc_type: acceptance-criteria
size: full
owner: "{{owner}}"
status: draft
doc_version: "{{doc_version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: acceptance-criteria
source_template_version: 0.1.0
---

<!--
FULL ACCEPTANCE CRITERIA. The comprehensive variant, and a strict superset of the lean checklist:
the Story reference, Acceptance criteria, and Out of scope sections appear here unchanged in name and
order, with Scenarios, Edge cases, and Non-functional criteria added between them. Use it for
behavior-heavy, risky, or integration-sensitive stories, and where AC will seed automated tests.
Default to the lean checklist and scale up only when scenarios earn their place.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   acceptance-criteria_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a
   WEAK example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. Do not pre-fill a section out of diligence. Add a full-only section the moment a real question it
   answers comes up (a flow needs scenarios, an edge case bites, a performance bar gets contested). If
   a section does not apply, write "N/A" and one line of why.
4. Before you ship: self-grade against acceptance-criteria_guide.md, then DELETE every HTML comment.
-->

# {{title}}

## Story reference

<!-- WHAT  Which user story or backlog item these criteria gate: a link, or the story statement
           itself. Name the user and the goal.
     WHY   AC are meaningless without the story they accept; "accepted into what" must be
           unambiguous. Deep dive: acceptance-criteria_companion.md section 3 (Anatomy > Story
           reference).
     ASK   Which story do these gate? Is it linked or quoted so a reviewer can find it? Are the user
           and goal clear?
     GOOD  "As a recurring analyst, I want to set one of my saved views as the default for a
           dashboard, so that the dashboard opens the way I work instead of in its generic default
           state. (See user-stories_example.md.)"
     WEAK  "Saved views feature." (no user, no goal, no link; a reviewer cannot tell what is being
           accepted)
     TRAP  Free-floating criteria with no parent story. -->

{{story_reference}}

## Acceptance criteria

<!-- WHAT  The rule-based conditions that must hold for the story to be accepted, as a checklist of
           observable, pass/fail outcomes. Use this for discrete rules; use Scenarios below for flows.
     WHY   Discrete rules are clearest as a list, and each must be markable pass or fail; a criterion
           you cannot mark is not finished. Deep dive: acceptance-criteria_companion.md section 3
           (Anatomy > Acceptance criteria).
     ASK   Is each row a single verifiable claim? Could QA mark it pass or fail as written? Is it what
           the user observes, not how it is built?
     GOOD  "Marking a new view as default un-marks the previous default automatically."
     WEAK  "Defaults are stored efficiently in a Redis cache." (implementation detail, not an
           observable outcome the user can verify)
     TRAP  Implementation, not behavior: criteria that describe how it is built rather than what the
           user can observe. -->

- [ ] {{criterion_1}}
- [ ] {{criterion_2}}

## Scenarios (Given / When / Then)

<!-- WHAT  Behavior expressed as scenarios in Given (context) / When (action) / Then (outcome) form,
           one scenario per distinct behavior.
     WHY   Flows are clearer as scenarios than as rules, and Given/When/Then can double as automated
           tests. Deep dive: acceptance-criteria_companion.md section 3 (Anatomy > Scenarios,
           Given/When/Then).
     ASK   Does each scenario test one behavior? Is "When" a single action? Do Given and Then read as
           precondition and observable outcome?
     GOOD  "Scenario: switching the default. Given 'EMEA, last 30 days' is currently my default, When
           I mark 'APAC, last 7 days' as the default, Then 'APAC, last 7 days' becomes my default and
           'EMEA, last 30 days' is no longer marked default."
     WEAK  "Given I am logged in with saved views, When I save, rename, set a default, and reload,
           Then everything works." (many actions and behaviors in one scenario, no single outcome to
           verify)
     TRAP  Mega-scenario: one Given/When/Then with many "And" steps testing several behaviors at
           once. -->

**Scenario: {{scenario_name}}**
- Given {{context}}
- When {{action}}
- Then {{expected_outcome}}

## Edge cases and negative paths

<!-- WHAT  The unhappy paths the rules and scenarios above do not cover: empty input, permission
           denied, conflict, timeout, missing data.
     WHY   Most production defects live here, not on the happy path; the negative criteria are often
           the most valuable and the most commonly omitted. Deep dive:
           acceptance-criteria_companion.md section 3 (Anatomy > Edge cases and negative paths).
     ASK   What happens on empty, denied, conflicting, or missing input? Which failure would bite a
           real user? Is the recovery behavior specified, not just the failure?
     GOOD  "Given my default view references a filter that has since been deleted, when I open the
           dashboard, then it loads the still-valid filters and shows a clear message naming the
           missing filter, rather than failing to load."
     WEAK  "Handle errors gracefully." (names no specific edge and no observable behavior; cannot be
           marked pass or fail)
     TRAP  Happy path only: no edge or negative cases, so error behavior gets invented during
           build. -->

- [ ] {{edge_case_1}}

## Non-functional criteria

<!-- WHAT  Story-specific quality gates: performance, accessibility, security, or privacy thresholds
           for this story, each with a measurable bar.
     WHY   A story can pass every functional check and still be unacceptable if it is slow or
           inaccessible; keep these story-specific. Deep dive: acceptance-criteria_companion.md
           section 3 (Anatomy > Non-functional criteria).
     ASK   What quality bar is specific to this story? Is each a measurable threshold? Does it belong
           here or in the team-wide Definition of Done?
     GOOD  "Loading a default view on dashboard open completes within 1 second at p95. The 'set as
           default' control is keyboard-operable and screen-reader labeled (WCAG 2.2 AA)."
     WEAK  "Must be fast and accessible." (no measurable threshold; cannot be marked pass or fail)
     TRAP  Duplicating the Definition of Done: restating universal quality bars that apply to every
           story instead of the ones specific to this one. -->

- [ ] {{non_functional_criterion_1}}

## Out of scope and notes

<!-- WHAT  What these criteria deliberately do not cover, plus assumptions and links to adjacent
           stories.
     WHY   It lets a reviewer tell an omission from a decision. Deep dive:
           acceptance-criteria_companion.md section 3 (Anatomy > Out of scope and notes).
     ASK   What did you choose not to cover? What assumptions do the criteria rest on? Where do
           adjacent concerns live?
     GOOD  "Out of scope: team-level defaults (a Team Lead setting a default for everyone) are a
           separate, open decision. Assumes per-user preference storage (shipped Q1). Does not cover
           sharing, which has its own story."
     WEAK  Leaving this blank. (silence on scope makes an omission read as a deliberate decision)
     TRAP  No scope statement, so omissions read as decisions. -->

{{out_of_scope_and_notes}}
