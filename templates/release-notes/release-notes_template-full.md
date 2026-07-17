---
title: "{{product}} {{version}}"
doc_type: release-notes
size: full
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
FULL RELEASE NOTES. The customer-facing announcement plus the developer-facing record: highlights,
the full set of change types (aligned to Keep a Changelog), breaking changes with upgrade steps,
security, and known issues. A strict superset of the lean notes: every lean section appears here
unchanged in name and order, and this file only adds sections between and after them. Use it for a
major release, a release with breaking changes, or notes that double as the permanent changelog
entry. Default to the lean notes and scale up only when a section here earns its place.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   release-notes_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. Do not pre-fill a section out of diligence. Add a full-only section the moment it has real content
   (a behavior changed, something was deprecated, a breaking change needs upgrade steps). If a
   section does not apply, write "None in this release" and one line of why.
4. FIRST RELEASE? Delete Improved, Fixed, Changed, Deprecated, Removed, and Breaking changes rather
   than filling them. Every one is defined against a previous release, and a 0.1.0 has none:
   everything you shipped is New. "None in this release" under all six reads as a product that
   improved nothing and fixed nothing, which is false about the work. This is the one case where rule
   3 does not apply. Summary, Highlights, New, Security, and Known issues all still earn their place.
   (Keep a Changelog treats a first release as entirely "Added"; same logic.) If your project has had
   real users on an untagged main for a while, you may keep the comparative sections and describe
   what changed FOR THEM since they last pulled: say so in the Summary, so the reader knows what
   "improved" is measured against.
5. Before you ship: self-grade against release-notes_guide.md, then DELETE every HTML comment.
-->

# {{product}} {{version}}

<!-- WHAT  The product name, version, and release date, plus whether the project follows a stated
           versioning scheme (SemVer, semver.org).
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

## Highlights

<!-- WHAT  The two or three changes worth calling out above everything else, for readers who scan only
           this section.
     WHY   Most readers scan; give them the headline. If everything is a highlight, nothing is. Deep
           dive: release-notes_companion.md section 3 (Anatomy > Highlights).
     ASK   If the reader reads only this, what must they know? Which two or three changes carry the
           release? Have you resisted listing everything?
     GOOD  "**Saved Views**: stop rebuilding your filters every morning. Save them once, reopen in a
           click, and set a default per dashboard."
     WEAK  A list of ten "highlights" covering every change in the release. (nothing stands out)
     TRAP  Listing everything as a highlight, which highlights nothing. -->

- {{highlight_1}}

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

## Changed

<!-- WHAT  Changes to existing behavior that are not purely improvements and that a user or integrator
           must be aware of (changed defaults, altered behavior). Distinct from breaking changes below.
     WHY   Silent behavior changes break integrations and trust. Deep dive:
           release-notes_companion.md section 3 (Anatomy > Changed).
     ASK   What behavior is now different? Who relied on the old behavior? How do they keep it if they
           need to?
     GOOD  "The dashboard now remembers your last view per dashboard. If you relied on dashboards
           always opening in the generic default state, set your default view to 'none' to keep it."
     WEAK  "Adjusted some default settings." (an integrator cannot tell what changed or if it affects
           them)
     TRAP  Silently changing behavior and surprising integrators who depended on the old default. -->

- {{change_1}}

## Deprecated

<!-- WHAT  Features now marked for future removal, with the timeline and the recommended alternative.
     WHY   A deprecation without a migration path and a date is just a threat. Deep dive:
           release-notes_companion.md section 3 (Anatomy > Deprecated).
     ASK   What is being deprecated? What should users move to instead? By which version or date is it
           removed?
     GOOD  "The legacy 'pinned filter' feature is deprecated in favor of Saved Views and will be
           removed in 3.0.0. Pinned filters are importable as views from the Views menu."
     WEAK  "Pinned filters are deprecated." (no alternative and no removal date; the user is left
           stranded)
     TRAP  Deprecating without naming the alternative or the removal date. -->

- {{deprecation_1}}

## Removed

<!-- WHAT  Features removed in this release (often previously deprecated). If nothing was removed, say
           so explicitly rather than dropping the section.
     WHY   Removing something users depended on with no prior notice breaks them. Deep dive:
           release-notes_companion.md section 3 (Anatomy > Removed).
     ASK   What was removed? Was it deprecated first, with notice? What replaces it?
     GOOD  "None in this release." (nothing was removed; state it rather than omitting the section)
     WEAK  Quietly dropping the legacy export API with no deprecation notice and no mention here.
     TRAP  Removing something users depended on with no prior deprecation notice. -->

- {{removal_1}}

## Security

<!-- WHAT  Security fixes and advisories, with severity and any required user action.
     WHY   A security fix deserves its own visibility; do not bury it in "Fixed." Deep dive:
           release-notes_companion.md section 3 (Anatomy > Security).
     ASK   What was the issue or hardening? What severity? What must the user do, if anything?
     GOOD  "Shared views enforce per-recipient permissions: a shared view never exposes data the
           recipient could not already access on that dashboard. No action required (informational)."
     WEAK  "Fixed a security bug." (no severity, no affected versions, no required action)
     TRAP  Burying a security-relevant fix in the generic "Fixed" list, with no severity. -->

- {{security_note_1}}

## Breaking changes and upgrade notes

<!-- WHAT  Anything that requires action to upgrade safely: API or contract changes, migrations,
           config changes, and the exact steps to take.
     WHY   In SemVer, breaking changes drive a major version bump; every one needs a concrete upgrade
           path. Deep dive: release-notes_companion.md section 3 (Anatomy > Breaking changes and
           upgrade notes).
     ASK   What will break on upgrade? Who is affected? What are the exact steps to upgrade safely?
     GOOD  "None. Saved Views is additive and behind no required migration. Existing dashboards and
           bookmarks continue to work unchanged."
     WEAK  "Some APIs changed; update accordingly." (names no API and gives no upgrade steps)
     TRAP  A breaking change with no upgrade path (a hidden breaking change). -->

{{breaking_changes_and_upgrade_notes}}

## Known issues

<!-- WHAT  Problems shipping in this release, with workarounds and expected fix timing.
     WHY   Transparency here builds trust; users prefer knowing in advance. Deep dive:
           release-notes_companion.md section 3 (Anatomy > Known issues).
     ASK   What known problems ship in this release? Is there a workaround? When is the fix expected?
     GOOD  "A view that references a filter you later delete loads the still-valid filters and shows a
           notice naming the missing one; re-saving the view clears it. A fix is planned for 2.4.1."
     WEAK  An empty Known issues section on a release that has them. (users hit problems unprepared)
     TRAP  Omitting known problems so users hit them unprepared. -->

- {{known_issue_1}}
