# History: PRD bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0, reviewed 2026-07-16 - citation integrity pass (WP-10)

**No template change, so `template_version` stays 0.1.0.** Corrections are to the companion and the
research log; `last_reviewed` bumped. WP-10 named four defects in this bundle and **all four were
real**; re-checking found a fifth.

- **A wrong date, and a load-bearing one.** The companion said Cagan "has argued since **2007**"; his
  "Revisiting the Product Spec" is dated **October 12, 2006**. The sentence is specifically about how
  long he has held the position, so the date is the claim. Corrected in prose and reference.
- **The Cagan quote was verified only by luck.** The research log had said the quote's wording was
  "confirmed across both the search excerpt and the catalog" - that is, against a search snippet and
  *this repository's own internal catalog*, never against Cagan. Re-fetched (the old 403 no longer
  reproduces): the quote **is** verbatim. A good outcome from a bad process, and the process is what
  changed.
- **The Lenny quote could never have been verified.** "The single most important step in solving any
  problem" was presented as Rachitsky's words, but **the post is paywalled** ("This post is for paid
  subscribers"). De-quoted, per WP-10. Better than de-quoting: the claims it carried moved to **[8]**,
  Atlassian's freely readable rendering of the same template, which anyone can check.
- **Refs 8 and 12 were uncited padding**, invisible to the gate: check E fails an inline citation with
  no anchor, never an anchor with no citation. [8] is now cited and is the *fix* for the paywalled
  [7]. **[12] Hustle Badger is removed** (uncited, and 403s to fetch); inventing a citation to justify
  a reference is padding by another name. The catalog reference renumbered 13 -> 12, leaving no gap.
- **SVPG entries gained retrieval qualifiers.** [2] is fully verified. [3] (a PDF) and [4] are
  confirmed live but **were not read**, and now say so; both are corroboration only.

## 0.1.0 - 2026-06-30

- Initial PRD bundle. First worked bundle in the library and the reference implementation of the
  bundle methodology.
- Variants: `lean` (7 sections) and `full` (strict superset, 17 sections); nesting verified by hand.
- Companion researched 2026-06-30 against a tiered source set (Scrum Guide 2020 and ProductPlan
  verified directly; Cagan/SVPG, Amazon Working Backwards, Pragmatic Institute, Lenny Rachitsky, and
  the modern-PRD-sections consensus via search). See `prd_research-log.md`.
- Status: `beta`. Pending the CI quality gate (size-nesting, frontmatter, emdash, pairs-with) once
  the repo scaffold is stood up.
