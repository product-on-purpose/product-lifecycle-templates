---
title: "Release notes"
description: "One published release note per tagged version, each written by filling this library's own release-notes template"
audience: "both"
level: "beginner"
tags:
  - releases
  - changelog
---

# Release notes

One page per tagged release. Each is a **filled instance of this library's own
[`release-notes` bundle](../../templates/release-notes/)**, not a hand-rolled format: the library
dogfoods the template it ships, which is why these pages carry `source_template` and
`source_template_version` in their frontmatter.

For the full, unabridged history including unreleased work, read
[`CHANGELOG.md`](../../CHANGELOG.md). These pages are the curated read; the changelog is the record.
The process that produces them is [`release-process.md`](../internal/release-process.md).

## Inventory

- [`v0.1.0.md`](v0.1.0.md) - the first tagged release: four bundles and the governance gate that admits them
- [`v0.2.0.md`](v0.2.0.md) - the Tier-1 floor completed, and the library's first user-facing documentation
- [`v0.2.1.md`](v0.2.1.md) - a listing-contract patch: `v0.2.0` was tagged before its downstream contract was read, and a published tag is not moved. **Backfilled 2026-08-09**
- [`v0.3.0.md`](v0.3.0.md) - Gold tier measured in CI, the pilot's held-out finding withdrawn, and two install defects found by running the install
- [`v0.3.1.md`](v0.3.1.md) - a documentation patch: the `v0.3.0` tag shipped four documents denying the efficacy evaluations that shipped beside them

**Every tagged release now has a page**, which was not true until 2026-08-09. `v0.2.1` shipped without one
and the gap sat unnoticed because nothing checks it:
[`release-process.md`](../internal/release-process.md) names a release note as one of **four** required
artifacts per release, and no CI step reads that rule. The backfilled page is dated as backfilled and says
so on its own face, rather than being presented as contemporaneous.
