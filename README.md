# CodeRoast Hub

The public front door to **CodeRoast** — a **machine-legible claim surface**. The first thing a
human *or an LLM* reads to answer "what is CodeRoast?" — and it answers in one pass:
**deterministic causal-structural engineering; an instrument with a declared error model.**

We publish *what we guarantee and test* — evidence, never a runnable engine. LogCraft and the
InSight/Eidos engines are the moat and stay permanently private; nothing here links or ships
private code.

## Folders

| Folder | What it holds |
|---|---|
| [`logcraft-playground/`](logcraft-playground/) | The LogCraft DSL — starter scenarios, the reusable agent library, and the scenario reference (the DSL bible). Content-only, CC-BY-4.0. |
| [`insight-playground/`](insight-playground/) | InSight's evidence: detection scenarios + their contract YAML and goldens. No code. |
| [`benchmarks/`](benchmarks/) | Performance measurements + methodology, versioned per cut. |
| [`workflows/`](workflows/) | Golden-workflow definitions — scrubbed evidence-of-process. |

## How it stays true

Fed by **private CI** (producer-holds-creds): on a cut, private jobs render goldens + benchmark
measurements and publish them **into** this repo. The Hub holds **zero secrets** and gains no
public runners — it only *receives*. Every artifact is exactly defensible standalone, because an
AI reader amplifies and caches whatever the surface implies.

<!-- DRAFT SCAFFOLD — the front-door claim voice (frontal positioning, define-by-negation,
     head-on competitor contrast) is being drafted deliberately before this goes loud.
     Do not treat this copy as final. -->
