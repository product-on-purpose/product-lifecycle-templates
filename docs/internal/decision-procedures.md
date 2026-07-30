# Decision procedures

**What to do when a recurring judgment call comes up, so it is decided the same way twice.**

This file is not an ADR. An ADR records **what was decided**; this records **how to decide** a class of
question that keeps arriving. Every procedure below is drawn from something that actually happened in this
repository, and each one names the precedent so a reader can check that the rule was earned rather than
invented.

**Why it exists.** Each of these was resolved correctly at least twice, and each time the reasoning lived
only in a commit message, a STATE.md finding, or a session log. That makes the pattern discoverable only by
reading history, which means it is rediscovered rather than applied, and rediscovery is where it gets decided
differently the third time.

Add to this file when a judgment call resolves the same way twice. Delete from it when a procedure is
superseded by a real ADR or a gate check.

---

## 1. A catalog call loses to research

**Do:** correct the catalog entry **in place, with a dated note** saying what it used to claim, what the
research found, and where. Correct every copy: `docs/internal/catalog.md`, `atlas/catalog-data.json`, and any
spec sheet that repeats it. Regenerate the atlas.

**Do not** silently edit it, and do not leave the bundle contradicting the catalog while deferring.

**Why:** the catalog was produced by one research pass and has never been verified type by type. Its own
header says the size calls are hypotheses; the same is true of its other calls. A bundle's research is the
first time any entry meets primary sources.

**Precedent:** entry 64 (ADR), whose "S only" size call did not survive and was corrected 2026-07-16 as
finding **EC-2**. Entry 6 (OKRs), which listed V2MOM as "Salesforce's named variant" and was corrected
2026-07-30 when Salesforce's own training material turned out never to mention OKRs.

## 2. A new check flags work that already shipped

**Do:** grandfather the existing failures **by name, with a measured count and a stated reason**, as a
ceiling that may only shrink. Print the list on every run. Fail the build if a listed count rises or an
unlisted subject fails. Delete entries as they are fixed, and delete the mechanism when the map empties.

**Do not** make the check report-only, and do not lower the threshold until the tree passes.

**Why:** a report-only gate on a large failure count gets ignored, and a loosened threshold silently
redefines the defect as acceptable. Grandfathering keeps the check blocking for new work, which is what it
exists for, while the backlog stays loud instead of decaying into a silent pass.

**Precedent:** `tools/check-research-logs.py`, whose `EXEMPT` map names six table-layout logs with the
measured reason and date (finding **DF-4**). `tools/check-example-independence.py`, whose `GRANDFATHERED` map
names sixteen bundles with per-bundle ceilings totalling 132 copied passages (finding **DF-6**).

## 3. A review finding does not survive verification

**Do:** reject it, and record the rejection **with its reason** in STATE.md's "Open by choice, not by
oversight" section. Name what was checked and what was found.

**Do not** apply it to be safe, and do not drop it silently.

**Why:** an unrecorded rejection gets re-raised by the next reviewer, and the verification work is done
twice. A recorded one turns a disagreement into a documented position.

**Precedent:** the `bug-report` rubric-threshold finding, rejected 2026-07-25 as family-wide house style
rather than a bundle defect. Codex's reading of `buildout-specs.md` as self-contradictory, rejected
2026-07-29 because the line above it explicitly resolves the markers below.

## 4. A review finding is right and its proposed fix is wrong

**Do:** verify the **fix** against the source, not only the finding. Apply the fix the evidence supports,
which is often not the one proposed.

**Why:** a reviewer that correctly spots an unsupported claim will often propose a substitute that is equally
unsupported, because it is reasoning from the same incomplete picture.

**Precedent:** a lens correctly found Perri cited for a claim her logged entries do not carry, and proposed
substituting her other entry, which does not carry it either; the correct fix was removal. A lens correctly
found a Roger Martin quote absent from its log entry and proposed de-quoting it; re-fetching showed the quote
was verbatim on the page and **the log** was the thing at fault.

## 5. An unwritten rule is being applied

**Do:** state the rule in the artifact that applies it, name the decision record that owns the rule, and
route the resolution there.

**Do not** apply it silently, and do not unilaterally amend the owning ADR from inside a bundle change.

**Why:** an unwritten criterion applied twice becomes precedent without ever being ratified, and a
27-type commitment should not be settled inside a change that ships one bundle.

**Precedent:** [ADR 0028 (the format-axis rule)](decisions/0028-adopt-a-format-axis.md) requires a format to
be "in circulation with a named source" and does not say *as what*. Two bundles used the strict reading
(`product-roadmap` rejecting the opportunity solution tree, `okrs` rejecting V2MOM) while `product-vision`
was admitted under the loose one. Both bundles state the ambiguity and route it to decision D-E.

## 6. A count in prose disagrees with the tree

**Do:** re-read the whole document and fix every sentence the change touched, then update the marker.

**Do not** edit the marker alone. `tools/check-counts.py` says this in its own failure message because
editing the marker recreates the defect with extra steps.

**Why:** a marker is one number and a document is many claims. Landing one bundle required twelve prose edits
across four files, and the marker check would have passed after the first.

**Precedent:** finding **DF-5**, now at six occurrences, including one where the change that *built* the
counts check left three other numbers stale in the same file.

## 7. A source could not be retrieved

**Do:** record the attempt with its honest retrieval status. For a source with no URL, state **why** there is
none. For something you searched for and did not find, record it as a **research gap**, not as a confirmed
absence.

**Do not** invent a URL, quote from a source you did not read, or assert an absence you did not search for.

**Why:** an unverified absence is a to-do, not a finding. An audit once reported 76 defects against a real
count of 2 by matching two regexes and writing down the absence as a fact.

**Precedent:** the print-source exemption, taken from `risk-register` source 33. The `product-roadmap`
timeline rejection, recorded as a research gap rather than a confirmed absence. Finding **DF-2**, where three
bundles accused of carrying no retrieval status turned out to carry it in full, in a third layout.

## 8. A circulating statistic cannot be traced

**Do:** record it as **deliberately excluded**, with what you searched and what you found. Keep the list in
the research log.

**Do not** quietly omit it, and do not soften an accusation into a fact or a fact into an accusation. If one
researcher looked and did not find it, the honest word is **untraceable**, not fabricated.

**Why:** the next author will meet the same figure and repeat the search. And naming a real institution's
work as fabricated is a serious claim that should not rest on one search.

**Precedent:** `product-roadmap`'s two untraceable roadmap figures. `okrs`' exclusion list, where two claims
attaching real institutional names were downgraded from "fabricated" to "untraceable" because the agent
commissioned to test the accusation did not complete.

## 9. A defect recurs after a convention was adopted to prevent it

**Do:** build the check. The convention has been tested and has failed.

**Why:** every doc-level check in this repository was written after the corresponding drift had already been
found in the tree, and each one was written only once the drift recurred.

**Precedent:** finding **DF-6**. Example reuse was found in `product-strategy`, a convention was adopted, it
recurred in `product-roadmap`, and then recurred again in `okrs` **with the convention correctly applied**,
because the reuse lives in the sentence skeleton and survives swapping every noun. Finding **DF-5** followed
the same arc over five occurrences before `check-counts.py` existed.

## 10. A family or axis assignment is uncertain

**Do:** leave it flagged in the spec sheet and make the definitive call **when the contract is written,
against the family's actual members**.

**Why:** a spec sheet assignment is a hypothesis made before the members exist. Deciding early means deciding
without the evidence that would settle it.

**Precedent:** `buildout-specs.md`'s own status note says exactly this. `kpi-dashboard`'s axis was left
deliberately unresolved by [ADR 0023](decisions/0023-resolve-the-tier-1-family-taxonomy.md) and settled at
`governance-docs` contract time.

---

## What always stops for the maintainer

These are not judgment calls with a procedure. They are decisions that belong to the person who owns the
library, and an autonomous run stops at each one:

- **Scope.** What this library is willing to template, and what it declares out of scope.
- **Family contracts.** Drafted autonomously, **adopted only after a maintainer read.** A contract binds
  every future member of a family, and it is the batch-review boundary the pipeline already names.
- **Releases.** Version tags, release notes, and anything the release note asserts.
- **Any change to what the library claims about itself**, including the credibility claims in the README and
  the honesty claims in STATE.md.

Everything else in this file is a procedure, and a procedure is meant to be applied without asking.
