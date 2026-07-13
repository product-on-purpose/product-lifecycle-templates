# Research log: Release Notes bundle

Evidence trail for the companion, per the methodology's research protocol (§A6). Researched 2026-06-30.

## Sources consulted

| # | Source | Tier | Retrieval | Claims it supports |
|---|---|---|---|---|
| 1 | Keep a Changelog 1.1.0 (Olivier Lacan) | primary | Fetched, verified | Six change types and meanings; human-first principles; ISO 8601 dates; newest-first; "don't dump git logs"; changelog-vs-release-notes distinction; v1.1.0, MIT, maintained since 2014 |
| 2 | Semantic Versioning 2.0.0 (Tom Preston-Werner) | primary | Search-corroborated | MAJOR/MINOR/PATCH meanings; breaking changes drive major bump |
| 3 | Conventional Commits 1.0.0 | primary | Search excerpt | feat/fix/BREAKING CHANGE mapping to MINOR/PATCH/MAJOR; enables automated changelog + version |
| 4 | conventional-changelog / semantic-release / release-please | vendor | Search excerpt | Tooling that automates version + changelog/release-note generation |
| 5 | ProductPlan, "Write Release Notes Users Will Read" | vendor | Search excerpt | Write for the reader not the shipper; benefit-led language example |
| 6 | Appcues / userpilot / AnnounceKit best-practice guides | vendor | Search excerpt | Group by category; benefit framing; transparency on known issues; New section read first |
| 7 | Master catalog entry 115 (Release Notes) | internal | On disk | Definition; customer-facing + internal variants; changelog/what's-new aliases; relationships |

## Notes and limitations

- Keep a Changelog (the load-bearing source for the change-type taxonomy and the changelog-vs-release-notes
  distinction) was fetched and verified directly, including the seven guiding principles and the v1.1.0
  status with v2.0.0 planned.
- SemVer and Conventional Commits dates/semantics were corroborated across multiple search results; the
  primary semver.org and conventionalcommits.org URLs are cited but were not individually fetched.
- Vendor best-practice sources (5, 6) are used for customer-facing tone and structure guidance, not for
  contested claims of fact.
- Recency note: Keep a Changelog 2.0.0 is planned for 2026; this bundle cites 1.1.0 as current and should
  be re-checked when 2.0.0 ships.
