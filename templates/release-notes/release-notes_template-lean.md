---
title: "{{product}} {{version}}"
doc_type: release-notes
size: lean
owner: "{{owner}}"
status: draft
doc_version: "{{version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: release-notes
source_template_version: 0.1.1
---

<!--
LEAN RELEASE NOTES. The customer-facing announcement: what is new, what got better, what was fixed,
in plain language framed around user benefit. Use this for a routine release. To grow it into full
notes, ADD sections (see release-notes_template-full.md); never rename or reorder the ones below (the
full variant is a strict superset of this one). Write for the user who needs to make sense of the
change, not the team that shipped it.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   release-notes_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, write "None in this release" rather than deleting it.
4. FIRST RELEASE? Delete "Improved" and "Fixed" instead. They are defined against a previous release,
   and a 0.1.0 has none: everything you shipped is New. Writing "None in this release" under them is
   worse than deleting them, because it reads as "we improved nothing and fixed nothing," which is
   false about the work and a bad first impression. This is the one case where rule 3 does not apply.
   (Keep a Changelog treats a first release as entirely "Added"; same logic.) If your project has had
   real users on an untagged main for a while, you may keep both sections and describe what changed
   FOR THEM since they last pulled: say so in the Summary, so the reader knows what "improved" is
   measured against.
5. Before you ship: self-grade against release-notes_guide.md, then DELETE every HTML comment. They
   are guidance, not content.
-->

# {{product}} {{version}}

<!-- WHAT  The product name, version, and release date, plus whether the project follows a stated
           versioning scheme (SemVer).
     WHY   Readers orient on what shipped and when before reading any change. Deep dive:
           release-notes_companion.md section 3 (Anatomy > Release header).
     ASK   What product and version is this? What date did it ship? Do you follow SemVer?
     GOOD  "Release date: 2026-06-30. Acme Analytics follows Semantic Versioning."
     WEAK  "Released this week." (no ISO date, no version scheme; ambiguous across regions)
     TRAP  Non-ISO dates that read differently across regions; use YYYY-MM-DD per Keep a Changelog. -->

## Summary

<!-- WHAT  One or two sentences on what this release is about, in user terms: the headline change and
           who benefits.
     WHY   The summary is the triage surface; a reader decides from it whether to read on. Deep dive:
           release-notes_companion.md section 3 (Anatomy > Summary).
     ASK   What is this release about? What single change matters most? Would a user recognize the
           benefit from this line alone?
     GOOD  "This release introduces Saved Views, so you can capture a dashboard's filters once and
           reopen them in a click, and improves dashboard load time."
     WEAK  "Various bug fixes and improvements." (a summary that tells the reader nothing)
     TRAP  "Various improvements and bug fixes" - a summary that communicates nothing specific. -->

{{summary}}

## New

<!-- WHAT  New capabilities (Keep a Changelog "Added"), each a benefit-led headline with a short
           description. Lead with what the user can now do, not how it was built.
     WHY   Readers check "what's new" first; this is the section that earns adoption. Deep dive:
           release-notes_companion.md section 3 (Anatomy > New).
     ASK   What can the user now do that they could not before? What is the benefit in their words?
           Have you led with the outcome, not the implementation?
     GOOD  "**Saved Views**: Save a dashboard's filters, date range, and visible columns as a named
           view, reopen it in one click, set one as your default, and share it with your team."
     WEAK  "Implemented enhanced data persistence layer for improved throughput." (implementation
           language; the user cannot tell what changed for them)
     TRAP  Written for the shipper: implementation detail instead of user benefit. -->

- **{{feature_headline}}**: {{benefit_description}}

## Improved

<!-- WHAT  Enhancements to existing functionality (Keep a Changelog "Changed", the user-positive
           subset): speed, workflow, UI. Frame as the impact the user feels.
     WHY   It shows responsiveness to user needs; state the impact, not the internal change that
           produced it. Deep dive: release-notes_companion.md section 3 (Anatomy > Improved).
     ASK   What got better for the user? Can you state it as impact ("twice as fast")? Would the user
           recognize the thing you named?
     GOOD  "Dashboards now load noticeably faster on large datasets (illustrative: about 30 percent
           faster at p95)."
     WEAK  "Optimized the query execution planner." (an internal component name the user has never
           heard, with no stated impact)
     TRAP  Naming the internal change instead of the impact the user feels. -->

- {{improvement_1}}

## Fixed

<!-- WHAT  Resolved issues in plain language: what the user experienced before versus what happens
           now. Frame positively (what now works), but honestly.
     WHY   Users want to know their specific pain is gone, in terms they recognize. Deep dive:
           release-notes_companion.md section 3 (Anatomy > Fixed).
     ASK   What did the user experience before? What happens now? Is it stated in user terms, not bug
           IDs?
     GOOD  "Fixed an issue where the date-range picker occasionally reset to 'last 7 days' after
           switching tabs."
     WEAK  "Fixed BUG-4821, BUG-4822, BUG-4830." (raw bug IDs with no user-facing meaning)
     TRAP  Dumping raw bug IDs or commit messages with no user-facing meaning (the git-log dump). -->

- {{fix_1}}
