# History: PRD bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0, reviewed 2026-08-15 - flagship content review, the half that could be applied (CR-5, CR-6, CR-7)

**No template change, so `template_version` stays 0.1.0.** The changes are to the example, the guide
rubric, and one companion cross-reference. This closes the applicable part of the 2026-07-10 audit's
flagship content review, which had sat unapplied for five weeks.

- **CR-5, the traceability gap, and the trap inside its own proposed fix.** The example declared six
  functional requirements against four stories. **FR-2 (list and switch views) is a Must and had no
  story**; FR-6 (stale-view indication) is a Could and had none either. The review proposed adding one
  line, *"every Must/Should FR must map to at least one story"*, which **would have shipped a document
  stating a rule its own content broke.** Fixed in the other order: the missing FR-2 story is added
  first, and only then the rule, which is now true of the example. FR-6 stays uncovered and is named as
  a deliberate Could rather than left as a silent gap. The guide's full-variant rubric gains the
  matching line.
- **CR-7, two of its four notes.** The `user-stories` example carried **two `## Story` headings at the
  same level as their own parents** (`## Lean card`, `## Full story`), so its outline read flat in a
  library that teaches structure; the inner headings are demoted to `###`. And the companion's
  upstream-artifacts line named a "solution brief" this library does not template. Half of that
  reference has since become resolvable: **PR/FAQ now exists here**, as a `product-vision` format
  ([ADR 0028](../../docs/internal/decisions/0028-adopt-a-format-axis.md)), which was not true when the
  review was written. It now links there, and the solution brief is flagged as out of scope.

### CR-6, recorded as the review asked: why this bundle ships two variants and the catalog signals three

**Catalog entry 29 gives this type `S/M/L`. The bundle ships `lean` and `full`.** That divergence is
legal under [ADR 0002](../../docs/internal/decisions/0002-variant-model.md), which lets the type decide
rather than the catalog, and it was **documented nowhere** until this line.

**The position:** the catalog's S signal is served by the lean variant used partially, which is exactly
what the companion's adaptations section already tells a solo user to do. **A true four-section S
variant is deferred until a real user asks for one.** The nesting rule makes adding it painless if they
do, and building it now would be speculation of the kind
[ADR 0021](../../docs/internal/decisions/0021-complete-the-tier-1-floor.md) confines to the Tier-1 floor.

### What was NOT applied, and why

The review's remaining findings are held deliberately, not overlooked.

- **CR-1 (the missing AI-era debate) and CR-2, CR-3, and CR-7's fourth note** all add teaching claims
  about how practitioners work. **They need sources, and the review does not supply them.** Writing
  them from the review's own summary would be the library's dominant defect (a plausible specific claim
  no logged source supports), committed on purpose. Each needs a research pass under
  [`bundle-pipeline.md`](../../docs/internal/bundle-pipeline.md), and CR-1 needs a full one.
- **CR-4 (add an "Alternatives considered" section to the full template) is now gated by a rule that
  did not exist when it was written.** It adds an **element** to an admitted type, so it faces
  [decision procedure 12](../../docs/internal/decision-procedures.md)'s admission test. Its E1 clause
  requires a named source publishing PRDs that contain that element, found by a search **capable of
  returning "no"**. The review asserts that "the strongest real PRDs" carry such a block and names no
  source for it. **This is the first candidate to meet procedure 12 since it was adopted, and it does
  not pass on the evidence available.** It is not rejected; it is unresearched.

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
