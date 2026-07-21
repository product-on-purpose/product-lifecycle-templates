---
title: "{{title}}"
status: "{{status}}"
authors: ["{{authors}}"]
created: "{{date}}"
updated: "{{date}}"
doc_type: sdd
size: lean
source_template: sdd
source_template_version: 0.1.0
---

<!--
LEAN SOFTWARE DESIGN DOCUMENT. The smallest design doc that still gets a design thought through and
reviewed before it is expensive to change. Use it for a change that is more than a one-file edit but is
not a hard-to-reverse, multi-team, or safety-critical design. To grow it into a full design doc (see
sdd_template-full.md), ADD sections and subsections; never rename or reorder the ones below, because the
full variant is a strict superset of this one.

WHAT A DESIGN DOC IS, AND IS NOT
A design doc describes HOW you will build something, so people can review the design before the code
exists. It is not an RFC (which PROPOSES a decision and asks for feedback) and not an ADR (which RECORDS
a decision after it is made). If what you actually want is feedback on whether to do this at all, write
an RFC. If you are recording a single hard-to-reverse choice, write an ADR. See sdd_companion.md
section 8. The value of this document is the review it gets, not the document itself.

STATUS is a lifecycle, not a label. Move it as the design moves:
  draft -> in-review -> approved -> implemented   (and later, possibly, superseded)
Keep it current, and once the code ships, either archive this doc or mark when it was last checked
against the real system. A design doc everyone trusts and no one has verified is worse than none.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   sdd_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK example, and
   the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you circulate it: self-grade against sdd_guide.md, then DELETE every HTML comment. They are
   guidance, not content.
-->

# {{title}}

## Context and Scope

<!-- WHAT  What exists today, what is changing, and the boundary of this design. Orient a reader who was
           not in the meetings, then say plainly what is in scope and what is out.
     WHY   A design doc with a vague boundary invites reviewers to drag in every adjacent system, and the
           review never converges. The scope line is the cheapest way to keep the discussion on the
           thing you are actually designing. Deep dive: sdd_companion.md section 3 (Anatomy > Context and
           Scope).
     ASK   What is the current state? What is changing and why now? Where does this design start and
           stop? What nearby system is explicitly NOT part of this?
     GOOD  "Today, task-list filters and sorts live in URL query params and are lost on navigation; there
           is no way to save or share a view. This design adds saved, shareable views. In scope: storing,
           listing, and sharing a view within a project. Out of scope: cross-project views, and any change
           to the filtering engine itself."
     WEAK  "We are building saved views." (no current state, no boundary, so the review has nothing to
           anchor on)
     TRAP  A Context section that re-derives the whole product's history. Orient in a paragraph; do not
           re-litigate the requirements the PRD already settled. -->

{{context_and_scope}}

## Goals and Non-Goals

<!-- WHAT  Goals: what the design must achieve to succeed, ideally observable. Non-goals: what it is
           deliberately NOT trying to do, to keep the design and its review bounded.
     WHY   Non-goals are the highest-value line of scope control in a design doc. Most runaway reviews are
           reviewers arguing about something you never meant to solve; naming it a non-goal ends that
           thread before it starts. Deep dive: sdd_companion.md section 3 (Anatomy > Goals and Non-Goals).
     ASK   What must be true for this design to have worked? What are we explicitly not solving here, and
           why? What is a reasonable-but-separate concern a reviewer might raise?
     GOOD  Goal: "A user can save the current filter/sort as a named view and reuse it across sessions and
           devices." Non-goal: "Real-time collaborative editing of a view. Views are saved and shared, not
           co-edited live; that is a separate feature."
     WEAK  A goals list with no non-goals, so every reviewer expands the scope in a different direction.
     TRAP  Goals written as a feature list ("build the views table, build the API") rather than as
           outcomes. State what must be TRUE, not what you will type. -->

{{goals_and_non_goals}}

## The Design

<!-- WHAT  The heart of the document: how the system is actually structured to meet the goals. The core
           idea, the main components, how they interact, and the data that flows between them. A diagram
           is usually worth more than the paragraph it replaces. For a heavier design, the full variant
           breaks this into structural, runtime, interface, and deployment views.
     WHY   This is the object of review. It has to be concrete enough for a colleague to disagree with,
           and no more exhaustive than that: the job is to convey the design and expose the risky parts,
           not to pre-write the code. Deep dive: sdd_companion.md section 3 (Anatomy > The Design).
     ASK   What are the components, and how do they depend on each other? What is the data model? What are
           the key interfaces? What is the important runtime behavior (the main sequences, the failure
           paths)?
     GOOD  "Add a `saved_view` table (id, name, owner_id, project_id, scope, config JSON, timestamps) in
           the existing Postgres database. The task-service exposes CRUD endpoints under
           /projects/{id}/views. The frontend adds a Views dropdown that captures the current filter/sort
           into `config` on save. Shared views are visible to all project members; private views only to
           the owner. [figure: component and data-flow sketch, illustrative]"
     WEAK  "Use a database to store views and an API to serve them." (names categories, not a design
           anyone can review or build from)
     TRAP  Turning this into an exhaustive spec that no reviewer can finish. Detail the risky and novel
           parts; compress the obvious ones. Approval by fatigue is not approval. -->

{{the_design}}

## Alternatives Considered

<!-- WHAT  The other designs you genuinely weighed and why you are not proposing them, including "do
           nothing" or "the obvious approach" where those are real options.
     WHY   Alternatives are the evidence the design is reasoned rather than merely preferred, and they are
           how a reviewer surfaces the option you missed. Their absence invites the reader to supply them
           adversarially. Deep dive: sdd_companion.md section 3 (Anatomy > Alternatives Considered); the
           no-alternatives anti-pattern is in section 7.
     ASK   What else could meet the goals? What is the obvious approach you rejected, and why? What would a
           skeptic build instead? Is "do nothing / keep it in the URL" acceptable, and why not?
     GOOD  "Store config in the URL and localStorage only (rejected: no sharing, lost across devices). A
           generic user-preferences key-value blob (rejected: no project-scoping or sharing semantics, and
           awkward to query). A separate views microservice (rejected: a new service and a data-sync
           problem for what is fundamentally one table)."
     WEAK  One decoy option dismissed in half a sentence.
     TRAP  Straw men. Listing only options you would never pick makes the design look inevitable, which
           reads as a sales pitch and costs the reviewer's trust. -->

{{alternatives_considered}}

## Cross-Cutting Concerns

<!-- WHAT  The concerns that touch every part of the design rather than living in one component: security
           and privacy, observability, error handling, data retention, cost, accessibility,
           internationalization. For each, one honest line: how the design handles it, or that it does
           not apply and why.
     WHY   This is where a design that looked clean reveals its real cost: the auth check, the privacy
           surface, the observability that has to be designed in rather than bolted on. Deep dive:
           sdd_companion.md section 3 (Anatomy > Cross-Cutting Concerns).
     ASK   What is the auth and privacy model? What do we log and measure, and are there quotas or cost
           limits? How does it fail, and what happens then? Any accessibility or i18n impact?
     GOOD  "Auth: shared views are readable by any project member; write is owner-only; a membership check
           gates every read of a shared view. Privacy: private views are never returned to non-owners.
           Observability: emit view.created and view.applied events. Cost: cap 100 saved views per user to
           bound storage."
     WEAK  "Standard security applies." (says nothing a reviewer can check)
     TRAP  Leaving the section blank because "nothing cross-cutting changed." Walk the list explicitly; a
           one-line "N/A, auth is unchanged and inherited" is a real answer, silence is not. -->

{{cross_cutting_concerns}}
