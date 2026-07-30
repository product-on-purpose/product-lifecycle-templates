# okrs: history

Change log for the `okrs` bundle. Each entry records what changed and why, so a reader can tell a correction
from a preference.

## 0.1.0 - 2026-07-30

**Initial release.** Researched 2026-07-29 across five parallel dimensions: origins and canon, structure and
formats, the evidence base, debates and failure modes, and relationships and practice; drafted and reviewed
2026-07-30.
[`okrs_research-log.md`](okrs_research-log.md) records **78 sources**, of which 64 were fetched and verified,
9 had their URL confirmed without the body being read, and 5 could not be retrieved.

**The fourth and final `strategy-docs` member**, completing the family adopted in
[ADR 0027 (the strategy-docs family contract)](../../docs/internal/decisions/0027-adopt-strategy-docs-family-contract.md)
and, with it, one continuous worked thread from a product vision down to a bug report.

### One format ships

[ADR 0028 (the format-axis rule)](../../docs/internal/decisions/0028-adopt-a-format-axis.md) admits a format
only when it is **structurally distinct AND in circulation with a named source**. **Six candidates were
examined individually and five rejected**, and a further **nine named goal-setting frameworks** were checked
for a counterexample, which is the last row. The two tiers are stated separately on purpose, because they
received different scrutiny and because collapsing them is how the sibling bundle came to claim "eight
researched, five rejected" while naming six rejections:

| Rejected | Ground |
|---|---|
| **V2MOM** (Benioff, Salesforce) | **Its own author does not present it as an OKR variant.** Genuinely structurally distinct, five components against two, with Values and Obstacles slots OKR has no equivalent for. The Salesforce training unit that defines all five components and tells the origin story does not mention OKRs once |
| OKRs with Initiatives | Not a distinct shape. It is this document's own full form |
| Cascading / tiered OKRs | An organisational process, not a document anatomy. The document at every tier has the same two parts |
| Vendor canvases and scorecards | Competing tracking layouts on the same anatomy, from no single named author |
| Wodtke's "OKR Four Square" | A named single-author artifact, but a check-in worksheet layered on standard Objectives and Key Results rather than a redefinition of them |
| OGSM, Hoshin Kanri, 4DX/WIGs, Balanced Scorecard and others | Checked for a counterexample and none found. Each is published as a competing framework; where a named author relates one to OKRs, OKRs are nested inside it rather than claimed as a variant of it |

**The rule's unwritten third criterion, recorded rather than hidden.** V2MOM was rejected on a test ADR 0028
does not contain: *does the artifact's own author present it as this type*. This is the **second consecutive
bundle** to reject candidates on that unwritten test, after `product-roadmap` excluded the opportunity
solution tree and Cagan's five-part alternative on the same ground. It has never been applied backwards, and
`product-vision` ships a PR/FAQ that Amazon does not present as a product vision. Either the rule gains a
third criterion explicitly or these two bundles are stricter than their sibling. Routed to the
`default_format` backfill (decision D-E), which already needs its own ADR.

**No `default_format` key is declared.** Having found exactly one shape, this bundle joins the fifteen that
carry no format key rather than declaring a single-member axis, which keeps the D-E decision open instead of
pre-empting it.

### The section design departs from the provisional spec, on evidence

`buildout-specs.md` proposed "Full adds: Initiatives; Owners; Confidence/Check-in." Two changes:

- **Owners became a column, not a section.** Ownership belongs attached to the thing owned, so every Key
  Result and every Initiative carries a named person in its row. A standalone Owners section would have
  invited a list of names with nothing to be accountable for.
- **`Initiatives` ships with its provenance stated in its own guidance comment.** The three-layer Objective,
  Key Result, Initiative structure is **vendor convention, not canon**: one vendor asserts John Doerr's
  framework includes it while citing no page, and Google's own published guide never names the layer at all.
  It earns its place for one reason, that it makes a Key Result nobody is working on visible at a glance, and
  the template says so rather than implying it is original doctrine.

A third section was added that the spec did not anticipate: **Scoring and Close-out**, because the research
found the compensation question to be the one place the practitioner position is close to one-sided, and a
template that lets an author skip it produces sandbagging the following cycle.

### Attribution corrections carried into the bundle

- **The year OKRs reached Google is stated as a contradiction, never as a year.** Doerr's own site says 1998,
  Doerr's own TED talk says 1999, and Google's own guide says "early 2000." Three sources that should be
  authoritative, three different years.
- **The Drucker lineage is labelled plausible and unverified.** It is asserted on Doerr's site with no
  citation to anything Grove said, and the encyclopedia articles on management by objectives and on OKRs do
  not reference each other.
- **Grove-as-inventor is carried with its named dissent**, from an institute arguing OKR and MBO "are based
  on the same principles and follow roughly the same process."
- **The "I will [Objective] as measured by [Key Results]" formula is used but not attributed**, because the
  page that states it credits nobody and the book that would settle it could not be retrieved.
- **Committed versus aspirational is attributed to Google**, reported by Doerr rather than invented by him.
- **Three measurement devices are kept apart**: Wodtke's 1-to-10 forecast confidence, Google's 0.0-to-1.0
  after-the-fact grading, and the committed/aspirational target split. Vendor writing merges all three.
- **V2MOM was dropped from the alias list** that `buildout-specs.md` proposed. Listing it as a search term for
  this document type would contradict the finding that its author presents it as a different artifact.

### The honest core

**No study measures whether the OKR artifact improves product or business outcomes.** Goal-setting theory is
real, replicated and old, with meta-analytic effect sizes of .42 to .80 for specific difficult goals against
"do your best," and a genuine adversarial literature alongside it. **Neither side mentions OKRs, quarterly
cadence or scoring anywhere.** The systematic mapping of OKR literature finds 47 primary studies and calls the
topic "under-documented from a theoretical point of view"; the best in-situ industry study measured engineer
perceptions rather than delivery outcomes. The transfer is assumed by vendor content and demonstrated by
nobody, and the one place the adjacent literature touches quarterly cadence at all, it is a warning about
short-termism.

Cadence, the 0.7 target and the 60-to-70-percent sweet spot are all stated conventions with no measurement
behind them, and the bundle says so at each point of use.

### Statistics found and deliberately excluded

Circulating OKR figures were traced where possible and recorded where not. Two attach real institutional
names to studies a direct search could not find. A further set carries no source at all. The most-repeated
impact figures trace to an unpublished internal company analysis that was never peer-reviewed. **A specific
"40 to 60 percent of Key Results should be bottom-up" rule attributed to Doerr was checked against his own
organisation's cascading FAQ, which gives no percentage at all.** None of these appears anywhere in the
bundle as fact.

### Verified before drafting

**The research log was adversarially verified before any other file was written**, by thirteen agents
re-fetching every load-bearing quote and attempting to refute the headline claims. It found **two fabricated
quotations** in the log, invented during the research fan-out and transcribed unchecked; one misattributed
citation; one paraphrase presented as verbatim; and one absence claim stated more broadly than the evidence
supported. All are corrected, and the log records what was wrong rather than quietly fixing it. The four
headline claims survived, and one was softened because the agent commissioned to test it did not complete.
