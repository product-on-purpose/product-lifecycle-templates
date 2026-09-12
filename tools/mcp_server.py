#!/usr/bin/env python3
"""
mcp_server.py - serve this library's templates to an agent over MCP.

WHY IT IS PYTHON, AND WHY IT LIVES HERE.
The 2026-07-12 audit sketch specified a separate TypeScript npm package mirroring `pm-skills-mcp`, with
an embed step packaging `templates/**` into the published artifact. That was not adopted. See
ADR 0045, `docs/internal/decisions/0045-the-mcp-server-is-python-and-lives-in-this-repository.md`; the
short version is that the recommended install route already clones this whole repository, so there is
nothing to embed, and an embedded copy would be a fifth artifact that can drift from the tree.

WHAT IT REFUSES TO DO.
Reimplement `validate-fill.py` or `strip-template.py`. Both are loaded and CALLED, so "the server agrees
with the CLI" is true by construction rather than by a parity test somebody has to keep running. The two
tools are the implementation; these are wrappers of about ten lines each.

THE BUDGET IS A DISCOVERY CONTRACT, NOT A GLOBAL ONE.
Discovery responses stay small so an agent can choose cheaply. Retrieval costs what the artifact costs: a
template IS the payload, and the largest is roughly 3,300 tokens. So every discovery response carries
`approx_tokens` per variant and the agent knows the price before it pays. `parts` therefore defaults to
`["template"]` alone; the sketch's template+guide default roughly doubles the median payload for a part
most callers do not want on the first fetch.

THE SDK, AND WHY `pip install mcp` IS THE WRONG COMMAND.
This module needs `FastMCP` at `mcp.server.fastmcp`, which exists only in the SDK's 1.x line. **The SDK
released v2 on 2026-07-28 and renamed `FastMCP` to `MCPServer`**, so a plain `pip install mcp` resolves to
a 2.x, succeeds, exits zero, installs twenty packages, and leaves this server unable to import. The
install command is therefore:

    python3 -m pip install "mcp<2"

The pin is a deliberate hold, not permanent advice: it stands until this module is ported to v2's
`MCPServer`, and v1 will stop receiving fixes before that becomes comfortable. Whoever does that port
removes the pin here, in `.github/workflows/ci.yml`, and in `docs/how-to/installing.md` together.

That this was wrong for the whole of `v0.6.0` is the point worth keeping. The advice was written against
1.27.2 while 2.0.0 was already the default install, and nothing caught it, because the CI self-test
SKIPPED its one SDK-dependent assertion and exited 0 rather than failing. `tools/test-mcp-server.py
--require-sdk` now fails instead. A check that returns SOMETHING is not one that returns the RIGHT thing.

If the SDK is absent the module still imports and every tool function still works and is testable; only
`serve` needs it, and it says so rather than failing obscurely.

Usage:
    python tools/mcp_server.py            # serve over stdio (what .mcp.json runs)
    python tools/mcp_server.py --selftest # report what it would serve, run no server
"""
import argparse
import importlib.util
import io
import json
import os
import re
import sys
from contextlib import redirect_stdout

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
TEMPLATES = os.path.join(ROOT, "templates")

# The out cap from the sketch, retained. It never fires on the default path, which is the point of a
# safety valve: a cap you hit routinely is a budget, and this is not one.
OUT_CAP_TOKENS = 8000
MAX_CANDIDATES = 8

PARTS = {
    "template": None,          # resolved per variant; the others are one file per bundle
    "guide": "_guide.md",
    "companion": "_companion.md",
    "example": "_example.md",
}

_RUBRIC_RE = re.compile(r"^##\s+.*\brubric\b.*$", re.M | re.I)
_ANTI_RE = re.compile(r"^##\s+.*anti-pattern.*$", re.M | re.I)
_H2_RE = re.compile(r"^##\s+", re.M)

# ADR 0003 fixed the phase vocabulary at these six to match the pm-skills seam exactly.
ADR_0003_PHASES = ["discover", "define", "develop", "deliver", "measure", "iterate"]

# Dropped before scoring. A caller asks in a sentence ("I need to write down what done means"), and
# without this every bundle scores on the connective tissue rather than on the words that carry intent.
STOPWORDS = {
    "a", "an", "the", "i", "to", "for", "of", "in", "on", "is", "it", "and", "or", "no", "not",
    "be", "am", "are", "was", "my", "me", "we", "our", "you", "your", "that", "this", "these",
    "do", "does", "how", "what", "when", "which", "with", "need", "needs", "want", "wants", "some",
    "thing", "things", "down", "up", "out", "about", "make", "have", "has", "get", "one", "any",
}


# ---------------------------------------------------------------- loading the tree


def _load_module(filename, name):
    """Import one of the hyphenated tool scripts. `validate-fill.py` is not a legal module name."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(SCRIPT_DIR, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _json(name):
    return json.loads(_read(os.path.join(ROOT, name)))


def library_version():
    """Read, never hardcoded. Every retyped number in this repository has eventually gone stale."""
    return _json("library.json").get("version", "unknown")


def manifest():
    return _json("manifest.json")["bundles"]


def estimate_tokens(text):
    """characters / 4, rounded to the nearest 50 - the same method `gen-manifest.py` uses.

    The same method, so a variant's cost reported here and its `approx_tokens` in the manifest cannot
    disagree. That is a stronger guarantee than asserting they agree within some tolerance.
    """
    return round(len(text) / 4 / 50) * 50


# ---------------------------------------------------------------- variant addressing


def variant_file(bundle_id, fmt, size, default_format):
    """The filename, per ADR 0028's convention. The format segment is omitted for the default format."""
    stem = size if fmt == default_format else fmt + "-" + size
    return bundle_id + "_template-" + stem + ".md"


def variants(bundle):
    """Every (format, size) this bundle actually ships, default format first.

    Reads `sizes_available` (the DEFAULT format's sizes) plus `additional_formats[].sizes`. A
    non-default format does not necessarily carry every size: `product-roadmap` ships `go` and `themes`
    in `full` only, so enumerating the cross product would invent two files that do not exist.
    """
    default_fmt = bundle.get("default_format")
    out = [(default_fmt, s) for s in bundle.get("sizes_available", [])]
    for extra in bundle.get("additional_formats", []):
        out += [(extra["id"], s) for s in extra.get("sizes", [])]
    return out


def axis_values():
    """What the taxonomy axis ACTUALLY holds, generated from the tree rather than typed.

    The axis is `phase` XOR `classification`: 17 bundles carry a phase, 10 a classification, none both
    and none neither. A `phase`-only filter - which is what the AG-2 sketch specified - can never reach
    those 10, and would return a plausible non-empty result while silently hiding 37% of the library.

    ADR 0003 fixed the phase VOCABULARY at six values and left "does this library need a second axis?"
    open. The tree has since answered yes. Only four of the six phase values are used by any built
    bundle, so a teachable error listing all six sends an agent looking for bundles that do not exist.
    This returns what is there, and separately what is allowed but unused.
    """
    bundles = manifest()
    phases = sorted({b["phase"] for b in bundles if "phase" in b})
    classes = sorted({b["classification"] for b in bundles if "classification" in b})
    return {
        "phase": phases,
        "classification": classes,
        "phase_declared_but_unused": [p for p in ADR_0003_PHASES if p not in phases],
    }


def _axis_of(bundle):
    return bundle.get("phase") or bundle.get("classification")


# ---------------------------------------------------------------- the five tools


def search_templates(query, axis=None, max_results=3):
    """Find template bundles by intent. Discovery: this response is small on purpose.

    Args:
        query: what the caller is trying to write, in their own words.
        axis: optional filter. Accepts a `phase` OR a `classification` value, because the library uses
            one or the other per bundle and never both.
        max_results: 1 to 8. Three candidates cost roughly 400 tokens, eight roughly 1,200.
    """
    max_results = max(1, min(int(max_results), MAX_CANDIDATES))
    q = (query or "").strip().lower()
    terms = [t for t in re.split(r"[^a-z0-9]+", q) if t and t not in STOPWORDS]

    scored = []
    for b in manifest():
        if axis and _axis_of(b) != axis:
            continue
        hay_alias = " ".join(b.get("aliases", [])).lower()
        hay_tags = " ".join(b.get("tags", [])).lower()
        title, summary = b.get("title", "").lower(), b.get("summary", "").lower()
        score = 0
        if q and q == b["id"].lower():
            score += 100
        if q and q in hay_alias:
            score += 40
        for t in terms:
            score += 12 * _word(t, b["id"]) + 8 * _word(t, hay_alias) + 6 * _word(t, title)
            score += 3 * _word(t, hay_tags) + 1 * _word(t, summary)
        if score or not terms:
            scored.append((score, b["id"], b))

    scored.sort(key=lambda x: (-x[0], x[1]))
    candidates = [_candidate(b) for _, _, b in scored[:max_results]]

    out = {"query": query, "candidates": candidates, "total_matched": len(scored),
           "library_version": library_version()}
    if not candidates:
        out["nothing_matched"] = {
            "axis_values": axis_values(),
            "try": ["prd", "acceptance criteria for a story", "how do I write a postmortem"],
            "note": "`axis` accepts a phase OR a classification value. A phase value alone can only "
                    "reach the bundles that carry a phase, which is not all of them.",
        }
    return out


def _word(term, haystack):
    """Whole-word match.

    Substring matching looked fine and was not. `thing` matched inside `Something`, `no` inside `note`,
    so a query naming nothing in the library still scored above zero on most bundles - which made the
    teachable empty-result branch unreachable, because the result was never empty. A ranking that always
    returns something is the same defect as a check that always passes.
    """
    return 1 if re.search(r"\b" + re.escape(term) + r"\b", haystack) else 0


def _candidate(b):
    """The manifest's own field names.

    A response carrying `bundle_id` or `one_line_summary` is wrong: those names come from the sketch and
    exist nowhere in the tree.

    `sizing_guidance` is deliberately NOT here, and its absence is the one place this server departs
    from its own spec's field list. Measured, it is 632 characters on the worst bundle - 158 tokens per
    candidate, 474 of the 1,194 a three-candidate response cost with it - against a 500-token discovery
    budget the spec set without measuring the payload it had itself specified. It is also prose for
    AFTER a bundle is chosen, when picking lean against full, so `get_template` returns it and
    discovery does not carry it. See the spec's section 5.
    """
    return {
        "id": b["id"],
        "title": b.get("title"),
        "summary": b.get("summary"),
        "doc_type": b.get("doc_type"),
        "family": b.get("family"),
        "axis": _axis_of(b),
        "status": b.get("status"),
        "default_format": b.get("default_format"),
        "default_size": b.get("default_size"),
        "sizes_available": b.get("sizes_available", []),
        "additional_formats": [f["id"] for f in b.get("additional_formats", [])],
        "approx_tokens": b.get("approx_tokens", {}),
        "tags": b.get("tags", []),
        "aliases": b.get("aliases", []),
    }


def _find(bundle_id):
    for b in manifest():
        if b["id"] == bundle_id:
            return b
    return None


def get_template(bundle_id, size=None, fmt=None, parts=None):
    """Fetch one template variant, and optionally its guide, companion or example.

    Retrieval costs what the artifact costs. Every response reports the price it charged, and
    `search_templates` reported it before the caller paid.

    Args:
        bundle_id: the `id` from a search candidate.
        size: `lean` or `full`. Defaults to the bundle's `default_size`.
        fmt: the format id. Defaults to the bundle's `default_format`.
        parts: any of `template`, `guide`, `companion`, `example`. Defaults to `["template"]` alone.
    """
    b = _find(bundle_id)
    if b is None:
        return {"error": "no such bundle: " + str(bundle_id),
                "did_you_mean": [c["id"] for c
                                 in search_templates(bundle_id, max_results=3)["candidates"]]}

    fmt = fmt or b.get("default_format")
    size = size or b.get("default_size")
    available = variants(b)
    if (fmt, size) not in available:
        return {"error": "no such variant: %s format=%s size=%s" % (bundle_id, fmt, size),
                "available": [{"format": f, "size": s} for f, s in available],
                "note": "A non-default format does not necessarily ship every size."}

    parts = list(parts or ["template"])
    unknown = [p for p in parts if p not in PARTS]
    if unknown:
        return {"error": "unknown part(s): " + ", ".join(unknown),
                "available_parts": sorted(PARTS)}

    d = os.path.join(TEMPLATES, bundle_id)
    out_parts, total = {}, 0
    for p in parts:
        path = (os.path.join(d, variant_file(bundle_id, fmt, size, b.get("default_format")))
                if p == "template" else os.path.join(d, bundle_id + PARTS[p]))
        if not os.path.isfile(path):
            out_parts[p] = {"error": "this bundle ships no " + p}
            continue
        text = _read(path)
        tokens = estimate_tokens(text)
        total += tokens
        out_parts[p] = {"file": os.path.basename(path), "approx_tokens": tokens, "content": text}

    result = {
        "id": bundle_id, "format": fmt, "size": size,
        "parts": out_parts,
        # Carried here rather than on every search candidate: it is what you read once you have
        # chosen the bundle and are choosing the size.
        "sizing_guidance": b.get("sizing_guidance"),
        "approx_tokens_total": total,
        "template_version": _template_version(bundle_id),
        "library_version": library_version(),
    }
    if total > OUT_CAP_TOKENS:
        for p in out_parts.values():
            p.pop("content", None)
        result["refused"] = ("%d approx tokens exceeds the %d cap. Content withheld; request fewer "
                             "parts." % (total, OUT_CAP_TOKENS))
    return result


def _template_version(bundle_id):
    """From the meta, by line scan.

    The gate's check J already validates every meta against the schema, so a regex is enough here and
    keeps the server from depending on PyYAML.
    """
    path = os.path.join(TEMPLATES, bundle_id, bundle_id + "_meta.yaml")
    if not os.path.isfile(path):
        return None
    m = re.search(r"^template_version:\s*(\S+)", _read(path), re.M)
    return m.group(1).strip().strip("\"'") if m else None


def get_grading_pack(bundle_id):
    """Fetch the guide sections a grader needs: the quality rubric and the named anti-patterns.

    Measured: all 27 guides carry a rubric heading; FOUR (`okrs`, `product-roadmap`,
    `product-strategy`, `product-vision`) carry no anti-patterns section. Absence is reported in
    `missing` rather than passed over, because a pack quietly short a section looks complete and is not.
    """
    b = _find(bundle_id)
    if b is None:
        return {"error": "no such bundle: " + str(bundle_id)}
    path = os.path.join(TEMPLATES, bundle_id, bundle_id + "_guide.md")
    if not os.path.isfile(path):
        return {"error": "this bundle ships no guide", "id": bundle_id}

    text = _read(path)
    sections = {}
    for key, pattern in (("rubric", _RUBRIC_RE), ("anti_patterns", _ANTI_RE)):
        body = _section(text, pattern)
        if body:
            sections[key] = {"approx_tokens": estimate_tokens(body), "content": body}

    return {
        "id": bundle_id,
        "sections": sections,
        "missing": [k for k in ("rubric", "anti_patterns") if k not in sections],
        "approx_tokens_total": sum(s["approx_tokens"] for s in sections.values()),
        "whole_guide_approx_tokens": estimate_tokens(text),
        "template_version": _template_version(bundle_id),
        "library_version": library_version(),
        "not_verified": "That a rubric score is deserved. No check scores a rubric; a reader does.",
    }


def _section(text, header_re):
    """One `##` section: its header through the line before the next `##`."""
    m = header_re.search(text)
    if not m:
        return None
    nxt = _H2_RE.search(text, m.end())
    return text[m.start():nxt.start() if nxt else len(text)].rstrip() + "\n"


def validate_fill(path):
    """Check a filled document against the template it declares it came from.

    Wraps `tools/validate-fill.py` by calling its `validate()`, so the server and the CLI cannot
    disagree about what passes.
    """
    if not os.path.isfile(path):
        return {"ok": False, "error": "no such file: " + str(path)}
    mod = _load_module("validate-fill.py", "plt_validate_fill")
    ok, findings = mod.validate(path)
    return {"file": os.path.basename(path), "ok": ok,
            "findings": [{"level": l, "message": m} for l, m in findings],
            "not_verified": "Whether any section says anything worth reading. This checks that the "
                            "shape survived the fill, never that the content is good."}


def stamp_and_strip(path, filled_by, fill_method="manual", out=None, allow_placeholders=False):
    """Remove the guidance comments from a filled template and stamp who filled it, when, and how.

    Wraps `tools/strip-template.py` by calling its `main()`, so its refusal rules ARE the rules here.
    In particular the placeholder refusal scans the STRIPPED body, because guidance comments name
    placeholders as instruction and scanning raw text would refuse every document forever.
    """
    if not os.path.isfile(path):
        return {"ok": False, "exit_code": 1, "error": "no such file: " + str(path)}
    mod = _load_module("strip-template.py", "plt_strip_template")
    argv = [path, "--fill-method", fill_method]
    if filled_by:
        argv += ["--filled-by", filled_by]
    if out:
        argv += ["--out", out]
    if allow_placeholders:
        argv += ["--allow-placeholders"]

    buf = io.StringIO()
    with redirect_stdout(buf):
        code = mod.main(argv)
    return {"ok": code == 0, "exit_code": code, "refused": code == 2,
            "output": _strip_ansi(buf.getvalue()),
            "note": "exit 2 means it refused and wrote nothing, which is the intended outcome for a "
                    "document that still carries an unfilled placeholder."}


def _strip_ansi(s):
    return re.sub(r"\033\[[0-9;]*m", "", s)


# ---------------------------------------------------------------- the MCP surface

TOOLS = [search_templates, get_template, get_grading_pack, validate_fill, stamp_and_strip]


def build_server():
    """Register the five tools. Raises ImportError with a usable message if the SDK is absent."""
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError as e:      # pragma: no cover - only without the SDK installed
        # The interpreter is NAMED, because one likely cause is not a missing package but the wrong
        # Python. `python`, `python3` and `py` routinely resolve to three different interpreters on one
        # machine, and "pip install mcp" is unhelpful advice to someone who already did.
        #
        # The VERSION is named for the other likely cause, and it is the one this message got wrong for
        # the whole of v0.6.0: it used to say `pip install mcp`, which since 2026-07-28 installs a 2.x
        # that renamed `FastMCP` to `MCPServer`. Following the advice landed the reader back here with
        # the identical error and twenty packages installed. The pin is what makes the command work.
        raise ImportError(
            "the MCP Python SDK is not importable from %s.\n"
            "Either install it there (%s -m pip install \"mcp<2\"), or point .mcp.json's `command` at "
            "an interpreter that has it. `python`, `python3` and `py` are frequently three different "
            "interpreters on the same machine.\n"
            "The `<2` is required, not cautious: the SDK's v2 renamed `FastMCP` to `MCPServer`, so a "
            "plain `pip install mcp` succeeds and still cannot be imported by this module.\n"
            "Every tool function in this module still works and is testable without the SDK; only "
            "serving needs it." % (sys.executable, sys.executable)
        ) from e

    server = FastMCP("product-lifecycle-templates")
    for fn in TOOLS:
        server.tool()(fn)
    return server


def selftest():
    """Report what would be served. Says what it did NOT check, like every other tool here."""
    bundles = manifest()
    n_variants = sum(len(variants(b)) for b in bundles)
    print("product-lifecycle-templates MCP server")
    print("  library version   %s" % library_version())
    print("  bundles           %d" % len(bundles))
    print("  variants          %d addressable (format x size)" % n_variants)
    print("  tools             %d: %s" % (len(TOOLS), ", ".join(f.__name__ for f in TOOLS)))
    ax = axis_values()
    print("  axis values       phase %s" % (ax["phase"],))
    print("                    classification %s" % (ax["classification"],))
    if ax["phase_declared_but_unused"]:
        print("                    declared by ADR 0003, used by no bundle: %s"
              % (ax["phase_declared_but_unused"],))
    try:
        build_server()
        print("  SDK               present; the server would start")
    except ImportError:
        print("  SDK               ABSENT (pip install \"mcp<2\" - the pin is required; v2 renamed")
        print("                    FastMCP to MCPServer). Tool functions work; serving does not.")
    print()
    print("  not checked: that any response is USEFUL. This counts what is addressable, which is a")
    print("  different claim from serving the right thing. tools/test-mcp-server.py checks contracts.")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="mcp_server.py",
                                 description="Serve this library's templates over MCP.")
    ap.add_argument("--selftest", action="store_true",
                    help="report what would be served and exit")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    build_server().run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
