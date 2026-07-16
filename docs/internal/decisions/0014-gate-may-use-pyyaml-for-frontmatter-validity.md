---
status: accepted
date: 2026-07-16
decision-makers: [jprisant, claude]
consulted: []
informed: []
---

# The gate may use PyYAML for one check (frontmatter validity); the other six stay pure stdlib

## Context and Problem Statement

On 2026-07-14 the ADR bundle shipped with invalid YAML in both template frontmatters: `decision-makers: [{{decision_makers}}]`, which YAML reads as a flow sequence containing a flow mapping with an unhashable key. **The gate passed it green.** It reads `sizes_available` with a regular expression and never parses YAML as YAML, so "the frontmatter is well-formed" was a Definition-of-Done clause with zero automation behind it. The defect was caught by a separate ad-hoc script, not the gate, and only because someone thought to run one.

[ADR 0008](0008-gate-python-local-interim.md) committed the gate to the **pure standard library**, explicitly as "a decided interim," so that anyone could run `python tools/check-bundles.py` with nothing installed. The Python standard library has no YAML parser. So closing this hole and honoring 0008's zero-install property are in direct tension, and the tension has to be resolved rather than fudged.

## Decision Drivers

- **The hole is real and was hit in practice**, not hypothetically. A governance gate that cannot tell valid YAML from invalid YAML is failing at its stated job.
- **Zero-install local running is a genuine value** from 0008: the gate should not require a virtualenv and a dependency file to run at all.
- **Since M0, CI is the enforcement point.** Branch protection requires the `gate` check to pass before merge, so "enforced in CI" now means "actually enforced," which was not true when 0008 was written and the gate had never run in CI.
- **A hand-rolled YAML validator is a trap.** YAML is famously large; a stdlib approximation would pass some invalid documents and reject some valid ones, trading a known gap for an unknown one.

## Considered Options

* **Option A:** Grant the gate exactly one dependency, PyYAML, used only by the new frontmatter-validity check. That check SKIPs with a clear message when PyYAML is absent; the other six checks stay pure stdlib and always run. CI installs PyYAML, so the check is enforced there.
* **Option B:** Hand-roll a minimal YAML validator in the standard library, covering the subset of YAML the bundles use.
* **Option C:** Make PyYAML a hard dependency of the whole gate: import it at the top, and let the entire script fail to run if it is missing.
* **Option D:** Do nothing. Leave frontmatter validity to human review, as it was.

## Decision Outcome

Chosen option: **A. One dependency, one check, graceful skip.**

The new check (G) tries to `import yaml`. If it succeeds, it parses the `meta.yaml` and every template and example frontmatter block, and fails the build on any that do not parse, which forces placeholders to be quoted (`"{{title}}"`) - exactly the discipline that would have prevented the original bug. If the import fails, G returns a distinct **SKIP** state (not a pass): the run prints `SKIP  G yaml  SKIPPED: PyYAML not installed ...` and the other six checks proceed. CI runs `pip install pyyaml`, so G is enforced on every push and pull request.

This is the smallest move that closes the hole. It treats 0008's "pure stdlib" as the default rather than an absolute, which is what "a decided interim" always meant, and it confines the dependency to the one check that genuinely cannot be done without it.

Option B was rejected because a partial YAML parser is a liability dressed as thrift: it would give confident wrong answers, which is worse than the honest gap it replaces. Option C was rejected because it sacrifices the whole gate's zero-install property to enforce a single check, punishing the five checks that never needed a dependency. Option D was rejected because the hole was demonstrated, not theorized.

### Consequences

* Good: the frontmatter-validity hole is closed, and closed by a real parser rather than a regex approximation. Reproduced and verified: reintroducing `decision-makers: [{{decision_makers}}]` now fails check G with `invalid YAML in adr_template-lean.md`.
* Good: 0008's zero-install promise survives for the six stdlib checks. A contributor with a bare Python can still run the gate and get six of seven checks; the seventh announces itself as skipped rather than lying about having passed.
* Good: the **SKIP** state is a permanent, honest addition to the gate's vocabulary. A check that could not run now says so, instead of being silently counted as a pass, which is the same lie-of-omission the nesting check was written to avoid ([0010](0010-meta-declares-size-contract.md)).
* Bad: **local and CI can now disagree.** A contributor without PyYAML sees G skip; CI enforces it. A bundle with bad frontmatter passes locally and fails in CI. This is a real footgun, mitigated by the explicit SKIP message (which tells you the check did not run and how to run it) and by branch protection catching it before merge. It is accepted because the alternative, Option C, breaks the far more common zero-install path to protect against the rarer disagreement.
* Bad: the "pure stdlib gate" is now "pure stdlib except one check," a claim with an asterisk. The asterisk is documented in the script header, in the gate's own output, and here, so it is honest, but 0008's clean line has a notch in it now.
* Accepted cost: `pip install pyyaml` is one more line in CI and one more thing a thorough local contributor installs. PyYAML is ubiquitous, pure-ish, and stable, so as dependencies go it is close to the cheapest one available.

### Confirmation

Enforced by CI: `.github/workflows/ci.yml` runs `pip install pyyaml` and then `python tools/check-bundles.py`, and branch protection on `main` requires the resulting `gate` check to pass before any merge. Check G is the fitness function for this decision.

Verified at authoring time, three ways: G passes on all five existing bundles with PyYAML present (`4 YAML block(s) parse` each); reintroducing the original invalid-YAML line makes G fail with a located message and a non-zero exit; and simulating an absent PyYAML makes G return SKIP with the install hint while the other six checks still run.

## More Information

Amends [0008](0008-gate-python-local-interim.md) rather than superseding it: the gate is still a local Python script, still runs in CI, and is still overwhelmingly standard library. What changed is that "pure stdlib" is now the default for six checks rather than an absolute for all of them. 0008's own framing ("a decided interim") anticipated exactly this kind of narrow evolution.

This closes the **YAML half** of the WP-11 gate-hardening item recorded in `STATE.md`. The harder half, **citation-tracing** (having the gate verify that a companion's claims match their cited sources, the failure mode that produced ~15 defects in the ADR bundle across three review rounds), is not addressed here and remains open. It is a materially harder problem: check E already confirms that inline citations *resolve* to anchors, but nothing checks that the anchored source *supports the claim*, and that may not be mechanically decidable at all. Tracked as the open remainder of WP-11.
