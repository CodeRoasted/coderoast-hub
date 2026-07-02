# benchmarks

**Measurements + methodology** — the performance evidence for the CodeRoast engines, published
as data you can read and reproduce the *shape* of, never as a runnable harness.

## What lives here

- **Measurements** — per-cut benchmark results (per-stage µs + the template / n-gram cardinality
  the cost scales with), versioned and comparable across tags.
- **Methodology** — how each number was produced: the workload, the cardinality, the gate
  (ordering invariant + per-stage regression band), the toolchain.

## The hard rule — evidence-only, never runnable

The benchmark *harness* runs on private CI (it needs the private engines). This folder holds the
**results and the method**, so a reader — human or machine — can see what we measure and how, and
judge the claim. It does not ship a way to re-run the private engine.

## How it is fed (producer-holds-creds)

On a cut, the private benchmark job renders the measurements and publishes them **into** this
folder (in-tree + tagged Release assets). Zero secrets here.

> **Status: charter — first measurements pending.** The standing benchmark mandate (every cut, a
> pushed/versioned baseline) is the source; the render/publish wiring is the next step.
