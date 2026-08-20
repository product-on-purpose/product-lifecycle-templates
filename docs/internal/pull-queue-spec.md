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
> ADR 0039 explicitly retains the queue as an intake and as a priority signal. **Section 4 is the part
> that needs rewriting**, from a rule about what may be built into a rule about what gets built first.
> That rewrite is WP-32 build work, not a decision, and it has not been done.

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
"state": "built | queued | pull-gated | out-of-scope",
"state_note": "one line: why, or what the pull was"
```

- `built` is **derived** by `tools/gen-atlas.py` from the bundles on disk, exactly as `built` is today.
- `out-of-scope` is derived from a small tracked overrides file, seeded from the decisions that already
  exist: `wireframe` and `interactive-prototype` (ADR 0030), `prototype-brief`
  ([ADR 0035](decisions/0035-prototype-brief-fails-the-admission-test.md)).
- `queued` is set by the maintainer at triage, in the same overrides file, with the issue number as its
  `state_note`.
- `pull-gated` is the **default for everything else**, so the 179 unbuilt types stop reading as gaps.

Keep `built` alongside `state` for one release, per the audit's backward-compatibility note.
`gen-atlas.py --check` already fails CI on drift and extends to cover this. The atlas renders a legend.

### D5. The demand-rule ADR (effort: M)

Section 4 is the content. It stops for the maintainer under
[`decision-procedures.md`](decision-procedures.md) because it amends how ADR 0021's gate operates.

### D6. The dogfood entry (effort: S)

**Seed the queue with the one real pull that already happened**, recorded honestly: `adr` was built early
because this repository's own governance needed it, and the audit names that as the standing example of a
self-pull. Record it as `state: queued`, resolved, with a `state_note` saying it was the maintainer's own
need and not an external request.

An empty queue that has never held anything teaches a reader nothing about how the queue works. A queue
whose only entry is labelled a self-pull teaches them exactly what counts.

## 4. The demand rule, which now sets priority rather than permission

Proposed, per the audit's 5.4, with one addition. **Read every rule below as a priority rule**: since
[ADR 0039](decisions/0039-maintainer-discretion-replaces-the-pull-gate.md) none of them decides whether a
type may be built, only where it sits in the order. The rules are left in their original permission
wording, and rewriting them is the open WP-32 task named at the top of this file.

1. **One named requester moves a type from `pull-gated` to `queued`.** Named means attributable: a person
   or a team, not an anonymous vote.
2. **The maintainer's own governance need counts as one pull**, and is recorded as a self-pull rather than
   disguised as external demand. `adr` is the standing example.
3. **Three or more requests for a Tier-2 methodology pack** trigger the catalog's active-practice test
   before any build, using the `methodology_in_use` field as the evidence.
4. **Tier-3 regulated stays blocked on decision D4 (regulated-industry appetite)** regardless of pull
   count, because that tier carries a currency discipline this library has not committed to. **D4 closed
   2026-08-14 as a deliberate no**, on that same currency burden, and it reopens only on a pull from a
   real regulated team, so this rule now states a settled position rather than a pending one. ADR 0039
   does not unblock it: discretion governs which types get built, and this tier is closed on a separate
   ground.
5. **Added here, not in the audit: a queued type is not a commitment**, and the queue page must say so in
   the requester's own reading path. The library has one credibility asset, which is that it does not
   claim what it has not earned. A queue that reads as a promise spends that asset.

**The one open question, recommended answer included.** Does an anonymous or unattributed request count as
a pull? **Recommended: no.** The entire purpose of the gate is evidence that someone will use the thing.
An unattributable request is evidence that someone finds the idea appealing, which is what grow-by-pull
exists to filter out.

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
