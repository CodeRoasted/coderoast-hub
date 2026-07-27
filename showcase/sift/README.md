# Sift over real CI logs

**3 real CI job logs and what Sift makes of them.** Not a toy fixture: 10,297
lines of one C++ project's actual build job — compiler output, CMake, package resolution, test
runs — verbatim from the runner. They are our own build logs; we run Sift on our own CI, so
this is the tool on the job it was built for.

Sift answers one question about two build logs: **what actually changed, and what is just
noise.** These samples are the evidence for both halves of that.

| pair | logs | lines a plain `diff` reports | changes Sift reports | |
| --- | --- | --- | --- | --- |
| **noise-floor** | [`logcraft__ci-build__green-a.log`](logs/logcraft__ci-build__green-a.log) → [`logcraft__ci-build__green-b.log`](logs/logcraft__ci-build__green-b.log) | **5,571** | **1** | [report](reports/noise-floor.report.md) |
| **regression** | [`logcraft__ci-build__green-a.log`](logs/logcraft__ci-build__green-a.log) → [`logcraft__ci-build__red.log`](logs/logcraft__ci-build__red.log) | **4,889** | **13** | [report](reports/regression.report.md) |

- **noise floor** — two runs that both **passed**. A plain text diff (timestamps already
  stripped) reports thousands of differing lines. Sift reports what is left after the churn is
  accounted for. This is the number that matters for a tool you leave switched on: it buries
  noise instead of missing signal.
- **regression** — the same passing run against the **failing** one. The report ranks the true
  cause at the top, above the collateral.

## What is here

- **`logs/`** — the three logs, exactly as published.
- **`reports/`** — Sift's report over each pair, as Markdown and as JSON.
- **`MANIFEST.json`** — provenance, every transformation applied per sample, and the digests
  that make both re-derivable.

## Provenance, plainly

These are real CI job logs — our own. Three runs of one C++ build job: an earlier passing run, a later passing run, and a failing run of the same job on the same project. Two transformations were applied to the raw bytes, both listed per sample in MANIFEST.json; each sample records the sha256 of the raw log and of the published one, so applying the listed transformations to the raw log yields exactly these bytes. Nothing else was touched. The build's own output — its compiler and CMake and package-manager chatter, its source file names, its test names, its timings, its errors — is the runner's verbatim bytes, down to the UTF-8 BOM and the ANSI colour escapes.

The two, in full:

1. **The Sift step was removed.** We run Sift in this very job, so the raw failing log contains
   Sift's own findings. A demo that diffs a log already containing the report is circular and
   inflates its own numbers, so the whole step is cut — and the count it was inflating is
   recorded in the manifest rather than quietly kept.
2. **Machine and filesystem identity were redacted.** The runner's host name and its private
   home-directory layout are mapped onto the standard hosted-runner shape, consistently across
   all three logs. Nothing else. The project, package, source-file and test names are the real
   ones — they are what makes these real build logs, and redacting them was measured to move
   the report, so redacting them would have meant publishing a claim these logs do not make.

### The scrub is not allowed to change the answer

Redacting identity could silently change the result: alter a template and the ranked report changes with it. So the build runs Sift twice — once on the logs before identity redaction, once on the published logs — and refuses to publish unless both reports carry the same claim.

- The same change counts and the same run verdicts.
- The same ranking curve, position by position, so nothing crosses a rank boundary unseen.
- The same findings, with the same evidence and the same line references.
- Template hashes that correspond one-to-one, so the redaction can neither merge two line shapes nor split one.
- All of it at two significance floors, including floor 0 — every change the engine detected, not only the significant ones.
- One tolerance, declared rather than hidden: some findings surface because a BOUNDED reservoir of high-salience lines happened to retain that line, and the reservoir keys on line content — so redacting the runner path, which is not optional, can swap which of several equally-ranked lines it kept. Those findings must still match on shape, severity, score and step; only which line was sampled is free, and the count is published per pair under `pairs[].declared.honesty_gate`. Here it is 0 for the noise-floor pair and 1 for the regression pair.

This is not a formality: it rejected the first redaction map this showcase was built with, which would have published a report the real logs do not support.

---
*Published under CC-BY-4.0.*
