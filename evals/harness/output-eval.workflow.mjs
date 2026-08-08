// what-it-is:   the EV-1 efficacy eval harness
// what-it-does: runs four arms (treatment, matched treatment, control, hollow) over the scenario bank
//               and scores them blind, in session-matched panels
// why:          the library's quality claim is argued, not measured; this is the attempt to measure it
//               without publishing a number a skeptic can take apart
// used-by:      run with the Workflow tool: Workflow({ scriptPath: "evals/harness/output-eval.workflow.mjs" })
//               pass { types: [...], scenarios: [...], generations: N } as args to narrow or widen the run
//
// READ docs/internal/eval-protocol.md BEFORE CHANGING ANYTHING HERE. Several choices in this file look
// like they could be simplified and cannot: the hollow arm, the equal-length truncation, the randomised
// arm order, the two-session judging split, and the absolute-failure-first verdict ordering each close a
// specific way the number could be wrong, and each is named in that document with the threat it answers.

export const meta = {
  name: 'ev1-output-eval',
  description: 'Four-arm blind efficacy eval over the template bundles, session-matched',
  phases: [
    { title: 'Generate', detail: 'treatment, matched treatment, control and hollow arms per scenario' },
    { title: 'Judge', detail: 'two blind panels per scenario, each scoring one treatment against the same control' },
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

// Independent drafts per arm. The pilot ran ONE and recorded that as a limit: the protocol's spec calls
// for two, so that a per-scenario number is not one sample of a stochastic generator. Every arm gets the
// same count, and the draft-number sentence handed to each is identical across arms, so it cannot act
// differentially on one of them.
const GENERATIONS = (args && args.generations) ? args.generations : 2
const GEN_INDICES = Array.from({ length: GENERATIONS }, (_, i) => i + 1)

// T2: both arms are truncated to the same budget under a stated rule, so length alone cannot separate them.
const LENGTH_RULE = 'Keep the finished document under roughly 900 words. This budget is identical for every arm, so length cannot be what separates them. Do not pad, and do not compress past the point of being useful.'

const draftRule = (gen) => 'Independent draft ' + gen + ' of ' + GENERATIONS + ' for this task. Write it fresh on its own merits; you are not matching or improving on any other draft.'

const scenarioPath = (id) => 'evals/scenarios/' + id + '.md'

function briefInstruction(id) {
  return [
    'Read ' + REPO + '/' + scenarioPath(id) + ' and use ONLY its "The ask" and "What you know" sections as your input.',
    'You MUST NOT read its "Retrieval probes" or "Distractors" sections. Those are the answer key. Reading them invalidates this run.',
  ].join('\n')
}

// NOTE ON WHERE THE ARM INSTRUCTIONS LIVE. Each arm is pointed at its own versioned prompt file and
// reads it, rather than receiving the words inline from here. That is deliberate and symmetric: a third
// copy of the discipline block living in this script is a copy the parity check does not cover, and
// every time this repository has held one fact in two places without a check, the copies drifted.
// The two files are held byte-identical on their shared block by tools/check-eval-arm-parity.py.
//
// It also equalises exposure. Both prompt files disclose the same amount about the run: what the arm
// receives and why its wording is fixed, and nothing about what the documents are scored on. Design
// reasoning that an arm must not read lives in docs/internal/eval-protocol.md instead.

phase('Generate')

// One generation job per arm per draft. The four arms and what each isolates are tabulated in
// evals/harness/treatment-prompt.md; the short version is that T+ minus C is the interpretable gap,
// T minus C is the pilot's gap re-measured, and T minus T+ is what one paragraph of generic advice
// buys on top of a template.
function generationJobs(s) {
  const jobs = []
  for (const gen of GEN_INDICES) {
    // T: the pilot's treatment arm, UNCHANGED. Kept so the re-run reports a number directly
    // comparable to the pilot's rather than replacing it with an incommensurable one.
    jobs.push({
      arm: 'T', gen, scenario: s.id, type: s.type,
      prompt: [
        briefInstruction(s.id),
        '',
        'Then read these two files and use them to write the document:',
        '  ' + REPO + '/templates/' + s.type + '/' + s.type + '_template-full.md',
        '  ' + REPO + '/templates/' + s.type + '/' + s.type + '_guide.md',
        '',
        'Fill the template for this situation. Strip every HTML guidance comment from your output; the finished document must contain none.',
        LENGTH_RULE,
        draftRule(gen),
        '',
        'Output ONLY the finished document. No preamble, no commentary about what you did.',
      ].join('\n'),
    })

    // T+: the same template and guide PLUS the identical discipline instruction the control receives.
    // This is the arm the pilot was missing, and the reason its held-out gap could not be attributed.
    jobs.push({
      arm: 'Tplus', gen, scenario: s.id, type: s.type,
      prompt: [
        briefInstruction(s.id),
        '',
        'Then read these two files and use them to write the document:',
        '  ' + REPO + '/templates/' + s.type + '/' + s.type + '_template-full.md',
        '  ' + REPO + '/templates/' + s.type + '/' + s.type + '_guide.md',
        '',
        'Then read ' + REPO + '/evals/harness/treatment-prompt.md and follow the instruction in its "The prompt" section, treating the document type as: ' + s.type,
        '',
        'Fill the template for this situation. Strip every HTML guidance comment from your output; the finished document must contain none.',
        LENGTH_RULE,
        draftRule(gen),
        '',
        'Output ONLY the finished document. No preamble, no commentary about what you did.',
      ].join('\n'),
    })

    // C: the versioned strong-generic instruction, and nothing from this library. control-prompt.md is
    // UNCHANGED at version 1, deliberately: git proves the counterfactual did not move, which is what
    // makes the pilot and this run comparable at all.
    jobs.push({
      arm: 'C', gen, scenario: s.id, type: s.type,
      prompt: [
        briefInstruction(s.id),
        '',
        'You MUST NOT read anything under ' + REPO + '/templates/ . Do not open a template, a guide, a companion or an example. Your value in this run depends on being independent of them.',
        '',
        'Read ' + REPO + '/evals/harness/control-prompt.md and follow the instruction in its "The prompt" section, treating the document type as: ' + s.type,
        LENGTH_RULE,
        draftRule(gen),
        '',
        'Output ONLY the finished document. No preamble.',
      ].join('\n'),
    })

    // H: the substance-sensitivity calibration. If judges score this near a treatment arm, the
    // instrument is measuring form and no number may be published. T1.3 in the measurement-validity pass.
    if (s.hollow) {
      jobs.push({
        arm: 'H', gen, scenario: s.id, type: s.type,
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
          draftRule(gen),
          '',
          'Output ONLY the document.',
        ].join('\n'),
      })
    }
  }
  return jobs
}

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

const JUDGES = [1, 2, 3]

// TWO judging sessions per scenario per draft, and this is not a cosmetic split.
//
// Session A shows exactly what the pilot's judges saw: {T, C} plus H where it exists. Session B shows
// {Tplus, C} plus H. Each treatment is therefore compared against the control inside a panel whose
// comparison set has the same SIZE and SHAPE as the pilot's.
//
// The naive alternative, one panel seeing all four arms, silently breaks the comparison this whole
// re-run exists to make: if the pilot's judges weighed three documents and this run's weigh four, then
// any movement in the T-versus-C gap could be caused by the changed comparison set rather than by the
// arm matching, and a confound would have been swapped rather than removed.
//
// The split also buys a measurement that is otherwise unavailable: the IDENTICAL control document is
// scored by two independent panels, so the spread between them estimates judging noise directly,
// rather than via the within-panel agreement gate.
const SESSIONS = [
  { id: 'A', treatment: 'T' },
  { id: 'B', treatment: 'Tplus' },
]

function judgePrompt(type, scenarioId, shown) {
  return [
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
  ].join('\n')
}

// Generate a scenario's artifacts, then judge them, per scenario. pipeline rather than a global barrier:
// a scenario whose generations finish first starts judging immediately instead of waiting for the
// slowest scenario in the bank.
const perScenario = await pipeline(
  SCENARIOS,

  // Stage 1: every arm, every draft, for this scenario.
  (s) => parallel(
    generationJobs(s).map((g) => () =>
      agent(g.prompt, { label: 'gen' + g.gen + ':' + g.arm + ':' + g.scenario, phase: 'Generate', model: 'sonnet', effort: 'medium' })
        .then((text) => ({ ...g, text }))
    )
  ).then((made) => {
    const good = made.filter(Boolean).filter((g) => typeof g.text === 'string' && g.text.length > 200)
    log(s.id + ': generated ' + good.length + ' of ' + generationJobs(s).length + ' artifacts')
    return { scenario: s, artifacts: good }
  }),

  // Stage 2: two panels per draft, three judges each.
  ({ scenario, artifacts }) => {
    const jobs = []
    for (const gen of GEN_INDICES) {
      for (const session of SESSIONS) {
        const inSession = artifacts.filter((a) => a.gen === gen && (a.arm === session.treatment || a.arm === 'C' || a.arm === 'H'))
        if (inSession.length < 2) continue
        for (const j of JUDGES) {
          jobs.push({ gen, session: session.id, judge: j, inSession })
        }
      }
    }
    return parallel(jobs.map((job) => () => {
      // Deterministic per-judge rotation. Math.random is unavailable in workflow scripts, and a fixed
      // rotation is enough: no judge sees the same ordering, and the mapping is recoverable afterwards.
      const rotated = job.inSession.slice(job.judge - 1).concat(job.inSession.slice(0, job.judge - 1))
      const labels = ['A', 'B', 'C', 'D']
      const shown = rotated.map((a, i) => ({ ...a, label: labels[i] }))
      return agent(
        judgePrompt(scenario.type, scenario.id, shown),
        {
          label: 'judge' + job.judge + ':' + job.session + job.gen + ':' + scenario.id,
          phase: 'Judge',
          schema: SCORE_SCHEMA,
          model: 'sonnet',
          effort: 'high',
        }
      ).then((v) => ({
        scenarioId: scenario.id,
        gen: job.gen,
        session: job.session,
        judge: job.judge,
        key: shown.map((a) => ({ label: a.label, arm: a.arm })),
        verdict: v,
      }))
    }))
  }
)

// Un-blind and aggregate.
//
// normLabel exists because of a real failure. The first pilot execution produced 33 valid judgments and
// ZERO aggregated rows: the key was built on "A" while judges echoed the heading they were shown and
// returned "Artifact A", so every lookup missed and every arm silently held no data. Match on the
// trailing letter rather than on string equality, and fail loudly if a verdict cannot be un-blinded,
// because a silent miss here turns a completed run into a null result that looks like a finding.
// TWO shapes have now been observed in the wild, and the second one broke the fix for the first.
//   pilot, 2026-08-08:    "Artifact A"                      -> a leading word before the letter
//   re-run, 2026-08-08:   "Artifact A (narrative postmortem)" -> a trailing parenthetical after it
// The pilot's fix anchored on the TRAILING letter, which the second shape defeats: it ends in ")".
// Patching per observed shape loses rows every time a judge phrases a label a new way, so this is a
// cascade from most specific to most general rather than one more anchor. Anything it still cannot
// read is logged by scenario, session, judge and raw label, and dropped rather than guessed at.
const normLabel = (s) => {
  const t = String(s ?? '').trim().toUpperCase()
  if (!t) return null
  const rules = [
    /^([A-D])$/,                              // exactly the label: "A"
    /^(?:ARTIFACT|DOCUMENT|DOC)?\s*([A-D])\b/, // label at the front: "Artifact A (...)"
    /\b([A-D])\s*$/,                           // label at the end: "...Artifact A"
    /\b([A-D])\b/,                             // any standalone letter, first wins
  ]
  for (const re of rules) {
    const m = t.match(re)
    if (m) return m[1]
  }
  return null
}

const rows = []
const unmapped = []
for (const scenarioResult of perScenario.filter(Boolean)) {
  for (const r of (scenarioResult ?? []).filter(Boolean)) {
    const map = Object.fromEntries(r.key.map((k) => [k.label, k.arm]))
    for (const a of r.verdict.artifacts ?? []) {
      const arm = map[normLabel(a.label)]
      if (!arm) { unmapped.push({ scenario: r.scenarioId, session: r.session, judge: r.judge, label: a.label }); continue }
      rows.push({
        scenario: r.scenarioId, gen: r.gen, session: r.session, judge: r.judge, arm,
        rubric: a.rubricMean, heldOut: a.heldOutMean, probes: a.probesAnswered, overall: a.overall,
        notes: a.notes,
      })
    }
  }
}
if (unmapped.length) log('WARNING: ' + unmapped.length + ' verdict(s) could not be un-blinded: ' + JSON.stringify(unmapped.slice(0, 4)))
log('aggregated ' + rows.length + ' judge-artifact rows')

const mean = (xs) => (xs.length ? xs.reduce((a, b) => a + b, 0) / xs.length : null)
const stdev = (xs) => {
  if (xs.length < 2) return null
  const m = mean(xs)
  return Math.sqrt(xs.reduce((a, b) => a + (b - m) ** 2, 0) / (xs.length - 1))
}

// Session-scoped selection. Every gap below is computed WITHIN a session, never across one, because a
// cross-session gap would compare documents judged in different comparison sets.
const sel = (arm, field, opts = {}) => rows
  .filter((r) => r.arm === arm)
  .filter((r) => (opts.session ? r.session === opts.session : true))
  .filter((r) => (opts.scenario ? r.scenario === opts.scenario : true))
  .map((r) => r[field])

const armBlock = (arm, session) => ({
  n: sel(arm, 'overall', { session }).length,
  rubric: mean(sel(arm, 'rubric', { session })),
  heldOut: mean(sel(arm, 'heldOut', { session })),
  probes: mean(sel(arm, 'probes', { session })),
  overall: mean(sel(arm, 'overall', { session })),
})

const summary = { generations: GENERATIONS, byArm: {}, gaps: {}, gates: {}, perScenario: {}, controlReplication: {} }

summary.byArm = {
  T: armBlock('T', 'A'),
  Tplus: armBlock('Tplus', 'B'),
  C_sessionA: armBlock('C', 'A'),
  C_sessionB: armBlock('C', 'B'),
  H_sessionA: armBlock('H', 'A'),
  H_sessionB: armBlock('H', 'B'),
}

// Subtraction that refuses to invent a zero. See the note on instructionEffect_crossSession below.
const diff = (a, b) => (a === null || b === null || a === undefined || b === undefined) ? null : a - b

const gapOn = (treatArm, treatSession, field) => diff(
  mean(sel(treatArm, field, { session: treatSession })),
  mean(sel('C', field, { session: treatSession }))
)

summary.gaps = {
  // PRIMARY: the matched comparison. Both arms received the identical discipline instruction, so this
  // gap is attributable to the template and to nothing else.
  matched: {
    rubricGap: gapOn('Tplus', 'B', 'rubric'),
    heldOutGap: gapOn('Tplus', 'B', 'heldOut'),
    probeGap: gapOn('Tplus', 'B', 'probes'),
    overallGap: gapOn('Tplus', 'B', 'overall'),
  },
  // The pilot's comparison, re-measured under the same conditions, so the two runs sit side by side.
  pilotComparable: {
    rubricGap: gapOn('T', 'A', 'rubric'),
    heldOutGap: gapOn('T', 'A', 'heldOut'),
    probeGap: gapOn('T', 'A', 'probes'),
    overallGap: gapOn('T', 'A', 'overall'),
  },
  // What one paragraph of generic advice buys ON TOP of a template. Cross-session by necessity, and
  // flagged as such: it is a decomposition aid, not a gate input.
  //
  // diff rather than bare subtraction, because mean([]) returns null and null minus null is 0 in
  // JavaScript, not null. That would report a confident zero effect computed over no data, which is
  // the exact failure mode the pilot's un-blinding bug produced: a completed run whose null looked
  // like a finding. Fail to null, loudly, instead.
  instructionEffect_crossSession: {
    rubricGap: diff(mean(sel('Tplus', 'rubric', { session: 'B' })), mean(sel('T', 'rubric', { session: 'A' }))),
    heldOutGap: diff(mean(sel('Tplus', 'heldOut', { session: 'B' })), mean(sel('T', 'heldOut', { session: 'A' }))),
    overallGap: diff(mean(sel('Tplus', 'overall', { session: 'B' })), mean(sel('T', 'overall', { session: 'A' }))),
  },
  hollowSeparation_matched: summary.byArm.H_sessionB.n
    ? summary.byArm.Tplus.overall - summary.byArm.H_sessionB.overall
    : null,
  hollowSeparation_pilotComparable: summary.byArm.H_sessionA.n
    ? summary.byArm.T.overall - summary.byArm.H_sessionA.overall
    : null,
}

// The same control documents, scored by two independent panels. This is a direct estimate of judging
// noise, and it bounds how much of any gap above can be read as real.
summary.controlReplication = {
  sessionA_overall: summary.byArm.C_sessionA.overall,
  sessionB_overall: summary.byArm.C_sessionB.overall,
  delta: (summary.byArm.C_sessionA.overall === null || summary.byArm.C_sessionB.overall === null)
    ? null
    : summary.byArm.C_sessionA.overall - summary.byArm.C_sessionB.overall,
  note: 'identical artifacts, independent panels; any gap smaller than this delta is not distinguishable from judging noise',
}

summary.gates = {
  // Ordering matters and is not cosmetic. Hollow first: if the instrument measures form, nothing
  // downstream means anything, so no other gate can rescue the run.
  hollowSeparation: summary.byArm.H_sessionB.n
    ? (summary.gaps.hollowSeparation_matched >= 1.0 ? 'pass' : 'FAIL, instrument measures form')
    : 'not run',
  // Keyed on the MATCHED gap. The pilot-comparable gap is reported for continuity and does not vote.
  discrimination: summary.gaps.matched.overallGap >= 1.0 ? 'pass' : 'FAIL, void rather than negative',
  agreement: (() => {
    const s = stdev(sel('Tplus', 'overall', { session: 'B' }))
    return s === null ? 'n/a' : (s <= 0.7 ? 'pass' : 'FAIL, rubric ambiguous')
  })(),
  controlSanity: (summary.byArm.C_sessionB.overall ?? 0) >= 2.0 ? 'pass' : 'FAIL, control drifted to a strawman',
  agreementStdev: stdev(sel('Tplus', 'overall', { session: 'B' })),
  agreementStdev_pilotComparable: stdev(sel('T', 'overall', { session: 'A' })),
}

for (const s of SCENARIOS) {
  summary.perScenario[s.id] = {
    T: mean(sel('T', 'overall', { session: 'A', scenario: s.id })),
    Tplus: mean(sel('Tplus', 'overall', { session: 'B', scenario: s.id })),
    C_A: mean(sel('C', 'overall', { session: 'A', scenario: s.id })),
    C_B: mean(sel('C', 'overall', { session: 'B', scenario: s.id })),
    H_A: mean(sel('H', 'overall', { session: 'A', scenario: s.id })),
    H_B: mean(sel('H', 'overall', { session: 'B', scenario: s.id })),
  }
}

log('MATCHED  T+ ' + JSON.stringify(summary.byArm.Tplus) + ' | C(B) ' + JSON.stringify(summary.byArm.C_sessionB))
log('PILOTCMP T  ' + JSON.stringify(summary.byArm.T) + ' | C(A) ' + JSON.stringify(summary.byArm.C_sessionA))
log('gaps.matched ' + JSON.stringify(summary.gaps.matched))
log('gaps.pilotComparable ' + JSON.stringify(summary.gaps.pilotComparable))
log('gates ' + JSON.stringify(summary.gates))
log('control replication delta ' + JSON.stringify(summary.controlReplication.delta))

return {
  summary,
  rows,
  meta: {
    controlPromptVersion: 1,
    treatmentPromptVersion: 1,
    generations: GENERATIONS,
    sessions: SESSIONS,
    scenarios: SCENARIOS.map((s) => s.id),
  },
}
