---
status: accepted
date: 2026-11-14
decision-makers: [jprisant]
consulted: [claude]
---

# The diary study plan is declined as a separate type; `user-research-plan` gains a conditional diary block

## TL;DR

- **Decision.** The diary study plan, the diary half of catalog entry 28 ("Diary Study / Field Study plan"), **does
  not ship as a bundle of its own**. A diary study plan is a user research plan whose method is a diary study.
  `user-research-plan` (catalog entry 210) gains a conditional diary block in a minor version, like its usability
  Tasks and Measures block.
- **Why.** No source read publishes a diary study plan as a document separate from a research plan. Nielsen Norman
  Group lists the diary items to "document them in your study plan".
- **What this leaves open.** The field-study and contextual-inquiry half of entry 28 stays unswept.
- **Status:** accepted 2026-11-14. The maintainer read sweep 8's batched decisions and answered "D1 a". A decline is a
  scope ruling, so it was put to the maintainer, not delegated.

## Context and Problem Statement

A placement pass on 2026-10-23 ruled entry 28 "a method-specific sibling, not an alias" of `user-research-plan`, at
medium-high confidence, and the shipped companion says the same (`user-research-plan_companion.md`, line 617). That
ruling compared the diary plan with catalog entry 210, not with the shipped template. Admission sweep 8 tested it
against the template on 2026-11-14:

1. All seven web quotes from the 2026-10-23 record passed a fresh raw read.
2. One Sonnet critic applied the five checks, recommended evidence-insufficient at medium confidence with this
   outcome the likelier reading, and named the read that would settle it.
3. The main loop did that read: NN/g's diary-studies page, raw.
4. One Sonnet reader looked for a separate diary plan template on dscout and Dovetail, and found none.

The working files are gitignored, at `_local/research/2026-11-14_admission-sweep-8/`.

## The evidence

- **NN/g puts the diary items inside the study plan.** Its lead-in reads: "After defining the goals of the study, you
  will need to consider a few important aspects (and document them in your study plan):" The nine items are when
  participants create entries, length of the study, number and profile of participants, incentives and response
  requirements, tools, communication templates and supporting materials, a pilot study, a pre-study brief and a
  post-study interview.
- **User Interviews points back to the general plan** for goals and research questions, then plans the diary in five
  phases.
- **Dovetail treats a diary study as a method.** Its research-plan page lists "Diary studies" among methods, and its
  research-plan template has no diary block.
- **dscout's diary study guide is a how-to, not a template.**
- **The library has a precedent for this shape.** `user-research-plan` already carries a conditional Tasks and
  Measures block for the usability test method.

## Considered Options

1. **Decline the separate type; add a conditional diary block to `user-research-plan`.** Chosen.
2. **Admit it to `research-docs` with an amendment.** Rejected: no source shows a separate document, and the family's
   section 4 binds every example to an interview study, which a diary plan cannot plan.
3. **Park until dscout's help-centre templates are read.** Rejected by the maintainer's choice. Those templates are
   the reopening condition below.

## Decision Outcome

**Chosen: decline, with a diary block.** Decision procedure 12's element test (E1 to E4) decides which of NN/g's nine
items join the template, at the `user-research-plan` minor version. The sweep's provisional reading is that only the
entry timing (event, interval or signal) and the response requirement are new. The other items already have homes:
Schedule and Logistics, Participants, Method and Related Documents.

- "Diary study plan" is **not** added as an alias of entry 210, because no source sentence states that identity, as
  one does for "usability test plan".
- `research-docs` needs no change. Its membership clause already names diary studies as a method of a member's one
  study.

**Reopening conditions.** dscout's help centre (`help.dscout.com`) reportedly has three built-in diary templates. If
one is a plan document with its own sections, separate from a research plan, this decline reopens.

### Consequences

- Catalog entry 28 gains a dated note recording this decline for its diary half.
- `user-research-plan` takes a minor `template_version` bump inside its own bundle PR. That is not a library release.

## More Information

- The bundle that absorbs the type: [`templates/user-research-plan/`](../../../templates/user-research-plan/).
- Family contract: [`research-docs`](../contracts/research-docs.md).
- The plan that ran the sweep: [`section9-candidates-plan.md`](../section9-candidates-plan.md).
