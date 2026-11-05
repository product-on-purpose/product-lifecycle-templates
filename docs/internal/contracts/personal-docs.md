# Family Contract: personal-docs

**Status:** **proposed 2026-11-05**, [ADR 0085](../decisions/0085-manager-user-guide-opens-a-personal-docs-family.md).
Not yet registered in check K. It takes effect only after the maintainer reads this contract and accepts that
record.
**Axis:** `classification`, single value `utility`.
**Members:** `manager-user-guide` (planned; not yet built).

Written before its member is built, per the
[ADR 0020 (delivery-docs family contract)](../decisions/0020-adopt-delivery-docs-family-contract.md) pattern.

**This family has one planned member, and that is stated rather than hidden.** A one-member family is a legal
shape, as `communication-docs` shows. The test of a family is whether it was drawn around a real category or around
a single document that needed somewhere to live. On today's evidence, this one is closer to the second. Section 1
says why it exists anyway.

## 1. Membership

A bundle belongs to this family when its document type is **written by one person, about themselves, for the people
who work with them.** Its author is its subject, nobody agrees to it, and it is useful only while it is true.

- a **manager user guide** tells a manager's direct reports how that manager works and how to work with them.

**The defining property is that the author is the subject and the only authority.** That is why no other family holds
it. A standard readers are judged against, or an instrument they execute, belongs in `standing-standards`. A document
that summarises facts held elsewhere for an audience outside the team belongs in `communication-docs`.

**A candidate written by a team about itself is not a member.** On the catalog's descriptions, a team charter (entry 80)
and a working agreement (entry 100) are agreed by a team, so they fit `standing-standards` as written. Neither has been
swept, and this sentence is a forecast. A candidate that trains people on a product or process, such as an onboarding
guide (entry 195), is not about its author and is not a member either.

**Likely future members:** none is named. A README written by someone who is not a manager is the same type, covered by
the member's own guide. If nothing else ever joins, this family stays at one member, and that is an acceptable outcome.

## 2. Required catalog metadata and allowed values

| Field | Allowed values for this family |
|---|---|
| family | `personal-docs` |
| classification | **`utility`**, single value. See the axis note below |
| methodology | **Descriptive, not gated** |
| sizes_available | `[lean, full]`, or `[lean]` where the type's research shows it does not earn a second weight |
| status | `beta` until the maintainer judges the bundle settled ([ADR 0055](../decisions/0055-retire-the-zero-fills-disclosure.md)) |
| pairs_with | pm-skills skill ID(s) or `[]`, resolving against `tools/known-skills.txt` |

**Why `classification`, and why `utility`.** A guide of this kind is tied to no lifecycle stage. It belongs to a person
and stays in use for as long as they hold the role, so it takes the `classification` axis
([ADR 0015 (phase XOR classification)](../decisions/0015-second-taxonomy-axis-phase-xor-classification.md)). `utility`
describes a standing document that is valuable only while current. `foundation` implies an argued, agreed basis that other
work is measured against, and that is the reading this family exists to avoid. `tool` implies an instrument someone
executes. This call is a POSITION, at medium confidence, because no readable source states how often such a guide is revised.

## 3. Structural obligations (gate-checkable)

1. **The eight files**, prefixed `<type>_`. A single-size member ships seven.
2. **Nesting**, where two sizes exist: lean's H2s are a strict ordered subset of full's, with the same names and order.
3. **Guidance comments.** Approach A in every section of every variant, with a "How to fill this in" preamble, inside the
   first comment block, that states the N/A rule and the self-grade step.
4. **Companion skeleton.** All 11 sections of methodology section 5, with one Anatomy subsection per template section.
5. **Guide shape.** When to use; when NOT to use; pick a variant; a rubric conforming to
   [`guide-rubric-spec.md`](../guide-rubric-spec.md); at least six named anti-patterns.
6. **Citations.** Methodology section 6 in full. **This family's specific citation hazard is that its literature is
   personal essays and individual examples.** Record an essay as one person's argument, and record an example as one
   instance, not as evidence of general practice.
7. **Example.** One fully worked instance, no placeholders, figures labeled, provenance stamped, and **independent of the
   template's own GOOD and WEAK text**. No member is grandfathered.

## 4. The two-way obligation (family-specific)

Every other family carries a shared-scenario rule or a rule shaped by its own failure mode. This one has three failure modes
named by critics, and every member must ship a mechanism for each.

1. **It can become a one-way instruction.** The template must carry a section in which the author says how to tell them they
   are wrong, and through which channel. The guide must say that the document does not replace that conversation.
2. **It goes stale silently.** The template must carry a review trigger, with a condition and not a calendar reminder: what
   event makes this document wrong, and who may correct it.
3. **It can claim an authority it does not have.** The template must say, in its opening section, that the document states
   one person's preferences and that nobody has agreed to them.

**On the shared scenario.** A member's example is written by a named person on the **Acme Analytics** thread, and it must
contradict no sibling example. The chain is weak by design, because the document belongs to a person and not to a moment in a
story.

## 5. Shareable-boundary rule

Template body is the reusable shape; guidance lives only in comments; example content never leaks into templates; meta
describes the asset, never the filled instance. A guide that has grown explanatory or a companion that has grown procedural is
out of contract even if every file exists.

## 6. Enforcement

**Family check letter K**, once registered, validates section 2's values for every declared member and that this contract
resolves. A member declaring `phase` fails with a message naming the axis it should have used. Of section 3, the eight files,
nesting, citations and the clean example are enforced by checks A, C, E and D. Guidance comments, the companion skeleton and
guide shape are review obligations. Section 4 is a review obligation at authoring time and an audit obligation thereafter.

## Change note

**0.1.0 (proposed 2026-11-05, [ADR 0085](../decisions/0085-manager-user-guide-opens-a-personal-docs-family.md)):** drafted,
pending the maintainer's read. It would be the twelfth family contract and the second one-member family, after
`communication-docs`. Section 1's forecast and section 2's axis call are this library's reasoning, labelled as such per
[procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world).
