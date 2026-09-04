---
title: "Evaluating a template you actually used"
description: "How to turn one real use of a template into evidence the library can learn from, in about ten minutes"
audience: both
level: beginner
---

# Evaluating a template you actually used

**This is optional.** No build in this library waits on it
([ADR 0043](../internal/decisions/0043-the-usage-gate-becomes-advisory.md)). It exists because the library
used to demand feedback without ever saying how to give it, and a demand without a method produces neither.

**It takes about ten minutes** and it is worth doing after you use a template on something real: a document
you would have written anyway, for work that matters to you or someone else.

---

## What counts as a real use

One filled document whose content is real work, not an example written to show the template off. That is
it. Both of these count:

- **You filled it for your own real work.** This satisfies the "real work artifact" half of the M3
  criterion in [`roadmap.md`](../internal/roadmap.md).
- **Someone else filled it, for anything.** This satisfies the other half.

**What does not count:** a trial run, a document written to test the template, or an example. Not because
those are worthless, but because a template will always look good on a document written to suit it. **The
whole value of this exercise is that the work came first and the template had to fit it.**

---

## The checklist

Work through it in order. **Answer honestly, including the answers that make the template look bad** - those
are the only ones that can change anything.

### Before you forget the experience

- [ ] **Which template, which variant, which version?** Lean or full, and the `source_template_version`
      from your document's frontmatter.
- [ ] **What was the document actually for?** One sentence. Not the type, the purpose.
- [ ] **Did you finish it?** If you abandoned it partway, that is the most useful data point in this
      document and the rest of the checklist can be skipped.

### What the template did

- [ ] **Which section did you have no idea how to fill?** Name it. "None" is a legitimate answer and a good
      sign.
- [ ] **Which section did you delete or ignore?** A section every user removes is a section that should not
      be there.
- [ ] **Which section made you write something you would not have written otherwise?** This is the one that
      matters most. If the answer is none, the template organised your thinking but did not change it, and
      that is worth knowing plainly.
- [ ] **Did the guidance comments help, or did you strip them unread?**
- [ ] **Did you fight the structure anywhere?** Reordering, merging sections, or wanting a section that did
      not exist.

### What happened after

- [ ] **Did a reader get what they needed from it?** If someone actually read it, what did they ask you
      that the document should have answered?
- [ ] **Would you use it again for the same kind of document?** Yes or no, and the reason in one clause.
- [ ] **What would you change about the template?** Concrete, not "make it better".

### Before you write anything down

- [ ] **Would this entry let anyone identify the product, the company, or a person?** If so, cut until it
      does not. See the rule below.
- [ ] **Do you consent to it being recorded?** For your own work this is your call alone. **For anyone
      else's document, no entry is written without their explicit yes.**

---

## Writing it down

Two places, and they are for different things.

**1. The bundle's own history**, `templates/<type>/<type>_history.md`. One short entry under the current
`template_version`, saying that a real document was filled and what it exposed. This is where a future
author of that bundle will look.

**2. The usage log**, `evals/usage-log/YYYY-MM-DD_<type>.md`, when a document was **graded** for someone.
Its format and the five questions behind it are in
[`feedback-form.md`](../../skills/plt-grade-doc/references/feedback-form.md). That file governs; do not
invent a second format here.

### The rule that does not bend

**The log never holds the document.** Not the text, not a summary of its content, not the quotes a report
card used as evidence, and nothing from which the product could be identified. Scores, the type, and the
reader's own words about the *template* are the record. A person's document is theirs.

---

## What good feedback looks like

The difference is almost always specificity, and specificity is uncomfortable.

| Weak | Strong |
|---|---|
| "The template was helpful." | "The Out of Scope section made me write down that we were not doing SSO, which I had been avoiding saying to the team." |
| "Some sections did not apply." | "I deleted Dependencies. Single-team work, nothing to depend on, and leaving it empty looked like an oversight." |
| "The guidance was good." | "I read the ASK lines and stripped the rest unread. The GOOD and WEAK examples I never looked at." |
| "It could be clearer." | "Scope and Goal and Context felt like the same question asked twice, and I wrote the same paragraph in both." |

**The test:** could someone rewrite the template from your feedback without asking you a follow-up
question? If not, it is not specific enough yet.

---

## What this evidence can and cannot do

**It can:** change a template, retire a section, move a bundle from `beta` toward `stable` eligibility,
and tell the next author what a real user actually did.

**It cannot:** become an efficacy claim. One person's experience of one document is not a measurement, and
the library keeps those separate deliberately. Efficacy runs live in [`evals/results/`](../../evals/results/)
under [a protocol](../internal/eval-protocol.md) written before any number existed, and its own rules
forbid quoting a usage average as an efficacy number. **Both are evidence. They are not the same evidence,
and neither substitutes for the other.**
