# History: Acceptance Criteria bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.1 - 2026-08-21 - the checklist rubric becomes a scored rubric

**This is the experiment [`guide-rubric-spec.md`](../../docs/internal/guide-rubric-spec.md) section 4 item
2 asks for, not a mechanical conversion.** That item names this bundle as the candidate, "being the
most-used", and instructs that one guide is converted and read before the rest follow. **It remains an open
question whether the other checklist guides should follow**, and this change does not answer it or amend
the document that owns it.

- **The eight-item checklist becomes a seven-row 0/1/2 table**, matching the house style set by
  `product-vision` on 2026-07-27: a threshold stated as a consequence, criteria as bolded short names, and
  three concrete levels per row.
- **The housekeeping item was dropped, not lost.** "All guidance comments deleted; no placeholders remain"
  is fill hygiene rather than document quality, **none of the fourteen already-scored guides carries such a
  row**, and both templates already say it in their own HOW TO FILL block: "Before you ship: self-grade
  against `acceptance-criteria_guide.md`, then DELETE every HTML comment."
- **Threshold: under 10 out of 14 for full, under 9 out of 12 for lean**, stated in a scope table rather
  than in prose. 71 and 75 percent, inside the range the scored guides already use (62 percent for
  `bug-report` at 10 of 16, 72 percent for `status-report` at 13 of 18).
- **Row 6 is marked full-only**, because the lean variant has no Scenarios section and a Given/When/Then
  criterion cannot be graded against a section a variant does not ship.
- **The scope table was not optional, and the gate said so.**
  [`check-rubric-scope.py`](../../tools/check-rubric-scope.py) enforces one as soon as any row carries a
  scope marker and the bundle ships more than one variant, and it **failed this change** when the variant
  scoping was written as a sentence instead. It also caught the first lean threshold: 8 of 12 is 67
  percent, and `status-report` states the house convention that both thresholds sit **above two-thirds**.
  **The prose version would have read as complete to a human reviewer.**

**One gap was found by converting and is reported rather than filled.** Named anti-pattern 6, "criteria as
afterthought: written after the code, describing what was built, not what was needed", **has no rubric row
and did not have one as a checklist item either.** It is arguably the most consequential failure for this
document type, since it defeats the purpose rather than degrading the artifact, and **no row here can
detect it**: a document written after the fact can satisfy all seven criteria. Adding a criterion is a
change to what the library asks of a document, so it is raised for the maintainer rather than taken here.

**Seven rows is one below the smallest scored sibling**, which run eight to twelve. That is a consequence
of converting faithfully rather than a target that was aimed at, and it is the second thing worth reading
when deciding whether the scored form is better.

## 0.1.0, reviewed 2026-07-16 - citation integrity pass (WP-10)

**No template change, so `template_version` stays 0.1.0.** Corrections are to the companion and the
research log; `last_reviewed` bumped. Eight defects, in a bundle the gate had always passed green.

- **A factual error.** The companion said "In 2007 the **Gherkin** syntax formalized Given/When/Then",
  cited to Dan North. The word "Gherkin" does not appear in North's article, and the date is wrong:
  Gherkin arrived with Cucumber, which Aslak Hellesoy created in **2008**, extracting the
  Given-When-Then parser from RSpec and naming the syntax "to separate it from the tool". No cited
  source carried the 2007 date at all. Rewritten to the verified lineage, sourced to Hellesoy's own
  account [9].
- **Two combined entries split.** Old [1] bundled North's article with a Gherkin claim it never makes.
  Old [3] bundled Ron Jeffries (2001) with Mike Cohn's *User Stories Applied* (2004) under one entry
  **with no URL for either**. Splitting them immediately exposed a misattribution: **"conditions of
  satisfaction" is Cohn's term and appears nowhere in Jeffries**, yet [3] was cited for it.
- **A stale URL that looked healthy.** [1] pointed at `dannorth.net/introducing-bdd/`, a 318-byte
  redirect stub returning HTTP 200. Browsers follow the meta-refresh, so it "worked" and nobody
  noticed. Now the canonical `/blog/introducing-bdd/`.
- **The Ranorex claim (WP-10 flagged this one, and was right).** [7] was cited five times and supports
  two: scenarios automate, and Given-When-Then suits behavior. It does **not** compare GWT to
  checklists, does not say discrete rules belong in a list, and does not survey team defaults. Per
  WP-10's instruction those are now **labeled author judgment** rather than re-sourced: the
  rule-vs-scenario framing is this bundle's contribution, and now says so.
- **"Keep When to a single action"** was cited to North, who prescribes no such thing; Cucumber
  actually recommends 3-5 steps per example. The trap now cites Cucumber's real guidance and the
  single-action rule is labeled this bundle's own.
- **The research log was wrong too**, recording Cucumber as supporting "one behavior per scenario".
  It does not.
- **The weakest evidence is now labeled, not hidden.** [2] Scrum.org is the most-cited source here
  (16 citations) and **has never been read at source**: it returns HTTP 403 to automated fetch. The
  reference itself now says so, and the claims are marked as corroborated from search excerpts and
  cross-checked against the Scrum Guide rather than verified.

## 0.1.0 - 2026-06-30

- Initial Acceptance Criteria bundle, third member of the delivery-docs family.
- Variants: `lean` (3 sections: Story reference, Acceptance criteria, Out of scope and notes) and `full`
  (strict superset, 6 sections, adding Scenarios, Edge cases, Non-functional criteria); nesting verified
  by hand.
- Companion researched 2026-06-30 against a tiered source set (Scrum.org AC-vs-DoD and the BDD/Gherkin
  lineage; Dan North BDD 2006 / Gherkin 2007; Jeffries/Cohn confirmation; Thoughtworks, Cucumber,
  Ranorex via search). See `acceptance-criteria_research-log.md`.
- Status: `beta`. Pending the CI quality gate once the repo scaffold is stood up.
