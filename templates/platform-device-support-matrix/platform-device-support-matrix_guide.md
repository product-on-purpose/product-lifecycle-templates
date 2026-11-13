# Guide: Platform and Device Support Matrix (operator card)

The short card. The reasoning behind every rule here, with the sources, is in
[`platform-device-support-matrix_companion.md`](platform-device-support-matrix_companion.md). A fully
worked instance is [`platform-device-support-matrix_example.md`](platform-device-support-matrix_example.md).
Where this card calls something the library's position, no source read for the bundle publishes it, and
the card says so each time.

## When to use

- A team has to choose which browsers to test, and you want a standing written answer rather than a
  fresh decision for each release. The GDS Way and the ONS both treat the browser list as what a team
  consults for that choice.
- Someone triages a bug from a browser the team does not list, and you want the rule for what that
  report is worth written down. The GDS Way, Jenkins and GitHub each state such a rule.
- An engineer decides what a polyfill or a code baseline must cover, and needs the matrix to decide
  against. GitHub's browser-support library ties its baseline to its matrix.
- You need to say what a user on a given browser gets, and separately what the team tests. The sources
  use the word "support" for both, so a matrix that does not define the word inherits the ambiguity.
- Some audiences need less than the rest, such as an internal tool used by staff on one managed
  browser. The Service Manual lets evidence make a case for an exception, and the ONS allows an
  evidence-based exemption for internal services. The Purpose and Scope section is where that exemption is stated.
- You want the page to name who may change a grade and what event makes it wrong. The Service Manual
  says why the page must be standing: "Decisions about compatibility cannot be something you specify at
  the start of your project and then forget about."

## When NOT to use

- **You are recording the browsers one release was tested on.** That belongs in a test plan's
  environment section. This document is standing, and it states which environments get which promise.
  The boundary is the family contract's call, not a sourced finding.
- **You are writing one test case's environment.** A test case states its own environment and
  configuration. The library's `test-case` template already opens that section with "device or browser
  matrix", and its TRAP warns against listing one nobody will run. That the matrix is the shared
  reference a test case points to is the library's inference, at medium confidence.
- **You are reporting one bug.** A bug report records the one browser, device and operating system where
  the bug was seen, and the `bug-report` template has no field for whether that configuration is
  supported. The triager compares the report against this matrix, which is the same inference at medium
  confidence.
- **You need a table of assistive-technology combinations.** GOV.UK keeps its table on a page of its own.
  The matrix should say where those combinations live and hold none of them. That is the library's
  reading, at medium confidence.
- **You want a rule about JavaScript switched off, a slow connection or a screen width.** The sources
  place each elsewhere: GOV.UK makes JavaScript-off a build rule, treats bandwidth as a performance
  budget, and the ONS and USWDS configure breakpoints as layout and not as a support commitment. None is
  a matrix row.
- **You want to decide between version lists and feature detection.** MDN and Jeremy Keith argue for
  capability tests, and the Service Manual keeps a browser list while also saying to use progressive
  enhancement. No source read argues that a matrix is the wrong tool, so this card does not either. A
  matrix states commitments, and a capability test is one way of meeting them. That reading is the
  library's.

## Pick a variant

This bundle ships one size, lean, so there is no second variant to choose. The research looked for the
evidence a heavier size would need: per-row evidence columns such as a usage share or a date last
verified, and a separate polyfill policy. The pages read carry neither. The single size stands at medium
confidence. A named matrix that publishes per-row evidence columns, or a polyfill policy kept apart from
its support grades, would be the evidence for a second size. A feeling that the page needs more is not.
See [`platform-device-support-matrix_companion.md` section 4](platform-device-support-matrix_companion.md#4-variants-and-sizing).

Three choices remain inside the one size. Settle them in this order.

1. **How many grades.** The sources disagree. Yahoo has three grades, GOV.UK Frontend four, Jenkins
   three levels, and Springer Nature and the AusDTO UI-Kit two. Grades are also optional. Material
   Components Web has none, and defines its support as the set it tests. A team whose whole promise is
   the latest browsers, tested, can run one grade, and the cost is that the page has nowhere to say a
   browser is supported but untested. This card's advice is to write one grade for each different set
   of three answers: what the user gets, what the team tests, and what the team does about a bug. Merge
   two grades whose three answers match. That advice is not a sourced rule.
2. **A minimum version or a version rule.** A minimum names one version, and the UI-Kit gives a reason
   for its minimum: "Minimum version based on support for CSS Flexible Box layout modules". A rule
   states a window. MetaMask states "The last two years of Chrome stable releases", and the UI-Kit
   states "All browsers listed are latest stable release, except Internet Explorer." Fill the mobile
   table first and give every mobile row one or the other. That ordering is the library's advice.
3. **Which figure brings a browser in.** Every figure in the sources is one team's choice for its own
   traffic, so choose yours and name its analytics source. See the Threshold Rule section.

## Quality rubric (self-grade)

Score each row 0, 1 or 2. Under 15 out of 22 and a tester, a triager or an engineer reading the matrix
still cannot tell from the page which browsers get which promise, or whom to ask when a row looks wrong.
Grade what the author added to the blank template. The template already prints the column headings and
the five Review Trigger conditions, so a row that rewards their presence is satisfied before anyone
writes a word.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Scope is bounded** | No product is named, or the scope reads "all modern browsers" with no record and no reader | The product and the place the record lives are named, but nothing says which audiences are exempt, and nothing says that none is | You can point at the sentence naming the product, the record and who reads it, and at either the audience it exempts with the evidence for the exemption, or a line saying no audience is exempt and why |
| 2 | **Grades are commitments** | A grade is a letter or an adjective, with no test commitment and no bug commitment | Each grade says what a user gets, but at least one grade omits what the team tests or what it does about a bug | For every grade you can point at what the user gets, what the team tests and what it does about a bug, and a stranger could say what the lowest grade promises without asking anyone |
| 3 | **Promise and test apart** | One column holds both the promise and the testing, or "supported" is used with no definition | Grade and Tested are filled in, but Tested repeats what the grade says the team should do rather than what it does today | The person who runs the pre-release checks would confirm each Tested value, and wherever Tested falls short of its grade's test commitment, or a row is undecided, Notes gives the reason |
| 4 | **Versions and date** | Mobile rows carry no minimum version or rule, and the effective-from date is blank or a placeholder | The mobile rows are versioned but the date is missing, or the date is present and the owner cannot say what it records | A tester can read any mobile row and say which version to install without asking, and the effective-from date is one the owner can explain, such as the review-history line that set it |
| 5 | **Threshold has a source** | A bare figure, or a figure borrowed from another team's rule | An analytics source and a decider are named, but nothing says why the figure fits this product's traffic | You can point at the analytics source, the person who reads it, the person who decides, and the sentence saying why the figure is this product's own, and a reader could open that report and check the figure |
| 6 | **Threshold runs both ways** | Only the way a browser enters the matrix is written | An exit rule exists, but it names no figure or event, or the Ownership section names nobody who is told when a browser falls below the line | You can point at the exit rule, at the figure or event that fires it, at what happens to the row, and at the Ownership section naming who is told |
| 7 | **Unsupported has an answer** | "Other browsers are not supported", and nothing more | The page says what a user on an unlisted browser gets, or what happens to a report from one, but not both, or it declines a fix without naming grounds | A support agent could say aloud what a person on an unlisted browser gets, the page says what the team does with a report from one, and each ground for declining a fix is written so that a reply can say which ground applied |
| 8 | **Owner is reachable** | "The team", or no owner | A role is named without a person, or a person without the place where changes are discussed | You can point at the role, the person in it, the place where changes are discussed, who may change a grade or the threshold, and who is told, and you could message the owner today |
| 9 | **Triggers carry owners** | The Review Trigger table is blank, or says "review regularly" | Some conditions have a named role and an action, but at least one row has neither, or the annual floor is the only row that does | Every condition has a role as owner and an action, the annual floor sits last and says what the owner does, and the review history holds a dated line for each firing or run, including "no change", or says the matrix is new |
| 10 | **Notice is planned** | A raised minimum has no action beside it | An action says to tell users and names no audience, place or timing | The action beside a raised minimum names who is told, whether end users or developers of a library, where they are told, and that it happens before the minimum rises |
| 11 | **Assistive technology by reference** | The matrix says nothing about assistive technology, or it holds combinations inside the browser table | The scope section names a location for the combinations, but the location does not exist or lists none | The scope section names where the combinations live, you can follow the pointer and find them, and the browser tables hold none |

The test behind every cell above: could someone satisfy it without improving the document? A row that
counted browsers, grades or conditions would reward padding the table. Each cell asks instead whether a
specific fact is on the page that a second reader, not the author, could point at. Grade with someone
who did not write the matrix. The blank template should score 0 on every row, and a new, honest matrix
can score 2 on every row without inventing a demotion or a fired trigger.

## Named anti-patterns (the usual wrecks)

1. **A grade defined by its letter.** The same letter means different things in different schemes, so a
   letter alone promises nothing. The Support Grades section and companion section 2 fix it.
2. **One column, two promises.** "Support" can mean what the user gets or what the team tests, and one
   status column cannot say both. Keep Grade and Tested apart, as The Matrix section does. The
   separation is the library's position.
3. **A borrowed figure presented as a standard.** Each figure in the sources is one team's choice for its
   own traffic. State your own figure and analytics source, as the Threshold Rule section asks.
4. **Listing a browser nobody tests.** A row marked Tested that the team does not run is a false claim.
   The Tested column and the Notes column in The Matrix section are where the truth goes.
5. **Every row simply supported.** A matrix with no demoted, untested or undecided row shows no judgment.
   This is the library's standard for its own example and not a finding from the sources. Companion
   section 7 explains.
6. **Writing only the entering side of the threshold.** A rule that never says when a browser leaves lets
   the matrix grow without a decision. The Exit rule field in the Threshold Rule section fixes it.
7. **A flat refusal.** "Not supported" skips the investigation that triage needs first. The Unsupported
   Browsers section names the grounds for declining a fix, and companion section 3 gives the sources.
8. **Silent drift, or the annual review as the whole mechanism.** A matrix with no owner and no trigger
   is the ungated case the family contract names. The list changed when usage moved, and periodic
   reviews checked whether it had. Reading the annual figure as a floor is the library's inference, at
   medium confidence. The Review Trigger section holds the conditions, and companion section 3 holds the
   evidence.
9. **Raising a minimum with no notice.** A Review Trigger row that names no notice action leaves that
   step to chance, and the audience, end users or developers, has to be named. The Review Trigger
   section's action column is the place, and companion section 3 gives the sources.
10. **Scope creep into other dimensions.** JavaScript switched off, a slow connection, a screen width and
    assistive-technology combinations are not rows in this matrix. The matrix points at where they live.
11. **Presenting the library's positions as received practice.** The separate Grade and Tested columns
    have support in the sources all the same. The Notes column has only partial support. The role names
    in Ownership are a proposal, because no source names a role that may change a grade. The table form
    of the Review Trigger is also the library's own. A filled matrix may keep them, and it should not
    describe them as a standard.

## Pairing with your process

This bundle ships in the `standing-standards` family as a **foundation**: a standard that a team's test
choices and bug triage are judged against, rather than an instrument executed under time pressure. The
reasoning is in
[ADR 0088 (the platform and device support matrix joins standing-standards as a foundation)](../../docs/internal/decisions/0088-platform-device-support-matrix-joins-standing-standards-as-a-foundation.md).
Three documents in this library point at a matrix that this bundle supplies: the test case, the test
plan and the bug report. That is the library's inference, at medium confidence. The `prd` template's
Non-functional requirements section is the nearest place that precedes the matrix, and the inference
that the matrix gives that section a reference to name is at low confidence.

Update the matrix when a Review Trigger condition fires, not on a calendar. Treat the annual figure
as the longest the conditions can go unchecked, and not as a calendar rewrite of the document. That
reading is the library's inference at medium confidence. The GOV.UK history shows the list changing when
usage moved and periodic reviews checking whether it had. The quoted review-only entries date from 2020
and 2021, and the annual commitment dates from 2024.

## What the research did not settle

- **Whether keeping a matrix helps.** No source read shows that a matrix improves outcomes, and none
  measures what keeping one costs.
- **Whether a graded list is overhead for a small team.** No source read argues it either way.
- **Regulated settings and a solo maintainer.** The research did not examine either, and this card makes
  no claim about them.
- **How often a team should review.** The quoted GOV.UK review-only entries are about six months apart,
  and its annual commitment dates from 2024. Treat the cadence of any other team as unknown.
- **The role names in Ownership.** No source read names a person or role who may change a grade, so the
  role names are a proposal and not received practice.
