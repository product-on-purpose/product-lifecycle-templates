#!/usr/bin/env python3
"""gen-bundle-build-report.py - what it cost to build a bundle, measured rather than estimated.

WHY THIS EXISTS.
Two documents state a per-bundle build cost and they disagree: `docs/internal/bundle-pipeline.md`
says "roughly 0.6-1M tokens" and `.claude/commands/build-bundle.md` says "roughly 700K-1M". Neither
cites a measurement, and until this tool ran, none existed. In a library that refuses to call a
bundle proven without evidence, the number used to decide whether a bundle is worth building was
the least evidenced number in the repository.

WHAT IT MEASURES, AND FROM WHERE.
The Claude Code harness already writes everything needed, outside this repository, under
`~/.claude/projects/<slug>/`:

    <session>.jsonl                                  the orchestrator's own turns
    <session>/subagents/workflows/<run>/journal.jsonl   agentId -> label, phase, file_written
    <session>/subagents/workflows/<run>/agent-<id>.jsonl  per-turn model and usage
    <session>/subagents/workflows/<run>/agent-<id>.meta.json  the requested model tier

This tool joins those three and attributes each agent to a bundle, a stage and a deliverable.

Usage is counted once per API RESPONSE, not once per transcript record. The harness writes one record
per content block of a response (thinking, text, each tool call) and every one of them repeats the
response's full usage block. Schema 1.0.0 summed records and so counted each response's cache reads
and writes two or three times; every report it wrote overstated its build by roughly 2x. See
agent_usage().

THE TWO MODES, AND WHY THEY ARE SEPARATE.
Transcripts are machine-local. They are not in this repository, they are not on the CI runner, and
they are pruned eventually. So ingestion and verification cannot be the same command:

    --ingest   reads transcripts and WRITES bundle-builds/reports/*.json and *.md.
               Runs only on a machine that holds the transcripts, at build time.
    (no flag)  regenerates bundle-builds/INDEX.md from the COMMITTED reports. No transcripts needed.
    --check    verifies INDEX.md matches the committed reports. CI-safe, no transcripts needed.

The committed JSON is the source of truth once written. That is deliberate: a measurement whose
source can disappear must be captured at the moment it is true, not re-derived later.

WHAT IT CANNOT TELL YOU.
- Reasoning effort is not recorded anywhere in the transcript tree. Only the requested model tier is.
- The orchestrator's own token spend is not divisible per bundle, because one session interleaves
  several bundles and other work. It is not reported at all, here or in INDEX.md.
- What a build actually cost the person who ran it. The dollar figure prices each response at API list
  rates; work run under a Claude subscription is not billed per token.
- Runs that predate the labelling convention carry no label, so their attribution is inferred from
  the agent's own prompt and is marked with a lower confidence tier. See CONFIDENCE below.

Usage:
    python tools/gen-bundle-build-report.py --ingest        # read transcripts, write reports
    python tools/gen-bundle-build-report.py --ingest --dry-run
    python tools/gen-bundle-build-report.py                 # regenerate INDEX.md from reports
    python tools/gen-bundle-build-report.py --check         # freshness gate (CI)

Exit 0 if written / in sync; 1 if --check finds drift, or --ingest finds no transcripts.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "bundle-builds")
REPORT_DIR = os.path.join(OUT_DIR, "reports")
INDEX_PATH = os.path.join(OUT_DIR, "INDEX.md")
MANIFEST_PATH = os.path.join(ROOT, "manifest.json")

GREEN, RED, DIM, OFF = "\033[32m", "\033[31m", "\033[2m", "\033[0m"

# The schema version of the emitted JSON. Bump when a field's meaning changes, never when one is
# added, so an older report stays readable against a newer tool.
#   2.0.0 (2026-09-22) every usage count is per API response rather than per transcript record, so
#         `turns` means responses and the token totals roughly halve. All reports were re-ingested.
REPORT_SCHEMA_VERSION = "2.0.0"

# Weights, relative to one fresh input token. The weighted total is a fixed UNIT, the same for every
# model and every report, so that two reports written months apart stay comparable and a reader can
# re-weight with their own numbers. It is not money. The ratios are the standard ones and are exact for
# Sonnet 5 and Opus 5, but NOT for every Claude model: Opus 5.5 reads cache at 0.05x its input price
# and Fable 5.1 at 0.025x. That is why cost in dollars is computed separately, from PRICES, per model.
WEIGHTS = {"input": 1.0, "cache_write": 1.25, "cache_write_1h": 2.0, "cache_read": 0.1,
           "output": 5.0}

# USD per million tokens at Anthropic API list rates, keyed by undated model id. Checked against the
# source on the date below; a price change needs a new date, not a silent edit. A model missing from
# this table is reported as unpriced, never as free.
PRICES_AS_OF = "2026-09-22"
PRICES_SOURCE = "https://platform.claude.com/docs/en/about-claude/pricing"
PRICES = {
    #                    input  5m write  1h write  cache read  output
    "claude-fable-5-1":  (10.0, 12.50,    20.0,     0.25,       50.0),
    "claude-fable-5":    (10.0, 12.50,    20.0,     1.00,       50.0),
    "claude-opus-5-5":   (4.0,  5.00,     8.0,      0.20,       20.0),
    "claude-opus-5":     (5.0,  6.25,     10.0,     0.50,       25.0),
    "claude-opus-4-8":   (5.0,  6.25,     10.0,     0.50,       25.0),
    "claude-sonnet-5":   (2.0,  2.50,     4.0,      0.20,       10.0),
    "claude-sonnet-4-6": (3.0,  3.75,     6.0,      0.30,       15.0),
    "claude-haiku-4-5":  (1.0,  1.25,     2.0,      0.10,       5.0),
}
WEB_SEARCH_USD = 0.01  # $10 per 1,000 searches. Web fetch costs nothing beyond its tokens.

# How a bundle was attributed to an agent, best first. Anything at or above "path" is treated as
# reliable; "name" is prose matching and is recorded but never used to key a report.
CONFIDENCE = {
    "label": "high",    # the workflow label carries the bundle id. Exact.
    "file": "high",     # the agent wrote a file under templates/<id>/. Exact.
    "quoted": "high",   # the prompt names the bundle in quotes: for "definition-of-done"
    "path": "high",     # the prompt head names templates/<id>/
    "name": "low",      # a title or alias appears in the prompt subject line. Over-matches.
    "excluded": "n/a",  # not a bundle build at all (an eval judge panel, for example)
    "none": "n/a",
}
RELIABLE = {"label", "file", "quoted", "path"}


# ---------------------------------------------------------------------------- transcript location

def project_slug():
    """Claude Code slugs a project path by replacing each separator with one dash.

    Each separator maps to one dash and runs are NOT collapsed: "E:\\Projects" becomes
    "E--Projects", because the drive colon and the backslash each contribute one.
    """
    return re.sub(r"[:\\/]", "-", ROOT)


def transcript_root():
    override = os.environ.get("PLT_TRANSCRIPT_ROOT")
    if override:
        return override
    home = os.path.expanduser("~")
    return os.path.join(home, ".claude", "projects", project_slug())


# ---------------------------------------------------------------------------------- attribution

def load_known_bundles():
    """(ids, name_patterns) from manifest.json, which is generated and gate-checked."""
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        man = json.load(f)
    entries = man.get("bundles", man) if isinstance(man, dict) else man
    if isinstance(entries, dict):
        entries = list(entries.values())
    ids, patterns = set(), []
    for e in entries:
        bid = e.get("id") or e.get("doc_type")
        if not bid:
            continue
        ids.add(bid)
        phrases = {bid.replace("-", " ")}
        if e.get("title"):
            phrases.add(e["title"])
        for a in e.get("aliases") or []:
            phrases.add(a)
        for p in phrases:
            p = re.sub(r"\s*\([^)]*\)", "", str(p)).strip()
            if len(p) < 6:
                continue
            words = [w for w in re.split(r"[\s\-]+", p) if w]
            pat = r"(?<![a-z])" + r"[\s\-/]+".join(re.escape(w) for w in words) + r"(?![a-z])"
            patterns.append((len(p), re.compile(pat, re.I), bid))
    patterns.sort(key=lambda t: -t[0])
    return ids, patterns


PATH_RE = re.compile(r"templates[\\/]([a-z0-9]+(?:-[a-z0-9]+)*)[\\/]")
QUOTED_RE = re.compile(r"for\s+[`\"']([a-z0-9-]+)[`\"']")
# A judge panel scoring finished documents is not a bundle build and must not be billed to one.
EXCLUDE_RE = re.compile(r"blind panel|judge (?:on|scoring)|evals[\\/]rubrics", re.I)
STAGE_RE = re.compile(r"^(research|draft|lens|review|verify)\b", re.I)


def first_prompt(path, head=600):
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                if rec.get("type") != "user":
                    continue
                content = (rec.get("message") or {}).get("content")
                if isinstance(content, list):
                    content = " ".join(
                        c.get("text", "") for c in content if isinstance(c, dict)
                    )
                if isinstance(content, str) and content.strip():
                    return content[:head]
    except OSError:
        pass
    return ""


def attribute(label, file_written, head, ids, patterns):
    if label and "/" in label:
        cand = label.split("/", 1)[0]
        if cand in ids:
            return cand, "label"
    if file_written:
        m = PATH_RE.search(file_written)
        if m and m.group(1) in ids:
            return m.group(1), "file"
    if EXCLUDE_RE.search(head):
        return "", "excluded"
    for m in QUOTED_RE.finditer(head):
        if m.group(1) in ids:
            return m.group(1), "quoted"
    for m in PATH_RE.finditer(head):
        if m.group(1) in ids:
            return m.group(1), "path"
    # A prose name counts only in the subject line, and only the EARLIEST one counts. Two rules,
    # each paid for by a wrong answer:
    #   - whole-prompt search let a phrase every prompt mentions in passing capture the run;
    #     "acceptance criteria" once claimed 226 agents.
    #   - longest-phrase-wins billed a research run to the SIBLING it compares against, because a
    #     research prompt names its own subject first and its comparators afterwards.
    # A tie between two different bundles at the same position is ambiguous, so it resolves to none.
    subject = head.lstrip()[:200]
    best_pos, best_bid, tied = None, "", False
    for length, pat, bid in patterns:
        m = pat.search(subject)
        if not m:
            continue
        if best_pos is None or m.start() < best_pos:
            best_pos, best_bid, tied = m.start(), bid, False
        elif m.start() == best_pos and bid != best_bid:
            tied = True
    if best_bid and not tied:
        return best_bid, "name"
    return "", "none"


def stage_of(label, head):
    if label:
        prefix = label.split("/")[-1].split(":")[0]
        if STAGE_RE.match(prefix):
            return prefix.lower()
    low = head.lower()
    if low.lstrip().startswith("research the") or "research the origins" in low[:200]:
        return "research"
    if "you are writing a file" in low[:500] or low.lstrip().startswith("draft "):
        return "draft"
    if "one lens in an adversarial review" in low:
        return "lens"
    if "adversarial verifier" in low or low.lstrip().startswith("refute"):
        return "verify"
    return "other"


def deliverable_of(label, file_written):
    if label:
        tail = label.split("/")[-1]
        if ":" in tail:
            return tail.split(":", 1)[1]
        return tail
    if file_written:
        base = os.path.basename(file_written)
        m = re.match(r"[a-z0-9-]+_(.+)\.md$", base)
        if m:
            return m.group(1)
    return ""


# -------------------------------------------------------------------------------------- usage

RESPONSE_FIELDS = ("input", "output", "cache_write", "cache_write_1h", "cache_read",
                   "web_search", "web_fetch")


def response_usd(model, row):
    """One response's cost at API list rates, or None when its model is not in PRICES.

    Transcripts carry some ids dated (claude-haiku-4-5-20251001); PRICES is keyed undated.
    """
    price = PRICES.get(re.sub(r"-\d{8}$", "", model or ""))
    if price is None:
        return None
    p_in, p_w5, p_w1h, p_read, p_out = price
    cw_1h = row["cache_write_1h"]
    return ((row["input"] * p_in + (row["cache_write"] - cw_1h) * p_w5 + cw_1h * p_w1h
             + row["cache_read"] * p_read + row["output"] * p_out) / 1e6
            + row["web_search"] * WEB_SEARCH_USD)


def agent_usage(path):
    """Usage for one agent transcript, counted once per API response.

    The harness writes one transcript record per CONTENT BLOCK of a response - thinking, text, each
    tool call - and each of those records repeats the response's whole usage block. Summing records
    counted every response's cache reads and writes two or three times. So records are grouped by
    message id and each field keeps its largest value: input and cache fields are identical across
    one response's records, and output_tokens grows as the response streams, so the largest value is
    the final count.
    """
    responses = {}
    try:
        fh = open(path, encoding="utf-8")
    except OSError:
        return blank(), {}
    with fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if rec.get("type") != "assistant":
                continue
            msg = rec.get("message") or {}
            use = msg.get("usage") or {}
            model = msg.get("model") or ""
            # "<synthetic>" records are written by the harness, not returned by the API, and carry
            # zero usage. Counting them would add responses that never happened.
            if not use or model == "<synthetic>":
                continue
            server = use.get("server_tool_use") or {}
            row = {
                "input": use.get("input_tokens", 0),
                "output": use.get("output_tokens", 0),
                "cache_write": use.get("cache_creation_input_tokens", 0),
                "cache_write_1h": (use.get("cache_creation") or {}).get(
                    "ephemeral_1h_input_tokens", 0),
                "cache_read": use.get("cache_read_input_tokens", 0),
                "web_search": server.get("web_search_requests", 0),
                "web_fetch": server.get("web_fetch_requests", 0),
            }
            key = msg.get("id") or rec.get("requestId") or rec.get("uuid")
            seen = responses.get(key)
            if seen is None:
                row["model"] = model
                responses[key] = row
            else:
                for k in RESPONSE_FIELDS:
                    seen[k] = max(seen[k], row[k])

    totals, models = blank(), {}
    for row in responses.values():
        totals["turns"] += 1
        for k in ("input", "output", "cache_write", "cache_write_1h", "cache_read", "web_search"):
            totals[k] += row[k]
        totals["web"] += row["web_search"] + row["web_fetch"]
        cost = response_usd(row["model"], row)
        if cost is None:
            totals["unpriced_turns"] += 1
        else:
            totals["usd"] += cost
        if row["model"]:
            models[row["model"]] = models.get(row["model"], 0) + 1
    return totals, models


def weighted(totals):
    cw_1h = totals.get("cache_write_1h", 0)
    return int(round(totals.get("input", 0) * WEIGHTS["input"]
                     + (totals.get("cache_write", 0) - cw_1h) * WEIGHTS["cache_write"]
                     + cw_1h * WEIGHTS["cache_write_1h"]
                     + totals.get("cache_read", 0) * WEIGHTS["cache_read"]
                     + totals.get("output", 0) * WEIGHTS["output"]))


def weights_text():
    return ("input x%s, cache write x%s (x%s for a 1-hour write), cache read x%s, output x%s"
            % (WEIGHTS["input"], WEIGHTS["cache_write"], WEIGHTS["cache_write_1h"],
               WEIGHTS["cache_read"], WEIGHTS["output"]))


def add(into, src):
    for k in blank():
        into[k] = into.get(k, 0) + src.get(k, 0)
    return into


def tidy(usage):
    """A copy with usd rounded to a hundredth of a cent, so the JSON does not carry float noise."""
    out = dict(usage)
    out["usd"] = round(out.get("usd", 0.0), 4)
    return out


def blank():
    return {"turns": 0, "input": 0, "output": 0, "cache_write": 0, "cache_write_1h": 0,
            "cache_read": 0, "web": 0, "web_search": 0, "usd": 0.0, "unpriced_turns": 0}


# -------------------------------------------------------------------------------------- ingest

def collect(ids, patterns):
    """Walk every workflow run on this machine and return one record per agent."""
    root = transcript_root()
    if not os.path.isdir(root):
        return [], root
    agents = []
    for session in sorted(os.listdir(root)):
        wf_root = os.path.join(root, session, "subagents", "workflows")
        if not os.path.isdir(wf_root):
            continue
        for run in sorted(os.listdir(wf_root)):
            run_dir = os.path.join(wf_root, run)
            journal = os.path.join(run_dir, "journal.jsonl")
            if not os.path.isfile(journal):
                continue
            labels, files = {}, {}
            with open(journal, encoding="utf-8") as f:
                for line in f:
                    try:
                        rec = json.loads(line)
                    except ValueError:
                        continue
                    aid = rec.get("agentId")
                    if not aid:
                        continue
                    if rec.get("type") == "started":
                        labels[aid] = rec.get("label") or ""
                    elif rec.get("type") == "result":
                        res = rec.get("result")
                        if isinstance(res, dict) and res.get("file_written"):
                            files[aid] = res["file_written"]
            for aid, label in labels.items():
                apath = os.path.join(run_dir, "agent-%s.jsonl" % aid)
                head = first_prompt(apath)
                bundle, method = attribute(label, files.get(aid, ""), head, ids, patterns)
                totals, models = agent_usage(apath)
                if not totals["turns"]:
                    continue
                tier = None
                mpath = os.path.join(run_dir, "agent-%s.meta.json" % aid)
                if os.path.isfile(mpath):
                    try:
                        with open(mpath, encoding="utf-8") as f:
                            tier = json.load(f).get("model")
                    except (OSError, ValueError):
                        tier = None
                resolved = max(models, key=models.get) if models else "unknown"
                agents.append({
                    "session": session, "run": run, "agent_id": aid,
                    "label": label, "bundle": bundle, "attribution": method,
                    "confidence": CONFIDENCE.get(method, "n/a"),
                    "stage": stage_of(label, head),
                    "deliverable": deliverable_of(label, files.get(aid, "")),
                    "requested_model": tier, "model": resolved,
                    "file_written": os.path.basename(files.get(aid, "")),
                    "usage": tidy(totals), "weighted": weighted(totals),
                    "mtime": os.path.getmtime(journal),
                })
    return agents, root


def resolve_runs(agents):
    """Decide which bundle each workflow RUN belongs to, then stamp every agent in it.

    A run is one stage of one bundle, so the run is the right unit. This matters most for the
    research and review fan-outs: their agents write no file and their prompts name the type in
    prose rather than as a path, so agent-by-agent they look unattributable. Six independent
    research agents whose prompts all name the same bundle is strong evidence even though any one
    of them alone is weak, which is why run consensus is promoted to "medium" and a lone prose
    match is not.
    """
    runs = {}
    for a in agents:
        runs.setdefault((a["session"], a["run"]), []).append(a)

    for rows in runs.values():
        excluded = sum(1 for a in rows if a["attribution"] == "excluded")
        if excluded * 2 >= len(rows):
            for a in rows:
                a["bundle"], a["run_confidence"] = "", "excluded"
            continue

        reliable = {}
        for a in rows:
            if a["attribution"] in RELIABLE and a["bundle"]:
                reliable[a["bundle"]] = reliable.get(a["bundle"], 0) + 1
        if reliable:
            winner = max(reliable, key=reliable.get)
            conf = "high" if len(reliable) == 1 else "mixed"
            for a in rows:
                a["bundle"], a["run_confidence"] = winner, conf
            continue

        named = {}
        for a in rows:
            if a["attribution"] == "name" and a["bundle"]:
                named[a["bundle"]] = named.get(a["bundle"], 0) + 1
        if len(named) == 1:
            winner = next(iter(named))
            unanimous = named[winner] >= 2 and named[winner] * 2 >= len(rows)
            for a in rows:
                a["bundle"] = winner if unanimous else ""
                a["run_confidence"] = "medium" if unanimous else "low"
            continue

        for a in rows:
            a["bundle"], a["run_confidence"] = "", "low"
    return agents


def group(agents, key):
    out = {}
    for a in agents:
        k = a.get(key) or "(none)"
        row = out.setdefault(k, {"agents": 0, "usage": blank()})
        row["agents"] += 1
        add(row["usage"], a["usage"])
    for row in out.values():
        row["weighted"] = weighted(row["usage"])
        row["usage"] = tidy(row["usage"])
    return dict(sorted(out.items(), key=lambda kv: -kv[1]["weighted"]))


def template_version(bundle):
    meta = os.path.join(ROOT, "templates", bundle, "%s_meta.yaml" % bundle)
    try:
        with open(meta, encoding="utf-8") as f:
            for line in f:
                m = re.match(r"\s*template_version:\s*[\"']?([0-9][^\"'\s]*)", line)
                if m:
                    return m.group(1)
    except OSError:
        pass
    return "0.0.0"


def build_report(bundle, agents):
    reliable = [a for a in agents if a["attribution"] in RELIABLE]
    totals = blank()
    for a in agents:
        add(totals, a["usage"])
    runs = sorted({a["run"] for a in agents})
    sessions = sorted({a["session"] for a in agents})
    run_confs = {a.get("run_confidence", "low") for a in agents}
    conf = "high" if run_confs == {"high"} else (
        "medium" if run_confs <= {"high", "medium"} else "mixed")
    return {
        "report_schema_version": REPORT_SCHEMA_VERSION,
        "bundle": bundle,
        "template_version": template_version(bundle),
        "attribution_confidence": conf,
        "agents_total": len(agents),
        "agents_reliably_attributed": len(reliable),
        "workflow_runs": len(runs),
        "run_ids": runs,
        "session_ids": sessions,
        "weights": WEIGHTS,
        "prices": {"as_of": PRICES_AS_OF, "source": PRICES_SOURCE,
                   "usd_per_mtok": {m: dict(zip(("input", "cache_write_5m", "cache_write_1h",
                                                 "cache_read", "output"), p))
                                    for m, p in PRICES.items()},
                   "web_search_usd": WEB_SEARCH_USD},
        "stages_present": sorted({a["stage"] for a in agents}),
        "complete": bool({a["stage"] for a in agents} >= {"research", "draft"}),
        "totals": tidy(totals),
        "weighted_total": weighted(totals),
        "cost_usd": round(totals["usd"], 2),
        "by_stage": group(agents, "stage"),
        "by_model": group(agents, "model"),
        "by_requested_tier": group(agents, "requested_model"),
        "by_deliverable": group(agents, "deliverable"),
        "by_attribution": group(agents, "attribution"),
        "agents": sorted(
            [{k: a[k] for k in ("run", "agent_id", "label", "stage", "deliverable",
                                "model", "requested_model", "attribution", "confidence",
                                "file_written", "usage", "weighted")} for a in agents],
            key=lambda a: -a["weighted"],
        ),
    }


def n(v):
    return "{:,}".format(v)


def usd(v):
    return "${:,.2f}".format(v)


def table(title, rows, label_head):
    out = ["### By %s" % title, "",
           "| %s | agents | input | cache write | cache read | output | weighted | list USD |"
           % label_head,
           "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for k, r in rows.items():
        u = r["usage"]
        out.append("| `%s` | %d | %s | %s | %s | %s | **%s** | %s |" % (
            k, r["agents"], n(u["input"]), n(u["cache_write"]),
            n(u["cache_read"]), n(u["output"]), n(r["weighted"]), usd(u["usd"])))
    out.append("")
    return out


def render(rep):
    b, u = rep["bundle"], rep["totals"]
    conf = rep["attribution_confidence"]
    L = []
    L.append("# Build report: `%s` v%s" % (b, rep["template_version"]))
    L.append("")
    L.append("Generated by [`tools/gen-bundle-build-report.py`](../../tools/gen-bundle-build-report.py). "
             "Do not edit by hand.")
    L.append("")
    L.append("Bundle: [`templates/%s/`](../../templates/%s/) - "
             "history: [`%s_history.md`](../../templates/%s/%s_history.md)"
             % (b, b, b, b, b))
    L.append("")
    L.append("## Headline")
    L.append("")
    L.append("| | |")
    L.append("|---|---|")
    L.append("| **Weighted total** | **%s** token-equivalents |" % n(rep["weighted_total"]))
    unpriced = (" plus %s response(s) on a model with no listed price" % n(u["unpriced_turns"])
                if u.get("unpriced_turns") else "")
    L.append("| **At API list rates** | **%s**%s |" % (usd(rep["cost_usd"]), unpriced))
    L.append("| Subagents | %d across %d workflow run(s) |"
             % (rep["agents_total"], rep["workflow_runs"]))
    L.append("| API responses | %s |" % n(u["turns"]))
    L.append("| Fresh input | %s |" % n(u["input"]))
    L.append("| Cache write | %s |" % n(u["cache_write"]))
    L.append("| Cache read | %s |" % n(u["cache_read"]))
    L.append("| Output | %s |" % n(u["output"]))
    L.append("| Server web search / fetch | %s |" % n(u["web"]))
    L.append("| Attribution confidence | **%s** (%d of %d agents reliably attributed) |"
             % (conf, rep["agents_reliably_attributed"], rep["agents_total"]))
    L.append("| Stages captured | %s |" % ", ".join("`%s`" % s for s in rep["stages_present"]))
    L.append("| Covers a whole build | %s |" % ("yes" if rep["complete"] else
                                                "**no, this is a floor**"))
    L.append("")
    if not rep["complete"]:
        L.append("> **This figure is a floor, not a total.** The stages captured above do not "
                 "include both research and drafting, so at least one fan-out of this build is "
                 "missing from the numbers below. The usual cause is a run whose agents wrote no "
                 "file and whose prompts never named the bundle, which is what the labelling "
                 "convention now prevents. Read this as \"at least this much\".")
        L.append("")
    L.append("Weighted total applies %s. It is one fixed unit for every model, stated so that two "
             "reports written months apart are comparable and so a reader can re-weight with their "
             "own numbers. It is not money: a weighted token on Opus costs more than one on Sonnet."
             % weights_text())
    L.append("")
    L.append("The list-USD figures price every API response at its own model's Anthropic API list "
             "rate as of %s ([source](%s)). They are a yardstick for comparing builds, not a bill: "
             "work run under a Claude subscription is not charged per token." % (
                 rep["prices"]["as_of"], rep["prices"]["source"]))
    L.append("")
    L += table("stage", rep["by_stage"], "stage")
    L += table("model", rep["by_model"], "resolved model")
    L += table("requested tier", rep["by_requested_tier"], "requested")
    L += table("deliverable", rep["by_deliverable"], "deliverable")
    L.append("## What this report does not measure")
    L.append("")
    L.append("- **Reasoning effort.** It is not recorded anywhere in the transcript tree. Only the "
             "requested model tier is, and it is reported above.")
    L.append("- **The orchestrator's own spend.** One session interleaves several bundles and other "
             "work, so the main loop's tokens cannot honestly be divided per bundle. They are not "
             "billed to a bundle here, and they are not reported anywhere else either.")
    if conf != "high":
        L.append("- **Exact attribution.** This build predates the labelling convention, so some "
                 "agents were attributed from their own prompt rather than from a label. "
                 "See the by-attribution counts in the raw JSON.")
    L.append("")
    L.append("Raw data: [`%s_v%s.json`](%s_v%s.json)."
             % (b, rep["template_version"], b, rep["template_version"]))
    L.append("")
    return "\n".join(L)


def write_text(path, text):
    # newline="\n" because .gitattributes pins *.md and *.json to LF. Writing platform newlines
    # would rewrite the whole file on the next commit on Windows.
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


# --------------------------------------------------------------------------------------- index

def load_reports():
    if not os.path.isdir(REPORT_DIR):
        return []
    out = []
    for fn in sorted(os.listdir(REPORT_DIR)):
        if not fn.endswith(".json"):
            continue
        try:
            with open(os.path.join(REPORT_DIR, fn), encoding="utf-8") as f:
                out.append(json.load(f))
        except (OSError, ValueError):
            continue
    return out


def render_index(reports):
    reports = sorted(reports, key=lambda r: -r["weighted_total"])
    L = []
    L.append("# Bundle build reports")
    L.append("")
    L.append("Generated by [`tools/gen-bundle-build-report.py`](../tools/gen-bundle-build-report.py). "
             "Do not edit by hand.")
    L.append("")
    L.append("What each build of a bundle actually cost, measured from the harness transcripts "
             "rather than estimated. Read [`README.md`](README.md) for what these numbers are and "
             "are not.")
    L.append("")
    if not reports:
        L.append("**No reports yet.**")
        L.append("")
        return "\n".join(L)
    tot = sum(r["weighted_total"] for r in reports)
    tot_usd = sum(r.get("cost_usd", 0.0) for r in reports)
    hi = [r for r in reports if r["attribution_confidence"] == "high"]
    L.append("| Bundle | Version | Weighted | List USD | Agents | Runs | Scope | Confidence | Report |")
    L.append("|---|---|---:|---:|---:|---:|---|---|---|")
    for r in reports:
        b, v = r["bundle"], r["template_version"]
        L.append("| `%s` | %s | %s | %s | %d | %d | %s | %s | [report](reports/%s_v%s.md) |"
                 % (b, v, n(r["weighted_total"]), usd(r.get("cost_usd", 0.0)),
                    r["agents_total"], r["workflow_runs"],
                    "whole build" if r.get("complete") else "**floor**",
                    r["attribution_confidence"], b, v))
    L.append("")
    L.append("<!-- build-reports: count=%d high=%d weighted=%d -->" % (len(reports), len(hi), tot))
    L.append("")
    L.append("**%d reports, %d of them at high attribution confidence, %s weighted "
             "token-equivalents and %s at API list rates in total.**"
             % (len(reports), len(hi), n(tot), usd(tot_usd)))
    L.append("")
    L.append("Weighted applies %s to the raw counts. List USD prices each response at its own "
             "model's API list rate as of %s; it is a yardstick, not a bill."
             % (weights_text(), PRICES_AS_OF))
    L.append("")
    return "\n".join(L)


# ---------------------------------------------------------------------------------------- main

def do_ingest(dry_run):
    ids, patterns = load_known_bundles()
    agents, root = collect(ids, patterns)
    if not agents:
        print(RED + "NO DATA" + OFF + "  no workflow transcripts under " + root)
        print(DIM + "  Transcripts are machine-local. Ingest on the machine that ran the build."
              + OFF)
        return 1
    resolve_runs(agents)
    by_bundle = {}
    for a in agents:
        if a["bundle"]:
            by_bundle.setdefault(a["bundle"], []).append(a)
    if not by_bundle:
        print(RED + "NO DATA" + OFF + "  %d agents found, none reliably attributed." % len(agents))
        return 1
    written = []
    for bundle, rows in sorted(by_bundle.items()):
        rep = build_report(bundle, rows)
        stem = os.path.join(REPORT_DIR, "%s_v%s" % (bundle, rep["template_version"]))
        if not dry_run:
            write_text(stem + ".json", json.dumps(rep, indent=2, sort_keys=False) + "\n")
            write_text(stem + ".md", render(rep))
        written.append((bundle, rep["weighted_total"], rep["agents_total"]))
    unattributed = [a for a in agents if not a["bundle"]]
    if not dry_run:
        write_text(INDEX_PATH, render_index(load_reports()))
    verb = "would write" if dry_run else "wrote"
    print(GREEN + "OK" + OFF + "  %s %d report(s) from %d agent(s) under %s"
          % (verb, len(written), len(agents), root))
    for bundle, w, count in sorted(written, key=lambda t: -t[1]):
        print("      %-36s %14s weighted  (%d agents)" % (bundle, n(w), count))
    if unattributed:
        skipped = {}
        for a in unattributed:
            key = a.get("run_confidence", "low")
            skipped[key] = skipped.get(key, 0) + 1
        print(DIM + "      %d agent(s) not reliably attributed and left out: %s"
              % (len(unattributed), ", ".join("%s=%d" % kv for kv in sorted(skipped.items())))
              + OFF)
    return 0


def main():
    argv = sys.argv[1:]
    if "--ingest" in argv:
        return do_ingest("--dry-run" in argv)

    reports = load_reports()
    fresh = render_index(reports)
    if "--check" in argv:
        if not os.path.isfile(INDEX_PATH):
            print(RED + "DRIFT" + OFF + "  bundle-builds/INDEX.md is missing; "
                  "run python tools/gen-bundle-build-report.py")
            return 1
        with open(INDEX_PATH, encoding="utf-8") as f:
            current = f.read()
        if current != fresh:
            print(RED + "DRIFT" + OFF + "  bundle-builds/INDEX.md does not match the %d committed "
                  "report(s); run python tools/gen-bundle-build-report.py" % len(reports))
            return 1
        print(GREEN + "OK" + OFF + "  bundle-builds/INDEX.md is fresh: %d report(s)."
              % len(reports))
        print(DIM + "      This checks the index against the committed reports. It cannot check "
              "the reports against the transcripts, which are machine-local." + OFF)
        return 0

    write_text(INDEX_PATH, fresh)
    print(GREEN + "OK" + OFF + "  wrote bundle-builds/INDEX.md: %d report(s)." % len(reports))
    return 0


if __name__ == "__main__":
    sys.exit(main())
