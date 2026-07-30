# okrs research log

Researched 2026-07-29 across five parallel dimensions: origins and canon, structure and formats, the
evidence base, debates and failure modes, and relationships, cadence and practice. **78 sources**, of which
**64 fetched-and-verified**, **9 url-confirmed-not-read**, and **5 not-retrieved**. Retrieval status is
recorded per source in the three-token vocabulary the library gates
([ADR 0029 (the research-log contract gate)](../../docs/internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md)), and only
`fetched-and-verified` sources are quoted.

**How to read this log.** A `Supports:` clause says what the bundle is allowed to rest on that source for.
A `Quotable:` phrase was read verbatim on the page. If a claim in the companion is not covered by some
entry's `Supports:` clause here, the claim has no home and must be cut, not justified after the fact.

---

## Honest framing: the five things this bundle has to say

**1. Goal-setting science is real. OKR science is not.** Locke and Latham's goal-setting theory is about as
solid as management research gets: specific difficult goals beat "do your best," with meta-analytic effect
sizes of **.42 to .80** on that comparison and **.52 to .82** on goal difficulty, across "well over 100
different tasks involving more than 40,000 participants in at least eight countries" [28]. A real
peer-reviewed adversarial literature exists alongside it [29][30], with a published rebuttal in the same
journal issue [31]. **Neither side of that debate mentions OKRs, quarterly cadence, or scoring anywhere.**

**2. The transfer is assumed, never demonstrated.** The move from "specific difficult goals work" to "the
OKR format works" is made constantly in vendor content and by no source located here. Nothing found
isolates whether quarterly time-boxing, 0.0-1.0 scoring, public visibility or cascading strengthen or weaken
the underlying goal effect. The systematic mapping of the OKR literature identifies **47 primary studies**
and calls OKR "under-documented from a theoretical point of view" [33]. The best in-situ industry study
measured engineer **perceptions and process friction**, not delivery outcomes [35]. **The one place the
adjacent literature touches quarterly cadence directly, it is a warning about short-termism, not an
endorsement** [29].

**3. One format ships, and the rejections are the useful result.** Under
[ADR 0028 (the format-axis rule)](../../docs/internal/decisions/0028-adopt-a-format-axis.md) a format ships
only when it is structurally distinct **and** in circulation with a named source. Nine candidates were
considered and **only the standard Objective plus Key Results form qualifies**. See the format verdict below.

**4. Three scoring and confidence devices come from three different people and are constantly conflated.**
Google's 0.0-1.0 grading with red/yellow/green bands [18], Doerr's reporting of Google's committed (target
1.0) versus aspirational (target 0.7) split [18][19], and Christina Wodtke's 1-to-10 **forecast confidence**
level [27] are three separate instruments with different jobs. Wodtke's is a weekly forward-looking bet;
Google's is an after-the-fact grade. Vendor writing merges them.

**5. The critics and the advocates concede more than their reputations suggest.** Doerr: "OKRs are not a
silver bullet" [5]. Wodtke: "I've botched OKRs more times than I can count" and "not everyone needs to set
OKRs" [54]. And **Rick Klau, whose video made OKRs famous inside Google's ecosystem, published a public
retraction of his own guidance a decade later** [23]. On the other side, the author of "Are OKRs 'Management
Malpractice'?" concludes "the best use of OKRs is for multi-directional alignment" [60]. **Nobody credible
found in this research argues OKRs are worthless.** The dispute is entirely about the conditions.

---

## The format verdict, against ADR 0028's rule

**Six candidates were evaluated individually: one ships and five are rejected.** A further **nine named
goal-setting frameworks** were then checked for a counterexample and none qualified, which is the last row
below. Stating it in two tiers is deliberate: the six got primary-source examination, the nine got a targeted
counterexample hunt, and collapsing them into one number is how the previous bundle in this family shipped
"eight researched, five rejected" while naming six rejections.

| Candidate | Verdict and ground |
|---|---|
| **Objective + Key Results** | **SHIPS**, the default and the only one. Documented by a chain of named primary sources: Grove [1][2], Doerr [3][5], and Google's own internal playbook [18] |
| **V2MOM** (Benioff, Salesforce) | REJECT. Genuinely structurally distinct, five components against two, with Values and Obstacles slots OKR has no equivalent for. But **the Salesforce Trailhead unit that defines all five components and gives the origin story does not mention OKRs once** [20]. Its author does not present it as an OKR variant. Note the scope: one unit of a longer module was read |
| OKRs with Initiatives | REJECT. Not a distinct shape but the default stated in full. See the Initiatives finding below |
| Cascading / tiered OKRs | REJECT. An organizational process, not a document anatomy. The document at every tier has the same two parts |
| Vendor one-pagers and canvases | REJECT. Competing software-vendor tracking layouts on the same anatomy. No single named canonical artifact |
| Wodtke's "OKR Four Square" | REJECT. A named single-author artifact, which is more than the vendor layouts can claim, but a weekly check-in worksheet layered on standard Objectives and Key Results, not a redefinition of them [27] |
| 4DX / WIGs, OGSM, Hoshin Kanri, Balanced Scorecard, North Star, FAST, GIST, PACT, iMBOs | REJECT. An adversarial pass on 2026-07-29 searched specifically for a counterexample, a named structurally distinct variant whose **own author** presents it as an OKR variant, and found none across all nine. Each is published as a competing framework rather than an OKR shape, and where a named author does relate the two, OKRs are **nested inside** the other framework rather than claimed as a variant of it. **The remaining limit, stated:** the book-length primaries behind several of these were not fetched, so this is a strong negative from published web material rather than an exhaustive one |

**The rule's unwritten third criterion, stated plainly.** V2MOM was rejected because its own author does not
present it as an OKR. **That test is not in ADR 0028**, whose written rule is structural distinctness plus
circulation with a named source. It has now decided rejections in two consecutive bundles: `product-roadmap`
excluded the opportunity solution tree and Cagan's five-part alternative on the same ground. The reading has
never been applied backwards, and `product-vision` ships a PR/FAQ admitted under the two written criteria
alone. Either the rule gains a third criterion explicitly or these two bundles are stricter than their
sibling. That belongs to the `default_format` backfill (decision D-E in
[`buildout-specs.md`](../../docs/internal/buildout-specs.md)), which already needs its own ADR.

---

## Claims flagged contested or time-bound

1. **The year OKRs reached Google is contradicted by three sources that should be authoritative on it, two of
   them Doerr's own and Google's own.** Doerr's site: "In 1998, when Larry Page and Sergey Brin were just 24
   years old, I gave them my OKR pitch" [5]. Doerr's own TED talk: "In 1999, I introduced OKRs to Google's
   cofounders, Larry and Sergey" [3]. Google's own re:Work guide: "A few decades later in **early 2000**,
   Doerr introduced OKRs to Google's leadership" [6]. **State the range, never a single year.**
   **Corrected 2026-07-30:** this item quoted the 1998 line as "Doerr pitched OKRs to 24-year-old Larry Page
   and Sergey Brin," a paraphrase the verification pass had already caught and replaced in entry [5] without
   anyone checking whether the same wrong wording survived elsewhere in this file. **It did.** That is the
   second time this log's narrative sections were found quoting something its own entries do not carry; the
   first was the Roger Martin line at [69]. **A verification pass over source entries does not verify the
   prose that cites them.**

2. **Whether Grove used the term "OKR" at all is unresolved, and the honest answer is a research gap.** The
   accessible portion of *High Output Management* contains no instance of "OKR," "objectives and key results"
   as a named acronym, or "Drucker" [1]. But that access was **partial**, stopping short of the
   Management by Objectives chapter, so this is not a confirmed absence. Wikipedia, citing Doerr's own book,
   reports that in 1975 the method was "then called 'iMBOs'" [10], which is a source close to Doerr implying
   the name he met at Intel was not "OKR."

3. **The Grove-inherits-from-Drucker lineage is folklore-shaped.** Doerr's own site asserts it: "He found it
   in the work of Peter Drucker, who had introduced MBOs, or Management by Objectives, in the 1950s" [7], with
   no citation to anything Grove said. Wikipedia's MBO article does not mention Grove, Intel or OKRs anywhere,
   and Wikipedia's OKR article does not mention Drucker anywhere [10][11]. The two lineages are documented
   separately. Treat the chain as plausible and unverified.

4. **Grove-as-inventor is actively disputed by a named institute.** "We should all be simply giving Grove
   credit for a more effective way to implement MBO. Instead, the world has declared him the 'inventor' of
   something called OKRs even though OKR and MBO are based on the same principles and follow roughly the same
   process" [15]. This is one side of a branding dispute, not settled fact, and it deserves to be in the
   bundle because it is the strongest challenge to the standard origin story.

5. **The "I will [Objective] as measured by [Key Results]" formula has no traceable author.** It appears on
   Doerr's own FAQ attributed to nobody [9], and *Measure What Matters* could not be retrieved to check
   whether it originates there [13].

6. **Committed versus aspirational is Google's framing**, documented in Google's own internal playbook [18],
   which Doerr then reported and republished with permission rather than invented [16]. It is **not** part of
   Grove's originating conception; neither Wikipedia's history section nor Google's own history section
   attaches it to the 1970s Intel formulation [6][10].

7. **The outcome rule is dominant but not unanimous, and the bundle must carry the qualification.** Google's
   playbook is categorical: Key Results "must describe outcomes, not activities" [18]. But Felipe Castro
   argues against forcing everything into outcome form, recommending a separate "due-dates bucket" for work
   such as security and compliance whose outcome cannot yet be measured [24], and Perdoo's CEO concedes
   "Milestone Key Results are great for projects that have distinct phases of completion" while still holding
   outcomes as the default [25].

8. **Quarterly cadence is convention, not measurement.** No source of any tier supplies comparative evidence
   for three months over any other period. The clearest voice calls quarterly-only a "common misconception"
   and replaces evidence with a heuristic [74]. Google itself added an annual layer after 2011 [74], and
   John Cutler argues the fixed 90-day cycle is itself the problem: "90.25 days might be perfect for your
   company, 60 for the next, 30 for the next" [64].

9. **The 0.7 target and the 60-70 percent "sweet spot" are stated conventions, not measured optima.** Google's
   playbook states the grading bands as internal practice [18] and re:Work states the sweet spot [6]; no
   controlled study validating either was found. Do not cite them as evidence that OKRs work; they describe a
   scoring philosophy.

10. **The anti-cascading consensus is narrower than its slogans.** "OKRs never cascade. OKRs align" [53], and
    Wodtke and Lamorte agree independently [54][55]. But all three still want leadership to set direction
    first, and Google's own guide recommends organizations "commit first to organizational objectives, so that
    teams and individuals can set their own objectives in service of those larger goals" [6], which is a
    top-down sequencing step. **The real disagreement is whether Key Results get mechanically copied downward
    as the next level's Objectives (universally rejected) or direction flows down and objectives are
    negotiated locally (what essentially everyone, including Google, actually does).**

11. **Public visibility is the default, not an absolute.** Google: "OKRs are public so that everyone in the
    organization can see what others are working on" [6]. A named practitioner lists explicit carve-outs for
    M&A, restructuring, personal development goals and public-company financial exposure [75].

12. **The Spotify cadence claim that circulates is imprecise.** Vendor blogs describe Spotify Rhythm as
    "Spotify's version of OKR" on a six-month/six-week rhythm. The primary account, by the consultant who
    wrote it up, describes Rhythm as what Spotify reached **after** moving through and away from OKRs, which
    were later reintroduced alongside it [76]. Do not repeat the vendor framing.

13. **`Initiatives` is vendor and tooling convention, not confirmed canon.** One vendor asserts "John Doerr's
    OKR framework consists of Objectives, Key Results, and Initiatives" while citing no page or quote for the
    structural claim [73], and **Google's own re:Work guide never mentions initiatives at all** [6]. This is
    an absence-of-evidence finding, not a confirmed absence in Doerr's book, which could not be retrieved
    [13]. The section may ship; it must not be presented as canon.

14. **The Key-Result count is convention with no independent settlement.** Google says "Pick just three to
    five objectives" and "Determine around three key results per objective" [6]; a summary of Doerr's book
    reports "five or fewer" [16]; a vendor recommends "between 2 and 4" from its own platform data [26]. No
    non-interested source settles the number.

15. **A summary of *Goals Gone Wild* contaminates its own source.** An infographic summarising the 2009 paper
    adds a 2016 Wells Fargo example [32]. The scandal postdates the paper by seven years. **Do not attribute
    the Wells Fargo case to Ordonez et al. (2009).**

---

## Statistics found and deliberately excluded

Recorded because the next author will meet all of them. None appears anywhere in this bundle as a fact.

**Two are worse than untraceable. They name a real institution that has no connection to the subject.**

| Claim | Finding |
|---|---|
| "A study from the UK's Institute for Fiscal Studies in 2025 found that 78% of enterprise OKR programmes failed because they were tied to performance pay", plus a paired "59% reduction in risk-taking" [49] | **Exclude as untraceable.** The IFS is a real, well-known UK think tank whose mandate is tax, welfare and public-spending policy. A direct search for any connection between the IFS and OKRs, or for this figure, returned nothing |
| "A 2026 study by the Scale-Up Institute found that 65% of high-growth companies that ditched OKRs did so because their goals got lost in the daily grind", with "92% of these failures linked to having no ongoing rhythm" [49] | **Exclude as untraceable.** No study matching this description, sample or year is findable, and the hosting article is dated the same year as the study it cites |

**A deliberate softening, 2026-07-29.** Both rows previously read "treat as fabricated." **The adversarial
pass commissioned to test that accusation did not complete**, so no independent search has confirmed the
studies do not exist. Calling a named real institution's work fabricated is a serious claim and this library
does not publish serious claims on one agent's search. **Untraceable is what was actually established:
one researcher looked and did not find them.** The bundle says that and no more. Anyone who wants the
stronger claim must search the IFS publication list directly and record the search.

**No source given at all:** "60% of OKR implementations are abandoned within the first 12 months" [48];
"the 75% OKR failure rate"; "companies using OKRs are 39% more likely to achieve their goals", attributed only
to "Psico-Smart" with no date, sample or method [45]; "2.5 to 4 times faster growth", sourced to an unlinked
undated blog post [45]; "60% higher revenue growth"; "23% of organizations achieve consistent OKR success
across two consecutive cycles" [44].

**Also excluded: a "40-60 percent of Key Results should be bottom-up" rule** attributed to Doerr by tertiary
summaries. Checked against What Matters' own cascading FAQ, which gives **no percentage at all** [77]. Do not
state a figure without tracing it to a page in *Measure What Matters*.

**Sourced but not safe to present as research:**

- **The Sears Holding Company OKR figures** ("8.5% increase in sales per hour", "11.5% increase in the chance
  of moving to a higher performance bracket") trace to a real named analyst, Chris Mason, covering roughly
  20,000 salaried associates over 2013 to 2015, but were **never peer-reviewed or published** beyond a blog
  interview [37]. **And there are three unrelated "Sears" items circulating in OKR content that get
  conflated:** this OKR rollout study [37]; Rucci, Kirn and Quinn's 1998 HBR "Employee-Customer-Profit Chain"
  piece, which is not about OKRs [38]; and the 1993 Harvard Business School teaching case on the Sears Auto
  Centers overcharging scandal, cited in *Goals Gone Wild* as evidence that goals cause unethical behaviour
  [39]. Citing the fraud case as OKR evidence would invert its meaning entirely.
- **The goal-gaming survey** (92% admit some gaming, 89% have sandbagged, 96% sandbag when scores affect
  ratings versus 81% when kept separate, 52% of analysed Key Results were tasks or KPIs in disguise) is a
  **vendor-run self-report survey of 210 full-time employees** [50][26]. Directional at best. If used, it
  ships with its N, its method and its vendor tier attached.
- **The Haufe Talent / Stuttgart comparative percentages** come from a real practitioner-academic partnership
  but sample size, response rate and significance testing could not be accessed [41].
- **The Mooncamp/Scaleon "OKR Impact Report 2022"** rests on "executives from 40 companies", a small
  self-selected sample [42].
- **OKR software market-size figures** are restated with materially different numbers by two vendor blogs
  citing nominally the same report. A visible case of stat drift through repeated citation [44][45].

**A documented search false positive**, recorded so the next author does not think it was missed: arXiv
2311.16542, "Agents meet OKR," borrows the term as a design metaphor for hierarchical LLM agent task
decomposition and has no bearing on corporate OKR practice [36].

---

## Notes for the companion

**The honest core.** Goal-setting science is real and does not measure this artifact. Say it in section 1 and
do not soften it. The bundle's value is the shape of the document and the failure modes, not a performance
claim.

**The load-bearing sections.** Objective and Key Results are the whole artifact; everything else is optional
scaffolding whose provenance differs. Keep the three measurement devices separate and attributed: Google's
grading bands, the committed/aspirational split, and Wodtke's forecast confidence.

**The sharpest teaching points, in order.**

1. **A Key Result that names an activity is not a Key Result.** Google's own test is a word list: "If your KRs
   include words like 'consult,' 'help,' 'analyze,' or 'participate,' they describe activities" [18]. That is
   a checkable rule an author can apply to their own draft in ten seconds, which makes it the single most
   useful sentence found in this research.
2. **The compensation rule, from the person who popularised the framework.** "Don't tie the OKR goals to bonus
   payments, except for sales quotas" [51]. Google: "OKRs are not synonymous with employee evaluations" [6].
   The named exception both camps accept is sales quotas.
3. **OKRs are not a strategy.** Roger Martin: OKRs are "a complement to strategy, not a substitute for
   strategy," and jumping from Objective to Key Results with no where-to-play choice produces "OKRs
   masquerading as strategy" [69].
4. **The KPI boundary, which this library needs because it ships a `kpi-dashboard`.** A KPI is a steady-state
   health metric; an OKR is a goal metric. "KPIs often inform - and even become - your OKRs, if it's a
   measurement that you want to significantly change" [70], and the metric reverts to KPI status once the
   change is achieved. The dissenting view is worth carrying: "Switching from KPIs to OKRs doesn't fix
   neglect. It just gives neglect a more ambitious name" [71].
5. **The retraction.** Rick Klau's 2022 post correcting his own most-cited OKR guidance on four separate
   points [23]. An advocate revising his own famous work is stronger evidence of the framework's real edges
   than any critic.

**Anti-patterns, sourced, six or more required by family practice.** OKR theatre [59][60]; sandbagging
[23][57][50]; watermelon reporting [50]; cascading as waterfall [53][54][55][59]; Key Results that are tasks
or KPIs in disguise [67][65][50]; individual OKRs conflated with performance review [6][23][10];
compensation coupling that kills stretch [51][56][57][62]; quarterly cadence mismatch [64].

**Do not write a polemic.** Carry Doerr's "not a silver bullet" [5], Wodtke's admitted failures and her
"not everyone needs to set OKRs" [54], Klau's retraction [23], and from the critical side the concession that
"the best use of OKRs is for multi-directional alignment" [60] and that OKRs deliver real focus "when executed
properly" [59]. Also carry the academic critic who still holds that "clear goals are still needed to enable
thriving" [61].

**What the example must chain onto.** The Acme Analytics thread, extending it upward into direction. Per the
[`strategy-docs` contract](../../docs/internal/contracts/strategy-docs.md) section 4 the objective **is** the
FY26 "Time to Insight" goal, which already exists in the library with a definition, a formula, a target, a
current actual, an owner, thresholds and a data source. Use those numbers; do not invent replacements.

**Use a different scenario in the template guidance comments than in the worked example.** Three sections of
the `product-roadmap` example were its own template's GOOD text reworded, and seven of eight were in
`product-strategy`. This is the library's most persistent defect and convention alone has not stopped it.

---

## Sources

### Origins and canon

**[1] Andrew Grove - High Output Management (1983), Internet Archive full-text stream.** primary (book). **fetched-and-verified.**
`https://archive.org/stream/dli.ernet.213936/213936-High%20Output%20Management_djvu.txt`
Supports: that in the accessible portion of the primary text the terms "OKR," "objectives and key results" as a named acronym, and "Drucker" do not appear.
Contested/time-bound: **access was partial.** The stream could be read through roughly the first third to half of the book and stopped short of the Management by Objectives chapter, so this is a research gap and not a confirmed absence. No claim of absence in the whole book may rest on this entry.

**[2] Nat Eliason - High Output Management by Andy Grove: Notes and Review.** practitioner. **fetched-and-verified.**
`https://www.nateliason.com/notes/high-output-management-andy-grove`
Supports: Grove's "two questions" passage, as a secondary rendering of the primary chapter.
Quotable: "A successful MBO system needs only to answer two questions: 1. Where do I want to go? (The answer provides the objective.) 2. How will I pace myself to see if I am getting there? (The answer gives us milestones or key results)."
Contested/time-bound: a secondary rendering. The primary chapter could not be reached to cross-check it [1]. Any use of this passage must say it is reported rather than read in the book.

**[3] John Doerr - TED talk, "Why the secret to success is setting the right goals" (2018), transcript.** primary. **fetched-and-verified.**
`https://singjupost.com/why-the-secret-to-success-is-setting-the-right-goals-john-doerr-transcript/`
Supports: Doerr's own attribution of the system to Grove, and his own dating of the Google introduction.
Quotable: "Andy invented a system called 'Objectives and Key Results.'" / "In 1999, I introduced OKRs to Google's cofounders, Larry and Sergey." / "But every quarter since then, every Googler has written down her objectives and her key results."
Contested/time-bound: read on a third-party transcript host rather than ted.com [4]. The 1999 date conflicts with [5] and [6].

**[4] TED - official transcript page for the same talk.** primary. **url-confirmed-not-read.**
`https://www.ted.com/talks/john_doerr_why_the_secret_to_success_is_setting_the_right_goals/transcript`
Supports: nothing. The fetch returned only the talk's title and description, not the transcript body. Recorded so the next author knows the official page exists and was not the source of the quotations in [3].

**[5] What Matters - "OKRs Explained: John Doerr course intro."** vendor (Doerr's own organisation). **fetched-and-verified.**
`https://www.whatmatters.com/okrs-explained/why-okrs-john-joerr`
Supports: Doerr naming Grove the originator, the 1998 date, Doerr's "not a silver bullet" concession, and the Grove line Doerr recalls.
Quotable: "In 1998, when Larry Page and Sergey Brin were just 24 years old, I gave them my OKR pitch." / "They are Andy Grove's invention, but I'm the messenger." / "Andy Grove, 'the Father of OKRs.'" / "John, it almost doesn't matter what you know. What matters is what you do." / "OKRs are not a silver bullet. They won't substitute for good judgment and a strong culture."
Contested/time-bound: the 1998 date conflicts with [3] and [6].

**[6] Google re:Work - "Guides: Set goals with OKRs."** primary (Google's own account of its own practice). **fetched-and-verified.**
`https://rework.withgoogle.com/intl/en/guides/set-goals-with-okrs`
Supports: Google's own dating of the introduction, the reason for adoption at Intel, current cadence, the objective and Key-Result counts, the not-a-checklist rule, the grading scale, the sweet spot, the review separation, transparency, the top-down plus bottom-up mix, and the mid-quarter check-in.
Quotable: "A few decades later in early 2000, Doerr introduced OKRs to Google's leadership who saw the value and started testing them out over the next couple of quarters." / "When he joined Intel, the company was transitioning from a memory company to a microprocessor company, and Grove and the management team needed a way to help employees focus on a set of priorities in order to make a successful transition." / "Today, Google sets annual and quarterly OKRs and holds company-wide meetings quarterly to share and grade OKRs." / "Pick just three to five objectives..." / "Determine around three key results per objective." / "One thing OKRs are not is a checklist." / "If a team treats this as a shared to-do list it may result in getting overly prescriptive about what the team wants done, rather than what the team wants to achieve." / "Google uses a scale of 0 - 1.0" / "The 'sweet spot' for an OKR grade is 60% - 70%; if someone consistently fully attains their objectives, their OKRs aren't ambitious enough and they need to think bigger." / "OKRs are not synonymous with employee evaluations." / "OKRs are public so that everyone in the organization can see what others are working on." / "Successful OKRs can often come from a mix of top-down and bottom-up suggestions..." / "Prior to assigning a final grade, it can be helpful to have a mid-quarter check-in for all levels of OKRs to give both individuals and teams a sense of where they are." / "commit first to organizational objectives, so that teams and individuals can set their own objectives in service of those larger goals"
Contested/time-bound: "early 2000" conflicts with [3] and [5]. **The word "initiatives" does not appear anywhere on this page**, which is the load-bearing absence behind finding 13. The "commit first to organizational objectives" sequencing sits in tension with the anti-cascading camp [53][54][55].

**[7] What Matters (Giulia Pines) - "The Origin Story" (2025-04-04).** vendor. **fetched-and-verified.**
`https://www.whatmatters.com/articles/the-origin-story`
Supports: biographical background on Grove, and the assertion of a Drucker-to-Grove lineage.
Quotable: "He found it in the work of Peter Drucker, who had introduced MBOs, or Management by Objectives, in the 1950s." / "He was sort of a walking OKR."
Contested/time-bound: the Drucker-inspiration claim carries no citation to any statement of Grove's, and could not be independently confirmed [1][11]. The word "quarterly" does not appear in the fetched text, so the quarterly rationale usually attributed to Grove was **not** located in the most likely place to find it.

**[8] What Matters - "OKR Example from John Doerr: How Intel Achieved their Goals" (Operation Crush).** vendor. **fetched-and-verified.**
`https://www.whatmatters.com/okrs-explained/john-doerr-operation-crush`
Supports: the Operation Crush narrative (Intel against Motorola and Zilog, 1979 to 1980) as the canonical worked OKR example, with the objective "Establish the 8086 as the highest performance 16-bit microprocessor family."
Quotable: "Bad companies are destroyed by crisis. Good companies survive them. Great companies are improved by them."
Contested/time-bound: the quoted line is attributed to Grove on this page; which of Grove's books or talks it originates in was not verified.

**[9] What Matters - FAQ, "How to write OKRs with examples."** vendor. **fetched-and-verified.**
`https://www.whatmatters.com/faqs/okr-examples-and-how-to-write-them`
Supports: the exact wording of the OKR formula, and the finding that this page attributes it to nobody.
Quotable: "I will [Objective] as measured by [Key Results]"
Contested/time-bound: no originator is named on the page. The formula's author is unresolved; see finding 5.

**[10] Wikipedia - "Objectives and key results."** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Objectives_and_key_results`
Supports: the general attribution chain, the "iMBOs" name, the 3-to-5 Key-Result convention, the scoring targets, and Rick Klau's 2017 position on individual OKRs. Also supports the finding that Drucker is not mentioned anywhere in the article.
Quotable: "The development of OKR is generally attributed to Andrew Grove who introduced the approach to Intel in the 1970s." / "documented the framework in his 1983 book High Output Management." / "In 1975, John Doerr, at the time a salesperson working for Intel, attended a course within Intel taught by Grove where he was introduced to the theory of OKRs, then called 'iMBOs'..." / "OKRs comprise an objective (a significant, concrete, clearly defined goal) and 3-5 key results." / Rick Klau, November 2017, as preserved in the article: "Skip individual OKRs altogether. Especially for younger, smaller companies. They're redundant. Focus on company- and team-level OKRs."
Contested/time-bound: this article's own citations trace to a vendor history post and to Doerr's and Levy's books, none of which were read directly. This entry supports Wikipedia's representation of those sources, not the sources themselves.

**[11] Wikipedia - "Management by objectives."** reference. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Management_by_objectives`
Supports: Drucker's origination of the MBO term, and the finding that this article does not connect MBO to Grove, Intel or OKRs anywhere.
Quotable: "Peter Drucker first used the term 'management by objectives' in his 1954 book The Practice of Management."

**[12] Internet Archive - item page for High Output Management.** reference (hosting page, not body text). **fetched-and-verified.**
`https://archive.org/details/dli.ernet.213936`
Supports: a negative result only. No table of contents or chapter list is exposed, which is why the MBO chapter's location could not be found this way [1].

**[13] John Doerr - Measure What Matters, third-party PDF mirror.** primary (book). **url-confirmed-not-read.**
`https://sunbytes.io/app/uploads/2022/04/Measure-What-Matter-John-Doerr.pdf`
Supports: nothing. The fetch failed because the file exceeded the tool's size limit. Recorded because three separate open questions depend on this text: the origin of the OKR formula [9], the 1975 Intel-course anecdote, and whether Doerr's book establishes an Initiatives layer [73].

**[14] OKR Training - "Chapter 1: Introduction to OKRs - The History of OKRs" sample PDF.** practitioner. **url-confirmed-not-read.**
`https://www.okrstraining.com/wp-content/uploads/2017/04/OKRTraining-Chapter-1-Sample.pdf`
Supports: nothing. The fetch returned raw PDF metadata rather than readable prose. Not used for any claim.

**[15] Balanced Scorecard Institute - "No, Andy Grove Didn't Invent OKRs and Other 'Stake-Your-Claim' Problems."** practitioner (named institute; blog commentary, not a standard). **fetched-and-verified.**
`https://balancedscorecard.org/blog/no-andy-grove-didnt-invent-okrs-and-other-stake-your-claim-problems/`
Supports: the strongest named dissent from the Grove-as-inventor story, and the claim that OKR and MBO are the same principles under different branding.
Quotable: "We should all be simply giving Grove credit for a more effective way to implement MBO. Instead, the world has declared him the 'inventor' of something called OKRs even though OKR and MBO are based on the same principles and follow roughly the same process."
Contested/time-bound: one side of a branding dispute, from an institute with its own competing methodology. Present as dissent, not as settled fact.

**[16] Graham Mann - book notes on Measure What Matters by John Doerr.** practitioner (book-summary site). **fetched-and-verified.**
`https://grahammann.net/book-notes/measure-what-matters-by-john-doerr`
Supports: secondary corroboration of Doerr's reporting of Google's committed and aspirational categories, the grading bands, the Key-Result count guidance, and the within-quarter review frequency.
Quotable: "In general, each objective should be tied to five or fewer key results." / "The expected score for a committed OKR is 1.0; a score of less than 1.0 requires explanation for the miss." / "Aspirational OKRs have an expected average score of 0.7, with high variance." / "0.7 to 1.0 = green. (We delivered.) 0.4 to 0.6 = yellow. (We made progress, but fell short of completion.) 0.0 to 0.3 = red. (We failed to make real progress.)"
Contested/time-bound: a summariser's rendering of the book, not the book. The primary text could not be retrieved [13]. Treat every book-attributed phrase here as reported.

**[17] Goodreads - reader highlight on Measure What Matters (Kiran Hegde).** reference (crowd-sourced). **fetched-and-verified.**
`https://www.goodreads.com/notes/37559166-measure-what-matters/8900274-kiran-hegde/fade6de5-fd33-40b2-8c17-bece412ea5c1`
Supports: independent corroboration of one sentence's wording as it appears in Doerr's book.
Quotable: "Google divides its OKRs into two categories, committed goals and aspirational (or 'stretch') goals. It's a distinction with a real difference."
Contested/time-bound: a reader-submitted highlight, not the publisher's text. Used as corroboration alongside [16], never as a sole source.

### Structure, formats and scoring

**[18] Google - "Google's OKR Playbook."** primary (internal Google document, reprinted with Google's permission, hosted by What Matters). **fetched-and-verified.**
`https://assets.ctfassets.net/mu244eycyvsr/3T7YZSUplO5Wt2UMpHKBoF/70ca14665b9735a7f7cff5f4c95c34df/WhatMatters.com_-_Google_s_OKR_Playbook.pdf`
Supports: **the definitive primary source for committed versus aspirational OKRs**, the outcome-not-activity rule with Google's own word test and a worked rewrite, the grading bands, and the sandbagging trap.
Quotable: "OKRs have two variants, and it is important to differentiate between them: Commitments are OKRs that we agree will be achieved, and we will be willing to adjust schedules and resources to ensure that they are delivered." / "The expected score for a committed OKR is 1.0; a score of less than 1.0 requires explanation for the miss" / "By contrast, aspirational OKRs express how we'd like the world to look, even though we have no clear idea how to get there and/or the resources necessary to deliver the OKR." / "Aspirational OKRs have an expected average score of 0.7, with high variance." / "Key Results are the 'Hows.' They: ... must describe outcomes, not activities. If your KRs include words like 'consult,' 'help,' 'analyze,' or 'participate,' they describe activities. Instead, describe the end-user impact of these activities: 'publish average and tail latency measurements from six Colossus cells by March 7,' rather than 'assess Colossus latency.'" / "We grade them with a color scale to measure how well we did: 0.0-0.3 is red, 0.4-0.6 is yellow, 0.7-1.0 is green." / under the heading TRAP #4, Sandbagging: "Teams who can meet all of their OKRs without needing all of their team's headcount/capital ... are assumed to either be hoarding resources or not pushing their teams, or both."
Contested/time-bound: undated in the visible text; PDF metadata shows creation in May 2018, consistent with the Measure What Matters launch window, but that is metadata rather than an in-document date claim. Nothing here is presented by Google as empirically derived; it is stated as internal convention.

**[19] What Matters (Lisa Shufro) - FAQ, "Committed vs. Aspirational OKRs: What's the Difference?"** vendor. **fetched-and-verified.**
`https://www.whatmatters.com/faqs/committed-aspirational-okrs-examples-difference`
Supports: that the committed and aspirational categories are attributed to Google rather than to Doerr.
Quotable: "Although most of their goals are aspirational OKRs, they also recognize that some OKRs need to be completed by the cycle's end. So they created a second category: committed OKRs." / attributed to Larry Page: "When you aim for the stars you may come up short, but still reach the moon."
Contested/time-bound: the page cites neither Doerr's book nor Google's internal playbook. Treat the Larry Page attribution as reported, not traced to a dated primary utterance.

**[20] Salesforce Trailhead - "Achieve Organizational Alignment with V2MOM."** primary (Salesforce's own official training material). **fetched-and-verified.**
`https://trailhead.salesforce.com/content/learn/modules/manage_the_sfdc_organizational_alignment_v2mom/msfw_oav2m_creating_org_alignment_v2mom`
Supports: V2MOM's five components with definitions, its origin story, and **critically, the complete absence of any OKR framing**, which is the ground on which the format is rejected.
Quotable: "an acronym that stands for Vision, Values, Methods, Obstacles, and Measures." / Vision: "Defines what you want to do or achieve." / Values: "Principles and beliefs that help you pursue the vision." / Methods: "Actions and steps to take to get the job done." / Obstacles: "The challenges, problems, issues you have to overcome to achieve the vision." / Measures: "Measurable results you aim to achieve." / "It all started back when our founder Marc Benioff was working at Oracle." / "they scribbled out the very first V2MOM on the back of an American Express envelope."
Contested/time-bound: **the unit fetched contains zero mention of OKRs, and only one unit was fetched.** The Trailhead module runs to roughly 55 minutes and 300 points; the unit read here is roughly 20 minutes and 100 points, so at least one further unit was never opened. The absence is load-bearing for the V2MOM rejection and is stated at the scope actually checked. **Do not widen this to "the module" without fetching the remaining units**, because any reader can click the next one.

**[21] Salesforce Blog - "What is the Salesforce V2MOM?"** primary. **not-retrieved.**
`https://www.salesforce.com/blog/how-to-create-alignment-within-your-company/`
Supports: nothing. The fetch returned HTTP 403. Recorded because it is the most likely place to find Benioff's own words on V2MOM, and it remains unread.

**[22] Tability - "V2MOM: What it is, how Salesforce uses it, and whether it's right for your team."** practitioner. **not-retrieved.**
`https://www.tability.io/odt/articles/v2mom`
Supports: nothing. HTTP 403. Recorded because it is one of several practitioner pieces that, per search summaries only, describe V2MOM and OKR as operating at different layers. No claim rests on it.

**[23] Rick Klau - "What my OKRs video got wrong" (2022-01-16).** primary (the original video's own author, self-published correction). **fetched-and-verified.**
`https://tins.rklau.com/2022/01/what-my-okrs-video-got-wrong/`
Supports: an advocate publicly retracting his own most-cited guidance on four points: individual OKRs, the quality of his own metric examples, the football analogy borrowed from Grove, and performance-review linkage.
Quotable: "If you're implementing OKRs for the first time...ignore individual OKRs." / on tying OKRs to reviews, that it will "encourage your teams to sandbag their OKRs, and set entirely achievable goals so they can get their bonus." / on his own earlier metric examples: "are, well, not great!" / "The analogy breaks down pretty quickly." / "the work in progress - the number of tasks, the lines of code, the incremental effort - but which are disconnected from the actual goal."
Contested/time-bound: explicitly supersedes his own 2012-era video on these specific points. Any citation of that video must note the correction.

**[24] Felipe Castro - "Not everything needs to be an outcome - or an OKR" (2024-06-20).** practitioner (independent OKR coach and author). **fetched-and-verified.**
`https://read.felipecastro.com/p/what-if-you-cant-measure-the-outcome`
Supports: the credible qualification of a strict universal outcome rule, which keeps the bundle out of polemic.
Quotable: "Not everything needs to be an outcome-or an OKR." / "Investments with outcomes we can measure go into the outcomes bucket. Investments with outcomes we can't measure-at least for now-go into the bucket focused on due dates."
Contested/time-bound: one credible practitioner's 2024 position, not a change to any named organisation's policy.

**[25] Perdoo (Henrik van der Pol, CEO) - "Different types of Key Results and when to use them."** vendor. **fetched-and-verified.**
`https://www.perdoo.com/resources/blog/different-types-of-key-results-and-when-to-use-them`
Supports: qualified acceptance of milestone Key Results as an exception, while holding outcomes as the default.
Quotable: "Key Results should measure outcomes, not outputs (activities)." / "Milestone Key Results are great for projects that have distinct phases of completion, such as the release of a new feature."
Contested/time-bound: a vendor with a commercial interest in appearing balanced. Practitioner opinion, not a rule change.

**[26] OKRs Tool - "How Many Key Results Per Objective? (The Right Number)."** vendor. **fetched-and-verified.**
`https://www.okrstool.com/blog/how-many-key-results-per-objective`
Supports: a competing Key-Result count recommendation, and the sourcing of the "tasks or KPIs in disguise" figure.
Quotable: "Our analysis of a sample of 7,857 Key Results - drawn from the broader 28,000 Key Result dataset, analyzed for output vs outcome language - found that 52% were tasks or KPIs in disguise." / "the right number of Key Results is between 2 and 4."
Contested/time-bound: both figures are the vendor's own proprietary platform data, explicitly sourced in-page to its own platform, neither independently audited nor peer-reviewed. Do not present as neutral research.

**[27] Christina Wodtke - "The Art of the OKR."** practitioner (author of Radical Focus). **fetched-and-verified.**
`https://cwodtke.com/the-art-of-the-okr/`
Supports: the 1-to-10 forecast confidence device and the weekly check-in, as Wodtke's own named contribution.
Quotable: "One great way to do this is to set a confidence level of five of ten on the OKR. A confidence level of one means 'never gonna happen my friend.' A confidence level of ten is also known as sandbagging." / "I highly recommend baking your OKRs into your weekly team meetings ... Adjust your confidence levels every single week."
Contested/time-bound: **this device is routinely attributed to "OKR practice" generically.** The primary source shows it is Wodtke's, and it is a different instrument from Google's 0.0-1.0 grading [18] and from the committed/aspirational targets [18][19]. Do not conflate the three.

### The evidence base

**[28] Locke, E. A., and Latham, G. P. - "Building a Practically Useful Theory of Goal Setting and Task Motivation: A 35-Year Odyssey." American Psychologist 57(9), 705-717 (2002).** academic (peer-reviewed). **fetched-and-verified.**
`https://med.stanford.edu/content/dam/sm/s-spire/documents/PD.locke-and-latham-retrospective_Paper.pdf`
Supports: the core specific-and-difficult-goals finding with effect sizes, the four mechanisms, the three moderators, and the theory's own stated boundary conditions including goal conflict, complex or novel tasks, and risk.
Quotable: "specific difficult goals have been shown to increase performance on well over 100 different tasks involving more than 40,000 participants in at least eight countries working in laboratory, simulation, and field settings" (p. 714). / "We found that specific, difficult goals consistently led to higher performance than urging people to do their best. The effect sizes in meta-analyses ranged from .42 to .80" (p. 706). / "Goal difficulty effect sizes (d) in meta-analyses ranged from .52 to .82" (p. 706). / "the organization's goal and the goal of the individual manager are sometimes in conflict... Goal conflict undermines performance if it motivates incompatible action tendencies" (p. 712). / "urging them to do their best sometimes leads to better strategies... than setting a specific difficult performance goal" (p. 708).
Contested/time-bound: **the terms "OKR," "objectives and key results," "quarterly," and "scoring" appear nowhere in the paper.** Its evidence base predates and is independent of the OKR format. **The two effect-size ranges are different claims and must not be merged:** .42 to .80 is specific-difficult goals against "do your best," .52 to .82 is goal difficulty.

**[29] Ordonez, L. D., Schweitzer, M. E., Galinsky, A. D., and Bazerman, M. H. - "Goals Gone Wild: The Systematic Side Effects of Over-Prescribing Goal-Setting." Academy of Management Perspectives 23(1), 6-16 (2009), journal version.** academic (peer-reviewed). **fetched-and-verified.**
`https://knowledge.wharton.upenn.edu/wp-content/uploads/2013/09/1359.pdf`
Supports: the side-effects literature, the real-world cases, and **the direct on-point warning about quarterly time horizons**, which is the only place in the adjacent literature that touches cadence.
Quotable: "Inappropriate Time Horizon. Even if goals are set on the right attribute, the time horizon may be inappropriate. For example, goals that emphasize immediate performance (e.g., this quarter's profits) prompt managers to engage in myopic, short-term behavior that harms the organization in the long run" (p. 8). / "4. Is the time horizon appropriate? Be sure that short-term efforts to reach a goal do not harm investment in long-term outcomes. For example, consider eliminating quarterly reports as Coco Cola [sic] did" (p. 26; the company name is misspelled in the source and is quoted as printed). / "we argue that the beneficial effects of goal setting have been overstated and that systematic harm caused by goal setting has been largely ignored."
Contested/time-bound: one side of a published dispute; the rebuttal appeared in the same issue [31]. Pages 1 to 8 and 20 to 27 of 27 were read directly. The paper addresses goal setting broadly and **never mentions OKRs**, so applying it to OKRs is an inference practitioners make, not a claim the paper makes.

**[30] Ordonez, Schweitzer, Galinsky, and Bazerman - "Goals Gone Wild," Harvard Business School Working Paper 09-083.** academic. **fetched-and-verified.**
`https://www.hbs.edu/ris/Publication%20Files/09-083.pdf`
Supports: the same work in its working-paper form, for the narrow-focus and unethical-behaviour mechanisms.
Quotable: "a narrow focus that neglects non-goal areas" (abstract) / "goal setting motivates unethical behavior" (p. 12)
Contested/time-bound: the same paper as [29] in a different document. Cite one or the other for a given claim, never both as if they were independent corroboration. **Corrected on verification 2026-07-29:** this entry previously carried two `Quotable:` strings, "Specific goals can induce tunnel vision..." and "Goal setting can promote unethical behavior as individuals focus on goal achievement...", **neither of which appears in the paper.** They were fabricated in the research fan-out and transcribed here unchecked. The paper does not use the phrase "tunnel vision" at all, so it must not appear anywhere in this bundle as quoted material.

**[31] Locke, E. A., and Latham, G. P. - "Has Goal Setting Gone Wild, or Have Its Attackers Abandoned Good Scholarship?" Academy of Management Perspectives 23(1) (2009).** academic (peer-reviewed). **url-confirmed-not-read.**
`https://journals.aom.org/doi/10.5465/amp.2009.37008000`
Supports: the existence of a direct published rebuttal to [29] in the same venue and issue, which establishes this as a live two-sided academic dispute rather than a one-sided critique. **No wording from it may be quoted.**
Contested/time-bound: the AOM page returned HTTP 403. Any characterisation of its argument is secondhand and must be labelled as such.

**[32] Ethical Systems - "Goals Gone Wild" summary infographic.** practitioner (summary of [29]). **fetched-and-verified.**
`https://a-us.storyblok.com/f/1016826/x/313bf5dfde/goals_gone_wild_final.pdf`
Supports: a warning, not a claim. **This summary adds a 2016 Wells Fargo example that cannot be in the 2009 paper**, since the scandal postdates it by seven years.
Contested/time-bound: **do not attribute the Wells Fargo case to Ordonez et al. (2009).** It is the summary's own addition. This is a worked example of a secondary source contaminating its primary.

**[33] Silva, R., and Santos, G. - "Surveying the Academic Literature on the Use of OKR (Objective and Key Results) - An Update." iSys, Brazilian Journal of Information Systems (2024).** academic (peer-reviewed systematic mapping). **fetched-and-verified.**
`https://journals-sol.sbc.org.br/index.php/isys/article/view/3885`
Supports: the state of the OKR-specific academic literature, 47 primary studies identified, and the authors' own assessment of its theoretical thinness.
Quotable: "OKR use is under-documented from a theoretical point of view" / "We found few academic studies addressing the topic in depth."
Contested/time-bound: a mapping of existing literature, not a new empirical outcome study.

**[34] Silva, R., and Santos, G. - "Surveying the Academic Literature on the Use of OKR," XIX Brazilian Symposium on Information Systems, ACM (2023), DOI 10.1145/3592813.3592934.** academic. **url-confirmed-not-read.**
`https://dl.acm.org/doi/10.1145/3592813.3592934`
Supports: the existence of an earlier conference version of [33]. HTTP 403 and paywalled. Not separately quoted.

**[35] Butler, J., Zimmermann, T., and Bird, C. - "Objectives and Key Results in Software Teams: Challenges, Opportunities and Impact on Development." arXiv:2311.00236 (2023).** academic (industry mixed-methods study; peer-review status of this preprint not confirmed). **fetched-and-verified.**
`https://arxiv.org/abs/2311.00236`
Supports: the best-documented real-world OKR study located, and the crucial point that **it measured perceptions, challenges and process rather than delivery outcomes**.
Quotable: "attitudes and beliefs of engineers are critical to the success of any goal setting framework"
Contested/time-bound: 47 interviews plus 512 survey responses from over 4,000 engineers at one unnamed large multinational software company. Not a treatment and control design. It establishes no causal effect on delivery outcomes, and must not be cited as if it did. The abstract page was read; the full paper was not.

**[36] arXiv:2311.16542 - "Agents meet OKR: An Object and Key Results Driven Agent System with Hierarchical Self-Collaboration and Self-Evaluation."** academic (LLM systems paper). **url-confirmed-not-read.**
`https://arxiv.org/abs/2311.16542`
Supports: nothing about OKR practice. **Recorded as a documented search false positive**, so the next author knows it was found, checked and excluded rather than missed. It borrows the term as a metaphor for hierarchical agent task decomposition.

**[37] OKRs.com - "Sears Holding Company Study Concludes OKRs Impact the Bottom Line" (2015).** vendor. **fetched-and-verified.**
`https://okrs.com/2015/03/sears-holding-company-study-concludes-okrs-impact-the-bottom-line/`
Supports: the origin and named authorship of the most-repeated OKR impact statistics, and the finding that no peer-reviewed publication exists for them.
Contested/time-bound: the "8.5% increase in sales per hour" and "11.5% increase in the chance of moving to a higher performance bracket" figures trace to Chris Mason (PhD, industrial-organisational psychology) and analyst Joe Kutter, covering roughly 20,000 salaried associates over 2013 to 2015. **Internal, unaudited, never peer-reviewed, published only as a blog interview.** If used at all it must be labelled an unpublished internal company account. Distinct from [38] and [39].

**[38] Rucci, A. J., Kirn, S. P., and Quinn, R. T. - "The Employee-Customer-Profit Chain at Sears." Harvard Business Review 76(1) (1998).** practitioner. **url-confirmed-not-read.**
`https://hbr.org/1998/01/the-employee-customer-profit-chain-at-sears`
Supports: nothing about OKRs. **Recorded solely to distinguish it from [37] and [39]**, because three unrelated Sears items circulate in OKR content and get conflated.

**[39] Santoro, M. A., and Paine, L. S. - "Sears Auto Centers." Harvard Business School Case 9-394-010 (1993).** academic (teaching case). **not-retrieved.**
No URL: a Harvard Business School teaching case distributed through HBS Publishing rather than at a public address, and known here only through its citation inside [29]. Inventing a bookseller or repository link would manufacture the appearance of retrieval.
Supports: nothing directly. **Recorded to distinguish it from [37] and [38].** In *Goals Gone Wild* this case is evidence that a sales quota drove staff "to overcharge for work and to complete unnecessary repairs on a companywide basis." Citing it as OKR evidence would invert its meaning.

**[40] "Effect of Objectives and Key Results (OKR) on Organisational Performance in the Hospitality Industry."** academic (claimed; authors and venue unconfirmed). **not-retrieved.**
`https://www.academia.edu/109762683/Effect_of_Objectives_and_Key_Results_OKR_on_Organisational_Performance_in_the_Hospitality_Industry`
Supports: nothing. Both fetch attempts returned HTTP 403. Search summaries describe a survey of 207 hotel employees in Abuja, Nigeria. Recorded as the one candidate for a traceable measured claim that could not be verified. No statistic from it may be used without a fresh successful fetch.

**[41] Haufe Talent with Hochschule fuer Technik Stuttgart - OKR study series (DACH region).** practitioner (practitioner-academic partnership). **url-confirmed-not-read.**
`https://www.haufe.de/personal/neues-lernen/studie-erfolgsbilanz-von-okr-in-der-praxis_589614_564574.html`
Supports: the existence of a more credible-than-vendor comparative study, without access to its methodology.
Contested/time-bound: sample size, response rate, significance testing and peer-review status could not be accessed. The comparative percentages it is cited for elsewhere are in the exclusion list.

**[42] Mooncamp with Scaleon - "OKR Impact Report 2022."** vendor (commissioned survey). **url-confirmed-not-read.**
`https://mooncamp.com/2022-okr-impact-report`
Supports: the sample behind a set of widely relayed figures.
Contested/time-bound: the sample is described in secondary summaries as "executives from 40 companies," a small self-selected group of OKR users surveyed by an OKR-adjacent partner. The report itself was not fetched.

**[43] Zhang, Y., and Jia, M. - "Stretch goals and unethical behavior" (2013).** academic (as characterised by secondary sources). **not-retrieved.**
`https://www.researchgate.net/publication/349114893_Stretch_goals_and_unethical_behavior_role_of_ambivalent_identification_and_competitive_psychological_climate`
Supports: nothing. **Flagged as a research gap, not a confirmed absence.** Secondary summaries describe it as linking stretch-goal design to unethical behaviour and referencing Wells Fargo. The body was not read, so no claim from it is asserted and no phrase is quoted.

### The statistics ecosystem

**[44] Mooncamp - "33 OKR Statistics for 2026."** vendor. **fetched-and-verified.**
`https://mooncamp.com/blog/okr-statistics`
Supports: the inventory of circulating statistics and their claimed sources, used to build the exclusion list. Also supports the market-size stat-drift finding.
Contested/time-bound: none of the underlying primary reports were verified. Every number sourced only to this page is vendor-relayed.

**[45] OKRs Tool - "60+ OKR and Strategy Statistics 2026 (Original Research)."** vendor. **fetched-and-verified.**
`https://www.okrstool.com/blog/okr-statistics`
Supports: the sourcing check that identified several untraceable figures, and this vendor's own methodology disclosure.
Contested/time-bound: "original research" here means vendor-commissioned market research on a self-selected technology-sector population. The disclosure of sample sizes and fielding dates is better than most, and it is still not independent research. The "39% more likely" and "2.5 to 4 times faster" figures relayed here trace to unnamed or unlinked third parties.

**[46] Yomly - "30+ OKR Statistics with Adoption and Benefits Data (2026)."** vendor. **fetched-and-verified.**
`https://www.yomly.com/okr-statistics`
Supports: confirmation that most circulating percentages carry no source citation at all in this rendering.

**[47] Jop - "Debunking the Myth: Exploring the Effectiveness of OKRs as a Goal-Setting Framework."** vendor. **fetched-and-verified.**
`https://www.getjop.com/blog/debunking-the-myth-exploring-the-effectiveness-of-okrs-as-a-goal-setting-framework`
Supports: **direct evidence for the transfer-gap finding.** A representative vendor article making the "OKRs are backed by goal-setting science" argument does not cite Locke and Latham, does not engage the gap between goal-setting findings and OKR mechanics, and gives no traceable primary sources.
Contested/time-bound: explicitly promotional, ending in a sales call to action.

**[48] PerformSpark - "The OKR Failure Rate: Why 60% of Implementations Fail."** vendor. **fetched-and-verified.**
`https://performspark.ai/blogs/okr-failure-rate-cascading-vs-alignment`
Supports: confirmation on direct read that the "60% abandoned within 12 months" claim carries no source, study name, institution, year or sample size anywhere in the article.

**[49] The OKR Hub - "Why OKRs Fail: The 7 Most Common Reasons (With Data)."** vendor. **fetched-and-verified.**
`https://www.theokrhub.com/insights/why-okrs-fail`
Supports: **the two least traceable attributions found in this research**, both naming a real institution.
Quotable: "A study from the UK's Institute for Fiscal Studies in 2025 found that 78% of enterprise OKR programmes failed because they were tied to performance pay."
Contested/time-bound: the Institute for Fiscal Studies is a real UK think tank working on tax, welfare and public spending, with no findable connection to OKRs or to this figure. The companion "2026 Scale-Up Institute" claim is equally unfindable and is dated the same year as the article citing it. **This entry exists to warn, not to support.**

**[50] OKRs Tool (Steven Macdonald) - "Goal Gaming: Why 92% of Employees Do It," citing "The State of Goal Management."** vendor. **fetched-and-verified.**
`https://www.okrstool.com/blog/goal-gaming`
Supports: quantified sandbagging and watermelon reporting, with a disclosed sample.
Contested/time-bound: a **self-report survey of 210 full-time employees, run in 2026 by a vendor with a commercial interest in the finding.** Figures: 92% admit at least one form of gaming; 89% have sandbagged; 96% sandbag when scores affect performance ratings against 81% when kept separate; 79% against 55% for health inflation. Directional only, not a population estimate. If any of these ships, its N, method and tier ship with it.

### Debates and failure modes

**[51] John Doerr, interviewed - Betterworks, "Keys to OKR Success: Q&A with John Doerr."** primary (direct interview). **fetched-and-verified.**
`https://www.betterworks.com/magazine/keys-okr-success-qa-john-doerr`
Supports: the compensation rule in Doerr's own words with its named exception, and an advocate's concession on customisation and failure.
Quotable: "Don't tie the OKR goals to bonus payments, except for sales quotas. We want to build a bold, risk-taking culture." / "Most companies that have implemented OKRs have adapted the system to their culture... And if it doesn't work for your company for whatever reason, that's ok too."

**[52] What Matters (Valerie Gilbert) - "Should You Connect OKRs and Compensation? (Spoiler Alert: No)."** vendor. **fetched-and-verified.**
`https://www.whatmatters.com/articles/should-you-connect-okrs-and-compensation-spoiler-alert-no`
Supports: the compensation position from Doerr's own organisation, and the sandbagging mechanism behind it.
Quotable: Ryan Panchadsaram: "You don't want to penalize people for aiming high."
Contested/time-bound: the page cites Volkswagen and Wells Fargo as illustrative scandals. Treat those as widely reported context, not verified here.

**[53] Felipe Castro - "Why you should not cascade your goals."** practitioner. **fetched-and-verified.**
`https://medium.com/the-alignment-shop/why-you-should-not-cascade-your-goals-c5f12020976a`
Supports: the anti-cascading position in its sharpest named form.
Quotable: "OKRs never cascade. OKRs align." / "Have you ever seen a cascade that flows bottom-up?"
Contested/time-bound: Castro also argues roughly 60 percent of OKRs should be bottom-up; that figure is his own and is not the unverified "40-60% per Doerr" claim in the exclusion list.

**[54] Christina Wodtke - "What I've Learned from 15 Years of Doing OKRs."** practitioner. **fetched-and-verified.**
`https://cwodtke.com/what-ive-learned-from-15-years-of-doing-okrs/`
Supports: the anti-cascading position, two advocate concessions, and the strategy boundary.
Quotable: "cascading creates bottlenecks. Everyone waits on the layer above to finalize goals." / "not everyone needs to set OKRs." / "I've botched OKRs more times than I can count." / "OKRs translate those high-level strategic decisions into focused, actionable efforts."
Contested/time-bound: a reflective retrospective. Wodtke still wants leaders to set direction before teams write their own, which is why the anti-cascading consensus is narrower than its slogan.

**[55] Ben Lamorte - OKRs.com, "How to Align OKRs: Why Cascading Fails and What Works Instead."** practitioner (co-author with Paul Niven of Objectives and Key Results). **fetched-and-verified.**
`https://okrs.com/2026/02/align-okrs/`
Supports: the anti-cascading position with its mechanism.
Quotable: "real alignment does not come from arrows connecting boxes. It comes from conversation, clarity, and shared understanding." / "When lower-level teams begin by copying and pasting OKRs instead of creating meaningful objectives through discussion and analysis, they are just going through the motions."

**[56] Ben Lamorte - OKRs.com, "OKRs and Compensation: 2 Mistakes to Avoid."** practitioner. **fetched-and-verified.**
`https://okrs.com/2026/02/okrs-and-compensation/`
Supports: the compensation boundary, and the nuance that the objection to sales quotas is about double measurement rather than comp linkage as such.
Quotable: "Business outcomes may influence compensation. OKR scores should not determine compensation."

**[57] Jeff Gothelf - "OKR Anti-pattern: Sandbagging your key results."** practitioner (author of Lean UX). **fetched-and-verified.**
`https://jeffgothelf.com/blog/sandbagging-okr-antipattern/`
Supports: the sandbagging anti-pattern and its link to compensation.
Quotable: "teams almost always sandbag their OKRs. Setting goals they know they can hit assures they not only keep their jobs but get their bonuses." / "they don't innovate. They don't stretch. They don't try new things."
Contested/time-bound: "almost always" is Gothelf's own characterisation, not a measured frequency. Do not restate it as one.

**[58] Tom Kerwin - Trigger Strategy, "OKRs sound good but they don't work (Part 1)."** practitioner. **fetched-and-verified.**
`https://triggerstrategy.substack.com/p/okrs-sound-good-but-they-dont-work`
Supports: the strongest-form critique, **and a critic naming the conditions under which OKRs did work for him**.
Quotable: "it's much safer for your career not to promise results." / "Every single other time, the OKRs have been bullshit, gamed, a wish-list, or a task-list."
Contested/time-bound: the author's personal experience across organisations, not a study. He reports one successful three-month period and names stable environments, clear measurable problems and genuine autonomy as the conditions.

**[59] Ant Murphy - "Escape OKR Theatre."** practitioner. **fetched-and-verified.**
`https://www.antmurphy.me/newsletter/escape-okr-theatre`
Supports: the OKR-theatre anti-pattern catalogue of nine hallmarks, including too many OKRs, non-measurable Key Results and cascading that mirrors the org chart. Also a critic conceding real value.
Quotable: citing Christian Idioti within the piece: "You want 10 teams working towards 1 goal, not 1 team with 10 goals."
Contested/time-bound: Murphy concedes OKRs deliver genuine focus and coherence "when executed properly."

**[60] Daniel Walters - "Are OKRs 'Management Malpractice'?"** practitioner. **fetched-and-verified.**
`https://www.greatcto.me/p/are-okrs-management-malpractice`
Supports: **the best critic-side concession found**, and the framing that misuse rather than the framework is the malpractice.
Quotable: "There is plenty of bad in the history of OKRs and in how many companies deploy them today." / "The best use of OKRs is for multi-directional alignment."

**[61] Antoinette Weibel with Meike Wiemann - Corporate Rebels, "The Dark Side Of OKRs (And Why We Should Care)."** academic (author is a professor of HRM at the University of St. Gallen), published on a practitioner platform. **fetched-and-verified.**
`https://www.corporate-rebels.com/blog/dark-side-of-okrs-and-why-we-should-care`
Supports: the surveillance and blinders critique, and an academic critic conceding goal-setting's value.
Quotable: "specific goals give a focus but at the same time can also act as blinders." / "a panopticon, a hardly visible but strongly felt control." / "clear goals are still needed to enable thriving."

**[62] Radhika Dutt - "Why OKRs Fail."** practitioner (author of Radical Product Thinking). **fetched-and-verified.**
`https://www.radicalproduct.com/blog/okrs-criticism`
Supports: the compensation-coupling anti-pattern and gaming.
Quotable: "people started gaming the system to get their bonuses"
Contested/time-bound: the Wells Fargo (roughly $3B in fines) and Lucent Technologies ($700M revenue overstatement) figures are Dutt's own citations within her piece and were **not** verified against any primary regulatory source. Do not restate them as established.

**[63] David Morrison - Applied Computing, "OKRs are Bullshit."** practitioner (dissenting voice). **fetched-and-verified.**
`https://blog.appliedcomputing.io/p/okrs-are-bullshit`
Supports: the rigidity critique and the no-true-Scotsman pattern in OKR advocacy.
Quotable: "we mostly rejected waterfall-style development a long time ago, and then promptly introduced a planning framework that encourages waterfall-style development."
Contested/time-bound: an opinion piece, not a measurement source.

**[64] John Cutler - "Why Quarterly OKRs?"** practitioner. **fetched-and-verified.**
`https://medium.com/hackernoon/why-quarterly-okrs-88113e885f56`
Supports: the cadence-mismatch anti-pattern.
Quotable: "quarterly planning hurts because it happens too infrequently (and at an artificial cadence)." / "90.25 days might be perfect for your company, 60 for the next, 30 for the next, or variable length periods for the next."

### Relationships, cadence and practice

**[65] Marty Cagan - Silicon Valley Product Group, "Outcomes Are Hard."** practitioner. **fetched-and-verified.**
`https://www.svpg.com/outcomes-are-hard/`
Supports: the root-cause framing of the OKR backlash, and the strongest statement of the roadmap boundary.
Quotable: "countless thousands of companies that thought that they could layer in the OKR technique on top of their existing, output-based product roadmap processes." / "The OKR technique originated from, and is predicated upon, the product model."

**[66] Marty Cagan - Silicon Valley Product Group, "Roadmap Alternative FAQ."** practitioner. **fetched-and-verified.**
`https://www.svpg.com/roadmap-alternative-faq/`
Supports: OKRs paired with a separate Product Scorecard, both KPI-based but serving different purposes.
Quotable: "The OKR's describe the outcomes that the team is focusing on right now... they are both KPI-based, and they complement each other, but they serve different purposes."
Contested/time-bound: Cagan's sharper "contrived mashup of outcomes and features" phrasing circulates in secondary summaries and was **not** found verbatim on this page. Attribute it to his wider corpus, not to this document.

**[67] Roman Pichler - "How to Combine Product Strategy, OKRs, and KPIs."** practitioner. **fetched-and-verified.**
`https://www.romanpichler.com/blog/product-strategy-okrs-and-kpis`
Supports: the strategy boundary and the KPI boundary, and the hazard of conflating a target with its metric.
Quotable: "What a product strategy is not, at least in my mind, is a set of objectives." / "a product strategy is more than a collection of OKRs. It provides the basis for discovering the right objectives."

**[68] Roman Pichler - "OKRs and Product Roadmaps."** practitioner. **fetched-and-verified.**
`https://romanpichler.medium.com/okrs-and-product-roadmaps-5c00773b32c0`
Supports: OKRs and outcome-based roadmaps as compatible rather than competing, with the roadmap goal doubling as the Objective if it is SMART.
Quotable: "What makes working with outcome-based goals like OKRs powerful ... is that they state *what* needs to be achieved but not *how*."
Contested/time-bound: assumes an outcome-based roadmap and does not address feature-list roadmaps. This is the softer of the two named positions; Cagan's [65] is harder.

**[69] Roger Martin - "Stop Letting OKRs Masquerade as Strategy."** practitioner (former Dean, Rotman School of Management). **fetched-and-verified.**
`https://rogermartin.medium.com/stop-letting-okrs-masquerade-as-strategy-a57fc2cea915`
Supports: **the sharpest named boundary claim on OKRs against strategy.**
Quotable: "OKRs must be a complement to strategy, not a substitute for strategy, as I have similarly argued previously about planning." / "Whenever anyone refers to their 'strategies,' I know they don't know what strategy is." / "desire (as with hope) is simply not a strategy."
Contested/time-bound: Martin's own strong normative position, not a neutral description. State it as his view. **Corrected on review 2026-07-30:** the first quotable above was used in the synthesis notes and in three drafted files while this entry listed only the other two, so the bundle was quoting something the log did not carry. Re-fetched and confirmed verbatim on the live page. **The defect was the log's, not the quote's**, and it is the reason the pre-draft verification pass missed it: that pass checked source entries against their sources, and never checked the log's own narrative sections against its source entries.

**[70] What Matters (Danielle Hughes) - "The Difference Between KPIs and OKRs."** vendor. **fetched-and-verified.**
`https://www.whatmatters.com/resources/difference-between-okr-kpi`
Supports: **the cleanest usable KPI boundary for this library**, including the lifecycle in which a KPI becomes a Key Result and then reverts.
Quotable: "KPIs often inform - and even become - your OKRs, if it's a measurement that you want to significantly change."

**[71] ClearPoint Strategy (Ted Jackson) - "OKRs vs. KPIs."** vendor (author has independent credentials and 30 years in strategy execution). **fetched-and-verified.**
`https://www.clearpointstrategy.com/blog/okrs-vs-kpis`
Supports: the health-metric against goal-metric distinction, and **a contrarian claim worth carrying**: that the framework choice matters less than execution discipline.
Quotable: "Run them together - almost everyone does. The argument over which to use was never the real fork in the road." / "Switching from KPIs to OKRs doesn't fix neglect. It just gives neglect a more ambitious name."
Contested/time-bound: a minority framing relative to the cleaner separation in [70]. Flag it as such if it is the only KPI-boundary source used.

**[72] What Matters (Billy Casey) - "Dear Andy: Are We Doing OKRs or Just Project Planning?"** vendor. **fetched-and-verified.**
`https://www.whatmatters.com/faqs/dear-andy-are-we-doing-okrs-or-just-project-planning`
Supports: the project-plan boundary.
Quotable: "OKRs describe what success looks like, and how it will be measured. OKRs do more than ensure that things happen on time and on budget (which are important, but lie more in the domain of project management)." / "If OKRs are a compass, then your project plan is a GPS that takes you from Point A to Point B turn by turn."
Contested/time-bound: **the "Dear Andy" framing implies Doerr answers personally; the byline is Billy Casey, a staff writer. Do not attribute this to Doerr or to Grove.**

**[73] Profit.co - "From Doerr's Book to Your Dashboard: Where Do Initiatives Actually Belong in OKRs?"** vendor. **fetched-and-verified.**
`https://www.profit.co/blog/okr-university/from-doerrs-book-to-your-dashboard-where-do-initiatives-actually-belong-in-okrs/`
Supports: **the load-bearing evidence that the Initiatives layer is vendor convention.** The article asserts Doerr's framework includes Initiatives while citing no page or quote for the structural claim.
Quotable: "John Doerr's OKR framework consists of Objectives, Key Results, and Initiatives"
Contested/time-bound: an absence-of-evidence finding, not a confirmed absence in Doerr's book, which could not be retrieved [13]. Combined with the silence of Google's own guide [6], it is enough to label Initiatives as convention rather than canon, and not enough to say Doerr never wrote it.

**[74] Perdoo (Felipe Castro) - "How to find the right OKR cadence."** vendor (Castro is a named independent coach publishing on a vendor blog). **fetched-and-verified.**
`https://www.perdoo.com/resources/blog/okr-cadence`
Supports: **the strongest source for cadence being convention rather than measurement**, and the named deviations.
Quotable: "It is a common misconception that OKR only works with quarterly cycles, which was the model Google used until 2011." / "The shorter the cadence, the smaller the OKR-setting overhead needs to be. The longer the cadence, the smaller the business uncertainty needs to be."
Contested/time-bound: the replacement for evidence is a heuristic, not data. No counter-source claiming quarterly is evidence-based was found anywhere in this research. The claim that Google added an annual layer after 2011 is Castro's and was not independently verified.

**[75] Perdoo (Nicole Capobianco) - "When it's ok NOT to be transparent with OKRs."** vendor. **fetched-and-verified.**
`https://www.perdoo.com/resources/blog/when-its-ok-not-to-be-transparent-with-okrs`
Supports: the clearest named dissent from absolute public visibility, with explicit carve-outs for M&A, restructuring, personal development goals and publicly traded financial exposure.
Quotable: "Transparency is the default, but it's not absolute. Knowing when to keep goals private is a sign of thoughtful leadership, not secrecy."

**[76] Henrik Kniberg - Crisp Blog, "Spotify Rhythm - how we get aligned" (2016).** practitioner (the consultant who wrote up the system). **fetched-and-verified.**
`https://blog.crisp.se/2016/06/08/henrikkniberg/spotify-rhythm`
Supports: **the correction to the widely repeated vendor claim that Spotify runs a six-month/six-week version of OKR.**
Quotable: "how we've gone through two other models (OKR and Priorities & Achievements) before arriving at our current model." / in the comments: "they reintroduced OKRs later, while also keeping the Rhythm."
Contested/time-bound: directly contradicts vendor framing of Rhythm as an OKR variant. Rhythm is what Spotify reached after moving away from OKRs, which were later reintroduced alongside it.

**[77] What Matters - FAQ, "Cascading top-down OKRs: What are some examples?"** vendor. **fetched-and-verified.**
`https://www.whatmatters.com/faqs/cascading-top-down-okr-examples`
Supports: that Doerr's own organisation describes OKRs flowing from executives downward while letting employees write their own Key Results, **and that it gives no bottom-up percentage at all**.
Quotable: "high-level OKRs flow downwards to department heads, managers, and individual employees."
Contested/time-bound: this is the check that puts the "40-60% of Key Results should be bottom-up" claim in the exclusion list. That figure is asserted by tertiary summaries and is absent from this primary-adjacent source.

**[78] WorkBoard - "OKR Performance Management Mistakes."** vendor. **fetched-and-verified.**
`https://www.workboard.com/resources/blog/okr-performance-management`
Supports: qualitative dissent on tying OKRs to compensation, through a named practitioner.
Quotable: Alexis Murphy, Chief People Officer at GHX: "If you tie their comp to it, they will sandbag it - full stop."
Contested/time-bound: the 96-against-81 sandbagging statistic was **checked against this source and is not present here.** It comes from [50], a different vendor's survey. Two researchers on this bundle disagreed about that figure for exactly this reason; the resolution is that it is traceable, to a small vendor self-report, and not to this page.

---

## Research access notes, for the next author

**Two primary books were never read directly and three open questions depend on them.** *High Output
Management* could be read only through roughly the first third to half of an Internet Archive text stream,
which stopped short of the Management by Objectives chapter [1]. *Measure What Matters* could not be fetched
at all because the available PDF exceeded the tool's size limit [13]. Anyone with physical or purchased copies
should check: whether the acronym "OKR" appears anywhere in Grove's book; whether Grove names Peter Drucker
anywhere; and whether Doerr's book establishes Objectives, Key Results and Initiatives as a three-layer
structure, and on what page.

**Five sources returned HTTP 403** and remain unread: Salesforce's own V2MOM blog post [21], a practitioner
V2MOM comparison [22], the ACM version of the systematic mapping [34], the Locke and Latham rebuttal [31],
and a hospitality-industry OKR paper [40]. The rebuttal in particular matters, because the bundle presents
*Goals Gone Wild* as one side of a live dispute and can currently vouch for only that side firsthand.

**Every untraceable statistic in the exclusion list came from vendor content published in the last two
years.** The two least traceable attach real institutional names to studies that one researcher searched for
and could not find [49]. That is a materially different research hazard from the misattribution and
quote-drift problems earlier bundles in this library met, and it is worth knowing about before the next pass.

## Verification pass, 2026-07-29

**This log was adversarially verified before any bundle file was drafted on it**, by thirteen agents: eight
re-fetching every load-bearing quote to confirm it verbatim, four attempting to refute the headline claims,
one synthesizing. That placement was deliberate. The previous bundle's format-count error originated in its
research fan-out and propagated verbatim into five documents before anyone added it up.

**It found two fabricated quotations in this log.** Entry [30] carried "Specific goals can induce tunnel
vision and cause decision makers to neglect other important areas" and "Goal setting can promote unethical
behavior as individuals focus on goal achievement at the expense of other considerations." **Neither sentence
exists in the paper.** Both were invented in the research fan-out and transcribed here unchecked. They are
replaced with verbatim text and the phrase "tunnel vision" is barred from the bundle as quoted material.

**It found one misattribution and one invented paraphrase.** Doerr's "not a silver bullet" was cited to the
Betterworks interview [51], which does not contain the phrase; it is [5]. And entry [5] rendered Doerr's
sentence as "In 1998, Doerr pitched OKRs to 24-year-old Larry Page and Sergey Brin" when the page reads "In
1998, when Larry Page and Sergey Brin were just 24 years old, I gave them my OKR pitch." **The correct
wording had already been read directly earlier in the same session and was still transcribed wrongly**,
which is worth recording: verifying a quote and then writing it from memory a few steps later reintroduces
exactly the defect the verification removed.

**It narrowed the single most load-bearing absence in the format verdict.** The V2MOM rejection rested on
"the module contains zero mention of OKRs." Only one unit of a longer Trailhead module had been fetched. The
claim now states the scope actually checked.

**All four headline claims survived**: no study measures the OKR artifact against outcomes, only one format
qualifies, committed versus aspirational is Google's framing, and the two institutional statistics could not
be traced. The fourth was softened because the agent commissioned to test it did not complete.
