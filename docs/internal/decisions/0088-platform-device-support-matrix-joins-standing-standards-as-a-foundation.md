---
status: accepted
date: 2026-11-09
decision-makers: [jprisant]
consulted: [claude]
---

# `platform-device-support-matrix` joins `standing-standards` as a `foundation`, its eighth member and fourth unforecast one

## TL;DR

- **Decision.** The `platform-device-support-matrix` bundle (catalog entry 212; issue #353, bundle:
  platform-device-support-matrix) declares **`family: standing-standards`** and **`classification: foundation`**.
  It becomes that family's eighth member, and the [contract](../contracts/standing-standards.md) moves to `0.7.0`.
- **What the type is.** It is a standing page that states which browsers, operating systems and devices a product
  supports, at what grade of support, and which of them the team tests on. It is not a per-release test
  environment list, which `test-plan` already holds.
- **Why a record is needed.** The contract's "likely future members" line (`standing-standards.md:46`) never named
  this type. Like ADR 0062 (production readiness review joins standing-standards), ADR 0071 (business continuity
  plan joins standing-standards) and ADR 0075 (test strategy joins standing-standards), it is admitted on the
  membership test and the falsifier alone.
- **What settled membership:** the family's falsifier. The matrix is consulted at the moment of action: when a team
  chooses which browsers to test, triages a bug report, or decides whether a fix or polyfill is owed.
- **What settled classification:** the contract's section 2 cut, "a standard you are judged against" against "an
  instrument you execute". A bug is judged against the matrix. Nobody executes the matrix under time pressure.
- **A consequence this record keeps rather than resolves by amendment: the cadence tension.** Section 1 says members
  are "not revised on a calendar". The strongest admitting source commits to an annual update. This record routes the
  tension to the bundle's Review Trigger section, as ADR 0071 and ADR 0075 did. This is the third time the family has
  met the tension, and the third time the clause stays as written.
- **Status:** accepted 2026-11-09. The maintainer asked for the admission sweep on 2026-11-08. Given its digest and a
  recommendation of this family and classification at medium confidence, the maintainer replied "Continue" on
  2026-11-09, which was first recorded as acceptance on delegation. The same day, asked whether to merge after
  reading the contract's Members line and `0.7.0` change note, the maintainer answered "Read it, merge". **The
  contract diff was read before it merged**, under the standing rule that every contract edit is read first.

## Context and Problem Statement

The seven Define reads of 2026-11-08 (PR #352) found that the device support matrix is not a `define` document. It
is a standing standard, and the maintainer asked for an admission sweep. The sweep ran four Sonnet agents through the
Agent tool on 2026-11-08: named sources, boundaries and cadence, internal fit across all eleven family contracts,
and a critic over the five admission checks. The main loop re-checked every returned quotation against raw page
text, from sources whose terms permit reading. All 37 passed. The working files are gitignored, at
`_local/research/2026-11-08_device-matrix-sweep/`.

**All five admission checks pass or do not apply.**

1. **Written document**, under ADR 0030 (templating scope: markdown documents) as read by ADR 0048 (one named source
   clears the admission test). Four named sources publish the matrix as a standing written page:
   - The GOV.UK Service Manual's page on designing for different browsers and devices, with a browser table and an
     update history. It says: "Decisions about compatibility cannot be something you specify at the start of your
     project and then forget about."
   - GOV.UK Frontend v5's browser support page, with four grades: "Each grade shows the level of support we will
     provide."
   - Yahoo's Graded Browser Support, on the YUI 3 wiki, with grades A, C and X: "A-grade support is the highest
     support level."
   - The Australian Digital Transformation Office's `BROWSER-SUPPORT.md`, in the archived gov-au-ui-kit repository.
     Its tables carry the columns Browser, Platforms, Minimum version, and support status, marked Tested or Untested.
   Two of the four are retired: the YUI wiki dates from about 2006, and the Australian repository was archived in 2018.
   The check passes on GOV.UK alone.
2. **Phase fit**, under ADR 0077 (the define phase ends with a chosen concept). Not applicable: the type takes a
   `classification`, not a phase.
3. **Written form**, under ADR 0078 (maps, canvases and session records are templatable through their written form).
   It passes: the type is a grade list and a table, the same shape `risk-register` and `raid-log` ship in Markdown.
4. **Not duplicated.** It passes. No shipped bundle holds a browser table or support grades. Two shipped files
   already point at the missing document: the GOOD example at `test-case_template-full.md:174-176` mentions "the
   browser matrix", and `test-case_companion.md:170` names a "browser or device matrix" as part of a case's
   environment.
5. **Software audience**, under ADR 0080 (admission gains a software audience check). It passes: every qualifying
   source is a software, design-system or government technology team.

## Decision Drivers

- Family membership (the falsifier) and classification (the cut) are separate questions. ADR 0058 (definition of
  ready joins standing-standards) warns that conflating them is the easiest way to get a member wrong.
- The classification must follow what the document does, not how its strongest quotation sounds.
- The cadence evidence is direct and recent, so it needs an explicit answer rather than a silent pass.
- An alternative family exists that fits the cadence better, and the record must say why it was not chosen.

## Considered Options

1. **`standing-standards`, `classification: foundation`.** Chosen.
2. **`standing-standards`, `classification: tool`.** Rejected: the timing half of the `tool` marker is not met.
3. **`governance-docs`, `classification: utility`.** Rejected: it fits the cadence but needs a purpose-phrase
   amendment for a document no product or program manager tracks.
4. **`qa-docs`.** Rejected: its members are produced at a stage and finished, and the matrix is not.
5. **Decline, or park.** Rejected on the evidence: four named sources clear admission, and two shipped files already
   point at the type.

## Decision Outcome

**Chosen: `standing-standards` with `classification: foundation`.**

### Why the family question tracks the falsifier

The falsifier reads: "if a candidate arrives that matches the cadence but is not consulted at the moment of action,
this family has been drawn around the axis rather than around a job" (`standing-standards.md:108-110`). The matrix
is consulted at three named moments. A tester consults it to choose browsers. A triager consults it to decide whether
a bug is owed a fix: GOV.UK Frontend says it will "treat bugs affecting Grade A browsers as high priority", and of
another grade, "We will not fix bugs affecting these browsers." A developer consults it before adding a polyfill.
**This bundle is the standing matrix.** A list of the browsers one release was tested on is a test plan's environment
section, and this bundle does not template it.

### Why `foundation`, marker by marker, against the honest `tool` case

| Marker | `foundation` | `tool` | A platform and device support matrix |
|---|---|---|---|
| What it is | "a standard you are judged against" | "an instrument you execute" | A bug report, a test run and a design choice are each judged against the grades it sets |
| When and by whom | "argued to, agreed by a team, and changed deliberately and rarely" | "usually under time pressure and often by someone who did not write it" | A frontend or design-system team agrees it, from analytics and user research. The GDS Way says "You should use analytics data and user research to determine whether you should regularly test in any other browsers." |
| Where authority comes from | "from having been agreed" | "from being correct right now" | From the agreed threshold and grades. USWDS states its rule: "We officially support any browser above 2% usage as observed by analytics.usa.gov." |

**The honest `tool` case.** People other than its authors consult the matrix, which matches the authorship half of
the `tool` marker. **What breaks the parallel is the timing half.** A runbook or a business continuity plan is
executed once a situation is declared. The matrix is consulted in the ordinary course of testing and triage, with no
declared event. That reading is this library's inference by analogy, the same inference ADR 0075 made. No source
tested when or under what pressure a matrix is applied. Confidence in the classification: medium.

### Why not `governance-docs`

The `governance-docs` contract fits the cadence, because its members are "set up once and maintained indefinitely"
(`governance-docs.md:13`). But its purpose phrase admits instruments "that a product or program manager uses to track
risk, open items, or performance". A matrix tracks none of these, and a frontend or design-system team keeps it.
Admitting it there would need one more clause in that phrase, as ADR 0084 (requirements traceability matrix joins
governance-docs) added one. `standing-standards` needs no widening of its membership clause.

### Why not `qa-docs`

`qa-docs` excludes a type whose job is not to "plan, specify, or report the verification of a product increment"
(`qa-docs.md:20`), and its members are produced at a stage and finished. The matrix is consulted by every increment
and finished at none. The sweep's internal-fit agent scored `qa-docs` as `excludes`, at high confidence.

### The cadence tension, recorded as a consequence rather than resolved by amendment

Section 1 says members are "not revised on a calendar" (`standing-standards.md:28`). Section 1 also routes a
candidate "revised on a cadence and valuable only while current" to `utility` (`standing-standards.md:41-43`). The
evidence against this family is direct. GOV.UK's update history records: "Commitment to update browser list updated
to annual." The GDS Way's browser page says it was "last reviewed on 13 July 2026" and "needs to be reviewed again on
13 July 2027".

**This record does not widen the contract to accommodate the tension.** Section 4 already requires every member to
carry a review trigger stated as a condition: what event makes the document wrong, and who notices. The matrix goes
wrong when usage moves. The GDS Way ties the list to analytics data and user research, and USWDS and the ONS tie
support to a 2% usage threshold. So the bundle's Review Trigger section names conditions: analytics show a browser
crossing the threshold, a grade changes, a new platform is adopted, or a bug is triaged against an unlisted browser.
The annual commitment is read as ADR 0071 read NIST's annual test: "a floor on how long the condition can go
unchecked, not a calendar rewrite". **The tension is recorded here, not argued away.**

**The weaker half of this reading.** The usage-driven reading rests on the threshold rules and the GDS Way line. The
sweep's readers summarised GOV.UK's "reviewed, no changes" history entries, and the main loop did not re-check them.
If those entries show the list rewritten each year whatever usage did, the `utility` reading gets stronger, and this
record is where to reopen it.

### The counter-arguments this record keeps

- **No forecast named this type.** It does not change the outcome, for the reason ADR 0057 (issue log joins
  governance-docs) gives: the membership test, not the forecast list, governs a candidate.
- **The evidence is narrow.** Every qualifying source is a government or design-system team. No commercial product
  team's matrix was read under a recorded terms verdict. A build should look for one.
- **Three cadence exceptions is a pattern.** ADR 0071, ADR 0075 and this record each read an annual figure as a floor.
  If a fourth candidate needs the same reading, the clause at `standing-standards.md:28` may be the thing that is
  wrong, and a contract amendment should be weighed instead of a fourth exception.

### Consequences

- `standing-standards` grows from seven members to eight. Its Members line and change note are updated in this
  change, moving it to `0.7.0`.
- Check K gates `classification` membership of the set `{foundation, tool}`. It cannot verify that this member picked
  the right value, so that stays a review obligation, argued above.
- At the bundle's landing, the catalog gains entry 212, numbered so that no existing entry number changes, as
  entries 209 and 211 were added at their landings.
- `tier2-specs.md` records the type as specced. The build waits for the sizes and example choices and
  for a build go, under ADR 0041 (maintainer preference sets the build order).

## More Information

- Family contract: [`standing-standards`](../contracts/standing-standards.md), adopted by
  [ADR 0032](0032-adopt-standing-standards-family-contract.md).
- The cadence precedents: [ADR 0071](0071-business-continuity-plan-joins-standing-standards-as-a-tool.md) and
  [ADR 0075](0075-test-strategy-joins-standing-standards-as-a-foundation.md).
- The family it does not join: [`governance-docs`](../contracts/governance-docs.md), widened most recently by
  [ADR 0084](0084-requirements-traceability-matrix-joins-governance-docs-as-an-eighth-member.md).
- The admission standard: [ADR 0030](0030-templating-scope-markdown-documents.md),
  [ADR 0048](0048-one-named-source-clears-the-admission-test.md) and
  [ADR 0080](0080-admission-gains-a-software-audience-check.md).
- Where the spec and the section design live: [`tier2-specs.md`](../tier2-specs.md).
