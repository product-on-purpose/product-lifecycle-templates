# The EV-3 feedback form, and the usage log entry

This is the only route by which this library learns anything from someone who is not its author. It is a
step in the flow, not a courtesy at the end of it.

## Ask these five, after delivering the report card

1. **How useful was this, 1 to 5?**
2. **Which finding was the most valuable?**
3. **Was anything wrong or unfair?**
4. **Would you use the template for the next one of these?**
5. **May this be logged anonymously?**

**Question 3 is the one that pays.** A grader is confidently wrong in a way that reads as authority, and
the person holding the document is the only one who can see it. Ask it plainly and record the answer even
when it is uncomfortable, especially then.

**Question 5 gates the write.** No entry is written without a yes.

## The log entry

Write to `evals/usage-log/YYYY-MM-DD_<type>.md` when the repository is on disk. When it is not, hand the
reader the filled entry and ask them to send it, because the CLI install route has nowhere to write.

```markdown
---
date: 2026-01-01
doc_type: prd
variant_graded: lean
rubric_form: checklist
scale: grader
grade: B
structure: 9/10
quality: 21/30
anti_patterns_hit: 1
usefulness: 4
would_use_template: yes
consented: yes
---

**Most valuable finding:** <their words, quoted>

**Wrong or unfair:** <their words, quoted, or "nothing reported">

**Notes:** <anything the grader got structurally wrong, in the grader's words>
```

## What never goes in the log

- **The document.** Not the text, not a summary of its content, not the quotes the report card used as
  evidence. The scores and the type are the record.
- **The author's name, their team, their company, or their product's name.** The frontmatter has no field
  for any of them, deliberately.
- **A reconstruction of the document from the findings.** If an entry would let a reader infer what the
  product was, cut it.

## Why the log is separate from `evals/results/`

[`evals/results/`](../../../evals/results/) holds runs of the efficacy harness: blinded, four-armed,
LLM-judged, and designed to answer whether the templates help. This log holds something weaker and more
useful at this stage, which is **whether a real person found a real report card worth their time**.

Do not mix them, and do not report a usefulness average as an efficacy number. They measure different
things and the harness is the one with a protocol written before it saw a result.
