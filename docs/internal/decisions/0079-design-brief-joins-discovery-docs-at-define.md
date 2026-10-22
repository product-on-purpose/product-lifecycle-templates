---
status: proposed
date: 2026-10-22
decision-makers: [jprisant]
consulted: [claude]
---

# `design-brief` joins `discovery-docs` as a fifth member, at `phase: define`

## TL;DR

- **Decision.** The catalog candidate `design-brief`, issue #294 (bundle: design-brief), is specced as the bundle
  **`design-brief`**. It declares **`family: discovery-docs`** and **`phase: define`**, in the Design Council's
  concept-handoff sense. The [contract](../contracts/discovery-docs.md) moves to `0.5.0`. It ships in two sizes,
  `[lean, full]`, by the maintainer's ruling of 2026-10-22.
- **Why an amendment, and how small.** The `0.4.0` contract already permits the brief's content, so section 2 does
  not change. Section 1's membership sentence gains one clause, which the maintainer chose. Section 1 also
  gains a member bullet, its cadence exception names the member, and section 4 gains an example bullet.
- **What this admits, and what it does not.** It admits the concept handoff: the chosen problem, the one concept
  chosen for design, and the handoff to the people who will design it. It does not admit Peter Phillips's
  commissioning agreement, Heap's solution brief or Figma's specification. It does not admit the Shape Up pitch,
  which stays out at medium-low confidence. The maintainer may reopen the pitch.
- **The evidence, and its limit.** The type clears
  [ADR 0048](0048-one-named-source-clears-the-admission-test.md) (one named source clears the admission test) on
  several named sources. No source models the narrow shape. The section set is the library's own composition,
  labelled a POSITION.
- **What this does not decide.** It sets no build order, under
  [ADR 0041](0041-maintainer-preference-sets-the-build-order.md) (maintainer preference sets the build order). It
  does not decide whether the opportunity statement joins the family.
  [ADR 0069](0069-problem-statement-joins-discovery-docs.md) (problem-statement joins discovery-docs) set a
  two-part condition for a define-pinned family. This record meets the first part and declines the route for now.
- **Status: proposed 2026-10-22.** This record amends a family contract, so it stops for the maintainer's read
  before any merge, under
  [decision-procedures.md](../decision-procedures.md#what-always-stops-for-the-maintainer). The maintainer ruled on
  the spec's ten choices on 2026-10-22, taking nine recommendations and choosing two sizes over one. The rulings
  close the spec section in [`tier2-specs.md`](../tier2-specs.md). They set the spec, and they are not the read.

## Context and Problem Statement

[ADR 0068](0068-define-means-problem-framing.md) (the define phase means problem framing) reserved `define` on
2026-10-10 for a document that names no solution. Three Define sweeps followed, one on 2026-10-11 and two on
2026-10-16. The second found the Design Council naming a design brief as the Define phase's output: "The result is
to create a design brief which clearly defines the challenge based on these insights." Issue #294 opened on that
finding.

**The third sweep recommended parking the candidate.** Its digest, dated 2026-10-16, found that the genre's main
book describes a brief that names a project and a design strategy. Such a brief failed ADR 0068's test. A narrow,
problem-only brief would have carried little that `problem-statement` does not.

**The rule then changed.** [ADR 0077](0077-define-ends-with-a-chosen-concept.md) (define ends with a chosen
concept) superseded ADR 0068 on 2026-10-17. A `define` document may now name one concept chosen for design, but
never a specification. The 2026-10-20 Define re-score returned the design brief for an admission sweep, in the
Design Council's sense, at medium confidence. It kept the Shape Up pitch out at medium-low confidence and asked the
sweep to resolve the collision between the two. The maintainer directed this sweep and a spec on 2026-10-22.

**This sweep ran two research dimensions.** D1 read software and product-team practice. D2 read the
concept-handoff line, the sizes and the boundaries. The main loop checked 53 returned web quotations against raw
page text. Fifty-one passed, and two stayed unverified and are not used. Five more quotations are this
repository's own text.

**What it found.**

- **The name splits.** Three technology sources use the name in three incompatible senses, and none is the Design
  Council's. Heap's goal is "to describe, holistically and at a high level, your proposed design solution(s)".
  Figma's design brief "builds on this foundation with specific technical and visual requirements". Y Combinator's
  mixes product context with how to engage a designer. D1 rates this high.
- **The concept handoff travels under other names.** Basecamp calls its version a pitch. Matej Kaninsky calls his
  written template a UX project brief. GitLab's public design handbook and Atlassian's template galleries carry no
  design-brief document at all. D1 rates this high.
- **No source models the narrow shape.** Every source that frames a design brief as a Define output adds content
  beyond problem framing. Every source that names a budget or a time line scopes it to the whole project. D2 rates
  this high.
- **No source splits a short brief from a long one.** Sources scale one brief by the size of the organization or
  the project. D2 rates this medium.

So the question this record answers is whether the Design Council's concept handoff earns a bundle beside
`problem-statement`, and how the family admits it.

## Decision Drivers

- **A phase value has to mean one thing.** This driver carries over from ADR 0077. A `define` document must sit on
  the concept side of ADR 0077's line: "A concept names the kind of answer the team will pursue. A specification
  says how that answer works or what it must do."
- **The admission bar does not move.** One named source must publish the type as a written document, under ADR 0048
  and [ADR 0030](0030-templating-scope-markdown-documents.md) (templating scope).
- **A new member must carry content no built member carries.**
  [ADR 0064](0064-deployment-plan-is-declined.md) (deployment-plan is declined) and
  [ADR 0065](0065-steering-committee-pack-is-declined.md) (steering-committee pack is declined) set that precedent.
- **A widening must be the smallest honest one.**
  [ADR 0076](0076-positioning-statement-joins-strategy-docs-as-a-sixth-member.md) (positioning-statement joins
  strategy-docs) applied that standard. It credits the standard to ADR 0060 (change-request joins delivery-docs).
- **A composed shape must say it is composed.** The defect this library's reviews find most often is a plausible
  specific claim that no logged source supports.

## Considered Options

1. **Amend `discovery-docs` and admit `design-brief` at `define`, in the Design Council's sense, in one size.**
   The spec recommended this, and the maintainer overruled it on sizes on 2026-10-22.
2. **The same, in two sizes.** The full size adds the handoff's scope, time line and budget, design constraints
   and open questions. The contract permits all three. The spec did not recommend it, and the maintainer chose it.
3. **A lean concept handoff and a full commissioning variant**, as the re-score suggested. Rejected. The full
   variant would carry Phillips's "written agreement, or contract, between the parties". The `define` rule bars that
   as the record that authorizes a project. One bundle carries one phase.
4. **Build the commissioning brief instead.** Rejected for this record. It is not a Define document, and this sweep
   tested no family for it. Sweep 3 named it a separate candidate with its own family question.
5. **A define-pinned family, with `problem-statement` moved into it.** This is ADR 0069's option 2. Its condition
   has two halves: a second problem-framing candidate clears admission, and the maintainer wants Define bundles on a
   shelf of their own. This candidate meets the first half. Rejected for now. The family would hold one built member
   and one spec, and the move would reopen a built bundle.
6. **Decline on duplication with `problem-statement`**, in the shape of ADR 0064 and ADR 0065. Rejected. The chosen
   concept and the handoff are content no built member carries.
7. **Park the candidate, as sweep 3 recommended.** Rejected. That recommendation tested ADR 0068's rule, which ADR
   0077 superseded the next day.
8. **Treat the Shape Up pitch as the same type, or as an alias.** Rejected. The pitch carries detail about how the
   concept works, and it exists to be bet on.

## Decision Outcome

**Chosen: option 2, by the maintainer's ruling of 2026-10-22.** The spec recommended option 1. The maintainer
chose two sizes on the ground ADR 0069 recorded for `problem-statement`, which also ships two sizes against its
sweep's lean-only finding. The contract amendment still stops for the maintainer's read.

### Why it fits

1. **Admission passes, with high confidence.** Jones and Askland, Phillips and Wikipedia each define the design
   brief as a written document. Heap and Y Combinator each publish a written template under that name. Jones and Askland write, "A written design brief will clearly
   articulate the product requirements to all parties involved in a project."
2. **The phase rule admits the content as written.** Section 2 permits "the one concept chosen for design". It also
   permits "the scope, time line and budget of handing that concept to the people who will design it". The brief decides no
   investment and authorizes no project.
3. **The content is distinct, at medium confidence.** `problem-statement`'s companion says, "This document names no
   solution". No built member names a concept chosen for design or a reader who will design from it.
4. **The cadence exception was written for this document.** ADR 0077 added it for a member revised while design
   work runs. Phillips calls the brief "a project-tracking tool", and that exception bounds the revision.

### The sizes

**Lean** carries The Challenge, Who It Is For and What We Learned, The Chosen Concept, and The Handoff. **Full**
adds Constraints on the Design, Open Questions for Design, and The Handoff's Scope, Time Line and Budget. The lean
sections nest inside the full variant in the same order, as section 3 requires. No source splits a short brief
from a long one, so the full-only sections are the library's construction. Each carries its source or the
POSITION label. The default is `lean`, as in `problem-statement` and `project-brief`.

### The membership sentence

Section 1 admits a type that exists to decide whether to build something, before anyone commits to building it. A
design brief carries a concept already chosen and hands it on. ADR 0077 left that sentence unchanged.

**Chosen by the maintainer on 2026-10-22, as recommended: add one clause**, so the sentence also admits a type
that decides which concept to design. Confidence: medium. The words keep the bound that nothing is yet committed to building. **The alternative** argues
that the sentence already fits, because design is not building. Confidence in that reading: medium-low. A
reviewer reading section 1 against this member would otherwise find a member the sentence does not describe.

### Where it sits in the chain

**A design brief follows the problem statement and precedes any document that specifies how the solution works or
what it must do.** That order is the library's POSITION, labelled so under
[procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world). ADR 0070
(north-star-metrics joins strategy-docs) and ADR 0076 labelled their own chain links the same way.

Two sources support part of it. Heap writes that "the team goes over both Problem and Design Brief with leadership
to get input." The Eleven Lessons report, quoted in ADR 0077, says "the Define stage would end with final sign-off
of the concept".

Noric Dilanchian says a design brief "comes early in a process which may lead to deal making, and then onwards
towards contracting". Dilanchian measures early against commissioning deals and contracts, so a brief may follow a
problem statement and a `discover`-phase project brief yet come early.

**The business case is left unordered.** None of this sweep's or sweep 3's research files orders the two. The
bundle fixes no order between them, at medium-low confidence.

### The line against the Shape Up pitch

**Two tests separate them, and both are the library's POSITION.**

1. **Altitude.** A design brief names its concept as the kind of answer. A pitch arrives shaped: Basecamp writes, "A
   problem without a solution is unshaped work." Its rabbit holes are "Details about the solution worth calling out
   to avoid problems", which is `develop` content.
2. **The act.** A design brief hands a concept to designers and does not itself commit the bet. A pitch exists for
   the bet: "The purpose of the pitch is to present a good potential bet." The betting table's decision commits a
   team's cycle.

**The exclusion stays at medium-low confidence.** Basecamp's no-gos are "Anything specifically excluded from the
concept", so Basecamp also calls shaped work a concept. The pitch's appetite also reads fairly as the handoff budget
the contract permits. The maintainer may reopen the pitch as its own `define` candidate.

### What widens, and by how much

- **Section 1's membership sentence** gains one clause, which the maintainer chose.
- **Section 1's member list** gains a fifth bullet for the design brief.
- **Section 1's cadence exception** names `design-brief` as the one member that takes it.
- **Section 4** gains the design brief's shared-scenario bullet.
- **The header's Members line** and the change note record the new member and version `0.5.0`.

The header's Axis line, section 2, section 3, section 5 and section 6 do not change. Check K does not change: it
already gates `["discover", "define"]`, and `[lean, full]` is already the default size shape. The exact text is in the
contract diff that accompanies this record.

### What the decision costs, stated rather than smoothed over

1. **The shape is the library's own composition.** No single source models a brief confined to a challenge, a
   chosen concept and a handoff. Every section must cite its source or carry the POSITION label.
2. **The name collides.** A technology reader may expect Heap's solution brief or Figma's specification. The
   companion must teach the senses, as ADR 0048 required `spike-report` to teach its dispute.
3. **The pitch line could fall.** A reader who weighs Basecamp's own word, concept, and the appetite-as-budget
   reading would admit the pitch beside this bundle.
4. **The membership sentence widens.** Every widening loosens a family's test a little. The added clause stays
   bounded by the existing words about committing to build.
5. **The phase order inverts again.** A `define` member may follow a `discover` member, the project brief. ADR 0069
   accepted the first inversion, and this record accepts a second.
6. **The family's thread changes direction.** The chosen example extends the delivery thread backward from its
   PRD, not the January discovery thread. The alternative example would be the family's first dated after the
   decision it relates to.
7. **The constraints section, kept in the full size, rests on an unread source.** Kuse and Heap mention
   constraints in general terms. The kinds of limit come from a page that returned HTTP 403.
8. **The unproven surface grows.** The library's efficacy runs found that documents written with these templates
   score no better than a strong generic-prompt control on decision-usefulness criteria. This bundle joins that
   surface.
9. **The full size rests on construction.** No source splits a short brief from a long one, and no source scopes
   a time line or a budget to the handoff alone. The full variant's three added sections are the library's
   composition, which the maintainer chose knowing that.

### Consequences

- **The contract moves to `0.5.0`.** Check K does not change.
- **The bundle id is `design-brief`, the same as the catalog id.**
- **The successor obligation binds the new member.** Section 1 requires its companion to name the document that
  takes over. That document is the PRD, once the designed concept is specified, and the choice is the library's
  POSITION.
- **The catalog gains entry 208 when the bundle lands**, as entry 206 arrived with `problem-statement`'s build.
  PR #305 (the opportunity statement becomes catalog entry 207) added entry 207 on 2026-10-22. Issue #294's body
  still names entry 207 and predates ADR 0077, and it is corrected on landing.
- **`project-brief` carries a dated note, not a rewrite.** Its guide, templates and companion route a design brief
  away, and the companion defines it in the commissioning sense. The note points to this bundle for the
  concept-handoff sense.
- **No other built bundle changes family or phase.** Existing members are not swept for a reciprocal mention, the
  precedent ADR 0076 recorded.
- **`pairs_with: []`.** No pm-skills skill addresses a design brief, checked against the local pm-skills checkout
  on 2026-10-22.
- **The bundle stays subject to ADR 0030.** This record removes the family objection only.
- **The amendment stops for the maintainer's read.** Nothing in this record or its contract diff merges before that
  read.

## More Information

- The family contract: [`discovery-docs`](../contracts/discovery-docs.md), adopted by
  [ADR 0031](0031-adopt-discovery-docs-family-contract.md) (adopt the discovery-docs family contract). ADR 0063
  (project-brief reopens discovery-docs), ADR 0069 and ADR 0077 amended it.
- The phase rule this record applies: [ADR 0077](0077-define-ends-with-a-chosen-concept.md).
- The written-form clarification: [ADR 0078](0078-maps-canvases-and-session-records-are-templatable-through-their-written-form.md)
  (maps, canvases and session records are templatable through their written form).
- The spec and the admission evidence: [`tier2-specs.md`](../tier2-specs.md), the `discovery-docs` (fifth member,
  at `define`) section.
- The research, in gitignored working files: `_local/research/2026-10-22_design-brief-spec/` (D1, D2 and the quote
  check), `_local/research/2026-10-16_define-sweep-3/digest.md` and `_local/research/2026-10-20_define-rescore/`.
