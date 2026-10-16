# data-dictionary: research log

Research conducted 2026-10-15, building on admission sweep 5 (2026-10-12), the prep research of 2026-10-14, and
the spec that merged on 2026-10-15 with ADR 0073 (data-dictionary joins governance-docs as a seventh member). The
build's seven-dimension fan-out covered the research-data-management canon, the enterprise sources and the several
senses of the term, the practitioner templates and documentation as code, the product-analytics sense and the metric
boundary, the debates over timing, upkeep, ownership and obsolescence, the library's own neighbours and the facts the
worked example must agree with, and the standing gap question. **46 sources are recorded below, all
fetched-and-verified**: 5 primary, 3 standards bodies, 18 practitioner and 20 vendor. Only `fetched-and-verified`
sources are quoted anywhere in this bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a retrieval tool
returns: pages as downloaded, and PDFs through a text extractor. One source refuses a plain download, so its text was
taken through a browser: the FastSlowMotion post [29]. The build's agents returned 311 quotations. Six belong to two
pages this log does not list, for the reasons the next section gives. Of the 305 for listed sources, 257 pass as
normalized substrings and 7 more pass once whitespace the extractor broke is ignored. Three quotations ran list or
table cells together and were split, keeping 13 passing parts. Twenty-six table rows that the agents returned as
joined cells were replaced with 22 cell-level strings, and twelve quotations that failed on rendering artifacts were
re-quoted as 23 shorter segments. Six quotations come from the FastSlowMotion browser excerpt, and five that the spec
and ADR 0073 rested on, which no agent returned, were re-read from raw text and added. **333 quotations remain.**

---

## What the checks caught, and what was not read

**Twelve quotations failed the raw-text check, for three different reasons.** Five failed because the raw text
carries an artifact that the agent's quotation rightly left out: zero-width spaces around in-text citations and a
running page header ("DATA DICTIONARY 5") inside two sentences of the Buchanan et al. preprint [2], PDF ligatures in
two sentences of Nazabal et al. [33], and a list bullet in the RudderStack whitepaper [27]. Six failed because the
agent added punctuation or formatting at a structural boundary that the raw text does not have: a colon at a table
cell on Segment's page [25] and on dbt's [20], a period at a heading in Chatterjee's newsletter [35], commas between
list items in two Arovy quotations [39], and backticks around a property name in the Open Contracting Data Standard
[43]. **One failed because the agent dropped a word**: Buchanan et al. wrote "We have also included detailed video
tutorials", and the agent's quotation omitted "also" [2]. None of the twelve changed a claim. All twelve were
re-quoted from the raw text, as 23 shorter segments.

**Two vendor tables came back as joined rows.** Docsie's template tables [17] and Basedash's attribute and comparison
tables [19] were returned row by row with their cells run together, which splitting turned into fragments such as
"Yes" and "[Monthly". All 26 joined rows were dropped and replaced with 22 cell-level strings checked against the same
raw text, so every table claim below rests on a cell, not on a reconstructed row.

**Five quotations the spec relied on had never been returned by this build's agents**, so they were re-read from raw
text rather than carried forward from the spec: Buchanan et al.'s pipeline sentence, "from source data (e.g., survey
answers on Qualtrics) to an openly shared dataset accompanied by a data dictionary or codebook" [2]; Basedash's
"Owners are usually the team that produces the data, not the team that consumes it" [19]; NIMH's "data structures that
awardees are expected to use for new data collection" [30]; and Phillips et al.'s ten-step list and its caveat [34].
All five pass.

**Phillips et al. list the data dictionary tenth, and say the steps overlap.** The paper's ten steps end with
"metadata, and data dictionary" [34], which the spec reads as "the tenth and final step". The same paper says
"Generation steps often occur concurrently with one another (e.g., data cleaning and quality assurance)." [34]. The
list position is sequence evidence that the dictionary is written from data already held, and it is weaker than "final
step" suggests. The companion must not call it the final step without that caveat.

**The OSF element list is now quoted, which settles one of the spec's risks.** The spec warned that OSF's seven-column
structure was "a retrieval note's own tally, not a passed quotation". The OSF help article [1] prints those elements as
its own headings, in its own order, and every one passes: "Variable names", "Readable variable name", "Measurement
units", "Allowed values", "Definition of the variable", "Synonyms for the variable name (optional)" and "Description
of the variable (optional)". The companion may cite [1] for that list directly.

**Two assigned URLs are not templates.** The OSF "download" URL serves the Buchanan et al. preprint, not a blank
template with printed column headings, and the log files the other Buchanan URL (`https://osf.io/vd4y3/`) under the
same entry [2]. The Data.gov page for the District of Columbia's template [8] is a catalog record that describes the
template in prose and links out to a page this research did not fetch, so it supports what the record says, not any
column list.

**Docsie's template disagrees with its own example.** Its guidance asks for "Field, Type, Required, Definition,
Example, and Notes" columns, and its worked "Customer Orders Data Dictionary" prints five of them, without Notes [17].
Neither is a canonical column set.

**FastSlowMotion [29] was read once, in a browser, as the spec reserved.** The quotations under [29] were checked
against a verbatim excerpt of the browser's extracted page text, not against a download, so they carry slightly less
assurance than the rest of the log. **Which of the spec's two outcomes holds: the first.** The page separates a full
metric entry, "A KPI dictionary entry per metric (1 page max)", from "A 'definition snippet' you can embed in
dashboards (tooltip/glossary)", and the full entry carries "definition, formula, inclusion/exclusion rules" [29].
That is what `kpi-dashboard`'s Metric Definitions section already carries. The page also lists a separate "source-of-
truth map (object/system → field → owner)" and calls its metric document a "KPI dictionary", not a data dictionary.
That corroborates the subject boundary at low weight, as the spec predicted; it settles nothing.

**What was assigned and not read, or read only in part:**

- **ISO/IEC 11179.** Paywalled. [11] is Wikipedia's description of the standard, not its text. It names the
  registration, naming and definition obligations on a data element and the value-domain concept. It names no "unit
  of measure" attribute. Nothing in this bundle may describe the standard's clause structure or attribute list beyond
  what [11] says.
- **The DAMA Dictionary of Data Management.** The assigned page is a sales page for the paid dictionary, so its entry
  for the term was not read and the page has no entry here.
- **Snowplow's tracking-design page.** The assigned URL now redirects to an "Event Studio" page that never uses the
  term. That is a null result for the product-analytics sense, recorded here, and the page has no entry.
- **One statistic surfaced in search and could not be verified.** A page attributing a "60% reduction in data
  interpretation errors" and "three weeks faster" onboarding to a 2024 DAMA International source returned HTTP 403 on
  every attempt, and no separate search found the underlying report. **Neither figure may appear anywhere in this
  bundle.**
- **Three practitioner pages on ownership and upkeep** (Control Engineering, Panoply and TDAN) returned a bot
  challenge or HTTP 403 to every fetch method tried. None is cited.
- **Gap-question leads not reached:** a UK Data Service page on units returned 404; SDMX 3.0's section on time
  formats was not fetched; the OMOP Common Data Model page failed on an expired certificate; and the national
  statistics offices tried (ONS, Statistics Canada, Eurostat) returned no operative text.
- **Navigation-only observations are not findings.** Avo's site navigation lists a "Metrics" item beside its
  tracking plan, and Amplitude's lists "Time to Live (TTL)". Neither page's body was read for either item, so this log
  claims nothing about either.

---

## The admission record

The spec's admission section stands, and this research adds to it. **The type admits on a literal downloadable
template**: Docsie publishes one [17], and the District of Columbia catalogs one under a CC BY 4.0 licence [8]. **It
is defined independently by research-data sources**: OSF [1], the Smithsonian [3], the University of North Carolina
[4], CASRAI [5], Harvard Medical School [6] and NNLM [7], and by the UK government's data architecture glossary [9].
OSF also publishes the element list as its own headings [1], under CC0.

**The sources use the name in three senses, and the bundle builds one.** The field-meaning sense, a document of what
a dataset's or table's fields mean, is this bundle's scope ([1], [5], [9], [17], [19]). The event-list sense, a
catalog of product events and their properties, is the tracking plan's subject, and Mixpanel [21], Amplitude [22],
[24] and RudderStack [27] use the name for it. The DBMS-internal sense, the read-only tables a database engine keeps
about its own objects, is Oracle's [12] and one of Wikipedia's listed meanings [10]; the bundle scopes it out.

---

## Claims flagged contested or time-bound

1. **Whether a data dictionary is written before or after the data is collected.** The sources disagree, and the
   disagreement is why ADR 0073 draws the tracking-plan boundary on subject rather than tense. Before: NIMH treats
   "data collection instruments (also known as data dictionaries)" as structures "awardees are expected to use for new
   data collection" [30], and Temple defines one as "a record of each variable and data field that you are going to
   collect in your project" [32]. After: CASRAI defines one as a document that "defines every variable in a dataset"
   [5], and Buchanan et al. run their pipeline "from source data ... to an openly shared dataset accompanied by a data
   dictionary or codebook" [2]. Nazabal et al. [33] and Phillips et al. [34] describe dictionaries built from data
   already held, which is sequence evidence, not a stated rule, and Phillips et al. say the steps overlap (see the
   section above). NIMH says the NIMH Data Archive's dictionary "is updated as researchers extend existing data
   collection instruments or create new instruments" [30], and the archive marks structures that are "obsolete,
   superseded by newer structures" [31], so a dictionary in that setting is written ahead of collection and revised
   after it. **No source states timing as what defines the
   document.** `tracking-plan`'s shipped templates and companion still draw this boundary on Wizbrand's tense line;
   the landing PR adds a dated note there rather than a rewrite.

2. **Whether a data dictionary carries metric formulas. The spec's falsifier is met, and the layering is the
   library's position.** The spec states that "a source stating that a data dictionary itself locks a metric's
   formula, inclusions, or exclusions would contradict this layering." Three sources say something close to that.
   Wizbrand lists "Calculation logic (for metrics): Formulas and inclusion/exclusion rules" among a data dictionary's
   key components [18]. Analytics8 says a data dictionary describes "measure names ... their calculations" [16].
   Mixpanel's Lexicon, which calls itself a data dictionary, "documents your saved metrics and Formulas" [21], though
   in the event-list sense. Against them, Basedash separates the dictionary from the semantic layer, "The metrics
   layer on top of tables" [19]; dbt's Semantic Layer exists to "centrally define business metrics" apart from
   downstream tools [28]; and FastSlowMotion keeps formulas in a "KPI dictionary" with a separate field-level map
   [29]. **ADR 0073's Considered Option 3 already weighed Wizbrand's calculation-logic language** and rejected the
   wider framing on duplication, because `kpi-dashboard`'s Metric Definitions section already ships the formula,
   inclusions, exclusions, owner and steward. That reasoning stands, and it is a reason about this library, not a
   finding about practice. **The companion must label the field-versus-formula layering a POSITION**, name the three
   sources that draw the line elsewhere, and route a reader who wants formulas to the KPI dashboard. The spec's
   Falsifier bullet takes a dated note at landing, and the build report names this finding for the maintainer.

3. **Codebook or data dictionary.** CASRAI calls the data dictionary "typically the narrower, more mechanical
   artifact" [5]. NNLM says the opposite for REDCap, where "the data dictionary can contain more information about
   the structure of a database" [7]. The University of North Carolina and Harvard Medical School treat the names as
   synonyms ([4], [6]); Buchanan et al. contrast them by subject, survey data against file structure, and add that
   "sometimes these terms are used interchangeably" [2]. UNC's summary holds: "There is no single standard." [4]. The
   bundle uses "data dictionary" and names "codebook" as the common synonym in research settings, without ranking the
   two.

4. **Dictionary, glossary and catalog: siblings or a hierarchy.** GDAC [9], Atlan [14] and Actian [15] treat the three
   as separate, related artifacts, and GDAC's entry records the confusion in its own "COMMON MISUNDERSTANDINGS" field.
   Analytics8 nests them instead: "A data dictionary is a subset of a business glossary, but both are required to
   build a data catalog." [16]. Atlan and Actian sell catalog products, and Atlan's framing positions the dictionary
   as the narrowest of the three. Wikipedia's dictionary-versus-catalogue distinction [10] is a different boundary,
   about coupling to the database engine, and must not be read as the governance one. The bundle builds neither a
   glossary nor a catalog and names both only to keep their jobs out of it.

5. **A signed-off document, or metadata kept beside the code.** Docsie's template is a dated document with a
   metadata header and a "Preparer", "Reviewer" and "Approver" sign-off block [17]. Basedash argues for keeping
   definitions wherever people already work and tying updates to schema changes [19], and dbt stores descriptions in
   "the same YAML files where you declare data tests" [20], with no version, date or sign-off field. The claim that dbt
   descriptions are "version-controlled with the code" is Basedash's description of dbt, not a statement on dbt's own
   page. The bundle templates the document, and the companion names documentation as code as the place many teams keep
   the same content, without ranking the two.

6. **Who owns it: three camps.** The producing team: Atlan's "Ownership should follow the data production hierarchy"
   [36], Basedash [19], Nazabal et al.'s normal case [33] and Phillips et al.'s practice [34]. The consumer, by default
   rather than design: when the producer's documentation is absent, the data scientist must "infer it from the data
   itself" [33]. A governance role that coordinates rather than authors: Arovy's "Ideal owners (depending on your
   org):" a "COE or Data Governance Lead", a "Salesforce Admin or RevOps lead" or a "Business Systems lead" [39].
   Wizbrand splits ownership by content, KPI definitions to analytics leadership and schema accuracy to engineering
   [18]. The bundle asks for a named owner per table and does not adjudicate the camps.

7. **Whether the data dictionary is obsolete.** Mullins says the term "is no longer in vogue" and argues that a
   catalog's automated discovery fixes the hand-maintained dictionary's failure [37]. Monte Carlo names the same
   staleness and concludes that "data dictionaries often feed into data catalogs" [38]. Both are commercially adjacent
   and neither is primary, so this is contested, not settled.

8. **The product-analytics label belongs to Mixpanel.** Mixpanel calls an import from Segment Protocols and from Avo
   "a data dictionary" [21]; Segment's own page calls its artifact "A Tracking Plan" and "a data spec" [25], and Avo's
   never uses the term [26]. This log reads the label as Mixpanel's own, which is why the bundle routes a reader who
   means the event list to `tracking-plan`.

9. **Review cadence has no fixed norm.** Docsie offers "[Monthly / Quarterly / Annual / Event-based]" [17]. Wizbrand
   says review "on a cadence (monthly or quarterly)" [18]. Basedash says update on every schema change, plus "a short
   quarterly review" [19]. Atlan says weekly for high-change assets and monthly for stable tables [36], and Arovy
   monthly, "or every two weeks if your org changes fast" [39]. The sources agree on two mechanisms, on change and on
   a calendar, and disagree on the interval. The Ownership and Review section asks the author to name both and to say
   whether the interval is borrowed or the team's own.

10. **Time-bound sources.** [28] is a launch announcement whose free-preview and pricing terms were promotional and
    time-bound. Mixpanel [21], Amplitude [22], [23], Segment [25], Avo [26] and dbt [20] are product documentation
    that changes with the product. Census's known-defect example [44] describes a limitation of the API at the time
    it was read. FastSlowMotion [29] is dated January 22, 2026.

---

## Notes for the companion

**The honest framing.** A data dictionary documents what the fields of a dataset or table mean, so that different
teams compute the same number from them. It is a standing reference, revised as the schema changes, not a one-time
record. Research-data sources define it independently ([1], [3], [4], [5], [6], [7]), Docsie ships it as a template
[17], and OSF publishes its element list [1]. The name is overloaded: product-analytics vendors use it for the event
list (contested item 8), and database engines use it for their own system tables ([12], [10]). The bundle's
boundaries are drawn on subject: the tracking plan specifies the events and properties a product emits, and the KPI
dashboard's Metric Definitions section locks a metric's formula. The first boundary is well sourced. The second is
the library's position against three sources (contested item 2), and the companion must say so.

**The evidentiary spine, in the order it should be used:**

- **Definitions and senses:** [1], [5], [6] and [9] for the field-meaning sense; [10] for the several senses and the
  active-versus-passive split; [12] for the engine sense the bundle scopes out; [21], [22] and [24] for the event-list
  sense.
- **What a field entry carries:** [1]'s element headings; CASRAI's seven questions, from "What is this variable
  called?" to "Where did this variable come from?", including "How is missingness represented?" [5]; [3]'s
  "allowable values in a field" and units; [4]'s "All values and value labels are fully described, including null or
  missing values"; Basedash's attribute cells, "Data type and nullability", "Where the value originates", "Enums,
  ranges, or units", "PII or restricted-data flag" and "Gotchas that cause wrong queries" [19]; [16]'s and [13]'s
  attribute lists.
- **The table as a whole:** [19]'s "its grain (what one row represents), its primary key, its update cadence, and how
  it relates to other tables"; [45]'s grain rule; [17]'s overview of "source systems, refresh cadence, and primary
  consumers"; [5]'s contrast with "dataset-level metadata".
- **Relationships and validation:** [17]'s "Document primary keys, foreign keys, joins, and related datasets" and
  "List accepted values, null handling, range checks, and uniqueness rules"; [6]'s "structure, content, and variable
  definitions for a dataset or collection of data"; [20]'s column tests.
- **Ownership, review and sign-off:** [17]'s "Identify data owner, steward, support channel, and review cadence" and
  its sign-off roles; [18]'s owner, implementer, consumers and "A simple process for proposing updates"; contested
  items 6 and 9.
- **Good and weak definitions:** OSF's genus-differentia form, "A is a B that C", and its circular counterexample [1];
  CASRAI's "header list" [5]; Basedash's contrast between a schema fact and a definition, and its cryptic-names case
  [19]; UNC's coded-value row [4].
- **Keeping it current:** [20]'s detection of undocumented columns; [2]'s tool-generated dictionary; contested items 5
  and 9; [31]'s obsolete and superseded structures.
- **The gap sources:** [42] to [46], routed below.

**How it fails, as sourced, and nothing more:**

- **It goes stale.** Chatterjee: "It's outdated. No one uses it." [35]; Nazabal et al.: metadata "missing or
  out-of-date" [33]; Monte Carlo [38], Atlan [36] and Arovy [39] describe the same drift.
- **It lists names without meanings.** CASRAI: a tab of column headers "is not a data dictionary under this
  definition - it is a header list" [5].
- **Its definitions are circular** [1], **or its names are cryptic**, so readers "will guess, and guesses produce
  confidently wrong numbers" [19].
- **It leaves the grain unstated**, which Basedash calls "the most common source of double-counted metrics" [19].
  That is Basedash's claim, not a measurement, and the companion must attribute it.
- **New readers misread the data without it.** Read et al. report that "the lack of a data dictionary combined with
  unclear variable names created the possibility for new study staff to misinterpret the data" [40]. That is one
  project's qualitative account, not a measured rate.

**Evidence of effect, stated plainly.** No source in this research measured whether having a data dictionary changes
an outcome. Read et al. [40] is a single case study. The University of Zurich abstract [41] reports that five teams
reproduced a trial's primary results while listing a "lack of complete data dictionaries" among the challenges. The
companion may cite both as what they are, and must not imply that either measured an effect.

**What this bundle must not say:** that timing defines a data dictionary; that no source puts metric formulas in a
data dictionary; that Phillips et al. place it as the final step without their concurrency caveat; that ISO/IEC 11179
contains any particular clause or attribute beyond what [11] says; that a data catalog has replaced the data
dictionary, or that it has not (contested item 7); that the owner should be the producer, the consumer or a
governance lead (contested item 6); that any review interval is the norm; that dbt states its documentation is
version-controlled with the code; that any failure above is "the most common", other than as Basedash's attributed
claim; the unverified DAMA statistic, in any form; or that any vendor template carries a licence.

**The section design, as the research moved it from the spec.** The spec's section names and order stand: three in
lean (Purpose and Boundary, Field Definitions, Ownership and Review), and full inserts Dataset Metadata, Relationships,
Validation Rules, and Review and Sign-off. The research changes the content of three of them:

- **Purpose and Boundary** (lean): the tables covered, and the four exclusions the spec names. The WHY comment states
  the product-analytics usage directly ([21], [22], [24]) and routes that reader to `tracking-plan`. It names the
  codebook as a common synonym in research settings (contested item 3).
- **Field Definitions** (lean, a table, the load-bearing section): **open each table with one line stating its grain
  and the key that enforces it** ([45], [19], [17]), then one row per field. **Recommended columns, the library's own
  convergence rather than any one source's list:** Field; Type and nullability (Basedash's own pairing [19]);
  Definition ([1], [5]); Allowed values, units and missing codes (UNC's "including null or missing values" [4], CASRAI
  [5], OSF's "Measurement units" [1], Basedash's "Enums, ranges, or units" [19]); Source, including how often it
  refreshes (CASRAI's "Where did this variable come from?" [5], Basedash [19]); Sensitivity ([19], [26], [21], [46]);
  and Owner. That is seven columns where the spec named six: Source and Sensitivity are added, and nullability joins
  Type rather than standing alone. A deprecated field stays in the table with its replacement and removal date in
  the Definition cell ([43], [31]), and a known trap is stated in the Definition cell where a reader meets the field,
  in the shape of Basedash's net-revenue caveat [19], without copying its wording.
- **Ownership and Review** (lean): the table's named owner and steward, the support channel or way to propose a
  change ([17], [18]), and the review triggers: every schema change, plus a stated interval marked as borrowed or the
  team's own (contested item 9).
- **Dataset Metadata** (full): source systems, refresh cadence and primary consumers ([17]), version and effective
  date ([17]), and any access or use conditions for the dataset as a whole ([46]).
- **Relationships**, **Validation Rules** and **Review and Sign-off** (full) stand as the spec designed them, sourced
  to [17], [19], [20] and [6]. Review and Sign-off carries the version history, including each deprecation.

**Gap-question candidates, routed by decision procedure 12:**

- **Admitted to the templates, each homed in an existing section above:** missing and sentinel codes, in the
  allowed-values column, because DDI-CDI says "Sentinel values are used for processing, not to describe subject
  matter" [42], the UK Data Service keeps missing values as their own attribute [46], and CASRAI asks "How is
  missingness represented?" [5]; a grain statement tied to its key, in Field Definitions, because "Naming the columns
  that enforce the unit is what lets another engineer write a test against it" [45]; a deprecation marker with a
  removal date, in the Definition cell and the version history ([43], [31], [39]); and a per-field sensitivity flag
  ([46], [19], [26]).
- **To the guide, as a rubric row or anti-pattern:** a header list passed off as a dictionary [5]; a circular
  definition [1]; a field whose missing codes are undocumented ([42], [5]); an unstated grain ([45], [19]); a known
  defect a reader has to discover by being misled ([44], [19]).
- **Declined, or left to the author:** units as a column of their own, because the sources that name units ([1], [3],
  [5], [19]) fold them into the value description and no source read separates them; a timezone convention, because
  no source read asks for one, though the example may state one as its own fact; a derivation-note format, because no
  source shows one attached to a field; and per-field consumer lists, which only Wizbrand asks for, per metric or
  event rather than per field [18].

**Teaching points the templates, guide and example must stay consistent with:**

- **A definition says what a value means, not what its type is** ([19], [1], [5]).
- **The grain comes first, stated with the key that enforces it** ([45], [19]).
- **Null, missing and sentinel values are documented, not assumed** ([42], [4], [5]).
- **Sensitivity is marked on the field where a reader meets it** ([19], [26], [46]).
- **A dictionary is updated as part of each schema change, and reviewed on a stated interval besides** ([19], [36],
  [39]; contested item 9).
- **It documents fields; the KPI dashboard locks formulas built from them.** That layering is the library's position
  (contested item 2).
- **The event list is the tracking plan's job, whatever a vendor calls it** ([25], [21]; contested item 8).

**Licences.** OSF's help article is CC0 [1]; CASRAI's content is CC-BY 4.0 [5]; UNC's article is CC BY-NC 4.0 [4];
the District of Columbia's catalog record is CC BY 4.0 [8]; and both Wikipedia articles are CC BY-SA 4.0 ([10], [11]).
No licence was found on Docsie, Wizbrand, Basedash, dbt or Amplitude. The templates' GOOD and WEAK text must not adapt
those vendors' wording or worked rows, including Docsie's customer-orders rows and Basedash's revenue rows.

**The example.** The Acme Analytics **data dictionary for the warehouse tables the tracking plan's events land in**,
the document `tracking-plan_example.md:50-51` says "this program has not yet written". **Dated after 2026-08-24**,
the tracking plan's date, with no version-history entry before that day. **Owner and steward: Lee Zhang (Data Eng)**,
the steward both siblings name (`tracking-plan_example.md:5`; `kpi-dashboard_example.md` names him steward of all
five metrics). **The facts it must agree with, and not restate:**

| Fact | Where it is stated |
|---|---|
| Ten events: `view_saved`, `view_switched`, `view_set_default`, `view_shared`, `view_load_error`, `report_opened`, `report_exported`, `report_shared`, `report_annotated`, `nudge_variant_assigned`, all from the Reporting web app to Amplitude | `tracking-plan_example.md:99-108` |
| Event properties and types: `dashboard_id`, `view_scope`, `recipient_user_id`, `report_id`, `annotation_id`, `variant_id`, `account_id` (string); `reason` (enum: filters_removed, permission_denied, timeout, unknown); `export_format` (enum: csv, pdf, image) | `tracking-plan_example.md:99-108` |
| `analyst_segment`: user trait, enum recurring, trialist, internal, set from the entitlements database, refreshed nightly | `tracking-plan_example.md:114` |
| `migration_reconciled`: account trait, boolean, set by the migration reconciliation job at cutover, feeding Migration integrity | `tracking-plan_example.md:115` |
| `recipient_user_id` on `view_shared` and `report_shared`: pii_flag true, "Hashed on the way into the warehouse", retained 180 days pending legal confirmation | `tracking-plan_example.md:121` |
| Time to Insight runs from "timestamp the report was opened" to "timestamp of first logged action on a report"; the three logged actions are `report_exported`, `report_shared` and `report_annotated` | `kpi-dashboard_example.md:63-66`; `tracking-plan_example.md:105-107` |
| The KPI dashboard's segments: it includes Recurring Analysts and excludes trialists, internal test accounts and, for Weekly active analysts, service accounts | `kpi-dashboard_example.md:64-66, 91-93` |

**What only the dictionary can add, which is what the stop rule tests:** the warehouse table and column names; types
and nullability stated as schema facts; the grain and key of each table; the joins from the events table to its user
and account tables; which column holds each of Time to Insight's two timestamps; and the column that holds the hashed
recipient. A row a product manager would look up must appear: the column that identifies a Recurring Analyst, the
column a Time to Insight timestamp comes from, or the hashed recipient. Any number the example introduces, such as a
row count, a range or a refresh time not stated above, is labelled illustrative.

**What it must not do.** It must not restate any event's business reason, the tracking plan's "why" column; restate
any metric's formula, inclusions or exclusions; invent a second steward, tool or warehouse; or claim to settle the
RAID log's assumption A-03 (legacy saved-view config schema fully documented, `raid-log_example.md:66`), which
concerns the legacy store, not the warehouse. **It must not invent a column that identifies service accounts**: no
sibling names one, and `analyst_segment`'s values do not include one. If the example needs to say how that exclusion
is applied, it states the gap as a known caveat rather than filling it. The `saved_view` table in Platform's Postgres
database (`production-readiness-review_example.md:85`, `business-continuity-plan_example.md:41-42`) is an
operational table, not one of this dictionary's warehouse tables, and the example must not redefine it. The product
vision's "We do not need to own the warehouse" (`product-vision_example.md:113-114`) refers to customers' warehouses, not
this program's. **The templates' GOOD and WEAK text must use a different organization, dataset and set of fields**:
grep the drafted templates for Acme, Amplitude, Looker, Lee Zhang, `analyst_segment`, `recipient_user_id`,
`occurred_at` and Time to Insight before review.

---

## Sources

### CANON: RESEARCH DATA MANAGEMENT

**[1] Center for Open Science (OSF Support) - "How to Make a Data Dictionary".** practitioner. **fetched-and-verified.**
`https://help.osf.io/hc/en-us/articles/360019739054-How-to-Make-a-Data-Dictionary`
Supports: Definition of a data dictionary; the field-entry element list in the OSF guide's own order; a worked good and a worked weak (circular) field definition; CC0 licence statement
Quotable: "A data dictionary is critical to making your research more reproducible because it allows others to understand your data."
Quotable: "The purpose of a data dictionary is to explain what all the variable names and values in your spreadsheet really mean."
Quotable: "Variable names"
Quotable: "Readable variable name"
Quotable: "Measurement units"
Quotable: "Allowed values"
Quotable: "Definition of the variable"
Quotable: "Synonyms for the variable name (optional)"
Quotable: "Description of the variable (optional)"
Quotable: "Other resources"
Quotable: "While there are many kinds of definition, where possible, please provide a definition with the following genus-differentia form:"
Quotable: "A is a B that C"
Quotable: "An a) attitude is a b) disposition c) to think or feel that is about something or someone, typically one that is reflected in a person's behavior."
Quotable: "Avoid circular definitions (e.g. A baseball is a ball used in baseball.)"
Quotable: "This article is licensed under CC0 for maximum reuse."

**[2] Buchanan, Crain, Cunningham, Johnson, Stash, Papadatou-Pastou, Isager, Carlsson and Aczel (2021), 'Getting Started Creating Data Dictionaries: How to Create a Shareable Dataset', OSF preprint (published in Advances in Methods and Practices in Psychological Science, DOI 10.1177/2515245920928007; the preprint was read, not the journal version).** practitioner. **fetched-and-verified.**
`https://osf.io/download/5ce2f5022a50c400197a8e09/`
Supports: The data-dictionary-versus-codebook distinction, as corroboration of the research-data reading; what the Data Dictionary Creator tool asks for per column; that this URL does not serve a blank fillable template with printed column headings; and the post-collection, producer-run upkeep mechanism, in which the researcher who holds the data regenerates the dictionary from the data with a tool rather than hand-editing prose
Quotable: "A data dictionary is a supplementary document that details the information provided in a dataset, often including the meaning and attributes of the included variables as well as information about the creation, format, and usage of the data"
Quotable: "The second step of the process involves entering the metadata for each column provided in the dataset. The application automatically provides a starting point for the number of unique values, missing values, variable type (i.e., character, numeric), and minimum/maximum values. A description of each column can be added, along with information about the levels/groups in the data and synonyms for the variables."
Quotable: "the data are converted to a data dictionary or codebook by using a tool, like Codebook or Data Dictionary Creator, that creates the metadata output in JSON-LD and/or HTML format"
Quotable: "This tutorial will demonstrate two simple procedures for non-programmers to create a codebook and data dictionary that describes research data in the social sciences."
Quotable: "Data dictionaries can be contrasted with codebooks, which are used to denote survey data, while the former include information about the data file structure."
Quotable: "Data dictionaries may include the information provided in a codebook and vice versa"
Quotable: "and sometimes these terms are used interchangeably"
Quotable: "we demonstrate how to export data from an online platform, Qualtrics"
Quotable: "and explain how to maintain the metadata provided automatically by the survey software"
Quotable: "We have also included detailed video tutorials as supplementary material to be updated as the applications update"
Quotable: "from source data (e.g., survey answers on Qualtrics) to an openly shared dataset accompanied by a data dictionary or codebook"

**[3] Smithsonian Libraries and Archives - "Describing Your Data: Data Dictionaries".** practitioner. **fetched-and-verified.**
`https://library.si.edu/research/describing-your-data-data-dictionaries`
Supports: Definition of a data dictionary as distinct from a descriptive metadata record; the element list it names for a field entry; its separate framing of dataset-level provenance detail
Quotable: "To enable discovery and citation all research data should have both a corresponding descriptive metadata record as well as explanatory metadata, or data dictionary, that defines and describes the data itself."
Quotable: "A data dictionary, "read me" file, or key explains the contents of the dataset. Any information someone would need to interpret or re-use your data should be included in the data dictionary. It may include full definitions of any abbreviations used, units of measurement, allowable values in a field, data types, thesauri or controlled vocabularies used, and other important details of the data elements along with a brief description of the provenance or parameters of the data, i.e., date or location the data was collected."

**[4] University of North Carolina at Chapel Hill, Research Data Management Core - "RDMC Data Management Guide: Documentation - Codebook".** practitioner. **fetched-and-verified.**
`https://tdx.unc.edu/TDClient/33/Portal/KB/ArticleDet?ID=443`
Supports: Treats codebook and data dictionary as the same document under two names; its own ordered element list for what a codebook should include; its own worked example rows; its explicit statement that there is no single format standard; its licence statement
Quotable: "This article provides instructions and tips for creating a codebook (sometimes referred to as a 'data dictionary') that describes the contents of a research data file or files."
Quotable: "A codebook is a document that describes an individual data file or a collection of data files."
Quotable: "Title of the project and contact information for PI(s)."
Quotable: "For projects with multiple data files, each section of the codebook should be labeled with the data filename it is describing."
Quotable: "All variables in the data file(s) are listed with the variable name used in the data file accompanied by the variable label or description of the content."
Quotable: "Variable Name | Variable Label"
Quotable: "gender | Whether or not the respondent is female"
Quotable: "All values and value labels are fully described, including null or missing values"
Quotable: "gender | Whether or not the respondent is female | male = 0; female = 1; missing = N/A"
Quotable: "Information on the structure of the data, as needed. For databases, provide table names, keys, and their relationships (e.g., ER diagram). For text file, provide formatting information (e.g., first row is variable names, tab or comma delimited)."
Quotable: "Codebooks and data dictionaries come in a variety of formats. There is no single standard, and some disciplines have their own nuances of a codebook."
Quotable: "This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License."

**[5] CASRAI Editorial Board - "Data Dictionary in Research Data Management: Definition, Components, and How It Differs from a Codebook".** standards. **fetched-and-verified.**
`https://casrai.org/guides/data-dictionary-research-data-management`
Supports: The fullest, most explicit definition and the sharpest drawn distinction among data dictionary, codebook, and metadata schema; its own ordered minimum-element list and its own worked good/weak contrast; its licence statement
Quotable: "A data dictionary is a structured document, table, or file that defines every variable in a dataset - its name, meaning, data type, unit of measurement, allowed values, and any coding scheme used to represent those values - so that anyone other than the person who collected the data can interpret it correctly."
Quotable: "it operates one column, field, or measurement at a time, in contrast to dataset-level metadata (title, creator, date, subject) or study-level documentation (methodology, sampling, provenance)"
Quotable: "What is this variable called?"
Quotable: "What does it measure or record?"
Quotable: "What type of data is it?"
Quotable: "What unit is it measured in?"
Quotable: "What values are valid, and what do coded values mean?"
Quotable: "How is missingness represented?"
Quotable: "Where did this variable come from?"
Quotable: "Derivation logic for any computed variable"
Quotable: "Universe/skip logic"
Quotable: "Format constraints"
Quotable: "Version history"
Quotable: "Cross-references to controlled vocabularies"
Quotable: "A spreadsheet tab that lists only column headers with no definitions is not a data dictionary under this definition - it is a header list. A single paragraph describing a dataset's general subject matter, with no per-variable breakdown, is also not a data dictionary - that is dataset-level metadata"
Quotable: "A data dictionary is typically the narrower, more mechanical artifact: a table of variable names, types, units, and value labels, often produced directly from a database schema or survey instrument export, and sometimes generated automatically by data-collection software."
Quotable: "A codebook usually wraps the same variable-level information inside a fuller document that also includes study-level context: the questionnaire text as administered, sampling and weighting information, fieldwork dates, and notes on how the study was conducted."
Quotable: "Content released under CC-BY 4.0 unless otherwise marked."

**[6] Harvard Medical School, Research Data Management - "Data Management Terminology".** practitioner. **fetched-and-verified.**
`https://datamanagement.hms.harvard.edu/about/data-management-terminology`
Supports: A short glossary-style definition that uses "data dictionary" and "data codebook" as the same term
Quotable: "data dictionary: Outlines the structure, content, and variable definitions for a dataset or collection of data. A data dictionary, or data codebook, defines and describes the elements of a dataset so that it can be understood and used at a later date. A data dictionary is a critical tool for reproducibility because it allows others to understand your data."

**[7] NNLM (Network of the National Library of Medicine), National Center for Data Services - "Data Dictionary" (Data Glossary).** practitioner. **fetched-and-verified.**
`https://nnlm.gov/guides/data-glossary/data-dictionary`
Supports: Definition; the specific case that codebook and data dictionary are interchangeable terms in casual use but opposite in which one carries more structural detail, illustrated by REDCap's own file split
Quotable: "A data dictionary is a document that outlines the structure, content, and meaning of a given variable. This includes what type of data is being collected (e.g. free text, numerical, categorical or group data), the full wording of a question, what values are allowable (e.g. numeric ranges, multiple choice codes), and what those values mean (e.g. 0 = no high blood pressure diagnosis, 1 = borderline high blood pressure, 2 = high blood pressure). A data dictionary is a critical tool for data analysis and reproducibility."
Quotable: "The term codebook is often used interchangeably with data dictionary, though the data dictionary can contain more information about the structure of a database. In the widely used data collection tool, REDCap, the data dictionary is a CSV file containing information on the variables and the structure of the REDCap database, while the codebook is a human readable document that provides information on each data element."

**[8] District of Columbia Office of the Chief Technology Officer, 'Open Data Dictionary Template Individual', Data.gov catalog entry.** primary. **fetched-and-verified.**
`https://catalog.data.gov/dataset/open-data-dictionary-template-individual`
Supports: What the template is for (per-field attribute description plus code values); its stated licence; the fact that this catalog page does NOT itself print the template's column headings
Quotable: "This template covers section 2.5 Resource Fields: Entity and Attribute Information of the Data Discovery Form cited in the Open Data DC Handbook (2022). It completes documentation elements that are required for publication. Each field column (attribute) in the dataset needs a description clarifying the contents of the column. Data originators are encouraged to enter the code values (domains) of the column to help end-users translate the contents of the column where needed, especially when lookup tables do not exist."
Quotable: "license https://creativecommons.org/licenses/by/4.0"

### CANON: ENTERPRISE DATA MANAGEMENT AND THE SENSES OF THE TERM

**[9] GOV.UK Data Architecture Community (GDAC), "Business Glossaries & Definitions" PDF (2020).** primary. **fetched-and-verified.**
`https://dataarchitecture.blog.gov.uk/wp-content/uploads/sites/220/2020/06/GDAC_Business_Glossaries_Definitions_2020-1.pdf`
Supports: The documentation sense of the term, and the three-way boundary between dictionary, glossary and catalogue, which the guidance records in its own 'Common misunderstandings' field
Quotable: "A centralised repository used to define and communicate the structure and content of data sets."
Quotable: "A data dictionary may describe data in business terms, however, the information held within a data dictionary extends to include the ‘technology relevant’ or ‘machine readable’ articulation of data."
Quotable: "The content of a data dictionary is usually extracted from the database or modelling tool and is sometimes seen as a data model in a narrative form."
Quotable: "A repository of approved, governed and maintained compendium of business term names, their definitions and, optionally, their relationships to other business terms."
Quotable: "An inventory of available data assets supported by a collection of metadata, enabling data users to: • search for and find data quickly • see all the available datasets • evaluate data and make informed choices on the suitability of data • perform data preparation and analysis efficiently and with confidence."
Quotable: "COMMON MISUNDERSTANDINGS: • Confusion over definition and with related concepts: o Business Glossary o Data Catalogue"
Quotable: "It can be used to manage the names, descriptions, structure, characteristics, storage requirements, default values, relationships, uniqueness, and other attributes of every data element in a data model."
Quotable: "TERM STEWARD (PARTY OR ROLE): GDAC"

**[10] Wikipedia, "Data dictionary".** practitioner. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Data_dictionary`
Supports: Names the database-catalog, document, middleware or DBMS-component, and active or passive senses of the term explicitly; lists the attributes an entry typically carries; states the boundary with the system catalog
Quotable: "A data dictionary, or metadata repository, as defined in the IBM Dictionary of Computing, is a "centralized repository of information about data such as meaning, relationships to other data, origin, usage, and format"."
Quotable: "Oracle defines it as a collection of tables with metadata. The term can have one of several closely related meanings pertaining to databases and database management systems (DBMS): A document describing a database or collection of databases"
Quotable: "An integral component of a DBMS that is required to determine its structure"
Quotable: "A piece of middleware that extends or supplants the native data dictionary of a DBMS"
Quotable: "The terms data dictionary and data repository indicate a more general software utility than a catalogue. A catalogue is closely coupled with the DBMS software."
Quotable: "If a data dictionary system is used only by the designers, users, and administrators and not by the DBMS Software, it is called a passive data dictionary. Otherwise, it is called an active data dictionary or data dictionary."
Quotable: "Database users and application developers can benefit from an authoritative data dictionary document that catalogs the organization, contents, and conventions of one or more databases."
Quotable: "There is no universal standard as to the level of detail in such a document."
Quotable: "Here is a non-exhaustive list of typical items found in a data dictionary for columns or fields: Entity or form name or their ID... Field name... Field type (string, integer, date, etc.)... Is-required (Boolean)... Reference table name, if a foreign key... Description or synopsis"
Quotable: "Text is available under the Creative Commons Attribution-ShareAlike 4.0 License"

**[11] Wikipedia, "ISO/IEC 11179".** practitioner. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/ISO/IEC_11179`
Supports: A description of ISO/IEC 11179, not the standard's own text: which principles and parts the standard has, and the naming, definition and registration obligations it places on a data element
Quotable: "A value domain is the permitted range of values for a characteristic of an object class. An example of a value domain for "sex of person" is "M = Male, F = Female, U = Unknown"."
Quotable: "Each Data element in an ISO/IEC 11179 metadata registry: should be registered according to the Registration guidelines (11179-6)"
Quotable: "will be uniquely identified within the register (11179-5)"
Quotable: "should be named according to Naming and Identification Principles (11179-5)"
Quotable: "should be defined by the Formulation of Data Definitions rules (11179-4)"
Quotable: "may be classified in a Classification Scheme (11179-2)"
Quotable: "Data elements that store "Codes" or enumerated values must also specify the semantics of each of the code values with precise definitions."
Quotable: "ISO/IEC 11179 proper does not describe data as it is actually stored. It does not refer to the description of physical files, tables and columns."
Quotable: "Text is available under the Creative Commons Attribution-ShareAlike 4.0 License"

**[12] Oracle, "Database Concepts" - "The Data Dictionary" chapter.** vendor. **fetched-and-verified.**
`https://docs.oracle.com/cd/B19306_01/server.102/b14220/datadict.htm`
Supports: The DBMS-internal system-catalog sense of the term, named explicitly. This bundle scopes that sense out
Quotable: "This chapter describes the central set of read-only reference tables and views of each Oracle database, known collectively as the data dictionary."
Quotable: "One of the most important parts of an Oracle database is its data dictionary, which is a read-only set of tables that provides information about the database."
Quotable: "A data dictionary contains: The definitions of all schema objects in the database (tables, views, indexes, clusters, synonyms, sequences, procedures, functions, packages, triggers, and so on)"
Quotable: "How much space has been allocated for, and is currently used by, the schema objects"
Quotable: "Default values for columns"
Quotable: "Integrity constraint information"
Quotable: "The names of Oracle users"

**[13] Dataedo, "ER diagram vs data dictionary" blog (vendor sells a data-catalog tool).** vendor. **fetched-and-verified.**
`https://dataedo.com/blog/er-diagram-vs-data-dictionary-documenting-data-models`
Supports: The content of a dictionary entry, including a list of values, default values and an owner, in the vendor's own field-meaning sense
Quotable: "Data Dictionary is a list of data elements (entity/table and attribute/column) with their attributes and descriptions. It has a form of a set of tables."
Quotable: "May include many data attributes (e.g. list of values, default values, owner, etc.)"
Quotable: "Includes detailed descriptions of each element (table, column)"

**[14] Atlan, "Data Catalog vs. Data Dictionary" (vendor sells a data-catalog tool).** vendor. **fetched-and-verified.**
`https://www.atlan.com/data-catalog-vs-data-dictionary/`
Supports: The boundary between dictionary, catalog and glossary, in the vendor's own three-way framing. The claim serves the seller's product, the catalog, by positioning the dictionary as narrower
Quotable: "A data dictionary captures technical metadata for individual databases, while a data catalog provides a holistic view of all metadata across an organization."
Quotable: "The main difference between a data catalog and a data dictionary is that a data dictionary documents technical metadata for a specific database, whereas a data catalog acts as a unified context, control, and collaboration layer of all metadata (technical, governance, operational, collaboration, quality, and usage) across your entire data ecosystem."
Quotable: "A data dictionary holds the technical metadata for a database, a business glossary pulls together a common understanding of business terms and concepts, whereas a data catalog is a unified access, control, and collaboration layer that spans all metadata across your data estate."
Quotable: "A data dictionary helps understand and trust data in databases better, a business glossary provides a common language for the organization when it comes to business concepts and metrics, and a data catalog helps find, understand, trust, and collaborate on data."

**[15] Actian, "Business Glossary, Data Catalog, and Data Dictionary" guide (vendor sells a data-intelligence platform).** vendor. **fetched-and-verified.**
`https://www.actian.com/blog/data-intelligence/the-guide-to-understanding-the-difference-between-a-business-glossary-a-data-catalog-and-a-data-dictionary/`
Supports: The three-way boundary between glossary, catalog and dictionary, and the content of a dictionary entry, including an owner. The vendor frames all three as 'pillars' of its own platform
Quotable: "A data catalog, data dictionary, and business glossary are complementary tools that help organizations manage and understand data more effectively."
Quotable: "A data dictionary provides detailed technical information about data elements, such as structure, format, meaning, ownership, and usage."
Quotable: "A data dictionary is a third tool that will help you strengthen and boost your data strategy. This data management tool provides detailed information about the data used in your business based on a set of metadata. This metadata describes the data, its structure, its format, its meaning, its owner, and its use."
Quotable: "A data dictionary is also a key tool for data quality management, as it allows you to monitor data quality by identifying errors and inconsistencies."

**[16] Analytics8, "Data Dictionary vs. Data Catalog vs. Business Glossary" blog (vendor sells data-intelligence consulting/tools).** vendor. **fetched-and-verified.**
`https://analytics8.com/blog/data-dictionary-vs-data-catalog-vs-business-glossary`
Supports: Disagrees with GDAC, Atlan and Actian by nesting the dictionary inside the glossary rather than treating them as siblings. Lists entry content including technical attributes, and places measure names and their calculations inside the data dictionary, the wider framing that this bundle's layering declines
Quotable: "A data dictionary is a subset of a business glossary, but both are required to build a data catalog."
Quotable: "As stated earlier, a business glossary is the starting point for any data initiative, but it is also a prerequisite to building a data dictionary."
Quotable: "A data dictionary is a more technical and thorough documentation of data and its metadata. It consists of detailed definitions and descriptions of data dimensions and measure names (in databases, data tables, etc.), their calculations, their types, and related information."
Quotable: "Attributes such as data type, size, allowed values, default values, and constraints, as well as any additional technical metadata that is relevant included in your data dictionary."
Quotable: "A data catalog is the pathway-or a bridge-between a business glossary and a data dictionary."

### STRUCTURE: PRACTITIONER TEMPLATES AND DOCUMENTATION AS CODE

**[17] Docsie, "Free Data Dictionary Template" (vendor template page).** vendor. **fetched-and-verified.**
`https://www.docsie.io/solutions/templates/data-ai-analytics/data-dictionary/`
Supports: Full section list, field-table column guidance, document-level metadata header, relationships/validation/ownership/sign-off sections, a worked example
Quotable: "Template Metadata"
Quotable: "Overview"
Quotable: "Describe the dataset purpose, source systems, refresh cadence, and primary consumers."
Quotable: "Dataset Scope"
Quotable: "Define included entities, excluded records, date range, and grain."
Quotable: "Field Definitions"
Quotable: "Create a table with Field, Type, Required, Definition, Example, and Notes columns."
Quotable: "Relationships"
Quotable: "Document primary keys, foreign keys, joins, and related datasets."
Quotable: "Validation Rules"
Quotable: "List accepted values, null handling, range checks, and uniqueness rules."
Quotable: "Ownership"
Quotable: "Identify data owner, steward, support channel, and review cadence. Use concise Markdown tables and make definitions unambiguous."
Quotable: "Review and Signoff"
Quotable: "Document review conclusions, approvals, unresolved items, and next review date."
Quotable: "order_id must be unique."
Quotable: "net_revenue_usd must be zero or greater."
Quotable: "order_status must be one of: pending, paid, shipped, refunded."
Quotable: "[Monthly / Quarterly / Annual / Event-based]"
Quotable: "[Draft / In Review / Approved]"
Quotable: "Review Cycle"
Quotable: "Effective Date"
Quotable: "Preparer"
Quotable: "Reviewer"
Quotable: "Approver"
Quotable: "Customer Orders Data Dictionary"
Quotable: "Unique order identifier"
Quotable: "Revenue after discounts and refunds"

**[18] Wizbrand, "Data Dictionary: What It Is, Key Features, Benefits, Use Cases, and How It Fits in Analytics" (practitioner tutorial/blog, posted March 23 2026).** practitioner. **fetched-and-verified.**
`https://www.wizbrand.com/tutorials/data-dictionary/`
Supports: Heading structure (prose, no field table), key components list, ownership/review-cadence FAQ answers, good/weak naming guidance, data-dictionary-vs-tracking-plan distinction
Quotable: "What Is Data Dictionary?"
Quotable: "Why Data Dictionary Matters in Conversion & Measurement"
Quotable: "How Data Dictionary Works"
Quotable: "Key Components of Data Dictionary"
Quotable: "Types of Data Dictionary"
Quotable: "Real-World Examples of Data Dictionary"
Quotable: "Benefits of Using Data Dictionary"
Quotable: "Challenges of Data Dictionary"
Quotable: "Best Practices for Data Dictionary"
Quotable: "Tools Used for Data Dictionary"
Quotable: "Metrics Related to Data Dictionary"
Quotable: "Future Trends of Data Dictionary"
Quotable: "Data Dictionary vs Related Terms"
Quotable: "Who Should Learn Data Dictionary"
Quotable: "Summary of Data Dictionary"
Quotable: "Frequently Asked Questions (FAQ)"
Quotable: "Data element name: Event name, field name, metric name, or dimension."
Quotable: "Business definition: Plain-language meaning (what it represents)."
Quotable: "Technical definition: Data type, format, and collection method (e.g., integer, string, timestamp; client-side vs server-side)."
Quotable: "Allowed values and conventions: Controlled vocabularies (e.g., approved channel names) and naming patterns."
Quotable: "Calculation logic (for metrics): Formulas and inclusion/exclusion rules (e.g., “conversion rate excludes internal traffic and refunded orders”)."
Quotable: "Data source and destination: Where data originates and where it is stored/used (warehouse tables, reports, dashboards)."
Quotable: "Ownership and stewardship: Who maintains it, who approves changes, and who is notified."
Quotable: "Versioning and change history: What changed, when, and why-critical for explaining trend shifts in Analytics."
Quotable: "Data quality notes: Known limitations, edge cases, and validation checks."
Quotable: "A tracking plan describes what you intend to track (events, triggers, parameters) and why. A Data Dictionary documents what the data means and how it is structured once implemented."
Quotable: "Create checks that confirm: - Events fire when expected - Required parameters are present - Data types match expectations - Volumes and conversion rates don’t change unexpectedly after releases"
Quotable: "For each metric/event, document: - Primary owner (approves changes) - Implementer (who updates tracking) - Consumers (teams impacted) - A simple process for proposing updates"
Quotable: "When KPI logic changes (e.g., a new qualification rule), log the change date and impact so trend interpretation remains accurate."
Quotable: "Ownership should be shared but explicit: marketing operations or analytics leadership often owns KPI definitions, while engineering/data teams own schema accuracy. The best Conversion & Measurement setups assign an owner per domain (acquisition, lifecycle, revenue)."
Quotable: "Update it whenever tracking, business rules, or reporting logic changes. In practice, teams review it on a cadence (monthly or quarterly) and also after major site releases, app updates, or measurement migrations that impact Analytics."
Quotable: "Use predictable patterns for events and parameters (e.g., verb_noun). Document examples and anti-examples so implementation stays consistent."
Quotable: "Write business definitions in plain language, then add technical specs underneath."
Quotable: "lead_submitted, lead_created_crm, lead_qualified"

**[19] Basedash (Max Musing), "What is a data dictionary, and how to build one for analytics" (vendor blog, June 28 2026).** vendor. **fetched-and-verified.**
`https://www.basedash.com/blog/what-is-a-data-dictionary-and-how-to-build-one-for-analytics`
Supports: Field attribute table and headings, three-layer model, table-level grain/primary-key/relationships guidance, ownership/review-cadence FAQ, good/weak definition examples, dbt as a storage location
Quotable: "What is a data dictionary?"
Quotable: "Data dictionary vs data catalog vs semantic layer"
Quotable: "What should a data dictionary include?"
Quotable: "The three layers of a useful data dictionary"
Quotable: "How to build a data dictionary"
Quotable: "Where should a data dictionary live?"
Quotable: "How to keep a data dictionary from going stale"
Quotable: "Why data dictionaries matter more with AI-assisted BI"
Quotable: "When you need a data dictionary, and when you do not"
Quotable: "Beyond individual columns, a complete dictionary also documents the table itself: its grain (what one row represents), its primary key, its update cadence, and how it relates to other tables. Grain is the most common source of double-counted metrics, so record it explicitly."
Quotable: "A database schema already tells you that orders.amount is a numeric column. A data dictionary tells you that amount is the gross order total in cents before refunds and excluding tax, sourced from Stripe, and that you should use net_amount for revenue reporting."
Quotable: "The two most important attributes are definition and notes. A good definition prevents the wrong column from being used. A good caveat (“this excludes refunds”) prevents the right column from being used the wrong way."
Quotable: "An AI assistant pointed at a schema with cryptic names like flg_2 and dt_x will guess, and guesses produce confidently wrong numbers."
Quotable: "If you use dbt, column and table descriptions live in schema.yml files alongside the models, and they are version-controlled with the code. This keeps definitions next to the transformations that produce them."
Quotable: "Ownership should sit with the team that produces each dataset, not the team that consumes it. Producers know the source and the caveats. A central data or analytics lead can own the structure and process, but per-field definitions should map to the people accountable for that data."
Quotable: "Update definitions whenever the schema changes, as part of the change itself rather than as a separate task. Beyond that, a short quarterly review where data owners confirm their definitions is usually sufficient. The fields most likely to drift are calculated metrics and enums, so review those first."
Quotable: "Assign an owner to each table. Ownership keeps a dictionary current, because unowned definitions don’t get updated."
Quotable: "The technical column name"
Quotable: "Data type and nullability"
Quotable: "Plain-language meaning, in one sentence"
Quotable: "Where the value originates"
Quotable: "Person or team accountable for it"
Quotable: "Enums, ranges, or units"
Quotable: "PII or restricted-data flag"
Quotable: "How current the data is"
Quotable: "Gotchas that cause wrong queries"
Quotable: "The metrics layer on top of tables"
Quotable: "Monthly recurring revenue in cents, excluding one-time charges"
Quotable: "Excludes refunds; use net_mrr for net"
Quotable: "Owners are usually the team that produces the data, not the team that consumes it"

**[20] dbt Developer Hub, "About documentation" (dbt Labs product documentation).** vendor. **fetched-and-verified.**
`https://docs.getdbt.com/docs/collaborate/documentation`
Supports: Documentation-as-code mechanism (description: key in schema.yml beside model/column/tests), docs blocks for reusable markdown descriptions, absence of owner/version/review-cadence fields on this page, staleness-detection via undocumented-column surfacing
Quotable: "Good documentation for your dbt models will help downstream consumers discover and understand the datasets you curate for them."
Quotable: "dbt provides a scalable way to generate documentation for your dbt project using descriptions and commands."
Quotable: "dbt also provides a way to add descriptions to models, columns, sources, and more, to further enhance your documentation."
Quotable: "Add the description: key to the same YAML files where you declare data tests."
Quotable: "models: - name: events description: This table contains clickstream events from the marketing website columns: - name: event_id description: This is a unique identifier for the event data_tests: - unique - not_null - name: user-id quote: true description: The user who performed the event data_tests: - not_null"
Quotable: "dbt will introspect your warehouse to generate a list of columns in each relation, and match it with the list of columns in your .yml files. As such, any undocumented columns will still appear in your documentation!"
Quotable: "Use a docs block to write the description in a separate Markdown file."
Quotable: "{% docs table_events %} This table contains clickstream events from the marketing website."
Quotable: "'{{ doc("table_events") }}' will be expanded to the markdown defined in the table_events docs block."
Quotable: "You can document almost everything in your project using the description: key."
Quotable: "A redesigned, open-source documentation site with Semantic Layer metadata and column-level lineage that you can host anywhere"

### THE PRODUCT-ANALYTICS SENSE OF THE TERM, AND THE METRIC BOUNDARY

**[21] Mixpanel - "Lexicon" (Data Governance docs).** vendor. **fetched-and-verified.**
`https://docs.mixpanel.com/docs/data-governance/lexicon`
Supports: Mixpanel's own name for its event/property catalog is "a data dictionary"; it also documents saved-metric and formula definitions inside that same artifact, and a sensitive-data flag on properties
Quotable: "Lexicon is a data dictionary that stores descriptions of events and their properties."
Quotable: "Mixpanel supports exporting and importing Lexicon data dictionaries."
Quotable: "When importing a data dictionary from Segment Protocols using the Segment Config API..."
Quotable: "To import your data dictionary from Avo.app, you will need to enable an integration with Mixpanel."
Quotable: "The Metrics page in your Lexicon documents your saved metrics and Formulas."
Quotable: "Click into a definition to review its formula, description, and query volume."
Quotable: "Custom properties combine existing properties into new ones on the fly using a simple, Excel-like formula language. When you save a custom property so your team can reuse it across reports, it appears in Lexicon as a saved definition."
Quotable: "Status... Also indicates if the property is blocked, merged, or marked as sensitive."
Quotable: "Sensitive data: If you accidentally send sensitive data, such as passwords or credit card information, you can block the event or property with that data and prevent it from being stored in Mixpanel servers."

**[22] Amplitude - "Event and property descriptions" (Amplitude Docs).** vendor. **fetched-and-verified.**
`https://amplitude.com/docs/en/data/event-property-descriptions`
Supports: Amplitude's own definition of "data dictionary" as a taxonomy document a user uploads, distinct from the in-product tracking plan; this is the event/property sense, not a warehouse-table sense
Quotable: "A data dictionary is a document that lays out the project's taxonomy: its events, the properties on those events, and what each means."
Quotable: "Uploaded files: Files you upload to a project under Settings > AI Controls, such as a data dictionary or a product spec. Amplitude treats these as the most authoritative source and prefers them over everything else."
Quotable: "For the best results, upload a data dictionary to your project."
Quotable: "This only applies to active events and properties included in your tracking plan. It also doesn't apply to custom events."

**[23] Amplitude - "Create a tracking plan" (Amplitude Docs, API/content docs).** vendor. **fetched-and-verified.**
`https://amplitude.com/docs/api/content/data/create-tracking-plan`
Supports: Amplitude's own account of what a tracking plan is for. The page never uses the term "data dictionary", so it is a null result on whether this page calls the event spec a data dictionary. Its one line about confusion after data lands concerns field names, not column meaning
Quotable: "A tracking plan defines every event and property you collect, why you collect each one, and which source emits it. Build one before you instrument code so analysts, PMs, and engineers work from one schema instead of arguing about field names after the data lands."
Quotable: "The autogenerated library is a lightweight wrapper over your analytics provider's SDK that provides type-safety, supports linting, and enables additional features like input validation. The code exactly replicates the spec in the tracking plan and enforces all its rules and requirements."

**[24] Amplitude Blog - Kate Adams, "5 steps to become more comfortable using data".** vendor. **fetched-and-verified.**
`https://www.amplitude.com/blog/5-steps-to-become-more-comfortable-using-data`
Supports: A second Amplitude-authored usage of "Data Dictionary" that is explicitly the event/action list, confirming the event-list sense recurs even within one vendor's own content, not only in product docs
Quotable: "Creating an internal Data Dictionary or Taxonomy Guide (example below) is a key part in enabling others to use more numbers. For user behavior data, the Data Dictionary or Taxonomy Sheet lists the user actions and descriptions of what each means."
Quotable: "Maintaining a data dictionary is a key component in making data easier to read and understand."
Quotable: "Your Data Dictionary from step #2 is a living, breathing document. It should continually be updated over time so that it's your company's source of truth for data definitions."

**[25] Twilio Segment - "Protocols Tracking Plan" (Segment Docs).** vendor. **fetched-and-verified.**
`https://www.twilio.com/docs/segment/protocols/tracking-plan/`
Supports: Segment's own term for the event and property spec is "Tracking Plan" or "data spec". The page never uses the words "data dictionary", which is a null result on Segment's own usage, although Mixpanel's Lexicon page calls an import from Segment Protocols "a data dictionary"
Quotable: "A Tracking Plan is a data spec outlining the events and properties you intend to collect across your Segment Sources."
Quotable: "Each user action maps to a distinct event, or Track call, that you will track in Segment."
Quotable: "Enter a description for your event or property. These descriptions are helpful for both engineers instrumenting Segment and consumers of the data."

**[26] Avo - "Properties" (Avo Docs, Tracking Plan Management).** vendor. **fetched-and-verified.**
`https://avo.app/docs/workspace/tracking-plan/properties`
Supports: Avo's own page never uses "data dictionary" either, another null result on the vendor's own usage, although Mixpanel's Lexicon page describes importing "your data dictionary from Avo.app." Avo also carries the clearest field-level PII flag quotation in this log
Quotable: "The PII status of the property - whether it carries personally identifiable information (Enterprise plan)"
Quotable: "A Description that gives additional context of what the property is describing beyond the property name (optional but highly recommended)"
Quotable: "Properties are also known as traits, attributes, metadata, etc. They are information that is attached to events, users or groups that describe the state of the user or the product at the time of the event."

**[27] RudderStack - "Behavioral Data Collection Best Practices" whitepaper (PDF).** vendor. **fetched-and-verified.**
`https://www.rudderstack.com/assets/behavioral_data_collection_best_practices_whitepaper.pdf`
Supports: RudderStack names two outputs of a single tracking-plan process, and uses "data dictionary" itself for the output that helps data consumers understand what each source collects. That is the event-list sense again, not warehouse column meaning
Quotable: "The tracking plan document, when deployed correctly, adds a ton of value to an implementation. Here are a few examples of the resources it will deliver and the teams it impacts:"
Quotable: "Instrumentation guide that tells the responsible dev team how to wire up events within the source"
Quotable: "Data dictionary/solution design document for analysts or data consumers to understand how and why data is collected at the source"
Quotable: "Reference schema for our Data Governance API to validate incoming events and surface any errors in a separate table in the warehouse (other observability improvements coming soon!)"
Quotable: "Reference table for RudderTyper, a library wrapper the dev team can use to ensure they are only instrumenting pre-approved event names and properties"
Quotable: "Autotrack... results in a large volume of semi-structured data sent downstream and places the burden of the work on data analysts to make sense of the data once it hits the warehouse."
Quotable: "What legal or regulatory issues do we have to contend with either now or on the horizon?"
Quotable: "GDPR, CCPA, HIPAA, etc."

**[28] dbt Labs - "dbt Labs Launches the dbt Semantic Layer" (press release / blog).** vendor. **fetched-and-verified.**
`https://www.getdbt.com/blog/dbt-labs-launches-the-dbt-semantic-layer-enabling-greater-consistency-across-analytics-tools`
Supports: dbt's own announcement says the Semantic Layer's job is to centralize metric definitions away from downstream tools, and a partner quotation names column-level lineage as the separate, lower layer the metrics sit on. This is the clearest evidence in the log for a metric layer distinct from column documentation, though the page never contrasts a metric definition with a column description in those words
Quotable: "the dbt Semantic Layer enables organizations to centrally define business metrics in dbt and then query them from any analytics tool, ensuring that critical definitions such as 'revenue,' 'customer count,' or 'churn rate' are consistent in every data application the organization is using."
Quotable: "Until now, organizations have been forced to define business metrics individually in each data application... the inevitability that the same metric is calculated inconsistently at different times and in different places."
Quotable: "By moving metric definitions out of downstream tools and into dbt, everyone in the business can feel confident that they are working from the same assumptions as their colleagues."
Quotable: "Atlan's integration with dbt's Semantic Layer brings end-to-end column-level lineage to metrics, enabling richer context, visibility, and self-service for data teams everywhere."
Quotable: "The dbt Semantic Layer is now an optional feature of dbt Cloud. Launched in public preview, it is currently available for no additional cost, and will be a paid feature once it is made generally available."

**[29] Kaitlynn Sirotkin, FastSlowMotion, 'Analytics Governance: Metric Definitions and Single Source of Truth' (January 22, 2026), read in a browser.** vendor. **fetched-and-verified.**
`https://www.fastslowmotion.com/salesforce-analytics-governance-metrics/`
Supports: nothing in this bundle. Listed because it was consulted.
Quotable: "Analytics governance is the system for defining metrics, assigning owners, and controlling how KPIs are calculated so everyone uses the same numbers."
Quotable: "A KPI dictionary (definition, formula, inclusion/exclusion rules)"
Quotable: "A source-of-truth map (object/system → field → owner)"
Quotable: "A KPI dictionary entry per metric (1 page max)"
Quotable: "A “definition snippet” you can embed in dashboards (tooltip/glossary)"
Quotable: "Every metric needs someone accountable for its meaning and maintenance."

### TIMING, UPKEEP, OWNERSHIP, AND WHETHER IT IS STILL NEEDED

**[30] National Institute of Mental Health (NIMH) - "NIMH Data Management and Sharing for Applicants and Awardees" (grant-management guidance page).** primary. **fetched-and-verified.**
`https://www.nimh.nih.gov/funding/managing-your-grant/nimh-data-management-and-sharing-for-applicants-and-awardees`
Supports: Names "data collection instruments (also known as data dictionaries)" as a forward-looking, before-collection artifact, one side of the contested timing debate. Separately states that a shared dictionary is updated on an ongoing basis as the community's data model evolves
Quotable: "there are an enormous number of different data collection instruments (also known as data dictionaries) used in mental health research"
Quotable: "NIMH strongly encourages the mental health research community to use the same data dictionaries rather than to continue to invent new ones"
Quotable: "The NDA Data Dictionary is updated as researchers extend existing data collection instruments or create new instruments."
Quotable: "The NDA provides an online Data Dictionary with a searchable interface to find data structures that awardees are expected to use for new data collection."

**[31] NIMH Data Archive (NDA) - "Data Dictionary" page.** primary. **fetched-and-verified.**
`https://nda.nih.gov/data_dictionary.html`
Supports: Shows the operational mechanism a shared, centrally-governed data dictionary uses to stay current without becoming permanently stale: individual "structures" (entries) are versioned, can be marked obsolete, and submissions can be closed off to a superseded structure while a newer one takes over - a built-in deprecation path rather than a single static document
Quotable: "Each structure represents a standardized definition of a measure that has been defined by researchers."
Quotable: "Some structures are obsolete, superseded by newer structures, or were created to support legacy projects. This column will display "Allowed" or "No" to indicate whether or not submissions of new data are currently accepted in this structure."

**[32] Temple University Libraries - "Managing Your Data" research-data-management guide.** practitioner. **fetched-and-verified.**
`https://guides.temple.edu/datamgmt/managingdata`
Supports: The before-collection timing position: Temple defines a data dictionary as a record of the variables a project is going to collect. The page earns no claim on staleness, ownership or obsolescence, and is listed as a consulted source for the timing debate only
Quotable: "a data dictionary is a record of each variable and data field that you are going to collect in your project"

**[33] Nazabal, A., Williams, C. K. I., Colavizza, G., Smith, C. R. M., & Williams, A. (2020) - "Data Engineering for Data Analytics: A Classification of the Issues, and Case Studies" (arXiv preprint).** practitioner. **fetched-and-verified.**
`https://arxiv.org/pdf/2004.12929`
Supports: Directly states the staleness problem in named, general terms (metadata going missing or out of date) and frames ownership as a two-sided, unresolved split in practice: the data collectors normally supply the dictionary, but when that supply fails, the burden shifts onto the data scientist (consumer), who must infer it from the data itself or from a domain expert
Quotable: "it is not uncommon that this metadata is missing or out-of-date, making it necessary to infer it from the data itself"
Quotable: "In such cases, table understanding involves an interaction with a domain expert or the data collectors."
Quotable: "This information is normally provided by the data collectors"
Quotable: "Often the owners of the data provide this information directly to the data scientists"
Quotable: "but this is not always so."

**[34] Phillips, C., Price, A. M. H., Forbes, L., Boulange, C., Mengersen, K., Reeves, P., & Glauert, R. (2024) - "Guidelines for the Generation of Analysis Ready Data: A Case Study" (arXiv preprint; ten-step ARD framework, with a case study on the Australian Child and Youth Wellbeing Atlas, ACYWA).** practitioner. **fetched-and-verified.**
`https://arxiv.org/pdf/2403.08127`
Supports: Supports the after-collection side of the timing debate: the dictionary is the tenth and final step, built from data already collected. On ownership, it gives a worked, named example: the research team that holds the data creates entries manually, partly pre-filled by an automated summary tool, and the entries pass a quality-assurance process before two audiences read them, the project's own development team and external data users. That is a producer-creates, consumer-reads split with an explicit quality gate as the currency check
Quotable: "The data dictionary for each variable was created manually by the researchers on ACYWA and has undergone a quality assurance process."
Quotable: "These items will be provided to two different end users: users of the data and members of the ACYWA development team."
Quotable: "A similar process was followed in the creation of metadata, where Posit's Rmarkdown created a summary output with the key information and the ACYWA development team manually filled in the entries for the data dictionary."
Quotable: "The entries not covered by the Rmarkdown output are then entered manually be the researchers. These entries then undergo a quality assurance process."
Quotable: "These steps can also be repeated and updated as required."
Quotable: "The guidelines proposed in this paper inform ten steps in the generation of ARD: ethics, project documentation, data governance, data management, data storage, data discovery and collection, data cleaning, quality assurance, metadata, and data dictionary."
Quotable: "Generation steps often occur concurrently with one another (e.g., data cleaning and quality assurance)."

**[35] Deep Chatterjee - "No One's Reading Your Data Dictionary," Data Comeback newsletter (Aug 7, 2025).** practitioner. **fetched-and-verified.**
`https://data-comeback.beehiiv.com/p/no-one-s-reading-your-data-dictionary`
Supports: A named practitioner stating the staleness problem bluntly and prescribing the documentation-as-code fix (auto-generate from schema, version-control the file, assign an owner) as the cure for a hand-maintained dictionary going stale and unused
Quotable: "You wrote a data dictionary. It lives in a tab of a spreadsheet. It's outdated. No one uses it."
Quotable: "Auto-Generate Docs from Your Schema"
Quotable: "No more manually updating column definitions."
Quotable: "Treat Docs Like Code"
Quotable: "Version it. Update it when data changes. Assign ownership."

**[36] Atlan - "Documentation Drift Prevention: Strategies That Work in 2026" (vendor know-how page).** vendor. **fetched-and-verified.**
`https://atlan.com/know/documentation-drift-prevention-strategies/`
Supports: Names the staleness mechanism precisely (schema changes outrunning manual updates) and states an explicit ownership rule - documentation ownership follows the data-production hierarchy, i.e., the producing/maintaining team owns it, not the consumer - plus a review-cadence prescription (freshness SLAs) as the maintenance process
Quotable: "Documentation drift occurs when data documentation falls out of sync with the actual state of data assets, schemas, pipelines, and business definitions."
Quotable: "A schema change here, a team transition there, and within months the catalog descriptions that analysts rely on no longer match reality."
Quotable: "Ownership should follow the data production hierarchy: the team that creates or maintains a dataset owns its documentation."
Quotable: "Review frequency depends on change velocity. High-change assets like staging tables and ML feature stores should be reviewed weekly or trigger reviews on schema change. Stable production tables may need monthly reviews."

**[37] Craig S. Mullins - "The Rise of the Data Catalog," DBA Corner column, Database Trends and Applications (DBTA).** practitioner. **fetched-and-verified.**
`https://www.dbta.com/Columns/DBA-Corner/The-Rise-of-the-Data-Catalog-135766.aspx`
Supports: The obsolescence side of the debate: a named practitioner argues that the hand-maintained data dictionary is a dated predecessor whose core weakness, keeping definitions current by manual effort, is what the modern automated data catalog was built to fix, and recommends that organizations adopt a catalog instead
Quotable: "The term "data dictionary" is no longer in vogue, but it is a centralized location for storing and defining metadata."
Quotable: "The ability to keep the information in a data catalog up-to-date using automated discovery and search techniques solves the greatest failure point of Repository products-keeping the data fresh and useful without requiring tedious manual processes."
Quotable: "The era of the data catalog is upon us and most organizations should be looking to implement a data catalog soon, if they have not already."

**[38] Monte Carlo - "Data Catalog Vs. Data Dictionary: 5 Essential Differences" (vendor blog).** vendor. **fetched-and-verified.**
`https://www.montecarlodata.com/blog-data-catalog-vs-data-dictionary/`
Supports: The counter-argument to Mullins: names the same staleness failure in a hand-maintained dictionary, but concludes that the dictionary is not obsolete. It remains the precision layer that feeds a catalog and complements it, and most organizations need both rather than one replacing the other
Quotable: "A data dictionary is typically created and maintained by hand. Someone writes it, often using spreadsheets or a documentation tool, and then updates it as changes happen. This sounds simple, but in practice it rarely keeps pace."
Quotable: "Without a dedicated process, the dictionary drifts out of sync with reality."
Quotable: "If a dictionary is outdated, it loses trust. And in dynamic environments where data is constantly changing, stale documentation is a liability."
Quotable: "The answer in many cases is both, but not as separate, redundant efforts. Instead, they are complementary components of a unified data management strategy."
Quotable: "In practice, data dictionaries often feed into data catalogs."
Quotable: "In summary, most organizations will leverage both. The data dictionary ensures each system's data is well-defined, while the data catalog ensures anyone in the organization can find and understand the data they need. They work in tandem."

**[39] Arovy - "Why Most Salesforce Data Dictionaries Fail (And 3 Shortcuts That Actually Work)" (vendor blog).** vendor. **fetched-and-verified.**
`https://www.arovy.com/resources/blog/why-most-salesforce-data-dictionaries-fail-and-3-shortcuts-that-actually-work`
Supports: On ownership, argues for a single named accountable owner, such as a governance lead, an admin or a business-systems lead, who coordinates review and approval rather than writing every entry personally. That platform-governance role is distinct from both a pure producer and a pure consumer. On staleness, names the no-process failure mode explicitly and prescribes a recurring governance cadence, monthly or biweekly for fast-changing organizations, as the fix
Quotable: "No process for post-launch change (it goes stale immediately)"
Quotable: "Salesforce does not stand still. New fields show up, old ones linger, and meaning changes over time. Without a maintenance process, the dictionary becomes outdated and untrusted very fast."
Quotable: "This does not mean one person writes every definition. It means one person is accountable as the lead, responsible for keeping the project moving and the dictionary reliable"
Quotable: "Minimum viable operating rhythm: monthly (or every two weeks if your org changes fast)"
Quotable: "Ideal owners (depending on your org):"
Quotable: "COE or Data Governance Lead"
Quotable: "Salesforce Admin or RevOps lead"
Quotable: "Business Systems lead"
Quotable: "Each cycle, review and manage:"
Quotable: "Deprecated fields"
Quotable: "Definition drift (meaning changes over time)"

**[40] Read, K. B., LaPolla, F. W. Z., Tolea, M. I., Galvin, J. E., & Surkis, A. (2017) - "Improving data collection, documentation, and workflow in a dementia screening study," Journal of the Medical Library Association, 105(2).** practitioner. **fetched-and-verified.**
`https://jmla.pitt.edu/ojs/jmla/article/view/221/347`
Supports: A named case study, not a controlled experiment, from a clinical research project that merged three dementia-screening studies with over 900 variables on paper forms. It reports that the absence of a data dictionary, together with unclear variable names, raised the risk that new staff would misread the data, and made merging the datasets error-prone and hard to reproduce
Quotable: "The data in the forms were represented by variables with unclear, nonstandard names that were not documented in a data dictionary."
Quotable: "Once entered into SPSS, the process for merging the 3 datasets into 1 analysis dataset increased the risk of error and was not easily reproducible."
Quotable: "The documentation of these variables was also incomplete in scope, an issue exacerbated by the study's lack of a data dictionary. Without a complete dictionary, the data were less likely to be useful to those with whom the data might be shared."
Quotable: "Furthermore, the lack of a data dictionary combined with unclear variable names created the possibility for new study staff to misinterpret the data."

**[41] University of Zurich (UZH) University Library, Lunch & Learn series / SHARE-CTD doctoral program - "How Good Research Data Management Enables Reproducibility and Data Reuse: A Case Study of Clinical Trial Data" (event abstract page; presenter not named on the page).** practitioner. **fetched-and-verified.**
`https://veranstaltungen.ub.uzh.ch/angebot/details/64824?culture=en`
Supports: The closest thing to a measured outcome study that the research found. In a datathon, five teams using R and Python each tried to reproduce the primary findings of the CAO/ARO/AIO-04 rectal cancer trial, and all teams succeeded. The abstract lists a lack of complete data dictionaries among the challenges, yet the reproductions still succeeded. Only the event abstract was read, not a full paper or dataset, and it reports no controlled comparison of work with and without a dictionary
Quotable: "a multi-team datathon was organized to independently reproduce the trial's primary findings using anonymized patient-level data and supporting materials. Five teams employed R and Python to replicate key outcomes, tables, figures, and statistical analyses."
Quotable: "Despite minor discrepancies due to incomplete documentation or software differences, all teams successfully reproduced the primary results, confirming the reliability of the original findings."
Quotable: "Challenges-such as broken protocol links, lack of complete data dictionaries, and partially documented analytical decisions-highlight the importance of comprehensive RDM for enabling data reuse."

### THE GAP QUESTION: WHAT GOOD PRACTICE ADDS BEYOND THE COMMONEST SECTIONS

**[42] DDI Alliance - DDI-CDI 1.0 model documentation, SentinelValueDomain class.** standards. **fetched-and-verified.**
`https://docs.ddialliance.org/DDI-CDI/1.0/model/FieldLevelDocumentation/DDICDILibrary/Classes/Representations/SentinelValueDomain.html`
Supports: Missing-value codes and sentinel values are a distinct, formally modeled documentation element, separate from a field's ordinary value domain
Quotable: "Value domain for a sentinel conceptual domain."
Quotable: "Missing categories expressed as codes: -9, refused; -8, Don't Know; for a numeric variable with values greater than zero."
Quotable: "Sentinel values are used for processing, not to describe subject matter."

**[43] Open Contracting Partnership - Open Contracting Data Standard, governance documentation on field deprecation.** standards. **fetched-and-verified.**
`https://standard.open-contracting.org/latest/en/governance/deprecation/`
Supports: Deprecated or renamed fields are marked with a structured, machine-readable deprecation flag rather than silently dropped, and consuming systems must keep supporting them for a defined window before removal
Quotable: "Validation tools must report use of deprecated fields to the user"
Quotable: "Before a field or codelist value is removed, it will be first marked as deprecated in a major or minor release"
Quotable: "removal will only take place, subject to the governance process, in the next major version"
Quotable: "Deprecated fields are marked in the JSON schema with the presence of a deprecated property and object which declares the version number in which the field was first deprecated, and provides a description of the reason for this deprecation."

**[44] U.S. Census Bureau - Microdata API User Guide, Limitations, Contact Us & Appendix section.** primary. **fetched-and-verified.**
`https://www.census.gov/data/developers/guidance/microdata-api-user-guide.Limitations%2C_Contact_Us_%26_Appendix.html`
Supports: A government data publisher documents known quality caveats and defects at the level of specific fields/queries, separate from the normal field definition
Quotable: "Queries for custom statistics may not satisfy all data needs due to some functionality limitations"
Quotable: "challenges with the way variables are defined in a survey, and known defects."
Quotable: "Results are being incorrectly formatted as exponents in API queries that only have variables in the rows."

**[45] DataDriven.io - dimensional modeling course, "Defining the Grain" section.** practitioner. **fetched-and-verified.**
`https://datadriven.io/learn/data_modeling_dimensional/section/3`
Supports: The grain of a table (what one row represents) is treated as a required, testable statement distinct from, and prior to, the field-level definitions, and is tied explicitly to the primary/unique key columns
Quotable: "The grain of a fact table states what 1 row means, and it is decided before any column is added."
Quotable: "Naming the columns that enforce the unit is what lets another engineer write a test against it."
Quotable: "1 row per sale"
Quotable: "1 row per order"
Quotable: "1 row per order line item, unique on (order_id, line_seq)"

**[46] UK Data Service (University of Essex) - "Documenting and contextualising your data" training slide deck, Research Data Management Support Services.** practitioner. **fetched-and-verified.**
`https://dam.ukdataservice.ac.uk/media/440277/documentingdata.pdf`
Supports: A national data-archive service's own documentation checklist separates variable-level documentation (labels, codes, missing values, derivations/aggregations) from a distinct confidentiality/access-conditions category, and shows missing-value ranges recorded in a field all its own, apart from the value-label field
Quotable: "Variable-level documentation: labels, codes, classifications; missing values; derivations and aggregations."
Quotable: "Data confidentiality, access and use conditions: anonymisation carried out; consent conditions/procedures; access or use conditions of data."
Quotable: "compilation of derived variables"
Quotable: "SPSS: variable attributes documented in Variable View (label, code, data type, missing values)"
