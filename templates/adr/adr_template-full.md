---
status: "{{status}}"
date: "{{date}}"
decision-makers: ["{{decision_makers}}"]
consulted: ["{{consulted}}"]
informed: ["{{informed}}"]
doc_type: adr
size: full
source_template: adr
source_template_version: 0.1.0
---

<!--
FULL ADR. Every section MADR defines, mandatory and optional. Use this weight only when the
decision earns it: it is hard to reverse, it is contested, it crosses teams, it carries
regulatory or safety weight, or you expect to be asked to defend it.

Most decisions do not earn it. The lean variant (adr_template-lean.md) is the default, and
reaching for this one by reflex is how a decisions folder fills up with ceremony nobody reads.
The full variant is a strict superset of lean: the shared sections keep their names and their
order, and this file only ADDS.

WHERE THIS FILE GOES
  docs/internal/decisions/NNNN-short-kebab-title.md
Numbered sequentially from 0001. Numbers are never reused, not even for a record that ends up
rejected or superseded. The number is an address, not a ranking.

IMMUTABILITY, THE RULE THAT MAKES THIS ARTIFACT WORTH ANYTHING
Once this record is accepted, do not rewrite the decision. Write a NEW record and set this one's
status to "superseded by ADR-NNNN". A decisions folder that silently rewrites itself is just a
wiki with extra steps. The trail is the product.
(One narrow exception, and only one: a factual error in the record, as opposed to a change in the
decision, is corrected in place with the correction dated and the error named. See
adr_companion.md section 6 for why that line sits exactly there.)

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   adr_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid.
2. Replace each {{placeholder}} with your content.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you ship: self-grade against adr_guide.md, then DELETE every HTML comment. They are
   guidance, not content.
-->

# {{title}}

<!-- WHAT  A short title naming BOTH the problem solved and the option chosen, in plain words.
           Phrased as a statement, not a question.
     WHY   The title is the only part of this record most people will ever read. A decisions
           directory is browsed as a list of filenames; a title that names a topic instead of a
           decision is invisible in that list.
           Deep dive: adr_companion.md section 3 (Anatomy > Title).
     ASK   What was the problem? What did we choose? Scanning the folder, would a stranger know?
     GOOD  "The meta declares the size contract; single-size bundles are a legal shape"
     WEAK  "Database decision" (a topic, not a decision; nobody can act on it)
     TRAP  Naming the topic rather than the decision. "Caching" is a folder name. "Use Redis for
           the session cache, accepting a new operational dependency" is a record. -->

## Context and Problem Statement

<!-- WHAT  The forces in play, and the problem they create, in two or three sentences or a short
           story. Make the SCOPE explicit: name the components or boundaries this decision binds.
     WHY   Context is what expires. The decision may stay right while the reason for it quietly
           stops being true, and the only way a future reader can tell is if you wrote down the
           conditions you were under. This section is the record's shelf-life label.
           Deep dive: adr_companion.md section 3 (Anatomy > Context and Problem Statement).
     ASK   What forces are pressing (technical, business, organizational)? What constraint,
           deadline, or skill gap is real? What breaks if we do nothing? What does this bind?
     GOOD  "Seven of the 27 Tier-1 types are single-size, so the next bundle we build is likely to
           be one, and the gate cannot pass it: two checks hardcode the assumption that every
           bundle ships exactly lean and full."
     WEAK  "We need to decide on our caching strategy." (restates that a decision exists; names
           no force, no constraint, and nothing that would ever stop being true)
     TRAP  Writing the context AFTER the decision, as justification. Then it records the argument
           you won, not the situation you were in, and it teaches a future reader nothing. -->

{{context_and_problem}}

## Decision Drivers

<!-- WHAT  The criteria the decision is actually being judged against: the qualities you must
           have, the constraints you cannot break, the forces you must resolve.
     WHY   Drivers are what turn an opinion into a decision. Stated up front, they are the
           yardstick every option gets measured with, and they are what stops the comparison
           below from being a rationalization of the answer you already liked.
           Deep dive: adr_companion.md section 3 (Anatomy > Decision Drivers).
     ASK   What quality must this protect (latency, cost, auditability, reversibility)? What
           constraint is non-negotiable? Which driver wins if two of them collide?
     GOOD  * "The gate must be able to distinguish a deliberately single-size bundle from a
             half-built one. This is the k.o. criterion: an option that fails it is out."
           * "No empty variant padded out of obligation (see ADR 0002, the variant model)."
     WEAK  "It should be good and maintainable."
     TRAP  Writing drivers that no option could ever fail. If every option satisfies every
           driver, the drivers are decoration and the real reason is still unwritten. Say which
           driver is the knockout. -->

* {{decision_driver_1}}
* {{decision_driver_2}}

## Considered Options

<!-- WHAT  The options genuinely on the table. Titles only here; the reasoning lives below in
           "Pros and Cons of the Options".
     WHY   The rejected options are the reason this artifact exists. A record that lists only the
           winner cannot answer the one question it will actually be asked, which is "did you
           think about X?" Without the alternatives, a future team re-litigates from zero.
           Deep dive: adr_companion.md section 3 (Anatomy > Considered Options), and the
           anti-pattern in section 7 (recording the decision but not the alternatives).
     ASK   What else was seriously on the table? What was the obvious option we rejected, and the
           one a newcomer will ask about in six months? Is "do nothing" one of them?
     GOOD  * Make the meta the size contract, enforced in both directions
           * Waive the checks whenever a variant file is absent
           * Require every type to ship two variants, padding out a full for single-size types
     WEAK  A single bullet, or a list padded with options nobody would ever have chosen.
     TRAP  Straw men. Two decoys and a winner is not a decision record, it is a press release.
           If an option was never real, leave it out and say so if it comes up. -->

* {{option_1}}
* {{option_2}}
* {{option_3}}

## Decision Outcome

<!-- WHAT  The option chosen, and the justification, in active voice: "We will ...", not "It was
           decided ...".
     WHY   Active voice puts a decision-maker back into the sentence. Passive voice ("it was
           decided") is how a record becomes accountability theater: everyone signed, nobody chose.
           Deep dive: adr_companion.md section 3 (Anatomy > Decision Outcome); the
           responsibility-deflection failure is in section 7.
     ASK   Which option, and against which driver did it win? Who is accountable for this?
     GOOD  "Chosen option: the meta is the contract, because it lets the gate tell a deliberately
           single-size bundle apart from a half-built one, which is the only thing a governance
           gate exists to do."
     WEAK  "After discussion, option A was selected as the best fit." (no agent, no reason)
     TRAP  Justifying the winner without ever referring back to a driver. If the reason it won is
           not one of the criteria you listed above, one of the two sections is lying. -->

Chosen option: "{{chosen_option}}", because {{justification}}.

### Consequences

<!-- WHAT  What becomes easier, and what becomes harder. Name the price you agreed to pay.
     WHY   The negative consequences are the highest-value lines in the whole record. They are
           what a future reader checks against reality to decide whether the decision still holds.
           Nygard is explicit: ALL consequences are listed, not just the positive ones.
           Deep dive: adr_companion.md section 3 (Anatomy > Consequences).
     ASK   What is now harder or more expensive? What risk did we accept on purpose? What would
           have to become true for this to have been the wrong call?
     GOOD  Bad, because "sizes_available is now load-bearing: a bundle whose meta omits it fails
           the gate rather than being skipped. That is a deliberate behavior change. A contract
           you can silently omit is not a contract."
     WEAK  "Bad, because there is a small learning curve." (a cost nobody would ever act on)
     TRAP  A "Bad, because" line so weightless it is really a "Good" in disguise. If you cannot
           name a real cost, you have probably not understood the decision yet. -->

* Good, because {{positive_consequence}}
* Bad, because {{negative_consequence}}

### Confirmation

<!-- WHAT  How anyone can check that the implementation actually complies with this decision.
           Name the fitness function: the test, the lint rule, the CI check, the review step.
     WHY   This is the section that separates a decision that binds from a decision that merely
           happened. An ADR nobody checks is a comment; an ADR a machine checks is a constraint.
           It is also the section teams skip most often, which is why so many decisions folders
           document an architecture the codebase no longer has.
           Deep dive: adr_companion.md section 3 (Anatomy > Confirmation) and section 6 (the
           AI-era argument for machine-checkable decisions).
     ASK   What automated check would fail if someone violated this tomorrow? If none can exist,
           what manual review step catches it, and who runs it?
     GOOD  "CI check F in tools/check-bundles.py enforces this on every push: sizes_available
           must exist, be non-empty, and use exactly one vocabulary. Verified against six
           fixtures, including a bundle with an undeclared stray variant file, which fails."
     WEAK  "The team will keep this in mind during code review."
     TRAP  Leaving this blank because no automated check exists. If the honest answer is "nothing
           enforces this", write THAT down. It is a real and useful finding about how much the
           decision is actually worth. -->

{{confirmation}}

## Pros and Cons of the Options

<!-- WHAT  Each option, weighed against the decision drivers above. Including the one you chose.
     WHY   This is the audit trail of the thinking, and it is what makes the record defensible
           rather than merely declarative. Weighing the WINNER honestly (it has real cons, or it
           would not have been a decision) is what signals the analysis was real.
           Deep dive: adr_companion.md section 3 (Anatomy > Pros and Cons of the Options).
     ASK   For each option: what does it buy, what does it cost, and which driver kills it?
     GOOD  "Good, because it needs no new dependency. Bad, because it cannot distinguish intent
           from incompletion, which is the knockout driver. Rejected on that ground alone."
     WEAK  Every rejected option getting a single "Bad, because it is worse."
     TRAP  A winner with no cons listed. It tells the reader you were selling, not deciding, and
           it is the fastest way to lose their trust in the rest of the record. -->

### {{option_1}}

* Good, because {{option_1_pro}}
* Bad, because {{option_1_con}}

### {{option_2}}

* Good, because {{option_2_pro}}
* Bad, because {{option_2_con}}

## More Information

<!-- WHAT  Whatever a future reader needs and cannot get from the sections above: links to related
           records, the evidence behind the call, the team agreement, and when this should be
           revisited.
     WHY   This is where you set the record's expiry. A decision made under conditions that will
           predictably change should say so, with a trigger, so that the next team knows whether
           they are reading history or law.
           Deep dive: adr_companion.md section 3 (Anatomy > More Information).
     ASK   Which records does this supersede, refine, or depend on? What evidence backs it? What
           event should make us revisit it?
     GOOD  "Refines ADR 0002 (the variant model), which flagged this exact loose end in its own
           consequences. Revisit if a third size vocabulary is ever proposed."
     WEAK  A bare link dump with no statement of the relationship.
     TRAP  Using this as a junk drawer. If a link matters to the decision, say in one clause WHY
           it matters; if it does not, leave it out. -->

{{more_information}}
