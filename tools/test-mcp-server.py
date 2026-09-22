#!/usr/bin/env python3
"""
test-mcp-server.py - the adversarial test for the MCP server.

WHAT THIS COVERS.
The seven acceptance criteria in `docs/internal/ag2-mcp-spec.md` section 5, each one an assertion here,
plus the failure modes that would let a broken server look healthy.

THE LOAD-BEARING CASE IS THE PARITY ONE.
`validate_fill` and `stamp_and_strip` must agree exactly with the CLI tools they wrap. The server calls
those tools rather than reimplementing them, so the assertion is cheap - but it is asserted anyway,
because "it is the same code" is a claim about the code as written today and a test is a claim about the
code as it runs. Both the passing and the REFUSING paths are compared: a wrapper that swallowed a
refusal and reported success would pass a test that only ever fed it good documents.

THE FAILURE THAT WOULD BE INVISIBLE.
A search that silently drops a third of the library. The taxonomy axis is `phase` XOR `classification`,
and the AG-2 sketch specified a `phase` filter alone - which returns a plausible non-empty result while
ten bundles become unreachable. That is this session's recurring defect shape: a check, or a filter, that
returns SOMETHING is not one that returns the RIGHT thing. So the axis assertions below check not that
filtering works, but that every bundle in the tree is reachable by some filter value.

THE SKIP THAT MADE THIS SUITE LOOK HEALTHY FOR ITS WHOLE LIFE.
The SDK-dependent assertion skips loudly rather than silently when `mcp` is absent, which is right for a
contributor and was wrong for CI. The SDK's v2 renamed `FastMCP` to `MCPServer` on 2026-07-28; the
workflow installed `mcp` unpinned, so every CI run since WP-51 shipped on 2026-09-06 got a 2.x this
server cannot import, skipped this one assertion, printed OK, and exited 0. Nothing had ever verified
that the server starts. `--require-sdk` makes that skip a failure, and CI passes it.

Pure standard library.
Usage: python tools/test-mcp-server.py               # skips the SDK assertion if `mcp` is absent
       python tools/test-mcp-server.py --require-sdk # that skip becomes a failure (what CI runs)
"""
import importlib.util
import json
import os
import shutil
import sys
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))

GREEN, RED, YELLOW, DIM, OFF = "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[0m"

# `--require-sdk` turns the one SDK-dependent skip below into a FAILURE. CI passes it; a contributor
# without the SDK installed does not, and still gets a loud skip rather than a broken checkout.
#
# It exists because the skip was load-bearing in the wrong direction. The SDK's v2 (2026-07-28) renamed
# `FastMCP` to `MCPServer`; CI installed `mcp` unpinned, so from the day WP-51 shipped it got a 2.x the
# server cannot import, this assertion skipped, and the suite printed OK and exited 0. The gate the
# roadmap calls a CI self-test had never once verified the server could start. Pinning `mcp<2` in the
# workflow fixes today's break; this flag is what makes the NEXT rename fail loudly instead of shrinking
# the suite. Deliberately narrow: it does not promote the environmental skip at the 8k-cap assertion,
# which is a true "this tree cannot exercise it" and not a missing dependency.
REQUIRE_SDK = "--require-sdk" in sys.argv


def _load(filename, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(SCRIPT_DIR, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


srv = _load("mcp_server.py", "plt_mcp_server")
val = _load("validate-fill.py", "plt_validate_fill_t")
strip = _load("strip-template.py", "plt_strip_template_t")

results = []
skipped = []


def check(label, passed, detail=""):
    results.append(passed)
    print("  " + (GREEN + "PASS" + OFF if passed else RED + "FAIL" + OFF) + "  " + label)
    if not passed and detail:
        print("        got: " + str(detail)[:400])


def skip(label, why):
    skipped.append((label, why))
    print("  " + YELLOW + "SKIP" + OFF + "  " + label + DIM + " - " + why + OFF)


def D(resp):
    """Unwrap the success branch, asserting the envelope shape on the way through (ADR 0054).

    Every tool now returns {"ok": bool, "data"|"error": ...}. These two helpers keep the domain
    assertions below readable while still failing loudly if a call lands on the wrong branch.
    """
    assert isinstance(resp, dict) and "ok" in resp, "response is not an envelope: %r" % (resp,)
    assert resp["ok"] is True, "expected the success branch, got error: %r" % (resp.get("error"),)
    assert "data" in resp, "ok: True with no data: %r" % (resp,)
    return resp["data"]


def E(resp):
    """Unwrap the error branch, asserting the envelope shape."""
    assert isinstance(resp, dict) and "ok" in resp, "response is not an envelope: %r" % (resp,)
    assert resp["ok"] is False, "expected the error branch, got data: %r" % (resp.get("data"),)
    assert "error" in resp, "ok: False with no error: %r" % (resp,)
    return resp["error"]


def approx_tokens_of(obj):
    """The size of a RESPONSE, by the same characters/4 the library uses for artifacts."""
    return len(json.dumps(obj)) / 4


def build_filled(bundle="prd", size="lean", stamped=False):
    """A complete filled document, sections taken FROM THE SCHEMA rather than hand-written.

    Hand-writing headings makes a fixture drift the moment a template gains a section, and it fails in
    the most confusing way available: the validator correctly reporting sections missing.

    `stamped` matters. A document straight out of a fill has no `filled_by` / `fill_method` /
    `fill_date`: those are what `strip-template.py` ADDS, and `validate-fill.py` requires them. So the
    unstamped fixture is what the strip step consumes and the stamped one is what validation accepts.
    Using one fixture for both made the validator correctly fail a document this test called good.
    """
    schema = val.load_schema()
    declared, err = val.find_variant(schema, bundle, None, size)
    assert not err, err
    prov = 'filled_by: "tester"\nfill_method: manual\nfill_date: 2026-09-06\n' if stamped else ""
    head = ('---\ntitle: "A Real PRD"\ndoc_type: %s\nsize: %s\nstatus: draft\n'
            'source_template: %s\nsource_template_version: %s\n%s---\n\n# A Real PRD\n'
            % (bundle, size, bundle, srv._template_version(bundle), prov))
    body = "".join("\n" + "#" * s["level"] + " " + s["title"] + "\n\nSomething.\n" for s in declared)
    return head + body


def tmpdoc(text, name="doc.md"):
    d = tempfile.mkdtemp(prefix="mcp-test-")
    p = os.path.join(d, name)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return d, p


def main():
    print("test-mcp-server.py")
    print()

    bundles = srv.manifest()
    lib = json.loads(open(os.path.join(ROOT, "library.json"), encoding="utf-8").read())

    # ---------------------------------------------------------------- AC 7
    print(DIM + "  AC7: the server reports the library version it was built from" + OFF)
    check("library_version is read from library.json, not hardcoded",
          srv.library_version() == lib["version"], srv.library_version())
    check("every tool response carries library_version",
          all("library_version" in r for r in (
              D(srv.search_templates("prd")),
              D(srv.get_template("prd")),
              D(srv.get_grading_pack("prd")))))

    # ---------------------------------------------------------------- AC 1
    # The budget is 800, not the spec's original 500, and the change is a measurement rather than a
    # concession. Three candidates carrying `sizing_guidance` cost 1,194 tokens on the worst bundle -
    # that field alone averages 632 characters. The spec set 500 without measuring the field list the
    # spec itself prescribed, which is the ninth falsified budget in this lineage and the first that
    # was ours rather than the 2026-07-12 sketch's. `sizing_guidance` moved to `get_template`, where it
    # is actually read, and 800 is the measured worst case plus room for one long summary.
    print(DIM + "\n  AC1: 3 candidates under 800 approx tokens, for all 30 bundles" + OFF)
    worst, worst_id = 0, None
    for b in bundles:
        r = D(srv.search_templates(b["title"], max_results=3))
        t = approx_tokens_of(r)
        if t > worst:
            worst, worst_id = t, b["id"]
    check("worst-case 3-candidate response is under 800 approx tokens (%d, on %s)"
          % (worst, worst_id), worst < 800, worst)
    check("no candidate carries sizing_guidance, which is post-selection prose",
          all("sizing_guidance" not in c for c in D(srv.search_templates("prd"))["candidates"]))
    check("get_template DOES carry sizing_guidance, so it is moved rather than lost",
          D(srv.get_template("prd")).get("sizing_guidance"))
    check("max_results is capped at 8",
          len(D(srv.search_templates("", max_results=99))["candidates"]) <= srv.MAX_CANDIDATES)

    # ---------------------------------------------------------------- AC 3
    print(DIM + "\n  AC3: responses use the manifest's field names, not the sketch's" + OFF)
    cand = D(srv.search_templates("prd"))["candidates"][0]
    check("candidate carries `id` and `summary`", "id" in cand and "summary" in cand, sorted(cand))
    check("candidate carries NEITHER `bundle_id` NOR `one_line_summary`",
          "bundle_id" not in cand and "one_line_summary" not in cand, sorted(cand))
    check("candidate carries no invented `conformance` field", "conformance" not in cand)
    check("candidate carries `status`, which the manifest does have", "status" in cand)

    # ---------------------------------------------------------------- AC 4
    print(DIM + "\n  AC4: every variant in the tree is addressable" + OFF)
    total, unreachable, mismatched = 0, [], []
    for b in bundles:
        for fmt, size in srv.variants(b):
            total += 1
            r = D(srv.get_template(b["id"], size=size, fmt=fmt))
            if "error" in r or not r["parts"]["template"].get("content"):
                unreachable.append((b["id"], fmt, size))
                continue
            # AC2's tolerance is 10%. The server uses gen-manifest's own function, so require EXACT.
            key = size if fmt == b.get("default_format") else fmt + "-" + size
            if r["parts"]["template"]["approx_tokens"] != b["approx_tokens"].get(key):
                mismatched.append((b["id"], key,
                                   r["parts"]["template"]["approx_tokens"],
                                   b["approx_tokens"].get(key)))
    check("all %d variants fetch content" % total, not unreachable, unreachable)
    check("the tree has 63 variants and all 63 are addressable", total == 63, total)
    check("every reported token count EQUALS manifest.json's approx_tokens (not merely within 10%)",
          not mismatched, mismatched[:4])

    # ---------------------------------------------------------------- AC 2
    print(DIM + "\n  AC2: the default fetch returns exactly one artifact, priced" + OFF)
    r = D(srv.get_template("prd"))
    check("default `parts` returns exactly one part", list(r["parts"]) == ["template"], list(r["parts"]))
    check("default part is the template, not template+guide", "guide" not in r["parts"])
    check("the response reports approx_tokens_total", isinstance(r.get("approx_tokens_total"), int))
    check("the default variant is the bundle's declared default",
          (r["format"], r["size"]) == (srv._find("prd").get("default_format"),
                                       srv._find("prd")["default_size"]))

    # ---------------------------------------------------------------- the axis falsification
    print(DIM + "\n  The axis is phase XOR classification - every bundle must be reachable" + OFF)
    ax = srv.axis_values()
    reachable = set()
    for v in ax["phase"] + ax["classification"]:
        reachable |= {c["id"] for c in D(srv.search_templates("", axis=v, max_results=99))["candidates"]}
    check("every one of the %d bundles is reachable by some axis value" % len(bundles),
          reachable == {b["id"] for b in bundles},
          sorted({b["id"] for b in bundles} - reachable))
    check("a phase-only filter reaches FEWER than all bundles, which is why `axis` takes both",
          len({b["id"] for b in bundles if "phase" in b}) < len(bundles))
    check("axis_values names the phases ADR 0003 declares but no bundle uses",
          ax["phase_declared_but_unused"] == ["define", "measure"], ax["phase_declared_but_unused"])
    check("an empty result is teachable: it carries the real axis values",
          "axis_values" in D(srv.search_templates("zzzz-no-such-thing")).get("nothing_matched", {}))

    # ---------------------------------------------------------------- refusals and errors
    print(DIM + "\n  Errors teach rather than merely fail" + OFF)
    r = E(srv.get_template("no-such-bundle"))
    check("an unknown bundle returns did_you_mean", "did_you_mean" in r, r)
    check("the refusal carries the closed error code", r["code"] == srv.ERR_NO_SUCH_BUNDLE, r["code"])
    r = E(srv.get_template("product-roadmap", fmt="go", size="lean"))
    check("a format/size pair that ships no file is refused, not invented",
          r["code"] == srv.ERR_NO_SUCH_VARIANT and "available" in r, r)
    check("the refusal lists the pairs that DO exist",
          {"format": "go", "size": "full"} in r.get("available", []), r.get("available"))
    r = E(srv.get_template("prd", parts=["template", "nonsense"]))
    check("an unknown part is refused with the list of real ones",
          r["code"] == srv.ERR_UNKNOWN_PART and "available_parts" in r, r)

    biggest = max(bundles, key=lambda b: max(b["approx_tokens"].values()))
    r = D(srv.get_template(biggest["id"], parts=["template", "guide", "companion", "example"]))
    if r.get("approx_tokens_total", 0) > srv.OUT_CAP_TOKENS:
        check("the 8k out cap fires on all four parts (%s, %d tokens) and withholds content"
              % (biggest["id"], r["approx_tokens_total"]),
              "refused" in r and all("content" not in p for p in r["parts"].values()))
    else:
        skip("the 8k out cap fires", "no bundle's four parts exceed it; the cap never fires here")

    # ---------------------------------------------------------------- grading pack
    print(DIM + "\n  The grading pack reports what it could not find" + OFF)
    no_rubric, no_anti = [], []
    for b in bundles:
        g = D(srv.get_grading_pack(b["id"]))
        if "rubric" in g.get("missing", []):
            no_rubric.append(b["id"])
        if "anti_patterns" in g.get("missing", []):
            no_anti.append(b["id"])
    check("all 27 guides yield a rubric section", not no_rubric, no_rubric)
    check("the 4 guides with no anti-patterns section are REPORTED, not silently short",
          sorted(no_anti) == ["okrs", "product-roadmap", "product-strategy", "product-vision"], no_anti)
    g = D(srv.get_grading_pack("prd"))
    check("the pack prices itself and the whole guide, so the caller can choose",
          g["approx_tokens_total"] > 0 and g["whole_guide_approx_tokens"] >= g["approx_tokens_total"])
    check("an unknown bundle's grading pack is an error",
          E(srv.get_grading_pack("nope"))["code"] == srv.ERR_NO_SUCH_BUNDLE)

    # ---------------------------------------------------------------- AC 5, parity
    print(DIM + "\n  AC5: the wrappers agree exactly with the tools they wrap" + OFF)
    d, p = tmpdoc(build_filled(stamped=True))
    try:
        want_ok, want_findings = val.validate(p)
        got = D(srv.validate_fill(p))
        check("validate_fill agrees with validate-fill.py on a GOOD document",
              got["valid"] == want_ok is True, (got["valid"], want_ok))
        check("validate_fill returns the identical finding list",
              [(f["level"], f["message"]) for f in got["findings"]] == want_findings)
    finally:
        shutil.rmtree(d, ignore_errors=True)

    # Break it by DROPPING a declared section, not by adding an extra heading. An extra heading at an
    # UNDECLARED level is legitimately ignored, so the first version of this fixture was not broken at
    # all: both tools correctly passed it, and the assertion proved they agreed about nothing.
    declared = val.find_variant(val.load_schema(), "prd", None, "lean")[0]
    drop = declared[-1]
    broken = build_filled(stamped=True).replace(
        "\n" + "#" * drop["level"] + " " + drop["title"] + "\n\nSomething.\n", "\n")
    d, p = tmpdoc(broken)
    try:
        want_ok, want_findings = val.validate(p)
        got = D(srv.validate_fill(p))
        check("validate_fill agrees on a BROKEN document, and both say it FAILS",
              got["valid"] == want_ok and want_ok is False, (got["valid"], want_ok))
        check("a document that FAILS validation is still a successful CALL (ADR 0054)",
              srv.validate_fill(p)["ok"] is True)
    finally:
        shutil.rmtree(d, ignore_errors=True)

    d, p = tmpdoc(build_filled())
    try:
        got = D(srv.stamp_and_strip(p, filled_by="agent:test", fill_method="batch"))
        out = os.path.join(d, "doc.filled.md") if not os.path.isfile(p) else None
        written = [f for f in os.listdir(d) if f != "doc.md"]
        check("stamp_and_strip succeeds on a fully filled document and writes a file",
              got["exit_code"] == 0 and written, (got["exit_code"], written))
        if written:
            text = open(os.path.join(d, written[0]), encoding="utf-8").read()
            check("the written file carries all three provenance keys",
                  all(k in text for k in ("filled_by:", "fill_method:", "fill_date:")))
    finally:
        shutil.rmtree(d, ignore_errors=True)

    with_placeholder = build_filled().replace("Something.", "{{still_unfilled}}", 1)
    d, p = tmpdoc(with_placeholder)
    try:
        got = D(srv.stamp_and_strip(p, filled_by="agent:test"))
        cli_code = strip.main([p, "--filled-by", "agent:test"])
        check("stamp_and_strip REFUSES a document with a placeholder, exactly as the CLI does",
              got["exit_code"] == cli_code == 2, (got["exit_code"], cli_code))
        check("the refusal is surfaced as `refused`, not swallowed into a success",
              got["refused"] is True and "ok" not in got, got)
        check("a strip REFUSAL is an outcome, not a transport error (ADR 0054)",
              srv.stamp_and_strip(p, filled_by="agent:test")["ok"] is True)
        check("a refusal writes nothing", os.listdir(d) == ["doc.md"], os.listdir(d))
    finally:
        shutil.rmtree(d, ignore_errors=True)

    check("a path that does not exist is an error, not a crash",
          E(srv.validate_fill(os.path.join(ROOT, "no-such.md")))["code"] == srv.ERR_NO_SUCH_FILE)

    # ---------------------------------------------------------------- AC 6, end to end
    print(DIM + "\n  AC6: intent to selection to fetch to fill to validation, nothing guessed" + OFF)
    # A named document type resolves to itself. This is the FLOW assertion, so the query is one with an
    # unambiguous answer.
    found = D(srv.search_templates("acceptance criteria for a user story"))
    picked = found["candidates"][0]["id"]
    check("a named intent resolves to its own bundle", picked == "acceptance-criteria", picked)

    # An open-ended sentence is checked against a SET, never one id. Asserting a single winner would
    # make this suite score ranking quality, which its own summary says it does not do. The first
    # version of this assertion did exactly that: it demanded `acceptance-criteria` for "what done
    # means", and the ranking answered `definition-of-done`, which is the better answer to that
    # sentence. The test was wrong, not the server.
    loose = [c["id"] for c in D(srv.search_templates(
        "I need to write down what done means for a story", max_results=3))["candidates"]]
    check("an open-ended sentence returns plausible candidates, ranking not asserted",
          len(loose) == 3 and set(loose) <= {"definition-of-done", "acceptance-criteria",
                                             "user-stories", "test-case", "incident-postmortem"},
          loose)
    fetched = D(srv.get_template(picked))
    check("the price was known BEFORE the fetch, from the search response",
          found["candidates"][0]["approx_tokens"][fetched["size"]]
          == fetched["parts"]["template"]["approx_tokens"])
    d, p = tmpdoc(build_filled("acceptance-criteria"))
    try:
        stamped = D(srv.stamp_and_strip(p, filled_by="agent:test", fill_method="batch"))
        written = [f for f in os.listdir(d) if f != "doc.md"]
        final = D(srv.validate_fill(os.path.join(d, written[0]))) if written else {"valid": False}
        check("the stripped, stamped document then passes validate_fill",
              stamped["exit_code"] == 0 and final["valid"],
              (stamped["exit_code"], final.get("findings")))
    finally:
        shutil.rmtree(d, ignore_errors=True)

    # ---------------------------------------------------------------- the SDK surface
    print(DIM + "\n  The MCP surface itself" + OFF)
    try:
        server = srv.build_server()
        names = {t.name for t in
                 __import__("asyncio").run(server.list_tools())}
        check("the server registers exactly the five specced tools",
              names == {"search_templates", "get_template", "get_grading_pack",
                        "validate_fill", "stamp_and_strip"}, sorted(names))
    except ImportError as e:
        label = "the server registers exactly the five specced tools"
        why = "the MCP SDK is not importable: " + str(e)[:120]
        if REQUIRE_SDK:
            check(label, False, why + "  [--require-sdk: a skip here is a failure. If this is an "
                                      "SDK 2.x rename, either pin `mcp<2` or port build_server() "
                                      "to `MCPServer`.]")
        else:
            skip(label, why)

    # ------------------------------------------------- structuredContent, over a REAL client (ADR 0054)
    #
    # THIS SECTION EXISTS BECAUSE THE SPIKE THAT DESIGNED THE ENVELOPE WAS NOT ENOUGH.
    #
    # The 2026-09-20 spike drove FastMCP IN PROCESS, saw `structuredContent` populated on both
    # branches, and concluded the shape worked. It did not. A real client ALSO validates the tool's
    # output against its declared `outputSchema`, and the first implementation failed every single
    # call with `Output validation error: None is not of type 'object'` - because the SDK serialises
    # the absent branch as an explicit null that the schema did not admit. In-process calls skip that
    # validation entirely, so the spike could not have seen it.
    #
    # So this asserts over a real stdio session, which is the only path that exercises what a caller
    # actually gets. Proving the mechanism works is not proving the path works (DF-7, again).
    label = "every tool returns populated structuredContent on BOTH the success and refusal path"
    try:
        import asyncio as _asyncio

        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client

        async def _probe():
            params = StdioServerParameters(
                command=sys.executable,
                args=[os.path.join(SCRIPT_DIR, "mcp_server.py")],
                cwd=ROOT,
            )
            cases = [
                ("search_templates", {"query": "acceptance criteria for a story"}, True),
                ("get_template", {"bundle_id": "prd"}, True),
                ("get_template", {"bundle_id": "no-such-bundle"}, False),
                ("get_template", {"bundle_id": "prd", "parts": ["nonsense"]}, False),
                ("get_grading_pack", {"bundle_id": "prd"}, True),
                ("get_grading_pack", {"bundle_id": "no-such-bundle"}, False),
                ("validate_fill", {"path": "no-such.md"}, False),
                ("stamp_and_strip", {"path": "no-such.md", "filled_by": "t"}, False),
            ]
            bad = []
            async with stdio_client(params) as (r, w):
                async with ClientSession(r, w) as sess:
                    await sess.initialize()
                    tools = {t.name: t for t in (await sess.list_tools()).tools}
                    for name, t in tools.items():
                        if not t.outputSchema:
                            bad.append("%s declares no outputSchema" % name)
                    for name, args, want_ok in cases:
                        res = await sess.call_tool(name, args)
                        sc = res.structuredContent
                        if not sc:
                            bad.append("%s(%s) returned no structuredContent: %s"
                                       % (name, args, getattr(res.content[0], "text", "")[:120]))
                        elif res.isError:
                            bad.append("%s(%s) came back as isError" % (name, args))
                        elif sc.get("ok") is not want_ok:
                            bad.append("%s(%s) ok=%r, wanted %r" % (name, args, sc.get("ok"), want_ok))
                        elif want_ok and sc.get("data") is None:
                            bad.append("%s(%s) ok:True with no data" % (name, args))
                        elif not want_ok and not (sc.get("error") or {}).get("code"):
                            bad.append("%s(%s) ok:False with no error.code" % (name, args))
            return bad, len(cases)

        problems, n = _asyncio.run(_probe())
        check("%s (%d calls)" % (label, n), not problems, problems[:4])
    except ImportError as e:
        why = "the MCP SDK is not importable: " + str(e)[:120]
        if REQUIRE_SDK:
            check(label, False, why + "  [--require-sdk: a skip here is a failure. This is the only "
                                      "assertion that exercises what a real caller receives.]")
        else:
            skip(label, why)

    # ---------------------------------------------------------------- summary
    print()
    passed = sum(1 for r in results if r)
    if skipped:
        print(YELLOW + "SKIPPED" + OFF + "  %d assertion(s), named so this is not read as a full run:"
              % len(skipped))
        for label, why in skipped:
            print(DIM + "        - " + label + ": " + why + OFF)
    if passed == len(results):
        print(GREEN + "OK" + OFF + "  %d assertion(s) passed." % passed)
        print(DIM + "      not verified: that a search RANKS well. These assert the contracts - field"
              "\n      names, addressability, parity, refusals - never that the top candidate is the"
              "\n      one a person would have picked. No check in this repository measures that."
              + OFF)
        return 0
    print(RED + "FAILED" + OFF + "  %d of %d assertion(s) failed." % (len(results) - passed,
                                                                     len(results)))
    return 1


if __name__ == "__main__":
    sys.exit(main())
