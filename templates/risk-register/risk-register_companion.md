# Companion: The Risk Register

> The deep explainer for the risk-register bundle. Read this to understand what a risk register is, where it
> came from, why it is shaped the way it is, and where practitioners disagree about it. The short operator
> card is [`risk-register_guide.md`](risk-register_guide.md); a fully worked instance is
> [`risk-register_example.md`](risk-register_example.md). Inline citations like [[1]](#ref-1) resolve to the
> [References](#references) at the bottom, tagged by source reliability.

---

## 1. Orientation

A risk register is **the single, maintained record of the risks to an objective: what could happen, how
likely and how damaging it is, who owns it, what you are doing about it, and whether that is working.** It is
not a one-time document filed at kickoff, not a list of problems you already have, and not a compliance
artifact you produce for an auditor and never open again. Wikipedia captures the plain version: it is *"a
document used as a risk management tool and to fulfill regulatory compliance, acting as a repository for all
risks identified"* [[1]](#ref-1). PRINCE2 states the purpose more sharply: the register *"aims to capture and
maintain information on identified threats and opportunities related to the project, supporting the practical
application of the risk practice"* [[5]](#ref-5).

The honest first thing to know is that the risk register is **universal in formal practice and under
sustained, credentialed attack.** Every major framework assumes one, and a serious body of work argues that
the way most registers score risk is mathematically unsound and that in practice they decay into "risk
theater": a list created once, filed, and never revisited. This bundle teaches the register that **survives
that critique**, and section 6 states the argument in full rather than hiding it.

The best one-line reframe of what a good register is comes from the governance world: it is *"not a list of
things that could go wrong. It is your organization's documented position on every significant risk it has
chosen to accept, treat, transfer, or avoid"* [[20]](#ref-20). A register is a set of **decisions**, not a
set of worries.

**At a glance**
- A **risk is a potential future event**; an **issue has already happened.** The register tracks risks; a
  risk that materializes moves to an issue log [[19]](#ref-19)[[21]](#ref-21).
- Each entry is a **cause -> event -> consequence** statement, not a vague label [[11]](#ref-11).
- It carries **who owns each risk and what the response is** - a named individual, not a team
  [[14]](#ref-14).
- The **residual** score (after your controls) matters more than the inherent one; the gap between them is
  the evidence your controls work [[13]](#ref-13).
- It is a **living tool, not a filing cabinet**; out-of-date scoring is the most common way it fails
  [[21]](#ref-21).
- It is the **"R" of a RAID log**, promoted into a standalone governance artifact when scale or regulation
  warrants it [[18]](#ref-18).

If you read nothing else: a risk register is a **living, owned record of decisions about uncertain events
that threaten (or could help) an objective.** The moment it stops being re-scored against what you have
learned, or its ratings stop meaning anything specific, it has become the thing its critics warn about.

---

## 2. Origins and evolution

**The risk register is a codification of project risk practice that hardened between the late 1990s and the
mid-2000s.** Before that, project risk was managed, but not through one canonical, named artifact with a
defined field set. Three strands converged.

**The academic strand.** Chris Chapman (founding chair of the UK Association for Project Management's project
risk management specific-interest group) and Stephen Ward's *Project Risk Management: Processes, Techniques
and Insights* (1997; 2nd ed. 2003) systematized project risk management into the structured, process-based
discipline that later frameworks encoded.

**The governance strand.** In the UK, the Turnbull Report on corporate governance (1999) embedded structured
risk practice into listed-company obligations, and the Office of Government Commerce answered it in 2002 with
**M_o_R (Management of Risk)**, which codified the register in public-sector project management
[[10]](#ref-10). M_o_R established a framing the register still carries: *"Risk is a neutral concept; risks
can either be threats (downside risks) or opportunities (upside risks)"* [[10]](#ref-10). A register tracks
both, not just what could go wrong. (In 2024 PeopleCert rebranded M_o_R as PRINCE2 Risk Management; pre-2024
"M_o_R" material remains valid history [[10]](#ref-10).)

**The standards strand.** PMI's PMBOK Guide elevated the register to the **primary output of a formal
"Identify Risks" process**, "created in one process, but... elaborated on during other processes throughout
the course of the project" [[7]](#ref-7): it is born at identification and then filled in as you analyze,
plan responses, and monitor. PMBOK defines the underlying object as *"an uncertain event or condition that,
if it occurs, has a positive or negative effect on one or more project objectives"* [[8]](#ref-8).

**The register's own definition was fixed by a vocabulary standard, and this is where a near-universal
misattribution starts.** The crisp one-line definition everyone quotes - a risk register is *"a record of
information about identified risks"* - is from **ISO Guide 73:2009**, the risk-management vocabulary
companion [[1]](#ref-1)[[2]](#ref-2). It is routinely attributed to **ISO 31000**, which is wrong: ISO 31000
*"addresses risk documentation... but doesn't specifically use the term 'risk register'"* [[1]](#ref-1). The
distinction matters because it tells you what the standard actually requires (a documented process), not a
particular document. Section 5 returns to this.

**The modern shift is toward "uncertainty," up and down.** ISO 31000:2018 redefined risk itself as *"the
effect of uncertainty on objectives"* rather than the older "chance of loss," explicitly *"encompassing both
negative and positive consequences of uncertainty"* [[3]](#ref-3). PMBOK's later editions moved risk from a
mandatory named process output (6th edition) to a principle-level concern (7th edition), repositioning the
register from a required artifact to a "commonly used" one without removing it from practice.

---

## 3. Anatomy (section by section)

The register's body is a **table**, one row per risk. Everything else in the document exists to make that
table's numbers mean something. This section walks the fields; the template groups them into the sections
you actually fill.

### Purpose and Scope

**What it is:** one short block naming what this register covers (which project, program, or objective), who
owns the register itself, and where the scoring scales live. **Why it exists:** a risk rating is meaningless
without a scope and a scale. The register's critics land their sharpest blow here: *"These are risks to what
and what the devil does a 'high' rating mean?"* [[25]](#ref-25). Naming the objective the risks threaten is
what makes them rankable; a register disconnected from an objective is *"a static list of risks... Managing
a list of what could go wrong is not the same as considering how best to achieve objectives"* [[25]](#ref-25).

### Scoring Scale

**What it is:** the anchored definitions of your likelihood and impact levels, and how they combine into a
score. **Why it exists:** so that "high" is not, in Tim Clements's phrase, like *"saying an investment is
'big' or 'small'"* [[26]](#ref-26). The dominant convention is a 5x5 matrix with **Risk Level = Probability
x Impact**, producing a 1-25 score [[16]](#ref-16). Likelihood levels are anchored to frequency (for example
"almost certain" = greater than 80% in a defined horizon) and impact levels to consequence (a cost, a delay,
a regulatory outcome) [[16]](#ref-16). The score is a **prioritization signal, not a measurement** - section
6 explains why that distinction is load-bearing, and why the color-zone thresholds are yours to set, not a
standard's to dictate [[15]](#ref-15).

### Risks (the table)

**What it is:** the heart of the register. One row per risk, each carrying at minimum: an **ID**, a
**risk statement**, **likelihood** and **impact** scores and their product, a **response**, an **owner**, and
a **status**. A register tracks *"both threats and opportunities, ensuring that each is logged, analysed, and
assigned an owner responsible for managing it"* [[6]](#ref-6) - the rows are not only bad news.

- **Risk statement.** A well-formed risk is a **cause -> event -> consequence** sentence, not a theme label
  like "security." The ISO-aligned form is *"Because of [cause], there is a risk that [event], which could
  lead to [consequence]"* [[11]](#ref-11); the equivalent If-Then form is *"If [event triggered by cause],
  then [consequence on objective]"* [[12]](#ref-12). The quality bar is the "4Cs" (clear, concise,
  consistent, comprehensive), and each statement should cover **one** risk so it can be scored and owned
  [[12]](#ref-12). A row that says "budget" is not a risk; a row that says "because the vendor contract is
  not signed, there is a risk the integration slips past the launch date, delaying revenue by a quarter" is.
- **Likelihood and impact.** Scored on the anchored scales above [[16]](#ref-16).
- **Response.** The chosen strategy plus the specific action. For threats, the strategies are **avoid,
  mitigate/reduce, transfer, accept** - *"eliminating the threat or protecting the project from its impact"*,
  *"decreasing the probability of occurrence or impact"*, *"shifting the impact of a threat to a third
  party"*, and *"not taking any action unless the risk occurs"* respectively [[17]](#ref-17). PMBOK 6 (2017)
  added **escalate** as a fifth, for risks whose response is above the team's authority [[17]](#ref-17). For
  opportunities the mirror strategies are the same five: **escalate, exploit, share, enhance, accept** -
  exploit is *"ensuring that an opportunity occurs"*, and escalate applies to opportunities beyond the team's
  authority just as it does to threats [[17]](#ref-17).
- **Owner.** *"A named individual, not a team or a job title without a person in it"* [[14]](#ref-14). PRINCE2
  splits this into two roles worth keeping straight: the **risk owner** *"is responsible for managing and
  monitoring"* the risk, while the **risk actionee** *"is assigned to carry out a particular action and they
  support the risk owner... not responsible for monitoring or managing the risk"* [[4]](#ref-4). On small
  efforts the two collapse into one person; on large programs they split.
- **Status.** A small controlled set - for example Open, In Mitigation, Escalated, Accepted, Closed
  [[15]](#ref-15).

**The dual-score pattern (full variant).** Mature registers carry **two** scores per risk: **inherent**
(before any controls) and **residual** (after your existing controls operate). This is *"the most
consequential distinction among the key elements of a risk register"* [[13]](#ref-13), because the residual
score is *"the figure reported to leadership"* [[14]](#ref-14) and the gap between inherent and residual is
the only on-register evidence that your controls are doing anything. A register with a single score cannot
show whether its mitigations work.

**The trigger / key risk indicator (full variant).** A row can carry *"observable, measurable events or
thresholds indicating materialization, converting registers into early-warning systems"* [[13]](#ref-13)
instead of leaving the register as a document you re-read on a calendar. The trigger is also how you
pre-decide the moment a risk becomes an issue (see section 8).

### Review and Ownership

**What it is:** the cadence on which the register is reviewed, who owns it, and how risks escalate. **Why it
exists:** because the register's defining failure mode is going stale - *"out-of-date scoring is one of the
most common risk register failures in practice"* [[21]](#ref-21). Reviews are both calendar-based (a steering
or governance rhythm) and event-triggered (a KRI breach, a control failure). Reporting is **audience-tiered**:
*"operational managers need entry-level detail for action, risk committees require portfolio-level trend
analysis, and boards need executive summaries showing risks exceeding tolerance"* [[20]](#ref-20).

---

## 4. Variants and sizing

**Lean** is the smallest register that is still a real register: **Purpose and Scope**, a lightweight
**Scoring Scale**, the **Risks** table (ID, statement, likelihood, impact, score, response, owner, status),
and **Review and Ownership**. It is a complete working risk register for a single team or project that needs
to track and act on its risks without governance overhead.

**Full** is a strict superset. It keeps all four lean sections in order and adds: an expanded **Scoring
Scale** (the full 5x5 heatmap and the inherent-versus-residual method); extra table columns (category,
inherent and residual scores, trigger/KRI, proximity, last-reviewed); an **Escalation and Risk Appetite**
section (the thresholds at which a risk is escalated and the tolerance it is judged against); and a **Closed
and Materialized Risks** section (the audit trail, including risks that became issues) [[9]](#ref-9)[[20]](#ref-20).

**The scaling signal is governance and audience, not project size.** Use lean when one team acts on its own
risks. Move to full when a steering committee or auditor consumes the register, when you must demonstrate
control effectiveness (which requires the dual score), or when regulation prescribes fields you must carry
[[9]](#ref-9)[[20]](#ref-20). The UK government's project guidance is an example of the full end: it mandates
unique IDs, cause-event-impact descriptions, current and target ratings, response categories, and residual
ratings, noting that *"proprietary or organisational tools usually prescribe similar data"* [[9]](#ref-9).

---

## 5. Methodology lineage

Different schools treat the register differently, and knowing which one you are in tells you which fields are
mandatory and which are optional.

- **PMBOK / PMI.** The register is the named output of the Identify Risks process and is progressively
  elaborated across qualitative analysis, quantitative analysis, response planning, and monitoring
  [[7]](#ref-7)[[8]](#ref-8). PMBOK 6 (2017) defined seven risk processes; PMBOK 7 (2021) moved to a
  principles model and repositioned the register from a mandatory output to a commonly used artifact.
- **ISO 31000:2018.** A principles-and-framework standard whose purpose is *"creating and protecting value"*
  [[30]](#ref-30). Critically, **it does not mandate a risk register**: it requires that risk be identified,
  analyzed, evaluated, treated, and monitored, and leaves the documentation form to the organization
  [[1]](#ref-1)[[3]](#ref-3). "ISO 31000 alignment" on a register usually means "consistent with its
  principles," not "these columns come from the standard."
- **PRINCE2 / M_o_R (now PRINCE2 Risk Management).** The most prescriptive about the register as a named
  management product. It defines a specific field set (identifier, author, date, category, cause-event-effect
  description, probability, impact, proximity, response, owner, actionee, status) and a governing "risk
  management approach" document that *"will outline the configuration and usage of the risk register"*
  [[4]](#ref-4). PRINCE2 uniquely carries a **proximity** field (when a risk is expected to materialize).
- **COSO ERM (2017).** A board-and-strategy framework, not a project one. It reframes risk as intrinsic to
  strategy and performance [[31]](#ref-31); its identification and assessment activities are where a
  register-like artifact lives, though COSO's own text works at the framework level rather than prescribing a
  named register document. Reach for COSO's framing when your audience is an audit committee, not a delivery
  team.
- **Agile and lean.** The most skeptical camp. Mike Cohn argues that *"a great deal of explicit risk
  management becomes unnecessary when a project uses an agile approach"* because short iterations surface and
  retire risk continuously, and that for small-to-medium projects *"the likely savings from explicitly
  managing risks is outweighed by the cost of explicitly managing risk"* [[28]](#ref-28). The countervailing
  practitioner position, from ISACA, is that even in agile *"risk should be recorded in a register"*, just
  supplemented with visual tools like risk-burndown charts and the "what-why" identification technique
  [[29]](#ref-29). The split is by scale and regulation, not ideology (section 6).

---

## 6. Debates and contested boundaries

**The central fault line is whether the likelihood-times-impact score is sound.** This is not a fringe
complaint; it is a credentialed, unresolved argument, and a template that pretends otherwise is not honest.

**The case against.** Tony Cox's *"What's Wrong with Risk Matrices?"* (Risk Analysis, 2008) makes the
mathematical case that matrices have poor resolution, can assign higher ratings to objectively lower risks,
and *"cannot"* rationally allocate resources: *"Effective allocation of resources to risk-reducing
countermeasures cannot be based on the categories provided by risk matrices"* [[23]](#ref-23). For risks
where frequency and severity are negatively correlated, he concludes matrices can be *"worse than useless"* -
worse than random [[23]](#ref-23). Hubbard and Evans (IBM Journal, 2010) add the empirical companion: ordinal
labels have poor inter-rater reliability, and multiplying them (a "3" times a "2") produces a number that
looks like arithmetic but is not, because ordinal labels are names, not quantities [[24]](#ref-24) (described
via secondary syntheses; the IEEE full text is paywalled and was not read). Hubbard's
book *The Failure of Risk Management* generalizes this: popular heat-map and 1-5 scoring methods can be worse
than doing nothing, because they manufacture false confidence [[33]](#ref-33). Norman Marks lands the
governance version: a typical register is *"a static list of risks, updated occasionally"* whose ratings
prompt the question *"what the devil does a 'high' rating mean?"* [[25]](#ref-25), and Tim Clements names the
organizational result "risk theater" - *"compliance does not equal security"* [[26]](#ref-26).

**The case for.** Julian Talbot's direct rebuttal is that *"risk matrices are still one of the best practical
tools that we have"* and that *"most of the flaws listed above only exist if risk matrices are used in
isolation, which is rarely the case"* [[27]](#ref-27). A matrix used as a **discussion scaffold** - to force
a cross-functional conversation about what could go wrong and get a shared, rough ordering - delivers value
the math critique does not touch. Wikipedia's balanced note agrees: *"If used with common sense, risk
registers are a useful tool to stimulate cross-functional debate"* [[1]](#ref-1).

**Where this bundle lands.** Both camps are right about different things, and the template is built for the
synthesis: **anchor the scales** so "high" means something specific [[16]](#ref-16)[[26]](#ref-26); **use the
score to drive discussion and triage**, not as a precise measurement [[27]](#ref-27); and for high-stakes
decisions, **escalate to quantification** rather than trusting the heat map. The leading quantitative
alternative is **FAIR** (Factor Analysis of Information Risk), which replaces red-amber-green buckets with
*"probable frequency and probable magnitude of future loss"* expressed in monetary ranges [[32]](#ref-32).
FAIR is strongest in cyber and financial risk and is itself criticized for demanding data most organizations
cannot supply; it is the right tool for the few decisions that justify the cost, not the default for a whole
register.

**The other live debate: does agile need a register at all?** Covered in section 5. The honest answer is
scope-dependent: a single agile team may not; a multi-team or regulated program still does, because shared,
auditable risk visibility is exactly what sprint retrospectives do not provide [[28]](#ref-28)[[29]](#ref-29).

**A smaller but real one: "risk register" versus "risk log."** Some organizations use them interchangeably;
others treat a "log" as lighter. ISO does not adjudicate this; the terms are organization-specific
[[1]](#ref-1).

---

## 7. Anti-patterns and failure modes

1. **The set-and-forget register (risk theater).** Created at kickoff, filed, never revisited. The register's
   signature failure; the fix is a stated review cadence and event triggers, so *"out-of-date scoring"* never
   becomes the norm [[21]](#ref-21)[[26]](#ref-26).
2. **Unanchored ratings.** "High" and "low" with no defined scale behind them, which reduces the score to
   *"saying an investment is 'big' or 'small'"* [[26]](#ref-26). Anchor every level.
3. **Theme labels instead of risk statements.** A row that says "security" or "budget" cannot be scored,
   owned, or acted on. Write a cause-event-consequence sentence [[11]](#ref-11).
4. **No owner, or a team as owner.** A risk owned by "Engineering" is owned by no one. Name an individual
   [[14]](#ref-14).
5. **Inherent-only scoring.** Recording risk before controls but never after, so the register cannot show
   whether its mitigations work. Carry the residual score [[13]](#ref-13)[[14]](#ref-14).
6. **The register that has quietly become an issue log.** Rows describing things that have already happened
   are issues, not risks, and belong in a separate log; mixing them hides which entries need action now
   versus watching [[19]](#ref-19)[[21]](#ref-21).
7. **Objective-disconnected risks.** A list of bad things with no link to the objective they threaten, which
   is Marks's core critique - *"managing a list of what could go wrong is not the same as considering how
   best to achieve objectives"* [[25]](#ref-25).

---

## 8. Relationships to other artifacts

**Risk register vs RAID log.** A RAID log tracks **R**isks, **A**ssumptions, **I**ssues, and **D**ependencies
in one working document; the risk register is the deepened, standalone form of its **R** column. The choice
is by audience and cadence: *"RAID logs operate on a weekly cycle for program teams as working documents;
risk registers follow quarterly reviews for steering committees as governance artifacts"* [[18]](#ref-18).
They feed each other - *"the strategic risks that surface in the weekly RAID review get promoted up"*
[[18]](#ref-18) - and the failure to avoid is *"one bloated artifact"* trying to be both, which *"becomes
unwieldy and ultimately abandoned"* [[18]](#ref-18). This bundle's sibling `raid-log` (the next
governance-docs member to be built) covers the consolidated form; use a standalone register when the R has
outgrown the RAID.

**Risk register vs issue log.** The distinction is temporal: *"risk registers track conditions that might
happen; issue logs address conditions that have happened"* [[19]](#ref-19). When a risk materializes it
*"stops being a risk and becomes an issue"* and moves to the issue log [[19]](#ref-19); the discipline is to
*"decide in advance what conditions will trigger transitioning a risk to the issue log"* [[19]](#ref-19) -
which is exactly what the trigger/KRI field records. Log them separately so you can *"distinguish potential
threats from active incidents"* [[21]](#ref-21).

**Risk register vs risk management plan.** The plan (PRINCE2's "risk management approach") is the strategy
that governs the register: it sets the categories, scales, appetite, and roles, and *"will outline the
configuration and usage of the risk register"* [[4]](#ref-4). The plan is the rules; the register is the
play.

**Risk register vs risk breakdown structure (RBS).** The RBS is *"a hierarchically organised depiction of the
identified project risks arranged by category"* [[22]](#ref-22) - a taxonomy used during identification to
prompt completeness. Its categories become the **category** field on the register [[22]](#ref-22).

**Risk register vs KPI dashboard.** Both are standing governance instruments in this family, but they face
opposite directions: the register tracks **threats to** an objective, the dashboard tracks **progress toward**
it. In the worked example they cover the same program, and a risk that materializes shows up as a dip on the
dashboard it threatened. The `kpi-dashboard` sibling is a forthcoming governance-docs member.

---

## 9. Adaptations

- **Regulated industries (finance, health, safety).** The register becomes an audit artifact: expect
  mandated fields (unique IDs, residual ratings, control mapping), formal appetite statements, and retained
  history. The UK government field set is a representative template [[9]](#ref-9), and the audience-tiered
  reporting model (operational / committee / board) is the norm [[20]](#ref-20).
- **Enterprise risk (COSO ERM).** At the board level the register connects to strategy and performance
  rather than to a single project; the framing shifts from "project threats" to "risks to enterprise
  objectives," and identification/assessment feed a portfolio view [[31]](#ref-31).
- **Cyber and high-stakes financial risk.** Where a decision justifies the cost, replace or supplement the
  qualitative score with **FAIR**-style quantification (loss frequency x loss magnitude, in dollars)
  [[32]](#ref-32).
- **Agile teams.** Keep the register lightweight and living: a single team can run the lean variant, refreshed
  each iteration and supplemented with visual tools, rather than a heavy governance document [[28]](#ref-28)[[29]](#ref-29).
- **Solo or small projects.** Collapse the owner and actionee into one person [[4]](#ref-4), skip the dual
  score, and keep the lean four sections.

---

## 10. Worked example

[`risk-register_example.md`](risk-register_example.md) is a full-variant risk register for the Acme Analytics
**Reporting Platform Modernization** program - the same program whose delivery work the delivery-docs family
examples cover. It demonstrates cause-event-consequence statements, inherent-versus-residual scoring, named
owners and actionees, response strategies including one opportunity and one escalation, triggers that double
as issue-log hand-off conditions, and an escalation-and-appetite section. Its risks, owners, and residual
scores are the ones the forthcoming sibling `raid-log` and `kpi-dashboard` examples will chain onto, so the
three read as one program's governance surface.

---

## References

<a id="ref-1"></a>[1] Wikipedia contributors. "[Risk register](https://en.wikipedia.org/wiki/Risk_register)." Wikipedia (accessed 2026-07-22). Supports the general definition, the ISO Guide 73:2009 attribution, the note that ISO 31000 does not use the term, and the academic criticism of ritualistic use ("a document used as a risk management tool and to fulfill regulatory compliance, acting as a repository for all risks identified"; "ISO 31000:2009 addresses risk documentation... but doesn't specifically use the term 'risk register'"; "ISO 73:2009 defines it as 'a record of information about identified risks.'"; "If used with common sense, risk registers are a useful tool to stimulate cross-functional debate."; "risk registers can lead to 'ritualistic decision-making' and 'illusion of control.'"). [reference]

<a id="ref-2"></a>[2] International Organization for Standardization. "[ISO Guide 73:2009, Risk management - Vocabulary](https://www.iso.org/standard/44651.html)." ISO (accessed 2026-07-22). Source of the canonical one-line definition of a risk register. **Not retrieved:** the ISO page returned HTTP 403 and was not read; the definition is confirmed and attributed only via the Wikipedia citation [[1]](#ref-1), and no claim rests on the ISO text directly. [primary]

<a id="ref-3"></a>[3] Wikipedia contributors. "[ISO 31000](https://en.wikipedia.org/wiki/ISO_31000)." Wikipedia (accessed 2026-07-22). Supports the publication dates, the "effect of uncertainty on objectives" redefinition, and that the standard does not require a register artifact ("risk is now defined as the 'effect of uncertainty on objectives' rather than merely 'chance or probability of loss,' encompassing both negative and positive consequences of uncertainty"; "risk registers, control frameworks, or compliance procedures"). [reference]

<a id="ref-4"></a>[4] PRINCE2 wiki. "[Risk practice](https://prince2.wiki/practices/risk/)." prince2.wiki (accessed 2026-07-22). Supports the PRINCE2 register field list, the risk owner vs actionee distinction, and the risk management approach as the governing document ("The risk owner is responsible for managing and monitoring risks aspects. They can also carry out actions that have been assigned to them."; "The risk actionee is someone who is assigned to carry out a particular action and they support the risk owner. So, they are not responsible for monitoring or managing the risk."; "The risk management approach document will outline the configuration and usage of the risk register, providing guidance on how it should be managed throughout the project."). [reference]

<a id="ref-5"></a>[5] PRINCE2 wiki. "[Risk register (management product)](https://prince2.wiki/management-products/project-log/risk-register/)." prince2.wiki (accessed 2026-07-22). Supports PRINCE2's canonical purpose statement for the register ("The risk register aims to capture and maintain information on identified threats and opportunities related to the project, supporting the practical application of the risk practice."; "a central record of project risks, providing details on their status, history, response actions, and ownership"). [reference]

<a id="ref-6"></a>[6] PRINCE2.com. "[The risk register: what to include and what to avoid](https://www.prince2.com/usa/blog/the-risk-register-what-to-include-and-what-to-avoid)." PRINCE2.com (PeopleCert), USA (accessed 2026-07-22). Supports the practitioner-level definition and that a register tracks both threats and opportunities with an assigned owner ("A risk register is a central record of all identified risks that could affect a project's objectives. It tracks both threats and opportunities, ensuring that each is logged, analysed, and assigned an owner responsible for managing it."). [primary]

<a id="ref-7"></a>[7] 4squareviews. "[6th Edition PMBOK Guide - Process 11.2 Identify Risks: Outputs](https://4squareviews.com/2018/08/01/6th-edition-pmbok-guide-process-11-2-identify-risks-outputs/)." 4squareviews (accessed 2026-07-22). Practitioner commentary paraphrasing PMBOK 6; supports the register as the primary output of Identify Risks, progressively elaborated ("created in one process, but is elaborated on during other processes throughout the course of the project"). [practitioner]

<a id="ref-8"></a>[8] 4squareviews. "[6th Edition PMBOK Guide - Chapter 11 Risk Management: Key Concepts](https://4squareviews.com/2018/07/09/6th-edition-pmbok-guide-chapter-11-risk-management-key-concepts/)." 4squareviews (accessed 2026-07-22). Supports the PMBOK definition of a project risk and the seven-process structure ("An uncertain event or condition that, if it occurs, has a positive or negative effect on one or more project objectives"). [practitioner]

<a id="ref-9"></a>[9] UK Government (Infrastructure and Projects Authority / Cabinet Office). "[Chapter 20: Risk Management](https://projectdelivery.gov.uk/teal-book/home/part-e-planning-and-control/chapter-20-risk-management/)." Project Delivery Functional Standard (the Teal Book) (accessed 2026-07-22). Primary-source specification of a government-mandated register field set and evidence that frameworks converge on the same fields ("Proprietary or organisational tools usually prescribe similar data to provide consistency and collation of risks"). [primary]

<a id="ref-10"></a>[10] Tecknologia. "[M_o_R Management of Risk](https://www.tecknologia.co.uk/concepts/management-of-risk)." Tecknologia (PeopleCert authorized training partner) (accessed 2026-07-22). Supports M_o_R's 2002 OGC origin in response to the Turnbull Report, the neutral (threat-and-opportunity) concept of risk, and the 2024 rebrand to PRINCE2 Risk Management ("Risk is a neutral concept; risks can either be threats (downside risks) or opportunities (upside risks)."). [practitioner]

<a id="ref-11"></a>[11] Risk Publishing. "[How to describe a risk: the cause-event-consequence format](https://riskpublishing.com/how-to-describe-a-risk/)." riskpublishing.com (accessed 2026-07-22). Supports the cause-event-consequence risk-statement anatomy ("Because of [cause], there is a risk that [event], which could lead to [consequence]."). [practitioner]

<a id="ref-12"></a>[12] Risk Publishing. "[How to write a good risk statement](https://riskpublishing.com/how-to-write-a-good-risk-statement/)." riskpublishing.com (accessed 2026-07-22). Supports the If-Then and Condition-Consequence statement templates, the 4Cs quality test, and the ISO 31000 definition of risk ("If [event triggered by cause], then [consequence on objective]."; "Given [condition/cause], there is a risk that [event], leading to [consequence]."; "ISO 31000:2018 defines risk as 'the effect of uncertainty on objectives'"). [practitioner]

<a id="ref-13"></a>[13] Risk Publishing. "[Key elements of a risk register](https://riskpublishing.com/key-elements-of-a-risk-register/)." riskpublishing.com (accessed 2026-07-22). Supports the inherent-vs-residual distinction as the most consequential and the risk trigger as an early-warning element ("The most consequential distinction among the key elements of a risk register is between inherent risk and residual risk."; "Observable, measurable events or thresholds indicating materialization, converting registers into early-warning systems"). [practitioner]

<a id="ref-14"></a>[14] Initia Risk. "[Risk register: definition, examples and structure](https://initiarisk.com/resources/what-is-a-risk-register)." initiarisk.com (accessed 2026-07-22). Supports risk owner as a named individual and the residual score as the figure reported to leadership ("a named individual, not a team or a job title without a person in it"; "Risk exposure after controls operate; the figure reported to leadership"). [practitioner]

<a id="ref-15"></a>[15] Rocketlane. "[Risk register template](https://www.rocketlane.com/blogs/risk-register-template)." rocketlane.com (accessed 2026-07-22). Supports a status-value set and that threshold color bands are a practitioner choice, not a standard ("A specific statement of what could go wrong, naming the trigger, affected workstream, and consequence"). Its band boundaries (1-7 / 8-14 / 15-25) differ from other sources; banding is a local choice. [vendor]

<a id="ref-16"></a>[16] SafetyCulture. "[What is a 5x5 risk matrix and how to use it](https://safetyculture.com/topics/risk-assessment/5x5-risk-matrix/)." safetyculture.com (accessed 2026-07-22). Supports the 5x5 matrix, the Risk = Probability x Impact formula, and anchored likelihood/impact labels ("Risk Level = Probability x Impact"; "Probability 4 x Impact 3 = Risk Score 12"). Its color-zone thresholds are specific to the ISO 45001 safety context and are not the project/enterprise norm. [vendor]

<a id="ref-17"></a>[17] Project Management Academy. "[Strategies for risk response](https://projectmanagementacademy.net/resources/blog/strategies-for-risk-response/)." projectmanagementacademy.net (accessed 2026-07-22). Supports the five threat strategies and five opportunity strategies, PMBOK-sourced ("Eliminating the threat or protecting the project from its impact."; "Shifting the impact of a threat to a third party."; "Decreasing the probability of occurrence or impact of a threat."; "Not taking any action unless the risk occurs."; "Ensuring that an opportunity occurs."). The five-strategy model (with "escalate") is PMBOK 6 (2017)+; earlier practice and ISO 31000 use the classic four. [practitioner]

<a id="ref-18"></a>[18] DirectorPM. "[RAID log vs risk register: when to use which](https://directorpm.com/blog/raid-log-vs-risk-register)." directorpm.com (accessed 2026-07-22). Supports the register as the "R" of RAID, the audience/cadence split, the feed direction, and the one-bloated-artifact failure ("RAID log feeds the risk register. The strategic risks that surface in the weekly RAID review get promoted up."; "The most common failure involves 'one bloated artifact' attempting both functions, which becomes unwieldy and ultimately abandoned."; "RAID logs operate on a weekly cycle for program teams as working documents; risk registers follow quarterly reviews for steering committees as governance artifacts."). [practitioner]

<a id="ref-19"></a>[19] Hopper, Tom. "[Issue logs and risk registers](https://tomhopper.me/2014/04/11/issue-logs-and-risk-registers/)." tomhopper.me (accessed 2026-07-22). Supports the temporal risk-vs-issue distinction and pre-deciding the transition trigger ("When something goes wrong - deviates from the plan - it stops being a risk and becomes an issue that must be addressed to ensure success."; "Risk registers track conditions that might happen; issue logs address conditions that have happened."; "Effective risk management requires deciding in advance what conditions will trigger transitioning a risk to the issue log."). [practitioner]

<a id="ref-20"></a>[20] DestCert. "[Risk register best practices (CRISC)](https://destcert.com/resources/crisc-risk-register)." destcert.com (accessed 2026-07-22). Supports the register as a documented governance position and audience-tiered reporting ("A risk register is not a list of things that could go wrong. It is your organization's documented position on every significant risk it has chosen to accept, treat, transfer, or avoid."; "Organizations must tailor register reporting to different audiences: operational managers need entry-level detail for action, risk committees require portfolio-level trend analysis, and boards need executive summaries showing risks exceeding tolerance and governance decisions made on high-significance exposures."). [practitioner]

<a id="ref-21"></a>[21] SureCloud. "[Complete guide to risk registers](https://www.surecloud.com/resource-hub/risk-registers-guide)." surecloud.com (accessed 2026-07-22). Supports the living-tool discipline, out-of-date scoring as the common failure, and register-vs-issue separation ("Out-of-date scoring is one of the most common risk register failures in practice."; "Treat registers as living tools, not filing cabinets."; "Risks can turn into issues, but they should be logged and managed separately so you can distinguish potential threats from active incidents."). [vendor]

<a id="ref-22"></a>[22] Wikipedia contributors. "[Risk breakdown structure](https://en.wikipedia.org/wiki/Risk_breakdown_structure)." Wikipedia (accessed 2026-07-22). Supports the RBS as a hierarchical category taxonomy feeding the register and its PMI Practice Standard origin ("A Risk Breakdown Structure (RBS) is 'a hierarchically organised depiction of the identified project risks arranged by category.'"; "The Project Management Institute (PMI) developed the RBS as part of its Practice Standard for Risk Management."). [reference]

<a id="ref-23"></a>[23] Cox, Louis Anthony (Tony) Jr. "[What's Wrong with Risk Matrices?](https://pubmed.ncbi.nlm.nih.gov/18419665/)" Risk Analysis, vol. 28, no. 2 (2008); PubMed abstract (accessed 2026-07-22). Supports the mathematical case that risk matrices have structural flaws ("worse than useless"; "Effective allocation of resources to risk-reducing countermeasures cannot be based on the categories provided by risk matrices"). Only the PubMed abstract was read, not the full paper; the "in isolation" premise is contested by Talbot [[27]](#ref-27). [primary]

<a id="ref-24"></a>[24] Hubbard, Douglas W. and Evans, Dylan. "[Problems with scoring methods and ordinal scales in risk assessment](https://ieeexplore.ieee.org/document/5464409/)." IBM Journal of Research and Development, vol. 54, no. 3 (2010) (accessed 2026-07-22). Supports the empirical case that ordinal scoring's perceived value is largely illusory and inter-rater reliability is poor. **Url-confirmed, not read:** the IEEE page resolves but the full text is paywalled; the argument is reported via secondary syntheses and carries no verbatim quote. [primary]

<a id="ref-25"></a>[25] Marks, Norman. "[What is wrong with a typical risk register?](https://normanmarks.wordpress.com/2021/01/10/what-is-wrong-with-a-typical-risk-register/)" Norman Marks on Governance, Risk Management, and Internal Audit (accessed 2026-07-22). Supports the governance/internal-audit critique of static, objective-disconnected registers ("It is a static list of risks, updated occasionally. Managing a list of what could go wrong is not the same as considering how best to achieve objectives."; "These are risks to what and what the devil does a 'high' rating mean?"). [practitioner]

<a id="ref-26"></a>[26] Clements, Tim. "[Risk theatre: stop the compliance charade before it costs you](https://www.purposeandmeans.io/risk-theatre-stop-the-compliance-charade-before-it-costs-you/)." Purpose and Means (accessed 2026-07-22). Supports the "risk theater" critique and the emptiness of unanchored categorical labels ("Saying a risk is 'high' or 'low' is like saying an investment is 'big' or 'small.'"; "compliance does not equal security"). Draws on UK financial-services observation, not a systematic study; Feb 2025. [practitioner]

<a id="ref-27"></a>[27] Talbot, Julian. "[What's right with risk matrices?](https://www.juliantalbot.com/post/2018/07/31/whats-right-with-risk-matrices)" juliantalbot.com (accessed 2026-07-22). Supports the mainstream rebuttal to Cox: matrices as a discussion scaffold, valuable when not used in isolation ("risk matrices are still one of the best practical tools that we have"; "most of the flaws listed above only exist if risk matrices are used in isolation, which is rarely the case"). [practitioner]

<a id="ref-28"></a>[28] Cohn, Mike. "[Managing risk on agile projects with the risk burndown chart](https://www.mountaingoatsoftware.com/blog/managing-risk-on-agile-projects-with-the-risk-burndown-chart)." Mountain Goat Software (accessed 2026-07-22). Supports the agile argument that iterative delivery makes much explicit register work unnecessary for small-to-medium projects ("a great deal of explicit risk management becomes unnecessary when a project uses an agile approach."; "for these projects the likely savings from explicitly managing risks is outweighed by the cost of explicitly managing risk"). Contested by ISACA [[29]](#ref-29) for large or regulated programs. [practitioner]

<a id="ref-29"></a>[29] ISACA. "[Risk management in agile projects](https://www.isaca.org/resources/isaca-journal/issues/2016/volume-2/risk-management-in-agile-projects)." ISACA Journal, 2016 vol. 2 (accessed 2026-07-22). Supports that even agile projects should keep a register and the what-why identification technique ("risk should be recorded in a register"; "The what-why approach entails a group brainstorming session to discover what might occur in a project followed by an analysis of why each event may occur"). 2016; agile risk tooling has evolved since. [practitioner]

<a id="ref-30"></a>[30] ISO Technical Committee TC 262. "[ISO 31000:2018 Risk Management](https://committee.iso.org/sites/tc262/home/projects/published/iso-31000-2018-risk-management.html)." iso.org (accessed 2026-07-22). Custodian-committee page supporting the 2018 purpose framing and the changes from 2009 ("creating and protecting value as the key driver of risk management"; "continual improvement, the inclusion of stakeholders, being customized to the organization and consideration of human and cultural factors"). [primary]

<a id="ref-31"></a>[31] ERM Initiative, Poole College of Management, NC State University. "[COSO's ERM framework](https://erm.ncsu.edu/resource-center/cosos-erm-framework/)." erm.ncsu.edu (accessed 2026-07-22). Supports COSO ERM 2017's five components and its governance/strategy framing, context for how enterprise risk differs from a project register ("ongoing identification and sharing of risk and strategy information"). [practitioner]

<a id="ref-32"></a>[32] Wikipedia contributors. "[Factor analysis of information risk (FAIR)](https://en.wikipedia.org/wiki/Factor_analysis_of_information_risk)." Wikipedia (accessed 2026-07-22). Supports FAIR as the leading quantitative alternative (Jack Jones, 2005) and its risk definition ("probable frequency and probable magnitude of future loss"). [reference]

<a id="ref-33"></a>[33] Hubbard, Douglas W. *The Failure of Risk Management: Why It's Broken and How to Fix It.* Wiley, 2009 (2nd ed. 2019). Named as the canonical source of the argument that popular heat-map and 1-5 scoring methods can be worse than doing nothing by creating false confidence. **Not retrieved** (book, not fetched); it carries no verbatim quote here, and the specific mechanism is cited via [[24]](#ref-24) and secondary practitioner syntheses. [primary]
