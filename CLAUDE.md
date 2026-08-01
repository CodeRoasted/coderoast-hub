# coderoast-hub — the public front door (content only, CC-BY-4.0)

Evidence, never engine: the machine-legible public claim surface for CodeRoast.
Scenarios, contracts, goldens, benchmarks, methodology — no runnable engine
code lives here or ever will.

## Arrival

- No build system. One Conan package exists: `insight_scenarios`
  (`insight-playground/`, content-only, never released — consumed as an
  editable by insight-eidos's `insight_e2e` and served read-only by
  `coderoast-server`).
- Layout: `logcraft-playground/` (THE LogCraft DSL reference + starter
  scenarios + agent library), `insight-playground/` (detection scenarios +
  declarative contracts), `determinism/` (per-engine reproducibility goldens +
  digests), `benchmarks/`, `showcase/sift/` (Sift over real CI logs),
  `workflows/` (pointers to the public CI).

## Constraints & traps

- PUBLIC repo: everything committed must be publishable as-is. No third-party
  corpus bytes, no secrets, nothing unscrubbed — private corpora live in
  `coderoast-corpora`.
- `determinism/` and `benchmarks/` artifacts are rendered and published INTO
  this repo by private CI at each release cut — the Hub only receives. Never
  hand-edit a golden or a measurement.
- A scenario/contract edit in `insight-playground/` lands in lockstep with the
  contract tests in the superproject checkout's `insight-eidos/insight-e2e/` — this folder is the single
  source of truth those gates read.
- The LogCraft DSL reference here is the one reference — the bible shelf points
  at it; never duplicate it elsewhere.
