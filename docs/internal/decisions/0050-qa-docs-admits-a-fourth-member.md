---
status: accepted
date: 2026-09-14
decision-makers: [jprisant]
consulted: [claude]
---

# `qa-docs` admits a fourth member, and the exclusion clause is what governs a candidate

## TL;DR

- **Decision:** the `qa-docs` family **admits a fourth member**, and `test-summary-report` is eligible to
  join it. The reading is stated here rather than assumed inside a build, because
  [ADR 0026](0026-adopt-qa-docs-family-contract.md) contains **no fourth-member clause** - unlike
  [ADR 0022](0022-adopt-decision-docs-family-contract.md), which admits a fourth `decision-docs` member in
  as many words - so nothing settled it.
- **Why:** the [contract](../contracts/qa-docs.md) contains two sentences about membership and **they do
  not say the same thing**. Its membership sentence describes the three planned members' roles and ends
  "*or reports a verification that **failed***". Its exclusion clause - the one that actually tests a
  candidate - reads "*A candidate type whose job is not to plan, specify, or **report the verification of a
  product increment** belongs in another family*", with **no failure qualifier**. A test summary report
  reports the verification of a product increment exactly.
- **What this does NOT decide:** whether `test-summary-report` passes
  [ADR 0030](0030-templating-scope-markdown-documents.md)'s admission test. That is a separate question,
  answered by research and not by contract reading, and it is **open at the time this record is written**.
  This ADR removes the family objection only.
- **Status:** accepted 2026-09-14.

## Context and Problem Statement

`qa-docs` was adopted **contract-first**, with zero members built, naming `test-plan`, `test-case` and
`bug-report` as its "planned members". All three shipped. `test-summary-report` is the first candidate to
arrive afterwards, and the contract answers the question twice, differently.

**The question is narrow and it matters beyond this type.** 174 catalog types remain candidates, and
several will arrive at a family whose adopting ADR never said whether the door was open. Deciding it
silently inside a build would set the precedent without anyone noticing - the same failure ADR 0048 exists
to avoid.

**There is a real argument for refusing**, and it should be stated at full strength rather than dismissed:
the contract says "The family's **three** roles are sequential rather than alternative, and that sequence
is its teaching value". Read strictly, "three roles" is a closed set, and a fourth member dilutes the
sequence the family exists to teach.

## Decision Drivers

* **An exclusion clause is what a candidate is tested against.** The contract's own sentence begins "A
  **candidate type** whose job is not..." - it is written to be applied to exactly this situation, and it
  is the broader of the two.
* **"Planned members" is not "only members".** The contract says "*Members at adoption: none built yet
  (test-plan, test-case, bug-report are the **planned** members)*". That is a statement about what was
  scheduled, not a closure.
* **The sequence extends rather than breaks.** Plan the verification, specify one unit of it, record one
  that failed, **report the verification as a whole**. A test summary report is the terminal step of the
  same sequence, not a fourth alternative to it.
* **The library already promises this document.** Four places in the shipped `test-plan` bundle send
  readers to a test report that does not exist. A family objection would leave that promise unkeepable.

## Considered Options

1. **Admit a fourth member on the exclusion clause** (this decision).
2. **Refuse**, reading "the family's three roles" as closed.
3. **Amend the contract** to name a fourth role explicitly, then admit.
4. **Move the type to a new family** of reporting artifacts.

## Decision Outcome

**Chosen: option 1.**

Option 2 gives the descriptive sentence priority over the operative one. The "three roles" phrase appears
in a passage **describing the three members the family had planned**, immediately followed by the three
bullets defining them; it reads as an inventory, not a cap. The exclusion clause is the sentence written to
adjudicate a candidate, and it is deliberately broader.

Option 3 is tempting and is rejected on the same ground ADR 0048 rejected raising the admission bar:
**changing a contract inside the record that applies it to one candidate makes the change
indistinguishable from the outcome it produces.** If the contract's two sentences should be reconciled,
that is an edit argued on its own, against the whole family. What this record does instead is state which
sentence governs and why, which is a reading rather than an amendment.

Option 4 invents a family to hold one type, and would separate a test report from the plan it reports
against - which is precisely the sequence `qa-docs` exists to teach.

### What this record does not do, and the distinction is the point

**It does not admit `test-summary-report` to the library.** It removes one of two objections.

- **The family question** - may `qa-docs` take a fourth member? - is a contract reading, answerable now,
  and answered here: **yes**.
- **The scope question** - does a named source publish a test summary report as a written document? - is
  [ADR 0030](0030-templating-scope-markdown-documents.md)'s test, answerable only by research, and **open
  when this is written**. The research is running.

**If that research comes back NOT ADMITTED, this record stands and the type still does not ship**, exactly
as `pi-release-retrospective` did not ship despite `process-docs` naming it by id as a likely member.
Family eligibility and scope admission are different gates, and passing one has never implied the other.

### The hazard already known about the scope question

`ISO/IEC/IEEE 29119-3` is the standard that defines test documentation and reportedly names a **Test
Completion Report**, which would be admission evidence of the strongest kind. **It is sold, not published**,
and this library's own `test-plan` research already recorded, in as many words, that "Nobody in this
research read 29119-3". Its predecessor IEEE 829-2008 is superseded **and** also sold, and second-hand
enumerations of its contents disagree with each other.

So a bundle here risks resting its section design on **second-hand descriptions of a superseded standard**,
which would be a rumour with a table. The build brief requires the structure to come from readable sources
and the standard to be cited **for existence, not for content**.

### Consequences

**Good.**

* The contract's two-sentence ambiguity is resolved in the open, once, rather than re-litigated by whoever
  builds next.
* A precedent generalises: **where a family contract's exclusion clause and its role inventory disagree,
  the exclusion clause governs a candidate.** That is worth more than this one admission.
* The `test-plan` bundle's four-fold promise of a test report becomes keepable.

**Bad, and stated plainly.**

* **This is a reading, and a careful person could read it the other way.** "The family's three roles" is
  real text and refusing on it would not be perverse. The record preserves that argument rather than
  burying it.
* **The family's teaching sequence gets longer**, and a four-step sequence is harder to hold than a three-
  step one. The fourth member's companion carries an added obligation to place itself against all three
  siblings *and* against acceptance criteria, which the contract already requires of every member.
* **ADR 0026 still has no fourth-member clause.** This record supplies the ruling without amending that
  ADR, so a future reader must find both. That cost is accepted for the reason option 3 was rejected.

### Confirmation

`test-summary-report`'s meta declares `family: qa-docs` and `phase: develop`, and gate check K validates it
against the contract like any other member. The contract's own text is unchanged by this record.
