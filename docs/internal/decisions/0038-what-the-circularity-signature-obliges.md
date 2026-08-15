---
status: accepted
date: 2026-08-08
decision-makers: [jprisant]
consulted: [claude]
---

# What the circularity signature obliges, and why the eval cannot answer it

## TL;DR

- **Decision:** adopt an **element admission test** and a **three-track triage** that
  routes any candidate property to exactly one of a guide rubric row, a house convention, or a template
  element. **This record proposes a rule, not a template edit.** Applying that rule to the four properties
  the eval surfaced then becomes a mechanical exercise rather than a judgment call.
- **Why:** two independent 114-agent runs put these templates at **+0.85** against criteria drawn from
  their own guide and **-0.03**, spanning zero, against criteria drawn from neither. Deciding what that
  obliges turned out to be impossible, and for two structural reasons that are **missing rules rather than
  hard trade-offs**: the library has no element-level admission test, and the protocol sets **no standard
  at all for what a held-out gap should look like**.
- **Status:** proposed 2026-08-08, substantially revised 2026-08-10, **accepted 2026-08-14**. The first
  draft recommended adopting three of four properties; that recommendation is **withdrawn**, because it
  rested on a number the protocol never gated and because two of the four were never scope questions at
  all. What is accepted is **option B with option D alongside it**: the rule, plus the instrument fix.
  **No template changes as a result of this record.**

## Context and Problem Statement

[The matched re-run](../../../evals/results/2026-08-08_matched-rerun.md) produced two numbers that sit beside
each other and mean something only together:

| Gap (matched arms) | Point | 95% interval | Reading |
|---|---|---|---|
| Rubric criteria, drawn from the templates' own guide | **+0.85** | +0.42 to +1.27 | Real, excludes zero |
| Held-out criteria, drawn from neither template nor guide | **-0.03** | -0.42 to +0.28 | Nothing, spans zero |

Both runs agree within 0.13 on every quantity. Judging noise is 0.14 between panels and 0.42 within one,
so the contrast is larger than the noise in one direction and smaller in the other, which is what makes it
readable rather than an artifact.

[The protocol](../eval-protocol.md) section 3 defines this exactly: *"A large rubric gap beside a
null held-out gap is the circularity signature. The treatment arm has read the answer key: it can win by
mentioning rubric items rather than by being better."*

**The templates move a document toward what they already ask for, and toward nothing else measured.** The
question this record exists to frame is what, if anything, that obliges.

## First, the number has no standard beside it

**The protocol defines four validity gates**: hollow separation, discrimination, agreement and control
sanity ([`eval-protocol.md`](../eval-protocol.md) section 4). **None of them is about the held-out gap.**

So **-0.03 is neither a pass nor a fail.** It is a measurement with no threshold behind it, and any
attempt to decide scope from it requires someone to invent the threshold at the moment of deciding. That
is not a hard judgment call; it is an undefined one, and it is the reason the first draft of this record
produced a recommendation nobody could calibrate.

Two further properties of the number matter before anything is built on it:

* **It measures spillover, and spillover was never established as a reasonable expectation.** The held-out
  criteria are, by construction, things the template does not mention. A template can only move them
  indirectly. A template that does exactly what it says and no more may be **working correctly**, and
  nothing in the protocol says otherwise.
* **The criteria were selected by searching the templates for absences**, which is the right way to prove
  absence and biases the result toward null. [The re-run](../../../evals/results/2026-08-08_matched-rerun.md)
  already records the related independence problem, that the authoring agents had read the templates. The
  sharper form is that **selecting on absence and then measuring absence is close to circular in its own
  right.**

**This does not withdraw the finding.** The rubric gap is real and its interval excludes zero. It means
the *held-out* half is currently uninterpretable as a verdict, and that is fixable: see the proposed
protocol work at the end of this record.

## The four properties are not one kind of thing

Their absence from each template and guide was **searched for rather than assumed**, with the search
recorded per criterion in [`evals/rubrics/`](../../../evals/rubrics/). But they resist a single decision
because they belong to three different tracks, and **only one of the three is a scope question at all**:

| Property | Track | What changing it would actually be |
|---|---|---|
| `no_internal_contradiction`, nothing here contradicts anything else here | **Quality property** | A guide rubric row and a named anti-pattern. No template gains a heading, and **no scope question arises**, because the document is not asked to contain anything new |
| `scopable_without_a_meeting`, a reader could size and sequence the work from this alone | **Quality property** | A guide rubric row. Arguably the implicit goal of several sections already; what is missing is that nothing grades the document *as a whole* against it |
| `decision_vs_input_traceable`, a reader can tell what the author decided from what they were told | **Convention** | A house-style change to how load-bearing claims are written, not a section. If adopted it touches **every guide in the library**, not one |
| `explicit_stop_or_kill_condition`, the document names what would make the team stop or kill this | **Element** | A genuine new section or field. **The only one of the four that is a scope question**, and the only one that needs a source |

**A quality property makes no claim about the world.** "This document should not contradict itself" does
not assert that practitioners write anything a particular way, so it needs no source, no admission test
and no decision record. **An element does make such a claim**: putting a Stop Conditions heading in the
`prd` template asserts that a PRD is the kind of document that carries one, and that assertion can be
wrong.

**That distinction is the resolution.** The first draft of this record treated all four as one scope
decision, which is exactly why its recommendation read as taste rather than as a rule being applied. Two
of the four were never scope decisions.

## Decision Drivers

* **The protocol commits the library to acting on this.** It was written before any number existed, which
  is the only condition under which "we will publish what we find" means anything.
* **The admission test exists and is load-bearing**, and it has twice changed an outcome rather than
  ratifying one (V2MOM, `prototype-brief`).
* **Adding four rubric rows is not free.** Every guide in this library carries a self-grade rubric with a
  threshold sentence, and two independent reviewers have already flagged those thresholds as unsourced
  predictive claims. Adding rows makes that open question bigger, not smaller.
* **The measurement cannot justify its own answer.** See the trap below, which is the single most
  important paragraph in this record.

## The trap, stated before any option is considered

**If the four held-out criteria are added to the templates, they stop being held out.**

The next run's "criteria drawn from neither the template nor its guide" would be criteria the templates now
ask for. The rubric gap would grow, the held-out gap would grow, and **both movements would be
uninformative**, because the instrument would have been rebuilt around the intervention. That is not a
subtle risk; it is the mechanical consequence of teaching to the test, and this library has already
published one number it had to withdraw for a structurally similar reason.

Two consequences follow, and any adopted version of this record must carry both:

1. **The eval identified candidates. It cannot justify them.** A property earns its place because a named
   source publishes documents of that type containing it, or because this library argues for it in its own
   voice and labels it as its own, per decision procedure 11. **"The eval said so" is not an admissible
   reason**, and a record that used it would be committing the unsourced-confidence defect that the
   four-lens review exists to catch.
2. **Any future run must draw fresh held-out criteria**, authored against the post-change templates, with
   the same absence-search discipline. Re-using these four after adopting them would produce a number that
   looks like progress and measures nothing.

## The problem with the governing test, which the maintainer should see before choosing

The continuation brief assigned this question to [ADR 0030's admission
test](0030-templating-scope-markdown-documents.md). Read literally, **that test does not reach it.**

ADR 0030 says: *"A candidate **type** is templatable when a named source publishes it **as a written
document** ... not 'could someone write this', but 'does someone'."*

It admits and rejects **document types**. It says nothing about **elements within** an admitted type. The
question "should the `prd` bundle ask for a stop-or-kill condition" is not "is a PRD a real document", and
`prd` was admitted long ago.

So one of three things must be true, and this record cannot choose between them:

* **(a) The test extends by analogy.** The element-level form would be: *a section is admissible when a
  named source publishes documents of that type containing it.* Clean, consistent with ADR 0028's lineage,
  and it makes the fourth criterion an evidence question rather than a taste question.
* **(b) The test does not apply, and the governing rule is decision procedure 11**: the library may state
  its own position provided it labels the claim as its own rather than as received practice. This is the
  route `standing-standards` already took for its Review Trigger sections, which are labelled as the
  bundle's own contribution precisely because the literature supplies no condition-based trigger.
* **(c) Neither, and a new rule is needed.**

**This is a live gap in the library's own rules, not a detail of this proposal**, and it will recur the
next time anyone proposes a section rather than a bundle. It is closely related to the open item already
recorded in [`STATE.md`](../../../STATE.md): ADR 0028's format-admission rule turned out to have a third
criterion in practice that the written rule does not contain.

## Considered Options

* **A. Decide the four case by case, now.** What this record's first draft proposed. **Rejected:** two of
  the four are not scope questions, and the one that is would be decided against a number the protocol
  never gated.
* **B. Adopt a rule first, then apply it.** A three-track triage plus an element admission test. The four
  properties become the rule's first worked application rather than four separate arguments.
* **C. Adopt nothing and close the finding.** Named rather than dismissed: a template's job may
  legitimately be to make documents match a good shape, and the re-run takes no position on whether that
  is valuable.
* **D. Fix the instrument first**, and re-open the question when the held-out gap means something.

## Decision Outcome

**B, with D running alongside it. Accepted 2026-08-14.**

D was accepted separately and on its own merits, because it is independent of any scope decision and would
have been worth doing even if C had been chosen. **C was considered and rejected**, not skipped: the
maintainer was asked to reject it consciously and did. The reason for preferring B is that the rule outlives
this eval and is re-runnable by a future maintainer, whereas C closes one question and leaves the next
proposed section facing the same undefined judgment call.

**Nothing about the four properties is decided by this acceptance.** The rule is adopted; its first
application is still pending the source search named below.

### The proposed triage: which track is this candidate on?

Applied in order, and it terminates for most candidates at step 1:

1. **Is it a claim about the world?** That is, does adopting it assert that documents of this type are
   written a particular way? **If no**, it is a **quality property**: it becomes a guide rubric row, and
   this record's machinery does not apply. No source, no admission test, no decision record.
2. **If yes, is it about what the document contains, or about how its claims are written?** *How* is a
   **convention**: it is house style, it is adopted across every guide at once or not at all, and it is
   argued on consistency rather than on evidence.
3. **Otherwise it is an element**, and it faces the test below.

### The proposed element admission test

Generalises [ADR 0030](0030-templating-scope-markdown-documents.md), which generalised
[ADR 0028](0028-adopt-a-format-axis.md). A template may ask a document to **contain** an element when:

* **E1, sourced.** A named source publishes documents of that type containing that element, in
  circulation. **The search must be capable of returning "no"**, which is what made `prototype-brief` fail
  ADR 0030's test rather than pass it decoratively.
* **E2, or labelled.** Failing E1, the library argues the element in its own voice under decision
  procedure 11, labels it as the library's own contribution rather than as received practice, **and states
  what would falsify it**. This is the route `standing-standards` already took for its Review Trigger
  sections.
* **E3, homed.** Name the artifact where the element would otherwise live. If a better home exists, it
  goes there instead. Without this clause every template becomes a junk drawer for good ideas, which is
  the failure mode ADR 0030 was written against in a different costume.
* **E4, sized.** It fits the lean variant, or it ships in `full` only. Lean is the default and stays the
  default; an element that pushes lean past its weight has changed the variant model, not added to it.

E1 or E2 is required. E3 and E4 are required in both cases.

### What the four properties do under this rule

Stated as the rule's first worked application, and **not as a decision**:

| Property | Track | Where it lands |
|---|---|---|
| `no_internal_contradiction` | Quality property | Rubric row. Terminates at step 1, needs nothing further |
| `scopable_without_a_meeting` | Quality property | Rubric row. Terminates at step 1 |
| `decision_vs_input_traceable` | Convention | A family-wide guide edit, argued on consistency, competing with the twice-raised rubric-threshold question already open in [`STATE.md`](../../../STATE.md) |
| `explicit_stop_or_kill_condition` | Element | Faces E1 through E4. **No search has been run**, and this record asserts nothing about whether one would succeed |

### What acceptance required, and where each item stands

| Follow-through | State |
|---|---|
| **Write the test into [`decision-procedures.md`](../decision-procedures.md)** as a numbered procedure, so it is citable from any future bundle rather than living inside one ADR about one eval | **Done 2026-08-14**, as procedure 12 |
| **Add the gap question to [`bundle-pipeline.md`](../bundle-pipeline.md)** as a standing research dimension: *what does a good document of this type do that this bundle does not ask for?* This is the part that makes it systematic; the question has so far been asked once, as a byproduct of building an eval | **Done 2026-08-14**, as research dimension 6 |
| **A protocol decision on the held-out gap** (option D): state what a passing gap looks like, or declare it deliberately non-gated and say why. And **change how held-out criteria are selected**, from searching the templates for absences to drawing them independently and measuring coverage afterwards | **Accepted, execution pending.** Both land in [`eval-protocol.md`](../eval-protocol.md) |
| **A source search for the stop-or-kill element**, per affected bundle, logged to the same standard as any bundle's research pass | **Not started.** It is the rule's first real application, and it may return "no" |
| **Fresh held-out criteria** for any subsequent run, if any template changes | **Not applicable yet.** No template has changed |

### Consequences

* Good: **the decision stops being a judgment call and becomes a rule application.** That is the only form
  in which this library has ever settled a scope question, and the only form a future maintainer can
  re-run.
* Good: two of the four properties leave the scope conversation entirely, at step 1, and cost a rubric row
  each.
* Good: the rule outlives this eval. The next candidate element arrives with a test already written.
* Bad, and stated plainly: **E3 will reject good ideas.** An element that genuinely improves a document
  but belongs in an adjacent artifact gets turned away, and the library has no mechanism to remember what
  it turned away or why. That is a real cost of the clause, not a hypothetical one.
* Bad: a convention adopted under step 2 is argued on **consistency rather than evidence**, which is a
  weaker footing than E1 or E2, and this record does not fix that.
* **Open, and deliberately not closed by this record:** whether the templates *should* move a document
  toward anything beyond their own criteria at all. A +0.85 rubric gap may be exactly what a user wants, and
  [the re-run](../../../evals/results/2026-08-08_matched-rerun.md) explicitly takes no position on whether
  scoring better against a document type's own standards is valuable. **Adopting the rule does not answer
  this**; it only ensures that whoever does answer it applies a test rather than a preference. Option C was
  rejected as a way of *closing* the question, not as a possible answer to it.

## More Information

* [The matched re-run](../../../evals/results/2026-08-08_matched-rerun.md), which produced the signature, and
  the two independent runs behind it.
* [The eval protocol](../eval-protocol.md), section 3, which named the signature before any number existed.
* [`evals/rubrics/`](../../../evals/rubrics/), where each held-out criterion carries the recorded search that
  established its absence from the template and guide.
* [ADR 0030 (templating scope)](0030-templating-scope-markdown-documents.md) for the admission test this
  record argues does not reach element-level questions, and
  [ADR 0028 (the format axis)](0028-adopt-a-format-axis.md) for its lineage.
* [ADR 0032 (standing-standards)](0032-adopt-standing-standards-family-contract.md) for the worked
  precedent of a section shipped as the library's own labelled contribution when the literature supplied
  none.

**Three of the twenty-six bundles were measured.** Nothing here generalises to the other twenty-three, and
any adopted version of this record should say which bundles it believes it is talking about.
