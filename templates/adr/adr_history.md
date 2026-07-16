# History: ADR bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-07-14

- Initial ADR bundle. First bundle in the `decision-docs` family, and the first outside
  `delivery-docs`.
- **Format: MADR v4**, not Nygard. Nygard's 2011 format is the origin and remains serviceable, but
  MADR is actively maintained and versioned (v4.0.0, 2024-09-17), has real tooling, and its section
  set is a strict superset, so no Nygard content is lost. It is also the format the product-on-purpose
  organization has standardized on for its own decision records. `adr_guide.md` carries a one-to-one
  Nygard-to-MADR mapping table so teams already on Nygard can adopt without rewriting.
- **Variants: `lean` and `full`, overturning the master catalog.** Catalog entry 64 classifies the
  ADR as single-size ("S only"). MADR itself ships a minimal template and a full template as separate
  files, which is decisive evidence from the standard's own maintainers that the type earns two
  weights. Lean carries MADR's three mandatory sections; full adds Decision Drivers, Confirmation,
  Pros and Cons of the Options, and More Information. Nesting verified: MADR's minimal section list is
  already a strict ordered subset of its full one, with no adjustment needed.
- **Worked example is a real decision, not an invented one.** `adr_example.md` is the library's own
  [ADR 0010 (the meta declares the size contract)](../../docs/internal/decisions/0010-meta-declares-size-contract.md),
  rendered at full weight. Its Confirmation section points at gate checks that actually run in CI on
  this repository, and its cons on the winning option are costs the project actually paid. This is the
  first example in the library that was not authored to be an example.
- Companion researched 2026-07-14 against a tiered source set: MADR templates fetched raw and
  verbatim; Nygard, Fowler, Zimmermann, InfoQ, ThoughtWorks Radar, Spotify, and Stride fetched
  directly; Tyree and Akerman (2005), Zdun et al. (2013), and ISO/IEC/IEEE 42010:2022 are paywalled
  and were **not** read, with claims held to what secondary sources agree on. See
  `adr_research-log.md` for per-source retrieval status.
- **Corrected before release, across two adversarial review rounds.** The first round found factual
  errors, the most serious in the bundle's single empirical claim: an AI-era study described as a 2025
  paper showing ADRs improved agent decision compliance "by roughly 49%." It is a 2026 paper, the 49 is
  a percentage-point delta rather than a relative gain, and the intervention was the authors' own
  commercial product-context system rather than ADRs at all. That round also caught `adr-tools` cited
  as MADR tooling (it is Nygard-only, so the claim argued against its own conclusion), a Nygard quote
  taken verbatim from a source read only in summary, and Tyree and Akerman's fields enumerated from a
  paper never read.
- **The second round was sent to re-check the first round's fixes, and it was right to be.** The fix
  for the `adr-tools` error had reproduced the same defect in subtler form: Log4brains and adr-manager
  were swapped in as evidence that MADR has tooling, cited to a page which shows both target MADR
  **2.1.2**, with nothing tracking v4. Tooling is therefore no longer offered as a reason to choose
  MADR; the two-major-version lag is stated as a real cost, and the choice rests on the maintained
  spec, the superset section set, and the org convention. The round also found the companion calling
  **Considered Options optional** when MADR makes it mandatory (contradicting three other places in
  this same bundle), the Y-statement template misquoted, and the lean/full frontmatter split
  miscredited to MADR when it is this library's own design.
- Every one of these is named in the research log's **Corrections** table rather than quietly patched,
  on the principle [ADR 0011](../../docs/internal/decisions/0011-madr-v4-at-docs-internal-decisions.md)
  applies to this repo's own records: **show the scars.** The standing lesson, now written into the log:
  a correction deserves the same adversarial pass as the draft, because fixing a citation defect is
  exactly where the next one gets introduced.
- **Two findings raised for the maintainer** (recorded in the research log, not acted on from here):
  1. The paired `develop-adr` skill in pm-skills ships a **Nygard**-format template, which diverges
     from the org's own MADR v4 convention. The guide documents the divergence and the mapping.
  2. Master catalog entry 64's "S only" size call is overturned by this bundle and should be
     corrected at the source.
- Status: `beta`. Gate-green, but with zero real usage by anyone other than the author, per the
  catalog's own Tier-2 rule.
