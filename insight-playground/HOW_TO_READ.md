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

Some cases add a subfolder (`NN_name/`) with input fixtures (hand-authored `.jsonl` / `.log`), or a
paired `control` scenario file used to contrast two authored runs.

**Transition cases are ONE bundled file** (`NN_name.yaml` carrying both roots): the
`deterministic_scenario` declares the world **and** the intervention — an axis edge — and the
`contract_scenario` root addresses **coordinates** of that axis. The second arm is *derived* by the
engine from the declared edge, never hand-authored, so the intervention has exactly one source of
truth. Two axes carry coordinates, and a position addresses the one its scenario declares:
`causal_axis: <edge-name|null>` (a counterfactual family — the name is the coordinate) or
`build_axis: <k>` (a CI build history — the ordinal is the coordinate, and there is no time
coordinate to give, because CI steps compare per build increment rather than instant to instant).
A transition reads:

```yaml
contract_scenario:
  reference_scenario: <the scenario's name>     # a checked label
  invariant:                                    # control cells — must be unmoved by EVERY transition
    - cube_a: { level: ERROR, where: [notifier] }
  positions:                                    # named coordinate vectors — the claim anchors
    - name: factual
      coordinates: { causal_axis: null,        time_axis: 10s }   # null = the base world
    - name: ablated
      coordinates: { causal_axis: <edge-name>, time_axis: 10s }   # after the intervention
  transitions:                                  # one comparison each, between named positions
    - from: factual
      to: ablated
      compare: RAW.run                          # which stratum of each run is compared
      expect:
        collapses:     [ ... ]                  # cells the intervention must REMOVE
        reappears_as:  [ ... ]                  # what the collapsed location degrades to
        untouched_projection: { exclude_where: [ ... ] }  # everything else byte-identical
```

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
  A second, contrasting anchor is how a claim is made *non-vacuous*: the signal must appear at the
  perturbed coordinate **and** stay absent at the matched control. In the bundled form that second
  anchor is simply another `position:` — an earlier time coordinate (silent before the trigger), or a
  different world coordinate on the scenario's axis.

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
