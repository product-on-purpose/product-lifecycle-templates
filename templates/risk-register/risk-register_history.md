# History: Risk Register bundle

Per-bundle changelog, by `template_version`. Newest first.

## 0.1.0 - 2026-07-22

- Initial Risk Register bundle. **First member of the `governance-docs` family** and the first bundle whose
  taxonomy axis is `classification` rather than `phase`. Catalog entry 150. Conforms to the
  [governance-docs contract](../../docs/internal/contracts/governance-docs.md) (`classification: utility`,
  `beta`, sizes `[lean, full]`); gate check K green on the classification axis
  ([ADR 0023](../../docs/internal/decisions/0023-resolve-the-tier-1-family-taxonomy.md),
  [ADR 0024](../../docs/internal/decisions/0024-adopt-governance-docs-family-contract.md)).
- **Scope: the canonical risk register, framed honestly.** The companion's sections 1, 6, and 7 make the
  case: the register is universal in formal practice (PMBOK, PRINCE2/M_o_R, ISO 31000's process, COSO's
  assessment activities) and under sustained, credentialed attack (Cox's "worse than useless" on risk
  matrices, Hubbard and Evans on ordinal scoring, the "risk theater" critique). The bundle teaches the
  register that survives the critique: living, objective-anchored, owner-assigned, residual-scored, and
  review-and-trigger driven.
- **The load-bearing honest-retrieval fact:** ISO 31000 does **not** name or mandate a "risk register." The
  one-line definition everyone quotes ("a record of information about identified risks") is from ISO Guide
  73:2009, the vocabulary companion. Practitioner and vendor pages routinely misattribute it; the companion
  (sections 2 and 5) states it correctly and makes it a teaching point rather than repeating the common
  error.
- **Variants: `lean` and `full`.** The catalog lists S/M/L; the two-weight split fits the artifact. Lean is
  the four sections every register needs: Purpose and Scope, an anchored Scoring Scale, the Risks table, and
  Review and Ownership. Full adds what governance earns: dual (inherent vs residual) scoring and columns
  (category, trigger/KRI, owner/actionee, proximity), an Escalation and Risk Appetite section, and a Closed
  and Materialized Risks audit trail. Nesting verified: lean's four H2 headings are a strict ordered subset
  of full's six.
- **The sharpest teaching points**, carried through companion, guide, and example: (1) a **risk is a
  potential future event; an issue has already happened** (register vs issue log); (2) the register is the
  **"R" of a RAID log**, a choice by audience and cadence; (3) a well-formed risk is a **cause -> event ->
  consequence** statement, not a theme label; (4) **inherent vs residual** scoring is the most consequential
  distinction and the only on-register evidence that controls work; (5) a register is a **living tool, not a
  filing cabinet**. These run through the guide's comparison table, quality rubric, and six named
  anti-patterns.
- **Worked example establishes the governance-docs shared scenario.** `risk-register_example.md` is a
  full-variant register for the Acme Analytics **Reporting Platform Modernization** program - the shared
  project the family's `raid-log` and `kpi-dashboard` examples will chain onto (the register is the RAID
  log's R; the dashboard tracks the outcomes these risks threaten). It delivers the same "Saved Views" work
  the delivery-docs family's PRD and SDD examples cover, tying the two families together. It demonstrates
  cause-event-consequence statements, inherent-vs-residual scoring, a named owner/actionee split, an
  opportunity row and an escalation, triggers that double as issue-log hand-off conditions, a measurable risk
  appetite, and a materialized risk with its scoring lesson.
- **`pairs_with: []`.** There is no `deliver-risk-register` or `govern-risk-register` skill in pm-skills
  (checked against `tools/known-skills.txt`, 2026-07-22). Recorded as context in `risk-register_guide.md`.
- Companion researched 2026-07-22 across five parallel dimensions and 33 tier-ranked, deduplicated sources
  (see `risk-register_research-log.md` for per-source retrieval status). Primary anchors include the PRINCE2
  wiki, the UK Government Teal Book (Chapter 20), the ISO 31000:2018 TC 262 page, and Cox's risk-matrix
  paper (abstract). Several strong sources are abstract-only or paywalled (Cox's full paper, Hubbard and
  Evans's IEEE paper, Hubbard's book, ISO Guide 73 itself); their arguments are attributed through fetched
  secondary syntheses and carry no fabricated quotes. Claims flagged contested: ISO 31000 not naming a
  register, four vs five response strategies, the heat-map "worse than useless" debate, whether agile needs
  a register, and that color-zone thresholds are a local choice. Nothing not fetched-and-verified is quoted.
- Status: `beta`. Gate-green, zero real usage by anyone other than the author.
