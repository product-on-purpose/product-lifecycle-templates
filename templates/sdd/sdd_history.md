# History: SDD bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-07-20

- Initial SDD bundle. Third bundle in the `decision-docs` family, alongside `adr` and `rfc`, and the
  first bundle built under the Tier-1 floor build-out ([ADR 0021](../../docs/internal/decisions/0021-complete-the-tier-1-floor.md)).
  Catalog entry 47.
- **Scope: the modern, living "design doc"**, not the heavy formal Software Design Description. The
  companion's sections 1, 2, and 5 frame this honestly: IEEE 1016 was classified Inactive-Reserved in
  2020 and the DOD-STD-2167A-era SDD is largely historical, while the living form (Google, Uber, Stripe,
  arc42) is what teams write today. The bundle teaches the living form with its formal lineage
  acknowledged rather than reproduced.
- **Variants: `lean` and `full`.** The catalog lists S/M/L; the two-weight split is what the sources
  actually attest (Google's five-section "mini design doc" versus its 10-20 page large-project form;
  arc42's lean/thorough/essential modes). Lean is exactly Google's five canonical sections: Context and
  Scope, Goals and Non-Goals, The Design, Alternatives Considered, Cross-Cutting Concerns. Full breaks
  The Design into four views (Static Structure, Runtime and Data Flow, Interfaces and Contracts,
  Deployment and Operations) and adds Quality Attributes and Risks and Open Issues. Nesting verified:
  lean's H2 headings are a strict ordered subset of full's.
- **The sharpest teaching point: design doc versus RFC versus ADR.** A design doc describes an
  implementation, an RFC proposes a decision, an ADR records one. The distinction runs through the
  companion (sections 1, 6.3, 8), the guide's comparison table and first anti-pattern, and the worked
  example (which flags its storage-model choice for an ADR). This is the most common real confusion
  around the type, so it is stated in every file that a user might read on its own.
- **Worked example chains with the delivery-docs family.** `sdd_example.md` is the design counterpart to
  the `prd` bundle's "Saved Views for Dashboards" example, so the PRD (what and why) and this design doc
  (how) read as one traceable scenario across the two families. It demonstrates the design-doc-to-ADR
  relationship in practice by lifting the storage-model decision out for its own record.
- **`pairs_with: []`.** There is no `develop-sdd` skill in pm-skills (checked against
  `tools/known-skills.txt`, 2026-07-20). The org has a skill for the decision *record* (`develop-adr`)
  but none for the design document. Recorded as context in `sdd_guide.md` and `STATE.md`.
- **`decision-docs` has no ratified family contract yet**, so the bundle passes gate check K with a note.
  Whether the family (rfc + adr + sdd) now earns its own contract is a small follow-on decision; the
  bundle does not need it to land.
- Companion researched 2026-07-20 across 24 tier-ranked sources (see `sdd_research-log.md` for per-source
  retrieval status). Two sources were confirmed live but not read (IEEE 1016-1987 on Xplore, and the
  Parasoft DO-178C page) and carry no claim alone; three claims are flagged contested (the IEEE viewpoint
  enumeration from a course summary, the Limoncelli template's attributed authorship, and whether DO-178C
  mandates a document literally named "SDD"). Nothing not fetched-and-verified is quoted.
- Status: `beta`. Gate-green, zero real usage by anyone other than the author.
