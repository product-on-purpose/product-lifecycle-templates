---
status: "{{status}}"
date: "{{date}}"
decision-makers: ["{{decision_makers}}"]
doc_type: adr
size: lean
source_template: adr
source_template_version: 0.1.0
---

<!--
LEAN ADR. The three sections MADR marks mandatory, and nothing else. This is the right default:
most decisions are recorded honestly in half a page, and a short record that gets written beats a
thorough one that does not. To grow this into a full ADR, ADD sections (see adr_template-full.md);
never rename or reorder the ones below, because the full variant is a strict superset of this one.

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

## Considered Options

<!-- WHAT  The options genuinely on the table. Titles only here; the reason the winner won goes in
           Decision Outcome below. (The full variant adds a "Pros and Cons of the Options" section
           for weighing each one properly. If you find you need it, you want that variant.)
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
           decided ...". Then the consequences, honestly, both directions.
     WHY   Active voice puts a decision-maker back into the sentence. Passive voice ("it was
           decided") is how a record becomes accountability theater: everyone signed, nobody chose.
           Deep dive: adr_companion.md section 3 (Anatomy > Decision Outcome); the
           responsibility-deflection failure is in section 7.
     ASK   Which option, and because of what? What gets harder now? What are we knowingly paying?
     GOOD  "Chosen option: the meta is the contract, because it lets the gate tell a deliberately
           single-size bundle apart from a half-built one, which is the only thing a governance
           gate exists to do."
     WEAK  "After discussion, option A was selected as the best fit." (no agent, no reason)
     TRAP  Listing only good consequences. Nygard is explicit that ALL consequences are listed,
           not just the positive ones. A record with no cost is a record nobody believes. -->

Chosen option: "{{chosen_option}}", because {{justification}}.

### Consequences

<!-- WHAT  What becomes easier, and what becomes harder. Name the price you agreed to pay.
     WHY   The negative consequences are the highest-value lines in the whole record. They are
           what a future reader checks against reality to decide whether the decision still holds.
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
