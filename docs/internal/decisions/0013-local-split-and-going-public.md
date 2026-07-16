---
status: accepted
date: 2026-07-14
decision-makers: [jprisant, claude]
consulted: []
informed: []
---

# Split `_local/`: promote what public docs cite into `docs/internal/`, untrack the rest, and go public

## Context and Problem Statement

The governance gate has **never run**. Not once. `.github/workflows/ci.yml` is correct, Actions are enabled, and the gate passes locally on all five bundles, but every run since 2026-07-13 dies in 3-4 seconds with the `gate` job executing **zero steps**. That is a job that never got a runner: the repository is private and out of Actions minutes. `pm-skills`, public in the same organization, runs its CI normally.

So the library's central claim, "enforceable, not aspirational," was false in the only place enforcement counts. Worse, `STATE.md` had been asserting that the gate "**Runs in CI** on every push to `main` and every pull request. Passing." The one file whose entire reason for existing is audit finding G-01, *a plan that lies about the tree is worse than no plan*, had started lying about the tree.

Making the repository public makes Actions free and unlimited, and fixes this permanently. But it could not be done safely, because `.gitignore` **force-included** `_local/` (`!_local/`, `!_local/**`), putting 39 files under version control that were written on the assumption nobody outside would read them. Going public would have published all of them.

The obvious fix, "just gitignore `_local/`," was also wrong, and this is the part that made the decision interesting. `_local/` was not a private annex. The public product had grown roots into it:

- **The master catalog** (`_local/initial-discovery/docs/deep-research_master-catalog.md`) is cited by `templates/methodology.md` **and by all four existing bundle companions.**
- **`README.md`**, the front door, links to four documents inside `_local/initial-discovery/docs/`.
- **`STATE.md`** links into the audit corpus for the roadmap and the family contract.

Untracking `_local/` wholesale would have deleted the master catalog from the repository and left ten broken links across the README, the methodology, and every companion. The boundary was in the wrong place, and nobody had noticed because everything was private, so every link resolved on the maintainer's disk.

## Decision Drivers

* **CI must actually run.** This is the knockout criterion. An unenforced gate is a decoration, and the library's positioning depends on it being real.
* **Nothing that is written for a private audience may become public by accident.** Irreversible, and irreversible in the bad direction.
* **No tracked file may link into an untracked directory.** Such a link resolves for exactly one person on earth and 404s for everyone else.
* **The public product must remain whole.** An option that publishes a README with four dead links, or companions citing a catalog that is not in the repo, is not a real option.

## Considered Options

* **Option A:** Split. Promote the material public docs actually cite into `docs/internal/`, untrack the remainder of `_local/`, then go public.
* **Option B:** Go public with `_local/` exactly as it is. Zero work, zero breakage.
* **Option C:** Stay private and pay for Actions minutes (or wait for the monthly reset).
* **Option D:** Untrack `_local/` wholesale and go public.

## Decision Outcome

Chosen option: **A, split it.**

Ten files are promoted into `docs/internal/`: the eight under `initial-discovery/` (the master catalog, the implementation plan, both strategy briefs, the design spec, the layered design, the architecture diagram, and the research prompt), plus the two artifacts inside the audit corpus that `STATE.md` depends on (the expanded roadmap, and the `delivery-docs` family contract). Those last two were promoted rather than left behind because both are **living documents that had been frozen inside a dated audit package**, which was the wrong home for them regardless of this decision.

The remaining 29 files stay on disk and leave git: the audit corpus, the session logs, and the working overview.

**Option D is the trap, and it is worth naming, because it is what "keep `_local/` gitignored" sounds like it means.** It would have removed the master catalog, which five tracked files cite, and broken ten links across the public surface. The instruction was right in spirit and would have been destructive taken literally. What the boundary needed was not enforcement but *relocation*.

Option B fails the second driver outright. Option C is the only option with no irreversible step, and it was seriously considered on that basis, but it pays money to preserve a state the project does not want: a template library nobody can use, whose gate is enforced by memory.

**A specific hazard settled the audit's fate.** The audit's `adoption-kit/` contains a competing `STATE.md` and **eight superseded decision records in the bespoke pre-MADR format** that [0011](0011-madr-v4-at-docs-internal-decisions.md) replaced. Publishing that directory would have put a second source of truth and a set of stale ADRs, in the exact format the organization forbids, into a public repository. The audit stays out of git for reasons far stronger than tidiness.

### Consequences

* Good: CI runs, for free, permanently. The gate becomes enforcement rather than a local habit.
* Good: the boundary is now real and load-bearing rather than nominal. `_local/` finally means what its name says, and the `.gitignore` states the rule so it does not have to be rediscovered: **anything under `_local/` that a tracked file needs must be promoted, never linked across the boundary.**
* Good: the roadmap and the family contract escape the dated audit package and reach canonical, maintainable addresses.
* Bad: **the master catalog is now public, and it contains errors.** Finding EC-2 established that its size call for the ADR is wrong, and by extension that its other 26 Tier-1 size calls are unverified hypotheses. Publishing a document while knowing it contains at least one error is a real cost. It is accepted because the alternative was worse (the companions cite it, so a private catalog means broken citations in the public product), and because `STATE.md` now says plainly that the catalog's size calls are hypotheses. A public document with a published caveat beats a private document with a hidden defect.
* Bad: history is now partly unreachable. The audit's findings are cited by `STATE.md`'s own framing (D-01, D-04, G-01, EC-*) and by several decision records, but a reader outside the maintainer's machine cannot follow those citations to their source. This is the price of keeping the adoption-kit out, and it is not free: it makes several claims in this repo unverifiable by outsiders.
* Accepted risk: **going public is irreversible in practice.** Anything published can be assumed cached, forked, or indexed.

### Correction, 2026-07-14 (same day, before going public)

The consequence above originally read, in part:

> The 29 untracked files were never pushed, so they were never exposed.

**That is false, and it was the single most load-bearing sentence in this record.** It was written from the state of the working tree rather than the state of the remote, and it is wrong twice over:

1. **The files were pushed.** `_local/` has been tracked and pushed since commit `cd7c6bd` (HY-1, version-controlling the working library). The remote's default branch **still contains `_local/_session-logs/` right now.** Untracking at the tip of a feature branch protects nothing until that branch merges.
2. **Merging does not fix it either.** Making a repository public exposes its **entire history**, not just its tip. Every commit that ever tracked `_local/` remains reachable, so the audit corpus and the session logs would be readable by anyone willing to run `git log`.

So the boundary this decision establishes is real going forward, and it does **nothing** retroactively. Deleting a file from the tip is not deletion; it is a rename to somewhere less obvious.

The error is corrected rather than superseded, per [0011](0011-madr-v4-at-docs-internal-decisions.md): the *decision* (split `_local/`, promote what public docs cite, go public) has not changed. What was wrong was a claim of fact about exposure, and a record that silently rewrote it would hide the most useful thing here, which is that **the check that caught it was mechanical.** The claim was written from the working tree; one query against the remote falsified it. The lesson is the same one this repo learned about citations three hours earlier, in a different costume: *a statement about a system is not verified by the confidence of the person writing it.*

**This correction blocks the decision's Confirmation.** Going public is now gated on a further choice, which belongs to the maintainer and is recorded as **PB-1** in `STATE.md`: accept the history exposure, or purge `_local/` from history with a rewrite before flipping visibility. This record does not decide it.

### Confirmation

Enforced by a **repo-wide link check**, which is added to CI as part of this change and which fails the build on any tracked file linking into `_local/` or at any dead relative path. That check is the fitness function for the central rule of this decision, and it exists specifically because the last relocation (HY-2, decision [0009](0009-scaffold-graduation-flat-templates.md)) broke four companion links and the gate did not notice, because the gate does not check links.

Verified at the time of the change: 10 links rewritten by computing each relative path from the file that contains it rather than by hand; every tracked `_local/` reference either repointed or confirmed to be deliberate historical prose (decision 0009's account of the move *out of* `_local/` is correct and is left alone); the gate green on all five bundles.

The remaining, and honest, gap: **this decision's success condition is "CI is green on `main`," and that cannot be confirmed from inside this record.** It requires a human to flip the repository to public. Until that happens, this ADR is accepted and unconfirmed, and `STATE.md` says so.

## More Information

Completes what [0009](0009-scaffold-graduation-flat-templates.md) (scaffold graduation) started. That decision moved the *templates* out of `_local/` and explicitly accepted, in its own consequences, that "historical documents now cite paths that no longer exist." This record pays that bill: the documents in question turned out to include the README, the methodology, and every companion in the library, and the boundary they were reaching across was the one thing standing between the repo and working CI.

Depends on [0011](0011-madr-v4-at-docs-internal-decisions.md) for the reason the audit's adoption-kit must not be published.

Revisit if the repository ever returns to private (the force-include would need re-examining, not restoring), or if the audit corpus is ever needed publicly, in which case it should be promoted **selectively** and its adoption-kit left behind, never wholesale.
