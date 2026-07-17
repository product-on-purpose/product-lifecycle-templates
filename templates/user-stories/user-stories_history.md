# History: User Stories bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0, reviewed 2026-07-16 - citation integrity pass (WP-10)

**No template change, so `template_version` stays 0.1.0.** Corrections are to the companion and the
research log; `last_reviewed` bumped. This bundle predates the citation discipline and had never had
an adversarial pass. Seven defects, all in a bundle the gate had always passed green.

- **A quote from a source that cannot be retrieved.** The job-story critique was presented as
  Klement's exact words. The jtbd.info domain times out from this environment, so the quote could
  never be checked, and search excerpts word it differently. **De-quoted to a paraphrase**, with the
  retrieval failure stated in the reference itself.
- **Four combined entries split**, each bundling a retrievable source with an unretrievable one:
  Beck's book with the C3/1997 claim; Cohn's book with his Mountain Goat page; Klement's post with the
  Intercom blog; Wikipedia with Patton's book. The splits are what exposed the misattributions below.
- **"Cohn credits Rachel Davies..."** was cited to the Mountain Goat page, which **never mentions
  Davies, Connextra, XP, or C3**. The claim is real, but belongs to Cohn's book and is recorded
  verbatim by Wikipedia. Re-pointed. Likewise "User Stories Applied generalized the practice" cited
  the *page* for a claim about the *book*.
- **Two claims made in Bill Wake's name that Wake does not make.** "Sized to fit inside one iteration"
  is not his: he says "at most a few person-weeks worth of work. (Some teams restrict them to a few
  person-days of work.)" And "Negotiable means the path, not the need" is a gloss; his actual
  definition is that a story "is not an explicit contract for features; rather, details will be
  co-created by the customer and programmer during development." Both rewritten to his wording, with
  the glosses labeled as this bundle's.
- **The research log was wrong too**, claiming Jeffries and Wake were corroborated but not fetched.
  Both are now fetched and verified, and Wake contradicted two claims made in his name.
- **Print books are now labeled as such.** Beck (1999), Cohn (2004), and Patton (2014) have no URL and
  are cited from the books, not retrieved. Previously they hid inside combined entries that carried a
  URL, which made them look retrieved.

## 0.1.0 - 2026-06-30

- Initial User Stories bundle, second member of the delivery-docs family.
- Variants: `lean` (3 sections: Story, Acceptance criteria, Notes) and `full` (strict superset, 7
  sections, adding Description, INVEST check, Estimate, Dependencies); nesting verified by hand.
- Companion researched 2026-06-30 against a tiered source set (Cohn / Mountain Goat and Wikipedia
  verified directly; Beck XP, Jeffries Three C's, Wake INVEST, Connextra, Klement/Intercom job stories,
  Scrum Guide via search). See `user-stories_research-log.md`.
- Status: `beta`. Pending the CI quality gate once the repo scaffold is stood up.
