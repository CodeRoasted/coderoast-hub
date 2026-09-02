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
| **regression** | [`logcraft__ci-build__green-a.log`](logs/logcraft__ci-build__green-a.log) → [`logcraft__ci-build__red.log`](logs/logcraft__ci-build__red.log) | **4,889** | **11** | [report](reports/regression.report.md) |

- **noise floor** — two runs that both **passed**. A plain text diff (timestamps already
  stripped) reports thousands of differing lines. Sift reports what is left after the churn is
  accounted for. This is the number that matters for a tool you leave switched on: what it
  costs you to read on a day when nothing broke.
- **regression** — the same passing run against the **failing** one. The report's top three are
  the failure and its cause: the step exited non-zero, then the error it raised. Ranks 1, 2
  and 3 of [the report](reports/regression.report.md) — open it and check.

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

- The same run verdicts and the same line totals.
- The same ranking curve for the significant changes, position by position, so nothing crosses a rank boundary unseen.
- The same findings, with the same evidence and the same line references.
- Template hashes that correspond one-to-one, so the redaction can neither merge two line shapes nor split one.
- The engine's raw per-step MetaLogDiff documents, held to the same rule: every count, frequency, divergence, verdict, n-gram and cube cell pinned; only the template hashes are free, and they must still correspond one-to-one.
- That the redaction changed NOTHING ABOUT WHAT WAS OBSERVED: per step, the number of line occurrences the engine attributed to templates is identical on both sides. Regrouping lines into different templates cannot move that number; inventing, dropping or rewording a line is the only thing that can.
- All of it at two significance floors, 0.05 and 0.0, so the raw tier is exercised twice over and the sub-significance tail is surfaced even when the published report is a single line. How many ranked rows each arm actually compared position by position is published per arm and reads: the noise-floor pair 1 of 1 at floor 0.05, 0 of 50 at floor 0; the regression pair 10 of 11 at floor 0.05, 10 of 50 at floor 0. Floor 0 compares FEWER of them, not more, and that is the point: at floor 0 the engine's ranked list is a fifty-row slice of a population of roughly a thousand, most of it below the shipped floor, and on the noise-floor pair it does not carry the single significant finding at all. Comparing an arbitrary slice row by row is not a claim; the raw tier below it is.
- WHAT IS COMPARED IS THE SIGNIFICANT SET, and the tail is declared instead. The changes at or above the shipped significance floor — the ones these reports headline — are held to every check above. Below that floor the redaction genuinely does move something, and pretending otherwise would be the dishonest choice: the runner path MUST be redacted, redacting it shortens the path by one segment, and the tokenizer then groups the lines carrying it into different templates. So the tail's grouping is not a claim this showcase makes. What holds it instead is the observation check above — regrouping cannot change how many lines were seen — plus a published count of exactly how many templates it reached: 50 and 55 for the noise-floor pair and 57 and 51 for the regression pair respectively, under `pairs[].declared.honesty_gate[].raw_tail_templates_repartitioned_by_the_redaction`. The population it moves is published on both sides too, as `detected_changes`: 936 against 941 for the noise-floor pair and 1072 against 1066 for the regression pair. And no template in the significant set may be one of them — if the redaction ever reached a change these reports publish, the build stops.
- One tolerance on which line was kept, declared rather than hidden: some findings surface because a BOUNDED store of high-salience lines happened to hold that line, and both such stores key on line content — so redacting the runner path can swap which of several equally-ranked lines was kept. Those findings must still match on shape, severity, score and step; only which line was sampled is free, and the count is published per pair. At the shipped floor it is 0 for the noise-floor pair and 0 for the regression pair; in the raw tier, where the same swap shows as a row whose template and count changed, it is 0 for the noise-floor pair and 0 for the regression pair.
- One tolerance on whether such a line is reported at all: the same stores are bounded, so changing a line's template can change its MEMBERSHIP and not merely its identity. A finding may therefore appear on one side and not the other — but only if it is a plain line appearing or disappearing, only if the store is why it surfaced, and only if it ranks strictly below every finding the failure lexicon or the statistics produced. The findings this showcase is about can never move that way. The count is published per pair: at the shipped floor it is 0 for the noise-floor pair and 1 for the regression pair.

This is not a formality: it rejected the first redaction map this showcase was built with, which would have published a report the real logs do not support.

---
*Published under CC-BY-4.0.*
