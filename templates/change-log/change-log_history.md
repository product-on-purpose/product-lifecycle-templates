# change-log: history

Change log for the `change-log` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-09-28

**Initial release.** Admitted as the fifth `governance-docs` member by
[ADR 0061 (change-log joins governance-docs as a fifth member)](../../docs/internal/decisions/0061-change-log-joins-governance-docs-as-a-fifth-member.md),
which lands the family contract at `0.3.0`. Assigned and specced 2026-09-27 in
[`tier2-specs.md`](../../docs/internal/tier2-specs.md), built on the maintainer's direction under
[ADR 0041 (maintainer preference sets the build order)](../../docs/internal/decisions/0041-maintainer-preference-sets-the-build-order.md).
[`change-log_research-log.md`](change-log_research-log.md) records **40 sources, all fetched-and-verified**.
Every quotation was checked against each source's raw text rather than a retrieval tool's summary of it: of
139 quotations the build's agents returned, 129 passed as returned, and after repairs and additions from the
main loop's own checks, **145 quotations remain, and every one passes.**

### The bundle id, kept apart from the catalog id

The catalog carries this candidate as `change-log-governance` (catalog entry **154**), to keep it apart from
a software changelog under the identical plain-English name. The bundle itself ships as `change-log`, the
shorter, natural phrase a reader or an agent actually types, because the boundary against a software
changelog is drawn in the template's own opening guidance and in the companion's section 1 and section 8,
not by a compound folder name. `change-log-governance` stays as the catalog id and as the reason
`change-log-governance` never appears in `aliases`, which instead carries the names practitioners and
public bodies actually use for the artifact itself.

### `pairs_with` resolved to empty, and checked against a near-miss

No skill in [`tools/known-skills.txt`](../../tools/known-skills.txt) addresses authoring or maintaining a
governance change log. The one name that reads like a match on a plain-text search,
`utility-pm-changelog-curator`, drafts software changelog entries from git history, the different artifact
this bundle's guide and companion both draw a boundary against; pairing this bundle to it would repeat the
exact collision the boundary exists to prevent. `pairs_with: []` is a deliberate, checked answer, in the same
posture the `rfc` and `issue-log` bundles already take for the same reason.

### `related_templates` and the family it joins

`related_templates` names `change-request` (the delivery-docs sibling that files one document per occasion
and feeds a row into this log), `issue-log`, `risk-register`, `raid-log`, and `kpi-dashboard` (the four other
`governance-docs` members this contract's section 1 states the relationship against). No source read in this
bundle's own research compares a change log to a risk register, a RAID log, or a KPI dashboard directly; the
family contract's own framing, not a numbered source, is what the companion's section 8 cites for that
parallel, and it is stated there as this library's own position rather than as a sourced claim.

### `sizes_available` resolved to `[lean, full]`, following the shared spine plus a genuine second weight

Three or more of the published field lists this research read share an identifier, a description, a
raised date, and a status; a smaller, working register needs no more than that plus a decider and a threshold, which is what
lean carries. A second weight earned its place on the same evidence the guide's Pick a variant section
states: a sponsor or governance body eventually asking how far a baseline has moved in total, a decision
date and a delivery date that genuinely diverge, or a log that needs a named owner because more than one
person could plausibly be asked to keep it. Full adds exactly the three sections that answer those three signals, and nothing else.

### PRINCE2, named as the family's one stated exception

This bundle's companion states PRINCE2's own convention, keeping a request for change inside its issue
register and naming a change log only as an alternative place to write the eventual decision, as a
deliberate methodology choice rather than the collapsing failure the family contract otherwise warns
against. The family contract itself was amended alongside this bundle's admission to record that
qualification in its own section 1, per
[decision-procedures.md section 11](../../docs/internal/decision-procedures.md#11-a-family-contract-asserts-something-about-the-world).

### What was not read, and is not claimed

The PMBOK Guide itself, sixth or eighth edition, was not read; only its openly hosted errata was. ISO
21502:2020 and AXELOS's PRINCE2 manual are both paid standards this research did not read; PRINCE2 enters
this bundle only through prince2.wiki's practitioner pages. Wikipedia's "Changelog" article was not
retrieved, so the boundary this bundle draws against a software changelog rests on Keep a Changelog alone.
Review-cadence figures a search tool's summary attributed to vendor pages nobody read do not appear anywhere
in this bundle.
