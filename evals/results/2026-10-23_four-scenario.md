# Four-scenario eval, acceptance criteria and incident postmortem, 2026-10-23

**Verdict: VOID on discrimination, with a held-out gap whose interval lies below zero.** Three of the four validity
gates pass. The discrimination gate fails because the matched overall gap is +0.23, against the harness's bar of 1.0.
The templates again lift scores on their own rubric criteria (+0.64). On criteria drawn from neither the template nor
its guide, the matched template arm scores **below** the control: -0.30, with a 95% interval of -0.61 to -0.04. It is
the first **matched** held-out interval in this library's runs that lies entirely below zero. The
[2026-09-03 `prd` run's](2026-09-03_two-scenario.md) matched interval was +0.11 to +0.17, and the
[2026-08-08 rerun's](2026-08-08_matched-rerun.md) spanned zero. That rerun's unmatched interval, -0.92 to -0.04, also
excluded zero, but the unmatched comparison carries the arm asymmetry the rerun was built to remove.

**The held-out gap is not a gate.** Per protocol section 4 it passes or fails nothing. These criteria were also
selected on absence, which biases them toward finding the template short. Read the negative interval with that bias
attached.

| | Generation | Judging | Panels | Scenarios | Arms | Drafts |
|---|---|---|---|---|---|---|
| Run | `sonnet` alias, which ran as `claude-sonnet-5` | seats 1 and 2 `sonnet` (`claude-sonnet-5`), seat 3 `opus` (`claude-opus-5-5`) | 2 per scenario, 3 judges each | **4** (`acceptance-criteria-001`, `-002`, `incident-postmortem-001`, `-002`) | T, T+, C, H | 2 per arm |

Harness: [`output-eval.workflow.mjs`](../harness/output-eval.workflow.mjs), unchanged, run with `args.scenarios` naming
the four scenarios.
Prompts: control [version 1](../harness/control-prompt.md), treatment [version 1](../harness/treatment-prompt.md), both
unchanged. `tools/check-eval-arm-parity.py` passed before the run.
Raw rows: [`2026-10-23_four-scenario_raw.json`](2026-10-23_four-scenario_raw.json), **120 judge-artifact rows**.
76 agents, 0 errors, 0 empty results, **about 9 minutes wall clock**, **5,835,590 subagent tokens**.
Analysis: `node evals/harness/analyze.mjs evals/results/2026-10-23_four-scenario_raw.json --seed 20260808`, a cluster
bootstrap over the 4 scenarios with 10,000 resamples. Re-running it on the published file reproduces every number
below.

**Same generation model as 2026-09-03, a different judge panel.** Both runs generated with `claude-sonnet-5`. That run
judged with `claude-sonnet-5` in all three seats, and this one put `claude-opus-5-5` in judge seat 3. It is also a
different pair of bundles. *(An early draft of this result said the run generated with Sonnet 5.5. The agent
transcripts record `claude-sonnet-5` on every generation response and every seat 1 and seat 2 response. The `sonnet`
alias did not resolve to 5.5.)*

**One alteration to the raw rows, stated rather than made silently.** Twelve em-dashes appeared inside judge notes,
and this repository bans that character in every tracked file with a repo-wide CI sweep. **Each was replaced with a
spaced hyphen and nothing else changed.** All 794 numeric fields were compared before and after, and none moved. This
is the [2026-09-03 handling](2026-09-03_two-scenario.md).

---

## Validity gates

| Gate | Target (harness) | Measured | Result |
|---|---|---|---|
| Hollow separation | T minus H clearly positive | **2.42** matched, 2.46 pilot-comparable | **pass** |
| Discrimination | matched overall gap at least 1.0 | **+0.23** | **FAIL, void rather than negative** |
| Agreement | stdev of T+ overall across judges at most 0.7 | **0.58** | **pass** |
| Control sanity | C (session B) overall at least 2.0 | **3.19** | **pass** |

The hollow arm scored 1.06 to 1.07 on rubric criteria and answered **0 of 5** probes. The instrument still separates
a fluent empty document from a filled one.

**Control replication:** the same control artifacts scored 3.29 and 3.19 overall across two independent panels, a
delta of **0.10**. A gap smaller than that is not distinguishable from judging noise.

## The gaps, with intervals

| Comparison | Point | 95% interval | Lower bound |
|---|---|---|---|
| **Rubric gap, matched** (T+ vs C) | **+0.64** | +0.45 to +0.83 | +0.45 |
| **Held-out gap, matched** | **-0.30** | -0.61 to -0.04 | -0.61 |
| **Probe gap, matched** | **+0.00** | +0.00 to +0.00 | +0.00 |
| Overall gap, matched | +0.23 | +0.17 to +0.29 | +0.17 |
| Rubric gap, pilot-comparable (T vs C) | +0.64 | +0.46 to +0.82 | +0.46 |
| Held-out gap, pilot-comparable | -0.66 | -0.94 to -0.32 | -0.94 |
| Probe gap, pilot-comparable | +0.00 | +0.00 to +0.00 | +0.00 |
| Overall gap, pilot-comparable | +0.17 | -0.33 to +0.67 | -0.33 |

The probe interval is zero-width because every arm except the hollow one answered the probes almost perfectly
(4.75 to 5 of 5) in every scenario. Read it as "no variation observed", not as precision.

**Per type, matched (T+ against C in session B), point estimates over two scenarios each, no interval:**

| Type | Rubric gap | Held-out gap | Probe gap | Overall gap |
|---|---|---|---|---|
| `acceptance-criteria` | +0.45 | -0.08 | 0.00 | +0.29 |
| `incident-postmortem` | +0.83 | -0.52 | 0.00 | +0.17 |

Most of the held-out shortfall comes from `incident-postmortem`. Two clusters per type cannot support a per-type
interval worth printing, so these are descriptive only.

## What this run can and cannot say

- **It extends the circularity signature to two more bundles.** The 2026-08-08 runs found the templates scoring
  well above the control on their own criteria and no better on held-out ones. This run shows the same split for
  `acceptance-criteria` and `incident-postmortem`, and on held-out criteria the template arms do measurably worse.
- **Why the template arm might score lower on held-out criteria is not measured here.** One reading: with a fixed
  900-word budget for every arm, filling the template's sections spends words the control spends on what the
  held-out criteria reward. The judge notes point that way for one acceptance-criteria artifact, where the treatment
  "never mentions the complaint volume or problem evidence that motivates the story". That is a hypothesis from
  notes, not a finding.
- **Held-out criteria remain selected-on-absence.** Both rubrics were written on 2026-08-07, by searching the
  template and guide for absences. The protocol's Fix 2 retired that method on 2026-08-14, but neither rubric has
  been redrawn. So the caveat recorded in
  [ADR 0038](../../docs/internal/decisions/0038-what-the-circularity-signature-obliges.md) still applies: criteria
  chosen because the template lacks them are biased toward finding the template short. The `prd` rubric dates from
  the same day, so the held-out comparison with the 2026-09-03 run is like for like.
- **Four scenarios, two bundles, one date, one model set.** Nothing generalizes to the other bundles.

## Publication

The maintainer decided on 2026-10-25 to publish this result, under the protocol's rule that nulls and negatives get
published, and to update the efficacy wording in the library's user, technical and agent documents to match it. No
number from this run is a quality claim about any bundle, and none may be repeated without its caveats.
