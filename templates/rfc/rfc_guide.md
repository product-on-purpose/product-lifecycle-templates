# Guide: RFC (operator card)

Fast reference for using the RFC bundle. For the full reasoning, history, and sources, read
[`rfc_companion.md`](rfc_companion.md).

## When to use

- You want to make a change that **affects people beyond yourself**, and their input could improve it
  or catch a flaw before you build.
- The decision is **not yet made**, and you genuinely want to shape it with feedback. (If it is made,
  see "When NOT to use.")
- More than one reasonable approach exists, and choosing well matters.
- You need durable **alignment** across people who were not in the room, and a record of why.

## When NOT to use

- **The decision is already made.** Writing an RFC to perform consultation that already happened is
  RFC theater; everyone can tell. Write an [ADR](../adr/adr_guide.md) instead.
- **The change is trivial or fully reversible.** A quick message or a pull-request description is
  enough. An RFC for a one-line, back-out-in-a-minute change is process for its own sake.
- **It affects only you or only your immediate team, with no external impact.** Talk it through and
  record it lightly.
- **Speed is the binding constraint** and the RFC's review period would cost more than the mistake it
  prevents. Some decisions are cheaper to make and reverse than to circulate.
- **You have no decider and no deadline.** Do not start an RFC you cannot finish; a process with no
  authority to decide produces open threads, not decisions.

## RFC or ADR? (the question people actually have)

| | **RFC** | **ADR** |
|---|---|---|
| Timing | **Before** the decision | **After** the decision |
| Question | "Should we, and how?" | "What did we decide, and why?" |
| State | Mutable while open | Immutable once accepted |
| Asks for | Input from an audience | Nothing; it records |
| Lives | In shared docs / discussion | Next to the code, in `docs/internal/decisions/` |

They are a sequence, not a choice: **RFC to decide, ADR to record.** An accepted RFC often produces
one or more ADRs. If you only adopt one, use RFC-for-discussion and ADR-for-record.

## Pick a variant

- **Lean** (default): Summary, Motivation, Proposal, Alternatives Considered, Open Questions, Outcome.
  Enough for most changes worth an RFC at all.
- **Full**: adds Goals and Non-Goals, Detailed Design, Drawbacks and Trade-offs, and Rollout and
  Adoption. Use it when the change is hard to reverse, crosses teams, carries security/privacy/
  regulatory weight, or reasonable people will disagree.

Grow lean into full by adding sections; never reorder the shared ones. The scaling signal is the
**cost of being wrong**, not the size of the system.

## Quality rubric (self-grade before you circulate)

- [ ] The **summary contains the proposal**, not just the problem.
- [ ] The **motivation would survive a different solution winning.** It describes the problem, not a
      case for your favorite option.
- [ ] **Alternatives are real**, including "do nothing," and each is described well enough that a
      reader could prefer it. No straw men.
- [ ] The **open questions are genuinely open**, and they point reviewers at where their input
      matters. The section is not empty or "None."
- [ ] (Full) **Non-goals are stated**, so the discussion stays bounded.
- [ ] (Full) **At least one real drawback** of the proposal is named, one someone would act on.
- [ ] (Full) The **rollout has an owner, a sequence, and a backout.**
- [ ] There is a **named decider and a review-by date** (or, for lean, at least a clear owner).
- [ ] **Status is current**, and the **Outcome section is present** even while the RFC is open.
- [ ] The proposal is **concrete enough to disagree with.**
- [ ] Every guidance comment is deleted; no placeholders remain.

## Named anti-patterns (the usual wrecks)

1. **The RFC with no decider.** No approver, no deadline; the thread never closes. The default
   outcome is *nothing*.
2. **The rubber stamp.** Written after the decision; no live questions, decoy alternatives. Write an
   ADR instead.
3. **The comment pile-on.** Reviewers flood it, blocking and non-blocking feedback indistinguishable.
   Fix with named approvers and "yes, if."
4. **Writing to exhaustion.** Burying objections under volume until reviewers give up and approve.
5. **Template bloat.** Ten mandatory sections a small change cannot justify; people route around the
   process. Use lean.
6. **No alternatives.** The proposal cannot show it was reasoned; reviewers supply them adversarially.
7. **No recorded outcome.** Abandoned at `in-review`; nobody can later tell what was decided. Fill in
   Outcome and update status the moment it is decided.

## No paired skill (yet)

Unlike the ADR bundle, which pairs with the `develop-adr` skill, there is **no `develop-rfc` skill**
in the product-on-purpose org today, so this bundle's `pairs_with` is empty. That is a genuine gap:
the org has a skill for the *record* (ADR) but none for the *proposal* (RFC) that precedes it. Until
one exists, this template is filled by hand. The gap is noted as a finding in `STATE.md`.
