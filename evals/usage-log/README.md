---
title: "Usage log"
---

# Usage log

**Empty, and that is the honest state.** Nobody outside this library's author has graded a document with
it. When that changes, the entries land here.

This is where [`plt-grade-doc`](../../skills/plt-grade-doc/) writes an EV-3 feedback record after grading a
real document for a real person. One file per grading, named `YYYY-MM-DD_<type>.md`. The entry format and
the five questions behind it are in
[`feedback-form.md`](../../skills/plt-grade-doc/references/feedback-form.md).

## What an entry holds, and what it must never hold

An entry holds the document **type**, the date, the variant graded, the rubric form, the scores, and the
reader's answers to five questions.

**It never holds the document.** Not the text, not a summary of its content, not the quotes the report card
used as evidence, and nothing from which the product could be identified. A grading is a service to the
person who asked for it, and their document is theirs.

**No entry is written without recorded consent.** The fifth question asks for it and the frontmatter
records the answer.

## Why this is not `results/`

[`results/`](../results/) holds runs of the efficacy harness: blinded, four-armed, LLM-judged, with a
protocol written before the first number existed. Both of its runs returned VOID.

This directory holds something weaker and, at zero external users, more useful: whether a real person found
a real report card worth their time. **A usefulness average from this log is not an efficacy number**, the
two must not be reported together, and the harness is the one with the protocol.

## The first entry is the milestone

The roadmap's M3 exit criterion is a first external document graded with an EV-3 form banked. `STATE.md`
records "zero fills by anyone but the author" and will keep recording it until a file appears here that
somebody else's document produced.
