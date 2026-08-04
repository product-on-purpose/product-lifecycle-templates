#!/usr/bin/env python3
"""Fail when a guide's quality rubric grades a variant on a section that variant does not ship.

WHY THIS EXISTS
---------------
Every guide carries a self-gradable rubric: numbered rows scored 0/1/2 with a stated pass threshold
(`docs/internal/guide-rubric-spec.md`). When a bundle ships more than one variant or format, some rows apply
to some variants and not others, and getting that scoping wrong penalises the CHOICE OF VARIANT rather than
the quality of the document.

Three occurrences, all in shipped bundles, all found by human review:

  product-strategy   rows graded sections its one-pager format does not have
  product-roadmap    rows 7 and 8 (Dependencies, Review Trigger) scored against `go` and `themes`, which
                     ship neither section. Choosing a non-default format cost four points for absent content
  product-vision     rows 9 and 10 marked "(not lean canvas)", so they score against `prfaq-full`, which has
                     no horizon section and no assumptions section. There is no scope table at all, and the
                     stated threshold implies all twelve rows always apply

WHAT IT ENFORCES, AND WHAT IT REFUSES TO
----------------------------------------
Calibrated against all nineteen guides on 2026-08-03 rather than assumed:

  ENFORCED  max == 2 x rows scored. Held for every guide with a rubric (4 of 4 checked).
  ENFORCED  a threshold strictly between half and all of the available points.
  ENFORCED  a scope table when rows carry scope markers and the bundle ships more than one variant.
            Without one, nothing states which variants a marked row applies to.
  ENFORCED  every shipped variant appears in the scope table where one exists.

  REFUSED   a threshold FORMULA. Two thirds rounded down holds for `bug-report` and `test-plan` and does NOT
            hold for `test-case` (11/16) or `product-vision` (17/24), both near 71 percent. The spec requires
            an explicit threshold, not an arithmetic one, so enforcing a formula would invent a house rule
            the house does not follow.

  REFUSED   anything about guides with no numbered rubric. Eleven of nineteen use checklist form, which
            `guide-rubric-spec.md` section 1 documents and section 4 explicitly declines to convert
            mechanically. They are skipped, and the count is printed so the skip is visible.

THE SECTION MATCH IS A HEURISTIC AND IS REPORTED AS A WARNING
-------------------------------------------------------------
To know that a row grades an absent section, the check matches distinctive words in the row title against the
H2 headings of each variant. It only fires when the word matches a heading in AT LEAST ONE variant, which is
what establishes that the row is section-shaped at all, and is missing from a variant the row is scored
against. A row like "Not a Gantt chart" grades a property rather than a section and never fires.

That is a real heuristic with a real false-negative rate: a row whose title shares no vocabulary with its
section is invisible here. It warns rather than fails for that reason.
"""
import math
import re
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / "templates"

ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|\s*\*\*(.+?)\*\*\s*(\*\(([^)]*)\)\*)?\s*\|", re.M)
THRESH_RE = re.compile(r"\b(\d+)\s+out of\s+(\d+)\b")
SCOPE_HDR_RE = re.compile(r"^\|\s*(Document|Variant)\s*\|", re.M)
SCOPE_ROW_RE = re.compile(r"^\|\s*([a-z][a-z0-9 ,\-]*?)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*\**(\d+)\**\s*\|", re.M)

STOP = {
    "it", "its", "is", "are", "has", "have", "and", "or", "a", "an", "the", "not", "with", "for", "to", "of",
    "in", "on", "by", "no", "each", "every", "that", "this", "one", "be", "been", "you", "your", "can",
    "does", "do", "who", "what", "when", "where", "which", "there", "here", "from", "at", "as", "into",
}


def h2s(path: Path) -> list[str]:
    return [l.strip()[3:].strip() for l in path.read_text(encoding="utf-8").splitlines()
            if l.startswith("## ")]


def tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]{4,}", text.lower()) if w not in STOP}


def rows_expr_count(expr: str, total: int) -> int | None:
    """How many rows an expression like 'all 9', '1-6', '1-6 and 9' selects.

    Parentheticals are stripped FIRST, and that is not cosmetic. Scope cells carry their reasoning inline:

        | one-pager | 3-8 (it starts from the choice, so rows 1-2 have no diagnosis to grade) | 12 |

    Counting the numbers inside that explanation yielded 8 rows against a correct maximum of 12, and the
    check reported a defect in a guide that was right. The row selection is what precedes the reasoning.
    """
    e = re.sub(r"\([^)]*\)", " ", expr).lower()
    if "all" in e:
        m = re.search(r"all\s+(\d+)", e)
        return int(m.group(1)) if m else total
    picked: set[int] = set()
    for a, b in re.findall(r"(\d+)\s*-\s*(\d+)", e):
        picked.update(range(int(a), int(b) + 1))
    e_wo = re.sub(r"\d+\s*-\s*\d+", " ", e)
    picked.update(int(n) for n in re.findall(r"\b(\d+)\b", e_wo))
    return len(picked) or None


def rows_selected(expr: str, total: int) -> set[int]:
    """Which row numbers an expression selects, as a set."""
    e = re.sub(r"\([^)]*\)", " ", expr).lower()
    if "all" in e:
        m = re.search(r"all\s+(\d+)", e)
        return set(range(1, (int(m.group(1)) if m else total) + 1))
    picked: set[int] = set()
    for a, b in re.findall(r"(\d+)\s*-\s*(\d+)", e):
        picked.update(range(int(a), int(b) + 1))
    picked.update(int(n) for n in re.findall(r"\b(\d+)\b", re.sub(r"\d+\s*-\s*\d+", " ", e)))
    return picked


def variant_matches_label(variant: str, label: str, default_fmt: str) -> bool:
    """Does a scope-table label like 'kernel, lean' or 'now-next-later, full' name this variant file?"""
    toks = [t for t in re.split(r"[,\s]+", label.lower()) if t]
    terms = variant_terms(variant, default_fmt)
    return bool(toks) and all(t in terms for t in toks)


def default_format(bundle: Path) -> str:
    meta = bundle / f"{bundle.name}_meta.yaml"
    if meta.exists():
        m = re.search(r"^default_format:\s*(\S+)", meta.read_text(encoding="utf-8"), re.M)
        if m:
            return m.group(1).strip().strip("\"'")
    return ""


def variant_terms(variant: str, default_fmt: str) -> set[str]:
    """The words that legitimately name a variant, so a scope marker can be matched against it.

    Per ADR 0028 the DEFAULT format keeps the plain filenames, so `full` is not merely "the full size", it
    is also "kernel, full" or "now-next-later, full" depending on the bundle. Without resolving that, a
    marker reading "(full, now-next-later only)" matches no variant at all and every check silently passes.
    """
    parts = variant.split("-")
    size = parts[-1]
    fmt = "-".join(parts[:-1]) or default_fmt
    terms = {variant, size}
    if fmt:
        terms.add(fmt)
        terms.update(fmt.split("-"))
    return {t for t in terms if t}


def marker_applies(marker: str, variant: str, default_fmt: str) -> bool:
    """Does a rubric row marked `*(...)*` apply to this variant?

    Two shapes appear in the tree, and both must be read correctly or the section heuristic fires on rows
    that were correctly scoped in the first place:

        *(full)*                        positive: applies where every token matches the variant
        *(full, now-next-later only)*   positive, multi-token
        *(not lean canvas)*             negated: applies everywhere EXCEPT the matching variant
    """
    m = marker.lower().replace("*", "").strip()
    negated = m.startswith("not ")
    if negated:
        m = m[4:]
    toks = [t for t in re.split(r"[,\s]+", m) if t and t not in {"only", "and", "the"}]
    if not toks:
        return True
    terms = variant_terms(variant, default_fmt)
    matches = all(t in terms for t in toks)
    return not matches if negated else matches


def check(bundle: Path) -> tuple[list[str], list[str], bool]:
    name = bundle.name
    guide = bundle / f"{name}_guide.md"
    if not guide.exists():
        return [], [], False
    text = guide.read_text(encoding="utf-8")
    rows = ROW_RE.findall(text)
    if not rows:
        return [], [], False   # checklist-style guide; out of scope, counted as skipped

    variants = {p.name.split("_template-")[1][:-3]: p for p in sorted(bundle.glob(f"{name}_template-*.md"))}
    fails, warns = [], []
    total = len(rows)
    marked = [(int(n), t, m) for n, t, _, m in rows if m]

    # --- max == 2 x rows, and a sane threshold -------------------------------------------------
    th = THRESH_RE.search(text)
    if th:
        thresh, mx = int(th.group(1)), int(th.group(2))
        if mx != total * 2:
            fails.append(f"    stated maximum {mx} but the rubric has {total} rows, which is {total * 2} points")
        if not (mx / 2 < thresh < mx):
            fails.append(f"    threshold {thresh} of {mx} is outside the sane band (more than half, less than all)")
    else:
        fails.append("    no 'N out of M' threshold found above the rubric (guide-rubric-spec section 2 rule 2)")

    # --- a scope table is required once rows are variant-scoped --------------------------------
    has_scope = bool(SCOPE_HDR_RE.search(text))
    if marked and len(variants) > 1 and not has_scope:
        names = ", ".join(f"row {n} *({m})*" for n, _, m in marked)
        fails.append(
            f"    {len(marked)} row(s) carry a scope marker and the bundle ships {len(variants)} variants, "
            f"but there is no scope table.\n"
            f"      {names}\n"
            f"      Nothing states which variants those rows apply to, or what each variant scores against."
        )

    # --- where a scope table exists, it must cover every shipped variant and add up -------------
    dfmt = default_format(bundle)
    scoped_rows: dict[str, set[int]] = {}
    if has_scope:
        for label, expr, mx_s, _thr_s in SCOPE_ROW_RE.findall(text):
            n = rows_expr_count(expr, total)
            if n is not None and int(mx_s) != n * 2:
                fails.append(f"    scope row '{label}' selects {n} rubric row(s) but states a maximum of {mx_s}")
            picked = rows_selected(expr, total)
            for v in variants:
                if variant_matches_label(v, label, dfmt):
                    scoped_rows.setdefault(v, set()).update(picked)
        for v in variants:
            if v not in scoped_rows:
                fails.append(f"    variant '{v}' ships but appears in no scope-table row")

    # --- heuristic: a scored variant lacking the section a row grades ---------------------------
    # THE SCOPE TABLE GOVERNS WHERE ONE EXISTS. Row markers are a reader's hint and use commas
    # inconsistently across the tree: "(full, now-next-later only)" means AND, while a marker naming two
    # formats would mean OR. The scope table states outright which rows each variant scores, so it is the
    # authority, and markers are only consulted when no table exists.
    all_heads = {v: tokens(" ".join(h2s(p))) for v, p in variants.items()}
    union = set().union(*all_heads.values()) if all_heads else set()
    for num, title, marker in marked:
        t = tokens(title) & union            # only rows whose title is section-shaped somewhere
        if not t:
            continue
        for v, heads in all_heads.items():
            applies = (num in scoped_rows[v]) if (has_scope and v in scoped_rows) \
                else marker_applies(marker, v, dfmt)
            if not applies:
                continue
            if not (t & heads):
                src = "the scope table" if has_scope else f"marker *({marker})*"
                warns.append(
                    f"    row {num} \"{title}\" is scored against variant '{v}' per {src}, which has no "
                    f"section matching {sorted(t)}")
    return fails, warns, True


def main() -> int:
    only = sys.argv[1] if len(sys.argv) > 1 else None
    bundles = sorted(d for d in TEMPLATES.iterdir()
                     if d.is_dir() and not d.name.startswith((".", "_")) and (only is None or d.name == only))

    checked = skipped = 0
    any_fail = False
    for b in bundles:
        fails, warns, had_rubric = check(b)
        if not had_rubric:
            if (b / f"{b.name}_guide.md").exists():
                skipped += 1
            continue
        checked += 1
        if fails or warns:
            print(f"  {'FAIL' if fails else 'warn'}  {b.name}")
            for f in fails:
                print(f)
            for w in warns:
                print(w)
        any_fail = any_fail or bool(fails)

    print()
    print(f"rubric scope: {checked} guide(s) with a numbered rubric checked, {skipped} checklist-style skipped")
    print("      Enforced: maximum equals twice the rows scored; a threshold between half and all; a scope")
    print("      table once rows are variant-scoped and more than one variant ships; every shipped variant")
    print("      listed in that table.")
    print("      NOT enforced: a threshold formula. Two thirds rounded down holds for bug-report and")
    print("      test-plan and does not hold for test-case (11/16) or product-vision (17/24). The spec asks")
    print("      for an explicit threshold, not an arithmetic one.")
    print("      NOT enforced: checklist-style guides. guide-rubric-spec section 4 declines to convert them")
    print("      mechanically, so they are skipped and counted rather than silently passed.")
    print("      The section match is a HEURISTIC and only warns: it fires when a row's wording matches a")
    print("      heading in some variant but not in one it is scored against, so a row whose title shares")
    print("      no vocabulary with its section is invisible here.")

    if any_fail:
        print()
        print("FAIL  a rubric grades a variant on a section it does not ship, or its arithmetic does not hold.")
        return 1
    print()
    print("OK  every numbered rubric scopes to what its variants actually contain.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
