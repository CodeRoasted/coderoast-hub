# LogCraft Playground

LogCraft generates synthetic log streams from a YAML scenario file. Describe your
services as agents, configure rates and formats, and get a continuous stream of
realistic log records — web server access logs, database traces, error events — to
send anywhere.

> **New to LogCraft?** Read [GUIDE.md](GUIDE.md) first — it explains scenarios,
> agents, fields, latency distributions (including what p50/p99 means), phases,
> and incidents with worked examples.

This folder is a **content-only package**: starter scenarios, a reusable agent
library, and the DSL documentation. It contains no source code — the `logcraft_core`
engine that runs these scenarios is distributed separately. All content here is
licensed [CC-BY-4.0](../LICENSE).

## Key Paths

| Path | Purpose |
|---|---|
| `GUIDE.md` | Getting started — concepts, examples, and onboarding for new users. |
| `scenario/01_starter/` | Starter scenarios, ordered by increasing complexity. |
| `scenario/agents/` | Reusable agent definitions (nginx, postgres, redis, kafka, …). |
| `scenario_reference.md` | Complete DSL reference — every key, type, and default. |
| `scenario.schema.json` | JSON Schema of the DSL for editors and CI — every closed key set, value token set and rule a JSON Schema can state. Hand-authored, and it LEADS: the engine complies, proving it in its own build. |
| `conformance/` | Every case an implementation must judge as stated (`cases.yaml`): each refuse case proves one rule beside a control that is accepted. |
| `conanfile.py` | Packages this directory as `logcraft_dsl`, the content-only DSL contract the engine's tests depend on. |

## License

All content in this folder — scenario and agent YAML, the DSL reference, and the
guide — is licensed under [CC-BY-4.0](../LICENSE).
