---
title: "{{use_case_title}}"
use_case_id: "{{use_case_id}}"
primary_actor: "{{primary_actor}}"
status: "{{status}}"
doc_type: use-case-specification
size: full
source_template: use-case-specification
source_template_version: 0.1.0
---

<!--
FULLY DRESSED USE CASE SPECIFICATION. Ten sections, in a fixed order: the use case's title and actor, its
goal in context, its scope and level, its stakeholders and interests, what must be true before it starts
and what starts it, the main success scenario, the extensions that branch off it, what stays true however
it ends, the project annotation a fully dressed use case carries beyond its header, and its open issues and
schedule. Use this variant for a use case formal or critical enough that a reviewer needs the full header,
the stakeholder list, and every extension numbered and findable on its own. See
use-case-specification_companion.md section 4 (Variants and sizing).

This is a STRICT SUPERSET of use-case-specification_template-lean.md: the lean variant's five sections
carry the same name and the same order as five of these ten. If you are growing a lean use case into this
one, ADD Scope and Level, Stakeholders and Interests, Extensions, Related Information, and Open Issues and
Schedule at the points this file places them; do not reorder the five sections the two variants share.

WHAT A USE CASE SPECIFICATION IS. Alistair Cockburn's own definition states the job directly: "A use case
captures a contract between the stakeholders of a system about its behavior." It writes down, for one
primary actor and one goal, a numbered main scenario plus the lettered extensions that branch off it when
something goes another way. See use-case-specification_companion.md section 1.

ITS VALUE SITS IN THE BRANCHES, NOT THE HAPPY PATH. Cockburn again: "The greatest value of the use case
does not lie in the main scenario, but in alternative behaviors." Spend more care on Extensions than on the
Main Success Scenario; the scenario is usually the easier half to write. See
use-case-specification_companion.md section 1 and section 6, item 1.

IT IS NOT A TEST PLAN. Cockburn states the limit directly: "Use cases are not test plans or test cases.
They are missing the data values needed for test cases." A use case states what the system must do; a test
case checks that it did. See use-case-specification_companion.md section 8.

IT DESCRIBES BEHAVIOR, NOT DESIGN. Cockburn's own distinction: "a black-box use case does not discuss the
internal structure of the system under discussion, while a white-box use case does." This bundle templates
the black-box reading; write what the actor and the system do, never how the system is built to do it. See
use-case-specification_companion.md section 6, item 11.

HOW TO FILL THIS IN
1. Read the comment under each heading: WHAT, WHY (with a companion pointer), ASK, GOOD, WEAK, TRAP; a
   section that records more than one entry adds PRIORITY and ROW HINT.
2. Replace each {{placeholder}}. Name the actor's goal in the title, and write the Main Success Scenario at
   the level of the actor's intention, never the user interface.
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

## Scope and Level

<!-- WHAT  The system under design, stated as a black box, and how large a unit of work this use case
           covers relative to the actor's own goals.
     WHY   Cockburn's own draft prints both fields together: "Scope: <design scope, what system is being
           considered black-box under design>" and "Level: <one of: Summary, User-goal, Subfunction>". The
           draft also names the design-scope axis directly: "A business use case has the enterprise as its
           design scope." against "A system use case has a computer system as its design scope." Deep
           dive: use-case-specification_companion.md section 3 (Scope and Level) and section 6, item 4.
     ASK   What system is this use case about, stated as a black box (what it does, not how it is built)?
           Is this a user-goal use case (one person, one sitting, roughly two to twenty minutes), a summary
           use case that bundles several user goals, or a subfunction use case that exists only because a
           user-goal use case needs it?
     GOOD  "Scope: the account system's sign-in and credential-recovery functions, considered as a black
           box. Level: user-goal (one person, one sitting)."
     WEAK  "Scope: the system. Level: medium." (names no actual boundary, and "medium" is not one of the
           three stated levels)
     TRAP  Describing the system's internals instead of its boundary. Cockburn's own rule: "Recall, in the
           following, that a black-box use case does not discuss the internal structure of the system under
           discussion, while a white-box use case does." This bundle templates the black-box reading only;
           see the preamble above. -->

**Scope:** {{scope}}

**Level:** {{level}}

## Stakeholders and Interests

<!-- WHAT  Everyone with a vested interest in how this use case behaves, including anyone who never
           interacts with the system directly, and what each of them wants from it.
     WHY   This section rests on Cockburn's own later work alone, at medium confidence: his 1998 template
           never mentions a stakeholder, but his draft carries "Stakeholders & Interests: <list of
           stakeholders and key interests in the use case>", and a stakeholder is, in the draft's own
           words, "someone with a vested interest in the behavior of the use case, even if they never
           interact directly with the system." His own writing process makes the rest of the document
           answer to this list: "7. Capture stakeholders and interests, preconditions and guarantees. The
           system will ensure the preconditions and guarantee the interests." Deep dive:
           use-case-specification_companion.md section 3 (Stakeholders and Interests).
     ASK   Who has a stake in how this use case behaves, beyond the primary actor? What does each one want
           from it? List a stakeholder even if they never touch the system themselves.
     PRIORITY  List every stakeholder whose interest could change how a step or a guarantee is written,
           even one who never interacts with the system; an omitted stakeholder's interest has no way to
           reach the Main Success Scenario or the Minimal Guarantees later.
     ROW HINT  A good row names a stakeholder and a specific, checkable interest. A weak row names a role
           with no stated interest, or an interest so broad it could belong to any use case.
     GOOD  | Support Team | Wants the volume of password-reset calls to go down, not up |
     WEAK  | Management | Cares about the product |
     TRAP  Listing only the primary actor here. The primary actor already has their own field above; this
           section exists for everyone else with a stake, the people a step or a guarantee could affect
           without ever appearing in the Main Success Scenario. -->

| Stakeholder | Interest |
|---|---|
| {{stakeholder}} | {{stakeholder_interest}} |

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
           wrong.
     WHY   Cockburn's 1998 template's own placeholder reads "<put here the steps of the scenario from
           trigger to goal delivery, and any cleanup after>", and RUP names the same section "2.1 Basic
           Flow". Cockburn's own writing rule asks for "one column of text (not a table)" and no branching
           inside it: steps that branch belong in Extensions. Deep dive:
           use-case-specification_companion.md section 3 (Main Success Scenario).
     ASK   What is the shortest sequence of steps that gets the actor from the trigger to the goal, with
           nothing going wrong? For each step, does it show a goal succeeding rather than a screen
           rendering? Does the actor and the system alternate, each step a response to the one before it?
     GOOD  "1. The account holder indicates they cannot sign in with their current password. 2. The account
           holder confirms which account this is, by email address. 3. The system sends a time-limited
           link to that address that lets the account holder set a new password. 4. The account holder
           follows the link and sets a new password."
     WEAK  "1. User clicks "Forgot password?". 2. A form appears. 3. User clicks Submit." (names screen
           elements, not the actor's intention; a redesigned form breaks every step)
     TRAP  Naming a user-interface element instead of the actor's intention. Cockburn's own step-writing
           rule: "Highlight the actor's intention, not the user interface details." Keep each step to one
           activity, written in the active voice, and stop between three and nine steps; Cockburn's own
           account is that he is "yet to write a main success scenario longer than nine steps." A step that
           needs an "if" belongs in Extensions below, not here. -->

1. {{step_1}}
2. {{step_2}}
3. {{step_3}}

## Extensions

<!-- WHAT  The branches off the main success scenario, each naming the condition that triggers it, how the
           system handles it, and where it ends up: back in the main scenario, a separate success, or a
           failure.
     WHY   Cockburn's 1998 template's own placeholder for a branch is "<step altered> <condition> : <action
           or sub.use case>", and his draft gives the numbering convention this section follows: "the
           numbering convention in the extensions sections involving combinations of digits and letters
           (e.g., 2a, 2a1, 2a2 and so on)". RUP's own "2.2 Alternative Flows" and the jointly authored
           foundation's framing, "A list of all the special cases, alternative paths, optional steps, and
           errors that need to be handled," both keep alternative and exception paths in one section rather
           than splitting them, which is the reading this bundle follows. Deep dive:
           use-case-specification_companion.md section 3 (Extensions) and section 6, item 8.
     ASK   What can go another way at each step, that the system itself can detect? For each one: what
           handles it, and does it rejoin the main scenario, end in a separate success, or end in failure?
           Did you brainstorm exhaustively before writing the handling steps, per Cockburn's own order:
           "9. Brainstorm and exhaustively list the extension conditions. Include all that the system can
           detect and must handle." then "10. Write the extension-handling steps."
     PRIORITY  Spend more effort here than on the Main Success Scenario above; per the preamble, the
           greatest value of a use case lies in its alternative behaviors, not its happy path.
     ROW HINT  A good row names the branch point and letter (3a), states a condition the system can
           actually detect, and names where the branch ends up. A weak row has a vague condition such as
           "error occurs" with no stated outcome.
     GOOD  | 2a | The email address does not match any account | Show the same generic "a link has been
           sent if this matches an account" message | Ends without revealing whether the account exists |
     WEAK  | 3a | Something goes wrong | Handle it | (unknown) |
     TRAP  Describing an error without saying what the system does about it. Sehlhorst names this directly:
           "Unanticipated error conditions. The error conditions are explicitly called out in a formal use
           case as exception courses. When we fail to think about how things can go wrong, we take a bad
           situation (an error) and make it worse by leaving our users with no reasonable way to deal with
           the errors." Every actor step in the main scenario should have a system response; the same
           discipline applies to every extension. -->

| Extension | Condition | Handling | Outcome |
|---|---|---|---|
| {{extension_id}} | {{extension_condition}} | {{extension_handling}} | {{extension_outcome}} |

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
     ASK   What must stay true however this use case ends, success or failure alike, to protect the
           stakeholders' interests? What is additionally true only when it ends successfully?
     GOOD  "Minimal Guarantees: the account holder's current password keeps working until a new one is
           confirmed, so an abandoned or failed reset never locks them out. Success Guarantees: the
           account has a new password, and every other active session for that account is signed out."
     WEAK  "Minimal Guarantees: the system doesn't crash. Success Guarantees: it worked." (neither is a
           checkable condition of the world, and neither names what the earlier Stakeholders list cares
           about)
     TRAP  Writing only a success condition and treating "it didn't fail" as the minimal guarantee. A
           minimal guarantee is a positive statement about what is protected on every exit, including a
           failed one, not an absence of failure; a template that asks only for success and failure end
           conditions never asks what must stay true however the case ends, which is exactly the gap this
           pairing closes. -->

**Minimal Guarantees:** {{minimal_guarantees}}

**Success Guarantees:** {{success_guarantees}}

## Related Information

<!-- WHAT  An open slot for whatever project-specific facts this use case needs beyond its core fields:
           priority, performance target, frequency, a channel or device difference that would otherwise
           bifurcate the scenario, secondary actors, and any superordinate or subordinate use case.
     WHY   Cockburn's 1998 template closes with exactly this block: "RELATED INFORMATION (optional)
           Priority: <how critical to your system / organization> Performance Target: <the amount of time
           this use case should take> Frequency: <how often it is expected to happen> Superordinate Use
           Case: <optional, name of use case that includes this one> Subordinate Use Cases: <optional,
           depending on tools, links to sub.use cases> Channel to primary actor: <e.g. interactive, static
           files, database> Secondary Actors: <list of other systems needed to accomplish use case>". A note
           on that template says his book renamed the sub-variations field to "Technology and Data
           Variations List", the line for a channel or device difference, which lets the Main Success
           Scenario above stay at the level of intention. Deep dive:
           use-case-specification_companion.md section 3 (Related Information).
     ASK   How critical is this use case, and how long should it take? How often does it happen? Does any
           secondary actor, system, or device variation belong here instead of inside the scenario? Does
           this use case include or get included by another one? Does any step enforce a business rule?
           Reference each rule by its identifier and say where its text lives, rather than copying it
           here. A nonfunctional requirement shared by
           many use cases is better linked from here than restated: OpenUP asks, "Are these nonfunctional
           requirements applicable to many use cases?" and answers, "consider capturing them in the
           supporting Requirements Specification to simplify maintenance".
     GOOD  "Priority: high (a core account-recovery path). Performance Target: the reset email arrives
           within two minutes at p95 (illustrative). Frequency: rare per account, constant in aggregate
           across all accounts. Technology and Data Variations: the request can also start from the
           mobile app. Secondary Actors: the email delivery service. Superordinate/Subordinate Use Cases:
           none."
     WEAK  "Priority: important." (no performance target, no frequency, nothing a reader could check against
           later)
     TRAP  Copying a performance target or priority that belongs to many use cases into this one instead of
           linking to where it is set once. OpenUP's own rule names exactly this failure. -->

**Priority:** {{priority}}

**Performance Target:** {{performance_target}}

**Frequency:** {{frequency}}

**Technology and Data Variations:** {{technology_and_data_variations}}

**Secondary Actors:** {{secondary_actors}}

**Superordinate/Subordinate Use Cases:** {{related_use_cases}}

## Open Issues and Schedule

<!-- WHAT  Unresolved questions this use case still carries, each with an owner, and the release or date it
           is due by.
     WHY   Cockburn's 1998 template closes with both fields: "OPEN ISSUES (optional) <list of issues about
           this use cases awaiting decisions>" and "SCHEDULE Due Date: <date or release of deployment>".
           Wiegers asks for the same content in different words: "List any additional comments about this
           use case or any remaining open issues or TBDs (To Be Determineds) that must be resolved." This
           is the one section with no corroboration from Cockburn's own later draft, which carries neither
           field. Deep dive: use-case-specification_companion.md section 3 (Open Issues and Schedule).
     ASK   What is still unresolved about this use case? Who owns resolving each open issue, not just that
           one exists? What release or date is this use case due by?
     PRIORITY  Name an owner for every open issue; an issue with no owner has no path to resolution.
     ROW HINT  A good row names the open question, who owns it, and when it must be resolved by. A weak row
           names only that something is undecided.
     GOOD  | Should a locked-out account auto-unlock once the reset completes, or stay locked pending a
           separate security review? | Security Lead | Before next release |
     WEAK  | It's not clear what happens on failure | (unowned) |
     TRAP  Recording an open issue with no owner. An unowned open issue tends to stay open past the date
           this use case is due, because no one is accountable for closing it. -->

| Open Issue | Owner | Needed By |
|---|---|---|
| {{open_issue}} | {{open_issue_owner}} | {{open_issue_deadline}} |

**Due Date:** {{due_date}}
