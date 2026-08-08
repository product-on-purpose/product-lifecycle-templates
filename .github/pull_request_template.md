<!-- Delete any section that does not apply. Do not delete Verification. -->

## What this changes

## Why

<!-- If this corrects a claim, say what the evidence is. If a research log does not support something, that
     is the strongest possible reason and should be stated as such. -->

## Verification

<!-- Paste real output. "Checks pass" is not verification; the output is. -->

```
python tools/check-bundles.py
python tools/check-links.py
python tools/check-counts.py
```

## Checklist

- [ ] Every claim I added has a home in a research log's `Supports:` or `Quotable:` clause
- [ ] Every number I stated is pinned by a `<!-- counts: ... -->` marker, or is not stated
- [ ] No em-dash or en-dash anywhere (CI sweeps repo-wide)
- [ ] Any claim about the world carries a source, or is written as this library's own position
