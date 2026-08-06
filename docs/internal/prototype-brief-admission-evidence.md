# `prototype-brief`: the admission-test evidence

**Supporting evidence for [ADR 0035](decisions/0035-prototype-brief-fails-the-admission-test.md), which
found that `prototype-brief` fails [ADR 0030](decisions/0030-templating-scope-markdown-documents.md)'s
admission test and does not ship.**

This file exists so the question can be reopened without re-fetching. The bundle was never built, so there
is no `templates/prototype-brief/` and no research log in the usual place; these are the sources that
settled the decision, in the same format a research log uses.

**29 unique sources**, of which **23 fetched-and-verified** and **6 url-confirmed-not-read**, across six
research dimensions, plus 20 further sources referenced without being read. Only `fetched-and-verified`
sources may be quoted, and the same honest-retrieval contract applies here as in any bundle.

**The decisive finding:** none of these publishes a document whose defined purpose is to commission a
prototype. What they publish is prototyping practice, canvases, cards, worksheets, code toolkits, and
briefs scoped to something else. ADR 0035 sets out the four conditions that would reopen the question.

---

## Sources

**[1] Google Ventures (Jake Knapp, John Zeratsky, Braden Kowitz) - Design Sprint methodology page.** practitioner. **fetched-and-verified.**
`https://www.character.vc/sprint`
Supports: Confirms GV's five-day Design Sprint process is documented and includes prototyping as one of five days, but there is no named, separately-published 'Sprint Brief' document on this canonical source page, and the process described spans the whole sprint (problem framing through customer testing), not a document that specifically commissions a prototype.
Quotable: "Solve big problems and test new ideas in just five days." / "build a prototype of your idea and test it with real customers" / "Test the key hypotheses behind your product or business. Rapidly build realistic prototypes that are optimized for answering key questions. Run effective customer interviews..."

**[2] GV Sprint methodology (redirect source) - gv.com/sprint/.** practitioner. **fetched-and-verified.**
`https://www.gv.com/sprint/`
Supports: Confirms no 'Sprint Brief' document is described on GV's own canonical sprint page; the storyboard (a step-by-step plan for the prototype) is produced mid-process on Wednesday, not as a pre-commissioning brief document.
Quotable: "a storyboard: a step-by-step plan for your prototype"

**[3] Stanford d.school - Prototype Report Card / Prototype Testing worksheet (DesignKit worksheet, Scribd-hosted copy).** practitioner. **url-confirmed-not-read.**
`https://www.scribd.com/document/517830842/DesignKit-prototypereportcard-worksheet`
Supports: Closest thing found to a named, structured prototype-related worksheet: a two-part sheet, a planning half (learning questions, metrics, testing method, assumptions) and a capture half (what was learned, needed iterations, next steps). Fetched via a summarizing tool rather than reading raw page text, so no verbatim phrase can be certified and no quote is offered; downgraded to url-confirmed-not-read per the honest-retrieval rule since the body itself was not read, only a model's paraphrase of it.

**[4] Jeff Gothelf - Lean UX hypothesis statement format (jeffgothelf.com, Lean UX Canvas materials).** practitioner. **url-confirmed-not-read.**
`https://jeffgothelf.com/blog/how-to-use-the-lean-ux-canvas/`
Supports: Existence of a named, reusable sentence template ('We believe that [doing this] for [these people] will achieve [this outcome]. We will know this is true when we see [this signal]') used to frame a hypothesis to prototype/test, drawn from Lean UX (Gothelf and Seiden). This is a single-sentence formula, not an ordered multi-section brief document, and no verbatim text from the page itself was read (search-engine synthesis only), so it cannot be quoted.

**[5] GOV.UK Design System - Prototyping guidance (Get started: Prototyping).** primary. **url-confirmed-not-read.**
`https://design-system.service.gov.uk/get-started/prototyping/`
Supports: Existence of GOV.UK prototyping guidance and the Prototype Kit's page templates (start page, question page, task list, check-your-answers, confirmation). Search synthesis found page-type templates for building a prototype, not a 'prototype brief' planning document with an ordered section list. No verbatim text read.

**[6] Digital Scotland Service Standard - Service Manual (servicemanual.gov.scot).** primary. **url-confirmed-not-read.**
`https://servicemanual.gov.scot/service-standard`
Supports: Confirms the Scottish service standard requires teams to 'test early prototypes of all or parts of your service with your users and use their feedback to improve the design' as one of its 14 criteria, but search synthesis surfaced no named 'prototype brief' template with an ordered section list published alongside it. No verbatim text read.

**[7] Maze - Early Prototype Test Template (maze.co/templates).** vendor. **url-confirmed-not-read.**
`https://maze.co/templates/test-early-prototypes/`
Supports: Existence of a vendor 'prototype test' template built around objectives, tasks (goal-based vs free-explore missions), and success criteria (reach a screen / follow a path) rather than a written brief document per se; this is a test-configuration template inside a research-ops tool, not a standalone document type. No verbatim text read.

**[8] Daniel Stillion - 'Design brief: IDEO' (Interactions magazine, ACM, 2000, vol 7, pp.32-35).** practitioner. **url-confirmed-not-read.**
`https://interactions.acm.org/archive/view/march-april-2000/design-brief-ideo1`
Supports: Confirms IDEO published a piece titled 'Design brief' describing its general design process (understanding, observation, visualization, evaluation/refinement, implementation), behind a paywall/archive; abstract-level search did not surface an ordered section list specific to a 'prototype brief' as opposed to a general project design brief. No verbatim text read; full text not accessible without ACM Digital Library access.

**[9] Stanford d.school (Hasso Plattner Institute of Design), "Design Thinking Bootleg" deck (2018 edition).** primary. **fetched-and-verified.**
`https://dschool.sfo3.digitaloceanspaces.com/documents/dschool_bootleg_deck_2018_final_sm2-6.pdf`
Supports: Defines the PROTOTYPE artifact and the TEST mode as distinct steps; states prototyping's purpose is broader than functional testing (empathy-gaining, exploration, testing, inspiration); ties fidelity to speed of learning; gives the named mantra for the prototype-vs-test posture.
Quotable: "Prototyping gets ideas out of your head and into the world. A prototype can be anything that takes a physical form - a wall of post-its, a role-playing activity, an object. In early stages, keep prototypes inexpensive and low resolution to learn quickly and explore possibilities." / "Prototyping is often thought of as a way to test functionality, but it serves many other purposes." / "Testing is your chance to gather feedback, refine solutions, and continue to learn about your users. The test mode is an iterative mode in which you place low-resolution prototypes in the appropriate context of your user's life. Prototype as if you know you're right, but test as if you know you're wrong." / "Testing may reveal that, not only did you get the solution wrong, but you also framed the problem incorrectly."

**[10] Nielsen Norman Group (unsigned NN/g staff article), "UX Prototypes: Low Fidelity vs. High Fidelity".** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/`
Supports: Defines low-fidelity vs high-fidelity prototypes on concrete attributes (clickability, response mechanism, visual polish, content completeness) and gives explicit guidance on which fidelity level to use for which kind of question, and named tradeoffs of each.
Quotable: "use high-fidelity when testing specific UI components (e.g. mega menus, accordions), graphical elements such as affordance, page hierarchy" / "You can sketch a quick response, and erase or change part of design between test sessions" / "you are indeed testing the design and not them"

**[11] Nielsen Norman Group, "The Wizard of Oz Method in UX".** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/wizard-of-oz/`
Supports: Defines Wizard of Oz prototyping and traces its named origin: first used in 1973 by Don Norman and Allen Munro on an airport travel-assistant terminal; the term itself coined in 1983 by Jeff Kelley in his Johns Hopkins dissertation on natural-language interfaces. States the technique's purpose is early, cheap insight into desirability/utility/usability before a system is built.
Quotable: "a moderated research method in which a user interacts with an interface that appears to be autonomous but is (fully or partially) controlled by a human." / "early insights into their desirability, utility, and usability before companies spend money building them." / "The Wizard of Oz method was first documented and used in 1973 by Don Norman and Allen Munro to test an automated airport computer-terminal travel assistant." / "coined in 1983 by researcher Jeff Kelley, in his dissertation on natural-language interfaces at Johns Hopkins University."

**[12] Nielsen Norman Group, "Don't 'Validate' Designs; User Test Them".** practitioner. **fetched-and-verified.**
`https://www.nngroup.com/articles/no-validate-in-ux/`
Supports: Directly on the 'what a prototype/test can and cannot learn' sub-question: argues testing exists to surface problems and learning, not to confirm correctness, and that a study that finds nothing wrong signals a bad test, not a validated design.
Quotable: "If a usability study found nothing to improve in a design then that only proved one thing: that the test was done wrong." / "Let's learn what works and what doesn't work well for users and why."

**[13] Forbes Technology Council (contributed opinion piece), "The Danger Of Software Prototypes".** practitioner. **fetched-and-verified.**
`https://www.forbes.com/councils/forbestechcouncil/2022/04/01/the-danger-of-software-prototypes/`
Supports: On the risk of a prototype becoming production code: names three causal mechanisms (sunk-cost pressure, underspecified requirements producing 'plausible but wrong' code that's hard to justify discarding, and an over-generalized belief that iterative development means any prototype can evolve into production) and reframes Brooks's advice as 'gather enough requirements to know when to throw your prototype away.'
Quotable: "often deployed in production before they are fully validated" / "expensive rewrites and migrations" / "gather enough requirements to know when to throw your prototype away"

**[14] Teresa Torres / Product Talk - "Opportunity Solution Trees: Visualize Your Discovery to Stay Aligned and Drive Outcomes".** practitioner. **fetched-and-verified.**
`https://www.producttalk.org/opportunity-solution-trees/`
Supports: Opportunity solution tree is explicitly a visual diagram, and assumption tests sit as nodes below the solution space rather than as a standalone document.
Quotable: "Opportunity solution trees are a simple way of visually representing the paths you might take to reach a desired outcome." / "Below the solution space are assumption tests. This is how we'll evaluate which solutions will help us best create customer value in a way that drives business value."

**[15] Product Talk - "Discovering Solutions: Quickly Determine Which Ideas Will Work (And Which Won't)" (course announcement page).** practitioner. **fetched-and-verified.**
`https://www.producttalk.org/discovering-solutions/`
Supports: Confirms Torres's assumption-testing curriculum is taught via a course, and the only artifact this page names is the visual opportunity solution tree; it does not describe a written brief format.
Quotable: "a simple visual"

**[16] ModelThinkers - "Riskiest Assumption Test".** practitioner. **fetched-and-verified.**
`https://modelthinkers.com/mental-model/riskiest-assumption-test`
Supports: RAT as a named four-step practice (identify, define, experiment, act) whose output is a test artifact (landing page, survey, prototype), not a written brief.
Quotable: "A Riskiest Assumption Test (RAT) involves rapidly identifying and testing the riskiest assumptions and potential fail points for any initiative early in the process."

**[17] character.vc - Design Sprint guide (publisher successor site hosting Jake Knapp's "Sprint" book material, redirected from thesprintbook.com).** practitioner. **fetched-and-verified.**
`https://www.character.vc/guide/design-sprint`
Supports: The five-day structure (Monday map, Tuesday sketch, Wednesday decide, Thursday prototype, Friday test) and the pre-build artifacts, all framed as whiteboard/sticky-note items rather than a written brief.
Quotable: "Write the long-term goal on a whiteboard."

**[18] Strategyzer (David J. Bland and Alexander Osterwalder, from "Testing Business Ideas") - "Validate Your Ideas with the Test Card".** practitioner. **fetched-and-verified.**
`https://www.strategyzer.com/library/validate-your-ideas-with-the-test-card`
Supports: Lean-startup-style experiment design's canonical artifact is the Test Card, a single-idea PDF card with four fields, used in multiples per initiative rather than one consolidated brief.
Quotable: "What needs to be true for your idea(s) to work (aka hypothesis, assumption, or simply guess)?" / "How are you going to test if that hypothesis is true or false?" / "What are you going to measure to (in)validate your hypothesis?" / "How does success look like? What's the threshold?"

**[19] Wikipedia, "Design brief".** standards. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Design_brief`
Supports: Definition and scope of a design brief as the commissioning document for design work generally
Quotable: "A design brief is a document for a design project developed by a designer in consultation with a client." / "The brief outlines the deliverables and scope of the project, including any products or works, function and aesthetics, as well as timing and budget."

**[20] Scaled Agile Framework (Scaled Agile, Inc.), "Spikes".** practitioner. **fetched-and-verified.**
`https://framework.scaledagile.com/spikes`
Supports: Definition of a spike/research spike in agile practice, its XP origin, and its purpose of reducing risk or answering a question rather than producing a shippable increment
Quotable: "Spikes are a type of SAFe Enabler Story. Defined initially in Extreme Programming (XP), spikes represent activities such as exploration, architecture, infrastructure, research, design, and prototyping." / "gain the knowledge necessary to reduce the risk of a technical approach, better understand a requirement, or increase the reliability of a story estimate"

**[21] Wikipedia, "Statement of work".** standards. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Statement_of_work`
Supports: Definition of a statement of work as a binding, vendor-facing description of activities/deliverables/timelines, distinct from an exploratory brief
Quotable: "A narrative description of a project's work requirement" / "defines project-specific activities, deliverables and timelines for a vendor providing services to the client" / "In many cases the statement of work is a binding contract."

**[22] Wikipedia, "Creative brief".** standards. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Creative_brief`
Supports: Definition of a creative brief in advertising, who writes it, and the client-brief-to-creative-brief handoff chain
Quotable: "A creative brief is a document used by creative professionals and agencies to develop creative deliverables, such as visual design, copy, advertising, and websites." / "creative briefs are written after the client briefs the agency (client brief). After receiving the client brief, the account manager is responsible to sort the data out to come up with a creative brief"

**[23] Wikipedia, "Product requirements document".** standards. **fetched-and-verified.**
`https://en.wikipedia.org/wiki/Product_requirements_document`
Supports: Definition of a PRD as specifying WHAT to build (not how), written from a user/client/marketing point of view once requirements are settled enough to hand to a maker
Quotable: "A product requirements document (PRD) is a document containing all the requirements for a certain product. It is written to allow people to understand what a product should do." / "should, however, generally avoid anticipating or defining how the product will do it" / "Typically, a PRD is created from a user's point-of-view by a user/client or a company's marketing department. The requirements are then analyzed by a (potential) maker/supplier from a more technical point of view, broken down and detailed in a Functional Specification."

**[24] ISTQB Glossary, "Test plan".** standards. **fetched-and-verified.**
`https://istqb-glossary.page/test-plan/`
Supports: Standards-body definition of a test plan as verifying a system that already exists, against scope/approach/resources/schedule
Quotable: "A document describing the scope, approach, resources and schedule of intended test activities."

**[25] Ron Kohavi and Stefan Thomke, "The Surprising Power of Online Experiments: Getting the Most Out of A/B and Other Controlled Tests," Harvard Business Review, Sept-Oct 2017 (Reprint R1705E).** practitioner. **fetched-and-verified.**
`https://web-docs.stern.nyu.edu/executive/The%20Surprising%20Power%20of%20Online%20Experiments.pdf`
Supports: Definition of an A/B test / controlled experiment as a measured comparison against an existing live system (a control), distinguishing it from a prototype which precedes having a measurable system at all
Quotable: "In an A/B test the experimenter sets up two experiences: 'A,' the control, is usually the current system and considered the 'champion,' and 'B,' the treatment, is a modification that attempts to improve something-the 'challenger.' Users are randomly assigned to the experiences, and key metrics are computed and compared." / "Controlled experiments can transform decision making into a scientific, evidence-driven process-rather than an intuitive reaction." / "The best data scientists follow Twyman's law: any figure that looks interesting or different is usually wrong."

**[26] Aakash Gupta, "How to Create a Product Prototype: A PM's Guide to De-Risking Your Roadmap".** practitioner. **fetched-and-verified.**
`https://www.aakashg.com/how-to-create-a-product-prototype/`
Supports: Who commissions a prototype (the PM), what it is for versus a PRD, and what document takes over once the prototype has answered its question
Quotable: "Before you write a single line of a Product Requirements Document (PRD), you need a prototyping strategy. As a Product Manager, your job isn't just to build; it's to de-risk." / "A prototype is your fastest path to answering these crucial questions...helping you move quickly without committing expensive engineering resources to the wrong thing." / "Once you've ironed out the critical issues that stop users from getting value, you have enough signal to start development."

**[27] Steven P. Dow, Alana Glassco, Jonathan Kass, Melissa Schwarz, Daniel L. Schwartz, Scott R. Klemmer - "Parallel Prototyping Leads to Better Design Results, More Divergence, and Increased Self-Efficacy" (ACM Transactions on Human-Computer Interaction 17(4), 2010).** primary. **fetched-and-verified.**
`https://hci.stanford.edu/publications/2010/parallel-prototyping/ParallelPrototyping2010-submitted.pdf`
Supports: Empirical (peer-reviewed, N=33 between-subjects experiment) evidence that iterating serially on a single prototype produces worse outcomes and more defensive reaction to critique than exploring multiple prototypes in parallel; also documents the single-prototype social-desirability bias in user feedback via the cited Tohidi et al. finding
Quotable: "Iteration can help people improve ideas. It can also give rise to fixation -- continuously refining one option without considering others." / "As measured by click-through data and expert ratings, ads created in the Parallel condition significantly outperformed those from the Serial condition." / "In post-task interviews, nearly half of serial participants reported negative reactions to critique of their prototypes; no Parallel participants reported this." / "designers make poor choices to justify prior investments in money or time" / "Tohidi et al. revealed that potential users of interactive systems withhold critique when presented with a single prototype; the users were concerned about offending the designer. More importantly, Tohidi et al. showed that the presence of multiple alternative concepts gave users license to be more critical."

**[28] Bradley Camburn, Vimal Viswanathan, Julie Linsey, David Anderson, Daniel Jensen, Richard Crawford, Kevin Otto, Kristin Wood - "Design prototyping methods: State of the art in strategies, techniques, and guidelines" (Design Science, vol. 3, 2017).** primary. **fetched-and-verified.**
`https://www.cambridge.org/core/journals/design-science/article/design-prototyping-methods-state-of-the-art-in-strategies-techniques-and-guidelines/560B306A5E799AEE54D30E0D2C1B7063`
Supports: A systematic literature review's own assessment of the empirical evidence base for prototyping's effectiveness: it exists and is positive for iteration and parallel prototyping specifically, but the review explicitly flags that broader claims (value of information, contextual factors, systems prototyping) are comparatively unexplored, and that low-fidelity prototypes carry their own risk of misleading results
Quotable: "Empirical studies show that teams iterating on a design significantly outperform teams without iteration" / "Controlled experiments show that groups producing prototypes in parallel produce designs that significantly outperform groups producing a single design" / "the value of information, contextual factors, and systems prototyping are relatively less explored" / "may misrepresent physical principles and must be evaluated with caution"

**[29] Rikke Friis Dam and Yu Siang Teo - "6 Common Pitfalls in Prototyping and How to Avoid Them" (Interaction Design Foundation).** practitioner. **fetched-and-verified.**
`https://ixdf.org/literature/article/prototyping-in-design-thinking-how-to-avoid-six-common-pitfalls`
Supports: Named-author practitioner enumeration of the sunk-cost/attachment failure mode (endowment effect) and the absence-of-purpose failure mode (testing without a defined question), independent of the academic sources, corroborating both
Quotable: "overly invested in the success" / "a central purpose"
