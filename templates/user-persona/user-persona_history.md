# user-persona: history

Change log for the `user-persona` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-08-05

**Initial release.** [`user-persona_research-log.md`](user-persona_research-log.md) records **45 sources**,
of which **33 were fetched and verified** and **12 could not be retrieved**; none sit at the middle,
url-confirmed-not-read, tier.

**The second `discovery-docs` member built**, in the family adopted by
[ADR 0031 (discovery-docs family contract)](../../docs/internal/decisions/0031-adopt-discovery-docs-family-contract.md).
It answers the second of the family's three ordered questions, who a product is being built for, following
`business-case` and preceding the still-provisional `prototype-brief`.

### One format ships, and the anti-persona departs from the build spec

Under [ADR 0028 (the format-axis rule)](../../docs/internal/decisions/0028-adopt-a-format-axis.md), four
candidates were checked against six published formats read in full. The profile-led persona, identity, goals,
pains, ships as the baseline, carried by five of the six formats read. The proto-persona was rejected as a
format: it is not a different document shape, only a lighter evidence tier of the same one, and is taught in
Evidence Basis rather than shipped as a second outline. The buyer persona, built on the Buyer Persona
Institute's 5 Rings of Buying Insight, is genuinely structurally distinct and answers a different question,
the purchase decision rather than product use; it stays out of scope and the boundary is taught, not shipped.

**The anti-persona departs from `buildout-specs.md` on the evidence available.** The spec proposed a
standalone Anti-persona section under `full`. Only two sources address anti-personas at all, and the one that
speaks to packaging builds and publishes it as its own artifact, "created data-based just like a buyer
persona, only 'the other way around.'" No source read presents it as a section inside a persona, so it ships
as a named sibling document in the companion's Relationships section instead. This is recorded in the
research log's contested register as a departure on one source's packaging evidence, not a refutation, and a
second source either way would settle it.

Two further sections depart from the spec on the same kind of evidence. A standalone "Behaviors" section
appears in only one of the six formats read, so this bundle folds the same material into Context of Use, the
label the closest-matching source actually uses. A bounded "Quotes/Evidence" section appears in none of the
formats read, except where verbatim buyer voice is the entire document, a different artifact; this bundle
instead ships Evidence Basis, a declared evidence-tier field, which is what every format actually needed and
none of them supplied under that name.

### Product-management literature is split four ways, not hostile or silent

Unlike `business-case`, where the product-management literature was found hostile or silent, this research
found it disagreeing with itself. Klement argues for outright replacement, on the ground that filling persona
gaps with invention is "disinformation." Nielsen Norman Group names that position and rebuts it as compatible
rather than competing. Cagan's SVPG publishes a persona how-to with no argument for or against the method at
all, unexamined use rather than endorsement. Teresa Torres's canonical discovery material never mentions
personas anywhere, an absence observed in a document that was read, not an inference about her views. The
bundle states the four-way split as the teaching point it is rather than picking a side.

### A statistic was retrieved, read, and disqualified on its own method

The circulating 900 percent website-visit-duration figure was traced to its source and read in full: a single
MarketingSherpa case study of one company that bundled persona work with a full site redesign, a content
overhaul, and an email-automation change, with no comparison group and no isolation of the persona variable.
The number is real; it supports nothing about personas and does not appear in this bundle as fact. The
research log notes the contrast with `business-case`, whose comparable statistics could not be retrieved at
all; here retrieval succeeded and the number still had to be quarantined.

### The academic critique is carried at its actual strength, not softened

Chapman and Milham's peer-reviewed 2006 paper is the sharpest source this research read, and its claim is
kept at its stated severity: personas are "outside the scientific method and cannot be verified," with "no
adequate studies addressing the reliability, validity, or utility of the method." The same paper supplies the
curse-of-dimensionality finding, worked through to roughly 134 people in the United States for a
21-attribute example, which this bundle teaches as a concrete design rule rather than an abstract warning:
every field a template adds makes the persona describe fewer real people.

### What the three central books could not settle

*The Inmates Are Running the Asylum* chapter 9, *About Face*, and Pruitt and Adlin's *The Persona Lifecycle*
are the three works a reader would most expect this bundle to cite, and none was reachable as full text. The
publisher's free sample of *Inmates* stops at front matter, so chapter 9's section titles are recorded from
its table of contents only, never from chapter prose. Nothing in this bundle states what any of the three
argues; the gap is named in the companion rather than filled with an inference.

### The chronology obligation

Per the discovery-docs family contract, the worked example, Elena Cho, is dated 2026-01-05, nine days ahead
of the product vision agreed 2026-01-14, and ahead of every other example in the library's shared Acme
Analytics thread. It defines the Recurring Analyst that the vision's reader aside names, the `kpi-dashboard`
metric definitions track, and the `acceptance-criteria` example's story assumes, without any of those
documents ever having defined her. It cites none of them, and cites no PRD, because none existed yet when it
was written; it rests only on interviews and a support-ticket review conducted before that date.
