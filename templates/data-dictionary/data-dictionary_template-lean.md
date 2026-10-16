---
title: "{{dataset_name}} Data Dictionary"
dataset: "{{dataset_name}}"
owner: "{{owner}}"
steward: "{{steward}}"
dictionary_version: "{{dictionary_version}}"
last_reviewed: "{{date}}"
status: "{{status}}"
doc_type: data-dictionary
size: lean
source_template: data-dictionary
source_template_version: 0.1.0
---

<!--
LEAN DATA DICTIONARY. The smallest data dictionary that is still a real one: what it covers and the two
neighboring documents it rules out, the load-bearing field table itself, and the table's own named owner
with a stated review trigger. Use it for a single small table, matching the shape the research-data
sources themselves ship: no relationships section, no separate validation table, and no formal sign-off
chain. To grow it into the full form (see data-dictionary_template-full.md), ADD sections; never rename or
reorder the ones below, because the full variant is a strict superset of this one.

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
   one table section also carries PRIORITY and ROW HINT.
2. Replace each {{placeholder}}. The Field Definitions table is the heart; every table it covers opens with
   one line stating its grain and the key column or columns that enforce it, before any field is listed.
   Repeat the grain line and the table once per table this document covers.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
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
