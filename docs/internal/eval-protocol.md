# The efficacy eval protocol

**What this measures, what it refuses to claim, and every way the number could be wrong.**

This is the protocol behind EV-1, the library's first attempt to replace an argued quality claim with a
measured one. It is written before the first number exists, deliberately, so that the protocol cannot be
tuned to a result it has already seen.

**Read [`review-standards.md`](review-standards.md) section 5 first if you have not.** The library's
dominant defect is a plausible specific claim nothing supports. A published efficacy number is that defect
at its most dangerous, because a number carries more authority than a sentence and is harder to argue with.

---

## 1. The estimand, stated before any number

This is the only long-form claim the eval is permitted to support. Anything shorter that appears in a
README, a badge, or a release note must link here.

> When a capable LLM drafts a {document type} for a realistic scenario, giving it this bundle's blank
> template and guide improves the draft's rubric-scored quality by X points over the same model given
> competent generic instructions, as scored by blinded LLM judges against the bundle rubric plus held-out
> criteria.

**Every qualifier is load-bearing.** *An LLM drafts* (not a human author). *This bundle's* (not templates in
general). *Over competent generic instructions* (the counterfactual is a good prompt, not nothing).
*Rubric-scored* (not business outcomes). *Blinded judges* (a procedure, not an oracle).

**What this eval can never claim.** That templates make human-written documents better, or that any
business outcome improved. Those belong to a field-evidence stream and must never borrow this number's
authority. A sentence like "templates make your documents 27 percent better" is out of scope, and one
careful reader turning that overreach into a story about the library's honesty would cost more than the
number is worth.

---

## 2. The arms

Three, not two. The third is what makes the first two believable.

| Arm | What it receives | What it tests |
|---|---|---|
| **T, treatment** | Scenario, context pack, the blank template with guidance comments intact, and the guide | The thing being measured |
| **C, control** | Scenario, context pack, and a strong generic instruction to write an excellent document of that type | The counterfactual |
| **H, hollow** | The template filled with fluent, generic, low-information filler | Whether the rubric measures substance or form |

**The control is not a strawman, and this is the single easiest way to fake a good result.** The C-arm
prompt is versioned in this repository so anyone can inspect its fairness, names the standard advice a
competent practitioner would follow, and is written at comparable length to the T-arm's instruction.
**Design rule: if making the control stronger erases the gap, that is a finding about the templates**, and
it is better to learn it privately than to have a skeptic demonstrate it publicly.

**A control that scores near the floor is a bug in the control, not a win.** Per the sibling harness in
`pm-skills`, a control scoring below roughly 2 on most criteria means the prompt has drifted toward a
strawman and the run is re-run rather than reported.

**The hollow arm is the one that can invalidate everything else.** If judges score H anywhere near T, the
instrument is measuring shape rather than content, and no number may be published until the rubric and
probes are tightened. Publishing the H result, including when it is unflattering, is the point: it is the
evidence that the authors attacked their own number before anyone else could.

---

## 3. Scoring, and the three numbers that get reported

Never one number. Three, always together.

| Number | What it is | Why it is separate |
|---|---|---|
| **Rubric gap** | T minus C on the bundle's own rubric criteria | The headline, and the most gameable |
| **Held-out gap** | T minus C on 3 to 4 decision-usefulness criteria that appear in **neither** the template nor the guide | The circularity control |
| **Probe gap** | T minus C on per-scenario retrieval probes answered from the document alone | Format-insensitive, hardest to game |

**A large rubric gap beside a null held-out gap is the circularity signature.** The treatment arm has read
the answer key: it can win by *mentioning* rubric items rather than by being better. That pattern is
published when found, not buried, and it means the template is teaching its own rubric rather than teaching
the document.

**The anchor scale is the hardened 1 to 5 scale ported from `pm-skills`.** A 5 is reserved for work a senior
practitioner would not touch; solid, shippable-with-a-nitpick work is a 4. Judges score conservatively and
break ties downward. The scale is hardened because the sibling's first proof of concept hit a perfect 5.0
and left no headroom to detect a regression.

---

## 4. Validity gates, checked before a score counts

Ported from the sibling harness, which unit-tests the ordering.

| Gate | Target | If it fails |
|---|---|---|
| **Hollow separation** | T minus H clearly positive | **The run is void.** The instrument measures form; fix the rubric before reporting anything |
| **Discrimination** | gap at least about 1.0 | Void, and a finding about the instrument rather than the bundle |
| **Agreement** | stdev of T overall across judges at most about 0.7 | The rubric is ambiguous; tighten before trusting scores |
| **Control sanity** | C not floored | The control drifted to a strawman; re-run |

**Verdict ordering is absolute-failure-first.** A bundle fails if its own score is below the bar or any
criterion floors, *regardless of the gap*. A weak control can never launder a bad bundle into a pass. Only a
bundle that independently clears the absolute bar is labelled void when the gap is inconclusive.

---

## 5. Blinding, and the honest admission about it

Judges see artifacts labelled only A, B and C, in an order randomised per judging session, with frontmatter
stripped and heading casing normalised. Both arms are truncated to the same token budget under a stated
rule, so length alone cannot separate them, and judges are instructed explicitly against form bias: a
well-organised document that omits the success metric scores below a messy one that states it.

**Perfect blinding is impossible and the protocol says so.** A treatment artifact carries the template's
section names and ordering, and a judge may recognise them. The hollow arm and the probes bound how much
that can matter, which is why they exist. This limitation ships in the validation notes rather than being
managed out of sight.

---

## 6. What makes a scenario legitimate

- **Written from the catalog entry alone, by an author who has not just read the bundle.** A scenario
  written by someone fresh from the template is template-shaped, and the control arm is then being asked a
  question phrased in the treatment's own vocabulary.
- **Never mentions the template or its section names.** That leaks structure into the control arm.
- **Carries distractor facts** that do not belong in a good document, so completeness cannot be scored by
  including everything.
- **Comes in three difficulties**: standard, messy (conflicting facts), and sparse (thin facts). Domains
  vary deliberately, which doubles as a probe: a template that only lifts in one domain is a finding.

---

## 7. Reporting rules, which are not optional

- **Report the gap with its scenario count and a bootstrap interval**, never a bare point estimate.
  Regression thresholds operate on the interval's lower bound, not the point.
- **Never rank bundles against each other.** Scenario difficulty differs, so a cross-bundle comparison is
  meaningless and any published surface that invites one is a defect.
- **The scorecard names the generation model, the judge models, and the run date.** The gap is a property of
  templates times model times date, and a model upgrade can move it without any template changing.
- **Publish nulls and negatives.** A bundle whose template shows no lift gets fixed or demoted, not hidden.
  That is what "measured, not asserted" costs, and it is the reason the phrase is worth anything.
- **Never round up.**

---

## 8. Pilot scope, and its stated limits

The first run is a **pilot on three bundles**, chosen for contrast rather than coverage:

| Bundle | Why it is in the pilot |
|---|---|
| `prd` | Large and heavily scaffolded. If form bias exists anywhere, it shows here, so this is the sharpest hollow-arm test |
| `acceptance-criteria` | Small and rule-shaped, where the template adds least structure. The gap should be smaller, and if it is not, that is informative |
| `incident-postmortem` | Narrative and analytical. Its template's value should be in the questions it forces rather than the shape it imposes, which tests whether the protocol generalises past structured documents |

**The pilot's job is to validate the instrument, not to produce a publishable number.** It runs at reduced
scale, and the limits below are stated rather than discovered later:

- **Reduced generations per arm**, so sampling noise is larger than a full run's.
- **A reduced judge panel**, so the agreement gate is measured on fewer points.
- **Three bundles of twenty-six**, so nothing here generalises to the library.
- **No human anchor re-grade yet**, so the judge scale is unanchored and absolute scores mean less than the
  gaps between arms.

**No number from the pilot goes into a README, a badge, a release note, or the scorecard block in any
bundle's metadata.** The pilot's output is a decision about whether the protocol is sound enough to run
properly, and its results live in `evals/results/` with those limits attached.
