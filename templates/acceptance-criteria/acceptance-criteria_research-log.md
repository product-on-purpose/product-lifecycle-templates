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
| 6 | Scrum Guide 2020 | primary | Verified (prior bundle); URL confirmed live 2026-07-16 | Definition of Done as a Scrum commitment; AC not separately named |
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
