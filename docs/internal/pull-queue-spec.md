# Spec: the pull queue, and what a pull is worth

Status: **spec, ready to execute.** Written 2026-08-14; **status corrected 2026-08-19**, because the one
decision this line said it was waiting on had already been taken when the line was written. Traces to roadmap WP-32 (demand capture), to [`plan.md`](plan.md) P7
(stand up the demand-gated roadmap), and to the 2026-07-10 audit's catalog recommendations section 5.4.

This exists because [ADR 0021 (complete the Tier-1 floor)](decisions/0021-complete-the-tier-1-floor.md)
demand-gates Tier 2 and Tier 3, and the Tier-1 floor is now complete. **The demand gate is therefore the
only gate left on new content, and it has no door in it.** Nothing in this repository records a request,
so no candidate outside the floor can legitimately be built, no matter how well argued.

> **Superseded the same day, marked 2026-08-19.**
> [ADR 0039 (maintainer discretion replaces the pull gate)](decisions/0039-maintainer-discretion-replaces-the-pull-gate.md)
> was accepted on 2026-08-14, the day this file was written, and it removes the premise the paragraph
> above rests on: **the maintainer may now build any Tier-2 or Tier-3 type at discretion with a recorded
> one-line rationale**, so the demand gate is no longer the only gate and no longer a stop. The paragraph
> is left standing rather than rewritten, because it was true when written and it is the argument ADR 0039
> answers.
>
> **What this changes in the spec, and what it does not.** Sections 1, 2, 3 and 5 are unaffected: intake,
> the field set, the queue page and the acceptance criteria all still describe work worth doing, and
> ADR 0039 explicitly retains the queue as an intake and as a priority signal. **Section 4 was the part
> that needed rewriting**, from a rule about what may be built into a rule about what gets built first.
> That rewrite was done 2026-08-21.
>
> **Superseded again 2026-08-22, and this time the decision changed rather than the wording.**
> [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md) closes **D5** and settles
> section 4: **the build order is set by the maintainer's own preference and need**, and external demand
> is an input rather than a rank. The 2026-08-21 rewrite is what exposed the reason: both ordering rules
> metered external pull, and **the queue has received zero issues since it shipped**, so the ranking
> input was empty and always had been. `pull-gated` becomes `candidate` throughout, and **D1 through D4
> and D6 are no longer sequenced behind a maintainer decision.** D4 shipped the same day.

---

## 1. What already exists, and what does not

Verified against the tree on 2026-08-14, because the roadmap's own M3 table calls this work "not started"
and that is wrong.

| Piece | State |
|---|---|
| **Intake forms** | **Built.** Three templates in `.github/ISSUE_TEMPLATE/`: `new-type.md`, `usage-report.md`, `correction.md`, shipped 2026-08-07 with the front-door documentation |
| **Structured fields** | **Not built.** All three are legacy `.md` templates, so every field is a prose prompt. Nothing is machine-readable |
| **Labels** | **Not built.** Each template declares a label in its frontmatter (`new-type`, `usage`, `correction`). **None of the three exists in the repository's label set**, which holds only GitHub's nine defaults |
| **Issues received** | **Zero**, open or closed |
| **The queue** | **Not built.** Nothing aggregates or orders requests. `docs/reference/pull-queue.md` does not exist |
| **Catalog state** | **Not built.** `atlas/catalog-data.json` carries `built: true/false` per type and no `state`. `state` and `resource_type` appear zero times in `tools/meta.schema.json` |
| **The demand rule** | **Not written.** No document in this repository says how many pulls move a type, what they move it to, or who decides |

**The correction worth recording:** this work has been described as unbuilt, both in the roadmap's M3
table and in the 2026-08-13 planning review. It is half built, and the half that exists is the half that
was hard to write. `new-type.md` states ADR 0030's admission test to a stranger in the stranger's own
terms, and names three real rejections (`wireframe`, `interactive-prototype`, `prototype-brief`) so the
test reads as a rule that has teeth rather than as a formality. Nothing below improves on that. Everything
below is mechanical by comparison.

## 2. What this is for, stated narrowly

A pull queue does three things and no more:

1. **Records a request without committing to it.** A recorded request is not a promise, and the queue must
   make that obvious to the person who filed it.
2. **Converts requests into a state a reader can see.** Today the catalog's 205 types are undifferentiated
   to an outside reader: 26 are built and 179 look like gaps. Most are decisions.
3. **Makes the refusal legible.** This is the VS-3 coverage discipline applied to the catalog surface. A
   type marked `pull-gated` with a reason is a stated position. A type with no marking is an omission.

**Non-goals, stated so they are not read in later:** this is not a backlog, not a prioritization system,
not a roadmap, and not a commitment device. A queued type is eligible, not scheduled.

## 3. Deliverables

### D1. Three labels (effort: S)

`new-type`, `usage`, `correction`. Until they exist, the three templates declare labels that cannot be
applied, so nothing can be filtered and no queue view is possible.

### D2. Convert the three templates to issue forms (effort: M)

`.md` to `.yml`, per the audit's section 5.4 field list. **Keep every word of the existing prose**; it
moves into `markdown` blocks unchanged. The prose is the part that works.

Fields the demand rule (section 4) actually consumes, and nothing else:

| Field | Type | Why the rule needs it |
|---|---|---|
| `catalog_ref` | input, free text | Which of the 205 types, or "not in catalog" |
| `requester_context` | input | Attribution. A pull must be attributable to someone |
| `document_written_today` | textarea, **required** | What they write instead, right now |
| `methodology_in_use` | dropdown | The Tier-2 active-practice test consumes this |
| `urgency` | dropdown | this-quarter / someday / just-signal |

**One deliberate deviation from the audit's 5.4 spec.** It calls for `requested_type` as a dropdown of all
205 catalog ids. Use a free-text input instead. A 205-option dropdown is hand-maintained YAML with no
generator behind it, which is finding DF-3 (gated documents stay fresh, ungated ones drift) written into
a new file on the day it is created. It also goes stale on every catalog edit and nothing would fail.
Free text is validated at triage by a human who is reading the issue anyway.

**`document_written_today` is required and the others are not.** A request from someone who writes no such
document today is a preference. A request from someone who writes one badly is a pull. That single field
is the difference, and it doubles as the LP-2 grade-my-doc lead the audit designed it to be.

### D3. `docs/reference/pull-queue.md` (effort: S)

**A rules page with live links, not a mirror of the issue list.** It states the demand rule, defines the
four states, and links three label-filtered issue searches.

**It must not be a committed copy of the queue**, and this is the load-bearing design call in this spec.
The source of truth is GitHub issues, which live outside the tree. A committed markdown mirror would be a
second hand-maintained copy of data that already exists elsewhere, which is precisely the defect
`gen-atlas.py` was written to close (two copies of `built`, generated by nothing, checked by nothing) and
precisely the defect the `check-readme-version.mjs` episode taught: **the honest fix for a rule that
already exists elsewhere is to run it, not to write a second copy.** A mirror would go stale silently on
every filed issue, and no check in this repository could see it.

### D4. The catalog `state` field (effort: M)

Extend `atlas/catalog-data.json` from `built: true/false` to a four-state enum, per the audit's 5.1:

```json
"state": "built | queued | candidate | out-of-scope",
"state_note": "one line: why, or what the pull was"
```

**BUILT 2026-08-22.** The vocabulary changed from the original `pull-gated` to **`candidate`** under
[ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md), because that name asserted a
demand gate ADR 0039 had already removed. What shipped:

- `built` is **derived** by `tools/gen-atlas.py` from the bundles on disk, exactly as `built` is.
- `out-of-scope` and `queued` come from [`atlas/state-overrides.json`](../../atlas/state-overrides.json),
  a small tracked file where **every entry carries a reason**. Seeded with the two decisions that already
  existed: `wireframe` and `interactive-prototype` (ADR 0030). **`prototype-brief` needs no entry**: ADR
  0035 rejected it as a *proposed* type, so it was never added to the catalog and has no row to label.
- `candidate` is the **default for everything else**, so the unbuilt types read as eligible-and-unranked
  rather than as gaps.

**Distribution at ship: 26 `built`, 177 `candidate`, 2 `out-of-scope`, across all 205 types.**

`built` is kept alongside `state` per the audit's backward-compatibility note. The atlas renders a chip and
a legend entry for the states that carry a decision; **`candidate` deliberately gets no chip**, because it
is the default and 177 of them would be noise on a map whose job is to show what is decided.

**Three guards, each mutation-tested rather than assumed:**

| Mutation | Result |
|---|---|
| Hide a bundle directory | `gen-atlas.py --check` **exits 1**, and that type's `state` flips `built` to `candidate`. This is section 5's acceptance criterion, and it proves the value is derived rather than hand-copied |
| Override names a type that has a bundle | **Fails**, naming the contradiction |
| Override names an id the catalog does not have | **Fails**, naming the id |

### D5. The demand-rule ADR (effort: M)

**DONE 2026-08-22** as [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md). Section 4
was the content, and it is now rewritten to match the record rather than proposing it. It stopped for the
maintainer under [`decision-procedures.md`](decision-procedures.md) because it amends how ADR 0021's gate
operates, and **the maintainer decided it: preference and need set the build order, not external demand.**

**It did not land as section 4 proposed.** The version that stopped for the maintainer ranked by external
pull. The record inverts that, on the ground that a ranking input which has never been non-zero cannot
rank. **This is the sequencing in section 7 paying off**: D5 was put first so the fields in D2 would not be
designed against a rule that had not been settled, and the rule that emerged is not the one D2 would have
been built for.

### D6. The dogfood entry (effort: S)

**Seed the queue with the one real pull that already happened**, recorded honestly: `adr` was built early
because this repository's own governance needed it, and the audit names that as the standing example of a
self-pull. Record it as `state: queued`, resolved, with a `state_note` saying it was the maintainer's own
need and not an external request.

An empty queue that has never held anything teaches a reader nothing about how the queue works. A queue
whose only entry is labelled a self-pull teaches them exactly what counts.

## 4. The build-order rule: maintainer preference, with demand as an input

**Settled 2026-08-22 by [ADR 0041](decisions/0041-maintainer-preference-sets-the-build-order.md), which is
deliverable D5.** This section is no longer an open question. It was proposed per the audit's 5.4, rewritten
2026-08-21 from permission wording into priority wording, and rewritten again here because that rewrite
exposed the real problem: **both ordering rules metered a currency the library has none of.**

**The order is set by the maintainer's own preference and need.** External requests are recorded, kept
visible, and may be weighed. **They do not rank the queue, and their absence blocks nothing.**

1. **A request is recorded and stays visible. It does not itself change rank.** Named means attributable:
   a person or a team, not an anonymous vote. The maintainer may weigh a request as evidence that a type
   is wanted, and is not obliged to.
2. **The maintainer's own preference and need are the ranking criterion.** Not one pull among others, which
   is what this rule said before ADR 0041 and which valued the only real input in the system at one unit of
   a currency whose total supply is one unit. Each build still carries a recorded one-line rationale, per
   ADR 0039. `adr` is the standing example: it was built early because this repository's governance needed
   it, and **that is now the normal case rather than a self-pull needing a disclaimer.**
3. **The catalog's active-practice test is a quality bar on the build, applied whenever a Tier-2
   methodology pack is built**, using the `methodology_in_use` field as the evidence. **It is no longer
   triggered by a request count.** Failing it changes what gets built and how it is scoped, never whether
   the type could be considered.
4. **Tier-3 regulated is blocked, and this is the one rule here that is still a permission rule.** It is
   blocked because that tier carries a currency discipline this library has not committed to: regulation
   text must be re-verified at authoring time and on a cadence forever. **Decision D4 (regulated-industry
   appetite) closed 2026-08-14 as a deliberate no** on that ground. **Neither ADR 0039 nor ADR 0041
   unblocks it**, because both govern how build order is chosen and this tier is closed on a maintenance
   obligation instead.

   > **One tension ADR 0041 creates and does not settle.** D4 states that Tier 3 "re-opens on a pull from a
   > real regulated team", and **a pull is exactly what ADR 0041 says does not govern the order.** The
   > reopening condition is now written in a currency this spec no longer ranks in. Restating it in
   > preference terms is open, and reopening Tier 3 is a scope decision of its own.

5. **A queued type is not a commitment, and a rank is not a schedule.** The queue page must say both in the
   requester's own reading path. **This rule became more load-bearing under ADR 0041, not less**, because
   the order is now openly one person's preference: a reader who mistakes it for a delivery plan is
   mistaking a preference for a promise. The library has one credibility asset, which is that it does not
   claim what it has not earned.

**The open question from the previous version is closed by the same record.** It asked whether an anonymous
or unattributed request counts as a pull, and recommended no. **Under ADR 0041 the question no longer
decides anything**, because no request, attributed or not, sets rank. Attribution still matters for a
different reason: an attributable request is someone the maintainer can go back to.

## 5. Acceptance criteria

- [ ] Three labels exist, and each template applies its own on a test issue.
- [ ] The three forms render as issue forms, and every field the demand rule consumes is a discrete field.
- [ ] `docs/reference/pull-queue.md` exists, states the rule and the four states, links three live
      filtered views, and is reachable from `README.md`, `CONTRIBUTING.md`, and
      `docs/reference/choosing-a-template.md`.
- [ ] `atlas/catalog-data.json` carries `state` for all 205 types, `gen-atlas.py --check` fails on drift,
      and the atlas renders a legend.
- [ ] The demand-rule ADR is accepted and the queue page cites it.
- [ ] **Mutation-checked, not assumed:** deleting a bundle directory makes `gen-atlas.py --check` exit
      non-zero on that type's `state`, proving the value is derived rather than hand-copied. This is the
      lesson from hand-editing `INDEX.md` and seeing the gate pass: a green run on a generated file is not
      evidence until it has been made to go red.
- [ ] The `adr` self-pull is recorded and labelled as a self-pull.

## 6. What this spec deliberately does not do

| Not in scope | Why | Where it lives instead |
|---|---|---|
| Mirroring issues into the tree | A second copy of data that lives elsewhere, ungated and silently staleable | D3 |
| A 205-option dropdown | Hand-maintained data with no generator, created stale | D2 |
| Prioritizing the queue | The queue records eligibility; sequencing is the roadmap's job | roadmap M6 |
| Amending ADR 0021 | The gate is fine. It has no door, which is a different problem | n/a |
| Creating demand | **This is the honest limit of this spec.** A door does not make anyone walk through it | roadmap WP-33, outreach |

## 7. Effort and sequencing

Roughly one focused day at the repository's normal standard, dominated by D4 and D5.

**Order: D5 (the ADR) first**, because the fields in D2 exist to feed the rule and should not be designed
before it. Then D1, D2, D3 together as one PR. Then D4, which touches the atlas and deserves its own PR
on the `gen-atlas.py` precedent. Then D6.

## 8. Risks, stated honestly

**The queue stays empty.** This is the most likely outcome and it is information rather than failure. An
empty queue after real outreach means the wedge is the problem, and the roadmap already says what to do
about that: fix outreach, do not soothe a stalled wedge by building more content.

**A door is not traffic.** Every deliverable here is cheap, and none of them creates demand. The item that
creates demand is WP-33 (wedge outreach), which is deliberately not in this spec and is not blocked by it.
Shipping this and then treating the empty queue as evidence that nobody wants the library would be the
wrong reading, and it is a reading worth pre-empting in writing.

**The state field can lie the way `built` did.** `built` drifted for weeks across two hand-maintained
copies. `queued` and `out-of-scope` are set by hand here by necessity, since no generator can know them,
so they carry that same risk and the mutation check in section 5 covers only the derived half. The
overrides file should be small, and every entry should carry an issue number or an ADR reference.
