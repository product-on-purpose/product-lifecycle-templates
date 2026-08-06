# runbook: history

Change log for the `runbook` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-08-06

**Initial release.** Researched 2026-08-06 across six parallel dimensions: the SRE canon, structure in
practice, the automation boundary, failure modes, ownership and staleness, and boundaries against adjacent
documents; drafted and reviewed the same day.
[`runbook_research-log.md`](runbook_research-log.md) records **31 sources**, of which **28** were fetched
and verified and **3** could not be retrieved. Of the 28 read, 12 are primary, 10 vendor and 6 practitioner.

**The second `standing-standards` member**, alongside `definition-of-done`, in the family adopted by
[ADR 0032 (the standing-standards family contract)](../../docs/internal/decisions/0032-adopt-standing-standards-family-contract.md).
The contract's own split places this bundle as `classification: tool`, an instrument you execute, against
`definition-of-done`'s `foundation`, a standard you are judged against.

### One format ships, and a bigger artifact is taught rather than templated

Under [ADR 0028 (the format-axis rule)](../../docs/internal/decisions/0028-adopt-a-format-axis.md) a format
ships only when it is structurally distinct **and** in circulation with a named source. The research found
two genuinely distinct shapes in circulation: an **incident-scoped procedure** (Emmer's six sections, four
naming Microsoft components) and a **standing service-operations manual** (PagerDuty's seven sections,
Skelton Thatcher's sixty-five headers, covering an entire service's overview, deployment, security and
disaster recovery). Both are real; only the first is what the family contract defines a runbook to be, so
the second is rejected as a format and taught as a boundary in the companion's Relationships section
instead of shipped as a third size. Two further candidates were checked and rejected: "playbook" as a
distinct document (the canon this bundle traces to uses the two words for the same object and never
contrasts them) and an "automated runbook" (the artifact there is code, not a document, out of scope on the
same reasoning that excluded `interactive-prototype` under
[ADR 0030](../../docs/internal/decisions/0030-templating-scope-markdown-documents.md)). **No `default_format`
key is declared**, joining the bundles that carry no format key rather than pre-empting decision D-E.

### The section design departs from the provisional spec, on evidence

Four departures, the last two corrections to a pairing no published template supports:

- **The alert trigger moved into `lean`.** The build spec treated it as a full-only addition; the sources
  put it in the core (PagerDuty builds its format around the paging alert, Atlassian's ITSM template lists
  the alerts it produces, and the SRE Workbook states that a playbook entry is usually created alongside
  each alert). A runbook with no stated trigger cannot be told apart from a wiki page about the service.
- **Prerequisites and Access moved out of `lean`.** It is named as its own section in exactly one source
  read; everywhere else it is folded into the first procedure steps.
- **"Verification and Rollback" is not a section pairing any source publishes.** No template read titles a
  section that way. The bundle uses the evidenced names instead, Validation and Remediation and Cleanup, and
  drops the invented pairing.
- **"Escalation" and "Related Runbooks" are dropped.** Neither appears as a full section in any source read.

**Review Trigger has no published precedent, and the template says so.** The `standing-standards` family
contract requires a named review trigger, an event plus an owner, in every member. Of the sources read, only
one carries a service-owner field at all, and none carries a last-verified date in the document body. This
section is the bundle's own contribution, labelled as such rather than dressed up as received practice.

### The name is kept over the canon's own word

Google's SRE literature, the load-bearing source for nearly everything this bundle says about the artifact,
calls it a **playbook**. Four of the five SRE Book chapters most likely to discuss it were fetched and
searched by full-text regex for both words and returned zero occurrences of either. The word "runbook"
appears exactly three times in the Workbook's Incident Response chapter, and every occurrence sits inside a
third-party case study contributed by PagerDuty staff, not in Google's own analytical prose. This bundle
keeps the name `runbook` because that is this catalog's own name and the term the wider industry uses, and
the companion says so plainly rather than implying the canon endorses the term.

### The honest core

**The central value claim is asserted, not measured.** Google's clearest number is one informally stated
roughly-3x MTTR improvement, with no described sample, method or comparison group in the text read. Four
separate vendor MTTR and cost-reduction figures were traced and none reaches a described method; all four
are recorded in the research log as `not-retrieved` as to method and none is stated as fact anywhere in the
bundle.

**One contested question is left open rather than resolved.** Google names, in consecutive sentences of its
own canon, a live internal disagreement between general playbook guidance and step-by-step commands, calling
it "a contentious topic." This bundle does not pick a side its own primary source declines to pick; the
template asks the author to state which they are writing and why.

**No `pairs_with` skill is declared.** Every entry in `tools/known-skills.txt` was checked against this
type's job; none names operations, on-call, incident response or runbook authorship. `pairs_with: []` is
the honest reading, the same legitimate answer the `rfc` bundle already carries for the same reason.

### Verified before drafting

Six entries in the research log record a verified absence rather than a quote: four SRE Book chapters
fetched and searched by full text for "runbook" and "playbook," returning zero hits each. An entry with an
empty `Quotable:` list is not thin research here; it is the evidence behind the finding that the canon
barely uses either word in the chapters most likely to define it.
