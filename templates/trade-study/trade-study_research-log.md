# trade-study: research log

Research conducted 2026-10-15, building on admission sweep 5 (2026-10-12), the spec research of 2026-10-14, and the
spec that merged on 2026-10-15 (`docs/internal/tier2-specs.md:4453-4812`). The build's seven-dimension fan-out
covered the NASA, SEBoK and ECSS canon; the FHWA's trade study step and other published outlines; how criteria are
weighted and options scored; the debates and failure modes; the library's own neighbours and the worked example's
independence; true technical facts about streaming-ingestion options for the worked example; and the standing gap
question. **31 sources are recorded below: 30 fetched-and-verified and one not retrieved.** The 30 are 10 primary,
6 standards bodies, 11 practitioner and 3 vendor. The one not retrieved is MITRE's trade study process [10], which
two passes could not retrieve and which supports no claim. Only `fetched-and-verified` sources are quoted anywhere
in this bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a retrieval tool
returns: pages as downloaded, and PDFs through a text extractor. The build's agents returned 244 quotations. 205
pass as normalized substrings, and 8 more pass once whitespace the extractor broke is ignored. 31 failed and were
dropped. The main loop added 50 quotations from raw text: 40 re-quotes of failed quotations, each cut shorter to
avoid the extraction artifact that failed it, and 10 spans the spec relied on that no agent returned as a separate
quotation (NASA's Table 6.8-1 title and eight of its row names, and the FHWA's "Do Nothing"). **263 quotations
remain.** Every span the spec's admission section quoted is a Quotable line in this log.

---

## What the checks caught, and what was not read

**Eight cached source bodies were not raw text, which this log treats as its most important check finding.** The
example-domain agent stored its own lists of the quotations it said it had extracted, instead of the pages, as the
cache body for six vendor documentation pages: Apache Kafka [26], Kinesis Data Streams [27], Amazon MSK [28],
RabbitMQ Streams [29], NATS JetStream [30] and Google Cloud Pub/Sub [31]. Its quotations therefore passed against
themselves. Two gap-question slide decks, the RAND presentation [25] and Baker and Whalen's NASA survey poster
[24], were cached as agent-written transcriptions with bracketed descriptions of their diagrams. All eight bodies
were replaced with raw fetches, and every quotation from them was re-tested. A check that compares a quotation with
a cached body cannot catch a body that the quoting agent wrote; in this build, only the fresh fetch did.

**The re-test dropped twelve quotations that appear on no page they cite.** Four sentences filed under the
Microsoft playbook's overview page [8] are on its template page instead; one of them, that the decision section
holds "The chosen solution, or a list of questions that need to be answered before the decision can be made", was
already a Quotable line under [9]. Two Kinesis sentences are not on the key-concepts page cited [27], including the
one saying the service ensures durability and giving a put-to-get delay. Five Amazon MSK sentences are not on the
page cited [28]: subnet counts per Availability Zone, Express brokers' storage and zone configuration, MSK
Serverless's capacity management and its access control. A shorter sentence on MSK Serverless that is on the cited
page survives [28]. One Pub/Sub sentence on how messages are leased to subscribers is not on the exactly-once page
cited [31]. `sources-report.txt` lists all twelve. **None of them may be stated anywhere in this bundle as a
sourced fact**, and the example notes below carry the consequence.

**Nineteen more failed for reasons that changed no claim.** Eight failed on artifacts in the raw text, where the
agent's quotation was faithful to the page as rendered: words that the extracted SEBoK page duplicates [2];
replacement characters where the FHWA page's quotation marks should be [4]; footnote markers inside sentences on
the AcqNotes page [5], in the SMC primer [7], on Wikipedia's decision-matrix page [12] and in the UK multi-criteria
analysis manual [14]; a running page header inside a DSMC sentence [6]; and a hyphen the extractor lost from RAND's
Task 6 label [25]. Seven ran list items or outline bullets together: four lines of the SMC primer's trade study
outline [7], the list of methods that exhibit rank reversal [18], the five stages the Barnet critique describes
[21], and the Evidence heading and its list on Microsoft's template [9]. Four changed the source's wording: the
Kafka quotation dropped three words from the middle of its sentence [26]; one ATAM quotation added a period after a
heading and another added two words at its start [20]; and one RAND quotation inserted a bracketed description of a
chart [25]. Where a shorter segment of the same text passed, it was added; where none carried the claim, the claim
is paraphrased with its citation or not made.

**The DSMC chapter needed a second extraction.** The METU course mirror serves the chapter as a two-column PDF [6],
and the first extraction interleaved the columns. The chapter was re-extracted in reading order and its quotations
re-tested. One then still failed. Measured while writing this log, the cause is a running page header that falls
inside the quotation's second sentence. The agent's quotation kept the quotation marks the source prints around the
word quantified, and its first sentence passes with them; the same sentence without the marks fails. The re-quote
ends before the header [6].

**Two spans the spec's admission section quoted were added as Quotable lines after the agents' return.** NASA's
Table 6.8-1 title, "Typical Information to Capture in a Decision Report", and eight of its row names, from
"Executive Summary" to "Dissent", were each tested against the handbook's raw text and added under [1]. The FHWA's
Do Nothing sentence reaches this log as two halves, "It is often good practice to include a" and "alternative as
the base case, depending on the nature of the trade study." [4], because the page's quotation marks around the
alternative's name decode as replacement characters and split the sentence; the name itself, "Do Nothing", passes
on its own and is a Quotable line under [4]. Table 6.8-1's row descriptions and ECSS's Annex L clause headings were
read from the raw text for this log (see the section design below), and they are not Quotable lines, so the
companion paraphrases them.

**Two gap-question sources survived thinly.** Baker and Whalen's poster [24] keeps one Quotable line. Its
Kepner-Tregoe-style worked example, which checks each option against named must-haves above a weighted table of
wants, is in the raw text and can only be paraphrased. RAND's surviving Quotable lines [25] are slide labels, so
they support the existence of separate effectiveness and cost tasks and nothing finer.

**What was assigned and not read, or read only in part:**

- **MITRE's trade study process** [10]: an access-denied block page on both passes, the cache and a direct fetch.
  It supports nothing in this bundle.
- **GAO's Cost Estimating and Assessment Guide.** Not fetched by this build, on instruction. The spec's recheck of
  its spans against the primary `gao.gov` PDF returned HTTP 403 on every span
  (`docs/internal/tier2-specs.md:4518-4526`). It has no entry here, stays a neighbour named in paraphrase, and is
  never quoted.
- **The INCOSE Systems Engineering Handbook.** Not retrieved; treated as paywalled. Two INCOSE conference papers
  that looked likely to bear on the gap question returned a bot-check page instead of their PDFs. INCOSE's
  statement of a trade study's purpose appears here only as the SMC primer quotes it [7], and Felix's 2004 INCOSE
  paper only as Ullman and Spiegel cite it [22]. The FAA Systems Handbook likewise appears only through [22].
- **Kepner-Tregoe's own method text.** The assigned page [11] is a course catalogue with no content on how the
  method weights, scores or screens. The must-and-want split this log attributes to Kepner-Tregoe rests on Umbrex's
  description of it [15] and on the Kepner-Tregoe-style example in [24], not on Kepner-Tregoe's own words.
- **Primary texts for Pugh and AHP.** Neither Pugh's own book nor Saaty's own writing was read. Both methods rest
  here on [12], [13], [15], [16] and the UK manual's secondary treatment [14]. **No consistency-ratio threshold for
  AHP appears in any Quotable line**, so none may appear in this bundle.
- **George Hazelrigg's critique of weighted scoring.** Only secondary characterizations were found, so the
  structural camp in contested item 1 has no primary voice here, and nothing is attributed to him.
- **Smith and Bahill's tradeoff-study paper** (University of Arizona): a 404 on one pass and a certificate error on
  another. Not read.
- **A DAU-hosted trade study template** was not found; the DSMC chapter [6], read through a university mirror, is
  the DAU-lineage text this log holds. **Two state DOT template sets** (Tennessee's and Florida's) were located and
  not opened; neither appeared to be scoped as a trade study.
- **Audit Scotland's options appraisal guide** was read in full by the debates dimension and holds no finding that
  an appraisal was used to justify a decision already made. It has no entry here.
- **Example-domain pages not used.** AWS's Kinesis resilience page was fetched and covers client-application
  failures, not the service's own replication, so no statement of Kinesis replicating across zones is sourced.
  Confluent's replication page and a practitioner explainer on `acks` and `min.insync.replicas` were referenced and
  not read. No NATS page read defines its replication settings or a failure-durability guarantee. Prices were
  deliberately not sought for any service.
- **Promotional figures.** The recovery-speed and scaling multiples for MSK Express brokers that the example-domain
  dimension noted appear in no Quotable line, and may not appear in this bundle.
- **ECSS's clause 3 definitions** were not read in full, so whether ECSS defines trade-off there is unchecked, not
  absent.
- **BABOK is not cited in either direction.** No pass of this build, of the spec research or of admission sweep 5
  read it. The catalog's notes column cites a BABOK section that was never fetched, which is catalog correction 4's
  subject (`docs/internal/tier2-specs.md:4664-4667`).

---

## The admission record

The spec's admission section stands, and this research adds a third public body. **NASA's Systems Engineering
Handbook admits the type in its own glossary** [1]: "A report written to document a trade study." The same handbook
says that "the report may be a simple white paper or a more formally formatted document" [1], which is the evidence
for two sizes, and it introduces its Table 6.8-1 with "Typical information captured in a decision report is shown
in Table 6.8-1." [1]. The table's title, as the spec quotes it, "Typical Information to Capture in a Decision
Report", is also a Quotable line [1].

**The FHWA admits it independently** [4]: "Select and document the preferred candidate, typically using a trade
study matrix that lists the alternatives on one axis". The same section says that "Trade studies compare the
relative merits of alternative approaches to ensure that the most cost-effective system is developed.", that "The
documented trade study is also a repository of alternatives in case a change is needed down the road.", and that
"Sensitivity analysis may also be used, especially with simulation" [4]. Its Do Nothing alternative is carried as
two Quotable halves, "It is often good practice to include a" and "alternative as the base case, depending on the
nature of the trade study." [4].

**ECSS is a third public body, and it specifies the report's content clause by clause.** ECSS-E-ST-10C Rev.1
requires that "The system engineering function shall evaluate alternative concepts, designs and solutions against
each other in a Trade-off report in conformance with Annex L." [3]. Annex L is the normative definition of that
report's content, and its Quotable clauses require weighted and justified criteria, a table of results per
criterion, a ranking, a sensitivity analysis, a recommendation with its conditions, and the risks the recommended
choice induces [3]. ADR 0048 (one named source clears the admission test) needs one source; admission now rests on
three.

**SEBoK corroborates without admitting.** It says "The decision management method most commonly employed by systems
engineers is the trade study" [2], which is SEBoK's own claim about practice and is quoted as such.

**GAO's guide is a neighbour, not an admitting source**, as the spec ruled. It describes the investment sense of an
analysis of alternatives (contested item 4), its spans failed the spec's recheck with HTTP 403, and it has no entry
here. It is named in paraphrase only and never quoted. The spec used GAO to corroborate Sensitivity Analysis, Risk
and Benefit, and Dissent or Independent Review; that corroboration is no longer needed, because each of those
sections now rests on sources in this log (see the section design below).

---

## Claims flagged contested or time-bound

1. **Whether weighted scoring is reliable, or sound when used well.** One camp says the arithmetic itself is
   fragile. A rank reversal is "a change in the rank ordering of the preferability of alternative possible
   decisions when, for example, the method of choosing changes or the set of other available alternatives changes"
   [18]; the methods listed as exhibiting it include "The analytic hierarchy process (AHP) and some of its
   variants." and "The TOPSIS method." [18]; and the UK manual reports that "serious doubts have been raised about
   the theoretical foundations of the AHP" [14]. On false precision, Wikipedia says "The values assigned to each
   option are guesses, not based on any quantitative measurements." [12], Ullman and Spiegel say a Pugh-style
   matrix "can not support uncertainty, a mix of quantitative and qualitative information, or teams" [22], and
   mechanicalc warns that "the results of the trade study should not be taken as absolute" [23]. The other camp
   says the method is sound and its failures are in the inputs. Bromage writes "I use it often, and I think its
   simplicity is the key to its popularity." and locates the failure in "the selection of decision objectives, the
   criteria for making the decision" [17]; ASQ treats the total as a prompt, since "The option with the highest
   score will not necessarily be the one to choose" [13]. The rank-reversal camp is itself divided: Wikipedia
   records that rank reversals "may not be indicative to faulty decision making" and calls the question "a highly
   debated issue in the decision making community" [18], and AHP's current version has one mode that "preserves
   rank" and one that "allows the ranks to change" [16]. Hazelrigg's primary critique was not read. **The bundle
   does not adjudicate.** Its position, which is the library's own, is to require a stated scoring method and a
   justified weight per criterion [3], a sensitivity check in full [6], [14], and the guidance that the total
   informs the recommendation without making it [13].

2. **Must criteria versus want criteria: a separate screen, or one weighted pass.** NASA treats some criteria as
   mandatory: "An option that does not meet mandatory criteria should be disregarded." [1]. The UK manual names the
   screen formally, "The conjunctive model eliminates options that fail to reach externally set levels of
   performance on each of one or more named criteria.", and calls it valid when the benchmarks are set
   independently, "although it is arguable that it scarcely needs formal MCA to make the judgement" [14]. Wikipedia
   names the risk a single weighted pass carries, "Scoring methods, even with weighting, tend to equalize all the
   requirements.", and says enough minor criteria can add up to select an option that misses a must-have [12].
   Umbrex says "Kepner-Tregoe is typically more formal. It separates must-have requirements from wants" [15], and
   Baker and Whalen's Kepner-Tregoe-style example screens options against must-haves before weighting the wants
   [24] (paraphrased; see above). The FHWA [4], AcqNotes [5], Microsoft [8] and the SMC outline [7] describe no
   must-have screen, which is silence rather than disagreement; the FHWA's multiple passes, in which "a limited set
   of criteria is applied to a broad set of alternatives" [4], narrow the field without a must-have gate. ASQ's
   "Identify any criteria that must be included and any that must not be included." [13] is about curating the
   criteria list and must not be read as a performance screen. The sources agree on the risk and differ on the
   remedy.

3. **The Pugh datum versus a do-nothing baseline.** A Pugh datum is a comparator. Umbrex: "Then select the datum,
   which may be the current product, the status quo, the leading concept, or another reasonable reference point."
   [15]. ASQ: "Establish a baseline, which may be one of the alternatives or the current product or service." [13].
   Wikipedia's basic matrix compares every design with one reference candidate design [12]. Umbrex warns "It is
   sensitive to the datum. A poor or biased reference option can distort the entire comparison." and advises
   testing "whether conclusions change when the datum changes" [15]. The FHWA's do-nothing alternative is different
   in kind: it is an alternative scored "as the base case" [4], not the comparator every other option is scored
   against, and the FHWA conditions it on "the nature of the trade study" [4]. NASA says "(Sometimes doing nothing
   or not making a decision is an option.)" [1]. The UK manual reports one case in which "the status quo option of
   continuing intensive agriculture (without GM) often ranked poorly" [14], in a stakeholder-mapping study the
   manual treats separately from its core method. No source read here calls a Pugh datum a do-nothing alternative.
   **The bundle scores do-nothing as an alternative; whether an author also uses it as a datum is the author's
   choice**, and the guide should say that a do-nothing datum carries Umbrex's caution.

4. **The investment sense versus the technical sense of analysis of alternatives (catalog correction 5).** The
   phrase names two different things across these sources. In US defense acquisition it names a decision about what
   to acquire: RAND's presentation [25], given at an acquisition research symposium, frames its analysis of
   alternatives around "Measuring the cost and benefits of each alternative", with "Task 4: Perform effectiveness
   analysis" and "Task 5: Estimate life cycle costs" ahead of a combined cost-effectiveness task [25]. GAO's guide
   and HM Treasury's Green Book, named by the spec (`docs/internal/tier2-specs.md:4668-4673`) and not read in this
   build, are in the same sense. Yet the SMC primer's own trade study outline lists performing an analysis of
   alternatives, glossed as comparative analysis, as one purpose a trade study can serve [7] (read in raw text; the
   outline line is not a Quotable line). And Wikipedia notes that the decision matrix, "frequently used in
   engineering for making design decisions", is also used to rank investment and vendor options [12]. So the
   scoring mechanism does not separate the two senses; the subject of the decision does. **Catalog correction 5
   stands for exactly this reason**: an alias that one major usage reads as an acquisition or investment appraisal
   would route that reader to a document that does not cover it.

5. **One recommended option, or every closely ranked one.** ECSS requires a single answer: "The trade-off report
   shall recommend one solution and explain the reason for this choice" [3]. NASA says "Generally, a single
   alternative should be recommended." but, where the alternatives do not differ significantly or uncertainty could
   alter the ranking, "the recommendation should include all closely ranked alternatives for a final selection by
   the decision-maker" [1]. Microsoft's template lets the decision section hold open questions instead, where "each
   question needs an action item and an assigned person for answering the question" [9]. Letting the Recommendation
   section report a near-tie as one, with what would separate the options, is the library's reading of [1] and [9]
   against [3].

6. **What a weight means: importance, or the swing between the options.** Wikipedia: "The more important the
   criterion the higher the weighting it should be given." [12]. ASQ allocates by importance, "By distributing 10
   points among the criteria" [13]. The UK manual: "Most proponents of MCDA now use the method of 'swing weighting'
   to elicit weights for the criteria.", and "the weight on a criterion reflects both the range of difference of
   the options, and how much that difference matters" [14]. These are two meanings of a weight, not two names for
   one. The sources also differ on whether a Pugh comparison is summed: the basic matrix's counts are displayed
   "but not summed up" [12], ASQ multiplies and adds [13], and Umbrex reports that some teams "add criterion
   weights or convert symbols into numbers" [15]. The template should ask the author to say which meaning their
   weights carry; it should not pick one.

7. **The predetermined winner: one advocacy critique, not an audit finding.** The Barnet critique says "The options
   appraisal process is flawed because it is operating to a predetermined agenda" [21], and describes a sequence
   that starts "Decide on a preferred solution or the" direction of travel and "Select a consultant who will
   deliver the" right solution [21]. Its entry title records that it was prepared for two trade unions opposing the
   transfer it critiques, and no neutral audit body's equivalent finding was found. Bromage's anecdote, in which
   "the alternative selected based on the evaluation of the decision objectives ended up to be number 4!" [17], is
   one practitioner's story. Both may illustrate the failure; neither is evidence of how often it happens.

8. **Time-bound facts.** Every fact from [26] to [31] is product documentation that changes with the product. The
   Kafka page is the 4.2 documentation [26]. Kinesis's 24-hour default retention, its 365-day maximum and its
   per-shard limits [27] are service limits as documented when read, not properties of streaming. MSK's page names
   both ZooKeeper nodes and KRaft controllers [28]; which one a given cluster uses is a version fact this log does
   not settle. Pub/Sub's exactly-once constraints [31] describe the feature as documented when read. The product
   names themselves (Kinesis Data Streams, Amazon MSK, RabbitMQ Streams, NATS JetStream, Google Cloud Pub/Sub) are
   as the pages used them when read, and the example should name each as current at its own date. The older sources
   carry their dates too: the SMC primer is 2005 [7], the UK manual 2009 [14], NASA's handbook Rev 2 2016 [1], and
   ECSS's Rev.1 2017 [3]; the Microsoft playbook [8], [9] is a living page.

---

## Notes for the companion

**The honest framing.** A trade study compares named technical alternatives against weighted criteria and records
the recommendation the comparison supports. The sources that define it frame its subject as technical. NASA's
glossary: "evaluating system designs by devising alternative means to meet functional requirements", in terms of
the "measures of effectiveness and system cost" [1]. The FHWA: "compare the relative merits of alternative
approaches to ensure that the most cost-effective system is developed" [4]. ECSS: to "assist in selecting system
concepts, designs and solutions" [3]. INCOSE, as the SMC primer quotes it: to "provide an objective foundation for
the selection of one of two or more alternative approaches to solution of an engineering problem" [7]. The FAA, as
Ullman and Spiegel quote it: "the most balanced technical solutions among a set of proposed viable solutions" [22].
Baker and Whalen: "the most acceptable technical solution among a set of proposed solutions" [24]. In each, the
organization has already taken the problem on, and the question is which approach solves it; cost sits inside the
comparison as a criterion, not outside it. **That is the ground for the boundary against `business-case`, and the
boundary itself is the library's position.** No definition quoted in this log frames a trade study as the decision
whether to invest, and no source read here draws a line between a trade study and a business case. The one source
that names a business case, the Barnet critique [21], places it after an options appraisal, in the investment
sense. `business-case_companion.md` section 8 draws that line and cites the FHWA's merits sentence for it; the
companion should rest the line on the definitions above, not on that sentence alone. It must not round the line up
either. SEBoK says trade studies "aim to define, measure, and assess shareholder and stakeholder" value [2], the
SMC outline lists an analysis of alternatives among a trade study's purposes [7], and the decision matrix is also
used for investment options [12] (contested item 4). The line is clean on subject and blurred in vocabulary, and
the companion should say both.

**Against its siblings, the companion places the trade study four ways and overstates none of them.** Contract
section 1 names three roles, propose, record and describe, and says a candidate whose job is none of them belongs
in another family (`docs/internal/contracts/decision-docs.md:11-17`). Evaluating named options is none of the three
verbs, so section 1 read alone would exclude this type. It joins on ADR 0022's clause that a further member joins
with no contract change unless it declares a different phase or size shape
(`docs/internal/decisions/0022-adopt-decision-docs-family-contract.md:84-85`), as `spike-report` did, and it
declares neither. The Relationships section must place it against `adr`, `rfc`, `sdd` and `spike-report`
(`docs/internal/tier2-specs.md:4718-4723`): an ADR records the decision a trade study's options feed; an RFC or SDD
whose Alternatives Considered prose needs weights can cite a trade study; a spike reduces an unknown before the
options exist. One boundary needs a caveat. NASA's decision report also records the outcome, since it includes the
"recommendation, and final decision" [1]. Separating the evaluation from the record of the decision is this
library's division of labour, not a line NASA draws. Microsoft's playbook recommends the same hand-off in its own
vocabulary: "Once the decision has been made we recommend adding an entry to the Decision Log that has references
back to the full text of the trade study" [8].

**Evidence of effect, stated plainly.** No source in this research measured whether writing a trade study improves
a decision or its outcome. The statements of value are claims, not measurements: Baker and Whalen's poster says
trade studies "provide an effective means for addressing this by documenting the decision-making process to enable
traceability and repeatability" [24]; SEBoK says "Reports are important for historical traceability and future
decisions." [2]; and the FHWA calls the documented study "a repository of alternatives" [4]. SEBoK cites research
concluding that cognitive bias "can seriously distort decisions made by any decision maker" [2]; that is evidence
about bias, not about whether a trade study reduces it. The ATAM paper [20] is an experience report, the Barnet
critique [21] is an advocacy document about one appraisal, and Donald's essay [19] concerns grant panels. The
companion may cite each as what it is, and must not imply that any of them measured an effect.

**Build decisions, 2026-10-15, taken from the notes below and overrulable by the maintainer.** The drafting
stages follow this list. Lean carries five sections, in this order: Problem and Decision Framing; Criteria and
Weights; Alternatives, Including a Do-Nothing Baseline; Scoring Matrix; Recommendation. Full carries nine, in this
order: Problem and Decision Framing; Criteria and Weights; Alternatives, Including a Do-Nothing Baseline; Scoring
Matrix; Sensitivity Analysis; Risk and Benefit; Recommendation; Dissent or Independent Review; References. Two
changes from the spec follow from the research: the word Mandatory leaves the Alternatives heading, because NASA [1]
and the FHWA [4] both make the do-nothing option conditional, so the template asks for the baseline and lets a
document that genuinely has none say why in one line; and Risk and Benefit covers every option still in contention,
not only the recommended one. The catalog's unsourced owner, "Architect / BA", becomes "Systems engineer /
engineering team", the value the sources below support. GAO is no longer needed to support any section.

**The section design, as the research moved it from the spec.** The spec's nine sections stand in order, with one
rename recommended below. Lean carries Problem and Decision Framing, Criteria and Weights, Alternatives, Scoring
Matrix and Recommendation; full inserts Sensitivity Analysis and Risk and Benefit before Recommendation, and
Dissent or Independent Review and References after it. The two sizes rest on NASA's "simple white paper or a more
formally formatted document" [1]; on AcqNotes' "formal trade studies are indicated for high-value, high-risk, or
other high-impact decisions" [5]; on DSMC's formal studies, those "used in formal decision forums", against the
less formal ones "documented in summary detail only" [6]; and on Microsoft's "Trade studies should be avoided if
there is a clear solution choice." [8].

**NASA's Table 6.8-1, now read in raw text, changes no section name or order.** Its rows run, in order: 1 Executive
Summary, 2 Problem/Issue Description, 3 Decision Matrix Setup Rationale, 4 Decision Matrix Scoring Rationale, 5
Final Decision Matrix, 6 Risk/Benefits, 7 Recommendation and/or Final Decision, 8 Dissent, 9 References, and A
Appendices. That is exactly the order the spec reconstructed from a research summary
(`docs/internal/tier2-specs.md:4618-4625`). The row descriptions add content the spec did not have. Row 3 asks for
the evaluation methods selected, as well as the criteria, options and weights. Row 4 asks for the rationale behind
the scores. Row 6 covers the risks and benefits of each final option, not only the chosen one. Row 7 allows the
final decision to be recorded in the same section. Row 8 asks how dissent was addressed. These rows and
descriptions are paraphrased from the raw text; none is a Quotable line.

**ECSS's Annex L, also read in raw text, gives Sensitivity Analysis the structural match the spec lacked.** Its ten
content clauses run: introduction; applicable and reference documents; objective and context of the study; key
technical requirements; evaluation criteria; presentation of the alternatives; their evaluation; their
classification; analysis of the robustness of the classification; and conclusion [3]. Criteria precede
alternatives, as in the spec and as the FHWA advises, since "Ideally, the criteria are developed early in the trade
study process, before the alternatives are selected" [4]. Robustness analysis follows the classification and
precedes the conclusion. That is where the spec puts Sensitivity Analysis, a placement the spec had called the
library's own (`docs/internal/tier2-specs.md:4612-4616`). The SMC outline orders it the same way, with "Sensitivity
Analysis" in its analytical approach ahead of its trade results [7]. ECSS also asks for four things the spec did
not, each a Quotable line: each weight justified, "provide the weighting of criteria and their justifications" [3];
"the entity responsible for the evaluation of the design solutions for any criteria, as well as the source and
agreement regarding weighting factors (e.g. with management)" [3]; the recommendation's conditions, "precise the
condition for the application of the recommended solution" [3]; and "the identified technical and programmatic
risks induced by the choice of the recommended solution, and any additional activity necessary to be performed for
risk mitigation" [3].

Section by section:

- **Problem and Decision Framing** (lean): the question, the decision it informs, who decides, and the constraints
  and assumptions the options must respect. Sourced to the FHWA's "First, define the question the trade study is to
  answer." [4]; NASA's "decision to be made" [1] and its Problem/Issue Description row, which names the decision
  makers (raw text); SEBoK's decision context, in which "the analyst should describe the system baseline,
  boundaries and interfaces" and which includes "a list of decision makers and stakeholders" [2]; DSMC's "Defining
  the problem entails developing a problem statement including any constraints." [6]; and AcqNotes' "Define the
  problem - Make sure you address the actual problem, not a symptom." [5].
- **Criteria and Weights** (lean): each criterion and its weight, why each was chosen and weighted so, which
  criteria are mandatory, and the scoring method and scale. Sourced to the FHWA's "These disparate evaluations are
  merged using the weighting factors" and its criteria-first advice [4]; ECSS's justification clause [3]; NASA's
  mandatory criteria [1]; AcqNotes' "Determine weight factors" [5]; DSMC's "determining weighting factors (if any)"
  [6]; the SMC outline's "Weighted reflecting their relative importance in the selection process" [7]; and ASQ's
  procedure [13].
- **Alternatives, Including a Do-Nothing Baseline** (lean; **rename recommended**): every option considered, how
  the set was narrowed, and a do-nothing or do-minimum row. Sourced to "Be sure that all reasonable alternatives
  are on the table." [4]; the FHWA's two base-case halves [4]; NASA's "(Sometimes doing nothing or not making a
  decision is an option.)" [1]; NASA's trade tree, which "is an excellent way to prune the set of variations before
  extensive analysis is undertaken" [1]; the FHWA's multiple passes [4]; and Microsoft's advice to "pick the 2-4
  solutions that seem most promising" [8]. **Both sources that name the baseline make it conditional**: the FHWA's
  "depending on the nature of the trade study" [4] and NASA's "Sometimes" [1]. Of the other outlines read here,
  AcqNotes, Microsoft, the SMC primer and DSMC do not mention one in the text read. Requiring the row is therefore
  the library's position, arguable only under procedure 12's E2 clause
  (`docs/internal/decision-procedures.md:237`). **Its falsifier:** adding the do-nothing row changes the ranking
  among the live options, which is the rank-reversal mechanism [18], and which weights set on the range of the
  options [14] make possible. The spec's heading puts the word Mandatory in the section name; this log recommends
  dropping the word from the heading and keeping the requirement in the guidance, where it can be labelled as the
  library's own and can allow a one-line rejection.
- **Scoring Matrix** (lean): the completed comparison, the weighted total, and the basis for each score. Sourced to
  the FHWA's matrix sentence [4]; ECSS's requirement to "present, in a table, the result of the evaluation per
  criteria" and its classification clause [3]; ASQ's "Multiply each option's rating by the weight. Add the points
  for each option." [13]; AcqNotes [5]; DSMC [6]; and NASA's setup, scoring-rationale and final-matrix rows (raw
  text). The FHWA's orientation, alternatives on one axis and criteria on the other [4], leaves rows and columns to
  the author.
- **Sensitivity Analysis** (full): how far a weight or a score would have to move before the recommendation
  changes. Now sourced in this log to NASA's glossary, which puts "computational results, including uncertainty
  ranges and sensitivity analyses performed" in a trade study report [1]; to ECSS's "the result of a sensitivity
  analysis of the criteria that provide advantage to the solution ranked first, e.g. when changing the weighting of
  the evaluation criteria" [3]; to DSMC's "the sensitivity analysis is crucial. If the solution can be changed with
  relatively minor changes in data input, the study is probably invalid" [6]; to the UK manual's eighth step [14];
  to Wikipedia's test "to see how much your opinion would have to change in order for a lower ranked alternative to
  outrank a competing alternative" [12]; and to the FHWA [4]. NASA's section 6.8.1.3.1 also lists assumptions,
  uncertainties and sensitivities among a decision report's contents (raw text). The spec's statement that NASA's
  template has no sensitivity section (`docs/internal/tier2-specs.md:4612-4613`) is true of Table 6.8-1 alone.
- **Risk and Benefit** (full): **position stands; content should widen.** The spec defines the section as the
  recommended option's risk and benefit profile and places it before Recommendation, as NASA orders its rows. But
  NASA's row 6 covers each option still under consideration (raw text), and ECSS puts the recommended option's
  induced risks and their mitigation in its conclusion, after the recommendation [3]. This log recommends that the
  section carry the risks and benefits of every option still in contention, plus the mitigation the leading option
  would need [3]. Keeping NASA's position rather than ECSS's is the library's position.
- **Recommendation** (lean): the option the matrix supports, the rows it depends on, the conditions under which it
  holds, and a near-tie reported as one. Sourced to the FHWA's "Select and document the preferred candidate" [4];
  ECSS's recommendation and conditions clauses [3]; NASA's single-or-closely-ranked rule [1] (contested item 5);
  and Microsoft's open questions with owners [9]. NASA's row 7 lets this section record the final decision (raw
  text). In this bundle it may record the decision taken in one line and point to the ADR that records it, which is
  the library's division of labour (see the honest framing).
- **Dissent or Independent Review** (full): who disagreed and how it was addressed, or who checked the scoring and
  how independent they are. Sourced to NASA's Dissent row (raw text); to SEBoK's independent review, whose
  authority "must be both organizationally and financially independent of the program in question" [2]; to
  Bromage's "if you stand to benefit greatly from one of the possible outcomes of the decision, have an
  independent, third party lead the decision-making process." [17]; and to the FHWA's "Have key stakeholders
  reviewed and support the trade study results?" [4]. ECSS's Annex L has no equivalent clause, which suits a
  full-only section.
- **References** (full): the data, models and documents the criteria, weights and scores rest on. Sourced to the
  NASA glossary's "all data sources used" [1] and NASA's References row (raw text), and to ECSS's applicable and
  reference documents clause (raw text).

**Gap-question candidates, routed by decision procedure 12.** Each is a CANDIDATE for the build to accept or
decline; this log admits none of them.

- **Candidates for an existing section's ASK or ROW HINT** (E1 sourced, E3 homed in the named section, E4 sized for
  lean unless noted): the decision makers and who conducted the study, in Problem and Decision Framing or the
  frontmatter, from Microsoft's "Conducted by" and "Decision Makers" fields [9], SEBoK [2] and NASA's row 2 (raw
  text); constraints and assumptions, in Problem and Decision Framing, from "Assumptions about the rest of the
  system" and "Constraints that apply to the system, both business and technical" [9], the SMC outline's "Identify
  Influencing requirements & constraints" [7], and [5], [6]; a mandatory marker on criteria, in Criteria and
  Weights, from [1], [14], [12], [15] and [24]; each weight's justification and who agreed it, in Criteria and
  Weights, from [3]; and the conditions under which the recommendation holds, in Recommendation, from [3] and [9].
- **Candidates for a guide rubric row:** what each point on the scale means, as in "a scale of 1-5, where 1 is very
  poor and 5 is excellent" [23] and ASQ's anchored scales [13]; the basis for each score, from Microsoft's "Present
  the evidence collected during experimentation that supports the hypothesis that this solution will meet the
  desired outcomes." [9] and NASA's scoring-rationale row (raw text); uncertainty ranges on scores, from Ullman and
  Spiegel's "supplementing point estimates of the outcome variables for each alternative with computed or estimated
  uncertainty ranges" [22], bounded by NASA's "Uncertainty matters in a particular analysis only if there is a
  non-zero probability that uncertainty reduction could alter the ranking of alternatives." [1]; the unweighted
  total beside the weighted one, since in some versions "the sum of the unweighted scores is also calculated and
  both totals are studied for guidance toward a decision" [13]; a matrix "easily comprehensible to management and
  other stakeholders" [4]; and cost shown as a view separate from the weighted score, from RAND's separate
  effectiveness and life-cycle-cost tasks [25]. That last one is at most a rubric row: its Quotable lines are task
  labels, and RAND speaks in the acquisition sense (contested item 4).
- **Candidates for the guide's anti-patterns, as sourced and no further:** criteria chosen after the options, to
  favour one ([4], [17]); criteria with no measure, which Bromage warns against as "selecting weak criteria that
  have only qualitative evaluation possibilities" [17]; a must-have outvoted by many minor criteria [12]; a result
  that flips on a small change [6]; scorers who use the scale differently, since "some people will use the full
  range, but others will probably cluster scores between 4 and 8" [19], or who anchor on the first figure or the
  first speaker [19]; averaged disagreement, against ASQ's "Do not average the ratings or vote for the most popular
  one." [13]; a biased datum [15]; and the total treated as the decision ([13], [23]).
- **Routed elsewhere:** the hand-off to a recorded decision belongs in the companion's Relationships section,
  toward `adr` [8]. The FHWA's repository of rejected alternatives [4] belongs in the Alternatives section's WHY,
  not in a new section.
- **Declined or left to the author, each recorded as a research gap rather than a confirmed absence:** a date by
  which the decision is needed, because no template read carries one; criteria traced to requirement identifiers,
  because the traceability source found speaks of the decision process as a whole [24] and the INCOSE paper that
  might settle it was not read; a reversibility or revisit-trigger field, because Microsoft's "Decisions should be
  made with the understanding that they can change as the team learns more." [9] is a caveat, not a field; a
  sign-off on the scores themselves, because RAND's steering group approves study decisions such as the "final set
  of alternatives" [25], not scores; and an executive summary, which NASA's row 1 carries (raw text) and the spec
  drops, since Recommendation already states the answer.

**Who writes it.** The catalog's owner value, Architect / BA, is unsourced (catalog correction 3,
`docs/internal/tier2-specs.md:4661-4663`), and no source in this research names either role. These are the roles
the sources do name. ECSS assigns trade-off analyses to "The system engineering function" and requires the report
to name the entity responsible for evaluating each criterion and who agreed the weights [3]. SEBoK names an
analyst, a "decision analysis team", "subject matter experts (SMEs) and stakeholders", and decision makers [2], and
calls the trade study the method "most commonly employed by systems engineers" [2]. DSMC calls trade studies a
methodology "used by integrated teams" [6]; the FAA, as Ullman and Spiegel quote it, calls one "the activity of a
multidisciplinary team" [22]. Microsoft's template separates "Conducted by" from "Decision Makers" [9]. NASA's
handbook lists participants from systems engineers, design engineers and decision scientists to operators and
project managers, and its decision report names the decision makers and the recommendation team; both are read in
raw text and are not Quotable lines [1]. RAND names a study director overseen by a steering group [25], in the
acquisition sense. **Recommendation:** replace Architect / BA with a value the sources support, such as `Systems
engineer / engineering team`, with the decision maker named separately in the document. Drop BA, which no source
names. A software-team label such as tech lead or architect would be the library's own translation and must be
labelled so. The spec's catalog correction 3 leaves the value for the landing build to decide.

**Licences.** No Quotable line in this log states a licence or reuse terms for any source. The companion must not
assert one for any of them, including the government handbooks and the Wikipedia articles. The templates' GOOD and
WEAK text must not adapt any source's worked example or wording: not Microsoft's template fields, not ASQ's or the
UK manual's procedures and examples, not Baker and Whalen's vehicle example, not mechanicalc's scale, and not
Bromage's anecdote. Short attributed quotations in the companion are the only reuse this log supports.

**The example.** The worked example is set at a new fictional logistics company, working name Thornwell Freight,
choosing a message-ingestion technology for GPS telemetry from its truck fleet, against a do-nothing baseline of
the current nightly batch upload (`docs/internal/tier2-specs.md:4751-4767`).

**What independence requires, and what the checker actually tests.** Contract section 4 requires decision-docs
examples to be deliberately independent, each a different decision or design, and places a cross-reference rule on
the companions rather than a plot rule (`docs/internal/contracts/decision-docs.md:42-44`).
`tools/check-example-independence.py` does not test that rule. Its docstring says it fails a bundle whose worked
example reuses its own template's GOOD and WEAK text (line 2). It compares a bundle's own guidance snippets
(`guidance_snippets`, line 56) with that bundle's own example prose (`example_prose`, line 69), reports a shared
run of 6 words and fails one of 8 (lines 45-46), and has no mechanism that compares one bundle's example with a
sibling's. `trade-study` is not in its `GRANDFATHERED` map (line 174), so any run of 8 shared words fails outright.
**The spec's sentence that the script enforces the distinct-jobs rule (`docs/internal/tier2-specs.md:4724-4727`)
overstates it**; the cross-sibling check is the manual grep the spec's risk 4 names (lines 4726-4730).

**Proper nouns the four siblings use, which the example must not reuse.** `adr_example.md` is a real decision about
this repository, with decision makers jprisant and claude, dated 2026-07-12. `rfc_example.md` is also about this
repository: jprisant and claude, RFC-0001 and WP-22, created 2026-07-16, updated 2026-07-17, review by 2026-07-30.
`sdd_example.md` is the Saved Views for Dashboards design from the Acme Analytics chain the delivery-docs examples
share: Marcus Bell, Priya Nair and Dana Osei, the Reporting and Platform teams, Recurring Analysts, ADR-014 and
Postgres, created 2026-07-02 and updated 2026-07-09. `spike-report_example.md` is set at Riverland Sensing: Hana
Okafor, SPK-2026-014, OPS-1187, and nodes RS4-0031, RS4-0033 and RS4-0035, dated 2026-09-04. A grep of every
`templates/*/*_example.md`, rerun for this log, finds no use of Thornwell, Kafka, GPS, truck, MSK, Kinesis,
Pub/Sub, RabbitMQ or JetStream. The word fleet appears in the spike report, for its monitoring nodes, and telemetry
appears in several Acme examples; both are generic words, not collisions. The spec's statement that the `adr`,
`rfc` and `sdd` examples share the Acme Analytics scenario (`docs/internal/tier2-specs.md:4747-4748`) is true of
the `sdd` example only; contract section 4 itself says the RFC and ADR examples are real repository decisions
(`docs/internal/contracts/decision-docs.md:44`).

**The family's example dates run from 2026-07-02 to 2026-09-04.** No file mandates a date for this example; the
spec leaves dates, names and figures to the build (`docs/internal/tier2-specs.md:4766-4767`). A date after
2026-09-04 and no later than the landing date fits both the family's range and the library's most recent builds.

**The true technical facts the criteria rows may use**, each from a Quotable line that survived the re-test:

- **Self-managed Kafka [26].** Replication is configurable per topic: "you can set this replication factor on a
  topic-by-topic basis". Each partition has "a single leader and zero or more followers", and "All writes go to the
  leader of the partition". Producers choose, through "the acks setting that the producer uses", whether to wait
  for a commit, "depending on their preference for tradeoff between latency and durability"; with a less stringent
  setting, a message is committed "asynchronously across the set of in-sync replicas if acks=0" or "synchronously
  only on the leader if acks=1". Topics have "a setting for the minimum number of in-sync replicas
  (min.insync.replicas)". The guarantee is conditional: "a committed message will not be lost, as long as there is
  at least one in sync replica alive, at all times.", "Only committed messages are ever given out to the
  consumer.", and "Kafka will remain available in the presence of node failures after a short fail-over period".
- **Amazon MSK, the managed Kafka option [28].** It "provides the control-plane operations, such as those for
  creating, updating, and deleting clusters." The customer chooses how many brokers to place in each Availability
  Zone, and "The minimum is one broker per Availability Zone." MSK creates the ZooKeeper nodes, and "KRaft
  controllers are included at no additional cost to you, and require no additional setup or management from you."
  On a broker failure, "it mitigates the failure or replaces the unhealthy or unreachable broker with a new one."
  MSK Serverless lets a team "Run Apache Kafka without having to manage and scale cluster capacity".
- **Kinesis Data Streams, a second managed option [27].** Retention defaults to 24 hours and can be raised to "8760
  hours (365 days)", and "Additional charges apply for streams with a retention period set to more than 24 hours."
  Capacity is per shard: each "can support up to 5 transactions per second for reads, up to a maximum total data
  read rate of 2 MB per second and up to 1,000 records per second for writes, up to a maximum total data write rate
  of 1 MB per second (including partition keys)." In on-demand mode the service "automatically manages the shards";
  in provisioned mode "you must specify the number of shards for the data stream." No durability, replication or
  latency statement for Kinesis survived, so if the example needs a durability row for its managed option, MSK is
  the one this log supports.
- **RabbitMQ Streams, a third broker [29].** "Streams are always persistent and replicated.", but they "do not
  explicitly flush (fsync) the data from the operating system page cache", so "an uncontrolled shutdown of a server
  could result in data loss for replicas hosted on that node." Confirmed writes differ: "publisher confirms are
  only issued once the data has been replicated to a quorum of stream replicas", and "No guarantees are provided
  for messages that have not been confirmed using the publisher confirm mechanism". Without a retention setting,
  "the log will grow indefinitely until the disk runs out". Operations fall to the team: "Replicas of a stream are
  explicitly managed by the operator.", "A stream requires a quorum of the declared nodes to be available to
  function.", and "Care needs to be taken not to accidentally make a stream unavailable by losing the quorum."
- **NATS JetStream, an alternative third broker [30].** Only its delivery semantics are sourced: "JetStream adds a
  persistence layer on top, giving you at-least-once delivery", against Core NATS, which delivers "at most once".
  If the example needs durability or operations rows for its third broker, RabbitMQ Streams is the one this log
  supports.
- **Google Cloud Pub/Sub, if a managed option needs a delivery-semantics row [31].** Its exactly-once feature is
  narrow: "Only the pull subscription type supports exactly-once delivery.", "The exactly-once delivery guarantee
  only applies when subscribers connect to the service in the same region.", a subscriber spread across regions
  "can lead to duplicate message delivery, even when exactly-once delivery is enabled.", "A subscription might
  receive multiple copies of the same message due to publish side duplicates", and without the acknowledgment
  interface "the acknowledgment failures can lead to silent re-deliveries of messages."

**What the example must not assert, because this research could not source it:** that Kinesis replicates across
Availability Zones, or any put-to-get or end-to-end latency figure for any option; any delivery-semantics claim for
Kinesis or MSK; anything about MSK Express brokers (storage, zone count, recovery or scaling multiples), MSK
Serverless's access control, or MSK's subnet requirements; NATS JetStream's replication settings or failure
durability; Kafka's default `acks`, its default replication factor, or its exactly-once features; that Kafka is
durable as an inherent property, rather than under a stated `acks` and `min.insync.replicas` configuration [26];
any price for any service; and the operational burden of self-managed Kafka as a sourced fact, since only MSK's
side of that contrast is sourced [28]. The team's latency measurements, cost estimates, familiarity with each
option, fleet size and ping volume are the example's own fictional facts. **Every figure in the example is labelled
illustrative**, including any figure that restates a documented limit, because those limits are time-bound
(contested item 8).

**What it must not do.** The bundle must not quote GAO anywhere, or paraphrase its content beyond naming it as a
neighbour, because it has no entry here to cite. It must not frame a trade study as an investment decision, or use
`analysis of alternatives` as an alias or a synonym for the type (catalog correction 5). The example must not reuse
Acme Analytics, Riverland Sensing or any proper noun listed above, and it must not state a technical claim beyond
the sourced facts above. **The example's own proper nouns must not appear in template guidance text**: before
review, grep the drafted templates for Thornwell, Kafka, MSK, Kinesis, RabbitMQ, NATS, Pub/Sub, GPS, telemetry,
truck and the example's people (`docs/internal/tier2-specs.md:4731-4735`). The companion must not present the
must-and-want split as Kepner-Tregoe's own words ([11], [15]); must not attribute anything to Hazelrigg, MITRE or
BABOK, or to INCOSE's handbook beyond what the SMC primer quotes [7]; must not present the Barnet critique as an
audit finding [21]; must not treat the Pugh datum and the do-nothing alternative as the same thing (contested item
3); must not say any source requires the do-nothing row, which is the library's position; and must not claim that
any source measured an effect.

---

## Sources

### CANON: NASA'S DECISION ANALYSIS, SEBOK AND THE ECSS TRADE-OFF REPORT

**[1] NASA, Systems Engineering Handbook, SP-2016-6105 Rev 2 (2016).** primary. **fetched-and-verified.**
`https://ntrs.nasa.gov/api/citations/20170001761/downloads/20170001761.pdf`
Supports: NASA's verbatim definitions of Trade Study and Trade Study Report (Glossary); Section 6.8 Decision Analysis process steps, criteria/weighting, alternative identification, evaluation, sensitivity/uncertainty treatment; Table 6.8-1 'Typical Information to Capture in a Decision Report' with every row and description verbatim; participant language
Quotable: "A means of evaluating system designs by devising alternative means to meet functional requirements, evaluating these alternatives in terms of the measures of effectiveness and system cost, ranking the alternatives according to appropriate selection criteria, dropping less promising alternatives, and proceeding to the next level of resolution, if needed."
Quotable: "A report written to document a trade study. It should include: the system under analysis; system goals, objectives (or requirements, as appropriate to the level of resolution), and constraints; measures and measurement methods (models) used; all data sources used; the alternatives chosen for analysis; computational results, including uncertainty ranges and sensitivity analyses performed; the selection rule used; and the recommended alternative."
Quotable: "A representation of trade study alternatives in which each layer represents some system aspect that needs to be treated in a trade study to determine the best alternative."
Quotable: "Decision Analysis is a framework within which analyses of diverse types are applied to the formulation and characterization of decision alternatives that best implement the decision-maker's priorities given the decision-maker's state of knowledge."
Quotable: "A decision analysis report should be generated including: decision to be made, decision criteria, alternatives, evaluation methods, evaluation process and results, recommendation, and final decision."
Quotable: "Decision criteria are requirements for individually assessing the options and alternatives being considered. Typical decision criteria include cost, schedule, risk, safety, mission success, and supportability."
Quotable: "Criteria may be mandatory (i.e., “shall have”) or enhancing. An option that does not meet mandatory criteria should be disregarded."
Quotable: "It is a best practice to document a decision matrix for a major decision even if only one alternative is determined to be viable. (Sometimes doing nothing or not making a decision is an option.)"
Quotable: "A “trade tree” (discussed later) is an excellent way to prune the set of variations before extensive analysis is undertaken, and to convey to other stakeholders the basis for that pruning."
Quotable: "Evaluation methods and tools/techniques to be used should be selected based on the purpose for analyzing a decision and on the availability of the information used to support the method and/or tool. Typical evaluation methods include: simulations; weighted tradeoff matrices; engineering, manufacturing, cost, and technical opportunity trade studies; surveys; human-in-the-loop testing; extrapolations based on field experience and prototypes; user review and comment; and testing."
Quotable: "Uncertainty matters in a particular analysis only if there is a non-zero probability that uncertainty reduction could alter the ranking of alternatives."
Quotable: "A robust decision is one that is based on sufficient technical evidence and characterization of uncertainties to determine that the selected alternative best reflects decision-maker preferences and values given the state of knowledge at the time of the decision."
Quotable: "Generally, a single alternative should be recommended. However, if the alternatives do not significantly differ, or if uncertainty reduction could credibly alter the ranking, the recommendation should include all closely ranked alternatives for a final selection by the decision-maker."
Quotable: "Based on the mission and system context and the decision made, the report may be a simple white paper or a more formally formatted document."
Quotable: "Typical information captured in a decision report is shown in Table 6.8-1."
Quotable: "Typical Information to Capture in a Decision Report"
Quotable: "Executive Summary"
Quotable: "Problem/Issue Description"
Quotable: "Decision Matrix Setup Rationale"
Quotable: "Decision Matrix Scoring Rationale"
Quotable: "Final Decision Matrix"
Quotable: "Risk/Benefits"
Quotable: "Recommendation and/or Final Decision"
Quotable: "Dissent"

**[2] SEBoK Editorial Board, 'Decision Management' (Lead Author Matt Cilli; Contributing Authors Garry Roedler, Greg Parnell, and Scott Jackson), SEBoK wiki.** standards. **fetched-and-verified.**
`https://sebokwiki.org/wiki/Decision_Management`
Supports: SEBoK's purpose statement for decision management (quoting ISO/IEC/IEEE 15288), its description of the trade study as the method systems engineers most commonly employ, what a trade study/decision process produces, its roles (analyst, decision team, decision maker, stakeholders, SMEs), and its cognitive-bias cautions
Quotable: "Many systems engineering decisions are difficult because they include numerous stakeholders, multiple competing objectives, substantial uncertainty, and significant consequences."
Quotable: "“…to provide a structured, analytical framework for objectively identifying, characterizing and evaluating a set of alternatives for a decision at any point in the life cycle and select the most beneficial course of action.”( ISO/IEC/IEEE 15288 )"
Quotable: "The decision management method most commonly employed by systems engineers is the trade study."
Quotable: "To ensure the decision team fully understands the decision context, the analyst should describe the system baseline, boundaries and interfaces. The decision context includes: the system definition, the life cycle stage, decision milestones, a list of decision makers and stakeholders, and available resources."
Quotable: "The first step is to develop objectives and measures using interviews and focus groups with subject matter experts (SMEs) and stakeholders."
Quotable: "This is the point in the process where the decision analysis team identifies key observations about trade-offs and the important uncertainties and risks."
Quotable: "Research by (Kahneman 2011) and (Thaler and Sunstein 2008) has concluded that cognitive bias can seriously distort decisions made by any decision maker."
Quotable: "most decision makers are unaware of these biases"
Quotable: "The idea of independent review is that advice on decisions should come from an outside body, called by the Columbia Accident Investigation Board (CAIB) (NASA 2003, 227) as the Independent Technical Authority (ITA). This authority must be both organizationally and financially independent of the program in question."
Quotable: "Reports are important for historical traceability and future decisions. Take the time and effort to create a comprehensive, high-quality report detailing study findings and supporting rationale."
Quotable: "Trade studies aim to define, measure, and assess shareholder and stakeholder"
Quotable: "search for an alternative that represents the best balance of competing objectives"

**[3] ECSS Secretariat, ECSS-E-ST-10C Rev.1, Space engineering - System engineering general requirements, 15 February 2017.** standards. **fetched-and-verified.**
`https://ecss.nl/wp-content/uploads/2017/02/ECSS-E-ST-10C-Rev.1(15February2017).pdf`
Supports: A second named public systems-engineering body's trade-off requirements (clause 5.3.3) and normative Trade-off report DRD (Annex L): criteria/weighting, alternatives, evaluation table, sensitivity/robustness analysis, recommendation with conditions and risks, and who is responsible for the evaluation
Quotable: "The system engineering function shall conduct or consolidate trade-off analyses to: 1. assist in selecting system concepts, designs and solutions (including people, parts and materials availability);"
Quotable: "The system engineering function shall evaluate alternative concepts, designs and solutions against each other in a Trade-off report in conformance with Annex L."
Quotable: "The Trade-off report provides the system-engineering point of view on alternative design solutions, an evaluation and a classification of the alternative design solutions, and the justification of their ranking."
Quotable: "The trade-off report shall list the selected evaluation criteria and precise the justification for selecting those criteria, and provide the weighting of criteria and their justifications."
Quotable: "The trade-off report shall identify the entity responsible for the evaluation of the design solutions for any criteria, as well as the source and agreement regarding weighting factors (e.g. with management)."
Quotable: "The trade-off report shall present, in a table, the result of the evaluation per criteria."
Quotable: "Based on the proposed scheme for weighting the evaluation criteria, the trade-off report shall provide a classification of the different alternative design solutions."
Quotable: "The trade-off report shall provide the result of a sensitivity analysis of the criteria that provide advantage to the solution ranked first, e.g. when changing the weighting of the evaluation criteria."
Quotable: "The trade-off report shall recommend one solution and explain the reason for this choice (e.g. evaluation criteria where the selected solution take advantage), and precise the condition for the application of the recommended solution."
Quotable: "The trade-off report shall present the identified technical and programmatic risks induced by the choice of the recommended solution, and any additional activity necessary to be performed for risk mitigation."

### STRUCTURE: THE FHWA'S TRADE STUDY STEP AND OTHER PUBLISHED OUTLINES

**[4] Federal Highway Administration, Systems Engineering for ITS (SEITS), Section 3.4.5 'Conduct Trade Studies' (Process View).** standards. **fetched-and-verified.**
`https://ops.fhwa.dot.gov/seits/sections/section3/3_4_5.html`
Supports: Full step sequence of a trade study (Understand the objectives; Define criteria and weightings; Identify alternatives; Evaluate alternatives; Select and document the preferred candidate via a trade study matrix; Validate the choice), the 'Do Nothing' alternative, sensitivity analysis, the trade matrix, and the 'repository of alternatives' framing; also a six-item review checklist
Quotable: "Trade studies compare the relative merits of alternative approaches to ensure that the most cost-effective system is developed."
Quotable: "First, define the question the trade study is to answer."
Quotable: "Ideally, the criteria are developed early in the trade study process, before the alternatives are selected, to avoid subconsciously biasing the criteria to favor a pre-determined preferred alternative."
Quotable: "It is important to rank or weight the criteria so that the selected alternative scores best against the most important criteria."
Quotable: "These disparate evaluations are merged using the weighting factors to give a measure of overall effectiveness for each alternative."
Quotable: "Use the techniques of risk assessment to compare the alternatives relative to technical or project risk."
Quotable: "For complex trade studies with many alternatives, the overall evaluation may involve multiple passes where a limited set of criteria is applied to a broad set of alternatives in order to focus additional analysis on the most promising alternatives."
Quotable: "Sensitivity analysis may also be used, especially with simulation, to see the effect of changes in sub-system parameters on overall system performance. The sensitivity analysis and the evaluations may suggest other, better alternatives."
Quotable: "Select and document the preferred candidate, typically using a trade study matrix that lists the alternatives on one axis, the criteria on the second axis, and the relative scores of each alternative versus each criteria in the body of the matrix."
Quotable: "The trade study documentation should support review of the decision by stakeholders, so the trade matrix should be easily comprehensible to management and other stakeholders who may not be as familiar with the technical details."
Quotable: "The documented trade study is also a repository of alternatives in case a change is needed down the road."
Quotable: "Has a broad and reasonable selection of alternatives been examined?"
Quotable: "Was a fair and balanced set of criteria used to evaluate the alternatives?"
Quotable: "Is the selection rationale documented?"
Quotable: "Is the sensitivity of system effectiveness to changes in key parameters well understood?"
Quotable: "Have key stakeholders reviewed and support the trade study results?"
Quotable: "It is often good practice to include a"
Quotable: "alternative as the base case, depending on the nature of the trade study."
Quotable: "Be sure that all reasonable alternatives are on the table."

**[5] AcqNotes, 'Trade Study' (career-field / Systems Engineering entry).** practitioner. **fetched-and-verified.**
`https://acqnotes.com/acqnote/careerfields/trade-study`
Supports: A 9-step 'How to Conduct a Trade Study' sequence, an explicit list of what a trade study report should contain, and the formal-vs-informal tailoring guidance (lightest acceptable study)
Quotable: "A Trade Study is a decision-making study that identifies a preferred solution from a list of qualified solutions."
Quotable: "Define the problem - Make sure you address the actual problem, not a symptom."
Quotable: "Define constraints on the course of actions (solutions)."
Quotable: "Develop multiple courses of action (solutions) for the problem"
Quotable: "Define evaluation criteria - How will you judge each course of action"
Quotable: "Determine weight factors"
Quotable: "Define the normalization scale"
Quotable: "Conduct the actual trade study analysis - use a spreadsheet to keep track of your analysis"
Quotable: "Perform Ranking - Determine the best actions to take and rank them from best to worst"
Quotable: "Choose the appropriate Course of Action (solution)"
Quotable: "A tabular representation known as a trade study matrix assesses components according to different metrics or criteria."
Quotable: "The problem statement, objectives, criteria, alternatives, evaluation procedures, results, suggestions, assumptions, limitations, risks, and lessons learned should all be included in a trade study report."
Quotable: "Most trade studies are not strictly formal or informal; they usually fall between these two extremes. Generally, formal trade studies are indicated for high-value, high-risk, or other high-impact decisions."
Quotable: "Not all trade studies should follow the full rigor of a formal process but should be tailored to the specific circumstances of the program"

**[6] Defense Systems Management College (DSMC), Systems Engineering Fundamentals, Chapter 12 'Trade Studies' (DAU-lineage text; retrieved via METU OCW course mirror, lecture12.pdf).** standards. **fetched-and-verified.**
`https://ocw.metu.edu.tr/pluginfile.php/408/mod_resource/content/0/lecture12.pdf`
Supports: The classic DoD/DAU-lineage trade study process diagram and steps (problem statement; requirements/constraints; methodology and weighted criteria; select viable alternatives; measure performance; evaluate via trade-off/decision matrix; sensitivity analysis; select preferred alternative; document process and results), the utility-curve/weighting methodology and its known sensitivity, and explicit formal-vs-informal tailoring language
Quotable: "Trade Studies are a formal decision making methodology used by integrated teams to make choices and resolve conflicts during the systems engineering process."
Quotable: "Defining the problem entails developing a problem statement including any constraints. Problem definition should be done with extreme care."
Quotable: "Establishing the methodology includes choosing the mathematical method of comparison, developing and quantifying the criteria used for comparison, and determining weighting factors (if any)."
Quotable: "Evaluating the alternatives is the analysis part of the study. It includes the development of a trade-off matrix to compare the alternatives, performance of a sensitivity analysis, selection of a preferred alternative, and a re-evaluation (sanity check) of the alternatives and the study process."
Quotable: "Both formal and informal trade studies are conducted in any systems engineering activity. Formal trade studies tend to be those that will be used in formal decision forums, e.g., milestone decisions. These are typically well documented and become a part of the decision database normal to systems development."
Quotable: "Most of these less-formal studies are documented in summary detail only, but they are important in that they define the design as it evolves."
Quotable: "To ensure study viability, sensitivity analysis should always be done to examine the consequences of methodology choice."
Quotable: "the sensitivity analysis is crucial. If the solution can be changed with relatively minor changes in data input, the study is probably invalid"

**[7] U.S. Air Force Space & Missile Systems Center (SMC), SMC Systems Engineering Primer & Handbook, 4th ed. (29 Apr 2005) - Chapter 4 'Systems Analysis - the Trade Study Process' and Appendix C8 'Example Trade Study Outline'.** standards. **fetched-and-verified.**
`https://spacese.spacegrant.org/SEModules/Reference%20Docs/SMC_SE_Primer4-05.pdf`
Supports: A verbatim, named military-service trade study report outline (Purpose of Study; Scope of Study; Trade Study Description; Analytical Approach [candidates, performance models, selection criteria, scoring, weighting, Sensitivity Analysis]; Trades Results [requirements/architecture derivation, cost analysis results, risk analysis results]), plus narrative on INCOSE's and Buede's definitions of a trade study and DSMC's definition
Quotable: "Appendix C8-Example Trade Study Outline"
Quotable: "Selection Criteria -- risk, performance, and cost are usually at lease three of the factors to be studied"
Quotable: "Sensitivity Analysis"
Quotable: "The DSMC Systems Engineering Fundamentals describes a trade as a formal decision making methodology used by integrated teams to make choices and resolve conflicts during the systems engineering process."
Quotable: "the focus of trade studies is to perform objective trade comparisons of all reasonable alternatives and to choose the alternative that best balances performance, cost, schedule, and risk."
Quotable: "Example Trade Study Outline"
Quotable: "Purpose of Study"
Quotable: "State level of detail of study"
Quotable: "State Assumptions"
Quotable: "Identify Influencing requirements & constraints"
Quotable: "Measures of results to be compared to criteria"
Quotable: "Weighted reflecting their relative importance in the selection process"
Quotable: "Cost Analysis Results"
Quotable: "Risk Analysis Results"
Quotable: "explains the purpose of trade studies is to provide an objective foundation for the selection of one of two or more alternative approaches to solution of an engineering problem"

**[8] Microsoft, Code With Engineering Playbook - 'Trade Studies' overview and 'Trade Study Template' pages.** vendor. **fetched-and-verified.**
`https://microsoft.github.io/code-with-engineering-playbook/design/design-reviews/trade-studies/`
Supports: A complete, named-organization trade study report template outline (Overview, Desired Outcomes, Evaluation Criteria, Key Metrics, Constraints, Accessibility, Solution Hypotheses [per-solution: description, experiments, evidence], Results table, Decision, Next Steps), a 5-step 'flow of a trade study,' explicit screening-to-2-4-alternatives guidance, and explicit lightest-acceptable / when-to-skip guidance; Framing of when a trade study should be skipped in favor of a logged decision, and the recommendation to log the completed study into a separate Decision Log entry for later reference
Quotable: "Trade studies are a tool for selecting the best option out of several possible options for a given problem (for example: compute, storage)."
Quotable: "Trade studies should be avoided if there is a clear solution choice. Because they require each solution to be fully thought out, they have the potential to take a lot of time to complete. When there is a clear design, the trade study should be omitted, and an entry should be made in the Decision Log documenting the decision."
Quotable: "Solidify the requirements - Work with the stakeholders to agree on the requirements for the functionality that you are trying to build."
Quotable: "Create evaluation criteria - This is a set of qualitative and quantitative assessment points that represent the requirements."
Quotable: "Brainstorm solutions - Gather a list of possible solutions to the problem. Then, use your best judgement to pick the 2-4 solutions that seem most promising."
Quotable: "Evaluate shortlisted solutions - Dive deep into each solution and measure it against the evaluation criteria. In this stage, time box your research to avoid overly investing in any given area."
Quotable: "Trade studies should be avoided if there is a clear solution choice. Because they require each solution to be fully thought out, they have the potential to take a lot of time to complete."
Quotable: "Once the decision has been made we recommend adding an entry to the Decision Log that has references back to the full text of the trade study."
Quotable: "Trade studies should be avoided if there is a clear solution choice."
Quotable: "When there is a clear design, the trade study should be omitted, and an entry should be made in the Decision Log documenting the decision."
Quotable: "Once the decision has been made we recommend adding an entry to the Decision Log that has references back to the full text of the trade study"
Quotable: "time box your research to avoid overly investing in any given area"

**[9] Microsoft (Code-with-Engineering Playbook) - "Trade Study Template".** practitioner. **fetched-and-verified.**
`https://microsoft.github.io/code-with-engineering-playbook/design/design-reviews/trade-studies/template/`
Supports: Named decision-maker field; constraints and assumptions as explicit sections; evidence/experiments backing each solution's evaluation, including prototypes; an explicit statement that a decision can change as the team learns more
Quotable: "Conducted by: {Names of those that can answer follow-up questions and at least one email address}"
Quotable: "Decision Makers:"
Quotable: "Assumptions about the rest of the system"
Quotable: "Constraints that apply to the system, both business and technical"
Quotable: "Constraints (Optional) If applicable, describe the boundaries from which we have to design the solution."
Quotable: "Describe how the solution will be evaluated to prove or dis-prove that it will produce the desired outcomes. This could take many forms such as building a prototype and researching existing documentation and sample solutions."
Quotable: "Decisions should be made with the understanding that they can change as the team learns more. It's a starting point, not a contract."
Quotable: "The chosen solution, or a list of questions that need to be answered before the decision can be made. In the latter case, each question needs an action item and an assigned person for answering the question."
Quotable: "Present the evidence collected during experimentation that supports the hypothesis that this solution will meet the desired outcomes."

**[10] MITRE, 'The Trade Study Process' (PRS-21-0522).** practitioner. **not-retrieved.**
`https://www.mitre.org/sites/default/files/2021-11/prs-21-0522-the-trade-study-process.pdf`
Supports: Could not be used for any claim; both the cache check and a direct fetch attempt this pass returned Akamai/EdgeSuite 'Access Denied' (HTTP 403-equivalent block page), matching the earlier pass's failure

### METHODS: HOW CRITERIA ARE WEIGHTED AND OPTIONS SCORED

**[11] Kepner-Tregoe, "Think Clearly / Decision Making" solution page.** vendor. **fetched-and-verified.**
`https://kepner-tregoe.com/solution/think-clearly-decision-making/`
Supports: Confirms KT markets a named decision-analysis methodology and sells training/e-learning on it ("Intro to Decision Analysis", "Decision Analysis Refresher", "Decision Making for Leaders"); the page carries no methodological content on how KT weights criteria, scores options, distinguishes must/want, or checks robustness
Quotable: "Discover our all-rounder Kepner-Tregoe methodology course. Train your teams to plan, prioritize, problem solve, and make strategic, data-driven decisions."
Quotable: "The Kepner-Tregoe decision making framework helps you analyze your options strategically, replacing guesswork with confidence"
Quotable: "Intro to Decision Analysis"
Quotable: "Decision Analysis Refresher"

**[12] Wikipedia, "Decision-matrix method".** practitioner. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Decision-matrix_method`
Supports: Confirms the decision-matrix method is also called the Pugh method / Pugh concept selection; basic (unweighted, better/worse/same vs a reference design, not summed) vs weighted variants; sensitivity studies; and the specific warning that weighted scoring can let minor criteria outvote a must-have
Quotable: "A basic decision matrix consists of establishing a set of criteria and a group of potential candidate designs. One of these is a reference candidate design. The other designs are then compared to this reference design and being ranked as better, worse, or same based on each criterion. The number of times "better" and "worse" appeared for each design is then displayed, but not summed up."
Quotable: "A weighted decision matrix operates in the same way as the basic decision matrix but introduces the concept of weighting the criteria in order of importance. The more important the criterion the higher the weighting it should be given."
Quotable: "Another advantage of this method is that sensitivity studies can be performed. An example of this might be to see how much your opinion would have to change in order for a lower ranked alternative to outrank a competing alternative."
Quotable: "Scoring methods, even with weighting, tend to equalize all the requirements. But a few requirements are "must haves". If enough minor criteria are listed, it is possible for them to add up and select an option that misses a "must have" requirement."
Quotable: "The values assigned to each option are guesses, not based on any quantitative measurements."
Quotable: "is a qualitative technique used to rank the multi-dimensional options of an option set"
Quotable: "It is frequently used in engineering for making design decisions"

**[13] ASQ (American Society for Quality), "What is a Decision Matrix? Pugh, Problem, or Selection Grid".** practitioner. **fetched-and-verified.**
`https://asq.org/quality-resources/decision-matrix`
Supports: Full named procedure for choosing and weighting criteria (two explicit weighting methods: 10-point distribution, or per-member weights composited), three distinct scoring methods including a numbered Pugh variant, and the multiply-and-sum combination rule
Quotable: "A decision matrix evaluates and prioritizes a list of options and is a decision-making tool. The team first establishes a list of weighted criteria and then evaluates each option against those criteria."
Quotable: "Discuss and refine the list of criteria. Identify any criteria that must be included and any that must not be included."
Quotable: "Assign a relative weight to each criterion, based on how important that criterion is to the situation. This can be done in two ways: By distributing 10 points among the criteria, based on team discussion and consensus. By each member assigning weights, then the numbers for each criterion for a composite team weighting."
Quotable: "Method 1: Establish a rating scale for each criterion. Some options are: 1, 2, 3 (1 = slight extent, 2 = some extent, 3 = great extent) ... 1, 4, 9 (1 = low, 4 = moderate, 9 = high)"
Quotable: "Method 2: For each criterion, rank-order all options according to how well each meets the criterion. Number them with 1 being the option that is least desirable according to that criterion."
Quotable: "Method 3 (Pugh matrix): Establish a baseline, which may be one of the alternatives or the current product or service. For each criterion, rate each other alternative in comparison to the baseline, using scores of worse (-1), same (0), or better (+1). Finer rating scales can be used, such as 2, 1, 0, -1, -2 for a five-point scale or 3, 2, 1, 0, -1, -2, -3 for a seven-point scale."
Quotable: "Multiply each option's rating by the weight. Add the points for each option. The option with the highest score will not necessarily be the one to choose, but the relative scores can generate meaningful discussion and lead the team toward consensus"
Quotable: "If individuals on the team assign different ratings to the same criterion, discuss until the team arrives at a consensus. Do not average the ratings or vote for the most popular one."
Quotable: "In some versions of this tool, the sum of the unweighted scores is also calculated and both totals are studied for guidance toward a decision."

**[14] Department for Communities and Local Government (UK), "Multi-criteria analysis: a manual" (2009).** standards. **fetched-and-verified.**
`https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/7612/1132618.pdf`
Supports: The fullest treatment: the canonical 8-step MCA process, three scoring methods (value functions, direct rating, pairwise/AHP-family), the swing-weighting method as the modern standard for criteria weighting (distinguished from naive importance weighting), the conjunctive/disjunctive screening model as the formal name for a must-have vs want-criteria distinction, the additive combination rule, sensitivity analysis on weights and scores (including a real case closest to a do-nothing/status-quo alternative), and an explicit critique of AHP's pairwise weighting (rank reversal)
Quotable: "A full application of multi-criteria analysis normally involves eight steps."
Quotable: "1. Establish the decision context. What are the aims of the MCA, and who are the decision makers and other key players? 2. Identify the options. 3. Identify the objectives and criteria that reflect the value associated with the consequences of each option. 4. Describe the expected performance of each option against the criteria. (If the analysis is to include steps 5 and 6, also 'score' the options, i.e. assess the value associated with the consequences of each option.) 5. 'Weighting'. Assign weights for each of the criteria to reflect their relative importance to the decision. 6. Combine the weights and scores for each of the options to derive and overall value. 7. Examine the results. 8. Conduct a sensitivity analysis of the results to changes in scores or weights."
Quotable: "Most proponents of MCDA now use the method of 'swing weighting' to elicit weights for the criteria. This is based, once again, on comparisons of differences: how does the swing from 0 to 100 on one preference scale compare to the 0 to 100 swing on another scale?"
Quotable: "Thus, the weight on a criterion reflects both the range of difference of the options, and how much that difference matters. So it may well happen that a criterion which is widely seen as 'very important' - say safety - will have a similar or lower weight than another relatively lower priority criterion - say maintenance costs."
Quotable: "The second approach to scoring performance on an interval scale is direct rating. This is used when a commonly agreed scale of measurement for the criterion in question does not exist, or where there is not the time nor the resources to undertake the measurement. Direct rating uses the judgement of an expert simply to associate a number in the 0-100 range with the value of each option on that criterion."
Quotable: "The Analytic Hierarchy Process (AHP) also develops a linear additive model, but, in its standard format, uses procedures for deriving the weights and the scores achieved by alternatives which are based, respectively, on pairwise comparisons between criteria and between options."
Quotable: "On the other hand, serious doubts have been raised about the theoretical foundations of the AHP and about some of its properties. In particular, the rank reversal phenomenon has caused concern."
Quotable: "The conjunctive model eliminates options that fail to reach externally set levels of performance on each of one or more named criteria. For example, candidates to be short-listed for a job interview might be expected to have reached certain minimum levels of achievement on each of a number of the criteria used in the selection process."
Quotable: "If the external benchmarks are set independently and represent accepted reasons (e.g., a safety threshold) whereby an option that fails to 'pass' would not normally ever be considered for implementation, then this type of screening process is valid, although it is arguable that it scarcely needs formal MCA to make the judgement."
Quotable: "First, interest groups can be consulted to ensure that the MCDA model includes criteria that are of concern to all the stakeholders and key players. Second, interest groups often differ in their views of the relative importance of the criteria, and of some scores, though weights are often the subject of more disagreement than scores."
Quotable: "an organic option was a robust performer, whereas the status quo option of continuing intensive agriculture (without GM) often ranked poorly."
Quotable: "A third approach to scoring the value of options"
Quotable: "by eliciting from the decision maker a series of verbal pairwise assessments"

**[15] Umbrex, "Pugh Matrix" (consulting-firm resource page on decision-making frameworks).** vendor. **fetched-and-verified.**
`https://umbrex.com/resources/frameworks/decision-making-frameworks/pugh-matrix/`
Supports: Named Pugh-method source: the datum/baseline concept defined and explicitly tied to several candidate anchors including the status quo; the classic +/S/- scoring convention and the separateness of weighted numeric variants; sensitivity-to-datum caution; and a direct, attributable comparison to Kepner-Tregoe's must/want split, used here only to source the Umbrex characterization of KT, not KT's own text
Quotable: "Instead of trying to assign an absolute score to each alternative, it evaluates each option relative to a reference concept, often called the datum."
Quotable: "Then select the datum, which may be the current product, the status quo, the leading concept, or another reasonable reference point."
Quotable: "Symbol Meaning + Better than the datum on that criterion S Substantially the same as the datum - Worse than the datum on that criterion"
Quotable: "Many teams then total the number of pluses, sames, and minuses for each concept. Some also add criterion weights or convert symbols into numbers such as +1, 0, and -1."
Quotable: "It is sensitive to the datum. A poor or biased reference option can distort the entire comparison."
Quotable: "Use a sensible reference point and test whether conclusions change when the datum changes."
Quotable: "Kepner-Tregoe is typically more formal. It separates must-have requirements from wants, scores alternatives, and explicitly considers adverse consequences."

**[16] Wikipedia, "Analytic hierarchy process".** practitioner. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Analytic_hierarchy_process`
Supports: The named AHP (Saaty) source: pairwise-comparison derivation of weights and scores, priorities as numbers between 0 and 1 summing to 1 within a level, the consistency check step, and the rank-reversal critique (a second camp within AHP itself on whether rank reversal is acceptable)
Quotable: "the analytic hierarchy process (AHP) ... is a structured technique for organizing and analyzing complex decisions ... It was developed by Thomas L. Saaty in the 1970s"
Quotable: "Individual experts' experiences are utilized to estimate the relative magnitudes of factors through pair-wise comparisons. Each of the respondents compares the relative importance of each pair of items using a specially designed questionnaire."
Quotable: "A numerical weight or priority is derived for each element of the hierarchy, allowing diverse and often incommensurable elements to be compared to one another in a rational and consistent way."
Quotable: "Establish priorities among the elements of the hierarchy by making a series of judgments based on pairwise comparisons of the elements."
Quotable: "Check the consistency of the judgments."
Quotable: "priorities are absolute numbers between zero and one, without units or dimensions. A node with priority .200 has twice the weight in reaching the goal as one with priority .100"
Quotable: "There are two schools of thought about rank reversal. One maintains that new alternatives that introduce no additional attributes should not cause rank reversal under any circumstances. The other maintains that there are some situations in which rank reversal can reasonably be expected."
Quotable: "The current version of the AHP can accommodate both these schools-its ideal mode preserves rank, while its distributive mode allows the ranks to change."

### DEBATES: FALSE PRECISION, BIAS, RANK REVERSAL AND THE PREDETERMINED WINNER

**[17] Alex Bromage (Kepner-Tregoe Program Leader at Tetra Pak), "Decisions Decisions…", Kepner-Tregoe Blog (posted under Anna Szałkiewicz, March 2016).** practitioner. **fetched-and-verified.**
`https://kepner-tregoe.com/blogs/decisions-decisions`
Supports: Favoured option framed in; criteria chosen without measures; qualitative/non-transparent scoring rationalizing a wanted outcome; remedy of using measurable criteria and an independent third party when the analyst has a stake
Quotable: "I use it often, and I think its simplicity is the key to its popularity."
Quotable: "The most common pitfall-and this should be of no surprise to you if you have practiced a lot of KT-is the selection of decision objectives, the criteria for making the decision."
Quotable: "I could have said the process of scoring objectives is the greatest challenge, but the problems that I see users face with scoring are caused by setting poor objectives in the first place."
Quotable: "I'm going to score them on an agreed upon scale of 1 to 10 in discussion with my manager."
Quotable: "Lo and behold, the alternative selected based on the evaluation of the decision objectives ended up to be number 4! That was no surprise."
Quotable: "The guy doing the decision analysis came up with a non-quantitative analysis that supported the decision to promote him and give him his own team of people. Nothing fishy there at all!"
Quotable: "avoid exposing yourself to criticism in your analysis by selecting weak criteria that have only qualitative evaluation possibilities!"
Quotable: "The correct approach is to select transparent, measurable objectives that can use available data and that are applicable to the decision."
Quotable: "if you stand to benefit greatly from one of the possible outcomes of the decision, have an independent, third party lead the decision-making process."

**[18] Wikipedia contributors, "Rank reversals in decision-making", Wikipedia.** practitioner. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Rank_reversals_in_decision-making`
Supports: Rank reversal when an option is added/removed or replaced (a structural weighted-scoring failure); which methods are confirmed to exhibit it; the debate over whether rank reversal is always a defect
Quotable: "a rank reversal is a change in the rank ordering of the preferability of alternative possible decisions when, for example, the method of choosing changes or the set of other available alternatives changes"
Quotable: "Next a copy of a non-optimal alternative was introduced. When the 4 alternatives... were evaluated, and under the assumption that the criteria weights are exactly the same as before, it was observed that now the indication of the best alternative can change."
Quotable: "Another way is to replace a non-optimal alternative with a worse one and then see if the indication of the best alternative changes or not."
Quotable: "The issue of rank reversals has captured the interest of many researchers and practitioners in the field of decision-making. It is something that continues to be considered controversial by many and is frequently debated."
Quotable: "having rank reversals in certain occasions and of certain types may not be indicative to faulty decision making. However, the key question is how to be able to distinguish when rank reversals indicate that something is wrong or when they do not conflict rational decision making. This is a highly debated issue in the decision making community."
Quotable: "The analytic hierarchy process (AHP) and some of its variants."
Quotable: "The TOPSIS method."

**[19] Dame Athene Donald, "The ABC of panel scoring: Anchoring, Bias and Committee Procedures", Occam's Typewriter blog (2017-01-20).** practitioner. **fetched-and-verified.**
`https://occamstypewriter.org/athenedonald/2017/01/20/the-abc-of-panel-scoring-anchoring-bias-and-committee-procedures/`
Supports: Bias in group scoring: inconsistent use of the scale across scorers, anchoring on an initial figure/first speaker, order-of-presentation and dominant-speaker effects, expertise not evenly represented across scorers, and the remedy of structuring discussion order rather than scoring by sub-topic block
Quotable: "If asked to score between 1 and 10 against some criterion, some people will use the full range, but others will probably cluster scores between 4 and 8 believing nothing is perfection and nothing is completely worthless."
Quotable: "Rightly, these judgements should have more weight than those of a less expert panel member, but it will be random in each case whether such immediately relevant expertise is represented on the panel."
Quotable: "if there is someone who has a prior high opinion of one particular applicant, this may shine through regardless of the case on the table. If this person happens to talk first and is... a dogmatic character, a strongly positive message can be conveyed which later speakers find hard or are unwilling to challenge. Randomness in order of speaking may have a significant effect on what is ultimately a collective decision."
Quotable: "it is the phenomenon by which the introduction of an initial figure may have subsequent impact on how people score/react or choose to proceed... people use that as a baseline and tweak what they believe is appropriate around it rather than starting afresh themselves with an objective view."
Quotable: "if the scores submitted in advance by panel members are averaged and presented to the panel before detailed discussion starts, it might influence how the subsequent debate unwinds and hence the final scores which are awarded."
Quotable: "there is absolutely no doubt that peer review does not always end up with the right answers, be it down to anchoring, ignorance or incompetence."

**[20] Rick Kazman, Mario Barbacci, Mark Klein, S. Jeromy Carrière (Software Engineering Institute, Carnegie Mellon University), "Experience with Performing Architecture Tradeoff Analysis".** primary. **fetched-and-verified.**
`https://www.se.rit.edu/~se440/documents/atam_experience.pdf`
Supports: ATAM's own definitions of sensitivity point and trade-off point, and confirmation that an ATAM evaluation produces a written output (a report) rather than only a facilitated conversation
Quotable: "A sensitivity point for an attribute is defined as a parameter in the architecture to which some measurable attribute is highly correlated; small changes in such parameters are likely to have significant effects on the measurable behavior of the system."
Quotable: "We have identified three sensitivities in the BCS system, and two of these are affected by the same architectural parameter... These two parameters control the tradeoff point between the overall performance of the system... and... the availability of the system..."
Quotable: "a set of recommendations for improving the architecture in the light of the analysis findings"
Quotable: "a location of many changes and hence of high potential complexity"

**[21] European Services Strategy Unit (prepared for GMB and Unison), "Adult Social Care In-House Provider Services: Options Appraisal - Critique", London Borough of Barnet (2014-09).** practitioner. **fetched-and-verified.**
`https://www.european-services-strategy.org.uk/wp-content/uploads/2014/09/barnet-adult-services-option-appraisal.pdf`
Supports: A documented public-sector case where an options appraisal (the trade-study analogue in local-government procurement) was used to rationalize a direction already chosen: decide the preferred solution, hire a consultant to deliver that conclusion, run a superficial appraisal, then write the business case
Quotable: "The options appraisal process is flawed because it is operating to a predetermined agenda, it is not comprehensive, nor in sufficient detail to examine the impact and consequences of the options."
Quotable: "The choice of consultant to carry out the appraisal demonstrates poor judgement and undermines the integrity and independence of the options appraisal process and resulted in an inherent bias in the options appraisal from the beginning."
Quotable: "it was stated at the presentation in July that "the services were fit for transfer" yet the options appraisal does not provide sufficient analysis or evidence to justify this conclusion."
Quotable: "The paucity of information and analysis in the options appraisal would appear to justify trade union concerns on this issue."
Quotable: "Decide on a preferred solution or the"
Quotable: "Select a consultant who will deliver the"
Quotable: "This is a flawed process"

### THE GAP QUESTION: WHAT GOOD PRACTICE ADDS BEYOND THE COMMONEST SECTIONS

**[22] Dr. David G. Ullman and Brian P. Spiegel - "Trade Studies with Uncertain Information" (INCOSE 16th Annual International Symposium, 2006).** primary. **fetched-and-verified.**
`https://davidullman.com/_files/ugd/20f020_cccae7b8bc1544c29aa869e57f43183d.pdf`
Supports: Uncertainty ranges on individual scores, as a named supplement to the point-estimate scoring matrix, attributed to the FAA Systems Handbook and separately to an INCOSE paper (Felix 2004)
Quotable: "In the FAA Systems Handbook (FAA 2004) the decision analysis matrix (aka Pugh's method) is suggested to support the activities, but this method can not support uncertainty, a mix of quantitative and qualitative information, or teams. To manage uncertainty, the authors suggest supplementing point estimates of the outcome variables for each alternative with computed or estimated uncertainty ranges."
Quotable: "The Standard Approach to Trade Studies (Felix 2004), an INCOSE paper from 2004 suggests a similar approach."
Quotable: "A trade study is the activity of a multidisciplinary team to identify the most balanced technical solutions among a set of proposed viable solutions (FAA 2004)."

**[23] mechanicalc.com - "Trade Study" reference page.** practitioner. **fetched-and-verified.**
`https://mechanicalc.com/reference/trade-study`
Supports: A worked definition of what each point on a qualitative scoring scale means, and a stated warning that an undisclosed weighting/rating choice injects bias
Quotable: "For a criteria such as safety, a numerical value may not be known, and instead only a general qualitative feel for how well each alternative performs is known. In this case, a rating value can be assigned to the alternative based on a scale of 1-5, where 1 is very poor and 5 is excellent."
Quotable: "A trade study is only as objective as you make it. Any biases that you have when setting weightings for the criteria or when rating the performance of the alternatives will be reflected in the results, so the results of the trade study should not be taken as absolute."

**[24] Paula J. Baker (NASA IV&V Facility / TASC, Inc.) and James T. Whalen (Stevens Institute of Technology) - "Survey of Trade Study Methods for Practical Decision-Making" (conference poster).** primary. **fetched-and-verified.**
`https://www.nasa.gov/wp-content/uploads/2016/10/survey_of_trade_study_methods_-_baker.pdf`
Supports: Traceability and repeatability of the decision-making process as the stated reason to document a trade study, and a worked example in which each alternative is screened Yes/No against named must-have constraints before any weighted scoring of the remaining 'wants' criteria
Quotable: "Trade studies are decision-making activities used to identify the most acceptable technical solution among a set of proposed solutions. By nature, all decisions are subjective and involve risks. Trade studies provide an effective means for addressing this by documenting the decision-making process to enable traceability and repeatability."

**[25] RAND Corporation - "Analysis of Alternatives: Keys to Success" (presented at the NPS Annual Acquisition Research Symposium, May 2012).** practitioner. **fetched-and-verified.**
`https://dair.nps.edu/bitstream/123456789/1396/1/SYM-AM-12-125.pdf`
Supports: Cost and life-cycle cost kept as a distinct analytical view from the effectiveness/performance scoring, shown as a separate relative-effectiveness-versus-relative-cost chart and as a separate estimation task; and an oversight steering group that formally approves interim study-director decisions, including the final set of alternatives
Quotable: "Measuring the cost and benefits of each alternative"
Quotable: "Task 4: Perform effectiveness analysis"
Quotable: "Task 5: Estimate life cycle costs"
Quotable: "Approve study director decisions as work progresses (e.g. final set of alternatives)"

### THE WORKED EXAMPLE'S DOMAIN: STREAMING INGESTION OPTIONS

**[26] Apache Kafka 4.2 documentation, Design - Replication (Apache Software Foundation).** primary. **fetched-and-verified.**
`https://kafka.apache.org/42/design/design/`
Supports: Kafka replication model, acks semantics, min.insync.replicas, durability guarantee under node/follower failure
Quotable: "you can set this replication factor on a topic-by-topic basis"
Quotable: "Under non-failure conditions, each partition in Kafka has a single leader and zero or more followers."
Quotable: "All writes go to the leader of the partition, and reads can go to the leader or the followers of the partition."
Quotable: "The leader keeps track of the set of "in sync" replicas, which is known as the ISR."
Quotable: "wait for the message to be acknowledged by 0,1 or all (-1) replicas"
Quotable: "committed asynchronously across the set of in-sync replicas if acks=0"
Quotable: "synchronously only on the leader if acks=1"
Quotable: "topics have a setting for the minimum number of in-sync replicas (min.insync.replicas)"
Quotable: "if a follower dies, then the controller will notice the failure through the loss of its session"
Quotable: "Only committed messages are ever given out to the consumer."
Quotable: "a committed message will not be lost, as long as there is at least one in sync replica alive, at all times."
Quotable: "Kafka will remain available in the presence of node failures after a short fail-over period"
Quotable: "have the option of either waiting for the message to be committed or not, depending on their preference for tradeoff between latency and durability"
Quotable: "This preference is controlled by the acks setting that the producer uses."

**[27] AWS Kinesis Data Streams Developer Guide - Terminology and concepts / Introduction (Amazon Web Services).** primary. **fetched-and-verified.**
`https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html`
Supports: Kinesis retention period, shard as the scaling unit and its fixed throughput, on-demand vs provisioned capacity, put-to-get latency, managed-service framing
Quotable: "A stream's retention period is set to a default of 24 hours after creation. You can increase the retention period up to 8760 hours (365 days) using the IncreaseStreamRetentionPeriod operation, and decrease the retention period down to a minimum of 24 hours using the DecreaseStreamRetentionPeriod operation. Additional charges apply for streams with a retention period set to more than 24 hours."
Quotable: "A shard is a uniquely identified sequence of data records in a stream. A stream is composed of one or more shards, each of which provides a fixed unit of capacity. Each shard can support up to 5 transactions per second for reads, up to a maximum total data read rate of 2 MB per second and up to 1,000 records per second for writes, up to a maximum total data write rate of 1 MB per second (including partition keys)."
Quotable: "With the on-demand mode, Kinesis Data Streams automatically manages the shards in order to provide the necessary throughput... With the provisioned mode, you must specify the number of shards for the data stream."
Quotable: "The producers continually push data to Kinesis Data Streams, and the consumers process the data in real time."

**[28] Amazon MSK Developer Guide - What is Amazon MSK / MSK Express brokers / MSK Serverless / Create an MSK Provisioned cluster (Amazon Web Services).** primary. **fetched-and-verified.**
`https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html`
Supports: What MSK operates for the customer (control plane, ZooKeeper/KRaft, broker failure detection and replacement) versus self-managed Kafka; MSK Express broker and MSK Serverless scaling and operational-burden claims; multi-AZ broker placement
Quotable: "Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service that enables you to build and run applications that use Apache Kafka to process streaming data. Amazon MSK provides the control-plane operations, such as those for creating, updating, and deleting clusters."
Quotable: "Broker nodes - When creating an Amazon MSK cluster, you specify how many broker nodes you want Amazon MSK to create in each Availability Zone. The minimum is one broker per Availability Zone."
Quotable: "ZooKeeper nodes - Amazon MSK also creates the Apache ZooKeeper nodes for you."
Quotable: "KRaft controllers -...KRaft controllers are included at no additional cost to you, and require no additional setup or management from you."
Quotable: "Amazon MSK detects and automatically recovers from the most common failure scenarios for clusters so that your producer and consumer applications can continue their write and read operations with minimal impact. When Amazon MSK detects a broker failure, it mitigates the failure or replaces the unhealthy or unreachable broker with a new one."
Quotable: "The minimum is one broker per Availability Zone."
Quotable: "MSK manages the broker nodes used to handle your traffic"
Quotable: "Run Apache Kafka without having to manage and scale cluster capacity with MSK Serverless"

**[29] RabbitMQ documentation - Streams (VMware/Broadcom, the RabbitMQ project).** primary. **fetched-and-verified.**
`https://www.rabbitmq.com/docs/streams`
Supports: RabbitMQ Streams persistence/replication model, what delivery guarantee actually requires (publisher confirms), what the operator must manage (replica placement, quorum, disk), and the "off by default" durability trap (no fsync)
Quotable: "Streams are always persistent and replicated."
Quotable: "Streams always store data on disk, however, they do not explicitly flush (fsync) the data from the operating system page cache"
Quotable: "publisher confirms are only issued once the data has been replicated to a quorum of stream replicas."
Quotable: "an uncontrolled shutdown of a server could result in data loss for replicas hosted on that node."
Quotable: "No guarantees are provided for messages that have not been confirmed using the publisher confirm mechanism"
Quotable: "which makes a read-process-write loop effectively-once (what other systems call exactly-once)"
Quotable: "the log will grow indefinitely until the disk runs out"
Quotable: "Replicas of a stream are explicitly managed by the operator."
Quotable: "it must be explicitly removed from the replica list of all streams it currently hosts replicas for."
Quotable: "A stream requires a quorum of the declared nodes to be available to function."
Quotable: "Care needs to be taken not to accidentally make a stream unavailable by losing the quorum."

**[30] NATS documentation - NATS Concepts: JetStream (The NATS.io / CNCF project).** primary. **fetched-and-verified.**
`https://docs.nats.io/nats-concepts/jetstream`
Supports: JetStream's delivery semantics (at-least-once, not exactly-once) and the contrast with Core NATS's at-most-once default
Quotable: "JetStream adds a persistence layer on top, giving you at-least-once delivery"
Quotable: "Core NATS delivers messages only to subscribers connected at the moment of publication - at most once"
Quotable: "if a message isn't acknowledged in time, the server redelivers it, which is what gives you at-least-once delivery."

**[31] Google Cloud Pub/Sub documentation - Exactly-once delivery / Overview (Google LLC).** primary. **fetched-and-verified.**
`https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery`
Supports: Pub/Sub's exactly-once feature and its real-world limits (pull-only, same-region-only, publish-side duplicates still possible) - the trap where a criterion like "delivery semantics: exactly-once" is misleading without these caveats
Quotable: "This page explains how to receive and acknowledge messages using Pub/Sub's exactly-once feature"
Quotable: "which makes it possible for you to track and prevent duplicate processing of messages."
Quotable: "Only the pull subscription type supports exactly-once delivery."
Quotable: "The exactly-once delivery guarantee only applies when subscribers connect to the service in the same region."
Quotable: "can lead to duplicate message delivery, even when exactly-once delivery is enabled."
Quotable: "A subscription might receive multiple copies of the same message due to publish side duplicates,"
Quotable: "the acknowledgment failures can lead to silent re-deliveries of messages."
Quotable: "No redelivery occurs after the message is successfully acknowledged."
Quotable: "Subscribers can determine if message acknowledgments were successful."
