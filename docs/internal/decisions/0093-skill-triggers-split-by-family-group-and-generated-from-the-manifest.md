---
status: proposed
date: 2026-11-26
decision-makers: [jprisant]
consulted: [claude]
---

# Skill descriptions are generated from the manifest, and split by family group before the cap is reached

## TL;DR

- **Decision.** The skill descriptions stop being hand-written. A generator writes them from `manifest.json`, using
  a new required meta field, `trigger_name`, and a hand-chosen order table. It fails when a description would pass
  1,024 characters. The trigger test moves into the repository and runs at any release that changes a description.
- **The skills split by family group before the 60th bundle lands.** Every type must stay named in some
  description, and one description cannot hold 60. **Which split shape to use is not settled.** The shape tested
  here split the fill skill only, and it lost runs on one type. The grade skill has the same cap and cannot drop
  its type list. Both remaining shapes are untested.
- **Why.** After v0.28.1 both descriptions sit within 11 and 3 characters of the cap, so the 60th bundle cannot be
  named without dropping or shortening another. Six rounds of tests on 2026-11-25 and 2026-11-26 showed that a skill
  loads for the types its description names, for grading as well as filling.
- **Status:** proposed 2026-11-26. The maintainer asked for this draft. The split shape needs one confirming test run
  before this record can be accepted. *(2026-11-26: the maintainer chose to build the parts that hold whatever the
  shape, the field and the generator, before that run. They shipped in the same pull request as this record, and
  the generator reproduces both v0.28.1 descriptions character for character. See "What was built" below.)*

## Context and Problem Statement

An agent decides whether to load a skill by reading its description in the skill listing. This library has two
skills, `plt-fill-template` and `plt-grade-doc`, and each description lists every document type by name. That list
is the trigger: a type it leaves out may never reach the skill. *(The rule was recorded in
[`release-process.md`](../release-process.md) on 2026-10-15, and measured on 2026-11-25.)*

The Agent Skills specification caps `description` at 1,024 characters, and the toolkit's G2 gate enforces that
cap here. After v0.28.1 the two descriptions measure 1,013 and 1,021 characters, so neither can name a 60th type.

### What the tests found

All tests used `claude plugin eval` (Claude Code 2.1.329) on Sonnet. Each run was a fresh session with only this
plugin loaded and the MCP server removed. A grader checked that the expected skill loaded within three turns. The
write-up and every result file are in the maintainer's local research folder,
`_local/research/2026-11-25_skill-trigger-test/`. The six rounds cost about $68 at API list rates.

| Round | Wording | Right skill loaded |
|---|---|---|
| 1 | The full list, as shipped in v0.28.0 | 101 of 110 |
| 1 | A short category sentence with ten examples | 89 of 110 |
| 3 | A list under seven category headings, with names merged | 150 of 165 |
| 3 | The full list with three names shortened, shipped in v0.28.1 | 163 of 165 |
| 4 | Fill split into two skills by family group, with a short grade description, over 43 cases | 211 of 215 |
| 5 | Ten grading requests for types the short grade description does not name | 39 of 50, against 45 shipped |

What the rounds show, with confidence:

- **Naming drives triggering (high).** The short sentence missed internal announcement, traceability matrix and
  spike report, which it does not name. The full list missed competitive analysis, the one type it left out.
- **The same holds for grading (medium).** The short grade description named ten example types. On a bug report,
  which it does not name, it loaded on 0 of 5 runs, against 5 of 5 for the shipped list. On the other unnamed types
  it held, so the defect is that nobody can predict which unnamed type falls. A status-report request loaded no
  skill under either wording, because the agent answered it directly. That is a prompt effect, not a wording effect.
- **Shortening a name can break it (high).** Merged as "test plan, case", the test-case request fell to 1 of 5. Cut
  to "readiness review", the production-readiness request fell to 1 of 5.
- **The agent did not confuse two fill skills (medium).** Each run's trace was read for the skills it loaded. Every
  fill request loaded its own group's skill, on all 131 runs of 27 requests that loaded one. No run loaded both fill
  skills, and no fill request loaded the grade skill.
- **Splitting the fill list cost one type (medium-low).** Run in one session at 15 runs each, the data-dictionary
  request loaded the right skill on 14 runs under the shipped list. Under the split it loaded on 8 runs, and on 6
  when the shipped grade text ran beside it. Every miss followed one pattern: the agent searched the empty test
  folder for the schema, found none, and declined to invent the columns. The cause is unknown. The split changed
  both the list's order and its opening sentence, and neither was tested alone. This case's rate also swings
  between sessions, from 4 of 15 to 14 of 15 under identical wording, which is why the confidence is low.
- **The spike-report drop did not repeat.** It fell to 11 of 15 once and recovered to 14 of 15, so it is treated as
  noise.

### Why one longer field will not do

Claude Code accepts a second field, `when_to_use`. The [skills documentation](https://code.claude.com/docs/en/skills)
says it is "Appended to `description` in the skill listing and counts toward the 1,536-character cap." That adds at
most 512 characters, which is about 30 more names, once. Worse, claude.ai and the Skills API reject any `SKILL.md`
field outside six: `allowed-tools`, `compatibility`, `description`, `license`, `metadata` and `name`. The
toolkit quotes that error and flags such fields as advisory finding ADV1. A skill using `when_to_use` would fail to
upload there.

## Decision Drivers

- **Every type must be named, and a name changes only after a test.** The tests support the full name, and the
  shortened or merged names a test has already shown safe, such as v0.28.1's "product or sprint backlog". Every
  other shortening is a risk, for both skills. Naming every type at its full name does not fit even today: with
  the eight shared phrases unmerged, the fill description measures 1,103 characters for 59 bundles.
- **A new bundle must not need a judgment call about wording.** Adding a type should land it in a trigger list
  mechanically, the way it already lands in `manifest.json`.
- **The skills must stay portable.** The six-field frontmatter is the portable set, so no Claude-Code-only field.
- **The listing must stay small.** Every installed skill costs every session a line in the listing, whether or not
  it is used.
- **A wrong pick must be harmless.** If the agent loads the "wrong" skill of a pair, the document must come out the
  same.

## Considered Options

1. **Keep one list per skill and shorten names as the cap bites.** This is what v0.28.1 did. It has no runway left,
   and the tests showed that shortening is where triggers break.
2. **A short category sentence with examples.** Rejected for both skills: it lost runs on types it did not name.
3. **A list under category headings, with names merged.** Rejected: 150 of 165 runs, against 156.
4. **Add `when_to_use`.** Rejected: it buys about 30 names once, and it breaks upload to claude.ai and the Skills
   API.
5. **One skill per family, eleven fill skills or more.** Rejected: it adds at least nine listing entries to every
   session, and three families hold three types or fewer.
6. **Rely on the MCP server's `search_templates` instead of the descriptions.** Rejected: the `npx skills add`
   route installs the skills without the server, and an agent must load a skill before it can search anything.
7. **Generate the descriptions, and split by family group (chosen).** Three split shapes were considered:
   - **7a. Split fill only, and shorten grade.** Tested in rounds 4 to 6. Rejected, because the short grade
     description lost the bug report, and a full grade list hits the same cap.
   - **7b. Split both skills by the same family groups**, giving two fill skills and two grade skills. Untested. It
     makes the listing about 2,900 characters, against 2,034 today.
   - **7c. Two group skills, each of which fills and grades its group's types.** Each description would name its
     group's types once, with both kinds of verb. Untested. It keeps the listing near today's size, but it merges two
     skills whose bodies differ, which is a larger change.

## Decision Outcome

**Chosen: option 7, with the split shape left to one confirming run.** The parts that hold whatever the shape, in
the order they would be built:

1. **A required meta field, `trigger_name`.** It holds the phrase a bundle is listed under, in the words a
   requester uses, such as "PRD" or "browser or device support matrix". Bundles that share one phrase in the list
   carry the same value, such as "product or sprint backlog", and the phrase is written once. Twenty of the 59
   shipped phrases match no title or alias in `manifest.json`. Sixteen of those are the eight shared phrases. The
   other four are single names: "PRD", "user stories", "internal announcement" and "browser or device support
   matrix". So the field cannot be derived, and it is required rather than defaulted. `tools/meta.schema.json`
   gains it, and `manifest.json` carries it.
2. **A generator, `tools/gen-skill-descriptions.py`.** It reads `manifest.json` and two small tables. One maps
   each family to a skill group. The other is the order the list names types in, because the shipped order is
   neither manifest order nor family order, and the tests showed that a name's position changes how often it
   triggers. So the generator never sorts, and a new bundle needs its place in the order table. The generator
   writes each description as a fixed sentence around the group's phrases. CI fails when a written description
   differs from what the generator would write, as it does for `manifest.json` today. The generator also fails when
   a bundle is missing from the order, when two bundles that share a phrase are apart in it, and when any
   description would pass 1,024 characters. That last failure is the signal for the next split, and moving a family
   between groups is a new decision.
3. **The trigger suite moves into the repository**, under `evals/skill-triggers/`, with its builder and scorer. It
   runs at any release that changes a description, at about $12 for a full run. Five runs per case cannot separate
   a regression from noise on the fragile cases: at five runs, round 4 flagged the spike report, which was noise,
   and passed the data dictionary, which was the real regression. So the rule has two parts:
   - Every case runs at 5 runs on the new wording.
   - The cases known to be fragile, today data dictionary and spike report, run at 15 runs on both wordings in one
     session. A drop of three or more runs in 15 blocks the release until the maintainer reads it.

**The confirming run.** It builds shapes 7b and 7c from the generator's real output, not hand-written text, and runs
each against the shipped wording. It uses the 53 cases of rounds 1 to 5, at 5 runs, plus the two fragile cases at
15. The shipped wording already has results on all 53 cases, so only the fragile pair reruns it. The estimate is about
$17 for one shape, or about $32 for both. The shape that holds the shipped wording's
rate, within the rule above, is the one this record adopts.

### The counter-arguments this record keeps

- **More skills cost more attention.** Each skill is used less often, and Claude Code drops descriptions for the
  least-used skills first when a listing overflows. *(Medium confidence: the drop order and the listing's budget of
  1% of the context window were read only through a summary of the skills documentation, not verbatim.)* A crowded
  session may drop these descriptions sooner. Nobody measured that, because every test loaded only this plugin.
- **The group boundary is the library's convenience, not the requester's.** In the tested grouping, "design
  principles" and "product principles" sit with the engineering group, because `standing-standards` does. That
  costs nothing when a wrong pick is harmless, but it reads oddly.
- **A new skill name is new public surface.** Once shipped, renaming it is a breaking change for anyone who invokes
  it by name.
- **The data-dictionary loss may come back under any split.** If both confirming shapes lose it, the fix may be its
  place in the list rather than the shape.

### Consequences

- **A minor release**, because it adds a skill. `library.json` gains each new skill entry, and
  `tools/check-export-surface.py` then expects that set. `tools/check-version-agreement.py` reads one more version
  per skill.
- **Every bundle's meta gains `trigger_name`**, 59 edits in one PR, with `manifest.json` regenerated.
- **The installing guide, `AGENTS.md`, the README and `INDEX.md`** name the new set of skills.
- **The bundle pipeline gains a step.** A new bundle sets `trigger_name` and takes a place in the order table, and
  the generator does the rest. The place is a judgment call, so it is the one part a person still chooses.
- **The release process's trigger-list rule changes.** It stops asking a person to edit the descriptions, and it
  points at the suite instead.
- **No bundle is queued today**, so nothing forces the confirming run before one is.

### What was built, 2026-11-26

The maintainer chose to build parts 1 and 2 before the confirming run, because both hold whatever the shape.
They shipped with this record, which stays proposed.

- **The field.** Every meta carries `trigger_name`, set to the phrase the v0.28.1 descriptions use, and the schema
  requires it. A name changes only after a test, so no name was improved on the way in.
- **The generator and its check.** It runs with one group, which holds every family, and both skills list it.
  Its output matches both shipped descriptions character for character, at 1,013 and 1,021 characters, so this
  change moves no trigger and needed no model run. Two CI steps run it: `--check` against both `SKILL.md` files, and
  a fixture self-test that proves each failure rule fires.
- **What the draft got wrong.** It said a `trigger_name` per bundle was enough. It was not, for two reasons. The
  shipped list merges eight pairs into shared phrases, and its order is hand-chosen. So the generator gained the
  shared-phrase rule and the order table in part 2 above.

Part 3, the trigger suite in the repository, was built on 2026-11-27, at
[`evals/skill-triggers/`](../../../evals/skill-triggers/README.md). It holds the 53 cases, a builder that takes the
skills from the working tree or a git ref, a runner for the release procedure, and a scorer that applies the
two-part rule. Replayed on the round-5 result files, the scorer blocks the real data-dictionary regression and
passes the spike report. A one-request smoke run through the runner cost USD 0.05 and loaded the right skill.
Graders match a skill-name prefix, so shape 7b needs none changed, and shape 7c would.

### What this record does not settle

- **The split shape.** See the confirming run.
- **Opus and Haiku were not tested.** Every run used Sonnet.
- **Crowded sessions were not tested.** See the first counter-argument.
- **32 of the 59 types have no dedicated fill request** in the suite. They are named in a description, which is
  what the tests show matters, but no run tried them.

## More Information

- The rule this record builds on: [`release-process.md`](../release-process.md), section 1, the trigger-list note.
- The skills: [`plt-fill-template`](../../../skills/plt-fill-template/SKILL.md) and
  [`plt-grade-doc`](../../../skills/plt-grade-doc/SKILL.md).
- The export-surface check this changes: [ADR 0037 (keep the build harness off the published skill
  surface)](0037-keep-the-build-harness-off-the-published-skill-surface.md).
- The skill path convention: [ADR 0036 (the library prefix and the skill's path)](0036-library-prefix-and-skill-under-skills.md).
