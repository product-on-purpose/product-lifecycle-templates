# Business Case: the companion

The reference behind the template. Read this when you want to know *why* a section exists, what the
research actually says, and where the standards and the product-management literature disagree with each
other.

## 1. Orientation

A business case "provides justification for undertaking a project, programme or portfolio. It evaluates
the benefit, cost and risk of alternative options and provides a rationale for the preferred solution"
[[3]](#ref-3). The job in one sentence: decide whether an investment is worth making, and say plainly what
it is being compared against. A case that names no alternative is a proposal wearing a bigger name; see
Options Considered below.

At a glance:

- Every standard this research could read in full treats it as a **living document**, revisited as the
  work proceeds, not a one-time gate [[1]](#ref-1)[[2]](#ref-2)[[3]](#ref-3). Most people use it as a
  one-time gate anyway. That gap between the standard and the habit is this document's central teaching
  point.
- The traditions agree on the principle and disagree on the mechanism. PRINCE2 keeps one document revised
  in place [[2]](#ref-2). The UK government model stages three separate, formally gated documents
  [[1]](#ref-1). A template has to pick one operating model or support both explicitly; this bundle ships
  the staged Five Case Model as its spine and teaches the living-document discipline as practice, not as a
  second format.
- Product-management literature is hostile or silent. No source this research found makes a positive case
  for the artifact from a product-management perspective [[26]](#ref-26)[[27]](#ref-27)[[28]](#ref-28)
  [[30]](#ref-30). Say so plainly rather than implying an endorsement that was not found.
- The most repeated "fact" about IRR, that it assumes reinvestment at the IRR rate, is a documented
  fallacy according to the finance sources that could be read [[11]](#ref-11), while the practitioner
  source a business-case author is most likely to open states the opposite as settled
  [[14]](#ref-14). Present it as contested, not resolved.
- The famous benefits-realisation statistics that circulate in practitioner writing could not be
  independently verified here and must not appear in this bundle as fact
  [[24]](#ref-24)[[25]](#ref-25). Their absence is itself worth teaching.

## 2. Origins and evolution

The clearest surviving lineage runs through UK public-sector spending guidance. HM Treasury and Welsh
Government's current guidance frames the whole exercise as more than paperwork: "The process of developing
a business case matters as much as the final document. It is not merely a writing exercise or something to
complete in order to obtain approval" [[1]](#ref-1). That guidance organises the case around five named
dimensions, the strategic, economic, commercial, financial and management cases, staged across three formal
gates: a Strategic Outline Case at scoping, an Outline Business Case at planning, and a Full Business Case
at procurement [[1]](#ref-1). Scottish Government's own service manual implements the same model and adds a
line worth keeping: "writing a business case is not a linear process" [[6]](#ref-6), even though the stage
gates look linear on paper.

PRINCE2 evolved a different mechanism for the same underlying commitment. Rather than three staged
documents, it keeps one artifact "desirable, viable, and achievable as a means to support decision-making
in its continued investment" [[2]](#ref-2), checked through a four-step Develop, Check, Maintain, Confirm
technique at every stage boundary, under a named principle: continued business justification.

This bundle's own format research considered a genuine fourth candidate and did not ship it. The SAFe Lean
Business Case substitutes an Epic Hypothesis Statement and leading indicators for a financial case, and
defers cost modelling until an MVP validates the hypothesis: "it acknowledges uncertainty and builds in
mechanisms to learn fast" [[7]](#ref-7). It is a structurally different document, not a shorter one, which
is exactly the distinction this library's format rule is built to catch. It is deferred rather than
rejected only because this research read a practitioner mirror of the format, not Scaled Agile's own
publication; see Variants and sizing.

**One gap is worth naming here rather than discovering later.** PMBOK 7 is named as a key source for this
document type, and this research could not retrieve it: the guide is available only to PMI members and no
free page states its treatment directly [[36]](#ref-36). Nothing in this bundle states what PMBOK 7 argues.
ISO 21502 and ISO 21500 were sought for the same reason and were equally unreachable behind their
publisher's paywall [[37]](#ref-37)[[38]](#ref-38). Their absence from this companion is a retrieval gap,
not a judgment that they disagree with anything stated here.

## 3. Anatomy (section by section)

### Problem and Opportunity (lean and full)

The section the rest of the case has to answer to. HM Treasury's model treats it as load-bearing rather
than introductory: "The strategic case is fundamental to the business case process. It drives the
identification and appraisal of options in the economic case" [[1]](#ref-1). A practitioner ordering makes
the same point in plainer language, describing the equivalent section as one that "provides general
information on the issues surrounding the business problem" [[9]](#ref-9). If this section names a solution
instead of a problem, the Options Considered section below has nothing genuine to compare, because the
answer was already assumed.

### Options Considered (lean and full)

The load-bearing section: a business case naming no alternative is a proposal rather than a case. The two
traditions place it differently in the document but neither treats it as optional in substance. PRINCE2
requires
business options including a mandatory do-nothing baseline [[2]](#ref-2). The UK government model folds
comparison inside the Economic Case, moving from a longlist to a shortlist and a preferred option across
the SOC and OBC stages [[4]](#ref-4)[[5]](#ref-5). The practitioner and PMI-adjacent family instead gives it
its own named heading mid-document, "Alternative Analysis" or "Option analysis"
[[8]](#ref-8)[[9]](#ref-9). Neither ordering is more authoritative; both traditions treat a named
alternative, including doing nothing, as non-negotiable. A business case that skips this section is a
proposal, and the honest label matters more than the section header above it.

### Costs (full only)

The place where optimism enters the document first, and where it is hardest to see. HM Treasury's
supplementary guidance states the problem directly: "There is a demonstrated, systematic, tendency for
project appraisers to be overly optimistic. To redress this tendency appraisers should make explicit,
empirically based adjustments to the estimates of a project's costs, benefits, and duration"
[[21]](#ref-21). The same guidance ties the remedy to governance: "high optimism bias may be acceptable for
a strategic outline business case but would not normally be acceptable at the full business case stage"
[[21]](#ref-21), meaning a rough cost estimate is a legitimate starting point, but the tolerance for
unexamined optimism should shrink as the decision gets closer. In the megaproject literature specifically,
Flyvbjerg's tracked database found "nine out of ten such projects have cost overruns. Overruns of up to 50
percent in real terms are common, over 50 percent not uncommon" [[20]](#ref-20); treat that figure as
evidence about megaprojects, not as a universal rate, since this research did not find an equivalent study
of ordinary product investments.

### Benefits (full only)

The section most tempted by false precision, and the one where the honest move is a range rather than a
point estimate. "An intangible benefit is not one that does not exist. It is one that cannot be measured
directly with conventional accounting and financial instruments," and "an honest range is more persuasive
than fabricated precision" [[18]](#ref-18). The Green Book's own guidance corroborates the pattern from a
different angle, recommending switching values: estimate what a currently unmonetisable benefit would need
to be worth for the case to clear zero, then state plainly whether that value is plausible
[[17]](#ref-17). **Resist the well-known benefits-realisation statistics.** A cluster of frequently repeated
figures circulates together in practitioner writing, each attached to a named primary source, but this
research could not independently verify any of them, and no figure from that cluster may be cited as fact
in this bundle [[24]](#ref-24)[[25]](#ref-25). This research also did not find a named academic treatment
of vague, untestable benefit language as its own documented failure category, though the intangible-benefit
and switching-value guidance above points at the same underlying problem from the honest-quantification
side [[17]](#ref-17)[[18]](#ref-18).

### Risks (full only)

Where the case has to reckon with why forecasts go wrong, and the research says there are two different
mechanisms, not one. Flyvbjerg's distinction: "Optimism bias and strategic misrepresentation are both
deception, but where the latter is intentional, i.e., lying, the first is not, optimism bias is
self-deception," and the two are complementary rather than competing, with strategic misrepresentation
dominating on high-stakes visible projects and optimism bias on smaller ones [[19]](#ref-19). His proposed
fix, reference class forecasting, comparing the specific project against a distribution of similar past
projects rather than estimating it from scratch, is designed to bypass both mechanisms at once without
first diagnosing which one is operating [[19]](#ref-19). HM Treasury operationalises essentially that idea
as mandatory empirical uplifts by project type [[21]](#ref-21). PRINCE2's continued-business-justification
principle supplies the ongoing check: "If, at any point, the business case becomes invalid, the project
should be halted" [[2]](#ref-2). A related but distinct risk sits outside the forecasting literature
entirely: decision-based evidence making, where "evidence is shaped by subordinates to meet perceived
expectations of company leaders" [[23]](#ref-23). Unlike strategic misrepresentation, which competes for
scarce funding against rival proposals, this pattern can appear even with no competing proposal in sight,
simply to support a decision a leader has already made.

### Financials (full only)

The most technically dense section, and the one where practitioner convention and academic finance dispute
each other openly. Net present value discounts every future cash flow to the present
[[13]](#ref-13); internal rate of return is "the discount rate that makes the net present value (NPV) of a
project zero" [[14]](#ref-14); payback period measures "how long it takes for a business to recoup an
investment" [[15]](#ref-15); return on investment is "a financial ratio used to calculate the benefit an
investor will receive in relation to their investment cost" [[16]](#ref-16). Each has documented limits: NPV
is "highly vulnerable to minor changes in drivers or inputs" [[13]](#ref-13); payback "does not explicitly
discount for the risk and opportunity costs associated with the project" [[15]](#ref-15); ROI "disregards
the factor of time" [[16]](#ref-16); and IRR alone gives no absolute-dollar context, since "knowing an IRR
of 30% alone doesn't tell you if it's 30% of $10,000 or 30% of $1,000,000" [[14]](#ref-14). **The
reinvestment claim about IRR is genuinely contested and this bundle presents both sides rather than picking
one.** See the Debates section below. For a discount rate, the Green Book publishes a specific structure:
"3.50% in real terms for years 1 to 30 of an appraisal. It is 3.00% for years 31 to 75, and then 2.50% for
year 76 onwards" [[17]](#ref-17), and it warns explicitly against a common decision shortcut: "Practitioners
should not make judgements on value for money using BCR thresholds... A proposal with a BCR of less than one
may still represent value for money" [[17]](#ref-17). Real options analysis, pricing the value of managerial
flexibility such as an option to delay, expand, or abandon, is the most advanced technique in this section
and the most disputed: Damodaran argues it "gives prominence to the upside potential for risk"
[[12]](#ref-12), while the Green Book warns it "can sometimes introduce spurious accuracy into the analysis"
[[17]](#ref-17).

### Recommendation (lean and full)

Where the case commits. APM's definition names the job precisely: the case "provides a rationale for the
preferred solution" [[3]](#ref-3), and APM records who is accountable for it: "The sponsor owns the business
case" [[3]](#ref-3). This section should read as the conclusion the Options Considered section earns, not as
the starting point everything above it was built to justify. Written the other way round, in the direction
already named above as decision-based evidence making [[23]](#ref-23), it is indistinguishable from a
proposal dressed up after the fact.

## 4. Variants and sizing

**Lean** carries Problem and Opportunity, Options Considered, and Recommendation: enough to scope a decision
and name what it is being compared against, without a financial model behind it. **Full** inserts Costs,
Benefits, Risks and Financials between Options Considered and Recommendation, the four sections a reader
needs to actually fund the thing rather than merely agree the idea is worth exploring. The natural signal to
scale up mirrors the UK government staging: a Strategic Outline Case can be thin because it is scoping, but
an Outline or Full Business Case, where real money and procurement commitments are at stake, needs the
weight the full variant carries [[1]](#ref-1).

**The SAFe Lean Business Case is not a third size of this template, and it is worth naming why.** It
substitutes a hypothesis and leading indicators for a financial model and "defers detailed planning until
learning validates the hypothesis," arguing against "spending months building a comprehensive financial
model based on assumptions" [[7]](#ref-7). That is a genuinely different document, not a shorter version of
this one, and a reader who is choosing between validating a hypothesis cheaply and building a funding case
for a known investment should know that a named alternative tradition exists. It does not ship here because
this research read a practitioner mirror of the format rather than Scaled Agile's own publication.

## 5. Methodology lineage

Three standards bodies converge on the living-document principle from independent starting points. HM
Treasury names it outright [[1]](#ref-1); PRINCE2 makes it a formal principle with an enforcement
consequence [[2]](#ref-2); APM states the case "is reviewed and revised at decision gates as more mature
estimates and information become available" [[3]](#ref-3). Within that shared principle, the two
operating traditions diverge on mechanism: PRINCE2's one evolving document against the UK government
model's three staged, separately gated documents. Neither tradition is a rewording of the other.

A separate, less formal practitioner family exists alongside both: ten-section and eight-section templates
that cover the same ground in a different order, without a staged-approval mechanism attached
[[8]](#ref-8)[[9]](#ref-9). One of them is explicit that its own ordering is a recommendation, not a
requirement: "you should generally use whatever format or template your company uses" [[8]](#ref-8).

Product-management literature sits outside all of the above, and mostly against it. Cagan names the funding
cycle almost verbatim in order to reject it, calling it "epic amounts of waste"
[[26]](#ref-26), and elsewhere concedes the artifact serves investment decisions while denying it
contributes to product work: "this doesn't really do anything to contribute to actually creating the
product" [[27]](#ref-27). A secondary treatment of Perri's *Escaping the Build Trap* does not engage
business cases or funding-justification documents at all [[28]](#ref-28), and a targeted search of Teresa
Torres's continuous-discovery material surfaced no use of the term anywhere in her published vocabulary
[[30]](#ref-30). This research found no product-management-authored source that makes a positive case for
the artifact, and no product-management-native alternative document with an equivalent name. State that as
the finding it is rather than treating product-management silence as tacit agreement.

PMBOK 7 and ISO 21502/21500 would plausibly belong in this section, and this bundle says nothing about their
specific treatment because none of the three could be retrieved past a paywall
[[36]](#ref-36)[[37]](#ref-37)[[38]](#ref-38).

## 6. Debates and contested boundaries

**Does IRR assume reinvestment at the IRR rate?** Academic finance says no: "There are no reinvestment rate
assumptions built into, or implicit to, the computation and use of either the IRR or NPV"
[[11]](#ref-11). The practitioner source a business-case author is far more likely to consult states the
opposite as settled fact: "it assumes all positive cash flows of a project will be reinvested at the same
rate as the project" [[14]](#ref-14). This is a live split running through the exact
tier of sources a reader will actually meet, not a settled question with one side simply uninformed.

**Is real options analysis an advance on discounted cash flow, or a source of false confidence?**
Damodaran argues it prices a genuine gap, managerial flexibility, that plain discounting cannot capture
[[12]](#ref-12); the Green Book warns the same technique "can sometimes introduce spurious accuracy"
[[17]](#ref-17). Not strictly incompatible positions, but the emphasis is sharply different, and a reader
deciding whether to reach for the technique needs both.

**Which section order is correct, options folded into a case or given its own heading?** Every UK
government implementation reviewed keeps options inside the Economic Case
[[4]](#ref-4)[[5]](#ref-5); the practitioner family gives it a standalone section mid-document
[[8]](#ref-8)[[9]](#ref-9). Neither is more authoritative. They reflect different governance traditions, and
no source reconciling them was found.

**Is the SAFe Lean Business Case a shorter document, or a different one?** The format's own structure
supports the different-document reading, substituting a hypothesis and leading indicators for a financial
case [[7]](#ref-7). No source arguing the alternate framing, that it is simply a condensed version of the
same document, was found; the tension is inferred from the section list itself rather than from a live
debate in the literature.

**Does Cagan reject the business case outright, or merely fence it off from product management?** "Product
vs. Project Teams" reads as rejection of the funding cycle [[26]](#ref-26); "What Product Management Is Not"
concedes the artifact a legitimate investment-decision audience while denying it is product management's
job [[27]](#ref-27). Both are Cagan; a reader could take either as the position.

**Does the silence of Perri and Torres mean the artifact is unnecessary, or simply that it never came up?**
This research cannot distinguish "considered and rejected" from "never addressed" from the sources it could
access [[28]](#ref-28)[[30]](#ref-30), and says so rather than picking one.

**Is Flyvbjerg's optimism-bias and strategic-misrepresentation framing the dominant academic account, or
one voice among several?** An independent MIT review corroborates it as the dominant framing rather than an
outlier, while also naming a rival practitioner explanation: Edward Merrow's Front End Loading, on the
argument that "FEL is the single most important predictive indicator of project success"
[[22]](#ref-22). The two are not presented as mutually exclusive in the source that names both.

**What formally closes a business case?** PRINCE2's closing process describes comparing performance against
the original baseline and handing off to a scheduled benefits review [[33]](#ref-33). Elsewhere the same
guidance does name a reviewer and an occasion: the business layer, at a post-project benefits review, with
a final update to the document during closing [[31]](#ref-31). What neither supplies is a person and a
date. The check is delegated to an organisational layer on a generic schedule, which is why the artifact
still needs its own explicit answer to "who checks this after go-live, and when."

## 7. Anti-patterns and failure modes

**Treating it as a one-time gate.** Every standard this research could read in full says the opposite
[[1]](#ref-1)[[2]](#ref-2)[[3]](#ref-3). This is the gap the bundle was built around, though how often it
occurs is not something any source this research could reach has measured.

**No named alternative, including no do-nothing option.** PRINCE2 makes the baseline mandatory
[[2]](#ref-2), and every structure this research read, whichever tradition, treats comparison against a
named alternative as non-negotiable in substance
[[4]](#ref-4)[[5]](#ref-5)[[8]](#ref-8)[[9]](#ref-9). Without it, the document is a proposal.

**Unexamined optimism in cost, benefit, and duration estimates.** The named remedy is an explicit,
empirically based adjustment, not vigilance alone [[21]](#ref-21), and the tolerance for skipping that
adjustment should shrink as the decision gets closer to a real commitment [[21]](#ref-21).

**Strategic misrepresentation dressed as optimism.** Flyvbjerg's point is that these are two different
mechanisms, self-deception versus deliberate lying, and naming the wrong one misses the actual failure
[[19]](#ref-19).

**Decision-based evidence making.** Assembling a case to support a decision a leader has already made,
independent of any competition for funding [[23]](#ref-23). This is easy to mistake for strategic
misrepresentation, and the fix is different because the underlying incentive is different.

**Citing the famous benefits-realisation statistics.** They circulate with named citations attached and
could not be independently verified here; treating them as settled fact when they are not is a documented
pattern this research explicitly quarantines [[24]](#ref-24)[[25]](#ref-25).

**Using a BCR threshold as a decision rule.** The Green Book warns against exactly this, and against
rejecting a proposal for a BCR below some round number when unmonetised benefits may still justify it
[[17]](#ref-17).

**Comparing IRRs across projects of very different scale without dollar context.** A high percentage on a
small base is not automatically the better bet [[14]](#ref-14).

**No accountable check after go-live.** The standard delegates the check to an organisational layer on a
generic schedule, a business-layer benefits review after the project closes [[31]](#ref-31), and its
closing process names nothing more specific for the document itself [[33]](#ref-33). Leaving it there is
the anti-pattern, because Flyvbjerg's break-fix model describes what fills the space: business cases get
revisited only once reality has already caught up with the estimate, not on any earlier schedule
[[20]](#ref-20).

## 8. Relationships to other artifacts

**What this document is not, and who takes over once the investment decision is made.** It is not a
project brief: PRINCE2's project brief is "a short, high-level overview of the project, created during the
starting up a project process," and it absorbs an outline business case as one component before retiring
once the project initiation documentation exists; the business case itself is not retired the same way, it
continues to be refined [[32]](#ref-32). It is not a trade study: trade studies are bounded technical
comparisons, and "compare the relative merits of alternative approaches to ensure that the most
cost-effective system is developed" [[34]](#ref-34), and their output feeds the Options Considered section as
an input rather than substituting for the case as a whole. It is not a PRD: a PRD is "an artifact used in
the product development process to communicate what capabilities must be included in a product release,"
and explicitly "does not touch on market opportunity or revenue" [[35]](#ref-35), which is precisely the
ground this document covers and the PRD deliberately does not. Once the investment decision this document
argues for is made, the PRD and its delivery-docs family take over specifying what actually gets built.

**Ownership and lifecycle.** "The project executive is accountable for creating the business case,
typically assisted by the project manager," and "the business layer reviews the business case in a
post-project benefits review to check if the intended benefits were realized" [[31]](#ref-31). It is
"actively maintained throughout" the work it justifies and "receives its final update during the closing a
project process" [[31]](#ref-31).

## 9. Adaptations

**Regulated and public-sector settings** should expect the staged model in full: a Strategic Outline Case,
Outline Business Case, and Full Business Case, each with its own gate review, and the Green Book's discount
rate and optimism-bias uplifts applied without shortcuts [[1]](#ref-1)[[17]](#ref-17)[[21]](#ref-21).

**Product-led organisations that lean agile** may find the lean size of this template still heavier than
what they actually want. The named alternative worth knowing is the SAFe Lean Business Case, which trades
the financial case for a testable hypothesis and leading indicators [[7]](#ref-7); it is not shipped here,
but a team that would rather validate an assumption cheaply than build a funding case should recognise that
tradition by name rather than reinvent a thinner version of this one.

**Small teams and solo founders** will likely use the lean size only, with an informally accountable
sponsor rather than a formal decision gate; the substance, naming the problem, naming the alternative,
naming the recommendation, does not shrink even when the ceremony does.

**Organisations governed by PRINCE2** should treat the document as continuously maintained rather than
filed once approved, checked at the Develop, Check, Maintain, Confirm cadence PRINCE2 names, and halted
outright if it stops being valid [[2]](#ref-2).

## 10. Worked example

See `business-case_example.md`. Per this library's discovery-docs family contract, the example is Acme
Analytics's own business case, and it justifies the investment that the FY26 product strategy later spends,
continuing the shared scenario backward from a decision the library's other bundles already assume was
made.

## References

<a id="ref-1"></a>[1] HM Treasury and Welsh Government. "[Guidance on Developing Business Cases for Projects and Programmes](https://assets.publishing.service.gov.uk/media/6a4390675b6406df58c14006/Guidance_on_Developing_Business_Cases.pdf)" (2026 edition, ISBN 978-1-918417-58-6, PU3650). [primary]

<a id="ref-2"></a>[2] prince2.wiki. "[Business Case](https://prince2.wiki/theme/business-case/)," a practitioner mirror of the AXELOS PRINCE2 manual's Business Case theme. [practitioner] Used for PRINCE2's structure and mechanism, which it states consistently and in detail; not treated as AXELOS's authoritative wording.

<a id="ref-3"></a>[3] Association for Project Management. "[What is a business case?](https://www.apm.org.uk/resources/what-is-project-management/what-is-a-business-case/)" drawing on the APM Body of Knowledge 7th edition. [primary]

<a id="ref-4"></a>[4] Scottish Government, Digital Scotland Service Manual. "[Strategic Outline Case](https://servicemanual.gov.scot/writing-business-case/strategic-outline-case)." [primary]

<a id="ref-5"></a>[5] Scottish Government, Digital Scotland Service Manual. "[Outline Business Case](https://servicemanual.gov.scot/writing-business-case/outline-business-case)." [primary]

<a id="ref-6"></a>[6] Scottish Government, Digital Scotland Service Manual. "[Business case overview and Final Business Case](https://servicemanual.gov.scot/writing-a-business-case)." [primary]

<a id="ref-7"></a>[7] agility-at-scale.com. "[SAFe Lean Business Case: From Epic Hypothesis to Go/No-Go](https://agility-at-scale.com/safe/lpm/lean-business-case/)." [practitioner] A practitioner mirror of a format published by Scaled Agile Inc.; the publisher's own page was not read, which is why the format is deferred rather than shipped as a second size.

<a id="ref-8"></a>[8] Slideworks. "[How to Write a Solid Business Case (with Examples and Template)](https://slideworks.io/resources/how-to-write-a-solid-business-case-examples-and-template)." [practitioner]

<a id="ref-9"></a>[9] ProjectManagementDocs.com. "[Business Case template](https://www.projectmanagementdocs.com/template/project-initiation/business-case/)." [practitioner]

<a id="ref-11"></a>[11] Carlo Alberto Magni and John D. Martin. "[The Reinvestment Rate Assumption Fallacy for IRR and NPV: A Pedagogical Note](https://mpra.ub.uni-muenchen.de/83889/1/MPRA_paper_83889.pdf)" (MPRA Paper No. 83889). [primary] Only pages 1-2 could be read; no claim about the paper's later technical sections is made.

<a id="ref-12"></a>[12] Aswath Damodaran. "[Real Option Valuation](https://pages.stern.nyu.edu/~adamodar/pdfiles/DSV2/Ch5.pdf)," Chapter 5, *Investment Valuation* 2nd ed., NYU Stern. [primary]

<a id="ref-13"></a>[13] Corporate Finance Institute. "[Net Present Value (NPV)](https://corporatefinanceinstitute.com/resources/valuation/net-present-value-npv/)." [practitioner]

<a id="ref-14"></a>[14] Corporate Finance Institute. "[Internal Rate of Return (IRR)](https://corporatefinanceinstitute.com/resources/valuation/internal-rate-return-irr/)." [practitioner]

<a id="ref-15"></a>[15] Corporate Finance Institute. "[Payback Period](https://corporatefinanceinstitute.com/resources/valuation/payback-period/)." [practitioner]

<a id="ref-16"></a>[16] Corporate Finance Institute. "[Return on Investment (ROI)](https://corporatefinanceinstitute.com/resources/accounting/return-on-investment-roi-formula/)." [practitioner]

<a id="ref-17"></a>[17] HM Treasury. "[The Green Book: UK Government Guidance on Appraisal](https://assets.publishing.service.gov.uk/media/6645c709bd01f5ed32793cbc/Green_Book_2022__updated_links_.pdf)" (2022 edition, per the publisher's own filename). [primary]

<a id="ref-18"></a>[18] VX Technology. "[Intangible Benefits Are Not Nonexistent - How to Quantify What Seems Unquantifiable](https://www.vx-technology.com/en/insights/intangible-benefits-are-not-nonexistent)." [vendor] Used only for the honest-quantification pattern, independently corroborated by the Green Book's switching-values guidance [[17]](#ref-17); no claim rests on this source alone.

<a id="ref-19"></a>[19] Bent Flyvbjerg. "[From Nobel Prize to Project Management: Getting Risks Right](https://arxiv.org/pdf/1302.3642)," *Project Management Journal* 37(3), 5-15, 2006. [primary]

<a id="ref-20"></a>[20] Bent Flyvbjerg. "[What You Should Know about Megaprojects and Why: An Overview](https://arxiv.org/pdf/1409.0003)," *Project Management Journal* 45(2), 6-19, 2014. [primary]

<a id="ref-21"></a>[21] HM Treasury. "[Supplementary Green Book Guidance: Optimism Bias](https://assets.publishing.service.gov.uk/media/5a74dae740f0b65f61322c72/Optimism_bias.pdf)," derived from Mott MacDonald 2002, *Review of Large Public Procurement in the UK*. [primary]

<a id="ref-22"></a>[22] G. Locatelli. "[Why are Megaprojects, Including Nuclear Power Plants, Delivered Overbudget and Late? Reasons and Remedies](https://arxiv.org/pdf/1802.07312)" (MIT-ANP-TR-172, CANES, MIT, 2018). [primary]

<a id="ref-23"></a>[23] Peter M. Tingling and Michael J. Brydon. "[Is Decision-Based Evidence Making Necessarily Bad?](https://sloanreview.mit.edu/article/is-decision-based-evidence-making-necessarily-bad/)" *MIT Sloan Management Review*, 26 June 2010. [practitioner]

<a id="ref-24"></a>[24] Project Management Institute. "[Pulse of the Profession 2016: The High Cost of Low Performance](https://www.pmi.org/-/media/pmi/documents/public/pdf/learning/thought-leadership/pulse/pulse-of-the-profession-2016.pdf)." [vendor] The widely circulated "17 percent report high benefits-realisation maturity" figure attributed to this document was not located in the pages read; this source does not support that figure.

<a id="ref-25"></a>[25] thinkpieces.stavros.io. "[How organizations consistently underinvest in the ability to actually evaluate whether a technical initiative worked after it shipped](https://thinkpieces.stavros.io/posts/how-organizations-consistently-underinvest-in-the-ability-to/)" (undated). [practitioner] Read to test the traceability of a cluster of widely repeated statistics, not to source the figures themselves; no figure from this source may be cited as fact.

<a id="ref-26"></a>[26] Marty Cagan (SVPG). "[Product vs. Project Teams](https://www.svpg.com/product-vs-project-teams/)." [practitioner]

<a id="ref-27"></a>[27] Marty Cagan (SVPG). "[What Product Management Is Not](https://www.svpg.com/what-product-management-is-not/)." [practitioner]

<a id="ref-28"></a>[28] Mind the Product. "[Escaping the Build Trap, Melissa Perri](https://www.mindtheproduct.com/escaping-build-trap-melissa-perri/)," a secondary summary. [practitioner] Supports a claim about this summary's coverage, not about Perri's full text, which was not read.

<a id="ref-30"></a>[30] Teresa Torres, Product Talk. Site-wide search across roadmaps, opportunity solution trees and prioritisation material. `https://www.producttalk.org/` [practitioner] **url-confirmed-not-read.** No page body was read; this supports only the observation that a targeted search surfaced no use of the term "business case" in her published vocabulary.

<a id="ref-31"></a>[31] PRINCE2 Wiki. "[Business case](https://prince2.wiki/management-products/baselines/business-case/)," management products, baselines. [practitioner]

<a id="ref-32"></a>[32] PRINCE2 Wiki. "[Project brief](https://prince2.wiki/management-products/baselines/project-brief/)," management products, baselines. [practitioner]

<a id="ref-33"></a>[33] PRINCE2 Wiki. "[Closing a project](https://prince2.wiki/processes/closing-a-project/)," processes. [practitioner]

<a id="ref-34"></a>[34] FHWA Office of Operations. "[Systems Engineering for ITS](https://ops.fhwa.dot.gov/seits/sections/section3/3_4_5.html)," section 3.4.5, Trade Studies. [primary]

<a id="ref-35"></a>[35] ProductPlan. "[Product Requirements Document](https://www.productplan.com/glossary/product-requirements-document/)" glossary entry. [vendor]

<a id="ref-36"></a>[36] PMI. *A Guide to the Project Management Body of Knowledge* (PMBOK Guide) 7th edition, 2021. `https://www.pmi.org/` [primary] **not-retrieved.** Available only to PMI members; no free page states its classification of the business case directly. Cited only for the fact that this bundle's own build spec named it as a key source and could not read it.

<a id="ref-37"></a>[37] ISO 21502:2020. "[Project, programme and portfolio management - Guidance on project management](https://www.iso.org/standard/74947.html)." [primary] **not-retrieved.** The catalogue page returned HTTP 403 and the standard is a paid document. Cited only for the fact that it was sought and could not be read.

<a id="ref-38"></a>[38] ISO 21500:2021. "[Project, programme and portfolio management - Context and concepts](https://www.iso.org/standard/75704.html)." [primary] **not-retrieved.** Paywalled; a reseller sample PDF contained no readable business-case text. Cited only for the fact that it was sought and could not be read.
