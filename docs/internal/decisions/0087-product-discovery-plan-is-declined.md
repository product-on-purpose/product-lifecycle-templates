---
status: accepted
date: 2026-11-07
decision-makers: [jprisant]
consulted: [claude]
---

# `product-discovery-plan` does not ship: its parts already live in three built bundles, and its one source disowns a template reading

## TL;DR

- **Decision.** `product-discovery-plan` (issue #331) **does not ship**, for now. The `project-brief` guide gains a
  paragraph naming what a brief for a discovery effort should add.
- **Why.** Cagan's ten components already have homes: the team and stakeholders in the project brief, the research
  in the user research plan, the vision and principles in the product strategy. What is left is a heading over
  those three. The one source that names the document also asks readers not to treat it as a template.
- **Who loses.** A team running a funded, time-boxed discovery effort that wants one fixed template for it. The
  guide paragraph routes that need, and nothing checks that a filled brief follows it.
- **Status:** accepted 2026-11-07. The maintainer read the recommendation and ruled: "Decline with paragraph."

## Context and Problem Statement

The candidate came from the library's 2026-10-23 resource crawl. Admission sweep 7 recommended parking it on
2026-10-29, at medium confidence. The sweep named two reads that would settle it: whether Cagan still uses the term
in his later books, and Teresa Torres read directly. The two family homes it found were `research-docs`, which fails
cleanly on its one-study rule, and `discovery-docs`, which fits only with strain.

The maintainer supplied *Inspired* (2nd edition), *Empowered* and *Transformed* on 2026-11-05, and *Continuous
Discovery Habits* on 2026-11-07. Both reads are done.

## Decision Drivers

- **Admission and the build decision are separate questions**
  ([ADR 0064 (deployment plan declined)](0064-deployment-plan-is-declined.md)).
- **A type whose parts are held by built bundles is a composite**, and the library declined the deployment plan
  and the steering committee pack on that ground
  ([ADR 0064](0064-deployment-plan-is-declined.md), [ADR 0065 (steering committee pack declined)](0065-steering-committee-pack-is-declined.md)).
- **Build order is the maintainer's preference**
  ([ADR 0041](0041-maintainer-preference-sets-the-build-order.md)), so this ruling needs no further argument, and
  this record states the reasoning for a later reader.

## Considered Options

1. **Decline, with a guide paragraph in `project-brief`.** Chosen. This follows
   [ADR 0086 (product opportunity assessment declined)](0086-product-opportunity-assessment-is-declined.md).
2. **Decline with no paragraph.** It leaves a team asking for authority to run discovery with no pointer to what
   the brief should add.
3. **Keep it parked.** The two reads the sweep named are done, so a park would keep an open row with nothing left
   to move it.
4. **Admit it to `discovery-docs`.** The family's documents decide whether to build, and a staffing and logistics
   plan does not. A contract amendment would be needed, for a type with one source.

## Decision Outcome

**Chosen: option 1.**

### The single source, and what it says about itself

[Cagan's SVPG page](https://svpg.com/product-discovery-plan/), dated October 12, 2009, says that in many company
cultures the team needs a plan that "spells out what the team believes must be done for this project". It lists ten
components, from the Discovery Core Team to the Required Level of Supporting Documentation. The same page says Cagan
does not want the list treated as a template, and calls it "a list of tools". Sweep 7 counted the page as the only
qualifying source.

### Neither later read supports a separate document

**Cagan's three later books do not name it as a document.** *Inspired* (2nd edition, 2017) uses "discovery planning"
for techniques such as story maps. *Empowered* (2020) and *Transformed* never use the phrase. This rests on text
searches, each empty one re-asked with a second pattern.

**Torres's *Continuous Discovery Habits* (2021) does not name it, and argues against the idea it rests on.** The
phrases "discovery plan" and "research plan" appear on no page. Her sixth mindset asks teams to stop treating
discovery as something done at the beginning of a project, and her working definition is a weekly cadence of
customer contact. Her artifacts, the experience map, the interview snapshot and the opportunity solution tree, are
meant to keep changing rather than to be written once.

### Check 4 fails on composition (POSITION)

| Cagan's components | Where a built bundle already holds them |
|---|---|
| Discovery Core Team, Discovery Extended Team, Key Stakeholders | `project-brief`, Constraints and Who Should Be Involved |
| Customer Development Plan, User Research Tools, User Testing Plan | `user-research-plan`, one study at a time |
| Product Strategy/Vision, Product Principles | `product-strategy` |
| Key Risks | `project-brief` (Constraints) and `risk-register` |
| Required Level of Supporting Documentation | No template section. It is an agreement inside the team |

The sweep's two dimensions disagreed on this mapping: one found three overlaps, the other nearly ten. This record
takes the wider reading. It is the library's position, and it is labelled as such because no source draws the
mapping.

**The project brief is the natural home for the paragraph.** Its job is to ask a named approver for authority "to
start finding out whether and how to proceed", which is what a discovery effort asks for.

### Consequences

**Good.**

- A reader of the project brief guide learns what a brief for a discovery effort should add, at the cost of one
  paragraph.
- The issue closes rather than sitting open with nothing to move it, and the sweep 7 batch is finished.

**Bad, and stated plainly.**

- **The prompts are advice and not template sections**, so nothing checks that a filled brief answers them.
- **The type has no catalog row**, so the decline is discoverable only through this record, the closed issue, the
  [`tier2-specs.md`](../tier2-specs.md) progress table and the backlog page's closed count. It is the fourth declined type without a row.

### What would reopen this, stated so it is falsifiable

1. **The maintainer chooses to build it**, as ADR 0041 allows.
2. **A second named source describes a discovery plan as a written document**, distinct from a project brief and a
   research plan.
3. **A real reader asks for it as its own template**, and the guide paragraph does not meet the need.

## More Information

- The book notes are held locally, at `_local/research/2026-11-05_cagan-books/notes.md` and
  `_local/research/2026-11-07_torres-book/notes.md`. The books stay on the maintainer's machine.
- Sweep 7's digest: `_local/research/2026-10-29_admission-sweep-7/digest.md`.
- **A side finding, not acted on.** Torres's interview snapshot is a named one-page written document, and no bundle
  holds it. Whether it is a type the library should build is a separate catalog question.
- The guide paragraph: [`project-brief_guide.md`](../../../templates/project-brief/project-brief_guide.md).
