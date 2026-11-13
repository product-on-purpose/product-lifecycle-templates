---
title: "Harbourline Bookings Platform and Device Support Matrix"
doc_type: platform-device-support-matrix
size: lean
product_name: "Harbourline Bookings"
owner: "Imogen Falk (Web and Booking Lead)"
status: active
doc_version: "1.1.0"
created: "2026-04-20"
updated: "2026-10-06"
related_links: []
source_template: platform-device-support-matrix
source_template_version: 0.1.0
---

> **Worked example.** A filled `platform-device-support-matrix`, the one size this bundle ships, for
> Harbourline Bookings, the booking site of a small fictional passenger-ferry operator. It is not on
> the library's Acme Analytics thread. The `standing-standards` family contract weakens that
> chaining on purpose, because a standing standard belongs to a team rather than to a moment in a
> story (see [section 4 of the contract](../../docs/internal/contracts/standing-standards.md)). So
> the body below cites no sibling example. It is dated 2026-10-06, the day of the last line in its
> review history.
>
> Read it alongside
> [`platform-device-support-matrix_guide.md`](platform-device-support-matrix_guide.md), the rubric
> it was graded against. Four decisions are visible in it. One row promises more than the team
> tests. One row has been demoted. Two Review Trigger conditions have fired, so the table is shown
> working. The assistive-technology combinations are named by reference and held nowhere in the
> tables. The separate Grade and Tested columns, the Notes column, the role names and the table form
> of the Review Trigger are this library's own position, not received practice. Every figure, date
> and name below is illustrative, and the threshold figures are Harbourline's own choice for its own
> traffic, not norms for anyone else.

# Harbourline Bookings Platform and Device Support Matrix

## Purpose and Scope

**Product covered:** The public booking website, where visitors search ferry sailings, choose
foot-passenger or vehicle places, pay by card, and show an e-ticket at the quay. It does not cover
any native app, because Harbourline has none.

**Who relies on this matrix:** The contractor who runs the pre-release checks, the harbour office
supervisor who answers customer complaints, and the developer who decides what the seat map and the
delay ticker must run on.

**Where the record lives:** This file, in the booking site's repository. No tool holds a second
copy, so a disagreement between this file and anything else is settled in favour of this file.

**Audiences exempt, and the evidence:** None. The harbour office staff take phone bookings on the
same public pages that visitors use, on their own office PCs. A gap for a visitor is therefore also
a gap for the person helping that visitor by phone, and the staff have no separate tool that could
justify a lower promise.

**Assistive-technology combinations live at:** The accessibility test guide,
`docs/accessibility-test-guide.md` in the same repository. It lists the screen reader and browser
pairs the contractor runs. This matrix holds none of them.

## Support Grades

The grades run from the strongest promise to the weakest. In this document, "supported" means the
Supported grade and nothing wider. Testing is marked in its own column in The Matrix.

| Grade | What a user gets | What the team tests | What the team does about a bug |
|---|---|---|---|
| Supported | The whole booking path, including the animated seat map and the live delay ticker | The full path, run manually on a physical device or a current desktop install before every release, ending in a card-provider test payment | Fixed in the next release, and a bug that blocks a booking holds that release |
| Core | Sailing search, booking, payment and the e-ticket. The seat map may appear as a plain list and the delay ticker may be missing | The full path, run by hand only when the search, booking or payment pages change | Fixed when it stops a booking or a payment. Otherwise it waits behind bugs on Supported browsers |
| Not listed | Whatever the booking pages do without their enhancements, plus the harbour office booking line for help | Nothing, on any schedule | The report is read and reproduced on a listed browser first. A fix is declined only on the grounds written under Unsupported Browsers |

## The Matrix

**Effective from:** 2026-09-03, the date of the Review History line that last changed a row.

**Mobile browsers**

| Browser | Platforms | Minimum version or version rule | Grade | Tested | Notes |
|---|---|---|---|---|---|
| Safari | iPhone and iPad (iOS and iPadOS) | The current and the previous major release | Supported | Tested | One iPhone and one iPad live in the harbour office test drawer. Both run the full path before each release |
| Chrome | Android | The latest stable release and the one before it | Supported | Tested | Two Android handsets run the full path. One is a deliberately low-memory model, so the seat map is judged on a slow device |
| Samsung Internet | Android | The latest stable release | Supported | Untested | The promise is higher than the testing. The test drawer has no Samsung handset and the budget has no device-rental line. Rustam Beketov accepted this on 2026-04-20 until a handset is bought. A report from this browser is reproduced on Chrome first |
| Firefox | Android | The latest stable release | Core | Tested | Demoted from Supported on 2026-09-03. Its share of booking sessions was 1.2 percent in the July read and 1.1 percent in the August read, both under the exit figure. Checked by hand when search, booking or payment pages change. Last checked on 2026-09-17, after the payment page changed |

**Desktop browsers**

| Browser | Platforms | Minimum version or version rule | Grade | Tested | Notes |
|---|---|---|---|---|---|
| Chrome | Windows, macOS | The latest stable release and the one before it | Supported | Tested | Run on a Windows PC and the office MacBook before each release |
| Edge | Windows | The latest stable release and the one before it | Supported | Tested | Run on the harbour office PCs before each release. Staff use these same PCs to take phone bookings |
| Safari | macOS | The current and the previous major release | Core | Tested | Checked by hand on the office MacBook when search, booking or payment pages change |
| Firefox | Windows, macOS | The latest stable release | Core | Tested | Checked by hand when search, booking or payment pages change. Last checked on 2026-09-17, with the Android row |

## Threshold Rule

**Entry figure:** A browser and platform pair joins the matrix when it makes up at least 3 percent
of booking sessions over the last 90 days, and it joins as Supported. A pair between 1.5 and 3
percent joins at Core. These numbers are illustrative.

**Exit rule:** A Supported row falls to Core after two consecutive monthly reads below 1.5 percent.
A Core row leaves the matrix, and becomes Not listed, after two consecutive monthly reads below 0.5
percent. Both numbers are illustrative.

**Analytics source, and who reads it:** Harbourline's own booking-site analytics, in the report
named "Sessions by browser and platform". Imogen Falk reads it on the first working day of each
month and writes the read date beside any change.

**Who decides:** Entries and demotions are Imogen Falk's call, made from the monthly read. Rustam
Beketov, the operations director, is told of each one, because a change moves which handsets the
test drawer must cover.

**Why this figure is ours:** Most bookings come from phones, and a small visitor base lets one
browser carry a large share. The entry figure was set so that the test drawer, which holds four
handsets and tablets, can cover the Supported rows. Samsung Internet is the one row it does not
cover, which is why that row says Untested. Neither figure is taken from another team's rule, and a
figure that fits Harbourline's traffic may not fit anyone else's.

## Unsupported Browsers

**What a user gets:** The booking pages arrive as plain forms first and are enhanced afterwards. A
visitor on a browser outside the matrix can usually reach the booking form and the payment step. The
seat map and the delay ticker may not appear. If the form fails, the page shows the harbour office
booking line.

**What happens to a bug report from one:** Imogen Falk takes each report that names an unlisted
browser, gets its version from the visitor, and replays the steps on a listed browser. A problem
that reproduces there is fixed at that browser's grade. Whatever the replay shows, she then checks
the unlisted browser's share in the analytics report. If it sits under the entry figure, no row is
added, and the reply says so.

**Grounds for declining a fix:** The reply names which ground applied, by number.

1. The fix would change the payment step in a way that puts bookings from a Supported browser at
   risk.
2. The browser cannot open the secure payment form that Harbourline's card provider requires.
3. The problem appears only with an extension, a content blocker or a modified browser build that
   the reporter installed, and it goes away without it.

## Ownership

**Owner (role and person):** Web and Booking Lead, currently Imogen Falk.

**Where changes are discussed:** The `#booking-site` chat channel, and the fortnightly web stand-up.

**May change a grade or the threshold:** Imogen Falk may change a grade once she has posted the
analytics read behind it in `#booking-site`. Moving the entry figure or the exit figure needs
Rustam Beketov's sign-off, because it changes how many handsets the test drawer must cover.

**Told when a grade changes:** Rustam Beketov, operations director, and Mirela Dussault, harbour
office supervisor. Pavol Reiter, the contractor who runs the pre-release checks, is told so his
checklist matches the table.

## Review Trigger

| Condition | Owner | What They Do About It |
|---|---|---|
| Analytics show a browser or version crossing the threshold, in either direction | Web and Booking Lead | Applies the entry or exit rule and moves the row. Writes a review-history line giving the date of the read and the browser's share. Tells the operations director, the harbour office supervisor and Pavol Reiter, so his checklist changes with the row. If a minimum is being raised, adds a line to the booking confirmation e-mail and the e-ticket page at least four weeks before the raise takes effect, because visitors book weeks ahead and open the e-ticket on the day they sail |
| A browser vendor ends support for a version a row depends on | Web and Booking Lead | Raises the minimum on the affected row and records the vendor's date in the review history. Puts the same line in the confirmation e-mail and on the e-ticket page before the raise. Warns the harbour office supervisor, so staff can answer calls from visitors who see the notice |
| The team adopts a platform this matrix does not yet cover | Operations Director | Before launch, asks the Web and Booking Lead to add rows with a minimum version, or to record that the platform sits outside this matrix and say where its support is written down |
| A bug is triaged against a browser the matrix does not list | Web and Booking Lead | Follows the steps under Unsupported Browsers. Checks that browser's share in the analytics report. Adds a row if the share is above the entry figure. Otherwise records "no change" in the review history with the share found |
| The annual floor: at least once a year, whatever else has fired, the owner reconfirms every row | Web and Booking Lead | Reads the latest analytics report against every row, and asks Pavol Reiter to confirm each Tested value from what he runs. Records the result in the review history, including "no change" |

**Review history (one dated line each time a condition fired or the annual floor ran, with the
outcome, including "no change"):**

- **2026-04-20.** First version written from the March analytics read, with every row set on this
  date. Samsung Internet on Android was marked Supported and Untested, and Rustam Beketov accepted
  that until a handset is bought. Safari on macOS and Firefox on desktop entered at Core, from the
  band between 1.5 and 3 percent. No earlier history exists.
- **2026-09-03.** The condition "a browser crossing the threshold" fired. The read dated 2026-09-01
  showed Firefox on Android below 1.5 percent for the second month running. Imogen Falk demoted its
  row from Supported to Core. Rustam Beketov and Mirela Dussault were told in `#booking-site` the
  same day, and Pavol Reiter was told so his pre-release checklist dropped the Firefox on Android
  row. A demotion raises no minimum, so no notice for visitors was needed. The effective-from
  date above is this date.
- **2026-10-06.** The condition "a bug triaged against an unlisted browser" fired. A visitor on
  Vivaldi for Windows reported a seat map that stayed blank. Imogen Falk reproduced it on Chrome
  with a content-blocking extension installed, so the fault was in the seat map and not in the
  unlisted browser. The seat map will show its plain list when its script is blocked, in the next
  release. Ground 3 for declining a fix was not applied, because the seat map should fall back to
  its plain list whenever its script is blocked, which the Unsupported Browsers promise already
  covers. The analytics check ran, as it does whenever a report names an unlisted browser. It showed
  Vivaldi at 0.3 percent of booking sessions, under the entry figure, so no row was added. Outcome:
  no change to the matrix.
- **Annual floor.** Not yet run, because the matrix is under a year old. The floor does not restart
  when another condition fires, so the lines of 2026-09-03 and 2026-10-06 did not move it. It falls
  due on 2027-04-20, a year after the first version.
