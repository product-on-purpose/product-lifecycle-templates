# positioning-statement: history

Change log for the `positioning-statement` bundle. Each entry records what changed and why, so a reader can
tell a correction from a preference.

## 0.1.0 - 2026-10-20

**Initial release.** Researched 2026-10-20, building on admission sweep 6 (2026-10-14) and the sitting
follow-up of 2026-10-15. The build's six-dimension fan-out covered the canon (the formula, its published
field sets, and its disputed origin), April Dunford's components, process and critique, who owns the
statement, its boundaries with vision, strategy, messaging and the battlecard, when it is revisited, and
the library's own neighbours and the Acme Analytics chain.
[`positioning-statement_research-log.md`](positioning-statement_research-log.md) records **59 sources**, of
which 57 were fetched and verified, 1 was confirmed to exist without the body being read, and 1 could not be
retrieved. Every quotation was checked against the source's raw text rather than a retrieval summary,
leaving **297 Quotable lines**.

**The sixth `strategy-docs` member, added by amendment rather than at the family's founding**, admitted by
[ADR 0076 (positioning-statement joins strategy-docs as a sixth member)](../../docs/internal/decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md),
which also amended the family contract to 0.3.0 and placed this type third in the chain, between the
product strategy and the North Star metric. That placement is this library's own POSITION, not a sequence
any one source states; the considered alternative places it second, between the vision and the strategy, on
Devika Nair's framing of positioning "as part of the vision."

### One size only, by the research's own finding

This bundle ships `lean` and no `full`. Every admitting source caps the artifact at one page or a few
sentences: MIT's template is a one-page format, HubSpot and Yesware both give a three to five sentence
ceiling, and Product Marketing Alliance's own template is a one-page, five-row document. April Dunford's own
material is longer, a workbook she gives her newsletter subscribers, but the research reads that workbook as
a facilitation process for arriving at the one-page statement, not a second, heavier version of the
statement document itself; its content belongs in the guide, not in a second template size.

### Admission does not rest on Geoffrey Moore

Three independent research passes could not locate the "for/who/that" wording inside *Crossing the Chasm*
itself, by edition, chapter, or page. Admission is credited to the five sources the research log marks
`fetched-and-verified` for the formula itself (MIT, HubSpot, eCornell, Yesware, Product Marketing Alliance).
Moore is named in the template and companion only as an unverified practitioner attribution, never as a
sourced fact, and the catalog's own prior attribution to him is corrected on landing.

### Ownership is recorded as a split, not a consensus

Two independent sources place ownership of the statement with product marketing, one of them by name
(Blackblot). A separate pair of sources supports placing it with product management instead. The catalog's
`owner` field becomes `PMM / PM`, by the maintainer's ruling of 2026-10-17, and the guide presents both
camps with their sources before suggesting a default; that default is labelled this library's own reasoning,
never a reported consensus.

### What the document does not carry

Nothing in the template carries a messaging deliverable, a battlecard, or a positioning map. The catalog
alias "positioning map" is dropped on landing: it names a two-axis competitive chart, a different,
out-of-scope artifact under this library's Markdown-document templating scope, not an alternate name for the
written statement.

### Open questions this research did not settle

No source read states a review cadence for the positioning statement itself; `classification: foundation`
is recommended on an inference from the admission case (the statement recurs at a repositioning event, not
on a calendar), not on a quoted cadence. Whether the type's chain placement belongs third, between strategy
and the North Star metric, or second, between vision and strategy, is argued rather than sourced; the
companion carries both and names third place the library's own recommendation at low confidence.

### pairs_with and related_templates

`pairs_with` ships empty. [`tools/known-skills.txt`](../../tools/known-skills.txt) was checked against this
type's own job on 2026-10-20 and contains no skill ID with "position" or "messag" in it. An empty list is the
honest answer, not a gap to paper over.

`related_templates` names `product-vision`, `product-strategy`, `north-star-metrics` and `okrs`, the four
siblings this type's companion states a position against in its Relationships section. `product-vision` and
`product-strategy` are the two sources the worked example is dated and scoped against: the example sits two
days after the 2026-01-28 `product-strategy` example and carries forward its target segment, and names the
`product-vision` example's alternative wording as the deliberate difference between the two document types.
