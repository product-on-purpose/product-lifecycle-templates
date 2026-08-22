#!/usr/bin/env node
// what-it-is:   the post-run analysis for an EV-1 eval result
// what-it-does: turns a run's raw judge-artifact rows into gaps carrying bootstrap confidence intervals
// why:          eval-protocol.md section 7 requires every gap be reported with an interval and never as a
//               bare point estimate, and the 2026-08-08 pilot shipped without one
// used-by:      node evals/harness/analyze.mjs <raw-rows.json> [--seed N] [--iterations N]
//
// WHY THIS IS A SEPARATE SCRIPT AND NOT PART OF THE HARNESS
//
// Workflow scripts cannot call Math.random: the runtime forbids it because a resumed run must replay
// identically, and a random draw would make the replay diverge from the original. A bootstrap is nothing
// but random draws. So the harness produces rows and this script, running under plain node, produces the
// intervals. It uses a SEEDED generator anyway, so two runs over the same rows give the same interval and
// a published number can be recomputed by anyone.
//
// THE ONE STATISTICAL CHOICE THAT MATTERS
//
// It resamples SCENARIOS, not rows. Three judges scoring the same document are not three independent
// observations of anything, and two drafts of one scenario share that scenario's difficulty. Resampling
// rows would treat all of that as independent evidence and return a tight, confident, wrong interval.
// Resampling whole scenarios and taking every row beneath them is the cluster bootstrap, and with six
// clusters it returns a wide interval. That width is the honest precision of a six-scenario pilot, and it
// is the reason the protocol says regression thresholds read the lower bound rather than the point.

import { readFileSync } from 'node:fs'

const argv = process.argv.slice(2)
const path = argv.find((a) => !a.startsWith('--'))
const flag = (name, fallback) => {
  const i = argv.indexOf('--' + name)
  return i === -1 ? fallback : Number(argv[i + 1])
}

const SEED = flag('seed', 20260808)
const ITERATIONS = flag('iterations', 10000)

if (!path) {
  console.error('usage: node evals/harness/analyze.mjs <raw-rows.json> [--seed N] [--iterations N]')
  console.error('  the json may be the workflow return object, or a bare array of rows')
  process.exit(2)
}

const raw = JSON.parse(readFileSync(path, 'utf8'))
const rows = Array.isArray(raw) ? raw : (raw.rows ?? [])

if (!rows.length) {
  // Fail loudly on an empty input. The pilot's un-blinding bug produced a completed run with zero
  // aggregated rows whose summary read as a clean null, and the only reason it was caught is that the
  // gates failed closed. Nothing here may report a confident number over no data.
  console.error('FAIL: no rows found in ' + path)
  console.error('      A run that produced no aggregated rows is not a null result. It is a broken run.')
  process.exit(1)
}

// mulberry32. Small, seeded, and adequate for a percentile bootstrap; nothing here is cryptographic.
function rng(seed) {
  let a = seed >>> 0
  return function () {
    a = (a + 0x6d2b79f5) >>> 0
    let t = a
    t = Math.imul(t ^ (t >>> 15), t | 1)
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61)
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

const mean = (xs) => (xs.length ? xs.reduce((a, b) => a + b, 0) / xs.length : null)

const scenarios = [...new Set(rows.map((r) => r.scenario))].sort()
const byScenario = Object.fromEntries(scenarios.map((s) => [s, rows.filter((r) => r.scenario === s)]))

// A gap is always computed WITHIN one judging session, because sessions differ in what else the panel
// was shown and a cross-session subtraction compares documents judged in different comparison sets.
function gapFrom(sample, { arm, session, field }) {
  const t = mean(sample.filter((r) => r.arm === arm && r.session === session).map((r) => r[field]))
  const c = mean(sample.filter((r) => r.arm === 'C' && r.session === session).map((r) => r[field]))
  return (t === null || c === null) ? null : t - c
}

function bootstrap(spec) {
  const point = gapFrom(rows, spec)
  if (point === null) return { point: null, lower: null, upper: null, note: 'no data for this comparison' }

  const rand = rng(SEED)
  const draws = []
  for (let i = 0; i < ITERATIONS; i++) {
    const sample = []
    for (let k = 0; k < scenarios.length; k++) {
      const picked = scenarios[Math.floor(rand() * scenarios.length)]
      sample.push(...byScenario[picked])
    }
    const g = gapFrom(sample, spec)
    if (g !== null) draws.push(g)
  }
  draws.sort((a, b) => a - b)
  const at = (q) => draws[Math.min(draws.length - 1, Math.max(0, Math.floor(q * draws.length)))]
  return {
    point,
    lower: at(0.025),
    upper: at(0.975),
    resamples: draws.length,
    clusters: scenarios.length,
  }
}

const COMPARISONS = [
  { key: 'matched.rubricGap', label: 'Rubric gap, matched (T+ vs C)', arm: 'Tplus', session: 'B', field: 'rubric' },
  { key: 'matched.heldOutGap', label: 'Held-out gap, matched (T+ vs C)', arm: 'Tplus', session: 'B', field: 'heldOut' },
  { key: 'matched.probeGap', label: 'Probe gap, matched (T+ vs C)', arm: 'Tplus', session: 'B', field: 'probes' },
  { key: 'matched.overallGap', label: 'Overall gap, matched (T+ vs C)', arm: 'Tplus', session: 'B', field: 'overall' },
  { key: 'pilot.rubricGap', label: 'Rubric gap, pilot-comparable (T vs C)', arm: 'T', session: 'A', field: 'rubric' },
  { key: 'pilot.heldOutGap', label: 'Held-out gap, pilot-comparable (T vs C)', arm: 'T', session: 'A', field: 'heldOut' },
  { key: 'pilot.probeGap', label: 'Probe gap, pilot-comparable (T vs C)', arm: 'T', session: 'A', field: 'probes' },
  { key: 'pilot.overallGap', label: 'Overall gap, pilot-comparable (T vs C)', arm: 'T', session: 'A', field: 'overall' },
]

const fmt = (x) => (x === null || x === undefined || Number.isNaN(x) ? 'n/a' : (x >= 0 ? '+' : '') + x.toFixed(2))

const results = {}
console.log('')
console.log('EV-1 gap analysis, cluster bootstrap over scenarios')
console.log('  input       ' + path)
console.log('  rows        ' + rows.length)
console.log('  clusters    ' + scenarios.length + ' scenario(s): ' + scenarios.join(', '))
console.log('  iterations  ' + ITERATIONS + ', seed ' + SEED)
console.log('')
console.log('| Comparison | Point | 95% interval | Lower bound |')
console.log('|---|---|---|---|')

for (const c of COMPARISONS) {
  const r = bootstrap(c)
  results[c.key] = r
  console.log(
    '| ' + c.label + ' | ' + fmt(r.point) + ' | ' +
    (r.lower === null ? 'n/a' : fmt(r.lower) + ' to ' + fmt(r.upper)) + ' | ' +
    fmt(r.lower) + ' |'
  )
}

console.log('')
console.log('The interval is resampled over SCENARIOS, not over judge-artifact rows. Rows within a')
console.log('scenario share a document and a panel, so treating them as independent would return a')
console.log('confident interval the data does not support.')
console.log('')
console.log('Protocol section 7: a regression threshold reads the LOWER BOUND, never the point.')

// A cluster bootstrap over ONE cluster is degenerate: every resample draws the same scenario, so
// lower === upper === point and the "interval" is zero-width. Said plainly because the previous
// wording asserted the opposite ("the interval is wide") directly under a table of +1.14 to +1.14,
// which reads as certainty rather than as the absence of an estimate. Found 2026-08-21 on the first
// single-scenario run, which is the only shape that triggers it.
if (scenarios.length < 2) {
  console.log('')
  console.log('WARNING: ' + scenarios.length + ' cluster. The bootstrap is DEGENERATE, not wide. Every')
  console.log('resample draws the same scenario, so lower === upper === point and the interval above')
  console.log('carries NO information about precision. Do not read it as a confidence interval, and do')
  console.log('not publish a gap from this run: protocol section 7 forbids a bare point estimate and')
  console.log('this run cannot produce anything else. Two or more scenarios are required.')
} else {
  console.log('With ' + scenarios.length + ' clusters the interval is wide, and that width is the run')
  console.log('precision rather than a defect.')
}

// A gap whose interval spans zero has not established a direction, whatever its point estimate says.
const spanning = Object.entries(results).filter(([, r]) => r.lower !== null && r.lower < 0 && r.upper > 0)
if (spanning.length) {
  console.log('')
  console.log('SPANS ZERO, so no direction is established for:')
  for (const [k] of spanning) console.log('  ' + k)
}

console.log('')
console.log('JSON:')
console.log(JSON.stringify({ seed: SEED, iterations: ITERATIONS, clusters: scenarios, results }, null, 2))
