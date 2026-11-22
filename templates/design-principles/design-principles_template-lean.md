---
title: "{{product_name}} Design Principles"
doc_type: design-principles
size: lean
product_name: "{{product_name}}"
owner: "{{owner}}"
status: draft
doc_version: "{{doc_version}}"
created: "{{date}}"
updated: "{{date}}"
related_links: []
source_template: design-principles
source_template_version: 0.1.1
---

<!--
LEAN DESIGN PRINCIPLES. This bundle ships one size, deliberately. No source the research read publishes a
fuller and a shorter version of one set. The only condensed forms found are a PDF GitLab links and an NHS
poster, and the research opened neither. NN/g warns that "having 10 or more leads to many being
forgotten", and Brignell writes "The most effective examples use 3-5 principles." So the document is
short on purpose, and a longer variant would model the weight the research rejected. The sources that
add detail add it per principle, not per document, and so does this template. Confidence in the single
size is medium-high. See design-principles_companion.md section 4 (Variants and sizing).

A DESIGN PRINCIPLES DOCUMENT IS A SHORT STANDING LIST OF VALUE STATEMENTS that a team agrees once and
then uses to frame and settle decisions about its product's experience. This family reads that as a
standard decisions are judged against. It is a standard applied by judgement, not by checkbox: GOV.UK
says "This isn't a straitjacket or a rule book." and Brignell writes "Unlike rules, which prescribe a
specific outcome, principles guide judgement." See design-principles_companion.md section 6 (Debates and
contested boundaries).

SOME OF THIS STRUCTURE IS THIS LIBRARY'S OWN POSITION, NOT RECEIVED PRACTICE.
No source the research read publishes a template for this type, so every section here is assembled from
published sets and method articles. Each principle below carries five fields. Published sets carry the
statement and, in three of the five tabulated, the reviewer's question. What it rules out appears only in
a vendor's AI prompt (Productboard). What it rests on appears in no set read. A decision it settled has
partial precedent in GitLab Pajamas' "Example in practice" and GOV.UK's linked case studies. Where a
section is the library's
position, its comment says so. No source shows that keeping such a document
improves outcomes. The research found no source on solo practitioners or regulated products, so the
template is untested for both.

WHAT THIS IS NOT
It is NOT a design system. NN/g says these principles are "not directions on how to design specific UI
elements (like design patterns or standards)", so on this library's reading, component rules and
pattern guidance belong to a design system. It is NOT a set of general usability heuristics, because
NN/g separates a team's own principles from "usability guidelines, heuristics, or visual-design
principles".
It is NOT a list of what the team builds, funds or declines. The line with the sibling product-principles
bundle is this library's, not the sources', and published sets cross it. The working test, at medium-low
confidence, is to ask what a principle settles. If it settles how an interaction, a message or a screen
should behave for its user, it belongs here. If it settles what the team builds, funds or declines, it
belongs in product principles. Some principles straddle, and this document should say so rather than
hide them. The last field of Purpose and Scope is where it says so.
Do not call this type by NN/g's longer name, which begins with the word "product". That name collides
with the sibling bundle.

All names, dates and figures in the GOOD and WEAK illustrations below are invented.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   design-principles_companion.md for the deep reasoning), guiding questions to ASK, a GOOD and a WEAK
   example, and the TRAP to avoid. The When Principles Conflict, Ownership and Changes and Review Trigger
   tables also carry PRIORITY and ROW HINT.
2. Replace each {{placeholder}} with your content. Draft Purpose and Scope first, then The Principles,
   then When Principles Conflict, then the rest. Within The Principles, start from a decision the team
   has argued about, ask which option a principle would have chosen, then write what it ruled out.
3. If a section, or one row inside a table, does not apply, write "N/A" and one line of why, rather than
   leaving it blank or deleting the section. An unexplained blank and a skipped item look identical to a
   later reader.
4. This is a standing document, revisited on the Review Trigger below, not written once and forgotten.
   Before you first share it: self-grade against design-principles_guide.md, then DELETE every HTML
   comment. They are guidance, not content. Keep the source_template and source_template_version
   frontmatter fields: they are the only record of which template and version produced this document.
-->

# {{product_name}} Design Principles

## Purpose and Scope

<!-- WHAT  The product or service these principles cover, who applies them, how they relate to the design
           system, which kinds of decision they do not settle, and which principles, if any, also settle what the
           team builds.
     WHY   NN/g says "Design principles are specific to the product or service that is being designed."
           Brignell makes the same point: "Design principles are unique to an organisation, team or
           project." A set with no stated scope leaves a new product with no way to know whether the set
           covers it, and that reading is this library's. Spool's test asks the question directly: "Have
           You Evaluated it for This Project?" Blackie separates industry heuristics, team principles and
           business or program principles, which implies that a set should say which kind it is. The
           relation to the design system is this library's position, because the sources split. GitLab
           says "Our design principles are outlined in the Pajamas Design System and guide all product
           design work." The U.S. Web Design System says "These design principles are one set of shared
           values, and the design language of the U.S. Web Design System is another." This template asks
           the author to state the relation and prescribes neither. The last two fields are where the line
           with product principles is first drawn, and that line is this library's. Published sets cross
           it: one of NN/g's own example principles is "Prioritize user needs over business
           constraints.", and USWDS's principle on earning trust asks about data privacy and
           continuous-integration testing. So some principles will straddle the line. The last field asks
           the author to name them and say why, or to write "None" with a reason, and it is the library's
           position. No source read asks for it.
           Deep dive: design-principles_companion.md section 3 (Anatomy > Purpose and Scope).
     ASK   Which product or products does this set cover, and who applies it: designers only, or designers
           and product managers and engineers? Does a design system exist, and does this set sit inside
           it or beside it? Which kinds of decision does this set not settle? Which principles, if any,
           also decide what the team builds, and why?
     GOOD  "These principles cover the Linden Transit journey planner, in its app and on its website. The
           designers, the two product managers and the front-end engineers apply them. They sit beside
           the Linden design system, which holds the components, and are linked from its front page. They
           do not decide which routes or features the team builds. That belongs in the product
           principles." For the last field: "Principle 4, Work without a signal, also settles what the
           team builds, because working offline means funding an offline timetable, and that is a
           product choice. This set settles only how the screen behaves when there is no signal."
     WEAK  "These principles apply to everything we make." (names no product, no reader and no design
           system, and gives a new product no way to tell whether it is covered) For the last field:
           "None." (gives no reason, so a reader cannot tell whether the author tested each principle
           or never looked)
     TRAP  A scope that drifts toward what the team should build or decline. That has strayed into
           product principles. It is a library judgement and no source states it. A close cousin is
           writing "None" in the last field without applying the what-does-it-settle test to each
           principle. -->

**Product or service covered:** {{product_covered}}

**Who applies this set:** {{set_appliers}}

**Relation to the design system:** {{design_system_relation}}

**Decisions this set does not settle:** {{out_of_scope_decisions}}

**Principles that also settle what the team builds:** {{straddling_principles}}

## The Principles

<!-- WHAT  Three to five principles. Each carries five fields: a statement, what it rules out, the
           question a reviewer asks, what it rests on, and a decision it settled. This section is the
           document. Copy the block below to add a fourth or fifth principle.
     WHY   NN/g's definition makes principles the thing that "frame design decisions", so each has to be
           specific enough to frame one. The three to five figure is advice, not a finding. Brignell
           writes "The most effective examples use 3-5 principles.", Kholmatova's slides say "not more
           than 3-5", and Mistry writes "Limit to 3-4 maximum." None of them cites a measurement. Each
           field has a source or is labelled. STATEMENT: all five sets tabulated carry one. WHAT IT
           RULES OUT: Productboard's AI prompt, a vendor's prompt and not a published set, has a field
           headed "What it rules out:", and Spool's test asks "Does it Help You Say 'No' Most of the
           Time?" No published set read carries the field, so asking for it is this library's position.
           Brignell writes "A slogan describes intent. A principle guides a choice." Mistry's opposite
           test is the check: "If you can't imagine another successful product using the opposite
           approach, you don't have a principle - you have a platitude." THE QUESTION A REVIEWER ASKS:
           GitLab's pages say "When designing any feature, ask:", IBM gives four to six yes-or-no
           questions per principle, and USWDS gives "Key considerations". WHAT IT RESTS ON: Spool's first
           test asks "Does It Come Directly From Research?", and the NHS states a provenance for its set.
           No published set read carries this field, so it is this library's addition. A DECISION IT
           SETTLED: GitLab gives each principle an "Example in practice", GOV.UK links case studies, and
           Spotify reports "The more examples, the better". Asking for one real case on every
           principle, and for the option it turned down, is this library's addition.
           The wording should be the team's own. The NHS and GOV.UK pages state a reuse licence, the
           Open Government Licence v3.0, except where otherwise stated, and Productboard reserves its
           rights. The other pages read state no licence in the text read, which is not proof that none
           exists.
           Deep dive: design-principles_companion.md section 3 (Anatomy > The Principles) and section 6
           (Debates and contested boundaries).
     ASK   Which decision has the team argued about, which option did this principle choose, and which
           option did it turn down? What can the team no longer do once it adopts the principle, and
           could a designer disagree with the statement? What question would a reviewer put to a proposed
           design? What research, earlier decision or stated value does it come from, and which real case
           did it settle?
     GOOD  Principle 1: "Show the next departure first." Statement: "Whenever a rider opens the app at a
           stop, the first thing on the screen is the time of the next vehicle for the stop they are most
           likely at." Rules out: "A home screen that opens on news, promotions or a map the rider must
           pan before any time appears." Reviewer question: "If the rider looks at this screen for two
           seconds, can they say when the next vehicle leaves?" Rests on: "The invented March rider
           interviews, in which riders opened the app at a stop and left when no time appeared." Decision
           it settled: "We turned down keeping the service-alerts banner above the departure time and moved
           it to a one-line note under it, after a critique showed the banner pushing the time off the
           first screen."
     WEAK  Principle 1: "Delight the user." Rules out: "Bad experiences." Reviewer question: "Is it
           delightful?" Rests on: "Best practice." Decision it settled: "Many." (a slogan: nobody would
           choose the opposite, so it rules nothing out, and no field names a real decision or a real
           source)
     TRAP  A principle that rules nothing out, which no source read defends: the Slogan or decision
           tool debate in the companion treats it as a failure. A close cousin is a UI direction in disguise: a statement that
           names a component belongs in the design system, as NN/g's separation shows. A last slip is
           copying a published principle and its wording from another team's set. A set written for
           another product may not pass the opposite test. -->

**Principle 1: {{principle_1_name}}**

- **Statement:** {{principle_1_statement}}
- **What it rules out:** {{principle_1_rules_out}}
- **The question a reviewer asks:** {{principle_1_reviewer_question}}
- **What it rests on:** {{principle_1_rests_on}}
- **A decision it settled:** {{principle_1_decision_settled}}

**Principle 2: {{principle_2_name}}**

- **Statement:** {{principle_2_statement}}
- **What it rules out:** {{principle_2_rules_out}}
- **The question a reviewer asks:** {{principle_2_reviewer_question}}
- **What it rests on:** {{principle_2_rests_on}}
- **A decision it settled:** {{principle_2_decision_settled}}

**Principle 3: {{principle_3_name}}**

- **Statement:** {{principle_3_statement}}
- **What it rules out:** {{principle_3_rules_out}}
- **The question a reviewer asks:** {{principle_3_reviewer_question}}
- **What it rests on:** {{principle_3_rests_on}}
- **A decision it settled:** {{principle_3_decision_settled}}

## When Principles Conflict

<!-- WHAT  A table that says which principle wins when two pull apart, and in which kind of decision.
     WHY   NN/g's method has a step titled "Identify Any Common Tradeoffs" and tells the author to "Take
           a stand on which value is important". Brignell writes "Real principles reveal priorities.",
           "Sometimes consistency conflicts with clarity." and "If everything is equally important,
           nothing actually guides the decision." THIS SECTION TAKES A SIDE IN A LIVE DISPUTE, AND THE SIDE
           IS THIS LIBRARY'S POSITION. NN/g also says a principle should "Not conflict with one another",
           and Blackie lists "Non-conflicting:" among his criteria. The dispute is narrower than it
           looks: in the same passage NN/g says that where two principles matter in different
           contexts, a team should "clearly specify in which contexts one of these principles is more
           important than the other". This library reads that sentence and Brignell's as asking for
           the same thing, a named winner for a kind of decision. No source says so, so that reading
           is at medium-low confidence. This template asks the author to name, for a kind of decision, which
           principle wins. A resolution can take several forms. Salesforce "stack-ranked" its four
           principles. Keith recommends the form "X, even over Y." Atlassian, as the principles.design
           mirror records it, writes each principle as one thing before another, as in "Trusted
           fundamentals before comprehensive patterns". As this research read them, GOV.UK, the NHS and
           USWDS state no priority order, though the NHS list is numbered. Ranking is welcome and not required. A resolution scoped
           to a kind of decision survives longer than a global order, and that reading is the library's.
           Deep dive: design-principles_companion.md section 3 (Anatomy > When Principles Conflict) and
           section 6 (Debates and contested boundaries).
     ASK   Which two principles are most likely to collide? In which kind of decision do they collide?
           Which one wins there, and why? Is the answer different in another kind of decision?
     PRIORITY  Resolve the most likely collision first, and do not rank every pair. One resolved conflict
           in a named kind of decision is worth more than a complete table nobody applies. That is this
           library's advice, not a sourced rule.
     ROW HINT  A good row names the two principles, names the kind of decision, says which principle wins
           there and gives the reason. A weak row says both matter equally.
     GOOD  | Show the next departure first, against Explain every delay in full | Layout of the home
           screen and notification text | Show the next departure first | A rider at a stop needs the
           time before the cause, so the explanation moves one tap away. |
     WEAK  | All of them | Everything | Use judgement | They are all important. | (no pair, no kind of
           decision, no winner)
     TRAP  Saying that all principles are equally important, or ranking every pair so the table becomes a
           document nobody applies. A set that never says which one wins leaves the argument to whoever
           is in the room. -->

| Principles in tension | Kind of decision | Which wins | Why |
|---|---|---|---|
| {{conflict_principles}} | {{conflict_decision_kind}} | {{conflict_winner}} | {{conflict_reason}} |

## Using Them in Decisions

<!-- WHAT  Where the set is applied, such as design critique, design review and proposals for a new
           pattern, how a decision cites a principle, and what a reviewer may do when a decision sets one
           aside.
     WHY   The sources say what a set is for before they say how to apply it. The NHS says "Use them to
           get started on a project and to help with making decisions." NN/g advises teams to "use the
           principles to explain and justify design decisions". GitLab's critique sessions tell designers
           to "Connect feedback to user needs and business goals instead of personal preference" and to
           "Review the complete design principles in Pajamas". Salesforce used its ranked principles in
           design review, and the practice spread to marketing and product management. Brignell names
           principles nobody refers to as a failure mode. This library infers that a set with no stated
           place where it is cited risks being read once and not applied, and no source read ties the
           failure to that cause. Productboard's AI prompt, a vendor's prompt and not a published set,
           names moments of use, among them design reviews and disagreements between designers, and
           offers the line "Our principles say [X] over [Y] in this case." The written line a decision
           record carries, and what a reviewer may do when a principle is set aside, are this library's
           additions. The last field rests on a reading.
           USWDS calls its set "an evaluative lens for design and implementation decisions" and GitLab
           says "Principles act as a reusable standard for teams to measure their work." The family reads
           judged against as judgement: a decision cites the principle it leaned on and the one it set
           aside, and a reviewer may accept the reasoning without accepting the outcome.
           Deep dive: design-principles_companion.md section 3 (Anatomy > Using Them in Decisions).
     ASK   In which two or three moments is a principle cited? How is the citation written down? When a
           decision sets a principle aside, what does the reviewer do?
     GOOD  "Applied in the fortnightly design critique, in design review before any screen ships, and when
           someone proposes a new component. A decision record carries one line naming the principle it
           leaned on and the one it set aside, with the reason. A reviewer may accept the reasoning
           without accepting the outcome, and says which."
     WEAK  "Designers should keep the principles in mind." (names no moment, no form of citation and no
           way to tell a decision that used them from one that did not)
     TRAP  A set that is read at adoption and never cited again, or a citation so mechanical that it
           becomes a checkbox. This library reads a standard judged against as judgement, not compliance. -->

**Where the set is applied:** {{where_applied}}

**How a decision cites a principle:** {{how_decisions_cite}}

**When a decision sets a principle aside:** {{when_set_aside}}

## Ownership and Changes

<!-- WHAT  The named owner, how anyone proposes a change, who decides, and a dated change log.
     WHY   This is where the set's own staleness is handled. GOV.UK credits a body, the Government
           Digital Service and the Central Digital and Data Office. Pajamas says "Everyone is welcome to
           suggest improvements by opening an issue", and the NHS offers "Feed back or share insights on
           GitHub". GitLab's handbook names designers as "the DRIs for design decisions", but names no
           owner or revision trigger for the principles themselves. No source read names a role that
           decides a change to a set, so the role names this template asks for are the library's
           position. The dated record is sourced in practice, not in method. GOV.UK's update history has
           three entries in thirteen years, from 3 April 2012 to 2 April 2025, and the NHS page carries
           "Updated: April 2023". The 2025 addition followed a cross-government working group: its
           authors wrote "We facilitated 2 workshops", and afterwards "we're now looking for someone to
           create an 11th poster, and to update the other 10", so a change had a cost beyond the sentence.
           Sets are replaced as well as amended. Spotify replaced a 2013 set of six with a set of three
           after an audit, and Spool writes that "old principles will need to go into storage". So record
           a retirement as a change and keep the reason. No source read states a revision interval, and
           sets appear to change rarely and on an event. That is at low to medium confidence, since three
           dated entries on one page are a thin base.
           Deep dive: design-principles_companion.md section 3 (Anatomy > Ownership and Changes).
     ASK   Who owns this set, by role and by name? Where does anyone propose a change? Who decides? When
           was the set first agreed, and what has changed since, including anything retired?
     PRIORITY  Start the log with the date the set was first agreed, so the first row is never blank.
     ROW HINT  A good row has a date, says what changed in a sentence a stranger could follow, and names
           what fired it: a Review Trigger row, or "first agreed". A weak row is a date and the word
           "updated".
     GOOD  | 2025-03-18 | Principle 4 retired and moved to the archive: an audit found it overlapped
           principle 2, and nobody could recall it unprompted | Review Trigger: an audit finds principles
           overlapping or forgotten | Design lead |
     WEAK  | 2025-03-18 | Updated | | |
     TRAP  A set with no owner and no condition that reopens it, which has no way to change on purpose. A
           change log that shows only additions hides replacement. -->

**Owner (role and person):** {{owner_role_and_person}}

**How anyone proposes a change:** {{how_to_propose}}

**Who decides a change:** {{who_decides}}

| Date | What changed | What fired it | Who decided |
|---|---|---|---|
| {{change_date}} | {{change_summary}} | {{change_trigger}} | {{change_decider}} |

## Review Trigger

<!-- WHAT  A table of conditions, owners and actions: what event makes this set wrong or incomplete, who
           notices, and what they do about it. The conditions are things an owner can observe, not dates.
     WHY   The standing-standards family requires every member to carry this mechanism, because members
           fail by going quietly out of date. No design principles source names a trigger, so the table
           form is this library's position, and each condition below is sourced where a source exists.
           A new cross-cutting concern with people behind it: GOV.UK added a principle in 2025 after a
           cross-government working group formed around the topic. An audit finds principles
           overlapping or forgotten: Spotify's audit named "Overlapping concepts" as a defect, and NN/g
           warns that "having 10 or more leads to many being forgotten". A new product or surface joins
           the scope: Spool's test asks "Have You Evaluated it for This Project?" A debate recurs and no
           principle settles it: the library's own position, with Mistry's stated goal to end repeated
           debates, not all debate. The audience or the strategy changes: the library's own inference,
           which no source read states. No calendar interval is sourced, so none is required. A team may
           add one as a floor if it wants one, and should label it as its own choice.
           Deep dive: design-principles_companion.md section 3 (Anatomy > Review Trigger).
     ASK   What could the owner observe that shows this set is wrong? Who notices each condition, by
           role? What do they do about it: reopen the set, run a short audit, or write the change into
           the log?
     PRIORITY  List the conditions an owner is most likely to see first, and write each as an event
           someone can observe, not as a date.
     ROW HINT  A good row states a condition the owner could observe, names a role as owner, and states an
           action, such as reopening the set or writing a dated line in the change log. A weak row says
           "review regularly" and names no one.
     GOOD  | An audit finds two principles overlapping, or one nobody can recall | Design lead | Merge or
           retire one, write the reason into the change log and move a retired principle to an archive
           section, not out of the document. |
     WEAK  | Review regularly | The team | Update the principles. |
     TRAP  Writing a date as the only trigger, or naming one condition and treating it as the whole
           mechanism. The strongest rows are the ones that have already fired once, so tie a row to a
           line in the change log when it does. -->

| Condition | Owner | What They Do About It |
|---|---|---|
| A new cross-cutting concern with people behind it | {{concern_owner}} | {{concern_action}} |
| An audit finds principles overlapping or forgotten | {{audit_owner}} | {{audit_action}} |
| A new product or surface joins the scope | {{new_scope_owner}} | {{new_scope_action}} |
| A debate recurs and no principle settles it | {{recurring_debate_owner}} | {{recurring_debate_action}} |
| The audience or the strategy changes | {{audience_change_owner}} | {{audience_change_action}} |
