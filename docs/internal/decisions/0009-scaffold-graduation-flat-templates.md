---
status: accepted
date: 2026-07-12
decision-makers: [jprisant, claude]
---

# Graduate the library out of `_local/` to a flat `templates/` scaffold

## Context and Problem Statement

The library was built under `_local/templates/`, an admittedly provisional address. The repo's `.gitignore` carries a comment explaining the arrangement: the user's global ignore rule hides `_LOCAL/` everywhere, and this repo deliberately re-includes it so the work could be version-controlled while the final scaffold stayed an open question (decision HY-2, scaffold graduation, open since 2026-07-02).

The question was deferred on purpose and for a good reason: because lifecycle phase is carried in metadata and never in the path ([0005-bundle-ids-doctype-spine.md](0005-bundle-ids-doctype-spine.md)), the directory layout is a derivable, late-binding choice rather than a load-bearing one. Nothing depended on answering it early.

Two things forced it on 2026-07-12. The repository is going public, and `_local/` is a name that reads as "working scratch, not for you" to every visitor: publishing the product at that path would misdescribe it. And CI cannot run on a private repo without Actions minutes, so going public is also what makes the M0 (credibility floor) exit act reachable at all.

## Considered Options

* Option A: flat `templates/<doctype>/` at the repo root, with `tools/` and `atlas/` alongside. `_local/` retains only genuinely internal material.
* Option B: nested by phase, `templates/<phase>/<doctype>/`.
* Option C: leave everything under `_local/` and publish it as-is.

## Decision Outcome

Chosen option: **A**.

Option B is precluded by a decision already taken: phase lives in metadata, never in the path. Materializing phase into the directory tree would re-introduce the exact second lens that [0005-bundle-ids-doctype-spine.md](0005-bundle-ids-doctype-spine.md) rejected, and would force renames whenever a type's phase assignment is refined. Option C publishes the product at an address that tells every reader it is not the product.

The final layout:

```
templates/          the library itself (methodology + one folder per document type)
tools/              the governance gate (check-bundles.py)
atlas/              the 205-type interactive catalog map
docs/internal/decisions/     these records
_local/             internal working material, not part of the product
```

The gate needed **no code change**: it resolves `TEMPLATES_DIR` relative to its own file (`SCRIPT_DIR/../templates`), so moving `_local/tools/` to `tools/` and `_local/templates/` to `templates/` preserved the relationship exactly. That is a small vindication of resolving paths relative to the script rather than the working directory.

### Consequences

* Good: the product lives at an address that describes it. A visitor cloning the repo finds `templates/` where they would look for it, which is what the credibility floor was for.
* Good: `_local/` finally means what its name says. The boundary between "the library" and "how the library got built" is now a directory boundary rather than a convention held in one person's head.
* Good: HY-2 closes after 10 days open.
* Accepted risk: **historical documents now cite paths that no longer exist.** The audit package, the session logs, and the implementation plan all reference `_local/templates/...`. These were **deliberately not rewritten.** The 2026-07-10 audit was performed against `_local/templates/` at commit `737354e`; editing its text to say `templates/` would falsify a record of what was true when it was written. A historical document that describes a moved file is accurate about the past. A historical document edited to describe the present is a forgery. Only live, forward-looking documents (README, STATE.md, the methodology, the gate, the two ADRs that cite the gate and the `_working/` folder) were rewritten.
* Follow-on: the family contract still needs adopting at `templates/_families/` or similar (roadmap WP-24). This decision does not settle where family-level artifacts live, only where bundles do.

## More Information

Provenance: accepted (decided 2026-07-12)
