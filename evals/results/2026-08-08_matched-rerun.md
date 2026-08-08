# Matched re-run, 2026-08-08

**Verdict: VOID, again, and for a better reason than last time.**

The pilot's headline number, a held-out gap of **-0.81** that read as evidence the templates actively
suppress decision-usefulness, **was an artifact of the harness.** With the arms matched it is
**-0.03**. The alarming finding does not survive, and it should not have been believed.

What replaces it is quieter and harder to dismiss. With both arms told the same things about what a good
document does, the templates win **+0.85** on criteria drawn from their own guide and **-0.03**, which is
nothing, on criteria drawn from neither the template nor the guide. **That is the circularity signature
this protocol was built to detect**, and it is now measured rather than suspected.

No number in this file may be published, quoted in a README, or written into any bundle's metadata. It is
an instrument result, not a quality claim.

| | Generation | Judging | Panels | Scenarios | Arms | Drafts |
|---|---|---|---|---|---|---|
| Run | `claude-sonnet-5` | `claude-sonnet-5` | 2 per scenario, 3 judges each | 6, across 3 bundles | T, T+, C, H | 2 per arm |

Control-arm prompt: **version 1, byte-identical to the pilot's** (`git log` on
[`control-prompt.md`](../harness/control-prompt.md) shows no change).
Treatment-arm prompt: [version 1](../harness/treatment-prompt.md), new.
Harness: [`output-eval.workflow.mjs`](../harness/output-eval.workflow.mjs).
Intervals: [`analyze.mjs`](../harness/analyze.mjs), cluster bootstrap, seed 20260808.

---

## What changed, and why only this changed

The pilot compared two arms that differed in **two** things at once. The control received seven
discipline points, two of which name decision-usefulness properties. The treatment received a template
and a guide and **no discipline instruction at all**. Held-out criteria then scored exactly those
properties. A two-variable difference cannot be attributed to one variable, which is why the pilot's
result was uninterpretable rather than merely inconclusive.

**T+ is the fix.** It receives the template, the guide, **and** the identical seven discipline points.
Byte-identical, not paraphrased, and held that way by
[`tools/check-eval-arm-parity.py`](../../tools/check-eval-arm-parity.py) in CI, because a paraphrase
leaves open the argument that one arm got better-worded advice.

**Matching upward rather than downward was a real choice.** The alternative, deleting the two lines from
the control, would also have matched the arms and would have inflated every gap below. It was rejected on
the control prompt's own stated design rule: *if making the control stronger erases the gap, that is a
finding about the templates*.

**T and C were left exactly as the pilot ran them**, so this run reports a number directly comparable to
the pilot's -0.81 instead of replacing it with an incommensurable one.

### The judging change nobody asked for, which the comparison required

Adding a fourth artifact to the pilot's panel would have quietly broken the comparison. The pilot's judges
weighed **three** documents; if these judges weighed four, any movement in the T-versus-C gap could be
caused by the changed comparison set rather than by the arm matching, and a confound would have been
swapped rather than removed.

So each scenario is judged by **two panels**: session A sees `{T, C, H}`, exactly the pilot's context, and
session B sees `{T+, C, H}`. Every gap below is computed **within** one session. Never across.

That split pays for itself twice. The identical control documents are scored by two independent panels, so
**the spread between them measures judging noise directly**: **0.14**. Any gap smaller than that is not
distinguishable from the judges disagreeing with themselves.

---

## It ran twice, independently

The harness was re-invoked to recover three verdicts lost to an un-blinding miss, and re-executed all 114
agents instead of replaying them from cache. The accident is the most useful thing in this file:
**two complete, independent executions of the same design.**

| Quantity | Run 1 | Run 2 | Difference |
|---|---|---|---|
| Rubric gap, matched | +0.92 | +0.85 | 0.07 |
| **Held-out gap, matched** | **+0.10** | **-0.03** | **0.13** |
| Probe gap, matched | -0.14 | -0.03 | 0.11 |
| Overall gap, matched | +0.56 | +0.60 | 0.04 |
| Held-out gap, unmatched | -0.48 | -0.51 | 0.03 |
| Overall gap, unmatched | +0.36 | +0.39 | 0.03 |
| Instruction effect on held-out | +0.44 | +0.47 | 0.03 |
| Hollow separation | +2.74 | +2.76 | 0.03 |
| Control replication delta | +0.15 | +0.14 | 0.01 |
| Agreement stdev | 0.47 | 0.42 | 0.05 |

**Nothing moves more than 0.13 and most of it moves less than 0.05.** Run 2 is reported below because its
data is complete (180 rows against 177). Run 1 is kept at
[`_run1_raw.json`](2026-08-08_matched-rerun_run1_raw.json) and reaches every conclusion in this file
independently.

---

## The numbers

Hardened 1 to 5 anchor scale. `n` is judge-artifact scores, not documents.

| Arm | Session | n | Rubric | Held-out | Probes (of 5) | Overall |
|---|---|---|---|---|---|---|
| **T** treatment, unmatched | A | 36 | 3.95 | 3.49 | 4.75 | 3.69 |
| **C** control | A | 36 | 3.22 | 3.99 | **5.00** | 3.31 |
| **H** hollow | A | 18 | 1.05 | 1.25 | **0.00** | 1.00 |
| **T+** treatment, matched | B | 36 | 4.05 | 3.96 | 4.97 | 3.76 |
| **C** control | B | 36 | 3.19 | 3.99 | **5.00** | 3.17 |
| **H** hollow | B | 18 | 1.03 | 1.24 | **0.00** | 1.00 |

Gaps with 95% intervals, resampled over scenarios:

| Gap | Point | 95% interval | Reading |
|---|---|---|---|
| **Rubric, matched** | **+0.85** | +0.42 to +1.27 | **Real.** The template wins on its own guide's criteria |
| **Held-out, matched** | **-0.03** | -0.42 to +0.28 | **Nothing.** Spans zero, and is smaller than judging noise |
| Probe, matched | -0.03 | -0.08 to +0.00 | Nothing, against a ceilinged control |
| Overall, matched | +0.60 | +0.24 to +0.92 | Positive, and **below the 1.0 discrimination gate** |
| **Held-out, unmatched** | **-0.51** | **-0.92 to -0.04** | **The pilot's finding, reproduced.** Excludes zero |
| Overall, unmatched | +0.39 | -0.08 to +0.85 | Spans zero |
| Instruction effect, held-out | +0.47 | | What one paragraph of generic advice buys |
| Hollow separation | +2.76 | | The instrument measures substance |

**The two held-out rows are the whole result.** Unmatched, the gap is **-0.51 and its interval excludes
zero**: the pilot's finding is real and reproducible *as measured*. Matched, the same comparison is
**-0.03 with an interval spanning zero**. The difference between them is the instruction effect, +0.47,
which accounts for essentially all of it.

## The gates

| Gate | Result | |
|---|---|---|
| **Hollow separation** | **pass**, 2.76 | H scored 1.00 overall and answered **zero of five probes in every scenario, in both runs**. The rubric is not measuring shape |
| **Agreement** | **pass**, stdev 0.42 | Under the 0.7 threshold, and tighter than the pilot's 0.50 |
| **Control sanity** | **pass**, C overall 3.17 | Nowhere near the floor |
| **Discrimination** | **FAIL**, 0.60 vs 1.0 | **The run is void.** Inconclusive, not negative |

---

## What this establishes, stated as narrowly as the data allows

**1. The pilot's alarming finding is withdrawn.** There is no evidence that these templates suppress
decision-usefulness. The negative held-out gap was produced by telling one arm to do something and not
telling the other, and it disappears when both are told.

**2. The circularity signature is confirmed.** Protocol section 3 defines it exactly: *"A large rubric gap
beside a null held-out gap is the circularity signature. The treatment arm has read the answer key: it can
win by mentioning rubric items rather than by being better."* That is +0.85 beside -0.03, in both runs,
with the rubric interval excluding zero and the held-out interval straddling it.

**This is a finding about the bundles and it gets published rather than buried**, because the protocol says
so and because the alternative is discovering it from someone else later.

**3. The probes have a ceiling and can no longer discriminate.** The control answered **5.00 of 5 in both
sessions of both runs**. A probe set the counterfactual saturates cannot show improvement, only harm. The
probe gap is not evidence that the templates fail to help retrieval; it is evidence that this instrument
has stopped being able to tell.

**4. The judges are reliable enough to trust at this resolution.** Two independent panels scoring identical
control documents landed 0.14 apart, and agreement within a panel is 0.42. **Both are smaller than the
rubric gap and larger than the held-out gap**, which is what makes the contrast in point 2 readable rather
than noise.

## What it does not establish

- **Nothing about the other 23 bundles.** Three of 26, chosen for contrast.
- **Nothing about human authors.** Every artifact here was written by an LLM.
- **Nothing about whether templates are worth their cost.** A +0.85 rubric gap is real and may be exactly
  what a user wants; this eval takes no position on whether scoring better against a document type's own
  standards is valuable.
- **No bundle-level reading.** Six scenarios cannot separate three bundles.

Per scenario, T+ beat the control in five of six and lost one:

| Scenario | T+ | C | T+ minus C |
|---|---|---|---|
| `prd-001` | 4.00 | 3.00 | +1.00 |
| `prd-002` | 4.00 | 3.00 | +1.00 |
| `acceptance-criteria-001` | 3.50 | 3.67 | **-0.17** |
| `acceptance-criteria-002` | 4.00 | 3.17 | +0.83 |
| `incident-postmortem-001` | 3.83 | 3.17 | +0.67 |
| `incident-postmortem-002` | 3.25 | 3.00 | +0.25 |

`acceptance-criteria` is the bundle the protocol predicted would gain least, on the reasoning that its
template adds the least structure. **One scenario is not a bundle-level finding** and is recorded here so
that nobody has to rediscover which one it was.

## Every remaining limit

- **Three bundles of twenty-six.** Nothing generalises to the library.
- **The probe instrument is saturated** and needs harder probes before the next run.
- **No human anchor**, so absolute scores mean less than the gaps between arms.
- **Judge and generation model are the same family.** The standard mitigation, a different model in one
  seat, was **deliberately not applied**, because changing judge models would have broken comparability
  with the pilot in the same run that was fixing a different comparability problem. It is the first thing
  to change next.
- **The held-out criteria were authored by agents that had read the templates**, because proving absence
  required searching them. Unchanged from the pilot, and still the right way to prove absence and the
  wrong way to stay independent.
- **Two drafts per arm**, which is what the spec asks for and is still few.

## The harness defect this run found in itself

The first execution aggregated **177 of 180 rows**. One judge returned the label
`"Artifact A (narrative postmortem...)"`, and the un-blinding matched on the *trailing* letter, so all
three of that judge's verdicts were dropped.

**That trailing-letter match was the pilot's fix**, applied when judges returned `"Artifact A"` where the
key expected `"A"`. A patch written for one observed shape failed on the second observed shape. It is now
a cascade from most specific to most general, unit-tested against both.

**The mechanism held.** Nothing was silently lost: the run logged `WARNING: 3 verdict(s) could not be
un-blinded` with the scenario, session, judge and raw label of each. The lesson is not that the fix was
wrong; it is that **a fix aimed at one observed string is not a fix**, and the loud failure is what made
the difference between a footnote and a quiet bias in session A.

---

## What happens next, in order

1. **Harden the probes.** A control that answers 5.00 of 5 has ended the probe gap's usefulness. This is
   the cheapest remaining fix and it blocks interpretation of the most game-resistant of the three numbers.
2. **Put a different model in one judge seat.** Comparability with the pilot no longer needs protecting,
   because the pilot's headline is withdrawn.
3. **Decide what the circularity signature obliges.** The templates move documents toward their own
   criteria and not toward anything else measured here. Whether that is a defect to fix or the intended
   behaviour of a template is a scope question governed by ADR 0030's admission test, and it
   **stops for the maintainer**.
4. **Still do not scale to 26 bundles.** The gap is now interpretable, which was the condition, but the
   instrument has a saturated probe set and one unfixed validity mitigation. Scaling now would buy 26
   numbers with the same two holes in each.
