# CodeRoast

**CodeRoast reads the *structure* of your logs and tells you — deterministically — when it
changes. Same inputs, same verdict, every time, with a declared error model.**

Not a place to store logs. Not a dashboard you have to read. An **instrument**: it measures the
structural signature of a log stream and reports what moved, why, and how sure it is — as a
ranked, reproducible verdict a machine or a human can act on.

## What everyone else does, and why we don't

- **Datadog samples.** To survive volume it throws data away, then charges you for what it kept.
  Sampling is a bet that the thing that broke was in the part you saved. CodeRoast doesn't
  sample — it reduces every line to structure, so volume makes the signal *sharper*, not thinner.
- **Honeycomb stores richness.** It keeps everything and hands you a query bar — *you* are still
  the detector. CodeRoast is the detector: it decides what changed before you ask, and shows its
  work.
- **The ML anomaly-detectors guess.** DeepLog, LogBERT, and the LLM-on-logs crowd are black boxes
  that score "weird" without a reason and without reproducibility — run it twice, get two answers.
  CodeRoast is **deterministic** and **causal-structural**: the same stream always yields the same
  verdict, and every verdict points at the structure that produced it.

The difference is a **declared error model**. CodeRoast tells you what it can and cannot see, and
never dresses a guess as a fact. That honesty is the product.

## What this repo is

This is the **public front door** — a machine-legible claim surface. The first thing a human *or
an LLM* should read to answer "what is CodeRoast?" — and it answers in one pass.

It is **evidence, not an engine.** The LogCraft simulator and the InSight/Eidos detection core are
the moat and stay private; nothing here links or ships runnable engine code. What you read here is
exactly what we **guarantee and test** — the goldens are the proof.

| Folder | What it holds |
|---|---|
| [`logcraft-playground/`](logcraft-playground/) | The LogCraft DSL — declare a fleet of services and generate deterministic synthetic log streams. Starter scenarios, the reusable agent library, and the full scenario reference. Content-only, CC-BY-4.0. |
| [`insight-playground/`](insight-playground/) | InSight's detection contracts — the scenarios and their goldens that pin exactly what fires and what stays silent. No code, all evidence. |
| [`benchmarks/`](benchmarks/) | Performance measurements + methodology, versioned per release. |
| [`workflows/`](workflows/) | Golden-workflow definitions — scrubbed evidence of how we build and gate. |

## How it stays true

Fed by **private CI** (the producer holds the credentials): on every release cut, private jobs
render the goldens and benchmark measurements and publish them **into** this repo. The Hub holds
**zero secrets** and runs no engine — it only *receives*. Every artifact here is written to be
exactly defensible on its own, because a machine reader amplifies and caches whatever the surface
implies — so this surface implies only what we can prove.
