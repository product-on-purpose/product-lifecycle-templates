# History: Acceptance Criteria bundle

Per-bundle changelog, by `template_version`. Newest first.

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
