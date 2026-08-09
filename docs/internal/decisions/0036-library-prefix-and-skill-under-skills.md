---
status: accepted
date: 2026-08-08
decision-makers: [jprisant]
consulted: [claude]
---

# Adopt the `plt-` component prefix and move the skill to `skills/plt-fill-template/`, reaching convergent tier

## TL;DR

- **Decision:** the library takes the component prefix `plt-`, and its single skill moves from the
  repository root to `skills/plt-fill-template/SKILL.md`, renamed from `product-lifecycle-templates` to
  `plt-fill-template` so the skill's `name` matches its parent directory. The **plugin** keeps the name
  `product-lifecycle-templates`; only the component inside it is prefixed.
> **Correction, 2026-08-08.** The "Why" bullet below claims the root `SKILL.md` "was almost certainly
> never discoverable by either consumer that matters". **That is false for the skills CLI**, and the word
> "almost certainly" is doing work no evidence supported. Tested on 2026-08-08 against a `v0.2.1`
> worktree, `npx skills add` reports **"Found 1 skill"** for the old layout: it looks for a root
> `SKILL.md` **by design**, and finding one short-circuits its entire subdirectory search.
>
> The claim about the **Agent Skills specification** and the **Claude Code plugin loader** is untested and
> may well hold; only the CLI half is refuted. **The decision itself does not change** - the move was
> required by the Standard at convergent tier regardless, and this record is corrected rather than
> superseded.
>
> The error had a consequence. Because the root file was believed inert, nobody predicted that removing it
> would switch the CLI's subdirectory search on, which is what caused the maintainer-internal build
> harness to start shipping. That is recorded in
> [ADR 0037 (keep the build harness off the published skill surface)](0037-keep-the-build-harness-off-the-published-skill-surface.md).

> **Second correction, same date.** The Context and Consequences sections below call the roadmap's install
> retest one that "has never been run" and say it "stays open". **It was run later the same day.** The
> install succeeds, and running it produced two real defects. The retest is recorded in full in
> [the roadmap](../roadmap.md)'s D2 block; what it obliged is in
> [ADR 0037](0037-keep-the-build-harness-off-the-published-skill-surface.md). Both statements were true
> when written, so they are marked in place rather than rewritten.

- **Why:** the move is not a compliance chore. The root `SKILL.md` was almost certainly never discoverable
  by either consumer that matters: the Agent Skills specification defines a skill as a directory whose
  `SKILL.md` carries a `name` matching that directory, and the Claude Code plugin loader scans `skills/`.
  Neither reads a `SKILL.md` at a repository root. The prefix is required at convergent tier and prevents a
  name collision once components are emitted alongside other libraries'.
- **Status:** accepted 2026-08-08. Raises the declared tier from universal to **convergent**, which is a
  measured result rather than a declaration. The registry listing still pins `v0.2.1` and is unaffected
  until re-pinned, which is a separate maintainer action.

## Context and Problem Statement

[ADR 0001 (repo and package name)](0001-repo-and-package-name.md) settled that
`product-lifecycle-templates` is the name used everywhere: the git repository, the plugin manifest, and the
install string. That decision was about the **library**. It said nothing about what the components inside
the library are called, because at the time there were none.

`v0.2.0` then shipped a `SKILL.md` at the repository root, closing the gap
[STATE.md decision D2](../../../STATE.md) had recorded: `npx skills add` against this repository cloned it and
installed nothing, reporting "No valid skills found." The fix was understood as one missing file.

Two things have since come into view that the original fix did not account for.

**First, the Advanced Skill Library Standard requires a prefix at convergent tier and above.** Requirement
S2 (section 8.2) requires `library.json` to declare a lowercase kebab-case `prefix` ending in a hyphen, and
requires every component name to start with it. Requirement S3 requires each declared component to exist on
disk at the declared path under `skills/`. This library declares one skill named
`product-lifecycle-templates` at path `.`, which satisfies neither: no name can begin with a prefix derived
from itself, and the root is not `skills/`.

**Second, and more important, the root placement was probably never working.** Two independent facts point
the same way, and neither was checked when the file was added:

- The [Agent Skills specification](https://agentskills.io/specification), read and recorded as
  [STATE.md decision D3](../../../STATE.md) on 2026-07-17, defines exactly one unit: a directory containing
  `SKILL.md`, whose `name` field **must match the parent directory**. A `SKILL.md` at a repository root has
  the repository directory as its parent, which is an accident of where someone cloned it.
- The Claude Code plugin loader discovers skills by scanning a `skills/` directory. A root `SKILL.md` is
  not in it.

The retest that would have caught this is written into
[the roadmap](../roadmap.md) and **has never been run**: "record whether
`npx skills add product-on-purpose/product-lifecycle-templates` now installs." **[Run later the same day.
See the second correction at the top of this record.]** The control in the original
D2 test, `skills add product-on-purpose/pm-skills`, **succeeded**, and `pm-skills` uses the
`skills/<name>/SKILL.md` layout. So the layout this record adopts is the one with a passing test behind it,
and the layout it replaces is the one with no test at all.

## Decision Drivers

- Convergent tier is blocked by exactly two requirements, and both live in this one decision.
- A prefix must be chosen once and is expensive to change later, because it is baked into every component
  name a consumer installs.
- The library's own standing rule is to **measure a tier rather than declare one**. The gate is the
  arbiter, and it is run before and after.
- An unverified install path is a claim on credit. This record should reduce the claim, not restate it.

## Considered Options

* **Option A: prefix `plt-`, skill at `skills/plt-fill-template/`.** Chosen.
* **Option B: prefix `plt-`, skill at `skills/plt-templates/`.**
* **Option C: keep the root `SKILL.md` and declare no components**, staying at universal tier.
* **Option D: keep the root `SKILL.md` and additionally ship `skills/plt-.../SKILL.md`.**

## Decision Outcome

Chosen: **A. The prefix is `plt-`, and the skill is `plt-fill-template` at
`skills/plt-fill-template/SKILL.md`.**

`plt-` is the initialism of the library name, matching the sibling convention in
`agent-skills-toolkit`, whose prefix is `askit-` and whose skills sit at
`skills/askit-<verb>-<noun>/SKILL.md`. The verb-first component name follows the same sibling: the skill's
own description says it "selects and fills a researched product-document template ... then grades the
result", and filling is the action a caller wants.

**The plugin name does not change.** `.claude-plugin/plugin.json` and the registry entry keep
`product-lifecycle-templates`. Prefixing applies to components inside a library, not to the library, which
is why `agent-skills-toolkit` ships `askit-` skills without being called `askit`.

Option B was rejected because `plt-templates` names the noun the library already is, and would read as the
library rather than as an action taken with it. Option C was rejected because it trades a real defect for a
cosmetic pass: declaring no components would satisfy S3 by having nothing to check, while leaving the skill
in a location neither consumer reads. Option D was rejected outright: two copies of one skill is the
dual-maintenance surface this library exists to argue against, and the Agent Skills spec's
name-matches-directory rule means the two copies could not even carry the same `name`.

### Consequences

* Good: convergent tier is reached, and both blocking requirements are closed by one coherent change rather
  than by two unrelated patches.
* Good: the skill is, for the first time, in the location both the Agent Skills specification and the
  Claude Code plugin loader actually read.
* Good: a prefix now exists, so a second component can be added without renaming the first.
* Bad, and stated plainly: **the installed skill's name changes** from `product-lifecycle-templates` to
  `plt-fill-template`. Anyone who installed the former gets a differently named skill on next install.
* **Open, and not closed by this record:** whether `npx skills add` now succeeds is still untested. This
  record improves the odds on documented spec behaviour and a passing control, and it does not claim the
  install works. The roadmap retest stays open, and the README's installability paragraph is corrected in
  this change from a stale "ships no `SKILL.md`" to an accurate "ships one, untested".
  **[Closed later the same day: the retest was run and the install succeeds. See the second correction at
  the top of this record.]**
* The registry listing pins `v0.2.1`, whose tree has the old layout, and is unaffected until deliberately
  re-pinned. Re-pinning is a cross-repository action and stops for the maintainer, per
  [decision procedures](../decision-procedures.md).

## More Information

The tier claim is measured, not asserted. Before this change,
`node scripts/tier-report.mjs . --json` from `agent-skills-toolkit` reported `"tier": "universal"` with
convergent blocked by `S2` and `S3`. After it, the same command reports convergent. That command, not this
paragraph, is the evidence.

Related: [ADR 0001 (repo and package name)](0001-repo-and-package-name.md) for the library name this record
deliberately leaves alone, and [ADR 0013 (local split and going public)](0013-local-split-and-going-public.md)
for the public-surface reasoning the root placement originally followed.
