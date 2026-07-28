# Version history: product-vision

Every change to this bundle's templates, with the reasoning. The version here must match
`template_version` in [`product-vision_meta.yaml`](product-vision_meta.yaml); gate check H enforces that.

## 0.1.0 - 2026-07-26

First release. Status `beta`: gate-green and cited to raw sources, with no fills by anyone but the author.

**The first bundle in the library to ship more than one format.** It carries a canvas (lean and full), a
narrative (full), and a PR/FAQ (full), under the format axis adopted in
[ADR 0028](../../docs/internal/decisions/0028-adopt-a-format-axis.md). The three are siblings, not sizes:
none of their outlines is a subset of another, and the gate asserts no nesting relationship between them.

**Why three formats rather than one.** The research found four named shapes in circulation and, more
importantly, found that the two practitioners who have written most directly about the product vision
disagree about whether a fillable template can do this job at all. Roman Pichler published a five-cell board
in 2011 and has maintained it since; Marty Cagan writes that one should not expect a fill-in-the-blanks,
canvas or board approach to produce a strong vision. Shipping only the canvas would have taken a side while
quoting the objection, so the bundle ships the canvas, the prose form Cagan argues for, and the Amazon PR/FAQ,
and lets the reader choose. The positioning-sentence shape is the one circulating form deliberately **not**
shipped: the template attributed to Geoffrey Moore could not be verified in any source read across two
research passes, and a positioning statement answers a different question than a vision does.

**Section design.** The canvas lean variant carries four sections: The Vision; Who It Is For, and What They
Need; Why Us; What This Rules Out. The fourth is in the *lean* variant rather than the full one on purpose.
The sharpest test any source offers for a product vision is whether it can be used to refuse a plausible
request from an influential stakeholder, so the section that makes the other three usable is not an optional
extra. The full variant adds Market and Competitive Context, Business Goals, Horizon and Review, and Leaps of
Faith.

**Two research passes, and the second corrected the first.** The first pass concluded there was no empirical
evidence base for vision, on the strength of one paywalled paper it could not read. Three relevant studies
exist. None measures a product vision *document* against product-team outcomes, so the bundle still makes no
performance claim, but now for a defensible reason rather than a false one. The first pass also could not
find a primary source for the "stubborn on vision, flexible on the details" aphorism; Amazon's 2020
shareholder letter contains a close statement in Jeff Bezos's own words, and the bundle quotes the letter
rather than quoting someone quoting it. Full detail, including four attribution verdicts and 52 annotated
sources, is in [`product-vision_research-log.md`](product-vision_research-log.md).

**Attribution hazards this bundle deliberately avoids**, because misattribution rather than staleness is this
subject's characteristic failure mode: it does not credit Collins and Porras with a product vision framework
(they wrote about companies, and the 1996 HBR article postdates the 1994 book rather than preceding it); it
does not reproduce the Moore positioning template as canon; it names no individual as the originator of the
Amazon PR/FAQ, because no readable source does; and it does not use the Saint-Exupery ship quote, which
appears in none of his published work and traces to a 1999 Usenet post where it was already misattributed.
