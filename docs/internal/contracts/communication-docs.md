# Family Contract: communication-docs

**Status:** **adopted 2026-08-05**, [ADR 0034](../decisions/0034-adopt-communication-docs-family-contract.md).
Registered in check K, which now gates `classification: utility` on every member.
**Axis:** `classification`, single value `utility`.
**Members:** `status-report`.

Written before its member is built, per the
[ADR 0020 (delivery-docs family contract)](../decisions/0020-adopt-delivery-docs-family-contract.md) pattern.

**This family has one Tier-1 member, and that is stated rather than hidden.** A one-member family is a legal
shape, and this contract exists for the same reason the others do: to bind the member that is coming and any
that follow. Section 1 names what would join it, so a future reader can tell whether the family was drawn
around a real category or around a single document that needed somewhere to live.

## 1. Membership

A bundle belongs to this family when its document type exists **to tell people who are not doing the work
what is happening with it.** Its audience is outside the team, its content is a summary of things recorded
elsewhere, and its value expires.

- a **status report** says where a piece of work stands, what changed, what is at risk, and what is needed
  from the reader.

**POSITION, not a claim about the field** (labelled 2026-08-07; see the change note). This library holds that the defining property is that **the document owns none of its own facts**. The `status-report` research searched for a named source stating it and found none: PMBOK's work-performance chain supports "compiled from elsewhere" and stops well short of a prohibition. The rule is kept because it is a good rule and because the failure it prevents is measured, not because the field defines the artifact this way. Every number in a status report is
read from somewhere with more authority: a KPI dashboard, a risk register, a roadmap, a backlog. That makes
its failure mode specific and different from every other family's: not being wrong, but being **stale, or
disagreeing with the source it summarises**. A status report that contradicts the dashboard is worse than no
status report, because someone will act on it.

A candidate that **owns** its facts belongs elsewhere: `governance-docs` for standing instruments,
`strategy-docs` for direction, `process-docs` for retrospective learning. A candidate written **for the team
doing the work** rather than for an audience outside it is not a communication document, it is a working one.

**Likely future members**, all Tier 2 and all grow-by-pull: `executive-briefing` / steering-committee pack,
a release announcement distinct from `release-notes`, a stakeholder update. If none is ever pulled, this
family stays at one member permanently, and that is an acceptable outcome rather than a defect.

## 2. Required catalog metadata and allowed values

| Field | Allowed values for this family |
|---|---|
| family | `communication-docs` |
| classification | **`utility`**, single value. A status report is maintained and periodic, and is valuable only while current; last month's is history. That is `utility`'s definition, and it is the same reasoning `governance-docs` used |
| methodology | **Descriptive, not gated** |
| sizes_available | `[lean, full]`, or `[lean]` where the type's research shows it does not earn a second weight |
| status | `beta` until one real usage cycle is recorded |
| pairs_with | pm-skills skill ID(s) or `[]`, resolving against `tools/known-skills.txt` |

**Why `classification` and not `phase`.** A status report is not the output of a lifecycle stage. It is
produced throughout, on a cadence, for as long as the work continues. It has no phase that is honestly its
own, and forcing one would misdescribe it. It is a standing periodic instrument, which is what the
`classification` axis exists for ([ADR 0015 (phase XOR classification)](../decisions/0015-second-taxonomy-axis-phase-xor-classification.md)).

## 3. Structural obligations (gate-checkable)

1. **The eight files**, prefixed `<type>_`.
2. **Nesting**, where two sizes exist: lean's H2s a strict ordered subset of full's, same names and order.
3. **Guidance comments.** Approach A in every section of every variant, with a "How to fill this in" preamble
   stating the N/A rule and the self-grade step.
4. **Companion skeleton.** All 11 sections of methodology section 5, one Anatomy subsection per template
   section.
5. **Guide shape.** When to use; when NOT to use; pick a variant; a rubric conforming to
   [`guide-rubric-spec.md`](../guide-rubric-spec.md); at least six named anti-patterns.
6. **Citations.** Methodology section 6 in full. **This family's specific citation hazard is that its
   literature is thin and vendor-dominated.** Status reporting is widely practised and rarely written about by
   named practitioners, so expect the honest finding to be that most guidance traces to project-management
   tooling vendors. Record that rather than dressing vendor content as practice.
7. **Example.** One fully worked instance, no placeholders, figures labeled, provenance stamped, and
   **independent of the template's own GOOD and WEAK text**. No member is grandfathered.

## 4. The no-new-facts rule (family-specific)

This family's members summarise; they do not originate. **Every figure in a member's example must be read
from an artifact that already exists in this library**, and the example must say where each one comes from.

That is a stricter version of the shared-scenario rule the other families carry, and it is stricter on
purpose, because it is the only way to demonstrate the type's real discipline. A status report example that
invents its own numbers is teaching the exact failure the document type has.

Concretely, the `status-report` example reports on the **Acme Analytics** thread and reads from the
`kpi-dashboard`, the `risk-register`, the `raid-log`, the `product-roadmap` and the `okrs` examples, all of
which already exist and already agree with each other. **A disagreement between the report and any of them is
a contract failure, not a rounding difference.**

**One further obligation.** The example must show **one thing going badly**, sourced from the existing thread,
which already contains suitable material: Time to Insight sitting at 18 percent against a 30 percent target
and reading amber. A status report example where everything is green teaches nothing, because the whole skill
of the type is saying a bad thing clearly to an audience that outranks you.

## 5. Shareable-boundary rule

Template body is the reusable shape; guidance lives only in comments; example content never leaks into
templates; meta describes the asset, never the filled instance. A guide that has grown explanatory or a
companion that has grown procedural is out of contract even if every file exists.

## 6. Enforcement

**Family check letter K** validates a `classification` of `utility`, a `beta`/`stable` status, a legal size
shape, and that this contract resolves; methodology is not gated. A member declaring `phase` fails with a
message naming the axis it should have used.

Of section 3, the eight files (3.1), nesting (3.2), citations (3.6) and the clean example (3.7) are enforced
by checks A, C, E and D, with example independence enforced by `tools/check-example-independence.py` and **no
member of this family eligible for its grandfather list**. Guidance comments (3.3), the companion skeleton
(3.4) and guide shape (3.5) are review obligations.

**Section 4 is a review obligation with no mechanical check, and it is the one most likely to need one.**
Cross-example numeric agreement is the kind of thing a script can verify, and if a member ever ships a figure
that disagrees with its source, that is the trigger to build the check rather than to re-state the rule
([`decision-procedures.md`](../decision-procedures.md) section 9).

## Change note

**0.1.1 (2026-08-07):** one claim relabelled after its first member was researched, per
[procedure 11](../decision-procedures.md#11-a-family-contract-asserts-something-about-the-world). No
obligation changed and `status-report` is not out of contract.

- **The no-new-facts rule is a POSITION, not a CLAIM.** Section 1 stated it as the artifact's defining
  property, which reads as a fact about the field. No source states it. It is this library's own rule and
  section 1 now says so.

**Research confirmation, 2026-08-07**, against `status-report`: the no-new-facts rule is UNSOURCED and now
labelled; the family's obligations are unaffected. Two findings from that research strengthen the contract
rather than weakening it, and are worth recording here because they are what the rule is *for*: across the
records of 56 experienced project managers, reports were biased 60 percent of the time and more than twice
as likely to be optimistic as pessimistic; and the most detailed published RAG scheme in circulation
explicitly declines to define its two intermediate colours. **The rule has no pedigree and a strong reason.**

### Earlier

**0.1.0

**0.1.0 (proposed 2026-07-30):** drafted, pending maintainer review. The ninth family contract and the fourth
on the `classification` axis. Drafted for a single Tier-1 member, with the category it belongs to named in
section 1 so the family's boundary is legible even while it holds one document.
