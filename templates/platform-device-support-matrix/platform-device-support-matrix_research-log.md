# platform-device-support-matrix: research log

Research conducted 2026-11-12. It builds on the admission sweep of 2026-11-08, held in a gitignored folder under
`_local/research/`, and on
[ADR 0088](../../docs/internal/decisions/0088-platform-device-support-matrix-joins-standing-standards-as-a-foundation.md)
(the platform and device support matrix joins standing-standards as a foundation). It also builds on the family
contract (`docs/internal/contracts/standing-standards.md`, 0.7.0) and on the spec, the section of
`docs/internal/tier2-specs.md` headed "standing-standards (eighth member): the platform and device support matrix".
The maintainer accepted ADR 0088 on 2026-11-09 after reading the contract change. On 2026-11-12 the maintainer asked
for the build, which this log reads as ruling the spec's remaining choices as recommended: a single `lean` size, the
Harbourline Bookings example with a stop rule, and the build go. This bundle is issue #353 (bundle:
platform-device-support-matrix), and it fills catalog entry 212.

The build ran six dimensions: origins, structure, practice, debates, relationships and the gap question. The working
files are numbered by return order: `dim1.md` holds relationships, `dim2.md` structure, `dim3.md` debates, `dim4.md`
practice, `dim5.md` origins and `dim6.md` the gap question.

**36 sources are recorded below, and all 36 are fetched-and-verified.** By tier they are 24 primary, 6 practitioner,
4 vendor and 2 standards. The vendor and most practitioner entries were read as repository source on GitHub.

## What the checks caught, and what was not read

**Every quotation was checked against raw text**, never against a retrieval tool's summary. Of the 132 quotations the
agents returned, 123 passed on the first check. Eight of the nine failures were quotations copied from Markdown
source formatting, such as link brackets, table pipes or HTML tags, checked against the rendered page. The main loop replaced each
with the rendered wording, and each replacement passed. The ninth, a sentence from the ISTQB syllabus [21], survives
only as its second clause.

**The main loop also added quotations of its own,** each tested against the same raw text. Beyond the replacements
above, it added three AusDTO headings [7], six lines from the GDS Way page [9] and seven entries in the GOV.UK Service
Manual's update history [8]. The GDS Way lines give its rule for declining a fix and its page owner, which the practice
dimension described without quoting. After the four-lens review it added two YUI lines [1] that characterise the C
and X grades, which this log had stated without a logged quotation. **Three quotations that passed against the cached
copy failed a fresh fetch,** one from Browserslist [17] and two from GitHub's browser-support README [14], and they
were dropped. The facts they carried stay in those entries' Supports lines.

**The Service Manual's history bears on a question ADR 0088 left open.** The record said that if GOV.UK's history
showed the list rewritten each year whatever usage did, the `utility` reading would get stronger. The history does not
show that, as the Practice section below sets out. *(Corrected 2026-11-12, after the four-lens review: this paragraph
first said the entries settle the question, and the Practice section read them as yearly reviews. The review-only
entries date from 2020 and 2021, about six months apart, before GOV.UK's annual commitment of 2024.)*

**The AusDTO column set is now quotable.** The admission sweep found that no quotation of the AusDTO table headers
passed the recheck, so the spec asked the build to label the column set a POSITION. The rendered header row, "Browser
Platforms Minimum version Advanced support status", passes against the page [7].

**Terms were checked against the 2026-11-08 verdicts first, and three new hosts were cleared after the read.** Every
research prompt named the six hosts the sweep had cleared and told the agent to record a verdict before reading any
other host. Three other hosts were read.

- **`developer.mozilla.org`.** The debates dimension recorded a verdict inside its source entries, and the log cannot
  establish whether it read the terms before or after the content pages. The main loop re-read Mozilla's website terms
  and acceptable use policy raw on 2026-11-12. Neither has a clause on automated access, and MDN's content is licensed
  CC-BY-SA. Permits, at high confidence.
- **`resilientwebdesign.com`.** It has no terms page at the usual paths, and its home page carries a Creative Commons
  Attribution-ShareAlike 4.0 licence. Permits, at medium confidence, because a licence statement is not a terms page.
- **`raw.githubusercontent.com` and `api.github.com`.** The origins and gap dimensions read GitHub files through these
  GitHub-operated hosts, and the origins dimension flagged the deviation itself. GitHub's acceptable use policy
  governs its whole service and bars scraping only for spam and excessive bulk load. Permits, at high confidence.

**One site bars reading, and its page was not read.** Red Hat's terms forbid a robot, spider or retrieval application.
The practice dimension read only that terms page and left Red Hat's browser support page alone. It is listed in the
section after the sources.

**Not read, because the host's terms were unresolved or unchecked.** Greenhouse's help-centre browser page, the best
commercial candidate found, has no website terms the practice dimension could find. Filament Group's page arguing that
components rather than browsers should be graded returned a missing terms page. Also unread: the BBC's original post
on capability testing, the Wayback copy of Yahoo's first Graded Browser Support article, the YUI Blog's update posts,
the WebAIM screen reader survey, the 2016 GOV.UK assistive technology survey, the ONS accessibility statement, two
GOV.UK Design System pages on `design-system.service.gov.uk`, and Enalyzer's help page. The Jenkins policy was read
from its source on GitHub [12], because `jenkins.io` carries no website terms. No claim below rests on any unread page.

## Findings

### What the type is

**A standing page that states which browsers, operating systems and devices a product supports, at what level, and
which the team tests on.** GOV.UK Frontend puts the purpose in one line: "Each grade shows the level of support we
will provide." [6] YUI gives the principle behind the grades: "Support does not mean that everybody gets the same
thing." [1] The page is consulted when a team picks browsers to test, triages a bug from an unusual browser, or
decides whether a polyfill is owed. Those three uses are documented in the Practice section below.

### Origins: YUI's grades, and a shared vocabulary rather than a documented lineage

**Yahoo's Graded Browser Support is the earliest scheme read.** "There are three grades: A-grade, C-grade, and X-grade
support." [1] "C-grade is the base level of support, providing core content and functionality." [1] Of the X grade,
"QA does not test, and bugs are not opened against X-grade browsers." [1] The wiki page lists dated updates from
2008-02-19 to 2012-07-26 and does not give the original publication date or the author.

**Authorship rests on one secondary statement.** Springer Nature's frontend playbook calls the scheme "a concept
originally conceived by Nate Koechley" [5]. The original Yahoo article was not read, so the date and the author are
leads, at low confidence.

**GOV.UK Frontend uses four grades, and no source read says they descend from YUI.** Its grades are A, B, C and X
[2], [6]. A 2023 issue records the move: "We're exploring moving towards a graded browser support model where we don't
always aim to provide exactly the same experience to every user." [4] None of the GOV.UK pages or issues read names
Yahoo or YUI. **The letters also mean different things.** YUI's C is a core-content grade for incapable browsers, and
its X is untested but assumed capable [1]. GOV.UK's C is a reduced grade, and its X gets no fixes: "We will not fix
bugs affecting these browsers." [6] The library should call this a shared vocabulary, not a documented lineage.

**One commercial team names YUI as its model.** Springer Nature says it implements graded support "using a variant of
Yahoo's Graded Browser support" [5], by "classifying all versions of all browsers into one of two levels" [5].
**AusDTO's file is a parallel form.** It defines two support levels and marks rows tested or untested, and it never
names YUI or uses grade letters [7].

### Structure: the seven sections tested, and the second size not earned

**The spec's seven sections, against what the sources carry.**

| Section | Result |
|---|---|
| Purpose and Scope | Supported. AusDTO opens with its purpose: "The UI-Kit team needs to support all of our users, regardless of their device, web browser or other user agent." [7] A statement of which product the matrix covers, and whether this file or a tool is the record, is the library's POSITION |
| Support Grades | Supported by GOV.UK Frontend's four grades, each with a test commitment and a bug commitment [6], by YUI's three [1], by Jenkins' three levels [12] and by two-level schemes [5], [7] |
| The Matrix | Supported. AusDTO publishes a mobile table and a desktop table [7], the Service Manual a table keyed by operating system [8], and Jenkins a table keyed by level and version rule [12]. The column set is discussed below |
| Threshold Rule | Supported by USWDS [10], the ONS [11] and the Service Manual's coverage figure [8]. Browserslist argues for a query instead [17] |
| Unsupported Browsers | Supported under two names. AusDTO has a section with this heading, whose body says "Other combinations may be supported but have not been extensively tested" [7]. GOV.UK Frontend carries the content as Grade X [6], and Jenkins as its default level [12]. The GDS Way gives a rule for out-of-policy bugs [9] |
| Ownership | Supported by the GDS Way's named page owner [9] and by GitHub's named team for polyfill removal [14]. The role names are the library's POSITION |
| Review Trigger | Contract-mandated. Supported by the GDS Way's review dates [9], the Service Manual's dated history [8], Jenkins' dated change history [12] and MetaMask's rule to warn users before raising a minimum [15]. The table form is the library's POSITION |

**The column set.** AusDTO's mobile header row is "Browser Platforms Minimum version Advanced support status" [7], and
its desktop table has no minimum version column. The single status column holds both the level and the test status.
The Service Manual's table pairs an operating system with a browser and puts versions inside the cells [8]. **No
source has separate Grade and Tested columns, and none has a Notes column**, so those three columns are the library's
POSITION. The separation has support all the same. The GDS Way separates what a team builds for from what it tests:
"The exact set of browsers you build for will vary by project" [9]. MetaMask supports browser forks it does not test:
"We try to support browser forks as well (aligned with supported Chrome/Firefox releases), but we don't actively test
them." [15]

**Version rules compete with minimum versions.** MetaMask states a window, "The last two years of Chrome stable
releases" [15]. Material Components Web states "We officially support the last two versions of every major browser.
Specifically, we test on the following browsers:" [16] Jenkins uses N and N-1 rules per level [12]. So the column
the spec calls Minimum version is better asked as a minimum version or a version rule. That is the library's
synthesis, at medium confidence.

**The second size is not earned.** The structure dimension looked for per-row evidence columns, such as a usage share
or a date last verified, and for a separate polyfill or progressive-enhancement policy section. It found neither in
the three pages it read [6], [7], [8]. The commercial pages were not checked for per-row columns. GitHub's
browser-support README documents a polyfill policy, but as a separate document beside the matrix, not as a section of
one [14]. The nearest things are AusDTO's principles list and a dated history kept for the whole page [8], [12], which
the Review Trigger section already holds. **The single `lean` size stands, at medium confidence**, up from the spec's low.

### Practice: who keeps a matrix, and what it is consulted for

**Commercial teams keep standing support pages, and none read pairs grades with a stated update policy.** The spec's
weakest claim was that every source was a government or design-system team. The practice dimension read five
commercial support pages, each as repository source on GitHub. The gap dimension adds two commercial pages on
assistive technology, from Deque [24] and Basecamp [25]. GitHub's help page names the latest browsers and gives a best-effort statement
for extended-support releases, with no grades [13]. MetaMask states version windows and a rule for raising them [15].
Material Components Web defines its support as the set it tests [16]. GitHub's browser-support library ties a code
baseline to the matrix: "to ensure that our baseline moves with our browser support matrix" [14]. Springer Nature
uses two levels [5]. **The open-source Jenkins project is the one non-government source in which this log records
levels, a matrix and a dated change history together** [12]. YUI has grades and a dated update archive, and links to
a separate matrix page that was not read [1]. The caveat narrows: commercial teams publish support statements, and
among them only Springer Nature was found with levels [5]. High confidence for what was read. The best commercial candidate with
tiers, Greenhouse, stayed unread under the terms rule.

**Who owns it.** The GDS Way page is "reviewed again on 13 July 2027" according to its own footer, and names its
owner: "by the page owner #frontend" [9]. GitHub's library names a team that decides whether a polyfill can go [14].
No source names a person or role who may change a grade, so the Ownership section's role names are POSITION.

**What it is consulted for.**

- **Choosing test browsers.** The GDS Way: "You should use analytics data and user research to determine whether you
  should regularly test in any other browsers." [9] The ONS adds any browser used by 2% of a service's users [11].
- **Triage of an out-of-policy bug.** The GDS Way: "You may receive reported issues on browsers outside of your normal
  policy. You should still investigate these issues, assess their impact, and consider how to address them." [9] It
  then lists three grounds for declining a fix, including "fixing the issue would require disproportionate engineering
  effort" and "a feature of your service inherently relies on an unsupported feature" [9]. Jenkins makes its lowest
  level the default: "This is the default unless a browser/version is listed" [12]. GitHub asks a reporter of a
  pre-release bug to "please verify that it also exists in the stable version of the same browser" [13].
- **Polyfills and monitoring.** GitHub's library decides polyfills against the matrix and keeps unsupported browsers
  out of its error monitoring [14]. No government source names the monitoring use.

**How it changes.** By a usage threshold [10], [11]. By dropping a browser: USWDS records "the Design System no
longer supports Internet Explorer 11" [10], Jenkins "2022-02-01 - Remove support for Internet Explorer, Add Edge"
[12], and the Service Manual "Updated the list of browsers to support, removing Internet Explorer. Added some
information on circumstances when it should still be supported." [8] These entries record the drop and not its cause,
so reading each as a vendor ending support is this log's inference. By discussion: each Jenkins change links to a
mailing-list thread or a governance meeting, as entry [12] records. And with notice: MetaMask says "before bumping our
minimum supported browser versions, we should always notify users in the application first." [15]

**How often, and how far ADR 0088's reading holds.** The Service Manual's history records reviews with no change,
each based on usage: "Reviewed list of browsers to make sure it's still current, based on recent usage figures for
GOV.UK. No change from the January 2021 version of the list." [8] Those review-only entries date from 2020 and 2021,
about six months apart. Three change entries cite usage: "Removed requirement to test with Safari 11 and earlier
versions, as they fall outside of the 95% most popular browsers." [8], "Removed requirement to test on Windows phone,
as it falls outside of the 95% most common browser/device combinations." [8] and "Updated the requirement to test in
Safari for iOS from 9.3 to 10.3 to reflect usage statistics." [8] Other changes, such as removing Internet Explorer,
cite none. The annual commitment came later: "18 September 2024 List of browsers to test in updated. Commitment to
update browser list updated to annual." [8] **So the list changed when usage moved, and periodic reviews checked
whether it had.** The history shows usage-driven change and periodic review, not a yearly cycle, at high confidence
for GOV.UK and unknown for anyone else. Reading today's annual commitment as a floor on how long the condition can go
unchecked, as ADR 0088 does, is this log's inference from that history, at medium confidence. Jenkins' history shows
a few changes over about a decade, each linked to a discussion [12]. That cadence is also this log's inference, at
medium confidence.

### Debates: thresholds, queries and capability tests

**A fixed usage threshold, against a query or judgment.** USWDS: "We officially support any browser above 2% usage as
observed by" its government analytics service [10]. The ONS: "if your service’s analytics data shows at least 2% of
your users are using a different browser or version, then you will need to test against that as well." [11] GOV.UK
states coverage instead: "The list in the table represents approximately 98% of the most popular browsers used on
GOV.UK." [8] Browserslist argues against a usage floor alone, warning that it "will in the long run make popular
browsers even more popular" [17], and lets a team query "statistics derived from your real-world traffic rather than
global marketshare" [17]. Each figure is one team's choice for its own traffic. The 2% and 98% are not norms.

**Supported against tested.** The sources use support in different senses. Material Components Web defines the
supported set as the tested set [16]. MetaMask supports forks it does not test [15]. YUI's X grade is untested but
assumed capable [1], and GOV.UK Frontend says of a lower grade that it "will not regularly test in these browsers"
[6]. A matrix that does not define its words inherits that ambiguity. That is this log's synthesis, at high
confidence that the senses differ.

**Capability tests against named versions.** MDN defines progressive enhancement as delivering "a baseline of
essential content and functionality to as many users as possible" [18], and calls browser sniffing "a terrible
practice that should be discouraged at all costs" [19]. Jeremy Keith: "There is a difference between support and
optimization." [20] and "Browsers that don’t cut the mustard still get access to the content, but without the
JavaScript enhancements." [20] **The camps coexist in practice.** The Service Manual keeps a browser list and also
says "Use progressive enhancement to give your service the best possible chance of working for the majority of your
users." [8] No source read argues that a support matrix document is the wrong tool. That step is not made here.

**Whether a graded list is overhead for a small team.** No source read argues it either way. This is a null result.

### Relationships with neighbouring documents

**The library's own templates already point at a matrix that does not exist.** Read from the working tree on
2026-11-12:

- `test-case_template-full.md:165-167` opens Environment and Configuration with "device or browser matrix", and its
  GOOD text at `:174-176` says "the accessibility cases cover the browser matrix separately". Its TRAP at `:178`
  warns against listing a matrix nobody will run.
- `test-case_companion.md:168-170` describes the section as holding "browser or device matrix".
- `test-plan_template-lean.md:119` holds environments as deployment tiers, and `test-plan_template-full.md:102`
  scopes compatibility in or out with no browser list.
- `test-strategy_template-lean.md:132` covers default tooling and environments, with no browser defaults.
- `bug-report_template-lean.md:110` and `:117-121` record one observed browser, device and OS per bug, with no field
  for whether that configuration is supported. The full variant repeats it at `:115`.
- `prd_template-full.md:161` opens Non-functional requirements, and nothing in the PRD bundle names compatibility,
  browsers or devices.

The quoted phrases in that list are the templates' own words, not sources. **The matrix is the shared reference the
test case, test plan and bug report point to.** That is this log's inference, at medium confidence.

**The standards body places environments elsewhere.** ISTQB lists compatibility among the quality characteristics and
names "test environment requirements" among test design work products: "Test design work products include:
(prioritized) test cases, test charters, coverage items, test data requirements and test environment requirements."
[21] It names no browser or device matrix. The GOV.UK quality assurance page states a goal, that a service "is easy
to use for anyone who needs to use it, regardless of the device they’re using" [22], and names no document that
records coverage.

### The gap question, routed under decision procedure 12

The gap dimension did not read this bundle's spec sections first, and read no file under `templates/`. Each candidate
is routed here. **None adds a section.**

| Candidate | Source | Route |
|---|---|---|
| Assistive-technology combinations | GOV.UK publishes a table: "your service must work with at least the following combinations of assistive technologies and browsers before it goes into public beta" [23]. Deque includes a combination if it would "be used by more than 1% of users" [24]. Basecamp tests one combination and then a secondary [25] | **The one real absence.** GOV.UK keeps the table on its own page [23], so the matrix should say where those combinations live, not hold them. An ASK in Purpose and Scope and a guide rubric row. Confidence medium |
| JavaScript off, or a slow connection | GOV.UK makes this a build rule: "Some users may deliberately turn off features in their browsers. You should respect their decision and make sure those users can still use your service." [27] Performance pages treat bandwidth as a budget [28], [29] | Not a matrix dimension. Unsupported Browsers may point at the progressive-enhancement rule |
| Viewport sizes | The ONS: "We use a set of device agnostic breakpoints to change the layout when best suited as opposed specific devices." [30] USWDS likewise [31] | Null. No source makes a viewport a support commitment |
| Native apps and operating-system versions | The GOV.UK app's terms state "iPhones running iOS 16 or later" [33] | Supports a minimum version on mobile rows. No source puts app and web support in one table |
| Telling users about a support change | MetaMask's in-app notice [15], AMP's rule to "Allow at least 2 weeks of open discussion after the I2D is created before proceeding with the deprecation of the feature" [34], and Cockpit's login message naming "which browsers do work" [35] | Review Trigger's action column, and a rubric row. Confidence medium |
| Audience exceptions | The Service Manual lets evidence make "a case for not meeting these browser requirements" [8]. The ONS exempts internal-only services [11] | An ASK in Purpose and Scope |
| A dated effective-from line on the matrix | The Service Manual heads its table "Browsers to test in (from February 2026)" [8] | A field in The Matrix. Low cost, medium confidence |

**Not found:** a filled, team-owned matrix with assistive-technology rows, a viewport floor stated as a commitment, a
government page on telling end users about a dropped browser, and a source arguing that a graded list costs a small
team too much.

## Claims flagged contested or time-bound

- **Lineage.** That GOV.UK's grades descend from YUI is not documented [1], [4], [6]. Treat it as shared vocabulary.
- **How many grades.** YUI has three [1], GOV.UK four [6], Jenkins three levels [12], and Springer Nature and AusDTO two
  [5], [7]. Graded support is not a fixed three-grade standard.
- **What support means.** Tested [16], or promised but untested [15], [1]. A matrix must define the word.
- **The unit of support.** A usage threshold [10], [11], a coverage figure [8], a query [17] or a capability test [18],
  [19], [20].
- **Where assistive technology belongs.** A separate page and table [23], or one support set [26]. No source argues
  the question directly.
- **Time-bound.** The Service Manual's list is dated "from February 2026" and was last updated 30 January 2026 [8]. The
  GDS Way page was last reviewed 13 July 2026 [9]. Entry [6] is the GOV.UK Frontend v5 page and entry [2] the latest
  version. AusDTO's repository was archived in 2018 [7]. YUI's updates end in 2012 [1]. The GOV.UK assistive technology
  table was last updated 24 May 2022, as entry [23] records. The 98% and 95% figures describe GOV.UK's own traffic [8].

## Honest framing

**A support matrix makes two different promises, and its worth is in keeping them apart.** One is what a user on a
given browser will get. The other is what the team will actually test. The sources use the word support for both,
and the GOV.UK Service Manual list is a list of browsers "to test in" [8]. The bundle's sharpest teaching point is
that a matrix must define its grades by their commitments and mark testing separately.

**The evidence is public matrices from government, design-system and open-source teams, plus a handful of commercial
support statements.** Commercial teams publish support statements, mostly as version rules without grades. No source
shows that a matrix improves outcomes, and no source measures what keeping one costs. **Every threshold read is one
team's choice for its own traffic.** The guide must not say every software team keeps one, and it must not present 2%
or 98% as a standard.

## Notes for the companion

**Facts the companion must carry.**

- Grades are defined by commitments: what is tested and how bugs are treated [6], [1], [12].
- Support and testing are different commitments, and the sources use support in different senses [16], [15], [1].
  This is the sharpest teaching point.
- GOV.UK's reviews check usage, and the list changes when usage moves [8]. The reviews quoted date from 2020 and 2021,
  about six months apart, and the annual commitment dates from 2024. Present the review trigger as conditions, with the
  annual floor last, and label the floor reading as the library's inference.
- The three uses: choosing test browsers [9], [11], triaging out-of-policy bugs [9], [12], [13], and polyfill and
  baseline decisions [14].
- Thresholds, queries and capability tests are camps, each with a source [10], [11], [17], [18], [19], [20].
- The relationships with test case, test plan, bug report and PRD, as the library's own templates show them.

**Hazards.**

- **Folklore presented as standard, this family's named hazard.** The 2% rule is USWDS's and the ONS's [10], [11], and
  98% is GOV.UK's coverage of its own traffic [8]. Attribute each. Deque's 1% is for assistive technology [24].
- **Lineage.** Do not say GOV.UK descends from YUI. Do not state YUI's publication date or author as fact; attribute
  the author to Springer Nature [5].
- **Commercial evidence.** Name the five commercial pages and say what each lacks. Do not write that commercial teams
  keep graded matrices; only Springer Nature's two levels were read [5].
- **The GDS Way** says its content is intended for internal use by the GDS Digital Products community. Cite it as a
  government team's own guidance, not as a standard.
- **No invented cadence.** The sources give an annual commitment from 2024 [8], an annual review date [9], review-only
  entries about six months apart in 2020 and 2021 [8], and changes linked to usage or discussion [8], [12], [15].
- **Separate Grade and Tested columns, a Notes column, the role names and the trigger table** are the library's
  POSITION. Say so where they appear.
- **Example reuse.** Grep the template for the example's product, team and people names before review.

**The section design for the template, as this research leaves it.** Seven sections in the spec's order. The Matrix
asks for Browser, Platforms, a minimum version or version rule, Grade, Tested, and Notes, with a mobile table and a
desktop table and an effective-from date. Purpose and Scope asks where assistive-technology combinations live and
which audiences are exempt. Review Trigger is a three-column table of Condition, Owner and What They Do About It, and
its candidate conditions are these: a browser crossing the threshold [10], [11]; a vendor ending support, where the
sources record the drop of a browser and not its cause [8], [10], [12]; a new platform adopted; a bug triaged against an unlisted browser [9]; and the annual floor [8], [9]. Telling
users about a raised minimum belongs in the action column [15], [35]. The new-platform condition is the library's
synthesis.

**The example.** The matrix for Harbourline Bookings, a passenger-ferry booking site run by a small fictional operator,
`lean` size. The family contract weakens the Acme Analytics chaining on purpose (`standing-standards.md:154-158`), so a
fresh scenario is allowed and the example need cite no sibling. It must be independent of the template's own GOOD and
WEAK text. **Facts the example must carry, with no contradiction:**

- A mobile table and a desktop table, with Grade, Tested or Untested, and a minimum version or version rule on every
  mobile row.
- At least one row whose promise is higher than its testing: a browser at a supported grade marked Untested, with the
  reason.
- A threshold row that moved: a browser fell below the operator's line and was demoted, with the analytics date and
  the owner who decided.
- A Review Trigger table whose rows include one that fired during the example's own history, so the trigger is shown
  working.
- A line saying where the assistive-technology combinations live.
- Every figure labelled illustrative. No real operator, brand or traffic number appears, and the threshold is the
  operator's own choice, not presented as a norm.

**The stop rule.** If the filled example reads as a table of browser names with no decision visible in it, the build
stops and the decision returns to the maintainer, as ADR 0064 and ADR 0074 record. A matrix whose every row is simply
supported shows no judgment.

## Sources

### Origins: graded support, and a shared vocabulary rather than a lineage

**[1] Yahoo YUI team - Graded Browser Support (yui/yui3 wiki on GitHub).** primary. **fetched-and-verified.**
`https://github.com/yui/yui3/wiki/Graded-Browser-Support`
Supports: Existence and definitions of YUI Graded Browser Support: three grades (C, A, X), what each means, what QA does for each, and the dated update archive (2008-02-19 to 2012-07-26). C-grade browsers are characterised as identified, incapable, antiquated and rare, and X-grade browsers as assumed to be capable and modern. The page links to a separate YUI Target Environments Matrix page, which was not read, so whether YUI published a browser-by-grade matrix is not recorded here. Does NOT state the original publication date or the author
Quotable: "There are three grades: A-grade, C-grade, and X-grade support."
Quotable: "C-grade is the base level of support, providing core content and functionality."
Quotable: "A-grade browsers should be identified on a whitelist."
Quotable: "Summary: A-grade browsers are identified, capable, modern and common. QA tests all A-grade browsers, and bugs are addressed with high priority."
Quotable: "X-grade browsers are all browsers not designated as any other grade."
Quotable: "QA does not test, and bugs are not opened against X-grade browsers."
Quotable: "Support does not mean that everybody gets the same thing."
Quotable: "This page is the permanent home of the GBS strategy."
Quotable: "Summary: C-grade browsers are identified, incapable, antiquated and rare."
Quotable: "X-grade browsers are assumed to be capable and modern."

**[2] GOV.UK Design System team - Browser support (GOV.UK Frontend documentation, latest version).** primary. **fetched-and-verified.**
`https://frontend.design-system.service.gov.uk/browser-support/`
Supports: GOV.UK Frontend defines four grades (A, B, C, X), each tied to testing level and bug priority; IE11 JavaScript removed from v5.0.0. The page does not mention Yahoo or YUI
Quotable: "the Design System team has divided browsers into 4 grades."
Quotable: "Each grade shows the level of support we will provide."
Quotable: "treat bugs affecting Grade A browsers as high priority"
Quotable: "We will not regularly test in these browsers. We will not fix bugs affecting these browsers."

**[3] GOV.UK Frontend team - How we provide support for different browsers (alphagov/govuk-frontend contributor docs).** primary. **fetched-and-verified.**
`https://raw.githubusercontent.com/alphagov/govuk-frontend/main/docs/contributing/browser-support.md`
Supports: The same four-grade scheme in the maintainers' own contributor docs, plus the necessary versus optional enhancement split. Contains no mention of Yahoo, YUI or 'graded' as a lineage statement. Commit history via the GitHub API shows the file's first commit on 2023-10-24 and a Grade C Safari minimum bump on 2024-06-17
Quotable: "we group browsers into 4 grades"
Quotable: "grade X - All other browsers (including IE11 and older)"
Quotable: "All other browsers (including IE11 and older)"

**[4] GOV.UK Frontend team - Explore frameworks to help us make decisions about browser support for features (alphagov/govuk-frontend issue 3293, opened 2023-02-15).** primary. **fetched-and-verified.**
`https://github.com/alphagov/govuk-frontend/issues/3293`
Supports: GOV.UK Frontend adopted the phrase 'graded browser support' in 2023 as a move to a model where not every user gets the same experience; the issue bodies do not name Yahoo or YUI (regex check on all three bodies returned no match)
Quotable: "We're exploring moving towards a graded browser support model where we don't always aim to provide exactly the same experience to every user."

**[5] Springer Nature frontend team - Browser support (springernature/frontend-playbook).** practitioner. **fetched-and-verified.**
`https://github.com/springernature/frontend-playbook/blob/HEAD/practices/graded-browser-support.md`
Supports: A named adopter that says in its own text it uses a variant of Yahoo's Graded Browser Support and credits Nate Koechley with the concept; it uses two levels (Core, Enhanced), not three. PR #253 (merged 2018-08-23) renamed the document from 'Graded browser support' to 'Browser support'
Quotable: "classifying all versions of all browsers into one of two levels"
Quotable: "implement it using a variant of Yahoo's Graded Browser support"
Quotable: "a concept originally conceived by Nate Koechley"

### Structure: what published matrices carry

**[6] GOV.UK Design System team - Browser support (GOV.UK Frontend v5 documentation).** primary. **fetched-and-verified.**
`https://frontend.design-system.service.gov.uk/v5/browser-support/`
Supports: Grades are carried as four prose-and-list blocks (A, B, C, X), not as a table. Each grade carries a definition, a test commitment and a bug-fix commitment. On the page, the sentence on disabling or reducing features and the sentence that begins 'will not regularly test' sit under Grade C, and 'We will not fix bugs affecting these browsers.' sits under Grade X, where the not-regularly-testing sentence is repeated. The page has no per-row usage share, no verified-date column, and no separate polyfill or progressive-enhancement policy section. Cached copy dated 2026-11-08, so the page is the v5.x one, not the v6.x 'Latest' version
Quotable: "the Design System team has divided browsers into 4 grades. Each grade shows the level of support we will provide."
Quotable: "treat bugs affecting Grade A browsers as high priority"
Quotable: "treat bugs affecting Grade B browsers as low priority unless we find evidence they prevent a user from being able to complete their task"
Quotable: "will not regularly test in these browsers"
Quotable: "We will not fix bugs affecting these browsers."
Quotable: "However, we might disable or reduce features on an individual basis in browsers where the underlying features are not available."

**[7] Australian Digital Transformation Office - Browser support (AusDTO/gov-au-ui-kit, archived 2018).** primary. **fetched-and-verified.**
`https://github.com/AusDTO/gov-au-ui-kit/blob/develop/BROWSER-SUPPORT.md`
Supports: Exact column headers of the matrix, read from the raw Markdown. Two tables, mobile and desktop, with different column sets. A short section sequence follows: Unsupported browsers, Advanced support, Functional support, Principles. The repository was archived by its owner on Mar 5, 2018, so the file is a frozen 2018-era artifact. The raw body was fetched via the github.com /raw/ URL, which redirected to raw.githubusercontent.com. The cache also holds an older rendered-HTML copy under the blob URL, which I read first. The raw text is now stored in the cache under the raw.githubusercontent.com URL; A government UI kit with a browser table (Browser, Platforms, Minimum version, Advanced support status of Tested or Untested) and two named levels, advanced and functional. It does not name YUI or Yahoo and does not use the grade letters, so it is a parallel form, not a documented descendant
Quotable: "Browser"
Quotable: "Platforms"
Quotable: "Minimum version"
Quotable: "Advanced support status"
Quotable: "All browsers listed are latest stable release, except Internet Explorer."
Quotable: "We list commonly used browsers and devices and their rough test status. Other combinations may be supported but have not been extensively tested."
Quotable: "We define ‘support’ as:"
Quotable: "This repository was archived by the owner on Mar 5, 2018."
Quotable: "The UI-Kit team needs to support all of our users, regardless of their device, web browser or other user agent."
Quotable: "We define 'support' as:"
Quotable: "Browser Platforms Minimum version Advanced support status"
Quotable: "Minimum version based on support for CSS Flexible Box layout modules"
Quotable: "This document has drawn on analytics data from various major"
Quotable: "Progressive enhancement over graceful degradation"
Quotable: "Mobile browsers"
Quotable: "Desktop browsers"
Quotable: "Other combinations may be supported but have not been extensively tested"
Quotable: "Unsupported browsers"

**[8] GOV.UK Service Manual - Designing for different browsers and devices.** primary. **fetched-and-verified.**
`https://www.gov.uk/service-manual/technology/designing-for-different-browsers-and-devices`
Supports: A two-column 'Operating system | Browser' test list, dated 'from February 2026', with a coverage figure (approx 98%) and a prose rule to use analytics for anything else. The page carries a full dated update history. The history has six or more review-only entries that read 'Reviewed list of browsers ... No change from ...', and the change entries after them record list changes. The page has no grade column, no Tested column, no usage-share column and no per-row verified date. It names no polyfill policy section, only a one-line 'Use progressive enhancement' instruction; The GOV.UK Service Manual states a list of browsers to test in (page history shows it dating from 2016 at least, reviewed repeatedly, current list 'from February 2026'), uses no grade letters and does not mention Yahoo or YUI. It is the service-side counterpart to the Frontend grades
Quotable: "Browsers to test in (from February 2026)"
Quotable: "The list in the table represents approximately 98% of the most popular browsers used on GOV.UK."
Quotable: "You should use analytics to understand how your users access the service and decide whether additional support is needed."
Quotable: "Decisions about compatibility cannot be something you specify at the start of your project and then forget about."
Quotable: "You also have to work out when to stop supporting a product or system if its popularity is declining."
Quotable: "Use progressive enhancement to give your service the best possible chance of working for the majority of your users."
Quotable: "18 September 2024 List of browsers to test in updated. Commitment to update browser list updated to annual."
Quotable: "6 August 2021 Reviewed list of browsers to make sure it's still current, based on recent usage figures for GOV.UK. No change from the January 2021 version of the list."
Quotable: "If evidence shows that your users have specific needs or extra support requirements, you can use this to make a case for not meeting these browser requirements."
Quotable: "Last updated: 30 January 2026"
Quotable: "Services do not have to look perfect in every browser."
Quotable: "Reviewed list of browsers to make sure it's still current, based on recent usage figures for GOV.UK. No change from the June 2020 version of the list."
Quotable: "Reviewed list of browsers to make sure it's still current, based on recent usage figures for GOV.UK. No change from the January 2020 version of the list."
Quotable: "Removed requirement to test with Safari 11 and earlier versions, as they fall outside of the 95% most popular browsers."
Quotable: "Removed requirement to test on Windows phone, as it falls outside of the 95% most common browser/device combinations."
Quotable: "Updated the requirement to test in Safari for iOS from 9.3 to 10.3 to reflect usage statistics."
Quotable: "Updated the list of browsers to support, removing Internet Explorer. Added some information on circumstances when it should still be supported."
Quotable: "Guidance first published"

### Practice: who keeps a matrix, and what it is consulted for

**[9] Government Digital Service - Supporting different browsers (The GDS Way).** primary. **fetched-and-verified.**
`https://gds-way.digital.cabinet-office.gov.uk/manuals/browser-support.html`
Supports: Government practice. Floor is the Service Manual browser list; analytics and user research decide extra browsers; out-of-policy bug reports are still investigated but may be declined on stated grounds; page has a named owner (#frontend) and an annual review cycle (reviewed 13 July 2026, next 13 July 2027). Matrix used to choose test browsers and to triage out-of-matrix bugs. Also states that the GDS Way is internal-use content
Quotable: "as a minimum, you should regularly test your service in the browsers listed in the Service Manual"
Quotable: "You should use analytics data and user research to determine whether you should regularly test in any other browsers."
Quotable: "You may receive reported issues on browsers outside of your normal policy. You should still investigate these issues, assess their impact, and consider how to address them."
Quotable: "This page was last reviewed on 13 July 2026."
Quotable: "It needs to be reviewed again on 13 July 2027"
Quotable: "You might still decide that an issue is not worth fixing if:"
Quotable: "fixing the issue would require disproportionate engineering effort"
Quotable: "a feature of your service inherently relies on an unsupported feature"
Quotable: "the browser in question cannot be supported without introducing serious security risks"
Quotable: "by the page owner #frontend"
Quotable: "The exact set of browsers you build for will vary by project"

**[10] U.S. Web Design System - Getting started for developers.** primary. **fetched-and-verified.**
`https://designsystem.digital.gov/documentation/getting-started-for-developers/`
Supports: Government design-system practice: a quantitative inclusion rule (the 2% rule) tied to an external analytics source, with progressive enhancement for the rest. Version 3.0 lists Chrome, Firefox, Safari, Edge; IE11 dropped
Quotable: "We officially support any browser above 2% usage as observed by"
Quotable: "Design System version 3.0 supports Chrome, Firefox, Safari, and Edge."
Quotable: "the Design System no longer supports Internet Explorer 11"

**[11] Office for National Statistics - Browser testing (ONS Design System).** primary. **fetched-and-verified.**
`https://service-manual.ons.gov.uk/design-system/guidance/browser-testing/`
Supports: Government practice: inherits the GOV.UK list as the floor, adds a 2% analytics threshold for extra browsers, and allows an evidence-based exemption for internal services restricted to certain browsers. Matrix consulted for choosing test browsers. Also records a dropped browser (IE) with a banner for remaining users
Quotable: "Services do not have to look perfect in every browser, but users must be able to access and use all the information and features they need."
Quotable: "if your service’s analytics data shows at least 2% of your users are using a different browser or version, then you will need to test against that as well."
Quotable: "internal services used exclusively by ONS staff may not need to work on all supported browsers"

**[12] Jenkins project - Browser compatibility policy (jenkins-infra/jenkins.io source on GitHub).** primary. **fetched-and-verified.**
`https://github.com/jenkins-infra/jenkins.io/blob/master/content/doc/book/platform-information/support-policy-web-browsers.adoc`
Supports: Open-source product (not a commercial vendor) with a standing three-level policy (Level 1 proactive/equal UX, Level 2 patches plus best effort, Level 3 no guarantees and the default for anything unlisted), a browser-by-level matrix with N / N-1 version rules, a pre-release exclusion, and a dated change history linking each change to a developer-mailing-list discussion or governance meeting (2014, 2019, 2022, 2025). Shows that changes are made by discussion in the community, a few times over a decade, and that mobile support was left undetermined. Read via gh api (GitHub contents API) of the AsciiDoc source, not the rendered jenkins.io page, because jenkins.io is not a cleared host
Quotable: "Level 1: Aim to proactively support these browsers and provide an equal"
Quotable: "Accept patches to fix issues and make the best effort to"
Quotable: "Level 3: No guarantees."
Quotable: "This is the default unless a browser/version is listed"
Quotable: "We do not claim any compatibility with or accept bug reports and"
Quotable: "Support for mobile browsers (e.g. iOS Safari) has not yet been determined."
Quotable: "2025-06-16 - Move Firefox ESR to level 2 from level 1"
Quotable: "2022-02-01 - Remove support for Internet Explorer, Add Edge"

**[13] GitHub - Supported browsers (github/docs source on GitHub).** vendor. **fetched-and-verified.**
`https://github.com/github/docs/blob/main/content/get-started/using-github/supported-browsers.md`
Supports: COMMERCIAL product team. A standing public help page for a commercial SaaS product. Two postures: 'latest version of a recommended browser' as the supported set, plus a separate best-effort statement for extended-support releases, and an explicit disclaimer for older or unlisted browsers. No numeric tiers or grades and no update-policy section. It does give a bug-triage rule (check whether a bug in a pre-release build also exists in the stable version) and a troubleshooting section. The page's git history shows it is edited, for example a commit dated 2026-06-29 adding troubleshooting guidance. It is a user-facing statement, not an internal test matrix. Read from the repository source, not docs.github.com
Quotable: "We design {% data variables.product.github %} with the latest web browsers in mind."
Quotable: "We do our best to ensure that {% data variables.product.github %} functions properly in the latest extended support release for:"
Quotable: "In earlier extended support releases, {% data variables.product.github %} may not work as you expect, and some features may not be available."
Quotable: "please verify that it also exists in the stable version of the same browser"

**[14] GitHub - browser-support README (github/browser-support).** vendor. **fetched-and-verified.**
`https://github.com/github/browser-support/blob/main/README.md`
Supports: COMMERCIAL product team, internal practice. The matrix is consulted in code: the isSupported() function sets a minimum feature baseline; below it, browsers send no errors or statistics to monitoring (a use of the matrix for observability triage). Polyfills are added and removed under a named owning team (@github/web-systems) with a Stage 4-only rule for ECMAScript features, and the baseline const is meant to move with the support matrix when a polyfill is removed. Shows polyfill choice as a downstream use of the matrix. The README does not itself contain a browser-by-tier matrix
Quotable: "to ensure that our baseline moves with our browser support matrix"

**[15] MetaMask - Browser support (MetaMask/metamask-extension docs).** vendor. **fetched-and-verified.**
`https://github.com/MetaMask/metamask-extension/blob/develop/docs/browser-support.md`
Supports: COMMERCIAL-backed product, engineering doc in the repo. A standing policy stated as version windows (two years of Chrome stable; current and previous Firefox ESR), a tested-versus-tried distinction for forks, and an explicit change procedure: notify users in-app one release before raising a minimum browser version, via a code constant. Shows who moves the matrix (the release process) and what protects users from being stranded. No grades or tiers
Quotable: "The last two years of Chrome stable releases"
Quotable: "The current and previous Firefox Extended Support Release"
Quotable: "We try to support browser forks as well (aligned with supported Chrome/Firefox releases), but we don't actively test them."
Quotable: "before bumping our minimum supported browser versions, we should always notify users in the application first."

**[16] Google Material Components Web - Supported browsers (material-components-web docs).** vendor. **fetched-and-verified.**
`https://github.com/material-components/material-components-web/blob/master/docs/supported-browsers.md`
Supports: Commercial-vendor open-source component library. A minimal rule (last two versions of every major browser) plus a list of the browser and operating-system pairs that are actually tested; the support set is defined as the tested set. No tiers and no update policy. Counter-example of a thin matrix
Quotable: "We officially support the last two versions of every major browser. Specifically, we test on the following browsers:"

### Debates: thresholds, queries and capability tests

**[17] Browserslist project - README (browserslist/browserslist).** primary. **fetched-and-verified.**
`https://github.com/browserslist/browserslist`
Supports: Query-based (judgment/configurable) list camp: default query, a usage floor with a stated caution, a warning against dropping browsers just because they are unfamiliar, query-composition options including own-traffic stats and Baseline. Its recommended custom query combines a usage floor with recency and exclusion terms
Quotable: "`> 0.5%, last 2 versions, Firefox ESR, not dead`"
Quotable: "`last 2 versions, not dead, > 0.2%`"
Quotable: "will in the long run make popular browsers even more popular"
Quotable: "We might run into a monopoly and stagnation situation, as we had with Internet Explorer 6."
Quotable: "Don’t remove browsers just because you don’t know them."
Quotable: "You can query against statistics derived from your real-world traffic rather than global marketshare"

**[18] MDN Web Docs - Progressive enhancement (glossary).** primary. **fetched-and-verified.**
`https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement`
Supports: Progressive-enhancement camp: defines the philosophy as a baseline for as many users as possible plus the best experience only on modern browsers; names feature detection and polyfills as the mechanism. TERMS developer.mozilla.org: permits (covered by Mozilla Website Terms and Acceptable Use Policy at mozilla.org, neither has an automated-access clause)
Quotable: "a baseline of essential content and functionality to as many users as possible"

**[19] MDN Web Docs - Implementing feature detection.** primary. **fetched-and-verified.**
`https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Testing/Feature_detection`
Supports: Feature-detection camp's explicit rejection of browser-identity lists: calls browser sniffing a terrible practice; prefers CSS @supports for CSS support checks
Quotable: "this is a terrible practice that should be discouraged at all costs"
Quotable: "it is the preferred method of determining browser support for CSS features"

**[20] Jeremy Keith - Resilient Web Design, chapter 5.** practitioner. **fetched-and-verified.**
`https://resilientwebdesign.com/chapter5/`
Supports: Argument that a version table is the wrong unit: capability tests ('cutting the mustard', credited to a BBC News team) replace identity; support versus optimization (quoting Brad Frost). TERMS resilientwebdesign.com: permits (no terms-of-use page found; site carries a Creative Commons Attribution-ShareAlike 4.0 licence statement; no automated-access clause)
Quotable: "Instead of asking “which browser are you?” and trying to infer feature support from the answer, it is safer to simply ask “do you support this feature?”"
Quotable: "There is a difference between support and optimization."
Quotable: "Browsers that don’t cut the mustard still get access to the content, but without the JavaScript enhancements."

### Relationships with neighbouring documents

**[21] ISTQB - Certified Tester Foundation Level Syllabus v4.0.1.** standards. **fetched-and-verified.**
`https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf`
Supports: Compatibility is a non-functional quality characteristic; test environment requirements are a test-design work product and a test-plan content item; configuration management records a test environment's components and versions so past results can be reproduced; a defect report identifies the test object and test environment. The syllabus names no browser or device matrix document
Quotable: "Test design work products include: (prioritized) test cases, test charters, coverage items, test data requirements and test environment requirements."
Quotable: "Performance efficiency • Compatibility • Usability (also known as interaction capability) • Reliability • Security • Maintainability • Portability (also known as flexibility) • Safety"
Quotable: "For a complex configuration item (e.g., a test environment), CM records the items it consists of, their relationships, and versions."
Quotable: "It is possible to revert to a previous baseline to reproduce previous test results."
Quotable: "Identification of the test object and test environment"
Quotable: "such as a usability lab for usability testing"

**[22] GOV.UK Service Manual - Quality assurance: testing your service regularly.** primary. **fetched-and-verified.**
`https://www.gov.uk/service-manual/technology/quality-assurance-testing-your-service-regularly`
Supports: The page states a device-independence goal for services and lists types of testing, but names no document that records which browsers or devices are covered, and does not use the words browser, compatibility or matrix
Quotable: "is easy to use for anyone who needs to use it, regardless of the device they’re using"
Quotable: "accessibility testing - to check that everyone, including disabled people, can use your service"

### The gap question

**[23] GOV.UK Service Manual - Testing with assistive technologies.** primary. **fetched-and-verified.**
`https://www.gov.uk/service-manual/technology/testing-with-assistive-technologies`
Supports: A government service manual publishes a table of assistive technology, version and browser combinations a service must work with before public beta, plus 'other' combinations to prioritise, a 'test with the actual device or technology' instruction and an issue-reporting rule that records browser, OS and AT version. Page history: published 26 October 2017, last updated 24 May 2022 (a 21 September 2020 entry updated the combination list)
Quotable: "your service must work with at least the following combinations of assistive technologies and browsers before it goes into public beta"
Quotable: "This table is based on the 2016 survey of assistive technologies used to access GOV.UK and the more recent WebAIM screen reader survey"
Quotable: "Windows Magnifier or Apple Zoom (screen magnifiers)"
Quotable: "test up to at least 4 times magnification"
Quotable: "Participants do not need to use any specific combinations of software"

**[24] Deque Systems - Accessibility supported (dequelabs/axe-core docs).** practitioner. **fetched-and-verified.**
`https://github.com/dequelabs/axe-core/blob/develop/doc/accessibility-supported.md`
Supports: A tool vendor lists seven screen reader/browser/OS combinations it tests against, and states a two-part inclusion rule (over 1% of users, and new coverage). One combination is marked DEPRECATED, so the list carries its own retirement mark. Body read via the GitHub contents API on github.com; the source cache entry is keyed to the raw.githubusercontent.com form of the same file
Quotable: "be used by more than 1% of users"
Quotable: "Introduce new coverage for a screen reader, browser, or environment not currently accessibility supported"
Quotable: "JAWS and IE11 on Windows (DEPRECATED)"
Quotable: "Dragon and Firefox on Windows"

**[25] Basecamp - Screen reader setup and testing (basecamp/accessibility).** practitioner. **fetched-and-verified.**
`https://github.com/basecamp/accessibility/blob/master/Section-2/Screen-reader-setup-and-testing.md`
Supports: A commercial product team's published list of screen reader plus platform combinations it tests, with a primary and a secondary, including native-app variants on iOS and Android. Body read via the GitHub contents API; cache entry keyed to the raw.githubusercontent.com form
Quotable: "results vary greatly across platform + browser combinations"
Quotable: "focus on one combination, then perform a run through using a secondary variant"
Quotable: "JAWS + Firefox (secondary)"
Quotable: "VoiceOver in mobile Safari & native app"

**[26] W3C WCAG 3 working group - Default accessibility support set (w3c/wcag3 discussion 277).** standards. **fetched-and-verified.**
`https://github.com/w3c/wcag3/discussions/277`
Supports: A standards-body working-group thread states that an 'accessibility support set' defines which user agents and assistive technologies you test with, names the GOV.UK page and axe-core as published examples, and records a participant's warning that such a set must not be cast in amber. Also records a Japanese contributor's point that a set built on English-language screen readers misses others (PC-Talker). A discussion thread, so it carries opinion, not a ruling; the opening post says the discussion was being closed and restarted
Quotable: "An "accessibility support set" is used at higher levels of conformance to define which user-agents and assistive technologies you test with."
Quotable: "Also worth considering how this set will be kept updated/extended."

**[27] GOV.UK Service Manual - Building a robust frontend using progressive enhancement.** primary. **fetched-and-verified.**
`https://www.gov.uk/service-manual/technology/using-progressive-enhancement`
Supports: JavaScript-disabled and failed-JavaScript support is stated as a mandatory building rule, with named causes of failure and a fallback-channel rule. It is a build rule, not a matrix row. Published 23 May 2016, last updated 27 September 2024
Quotable: "All government services must follow progressive enhancement, even if part of the service or a parent service needs JavaScript"
Quotable: "Some users may deliberately turn off features in their browsers. You should respect their decision and make sure those users can still use your service."
Quotable: "you’ll need to consider how users can access your service through other channels"

**[28] GOV.UK Service Manual - How to test frontend performance.** primary. **fetched-and-verified.**
`https://www.gov.uk/service-manual/technology/how-to-test-frontend-performance`
Supports: Low-bandwidth, low-spec-device support is handled as a performance budget and a testing practice, not as a support-matrix dimension. The page names no network speed or device-spec target. Published 21 May 2018, last updated 14 March 2019
Quotable: "Set a performance budget"
Quotable: "users on limited data plans"
Quotable: "testing on a wide range of devices"

**[29] Government Digital Service - How to optimise frontend performance (The GDS Way).** primary. **fetched-and-verified.**
`https://gds-way.digital.cabinet-office.gov.uk/standards/optimise-frontend-perf.html`
Supports: Frontend performance is a prioritised task list (high, medium, low) with CI integration, again not a support-matrix dimension
Quotable: "You should integrate these tools into your Continuous Delivery (CD) and Continuous Integration (CI) workflow"

**[30] Office for National Statistics - Layout: grid (ONS Design System).** primary. **fetched-and-verified.**
`https://service-manual.ons.gov.uk/design-system/foundations/grid`
Supports: Viewport breakpoints (300, 400, 500, 740, 980, 1300, 1600 px) are specified as design-system layout configuration, described as device agnostic, and are not tied to any supported/unsupported statement. A gutter rule changes at 600px
Quotable: "We use a set of device agnostic breakpoints to change the layout when best suited as opposed specific devices."

**[31] U.S. Web Design System - Layout grid.** primary. **fetched-and-verified.**
`https://designsystem.digital.gov/utilities/layout-grid/`
Supports: USWDS breakpoints (160 to 1400 px, minimum-width media queries) are likewise layout configuration. No supported-viewport floor is stated on the page
Quotable: "Grid breakpoints are based on minimum-width media queries"

**[32] U.S. Web Design System - Accessibility.** primary. **fetched-and-verified.**
`https://designsystem.digital.gov/documentation/accessibility/`
Supports: USWDS names assistive-technology and zoom testing as a practice (VoiceOver and JAWS, keyboard, browser zoom, touch, 'across browsers and operating systems') but publishes no table of combinations on this page
Quotable: "Test with screen readers (VoiceOver, JAWS)"
Quotable: "Test across browsers and operating systems"

**[33] Government Digital Service - GOV.UK app: terms and conditions.** primary. **fetched-and-verified.**
`https://www.gov.uk/guidance/govuk-app-terms-and-conditions`
Supports: A native-app support statement is published as a minimum-OS list in the app's terms, with no review cadence or support-change notice period on the page. It also says content may change 'without notice' and that users who decline updates may lose use of the app
Quotable: "iPhones running iOS 16 or later"
Quotable: "Android phones running Android 10 or later"
Quotable: "If you choose not to install such updates, or opt out of automatic updates, you may not be able to continue using the GOV.UK app."

**[34] AMP Project - Intent to Deprecate: IE11 Support (ampproject/amphtml issue 34453).** practitioner. **fetched-and-verified.**
`https://github.com/ampproject/amphtml/issues/34453`
Supports: One project's recorded process for communicating a browser support drop: a written motivation and user-impact section, a two-week open-discussion rule, a mailing-list and Slack announcement, and a roughly six-week lead before production. The audience is developers of a library, not end users of a site
Quotable: "Allow at least 2 weeks of open discussion after the I2D is created before proceeding with the deprecation of the feature"
Quotable: "this change will be announced on the mailing list and on Slack"

**[35] Cockpit project - login: add message for Internet Explorer deprecation (cockpit-project/cockpit issue 9689).** practitioner. **fetched-and-verified.**
`https://github.com/cockpit-project/cockpit/issues/9689`
Supports: One project's end-user-facing communication of a browser support drop: a deprecation warning on the login page first, then an outright block that points to working browsers
Quotable: "a friendlier message that communicates that their browser does not work and message which browsers do work"

**[36] U.S. Web Design System - Component lifecycle.** primary. **fetched-and-verified.**
`https://designsystem.digital.gov/components/lifecycle/`
Supports: USWDS defines a Deprecated stage with a stated meaning for components, not for browsers. Cited only to show the staged-wording model exists in a permitted source; it does not address browser or device support changes
Quotable: "The component is removed from active support."

## Pages not read under the terms rule

- `https://www.redhat.com/en/about/browser-support`. Red Hat's terms of use forbid deploying a robot, spider or
  retrieval application on the site. It would have been a commercial vendor's browser support policy, read for tiers,
  a version rule and an update statement. The maintainer may read it by hand.
