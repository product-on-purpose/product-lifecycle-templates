# Research log: Acceptance Criteria bundle

Evidence trail for the companion, per the methodology's research protocol (§A6). Researched 2026-06-30.
**Citation integrity pass 2026-07-16 (WP-10): every reachable source fetched and verified against the
claims that cite it.** Corrections below, including one factual error.

## Sources consulted

| # | Source | Tier | Retrieval | Claims it supports |
|---|---|---|---|---|
| 1 | Dan North, "Introducing BDD" (Better Software, March 2006) | primary | **Fetched and verified 2026-07-16** at the canonical URL | BDD origin and 2006 date; Given/When/Then as context/event/outcome, verbatim: "Given some initial context (the givens), When an event occurs, Then ensure some outcomes". **Does NOT mention Gherkin** and prescribes nothing about single-action "When" |
| 2 | Scrum.org, "Difference Between DoD and Acceptance Criteria" | primary | **BLOCKED. HTTP 403 to automated fetch on 2026-06-30 and again 2026-07-16.** Publicly readable in a browser; never verified against its text | AC per-story vs DoD per-increment; PO owns AC, team owns DoD; AC at refinement, DoD up front; both needed for done. **All corroborated from search excerpts and cross-checked against the Scrum Guide [6], not read at source** |
| 3 | Ron Jeffries, "Essential XP: Card, Conversation, Confirmation," 2001 | practitioner | **Fetched and verified 2026-07-16** | The three C's, verbatim: "User stories have three critical aspects. We can call these Card, Conversation, and Confirmation." Confirmation as the acceptance test: "This component is the acceptance test". **Does NOT use "conditions of satisfaction"** |
| 4 | Thoughtworks, "BDD acceptance criteria in user stories" | practitioner | URL confirmed live 2026-07-16; body not re-verified claim by claim | AC as scenarios; scenarios convert to automated tests; written from the user's view |
| 5 | Cucumber / SmartBear, Gherkin reference | vendor | **Fetched and verified 2026-07-16** | Gherkin keywords; Given "put the system in a known state", When "describe an event, or an action", Then "describe an expected outcome, or result"; recommends 3-5 steps per example. **Gives no Gherkin origin date and does NOT say "one behavior per scenario"** |
| 6 | Scrum Guide 2020 | primary | **Fetched and verified 2026-08-08**, body read in full and counted programmatically (also verified for the `definition-of-done` bundle 2026-08-06) | Definition of Done as a Scrum commitment; DoD is "a formal description of the state of the Increment when it meets the quality measures required for the product"; an organisational DoD binds every team, verbatim "all Scrum Teams must follow it as a minimum", otherwise "the Scrum Team must create a Definition of Done appropriate for the product"; multiple teams on one product "must mutually define and comply with the same Definition of Done"; "The Developers are required to conform to the Definition of Done"; an item that does not meet it "cannot be released or even presented at the Sprint Review". **Zero occurrences of "acceptance criteria" and zero of "acceptance" in any form**, so the Guide names no AC concept and draws no AC-to-DoD boundary. **Does NOT state that a team may add criteria stricter than an organisational standard** (that is an inference from "as a minimum"), and says nothing about how often a DoD is revised |
| 7 | Ranorex, "When to Use Given-When-Then" | vendor | **Fetched and verified 2026-07-16** | Given-When-Then suits user-behavior cases; scenarios automate via Cucumber/Selenium. **Does NOT compare GWT to rule checklists, does not discuss team defaults, and does not say discrete rules belong in a list** |
| 8 | Master catalog entry 38 (Acceptance Criteria) | internal | On disk | Canonical form, aliases, Gherkin/BDD note, relationships |
| 9 | Aslak Hellesoy / Ben Linders, "Cucumber is 10 Years Old" (InfoQ, 2018) | primary | **Fetched and verified 2026-07-16** | Gherkin's real origin, in the creator's words: "I created Cucumber in 2008"; "I also decided to give the Given-When-Then syntax a name, to separate it from the tool. That's why it's called Gherkin"; "I extracted the Given-When-Then parser from RSpec" |
| 10 | Mike Cohn, *User Stories Applied*, 2004 | practitioner | **Print book, no URL. Not retrieved online**; cited from the book | "Conditions of satisfaction" as the story's AC |

## Corrections applied 2026-07-16 (WP-10 citation integrity pass)

Eight defects in a bundle the gate had always passed green, because check E proves anchors *resolve*,
not that a source *supports the claim*.

**One factual error, not just a citation error.** The companion stated: *"In 2007 the Gherkin syntax
formalized the Given/When/Then structure,"* cited to Dan North [1]. Three things were wrong:

- **The word "Gherkin" does not appear in North's article at all.**
- **The date is wrong.** Gherkin came with Cucumber, which Hellesoy created in **2008**, not 2007. In
  his own words he "extracted the Given-When-Then parser from RSpec" and named the syntax Gherkin "to
  separate it from the tool" [9]. 2007 belongs to North's RSpec story runner, not to Gherkin.
- **No cited source carried the date.** Cucumber's own Gherkin reference [5] gives no origin date, so
  the claim had no support anywhere in the reference list.

Fixed by rewriting the passage to the verified lineage (North 2006, then the RSpec parser extracted
into Cucumber and named Gherkin in 2008) and adding [9] as the source, in the creator's own words.

**Two combined entries split.**

- **Old [1]** read "Introducing BDD, 2006; Gherkin and Given/When/Then, 2007", bundling a source with
  a claim that source does not make. Now [1] is North's article alone, and the Gherkin origin is [9].
- **Old [3]** bundled "Ron Jeffries, 2001" with "Mike Cohn, *User Stories Applied*, 2004" under one
  entry **with no URL for either**. Now [3] Jeffries (URL added, verified) and [10] Cohn (a print
  book, labeled as such). The split immediately exposed a misattribution: **"conditions of
  satisfaction" is Cohn's term and does not appear in Jeffries**, yet [3] was cited for it.

**A stale URL that looked fine.** [1] pointed at `dannorth.net/introducing-bdd/`, which returns HTTP
200 but is a **318-byte redirect stub** whose canonical is `dannorth.net/blog/introducing-bdd/`.
Browsers follow the meta-refresh, so the link "worked" for humans and nobody noticed. Now canonical.

**The Ranorex claim, which WP-10 flagged and was right about.** [7] was cited five times and supports
**two** of them:

| Claim | Verdict |
|---|---|
| Scenarios convert to automated tests | **SUPPORTED**, kept |
| Given-When-Then suits genuine flows/behavior | **SUPPORTED**, kept |
| Rule-oriented and scenario-oriented "mix freely" | NOT SUPPORTED; de-cited and labeled this bundle's position |
| Discrete rules are clearest as a list | NOT SUPPORTED; de-cited and labeled a judgment |
| Some teams default to checklists, others to GWT | NOT SUPPORTED; no cited source surveys team defaults |

Per WP-10's instruction, the unsupported claims are now **labeled author judgment** rather than
re-sourced: the rule-vs-scenario framing is this bundle's contribution and is now presented as such.

**"Keep When to a single action"** was cited to North [1], who prescribes no such thing. Cucumber [5]
actually recommends **3-5 steps per example**. The beginner trap now cites Cucumber's real guidance,
and the single-action rule is labeled this bundle's own.

**This log was wrong too.** It previously recorded [5] Cucumber as supporting "one behavior per
scenario". Cucumber says something different ("You can have as many steps as you like, but we
recommend 3-5 steps per example"). Corrected above.

## Notes and limitations

**RESOLUTION ATTEMPT, 2026-08-08.** The remedy this note proposed was to read the page or re-source its
claims to the Scrum Guide. **The page still cannot be read**: a third attempt returned HTTP 202 with an
empty body behind a bot challenge. So the second path was taken, and it produced a finding larger than the
bundle.

**The 2020 Scrum Guide contains zero occurrences of "acceptance criteria", and zero of "acceptance" in any
form.** Counted programmatically over the full body text. The Guide therefore draws **no boundary at all**
between the Definition of Done and acceptance criteria: there is no sentence relating the two concepts. Any
claim in this library that cites the Scrum Guide for that boundary is unsupported by the primary text, and
the boundary is this library's own.

What the Guide **does** support, verbatim and re-confirmed: "The Developers are required to conform to the
Definition of Done", and "all Scrum Teams must follow it as a minimum" where an organisational Definition
of Done exists. **One correction to this library's own gloss**: "floor", "raise" and "never lower" are not
Guide vocabulary. "As a minimum" is. The paraphrase is faithful and must not be presented as a quotation.

**PER-CLAIM PASS APPLIED 2026-08-08.** The duplicate classification of all sixteen [2] citations
(re-source, keep-labelled, or cut) is at `_local/plans/2026-08-07_autonomous/F2-ac-403-verdicts.json`. The
two passes agreed on six re-sourcings and split four-ways on cut-versus-keep, so the split was adjudicated
against this log's own `Supports:` clauses rather than settled on one pass's authority.

**The adjudication overturned two verdicts the passes agreed on, and the disagreement is the useful part.**
Both passes read lines 14 and 19 as safe cuts because each sentence was dual-cited: drop the unread [2] and
the co-citation carries the claim. It does not.

| Line | Claim after the proposed cut | Remaining citation | What that source's `Supports:` clause actually carries |
|---|---|---|---|
| 14 | "observable outcomes from the user's point of view" | [3] Jeffries | The three C's, and "This component is the acceptance test". The entry records an explicit negative, "**Does NOT** use 'conditions of satisfaction'" |
| 19 | "give QA and engineering a concrete target before work starts" | [4] Thoughtworks | AC as scenarios; scenarios convert to automated tests; written from the user's view. Nothing about a pre-work target |

Applying either cut as proposed would have left a claim resting on a source that does not support it,
which is this library's dominant defect class manufactured by the fix rather than caught by it. Both are
instead re-grounded: line 14 attributes the user's-view half to [4], which does carry it, and labels the
surrounding definition as this bundle's; line 19 is labelled this bundle's reading outright. This is
[decision procedure 4](../../docs/internal/decision-procedures.md) - a review finding can be right while
its proposed fix is wrong - and it is the second time this bundle has produced that exact shape, after the
WP-10 pass proposed substituting one Jeffries/Cohn entry for another that carried the claim no better.

**The four genuine splits, and how each was settled.** (A fifth line, 140, was not split but was
narrowed on the same principle; it is listed last.)

- **Line 67** (lean-variant field description): **cut**. Section 3 describes this bundle's own template
  sections and every other field description there is uncited; the clause immediately after this one
  already says "that is this bundle's judgment, not a sourced claim". A citation on a sentence that
  disclaims being sourced two clauses later is incoherent either way.
- **Line 125** ("the DoD is set once, up front, and revised rarely"): **cut**, and on stronger grounds than
  unsourcedness. This library's own [`definition-of-done` bundle](../definition-of-done/definition-of-done_companion.md)
  names the opposite as a measured failure mode twice: anti-pattern 2, "the DoD written once and never
  revisited", carrying 15 of 137 surveyed practitioners whose DoD "have never been updated"; and
  anti-pattern 8, "the static DoD, read as a strength". A companion contradicting a sibling companion is a
  defect the gate cannot see and [`review-standards.md`](../../docs/internal/review-standards.md) section 2
  names it directly.
- **Line 126** ("done only when it meets both"): **citation cut, sentence kept as labelled synthesis**. The
  DoD half is Guide-sourced and the AC half is Jeffries'; marking the sentence "per unread source" would
  have understated its support in the opposite direction.
- **Line 148** (anti-pattern restating the what-not-how principle): **cut, and deliberately not
  re-cited to [3]**, which one pass proposed. [3] does not carry that principle either. The line now points
  back to section 1, where the principle is stated and labelled as this bundle's framing.
- **Line 140** ("who writes them"): **kept, but narrowed.** [2]'s `Supports:` clause carries "PO owns AC"
  and "AC at refinement" and nothing else. The collaborative-authorship rationale, that engineering and QA
  should flag risky assumptions before the sprint, was never recorded as [2]'s, so it moved into the
  sentence's own *Recommendation*, which is already this bundle's voice.

**An adversarial pass over this adjudication then caught four more, three of them introduced by the fix
itself.** Five independent lenses re-read the change against these `Supports:` clauses; eight findings
survived an opus-level judging pass, and the useful ones were all of one kind: **a citation left carrying
more of its sentence than the log grants it.** Line 22 read "per-story **and functional**" under [2], whose
clause carries the per-story contrast only. Line 26's "describing *what*, not *how*" had no home in [2] at
all and is now labelled. And line 125's replacement, written in this pass, said the DoD "is created
**once**" under [6], reintroducing as a creation count exactly the cadence claim the same sentence's
correction note had just cut, against a `Supports:` clause that says outright the Guide "says nothing about
how often a DoD is revised". **Writing a fix is not exempt from the rule the fix enforces**, and three of
eight confirmed findings were defects this pass created rather than found.

**Disposition of all sixteen:** six re-sourced to the Guide [6], seven cut, one unchanged (the 2026-08-06
correction note in the companion's section 6, which already disclosed that [2] was never read), two kept as
live claims, each narrowed to the clause [2] is recorded as supporting and marked unverified at the point
it is made. The Guide entry [6] above was expanded in the same pass, because moving six claims onto a
`Supports:` clause that did not yet describe them would have recreated the defect one reference to the left.

**Two defects of the same class were confirmed outside this pass's scope and are recorded, not fixed here,
because scope discipline is what makes this diff auditable against the verdicts file.** First, [7] Ranorex
is cited in section 4 and again in section 6 for a **comparison** between rule checklists and
Given/When/Then, while its `Supports:` row states it "**does NOT** compare GWT to rule checklists". The
2026-07-16 pass de-cited three [7] claims but abstracted a fourth in a way that kept the comparison under
the citation. Second, the [3] Jeffries entry supports the three C's and nothing about observable outcomes,
which is why line 14 was re-grounded rather than left to [3]; no other [3] citation was audited in this
pass.

- **[2] Scrum.org is the load-bearing source for the AC-vs-DoD distinction and is the most-cited
  reference in this bundle (16 citations), yet it has never been read at source.** It returns HTTP 403
  to automated retrieval. Its claims are corroborated by search excerpts and are consistent with the
  Scrum Guide [6], which was verified, but this is the weakest evidence in the bundle and is now
  labeled as such in the reference itself. A human should read the page and confirm, or the claims
  should be re-sourced to the Scrum Guide where it covers them.
- **[4] Thoughtworks** was confirmed live but not re-verified claim by claim in this pass. Its claims
  are uncontested and corroborated by [5] and [7].
- **[10] Cohn is a print book with no URL**, cited from the book rather than retrieved. This is the
  book/pre-web format case that WP-10e will codify in the methodology.
- Vendor sources ([5], [7]) are used for Gherkin convention and form-selection guidance, not for
  contested claims of fact.
- No time-bound regulatory claims appear in this bundle.
