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
- [`v0.3.0.md`](v0.3.0.md) - Gold tier measured in CI, the pilot's held-out finding withdrawn, and two install defects found by running the install
