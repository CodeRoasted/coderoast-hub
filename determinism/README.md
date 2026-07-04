# determinism — the reproducibility evidence

**Machine-checkable proof that the CodeRoast engines are deterministic** — the same
input yields a **bit-identical** result, and that result is **identical across
compilers, standard libraries, and optimization levels**. This folder holds the
committed *goldens* (the expected output) and their SHA-256 digests. Rebuild the
engines from source at this release and you get these exact digests back.

> Evidence snapshot for **v1.7.1**. Regenerated on every cut; the digests below move
> only when the deterministic output legitimately changes.

## The goldens

| file | sha256 | what it pins |
| --- | --- | --- |
| `canon.det_proof.txt` | `d34ffb49a43c1b0de5b765e275e4aa4a63d2ae2ea40f812130b21e2adf58c862` | canon public determinism proof — tokenization + event extraction over a fixed corpus |
| `metalog.determinism_golden.txt` | `939745ff4772d68164f168a91486b4753560347b29b062a3bc9fee52e03858ec` | the serialized MetaLog document — the cross-toolchain bit-identity anchor |
| `eidos.parse_replay_golden.txt` | `b563215322813b8e60431c0ec1a827e4ced7bb4108c1a42b81e926384ea9f806` | eidos parse -> replay classification golden over the fuzz corpus |

Each `.sha256` is a `sha256sum`-compatible line, so a reader can verify a copy with:

```
sha256sum -c canon.det_proof.txt.sha256
```

## The claim, and why it holds

The serialized MetaLog document is **bit-identical** across the full cross-standard-library
diagonal — GCC-15.3 / libstdc++ **and** Clang-21 / libc++ — plus an MSVC anchor: a
cross-OS, cross-toolchain result, currently verified on all three toolchains. Determinism
is a first-class product constraint, engineered for, not hoped for:

- **No machine-divergent float in deterministic content.** Paths that feed the
  serialized output use integer / fixed-point arithmetic; `-ffp-contract=off` is
  compiled in, so `libm`, FMA contraction, and expression reassociation cannot make
  two machines disagree.
- **No wall-clock dependence** in the replay logic — replay is a pure function of the
  input and the declared window target.
- **Causal order is reconciled**, so per-window membership and the data-before-seal
  ordering are fixed for a fixed replay target, not timing-dependent.

This is gated on **every release cut**: the goldens above are regenerated from source
under each toolchain and compared byte-for-byte. A divergence blocks the release.

## Reproduce it

1. Provision the pinned toolchains (public actions):
   `setup-gcc153`, `setup-clang21-libcxx`, and — for the Windows anchor — MSVC 14.52.
2. Build the engines from source at this release.
3. Regenerate each engine's determinism proof and hash it.

You should get the digests in the table above, from every toolchain. That equality —
not any single run — is the guarantee.

---
*Published under CC-BY-4.0. Evidence-only: this folder holds results and method, not a
runnable copy of the private engine.*
