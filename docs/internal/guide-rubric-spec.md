# Spec: the guide quality rubric, and the backfill to converge on it

Status: **spec, ready to execute**. Adopted 2026-07-27 as option C (decide the house style now, apply to
`product-vision`, backfill the rest opportunistically).

This is the executable spec for that backfill. It exists because an inventory of all 16 guides found three
different rubric forms in the tree and no written rule, so each new bundle has been inventing one.

---

## 1. What the inventory actually found

Contrary to the assumption that started this work, **a house style already exists**. It is used by the three
most recently and most rigorously built guides, and it was not written down anywhere.

| Rubric form | Bundles | Notes |
|---|---|---|
| **0/1/2 scored table with an explicit pass threshold** | `bug-report` (8 rows, 10/16), `test-case` (8 rows), `test-plan` (9 rows, 12/18) | The de facto house style. Numeric, with a stated cut line. |
| **Strong / Adequate / Weak table** | `product-vision` (12 rows) | **The deviation.** Introduced 2026-07-26 without checking the others. |
| **Checklist** (`- [ ]` items under `## Quality rubric`) | `acceptance-criteria`, `prd`, `release-notes`, `user-stories` | The four earliest guides. Usable, but ungraded: no score, no threshold. |
| Comparison tables, not rubrics | `adr`, `kpi-dashboard`, `product-backlog`, `raid-log`, `rfc`, `risk-register`, `sdd`, `sprint-backlog` | These guides carry the contract sections but their rubric is prose or checklist; the tables detected in them are artifact-comparison tables, not rubrics. **Confirm per guide during execution.** |

**The surrounding structure is already consistent** and is not in scope here: every guide checked carries
"When to use", "When NOT to use", "Pick a variant", a quality rubric and named anti-patterns, as the family
contracts require.

## 2. The house style, stated

**A guide's quality rubric is a numbered table scored 0/1/2, with an explicit pass threshold in the sentence
above it.**

```
Score each 0, 1 or 2. Under 10 out of 16 and the report will come back with questions instead of a fix.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Reproducible** | No steps | Steps that start mid-flow | Numbered steps from a named starting state |
```

Rules:

1. **Three columns, scored 0, 1, 2.** Not Strong/Adequate/Weak, not pass/fail.
2. **An explicit threshold above the table**, expressed as a consequence rather than a grade: what happens to
   the reader or the work if the document lands under the line.
3. **Cells describe evidence, not counts.** See section 3.
4. **6 to 12 rows.** Fewer and it is a checklist; more and nobody completes it.
5. **Row titles are properties of the document**, bolded, two to four words.

## 3. Evidential, not countable (the rule that matters)

A threshold that can be satisfied by adding items will be satisfied by adding items. This library has already
documented the mechanism: the `bug-report` research found that **defect counts get gamed the moment they
become targets**, in named ways - splitting one bug across tickets, filing trivial ones to hit a quota.

A rubric cell is a target. Write it so it cannot be cleared by padding.

| Countable, and gameable | Evidential, and not |
|---|---|
| "2: names at least two exclusions" | "2: you can point at the sentence, and name the request it refused and who asked" |
| "2: has three or more acceptance criteria" | "2: every criterion could be marked pass or fail by someone who did not write it" |
| "2: lists five risks" | "2: at least one risk has an owner who has seen it and disagreed with the rating" |

The test for a cell: **could someone satisfy this without improving the document?** If yes, rewrite it.

## 4. Scope and sequencing

**Item 1, `product-vision`: DONE 2026-07-27**, converged inside PR #46 before that PR merged rather than
left to a follow-up. Its 12-row Strong/Adequate/Weak table is now 0/1/2 scored with a threshold stated as a
consequence, and the "(not lean canvas)" scope markers on rows 9 and 10 are preserved.

**Item 2: the four checklist guides** (`acceptance-criteria`, `prd`, `release-notes`, `user-stories`). These
need a decision before conversion, recorded here as an open question rather than assumed:

> **`acceptance-criteria` was converted 2026-08-21**, which is the experiment the instruction below asks
> for and **not an answer to it**. The question of whether `prd`, `release-notes` and `user-stories` follow
> is still open and still stops for the maintainer. **Two things worth reading before deciding**: the
> conversion produced **seven rows, one below the smallest scored sibling**, and named anti-pattern 6
> ("criteria as afterthought") **has no rubric row and had none as a checklist item either**, so no
> criterion in either form can detect a document written after the code.
>
> **The scope of this item is also wider than it says.** It names four guides against a **16-guide** tree
> on 2026-07-27. The tree now holds **26**, and **eleven** carry a checklist, so eight were never in
> anyone's scope. Counted 2026-08-21 by testing every guide, not from a list.

> A checklist and a scored rubric do different jobs. A checklist asks "did you do the thing"; a scored rubric
> asks "how well". For a short artifact such as a set of acceptance criteria, a checklist may genuinely be
> the right instrument. **Do not convert these mechanically.** Convert one (`acceptance-criteria` is the
> best candidate, being the most-used), see whether the scored form reads better, and decide from that.

**Item 3: the remaining eight guides.** Audit each for whether it has a rubric at all, and bring it to the
house style when that bundle is next touched for another reason. **No big-bang rewrite.** These bundles are
gate-green and reviewed; churn on them buys presentation, not correctness. The same reasoning that produced
[ADR 0029](decisions/0029-gate-the-research-log-contract-not-its-layout.md).

## 5. Acceptance criteria

A guide has converged when all of these hold:

- [ ] The rubric is a numbered table with columns `# | Criterion | 0 | 1 | 2`.
- [ ] A sentence above it states the pass threshold **as a consequence**, not as a grade.
- [ ] Every cell describes observable evidence; none can be satisfied by adding items (section 3 test).
- [ ] Row count is 6 to 12.
- [ ] Rows that do not apply to every variant or format carry an inline scope marker, e.g. *(not lean)*.
- [ ] The surrounding contract sections are intact: when to use, when NOT to use, pick a variant, named
      anti-patterns.
- [ ] The gate is green and `check-links.py` passes.

## 6. What this spec deliberately does not do

- **It does not add a gate check.** Rubric quality is not machine-checkable, and a check that counted rows or
  matched a header would be exactly the countable-target failure this spec warns about. This is a house style
  enforced by review, and saying so is more honest than a check that pretends.
- **It does not touch the guide's other sections.** Those are already consistent.
- **It does not mandate identical row counts or wording across bundles.** Different document types are judged
  on different properties.

## 7. Provenance

The de facto style was read off `bug-report`, `test-case` and `test-plan` on 2026-07-27 by inventorying all
16 guides. The gaming argument in section 3 comes from the `bug-report` research log, which documents
measured ways defect counts are manipulated once they become targets. Nothing in this spec rests on a source
that was not read.
