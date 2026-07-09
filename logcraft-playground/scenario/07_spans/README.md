# 07 — Span-native scenarios (OTLP spans)

These scenarios emit **OpenTelemetry OTLP JSON spans** (`format: otel_span`) instead of log
lines: a [causal flow](../../scenario_reference.md#causal-flows) instance is a *trace*, each
visited state is a *span*, and the parent is the spawning step's span. They demonstrate the
three span-native DSL knobs — `format: otel_span`, per-state `span_duration_ms`, and
`fan_out: true` — documented under [Span output](../../scenario_reference.md#span-output-otel_span).

Run any of them and you get one flat span object per line on stdout:

```
logcraft run scenario/07_spans/03_duration_shift_green.yaml
```

## Green / red trace-diff pairs

Each pair plants **exactly one** structural change in the target flow and keeps a matched
control that stays stationary — the two-arm shape a trace-diff consumer scores (added span /
dropped branch / duration-regime shift = the *loud* arm; the control = *quiet*).

| Pair | Green | Red | The single planted change |
|---|---|---|---|
| Added span | `01_added_span_green.yaml` | `01_added_span_red.yaml` | red inserts a new `validate` span the green lacks |
| Dropped branch | `02_dropped_branch_green.yaml` | `02_dropped_branch_red.yaml` | red drops the `sms` fan-out child branch |
| Duration shift | `03_duration_shift_green.yaml` | `03_duration_shift_red.yaml` | red moves `charge` from a ~20 ms to a ~200 ms regime; everything else byte-identical |

The `heartbeat` control flow (pairs 1–2) is byte-identical across green/red — a graph change in
one flow provably cannot perturb another (position-stable RNG). For the duration pair, green **is**
the stationary control: `span_duration_ms` is drawn last, so only `charge`'s duration moves.

## Fan-out checkpoint

`04_fanout_observed.yaml` — a `max_concurrent > 1`, two-branch fan-out. Its **observed** parentage
DAG (`ingest→transform_a`, `ingest→transform_b`, each transform → its sink) is clean, while a naive
**sequential-adjacency** graph over the interleaved emission order manufactures sibling and
cross-trace edges the observed DAG never contains.

> **Determinism.** Every scenario here is seeded and single-worker; the emitted span stream is
> bit-identical across replays. The paired producer assertions live in
> `logcraft/core/tests/determinism/test_span_trace_diff.cpp`.
