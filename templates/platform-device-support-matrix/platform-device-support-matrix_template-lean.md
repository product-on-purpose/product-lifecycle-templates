---
title: "{{product_name}} Platform and Device Support Matrix"
doc_type: platform-device-support-matrix
size: lean
product_name: "{{product_name}}"
owner: "{{owner}}"
status: draft
doc_version: "{{doc_version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: platform-device-support-matrix
source_template_version: 0.1.0
---

<!--
LEAN PLATFORM AND DEVICE SUPPORT MATRIX. This bundle ships one size, deliberately. The research looked for
the evidence a second, heavier weight would need: per-row evidence columns, such as a usage share or a date
last verified, and a separate polyfill or progressive-enhancement policy section. The pages it read carry
neither. The nearest things are a principles list and a dated history kept for the whole page, and the
Review Trigger section below already holds that history. A longer variant would model the weight the
research rejected, so the document stays short on purpose. Confidence in the single size is medium. See
platform-device-support-matrix_companion.md section 4 (Variants and sizing).

A MATRIX MAKES TWO PROMISES, AND THIS TEMPLATE KEEPS THEM APART.
One is what a user on a given browser gets. The other is what the team tests. The sources use the word
"support" for both: Material Components Web defines its supported set as the set it tests, MetaMask
supports browser forks it does not test, and the GOV.UK Service Manual's own list is a list of browsers
"to test in". A matrix that does not define its words inherits that ambiguity. So the grades below are
defined by their commitments, and testing is marked in a column of its own. That the senses differ is well
supported. That a matrix should therefore mark testing separately is this library's position. See
platform-device-support-matrix_companion.md section 6 (Debates and contested boundaries).

SOME OF THIS STRUCTURE IS THIS LIBRARY'S OWN POSITION, NOT RECEIVED PRACTICE.
No source read for this bundle has separate Grade and Tested columns or a Notes column. None names a person
or a role that may change a grade, and none sets its review conditions out as a table. Each of these is
labelled where it appears. Nothing here is a standard. Every threshold figure in the sources is one team's
choice for its own traffic. The evidence base is public matrices from government, design-system and
open-source teams plus five commercial pages, and no source shows that keeping a matrix improves outcomes
or measures what keeping one costs.

WHAT THIS IS NOT
It is NOT the list of browsers one release was tested on. That belongs in a test plan's environment
section. This document is standing: it states which environments get which promise, and it is consulted
every time a team picks browsers to test or triages a bug from an unusual one. That boundary is the
family contract's call, not a sourced finding.
It is NOT an assistive-technology table. Those combinations live on a page of their own and this document
points at them.
It is NOT a rule about JavaScript being switched off, a slow connection or a screen width. The sources
treat each as something other than a matrix row. See platform-device-support-matrix_companion.md section 3
(Anatomy).

All names and figures in the GOOD and WEAK illustrations below are invented.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   platform-device-support-matrix_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and
   a WEAK example, and the TRAP to avoid. The Support Grades, The Matrix and Review Trigger tables also
   carry PRIORITY and ROW HINT.
2. Replace each {{placeholder}} with your content.
3. If a section, or one row inside a table, does not apply, write "N/A" and one line of why, rather than
   leaving it blank or deleting the section. An unexplained blank and a skipped item look identical to a
   later reader.
4. This is a standing document, revisited on the Review Trigger below, not written once and forgotten.
   Before you first share it: self-grade against platform-device-support-matrix_guide.md, then DELETE every
   HTML comment. They are guidance, not content. Keep the source_template and source_template_version
   frontmatter fields: they are the only record of which template and version produced this document.
-->

# {{product_name}} Platform and Device Support Matrix

## Purpose and Scope

<!-- WHAT  Which product this matrix covers, who relies on it, whether this file or a tool is the record,
           which audiences are exempt, and where the assistive-technology combinations live.
     WHY   It says which product the promises apply to. The AusDTO UI-Kit file opens with its purpose:
           "The UI-Kit team needs to support all of our users, regardless of their device, web browser or
           other user agent." The GDS Way adds a reason to scope by product: "The exact set of browsers you
           build for will vary by project". The ONS names the floor under any list: "Services do not have
           to look perfect in every browser, but users must be able to access and use all the information
           and features they need." Audience exceptions have two sources. The Service Manual lets evidence
           change the requirement: "If evidence shows that your users have specific needs or extra support
           requirements, you can use this to make a case for not meeting these browser requirements." The
           ONS allows an evidence-based exemption for a class of services: "internal services used
           exclusively by ONS staff may not need to work on all supported browsers". Assistive technology goes by reference, not inside the
           matrix: GOV.UK publishes its table of combinations on a page of its own, saying "your service
           must work with at least the following combinations of assistive technologies and browsers
           before it goes into public beta". That reading is this library's, at medium confidence. The
           form of the scope statement is this library's position; no source publishes one. The Service
           Manual says why the page is standing: "Decisions about compatibility cannot be something you
           specify at the start of your project and then forget about."
           Deep dive: platform-device-support-matrix_companion.md section 3 (Anatomy > Purpose and Scope).
     ASK   Which product does this cover, and who reads it? Is this file the record or a tool, and where do
           the assistive-technology combinations live? Which audiences are exempt, and what evidence says
           so?
     GOOD  "This matrix covers the Fernhill Library public catalogue site. It does not cover the staff
           cataloguing tool, an internal service used only by library staff on managed laptops, which is
           exempt because every staff machine runs one browser. The record is this file in the site
           repository. Testers and whoever triages bug reports both read it. Assistive-technology
           combinations are kept in the accessibility test guide, linked below, not here."
     WEAK  "We support all modern browsers." (names no product, no reader and no record, exempts no
           audience, and says nothing about assistive technology)
     TRAP  Letting the scope grow past browsers and devices. JavaScript switched off is a build rule in the
           sources, bandwidth is a performance budget and a screen width is layout configuration. None is a
           matrix row. Folding assistive-technology combinations into the browser table is the same
           mistake, and it is this library's position that the matrix should point to them instead. -->

**Product covered:** {{product_covered}}

**Who relies on this matrix:** {{matrix_readers}}

**Where the record lives:** {{record_location}}

**Audiences exempt, and the evidence:** {{audience_exceptions}}

**Assistive-technology combinations live at:** {{assistive_technology_location}}

## Support Grades

<!-- WHAT  Each grade this matrix uses, with what a user on it gets, what the team tests, and what the
           team does about a bug. This section defines the words The Matrix then uses.
     WHY   The sources define grades by what the team commits to do, and the commitments differ. GOV.UK
           Frontend commits to priority: "treat bugs affecting Grade A browsers as high priority", and
           "treat bugs affecting Grade B browsers as low priority unless we find evidence they prevent a
           user from being able to complete their task". For its lowest grade it commits to neither
           testing nor fixing: "will not regularly test in these browsers" and "We will not fix bugs
           affecting these browsers." Yahoo's older scheme states its lowest grade the same plain way:
           "QA does not test, and bugs are not opened against X-grade browsers." The letters do not carry
           across schemes. In Yahoo's, "C-grade is the base level of support, providing core content and
           functionality." In GOV.UK's, C is a reduced grade and X gets no fixes. A grade defined only by
           its letter therefore promises nothing a reader can use. The number of grades is open: Yahoo
           has three, GOV.UK Frontend four, Jenkins three levels, and Springer Nature and the AusDTO
           UI-Kit two. Grades are also optional. Material Components Web has none: "We officially support
           the last two versions of every major browser. Specifically, we test on the following
           browsers:" The cost of one grade is that the page has nowhere to say a browser is supported but
           untested.
           Deep dive: platform-device-support-matrix_companion.md section 3 (Anatomy > Support Grades).
     ASK   For each grade: what does a user on it get? What will the team test on it, and what will it not
           test? What does the team do about a bug on it: fix with priority, fix only if it blocks a task,
           or not fix? Could a stranger read the row and say what the team promised?
     PRIORITY  List grades from the strongest promise to the weakest, and write the lowest grade's bug
           commitment before anything else. Both GOV.UK and Yahoo state it for their lowest grade in
           plain words. The ordering is this library's advice, not a sourced rule.
     ROW HINT  A good row names a grade, says what the user gets, says what the team tests, and says what it
           does about a bug, each as something the team actually does. A weak row is a letter and an
           adjective.
     GOOD  | Supported | The full catalogue, including saved searches and reading lists | Checked by hand on
           a real device whenever the search or account pages change | Fixed ahead of other work |
     WEAK  | Grade A | Full support | | | (a letter and a phrase; no test commitment and no bug commitment)
     TRAP  Defining a grade by its letter, or putting two promises in one cell. "Supported" that means
           "we promise it works" in one row and "we test it" in another leaves the reader unable to tell
           what the team tests. This column set keeps the user's experience, the testing and the bug
           response apart. -->

| Grade | What a user gets | What the team tests | What the team does about a bug |
|---|---|---|---|
| {{grade_name}} | {{grade_user_gets}} | {{grade_test_commitment}} | {{grade_bug_commitment}} |

## The Matrix

<!-- WHAT  A mobile table and a desktop table, each row a browser, with an effective-from date. The columns
           are Browser, Platforms, a minimum version or a version rule, Grade, Tested, and Notes.
     WHY   It is the table itself: the browsers, platforms, versions, grades and test status that the other
           sections define and govern. THE COLUMN SET IS PARTLY THIS LIBRARY'S POSITION. The AusDTO
           UI-Kit's mobile header row is "Browser Platforms Minimum version Advanced support status". Its
           desktop table has no minimum version column, and its single status column holds both the level
           and the test status. No source read has separate Grade and Tested columns, and none has a Notes
           column. The separation still has support. The GDS Way separates what a team builds for from
           what it tests, and MetaMask shows a row one status column cannot express: "We try to support
           browser forks as well (aligned with supported Chrome/Firefox releases), but we don't actively
           test them." A version rule can replace a minimum version. MetaMask states "The last two years of
           Chrome stable releases", and the UI-Kit states "All browsers listed are latest stable release,
           except Internet Explorer." That reading of the column is this library's synthesis, at medium
           confidence. The Service Manual dates its table: "Browsers to test in (from February 2026)". This
           library borrows the dated line from that one source, at medium confidence. A row may also
           be left open on purpose: Jenkins says "Support for mobile browsers (e.g. iOS Safari) has not yet been
           determined." No source read puts native-app support and web support in one table, and the
           GOV.UK app's terms publish "iPhones running iOS 16 or later" as a minimum operating system.
           Deep dive: platform-device-support-matrix_companion.md section 3 (Anatomy > The Matrix).
     ASK   Which browsers and platforms does the team promise something to, and what is the minimum
           version or rule for each? Which grade from Support Grades does each get? Is each row actually
           tested today, and if its Tested value falls short of what its grade promises, why? Which row is
           undecided, and does the table say so?
     PRIORITY  Fill the mobile table first and give every mobile row a minimum version or a version rule.
           Mark Tested from what the team does today, not from what its grade says it should do.
     ROW HINT  A good row names the browser and platform, gives a minimum version or a rule, names a grade
           defined above, marks Tested or Untested, and uses Notes to give the reason whenever Tested falls
           short of the grade's test commitment or the row is undecided. A weak row is a browser name with
           the other cells blank or all saying "supported".
     GOOD  | Brave | Windows, macOS | Same rule as Chrome | Supported | Untested | Chromium-based. We fix
           reported bugs, but nobody runs it before a release. |
     WEAK  | Chrome | All | Latest | Supported | Yes | | (every cell filled and no decision visible)
     TRAP  Listing a browser nobody tests, or marking every row simply supported. A matrix with no
           demoted, untested or undecided row shows no judgment; that is this library's standard, not a
           finding from the sources. The library's own test-case template makes the related warning,
           against listing a matrix nobody will run. -->

**Effective from:** {{effective_from_date}}

**Mobile browsers**

| Browser | Platforms | Minimum version or version rule | Grade | Tested | Notes |
|---|---|---|---|---|---|
| {{browser_name}} | {{platforms}} | {{minimum_version_or_rule}} | {{grade_name}} | {{tested_status}} | {{row_notes}} |

**Desktop browsers**

| Browser | Platforms | Minimum version or version rule | Grade | Tested | Notes |
|---|---|---|---|---|---|
| {{browser_name}} | {{platforms}} | {{minimum_version_or_rule}} | {{grade_name}} | {{tested_status}} | {{row_notes}} |

## Threshold Rule

<!-- WHAT  The rule by which a browser enters or leaves the matrix: the usage figure, the analytics source
           it is read from, who decides, and what happens in both directions.
     WHY   It gives a change to the list a stated reason. Each figure below is one team's choice for its
           own traffic. USWDS: "We officially support
           any browser above 2% usage as observed by" an analytics service. The ONS: "if your
           service’s analytics data shows at least 2% of your users are using a different browser or
           version, then you will need to test against that as well." GOV.UK does not state a floor. It
           states coverage: "The list in the table represents approximately 98% of the most popular
           browsers used on GOV.UK." Its change entries cite a percentile: "Removed requirement to test
           with Safari 11 and earlier versions, as they fall outside of the 95% most popular browsers."
           The GDS Way leaves the choice to the team: "You should use analytics data and user research to
           determine whether you should regularly test in any other browsers." Deque's 1% is a rule for
           assistive-technology combinations, "be used by more than 1% of users", not for browsers. These
           figures are not norms. Browserslist warns that a usage floor used alone "will in the long run
           make popular browsers even more popular", and offers a query over "statistics derived from your
           real-world traffic rather than global marketshare". The Service Manual points at the other end
           of the decision: "You also have to work out when to stop supporting a product or system if its
           popularity is declining." It is this library's position that a matrix should name its own
           analytics source beside any figure.
           Deep dive: platform-device-support-matrix_companion.md section 3 (Anatomy > Threshold Rule)
           and section 6 (Debates and contested boundaries).
     ASK   What usage figure brings a browser in, what takes one out, and what does the team do when one
           crosses the line in either direction? Which analytics source is it read from, and who reads it?
           Who decides? Why is this figure ours rather than someone else's?
     GOOD  "A browser enters the matrix when the library's own web analytics show it above 4 percent of
           sessions, and its row is demoted when it falls below 1 percent. Both figures are our own
           choice for our own traffic and are illustrative here. The web officer reads the analytics
           report and decides. The head of digital services is told of every demotion."
     WEAK  "We support any browser above 2%." (a figure borrowed from another team's rule, with no
           analytics source, no decider, and no word on what happens when a browser falls below it)
     TRAP  Presenting a borrowed figure as a standard, or writing only the entering side. A threshold with
           no named analytics source cannot be checked, and a rule that never says when a browser leaves
           lets the matrix grow without anyone deciding it should. -->

**Entry figure:** {{entry_threshold}}

**Exit rule:** {{exit_rule}}

**Analytics source, and who reads it:** {{analytics_source}}

**Who decides:** {{threshold_decider}}

**Why this figure is ours:** {{threshold_rationale}}

## Unsupported Browsers

<!-- WHAT  What a user on an unlisted or lowest-grade browser gets, and what a bug report from one is
           worth.
     WHY   The matrix lists what the team supports, so the people who are not on it need an answer too.
           The sources carry that answer under three names. The AusDTO UI-Kit has a section headed
           "Unsupported browsers" whose body says "Other combinations may be supported but have not been
           extensively tested". GOV.UK Frontend carries it as its lowest grade. Jenkins makes its lowest
           level the default: "This is the default unless a browser/version is listed". The GDS Way sets
           the posture for a report from outside the policy: "You may receive reported issues on browsers
           outside of your normal policy. You should still investigate these issues, assess their impact,
           and consider how to address them." It names grounds for declining a fix after that: "fixing the
           issue would require disproportionate engineering effort", "a feature of your service
           inherently relies on an unsupported feature", and "the browser in question cannot be supported
           without introducing serious security risks". GitHub asks a reporter of a pre-release bug to
           "please verify that it also exists in the stable version of the same browser". A fallback for
           the person on an unlisted browser can point at progressive enhancement, in the Service
           Manual's words: "Use progressive enhancement to give your service the best possible chance of
           working for the majority of your users." Reading a report from an unlisted browser as a gap in
           the matrix is this library's inference.
           Deep dive: platform-device-support-matrix_companion.md section 3 (Anatomy > Unsupported
           Browsers).
     ASK   What does a person on an unlisted browser get? What does the team do with a bug report from one:
           investigate, ask the reporter to reproduce it on a listed browser, decline? On what grounds may
           the team decline a fix? Could a support agent say the answer aloud?
     GOOD  "Anyone on a browser the matrix does not list still gets catalogue search and record pages,
           because the site is built to work without scripting. We read every report from an unlisted
           browser and try to reproduce it on a listed one first. We decline a fix when it would cost
           more than the problem is worth or when the browser cannot be supported safely, and the reply
           says which."
     WEAK  "Other browsers are not supported." (a decision with no answer for the person on one: it says
           nothing about what they get or whether their report is read)
     TRAP  Stopping at "not supported". The GDS Way's posture is to investigate a report from outside the
           policy and then decide. A flat refusal skips the investigation, and on this library's
           inference it also loses the sign that the matrix may have a gap. -->

**What a user gets:** {{unsupported_user_experience}}

**What happens to a bug report from one:** {{unsupported_bug_triage}}

**Grounds for declining a fix:** {{declining_grounds}}

## Ownership

<!-- WHAT  The named owner, who may change a grade or the threshold, and who is told when one changes.
     WHY   The standing-standards family asks every member to name who notices when the document goes
           wrong, and an unowned matrix has nobody to notice. The GDS Way page names its owner in its own
           text: "by the page owner #frontend". GitHub's browser-support library names a team that decides
           whether a polyfill can go. Jenkins records that each of its changes followed a mailing-list
           thread or a governance meeting, so its owner is a community process rather than a person. THE
           ROLE NAMES BELOW ARE THIS LIBRARY'S POSITION. No source read names a person or role who may
           change a grade. The GDS Way states that its content is intended for internal use by the GDS
           Digital Products community, so it is cited here as one government team's guidance, not as a
           standard.
           Deep dive: platform-device-support-matrix_companion.md section 3 (Anatomy > Ownership).
     ASK   Who owns this matrix, by role and by name? Who may change a grade or the threshold figure? Who
           must be told when one changes? Where does the discussion happen?
     GOOD  "Owner: the web officer, discussed in the #web-team channel, currently Dana Whitlow. A grade or
           the threshold figure changes only with the owner's agreement after a note in #web-team. The
           head of digital services and the front-desk lead are told of any change."
     WEAK  "The team owns it." (names no role, no person and no place where a change is discussed)
     TRAP  Naming a team and no person, or letting anyone edit a grade with nobody told. A matrix with no
           owner and no trigger is the ungated case the family contract describes. -->

**Owner (role and person):** {{owner_role_and_person}}

**Where changes are discussed:** {{change_channel}}

**May change a grade or the threshold:** {{who_may_change}}

**Told when a grade changes:** {{who_is_told}}

## Review Trigger

<!-- WHAT  A table of conditions, owners and actions: what event makes this matrix wrong, who notices, and
           what they do about it. The conditions are things an owner can observe, not dates, with the
           annual floor last.
     WHY   The standing-standards family requires every member to carry this mechanism. THE TABLE FORM IS
           THIS LIBRARY'S POSITION: the sources show the content in prose and in dated change histories.
           The conditions have these sources. A browser crosses the threshold: the Service Manual records
           "Updated the requirement to test in Safari for iOS from 9.3 to 10.3 to reflect usage
           statistics." A vendor ends support: USWDS records "the Design System no longer supports
           Internet Explorer 11", and Jenkins "2022-02-01 - Remove support for Internet Explorer, Add
           Edge". The sources record the drop, not the cause, so reading each drop as a vendor ending
           support is the library's inference. A new platform is adopted: this condition is the
           library's synthesis, and no source states it. A bug is triaged against an unlisted browser:
           the GDS Way describes the report, and reading it as a gap in the matrix is the library's
           inference. The annual floor: the Service Manual records "18 September 2024 List of browsers
           to test in updated. Commitment to update browser list updated to annual.", and the GDS Way
           page says "It needs to be reviewed again on 13 July 2027". The Service Manual's history also
           records reviews with no change, "Reviewed list of browsers to make sure it's still current,
           based on recent usage figures for GOV.UK. No change from the June 2020 version of the list.",
           and three of its changes cite usage. So the list changed when usage moved, and periodic
           reviews checked whether it had. Those review-only entries date from 2020 and 2021, before the
           annual commitment of 2024. That is high confidence for GOV.UK and says nothing about any
           other team. Reading the annual figure as a floor is the library's inference, at medium
           confidence. Telling users about a raised minimum belongs in the action column. MetaMask: "before bumping our minimum supported browser
           versions, we should always notify users in the application first." AMP requires "Allow at
           least 2 weeks of open discussion after the I2D is created before proceeding with the
           deprecation of the feature", for an audience of library developers. Cockpit asked for "a
           friendlier message that communicates that their browser does not work and message which
           browsers do work".
           Deep dive: platform-device-support-matrix_companion.md section 3 (Anatomy > Review Trigger).
     ASK   What could the owner observe that shows this matrix is wrong? Who notices each condition, by
           role? What do they do about it, and when a minimum is raised, who is told, how, and is the
           audience end users or developers? Who runs the annual floor?
     PRIORITY  List the event conditions first and the annual floor last. The floor is the longest the
           conditions can go unchecked, not a calendar rewrite of the document.
     ROW HINT  A good row states a condition the owner could observe, names a role as owner, and states an
           action, which for a raised minimum includes the notice to users. A weak row says "review
           regularly" and names no one.
     GOOD  | Analytics show Safari on iOS has fallen below the demotion figure | Web officer | Demote the
           row, record the analytics date and the reason in the review history, tell the head of digital
           services, and if a minimum is being raised, put a notice on the search page first that names
           the browsers that still work. |
     WEAK  | Review regularly | The team | Update the matrix. |
     TRAP  Naming one condition, usually the usage figure, and treating the annual review as the whole
           mechanism. That the conditions are several is this library's position. A related slip is a
           raised minimum with no notice action, which leaves that step to chance. -->

| Condition | Owner | What They Do About It |
|---|---|---|
| Analytics show a browser or version crossing the threshold, in either direction | {{crossing_owner}} | {{crossing_action}} |
| A browser vendor ends support for a version a row depends on | {{vendor_end_owner}} | {{vendor_end_action}} |
| The team adopts a platform this matrix does not yet cover | {{new_platform_owner}} | {{new_platform_action}} |
| A bug is triaged against a browser the matrix does not list | {{unlisted_bug_owner}} | {{unlisted_bug_action}} |
| The annual floor: at least once a year, whatever else has fired, the owner reconfirms every row | {{annual_floor_owner}} | {{annual_floor_action}} |

**Review history (one dated line each time a condition fired or the annual floor ran, with the
outcome, including "no change"):** {{review_history}}
