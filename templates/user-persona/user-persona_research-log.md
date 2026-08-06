# user-persona research log

Researched 2026-08-05 across six parallel dimensions: origins and canonical definition, structure in
practice, evidence grounding and the proto-persona, the case against personas, the product-management
context, and boundaries and adjacent artifacts. **45 sources**, of which **33 fetched-and-verified** and
**12 not-retrieved**. Retrieval status is recorded per source in the three-token vocabulary the library
gates ([ADR 0029 (the research-log contract gate)](../../docs/internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md)),
and only `fetched-and-verified` sources are quoted.

**How to read this log.** A `Supports:` clause says what the bundle is allowed to rest on that source for.
A `Quotable:` phrase was read verbatim on the page. If a claim in the companion is not covered by some
entry's `Supports:` clause here, the claim has no home and must be cut, not justified after the fact.

**The tier mix is itself a finding.** Of the 33 sources read in full, **20 are practitioner and 7 vendor**,
leaving 3 primary, 2 academic and 1 standards. This is not a gap in the search. The persona is a
practitioner artifact whose canon is thin: **only two peer-reviewed papers could be read**, and they do
different jobs, one extending the method [3] and one arguing that it cannot be tested at all [19]. The 2021
review that assessed the evidence base was read only through a project-authored summary [20], **not the
paper itself**. A reader should know that the confident-sounding persona literature is overwhelmingly
written by people publishing a template, a tool or a course.

**The three books at the centre of this type could not be read.** *The Inmates Are Running the Asylum*
chapter 9, *About Face*, and Pruitt and Adlin's *The Persona Lifecycle* are the works a reader would most
expect this bundle to cite, and none was reachable as full text [34][35][36]. **Nothing in this bundle
states what those books say.** What is recorded about Cooper's original claim comes from Cooper's own later
essays [1][2] and from a contemporaneous academic paper that quotes the 1999 book directly [3]. The
publisher's free sample of *Inmates* was read, but it stops at front matter: its chapter 9 section titles
come from the table of contents and **not from chapter prose**, and are recorded that way [4].

---

## Honest framing: the seven things this bundle has to say

**1. Cooper invented the persona to narrow focus, and then disowned control of it.** His own account is that
interviews produced three clusters and he built three named archetypes: "So I created Chuck, Cynthia, and
Rob. These three were the first true, Goal-Directed, personas" [1]. The purpose was to let a design be
argued from their points of view rather than from his own [1]. He is
explicit that the point was restriction: "we tightly restricted the number of personas we used" [2]. He is
equally explicit that he never owned the term and no longer defines it: "I can't put them in a box and sell
them. From the very beginning I gave them away by telling the world about them", and "That community owns
and is responsible for the tools of their trade, and they must assure their definition" [2]. **A bundle
appealing to Cooper's authority for current practice is appealing to an authority its holder formally
declined.**

**2. The split between persona-as-research and persona-as-focusing-device is original, not modern.** Pruitt and Grudin, writing from Microsoft in 2003, set out their extension of Cooper's method and
name the difference plainly: Cooper's rested on a lighter "initial investigation phase", and they quote him
dismissing heavier ongoing research as "Seems like sandpaper... Very expensive and time-consuming, it wasn't
solving the fundamental problem" [3]. Their own position is the opposite: persona use "needs to be
complemented with a strong, ongoing effort to obtain as much quantitative and qualitative information about
users as possible" [3]. Cooper later characterised the Microsoft lineage far less kindly: "At Microsoft,
they invented personas to defend the features that the engineers cooked up in their ivory towers", and "they
had hundreds of personas, one for each feature they wanted to inflict on their users" [2]. **Both camps are
named and sourced, and this bundle presents the disagreement rather than settling it.**

**3. The strongest academic critique is not that personas fail, it is that they cannot be tested.** Chapman
and Milham's peer-reviewed 2006 paper argues personas are "outside the scientific method and cannot be
verified" because "no data can disprove a fictional construction", and that "there is essentially no way to
generalize from a well-specified persona to a population of interest"
[19]. Their conclusion is stated as an evidence gap rather than a disproof: "There have been no adequate
studies addressing the reliability, validity, or utility of the method" [19]. **That is a different and more
serious claim than a warning that personas sometimes go wrong, and flattening it into the practitioner
critique would misrepresent the source.**

**4. The curse of dimensionality is the sharpest thing this research found, and it is a design rule.** The
same paper shows a persona's population coverage shrinks combinatorially as attributes accumulate, and works
a 21-attribute example through to roughly 134 people in the United States [19]. **Every field a template
adds makes the persona describe fewer real people.** That turns an abstract warning into a concrete
instruction: the document is short because length is not free, and each attribute earns its place by
changing a decision.

**5. The famous persona statistic traces to one uncontrolled case study, and this research followed it
home.** The circulated 900 percent website-visit-duration increase and its companion revenue figure
resolve to a single MarketingSherpa case study of one company, which bundled persona work with a full site
redesign, a content overhaul and an email-automation change, **with no comparison group and no isolation of
the persona variable** [22]. The source was read; the number is real; it supports nothing about personas.
**This is the contrast worth teaching:** where `business-case` had to quarantine its famous statistics
unread, here the statistic was retrieved and is disqualified on its own published method.

**6. The evidence base is uneven rather than absent, and one study measured the unevenness.** Salminen and
colleagues extracted 130 knowledge claims from 346 persona research articles and report "a higher degree of
consensus" on what a persona *is* against "a high proportion of unverified claims" in the creation and use
categories, concluding that the field carries "claims that are not substantiated with strong empirical
evidence and warrant future work" [20]. **This was read from a project-authored summary and not
from the primary publication**, which the entry records and which limits what may rest on it. The companion
2022 systematic review could not be retrieved at all [37].

**7. Product-management literature is split four ways, and the split is the teaching point.** Klement argues
for replacement rather than repair, on the ground that filling persona gaps with invention is
"disinformation" [23]. Nielsen Norman Group names and rebuts that position: "Despite many contrary voices
suggesting that JTBD can entirely replace personas, the two are in fact, quite compatible" [24]. Cagan's
SVPG publishes a persona how-to with **no argument for or against the method at all**, which is unexamined
use rather than endorsement [27]. And Teresa Torres's canonical account of the opportunity solution tree,
the structural core of continuous discovery, **never mentions personas** [25]. That last is an absence
observed in a document that was read, not an inference about her views, and it is stated that way. **This
differs from `business-case`, where the product literature was hostile or silent. Here it disagrees with
itself, and a reader is owed the disagreement rather than a verdict.**

**And one number that is real, numeric, and disclaimed by its own publisher.** Nielsen Norman Group names
three tiers by evidence level: proto-personas built with "no new research" in a two to four hour workshop;
qualitative personas "based on small-sample qualitative research", with 5 to 30 interviews; and statistical
personas needing "at least 100 (ideally 500 or more) respondents" analysed by clustering [15]. A companion
piece from the same publisher warns "Unfortunately, there isn't a golden number" and pushes back on the
five-per-persona heuristic [16]. **Both are Nielsen Norman Group.** The bundle teaches the ladder as the
useful thing it is, and records that its own publisher declines to make the numbers a law.

---

## Format verdict (ADR 0028)

Under [ADR 0028 (the format-axis rule)](../../docs/internal/decisions/0028-adopt-a-format-axis.md) a format
ships only when it is **structurally distinct** and **in circulation with a named source**. Four candidates
were considered against the six published formats read in full.

| Candidate | Structurally distinct? | Named source in circulation? | Verdict |
|---|---|---|---|
| **Profile-led persona** (identity, goals, pains, context) | This is the baseline shape | Yes, and near-universal: 5 of the 6 formats read carry it [5][6][7][8] | **Ships** as the default format |
| **Proto-persona** | No. Same document shape; what differs is the **evidence behind it**, not the sections | Yes [12][14] | **Rejected as a format.** It is an evidence tier, taught in the companion and carried as a declared field, not a second outline |
| **Buyer persona / 5 Rings of Buying Insight** | **Yes, genuinely.** Priority Initiatives, Success Factors, Perceived Barriers, Buyer's Journey and Decision Criteria replace the profile spine outright [9] | Yes, Buyer Persona Institute [9][29] | **Rejected as out of scope.** A **different artifact for a different question**, the purchase decision rather than product use. The bundle teaches the boundary instead of shipping it |
| **Anti-persona** | Yes, and the one source that addresses its packaging publishes it as a **separate document** [10] | Yes [10][32] | **Not a format and not a section.** See below |

**The build spec is wrong about the anti-persona on the evidence available, and this bundle departs from
it.** The spec proposes that `full` adds an Anti-persona section. Two sources address anti-personas
directly [10][32]; the one that speaks to packaging builds and publishes it as a separate artifact with its
own data, "created data-based just like a buyer persona, only 'the other way around'" [10]. Neither presents
it as a section inside a persona. Folding it in would teach a shape no read source practises, so the bundle
names the anti-persona in the companion's Relationships section as a sibling document a team may choose to
write. **This is a departure on one source's packaging evidence, not a refutation, and it is recorded in the
contested register so a later pass can reopen it.**

**Two further spec departures, on the same kind of evidence.** A section labelled "Behaviors" appears in
**none** of the six formats read. The nearest is the service manual's Behaviour and preferences block [5];
elsewhere behaviour is folded into Usage Context [6] or Situations [8], and no format gives it a standalone
heading under the spec's own wording. A bounded "Quotes/Evidence" section appears in **none** of them, except where verbatim buyer
voice is the entire spine [9]. The section design therefore follows the core the sources actually share,
and the two spec sections no published format carries are not invented to satisfy the spec. The catalog's
section calls are hypotheses rather than facts, which is finding EC-2 in [`STATE.md`](../../STATE.md) and has
already changed two `qa-docs` members.

**So one format ships**, with `lean` and `full` weights on it.

---

## Sources

### Origins and canonical definition

**[1] Alan Cooper, "The Origin of Personas," The Cooper Journal (2008), reproduced/quoted at Tim Strehle's Blog.** primary. **fetched-and-verified.**
`https://www.strehle.de/tim/weblog/archives/2003/10/20/197/`
Supports: Cooper's own first-person account of inventing personas: he interviewed software users, found they fell into three distinct groups differentiated by goals, tasks, and skill level, and built three named archetypes (Chuck, Cynthia, Rob) to represent them. The stated original purpose was to give a design team a shared, specific reference point instead of designing from the designer's own point of view or from a vague averaged 'user.'
Quotable: "So I created Chuck, Cynthia, and Rob. These three were the first true, Goal-Directed, personas." / "a clear pattern emerged after just a few interviews"

**[2] Alan Cooper, "Defending Personas," Medium (mralancooper).** primary. **fetched-and-verified.**
`https://mralancooper.medium.com/defending-personas-2657fe26dd0f`
Supports: Cooper's own later statement of what a persona is for, who is meant to own the concept once published, and his explicit contrast between his original intent (field-research-derived, tightly restricted in number, used to focus design) and what he calls the corrupted Microsoft variant (large proliferating sets used to defend engineer-driven features). Also his explicit renunciation of control over the term.
Quotable: "At Cooper, we did our field research and then synthesized personas as a tool for understanding and communicating the goals, motivations, and desired end-states of our real-world users." / "At Cooper, we knew that narrowing the focus was the key to good design, so we tightly restricted the number of personas we used." / "At Microsoft, they invented personas to defend the features that the engineers cooked up in their ivory towers." / "At Microsoft, they had hundreds of personas, one for each feature they wanted to inflict on their users." / "I can't put them in a box and sell them. From the very beginning I gave them away by telling the world about them." / "My defense of them is seen simply as one man's opinion. Defending their 'proper' usage is a quixotic battle." / "That community owns and is responsible for the tools of their trade, and they must assure their definition."

**[3] John Pruitt and Jonathan Grudin (Microsoft), "Personas: Practice and Theory," Proceedings of DUX 2003 (Designing for User Experiences), Microsoft Research.** academic. **fetched-and-verified.**
`https://www.microsoft.com/en-us/research/wp-content/uploads/2017/03/pruitt-grudinold.pdf`
Supports: A contemporaneous, non-Cooper peer-reviewed conference paper (co-authored by Pruitt, later co-author of The Persona Lifecycle with Tamara Adlin, who appears here only in the acknowledgments, not as co-author) that explicitly separates what Cooper originally claimed from what Microsoft's practitioners added on top. It documents that Cooper's persona was originally a single-designer discussion tool ('Would Dave use this feature?'), built from a lighter 'initial investigation phase' that Cooper himself said could be skipped, used primarily to justify design decisions to clients and engineers, and explicitly de-emphasized ongoing quantitative/qualitative data collection. Microsoft's extension -- foundation documents, cross-discipline distribution to marketers/testers/writers, weighted feature-priority matrices, persona user panels, posters, an actual company email address per persona -- is presented by the authors as their own addition, explicitly contrasted with Cooper.
Quotable: "we and our colleagues have extended Cooper's technique to make Personas a powerful complement to other usability methods" / "His 'goal-directed design' provides focus through the creation of fictional Personas whose goals form the basis for scenario creation. Cooper's early Personas were rough sketches, but over time Cooper's method evolved to include interviews or ethnography to create more detailed characters." / "He emphasizes an 'initial investigation phase' and downplays ongoing data collection and usability engineering: 'Seems like sandpaper... Very expensive and time-consuming, it wasn't solving the fundamental problem.'" / "Personas as used by Cooper can be valuable, but they can be more powerful if used to complement, not replace, a full range of quantitative and qualitative usability methods." / "Cooper describes Persona use mostly as a discussion tool. 'Would Dave use this feature?'" / "Unlike Cooper, we feel strongly that Persona use needs to be complemented with a strong, ongoing effort to obtain as much quantitative and qualitative information about users as possible, to improve the selection, enrichment, and evolution of sets of Personas." / "Cooper argues that designing for any one external person is better than trying to design vaguely for everyone or specifically for oneself." / "Cooper offers no explanation for why it is better to develop Personas before scenarios." / "all things being equal, I will use people of different races, genders, nationalities, and colors"

**[4] Alan Cooper, The Inmates Are Running the Asylum (2004 2nd ed., Sams Publishing) -- publisher-issued free sample chapter PDF (front matter: Foreword to the Original Edition, 2004 Foreword, Table of Contents through Part IV).** primary. **fetched-and-verified.**
`https://ptgmedia.pearsoncmg.com/images/9780672326141/samplepages/0672326140.pdf`
Supports: Confirms the book's own stated framing and genesis (a deliberately business-case-first book, not a how-to design book, written to convince executives of interaction design's value) and locates the persona material precisely: Part IV, Chapter 9 ('Personas,' book pages 123-148), with subsections including 'Design for Just One Person,' 'The Elastic User,' 'Be Specific,' 'Hypothetical,' 'Precision, Not Accuracy,' 'Personas End Feature Debates,' and 'It's a User Persona, Not a Buyer Persona.' The sample excerpt stops at front matter and does not include Chapter 9's body text, so no direct persona-definition quote could be verified from this file; the section titles above are from the table of contents only, not chapter prose.
Quotable: "The point of this book is uncomplicated: We can create powerful and pleasurable software-based products by the simple expedient of designing our computer-based products before we build them."

### Structure in practice

**[5] Office for National Statistics (GOV.UK-derived) Service Manual - "Understanding your users: User personas".** standards. **fetched-and-verified.**
`https://service-manual.ons.gov.uk/content/writing-for-users/user-personas`
Supports: A government service-manual persona document format: ordered section list plus the practice of dating and periodically reviewing personas.
Quotable: "I want to find unbiased information so that I can verify the key points..."

**[6] Nielsen Norman Group - "Personas" (nngroup.com).** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/persona/`
Supports: Baseline claim that personas must rest on user research, not invention; lists research methods and the elements a persona carries, including attached quotes
Quotable: "Personas must be based on user research to accurately represent a product's users." / "Quotes to sum up the persona's attitude"
Contested/time-bound: claimed by 2 research dimensions; one entry kept, carrying the fuller extract.

**[7] Atlassian - "Persona" Confluence template (PDF).** vendor. **fetched-and-verified.**
`https://www.atlassian.com/dam/jcr:ba94bcb7-5e63-4457-9460-6d0212ae81e1/Persona.pdf`
Supports: A tool vendor's documented, ready-made persona template with an exact field order, useful as a B2B/enterprise counterpoint to UX-agency templates.
Quotable: "Persona name:" / "Persona role:" / "Job description:" / "Persona quote" / "Add a quote from an actual customer who resembles the persona you're building" / "Biography" / "Professional goals" / "Motivatiors" / "Challenges" / "Sources of information"

**[8] Interaction Design Foundation - "Persona Template" (PDF), attributing the base model to Aurora Harley/NN Group.** practitioner. **fetched-and-verified.**
`https://public-media.interaction-design.org/pdf/Persona-Template.pdf`
Supports: An established design-education publisher's fillable template with a full ordered field list, plus a worked example (Rebecca/Spotify) showing how the fields get laid out on a real one-pager.
Quotable: "Name, age, gender, and an image of the persona, preferably including some context in the background" / "A tag line, indicating what the persona does or considers relevant in his or her life" / "Any goals, attitudes, and concerns they would have when using your product or service" / "Quotes or a brief scenario, which indicate the persona's attitude toward the product or service you're designing" / "Background" / "Emotions and attitudes" / "Personal traits" / "Needs" / "Situations" / "Scenarios" / "Create some scenarios that show how the person manages to solve their needs in a new way, using your product. The scenario should have a beginning (presents the user and what the persona wants to achieve), middle (what the user does with your product and the persona's motivation for pursuing the goal) and end (describes whether the persona succeeds in his or her intentions)."

**[9] Buyer Persona Institute (Adele Revella) - "The Buyer Persona Manifesto", 2nd edition (PDF).** practitioner. **fetched-and-verified.**
`https://www.buyerpersona.com/wp-content/uploads/2016/02/Buyer-Persona-Manifesto-2016.pdf`
Supports: A named, established practitioner methodology (B2B marketing lineage, distinct from UX personas) whose persona content structure is the "5 Rings of Buying Insight," evidence that some influential formats reject a demographic/bio-first structure entirely.
Quotable: "Where the Buyer Persona Profile creates a composite picture of the person you need to reach, the 5 Rings of Buying Insight reveal the buying decision you need to influence" / "Priority Initiatives" / "Success Factors" / "Perceived Barriers" / "The Buyer's Journey" / "Decision Criteria" / "Sure, it's great to have a picture of your buyer. But pictures don't talk, and it's her voice that you need." / "When you write up the results, quote the buyer directly."

**[10] Persona Institut (German UX/marketing consultancy) - "Anti-Personas" page.** vendor. **fetched-and-verified.**
`https://www.persona-institut.de/en/anti-personas/`
Supports: Direct evidence against treating anti-persona as a section within the main persona document: this publisher treats it as a separate artifact.
Quotable: "An antipersona is created data-based just like a buyer persona, only 'the other way around': collect data and facts regarding the 'undesired' customers."

### Evidence grounding and the proto-persona

**[11] Steve Mulder, interviewed in "Long Live the User (Persona): Talking with Steve Mulder" - Boxes and Arrows.** practitioner. **fetched-and-verified.**
`https://boxesandarrows.com/long-live-the-user-persona-talking-with-steve-mulder/`
Supports: States a practical floor for evidence quality (a dozen qualitative interviews alone is thin for high-stakes business decisions in some orgs), gives a fallback minimum bar when primary research is impossible, and defines what a persona's data should be built from (goals, behaviors, attitudes, not superficial trivia)
Quotable: "Talking to a dozen users and making critical business decisions based solely on that qualitative research just doesn't cut it within some organizations." / "personas based on no research are better than no personas at all"

**[12] Jeff Gothelf, "Using Personas for Executive Alignment" (jeffgothelf.com blog).** practitioner. **fetched-and-verified.**
`https://jeffgothelf.com/blog/using-personas-for-executive-alignment/`
Supports: Gothelf's own account of the proto-persona exercise: personas built from what executives believed about customers, explicitly NOT research-proven, plus his statement that the UX team is responsible for continuously updating the proto-personas against real user interactions and reporting the deltas back to executives
Quotable: "These were not going to be research-proven customer archetypes." / "reference points which the team can use as filters" / "continue to update the 6 personas we created as we learn more from actual user interactions. We must then update the executives with these new details."

**[13] Jeff Gothelf and Josh Seiden's proto-persona formats, summarized at insideproduct.co ("Personas").** practitioner. **fetched-and-verified.**
`https://insideproduct.co/personas/`
Supports: Confirms Gothelf and Seiden proposed two proto-persona layouts (four-box and three-box); page's own prose was too sparse to yield a verbatim definition or an assumptions-vs-research contrast, so no claim rests on this source alone beyond the format naming, which the Open Practice Library entry corroborates independently

**[14] Open Practice Library - "Proto-Persona" practice entry.** practitioner. **fetched-and-verified.**
`https://openpracticelibrary.com/practice/proto-persona/`
Supports: Independent definition of proto-persona as assumption-built, and its explicit statement that a proto-persona must be updated as new evidence (surveys, usability tests, interviews) arrives, i.e. the assumption-first / evidence-later lifecycle
Quotable: "A proto-persona is a description of the target users and audience of a product based on the assumptions of stakeholders." / "the persona should be updated with any new information or analysis gained during the course of the project" / "constantly comparing preexisting assumptions to new facts and discoveries"

**[15] Nielsen Norman Group - "3 Persona Types: Lightweight, Qualitative, and Statistical".** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/persona-types/`
Supports: The single most load-bearing source for a stated minimum evidence bar. Names proto personas explicitly as the no-new-research tier, then gives concrete numeric floors for the two research-based tiers (qualitative: 5-30 interviews rolling to saturation; statistical: qualitative research first, then a survey of at least 100, ideally 500+, respondents, run through clustering)
Quotable: "Proto personas are a lightweight form of ad-hoc personas created with no new research." / "based on small-sample qualitative research, such as interviews, usability tests, or field studies" / "based on both qualitative and quantitative research" / "at least 100 (ideally 500 or more) respondents" / "rooted in a qualitative understanding of users"

**[16] Nielsen Norman Group - "How Many Participants for a UX Interview?".** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/interview-sample-size/`
Supports: Directly addresses whether a numeric minimum exists for interviews feeding a persona, and pushes back on the '5 per persona' rule of thumb as sometimes wasteful rather than authoritative
Quotable: "Unfortunately, there isn't a golden number" / "Others have been taught to recruit 5 people per persona, a rule of thumb to ensure that the sample is representative and large enough. However, this rule can result in many more interviews than necessary."

**[17] Nielsen Norman Group - "Are Your Personas Outdated? Know When It's Right To Revise".** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/revising-personas/`
Supports: The dimension's source on updating and retiring personas: named triggers (business change, competitive change, user-base drift), a surveyed cadence distribution, an outcome claim tying update frequency to perceived project success, and the explicit option to retire and replace rather than revise
Quotable: "Has the business changed?" / "If the behaviors of any one segment differs from your expectations...your persona may need an update." / "nearly half of respondents (46%) update personas every 1-4 years" / "teams who keep their personas up-to-date perceive their projects as more successful" / "If you have not updated your personas in 5 or more years, chances are they are performing for your products about as well as a dull butter knife cutting steak." / "retire them altogether and create new personas that better reflect your current business and customers" / "Has the business changed? If your business offerings and objectives have remained fairly steady, it's less likely that your personas are out of date." / "Has the competitive landscape changed? Competition has an impact on your customers' expectations."
Contested/time-bound: claimed by 2 research dimensions; one entry kept, carrying the fuller extract.

### The case against personas

**[18] Kim Flaherty, "Why Personas Fail" (Nielsen Norman Group).** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/why-personas-fail/`
Supports: The dominant practitioner account of persona failure, framed as organizational/process failure (non-use, no buy-in, siloed creation, poor communication, wrong scope) rather than a method-validity critique; explicitly cites no studies or statistics.
Quotable: "Personas should not be an isolated endeavor undertaken by the UX team and unveiled like a piece of artwork." / "not 8.5 x 11 handouts"

**[19] Christopher N. Chapman & Russell P. Milham, "The Personas' New Clothes: Methodological and Practical Arguments against a Popular Method" (Proceedings of the Human Factors and Ergonomics Society 50th Annual Meeting, 2006).** academic. **fetched-and-verified.**
`https://cnchapman.wordpress.com/wp-content/uploads/2007/03/chapman-milham-personas-hfes2006-0139-0330.pdf`
Supports: The primary peer-reviewed academic methodological critique of personas: unfalsifiability, the curse of dimensionality, no demonstrable population coverage, political misuse, and an explicit 2006-era statement that no adequate reliability/validity/utility studies existed.
Quotable: "Personas cannot be adequately verified or falsified and therefore have no demonstrable validity." / "Because personas are admittedly fictional, it would seem that there is no way to falsify them; no data can disprove a fictional construction. Therefore, they are outside the scientific method and cannot be verified." / "there is essentially no way to generalize from a well-specified persona to a population of interest" / "There have been no adequate studies addressing the reliability, validity, or utility of the method." / "Rönkkö (2005) found that personas had limited value to inform design, but served primarily to justify decisions that were actually made on other grounds."

**[20] Joni Salminen, S.G. Jung, K. Chhirang & B.J. Jansen, "Instilling Knowledge Claims of Personas from 346 Research Articles" (ACM CHI 2021), summarized on the QCRI Persona Research blog.** practitioner. **fetched-and-verified.**
`https://persona.qcri.org/blog/instilling-knowledge-claims-of-personas-from-346-research-articles/`
Supports: A systematic, meta-level assessment (130 knowledge claims extracted from 346 articles) that the persona evidence base is real but uneven: strong consensus on persona definition, but a high proportion of unverified claims specifically in the creation and use categories, with minimal literature on evaluation.
Quotable: "a higher degree of consensus" / "a high proportion of unverified claims" / "claims that are not substantiated with strong empirical evidence and warrant future work"

**[21] Jessica Marriott, "Beware of Persona Bias" (Bentley University User Experience Center).** practitioner. **fetched-and-verified.**
`https://www.bentley.edu/centers/user-experience-center/beware-persona-bias`
Supports: The equity/stereotyping critique: names naming, imagery, and accessibility as three concrete bias vectors in persona construction, and cites a disability-population figure to argue for deliberately including disability attributes in core personas.
Quotable: "nearly 40 million Americans with a disability in 2015"

**[22] Allison Banko, "Persona Marketing: NetProspex increases website visit duration 900%, lifts marketing-generated revenue 171%" (MarketingSherpa, March 26, 2014).** vendor. **fetched-and-verified.**
`https://marketingsherpa.com/article/case-study/netprospex-increases-website-visit-duration`
Supports: Traces the widely-circulated '900% increase' and related persona-effectiveness percentages to their primary source: a single uncontrolled case study of one company (NetProspex) bundling persona creation with a full site redesign, content overhaul, and email-automation change, with no comparison group and no isolation of the persona variable specifically.

### The product-management context

**[23] Alan Klement - "Replacing Personas With Characters" (Medium, Jobs-to-be-Done author).** practitioner. **fetched-and-verified.**
`https://medium.com/down-the-rabbit-hole/replacing-personas-with-characters-aa72d3cf6c69`
Supports: The explicit JTBD-camp rejection of personas: they lack causality, invite team-member-specific fabricated assumptions (his WYSIATI framing), and he proposes replacing them outright with a different artifact (Characters, built on anxieties/motivations and purchase-progress events/situations), not a variant of persona.
Quotable: "each team member reads a persona, they will subconsciously fill it with their own assumptions which differ from everyone else" / "adding subjective and fictional details...will unwittingly distract and fragment a team as each team member subconsciously brings in their own prejudices & confirmation biases" / "adding fictional information to this process is disinformation"

**[24] Nielsen Norman Group - "Personas vs. Jobs-to-Be-Done".** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/personas-jobs-be-done/`
Supports: The counter-position inside the same JTBD-vs-persona debate: NN/g explicitly names and rejects the replace-personas camp, arguing the two artifacts answer different questions (who vs. what) and are complementary. Also supplies the sharpest available critique of bad personas as disguised marketing segments.
Quotable: "Despite many contrary voices suggesting that JTBD can entirely replace personas, the two are in fact, quite compatible" / "marketing segments being masqueraded as personas" / "personas are meant to be rich representations of users" / "whenever users 'hire' (i.e., use) a product, they do it for a specific 'job'" / "generalize them among the entire user base, and therefore miss that key sense of context"
Contested/time-bound: claimed by 2 research dimensions; one entry kept, carrying the fuller extract.

**[25] Teresa Torres - "Opportunity Solution Trees: Visualize Your Discovery to Stay Aligned and Drive Outcomes" (Product Talk).** practitioner. **fetched-and-verified.**
`https://www.producttalk.org/opportunity-solution-trees/`
Supports: Direct evidence for the continuous-discovery question: this canonical explainer of the opportunity solution tree, the core artifact of continuous-discovery practice, does not mention personas anywhere. The tree's vocabulary (outcome, opportunity, solution, assumption test, customer segment) has no persona node.

**[26] Wikipedia - "Outcome-Driven Innovation" (Ulwick's ODI methodology).** vendor. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Outcome-Driven_Innovation`
Supports: Confirms Ulwick's ODI is defined in explicit opposition to demographic/attribute-based segmentation (the same category persona critiques target), even though the article never names personas directly.
Quotable: "ODI focuses on customer-desired outcome rather than demographic profile in order to segment markets and offer well-targeted products"

**[27] Marty Cagan / Silicon Valley Product Group - "Personas for Product Management" (SVPG).** practitioner. **fetched-and-verified.**
`https://www.svpg.com/personas-for-product-management-2/`
Supports: Evidence for named product sources' silence-as-acceptance: a leading product-management voice (Cagan, author of INSPIRED) publishes personas descriptively, with worked examples, and neither argues for nor against the method, treating it as unremarkable accepted practice rather than either endorsing it with argument or rejecting it.

**[28] HubSpot - "Ideal customer profiles and buyer personas: How are they different?".** vendor. **fetched-and-verified.**
`https://blog.hubspot.com/customers/ideal-customer-profiles-and-buyer-personas-are-they-different`
Supports: Establishes ICP and buyer persona as a DIFFERENT artifact pair from the product/design user persona: ICP describes a qualifying company (B2B firmographic filter), buyer persona describes an individual decision-maker inside that company, and marketing/sales literature treats both as sales-qualification tools distinct in purpose from a UX/product user persona.
Quotable: "An ideal customer profile (ICP) defines the perfect company for your product or service. It's a detailed description of the organization that would get the most value from what you're selling and actually has the budget and authority to buy it." / "A buyer persona is a detailed profile of an individual decision-maker within your ideal customer companies." / "Personas tell you who you're speaking to. ICPs tell you which companies are worth speaking to in the first place." / "nailed the individual, but missed the organization"
Contested/time-bound: claimed by 2 research dimensions; one entry kept, carrying the fuller extract.

### Boundaries and adjacent artifacts

**[29] Adele Revella / Buyer Persona Institute - "What Is a Buyer Persona?" (buyerpersona.com).** practitioner. **fetched-and-verified.**
`https://www.buyerpersona.com/what-is-a-buyer-persona`
Supports: The test that separates a buyer persona from a generic profile / user persona: a buyer persona reveals insight into the buying decision (attitudes, concerns, decision criteria, journey to choosing you vs. a competitor vs. status quo), whereas a profile that only lists individual characteristics reveals nothing about how to influence the decision.
Quotable: "A buyer persona reveals insights about your buyers' decisions - the attitudes, concerns, decision criteria, and journey that drive prospective customers to choose you, your competitor or the status quo." / "buyer profiles that only describe characteristics of individuals involved in the buying decision reveal little insight about how to influence them when they are evaluating you and your competitors"

**[30] UXPressia Blog - "Persona vs. market segment: two sides of the same coin?".** vendor. **fetched-and-verified.**
`https://uxpressia.com/blog/persona-vs-market-segment`
Supports: The test that separates a market segment from a persona: segmentation is a strategic, faceless grouping tool used once a strategy exists; a persona is a tactical, humanized single-character tool used early in product development to see the business through one representative user's eyes.
Quotable: "Personas feel like real people while representing a bunch of customers. A market segment is more about a faceless crowd." / "market segmentation will be a great help when you already have a certain strategy"

**[31] Roman Pichler - "From Personas to User Stories" (romanpichler.com).** practitioner. **fetched-and-verified.**
`https://www.romanpichler.com/blog/personas-epics-user-stories/`
Supports: Relationship/boundary between a persona and an agile user role/user story: the persona is the upstream research artifact (a full archetype with goals and problems); the user role and user story are the downstream, sprint-ready requirement artifact written from the persona's perspective. Credits Mike Cohn with first deriving user stories from personas.
Quotable: "User stories are a powerful technique to capture the product functionality from the perspective of a user or customer. But how do we discover the right stories?" / "Personas offer a great way to capture the users and the customers with their needs"

**[32] Evolv (Evolv Branding Advertising and Marketing LLC) - "What is Anti-Persona?" (evolvbam.com, updated Sept 17 2022).** vendor. **fetched-and-verified.**
`https://www.evolvbam.com/post/what-is-anti-persona`
Supports: Definition and test for anti-persona: a semi-fictional depiction of the customer type a company deliberately does NOT want to attract (dissatisfied, high-return, reputation-damaging), used to sharpen and bound the positive persona by explicit contrast, illustrated with a named example pair (Susie the Solopreneur vs. Beth the Bureaucrat).
Quotable: "Your anti-persona is the type of customer that is never satisfied, returns everything, and tells all their friends how terrible you are."

**[33] Gamestorming (Dave Gray, Sunni Brown, James Macanufo) - "Empathy Map" (gamestorming.com).** practitioner. **fetched-and-verified.**
`https://gamestorming.com/empathy-mapping/`
Supports: Definition, origin, and structure of the empathy map as one of Gamestorming's methods; the test that separates it from a persona is structural (a single-session, five-sense workshop canvas centered on a stakeholder in a specific context) rather than an explicit textual comparison, since the source itself does not name personas.
Quotable: "one of Gamestorming's methods for understanding audiences, including users, customers, and other players in any business ecosystem" / "gain a deeper level of understanding of a stakeholder in your business ecosystem"

---

### Sought and not retrieved

These are recorded so that no draft can quietly assume them. **Nothing in this bundle may rest on any entry
in this section.**

**[34] Alan Cooper. *The Inmates Are Running the Asylum*, chapter 9, "Personas" (book pages 123-148).** primary. **not-retrieved.**
No URL: this is a printed book, and linking a bookseller page would manufacture the appearance of retrieval.
The publisher's free sample PDF was read and is entry [4], but it stops at front matter.
Supports: nothing in this bundle. Sought for: Cooper's own definitional prose on what a persona is, the
elastic user, and precision versus accuracy. **The chapter body was never read. Its section titles, listed
in [4], come from the table of contents only, and this bundle states nothing about the chapter's argument.**

**[35] Alan Cooper, Robert Reimann and David Cronin. *About Face: The Essentials of Interaction Design*.** primary. **not-retrieved.**
No URL: a printed book, not retrieved; no free full text was located and no bookseller link is given for the
reason stated in [34].
Supports: nothing in this bundle. Sought for: the elaborated Goal-Directed Design method and its persona
chapter, including the primary/secondary/negative/served persona taxonomy. **Not read in any edition.**

**[36] John Pruitt and Tamara Adlin. *The Persona Lifecycle: Keeping People in Mind Throughout Product Design* (2006).** standards. **not-retrieved.**
`https://www.amazon.com/Persona-Lifecycle-Throughout-Interactive-Technologies/dp/0125662513`
Supports: nothing in this bundle. Sought for: the fullest published treatment of persona creation, use and
retirement. Only secondary summaries and the title framing were available. **No body text was read.**

**[37] Joni Salminen, Kathleen Guan, Soon-Gyo Jung and Bernard Jansen. "Use Cases for Design Personas: A Systematic Review and New Frontiers" (ACM CHI 2022).** academic. **not-retrieved.**
`https://dl.acm.org/doi/10.1145/3491102.3517589`
Supports: nothing in this bundle. Sought for: a systematic review of 95 persona-use-case articles, the
companion to [20]. **The ACM page returned HTTP 403 and only abstract-level snippet text was visible, which
is treated as unverified and is not quoted.**

**[38] "How Empathizing with Persona Helps in Design Thinking: An Experimental Study" (ResearchGate).** academic. **not-retrieved.**
`https://www.researchgate.net/publication/331430823_HOW_EMPATHIZING_WITH_PERSONA_HELPS_IN_DESIGN_THINKING_AN_EX`
Supports: nothing in this bundle. Sought for: the one experimental study located that reports a measured
design-outcome effect from persona use, a five-week study with novice designers. **Found only as a search
summary. Its effect size, method and sample were never read, and no claim of persona effectiveness in this
bundle rests on it.**

**[39] Kari Ronkko (2005), and Ronkko, Hellman, Kilander and Dittrich (2004).** academic. **not-retrieved.**
No URL: neither paper was located as a retrievable document; both are known to this research only as
citations inside [19].
Supports: nothing in this bundle. Sought for: the two empirical studies Chapman and Milham cite for the
finding that personas served to justify decisions made on other grounds, and that political dominance caused
persona use to fail. **Known only at second hand. Where the bundle mentions this finding it attributes it to
Chapman and Milham citing them, never directly to Ronkko.**

**[40] Jonathan Grudin and John Pruitt (2002).** academic. **not-retrieved.**
No URL: known to this research only as a citation inside [19].
Supports: nothing in this bundle. Sought for: the documented case of a senior manager removing persona
posters to make his team ignore them, which [19] cites to this paper. **Second hand only.**

**[41] Anthony Ulwick, own writing on Outcome-Driven Innovation and personas.** practitioner. **not-retrieved.**
`https://strategyn.com/`
Supports: nothing in this bundle. Sought for: a direct statement by Ulwick addressing personas by name.
**Not found.** Only ODI's general anti-demographic-segmentation framing was confirmed, and only through a
Wikipedia summary [26]. **This bundle makes no claim about what Ulwick says about personas.**

**[42] Clayton Christensen and the Christensen Institute, primary Jobs-to-be-Done material.** primary. **not-retrieved.**
`https://www.christenseninstitute.org`
Supports: nothing in this bundle. Sought for: a primary Christensen-camp statement contrasting JTBD against
persona-based segmentation, including the milkshake study. **Summarised at search-snippet level only and
never fetched. The bundle attributes the replace-personas argument to Klement [23], who made it in a
document that was read, and not to Christensen.**

**[43] Cooper (the firm). "The Origin of Personas" and "Getting from Research to Personas", cooper.com.** primary. **not-retrieved.**
`https://www.cooper.com/journal/2008/5/the_origin_of_personas/`
Supports: nothing in this bundle. Sought for: the canonical hosted versions of Cooper's essays. **Repeated
fetches returned a socket hang up.** A faithful-looking third-party mirror was read instead and is entry
[1]; the mirror's fidelity against the original could not be confirmed, and that limitation is recorded in
[1] rather than glossed.

**[44] UX Booth. "Rethinking User Personas".** practitioner. **not-retrieved.**
`https://uxbooth.com/articles/rethinking-user-personas/`
Supports: nothing in this bundle. Sought for: a practitioner critique on persona storytelling and stereotype
risk. **The fetch exceeded ten redirects and the body was never read.**

**[45] Kerry Stith. "Problems with personas for people with disabilities, and how to fix them" (LinkedIn).** practitioner. **not-retrieved.**
`https://www.linkedin.com/pulse/problems-personas-people-disabilities-how-fix-them-kerry-stith`
Supports: nothing in this bundle. Sought for: a first-hand practitioner account of disability personas
reinforcing stereotypes. **Only a search snippet was seen.** The accessibility critique in this bundle rests
on [21], which was read in full, and not on this.

---

## Contested register

Recorded rather than resolved. Where sources genuinely disagree, the bundle presents the disagreement.

**1. Did Cooper invent the persona, or formalise something already circulating?** Pruitt and Grudin note the
abstract user was a known problem and that comparable ideas, including Geoffrey Moore's Target Customer
Characterizations and independently developed user archetypes, were in circulation [3]. Cooper's own account
presents it as an original discovery on a specific project [1]. **Neither was tested against the other here.**

**2. How much research must sit behind a persona?** Cooper's position, as quoted by Pruitt and Grudin, is
that a lighter initial investigation suffices and heavier ongoing research "wasn't solving the fundamental
problem"; theirs is that persona use needs a strong and ongoing research effort [3]. This is the field's
founding disagreement and it has never closed.

**3. Is a persona a profile or a decision narrative?** Four of the formats read organise around identity,
goals and pains [5][6][7][8]. The Buyer Persona Institute discards that spine for the 5 Rings of Buying
Insight and argues the buyer's own voice is the document: "pictures don't talk, and it's her voice that you
need" [9]. **This is a lineage split between UX and B2B marketing, not a quality difference.**

**4. Does Scenarios belong as a labelled section?** Only the Interaction Design Foundation names it as one,
defining it structurally as beginning, middle and end [8]. The others fold the same material into Usage
Context [6] or Situations [8], or omit it [7].

**5. Is the anti-persona a section or a separate document?** The one source addressing its packaging
publishes it separately [10]; the other defines the concept without saying how it is packaged [32]. **This
bundle follows [10] and departs from its own build spec, on one source. A second source either way would
settle it.**

**6. Is there a minimum interview count?** Nielsen Norman Group gives 5 to 30 for qualitative personas [15]
and, in a companion piece, warns "Unfortunately, there isn't a golden number" and resists the
five-per-persona rule [16]. **Both are the same publisher.**

**7. Do personas improve design outcomes?** The two sources that examined the evidence base as a whole
conclude the rigorous evidence for creation and use claims is thin or absent [19][20]. The circulating
counter-evidence is a single uncontrolled case study that isolated nothing [22], and the one experimental
study located was never read [38]. **The honest answer is that nobody has shown it either way.**

**8. Is persona failure a method problem or an implementation problem?** Flaherty attributes failure
entirely to organisational process, buy-in, siloed creation and poor communication, and does not question
the method's validity [18]. Chapman and Milham attribute it to the method itself, independent of
implementation quality [19]. **These are different diagnoses with different remedies, and a reader should
know which one they are buying.**

**9. Is JTBD meant to replace personas?** Klement argues yes and proposes a structurally different artifact
[23]. Nielsen Norman Group names that position and rebuts it as compatible rather than competing [24].

**10. Who owns a persona?** Search evidence split between product management and UX research, with no source
read in full resolving it. **Treated as organisation-dependent rather than settled.**

**11. How often should a persona be revised?** Nielsen Norman Group surveyed the cadence and found it
spread rather than clustered. The one share its page states verbatim is that "nearly half of respondents
(46%) update personas every 1-4 years" [17], with the rest divided between much more frequent and much less
frequent revision. **The other shares were not captured verbatim and no number for them appears anywhere in
this bundle.** Only the event triggers are unambiguous; the cadence is not.

**12. Is a user profile a different artifact from a persona?** Asserted in secondary and vendor commentary,
but **no source read in full states the test in its own words**. The fictional-versus-factual framing
commonly attributed to Nielsen Norman Group was seen only in a search snippet and was not verified, so it is
not quoted anywhere in this bundle.

---

## Sought and not found

Distinct from `not-retrieved` above: these were searched for and appear not to exist in the form sought.

- **A large-sample controlled study comparing design outcomes with personas against without them.** The two
  sources that surveyed the evidence base both report its absence [19][20], and Chapman and Milham go
  further by proposing four concrete experimental designs that would settle it, which is itself evidence
  that as of that paper they had not been run [19].
- **A published persona format using "Behaviors" as a standalone top-level section.** None of the six read.
  The nearest is the Service Manual's Behaviour and preferences block [5].
- **A published format treating a multi-quote "Quotes and Evidence" block as a standard bounded section.**
  None, except where buyer quotation is the whole document rather than a subsection [9].
- **A named source stating the user-profile-versus-persona test in its own words.** Not found in any source
  read in full.
- **A single authoritative source on who owns the persona.** Not found; see contested register 10.
- **A direct statement by Ulwick [41] or Torres [25] about personas by name.** Neither exists in what was
  read. The Torres finding is an absence observed in a document that *was* read, which is a weaker and more
  honest claim than a stated position, and the bundle says so.
