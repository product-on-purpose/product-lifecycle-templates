# Two-scenario eval, 2026-09-03

**Verdict: the first run that is not void.** All four validity gates pass and the bootstrap is
non-degenerate for the first time, so this run produces a countable gap with a real interval rather than a
finding about the instrument.

**What it does not produce is a verdict on the library.** Two scenarios, both `prd`. Nothing here
generalises past that one bundle, and the protocol's standing rule against cross-bundle ranking applies
with full force.

| | Generation | Judging | Panels | Scenarios | Arms | Drafts |
|---|---|---|---|---|---|---|
| Run | `claude-sonnet-5` | `claude-sonnet-5` | 2 per scenario, 3 judges each | **2** (`prd-001`, `prd-002`) | T, T+, C, H | 2 per arm |

Harness: [`output-eval.workflow.mjs`](../harness/output-eval.workflow.mjs), unchanged.
Prompts: control [version 1](../harness/control-prompt.md), treatment [version 1](../harness/treatment-prompt.md), both unchanged.
Raw rows: [`2026-09-03_two-scenario_raw.json`](2026-09-03_two-scenario_raw.json), **60 judge-artifact rows**.
38 agents, 0 errors, 0 empty results, **11 minutes wall clock**, **2,364,791 subagent tokens**.

**One alteration to the raw rows, stated rather than made silently.** Five em-dashes appeared inside judge
notes, and this repository bans that character in every tracked file with a repo-wide CI sweep. **Each was
replaced with a spaced hyphen and nothing else changed.** The scores were not touched. The two earlier raw
files carry judge notes and zero em-dashes, so this is the established handling rather than a new one.

---

## Why this run exists

[The 2026-08-21 run](2026-08-21_first-runnable.md) was mechanically clean and still returned no verdict,
because it ran **one** scenario. The bootstrap in [`analyze.mjs`](../harness/analyze.mjs) resamples
**scenarios, not judge-artifact rows**, on the stated ground that three judges scoring one document are not
three independent observations. With one cluster every resample returns the same value and there is no
interval at all.

Two clusters is the minimum that produces one. **This run exists to cross that line and does nothing
else.** The design is the 2026-08-21 design with the scenario count doubled.

---

## Validity gates, all four passing for the first time

| Gate | Target | Measured | Result |
|---|---|---|---|
| Hollow separation | T minus H clearly positive | **3.00** | **pass** |
| Discrimination | gap at least about 1.0 | rubric gap **1.18**, lower bound **1.10** | **pass** |
| Agreement | stdev of T overall across judges at most about 0.7 | **0.00** matched, **0.29** pilot-comparable | **pass** |
| Control sanity | C not floored | **3.08** and **3.00** across two independent panels | **pass** |

The hollow arm scored **1.00 to 1.03** on rubric criteria and answered **0 of 5** probes, against the
treatment's 4.11 to 4.26 and 5 of 5. The instrument distinguishes a fluent empty document from a filled
one, which is the whole point of that arm.

**Control replication is the quiet result worth noticing.** The same control artifacts were scored by two
independent panels at **3.083** and **3.000**, a delta of **0.083**. Any gap smaller than that is not
distinguishable from judging noise, and the harness says so in its own output rather than leaving a reader
to work it out.

---

## The gaps, with intervals

Cluster bootstrap over 2 scenarios, 10,000 resamples, seed `20260808`. Reproducible by anyone from the raw
rows.

| Comparison | Point | 95% interval | Lower bound |
|---|---|---|---|
| **Rubric gap, matched** (T+ vs C) | **+1.18** | +1.10 to +1.26 | **+1.10** |
| **Held-out gap, matched** | **+0.14** | +0.11 to +0.17 | +0.11 |
| **Probe gap, matched** | **+0.00** | +0.00 to +0.00 | +0.00 |
| Overall gap, matched | +1.00 | +1.00 to +1.00 | +1.00 |
| Rubric gap, pilot-comparable (T vs C) | +1.00 | +0.86 to +1.14 | +0.86 |
| Held-out gap, pilot-comparable | +0.03 | +0.00 to +0.07 | +0.00 |
| Probe gap, pilot-comparable | +0.08 | +0.00 to +0.17 | +0.00 |
| Overall gap, pilot-comparable | +0.83 | +0.83 to +0.83 | +0.83 |

**Two of these intervals are zero-width and that is an artifact, not a precision claim.** The matched
overall gap reads +1.00 to +1.00 and the matched probe gap +0.00 to +0.00 because **both scenarios returned
identical values on those measures**, so every resample of two clusters returns the same number. With two
clusters a bootstrap can only ever draw from two values. Read those two rows as "no variation observed
across two scenarios", never as "measured to within zero".

---

## What the held-out gap does and does not mean

The rubric gap is **+1.18** and the held-out gap is **+0.14**. It is tempting to call that the circularity
signature and treat it as damning. **The protocol forbids that reading, and it is right to.**

**Section 4 states plainly that the held-out gap is not a gate**, and [ADR 0038](../../docs/internal/decisions/0038-what-the-circularity-signature-obliges.md)
is the record of why. Three things follow, all binding:

1. **A held-out value is neither a pass nor a fail.** There is no target, and inventing one at the moment
   of deciding is the opposite of a gate. No scope or content decision may be driven from `+0.14`.
2. **A template that does exactly what it says and no more may be working correctly.** Nothing in this
   protocol, this library, or the literature establishes that these templates *ought* to improve properties
   they never mention.
3. **The held-out criteria are selected by searching the templates for absences**, which
   **biases the measurement toward a null result by construction**. A small held-out gap is what this
   design predicts even for a template that works perfectly.

**What is genuinely new is the direction.** The two 114-agent runs of 2026-08-08 recorded the held-out gap
at **-0.03, spanning zero**. This run puts the matched held-out gap at **+0.14 with an interval of +0.11 to
+0.17, which excludes zero**, and the pilot-comparable equivalent at **+0.03, whose interval touches zero at
its lower bound**. That is a movement from "indistinguishable from nothing" to "small and positive" on the
matched comparison. **It is not a pass, because there is nothing to pass.** It is the first time the number
has had a sign the interval supports.

---

## The probe gap is the uncomfortable number, and it is also not a gate

**Treatment and control both answered essentially every reader probe.** Matched probe gap is **exactly
0.00**; the control arms answered 4.92 and 5.00 of 5 against the treatment's 5.00.

Probes ask whether a reader can get real questions answered from the document. On these two scenarios, a
competent writer with no template answered them as well as a writer with one. **That is worth saying out
loud**, and it is worth saying with the same discipline applied to the held-out gap above: **the probe gap
is not on the validity-gate list either**, so it cannot be used to fail the bundle any more than the
held-out gap can be used to pass it.

The judges' own notes are where the texture is, and they cut both ways. The control artifacts were repeatedly
described as the strongest on evidence and reasoning, with one judge calling the control's "what we're told
versus what we're concluding" section *"the clearest decision-vs-input separation in the set"*. The same
judges recorded that the control had **no functional requirements list, no priority markers, and no
UX or error-state coverage at all**, against a brief that explicitly asked for enough detail to size the
work. The template appears to buy structural completeness rather than analytical quality, on two scenarios.

---

## Limits, stated rather than discovered later

- **Two scenarios, one bundle.** Every number here is a property of `prd` times `claude-sonnet-5` times
  2026-09-03. Nothing generalises to the other 26 bundles, and the protocol's rule against ranking bundles
  against each other is not softened by a wider interval.
- **Two clusters is the floor, not a comfortable sample.** The intervals are wide where the data varies and
  zero-width where it does not, and both are honest reports of a two-cluster bootstrap.
- **The hollow arm ran on `prd-001` only, by design**, since it never reads the scenario and one calibration
  artifact per type is the harness's stated intent. Its n is 6 where the other arms are 12.
- **Held-out criteria remain selected-on-absence**, the bias ADR 0038 records and does not claim to have
  fixed.
- **This run measured output quality by LLM judges.** It says nothing about whether a human writing a real
  document is helped, which is what WP-31 and WP-33 exist to find out and what zero real fills means the
  library still cannot answer.

---

## What may be done with these numbers

**Publication is a maintainer decision and this file does not make it.** What the protocol already settles:

- The gap **must** be reported with its scenario count and interval, never as a bare point estimate, and a
  regression threshold reads the **lower bound**.
- **Nulls and negatives get published.** The probe gap of 0.00 is part of this result, not a footnote to it.
- Any published surface names the generation model, the judge models, and the run date, because the gap is a
  property of all three.

**No number here may be quoted into a bundle's metadata, a README, or a marketing surface without the
maintainer deciding that two scenarios of one type is enough to carry it.** The honest summary of this run
is one sentence: **the instrument now works, and on two `prd` scenarios the template buys about a point of
structural completeness on its own criteria, a fraction of that on criteria chosen to be independent, and
nothing measurable on whether a reader can answer their questions.**
