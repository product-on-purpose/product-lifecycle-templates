// what-it-is:   the EV-1 efficacy eval harness
// what-it-does: runs three arms (treatment, control, hollow) over the scenario bank and scores them blind
// why:          the library's quality claim is argued, not measured; this is the attempt to measure it
//               without publishing a number a skeptic can take apart
// used-by:      run with the Workflow tool: Workflow({ scriptPath: "evals/harness/output-eval.workflow.mjs" })
//               pass { types: [...], scenarios: [...] } as args to narrow the run
//
// READ docs/internal/eval-protocol.md BEFORE CHANGING ANYTHING HERE. Several choices in this file look
// like they could be simplified and cannot: the hollow arm, the equal-length truncation, the randomised
// arm order, and the absolute-failure-first verdict ordering each close a specific way the number could
// be wrong, and each is named in that document with the threat it answers.

export const meta = {
  name: 'ev1-output-eval',
  description: 'Three-arm blind efficacy eval over the template bundles',
  phases: [
    { title: 'Generate', detail: 'treatment, control and hollow arms per scenario' },
    { title: 'Judge', detail: 'blind panel scores every arm on rubric, held-out and probes' },
  ],
}

const REPO = 'E:/Projects/product-on-purpose/product-lifecycle-templates'

// The pilot set. Deliberately three bundles chosen for contrast, not coverage: a large scaffolded
// document, a small rule-shaped one, and a narrative one. See eval-protocol.md section 8.
const DEFAULT_SCENARIOS = [
  { id: 'prd-001', type: 'prd', hollow: true },
  { id: 'prd-002', type: 'prd', hollow: false },
  { id: 'acceptance-criteria-001', type: 'acceptance-criteria', hollow: true },
  { id: 'acceptance-criteria-002', type: 'acceptance-criteria', hollow: false },
  { id: 'incident-postmortem-001', type: 'incident-postmortem', hollow: true },
  { id: 'incident-postmortem-002', type: 'incident-postmortem', hollow: false },
]

const SCENARIOS = (args && args.scenarios)
  ? DEFAULT_SCENARIOS.filter((s) => args.scenarios.includes(s.id))
  : DEFAULT_SCENARIOS

// T2: both arms are truncated to the same budget under a stated rule, so length alone cannot separate them.
const LENGTH_RULE = 'Keep the finished document under roughly 900 words. This budget is identical for every arm, so length cannot be what separates them. Do not pad, and do not compress past the point of being useful.'

const scenarioPath = (id) => 'evals/scenarios/' + id + '.md'

function briefInstruction(id) {
  return [
    'Read ' + REPO + '/' + scenarioPath(id) + ' and use ONLY its "The ask" and "What you know" sections as your input.',
    'You MUST NOT read its "Retrieval probes" or "Distractors" sections. Those are the answer key. Reading them invalidates this run.',
  ].join('\n')
}

phase('Generate')

const GEN = []
for (const s of SCENARIOS) {
  // T-arm: the template and the guide.
  GEN.push({
    arm: 'T', scenario: s.id, type: s.type,
    prompt: [
      briefInstruction(s.id),
      '',
      'Then read these two files and use them to write the document:',
      '  ' + REPO + '/templates/' + s.type + '/' + s.type + '_template-full.md',
      '  ' + REPO + '/templates/' + s.type + '/' + s.type + '_guide.md',
      '',
      'Fill the template for this situation. Strip every HTML guidance comment from your output; the finished document must contain none.',
      LENGTH_RULE,
      '',
      'Output ONLY the finished document. No preamble, no commentary about what you did.',
    ].join('\n'),
  })

  // C-arm: the versioned strong-generic instruction, and nothing from this library.
  GEN.push({
    arm: 'C', scenario: s.id, type: s.type,
    prompt: [
      briefInstruction(s.id),
      '',
      'You MUST NOT read anything under ' + REPO + '/templates/ . Do not open a template, a guide, a companion or an example. Your value in this run depends on being independent of them.',
      '',
      'Read ' + REPO + '/evals/harness/control-prompt.md and follow the instruction in its "The prompt" section, treating the document type as: ' + s.type,
      LENGTH_RULE,
      '',
      'Output ONLY the finished document. No preamble.',
    ].join('\n'),
  })

  // H-arm: the substance-sensitivity calibration. If judges score this near T, the instrument is
  // measuring form and no number may be published. T1.3 in the measurement-validity pass.
  if (s.hollow) {
    GEN.push({
      arm: 'H', scenario: s.id, type: s.type,
      prompt: [
        'You are producing a deliberate NEGATIVE CONTROL for a measurement-validity check. This is not a trick and it is not sabotage; it is a calibration artifact, and it must be produced honestly.',
        '',
        'Read ' + REPO + '/templates/' + s.type + '/' + s.type + '_template-full.md and reproduce its structure faithfully: every section, in order, with its heading.',
        '',
        'Then fill each section with FLUENT, PROFESSIONAL, GENERIC, LOW-INFORMATION prose. It must read like a competent document at a glance and contain nothing a reader could act on.',
        '  Use no specific numbers, names, dates, systems, or thresholds.',
        '  Make no decision and state no trade-off.',
        '  Prefer confident generalities: "the team will monitor relevant metrics", "stakeholders will be aligned as appropriate".',
        '  Do NOT read the scenario file. This arm is deliberately blind to the situation.',
        '',
        'Strip every HTML guidance comment. ' + LENGTH_RULE,
        '',
        'Output ONLY the document.',
      ].join('\n'),
    })
  }
}

const generated = await parallel(
  GEN.map((g) => () =>
    agent(g.prompt, { label: 'gen:' + g.arm + ':' + g.scenario, phase: 'Generate', model: 'sonnet', effort: 'medium' })
      .then((text) => ({ ...g, text }))
  )
)

const ok = generated.filter(Boolean).filter((g) => typeof g.text === 'string' && g.text.length > 200)
log('generated ' + ok.length + ' of ' + GEN.length + ' artifacts')

phase('Judge')

const SCORE_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['artifacts', 'strongest', 'rationale'],
  properties: {
    artifacts: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['label', 'rubricMean', 'heldOutMean', 'probesAnswered', 'overall', 'notes'],
        properties: {
          label: { type: 'string', description: 'the blind label you were given' },
          rubricMean: { type: 'number', description: 'mean of your 1-5 scores on the rubric criteria' },
          heldOutMean: { type: 'number', description: 'mean of your 1-5 scores on the held-out criteria' },
          probesAnswered: { type: 'integer', description: 'how many of the 5 probes you could answer correctly from this document alone' },
          overall: { type: 'number', description: '1-5 holistic, on the anchor scale' },
          notes: { type: 'string' },
        },
      },
    },
    strongest: { type: 'string' },
    rationale: { type: 'string' },
  },
}

// One judging job per scenario. Each judge sees every arm for that scenario, blind and in a
// per-judge order, so no judge can infer an arm from its position. T4.
const JUDGES = [1, 2, 3]
const byScenario = {}
for (const g of ok) (byScenario[g.scenario] ||= []).push(g)

const judged = await pipeline(
  Object.entries(byScenario),
  ([scenarioId, arms]) => {
    const type = arms[0].type
    return parallel(JUDGES.map((j) => () => {
      // Deterministic per-judge rotation. Math.random is unavailable in workflow scripts, and a fixed
      // rotation is enough: no judge sees the same ordering, and the mapping is recoverable afterwards.
      const rotated = arms.slice(j - 1).concat(arms.slice(0, j - 1))
      const labels = ['A', 'B', 'C', 'D']
      const shown = rotated.map((a, i) => ({ ...a, label: labels[i] }))
      return agent([
        'You are one judge on a blind panel scoring ' + type + ' documents. You do not know how any of these was produced and you must not speculate in your scores.',
        '',
        'Read the rubric at ' + REPO + '/evals/rubrics/' + type + '.md . Apply its anchor scale literally: a 5 is reserved for work a senior practitioner would not touch, solid work with a nitpick is a 4, and when torn between two levels pick the lower.',
        '',
        'Read the scenario at ' + REPO + '/' + scenarioPath(scenarioId) + ' IN FULL, including its probes, so you can check what each document actually delivers.',
        '',
        'ANTI-FORM INSTRUCTION, and it overrides your instinct: a well-organised document that omits the success metric scores BELOW a messy one that states it. Headings, ordering and confident tone are not quality. Do not reward a document for looking like a document. Several of the artifacts below may share a structure; that tells you nothing about which is better.',
        '',
        'The scenario contains DISTRACTOR facts that do not belong in a good document of this type. A document that includes them is not more complete. Penalise it.',
        '',
        'For EACH artifact, report: the mean of your 1-5 scores across the rubric criteria, the mean across the held-out criteria, how many of the five probes you could answer correctly FROM THAT DOCUMENT ALONE, and a holistic 1-5.',
        '',
        shown.map((a) => '===== ARTIFACT ' + a.label + ' =====\n' + a.text).join('\n\n'),
      ].join('\n'), { label: 'judge' + j + ':' + scenarioId, phase: 'Judge', schema: SCORE_SCHEMA, model: 'sonnet', effort: 'high' })
        .then((v) => ({ scenarioId, judge: j, key: shown.map((a) => ({ label: a.label, arm: a.arm })), verdict: v }))
    }))
  }
)

// Un-blind and aggregate.
//
// normLabel exists because of a real failure. The first run produced 33 valid judgments and ZERO
// aggregated rows: the key was built on "A" while judges echoed the heading they were shown and
// returned "Artifact A", so every lookup missed and every arm silently held no data. Match on the
// trailing letter rather than on string equality, and fail loudly if a verdict cannot be un-blinded,
// because a silent miss here turns a completed run into a null result that looks like a finding.
const normLabel = (s) => {
  const m = String(s ?? '').trim().toUpperCase().match(/([A-D])\s*$/)
  return m ? m[1] : null
}

const rows = []
const unmapped = []
for (const perScenario of judged.filter(Boolean)) {
  for (const r of perScenario.filter(Boolean)) {
    const map = Object.fromEntries(r.key.map((k) => [k.label, k.arm]))
    for (const a of r.verdict.artifacts ?? []) {
      const arm = map[normLabel(a.label)]
      if (!arm) { unmapped.push({ scenario: r.scenarioId, judge: r.judge, label: a.label }); continue }
      rows.push({ scenario: r.scenarioId, judge: r.judge, arm, rubric: a.rubricMean, heldOut: a.heldOutMean, probes: a.probesAnswered, overall: a.overall, notes: a.notes })
    }
  }
}
if (unmapped.length) log('WARNING: ' + unmapped.length + ' verdict(s) could not be un-blinded: ' + JSON.stringify(unmapped.slice(0, 4)))

const mean = (xs) => (xs.length ? xs.reduce((a, b) => a + b, 0) / xs.length : null)
const stdev = (xs) => {
  if (xs.length < 2) return null
  const m = mean(xs)
  return Math.sqrt(xs.reduce((a, b) => a + (b - m) ** 2, 0) / (xs.length - 1))
}
const pick = (arm, field, scen) => rows.filter((r) => r.arm === arm && (!scen || r.scenario === scen)).map((r) => r[field])

const summary = { byArm: {}, gaps: {}, gates: {}, perScenario: {} }
for (const arm of ['T', 'C', 'H']) {
  summary.byArm[arm] = {
    n: pick(arm, 'overall').length,
    rubric: mean(pick(arm, 'rubric')),
    heldOut: mean(pick(arm, 'heldOut')),
    probes: mean(pick(arm, 'probes')),
    overall: mean(pick(arm, 'overall')),
  }
}
summary.gaps = {
  rubricGap: summary.byArm.T.rubric - summary.byArm.C.rubric,
  heldOutGap: summary.byArm.T.heldOut - summary.byArm.C.heldOut,
  probeGap: summary.byArm.T.probes - summary.byArm.C.probes,
  overallGap: summary.byArm.T.overall - summary.byArm.C.overall,
  hollowSeparation: summary.byArm.H.n ? summary.byArm.T.overall - summary.byArm.H.overall : null,
}
summary.gates = {
  // Ordering matters and is not cosmetic. Hollow first: if the instrument measures form, nothing
  // downstream means anything, so no other gate can rescue the run.
  hollowSeparation: summary.byArm.H.n ? (summary.gaps.hollowSeparation >= 1.0 ? 'pass' : 'FAIL, instrument measures form') : 'not run',
  discrimination: summary.gaps.overallGap >= 1.0 ? 'pass' : 'FAIL, void rather than negative',
  agreement: (() => { const s = stdev(pick('T', 'overall')); return s === null ? 'n/a' : (s <= 0.7 ? 'pass' : 'FAIL, rubric ambiguous') })(),
  controlSanity: summary.byArm.C.overall >= 2.0 ? 'pass' : 'FAIL, control drifted to a strawman',
  agreementStdev: stdev(pick('T', 'overall')),
}
for (const s of SCENARIOS) {
  summary.perScenario[s.id] = {
    T: mean(pick('T', 'overall', s.id)), C: mean(pick('C', 'overall', s.id)), H: mean(pick('H', 'overall', s.id)),
  }
}

log('T ' + JSON.stringify(summary.byArm.T) + ' | C ' + JSON.stringify(summary.byArm.C) + ' | H ' + JSON.stringify(summary.byArm.H))
log('gates ' + JSON.stringify(summary.gates))

return { summary, rows, artifacts: ok.map((a) => ({ arm: a.arm, scenario: a.scenario, chars: a.text.length })) }
