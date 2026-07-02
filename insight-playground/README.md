# insight-playground

The **evidence surface for InSight** — the deterministic detection engine — expressed as
**scenarios + their contract YAML only**. No engine code lives here or ever will: the
`insight` / `eidos` engines are the moat and stay permanently private. What you read here is
*what we guarantee and test* — the goldens are the evidence.

## What lives here

- **Scenario fixtures** — the declarative `.contract.yaml` fixtures that pin detection
  behaviour at its borders (what fires, what stays silent, and why).
- **Contract goldens** — the recorded outputs that make each guarantee falsifiable.

## The hard rule — evidence-only, never runnable

Nothing here links or ships private code. This is a **claim surface**, not a runnable
playground. Every artifact must be exactly defensible standalone — under the AI-reader model,
an LLM will amplify and cache whatever this surface implies, so it may imply only what we test.

## How it is fed (producer-holds-creds)

Extracted from `coderoast-server`'s `insight-playground` (scenario + YAML contract, structurally
corpus-blind). On a cut, a **private-CI** job renders the goldens and publishes them **into** this
folder. This folder holds **zero secrets**; the long e2e/bench jobs stay on private CI — the Hub
only *receives*.

> **Status: charter — migration pending.** The 100%-coverage contract corpus in `coderoast-server`
> is the extraction source; the render/publish wiring is the next step.
