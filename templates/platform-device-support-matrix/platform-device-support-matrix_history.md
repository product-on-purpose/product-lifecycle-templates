# platform-device-support-matrix: history

Change log for the `platform-device-support-matrix` bundle. Each entry records what changed and why, so a
reader can tell a correction from a preference.

## 0.1.0 - 2026-11-12

**Initial release.** Admitted by
[ADR 0088 (the platform and device support matrix joins standing-standards as a foundation)](../../docs/internal/decisions/0088-platform-device-support-matrix-joins-standing-standards-as-a-foundation.md),
which the maintainer accepted on 2026-11-09. Built on 2026-11-12 after a six-dimension research run covering
origins, structure, practice, debates, relationships with neighbouring documents, and the question of what
the first design missed. The build is issue #353 (bundle: platform-device-support-matrix), and it fills
catalog entry 212.
[`platform-device-support-matrix_research-log.md`](platform-device-support-matrix_research-log.md) records
**36 sources, all fetched-and-verified**: 24 primary, 6 practitioner, 4 vendor and 2 standards.

**The eighth `standing-standards` member.** It declares `classification: foundation`, the contract's cut
for a standard you are judged against. ADR 0088 argues the choice marker by marker against the honest `tool`
case. People other than the authors consult the matrix, which fits the `tool` marker. What breaks the
parallel is timing: a runbook is executed once a situation is declared, and the matrix is consulted in the
ordinary course of testing and triage. That reading is this library's inference by analogy. No source tested
when or under what pressure a matrix is applied, and the ADR puts its confidence in the classification at
medium.

### One size ships, at medium confidence

The bundle ships `lean` only. The research looked for the evidence a second size would need, per-row
evidence columns such as a usage share or a date last verified, and a separate polyfill or
progressive-enhancement policy section. It found neither in the three government and design-system pages
the structure dimension read. The commercial pages were not checked for per-row columns, and GitHub's
polyfill policy is a document beside its matrix, not a section of one. The nearest things are a principles
list and a dated history kept for the whole page, and the Review Trigger section already holds that history. The spec rated its confidence in the
single size as low, and the research raised it to medium. The signal for a second size is a named matrix
that publishes either, and a feeling that the page needs more is not one.

### The two promises are kept apart, and the separation is this library's position

The sources use the word "support" in different senses. Material Components Web defines its supported set
as the set it tests, MetaMask supports browser forks it does not test, and the GOV.UK Service Manual's list
is a list of browsers "to test in". That the senses differ is well supported. The template therefore
defines each grade by its commitments and marks testing in a column of its own. That separation is the
library's position, and the template labels it as such.

Several other parts of the structure have no source that publishes them, and each is labelled where it
appears:

- The separate Grade and Tested columns, and the Notes column. The one source whose table header was read
  keeps a single status column that holds both the level and the test status.
- The role names in Ownership. No source names a person or role who may change a grade.
- The trigger table in Review Trigger. Its new-platform condition is the library's own synthesis.

The matrix's own column for versions is worded as a minimum version or a version rule, because MetaMask,
Material Components Web and Jenkins state windows and N-and-N-1 rules where AusDTO states a minimum.

### Attribution corrections carried into the bundle

- **No lineage is claimed from YUI to GOV.UK.** No GOV.UK page or issue read names Yahoo or YUI, and the
  letters mean different things in each scheme. The bundle calls this a shared vocabulary, not a documented
  lineage.
- **The authorship of YUI's scheme is attributed, not asserted.** The only statement read is Springer
  Nature's, that the concept was originally conceived by Nate Koechley. The original Yahoo article was not
  read, so the date and the author stay as leads.
- **Every threshold is attributed to the team that chose it.** USWDS and the ONS use 2 percent. The GOV.UK
  Service Manual states a coverage figure of approximately 98 percent of GOV.UK's own traffic. Deque's 1
  percent applies to assistive-technology combinations. None is presented as a norm.
- **The annual review is presented last among the review conditions.** The Service Manual's history shows
  the list changing when usage moved, and periodic reviews checking whether it had. Those reviews date from
  2020 and 2021, about six months apart, and GOV.UK's annual commitment dates from 2024. Reading the annual
  figure as a floor on how long the condition can go unchecked, as ADR 0088 does, is this library's
  inference at medium confidence. The evidence is GOV.UK's, and no other team's cadence is known. The
  four-lens review caught the first draft reading those entries as yearly reviews, and the research log
  carries a dated correction.
- **No cadence is invented.** The sources give GOV.UK's annual commitment, the GDS Way's annual review date,
  GOV.UK's earlier reviews about six months apart, and changes linked to usage or discussion.
- **The GDS Way is cited as a government team's own guidance.** Its page says it is intended for internal
  use, so it is not cited as a standard.

### What the research found and did not find

**The commercial caveat narrows, and it does not close.** The spec's weakest claim was that every source was
a government or design-system team. The build read five commercial pages, each as repository source on
GitHub. Commercial teams publish support statements, mostly as version rules without grades. Among
commercial teams, levels were found only at Springer Nature. Jenkins also keeps levels, and it is an
open-source project rather than a commercial vendor. The bundle does not say commercial teams keep graded
matrices.

**Not found:** a filled, team-owned matrix with assistive-technology rows, a viewport floor stated as a
commitment, a government page on telling end users about a dropped browser, and a source arguing that a
graded list costs a small team too much. No source shows that keeping a matrix improves outcomes, and none
measures what keeping one costs.

### What the gap question added, and what it routed elsewhere

The gap dimension found one real absence, assistive-technology combinations. GOV.UK keeps its table on a
page of its own, so Purpose and Scope asks where those combinations live and the matrix holds none of them.
Telling users about a raised minimum, an exemption for some audiences, and an effective-from date also
entered as asks or fields. JavaScript switched off, a slow connection and viewport sizes were each routed
out of the matrix, because the sources treat each as a build rule, a performance budget or layout
configuration, not as a support commitment. None of the candidates added a section.

### Verified before drafting

**Every quotation was checked against raw text**, never against a retrieval tool's summary. Of the 132
quotations the research agents returned, 123 passed on the first check. Eight of the nine failures were
copied from Markdown source formatting and checked against the rendered page, and each replacement passed.
The ninth survives only as its second clause. Three quotations that passed against the cached copy failed a
fresh fetch, and they were dropped. The facts they carried stay in the log's Supports lines. The AusDTO
table's header row was not quotable at the sweep stage, and the rendered header row now passes against the
page.

**Terms were checked against the admission sweep's verdicts first, and three new hosts were cleared after
they were read, which is the wrong order.** The main loop re-read each host's terms page raw, and each
permits reading. One site bars reading, and its page was not read.
Red Hat's terms forbid a robot, spider or retrieval application. The log lists the pages left unread under
the terms rule, and no claim in the bundle rests on one.

### Pairing

`pairs_with` is empty. `tools/known-skills.txt` holds no skill for browser, device or compatibility support,
which the 2026-11-12 read of that file confirmed again. An empty list is the legal answer, and the pairing
stays unclaimed until a skill exists that addresses this document.

### The example, and the stop rule it was built under

The worked example is the matrix for Harbourline Bookings, a passenger-ferry booking site run by a small
fictional operator, at `lean` size. The family contract weakens the Acme Analytics chaining on purpose, so a
fresh scenario was allowed and the example cites no sibling. Every figure in it is labelled illustrative. It
was built under the stop rule ADR 0064 and ADR 0074 record: if the filled example read as a table of browser
names with no decision visible in it, the build would stop and the decision would return to the maintainer.
The main loop read the example against that rule on 2026-11-12, and it shows a promised but untested row,
a demotion on a dated analytics read, and two review conditions that fired.
