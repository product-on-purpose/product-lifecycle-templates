---
status: accepted
date: 2026-09-13
decision-makers: [jprisant]
consulted: [claude]
---

# `pi-release-retrospective` fails ADR 0030's admission test and does not ship; `process-docs` grows to three

## TL;DR

- **Decision:** `pi-release-retrospective` **does not ship**. No named source publishes a PI or release
  retrospective as a written document. `process-docs` grows to three members - `sprint-retrospective-notes`,
  `incident-postmortem`, and `project-milestone-retrospective` - not four.
- **Why:** Scaled Agile's own Inspect and Adapt Facilitator's Guide, read in full and freely available,
  names the event's outputs as a predictability score, tacit understanding, and *"a set of improvement
  backlog items ... that go into the ART Backlog"*. **No document appears anywhere in it.** The only two
  vendor candidates are a **4-column board** - which ADR 0030 already refused for `wireframe` - and a
  template scoped to a single-team release rather than the multi-team event this type is defined as.
- **The structural finding, which is worth more than the refusal:** **cadence retrospectives feed a
  backlog; terminal retrospectives produce a document.** The Scrum Guide describes the Sprint
  Retrospective's output the same way SAFe describes I&A's, so this is the shape of the whole cadence line
  rather than a quirk of SAFe.
- **One research pass, two opposite verdicts, and that is the point.**
  `project-milestone-retrospective` was **admitted twice over** in the same pass - CALL's written
  after-action report and PMBOK's lessons learned register. The difference between the two types is
  principled, not accidental.
- **Status:** accepted 2026-09-13. Evidence:
  [`pi-release-retrospective-admission-evidence.md`](../pi-release-retrospective-admission-evidence.md).

## Context and Problem Statement

The two retrospectives were specified together on 2026-09-11 and researched together on 2026-09-12, in one
six-dimension pass, because they share almost their whole source base. The
[`process-docs` contract](../contracts/process-docs.md) names **both** by exact catalog id under "Likely
future members, if pulled", so the family question was settled before the research began and only ADR 0030's
admission test was open.

**It closed differently for each.**

## Decision Drivers

* **ADR 0030 asks whether a named source publishes the type as a written document**, and the answer here is
  no, from the framework's own primary material.
* **The refusal must bite symmetrically.** This library refused `wireframe` because its artifact is
  annotated inside a tool, and refused `prototype-brief` because every candidate turned out to be a
  neighbouring artifact under another name. Both failures recur here exactly.
* **A vendor source can suffice**, and was checked on that basis rather than dismissed.

## Considered Options

1. **Refuse, and ship only the project/milestone retrospective** (this decision).
2. **Admit on the Aha! board**, treating a 4-column board as a document.
3. **Admit on the EasyRetro template**, treating a single-team release retro as this type.
4. **Defer** pending readable SAFe content.

## Decision Outcome

**Chosen: option 1.**

Option 2 would require reading a board as a document, which **directly contradicts ADR 0030's own worked
refusal of `wireframe`** - excluded because designers annotate inside the design tool and no named source
publishes a written wireframe specification. Admitting a retrospective board while refusing a wireframe
would make the rule mean whatever the current candidate needs.

Option 3 substitutes a neighbouring artifact for the one under test. That is the `prototype-brief` failure
verbatim.

Option 4 defers on material behind a SAFe Studio login. The freely readable primary source - the vendor's
own facilitator guide - is unambiguous, and this library does not hold a decision open waiting for content
it cannot cite. If that gated material later turns out to prescribe a document, this record says plainly how
to reopen.

### The distinction this establishes, and it generalises

**Cadence retrospectives feed a backlog. Terminal retrospectives produce a document.**

- The **Scrum Guide** describes the Sprint Retrospective's output as changes that *"may even be added to the
  Sprint Backlog for the next Sprint"*.
- **SAFe** describes Inspect and Adapt's output as improvement backlog items for the ART Backlog.
- The **after-action review and lessons-learned lineage** attaches to work that has **ended** - where the
  team may disperse and part of the audience was not there - and **there** a named source does prescribe a
  written artifact.

That is why a type can be refused at PI scale and admitted at project scale without the rule wobbling. The
discriminator is not size or seniority; it is whether the work is **over**.

### Consequences

**Good.**

* The admission test bites symmetrically for the third time, and the refusal is grounded in the framework's
  own primary material rather than in an absence of searching.
* `project-milestone-retrospective` ships with its boundary **sourced** rather than asserted, because the
  refusal supplies the contrast.
* The research is preserved. A refused type normally costs its whole research pass; here the pass served a
  bundle that did ship.

**Bad, and stated plainly.**

* **Some SAFe content was not readable.** The deeper Inspect and Adapt body is behind a login and the
  decision was taken without it. That is a real limit, recorded rather than smoothed over.
* **A `future:` promise is not created but an expectation may be.** Readers who work in SAFe will look for
  this type and not find it. **The catalog entry stays `candidate` and carries no state override**, which is
  how `prototype-brief`'s refusal is handled and is also what the tooling permits: `gen-atlas.py` forces
  `state_note` to empty for any `candidate`, and the `out-of-scope` vocabulary is for a refusal about the
  **medium** - `wireframe` and `interactive-prototype` are not documents in any possible world. **This
  refusal is contingent, not categorical**: the artifact could exist tomorrow if someone publishes one, so
  marking it out-of-scope would overstate the finding and would need reversing on the first vendor template.
  The cost is that the refusal is discoverable only through this record and its evidence file, not from the
  catalog row. That is the same cost `prototype-brief` carries, accepted for the same reason.

### What this does not disturb

**`sprint-retrospective-notes` is not reopened.** It sits on the same cadence line and would face the same
structural finding, but it was admitted on its own vendor-tier evidence: three named vendors publish a
fill-in sprint retrospective **document** with fixed headings. Its research log already confronts the
tension directly, recording that *"The Scrum Guide does not ask you to write this down"* and calling that
*"the honest starting point for a bundle whose entire subject is a document."*

**That admission does not transfer**, and the reason is specific rather than convenient: no equivalent
document-shaped vendor template was found for a PI or release retrospective. The only candidate is a board.

## More Information

Three things would reopen this, in descending order of cheapness: **readable SAFe content** using the words
document, report or record for an I&A output, which a maintainer with a SAFe Studio login could check in
minutes; **a named source publishing a PI or release retrospective as a written document** with fixed
headings, vendor tier being sufficient on the `sprint-retrospective-notes` precedent provided it is a
document and not a board; or **a real pull from a team that writes one**, which would supply the artifact
as well as the demand.
