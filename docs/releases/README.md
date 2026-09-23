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

**Newest first**, matching [`RELEASE-NOTES.md`](../../RELEASE-NOTES.md). Stated because it was not: entries through `v0.7.0` were appended in ascending order and everything from `v0.8.0` was inserted at the top, so the list disagreed with itself for four releases.

- [`v0.12.0.md`](v0.12.0.md) - a 31st bundle, the launch coordination checklist: the standing list a team consults before it ships an externally visible change. Admitted on a source retrieved while its spec was written, Appendix E of Google's *Site Reliability Engineering* book, which is licensed no-derivatives, so the bundle teaches the practice around that list and adapts none of its items. Every quotation in its research log was checked against the source's raw text, and 19 of 193 were not there
- [`v0.11.2.md`](v0.11.2.md) - a correctness patch. The build-cost reports `v0.11.0` shipped counted every API response two or three times, because the harness writes one transcript record per content block and each repeats the whole usage block. Recounted from the same transcripts with attribution unchanged, a whole build is about 10M to 12M weighted token-equivalents, not 21M to 25M, and every report now also states its cost at API list rates: $33 to $41 for a whole build. Every document that quoted the old figures is corrected, ADR 0056 carries a dated Correction, and the shipped `v0.11.0` pages are left as they were with a pointer here
- [`v0.11.1.md`](v0.11.1.md) - a documentation and correctness patch. The library had published a website and never told a human reader it exists: no link, no explanation, no how-to anywhere a human would look. Also corrects a reason this repository stated for a decision and had wrong, finishes an ADR cleanup that had missed the two most visible surfaces in the project, and records the decision `v0.11.0` shipped without
- [`v0.11.0.md`](v0.11.0.md) - what a bundle costs to build is measured rather than estimated, and the two estimates it replaces were wrong by between 20 and 30 times. The harness had been writing a full usage block on every subagent turn since the beginning and nothing had ever read one. Measured, a bundle costs 21M to 25M weighted token-equivalents, and drafting rather than research is the largest single stage, which is the opposite of what the runbook assumed. 22 reports backfilled into `bundle-builds/`, and four stale claims corrected on the way. *Its cost figures were about twice the truth, from a generator that counted each API response two to three times; corrected in [`v0.11.2`](v0.11.2.md).*
- [`v0.10.0.md`](v0.10.0.md) - the MCP server becomes usable from a clone and speaks a typed response envelope. It could not start from a `git clone` and had not since it shipped, because `.mcp.json` used a variable Claude Code sets only for plugin installs; the server itself was fine the whole time, which is why every check passed. All five tools now return `{ok, data?, error?}` as `structuredContent`, a breaking change taken while nothing external calls the server. The zero-fills disclosure is retired, and the ban on calling a bundle proven is kept
- [`v0.9.0.md`](v0.9.0.md) - the library gets a website. All 30 bundles are readable at a URL, generated from the tree with nothing hand-listed, and five guards run between `astro build` and the upload so the artifact that is checked is the artifact that ships. The edit-link guard found a live 404 on its first run against a real build, which no build and no CI run could have caught. Also closes two decisions open since 2026-09-11 and 2026-09-12
- [`v0.8.0.md`](v0.8.0.md) - three new bundles and a fourth document type refused on its own evidence, plus the first admission rulings this library wrote down BEFORE building on them. Two of the three teach a dispute rather than a settled practice: the spike report's own canon argues against writing one, and the test summary report's governing standard was the subject of a campaign to withdraw it
- [`v0.7.0.md`](v0.7.0.md) - the release that carries the MCP install fix to anyone who had it broken, the `--require-sdk` flag that makes a CI check able to fail, an open pull queue with a page that states the build order is one person's preference, and nine claims this repository made about itself that had aged into being false
- [`v0.6.0.md`](v0.6.0.md) - an MCP server so an agent can find a template without being told where to look, a gate runner that refuses to say everything passed, and two install-time descriptions that had been quietly false. **The first release note filled with the library's own fill tools, which failed on it and were wrong**
- [`v0.5.0.md`](v0.5.0.md) - the first template built because the maintainer wanted it: the `epic` bundle, whose own research argues against the easy version of the document, and a floor counter that had assumed this release would never happen
- [`v0.4.0.md`](v0.4.0.md) - the first release carrying a feature rather than a correction: a second skill that grades documents you already have, the first eval run that was mechanically possible, and four claims the library made about itself that were not true
- [`v0.3.1.md`](v0.3.1.md) - a documentation patch: the `v0.3.0` tag shipped four documents denying the efficacy evaluations that shipped beside them
- [`v0.3.0.md`](v0.3.0.md) - Gold tier measured in CI, the pilot's held-out finding withdrawn, and two install defects found by running the install
- [`v0.2.1.md`](v0.2.1.md) - a listing-contract patch: `v0.2.0` was tagged before its downstream contract was read, and a published tag is not moved. **Backfilled 2026-08-09**
- [`v0.2.0.md`](v0.2.0.md) - the Tier-1 floor completed, and the library's first user-facing documentation
- [`v0.1.0.md`](v0.1.0.md) - the first tagged release: four bundles and the governance gate that admits them

**Every tagged release now has a page**, which was not true until 2026-08-09. `v0.2.1` shipped without one
and the gap sat unnoticed because nothing checks it:
[`release-process.md`](../internal/release-process.md) names a release note as one of **four** required
artifacts per release, and no CI step reads that rule. The backfilled page is dated as backfilled and says
so on its own face, rather than being presented as contemporaneous.
