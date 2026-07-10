# Canon over our public samples

**Canon** is the open (Apache-2.0) core of the CodeRoast log engine — the
tokenizer, the stateless masker, the failure/warning lexicon, and the integer-domain
`det_math`. This page is that exact core run over the **public sample logs** we ship
in [coderoast-hub](https://github.com/CodeRoasted/coderoast-hub) under `samples/`.

It is a **transparency showcase, not a test result**: nothing here passes or fails.
It lets you read, line by line, what Canon does to a log before any of our proprietary
analysis runs. The end-to-end detection is exercised elsewhere (Eidos + Sift).

- `semantic_identity 990e17d758a2eec145f951b6ceae48f5`
- `packages: github@1.1.0 test_frameworks@1.0.0`

## What each `*.canon.txt` shows

Per source log, Canon emits three sections:

- **templates** — the distinct line shapes Canon collapsed the log into (variable
  parts masked to `<*>`), with how many lines matched each.
- **events** — one row per line: its severity level, a two-char `failure/warning`
  lexicon flag (`F`/`W`, `-` when absent), its structural role, and the template.
- **det_math** — the deterministic entropy term over the template distribution
  (integer domain; identical on every compiler / OS / CPU — that is the whole point).

## Corpora in this showcase

| corpus | source logs | canon output |
| --- | --- | --- |
| `loghub` | 16 | [`loghub.canon.txt`](loghub.canon.txt) |
| `marker_corpus` | 5 | [`marker_corpus.canon.txt`](marker_corpus.canon.txt) |
| `revert_corpus` | 10 | [`revert_corpus.canon.txt`](revert_corpus.canon.txt) |

> The sample logs are public-safe by construction — fully synthetic fixtures or
> CC-BY-licensed corpora. Our real third-party crawl corpora stay private.
