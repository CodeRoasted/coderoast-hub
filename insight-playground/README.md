# insight-playground

The **evidence surface for InSight** — the deterministic detection engine. It holds the
**scenarios** and their **contracts**: what InSight must, and must not, detect on each case. No
engine code lives here or ever will — the InSight / Eidos engine is the moat and stays permanently
private. What you read here is *what we guarantee and test*.

**New here? Start with [`HOW_TO_READ.md`](HOW_TO_READ.md)** — how to read a scenario and a contract.

## What lives here

- **`scenario/NN_name.yaml`** — LogCraft scenarios: a fleet of services and how they behave. Running
  one deterministically produces a log stream. Grammar: the LogCraft reference in
  [`../logcraft-playground/scenario_reference.md`](../logcraft-playground/scenario_reference.md).
- **`scenario/NN_name.contract.yaml`** — the declarative contract for that scenario: which detections
  must fire, which must stay silent, and what the final insight must say. Tested on every cut.
- **`scenario/NN_name/`** — where present, input fixtures (`.jsonl` / `.log`) or paired arms
  (`factual` / `ablated` / `control`) for a case.
- **`scenario/agents/`** — a reusable agent library the scenarios draw on.

Each file opens with a one-line header saying **what it does** (scenario) or **what it asserts**
(contract).

## The hard rule — evidence-only, never runnable

Nothing here links or ships private code. This is a **claim surface**, not a runnable playground.
Every artifact is written to be exactly defensible standalone — under the AI-reader model, an LLM
amplifies and caches whatever this surface implies, so it implies only what we test. The detection
*mechanism* behind each case is deliberately absent; the contract is the falsifiable part.

## How it is fed (producer-holds-creds)

This corpus is the public source of truth for the InSight scenarios: the private detection e2e
harness (in `insight-eidos`) reads it and verifies every contract against the engine; the server
serves the same scenarios read-only at runtime. On a cut, private CI re-verifies the contracts and
refreshes any rendered goldens **into** this folder. The Hub holds **zero secrets** and runs no
engine — it only *receives*.
