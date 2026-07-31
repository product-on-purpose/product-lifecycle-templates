---
status: proposed
date: 2026-07-30
decision-makers: [jprisant]
consulted: [claude]
---

# This library templates Markdown documents, and says which catalog types it will not

## Context and Problem Statement

Two of the 27 Tier-1 "must-have" types are **not documents**. `wireframe` (catalog 52) is "layout blocks,
content hierarchy, navigation"; `interactive-prototype` (catalog 54) is "flows, interactions, states,
transitions". A Markdown template library cannot produce either artifact.

The build-out plan proposed shipping each as "a *specification wrapper* around the artifact, not the pixels."
That is untested, and for `wireframe` especially it risks inventing a document type nobody writes in order to
fill a catalog slot, which is the failure the README explicitly disavows: *"Coverage is not the product."*

**The deeper problem is that this library has never written down what it is willing to template.** Two claims
got silently merged during the floor build-out:

1. **Product organisations need wireframes.** True, and the catalog is right to list them.
2. **This library must ship a wireframe template.** Does not follow.

[ADR 0021 (complete the Tier-1 floor)](0021-complete-the-tier-1-floor.md) justified the floor as "the
catalog's own `must_have` baseline", and the catalog defines that baseline as types that "cover ~80% of
organizations". That is a claim about **what teams need**, not about **what this repository can produce**. The
catalog holds 205 types and more visual, executable and tabular ones sit in Tier 2 and Tier 3, so this
question recurs until it is answered once.

## Decision Drivers

* **Honesty over coverage.** A floor reported as 27 of 27 where two entries are inventions is worth less than
  25 of 27 with two exclusions named.
* **The library already ships wrappers, and they work when the wrapper is a real document.** `kpi-dashboard`
  states in its own honest core that it is a dashboard **definition**, not a live BI tool. Nobody considers
  that dishonest, because a dashboard definition is a document teams genuinely write.
* **An admission test already exists.** [ADR 0028 (the format-axis rule)](0028-adopt-a-format-axis.md) admits
  a *format* only when it is in circulation with a named source. Generalising that from formats to **types**
  is consistent rather than novel, and it is the same test that rejected V2MOM and the timeline roadmap.
* **The catalog's claim should not be edited to make our number look better.** Orgs really do need
  wireframes.

## Considered Options

* **A. Build both as specification wrappers**, per the existing spec sketch. Floor reaches 27 of 27.
* **B. Reclassify both out of Tier 1**, amending the catalog's `must_have` baseline. Floor becomes 25 of 25.
* **C. State the library's templating scope, leave the catalog alone, report the floor as 25 of 27
  templatable with two exclusions named.** Chosen.
* **D. Ship nothing and say nothing.** Leave the two rows "planned" indefinitely.

## Decision Outcome

**Chosen: option C**, with one addition.

**The scope rule.** This library templates artifacts whose primary form is a **written document**. An
artifact whose primary form is **visual, executable, or a live data surface** is out of scope for templating,
and is named as such with its reason rather than left silently unbuilt.

**The admission test, generalised from ADR 0028.** A candidate type is templatable when a named source
publishes it **as a written document**. Where a *wrapper* around a non-document artifact is proposed, the
wrapper must clear the same bar in its own right: not "could someone write this", but "does someone".

**Applied now:**

| Catalog type | Outcome |
|---|---|
| **52, Wireframe** | **Out of scope.** The artifact is visual. No named source publishes a "wireframe specification" as a written document; designers annotate inside the design tool. The adjacent documents that *do* exist are a design brief and a UX spec, which are different types |
| **54, Interactive Prototype** | **Out of scope as an artifact.** But the work it commissions is real, and see below |

**The addition: `prototype-brief` is added as a new type.** Not a wrapper describing a prototype after the
fact, which is the weak version, but a **brief written before it exists that commissions the work** and tells
an engineer or an agent what to build, for whom, and what it must let a user do. That is a forward-looking
document with a real readership, and it is the artifact the catalog's own note points at when it records
Cagan's position that the prototype is "the majority of the spec".

It joins **`discovery-docs`**, not a new `design-docs` family. Families here are defined by what a document
**does**, and this one commissions and validates rather than designs; the catalog's own entry categorises the
prototype as "design/**validation**". `design-docs` is therefore never created.

**One test ships with it, in the guide's "when NOT to use" section:** *is the filled brief valuable to a human
builder who has never heard of an LLM?* If yes, it is a document and belongs here. If it is only useful pasted
into an agent, it is a prompt, and prompts belong in the skills library.

### Consequences

* Good, because the floor becomes reportable honestly: **25 of 27 templatable**, 18 built, 2 named and
  excluded with reasons. No number is inflated by an invention.
* Good, because the question is answered **once** for the 205-type catalog rather than per awkward type.
* Good, because `design-docs` is never created, reducing the remaining work to **four family contracts**.

**Two numbers, and they are not the same number.** Conflating them is the arithmetic defect this library has
now caught three times, so they are separated here:

| Metric | Value | What it counts |
|---|---|---|
| **The catalog floor** | **18 of 25** | Original Tier-1 `must_have` types this library will template. 27 named, 2 excluded here, 18 built, **7 of the original set remain** |
| **The build backlog** | **8 bundles** | What actually has to be authored: those 7, **plus `prototype-brief`**, which is a new type and is not one of the 27 |

The floor completes at 25 of 25. The backlog completes at 8. Reporting either number alone misstates the
other.
* Good, because the wrapper pattern is now bounded rather than open: `kpi-dashboard` is legitimate under the
  stated test, and a hypothetical "wireframe specification" is not.
* Bad, because two Tier-1 rows stay visibly unfilled forever. That is the intended cost of the honesty claim,
  and it is what the README's "real fills: 0 (honest)" badge already commits to in a different register.
* Neutral, because the catalog is unchanged on its own terms. Entries 52 and 54 keep their Tier-1
  `must_have` status, and gain a note that this library does not template them.
* Neutral, because `prototype-brief` is a new type rather than a catalog entry, and is added to the catalog
  with its own row rather than by repurposing entry 54. **Renaming entry 54 would be the exact defect this
  library rejects elsewhere**: presenting artifact Y under type X's name, which is why V2MOM was excluded.

### Confirmation

These are the criteria this decision is checked against, not a claim that they are already satisfied.

**Applied in the change that proposes this record**, so that no surface disagrees with another while the
record is pending:

* `docs/internal/catalog.md` entries 52 and 54 carry a dated out-of-scope note naming this record.
* `atlas/catalog-data.json` carries the same, and `gen-atlas.py --check` passes.
* `README.md` and `STATE.md` report the floor as **18 of 25 templatable**, never as a bare fraction that
  implies 27 is reachable, and STATE.md states that this record is `proposed` rather than describing every
  decision record as accepted.
* `docs/internal/buildout-specs.md`'s progress table marks rows 22 and 23 **out of scope**, not "planned",
  and carries a `prototype-brief` row under `discovery-docs`.
* No `design-docs` contract exists.

**Deferred to acceptance, deliberately:**

* **A catalog entry for `prototype-brief`.** The catalog currently asserts **205 types across 30 places in
  the repository**, and adding a 206th cascades to all of them. That churn should follow a ratified decision,
  not a proposed one. Until it lands, `prototype-brief` exists in the build plan and in the `discovery-docs`
  contract but **not** in the catalog, and that gap is stated here rather than left for a reader to notice.

## More Information

Generalises the admission logic of [ADR 0028 (the format-axis rule)](0028-adopt-a-format-axis.md) from
formats to types. Amends the scope of [ADR 0021 (complete the Tier-1 floor)](0021-complete-the-tier-1-floor.md)
by making explicit that its baseline is the catalog's claim about organisations, not a commitment that every
row is templatable. Does not amend [ADR 0023 (the Tier-1 family taxonomy)](0023-resolve-the-tier-1-family-taxonomy.md)
except by removing `design-docs`, which that record listed provisionally and which now has no members.

The procedure this record follows when a catalog call meets contrary evidence is written down in
[`decision-procedures.md`](../decision-procedures.md) section 1.
