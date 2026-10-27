# experiment-readout: history

Change log for the `experiment-readout` bundle. Each entry records what changed and why, so a reader can
tell a correction from a preference.

## 0.1.1 - 2026-10-26 - a ratio metric gets its own numerator and denominator check

**Applies a proposal from the library's 2026-10-23 resource crawl, approved by the maintainer on
2026-10-25.** Statsig's product-experimentation best-practices post states that a ratio metric's overall
value can move opposite to the change in its own numerator and denominator, and recommends checking both
separately.

- The Key Results: Primary Metrics section's TRAP line, in both the lean and the full variant, now names
  this hazard as a risk in reading the result, separate from whether the comparison itself can be
  trusted.
- The companion's Key Results: Primary Metrics section gains one sourced sentence citing the new entry,
  [`experiment-readout_research-log.md`](experiment-readout_research-log.md) entry 28, Statsig's "Product
  experimentation best practices," the same source the sibling bundle cites, homed differently here.
- `template_version` moves to 0.1.1. The worked example's own `source_template_version` stamp is left at
  0.1.0.

## 0.1.0 - 2026-10-11

**Initial release.** Admission sweep run 2026-10-05, writing the spec in `tier2-specs.md`; built and researched
2026-10-11, extending the six-dimension fan-out the sibling bundle used: the product-experimentation canon,
contested practice (learning, archives and who decides), the boundaries with this library's neighbours and
the worked example's commitments, reporting honestly (validity checks, uncertainty and the named traps), the
two non-product lineages, and the standing-instrument gap question.
[`experiment-readout_research-log.md`](experiment-readout_research-log.md) records **27 sources, all
fetched-and-verified**. Every quotation was checked against the source's raw text rather than a retrieval
tool's summary; pages first cached during the build were re-fetched with the cache bypassed.

**The second founding member of the `experimentation-docs` family**, adopted by
[ADR 0066 (adopt the experimentation-docs family contract)](../../docs/internal/decisions/0066-adopt-experimentation-docs-family-contract.md)
on `phase: measure`. Built after `experiment-design-doc` so that this bundle's worked example reports the
same Saved Views adoption-nudge test that document's example planned, chaining onto the existing Acme
Analytics PRD, KPI dashboard, OKRs and risk-register thread per the family contract's shared-scenario rule
(contract, section 4).

### What the document carries, and what it deliberately does not restate

**It is post-test and decision-bearing.** The document exists after a test has run its course: Optimizely's
own stakeholder guidance is to share results "at the end of each test," and Amplitude names its fourth phase
plainly, "Analyze and Decide." The family contract's own finish line is the recorded decision, not the
reading of the result, and this bundle's Decision section and Decision Owner field carry that line forward.

**Two sections ship in the full variant only: Deep-Dive, and Implementation Details and Analysis Notes, plus
Further Analysis.** The lean variant is the whole artifact for a test with one clear primary metric: an
Executive Summary, Context and Setup, the two Key Results tables, Validity Checks, the Decision, its Owner,
and Next Steps and Owners. The full variant adds the sections a test needs only when the decision rests on
more than that primary read.

### A boundary stated from this side alone

**`test-summary-report` (`qa-docs`) never states its own collision with this bundle.** A case-insensitive
search of `templates/test-summary-report/test-summary-report_guide.md` for "experiment," "hypothesis" and
"A/B" returns nothing, while `test-plan_guide.md:27` names its own collision under the heading *Your tool
already has a "test plan"*. This companion states the distinction from the readout's side: a test plan and
its summary report verify a product increment against an agreed specification and grade it pass or fail,
with no hypothesis, no allocation between variants, and no statistical decision rule; this document
estimates an effect against a baseline and reports a ship, iterate, or stop decision.

### Scope: the written readout only, not a live scorecard or a one-time export

Optimizely's Experiment Scorecard is a live, configurable in-tool surface, not a document; Statsig's export
is a one-time PDF of setup facts and metric-by-metric raw stats, with no decision field. Microsoft's own
research answers whether evaluation can be automated from metric movements alone with "Not quite," because
"the experimentation platform typically has limited context about the experiment itself." No source read
says a scorecard or an export replaces a written readout or sits beside one; that boundary is the library's
own, under [ADR 0030](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md).

### Claims left contested rather than resolved

**Whether a design doc and its readout belong in one document or two was decided by the maintainer, not by
the research.** Sources split: Optimizely's own template distributes plan and results across one page, while
a separate practitioner guide keeps the two in one document with "four distinct parts." The maintainer ruled
for two bundles in [ADR 0066](../../docs/internal/decisions/0066-adopt-experimentation-docs-family-contract.md);
the guide names the one-document alternative for a team that keeps one living document instead.

**What a null result is worth is left to the author to state, not chosen for them.** One source counts a
powered null as a result in its own right; a separate account describes a team shipping on a north-star gain
while secondary metrics held, a different acceptance ground. The bundle asks the author to state which
ground the design doc fixed rather than picking one as a default.

**"Ship, iterate or stop," the Validity Checks section, and the Decision Owner field are this library's own
position, not a sourced convention.** No single source names a section with this exact scope; the companion
labels this plainly rather than citing a source that does not exist.

### No paired pm-skills skill

`pairs_with` ships `[]`, matching the sibling bundle. No skill ID in `tools/known-skills.txt` names
experiment results, readouts, or post-test decision reporting; this bundle makes no pairing claim rather than
guessing one.

### The honest core

**No source measured whether writing this document improves a decision.** The case for it rests on the
failure modes the sources name (peeking, cherry-picking, a loss reported as a win) and on keeping a record a
later reader can audit, not on a controlled comparison of documented against undocumented tests. The
companion and guide both state this before anything else, because a reader should not infer a stronger claim
than the sources make.
