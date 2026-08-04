# Review standards: the brief a review lens reads

**Audience: a review agent in pipeline phase 4.** This is the single file you read before reviewing a
bundle. It states what the machine has already proved, what no machine can prove, and which of the second
list is yours. Read your family's contract too. Read nothing else unless this file sends you there.

**Why this file exists.** The standards a lens needs were spread across six documents totalling roughly a
thousand lines, and one of them, [`design-spec.md`](design-spec.md), is explicitly superseded in part: its
Definition of Done names CI scripts (`validate-template-family.sh`, `lint-template-frontmatter`) and a
contract path (`_families/<family>.contract.md`) that the build never adopted. A lens reading it for the DoD
gets an architecture that does not exist. Every standard below is stated from the tree as it is.

---

## 1. Already proved by machine. Do not re-check any of this.

Re-verifying these is the single largest waste in a review pass. If one were broken, the branch would be red
and there would be nothing to review.

**The bundle gate, `tools/check-bundles.py`, eleven checks per bundle:**

| | Check | Guarantees |
|---|---|---|
| A | files | All eight files present; declared variants exist |
| B | dashes | No em-dash or en-dash anywhere in the bundle |
| C | nesting | Section IDs nest strictly: lean is a subset of full |
| D | example | No unfilled `{{placeholder}}` survives in the worked example |
| E | citations | Every reference anchor is cited in the body, and none is padded |
| F | meta | Variant vocabulary, declared set and default all agree |
| G | yaml | Every YAML frontmatter block parses |
| H | history | A history entry exists for the current `template_version` |
| I | refs | `pairs_with` and `related_templates` resolve to real targets |
| J | schema | The meta validates against `meta.schema.json` |
| K | family | Phase, status and sizes conform to the family contract |

**Further CI steps, each proving something the gate cannot see:** the check-K, format-axis and research-log
self-tests (fixture-driven, because those branches have no live subject once the tree is clean); the link
gate (every relative link resolves, and no tracked file links into untracked `_local/`); manifest, atlas and
changelog freshness; the ADR index (no decision record without an index row, and no row without a file);
the research-log contract; self-reported counts; example independence; example chronology; rubric scope;
and a repo-wide dash sweep over every tracked file.

So: **do not** count files, hunt placeholders, check nesting, follow links, tally references, validate YAML,
compare the manifest, or look for em-dashes. All of it is settled before you start.

---

## 2. What no machine checks. This is the review surface.

Every one of these has shipped past a green gate at least once.

1. **A claim no logged source supports.** The dominant defect class. Plausible, specific, in the authorial
   voice, and supported by nothing. See section 5.
2. **A quotation that exists in no source.** Two shipped in one bundle's research log and survived a
   verification pass over its source entries, because they sat in the log's *narrative*, not its entries.
   **A verification pass over source entries does not verify the prose that cites them.**
3. **A frequency or superlative claim nothing measured.** "The most common failure", "universally
   acknowledged". `tools/lint-unsourced-confidence.py` enumerates candidates; only a reader can judge them.
4. **A teaching point that contradicts a sibling file.** The companion, guide and example must agree.
5. **An example that is the template's own guidance text reworded.** The check catches copied *passages*;
   it cannot catch a copied *argument*.
6. **A rubric row that grades a section the variant does not ship.** The check enforces the arithmetic and
   demands a scope table; whether the table is *right* is yours.
7. **Prose that disagrees with a count marker beside it.** `check-counts.py` says outright that it compares
   markers and cannot read the sentences around them.

---

## 3. The standards themselves

### Honest retrieval

The library's central quality claim. Every source in a research log carries one of exactly three tokens:

| Token | Meaning | May be quoted? |
|---|---|---|
| `fetched-and-verified` | The page body was actually read | **Yes, and only these** |
| `url-confirmed-not-read` | The URL resolves; the body was not read | No |
| `not-retrieved` | Neither | No |

A phrase enters `quotable` **only if it was read verbatim**. Never fabricate a quote. A near-miss token
(`not-retrieved-ish`) is a failure, not a pass; the contract check exists because an earlier version asked
only whether the token appeared *anywhere* in the log and a source in the wrong column slipped through.

A source that was not fetched may support the *existence* of a topic. It may not support a specific claim
about that topic, and it may never be quoted.

### The guide's rubric

- A numbered table scored **0 / 1 / 2**. Not Strong/Adequate/Weak, not pass/fail.
- **An explicit threshold in the sentence above the table**, stated as a *consequence*: what happens to the
  reader or the work below the line, not a grade.
- **6 to 12 rows.** Fewer is a checklist; more and nobody finishes.
- Row titles are **properties of the document**, bolded, two to four words.
- **Cells describe evidence, not counts.** The test: *could someone satisfy this cell without improving the
  document?* If yes, it is written wrong. "Names at least two exclusions" is gameable; "you can point at the
  sentence, and name the request it refused and who asked" is not. This library's own `bug-report` research
  documents defect counts being gamed the moment they become targets, and a rubric cell is a target.
- If rows are variant-scoped, a **scope table** governs, naming for each variant which rows apply, the
  maximum, and the threshold. Row markers are ambiguous (a comma reads as both AND and OR); the table wins.

A checklist and a scored rubric do different jobs, and for a short artifact a checklist may be right. **Do
not convert one mechanically.**

### The worked example

- A genuine worked artifact, never placeholder filler.
- **A different scenario from the template's guidance comments.** Not a reworded one: the reuse survives
  swapping every noun, which is why the convention failed three times and a string check now enforces it.
- Chronologically possible. It may only cite documents that existed when it is dated. An opening
  `> **Worked example.**` blockquote addresses the library's reader rather than the fictional author, so it
  may mention later documents; body prose may not.
- Consistent with its sibling examples, which form one continuous thread from vision to bug report.

### House rules

- **No em-dash or en-dash, anywhere.** Use ` - `, or restructure. Ranges use plain hyphens.
- Placeholders are `{{snake_case}}` and consistent across variants.
- Guidance lives in HTML comments and strips cleanly on render.
- A reference ID never appears bare: pair it with a short handle on first use.

---

## 4. The four lenses, and what each reads

Reading the whole bundle four times is the second largest waste in a pass. Read your own files.

| Lens | Reads | Owns |
|---|---|---|
| **citation-support** | research log, companion | Every companion claim against the log's `Supports:` clause. Every quote against `quotable`. Unread sources carry no claim. Contested claims flagged as contested. |
| **dod-family-conformance** | templates, guide, family contract | The DoD items the gate cannot see: guidance-comment grammar, section skeleton, guide shape (section 3 above), and the family's own obligation. |
| **accuracy-teaching-point** | companion, guide, example | Historical and conceptual claims against the log. Teaching points consistent across all three files. |
| **chaining-consistency** | example, sibling examples, templates | The example internally sound, instantiating every template section, no placeholders, consistent with the thread. |

Return structured findings: `{severity, file, location, issue, fix}`. Cite the log line or file line that
grounds each. A finding without a location is not actionable.

**Run the two report-only lints first** (pipeline phase 3.5). They enumerate candidates mechanically so you
spend your attention judging rather than hunting:

```
python tools/lint-number-provenance.py <type>
python tools/lint-unsourced-confidence.py <type> --uncited
```

Neither output is a defect list. A flagged line is a candidate, and both tools print what they cannot see.

---

## 5. The dominant defect class, and how to fix it

**A plausible specific claim that no logged source supports.** Not a misreading and not a stale fact: a
number, a year, a named person or a frequency that reads entirely credible and that nothing in the log
carries. Recorded examples, all of which passed a green gate:

- *"Robert Galvin supplied the definition everyone quotes, EIRMA formalised a generic method in 1997."*
  Galvin, 1997 and "late 1990s" each return zero matches in that bundle's log.
- *"The single most common substantive failure."* `most common` returns zero matches in that bundle's log.
- *"The phenomenon is universally acknowledged"*, where the same log records both relevant sources as
  unretrieved and says the retrieval "was too weak to put words in anyone's mouth."

**The fix rule, and it is not optional: delete the claim, or label it honestly. Never hunt for a citation
that would justify it.** Searching for a source that supports a sentence you have already written is how a
fabrication acquires a footnote. If a source genuinely supports it, the log would already say so.

Honest labelling is a first-class outcome, not a retreat. The library's own best phrasings are of this kind:
*"widely asserted and thinly evidenced"*, *"as far as this research found, never measured"*, *"the research
could not retrieve the piece most often cited for it, so treat the claim as a framing."*

---

## 6. Where to go deeper

Only when this file does not settle a question.

| For | Read |
|---|---|
| The per-bundle runbook and its gotchas | [`bundle-pipeline.md`](bundle-pipeline.md) |
| A recurring judgment call, and what always stops for the maintainer | [`decision-procedures.md`](decision-procedures.md) |
| The full rubric spec and its provenance | [`guide-rubric-spec.md`](guide-rubric-spec.md) |
| A family's own obligation | `contracts/<family>.md` |
| Why a rule is the way it is | [`decisions/`](decisions) - the decision records win over any prose |
| What is true of the tree right now | [`STATE.md`](../../STATE.md) - it wins over any document |
