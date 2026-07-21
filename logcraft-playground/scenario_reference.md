# LogCraft Scenario Reference

Complete, source-derived reference for every configuration key in a LogCraft scenario
file. Generated from direct source-code audit of the scenario parsers
(`scenario_loader.cpp`, `scenario_*_parsing.cpp`, `scenario_validation.cpp`), the config
and capability modules (`core.api-agent.cppm`, `core.api-scenario.cppm`), and
`field_generator.cpp`. This is the single source of truth;
`logcraft/technical_docs/reference/scenario_reference.md` redirects here.

A scenario is a YAML file under **exactly one world root**: `scenario:` — the real,
wall-clock world, randomized on every run — or `deterministic_scenario:` — the virtual-clock
world that replays bit-identically. The root **selects the engine**: a `seed:` is required
under `deterministic_scenario:` and rejected under `scenario:`, so the root key alone tells
you which world a file describes (see [Scenario Root Keys](#scenario-root-keys) and
[Engine Modes](#engine-modes)). These scenarios are openly published (CC-BY-4.0); the
LogCraft **engine** that runs them is part of [CodeRoast](https://coderoast.fr), where you
run a scenario in the hosted **Lab**.

---

## Table of Contents

- [Scenario Root Keys](#scenario-root-keys)
- [Duration Format](#duration-format)
- [Rate Format](#rate-format)
- [Engine Modes](#engine-modes)
- [Outputs](#outputs)
  - [Output Types](#output-types)
  - [Output Formats](#output-formats)
  - [Output Options](#output-options)
- [Agents](#agents)
- [Fields & Generators](#fields--generators)
  - [weighted_choice](#weighted_choice)
  - [choice](#choice)
  - [range](#range)
  - [sequence](#sequence)
  - [static](#static)
  - [timestamp](#timestamp)
  - [normal](#normal)
  - [percentile](#percentile)
  - [conditional](#conditional)
- [Phases](#phases)
  - [Distribution drift (ramps)](#distribution-drift-ramps)
- [Latency](#latency)
- [Templates](#templates)
- [Causal Flows](#causal-flows)
- [Interventional Axes](#interventional-axes)
- [Rules](#rules)
- [Incidents](#incidents)
- [Health State Machine](#health-state-machine)
- [State & Effects](#state--effects)
- [Rate Modulation](#rate-modulation)
- [Auto-Cascade](#auto-cascade)
- [Noise](#noise)
- [Users & Personas](#users--personas)
- [Entity Pool](#entity-pool)
- [Field Variations](#field-variations)
- [Output Field Projection](#output-field-projection)
- [System Archetypes](#system-archetypes)
  - [Contention](#contention)
  - [Slow Queries](#slow-queries)
  - [Availability](#availability)
  - [Failures](#failures)
- [Registry](#registry)
- [Includes](#includes)
- [Replay](#replay)
- [Clock](#clock)
- [Pipeline](#pipeline)
- [Time Context](#time-context)
- [Environment](#environment)

---

## Scenario Root Keys

A file starts with **one** world root: `scenario:` (the REAL, wall-clock world) or
`deterministic_scenario:` (the DETERMINISTIC, virtual-clock world — a `seed:` is required). See
[Engine Modes](#engine-modes). The **document root is a closed vocabulary** — `scenario:`,
`deterministic_scenario:`, and an optional bundled `contract_scenario:` (read by the InSight
contract harness, ignored by LogCraft); any other document root is a **hard reject** (a typo'd root
must fail loudly, never parse as an empty scenario). *Scenario-level* unrecognized keys warn but do
not fail parsing.

The worlds differ in **shape**: the real world is **flat**; the deterministic world nests its world
under an **axis block**, keeping scenario **config** at the root. Which axis you declare says what the
world is compared along: `time_axis:` (the stream world — the clock plus the world it scopes),
`build_axis:` (the CI world — the world inline, no clock, because CI steps compare per build
increment), or `causal_axis:` wrapping a `time_axis` one level deeper. See
[Interventional Axes](#interventional-axes).

```yaml
# REAL — flat, no axis
scenario:
  name: "my-scenario"
  duration_seconds: 5m
  agents:
    - { name: api-server, rate_per_second: 100 }

# DETERMINISTIC — the world nests under time_axis
deterministic_scenario:
  name: "my-scenario"
  seed: 42                    # config lives at the root
  outputs: [ ... ]            # config
  time_axis:                  # the clock + the world it scopes
    duration_seconds: 5m
    epoch_duration_ns: 1s      # the epoch grid (optional; default 1s)
    agents:
      - { name: api-server, rate_per_second: 100 }
    incidents: [ ... ]
    flows: [ ... ]
```

**Config keys — at the root in both worlds:**

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `name` | string | `"unnamed"` | Human-readable scenario name |
| `seed` | uint64 | 42 (det) | The RNG root. **Required** under `deterministic_scenario:`; **rejected** under `scenario:`. See [Engine Modes](#engine-modes) |
| `outputs` | sequence | `[{type: console, format: json}]` | Output sink definitions |
| `pipeline` | map | absent | Sharded pipeline config |
| `templates` | map | absent | Named reusable agent presets |
| `registry` | map | absent | External agent file registry |
| `includes` | sequence | absent | Merge other YAML files |
| `causal_axis` | map | absent | The counterfactual axis — `{ edges, time_axis }`; NAMED coordinates. When declared, `time_axis` nests under it. Deterministic only. See [Interventional Axes](#interventional-axes) |
| `build_axis` | map | absent | The CI history — `{ edges, <the CI world inline> }`; ORDINAL coordinates, no `time_axis`. Deterministic only. See [Interventional Axes](#interventional-axes) |

**World keys — under `time_axis:` in the deterministic world; flat at the root in the real world:**

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `duration_seconds` | string/number | `0` | Auto-stop duration (`0` = run forever). Duration string (`"5m"`) or seconds. See [Duration Format](#duration-format) |
| `epoch_duration_ns` | int/duration | `1s` | *(deterministic)* the epoch grid. Int ns or `1s`/`250ms`/`1us` |
| `start_time_unix_ns` | int | `0` | *(deterministic)* the virtual-clock start |
| `timezone` / `offset_minutes` | string/int | `UTC` / `0` | Calendar context; `local` is real-only |
| `agents` | sequence | required | One or more agent definitions |
| `environment` | map | absent | Global metadata (region, cluster, version) |
| `noise` | map | absent | Global noise settings |
| `users` | map | absent | Simulated user pool |
| `personas` | sequence | absent | User behavior profiles |
| `entity_pool` | sequence | absent | Shared entity IDs for cross-agent correlation |
| `field_variations` | sequence | absent | Numeric field jitter config |
| `incidents` | sequence | absent | Time- or probability-triggered events |

**Real-world-only keys — at the root under `scenario:`; rejected under `deterministic_scenario:`:**

| Key | Type | Description |
|-----|------|-------------|
| `rules` | sequence | Propagation rules |
| `auto_cascade` | map | Automatic error cascading |
| `replay` | map | Replay a recorded session |

**Deterministic-world-only keys — rejected under `scenario:`:**

| Key | Type | Description |
|-----|------|-------------|
| `flows` | sequence | Causal flows — instanced traces (see [Causal Flows](#causal-flows)). A world key: under `time_axis:`, or under `build_axis:` in the CI world |
| `seed` | uint64 | The RNG root — required here, and the reason the real world has no deterministic replay |
| agent `seed` / `instances_seed` | uint64 / sequence | Per-agent and per-instance RNG seed bases (see [Agent Keys](#agent-keys)) |

---

## Duration Format

Durations accept a string with a suffix or a plain number (seconds).

| Format | Example | Seconds |
|--------|---------|---------|
| `Ns` | `"30s"` | 30 |
| `Nm` | `"5m"` | 300 |
| `Nh` | `"1h"` | 3600 |
| plain | `120` | 120 |
| `0` | `0` | Run forever |

Fractional values are supported: `"0.5s"`, `"1.5m"`.

---

## Rate Format

Rates accept `"N/s"` or a plain number (records per second).

```yaml
rate_per_second: 200/s   # string form ("N/s")
rate_per_second: 200     # plain number (records per second)
```

`rate_per_second: 0` is **silence** — a first-class state, **never** a fallback to
`1/s`. The agent emits **no records** while staying alive and re-armable. It is
honored everywhere a rate is read, **including the first phase from `t = 0`**:

- A **not-yet-deployed service** — `phases:` whose **phase 0** sets `rate_per_second: 0`
  and a later phase raises it — is silent from the start and begins emitting only when
  it "deploys". (This is honored from `t = 0`; a phase-0 silence is applied at agent
  start, not skipped.)
- An agent or a **later** phase set to `0` goes quiet at that sim-time boundary
  (vanish-a-template-at-T).
- A **flow-only service** — the agent exists only so a `flows:` trace can log *through*
  it (no `start_delay` hack) — and silencing background agents so a flow spine is the
  only stream.

**Set vs omit (absent ≠ 0):** a phase that **sets** `rate_per_second: 0` silences; a
phase that **omits** the key keeps the current rate. The per-field default (agent
`1.0`, phase inherits) applies only when the key is **absent**, never to an explicit `0`.

---

## Engine Modes

| Mode | Selected by | Clock | Notes |
|------|-------------|-------|-------|
| **Real** | `scenario:` root (no `seed:`) | real wall-clock (structural) | Default. Randomized each run. Flat — no axis. |
| **Deterministic** | `deterministic_scenario:` root (`seed:` required) | virtual (structural; no `clock:`/`mode:`) | Same logs every run. The clock + world nest under `time_axis`; `epoch_duration_ns` sets the epoch grid. Forces `pipeline.policy: block`; rejects `local` timezone + the real-only knobs. |

In deterministic mode the clock is **virtual by construction** (the `deterministic_scenario:` root
types the world — there is no `clock:`/`mode:`); the loader forces `pipeline.policy: block` when the
pipeline block is absent, and emits a notice.

---

## Outputs

Define where and how logs are written. All outputs receive the same events simultaneously.

```yaml
outputs:
  - name: elastic          # Optional name (required for per-agent routing)
    type: http
    url: "http://localhost:9200/_bulk"
    format: ecs
    http_batch_size: 100
    http_flush_interval_ms: 1000

  - type: console
    format: json
```

### Output Types

| Value | Description |
|-------|-------------|
| `console` | Print to stdout |
| `file` | Write to disk with optional rotation |
| `recording` | Write JSONL for later replay |
| `http` | Batched HTTP POST (e.g. Elasticsearch, Loki, any webhook) |
| `prometheus` | Expose `/metrics` scrape endpoint |
| `statsd` | Push metrics over UDP |
| `insight_shm` | Shared-memory IPC channel for InSight integration |

### Output Formats

Every output except `prometheus` and `statsd` requires a `format:` (or `formats:`) field.

| Value | Alias | Description |
|-------|-------|-------------|
| `json` | — | Structured JSON, newline-delimited |
| `text` | — | Human-readable key=value |
| `clf` | — | Apache/Nginx Combined Log Format |
| `apache_error` | — | Apache error log |
| `log4j` | — | Log4j / Python logging format |
| `syslog` | — | BSD syslog (RFC 3164) |
| `rfc5424` | — | IETF syslog (RFC 5424) |
| `nginx_error` | — | Nginx error log |
| `kv` | `logfmt` | Key=value / logfmt |
| `android_logcat` | — | Android logcat |
| `windows_cbs` | — | Windows CBS/CSI log |
| `spark_hdfs` | `spark` | Apache Spark / HDFS |
| `health_app` | — | Health app pipe-delimited |
| `proxifier` | — | Proxifier bracket format |
| `cloudwatch` | — | AWS CloudWatch JSON |
| `systemd_journal` | — | systemd journal JSON export |
| `hpc` | `bgl` | HPC / Blue Gene/L |
| `iis_w3c` | `iis` | IIS W3C Extended log |
| `ecs` | — | Elastic Common Schema 8.x |
| `otel` | `opentelemetry`, `otlp` | OpenTelemetry OTLP JSON **log record** |
| `otel_span` | `otlp_span`, `otel_trace` | OpenTelemetry OTLP JSON **span** — one flat span object per line (`traceId` / `spanId` / `parentSpanId` / `name` / `startTimeUnixNano` / `endTimeUnixNano` / `status` / `service.name`). Renders a [causal flow](#causal-flows)'s trace/span context + `span_duration_ms`; a non-flow record becomes a valid synthesised root span. This is the span-native surface (see [Span output](#span-output-otel_span)) |
| `github_actions` | `gha` | Timestamped line with a GitHub Actions workflow-command prefix (`::error::` / `::warning::`; empty for info/trace) — the surface Sift annotates from |
| `raw` | `messy`, `stdout` | Unstructured `LEVEL message field=value` line — CI/app-stdout "dirty logs" the structured formats never exercise |

When `formats:` (sequence) is set it overrides `format:` (single string), allowing one
sink to write multiple formats to the same path prefix.

### Intent channel

Some log formats have **more than one way to write the same thing**. A GitHub Actions step banner is
the standing example — the runner writes it wrapped:

```
2026-05-01T10:00:00.1000000Z ##[group]Run yarn lint
```

while a log that has had its workflow commands removed carries the same step as:

```
2026-05-01T10:00:00.1000000Z Run yarn lint
```

Same step, same identity, two **materializations**. The channel is which one you render:

```yaml
outputs:
  - type: file                      # the sink — where bytes go
    format: github_actions          # the format — the line shape + its enrichment
    intent_channel: annotated       # the channel — which materialization
    path: build.log
```

Declare it, or the writer defaults to `annotated` — the form GitHub actually serves. `stripped` is a
deliberately structure-poor lab form (a measurement control arm, not a channel GitHub serves): asking
for it is the deliberate act, never the silent default.

| Key | Axis | Question it answers |
|-----|------|--------------------|
| `type` | sink / transport | *Where do the bytes go?* |
| `format` | intent format | *What shape are the lines?* |
| `intent_channel` | intent channel | *Which materialization of that shape?* |

**`github_actions` channels:**

| Channel | Step banner | What it is |
|---------|-------------|------------|
| `annotated` (default) | `##[group]Run <cmd>` | **What GitHub actually serves.** The API, the Action, and a log download all give you this |
| `stripped` | `Run <cmd>` | An intentionally structure-poor form. Used as a control arm when measuring how much the structure buys — **not** a form GitHub serves |

Notes:

- **The key is `intent_channel`, spelled in full** — `channel:` on an output already names the shared-memory
  ring, and YAML would silently keep only one of two identical keys.
- **An unrecognized channel name is a hard error at parse**, not a fallback. A typo would otherwise render
  the Job banner and silently drop every Step — a hollow document that still looks plausible.
- Formats with only one materialization (everything except `github_actions` today) ignore the key.

### Output Options

All options are parsed per-sink and ignored when not applicable to the sink type.

| Key | Type | Default | Applies to | Description |
|-----|------|---------|-----------|-------------|
| `name` | string | `""` | all | Named outputs support per-agent routing |
| `type` | string | `"console"` | all | Sink type (see table above) |
| `format` | string | `"json"` | all | Single format (see table above) |
| `formats` | sequence | `[]` | all | Multi-format; overrides `format` when non-empty |
| `recording_format` | string | `"jsonl"` | `recording` | Recording sub-format (`smf` \| `jsonl`). NOT a log formatter — `format:` is **refused** on a `type: recording` output |
| `project_fields` | sequence | absent (= all fields) | all | Field projection — when **present**, only these fields are emitted, in this order (the *which-fields* half, orthogonal to `format`). Presence is load-bearing: **absent** = emit every field, `project_fields: []` = emit **none** |
| `intent_channel` | string | `""` (= writer default, `annotated`) | dialect formats | Which materialization to render (see [Intent channel](#intent-channel)). Only meaningful for a format that has more than one — today `github_actions` |
| `path` | string | `""` | `file`, `recording`, `prometheus` | Output file path or metric prefix |
| `max_size_bytes` | integer | `0` | `file` | Rotate when file exceeds this size (0 = no rotation) |
| `max_files` | integer | `5` | `file` | Number of rotated files to keep |
| `url` | string | `""` | `http` | Destination endpoint URL |
| `http_batch_size` | integer | `100` | `http` | Records per POST request |
| `http_flush_interval_ms` | integer | `1000` | `http` | Max ms before flushing a partial batch |
| `http_content_type` | string | `"application/json"` | `http` | Content-Type header |
| `headers` | map | `{}` | `http` | Extra HTTP request headers (string key-value pairs) |
| `host` | string | `"127.0.0.1"` | `statsd` | StatsD server address |
| `port` | integer | `8125` | `statsd` | StatsD server UDP port |
| `metrics_interval_seconds` | integer | `15` | `prometheus`, `statsd` | Metric snapshot frequency |
| `metrics_prefix` | string | `"logcraft"` | `prometheus`, `statsd` | Metric name prefix |
| `channel` | string | `"coderoast.default"` | `insight_shm` | Shared-memory channel base name |
| `shm_slot_count` | integer | `8192` | `insight_shm` | Number of fixed-size slots per shard |
| `shm_max_payload_bytes` | integer | `4096` | `insight_shm` | Max payload bytes per slot |
| `shm_window_seal_interval_seconds` | number | `25.0` | `insight_shm` | Window seal cadence in seconds |
| `shm_backpressure_policy` | string | pipeline policy | `insight_shm` | `"block"` or `"drop"` (output-level override) |

---

## Agents

Agents are the log-producing services in your simulation. The `agents:` sequence is
required and must contain at least one entry.

```yaml
agents:
  - name: api-gateway             # Required
    intent: web_server            # What the agent IS (see Intent below)
    rate_per_second: 100                     # Records per second
    error_rate: 0.03              # Probability of ERROR-level log (0.0–1.0)
    log_level: info               # Base log level
    instances: 3                  # Run N copies (names become api-gateway-1, -2, -3)
    start_delay_seconds: 5s               # Delay before this agent starts
    use_template: my_template              # Inherit defaults from a template
    message_template: "{method} {path} -> {status_code}"
    fields: [...]
    phases: [...]
    latency_ms: [10, 50]
```

### Agent Keys

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `name` | string | required | Unique identifier; expanded to `name-1`, `-2` when `instances > 1` |
| `intent` | string/map | `""` | What the agent IS — its structural axis (see [Intent](#intent)) |
| `rate_per_second` | string/number | `1.0` / `0` | Records/s as a number or `"200/s"` string. Unbound default depends on the intent: `1.0` for a generic-world agent, `0` (banner-only) for a structural quantum — see [Intent](#intent) |
| `log_level` | string | `"info"` | Default severity: `trace`, `debug`, `info`, `warn`, `error`, `fatal` |
| `level_weights` | map | `{}` | Explicit level distribution weights (auto-normalized) |
| `error_rate` | number | `0.0` | Global ERROR probability (0.0–1.0) |
| `message_template` | string | `""` | Message string with `{field_name}` placeholders |
| `use_template` | string | `""` | Template name to inherit from |
| `instances` | integer | `1` | Number of parallel copies |
| `seed` | uint64 | absent | *(deterministic only)* Re-bases this agent's RNG stream — **one** seed shared by all its instances. Overrides the root `seed:` for this agent |
| `instances_seed` | sequence | absent | *(deterministic only)* One RNG seed **per instance** — the population primitive. Requires `instances:` > 1 and exactly one entry per instance; mutually exclusive with `seed:`. Each expanded copy (`name-1`, `-2`, …) takes its own entry as its seed base, and the instance name still keys the stream, so the copies are independent draws of the *same* agent rather than one stream split N ways |
| `after` | string | absent | *(`build_axis` world only)* the agent this step follows — the declared step chain. Rejected elsewhere: a stream world's agents are a population with no order |
| `start_delay_seconds` | string/number | `0.0` | Startup delay (duration format or seconds) |
| `fields` | sequence | `[]` | Field definitions (see [Fields & Generators](#fields--generators)) |
| `phases` | sequence | `[]` | Time-based behavior phases (see [Phases](#phases)) |
| `latency_ms` | distribution | absent | Latency distribution (see [Latency](#latency)) |
| `dependencies` | sequence | `[]` | Upstream agent names (used by auto_cascade) |
| `health_state` | map | absent | Health state machine |
| `state` | map | `{}` | Internal state variables |
| `effects` | sequence | `[]` | Conditional behavior from state |
| `noise` | map | absent | Per-agent noise overrides |
| `rate_modulation` | map | absent | Time-varying rate changes |
| `slow_queries` | map | absent | Probabilistic slow operations |
| `availability` | map | absent | Uptime and failure mode |
| `failures` | map | absent | Burst failure patterns |
| `contention` | map | absent | Connection pool limits |
| `outputs` | sequence | `[]` | Route to specific named outputs (empty = all) |

---

### Intent

An agent's `intent:` declares **what the agent is** — its structure. It is the agent's one
structural axis. (It replaces the old agent-scope `type:` key, which is now rejected with an
error. `type:` remains valid for output sinks, format nodes and rate models.)

Intent declares **structure only**. The *dynamics* — `rate_per_second`, `error_rate`,
`latency_ms` — are bound separately by the scenario. A structural declaration never carries
behaviour.

**Scalar form** — a generic-world intent. This is what `type: web_server` used to say:

```yaml
agents:
  - name: api-gateway
    intent: web_server        # the agent's identity; reaches the log line
    rate_per_second: 200/s
```

The name is not decorative — it is emitted on every record (the `type` field in `json`
output, `[agent/type]` in `text`). Omit `intent:` entirely and you get the unnamed generic
world: an ordinary flux agent.

**Mapping form** — a declared **structural quantum**. Structural quanta live in the CI world
only (under `build_axis:`), and that axis declares its `dialect:` **once**; a quantum never
restates it. `kind:` is required and must be `job` (container) or `step` (leaf):

```yaml
build_axis:
  dialect: github                                    # declared ONCE for the whole axis
  agents:
    - name: build-job
      intent: { kind: job, payload: "build" }        # BANNER: emits its banner, nothing else
    - name: lint-step
      intent: { kind: step, payload: "yarn lint" }   # CONTENT: banner, then its content flux
      after: build-job
      rate_per_second: 20/s
      error_rate: 0.02
      message_template: "checked {file}"             # the BODY — what makes it a content quantum
      fields:
        - { name: file, generator: choice, values: ["app.ts", "index.ts"] }
```

Agents in declaration order form the document tree. A `job` is a container — it emits its
banner and nothing else. A `step` opens with its banner, then emits content under it **if it
has a body**.

**A structural quantum is a BANNER or a CONTENT quantum, and the difference is the body** — a
`message_template:` (with its `fields:`). That partition decides which dynamics keys are legal,
so it governs the table rather than the other way round:

| Intent | Body | `rate_per_second` | Meaning |
|--------|------|-------------------|---------|
| scalar / absent (generic world) | yes | unbound → `1.0` | An ordinary flux agent |
| `kind: job` / `kind: step` | **no** → BANNER | **refused** | A banner has no body half, so there is nothing for dynamics to bind |
| `kind: job` / `kind: step` | **yes** → CONTENT | **required** | Its content flux is dynamics the scenario must declare (`0` = declared silence) |

A banner needs no `rate_per_second: 0` boilerplate — declaring the quantum is enough. But a
banner does not merely *default* its dynamics away: it **refuses every dynamics key**, with an
error. `rate_per_second`, `error_rate`, `latency_ms`, `use_template:` and the rest are not
silently ignored on a banner, because a DSL that accepts a key it will ignore hides the
mistake. A banner may carry only `name`, `intent`, `use_intent`, `payload`, `after`,
`log_level`, `outputs`, `instances`, `seed`, `instances_seed`, `start_delay_seconds` and
`dependencies` — identity, position, sinks, population; never behavior over time. **To give a
quantum behavior, give it a body.**

`rate_per_second: 0` remains a legitimate explicit binding on a generic agent (that is how
flow-driven agents are silenced) and on a content quantum (declared silence).

Rejected, deliberately, with an error rather than a silent fallback:

- agent-scope `type:` — removed; `type:` and `intent:` were two declarations of one structural axis;
- `intent:` that is neither a scalar nor a mapping;
- the mapping form without `kind:`;
- `kind: none` — a quantum with no quantum; use the scalar form;
- any unrecognized `kind:` spelling;
- per-quantum `intent.name:` — removed; the dialect belongs to the axis and is declared once;
- a structural quantum with no axis `dialect:` to inherit;
- a structural quantum outside `build_axis:` — a stream world's agents are a population with no
  intent tree to hold one; declare a generic intent instead;
- any dynamics key on a banner quantum (see the allowlist above);
- a content quantum with no bound `rate_per_second:`.

## Fields & Generators

Fields define the dynamic data inside each log record. Each field entry needs `name`
and `generator`.

```yaml
fields:
  - name: status_code
    generator: weighted_choice
    values: ["200", "201", "400", "404", "500"]
    weights:  [70,    10,    10,    5,    5]
```

### Universal Field Keys

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `name` | string | Yes | Field identifier in generated records |
| `generator` | string | Yes | Generator type (see below) |
| `level_overrides` | map | No | Map of field value → log level override |

---

### `weighted_choice`

Pick from a list with specified weights.

```yaml
- name: method
  generator: weighted_choice
  values: [GET, POST, PUT, DELETE]
  weights: [60, 25, 10, 5]
```

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `values` | sequence | Yes | List of value strings |
| `weights` | sequence | Yes | Relative weights (same length as `values`; auto-normalized) |

---

### `choice`

Pick uniformly at random from a list.

```yaml
- name: path
  generator: choice
  values: [/api/users, /api/orders, /health]
```

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `values` | sequence | Yes | Must not be empty |

---

### `range`

Random number in a range.

```yaml
- name: bytes_sent
  generator: range
  min: 200
  max: 50000
  integer: true
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `min` | number | `0.0` | Inclusive lower bound |
| `max` | number | `100.0` | Inclusive upper bound |
| `integer` | boolean | `true` | Round to integer; `false` emits two decimal places |

---

### `sequence`

Auto-incrementing counter with optional prefix.

```yaml
- name: request_id
  generator: sequence
  prefix: "req-"
  start_value: 1000
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `prefix` | string | `""` | String prepended to the counter |
| `start_value` | uint64 | `1` | Starting counter value |

Generates: `"req-1000"`, `"req-1001"`, …

---

### `static`

Always the same fixed value.

```yaml
- name: host
  generator: static
  value: "web-prod-01"
```

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `value` | string | Yes | Constant value to emit |

---

### `timestamp`

Formatted date/time from simulation clock.

```yaml
- name: access_time
  generator: timestamp
  strftime: "%d/%b/%Y:%H:%M:%S %z"   # CLF timestamp
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `strftime` | string | `"%Y-%m-%dT%H:%M:%S"` | `strftime()` format string |

Timestamp uses simulation-clock time, not system time. In real mode the timezone
follows `time.timezone`; in deterministic mode it uses the configured offset.

---

### `normal`

Gaussian (bell-curve) distribution.

```yaml
- name: response_time
  generator: normal
  mean: 50
  stddev: 12
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `mean` | number | `0.0` | Distribution mean |
| `stddev` | number | `1.0` | Standard deviation |

Negative values are clamped to `0.0`.

---

### `percentile`

Piecewise distribution defined by percentile targets.

```yaml
- name: latency_ms
  generator: percentile
  p50: 10
  p95: 80
  p99: 300
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `p50` | number | `0.0` | 50th percentile value |
| `p95` | number | `0.0` | 95th percentile value |
| `p99` | number | `0.0` | 99th percentile value |

Distribution shape: uniform [0, p50] → linear [p50, p95] → linear [p95, p99] →
linear [p99, p99 × 1.5].

---

### `conditional`

Different generator per value of a prior field.

```yaml
- name: status_code
  generator: weighted_choice
  values: ["200", "404", "500"]
  weights: [90, 7, 3]

- name: response_body_size
  generator: conditional
  condition_field: status_code    # Must reference a field defined EARLIER in the list
  branches:
    "200":
      generator: range
      min: 100
      max: 10000
      integer: true
    "404":
      generator: static
      value: "0"
    "500":
      generator: range
      min: 50
      max: 500
      integer: true
  default:
    generator: static
    value: "0"
```

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `condition_field` | string | Yes | Name of a field defined earlier in this agent's `fields:` list |
| `branches` | map | Yes | Map of match-value → nested generator config |
| `default` | generator | No | Fallback generator when no branch matches (default: `static: "unknown"`) |

Nested conditionals are allowed. `condition_field` must appear before this field in
the `fields:` sequence.

---

## Phases

Phases override an agent's rate, error rate, or latency for a set duration, in order.

```yaml
agents:
  - name: api-server
    rate_per_second: 50
    phases:
      - name: warmup
        duration_seconds: 30s
        rate_per_second: 10
        latency_ms: [5, 20]
      - name: steady
        duration_seconds: 5m
        rate_per_second: 50
        latency_ms:
          distribution: normal
          mean: 25
          stddev: 8
      - name: peak
        duration_seconds: 1m
        rate_per_second: 150
        error_rate: 0.08
        latency_ms:
          distribution: percentile
          p50: 40
          p95: 200
          p99: 600
```

### Phase Keys

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `name` | string | required | Phase label |
| `duration_seconds` | string/number | `0.0` | Phase duration (duration format or seconds); `0` = run forever |
| `rate_per_second` | string/number | `0.0` | Override agent rate for this phase |
| `error_rate` | number | `0.0` | Override agent error rate for this phase (0.0–1.0) |
| `latency_ms` | distribution | absent | Override agent latency for this phase |
| `field_weight_ramps` | sequence | `[]` | Gradually drift a `weighted_choice` field's value distribution over the phase (see [Distribution drift](#distribution-drift-ramps)) |
| `level_weight_ramp` | map | absent | Gradually drift the agent's `level_weights` (severity mix) over the phase (see [Distribution drift](#distribution-drift-ramps)) |

Phases run sequentially in order. **Past the last phase the agent STAYS on that last phase** — it
does *not* revert to its base configuration. The base config is the agent's behaviour *before* the
first phase, never after the last; a phase list is a one-way timeline whose final entry is the
terminal state. So an agent that must go quiet at the end declares that explicitly, as a trailing
zero-rate phase:

```yaml
    rate_per_second: 0                 # base — the behaviour BEFORE the first phase
    start_delay_seconds: 10s
    phases:
      - { name: run,  duration_seconds: 10s, rate_per_second: 4 }
      - { name: idle, duration_seconds: 40s, rate_per_second: 0 }   # terminal: silent to the end
```

Without the trailing `idle`, the agent keeps emitting at `run`'s rate for the rest of the scenario.

### Distribution drift (ramps)

A normal phase swaps behavior at its boundary (a *step*). A **ramp** instead *interpolates* a
distribution **gradually** across the phase, so the change emerges window by window — the way a
real system drifts (a slow error-rate creep, a backend slowly shifting its status-code mix). Both
ramp kinds reweight over a **FIXED support** (they never add or remove a value/level), advance in
**per-window quanta** (the weight vector is frozen within each `window_seconds` slice), and are
**fully deterministic** (a given seed replays bit-for-bit). The interpolation is linear:

```
w_i(n) = w_start_i + (w_end_i − w_start_i) · n / N
```

where `w_start` is the field/level's **base** distribution, `w_end` is the declared target, `n` is
the window index within the phase, and `N` is the phase span in windows. A **flat** ramp (target ==
base) is stationary — the clean control for a before/after experiment.

**`field_weight_ramps`** — drift a `weighted_choice` field's *value* distribution. Each entry ramps
one field toward `target_weights` (which must have the same length as the field's `values`):

```yaml
agents:
  - name: api-server
    fields:
      - name: status
        generator: weighted_choice
        values:  ["200", "500"]    # FIXED support
        weights: [1.0, 0.0]        # base (w_start) — all 200
    phases:
      - name: healthy
        duration_seconds: 5m
      - name: degrading
        duration_seconds: 10m
        field_weight_ramps:
          - field: status            # a weighted_choice field on this agent
            target_weights: [0.5, 0.5]   # w_end — drift toward a 50/50 mix
            window_seconds: 60           # quantum (default 60s)
```

**`level_weight_ramp`** — drift the agent's `level_weights` (the severity mix) toward a target over
the phase. `target_weights` reweights the **same level set** the agent declares in `level_weights`.
`level_weights` shapes the mix *within* the normal (`trace`/`debug`/`info`/`warn`) and error
(`error`/`fatal`) groups, so this drifts the within-group severity distribution (e.g. `info`→`warn`):

```yaml
agents:
  - name: worker
    level_weights: { info: 1.0, warn: 0.0 }   # base severity mix
    phases:
      - name: nominal
        duration_seconds: 5m
      - name: noisy
        duration_seconds: 10m
        level_weight_ramp:
          target_weights: { info: 0.2, warn: 0.8 }   # drift toward mostly-warn
          window_seconds: 60
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `field_weight_ramps[].field` | string | required | Name of a `weighted_choice` field on this agent |
| `field_weight_ramps[].target_weights` | sequence | required | Target weights (`w_end`); length must equal the field's `values` |
| `field_weight_ramps[].window_seconds` | number | `60.0` | Quantum the ramp advances in (align with the consuming window) |
| `level_weight_ramp.target_weights` | map | required | Target level mix; keys must match the agent's `level_weights` keys |
| `level_weight_ramp.window_seconds` | number | `60.0` | Quantum the ramp advances in |

---

## Latency

Latency can be set at agent level (`agents[].latency_ms`) or phase level
(`phases[].latency_ms`). Three forms are supported.

### Uniform (array)

```yaml
latency_ms: [10, 50]    # Uniform random between 10 ms and 50 ms
```

### Scalar (fixed)

```yaml
latency_ms: 25          # Always 25 ms (zero variance)
```

### Named distribution (map)

```yaml
# Normal (Gaussian)
latency_ms:
  distribution: normal
  mean: 50
  stddev: 15

# Percentile
latency_ms:
  distribution: percentile
  p50: 10
  p95: 80
  p99: 300

# Explicit uniform
latency_ms:
  distribution: uniform
  min: 10
  max: 100
```

| Key | Type | Applies to | Default |
|-----|------|-----------|---------|
| `distribution` | string | map form | `"uniform"` |
| `min` | number | uniform | `0.0` |
| `max` | number | uniform | `100.0` |
| `mean` | number | normal | `50.0` |
| `stddev` | number | normal | `10.0` |
| `p50` | number | percentile | `0.0` |
| `p95` | number | percentile | `0.0` |
| `p99` | number | percentile | `0.0` |

---

## Templates

Named presets that agents inherit via `use_template: template_name`. Agent values override
template defaults. Templates can include any agent-level key.

```yaml
templates:
  go_microservice:
    rate_per_second: 100
    error_rate: 0.008
    latency_ms:
      distribution: normal
      mean: 12
      stddev: 5
  high_traffic:
    rate_per_second: 1000
    error_rate: 0.01

agents:
  - name: user-service
    use_template: go_microservice      # Inherits rate, error_rate, latency_ms
    error_rate: 0.05          # Override: this takes precedence over template value
```

### Template Keys

| Key | Type | Description |
|-----|------|-------------|
| `rate_per_second` | string/number | Default rate |
| `error_rate` | number | Default error rate |
| `latency_ms` | distribution | Default latency |
| `fields` | sequence | Default field definitions |

---

## Causal Flows

Causal flows model distributed traces/workflows as deterministic, **instanced** state
machines. Each flow spawns new trace *instances* at `instance_rate_per_second`; an instance
walks the state graph from `start_state`, emitting one record per visited state **through the bound
agent (service)**, carrying a shared correlation id, until it reaches a state with no
outgoing transition. This is the only construct that imposes a declared *order* on the event
stream (rate-driven agents are unordered) — it is what gives a consumer a crisp causal /
transition graph (e.g. InSight's `dominant_path`).

Flows are **deterministic-world only** and are **rejected** under a real `scenario:` root — a flow is
unfolded from a materialized timeline, which only the deterministic engine builds, so the real world
declines the key with an error naming deterministic mode rather than accepting a declaration it cannot
honour. Declare them as a world key under `deterministic_scenario:` (below `time_axis:`, or below
`build_axis:` in the CI world). Branch selection and step content are seeded per-instance, so the same
scenario+seed replays bit-identically — adding a flow never shifts an agent's own content.

> **Agent-envelope inheritance (A1).** A flow step **inherits the bound agent's
> deterministic effective envelope** — its `error_rate` and `latency` at the step's
> emission sim-time — composed from the agent's `phases` and its **deterministic
> (offset-triggered) `incidents`** (`trigger: "time > Xs"`). So an incident that
> degrades the `payments` agent **does** degrade a step routed through it, for the
> incident's window — the canonical *"service X degrades → every trace through X
> degrades"* signal.
>
> **Precedence — explicit > inherited > default.** An **explicit** per-step `level` /
> `error_rate` **overrides** the inherited value (absent → inherit). The explicit value
> (including `error_rate: 0`) is the escape hatch back to isolation. A step's
> **structural identity is always its own** — `message_template` and `fields` are the
> step's; the `agent` is name/routing only for them. Its inter-step delay is still only
> the transition's `network_latency_ms` / `network_jitter_ms`.
>
> **Does NOT inherit (today).** The agent's **stochastic** dynamics — `health_state`,
> latency-threshold failure bursts, and **probability-triggered** incidents
> (`trigger_probability`) — and `rules` / `effects` / cascade have **no effect** on
> flow-step records. They are path-dependent on the agent's own RNG trajectory;
> inheriting them would cross the two seeded streams. Flow **topology** and `weights`
> likewise remain **static for the run**.
>
> **Determinism (the rule that makes inheritance safe).** The step reads only the
> agent's deterministic *parameter* `f(seed, T)` from immutable config — never the
> agent's live atomics — and draws its own outcome from the **flow instance's seeded
> stream** (`instance.rng`), never the agent's. The two streams never cross and the
> flow is **read-only** on the agent: adding a flow, or removing the incident it reads,
> never shifts the agent's own records (intervention-stable, the cube do-operator's
> minimal-intervention property).

```yaml
flows:
  - name: checkout
    instance_rate_per_second: 50     # new trace instances per second
    start_delay_seconds: 0           # when the flow begins spawning (duration format)
    max_concurrent: 200              # cap in-flight instances (0 = unbounded; drop new on full)
    correlation_field: trace_id      # field stamped on every step record of an instance
    start_state: receive              # initial state
    states:                          # map: state-name -> step (emits 1 record via `agent`)
      receive: { agent: nginx,    message_template: "GET /checkout" }
      auth:    { agent: auth,     message_template: "verify {user}" }
      charge:  { agent: payments, message_template: "charge {amount}" }
      done:    { agent: nginx,    message_template: "200 checkout" }
    transitions:                     # weighted edges; integer-ns inter-step delay
      - { from: receive, to: auth,   network_latency_ms: 2 }
      - { from: auth,    to: charge, weight: 0.98, network_latency_ms: 8 }
      - { from: auth,    to: done,   weight: 0.02 }   # rare off-path branch
      - { from: charge,  to: done,   network_latency_ms: 5 }
```

### Flow Keys

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `name` | string | required | Flow name; also the correlation-id prefix (`name-<n>`) |
| `instance_rate_per_second` | string/number | `1.0` | New trace instances spawned per second |
| `start_delay_seconds` | string/number | `0` | Delay before spawning starts (duration format or seconds) |
| `max_concurrent` | integer | `0` | Max in-flight instances; `0` = unbounded. On full, the new arrival is dropped |
| `max_steps` | integer | `10000` | Per-instance termination guard: an instance emits at most this many step records, then terminates. Must be ≥ 1 — it bounds a walk over a cyclic state graph so a flow always terminates |
| `correlation_field` | string | `"trace_id"` | Field stamped on every step record of an instance |
| `start_state` | string | required | Initial state name (must be a declared state) |
| `states` | map | required | State name → step spec |
| `transitions` | sequence | absent | Weighted directed edges between states |
| `branch_weight_ramps` | sequence | `[]` | Per-state step-function schedules of outgoing edge weights — author a branching-entropy shift / `BranchingShift` (see [Branch weight ramps](#branch-weight-ramps--authoring-a-branching-entropy-shift)) |

### Flow State Keys

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `agent` | string | required | Service the step logs through. Its **deterministic envelope (`error_rate` / `latency` from phases + deterministic incidents) is inherited** (A1); its `message_template` / `fields` and stochastic dynamics (`health_state`, bursts, `trigger_probability`, `effects`) are **not**. Must be a declared agent |
| `message_template` | string | `""` | Message with `{field}` placeholders (always the step's own — never inherited) |
| `log_level` | string | the agent's `log_level` | Per-step base log level; an explicit value **overrides** any inherited escalation. An unrecognized token is a **load failure**, never a silent demotion to `info` |
| `error_rate` | number | inherit | Per-step probability the record is escalated to `error`. Absent → **inherited** from the agent's effective envelope (A1); an explicit value (incl. `0`) **overrides** — the isolation escape hatch |
| `fields` | sequence | absent | Step-local field generators (same shape as agent `fields`) |
| `span_duration_ms` | distribution | absent | **Span-native (`otel_span` only).** The span's declared wall-duration, in **milliseconds**, as a [distribution](#latency) (`uniform` `[min,max]` / `normal` / `percentile`). Sampled once per span from the instance's position-stable RNG, rounded to integer ns → `endTimeUnixNano = start + duration`. Arrival-independent iid; **drawn LAST**, so it never perturbs any id/schedule draw — shifting a state's regime changes only that span's duration. Absent ⇒ a 0-ns span (`start == end`). Inert for every non-span format |
| `fan_out` | bool | `false` | **Span-native fan-out.** When `true`, reaching this state spawns **one concurrent child branch per outgoing transition** (instead of one weighted successor); each child span parents to this step's span, on its own span-id path + RNG seek, bounded by `max_steps`. This is the concurrent-branch primitive — an observed DAG, not a linear chain (see [Span output](#span-output-otel_span)) |

### Flow Transition Keys

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `from` | string | required | Source state (must be declared) |
| `to` | string | required | Target state (must be declared) |
| `weight` | number | `1.0` | Relative weight among a state's outgoing edges (normalized) |
| `network_latency_ms` | number | `0.0` | Inter-step delay before the target step |
| `network_jitter_ms` | number | `0.0` | Uniform ± jitter on the inter-step delay |

A state with no outgoing transition terminates the instance. A step is a **single-successor**
walk by default — outgoing edges are a *weighted choice*, so the causal path stays a clean
linear chain (one agent per state). To model **true concurrent fan-out** (a step spawning
several branches at once — the observed-DAG shape a distributed trace really has), set
`fan_out: true` on the state (see [Span output](#span-output-otel_span)); every outgoing edge
then becomes a concurrent child branch instead of a probabilistic choice.

### Span output (`otel_span`)

Point a flow at an `otel_span` output and each visited state emits a **flat OTLP JSON span**
(one span object per line) instead of a log line. A flow instance is a *trace*; each step is a
*span*; the parent is the spawning step's span. Two flow-state keys shape the span:
`span_duration_ms` (the span's wall-duration → `endTimeUnixNano - startTimeUnixNano`) and
`fan_out` (concurrent child branches, one per outgoing edge). `status.code` is `ERROR` iff the
step's effective `level` is `error`/`fatal`, else `UNSET`; `name` is the state name; the bound
agent's name rides `service.name`. Everything stays bit-identical across replays — span ids are
`splitmix64` over (flow identity, instance ordinal, branch, step), rendered to OTLP hex only at
the seam (no float in the id path).

```yaml
# deterministic-world only — author under a `deterministic_scenario:` root (a real `scenario:`
# rejects `flows:`); the world keys below nest under its `time_axis:`
outputs:
  - { name: spans, type: console, format: otel_span }

agents:
  - { name: svc, intent: service, rate_per_second: 0, log_level: info }   # flow-driven, silent

flows:
  - name: pipeline
    instance_rate_per_second: 8
    max_concurrent: 4                # >1 ⇒ concurrent traces interleave in the stream
    start_state: ingest
    states:
      ingest:      { agent: svc, message_template: "ingest", fan_out: true }   # → both children
      transform_a: { agent: svc, message_template: "transform_a",
                     span_duration_ms: { distribution: normal, mean: 20, stddev: 2 } }
      transform_b: { agent: svc, message_template: "transform_b" }
      sink_a:      { agent: svc, message_template: "sink_a" }
      sink_b:      { agent: svc, message_template: "sink_b" }
    transitions:                     # under fan_out these are BRANCHES, not weighted choices
      - { from: ingest,      to: transform_a }
      - { from: ingest,      to: transform_b }
      - { from: transform_a, to: sink_a }
      - { from: transform_b, to: sink_b }
```

> **Observed DAG vs inferred adjacency.** The parentage above (`parentSpanId`) is the *observed*
> causal DAG — `ingest→transform_a`, `ingest→transform_b`, and each transform to its sink, and
> nothing else. A consumer that instead infers edges from **sequential adjacency** in the emitted
> stream would manufacture edges the observed DAG never contains (sibling `transform_a→transform_b`,
> and — with `max_concurrent > 1` — cross-trace edges from the interleave). Span output makes that
> gap first-class: the worked green/red exhibits live in
> [`scenario/07_spans/`](scenario/07_spans/).

### Branch weight ramps — authoring a branching-entropy shift

`branch_weight_ramps` reshape a `from` state's **outgoing transition weights** over sim-time as a
**step-function** — the structural sibling of a phase's [`field_weight_ramps`](#distribution-drift-ramps).
Where a field ramp moves a field-value histogram (a *distributional* `FieldDrift` — the DISJOINT
authoring primitive), a branch ramp moves the **spread** of a state's successor distribution, which
shifts the metalog **branching entropy** of that state → an acute **`BranchingShift`** (the *structural*
instant voice, InSight §5.2). It is what lets a scenario co-fire a structural regression with a drift on
one template → a **branch-A Composite**.

At each declared `at_seconds` boundary the `from` state's outgoing edges take the step's `branch_weights`
(a `to`-state → weight map; an edge **absent** from the map takes weight `0`). Before the first
boundary the declared transition `weight`s apply. A sharp spread change — e.g. all-mass-on-one edge
(entropy 0) → uniform over *K* edges (entropy `log2 K`) — yields a per-window entropy jump ≈ `log2 K`;
to clear the sequence bank's default `branching_delta_threshold_bits` (~3.5) fan out to **≥ 12 edges**.

```yaml
flows:
  - name: worker
    start_state: process
    states:
      process:  { agent: api-svc, message_template: "request bucket {bucket} processed" }
      step_01:  { agent: api-svc, message_template: "worker step_01" }
      # … step_02 … step_16 (≥12 successors so the uniform spread ≥ 3.5 bits) …
    transitions:
      - { from: process, to: step_01, weight: 1.0 }   # base: all mass on one edge (entropy 0)
      - { from: process, to: step_02, weight: 0.0 }
      # … one edge per successor …
    branch_weight_ramps:
      - from: process                    # the state whose successor spread shifts
        schedule:                        # step-function of sim-time (ascending at_seconds)
          - at_seconds: 0                 # entropy 0 — all mass on step_01
            branch_weights: { step_01: 1.0 }
          - at_seconds: 1700s             # sharp jump to uniform over 16 → ~4 bits → BranchingShift
            branch_weights: { step_01: 1, step_02: 1, step_03: 1, step_04: 1, step_05: 1, step_06: 1,
                       step_07: 1, step_08: 1, step_09: 1, step_10: 1, step_11: 1, step_12: 1,
                       step_13: 1, step_14: 1, step_15: 1, step_16: 1 }
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `branch_weight_ramps[].from` | string | required | The state whose outgoing edges the schedule reshapes (must be a declared state) |
| `branch_weight_ramps[].schedule` | sequence | required | Ascending step-function; each entry `{ at_seconds, branch_weights }` |
| `branch_weight_ramps[].schedule[].at_seconds` | number/string | `0` | Sim-time boundary (duration format or seconds); active for `T ≥ at_seconds` |
| `branch_weight_ramps[].schedule[].branch_weights` | map | required | `to`-state → relative weight over `from`'s edges; an omitted edge takes weight `0`. Named `branch_weights`, not `weights`: a weighted_choice field's `weights:` is a **positional vector** parallel to `values:`, this is a **name→weight map** |

> **Determinism.** Boundaries are compared in **integer ns** (a pure step-function of `T` — `PlayToTarget(T)`
> freezes them, no wall-clock). The selection **draw is unchanged** — the existing per-instance `CounterRng`
> + `DiscreteDist` over the *reshaped* weight vector (LogCraft's certified strict-float regime; no new float
> path, symmetric to `field_weight_ramps`). Same scenario + seed replays bit-identically.

### Flow field weight ramps — a field drift on the flow spine

A flow-level `field_weight_ramps` drifts a **flow STATE's** `weighted_choice` field value-distribution over
sim-time — the continuous ([`field_weight_ramps`](#distribution-drift-ramps))-style sibling that lives on the
flow instead of an agent phase. Its purpose is co-location: a single flow can carry BOTH a `field_weight_ramp`
(a *distributional* drift → a DISJOINT `FieldDrift` on the flow's own template) AND a `branch_weight_ramp` (a
*structural* `BranchingShift` on the same template) — because a flow's records are trace-scoped, both signals
stay clean (no rate-agent self-succession diluting them). It interpolates base→`target_weights` over
`[start_seconds, start_seconds + duration_seconds]` in per-window quanta; before `start_seconds` the base
weights stand. FIXED support (reweights declared values only).

```yaml
flows:
  - name: walk
    start_state: process
    states:
      process: { agent: svc, message_template: "request bucket {bucket} processed",
                 fields: [ { name: bucket, generator: weighted_choice, values: ["10","90"], weights: [1.0, 0.0] } ] }
    field_weight_ramps:
      - state: process          # the flow state whose field drifts
        field: bucket           # a weighted_choice field on that state
        target_weights: [0.0, 1.0]
        start_seconds: 550s     # stationary before this (seeds a DISJOINT far block)
        duration_seconds: 1500s
        window_seconds: 25
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `field_weight_ramps[].state` | string | required | The flow state whose field drifts (must be a declared state) |
| `field_weight_ramps[].field` | string | required | A `weighted_choice` field on that state |
| `field_weight_ramps[].target_weights` | sequence | required | `w_end` over the field's fixed value support (length = the field's `values`) |
| `field_weight_ramps[].start_seconds` | number/string | `0` | Sim-time the ramp begins (base weights before it) |
| `field_weight_ramps[].duration_seconds` | number/string | `0` | Ramp span; interpolate over `[start, start+duration]` |
| `field_weight_ramps[].window_seconds` | number | `25` | Quantum the ramp advances in (align with the consuming InSight window) |

> **Determinism.** Integer-ns window quantum + contraction-off double interpolation + the existing per-instance
> draw — LogCraft's certified strict-float regime, symmetric to the agent `field_weight_ramps`.

---

## Interventional Axes

An **axis block is its own declaration plus its base** — and the base is either another axis or the
world itself, inline. Two interventional axes exist; both use the same edges, the same verbs and the
same fold, and differ only in what a coordinate MEANS:

| | `causal_axis` | `build_axis` |
|---|---|---|
| what it models | a family of counterfactuals — *what if X had not happened* | a CI history — build 1, build 2, … |
| its base | a nested `time_axis:` (the stream world) | the **CI world, inline** (no time axis) |
| coordinates | **NAMED** — the label is the meaning; `null` = the base | **ORDINAL** — the succession is the meaning; an edge `name:` is rejected |
| edges may be empty | no (with no edge it is the axis-less scenario — drop the block) | yes (the one-build history; the block still types the world) |

Deterministic world only — an axis under `scenario:` is a hard reject. Exactly one interventional
axis per file: nesting two (`causal_axis ⊃ build_axis` — do(…) on a declared history) is recognized
and refused.

```yaml
deterministic_scenario:
  name: my-causal-scenario
  seed: 2828
  outputs: [ ... ]                    # config stays at the root

  causal_axis:
    edges:
      - name: ablate-outage           # the edge NAME is the public axis coordinate
        remove: [ incidents.payments_outage ]
      - name: heal-notify
        upsert:
          - path: flows.settle.states.notify.error_rate
            value: 0.0
    time_axis:                        # the axis BASE — the ordinary deterministic world
      duration_seconds: 10
      agents: [ ... ]
      incidents: [ ... ]
      flows: [ ... ]
```

```yaml
deterministic_scenario:
  name: my-build-history
  seed: 4040
  outputs: [ ... ]

  build_axis:
    dialect: github                   # the axis's structural vocabulary, declared ONCE
    edges:                            # no names: coordinate 1 is "build 1"
      - upsert:                       # build 1 — do(inject failure into a step)
          - path: agents.step-lint.error_rate
            value: 0.9
    duration_seconds: 20              # the BUILD'S LENGTH — see "time in the CI world" below
    agents:                           # the CI world, inline — ordered by `after:`
      - name: job
        intent: { kind: job, payload: "build (ubuntu-latest)" }
      - name: step-install
        intent: { kind: step, payload: "yarn install" }
        after: job
      - name: step-lint                          # a CONTENT quantum: it has a body, so
        intent: { kind: step, payload: "yarn lint" }   # dynamics can bind to it
        after: step-install
        rate_per_second: 4
        message_template: "checked {file}"
        fields:
          - { name: file, generator: choice, values: ["app.ts", "index.ts", "util.ts"] }
```

Note which agent carries a body. `job` and `step-install` are **banners** — they emit their
banner and nothing else, and they would *refuse* a dynamics key. `step-lint` has a
`message_template:`, which makes it a **content quantum** — and that is precisely what makes
the edge above legal: `do(error_rate = 0.9)` needs something with content to fail. Injecting
failure into a banner is rejected at load, not silently ignored.

**Coordinates.** Coordinate `0` is the **base** — the world exactly as written. Edge *k* lands at
coordinate *k*: the world after applying edges 1..k **in order** (a fold — edge 2 operates on the
world edge 1 produced, not on the base). The engine never meets an axis: materializing a coordinate
yields a plain scenario, and a derived coordinate is **byte-equivalent to hand-authoring** the
transformed world (the fold edits the YAML world, then the ordinary parse runs). Loading a scenario
validates the WHOLE axis — every coordinate is parsed, not merely folded, so an edge that applies
cleanly but produces an illegal world fails on the declaration rather than on whoever asks for that
coordinate first.

**Edge keys:**

| Key | Type | Description |
|-----|------|-------------|
| `name` | string | `causal_axis`: required — the public coordinate (unique; `null` reserved for the base). `build_axis`: **rejected** — the coordinate is the position |
| `upsert` | sequence of `{path, value}` | create-or-**replace the whole node** at `path` |
| `remove` | sequence of paths | remove the element/key at `path` (must exist) |

An edge declares at least one operation. Within an edge, upserts apply before removes, in
declaration order. An edge may be compound (a real `do(X=x, Y=y)`); single-operation edges are the
causal-battery norm.

**Paths** are world-relative (resolved from the axis's base), dot-separated, and **name-keyed** in
named-object lists — `agents.gateway` is the agent *named* gateway, never an index (numeric segments
are rejected). Every path is validated: an unknown segment is a **hard reject** with the live roster
in the message, never a silent no-op edit.

- **Replacement granularity = path depth.** There are no merge semantics: `upsert` at a node
  (`agents.gateway`) replaces the whole object (the `name:` is injected from the path — a value
  whose `name:` differs is rejected as a smuggled rename); `upsert` at a leaf
  (`flows.settle.states.notify.error_rate`) is the one-knob tweak, sibling keys untouched.
- **`upsert` creates.** A missing element in a named list is appended (that is how a removed
  incident is *restored* by a later edge).
- **`remove` keeps the key.** Removing the last element of a list leaves the (empty) list in place,
  so a later edge can upsert back into it.

Exactly-K holds across an edge by construction: an agent's RNG stream is keyed by its identity
(never its index), so an edge that touches K moves exactly K — every unintervened agent's records
are bit-identical across adjacent coordinates.

### The CI world (`build_axis`)

The world under `build_axis:` is the CI world, and the agents **inherit** it — which is what makes
the keys below legal here and rejected elsewhere, and vice versa.

**The step chain (`after:`).** A CI document is ORDERED (the step sequence is semantics), so each
agent names its predecessor. The chain is strict — exactly one head (an agent following nothing), at
most one successor per agent, no cycle — i.e. a **total order**, and the agents are materialized *in*
it: the order they happen to be listed in carries nothing. A fork, a cycle, two heads, a self-loop or
an `after:` naming no live agent are all hard rejects.

The order is declared in the WORLD rather than performed by an edge for one reason: a world property
can be restated by hand, so a derived build is a world you could have written yourself. It has two
visible consequences, both matching what a real CI YAML diff shows:

- **adding a step re-parents its successor** — two upserts, the new step and the successor's `after:`;
- **removing a step must re-parent too** — leaving a dangling `after:` is a reject, not an automatic
  splice. An edge does exactly and only what it says.

**Time in the CI world.** There is no `time_axis` here (nesting one is a hard reject): CI steps do
not compare instant to instant, they compare per build increment. Time survives as a shared monotone
**sequence** — it keeps an origin (`start_time_unix_ns`), a format (`timezone`, rendered by the
[`timestamp`](#timestamp) generator) and a length (`duration_seconds`, the build's own duration), but
nothing compares along it.

> **`after:` orders the ROSTER, it does not sequence TIME — and a document consumer can tell.** An
> agent emits from its start until the scenario ends, so steps declared in a chain still *overlap*:
> every banner fires at t=0 and every later line falls inside the last quantum opened. That is
> invisible at cube grain (mass is summed, not segmented) and fatal at **intent grain** — the
> quantum-aligned diff (`diff_logs_aligned`) would compare one giant last-step quantum against
> another. A step that must own a *slot* declares it, with the terminal-phase rule above:
>
> ```yaml
>   - name: step-lint
>     after: step-install
>     rate_per_second: 0                 # silent before its slot
>     start_delay_seconds: 10            # the slot opens where step-install's closes
>     phases:
>       - { name: run,  duration_seconds: 10, rate_per_second: 4 }
>       - { name: idle, duration_seconds: 20, rate_per_second: 0 }   # …and closes here
> ```
>
> An edge intervening on such a step upserts the **phase's** knob
> (`agents.step-lint.phases.run.error_rate`), not the agent's: the phase overrides the agent for the
> slot's duration, so an agent-level upsert is shadowed and the edge silently does not bite.
> Worked example: `insight-playground/scenario/41_build_axis_intent_grain.yaml`. `incidents:` is therefore rejected as well: its `trigger: "time > …"`
addresses a coordinate that does not exist. A failing step is the agent's `error_rate` — which is
also exactly what an edge upserts to inject one.

### The bundled contract

A scenario carrying an axis may carry its detection contract in the same file under the
`contract_scenario:` root — named `positions:` (coordinate vectors: `causal_axis: <name|null>`, or
`build_axis: <k>`) and `transitions:` referencing them by name, compared at a declared `compare:`
locus. LogCraft ignores that root; the InSight contract harness reads it (see
`insight-playground/HOW_TO_READ.md`).

---

## Rules

Propagation rules cascade effects from one agent to another when a condition is met.
Condition expressions are evaluated by the engine; the loader passes them as strings.

```yaml
rules:
  - condition: "postgres-primary.error_rate > 0.05"
    propagate:
      to: order-service
      latency_multiplier: 3.0
  - condition: "order-service.error_rate > 0.1"
    propagate:
      to: api-gateway
      error_rate: 0.08
```

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `condition` | string | Yes | Condition expression (e.g. `"agent.metric > N"`) |
| `propagate.to` | string | Yes | Target agent name (validated post-parse) |
| `propagate.latency_multiplier` | number | No | Multiply target's latency |
| `propagate.error_rate` | number | No | Set target's error rate |

---

## Incidents

Time- or probability-triggered events that modify agent behavior for a duration.

```yaml
incidents:
  - name: database_overload
    trigger: "time > 5m"          # Fires once at the 5-minute mark
    duration_seconds: 2m
    effects:
      - target: postgres-primary
        latency_multiplier: 8.0
        error_rate: 0.25
      - target: order-service
        latency_multiplier: 3.0
        error_rate: 0.10

  - name: random_spike
    trigger_probability: 0.003    # 0.3% chance per second; overrides trigger:
    duration_seconds: 30s
    effects:
      - target: cache-service
        latency_multiplier: 5.0
```

### Incident Keys

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `name` | string | required | Incident label |
| `trigger` | string | `""` | Condition expression: `"time > Xm"` fires once at that time |
| `trigger_probability` | number | `0.0` | Per-second fire probability (0–1); when non-zero, overrides `trigger:` |
| `duration_seconds` | string/number | `0.0` | How long effects last (duration format or seconds); omit or `0` = permanent |
| `effects` | sequence | `[]` | Agent modifications while incident is active |

### Incident Effect Keys

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `target` | string | Yes | Agent name to affect (validated post-parse) |
| `latency_multiplier` | number | No | Multiply the agent's base latency |
| `error_rate` | number | No | Set the agent's error rate during the incident |

---

## Health State Machine

Probabilistic four-state machine: **Healthy (0)** → **Degraded (1)** → **Failing (2)**
→ **Recovering (3)** → **Healthy (0)**. Each state has its own latency multiplier and
error rate.

```yaml
agents:
  - name: order-service
    health_state:
      latency_multipliers: [1.0, 2.0, 5.0, 1.5]   # [Healthy, Degraded, Failing, Recovering]
      error_rates:         [0.0, 0.05, 0.30, 0.02]
      transitions:
        - from: 0           # Healthy
          to: 1             # Degraded
          probability: 0.005
        - from: 1           # Degraded
          to: 2             # Failing
          probability: 0.02
        - from: 2           # Failing
          to: 3             # Recovering
          probability: 0.10
        - from: 3           # Recovering
          to: 0             # Healthy
          probability: 0.15
```

### Health State Keys

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `latency_multipliers` | array of 4 | `[1.0, 2.0, 5.0, 1.5]` | Latency factor per state (Healthy, Degraded, Failing, Recovering) |
| `error_rates` | array of 4 | `[0.0, 0.05, 0.30, 0.02]` | Error rate per state |
| `transitions` | sequence | `[]` | State transition rules |

### Transition Keys

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `from` | integer | Yes | Source state index (0–3) |
| `to` | integer | Yes | Destination state index (0–3) |
| `probability` | number | Yes | Per-tick transition probability (0.0–1.0) |

**State index mapping:** 0 = Healthy, 1 = Degraded, 2 = Failing, 3 = Recovering.

---

## State & Effects

State variables track internal agent metrics (queue depth, connection count, etc.).
Effects change behavior when a variable crosses a threshold. Condition expressions are
engine-evaluated strings.

```yaml
agents:
  - name: order-service
    state:
      queue_depth:
        initial: 0
        max_value: 10000
        growth_per_request: 0.1
      cpu_load:
        initial: 0.2
        max_value: 1.0
        growth_per_request: 0.001
    effects:
      - condition: "queue_depth > 5000"
        latency_multiplier: 3.0
      - condition: "queue_depth > 8000"
        error_rate: 0.15
      - condition: "cpu_load > 0.9"
        latency_multiplier: 5.0
        error_rate: 0.10
```

### State Variable Config

State variables are declared as a map, where each key is the variable name:

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `initial` | number | `0.0` | Starting value |
| `max_value` | number | `1.0` | Upper bound (capped) |
| `growth_per_request` | number | `0.0` | Value increment per log event |

### Effect Keys

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `condition` | string | Yes | Condition expression (e.g. `"queue_depth > 5000"`) |
| `latency_multiplier` | number | No | Multiply latency when condition is true |
| `error_rate` | number | No | Override error rate when condition is true |

---

## Rate Modulation

Makes an agent's traffic vary over time. Two patterns are supported.

### Sinusoidal

Smooth periodic wave — useful for day/night cycles or repeating traffic patterns.

```yaml
rate_modulation:
  type: sinusoidal
  amplitude_factor: 0.5          # ±50% variation around the base rate
  period_seconds: 86400          # Full cycle = 24 hours
  phase_offset_seconds: 0        # Shift the wave start (positive = later peak)
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `type` | string | `"sinusoidal"` | Pattern selector |
| `amplitude_factor` | number | `0.5` | Peak deviation as fraction of base rate |
| `period_seconds` | number | `86400.0` | Cycle period in seconds |
| `phase_offset_seconds` | number | `0.0` | Phase shift in seconds |

Effective rate: `base × (1 + amplitude × sin(2π × (t + phase) / period))`

### Business Hours

Higher traffic during a configurable peak window, lower outside it.

```yaml
rate_modulation:
  type: business_hours
  peak_start_hour: 9             # Peak begins (inclusive)
  peak_end_hour: 18              # Peak ends (exclusive)
  peak_multiplier: 2.0           # Rate multiplier during peak
  off_peak_multiplier: 0.1       # Rate multiplier outside peak
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `type` | string | required | `"business_hours"` |
| `peak_multiplier` | number | `1.0` | Rate multiplier during peak window |
| `off_peak_multiplier` | number | `0.1` | Rate multiplier outside peak window |
| `peak_start_hour` | integer | `9` | Peak window start, inclusive (0–23, local hour) |
| `peak_end_hour` | integer | `18` | Peak window end, exclusive (0–23, local hour) |

Local hour calculation uses `time.timezone` and `time.offset_minutes`.

---

## Auto-Cascade

Automatically propagates error and latency effects from failing agents to their
dependents (declared via `dependencies:`), without explicit rules.

```yaml
auto_cascade:
  error_threshold: 0.10          # Cascade when error rate > 10%
  latency_threshold_ms: 0.0      # Also cascade on latency (0 = disabled)
  dampening_factor: 0.5          # Effect is halved at each hop
  blast_radius: 3                # Max hops from the failing agent (0 = unlimited)
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `error_threshold` | number | `0.1` | Effective error rate that triggers cascade (0.0–1.0) |
| `latency_threshold_ms` | number | `0.0` | Latency (ms) that also triggers; `0` = error-only |
| `dampening_factor` | number | `0.5` | Fraction of effect forwarded per hop (0.0–1.0) |
| `blast_radius` | integer | `3` | Max hops from source (0 = unlimited) |

---

## Noise

Simulates imperfections in your logging pipeline. Can be configured globally (applies
to all agents) or per-agent (overrides the global setting for that agent).

```yaml
noise:
  log_duplication_rate: 0.005    # 0.5% of logs are duplicated
  missing_fields_rate: 0.002     # 0.2% of logs have random fields stripped
  random_delay_ms: [0, 10]       # Per-record timing jitter
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `log_duplication_rate` | number | `0.0` | Per-log probability of emitting the same record twice. The duplicate is byte-identical (same timestamp and content, its own transport sequence index) and draws no RNG, so it is deterministic and works on the `seed:` replay path as well as live mode |
| `missing_fields_rate` | number | `0.0` | Per-field probability of omission (0.0–1.0) |
| `random_delay_ms` | [min, max] | `[0, 0]` | Uniform delay range added to each record |

---

## Users & Personas

Simulate session-based user traffic with behavioral profiles.

### Users

```yaml
users:
  count: 50000
  sessions:
    duration_seconds: [30s, 10m]   # a duration expression OR bare seconds
    requests_per_session: [3, 80]  # Requests per session range
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `count` | integer | `0` | Number of simulated users |
| `sessions.duration_seconds` | [min, max] | `[10.0, 300.0]` | Session length range. The value is **a duration expression (`30s`, `10m`) or a bare number of seconds** — the `_seconds` suffix names the bare-number unit, it does not forbid the expression form |
| `sessions.requests_per_session` | [min, max] | `[1, 50]` | Requests per session range |

### Personas

```yaml
personas:
  - name: power_user
    weight: 2.0
    behavior:
      request_rate: high
      endpoints: ["/api/checkout", "/api/search"]
  - name: casual_browser
    weight: 5.0
    behavior:
      request_rate: low
      endpoints: ["/api/products"]
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `name` | string | required | Persona label |
| `weight` | number | `1.0` | Relative selection weight (higher = more frequent) |
| `behavior.request_rate` | string | `"medium"` | `"high"` (×2.0), `"medium"` (×1.0), `"low"` (×0.5) |
| `behavior.endpoints` | sequence | `[]` | Endpoint strings this persona targets |

---

## Entity Pool

A fixed list of entity strings reused across agents to create realistic cross-agent
correlations (e.g. the same order ID appearing in gateway, service, and database logs).

```yaml
entity_pool:
  - "order-10001"
  - "order-10002"
  - "customer-201"
  - "session-abc123"
```

---

## Field Variations

Add random jitter to numeric fields via the top-level `field_variations`.

```yaml
field_variations:
  - field: latency_ms
    jitter_percent: 8.0      # ±8% random variation
  - field: response_bytes
    jitter_percent: 15.0
```

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `field` | string | Yes | Field name to apply jitter to |
| `jitter_percent` | number | No | Jitter amount as percentage (0–100) |

---

## Output Field Projection

Field selection and ordering is a **per-output** concern: each output declares an
optional `fields:` allowlist. Empty (the default) emits every field; when set, the
formatter projects each record onto exactly these fields, in this order. It is the
*which-fields* half of an output, orthogonal to `format` (the *how-to-serialize*
half) — so the InSight bus and a console can project differently.

```yaml
outputs:
  - name: insight
    type: insight_shm
    channel: calibration
    format: json
    project_fields:        # projection — only these fields reach this sink, in order
      - timestamp
      - level
      - service
      - trace_id
      - message
      - latency_ms
```

See [Output Options](#output-options) for the full per-output key table.

---

## System Archetypes

System archetypes model production-grade service behavior patterns. (Distributed call
chains with network latency are now modeled by [Causal Flows](#causal-flows).)

### Contention

Models connection pool exhaustion and request queuing.

```yaml
contention:
  max_connections: 200
  queue_latency_ms: [1, 50]    # Extra latency when a request must queue
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `max_connections` | integer | `0` | Max concurrent connections (`0` = unlimited) |
| `queue_latency_ms` | [min, max] | `[0, 0]` | Uniform queuing latency when pool is full |

---

### Slow Queries

Injects probabilistic slow operations.

```yaml
slow_queries:
  probability: 0.015           # 1.5% of requests are slow
  latency_ms: [500, 5000]     # Slow requests take 500 ms – 5 s
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `probability` | number | `0.0` | Per-request probability of slow query (0.0–1.0) |
| `latency_ms` | [min, max] | `[0, 0]` | Slow query latency range |

---

### Availability

Controls overall uptime and how failures manifest.

```yaml
availability:
  uptime: 0.985                # 98.5% uptime
  failure_mode: timeout        # "timeout" or "error"
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `uptime` | number | `1.0` | Uptime fraction (0.0–1.0) |
| `failure_mode` | string | `"timeout"` | `"timeout"` or `"error"` |

---

### Failures

Burst failure patterns triggered by threshold conditions.

```yaml
failures:
  mode: burst
  trigger: latency_threshold
  threshold_ms: 500
  duration_seconds: 30s
  error_rate: 0.20
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `mode` | string | `"burst"` | Failure pattern (`"burst"` is the only recognized value) |
| `trigger` | string | `""` | Trigger condition expression |
| `threshold_ms` | number | `0.0` | Latency threshold that activates the burst |
| `duration_seconds` | string/number | `0.0` | How long the burst lasts (duration format or seconds) |
| `error_rate` | number | `0.0` | Error rate injected during the failure |

---

## Registry

Maintain a library of reusable agent definitions in external YAML files. Agents are
referenced by name (and optionally version) with optional overrides.

```yaml
registry:
  nginx:
    v1: agents/nginx_v1.yaml
    v2: agents/nginx_v2.yaml
  auth: agents/auth.yaml

  agents:
    - ref: "nginx:v2"
      name: nginx-primary
      overrides:
        rate_per_second: 500
        error_rate: 0.01
        instances: 3
    - ref: auth
      name: auth-service
```

### Registry Keys

| Key | Type | Description |
|-----|------|-------------|
| `<agent_name>` | string | File path to agent YAML (simple form) |
| `<agent_name>` | map | Map of version → file path (versioned form) |
| `agents` | sequence | Agent instances to create from the registry |
| `agents[].ref` | string | Reference: `"name"` or `"name:version"` |
| `agents[].name` | string | Instance name in this scenario (defaults to `ref`) |
| `agents[].overrides` | map | Override any agent-level key |

Agent YAML files must contain an `agent:` top-level key.

---

## Includes

Merge other scenario YAML files before parsing. Useful for splitting large scenarios
across multiple files.

```yaml
includes:
  - ./shared_templates.yaml
  - ./incident_definitions.yaml
```

Paths are resolved relative to the including scenario file. Agents, templates,
incidents and rules are merged into the main config. Includes are
processed recursively.

---

## Replay

Replay a previously recorded log stream at configurable speed.

```yaml
replay:
  file: recordings/my_scenario.jsonl
  speed: 2.0    # 2× faster than recorded pace
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `file` | string | required | Path to recording file |
| `speed` | number | `1.0` | Playback speed multiplier (>1 = faster) |

Replay requires a `recording` output to have been used during the original run.

---

## Clock

In the **deterministic** world the clock lives **inside `time_axis:`** — there is no separate
`clock:` block and no `mode:` (the `deterministic_scenario:` root types the clock **virtual**; the
real world is always wall-clock). The `time_axis` clock keys:

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `duration_seconds` | string/number | `0` | The run horizon (`0` = run forever) |
| `start_time_unix_ns` | int64 | `0` | Unix epoch nanoseconds start; `0` = seed-derived |
| `epoch_duration_ns` | int/duration | `1s` | The epoch grid → `TimelineConfig::epoch_duration_ns` (the materialization/parallelism grain + window-seal cadence). Int ns or a duration (`1s`/`250ms`/`1us`); sub-second is supported (a de-risked pure materialization grain) |

The whole world (agents, incidents, flows, environment, noise, personas, users, entity_pool,
field_variations, timezone) nests under `time_axis` alongside these clock keys — see
[Scenario Root Keys](#scenario-root-keys).

---

## Pipeline

High-performance sharded pipeline. Rarely needed unless tuning throughput.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `num_shards` | integer | `0` | Number of pipeline shards; `0` = auto (≤ hardware concurrency) |
| `ring_capacity` | integer | `8192` | Ring buffer capacity per shard (round up to power of 2) |
| `low_watermark` | number | `0.5` | Low backpressure threshold fraction |
| `high_watermark` | number | `0.8` | High backpressure threshold fraction |
| `min_batch` | integer | `16` | Minimum batch size for emission |
| `max_batch` | integer | `256` | Maximum batch size for emission |
| `policy` | string | `"drop"` | `"drop"` (maximize throughput) or `"block"` (no loss). Deterministic mode requires `"block"` (auto-set). |

---

## Time Context

Timezone context for calendar-based logic (rate modulation business hours, timestamp
formatting).

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `timezone` | string | `"UTC"` | `"UTC"`, `"local"`, or IANA zone (e.g. `"America/New_York"`) |
| `offset_minutes` | integer | `0` | Fixed UTC offset in minutes (e.g. `330` = UTC+5:30) |

`"local"` is non-deterministic and is rejected in deterministic mode.

---

## Environment

Optional metadata embedded in every log record. All three keys are free-form strings.

```yaml
environment:
  region: us-east-1
  cluster: prod-ecommerce
  version: v3.2.1
```

Only `region`, `cluster`, and `version` are parsed. All appear in every output record.
