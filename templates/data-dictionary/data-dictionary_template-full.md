---
title: "{{dataset_name}} Data Dictionary"
dataset: "{{dataset_name}}"
owner: "{{owner}}"
steward: "{{steward}}"
dictionary_version: "{{dictionary_version}}"
last_reviewed: "{{date}}"
status: "{{status}}"
doc_type: data-dictionary
size: full
source_template: data-dictionary
source_template_version: 0.1.0
---

<!--
FULL DATA DICTIONARY. Everything in the lean variant, plus a dataset-level header ahead of the field table,
a place to state how a table's fields relate to other tables, a place to list cross-field and range checks
separately from the field table itself, and a formal sign-off record with a running version history. Use
it for several related tables, for a dataset several teams rely on, or for one that feeds a regulated
report, following Docsie's own fuller shipped shape: a metadata header, a relationships section, a
validation section, and a sign-off block beyond the basic owner-and-cadence fields the lean variant already
carries.

This is a STRICT SUPERSET of data-dictionary_template-lean.md: every lean section appears here in the same
relative order, under the same names. If you are growing from lean, insert Dataset Metadata before Field
Definitions; insert Relationships and Validation Rules after Field Definitions and before Ownership and
Review; and append Review and Sign-off last.

WHAT A DATA DICTIONARY IS. CASRAI states the job in full: "A data dictionary is a structured document,
table, or file that defines every variable in a dataset - its name, meaning, data type, unit of
measurement, allowed values, and any coding scheme used to represent those values - so that anyone other
than the person who collected the data can interpret it correctly." OSF puts the same job more plainly:
"The purpose of a data dictionary is to explain what all the variable names and values in your spreadsheet
really mean." It is a standing reference, revised as the schema changes, not a one-time record filed once
and archived. In research settings this same document is often called a codebook; sources disagree on
which name is the narrower one, and this template does not rank the two. See data-dictionary_companion.md
section 1 and section 6, item 3.

IT IS NOT THE EVENT LIST, AND IT DOES NOT LOCK A METRIC'S FORMULA. Product-analytics vendors use this
template's own name for a catalog of a product's events and their properties; Mixpanel's own Lexicon page
states, "Lexicon is a data dictionary that stores descriptions of events and their properties." That
document is the tracking plan's job, drawn on subject rather than on which document is written first: a
tracking plan specifies the events and properties a product emits, and this document describes what the
fields of a dataset or table mean once those events and properties land somewhere. Separately, this
document does not lock a derived metric's own formula, inclusions, or exclusions; that is the KPI
dashboard's own Metric Definitions section. This second boundary is this library's own position against
three sources that place calculation logic inside a data dictionary, not a settled reading every source
shares. See data-dictionary_companion.md section 1, section 3 (Purpose and Boundary), section 6 (items 1,
2, and 8), and section 8.

NO SOURCE READ FOR THIS BUNDLE MEASURED WHETHER HAVING ONE CHANGES AN OUTCOME. What exists is one
qualitative case study of a clinical-research project that lacked one, reporting that the absence "created
the possibility for new study staff to misinterpret the data," and one datathon event abstract that names
incomplete data dictionaries among several reproduction challenges while every team still reproduced the
trial's results. Neither is a measured effect, and this template's reason to exist rests on named failure
modes, not on a measurement. See data-dictionary_companion.md section 1 and section 7.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP; the
   four table sections also carry PRIORITY and ROW HINT.
2. Replace each {{placeholder}}. The Field Definitions table is the heart; every table it covers opens with
   one line stating its grain and the key column or columns that enforce it, before any field is listed.
   Repeat the grain line and the table once per table this document covers.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it. Relationships and
   Validation Rules in particular may be "N/A, this dataset is a single table with no foreign keys and no
   cross-field rules beyond the allowed values already stated" for a small dataset.
4. This document is never finished, but before you share it: self-grade against data-dictionary_guide.md,
   then DELETE every HTML comment. They are guidance, not content.
-->

# {{dataset_name}} Data Dictionary

## Purpose and Boundary

<!-- WHAT  A short statement of which dataset's or table's fields this document covers, and what it rules
           out by name.
     WHY   The name this document carries is overloaded, so the first job of this section is to rule the
           other senses out before the field table starts. It excludes event cataloguing: Mixpanel's own
           Lexicon page states, "Lexicon is a data dictionary that stores descriptions of events and their
           properties," using this document's own name for a different document; that subject is the
           tracking plan's job, and a reader who means the event list is routed there. It excludes
           metric-formula locking: Basedash separates "The metrics layer on top of tables" from the
           field-level facts a dictionary carries, and dbt's own Semantic Layer exists specifically to
           "centrally define business metrics" apart from the tools that consume them; that subject is the
           KPI dashboard's own Metric Definitions section. The section also names codebook as the common
           synonym this type carries in research settings, without ranking the two terms against each
           other. Deep dive: data-dictionary_companion.md section 3 (Purpose and Boundary) and section 6
           (items 1, 2, 3, and 8).
     ASK   Which dataset or table, or which several related tables, does this document cover? What does it
           rule out by name: the event list another team already catalogs, and any metric's own formula?
           If your organization calls a document like this a codebook, does this template serve that job
           too, or does your team keep both under different names?
     GOOD  "This document covers the shipments and warehouses tables in Cedarbrook Fulfillment's
           operational warehouse. It does not catalog the events Cedarbrook's driver app emits; that
           catalog is the tracking plan's job. It does not lock the formula behind On-Time Delivery Rate;
           that formula lives in the KPI dashboard's own Metric Definitions section. Some teams at
           Cedarbrook call a document like this one a codebook; this one serves that job too."
     WEAK  "This describes our data." (names no table, rules out nothing, and a reader cannot tell this
           document from a business glossary or the tracking plan)
     TRAP  Letting a metric's formula, or an event's own trigger and business reason, creep into this
           document instead of staying in the KPI dashboard or the tracking plan, where each already
           belongs. -->

{{purpose_and_boundary}}

## Dataset Metadata

<!-- WHAT  A header naming the dataset or table, its source system, its version, and its effective date,
           ahead of the field table.
     WHY   A single small table needs little more than its field list, while several related tables need a
           header that says which system each one came from and when this version took effect. Docsie's
           own shipped document opens with exactly this header before its field table, asking the author to
           "Describe the dataset purpose, source systems, refresh cadence, and primary consumers." Basedash
           frames the same idea at the table level throughout, describing what a complete dictionary
           documents about a table beyond any single column. Deep dive: data-dictionary_companion.md
           section 3 (Dataset Metadata).
     ASK   What is this dataset or table's source system? What version of this document is this, and when
           did it take effect? How often does the underlying data refresh? Who are its primary consumers?
     GOOD  "Source system: Fulfillment Core, the warehouse management platform. Version 2.1, effective
           2026-09-01. Refreshes nightly at 02:00 UTC. Primary consumers: the fulfillment analytics team
           and the carrier-performance dashboard."
     WEAK  "This is our warehouse data." (no source system, no version, no effective date, and no consumer
           named)
     TRAP  Stating a version number with no effective date, so a reader cannot tell whether a field's
           definition below reflects the schema as it exists today or as it existed several releases ago. -->

**Source system(s):** {{source_system}}

**Version:** {{dictionary_version}}

**Effective date:** {{effective_date}}

**Refresh cadence:** {{refresh_cadence}}

**Primary consumers:** {{primary_consumers}}

## Field Definitions

<!-- WHAT  One row per field, naming its type and nullability, its meaning, its allowed values, its source,
           its sensitivity, and its owner. Repeat the grain line and the table once per table this document
           covers.
     WHY   This is the section every admitting source converges on, and the one a reader actually opens
           the document to find. Each table's entry opens with one line stating its grain, what one row
           represents, and the key that enforces it, following the dimensional-modeling rule that "The
           grain of a fact table states what 1 row means, and it is decided before any column is added,"
           and that "Naming the columns that enforce the unit is what lets another engineer write a test
           against it." Below the grain line, the columns are this library's own convergence across several
           sources, not any single vendor's whole list: Field, the technical column name; Type and
           nullability, paired the way Basedash pairs them, "Data type and nullability"; Definition, a
           plain-language sentence of what the value means, following OSF's "Definition of the variable"
           and CASRAI's "What does it measure or record?"; Allowed values, units and missing codes, sourced
           to the University of North Carolina's "including null or missing values," CASRAI's "How is
           missingness represented?," OSF's "Measurement units," and Basedash's "Enums, ranges, or units";
           Source, including how often it refreshes, sourced to CASRAI's "Where did this variable come
           from?" and Basedash's "Where the value originates"; Sensitivity, sourced to Basedash's "PII or
           restricted-data flag" and Avo's own property field, "The PII status of the property - whether it
           carries personally identifiable information"; and Owner, a person or team accountable for the
           field, sourced to Basedash's own "Person or team accountable for it." A missing or sentinel
           value is documented, not assumed: the DDI Alliance's own metadata model states, "Sentinel values
           are used for processing, not to describe subject matter." A field the schema has stopped using
           stays in the table rather than disappearing from it, with its replacement and removal date
           recorded in its own Definition cell, following the Open Contracting Data Standard's own
           deprecation rule, "Validation tools must report use of deprecated fields to the user," and the
           NIMH Data Archive's own practice of marking an entry "obsolete, superseded by newer structures"
           rather than deleting it. Deep dive: data-dictionary_companion.md section 3 (Field Definitions)
           and section 6, item 2.
     ASK   For each table: what is its grain, in one sentence, and what key column or columns enforce it?
           For each field: what is its name? Its type, and is it nullable? What does its value mean, in one
           plain sentence? What values, units, or missing codes are allowed? Where does it come from, and
           how current is it? Does it carry a sensitivity flag? Who is accountable for it?
     PRIORITY  Every table opens with a stated grain and key before any field is listed. A good definition
           follows a genus-differentia form, "A is a B that C"; a circular definition, naming the thing by
           itself, or a cryptic column name with no definition at all, fails this section outright.
     ROW HINT  A good row names the value's meaning in one plain sentence and states any known caveat in
           the same cell, such as an exclusion the column's name does not advertise. A weak row restates
           the column's own name as though that were a definition, or leaves the allowed-values cell blank.
     GOOD  Grain line: "Table: shipments. Grain: one row per shipment. Key: shipment_id enforces the
           grain." Row: | carrier_code | string, not null | The carrier that physically moved the shipment
           out of the warehouse; set once at dispatch and never changed afterward | Enum: ups, fedex, dhl,
           usps | Set by Fulfillment Core at dispatch | none | Fulfillment Eng |
     WEAK  Grain line: none stated. Row: | carrier_code | string | The carrier | | | | |
     TRAP  Writing a definition that only restates the column's own name ("carrier_code: the carrier
           code"), which CASRAI names directly as the failure this section exists to avoid: a tab of column
           headers with no definitions "is not a data dictionary under this definition - it is a header
           list." -->

**Table:** {{table_name}}

**Grain:** {{grain_statement}}

**Key column(s):** {{key_columns}}

| Field | Type and nullability | Definition | Allowed values, units, or missing codes | Source | Sensitivity | Owner |
|---|---|---|---|---|---|---|
| {{field_name}} | {{field_type_nullability}} | {{field_definition}} | {{field_allowed_values}} | {{field_source}} | {{field_sensitivity}} | {{field_owner}} |

## Relationships

<!-- WHAT  How this table's fields relate to other tables: foreign keys, joins, or a field computed from
           another table's field.
     WHY   A single table with no related tables has nothing to describe here, while several related
           tables need the joins stated somewhere. Docsie's own template asks the author to "Document
           primary keys, foreign keys, joins, and related datasets," and Harvard Medical School's own
           definition, "Outlines the structure, content, and variable definitions for a dataset or
           collection of data," reads naturally as more than one table in scope once relationships exist
           between them to describe. Deep dive: data-dictionary_companion.md section 3 (Relationships).
     ASK   Which field in this table is a foreign key into another table? What table and field does it
           point to? Is the relationship a straightforward foreign key, a join condition, or a field this
           table computes from another table's own field?
     PRIORITY  Name the exact field on each side of the relationship, not only the two table names; "joins
           to the warehouse table" with no field named is not a relationship statement a reviewer can test.
     ROW HINT  A good row names both fields and the relationship's kind (foreign key, join, or derived). A
           weak row names only the two tables and leaves the kind and the fields unstated.
     GOOD  | shipments.warehouse_id | warehouses.warehouse_id | Foreign key | Every shipment originates
           from exactly one warehouse |
     WEAK  | shipments | warehouses | related | |
     TRAP  Naming a relationship that exists only informally, through a shared naming convention, as though
           it were an enforced foreign key, when no constraint or documented join condition actually ties
           the two columns together. -->

| This field | Related table and field | Relationship | Notes |
|---|---|---|---|
| {{related_field}} | {{related_table_field}} | {{relationship_type}} | {{relationship_notes}} |

## Validation Rules

<!-- WHAT  Enum lists, numeric ranges, required-versus-optional fields, and any cross-field rule a loader or
           a reviewer should check, stated separately from the field table's own allowed-values cells.
     WHY   A small table's Field Definitions table already carries its allowed values, while a larger or
           more heavily consumed table benefits from stating the checks separately so a loader can test
           against them directly. Docsie's own template asks the author to "List accepted values, null
           handling, range checks, and uniqueness rules," and Basedash's own attribute list names the same
           content at the field level, "Enums, ranges, or units." dbt's own documentation-as-code mechanism
           offers a parallel, automated form of the same idea, a test declared beside the field's own
           description. Deep dive: data-dictionary_companion.md section 3 (Validation Rules).
     ASK   Which fields must be unique? Which are required rather than optional? What numeric range, if
           any, is valid? What cross-field rule, if any, must hold (for example, a status that constrains
           which other fields may be populated)?
     PRIORITY  State the rule as something a loader could actually run, not as prose a human must interpret
           differently each time; "shipment_id must be unique" is testable, "shipment IDs should make
           sense" is not.
     ROW HINT  A good row names the exact field and a rule specific enough to fail a real row against it. A
           weak row names a field with no rule, or a rule so general it would accept almost anything.
     GOOD  | shipment_id | Must be unique across the table |
     WEAK  | shipment_id | Should be correct |
     TRAP  Restating a field's allowed-values cell here word for word with no added rule, which duplicates
           the Field Definitions table instead of adding a check that table does not already state. -->

| Field | Rule |
|---|---|
| {{validation_field}} | {{validation_rule}} |

## Ownership and Review

<!-- WHAT  The table's own named owner and steward, apart from any individual field's own owner, and how
           the table is reviewed.
     WHY   An unowned, unreviewed dictionary is the staleness failure this bundle's own research names most
           often, and this section is where that failure is prevented. Basedash states the ownership
           default plainly, "Owners are usually the team that produces the data, not the team that consumes
           it." Docsie's own template asks the author to "Identify data owner, steward, support channel,
           and review cadence." No fixed interval is a norm across the sources: Docsie offers a choice
           rather than one answer, Wizbrand says monthly or quarterly, Basedash ties review to every schema
           change plus a short quarterly check, and Atlan ties review frequency to change velocity. This
           section asks the author to name an interval and to say whether it is borrowed or the team's own.
           The review trigger itself has two parts the sources agree on even where the interval disagrees:
           Basedash ties the first trigger directly to the change itself, "Update definitions whenever the
           schema changes, as part of the change itself rather than as a separate task," and Atlan states
           the second as a rule, "Review frequency depends on change velocity." Deep dive:
           data-dictionary_companion.md section 3 (Ownership and Review) and section 6, items 6 and 9.
     ASK   Who is this table's own named owner, apart from any individual field's own owner? Who is its
           steward? What is the support channel or process for proposing a change to a definition? What
           triggers a review, besides every schema change: what calendar interval, and is that interval
           borrowed from somewhere else or this team's own choice?
     GOOD  "Owned by Fulfillment Eng, the team that produces this data; stewarded by Priya Okafor. Propose
           a change in the #fulfillment-data channel. Reviewed on every schema change, plus a standing
           quarterly check; this quarterly interval is this team's own choice, not a sourced norm."
     WEAK  "Reviewed periodically by the data team." (no named owner, no steward, no interval, and nothing
           a reader could check the table against)
     TRAP  Naming an owner but no review trigger beyond "periodically," which leaves a reader with no way
           to tell whether the table is actually current or merely was current once. -->

**Table owner:** {{table_owner}}

**Table steward:** {{table_steward}}

**How to propose a change:** {{change_proposal_process}}

**Review interval:** {{review_interval}}

**Other review triggers:** {{review_triggers}}

## Review and Sign-off

<!-- WHAT  A formal record of who reviewed and approved this version, and when, apart from the Ownership
           and Review section's own standing owner and cadence, plus the running record of what changed,
           including each field's own deprecation.
     WHY   A small, informally maintained table needs no sign-off chain, while a dataset several teams rely
           on, or one that feeds a regulated report, benefits from a dated approval trail. Docsie's own
           shipped document carries exactly this beyond its basic owner-and-cadence fields, with
           "Preparer," "Reviewer," and "Approver" roles, a "Review Cycle," an "Effective Date," and a status
           field, "[Draft / In Review / Approved]." A field the schema has stopped using is marked rather
           than silently dropped: the NIMH Data Archive marks an entry "obsolete, superseded by newer
           structures," and this section's version history is where that marker, and its date, are
           recorded. Deep dive: data-dictionary_companion.md section 3 (Review and Sign-off).
     ASK   Who prepared this version? Who reviewed it, and who approved it? What review cycle does this
           version follow, and what is its status: Draft, In Review, or Approved? What is the running
           record of what changed, when, why, and who approved it, including when a field was deprecated?
     PRIORITY  Every version-history row names the field or table affected and the person who approved the
           change, not only that "something was updated." A deprecated field's row names its replacement,
           if one exists, and the date the deprecation took effect.
     ROW HINT  A good version-history row names the field, what changed about it (added, redefined,
           deprecated, removed), who approved it, and when. A weak row says "updated" with no field named
           and no approver.
     GOOD  "Preparer: Priya Okafor. Reviewer: the fulfillment data steward. Approver: the Fulfillment Eng
           lead. Review cycle: quarterly. Status: Approved." Version history row: | v2.1 | 2026-09-01 |
           carrier_code enum value "ontrac" removed, superseded by a direct carrier-API integration |
           Approved by the Fulfillment Eng lead |
     WEAK  Version history row: | v2.1 | | updated some fields | |
     TRAP  Marking a field deprecated with no replacement named and no removal date, leaving a reader with
           no way to tell whether the field is still safe to query against. -->

**Preparer:** {{preparer}}

**Reviewer:** {{reviewer}}

**Approver:** {{approver}}

**Review cycle:** {{review_cycle}}

**Status:** {{signoff_status}}

| Version | Date | What changed | Approved by |
|---|---|---|---|
| {{version_number}} | {{version_date}} | {{version_change_summary}} | {{version_approved_by}} |
