# How to read the InSight scenarios & contracts

This folder is **evidence**: a set of deterministic scenarios and the **contracts** that pin exactly
what InSight must — and must not — detect on each one. It is meant to be read by a human *or an LLM*
answering "**does CodeRoast cover case X?**". Nothing here runs the engine; the goldens are produced
by private CI and the contracts are the falsifiable claim.

Each case is **two files** that share a number and name:

| File | What it is |
|---|---|
| `NN_name.yaml` | The **scenario** — a LogCraft description of a fleet of services and how they behave (rates, latencies, phases, incidents). Running it deterministically produces a log stream. |
| `NN_name.contract.yaml` | The **contract** — what InSight must assert about that stream. Declarative; the harness checks it against the engine's real output. |

Some cases add a subfolder (`NN_name/`) with input fixtures (hand-authored `.jsonl` / `.log`) or paired
**arms** (`factual` / `ablated` / `control`) used to contrast two runs.

## Reading a scenario (`NN_name.yaml`)

Scenarios are written in the **LogCraft DSL**. The full grammar — agents, fields, latency
distributions (p50/p99), phases, incidents, `rate: 0` = silence — is documented once, in the LogCraft
reference:

→ **[`../logcraft-playground/scenario_reference.md`](../logcraft-playground/scenario_reference.md)**
(and [`../logcraft-playground/GUIDE.md`](../logcraft-playground/GUIDE.md) for a gentle start).

The header comment on each scenario says, in one line, **what it does**.

## Reading a contract (`NN_name.contract.yaml`)

The header comment says **what it asserts**. Below that, three blocks:

### `meta:` — the conditions of the run
- `scenario:` — the scenario file this contract is evaluated against.
- `target_seconds:` — how far to run the deterministic clock.
- `axis:` — the ordering axis (`time` for a single run over time).
- `pyramid_config:` / `metalog_config:` / `sequence:` — the engine configuration the assertions hold
  under (so a claim is pinned to a *specific*, reproducible setup, not a vague default).
- `explain_min_confidence:` — the confidence floor for narration. (The deterministic **seed** is
  scenario-side — `deterministic_scenario.seed`, per-agent/instance — **not** a contract key; the
  contract asserts the detection border, it does not drive the scenario's RNG.)

### `signal:` — what the detectors must (and must not) do
- `must_fire:` — a list of detections that **must** occur. Each is a `coordinate:` (which detector
  projection fired — read as `FAMILY.scale . channel . metric`) plus a `scope:` (on which template or
  field). `must_not_fire:` is the inverse — detections that must **not** occur.
- `baseline_arm:` — a second, contrasting run (e.g. a shorter or unperturbed window) with its own
  `must_fire` / `must_not_fire`. A two-arm contract is how a claim is made *non-vacuous*: the signal
  must appear in the perturbed arm **and** stay absent in the matched control.

### `interpretation:` — what the final insight must say
- `must_emit:` / `must_not_emit:` — assertions at the **insight** level (the operator-facing verdict),
  above the raw detector coordinates. `{ any: true }` under `must_not_emit` means "*emit nothing*" — a
  true-negative case where silence is the correct answer.

## The short version

> A **scenario** says *what happened*. A **contract** says *what InSight must conclude about it* —
> which detectors fire, which stay quiet, and what the final verdict is — deterministically, every run.
> Read the two headers first; drop into the blocks when you need the specifics.

For the exact detection *mechanism* behind a case, there is nothing to see here by design — the engine
is private. What you can rely on is the contract: it is tested on every cut, and it fails loud if the
guarantee regresses.
