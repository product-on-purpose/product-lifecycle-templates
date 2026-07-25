# History: Test Case bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-07-25

- Initial Test Case bundle. **Second member of the `qa-docs` family.** Catalog entry 104. Conforms to the
  [qa-docs contract](../../docs/internal/contracts/qa-docs.md) (`phase: develop`, `beta`, sizes
  `[lean, full]`); gate check K green
  ([ADR 0026](../../docs/internal/decisions/0026-adopt-qa-docs-family-contract.md)).
- **Scope: the test case, which is the most argued-about artifact in testing.** Two named schools disagree
  about whether writing them down helps or harms, and the companion's section 6 gives both their strongest
  form rather than picking quietly. The framing this bundle takes: a test case is **a design artifact, not a
  record of a run, and not a substitute for a tester's judgment**. The sharpest line in the literature is
  Michael Bolton's, and the bundle builds on it rather than around it: *"The test case is not the test. The
  test is what you think and what you do."*
- **The structural decision that follows from that framing:** the templates carry **no "actual result" and no
  pass/fail field**. Vendor templates almost universally include both, which silently turns a reusable
  specification into a single-use form. The frontmatter's `case_status` is the lifecycle of the
  *specification* (draft, active, deprecated), never the outcome of a test, and says so.
- **The load-bearing vocabulary finding:** the certification glossary does not draw the taxonomy
  practitioners think it draws. **Test procedure and test script carry word-for-word identical definitions**,
  and **test scenario is defined as a synonym for test script**, not as the high-level description almost
  everyone means by it. The bundle reports the conflict and tells teams to write down which they mean,
  rather than pretending the vocabulary is settled.
- **Attribution care, continuing the pattern the test-plan bundle established.** Myers (1979) **systematized**
  equivalence partitioning and boundary value analysis for software; he did not invent equivalence classes,
  and calling him the inventor overstates it. On a strict reading, **BVA presupposes partitioning**. The
  Given/When/Then **2004 date that circulates widely could not be verified** and is not used; what is verified
  is JBehave from 2003, the article in 2006, and **"Gherkin" as a 2008 name** coined with Cucumber. The FIRST
  acronym's attribution to Robert C. Martin was not verified and is therefore absent.
- **Variants: `lean` and `full`, against the catalog.** The catalog marks entry 104 single-size (S). This
  bundle ships two weights, on the same grounds that corrected the ADR entry (finding EC-2 in `STATE.md`):
  the regulated case for design rationale, environment, automation linkage and approval is documented, and it
  is a genuinely different weight of document from a case a developer writes in five minutes. Recorded as a
  second tested catalog size hypothesis. Lean is the four sections a case cannot do without; full adds Design
  Rationale, Environment and Configuration, Automation Status, and Version and Approval. Nesting verified:
  lean's four H2 headings are a strict ordered subset of full's eight.
- **The sharpest teaching points**, carried through companion, guide and example: (1) **one case, one
  objective** - one objective is not one assertion; (2) **expected results are written before execution**, or
  they are descriptions of what happened and cannot fail; (3) **preconditions are what make a case repeatable
  by a stranger**, which practitioner research ranks at the top of what testers value; (4) **design and
  execution fields are different things**; (5) **acceptance criteria do not exhaust test design** - negative,
  boundary, regression and non-functional territory is nobody's agreed criterion; (6) **counting test cases is
  a vanity metric**, and both camps agree on that one; (7) **automation changes a case's role rather than
  retiring it**, and usually checks less than the case specifies.
- **Worked example demonstrates the family boundary rather than describing it.** `test-case_example.md` is a
  full-variant case that traces to the highest-tier risk in the
  [test plan](../test-plan/test-plan_example.md) and to **no acceptance criterion at all**, which is the
  concrete form of "test design continues past the agreed criteria". Its design rationale partitions
  entitlement three ways and explains why the *partially entitled* partition is where a leak can occur; its
  step 4 (an aggregate computed before the row filter) exists because of a specific fact in the
  [design document](../sdd/sdd_example.md), not by symmetry; and its version history records that version 1.0
  would have passed against a defective implementation, which is the bundle's strongest argument for reviewing
  cases before running them. The automation section names what the automated version does **not** check.
- **`pairs_with: [deliver-edge-cases]`.** pm-skills ships no testing or QA skill (finding EC-4 in `STATE.md`).
  The pairing is especially direct for this member: an edge-case catalog is exactly the negative, boundary and
  error-state territory acceptance criteria do not cover, which is where a large share of test cases should
  come from.
- Companion researched 2026-07-25 across five parallel dimensions and 42 tier-ranked, deduplicated sources
  (see `test-case_research-log.md` for per-source retrieval status). Primary anchors include the IEEE SA page
  for 829-2008, the ISTQB Foundation syllabus on black-box techniques, NIST on combinatorial testing, a peer
  reviewed practitioner study of test-case quality, Dan North's original BDD article, Adzic's own ten-year
  retrospective, the context-driven testing principles, and Bach's and Bolton's essays. **29119-3 was not
  read** (paywalled) and is not quoted; **ISTQB's official glossary blocked retrieval**, so both circulating
  definitions of "test case" are cited from mirrors and labeled as such. One Adzic source is page-only (the
  book page; the book was not read) and one Kaner source is url-confirmed-not-read. Claims flagged contested: which ISTQB definition is current, the test-scenario
  vocabulary conflict, EP and BVA attribution, the Given/When/Then date, whether acceptance criteria and test
  cases are one artifact, and whether scripted cases help or harm outside regulated contexts. An unverified
  "70 percent of QA effort" figure found in the research is deliberately unused.
- Status: `beta`. Gate-green, zero real usage by anyone other than the author.
