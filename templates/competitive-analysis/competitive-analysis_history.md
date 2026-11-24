# competitive-analysis: history

Change log for the `competitive-analysis` bundle. Each entry records what changed and why, so a reader can
tell a correction from a preference.

## 0.1.1 - 2026-11-23 - corrections from a Codex review

A read-only Codex review raised 13 findings. The main loop and a Sonnet verifier checked each one against
the cited lines and the cached source pages: 8 held, 5 held in part, and none failed. Every fix below is a
correction.

- **The rubric gains a floor.** A 0 on row 6 (findings ending in moves) or row 8 (refresh that can fire)
  now fails the document whatever the total. Before, a document scoring 0 on both still passed, at 12 of 16
  on lean and 16 of 20 on full.
- **The templates' GOOD texts agree with each other.** The profile said Northgate Booking has no billing, and
  the evidence row marked the same fact "unknown". The evidence row now sources it, and the unknown moves
  to a claim no GOOD text acts on.
- **The example routes the modelling claim instead of waving it through.** Its last implication said no row
  contradicts the positioning statement. Yet Plumline needs no modelling step for a one-file question, and
  the positioning statement says a general-purpose BI tool does. The statement's "unlike" clause still
  stands, on copying the data out; the modelling sentence goes to its owner as a note.
- **Source readings corrected.** Klue's "Continuous" cadence is for a one-rival analysis for sales reps; its
  broad analysis for product teams says "Quarterly or bi-annually", so Klue leaves the living camp. Blank
  opposes feature lists without customer evidence, not feature charts. The status quo is named by at least
  six publishers, four of them vendors, not by four. Aha!'s and Calven's pages do print field sets; what was
  not opened is the downloads.
- **Counts and dates.** The research log held 199 Quotable lines, not 197, and now holds 203, after four
  raw-checked additions. The example's two versions sit across the start of FY26, not inside one fiscal
  year.
- **Smaller fixes.** The example's connector row no longer claims "every system", and Plumline's jobs cell
  names one task. The guide gains a trade-study row and says a comparison informs a decision rather than
  settles it.
- **One deviation, recorded rather than changed.** ADR 0091's sizing evidence says the frontmatter carries a
  review trigger. The spec is silent, and both templates carry the trigger in the body section Refresh
  Trigger and Versions, beside the owner and the version table. That stays as built.

No section, field or placeholder changes. The example was filled from 0.1.0 and keeps that stamp.

## 0.1.0 - 2026-11-22

**Initial release.** Researched 2026-11-22, building on admission sweep 8 of 2026-11-14 and on
[ADR 0091 (competitive analysis joins strategy-docs as an eighth member)](../../docs/internal/decisions/0091-competitive-analysis-joins-strategy-docs-as-an-eighth-member.md).
The build's six-dimension fan-out covered origins, structure, practice, debates, relationships and the
standing gap question.
[`competitive-analysis_research-log.md`](competitive-analysis_research-log.md) records **56 sources**, all
fetched and verified: 25 practitioner, 23 vendor, 5 reference, 2 standards and 1 primary. The entries carry
**197 Quotable lines**, and every one was tested against the cached raw text of its page.

**The eighth `strategy-docs` member, added by amendment.** The maintainer accepted ADR 0091 on 2026-11-14,
which ruled the family and `classification: utility`. The maintainer confirmed the chain place, immediately
before the positioning statement, on 2026-11-17. That placement is this library's own POSITION: none of the 56
sources states the sequence. The maintainer ruled every remaining choice in the spec as recommended on
2026-11-20. This bundle is issue #361 (bundle: competitive-analysis) and it fills catalog entry 11.

### Two sizes ship, with the second weight unmeasured

The bundle ships `lean` as the default and `full`, which adds Competitor Briefs and a Jobs-Based Scorecard.
The nearest published source for two weights is Aha!, which asks for a regular high-level pass and a more
detailed one before major strategic decisions. That is a vendor's framing. The research found no measurement
of when the second weight pays for itself, so the signals for moving to full are this library's reading and
the size call is a hypothesis that evidence can overturn.

### classification: utility

The maintainer ruled `utility` through ADR 0091. That ruling does not depend on any refresh interval. The
sources do not converge on one: GitLab ties an annual minimum to a category at its most mature level and names
an event for every other category, Klue says quarterly, Aha! said quarterly in 2018 and biannually in 2023,
and Dovetail offers annual, quarterly, monthly or event-driven. None is measured, and every one except
GitLab's comes from a vendor.

### Corrections carried into the bundle

- **The GitLab cadence quotation is carried with its condition.** ADR 0091 and the family contract had quoted
  GitLab's "should be done at least annually" as a general cadence. The raw page ties it to a category at
  Complete maturity and says "Otherwise, when you intend to make a category shift". The spec records the
  correction and the log carries the full sentence.
- **BABOK is not cited as an origin.** Catalog entry 11 cites BABOK technique 10.4 in its note. The number
  exists, but its title is Benchmarking and Market Analysis and it is a technique, not a written document. No
  BABOK technique is titled Competitive Analysis. The page's text was not readable, so only its title and
  number are used.
- **Three carried quotations were removed from the pages that did not hold them.** The NN/g sentence that
  separates competitive testing from a competitive review survives only on [40], and Aha!'s two framing
  questions only on its whiteboard template page [8].
- **A null finding was reversed.** The practice dimension found no source that asks for a source and a date on
  each claim. The gap dimension found one, Calven's template, which is a vendor's guidance.

### Aliases and what the name excludes

Two aliases are declared: *competitive landscape*, which the catalog uses, and *competitor analysis*, the
title of Aha!'s and Productboard's pages. *Competitor matrix* is left out because a bare matrix collides with
other types in this library. *Benchmarking report* is left out because NN/g uses benchmarking for a recurring
UX measurement program. SWOT of the company's own position is kept out of the template, because a SWOT assesses
us and this document is about the others. That reason is this library's, not any source's.

### `pairs_with` is empty

No skill in `tools/known-skills.txt` addresses a competitive analysis. An empty list is the honest answer, not
a gap to paper over.

### The honest core

**No filled-in, published competitive analysis was read.** The evidence for what a strong one holds is
vendor and consultancy guidance, and most of those vendors sell competitive-intelligence or
product-management software. The section set is therefore largely the library's POSITION, built from vendors'
field lists, SVPG's narrative, GitLab's practice and the positioning sources. The log could not establish who
first wrote a competitive analysis for a product team, so the companion names no originator. Several pages
were readable only in part, and the log lists what each read did and did not cover. Every cadence or
structure claim from a vendor is labelled as that vendor's, and no vendor's cadence is presented as a
consensus.
