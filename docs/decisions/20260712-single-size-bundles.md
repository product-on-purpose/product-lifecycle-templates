# The meta declares the size contract; single-size bundles are a legal shape

Status: accepted (decided 2026-07-12)
Date: 2026-07-12
Deciders: jprisant

## Context and problem statement

[20260629-variant-model.md](20260629-variant-model.md) settled that a type ships the number of variants it earns, and it left a loose end in its own consequences:

> Note for single-size types (seven Tier-1 types are S-only per the catalog): the machine-metadata spec proposes `sizes_available: [lean]` with the nesting check waived; record that refinement as its own decision when the first single-size bundle is built.

That moment arrived. Seven of the 27 Tier-1 catalog types are single-size, so the next bundles to build are likely to include one, and the gate could not pass it. Two checks hardcoded the assumption that every bundle ships exactly `lean` and `full`:

- **Check A (files)** required all eight canonical files, including both variants, so a single-size bundle failed with "missing: template-full.md".
- **Check C (nesting)** hard-failed when either variant was absent.

The naive fix is to relax both checks when a variant is missing. That is the wrong fix: it converts a real defect (a bundle that was supposed to ship two variants and only shipped one) into a silent pass. The gate would stop being able to tell "deliberately single-size" from "half-built".

## Considered options

* Option A: make `sizes_available` in the meta the size contract, and have the gate enforce that the files on disk match it exactly, in both directions.
* Option B: waive the nesting and file checks whenever a variant file is absent.
* Option C: require every type to ship two variants, padding out a `full` for single-size types.

## Decision outcome

Chosen option: **A. The meta is the contract.**

`sizes_available` is no longer a field the gate cross-checks as an afterthought. It is the declaration of what the bundle IS, and every structural check keys off it:

- **A (files):** the six core files, plus exactly one variant file per declared size. A declared variant that is missing fails. **A variant file present on disk that the meta never declared also fails.** That second direction is new, and it closes a hole nobody had noticed: a stale `template-full.md` could previously linger in a bundle whose meta said lean-only, and nothing would ever catch it.
- **C (nesting):** each variant must be an ordered subset of the next larger one (`lean` in `full`, or `s` in `m` in `l`). For a single-size bundle the rule is **vacuous, not waived**, and the gate says so out loud: "single-variant bundle {lean}; nesting rule not applicable". A green run that silently skipped a check would be a lie of omission.
- **F (meta):** `sizes_available` must exist, be non-empty, and use exactly one size vocabulary. `lean`/`full` and `s`/`m`/`l` are the two legal vocabularies and may not be mixed.

Option B was rejected because it makes the gate unable to distinguish intent from incompletion, which is the one thing a governance gate exists to do. Option C was rejected because it contradicts the variant-model decision directly: no empty third variant padded out of obligation, and by the same logic no empty second one.

### Consequences

* Good: a single-size bundle is now a **declared shape** rather than a hole in the checks. The gate reads the meta and enforces it.
* Good: the reverse direction (undeclared variant files) is now caught. This was a real gap, found while making this change rather than by a user.
* Good: three-weight (`s`/`m`/`l`) bundles are supported end to end, including transitive nesting (`s` in `m` in `l`), which the variant model always allowed but the gate never checked.
* **Consequence for the rulebook: a bundle is no longer always eight files.** It is six core files plus one per declared size. Two variants gives eight (the common case), one gives seven, three gives nine. The methodology is updated to state the rule rather than the common case, which is a better rule anyway: [20260630-research-log-as-8th-file.md](20260630-research-log-as-8th-file.md) established that the research log ships, and that remains true at every size.
* Accepted risk: `sizes_available` is now load-bearing. A bundle whose meta omits it fails the gate rather than being skipped, which is a deliberate behavior change. A contract you can silently omit is not a contract.
* Verified with six fixtures: single-size passes; `s`/`m`/`l` passes; an undeclared stray variant fails; a declared-but-missing variant fails; mixed vocabularies fail; a variant that does not nest fails. All four existing bundles still pass unchanged.
