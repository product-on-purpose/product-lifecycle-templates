# experiment-design-doc: history

Change log for the `experiment-design-doc` bundle. Each entry records what changed and why, so a reader can
tell a correction from a preference.

## 0.1.0 - 2026-10-08

**Initial release.** Admission sweep run 2026-10-05, writing the spec in `tier2-specs.md`; built and researched
2026-10-08 across six parallel dimensions: the product-experimentation canon, the statistical core (minimum
detectable effect, sample size, duration and the decision rule), the academic preregistration and
public-sector evaluation lineages, contested practice, the boundaries with this library's neighbours and
with in-tool experiment surfaces, and the standing-instrument gap question.
[`experiment-design-doc_research-log.md`](experiment-design-doc_research-log.md) records **35 sources, all
fetched-and-verified**. Every quotation was checked against the source's raw text rather than a retrieval
tool's summary, and every page first cached during the build was checked a second time against a fresh
download.

**The first founding member of the `experimentation-docs` family**, adopted by
[ADR 0066 (adopt the experimentation-docs family contract)](../../docs/internal/decisions/0066-adopt-experimentation-docs-family-contract.md)
on `phase: measure`, the first family contract to use that phase value. The family's second member,
`experiment-readout`, is built after this one so that its example reports the test this document plans.

### What the document carries, and what it deliberately does not restate

**It leads with what the PRD does not already ship.** A PRD's Success metrics section already names a
primary metric, a guardrail and a measurement window
(`templates/prd/prd_template-full.md:192-207`), so this document starts past that point: the variants and
their allocation, the minimum detectable effect and the sample size or duration it implies, and a decision
rule naming an action for every outcome, including a null one. The guide's own anti-pattern names the
failure directly: a design document that opens by restating the PRD's metrics section, rather than leading
with the variants, the allocation, the minimum detectable effect, and the decision rule, duplicates work the
PRD already did.

**Two sections ship in the full variant only: Tracking and Instrumentation Note, and Validity
Pre-Commitments.** Both are pointers rather than restatements. The tracking note names which of the PRD's
own instrumentation events feed this test's metrics, plus the test's own exposure event, and a verification
date; it does not duplicate the PRD's Analytics and instrumentation section
(`templates/prd/prd_template-full.md:209-223`). The Validity Pre-Commitments section's name and grouping are
this library's own synthesis - no single source in the research names a section with this exact scope - and
it combines several individually sourced checks: sample ratio mismatch, peeking, shutdown for harm, ramp-up,
novelty effects and fixed segments, overlap with concurrent experiments, and risks and notification.

### One live methodological question is named rather than settled

Whether the statistical framework a test runs on (fixed-horizon, sequential or Bayesian) is a per-program or
a per-test choice is unresolved across the sources. Spotify Engineering argues for a program-wide choice,
stated explicitly as its own current, time-bound position rather than a settled industry answer; a separate
practitioner guide frames the same choice per test, as a trade between confidence and time. The Minimum
Detectable Effect section asks the author to name the framework the team's platform actually runs rather than
choosing one for them, and no power level or significance threshold is presented as a default.

### Statistics found and deliberately not presented as norms

**Microsoft's own reported 7-day typical test duration is attributed to Microsoft, not presented as a
field-wide convention.** The same source and a separate practitioner's classic piece both derive duration
from the effect size and expected variance rather than from a fixed number, and the guide's own anti-pattern
names presenting seven days as a standard duration as a failure mode in its own right.

**Two vendors' claims that interaction effects between concurrent experiments are rare are reported as each
vendor's own position, not adopted as fact.** One of the two sources attributes its version to unread
Microsoft research. A separate checklist and a tracking-field convention both treat overlap as something a
design document should handle. The bundle does not resolve the disagreement; it asks the author to state how
this test handles the question.

**Spotify Engineering's own 2025 learning-rate and win-rate figures, and a secondary 2022 account of
Netflix's confidence-level practice, are both attributed to their own organizations rather than generalized
as industry norms.**

### Attribution correction carried into the bundle

**An early research pass attributed to Adam Fishman a claim he does not make.** One dimension reported that
Fishman "reports that most experiment failures trace back to" a specific small set of causes. That string
does not appear on his page; what he actually writes is narrower and carries no frequency claim at all: "it
IS a failed experiment if you can't learn something reliable due to poor design." The companion's anti-pattern
section states the correction and the fix rule: state the design principle Fishman actually makes, and do
not borrow a frequency claim no source makes.

### A guidance note flagged unverified, not deleted

The catalog row's guidance note, "NN/g: define metrics in advance; power analysis," was checked during the
2026-10-05 admission sweep against the one NN/g source read, the UX Research Methods glossary, which was
cited only for its definition of concept testing, a different document type, never for metrics-in-advance or
power-analysis guidance. The note is carried as unverified rather than deleted or treated as sourced.

### No paired pm-skills skill

`pairs_with` ships `[]`. No skill ID in `tools/known-skills.txt` names experiment design, A/B testing, or
hypothesis-driven measurement; this bundle makes no pairing claim rather than guessing one.

### The honest core

**No source measured whether writing this document improves an experiment's outcome.** The case for it rests
on practitioner testimony and on the statistics of what goes wrong without a pre-committed stopping rule -
chiefly that committing to a sample size in advance is what prevents the inflated false-positive rate that
peeking produces - not on a controlled comparison of documented against undocumented tests. The companion
states this plainly in its opening section, because a reader should not infer a stronger claim than the
sources make.
