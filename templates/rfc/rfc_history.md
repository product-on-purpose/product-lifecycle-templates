# History: RFC bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-07-16

- Initial RFC bundle. Second bundle in the `decision-docs` family, alongside `adr`.
- **Scope: the engineering RFC**, the internal proposal circulated before a decision to gather input,
  not the IETF standards instrument. The companion's section 2 disambiguates the two at length,
  because they share a name and are almost opposite artifacts (IETF RFC: permanent, published after
  consensus; engineering RFC: mutable, circulated before the decision). Catalog entry 48.
- **Variants: `lean` and `full`.** Catalog says S/M; the two-weight split is well-attested (Rust and
  React run heavyweight processes; Uber and others tier lightweight vs heavyweight by impact). Lean:
  Summary, Motivation, Proposal, Alternatives Considered, Open Questions, Outcome. Full inserts Goals
  and Non-Goals, Detailed Design, Drawbacks and Trade-offs, Rollout and Adoption. Nesting verified:
  lean's H2 headings are a strict ordered subset of full's.
- **Opinionated choice: an Outcome section in both variants.** Several real RFC processes leave the
  decision record implicit or in a separate tracking issue, which is exactly where the most-cited RFC
  failure ("no decision recorded at the end") lives. Making Outcome a required section at every size
  is this bundle's fix, and it is the bridge to the ADR (an accepted RFC's Outcome is what the ADR is
  written from).
- **Worked example is a real, currently-open decision in this repo:** RFC-0001, the metadata-schema
  proposal (roadmap WP-21), rendered at full weight with status `in-review` and an honest
  "no decision yet" Outcome. It is the first example in the library whose outcome is correctly
  undecided, which is what an RFC in flight actually is.
- **`pairs_with: []`.** There is no `develop-rfc` skill in pm-skills. The org has a skill for the
  decision *record* (`develop-adr`) but none for the *proposal* that precedes it. Recorded as a
  finding (see `STATE.md`).
- Companion researched 2026-07-15 across two source sweeps (origins/primary and modern practice/
  debates). The two RFC-series quotations (RFC 1 and RFC 3) were verified verbatim by direct fetch of
  the primary text at rfc-editor.org; all other sources are paraphrased-and-cited rather than quoted,
  a deliberate discipline after the ADR bundle's citation defects taught that research-agent summaries
  must not be presented as verbatim quotes. See `rfc_research-log.md` for per-source retrieval status.
- First bundle built after gate check G (frontmatter YAML validity) shipped, so its frontmatter was
  YAML-validated from the first gate run rather than by a later sweep.
- Status: `beta`. Gate-green, zero real usage by anyone other than the author.
