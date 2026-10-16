# data-dictionary: history

Change log for the `data-dictionary` bundle. Each entry records what changed and why, so a reader can
tell a correction from a preference.

## 0.1.0 - 2026-10-15

**Initial release.** Admitted as the seventh `governance-docs` member by
[ADR 0073 (data-dictionary joins governance-docs as a seventh member)](../../docs/internal/decisions/0073-data-dictionary-joins-governance-docs-as-a-seventh-member.md),
which lands the family contract at `0.5.0`. Assigned and specced 2026-10-15 in
[`tier2-specs.md`](../../docs/internal/tier2-specs.md), building on admission sweep 5 (2026-10-12) and the
prep research of 2026-10-14. The build's seven-dimension fan-out covered the research-data-management
canon, the enterprise senses of the term, practitioner templates and documentation as code, the
product-analytics sense and the metric boundary, the debates over timing, upkeep, ownership and
obsolescence, this library's own neighbors and the facts the worked example must agree with, and the
standing gap question. [`data-dictionary_research-log.md`](data-dictionary_research-log.md) records **46
sources, all fetched-and-verified**: 5 primary, 3 standards bodies, 18 practitioner and 20 vendor. Every
quotation was checked against each source's raw text rather than a retrieval tool's summary of it: of 311
quotations the build's agents returned, 305 belonged to listed sources, and of those 257 passed as
normalized substrings and 7 more passed once a whitespace artifact was removed. Twelve quotations that
failed on rendering artifacts, dropped words, or added punctuation were re-quoted as 23 shorter segments,
26 joined table rows were replaced with 22 cell-level strings, and 3 quotations that ran list or table
cells together were split into 13 passing parts. Six quotations come from one source read in a browser
because it refuses a plain download, and five that the spec and ADR 0073 rested on, which no agent had
returned, were re-read from raw text and added. **333 quotations remain, all checked against raw source
text.**

### Membership widened the family's test a second time, drawn on subject rather than cadence

Like `tracking-plan`, this type did not fit the family contract's membership test as written at the time
of research: its noun ("structured reference") and its cadence ("revised as the schema changes, not
written once") fit, but a data dictionary does not track risk, open items, or performance, and it does not
specify what a product records so that performance can be tracked, which is `tracking-plan`'s own job.
ADR 0073 widens section 1 of the family contract with a second clause, "or to document what the fields of
a dataset or table mean, so that different teams compute the same number from them," and no existing word
changes. Unlike `tracking-plan`'s own widening, the boundary this one draws against its nearest neighbor is
reasoned on subject, not on which document is written first: the maintainer's 2026-10-13 sitting had
approved a tense-based scope condition (a tracking plan says what will be recorded, a data dictionary says
what recorded data means), and the 2026-10-14 research found that line was not the soundest statement of
the boundary, because several admitting sources use "data dictionary" for the forward-looking, event-shaped
sense `tracking-plan` already owns. The companion states both lines, the subject-based one this bundle is
built on and the tense-based one `tracking-plan`'s own shipped companion still carries, naming them as
different claims rather than smoothing over the reversal.

### `pairs_with` resolved to empty, and checked against the pinned list

A query against the pm-skills repository's `skills` directory on 2026-10-14 returned 68 skill names, none
of them naming "dictionary," "glossary," or "catalog." The closest adjacent name,
`measure-instrumentation-spec`, addresses a single feature's own instrumentation plan, the per-feature
neighbor this library has already placed outside this bundle's scope. `pairs_with: []` is a deliberate,
checked answer, in the same posture the `rfc`, `issue-log`, `change-log`, and `tracking-plan` bundles
already take for the same reason: no governance skill of any kind exists in pm-skills today.

### `related_templates` named the two neighbors the boundary is actually drawn against

`related_templates` names `tracking-plan` and `kpi-dashboard`, the two siblings this bundle's own
companion, section 8, states a load-bearing boundary against: the tracking plan specifies the events and
properties a product emits, upstream of what this document describes once those events land somewhere, and
the KPI dashboard's own Metric Definitions section locks a derived metric's formula, a job this document
does not do. The worked example links both siblings directly in its own body prose. The companion's section
8 also states a position against `risk-register`, `raid-log`, `issue-log`, and `change-log`, because the
family contract requires every member to state its position against every other member, but that section
says plainly that no source read connects this type's field-meaning job to any of the four, and the worked
example names them only in its opening library-facing blockquote as the shared program's other standing
instruments, never in body prose. `related_templates` does not carry a sibling the companion itself says no
source ties this type to; it names the two genuine neighbors, not every family member.

### `sizes_available` resolved to `[lean, full]`, matching the shared spine plus a genuine second weight

Every admitting source that ships a column set converges on the same spine: a field's name, type,
definition, and allowed values, which is what the lean variant's Field Definitions table carries alongside
Purpose and Boundary and a named Ownership and Review. A second weight earned its place on the same
evidence Docsie, Wizbrand, and Basedash each state: more than one team maintaining the schema, a field
holding personal or restricted data, and a need to answer later what changed and who approved it. Full adds
exactly the sections those signals call for and nothing else: Dataset Metadata, Relationships, Validation
Rules, and Review and Sign-off.

### Catalog corrections applied at landing

Per the spec's own Catalog corrections subsection, the alias "metric definitions" is dropped: it collides
exactly, case-insensitively, with `kpi-dashboard`'s own shipped "## Metric Definitions" heading, and a
catalog search on that alias would return the wrong artifact. The alias "data catalog entry" is not carried
forward either: the companion's own section 8 names a Data Catalogue as a different, independently defined
concept ("an inventory of available data assets," distinct from a Data Dictionary on the same glossary
page), so keeping it as an alias for this type would mislead a reader toward the wrong document rather than
disambiguate one. "Codebook" is added as the one alias the research supports directly: the common synonym
this type carries in research-data-management settings, stated by the University of North Carolina and
named without ranking in the companion itself.

### The honest core

No source read for this bundle measured whether keeping a data dictionary changes an outcome. What exists
is one qualitative case study of a clinical-research project that lacked one, reporting that the absence
"created the possibility for new study staff to misinterpret the data," and one datathon event abstract
that names incomplete data dictionaries among several reproduction challenges while every team still
reproduced the trial's results. Neither is a measured effect, and the guide and companion both state the
case for this document as resting on named failure modes and practitioner testimony, not on a measured
result.

### What was not read, and is not claimed

ISO/IEC 11179's own text is paywalled; the bundle cites only Wikipedia's description of it, and makes no
claim about the standard's clause structure or attribute list beyond what that description states. The
DAMA Dictionary of Data Management's paid entry for the term was not read. Snowplow's assigned
tracking-design page now redirects to a page that never uses the term, a null result recorded rather than
silently dropped. A statistic claiming a "60% reduction in data interpretation errors," attributed to a
2024 source, returned HTTP 403 on every fetch attempt and appears nowhere in this bundle. Three practitioner
pages on ownership and upkeep returned a bot challenge or HTTP 403 to every method tried and are not cited.
Several gap-question leads on units and standard formats (a UK Data Service page, SDMX 3.0, the OMOP Common
Data Model, and three national statistics offices) returned no operative text and are not cited.
