---
status: accepted
date: 2026-09-15
decision-makers: [jprisant]
consulted: [claude]
---

# Site dependency updates follow the family Dependabot pattern, and no `npm audit` gate is added

## TL;DR

- **Decision:** when the Node toolchain lands, this repository adopts `pm-skills`' Dependabot
  configuration for the `npm` ecosystem at `/site`: **weekly, grouped, `minor` and `patch` only**, with a
  `dependencies` label and a `chore(deps)` commit prefix. **No `npm audit` step is added to CI** and no
  advisory blocks a build. Major bumps arrive as individual pull requests and are read by hand, which is
  where an Astro or Starlight major belongs.
- **Why:** this is section 9 item 6 of [`site-plan.md`](../site-plan.md) - the one part of taking on Node
  that [ADR 0046](0046-the-site-is-astro-starlight-under-pattern-s.md) did **not** settle. The family
  already runs a pattern, and "match family-wide" is the plan's own conformance standard, so adopting it
  *is* conformance and inventing a local one would be the departure.
- **The cost, named:** a recurring weekly pull-request stream in a repository that has never had one, and
  a second dependency surface whose updates nobody is obliged to merge.
- **Status:** accepted 2026-09-15. Decided by the agent under explicit maintainer delegation ("move
  forward with your best decision and record your reasoning"), with the maintainer as the accountable
  decision-maker. Binds nothing until the toolchain exists; the config file lands with S0.

## Context and Problem Statement

[`site-plan.md`](../site-plan.md) section 9 lists six concrete costs of taking on Node. Five are specified
by [ADR 0046](0046-the-site-is-astro-starlight-under-pattern-s.md): the `engines.node` floor, the `.nvmrc`
pin read through `node-version-file`, the committed lockfile with `npm ci`, the local guard port, and the
gitignore entry. The sixth is not decided anywhere:

> A decision about whether `npm audit` or Dependabot applies, which this repository has never needed.

**Verified 2026-09-15: this repository has no `.github/dependabot.yml` at all** - not for npm, which does
not exist here yet, and not for GitHub Actions, which does. So the question is not "change the policy" but
"there is no policy, and a second ecosystem is about to arrive."

### The question this record is *not* reopening

For four days the repository carried "approve the Node toolchain" as an open maintainer decision, in
`site-plan.md` section 14 item 2 and in a session log's waiting-on list. **It was not open.** ADR 0046
chose Astro plus Starlight from five options, none of which supplies Astro without Node; said so in its
TL;DR ("also decided, and the part with teeth: this repository takes on Node"); fixed the version set; and
listed the second toolchain in its Consequences under "Bad, and stated plainly", which is this
repository's form for an accepted cost rather than a deferred one. Node is entailed by the option that was
chosen.

The error was documentary, and tighter than it looks: **ADR 0046 and section 14 landed in the same
commit**, `b534fd1`. Item 1 was annotated as closed by that record and item 2 was not, so one change both
decided Node and asked for permission to decide it. Nothing drifted; the commit disagreed with itself,
which is why no later sweep caught it. Both items are corrected in place on 2026-09-15, per
[ADR 0011](0011-madr-v4-at-docs-internal-decisions.md)'s rule that a factual error is corrected where it
sits and only a changed decision takes a new number. **This record takes a new number because the
dependency-update policy is a decision nobody had made**, not because Node is being re-decided.

## Decision Drivers

* **"Match family-wide" is the conformance standard the plan already adopted**, and the family has a
  working pattern rather than a specification to interpret.
* **Unattended rot is the plan's own named risk.** Its risk table carries "Node toolchain rots unattended
  in a Python repo" with the lockfile as the mitigation - but a lockfile freezes a build, it does not
  update anything. Manual-only is that risk unmitigated.
* **A gate that fires on things nobody can act on becomes a gate nobody trusts.** DF-7 is this
  repository's cautionary tale about a check that *could not* fail; the opposite failure is a check that
  fails constantly on findings outside the maintainer's control, and its end state is the same - someone
  adds `--audit-level=critical` or `|| true` and it is a report again.
* **One maintainer.** Pull-request volume has to stay proportionate or the stream gets muted, which is
  worse than not having it.

## Considered Options

1. **Adopt the family Dependabot pattern; no audit gate** (this decision).
2. **Dependabot plus an `npm audit` step in CI.**
3. **Dependabot ungrouped, or majors only.**
4. **No automation:** update by hand when someone touches the site.

## Decision Outcome

**Chosen: option 1.**

The family configuration, read from `pm-skills/.github/dependabot.yml` on 2026-09-15, groups all patterns
per ecosystem, restricts grouped updates to `minor` and `patch`, runs weekly, and labels and prefixes
commits. Its `npm` block for `/site` is directly transposable; only the directory differs, and here it is
`/site` too under Pattern S.

**Option 2 is refused on actionability, not on safety.** `npm audit` reports against the whole dependency
tree, and for a static-site toolchain the large majority of that tree runs at build time on a CI runner,
not in a reader's browser. An advisory in a transitive build-time dependency typically cannot be actioned
except by waiting for an upstream release, so a gate on it blocks a docs deploy on something the
maintainer cannot fix.

**What is deliberately not claimed:** that the site has no client-side surface. Starlight ships browser
JavaScript, so the browser-facing surface is small but **not zero**, and this record does not pretend
otherwise. *(What that JavaScript consists of was not enumerated here, because it was not checked against
a built `dist/`; naming components on recollection is how a plausible sentence acquires a false detail.)*
The argument is about what a failing gate would be actionable on, not about an absence of risk. **Verified 2026-09-15:** `pm-skills` runs `npm ci`
in `deploy-pages.yml` and twice in `validation.yml` and runs no `npm audit` in either, nor in
`codeql.yml`; the one "audit" string in `validation.yml` refers to that project's own internal audit
findings.

**Option 3 is refused on volume.** Ungrouped weekly updates across a Starlight tree produce a pull request
per package. Majors-only inverts the risk: majors are the updates that need a human, and the routine
patches that keep a tree healthy are exactly what should be batched.

**Option 4 is refused** because it is the risk the plan already named, written down as a plan.

### Consequences

**Good.**

* Conformant by construction, like the rest of the site decision, rather than earning conformance later.
* Rot acquires a mechanism instead of an intention.
* **It fails safe.** The lockfile plus `npm ci` pin the build, so an unmerged Dependabot pull request
  never breaks anything. The cost of ignoring the stream is staleness, never a broken deploy.
* Majors, the updates that actually change behaviour, arrive separately and legibly.

**Bad, and stated plainly.**

* **A weekly pull-request stream in a repository that has never had one.** Unmerged, they accumulate, and
  a stack of stale dependency pull requests is its own rot - more visible, not less real.
* **Nothing forces anyone to look.** This buys notification, not maintenance. It would be easy to read the
  existence of this policy as having addressed dependency health; it has not.
* **Build-time advisories will be visible and unactioned by policy.** That is a defensible posture for a
  static docs site and it is still a posture, not a solution.

### Confirmation

The configuration lands with S0 and is confirmed by reading it against `pm-skills/.github/dependabot.yml`
at that time, since this record pins a pattern observed on 2026-09-15 rather than a version.

**Not verified, and not verifiable until the toolchain exists:** that grouped weekly updates produce
proportionate volume *here*. `pm-skills` is the evidence that they do there, on a tree this one does not
have yet. If the volume is wrong, the interval is the dial to turn - and per
[ADR 0011](0011-madr-v4-at-docs-internal-decisions.md), **changing the interval is a new record, not a
correction to this one**. Weekly to monthly is a change in the decision, not a factual error in it. This
record stays as what was believed on 2026-09-15.

## More Information

**The GitHub Actions gap is named here and not decided.** This repository pins action versions in
`ci.yml` and has no update policy for them either, while `pm-skills` covers `github-actions` weekly in the
same file. Extending Dependabot to that ecosystem is probably right and is **out of scope for a record
about the Node decision**; deciding it here would be scope the delegation did not cover. It is written
down so the next person sees it rather than rediscovering it.

**This record does not sequence the site against anything.** [ADR 0043](0043-the-usage-gate-becomes-advisory.md)
made the usage gate advisory and [ADR 0047](0047-the-usage-precondition-leaves-the-language-too.md)
removed the precondition from the language after it regrew as "a preference, not a prohibition". A third
copy was found in ADR 0046's More Information on 2026-09-15 and removed. The honesty rules in
`site-plan.md` section 13 are untouched and are a different thing: the site may be built whenever, and no
page it renders may call a bundle proven.
