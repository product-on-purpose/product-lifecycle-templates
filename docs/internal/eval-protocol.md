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

Four, as of 2026-08-08. It was three, and three was not enough to attribute a result.

| Arm | What it receives | What it tests |
|---|---|---|
| **T, treatment** | Scenario, context pack, the blank template with guidance comments intact, and the guide | The thing being measured, as the pilot measured it |
| **T+, matched treatment** | All of T, **plus the identical discipline instruction the control receives** | The thing being measured, with the arms matched |
| **C, control** | Scenario, context pack, and a strong generic instruction to write an excellent document of that type | The counterfactual |
| **H, hollow** | The template filled with fluent, generic, low-information filler | Whether the rubric measures substance or form |

### Why T+ exists, which is a mistake worth keeping written down

**The pilot's arms differed in two things at once.** C received seven discipline points, two of which name
decision-usefulness properties. T received a template and a guide and **no discipline instruction at all**.
The held-out criteria then scored exactly those properties. A difference across two variables cannot be
attributed to one of them, so the pilot's headline held-out gap of -0.81 was not a weak finding. It was
not a finding.

**The error is easy to make and hard to see.** Both prompts were written carefully, the control was
deliberately made strong, length was matched, and the arms were still not comparable, because "what does
the treatment get that the control does not" was answered as *the template* when the true answer was
*the template, and also nothing else while the control got a paragraph of advice*.

**T+ closes it by matching upward.** The discipline block is byte-identical across
[`control-prompt.md`](../../evals/harness/control-prompt.md) and
[`treatment-prompt.md`](../../evals/harness/treatment-prompt.md), enforced by
[`tools/check-eval-arm-parity.py`](../../tools/check-eval-arm-parity.py) in CI. A paraphrase would leave
open the argument that one arm was handed better-worded advice.

**Matching downward was rejected on the control prompt's own design rule.** Deleting the two lines from
the control would also have matched the arms, and would have inflated every gap thereafter. *If making the
control stronger erases the gap, that is a finding about the templates.*

**T is kept, unchanged, alongside T+.** A re-run that replaced the old comparison would produce a number
nobody could set beside the one it was correcting.

### Judging is session-split, and this is not cosmetic

Each scenario is judged by **two panels**: session A sees `{T, C, H}`, session B sees `{T+, C, H}`.
**Every gap is computed within one session, never across one.**

The obvious alternative, one panel seeing all four arms, silently breaks the comparison a re-run exists to
make. If the pilot's judges weighed three documents and a later run's judges weigh four, then any movement
in the T-versus-C gap may be caused by the changed comparison set rather than by the change under test, and
a confound has been swapped rather than removed.

The split also buys a measurement available no other way. **The identical control documents are scored by
two independent panels**, so the spread between them estimates judging noise directly rather than through
the within-panel agreement gate. Measured 2026-08-08: **0.14**. Any gap smaller than that is not
distinguishable from the judges disagreeing with themselves, and no reading may rest on one.

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

**The held-out gap is not on that list, and this is a gap in the protocol rather than an omission with a
reason.** Recorded 2026-08-10, while trying to decide what the measured circularity signature obliges
([ADR 0038](decisions/0038-what-the-circularity-signature-obliges.md)):

* **There is no target for the held-out gap**, so a value like `-0.03` is **neither a pass nor a fail**. It
  can be reported and discussed, but no scope or content decision can be driven from it without someone
  inventing a threshold at the moment of deciding, which is the opposite of a gate.
* **The held-out gap measures spillover**, whether a template improves properties it never mentions, and
  **nothing here establishes that spillover is a reasonable expectation**. A template that does exactly
  what it says and no more may be working correctly.
* **Held-out criteria are currently selected by searching the templates for absences.** That is the right
  way to prove absence and it **biases the measurement toward a null result**, because the criteria are
  chosen for maximal distance from what the template addresses.
  [The re-run](../../evals/results/2026-08-08_matched-rerun.md) already records the related independence
  problem, that the authoring agents had read the templates. **This protocol did not**, and this is the
  sharper form of it: contamination is a risk to the criteria, whereas selection-on-absence is a bias in
  the design.

### Both fixes adopted 2026-08-14

Recorded here rather than in a decision record, because changing the instrument is a maintainer decision and
the maintainer took it. [ADR 0038](decisions/0038-what-the-circularity-signature-obliges.md) is the context.

**Fix 1. The held-out gap is deliberately NOT gated, and this is the reason.**

No threshold is set, and none should be invented later without superseding this paragraph. **A template
that does exactly what it says and no more may be working correctly**, so there is no defensible value at
which a held-out gap becomes a failure. Setting a target would mean asserting that these templates *ought*
to improve properties they never mention, and **nothing in this protocol, this library, or the literature
establishes that they ought to.**

What follows from the non-gate, and it is binding:

- **The held-out gap may be reported and discussed. It may not be used as a pass or a fail**, and no scope
  or content decision may be driven from it alone. That is what
  [decision procedure 12](decision-procedures.md#12-a-property-or-section-is-proposed-for-a-template) is
  for: candidates it surfaces face a source search, not a score.
- **It stays reported anyway.** A non-gated number is not a suppressed one. Removing it would hide the
  circularity signature, which is the most interesting thing either run produced.
- **Reopening this requires an argument that spillover is expected**, naming who expects it and why. The
  point of writing the reason down is that the next person must beat the reason rather than just pick a
  number.

**Fix 2. Held-out criteria are drawn independently, then coverage is measured afterwards.**

The old method (search the templates for absences, then measure those absences) is retired. It biases
toward null by construction, and selecting on absence to then measure absence is close to circular in its
own right.

**The new method, in order, and the order is the whole point:**

1. **Draw criteria from the decision-usefulness literature**, independently, **without reading the template
   or its guide first**. What makes a document of this type useful to the person who must act on it?
2. **Then measure how many of them the template happens to cover**, and report that as **coverage**.
3. **Then score both arms against the full set.**

**This converts coverage from an artifact of the selection method into a finding.** Under the old method,
coverage was near zero by construction and meant nothing. Under the new one, "the template addresses 6 of
the 20 things the literature says matter" is a real sentence about the template, and it is a more useful
one than any gap number.

**Consequence, stated so it is not discovered later: this makes the next run incomparable with the first
two on the held-out axis.** The criteria change, so the number changes for reasons that have nothing to do
with the templates. The rubric axis and the gates remain comparable. Any report covering both must say so.

**Verdict ordering is absolute-failure-first.** A bundle fails if its own score is below the bar or any
criterion floors, *regardless of the gap*. A weak control can never launder a bad bundle into a pass. Only a
bundle that independently clears the absolute bar is labelled void when the gap is inconclusive.

---

## 5. Blinding, and the honest admission about it

Judges see artifacts labelled only A, B and C, in an order randomised per judging session, with frontmatter
stripped and heading casing normalised. Both arms are truncated to the same token budget under a stated
rule, so length alone cannot separate them, and judges are instructed explicitly against form bias: a
well-organised document that omits the success metric scores below a messy one that states it.

**Who the judges are, which this protocol did not previously state.** Three seats per panel. **From
2026-08-10, seat 3 runs a different model from the other two and from the generator**; before that date,
including in both completed runs, every seat and the generator were the same model, so nothing separated
the scorer from the writer. The mitigation was skipped deliberately in the matched re-run to protect
comparability with the pilot, and that reason expired when the pilot's headline was withdrawn.

**This is a partial mitigation and no result should be read as though it controlled for judge identity.**
Every model reachable from this harness is a Claude model, so a shared-vendor scoring idiosyncrasy is
untouched. What it buys is narrower: a quirk specific to one model can no longer sweep all three seats
unnoticed. The per-seat model is emitted on every row as `judgeModel`, so whether the diverse seat
actually disagrees is a measurable question rather than an assumption.

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

### How the blinding rule is actually satisfied, added 2026-08-14

**The rule above disqualified the only author available**, and that is worth recording rather than working
around. Probe hardening was authorised on 2026-08-10 and **was not done**, because the agent holding the
authorisation had spent the session reading these templates, rubrics and held-out criteria, and is
therefore precisely the contaminated author this section excludes. **Authorisation is not competence to do
the task correctly.**

**The mechanism now is a scoped subagent**, [`blind-probe-author`](../../.claude/agents/blind-probe-author.md),
which is given **no filesystem tools at all**: no `Read`, no `Grep`, no `Glob`, no `Bash`. It cannot open
`templates/`, `evals/rubrics/` or `manifest.json` because it has nothing to open them with. Everything it
needs, the catalog entry and the scenario brief, is passed to it in its prompt.

**Blinding by construction rather than by instruction.** An agent told not to look can look. An agent with
no read tool cannot, and this is the difference between a rule and a guarantee. Path-level restriction is
not something agent configuration can express, so the enforceable version is tool removal.

**Its honest limitation, which must travel with any result it produces:** it is an approximation of a blind
author, not a real one. It shares a model family and a training distribution with the agents that wrote the
templates, so it may reach for the same vocabulary without ever reading them. **That is a weaker claim than
"written by someone who has never seen this library", and no report should make the stronger one.** The
stronger version needs a human who has not read the bundles.

### The probe set and the held-out set are not independent instruments

**Found 2026-08-10 and not yet fixed.** `prd-001` probe 2 ("what would make the team stop or reconsider")
and probe 5 ("who owns that constraint") measure **the same properties as two of the held-out criteria**.
They do not provide independent evidence, and hardening the probes without addressing the overlap would
deepen it.

**This is fixed as part of the rewrite, not before it**, because fix 2 in section 4 redraws the held-out
criteria from scratch. Fixing the overlap against criteria that are about to be replaced would be work
against a moving target. **The rule for the rewrite: probes and held-out criteria are drawn separately and
checked against each other for overlap before either is used.**

---

## 7. Reporting rules, which are not optional

- **Report the gap with its scenario count and a bootstrap interval**, never a bare point estimate.
  Regression thresholds operate on the interval's lower bound, not the point.
  [`evals/harness/analyze.mjs`](../../evals/harness/analyze.mjs) computes them, and it lives outside the
  harness because workflow scripts may not call `Math.random`: a resumed run must replay identically, and
  a bootstrap is nothing but random draws. **It resamples scenarios, not judge-artifact rows.** Three
  judges scoring one document are not three independent observations, and resampling rows would return a
  tight, confident interval the data does not support.
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
