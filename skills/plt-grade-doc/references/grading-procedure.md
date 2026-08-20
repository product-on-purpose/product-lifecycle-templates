# The grading procedure in detail

The `SKILL.md` carries the flow. This file carries the parts that are easy to get subtly wrong.

## 1. Type detection, and the confidence rule

The four routes in order are explicit type, frontmatter provenance, alias or tag match, heading
fingerprint. Two rules govern what happens when they disagree.

**Never guess silently.** A wrong type produces a report card that is internally consistent, fluently
written, and grading against the wrong standard. It is the single worst output this skill can produce,
because every quality signal a reader uses to sanity-check a critique is intact.

**Below confidence, ask exactly one question**, and make it distinguishing rather than open. "Is this
closer to a PRD or a software design document?" is answerable. "What kind of document is this?" hands the
work back.

### Types that are genuinely hard to tell apart

| Pair | The distinguishing question |
|---|---|
| `prd` and `sdd` | Does it say what to build and why, or how it is built? |
| `prd` and `rfc` | Is it a commitment to build, or a proposal seeking a decision? |
| `adr` and `rfc` | Is the decision made, or being proposed? |
| `product-vision` and `product-strategy` | Is it where the product is going, or how it wins? |
| `risk-register` and `raid-log` | Does it track risks only, or also assumptions, issues and dependencies? |
| `user-stories` and `acceptance-criteria` | Is the unit a story with a value clause, or a testable condition? |

**No match at all is a result, not a failure.** The catalog holds 205 types and only the Tier-1 floor is
built. Record the miss: what the document appeared to be, and what the reader called it. That is demand
evidence for a type nobody has asked for yet in any other way.

## 2. Reading the rubric

**Detect the form from the guide in front of you.** Do not carry a memorised list of which bundles are in
which form; the library has an open decision to convert some of them, and a memorised list goes stale
silently the moment one converts.

The detection rule is mechanical:

- A rubric table whose header row carries a criterion number and three columns headed `0`, `1` and `2` is
  the **scored table** form. The sentence directly above it states the pass threshold.
- `- [ ]` items under the rubric heading are the **checklist** form. There is no scale and no threshold.

**As of 2026-08-19 the split was 14 scored-table and 12 checklist across the 26 guides. That count is not
gated by anything and is recorded here only as context.** The detection rule above is the authority.

### Why the checklist form is not simply converted on the fly

[`guide-rubric-spec.md`](../../../docs/internal/guide-rubric-spec.md) section 4, item 2 records the open
decision and its reasoning verbatim: a checklist asks "did you do the thing", a scored rubric asks "how
well", and for a short artifact the checklist may genuinely be the right instrument. It instructs that the
checklist guides are **not** converted mechanically, and that one is converted first and read before the
rest follow.

This skill does not convert anything. It applies a scale in order to produce a comparable band, **states in
the report card that the scale is its own**, and routes the question back to that spec. That is
[decision procedure 5](../../../docs/internal/decision-procedures.md): state the rule in the artifact that
applies it, name the document that owns it, route the resolution there, and do not amend the owning
document from inside the change.

**Each checklist-form report card is a data point the open decision needs.** It is worth saying so to the
reader when they ask why the frontmatter carries a caveat.

## 3. Scoring a checklist criterion

The scale this skill supplies, and the reason each step is where it is:

| Score | Meaning |
|---|---|
| **0** | The criterion is not met, and the document contains nothing addressing it |
| **1** | Addressed, but a reader could not act on it, or it is asserted without the evidence the criterion asks for |
| **2** | Met, and the document contains the specific thing the criterion names |

**Apply the guide's own evidential test where the guide states one.** Several guides say plainly that a
criterion is satisfied by pointing at something, not by counting something. Where a criterion could be
cleared by adding items rather than by improving the document, score it on the evidence and say so.

## 4. The variant scope trap

A guide may score some rows against one variant only. Where a scope table exists, it says which. Score a
document only on the rows in scope for the variant it is written at.

Getting this wrong penalises the author for choosing the smaller variant, which is the opposite of what the
guides advise, and it is a defect the library already found and fixed on the authoring side. Reproducing it
on the reading side would be the same defect one layer out.

**Which variant is the document at?** Infer from the sections present. If it carries only lean sections,
grade lean. If it carries full-only sections, grade full. If it is between the two, grade lean and say in
the report card that the document is partway to full, since that is information the author wants.

## 5. Evidence discipline

**Every score below 2 carries a quote or an explicit statement of absence.** No exceptions, and the report
card does not ship without them.

- A quote is copied from the document, never reconstructed from memory of it.
- An absence is stated as an absence: "no non-goals section" rather than "non-goals are weak".
- Where a criterion is met in one place and broken in another, quote the break, not the compliance.

**This rule exists because this library's own review process names unsourced confidence as its dominant
defect class**: plausible, specific, well-written claims that no source supports. A report card is the
easiest possible place to commit it, because critique reads as authority.

## 6. What the grade may and may not be called

The band is arithmetic. It is produced by weights this skill chose so that a report is shareable, and no
research supports the weights or the cut lines.

**Say the grade. Do not defend it as a measurement of quality.** The library measured whether its templates
produce better documents, twice, and the result was VOID both times: the templates beat a strong control on
the bundles' own criteria and did not beat it on criteria drawn from outside the template and the guide.
That is the honest state of the evidence and it is published in
[`evals/results/`](../../../evals/results/).

Where the guide states its own threshold, report it **as the guide's sentence, attributed to the guide**,
separately from the band. Do not restate it as this skill's prediction. Those threshold sentences have been
flagged by three independent reviewers as unsourced predictive claims, and a family-wide rewording is
scheduled.
