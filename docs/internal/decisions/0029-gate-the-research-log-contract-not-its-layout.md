---
status: accepted
date: 2026-07-27
decision-makers: [jprisant]
consulted: [claude]
---

# Gate the research log's contract, not its layout

## TL;DR

- **Decision:** Adopt a machine-checkable research-log contract, enforced by a new CI check (`tools/check-research-logs.py`), requiring every source entry across any of three legal layouts (numbered prose, numbered list, or table) to carry an identifier, title and author or organization, URL (with a documented print-source exemption), tier, retrieval status, and a `Supports:` clause; six table-layout logs (acceptance-criteria, adr, prd, release-notes, rfc, user-stories) are named and exempted rather than converted, tracked as finding DF-4.
- **Why:** the library's central honest-retrieval claim, that only a `fetched-and-verified` source may be quoted verbatim, had never actually been checked by the gate across any of sixteen bundles; the fix gates the contract's fields rather than forcing every log onto one presentation, so ten already-correct logs need only six relabelled lines rather than a rewrite.
- **Status:** accepted 2026-07-27. Corrected in place on 2026-07-28, per ADR 0011 (the correction procedure at 0011-madr-v4-at-docs-internal-decisions.md): the original finding (DF-2, three status-less logs needing conversion) was itself wrong, an unverified absence recorded as a finding; the real gap is the opposite, the six table-layout logs carry no URL and no retrieval-status token for any of their 86 sources, which is what the decision (gate the contract, not the layout) already resolves.

The honest-retrieval standard is this library's central quality claim: a source is tagged with how it was
actually retrieved, and **only a source marked `fetched-and-verified` may be quoted verbatim**. Every bundle
carries a `<type>_research-log.md` that is supposed to carry that record.

**The gate has never checked it. Not once, across sixteen bundles.**

The reason is a seam nobody crossed. The requirement is written into the research workflow's JSON schema in
[`bundle-pipeline.md`](../bundle-pipeline.md) phase 1, which requires `title`, `author_or_org`, `url`,
`tier`, `retrieval_status` and `supports` for every source. That schema constrains **what the research agents
return**. It says nothing about the markdown file a human then writes from those returns, and nothing
downstream re-checks it.

Auditing for this (finding **DF-2**, research-log format drift, in [`STATE.md`](../../../STATE.md)) found three
mutually incompatible layouts in the tree:

| Layout | Bundles | Per-source retrieval status a checker can see |
|---|---|---|
| Numbered prose entries (`**[n]** tier. status.` then `Supports:`) | 7 | yes |
| Numbered markdown table (`\| # \| Source \| Tier \| Retrieval \|`) | 6 | yes |
| `###` subsections, sources as ungrouped prose | 3 (`product-backlog`, `sdd`, `sprint-backlog`) | **no** |

> **Correction, 2026-07-28, before the check was built. The third row of that table is false, and so is
> the paragraph that followed it.** `product-backlog`, `sdd` and `sprint-backlog` do not record sources as
> ungrouped prose. They use a **third numbered layout**, `n. **[Tier N] Author. "Title."** url - **status**
> - Supports: ...`, grouped under `###` dimension headings, and each of their 73 sources carries the full
> contract including the same three-token retrieval enum. All three even open with a retrieval-status
> legend. The audit that produced DF-2 matched two regexes, found neither, and recorded the absence as a
> finding. **An unverified absence is a to-do, not a finding**, which is the rule this repository had
> already written down and then broke in the act of writing it down.
>
> Measured against every one of the 430 sources in the tree on 2026-07-28, the real distribution is:
>
> | Layout | Bundles | Sources | Carries url | Carries the retrieval enum |
> |---|---|---|---|---|
> | Numbered prose `**[n]**` | 7 | 271 | all but the documented print exemption | all |
> | Numbered list `n. **[Tier N]**` | 3 | 73 | all but one cross-reference, since fixed | all |
> | Numbered table | 6 | 86 | **none** | **none** |
>
> So the gap is the opposite of the record: the three "status-less" logs need no conversion, and the six
> **table** logs are the ones that cannot satisfy the contract. Their retrieval column is prose
> ("Fetched and verified 2026-07-16", "BLOCKED. HTTP 403") and no row carries a URL at all. The cost claim
> below ("three log conversions") was therefore wrong in both directions.
>
> **The decision itself stands and is strengthened**: gate the contract, not the layout. There are three
> legal layouts rather than two, which is what a contract-shaped rule is for. Corrected in place rather
> than superseded, per [ADR 0011](0011-madr-v4-at-docs-internal-decisions.md): the facts under the
> decision were wrong, the decision was not.

**The framing that decides this.** "Three layouts" is the visible symptom and not the defect. What matters
is whether each source carries a record a checker can read, which is why this ADR gates fields and not
presentation. (As corrected above: all three numbered layouts carry that record; the table layout does not
carry a URL.)

A second lesson came out of the same audit and belongs in this record. The first pass of that audit reported
**76 defects**. The real number was **2**. The checker demanded `Contested/time-bound` and `Quotable` on
every entry; the written standard marks both **optional**. Acting on it would have meant editing 74 correct
entries in a diff that looked like diligence. **Verify the rule before enforcing it** is the reason this ADR
gates the documented contract rather than the stricter thing that felt right.

## Decision Drivers

- **The claim has to be checkable.** A quality standard nothing verifies is a promise, not a standard.
- **Do not rewrite eleven settled logs for cosmetic uniformity.** Those bundles are gate-green, reviewed, and
  shipped; churn on them buys presentation, not correctness.
- **There is precedent for one rule over two legal shapes.** `sizes_available` has accepted two vocabularies
  (`lean`/`full` and `s`/`m`/`l`) since [ADR 0010](0010-meta-declares-size-contract.md); the gate enforces the
  rule, not the vocabulary.
- **Fix the real gap, which is three files, not sixteen.**
- **The check must not overstate itself.** Same discipline as
  [`check-changelog.py`](../../../tools/check-changelog.py): say in the output what was not verified.

## Considered Options

- **Option A: unify on numbered prose entries.** Rewrite the 6 table logs and the 3 prose ones. Rejected:
  nine rewrites, of which six buy nothing but uniformity. The prose format is richer and is what the seven
  most recent bundles use, so it wins by drift anyway without a mandate.
- **Option B: unify on the table.** Rewrite ten logs. Rejected for the same reason plus a real loss: the
  table has no natural home for the per-source `Contested/time-bound` prose that the recent bundles use
  heavily.
- **Option C: gate the contract, accept either numbered layout, convert only the three that carry no
  status.** Chosen.
- **Option D: record DF-2 and move on.** Rejected. It leaves the library's central claim unverifiable in
  three bundles and unverified in all sixteen, which is exactly the shape of the drift classes this
  repository has already had to close twice (the atlas, the ADR index).

## Decision Outcome

**Adopt a machine-checkable research-log contract, enforced by a new CI check, that constrains the record and
not the presentation.**

**The contract.** Every source entry in a `<type>_research-log.md` must carry:

| Field | Required | Notes |
|---|---|---|
| identifier | yes | a contiguous number, `[n]`, unique within the log |
| title and author or organisation | yes | |
| `url` | yes, with one exemption | see the print-source exemption below |
| tier | yes | one of `primary`, `standards`, `academic`, `practitioner`, `vendor`, `reference`, `internal` |
| retrieval status | yes | exactly one of `fetched-and-verified`, `url-confirmed-not-read`, `not-retrieved` |
| `Supports:` | yes | what the source is being relied on for |
| `Quotable:` | **no** | optional, per the phase 1 schema |
| `Contested/time-bound:` | **no** | optional, per the phase 1 schema |

**Three numbered layouts are legal** (corrected 2026-07-28): the prose-entry form, the numbered-list form,
and the table form. Any form that carries no per-source record is not, because the contract cannot be read
out of it, and a log the check cannot parse fails rather than passing quietly.

**The print-source exemption.** A source that is a physical book, not retrieved, legitimately has no URL, and
inventing a bookseller link would manufacture the appearance of retrieval. Such an entry must instead state
the absence explicitly and say why, as `risk-register` [33] (Hubbard, *The Failure of Risk Management*) now
does. The check accepts an entry with no URL only when it carries that explicit statement.

**No log is converted** (corrected 2026-07-28, replacing "three logs are converted"). The three the original
record named already carry the contract. Six entries across them said `Corroborates`, `Additional support:`
or nothing where the contract says `Supports:`, and one carried no URL because it duplicates an earlier
entry; those six lines are relabelled without changing a claim.

**Six logs are exempt, by name, with a measured reason and a date.** `acceptance-criteria`, `adr`, `prd`,
`release-notes`, `rfc` and `user-stories` use the table layout and carry no URL for any of their 86 sources
and no enum token in any retrieval cell. They are listed in the check's `EXEMPT` map, skipped, and **printed
on every run** with the reason. This follows the `GRANDFATHERED` precedent in
[`check-changelog.py`](../../../tools/check-changelog.py). It is deliberately loud, because the alternative
was weakening the contract until they happened to pass, and because backfilling them means fetching 85
sources again: a URL cannot be invented and a retrieval status cannot be claimed for a fetch nobody
performed. Tracked as **DF-4** in [`STATE.md`](../../../STATE.md).

**The check states its own limits on every run.** It verifies that each entry carries the required fields.
It does **not** verify that a retrieval status is truthful, that a `Supports:` clause is accurate, or that a
quoted phrase really appears in the cited source. Those are the four-lens review's job, and the check says so
rather than letting a green run be read as more than it is.

### Consequences

* Good: the library's central quality claim becomes machine-verified for the first time, in **10 of 16**
  bundles covering 344 of 430 sources (corrected 2026-07-28 from "in all bundles").
* Good: the fix costs six relabelled lines rather than nine or ten rewritten files, and touches no bundle
  that is already correct.
* Good: the rule generalises. A bundle may use any of the three legal layouts, and a fourth is legal the
  moment it carries the contract.
* Good: the print-source exemption turns an awkward edge case into a documented convention, so the next
  unfetchable book is handled rather than argued about.
* Neutral: three legal layouts persist, so a reader moving between bundles meets three presentations. This
  is the same trade `sizes_available` already makes and it has not caused a problem there.
* Bad, and the price of shipping today: **six logs are exempt, so a third of the library's sources stay
  unverified.** Naming them in code with a printed reason is better than a contract weakened to fit them,
  but it is debt either way, and DF-4 says so.
* Bad, and worth stating: **a green run proves the fields are present, not that they are honest.** A source
  mislabelled `fetched-and-verified` passes. The check narrows the failure surface from "anything" to
  "deliberate or careless mislabelling", and the review remains the only thing that catches the rest.
* Bad: the numbered-table layout has no place for `Contested/time-bound`, so bundles using it will keep
  carrying that information elsewhere or not at all. Accepted, because the field is optional by the
  documented standard.

### Confirmation

**Built and enforced 2026-07-28.** [`tools/check-research-logs.py`](../../../tools/check-research-logs.py)
runs in CI alongside the other document gates (`check-adr-index.py`, `check-changelog.py`) and fails the
build when any checked log contains an entry missing a required field, or contains no parseable source
entries at all. It reports **10 logs checked, 344 sources, 6 exempt** and prints both the exemption list and
its own limits on every run.

Because most of its failure branches have no live subject once the tree is clean (a missing tier, an invalid
status token, a URL-less entry without its exemption, a gap or duplicate in the numbering, a table header
that does not declare the contract columns), it carries fixture-based tests per
[ADR 0025](0025-executable-tests-for-gate-logic.md):
[`tools/test-check-research-logs.py`](../../../tools/test-check-research-logs.py), 78 assertions,
**mutation-checked** against seven deliberate breakages of the check to prove each is caught.

**An adversarial review rewrote this check before it shipped, and the reason is worth recording.** The first
implementation asked whether a required token appeared **anywhere in the entry block**. An external review
reproduced **nine false negatives** against a green run: a status sitting in a quotation, in a legend, in the
title or in the wrong table column all satisfied the status requirement; `not-retrieved-ish` satisfied
`not-retrieved`; `presupportscondition` satisfied `Supports:`; the same source under two numbers passed; and
a stray malformed entry was silently discarded by a layout heuristic that counted markdown shapes across the
whole file. It also found **three false positives**, including a valid concise `No URL: print-only book.`
failing an undocumented 40-character threshold the contract never set.

The rewrite reads every field **from its own position in the entry grammar**, scopes source parsing to
sections whose heading names sources, maps table columns through the header rather than fixed indexes, and
matches the enum by whole token. All twenty reproductions from that review are now regression fixtures.

Two of the review's findings were **declined on purpose and moved into the check's printed output instead**:
whether a URL belongs to the source it sits with (unknowable without a source registry this library does not
have) and whether an identity carries both an author and a title (real correct entries name a document whose
author is the organisation, such as `The Scrum Guide (November 2020)`). Naming them as unchecked is honest;
enforcing them would fail correct work, which is the 76-defects-against-2 mistake in a new costume.

## More Information

This **closes** finding **DF-2** (research-log format drift) in [`STATE.md`](../../../STATE.md) for the ten
logs the check covers, having first corrected what DF-2 actually was: see the correction above. It **opens**
**DF-4**, the six table-layout logs that carry no URL and no enum token for any of their 86 sources.

STATE.md also records the two real defects the original audit surfaced and fixed on the way: `bug-report`
[17] wrote its status as `not retrieved` where the enum token is `not-retrieved`, and `risk-register` [33]
carried no URL for a print book, now documented as a deliberate absence and the basis of the exemption
above. The check has a fixture for each, so neither can return unnoticed.

The authoring rule is written into [`bundle-pipeline.md`](../bundle-pipeline.md) phase 2, so the next bundle
inherits it rather than rediscovering it.
