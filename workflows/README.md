# workflows

**Evidence of process** — the golden-workflow definitions that show *how CodeRoast is built and
guaranteed*, published as scrubbed, machine-legible artifacts.

## What lives here

- **Golden-workflow definitions** — the canonical process/CI shapes that produce and gate our
  guarantees, presented as evidence-of-process (not the live private pipelines).

## The hard rule — evidence-only, never runnable, scrubbed

These are **scrubbed** copies: no secrets, no private repo names, no internal flaw/bug IDs, no
private paths. They demonstrate the discipline (deterministic gates, cross-toolchain proof,
benchmark-on-cut) without exposing the private machinery or handing a reader a runnable pipeline.

## How it is fed (producer-holds-creds)

Rendered and scrubbed by a private-CI job and published **into** this folder on a cut. Zero
secrets here.

> **Status: charter — first definitions pending.** Scrub rules must pass before any workflow lands
> (public-repo pre-launch scrub: flaw-IDs / private refs / secrets).
