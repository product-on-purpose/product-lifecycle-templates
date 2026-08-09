---
status: accepted
date: 2026-08-08
decision-makers: [jprisant]
consulted: [claude]
---

# Keep the build harness off the published skill surface, and gate the surface rather than trusting the layout

## TL;DR

- **Decision:** the maintainer-internal build harness moves from `.claude/skills/build-bundle/SKILL.md` to
  a Claude Code slash command at `.claude/commands/build-bundle.md`, and
  [`tools/check-export-surface.py`](../../../tools/check-export-surface.py) asserts in CI that the set of
  skills an installer would export equals exactly the set [`library.json`](../../../library.json) declares.
- **Why:** on 2026-08-08 the first ever execution of `npx skills add` against this repository reported
  **two** skills and installed both. The second was the build harness, whose own description says it is
  not shipped to library users. No check here could see it, because every check here validates the tree
  and none of them asked what a stranger receives.
- **Why a check and not just a move:** the installer scans **thirty-one** directory prefixes,
  twenty-seven of them agent-config directories including `.claude/skills`, **`.codex/skills`** and
  `.github/skills`, and it reads no ignore file. Moving one file fixes one leak. The next one is most
  likely `.codex/skills`, in a repository whose maintainer also uses Codex.
- **Status:** accepted 2026-08-08. Does not change the declared tier; the Standard's gate was re-run with
  the move applied and reports **Advanced, no blockers, 0 errors**.

## Context and Problem Statement

[ADR 0036 (the library prefix and the skill's path)](0036-library-prefix-and-skill-under-skills.md) moved
this library's public skill from a root `SKILL.md` to `skills/plt-fill-template/SKILL.md`. That decision
was correct and is not reopened here.

It also had a consequence nobody predicted, because the retest that would have shown it had been open
since 2026-07-17 and was not run until three weeks later.

**The installer short-circuits on a root `SKILL.md`.** Its discovery routine reads:

```js
if (await hasSkillMd(searchPath)) { ...; if (!options?.fullDepth) return skills; }
const prioritySearchDirs = [searchPath, join(searchPath, "skills"), ..., ...AGENT_PROJECT_SKILL_DIRS]
```

A root `SKILL.md` is taken and the function **returns**, never searching subdirectories. This repository
had one until ADR 0036 removed it. With it gone, the search descended into `AGENT_PROJECT_SKILL_DIRS`,
which contains `.claude/skills`, and found the build harness.

**So a correct change removed a protection nobody knew existed.** That is the shape worth recording: the
defect was not introduced by a mistake, and reviewing the change more carefully would not have revealed
it. Only running the install did.

## Decision Drivers

- **A published surface should be declared, not incidental.** Today what ships is "whatever happens to sit
  in a directory some external tool decided to scan". `build-bundle` is the first thing to fall through
  that, not the last.
- **`.claude/` is consumer configuration, not source.** In a private repository, putting a build tool
  there is unremarkable. In a published one it silently makes development tooling part of the
  distribution.
- **The installer offers no exclusion mechanism.** Its skip list is hardcoded to `node_modules`, `.git`,
  `dist`, `build` and `__pycache__`. A search of the distributed bundle for `.skillsignore`, `ignoreFile`
  and `ignorePatterns` returns nothing.
- **Whatever is chosen must survive the tool changing.** `AGENT_PROJECT_SKILL_DIRS` is a hardcoded list in
  a package at version 1.5.22 that ships often.

## Considered Options

1. **Convert to a slash command** at `.claude/commands/build-bundle.md`.
2. **Relocate the skill** to `tools/build-bundle/SKILL.md`, with a gitignored junction at
   `.claude/skills/build-bundle` to preserve local discovery.
3. **Relocate without the junction**, accepting the loss of local invocation.
4. **Ship it and document a workaround** (`--skill plt-fill-template`).
5. **Move it to the maintainer's global `~/.claude/skills/`.**

## Decision Outcome

**Chosen: option 1, the slash command, plus the export-surface check in every case.**

Every claim below was verified rather than reasoned about.

| Claim | How it was verified |
|---|---|
| A command is invisible to the installer | Synthetic fixture across four locations, **and** the real repository at a scratch commit: "Found 1 skill: `plt-fill-template`" |
| `tools/**/SKILL.md` is also invisible | Same fixture |
| A command is invisible to the **Standard** too | The toolkit's `listCommandFiles` reads `<root>/commands/`, not `.claude/commands/`, so the file never becomes a declared component and never triggers `command-contract` (S7) |
| Gold tier survives | Gate run with the move applied: `DECLARED: advanced, MEASURED: advanced, BLOCKED: nothing, 0 error(s), 0 warning(s)` |
| No Codex obligation is created | `per-target-presence` (S6) returns early for undeclared targets, and `library.json` declares `agent-targets: ["claude"]` only |
| **Claude Code actually loads it as `/build-bundle`** | **Added 2026-08-09.** The maintainer typed `/build-bundle` in a live session and it resolved, rendering the command body with its intended description. Until then this row did not exist, and it is the load-bearing one: the option was chosen partly because "it keeps `/build-bundle` working", which was **reasoned about rather than verified** while sitting three lines under a heading that says every claim here was verified. Nothing about the file could establish it, because the only instrument is a human typing the command. The fallback in option 2, `tools/build-bundle/SKILL.md`, is therefore **not needed** and stays recorded as the tested alternative rather than a pending action. |

**Why option 1 over option 2 or 3.** It keeps `/build-bundle` working with **no per-machine setup**, and
it keeps the harness in `.claude/`, where a repository's own agent configuration belongs. Option 2 buys
the same outcome at the cost of a gitignored junction every contributor must recreate and nobody can see;
option 3 loses local invocation for no gain over option 1.

**A modelling argument that stands on its own.** A skill is **model-invoked**: Claude decides to reach for
it. A command is **user-invoked**. This harness runs research fan-outs and opens pull requests, and should
only ever run because somebody typed it. It was a command wearing a skill's clothes.

**Why option 4 was rejected.** It leaves the default install wrong and depends on every user passing a
flag they have no reason to know about.

**Why option 5 was rejected.** Maximally robust, since nothing in the repository can leak, but it drops the
build harness out of version control. That is a worse trade than the leak.

### The check is the part that lasts

Relocating a file addresses one instance. `check-export-surface.py` addresses the class:

- It encodes the installer's own **thirty-two priority prefixes** as data, including the root
  short-circuit, copied from `skills@1.5.22` and dated in the source.
- It fails in **both** directions. An undeclared skill that would ship is the leak above. A declared skill
  that would **not** ship is the same defect pointed the other way: an install silently missing something
  the library promises.
- It was mutation-checked three ways: the original leak restored under `.claude/skills`, a new leak under
  `.codex/skills`, and a declared-but-absent component. All three fail; the clean tree passes.

**Its own limitation is printed on every run.** `PRIORITY_PREFIXES` is a copy of an upstream constant. If
that list grows, this check goes stale *in the dangerous direction*, by continuing to pass. The honest
mitigation is to re-read it when the installer majors, and the check says so rather than implying a
guarantee it cannot make.

### Consequences

- **Good:** the install ships exactly one skill, verified against the real repository. The class of defect
  is gated rather than remembered. The harness gains a more honest invocation model.
- **Good:** the Codex recurrence, which is the likely next instance, now fails CI instead of shipping.
- **Bad:** `build-bundle` no longer auto-triggers. It must be typed. For a tool that opens pull requests
  this is a feature, but it is a real behaviour change.
- **Bad:** the repository now depends on a copied upstream constant staying accurate, which is a new thing
  to keep true. It is stated in the tool's own output rather than assumed.
- **Neutral:** four documents referencing the old path were updated. Nothing about the public skill or the
  bundles changed.

## More Information

- The retest that found this, in full, including the two other findings and one refuted claim:
  [`docs/internal/roadmap.md`](../roadmap.md), the D2 retest block.
- The defects as recorded when found: [`STATE.md`](../../../STATE.md), B-1 and B-2.
- The install routes and what each delivers: [`docs/how-to/installing.md`](../../how-to/installing.md).
- **A correction this decision forces on [ADR 0036](0036-library-prefix-and-skill-under-skills.md)**,
  applied there in place and dated: its claim that the root `SKILL.md` "was almost certainly never
  discoverable by either consumer that matters" is **false for the skills CLI**, which finds a root
  `SKILL.md` by design and short-circuits on it. That error is the reason this consequence was not
  predicted, and it is corrected rather than left standing.
