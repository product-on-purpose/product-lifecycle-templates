# project-milestone-retrospective: history

Change log for the `project-milestone-retrospective` bundle. Each entry records what changed and why, so a
reader can tell a correction from a preference.

## 0.1.0 - 2026-09-13

- **The four-lens review found no fabricated quotation and no blocker**, which is worth recording because
  the bundle built the day before this one shipped a first draft containing two. The citation lens mapped
  all 48 companion references to their log entries, confirmed every one is `fetched-and-verified`, and
  checked both admission quotes character by character against the log.
- **What it did find was overstatement, in five places, all corrected by narrowing rather than by
  re-sourcing.** "Everybody uses" and "widely used", of Derby and Larsen's five-stage model, asserted an
  adoption level no source measures. "Changed the content of every real filled document read" was true of
  the three accountability-grade documents and not of all five. A Kubernetes "defect rate" figure existed
  only in the research's own synthesis narrative and not in any source's logged quotation - the precise
  pattern that produced yesterday's fabrications - so the claim was softened to engineering quantities
  rather than hunted for in the original document. And Nancy Dixon had been folded into the set of critics
  who "still recommend writing something down" when this research records her as locating the value in
  in-team sense-making rather than in a transferable artifact; she is now kept distinct.


**Initial release.** Researched 2026-09-12 across six dimensions: origins and admission, structure,
methodology lineage, debates and status, relationships and tooling, and a blinded gap question read against
real filled documents.
[`project-milestone-retrospective_research-log.md`](project-milestone-retrospective_research-log.md) records
**93 source records merged to 80 unique sources**, of which **63 are fetched-and-verified**, 8 are
url-confirmed-not-read and 9 were not retrieved. Only fetched-and-verified sources are quoted anywhere in
this bundle.

**The third member of the `process-docs` family**, adopted in
[ADR 0033 (the process-docs family contract)](../../docs/internal/decisions/0033-adopt-process-docs-family-contract.md),
which groups documents written once to convert hindsight into an owned change and which names this type by
exact catalog id as a likely future member. The family is built to be taught by contrast, and this member
completes the set: `sprint-retrospective-notes` looks back on a **period**, on a cadence, at how a team
worked; `incident-postmortem` looks back on an **event**, triggered by it, at why a specific thing failed;
this document looks back on **a bounded piece of work that has ended**, for readers who may not have been
there.

**One research pass was designed for two bundles, and only this one ships.** The pass served both
`project-milestone-retrospective` and `pi-release-retrospective`, because the two share almost their whole
source base and two fan-outs would have paid for the same pages twice. The second **failed** the admission
test and does not ship, recorded in
[ADR 0049 (pi-release-retrospective fails the admission test)](../../docs/internal/decisions/0049-pi-release-retrospective-fails-the-admission-test.md)
with the full evidence preserved in
[`pi-release-retrospective-admission-evidence.md`](../../docs/internal/pi-release-retrospective-admission-evidence.md).
The refusal is kept here rather than discarded because the boundary it draws is one of this bundle's
teaching points: the cadence-retrospective line feeds a backlog and produces no document, while the
after-action and lessons-learned lineage produces a document by design.

### Admission rested on two independent named lineages, a stronger bar than the library had just set

The bundle built the day before, `spike-report`, was admitted on **one** named source standing against its
own canon, under
[ADR 0048 (one named source clears the admission test)](../../docs/internal/decisions/0048-one-named-source-clears-the-admission-test.md).
This type needed no such ruling, because two unrelated institutions publish it as a written document:

- **The Center for Army Lessons Learned** names the "After action report" separately from the review itself
  and defines it as a written report submitted after a mission, which documents a unit's actions for
  historical purposes and carries key observations and lessons learned. It ships a formal template whose
  two stated purposes are historical documentation and Army-wide dissemination.
- **PMI**, via the PMBOK Guide **Sixth Edition**, lists the "Lessons learned register" as a named output of
  process 4.4, Manage Project Knowledge, and the register recurs as a named input across roughly a dozen
  other processes. It was retrieved from a freely published PMI errata PDF on pmi.org, not inferred from a
  consultancy blog.

### The foundational Army source is the weaker one, and that inverts the obvious assumption

**TC 25-20 (1993)** is the older and more foundational Army source, and it is the one that does **not**
support a written after-action report. It defines the AAR as a verbal, professional discussion and insists
an AAR is not a critique; the only writing it prescribes is the observer's own preparation notes, not the
session's output. The written-report admission comes from CALL's later and more explicit doctrine. Anyone
citing TC 25-20 for a mandated written AAR is citing the wrong document, and this bundle says so wherever
the lineage is described.

**The PMI citation is time-bound and labelled as such.** The PMBOK Guide's **Eighth Edition** restructured
around principles rather than named ITTO artifacts, and its freely published table of contents carries no
"Lessons Learned" heading at all. Whether the register survives under that name could not be confirmed,
because the full Eighth Edition text is paywalled and was not read. Every claim about the register cites the
Sixth Edition and says which edition it is citing.

### Two sizes ship, and the argument is two genres rather than two weights

The filled and blank documents read for this research split into two genuinely different kinds of document.
The **team-authored retrospective** is written by the people who did the work, read by the team and whoever
comes next, short and narrative, and it never tracked prior findings in any example read. The
**accountability-grade report** is read by a sponsor, a board or a named official, is long, quantified and
addressed, and tracks prior findings structurally. `lean` serves the first and `full` serves the second.

**Previously Identified Issues is `full` only, and the limit is the reason.** Recording a lesson that was
already known and not acted on appeared **specifically in the external-audit genre** and not in the
team-authored retrospectives read, so promoting it into `lean` would have asserted more than the corpus
supports. No published template read here ships a named lean and full pair; the two sizes package an
observed split in practice, and the companion says so rather than implying vendor precedent.

**One honest counter-signal is carried rather than filtered out.** The strongest worked example this
research found, 18F's published acquisition retrospective, uses none of the standard sections and is
organised instead around the project's own three named aims. The template's claim is that these sections are
what this research found missing, not that no good document was ever written without them.

### Two departures from the Tier-2 spec, both forced by the research

The spec in [`tier2-specs.md`](../../docs/internal/tier2-specs.md) proposed the section set and expected the
research to move it. It moved it twice.

- **Scope and Period carries a second half the spec did not have: the audience and the document's next
  use.** The spec described this section as boundaries alone, the thing that stops the three family members
  blurring. Three of the four real filled documents read show that naming the reader **changed the content
  and not just the cover page**: the IRS relabelled its own findings as opportunities rather than lessons
  because they fed a specific pending decision, and said so in the same sentence; GAO-19-25 is literally a
  letter addressed to a named recipient and closes by naming what it wants from whom; the NAO report ends
  in lettered recommendations aimed at one named body. A naive what-went-well, what-did-not, actions shape
  has no field for any of that. The expert guidance follows from the same evidence: if no reader and no
  next use can be named, that is a finding rather than a formatting problem.
- **What Happened asks for quantification, and the rule is quantify something material, not quantify in
  currency.** All three government sources read lead with numbers, and it would have been easy to write a
  template that demands money. The Kubernetes 1.3 Storage SIG retrospective quantifies a defect rate and a
  schedule slip instead, which is what stopped that overfit: currency is a feature of public-money
  accountability documents, not a universal requirement. The `full` variant's quantification table asks for
  planned against actual on the two or three measures the work was actually judged on, and says to record
  that only elapsed time is available rather than manufacture a metric.

### The honest core

**The criticism of this document type is real, and it is narrower than it first sounds.** Every
fetched-and-verified source that criticises lessons-learned practice attacks a **specific pattern**, an
inert repository or minutes filed and never consulted, and **every one of those critics still recommends
writing something down**. Their fix is always a different kind of document, never no document. The
discriminator is whether retrieval is wired into somebody's workflow rather than dumped into a general
archive nobody has a reason to open. The framing this bundle carries is therefore
**anti-deposit-and-forget, not anti-documentation**, and a bundle reporting that "retrospective documents
are widely criticised" without that distinction would be overstating its own sources.

**Two peer-reviewed findings pull in opposite directions, and both are kept.** Dingsøyr et al. (2018) find
that the document can actively harm the practice: publishing retrospective minutes may cause participants to
tone down or remove real critique before it is ever written. Anandayuvaraj et al. (2026) find the opposite
failure at a different kind of organisation: engineers at a national space research centre explicitly want a
lessons-learned database, do not have one, and lose knowledge to staff turnover. A bundle carrying only the
first would be arguing against its own artifact; one carrying only the second would be ignoring a real harm.

**`after-action review` is an alias this type shares with `incident-postmortem`, deliberately.** Both
bundles declare it, because both lineages really do use the phrase, and the shared alias is a boundary fact
worth knowing rather than a collision to resolve by deleting one. The trigger is what tells them apart: an
ending versus an event.

### pairs_with declares `iterate-retrospective`, and names an inconsistency it does not fix

`pairs_with: [iterate-retrospective]`. The skill was verified present at `skills/iterate-retrospective/SKILL.md`
in product-on-purpose/pm-skills on 2026-09-13, using the command in the header of `tools/known-skills.txt`
against the tracked source rather than the gitignored build copy: version 2.2.0, phase `iterate`. The
pairing is the skill's own claim, not this bundle's inference, because its description names the occasion
directly: use it at the end of a sprint, project, or milestone.

**The inconsistency is recorded rather than papered over.** That same description names the **sprint**, and
the shipped `sprint-retrospective-notes` bundle still declares `pairs_with: []`. Either that empty pairing is
a miss nobody has revisited or it was deliberate and the reasoning was never recorded. This build does not
change a shipped bundle's metadata, so the question is logged here and in the Tier-2 spec for the maintainer
to settle for all three members at once.
