# change-request: history

Change log for the `change-request` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-09-25

**Initial release.** Specced in
[`tier2-specs.md`](../../docs/internal/tier2-specs.md), built on the maintainer's direction under
[ADR 0041 (maintainer preference sets the build order)](../../docs/internal/decisions/0041-maintainer-preference-sets-the-build-order.md)
(GitHub issue #179, build-candidate 5). Researched 2026-09-25 in two passes: an admission sweep run while the
spec was written, covering IT service management, project change control, boundaries and the library's own
references, and the build's six-dimension fan-out (definitions and process, published forms, the IT service
neighbor, the agile position, boundaries and failure modes, and the standing gap question).
[`change-request_research-log.md`](change-request_research-log.md) records **48 sources, all
fetched-and-verified.** Of 246 quotations the build's agents returned, 225 passed a check against each
source's raw text as retrieved; thirteen survive only as the separate verbatim sentences a composite had
fused together, eight were dropped, ten salvaged fragments too short to mean anything were removed, and eight
quotations were added from the main loop's own checks.

**No `delivery-docs` contract admitted this type as written.** A 2026-09-25 research pass tested a
per-occasion change request against all nine family contracts and every one excluded it; the closest,
`governance-docs`, names "an event-driven or phase-bound artifact" as out of its family. The maintainer
widened `delivery-docs` with a fifth verb, "changes", carrying the contract to `0.2.0`: see
[ADR 0060 (change-request joins delivery-docs)](../../docs/internal/decisions/0060-change-request-joins-delivery-docs.md).

### Which change request, decided and stated

Two lineages publish this name and the readable sources support them about equally: the **project and
product baseline** lineage (PMI's *Lexicon*, the PMBOK Guide 6th edition errata, PRINCE2, APM, the European
Commission's PM² guide and its Change Request Form, the CDC Unified Process form, GSA's Requirements Change
Request Form) and the **IT service** lineage, a change to a running production system reviewed by a change
advisory board (NIST SP 800-128 and SP 800-53 CM-3, the ITIL glossary, IT Process Wiki's RFC checklist). This
bundle serves the baseline lineage, because the library's own routing already used it that way (a bug-report
reader asking for behavior nothing promised is asking to change what the PRD and acceptance criteria agreed)
and because the library's audience is product management and software delivery, not IT operations. The IT
service lineage is described as a named neighbor in the companion (its vocabulary of standard, normal and
emergency changes, a change authority, and a back-out plan) and is not templated.

### `pairs_with` resolved to empty

No skill in [`tools/known-skills.txt`](../../tools/known-skills.txt) addresses authoring a per-occasion
change request; the closest entries (`deliver-prd`, `deliver-user-stories`, `deliver-acceptance-criteria`,
`deliver-release-notes`, `develop-adr`) serve other stages of the same delivery chain. `pairs_with: []` is a
deliberate, checked answer, in the same posture the `rfc` bundle already takes for the same reason.

### `related_templates` and the catalog entry

`related_templates` names the siblings this document actually connects to: `prd` and `acceptance-criteria`
as upstream baselines a change can target, `bug-report` and `issue-log` as the two members whose own guidance
routes a reader here (`bug-report_guide.md`: "If nothing promised the behavior you want, that is a change
request"; `issue-log_template-full.md` links an issue "to a risk it materialized from, a change request it
raised, or a decision that closed it"), and `release-notes` as the downstream record of what an approved
change eventually ships as.

The library's own catalog (entry 120, "Change Request") frames the type as an IT-service artifact: purpose
"Formally request and authorize a production change", owner Change Manager, methodology ITIL, related to CAB
review. This bundle corrects that framing on landing, per
[procedure 1](../../docs/internal/decision-procedures.md#1-a-catalog-call-loses-to-research): the metadata
keeps the catalog's `change record` and `change ticket` aliases but drops its `RFC (ITIL)` alias, because
that abbreviation collides with this library's own `rfc` bundle (a request for comments), a collision the
companion names on its first page rather than inherits silently.
