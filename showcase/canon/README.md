# Canon over our public samples

**Canon** is the open (Apache-2.0) core of the CodeRoast log engine — the
tokenizer, the stateless masker, the failure/warning lexicon, and the integer-domain
`det_math`. This page is that exact core run over the **public sample logs** we ship
in [coderoast-hub](https://github.com/CodeRoasted/coderoast-hub) under `samples/`.

It is a **transparency showcase, not a test result**: nothing here passes or fails.
It lets you read, line by line, what Canon does to a log before any of our proprietary
analysis runs. The end-to-end detection is exercised elsewhere (Eidos + Sift).

- `semantic_identity 84df619d0946c1c7b470b5e6f71a825c`
- `packages: github@1.4.0 gitlab@1.0.0 jenkins@1.1.0 test_frameworks@1.0.0`

The two lines above are the canon vocabulary of **this run** — not a standing version claim.
This page is rendered on demand, not at every release cut, so read it as a snapshot of one
run. The release-stamped evidence lives beside it in [`determinism/`](../../determinism/),
which is regenerated at each cut and names the version it belongs to.

## What each `*.canon.txt` shows

Per source log, Canon emits three sections:

- **templates** — the distinct line shapes Canon collapsed the log into (variable
  parts masked to `<*>`), with how many lines matched each.
- **events** — one row per line: its severity level, a two-char `failure/warning`
  lexicon flag (`F`/`W`, `-` when absent), its structural role, and the template.
- **det_math** — the deterministic entropy term over the template distribution
  (integer domain; identical on every compiler / OS / CPU — that is the whole point).

## Corpora in this showcase

| corpus | source logs | right to redistribute | canon output |
| --- | --- | --- | --- |
| `loghub` | 16 | licensed — see [`ATTRIBUTION.md`](ATTRIBUTION.md) | [`loghub.canon.txt`](loghub.canon.txt) |
| `marker_corpus` | 5 | synthetic fixture (`SLICE.json`) | [`marker_corpus.canon.txt`](marker_corpus.canon.txt) |
| `revert_corpus` | 10 | synthetic fixture (`SLICE.json`) | [`revert_corpus.canon.txt`](revert_corpus.canon.txt) |

> **What this run checked, and what it did not.** The *right to redistribute* in the table
> above was read from each source corpus during this run — a `SLICE.json` declaring it
> fabricated, or an `ATTRIBUTION.md` naming a licence — and this page is not rendered at
> all when a corpus declares neither. **No identifying-content scan was computed for these
> rendered artifacts.** That scan is a separate axis, it runs outside this repository, and
> a redistribution licence says nothing about what is *in* the bytes. Read the table as a
> statement about our right to publish these renders, never as a statement about their
> contents. Our real third-party crawl corpora stay private.
