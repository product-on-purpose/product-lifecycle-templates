---
status: accepted
date: 2026-07-27
decision-makers: [jprisant]
consulted: [claude]
---

# Gate the research log's contract, not its layout

## Context and Problem Statement

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

**The framing that decides this.** "Three layouts" is the visible symptom and not the defect. Two of the
three carry every required field; they differ in presentation. The actual gap is that **three bundles record
no per-source retrieval status in any form a checker could read**, so for those three the library's central
claim is not merely unverified, it is unverifiable.

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

**Two numbered layouts are legal**, the prose-entry form and the table form. A third form with no per-source
status is not, because the contract cannot be read out of it.

**The print-source exemption.** A source that is a physical book, not retrieved, legitimately has no URL, and
inventing a bookseller link would manufacture the appearance of retrieval. Such an entry must instead state
the absence explicitly and say why, as `risk-register` [33] (Hubbard, *The Failure of Risk Management*) now
does. The check accepts an entry with no URL only when it carries that explicit statement.

**Three logs are converted** as part of adopting this: `product-backlog`, `sdd` and `sprint-backlog`. Nothing
else changes.

**The check states its own limits on every run.** It verifies that each entry carries the required fields.
It does **not** verify that a retrieval status is truthful, that a `Supports:` clause is accurate, or that a
quoted phrase really appears in the cited source. Those are the four-lens review's job, and the check says so
rather than letting a green run be read as more than it is.

### Consequences

* Good: the library's central quality claim becomes machine-verified for the first time, in all bundles.
* Good: the fix costs three files rather than nine or ten, and touches no bundle that is already correct.
* Good: the rule generalises. A future bundle may use either legal layout, and a future third layout is
  legal the moment it carries the contract.
* Good: the print-source exemption turns an awkward edge case into a documented convention, so the next
  unfetchable book is handled rather than argued about.
* Neutral: two legal layouts persist, so a reader moving between bundles still meets two presentations. This
  is the same trade `sizes_available` already makes and it has not caused a problem there.
* Bad, and worth stating: **a green run proves the fields are present, not that they are honest.** A source
  mislabelled `fetched-and-verified` passes. The check narrows the failure surface from "anything" to
  "deliberate or careless mislabelling", and the review remains the only thing that catches the rest.
* Bad: the numbered-table layout has no place for `Contested/time-bound`, so bundles using it will keep
  carrying that information elsewhere or not at all. Accepted, because the field is optional by the
  documented standard.

### Confirmation

A new `tools/check-research-logs.py`, run in CI alongside the other document gates
(`check-adr-index.py`, `check-changelog.py`), failing the build when any bundle's research log contains an
entry missing a required field, or contains sources in a layout carrying no per-source retrieval status.

Because the check has branches no live bundle exercises once the three conversions land (a missing tier, an
invalid status token, a URL-less entry without the exemption statement), it carries fixture-based tests per
[ADR 0025](0025-executable-tests-for-gate-logic.md).

## More Information

This closes finding **DF-2** (research-log format drift) in [`STATE.md`](../../../STATE.md), which also records
the two real defects the audit surfaced and fixed on the way: `bug-report` [17] wrote its status as
`not retrieved` where the enum token is `not-retrieved`, and `risk-register` [33] carried no URL for a print
book, now documented as a deliberate absence and the basis of the exemption above.

The authoring rule is written into [`bundle-pipeline.md`](../bundle-pipeline.md) phase 2, so the next bundle
inherits it rather than rediscovering it.
