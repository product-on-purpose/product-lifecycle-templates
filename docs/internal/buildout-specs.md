# Tier-1 floor build-out: per-type specs and progress

Companion to [`buildout-plan.md`](buildout-plan.md) (adopted, [ADR 0021](decisions/0021-complete-the-tier-1-floor.md)).
This is the **working spec sheet and progress tracker** for completing the 27-type Tier-1 floor. It
front-loads the per-type judgment (family, phase/classification, sizes, catalog_ref, section design) so
each bundle is a spec-driven execution rather than an open-ended design task, and it is the durable
reference a future session reads to continue.

> **Status of the calls below: provisional, pending maintainer ratification.** Phase/classification
> assignments especially are hypotheses (like the catalog's own size calls, EC-2). The definitive call for
> each family is made when its contract is written, against its actual members. Where the phase-XOR-
> classification axis does not cleanly fit a family, it is **flagged** rather than forced.

## Progress

| # | Bundle | Family | Phase/Class | Status | PR |
|---|---|---|---|---|---|
| 1 | prd | delivery-docs | phase: deliver | **done** | - |
| 2 | user-stories | delivery-docs | phase: deliver | **done** | - |
| 3 | acceptance-criteria | delivery-docs | phase: deliver | **done** | - |
| 4 | release-notes | delivery-docs | phase: deliver | **done** | - |
| 5 | product-backlog | delivery-docs | phase: deliver | **done** | #28 |
| 6 | adr | decision-docs | phase: develop | **done** | - |
| 7 | rfc | decision-docs | phase: develop | **done** | - |
| 8 | sdd | decision-docs | phase: develop | **done** | #26 |
| 9 | sprint-backlog | delivery-docs | phase: deliver | **done** (delivery-docs complete) | kickoff PR |
| 10 | product-vision | strategy-docs | *see flag* | planned | - |
| 11 | product-strategy | strategy-docs | *see flag* | planned | - |
| 12 | business-case | strategy-docs | phase: discover | planned | - |
| 13 | okrs | strategy-docs | *see flag* | planned | - |
| 14 | product-roadmap | strategy-docs | *see flag* | planned | - |
| 15 | test-plan | qa-docs | phase: develop | planned | - |
| 16 | test-case | qa-docs | phase: develop | planned | - |
| 17 | bug-report | qa-docs | phase: develop | planned | - |
| 18 | risk-register | governance-docs | class: utility | planned | - |
| 19 | raid-log | governance-docs | class: utility | planned | - |
| 20 | kpi-dashboard | governance-docs | *see flag* | planned | - |
| 21 | user-persona | discovery-docs | phase: discover | planned | - |
| 22 | wireframe | design-docs | phase: develop | planned | - |
| 23 | interactive-prototype | design-docs | phase: develop | planned | - |
| 24 | runbook | ops-docs | class: tool | planned | - |
| 25 | incident-postmortem | ops-docs | *see flag* | planned | - |
| 26 | status-report | communication-docs | class: utility | planned | - |
| 27 | definition-of-done | **standing-standards (reassigned)** | class: foundation | planned | - |
| - | sprint-retrospective-notes | process-docs | phase: iterate | planned | - |

**Count:** 9 done (both existing families complete), 18 planned. (The catalog's 27-type Tier-1 set plus
sprint-retrospective-notes, which the buildout-plan includes; final count reconciled when the last family
lands.)

---

## Cross-cutting decisions to ratify before the mass build

These are the judgment calls that affect multiple bundles. **They are the highest-value thing to review
now**, because building 18 bundles on a wrong call is expensive to unwind.

### D-A. definition-of-done is reassigned out of delivery-docs

The buildout-plan lists `definition-of-done` under delivery-docs, but a DoD is a **standing quality
standard** (one DoD applies to every increment), which is `classification: foundation`, not
`phase: deliver`. Forcing it into the phase-`deliver` delivery-docs family would require either bending
its honest metadata or amending the delivery-docs contract to accept a classification member, the exact
anti-pattern [ADR 0020](decisions/0020-adopt-delivery-docs-family-contract.md) warns against.

**Proposed resolution:** delivery-docs **completes at sprint-backlog** (six phase-`deliver` members).
definition-of-done moves to a **standing-standards** family (with definition-of-ready and similar
"agreed-once, applied-repeatedly" standards) built later, or to governance-docs. This keeps every family
coherent on the phase/classification axis. **Needs maintainer ratification.**

### D-B. Several proposed families are not phase/classification-coherent

The check-K family contract currently expresses one `phase` per family. Families flagged *see flag* above
mix the axis and will each need a decision when their contract is written:

- **strategy-docs**: `business-case` is a one-time, phase-bound artifact (discover/feasibility), but
  `product-vision` and `product-roadmap` are standing (foundation/utility) and `okrs`/`product-strategy`
  are periodic. Options: (a) make strategy-docs a **classification-coherent** family (most are standing),
  moving business-case elsewhere; (b) a phase-`discover` family, treating vision/roadmap as discover-phase
  outputs; (c) split into strategy (standing) and planning (periodic). **Leaning (a)/(c); ratify at
  contract time.**
- **ops-docs**: `runbook` is a standing operational tool (`class: tool`), `incident-postmortem` is an
  event-driven learning artifact (phase `iterate`/`measure`). These do not share an axis. Options: split,
  or a family defined by *domain* (operations) with a contract that allows both a standing tool and an
  event artifact. **Ratify at contract time.**
- **kpi-dashboard**: standing measurement tool (`class: utility`/`tool`) vs. phase `measure`. Leaning
  `class: utility` to keep governance-docs classification-coherent.

### D-C. check-K may need to support classification-axis families

Every family contract so far (delivery-docs, decision-docs) gates on `phase`. governance-docs is the first
**classification**-axis family. Before it lands, check-K's `FAMILY_CONTRACTS` and `check_family` must
accept a `classification` constraint (a member declares phase XOR classification; the contract should gate
whichever axis the family uses). Small, adversarially-tested gate change, sequenced before governance-docs.

---

## Per-type specs

Each entry: **family, phase/classification, sizes, default, methodology, catalog_ref, aliases** and a
**section-design sketch** (lean H2s; full adds). Section designs are sketches to be finalized during the
bundle's own research; they exist to make the build spec-driven, not to freeze it. "Key sources" names the
research anchors; the actual research log is built per bundle to the honest-retrieval standard.

### delivery-docs (finishing)

**sprint-backlog** (catalog 76) - family delivery-docs, **phase deliver**, sizes [lean, full], default
lean, methodology agile-scrum, aliases: iteration backlog, sprint plan. Drawn from the product backlog;
commitment is the Sprint Goal.
- Lean: Sprint Goal; Selected Items (table); Plan and Ownership.
- Full adds: Capacity and Commitment; Progress and Tracking (burndown/board); Risks and Carry-over.
- Key sources: Scrum Guide 2020 (Sprint Backlog: goal + selected items + actionable plan; developers own
  it), Cohn/Pichler on sprint planning and capacity, the product-backlog bundle (its downstream sibling).
- Teaching points: the sprint backlog is the developers' plan (not the PO's), it is a forecast not a
  contract, and it derives from (not duplicates) the product backlog. Chains with the delivery-docs Saved
  Views example (the sprint that pulls the top Saved Views items).

**definition-of-done** (catalog 39) - **reassigned** (see D-A). class foundation, sizes [lean], methodology
agile-scrum, aliases: DoD, done criteria. Build with the standing-standards family, not delivery-docs.

### strategy-docs (new family; contract first; see D-B)

**product-vision** (catalog 1) - strategy-docs, phase/class *TBD (foundation leaning)*, sizes [lean, full],
methodology methodology-agnostic, aliases: vision statement, product vision board (Pichler), Vision FAQ
(Cagan). Section sketch - Lean: The Vision (aspirational end-state); Target Customer and Needs; Why Us
(differentiation). Full adds: Business Goals; Guardrails/Principles; Time Horizon. Key sources: Pichler
Product Vision Board, Cagan Product Vision FAQ, Moore (positioning). Teaching point: a vision is an
enduring aspiration, not a roadmap or a feature list.

**product-strategy** (catalog 2) - strategy-docs, phase/class *TBD*, sizes [lean, full], methodology-agnostic
(OKR-friendly), aliases: strategy doc, strategy one-pager. Lean: Focus (which problems matter); Insights;
Strategic Bets. Full adds: Target Segments; Principles; What We Are Not Doing. Key sources: Cagan
(strategy as "which problems matter most"), Rumelt (good vs bad strategy), Ramp/Reforge strategy formats.

**business-case** (catalog 3) - strategy-docs (or reassign), **phase discover**, sizes [lean, full],
methodology methodology-agnostic (PMBOK), aliases: cost-benefit analysis, investment case, value case.
Lean: Problem and Opportunity; Options Considered; Recommendation. Full adds: Costs; Benefits; Risks;
Financials. Key sources: PMBOK 7 (Strategy artifact), standard cost-benefit/NPV practice. Formal-auditable.

**okrs** (catalog 6) - strategy-docs, phase/class *TBD (utility/periodic leaning)*, sizes [lean, full],
methodology OKR-driven, aliases: objectives and key results, V2MOM (Benioff variant). Lean: Objective(s);
Key Results (measurable, table). Full adds: Initiatives; Owners; Confidence/Check-in. Key sources: Doerr
(*Measure What Matters*), Grove (origin at Intel), Google re:Work OKR guide. Teaching point: key results
are measurable outcomes, not a task list; separate committed vs aspirational.

**product-roadmap** (catalog 68) - strategy-docs, phase/class *TBD (utility leaning)*, sizes [lean, full],
methodology methodology-agnostic, aliases: roadmap, now-next-later, outcome roadmap. Lean: Outcomes/Themes;
Now-Next-Later (table). Full adds: Timeframes; Dependencies; Status/Confidence. Key sources: Cagan (outcome
vs feature roadmaps), Lombardo (*Roadmaps Relaunched*), the product-backlog bundle (roadmap-vs-backlog).
Teaching point: outcome roadmap over feature-list roadmap; the roadmap scopes the backlog.

### qa-docs (new family; contract first; see D-B)

**test-plan** (catalog 102) - qa-docs, **phase develop** *(TBD; QA may be utility)*, sizes [lean, full],
methodology methodology-agnostic, aliases: master test plan, MTP. Lean: Scope and Approach; Test Items;
Entry/Exit Criteria. Full adds: Environments and Data; Schedule and Resources; Risks. Key sources:
ISO/IEC/IEEE 29119-3 (supersedes IEEE 829), practitioner test-strategy writing. Note recency: 829 is legacy.

**test-case** (catalog 104) - qa-docs, phase develop, sizes [lean] *(catalog S)*, methodology-agnostic,
aliases: test case specification, test script. Lean: Preconditions; Steps and Test Data; Expected Result;
Status. Key sources: ISO/IEC/IEEE 29119, practitioner test-design (equivalence partitioning, boundary).

**bug-report** (catalog 107) - qa-docs, phase develop, sizes [lean] *(catalog S)*, methodology-agnostic,
aliases: defect report, defect ticket, issue. Lean: Summary; Steps to Reproduce; Expected vs Actual;
Severity and Environment. Key sources: practitioner defect-reporting guides; severity-vs-priority
distinction is the teaching point.

### governance-docs (new family; classification-axis; needs D-C gate change first)

**risk-register** (catalog 150) - governance-docs, **class utility**, sizes [lean, full], methodology
methodology-agnostic (PMBOK), aliases: risk log. Lean: Risks (table: risk, likelihood, impact, owner,
response, status). Full adds: Scoring/Heatmap; Review Cadence; Escalation. Key sources: PMBOK 7 risk
management, ISO 31000.

**raid-log** (catalog 151) - governance-docs, class utility, sizes [lean, full], PMBOK, aliases: RAID,
DCARI variant. Lean: Risks; Assumptions; Issues; Dependencies (one table or four). Full adds: Ownership and
Dates; Cross-links; Review Cadence. Key sources: PMBOK, PMI. Teaching point: RAID is a superset of the risk
register; when to use which.

**kpi-dashboard** (catalog 139) - governance-docs, class utility *(TBD; measure)*, sizes [lean, full],
methodology-agnostic, aliases: metrics dashboard, scorecard. Lean: Metrics (table: KPI, target, current,
trend). Full adds: Segments; Alerting/Thresholds; Data Sources. Key sources: NSM/OKR-derived metrics,
Croll/Yoskovitz (*Lean Analytics*). Note: this is a document *template* for a dashboard's definition, not a
live dashboard.

### discovery-docs (new family; single member for now)

**user-persona** (catalog 19) - discovery-docs, **phase discover**, sizes [lean, full], methodology design
thinking, aliases: customer persona, buyer persona, proto-persona. Lean: Who They Are; Goals; Pains and
Behaviors. Full adds: Scenarios; Quotes/Evidence; Anti-persona. Key sources: Cooper (personas origin),
design-thinking practice, proto-persona (Gothelf). Teaching point: evidence-based vs invented personas;
proto-persona as the lean form.

### design-docs (new family; see D-B)

**wireframe** (catalog 52) - design-docs, **phase develop** *(TBD; design)*, sizes [lean, full],
methodology-agnostic, aliases: lo-fi mockup, schematic. **Note:** a wireframe is inherently visual; the
template is a *specification wrapper* (intent, layout description, annotations) around the artifact, not
the pixels. Lean: Purpose and Context; Layout and Hierarchy; Annotations. Full adds: States; Flow;
Handoff Notes.

**interactive-prototype** (catalog 54) - design-docs, phase develop, sizes [lean, full], design
thinking/dual-track, aliases: clickable prototype, hi-fi prototype. Template is the spec around the
prototype (flows, interactions, states) per Cagan's "prototype is the majority of the spec". Lean:
Purpose and Scope; Flows and Interactions; States. Full adds: Test Plan/Usage; Fidelity Notes; Handoff.

### ops-docs (new family; see D-B, mixed axis)

**runbook** (catalog 116) - ops-docs, **class tool**, sizes [lean, full], methodology DevOps/SRE, aliases:
operational runbook, SOP. Lean: Purpose and Prerequisites; Procedure (steps); Verification and Rollback.
Full adds: Triggers/Alerts; Escalation; Related Runbooks. Key sources: Google SRE book, PagerDuty runbook
guidance.

**incident-postmortem** (catalog 127) - ops-docs, **phase iterate** *(event-driven learning)*, sizes
[lean, full], methodology SRE/DevOps, aliases: postmortem, RCA, after-action review. Lean: Summary and
Impact; Timeline; Root Causes and Action Items. Full adds: Contributing Factors; Detection/Response
analysis; Prevention. Key sources: Google SRE (blameless postmortem, every user-affecting outage gets a
P0/P1 action item), Etsy/Allspaw. Teaching point: blameless; the sharpest distinction is postmortem
(learning) vs incident report (live record).

### communication-docs (new family; single member for now)

**status-report** (catalog 180) - communication-docs, **class utility**, sizes [lean, full], methodology-
agnostic, aliases: project status, weekly update, RAG report. Lean: Summary and RAG Status; Accomplishments;
Risks and Next Steps. Full adds: Metrics; Decisions Needed; Detailed Breakdown. Key sources: PMBOK report
artifact, practitioner status-update writing. Teaching point: RAG honesty; audience-appropriate brevity.

### process-docs / standing-standards (single members; small families or reassignments)

**sprint-retrospective-notes** (catalog 187) - process-docs, **phase iterate**, sizes [lean], methodology
Scrum/agile, aliases: retro notes, retrospective. Lean: What Went Well; What To Improve; Action Items. Key
sources: Derby and Larsen (*Agile Retrospectives*), Scrum Guide. Teaching point: distinct from an incident
postmortem; action items with owners are the point.

**definition-of-done** - see D-A. Likely anchors a **standing-standards** family (with definition-of-ready).
class foundation, sizes [lean], methodology agile-scrum.

---

## Build order (revised from buildout-plan, pending ratification)

1. **Finish delivery-docs**: sprint-backlog. (decision-docs already complete.)
2. **The check-K classification-axis change** (D-C), then **governance-docs** (risk-register, raid-log,
   kpi-dashboard): the first classification family, clean once D-C lands.
3. **qa-docs** (test-plan, test-case, bug-report): coherent phase-develop family.
4. **strategy-docs** once D-B is resolved (family shape decided): the biggest, highest-visibility family.
5. **The small families**: discovery-docs (user-persona), design-docs (wireframe, interactive-prototype),
   ops-docs (runbook, incident-postmortem - after D-B), communication-docs (status-report), process-docs
   (sprint-retrospective-notes), and the standing-standards family (definition-of-done).

Rationale for reordering from the buildout-plan: do the **axis-coherent** families (governance classification,
qa develop) early to exercise and settle the classification-axis machinery (D-C) before the **mixed-axis**
families (strategy, ops) that need the harder contract decisions. Every reorder is a hypothesis; ratify.

## The discipline that does not change

- Research to the honest-retrieval standard (only quote fetched-and-verified); adversarial four-lens review
  on every bundle before the PR (see [`bundle-pipeline.md`](bundle-pipeline.md)); the gate proves structure,
  never truth.
- Every new family gets a **contract first** (the [ADR 0020](decisions/0020-adopt-delivery-docs-family-contract.md)
  pattern), which is where its phase/classification is finally decided against real members.
- No bundle is "verified" until a real person fills it; coverage and real usage stay separate, honest
  numbers in STATE.md ([ADR 0021](decisions/0021-complete-the-tier-1-floor.md)).
