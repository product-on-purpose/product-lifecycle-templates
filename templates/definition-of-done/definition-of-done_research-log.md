# definition-of-done research log

Researched 2026-08-06 across six parallel dimensions: the Scrum Guide canon, structure in practice, the
boundary against acceptance criteria and neighbours, failure modes and the evidence base, ownership and
staleness, and levels above the single team. **27 sources**, of which **22 fetched-and-verified** and
**5 not-retrieved**. Of the 22 read, 5 are primary, 3 standards, 9 practitioner and 5 vendor. Retrieval
status is recorded per source in the three-token
vocabulary the library gates
([ADR 0029](../../docs/internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md)), and only
`fetched-and-verified` sources are quoted.

**How to read this log.** A `Supports:` clause says what the bundle is allowed to rest on that source for.
A `Quotable:` phrase was read verbatim on the page. If a claim in the companion is not covered by some
entry's `Supports:` clause here, the claim has no home and must be cut, not justified after the fact.

**This family's contract names its citation hazard as "folklore presented as standard", and the hazard is
real.** The 2020 Scrum Guide was fetched and read directly rather than summarised, and three of the most
widely repeated things said about the Definition of Done **are not in it**. Those absences are recorded in
framing point 4 and are the single most useful output of this research.

---

## Honest framing: the seven things this bundle has to say

**1. The Definition of Done is a commitment, not an artifact, and that is a 2020 change.** The Guide states
it plainly: "The Definition of Done is a formal description of the state of the Increment when it meets the
quality measures required for the product" [1], and places it in a three-way structure, "For the Product
Backlog it is the Product Goal. For the Sprint Backlog it is the Sprint Goal. For the Increment it is the
Definition of Done" [1]. Scrum.org's own revisions page confirms this is new in 2020: "Each of the three
artifacts now contain 'commitments' to them", and "the Increment has the Definition of Done (now without the
quotes)" [2]. **Any description of the DoD as an artifact in its own right predates 2020**, and a great deal
of circulating material does.

**2. An organisational standard is a floor, never a ceiling, and the rule has two branches.** "If the
Definition of Done for an increment is part of the standards of the organization, all Scrum Teams must
follow it as a minimum. If it is not an organizational standard, the Scrum Team must create a Definition of
Done appropriate for the product" [1]. A team may strengthen an inherited standard and may not weaken it.
For multiple teams on one product there is **one** Definition of Done: they "must mutually define and comply
with the same Definition of Done" [1]. The 2017 Guide said something recognisably similar and not identical,
"conventions, standards or guidelines of the development organization" [15], which the 2020 rewrite narrowed
to "standards of the organization" [1].

**3. Nobody owns it, and the Guide names no owning role.** What it says is "The Developers are required to
conform to the Definition of Done" [1] and lists "Instilling quality by adhering to a Definition of Done"
among their accountabilities [1]. **Across every source read, ownership is collective and no single role is
ever named**: not the Scrum Master, not an architect, not the Product Owner. That matters here because this
library's own `acceptance-criteria` bundle currently states that "the development team owns the DoD, with
the Product Owner having final say", citing a Scrum.org page that its own reference entry records as
**HTTP 403 and never read**, cross-checked against the Guide. **The Guide does not support it**, and
"development team" is vocabulary the 2020 rewrite retired. That correction ships with this bundle.

**4. Three things everyone says about the Definition of Done are not in the Scrum Guide.** Recorded because
a reader will meet all three, and because this family's contract predicted exactly this failure mode.

- **"It is a checklist."** The word *checklist* does not appear in the Guide. The Guide says "a formal
  description of the state" [1], which a checklist can implement but which the Guide never prescribes.
- **"It evolves and gets stricter over time."** This one needs stating precisely, because a flat denial
  would itself be wrong. The **2017** Guide did link the Sprint Retrospective to adapting the Definition of
  Done [15]. No equivalent sentence was confirmed in the **2020** DoD passages retrieved, across repeated
  attempts. So the practice has canonical support in the superseded edition and, as far as this research
  could verify, none in the current one. The stronger claim, that a DoD should get progressively
  *stricter*, is in neither.
- **"It is the team's contract."** The Guide uses no contract language anywhere near the DoD.

None of the three is *wrong* as practice. All three are folklore when presented as the standard.

**5. The one large statistic about the Definition of Done traces cleanly, and its authors say it is
incomplete.** The circulating "93 percent of practitioners find the DoD valuable" resolves to Kopczynska,
Ochodek, Piechowiak and Nawrocki, a survey of 137 practitioners across 45 countries published in the
*Journal of Systems and Software* [13]. It is the **only controlled evidence this research found**, and the
authors state their own list of benefits and problems "is largely incomplete or partially irrelevant" as a
threat to validity, because no prior study had produced one to build on [13]. Two smaller predecessor
studies exist. **Treat the evidence base as thin but real: one solid survey, not a settled literature, and
not an absence.**

**6. Published Definitions of Done vary by roughly seven times, and the variance tracks scope rather than
formality.** GitLab publishes a real, currently-shipping engineering DoD: 41 items across six labelled
subsections, gating a merge to production [4]. Practitioner story-level checklists run six or seven flat
items [6]. Scrum Alliance is the clearest named source on why, naming three levels and giving a **sorting
rule** rather than a fixed list per level: can we do this for each feature, and if not each sprint, and if
not then it is a release activity [3]. **That is what justifies a second size on this type**, and it is a
departure from the build spec, which called for one. See the format verdict.

**7. No source supplies a condition-based review trigger, and that is this bundle's contribution.** Every
source that discusses keeping a DoD current reaches for a cadence or a ceremony, most often the
retrospective. **None names an event that makes the document wrong and a person who notices.** The family
contract requires exactly that, on the reasoning that a standing document fails by drifting quietly out of
date. The absence is recorded here so the template's Review Trigger section is understood as filling a real
gap rather than restating received practice.

---

## Format verdict (ADR 0028), and the size call

Under [ADR 0028](../../docs/internal/decisions/0028-adopt-a-format-axis.md) a format ships only when it is
**structurally distinct** and **in circulation with a named source**.

| Candidate | Structurally distinct? | Named source in circulation? | Verdict |
|---|---|---|---|
| **Criteria list** (scope, criteria, trigger) | This is the baseline shape, and every source read carries it in some form | Yes [1][3][4][6] | **Ships** as the only format |
| **Levelled DoD** (feature, sprint, release) | No. Same document; the levels are a **sorting rule for criteria**, not a different outline | Yes [3] | **Rejected as a format.** It is a section inside `full`, which is where the sorting rule belongs |
| **Definition of Ready** | Yes, genuinely: it gates entry rather than exit | Yes, and **contested by name** [7][8] | **Out of scope.** A different document for the opposite gate, taught as a boundary |

**One format ships, at two sizes, and the second size is a departure from the build spec.** The spec called
for `[lean]` only. The evidence does not support that: a six-item story-level checklist [6] and a 41-item
sectioned release gate [4] are not the same weight of document, and Scrum Alliance supplies the rule that
separates them [3]. So `lean` carries Scope and Ownership, Done Criteria, and Review Trigger; `full` inserts
Criteria by Level, What This Excludes, and When Work Does Not Meet It, keeping lean a strict ordered subset.
The catalog's size calls are hypotheses rather than facts, which is finding EC-2 in
[`STATE.md`](../../STATE.md) and has already changed members of two other families.

**On the Definition of Ready, and why the bundle teaches it as a boundary rather than ignoring it.** It is
the sibling readers most often conflate with the DoD, and it is **genuinely contested**: Agile Alliance
carries it as a glossary entry [7] while a named practitioner account traces its rise and argues against it
[8]. Presenting it as settled either way would misrepresent the field.

---

## Sources

### The Scrum Guide canon, checked against the primary text

**[1] Scrum.org / Ken Schwaber and Jeff Sutherland - The Scrum Guide (2020 version).** primary. **fetched-and-verified.**
`https://scrumguides.org/scrum-guide.html`
Supports: Who creates/owns the DoD: Developers conform to it; organizational standards take precedence when they exist, otherwise the Scrum Team creates one appropriate for the product. Current version does not surface an explicit retrospective-adaptation trigger sentence.
Quotable: "The Definition of Done is a formal description of the state of the Increment when it meets the quality measures required for the product." / "If the Definition of Done for an increment is part of the standards of the organization, all Scrum Teams must follow it as a minimum. If it is not an organizational standard, the Scrum Team must create a Definition of Done appropriate for the product." / "If there are multiple Scrum Teams working together on a product, they must mutually define and comply with the same Definition of Done." / "The Developers are required to conform to the Definition of Done." / "The moment a Product Backlog item meets the Definition of Done, an Increment is born." / "If a Product Backlog item does not meet the Definition of Done, it cannot be released or even presented at the Sprint Review. Instead, it returns to the Product Backlog for future consideration." / "For the Product Backlog it is the Product Goal. For the Sprint Backlog it is the Sprint Goal. For the Increment it is the Definition of Done." / "Work cannot be considered part of an Increment unless it meets the Definition of Done." / "Instilling quality by adhering to a Definition of Done" / "An Increment is a concrete stepping stone toward the Product Goal. Each Increment is additive to all prior Increments and thoroughly verified, ensuring that all Increments work together. In order to provide value, the Increment must be usable." / "Work cannot be considered part of an Increment unless it meets the Definition of Done"
Contested/time-bound: one source reached by 4 dimensions or URL forms; a single entry is kept, carrying the union of their extracts.

**[2] Scrum.org, "Scrum Guide Revisions" history page (scrumguides.org).** primary. **fetched-and-verified.**
`https://www.scrumguides.org/revisions.html`
Supports: That the 2020 rewrite formalized Definition of Done as one of three artifact "commitments", changed from the pre-2020 framing
Quotable: "the Increment has the Definition of Done (now without the quotes)" / "Each of the three artifacts now contain 'commitments' to them. For the Product Backlog it is the Product Goal, the Sprint Backlog has the Sprint Goal, and the Increment has the Definition of Done"

### Structure in practice

**[3] Scrum Alliance - "What is the Definition of Done?".** standards. **fetched-and-verified.**
`https://resources.scrumalliance.org/Article/definition-dod`
Supports: DoD is explicitly leveled (feature/story, sprint, release), not flat, and is chosen by a decision tree rather than listed as one fixed checklist.
Quotable: "Can we do this activity for each feature? If not, then" / "Can we do this activity for each sprint? If not, then" / "We have to do this activity for our release!" / "a comprehensive checklist of necessary, value-added activities" / "not all value-added activities will be applicable to each feature"

**[4] GitLab - "Merge requests workflow" (docs.gitlab.com, Definition of Done section).** practitioner. **fetched-and-verified.**
`https://docs.gitlab.com/development/contributing/merge_request_workflow/`
Supports: The single best-documented, actually-filled, named-company DoD found: not a flat checklist, organized into 6 labeled subsections (Functionality, Testing, UI changes, Description of changes, Approval, Production use) plus 4 top-level criteria, totaling 41 dated line items. This is a release/production-grade DoD, considerably longer than any story-level example found elsewhere.
Quotable: "To reach the definition of done, the merge request must create no regressions and meet all these criteria:" / "Verified as working in production on GitLab.com." / "Working and clean code that is commented where needed." / "Unit, integration, and system tests that all pass on the CI server." / "The MR must include "Before" and "After" screenshots if UI changes are made." / "Reviewed by relevant reviewers, and all concerns are addressed for Availability, Regressions, and Security." / "Merged by a project maintainer." / "Confirmed to be working in the production with no new Sentry errors after the contribution is deployed."

**[5] Agile Alliance - "Definition of Done" glossary entry.** practitioner. **fetched-and-verified.**
`https://agilealliance.org/glossary/definition-of-done/`
Supports: Canonical framing that DoD is structurally a checklist of activities (testing, documenting, deploying) rather than outcomes, and two named failure modes: a DoD that stays implicit/unwritten loses its effectiveness, and a DoD that becomes an over-engineered perfectionist list stops serving its minimum-bar purpose.
Quotable: "The team agrees on and displays a list of criteria that must be met before a product increment (often a user story) is considered "done"." / "product sashimi" / "Effectiveness diminishes if the definition remains unwritten" / "done programming, creating test data, actually testing, ensuring it's deployable, documenting…" / "a list of criteria that must be met before a product increment 'often a user story' is considered 'done'." / "Failure to meet these criteria at the end of a sprint normally implies that the work should not be counted toward that sprint's velocity." / "the team agrees on, and displays prominently somewhere in the team room, a list of criteria."
Contested/time-bound: one source reached by 3 dimensions or URL forms; a single entry is kept, carrying the union of their extracts.

**[6] Plane (project-management vendor blog) - "Definition of done (DoD): Checklist examples for Agile teams".** vendor. **fetched-and-verified.**
`https://plane.so/blog/definition-of-done-dod-checklist-examples-for-agile-teams`
Supports: A practitioner/vendor source publishing four concrete, short (6-7 item), flat checklists scoped by team type (universal, software dev, product/feature, non-engineering). Directly contrasts with GitLab's 41-item sectioned DoD on length, and shows flat is a real, common published shape at the team/story level even though multi-level (story/sprint/release) is discussed conceptually without itemized breakdowns per level.
Quotable: "Task meets defined acceptance criteria" / "Code reviewed and approved" / "Feature deployed to staging and verified" / "Ready for rollout or announcement"

### The boundary against acceptance criteria and other neighbours

**[7] Agile Alliance, "What is Definition of Ready?" (glossary entry).** standards. **fetched-and-verified.**
`https://agilealliance.org/glossary/definition-of-ready/`
Supports: the definition, purpose, and non-Scrum-standard status of Definition of Ready as a sibling artifact to DoD, and the origin of the term
Quotable: "the team makes explicit and visible the criteria (generally based on the INVEST matrix) that a user story must meet prior to being accepted into the upcoming iteration" / "avoids beginning work on features that do not have clearly defined completion criteria, which usually translates into costly back-and-forth discussion or rework" / "provides the team with an explicit agreement allowing it to 'push back' on accepting ill-defined features to work on"

**[8] Willem-Jan Ageling, "The rise and fall of the Definition of Ready in Scrum" (Serious Scrum, Medium).** practitioner. **fetched-and-verified.**
`https://medium.com/serious-scrum/the-rise-and-fall-of-the-definition-of-ready-in-scrum-2407c6f1c455`
Supports: the critique of Definition of Ready as anti-Agile, and the claim that it was once part of Scrum guidance and has since been dropped
Quotable: "the DoR exists to help everyone have the same understanding of when a Product Backlog Item is ready for a Sprint" / "conflicts with an Agile way of working" / "incentivizes Waterfall thinking and task completion over meeting a goal" / "The Definition of Ready used to be part of Scrum. But not anymore."

**[9] Jeremy D. Miller, "'Code Complete' is a polite fiction, 'Done, done, done' is the hard truth" (personal blog, 2012).** practitioner. **fetched-and-verified.**
`https://jeremydmiller.com/2012/12/13/code-complete-is-a-polite-fiction-done-done-done-is-the-hard-truth/`
Supports: the origin and meaning of the phrase 'done done' (or 'done, done, done') as an XP-era emphatic distinguishing true completion from 'code complete'
Quotable: "'Done, done, done' means the feature is 100% ready to deploy to production." / "XP teams used the phrase 'Done, done, done' to describe a feature as complete." / "Code complete just means that the developers have reached a point where they're ready to turn the code over for testing."

**[10] SonarSource, "What are Quality Gates?" (resource library).** vendor. **fetched-and-verified.**
`https://www.sonarsource.com/resources/library/quality-gate/`
Supports: the definition of quality gate as an automated, tool-checked pipeline checkpoint distinct from a manual completion checklist
Quotable: "Quality gates are essentially checkpoints in the software development lifecycle. They are designed to ensure that each phase of the process meets certain predefined standards before moving on to the next." / "before a piece of code can progress from development to testing, or from testing to deployment, it must pass through a quality gate. The gate checks for various criteria such as code coverage, complexity, and security vulnerabilities." / "Quality gates can be tailored to specific project requirements."

**[11] Semaphore (CI/CD vendor blog), "Release Management: Definition of Ready and Definition of Done".** vendor. **fetched-and-verified.**
`https://semaphore.io/blog/release-management`
Supports: an example of a release checklist framed (non-standardly) using DoR/DoD labels at the release-management level, distinct from the Scrum sprint-item sense of those terms
Quotable: "These are all required tasks before users can access the system or experience the feature." / "Consists of all the follow-up tasks closing a stage, like gathering user feedback, completing outstanding tickets, or doing a retrospective." / "Preliminary documentation: the users will need instructions about what changed and how to use it."

**[12] Wikipedia contributors, "Coding conventions".** standards. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Coding_conventions`
Supports: the definition and scope of coding conventions/standards, and their unenforced-by-compiler, human-facing nature as distinct from a DoD's checkable completion criteria
Quotable: "a set of guidelines for a specific programming language that recommend programming style, practices, and methods for each aspect of a program written in that language" / "Coding conventions are not enforced by compilers." / "Code conventions improve the readability of the software, allowing engineers to understand new code more quickly and thoroughly"

### Failure modes and the evidence base

**[13] Sylwia Kopczyńska, Mirosław Ochodek, Jakub Piechowiak, Jerzy Nawrocki - "On the Benefits And Problems Related to Using Definition of Done - A Survey Study" (Poznan University of Technology; accepted preprint of the paper published in Journal of Systems and Software, 2022).** primary. **fetched-and-verified.**
`https://arxiv.org/pdf/2208.04003`
Supports: The only empirical, survey-based evidence found on DoD benefits/problems: 137 practitioners across 45 countries, statistically analyzed. Grounds nearly every claim in this dimension: the 93% 'DoD is valuable' figure, the specific problem catalogue (imprecise/missing/unclear items, unavailable/undocumented DoD, DoD written verbally and never revisited, DoD creeping, team members not caring about DoD), the frequency/significance data for each problem, the finding that 22% of projects create DoD without developer involvement, and that 15 of 137 respondents said their DoD was never updated after creation.
Quotable: "93% of the respondents perceive DoD as at least valuable for their ventures. It helps them to make work items complete, assure product quality, and ensure the needed activities are executed. However, they indicated that every second project struggles with infeasible, incorrect, unavailable, or creeping DoD." / "It follows from the study that DoD is important but not easy to use and more empirical studies are needed to identify best practices in this area." / "Interestingly, 15 respondents stated that the DoDs in their projects have never been updated." / "we could still see that in 22% of the projects, the DoDs were created without involving the developers. It is a surprising observation since the DoD is used by developers everyday, and every increment they produce needs to adhere to it." / "Also, 26 respondents stated that in their projects DoDs were not explicitly documented." / "P17: DoD was not documented, unavailable (DoD was established verbally, not written down)" / "P11: Team members did not care about DoD (they omitted some or all DoD items)" / "P16: DoD was creeping (continuously growing in uncontrolled manner)" / "the most important problems with using DoDs relate to imprecise, missing, or unclear DoD items" / "Since none of the previous studies reported comprehensive lists of benefits or problems related to using DoDs, there is a threat that our list is largely incomplete or partially irrelevant."

**[14] Kollabe (vendor blog) - "Definition of Done Checklist: How High-Performing Teams Use DoD to Ship Better Software".** vendor. **fetched-and-verified.**
`https://kollabe.com/posts/definition-of-done-checklist`
Supports: The 'DoD theatre' framing named in the task: DoD as an ignored poster/ritual, weak ownership when externally imposed, vague unverifiable criteria, and the 'hardening sprint' pattern where weak DoD lets undone work hide until it forces a cleanup sprint. Also carries an unattributed claim ('research shows') about team-created vs. externally-imposed DoD correlating with performance, which this agent could NOT trace to a primary study and is flagging as unverified, not as an evidence-based finding.
Quotable: "A checklist buried in a wiki is a checklist nobody reads." / "The rest of the team never feels ownership over it, so they treat it as optional." / "'Code is good quality' and 'testing done' aren't verifiable."

### Ownership, change authority and staleness

**[15] Scrum.org / Ken Schwaber and Jeff Sutherland - The Scrum Guide (2017 version).** primary. **fetched-and-verified.**
`https://scrumguides.org/scrum-guide-2017.html`
Supports: The explicit, named review trigger for the DoD in the prior canonical text: Sprint Retrospective, actor is the Scrum Team, constrained by organizational standards.
Quotable: "During each Sprint Retrospective, the Scrum Team plans ways to increase product quality by improving work processes or adapting the definition of "Done", if appropriate and not in conflict with product or organizational standards." / "If the definition of "Done" for an increment is part of the conventions, standards or guidelines of the development organization, all Scrum Teams must follow it as a minimum." / "If there are multiple Scrum Teams working on the system or product release, the Development Teams on all the Scrum Teams must mutually define the definition of "Done"." / "If the definition of 'Done' for an increment is part of the conventions, standards or guidelines of the development organization, all Scrum Teams must follow it as a minimum." / "If there are multiple Scrum Teams working on the system or product release, the Development Teams on all the Scrum Teams must mutually define the definition of 'Done'." / "Although this may vary significantly per Scrum Team, members must have a shared understanding of what it means for work to be complete, to ensure transparency."
Contested/time-bound: one source reached by 2 dimensions or URL forms; a single entry is kept, carrying the union of their extracts.

**[16] Scrum Inc. - Definition of Done: The Team's Quality Bar.** practitioner. **fetched-and-verified.**
`https://www.scruminc.com/definition-of-done/`
Supports: DoD is not static and should expand as the team matures; a static DoD signals stagnation. Ownership follows organizational-standard-first, team-second structure. No explicit trigger mechanism given beyond team maturity.
Quotable: "If the organization has a Definition of Done for the product, every Scrum Team must follow it as a minimum. If not, the team creates its own." / "The Definition of Done is not static. As the team matures, it expands." / "A static Definition of Done means the team has stopped raising its quality bar."

**[17] Roman Pichler - Why Product Owners Should Care about Quality.** practitioner. **fetched-and-verified.**
`https://www.romanpichler.com/blog/why-product-owners-should-care-about-quality/`
Supports: Names the Product Owner as the role that enforces the DoD at acceptance/review time, calling the PO the 'guardian of quality'; this is an enforcement claim, not a change-authority claim.
Quotable: "As the product owner, you have to apply the done criteria to accept or reject work results when reviewing items; only work results that fulfil all the done criteria can be accepted. By enforcing the definition of done the product owner acts as the guardian of quality." / "Make sure that a definition of done is available and apply it properly."

### Above the single team: levels, scaling and regulated contexts

**[18] Bas Vodde and Craig Larman (LeSS.works) - "Definition of Done" framework page.** primary. **fetched-and-verified.**
`https://less.works/less/framework/definition-of-done`
Supports: LeSS's treatment of DoD as one product-level document all teams share, with teams permitted to expand it locally, and its silence on separate sprint/release-level DoD artifacts
Quotable: "The Definition of Done is an agreed list of criteria that the software will meet for each Product Backlog Item." / "The Definition of Done applies uniformly to all Product Backlog items." / "The teams that can do more will expand this product Definition of Done within their teams." / "The teams discuss their context and select the subset of the activities that all teams think they realistically can do during the Sprint."

**[19] Scaled Agile, Inc. - SAFe glossary entry, "Definition of Done".** vendor. **fetched-and-verified.**
`https://framework.scaledagile.com/blog/glossary_term/definition-of-done`
Supports: SAFe's own (thin) glossary-level framing of DoD as completeness criteria for a work product or increment of value; confirms SAFe publishes a DoD concept but this particular page does not itself elaborate the multi-level (team/program/solution) structure
Quotable: "The Definition of Done specifies the requirements for completeness of a work product or increment of value."

**[20] Johner Institute - blog post on AAMI TIR45 (agile software development for medical devices) and IEC 62304.** practitioner. **fetched-and-verified.**
`https://blog.johner-institute.com/iec-62304-medical-software/tir-45-agile-software-development/`
Supports: The regulated/safety-critical claim: DoD carries compliance weight in medical device software only when it explicitly incorporates documentation/traceability requirements, not on its own
Quotable: "QM requirements are met because there is a clear definition of done." / "The 'Definition of Done' leads to better and more compliant development documentation if it includes the documentation aspects."

**[21] Scaling Patterns Library - "Shared Definition of Done (DoD)" play.** practitioner. **fetched-and-verified.**
`https://scalingpatterns.org/plays/shared-definition-of-done/`
Supports: A practitioner articulation of shared/multi-team DoD versus single-team DoD, framed as product-level integration and consistency versus team-level functionality
Quotable: "A Shared Definition of Done (DoD) creates this clarity by establishing common expectations for quality, completeness, and consistency."

**[22] Mirko Perkusich - "Doing it Right: Definition of Done in Scaled Scrum" (Medium).** practitioner. **fetched-and-verified.**
`https://medium.com/@mirkoperkusich/doing-it-right-definition-of-done-in-scaled-scrum-3e67814a99ea`
Supports: The Nexus Guide's (2021) rule on individual Scrum Teams applying a more stringent local DoD but never a less rigorous one than the Integrated Increment's shared DoD -- quoted here as a secondary carrier because scrum.org's own Nexus Guide page would not render for direct fetch
Quotable: "they must mutually define and comply with the same Definition of Done." / "Individual Scrum Teams … may choose to apply a more stringent Definition of Done within their own teams, but cannot apply less rigorous criteria than agreed for the Integrated Increment."

---

### Sought and not retrieved

Recorded so that no draft can quietly assume them. **Nothing in this bundle may rest on any entry in this
section.**

**[23] N. Davis. "Driving Quality Improvement and Reducing Technical Debt with the Definition of Done" (IEEE, 2013).** academic. **not-retrieved.**
`https://ieeexplore.ieee.org/document/6612887`
Supports: nothing in this bundle. Sought for: the one earlier academic treatment located that ties the
Definition of Done to technical-debt reduction. **Paywalled and never read.** No claim about a DoD reducing
technical debt rests on it, or on anything else, in this bundle.

**[24] Scrum.org. The Nexus Guide.** primary. **not-retrieved.**
`https://www.scrum.org/resources/nexus-guide`
Supports: nothing in this bundle. Sought for: Nexus's clause that a team's local Definition of Done may not
be weaker than the shared one. **The page would not render its body across three fetch attempts.** The
clause is quoted in this research only through a secondary Medium article [22], so the bundle attributes it
to that secondary treatment or omits it, never to the Nexus Guide directly.

**[25] Scaled Agile, Inc. SAFe's own primary text on Definition of Done levels.** vendor. **not-retrieved.**
`https://framework.scaledagileframework.com/`
Supports: nothing in this bundle. Sought for: confirmation of whether SAFe formally defines three levels
(Team, Program, Solution) or four. **Aggregator sites assert it; Scaled Agile's own text was not
confirmed.** The SAFe glossary entry that *was* read is [19] and supports only its own definition.

**[26] Scrum.org. The bakery worked example of a Definition of Done.** primary. **not-retrieved.**
`https://www.scrum.org/resources/blog/walking-through-definition-done`
Supports: nothing in this bundle. Sought for: the closest candidate to a filled story-level example
published by a standards-tier source. **WebFetch returned empty content.** GitLab [4] is the only real
filled example this research read.

**[27] Scrum.org. The multi-team XML-injection anecdote about a missing shared Definition of Done.** primary. **not-retrieved.**
`https://www.scrum.org/resources/blog/done-understanding-definition-done`
Supports: nothing in this bundle. Sought for: a named, citable illustration of what a missing shared DoD
costs across teams. **The page returned empty content twice.** The anecdote circulates widely in search
summaries and **must not be reproduced here**, because this research never read it at its source.

---

## Contested register

Recorded rather than resolved. Where sources genuinely disagree, the bundle presents the disagreement.

**1. Should a Definition of Ready exist at all?** Agile Alliance carries it neutrally as a glossary entry
that helps avoid rework [7]. A named practitioner account traces its rise and argues it "conflicts with an
Agile way of working" [8]. **Both were read in full.** The bundle teaches the boundary and reports the
dispute rather than recommending the practice.

**2. Who has authority over the Definition of Done?** The Guide places conformance with the Developers and
makes authorship contingent on whether an organisational standard exists [1]. Roman Pichler frames the
Product Owner as carrying responsibility for quality in a way that reads as more central than the Guide
allows [17]. **This is a real difference in emphasis between a primary source and a named practitioner**,
and it is the disagreement most likely to mislead, because the practitioner framing is the one that
circulates.

**3. Is a Definition of Done a flat list or a sectioned document?** Scope-dependent rather than settled.
Practitioner story-level checklists are flat and short [6]; GitLab's real production gate is sectioned and
long [4]; Scrum Alliance supplies the sorting rule that explains why [3]. **No source read argues the other
shape is wrong.**

**4. Does the retrospective adapt the Definition of Done?** The 2017 Guide says so [15]. Repeated attempts
did not confirm an equivalent sentence in the 2020 Guide's DoD passages [1]. **Recorded as a version
difference, not as a contradiction**, because absence from the passages retrieved is weaker evidence than
presence in the text read.

**5. A vendor claim about team-created versus imposed Definitions of Done, quarantined.** A vendor blog
asserts that "research shows" only team-created definitions correlate with high performance while imposed
ones show no correlation [14]. **No primary study supporting this was found.** The source was read, the
claim was not traced, and **it must not appear in this bundle in any form.** It is recorded because a reader
will meet it.

**6. Is "encodes activities rather than outcomes" a real failure mode?** Argued in secondary and vendor
commentary, and **not** present in the one academic survey [13]. Reported as a practitioner concern, not as
a finding.

**7. Why did the 2017 wording change in 2020?** No source read states the authors' rationale. Whether the
narrowing from "conventions, standards or guidelines of the development organization" [15] to "standards of
the organization" [1] was deliberate or incidental to the larger removal of the Development Team sub-role is
**unknown**, and the bundle says so rather than inferring intent.

---

## Sought and not found

Distinct from `not-retrieved` above: these were searched for and appear not to exist in the form sought.

- **Any experimental or longitudinal study linking a Definition of Done to improved outcomes** (defect
  rates, cycle time, release success). The one solid empirical source is an explicitly non-causal
  perception-and-frequency survey [13]. **Nobody has shown the causal claim either way.**
- **A worked artifact populating all three levels side by side.** Scrum Alliance names the levels and gives
  the sorting rule [3], but no filled three-tier example was retrieved from any source.
- **A named source relating a quality gate or a coding standard to the Definition of Done directly.** Both
  neighbours are defined on their own terms [10][12] without mentioning it. The relationship the bundle
  states, that they are candidate line items inside a DoD rather than competing artifacts, is **synthesis
  from two definitions and is labelled as such**, not a sourced claim.
- **Any source naming a single role as sole owner of the Definition of Done.** Every source that addresses
  ownership makes it collective or contingent. The absence is consistent across all 22.
- **Any source supplying a condition-based review trigger**, an event that makes the document wrong plus a
  person who notices. Every source reaches for a cadence or a ceremony. This is the gap the template's
  Review Trigger section exists to fill, and it is the same gap the `runbook` research found independently
  in an entirely separate literature.
