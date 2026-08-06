---
title: "{{persona_name}} User Persona"
persona_name: "{{persona_name}}"
persona_role: "{{persona_role}}"
product_or_team: "{{product_or_team}}"
owner: "{{owner}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: user-persona
size: lean
source_template: user-persona
source_template_version: 0.1.0
---

<!--
LEAN USER PERSONA. The smallest persona that is still a real one: who this person is, what they are actually
trying to do, and what gets in their way, each grounded in research rather than invention. Use it to give a
design conversation a specific person to argue from, before you have the interview count or workshop time for
Context of Use, Scenarios, and a declared evidence tier (see user-persona_template-full.md). To grow it into
the full variant, ADD sections after Pains and Barriers; never rename or reorder the ones below, because the
full variant is a strict superset of this one.

WHAT A USER PERSONA IS, AND IS NOT
It says who a product is being built for, grounded in research rather than in invention. It is NOT a buyer
persona (a different artifact answering the purchase decision, not product use), NOT an anti-persona (the
customer type you deliberately do not want, published as its own sibling document once a positive persona
exists), NOT a market segment (a strategic, faceless grouping tool used once a strategy exists, where this is
a tactical, single-character tool used early), and NOT an empathy map (a single-session workshop canvas,
structurally distinct even though the two are often used together). See user-persona_companion.md section 8.

EVERY PERSONA CARRIES AN HONEST EVIDENCE FLOOR, EVEN THIS ONE. This lean variant does not ship a declared
evidence-tier field, but that does not exempt it from having one honestly in mind: if this persona is built
from assumptions rather than interviews, say so out loud when you share it, the same way the full variant's
Evidence Basis section requires in writing. See user-persona_companion.md section 3 (Anatomy > Evidence
Basis) and section 4 (Variants and sizing).

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into user-persona_
   companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid. For tables,
   PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Every goal and every pain needs an evidence column filled
   in with where you actually learned it, not what the product team assumes.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This document should be revisited as your understanding of this person changes, not filed once and
   forgotten. Before you circulate it: self-grade against user-persona_guide.md, then DELETE every HTML
   comment. They are guidance, not content.
-->

# {{persona_name}} User Persona

## Who They Are

<!-- WHAT  The identity block: a name, a role, a short quote in the persona's own voice, and enough
           background to place them, without stacking demographic fields that do not change a design
           decision.
     WHY   This is the near-universal baseline across published persona formats: a name, a role, and a
           quote, and its content stays consistent across sources for a reason, it is the minimum a reader
           needs to argue a design from a specific person's point of view instead of an average or a guess.
           Deep dive: user-persona_companion.md section 3 (Anatomy > Who They Are).
     ASK   Who is this person? What is their role or job? What is one thing they would actually say, in
           their own words, about their work? What context does a reader need to place them, without listing
           every demographic fact you could gather?
     GOOD  "Name: Renata Ibarra. Role: Overnight shift lead, regional distribution warehouse. Quote: 'I
           don't need a report, I need to know who's not showing up before the trucks arrive.' Background:
           Runs a 40-person overnight crew across three loading docks; has covered a no-show shift herself
           four times this quarter. (Quote and detail from the March 2026 shift-lead interviews, n=9.)"
     WEAK  "Renata is a hardworking supervisor who wants to do her job well and values good communication."
           (no quote, no source, and nothing here that could not apply to any supervisor at any company)
     TRAP  Stacking demographic fields, age, marital status, income bracket, because a template elsewhere
           has them. Every field you add narrows who the persona actually describes: the companion's
           curse-of-dimensionality math (section 7) works a 21-attribute persona down to roughly 134 people
           in the whole United States. Add a field only when it would change a design decision. -->

- Name: {{persona_name}}
- Role: {{persona_role}}
- Quote: "{{persona_quote}}"
- Background: {{persona_background}}

## Goals and Motivations

<!-- WHAT  The goals and motivations that come from actually talking to people in this role, not from what
           the team assumes they want.
     WHY   Nielsen Norman Group states the baseline plainly: personas must be based on user research to
           accurately represent a product's users. This section is where that standard is tested hardest,
           because an invented goal reads exactly like a researched one until someone asks for the evidence
           column. Deep dive: user-persona_companion.md section 3 (Anatomy > Goals and Motivations).
     ASK   What is this person trying to accomplish? Why does it matter to them specifically, not to the
           product team? How do you know, an interview, a support-ticket pattern, a field observation?
     PRIORITY  Order goals by how often they surfaced in your research, not by how well they justify a
           feature already planned. A goal with no evidence column filled in is a guess wearing a goal's
           shape.
     ROW HINT  A good row states a goal a real person would recognize as their own, why it matters to them,
           and where you learned it. A weak row is a goal that only makes sense from the product's point of
           view.
     GOOD  | Know who won't show up before the trucks arrive | A single missed no-show cascades into a
           missed dock window | March 2026 shift-lead interviews (n=9), raised by 7 of 9 |
     WEAK  | Wants better visibility | | |
     TRAP  Writing goals the product team already wants to hear, rather than goals a real interview actually
           produced. If every goal in this table happens to match a feature already on the roadmap, that is
           worth noticing, not celebrating. -->

| Goal | Why it matters | Evidence (how you know) |
|---|---|---|
| {{goal_statement}} | {{goal_rationale}} | {{goal_evidence}} |

## Pains and Barriers

<!-- WHAT  The obstacles and frustrations paired with the goals above, each with enough evidence that a
           reader could go check it.
     WHY   Every published format this research read pairs a goals field with an obstacles field; the pair
           is what turns an identity sketch into something a team can actually design against. This section
           is also the one most exposed to the equity critique the research found: naming, imagery, and
           accessibility are three concrete bias vectors in how pains get written. Deep dive:
           user-persona_companion.md section 3 (Anatomy > Pains and Barriers), section 7 (anti-patterns).
     ASK   What gets in the way of the goals above? What does it cost this person when it happens? Where did
           you observe or hear this?
     PRIORITY  Order by how much the barrier actually blocks the goal it pairs with. A barrier that never
           surfaced in research does not belong here no matter how plausible it sounds.
     ROW HINT  A good row names a specific obstacle, its concrete impact, and its source. A weak row is a
           vague complaint with no evidence.
     GOOD  | The scheduling board only updates from a desktop terminal | Finds out about a no-show after the
           shift has already started, not before | March 2026 shift-lead interviews (n=9) |
     WEAK  | Communication could be better | | |
     TRAP  Writing pains and barriers that quietly exclude disability. A persona that never names a
           disability-related barrier for a broad user base is making a choice, not an omission. -->

| Pain or Barrier | Impact | Evidence (how you know) |
|---|---|---|
| {{pain_statement}} | {{pain_impact}} | {{pain_evidence}} |
