# business-case: history

Change log for the `business-case` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-08-05

**Initial release.** [`business-case_research-log.md`](business-case_research-log.md) records **43 sources**,
of which 33 were fetched and verified, 2 had their URL confirmed without the body being read, and 8 could not
be retrieved.

**The first `discovery-docs` member built**, the family adopted by
[ADR 0031 (discovery-docs family contract)](../../docs/internal/decisions/0031-adopt-discovery-docs-family-contract.md).
`business-case` itself arrives in this family from `strategy-docs` by
[ADR 0023 (the Tier-1 family taxonomy)](../../docs/internal/decisions/0023-resolve-the-tier-1-family-taxonomy.md),
which moved it on the reasoning that a one-time, phase-bound artifact does not belong in a family of standing
instruments.

### The Five Case Model ships as the spine, and the alternative is named rather than shipped

Every standard the research could read in full treats the business case as a living document, revisited as
the work proceeds, not a one-time gate. The traditions disagree on mechanism rather than principle: PRINCE2
keeps one document revised in place, while the UK government model stages three separately gated documents,
a Strategic Outline Case, an Outline Business Case, and a Full Business Case. This bundle ships the staged
Five Case Model as its spine and teaches the living-document discipline as practice, not as a second format.

**The SAFe Lean Business Case was considered and not shipped.** It substitutes an Epic Hypothesis Statement
and leading indicators for a financial case, which is a structurally different document rather than a
shorter one. It stays out because the research read only a practitioner mirror of the format, not Scaled
Agile's own publication, and is named in the guide and companion as a tradition a reader should know about
rather than reinvent.

### Product-management literature is hostile or silent, and the bundle says so plainly

No source this research found makes a positive case for the artifact from a product-management perspective.
Cagan names the funding cycle almost verbatim in order to reject it, elsewhere concedes the artifact serves
investment decisions while denying it is product management's job, a secondary treatment of Perri's
*Escaping the Build Trap* does not engage the topic at all, and a targeted search of Teresa Torres's
published material surfaced no use of the term anywhere in her vocabulary. The bundle states this as the
finding it is rather than implying an endorsement that was not found.

### Contested claims presented as contested, not resolved

**Whether IRR assumes reinvestment at the IRR rate is a live split.** Academic finance says there is no such
assumption built into IRR or NPV; the practitioner source a business-case author is far more likely to
consult states it as a defining flaw of the method. Both sides are given, and neither is picked.

**Whether real options analysis is an advance on discounted cash flow or a source of false confidence is
also left open.** One source argues it prices a genuine gap that plain discounting cannot capture; the UK
government's own appraisal guidance warns the same technique can introduce spurious accuracy.

### A cluster of statistics is quarantined rather than cited

The well-known benefits-realisation figures that circulate in practitioner writing, each attached to a named
primary source, could not be independently verified here. One of the two sources checked for this cluster
does not contain the figure attributed to it in the pages read. No figure from that cluster appears in this
bundle as fact, and its absence is itself named as a teaching point in the companion.

### A retrieval gap is named rather than papered over

PMBOK 7, ISO 21502, and ISO 21500 are named in the build spec as key sources for this document type, and
none could be retrieved past its publisher's paywall. Nothing in this bundle states what any of the three
argues; the gap is recorded in the companion rather than filled with an inference.

### The chronology obligation

Per the discovery-docs family contract, the worked example is dated 2026-01-20, ahead of every other example
in the library's shared Acme Analytics thread: six days before the leadership review it requests, and eight
days before the FY26 product strategy whose Guiding Policy and Coherent Action sections spend the investment
it argues for. It cites only the product vision, agreed six days earlier, and Acme's own telemetry, and does
not cite the strategy or the roadmap, neither of which existed yet when it was written.
