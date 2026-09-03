# Research log: epic

Built for the `epic` bundle (delivery-docs family, seventh member, admitted by
[ADR 0042](../../docs/internal/decisions/0042-epic-joins-delivery-docs.md)) to the methodology section 6
honest-retrieval standard. Sources were gathered by a six-dimension research fan-out (origins and canon,
published field sets, methodology lineage and absences, live debates, relationships and tooling, and the
standing gap question), each doing real WebSearch and WebFetch. Every source below is tagged with its tier
and retrieval status; **only sources marked fetched-and-verified may be quoted verbatim** in the companion,
and each verbatim phrase used is listed here.

Thirty sources, twenty-nine fetched and verified, one url-confirmed-not-read and carrying no claim of its
own. Six sources were owned by two dimensions each; every one is a single entry here, with the fuller
extract kept. Three further sources returned 403 or an empty body and were dropped rather than cited: a
Scrum.org forum thread, an Ivar Jacobson International piece, and a Medium article. **No claim in this
bundle rests on any of them.**

Research date: 2026-09-02. Catalog ref: 31.

---

## One alteration to quoted text, stated rather than made silently

Six of the sources below use an em-dash inside a phrase this bundle quotes. This repository bans em-dashes
and en-dashes in every tracked file, enforced by check B per bundle and by a repo-wide sweep in CI, so the
character cannot appear here even inside quotation marks. **Every such quote has had the em-dash replaced
with a spaced hyphen and nothing else changed.** No word, order, or punctuation beyond that character has
been altered.

This is recorded because silently editing a verbatim quotation is precisely the failure this library's
citation discipline exists to prevent, and a reader comparing a quote here against its source deserves to
know the one mechanical difference they will find. The affected entries are 12, 23, 27, 29 and 30.

---

## Honest framing (the through-line for the companion)

**An epic is a container of stories whose written content carries the context that the stories cannot
carry themselves: why this body of work exists, who it serves, and how it ladders up to the larger effort
above it.** That is this library's position, and it is a choice among live alternatives rather than a
neutral summary. The rest of this section says what the choice is choosing between, because a reader who
does not know that will not understand why the template asks what it asks.

**The founding definition is much thinner than what everyone now means, and the divergence is documented
by the founder himself.** Mike Cohn's *User Stories Applied* (2004) is the first durable published
definition, and it is one sentence: *"When a story is too large it is sometimes referred to as an epic.
Epics can be split into two or more stories of smaller size"* [14]. That epic is **singular** - one
oversized story, destined to be split and then to disappear from the backlog. The Agile Alliance glossary
dates the origin the same way [16]. Cohn does not claim he coined it; he attributes it to *"the XP teams
that invented user stories"* [15], and no fetched source gives a date or document for that informal
coinage, so 2004 is the date of first published definition and not of first use.

**The modern meaning is the container, and Cohn flags it as a departure he did not author:** *"Jira, for
example, uses epic to mean a group of user stories rather than a single, big user story. I do not know if
this was a mistake on their part or not"* [15]. Every tracker examined implements the container sense, not
the 2004 sense. This bundle teaches the container, because that is what practitioners actually have in
front of them, and it says plainly that the founding text meant something narrower.

**Four of the five methodologies surveyed have no epic at all, and each absence is a different substitution.**

| Method | Treatment |
|---|---|
| Scrum (2020 Guide) | **Absent.** Zero occurrences of "epic", confirmed by literal string search over the raw fetched HTML [17]. One flat Product Backlog plus refinement, which is *"the act of breaking down and further defining Product Backlog items into smaller more precise items"* [17]. The nearest container is the Product Goal, a *"future state of the product"* [17], which is a target rather than a groupable unit |
| XP | **Absent.** No container artifact; a time-box rule on the story instead: *"Longer than 3 weeks means you need to break the story down further"* [18] |
| Kanban Method | **Absent, and flatter than Scrum.** No product-specific work unit at all; *"request"*, *"card"* and *"work item"* used generically [19] |
| LeSS Huge | **Absent as "epic".** Partitions the one backlog by customer concern into Requirement Areas, *"a categorization of the requirements leading to different views of the Product Backlog"* [20], which is an orthogonal axis rather than a size tier |
| SAFe | **Present and heavily formalized.** *"An Epic is a significant solution development initiative"* [21], requiring *"an MVP, a Lean business case, and an estimate of costs"* [21], approved by Portfolio Leadership, with a named accountable Epic Owner role [22] |

**This is the same shape as this library's PRD finding, one level down.** `prd` had to record that Scrum
recognizes no PRD and routes requirement capture through the Product Backlog. `epic` records that Scrum
recognizes no epic either, and for the same structural reason: Scrum-lineage and pull-system methods keep
the vocabulary flat and push the question of size into an ongoing activity, while SAFe is the outlier that
formalizes a discrete artifact with a role and a gate around it. **A reader who works in Scrum, XP or
Kanban is using a word their own framework does not define**, and the guide should say so without telling
them to stop.

**In its native habitat the epic is a record, not a document, and the bundle must not pretend otherwise.**
Jira, Azure Boards, GitLab, Linear and Aha! all publish an epic as a form of typed fields on a work-item
panel, with no publisher-defined prose sections [1][2][3][4][5][7][8][9], and Linear has no construct
named Epic at all, its nearest analog being the Project [6]. Azure Boards is explicit that
adding one means filling fields such as Value Area, Business Value, Time Criticality and Target Date [1].
The only epic-level reporting found anywhere is Jira's Epic Burndown, and it is a rollup chart computed
from child-story estimates and team velocity [3], never a narrative status.

**Two named sources do publish prose, and they are the precedent this bundle actually rests on.**
ProductPlan's *How to Write an Epic* prescribes written parts rather than fields: a title, a narrative in
the form *"As the [persona], I want to [objective] so that [value]"*, an instruction to *"jot down the
scope of work for this epic - in other words, the boundaries"*, and acceptance criteria [23]. And SAFe's
**Lean Business Case** is a genuine multi-section document, per Atlassian's own template page, carrying
Business Outcomes Hypothesis, Leading Indicators, Scope Definition, MVP Definition, In Scope, Out of Scope,
Cost Estimate and a Go/No-Go Recommendation, with the Epic Hypothesis Statement sitting inside it as one
section [12]. **So when an epic is written as a document, it is written as a business case.**

**That fact draws this bundle's sharpest boundary.** This library already ships `business-case`, and its
companion already records that SAFe substitutes an Epic Hypothesis Statement and leading indicators for a
financial case. The epic bundle therefore does **not** template cost estimates, value return, or a go/no-go
recommendation. It templates the container and its context. The line is: **a business case argues for an
investment; an epic groups the work and explains what it is in service of.**

**The layer above the epic is real in tools and absent from methodologies, and the template must not
assert it as universal.** "Initiative" above epic is a vendor construct: Tempo records that *"many
entities (including Atlassian) incorporate a layer above the Jira epic called an initiative"* [26], which
places the tier in Atlassian practice rather than in any method. **Whether that tier is gated behind a paid
Jira licence was reported by search summary only and never fetched, so this log does not claim it.** Aha!
defines its own Initiative > Epic > Feature ladder independent of Scrum and SAFe vocabulary [27], and Tempo frames the
choice between Initiative > Epic > Story and SAFe's Epic > Feature > Story as a genuine unresolved decision
between tool pragmatism and framework alignment [26]. SAFe itself has no initiative tier; it has
Epic > Feature > Story, with Capability inserted in Large Solution SAFe [10]. **The template may point
upward; the guide must say the thing above you may be called an initiative, a theme, or nothing at all.**

---

## Sources (curated, deduplicated, contiguously numbered; one source per entry)

**[1] Microsoft Learn - Define features and epics to organize backlog items (Azure Boards).** primary. **fetched-and-verified.**
`https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/define-features-epics?view=azure-devops`
Supports: Azure DevOps epic work-item fields and their definitions, and the portfolio-backlog hierarchy of epic over feature over backlog item. Load-bearing for the record-not-document finding.
Quotable: "Value Area - The area of customer value addressed by the epic, feature, or backlog item."; "Business Value - Specify a priority that captures the relative value of an Epic, Feature, or backlog item compared to other items of the same type. The higher the number, the greater the business value."; "Time Criticality - A subjective unit of measure that captures how the business value decreases over time. Higher values indicate that the Epic or Feature is inherently more time critical than those items with lower values."; "Target Date - Specify the date by which to implement the feature."; "Epic: An epic is a large body of work that can be broken down into multiple features. It represents a major initiative or goal and might span several sprints or even releases."

**[2] Microsoft Learn - About work items and work item types (Azure Boards).** primary. **fetched-and-verified.**
`https://learn.microsoft.com/en-us/azure/devops/boards/work-items/about-work-items?view=azure-devops`
Supports: the formal four-level work-item hierarchy statement, and confirmation that every level including the epic is a work-item form with fields rather than a freestanding document.
Quotable: "Work item types form a hierarchy: Epics group Features, Features group Requirements (User Stories, Product Backlog Items, Issues, or Requirements), and Requirements group Tasks. You connect items across the hierarchy with parent-child links."; "The work item form displays the fields you use to track information for each work item."

**[3] Atlassian Support - View and understand the epic burndown report.** primary. **fetched-and-verified.**
`https://support.atlassian.com/jira-software-cloud/docs/view-and-understand-the-epic-burndown-report/`
Supports: the only form of epic-level reporting found across any tool surveyed, and that its arithmetic is derived entirely from child-story estimates and team velocity rather than from any narrative the epic carries.
Quotable: "The Epic Burndown report shows you how your team is progressing against the work for an epic."; "Predict how many sprints it will take to complete the work for an epic, based on past sprints and changes during the sprints"; "Predicted sprints are calculated based on your team's velocity (amount of work completed in the last three sprints), and the total work remaining for the epic."

**[4] GitLab Docs - Manage epics.** primary. **fetched-and-verified.**
`https://docs.gitlab.com/user/group/epics/manage_epics/`
Supports: the GitLab epic record field list, including the multi-assignee and date behaviours and the three-value health status enum.
Quotable: "An epic can be assigned to one or more users"; "Select a start and due date, or inherit them"; "On track (green), Needs attention (amber), At risk (red)"

**[5] GitLab Docs - Epics overview.** primary. **fetched-and-verified.**
`https://docs.gitlab.com/user/group/epics/`
Supports: GitLab epic scheduling fields, and the single piece of evidence found anywhere that a tool lets teams impose prose structure on an epic, which it does by convention through templates rather than by shipping sections.
Quotable: "Track the progress of related work items with scheduled start and end dates."; "Create epic templates...to standardize epic descriptions."

**[6] Linear Docs - Projects.** primary. **fetched-and-verified.**
`https://linear.app/docs/projects`
Supports: that Linear has no construct literally named Epic, its nearest analog being the Project, which is evidence that even the container noun is not universal across tools.
Quotable: "the only required field is the project name"; "Projects can be shared across multiple teams"

**[7] Aha! Support - Get Started With Epics in Aha! Roadmaps.** vendor. **fetched-and-verified.**
`https://support.aha.io/aha-roadmaps/support-articles/features/epics-introduction`
Supports: the Aha! epic record fields, its scoring and progress-rollup mechanics, and its epic-to-feature hierarchy; also the clearest vendor statement that an epic groups by shared objective.
Quotable: "Epics are used to group features that often share a common business objective."; "Add/Delete progress field"

**[8] Atlassian Support - What is an epic? (Jira Software Cloud).** primary. **fetched-and-verified.**
`https://support.atlassian.com/jira-software-cloud/docs/what-is-an-epic/`
Supports: that Jira's own epic landing page enumerates no field list, and that Epic is a renameable work type rather than a fixed concept in the product.
Quotable: "Epic is the default name, but you can rename it and the functionality remains the same"

**[9] Atlassian Support - Manage epics in a scrum space (Jira Software Cloud).** primary. **fetched-and-verified.**
`https://support.atlassian.com/jira-software-cloud/docs/manage-epics-in-a-scrum-project/`
Supports: the Epic Status and Parent fields named operationally, with no consolidated field-list section anywhere on the page.
Quotable: "Epic Status field"; "Locate the Parent field"

**[10] Morne Wiggins, Agility at Scale - SAFe Epics: Strategic Portfolio Initiatives.** practitioner. **fetched-and-verified.**
`https://agility-at-scale.com/safe/lpm/epics/`
Supports: the SAFe hierarchy variants and why the Large Solution variant inserts a level; the Epic Hypothesis Statement as a deliberate alternative to acceptance criteria; the MVP as a pivot-or-persevere test rather than a milestone; Lean Portfolio Management as the named approval authority; and closure defined as hypothesis validation rather than work completion.
Quotable: "the hierarchy is Epic → Feature → Story"; "Epic → Capability → Feature → Story"; "when multiple ARTs coordinate on a single solution, feature-level granularity is too fine for cross-train governance and epic-level granularity is too coarse"; "a falsifiable scientific hypothesis, not a fill-in-the-blank form"; "Done marks hypothesis validation: the epic's benefit hypothesis has been tested and the outcome measured"; "the minimum investment required to test the epic's benefit hypothesis with sufficient confidence to make a pivot-or-persevere decision"; "the individual accountable for shepherding an epic through the entire Portfolio Kanban system; from Funnel through Done"

**[11] Agility at Scale - SAFe Epics (hypothesis statement page).** practitioner. **fetched-and-verified.**
`https://agility-at-scale.com/safe/epics/`
Supports: the exact Epic Hypothesis Statement sentence template and its seven named slots, and the observation that the measurable-outcome slot is the one teams most often fill badly.
Quotable: "For [target customer] who [need or opportunity], the [epic name] is a [solution type] that [benefit]. Unlike [current alternative], our solution [differentiator]. We will know we are successful when [measurable outcome with leading indicators]."; "the most commonly mistreated field"
Contested/time-bound: this is a practitioner explainer, not Scaled Agile Inc.'s own text. The official page was paywalled past its public summary, so the seven-slot template and the falsifiable-hypothesis framing are recorded on practitioner authority and should not be attributed to Scaled Agile Inc. directly.

**[12] Atlassian - SAFe lean business case template (Confluence templates).** vendor. **fetched-and-verified.**
`https://www.atlassian.com/software/confluence/templates/safe-lean-business-case`
Supports: **the strongest evidence in this log that an epic is ever written as a multi-section prose document.** The Lean Business Case carries named narrative sections (Epic Name and Description, Business Outcomes Hypothesis, Leading Indicators, Scope Definition, MVP Definition, In Scope, Out of Scope, Nonfunctional Requirements, Epic Hypothesis Statement, Cost Estimate, Value Return, Solution Analysis, Notes and Comments, Go/No-Go Recommendation) and wraps the short hypothesis sentence rather than replacing it. It is also the boundary this bundle refuses to cross, since the costing and recommendation sections belong to `business-case`.
Quotable: "Short and concise way to define the business rationale, or the 'why' of this Epic"
Contested/time-bound: this is Atlassian's rendering of a SAFe artifact, not Scaled Agile Inc.'s own publication of it. The section list is Atlassian's template, and a SAFe practitioner may see a different one.

**[13] Atlassian Community - Solved: Epic and summary (forum thread).** practitioner. **url-confirmed-not-read.**
`https://community.atlassian.com/forums/Jira-questions/Epic-and-summary/qaq-p/2094723`
Supports: nothing in this bundle. Listed because it was consulted while checking whether Jira's Epic Name and Summary are distinct fields, a claim that is carried by [9] instead. **The body was not read, so no claim rests on it and it is not quoted.**

**[14] Mike Cohn - User Stories Applied: For Agile Software Development.** primary (book). **fetched-and-verified.**
`https://athena.ecs.csus.edu/~buckley/CSc191/User-Stories-Applied-Mike-Cohn.pdf`
Supports: the founding dated definition of "epic"; the compound and complex splitting taxonomy; and the earliest published attribution of "theme" to Kent Beck. Read as full text extracted from the PDF, whose verso confirms copyright 2004 by Pearson Education, Inc., ISBN 0-321-20568-5.
Quotable: "When a story is too large it is sometimes referred to as an epic. Epics can be split into two or more stories of smaller size."; "Even though they are too big to estimate reliably, it is sometimes useful to write epics such as \"A Job Seeker can find a job\" because they serve as placeholders or reminders about big parts of a system that need to be discussed."; "Epics typically fall into one of two categories: The compound story, The complex story"; "A compound story is an epic that comprises multiple shorter stories."; "A product development roadmap can be as simple as a list of the main areas of focus, or themes as Kent Beck calls them, for each of the next few releases."

**[15] Mike Cohn - Epics, Features and User Stories (Mountain Goat Software).** practitioner. **fetched-and-verified.**
`https://www.mountaingoatsoftware.com/agile/stories-epics-and-themes`
Supports: Cohn's present-day restatement of the taxonomy; his attribution of both "epic" and "theme" to the XP teams rather than to himself or to Scrum; his statement that Scrum says nothing about any of these terms; and his flagging of Jira's container usage as a departure from the original meaning. Used only for present-day and attribution claims. The page's embedded JSON-LD, read from the fetched HTML, gives datePublished 2022-11-08 and dateModified 2025-04-28, so this is a maintained restatement and is **not** evidence of the 2004 wording, which is carried by [14].
Quotable: "As defined by the XP teams that invented user stories, an epic is a large user story. There's no magic threshold at which we call a particular story an epic."; "The team that invented user stories used the word theme to mean a collection of user stories."; "Remember that the Scrum framework doesn't say anything about epics, stories, and themes. These terms come from XP."; "Jira, for example, uses epic to mean a group of user stories rather than a single, big user story. I do not know if this was a mistake on their part or not."; "One more term worth defining is feature. This term was not used by the original user stories team, which has led to feature being applied to different things in different organizations and teams."

**[16] Agile Alliance - What is an Epic? (Agile Glossary).** standards. **fetched-and-verified.**
`https://agilealliance.org/glossary/epic/`
Supports: third-party confirmation of the 2004 origin and originating publication; a neutral working definition; and the observation that themes are not normally a backlog-hierarchy level, which matters because the catalog lists Theme among epic's relationships.
Quotable: "An epic is a large user story that cannot be delivered as defined within a single iteration or is large enough that it can be split into smaller user stories."; "2004: Mike Cohn introduced the concept of an epic as a large user story in his book User Stories Applied For Agile Software Development."; "You may also see the concept of themes used for grouping user stories dealing with the same topic. ... Themes are typically not used as a level in a backlog hierarchy."

**[17] Scrum.org / Ken Schwaber and Jeff Sutherland - The 2020 Scrum Guide.** primary. **fetched-and-verified.**
`https://scrumguides.org/scrum-guide.html`
Supports: **that the Scrum Guide contains zero occurrences of the word "epic"**, confirmed by literal string search over the raw fetched HTML with tags stripped, not by an LLM summary. Also that Scrum routes all requirement capture through the Product Backlog and refinement, with no size-tier vocabulary above a Product Backlog item, and that the Product Goal is a directional target rather than a groupable container.
Quotable: "The Product Backlog is an emergent, ordered list of what is needed to improve the product. It is the single source of work undertaken by the Scrum Team."; "Product Backlog refinement is the act of breaking down and further defining Product Backlog items into smaller more precise items. This is an ongoing activity to add details, such as a description, order, and size."; "The Product Goal describes a future state of the product which can serve as a target for the Scrum Team to plan against."

**[18] Don Wells - User Stories (ExtremeProgramming.org).** practitioner. **fetched-and-verified.**
`http://www.extremeprogramming.org/rules/userstories.html`
Supports: that XP has no epic term at all, confirmed by literal search of the fetched page; and that XP's only decomposition mechanism is a time-box rule applied to the story itself. Also that XP frames the story as a replacement for a requirements document rather than a tier beneath one.
Quotable: "They are also used instead of a large requirements document."; "Each story will get a 1, 2 or 3 week estimate in \"ideal development time\"."; "Longer than 3 weeks means you need to break the story down further. Less than 1 week and you are at too detailed a level, combine some stories."

**[19] David J. Anderson School of Management - Revisiting the Principles and General Practices of the Kanban Method.** practitioner. **fetched-and-verified.**
`https://djaa.com/revisiting-the-principles-and-general-practices-of-the-kanban-method/`
Supports: that the canonical restatement of the Kanban Method contains zero occurrences of "epic", verified by literal string search on the fetched and tag-stripped HTML, and that the Method's vocabulary for a unit of work is generic rather than product-specific. This is a stronger absence than Scrum's, which at least names a Product Backlog item.
Quotable: "Visualize each request with a card on a kanban board."; "The flow of work items through each stage in the workflow should be monitored and reported"

**[20] LeSS.works (Craig Larman and Bas Vodde) - Requirement Areas (LeSS Huge).** primary. **fetched-and-verified.**
`https://less.works/less/less-huge/requirement-areas`
Supports: that LeSS has no epic concept, and that its scaling device is a categorization axis over one flat backlog rather than a new artifact tier above the item. This is the architectural opposite of SAFe's move and is the sharpest contrast available for the companion's lineage section.
Quotable: "A requirement area is a categorization of the requirements leading to different views of the Product Backlog."; "groups every Product Backlog item under exactly one requirement category - its requirements area"; "generates different views on the overall Product Backlog - called an Area Backlog"

**[21] Scaled Agile, Inc. - Epic (SAFe framework article).** vendor. **fetched-and-verified.**
`https://framework.scaledagile.com/epic/`
Supports: SAFe's own epic definition, the business and enabler split, and the requirement for an MVP, a Lean business case and Portfolio Leadership approval. This is the only framework source that treats the epic as a first-class governed artifact.
Quotable: "An Epic is a significant solution development initiative."; "An epic is a substantial business venture with significant scope and impact."; "Business epics deliver value directly to the customer. Enabler epics enhance the architectural runway to support future business or technical needs."; "Each epic requires an MVP, a Lean business case, and an estimate of costs."; "they're managed through a portfolio's Kanban system. This enables visibility and tracking of their development until they are approved or rejected."
Contested/time-bound: the page is paywalled past its public summary. Deeper sections on Lean Startup mechanics, cost and duration forecasting, and Agile Release Train specifics were visible only as headings behind a login wall and are **not** claimed here.

**[22] Scaled Agile, Inc. - Epic Owners (SAFe extended guidance).** vendor. **fetched-and-verified.**
`https://framework.scaledagile.com/epic-owner/`
Supports: the Epic Owner role, which no other framework surveyed has any equivalent of, and its duties across the business case, the MVP definition, the Portfolio Kanban and the Agile Release Trains.
Quotable: "The Epic Owner is responsible for coordinating epics through the portfolio Kanban system."; "Epic Owners (EO) work collaboratively with stakeholders to define the Epic, the Lean business case, and the definition of a Minimum Viable Product (MVP) and are responsible for shepherding the epic through the portfolio Kanban system."; "Enterprise Architects typically act as Epic Owners for Enabler epics."
Contested/time-bound: same paywall caveat as [21]; only public-summary text was retrieved.

**[23] ProductPlan - How to Write an Epic (for Product Managers).** practitioner. **fetched-and-verified.**
`https://www.productplan.com/learn/how-to-write-an-epic`
Supports: **the clearest named-source precedent for writing an epic as prose rather than as fields.** It prescribes a title, a narrative in persona form, an explicit scope-boundary step written as a distinct activity, and acceptance criteria as the completion gate. It still frames the output as feeding a tool's epic record rather than as a standalone document, which is stated here rather than glossed.
Quotable: "a clear, concise title"; "a short description of what you hope to achieve with the epic"; "As the [persona], I want to [objective] so that [value]"; "jot down the scope of work for this epic - in other words, the boundaries"; "a clear set of acceptance criteria - the high-level list of requirements your team will need to approve"

**[24] Kent McDonald - Epic Confusion (Agile Alliance).** practitioner. **fetched-and-verified.**
`https://agilealliance.org/epic-confusion/`
Supports: the naming of the competing meanings as a genuine and unresolved dispute, and the skeptical case against the container model earning its overhead. This is the source that lets the companion present the debate rather than flatten it.
Quotable: "Epic has taken on a variety of different meanings over the course of the last 16 years."; "It's difficult to tell whether having a separate thing, as opposed to a bigger version of the same thing, actually furthers that goal."; "now when people say 'epic' you have to figure out whether they are talking about SAFe epics"; "Spend more time talking about the items on your backlog and less time categorizing and documenting them."

**[25] Bertil Muth - Epics are dead. Here's what we should do instead. (freeCodeCamp).** practitioner. **fetched-and-verified.**
`https://www.freecodecamp.org/news/epics-are-dead-heres-what-we-should-do-instead-279bada1e644/`
Supports: the never-closing-bucket failure mode named directly, and the abolitionist position that the fix is to dissolve the epic into a story attribute rather than to discipline it. The strongest published argument against this bundle existing, which is why it is here.
Quotable: "The backlog becomes bloated. It contains epics that you don't need any more."; "what you lose is the ordered list of the backlog. How do you determine the implementation order then?"; "A theme can be thought of as an additional attribute of the stories. Normally, several stories share the same theme."

**[26] Tempo - SAFe hierarchy: Epic-Feature-Story vs Initiative-Epic-Story?** vendor. **fetched-and-verified.**
`https://www.tempo.io/blog/which-safe-hierarchy-should-you-choose`
Supports: that the layer above the epic is a live and unresolved choice rather than a settled fact, and specifically that the initiative tier is an Atlassian and Jira convention rather than a SAFe one.
Quotable: "Jira natively comes with a very useful epic link between stories and epics, and many entities (including Atlassian) incorporate a layer above the Jira epic called an initiative."; "You might prioritize being in alignment - that is, sharing the same vocabulary - with the Scaled Agile literature and all the classes your team will follow"

**[27] Brian de Haaff - Initiatives vs. Epics vs. Features: What Is the Difference? (Aha!).** vendor. **fetched-and-verified.**
`https://www.aha.io/blog/initiatives-vs-epics-vs-features`
Supports: a third competing hierarchy, Initiative over Epic over Feature, defined independently of both Scrum and SAFe vocabulary. Three vendor hierarchies that disagree is the evidence for the guide's warning that the tier above the epic is named by tooling rather than by method.
Quotable: "Major areas of investment that contain epics or high-level themes of delivery needed to achieve specific goals."; "Larger bodies of work that are comprised of many features"; "Specific capabilities or functionality that you deliver to end-users - problems you solve that add value."

**[28] David J. Anderson - Tyranny of the Timebox Revisited (DJAA).** practitioner. **fetched-and-verified.**
`https://djaa.com/tyranny-of-the-timebox-revisited/`
Supports: the flow camp's case that large work should be constrained by work-in-progress limits rather than by time.
Quotable: "You cannot scale Agile using timeboxed sprints!"; "Fine-grained requirements analysis coupled to short timeboxed sprints introduces a dependency management problem."; "Instead of limiting the time, limit the WIP, use a constant work-in-progress (CONWIP) limit."
Contested/time-bound: **this piece never mentions epics.** Connecting it to how epics should be governed is an inference drawn by the research, not a claim Anderson makes. The companion may use it for the flow-versus-timebox debate and may not attribute an epic-specific position to him.

**[29] Ryan Singer - The Circuit Breaker, Shape Up (Basecamp).** practitioner. **fetched-and-verified.**
`https://basecamp.com/shapeup/2.2-chapter-08`
Supports: a named methodology's explicit, published abandonment mechanism for a large unit of work, with the decision sitting at a recurring review rather than left implicit. Shape Up's project is analogous to an epic in scope, and the analogy is this library's rather than Singer's.
Quotable: "The amount of time we want to spend on a project, as opposed to an estimate."; "A risk management technique: Cancel projects that don't ship in one cycle by default instead of extending them by default."; "We intentionally create a risk that the project - as pitched - won't happen."

**[30] Agility at Scale - SAFe Dependencies Assessment.** practitioner. **fetched-and-verified.**
`https://agility-at-scale.com/safe/requirements-model/safe-dependencies-assessment/`
Supports: recording a dependency with more structure than a link, specifically classification by type and severity and a mandatory owner on each side. This is the sourced basis for the dependency section asking more than a tracker's link field does.
Quotable: "Classify each dependency by type (knowledge, technical, process) and severity (blocking versus informational)."; "Every dependency gets an owner on both sides - the requesting team and the providing team. Unowned dependencies are invisible dependencies in disguise."

---

## Claims flagged contested or time-bound

1. **Is an epic a big story or a different kind of object?** The oldest and deepest split. Cohn and the XP lineage say a large story with *"no magic threshold"* [15]; SAFe says *"a significant solution development initiative"* requiring a business case [21]. McDonald names the split and doubts the second camp earns its overhead [24]. **This bundle takes the container side and says so; it does not claim the question is settled.**

2. **Should an epic carry acceptance criteria or a hypothesis?** SAFe departs from acceptance criteria in favour of a falsifiable hypothesis [10][11]; ProductPlan uses acceptance criteria [23]; the Cohn lineage has no closure artifact for epics at all because the epic is not distinct enough from a story to need one [15].

3. **Are epics an anti-pattern?** Muth argues the container model produces bloated backlogs of epics nobody needs and should be abolished [25]. SAFe's answer to the same failure is an evidence-based Done rather than removal [10]. **Both camps agree the failure is real; they disagree on the fix.**

4. **What sits above the epic.** Three vendor hierarchies disagree: Jira and Atlassian use Initiative over Epic over Story with the initiative tier available only in paid Plans [26], Aha! uses Initiative over Epic over Feature [27], and SAFe uses Epic over Feature over Story with Capability added at Large Solution scale [10]. No source claims one is correct.

5. **Timeboxing epics.** Anderson's flow argument [28] is adjacent, not about epics. Flagged above and not to be attributed to him as an epic-specific claim.

6. **The Epic Hypothesis Statement's provenance.** The seven-slot template and the falsifiable-hypothesis framing come from a practitioner explainer [11], not from Scaled Agile Inc.'s own page, which was paywalled [21]. Attribute to the explainer.

7. **The Lean Business Case section list** is Atlassian's rendering [12], not Scaled Agile Inc.'s publication.

8. **Theme as a hierarchy level.** The catalog lists Theme among epic's relationships, but the Agile Alliance glossary records that themes are *"typically not used as a level in a backlog hierarchy"* [16], and Cohn defines a theme as a collection of stories rather than a tier [15]. The companion should not present Theme as a rung.

---

## Notes for the companion

**The honest framing** is the section above; do not restate it, build on it.

**The load-bearing sections** are the context and laddering sections, because they are the only reason to write an epic as a document rather than open a ticket. Everything a tracker already does well, it should keep doing; this template earns its place only where prose beats fields.

**The sharpest teaching points, in order:**

1. **Your framework probably does not define this word.** Four of five surveyed have no epic [17][18][19][20]. That is not a reason to stop, but a reader should know they are using tool vocabulary, not method vocabulary.
2. **The founding definition is one sentence and means something narrower than you do** [14][15].
3. **An epic that never closes is the documented failure mode** [25], and the two published answers are opposite: kill the artifact [25], or give it an evidence-based Done [10].
4. **Write the exclusions, not just the scope** [23], and give every dependency an owner on both sides [30].
5. **The boundary against `business-case` is the costing and the recommendation.** If the document is arguing for an investment, it is a business case [12].

**Gap-question candidates**, routed through decision procedure 12 and **not** automatically template sections: outcome stated as a testable prediction with a leading indicator [11]; a scheduled pivot-or-persevere checkpoint [10]; an explicit default-to-cancel rule with a named decision venue [29]; classified dependencies with two-sided ownership [30]. **A null result was not returned on this dimension**; four candidates were, each tied to a named published source.
