# Version history: product-roadmap

Every change to this bundle's templates, with the reasoning. The version here must match
`template_version` in [`product-roadmap_meta.yaml`](product-roadmap_meta.yaml); gate check H enforces that.

## 0.1.0 - 2026-07-28

First release. Status `beta`: gate-green and cited to raw sources, with no fills by anyone but the author.

**The bundle that tested the format rule hardest, and the rule held.**
[ADR 0028](../../docs/internal/decisions/0028-adopt-a-format-axis.md) admits a format only when it is
**structurally distinct AND in circulation with a named source**. Roadmap shapes proliferate more than any
other product artifact, so this was the case most likely to expose a rule that waves everything through.
Eight candidates were researched. **Three qualify and five were rejected**, on three different grounds:

| Rejected | Ground |
|---|---|
| Timeline / Gantt | No contemporary named product-management practitioner was found defending the bar-and-dependency form as a roadmap, despite a search aimed specifically at finding one. Recorded as a research gap, not a confirmed absence |
| Release plan | A different artifact category, by the account of the person who named both |
| Release roadmap | A relabel of the timeline form, vendor terminology, no named champion |
| Kanban board | No named practitioner publishes it as a roadmap format |
| **Opportunity solution tree, and Cagan's OKR-based alternative** | **Their own authors do not present them as roadmaps.** One is a discovery artifact, the other is explicitly an alternative *to* roadmaps |

That last row is the most useful result in this bundle. The rule rejected two well-known, well-structured
frameworks that a careless author would have shipped as roadmap variants, on the grounds that their creators
say they are something else.

**Three formats ship.** `now-next-later` is the default: its lanes are confidence levels rather than dates,
which makes it the only one showable to a customer without implying a schedule. `go` ships for teams whose
releases are real events needing a measurable goal each. `themes` ships for when the roadmap has to travel
and argue for itself, carrying vision and objectives inside the document.

**Two of the three carry a section their published originals do not:** "What Is Not On Here", added to the
GO and themes formats and marked as this bundle's addition in each. A goal grid and a themes list both fill
up without ever recording a refusal, and a roadmap that cannot be cited to decline a request settles no
arguments. This follows the `product-vision` and `product-strategy` precedent of putting the refusal section
in the smallest variant rather than treating it as an optional extra.

**The honest core is a confirmed evidence gap, plus a real convergence that is not evidence.** No study
links any roadmap format, cadence or confidence device to product or business outcomes; arXiv, Semantic
Scholar and general web search were all tried. What does exist is four named practitioners arriving
independently at the same principle: express less certainty, further out. The companion teaches that
convergence and says plainly that a convergence of prescription is not a measurement.

**Two circulating statistics were found and deliberately excluded.** A "60-70 percent less maintenance work"
claim for now-next-later roadmaps, and a "38 percent of best-performing companies" correlation between
roadmapping and innovation success. Neither could be traced to any study. They appear nowhere in this
bundle, and the research log records that they were found and rejected, because the next author to research
this type will meet them too.

**The bundle refuses to be a polemic.** The literature on roadmaps is dominated by criticism, and quoting
only the critics would have been easy and wrong. Three credible defences of dated roadmaps are carried:
an enterprise framework that commits its nearest increment while labelling the next two a forecast, an
enterprise-sales argument for buffered committed dates, and hardware validation gates that impose real lead
times. The critics concede more than their reputations suggest, and the bundle records that: the most-cited
opponent of feature roadmaps also writes that roadmaps are "one of my favorite tools. When done right."

**Attribution corrections carried into the bundle.** Now/Next/Later has **two** named creators, not the one
most secondary sources credit, and its 2012 date rests on a retrospective account that could not be checked
against a period artifact. A competing vendor republishes the format with no attribution at all. "Themes"
is credited to Bruce McCarthy through a single account. Product Roadmaps Relaunched was never read; its
five-part structure is summary-reported and labelled as such wherever it appears.

**The sharpest checkable fact in the bundle:** the word "roadmap" does not appear anywhere in the Scrum
Guide, confirmed by direct text search. Whatever process a team runs, this artifact sits outside it.
