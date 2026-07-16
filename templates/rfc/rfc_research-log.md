# Research log: RFC bundle

Evidence trail for the companion, per the methodology's research protocol (§A6). Researched
2026-07-15 across two source sweeps (origins/primary, and modern practice/debates), synthesized
2026-07-16.

Reference numbers match the companion's [References](rfc_companion.md#references) for rows 1-20.

## Sources consulted

| # | Source | Tier | Retrieval | Claims it supports |
|---|---|---|---|---|
| 1 | Crocker, "Host Software," RFC 1, 1969 | primary | **Fetched RAW and verified verbatim** (rfc-editor.org/rfc/rfc1.txt, 2026-07-15) | The RFC series began 1969-04-07; the origin of the request-for-comment posture. Verbatim: "Very little of what is here is firm and reactions are expected"; "I present here some of the tentative agreements reached and some of the open questions encountered" |
| 2 | Crocker, "Documentation Conventions," RFC 3, 1969 | primary | **Fetched RAW and verified verbatim** (rfc-editor.org/rfc/rfc3.txt, 2026-07-15) | The series' deliberate informality. Verbatim: "Notes are encouraged to be timely rather than polished"; "we hope to promote the exchange and discussion of considerably less than authoritative ideas" |
| 3 | Bradner, "The Internet Standards Process, Rev 3," RFC 2026 (BCP 9), 1996 | primary | Fetched by research agent (processed summary, not raw) | The IETF RFC as the archival, official publication channel; the maturity levels; published post-discussion. **Paraphrased, not quoted** |
| 4 | Crocker, "Today's Internet Still Relies on... The Request for Comments," IEEE Spectrum, 2020 | primary | Fetched by research agent (processed summary) | Crocker's own reflections that even "proposal" felt too strong; the NWG's lack of authority. **Paraphrased, not quoted** |
| 5 | Crocker, "How the Internet Got Its Rules," NYT op-ed, 2009 | primary | **PAYWALLED, NOT fetched.** Only the lede was recoverable via a mailing-list archive | Cited as Crocker's best-known reflection on RFC origins. **The companion quotes nothing from it** |
| 6 | Flanagan and Ginoza, "RFC Style Guide," RFC 7322, 2014 | primary | Fetched by research agent (processed) | Published RFCs are corrected by errata or by a new obsoleting RFC, never by editing the original: the permanence mechanism. **Paraphrased** |
| 7 | Nygard, "Documenting Architecture Decisions," 2011 | practitioner | Verified in the ADR bundle's research | The ADR as the post-decision counterpart to the RFC |
| 8 | Fowler, "Architecture Decision Record" | practitioner | Verified in the ADR bundle's research | Nygard as ADR origin; the ADR contrast |
| 9 | Calcado, "A Structured RFC Process," 2018 | practitioner | Fetched by research agent | The explicit IETF-vs-internal-engineering-RFC distinction; the pre-decision lifecycle. **Paraphrased** |
| 10 | Orosz, "Companies Using RFCs or Design Docs," Pragmatic Engineer | practitioner | Fetched by agent (**partially paywalled**; free portion only) | Spread across Uber/Google/Amazon/Stripe/Spotify; Uber's DUCK precursor; PRD-beside-RFC; RFC/design-doc interchangeability. **Paraphrased; the paywalled detail is not relied on** |
| 11 | Dagdeviren, "ADRs and RFCs: Differences and When to Use Which" | practitioner | Fetched by research agent | The RFC(pre-decision)/ADR(post-decision) boundary; an accepted RFC can spawn multiple ADRs. Same author the ADR bundle used |
| 12 | Dagdeviren, "How and Why RFCs Fail" | practitioner | Fetched by research agent | Anti-patterns: rubber-stamp, template bloat, wrong audience, missing business need, culture prerequisite. **Paraphrased** |
| 13 | The Rust RFC Book + RFC 0002 (RFC Process), from 2014 | primary | Fetched by research agent | An early, much-copied open-source RFC process: PR-based, subteam sign-off, 10-day Final Comment Period, "not a rubber stamp." **Paraphrased** |
| 14 | React RFCs (README + 2017 announcement) | primary | Fetched by research agent | Two-class system (team vs community RFCs); most community RFCs do not merge; 3-day FCP; cites Yarn/Ember/Rust. **Paraphrased** |
| 15 | Oxide Computer, RFD 1 (blog + RFD 0001 + podcast) | primary | Fetched by research agent (blog/RFD processed; naming rationale from a podcast transcript) | The rename to "Requests for Discussion" to avoid IETF conflation; six RFD states; covers culture as well as code. **Paraphrased**; the podcast quote was NOT independently verified, so it is not quoted |
| 16 | Kaplan-Moss, "RFC processes are a poor fit for most organizations," 2023 | practitioner | Fetched by research agent | The sharp Camp-B critique: endless discussion at scale, rewarding writing-to-exhaustion, blindness to power dynamics; the "document, discuss, THEN decide" prescription. **Paraphrased** |
| 17 | Squarespace Engineering, "The Power of 'Yes, If'," 2019 | practitioner | Fetched by research agent | Comment pile-on as a real failure; named approvers and "yes, if"; adding synchronous review on top of async. **Paraphrased** |
| 18 | Python PEP 1 | primary | Fetched by research agent | PEPs as a governance cousin with their own lifecycle and a "Provisional" state. **Paraphrased** |
| 19 | Joshi, "Planning for Change with RFCs," Increment, 2021 | practitioner | Fetched by research agent | The format's spread across Ember/React/Vue/Swift/Rust and companies; the egalitarian framing. **Paraphrased** |
| 20 | "RFCs vs ADRs," DesignDoc.tech | vendor | Fetched by research agent (verbatim extract available) | The clean temporal RFC/ADR distinction. **Paraphrased**, used as corroboration of [11] |

## Findings that shaped the bundle

**1. The name inverted itself twice, and that is the companion's spine.** Crocker's 1969 RFC was
deliberately provisional and non-authoritative [1][2]. The IETF RFC evolved into a permanent,
post-consensus standard, so its "Request for Comments" is now nominal [3][6]. The corporate
engineering RFC borrowed the name a second time for a pre-decision proposal, and in doing so landed
closer to Crocker's original spirit than the IETF ever kept [9][10]. This is not a stylistic
observation; it is why "RFC" is ambiguous and why the bundle has to say up front which RFC it teaches.

**2. Every serious critique of RFCs is really a critique of RFCs without a decider.** The Camp-A/
Camp-B debate [16][17][19] resolves on one axis: a named authority and a deadline. That finding drove
two template choices: the full variant asks for `reviewers` and a `review_by` date, and even lean
carries an Outcome section.

**3. "No decision recorded" is the most-cited failure, so Outcome is mandatory at every size.** Across
sources the recurring rot is an RFC abandoned at `in-review` after the decision was made elsewhere
[12][16]. Making Outcome a required section, and the bridge to the ADR, is the countermeasure.

**4. There is no `develop-rfc` skill.** pm-skills has `develop-adr` but nothing that generates an RFC,
despite the RFC preceding the ADR. `pairs_with` is empty, and the gap is recorded as a finding.

## Corrections and disciplines applied

**The quotation discipline held; the paraphrase discipline did not, and a round-two audit caught it.**
The draft was written under a rule learned the hard way on the ADR bundle - research-agent output is a
summary, and a summary is not a quotation - and that rule protected the *quotations*. But on
2026-07-16 an adversarial citation pass (raw-source verification of the load-bearing practitioner
paraphrases, run in the main loop after the delegated reviewer hit an auth error) found that several
*paraphrases* were attributed to sources that do not support them. All were corrected before the
bundle was committed. This is recorded, not hidden, because a research log that claims a clean pass it
did not have is the same defect it exists to prevent.

**What held (verbatim quotations):**

- **Only two quotations appear in the companion, both from RFC 1 and RFC 3.** All four quoted phrases
  ("tentative agreements... open questions encountered" and "Very little of what is here is firm and
  reactions are expected" from RFC 1; "timely rather than polished" and "considerably less than
  authoritative ideas" from RFC 3) were **re-verified verbatim against the raw primary text** in the
  round-two pass [1][2]. No quotation defect was found.

**What did not hold (paraphrase misattributions found and fixed 2026-07-16):**

- **[16] Kaplan-Moss URL was dead.** The reference pointed at `.../rfc-considered-harmful/`, which
  404s; the correct slug is `.../against-rfcs/`. Fixed, and the article's supported claims
  (endless-discussion/no-decision-framework, "write to exhaustion" - verified near-verbatim,
  "document, discuss, then decide") re-confirmed against the live page.
- **Non-goals claim was miscited to [17] Squarespace**, which never mentions non-goals. The citation
  was removed and the doubled "single most reliable way" superlative dropped; the point now stands as
  an uncited craft assertion.
- **"No alternatives" and "the rubber stamp" were miscited to [12] Dagdeviren.** Neither is among the
  nine failure modes that article actually names (its list was fetched in full to check). The rubber
  stamp arguably *inverts* Dagdeviren's point (he argues the "what" *should* precede the RFC). Both
  citations were removed; the anti-patterns remain as widely-observed craft.
- **The "stuck at in-review forever" rot was miscited to [16]**; that failure is Dagdeviren's #7
  ("Don't Publish and Forget; Follow Up"), so it was re-pointed to [12].
- **Anti-pattern #1 contradicted its own source.** It read "the default outcome is not 'no'; it is
  nothing," but Kaplan-Moss [16] says the default outcome *is* "no." Reworded to "default outcome is
  inaction... stalls in an open thread," which both camps' wording supports.
- **Two [17] Squarespace claims overreached** and were softened: "reports its process caught" became
  "redesigned its process specifically to catch" (the article frames flaws as the motivating problem,
  not a measured result), and an unsupported causal claim (synchronous review added "precisely because
  async-only produced shallow engagement") was cut to what the article states.
- **[16] power-dynamics claim was an extrapolation** ("block through sheer persistence without formal
  authority") and was pulled back to the article's actual wording (processes are "insensitive to power
  dynamics," companies "don't operate in an even, egalitarian manner").

**Remaining discipline that held from the first draft:** every other practitioner line (Oxide's naming
rationale, the DesignDoc.tech RFC/ADR formulation) is **paraphrased and cited**, not quoted, because
those came through processed agent fetches not independently verified against raw sources.
- The NYT op-ed [5] is paywalled and was not read; the companion cites it as Crocker's known
  reflection but quotes nothing from it.
- The Pragmatic Engineer article [10] is partly paywalled; only its free portion is relied on, and no
  paywalled detail (e.g. the full DUCK structure) is asserted as fact.
- The AI-era angle was investigated and **deliberately omitted**: the second research sweep found no
  retrieved evidence of engineering RFCs being used as AI-agent context (only adjacent, differently-
  scoped work). Rather than inflate a thin thread into a section, the companion says nothing about it.
  This is the opposite of the ADR bundle's first-draft mistake, where a single vendor preprint was
  overstated.

## Notes and limitations

- **Three primary sources were fetched only as processed summaries, not raw** ([3] RFC 2026, [6] RFC
  7322, [18] PEP 1). Their content is well-established and the companion paraphrases rather than
  quotes them, so the risk is low, but a verbatim pass would be a cheap future improvement if any of
  their specifics become load-bearing.
- **One memorable quote was deliberately not used.** Oxide's "avoid conflation with the IETF
  construct" rationale [15] came from a podcast transcript the agent fetched but that was not
  independently verified; the companion paraphrases the rename rationale instead of quoting it.
- **No quantitative evidence** on whether RFC processes help or harm engineering velocity was found in
  either sweep; all practitioner claims are qualitative. The companion's debate section reflects that
  by naming camps rather than asserting a settled answer.
