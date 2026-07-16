# benchmarks

**Measurements + methodology** — the performance evidence for the CodeRoast engines,
published as data you can read and reproduce the *shape* of, never as a runnable harness.

> Evidence snapshot for **v1.8.0**. Each engine measures itself fresh on the release runner at
> the cut and publishes here.

## What lives here

- **[SUMMARY.md](SUMMARY.md)** — per-stage measurements: benchmark, median time, and the
  template / n-gram cardinality the cost scales with.
- **[METHODOLOGY.md](METHODOLOGY.md)** — what is measured, the ordering invariant we gate on,
  the provenance caveat, and the toolchain.
- **`*.baseline.json`** — the same measurements, machine-legible (identifying context
  stripped; a non-identifying `machine_class` retained).

## The hard rule — evidence-only, never runnable

The benchmark *harness* runs on private CI (it needs the private engines). This folder holds
the **results and the method**, so a reader — human or machine — can see what we measure and
how, and judge the claim. It does not ship a way to re-run the private engine.

## How it is fed (producer-holds-creds)

On a cut, each engine's CI measures itself and publishes its numbers; a private aggregation
job merges them **into** this folder (in-tree + a tagged Release asset). Zero secrets here.

---
*Published under CC-BY-4.0.*
