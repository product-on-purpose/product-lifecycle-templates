---
status: accepted
date: 2026-09-12
decision-makers: [jprisant]
consulted: [claude]
---

# One named source clears ADR 0030's admission test, and `spike-report` is admitted on that reading

## TL;DR

- **Decision:** **`spike-report` is admitted** and may be built. The reading that admits it is stated here
  deliberately rather than set by accident: [ADR 0030](0030-templating-scope-markdown-documents.md) says "a
  named source publishes it as a written document", **singular**, and one qualifying named source is
  therefore sufficient.
- **The evidence, which is thinner than any previous admission.** Exactly **one** source qualifies:
  Microsoft's Code with Engineering Playbook, which states the deliverable "should be a document" and ships
  a fill-in template. **The term's own inventors publish the opposite** - Ward Cunningham's c2 account,
  crediting Kent Beck, describes the output as throwaway **code**. Full record:
  [`spike-report-admission-evidence.md`](../spike-report-admission-evidence.md), 72 sources, 61
  fetched-and-verified.
- **What this does NOT do:** it does not weaken the test, and it does not reopen
  [`prototype-brief`](0035-prototype-brief-fails-the-admission-test.md), which failed with **zero**
  qualifying sources. One and zero are different numbers, and that is the whole distinction.
- **The obligation this creates:** the bundle must **teach the dispute rather than resolve it**. A spike
  report bundle that presents the written artifact as settled practice would be making a claim this
  evidence does not support.
- **Status:** accepted 2026-09-12.

## Context and Problem Statement

ADR 0030 admits a candidate document type when **a named source publishes it as a written document**. That
test has bite: it rejected `wireframe` and `interactive-prototype` on scope, and on 2026-08-05 it rejected
`prototype-brief` after a full six-dimension research pass, closing `discovery-docs` at two members.

`spike-report` was specified on 2026-09-11 and its research ran the same day. The verdict was not the clean
pass the build order had assumed, and it was not the clean failure `prototype-brief` produced. It was one
source.

**The question this record answers is not really about spikes.** It is: *does ADR 0030 require one
qualifying source, or a preponderance?* The text says one. Nothing had ever tested that, because every
previous admission had several and the one rejection had none. `spike-report` is the first candidate to land
in the gap, and answering it silently by building the bundle would have set the precedent without anyone
noticing it had been set.

## Decision Drivers

* **The rule says what it says.** "A named source" is singular. Reading it as "several named sources" is a
  different, stricter rule, and adopting a stricter rule by inference is how a test stops being checkable.
* **The evidence is verifiable and current**, not a plausible memory. The Microsoft template was read from
  the raw markdown in its repository, not from a rendered page that might be stale.
* **The artifact demonstrably exists in practice.** The research read **14 real, filled spike reports**,
  fetched as raw bytes and verified line by line. Whatever the canon prescribes, people write these.
* **The precedent matters more than the bundle.** 176 catalog types remain candidates. Several will land in
  the same gap.

## Considered Options

1. **Admit on one named source** (this decision).
2. **Refuse**, on the ground that the origin contradicts the single supporting source.
3. **Raise the bar to two or more sources**, and refuse `spike-report` under the new bar.
4. **Defer** until a second source is found.

## Decision Outcome

**Chosen: option 1.**

Option 2 gives the origin a veto the test does not grant it. ADR 0030 asks whether *a named source publishes
the document*, not whether the practice's inventors approve of publishing it. A test that additionally
required the canon's blessing would reject documents that demonstrably exist, which is the opposite failure
from the one it was written to prevent.

Option 3 is a real alternative and is rejected on timing, not on merit. Raising the bar in the record that
applies it to a specific candidate makes the rule change indistinguishable from the outcome it produces. If
the bar should be higher, that is a change to ADR 0030 argued on its own, against the whole catalog, not
introduced underneath one type.

Option 4 defers indefinitely on evidence that a 72-source pass already failed to find.

### What this does not disturb

**`prototype-brief` stays refused, and this record strengthens rather than weakens ADR 0035.** That type
failed with **zero** qualifying sources: every candidate examined turned out to be a neighbouring artifact
under another name. The distinction between zero and one is exactly the distinction ADR 0030 draws, so
applying it consistently produces opposite answers for the two types. **If this record had admitted
`spike-report` on a preponderance-of-practice argument, it would have reopened `prototype-brief`**, because
prototyping practice is at least as widespread. It does not, and that is deliberate.

### Consequences

**Good.**

* The test stays checkable: a future candidate needs one qualifying named source, and "how many is enough"
  is no longer an open question answered differently by whoever is building.
* `decision-docs` gains a fourth member with no contract change, exactly as
  [ADR 0022](0022-adopt-decision-docs-family-contract.md) anticipated.
* The `future:spike-report` tag in `templates/adr/adr_meta.yaml` stops being a promise and becomes a
  reference.

**Bad, and stated plainly.**

* **This is the thinnest admission this library has granted.** One source, against the canon. A reader who
  finds that unconvincing is not misreading the evidence.
* **It lowers the observed floor.** Every previously admitted type had more. Nothing stops a future
  candidate clearing the bar on one vendor-adjacent page, and the only guard is that the source must be
  genuinely named and genuinely publish the document.
* **The bundle inherits an obligation that no other bundle carries**, below.

### The obligation this creates for the bundle

**The `spike-report` bundle must teach the dispute, not resolve it.** Its companion must record that the XP
canon describes a spike's output as throwaway code, that the most-cited living practitioner describes an
activity rather than a document, and that the written artifact is a later enterprise formalisation. Its
research log carries the contested register.

A bundle that presented "write up your spike" as settled practice would be **making a claim this evidence
does not support**, in a library whose entire credibility rests on not doing that. The dispute is not a
weakness in the bundle; it is one of the more interesting things the bundle has to teach.

## More Information

The section design also changes on this research, and the changes are recorded in
[`tier2-specs.md`](../tier2-specs.md): the blinded gap dimension **defended** the proposed "What This Does
Not Settle" section - an explicit non-scope statement is the single most consistent element real filled
spike reports supply and a naive four-part shape omits - while the structure dimension **weakened** the
proposed "Time Box" section, which belongs to pre-spike planning artifacts rather than to the report of a
completed spike.
