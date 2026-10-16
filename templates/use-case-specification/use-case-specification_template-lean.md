---
title: "{{use_case_title}}"
use_case_id: "{{use_case_id}}"
primary_actor: "{{primary_actor}}"
status: "{{status}}"
doc_type: use-case-specification
size: lean
source_template: use-case-specification
source_template_version: 0.1.0
---

<!--
CASUAL USE CASE SPECIFICATION. The five sections every fully dressed use case shares: the use case's title
and actor, its goal in context, what must be true before it starts and what starts it, the main success
scenario, and what stays true however it ends. This is this library's own nearest equivalent of Cockburn's
casual form: it drops the project annotation and the separate Extensions section casual prose drops too,
while keeping numbered steps where Cockburn's own casual form writes free prose paragraphs. See
use-case-specification_companion.md section 4 (Variants and sizing).

To grow this into the fully dressed form (see use-case-specification_template-full.md), ADD Scope and
Level, Stakeholders and Interests, Extensions, Related Information, and Open Issues and Schedule; never
rename or reorder the five sections below, because the full variant is a strict superset of this one.
Cockburn's own writing order grows a use case the same way, from lower precision to higher: "Precision
Level 1: Primary actor's name and goal Precision Level 2: The use case brief, or the main success scenario
Precision Level 3: The extension conditions Precision Level 4: The extension handling steps."

WHAT A USE CASE SPECIFICATION IS. Alistair Cockburn's own definition states the job directly: "A use case
captures a contract between the stakeholders of a system about its behavior." It writes down, for one
primary actor and one goal, a numbered main scenario plus the deviations that branch off it when something
goes another way. See use-case-specification_companion.md section 1.

ITS VALUE SITS IN THE BRANCHES, NOT THE HAPPY PATH. Cockburn again: "The greatest value of the use case
does not lie in the main scenario, but in alternative behaviors." Even at this size, do not skip the known
deviation lines inside the Main Success Scenario section below. See use-case-specification_companion.md
section 1 and section 6, item 1.

IT IS NOT A TEST PLAN. Cockburn states the limit directly: "Use cases are not test plans or test cases.
They are missing the data values needed for test cases." A use case states what the system must do; a test
case checks that it did. See use-case-specification_companion.md section 8.

IT DESCRIBES BEHAVIOR, NOT DESIGN. Cockburn's own distinction: "a black-box use case does not discuss the
internal structure of the system under discussion, while a white-box use case does." This bundle templates
the black-box reading; write what the actor and the system do, never how the system is built to do it. See
use-case-specification_companion.md section 6, item 11.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP.
2. Replace each {{placeholder}}. Name the actor's goal in the title, write the Main Success Scenario at the
   level of the actor's intention, never the user interface, and give each known
   deviation one line of prose rather than inventing a separate Extensions section.
3. If a section does not apply to this use case, write "N/A" and one line of why, rather than deleting it.
4. Before you share it: self-grade against use-case-specification_guide.md, then DELETE every HTML
   comment. They are guidance, not content.
-->

# {{use_case_title}}

## Title and Actor

<!-- WHAT  The use case's name, stated as a short active verb phrase naming the goal, a unique identifier,
           and the primary actor whose goal this use case serves.
     WHY   Cockburn's own 1998 template opens every use case with "Use Case: <number> <the name
           should be the goal as a short active verb phrase>", and the same header block names "Primary
           Actor: <a role name for the primary actor, or description>" a few fields further down. Three further sources independently ask for a unique
           identifier beyond a bare number: Wiegers' "Give each use case a unique numeric identifier, in
           hierarchical form: X.Y.", NYU's "Use Case ID: {This should be coded to identify the owning team
           and the level of the use case}", and Notre Dame's "Each use case should have a unique identifier
           that can be used for quick reference and traceability." Deep dive:
           use-case-specification_companion.md section 3 (Title and Actor).
     ASK   What is the actor's goal, stated as a short active verb phrase? What identifier does this use
           case carry, so it can be found again? Who is the primary actor: a role name, or a short
           description if no settled role name exists?
     GOOD  "Title: Reset a forgotten password. ID: UC-07. Primary Actor: Account Holder, an actor who has
           lost access to their own account and wants back in without contacting support."
     WEAK  "Title: Account Settings. ID: (none). Primary Actor: user." (not a goal phrase, no identifier,
           and "user" is a role so generic the use case could be about almost anything)
     TRAP  Naming the use case after a feature or a screen instead of the actor's goal. "Account Settings"
           is a part of the system; "Reset a forgotten password" is what the actor is trying to
           accomplish, and the latter is what Cockburn's own field asks for. -->

**Use Case ID:** {{use_case_id}}

**Primary Actor:** {{primary_actor}} - {{primary_actor_description}}

## Goal in Context

<!-- WHAT  A longer statement of the actor's goal than the title line gives, including the circumstances
           under which the goal normally arises.
     WHY   Cockburn's 1998 template carries this field under the same name used here: "Goal in Context: <a
           longer statement of the goal, if needed>". His later draft renames it "Context of use" and adds
           a question this ASK keeps: "<a longer statement of the goal, if needed, its normal occurrence
           conditions>". This is the field the family's own "elaborates" verb is organized around: the goal
           that every other section serves. Deep dive: use-case-specification_companion.md section 3 (Goal
           in Context).
     ASK   What is the actor trying to accomplish, in a sentence or two beyond the title? Under what
           circumstances does this goal typically arise: a regular habit, a one-time event, a response to
           something else happening?
     GOOD  "An account holder who has forgotten their password can no longer sign in to any of their own
           accounts. They want to regain access on their own, without calling support or waiting for a
           human to intervene."
     WEAK  "The actor wants to use the reset feature." (restates the title without adding the
           circumstance that brings the actor to this goal)
     TRAP  Writing a one-line paraphrase of the title instead of the longer statement the field asks for.
           If this section adds nothing the title did not already say, the field has not done its job. -->

{{goal_in_context}}

## Preconditions and Trigger

<!-- WHAT  What must already be true of the world before this use case can start, and the event that
           actually starts it.
     WHY   Cockburn's 1998 template: "Preconditions: <what we expect is already the state of the world>"
           and "Trigger: <the action upon the system that starts the use case, may be time event>". Wiegers
           asks the same thing in different words: "List any activities that must take place, or any
           conditions that must be true, before the use case can be started." RUP defines the term
           directly: "A precondition of a use case is the state of the system that must be present prior to
           a use case being performed." Deep dive: use-case-specification_companion.md section 3
           (Preconditions and Trigger).
     ASK   What must already be true before this use case can begin? What single event starts it: an
           action the actor takes, or a time event the system itself raises?
     GOOD  "Preconditions: the account already exists and has a verified email address on file. Trigger:
           the account holder indicates, from the sign-in screen, that they cannot sign in with their
           current password."
     WEAK  "Preconditions: none. Trigger: the user does something." (a use case with genuinely no
           preconditions is rare, and "does something" names no event)
     TRAP  Writing a step of the scenario itself as a precondition. A precondition is a fact about the
           world before the use case starts, not an action the actor takes once it has; the 1998 field's
           own wording distinguishes "what we expect is already the state of the world" from the trigger
           that starts the clock. A trigger can also be a time event rather than an action; do not assume
           every use case starts with someone clicking something. -->

**Preconditions:** {{preconditions}}

**Trigger:** {{trigger}}

## Main Success Scenario

<!-- WHAT  The numbered sequence of steps, from trigger to goal delivery, that plays out when nothing goes
           wrong, plus one line of prose for each known deviation.
     WHY   Cockburn's 1998 template's own placeholder reads "<put here the steps of the scenario from
           trigger to goal delivery, and any cleanup after>", and RUP names the same section "2.1 Basic
           Flow". Cockburn's own writing rule asks for "one column of text (not a table)" and no branching
           inside it: a step that branches belongs in Extensions in the full template. This library's own
           lean variant has no separate Extensions section; it asks for each known deviation in one
           line of prose here instead, because the casual form Cockburn describes is "likely to be
           less rigorous in its description than a fully dressed use case" while its value still sits in
           its deviations, per Cockburn's own account: "The greatest value of the use case does not lie in
           the main scenario, but in alternative behaviors." Deep dive:
           use-case-specification_companion.md section 3 (Main Success Scenario) and section 4 (Variants
           and sizing).
     ASK   What is the shortest sequence of steps that gets the actor from the trigger to the goal, with
           nothing going wrong? For each step, does it show a goal succeeding rather than a screen
           rendering? Does the actor and the system alternate, each step a response to the one before it?
           In which ways can this scenario go another way, and how does the system handle each one, in a
           line of prose apiece?
     GOOD  "1. The account holder indicates they cannot sign in with their current password. 2. The account
           holder confirms which account this is, by email address. 3. The system sends a time-limited
           link to that address that lets the account holder set a new password. 4. The account holder
           follows the link and sets a new password. Known deviations: if the email address does not
           match any account, the system shows the same generic message rather than revealing whether an
           account exists. If the link has expired when it is followed, the system offers to send a new one."
     WEAK  "1. User clicks "Forgot password?". 2. A form appears. 3. User clicks Submit." with no deviation
           lines at all (names screen elements, not the actor's intention, and skips the branch this
           library's own research found to be where a use case's real value sits)
     TRAP  Naming a user-interface element instead of the actor's intention. Cockburn's own step-writing
           rule: "Highlight the actor's intention, not the user interface details." Keep each step to one
           activity, stop between three and nine steps, and do not let a deviation line become a second
           full scenario; if a deviation genuinely needs its own numbered handling steps, that is the
           signal to grow this use case into the full variant instead of stacking lines here. -->

1. {{step_1}}
2. {{step_2}}
3. {{step_3}}

**Known deviations:**

- {{known_deviation}}

## Minimal and Success Guarantees

<!-- WHAT  What stays true no matter how the use case ends, paired with what is additionally true only when
           it ends successfully.
     WHY   Cockburn's 1998 template carried a single "Failed End Condition: <the state of the world if goal
           abandoned>", a property of the failure exit alone. His later draft replaces it with two paired
           fields, and this is a change of meaning, not just a rename: "Minimal Guarantees: <how the
           interests are protected under all exits>" beside "Success Guarantees: <the state of the world if
           goal succeeds>". OpenUP's checklist states the distinction as two separate, checkable
           properties: "(A Minimal Guarantee represents a condition that will be true when the use case
           ends, regardless of how it terminates.)" against "(A Success Guarantee represents a condition
           that will be true when the use case ends successfully, regardless of which path it takes.)"
           Deep dive: use-case-specification_companion.md section 3 (Minimal and Success Guarantees).
     ASK   What must stay true however this use case ends, success or failure alike? What is additionally
           true only when it ends successfully?
     GOOD  "Minimal Guarantees: the account holder's current password keeps working until a new one is
           confirmed, so an abandoned or failed reset never locks them out. Success Guarantees: the
           account has a new password, and every other active session for that account is signed out."
     WEAK  "Minimal Guarantees: the system doesn't crash. Success Guarantees: it worked." (neither is a
           checkable condition of the world)
     TRAP  Writing only a success condition and treating "it didn't fail" as the minimal guarantee. A
           minimal guarantee is a positive statement about what is protected on every exit, including a
           failed one, not an absence of failure. -->

**Minimal Guarantees:** {{minimal_guarantees}}

**Success Guarantees:** {{success_guarantees}}
