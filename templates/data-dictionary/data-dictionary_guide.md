# Guide: Data Dictionary (operator card)

Fast reference for using the data-dictionary bundle. For the full reasoning, origins, and sources, read
[`data-dictionary_companion.md`](data-dictionary_companion.md).

## When to use

- A dataset or table already exists, or is about to, and more than one team reads from it: each team needs
  to compute the same number from the same field, and the honest answer to "what does this column mean"
  today is "ask the person who built it."
- The schema will change over time. This is a standing reference, revised as the schema changes, not a
  one-time record filed once and archived; a field you add, redefine, or stop using gets a row here before
  or as part of that same change.
- A field carries a value a reader could misread without help: a coded value, a unit, a missing or sentinel
  code, or a flag that the field holds personal or restricted data.
- Your organization already keeps a similar document under the name codebook. Some research-data guides
  treat the two names as one document and others separate them, so check which yours is. If they are the
  same document, name which word your team actually uses rather than maintaining both under different
  headings.

## When NOT to use

- **The question is what events a product emits, and why.** That is the tracking plan's job: it specifies
  the events and properties a product intends to track, drawn on subject rather than on which document is
  written first. Several product-analytics vendors use this bundle's own name, "data dictionary," for that
  event-and-property catalog; a reader who means the event list wants the tracking plan, not this document.
- **The question is a metric's own formula, inclusions, or exclusions.** That is the KPI dashboard's own
  Metric Definitions section. This bundle documents what a field means; it does not lock what a derived
  metric computes from that field. This is this library's own position, held against three sources that
  place calculation logic inside a data dictionary, not a settled reading every source shares.
- **The question is an approved vocabulary of business terms, or an inventory of every data asset in the
  organization.** Those are a business glossary and a data catalog, two related, named artifacts this
  library does not build. Naming them here is only to keep their jobs out of this one.
- **The question is a risk, an open item, a resolved issue, or a change to an agreed baseline.** Those belong
  in the risk register, the RAID log, the issue log, or the change log. Nothing in this bundle's research
  connects a field's meaning to any of those four subjects.
- **The data has not landed anywhere yet, and nothing has been built to read it.** A data dictionary
  documents a field once it exists; a team with nothing to describe yet wants the tracking plan, which
  specifies what will be emitted before it lands.

### Data dictionary, or one of its three neighbors?

| | **Data dictionary** | **Tracking plan** | **KPI dashboard's Metric Definitions** |
|---|---|---|---|
| Tense | Documents a field once it exists | Specifies events before, or as, they are emitted | Locks a metric already defined elsewhere |
| Scope | What a field means, its type, its allowed values, its owner | Events, properties, and traits a product emits | One metric's formula, inclusions, exclusions, owner, and steward |
| Drawn on | Subject: what a field means versus what a product emits | Subject, not tense: this library's own reasoning differs from a tense-based line an older companion still carries | This library's own position against three sources that place formula logic inside a dictionary |

A business glossary and a data catalog are not a fourth neighbor on this table: this bundle builds neither,
and names both only so a reader reaching for glossary or catalog language does not fold a different
document's job into this one.

## Pick a variant

- **Lean** (default): Purpose and Boundary, Field Definitions, Ownership and Review. A single table's grain,
  its field-level facts, and a named owner with a review trigger, and nothing else. This matches the shape
  every research-data source in this bundle's research ships for one dataset: no relationships section, no
  separate validation table, and no formal sign-off chain.
- **Full**: adds **Dataset Metadata** (source system, version, effective date, refresh cadence, and primary
  consumers, ahead of the field table), **Relationships** (how this table's fields join to other tables),
  **Validation Rules** (enum lists, ranges, and cross-field checks stated separately from the field table's
  own allowed-values cells), and **Review and Sign-off** (a dated approval chain and the running version
  history, including each field's own deprecation). This matches a vendor's own fuller shipped template.
  Move to full once you have several related tables whose joins need stating somewhere, a dataset several
  teams rely on, or one that feeds a regulated report.

Grow lean into full by inserting Dataset Metadata before Field Definitions, inserting Relationships and
Validation Rules after Field Definitions and before Ownership and Review, and appending Review and Sign-off
last; the three lean sections keep their name, order, and table. No source read for this bundle states a
rule for when a team should make that move; the match between the lean and full shapes and what each group
of sources actually ships is this library's own observation, not a sizing threshold any source states, and
the choice is left to the author.

A team already keeping field descriptions in a documentation-as-code tool, beside the model that produces
them, may use either variant as a parallel, hand-read document, or may use neither and keep the same content
in the tool instead; this bundle does not resolve that choice.

## Quality rubric (self-grade)

Score each row 0, 1, or 2. Below 13 out of 18, a reader who joins this table to another, hits a missing
value, or needs to know who to ask will have to go find that person instead of reading the document, which
is the staleness and ownership failure this bundle's research describes most fully. A lean dictionary
carries no Dataset Metadata,
Relationships, Validation Rules, or Review and Sign-off section to grade, so it is scored, and cleared,
against a smaller table; see the scope table below.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Boundary rules out neighbors** | No line says what this document does not cover | A boundary line exists, but it names no specific neighboring document | You can point at the sentence naming at least one neighbor by name (the tracking plan's event list, or the KPI dashboard's metric formula) and at where that content actually lives instead |
| 2 | **Grain and key** | A field table appears with no grain line above it | A grain line exists, but it names no key column, or names a table with no grain line of its own | For every table this document covers, you can point at its own grain line and the key column or columns that enforce it, stated before any field is listed |
| 3 | **Non-circular definitions** | A definition restates the field's own name, or the cell is blank | Definitions are present, but at least one is circular, or one field's name is left to speak for itself with no definition at all | You can point at any field's Definition cell and state back what the value means in one plain sentence, without reading the column name out loud |
| 4 | **Missing and deprecated values** | A field's missing or sentinel code is unstated, or a retired field has simply disappeared from the table | Missing values are named, but at least one sentinel code is undocumented, or a deprecated field is marked with no replacement or removal date | You can point at the exact code that marks a value missing or a sentinel, and at a deprecated field's own replacement and removal date, for every field that carries one |
| 5 | **Owner and review trigger** | A table has no named owner, or the owner is a department label such as "the data team" with no steward named | An owner and a review interval are named, but nothing states whether a schema change itself also triggers a review | You can point at a named owner, either a person or the specific team that produces the data, a named person as steward, a named interval, and a statement that every schema change triggers a review in addition to that interval |
| 6 | **Dataset metadata complete** *(full)* | The source system, version, or effective date is missing | The source system, version, and effective date are present, but the refresh cadence or the primary consumers are missing | You can point at the source system, version, effective date, refresh cadence, and primary consumers, all stated before the field table starts |
| 7 | **Exact relationship fields** *(full)* | A relationship names only the two table names, with no field on either side | A relationship names one field, but not the field it points to, or leaves the relationship's kind (foreign key, join, or derived) unstated | You can point at the exact field on each side of a stated relationship and the kind of relationship it is, not only the two table names |
| 8 | **Testable validation rules** | A validation row states no rule, or restates a field's own allowed-values cell with nothing added | Rules exist, but at least one is too general for a loader to run against ("should be correct") | You can point at a validation row stated specifically enough that a loader could run it against a real row and get a pass or fail |
| 9 | **Sign-off and history** *(full)* | No reviewer or approver is named for the current version | A sign-off is present, but the version history has a row naming no field, no approver, or no date | You can point at the current version's preparer, reviewer, and approver, and at a version-history row naming the field affected, what changed, who approved it, and when |

### Rubric scope by variant

| Variant | Rows scored | Maximum | Threshold |
|---|---|---|---|
| lean | 1-5 | 10 | 7 |
| full | 1-9 | 18 | 13 |

Lean ships no Dataset Metadata, Relationships, Validation Rules, or Review and Sign-off section, so rows 6
through 9 grade content it does not carry; score a lean dictionary against rows 1 through 5 only. A lean
dictionary at 7 out of 10 clears a comparable bar to a full dictionary at 13 out of 18.

## Named anti-patterns (the usual wrecks)

1. **It goes stale.** The most fully sourced failure mode in this bundle's research: a dictionary written
   once and never reopened drifts from the schema it describes, and a reader trusts a definition that no
   longer matches the column. Fix: update the affected row as part of the same change that touches the
   schema, not as a separate task someone may skip, plus a standing calendar review besides.
2. **A header list standing in for a dictionary.** A tab of column names with no Definition cell filled in
   is not a data dictionary; it is a list of the names a reader already had. Fix: no field ships without a
   plain-language sentence in its Definition cell, even a short one.
3. **A circular or cryptic definition.** A definition that only restates the field's own name ("carrier_code:
   the carrier code"), or an abbreviated name such as `stat_cd` with no definition at all, leaves a reader
   to guess what the value means, and a wrong guess goes straight into a query. Fix: write the definition
   in genus-differentia form, "A is a B that C," and never let a field's own name serve as its definition.
4. **The grain left unstated.** A field table with no grain line forces a reader to infer what one row
   represents, which is a named source's own candidate for the most common cause of double-counted metrics,
   stated here as that source's own claim rather than a measured rate. Fix: one grain line, naming the key
   column or columns that enforce it, before any field is listed.
5. **A missing or sentinel value left undocumented.** A null, a sentinel code, or a deprecated field marked
   only by quietly vanishing from the table leaves a reader unable to tell a missing value from a real zero,
   or a retired field from one still safe to query. Fix: state the exact missing or sentinel code in the
   Allowed values cell, and mark a retired field obsolete with its replacement and removal date rather than
   deleting its row.
6. **A metric's formula, or an event's own business reason, creeping into this document.** Once a derived
   metric's calculation, or an event's own "why we track it," starts living in a Field Definitions row, this
   document stops being a single source of truth for field meaning and starts duplicating the KPI dashboard
   or the tracking plan. Fix: route a metric's formula to the KPI dashboard's Metric Definitions section and
   an event's own business reason to the tracking plan, and name the field this document actually documents
   instead.
7. **Ownership with no one to ask, and no review trigger beyond "periodically."** "Reviewed periodically
   by the data team" gives a reader no person to ask and no way to tell whether the table is actually current
   or merely was current once. Fix: one named owner, either a person or the specific team that produces
   the data, one named person as steward, and a stated review interval that names whether it is borrowed
   from elsewhere or the team's own choice, in addition to the schema-change trigger.
8. **A known caveat left for a reader to discover the hard way.** A field whose value excludes something its
   name does not advertise, such as a total that quietly excludes refunds, and that caveat is left unstated,
   lets a reader build a wrong number with full confidence. Fix: state the caveat in the field's own
   Definition cell, where a reader actually meets the field, rather than leaving it to be rediscovered.

## No paired skill (yet)

This bundle's family contract states plainly that no governance skill exists in pm-skills today for any of
its members, so every member adopts `pairs_with: []` until one does. Until a governance-side skill exists,
this template is filled by hand.
