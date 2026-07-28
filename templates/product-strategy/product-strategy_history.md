# Version history: product-strategy

Every change to this bundle's templates, with the reasoning. The version here must match
`template_version` in [`product-strategy_meta.yaml`](product-strategy_meta.yaml); gate check H enforces
that.

## 0.1.0 - 2026-07-28

First release. Status `beta`: gate-green and cited to raw sources, with no fills by anyone but the author.

**The second bundle to ship more than one format, and the evidence that format variation is not peculiar to
`product-vision`.** [ADR 0028](../../docs/internal/decisions/0028-adopt-a-format-axis.md) deferred the
15-bundle `default_format` backfill until `product-strategy` and `product-roadmap` showed whether their
formats vary the way vision's do. This bundle is half that answer, and it is yes: the research found named,
structurally distinct, in-circulation shapes with no shared section list, and applied the ADR's own rule
(structurally distinct AND in circulation with a named source) to ship two of them.

**Two formats, not five.** The kernel (diagnosis, guiding policy, coherent action) is the default because it
forces the obstacle to be named, which is the defect the sources agree on most. The one-pager is a
Playing-to-Win choice cascade, shipped because it opens with a different question rather than a different
layout. Three further candidates were researched and **not** shipped: Ramp's seven-question template is one
company's document rather than a named reusable format and is described in the guide instead; the Perri and
Reforge strategy cascades describe a system of documents at different altitudes rather than one document, so
they are a placement note in the companion; and A3 or Hoshin Kanri, though real strategy-deployment methods,
had no named product-management practitioner publishing them for this artifact.

**"What We Are Not Doing" ships in the LEAN variant**, following the `product-vision` precedent for the same
reason: it is the section that makes the others usable, and every quality test found in the research turns on
it. A strategy nobody could disagree with has not chosen anything.

**The section design departs from the provisional spec, on evidence.**
[`buildout-specs.md`](../../docs/internal/buildout-specs.md) sketched Focus, Insights and Strategic Bets for
lean, with Target Segments, Principles and What We Are Not Doing added at full. The research put the kernel
in its place: it is the most-cited structure in the field, it is the one that forces a diagnosis, and its
three parts are quoted verbatim from Rumelt. The spec's sections survive in the full variant and in the
one-pager format, where they fit the cascade better than they fit the kernel. Per the spec's own note, the
per-type designs are hypotheses to be tested against a type's research, as `test-case` already demonstrated
against a catalog size call.

**The honest core, and it is a negative.** No study measures whether writing a product strategy document
improves product outcomes. The bundle says so and shows the search that establishes it, because a *tested*
negative is worth more than an untested assumption. The adjacent literature on strategic planning as a
process is genuinely mixed, and one study of 77 listed firms found no correlation with objective financial
performance while finding one with what managers believed it had done. That result is carried into the
companion, because "everyone felt it helped" is the most likely defence of a document that is not working.

**Attribution hazards found and avoided.** The research surfaced four, all recorded in the research log:
"the crux" is vocabulary from Rumelt's 2022 book and is routinely blended into explanations of the 2011
kernel; the widely circulated "Product Strategy Canvas" is attributed to Roman Pichler by many sources and
appears nowhere on his site; Melissa Perri's 2016 and 2018 structures differ and are often presented as one;
and Rumelt's own McKinsey essay could not be retrieved in six attempts across three research passes, so
every Rumelt quotation in this bundle is either from a quotations page or explicitly attributed to the
practitioner rendering it.
