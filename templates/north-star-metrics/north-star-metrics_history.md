# north-star-metrics: history

Change log for the `north-star-metrics` bundle. Each entry records what changed and why, so a reader can
tell a correction from a preference.

## 0.1.0, corrected 2026-10-20 - the North Star now sits fourth in the chain

**A chain-position correction, not a template change**, so the version stays 0.1.0. The
`positioning-statement` bundle joined `strategy-docs` on 2026-10-20, third in the chain, by
[ADR 0076 (positioning-statement joins strategy-docs as a sixth member)](../../docs/internal/decisions/0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md),
so the family contract already puts the North Star fourth. The example's opening note and two companion
sentences still said "third", and each now carries a dated note saying fourth. Nothing was rewritten in place.

## 0.1.0 - 2026-10-12

**Initial release.** Researched 2026-10-12, building on the admission sweep of 2026-10-05. Six dimensions
ran: origins and canon, the structure of a written North Star document, input metrics, debates and cadence,
relationships with this family's other documents, and the standing gap question.
[`north-star-metrics_research-log.md`](north-star-metrics_research-log.md) records **54 sources**, of which
47 were fetched and verified, 6 had their URL confirmed without the body being read, and 1 could not be
retrieved. Every quotation was checked against the source's raw text rather than a retrieval summary; 60 of
353 filed quotations failed that check and were dropped, leaving 343 quotations on 42 sources.

**The fifth `strategy-docs` member**, admitted by
[ADR 0070 (north-star-metrics joins strategy-docs as a fifth member)](../../docs/internal/decisions/0070-north-star-metrics-joins-strategy-docs-as-a-fifth-member.md),
which also amended the family contract to 0.2.0 and placed this type third in the chain, between the
product strategy and the product roadmap. That placement is inferred from the camp of sources describing a
North Star as measuring the *current* strategy, not stated as a sequence by any one source, and the contract
names it a POSITION rather than a finding.

### Both sizes ship

The full variant is held to the spec's stop condition: if the research could not support it, the build
would stop and report rather than pad one. It did not stop. Each of the four full-only sections rests on at
least two independent publishers outside Amplitude's own two documents: Candidates Considered, Guardrails,
What It Does Not Tell Us and Definition History. Guardrails in particular rests on three sources
([49], [51], [10]) that use the word for a standing companion metric; Amplitude's own two documents never
use it that way, and two other vendors ([25], [11]) scope the same word to a single experiment's safety
check instead. The full variant's section is explicit about resting on the first group, not on Amplitude's
canon.

### What the document does not carry

Nothing in either variant carries a formula, a data source, a refresh schedule, a target, a threshold, a
dashboard layout, or a tree of metrics below the inputs. That boundary is the maintainer's own ruling of
2026-10-12, not a gap the research found: those belong to `kpi-dashboard`, which this bundle's Relationships
section and guide both point to directly.

### Open questions this research did not settle

Who coined the term "North Star Metric," and whether Amplitude invented the practice described in its own
playbook, is not established by anything this research read firsthand; the companion's Origins section
states this as an open question rather than a finding. Where the North Star sits relative to the product
strategy and OKRs is contested across the sources read; this library's placement is recorded as a POSITION
in the family contract, not asserted here as settled practice.

### pairs_with and related_templates

`pairs_with` ships empty. Every pm-skills skill ID in [`tools/known-skills.txt`](../../tools/known-skills.txt)
was checked against this type's own job; none of the thirteen pinned IDs, including the three already paired
to this family (`foundation-okr-writer`, `measure-okr-grader`, `foundation-lean-canvas`), address naming a
North Star metric and its inputs. An empty list is the honest answer, not a gap to paper over.

`related_templates` names `product-vision`, `product-strategy`, `product-roadmap`, `okrs` and
`kpi-dashboard`, the five siblings the companion's Relationships section (section 8) states a position
against. `product-vision` and `product-strategy` are the two sources the worked example is dated and scoped
against: the example quotes the 2026-01-14 `product-vision` example verbatim twice and the 2026-01-28
`product-strategy` example verbatim once, and reuses that strategy example's baseline and leading and
lagging figures exactly, rather than inventing its own numbers.
