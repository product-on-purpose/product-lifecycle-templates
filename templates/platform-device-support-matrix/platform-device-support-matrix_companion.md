# Companion: The Platform and Device Support Matrix

> The deep explainer for the platform-device-support-matrix bundle. Read this to understand what a
> support matrix is, how published matrices are built, and where their authors disagree about grades,
> thresholds and what the word "support" promises. The short operator card is
> [`platform-device-support-matrix_guide.md`](platform-device-support-matrix_guide.md); a fully worked
> instance is [`platform-device-support-matrix_example.md`](platform-device-support-matrix_example.md).
> Inline citations like [[1]](#ref-1) resolve to the [References](#references) at the bottom, numbered
> exactly as the research log numbers them. The full retrieval trail, including the pages this bundle
> did not read under the terms rule, is
> [`platform-device-support-matrix_research-log.md`](platform-device-support-matrix_research-log.md).
> This bundle sits in the `standing-standards` family as a **foundation**: a standard that a team's test
> choices and bug triage are judged against, rather than an instrument executed under time pressure, per
> [ADR 0088 (the platform and device support matrix joins standing-standards as a foundation)](../../docs/internal/decisions/0088-platform-device-support-matrix-joins-standing-standards-as-a-foundation.md).

---

## 1. Orientation and TL;DR

A platform and device support matrix is a standing page that states which browsers, operating systems and
devices a product supports, at what level, and which of them the team tests on. GOV.UK Frontend states the
purpose of its grading in one sentence: "Each grade shows the level of support we will provide."
[[2]](#ref-2) Yahoo's older scheme states the principle behind grading: "Support does not mean that
everybody gets the same thing." [[1]](#ref-1) The page is consulted for three jobs. A team picks browsers
to test with it [[9]](#ref-9), [[11]](#ref-11). A triager decides what an out-of-policy bug report is worth
with it [[9]](#ref-9), [[12]](#ref-12), [[13]](#ref-13). An engineer decides what a polyfill or a code
baseline must cover with it [[14]](#ref-14).

The job in one sentence: a short, standing page that tells the people who build, test or triage the
product which environments get which promise, and who changes that promise when conditions change.

**At a glance**

- **A matrix makes two different promises.** One is what a user on a given browser will get. The other is
  what the team will test. The sources use the word "support" for both, so a matrix has to define its
  grades by their commitments and mark testing separately (section 6 sets out the evidence).
- **The evidence base is public.** It is matrices and support statements from government teams, design
  systems, open-source projects and a few commercial teams. No source read shows that keeping a matrix
  improves outcomes, and no source read measures what keeping one costs.
- **Every threshold read is one team's choice for its own traffic.** The 2% figure belongs to the U.S. Web
  Design System [[10]](#ref-10) and to the Office for National Statistics [[11]](#ref-11). The 98% figure is
  GOV.UK's description of its own coverage [[8]](#ref-8). Neither is a norm.
- **The Review Trigger section states conditions, with the annual floor last.** GOV.UK's own update
  history shows the list changing when usage moves, and periodic reviews checking whether it had
  [[8]](#ref-8). The quoted review-only entries date from 2020 and 2021, before the annual commitment of
  2024, so reading the annual figure as a floor is the library's inference, at medium confidence.
- **Some of this bundle's structure is the library's own position.** The separate Grade and Tested columns
  have support in the sources all the same, because the GDS Way and MetaMask separate what a team builds
  for from what it tests [[9]](#ref-9), [[15]](#ref-15). The Notes column has only partial support. No
  source names a role that may change a grade, so the role names in Ownership are a proposal. The table
  form of the Review Trigger is the library's own as well. Each is labelled where it appears.

If you read nothing else: define "support" by what you promise and what you test, then keep those two
promises in separate columns. That separation is the library's position, drawn from sources that use
"support" in different senses.

## 2. Origins and evolution

No source read documents a lineage from Yahoo's scheme to the GOV.UK schemes, so this section reports what
each source says about itself and stops there.

**Yahoo's Graded Browser Support is the earliest scheme this research read.** Its wiki page states that
"There are three grades: A-grade, C-grade, and X-grade support." [[1]](#ref-1) It defines the base grade
plainly: "C-grade is the base level of support, providing core content and functionality." [[1]](#ref-1)
It states what the X grade means in testing terms: "QA does not test, and bugs are not opened against
X-grade browsers." [[1]](#ref-1) The page lists dated updates from 2008-02-19 to 2012-07-26 and calls
itself the permanent home of the strategy, but it gives neither the original publication date nor the
author [[1]](#ref-1).

**Authorship rests on one secondary statement, at low confidence.** Springer Nature's frontend playbook
calls the scheme "a concept originally conceived by Nate Koechley" [[5]](#ref-5). The original Yahoo
article was not read. This companion therefore attributes the author to Springer Nature and states no date
for the scheme's first publication.

**GOV.UK Frontend uses four grades, and no source read says they descend from Yahoo's.** The design
system's documentation says "the Design System team has divided browsers into 4 grades." [[2]](#ref-2)
The maintainers' contributor documentation carries the same scheme in its own words, "we group browsers
into 4 grades" [[3]](#ref-3), and its first commit is dated 2023-10-24 [[3]](#ref-3). A 2023 issue records
the move: "We're exploring moving towards a graded browser support model where we don't always aim to
provide exactly the same experience to every user." [[4]](#ref-4) None of the GOV.UK pages or issues read
names Yahoo or YUI [[2]](#ref-2), [[3]](#ref-3), [[4]](#ref-4). The right description is a **shared
vocabulary**, not a documented lineage.

**The letters mean different things in the two schemes.** YUI's C grade is the base level that carries
core content, and its X grade is untested [[1]](#ref-1). GOV.UK's X grade is also untested, and it adds a
fix commitment: "We will not fix bugs affecting these browsers." [[6]](#ref-6) A reader who sees "Grade C"
in a matrix therefore cannot know what it promises without the matrix's own definition. That is the
reason the Support Grades section exists.

**One commercial team names Yahoo's scheme as its model.** Springer Nature says it implements graded
support "using a variant of Yahoo's Graded Browser support" [[5]](#ref-5), by "classifying all versions of
all browsers into one of two levels" [[5]](#ref-5). Its playbook page was renamed from "Graded browser
support" to "Browser support" in a pull request merged on 2018-08-23 [[5]](#ref-5).

**Two other published forms are parallel, not descended.** The Australian Digital Transformation Office's
UI-Kit file defines support levels and marks each row tested or untested, and it names neither YUI nor
grade letters [[7]](#ref-7). The GOV.UK Service Manual states a list of browsers to test in, and it names
neither grades nor Yahoo [[8]](#ref-8). The Service Manual page history reaches back to at least 2016
[[8]](#ref-8).

**Time-bound facts a reader should recheck.** The Service Manual table is headed "Browsers to test in
(from February 2026)" and the page says "Last updated: 30 January 2026" [[8]](#ref-8). The GDS Way page says
"This page was last reviewed on 13 July 2026." [[9]](#ref-9) Entry [[6]](#ref-6) is the GOV.UK Frontend
v5 page and entry [[2]](#ref-2) is the latest version, so the two can differ. The UI-Kit repository
states that "This repository was archived by the owner on Mar 5, 2018." [[7]](#ref-7) YUI's updates end in
2012 [[1]](#ref-1).

## 3. Anatomy (section by section)

The template has seven sections, in one size. Each subsection below says what the section is, why it
exists, a beginner note, and where useful an expert note.

### Purpose and Scope

**What it is.** A statement of which product the matrix covers, who relies on it, whether this file or a
tool is the record, which audiences are exempt, and where the assistive-technology combinations live.
The sentence about the product and the record is the library's POSITION. No source publishes a scope
statement in that form.

**Why it exists.** It says which product the promises apply to, in the words of the sources below. The
UI-Kit file opens with its purpose: "The UI-Kit team needs to support all of our users, regardless of their
device, web browser or other user agent." [[7]](#ref-7) The Service Manual states the other side of the
same bargain: "Services do not have to look perfect in every browser." [[8]](#ref-8) The ONS adds the floor
under that sentence: "Services do not have to look perfect in every browser, but users must be able to
access and use all the information and features they need." [[11]](#ref-11)

**Beginner note.** Say which product the matrix covers, then say where the record lives. The GDS Way adds
a reason to scope it by product: "The exact set of browsers you build for will vary by project"
[[9]](#ref-9).

**Assistive technology belongs by reference, not inside the matrix.** GOV.UK publishes its own table of
assistive-technology and browser combinations on a separate page: "your service must work with at least
the following combinations of assistive technologies and browsers before it goes into public beta"
[[23]](#ref-23). Deque includes a combination in its list if it would "be used by more than 1% of users"
[[24]](#ref-24), and Basecamp's published testing guidance says to "focus on one combination, then
perform a run through using a secondary variant" [[25]](#ref-25). Because GOV.UK keeps its table on its own page, the matrix points to
where those combinations live and does not hold them. That is the library's reading, at medium confidence,
and it is the one gap the research found that the spec's seven sections did not cover.

**Audience exceptions.** The Service Manual lets evidence change the requirement: "If evidence shows that
your users have specific needs or extra support requirements, you can use this to make a case for not
meeting these browser requirements." [[8]](#ref-8) The ONS allows an evidence-based exemption for a class
of services: "internal services used exclusively by ONS staff may not need to work on all supported
browsers" [[11]](#ref-11).

**Expert note.** The matrix is a standing page, and the Service Manual says so about compatibility
decisions: "Decisions about compatibility cannot be something you specify at the start of your project and
then forget about." [[8]](#ref-8)

### Support Grades

**What it is.** Each grade, with its definition, its test commitment and its bug-fix commitment. The
section defines the words the Matrix section then uses.

**Why it exists.** The sources define grades by what the team commits to do, and the commitments differ.
GOV.UK Frontend commits to priority: "treat bugs affecting Grade A browsers as high priority"
[[6]](#ref-6), and "treat bugs affecting Grade B browsers as low priority unless we find evidence they
prevent a user from being able to complete their task" [[6]](#ref-6). For its lowest grade it commits to
neither testing nor fixing: "will not regularly test in these browsers" and "We will not fix bugs affecting
these browsers." [[6]](#ref-6) Grade C also reserves a power to reduce features: "However, we might
disable or reduce features on an individual basis in browsers where the underlying features are not
available." [[6]](#ref-6)

Yahoo's scheme carries a test commitment for its top grade: "A-grade browsers are identified, capable,
modern and common. QA tests all A-grade browsers, and bugs are addressed with high priority." [[1]](#ref-1)
It also names how the top grade is kept: "A-grade browsers should be identified on a whitelist."
[[1]](#ref-1)

**How many grades the sources use.** Yahoo has three [[1]](#ref-1), GOV.UK Frontend four [[6]](#ref-6),
Jenkins three levels [[12]](#ref-12), and Springer Nature [[5]](#ref-5) and the UI-Kit [[7]](#ref-7) two.
Graded support is not a fixed three-grade standard. Jenkins' levels run from proactive support with an
equal experience, through accepting patches and a best effort, to a third level: "Level 3: No guarantees."
[[12]](#ref-12)

**Beginner note.** Write each grade as three lines: what the user gets, what the team tests, and what the
team does about a bug. A grade defined only by its letter promises nothing.

**Expert note.** Grades are optional. GitHub's help page names the latest browsers and gives a best-effort
statement for extended-support releases, with no grades [[13]](#ref-13). Material Components Web defines
its support as the set it tests, and lists the pairs it tests, with no tiers: "We officially support the
last two versions of every major browser. Specifically, we test on the following browsers:"
[[16]](#ref-16). A team whose whole promise is the latest browsers, tested, can run a matrix with one grade.
The cost is that the page then has nowhere to say that a browser is supported but untested, and section 6
shows why that statement is sometimes the honest one.

### The Matrix

**What it is.** A mobile table and a desktop table, with an effective-from date. The columns are Browser,
Platforms, a minimum version or version rule, Grade, Tested, and Notes.

**Why it exists.** It is the table itself: the browsers, platforms, versions, grades and test status that
the other six sections define and govern.

**The column set is partly the library's POSITION.** The UI-Kit mobile table's header row is "Browser
Platforms Minimum version Advanced support status" [[7]](#ref-7). Its desktop table has no minimum
version column, and its single status column holds both the level and the test status [[7]](#ref-7). The
Service Manual's table pairs an operating system with a browser and puts versions inside the cells
[[8]](#ref-8). Jenkins keys its table by level and version rule [[12]](#ref-12). **No source read has
separate Grade and Tested columns, and none has a Notes column**, so those columns are the library's
POSITION.

**Why the library still separates Grade from Tested.** The GDS Way separates what a team builds for from
what it tests, with the first varying by project [[9]](#ref-9). MetaMask supports browsers it does not
test: "We try to support browser forks as well (aligned with supported Chrome/Firefox releases), but we
don't actively test them." [[15]](#ref-15) A single status column cannot express a row like that one.

**A version rule can replace a minimum version.** MetaMask states a window: "The last two years of Chrome
stable releases" [[15]](#ref-15). The UI-Kit states "All browsers listed are latest stable release, except
Internet Explorer." [[7]](#ref-7) Jenkins uses N and N-1 rules per level [[12]](#ref-12), and Material
Components Web the last two versions [[16]](#ref-16). So the column is better asked as a minimum version
or a version rule. That is the library's synthesis, at medium confidence. The UI-Kit also gives a reason
for one minimum: "Minimum version based on support for CSS Flexible Box layout modules" [[7]](#ref-7).

**An effective-from date.** The Service Manual heads its table "Browsers to test in (from February 2026)"
[[8]](#ref-8). A dated line costs little and lets a reader tell a current table from a forgotten one. This
is a medium-confidence borrowing from a single source.

**Beginner note.** Fill the mobile rows first and give each a minimum version or a rule. The GOV.UK app's
terms show the form a native minimum takes, "iPhones running iOS 16 or later" and "Android phones running
Android 10 or later" [[33]](#ref-33), and no source read puts app support and web support in one table.

**Expert note.** Viewport width is not in this table. The ONS describes its breakpoints as "a set of device
agnostic breakpoints to change the layout when best suited as opposed specific devices." [[30]](#ref-30)
USWDS states that "Grid breakpoints are based on minimum-width media queries" [[31]](#ref-31). Neither
makes a viewport size a support commitment, so this research found no basis for a viewport column.
Jenkins marks a gap openly: "Support for mobile browsers (e.g. iOS Safari) has not yet been determined."
[[12]](#ref-12) A matrix can state that a row is undecided.

### Threshold Rule

**What it is.** The rule by which a browser enters or leaves the matrix: the usage figure, the analytics
source it is read from, and who decides.

**Why it exists.** It gives a change to the list a stated reason. The USWDS, ONS and Browserslist rules
name their source for the figure, whether an analytics service [[10]](#ref-10), the service's own
analytics [[11]](#ref-11) or a team's own traffic [[17]](#ref-17).

**The sources, each attributed.** USWDS: "We officially support any browser above 2% usage as observed by"
an analytics service [[10]](#ref-10). The ONS: "if your service’s analytics data shows at least
2% of your users are using a different browser or version, then you will need to test against that as
well." [[11]](#ref-11) GOV.UK does not state a floor. It states coverage: "The list in the table represents
approximately 98% of the most popular browsers used on GOV.UK." [[8]](#ref-8) Its change entries cite a
percentile of usage too: "Removed requirement to test with Safari 11 and earlier versions, as they fall
outside of the 95% most popular browsers." [[8]](#ref-8) The GDS Way leaves the choice to the team:
"You should use analytics data and user research to determine whether you should regularly test in any
other browsers." [[9]](#ref-9)

**These figures are not norms.** Each one is a team's choice for its own traffic. The 2% belongs to USWDS
and the ONS, the 98% and 95% describe GOV.UK's traffic, and Deque's 1% is a rule for assistive-technology
combinations [[24]](#ref-24). The library's position is that a matrix should name its own analytics source
beside any figure it uses.

**Beginner note.** Name the analytics source and the person who reads it. Then choose a figure and say it
is yours.

**Expert note.** Browserslist argues against a usage floor used alone, warning that it "will in the long
run make popular browsers even more popular" [[17]](#ref-17), and lets a team query "statistics derived
from your real-world traffic rather than global marketshare" [[17]](#ref-17). The Service Manual points at
the other end of the decision: "You also have to work out when to stop supporting a product or system if
its popularity is declining." [[8]](#ref-8) A threshold rule should say what happens in both directions.

### Unsupported Browsers

**What it is.** What a user on an unlisted or lowest-grade browser gets, and what a bug from one is worth.

**Why it exists.** The matrix lists what a team supports, so the people who are not on it need an answer
too. The sources carry this content under three names. The UI-Kit has a section headed "Unsupported
browsers" whose body says "Other combinations may be supported but have not been extensively tested"
[[7]](#ref-7). GOV.UK Frontend carries it as its lowest grade [[6]](#ref-6). Jenkins makes its lowest level
the default: "This is the default unless a browser/version is listed" [[12]](#ref-12).

**The triage rule.** The GDS Way sets the posture for a report from outside the policy: "You may receive
reported issues on browsers outside of your normal policy. You should still investigate these issues,
assess their impact, and consider how to address them." [[9]](#ref-9) It then names three grounds for
declining a fix after that investigation: "fixing the issue would require disproportionate engineering
effort", "a feature of your service inherently relies on an unsupported feature", and "the browser in
question cannot be supported without introducing serious security risks" [[9]](#ref-9). GitHub asks a
reporter of a pre-release bug to "please verify that it also exists in the stable version of the same
browser" [[13]](#ref-13).

**Beginner note.** Write the answer you want to give a person on a browser the matrix does not list, in a
sentence a support agent can say aloud.

**Expert note.** JavaScript switched off and slow connections are not matrix rows. GOV.UK makes
JavaScript-off a building rule: "Some users may deliberately turn off features in their browsers. You
should respect their decision and make sure those users can still use your service." [[27]](#ref-27)
It treats bandwidth as a budget and a testing practice, "Set a performance budget" [[28]](#ref-28), not as
a support grade. The Unsupported Browsers section can point at the progressive-enhancement rule, in the
Service Manual's own words: "Use progressive enhancement to give your service the best possible chance of
working for the majority of your users." [[8]](#ref-8)

### Ownership

**What it is.** The named owner, who may change a grade, and who is told when one changes.

**Why it exists.** The family contract's staleness obligation asks every member to name who notices when
the document goes wrong, and an unowned matrix has nobody to notice. The GDS Way page names its owner in its own
text: "by the page owner #frontend" [[9]](#ref-9). GitHub's browser-support library names a team that
decides whether a polyfill can go [[14]](#ref-14). Jenkins records that each of its changes followed a
mailing-list thread or a governance meeting, as entry [[12]](#ref-12) records, so its owner is a community
process rather than a person.

**The role names are the library's POSITION.** No source read names a person or role who may change a
grade. The template's role names are a proposal, not received practice.

**Beginner note.** Name a role and a channel, then name a person in that role. A matrix that says "the
team" has no owner.

**Expert note.** The GDS Way states that its content is intended for internal use by the GDS Digital Products
community [[9]](#ref-9). It is cited here as a government team's guidance and not as a standard.

### Review Trigger

**What it is.** A table of conditions, owners and actions: what event makes the matrix wrong, who notices,
and what they do about it. The family contract makes this section mandatory for every member.

**The table form is the library's POSITION.** The sources show the content in prose and in dated change
histories: the GDS Way's review dates [[9]](#ref-9), the Service Manual's update history [[8]](#ref-8),
Jenkins' change history [[12]](#ref-12), and MetaMask's rule to warn users before raising a minimum
[[15]](#ref-15).

**The conditions, with their evidence.**

- **A browser crosses the threshold, in either direction.** The usage rule is USWDS's [[10]](#ref-10) and
  the ONS's [[11]](#ref-11). The Service Manual shows it working: "Updated the requirement to test in
  Safari for iOS from 9.3 to 10.3 to reflect usage statistics." [[8]](#ref-8)
- **A vendor ends support.** USWDS records "the Design System no longer supports Internet Explorer 11"
  [[10]](#ref-10). Jenkins records "2022-02-01 - Remove support for Internet Explorer, Add Edge"
  [[12]](#ref-12). The Service Manual records "Updated the list of browsers to support, removing Internet
  Explorer. Added some information on circumstances when it should still be supported." [[8]](#ref-8)
  The sources record the drop, not the cause, so reading each drop as a vendor ending support is the
  library's inference.
- **A new platform is adopted.** This condition is the library's synthesis. No source read states it.
- **A bug is triaged against a browser the matrix does not list.** The GDS Way describes the report and
  the response [[9]](#ref-9). Reading such a report as evidence of a gap in the matrix is the library's
  inference.
- **The annual floor.** At least once a year, whatever else has fired, the owner reconfirms every row. The
  Service Manual records "18 September 2024 List of browsers to test in updated. Commitment to update
  browser list updated to annual." [[8]](#ref-8) The GDS Way page says "It needs to be reviewed again on
  13 July 2027" [[9]](#ref-9).

**Why the annual figure is read as a floor, and the evidence for that.** The Service Manual's history
records reviews with no change: "Reviewed list of browsers to make sure it's still current, based on
recent usage figures for GOV.UK. No change from the June 2020 version of the list." [[8]](#ref-8) Those
review-only entries date from 2020 and 2021, about six months apart. Three of its changes cite usage, as
the entries quoted above show, and other changes, such as removing Internet Explorer, cite none. So the
list changed when usage moved, and periodic reviews checked whether it had. The annual commitment dates
only from 2024: "18 September 2024 List of browsers to test in updated. Commitment to update browser
list updated to annual." [[8]](#ref-8) The history shows usage-driven change and periodic review, not a
yearly cycle, at high confidence for GOV.UK and unknown for any other team. Reading today's annual figure
as a floor on how long the conditions can go unchecked is the library's inference from that history, at
medium confidence, and it is the reading ADR 0088 left open. Jenkins' history records changes dated
2014, 2019, 2022 and 2025, each linked to a mailing-list discussion or governance meeting
[[12]](#ref-12). Calling that cadence discussion-driven is the research's inference from the dated
entries, at medium confidence.

**Telling users belongs in the action column.** MetaMask states its rule: "before bumping our minimum
supported browser versions, we should always notify users in the application first." [[15]](#ref-15) The
AMP project's deprecation process requires "Allow at least 2 weeks of open discussion after the I2D is
created before proceeding with the deprecation of the feature" and that "this change will be announced on
the mailing list and on Slack" [[34]](#ref-34). The audience there is developers of a library. Cockpit
asked for the login page to carry "a friendlier message that communicates that their browser does not work
and message which browsers do work" [[35]](#ref-35). The GOV.UK app's terms, by contrast, carry no review
cadence and no notice period on the page [[33]](#ref-33). The ONS records a dropped browser, Internet
Explorer, with a banner for the users who remain on it [[11]](#ref-11).

**Beginner note.** Write each condition as something an owner can observe, not as a date. Put the annual
floor last.

**Expert note.** Treat the annual figure as the longest the conditions can go unchecked, not as a
calendar rewrite of the document. That is the reading ADR 0088 and the family contract's `0.7.0` change
note record.

## 4. Variants and sizing

The bundle ships one size, `lean`. The research looked for a second size's evidence and did not find it.
It searched for per-row evidence columns, such as a usage share or a date last verified, and for a separate
polyfill or progressive-enhancement policy section. The government pages read carry neither
[[6]](#ref-6), [[7]](#ref-7), [[8]](#ref-8). The commercial pages record no tiers and no update policy
[[13]](#ref-13), [[15]](#ref-15), [[16]](#ref-16), and the structure check of per-row columns covered
only the government pages. GitHub's browser-support README documents a polyfill policy, with a named
owning team and a rule for ECMAScript features [[14]](#ref-14). It is a separate document beside the
matrix, not a section of one, which is why it does not argue for a second size. The nearest things are
the UI-Kit's principles list, which includes "Progressive enhancement over graceful degradation"
[[7]](#ref-7), and a dated history kept for the whole page [[8]](#ref-8), [[12]](#ref-12). The Review
Trigger section already holds that history. **The single `lean` size stands, at medium confidence.**

The signal for a second size is therefore a source, not a feeling. A named matrix that publishes per-row
evidence columns, or a polyfill policy as a section of the matrix itself, would be the evidence to weigh.

## 5. Methodology lineage

The research's six dimensions did not examine how any named delivery methodology treats the matrix, so
this section does not trace one. What the research found are practice traditions, each with a
different unit of support.

- **Graded support.** Yahoo [[1]](#ref-1), GOV.UK Frontend [[6]](#ref-6) and Jenkins [[12]](#ref-12)
  define levels by commitment. Springer Nature [[5]](#ref-5) uses two levels.
- **A usage threshold.** USWDS [[10]](#ref-10) and the ONS [[11]](#ref-11) bind inclusion to a figure.
- **A query.** Browserslist composes a list from rules and a team's own traffic [[17]](#ref-17).
- **A capability test.** MDN [[18]](#ref-18), [[19]](#ref-19) and Jeremy Keith [[20]](#ref-20) replace
  version lists with feature checks.
- **A bare support statement.** GitHub [[13]](#ref-13), MetaMask [[15]](#ref-15) and Material Components
  Web [[16]](#ref-16) publish what they support and, in the last case, what they test, without grades.

**The standards body places the matter elsewhere.** ISTQB lists compatibility among the quality
characteristics, and names test environment requirements among the test design work products: "Test design
work products include: (prioritized) test cases, test charters, coverage items, test data requirements and
test environment requirements." [[21]](#ref-21) The syllabus names no browser or device matrix document
[[21]](#ref-21).
## 6. Debates and contested boundaries

**A fixed usage threshold, against a query or judgment.** USWDS and the ONS state 2% [[10]](#ref-10),
[[11]](#ref-11), GOV.UK states coverage [[8]](#ref-8), and Browserslist argues that a floor alone has a
cost, and recommends combining a floor with other terms in a query [[17]](#ref-17). Browserslist also
warns against dropping browsers just because they are unfamiliar: "Don’t remove browsers just because
you don’t know them." [[17]](#ref-17) This companion's
recommendation is to state a threshold with a named analytics source, call it the team's own choice, and
accept Browserslist's caution that it entrenches the popular browsers. Each figure is one team's choice
for its own traffic. The 2% and the 98% are not norms.

**Supported against tested.** The sources use "support" in different senses, and the library treats this
as the sharpest point for the matrix's design, which is its own synthesis.

- Material Components Web defines the supported set as the tested set [[16]](#ref-16).
- MetaMask supports forks it does not test [[15]](#ref-15).
- Yahoo's X grade is untested [[1]](#ref-1), and GOV.UK Frontend says of a lower grade that it "will not
  regularly test in these browsers" [[6]](#ref-6).
- The Service Manual's own list is a list of browsers "to test in" [[8]](#ref-8).

A matrix that does not define its words inherits that ambiguity. That the senses differ is high
confidence. That this ambiguity is the cost to avoid, and that a matrix should mark testing separately, is
the library's synthesis and its sharpest teaching point.

**Capability tests against named versions.** MDN defines progressive enhancement as delivering "a baseline
of essential content and functionality to as many users as possible" [[18]](#ref-18). Of browser
sniffing it says "this is a terrible practice that should be discouraged at all costs"
[[19]](#ref-19), and it prefers feature checks: "it is the preferred method of determining browser support for
CSS features" [[19]](#ref-19). Jeremy Keith puts the argument as a question: "Instead of asking “which
browser are you?” and trying to infer feature support from the answer, it is safer to simply ask “do you
support this feature?”" [[20]](#ref-20) He quotes Brad Frost: "There is a difference between support and
optimization." [[20]](#ref-20) And he describes the fallback: "Browsers that don’t cut the mustard still
get access to the content, but without the JavaScript enhancements." [[20]](#ref-20)

**The camps coexist in practice.** The Service Manual keeps a browser list and also says to use
progressive enhancement [[8]](#ref-8). No source read argues that a support matrix is the wrong tool, so
this companion does not take that step. It treats a matrix as a statement of commitments and capability
tests as one way of meeting them, which is the library's reading and not a source's.

**Lineage and counting.** Whether GOV.UK's grades descend from Yahoo's is undocumented, so treat the link
as shared vocabulary [[1]](#ref-1), [[4]](#ref-4), [[6]](#ref-6). How many grades a scheme needs is open:
two [[5]](#ref-5), [[7]](#ref-7), three [[1]](#ref-1), [[12]](#ref-12), or four [[6]](#ref-6).

**Where assistive technology belongs.** GOV.UK keeps a separate page and table [[23]](#ref-23). A W3C
WCAG 3 working-group thread states a definition of an "accessibility support set" that "is used at higher
levels of conformance to define which user-agents and assistive technologies you test with."
[[26]](#ref-26) The same thread adds: "Also worth considering how this set will be kept updated/extended."
[[26]](#ref-26) It is a discussion thread, so it carries opinion and not a ruling, and the opening post
says the discussion was being closed and restarted. No source argues the question directly. This
bundle's answer is a reference from the matrix to wherever the combinations live.

**Whether a graded list is overhead for a small team.** No source read argues it either way. That is a
null result, and this companion makes no claim about it.

## 7. Anti-patterns and failure modes

**Beginner failures**

- **A grade defined by its letter.** A grade with no test commitment and no bug commitment promises
  nothing, and the same letter means different things in different schemes (section 2) [[1]](#ref-1),
  [[6]](#ref-6).
- **"Support" used for two promises in one column.** The reader cannot tell what the team tests, which is
  the supported-against-tested ambiguity in section 6 [[15]](#ref-15), [[16]](#ref-16).
- **A threshold with no named analytics source, or a borrowed figure presented as a standard.** The 2% and
  98% each belong to one team's traffic [[10]](#ref-10), [[11]](#ref-11), [[8]](#ref-8).
- **A browser listed that nobody tests.** The library's own test-case template warns against listing a
  matrix nobody will run, as the research log records from the working tree on 2026-11-12.
- **Every row simply supported.** A matrix with no demoted, untested or undecided row shows no judgment.
  This is the library's standard for its own example and not a finding from the sources.

**Subtler failures**

- **Silent drift.** The Service Manual states the risk: "Decisions about compatibility cannot be something
  you specify at the start of your project and then forget about." [[8]](#ref-8) A matrix with no owner and
  no trigger is the ungated case the family contract names.
- **Raising a minimum with no notice.** MetaMask requires users to be told first [[15]](#ref-15), AMP
  requires open discussion and an announcement [[34]](#ref-34), and Cockpit's login page points users to
  browsers that work [[35]](#ref-35). A matrix whose Review Trigger names no action beside a raised minimum
  leaves that step to chance.
- **Scope creep into other dimensions.** JavaScript-off is a build rule [[27]](#ref-27), bandwidth a budget
  [[28]](#ref-28) and viewport width layout configuration [[30]](#ref-30), [[31]](#ref-31). None is a row
  in this matrix.
- **Folding assistive technology into the browser table.** GOV.UK keeps its combinations on a page of
  their own [[23]](#ref-23), and the library's position is that the matrix should point to them.
- **Naming only one trigger.** The Service Manual's history shows reviews that changed nothing and
  changes that followed usage [[8]](#ref-8), and other sources record the drop of a browser
  [[10]](#ref-10), [[12]](#ref-12). The library's position is that the conditions are several.
- **Presenting the library's positions as received practice.** The Grade and Tested columns, the Notes
  column, the role names and the trigger table are labelled as the library's own.

## 8. Relationships to other artifacts

**The library's own templates already point at a matrix that does not exist.** The research log read these
from the working tree on 2026-11-12.

- The `test-case` template opens its Environment and Configuration section with "device or browser
  matrix", and its TRAP warns against listing a matrix nobody will run.
- The `test-plan` template holds environments as deployment tiers, and its full variant scopes
  compatibility in or out with no browser list.
- The `test-strategy` template covers default tooling and environments, with no browser defaults.
- The `bug-report` template records one observed browser, device and operating system per bug, with no
  field for whether that configuration is supported.
- The `prd` template opens Non-functional requirements, and nothing in the PRD bundle names compatibility,
  browsers or devices.

The matrix is the shared reference that the test case, the test plan and the bug report point to. That is
the library's inference, at medium confidence.

**What feeds it and what consults it.** The `prd` template's Non-functional requirements section is the
nearest place that precedes it, and the library's inference is that the matrix gives that section a
reference to name, at low confidence. The test plan, the test cases and bug triage consult it. Code consults
it too. GitHub's browser-support library keeps its code baseline tied to the matrix, "to ensure that our
baseline moves with our browser support matrix" [[14]](#ref-14), and keeps browsers below that baseline out
of its error monitoring [[14]](#ref-14). No government source names the monitoring use.

**The standards body places environments elsewhere.** ISTQB names test environment requirements as a test
design work product [[21]](#ref-21). Its configuration management practice records a test environment's
components so that past results can be reproduced: "For a complex configuration item (e.g., a test
environment), CM records the items it consists of, their relationships, and versions." [[21]](#ref-21)
A defect report includes "Identification of the test object and test environment" [[21]](#ref-21). The GOV.UK quality assurance page
states a goal, that a service "is easy to use for anyone who needs to use it, regardless of the device
they’re using" [[22]](#ref-22), and it names no document that records coverage [[22]](#ref-22).

## 9. Adaptations

- **Regulated settings.** The research did not examine regulated settings, and this bundle makes no claim
  about one.
- **Organization size.** No source argues that a graded list costs a small team too much. The
  practice dimension read five commercial support pages. GitHub's help page [[13]](#ref-13), MetaMask
  [[15]](#ref-15) and Material Components Web [[16]](#ref-16) state versions and carry no grades. GitHub's
  browser-support library [[14]](#ref-14) shows a baseline tied to the matrix. Springer Nature uses two
  levels [[5]](#ref-5). The accessibility sections also cite Deque [[24]](#ref-24) and Basecamp
  [[25]](#ref-25). The best commercial candidate with tiers was not read, because its host had no terms
  the research could find. The open-source Jenkins project is the one non-government source in which the
  research log records levels, a matrix and a dated change history together [[12]](#ref-12). Yahoo's
  scheme has grades and a dated update archive and links to a separate matrix page that was not read
  [[1]](#ref-1). Commercial teams publish support statements. Among them only Springer Nature was found
  with levels. Jenkins, an open-source project, is the other graded non-government source. High
  confidence for what was read.
- **Solo or team.** The research did not examine a solo maintainer, and this bundle makes no claim about
  one.
- **Internal-only products.** The ONS allows an evidence-based exemption for internal services
  [[11]](#ref-11), and the Service Manual
  lets evidence make a case for an exception [[8]](#ref-8). The Purpose and Scope section is where an
  exemption is stated.
- **Libraries and tools, as against sites.** Material Components Web is a component library [[16]](#ref-16),
  and the AMP deprecation process addresses developers of a library [[34]](#ref-34), not end users of a
  site. The Review Trigger's notice action should name which audience it addresses.
- **Native apps.** The GOV.UK app's terms publish a minimum operating system version
  [[33]](#ref-33). A product with an app can add rows that carry a minimum version, and no source read
  puts app and web support in one table.
- **Assistive technology.** Reference, as set out under Purpose and Scope [[23]](#ref-23).

## 10. Worked example

[`platform-device-support-matrix_example.md`](platform-device-support-matrix_example.md) is the matrix for
Harbourline Bookings, a passenger-ferry booking site run by a small fictional operator, in the `lean`
size. It is worth checking four things in it. First, that it has a mobile table and a desktop table, and
that every mobile row carries a minimum version or a version rule. Second, that at least one row promises
more than it tests: a browser at a supported grade marked Untested, with the reason given. Third, that a
threshold row has moved, with the analytics date and the owner who decided. Fourth, that its Review Trigger
table has a row that fired during the example's own history, so the trigger is shown working. Every figure
in it is labelled illustrative, and its threshold is the operator's own choice, not a norm. The example
also says where its assistive-technology combinations live.

---

## References

Access dates are the research date, 2026-11-12, because the research log records no per-source fetch date.
The GOV.UK Frontend v5 entry was read from a cached copy dated 2026-11-08.

<a id="ref-1"></a>[1] Yahoo YUI team. "[Graded Browser Support](https://github.com/yui/yui3/wiki/Graded-Browser-Support)," yui/yui3 wiki on GitHub (accessed 2026-11-12). Supports the existence and definitions of YUI Graded Browser Support: three grades (C, A, X), what each means, what QA does for each, and the dated update archive from 2008-02-19 to 2012-07-26. It does not state the original publication date or the author. [primary]

<a id="ref-2"></a>[2] GOV.UK Design System team. "[Browser support](https://frontend.design-system.service.gov.uk/browser-support/)," GOV.UK Frontend documentation, latest version (accessed 2026-11-12). Supports four grades (A, B, C, X), each tied to a testing level and a bug priority. The page does not mention Yahoo or YUI. [primary]

<a id="ref-3"></a>[3] GOV.UK Frontend team. "[How we provide support for different browsers](https://raw.githubusercontent.com/alphagov/govuk-frontend/main/docs/contributing/browser-support.md)," alphagov/govuk-frontend contributor docs (accessed 2026-11-12). Supports the same four-grade scheme in the maintainers' own documentation, with a first commit on 2023-10-24. It contains no mention of Yahoo or YUI. [primary]

<a id="ref-4"></a>[4] GOV.UK Frontend team. "[Explore frameworks to help us make decisions about browser support for features](https://github.com/alphagov/govuk-frontend/issues/3293)," alphagov/govuk-frontend issue 3293, opened 2023-02-15 (accessed 2026-11-12). Supports the adoption of the phrase "graded browser support" in 2023 as a move to a model where not every user gets the same experience. The issue bodies do not name Yahoo or YUI. [primary]

<a id="ref-5"></a>[5] Springer Nature frontend team. "[Browser support](https://github.com/springernature/frontend-playbook/blob/HEAD/practices/graded-browser-support.md)," springernature/frontend-playbook (accessed 2026-11-12). Supports a named adopter that says it uses a variant of Yahoo's scheme and credits Nate Koechley with the concept, using two levels (Core, Enhanced), and a 2018-08-23 rename of the page. [practitioner]

<a id="ref-6"></a>[6] GOV.UK Design System team. "[Browser support](https://frontend.design-system.service.gov.uk/v5/browser-support/)," GOV.UK Frontend v5 documentation, cached copy dated 2026-11-08 (accessed 2026-11-08). Supports four grades carried as prose-and-list blocks, each with a definition, a test commitment and a bug-fix commitment, and no usage-share or verified-date column. [primary]

<a id="ref-7"></a>[7] Australian Digital Transformation Office. "[Browser support](https://github.com/AusDTO/gov-au-ui-kit/blob/develop/BROWSER-SUPPORT.md)," AusDTO/gov-au-ui-kit, archived 2018 (accessed 2026-11-12). Supports the exact column headers of the matrix, two tables with different column sets, a section sequence ending in principles, and a parallel form that does not use grade letters or name YUI. [primary]

<a id="ref-8"></a>[8] GOV.UK Service Manual. "[Designing for different browsers and devices](https://www.gov.uk/service-manual/technology/designing-for-different-browsers-and-devices)," gov.uk (accessed 2026-11-12). Supports a two-column test list dated "from February 2026", a coverage figure, a prose rule to use analytics, a full dated update history with review-only entries and change entries, and a one-line progressive-enhancement instruction. [primary]

<a id="ref-9"></a>[9] Government Digital Service. "[Supporting different browsers](https://gds-way.digital.cabinet-office.gov.uk/manuals/browser-support.html)," The GDS Way (accessed 2026-11-12). Supports government practice: the Service Manual list as the floor, analytics and user research deciding extra browsers, stated grounds for declining an out-of-policy fix, a named page owner, and a review cycle. It also states that the GDS Way is internal-use content. [primary]

<a id="ref-10"></a>[10] U.S. Web Design System. "[Getting started for developers](https://designsystem.digital.gov/documentation/getting-started-for-developers/)," designsystem.digital.gov (accessed 2026-11-12). Supports a quantitative inclusion rule tied to an external analytics source, with progressive enhancement for the rest, and the end of Internet Explorer 11 support. [primary]

<a id="ref-11"></a>[11] Office for National Statistics. "[Browser testing](https://service-manual.ons.gov.uk/design-system/guidance/browser-testing/)," ONS Design System (accessed 2026-11-12). Supports a 2% analytics threshold for extra browsers on top of the GOV.UK list, and an evidence-based exemption for internal services. [primary]

<a id="ref-12"></a>[12] Jenkins project. "[Browser compatibility policy](https://github.com/jenkins-infra/jenkins.io/blob/master/content/doc/book/platform-information/support-policy-web-browsers.adoc)," jenkins-infra/jenkins.io source on GitHub (accessed 2026-11-12). Supports an open-source product's three-level policy, a browser-by-level matrix with N and N-1 rules, and a dated change history linking each change to a mailing-list discussion or governance meeting. [primary]

<a id="ref-13"></a>[13] GitHub. "[Supported browsers](https://github.com/github/docs/blob/main/content/get-started/using-github/supported-browsers.md)," github/docs source on GitHub (accessed 2026-11-12). Supports a commercial help page that names the latest browsers, gives a best-effort statement for extended-support releases, has no grades, and gives one bug-triage rule. [vendor]

<a id="ref-14"></a>[14] GitHub. "[browser-support README](https://github.com/github/browser-support/blob/main/README.md)," github/browser-support (accessed 2026-11-12). Supports the matrix consulted in code: a feature baseline below which browsers send no errors or statistics to monitoring, and polyfills decided under a named owning team. [vendor]

<a id="ref-15"></a>[15] MetaMask. "[Browser support](https://github.com/MetaMask/metamask-extension/blob/develop/docs/browser-support.md)," MetaMask/metamask-extension docs (accessed 2026-11-12). Supports a standing policy stated as version windows, a tested-versus-tried distinction for forks, and a rule to notify users in the application before raising a minimum. [vendor]

<a id="ref-16"></a>[16] Google. "[Supported browsers](https://github.com/material-components/material-components-web/blob/master/docs/supported-browsers.md)," material-components-web docs (accessed 2026-11-12). Supports a commercial open-source component library whose support set is the tested set, with no tiers and no update policy. [vendor]

<a id="ref-17"></a>[17] Browserslist project. "[README](https://github.com/browserslist/browserslist)," browserslist/browserslist (accessed 2026-11-12). Supports the query-based camp: a usage floor with a stated caution, a warning against dropping browsers just because they are unfamiliar, and queries built from a team's own traffic. [primary]

<a id="ref-18"></a>[18] MDN Web Docs. "[Progressive enhancement](https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement)," glossary (accessed 2026-11-12). Supports progressive enhancement as a baseline for as many users as possible, with the best experience only on modern browsers. [primary]

<a id="ref-19"></a>[19] MDN Web Docs. "[Implementing feature detection](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Testing/Feature_detection)" (accessed 2026-11-12). Supports the feature-detection camp's rejection of browser-identity checks and its preference for CSS `@supports`. [primary]

<a id="ref-20"></a>[20] Jeremy Keith. "[Resilient Web Design, chapter 5](https://resilientwebdesign.com/chapter5/)," resilientwebdesign.com (accessed 2026-11-12). Supports the argument that capability tests replace identity, and the distinction between support and optimization. [practitioner]

<a id="ref-21"></a>[21] ISTQB. "[Certified Tester Foundation Level Syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)" (accessed 2026-11-12). Supports compatibility as a quality characteristic, test environment requirements as a test design work product, configuration records for a test environment, and a defect report that identifies the test environment. It names no browser or device matrix document. [standards]

<a id="ref-22"></a>[22] GOV.UK Service Manual. "[Quality assurance: testing your service regularly](https://www.gov.uk/service-manual/technology/quality-assurance-testing-your-service-regularly)," gov.uk (accessed 2026-11-12). Supports a device-independence goal and a list of testing types, and names no document that records which browsers or devices are covered. [primary]

<a id="ref-23"></a>[23] GOV.UK Service Manual. "[Testing with assistive technologies](https://www.gov.uk/service-manual/technology/testing-with-assistive-technologies)," gov.uk (accessed 2026-11-12). Supports a published table of assistive-technology, version and browser combinations a service must work with before public beta. [primary]

<a id="ref-24"></a>[24] Deque Systems. "[Accessibility supported](https://github.com/dequelabs/axe-core/blob/develop/doc/accessibility-supported.md)," dequelabs/axe-core docs (accessed 2026-11-12). Supports a tool vendor's list of tested screen reader, browser and operating system combinations and its inclusion rule of use by more than 1% of users. [practitioner]

<a id="ref-25"></a>[25] Basecamp. "[Screen reader setup and testing](https://github.com/basecamp/accessibility/blob/master/Section-2/Screen-reader-setup-and-testing.md)," basecamp/accessibility (accessed 2026-11-12). Supports a commercial team's published screen reader and platform combinations, with a primary and a secondary. [practitioner]

<a id="ref-26"></a>[26] W3C WCAG 3 working group. "[Default accessibility support set](https://github.com/w3c/wcag3/discussions/277)," w3c/wcag3 discussion 277 (accessed 2026-11-12). Supports a working-group thread defining an accessibility support set and asking how it will be kept updated. It is a discussion thread, so it carries opinion and not a ruling. [standards]

<a id="ref-27"></a>[27] GOV.UK Service Manual. "[Building a robust frontend using progressive enhancement](https://www.gov.uk/service-manual/technology/using-progressive-enhancement)," gov.uk (accessed 2026-11-12). Supports JavaScript-disabled support as a mandatory building rule, not a matrix row. [primary]

<a id="ref-28"></a>[28] GOV.UK Service Manual. "[How to test frontend performance](https://www.gov.uk/service-manual/technology/how-to-test-frontend-performance)," gov.uk (accessed 2026-11-12). Supports low-bandwidth and low-spec support handled as a performance budget and a testing practice, not a matrix dimension. [primary]

<a id="ref-30"></a>[30] Office for National Statistics. "[Layout: grid](https://service-manual.ons.gov.uk/design-system/foundations/grid)," ONS Design System (accessed 2026-11-12). Supports viewport breakpoints specified as device-agnostic layout configuration, not tied to any supported or unsupported statement. [primary]

<a id="ref-31"></a>[31] U.S. Web Design System. "[Layout grid](https://designsystem.digital.gov/utilities/layout-grid/)," designsystem.digital.gov (accessed 2026-11-12). Supports USWDS breakpoints as layout configuration, with no supported-viewport floor stated. [primary]

<a id="ref-33"></a>[33] Government Digital Service. "[GOV.UK app: terms and conditions](https://www.gov.uk/guidance/govuk-app-terms-and-conditions)," gov.uk (accessed 2026-11-12). Supports a native-app support statement published as a minimum-operating-system list, with no review cadence or notice period on the page. [primary]

<a id="ref-34"></a>[34] AMP Project. "[Intent to Deprecate: IE11 Support](https://github.com/ampproject/amphtml/issues/34453)," ampproject/amphtml issue 34453 (accessed 2026-11-12). Supports one project's recorded process for communicating a browser support drop, with a two-week open-discussion rule and an announcement. The audience is developers of a library. [practitioner]

<a id="ref-35"></a>[35] Cockpit project. "[login: add message for Internet Explorer deprecation](https://github.com/cockpit-project/cockpit/issues/9689)," cockpit-project/cockpit issue 9689 (accessed 2026-11-12). Supports one project's end-user-facing communication of a browser support drop: a warning first, then a block that points to working browsers. [practitioner]
