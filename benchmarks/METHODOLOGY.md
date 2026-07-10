# benchmark methodology

How every number in `SUMMARY.md` and the `*.baseline.json` files is produced and what it
does — and does not — claim.

> Evidence snapshot for **v1.7.6**.

## What is measured

Each engine ships a micro-benchmark suite (Google Benchmark). On a release cut, the engine's
own CI runs it **fresh on the release runner** (median over 5 repetitions — variance-aware)
and records, per benchmark, the median wall-time plus **domain counters**: the cardinalities
the cost scales with — template count, n-gram count, lines-per-second, ns-per-line. The
counters are the point: they let a reader see *why* a stage costs what it does and how it
grows, independent of the machine it ran on.

## The invariant we actually gate — ordering, not absolute µs

Absolute timings are machine-relative, so the release gate never asserts a µs budget. It
asserts a **cross-stage ordering** over the full `simulate -> ingest -> compress -> diff`
pipeline: **ingestion (O(lines)) must stay the single largest stage.** That ordering is
healthy — you read more than you compress, and compress more than you diff — and it is
machine-robust. A regression that flips it (some later stage overtaking ingestion) blocks
the cut. A secondary, **advisory** per-stage band compares each stage against the prior cut's
numbers on the same runner; it warns, it does not block. A run captured with CPU frequency
scaling enabled is rejected before it can be published, so a throttled measurement never
becomes evidence.

## Provenance — read the shape, not the wall-time

Each measurement is taken on the release runner at the tag. Its identifying machine context
(host name, build paths, load) is stripped before publication; a non-identifying
`machine_class` (CPU count, clock, cache sizes) is retained so the numbers are interpretable.
The trustworthy signal is the **shape** — relative stage cost and how each stage scales with
the counters — not the absolute time, which depends on the runner.

## Toolchain

The ship leg is GCC-15.3 / libstdc++ with `-ffp-contract=off` and pinned CMake/Conan (the
same pinned toolchain the determinism proof uses).

---
*Published under CC-BY-4.0. Evidence-only: the benchmark harness runs on private CI against
the private engines; this folder holds the results and the method, never a way to re-run the
engine.*
