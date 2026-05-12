# LogCraft Scenario Reference

Complete, source-derived reference for every configuration key in a LogCraft scenario
file. Generated from direct source-code audit of `scenario_loader.cpp`, `config.hpp`,
`capability_keys.hpp`, and `field_generator.cpp`. This is the single source of truth;
`logcraft/technical_docs/reference/scenario_reference.md` redirects here.

All scenarios are defined in YAML under a top-level `scenario:` key.

```bash
logcraft my_scenario.yaml
```

---

## Capability Tiers

When running through the CodeRoast playground server, features are gated by tier.
The standalone CLI binary has full unrestricted access to all features except those
marked **CLI only** (which are only meaningful locally).

| Badge | Tier | Who can use it |
|-------|------|---------------|
| **[Anyone]** | Anyone | No login required |
| **[Free]** | Free | Logged-in free users |
| **[Pro]** | Pro | Pro subscription |
| **[Enterprise]** | Enterprise | Enterprise accounts |
| **[CLI only]** | — | Standalone binary only; server rejects for all tiers |

Permissions are additive: Pro includes all Free and Anyone capabilities, etc.

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
- [Latency](#latency)
- [Templates](#templates)
- [Interactions](#interactions)
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
- [Log Format](#log-format)
- [System Archetypes](#system-archetypes)
  - [Request Flow](#request-flow)
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
- [Tier Matrix](#tier-matrix)

---

## Scenario Root Keys

Every file starts with a `scenario:` block. Unrecognized top-level keys produce a
warning but do not fail parsing.

```yaml
scenario:
  name: "my-scenario"
  duration: 5m
  agents:
    - name: api-server
      rate: 100/s
```

| Key | Type | Default | Tier | Description |
|-----|------|---------|------|-------------|
| `name` | string | `"unnamed"` | **[Anyone]** | Human-readable scenario name |
| `duration` | string/number | `0` | **[Free]** | Auto-stop duration (`0` = run forever). See [Duration Format](#duration-format) |
| `duration_seconds` | number | `0.0` | **[Free]** | Legacy alias for `duration` in raw seconds; `duration` takes precedence |
| `seed` | uint64 | absent | **[Free]** | Sets deterministic mode. See [Engine Modes](#engine-modes) |
| `agents` | sequence | required | **[Anyone]** | One or more agent definitions |
| `outputs` | sequence | `[{type: console, format: json}]` | — | Output sink definitions |
| `environment` | map | absent | **[Free]** | Global metadata (region, cluster, version) |
| `noise` | map | absent | **[Pro]** | Global noise settings |
| `users` | map | absent | **[Pro]** | Simulated user pool |
| `personas` | sequence | absent | **[Pro]** | User behavior profiles |
| `entity_pool` | sequence | absent | **[Pro]** | Shared entity IDs for cross-agent correlation |
| `field_variations` | sequence | absent | **[Pro]** | Numeric field jitter config |
| `log_format` | map | absent | **[Free]** | Output field selection |
| `templates` | map | absent | **[Pro]** | Named reusable agent presets |
| `interactions` | sequence | absent | **[Pro]** | Cross-agent dependency declarations |
| `rules` | sequence | absent | **[Enterprise]** | Propagation rules |
| `incidents` | sequence | absent | **[Pro]** | Time- or probability-triggered events |
| `auto_cascade` | map | absent | **[Enterprise]** | Automatic error cascading |
| `registry` | map | absent | **[Enterprise]** | External agent file registry |
| `includes` | sequence | absent | **[CLI only]** | Merge other YAML files |
| `replay` | map | absent | **[CLI only]** | Replay a recorded session |
| `clock` | map | absent | — | Simulation clock config |
| `pipeline` | map | absent | — | Sharded pipeline config |
| `time` | map | absent | — | Timezone context |

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
rate: 200/s          # string form
rate_per_second: 200 # numeric fallback
```

When both are present, `rate` takes precedence.

---

## Engine Modes

| Mode | Selected by | Clock | Notes |
|------|-------------|-------|-------|
| **Real** | no `seed:` | `real` | Default. Randomized each run. |
| **Deterministic** | `seed:` present | `virtual` (required) | Same logs every run. Requires `pipeline.backpressure: block`. Rejects `time.timezone: local`. |

In deterministic mode, the loader auto-creates a `clock: {mode: virtual}` and sets
`pipeline.backpressure: block` when those blocks are absent, and emits a notice.

---

## Outputs

Define where and how logs are written. All outputs receive the same events simultaneously.

```yaml
outputs:
  - name: elastic          # Optional name (required for per-agent routing)
    type: http
    url: "http://localhost:9200/_bulk"
    format: ecs
    batch_size: 100
    flush_interval_ms: 1000

  - type: console          # CLI only
    format: json
```

### Output Types

| Value | Tier | Description |
|-------|------|-------------|
| `console` | **[CLI only]** | Print to stdout |
| `file` | **[CLI only]** | Write to disk with optional rotation |
| `recording` | **[CLI only]** | Write JSONL for later replay |
| `http` | **[Free]** | Batched HTTP POST (e.g. Elasticsearch, Loki, any webhook) |
| `prometheus` | **[Enterprise]** | Expose `/metrics` scrape endpoint |
| `statsd` | **[Enterprise]** | Push metrics over UDP |
| `insight_shm` | **[Enterprise]** | Shared-memory IPC channel for InSight integration |

### Output Formats

Every output except `prometheus` and `statsd` requires a `format:` (or `formats:`) field.

| Value | Alias | Tier | Description |
|-------|-------|------|-------------|
| `json` | — | **[Free]** | Structured JSON, newline-delimited |
| `text` | — | **[Free]** | Human-readable key=value |
| `clf` | — | **[Free]** | Apache/Nginx Combined Log Format |
| `apache_error` | — | **[Free]** | Apache error log |
| `log4j` | — | **[Free]** | Log4j / Python logging format |
| `syslog` | — | **[Free]** | BSD syslog (RFC 3164) |
| `rfc5424` | — | **[Free]** | IETF syslog (RFC 5424) |
| `nginx_error` | — | **[Free]** | Nginx error log |
| `kv` | `logfmt` | **[Free]** | Key=value / logfmt |
| `android_logcat` | — | **[Pro]** | Android logcat |
| `windows_cbs` | — | **[Pro]** | Windows CBS/CSI log |
| `spark_hdfs` | `spark` | **[Pro]** | Apache Spark / HDFS |
| `health_app` | — | **[Pro]** | Health app pipe-delimited |
| `proxifier` | — | **[Pro]** | Proxifier bracket format |
| `cloudwatch` | — | **[Pro]** | AWS CloudWatch JSON |
| `systemd_journal` | — | **[Pro]** | systemd journal JSON export |
| `hpc` | `bgl` | **[Pro]** | HPC / Blue Gene/L |
| `iis_w3c` | `iis` | **[Pro]** | IIS W3C Extended log |
| `ecs` | — | **[Enterprise]** | Elastic Common Schema 8.x |
| `otel` | `opentelemetry`, `otlp` | **[Enterprise]** | OpenTelemetry OTLP JSON |

When `formats:` (sequence) is set it overrides `format:` (single string), allowing one
sink to write multiple formats to the same path prefix.

### Output Options

All options are parsed per-sink and ignored when not applicable to the sink type.

| Key | Type | Default | Applies to | Description |
|-----|------|---------|-----------|-------------|
| `name` | string | `""` | all | Named outputs support per-agent routing |
| `type` | string | `"console"` | all | Sink type (see table above) |
| `format` | string | `"json"` | all | Single format (see table above) |
| `formats` | sequence | `[]` | all | Multi-format; overrides `format` when non-empty |
| `path` | string | `""` | `file`, `recording`, `prometheus` | Output file path or metric prefix |
| `max_size_bytes` | integer | `0` | `file` | Rotate when file exceeds this size (0 = no rotation) |
| `max_files` | integer | `5` | `file` | Number of rotated files to keep |
| `url` | string | `""` | `http` | Destination endpoint URL |
| `batch_size` | integer | `100` | `http` | Records per POST request |
| `flush_interval_ms` | integer | `1000` | `http` | Max ms before flushing a partial batch |
| `content_type` | string | `"application/json"` | `http` | Content-Type header |
| `headers` | map | `{}` | `http` | Extra HTTP request headers (string key-value pairs) |
| `host` | string | `"127.0.0.1"` | `statsd` | StatsD server address |
| `port` | integer | `8125` | `statsd` | StatsD server UDP port |
| `metrics_interval_seconds` | integer | `15` | `prometheus`, `statsd` | Metric snapshot frequency |
| `interval_seconds` | integer | `15` | `prometheus`, `statsd` | Alias for `metrics_interval_seconds` |
| `metrics_prefix` | string | `"logcraft"` | `prometheus`, `statsd` | Metric name prefix |
| `prefix` | string | `"logcraft"` | `prometheus`, `statsd` | Alias for `metrics_prefix` |
| `channel` | string | `"coderoast.default"` | `insight_shm` | Shared-memory channel base name |
| `slot_count` | integer | `8192` | `insight_shm` | Number of fixed-size slots per shard |
| `max_payload_bytes` | integer | `4096` | `insight_shm` | Max payload bytes per slot |
| `backpressure` | string | pipeline policy | `insight_shm` | `"block"` or `"drop"` (output-level override) |

---

## Agents

Agents are the log-producing services in your simulation. The `agents:` sequence is
required and must contain at least one entry.

```yaml
agents:
  - name: api-gateway             # Required
    type: web_server              # Free-form label (metadata only)
    rate: 100/s                   # Records per second
    error_rate: 0.03              # Probability of ERROR-level log (0.0–1.0)
    log_level: info               # Base log level
    instances: 3                  # Run N copies (names become api-gateway-1, -2, -3)
    start_after: 5s               # Delay before this agent starts
    use: my_template              # Inherit defaults from a template
    message_template: "{method} {path} -> {status_code}"
    fields: [...]
    phases: [...]
    latency_ms: [10, 50]
```

### Agent Keys

| Key | Type | Default | Tier | Description |
|-----|------|---------|------|-------------|
| `name` | string | required | **[Anyone]** | Unique identifier; expanded to `name-1`, `-2` when `instances > 1` |
| `type` | string | `""` | **[Anyone]** | Free-form label (e.g. `web_server`, `database`) |
| `rate` | string | — | **[Free]** | Records/s as `"200/s"` or numeric |
| `rate_per_second` | number | `1.0` | **[Free]** | Numeric fallback when `rate` absent |
| `log_level` | string | `"info"` | **[Anyone]** | Default severity: `trace`, `debug`, `info`, `warn`, `error`, `fatal` |
| `level_weights` | map | `{}` | **[Anyone]** | Explicit level distribution weights (auto-normalized) |
| `error_rate` | number | `0.0` | **[Free]** | Global ERROR probability (0.0–1.0) |
| `message_template` | string | `""` | **[Anyone]** | Message string with `{field_name}` placeholders |
| `use` | string | `""` | **[Pro]** | Template name to inherit from |
| `instances` | integer | `1` | **[Pro]** | Number of parallel copies |
| `start_after` | string/number | `0.0` | **[Free]** | Startup delay (duration format) |
| `fields` | sequence | `[]` | **[Free]** | Field definitions (see [Fields & Generators](#fields--generators)) |
| `phases` | sequence | `[]` | **[Free]** | Time-based behavior phases (see [Phases](#phases)) |
| `latency_ms` | distribution | absent | **[Free]** | Latency distribution (see [Latency](#latency)) |
| `dependencies` | sequence | `[]` | **[Pro]** | Upstream agent names (used by auto_cascade) |
| `health_state` | map | absent | **[Pro]** | Health state machine |
| `state` | map | `{}` | **[Pro]** | Internal state variables |
| `effects` | sequence | `[]` | **[Pro]** | Conditional behavior from state |
| `noise` | map | absent | **[Pro]** | Per-agent noise overrides |
| `rate_modulation` | map | absent | **[Pro]** | Time-varying rate changes |
| `slow_queries` | map | absent | **[Pro]** | Probabilistic slow operations |
| `availability` | map | absent | **[Pro]** | Uptime and failure mode |
| `failures` | map | absent | **[Pro]** | Burst failure patterns |
| `request_flow` | sequence | `[]` | **[Enterprise]** | Distributed call chain |
| `contention` | map | absent | **[Enterprise]** | Connection pool limits |
| `outputs` | sequence | `[]` | **[CLI only]** | Route to specific named outputs (empty = all) |

**Note:** Per-agent `outputs:` routing (`dsl.agent.output_routing`) is disabled on the
server for all tiers. All agents receive all sinks.

---

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

All field generators are available from **[Free]** except `normal`, `percentile`, and
`conditional` which require **[Pro]**.

---

### `weighted_choice`

**[Free]** — Pick from a list with specified weights.

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

**[Free]** — Pick uniformly at random from a list.

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

**[Free]** — Random number in a range.

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

**[Free]** — Auto-incrementing counter with optional prefix.

```yaml
- name: request_id
  generator: sequence
  prefix: "req-"
  start: 1000
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `prefix` | string | `""` | String prepended to the counter |
| `start` | uint64 | `1` | Starting counter value |

Generates: `"req-1000"`, `"req-1001"`, …

---

### `static`

**[Free]** — Always the same fixed value.

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

**[Free]** — Formatted date/time from simulation clock.

```yaml
- name: access_time
  generator: timestamp
  format: "%d/%b/%Y:%H:%M:%S %z"   # CLF timestamp
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `format` | string | `"%Y-%m-%dT%H:%M:%S"` | `strftime()` format string |

Timestamp uses simulation-clock time, not system time. In real mode the timezone
follows `time.timezone`; in deterministic mode it uses the configured offset.

---

### `normal`

**[Pro]** — Gaussian (bell-curve) distribution.

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

**[Pro]** — Piecewise distribution defined by percentile targets.

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

**[Pro]** — Different generator per value of a prior field.

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
    rate: 50/s
    phases:
      - name: warmup
        duration: 30s
        rate: 10/s
        latency_ms: [5, 20]
      - name: steady
        duration: 5m
        rate: 50/s
        latency_ms:
          distribution: normal
          mean: 25
          stddev: 8
      - name: peak
        duration: 1m
        rate: 150/s
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
| `duration` | string/number | — | Phase duration (duration format); `0` = run forever |
| `duration_seconds` | number | `0.0` | Numeric fallback for `duration` |
| `rate` | string | — | Override agent rate for this phase |
| `rate_per_second` | number | `0.0` | Numeric fallback for `rate` |
| `error_rate` | number | `0.0` | Override agent error rate for this phase (0.0–1.0) |
| `latency_ms` | distribution | absent | Override agent latency for this phase |

Phases run sequentially in order. When all phases complete, the agent continues at its
base configuration (or the scenario ends if `duration` has elapsed).

**Tier:** `dsl.agent.phases` — **[Free]**

---

## Latency

Latency can be set at agent level (`agents[].latency_ms`) or phase level
(`phases[].latency_ms`). Three forms are supported.

**Tier:** `dsl.agent.latency` — **[Free]**

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

Named presets that agents inherit via `use: template_name`. Agent values override
template defaults. Templates can include any agent-level key.

**Tier:** `dsl.scenario.templates` and `dsl.agent.use_template` — **[Pro]**

```yaml
templates:
  go_microservice:
    rate: 100/s
    error_rate: 0.008
    latency_ms:
      distribution: normal
      mean: 12
      stddev: 5
  high_traffic:
    rate: 1000/s
    error_rate: 0.01

agents:
  - name: user-service
    use: go_microservice      # Inherits rate, error_rate, latency_ms
    error_rate: 0.05          # Override: this takes precedence over template value
```

### Template Keys

| Key | Type | Description |
|-----|------|-------------|
| `rate` / `rate_per_second` | string/number | Default rate |
| `error_rate` | number | Default error rate |
| `latency_ms` | distribution | Default latency |
| `fields` | sequence | Default field definitions |

---

## Interactions

Declare the communication topology between agents. Used by auto-cascade and rules to
determine propagation paths. `type:` is metadata only — it does not affect engine
behavior.

**Tier:** `dsl.scenario.interactions` — **[Pro]**

```yaml
interactions:
  - from: api-gateway
    to: order-service
    type: request
  - from: order-service
    to: postgres-primary
    type: dependency
  - from: order-service
    to: redis-cache
    type: cache_lookup
```

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `from` | string | Yes | Calling agent name (validated post-parse) |
| `to` | string | Yes | Called agent name (validated post-parse) |
| `type` | string | No | Label: `request`, `dependency`, `query`, `cache_lookup`, etc. |

---

## Rules

Propagation rules cascade effects from one agent to another when a condition is met.
Condition expressions are evaluated by the engine; the loader passes them as strings.

**Tier:** `dsl.scenario.rules` — **[Enterprise]**

```yaml
rules:
  - when: "postgres-primary.error_rate > 0.05"
    propagate:
      to: order-service
      latency_multiplier: 3.0
  - when: "order-service.error_rate > 0.1"
    propagate:
      to: api-gateway
      error_rate: 0.08
```

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `when` | string | Yes | Condition expression (e.g. `"agent.metric > N"`) |
| `propagate.to` | string | Yes | Target agent name (validated post-parse) |
| `propagate.latency_multiplier` | number | No | Multiply target's latency |
| `propagate.error_rate` | number | No | Set target's error rate |

---

## Incidents

Time- or probability-triggered events that modify agent behavior for a duration.

**Tier:** `dsl.scenario.incidents` — **[Pro]**

```yaml
incidents:
  - name: database_overload
    trigger: "time > 5m"          # Fires once at the 5-minute mark
    duration: 2m
    effects:
      - target: postgres-primary
        latency_multiplier: 8.0
        error_rate: 0.25
      - target: order-service
        latency_multiplier: 3.0
        error_rate: 0.10

  - name: random_spike
    trigger_probability: 0.003    # 0.3% chance per second; overrides trigger:
    duration: 30s
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
| `duration` | string/number | — | How long effects last; omit or `0` = permanent |
| `duration_seconds` | number | `0.0` | Numeric fallback for `duration` |
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

**Tier:** `dsl.agent.health_state` — **[Pro]**

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

**Tier:** `dsl.agent.state_variables` and `dsl.agent.effects` — **[Pro]**

```yaml
agents:
  - name: order-service
    state:
      queue_depth:
        initial: 0
        max: 10000
        growth_per_request: 0.1
      cpu_load:
        initial: 0.2
        max: 1.0
        growth_per_request: 0.001
    effects:
      - when: "queue_depth > 5000"
        latency_multiplier: 3.0
      - when: "queue_depth > 8000"
        error_rate: 0.15
      - when: "cpu_load > 0.9"
        latency_multiplier: 5.0
        error_rate: 0.10
```

### State Variable Config

State variables are declared as a map, where each key is the variable name:

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `initial` | number | `0.0` | Starting value |
| `max` | number | `1.0` | Upper bound (capped) |
| `growth_per_request` | number | `0.0` | Value increment per log event |

### Effect Keys

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| `when` | string | Yes | Condition expression (e.g. `"queue_depth > 5000"`) |
| `latency_multiplier` | number | No | Multiply latency when condition is true |
| `error_rate` | number | No | Override error rate when condition is true |

---

## Rate Modulation

Makes an agent's traffic vary over time. Two patterns are supported.

**Tier:** `dsl.agent.rate_modulation` — **[Pro]**

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
dependents (declared via `interactions:` and `dependencies:`), without explicit rules.

**Tier:** `dsl.scenario.auto_cascade` — **[Enterprise]**

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

**Tier:** Global `dsl.scenario.noise` — **[Pro]**; per-agent `dsl.agent.noise` — **[Pro]**

```yaml
noise:
  log_duplication_rate: 0.005    # 0.5% of logs are duplicated
  missing_fields_rate: 0.002     # 0.2% of logs have random fields stripped
  random_delay_ms: [0, 10]       # Per-record timing jitter
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `log_duplication_rate` | number | `0.0` | Per-log probability of emitting twice (0.0–1.0) |
| `missing_fields_rate` | number | `0.0` | Per-field probability of omission (0.0–1.0) |
| `random_delay_ms` | [min, max] | `[0, 0]` | Uniform delay range added to each record |

---

## Users & Personas

Simulate session-based user traffic with behavioral profiles.

**Tier:** `dsl.scenario.users` and `dsl.scenario.personas` — **[Pro]**

### Users

```yaml
users:
  count: 50000
  sessions:
    duration: [30s, 10m]           # Session length range
    requests_per_session: [3, 80]  # Requests per session range
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `count` | integer | `0` | Number of simulated users |
| `sessions.duration` | [min, max] | `[10.0, 300.0]` | Session length range (duration format) |
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

**Tier:** `dsl.scenario.entity_pool` — **[Pro]**

```yaml
entity_pool:
  - "order-10001"
  - "order-10002"
  - "customer-201"
  - "session-abc123"
```

---

## Field Variations

Add random jitter to numeric fields globally or under `log_format.field_variation`.

**Tier:** `dsl.scenario.field_variations` — **[Pro]**

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

## Log Format

Define the output field ordering and selection. Also supports per-format field
variation under `field_variation`.

**Tier:** `dsl.scenario.log_format` — **[Free]**

```yaml
log_format:
  type: json
  fields:
    - timestamp
    - level
    - service
    - trace_id
    - span_id
    - message
    - latency_ms
```

| Key | Type | Description |
|-----|------|-------------|
| `type` | string | Format type (`json`) |
| `fields` | sequence | Ordered list of fields to include |
| `field_variation` | sequence | Per-format jitter (same structure as `field_variations`) |

---

## System Archetypes

System archetypes model production-grade service behavior patterns.

### Request Flow

**[Enterprise]** — Simulates distributed call chains with network latency and timeouts.

```yaml
agents:
  - name: api-gateway
    request_flow:
      - call: auth-service
        timeout_ms: 30
        network_latency_ms: 2.0
        network_jitter_ms: 0.5
      - call: product-service
        timeout_ms: 100
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `call` | string | required | Target agent name (validated post-parse) |
| `timeout_ms` | number | `0.0` | Request timeout; `0` = no timeout |
| `network_latency_ms` | number | `0.0` | One-way base propagation delay |
| `network_jitter_ms` | number | `0.0` | Uniform ±jitter on the base delay |

---

### Contention

**[Enterprise]** — Models connection pool exhaustion and request queuing.

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

**[Pro]** — Injects probabilistic slow operations.

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

**[Pro]** — Controls overall uptime and how failures manifest.

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

**[Pro]** — Burst failure patterns triggered by threshold conditions.

```yaml
failures:
  mode: burst
  trigger: latency_threshold
  threshold_ms: 500
  duration: 30s
  error_rate: 0.20
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `mode` | string | `"burst"` | Failure pattern (`"burst"` is the only recognized value) |
| `trigger` | string | `""` | Trigger condition expression |
| `threshold_ms` | number | `0.0` | Latency threshold that activates the burst |
| `duration` | string/number | — | How long the burst lasts |
| `duration_seconds` | number | `0.0` | Numeric fallback for `duration` |
| `error_rate` | number | `0.0` | Error rate injected during the failure |

---

## Registry

Maintain a library of reusable agent definitions in external YAML files. Agents are
referenced by name (and optionally version) with optional overrides.

**Tier:** `dsl.scenario.registry` — **[Enterprise]**

```yaml
registry:
  sources: [agents/]           # Directories to scan for agent YAML files
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
| `sources` | sequence | Directories to scan for `.yaml` agent files |
| `<agent_name>` | string | File path to agent YAML (simple form) |
| `<agent_name>` | map | Map of version → file path (versioned form) |
| `agents` | sequence | Agent instances to create from the registry |
| `agents[].ref` | string | Reference: `"name"` or `"name:version"` |
| `agents[].name` | string | Instance name in this scenario (defaults to `ref`) |
| `agents[].overrides` | map | Override any agent-level key |

Agent YAML files must contain an `agent:` top-level key.

---

## Includes

**[CLI only]** — Merge other scenario YAML files before parsing. Useful for splitting
large scenarios across multiple files.

```yaml
includes:
  - ./shared_templates.yaml
  - ./incident_definitions.yaml
```

Paths are resolved relative to the including scenario file. Agents, templates,
incidents, interactions, and rules are merged into the main config. Includes are
processed recursively.

---

## Replay

**[CLI only]** — Replay a previously recorded log stream at configurable speed.

```yaml
replay:
  file: recordings/my_scenario.jsonl
  speed: 2.0    # 2× faster than recorded pace
```

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `file` | string | required | Path to recording file |
| `speed` | number | `1.0` | Playback speed multiplier (>1 = faster) |

Replay requires a `recording` output to have been used during the original run. Replay
is not a third engine mode — it is configured separately.

---

## Clock

Controls time advancement. In most cases you do not need to set this explicitly; the
loader auto-configures it based on whether `seed:` is present.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `mode` | string | `"real"` / `"virtual"` | `"real"` (auto-advance) or `"virtual"` (manual stepping). Deterministic mode requires `"virtual"`; real mode forbids it. |
| `start_time_unix_ns` | int64 | `0` | Unix epoch nanoseconds; `0` = system time (real) or seed-derived (deterministic) |
| `tick_duration` | string/number | `"1ms"` | Step size used by `SimulationClock::step()` (e.g. `"1ms"`, `"10us"`) |

**Mode policy:**
- `seed:` present → `clock.mode: virtual` is required (auto-created if absent)
- `seed:` absent → `clock.mode: real` (default); `virtual` is rejected

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
| `backpressure` | string | `"drop"` | `"drop"` (maximize throughput) or `"block"` (no loss). Deterministic mode requires `"block"` (auto-set). |

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

**Tier:** `dsl.scenario.environment` — **[Free]**

```yaml
environment:
  region: us-east-1
  cluster: prod-ecommerce
  version: v3.2.1
```

Only `region`, `cluster`, and `version` are parsed. All appear in every output record.

---

## Tier Matrix

Summary of all DSL capabilities by minimum required tier.

### Anyone (no login required)

| Capability | Key |
|-----------|-----|
| Validate / list scenarios, load scenario | commands |
| Agent basic (`name`, `type`, `log_level`, `level_weights`, `message_template`) | `dsl.agent.basic` |
| Scenario `name` | `dsl.scenario.name` |

### Free (logged-in free users)

| Capability | Key |
|-----------|-----|
| Create / start / stop / destroy engine; WebSocket | commands |
| Play / pause / speed / advance (deterministic) | commands |
| Scenario `duration`, `seed`, `environment`, `log_format` | dsl.scenario.* |
| Agent `fields`, `phases`, `latency_ms`, `start_after` | dsl.agent.* |
| HTTP output | `dsl.output.http` |
| Field generators: `weighted_choice`, `choice`, `range`, `sequence`, `static`, `timestamp` | dsl.field.* |
| Formats: `json`, `text`, `clf`, `apache_error`, `log4j`, `syslog`, `rfc5424`, `nginx_error`, `kv`/`logfmt` | dsl.format.* |

### Pro

| Capability | Key |
|-----------|-----|
| Add / remove agents; set rate / error_rate; generate burst | commands |
| Scenario `noise`, `users`, `personas`, `entity_pool`, `field_variations`, `templates`, `interactions`, `incidents` | dsl.scenario.* |
| Agent `state_variables`, `effects`, `failures`, `dependencies`, `slow_queries`, `availability`, `noise`, `health_state`, `rate_modulation`, `instances`, `use` | dsl.agent.* |
| Field generators: `normal`, `percentile`, `conditional` | dsl.field.* |
| Formats: `android_logcat`, `windows_cbs`, `spark_hdfs`, `health_app`, `proxifier`, `cloudwatch`, `systemd_journal`, `hpc`/`bgl`, `iis_w3c`/`iis` | dsl.format.* |

### Enterprise

| Capability | Key |
|-----------|-----|
| Evaluate cascade | command |
| Scenario `registry`, `rules`, `auto_cascade` | dsl.scenario.* |
| Agent `request_flow`, `contention` | dsl.agent.* |
| Output sinks: `prometheus`, `statsd`, `insight_shm` | dsl.output.* |
| Formats: `ecs`, `otel`/`opentelemetry`/`otlp` | dsl.format.* |

### Disabled in server (CLI only)

| Feature | Key |
|---------|-----|
| Output type `console` | `dsl.output.console` |
| Output type `file` | `dsl.output.file` |
| Output type `recording` | `dsl.output.recording` |
| Scenario `includes` | `dsl.scenario.includes` |
| Scenario `replay` | `dsl.scenario.replay` |
| Per-agent output routing (`outputs:` on an agent) | `dsl.agent.output_routing` |

These are structurally valid YAML but the server returns HTTP 403 when they are used.
