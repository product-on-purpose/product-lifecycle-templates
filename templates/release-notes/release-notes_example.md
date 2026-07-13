---
title: "Acme Analytics 2.4.0"
doc_type: release-notes
size: full
owner: "Priya Nair (PM, Reporting)"
status: approved
doc_version: "2.4.0"
created: "2026-06-29"
updated: "2026-06-30"
related_links:
  - "PRD: Saved Views for Dashboards (prd_example.md)"
source_template: release-notes
source_template_version: 0.1.0
---

<!--
Worked example for the Release Notes bundle. Full release notes announcing the "Saved Views" feature
(from the PRD, story, and acceptance-criteria examples) shipping in a fictional Acme Analytics 2.4.0.
"Acme Analytics" and all figures are illustrative.
-->

# Acme Analytics 2.4.0

Release date: 2026-06-30. Acme Analytics follows Semantic Versioning.

## Summary

This release introduces Saved Views, so you can capture a dashboard's filters once and reopen them in a
click, and improves dashboard load time.

## Highlights

- **Saved Views**: stop rebuilding your filters every morning. Save them once, reopen in a click, and
  set a default per dashboard.

## New

- **Saved Views**: Save a dashboard's filters, date range, and visible columns as a named view, reopen it
  in one click, set one view as your default for a dashboard, and share a view with your team. If you
  check the same slice of data every day, you no longer rebuild it each time.

## Improved

- Dashboards now load noticeably faster on large datasets (illustrative: about 30 percent faster at p95).

## Fixed

- Fixed an issue where the date-range picker occasionally reset to "last 7 days" after switching tabs.
- Fixed a misaligned column header on narrow screens.

## Changed

- The dashboard now remembers your last view per dashboard. If you previously relied on dashboards always
  opening in the generic default state, set your default view to "none" to keep that behavior.

## Deprecated

- The legacy "pinned filter" feature is deprecated in favor of Saved Views and will be removed in 3.0.0.
  Pinned filters are automatically importable as views from the Views menu.

## Removed

- None in this release.

## Security

- Shared views enforce per-recipient permissions: a shared view never exposes data the recipient could
  not already access on that dashboard. No action required (informational).

## Breaking changes and upgrade notes

- None. Saved Views is additive and behind no required migration. Existing dashboards and bookmarks
  continue to work unchanged.

## Known issues

- A view that references a filter you later delete will load the still-valid filters and show a notice
  naming the missing one; re-saving the view clears the notice. A fix to prompt re-save automatically is
  planned for 2.4.1 (illustrative).
