# business-case research log

Researched 2026-08-04 across six parallel dimensions: standards and canonical definition, structure in
practice, financial appraisal, failure modes and critique, the product-team context, and boundaries and
lifecycle. **43 sources**, of which **33 fetched-and-verified**, **2 url-confirmed-not-read**, and
**8 not-retrieved**. Retrieval status is recorded per source in the three-token vocabulary the library gates
([ADR 0029 (the research-log contract gate)](../../docs/internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md)),
and only `fetched-and-verified` sources are quoted.

**How to read this log.** A `Supports:` clause says what the bundle is allowed to rest on that source for.
A `Quotable:` phrase was read verbatim on the page. If a claim in the companion is not covered by some
entry's `Supports:` clause here, the claim has no home and must be cut, not justified after the fact.

**The eight `not-retrieved` entries are load-bearing and are listed deliberately.** They are the sources a
reader would most expect a business case bundle to cite, and this research could not read any of them. They
are recorded so that no draft can quietly assume them. In particular, PMBOK 7 is named as a key source in
this type's own build spec and **could not be retrieved**, so nothing in this bundle may state what PMBOK 7
says.

---

## Honest framing: the seven things this bundle has to say

**1. Every standard that could be read in full says the business case is a living document, and most people
use it as a one-time gate.** This is the central teaching point. HM Treasury's guidance states it outright:
"A business case is a 'living document'. It should be revisited and updated as the proposal develops" [1].
PRINCE2 goes further and makes it a named principle, continued business justification, with a consequence
attached: "If, at any point, the business case becomes invalid, the project should be halted" [2]. APM
agrees the case "is reviewed and revised at decision gates as more mature estimates and information become
available" [3]. Three independent bodies, no dissent among the sources that could be verified.

**2. They agree on the principle and differ on the mechanism, and the difference is real.** PRINCE2 keeps
**one evolving document** revised in place, checked at every stage boundary via a four-step
Develop/Check/Maintain/Confirm technique [2]. The Green Book instead stages **three formally separate
documents** at three approval gates: Strategic Outline Case (scoping), Outline Business Case (planning),
Full Business Case (procurement) [1]. Both reject the one-time-gate framing; they are not the same operating
model, and a template has to pick one or support both explicitly.

**3. Product-management literature is hostile or silent, and that is the finding rather than a gap in the
research.** Marty Cagan names the cycle almost verbatim in order to reject it: "provide a business case for
the project, get funding for the project, staff the project, ship the project, hope nobody checks actual
results against the business case, rinse and repeat," which he calls "epic amounts of waste" [26]. He also
has a section titled *Product Management is not defining the business case*, conceding the artifact serves
investment decisions but stating "this doesn't really do anything to contribute to actually creating the
product" [27]. Perri's *Escaping the Build Trap*, per the secondary treatment read, never engages the
artifact [28]; a targeted search of Teresa Torres's continuous-discovery material surfaced no use of the
term at all [30]. **No product-management source found makes a positive case for this document.** The
bundle must say so rather than implying a product audience endorses it.

**4. The alternatives section is the load-bearing one, and the two traditions place it differently.** The UK
government family folds options inside the Economic Case, as a longlist at SOC stage narrowing to a
shortlist and preferred option at OBC stage, with no standalone heading [4][5]. The practitioner and
PMI-adjacent family gives it its own named section mid-document: "Alternative Analysis" as section 7 of 8
[9], "Option analysis" as section 5 of 10 [8]. PRINCE2 requires business options including a mandatory *do
nothing* baseline [2]. Neither ordering is more authoritative; both traditions treat comparison against a
named alternative as non-optional in substance. **A business case naming no alternative is a proposal.**

**5. The most repeated "fact" about IRR is a documented fallacy, and the source a business-case author is
most likely to consult states it as settled.** Magni and Martin: "There are no reinvestment rate
assumptions built into, or implicit to, the computation and use of either the IRR or NPV" [11]. Corporate
Finance Institute states the opposite as IRR's "critical flaw": it "assumes all positive cash flows of a
project will be reinvested at the same rate as the project" [14]. This is a genuine academic-versus-
practitioner split running through the same tier of sources a reader will meet, and the bundle must present
it as contested rather than picking the version it prefers. See the contested register.

**6. Flyvbjerg's distinction must not be blurred, and it is not a binary.** "Optimism bias and strategic
misrepresentation are both deception, but where the latter is intentional, i.e., lying, the first is not,
optimism bias is self-deception" [19]. He argues the two are **complementary rather than competing**, with
the balance set by political and organisational pressure, so strategic misrepresentation dominates on
high-stakes visible projects and optimism bias on smaller ones [19]. Flattening this into "sometimes people
are wrong, sometimes they lie" loses the mechanism. His proposed fix, reference class forecasting, is
designed to bypass both at once without diagnosing which is operating [19], and HM Treasury operationalises
essentially that idea as mandatory percentage uplifts by project type [21].

**7. The famous benefits-realisation statistics are quarantined, not cited.** The figures that circulate
together in practitioner writing - 13 percent of organisations tracking benefits to realisation (KPMG
2005), 17 percent reporting high benefits-realisation maturity (PMI 2016), 56 percent less value than
predicted across 5,400+ IT projects (McKinsey/Oxford) - were **not independently verified**. The PMI
document was confirmed genuine but the 17 percent figure was not located in the pages read [24]; the
McKinsey and KPMG originals could not be fetched [39][40]. Standish CHAOS figures carry published academic
criticism of their methodology and sampling [41]. **None of these numbers may appear in this bundle as
fact.** The one large statistic that does trace cleanly is Flyvbjerg's nine-in-ten cost overrun figure,
which resolves to his own named database and cited studies [20], and the contrast between the two is itself
worth teaching.

---

## Format verdict (ADR 0028)

Under [ADR 0028 (the format-axis rule)](../../docs/internal/decisions/0028-adopt-a-format-axis.md) a format
ships only when it is **structurally distinct** and **in circulation with a named source**. Four candidates
were considered.

| Candidate | Structurally distinct? | Named source in circulation? | Verdict |
|---|---|---|---|
| **Five Case Model** (strategic, economic, commercial, financial, management) | Yes. Five named cases, options folded inside the economic case, staged SOC/OBC/FBC | Yes. HM Treasury, and implemented by Scottish Government [1][4][5][6] | **Ships** as the full variant's spine |
| **Practitioner / PMI-adjacent** (options as its own numbered section) | No. Same five recurring elements, different order and headings | Yes [8][9] | **Rejected.** Reordering is not a distinct structure |
| **PRINCE2 business case** | No. Content parallels the five cases; the difference is lifecycle mechanism, not document shape | Yes [2] | **Rejected as a format.** Its living-document mechanism is taught in the companion instead |
| **SAFe Lean Business Case** | **Yes, genuinely.** Substitutes an Epic Hypothesis Statement, business-outcomes hypothesis and leading indicators for a financial case, and defers cost modelling until an MVP validates the hypothesis [7] | **Weakly.** Scaled Agile Inc. owns the format, but this research read a practitioner mirror, not Scaled Agile's own page | **Deferred, with the gap named** |

**On the SAFe Lean Business Case, and the reason it is deferred rather than rejected.** It is the strongest
format candidate found: it is not a shorter business case but a different document, and the distinction
between reducing page count and changing what the document argues is exactly what ADR 0028's admission test
is for. It is deferred only because the format's own publisher was not read. That is a retrieval gap, not a
judgment that the format fails the test, and it is stated here so a later pass can close it by fetching
Scaled Agile's own page rather than re-deriving the question.

**So one format ships**, with `lean` and `full` weights on it. The lean variant carries Problem and
Opportunity, Options Considered, and Recommendation; the full variant adds Costs, Benefits, Risks and
Financials. The hypothesis-driven alternative is taught in the companion as a real and named option a reader
may be right to prefer, without being shipped as a second format on a source this research did not read.

---

## Sources

### Standards and canonical definition

**[1] HM Treasury and Welsh Government. "Guidance on Developing Business Cases for Projects and Programmes" (2026 edition, ISBN 978-1-918417-58-6, PU3650).** primary. **fetched-and-verified.**
`https://assets.publishing.service.gov.uk/media/6a4390675b6406df58c14006/Guidance_on_Developing_Business_Cases.pdf`
Supports: the Five Case Model's five required dimensions and their contents, the SOC/OBC/FBC staged
process, the explicit living-document framing, and the Gate Review structure.
Quotable: "A business case contains the information needed to make a decision on a public sector spending
proposal." / "The process of developing a business case matters as much as the final document. It is not
merely a writing exercise or something to complete in order to obtain approval." / "A business case is a
'living document'. It should be revisited and updated as the proposal develops. As new information and new
analysis is generated in the business case process, practitioners may need to review and adjust their
previous assumptions." / "The strategic case is fundamental to the business case process. It drives the
identification and appraisal of options in the economic case." / "Strategic Outline Case (SOC): ... It is
the scoping phase of the project." / "Outline Business Case (OBC): ... It is the planning phase of the
project." / "Full Business Case (FBC): ... It is the procurement phase of the project."

**[2] prince2.wiki. "Business Case" theme summary, a practitioner mirror of the AXELOS PRINCE2 manual's Business Case theme.** practitioner. **fetched-and-verified.**
`https://prince2.wiki/theme/business-case/`
Supports: PRINCE2's treatment of the business case as a continuously maintained document under the
continued-business-justification principle, its four-step Develop/Check/Maintain/Confirm technique, and its
standard content structure including a mandatory do-nothing option.
Quotable: "desirable, viable, and achievable as a means to support decision-making in its continued
investment" / "Assess whether the project is still worthwhile" / "Keep the business case updated with
actual progress and current forecasts" / "Assess if the intended benefits have been or will be realized" /
"If, at any point, the business case becomes invalid, the project should be halted."
Contested/time-bound: this is a practitioner mirror, not AXELOS's own manual. It is used for PRINCE2's
structure and mechanism, which it states consistently and in detail; it is not treated as AXELOS's
authoritative wording.

**[3] Association for Project Management. "What is a business case?", the APM resource page drawing on the APM Body of Knowledge 7th edition.** standards. **fetched-and-verified.**
`https://www.apm.org.uk/resources/what-is-project-management/what-is-a-business-case/`
Supports: APM's own definition, its five key elements, its statement that the case is revised at decision
gates, and its ownership assignment.
Quotable: "A business case provides justification for undertaking a project, programme or portfolio. It
evaluates the benefit, cost and risk of alternative options and provides a rationale for the preferred
solution." / "The business case is reviewed and revised at decision gates as more mature estimates and
information become available." / "The sponsor owns the business case"

### Structure in practice

**[4] Scottish Government, Digital Scotland Service Manual. "Strategic Outline Case".** primary. **fetched-and-verified.**
`https://servicemanual.gov.scot/writing-business-case/strategic-outline-case`
Supports: the full ordered 18-item section list for the SOC stage of the five-case model, showing options
analysis (longlist then shortlist) placed inside the Economic Case, after the Strategic Case and before the
Commercial, Financial and Management cases.
Quotable: "Write a concise and comprehensive overview of the document's content, key conclusions and
principal recommendations."

**[5] Scottish Government, Digital Scotland Service Manual. "Outline Business Case".** primary. **fetched-and-verified.**
`https://servicemanual.gov.scot/writing-business-case/outline-business-case`
Supports: the ordered five-case section list for the OBC stage, and that no section is literally titled
Options or Alternatives at this stage, option comparison being folded into the Economic Case as shortlisted
options, preferred option and sensitivity analysis.

**[6] Scottish Government, Digital Scotland Service Manual. "Business case" overview and "Final Business Case".** primary. **fetched-and-verified.**
`https://servicemanual.gov.scot/writing-a-business-case`
Supports: the three-phase SOC/OBC/FBC structure and the five-case model as the organising frame, and that
writing a business case is iterative rather than linear.
Quotable: "a live, practical tool" / "writing a business case is not a linear process"

**[7] agility-at-scale.com. "SAFe Lean Business Case: From Epic Hypothesis to Go/No-Go".** practitioner. **fetched-and-verified.**
`https://agility-at-scale.com/safe/lpm/lean-business-case/`
Supports: the ordered 8-field structure of the SAFe Lean Business Case (Epic Hypothesis Statement,
Business Outcomes Hypothesis, Leading Indicators, Non-Functional Requirements, MVP, in and out of scope,
background analysis, Go/No-Go recommendation) and the page-count contrast with traditional business cases.
Quotable: "The LBC takes the opposite approach: it acknowledges uncertainty and builds in mechanisms to
learn fast." / "defers detailed planning until learning validates the hypothesis" / "spending months
building a comprehensive financial model based on assumptions"
Contested/time-bound: this is a practitioner mirror of a format published by Scaled Agile Inc. The format's own
publisher page was not read, which is why the format is deferred rather than shipped. See the format
verdict.

**[8] Slideworks. "How to Write a Solid Business Case (with Examples and Template)".** practitioner. **fetched-and-verified.**
`https://slideworks.io/resources/how-to-write-a-solid-business-case-examples-and-template`
Supports: a 10-section practitioner ordering with Option analysis as its own section between the high-level
solution and the recommended solution; that the executive summary is written last though placed first; and
that the structure is offered as a recommendation rather than a requirement.
Quotable: "The executive summary should be the final thing you write." / "In our experience, the business
case structure below is the most logical and effective, but you should generally use whatever format or
template your company uses."

**[9] ProjectManagementDocs.com. Business Case template.** practitioner. **fetched-and-verified.**
`https://www.projectmanagementdocs.com/template/project-initiation/business-case/`
Supports: an 8-section PMI-adjacent ordering in which Alternative Analysis is an explicitly named section
placed after cost-benefit analysis and before approvals, a different placement from the UK model.
Quotable: "provides general information on the issues surrounding the business problem" / "costs of the
project and compare them with the benefits and savings"

**[10] UK Cabinet Office and HM Treasury. "The Green Book and accompanying guidance" collection.** primary. **fetched-and-verified.**
`https://www.gov.uk/government/collections/the-green-book-and-accompanying-guidance-and-documents`
Supports: the existence and current titles of the two operative documents anchoring the five-case model as
the UK government's recommended framework.
Contested/time-bound: this page does not itself state that options analysis is mandatory. That language lives in the
full guidance PDF, whose extraction degraded. See the contested register.

### Financial appraisal

**[11] Carlo Alberto Magni and John D. Martin. "The Reinvestment Rate Assumption Fallacy for IRR and NPV: A Pedagogical Note"** primary.  (MPRA Paper No. 83889). **fetched-and-verified.**
`https://mpra.ub.uni-muenchen.de/83889/1/MPRA_paper_83889.pdf`
Supports: that the claim IRR and NPV assume reinvestment at the IRR or discount rate is a widely repeated
fallacy rather than a mathematical fact, and the historical origin of the confusion.
Quotable: "There are no reinvestment rate assumptions built into, or implicit to, the computation and use
of either the IRR or NPV. Once an investment's cash flows are received they can be distributed to the
firm's creditors or shareholders without any necessity to reinvest them." / "Dudley (1972, p. 908) put it
bluntly, \"There is no such assumption implicit in the technique\"." / "We conclude that the reinvestment
assumption is a sufficient condition, not an implicit assumption, for solving the problems of conflicting
ranking and multiple IRRs." / "In the 1950s the finance literature devoted to the analysis of mutually
exclusive investment projects and the analysis of multiple IRRs both incorporated consideration for
reinvestment rates. The discussion of reinvestment rates in this context, we believe, may well be the
source of the confusion about reinvestment rates and project IRRs and NPVs."
Contested/time-bound: only pages 1-2 could be read. The paper's technical sections on the multiple-IRR problem and the
modified IRR were not retrieved, so no claim about their content is made.

**[12] Aswath Damodaran. "Real Option Valuation"** primary.  (Chapter 5, *Investment Valuation* 2nd ed. **fetched-and-verified.**
course text), NYU Stern.
`https://pages.stern.nyu.edu/~adamodar/pdfiles/DSV2/Ch5.pdf`
Supports: the definition of real option valuation, the three option types (delay, expand, abandon), and the
practical limits of applying option-pricing mathematics to real investment decisions.
Quotable: "The real options approach is the only one that gives prominence to the upside potential for
risk, based on the argument that uncertainty can sometimes be a source of additional value, especially to
those who are poised to take advantage of it." / "In its binomial version, there can be only two outcomes
at each stage and the probabilities are not specified." / "The value of learning is greatest, when you and
only you have access to that learning and can act on it. After all, the expected value of knowledge that is
public, where anyone can act on that knowledge, will be close to zero."

**[13] Corporate Finance Institute. "Net Present Value (NPV)".** practitioner. **fetched-and-verified.**
`https://corporatefinanceinstitute.com/resources/valuation/net-present-value-npv/`
Supports: the NPV definition and its limits, namely discount-rate sensitivity, the constant-rate
assumption, and manipulability of forward-looking inputs.
Quotable: "the value of all future cash flows (positive and negative) over the entire life of an investment
discounted to the present" / "The analysis requires extensive assumptions and proves highly vulnerable to
minor changes in drivers or inputs." / "The methodology assumes a constant discount rate throughout the
investment period, which rarely reflects real-world conditions where risk profiles evolve." / "Because NPV
relies heavily on forward-looking assumptions, analysts can easily manipulate inputs to produce desired
conclusions, raising concerns about objectivity in investment decisions."

**[14] Corporate Finance Institute. "Internal Rate of Return (IRR)".** practitioner. **fetched-and-verified.**
`https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/`
Supports: the IRR definition, the practitioner statement of the reinvestment-rate critique (used as the
contested counterpoint to [11]), the absence of absolute-dollar context, and mis-ranking across durations.
Quotable: "The Internal Rate of Return (IRR) is the discount rate that makes the net present value (NPV) of
a project zero." / "it assumes all positive cash flows of a project will be reinvested at the same rate as
the project" / "Knowing an IRR of 30% alone doesn't tell you if it's 30% of $10,000 or 30% of $1,000,000"

**[15] Corporate Finance Institute. "Payback Period".** practitioner. **fetched-and-verified.**
`https://corporatefinanceinstitute.com/resources/valuation/payback-period/`
Supports: the payback definition and its two headline limits, disregarding cash flows after the recovery
date and ignoring the time value of money.
Quotable: "how long it takes for a business to recoup an investment" / "cash flows continue beyond period
3, but they are not relevant in accordance with the decision rule" / "does not explicitly discount for the
risk and opportunity costs associated with the project"

**[16] Corporate Finance Institute. "Return on Investment (ROI)".** practitioner. **fetched-and-verified.**
`https://corporatefinanceinstitute.com/resources/accounting/return-on-investment-roi-formula/`
Supports: the ROI definition and its limits, ignoring the time horizon and varying with which costs are
included.
Quotable: "Return on investment (ROI) is a financial ratio used to calculate the benefit an investor will
receive in relation to their investment cost." / "disregards the factor of time" / "an investor needs to
consider the true ROI, which accounts for all possible costs incurred"

**[17] HM Treasury. "The Green Book: UK Government Guidance on Appraisal" (2026 edition).** primary. **fetched-and-verified.**
`https://assets.publishing.service.gov.uk/media/6645c709bd01f5ed32793cbc/Green_Book_2022__updated_links_.pdf`
Supports: the social time preference discount rate and its term structure, the definition of optimism bias,
the four summary metrics, the explicit warning against BCR-threshold decision rules, the spurious-accuracy
caution on real options, and switching values as an honest treatment of unmonetisable benefits.
Quotable: "The discount rate used in the Green Book is known as the social time preference rate (STPR). It
is set at 3.50% in real terms for years 1 to 30 of an appraisal. It is 3.00% for years 31 to 75, and then
2.50% for year 76 onwards." / "Optimism bias is the demonstrated systematic tendency for practitioners to
be over-optimistic about key assumptions in appraisal, such as social costs, social benefits or project
duration." / "Real options analysis (ROA) is a technique used to assess whether flexibility can be
incorporated during the design of a proposal... However, real options analysis typically requires
estimating probabilities of different scenarios. This can sometimes introduce spurious accuracy into the
analysis." / "Practitioners should not make judgements on value for money using BCR thresholds. In other
words, practitioners should not reject a proposal simply because it has a BCR less than a particular value
(e.g. below two). This practice incorrectly assumes that a BCR on its own can provide a comprehensive
assessment of value for money." / "A proposal with a BCR of less than one may still represent value for
money. It may have a low BCR but significant unmonetisable benefits." / "Switching values can also help
assess unmonetisable benefits. Practitioners might estimate the monetary value that an unmonetisable
benefit would need to be for the proposal's NPSV to be greater than zero. They should then explain whether
this value is likely or unlikely, based on past evidence." / "The benefit-cost ratio is the social return
of a proposal. It captures the monetisable social benefits that are generated for each pound sterling of
monetisable social costs."

**[18] VX Technology. "Intangible Benefits Are Not Nonexistent - How to Quantify What Seems Unquantifiable".** vendor. **fetched-and-verified.**
`https://www.vx-technology.com/en/insights/intangible-benefits-are-not-nonexistent`
Supports: practitioner guidance on quantifying intangible benefits honestly, using measurable proxies,
presenting ranges rather than false point precision, and being transparent about attribution limits.
Quotable: "An intangible benefit is not one that does not exist. It is one that cannot be measured directly
with conventional accounting and financial instruments." / "The difference between an honest proxy and a
convenient one is transparency about its limitations." / "An honest range is more persuasive than
fabricated precision." / "Precision decreases as the attribution chain lengthens."
Contested/time-bound: vendor tier. Used only for the honest-quantification pattern, which the Green Book's
switching-values guidance [17] independently corroborates. No claim rests on this source alone.

### Failure modes and critique

**[19] Bent Flyvbjerg. "From Nobel Prize to Project Management: Getting Risks Right"** primary.  (*Project **fetched-and-verified.**
Management Journal* 37(3), 5-15, 2006).
`https://arxiv.org/pdf/1302.3642`
Supports: the distinction between optimism bias and strategic misrepresentation, their complementary rather
than competing relationship, reference class forecasting and its three steps, and the finding that
inaccuracy distributions are non-normal and therefore reflect bias rather than error.
Quotable: "Psychological explanations account for inaccuracy in terms of optimism bias, that is, a
cognitive predisposition found with most people to judge future events in a more positive light than is
warranted by actual experience. Political explanations, on the other hand, explain inaccuracy in terms of
strategic misrepresentation. Here, when forecasting the outcomes of projects, forecasters and managers
deliberately and strategically overestimate benefits and underestimate costs in order to increase the
likelihood that it is their projects, and not the competition's, that gain approval and funding." /
"Optimism bias and strategic misrepresentation are both deception, but where the latter is intentional,
i.e., lying, the first is not, optimism bias is self-deception." / "rather than compete, the two types of
explanation complement each other: one is strong where the other is weak" / "(1) Identification of a
relevant reference class of past, similar projects. The class must be broad enough to be statistically
meaningful but narrow enough to be truly comparable with the specific project. (2) Establishing a
probability distribution for the selected reference class... (3) Comparing the specific project with the
reference class distribution, in order to establish the most likely outcome for the specific project." /
"if technical explanations were valid one would expect the distribution of inaccuracies to be normal or
near-normal with an average near zero. Actual distributions of inaccuracies are consistently and
significantly non-normal with averages that are significantly different from zero. Thus the problem is bias
and not inaccuracy as such."

**[20] Bent Flyvbjerg. "What You Should Know about Megaprojects and Why: An Overview"** primary.  (*Project **fetched-and-verified.**
Management Journal* 45(2), 6-19, 2014).
`https://arxiv.org/pdf/1409.0003`
Supports: the iron law of megaprojects and the nine-in-ten cost overrun figure with its traceable origin;
the direct claim that business cases and cost-benefit analyses generally cannot be trusted at observed
forecast-error magnitudes; the Channel Tunnel as a worked example of a falsifiable founding claim that was
falsified; the break-fix model explaining why business cases are revisited only under crisis; and that
success is too rare to sample statistically.
Quotable: "Performance data for megaprojects speak their own language. Nine out of ten such projects have
cost overruns. Overruns of up to 50 percent in real terms are common, over 50 percent not uncommon." /
"Combine the large cost overruns and benefit shortfalls with the fact that business cases, cost-benefit
analyses, and social and environmental impact assessments are typically at the core of planning and
decision-making for megaprojects and we see that such analyses can generally not be trusted... 'Garbage in,
garbage out,' as the saying goes." / "at the initial public offering, Eurotunnel, the private owner of the
tunnel, tempted investors by telling them that 10 percent 'would be a reasonable allowance for the possible
impact of unforeseen circumstances on construction costs.' In fact, costs went 80 percent over budget for
construction... Revenues have been half of those forecasted." / "If, as the evidence indicates,
approximately one out of ten megaprojects is on budget, one out of ten is on schedule, and one out of ten
is on benefits, then approximately one in a thousand projects is a success, defined as on target for all
three... This serves to illustrate what may be called the 'iron law of megaprojects': Over budget, over
time, over and over again." / "megaproject planners and managers -- and their organizations -- do not know
how to deliver successful megaprojects, or do not have the incentives to do so, and therefore such projects
tend to 'break' sooner or later, for instance when reality catches up with optimistic, or manipulated,
estimates of schedule, costs, or benefits."

**[21] HM Treasury. "Supplementary Green Book Guidance: Optimism Bias"** primary.  (derived from Mott **fetched-and-verified.**
MacDonald 2002, *Review of Large Public Procurement in the UK*).
`https://assets.publishing.service.gov.uk/media/5a74dae740f0b65f61322c72/Optimism_bias.pdf`
Supports: the institutionalised remedy of mandatory empirical uplifts to cost, benefit and duration
estimates by project type, and the governance rule that unmitigated high optimism bias is acceptable at
outline stage but not at full business case stage.
Quotable: "There is a demonstrated, systematic, tendency for project appraisers to be overly optimistic. To
redress this tendency appraisers should make explicit, empirically based adjustments to the estimates of a
project's costs, benefits, and duration." / "Generally, if the optimism bias at the appraisal stage is
appropriately low, then the project should be allowed to proceed. If the optimism bias remains high, then
approval should be withheld, or given on a qualified basis... high optimism bias may be acceptable for a
strategic outline business case but would not normally be acceptable at the full business case stage." /
"Clear and tangible evidence of the mitigation of contributory factors must be observed, and should be
independently verified, before reductions in optimism bias are made."

**[22] G. Locatelli. "Why are Megaprojects, Including Nuclear Power Plants, Delivered Overbudget and Late? Reasons and Remedies" (MIT-ANP-TR-172, CANES, MIT, 2018).** standards. **fetched-and-verified.**
`https://arxiv.org/pdf/1802.07312`
Supports: independent corroboration that the optimism-bias / strategic-misrepresentation split is the
dominant academic framing rather than an outlier, and Edward Merrow's rival practitioner explanation
centred on Front End Loading.
Quotable: "So according to Bent Flyvbjerg the specific characteristics of each megaproject are rather
irrelevant, and the overbudget/delay is explained by the stakeholder's attitude toward the project." /
"After 30 years of showing the data, badgering, cajoling, and whining to the industry about the criticality
of FEL, I believe there is now virtual consensus among project professionals within the community of
industries we serve that FEL is the single most important predictive indicator of project success."

**[23] Peter M. Tingling and Michael J. Brydon. "Is Decision-Based Evidence Making Necessarily Bad?"** practitioner.  (*MIT Sloan Management Review*, 26 June 2010). **fetched-and-verified.**
`https://sloanreview.mit.edu/article/is-decision-based-evidence-making-necessarily-bad/`
Supports: the named concept of decision-based evidence making, evidence assembled to support a decision
already taken. This is a general-management finding independent of the megaproject literature, and it is a
**distinct mechanism** from Flyvbjerg's strategic misrepresentation: the latter is about competing for
scarce funds against rival proposals, the former about retrofitting a case to a leader's private preference
even absent competition.
Quotable: "Evidence is shaped by subordinates to meet perceived expectations of company leaders."

**[24] Project Management Institute. "Pulse of the Profession 2016: The High Cost of Low Performance".** vendor. **fetched-and-verified.**
`https://www.pmi.org/-/media/pmi/documents/public/pdf/learning/thought-leadership/pulse/pulse-of-the-profession-2016.pdf`
Supports: **only** that this is a genuine PMI survey document, and the two statements quoted below.
Quotable: "Organizations that invest in project management waste 13 times less money because their
strategic initiatives are completed more successfully." / "compared to last year, fewer projects are being
completed within budget or meeting original goals and business intent."
Contested/time-bound: the widely circulated "17 percent report high benefits-realisation maturity" figure
attributed to this document **was not located in the pages read**. This source does not support that
figure. See the contested register.

**[25] thinkpieces.stavros.io. "How organizations consistently underinvest in the ability to actually evaluate whether a technical initiative worked after it shipped"** practitioner.  (undated blog). **fetched-and-verified.**
`https://thinkpieces.stavros.io/posts/how-organizations-consistently-underinvest-in-the-ability-to/`
Supports: **only** that a cluster of widely repeated benefits-realisation statistics circulates together
with named citations attached. Read specifically to test the traceability of those citations, not to source
the figures themselves. It attributes each figure to a named primary source, which is better practice than
most repetitions, but this research could not fetch those primaries. **No figure from this source may be
cited as fact.**

### The product-team context

**[26] Marty Cagan (SVPG). "Product vs. Project Teams".** practitioner. **fetched-and-verified.**
`https://www.svpg.com/product-vs-project-teams/`
Supports: that the up-front business case is named as a defining feature of project teams and rejected as
such, and the waste claim attached to the cycle.
Quotable: "provide a business case for the project, get funding for the project, staff the project, ship
the project, hope nobody checks actual results against the business case, rinse and repeat" / "epic amounts
of waste"

**[27] Marty Cagan (SVPG). "What Product Management Is Not".** practitioner. **fetched-and-verified.**
`https://www.svpg.com/what-product-management-is-not/`
Supports: that Cagan explicitly demotes the artifact in a section titled *Product Management is not
defining the business case*, conceding management uses it for investment decisions while denying it is
product management's job.
Quotable: "this doesn't really do anything to contribute to actually creating the product"

**[28] Mind the Product summary of Melissa Perri, *Escaping the Build Trap*.** practitioner. **fetched-and-verified.**
`https://www.mindtheproduct.com/escaping-build-trap-melissa-perri/`
Supports: **an absence, and only within this secondary treatment.** This summary of the book does not
engage business cases or funding-justification documents at all; its escape route runs through process,
strategy, culture and the outcomes-versus-outputs distinction.
Quotable: "we need to create a customer-centric organisation that rewards learning and reaching outcomes,
rather than focusing on outputs"
Contested/time-bound: the book itself was not read. This supports a claim about the summary's coverage, not
about Perri's full text.

**[29] John Cutler (The Beautiful Mess). "TBM 322: Work Shape Mix".** practitioner. **url-confirmed-not-read.**
`https://cutlefish.substack.com/p/tbm-322-work-shape-mix`
Supports: nothing on its own. Search-snippet level only: it distinguishes project-based funding, where ROI
is assessed per project, from product-team funding. **No claim in this bundle may rest on this source.**

**[30] Teresa Torres, Product Talk. Site-wide search across roadmaps, opportunity solution trees and prioritisation material.** practitioner. **url-confirmed-not-read.**
`https://www.producttalk.org/`
Supports: **an absence.** Repeated targeted search across Torres's core published material surfaced no use
of the term "business case" anywhere in her continuous-discovery vocabulary. No page body was read in full,
so this supports the observation of silence and nothing more.

### Boundaries and lifecycle

**[31] PRINCE2 Wiki. "Business case" (management products, baselines).** practitioner. **fetched-and-verified.**
`https://prince2.wiki/management-products/baselines/business-case/`
Supports: ownership split (executive accountable, project manager assists and maintains), the creation and
refinement timeline, the review cadence, and that it is a maintained document receiving a final update at
project closure.
Quotable: "The project executive is accountable for creating the business case, typically assisted by the
project manager." / "An 'outline business case' document is drafted by the project manager during the
'starting up a project' process" / "Initially created at the project's inception, it is actively maintained
throughout by the project manager" / "The business case receives its final update during the closing a
project process" / "The project board should check the business case: At the end of starting up to
authorize project initiation; At the end of initiating to authorize the project; At the end of each stage
to authorize the next stage" / "The business layer reviews the business case in a post-project benefits
review to check if the intended benefits were realized." / "The business case gathers information to allow
management to judge if a project is desirable, viable, and achievable."

**[32] PRINCE2 Wiki. "Project brief" (management products, baselines).** practitioner. **fetched-and-verified.**
`https://prince2.wiki/management-products/baselines/project-brief/`
Supports: the precise boundary test against the business case. The brief is assembled once in Starting Up,
*contains* an outline business case as one component, and retires once the PID exists; the business case is
refined into a standalone product and does not retire.
Quotable: "a short, high-level overview of the project, created during the starting up a project process by
the project manager" / "ensures that everyone - especially the project board - has a shared understanding
of the project's background, objectives, scope, constraints, risks, stakeholders, and outline business
case" / "The project brief is created during the starting up a project process." / "Once the project
initiation documentation (PID) is created, the project brief is no longer used in project management
activities."

**[33] PRINCE2 Wiki. "Closing a project" (processes).** practitioner. **fetched-and-verified.**
`https://prince2.wiki/processes/closing-a-project/`
Supports: what happens to the business case at closure, namely comparison against the original baseline and
a handoff to a scheduled post-project benefits review. **Also supports the negative finding** that no
specific closure event or accountable role for the business case itself is named.
Quotable: "Review project performance against the original baselines such as the original project plan and
business case." / "update the plan to plan the benefits reviews that should take place after the project is
closed" / "The business level will follow up on this benefits review"

**[34] FHWA Office of Operations. "Systems Engineering for ITS", section 3.4.5, Trade Studies.** primary. **fetched-and-verified.**
`https://ops.fhwa.dot.gov/seits/sections/section3/3_4_5.html`
Supports: the trade study's definition and scope, and the distinguishing test against a business case. A
trade study is a bounded technical comparison against weighted criteria; its output is consumed as an input
to the business case's options section rather than substituting for it.
Quotable: "Trade studies compare the relative merits of alternative approaches to ensure that the most
cost-effective system is developed."

**[35] ProductPlan. "Product Requirements Document" glossary entry.** vendor. **fetched-and-verified.**
`https://www.productplan.com/glossary/product-requirements-document/`
Supports: the distinguishing test between a business case and a PRD. The PRD specifies what to build once
funding is settled and is explicitly not about market opportunity or revenue.
Quotable: "an artifact used in the product development process to communicate what capabilities must be
included in a product release to the development and testing teams" / "does not touch on market opportunity
or revenue but is instead firmly rooted in use cases and desired functionality"

### Sought and not retrieved

These are recorded so that no draft can quietly assume them. **Nothing in this bundle may rest on any entry
in this section.**

**[36] PMI. *A Guide to the Project Management Body of Knowledge* (PMBOK Guide) 7th edition, 2021.** standards. **not-retrieved.**
`https://www.pmi.org/`
Supports: nothing in this bundle. Sought for: PMBOK 7's own text classifying Business Case as a Strategy artifact alongside Project Charter
and Roadmap, and its stated components. **Paywalled to PMI members; no free PMI.org page states this
directly.** Third-party summaries agree on the classification but were not read in full, and one candidate
verification site returned HTTP 503 while another had been updated to PMBOK 8 content.
**This bundle's own build spec names PMBOK 7 as a key source. It could not be read, and this bundle
therefore states nothing about what PMBOK 7 says.**

**[37] ISO 21502:2020, *Project, programme and portfolio management - Guidance on project management*.** standards. **not-retrieved.**
`https://www.iso.org/standard/74947.html`
Supports: nothing in this bundle. Sought for: ISO 21502's clause-level requirements for business case content and its role in the governance framework. **Not read: the ISO catalogue page returned HTTP 403 and the standard is a paid document.**

**[38] ISO 21500:2021, *Project, programme and portfolio management - Context and concepts*.** standards. **not-retrieved.**
`https://www.iso.org/standard/75704.html`
Supports: nothing in this bundle. Sought for: ISO 21500's treatment of the business case as a foundational concept. **Not read: paywalled, and a reseller sample PDF contained no readable business-case text.**

**[39] McKinsey and University of Oxford. "Delivering large-scale IT projects on time, on budget, and on value".** practitioner. **not-retrieved.**
`https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value`
Supports: nothing in this bundle. Sought for: the widely repeated "5,400+ large IT projects deliver 56 percent less value than predicted"
figure. **Unverified. Must not be cited.**

**[40] KPMG. *Global IT Project Management Survey* (2005).** vendor. **not-retrieved.**
`https://assets.kpmg.com/content/dam/kpmg/pdf/2009/12/Global-IT-Project-Management-Survey-0508.pdf`
Supports: nothing in this bundle. Sought for: the "only 13 percent of organisations track benefits until realised" figure. **Unverified. Must
not be cited.**

**[41] The Standish Group. CHAOS Report (various editions).** vendor. **not-retrieved.**
No URL: the CHAOS reports have no stable public address, being sold by the publisher rather than published.
Supports: nothing in this bundle. Sought for: IT project failure rates. Search surfaced substantial published academic criticism of the
report's undisclosed methodology, narrow sampling and one-sided success definition (Glass; Jorgensen and
Molokken-Ostvold), none of which was read in full either. **This is the archetype of the famous-but-
unverifiable statistic. It must not appear in this bundle in any form.**

**[42] Investopedia. NPV, IRR, payback and ROI definitions.** practitioner. **not-retrieved.**
`https://www.investopedia.com/`
Supports: nothing in this bundle. Sought for: plain-language definitions of NPV, IRR, payback and ROI. **Not read: every fetch attempt failed.** Corporate Finance Institute [13][14][15][16] was
used as the practitioner-tier substitute. Noted because Magni and Martin [11] open by quoting Investopedia
making exactly the claim they argue is false, so the source is part of the contested story even though its
text could not be read here.

**[43] Martin Wachs. Writing on forecasting ethics.** primary. **not-retrieved.**
No URL: none was ever captured, because the claim surfaced only inside a search-result snippet and no source page was opened.
Supports: nothing in this bundle. Sought for: a primary statement of Wachs's position on forecasting ethics. A search snippet attributed to him a phrase about deliberate misrepresentation
amounting to "a collective failure of professional ethics." **The original was not fetched and this quote
must not be treated as verified or reproduced.**

---

## Contested register

Recorded rather than resolved. Where sources genuinely disagree, the bundle presents the disagreement.

**1. Does IRR assume reinvestment at the IRR rate?** Magni and Martin [11], academic and primary, say the
claim is a documented fallacy with no basis in the mathematics. Corporate Finance Institute [14],
practitioner tier and the source a business-case author is far more likely to consult, states it as IRR's
"critical flaw" and recommends MIRR as the fix. This is a real split running through the tier of sources
readers will actually meet. **Present both.** The practitioner warning against comparing IRRs across
projects of different scale is independently sound; the "implicit assumption" framing specifically is what
finance academics dispute.

**2. Is real options analysis an advance or a source of spurious accuracy?** Damodaran [12] argues it fills
a genuine gap in DCF by pricing managerial flexibility. The Green Book [17] warns it "can sometimes
introduce spurious accuracy." Not strictly incompatible, but the emphasis differs sharply, and a reader
deciding whether to use the technique needs both.

**3. Is options analysis formally mandatory in the Green Book model, or a strong default?** Every
implementation read shows it consistently present [4][5], but never as a standalone heading, and the
mandatory-language question could not be settled because the guidance PDF's extraction degraded [10].

**4. Which section order is right?** The UK government family subordinates options inside the Economic Case
[4][5]; the practitioner family gives it its own heading mid-document [8][9]. **Neither is more
authoritative.** They reflect different governance traditions and no source reconciling them was found.

**5. Is a lean business case a shorter document or a different one?** The SAFe format [7] supports the
structurally-different reading, substituting hypothesis and leading indicators for a financial case. No
source explicitly arguing the alternate framing was found, so the tension is inferred from the section list
rather than from a debate in the literature.

**6. Does PMBOK 7 treat the business case as a one-time pre-charter input or a maintained artifact?**
Secondary summaries lean toward pre-charter input, which would put PMBOK 7 closer to the one-time-gate
framing than PRINCE2, the Green Book or APM. **Unverifiable here** [36].

**7. Does Cagan reject the business case or merely demote it?** "Product vs. Project Teams" [26] reads as
rejection of the cycle; "What Product Management Is Not" [27] concedes the artifact has a legitimate
investment-decision audience while fencing it off from product management. Both are Cagan; a reader could
take either as the SVPG position.

**8. Does the silence of Perri and Torres mean the artifact is unnecessary, or that it never came up?**
This research cannot distinguish "considered and rejected" from "never addressed" from the sources
accessible [28][30], and says so rather than choosing.

**9. Business case versus feasibility study sequencing.** Unread practitioner sources assert feasibility
first; the one source fetched cleanly on the pairing treats them as a bundled advisory offering rather than
a sequence. Unresolved.

**10. Business case versus investment proposal.** Whether these are distinct types or near-synonyms in
public-sector capital frameworks is unresolved; both candidate primaries returned HTTP 403.

**11. What formally closes a business case?** PRINCE2's closing process [33] describes baseline comparison
and a handoff to a benefits review, but names **no closure event or accountable role** for the business case
itself. This is a genuine gap in the sources, and it has a template implication: the artifact probably needs
an explicit "how this gets checked after go-live" section precisely because the standard process supplies no
hard stop.

---

## Sought and not found

Distinct from `not-retrieved` above: these were searched for and appear not to exist in the form sought.

- **A named academic treatment of unfalsifiable benefit claims as their own failure category.** The
  literature covers measurement difficulty for soft benefits, and it covers specific claims that were
  falsified (the Channel Tunnel [20]), but no source was found treating vague, untestable benefit phrasing
  as a documented category in its own right.
- **A product-management-authored source naming where a business case is still genuinely required.**
  Searches on regulated industries, large capex and procurement returned generic finance and procurement
  content with no connection to product practice. The one adjacent signal is a secondary description of
  Cagan's *Empowered* noting it assumes a late-stage SaaS context, which implies the carve-out by omission
  rather than stating it. **That is an inference, not a sourced claim.**
- **A product-management-native alternative document** with a name equivalent to "business case." None was
  found. The literature's posture is silence or hostility, not a replacement artifact.
- **A single named one-page government business case template** readable in full. Canada's PSPC publishes a
  named "Lite Version" but the page failed on a certificate error; the "one-page business case" otherwise
  appears only as a generic genre description, never as one publisher's readable document.
- **Section lists for several government templates**, all blocked: Australia's DTA Second Pass template
  (fetch timeouts), Canada's Treasury Board guide (HTTP 403), OMB Circular A-11 Exhibit 300 (extraction too
  degraded to quote), and three university PMO templates whose real content sits in DOCX or shared-drive
  files the web pages only link to.
- **An earlier or more authoritative coinage** of the business-case-written-backward idea than Tingling and
  Brydon's decision-based evidence making [23]. It is a commonly asserted pattern with little rigorous study
  of its prevalence.
