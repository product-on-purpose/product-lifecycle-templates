---
title: "Efficacy evals"
---

# Efficacy evals

**The attempt to replace this library's argued quality claim with a measured one.**

Every check in `tools/` proves something about **form**: that a bundle has its files, that its citations
resolve, that its numbers match the tree. None of them tests **function**. A bundle can pass all eleven
gate checks and still produce a worse document than a competent practitioner would write freehand. That
question is what lives here.

## Read this before reading a number

[`docs/internal/eval-protocol.md`](../docs/internal/eval-protocol.md) states what the eval measures, what
it refuses to claim, and eight ways the number could be wrong. It was written **before** the first number
existed, deliberately, so the protocol could not be tuned to a result it had already seen.

The short version of the honest scope: this measures whether **an LLM** drafts a better document with the
bundle than without it, scored by **blinded LLM judges**. It says nothing about human authors and nothing
about business outcomes. A sentence like "templates make your documents better" is not a claim this
evidence supports.

## The three arms, and why the third one exists

The treatment arm gets the template and guide. The control arm gets a strong generic instruction and none
of this library. **The hollow arm gets the template filled with fluent, generic, low-information filler.**

If judges score the hollow arm anywhere near the treatment arm, the instrument is measuring shape rather
than substance, and **no number may be published** until the rubric and probes are tightened. Running that
check, and publishing its result even when unflattering, is more persuasive than any headline gap, because
it is the evidence that the authors attacked their own number first.

## Inventory

- [`scenarios/`](scenarios/) - the input briefs. Each is authored from the document type's description
  alone, by an agent instructed not to open this library's templates, so a brief cannot be shaped like the
  thing it is meant to test. Each carries deliberate distractor facts and five retrieval probes
- [`rubrics/`](rubrics/) - per-type scoring criteria, split into **rubric criteria** derived from the
  bundle's own guide and **held-out criteria** that appear in neither the template nor the guide. The split
  is the circularity control: a large rubric gap beside a null held-out gap means the template is teaching
  its own rubric rather than teaching the document
- [`harness/`](harness/) - the runner and the versioned control-arm prompt. The prompt is public so that
  anyone who thinks the counterfactual is unfair can say which sentence is unfair
- [`results/`](results/) - raw runs, kept. Nulls and negatives are published here alongside anything good

## Running it

```
Workflow({ scriptPath: "evals/harness/output-eval.workflow.mjs" })
```

It is deliberately **not** wired into CI. A judged eval is expensive and non-deterministic, and a
non-deterministic check that blocks a merge teaches people to re-run until it passes. Regression use comes
later, against a recorded baseline and an interval rather than a point estimate.
