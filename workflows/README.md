# workflows — how we build & gate

The other evidence folders show **results** — [`determinism/`](../determinism/) the goldens,
[`benchmarks/`](../benchmarks/) the numbers. This one shows **process**: the exact CI that produces
and gates them.

We do **not** paste scrubbed copies of our pipelines here. The workflows that matter are already
**public and anonymously reproducible** — so we link the single source instead. A scrubbed copy would
be a duplicate you'd have to *trust*; the real workflow is one you can read, fork, and run. That is the
same "not «trust us»" ethos as the rest of this Hub.

## The determinism gate — same input → same bytes, on every leg

Determinism is proven by a **5-leg** matrix — gcc and clang on **x86-64 *and* arm64**, plus an MSVC
anchor. Each leg rebuilds the engine from source and emits its digest; a compare job asserts all five
are byte-identical. There is **no committed golden to go stale** — the equality *is* the proof, and any
divergence fails the release.

- **[insight-canon · "Determinism Golden Proof"](https://github.com/CodeRoasted/insight-canon/blob/main/.github/workflows/golden.yaml)**
  — the foundation: tokenization + the integer/no-libm math core, proven bit-identical across all five
  legs. **Public + anonymous** — fork it and reproduce our digest yourself.
- **[insight-metalog · "Determinism Golden Proof"](https://github.com/CodeRoasted/insight-metalog/blob/main/.github/workflows/golden.yaml)**
  — the tower: each leg rebuilds canon + metalog from source and emits the serialized-MetaLog bit-identity
  digest. **Public + anonymous.**
- **[malf-toolchain · `coderoast-golden-compare`](https://github.com/CodeRoasted/malf-toolchain/blob/main/.github/actions/coderoast-golden-compare/action.yml)**
  — the cross-leg assertion the two proofs call: all legs byte-identical, or the release is blocked.

The eidos chain-apex determinism proof runs in the **private** detection repo — that engine is the moat.
But the public canon + metalog legs above let you verify the deterministic *foundation* the whole chain
rests on, from source, with no access to the closed core.

## The release gate — how a cut ships

Every release chains **Lint → CI → Determinism Golden (gate) → Release**, and the **benchmark gates the
release** — measured *before* the release is created, not attached after. The shape is mutualised as
public reusable workflows, so each engine's own workflow is a thin caller over the shared one:

- **[`coderoast-lint.yml`](https://github.com/CodeRoasted/malf-toolchain/blob/main/.github/workflows/coderoast-lint.yml)**
  · **[`coderoast-ci.yml`](https://github.com/CodeRoasted/malf-toolchain/blob/main/.github/workflows/coderoast-ci.yml)**
  · **[`coderoast-release.yml`](https://github.com/CodeRoasted/malf-toolchain/blob/main/.github/workflows/coderoast-release.yml)**
  — the reusable build / lint / release workflows in malf-toolchain.
- A real caller, end to end:
  **[insight-canon `ci.yml`](https://github.com/CodeRoasted/insight-canon/blob/main/.github/workflows/ci.yml)**
  + **[`release.yaml`](https://github.com/CodeRoasted/insight-canon/blob/main/.github/workflows/release.yaml)**
  — see how little a per-engine workflow has to say once the gates are shared.

## The rule — link, never copy

Two reasons, both load-bearing:

1. **Single source of truth.** A pasted copy drifts the instant the real workflow changes — and ours do
   (the whole tower was just refactored onto the shared workflows above). A rotting duplicate is exactly
   the kind of tech debt CodeRoast doesn't ship.
2. **Credibility.** The determinism gate is *public and anonymous* — you fork it and get our bytes. Evidence
   you can run beats a scrubbed artifact you'd have to believe.

The only workflows **not** linked here are the ones that run private engine code — the eidos detection
gates and the server pipeline. They are named, never shown: the line between what you can verify and what
stays closed is the same line drawn everywhere else in this Hub.
