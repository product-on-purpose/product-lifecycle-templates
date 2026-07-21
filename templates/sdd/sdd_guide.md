# Guide: Software Design Document (operator card)

Fast reference for using the SDD bundle. For the full reasoning, history, and sources, read
[`sdd_companion.md`](sdd_companion.md).

## When to use

- You are about to build something **more than a one-file change**, and thinking the design through and
  getting it reviewed first would catch an expensive mistake on paper.
- The work is **hard to estimate or hard to deliver** without settling the design (a good default
  trigger).
- The design touches **more than one component or team**, and people who were not in the room need to
  reason about it.
- A choice in the design is **hard to reverse** (a data model, a public API, a persistence or auth
  decision) and worth a record.

## When NOT to use

- **You want feedback on whether to do this at all.** That is an [RFC](../rfc/rfc_guide.md): it proposes
  a decision and asks for input. (Many teams call this a design doc too; the distinction that matters is
  whether the primary output is a decision-before-building or a description of the implementation.) A
  design doc describes how you will build something.
- **You are recording a single, already-made, hard-to-reverse decision.** That is an
  [ADR](../adr/adr_guide.md). (A design doc may still spin one off; see below.)
- **The change is trivial or fully reversible.** A pull-request description is enough. A design doc for a
  one-line change is process for its own sake.
- **The design is genuinely unknowable until you build it**, and a spike would teach you more than a
  document. Prototype first, then write the doc if the design still warrants review.

## Design doc, or RFC, or ADR? (the question people actually have)

| | **Design doc / SDD** | **RFC** | **ADR** |
|---|---|---|---|
| Answers | "How will we build it?" | "Should we, and which way?" | "What did we decide, and why?" |
| Timing | Before/while building | Before the decision | After the decision |
| Describes | An implementation | A proposal | A decision |
| State | Living, then archived | Mutable while open | Immutable once accepted |
| Scope | The whole design | One proposed change | One decision |

They are a division of labor, not a competition. Much of the industry uses **"design doc" and "RFC"
interchangeably**, which is fine when one document does both jobs; the moment feedback on the *decision*
is the point, it is an RFC. The **ADR is genuinely distinct**: when your design makes a significant,
hard-to-reverse choice, record that decision *also* as an ADR, so the next person finds it next to the
code rather than buried in a design doc.

## Pick a variant

- **Lean** (default): Context and Scope, Goals and Non-Goals, The Design, Alternatives Considered,
  Cross-Cutting Concerns. This is the Google-style "mini design doc," enough for most changes worth a
  design doc at all (roughly one to three pages).
- **Full**: breaks The Design into Static Structure, Runtime and Data Flow, Interfaces and Contracts, and
  Deployment and Operations, and adds Quality Attributes and Risks and Open Issues. Use it when the design
  is hard to reverse, crosses teams, carries security/privacy/regulatory weight, or has real
  non-functional targets.

Grow lean into full by adding sections; never reorder the shared ones. The scaling signal is the **cost
of being wrong**, not the size of the system.

## Quality rubric (self-grade before you circulate)

- [ ] The **scope has a boundary**: the doc says what is in and, explicitly, what is out.
- [ ] **Goals are outcomes, not a build list**, and there is **at least one non-goal**.
- [ ] The **design is concrete enough to disagree with**, and a diagram carries the structure where prose
      would be worse.
- [ ] **Alternatives are real**, including "do nothing" or the obvious approach, each described well
      enough that a reader could prefer it. No straw men.
- [ ] **Cross-cutting concerns are walked explicitly** (auth, privacy, observability, failure, cost), not
      waved off as "standard."
- [ ] (Full) **Quality attributes have numbers or scenarios**, not adjectives.
- [ ] (Full) **Risks and open issues are named**, and any hard-to-reverse decision is flagged for an ADR.
- [ ] You know **which of design-doc / RFC / ADR you are writing**, and this is the right one.
- [ ] **Status is current**, and there is a plan for the doc after shipping (archive, or mark last
      verified).
- [ ] Every guidance comment is deleted; no placeholders remain.

## Named anti-patterns (the usual wrecks)

1. **Conflating design doc, RFC, and ADR.** Writing a "design doc" that is really an undecided proposal
   (an RFC), or burying a significant hard-to-reverse decision inside a design doc instead of recording it
   as an ADR where it can be found. Know which of the three you are writing.
2. **Big design up front.** A complete, detailed design produced before any code and treated as fixed. It
   commits you before you have learned the most, and produces a design the implementation quietly
   abandons. Write "just enough" design; reach for the full variant only when the cost of being wrong
   earns it.
3. **The stale living doc.** A design doc kept as the system's description long after the code diverged.
   A half-correct document everyone trusts is worse than an obviously archived one. Archive it after
   shipping, or mark when it was last verified against reality.
4. **Writing to exhaustion.** Using length and exhaustive detail as a substitute for clear thinking, so
   the design is approved because no reviewer could finish it. Detail the risky parts; compress the
   obvious ones.
5. **No alternatives.** A design presented as the only option cannot show it was reasoned; reviewers
   supply the missing options adversarially.
6. **Wishes instead of targets.** Quality attributes stated as adjectives ("fast," "scalable") with no
   number or scenario, so nothing in the design can be checked against them.

## No paired skill (yet)

There is **no `develop-sdd` skill** in the product-on-purpose org today, so this bundle's `pairs_with` is
empty. The org has a skill for the decision *record* (`develop-adr`) but none for the design document.
Until one exists, this template is filled by hand. Recorded as context in `STATE.md`.
