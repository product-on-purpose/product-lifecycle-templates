---
title: "{{problem_name}} Problem Statement"
problem_name: "{{problem_name}}"
author: "{{author}}"
decider: "{{decider}}"
status: "{{status}}"
last_updated: "{{date}}"
doc_type: problem-statement
size: lean
source_template: problem-statement
source_template_version: 0.1.1
---

<!--
LEAN PROBLEM STATEMENT. The shortest form that still names which problem is worth solving, who has
it, and what evidence shows it is real, before anyone names a solution. Use it to decide whether a
problem is worth taking to a project brief or a business case at all, not to make that case itself.
To grow it into a form that also carries success measures, a boundary on what the problem excludes,
and open questions, see problem-statement_template-full.md. ADD sections between Evidence and
Decision This Informs; never rename or reorder the ones below, because the full variant is a strict
ordered superset of this one.

SHORT AT BOTH SIZES, NOT ONLY THIS ONE. Nielsen Norman Group's own brevity rule reads, "If you can
condense your problem statement down to a few sentences, others will quickly understand what you
focus on and why, and what's out of scope," and NHS Wales puts a typical instance at "about 18 words
long." The full variant adds four named fields around the statement; it does not add length to the
statement itself. See problem-statement_companion.md section 4.

WHAT A PROBLEM STATEMENT IS, AND IS NOT
It names which problem is worth solving, who has it, and what evidence shows it is real, before
anyone names a solution, an option, a project, or an investment. It is NOT a business case (this
library's own `business-case` bundle asks the same questions inside a funded investment comparison;
this document comes earlier, asks for no money, and decides whether a problem is worth that
comparison at all; one Six Sigma source draws the same line by name, and the order, statement first,
is this library's own POSITION). It is NOT a project brief (which asks a named approver
for authority to start initiation; this document asks for no authority and names no project; an
Association for Project Management consultation draft read for this library's `project-brief`
research names the three documents as interchangeable for one early rationale, but APM's own
published glossary carries no "problem statement" entry and defines "Brief" and "Charter" as two
different things). It is NOT a PRD (this library's own `prd` companion already names a problem
statement as one of the things that precede a PRD). It is NOT a hypothesis statement, a How Might We
question, or a job story (each of those already points at a solution or tests one). It is NOT, in
this library, an opportunity statement: that is a separate catalog type, not yet built, though
Nielsen Norman Group names the two "written and used in the same way." A design-thinking Point of
View statement is listed as an alias of this document.
See problem-statement_companion.md section 6 and section 8.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT it wants, WHY it matters (with a pointer into
   problem-statement_companion.md), guiding questions to ASK, a GOOD and a WEAK example, and the
   TRAP to avoid. For the table, PRIORITY explains the ordering rule and ROW HINT says what a good
   row contains.
2. Replace each {{placeholder}} with your content. Name no solution, option, project, or investment
   anywhere in this document; that is a later document's job.
3. If a section does not apply, write "N/A" and one line of why, rather than deleting it.
4. Before you send this for a decision: self-grade against problem-statement_guide.md, then DELETE
   every HTML comment. They are guidance, not content.
-->

# {{problem_name}} Problem Statement

## Problem Statement

<!-- WHAT  The statement itself: a few sentences, from the affected person's perspective, naming no
           solution.
     WHY   Nielsen Norman Group's own definition anchors this section, "A concise description of the
           problem that needs to be solved," and NHS Wales adds the brevity bar, "about 18 words
           long." Atlassian's own Problem Framing play names the same four elements this section
           asks for, "who is affected, what is affecting them, why it needs to be solved, and where
           the problem is happening." Deep dive: problem-statement_companion.md section 3
           (Anatomy > Problem Statement).
     ASK   Who has this problem? What is happening to them? Why does it need to be solved? Where and
           when does it occur?
     GOOD  "Patrons who borrow ebooks through the library's mobile app cannot renew a loan from
           within the app, and must call the branch during open hours to ask staff to renew it for
           them."
     WEAK  "We need to add a renew button to the ebook app." (a solution stated as if it were the
           problem; nothing is left to investigate)
     TRAP  Naming a solution instead of a problem. Nielsen Norman Group's own quality rule reads,
           "Leave solutions out of your problem statement. At the beginning of discovery, there are
           too many unknowns, so the best solution is not obvious." -->

{{problem_statement}}

## Background

<!-- WHAT  Where the problem shows up, how it came to attention, and what is affecting the people
           who have it.
     WHY   Nielsen Norman Group names the question directly, "Which organization or department has
           the problem and what is the problem? Why has the problem arisen?" and Atlassian's own
           prompts ask, "What is the nature of the problem? What signs point to there being a
           problem?" Deep dive: problem-statement_companion.md section 3 (Anatomy > Background).
     ASK   Which team, product, or service has this problem? How did it come to attention? Why has
           it arisen now rather than earlier?
     GOOD  "Flagged by three branch managers in the October staffing review, after phone-renewal
           requests started crowding out other reference calls during the two weekday hours the
           branches are fully staffed."
     WEAK  "The app has some issues." (no organization named, no origin, no reason it surfaced now)
     TRAP  Restating the Evidence section's data as narrative instead of explaining where the
           problem shows up and how it was noticed. -->

{{background}}

## Who Is Affected

<!-- WHAT  The people who have the problem, named specifically enough to find them.
     WHY   Nielsen Norman Group's own wording leaves room for more than one group, "There could be
           multiple user groups affected by a specific problem in different ways," and Atlassian
           asks the verification question directly, "Who is experiencing this problem? How do we
           know that they are experiencing it?" NHS Scotland's Problem Framer tool carries a closely
           related field, "Who The Problem Most Affects." Deep dive: problem-statement_companion.md
           section 3 (Anatomy > Who Is Affected).
     ASK   Who specifically has this problem? Is there more than one affected group, and does each
           experience it differently? How do you know they are experiencing it, rather than assuming
           it? Does an existing persona already describe this group?
     GOOD  "Patrons who borrow ebooks through the app, especially those who use it in the evening or
           on weekends when no branch phone line is staffed."
     WEAK  "Our users." (no group named specifically enough to find them)
     TRAP  Folding more than one differently affected group into one generic line. Nielsen Norman
           Group treats more than one group as the normal case, not the exception. -->

- Who is affected: {{who_is_affected}}
- Existing persona, if one already describes this group: {{persona_reference}}

## Impact and Why Now

<!-- WHAT  What the problem costs the people who have it and the organization, and why it matters
           now rather than later.
     WHY   Nielsen Norman Group's own prompt runs, "If the problem is not fixed, what will be the
           effect on the organization?" and Atlassian asks it from the affected person's side, "What
           happens if we don't solve it?" GOV.UK adds the instruction to size the impact where
           possible, "You should also consider quantifying the value of solving the problem."
           Keep any figure directional: a Six Sigma source draws the line this section stops short
           of, "the problem statement describes what, where, and how much, without the persuasive
           framing," while a specific dollar estimate belongs to a business case. Deep dive:
           problem-statement_companion.md section 3 (Anatomy > Impact and Why Now).
     ASK   What does this problem cost the affected people, and the organization? Why does it matter
           now rather than later? What changes if nothing is done? What is a rough, directional
           figure for the cost of not solving it, not a costed estimate?
     GOOD  "Branch phone lines run near capacity during the two staffed hours, and the October
           survey named the call-in renewal step the top app complaint. Ebook loans are a growing
           share of total borrowing, so the volume of calls this causes is rising each quarter."
     WEAK  "This is frustrating for everyone." (no organizational effect, no timing reason, no
           figure at all, directional or otherwise)
     TRAP  Writing a full costed estimate with its own methodology. That is a business case's job,
           not this one's; a rough, directional figure is enough here. -->

- Impact: {{impact}}
- Why now: {{why_now}}

## Evidence

<!-- WHAT  What shows the problem is real, where each piece came from, and how strong it is.
     WHY   Digital NSW states the obligation plainly, "Use the evidence you gather to document your
           clearly defined problem," and NHS Wales states the cost of skipping it, "without evidence
           of your problem, you are left with opinion." Name the extent of the problem, not only
           its existence: a Six Sigma source adds the magnitude question, "it is essential to
           explain the extent or magnitude of the issue." Deep dive: problem-statement_companion.md
           section 3 (Anatomy > Evidence).
     ASK   What evidence shows this problem is real? Where did each piece come from? How strong is
           it, a direct measurement, a survey, or an anecdote? How large or widespread is the
           problem, not only that it exists?
     PRIORITY  List the strongest, most direct evidence first. A statement resting only on the
           weakest row is a statement resting on opinion.
     ROW HINT  A good row names where the evidence came from and what it shows, specifically enough
           that a reader could go check it. A weak row asserts a fact with no named source.
     GOOD  | Branch call logs, Sept-Oct | Renewal-assistance calls are the largest single call
           category during staffed hours | Direct measurement |
     WEAK  | Staff say it's a problem | | Anecdote |
     TRAP  Opinion standing in for evidence. NHS Wales's own warning is blunt: without evidence, a
           problem statement is left with opinion, not a documented fact. -->

| Evidence | What it shows | Strength |
|---|---|---|
| {{evidence_source}} | {{evidence_summary}} | {{evidence_strength}} |

## Decision This Informs

<!-- WHAT  Who decides whether this problem is worth pursuing further, by when, and which document
           takes over if the answer is yes.
     WHY   GOV.UK frames the decision itself, "Your discovery is finished when you've decided
           whether or not you want to move on to alpha," adding, "It's not a failure to stop at
           the end of the discovery phase," and Digital NSW's own checklist ends on the same
           question, "Is the problem clear enough to investigate further?" Which document takes over
           is this library's own POSITION, from the `discovery-docs` family contract's successor
           obligation: name the specific document, a project brief, a business case, or both in
           sequence, rather than leaving the pointer generic. Deep dive:
           problem-statement_companion.md section 3 (Anatomy > Decision This Informs).
     ASK   Who decides whether this problem is worth pursuing further? By when do they need to
           decide? Which specific document takes over if the answer is yes, a project brief, a
           business case, or both in sequence?
     GOOD  "Decider: the digital services manager, by the end of the month. If the problem is
           confirmed worth pursuing, a project brief is written next to ask for authority to
           investigate options."
     WEAK  "We'll figure out next steps later." (no decider, no date, no named next document)
     TRAP  Leaving the next document generic, or naming an option or a project instead of a
           decision. This section names who decides and what happens to the answer, nothing
           more. -->

- Decider: {{decider}}
- Decide by: {{decision_deadline}}
- Next document if pursued: {{next_document}}
