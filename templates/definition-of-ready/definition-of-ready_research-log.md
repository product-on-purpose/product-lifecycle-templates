# definition-of-ready: research log

Research conducted 2026-09-23 in two passes: an admission sweep run while the spec was written, and the build's
six-dimension fan-out (origins and admission, contents and structure, the dispute, boundaries, practice and
failure, and the standing gap question). **33 sources are recorded below: 30 fetched-and-verified, two
url-confirmed-not-read and one not-retrieved.** Only `fetched-and-verified` sources are quoted anywhere in this
bundle.

**Every quotation in this log was checked against the source's raw text**, not against the summary a retrieval
tool returns. Pages were downloaded directly (HTML decoded as UTF-8, PDFs through `pdftotext` without
`-layout`) and each quotation searched for as a normalized substring. Two Scrum.org pages refuse plain HTTP
clients; they were read through a rendering browser, stored as rendered page text, and that stored text was
inspected to confirm it is the page (navigation, byline and ratings included), not a summary of it.

---

## What the checks caught, and what was not read

**The spec's brief named the wrong paper for "ready-ready", and the check caught it before the spec shipped.**
The coinage is in Jakobsen and Sutherland [3]; the earlier Sutherland, Jakobsen and Johnson paper on Scrum and
CMMI does not contain the string. This build then found a second thing the spec did not know: [1] names the
state "Ready-Ready" too, so there are two practitioner lineages for the phrase, and neither cites the other.

**A practitioner page carried another author's words.** [25] quotes Mountain Goat Software's "it moves the team
dangerously close to stage-gate process" and "A stage-gate approach is, after all, another way of describing a
waterfall process". Both are in [14], which is where this bundle attributes them.

**The spec said no source bridges a definition of ready and testing's entry criteria. One does.** The ISTQB
glossary mirror [21] lists "definition of ready" among the translations and synonyms of "entry criteria". The
spec is corrected in place; the companion reports the synonym, and that the mirror is not ISTQB's own site.

**Not read, and nothing in this bundle may rest on them:**

- **Barry Overeem's "The (dis)advantages of a Definition of Ready"** on Medium [31], which returned 403.
- **PMI Disciplined Agile's page on ways to use a definition of ready** [32], which returned a bot-block page.
- **Jeff and J. J. Sutherland's "Scrum: The Art of Doing Twice the Work in Half the Time" (2014)** [33], a
  print book [2] cites for a chapter on readiness. Not retrieved.

---

## The admission record

**ADR 0030's test is met at the practitioner and pattern tier, several times over.** [1] (1 October 2008)
publishes a definition of ready as a list: "So, the definition of Ready should be;" followed by six criteria,
and names the resulting state: "Let's call this state "Ready-Ready"." [2], the Scrum Patterns Group's pattern,
credits it with a hedge the bundle keeps: "Richard Kronfält apparently published the first formal description of
Definition of Ready in 2008." [7], Microsoft's playbook, publishes one as a page with its own sections, under
CC BY 4.0 [8]. [6] and [12] define the type by name.

**The two standards that could have admitted it decline to.** The 2020 Scrum Guide [4] never uses the phrase;
its nearest sentence is "Product Backlog items that can be Done by the Scrum Team within one Sprint are deemed
ready for selection in a Sprint Planning event." SAFe's glossary [5] defines the Definition of Done and has no
entry for a Definition of Ready. [12] says it outright: "While the definition of done (DoD) is part of scrum, a
definition of ready (DoR) is an external and optional tool".

**This family's named citation hazard is "folklore presented as standard", and "a definition of ready is part of
Scrum" is that folklore exactly.** The companion says plainly that neither Scrum's nor SAFe's own text names it.

---

## Claims flagged contested or time-bound

**Whether a definition of ready should exist: three positions, and no source holds a fourth.**

1. **Against a rigid one, not against the idea.** [14]: "Avoid including rules that require something be 100
   percent done before a story is allowed into the iteration", and "Favor guidelines rather than rules on your
   Definition of Ready". [14] also says "for most development teams, I do not recommend using a definition of
   ready". [17]: "a rigid DoR used like a phase-gate can just as easily undermine agility". [16] quotes Stefan
   Roock: "For the Definition of Ready I recommend: The smaller the better".
2. **Against a named, standing artifact.** [19]: "I'm not a big fan of the Definition of Ready. Quite often it
   becomes a contract - instead of a guideline - between the Development Team and the Product Owner", with its
   replacement: "Instead of using the Definition of Ready as a sequential, phase-gate checklist I prefer the
   activity of Backlog Refinement." [15]: a definition of ready "reduces agility because it breaks up process
   flow, assumes greater role specific responsibilities, introduces more wait states (delay) and potentially
   undermines business-value based prioritisation". Both concede ground: [19] "I do support using a checklist
   that clarifies 'readiness' during backlog refinement" and [15] "I might even recommend it myself but I'd hope
   it was an temporary measure on the way to something better".
3. **It depends.** [20]: "Is Definition of Ready obligatory in Scrum? The answer is short: no", and "Definition
   of Ready can be weaponized and it can become a threat to your Agility", with the decision handed back to the
   team.

**No source read argues for a rigid, growing, non-negotiable definition of ready.** The dispute runs from
abolition to "keep it small"; there is no opposite pole, and the companion must not invent one for balance.

**[18] is a passing remark, not a position.** Its one sentence ("Notions like "Definition of Ready" can seem to
support this idea") is about a product owner handing work down; the bundle does not cite Ron Jeffries as a critic.

**Whether INVEST is a definition of ready.** [9] presents the six INVEST criteria as a DoR's components. [11], the
origin of INVEST, never uses the phrase "Definition of Ready". [10] uses its own three: "clear", "feasible" and
"testable". **The template offers the questions criteria ask, not either list.**

**Who owns it.** [10] "I suggest that the definition of ready (DOR) is jointly owned by the product owner and the
team"; [9] "Remember that the DoR is created for the team, by the team"; [29] "agreed by the whole Scrum team";
[7] "The ready checklist can be written by a Product Owner in agreement with the development team and the
Process Lead". [27] names what goes wrong when one role owns it: "the Definition of Ready is used as an argument
and reason for rejecting backlog items".

**Where the "ready-ready" name came from.** [1] names the state; [3] credits Systematic: "Systematic introduced the
term ready-ready, to express that work from the Product Backlog has been sufficiently elaborated to be allocated
to a sprint for implementation." [3]'s venue and year (Agile 2009) come from its filename and bibliographies, not
its text. **Two lineages, unsequenced**; the companion records both and picks neither.

**No measured evidence exists in what was read.** No study or survey measuring a definition of ready's effect on
flow or predictability was found. Every effect claimed in this log is a practitioner's account, and the bundle
says so.

---

## Notes for the companion

**The honest framing.** A definition of ready is optional, contested, and absent from the frameworks people assume
it comes from. **The bundle teaches a small, team-owned one written as guidelines, and treats keeping none as a
legitimate outcome**, which is where every source that is not against it lands.

**The evidentiary spine:**

1. **That the type exists, and where:** [1], [2], [7]; declined by [4] and [5].
2. **The dispute:** [14], [15], [16], [17], [19], [20].
3. **What it contains, as questions:** [7], [9], [10], [11], [12].
4. **Where it is used:** at refinement, as its success test ([29]: "Refinement results in product backlog items
   that are ready for development, and the Definition of Ready is the criteria by which we can say that
   refinement has been successful"), and at sprint planning ([4]).
5. **What happens to a top item that is not ready:** [26], [15], [17], [28].
6. **How it is revised:** [7], [9], [10], [12], [17].

**The section design, as the research moved it from the spec.** Five sections, single size. **The spec's shape
held**; the research strengthened two sections and took one claim of the spec's own away from it.

| Section | What the research did to it |
|---|---|
| **Why We Keep One** | **Now sourced, not only the library's contribution.** [14] gives the reason a team keeps one ("The goal is to prevent problems before they have a chance to start"), and [15] gives the other half, a reason to stop ("I'd hope it was an temporary measure on the way to something better", the source's own typo kept). **No source states a condition for retiring one**; the section asks the team to state its own, labelled as this bundle's contribution |
| **Scope and Ownership** | Joint ownership, with [27]'s warning about one role owning it. Applied at refinement [29] and confirmed at sprint planning [4]. [7]: "The ready checklist should contain items that apply broadly" |
| **Readiness Criteria** | Each criterion is a question with a stated consequence of a miss. [14] gives the TRAP (any "100 percent" rule), and [22] what a stage gate is, which a criterion like that turns the document into. **One hard stop has a source**: [14] names "the possible exception of dependencies on certain teams or vendors", the only case it allows a firm rule |
| **When an Item Is Not Ready** | **Now sourced from four directions**: [26] "If an item doesn't fully meet the Definition of Ready but the Scrum team believes it can be completed within a Sprint, it is acceptable to pull it into the Sprint"; [15] make it ready as the first task; [17] "Let the team override it with a quick, documented decision"; [28]'s risk-based exception |
| **Review Trigger** | **Bidirectional, and both directions now have a source.** Too loose: [7] "Update or change the definition of ready anytime the scrum team observes that there are missing information in the user stories that recurrently impacts the planning", and [9]'s signs of scrambling mid-sprint. Too tight: [17] "When the DoR blocks more value than it enables, it stops being a safety rail and becomes a parking brake". The spec labelled the second direction the library's own; [17] states it, so the label comes off |

**Teaching points the template, guide and example must stay consistent with:**

- **A definition of ready is optional and absent from the Scrum Guide and SAFe's glossary; keeping none is a
  legitimate outcome.**
- **Criteria are guidelines that start a conversation, with at most a few hard stops, each justified.**
- **It fails in both directions: too loose lets unready work in, too tight blocks work the team could have done.**
- **A top-priority item that misses it has a stated way in.**
- **It should get shorter as the team matures** ([16]'s Roock: it "should be shrinking over time and not
  growing").
- **It is owned by the team that applies it**, not imposed by one role on another.

**What this bundle must not say:** that a definition of ready is part of Scrum or SAFe; that it improves
predictability or flow by any measure; that INVEST is the definition of ready; that Ron Jeffries argues against
it; that anyone argues for a rigid one; which lineage coined "ready-ready"; anything from the three unread
sources below.

**The example.** The Reporting Squad's first definition of ready, which must make a sentence the family already
wrote come true: `definition-of-done_example.md` says "if the squad adopts a Definition of Ready later, it will
gate entry into the sprint, not exit from it, and will not replace anything above." So it is dated after that
example's last update, 2026-07-24, and its sprint numbers follow the thread's two-week cadence (Sprint 24 ran
2026-07-13 to 2026-07-24, and the planning session that opened Sprint 25 is where that example's 2026-07-24
amendment was adopted, still with no definition of ready). **Its reason for existing must come from a
real event in the thread**, and the natural one is `SV-5`, the sharing story, whose permissions dependency
(`D-02` in the epic, "Confirmed, integration pending") is exactly the cross-team dependency [14] allows as a hard
stop. It must agree with the Saved Views items' recorded states in the `product-backlog`, `epic` and
`sprint-backlog` examples, and it must be short. It must not reproduce [7]'s, [9]'s or [2]'s lists.

**The pairing.** `pairs_with: []`: the one pm-skills candidate, `iterate-refinement-notes`, never mentions a
definition of ready.

---

## Sources

**[1] Richard Kronfält - "Ready-ready: the Definition of Ready for User Stories going into sprint planning", Scrum FTW (blog), 1 October 2008.** practitioner (blog). **fetched-and-verified.**
`https://scrumftw.blogspot.com/2008/10/ready-ready-definition-of-ready-for.html`
Supports: The earliest verified instance of a definition of ready published as a list, and its name for the state.
Quotable: "So, the definition of Ready should be;" / "Let's call this state "Ready-Ready"."
Contested/time-bound: No licence stated. Priority over [3]'s lineage is not established.

**[2] The Scrum Patterns Group - "Definition of Ready" pattern, scrumbook.org (companion site to "A Scrum Book", Pragmatic Bookshelf, 2019).** practitioner (pattern language). **fetched-and-verified.**
`https://scrumbook.org/value-stream/product-backlog/definition-of-ready.html`
Supports: A named group publishing the type as a pattern, and its hedged attribution of the first description.
Quotable: "Richard Kronfält apparently published the first formal description of Definition of Ready in 2008."
Contested/time-bound: The attribution is hedged ("apparently") in the source; the bundle keeps the hedge. All rights reserved.

**[3] Carsten Ruseng Jakobsen and Jeff Sutherland - "Scrum and CMMI - Going from Good to Great: Are you ready-ready to be done-done?" (PDF at jeffsutherland.com).** academic (conference paper). **fetched-and-verified.**
`http://jeffsutherland.com/scrum/JakobsenScrumCMMIGoingfromGoodtoGreatAgile2009.pdf`
Supports: A second lineage for the "ready-ready" name, credited to Systematic's practice.
Quotable: "Systematic introduced the term ready-ready, to express that work from the Product Backlog has been sufficiently elaborated to be allocated to a sprint for implementation."
Contested/time-bound: Its venue and year (Agile 2009) come from the filename and bibliographies, not the text.

**[4] Ken Schwaber and Jeff Sutherland - "The 2020 Scrum Guide".** primary (framework definition). **fetched-and-verified.**
`https://www.scrumguides.org/scrum-guide.html`
Supports: That the Scrum Guide never names a definition of ready; its readiness and refinement sentences.
Quotable: "Product Backlog items that can be Done by the Scrum Team within one Sprint are deemed ready for selection in a Sprint Planning event." / "Product Backlog refinement is the act of breaking down and further defining Product Backlog items into smaller more precise items." / "This publication is offered for license under the Attribution Share-Alike license of Creative Commons"
Contested/time-bound: CC BY-SA 4.0. The phrase "Definition of Ready" does not occur in it.

**[5] Scaled Agile, Inc. - SAFe Glossary.** vendor (framework glossary). **fetched-and-verified.**
`https://framework.scaledagile.com/glossary`
Supports: That SAFe's glossary defines the Definition of Done and has no entry for a definition of ready.
Quotable: "The Definition of Done specifies the requirements for completeness of a work product or increment of value."
Contested/time-bound: Proprietary.

**[6] Agile Alliance - "Definition of Ready", glossary entry.** reference (glossary). **fetched-and-verified.**
`https://www.agilealliance.org/glossary/definition-of-ready/`
Supports: A named body defining the type, and its purpose of letting a team decline ill-defined work.
Quotable: "provides the team with an explicit agreement allowing it to "push back" on accepting ill-defined features"
Contested/time-bound: All rights reserved.

**[7] Microsoft - "Definition of Ready", Code-With Engineering Playbook.** practitioner (engineering playbook). **fetched-and-verified.**
`https://microsoft.github.io/code-with-engineering-playbook/agile-development/team-agreements/definition-of-ready/`
Supports: The most template-shaped published definition of ready: what it is, example checklist items, who writes it, when to update it, and what to avoid; the one source whose licence permits adapting its wording.
Quotable: "Definition of Ready is the agreement made by the scrum team around how complete a user story should be in order to be selected as candidate for estimation in the sprint planning" / "The ready checklist can be written by a Product Owner in agreement with the development team and the Process Lead" / "Update or change the definition of ready anytime the scrum team observes that there are missing information in the user stories that recurrently impacts the planning" / "The ready checklist should contain items that apply broadly. Don't include items or details that only apply to one or two user stories."
Contested/time-bound: CC BY 4.0 per the repository's licence file [8]. Its older URL now returns 404.

**[8] Microsoft - code-with-engineering-playbook repository, LICENSE file.** reference (licence file). **fetched-and-verified.**
`https://raw.githubusercontent.com/microsoft/code-with-engineering-playbook/main/LICENSE`
Supports: That [7] is licensed Creative Commons Attribution 4.0.
Quotable: "Attribution 4.0 International"

**[9] Atlassian - "What is Definition of Ready? DoR Explained & Key Components".** vendor. **fetched-and-verified.**
`https://www.atlassian.com/agile/project-management/definition-of-ready`
Supports: A vendor presenting INVEST as a definition of ready's components; team ownership; a revision signal.
Quotable: "Remember that the DoR is created for the team, by the team" / "If you notice the team is regularly not completing all their work in a sprint, or there is a lot of scrambling to understand work within the sprint, it likely means your Definition of Ready needs to be reviewed and updated"
Contested/time-bound: Equates INVEST with a definition of ready, which [10] and [11] do not.

**[10] Roman Pichler - "The Definition of Ready in Scrum".** practitioner. **fetched-and-verified.**
`https://www.romanpichler.com/blog/the-definition-of-ready/`
Supports: A three-criterion model (clear, feasible, testable), joint ownership, and revision in retrospectives.
Quotable: "I suggest that the definition of ready (DOR) is jointly owned by the product owner and the team" / "A story is clear if all Scrum team members have a shared understanding of what it means" / "A story is feasible if it can be completed in one sprint, according to the definition of done" / "An item is testable if there is an effective way to determine if the functionality works as expected" / "I recommend starting with a good-enough DOR and adapting it in the sprint retrospectives if and when necessary"

**[11] Bill Wake - "INVEST in Good Stories, and SMART Tasks", xp123.com.** practitioner. **fetched-and-verified.**
`https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/`
Supports: The origin of INVEST as a story-quality heuristic. It never uses the phrase "Definition of Ready", so it is cited for INVEST only.
Quotable: "Stories are easiest to work with if they are independent" / "A good story is testable"

**[12] Scrum Alliance - "Definition of Ready vs. Definition of Done: Understanding the Differences".** practitioner (certifying body). **fetched-and-verified.**
`https://resources.scrumalliance.org/Article/definition-vs-ready`
Supports: The definition of ready as optional and outside the Scrum Guide; its difference from the definition of done and from acceptance criteria; extrinsic example items.
Quotable: "While the definition of done (DoD) is part of scrum, a definition of ready (DoR) is an external and optional tool" / "The definition of done refers to the PBI itself, while the definition of ready often refers to externalities" / "The definition of done applies to all work in the backlog. Contrast this with acceptance criteria, which are unique to each PBI" / "No blockers have been found that cannot be addressed by the team during the sprint"

**[13] Applied Frameworks - "A Definition of Ready for PI Planning".** vendor (consultancy). **fetched-and-verified.**
`https://appliedframeworks.com/a-definition-of-ready-for-pi-planning/`
Supports: A published definition of ready one level above the story, for SAFe PI Planning; a consultancy's extension, not a SAFe artifact.
Quotable: "Your PI Planning Definition of Ready will likely revolve around two things: features and knowledge"

**[14] Mountain Goat Software (Mike Cohn's company) - "Definition of Ready: What It Is and Why It's Dangerous".** practitioner. **fetched-and-verified.**
`https://www.mountaingoatsoftware.com/agile/the-dangers-of-a-definition-of-ready`
Supports: The case against a rigid definition of ready (a stage gate), guidelines over rules, the one named exception (dependencies on other teams or vendors), and the reason a team keeps one.
Quotable: "If these rules include saying that something must be 100 percent finished before a story can be brought into an iteration, the definition of ready becomes a huge step towards a sequential, stage-gate approach" / "Avoid including rules that require something be 100 percent done before a story is allowed into the iteration" / "Favor guidelines rather than rules on your Definition of Ready" / "the possible exception of dependencies on certain teams or vendors" / "The goal is to prevent problems before they have a chance to start" / "for most development teams, I do not recommend using a definition of ready" / "it moves the team dangerously close to stage-gate process" / "A stage-gate approach is, after all, another way of describing a waterfall process"
Contested/time-bound: No byline on the page; attributed to the company.

**[15] Allan Kelly - "Definition of Ready considered harmful" (2017).** practitioner. **fetched-and-verified.**
`https://www.allankelly.net/archives/1615/definition-of-ready-considered-harmful/`
Supports: The case against a definition of ready as a practice, its concession, and making a not-ready item ready as the first task.
Quotable: "reduces agility because it breaks up process flow, assumes greater role specific responsibilities, introduces more wait states (delay) and potentially undermines business-value based prioritisation" / "I can see why teams adopt definition of ready and I might even recommend it myself but I'd hope it was an temporary measure on the way to something better" / "then the first task is to make it ready" / "The definition of done at the end of one activity is the definition of ready for the next"

**[16] Ben Linders - "Using Definition of Ready", InfoQ (2014).** practitioner (news). **fetched-and-verified.**
`https://www.infoq.com/news/2014/06/using-definition-of-ready`
Supports: Practitioners for and against, including Stefan Roock's case for a small definition of ready that shrinks.
Quotable: "For the Definition of Ready I recommend: The smaller the better" / "should be shrinking over time and not growing" / "the Definition of Ready may be used to create an over regulated process that impedes collaboration" / "This is NOT Scrum and it is NOT Agile"
Contested/time-bound: A news piece quoting others; attributed per speaker.

**[17] Lance Dacy - "Definition of Ready: Guardrail or Roadblock?", Big Agile (3 June 2025).** practitioner. **fetched-and-verified.**
`https://big-agile.com/blog/definition-of-ready-guardrail-or-roadblock`
Supports: The named middle position, a documented team override, and the signal that a definition of ready has become too tight.
Quotable: "a rigid DoR used like a phase-gate can just as easily undermine agility" / "a clarity compass, not a compliance document" / "Let the team override it with a quick, documented decision" / "When the DoR blocks more value than it enables, it stops being a safety rail and becomes a parking brake"

**[18] Ron Jeffries - "Dark Scrum: Hills: The Backlog".** practitioner. **fetched-and-verified.**
`https://ronjeffries.com/articles/018-01ff/ds-hills-backlog/`
Supports: nothing beyond a passing remark. Consulted; its one mention is incidental to a different argument, so the bundle does not cite Jeffries as a critic.

**[19] Barry Overeem - "Why isn't the Definition of Ready described in the Scrum Guide?", Scrum.org blog (5 September 2016).** practitioner. **fetched-and-verified.**
`https://www.scrum.org/resources/blog/why-isnt-definition-ready-described-scrum-guide`
Supports: The case for refinement instead of a standing definition of ready, and its concession.
Quotable: "I'm not a big fan of the Definition of Ready. Quite often it becomes a contract - instead of a guideline - between the Development Team and the Product Owner" / "Instead of using the Definition of Ready as a sequential, phase-gate checklist I prefer the activity of Backlog Refinement" / "So why isn't the Definition of Ready described in the Scrum Guide? Because it is. However not as a checklist but as an activity: backlog refinement." / "I do support using a checklist that clarifies ‘readiness’ during backlog refinement"
Contested/time-bound: An individual author's post on Scrum.org, not Scrum.org policy. Read through a rendering browser.

**[20] Joanna Płaskonka - "Ready or Not? Demystifying the Definition of Ready in Scrum", Scrum.org blog (27 September 2023).** practitioner. **fetched-and-verified.**
`https://www.scrum.org/resources/blog/ready-or-not-demystifying-definition-ready-scrum`
Supports: The explicit "it depends" position, and the definition of ready as optional in Scrum.
Quotable: "Is Definition of Ready obligatory in Scrum? The answer is short: no" / "Definition of Ready can be weaponized and it can become a threat to your Agility"
Contested/time-bound: An individual author's post, not Scrum.org policy. Read through a rendering browser.

**[21] ISTQB Glossary (unofficial mirror) - "Entry Criteria".** reference (glossary mirror). **fetched-and-verified.**
`https://istqb-glossary.page/entry-criteria/`
Supports: Testing's entry criteria, and that the mirror lists "definition of ready" among its synonyms, catalogued against the Agile Tester syllabus.
Quotable: "The set of generic and specific conditions for permitting a process to go forward with a defined task, e.g., test phase." / "definition of ready"
Contested/time-bound: A mirror stating it is based on the official ISTQB glossary, not ISTQB's own site; whether the synonym reflects ISTQB policy is unconfirmed.

**[22] Robert G. Cooper (Stage-Gate International) - "The Stage-Gate Model: An Overview".** primary. **fetched-and-verified.**
`https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/`
Supports: What a stage gate is, for the boundary: a governance decision on readiness and value, taken above the team.
Quotable: "They include both project readiness and project value" / "an explicit decision point where the business must choose whether and how to continue investing" / "Go, Kill, Hold, or Recycle"

**[23] Debashish Chakrabarty - "Definition of Done, Definition of Ready and Acceptance Criteria are not the same darn thing", The Agile Chronicles.** practitioner. **fetched-and-verified.**
`https://agilechronicles.substack.com/p/definition-of-done-definition-of`
Supports: The three-way boundary between a definition of done, a definition of ready and acceptance criteria.
Quotable: "the DoD focuses on quality and ensures a consistent, releasable standard for all work; the DoR aims to improve Product Backlog clarity and prevent unprepared work from entering the Sprint; and the Acceptance Criteria focus on specific functionality and ensure individual Product Backlog Items (PBIs) meet stakeholder needs"

**[24] Agile Alliance - "What is Backlog Refinement (or Backlog Grooming)?", glossary entry.** reference (glossary). **fetched-and-verified.**
`https://agilealliance.org/glossary/backlog-refinement/`
Supports: Refinement as the activity and a definition of ready as the criteria it aims at.
Quotable: "Definition of Ready involves creating clear criteria that a user story must meet before being accepted into an upcoming iteration"

**[25] Jasti Smythe - "Is the Definition of Ready (DoR) Outdated?", Agile Guru.** practitioner. **fetched-and-verified.**
`https://agileguru.substack.com/p/is-the-definition-of-ready-dor-outdated`
Supports: A practitioner definition. Its stage-gate sentences quote [14] and are attributed there.
Quotable: "Definition of Ready describes the requirements that must be met in order for a story to move from the backlog to development"

**[26] RebelScrum - "Ready or Not!".** practitioner. **fetched-and-verified.**
`https://www.rebelscrum.site/post/ready-or-not`
Supports: A team that refused an urgent item for missing its definition of ready, and the norm that it may still be pulled in.
Quotable: "The Definition of Ready is an optional practice and shouldn't be as strictly enforced as the Definition of Done" / "If an item doesn't fully meet the Definition of Ready but the Scrum team believes it can be completed within a Sprint, it is acceptable to pull it into the Sprint"

**[27] t2informatik - "What is a Definition of Ready?", Smartpedia.** vendor. **fetched-and-verified.**
`https://t2informatik.de/en/smartpedia/definition-of-ready/`
Supports: What goes wrong when one role owns it: it becomes grounds for rejecting work; the alternative of treating it as an agenda.
Quotable: "the Definition of Ready is used as an argument and reason for rejecting backlog items" / "a basis for discussion or a kind of agenda"

**[28] Box UK - "Definition of ready in agile".** vendor. **fetched-and-verified.**
`https://www.boxuk.com/insight/definition-of-ready-in-agile/`
Supports: Introducing one experimentally, firmer for new teams, and the warning against irreversible phases.
Quotable: "experiment by using the construct on a project, inspect its impact on the project, and adapt your approach accordingly" / "Inexperienced teams may be advised to consider the Definition of Ready as mandatory, at least to begin with" / "it is definitely not the intention to promote hard and fast, cannot-go-back phases of development, as this removes agility"

**[29] Boldare - "Definition of Ready and Backlog Refinement Process".** vendor (software company). **fetched-and-verified.**
`https://www.boldare.com/blog/definition-of-ready-and-backlog-refinement-process/`
Supports: A definition of ready as refinement's success test; whole-team agreement; unclear criteria as a revision signal.
Quotable: "Refinement results in product backlog items that are ready for development, and the Definition of Ready is the criteria by which we can say that refinement has been successful" / "The DoR differs according to the type of backlog item under consideration and is agreed by the whole Scrum team" / "if a Definition of Ready is at all unclear, you need to revisit the refinement process"

**[30] agility.ac - "What is a definition of ready?", Frequent Agile Questions.** practitioner. **fetched-and-verified.**
`https://agility.ac/frequent-agile-questions/what-is-a-definition-of-ready`
Supports: Criteria as a guideline to consider, not a gate; a living document owned by the whole team.
Quotable: "a checklist of things to consider, rather than a stage gate" / "the definition of ready should be collaboratively created and agreed upon by the whole team and be seen as a living document that grows with the team as they mature"

**[31] Barry Overeem - "The (dis)advantages of a Definition of Ready", The Liberators (Medium).** practitioner. **url-confirmed-not-read.**
`https://medium.com/the-liberators/the-dis-advantages-of-a-definition-of-ready-e1c96937cb69`
Supports: nothing in this bundle. Returned 403.

**[32] Project Management Institute - Disciplined Agile, "Definition of Ready and different ways to use it".** practitioner. **url-confirmed-not-read.**
`https://www.pmi.org/disciplined-agile/definition-of-ready-and-different-ways-to-use-it`
Supports: nothing in this bundle. Returned a bot-block page.

**[33] Jeff Sutherland and J. J. Sutherland - "Scrum: The Art of Doing Twice the Work in Half the Time" (2014).** practitioner (book). **not-retrieved.**
No URL: a print book cited by [2] for a chapter on readiness; no retrievable text was attempted, and a bookseller link would imply a retrieval that did not happen.
Supports: nothing in this bundle.
