# user-research-report: research log

Research conducted 2026-10-25, the day the maintainer set the terms rule. The research stage stored its pages
between 03:51 and 04:17 UTC on 2026-10-26, which the build notes date 2026-10-25 by local time
(`2026-10-25_urr-build-notes.md`). The quotation checks ran after that, and two pages re-stored during them carry
2026-10-27 UTC stamps. The research builds on the report's admission sweep of 2026-10-23, whose digest sits in a
gitignored folder under `_local/research/`. It builds on the plan's research log
(`templates/user-research-plan/user-research-plan_research-log.md`) and on ADR 0081 (adopt the research-docs
family contract). It builds on the family contract (`docs/internal/contracts/research-docs.md`) and on the
approved spec (`docs/internal/tier2-specs.md:6963-7425`). The maintainer's ten rulings of 2026-10-24
(`:7376-7393`) fix the ids, the sizes, the usability block, the pairing and the example. This bundle is the
report, catalog entry 18 (the user research report), tracked as issue #317 (bundle: user-research-report). The
plan, catalog entry 210, was built and merged on 2026-10-24 under issue #316 (bundle: user-research-plan).

The build ran seven dimensions, and one of them twice. Three read published reports: the formal reports of
government and standards bodies, vendors' section lists at two depths, and the evidence a finding carries. One
read practice and its debates, and one the gap question. One read the library's own neighbours and the Acme
Analytics chain, and it ran twice. The seventh, a gap-fill pass, read pages the others had referenced and not
read, on sites the terms rule allows. The working files are numbered by run. `dim1.md` holds government and
standards, `dim2.md` vendors and `dim3.md` evidence, counts and severity. `dim4.md` holds practice and `dim6.md`
the gap question. `dim5.md` and `dim7.md` hold the library chain's second and first passes, and `dim8.md` the
gap-fill pass. The headers inside the files carry other numbers (`dim7.md`'s says dimension 5), so go by file name.

**52 sources are recorded below, and all 52 are fetched-and-verified.** The maintainer read two of them by hand:
Mozilla's post [51] and Koji's page on how long findings stay valid [52]. By tier they are 22 vendor, 20
practitioner, 6 primary and 4 standards. The six primary sources are US government documents: NIST's NISTIR 7742
template [1], DHS's usability testing kit [3], digital.gov's starter kit [6], the Employee Express summary [7], and
usability.gov's template page [8] and template file [9]. The four standards sources are NIST's page on the Common
Industry Format [2], GOV.UK's two Service Manual pages [4], [49] and the GOV.UK Design System's community page [5].
Nielsen Norman Group's six pages [16] to [21] are tiered practitioner, as `order.json` sets; one dimension tagged
them primary. Five entries carry little. Moran's study guide [18] is a reading list and supports one line. Paul's
video page [21] supports its summary line only. The Design System page [5] is not a report template. Condens [15]
gives no section list. Dovetail's deprecation article [42] governs a repository and fails the one-study test.
**522 Quotable lines remain: 490 from the automated research and 32 from the two hand reads.** Quotable lines render the sources' long dashes as hyphens and keep their curly
apostrophes; copy them as they stand.

**Every quotation was checked against the source's raw text**, not against a retrieval tool's summary. Six
dimensions returned 381 quotations, which the recheck read as 52 entries (`recheck-report.txt`). By
`research.json`, government and standards returned 87, vendors 79 and evidence 69. Practice returned 53, the gap
question 24 and the gap-fill pass 69. The two library-chain files own no web source; they cite repository files
by line, and this log does the same. The recheck's own labels show 74 for vendors and 74 for the gap-fill pass.
It labels each URL by its last owner, and Condens [15] had two: five quotations from vendors and two from the
gap-fill pass. Go by `research.json`.

**The 52 entries are 51 distinct URLs and one duplicate.** Condens [15] is listed twice, once per owner. One of
the 51 is GOV.UK's terms page, which the gap-fill pass read to check the site's terms and quoted twice. The main
loop dropped it from the log, since it supports no claim about reports. `order.before-drop51.json` holds 51 URLs
and `order.json` holds 50. So 52, less the duplicate and the terms page, makes 50. Those 50 are entries [1] to
[50]. The recheck never saw the two hand-read entries, [51] and [52].

**The recheck recorded 312 strict passes, 10 passes as extraction artifacts and 59 failures.** By entry, the
failures are 10 from [1], 2 from [4], 1 from [5], 9 from [7], 13 from [9], 3 from [11], 1 from [12], 5 from [13],
9 from [14], 1 from [15] and 5 from [36]. All nine Employee Express failures [7] came from the stored copy, not
from the quotations. The recheck fetched the `.docx` over the network, and the stored copy became the file's zip
bytes in place of its text. The main loop then extracted the document's paragraph text and stored that. All nine
lines pass against it. The five Ethnio failures [36] joined each table row's label to its cells with the agent's
own markers. Ethnio's stored copy carries a stamp of 01:37 UTC on 2026-10-27, inside the recheck's own
hour, so the page was re-stored during or just after the recheck. Confidence: medium.

**A fresh fetch was tried for 222 quotations, from the URLs stored since 2026-10-26.** Those are the 34 sources
this build first stored, with 220 quotations, and GOV.UK's terms page, with 2. 192 passed. 26 failed: 25 from
usability.gov's page [8] and template file [9], and 1 from Condens [15]. The live usability.gov site now
redirects to digital.gov (`2026-10-25_urr-build-notes.md`), so a fresh fetch cannot reach either archived page.
Both rest on stored copies taken through the Wayback Machine. The Condens failure is its tailored-content line
[15], which also failed the strict test against the stored copy and stands on the generator's relaxed test
(below). Four came back empty, all from digital.gov's starter kit [6], whose
live page returns HTTP 404; it too was read through the Wayback Machine. The other 159 quotations, from 16
sources, were checked against the stored copies only in this build. Those are the 14 sources stored before this
run, and Employee Express [7] and Ethnio [36], which the recheck itself fetched.

**Fetch stamps.** The stored copies carry UTC stamps on five dates. One source was stored on 2026-10-17: GOV.UK's
sharing page [4]. Three were stored on 2026-10-23, the day of the admission sweeps: Maze [13], User Interviews
[14] and MeasuringU's test-plan article [22]. Ten were stored on 2026-10-24, during the plan's build: [1], [2],
[3], [5], [10], [11], [12], [19], [28] and [29]. Thirty-four were stored on 2026-10-26, by this build's research
stage. Two carry 2026-10-27 stamps from the recheck's hour: Employee Express [7] and Ethnio [36].

**The recheck counted 39 cache entries stored since 2026-10-26** (`new-cache.json`). 34 are this log's sources
with 2026-10-26 stamps. Three more are pages this build read and does not cite: two terms pages, Askable's
participant-facing one and GOV.UK's, and the Askable glossary page withdrawn below. The remaining two are pages from
jpattonassociates.com, stored at 01:14 UTC on 2026-10-27 by other work that shares the cache. No dimension cites
them. So 37 of the 39 carry 2026-10-26 stamps and 2 carry 2026-10-27 stamps.

**The failures were repaired in two steps, and then the generator re-tested everything.**

- **Splitting.** Most failures joined headings into one run with the agent's own separators, or ran a lead-in
  into its list. `gen_sources.py` split the 48 quotations that failed whole. 35 survived as 124 passing parts,
  and 13 were dropped whole. Two strict failures passed the generator's relaxed tests and stand as written:
  Condens's tailored-content line [15] and usability.gov's satisfaction footnote [9].
- **Re-quoting.** The main loop re-quoted 36 passages verbatim from the stored text of three entries: 19 from NIST
  [1], 9 from GOV.UK's sharing page [4] and 8 from Ethnio [36]. All 36 passed (`requotes-1.json`). Every one of
  the 13 drops came from those three entries: 6 from [1], 2 from [4] and 5 from [36].

The arithmetic is 381 returned, less the terms page's 2, which leaves 379. Adding the 36 re-quotes makes 415
tested. 367 passed whole: 355 strictly and 12 only under the generator's relaxed tests. The 355 are the recheck's
312 strict passes, less the terms page's 2, plus the 36 re-quotes and the 9 Employee Express lines. The 12 are the
recheck's 10 artifact passes and the two failures named above. 48 failed whole, and their 124 surviving parts
bring the total to 491. The generator merged one duplicate, UserTesting's Recommendations heading, which two of
its forms carry [11]. That leaves 490. `sources-report.txt` reports `split 48, dropped 13`. The split figure counts
every quotation that failed as a whole span, so it includes the 13 drops. The recheck's 59 failures are those 48,
the 9 Employee Express lines and the 2 relaxed passes. Every line in sources.md passed a check against the stored
raw body.

**The two hand reads add 32 Quotable lines, for 522.** The maintainer pasted each page's text into a gitignored
folder, as the terms rule's hand-read steps describe (`docs/internal/bundle-pipeline.md:179-191`). The copies
were saved on 2026-10-27, and that is the date the two entries carry. The main loop chose the quotations from
those copies and tested each one with the generator's own string test, against the copy alone. All 15 from
Mozilla [51] and all 17 from Koji [52] passed. Neither copy went into the source cache, so neither entry carries a
fetch stamp.

---

## What the checks caught, and what was not read

**The terms rule took effect the day this research ran, and the research stage ran twice because of it.** The
rule bars any automated read of a site whose terms of use forbid automated access, a read from the source cache
included (`docs/internal/bundle-pipeline.md:136-157`). The first pass stopped where agents read the new rule as a
ban on all automated retrieval. The second pass ran with the rule as written. The library-chain dimension ran in
both passes, though the resume should have replayed it, so `dim7.md` holds its first pass and `dim5.md` its
second. These pages and slips need a word here:

- **The Askable glossary page is withdrawn.** One agent read
  `https://www.askable.com/glossary/what-is-traceable-evidence` before it found Askable's general terms of use. It
  had first found a participant-facing terms page with no automated-access clause. The general terms forbid
  automated access, and Askable is now on the excluded list (`docs/internal/bundle-pipeline.md:173`). The page is
  no numbered source here, and no quotation or claim in this log rests on it (`withdrawn.json`).
- **Mozilla's post was read by hand.** The practice dimension wanted Mozilla's *Reflecting on 'It's Our Research'
  at Mozilla* (`https://blog.mozilla.org/ux/2019/12/reflecting-on-its-our-research-at-mozilla/`). The fetch
  returned a Cloudflare challenge page. That is a block, not a terms bar, and the rule allows no proxy past a
  block (`docs/internal/bundle-pipeline.md:155-157`). The maintainer read the post by hand, and it is [51]. The
  dimension wanted a practitioner's account of product managers and designers running their own research. The
  post does not give one. A product manager and two designers take part in field research and analysis that the
  team's user researcher led. The post gives the executive summary and the debrief instead (Findings 5, 6 and 12).
- **GitLab's handbook stays readable.** The build at first counted handbook.gitlab.com as excluded. A correction of
  2026-10-26 found a Creative Commons BY-SA 4.0 badge on every handbook and docs page. GitLab's website terms
  of use except content `permitted under applicable content licensing permissions` from their retrieval clause
  (`docs/internal/bundle-pipeline.md:150-152`), so the DRI page [28] stands as read from the cache. The maintainer
  also read it by hand on 2026-10-27, and that copy passes all seven of the entry's Quotable lines.
- **Mind the Product stays readable.** Pendo, which is on the excluded list, owns it. Its own terms carry no
  automated-access clause, and a site's own terms govern (`docs/internal/bundle-pipeline.md:152-153`). It is [34].
- **Sequencing slips.** The evidence dimension read cached pages from nngroup.com and measuringu.com before it
  checked those sites' terms (`dim3.md`; `docs/internal/bundle-pipeline.md:144-146`). Neither site bars reading,
  so nothing changed. `dim4.md` read GitLab's handbook [28] and Gilad's site [29] from the cache with no terms
  check of its own. The build's terms scout found no terms page on itamargilad.com
  (`2026-10-25_urr-build-notes.md`), and the GitLab correction cleared the handbook after the read.
- **One host has no recorded check.** No terms check is recorded for s3.amazonaws.com, which serves digital.gov's
  legacy Employee Express file [7]. The file is digital.gov's, and the terms scout found no clause on digital.gov.
  Confidence: medium.
- **Twelve pages on excluded sites were wanted and not read:** seven on koji.so, one each on entropik.io,
  getwhy.io and productplan.com, and two on Substack. The closing section, Pages not read under the terms rule,
  lists each one with what it would have supported. No claim in this log rests on them. The maintainer read a
  thirteenth by hand, Koji's page on how long findings stay valid, and it is [52].

**Four spans and two headings that the spec, the contract and ADR 0081 quote for the report are not Quotable
lines here.** This log matched every quoted span in the report's spec section, the contract and ADR 0081 against
the Quotable lines.
This build ran no carrying step, unlike the plan's, so spans the admission sweep checked were not carried in. The
spans below sit in this log's stored copies and survived as no Quotable line. A drafter may paraphrase each one
with the source number, and may not quote it from this log.

- NIST's `vendors demonstrate evidence of usability in their final product`, quoted at `research-docs.md:104-105`,
  at ADR 0081 `:72` and, as `final product`, at `tier2-specs.md:7189`. The stored copy of NISTIR 7742 holds it.
  NIST's Quotable sentence on summative studies carries the same point.
- Maze's `Research questions the report is hoping to answer`, quoted at `tier2-specs.md:7152` and
  `research-docs.md:28`.
- Maze's `an ongoing reference point`, quoted at `research-docs.md:17`.
- Nielsen Norman Group's sentence ending `consumed asynchronously`, quoted at `tier2-specs.md:7171-7172`.
- Two headings at `tier2-specs.md:7158`. NIST's `APPENDICES` sat in a dropped line, and only its six appendix
  titles survive. Maze's `Appendix` survives only in lower case, inside a sentence.

Three further spans belong to the plan's log, not this one: Maze's `Successful task completion` (`:7155`), from
Maze's usability-plan guide; Dovetail's `Findings stay traceable` line (`research-docs.md:27`), from Dovetail's
plan template; and the Design System's `going live` sentence (`research-docs.md:106-107`). The NSW span at `:7194`
is the plan's too. Every other external span the report's section quotes is a Quotable line, or part of one; the
rest are repository or catalog text.

**What the drops and splits lost.** The re-quotes recovered most of each dropped passage. These parts were not
recovered and may only be paraphrased, with the source number:

- **NIST [1]:** the sentence listing the template's five top-level sections, from executive summary to
  appendices. The third test goal, satisfaction measured through ease-of-use ratings. The verbalizations item in
  the list of data collected. The ISO number in the sentence on the expertise a reader needs. The narrative
  satisfaction and major-findings headings in the discussion. The pointer to the results table. The numbered
  appendices heading. The rest survives: the conformance sentence, five of the six data items, the first two
  goals and the six appendix titles.
- **usability.gov's template [9]:** the executive-summary instruction, which a split lost. It asked for when and
  where the test ran, its purpose, the number of participants and the session length. It also asked for an
  overview of results, a glimpse of ease of use and demographics, a bulleted list of problems, and a paragraph on
  what the document contains. Only the heading survives.
- **Ethnio [36]:** the row labels, which were purpose, design stage and outcome, and which column each cell
  belongs to. The eight re-quoted cells stand without labels. UserTesting's comparison [48] carries the two
  methods sentences with their labels, so a drafter who needs the pairing quotes [48].
- **GOV.UK [4]:** nothing. The nine re-quotes recovered both slide lists whole.

**Spans in stored copies that are not Quotable lines.** A search of the stored copies on 2026-10-26 found these
spans. They are real text on the pages and still may not be quoted:

- NIST's instruction to report testing irregularities that affected data collection or interpretation, which
  would support the spec's deviation line. Also NIST's de-identification line and its title-page requirement.
- usability.gov's placeholders for the report writer's name and the report date [9].
- Schade's warning that a finding phrased around users, with her example of three users who could not find
  something, seems to blame them [16]. It concerns phrasing, so this log cannot say Schade argues against counts.
- Schade's explanation that recommendations are meant to start the team thinking about design solutions, not to
  stand as the only or best one [16]. It would support Finding 4's line between a recommendation and a concept.
- User Interviews' remark that the research-goals section can reuse, by copying and pasting, what the plan
  already mapped out [14]. It would support the tie between the plan's questions and the report's.
- Usercall's advice to set a refresh cadence tied to business cycles [30]. Its example is a report refreshed each
  quarter, which is a standing report, not one study's.
- Sauro's reason for reporting positives: they keep the team from seeming the constant bearers of bad news [26].

**Spans the dimension files present that are not Quotable lines.** Drafters who read the dimension files will
meet these and must not quote them:

- `dim1.md` quotes NIST's title-page sentence and the EHR report's title, usability.gov's executive-summary
  instruction, and NIST's satisfaction goal and heading. It records the Wayback timestamps, which are retrieval
  facts, not quotations.
- `dim2.md` quotes Dovetail's heading on recommending rather than observing, and its line on AI citations. It
  quotes Maze's list of reader roles, its line on what the study originally hoped to answer, its appendix line on
  secondary research and a FAQ phrase. It quotes User Interviews' copy-and-paste line and its phrase on further
  research. It quotes Condens's heading-size line and its Interview Snapshot, credited to Teresa Torres.
- `dim3.md` quotes Schade's two user-focused lines and her word jumpstart, all in the stored copy and not
  Quotable. It quotes Sauro's phrase on utterances, actions and images, a line naming Abelson's law, the
  harbingers sentence and MeasuringU's sentence on the structure it usually uses.
- `dim4.md` quotes Usercall's refresh-cadence heading. Its phrase about a product already in use is its own
  reading; the stored copy does not contain it.
- `dim6.md` quotes Userfeel's phrase on order of priority and CleverX's fields for data retention expiry and an
  anonymised participant ID. It names GRADE-CERQual, which rates findings across a synthesis of many studies.
- `dim8.md` quotes Erin May's question on expiration and an O'Neill phrase on what is not the most important
  thing. It attributes Maze's evaluative epigraph to Mithila Fox and UserTesting's to Erika Hall. No Quotable line
  names either person.
- Three dimensions tag tiers differently from `order.json`. `dim3.md` tags NN/g primary, `dim1.md` tags Employee
  Express practitioner, and `dim8.md` tags GOV.UK's privacy page primary. This log follows `order.json`:
  practitioner, primary and standards.
- `dim8.md` notes that Maze's evaluative URL [47] now redirects to a guide chapter. The stored copy is the blog
  URL's, and the entry cites it.

**Where the dimensions contradict one another.**

- **The evidence dimension found no source on stating an unanswered question in a finished report.** O'Neill
  says "the next session needs to test these open questions" [46]. Userfeel asks for "further questions that arose
  from the test and how they could be investigated in the future" [38]. Dovetail's debrief template ends with
  "Open questions for the team" [44]. Other dimensions owned those sources.
- **The evidence dimension found no UX guide to stating limitations.** Dovetail's pre-read asks for "The method
  used and any important limitations" [43]. Userfeel says "Discuss any concerns you have about your methods"
  [38]. Sauro and Lewis name the limits of small samples [23], [24]. None is a section heading, so the narrow
  claim holds.
- **The gap dimension found no element comparing prior belief with finding.** Maze says "Remind your audience of
  'what we thought' vs. what you actually learned." [13]. User Interviews asks for "Your hypotheses and
  expectations prior to conducting the research." [14]. MeasuringU's Bayesian primer is built on "the prior
  hypothesis (before)" [50]. The gap-fill pass read the last one.
- **The gap dimension found no element crediting who analysed the data.** Sauro proposes "a section on the
  interviewer or principal investigator’s background and how it might influence their conclusions" [25]. GitLab
  names the DRI who synthesises and creates the report [28]. One source each, so the element stays thin.
- **The gap dimension found no per-finding confidence.** Sauro reports "confidence intervals around the issue and
  insight frequency" [25], and his small-sample article argues for intervals [24]. The Bayesian primer gives "A
  95% credible interval runs from roughly 72% to 96%" [50]. That is the quantitative half only. No source rates
  confidence in a qualitative finding within one study.
- **The vendors dimension found open questions only in Dovetail.** Dovetail's own debrief template [44] and
  O'Neill [46] carry them too.
- **The library-chain passes disagree.** The second pass (`dim5.md`) found no wording mismatch in the spec's
  binding facts. The first pass (`dim7.md`) found two. Both are real; the example note records them.
- **Government terms.** `dim1.md` says no terms check was needed for government sites. The build's terms scout
  checked nist.gov, dhs.gov, gov.uk, design-system.service.gov.uk, digital.gov and usability.gov, and found no
  clause (`2026-10-25_urr-build-notes.md`). The gap-fill pass read GOV.UK's terms page itself.
- **A count check of the Findings, 2026-10-27.** One sonnet agent read Findings 1 to 13 for unsourced counts,
  quantifiers, negative claims and attributions. It checked 29 claims and found two of Finding 2's tallies
  wrong or thin. Research questions as their own item fell from 3 to 2 of 14, because [43] is the fifteenth
  list. The method tally now names the reading it rests on. A recount in the main loop added the grounds for the
  recommendations tally. Finding 5's Mozilla attributions match the maintainer's hand copy [51].

**What was assigned and not read, or not usable:**

- **DHS's report template and its per-method downloads** [3]. `dim1.md` found no static download links on the
  page.
- **digital.gov's PowerPoint report template** [6], the kit's "Usability Report Template 1 (PowerPoint
  presentation, 373 KB, 8 slides, May 2014)" [6]. Not opened, so the deck's structure is unknown.
- **NIST's CIF overview PDF**, and ISO/IEC 25062 itself, which is a paid standard. Neither was read.
- **The origin of atomic research** by Tomer Sharon and Daniel Pidcock, which Maze credits [13]. Not fetched.
- **Medium's terms page**, which returned HTTP 403, so a uxdesign.cc article the gap dimension found was never
  fetched.
- **A filled report, end to end, from a product team.** The nearest are Employee Express [7] and usability.gov's
  sample figures [9], both from government.

---

## Findings

### 1. What a user research report is, and its two depths

**The definition is settled across sources.** User Interviews: "A research report is a document that summarizes
all the details of a research study, including the research questions, methodology, notable insights, and
recommended next steps." [14]. Maze: "A user research report is an easy-to-digest summary of a user research
project that aims to update product stakeholders on results, inform product decisions with user data, and
harmoniously guide a product build or iteration." [13]. Dovetail separates the report from its parts: "A report
packages several insights into a narrative for a specific audience, with method, context, and recommendations."
[10]. NIST's format is "a standard method for reporting usability test findings" [2]. Confidence: high.

**It reports one study, after the study ends.** User Interviews' definition names "a research study" [14]. Dovetail
builds every depth "from the same project-same findings, same citations, different depth" [10]. Its comparison of
synthesis methods says the output "is typically a report or presentation tied to a specific study" [45]. The
repository material [33], [42] fails the one-study test and stays out.

**Two depths are published, as two forms of one study's report.** This is where the report differs from the plan:
the plan's log found no source naming a short and a long form of one plan. Dovetail: "Executives want one page
with the decision; your product team wants the detail behind it." [10]. UserTesting names three forms: "Executive
summary report (For Stakeholders and Leadership)", "Detailed research report (For UX and Product teams)" and "Quick
feedback snapshot (For Agile teams)" [11]. Condens offers "concise summaries for executives who need quick
takeaways, and in-depth reports for product and design teams looking for detailed insights." [15]. Usercall's
author produces "a full report for the record, and a one-page brief or clip reel for the people who will never
open the PDF." [30]. User Interviews: "Creating both a detailed report and a presentation ensures that different
types of audiences can access and appreciate your findings in the future." [14]. Maze: "If you can tailor versions
of your report or provide key summaries for each collective, even better!" [13]. Confidence: high. The spec's
sizes call (`:7078`) holds.

**DHS scales the write-up to the kind of test.** For a quick office test: "Reporting - There's no need to
formalize your findings; just use your rough notes on usability issues to revise the materials or start
developing a prototype." [3]. In the field, "you can use your findings to compile a short report or simply use
your notes to iterate your design further." [3]. A full test "may or may not result in a formal report." [3], and
its reporting uses "the report template provided" [3].

**Two sizes, not three.** UserTesting's snapshot lists four items: "Study Goal", "Key Insights (Bullet Points)",
"Supporting Data (Screenshots, Videos, Metrics)" and "Next Steps & Prioritized Action Items" [11]. Each maps to a
lean section, as the spec says (`:7085-7087`). DHS's lightest level is no report at all [3]. The spec's medium
confidence on not three holds.

**Against length.** Dovetail: "As short as the decision allows." [10]. User Interviews: a report is not "A
lengthy, dissertation-style paper" [14]. On the CIF, it says "However, this format tends to be quite lengthy,
making it less-than-ideal for sharing with stakeholders." [14]. Maze's common mistakes include "focusing too much
on methodology, burying the main insights" [13].

### 2. Sections, list by list

Fourteen lists give a report's sections. Dovetail's debrief pre-read [43] gives a fifteenth, partial list.

| List | Form | Sections, in the list's order |
|---|---|---|
| NIST NISTIR 7742 [1] | Long, formal | "1 EXECUTIVE SUMMARY", "2 INTRODUCTION", "3 METHOD" with nine subsections, "4 RESULTS" with "4.1 DATA ANALYSIS AND REPORTING" and "4.2 DISCUSSION OF THE FINDINGS", then six appendices from "SAMPLE RECRUITING SCREENER" to "INCENTIVE RECEIPT AND ACKNOWLEDGMENT FORM" |
| NIST's CIF page [2] | The standard's outline | "Executive Summary, Introduction, Method, and Results" |
| usability.gov template [9] | Long | "Table of Contents", "Introduction", "Executive Summary", "Methodology" ("Sessions", "Participants", "Evaluation Tasks/Scenarios"), "Results" (task completion, ratings, time, errors, "Summary of Data"), "Recommendations", "Conclusion", attachments |
| Employee Express [7] | Short, filled | An executive summary, "Short Term Problems and Solutions", "Long Term Problems and Solutions", "Other Identified Problems:", "4. Who We Tested", "5. List of Tasks", "6. Learn More" |
| DHS kit [3] | Full test | "participant data, testing locations, material tested, findings, and recommendations" |
| GOV.UK [4] | Slide deck | "1 or 2 slides that outline the research you did", "5-10 slides that describe your findings", "1 or 2 slides that show what you’re doing next (if relevant)" |
| Dovetail [10] | One form, cut by audience | "a summary that states the answer up front, background and objectives (two or three sentences on why the study ran), method and participants, key findings, recommendations, and open questions" |
| UserTesting, executive [11] | Short | "Title", "Objective of the Study", "Key Takeaways (3-5 bullet points)", "Top 3-5 Findings (with short explanations and evidence)", "Recommendations", "Next Steps & Action Items" |
| UserTesting, detailed [11] | Long | "Introduction", "Background & Objectives", "Research Questions", "Methodology (e.g., unmoderated usability tests, surveys, etc.)", "Key Findings", "Pain Points & Opportunities", "Appendices" |
| UserTesting, snapshot [11] | Shortest | "Study Goal", "Key Insights (Bullet Points)", "Supporting Data (Screenshots, Videos, Metrics)", "Next Steps & Prioritized Action Items" |
| Maze [13] | One form | "Introduction", "Key findings", "Next steps", a Q&A, an appendix |
| User Interviews [14] | One form | "Introduction", "Research goals", "Business value", "Methodology", "Key learnings", "Recommendations" |
| MeasuringU [22] | Usability test | "Study Overview", "Findings Summary", "Participant Profiles & Demographic Summaries", "Task Metrics", "Usability Issues by Task and Recommendations", "Test Metric Summary", "Appendix & Verbatims" |
| Dovetail's debrief [44] | A debrief document | "Research objective", "Method and participants", "Executive summary", "Findings by theme (with evidence)", "Recommendations", "Open questions for the team" |

**What recurs across the fourteen lists.** These counts come from the table above and the entries behind it.

- **A summary: 8 of 14.** They are NIST [1], [2], usability.gov [9], Employee Express [7], Dovetail [10],
  UserTesting's executive form [11], MeasuringU [22] and Dovetail's debrief [44]. usability.gov puts its
  introduction before its summary [9].
- **An introduction, objective or study overview: 11 of 14.** All three UserTesting forms carry one [11]. Only
  DHS [3], GOV.UK's deck [4] and Employee Express [7] lack one.
- **Research questions as their own item: 2 of 14.** They are UserTesting's detailed form [11] and User
  Interviews' research-goals section [14]. Dovetail's debrief pre-read [43], the fifteenth list, names them too.
  No short report form carries them.
- **Method and participants: 12 of 14.** Only UserTesting's executive form and snapshot leave them out [11].
  Maze puts the method in a step after its introduction [13]. GOV.UK's "1 or 2 slides that outline the research
  you did" [4] counts as method on this log's reading.
- **Findings: all 14.**
- **Recommendations or next steps: 13 of 14.** Only NIST's CIF outline lists none [2]. NIST's template ends its
  discussion with "AREAS FOR IMPROVEMENT" [1]. UserTesting's detailed form counts through its "Potential
  solutions or design changes" [11].
- **Open questions: 2 lists**, Dovetail's two [10], [44], and guidance in three more [14], [38], [46].
- **An appendix or attachments: 6 lists** [1], [9], [10], [11], [13], [22]. None is a short form.
- **Task metrics: 3 lists**, all usability formats [1], [9], [22].
- **Items in one list only:** a conclusion [9], a Q&A [13], business value [14], and pain points and
  opportunities [11].

**The method section stays brief for most readers.** Maze: "Ultimately, while methodology is important, it's the
results that most people are here for." [13]. Its practitioner warns "As researchers, it's not uncommon to dwell
on the methodology for longer than needed." [13]. User Interviews asks only for "A brief explanation of why you
chose those methods." [14]. Usercall: "They lead with the decision, not the methodology." [30]. The CIF serves the
other reader, for whom "the CIF format works great" [14].

**The answer comes first.** Dovetail: "Put the headline finding in the first three sentences-don't make readers
excavate it" [10]. Maze: "Lead with a short summary of key findings and recommendations, then add the context
people need-such as why you conducted the study and the methods you used." [13]. O'Neill: "The other is a TLDR."
[46]. Confidence: high.

### 3. Evidence, counts and severity

**A finding carries a claim, its evidence and why it matters.** Dovetail: "Limit findings to three to five-each
one a claim, the evidence behind it, and why it matters." [10]. GOV.UK's findings slide has "a headline that
communicates something you’ve learned" and "1 or 2 sentences that describe the essential facts of the finding"
[4]. It adds "1 or 2 sentences that explain its importance and any consequences" [4]. NN/g's chain: "Data leads
to findings, which build insights, which justify recommendations." [20]. Paul: "findings capture patterns among
data points" [21]. Confidence: high.

**Evidence a reader can check.** Dovetail: "Every claim cites a quote, a clip, or a number a reader can check"
[10], and "A finding without evidence is an opinion with formatting." [10]. Usercall: "They tie every claim to
evidence the reader can verify in seconds, usually a quote or a clip, not a paraphrase buried in an appendix."
[30]. UserTesting: "Use direct quotes or clips to support findings" [11]. Krause cautions that "Anecdotes can lead
to narrative bias, so it’s best to use them to illustrate or support your data." [19]. Sauro: "Including
verbatims along with the interpretation also helps others see how the conclusions were drawn." [25].

**A finding names the design, specifically.** Schade: "Findings should explain the elements of the design that
confused users or led them down the wrong path." [16]. User Interviews gives an observation that users are
unhappy as its example of a finding too vague to act on [14].

**State counts, with the denominator.** Sauro: "We start with the most important findings, and then note the
number of participants that supported these findings and some good quotes to support what we concluded." [25].
Sauro and Lewis: "it’s completely permissible from a statistical perspective to report numbers when studies have
very small sample sizes (fewer than ten people)" [23]. They prefer fractions: "Unless this information appears
elsewhere in your report, we recommend presenting fractions." [23]. The reason is that "the denominator shows
whether the corresponding percentage was based on a small, medium, or large sample size" [23]. Their formats run
from "5 (simple count)" to "5/7 (71%) (fraction + percentage)" [23]. O'Neill adds the why: "making it a report
informative means not just saying the what" [46]. Confidence: high that counts belong; medium on the format,
since Sauro and Lewis give five.

**State the limits of a small sample.** Sauro: "the key limitation is that you are limited to detecting large
differences between designs or measures" [24], and "with five users attempting a task, the only possible outcomes
are 0%, 20%, 40%, 60%, 80% and 100% success" [24]. dscout: "We can’t distill preference with small sample sizes."
[27]. Sauro and Lewis: "Limits to generalization: You can’t manipulate all possible variables in a single
experiment." [23]. Dovetail's pre-read and Userfeel ask for limits beside the method [43], [38]. No list gives
limitations a heading of its own.

**Rate severity, for usability findings.** Nielsen's scale runs from "0 = I don’t agree that this is a usability
problem at all" to "4 = Usability catastrophe: imperative to fix this before product can be released" [17]. It
rests on frequency, impact and persistence [17]. Nielsen: "My experience indicates that severity ratings from a
single evaluator are too unreliable to be trusted." [17]. Sauro cut his scale to "just three levels, along with
one for insights, user suggestions or positive attributes" [26]. He also says "Treat frequency separately from
severity" [26]. usability.gov: "Each recommendation includes a severity rating." [9]. Schade ranks findings "as
low, medium or high severity" [16]. Confidence: high that usability reports rate severity; the scales are
contested.

**Say what works.** Schade: "Don’t forget to include positive findings as well, letting the team know what’s
already working." [16]. Sauro: "Don’t forget the positives" [26]. Userfeel: "although it can help to start with
a positive finding even if it's less important" [38].

### 4. Recommending without deciding

**Every list but one recommends** (Finding 2). NN/g: "Recommendations are the highest-value output in the research
process." [20]. User Interviews: "it's okay to offer your opinion after the research is done" [14]. Schade: "But
present recommendations as recommendations." [16]. User Intuition: "An insight without a recommendation is an
intellectual exercise. An insight with a recommendation is a decision input." [32]. Confidence: high.

**The sources pull the report toward the decision itself.** Usercall: "If your report doesn't end in a decision
or a debate about a decision, you haven't written a report, you've written a diary." [30]. Dovetail: "End each
finding with what the team should do about it, and who decides" [10]. Useberry: "Lead with decisions, then show
the evidence." [37], and "assign a name and date to each recommendation during the presentation" [37].
UserTesting's executive form ends in "Next Steps & Action Items" [11]. Dovetail tells trios to "Document the key
takeaways and decisions from every debrief" [43], though that is the debrief's record, not the report's.

**The contract's line holds as the library's boundary.** The contract says a member may recommend and records no
decision (`research-docs.md:47-48`). A report can name the decision its findings inform, and who makes it,
without recording the outcome. Usercall's debate about a decision [30] fits that reading. On this log's reading,
the template meets Dovetail [10] and Usercall [30] inside the contract this way. An ASK names the decision and
its owner, and a TRAP rules out the outcome. Confidence: medium. No source argues for keeping the decision out;
that is the contract's call.

**Solutions sit inside reports in several sources.** UserTesting's detailed form has "Potential solutions or
design changes" [11]. User Interviews asks for "Clear, specific solutions and next steps to solve pain points or
answer pending decisions." [14]. Employee Express pairs each problem with a solution under "Short Term Problems
and Solutions" [7]. Maze's deck framework ends in "Solution: Offer a route forward from the research findings and
insights, the next steps, and likely outcomes by solving the problem" [13]. The spec keeps a chosen concept out
(`:7167-7168`). A recommended change is not a chosen concept, but the line between them is the library's. The
guide should draw it: a recommendation names a change worth weighing, and the design brief names the concept
chosen. Confidence: medium.

**Who acts after the report.** GitLab: "It is expected that stakeholders and / or the Research DRI will follow up
the report by identifying and issuing actionable insights for the Product and Design team to action on." [28].
O'Neill says a report fails if readers "don't walk away with clear next steps to work with it" [46].

### 5. Practice: who writes it, who reads it, and whether teams write one at all

**Who writes it: a researcher, or whoever led the study.** GitLab: "In GitLab, anyone can be the DRI of a UX
Research project. If the Research DRI is not a UX Researcher, they are partnered with a UX Researcher acting in a
supporting role." [28]. "The Research DRI, and their UX Researcher partner if applicable, synthesise findings,
validate key takeaways, and create the report." [28]. "Other roles, such as Product Managers and Product
Designers, frequently conduct research with guidance from the UX Research team." [28]. User Interviews: "As the
researcher who led the project from start to finish, you're in the best position to interpret the data and make
recommendations for how it should be used." [14]. Humble wrote his own as a designer: "Ironically, I was a
designer doing research, and my research report was completely undesigned." [35]. Mind the Product writes for
product managers who "want to do user research themselves" [34], and does not discuss the report. Usercall
describes product managers running interviews with "No shared repository, no consistent screener, no synthesis
process." [31]. Mozilla's post shows a product manager and two designers taking part in field research and
analysis that the team's user researcher led [51]. It does not say who wrote the report. Confidence: high that
either a researcher or a product person writes it. The catalog's two
owner values (`tier2-specs.md:7324-7325`) gain a source: GitLab lets a product manager author the report [28].

**Who reads it: two audiences at least.** NIST: "The CIF targets two audiences: usability professionals and
stakeholders in an organization." [2]. UserTesting tailors depth to "executives, designers, product managers, etc."
[11]. Dovetail's debrief: "Write for the product managers, designers, and engineers who will use the findings."
[44]. User Interviews: "If it's only executives, you'll probably want to focus the report around strategy and
business application." [14]. Usercall: "They're scoped to one audience." [30].

**Whether anyone reads it.** Usercall: "Most customer research reports are built to prove that research
happened, not to actually change anything." [30]. Humble: "We do that because we know the truth… nobody reads. At
best, people skim" [35]. User Interviews: "However, many researchers complain that stakeholders don't read them or
are overwhelmed by the sheer volume of information." [14]. O'Neill: "If you write a report that people don't want
to read and don't read, it doesn't have any impact, even if it had the best possible insights in it." [46].
Usercall puts the cause in timing: "It still got shelved because it landed two weeks after the pricing decision
was finalized. The insight wasn't wrong, it was just late." [30]. Firefox's VP of Product puts the risk on the
summary: "In short, without a good executive summary, the document will likely not get the attention it
deserves." [51]. This is practitioner testimony. Confidence:
medium that it describes practice widely.

**Whether to write one at all.** GOV.UK: "researchers on an agile team won't have time to write research reports
(though they might produce brief research summaries)" [4]. Humble: "if you're bringing the team into research
activities, you don't have to make a research report ever again." [35]. Dovetail's trios article: "reports are
artifacts. Understanding is the actual output, and understanding is built through conversation, not
consumption." [43]. The same article says "Research that never leaves the researcher's head is research that
never happened." [43]. Dovetail's debrief article: "Async debriefs are not a blanket replacement for all live
conversation about research." [44]. Usercall argues that reports mostly fail and still keeps "a full report for
the record" [30]. User Interviews: "some researchers always create them for the research repository" [14].
Confidence: high that practice disagrees. The bundle must not claim that every study ends in a report.

### 6. Formats: written report, deck, debrief and repository

**The format is open.** GitLab: "Though Google Slides is the most popular format, the report can really be in any
form, for example, a doc, an issue, a board, or an diagram." [28]. Maze lists "5. Written reports: For direct and
simple sharing" [13] and "4. Presentations / slide decks: Great for the PAS framework" [13]. Of written reports,
Maze says "These types of reports often come as a PDF or a Word document, making them static, reluctant to
change, and resulting in low engagement or re-reads." [13]. Then: "Written UX reports enable people to go through
things in their own time-and come back to them when they need to." [13]. EnjoyHQ: "Instead of a slide deck, this
is your way to tell a compelling story" [12]. digital.gov's kit pairs a PowerPoint template with a "Usability
Report Template 2 (Word document, 20 KB, 6 pages, May 2014)" [6]. The PowerPoint was not opened.

**Does a deck have its own structure? Two sources bear on it.** GOV.UK's deck [4] maps onto the written sections:
what the team did, the findings, and what it does next. Maze's PAS framework does not. It runs "Problem: State the
problem you set out to overcome" [13], then "Agitate: Detail the impact or opportunity missed by not meeting the
problem" [13], then a solution [13]. That is a deck with a structure distinct from the written sections. It
weakens the spec's sentence that no source shows one (`tier2-specs.md:7171-7173`). The spec's recommendation can
still hold. PAS opens on a problem and closes on a solution, which edges toward the framed problem and the chosen
concept the spec keeps out (`:7167-7168`). On this log's reading, the guide may say a deck can carry the same
sections, and should name PAS as a presenting frame the library does not adopt. Confidence: medium.

**Debriefs and repositories sit beside the report.** Dovetail: "A debrief is not a research report for peer
review." [44]. It also says "In these cases, the async debrief still serves as the foundation." [44]. Its trios
article prefers a regular session to "a quarterly research readout" [43]. Mozilla separates a debrief from
analysis: "Notably, debriefs are not analysis. They may start the analysis juices going, but analysis is much more
in-depth and complex." [51]. Atomic research breaks findings into
nuggets: "A nugget is a labelled observation supported by evidence." [33]. UserTesting [11] and Maze [13] describe
the same unit differently. Usercall's operations article warns that "Insights get reported once in a deck and then
never referenced again" [31]. User Intuition wants each report to "reference prior findings - confirming,
contradicting, or extending what the organization learned previously" [32]. Only Humble argues for dropping the
report [35]. The others put the debrief or the repository beside it. The spec's boundary list names no debrief
(`:7179-7206`), and the companion's Relationships section should. Confidence: medium.

### 7. The usability block: Task Results

**The content is well sourced.** NIST: "The total number of successes were calculated for each task and then
divided by the total number of times that task was attempted." [1]. Path deviation: "The number of steps in the
observed path is divided by the number of optimal steps to provide a ratio of path deviation." [1]. Time: "Average
time per task was calculated for each task. Variance measures (standard deviation and standard error) were also
calculated." [1]. usability.gov: "The task success rate is the number of successes divided by the number of
participants completing the task." [9]. Its errors: "A non-critical error is an error that does not prevent
successful completion of the scenario." [9]. Its times: "Provide the range of completion times." [9]. MeasuringU
gives "Task Metrics" and "Test Metric Summary" their own items [22]. UserTesting asks for "success rates, charts,
QX Score visualizations" [11]. Confidence: high on content.

**Questionnaire scores come with thresholds.** NIST: "Broadly interpreted, scores under 60 represent systems with
poor usability; scores over 80 would be considered above average." [1]. And "Common convention is that average
ratings for systems judged easy to use should be 3.3 or above." [1]. usability.gov's sample reports "Mean
agreement rating = 4.7" [9]. A drafter cites these as NIST's conventions within the template's health-records
scope, not as the library's thresholds.

**Results are read against the goals.** NIST: "The results should be seen in light of the objectives and goals
outlined in Section 3.2 Study Design." [1]. And "The data should yield actionable results that, if corrected,
yield material, positive impact on user performance." [1]. That supports tying Task Results to the plan's Tasks
and Measures.

**Formative or summative: NIST's two pages disagree.** The template: "The modifications here allow for the
reporting of qualitative findings (i.e., formative) but strongly recommend and encourage the collection of
quantitative measures of user performance." [1]. The CIF page: "The CIF is designed for summative testing rather
than formative testing." [2]. The GOOD text for Task Results should show a small qualitative test reported in
fractions [23], not a summative table alone. Confidence: medium.

**One conditional section is the library's arrangement.** Three lists carry task metrics as their own sections,
all of them usability formats [1], [9], [22]. No general list does. The spec's medium confidence (`:7155`) splits:
content rises to high, and placement holds at medium.

### 8. The software-audience check (ADR 0080)

ADR 0080 (admission gains a software-audience check) asks for one named source. That source must show a software
product, UX or technology team writing or using the document
(`docs/internal/decisions/0080-admission-gains-a-software-audience-check.md:125-126`). **The type passes by name,
on several teams' own practice.** Confidence: high.

- **GitLab's UX Research team** runs the report process for a software company's product teams, and "The final
  report is shared in the ux_research_reports channel" [28].
- **UserTesting** writes its detailed report "For UX and Product teams" [11].
- **NIST's CIF** exists so stakeholders can decide on "the release of software products or the procurement of
  such products" [2].
- **Vendors writing for product teams**: Dovetail's "product team wants the detail behind it" [10], Condens's
  "in-depth reports for product and design teams" [15], and Maze's report that will "update product stakeholders
  on results" [13].
- **Practitioners describing their own reports**: Usercall's author [30], Humble [35] and O'Neill [46].

The name-versus-job question in ADR 0080 (`0080-...:134-145`) does not arise, because the name matches.

### 9. Lineage: what the report borrows from government and from the CIF

Contract section 3.6 (citations, with the family's lineage trap) requires a member that borrows a structure from a
government form or from ISO/IEC 25062 to say so (`research-docs.md:131-136`). **This report borrows section
structure from US government templates and from the Common Industry Format.**

- **NIST's NISTIR 7742** (US) customizes the CIF for health records: "This version of the CIF has been customized
  for use in usability testing of Electronic Health Records (EHRs) by usability administrator(s) and data
  logger(s)." [1]. It is "Version 0.2", dated "15-Nov-10" [1]. The spec's risk 5 requires that sentence beside any
  NIST heading (`tier2-specs.md:7340-7341`).
- **NIST's CIF page** dates the standard: "The American National Standards Institute (ANSI) approved the CIF
  December 12, 2001 as the standard for reporting usability test results." [2]. Its purpose is "to encourage
  incorporation of usability as an element in decision making for software procurement" [2]. The page says "This
  page is no longer being updated and the information may be out of date." [2].
- **usability.gov's template** [8], [9] and **digital.gov's kit** [6], [7] (US, GSA), both retired. usability.gov:
  "Usability.gov is archived and no longer updated." [8]. digital.gov's templates date from "May 2014" [6], and the
  Employee Express test from "July 22, 2013" [7]. [6], [8] and [9] were read through the Wayback Machine.
  `dim1.md` records snapshots of 2024-02-21 for usability.gov and 2026-04-17 for digital.gov.
- **DHS's kit** (US), "Last Updated: 02/27/2025" [3]. Its report template was not opened.
- **GOV.UK** (UK): the sharing page, "Published: 24 May 2016" [4], the privacy page [49] and the Design System's
  community template [5].

**Is NISTIR 7742 a regulatory format?** The spec calls it `that regulatory format` (`:7029`), and the contract
speaks of a regulatory reporting format (`research-docs.md:135-136`). No Quotable line in this log says a
regulator requires it. NIST describes an ANSI standard for software procurement [2] and a template "customized
for use in usability testing of Electronic Health Records" [1]. The lineage trap still holds: a reader should not
take a health-records template for general product practice. But the word regulatory has no support in this log.
Confidence: medium, because this log did not read the certification programme the template may have served.

**Only User Interviews among the vendors mentions the CIF**, and it treats it as a format for researchers: "If
your audience is other researchers... then the CIF format works great" [14]. No vendor list traces its sections
to the CIF. This log did not trace whether usability.gov's template derives from it.

### 10. The shipped-product clause

The friction study studies a dashboard customers already use (`tier2-specs.md:7267-7269`). Contract section 2
requires a member that serves such a study to declare `discover` anyway, with its companion saying why
(`research-docs.md:107-109`). The plan's example gives its reason in its first section
(`templates/user-research-plan/user-research-plan_example.md:44-47`). What this research gives the report's
companion:

- **The sources sort research by purpose and by object, and the friction study splits them.** Maze: "Evaluative
  research assesses and validates existing designs for improvements" [47], and "Generative research helps
  identify user needs and opportunities before design begins" [47]. UserTesting: "Generative research dives into
  'What problem might we solve?' while evaluative research asks, 'How well is our solution working?'" [48]. The
  friction study asks where analysts lose time, which is the generative question. Its object is an existing
  design, which is the evaluative object. Its method is interviews, and UserTesting ties generative work to
  qualitative methods: "Generative research: Typically uses qualitative methods to understand user needs and
  motivations to inspire design and product development innovation." [48].
- **The companion's reason.** The report finds an opportunity in a shipped product and grades no design against a
  target. On this log's reading, that is the companion's best reason, and it matches the plan's. Confidence:
  medium, because the clause remains the library's POSITION (`research-docs.md:107-109`).
- **What the companion must not say:** that any source calls a study of a shipped product discovery work. None
  does. Nor may it quote NIST's final-product phrase from this log (the checks above).

### 11. The gap question: candidates, routed under decision procedure 12

The gap dimension and the gap-fill pass return **candidates, never obligations**. Each is routed under decision
procedure 12 (a property or section proposed for a template) (`docs/internal/decision-procedures.md:207-254`). E1
means a named source publishes documents of this type carrying the element. E2 means the library argues it in
its own voice with a falsifier. E3 names its home, and E4 fits it to lean or to full. A quality property stops at
step 1 and becomes a guide rubric row. **This log admits no element and proposes no section.**

**Weigh the gap dimension's sources honestly.** Four of its five are vendor blogs: Useberry [37], Userfeel [38] and
CleverX's two pages [39], [40]. Where a candidate also has a GOV.UK, NN/g or MeasuringU source, that source
carries it.

1. **The decision the findings inform, and who makes it. Supported.** E1: "End each finding with what the team
   should do about it, and who decides" [10]; "which decisions they own" [37]; "Would this report change a
   decision?" [32]; "How do your findings influence the decisions you mapped out in your research plan?" [14];
   and Usercall [30]. **Route:** an ASK in Summary that names the decision the plan named and who makes it. A
   TRAP rules out recording the outcome (`research-docs.md:47-48`). Plus a rubric row. In full, Background and
   Objectives restates the decision.
2. **What the team believed before, against what it found. Supported.** E1: "Remind your audience of 'what we
   thought' vs. what you actually learned." [13]; "Your hypotheses and expectations prior to conducting the
   research." [14]; "Our original belief is called the prior hypothesis (before)." [50]. **Route:** an ASK in
   Research Questions and Answers, on whether each answer confirms the plan's hypothesis. The friction study's
   plan states one (`user-research-plan_example.md:66-69`). No column.
3. **Questions the study could not answer, and split results. Supported.** E1: "the next session needs to test
   these open questions" [46]; "further questions that arose from the test and how they could be investigated
   in the future" [38]; "Open questions for the team" [44]; "Suggestions for future research studies, if
   applicable." [14]; "we need to let our teams know when a question is unanswerable" [27]. Useberry asks, in the
   agreement before the study, for "a line on what happens if findings split or are inconclusive" [37].
   **Route:** Open Questions (full) holds it. In lean, the spec's Research Questions and Answers row already says
   that a question the study could not answer says so (`tier2-specs.md:7152`). An ASK there covers split results.
4. **Positive findings. Supported.** E1: [16], [26], [38]. **Route:** an ASK in Key Findings, and a rubric row.
   Not a section.
5. **Counts with their denominator, and the sample's limits. Supported.** E1: [25], [23], [24], [46]. **Route:**
   Key Findings already carries how many participants showed each finding (`:7154`), and an ASK asks for the
   fraction. The limits go in What We Did, which already names them (`:7153`). A TRAP names a percentage from
   twelve people without its fraction [23].
6. **Severity, for usability findings. Supported; the scales are contested.** E1: [16], [17], [26], [9].
   **Route:** an ASK in Task Results, the conditional section. Not a field for an interview study.
7. **Quotations anonymised, and used within consent. Supported.** E1: GOV.UK: "Whenever you can, you should fully
   anonymise the extracts you use so that the participants cannot be identified." [49]. CleverX: "I consent to
   anonymized quotes being used in internal reports" [40], and "If you want to use a specific quote or clip, get
   explicit permission referencing the exact content" [40]. Digital Government Hub: consent applies "as soon as
   you transcribe quotes from that call or share that person's information with other people on your team" [41].
   **Route:** an ASK in Key Findings on whether each quotation is anonymised and covered by consent. A TRAP names
   a participant. The plan's consent statement governs (`user-research-plan_example.md:159-171`).
8. **Where the raw data lives, and for how long. Supported; already homed.** E1: GOV.UK: "Keep your research data
   only in places that your organisation has approved for storing personal data." [49], and "We suggest 2 or 3
   years as reasonable retention periods for user research data - but delete it sooner if it's no longer needed."
   [49]. **Route:** the Appendix (full) already says where the raw notes live (`:7158`). The retention period
   belongs to the organisation's policy, as in the plan. CleverX's periods are a repository's [39], so the report
   states no period of its own.
9. **Author, dates and contact. Supported.** E1: "People need to put the dates, their names and contact
   information and what the study concerned." [46]; "When did the research take place? This helps readers assess
   how current the findings are." [44]. **Route:** frontmatter for author and date, and the dates in What We Did
   (`:7153`).
10. **Who ran and analysed the sessions. Thin.** E1: Sauro's interviewer-background section [25], and GitLab's DRI
    [28]. Dovetail's "Document your reasoning." [45] concerns working notes, not the deliverable. **Route:** an ASK
    in What We Did on who ran and analysed the sessions. No section.
11. **Confidence in each finding. Supported for counts only.** E1: Sauro's "confidence intervals around the issue
    and insight frequency" [25]; [24]; [50]. **Route:** guidance in Task Results for a quantitative usability
    test. For an interview study, the fraction and the sample's limits carry it [23], [27]. No confidence field.
12. **Related prior research. Thin.** E1: User Intuition's line on referencing prior findings [32], and User
    Interviews' "Links to more resources, including full session recordings, transcripts, notes, or other data."
    [14]. **Route:** an ASK in Background and Objectives (full), linking the plan and any earlier report. The plan
    already lists earlier reports (`user-research-plan_example.md:191-192`).
13. **Participants' own suggestions. Supported.** E1: "Any specific recommendations brought up by users during
    interviews or in surveys." [14]; "4.6.2 Likes, Dislikes, Participant Recommendations" [9]; Sauro's
    "Insight/Suggestion/Positive" level [26]. **Route:** an ASK in Key Findings, labelled as participants' words,
    not the team's recommendation.
14. **A recommendation after each finding, or all at the end. Contested.** Per finding, Condens: "Rather than
    listing them all at the end, include a recommendation after each finding throughout the report, while still
    including the summary at the conclusion." [15]; Dovetail [10]. By task, MeasuringU: "Usability Issues by Task
    and Recommendations" [22]. At the end: [9], [11], [14]. **Route:** the spec's separate Recommendations
    section stays, each recommendation tied to findings (`:7156`). The guide states both practices.
15. **Offhand comments. Thin.** E1: Maze: "make special notes of 'offhand' comments users make" [13]. **Route:**
    an ASK in Key Findings. One source.
16. **Peer review before the report goes out. Thin; fails E3 for one study's document.** E1: GitLab: "It should be
    put through a peer review process in the ux_research_team_lounge channel." [28]. **Route:** out of the
    template; a guide line at most. Dovetail's debrief contrasts itself with "a research report for peer review"
    [44].
17. **A date after which the findings should be checked again. Out; the product version tested is thin.**
    Dovetail's deprecation policy [42] governs a repository, and fails the one-study test. Koji's page [52], read
    by hand, is written for a repository too. Its half-life table cites no study, and it credits its one-year and
    five-year review points to an unnamed practitioner heuristic. Two of its
    tags belong to each insight at publication. E1: "Collected on: the fieldwork date, not the publication date"
    and "Product version / state: what the participants were actually reacting to" [52]. Of usability findings,
    it says "a redesign invalidates them instantly" [52]. **Route:** a review-by date stays out. The fieldwork
    dates already sit in What We Did (`tier2-specs.md:7153`). The product version tested could enter there as an
    ASK, on one vendor source. GetWhy's pages on the question were not read, and are listed in the closing
    section.
18. **The coding or analysis method. Unsupported.** No Quotable line asks a report to name one. **Route:** out.

### 12. The nine proposed sections, against this research

The spec's section table (`docs/internal/tier2-specs.md:7148-7158`) is headed as proposed, for the build's
research to test (`:7146`). The maintainer's rulings of 2026-10-24 close the spec's section (`:6979-6980`), so its
sections and sizes bind. The table records which sources now support each section and whether confidence moves.
**Every movement is a candidate for the maintainer; none is applied here.**

| Section | Size | Spec | Support in this log | Movement |
|---|---|---|---|---|
| **Summary** | both | High | [10] "a summary that states the answer up front"; [1] "1 EXECUTIVE SUMMARY"; [11] "Key Takeaways (3-5 bullet points)"; [44] "Executive summary"; [22] "Findings Summary"; [46] "The other is a TLDR."; [51] "An executive summary is a few sentences, maybe one slide" and "clear takeaways and calls to action for each report" | **Holds at high.** All three of the spec's spans are Quotable lines. Gap candidate 1 enters as an ASK |
| **Background and Objectives** | full | High | [10] "background and objectives (two or three sentences on why the study ran)"; [11] "Background & Objectives"; [13] "Your introduction should lay out your research goals, plan, and scope."; short forms: [11] "Objective of the Study" and "Study Goal"; [44] "Research objective" | **Holds at high on the element; full-only placement weakens.** Every short form with an objective line puts it near the top. That argues for a lean ASK in Summary naming the objective. Gap candidate 12 enters as an ASK |
| **Research Questions and Answers** | both | Medium-high | [11] "Research Questions"; [14] "Actionable reports should relate back to the initial research question" and "The research questions you'd asked as the catalyst for your study."; [43] "The research questions the study aimed to answer"; [22] "If possible, try to outline how the report will be structured in the test plan." | **Holds at medium-high, with lean placement a POSITION.** Maze's span is not a Quotable line here. No short report form carries research questions. Gap candidates 2 and 3 enter as ASKs |
| **What We Did** | both | High; medium on the deviation line | [10] "method and participants"; [1] "3 METHOD" and "3.1 PARTICIPANTS"; [11] "Methodology (e.g., unmoderated usability tests, surveys, etc.)"; [44] "Method and participants"; limits: [43] "The method used and any important limitations", [38] "Discuss any concerns you have about your methods", [24] | **Holds at high.** The limits clause gains three sources. The deviation line stays a POSITION: NIST's instruction on irregularities sits in its stored copy and is not a Quotable line. Gap candidates 9 and 10 enter as ASKs |
| **Key Findings** | both | High | [10] "key findings", "A one-page summary with linked evidence beats a forty-slide deck nobody opens." and "Limit findings to three to five-each one a claim, the evidence behind it, and why it matters."; [13] "Key findings"; [14] "Key learnings"; [11] "Use direct quotes or clips to support findings"; counts: [25], [23]; [4] the findings slide | **Holds at high.** The count clause gains Sauro and Sauro and Lewis. Gap candidates 4, 5, 7, 13 and 15 enter as ASKs |
| **Task Results** *(usability tests only)* | both | Medium | [1] "3.9 USABILITY METRICS", "4 RESULTS" and its measures; [9] "Task Completion Success Rate", "Time on Task", "Errors"; [22] "Task Metrics"; [11] "Include quantitative data where applicable (e.g., success rates, charts, QX Score visualizations)" | **Content up to high; placement holds at medium.** Maze's plan-side span lives in the plan's log. Gap candidates 6 and 11 enter as guidance |
| **Recommendations** | both | High | [10] "recommendations"; [14] "Recommendations"; [11] "Prioritized based on impact"; [13] "Next steps"; [9] "Each recommendation includes a severity rating."; [16] "But present recommendations as recommendations." | **Holds at high.** Placement beside the findings is contested (gap candidate 14). The no-decision clause is the library's line, against [30] and [37] (Finding 4) |
| **Open Questions** | full | Medium | [10] "open questions"; [44] "Open questions for the team"; [46]; [38]; [14] "Compelling insights that illuminate unanswered questions"; [27] | **Up to medium-high.** A second list carries it, and that list is Dovetail's lighter debrief [44]. That argues for lean placement, against the spec's full. Confidence: medium. The route is a lean ASK in Research Questions and Answers, not a move |
| **Appendix** | full | High | [11] "Full responses, session details, additional data"; [22] "Appendix & Verbatims"; [10] "Everything else, including discussion guides and full transcripts, belongs in an appendix or a link."; [1] six appendix titles; [9] attachments; [13] the appendix sentence | **Holds at high.** No short form carries an appendix, which supports full-only. NIST's and Maze's headings are not Quotable lines; their content is |

**Three findings bear on the section set without overturning it.**

- **The objective line sits in every short form that has one** [11], [44]. Background and Objectives can stay
  full-only if lean's Summary asks for the objective and the decision. Confidence: medium.
- **Open Questions sits in Dovetail's lighter document** [44]. A lean ASK in Research Questions and Answers
  carries it without a new lean section. Confidence: medium.
- **Research Questions and Answers in lean is the library's POSITION.** No short report form carries research
  questions (Finding 2). It rests on the contract's tie between plan and report (`research-docs.md:23-24`).

**Nothing argues for a new section.** Every candidate that clears E1 already has a home in the nine. The rest fail
E3, are quality properties, or are unsupported.

### 13. Spec sentences this research tests

These are candidates for a dated note in the spec, not a silent rewrite. Each is maintainer-vetoable.

**Weakened:**

- `:7029` and `research-docs.md:135-136`, the word regulatory for NIST's format. No Quotable line supports it
  (Finding 9).
- `:7151`, Background and Objectives as full only. Every short form with an objective line puts it near the top
  (Finding 12).
- `:7152`, Maze's span on research questions, which sits in the stored copy and is not a Quotable line. The row
  holds on UserTesting [11] and User Interviews [14].
- `:7158`, NIST's and Maze's appendix headings, lost in a drop or present only in lower case.
- `:7171-7173`, the deck exclusion. NN/g's span is not a Quotable line here, and Maze's PAS framework gives a deck
  its own structure [13]. The no-format recommendation can stand on other grounds (Finding 6).
- `:7175-7177`, which paraphrases GOV.UK as saying agile teams `often skip a formal report`. GOV.UK says that
  agile researchers "won't have time to write research reports" [4], and allows brief summaries. The spec's word
  often is softer than the source, and it drops the qualifier.
- `:7189-7190`, `research-docs.md:104-105` and ADR 0081 `:72`, NIST's final-product span, which is not a Quotable
  line. The QA edge holds on NIST's summative lines [1], [2].
- `:7179-7206`, the boundary list, which names no debrief. Two Dovetail articles distinguish one from a report
  [43], [44]. Mozilla separates a debrief from analysis [51].
- `:7219` and `:7221`, the binding facts' wording against the epic. See the example note.
- `:7089-7090` beside the plan's own promise. The plan promises a short written readout
  (`user-research-plan_example.md:175-176`), and the example uses the full variant. A full variant can still read
  short, and the example should.

**Tested and holding:**

- `:7078` and `:7080-7087`, two sizes and not three (Finding 1).
- `:7150`, `:7154` and `:7156`, the Summary, Key Findings and Recommendations rows. All their spans are Quotable
  lines.
- `:7153`, What We Did, with the deviation line still a POSITION.
- `:7160-7162`, the order after UserTesting's detailed form [11]. No list puts research questions after the
  method; usability.gov puts its introduction before its summary [9].
- `:7166-7168`, no decision and no chosen concept, as the library's boundary. The sources pull toward both
  (Finding 4).
- `:7169-7170`, no aggregate across studies. The repository and cumulative-base material [32], [42] fails the
  one-study test.
- `:7183-7186`, the experiment boundary, which this log did not retest. Gilad's qualifier travels with his line
  here too: "I realize that this is not the common definition used in the industry - in many cases the words test
  and experiment are used interchangeably." [29].
- `:7187-7190`, the QA edge, on NIST's summative lines [1], [2].
- `:7258-7260` and `:7324-7325`: either role writes the report, and GitLab lets a product manager author it [28].
- `:7262-7265`, the interview method, with Task Results marked not applicable.
- `:7340-7341`, risk 5's lineage sentence, which NIST's first Quotable line supplies [1].

**Strengthened:**

- `:6990-6991`, one study's report at two depths. Condens [15], Usercall [30], User Interviews [14] and Maze [13]
  join Dovetail and UserTesting (Finding 1).
- `:7155`, Task Results' content, now on three lists (Finding 7).
- `:7157`, Open Questions, from one list to two lists and four further sources.
- `:7153`, the limits clause, on [43], [38] and [24].

---

## Claims flagged contested or time-bound

1. **Where recommendations go.** After each finding [15], [10]; by task [22]; in their own section [9], [11], [14].
2. **Whether to write a report at all.** No report for a quick test [3]; no time on agile teams [4]; stop
   reporting [35]; the debrief first [43]; always, for the record [14], [30].
3. **Format.** Slides are most popular at GitLab [28]; written reports are static [13]; a story instead of a deck
   [12]; a deck framework of its own [13].
4. **Whether the report ends in a decision.** A decision or a debate [30]; who decides [10]; lead with decisions
   [37]. The contract recommends only.
5. **Severity scales.** Zero to four [17]; three levels plus insights [26]; low, medium and high [16].
6. **Count formats.** Five formats, with fractions preferred unless the denominator appears elsewhere [23].
7. **Formative and summative.** NIST's template allows formative reporting [1]; NIST's CIF page says the format is
   for summative testing [2].
8. **Method depth.** Brief for stakeholders [13], [14]; the full CIF for other researchers [14].
9. **What a nugget is.** One insight, observation or piece of data [11]; experiments, facts, insights and
   conclusions [13]; a labelled observation [33].
10. **Test versus experiment.** Gilad's line is his own definition, by his own account [29].
11. **Who writes it.** A researcher [14]; anyone as DRI, with a researcher's support [28]; a designer [35].
12. **Time-bound facts.** NISTIR 7742 is version 0.2 of November 2010 [1]. NIST's CIF page is no longer updated
    [2]. DHS's kit was updated in February 2025 [3]. GOV.UK's sharing page dates from 2016 [4]. usability.gov is
    archived [8], and digital.gov's templates date from 2014 [6]. Employee Express reports a 2013 test [7]. User
    Interviews' chapter says it is 2019 content [14]. Mozilla's post dates from December 2019 [51]. Every vendor
    page is a living page, and the maintainer's copy of Koji's shows no date [52].

---

## Honest framing

**What the bundle exists to say.** A user research report, as this bundle builds it, records what one study of
people found and what it recommends, after the study ends. It answers the questions the plan set. Each finding
carries a count and evidence a reader can check, and the report names what the study could not answer. For a
usability test, it also reports the tasks' results. Each part is sourced: the definition [13], [14]; the two
depths [10], [11], [15]; the answer first [10], [46]; the evidence [10], [25], [30]; the counts [23], [25]; the
usability results [1], [9], [22]; the recommendations [10], [14], [20]. **The lean and full pair rests on sources
that name two depths of one study's report** [10], [11]. One answer per question, the conditional usability
section and the deviation line are the library's arrangement.

**What the bundle must not claim:**

- **That a report improves research or product outcomes.** No source in this log measured it.
- **That reports go unread, as a measured fact.** The sources give testimony [14], [30], [35], [46].
- **That every study ends in a written report** [3], [4], [35].
- **That keeping the decision out of the report is received practice.** The sources pull the other way [10],
  [30], [37]; it is the contract's line.
- **That no deck has a structure of its own** [13].
- **That NISTIR 7742 is general product practice, or a regulatory form** (Finding 9).
- **That NIST's own pages agree on formative testing** [1], [2].
- **That any severity scale or count format is the standard** [16], [17], [23], [26].
- **That a product manager usually writes the report.** GitLab shows that one may [28]; no source gives a share.
- **That usability.gov's template or digital.gov's kit is current federal guidance** [6], [8].
- **That User Interviews' chapter is current.** It says it is 2019 content [14].
- **That any source calls a study of a shipped product discovery work** (Finding 10).
- **That a fixed retention period belongs in one study's report** [39], [49].
- **That a report records a decision or names the concept to build** (Finding 4).

---

## Notes for the companion

**The load-bearing sections.** Five of the skeleton's eleven (`templates/methodology.md:172-182`) carry this
bundle. **Origins** must teach the CIF and the US government lineage, with the retired sources dated and NIST's
formative tension named (Findings 7 and 9). **Variants and sizing** must teach two depths of one study's report
(Finding 1). **Debates** must name the disputes over whether to write a report, its format, where recommendations
go, the pull toward the decision, and severity scales (Findings 3 to 6). **Relationships** must place the plan,
the debrief, the repository, the QA pair's edge on NIST's summative lines, the documents that use the findings and
the experiment pair. **Anatomy** must label which parts are sourced and which are the library's arrangement: one
answer per question, the deviation line and the conditional Task Results. Wherever the companion explains the
phase, it carries the shipped-product paragraph (Finding 10).

**The sharpest teaching points:**

1. **Lead with the answer** [10], [13], [46].
2. **Give every claim evidence a reader can check** [10], [30].
3. **Report counts as fractions, with the denominator** [23], [25].
4. **Answer each question the plan set, and say which the study could not answer** [14], [27], [46].
5. **Recommend, and name who decides; do not record the decision** [10], [16].
6. **Say what already works** [16], [26].
7. **Anonymise quotations, and keep within consent** [40], [49].
8. **Write two depths for two audiences, from the same findings** [10], [15].

**Section design.** Finding 12 maps the research onto the nine proposed sections, and Finding 11 routes every gap
candidate under decision procedure 12. Every proposed change there is a candidate, and this log admits none. The
strongest are lean ASKs. Summary asks for the objective, the decision and who makes it. Research Questions and
Answers asks whether each answer confirms the plan's hypothesis, and which questions stayed open. Key Findings
asks for fractions, positive findings, and anonymised quotations within consent. What We Did may ask which
product version the participants reacted to (gap candidate 17, on one vendor source [52]). A review-by date
stays out.

**The traps:**

1. **Quoting anything that is not a Quotable line**: the spec's spans this log lacks, the lost parts of the drops,
   and the dimension-file spans, all listed in the checks section.
2. **Citing NIST's headings without the health-records customization in the same sentence** [1]
   (`tier2-specs.md:7340-7341`).
3. **Calling NISTIR 7742 regulatory** on this log's evidence (Finding 9).
4. **Presenting the no-decision line as what the sources do** (Finding 4).
5. **Using test report or test results alone where `test-summary-report` collides** (`:7136-7138`).
6. **Quoting Ethnio's cells as evaluative or generative** [36]. Use UserTesting's labelled sentences [48].
7. **Treating User Interviews' 2019 chapter as current** [14].
8. **Repeating NIST's questionnaire thresholds as the library's standards** [1].
9. **Reusing the worked example's scenario in GOOD and WEAK text**, the risk the spec names (`:7337-7339`). Grep
   the drafted templates and guide for Saved Views, Recurring Analyst, Priya Nair, friction study, Team Lead and
   re-filter before review. The Task Results GOOD text uses a usability test unrelated to the example
   (`:7142-7143`).

**The example.** The maintainer ruled the scenario on 2026-10-24 (ruling 7,
`docs/internal/tier2-specs.md:7389-7390`). The report is the readout of the 2026-05 Reporting friction study,
which four shipped examples cite and none shows. It answers the plan's example
(`templates/user-research-plan/user-research-plan_example.md`), and it uses the full variant (`:7089-7090`). Priya
Nair, PM, Reporting, writes it, dated 2026-05-27. Acme's UX Research function ran the sessions; that is a
function, not a person. The sessions ran from 2026-05-04 to 2026-05-15 with 12 analysts. Each was a one-to-one
interview of about an hour, with a walkthrough of the analyst's own dashboard (`:7262-7265`). Task Results is
marked not applicable in one line. The report must be findable by the PRD's own citation,
`Discovery readout: Reporting friction study, 2026-05` (`templates/prd/prd_example.md:12`, `:173`).

- **What the plan promised, which the report keeps.** The plan names Priya Nair as author and
  `Dana Okoro, VP Product` as approver, dated 2026-04-20 (`user-research-plan_example.md:4-7`). It promises
  `A short written readout to the Reporting product and design team, within two weeks of the last session`
  (`:175-176`). Two weeks from 2026-05-15 ends on 2026-05-29, so 2026-05-27 keeps the promise, and the full variant
  should still read short. The report addresses the Reporting product and design team, unnamed. Marcus Webb, the
  design lead, appears first in the design brief of 2026-06-01 (`design-brief_example.md:116-117`). The plan
  expects the readout to follow where the time went in a session, with re-filtering counted beside the other
  repeated actions the note taker logged (`:177-179`). The decision it feeds is whether to fund the work next
  quarter (`:39-43`, `:180-181`). The report recommends and does not decide.
- **The five questions, each answered** (`:56-65`). Question 5, re-filtering against exporting and sharing, is the
  top finding. Question 3, workarounds, is the text file. Question 2, whether rebuilt filters match intent, is the
  wrong-slice risk (`prd_example.md:46-47`). Question 1 is answered by the top finding, with no minutes-per-day
  figure (`tier2-specs.md:7279-7281`). No sibling answers question 4, on analysts who open the dashboard several
  times a week against about once a week (`:62-63`). The persona's `3 to 4 times a week`
  (`user-persona_example.md:70`) describes the persona study, not this one. On this log's reading, Open Questions
  is the safer home for question 4, since any answer would add a fact no sibling states.
- **The hypothesis** (`:66-69`) can be confirmed in the report's terms, with the binding counts and no time
  figure (gap candidate 2).
- **The binding facts** (`tier2-specs.md:7215-7229`), with each sibling's exact wording, read on 2026-10-26:
  - **The top finding.** The PRD says re-filtering was
    `the single most frequent repeated action in the dashboard, ahead of export and share`
    (`prd_example.md:35-36`). The design brief says
    `the single most frequent repeated action on the dashboard, ahead of both exporting and` /
    `sharing` (`design-brief_example.md:34-35`). The epic says
    `the single most frequent repeated action inside a dashboard, ahead of both export and share`
    (`epic_example.md:46`). The spec's row quotes the PRD and cites the epic at `:45-46` (`tier2-specs.md:7219`).
    The build notes place the epic's phrase at `:45`, but it sits on `:46`. The PRD's citation is how a reader
    finds the report, so the report's sentence should match the PRD's wording.
  - **The sample.** The epic says `across the twelve analysts interviewed` (`epic_example.md:45`), in words. The
    PRD says `9 of 12 interviewed analysts` (`prd_example.md:44`), and the design brief says
    `The friction study interviewed 12 analysts` (`design-brief_example.md:62`). The spec's table gives
    `12 analysts, interviewed` (`tier2-specs.md:7218`). The forms agree; the report should use the digit, as two
    of the three siblings do.
  - **The first count.** The PRD: `9 of 12 interviewed analysts described manually rebuilding filters several times a day`
    (`prd_example.md:44`). The design brief: `9 of them described` / `rebuilding filters by hand several times a day`
    (`design-brief_example.md:62-63`).
  - **The second count.** The PRD says `3 kept a personal text file of` (`prd_example.md:45`), and the design
    brief says `3 kept a personal text file listing` (`design-brief_example.md:63`). The epic says
    `three kept a personal note of` (`epic_example.md:47`). The spec's table says `a personal text file`
    (`tier2-specs.md:7221`), as the PRD and the design brief do, and the report should too. The design brief
    later calls it `a personal list` (`:107`), a looser echo.
  - **The cost:** broken flow, and the wrong slice from a filter set rebuilt from memory
    (`prd_example.md:46-47`; `design-brief_example.md:64-66`).
  - **The reframing** from a feature gap to a recurring time tax, after two deferrals (`prd_example.md:36-37`).
    The report states it as a finding, not as a decision.
  - **Illustrative.** The PRD labels them `illustrative counts from a 12-person` / `study` (`prd_example.md:45-46`).
    The report labels its counts illustrative too.
- **The sharing clause.** The announcement says the pattern found `more often than any other` was an analyst
  rebuilding a setup `because nobody else could reach their saved setup`
  (`announcement-internal-comms_example.md:66-68`). The spec's reading (`tier2-specs.md:7249-7252`) is that the
  only saved setups were personal notes no teammate could see. That fits the three text files. On this log's
  reading, the report can say the personal text files were the only saved setups, and that no teammate could
  reach them. The review checks the wording against both sentences.
- **The Team Lead.** The design brief says Priya named this second audience from the study,
  `not a separately documented persona` (`design-brief_example.md:53-55`, `:60-61`). The report may mention team
  leads wanting one agreed view, and only as far as that sentence goes.
- **What the study did not ask.** Who owns a shared lens, and what a saved lens does when its dashboard changes
  (`design-brief_example.md:103-106`). The report answers neither. Lens is the design brief's concept word, so the
  report does not use it to raise them either.
- **Coverage.** The study covered only a small set of report types (`design-brief_example.md:110-112`). The report
  names that limit in What We Did.
- **The notes.** The full interview notes exist, and the design team receives them with the brief
  (`design-brief_example.md:116-118`). The brief's date, 2026-06-01, comes from its opening note (`:16`), not from
  the handoff line, as `dim5.md` notes. The Appendix says where the notes live, as the plan's consent section
  provides (`user-research-plan_example.md:159-171`).
- **Facts older than the plan, which the report may read.** The persona (2026-01-05), the strategy's
  `Time to Insight` goal (2026-01-28) and the roadmap's Saved Views line (2026-02-11), as the spec lists
  (`tier2-specs.md:7231-7234`). The plan's log found a trap in two of them: the strategy names later documents'
  versions of the goal, and the roadmap frames Saved Views as the second-view problem. The report cites neither
  framing.
- **Trap 1: two 12-person studies.** The persona's study ran in November and December 2025, n=12
  (`user-persona_example.md:42`). It found `9 of 12` raising re-filtering (`:54`) and `6 of 12` keeping a
  spreadsheet (`:71`). The friction study also has a `9 of 12`, a different count (`prd_example.md:44`), so each
  use names its study. No spreadsheet and no `6 of 12` appear as friction-study facts. The persona's time range
  of `5 to 10 minutes` and its count of 34 tickets (`user-persona_example.md:61`) are the persona's. The report
  may cite the tickets in Background and Objectives as the persona work's, as the plan does
  (`user-research-plan_example.md:76-77`), and never as a finding. It leaves the time range out, since a time
  figure invites the reconciling the spec warns against (`tier2-specs.md:7279-7281`). The colorblind hub lead came from the persona interviews (`design-brief_example.md:99`),
  not the friction study. The nine customer accounts are the persona study's (`user-persona_example.md:90-91`).
- **Two people named Elena Cho.** The persona is Elena Cho (`user-persona_example.md:3`), and the epic names an
  Elena Cho in Design Systems (`epic_example.md:114`). The report names neither, and reports analysts unnamed.
- **People.** Priya Nair writes. Dana Okoro approved the plan. UX Research moderated and took notes, unnamed
  (`user-research-plan_example.md:151-152`). Priya and a Reporting designer observed two calls apiece (`:153-154`).
  No new named person is needed (`tier2-specs.md:7258-7260`). The epic's Marcus Bell and Dana Osei are different
  people from Marcus Webb and Dana Okoro (`epic_example.md:112-113`), so a name check covers both pairs.
- **Not carried.** The per-user preferences storage that shipped in Q1 appears in the PRD and the design brief
  (`prd_example.md:38`, `design-brief_example.md:37`), both dated after the report. It is a data-model fact, not a
  finding, and the report leaves it out.
- **What it must not contain.** No concept, and no decision (`tier2-specs.md:7271-7282`). No minutes-per-day
  figure. No document dated after 2026-05-27 cited as existing: not the design brief, the PRD, the epic, the user
  stories, the test plan or the announcement. The opening Worked example blockquote may mention later documents,
  as sibling examples do.
- **Check the siblings' own text, not this note.** Read the plan, persona, PRD, design brief, epic and
  announcement examples before writing, and make every carried fact match them exactly.

## Sources

### Government and standards bodies: the formal report

**[1] NIST (Robert M. Schumacher and Svetlana Z. Lowry) - NISTIR 7742, "Customized Common Industry Format Template for Electronic Health Record Usability Testing" (v0.2, Nov 2010).** primary. **fetched-and-verified.**
`https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7742.pdf`
Supports: Full 37-page CIF-derived report template: every section heading verbatim, its guidance/instruction text, the executive-summary instructions, the results-reporting mechanics (task success, path deviation, task time, errors, SUS), how results tie to the stated study goals, and the formative/summative and EHR-specific scope statements
Quotable: "This document provides a template for the modified version of Software engineering - Software product Quality Requirements and Evaluation(SQuaRE) - Common Industry Format (CIF) for usability test reports (ISO/IEC 25062:2006(E)), the Common Industry Format (CIF) usability test report. This version of the CIF has been customized for use in usability testing of Electronic Health Records (EHRs) by usability administrator(s) and data logger(s)."
Quotable: "The ISO document is intended for the reporting of summative (i.e., quantitative) studies. The modifications here allow for the reporting of qualitative findings (i.e., formative) but strongly recommend and encourage the collection of quantitative measures of user performance."
Quotable: "1 EXECUTIVE SUMMARY"
Quotable: "2 INTRODUCTION"
Quotable: "3 METHOD"
Quotable: "3.1 PARTICIPANTS"
Quotable: "3.2 STUDY DESIGN"
Quotable: "3.3 TASKS"
Quotable: "3.4 PROCEDURE"
Quotable: "3.5 TEST LOCATION"
Quotable: "3.6 TEST ENVIRONMENT"
Quotable: "3.7 TEST FORMS AND TOOLS"
Quotable: "3.8 PARTICIPANT INSTRUCTIONS"
Quotable: "3.9 USABILITY METRICS"
Quotable: "4 RESULTS"
Quotable: "4.1 DATA ANALYSIS AND REPORTING"
Quotable: "4.2 DISCUSSION OF THE FINDINGS"
Quotable: "A usability test of [name of product, version, and type of EHR] was conducted on [date] in [location] by [test laboratory]. The purpose of this test was to test and validate the usability of the current user interface, and provide evidence of usability in the EHR Under Test (EHRUT)."
Quotable: "This study collected performance data on [xx] tasks typically conducted on an EHR:"
Quotable: "During the [time, e.g., xx minute] one-on-one usability test, each participant was greeted by the administrator and asked to review and sign an informed consent/release form"
Quotable: "The results from the System Usability Scale scored the subjective satisfaction with the system based on performance with these tasks to be: [xx]. ... Broadly interpreted, scores under 60 represent systems with poor usability; scores over 80 would be considered above average."
Quotable: "A task was counted as a "Success" if the participant was able to achieve the correct outcome, without assistance, within the time allotted on a per task basis. The total number of successes were calculated for each task and then divided by the total number of times that task was attempted. The results are provided as a percentage."
Quotable: "The number of steps in the observed path is divided by the number of optimal steps to provide a ratio of path deviation."
Quotable: "Average time per task was calculated for each task. Variance measures (standard deviation and standard error) were also calculated."
Quotable: "Common convention is that average ratings for systems judged easy to use should be 3.3 or above."
Quotable: "The discussion should commence with a narrative discussion of each of the major areas in light of the findings] EFFECTIVENESS"
Quotable: "EFFICIENCY"
Quotable: "AREAS FOR IMPROVEMENT"
Quotable: "15-Nov-10"
Quotable: "Version 0.2"
Quotable: "Page 1 of 37"
Quotable: "Reports delivered using this template should conform to the major headings and content areas outlined below. Minor deviations from the outline and format are acceptable, but the reports should follow the template in all material aspects."
Quotable: "The following types of data were collected for each participant:"
Quotable: "Number of tasks successfully completed within the allotted time without assistance"
Quotable: "Time to complete the tasks"
Quotable: "Number and types of errors"
Quotable: "Path deviations"
Quotable: "Participant’s satisfaction ratings of the system"
Quotable: "The results should be seen in light of the objectives and goals outlined in Section 3.2 Study Design."
Quotable: "The data should yield actionable results that, if corrected, yield material, positive impact on user performance."
Quotable: "Effectiveness of [EHRUT] by measuring participant success rates and errors"
Quotable: "Efficiency of [EHRUT] by measuring the average task time and path deviations"
Quotable: "This document is not intended to be a tutorial on usability or usability testing."
Quotable: "To work with this document you should have expertise with common usability industry practices"
Quotable: "SAMPLE RECRUITING SCREENER"
Quotable: "PARTICIPANT DEMOGRAPHICS"
Quotable: "NON-DISCLOSURE AGREEMENT AND INFORMED CONSENT FORM"
Quotable: "EXAMPLE MODERATOR’S GUIDE"
Quotable: "SYSTEM USABILITY SCALE QUESTIONNAIRE"
Quotable: "INCENTIVE RECEIPT AND ACKNOWLEDGMENT FORM"

**[2] NIST, Information Technology Laboratory / Technology Test and Evaluation Division - "What is the CIF?" (Human-Centered Technologies page).** standards. **fetched-and-verified.**
`https://www.nist.gov/itl/iad/human-centered-technologies/what-cif`
Supports: The CIF lineage and scope: what the ANSI/INCITS-354 CIF is, who it is for, what format it prescribes, and NIST's own caution that the CIF is designed for summative rather than formative testing - the qualifying sentence that complicates NISTIR 7742's claim to also support formative reporting
Quotable: "The ANSI/INCITS-354 Common Industry Format (CIF) for Usability Test Reports is a standard method for reporting usability test findings. The American National Standards Institute (ANSI) approved the CIF December 12, 2001 as the standard for reporting usability test results. The purpose of the CIF is to encourage incorporation of usability as an element in decision making for software procurement."
Quotable: "The CIF targets two audiences: usability professionals and stakeholders in an organization. The CIF is designed for usability professionals who generate reports to be used by stakeholders. Stakeholders can use the usability data to help make informed decisions concerning the release of software products or the procurement of such products."
Quotable: "The format is primarily for reporting results of formal usability tests in which quantitative measurements were collected and is particularly appropriate for summative/comparative testing. The format includes the following main sections: Executive Summary, Introduction, Method, and Results."
Quotable: "The CIF assumes that best practice is used in designing and conducting a usability test. The CIF does not tell you what to do; it tells you how to report on what you did. The CIF is designed for summative testing rather than formative testing."
Quotable: "This page is no longer being updated and the information may be out of date."
Quotable: "Created May 20, 2016, Updated August 27, 2025"

**[3] U.S. Department of Homeland Security - DHS Usability Testing Kit (landing page).** primary. **fetched-and-verified.**
`https://www.dhs.gov/cx/dhs-usability-testing-kit`
Supports: DHS's scaled approach to reporting, from no formal report through a short report to a full report using a provided report template, across four testing methods of increasing formality. Also DHS's minimum-participant guidance and last-updated date
Quotable: "Testing in the office: quick usability feedback from colleagues. If you're in the early stages of designing your materials, this approach is a fast way to get a second opinion."
Quotable: "Reporting - There's no need to formalize your findings; just use your rough notes on usability issues to revise the materials or start developing a prototype."
Quotable: "Testing out of the office: catch real users in the field. If you have drafts or prototypes that are close to complete, use this approach to test how people use them."
Quotable: "Reporting - Depending on your situation, you can use your findings to compile a short report or simply use your notes to iterate your design further."
Quotable: "Testing in the conference room: thorough, structured testing with real users. If you have solid, revised materials, this approach allows you to run a structured test with real users who you've scheduled ahead of time."
Quotable: "A full usability test can happen at any stage in the process, from testing the original version, testing drafts, or testing the almost-final version. This approach may or may not result in a formal report."
Quotable: "Reporting - Using the report template provided, compile your results into a report, highlighting all stages of the usability test (i.e., participant data, testing locations, material tested, findings, and recommendations)."
Quotable: "Testing remotely by videoconference: expanded testing with remote users. ... This can be especially useful for testing websites, digital forms, and applications, where the user's screen can be shared and recorded during the test."
Quotable: "Try to test at least four people who normally might use the material you're testing. If you think there might be different behaviors for different types of users, include four of each type."
Quotable: "Full usability tests can be conducted with anywhere between eight and 100 participants. Most of these usability tests include 8-20 participants in individual sessions that last between 30 and 90 minutes."
Quotable: "Last Updated: 02/27/2025"

**[4] GOV.UK Service Manual, User research community - "Sharing user research findings".** standards. **fetched-and-verified.**
`https://www.gov.uk/service-manual/user-research/sharing-user-research-findings`
Supports: GOV.UK's scaling of the write-up away from a formal report toward slide decks and research walls, and its explicit statement that agile-team researchers often skip a written report (the qualifying sentence that softens any claim that every study ends in a report)
Quotable: "User research is only useful if your team can use what you've learned to improve your service."
Quotable: "It's important to update your team regularly, ideally at a fixed time each week or sprint."
Quotable: "As sprints go by, your collection of slide decks will provide a record of what you've learned about your users. This is useful because researchers on an agile team won't have time to write research reports (though they might produce brief research summaries)."
Quotable: "Published: 24 May 2016"
Quotable: "A simple way to present research findings is to create a group of slides (or ‘slide deck’) that includes:"
Quotable: "1 or 2 slides that outline the research you did"
Quotable: "5-10 slides that describe your findings"
Quotable: "1 or 2 slides that show what you’re doing next (if relevant)"
Quotable: "Each findings slide should include:"
Quotable: "a headline that communicates something you’ve learned"
Quotable: "1 or 2 sentences that describe the essential facts of the finding"
Quotable: "1 or 2 sentences that explain its importance and any consequences"
Quotable: "a relevant photo or screenshot of what you were testing, or a quote from a participant"

**[5] GOV.UK Design System community page - "Share findings about your users".** standards. **fetched-and-verified.**
`https://design-system.service.gov.uk/community/share-research-findings/`
Supports: A negative/contextual finding: this page is NOT a user-research-report template. It is a GitHub-comment template for feeding findings back to the GOV.UK Design System team about components and patterns, with no Executive Summary / Method / Results structure of its own
Quotable: "We want to hear how users experience styles, components and patterns in your service - it helps us improve the Design System. You can do this by taking part in discussions on GitHub."
Quotable: "## Insights"
Quotable: "What are your insights about how people use the style, pattern or component?"
Quotable: "## Methods"
Quotable: "Give us some context and briefly explain how you gathered the findings."
Quotable: "## More information"
Quotable: "Add links to any prototypes or research documents."
Quotable: "Use this template to give the community useful context about your findings. Copy and paste it into the GitHub comments box and add your findings."
Quotable: "we will usually investigate something if we hear similar findings from 4 or more different services"

**[6] GSA Digital.gov (via Wayback Machine, snapshot of the retired digitalgov.gov page) - "Usability Starter Kit".** primary. **fetched-and-verified.**
`https://digital.gov/resources/digitalgov-user-experience-resources/digitalgov-user-experience-program-usability-starter-kit`
Supports: Confirms the digital.gov kit links two distinct report templates (a PowerPoint and a Word document) rather than a single report document; supplies the direct download link used to retrieve and read Usability Report Template 2's headings. The live page now 404s; read via Wayback Machine per the terms rule's allowance for retired government pages
Quotable: "Here are some tools and templates to help you create better user experiences."
Quotable: "Usability Report Template 1 (PowerPoint presentation, 373 KB, 8 slides, May 2014)"
Quotable: "Usability Report Template 2 (Word document, 20 KB, 6 pages, May 2014)"
Quotable: "Usability Testing Script (Word document, 81 KB, 6 pages, November 2013)"

**[7] GSA Digital.gov / Usability.gov (worked example docx, no named individual author) - "Usability Test Summary: Employee Express" (filled instance of Usability Report Template 2).** primary. **fetched-and-verified.**
`https://s3.amazonaws.com/digitalgov/_legacy-img/2014/01/EmployeeExpressfinalreport-2.docx`
Supports: A second, shorter report shape (filled, not blank) used by the digital.gov/usability.gov community: a one-page problem/solution summary table plus a short narrative report with 'Executive Summary', 'Short Term Problems and Solutions', 'Long Term Problems and Solutions', 'Other Identified Problems', 'Who We Tested', 'List of Tasks', and 'Learn More' - a far leaner structure than the NIST/usability.gov CIF-style template
Quotable: "Usability Test Summary: Employee Express"
Quotable: "Test Details: Test date: July 22, 2013 Users tested: 3 Method: Formal Usability Test"
Quotable: "Executive Summary: The test participants used major functions of the site relatively easily. However, users experienced frustration with the Login and Security pages."
Quotable: "Short Term Problems and Solutions"
Quotable: "Long Term Problems and Solutions"
Quotable: "Other Identified Problems:"
Quotable: "4. Who We Tested"
Quotable: "5. List of Tasks"
Quotable: "6. Learn More"

**[8] Usability.gov (GSA), archived page via Wayback Machine - "Report Template: Usability Test".** primary. **fetched-and-verified.**
`https://www.usability.gov/how-to-and-tools/resources/templates/report-template-usability-test.html`
Supports: Confirms the retired usability.gov page's existence, its archival banner, its summary line, and the direct docx link used to retrieve the full template read below. This is the specific 'retired usability.gov report template' the task named
Quotable: "Usability.gov is archived and no longer updated."
Quotable: "External links may not function and information on the site may be out of date. Visit Digital.gov for current information."
Quotable: "Report Template: Usability Test"
Quotable: "DOCX - 85KB"
Quotable: "Summary: An example of a usability test report. Customize the report to suit your needs."
Quotable: "Tags: Reporting Results, Testing, Usability Evaluation, User Research, User-centered Design Process"

**[9] Usability.gov (GSA) - "[Name of Web Application/Site] Test" report template docx (the full retired usability.gov Report Template: Usability Test).** primary. **fetched-and-verified.**
`https://www.usability.gov/sites/default/files/report-template-usability-test_0.docx`
Supports: The complete section-by-section structure and per-section instruction text of the usability.gov report template, read in full by downloading the docx via the Wayback Machine and parsing its heading styles and text runs directly (not via WebFetch)
Quotable: "[Name of Web Application/Site] Test"
Quotable: "Table of Contents"
Quotable: "[insert Table of Contents]"
Quotable: "Introduction"
Quotable: "[Include and introduction about the Web site or application and the purpose of the site.]"
Quotable: "A usability test is intended to determine the extent an interface facilitates a user's ability to complete routine tasks. Typically the test is conducted with a group of potential users either in a usability lab, remotely (using e-meeting software and telephone connection), or on-site with portable equipment."
Quotable: "Executive Summary"
Quotable: "Methodology"
Quotable: "Sessions"
Quotable: "Participants"
Quotable: "Evaluation Tasks/Scenarios"
Quotable: "Results"
Quotable: "Task Completion Success Rate"
Quotable: "[Explain who recorded the participant's ability to complete the tasks without prompting. The task success rate is the number of successes divided by the number of participants completing the task.]"
Quotable: "Task Ratings"
Quotable: "Ease in Finding Information"
Quotable: "Keeping Track of Location in Site"
Quotable: "Predicting Information Section"
Quotable: "Time on Task"
Quotable: "The testing software recorded the time on task for each participant. ... [Provide a task by task description - include the task title or goal and the mean time to complete. Provide the range of completion times.]"
Quotable: "Errors"
Quotable: "[Insert who captured the errors here] captured the number of errors participants made while trying to complete the task scenarios. ... A non-critical error is an error that does not prevent successful completion of the scenario."
Quotable: "Summary of Data"
Quotable: "The table below displays a summary of the test data. Low completion rates and satisfaction ratings and high errors and time on tasks are highlighted in red."
Quotable: "Overall Metrics"
Quotable: "Overall Ratings"
Quotable: "4.6.2 Likes, Dislikes, Participant Recommendations"
Quotable: "Recommendations"
Quotable: "The recommendations section provides recommended changes and justifications driven by the participant success rate, behaviors, and comments. Each recommendation includes a severity rating."
Quotable: "Conclusion"
Quotable: "[Provide a short conclusion paragraph. Begin with an overall statement of what the participants found and what is key about the Web site/application]."
Quotable: "[Add Attachments. Attachments may include: Attachment A - Background Questionnaire, Attachment B - Post-Task Questionnaire, Attachment C - Post-session Overall Subjective Questionnaire, Attachment D - Task Scenarios]"
Quotable: "All participants successfully completed Task 1 (find a news item). Six of the seven (86%) completed Task 5 (find HIV Testing Day). ... None of the participants were able to complete Task 6"
Quotable: "Mean agreement rating = 4.7"
Quotable: "*Percent Agree (%) = Agree & Strongly Agree Responses combined"
Quotable: "*Satisfaction = Mean combined rating across three post-task measures: ease of finding the information, ability to keep track of location in site, and site information prediction accuracy."

### Vendors and practitioners: the report's sections at two depths

**[10] Dovetail, "Research report template" (marketing/template page).** vendor. **fetched-and-verified.**
`https://dovetail.com/research-report-template/`
Supports: Section list (six sections), summary-first framing, finding = claim + evidence + why-it-matters, length guidance, audience tailoring, written-vs-slide framing, FAQ restating the same structure
Quotable: "Six sections, in this order: a summary that states the answer up front, background and objectives (two or three sentences on why the study ran), method and participants, key findings, recommendations, and open questions."
Quotable: "Limit findings to three to five-each one a claim, the evidence behind it, and why it matters."
Quotable: "Everything else, including discussion guides and full transcripts, belongs in an appendix or a link."
Quotable: "Put the headline finding in the first three sentences-don't make readers excavate it"
Quotable: "Every claim cites a quote, a clip, or a number a reader can check"
Quotable: "End each finding with what the team should do about it, and who decides"
Quotable: "As short as the decision allows. A one-page summary with linked evidence beats a forty-slide deck nobody opens."
Quotable: "A useful test: a stakeholder should grasp the headline finding in under a minute and reach the supporting evidence in one click."
Quotable: "Executives want one page with the decision; your product team wants the detail behind it. Rather than writing one report that serves nobody, generate reports tailored to each audience from the same project-same findings, same citations, different depth."
Quotable: "A finding without evidence is an opinion with formatting."
Quotable: "An insight is a single evidence-backed finding-one pattern, with the data behind it. A report packages several insights into a narrative for a specific audience, with method, context, and recommendations. In Dovetail, insights are the building blocks; reports are how you deliver them to the people making decisions."

**[11] UserTesting Knowledge Base, "Create a good report" (help article, dated January 22, 2026).** vendor. **fetched-and-verified.**
`https://help.usertesting.com/hc/en-us/articles/25142550337565-Create-a-good-report`
Supports: Three named templates at three depths (executive summary, detailed report, quick snapshot) with explicit section lists; evidence types; audience tailoring; Atomic Research nugget concept (conflates observation/insight)
Quotable: "Use this article to help you create a clear, actionable research report that highlights key insights, supports them with evidence, and provides recommendations."
Quotable: "Clear Structure: Organize findings logically so stakeholders can quickly grasp key takeaways."
Quotable: "Concise Insights: Focus on high-impact insights rather than listing every detail."
Quotable: "Support your points with Evidence: Easily add video clips, screenshots, charts, or summaries to reports to support your recommendations."
Quotable: "Actionable Recommendations: Provide next steps that are based on research findings and are clearly actionable."
Quotable: "Tailored for the Audience: Adjust depth and tone depending on whether the report is for executives, designers, product managers, etc."
Quotable: "💡Note: Consider including an executive summary for quick insights."
Quotable: "Defined research methodology: Clearly outline the research type, participant details, recruitment criteria, and tools used to provide context and ensure insight reliability."
Quotable: "Executive summary report (For Stakeholders and Leadership)"
Quotable: "Title"
Quotable: "Objective of the Study"
Quotable: "Key Takeaways (3-5 bullet points)"
Quotable: "Top 3-5 Findings (with short explanations and evidence)"
Quotable: "Recommendations"
Quotable: "Next Steps & Action Items"
Quotable: "Detailed research report (For UX and Product teams)"
Quotable: "Introduction"
Quotable: "Background & Objectives"
Quotable: "Research Questions"
Quotable: "Methodology (e.g., unmoderated usability tests, surveys, etc.)"
Quotable: "Key Findings"
Quotable: "Group insights into themes (e.g., usability, navigation, trust, engagement)"
Quotable: "Use direct quotes or clips to support findings"
Quotable: "Include quantitative data where applicable (e.g., success rates, charts, QX Score visualizations)"
Quotable: "Pain Points & Opportunities"
Quotable: "What's not working?"
Quotable: "Areas for improvement"
Quotable: "Prioritized based on impact"
Quotable: "Potential solutions or design changes"
Quotable: "Appendices"
Quotable: "Full responses, session details, additional data"
Quotable: "Quick feedback snapshot (For Agile teams)"
Quotable: "Study Goal"
Quotable: "Key Insights (Bullet Points)"
Quotable: "Supporting Data (Screenshots, Videos, Metrics)"
Quotable: "Next Steps & Prioritized Action Items"
Quotable: "Atomic Research is an approach that breaks down research findings into their smallest components, known as "nuggets.""
Quotable: "Each nugget represents a single insight, observation, or piece of data, which can be tagged and organized for easy retrieval and combination in future analyses."
Quotable: "Be Story-Driven: Instead of just listing insights, tell a story that helps stakeholders understand the "why" behind the findings."
Quotable: "Keep It Actionable: Ensure every insight ties back to a clear next step."
Quotable: "Highlight Patterns: One-off feedback is less important than recurring themes across multiple contributors."

**[12] UserTesting Knowledge Base (EnjoyHQ product docs), "Research Projects" (help article, dated January 14, 2026 - NOT a report-writing guide; covers the Plan/Data/Analysis/Report workflow of a research project in the EnjoyHQ tool).** vendor. **fetched-and-verified.**
`https://help.usertesting.com/hc/articles/11880311177117`
Supports: Written-report-vs-deck framing (report as narrative, not slides); 'stories' as the individual-finding unit; report built from curated stories for stakeholders to read
Quotable: "4. Report"
Quotable: "This is the section where you will report on the insights you've uncovered to the rest of the organization. Use this section to write an executive summary and add stories below for your stakeholders to read and digest easily. Instead of a slide deck, this is your way to tell a compelling story that can truly communicate the facts behind your research in a quick and easily readable way."
Quotable: "You can think of stories as individual findings or insights. They are digestible articles that help you capture and share your learnings with your colleagues and the entire organization."
Quotable: "Reports are a great way to summarise and transfer knowledge to other teams in your organization. You can feature the stories which capture the essence of your research, its stages, and key findings."
Quotable: "Only Published stories can be attached to the project's report"

**[13] Maze, "How to Create Effective UX Research Reports (+ Free Templates)" (field-guide chapter 11).** vendor. **fetched-and-verified.**
`https://maze.co/guides/ux-research/report/`
Supports: Section list (Introduction/Key findings/Next steps/Q&A/Appendix); report-vs-deck formats list including written reports; audience tailoring; practitioner quotes on methodology depth and on offhand comments; atomic research nuggets (Experiments/Facts/Insights/Conclusions, credited to Sharon/Pidcock, distinct from UserTesting's single-nugget definition)
Quotable: "A user research report is an easy-to-digest summary of a user research project that aims to update product stakeholders on results, inform product decisions with user data, and harmoniously guide a product build or iteration."
Quotable: "Kevin Rapley, Senior User Researcher at Justice Digital, explains a UX report as being "about arming our teammates with data that allows them to decide on the direction of a product or service.""
Quotable: "Introduction"
Quotable: "Your introduction should lay out your research goals, plan, and scope. It should cover your product team's pain points, and give a clear study overview. You need to answer what you did and why."
Quotable: "As a secondary step to your introduction, ensure you're including the approach you took to your UX research process: i.e. what research methods you used, as well as participant profiles and your user personas."
Quotable: "Don't feel you need to spend too much time on this, says Charlie Herbozo Vidal, Senior User Experience Researcher at CVS Health. "As researchers, it's not uncommon to dwell on the methodology for longer than needed. While interrogating methods might be valuable to other researchers, business partners might be disengaged by them.""
Quotable: "Ultimately, while methodology is important, it's the results that most people are here for."
Quotable: "Key findings"
Quotable: "This is where you get people on the edge of their seats! Give an overview of your findings before breaking them down into more detail. Remind your audience of 'what we thought' vs. what you actually learned."
Quotable: "Make sure you champion the user's needs throughout, and make special notes of 'offhand' comments users make. Often, it's the random comments that provide the most insight-they must not be forgotten about when writing the report."
Quotable: "Next steps"
Quotable: "Summarize your quantitative and qualitative research, and how they'll both impact your product design and growth. Lay out opportunities versus risks, good-to-knows versus must-knows."
Quotable: "No matter how you're presenting your research, be it asynchronously or not, you'll need to include a Q&A."
Quotable: "It's easy to overlook the appendix after putting together a detailed report, but all that glorious research data needs to be accounted for and referenced clearly."
Quotable: "5. Written reports: For direct and simple sharing"
Quotable: "These types of reports often come as a PDF or a Word document, making them static, reluctant to change, and resulting in low engagement or re-reads."
Quotable: "For many teams this method still works, especially if you're trying to communicate findings to a distributed, asynchronous team. Written UX reports enable people to go through things in their own time-and come back to them when they need to."
Quotable: "6. Atomic research nuggets: To eliminate 'bad research memory' ... Formalized by Tomer Sharon and Daniel Pidcock, it's described as "the concept of breaking UX research down into its constituent parts": Experiments: "We did this…" Facts: "…and we found out this…" Insights: "…which makes us think this…" Conclusions: "…so we'll do that.""
Quotable: "4. Presentations / slide decks: Great for the PAS framework ... Live presentations tend to be the most impactful, but do risk being short-lived if you don't have a follow-up plan for after your presentation."
Quotable: "Kevin Rapley ... recommends presenting slides using the PAS framework: Problem: State the problem you set out to overcome"
Quotable: "Agitate: Detail the impact or opportunity missed by not meeting the problem"
Quotable: "Solution: Offer a route forward from the research findings and insights, the next steps, and likely outcomes by solving the problem"
Quotable: "Who is your audience? Who needs to see the report, and who will benefit from seeing it? ... If you can tailor versions of your report or provide key summaries for each collective, even better!"
Quotable: "How do you write a UX research report that stakeholders will read? Lead with a short summary of key findings and recommendations, then add the context people need-such as why you conducted the study and the methods you used. Keep language simple, use clear headings and visuals, and tailor depth to your audience instead of over-explaining methods."
Quotable: "What are common mistakes to avoid in UX research reports? Common mistakes include focusing too much on methodology, burying the main insights, using confusing jargon, and not linking findings to concrete next steps."

**[14] User Interviews, UX Research Field Guide, "Writing UX Research Reports and Presentations" (chapter 09.i; carries an in-page note that this chapter is unrevised 2019-vintage content despite a "Last Updated: November 1, 2025" stamp).** vendor. **fetched-and-verified.**
`https://www.userinterviews.com/ux-research-field-guide-chapter/how-to-write-effective-reports-and-presentations`
Supports: Section list (Introduction/Research goals/Business value/Methodology/Key learnings/Recommendations) with per-section guidance; what evidence a finding should carry; actionable-vs-observational finding distinction; audience tailoring; report-vs-presentation tradeoff; recommendations tied to research plan/questions; limitations/follow-up proxy (future research suggestions)
Quotable: "Note to the reader: This part of the field guide comes from our 2019 version of the UX Research Field Guide. Updated content for this chapter is coming soon!"
Quotable: "A research report is a document that summarizes all the details of a research study, including the research questions, methodology, notable insights, and recommended next steps."
Quotable: "In the context of UX research, the report you share outside your research team will likely be closer to a summary: a shorter, top-level document with a greater emphasis on next steps and business application than on methodology."
Quotable: "A UX research report is: A summary of the data and findings of a study"
Quotable: "Well-written with a standardized structure"
Quotable: "Informative, often with links, charts, images, and other data sources"
Quotable: "A data-backed basis for decision-making"
Quotable: "A UX research report is not: A lengthy, dissertation-style paper"
Quotable: "An opinion-based essay"
Quotable: "Something that should require deep UXR expertise to interpret"
Quotable: "Written reports work well for when you're speaking to small groups, a geographically distributed team or technical stakeholders like engineers or other researchers. They're also great for when you need to keep a comprehensive account of the study on record; some researchers always create them for the research repository."
Quotable: "However, many researchers complain that stakeholders don't read them or are overwhelmed by the sheer volume of information."
Quotable: "When to use reports vs. presentations ... Although each has its pros and cons, we recommend doing both! Creating both a detailed report and a presentation ensures that different types of audiences can access and appreciate your findings in the future."
Quotable: "Good research reports all share four fundamental qualities. They are: Attention-grabbing. Actionable. Tailored to the audience. Easy to access and understand."
Quotable: "Actionable reports should relate back to the initial research question: How do your findings influence the decisions you mapped out in your research plan?"
Quotable: "For example, "users are unhappy" is not an actionable insight. Although this might be a true observation from your study, it's not specific enough about the context or application of the insight."
Quotable: "In other words, actionable reports provide: Recommendations for product or business decisions"
Quotable: "Concrete next steps for stakeholders"
Quotable: "Suggestions for what kind of research needs to happen next"
Quotable: "Compelling insights that illuminate unanswered questions"
Quotable: "Although you should be objective and unbiased while conducting and analyzing research, know that it's okay to offer your opinion after the research is done. As the researcher who led the project from start to finish, you're in the best position to interpret the data and make recommendations for how it should be used."
Quotable: "Who's your core audience for the report? If it's only executives, you'll probably want to focus the report around strategy and business application. If you're speaking to your immediate research team, you'll probably want to include more of the minute details."
Quotable: "The basic outline of a research report is: Introduction"
Quotable: "Research goals"
Quotable: "Business value"
Quotable: "Methodology"
Quotable: "Key learnings"
Quotable: "Recommendations"
Quotable: "What should the introduction of a report include? A brief overview of the parameters of your study"
Quotable: "The company goals and pain points you've been studying"
Quotable: "The direct business application of the insights"
Quotable: "What should the research goals section of a report include? The key decisions on which you based your research."
Quotable: "The research questions you'd asked as the catalyst for your study."
Quotable: "Your hypotheses and expectations prior to conducting the research."
Quotable: "What should the methodology section of a report include? The research methods you used to answer your research questions."
Quotable: "A brief explanation of why you chose those methods."
Quotable: "What should the key learnings section of a report include? Recurring themes or trends that you noticed during your analysis."
Quotable: "Relevant quotes, audio clips, or other artifacts that illustrate compelling insights, pain points, common experiences, or aha moments."
Quotable: "Links to more resources, including full session recordings, transcripts, notes, or other data."
Quotable: "What should the recommendations section of a report include? Clear, specific solutions and next steps to solve pain points or answer pending decisions."
Quotable: "Any specific recommendations brought up by users during interviews or in surveys."
Quotable: "Suggestions for future research studies, if applicable."
Quotable: "The common industry format (CIF) for a usability report provides universal guidelines for the research community... If your audience is other researchers... then the CIF format works great... However, this format tends to be quite lengthy, making it less-than-ideal for sharing with stakeholders."

**[15] Condens, "How to work with Condens Artifacts" (help/how-to guide).** vendor. **fetched-and-verified.**
`https://condens.io/help/how-to-guides/best-practices/how-to-work-with-condens-artifacts`
Supports: No report section list; supports audience-depth tailoring, recommendation placement relative to findings, and evidence-as-raw-clips practice; Closest material found to the assigned question, but it does not answer it: a 'Research summary' is listed as one of six Artifact types Condens' tool supports, with a single descriptive sentence and no section list of any kind. No page anywhere on condens.io (checked via full sitemap and two targeted site searches) is titled or structured as a 'Summary of Findings' template or example with an orderable section list. Supports the not_found entry for question 10, nothing else
Quotable: "It gives you the opportunity to integrate raw data - such as video clips and audio recordings - into the final reports, which can significantly enhance your audience's engagement."
Quotable: "When working with Artifacts, it's important to prioritize their intended purpose. For example, if you're crafting a report for stakeholders, start by identifying the information most relevant to them and consider whether a streamlined and minimalistic report would be enough, or if a more detailed and visual presentation could capture their attention better."
Quotable: "Many teams include recommendations in their reports, so ensuring they reach the right audience is essential. If your reports tend to be rather lengthy, consider adjusting how you present your recommendations. Rather than listing them all at the end, include a recommendation after each finding throughout the report, while still including the summary at the conclusion."
Quotable: "Instead of a one-size-fits-all report, you can create tailored content - concise summaries for executives who need quick takeaways, and in-depth reports for product and design teams looking for detailed insights."
Quotable: "Before creating your reports, always keep your audience in mind to ensure that the information included is relevant and actionable for them."
Quotable: "Research summary: to summarise your findings and observations and make it easy to share with the rest of your organization"
Quotable: "While no universal Artifact format can fit every organization or team, Condens provides a set of templates commonly used in UX Research that can spark your creativity and help you get started."

### Evidence, counts, severity, and the line from finding to recommendation

**[16] Amy Schade - "Making Usability Findings Actionable: 5 Tips for Writing Better Reports" (Nielsen Norman Group).** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/actionable-usability-findings/`
Supports: How a finding should be phrased (specific, design-focused, not user-blaming), ranking findings by severity, and including positive findings alongside problems
Quotable: "A finding of “Registration was hard” doesn’t identify the problem or hint at solutions."
Quotable: "Findings need to be specific: “The button to register for the site had poor color contrast and faded into the page background.”"
Quotable: "Findings should explain the elements of the design that confused users or led them down the wrong path."
Quotable: "Ranking findings as low, medium or high severity helps the team understand what critical issues the usability study exposed."
Quotable: "Don’t forget to include positive findings as well, letting the team know what’s already working."
Quotable: "But present recommendations as recommendations."

**[17] Jakob Nielsen - "Severity Ratings for Usability Problems" (Nielsen Norman Group).** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/`
Supports: The canonical 0-4 severity scale, its three components (frequency, impact, persistence), and the practice of collecting ratings from multiple evaluators after a heuristic evaluation session
Quotable: "The following 0 to 4 rating scale can be used to rate the severity of usability problems:"
Quotable: "0 = I don’t agree that this is a usability problem at all"
Quotable: "1 = Cosmetic problem only: need not be fixed unless extra time is available on project"
Quotable: "2 = Minor usability problem: fixing this should be given low priority"
Quotable: "3 = Major usability problem: important to fix, so should be given high priority"
Quotable: "4 = Usability catastrophe: imperative to fix this before product can be released"
Quotable: "The frequency with which the problem occurs: Is it common or rare?"
Quotable: "The impact of the problem if it occurs: Will it be easy or difficult for the users to overcome?"
Quotable: "The persistence of the problem: Is it a one-time problem that users can overcome once they know about it or will users repeatedly be bothered by the problem?"
Quotable: "severity ratings can be collected by sending a questionnaire to the evaluators after the actual evaluation sessions"
Quotable: "it is important to note that each evaluator should provide individual severity ratings independently of the other evaluators"
Quotable: "My experience indicates that severity ratings from a single evaluator are too unreliable to be trusted."
Quotable: "using the mean of a set of ratings from three evaluators is satisfactory for many practical purposes"

**[18] Kate Moran - "Qualitative Usability Testing: Study Guide" (Nielsen Norman Group).** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/qual-usability-testing-study-guide/`
Supports: Confirms the roughly-five-participants-per-group recommendation as the sample-size convention this bundle's findings rest on; the page itself is a curated reading list, not a prose guide, so it supports existence of the recommendation only
Quotable: "Why we recommend conducting qualitative usability testing with about 5 participants per user group"

**[19] Rachel Krause - "Creating Engaging Reports & Asynchronous Presentations" (Nielsen Norman Group).** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/engaging-reports-presentations/`
Supports: Using participant quotes and video clips as evidence, and the caution that anecdotes must illustrate data rather than replace it
Quotable: "Is there a quote or video clip of a user making this point that I could use?"
Quotable: "Anecdotes trigger an emotional reaction and will spark empathy from your audience. This isn’t to say that you should rely only on anecdotes though. Anecdotes can lead to narrative bias, so it’s best to use them to illustrate or support your data."
Quotable: "Couple your numerical data (top) with an anecdote or two (bottom) to remind your audience that there are real people behind the numbers."

**[20] Brian Utesch and Tammi Fitzwater - "Insights Aren't Outcomes: Research Recommendation Breakage" (Nielsen Norman Group).** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/research-recommendation-breakage/`
Supports: The chain from data to finding to insight to recommendation, and the claim that a recommendation is the point where an insight becomes a specific, actionable fix
Quotable: "Data leads to findings, which build insights, which justify recommendations."
Quotable: "When the process is working, researchers’ recommendations transition from insights into specific fixes that improve the user experience."
Quotable: "Insights and recommendations generated by research teams are useful only if they bridge the divide between research and outcomes and are translated into action."
Quotable: "Recommendations are the highest-value output in the research process. We collect data, derive findings, uncover insights, and finally craft recommendations."

**[21] Sara Paul - "Data vs. Findings vs. Insights" (Nielsen Norman Group, video page).** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/videos/data-findings-insights/`
Supports: A one-sentence, named definition distinguishing data, findings, and insights; the video itself is not transcribed on the page, so only the summary line is verified text
Quotable: "Data refers to unanalyzed user observations, findings capture patterns among data points, and insights are the actionable opportunities based on research and business goals."

**[22] Jeff Sauro, PhD - "What Goes into a Usability Test Plan?" (MeasuringU) - report outline section only.** practitioner. **fetched-and-verified.**
`https://measuringu.com/usability-test-plan/`
Supports: MeasuringU's recommended report outline, verbatim and in order, as requested in question (h)
Quotable: "If possible, try to outline how the report will be structured in the test plan."
Quotable: "Study Overview"
Quotable: "Findings Summary"
Quotable: "Participant Profiles & Demographic Summaries"
Quotable: "Task Metrics"
Quotable: "Usability Issues by Task and Recommendations"
Quotable: "Test Metric Summary"
Quotable: "Appendix & Verbatims"

**[23] Jeff Sauro, PhD and Jim Lewis, PhD - "You Can Report Percentages with Small Samples, but Should You?" (MeasuringU).** practitioner. **fetched-and-verified.**
`https://measuringu.com/should-you-avoid-reporting-percentages-from-small-sample-studies/`
Supports: Whether and how to report percentages from small qualitative/usability samples, including the fraction-vs-percentage format question raised in (b)
Quotable: "it’s completely permissible from a statistical perspective to report numbers when studies have very small sample sizes (fewer than ten people)"
Quotable: "5 (simple count)"
Quotable: "5/7 (fraction)"
Quotable: "71% (percentage)"
Quotable: "5 (71%) (simple count + percentage)"
Quotable: "5/7 (71%) (fraction + percentage)"
Quotable: "The information in the fractions is valuable to readers because the denominator shows whether the corresponding percentage was based on a small, medium, or large sample size."
Quotable: "Unless this information appears elsewhere in your report, we recommend presenting fractions."
Quotable: "We encourage you to report percentages."
Quotable: "Should you report percentages from small sample studies?… Yes, you should."
Quotable: "Limits to generalization: You can’t manipulate all possible variables in a single experiment."

**[24] Jeff Sauro, PhD - "Best Practices for Using Statistics on Small Sample Sizes" (MeasuringU).** practitioner. **fetched-and-verified.**
`https://measuringu.com/small-n/`
Supports: The generalization limits of small-sample usability data and the use of confidence intervals rather than bare point estimates
Quotable: "Some people think that if you have a small sample size you can’t use statistics. Put simply, this is wrong, but it’s a common misconception."
Quotable: "it’s important to know that there are limitations to these smaller sample studies: you are limited to seeing big differences or big “effects.”"
Quotable: "the key limitation is that you are limited to detecting large differences between designs or measures"
Quotable: "with five users attempting a task, the only possible outcomes are 0%, 20%, 40%, 60%, 80% and 100% success"
Quotable: "There’s something about reporting perfect success at this sample size that doesn’t resonate well. It sounds too good to be true."
Quotable: "even the “best” single estimate will still differ from the actual average, so using confidence intervals provides a better method for estimating the unknown population average"

**[25] Jeff Sauro, PhD - "7 Steps to Conducting Better Qualitative Research" (MeasuringU).** practitioner. **fetched-and-verified.**
`https://measuringu.com/qualitative-steps/`
Supports: Reporting counts of supporting participants alongside findings, using verbatims to validate findings, and disclosing researcher bias as a limitation
Quotable: "Creating a system for coding actions and notable quotes helps speed through the process of turning utterances into actionable insights."
Quotable: "Having recordings of sessions and detailed notes helps other interested parties come to their own conclusions and can help validate findings. Including verbatims along with the interpretation also helps others see how the conclusions were drawn."
Quotable: "One approach to minimize this researcher bias is to include a section on the interviewer or principal investigator’s background and how it might influence their conclusions."
Quotable: "We start with the most important findings, and then note the number of participants that supported these findings and some good quotes to support what we concluded."
Quotable: "We also provide confidence intervals around the issue and insight frequency so readers have some idea about the prevalence of an issue in the larger user population."

**[26] Jeff Sauro, PhD - "Rating the Severity of Usability Problems" (MeasuringU).** practitioner. **fetched-and-verified.**
`https://measuringu.com/rating-severity/`
Supports: Multiple named severity-scale traditions (Nielsen, Rubin, Dumas & Redish, Wilson, Molich & Jeffries), the practice of multi-evaluator independent rating, treating frequency separately from severity, and the direct instruction to include positive findings
Quotable: "Accounting for problem frequency and severity are two critical ingredients when communicating the importance of usability problems."
Quotable: "Take the number of users that encounter a problem divided by the total number of users. For example, if 1 out of 5 users encounter a problem, the problem frequency is .20, or 20%."
Quotable: "0 = I don’t agree that this is a usability problem at all ... 4 = Usability catastrophe: imperative to fix this before product can be released"
Quotable: "So we reduced our severity scale to just three levels, along with one for insights, user suggestions or positive attributes."
Quotable: "Insight/Suggestion/Positive: Users mention an idea or observation that does or could enhance the overall experience."
Quotable: "There will still be inter-rater disagreement and judgment calls: ... One of the best approaches is to have multiple evaluators rate the severity independently, calculate the agreement, and then average the ratings."
Quotable: "Don’t forget the positives: Dumas, Molich & Jeffries wrote a persuasive article talking about the need for pointing out positive findings."
Quotable: "Treat frequency separately from severity: We report the frequency of an issue along with its severity. When possible, we have a separate analyst rate the severity of a problem without knowing its frequency"

**[27] Nikki Anderson-Stanier - "To Ask or Not to Ask? How to Design Research for Difficult Questions" (dscout).** practitioner. **fetched-and-verified.**
`https://dscout.com/people-nerds/difficult-question-methods`
Supports: Naming a research question as unanswerable by the chosen method; this is design-time scoping advice, not guidance on how to state an unanswered question inside a finished report
Quotable: "There are questions out there that qualitative, and even quantitative, research simply cannot answer and we need to let our teams know when a question is unanswerable."
Quotable: "I learned the lesson of “No, but...” and it was one of the most powerful lessons I ever encountered."
Quotable: "We can’t distill preference with small sample sizes."

### Practice: who writes a report, who reads it, and where practice disagrees

**[28] GitLab (company UX Research Operations team) - "Resources for Research DRIs," The GitLab Handbook.** practitioner. **fetched-and-verified.**
`https://handbook.gitlab.com/handbook/product/ux/ux-research/resources-for-research-dris/`
Supports: (a) who writes a report - PMs and designers routinely conduct and write up research themselves, with a UX researcher in a supporting role; describes the reporting step and its format and review process
Quotable: "UX Researchers are one of the many GitLab Team Members who conduct user research. Other roles, such as Product Managers and Product Designers, frequently conduct research with guidance from the UX Research team."
Quotable: "In GitLab, anyone can be the DRI of a UX Research project. If the Research DRI is not a UX Researcher, they are partnered with a UX Researcher acting in a supporting role."
Quotable: "The Research DRI, and their UX Researcher partner if applicable, synthesise findings, validate key takeaways, and create the report."
Quotable: "Though Google Slides is the most popular format, the report can really be in any form, for example, a doc, an issue, a board, or an diagram."
Quotable: "It should be put through a peer review process in the ux_research_team_lounge channel. The peer review may results in further analysis."
Quotable: "The final report is shared in the ux_research_reports channel (using the template in the research issue itself), and any other relevant channels and sync meetings."
Quotable: "It is expected that stakeholders and / or the Research DRI will follow up the report by identifying and issuing actionable insights for the Product and Design team to action on."

**[29] Itamar Gilad - "Idea Validation Using the AFTER Model," itamargilad.com.** practitioner. **fetched-and-verified.**
`https://itamargilad.com/idea-validation-much-more-than-just-a-b-experiments/`
Supports: (h) Gilad's definition that separates a usability test from an experiment, with his own qualifier that this is a nonstandard, deliberately chosen definition
Quotable: "Experiments are tests that include a control element to guard against false results caused by random chance."
Quotable: "Per this definition an A/B test is an experiment, but a usability test is not."
Quotable: "I realize that this is not the common definition used in the industry - in many cases the words test and experiment are used interchangeably. I chose this definition because it's closer to how scientists think of experiments."
Quotable: "Usability tests - In Usability Tests we ask users to try using the product under the supervision and guidance of a tester. We may use interactive mockups, a code prototype, or an actual product. In all cases we'll try to make the user interface look reasonably realistic, but in early tests the functionality may be limited and we may use canned data."

**[30] Junu Yang - "Customer Research Reports Nobody Reads (And How to Fix That)," Usercall blog.** vendor. **fetched-and-verified.**
`https://www.usercall.co/post/customer-research-reports-guide`
Supports: (d) why reports go unread and what makes a report change a decision; (e) evaluative (live-product) reports going stale the moment a decision or a redesign overtakes them; (b)/contested - argues reports mostly fail yet still recommends writing one
Quotable: "I've written probably 200 customer research reports in my career. I'd guess 150 of them got opened once, skimmed for the executive summary, and then quietly died in a shared drive."
Quotable: "Most customer research reports are built to prove that research happened, not to actually change anything."
Quotable: "If your report doesn't end in a decision or a debate about a decision, you haven't written a report, you've written a diary."
Quotable: "They lead with the decision, not the methodology."
Quotable: "They tie every claim to evidence the reader can verify in seconds, usually a quote or a clip, not a paraphrase buried in an appendix."
Quotable: "They're scoped to one audience."
Quotable: "First, the research happens too late. By the time the report lands, the roadmap decision has already been made informally in a Slack thread."
Quotable: "It still got shelved because it landed two weeks after the pricing decision was finalized. The insight wasn't wrong, it was just late."
Quotable: "the report is a snapshot instead of a system. It answers one question at one point in time, then it's obsolete the moment the market shifts."
Quotable: "I've started defaulting to producing at least two formats from every study: a full report for the record, and a one-page brief or clip reel for the people who will never open the PDF."
Quotable: "Here's the test I use now before I ship any report: if I deleted the report entirely and just told the stakeholder the headline finding in a hallway conversation, would they act differently? If the answer is no, the report has failed regardless of how well it's written or designed."

**[31] Junu Yang - "Research Operations Is the Reason Your Insights Team Either Ships Fast or Falls Apart," Usercall blog.** vendor. **fetched-and-verified.**
`https://www.usercall.co/post/research-operations-guide`
Supports: (a) PMs running their own unsynthesized interviews with no shared report or repository; (c) report vs. repository both failing without an enforced single source of truth
Quotable: "every PM ran their own "user interviews" whenever they felt like it. No shared repository, no consistent screener, no synthesis process."
Quotable: "They had run 140 customer conversations. Nobody could tell me what had actually been learned across all of them because nothing was centralized or synthesized."
Quotable: "Insights get reported once in a deck and then never referenced again"
Quotable: "Your research repository, if it exists, is a shared drive folder nobody opens"
Quotable: "Pick one repository and enforce it. It doesn't need to be fancy. It needs to be the single place people check before starting new research."
Quotable: "the biggest unlock wasn't a new tool, it was picking one repository and actually enforcing that people use it."

**[32] Kevin (Founder & CEO) - "Consumer Insights Reports: What Executives Actually Read," User Intuition Reference Deep-Dive.** vendor. **fetched-and-verified.**
`https://www.userintuition.ai/reference-guides/consumer-insights-report-structure-what-executives-read/`
Supports: (d) why reports go unread and what makes a report change a decision; (f)/(c) connecting a single report to a cumulative, dated intelligence base rather than treating it as a standalone snapshot
Quotable: "The research team optimized for comprehensiveness when they should have optimized for decision velocity."
Quotable: "Failure 4: The recommendation gap. The report describes what was found but does not state what should be done. ... An insight without a recommendation is an intellectual exercise. An insight with a recommendation is a decision input."
Quotable: "Would this report change a decision? If the answer is no - if the findings are interesting but do not alter what the organization plans to do - the report should either not be written or should be repositioned as a knowledge-building study rather than a decision-driving one."
Quotable: "Individual reports become exponentially more valuable when they connect to a cumulative intelligence base. Each report should reference prior findings - confirming, contradicting, or extending what the organization learned previously."
Quotable: "The consumer insights report template should include a required field for "Related Prior Research" that forces the connection between new findings and existing knowledge. This field prevents the common pattern of research teams rediscovering insights that were already documented but forgotten."
Quotable: "Reports designed as standalone documents become obsolete immediately; reports designed as intelligence system inputs accumulate value over time."

**[33] Bence Mózer, Tamás Virágh, Dan Damsa - "Atomic research principles for building a sustainable research repository," UX studio blog.** vendor. **fetched-and-verified.**
`https://www.uxstudioteam.com/ux-blog/atomic-research-principles-for-building-a-sustainable-research-repository`
Supports: (c) atomic research nuggets as the alternative unit to a one-study report - a labelled, tagged observation that findings and insights are built up from, re-used across multiple studies
Quotable: "A nugget is a labelled observation supported by evidence. It's a single-experience insight from the experience of a particular customer."
Quotable: "Nuggets are organised with tags in a research repository."
Quotable: "In atomic research, nuggets are combined to form findings that lead to certain conclusions. In this approach, multiple findings can be supported by the same nugget."
Quotable: "Depending on the case, a finding may be confirmed - or infirmed - more than once because there are multiple nuggets associated with it. This can build confidence in the insight."
Quotable: "The element at the core of the atomic research approach is the nugget"

**[34] Chris Massey, writing up a talk by Julia Shalet ("The Product Doctor") - "DIY User Research for Product People," Mind the Product.** practitioner. **fetched-and-verified.**
`https://www.mindtheproduct.com/diy-user-research-for-product-people/`
Supports: (a) product managers doing their own user research without a UX researcher or designer on the team, as a stated premise of the toolkit (does not itself discuss writing a report, only running the research)
Quotable: "Julia offers a toolkit for those product managers who don't have a UX designer or researcher in their team, and want to do user research themselves."
Quotable: "Act, record and start again ... Track every experiment, and track the data. Share the findings within the team and across the business."

**[35] Jeff Humble (Designer & Co-Founder, The Fountain Institute) - "This could have been shorter," The Fountain Institute newsletter.** practitioner. **fetched-and-verified.**
`https://pages.thefountaininstitute.com/posts/this-could-have-been-shorter`
Supports: (a) a designer doing and writing up their own research, told in first person; (b)/(d) why reports go unread, with a named practitioner arguing for abandoning the static-report format
Quotable: "Ironically, I was a designer doing research, and my research report was completely undesigned. I turned off my design brain and sent out a barely-formatted report."
Quotable: "That same boss used to print out research reports she wanted me to read. She would leave them on my desk because she knew that was the only thing that worked."
Quotable: "We do that because we know the truth… nobody reads. At best, people skim"
Quotable: "Your research report is like any piece of content. If it's too hard to consume, people won't."
Quotable: "It's easy to complain that nobody does research, but it's hard to do something about it."
Quotable: "if you're bringing the team into research activities, you don't have to make a research report ever again."
Quotable: "Until next week, stop reporting and start inspiring!"

**[36] Dr Asma A Qureshi / Crystal Chin (quoted practitioners) - Ethnio editorial team, "Generative vs Evaluative Research Methods," Ethnio blog.** vendor. **fetched-and-verified.**
`https://ethn.io/blog/generative_vs_evaluative_research_methods`
Supports: (e) the generative-vs-evaluative distinction itself (purpose, design stage, methods, outcome); the article compares the two research modes, not the two report types specifically, so it supports the underlying distinction the report dimension rests on rather than a report-writing claim
Quotable: "Typically uses quantitative methods to assess the success or failure of a specific product/feature and identify necessary improvements."
Quotable: "Typically uses qualitative methods to understand user needs and motivations to inspire design and product development innovation."
Quotable: "Measure existing design."
Quotable: "Uncover new insights and opportunities related to user needs and behaviors."
Quotable: "Later stages (post-design completion, iteration)."
Quotable: "Early stages (ideation, concept development)."
Quotable: "Improved usability and design validation."
Quotable: "New insights, ideas, and opportunities informing design direction."

### The gap question: what good reports add

**[37] Useberry (vendor blog, unsigned) - "Stakeholder Buy-In for UX Research: Templates, Timelines, and Talking Points".** vendor. **fetched-and-verified.**
`https://www.useberry.com/blog/stakeholder-buy-in-for-ux-research-templates-timelines-and-talking-points/`
Supports: A report should name the decision it supports and who owns that decision, and should state in advance what happens if findings are split or inconclusive
Quotable: "Lead with decisions, then show the evidence."
Quotable: "Capture what each group values, how they prefer to consume information, and which decisions they own."
Quotable: "assign a name and date to each recommendation during the presentation"
Quotable: "Include a line on what happens if findings split or are inconclusive."
Quotable: "If we see X, we will recommend A. If we see Y, we will recommend B."
Quotable: "overpromise on the results so nobody is surprised when you recommend a follow-up"

**[38] Userfeel (vendor blog, unsigned) - "Optimizing Your Usability Testing Process with Report Templates".** vendor. **fetched-and-verified.**
`https://www.userfeel.com/blog/optimizing-your-usability-testing-process-with-report-templates`
Supports: A report's Findings section should open with a positive finding even when it ranks lower in priority, and its Discussion section should name questions the test raised that a future study should investigate
Quotable: "although it can help to start with a positive finding even if it's less important"
Quotable: "further questions that arose from the test and how they could be investigated in the future"
Quotable: "Discuss any concerns you have about your methods"

**[39] CleverX (vendor blog, unsigned) - "Research Repository Template: Build Your Own in 2026".** vendor. **fetched-and-verified.**
`https://cleverx.com/blog/research-repository-template-build-your-own-in-2026/`
Supports: Raw research data (recordings, transcripts, identifiable participant records) needs a named storage location, a retention/expiry policy, and participant de-identification via an anonymised ID - adjacent to, but describing repository metadata rather than a one-study report itself
Quotable: "identifiable participant data (names, emails) deleted within 12 months; transcripts and recordings retained for 24 months"
Quotable: "the date after which raw data should be deleted per policy"
Quotable: "Never store personally identifiable information in the main studies database."
Quotable: "Cloud folders with role-based access (Google Drive, SharePoint, S3)"
Quotable: "store recordings alongside transcripts and link them directly to insight clips"
Quotable: "2026-05-14_S042_ModInt_P07"

**[40] CleverX (vendor guide, unsigned) - "Research Participant Consent Best Practices: A Practical Guide for User Research Teams".** vendor. **fetched-and-verified.**
`https://cleverx.com/guides/research-participant-consent-best-practices-a-practical-guide-for-user-research-teams`
Supports: Consent to quote a participant in a report should be granular (separate checkboxes for recording types and for internal-report vs. published-case-study quote use), and using a specific quote or clip needs explicit permission referencing that exact content, with the participant's identity stripped from the report
Quotable: "Do not bundle everything into a single "I agree" signature. Participants should be able to opt in or out of specific elements."
Quotable: "I consent to anonymized quotes being used in internal reports"
Quotable: "I consent to anonymized quotes being used in published case studies"
Quotable: "Consent for the study is separate from consent to be contacted. Collect study-specific consent before each session."
Quotable: "If you want to use a specific quote or clip, get explicit permission referencing the exact content"
Quotable: "Your name and identifying information are removed from all reports and findings"
Quotable: "In practice, this means being able to locate and delete a specific participant's recordings, transcripts, and any quotes used in reports."

**[41] Digital Government Hub (Georgetown University's Beeck Center) - "Obtaining Consent for User Research".** practitioner. **fetched-and-verified.**
`https://digitalgovernmenthub.org/library/obtaining-consent-for-user-research/`
Supports: Reinforces, from a university-affiliated public-sector research hub, that consent governs what happens once quotes are transcribed and shared with the team, and that undisclosed uses of participant data are an ethical concern - a weaker, more general echo of the CleverX consent findings; adds nothing new on attribution mechanics
Quotable: "as soon as you transcribe quotes from that call or share that person's information with other people on your team"
Quotable: "Informed consent is a fundamental part of an ethical research program"

### Pages the first pass referenced and a second pass read

**[42] Dovetail - "How to create a research findings deprecation policy that keeps your insight repository current and trustworthy".** vendor. **fetched-and-verified.**
`https://dovetail.com/research/research-findings-deprecation-policy-insight-repository/`
Supports: Fails the one-study test for the report-dating question. The entire article is scoped to a research REPOSITORY holding many findings from many studies (a three-state Active/Flagged/Archived model, quarterly review cadences, a repository owner role), not to anything a single study's own report should say about itself. It supports only the repository-level practice of dating and re-checking findings, which the one-study test excludes for this bundle
Quotable: "A deprecation policy is the mechanism that prevents this. It establishes clear rules for when research findings should be flagged, reviewed, and eventually archived."
Quotable: "Most teams benefit from a simple three-state model: Active - The finding is considered current and reliable. Teams can reference it with confidence. Flagged - The finding has been identified for review. It may still be valid, but its currency is uncertain. Anyone referencing it should verify before acting. Archived - The finding is no longer considered current."
Quotable: "Time elapsed. Any finding older than a defined threshold (e.g., 12 or 18 months) is automatically flagged for review."
Quotable: "The goal is not to erase history. Archived findings remain valuable for trend analysis, longitudinal comparison, and institutional memory. But they must be clearly separated from active, decision-ready insights."

**[43] Dovetail - "How to run effective research debriefs with product trios that lead to shared understanding and aligned next steps".** vendor. **fetched-and-verified.**
`https://dovetail.com/product-development/research-debriefs-product-trios-shared-understanding/`
Supports: Supports the debrief-vs-report question. Argues the debrief, not the written report, is where shared understanding actually forms, but does not claim teams eliminate written documentation: it still instructs researchers to document debrief outcomes afterward. A pre-read for the debrief lists elements (research questions, participants, method/limitations, 3-5 preliminary observations) that map closely onto a report's own front matter
Quotable: "There is a persistent assumption in product organizations that the primary output of research is a report or a presentation. But reports are artifacts. Understanding is the actual output, and understanding is built through conversation, not consumption."
Quotable: "Research that never leaves the researcher's head is research that never happened."
Quotable: "Document the key takeaways and decisions from every debrief and store them somewhere the team can reference later."
Quotable: "A weekly or biweekly 45-minute session where the trio reviews recent evidence together can be more valuable than a quarterly research readout."
Quotable: "The research questions the study aimed to answer"
Quotable: "Who was involved (number of participants, relevant segments)"
Quotable: "The method used and any important limitations"
Quotable: "Three to five preliminary observations (framed as observations, not recommendations)"

**[44] Dovetail - "How to document and share research debriefs asynchronously for distributed product teams".** vendor. **fetched-and-verified.**
`https://dovetail.com/research/async-research-debriefs-distributed-teams/`
Supports: Strong, directly on point for the debrief-companion-vs-substitute question. States plainly that async debriefs are not a blanket replacement for live discussion, and explicitly distinguishes a 'debrief' document from a 'research report for peer review' as different genres for different audiences. Gives a verbatim suggested template section list for the debrief document that maps closely onto a one-study report's own structure
Quotable: "Async debriefs are not a blanket replacement for all live conversation about research."
Quotable: "In these cases, the async debrief still serves as the foundation. Share the document first, give people time to read and reflect, then hold a focused live session for discussion."
Quotable: "Writing for yourself instead of your audience. A debrief is not a research report for peer review. Write for the product managers, designers, and engineers who will use the findings."
Quotable: "A simple template might include:"
Quotable: "Research objective"
Quotable: "Method and participants"
Quotable: "Executive summary"
Quotable: "Findings by theme (with evidence)"
Quotable: "Recommendations"
Quotable: "Open questions for the team"
Quotable: "What was the research objective? State the question or problem the research set out to address. One or two sentences is usually enough."
Quotable: "What method did you use? Interviews, usability tests, diary studies, surveys-name the method and briefly explain why it was appropriate."
Quotable: "Who participated? Describe the participants at a high level: how many, how they were recruited, and any relevant characteristics (e.g., "8 enterprise customers who have used the product for more than 6 months")."
Quotable: "When did the research take place? This helps readers assess how current the findings are."
Quotable: "Should async debriefs replace live debrief sessions entirely? Not necessarily."

**[45] Dovetail - "Comparing research synthesis methods: atomic research vs. thematic analysis vs. affinity mapping".** vendor. **fetched-and-verified.**
`https://dovetail.com/research/atomic-research-vs-thematic-analysis-vs-affinity-mapping/`
Supports: Partial support only. Confirms that thematic analysis is the method typically behind 'a report that will inform a significant product or strategic decision,' and that its output 'is typically a report or presentation tied to a specific study' -- satisfying the one-study test for that strand. But it never states that the finished report itself must name the synthesis method or the analyst who performed it; its one instruction to 'document your reasoning' is aimed at the researcher's own working notes, not the deliverable. The who-performed-it half of the question returns null
Quotable: "You are producing a report that will inform a significant product or strategic decision"
Quotable: "The output is typically a report or presentation tied to a specific study. Without additional work to extract and store the findings in a reusable format, the insights can become trapped in a document that nobody revisits after the initial readout."
Quotable: "Document your reasoning. When you group codes into themes, merge clusters, or link a fact to an insight, write down why. Your future self (and your colleagues) will thank you."
Quotable: "You are working with a single study and need quick, shared understanding"

**[46] Awkward Silences #172 - Summer Throwback: Caitria O'Neill on the Problems of Research Reports (transcript).** practitioner. **fetched-and-verified.**
`https://podcast.userinterviews.com/episodes/throwback-no-one-reads-your-reports/transcript`
Supports: Directly on point. Caitria O'Neill names three qualities a research report needs -- enjoyable, informative, actionable -- and explains why a report that isn't read has no impact regardless of its insight quality, why 'informative' (explaining the why, not just the what) is the single most important of the three, and what makes a report actually change a decision: clear, near-term recommendations the stakeholder can act on, stated up front and recapped at the end, alongside explicit open questions and next steps rather than a final decision
Quotable: "If you write a report that people don't want to read and don't read, it doesn't have any impact, even if it had the best possible insights in it."
Quotable: "So making it a report informative means not just saying the what, so that's like, you know, four of X users had trouble finding this, but the Y."
Quotable: "I think overall to answer the question, informative is the most important thing you can do as a researcher."
Quotable: "But once it has to be a very clear recommendation and that push to make sure that people actually come back and act on it, even if they enjoy the whole deck and your memes doesn't mean anything if they don't walk away with clear next steps to work with it."
Quotable: "People need to put the dates, their names and contact information and what the study concerned."
Quotable: "The other is a TLDR. So that upfront list of, if you don't have any other time, these are the things I really need you to know."
Quotable: "I'm like, okay, the next session needs to test these open questions. We still don't know X, Y, and Z. And then I'll say like the next step for the product team is to give me mocks that help us text X, Y, and Z."

**[47] Maze - "Evaluative Research: Key Methods & Examples" (chapter 5 of "What is UX Research: The Ultimate Guide").** vendor. **fetched-and-verified.**
`https://maze.co/blog/evaluative-specialization/`
Supports: Partial support. Clearly distinguishes evaluative from generative research by purpose, timing, focus, methods, and a worked example, and situates both as research-stage categories. Returns null on the second half of the assigned question: the page never states whether the WRITTEN REPORT itself should differ in structure or content between an evaluative and a generative study -- it only differentiates the research activity, not the reporting document
Quotable: "Generative research helps identify user needs and opportunities before design begins"
Quotable: "Evaluative research assesses whether the final product meets user expectations and performs well"
Quotable: "Evaluative research assesses and validates existing designs for improvements"
Quotable: "Generative methods investigate user needs for new solutions"
Quotable: "Generative research helps us deeply understand our users and learn their needs, wants, and challenges. On the other hand, evaluative research helps us test whether the solutions we've come up with address those needs, wants, and challenges."

**[48] UserTesting blog - "Generative vs. evaluation research".** vendor. **fetched-and-verified.**
`https://www.usertesting.com/blog/generative-vs-evaluation-research`
Supports: Second vendor's take on the same distinction, same partial-support pattern as the Maze source: a clean comparison of purpose, timing, and methods, plus named epigraphs from UX practitioners, but no statement anywhere on the page about whether the deliverable report differs in form between the two research types
Quotable: "Generative research dives into 'What problem might we solve?' while evaluative research asks, 'How well is our solution working?'"
Quotable: "To summarize, generative research:"
Quotable: "Focuses on understanding user needs, behaviors, and motivations"
Quotable: "Alternatively, evaluative research:"
Quotable: "Centers around assessing a product's effectiveness, impact, and user satisfaction"
Quotable: "Generative research: Typically uses qualitative methods to understand user needs and motivations to inspire design and product development innovation. Evaluative research: Typically uses quantitative methods to assess the success or failure of a specific product/feature and identify necessary improvements."
Quotable: "Generative vs. evaluative research: Why not both?"

**[49] GOV.UK Service Manual - "Managing user research data and participant privacy".** standards. **fetched-and-verified.**
`https://www.gov.uk/service-manual/user-research/managing-user-research-data-participant-privacy`
Supports: Strong, direct support for all three sub-questions: anonymising quotes/clips/screenshots before sharing, where raw data should live, and how long it should be kept. Official UK government service-manual guidance, published 5 November 2018, addressed to anyone 'reporting findings publicly' or sharing 'research outputs' generally -- broad enough to cover a single study's report
Quotable: "Whenever you can, you should fully anonymise the extracts you use so that the participants cannot be identified."
Quotable: "Whether or not you fully anonymise an extract, we recommend that you always remove or obscure:"
Quotable: "direct personal identifiers - such as names or badge numbers"
Quotable: "contact details - such as addresses and phone numbers"
Quotable: "other confidential information - such as bank account details"
Quotable: "We suggest 2 or 3 years as reasonable retention periods for user research data - but delete it sooner if it's no longer needed."
Quotable: "Keep your research data only in places that your organisation has approved for storing personal data. For example, user researchers in GDS and other government organisations use Microsoft OneDrive."
Quotable: "If you do make user research findings public, make sure that you remove participants' personal data and fully anonymise any research data you use to illustrate your findings."
Quotable: "It's best not to make public any non-anonymised research outputs. Once others have downloaded and copied the outputs, it is difficult to find and destroy the personal data if a participant withdraws their consent."

**[50] Jeff Sauro, PhD and Jim Lewis, PhD - "An Intro to Bayesian Thinking for UX Research: Updating Beliefs with Data" (MeasuringU, February 24, 2026).** practitioner. **fetched-and-verified.**
`https://measuringu.com/intro-to-bayesian-thinking-in-ux-research`
Supports: Strong, direct support, and passes the one-study test cleanly: the article's own worked example is a single hypothetical 20-participant usability test, walking through a prior belief (historical 78% completion rate), the data observed (18/20 completions), the updated posterior belief (~86%), and a stated confidence level (95% credible interval of ~72%-96%; ~89% probability the true rate exceeds 78%). This is exactly the prior-belief / posterior-belief / confidence pattern the question asks about, applied to one study's result
Quotable: "Our original belief is called the prior hypothesis (before). The belief we have after observing data and calculating an update is our posterior belief (after)."
Quotable: "The Bayes' formula means that beliefs that better predict the data become more credible; beliefs that predict the data poorly lose credibility."
Quotable: "Our updated best estimate of the true completion rate is about 86%"
Quotable: "A 95% credible interval runs from roughly 72% to 96%"
Quotable: "There's about an 89% probability that the true completion rate exceeds 78%."
Quotable: "The prior kept us from overreacting to just twenty observations."

### Pages the maintainer read by hand

**[51] Mozilla UX blog (Jennifer Davidson, with Julia Starkov, Jim Thomas, Marissa (Reese) Wood and Michael Verdi) - "Reflecting on 'It's Our Research' at Mozilla" (December 18, 2019).** practitioner. **fetched-and-verified, read by hand by the maintainer on 2026-10-27.**
`https://blog.mozilla.org/ux/2019/12/reflecting-on-its-our-research-at-mozilla/`
Supports: An in-house research team's account, from Firefox user research, of how its reports reach stakeholders. The executive summary: what it is (a few sentences, or one slide in a deck), that it is the hardest part of a study, a VP of Product on why a document without a good one goes unread, and the team's move to shorter summaries with clear takeaways and calls to action for each report. That debriefs are not analysis. Stakeholders, a product manager and two designers among them, taking part in field research and analysis that a user researcher led, with Tomer Sharon's advice quoted second-hand. It does not show product managers writing their own reports
Quotable: "Stakeholders come to research studies, listen attentively to research report-outs, and generally value the work our team does."
Quotable: "An executive summary is a few sentences, maybe one slide (if it’s in slide format) that summarizes a research study."
Quotable: "I’ll tell you - it is the hardest part of a research study."
Quotable: "The purpose of an executive summary is to describe the main and important points of your document in such a way that it will engage the readers."
Quotable: "In short, without a good executive summary, the document will likely not get the attention it deserves."
Quotable: "without an executive summary, people may not pay any attention to the study results (a researcher’s worst nightmare!)."
Quotable: "So over the past year, the Firefox UR team has been iterating on our executive summary style, to better fit the needs of our current executives."
Quotable: "We try to be more succinct with our executive summaries than before, with clear takeaways and calls to action for each report."
Quotable: "A debrief includes those precious moments immediately after interviewing a participant or visiting a participants’ home. They capture your first reactions after the experience."
Quotable: "Notably, debriefs are not analysis. They may start the analysis juices going, but analysis is much more in-depth and complex."
Quotable: "Sharon recommends analyzing results together with stakeholders."
Quotable: "Stakeholders are more likely to act upon study results because they participated in the study’s development"
Quotable: "We don’t always involve stakeholders in analysis, particularly if the timing is tight."
Quotable: "As a Product Manager, I know how important it is to spend time connecting with your users, learning how they think about your product, observing what they do and how they react."
Quotable: "All the process was handled for me so I was able to focus on my most important goal: learning about our users and their perspectives."

**[52] Koji (docs) - "How Long Is User Research Valid? Insight Decay and When to Re-Run a Study".** vendor. **fetched-and-verified, read by hand by the maintainer on 2026-10-27.**
`https://www.koji.so/docs/research-refresh-cadence`
Supports: A vendor's guidance on how long findings stay valid, written for a research repository and ending in a pitch for the vendor's own platform. Findings decay at the speed of what they describe. Every insight is tagged at publication with its fieldwork date, population, product version and a decay class, and carries a confidence label with a review-by date. Every cited insight needs a date. A usability finding on one interface lasts until that interface changes, and a material product change invalidates evaluative findings. The half-life table cites no study, and the one-year and five-year review points are credited to an unnamed practitioner heuristic. It partly fails the one-study test: the four tags and the label belong to each insight, which one report can carry, while the quarterly sweep belongs to the repository
Quotable: "Research does not expire on a fixed schedule"
Quotable: "research decays at the speed of the thing it describes."
Quotable: "Research repositories are built to accumulate and preserve; almost none are built to mark things stale."
Quotable: "A widely used practitioner heuristic is to check for existing research before commissioning new work, treating roughly one year as the review point for evaluative research and about five years for generative research."
Quotable: "Usability findings on a specific interface"
Quotable: "Until the next material change to that interface"
Quotable: "Often under 12 months; a redesign invalidates them instantly"
Quotable: "Your product changed materially. Any change to the flow the research described. This invalidates evaluative findings immediately and completely."
Quotable: "Tag every insight with four fields at the time of publication."
Quotable: "Collected on: the fieldwork date, not the publication date"
Quotable: "Population: the exact cohort, including how they were recruited"
Quotable: "Product version / state: what the participants were actually reacting to"
Quotable: "Decay class: from the table above"
Quotable: "Run a quarterly staleness sweep."
Quotable: "Publish an explicit confidence label."
Quotable: "Validated Q1 2026, population: SMB admins, decay class: competitive expectations, review by Q3"
Quotable: "The most damaging pattern: a slide with a compelling quote and no fieldwork date. Require dates on every cited insight."

## Pages not read under the terms rule

The research agents found each page below and did not read it, because the site's own terms of use forbid
automated access. The maintainer has not read any of them by hand. No claim in this bundle rests on them. The
excluded sites and their clauses are listed in `docs/internal/bundle-pipeline.md`, under "The terms rule".

- `https://www.koji.so/docs/ux-research-report-template`. Koji's terms bar automated access to its services
  without permission. The page would have supported a second worked report template, with a cover page and a
  version field.
- `https://www.koji.so/docs/atomic-research-nuggets-guide`. Koji, the same clause. The page would have
  supported the difference in size between a research nugget and a report.
- `https://www.koji.so/docs/research-debrief-guide`. Koji, the same clause. The page would have supported the
  difference between a debrief, which is an internal working session, and a report written for stakeholders.
- `https://www.koji.so/docs/generative-vs-evaluative-research`. Koji, the same clause. The page would have
  supported a second comparison of generative and evaluative research.
- `https://www.koji.so/docs/anonymizing-customer-interview-data`. Koji, the same clause. The page would have
  supported a checklist for removing names and other identifiers from quotations before they enter a report.
- `https://www.koji.so/docs/stakeholder-buy-in-user-research`. Koji, the same clause. The page would have
  supported advice on winning stakeholder support for research.
- `https://www.koji.so/blog/ux-research-for-designers-2026`. Koji, the same clause. The page would have
  supported a claim about how much research designers and product managers now run themselves.
- `https://www.entropik.io/resources/blog-articles/generative-vs-evaluative-research-explained`. Entropik's
  terms allow access only through the interface Entropik provides. The page would have supported another
  vendor's comparison of generative and evaluative research.
- `https://www.getwhy.io/`, the blog's pages on how findings decay. GetWhy's terms bar spiders, robots,
  crawlers and similar tools. The pages would have supported a second view on when findings stop describing
  current customers. The agent that wanted them did not record a single page address.
- `https://www.productplan.com/learn/ux-research-with-ai`. ProductPlan's terms bar automated tools that scrape,
  crawl or extract content. The page would have supported the claim that a finding with no link to its evidence
  should be treated as unverified.
- `https://dataanddesign.substack.com/p/you-might-be-using-the-wrong-wording`. Substack's terms bar crawling,
  scraping and spidering any page it hosts. The page would have supported practitioner advice on how to word a
  finding.
- `https://haphan.substack.com/p/design-is-an-activity-of-research`. Substack, the same clause. The page would
  have supported a practitioner's account of running discovery research without a research team.
