# Family Contract: standing-standards

**Status:** **adopted 2026-08-05**, [ADR 0032](../decisions/0032-adopt-standing-standards-family-contract.md).
Registered in check K, which now gates `classification: foundation or tool` on every member.
**Axis:** `classification`, **a set**: `foundation` or `tool`.
**Members:** `definition-of-done`, `runbook`.

Written before any member is built, per the
[ADR 0020 (delivery-docs family contract)](../decisions/0020-adopt-delivery-docs-family-contract.md) pattern.
This is the **second** family to gate a set rather than a single axis value, after `strategy-docs`.

## 1. Membership

A bundle belongs to this family when its document type is **agreed once and applied every time**. Not written
per increment, not revised on a calendar, not the output of a phase: written when the team decides how it will
work, and then consulted repeatedly without being rewritten.

- a **definition of done** is the standard every increment is judged against, so that "done" stops being an
  opinion;
- a **runbook** is the procedure executed when a known situation occurs, so that the response does not depend
  on who is awake.

The shared property is **standing applicability**. A definition of done written for one sprint is not a
definition of done; a runbook written for one incident is an incident report. Both are consulted far more
often than they are edited, and both fail the same way: by drifting out of date silently while everyone still
believes they are current.

A candidate written **once per unit of work** belongs to `delivery-docs` or `qa-docs`. A candidate **revised
on a cadence and valuable only while current** is `utility` and belongs to `governance-docs` or
`strategy-docs`. A candidate that is the **output of a phase** belongs to a `phase` family. This family is
neither periodic nor phase-bound, which is exactly why it needs the `classification` axis.

**Likely future members**, if pulled: `definition-of-ready`, a coding-standards or engineering-handbook
document, a release checklist. None is Tier 1, so none is scheduled;
[ADR 0021 (complete the Tier-1 floor)](../decisions/0021-complete-the-tier-1-floor.md) leaves Tier 2 and Tier
3 strictly grow-by-pull.

## 2. Required catalog metadata and allowed values

| Field | Allowed values for this family |
|---|---|
| family | `standing-standards` |
| classification | **`foundation` or `tool`** - the second family contract to allow a set on the axis key. `foundation` for `definition-of-done`; `tool` for `runbook`. See the axis note below |
| methodology | **Descriptive, not gated.** `definition-of-done` is agile-lineage; `runbook` is DevOps/SRE-lineage. Requiring one value would force one member to misdescribe itself |
| sizes_available | `[lean, full]`, or `[lean]` where the type's own research shows it does not earn a second weight |
| status | `beta` until one real usage cycle is recorded; then `stable` eligible |
| pairs_with | the pm-skills skill ID(s) this template serves, or `[]`; every value must resolve against `tools/known-skills.txt`. Verify per member; claim only what is true of that member |

**The axis call, and why this family needs a set.** Both members are standing, so both are
`classification`-axis rather than `phase`-axis. But they are not the same **kind** of standing artifact, and
collapsing them would misdescribe one:

- **`definition-of-done` is `foundation`.** It is a **standard you are judged against**. It is argued to,
  agreed by a team, and changed deliberately and rarely. Its authority comes from having been agreed; its
  failure mode is being agreed once and never honoured.
- **`runbook` is `tool`.** It is an **instrument you execute**, usually under time pressure and often by
  someone who did not write it. Its authority comes from being correct right now; its failure mode is being
  correct on the day it was written and wrong the day it is needed.

**The distinction that does the work: is it a standard you judge against, or an instrument you execute?** The
first is `foundation`, the second is `tool`. That is a different cut from `strategy-docs`' set, which split
`foundation` from `utility` on argued-and-durable versus maintained-and-periodic, and both cuts are legitimate
because the axis has more than two legal values.

**This cut is not invented here; it matches the vocabulary's source.**
[ADR 0015 (phase XOR classification)](../decisions/0015-second-taxonomy-axis-phase-xor-classification.md)
adopted these three values **because pm-skills uses them**, and pm-skills' own usage settles the question:
`classification: tool` was introduced there for the Sprint families, which are **defined procedures a team
runs**, while `foundation` covers artifacts other work rests on. A runbook is structurally the same kind of
object as a sprint: a procedure you execute. A definition of done is the same kind as a foundational
artifact: a thing other work is measured against. Aligning with the source vocabulary is what keeps the two
libraries able to describe each other.

**The functional coherence, stated so it can be falsified.** These two members share more than a cadence.
Both are **reference documents consulted at the moment of action, written by a team for its own future
self**: a definition of done is consulted when deciding whether work is finished, a runbook when deciding what
to do about a situation. Neither is authored per occasion, and neither is read for its own sake.

**That said, this family's coherence is thinner than `governance-docs`' or `strategy-docs`'**, both of which
group documents by a shared job rather than a shared rhythm. "Agreed once, applied every time" is closer to a
cadence than to a function. **The falsifier:** if a candidate arrives that matches the cadence but is not
consulted at the moment of action, this family has been drawn around the axis rather than around a job, and
it should split rather than absorb the candidate.

Check K has supported a set on the axis key since
[ADR 0023 (the Tier-1 family taxonomy)](../decisions/0023-resolve-the-tier-1-family-taxonomy.md), and
`strategy-docs` proved it live. This family is the second use, and the **first to combine `foundation` with
`tool`**, so `tools/test-check-k.py` gains a fixture asserting that combination before the first member lands.

**One consequence, stated plainly.** Check K can enforce that a member picks a value **from the set**, never
that it picked the **right** one. Nothing mechanical stops `runbook` declaring `foundation`. That assignment
is a review obligation, and the argued split above is the standard it is reviewed against.

## 3. Structural obligations (gate-checkable)

1. **The eight files**, filenames prefixed `<type>_`.
2. **Nesting.** Where two sizes exist, lean's H2 sections are a strict ordered subset of full's, same names,
   same order. Single-size members are exempt from nesting, not from anything else.
3. **Guidance comments.** Approach A in every section of every variant (WHAT, WHY with a companion pointer,
   ASK, GOOD, WEAK, TRAP; PRIORITY and ROW HINT for table sections), with a "How to fill this in" preamble
   that states the N/A rule and the self-grade step.
4. **Companion skeleton.** All 11 sections of methodology section 5, in order, one Anatomy subsection per
   template section.
5. **Guide shape.** When to use; when NOT to use; pick a variant; a self-gradable rubric conforming to
   [`guide-rubric-spec.md`](../guide-rubric-spec.md); at least six named anti-patterns.
6. **Citations.** Methodology section 6 in full. **This family's specific citation hazard is folklore
   presented as standard**: "definition of done" is Scrum-adjacent vocabulary whose actual definition in the
   Scrum Guide should be checked rather than assumed, and runbook practice is dominated by vendor content.
   Verify what the named source actually says.
7. **Example.** One fully worked instance, no placeholders, illustrative figures labeled, provenance stamped,
   and **independent of the template's own GOOD and WEAK text**. No member of this family is grandfathered.

## 4. The staleness obligation (family-specific)

Every other family's contract carries a shared-scenario rule. This one carries a different family-specific
obligation, because this family's members share a failure mode rather than a narrative position.

**Both members fail by going quietly out of date, and every member must ship the mechanism that surfaces
that.** Concretely, each member's template must carry a **review trigger** with a named owner and a condition,
not a calendar reminder: what event makes this document wrong, and who notices. A definition of done goes
stale when the team's practice changes without the document changing; a runbook goes stale when the system it
describes is redeployed.

This is the same discipline the repository applies to itself in finding **DF-3**, where the documents gated for
freshness stayed fresh and the ungated ones drifted. A standing document with no trigger is the ungated case.

**On the shared scenario:** members still chain onto the **Acme Analytics** thread where it is natural
(a definition of done that the `sprint-backlog` and `acceptance-criteria` examples could plausibly be judged
against; a runbook for the Saved Views service the `sdd` and `test-plan` examples describe). But the chaining
is weaker here by design, because a standing standard belongs to a team rather than to a moment in a story,
and forcing a narrative position on it would misrepresent the type.

## 5. Shareable-boundary rule

Template body is the reusable shape; guidance lives only in comments; example content never leaks into
templates; meta describes the asset, never the filled instance. A guide that has grown explanatory or a
companion that has grown procedural is out of contract even if every file exists.

## 6. Enforcement

**Family check letter K** validates section 2's values for every declared member (a `classification` of
**either** `foundation` or `tool`, a `beta`/`stable` status, and a legal size shape) and that this contract
resolves; methodology is descriptive and is not gated. A member declaring `phase` fails with a message naming
the axis it should have used; a member declaring `classification: utility` fails with a message listing the
allowed set, because the check reports the set rather than a single value.

Of section 3, the eight files (3.1), nesting (3.2), citations (3.6) and the clean example (3.7) are enforced
by checks A, C, E and D, with example independence enforced by `tools/check-example-independence.py` and **no
member of this family eligible for its grandfather list**. Guidance comments (3.3), the companion skeleton
(3.4) and guide shape (3.5) are review obligations. Section 4's review-trigger requirement is a review
obligation at authoring time; it is a section-presence rule and could later be gated if it recurs as a defect.

## Change note

**Research confirmation, 2026-08-07**, per
[procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world). This
contract was drafted on 2026-08-05 for a family with no built members, in the same batch as `process-docs`
and `communication-docs`. Its members were researched on 2026-08-06 and **its central claim held**.

The contract asserted that both members fail the same way, by drifting quietly out of date while everyone
still believes they are current, and that neither literature supplies a condition-based review trigger.
**Both halves were confirmed independently**: every Scrum source reached for the retrospective, every SRE
source reached for a cadence or a 90-day heuristic, and neither supplied a condition. Both members ship a
named Review Trigger section labelled as the bundle's own contribution rather than as received practice.

**This is recorded because a vindicated claim is worth as much as a refuted one.** Two of the three
contracts in that batch carried assertions no source supports; this one did not. Drafting a contract before
its members exist is therefore not automatically wrong, which is why procedure 11 governs the **mood** a
sentence is written in rather than the order contracts are written in.

### Earlier

**0.1.0 (proposed 2026-07-30):** drafted, pending maintainer review. The seventh family contract, the third on
the `classification` axis, and the **second to gate a set**, after `strategy-docs`. The membership was
ratified in principle by [ADR 0023 (the Tier-1 family taxonomy)](../decisions/0023-resolve-the-tier-1-family-taxonomy.md),
which moved `definition-of-done` out of `delivery-docs` (D-A) and `runbook` out of the dissolved `ops-docs`
(D-B) on the shared reasoning that both are *agreed once, applied every time*. This contract is where that
reasoning is argued against real members, as ADR 0023 required.
