# Measurement Validity: Hardening EV-1 Before Its Number Goes Public

- **Date:** 2026-07-11
- **What this is:** an adversarial epistemics pass on [specs/spec_ev1-efficacy-evals.md](specs/spec_ev1-efficacy-evals.md). The discrimination gap will become the library's most load-bearing public number ("measured, not asserted"). A number that a skeptic can take apart is worse than no number: it converts the credibility play into a credibility liability. This document enumerates the ways the number can be wrong or attackable, and amends the protocol so it survives hostile replication.
- **Output:** eight threats with mitigations, a precise statement of what the number does and does not claim, and a protocol-amendment list to fold into the spec as v0.2.

---

## 1. State the estimand precisely (most eval fights are definition fights)

The honest claim EV-1 can support:

> "When a capable LLM drafts a {doc type} for a realistic scenario, giving it this bundle's blank template and guide improves the draft's rubric-scored quality by X points over the same model given competent generic instructions, as scored by blinded LLM judges against the bundle rubric plus held-out criteria."

Every qualifier is load-bearing: *LLM drafts* (not human authors), *this bundle's* (not templates in general), *over competent generic instructions* (the counterfactual is a good PM prompt, not nothing), *rubric-scored* (not ground-truth business outcomes), *blinded judges* (procedure, not oracle). The README badge may compress to "measured lift: +X on blinded rubric evals," but the scorecard must link to this full statement. Claims about **human** authors and **real-world** outcomes belong to the EV-3/LP-2 field-data stream, never to EV-1.

---

## 2. Threats to validity, each with its mitigation

### T1: Rubric circularity (the treatment arm has read the answer key)

The T-arm receives the guide; the judges score against a rubric derived from that same guide. The T-arm can win by *mentioning* rubric items, not by being better. This is the single most attackable feature of the naive design.

**Mitigations (all three):**
1. **Held-out criteria.** Judges score 3-4 criteria that appear in neither the template nor the guide, focused on decision-usefulness: "Could an engineer scope work from this without a meeting?" "Does the document state what would make the team kill the feature?" "Is anything internally contradictory?" Report the rubric gap AND the held-out gap; a large rubric gap with a null held-out gap is the circularity signature, published honestly if found.
2. **Task-based judging (retrieval probes).** For each scenario, pre-write 5 factual probes a downstream consumer would ask ("What is out of scope?" "What is the guardrail metric?" "Which dependency is riskiest?"). Judges answer probes using only the document; score = probes answerable correctly. Probe-answering is much harder to game with rubric-shaped prose than impression scoring.
3. **Substance-sensitivity calibration: the hollow-template arm.** Once per harness version, run an H-arm: the template filled with fluent, generic, low-information filler. If judges score H anywhere near T, the eval is measuring form, not substance, and the rubric/probes must be tightened before any number is published. The H-arm result ships in the harness validation notes; publishing it preempts the strongest external attack by showing the authors ran it first.

### T2: Form bias in LLM judges

LLM judges systematically over-reward structure, headings, confident tone, and length. The T-arm inherits structure from the template, so form bias inflates the gap.

**Mitigations:** the H-arm quantifies this directly; probes (T1.2) are format-insensitive; additionally, cap judged length (truncate both arms at the same token budget with a stated rule) so length alone cannot separate arms, and instruct judges with explicit anti-form language ("a well-organized document that omits the success metric scores below a messy one that states it").

### T3: A strawman control arm

If the C-arm prompt is thin ("write a PRD"), the gap measures prompt effort, not template value, and a skeptic reproduces with a strong generic prompt and halves the number.

**Mitigations:** the C-arm prompt is a genuinely strong, versioned, public "competent generic practice" instruction: it names the standard advice (state the problem with evidence, define metrics up front, list out-of-scope) WITHOUT this library's specific structure or wording, at comparable instruction length to the T-arm's template+guide. Publish the C-arm prompt in the repo so anyone can judge its fairness. Design rule: if making the C-arm stronger erases the gap, that is a finding about the templates, and better to learn privately than publicly.

### T4: Blinding leakage (judges detect the template arm)

T-arm outputs will carry the template's section names and ordering; judges may recognize and favor (or disfavor) them.

**Mitigations:** normalize before judging: strip frontmatter, normalize heading casing, randomize document order per judging session; the probes are again leak-resistant. Accept that perfect blinding is impossible and say so in the validation notes; the H-arm plus probes bound how much leakage can matter.

### T5: Small-sample noise dressed as precision

Twelve scenarios, two generations, three judges produces a gap with real variance; publishing "+27.5" implies false precision, and bundle-to-bundle comparisons are meaningless (different scenario difficulty).

**Mitigations:** report the gap with a bootstrap interval over scenarios x generations ("+27.5, 90 percent interval +19 to +36, n=12 scenarios"); never rank bundles against each other; set regression thresholds on the interval, not the point estimate (fail when the interval's lower bound drops below the floor); grow the scenario bank before growing claimed precision.

### T6: Model coupling and time drift

The gap is a property of (templates x model x date). A model upgrade can move it in either direction without any template change; a skeptic on a different model gets a different number.

**Mitigations:** the scorecard names the generation and judge models and the run date; run two generation models when publishing (report both, claim the range); on model deprecation, re-baseline and annotate the scorecard history rather than silently overwriting (the per-bundle history file is the natural ledger).

### T7: Goodhart drift once the number is public

After publication, edits chase the gap: guidance text evolves toward what judges reward, scenario authors unconsciously write template-shaped scenarios.

**Mitigations:** held-out criteria rotate quarterly (small pool, sampled per run); scenario bank additions are written by someone (or some agent session) that has not read the templates recently, from the catalog entry alone; the annual human-anchor re-grade (two documents per type, human scored) re-tethers the judge scale; and the honest-number rules from the spec (publish nulls and negatives) remain the backstop.

### T8: External-validity overreach in downstream messaging

The subtle failure: the number is computed correctly and then the README says "templates make your documents 27 percent better." That claim is about human authors and real documents, which EV-1 does not measure, and one careful reader can turn the overreach into a story about the library's honesty.

**Mitigations:** the estimand statement (section 1) is the only permitted long-form claim; the badge links to it; the tense-discipline rule from the audit applies to eval claims doubly. The human-authors question has its own honest path: LP-2 gradings of real documents before and after template adoption (EV-3 stream) accumulate the field evidence over time; keep the two streams separate and label them.

---

## 3. What this changes in the spec (amendment list for spec_ev1 v0.2)

1. Add the estimand statement verbatim; badge must link to it (T8).
2. Add held-out criteria (3-4, decision-usefulness) and per-scenario retrieval probes (5) to the scenario format; report three numbers per bundle: rubric gap, held-out gap, probe gap (T1).
3. Add the hollow-template H-arm to harness validation (once per harness version), results published in validation notes (T1, T2, T4).
4. Specify the C-arm prompt as strong-generic, versioned, and public; add the fairness rule (T3).
5. Equal-length truncation rule and anti-form judge instructions (T2).
6. Normalization pass before judging: strip frontmatter, normalize headings, randomize order (T4).
7. Report bootstrap intervals; thresholds operate on the interval lower bound; forbid cross-bundle ranking in any published surface (T5).
8. Scorecard carries model names and run date; two-model publication; re-baseline protocol on model change, logged in bundle history (T6).
9. Quarterly held-out rotation; scenario authorship independence rule; annual human anchor re-grade (T7).

Cost of all nine amendments: roughly one additional day on the harness and a modest per-run token increase (the probes and H-arm). Against the alternative, a public number that fails hostile replication, the price is trivial.

---

## 4. The strategic framing

Publishing evals invites replication; that is the point. The library's positioning ("measured, not asserted") only compounds if the measurement survives someone trying to break it. Every mitigation above is therefore also a marketing asset: the validation notes that say "we ran the hollow-template control and here is the result" are more persuasive than the headline gap itself, because they are the evidence the authors attacked their own number before anyone else could. That is the same posture the audit applied to its own findings, and it should be the house style for every number this project ever publishes.
