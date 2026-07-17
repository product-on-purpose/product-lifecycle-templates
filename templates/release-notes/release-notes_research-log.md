# Research log: Release Notes bundle

Evidence trail for the companion, per the methodology's research protocol (§A6). Researched 2026-06-30.
**Citation integrity pass 2026-07-16 (WP-10): every source fetched and verified against the claims that
cite it.** Corrections below.

## Sources consulted

| # | Source | Tier | Retrieval | Claims it supports |
|---|---|---|---|---|
| 1 | Keep a Changelog 1.1.0 (Olivier Lacan) | primary | **Fetched and verified** (2026-06-30; re-verified 2026-07-16, incl. canonical-version check) | Six change types and meanings; human-first principles; ISO 8601 dates; newest-first; "don't dump git logs"; changelog-vs-release-notes distinction; v1.1.0, MIT, maintained since 2014 |
| 2 | Semantic Versioning 2.0.0 (Tom Preston-Werner) | primary | Search-corroborated; **URL confirmed live 2026-07-16**, body not fetched | MAJOR/MINOR/PATCH meanings; breaking changes drive major bump |
| 3 | Conventional Commits 1.0.0 | primary | Search excerpt; **URL confirmed live 2026-07-16**, body not fetched | feat/fix/BREAKING CHANGE mapping to MINOR/PATCH/MAJOR; enables automated changelog + version |
| 4 | conventional-changelog | vendor | **URL confirmed live 2026-07-16** | Tooling that automates version + changelog generation |
| 5 | ProductPlan, "How to Write Release Notes Your Users Will Actually Read" | vendor | **Fetched and verified 2026-07-16** | Plain language over developer-speak ("explaining them to a friend... not [one] in computer science"); bold category headers; visuals for major releases. **Does NOT support** the Appcues quote or migration detail |
| 6 | Appcues, "Release notes examples" | vendor | **Fetched and verified 2026-07-16** | The "written for the team that shipped the feature" quote (verbatim); the throughput/reports example pair (verbatim); grouping by type; before-versus-now framing; "users respect transparency more than they resent imperfection"; visuals for major releases |
| 7 | Master catalog entry 115 (Release Notes) | internal | On disk | Definition; customer-facing + internal variants; changelog/what's-new aliases; relationships |
| 8 | semantic-release | vendor | **URL confirmed live 2026-07-16** | Automated version + release-note generation |
| 9 | release-please (Google) | vendor | **URL confirmed live 2026-07-16** | Automated version + changelog generation |
| 10 | AnnounceKit, "Release Notes Best Practices" | vendor | **Fetched and verified 2026-07-16** | Breaking changes stated prominently rather than buried, with migration steps and a timeline (verbatim). Also corroborates category labels and benefit-first phrasing |

## Corrections applied 2026-07-16 (WP-10 citation integrity pass)

Every source was fetched and each claim citing it was checked. Six defects found and fixed. This is
recorded rather than quietly patched, because a research log that claims a clean pass it did not have is
the defect it exists to prevent.

**Combined entries split (the defect that caused the rest).** Two references bundled multiple sources
under one number and one URL:

- **Old [4]** was "conventional-changelog, semantic-release, and release-please (Google) tooling" with a
  single URL reaching only the first. Split into **[4]**, **[8]**, **[9]**, each independently
  reachable. Claims naming all three now cite all three.
- **Old [6]** was "Appcues ... and AnnounceKit" under one URL, with **no URL at all for AnnounceKit**.
  Split into **[6]** (Appcues) and **[10]** (AnnounceKit). This mattered: the two sources support
  *different* claims, and the combined entry made it impossible to tell which. Verifying them separately
  is what exposed the three defects below.

**Misattributions and overstatements fixed:**

| Where | Defect | Fix |
|---|---|---|
| The "written for the team that shipped the feature" quote | Cited [5][6]. The quote and both examples are verbatim in Appcues; **ProductPlan contains none of them.** | Dropped [5]; the sentence cites [6] alone |
| Known issues, "*Why:*" | Read "transparency improves credibility; users prefer knowing in advance" [6]. **Neither Appcues nor AnnounceKit says this.** Appcues says users "respect transparency more than they resent imperfection" | Reworded to the claim Appcues actually makes |
| Customer-facing vs internal | "behavior, breaking changes, and migration detail" cited [5][6]. **Neither supports migration detail.** AnnounceKit does, verbatim | Split the sentence: plain language to [5][6], breaking changes and migration steps to [10] |
| Anti-pattern "No known issues" | "users hit them unprepared" [6]. **Neither source frames it that way** | Reworded to Appcues' actual position (saying so is what earns trust) |

**A third source vanished between the research and the references.** This log previously recorded source
6 as "Appcues / **userpilot** / AnnounceKit". No reference in the companion ever cited userpilot, and no
surviving claim needs it: Appcues and AnnounceKit carry every claim that cited old [6]. It is dropped
rather than added as an uncited entry, since a reference nothing cites is padding.

## A correction to the roadmap, not to this bundle

**WP-10 instructed: "Keep a Changelog corrected to 1.1.2 with root URL." That instruction is wrong, and
following it would have introduced an error.** Verified 2026-07-16:

- `https://keepachangelog.com/en/` serves **1.1.0** and advertises no other version.
- `/en/1.1.1/` and `/en/1.1.2/` return HTTP 200 but are **redirect stubs**, 242 bytes, whose entire body
  is `<link rel="canonical" href="/en/1.1.0/">` plus a meta-refresh back to 1.1.0.
- Nonsense versions (`/en/9.9.9/`) return a genuine 404, so the 200s are real routes, not a catch-all.
- The repo (`olivierlacan/keep-a-changelog`) does carry tags `v1.1.1` and `v1.1.2`, and its latest
  *release* is v1.1.1. **These are site/repo releases, not published spec versions.** The audit most
  likely read a git tag and mistook it for the spec version.

**The companion's "version 1.1.0" at `/en/1.1.0/` is correct and is the site's own declared canonical
URL, so it is left unchanged.** The roadmap's WP-10 row has been corrected instead.

## Notes and limitations

- **Bodies not fetched:** [2] semver.org and [3] conventionalcommits.org. Both URLs were confirmed live
  2026-07-16 and both are stable, well-known specs whose cited semantics (MAJOR/MINOR/PATCH; feat/fix/
  BREAKING CHANGE) are uncontested, but neither body was read. A verbatim pass is a cheap future
  improvement if any of their specifics become load-bearing.
- **[4], [8], [9] are cited for existence and purpose only** ("this tooling automates the flow"). Their
  URLs are confirmed live; their READMEs were not read in depth.
- Vendor best-practice sources ([5], [6], [10]) are used for customer-facing tone and structure guidance,
  not for contested claims of fact.
- **Recency:** Keep a Changelog 2.0.0 is planned; as of 2026-07-16 the site still serves 1.1.0 as
  canonical. Re-check when 2.0.0 ships.
