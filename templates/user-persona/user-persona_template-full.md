---
title: "{{persona_name}} User Persona"
persona_name: "{{persona_name}}"
persona_role: "{{persona_role}}"
product_or_team: "{{product_or_team}}"
owner: "{{owner}}"
status: "{{status}}"
last_updated: "{{date}}"
evidence_tier: "{{evidence_tier}}"
doc_type: user-persona
size: full
source_template: user-persona
source_template_version: 0.1.0
---

<!--
FULL USER PERSONA. Everything the lean variant carries, plus Context of Use, Scenarios, and Evidence Basis,
the three sections a reader needs to see how this person actually behaves and how much research stands
behind the picture. Use it once you have enough research, interviews, a workshop, field observation, to fill
Evidence Basis honestly, and once a decision genuinely turns on knowing this person's situation and not just
their goals and pains.

THIS VARIANT IS A STRICT SUPERSET OF THE LEAN ONE. The three lean sections appear here under the same
headings and in the same order, with the same placeholders; three sections are added after Pains and
Barriers. If you started lean, grow into this without rewriting anything you already filled in.

WHAT A USER PERSONA IS, AND IS NOT
It says who a product is being built for, grounded in research rather than in invention. It is NOT a buyer
persona (a different artifact answering the purchase decision, not product use), NOT an anti-persona (the
customer type you deliberately do not want, published as its own sibling document once a positive persona
exists), NOT a market segment (a strategic, faceless grouping tool used once a strategy exists, where this is
a tactical, single-character tool used early), and NOT an empathy map (a single-session workshop canvas,
structurally distinct even though the two are often used together). See user-persona_companion.md section 8.

A PROTO-PERSONA IS NOT A DIFFERENT FORMAT, IT IS THIS DOCUMENT AT ITS LIGHTEST EVIDENCE TIER. If Evidence
Basis below honestly says "proto, built from workshop assumptions, no new research," that is not a lesser
document, it is this same format used honestly. What is not acceptable is filling in Evidence Basis with a
research-sounding tier the work does not actually support. See user-persona_companion.md section 3 (Anatomy
> Evidence Basis) and section 4 (Variants and sizing).

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into user-persona_
   companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the TRAP to avoid. For tables,
   PRIORITY explains the ordering rule and ROW HINT says what a good row contains.
2. Replace each {{placeholder}} with your content. Every goal, pain, and context factor needs an evidence
   column filled in with where you actually learned it, not what the product team assumes.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This document should be revisited as your understanding of this person changes, not filed once and
   forgotten, and Evidence Basis below names what should trigger that revisit. Before you circulate it:
   self-grade against user-persona_guide.md, then DELETE every HTML comment. They are guidance, not content.
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

## Context of Use

<!-- WHAT  The situational and behavioral facts, device, environment, frequency, workarounds already built,
           that shape how this person actually uses a product, distinct from what they want (Goals) and
           what stops them (Pains).
     WHY   The original build spec called for a standalone Behaviors section; the research instead found
           that structure in only one of six published formats read, while the rest fold the same material
           into a broader situational block. This section follows the core the sources actually share rather
           than inventing a section to satisfy the spec as originally written. Deep dive: user-persona_
           companion.md section 3 (Anatomy > Context of Use).
     ASK   Where and when does this person actually use the product? What device or environment? How often?
           What workaround have they already built because the product does not do this today?
     PRIORITY  Order rows by how much getting the factor wrong would change what you build, hardest
           constraint first. One row per context factor that would change a design decision; a factor that
           would not change anything you would build does not earn a row at all.
     ROW HINT  A good row names a concrete factor, states what is actually true for this person, and where
           you learned it. A weak row restates the persona's role instead of a new fact.
     GOOD  | Device during a shift | Handheld radio and a shared floor terminal, never a laptop | March 2026
           shift-lead interviews (n=9) and a floor observation shift |
     WEAK  | Uses the system | Yes | |
     TRAP  Turning this into a second Who They Are section. If a row does not describe a situation, a
           device, a frequency, or a workaround, it belongs in Who They Are above or nowhere. -->

| Factor | Detail | Evidence (how you know) |
|---|---|---|
| {{context_factor}} | {{context_detail}} | {{context_evidence}} |

## Scenarios

<!-- WHAT  One scenario showing this person actually using the product, structured as a beginning (what
           they want), a middle (what they do with the product and why), and an end (whether it worked).
     WHY   Only one of the published formats this research read names Scenarios as its own section,
           structured exactly this way; the rest fold the same material into a broader context block or omit
           it. This is a genuine minority practice, not an absent one, which is why it ships as its own
           full-only section rather than being merged into Context of Use above. Deep dive: user-persona_
           companion.md section 3 (Anatomy > Scenarios), section 6 (contested boundary on whether Scenarios
           is its own section).
     ASK   What does this person want to achieve in this moment? What do they actually do with the product
           to get there, and why that path? Do they succeed, and how would you know?
     GOOD  "Beginning: Renata needs to know before 5am whether her overnight crew is fully staffed. Middle:
           She opens the app on the floor terminal, filters to her shift, and sees two unconfirmed slots
           highlighted before she is due at a status meeting; she texts both workers directly from the app
           instead of paging the scheduling office. End: One confirms, one does not; she pulls a floater
           from the pool with 40 minutes to spare instead of finding out at the dock."
     WEAK  "Renata uses the app to check the schedule." (no want, no path, no outcome, could describe any
           user of any scheduling tool)
     TRAP  Writing a scenario that is really a feature tour, walking through screens in order rather than
           following what this specific person is trying to accomplish. If you could swap in a different
           persona's name and nothing else would need to change, it is not yet a scenario. -->

**Scenario: {{scenario_name}}**

- Beginning: {{scenario_beginning}}
- Middle: {{scenario_middle}}
- End: {{scenario_end}}

## Evidence Basis

<!-- WHAT  A declared evidence tier for this persona, proto (workshop assumptions, no new research),
           qualitative (small-sample interviews), or statistical (large-sample survey), what actually
           supports it, and when it was last checked against reality.
     WHY   This is the section the honest-retrieval standard cares about most. The original build spec
           called for a bounded Quotes/Evidence section; the research instead found that no published format
           carries one, what every format needs instead is a record of how much research actually sits
           behind the persona, so this section carries that record rather than a quote bank. Deep dive:
           user-persona_companion.md section 3 (Anatomy > Evidence Basis), section 4 (Variants and sizing),
           section 5 (Methodology lineage).
     ASK   Which evidence tier is this honestly, proto, qualitative, or statistical? What specifically
           supports it, interview count, survey sample, workshop date? When was it last checked, and what
           would trigger a revision, a business change, a competitive change, a shift in who is actually
           using the product?
     GOOD  "Evidence tier: Qualitative. Basis: 9 semi-structured interviews with overnight shift leads
           across three regional warehouses, March 2026, plus one floor observation shift. Last updated:
           2026-03-28. Revisit when: the scheduling system this persona uses changes, or shift-lead turnover
           in the interview pool exceeds half."
     WEAK  "Evidence tier: Research-backed. Basis: user research." (a tier with no honest floor under it,
           and a basis that names no method, no count, and no date)
     TRAP  Labelling an assumption-built persona as though it were interview-backed. There is no golden
           number of interviews that makes a persona correct, but there is a real difference between zero
           and nine, and a reader of this document deserves to know honestly which one they are getting, not
           a tier chosen to sound more credible than the evidence supports. -->

- Evidence tier: {{evidence_tier}}
- Basis: {{evidence_basis}}
- Last updated: {{evidence_last_updated}}
- Revisit when: {{evidence_revisit_trigger}}
