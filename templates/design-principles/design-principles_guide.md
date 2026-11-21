# Guide: Design Principles (operator card)

The short card. The reasoning behind every rule here, with the sources, is in
[`design-principles_companion.md`](design-principles_companion.md). A fully worked instance is
[`design-principles_example.md`](design-principles_example.md). Where this card calls something the
library's position, no source read for the bundle publishes it, and the card says so each time.

**What this document decides.** A design principles document settles how an interaction, a message or
a screen should behave for the person using it when two good options compete. It does not settle what
the team builds, funds or declines. That test is the library's own inference, at medium-low confidence.
No source read draws the line in so many words, and published sets cross it, so some principles will
straddle. The Purpose and Scope section has a field where the document says which ones do.

**What to call it.** NN/g's own longer name for this type begins with the word "product", and it
collides with the sibling bundle `product-principles`. This bundle does not use that name. Its safe
aliases are "UX design principles" and "experience principles".

## When to use

- The team keeps arguing the same trade-off between two good options, and nothing written says which
  way to lean. Jay Mistry's stated goal for a set is to end repeated debates, not all debate.
- Design critique or review comes down to personal preference. GitLab's critique sessions tell
  designers to "Connect feedback to user needs and business goals instead of personal preference".
- A new product or surface has joined, and nobody can say whether the existing set covers it. Jared
  Spool's test asks "Have You Evaluated it for This Project?", and Purpose and Scope holds the answer.
- A set already exists and nobody cites it. Grade it with the rubric below, then rewrite the rows that
  score 0.
- A team is about to amend or replace a set and wants the reason on record. The Ownership and Changes
  section holds that record.

## When NOT to use

Several documents get mistaken for design principles. The table says which one you likely need.

| You actually need | Because |
|---|---|
| **Product principles** | Those settle what the team builds, funds or declines. This document settles how an interaction, a message or a screen behaves. The line is the library's, at medium-low confidence, and published sets cross it. When a principle straddles, say so in the Purpose and Scope field built for it. |
| **A design system** | NN/g says these principles are "not directions on how to design specific UI elements (like design patterns or standards)". Component rules and pattern guidance belong to a design system. Purpose and Scope states the relation, because the sources split. |
| **General usability heuristics or principles of good design** | NN/g separates a product's own principles from "usability guidelines, heuristics, or visual-design principles". Heuristics are universal, and a team's principles are specific to its product. |
| **A team charter** | A charter governs how a team works. A set of principles frames design decisions about the product. |
| **A definition of done** | Both are standing standards that work is judged against. The [definition of done](../definition-of-done/definition-of-done_guide.md) judges whether an increment is finished. Design principles judge which design choice to make. |
| **A product vision** | The [product vision](../product-vision/product-vision_guide.md) says where the product is going, and it sits upstream. A principle says how every design decision on the way should lean. |
| **A design brief** | The [design brief](../design-brief/design-brief_guide.md) hands one chosen concept to the people who design it. A brief may cite the principles, and the principles outlive every brief. |

## Pick a variant

This bundle ships one size, lean, so there is no variant to choose. The reason is in
[`design-principles_companion.md` section 4](design-principles_companion.md#4-variants-and-sizing).
Three choices remain inside it.

1. **How many principles.** Three to five is advice, not a finding, and the template ships three
   principle blocks. Add a fourth or fifth only when you can attach a real decision to it.
2. **How the design system relates.** The set can sit inside the design system or beside it. State
   which, because the template prescribes neither.
3. **Which fields to leave honest.** If a principle has no source or settled case yet, write N/A and one
   line of why. Do not invent a source or a case.

## Run these tests on each principle before you grade

1. **The opposite test.** Mistry writes: "If you can't imagine another successful product using the
   opposite approach, you don't have a principle - you have a platitude." Name the team or product that
   would reasonably choose the opposite. If you cannot, rewrite the statement.
2. **The say-no test.** Spool asks "Does it Help You Say 'No' Most of the Time?" Write down a design the
   team can no longer ship because of the principle. That is the "What it rules out" field.
3. **The what-does-it-settle test.** Ask what the principle decides. If it decides how an interaction, a
   message or a screen behaves for its user, it belongs here. If it decides what the team builds, funds or
   declines, it belongs in `product-principles`. If it decides both, say so in the straddling field.

## Quality rubric (self-grade)

Score each row 0, 1 or 2. A score under 15 out of 22 means several rows are thin or empty, so the set is
not yet a standard a designer can lean on. The total does not say which rows failed. Read the rows that
scored 0 first, because a missing conflict resolution (row 6) or a missing owner (row 8) leaves a
designer with no way to choose or no one to ask, even in a set that scores well elsewhere. Grade what
the author added to the blank template. The template already prints the field labels and the Review
Trigger conditions, so a row that rewards their presence is satisfied before anyone writes a word.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Scope is bounded** | No product is named, or the scope covers "everything we make" | The product and its readers are named, but nothing says which kinds of decision the set does not settle, or how it relates to a design system | You can point at the sentence naming the product, the people who apply the set and the relation to the design system, and at one kind of decision the set refuses to settle and where that decision goes instead |
| 2 | **Principles rule something out** | The rules-out field is blank, restates the statement, or names "bad experiences" | Some principles name a choice a team could have made, and others rule out only what nobody would choose | For every principle you can point at a design the team could have shipped and now cannot, and a colleague who did not write it can state the opposite approach and say who might reasonably choose it |
| 3 | **Questions are askable** | The reviewer question restates the statement, asks whether the design is good, or is blank | Each principle has a question, but two reviewers could answer it differently about the same screen | For every principle, a reviewer who did not write the set can put the question to a proposed design and reach an answer they could defend in a critique |
| 4 | **Principles rest on something** | The field reads "best practice" or is blank | A source is named but a reader cannot find it or it does not support the statement, or the field says plainly that no source exists yet | You can open the interview round, decision record or stated value the field names, and it supports the statement it sits under |
| 5 | **Cases are real** | The field says "many", describes a case no one can place, or is blank | A case is described, but the same outcome would have followed without the principle, or the option it turned down is not named, or the field says plainly that no decision has met the principle yet | You can point at the critique, ticket or decision record where the principle settled something, and the option it turned down is named |
| 6 | **A conflict is resolved** | The section says every principle matters equally, or is blank | Two principles are named and a winner is stated, but the kind of decision is "everything" or no reason is given | You can point at two principles, a named kind of decision where they collide, which one wins there and why, and a designer could apply it to the next decision of that kind without asking the author |
| 7 | **Use has a place** | The section says designers should keep the principles in mind, or is blank | Moments of use are named, but the form of a citation, or what a reviewer may do when a decision sets a principle aside, is missing | You can point at the moments where the set is cited, at the line a decision record carries, and at what a reviewer may do when a principle is set aside, and someone who was not in the room could write that line |
| 8 | **Owner is reachable** | "The team", or no owner | A role is named without a person, or the place to propose a change or who decides is missing | You can point at the role and person who own the set, the place where anyone proposes a change and who decides, and you could message the owner today |
| 9 | **Changes keep reasons** | The log is blank, or each entry is a date and the word "updated" | Entries say what changed but not what fired the change, or a retirement leaves no reason | The log opens with the date the set was first agreed. Each later entry says what changed in a sentence a stranger could follow and names the Review Trigger row that fired it. A retired principle keeps its reason and sits in an archive, not out of the document |
| 10 | **Triggers carry owners** | The Review Trigger table is blank, or every owner is "the team" | Some conditions have a role and an action, but at least one has neither, or the only observable condition is a date | Every condition has a role as owner and an action that person takes, such as reopening the set or writing a dated line in the log, and any condition that has already fired points at its line in the change log |
| 11 | **Direction, not craft** | Several principles name a component or a pattern, or settle what the team builds or declines, or the set holds no principles, or the straddling field is blank | The statements are clean, but the straddling field says "None" with no reason, or a principle that straddles the product-principles line is not named in it | At least one principle is present, and you can apply the what-does-it-settle test to each: it decides how an interaction, a message or a screen behaves, and the straddling field names every principle that also decides what is built, or says "None" and gives the reason |

Every cell above describes evidence, not a count. The test for each cell is whether someone could
satisfy it without improving the document. If they could, the cell is written wrong. The rubric does
not grade how many principles the set holds, because the number is advice and not a finding.

Rows 4 and 5 grade two fields that published sets rarely carry. An honest "none yet" scores 1 on both
rows, so a new set can clear the line without inventing a source or a settled case. Grade with someone
who did not write the set. The blank template should score 0 on every row.

## Named anti-patterns (the usual wrecks)

Each entry gives the failure, the test that catches it and the rubric row it costs. The arguments behind
them, and the disputes among sources, are in the companion's sections 6 and 7.

1. **The slogan.** A statement with no decision it would change. Test: could a designer disagree with
   it? Costs row 2.
2. **The platitude.** A principle whose opposite nobody would choose. Test: Mistry's opposite test. Costs
   row 2.
3. **Too many.** The figures sources give are heuristics, and none cites a measurement. Test: can you
   attach a real decision to each one? Costs row 5.
4. **A UI direction dressed as a principle.** A statement that names a component belongs to the design
   system. Test: does it name a component or a pattern? Costs row 11.
5. **Values mistaken for principles.** Brignell: "Values shape culture. Principles shape decisions." Test:
   what decision does it settle? Costs row 2.
6. **No stated order when two collide.** Brignell: "If everything is equally important, nothing actually
   guides the decision." Test: does the table name a winner in a named kind of decision? Costs row 6.
7. **Overlapping principles.** Spotify's audit named "Overlapping concepts" as a defect. Test: do two
   principles settle the same decision? Merge or retire one. Costs rows 5 and 9.
8. **A set nobody cites.** The library's inference is that a set with no stated moment of use risks being
   read once and not applied. Test: could someone who was not in the room write the citation line? Costs
   row 7.
9. **A standard read as a rule book.** GOV.UK says "This isn't a straitjacket or a rule book." Test: does
   a decision cite the principle it leaned on and the one it set aside, with a reason? A citation so
   mechanical that it becomes a checkbox has lost that reading. Costs row 7.
10. **A set that never changes, or changes with no record.** Test: does the log keep the reason for each
    retirement, and does each trigger name an owner? Costs rows 8, 9 and 10.
11. **Borrowing another team's set.** Only the NHS page read states a reuse licence, and Productboard's
    prompt reserves its rights. Test: would the opposite test hold for your product? Write the team's own
    words. Costs row 2.
12. **A set that restates the current strategy.** The library's own caution, not a sourced one. Test:
    would the principle survive a change of strategy while its evidence holds? Costs row 4.
13. **Presenting the library's positions as received practice.** Published sets carry the statement and,
    in three of the five tabulated, the reviewer's question. What it rules out appears only in a vendor's
    AI prompt (Productboard). What it rests on appears in no set read. A decision it settled has partial
    precedent in GitLab Pajamas' "Example in practice" and GOV.UK's linked case studies. The role names
    in Ownership and the table form of the Review Trigger are also the library's. A filled set may keep
    them and should not describe them as a standard.

## Pairing with your process

This bundle ships in the `standing-standards` family as a **foundation**: a standard that a team's
experience decisions are judged against. The reasoning is in
[ADR 0089 (design principles joins standing-standards as a foundation)](../../docs/internal/decisions/0089-design-principles-joins-standing-standards-as-a-foundation.md).
Update the set when a Review Trigger condition fires, not on a calendar, because no source read states a
revision interval. A done criterion may say that work was reviewed against the principles, and the
principles own the content of that review.

## What the research did not settle

The companion's section 6 lists the open disputes: conflict, ranking, generic principles, the right
count and the two kinds of principles. Sections 2, 5 and 9 list what the research did not find, among it
who started the practice, any tie to a delivery methodology, and any research on regulated products or a
solo author. The template is untested for both of the last two.

## When it is good enough

When a designer who did not write the set can take the next real choice between two good options, name
the principle that decides it, say what that principle rules out, and say which principle wins if a
second one pulls the other way. And when the page names who owns the set and what event reopens it.

Then delete every HTML comment. Keep the `source_template` and `source_template_version` frontmatter
fields, because they are the only record of which template and version produced the document.
