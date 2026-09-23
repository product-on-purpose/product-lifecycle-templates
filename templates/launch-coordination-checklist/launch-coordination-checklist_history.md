# launch-coordination-checklist: history

Change log for the `launch-coordination-checklist` bundle. Each entry records what changed and why, so a
reader can tell a correction from a preference.

## 0.1.0 - 2026-09-22

**Initial release.** Researched 2026-09-22 across six dimensions: origins and admission, structure,
methodology lineage, debates and status, relationships and tooling, and the standing-versus-per-launch
question; drafted and reviewed the same day.
[`launch-coordination-checklist_research-log.md`](launch-coordination-checklist_research-log.md) records
46 source records merged to **39 unique sources, all 39 fetched-and-verified**. No source is quarantined
as not-retrieved, so nothing in this bundle rests on an unverified figure.

**The third `standing-standards` member**, alongside `definition-of-done` and `runbook`, in the family
[ADR 0053](../../docs/internal/decisions/0053-launch-coordination-checklist-joins-standing-standards-as-a-tool.md)
assigned this type to. It carries `classification: tool`, an instrument consulted at the moment of a
launch decision, against `definition-of-done`'s `foundation` and alongside `runbook`'s own `tool`
placement.

### The admission source is licensed, so the load-bearing section is not an adaptation of it

The type's admission source, Appendix E of Google's *Site Reliability Engineering*, is a full published
checklist under the type's own catalog name, "Launch Coordination Checklist," circa 2005. It is licensed
CC BY-NC-ND 4.0, no derivatives, so this bundle's Readiness Checks section is built from categories found
across several other structural sources rather than as a restyling of Google's own list. The shape of a
good check, question paired with action and a response that states actual status rather than a bare
"done," is sourced directly from Google's own practice and from aviation checklist design literature, both
cited for design discipline rather than as software-launch evidence.

### A per-check owner and evidence field is the exception, and the design says so

Of the structural precedent read, GitLab's issue template and a filled instance of it, a government
open-source checklist, and a personal practitioner checklist all carry no owner, pass-condition, or
evidence field on individual items. Only one source, a launch-day go/no-go framework, carries an
owner-equivalent decision role and an explicit evidence field together. This bundle's per-check design
follows that source and Google's own question-plus-action unit, not a count of how many published
templates already do it this way, and the companion says so rather than implying the design is the norm.

### Rollout and Rollback is promoted into lean

The build spec's provisional shape was not re-derived section by section against the research; Rollout
and Rollback earned a place in the lean variant on direct evidence that it is the element a naive
checklist most reliably omits. Google's own practice treats staged rollout and a pre-decided reversal as
the default rather than the exception, and a real deployment failure (Knight Capital, 2012) shows what an
undeclared rollback trigger costs in practice: the incident's own emergency response made the outage worse
because there was no kill switch.

### Review Trigger is the bundle's own contribution, and the disagreement beneath it is stated rather than resolved

No structural source read publishes a section with this name or job; it is required directly by the
`standing-standards` family contract, the same way `runbook`'s Review Trigger section is. The two most
direct sources on what an incident should do to a checklist disagree: Google's own guideline invites
justifying a new item by a past disaster, while a practitioner account of production-readiness-review
practice warns explicitly against a naive per-incident append loop. The section is built to ask a narrower
question, which mechanism failed, rather than pick a side neither source settles.

### `pairs_with` is declared, verified against the pm-skills repo the same day this bundle was specced

`deliver-launch-checklist` was added to `tools/known-skills.txt` on 2026-09-22, before this bundle was
built, with the pairing's honesty left open as the spec's question: the skill writes a checklist per
launch, while the family admits this type as a standing instrument, so the pairing holds only if the
per-launch document is what the skill's template is made from. The research confirmed that reading: the
skill's own template names Go/No-Go Criteria and a Rollback Plan as per-launch content, exactly what this
bundle's standing checklist supplies.

### The honest core

**Google's checklist is a historical artifact of one company's mid-2000s infrastructure, not a current
external standard**, and the companion presents it that way rather than as present practice. No source
read asserts that checklists save lives or reduce failures by any measured figure, that Google's checklist
carries a sign-off gate, that production readiness review replaced the launch checklist, or that an
Operational Readiness Review meeting feeds a go or no-go decision; that last claim was seen only in a
search snippet, not in the fetched source, and is excluded rather than carried as fact. *The Checklist
Manifesto* was not read for this bundle and nothing here quotes it.

### Verified before drafting

Every quotation the research agents returned was checked against each source's raw text rather than
against a retrieval tool's summary of it. 19 of 193 quotations returned were not found in their sources and
were removed, including an invented specific inside quotation marks, a quotation attributed to a file that
does not contain it, a checklist field that does not exist in its source, and paraphrase presented as
verbatim. None of the four survives anywhere in this bundle.
