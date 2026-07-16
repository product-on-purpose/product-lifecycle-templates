---
title: "{{title}}"
status: "{{status}}"
authors: ["{{authors}}"]
reviewers: ["{{reviewers}}"]
created: "{{date}}"
updated: "{{date}}"
review_by: "{{date}}"
rfc_id: "{{rfc_id}}"
doc_type: rfc
size: full
source_template: rfc
source_template_version: 0.1.0
---

<!--
FULL RFC. Every section, for a change that earns the weight: hard to reverse, crosses teams,
carries regulatory or security consequence, or expensive if it goes wrong. Most changes do not
earn it. Reaching for this variant by reflex is how an RFC process turns into the bureaucracy its
critics warn about, where writing to exhaustion substitutes for deciding.

The full variant is a strict superset of the lean one: the shared sections keep their names and
their order, and this file only ADDS (Goals and Non-Goals, Detailed Design, Drawbacks and
Trade-offs, Rollout and Adoption).

WHAT AN RFC IS, AND IS NOT
An RFC proposes a change and asks for input BEFORE the decision is made. That is the opposite of
an ADR, which RECORDS a decision after it is made. If the decision is already taken, do not dress
it as an RFC; write an ADR.

STATUS is a lifecycle, not a label. Keep it current:
  draft -> in-review -> accepted | rejected | withdrawn   (and later, possibly, superseded)
Name real reviewers and a real review-by date. An open-ended comment period is how an RFC dies of
endless discussion; a named decider and a deadline are how it reaches a decision.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   rfc_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you circulate it: self-grade against rfc_guide.md, then DELETE every HTML comment.
-->

# {{title}}

## Summary

<!-- WHAT  Two or three sentences: what you are proposing and what changes if it is accepted. The
           whole idea, graspable before any detail.
     WHY   The summary is the triage surface; most reviewers decide from it whether to engage, and
           engagement is the entire value of an RFC.
           Deep dive: rfc_companion.md section 3 (Anatomy > Summary).
     ASK   What are you proposing? What becomes true if it ships? Who should care?
     GOOD  "Propose moving service-to-service auth from shared static tokens to short-lived mTLS
           certs issued by an internal CA, so a leaked credential expires in minutes."
     WEAK  "We should improve our auth." (a wish, not a proposal)
     TRAP  A summary that states the problem but never the proposed change. -->

{{summary}}

## Motivation

<!-- WHAT  The problem or opportunity and why it is worth solving now: the forces (technical,
           product, organizational) and the cost of doing nothing.
     WHY   Motivation earns the reader's attention and is what a reviewer argues with first. Thin
           motivation invites bikeshedding on the solution.
           Deep dive: rfc_companion.md section 3 (Anatomy > Motivation).
     ASK   What is wrong today? Who feels it, how often, at what cost? Why now?
     GOOD  "Static service tokens have leaked twice this year via logs; each rotation is a manual
           multi-team scramble, and the blast radius grows with every service we add."
     WEAK  "Our current approach is not best practice." (fashion, not cost)
     TRAP  Motivation reverse-engineered from your preferred solution, so only that option fits. -->

{{motivation}}

## Goals and Non-Goals

<!-- WHAT  Goals: what the proposal must achieve to succeed, ideally observable. Non-goals: what it
           is deliberately NOT trying to do, to keep the discussion bounded.
     WHY   Non-goals are the highest-value line of scope control in an RFC. Most runaway comment
           threads are reviewers arguing about something the author never intended to address;
           naming it a non-goal ends that thread before it starts.
           Deep dive: rfc_companion.md section 3 (Anatomy > Goals and Non-Goals).
     ASK   What must be true for this to have worked? What are we explicitly not solving here, and
           why? What is a reasonable-but-separate concern?
     GOOD  Goal: "Any leaked service credential is unusable within 15 minutes." Non-goal: "End-user
           auth. This RFC is service-to-service only; user sessions are out of scope and unchanged."
     WEAK  A goals list with no non-goals, so every reviewer expands the scope in a different way.
     TRAP  Omitting non-goals. It is the single most reliable cause of an RFC that will not converge. -->

{{goals_and_non_goals}}

## Proposal

<!-- WHAT  The proposed change at the level of a shared mental model: the core idea and how people
           experience it. Concrete enough to disagree with.
     WHY   This is the object of discussion. A vague proposal produces vague feedback and no
           decision. Deep dive: rfc_companion.md section 3 (Anatomy > Proposal).
     ASK   What exactly changes? What is the shape? What is in, and what is deferred?
     GOOD  "Stand up an internal CA. Each service gets a workload identity and a 15-minute cert,
           auto-renewed by a sidecar; the mesh rejects any connection without a valid cert."
     WEAK  "Adopt mTLS." (a technology name, not an evaluable proposal)
     TRAP  Lowest-level detail before the shape is clear, or so abstract no one can push on it. -->

{{proposal}}

## Detailed Design

<!-- WHAT  The how, for reviewers who must implement or integrate: interfaces, data flows, failure
           modes, migration, security and privacy surface. The parts a careful reviewer will probe.
     WHY   This is where a proposal that sounded fine reveals whether it actually works. The detail
           is what lets a domain expert catch the flaw now, on paper, instead of in production. It
           is also the section that most tempts over-writing; include what a reviewer needs to find
           problems, not everything you know. Deep dive: rfc_companion.md section 3 (Anatomy >
           Detailed Design).
     ASK   What are the interfaces and contracts? What are the failure modes and how are they
           handled? How does data migrate? What is the security, privacy, and compliance surface?
     GOOD  "Cert issuance flow (sequence). Sidecar renewal at 50% of TTL with jitter. CA outage
           behavior: existing certs remain valid to TTL; issuance pauses; a documented break-glass
           path. Identity bootstrap for new workloads via the orchestrator's attestation."
     WEAK  Repeating the Proposal at more length without adding anything a reviewer can test.
     TRAP  Using length as a weapon. An exhaustive design that no one can finish reading is how RFCs
           get approved by fatigue rather than by understanding. Detail the risky parts. -->

{{detailed_design}}

## Alternatives Considered

<!-- WHAT  The other options you genuinely weighed and why you are not proposing them. Include "do
           nothing" when it is real, which is usually.
     WHY   Alternatives are the evidence the proposal is reasoned rather than preferred, and they
           are how a reviewer surfaces the option you missed. Their absence invites the reader to
           supply them adversarially. Deep dive: rfc_companion.md section 3 (Anatomy > Alternatives
           Considered); the anti-pattern is in section 7.
     ASK   What else could meet the goals? What obvious option did you reject, and why? What would a
           skeptic propose? Why not "do nothing"?
     GOOD  "Auto-rotate static tokens (rejected: still a shared secret). Vendor mesh (rejected:
           cost, lock-in). Do nothing (rejected: the leak cost is already being paid)."
     WEAK  One decoy dismissed in half a sentence.
     TRAP  Straw men. Two decoys and a winner is a sales pitch, not an RFC. -->

{{alternatives_considered}}

## Drawbacks and Trade-offs

<!-- WHAT  The honest costs of the proposal itself: what gets worse, harder, or riskier if it is
           accepted. The price you are asking the org to pay.
     WHY   The drawbacks are what make the RFC trustworthy. A proposal presented with no downsides
           tells reviewers you are selling, not proposing, and it invites them to go find the cost
           you hid. Naming it yourself is disarming and faster.
           Deep dive: rfc_companion.md section 3 (Anatomy > Drawbacks and Trade-offs).
     ASK   What does this make worse? What new operational burden, dependency, or risk does it add?
           Who pays, and how much? What could go wrong at scale?
     GOOD  "Adds a CA as a new critical dependency, with its own uptime and recovery burden. Adds a
           sidecar to every pod (memory, one more failure surface). A CA compromise is now a
           system-wide event. The mesh becomes a hard requirement for all service traffic."
     WEAK  "There is a learning curve." (a cost nobody would act on)
     TRAP  A drawbacks section so weightless it is really an advantages section in disguise. If you
           cannot name a real cost, you have not understood the proposal yet. -->

{{drawbacks_and_tradeoffs}}

## Open Questions

<!-- WHAT  What is genuinely undecided or unknown, that you want input on. Real questions, ideally
           with who might answer.
     WHY   The open questions are the literal request for comment: they point reviewers at exactly
           where their input changes the outcome. An RFC with none is usually hiding them.
           Deep dive: rfc_companion.md section 3 (Anatomy > Open Questions).
     ASK   What are you unsure about? Where could a reviewer change your mind? What did you punt on?
     GOOD  "How do we bootstrap identity for a brand-new service? Must we support non-mesh clients?
           What is the CA's own rotation and recovery story?"
     WEAK  "None," on a proposal that plainly has unknowns.
     TRAP  Hiding hard questions to look finished. They resurface later as incidents. -->

{{open_questions}}

## Rollout and Adoption

<!-- WHAT  How the change actually reaches production and gets adopted: sequencing, flags, migration,
           backout, and how you will know it is working. Who has to do what.
     WHY   Many RFCs die at rollout, not at design: the idea is sound but no one owns the messy path
           to production, so it never ships. A credible adoption plan is often what separates an RFC
           that happens from one that is merely admired.
           Deep dive: rfc_companion.md section 3 (Anatomy > Rollout and Adoption).
     ASK   What is the sequence? What is behind a flag? How do teams migrate, and who supports them?
           What is the backout plan if it goes wrong? How do you measure success?
     GOOD  "Per-namespace behind a flag, dual-running static tokens until each namespace is cut over.
           Backout: disable the flag, fall back to tokens. Success: 100% of service traffic on mTLS,
           zero manual token rotations, by Q3. Platform owns the CA; each team owns its cutover."
     WEAK  "Roll it out gradually." (names no sequence, owner, or backout)
     TRAP  Treating rollout as an afterthought. The gap between an accepted design and a shipped
           change is where most proposals quietly die. -->

{{rollout_and_adoption}}

## Outcome

<!-- WHAT  The decision, once made: accepted, rejected, or deferred; who decided; the date; a
           one-line why; and what happens next. While the RFC is open, this says so.
     WHY   An RFC with no recorded outcome is the most common way the format fails: the discussion
           happens, the decision is reached somewhere off the page, and the document is abandoned
           mid-thread. This section turns the proposal into a durable record and is what an ADR is
           later written FROM. Deep dive: rfc_companion.md section 3 (Anatomy > Outcome); the RFC-to-
           ADR relationship is in section 8.
     ASK   Has a decision been made? By whom, when? If accepted, what is the resulting ADR or
           tracking issue? If deferred, what reopens it?
     GOOD  "Accepted 2026-05-02 by the Platform review group, on condition that the break-glass path
           is designed first (open question 3). Rollout tracked in PLAT-1421. Recorded as ADR 0031."
     WEAK  Blank, because "it is still open." Instead: "Status: in review, decision due 2026-05-02."
     TRAP  Never filling this in. An RFC that does not record its own outcome is indistinguishable
           from one that was ignored. Set the status and write the line the moment it is decided. -->

{{outcome}}
