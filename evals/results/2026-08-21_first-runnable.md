# First runnable eval, 2026-08-21

**Verdict: no verdict, and that is the correct outcome. This run measured the instrument and the price,
not the templates.**

**The harness had never run. Not "was never run": could not run.** `.gitattributes` pinned `*.js` to LF
and not `*.mjs`, so every Windows checkout produced a pure-CRLF
[`output-eval.workflow.mjs`](../harness/output-eval.workflow.mjs) and the Workflow tool refused it with
"script contains control characters that would be hidden in the approval dialog". Three sessions recorded
"no eval was run" and gave the reason as needing a direct request. **That reason was true and had never
been tested against the harness starting.** One `.gitattributes` line later it started.

**No number in this file may be published, quoted in a README, or written into any bundle's metadata.**
That standing rule applies with extra force here: this is **one scenario**, so the cluster bootstrap is
degenerate and there is no interval at all. See "Why this run cannot carry a gap" below.

| | Generation | Judging | Panels | Scenarios | Arms | Drafts |
|---|---|---|---|---|---|---|
| Run | `claude-sonnet-5` | `claude-sonnet-5` | 2 per scenario, 3 judges each | **1** (`prd-001`) | T, T+, C, H | 2 per arm |

Harness: [`output-eval.workflow.mjs`](../harness/output-eval.workflow.mjs), unchanged.
Prompts: control [version 1](../harness/control-prompt.md), treatment [version 1](../harness/treatment-prompt.md), both unchanged.
Raw rows: [`2026-08-21_first-runnable_raw.json`](2026-08-21_first-runnable_raw.json), 36 judge-artifact rows.
20 agents, 0 errors, 0 empty results, **11 minutes wall clock**.

---

## The price, measured for the first time

| Quantity | Value | What it is |
|---|---|---|
| **Subagent tokens** | **1,229,196** | Reported by the harness runtime for this workflow's 20 agents |
| **`budget.spent()`** | **411,179** | Turn-level output tokens. **This global had never executed at runtime before** |
| `budget.total` | `null` | No turn budget was set |
| Tool calls | 136 | |
| Wall clock | **660,677 ms**, about 11 minutes | |

**Read `budget.spent()` with the two limits the harness prints beside it**, both real: it is *turn*-level
across the main loop and every workflow in it, so it is an **upper bound** on this run rather than its
cost; and it counts **output only**, while for this harness the input side (every treatment agent reading
bundle text) is likely the larger half. **An upper bound on half the cost is still the first cost figure
this repository has ever had.**

**Extrapolating to a six-scenario run is arithmetic and should be treated as such:** roughly 7.4M subagent
tokens and about 66 minutes, if the per-scenario cost holds. Nothing here establishes that it does.

---

## What the gates said

| Gate | Result |
|---|---|
| **Hollow separation** | **pass**, 2.83 matched / 3.00 pilot-comparable |
| **Discrimination** | **FAIL, void rather than negative** |
| **Panel agreement** | **pass**, stdev 0.41 |
| **Control sanity** | **pass** |

**The hollow arm is the one result worth stating plainly, because it is the instrument working.** A
document with the right shape and no content scored **1.05** against the treatment's **4.53**. The judges
were not told which arm anything came from, and one wrote of the hollow draft that *"technically no
internal contradiction is findable, but only because there is no substantive claim anywhere to
contradict, which is not meaningful decision-usefulness."* **A rubric that a fluent empty document could
pass would be worthless, and this one is not that.**

## The circularity signature reproduces

| Gap (matched, T+ vs C) | This run | 2026-08-08 re-run |
|---|---|---|
| **Rubric criteria**, drawn from the templates' own guide | **+1.14** | +0.85 |
| **Held-out criteria**, drawn from neither template nor guide | **-0.08** | -0.03 |
| Retrieval probes | **-0.67** | |
| Overall | +0.50 | |

**Same shape, same sign, on an independent run through a harness that had never executed.** The templates
win by a wide margin on criteria their own guide supplies and by nothing at all on criteria neither the
template nor the guide has seen.

**The held-out gap is inside the noise floor and is not a finding.** The control replication delta, the
same artifacts scored by two independent panels, is **-0.17**. A held-out gap of **-0.08** is smaller than
that, so it is not distinguishable from judging noise. **This is the "VOID rather than negative" verdict
the protocol defines**, and it is the third time it has been returned.

**The probe gap is the uncomfortable one and is not being buried.** The control arm answered **5.0 of 5**
retrieval probes; the treatment answered **4.5**. On one scenario, with no interval, that is an
observation rather than a result. **It points the wrong way for the library and it is recorded because it
does.**

---

## Why this run cannot carry a gap, and the defect that found

[`analyze.mjs`](../harness/analyze.mjs) resamples **scenarios**, not rows, deliberately: three judges
scoring one document are not three independent observations. **With one scenario there is one cluster,
every resample draws it, and `lower === upper === point`.** Every interval this run produces is
zero-width. Protocol section 7 forbids a bare point estimate, and a zero-width interval is a bare point
estimate wearing an interval's clothes.

**The analyzer said the opposite, confidently.** Its closing line was hardcoded:

> "With 1 clusters the interval is wide, and that width is the run precision rather than a defect."

It printed that **directly beneath a table reading `+1.14 to +1.14`**. The sentence encodes a true
intuition, that fewer clusters means a wider interval, which **inverts at n=1** where the bootstrap
degenerates instead of widening. Fixed in the same change as this record: under two clusters the script
now refuses the reading in as many words. The six-scenario path was re-run against
[`2026-08-08_matched-rerun_run1_raw.json`](2026-08-08_matched-rerun_run1_raw.json) to confirm the normal
branch and its historical numbers are unchanged.

**This defect could only appear on a single-scenario run**, and a single-scenario run is exactly what a
first cautious execution looks like.

---

## What this run does and does not establish

**Does:**

- **The harness runs end to end.** 20 agents, 0 errors, 4 arms, 2 sessions, 36 judge rows, all gates
  evaluated. That was an assumption for three sessions and is now an observation.
- **The first real cost figure**, with its limits stated.
- **`budget.spent()` executes at runtime**, returning 411,179.
- **The hollow control works**, which is the single most important property of the instrument.
- **The circularity signature reproduces** on an independent run.

**Does not:**

- **Any claim about whether the templates help.** One scenario, one document type, no interval.
- **Anything about the other 25 bundles.** `prd-001` is one scenario against one type.
- **Any revision to the 2026-08-08 verdicts.** Those stand on six scenarios; this stands on one.
- **That the per-scenario cost is stable.** One observation, no variance estimate.
