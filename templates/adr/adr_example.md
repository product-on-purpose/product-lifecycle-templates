---
status: accepted
date: "2026-07-12"
decision-makers: [jprisant, claude]
consulted: []
informed: []
doc_type: adr
size: full
source_template: adr
source_template_version: 0.1.0
---

# The meta declares the size contract; single-size bundles are a legal shape

## Context and Problem Statement

An earlier decision, ADR 0002 (the variant model), settled that a document type ships the number of
size variants it earns rather than a fixed two, and it left a loose end sitting in its own
consequences: a note that single-size types would need `sizes_available: [lean]` with the nesting
check waived, and that the refinement should be recorded as its own decision when the first
single-size bundle was actually built.

That moment arrived. Seven of the 27 Tier-1 types in the master catalog are single-size, so the next
bundle we build is likely to be one, and the governance gate cannot pass it. Two of its checks
hardcode the assumption that every bundle ships exactly `lean` and `full`:

- **Check A (files)** requires all eight canonical files, including both variant files, so a
  single-size bundle fails with `missing: template-full.md`.
- **Check C (nesting)** hard-fails when either variant file is absent, because it has nothing to
  compare.

The obvious fix is to relax both checks whenever a variant file is missing. That fix is wrong, and
seeing why is the whole decision: it silently converts a real defect (a bundle that was *supposed* to
ship two variants and only shipped one) into a passing run. The gate would lose the ability to tell
"deliberately single-size" apart from "half-built," which is the one thing a governance gate exists
to do.

This decision binds `tools/check-bundles.py` and the `sizes_available` field in every bundle's
`<type>_meta.yaml`.

## Decision Drivers

* **The gate must distinguish intent from incompletion.** This is the knockout criterion. Any option
  that leaves a half-built bundle passing green is out, regardless of its other merits.
* **No empty variant padded out of obligation.** ADR 0002 (the variant model) settled this, and a
  fix that contradicts a standing decision is not a fix.
* **Drift must be catchable in both directions.** A missing declared file and an undeclared present
  file are both forms of the bundle disagreeing with itself.
* **The gate stays pure standard library.** ADR 0008 (gate as a local Python script) committed to no
  third-party dependencies, so no option may require a YAML parser.

## Considered Options

* **Option A:** Make `sizes_available` the size contract, and have the gate enforce the files on disk
  against it exactly, in both directions.
* **Option B:** Waive the nesting and file checks whenever a variant file is absent.
* **Option C:** Require every type to ship two variants, padding out a `full` for single-size types.

## Decision Outcome

Chosen option: **"Make `sizes_available` the size contract"**, because it is the only option that
satisfies the knockout driver. The gate can distinguish a deliberately single-size bundle from a
half-built one for the simplest possible reason: the bundle now *says* which it is, and the gate
holds it to its word.

`sizes_available` stops being a field the gate cross-checks as an afterthought. It becomes the
declaration of what the bundle **is**, and every structural check keys off it:

- **A (files):** the six core files, plus exactly one variant file per declared size. A declared
  variant that is missing fails. A variant file present on disk that the meta never declared **also**
  fails.
- **C (nesting):** each variant must be an ordered subset of the next larger one (`lean` in `full`,
  or `s` in `m` in `l`). For a single-size bundle the rule is **vacuous, not waived**, and the gate
  says so out loud: `single-variant bundle {lean}; nesting rule not applicable`.
- **F (meta):** `sizes_available` must exist, be non-empty, and use exactly one size vocabulary.
  `lean`/`full` and `s`/`m`/`l` are the two legal vocabularies and may not be mixed.

### Consequences

* Good, because a single-size bundle is now a **declared shape** rather than a hole in the checks.
* Good, because the reverse direction is now caught. A stale `template-full.md` could previously
  linger in a bundle whose meta said lean-only and nothing would ever notice. This was a real gap,
  and it was found by making this change rather than by a user.
* Good, because three-weight (`s`/`m`/`l`) bundles are now supported end to end, including transitive
  nesting, which the variant model always permitted but the gate never checked.
* Bad, because **`sizes_available` is now load-bearing**. A bundle whose meta omits it fails the gate
  rather than being skipped. That is a deliberate behavior change and it will break any bundle
  authored before this record. A contract you can silently omit is not a contract, so the cost is
  accepted.
* Bad, because the gate now **parses YAML with a regular expression**. The pure-stdlib driver forbids
  a YAML dependency, so `sizes_available` is read with a pattern that handles an inline list and a
  block list and would mis-read an exotic-but-legal YAML construction. This is a real fragility in
  the option we chose, and the honest mitigation is that it is confined to one function
  (`parse_sizes`) and would be replaced the moment the gate is allowed a dependency.
* Consequence for the rulebook: **a bundle is no longer always eight files.** It is six core files
  plus one per declared size. Two variants gives eight (the common case), one gives seven, three
  gives nine. The methodology now states the rule rather than the common case, which is a better rule
  anyway.

### Confirmation

Enforced automatically, on every push to `main` and every pull request, by
`.github/workflows/ci.yml`, which runs `tools/check-bundles.py`. Checks A, C, and F above are the
fitness function, and a violation fails the build rather than producing a warning.

Verified at the time of the change against six purpose-built fixtures, each asserting a distinct
failure mode rather than only the happy path:

| Fixture | Shape | Expected |
|---|---|---|
| `aa-single` | declares `[lean]`, ships one variant | pass |
| `bb-sml` | declares `[s, m, l]`, nests transitively | pass |
| `cc-stray` | declares `[lean]`, but a `template-full.md` sits on disk | fail |
| `dd-missing` | declares `[lean, full]`, ships only `lean` | fail |
| `ee-mixed` | declares `[lean, m]`, mixing vocabularies | fail |
| `ff-badnest` | `lean` sections are not an ordered subset of `full` | fail |

All four bundles existing at the time continued to pass unchanged, which is the regression evidence
that the contract was tightened without moving the goalposts under work already done.

## Pros and Cons of the Options

### Make `sizes_available` the size contract

* Good, because the gate can finally distinguish intent from incompletion. This is the knockout
  driver, and this is the only option that clears it.
* Good, because it catches undeclared stray files, a direction of drift no option else even
  considered.
* Good, because it generalizes: a `s`/`m`/`l` bundle needs no further gate work.
* Bad, because it makes a metadata field load-bearing, so a meta typo becomes a build failure.
* Bad, because it forces regex-parsing of YAML under the pure-stdlib constraint (see Consequences).

### Waive the checks whenever a variant file is absent

* Good, because it is a three-line change and ships in ten minutes.
* Bad, because it **fails the knockout driver outright**: a half-built bundle and a deliberately
  single-size bundle become indistinguishable, both passing green. Rejected on this ground alone,
  and no other merit could have rescued it.
* Bad, because it makes the gate quieter over time. Every future variant mistake would pass in
  silence, and a gate that cannot fail is decoration.

### Require every type to ship two variants

* Good, because it keeps the gate's existing logic completely untouched.
* Bad, because it directly contradicts ADR 0002 (the variant model), which settled that a type ships
  the variants it earns. Re-litigating a standing decision to avoid changing a script is the tail
  wagging the dog.
* Bad, because a padded `full` variant that duplicates its `lean` is a lie told to a linter. It
  would teach every future author that the way past the gate is to produce a file nobody needs.

## More Information

Refines **ADR 0002 (the variant model)**, which flagged this exact loose end in its own consequences
and deferred it to the first single-size bundle. Constrained by **ADR 0008 (gate as a local Python
script)**, whose no-dependencies rule is directly responsible for the regex-parsing cost accepted
above.

Revisit if either of two things becomes true: a third size vocabulary is proposed (the current design
hardcodes two), or the gate is permitted a third-party dependency, at which point `parse_sizes`
should be replaced with a real YAML parse and the second "Bad" consequence disappears.
