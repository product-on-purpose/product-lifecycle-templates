# trade-study: history

Change log for the `trade-study` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-10-15

**Initial release.** Researched 2026-10-15 across a seven-dimension fan-out: the NASA, SEBoK and ECSS
canon; the FHWA's trade study step and other published outlines; how criteria are weighted and options
scored; the debates and failure modes around weighted scoring; the library's own neighbours and the
worked example's independence; true technical facts about streaming-ingestion options for the worked
example; and the standing gap question. [`trade-study_research-log.md`](trade-study_research-log.md)
records 31 sources, of which 30 are fetched-and-verified and one, MITRE's trade study process, could not
be retrieved and supports no claim in this bundle.

**The fifth `decision-docs` member, and the second added beyond its three founders.** [ADR 0022 (adopt the
decision-docs family contract)](../../docs/internal/decisions/0022-adopt-decision-docs-family-contract.md)
names three roles, an RFC proposes a decision, an ADR records one, and an SDD describes an
implementation, and a trade study fills none of them: it evaluates named alternatives against weighted
criteria and feeds the decision rather than proposing, recording, or describing it. It joins under
ADR 0022's own consequence that a further member needs no contract change unless it declares a different
phase or size shape, the same way `spike-report` joined earlier, and its companion's section 8 states that
placement against the three founders and against `business-case` directly.

**The lean/full split tracks formality, not length alone.** The lean variant carries the five sections
this bundle treats as the minimum comparison: Problem and Decision Framing, Criteria and Weights,
Alternatives, Scoring Matrix, and Recommendation. The full variant is a strict superset, adding
Sensitivity Analysis, Risk and Benefit, Dissent or Independent Review, and References for a decision that
is hard to reverse or will be checked by a reviewer outside the immediate team. Microsoft's own
engineering playbook sets the floor on the other side: "Trade studies should be avoided if there is a
clear solution choice," and that guidance is carried into both variants' opening comment rather than left
for a reader to infer.

**No pm-skills pairing.** `tools/known-skills.txt` carries no skill for a trade study, trade-off analysis,
decision analysis, or options analysis as of this check, so `pairs_with: []`, the same honest declaration
`rfc` and `sdd` already carry in this family.

**The honest core, carried into the bundle rather than assumed.** Every claim of value this research
found, traceability, repeatability, a defense against bias, is an assertion by the bodies that recommend
the practice, not a measured outcome. Nothing retrieved for this bundle measured whether writing a trade
study improves the decision it supports, and the companion says so rather than borrowing more confidence
than the evidence carries.
