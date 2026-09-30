---
title: "{{project_name}} Project Brief"
project_name: "{{project_name}}"
author: "{{author}}"
approver: "{{approver}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: project-brief
size: lean
source_template: project-brief
source_template_version: 0.1.0
---

<!--
LEAN PROJECT BRIEF. The shortest form that still asks for real authority to start: where the
project comes from, what it must achieve, what is explicitly out of scope, an outline of why it is
worth doing, the constraints and people involved, and the decision being requested. Use it to ask a
named decision maker for authority to begin initiation, before anyone commits to delivering
anything. To grow it into a brief that also states the delivery approach and where it sits against
other documents, see project-brief_template-full.md. ADD sections after Decision Requested; never
rename or reorder the ones below, because the full variant is a strict ordered superset of this one.

STAYS SHORT AT EITHER SIZE. Unlike this library's business-case bundle, where the full variant adds
real financial weight, this bundle's full variant stays short too: prince2.wiki's own quality bar is
"short, focused," and Smartsheet's stronger claim is that the whole document "should be a single
page long, and anyone should be able to understand it at a glance." Length guidance is otherwise
inconsistent across the sources this bundle read, from a paragraph to a few pages, and no source
measured length against outcome. Scale to your own project rather than treating any one figure as a
rule. See project-brief_companion.md section 4.

WHAT A PROJECT BRIEF IS, AND IS NOT
It asks for authority to start finding out whether and how to proceed, before anyone commits to
building anything. It is NOT a business case (a full comparison of options and a funded
recommendation; this document carries only an outline of that case and defers the comparison, per
business-case_guide.md:17). It is NOT a project charter or a project initiation document, called a
PID (this library's POSITION: those authorize delivery once initiation is approved, and neither is
built in this library). It is NOT a product brief (which scopes a single product opportunity, where
this document scopes a whole initiative or project; this boundary is labeled inferred, since no
source read for this bundle draws it explicitly). It is NOT a creative or design brief (a different
discipline entirely). It is NOT a Project Canvas (the
same kind of content in a one-page diagram, a difference of medium, not of content). It is NOT a
project proposal or a one-page pitch (this library's POSITION: a pitch sells a decision not yet
made, while this document records a mandate that already exists and asks for authority to explore
it further). A separate, heavyweight sense of the name, published by NSW Health, the Treasury Board
of Canada and Ireland's National Transport Authority, is large, iterative and revised across a
project's whole life; this bundle does not build that document. See project-brief_companion.md
section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   project-brief_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to
   avoid. For the tables, PRIORITY explains the ordering rule and ROW HINT says what a good row
   contains.
2. Replace each {{placeholder}} with your content. Name the approver in the frontmatter and mean it:
   this document is not finished until a real person has agreed to decide.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you send this for a decision: self-grade against project-brief_guide.md, then DELETE every
   HTML comment. They are guidance, not content.
-->

# {{project_name}} Project Brief

## Background and Mandate

<!-- WHAT  Where the project comes from, the mandate that triggered it, and why it needs to start
           now rather than later.
     WHY   BIS names the trigger precisely: start-up begins when a senior manager "agrees/decides to
           take responsibility for a new initiative that might best be run as a project," arriving
           from business planning, an external driver, or "identification of a significant problem
           that cannot be dealt with as a matter of routine." The mandate itself is, in BIS's own
           phrase, "often as simple as an email," so this section's job is to make that trigger
           legible to a reader who was not in the room when it was decided. Deep dive:
           project-brief_companion.md section 3 (Anatomy > Background and Mandate).
     ASK   Where did this project come from, and who issued the mandate? What form did it take, a
           conversation, an email, a formal memo? Why does it need to start now rather than later?
           What happens if nothing changes?
     GOOD  "Mandate: verbal instruction from the COO at the 2026-07 operations review, following
           three consecutive quarters of rising checkout abandonment. Why now: the pattern is
           worsening each quarter, and the holiday peak arrives in twelve weeks, after which a fix
           could not ship before the season that matters most."
     WEAK  "We think this would be a good idea." (no mandate, no source, and no reason the timing
           matters)
     TRAP  Skipping the mandate and writing only the background. A brief with no named mandate reads
           as something the project manager invented, not something a decision maker actually asked
           for. -->

- Mandate and background: {{mandate_and_background}}
- Why now: {{why_now}}

## Objectives

<!-- WHAT  What the project must achieve, stated so a reader can tell later whether it did.
     WHY   BIS's own start-up checklist calls for objectives that are "achievable and measurable
           (SMART)," and prince2.wiki repeats SMART as the brief's own quality bar. How firmly
           sources hold that bar varies: Oxford City Council's template asks for it only "wherever
           possible," one practitioner source states it as a flat requirement ("Avoid vague verbs
           like improve, optimise or streamline, because nobody can tell when they are done"), and
           at least one published template carries no measurability wording for this field at all.
           Treat SMART as the convergent recommendation, not a universal rule every published
           template enforces. Deep dive: project-brief_companion.md section 3 (Anatomy >
           Objectives).
     ASK   What must this project achieve to be judged complete and successful? How will you know,
           concretely, whether each objective was met? Is each one stated as an outcome rather than
           an activity?
     PRIORITY  Order objectives by how central each is to the mandate above. A brief carrying many
           objectives at this size is probably several projects wearing one brief.
     ROW HINT  A good row states an outcome a reader could check later, and names what checking it
           would look like. A weak row is an activity, or a vague verb, with nothing to measure.
     GOOD  | OBJ-1 | Cut checkout abandonment on the self-checkout lanes from 14% to under 8% |
           Weekly abandonment rate from point-of-sale logs, measured for four weeks after launch |
     WEAK  | OBJ-1 | Improve the self-checkout experience | |
     TRAP  Writing an activity, "build queue alerts," instead of an outcome, "cut abandonment to
           under 8%." An activity tells you the project shipped; only an outcome tells you it
           worked. -->

| ID | Objective | How you will know it succeeded |
|---|---|---|
| {{objective_id}} | {{objective_statement}} | {{objective_measure}} |

## Scope and Exclusions

<!-- WHAT  What is in scope, including the deliverables, and what is explicitly out, as its own
           named field rather than folded into a general paragraph.
     WHY   BIS's own start-up checklist item is exactly this pairing, "Scope - what in and what's
           out," and Oxford City Council gives the exclusion half a numbered heading of its own, "3
           Project Scope and Exclusions," prompting "What is outside the remit of the project?"
           Deliverables belong on the in-scope side: BIS's own contents list names "Deliverables,"
           and Oxford City Council carries a matching deliverables section of its own. Several
           sources recommend naming exclusions specifically because an unwritten boundary invites
           disputes later; none of them measured whether writing one actually reduces scope creep,
           and this section does not repeat that as a measured fact. Deep dive:
           project-brief_companion.md section 3 (Anatomy > Scope and Exclusions), section 7
           (anti-patterns).
     ASK   What deliverables are in scope? What is explicitly out, that someone might otherwise
           assume is included? What would you say to a stakeholder who asked for something on the
           excluded list?
     GOOD  In scope: "Self-service queue-length alerts on the four busiest self-checkout lanes,
           shown on the existing overhead displays." Exclusions: "Staffed-lane queueing is
           explicitly out of scope; this project does not touch cashier scheduling or staffing
           levels."
     WEAK  In scope: "Improve checkout." Exclusions: (left blank)
     TRAP  Leaving exclusions blank because nothing seems worth excluding yet. An unwritten boundary
           is not a small boundary, it is one nobody has agreed to yet, and the dispute arrives
           later instead of now. -->

- In scope and deliverables: {{in_scope_and_deliverables}}
- Explicitly out of scope: {{exclusions}}

## Outline Business Justification

<!-- WHAT  Why this project is worth doing, in outline only, an illustrative estimate of time and
           cost, and a named pointer to where the full comparison of options happens.
     WHY   prince2.wiki names "outline business case" as one item in its own composition list for
           the brief, and prince2.ca states plainly that in PRINCE2 "the creation of the business
           case (in outline form) is part of the project brief." This library's own business-case
           guide states the boundary from its own side: "a project brief absorbs an outline business
           case as one component and retires once initiation documentation exists; the business
           case itself keeps being refined, it does not retire with the brief"
           (business-case_guide.md:17). This section carries the outline only; it does not attempt
           the fuller comparison of options, including doing nothing, that a business-case document
           brings to a later decision. Deep dive: project-brief_companion.md section 3 (Anatomy >
           Outline Business Justification), section 6 (the business-case nesting debate).
     ASK   Why is this worth doing? Who benefits, and how? What is an illustrative, not final,
           estimate of the time and cost involved? What later document, and what decision gate, will
           bring the fuller comparison of options?
     GOOD  "Reduces checkout abandonment, the retailer's second-largest source of lost sales per the
           Q2 operations review. Illustrative estimate: roughly six engineer-weeks and no new
           hardware, to be confirmed. A full comparison against alternatives, including doing
           nothing, will be brought to a business case at the September funding review."
     WEAK  "This will definitely pay for itself many times over." (no comparison named, no estimate,
           no pointer to where the real case gets made)
     TRAP  Treating this section as the finished business case. A brief that tries to settle the
           comparison of options itself has stepped outside its own boundary; that comparison
           belongs to a business-case document, not here. -->

- Why this is worth doing: {{outline_justification}}
- Outline estimate, illustrative and not final: {{outline_estimate}}
- Full comparison of options deferred to: {{business_case_reference}}

## Constraints and Who Should Be Involved

<!-- WHAT  Known constraints and dependencies on the work, brief notes on risks and assumptions,
           and the people who need to be part of it.
     WHY   BIS states the pairing directly in its own summary sentence, "the Project Brief says why
           the project is needed, what it must achieve and who should be involved," and separately
           lists constraints, stakeholders and dependencies among the brief's contents. AXELOS's own
           glossary names constraints as part of the standards-body definition itself. Risks and
           assumptions belong here too, as a line or two each rather than a formal register:
           prince2.wiki's own composition list names "risks," and its starting-up page describes the
           brief as covering "the scope, objectives, risks, and approach," which is also where
           prince2.wiki names "project management team structure" as part of what the wider process
           assembles into the brief. A formal risk-scoring table stays out of a document this size;
           that belongs to the heavyweight public-sector sense this bundle does not build. Deep
           dive: project-brief_companion.md section 3 (Anatomy > Constraints and Who Should Be
           Involved).
     ASK   What constraints, and what dependencies on other work, apply here? What are the known
           risks and assumptions, in a line or two each? Who needs to be involved, and why, beyond
           the approver named in the frontmatter?
     PRIORITY  List every person whose absence would stop the project cold, not everyone who might
           be interested. A stakeholder with no stated reason for being on the list probably should
           not be.
     ROW HINT  A good row names a real person or role, and states in a few words why they need to be
           involved. A weak row is a job title with no stated reason.
     GOOD  | Ines Draper | VP, Store Operations | Owns the budget and the overhead-display hardware
           this project depends on |
     WEAK  | IT | | |
     TRAP  Listing a whole department as one row. "Engineering" is not a stakeholder; the specific
           person or role who owns the decision or the dependency is. -->

- Constraints and dependencies: {{constraints_and_dependencies}}
- Known risks and assumptions: {{risks_and_assumptions}}

| Name | Role | Why involved |
|---|---|---|
| {{stakeholder_name}} | {{stakeholder_role}} | {{stakeholder_reason}} |

## Decision Requested

<!-- WHAT  The decision being asked for, who is being asked, and what happens to the answer.
     WHY   prince2.wiki states the decision plainly, the brief "is used by the project board to make
           the first key decision: whether to authorise the initiation stage," and its own
           starting-up page names the request itself as that process's final output, "to send a
           request to the project board to initiate the project." BIS lists what the approvers are
           confirming when they sign off, ending with a commitment to plan rather than to build:
           they are willing to provide the project manager with the time and resources "needed to
           plan the project in detail and to produce the Project Initiation Document (PID)." One
           practitioner source frames approval itself as what changes the document's status: "A
           brief that is filled in but never approved is a wish list, not a mandate; the signature
           is what turns it into permission to start," and another puts the same instruction more
           bluntly, "Get it approved by the decider, out loud." This section also carries the
           discovery-docs family contract's own obligation: every member must say, in its
           companion, what document takes over once the decision is made; naming that document
           here, and recording the approver's own answer, is this library's own structural choice.
           Deep dive: project-brief_companion.md section 3 (Anatomy > Decision Requested), section 6
           (what approval actually authorizes).
     ASK   What decision are you asking for, proceed to a business case, proceed straight to
           initiation, or stop? What document takes over once the decision is made? Has the person
           named as approver in the frontmatter actually agreed to decide, not just to be copied?
     GOOD  "Decision requested: authorize proceeding to a full business case. Next document: a
           business-case draft, due before the September funding review. Approved by Ines Draper,
           VP Store Operations, out loud at the 2026-08-04 operations sync, not left as an email
           nobody replied to."
     WEAK  "Please take a look and let us know your thoughts." (no decision named, no next document,
           and no approver who has actually agreed to decide)
     TRAP  Circulating a brief for comment without ever naming a decision or a decider. A brief that
           nobody approves is a wish list, not a mandate, whatever else it contains. -->

- Decision requested: {{decision_requested}}
- Approver: {{approver}}
- Next document once decided: {{next_document}}
