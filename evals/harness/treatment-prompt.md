---
title: "The matched treatment-arm prompt"
description: "The discipline instruction the matched treatment arm receives alongside the template and guide, held byte-identical to the control's so the arms differ only in whether one has a template"
audience: engineer
level: advanced
tags:
  - evals
  - measurement
---

# The matched treatment-arm prompt

**Version 1, 2026-08-08.**

This file is public and versioned for the same reason
[`control-prompt.md`](control-prompt.md) is: **an arm that was told more than another arm has an advantage
that has nothing to do with what is being measured.** Both prompts are written down so that a reader who
thinks one arm was favoured can point at the sentence that favoured it.

**This file is deliberately kept at the same disclosure level as the control prompt.** It says what this
arm receives and why the wording is fixed, and nothing about what the finished documents are scored on. The
design reasoning for the arm lives in [the eval protocol](../../docs/internal/eval-protocol.md) section 2,
which no arm reads.

## What this arm gets and does not get

**Gets:** the scenario, the context pack, the document type by name, this library's blank template and its
guide, and the discipline instruction below.

**Gets, and this is the whole point of the arm:** the discipline instruction below is **byte-identical** to
the one the control arm receives. Not a paraphrase of it. A paraphrase would leave open the argument that
one arm was handed better-worded advice, which is precisely the difference this arm exists to eliminate.
[`tools/check-eval-arm-parity.py`](../../tools/check-eval-arm-parity.py) fails CI if the two blocks diverge
by a single character, because two hand-maintained copies of one paragraph is a drift this repository has
been bitten by repeatedly.

**Does not get:** any scenario section marked as an answer key, and any freedom over structure. That second
one is not an oversight. The control is told to organise its document however it judges best; this arm is
told to follow a template. **That difference is the independent variable**, so making it identical would
delete the comparison rather than clean it up.

**Length parity.** The same word budget applies to every arm under a stated rule, so length alone cannot
separate them.

---

## The prompt

This arm receives the following **in addition to** the template and the guide, not instead of them.

> You are an experienced practitioner writing a **{doc_type}** for the situation described below, using the
> template and guide you have been given. Write the document you would actually hand to the team.
>
> Bring the standard discipline this kind of document deserves:
>
> - **State the problem with evidence**, not as an assertion. Say what you know, how you know it, and how
>   confident you are.
> - **Define success up front**, in terms someone could later check. If a number matters, name it and say
>   what value would count as good.
> - **Say what is out of scope**, explicitly, so a reader can tell an omission from a decision.
> - **Name the risks and the unknowns**, including the ones that would be uncomfortable to raise, and say
>   what you would do about each.
> - **Make it actionable.** A reader should be able to act on this without booking a meeting to ask you
>   what you meant.
> - **Distinguish what you were told from what you concluded.** Where the input is thin or contradictory,
>   say so plainly rather than smoothing it over.
> - **Be concrete.** Prefer a specific claim you can defend over a general one that sounds safe.
>
> Follow the template's structure. Where the template has no obvious place for one of the points above,
> put it where a reader would look for it rather than dropping it. Write the whole document, not an
> outline.

**That closing sentence is load-bearing and is not padding.** Without it, a discipline point the template
has no home for would be lost, and the run could not tell the difference between a template that suppresses
something and an arm that was never really asked for it. With it, a point that still fails to appear is a
fact about the template.

---

## Change log

A change here changes this arm, which changes every number this arm has ever produced. Each version is
dated and kept, and results record which version produced them.

| Version | Date | Change |
|---|---|---|
| 1 | 2026-08-08 | First version. Seven discipline points, byte-identical to control prompt version 1; the framing differs by design, because freedom over structure is the independent variable. |
