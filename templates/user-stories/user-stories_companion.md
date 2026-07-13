# Companion: The User Story

> The deep explainer for the User Story bundle. Read this to understand what a user story is, where it
> came from, why it is shaped the way it is, and where practitioners disagree. The short operator card
> is [`user-stories_guide.md`](user-stories_guide.md); worked instances are in
> [`user-stories_example.md`](user-stories_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references), tagged by source reliability.

---

## 1. Orientation

A user story is "a short, simple description of a feature told from the perspective of the person who
desires the new capability, usually a user or customer of the system" [[2]](#ref-2). Its canonical shape is the
Connextra template: **"As a [type of user], I want [goal], so that [benefit]"** [[2]](#ref-2)[[5]](#ref-5).

The crucial idea, and the one most often missed, is that a user story is **not a specification**. It is
"a placeholder for a future conversation" [[2]](#ref-2). The card is a pointer to a requirement, not the
requirement itself; the real detail emerges in conversation and is captured as confirmation (acceptance
criteria) [[2]](#ref-2)[[3]](#ref-3). A team that treats the one-liner as a complete spec has missed the point of the form.

**At a glance**
- It reframes work from "what to build" to "who needs what, and why."
- It is deliberately small: sized to fit inside one iteration [[4]](#ref-4).
- Its value lives in the conversation it triggers, not the sentence on the card [[2]](#ref-2)[[3]](#ref-3).
- Detailed "done" conditions live in its acceptance criteria, a separate concern (see the
  [acceptance-criteria](../acceptance-criteria/acceptance-criteria_companion.md) bundle).

---

## 2. Origins and evolution

The user story is a practice of **Extreme Programming (XP)**. Kent Beck introduced it in 1997 on the
Chrysler Comprehensive Compensation (C3) project and formalized it when he published *Extreme
Programming Explained* in 1999, where stories drove the planning game [[1]](#ref-1)[[7]](#ref-7).

Three contributions turned the practice into the form used today:

- **The Connextra template (2001).** The XP team at Connextra in London devised the "As a [role], I want
  [goal], so that [benefit]" format and shared it; it became the most common story shape [[5]](#ref-5)[[7]](#ref-7). Mike
  Cohn credits Rachel Davies, who in turn credits the whole team [[2]](#ref-2).
- **The Three C's (2001).** Ron Jeffries named the three components that keep a story from becoming a
  mini-spec: **Card** (a short written token), **Conversation** (where the detail is worked out), and
  **Confirmation** (the tests or acceptance criteria that say it is done) [[2]](#ref-2)[[3]](#ref-3).
- **User Stories Applied (2004).** Mike Cohn's book generalized the practice beyond index cards and
  became the standard reference [[2]](#ref-2)[[7]](#ref-7).

A quality heuristic followed in 2003: Bill Wake's **INVEST** (Independent, Negotiable, Valuable,
Estimable, Small, Testable), a checklist for a good story or backlog item [[4]](#ref-4). Later, Jeff Patton's
2014 *User Story Mapping* added a way to arrange stories into a narrative of the whole product [[7]](#ref-7).

Scrum did not invent the user story but adopted it widely: stories are the most common form of Product
Backlog item, though the Scrum Guide itself does not mandate the format [[8]](#ref-8).

---

## 3. Anatomy (section by section)

The lean card carries the starred sections; the full variant adds quality scaffolding.

**Story (lean).** The "As a / I want / so that" statement. *Why:* it forces the user, the goal, and the
benefit into one sentence. *Beginner trap:* a UI task in disguise ("As a user I want a dropdown"). The
"so that" clause is the test; if you cannot state a real benefit, the value is unclear [[2]](#ref-2). *Expert
note:* when the user's situation and motivation matter more than their role, the job-story form is
often sharper (see [§6](#6-debates-and-contested-boundaries)).

**Description and context (full).** Background the one-liner cannot carry: the parent epic, the problem,
links to designs or the PRD. *Why:* it orients without bloating the card. *Expert note:* keep it thin;
if the story needs paragraphs of context, it may be an epic that should be split.

**Acceptance criteria (lean).** The conditions that confirm "done," from the user's view. This is
Jeffries' Confirmation [[3]](#ref-3). *Why:* it makes the story testable (the T in INVEST) [[4]](#ref-4). *Expert note:* for
anything with real behavior, push detailed criteria into the acceptance-criteria artifact rather than
overloading the card.

**INVEST check (full).** A self-test of story quality [[4]](#ref-4). *Why:* it catches the two failures that wreck
sprints, stories that are not Independent and stories that are not Small. *Expert note:* "Negotiable"
does not mean the need is up for debate, only the path to meeting it [[4]](#ref-4).

**Estimate and sizing (full).** The team's relative estimate and its confidence. *Why:* it informs
planning. *Expert note:* an estimate is the output of a conversation, not a commitment; a precise number
with no shared basis is theater.

**Dependencies (full).** What the story needs before it can be done. *Why:* the unlisted dependency is
the classic mid-sprint blocker. *Expert note:* a story with many hard dependencies is failing the "I"
in INVEST and probably wants restructuring.

**Notes and open questions (lean).** Links, decisions, and surfaced unknowns. *Why:* refinement runs on
these. *Beginner trap:* hiding unknowns to look ready.

---

## 4. Variants and sizing

A user story is inherently small, so the two variants here are not about document length but about how
much **quality scaffolding** travels with the story.

- **Lean.** Just the card: Story, Acceptance criteria, Notes. The right default for most backlog items,
  and what you write dozens of. For a set of stories, repeat the card.
- **Full.** The card plus INVEST, estimate, and dependencies. Use it for a story that carries risk,
  crosses teams, or must be sized and de-risked before commitment, and for the few stories where the
  scaffolding earns its keep.

The nesting rule holds: the lean card's sections are a strict subset of the full story's, so a card can
grow into a fully scaffolded story in place. Bias toward the lean card; the whole point of stories is to
stay light and lean on conversation [[2]](#ref-2).

---

## 5. Methodology lineage

- **XP (origin).** Stories drive the planning game; they are estimated, prioritized, and pulled into
  iterations [[1]](#ref-1).
- **Scrum.** Stories are the usual Product Backlog item, refined into Sprint Backlog work, but the Scrum
  Guide mandates neither stories nor their format; it speaks only of Product Backlog items and the
  Product Goal [[8]](#ref-8).
- **SAFe and scaled frameworks.** Stories nest under features and epics, with INVEST applied at the story
  level and additional structure above [[4]](#ref-4)[[7]](#ref-7).
- **JTBD / job stories.** A pointed alternative that replaces the persona-and-role framing with situation
  and motivation (see below) [[6]](#ref-6).
- **Story mapping (Patton).** Arranges stories along the arc of user activity, so a backlog reads as a
  narrative rather than a flat list [[7]](#ref-7).

---

## 6. Debates and contested boundaries

**User story vs job story.** The sharpest live debate. Alan Klement, drawing on Jobs to be Done and an
approach that originated at Intercom, argues the user story "contains too many assumptions and doesn't
acknowledge causality," and that the "As a [role]" framing is engineering-driven rather than
customer-driven [[6]](#ref-6). The job story replaces it with **"When [situation], I want [motivation], so I can
[outcome]"**, emphasizing context over persona [[6]](#ref-6). *Recommendation:* use the user story as the default
(it is universally understood); reach for the job story when the user's situation and motivation are the
crux and a generic role would flatten them.

**Story as placeholder vs story as spec.** The original intent is a conversation placeholder [[2]](#ref-2)[[3]](#ref-3). In
practice many teams write heavy, fully-specified stories that function as mini-PRDs. *Recommendation:*
keep the card light and move real detail into acceptance criteria and, where needed, a PRD; a story
straining to hold a spec is a sign the work is mis-sized.

**Format dogma.** Teams sometimes enforce the "As a / I want / so that" wording rigidly. Cohn and others
treat it as a useful default, not a law; the goal is shared understanding, not template compliance [[2]](#ref-2).
*Recommendation:* keep the format when it helps and drop it when it forces awkward phrasing.

**Stories vs use cases.** A use case documents an actor-system interaction in full (main and alternate
flows); a story is a thin slice that triggers a conversation [[7]](#ref-7). *Recommendation:* prefer stories for
iterative delivery; reserve use cases for contexts that genuinely need exhaustive flow documentation.

---

## 7. Anti-patterns and failure modes

- **The card is the spec.** Treating the one-liner as complete and skipping the conversation. The
  founding mistake the Three C's exist to prevent [[2]](#ref-2)[[3]](#ref-3).
- **UI task disguised as a story.** "As a user I want a button" states a solution, not a goal.
- **No "so that."** Dropping the benefit clause hides whether the work is worth doing.
- **Stories too big.** A story that cannot fit an iteration fails "Small" and should be split [[4]](#ref-4).
- **Hidden dependencies.** Unlisted blockers that surface mid-sprint, a failure of "Independent" [[4]](#ref-4).
- **Acceptance criteria absent or vague.** Leaves "done" to interpretation, a failure of "Testable" [[4]](#ref-4).
- **Persona theater.** "As a user" for every story, where naming the real situation would change the
  design; this is the gap job stories target [[6]](#ref-6).

---

## 8. Relationships to other artifacts

- **Upstream:** the PRD or product brief (sets scope and the why), discovery research and personas
  (ground the user), epics and themes (the parent the story is split from) [[7]](#ref-7)[[9]](#ref-9).
- **Attached:** acceptance criteria (the Confirmation that makes the story testable) [[3]](#ref-3), and estimates.
- **Downstream:** the Sprint Backlog (where stories become committed work), the Increment (what done
  stories sum to), and the test plan that verifies them [[8]](#ref-8)[[9]](#ref-9).

In this library the User Story pairs with the `deliver-user-stories` skill and sits in the
`delivery-docs` family beside the `prd`, `acceptance-criteria`, and `release-notes` templates.

---

## 9. Adaptations

- **Solo or small team.** The lean card is plenty; lean hard on conversation since the conversation is
  in the room.
- **Scaled / multi-team.** Use the full variant with INVEST and dependencies; the "Independent" check
  earns its keep when many teams share a backlog [[4]](#ref-4).
- **Discovery / JTBD teams.** Use the job-story form to keep situation and motivation central [[6]](#ref-6).
- **Regulated contexts.** Stories alone rarely satisfy auditors; pair them with traceable requirements
  (an SRS, a requirements traceability matrix) so each story links to a controlled requirement [[9]](#ref-9).

---

## 10. Worked example

See [`user-stories_example.md`](user-stories_example.md) for a small set of stories for the same
"Saved Views" feature used in the PRD example, including a lean card, a fully scaffolded story with an
INVEST check, and the same need expressed as a job story for contrast.

---

## References

Tagged by reliability: `[primary]` originating source or standards body; `[practitioner]` recognized
authority; `[vendor]` commercially motivated; `[reference]` consolidated secondary. Researched 2026-06-30.

<a id="ref-1"></a>[1] Kent Beck. "Extreme Programming Explained: Embrace Change." Addison-Wesley, 1999; user stories introduced on the Chrysler C3 project, 1997. [primary]

<a id="ref-2"></a>[2] Mike Cohn. "User Stories Applied: For Agile Software Development." Addison-Wesley, 2004; and "[User Stories and User Story Examples](https://www.mountaingoatsoftware.com/agile/user-stories)." Mountain Goat Software (accessed 2026-06-30). [practitioner]

<a id="ref-3"></a>[3] Ron Jeffries. "[Essential XP: Card, Conversation, Confirmation](https://ronjeffries.com/xprog/articles/expcardconversationconfirmation/)," 2001 (the Three C's). ronjeffries.com (accessed 2026-06-30). [practitioner]

<a id="ref-4"></a>[4] Bill Wake. "[INVEST in Good Stories, and SMART Tasks](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)." XP123, 2003 (accessed 2026-06-30). [practitioner]

<a id="ref-5"></a>[5] Connextra team (credited to Rachel Davies and the team). The "As a [role], I want [goal], so that [benefit]" template, 2001. [practitioner]

<a id="ref-6"></a>[6] Alan Klement. "[Replacing the User Story with the Job Story](https://jtbd.info/replacing-the-user-story-with-the-job-story-af7cdee10c27)." jtbd.info, 2013; and Intercom, "[How we accidentally invented Job Stories](https://www.intercom.com/blog/accidentally-invented-job-stories/)." intercom.com (accessed 2026-06-30). [practitioner]

<a id="ref-7"></a>[7] Wikipedia. "[User story](https://en.wikipedia.org/wiki/User_story)." en.wikipedia.org (accessed 2026-06-30); see also Jeff Patton, "User Story Mapping," O'Reilly, 2014. [reference]

<a id="ref-8"></a>[8] Ken Schwaber and Jeff Sutherland. "[The 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html)." scrumguides.org, 2020 (accessed 2026-06-30). [primary]

<a id="ref-9"></a>[9] "[Master Catalog of Product Management and SDLC Document and Artifact Types](../../_local/initial-discovery/docs/deep-research_master-catalog.md)," entry 30 (User Story). Internal deep-research catalog, 2026. [internal]
