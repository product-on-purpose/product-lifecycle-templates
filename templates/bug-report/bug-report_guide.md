# Guide: Bug Report (operator card)

The short card. Why the document is shaped this way, and the argument behind every rule here, is in
[`bug-report_companion.md`](bug-report_companion.md). A fully worked instance is
[`bug-report_example.md`](bug-report_example.md).

## When to use

- Something behaved differently from what you expected, and someone other than you will have to look at it.
- The fix will outlive your working memory: a different sprint, a different team, a different person.
- Someone outside the team reported it. Their report needs a home even if the fix takes ten minutes.
- The defect affects a release decision, so its severity has to be visible to whoever holds the gate.
- The work is regulated or audited and the closed record is evidence.

## When NOT to use

- **You can fix it now, alone, today, and nobody outside the team saw it.** Fix it. A report you write and
  close yourself in the same hour is overhead, not process.
- **It is a request, not a defect.** If nothing promised the behavior you want, that is a change request. The
  working test: a defect means the software does not work the way it says it will; an enhancement means it
  does not work the way someone wants.
- **It is a live production incident.** Get service back first. Incident response and defect management have
  different goals; the bug report comes after, or alongside, and is not the thing that restores service.
- **It is really three problems.** File three. One report, one defect, or it can never be closed.
- **You want a postmortem.** A postmortem covers an event: timeline, contributing factors, actions. A bug
  report covers one flaw and is usually an input to one.

## Report the anomaly, not the diagnosis

The standards do not call this a bug report. They call it an **anomaly report** or an **incident report**,
because at the moment you write it nobody knows whether the cause is a code flaw, a configuration, stale
data, or a misunderstanding of what the software was supposed to do.

That is not pedantry, it is practical advice about how to write the thing. Report what you observed and what
you expected. If you have a theory, label it as a theory and put it last. Reports that lead with a diagnosis
get argued with; reports that lead with a reproduction get fixed.

## Pick a variant

**Lean (four sections)** is the intake form: Summary, Steps to Reproduce, Expected and Actual Behavior,
Environment and Reproducibility. **Use this for anything a non-tester will fill in.** Every field beyond these
four costs you reports from support agents, salespeople and users, and the elements you most want are already
the expensive ones.

**Full (eight sections)** adds Evidence, Impact/Severity/Priority, Triage and Ownership, and Resolution and
Regression Guard. Three of those four are filled in **by other people, after filing** - which is the real
split. Lean is what arrives; full is what the record becomes.

Use full when the defect is tracked formally: a release gate reads its severity, ownership crosses teams, or
the closed record is audit evidence.

## Severity is not priority

| | Means | Usually set by | Example |
|---|---|---|---|
| **Severity** | How much damage it does | QA or the reporting team | Data exposed across an entitlement boundary: high |
| **Priority** | How soon it must be fixed | Product manager or triage | Cosmetic error on the launch homepage: high |

The two crossing cases are the proof they are independent:

- **High severity, low priority.** A crash in a rarely used legacy path. Maximum damage, minimal exposure.
- **Low severity, high priority.** A misspelled word on the homepage during a launch. No damage, maximum
  visibility.

Two honest caveats. The **ownership rule above is convention, not standard** - the certification glossary
defines both terms and says nothing about who assigns them. And there is **no standard severity scale**:
four, five and six-level scales are all in daily use, and S1-S4 numbering means different things in different
places. Pick one, define the levels in words, and put the definitions where reporters can see them.

**If your tracker has only one field**, which is common - Jira removed its Severity field deliberately, on
the grounds that it confused business users - decide as a team whether that field means damage or urgency,
write the decision down, and stop relitigating it per ticket.

## Quality rubric (self-grade)

Score each 0, 1 or 2. Under 10 out of 16 and the report will come back with questions instead of a fix.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Reproducible** | No steps | Steps that start mid-flow | Numbered steps from a named starting state |
| 2 | **Expected stated** | Missing | Implied | Stated explicitly, with where the expectation comes from |
| 3 | **Actual stated** | Vague ("wrong") | Described | Precise and observable, with the value or message |
| 4 | **One defect** | Several bundled | Mostly one | Exactly one, closeable on its own |
| 5 | **Environment** | Not given | Partial | Build, environment, account and configuration |
| 6 | **Reproducibility rate** | Not mentioned | "Sometimes" | A count: n out of m attempts |
| 7 | **Observation, not diagnosis** | Leads with a cause | Mixed | Observation first, theory labeled and last |
| 8 | **Tone** | Blames a person | Neutral-ish | Describes system behavior only |

## Named anti-patterns (the usual wrecks)

1. **No expected behavior.** The most common real defect in real reports. The reader cannot tell whether the
   software is wrong or you are.
2. **The diagnosis report.** "The cache is broken" when what you saw was a stale number. If the theory is
   wrong, you have sent the reader down your wrong path.
3. **Steps that start in the middle.** No account, no data, no configuration, and a "works for me" close.
4. **The everything-report.** Three problems in one ticket. It can never be closed.
5. **Blaming the developer.** Costs you the collaborative fix and gets you a defensive one.
6. **Severity as a negotiating position.** Inflating severity corrupts the only signal a release gate reads,
   and once counts or caps are watched it becomes systematic.
7. **Reopening a closed bug for a regression.** Open a new one and link it, or you lose the record of what
   the original fix actually did.
8. **Closing "cannot reproduce" as though that settled it.** It is a large studied category with many
   causes; linking related reports is a documented way to make progress on it.
9. **Counting bugs.** The moment defect counts become targets they get gamed: one bug split into five
   tickets, trivial bugs filed to hit quotas, relabeling to stay under a severity cap.

## Pairing with a skill

`pairs_with: [deliver-edge-cases]`. There is **no testing or QA skill** in the `pm-skills` library (finding
EC-4 in the repository's `STATE.md`), and the fit here is looser than for this bundle's two siblings: an
edge-case catalog is written before the fact and a bug report after it. The honest connection is that a
defect found in the wild is evidence the failure surface was under-mapped, and it is worth feeding back into
the catalog. Everything in this template is filled by hand.
