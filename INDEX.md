# INDEX - product-lifecycle-templates

> Generated from `library.json` + component frontmatter by `gen-index` and
> drift-checked (G4). Edit the source, not this file. Overview and positioning are
> in [`README.md`](README.md); agent guidance is in [`AGENTS.md`](AGENTS.md).

**Tier:** Gold (advanced). Standard 0.17. Version 0.25.0. Self-validating: `npx agent-skills-toolkit .`.

## Components

### Skills (2)

- [`plt-fill-template`](skills/plt-fill-template/) - Selects and fills a product-document template from a 56-bundle library, then grades it on that type's rubric. Use when writing a PRD, epic, user stories, use case specification, acceptance criteria, product or sprint backlog, change request, release notes, internal announcement, risk register, RAID log, issue log, change log, KPI dashboard, tracking plan, data dictionary, test plan, test case, traceability matrix, bug report, test summary report, ADR, RFC, software design document, spike report, trade study, product vision, strategy or roadmap, Lean Canvas or Lean UX Canvas, positioning statement, OKRs, North Star metric, problem statement, design brief, user research plan or report, project brief, business case, user persona, experiment design or readout, definition of done or ready, test strategy, runbook, launch checklist, production readiness review, business continuity plan, incident postmortem, retrospective notes, or status report. Most ship lean and full variants, a worked example and a research log.
- [`plt-grade-doc`](skills/plt-grade-doc/) - Grades a product document on its type's researched rubric, returning a report card quoting it and naming three fixes worth an hour. Use when asked for a review, critique, second opinion, or score on a PRD, epic, user stories, use case specification, acceptance criteria, product or sprint backlog, change request, release notes, internal announcement, risk register, RAID log, issue log, change log, KPI dashboard, tracking plan, data dictionary, test plan, test case, traceability matrix, bug report, test summary report, ADR, RFC, software design document, spike report, trade study, product vision, strategy or roadmap, Lean Canvas or Lean UX Canvas, positioning statement, OKRs, North Star metric, problem statement, design brief, user research plan or report, project brief, business case, user persona, experiment design or readout, definition of done or ready, test strategy, runbook, launch checklist, production readiness review, business continuity plan, incident postmortem, retrospective notes, or status report.

### Subagents (0, Claude-only)

- none

### Commands (0)

- none

## Manifests

- [`library.json`](library.json) - authored canonical cross-agent manifest (the source of truth).
- [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) - Claude Code native manifest (generated; do not hand-edit).

## Documentation and governance

- [`README.md`](README.md) - overview, positioning, quickstart.
- [`CHANGELOG.md`](CHANGELOG.md) - full technical history; [`RELEASE-NOTES.md`](RELEASE-NOTES.md) - curated, user-facing notes.
- [`docs/`](docs/) - Diataxis docs (reference, how-to, explanation).
- [`docs/internal/decisions/`](docs/internal/decisions/) - ADRs.
- [`templates/`](templates/) - scaffolder templates.
- [`scripts/`](scripts/) - the Node validation spine (conformance checks, generators, gate, evaluate).
