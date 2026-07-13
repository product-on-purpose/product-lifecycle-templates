# Spec: EV-1 Efficacy Evals (measure the lift, or stop claiming it)

- **Status:** proposed | **Roadmap:** WP-40 (M4) | **Effort:** L first time, S per bundle after | **Closes:** audit finding D-04 (no behavioral measurement)
- **One line:** for each bundle, generate documents with and without the template under identical scenarios, score both blind against the bundle's own rubric, and publish the discrimination gap as the bundle's measured lift.

## 1. Purpose

Every existing check is structural (form). Nothing tests function: does the template produce a better document than a competent freehand attempt? The pm-skills sibling already runs exactly this class of eval for skills; this spec ports the pattern with the template as the treatment. The output number converts "best-in-class" from adjective to measurement (Play 1, eval-certified bundles) and becomes the regression harness that protects every future edit.

## 2. What ports and what is new (grounded in the sibling repo)

| Piece | Source | Disposition |
|---|---|---|
| Two-arm runner (treatment vs control, blind judging, aggregation) | `pm-skills/scripts/output-eval.workflow.mjs` + `output-eval-aggregate.mjs` (unit-tested) | Adapt: the treatment arm injects the blank template (with guidance comments) + the guide, instead of a skill prompt |
| Rubrics | `pm-skills/docs/internal/eval-rubrics/specification.md` (covers prd, acceptance-criteria, user-stories) and `communication.md` (covers release-notes; mapping verifier-corrected in the audit) | Extract per-type criteria; merge with each bundle guide's own rubric items |
| Scenario format | `pm-skills` output-scenarios | Follow the shape; content is new |
| Scenario bank | none | NEW: 12 files (3 per bundle) |
| Scorecard publication | none | NEW: meta.yaml `scorecard:` block + README badge line |

## 3. Directory layout

```
evals/
  scenarios/        prd-001.yaml ... release-notes-003.yaml   (12 files)
  rubrics/          prd.rubric.md ... (extracted: guide rubric + universal criteria)
  results/          2026-07-XX_prd.json ...                   (raw runs, kept)
  usage-log/        (EV-3 forms from LP-2; separate stream, same family)
```

## 4. Scenario file format (normative)

```yaml
id: prd-001
doc_type: prd
size: lean
title: "In-app usage alerts for a B2B billing dashboard"
scenario_prompt: >
  You are the PM for {{product context, 3-5 sentences}}. Write the document
  that defines this work for the team. {{The realistic ask, stated the way
  a manager would state it, NOT the way the template would.}}
context_pack: |
  - {{6-12 facts the writer may use: user complaints, one data point,
     a constraint, a stakeholder opinion}}
  - {{at least 2 distractor facts that do NOT belong in a good document}}
difficulty: standard   # standard | messy (conflicting facts) | sparse (thin facts)
domain: fintech-b2b    # scenario domains deliberately differ from Saved Views
created: 2026-07-XX
```

Design rules: scenarios never mention the template or its section names (that would leak structure into the control arm); each bundle gets one `standard`, one `messy`, one `sparse`; domains vary across scenarios (this doubles as the CT-1 domain-travel probe: if the template only lifts in B2B SaaS scenarios, that is a finding).

## 5. Arms and generation protocol

- **T-arm (treatment):** model receives the scenario + context pack + the blank template (guidance comments intact) + the guide, instructed to fill the template and strip comments.
- **C-arm (control):** same model, same scenario + context pack, instructed to "write an excellent {doc type}" with no template. The control must be competent-but-unaided (no deliberately weak prompt; a strawman control invalidates the number).
- Same model and settings across arms; N=2 generations per arm per scenario to damp sampling variance. Total per full run: 12 scenarios x 2 arms x 2 = 48 generations.

## 6. Judging protocol

- **Blinding:** strip provenance frontmatter and any template-identifying artifacts from both arms before judging; randomize presentation order; judges never see arm labels.
- **Panel:** 3 independent judge runs per document (different seeds; a different model for one judge is acceptable and noted). Judge prompt contains: the rubric (per-item 0/1/2 with descriptors), two anchor exemplars (one strong, one weak, human-graded once at setup) to calibrate the scale, and the instruction to justify each item score in one line.
- **Scores:** per-item mean across judges; document score = percent of available points; arm score = mean over scenarios and generations.

## 7. Metrics (what gets published)

| Metric | Definition | Published where |
|---|---|---|
| Discrimination gap | mean(T-arm) minus mean(C-arm), in rubric percentage points | meta.yaml scorecard, README table, atlas |
| Judge agreement | mean pairwise absolute item-score difference (lower is better; flag if worse than 0.5 on the 0-2 scale) | scorecard fine print |
| Per-item lift | gap per rubric item | evals/results only; this is authoring feedback (items with no lift mean the template's guidance is not earning that row) |
| Domain spread | gap per scenario domain | results; feeds CT-1 |

meta.yaml block (added to the schema in the machine-metadata spec):

```yaml
scorecard:
  eval_gap_pct: 27.5
  judge_agreement: 0.31
  scenarios: 3
  last_run: 2026-07-XX
  harness_version: 0.1
```

## 8. Regression policy (the harness's second job)

- Any commit touching a bundle's template, companion, or guide triggers that bundle's eval subset in CI (12 generations + judging; keep it under ~15 minutes of pipeline time by running arms concurrently).
- Fail the check if the gap drops more than 20 percent relative to the recorded baseline or below an absolute floor of +10 points; update the baseline only via an explicit commit that says so.
- Full 4-bundle runs: at each release tag and each quarterly freshness pass.

## 9. Cost envelope (estimate, state assumptions)

Per full run: 48 generations x ~2-4k tokens + 144 judge passes x ~1-2k tokens, roughly 350-550k tokens end to end; per-bundle regression subset roughly a quarter of that. At current API list prices this is single-digit dollars per full run; negligible against the credibility it buys. Re-estimate after the first real run and record actuals in results/.

## 10. Honest-number rules (normative)

- Publish the gap with its scenario count; never round up; never publish a gap whose judge agreement is worse than the flag threshold without the flag.
- The control arm prompt is versioned in the repo; anyone can inspect that it is not a strawman.
- Negative or null results are published too (a bundle whose template shows no lift gets fixed or demoted, not hidden; that is what "measured, not asserted" costs and why it is worth something).

## 11. Acceptance criteria

- [ ] 12 scenarios exist and pass a review for the design rules (no structure leakage, distractors present, domains vary).
- [ ] One full run completes; per-bundle scorecards written to meta and rendered in the README table.
- [ ] Blind protocol verified: a reviewer cannot identify arms from the judged artifacts.
- [ ] Regression subset wired to CI with the stated thresholds; demonstrated once on a synthetic degradation (delete half the guidance comments on a branch; the gap should drop and CI should fail).
- [ ] Anchor exemplars human-graded and stored.

## 12. References

Audit finding D-04 (CONFIRMED) and its verifier's rubric-mapping correction; G6 section 2 and EV-1; pm-skills eval assets listed in section 2; judging-bias cautions per standard LLM-as-judge practice (blind, randomized order, anchored scale).
