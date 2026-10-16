# Companion: The Data Dictionary

> The deep explainer for the data-dictionary bundle. Read this to understand what a data dictionary is,
> where the name comes from, why this bundle draws its boundary where it does, and where the sources
> disagree. The short operator card is `data-dictionary_guide.md`; a fully worked instance is
> `data-dictionary_example.md`. Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A data dictionary documents what the fields of a dataset or table mean, so that different teams compute
the same number from them. CASRAI states the job in full: "A data dictionary is a structured document,
table, or file that defines every variable in a dataset - its name, meaning, data type, unit of
measurement, allowed values, and any coding scheme used to represent those values - so that anyone other
than the person who collected the data can interpret it correctly." [[5]](#ref-5). OSF puts the same job
more plainly: "The purpose of a data dictionary is to explain what all the variable names and values in
your spreadsheet really mean." [[1]](#ref-1). It is a standing reference, revised as the schema changes,
not a one-time record filed once and archived.

- **The name covers three distinct senses, and this bundle builds one.** The field-meaning sense, a
  document of what a dataset's or table's fields mean, is this bundle's own scope, independently defined
  by OSF, CASRAI, GOV.UK's Data Architecture Community, Docsie and Basedash
  [[1]](#ref-1)[[5]](#ref-5)[[9]](#ref-9)[[17]](#ref-17)[[19]](#ref-19). The event-list sense, a catalog of
  a product's events and their properties, is `tracking-plan`'s subject, and Mixpanel, Amplitude and
  RudderStack each use this bundle's own name for it
  [[21]](#ref-21)[[22]](#ref-22)[[24]](#ref-24)[[27]](#ref-27). The DBMS-internal sense, the read-only
  tables a database engine keeps about its own objects, is named explicitly by Oracle and listed as one of
  several meanings on Wikipedia's own page [[12]](#ref-12)[[10]](#ref-10); this bundle scopes that sense
  out entirely.
- **The field-meaning sense itself has two names, and research settings use both.** Codebook is the
  common synonym in research data management; the University of North Carolina treats the two as the same
  document under different names [[4]](#ref-4), while CASRAI draws a narrower, more mechanical line for
  the dictionary against a fuller, study-level codebook [[5]](#ref-5). Section 6, item 3, states this as
  contested rather than settled.
- **No source in this research measured whether having a data dictionary changes an outcome.** What
  exists is one qualitative case study of a project that lacked one [[40]](#ref-40) and one event abstract
  that names the lack of a complete dictionary among several reproduction challenges while every team
  still reproduced the results [[41]](#ref-41). Section 7 states both as what they are, not as a measured
  effect.
- **The bundle's own two boundaries are not symmetrically sourced.** The line against `tracking-plan`,
  drawn on subject rather than on which document is written first, holds across every source that
  addresses timing at all (section 6, item 1). The line against `kpi-dashboard`'s own Metric Definitions
  section, keeping a metric's formula out of this document, is this library's own position against three
  sources that place calculation logic inside a data dictionary (section 6, item 2). The companion states
  which boundary is which rather than presenting both with equal certainty.

---

## 2. Origins and evolution

No source read for this bundle traces when the term data dictionary began, who coined it, or which
field first published one, and this companion does not invent a founding date. What the sources do show is
three lineages that each arrived at the field-meaning sense independently.

The research-data-management lineage is the most explicit about the document's purpose: OSF, the
Smithsonian, the University of North Carolina, CASRAI, Harvard Medical School and NNLM each define it as a
document a researcher writes so that someone other than the person who collected the data can understand
it [[1]](#ref-1)[[3]](#ref-3)[[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7). Buchanan et al.'s own
tutorial states the same reproducibility purpose and adds a production mechanism: a tool converts
already-held data into the dictionary automatically, "the data are converted to a data dictionary or
codebook by using a tool, like Codebook or Data Dictionary Creator, that creates the metadata output in
JSON-LD and/or HTML format" [[2]](#ref-2). This lineage also carries the interchangeable-terms observation
most directly: "Data dictionaries may include the information provided in a codebook and vice versa", and
"and sometimes these terms are used interchangeably" [[2]](#ref-2).

The enterprise-data-management lineage frames the document against two named neighbors rather than against
a codebook. GOV.UK's Data Architecture Community defines all three terms on one page and names the
confusion directly in its own "COMMON MISUNDERSTANDINGS" field: "Confusion over definition and with related
concepts: o Business Glossary o Data Catalogue" [[9]](#ref-9). Wikipedia's own entry for the term separates
a document sense, a DBMS-component sense, and a middleware sense, and states plainly, "There is no
universal standard as to the level of detail in such a document." [[10]](#ref-10).

The documentation-as-code lineage treats the data dictionary as something generated from, and kept beside,
a data model rather than authored as a separate prose document: dbt instructs a team to "Add the
description: key to the same YAML files where you declare data tests." [[20]](#ref-20), and a practitioner newsletter prescribes the same
move as a fix for a stale, hand-written dictionary: "Treat Docs Like Code", "Version it. Update it when
data changes. Assign ownership." [[35]](#ref-35).

**One standards body is named in this research, and only its description is read.** Wikipedia's own entry
for ISO/IEC 11179 names the registration, naming and value-domain obligations the standard places on a
data element [[11]](#ref-11); the standard's own text is paywalled, so nothing in this bundle describes
ISO/IEC 11179's clause structure or attribute list beyond what that description states.

---

## 3. Anatomy (section by section)

The template's full variant carries seven sections; the lean variant carries three of them, Purpose and
Boundary, Field Definitions and Ownership and Review, in that order, as a strict ordered subset of the
full variant's seven. The column set below is this library's own convergence across several admitting
sources, not any single vendor's shipped list, following the same practice `tracking-plan`'s own Structure
section used for columns no one source states whole.

### Purpose and Boundary

**What it is:** a short statement of which dataset's or table's fields this document covers, and what it
rules out by name. **Why it exists:** because the name this bundle carries is overloaded, and the first
job of this section is to rule the other senses out before the field table starts. It excludes event
cataloguing: product-analytics vendors use this bundle's own name for an events-and-properties catalog,
most directly Mixpanel's own Lexicon page, "Lexicon is a data dictionary that stores descriptions of
events and their properties." [[21]](#ref-21); that subject is `tracking-plan`'s job, and a reader who
means the event list is routed there. It excludes metric-formula locking: Basedash separates "The metrics
layer on top of tables" [[19]](#ref-19) from the field-level facts a dictionary carries, and dbt's own
Semantic Layer exists specifically to "centrally define business metrics" apart from the tools that
consume them [[28]](#ref-28); that subject is `kpi-dashboard`'s own Metric Definitions section. The section
also names codebook as the common synonym this type carries in research settings, without ranking the
two terms against each other [[2]](#ref-2)[[4]](#ref-4)[[5]](#ref-5).

### Dataset Metadata (full only)

**What it is:** a header naming the dataset or table, its source system, its version and its effective
date, ahead of the field table. **Why it exists, and why it is full-only:** a single small table needs
little more than its field list, while several related tables need a header that says which system each
one came from and when this version took effect. Docsie's own shipped document opens with exactly this
header before its field table, asking the author to "Describe the dataset purpose, source systems, refresh
cadence, and primary consumers." [[17]](#ref-17). Basedash's own framing runs throughout at the table level
rather than the field level, describing "its grain (what one row represents), its primary key, its update
cadence, and how it relates to other tables" as what a complete dictionary documents about the table as a
whole, beyond any single column [[19]](#ref-19).

### Field Definitions (lean, a table, the load-bearing section)

**What it is:** one row per field, naming its type, its meaning, its allowed values and its owner.
**Why it exists:** because this is the section every admitting source converges on, and the one a reader
actually opens the document to find. Each table's entry opens with one line stating its grain, what one
row represents, and the key that enforces it: "The grain of a fact table states what 1 row means, and it
is decided before any column is added." [[45]](#ref-45), and "Naming the columns that enforce the unit is
what lets another engineer write a test against it." [[45]](#ref-45); Basedash makes the same point about
cost, calling an unstated grain "the most common source of double-counted metrics", which this companion
attributes to Basedash's own claim rather than to a measurement [[19]](#ref-19). Below the grain line, the
library's own seven-column convergence, no single source's whole list, is: **Field**, "The technical
column name" [[19]](#ref-19); **Type and nullability**, paired the way Basedash pairs them, "Data type and
nullability" [[19]](#ref-19); **Definition**, a plain-language sentence of what the value means, sourced
to OSF's "Definition of the variable" [[1]](#ref-1) and CASRAI's "What does it measure or record?"
[[5]](#ref-5); **Allowed values, units and missing codes**, sourced to the University of North Carolina's
"including null or missing values" [[4]](#ref-4), CASRAI's "How is missingness represented?" [[5]](#ref-5),
OSF's "Measurement units" [[1]](#ref-1) and Basedash's "Enums, ranges, or units" [[19]](#ref-19);
**Source**, including how often it refreshes, sourced to CASRAI's "Where did this variable come from?"
[[5]](#ref-5) and Basedash's "Where the value originates" and "How current the data is" [[19]](#ref-19);
**Sensitivity**, sourced to Basedash's "PII or restricted-data flag" [[19]](#ref-19) and Avo's own property
field, "The PII status of the property - whether it carries personally identifiable information"
[[26]](#ref-26); and **Owner**, a person or team accountable for the field, sourced to Basedash's own
"Person or team accountable for it" [[19]](#ref-19) and Dataedo's own entry content, which "May include
many data attributes (e.g. list of values, default values, owner, etc.)" [[13]](#ref-13).

A missing or sentinel value is documented, not assumed. The DDI Alliance's own metadata model treats a
sentinel code as a distinct, formally modeled kind of value: "Sentinel values are used for processing, not
to describe subject matter." [[42]](#ref-42), and the UK Data Service's own training materials keep
missing-value ranges in a field of their own, apart from the ordinary value-label field [[46]](#ref-46). A
field the schema has stopped using stays in the table rather than disappearing from it, with its
replacement and removal date recorded where a reader meets the field: the Open Contracting Data Standard's
own deprecation rule requires that "Validation tools must report use of deprecated fields to the user" and
that a deprecated field is marked "with the presence of a deprecated property and object which declares
the version number in which the field was first deprecated" [[43]](#ref-43); the NIMH Data Archive's own
dictionary marks an entry obsolete the same way: "Some structures are obsolete, superseded by newer
structures, or were created to support legacy projects." [[31]](#ref-31), rather than simply deleting it. A known trap belongs in the Definition cell where a reader meets the field,
in the shape of Basedash's own net-revenue caveat, "A good caveat ("this excludes refunds") prevents the
right column from being used the wrong way." [[19]](#ref-19), without copying its wording.

A good definition follows OSF's own genus-differentia form, "A is a B that C" [[1]](#ref-1), illustrated by
OSF's own worked example, "An a) attitude is a b) disposition c) to think or feel that is about something
or someone, typically one that is reflected in a person's behavior." [[1]](#ref-1). A weak one is circular,
OSF's own counterexample, "Avoid circular definitions (e.g. A baseball is a ball used in baseball.)"
[[1]](#ref-1); or cryptic, Basedash's own warning that "An AI assistant pointed at a schema with cryptic
names like flg_2 and dt_x will guess, and guesses produce confidently wrong numbers." [[19]](#ref-19); or a
bare list of column headers with nothing said about what any of them mean, which CASRAI names directly as
the failure this whole section exists to avoid: "A spreadsheet tab that lists only column headers with no
definitions is not a data dictionary under this definition - it is a header list." [[5]](#ref-5). The
University of North Carolina's own worked row shows the coded-value form this section's allowed-values
column follows: "gender | Whether or not the respondent is female | male = 0; female = 1; missing = N/A"
[[4]](#ref-4). This section carries a PRIORITY marker and a ROW HINT.

**A note on reuse.** OSF's help article is released under CC0 [[1]](#ref-1), CASRAI's content under
CC-BY 4.0 [[5]](#ref-5), the University of North Carolina's article under CC BY-NC 4.0 [[4]](#ref-4), the
District of Columbia's catalog record under CC BY 4.0 [[8]](#ref-8), and both Wikipedia articles cited here
under CC BY-SA 4.0 [[10]](#ref-10)[[11]](#ref-11). No licence was found on Docsie's, Wizbrand's, Basedash's,
dbt's or Amplitude's pages, so this bundle's own worked example and its GOOD and WEAK text do not borrow
any of those vendors' wording or worked rows.

### Relationships (full only)

**What it is:** how this table's fields relate to other tables: foreign keys, joins, or a field computed
from another table's field. **Why it exists, and why it is full-only:** a single table with no related
tables has nothing to describe here, while several related tables need the joins stated somewhere. Docsie's
own template asks the author to "Document primary keys, foreign keys, joins, and related datasets."
[[17]](#ref-17), and Harvard Medical School's own definition, "Outlines the structure, content, and
variable definitions for a dataset or collection of data" [[6]](#ref-6), reads naturally as more than one
table in scope once relationships exist between them to describe.

### Validation Rules (full only)

**What it is:** enum lists, numeric ranges, required-versus-optional fields, and any cross-field rule a
loader or a reviewer should check. **Why it exists, and why it is full-only:** the same reasoning as
Relationships; a small table's Field Definitions table already carries its allowed values, while a larger
or more heavily consumed table benefits from stating the checks separately. Docsie's own template asks the
author to "List accepted values, null handling, range checks, and uniqueness rules." [[17]](#ref-17), and
Basedash's own attribute list names the same content at the field level, "Enums, ranges, or units"
[[19]](#ref-19). dbt's own documentation-as-code mechanism offers a parallel, automated form of the same
idea: a `not_null` or `unique` test declared beside the field's own description [[20]](#ref-20).

### Ownership and Review (lean)

**What it is:** the table's own named owner and steward, apart from any individual field's owner, and how
the table is reviewed. **Why it exists:** because an unowned, unreviewed dictionary is the failure section
7 describes, and this section is where that failure is prevented. Basedash states the ownership default
plainly, "Owners are usually the team that produces the data, not the team that consumes it"
[[19]](#ref-19). Docsie's own template asks the author to "Identify data owner, steward, support channel,
and review cadence." [[17]](#ref-17), and Wizbrand's own key-components list carries "Ownership and
stewardship: Who maintains it, who approves changes, and who is notified." [[18]](#ref-18). No fixed
interval is a norm across the sources (section 6, item 9), so this section asks the author to name one and
to say whether it is borrowed or the team's own, the same discipline `tracking-plan`'s own Review and
Ownership section already applies. The review trigger itself has two parts the sources agree on even where
the interval disagrees: every schema change, plus a stated calendar interval. Basedash ties the first
trigger directly to the change itself, "Update definitions whenever the schema changes, as part of the
change itself rather than as a separate task." [[19]](#ref-19), and Atlan's own drift-prevention guidance
states the same rule as an SLA, "Review frequency depends on change velocity." [[36]](#ref-36).

### Review and Sign-off (full only)

**What it is:** a formal record of who reviewed and approved this version, and when, apart from the
Ownership and Review section's own standing owner and cadence. **Why it exists, and why it is full-only:**
a small, informally maintained table needs no sign-off chain, while a dataset several teams rely on, or one
that feeds a regulated report, benefits from a dated approval trail. Docsie's own shipped document carries
exactly this beyond its basic owner-and-cadence fields, with "Preparer", "Reviewer" and "Approver" roles,
a "Review Cycle", an "Effective Date" and a status field, "[Draft / In Review / Approved]"
[[17]](#ref-17). This section also carries the version history, including each field's own deprecation, so
a reader can see what changed, when, and under whose approval, apart from reading the current table alone.

---

## 4. Variants and sizing

**Lean** carries Purpose and Boundary, Field Definitions and Ownership and Review: a dataset's purpose, its
field table, and a named owner with a review trigger, and nothing else. This matches the shape the
research-data sources themselves ship: OSF, the Smithsonian, the University of North Carolina, CASRAI,
Harvard Medical School and NNLM each describe only field-level elements, with no relationships section, no
validation-rule table and no formal sign-off chain
[[1]](#ref-1)[[3]](#ref-3)[[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7).

**Full** adds Dataset Metadata, Relationships, Validation Rules and Review and Sign-off. This matches
Docsie's own shipped template, which carries a metadata header, a relationships section, a validation
section and a sign-off block beyond the basic owner-and-cadence fields lean already carries
[[17]](#ref-17). No source read for this bundle states a rule for when a team should move from one shape
to the other; the match between the lean/full split and what each group of sources actually ships is this
library's own observation, not a sizing threshold any source states, and the template leaves the choice to
the author.

---

## 5. Methodology lineage

The research behind this bundle spans research-data management, enterprise data governance,
documentation-as-code and product analytics, not named delivery methodologies, so this companion makes no
claim about how any delivery methodology treats a data dictionary.

What the research does support are four distinct lineages, each attributable to the sources that carry it:

- **Research data management**, the academic reproducibility tradition. OSF, the Smithsonian, the
  University of North Carolina, CASRAI, Harvard Medical School, NNLM, Temple University and the National
  Institute of Mental Health all write from this tradition, where the document exists so that a reader
  other than the person who collected the data can interpret it correctly
  [[1]](#ref-1)[[3]](#ref-3)[[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7)[[30]](#ref-30)[[32]](#ref-32).
- **Enterprise data governance**, the tradition that distinguishes a dictionary from a business glossary
  and a data catalog. GOV.UK's Data Architecture Community, Atlan and Actian each write from this
  tradition, and Analytics8 writes against it, nesting the dictionary inside the glossary instead
  [[9]](#ref-9)[[14]](#ref-14)[[15]](#ref-15)[[16]](#ref-16). Section 6, item 4, states the disagreement
  directly.
- **Documentation as code**, the software-engineering tradition that keeps a field's description beside
  the code that produces it rather than in a separate signed document. dbt's own product documentation and
  a practitioner newsletter both write from this tradition [[20]](#ref-20)[[35]](#ref-35).
- **Product analytics**, the tradition that uses this bundle's own name for a different document, the
  event-and-property catalog. Mixpanel, Amplitude and RudderStack each write from this tradition
  [[21]](#ref-21)[[22]](#ref-22)[[24]](#ref-24)[[27]](#ref-27); this bundle routes a reader from that
  tradition to `tracking-plan` rather than building its sense.

One standards-body thread runs alongside these four rather than inside any one of them: ISO/IEC 11179's
registration and naming obligations [[11]](#ref-11), the DDI Alliance's sentinel-value modeling
[[42]](#ref-42) and the Open Contracting Data Standard's deprecation rule [[43]](#ref-43) each formalize one
piece of what this bundle's Field Definitions section asks an author to do by hand.

---

## 6. Debates and contested boundaries

1. **Whether a data dictionary is written before or after the data is collected.** Sources disagree
   outright. Before: the National Institute of Mental Health treats "data collection instruments (also
   known as data dictionaries)" as structures "awardees are expected to use for new data collection"
   [[30]](#ref-30), and Temple University defines one as "a record of each variable and data field that
   you are going to collect in your project" [[32]](#ref-32). After: CASRAI defines one as a document that
   "defines every variable in a dataset" [[5]](#ref-5), and Buchanan et al. run their own worked pipeline
   "from source data (e.g., survey answers on Qualtrics) to an openly shared dataset accompanied by a data
   dictionary or codebook" [[2]](#ref-2). Phillips et al. place the data dictionary as the tenth of ten
   steps in their own framework, but the same paper states that its steps overlap, "Generation steps often
   occur concurrently with one another (e.g., data cleaning and quality assurance)." [[34]](#ref-34), so
   this is sequence evidence, not a stated rule, and this companion does not call it the final step without
   that caveat. **No source states timing as what defines the document**, which is why this bundle draws
   its own boundary against `tracking-plan` on subject instead. `tracking-plan`'s own shipped companion
   still draws that boundary on tense, following Wizbrand's own account, "A tracking plan describes what
   you intend to track (events, triggers, parameters) and why." against "A Data Dictionary documents what
   the data means and how it is structured once implemented." [[18]](#ref-18). Both statements are true of
   their own sources; they are not the same claim, and a reader comparing the two companions should read
   this one as the newer reasoning, not a contradiction to resolve.
2. **Whether a data dictionary carries metric formulas.** This is a **POSITION**, not a settled reading of
   the sources. Wizbrand's own key-components list includes "Calculation logic (for metrics): Formulas and
   inclusion/exclusion rules" [[18]](#ref-18), and Mixpanel's own Lexicon page states that it "documents
   your saved metrics and Formulas" [[21]](#ref-21), though in the event-list sense. Against them, Basedash
   separates the dictionary from "The metrics layer on top of tables" [[19]](#ref-19), and dbt's own
   Semantic Layer exists to "centrally define business metrics" apart from the tools that consume them
   [[28]](#ref-28). This bundle takes the second reading: a data dictionary documents what a field means,
   and `kpi-dashboard`'s own Metric Definitions section locks a derived metric's formula, inclusions,
   exclusions, owner and steward. A reader who wants a metric's formula is routed to `kpi-dashboard`, not
   handed a formula column here.
3. **Codebook or data dictionary.** CASRAI calls the data dictionary "typically the narrower, more
   mechanical artifact" against a fuller codebook [[5]](#ref-5). NNLM states the reverse for REDCap
   specifically, where "the data dictionary can contain more information about the structure of a database"
   than the codebook [[7]](#ref-7). The University of North Carolina and Harvard Medical School both treat
   the names as synonyms [[4]](#ref-4)[[6]](#ref-6), and Buchanan et al. contrast them by subject, survey
   data against file structure, while adding that "and sometimes these terms are used interchangeably"
   [[2]](#ref-2). The University of North Carolina's own summary holds across all of this: "There is no
   single standard" [[4]](#ref-4). This bundle uses the name data dictionary and names codebook as the
   common synonym in research settings, without ranking the two.
4. **Dictionary, glossary and catalog: siblings or a hierarchy.** GOV.UK's Data Architecture Community,
   Atlan and Actian each treat the three as separate, related artifacts, and GOV.UK's own page records the
   confusion directly in its own "COMMON MISUNDERSTANDINGS" field [[9]](#ref-9)[[14]](#ref-14)[[15]](#ref-15).
   Analytics8 nests them instead: "A data dictionary is a subset of a business glossary, but both are
   required to build a data catalog." [[16]](#ref-16). Atlan and Actian each sell a catalog product, and
   Atlan's own framing positions the dictionary as the narrowest of the three [[14]](#ref-14). Wikipedia's
   own dictionary-versus-catalogue distinction is a different boundary, about coupling to the database
   engine rather than about governance scope, and must not be read as the same line [[10]](#ref-10). This
   bundle builds neither a glossary nor a catalog, and names both only to keep their jobs out of it.
5. **A signed-off document, or metadata kept beside the code.** Docsie's own template is a dated document
   with a metadata header and a "Preparer", "Reviewer" and "Approver" sign-off block [[17]](#ref-17).
   Basedash argues instead for keeping definitions wherever people already work and tying updates to schema
   changes [[19]](#ref-19), and dbt instructs a team to add column descriptions "to the same YAML files
   where you declare data tests" [[20]](#ref-20), with no version, date or sign-off field on that page. This
   bundle templates the
   document form and names documentation as code as a place many teams keep the same content, without
   ranking the two.
6. **Who owns it: three camps.** The producing team: Atlan's own drift-prevention guidance states
   "Ownership should follow the data production hierarchy: the team that creates or maintains a dataset
   owns its documentation." [[36]](#ref-36), matching Basedash's own default [[19]](#ref-19) and Nazabal et
   al.'s and Phillips et al.'s described normal practice [[33]](#ref-33)[[34]](#ref-34). The consumer, by
   default rather than by design: when the producer's documentation is absent, Nazabal et al. state that
   the data scientist "is not uncommon that this metadata is missing or out-of-date, making it necessary to
   infer it from the data itself" [[33]](#ref-33). A governance role that coordinates rather than authors:
   Arovy's own list of "Ideal owners (depending on your org):" names a "COE or Data Governance Lead", a
   "Salesforce Admin or RevOps lead" or a "Business Systems lead" [[39]](#ref-39), and Wizbrand splits
   ownership by content, naming marketing operations or analytics leadership for KPI definitions and
   engineering for schema accuracy [[18]](#ref-18). This bundle's own Ownership and Review section asks for
   a named owner per table and does not adjudicate among the three camps.
7. **Whether the data dictionary is obsolete.** Craig Mullins states the term "is no longer in vogue" and
   argues that an automated data catalog's own discovery fixes the hand-maintained dictionary's central
   failure [[37]](#ref-37). Monte Carlo names the same staleness problem and reaches the opposite
   conclusion: "data dictionaries often feed into data catalogs." [[38]](#ref-38), and that most
   organizations need both rather than one replacing the other. Both sources are commercially adjacent to a
   catalog product, and neither is a primary source, so this bundle treats the question as contested, not
   settled, and does not claim that a catalog has replaced the dictionary, or that it has not.
8. **The product-analytics label belongs to Mixpanel.** Mixpanel calls an import from Segment Protocols and
   from Avo "a data dictionary" [[21]](#ref-21); Segment's own page calls its artifact "A Tracking Plan" and
   "a data spec" [[25]](#ref-25), and Avo's own documentation never uses that name at all
   [[26]](#ref-26). This companion reads the label as Mixpanel's own usage, which is why Purpose and
   Boundary routes a reader who means the event list to `tracking-plan` directly.
9. **Review cadence has no fixed norm.** Docsie's own template offers a choice rather than a single answer,
   "[Monthly / Quarterly / Annual / Event-based]" [[17]](#ref-17). Wizbrand says review "on a cadence
   (monthly or quarterly)" [[18]](#ref-18). Basedash says update on every schema change, plus "a short
   quarterly review" [[19]](#ref-19). Atlan says weekly for high-change assets and monthly for stable tables
   [[36]](#ref-36), and Arovy says monthly, "or every two weeks if your org changes fast" [[39]](#ref-39).
   The sources agree on two mechanisms, a change trigger and a calendar trigger, and disagree on the
   interval. Ownership and Review asks the author to name both and to say whether the interval is borrowed
   or the team's own.
10. **Time-bound sources.** dbt's own Semantic Layer announcement is a launch post whose free-preview terms
    were promotional and time-bound at the time it was read [[28]](#ref-28). Mixpanel, Amplitude, Segment,
    Avo and dbt's documentation pages are product documentation that changes with the product
    [[20]](#ref-20)[[21]](#ref-21)[[22]](#ref-22)[[25]](#ref-25)[[26]](#ref-26). The Census Bureau's own
    documented API limitation describes that API's own state at the time it was read [[44]](#ref-44).

---

## 7. Anti-patterns and failure modes

No source read for this bundle measured how often a real data dictionary fails, or how often keeping one
prevents a failure; what follows is a named, sourced list of the shapes failure takes, not a frequency
claim.

- **It goes stale.** The most fully sourced failure mode in this research. A practitioner newsletter states
  it bluntly: "It's outdated. No one uses it." [[35]](#ref-35). Nazabal et al. name the same drift in
  general terms, metadata "missing or out-of-date" [[33]](#ref-33), and Monte Carlo, Atlan and Arovy each
  describe the same mechanism from their own angle
  [[38]](#ref-38)[[36]](#ref-36)[[39]](#ref-39).
- **It lists names without meanings.** CASRAI names this directly as the specific failure Field Definitions
  exists to prevent: a tab of column headers "is not a data dictionary under this definition - it is a
  header list." [[5]](#ref-5).
- **Its definitions are circular, or its names are cryptic.** OSF's own counterexample names the first
  [[1]](#ref-1); Basedash names the second and its downstream cost, a reader who "will guess, and guesses
  produce confidently wrong numbers." [[19]](#ref-19).
- **It leaves the grain unstated.** Basedash calls an unstated grain "the most common source of
  double-counted metrics" [[19]](#ref-19); this companion states that as Basedash's own claim, not as a
  measured rate, and names no other source that measured it.
- **A known defect goes undiscovered until a reader hits it.** The Census Bureau's own API guide documents
  a specific formatting defect rather than leaving a user to find it unannounced [[44]](#ref-44); Basedash's
  own "Gotchas that cause wrong queries" column exists for the same reason, stated at the field level
  [[19]](#ref-19).
- **New readers misread the data without it.** Read et al. report, from a single clinical-research project
  that merged datasets from paper forms, that "the lack of a data dictionary combined with unclear
  variable names created the possibility for new study staff to misinterpret the data." [[40]](#ref-40).
  That is one project's own qualitative account, not a measured rate, and this companion names it as such.

---

## 8. Relationships to other artifacts

**Data dictionary vs the tracking plan.** Drawn on subject, not on which document is written first: a
tracking plan specifies the events and properties a product emits; a data dictionary documents what the
fields of a dataset or table mean, once those events and properties land somewhere. No source read
connects a data dictionary's own field-meaning job to specifying what a product will emit, and no
tracking-plan source read describes that document as explaining what a field means once it lands. Section
6, item 1, states this fully, including why this bundle's own reasoning differs from the tense-based line
`tracking-plan`'s own shipped companion still carries.

**Data dictionary vs the KPI dashboard's own Metric Definitions section.** A data dictionary documents what
a field means, its name, type, allowed values and where it lives; the Metric Definitions section locks a
derived, computed metric's own formula, inclusions, exclusions, grain, owner and data steward. This is a
**POSITION**, stated in full in section 6, item 2, against three sources that place calculation logic
inside a data dictionary. A source stating that a data dictionary itself locks a metric's formula,
inclusions or exclusions would contradict this layering, and this companion names the sources that already
come closest to saying so rather than treating the line as uncontested.

**A business glossary and a data catalog are named, related concepts this library does not build.** GOV.UK's
Data Architecture Community's own glossary distinguishes all three: a Business Glossary is "A repository of
approved, governed and maintained compendium of business term names, their definitions" [[9]](#ref-9), a
Data Catalogue is "An inventory of available data assets supported by a collection of metadata"
[[9]](#ref-9), and a Data Dictionary's own content "is usually extracted from the database or modelling
tool" [[9]](#ref-9). This bundle builds none of the other two, and names them only so a reader reaching for
glossary or catalog language does not fold a different document's job into this one.

**Data dictionary vs risk-register, raid-log, issue-log and change-log.** **POSITION**, stated for
completeness because the `governance-docs` family contract requires every member to state its position
against every other member. No source read for this bundle connects a data dictionary's field-meaning job
to tracking a risk, a RAID quadrant, a resolved issue or a baseline change request, and this bundle's own
research names no finding that would place any of that content inside a data dictionary.

---

## 9. Adaptations

- **A single small table.** The lean variant, with no relationships to state and no formal sign-off chain,
  matches what every research-data source in this research ships for a single dataset
  [[1]](#ref-1)[[3]](#ref-3)[[4]](#ref-4)[[5]](#ref-5)[[6]](#ref-6)[[7]](#ref-7).
- **Several related tables, or a dataset several teams rely on.** The full variant's Dataset Metadata,
  Relationships, Validation Rules and Review and Sign-off sections, matching Docsie's own fuller shipped
  shape, are sized for this case [[17]](#ref-17).
- **A team already on documentation as code.** Section 6, item 5, and the Validation Rules anatomy both
  name dbt's own `description` key and column tests as a place the same content can live beside the model
  that produces it, instead of, or alongside, this document [[20]](#ref-20).
- **A regulated or high-change dataset.** Atlan's own change-velocity SLA, weekly for high-change assets
  and monthly for stable ones [[36]](#ref-36), and Arovy's own accelerated cadence, "every two weeks if
  your org changes fast" [[39]](#ref-39), are the sourced models for a team that wants the Ownership and
  Review section's own review trigger enforced more tightly than the calendar default.
- **A research-data setting with an existing codebook.** Section 1 and section 6, item 3, both apply: this
  bundle's own template may serve as, or sit beside, an existing codebook, and the author should state
  which of the two names the team actually uses rather than maintain both under different headings.

---

## 10. Worked example

`data-dictionary_example.md` is the worked instance for this bundle, and it chains onto the same Acme
Analytics Reporting Platform Modernization program the library's other `governance-docs` examples share.
It documents the warehouse tables that sit between the events `tracking-plan_example.md` already catalogs
and the executive dashboard `kpi-dashboard_example.md` already defines: the fact table those ten events
land in, and the dimension tables its foreign keys point to. The research log fixes the facts it must
agree with rather than invent, including the event list, the two traits `analyst_segment` and
`migration_reconciled`, the hashed `recipient_user_id` column, and Lee Zhang as the table's own named
steward, and it must add a field-level fact beyond what either sibling already states, such as a table's
grain and key, a join, or which column holds one of Time to Insight's two timestamps, rather than restate
either sibling's own content under a new heading. Its own date and version history, in the full variant's
Review and Sign-off section, follow `tracking-plan_example.md`'s 2026-08-24 date, so the two examples agree
on when this document starts existing.

---

## References

<a id="ref-1"></a>[1] Center for Open Science (OSF Support). "[How to Make a Data Dictionary](https://help.osf.io/hc/en-us/articles/360019739054-How-to-Make-a-Data-Dictionary)."
help.osf.io (accessed 2026-10-15). The field-meaning definition, the element list in OSF's own order, the
genus-differentia form for a good definition and its circular counterexample, and the CC0 licence
statement. [practitioner]

<a id="ref-2"></a>[2] Buchanan, Crain, Cunningham, Johnson, Stash, Papadatou-Pastou, Isager, Carlsson and
Aczel. "[Getting Started Creating Data Dictionaries: How to Create a Shareable Dataset](https://osf.io/download/5ce2f5022a50c400197a8e09/)."
OSF preprint, 2021 (accessed 2026-10-15). The data-dictionary-versus-codebook distinction, the
interchangeable-terms observation, and the tool-generated production mechanism. [practitioner]

<a id="ref-3"></a>[3] Smithsonian Libraries and Archives. "[Describing Your Data: Data Dictionaries](https://library.si.edu/research/describing-your-data-data-dictionaries)."
library.si.edu (accessed 2026-10-15). The definition as distinct from a descriptive metadata record, and
the required-element list it names for a field entry. [practitioner]

<a id="ref-4"></a>[4] University of North Carolina at Chapel Hill, Research Data Management Core.
"[RDMC Data Management Guide: Documentation - Codebook](https://tdx.unc.edu/TDClient/33/Portal/KB/ArticleDet?ID=443)."
tdx.unc.edu (accessed 2026-10-15). The codebook-and-dictionary-as-synonyms treatment, the ordered element
list, the worked coded-value row, the "no single standard" statement, and the CC BY-NC 4.0 licence.
[practitioner]

<a id="ref-5"></a>[5] CASRAI Editorial Board. "[Data Dictionary in Research Data Management: Definition,
Components, and How It Differs from a Codebook](https://casrai.org/guides/data-dictionary-research-data-management)."
casrai.org (accessed 2026-10-15). The fullest definition, the sharpest drawn distinction among dictionary,
codebook and dataset-level metadata, the seven-question minimum-element list, the header-list
counterexample, and the CC-BY 4.0 licence. [primary]

<a id="ref-6"></a>[6] Harvard Medical School, Research Data Management. "[Data Management Terminology](https://datamanagement.hms.harvard.edu/about/data-management-terminology)."
datamanagement.hms.harvard.edu (accessed 2026-10-15). A short glossary definition that uses "data
dictionary" and "data codebook" as the same term. [practitioner]

<a id="ref-7"></a>[7] NNLM (Network of the National Library of Medicine), National Center for Data
Services. "[Data Dictionary](https://nnlm.gov/guides/data-glossary/data-dictionary)." nnlm.gov (accessed
2026-10-15). The definition, and the REDCap case where codebook and data dictionary carry opposite levels
of structural detail. [practitioner]

<a id="ref-8"></a>[8] District of Columbia Office of the Chief Technology Officer. "[Open Data Dictionary
Template Individual](https://catalog.data.gov/dataset/open-data-dictionary-template-individual)."
catalog.data.gov (accessed 2026-10-15). What the template is for, and its CC BY 4.0 licence; this catalog
record does not itself print the template's column headings. [primary]

<a id="ref-9"></a>[9] GOV.UK Data Architecture Community (GDAC). "[Business Glossaries & Definitions](https://dataarchitecture.blog.gov.uk/wp-content/uploads/sites/220/2020/06/GDAC_Business_Glossaries_Definitions_2020-1.pdf)."
dataarchitecture.blog.gov.uk, 2020 (accessed 2026-10-15). The three-way boundary between dictionary,
glossary and catalogue, and its own "COMMON MISUNDERSTANDINGS" field naming the confusion directly.
[primary]

<a id="ref-10"></a>[10] Wikipedia. "[Data dictionary](https://en.wikipedia.org/wiki/Data_dictionary)."
en.wikipedia.org (accessed 2026-10-15). Names the document, DBMS-component, middleware, and active-versus-
passive senses of the term, and the dictionary-versus-catalogue boundary drawn on coupling to the database
engine; CC BY-SA 4.0. [practitioner]

<a id="ref-11"></a>[11] Wikipedia. "[ISO/IEC 11179](https://en.wikipedia.org/wiki/ISO/IEC_11179)."
en.wikipedia.org (accessed 2026-10-15). A description of the standard, not its own text: the naming,
definition, registration and value-domain obligations it places on a data element; CC BY-SA 4.0.
[practitioner]

<a id="ref-12"></a>[12] Oracle. "[Database Concepts - The Data Dictionary](https://docs.oracle.com/cd/B19306_01/server.102/b14220/datadict.htm)."
docs.oracle.com (accessed 2026-10-15). The DBMS-internal, system-catalog sense of the term, named
explicitly; this bundle scopes that sense out. [vendor]

<a id="ref-13"></a>[13] Dataedo. "[ER diagram vs data dictionary](https://dataedo.com/blog/er-diagram-vs-data-dictionary-documenting-data-models)."
dataedo.com blog (accessed 2026-10-15). A field entry's content, including a list of values, default
values and an owner, in the vendor's own field-meaning sense. [vendor]

<a id="ref-14"></a>[14] Atlan. "[Data Catalog vs. Data Dictionary](https://www.atlan.com/data-catalog-vs-data-dictionary/)."
atlan.com (accessed 2026-10-15). The three-way boundary between dictionary, catalog and glossary, framed
from the vendor's own catalog-product perspective. [vendor]

<a id="ref-15"></a>[15] Actian. "[Business Glossary, Data Catalog, and Data Dictionary](https://www.actian.com/blog/data-intelligence/the-guide-to-understanding-the-difference-between-a-business-glossary-a-data-catalog-and-a-data-dictionary/)."
actian.com (accessed 2026-10-15). The same three-way boundary, framing all three as complementary tools,
and a field entry's content including ownership. [vendor]

<a id="ref-16"></a>[16] Analytics8. "[Data Dictionary vs. Data Catalog vs. Business Glossary](https://analytics8.com/blog/data-dictionary-vs-data-catalog-vs-business-glossary)."
analytics8.com blog (accessed 2026-10-15). Nests the dictionary inside the glossary rather than treating
the three as siblings, and places measure names and their calculations inside the dictionary, the wider
framing this bundle's own layering declines. [vendor]

<a id="ref-17"></a>[17] Docsie. "[Free Data Dictionary Template](https://www.docsie.io/solutions/templates/data-ai-analytics/data-dictionary/)."
docsie.io (accessed 2026-10-15). The fullest shipped section list and field-table column guidance: dataset
metadata header, relationships, validation rules, ownership and review, and a sign-off block. [vendor]

<a id="ref-18"></a>[18] Wizbrand. "[Data Dictionary: What It Is, Key Features, Benefits, Use Cases, and How
It Fits in Analytics](https://www.wizbrand.com/tutorials/data-dictionary/)." wizbrand.com, 2026 (accessed
2026-10-15). The key-components list, including calculation logic, the ownership-and-cadence guidance, and
the tense-based distinction against a tracking plan. [practitioner]

<a id="ref-19"></a>[19] Basedash (Max Musing). "[What is a data dictionary, and how to build one for
analytics](https://www.basedash.com/blog/what-is-a-data-dictionary-and-how-to-build-one-for-analytics)."
basedash.com blog, 2026 (accessed 2026-10-15). The field attribute list, the table-level grain and
relationships framing, the ownership default, the review-cadence guidance, and the good-versus-weak
definition contrast. [vendor]

<a id="ref-20"></a>[20] dbt Developer Hub. "[About documentation](https://docs.getdbt.com/docs/collaborate/documentation)."
docs.getdbt.com (accessed 2026-10-15). The documentation-as-code mechanism, the `description` key beside
column tests, and undocumented-column detection. [vendor]

<a id="ref-21"></a>[21] Mixpanel. "[Lexicon](https://docs.mixpanel.com/docs/data-governance/lexicon)."
docs.mixpanel.com (accessed 2026-10-15). Mixpanel's own name for its event-and-property catalog, "a data
dictionary"; also documents saved-metric formulas and a sensitive-data flag inside the same artifact.
[vendor]

<a id="ref-22"></a>[22] Amplitude. "[Event and property descriptions](https://amplitude.com/docs/en/data/event-property-descriptions)."
amplitude.com (accessed 2026-10-15). Amplitude's own definition of a data dictionary as an uploaded
taxonomy document, the event-list sense. [vendor]

<a id="ref-24"></a>[24] Amplitude Blog (Kate Adams). "[5 steps to become more comfortable using data](https://www.amplitude.com/blog/5-steps-to-become-more-comfortable-using-data)."
amplitude.com blog (accessed 2026-10-15). A second Amplitude-authored use of "Data Dictionary" for an
events-and-actions list, confirming the event-list sense recurs within the vendor's own content. [vendor]

<a id="ref-25"></a>[25] Twilio Segment. "[Protocols Tracking Plan](https://www.twilio.com/docs/segment/protocols/tracking-plan/)."
twilio.com (accessed 2026-10-15). Segment's own term for its events-and-properties spec is "Tracking Plan"
or "a data spec"; this page never uses the other name at all. [vendor]

<a id="ref-26"></a>[26] Avo. "[Properties](https://avo.app/docs/workspace/tracking-plan/properties)."
avo.app (accessed 2026-10-15). Avo's own PII-status property field; its own page never uses the term "data
dictionary" either. [vendor]

<a id="ref-27"></a>[27] RudderStack. "[Behavioral Data Collection Best Practices](https://www.rudderstack.com/assets/behavioral_data_collection_best_practices_whitepaper.pdf)."
rudderstack.com, PDF whitepaper (accessed 2026-10-15). Names "Data dictionary/solution design document" as
one output of a single tracking-plan process, the event-list sense. [vendor]

<a id="ref-28"></a>[28] dbt Labs. "[dbt Labs Launches the dbt Semantic Layer](https://www.getdbt.com/blog/dbt-labs-launches-the-dbt-semantic-layer-enabling-greater-consistency-across-analytics-tools)."
getdbt.com blog (accessed 2026-10-15). States the Semantic Layer's job as centralizing metric definitions
away from downstream tools; a launch announcement whose preview terms were time-bound when read. [vendor]

<a id="ref-30"></a>[30] National Institute of Mental Health (NIMH). "[NIMH Data Management and Sharing for
Applicants and Awardees](https://www.nimh.nih.gov/funding/managing-your-grant/nimh-data-management-and-sharing-for-applicants-and-awardees)."
nimh.nih.gov (accessed 2026-10-15). Names "data collection instruments (also known as data dictionaries)"
as a forward-looking, before-collection artifact. [primary]

<a id="ref-31"></a>[31] NIMH Data Archive (NDA). "[Data Dictionary](https://nda.nih.gov/data_dictionary.html)."
nda.nih.gov (accessed 2026-10-15). The deprecation mechanism a shared, centrally governed dictionary uses:
individual structures marked obsolete and superseded rather than deleted. [primary]

<a id="ref-32"></a>[32] Temple University Libraries. "[Managing Your Data](https://guides.temple.edu/datamgmt/managingdata)."
guides.temple.edu (accessed 2026-10-15). The before-collection timing position: a record of the variables a
project is going to collect. [practitioner]

<a id="ref-33"></a>[33] Nazabal, Williams, Colavizza, Smith and Williams. "[Data Engineering for Data
Analytics: A Classification of the Issues, and Case Studies](https://arxiv.org/pdf/2004.12929)." arXiv
preprint, 2020 (accessed 2026-10-15). States the staleness problem in general terms and frames ownership
as a two-sided, unresolved split between the data's producer and its consumer. [practitioner]

<a id="ref-34"></a>[34] Phillips, Price, Forbes, Boulange, Mengersen, Reeves and Glauert. "[Guidelines for
the Generation of Analysis Ready Data: A Case Study](https://arxiv.org/pdf/2403.08127)." arXiv preprint,
2024 (accessed 2026-10-15). Places the data dictionary as the tenth of ten generation steps, and states
that the steps often overlap; a worked, named producer-creates, consumer-reads ownership split.
[practitioner]

<a id="ref-35"></a>[35] Deep Chatterjee. "[No One's Reading Your Data Dictionary](https://data-comeback.beehiiv.com/p/no-one-s-reading-your-data-dictionary)."
data-comeback.beehiiv.com, Data Comeback newsletter, 2025 (accessed 2026-10-15). States the staleness
problem bluntly and prescribes the documentation-as-code fix. [practitioner]

<a id="ref-36"></a>[36] Atlan. "[Documentation Drift Prevention: Strategies That Work in 2026](https://atlan.com/know/documentation-drift-prevention-strategies/)."
atlan.com (accessed 2026-10-15). Names the staleness mechanism precisely, states an ownership rule tied to
the data production hierarchy, and a change-velocity review SLA. [vendor]

<a id="ref-37"></a>[37] Craig S. Mullins. "[The Rise of the Data Catalog](https://www.dbta.com/Columns/DBA-Corner/The-Rise-of-the-Data-Catalog-135766.aspx)."
dbta.com, DBA Corner column (accessed 2026-10-15). Argues the term "is no longer in vogue" and that an
automated data catalog fixes the hand-maintained dictionary's central weakness. [practitioner]

<a id="ref-38"></a>[38] Monte Carlo. "[Data Catalog Vs. Data Dictionary: 5 Essential Differences](https://www.montecarlodata.com/blog-data-catalog-vs-data-dictionary/)."
montecarlodata.com blog (accessed 2026-10-15). Names the same staleness failure and concludes the
dictionary feeds into, rather than is replaced by, a data catalog. [vendor]

<a id="ref-39"></a>[39] Arovy. "[Why Most Salesforce Data Dictionaries Fail (And 3 Shortcuts That Actually
Work)](https://www.arovy.com/resources/blog/why-most-salesforce-data-dictionaries-fail-and-3-shortcuts-that-actually-work)."
arovy.com blog (accessed 2026-10-15). Argues for a single named accountable owner coordinating rather than
authoring every entry, and a recurring governance cadence as the fix for staleness. [vendor]

<a id="ref-40"></a>[40] Read, LaPolla, Tolea, Galvin and Surkis. "[Improving data collection, documentation,
and workflow in a dementia screening study](https://jmla.pitt.edu/ojs/jmla/article/view/221/347)." Journal
of the Medical Library Association, 105(2), 2017 (accessed 2026-10-15). A named case study reporting that
the absence of a data dictionary raised the risk that new staff would misread merged data. [practitioner]

<a id="ref-41"></a>[41] University of Zurich (UZH) University Library. "[How Good Research Data Management
Enables Reproducibility and Data Reuse: A Case Study of Clinical Trial Data](https://veranstaltungen.ub.uzh.ch/angebot/details/64824?culture=en)."
veranstaltungen.ub.uzh.ch, event abstract (accessed 2026-10-15). A datathon where five teams reproduced a
trial's primary results while listing a lack of complete data dictionaries among several challenges.
[practitioner]

<a id="ref-42"></a>[42] DDI Alliance. "[SentinelValueDomain](https://docs.ddialliance.org/DDI-CDI/1.0/model/FieldLevelDocumentation/DDICDILibrary/Classes/Representations/SentinelValueDomain.html)."
DDI-CDI 1.0 model documentation (accessed 2026-10-15). Models a sentinel or missing-value code as a
distinct documentation element, separate from a field's ordinary value domain. [primary]

<a id="ref-43"></a>[43] Open Contracting Partnership. "[Deprecation](https://standard.open-contracting.org/latest/en/governance/deprecation/)."
Open Contracting Data Standard governance documentation (accessed 2026-10-15). A structured,
machine-readable deprecation flag for a removed or renamed field, kept for a defined window before
removal. [primary]

<a id="ref-44"></a>[44] U.S. Census Bureau. "[Microdata API User Guide, Limitations, Contact Us & Appendix](https://www.census.gov/data/developers/guidance/microdata-api-user-guide.Limitations%2C_Contact_Us_%26_Appendix.html)."
census.gov (accessed 2026-10-15). Documents a known formatting defect at the level of a specific query,
separate from the normal field definition. [primary]

<a id="ref-45"></a>[45] DataDriven.io. "[Defining the Grain](https://datadriven.io/learn/data_modeling_dimensional/section/3)."
datadriven.io, dimensional modeling course (accessed 2026-10-15). Treats a table's grain as a required,
testable statement tied explicitly to its primary or unique key columns. [practitioner]

<a id="ref-46"></a>[46] UK Data Service (University of Essex). "[Documenting and contextualising your data](https://dam.ukdataservice.ac.uk/media/440277/documentingdata.pdf)."
dam.ukdataservice.ac.uk, training slide deck (accessed 2026-10-15). Separates variable-level documentation,
including missing values, from a distinct confidentiality and access-conditions category. [practitioner]
