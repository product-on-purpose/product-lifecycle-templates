---
status: accepted
date: 2026-06-29
decision-makers: [jprisant]
---

# Use product-lifecycle-templates as the name everywhere

## Context and Problem Statement

The design spec used the working name `pm-templates` and recommended keeping the `pm-` prefix for coherence with `pm-skills`, while the repo on disk was already named `product-lifecycle-templates`. Manifests, install commands, and READMEs need one identity before content accretes around it.

## Considered Options

* Option A: `product-lifecycle-templates` everywhere; drop the `pm-` family handle.
* Option B: `pm-templates`, matching the sibling naming family.

## Decision Outcome

Chosen option: A. The broader name ages better if the library outgrows pure product management into general software-lifecycle documents (the design spec's own section 15 anticipates this). Ecosystem coherence with pm-skills is carried by shared conventions and the `pairs_with` seam, not by a shared name prefix.

The name applies to: the git repo, the plugin and marketplace `name` fields, and the install string (`npx skills add product-on-purpose/product-lifecycle-templates`).

### Consequences

* Good: no rename cost later if scope broadens; identity settled before distribution surfaces exist.
* Accepted risk: the sibling relationship to pm-skills is less obvious from the name alone; mitigated by README positioning and the pairs_with metadata.

## More Information

Provenance: accepted (decided 2026-06-29; transcribed 2026-07-11 from strategy brief section 5; ratified 2026-07-12)
