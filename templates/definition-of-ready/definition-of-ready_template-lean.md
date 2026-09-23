---
title: "{{team_name}} Definition of Ready"
doc_type: definition-of-ready
size: lean
team: "{{team_name}}"
owner: "{{owner}}"
status: draft
doc_version: "{{doc_version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: definition-of-ready
source_template_version: 0.1.0
---

<!--
LEAN DEFINITION OF READY. This bundle ships one size, deliberately, and the evidence for that runs the
opposite way from a document that earns a second, heavier weight. No source read for this bundle argues for a
bigger Definition of Ready, and the ones that address its size at all argue for a smaller one: Stefan
Roock's own maturity signal is that it "should be shrinking over time and not growing," and Roman Pichler
recommends starting with a good-enough version and adapting it later rather than building a heavier one
up front. A longer variant would model the exact failure this bundle warns against, so the document stays
small on purpose. See definition-of-ready_companion.md section 4 (Variants and sizing).

READ THIS BEFORE YOU FILL IT IN, BECAUSE IT CHANGES WHAT THIS TEMPLATE CLAIMS.
A Definition of Ready is optional. The 2020 Scrum Guide never uses the phrase, and the Scaled Agile
Framework's own glossary has no entry for it either. Scrum Alliance states the asymmetry directly: a
Definition of Done is part of Scrum, a Definition of Ready is an external and optional tool. Whether to
keep one at all is a live, three-sided argument in the sources behind this bundle, running from abolition,
through keeping a small, guideline-based one, to leaving the decision entirely to the team, and keeping
none is a legitimate outcome of that argument, not a gap in this document. See
definition-of-ready_companion.md section 1 (Orientation) and section 6.1 (Debates).

IT FAILS IN BOTH DIRECTIONS, AND THIS TEMPLATE IS BUILT AROUND THAT.
Every criterion below is written as a guideline with a stated consequence. Only one kind of criterion has
a sourced case for a hard stop, a dependency on another team or a vendor's own calendar; everything else
that reads as a rule rather than a guideline is very likely building the stage gate this document exists
to avoid. See definition-of-ready_companion.md section 3.3 (Readiness Criteria) for both failure
directions, and the Review Trigger section for why it has to check for each of them separately.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   definition-of-ready_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid. The Readiness Criteria table also carries PRIORITY and ROW HINT.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. This is a standing document, revisited on the Review Trigger below, not written once and forgotten.
   Before you first share it: self-grade against definition-of-ready_guide.md, then DELETE every HTML
   comment. They are guidance, not content.
-->

# {{team_name}} Definition of Ready

## Why We Keep One

<!-- WHAT  The specific problem this team's Definition of Ready exists to solve, in plain language, plus
           the condition under which the team would drop it.
     WHY   One source behind this bundle gives the reason a team keeps one at all: "The goal is to
           prevent problems before they have a chance to start." Another, arguing the opposite side of
           the dispute, would still recommend one himself, but only "as an temporary measure on the way
           to something better" (the source's own wording, kept as written). No source read for this
           bundle states a condition for retiring a Definition of Ready once adopted; this template asks
           the team to write its own, as this library's own contribution rather than received practice.
           Deep dive: definition-of-ready_companion.md section 3.1 (Anatomy > Why We Keep One).
     ASK   What is the actual pain this document exists to fix? Has it happened more than once? Under
           what condition would we drop this document rather than keep tightening it?
     GOOD  "We keep pulling in stories the team doesn't understand and losing the first two days of the
           sprint to questions the Product Owner could have answered at refinement. We would drop this
           document if that stopped happening for two sprints running without anyone pointing at it."
     WEAK  "To ensure alignment and quality across the backlog." (agile vocabulary, not a pain; nobody
           could point at the sentence that goes away if this document works)
     TRAP  Writing the reason in the vocabulary of agile ceremony instead of the team's own recent
           experience. A team that cannot fill this section honestly may be a candidate for keeping no
           Definition of Ready at all, which this bundle treats as a legitimate outcome, not a failure to
           complete the exercise. -->

{{why_we_keep_one}}

**We would drop this document if:** {{retirement_condition}}

## Scope and Ownership

<!-- WHAT  Which kinds of backlog items this Definition of Ready applies to, at which recurring moment
           it is checked, and who owns it.
     WHY   Ownership is the one point every source behind this bundle converges on without exception:
           jointly, by the product owner and the team together, created for the team, by the team, never
           handed down by one role to another. One source names what goes wrong when ownership slips to
           a single role: the document gets used "as an argument and reason for rejecting backlog items."
           The moment it is checked has two names in what this bundle read, and both are real: refinement,
           where one source treats it as the success test for whether refinement has done its job, and
           sprint planning, which the Scrum Guide names as the moment items are "deemed ready for
           selection." Pick one or name both; the sources do not force a single answer.
           Deep dive: definition-of-ready_companion.md section 3.2 (Anatomy > Scope and Ownership).
     ASK   Which item types does this apply to (stories, bugs, spikes)? At which moment do we actually
           check it: refinement, sprint planning, or both? Who agreed this document, by name or by role,
           and is it genuinely joint rather than one role's checklist for another?
     GOOD  "Applies to user stories only; bugs and spikes are scoped separately. Checked at refinement,
           and re-checked at sprint planning if a story changed since. Agreed jointly by the Product
           Owner and the whole development team at the retrospective that adopted this document."
     WEAK  "The team's readiness checklist." (names no item types, no moment, and no owner a reader could
           actually hold to it)
     TRAP  Writing this document as one role's gate on another's work, or scoping it to detail that only
           one story ever needed. A criterion only one item needs belongs in that item's own acceptance
           criteria, not here. -->

{{scope_and_ownership}}

## Readiness Criteria

<!-- WHAT  The load-bearing section: each criterion stated as a question a reviewer could answer yes or
           no, the evidence that answers it, and whether missing it stops the item at the door or only
           starts a conversation.
     WHY   This is where the dispute this bundle carries is concentrated, and the template resolves it
           structurally rather than by argument: every criterion is a guideline with a stated
           consequence, never a silent rule. The TRAP below comes directly from one source behind this
           bundle: a rule requiring something be 100 percent finished before a story can be brought into
           an iteration turns this document into "a huge step towards a sequential, stage-gate approach."
           Two competing shapes for what the questions themselves ask appear in the sources behind this
           bundle: clear, feasible and testable from one, and the INVEST heuristic presented as a
           Definition of Ready's components by another, though INVEST's own originating article never
           uses the phrase "Definition of Ready" and is cited here for INVEST's origin only, not as a
           source for this document type. Write the questions either shape can ask; do not adopt one list
           wholesale.
           Deep dive: definition-of-ready_companion.md section 3.3 (Anatomy > Readiness Criteria).
     ASK   For each criterion: what question does it ask, answerable yes or no? What evidence would
           actually answer it? If the answer is no, does the item stop at the door, or does it only start
           a conversation? Could a Product Owner answer every "no" alone, or does someone else need to be
           in the room?
     PRIORITY  Only one kind of criterion has a sourced case for setting "If Missing" to a hard stop: a
           dependency on another team or a vendor, the only case named without a hedge anywhere in this
           bundle's sources, because a team cannot negotiate its way past another team's or a vendor's
           own calendar. Every other row is a guideline: missing it starts a conversation, it does not
           block the door by itself.
     ROW HINT  A good row states a question someone could actually answer, names the evidence that
           answers it, and states the consequence of a miss plainly. A weak row states a state instead of
           a question ("story is clear") with no evidence and no stated consequence.
     GOOD  | Has the team agreed what "done" looks like for this story? | The story links to a completed
           Definition of Done checklist walkthrough with the team, dated. | Guideline: starts a
           conversation at refinement, does not block sprint planning by itself. |
     WEAK  | Story is clear. | | Blocks. |
     TRAP  Writing a hard stop outside the one sourced category, or writing one because a Product Owner
           wants extra leverage rather than because a real cross-team or vendor dependency exists. If a
           criterion cannot be answered without the Product Owner personally weighing in every time, it
           has probably drifted from a guideline back toward the gate this section exists to avoid. -->

| Criterion (a question) | Evidence | If Missing |
|---|---|---|
| {{criterion_question}} | {{criterion_evidence}} | {{criterion_consequence}} |

## When an Item Is Not Ready

<!-- WHAT  The stated escape valve: what actually happens when a top-priority item does not meet this
           Definition of Ready.
     WHY   Every source behind this bundle that is not flatly against keeping a Definition of Ready
           supplies some version of a pressure valve, which is why this template makes it a named section
           rather than leaving it implied. One account of a team that refused an urgent item is explicit
           that refusal is not the only legitimate outcome: if the team believes the item can still be
           completed within the sprint, pulling it in anyway is acceptable. Another source's alternative
           is procedural rather than a waiver: making the item ready is itself the sprint's first task. A
           third names the mechanism directly: letting the team override the document with a quick,
           documented decision. This section is the direct mirror of definition-of-done's "When Work Does
           Not Meet It" section: both exist because a standard nobody can bend under real pressure is a
           standard people learn to route around instead of honour.
           Deep dive: definition-of-ready_companion.md section 3.4 (Anatomy > When an Item Is Not Ready).
     ASK   Which of these does this team actually do when a top-priority item misses: pull it in anyway
           on team judgment, make it ready as the sprint's first task, or override with a documented
           decision? Is that choice written down here, or only understood informally?
     GOOD  "If a top-priority item misses this Definition of Ready, the team's default is to make it
           ready as the sprint's first task. A documented override, recorded in the sprint notes with who
           agreed it, is available when the team judges the item completable anyway."
     WEAK  "We use judgment." (names no actual mechanism; a reader cannot tell what happens under
           pressure, which is exactly when this section is needed)
     TRAP  Leaving this section silent. Silence on what happens when a top-priority item misses is what
           turns a Definition of Ready into the stage gate the Readiness Criteria section warns against:
           nobody can point to a documented way in, so the document either gets ignored under pressure or
           becomes an argument for rejecting the item outright. -->

{{not_ready_path}}

## Review Trigger

<!-- WHAT  Two named conditions, not calendar dates, that tell the team this Definition of Ready has
           gone stale in each direction, and who is responsible for noticing each one.
     WHY   The standing-standards family this bundle belongs to requires every member to carry this
           mechanism, because every member fails the same quiet way: by drifting out of date while
           everyone still believes it is current. What makes this section distinctive for a Definition of
           Ready is that the trigger has to fire in both directions, and both directions have a source in
           this bundle's research. Too loose: one source's own guidance is to update the document
           whenever the team observes recurring missing information in stories that impacts planning, and
           another names the same signal from the other side, "a lot of scrambling to understand work
           within the sprint." Too tight: a third source names the opposite failure directly, "When the
           DoR blocks more value than it enables, it stops being a safety rail and becomes a parking
           brake."
           Deep dive: definition-of-ready_companion.md section 3.5 (Anatomy > Review Trigger).
     ASK   What concrete, recurring signal would tell us this document is letting unready work through?
           Who notices that signal, by name or role? What concrete signal would tell us it is blocking
           work the team could have done? Who notices that one?
     GOOD  "Too loose trigger: a top-priority item needed the override in 'When an Item Is Not Ready'
           three sprints in a row for the same missing information. Noticed by: whoever runs refinement,
           raised at the next retrospective. Too tight trigger: the team has made a not-ready item ready
           as the sprint's first task in every sprint for a month, and it is always the same criterion.
           Noticed by: the Scrum Master, raised at the next retrospective."
     WEAK  "Reviewed quarterly." (a calendar reminder, not a condition; it fires whether or not anything
           is actually wrong, and it only ever looks in one direction even when it does fire)
     TRAP  Naming only the too-loose direction. A Definition of Ready that has never once been loosened
           is, per the dispute this bundle carries, at least as worth investigating as one that has never
           been tightened; a trigger that cannot fire toward "we are being too strict" has quietly
           assumed the wrong failure mode for this document type. -->

**Too loose trigger:** {{too_loose_trigger}}
**Noticed by:** {{too_loose_owner}}

**Too tight trigger:** {{too_tight_trigger}}
**Noticed by:** {{too_tight_owner}}
