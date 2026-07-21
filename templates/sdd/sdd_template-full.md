---
title: "{{title}}"
status: "{{status}}"
authors: ["{{authors}}"]
reviewers: ["{{reviewers}}"]
created: "{{date}}"
updated: "{{date}}"
related: ["{{related_docs}}"]
doc_type: sdd
size: full
source_template: sdd
source_template_version: 0.1.0
---

<!--
FULL SOFTWARE DESIGN DOCUMENT. Every section, for a design that earns the weight: hard to reverse,
crosses teams, carries security, privacy, or regulatory consequence, or has real non-functional targets
the design must be shaped around. Most changes do not earn it. Reaching for this variant by reflex is how
a design-doc practice turns into the big-design-up-front bureaucracy its critics warn about, where writing
to exhaustion substitutes for deciding.

The full variant is a strict superset of the lean one: the shared sections keep their names and their
order, and this file only ADDS (the structural, runtime, interface, and deployment subsections under The
Design, plus Quality Attributes and Risks and Open Issues).

WHAT A DESIGN DOC IS, AND IS NOT
A design doc describes HOW you will build something. It is not an RFC (which PROPOSES a decision and asks
for feedback) and not an ADR (which RECORDS a decision after it is made). If a significant, hard-to-reverse
choice is made inside this design (a database, an auth model, a public contract), record that decision
ALSO as an ADR, so someone can find it next to the code later. See sdd_companion.md section 8.

STATUS is a lifecycle, not a label. Keep it current:
  draft -> in-review -> approved -> implemented   (and later, possibly, superseded)
Name real reviewers. Once the code ships, either archive this doc or mark when it was last verified
against the running system; a design doc trusted but never checked is worse than none.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   sdd_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK example, and the
   TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you circulate it: self-grade against sdd_guide.md, then DELETE every HTML comment.
-->

# {{title}}

## Context and Scope

<!-- WHAT  What exists today, what is changing, and the boundary of this design. Orient a reader who was
           not in the meetings, then say plainly what is in scope and what is out.
     WHY   A design doc with a vague boundary invites reviewers to drag in every adjacent system, and the
           review never converges. Deep dive: sdd_companion.md section 3 (Anatomy > Context and Scope).
     ASK   What is the current state? What is changing and why now? Where does this design start and stop?
           What nearby system is explicitly NOT part of this?
     GOOD  "Today, task-list filters and sorts live in URL query params and are lost on navigation. This
           design adds saved, shareable views. In scope: storing, listing, and sharing a view within a
           project. Out of scope: cross-project views, and any change to the filtering engine itself."
     WEAK  "We are building saved views." (no current state, no boundary)
     TRAP  A Context section that re-derives the whole product's history. Orient in a paragraph; do not
           re-litigate the requirements the PRD already settled. -->

{{context_and_scope}}

## Goals and Non-Goals

<!-- WHAT  Goals: what the design must achieve to succeed, ideally observable. Non-goals: what it is
           deliberately NOT trying to do, to keep the design and its review bounded.
     WHY   Non-goals are the highest-value line of scope control in a design doc. Most runaway reviews are
           reviewers arguing about something you never meant to solve. Deep dive: sdd_companion.md
           section 3 (Anatomy > Goals and Non-Goals).
     ASK   What must be true for this design to have worked? What are we explicitly not solving, and why?
     GOOD  Goal: "A user can save the current filter/sort as a named view and reuse it across sessions and
           devices." Non-goal: "Real-time collaborative editing of a view; that is a separate feature."
     WEAK  A goals list with no non-goals, so every reviewer expands the scope differently.
     TRAP  Goals written as a build list ("build the table, build the API") rather than as outcomes.
           State what must be TRUE, not what you will type. -->

{{goals_and_non_goals}}

## The Design

<!-- WHAT  The heart of the document: how the system is structured to meet the goals. In this full
           variant, present it through the four views below (static structure, runtime, interfaces,
           deployment). Open with a paragraph naming the core idea before the views.
     WHY   This is the object of review. It must be concrete enough to disagree with, and no more
           exhaustive than that. Deep dive: sdd_companion.md section 3 (Anatomy > The Design).
     ASK   What is the core design idea in one paragraph, before the detail? What one-sentence framing
           orients a first-time reader before the views below?
     GOOD  "Saved views are one new entity in the existing task-service and database, exposed by new REST
           endpoints and a Views dropdown in the task-list UI. The four views below detail the structure,
           the runtime, the contracts, and how it deploys."
     WEAK  Jumping straight into the data model with no framing sentence, so a reviewer cannot tell what
           they are about to read.
     TRAP  Detail before shape. Give the one-paragraph idea first, then the views. -->

{{the_design_overview}}

### Static Structure and Components

<!-- WHAT  What the parts are and how they depend on each other: components, modules, the data model, and
           the dependencies between them. The "building block" view; a component diagram belongs here.
     WHY   The static view is where a reviewer sees whether the decomposition is sound and whether a
           dependency is pointing the wrong way. Deep dive: sdd_companion.md section 3 (Anatomy > The
           Design).
     ASK   What are the components and their responsibilities? What is the data model (entities, fields,
           relationships)? What depends on what? What is new versus reused?
     GOOD  "New: a `saved_view` table (id, name, owner_id, project_id, scope enum private|shared, config
           JSONB, created_at, updated_at) and a ViewsController in the task-service. Reused: the existing
           auth middleware and the project-membership service. [figure: C4 component diagram,
           illustrative]"
     WEAK  A class-by-class dump of every field and method, so the shape is lost in the detail.
     TRAP  One diagram that mixes system context, containers, and code into an unreadable everything-map.
           Pick a level and keep to it. -->

{{static_structure_and_components}}

### Runtime and Data Flow

<!-- WHAT  How the parts behave together over time: the important sequences, the state transitions, and
           the failure paths. What happens on the key operations, step by step.
     WHY   The static view shows what the parts are; the runtime view shows whether they actually work
           together, and it is where a race, a missing failure path, or a chatty call pattern shows up.
           Deep dive: sdd_companion.md section 3 (Anatomy > The Design).
     ASK   What is the sequence for the main operations (create, apply, share a view)? What are the
           failure modes and how are they handled? Where is state, and how does it change?
     GOOD  "Save: the client posts the current filter/sort to POST /projects/{id}/views; the service
           validates membership, persists the row, returns the view id. Apply: the client fetches
           GET /projects/{id}/views/{viewId} and rehydrates the filter state. Failure: a shared view that
           references a since-deleted field applies the rest and flags the missing filter rather than
           erroring. [figure: sequence diagram, illustrative]"
     WEAK  Restating the static structure again, with no sequence or failure behavior.
     TRAP  Only drawing the happy path. The failure paths are the reason this section exists. -->

{{runtime_and_data_flow}}

### Interfaces and Contracts

<!-- WHAT  The APIs, schemas, events, and contracts this design exposes and consumes: endpoints and their
           shapes, the config schema, events emitted, and any external contract touched.
     WHY   Interfaces are the design's public surface and the part other teams build against, so they are
           the part a careful reviewer probes hardest and the most expensive to change after the fact.
           Deep dive: sdd_companion.md section 3 (Anatomy > The Design).
     ASK   What are the endpoints and their request/response shapes? What is the schema of the stored
           config? What events are emitted, and who consumes them? What existing contract changes?
     GOOD  "REST: GET/POST /projects/{id}/views, GET/PUT/DELETE /projects/{id}/views/{viewId}. Config
           schema (versioned): { version: 1, filters: [...], sort: {...}, columns: [...] }. Events:
           view.created, view.applied. No change to existing task endpoints."
     WEAK  "A CRUD API for views." (names no shapes, so no one can build a client or a test against it)
     TRAP  Omitting the config schema. The stored JSON is the real contract here, and an unversioned one
           will hurt the first time filters change (see Risks). -->

{{interfaces_and_contracts}}

### Deployment and Operations

<!-- WHAT  Where it runs and how it is released: the deployment target, the migration, feature-flagging,
           rollout and backout, and the operational ownership.
     WHY   Many designs are sound and still never ship, because no one owned the messy path to production.
           Deep dive: sdd_companion.md section 3 (Anatomy > The Design); the deployment view is arc42's.
     ASK   What is the migration? Is it behind a flag, and how does it roll out and back out? Who
           operates it? What has to be true in each environment?
     GOOD  "Additive migration: create the `saved_view` table (no change to existing tables). Ship behind
           a `saved_views` flag, enabled per-project, dark-launched to internal projects first. Backout:
           disable the flag; the table is inert. Owned by the task-service team; no new service to run."
     WEAK  "Deploy it normally." (names no migration, flag, or backout)
     TRAP  Treating the migration as an afterthought. State whether it is additive and reversible; a
           destructive migration is a different risk conversation. -->

{{deployment_and_operations}}

## Alternatives Considered

<!-- WHAT  The other designs you genuinely weighed and why you are not proposing them, including "do
           nothing" or "the obvious approach" where those are real options.
     WHY   Alternatives are the evidence the design is reasoned rather than preferred, and how a reviewer
           surfaces the option you missed. Deep dive: sdd_companion.md section 3 (Anatomy > Alternatives
           Considered); the anti-pattern is in section 7.
     ASK   What else could meet the goals? What obvious approach did you reject, and why? What would a
           skeptic build? Why not "do nothing"?
     GOOD  "URL and localStorage only (rejected: no sharing, lost across devices). A generic
           user-preferences blob (rejected: no project-scoping or sharing semantics, awkward to query). A
           separate views microservice (rejected: a new service and a sync problem for one table)."
     WEAK  One decoy dismissed in half a sentence.
     TRAP  Straw men. Two decoys and a winner is a sales pitch, not a design review. -->

{{alternatives_considered}}

## Cross-Cutting Concerns

<!-- WHAT  The concerns that touch every part of the design: security and privacy, observability, error
           handling, data retention, cost, accessibility, internationalization. For each, one honest
           line: how the design handles it, or that it does not apply and why.
     WHY   This is where a design that looked clean reveals its real cost. Deep dive: sdd_companion.md
           section 3 (Anatomy > Cross-Cutting Concerns).
     ASK   What is the auth and privacy model? What do we log and measure? How does it fail? Any quotas,
           cost, accessibility, or i18n impact?
     GOOD  "Auth: shared views readable by any project member, write owner-only, membership checked on
           every read. Privacy: private views never returned to non-owners. Observability: view.created
           and view.applied events. Cost: cap 100 saved views per user."
     WEAK  "Standard security applies." (nothing a reviewer can check)
     TRAP  Leaving it blank because "nothing cross-cutting changed." Walk the list; a one-line
           "N/A, inherited" is a real answer, silence is not. -->

{{cross_cutting_concerns}}

## Quality Attributes

<!-- WHAT  The non-functional requirements the design must satisfy, as targets a reader could check:
           performance and latency, scalability, availability, reliability, security posture,
           maintainability. Give numbers and scenarios, not adjectives.
     WHY   A quality attribute with no scenario and no target is one the design has not actually
           addressed. This is where the design meets the non-functional parts of the PRD or SRS. Deep
           dive: sdd_companion.md section 3 (Anatomy > Quality Attributes).
     ASK   What are the latency and throughput targets? How much data and load must it handle? What is the
           availability target? How maintainable and evolvable must it be?
     GOOD  "Performance: the views list loads p95 < 150ms at 50 views. Scale: up to ~500 shared views per
           project. Availability: inherits the task-service SLO (99.9%). Maintainability: the config
           schema is versioned so filters can evolve without breaking stored views."
     WEAK  "It should be fast and scalable." (adjectives with no target, so nothing can be verified)
     TRAP  Listing every quality attribute in the textbook. Name the two or three that actually constrain
           THIS design and give them real numbers; mark the rest N/A. -->

{{quality_attributes}}

## Risks and Open Issues

<!-- WHAT  The parts of the design that are uncertain, risky, or undecided, and what you plan to do about
           each. Name the things that could go wrong and the questions not yet answered.
     WHY   A design doc with no risks section, on any non-trivial design, is not riskless; it is
           undisclosed. Naming a risk is not weakness. Where a risk is really an open decision, that is
           the signal to record an ADR or open an RFC. Deep dive: sdd_companion.md section 3 (Anatomy >
           Risks and Open Issues).
     ASK   What is most likely to go wrong? What depends on something you do not control? What is still
           undecided, and who decides it? What technical debt does this knowingly take on?
     GOOD  "Risk: the stored config references filter fields that may later be renamed or removed; mitigate
           by versioning the config schema and applying-what-resolves. Open: should shared views be
           editable by any member or only the owner? Owner: the product lead, by design review. Debt: no
           pagination on the views list until a project exceeds ~200 views."
     WEAK  "Some risks may exist." (discloses nothing)
     TRAP  Listing only generic risks ("scope creep," "timeline") instead of the design's real technical
           risks. This section is about THIS design's uncertainties. -->

{{risks_and_open_issues}}
