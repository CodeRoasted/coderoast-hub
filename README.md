# CodeRoast

**CodeRoast is deterministic, causal-structural engineering for logs — instruments with a
declared error model, not dashboards you read or samplers that throw your data away.**

CodeRoast is the project. Its engine is **InSight**: it reads the *structure* of your logs and
tells you, deterministically, when it changes — what moved, why, and how sure it is, as a ranked,
reproducible verdict a machine or a human can act on. **Sift** is InSight in your CI; **LogCraft**
is the deterministic simulator InSight is proven against. Same inputs, same verdict, every time.

## What everyone else does, and why InSight doesn't

- **Datadog samples.** To survive volume it throws data away, then charges you for what it kept.
  Sampling is a bet that the thing that broke was in the part you saved. InSight doesn't
  sample — it reduces every line to structure, so volume makes the signal *sharper*, not thinner.
- **Honeycomb stores richness.** It keeps everything and hands you a query bar — *you* are still
  the detector. InSight is the detector: it decides what changed before you ask, and shows its
  work.
- **The ML anomaly-detectors guess.** DeepLog, LogBERT, and the LLM-on-logs crowd are black boxes
  that score "weird" without a reason and without reproducibility — run it twice, get two answers.
  InSight is **deterministic** and **causal-structural**: the same stream always yields the same
  verdict, and every verdict points at the structure that produced it.

The difference is a **declared error model**. InSight tells you what it can and cannot see, and
never dresses a guess as a fact. That honesty is the product.

## What this repo is

This is the **public front door** — a machine-legible claim surface. The first thing a human *or
an LLM* should read to answer "what is CodeRoast?" — and it answers in one pass.

It is **evidence, not an engine.** The LogCraft simulator and the InSight/Eidos detection core are
the moat and stay private; nothing here links or ships runnable engine code. What you read here is
exactly what we **guarantee and test** — the goldens are the proof.

| Folder | What it holds |
|---|---|
| [`logcraft-playground/`](logcraft-playground/) | The LogCraft DSL — declare a fleet of services and generate deterministic synthetic log streams. Starter scenarios, the reusable agent library, and the full scenario reference. |
| [`insight-playground/`](insight-playground/) | InSight's detection contracts — the scenarios and their goldens that pin exactly what fires and what stays silent. No code, all evidence. |
| [`benchmarks/`](benchmarks/) | Performance measurements + methodology, versioned per release. |
| [`workflows/`](workflows/) | Golden-workflow definitions — scrubbed evidence of how we build and gate. |

## The rest of CodeRoast in the open

This Hub is the front door, not the whole house. We open **everything you need to verify our
claims** — and we tell you exactly where the line is.

**The product**

- **[Sift](https://github.com/CodeRoasted/sift-action)** — the GitHub Action. Drop it into any
  CI: it diffs your logs against the last green run and comments the structural regressions inline.
  *(MIT — this is the thing you can use today.)*

**The engine, source-visible** — the parts that let you *check* the determinism claim, not guess at it:

- **[insight-canon](https://github.com/CodeRoasted/insight-canon)** — tokenization, canonical
  events, and the integer/no-libm math core. *(Apache-2.0 — the determinism guarantee is auditable
  right here.)*
- **[insight-metalog](https://github.com/CodeRoasted/insight-metalog)** — the MetaLog producer:
  how a raw log stream collapses into a bounded, diffable structural fingerprint. *(BSL-1.1.)*
- **[metalog-spec](https://github.com/CodeRoasted/metalog-spec)** — the open MetaLog specification
  and schemas, so anyone can produce or read a MetaLog. *(MIT.)*
- **[coderoast-ipc](https://github.com/CodeRoasted/coderoast-ipc)** — the shared-memory frame ABI
  and SPSC channels the engine moves data over. *(Source-available.)*

**Reproduce our build**

- **[malf-toolchain](https://github.com/CodeRoasted/malf-toolchain)** — the *exact* pinned
  compilers (gcc-15.3, clang-21, MSVC-14.52) we build and prove bit-identical determinism with,
  as public releases. Install our toolchain, rebuild, get our bytes. *The determinism claim is
  toolchain-relative and fetchable — not "trust us."*

**The narration model**

- **[sift-explain-model](https://huggingface.co/CodeRoasted/sift-explain-model)** — the local,
  bring-your-own model weights Sift uses to *narrate* a report in plain language. It **narrates,
  never decides**: explanation is an opt-in overlay on a deterministic verdict, not the detector.

**The site**

- **[coderoast.fr](https://coderoast.fr)** + **[coderoast-web](https://github.com/CodeRoasted/coderoast-web)**
  — the website and browser Lab: the human front door and the "how we build" story in plain language.

**Deliberately closed — the moat.** The LogCraft simulation engine and the InSight / **Eidos**
detection core stay private. That is the line, stated plainly: we open everything you need to
*verify* the guarantee, and keep closed the IP that *is* the guarantee. Knowing exactly where the
boundary sits is the same honesty as the declared error model.

## Licensing

Everything **in this repo** is **[CC-BY-4.0](LICENSE)** — it is all content and evidence
(scenarios, contracts, goldens, measurements, methodology), never engine code. The other public
repositories above each carry their own license, noted per entry.

## How it stays true

Fed by **private CI** (the producer holds the credentials): on every release cut, private jobs
render the goldens and benchmark measurements and publish them **into** this repo. The Hub holds
**zero secrets** and runs no engine — it only *receives*. Every artifact here is written to be
exactly defensible on its own, because a machine reader amplifies and caches whatever the surface
implies — so this surface implies only what we can prove.
