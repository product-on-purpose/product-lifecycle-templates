---
title: "{{title}}"
status: "{{status}}"
authors: ["{{authors}}"]
created: "{{date}}"
updated: "{{date}}"
rfc_id: "{{rfc_id}}"
doc_type: rfc
size: lean
source_template: rfc
source_template_version: 0.1.0
---

<!--
LEAN RFC. The smallest proposal that can still gather real feedback and reach a decision. Use it
for a change that affects more than your own corner but is not a multi-team, hard-to-reverse
commitment. To grow it into a full RFC, ADD sections (see rfc_template-full.md); never rename or
reorder the ones below, because the full variant is a strict superset of this one.

WHAT AN RFC IS, AND IS NOT
An RFC proposes a change and asks for input BEFORE the decision is made. That is the whole point,
and it is the opposite of an ADR, which RECORDS a decision after it is made. If the decision is
already taken and you are writing this to look consultative, you are writing RFC theater, and
everyone can tell. Write an ADR instead.

STATUS is a lifecycle, not a label. Move it as the RFC moves:
  draft -> in-review -> accepted | rejected | withdrawn   (and later, possibly, superseded)
The status field in the frontmatter is the single most important thing to keep current. A stale
status is how an RFC graveyard forms.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   rfc_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you circulate it: self-grade against rfc_guide.md, then DELETE every HTML comment. They
   are guidance, not content.
-->

# {{title}}

## Summary

<!-- WHAT  Two or three sentences: what you are proposing and what changes if it is accepted. A
           reader should grasp the whole idea before any detail.
     WHY   The summary is the triage surface. Most people decide from it whether to engage, and an
           RFC's entire value is the engagement it attracts. If you cannot summarize the proposal,
           it is not shaped enough to circulate.
           Deep dive: rfc_companion.md section 3 (Anatomy > Summary).
     ASK   What are you proposing? What becomes true if it ships? Who should care?
     GOOD  "Propose moving service-to-service auth from shared static tokens to short-lived mTLS
           certs issued by an internal CA, so a leaked credential expires in minutes rather than
           living until someone rotates it by hand."
     WEAK  "We should improve our auth." (a wish, not a proposal)
     TRAP  Writing the summary as a problem statement with no proposal in it. The Motivation section
           is for the problem; the summary must contain the actual proposed change. -->

{{summary}}

## Motivation

<!-- WHAT  The problem or opportunity, and why it is worth solving now. The forces in play:
           technical, product, organizational. What breaks or stays broken if nobody acts.
     WHY   Motivation is what earns the reader's attention and what a reviewer argues with first. A
           proposal whose motivation is thin gets bikeshed on the solution, because there is nothing
           more substantial to engage. Spend real effort here.
           Deep dive: rfc_companion.md section 3 (Anatomy > Motivation).
     ASK   What is wrong today? Who feels it, and how often? What is the cost of doing nothing? Why
           now rather than next quarter?
     GOOD  "Static service tokens have leaked twice this year via logs. Each rotation is a manual,
           coordinated, multi-team scramble that takes a day. As we add services, the blast radius
           of a single leak grows and the rotation cost grows with it."
     WEAK  "Our current approach is not best practice." (an appeal to fashion, not a cost)
     TRAP  Motivation written backwards from the solution you already like, so it only justifies
           that one option. Describe the problem so honestly that a DIFFERENT solution could win. -->

{{motivation}}

## Proposal

<!-- WHAT  The proposed change, at the level of a shared mental model: the core idea and how people
           experience it. Enough that a reader can reason about it, not every implementation detail.
     WHY   This is the object of discussion. It should be concrete enough to disagree with. A vague
           proposal produces vague feedback and no decision.
           Deep dive: rfc_companion.md section 3 (Anatomy > Proposal).
     ASK   What exactly changes? What is the shape of the solution? What is explicitly in, and what
           is left for later?
     GOOD  "Stand up an internal CA. Each service gets a workload identity and requests a cert valid
           for 15 minutes, auto-renewed by a sidecar. The mesh rejects any connection without a
           valid cert. Rollout is per-namespace behind a flag, dual-running static tokens until each
           namespace is cut over."
     WEAK  "Adopt mTLS." (names a technology, not a proposal anyone can evaluate)
     TRAP  Jumping to the lowest-level detail before the shape is clear, or leaving it so abstract
           that no one can find anything to push on. -->

{{proposal}}

## Alternatives Considered

<!-- WHAT  The other options you genuinely weighed, and why you are not proposing them. Include
           "do nothing" when it is a real option, which is usually.
     WHY   The alternatives are the strongest evidence that the proposal is the result of thinking
           rather than preference, and they are what let a reviewer surface the option you missed.
           An RFC with no alternatives invites the reader to supply them, adversarially.
           Deep dive: rfc_companion.md section 3 (Anatomy > Alternatives Considered); the missing-
           alternatives anti-pattern is in section 7.
     ASK   What else could solve the motivation? What is the obvious option you rejected, and why?
           What would a skeptic propose instead? Is "do nothing" acceptable, and why not?
     GOOD  "Rotate static tokens automatically (rejected: reduces but does not remove leak lifetime;
           still a shared secret). Buy a vendor mesh (rejected: cost, and lock-in for a capability
           we can run). Do nothing (rejected: leak cost is already being paid, twice this year)."
     WEAK  One decoy option dismissed in half a sentence.
     TRAP  Straw men. Listing only options you would never pick makes the proposal look inevitable,
           which reads as a sales pitch and costs you the reviewer's trust. -->

{{alternatives_considered}}

## Open Questions

<!-- WHAT  What is genuinely undecided or unknown, that you want input on. Each as a real question,
           ideally with who might answer it.
     WHY   The open questions are the actual request for comment. They tell reviewers exactly where
           their input changes the outcome, which is how you get engagement instead of a silent
           rubber stamp. An RFC with no open questions is usually hiding them.
           Deep dive: rfc_companion.md section 3 (Anatomy > Open Questions).
     ASK   What are you unsure about? Where could a reviewer change your mind? What did you punt on?
     GOOD  "How do we bootstrap identity for a brand-new service before it has a cert? Do we need to
           support non-mesh clients, and if so how do they authenticate? What is the CA's own
           rotation and recovery story?"
     WEAK  An empty section, or "None" on a proposal that obviously has unknowns.
     TRAP  Hiding the hard questions to look more finished. A confident-looking RFC with no open
           questions gets rubber-stamped, and the questions surface later as production incidents. -->

{{open_questions}}

## Outcome

<!-- WHAT  The decision, once it is made: accepted, rejected, or deferred; who decided; the date;
           and a one-line why. While the RFC is open, this says so.
     WHY   An RFC with no recorded outcome is the single most common way the format fails. The
           discussion happens, a decision is reached in someone's head or a meeting, and the
           document is abandoned mid-thread, so the next person cannot tell what was decided or why.
           This section is what turns a proposal into a durable record and what an ADR is later
           written FROM. Deep dive: rfc_companion.md section 3 (Anatomy > Outcome) and the RFC-to-
           ADR relationship in section 8.
     ASK   Has a decision been made? By whom, and when? If accepted, what happens next (an ADR, a
           tracking issue)? If deferred, what would reopen it?
     GOOD  "Accepted 2026-05-02 by the Platform review group. Rollout tracked in PLAT-1421. The
           decision itself is recorded as ADR 0031; this RFC is its rationale trail."
     WEAK  Deleting this section because "the RFC is still open." Keep it, and write "Status: in
           review. No decision yet."
     TRAP  Leaving this blank forever. An RFC that never records its outcome is indistinguishable
           from one that was ignored. Set the status and write the one line the moment it is decided. -->

{{outcome}}
