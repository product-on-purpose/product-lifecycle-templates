# Family Contract: process-docs

**Status:** **adopted 2026-08-05**, [ADR 0033](../decisions/0033-adopt-process-docs-family-contract.md).
Registered in check K, which now gates `phase: iterate` on every member.
**Axis:** `phase`, single value `iterate`.
**Members:** `sprint-retrospective-notes`, `incident-postmortem`.

Written before any member is built, per the
[ADR 0020 (delivery-docs family contract)](../decisions/0020-adopt-delivery-docs-family-contract.md) pattern.

## 1. Membership

A bundle belongs to this family when its document type exists **to look back at what happened and change what
happens next.** Its members are the two occasions a team does that:

- **sprint retrospective notes** look back on a **period**, on a cadence, at how the team worked;
- an **incident postmortem** looks back on an **event**, triggered by it, at why a specific thing failed.

The shared job is converting hindsight into a change someone owns. The shared failure is producing a document
that records feelings or timelines and commits nobody to anything, which is why every member of this family
must carry **owned actions with a place they are tracked**, not a list of observations.

A candidate that looks **forward** belongs elsewhere: `discovery-docs` before a decision, `strategy-docs` for
direction, `delivery-docs` for the work itself. A candidate that is **consulted repeatedly rather than
written per occasion** is a `standing-standards` member. This family is phase-bound: each instance is written
once, about one period or one event, and is then finished.

**The postmortem-versus-retro distinction is this family's central teaching point**, and
[ADR 0023 (the Tier-1 family taxonomy)](../decisions/0023-resolve-the-tier-1-family-taxonomy.md) put both here
specifically so it could be taught by contrast rather than asserted twice. Each member's companion must state,
in its Relationships section, what the **other** member is for and when a team is reaching for the wrong one.
The common real-world error is running a retro on an incident, which produces a blameless discussion of a
thing that needed a causal analysis, or running a postmortem on a sprint, which pathologises ordinary work.

**That last sentence is this library's own reasoning, not received practice** (corrected 2026-08-07; see the
change note). The research behind both members found named sources drawing the retro/postmortem line by
purpose and timing, but **none** framing the confusion of the two as a documented failure mode. It also found
live counterexamples worth carrying rather than filtering out: Honeycomb calls its incident process an
"incident retrospective", uses "retrospective" and "incident review" interchangeably, never uses
"postmortem", and declines even "blameless" in favour of "blame-aware"; FireHydrant, an incident-management
vendor, titles its material "Blameless Retrospectives" and splits *retrospective* into an incident-triggered
type and a post-project type. Naming practice in the wild is less settled than this contrast implies, and a
member may teach the distinction only as the library's own, never as consensus.

**Likely future members**, if pulled: `project-milestone-retrospective` and `pi-release-retrospective`, both
Tier 2 and both grow-by-pull.

## 2. Required catalog metadata and allowed values

| Field | Allowed values for this family |
|---|---|
| family | `process-docs` |
| phase | **`iterate`**, single value |
| methodology | **Descriptive, not gated.** The retro is Scrum/agile-lineage; the postmortem is SRE-lineage. Requiring one value would force one member to misdescribe itself, and this family is a clear case of the [ADR 0020](../decisions/0020-adopt-delivery-docs-family-contract.md) lesson |
| sizes_available | `[lean, full]`, or `[lean]` where the type's research shows it does not earn a second weight. **Expect pressure here**: retrospective notes are a strong candidate for single-size, and the catalog's size call is a hypothesis, not a fact |
| status | `beta` until one real usage cycle is recorded |
| pairs_with | pm-skills skill ID(s) or `[]`, resolving against `tools/known-skills.txt`. Verify per member |

## 3. Structural obligations (gate-checkable)

1. **The eight files**, prefixed `<type>_`.
2. **Nesting**, where two sizes exist: lean's H2s a strict ordered subset of full's, same names and order.
3. **Guidance comments.** Approach A in every section of every variant, with a "How to fill this in" preamble
   stating the N/A rule and the self-grade step.
4. **Companion skeleton.** All 11 sections of methodology section 5, one Anatomy subsection per template
   section.
5. **Guide shape.** When to use; when NOT to use; pick a variant; a rubric conforming to
   [`guide-rubric-spec.md`](../guide-rubric-spec.md); at least six named anti-patterns.
6. **Citations.** Methodology section 6 in full. **This family's specific citation hazard is attributed
   folklore.** "Blameless postmortem", the prime directive, the five whys and the sprint retrospective's own
   canonical shape all circulate detached from whoever actually wrote them, and at least one has a contested
   origin. Verify who said it before quoting it, and record the ones you could not trace.
7. **Example.** One fully worked instance, no placeholders, figures labeled, provenance stamped, and
   **independent of the template's own GOOD and WEAK text**. No member is grandfathered.

## 4. The shared-scenario rule (family-specific)

Members chain their examples on the library's existing **Acme Analytics** thread, and this family has an
unusually strong hook already waiting: the `bug-report` example documents **DEF-2291**, an aggregate computed
before the entitlement row filter, which disclosed the magnitude of hidden rows. That defect is exactly the
kind of thing a postmortem examines, and the `test-plan` example already records a suspension rule firing and
a triage disagreement left visible.

**The obligation:**

- the **incident postmortem** example analyses a real event from the existing thread rather than a new one,
  and its actions must land somewhere the library already models: the `risk-register`, the `raid-log`, or the
  `product-backlog`. **Of those three, only the `product-backlog` reflects published practice** (noted
  2026-08-07): two independent sources place postmortem actions in the team's ordinary ticket tracker and
  explicitly not in the postmortem document, and **neither names a risk register or a RAID log**. The menu is
  unchanged, because both remain artifacts this library models and a real programme does escalate a risk. A
  member using either must say that it is this library's convention rather than received postmortem practice;
- the **retrospective notes** example covers a sprint from the `sprint-backlog` example's own scenario, and
  must **not** be about the incident, because the two members exist to be contrasted and an example that
  blurs them teaches the opposite of the family's teaching point.

**One honesty obligation.** A postmortem example that ends with every action closed is a fiction. At least one
action must be open, owned, and dated, because the failure mode this document type actually has is actions
that are recorded and never done.

## 5. Shareable-boundary rule

Template body is the reusable shape; guidance lives only in comments; example content never leaks into
templates; meta describes the asset, never the filled instance. A guide that has grown explanatory or a
companion that has grown procedural is out of contract even if every file exists.

## 6. Enforcement

**Family check letter K** validates a `phase` of `iterate`, a `beta`/`stable` status, a legal size shape, and
that this contract resolves; methodology is not gated. A member declaring `classification` fails with a
message naming the axis it should have used.

Of section 3, the eight files (3.1), nesting (3.2), citations (3.6) and the clean example (3.7) are enforced
by checks A, C, E and D, with example independence enforced by `tools/check-example-independence.py` and **no
member of this family eligible for its grandfather list**. Guidance comments (3.3), the companion skeleton
(3.4) and guide shape (3.5) are review obligations. Section 4 and section 5 are review obligations at
authoring time and audit obligations thereafter.

## Change note

**Research confirmation, 2026-08-07**, per
[procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world), against `incident-postmortem` and `sprint-retrospective-notes`: of this contract's assertions about the world, **the retro-versus-postmortem harm claim is REFUTED** (no source states it, and named organisations do the opposite deliberately) and **the risk-register destination is UNSOURCED** (practice names only the ticket tracker). Obligations unaffected; both corrected below.

**0.1.1 (2026-08-07):** two claims corrected against the research that built both members, in the dated
in-place pattern this library uses for the catalog (finding EC-2) rather than by a superseding decision
record. Neither correction changes an obligation, and no member is out of contract.

- **The "common real-world error" framing in section 1 is this library's own reasoning.** No source read in
  full states it. Two named organisations do the opposite deliberately: Honeycomb runs what it calls an
  "incident retrospective" and prefers "blame-aware" to "blameless"; FireHydrant splits "retrospective" into
  incident-triggered and post-project types. Both are recorded in section 1.
- **Section 4's destination menu is unchanged, but published practice names only the ticket tracker.** The
  `product-backlog` option is the one practice describes; `risk-register` and `raid-log` are this library's
  own convention, and a member using them must say so.

Both corrections were already carried by `incident-postmortem` and `sprint-retrospective-notes` when they
landed (PR #75). This amendment closes the gap between what those bundles say and what this contract asserted,
which is the drift class the repository tracks: a governing document should not state as fact what the
documents it governs disclaim.

**0.1.0 (proposed 2026-07-30):** drafted, pending maintainer review. The eighth family contract and the fourth
on the `phase` axis. Both members arrive by
[ADR 0023 (the Tier-1 family taxonomy)](../decisions/0023-resolve-the-tier-1-family-taxonomy.md), which
dissolved `ops-docs` and moved `incident-postmortem` here to sit beside `sprint-retrospective-notes` so that
the postmortem-versus-retro distinction becomes a teaching point inside one family rather than a boundary
between two.
