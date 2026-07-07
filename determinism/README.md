# determinism — the reproducibility evidence

**Machine-checkable proof that the CodeRoast engines are deterministic** — the same
input yields a **bit-identical** result, and that result is **identical across
compilers, standard libraries, instruction-set architectures, and optimization
levels**. This folder holds the
committed *goldens* (the expected output) and their SHA-256 digests. Rebuild the
engines from source at this release and you get these exact digests back.

> Evidence snapshot for **v1.7.3**. Regenerated on every cut; the digests below move
> only when the deterministic output legitimately changes.

## The goldens

| file | sha256 | what it pins |
| --- | --- | --- |
| `canon.det_proof.txt` | `d34ffb49a43c1b0de5b765e275e4aa4a63d2ae2ea40f812130b21e2adf58c862` | canon public determinism proof — tokenization + event extraction over a fixed corpus |
| `metalog.determinism_golden.txt` | `74be64a3d65b3c8c6c0af17d0957c32ecb535ba97f1c7a0075244d29628fe6a6` | the serialized MetaLog document — the cross-toolchain bit-identity anchor |
| `eidos.parse_replay_golden.txt` | `02fb30d2baa5fa7db0e4324df0cf8c43d79c227e1744ab213b1f5987a16402cb` | eidos parse -> replay classification golden over the fuzz corpus |

Each `.sha256` is a `sha256sum`-compatible line, so a reader can verify a copy with:

```
sha256sum -c canon.det_proof.txt.sha256
```

## The claim, and why it holds

The serialized MetaLog document is **bit-identical** across **five independent build
legs** — GCC-15.3 / libstdc++ and Clang-21 / libc++ on **both x86-64 and arm64**, plus an
MSVC anchor on Windows: a cross-OS, cross-toolchain, **cross-ISA** result, verified on every
leg at each cut. Determinism is a first-class product constraint, engineered for, not hoped for:

- **No machine-divergent float in deterministic content.** Paths that feed the
  serialized output use integer / fixed-point arithmetic; `-ffp-contract=off` is
  compiled in, so `libm`, FMA contraction, and expression reassociation cannot make
  two machines disagree.
- **No wall-clock dependence** in the replay logic — replay is a pure function of the
  input and the declared window target.
- **Causal order is reconciled**, so per-window membership and the data-before-seal
  ordering are fixed for a fixed replay target, not timing-dependent.

This is gated on **every release cut**: the goldens above are regenerated from source
on each of the five legs and compared byte-for-byte. A divergence blocks the release.

## Reproduce it

1. Provision the pinned toolchains (public actions):
   `setup-gcc153`, `setup-clang21-libcxx`, and — for the Windows anchor — MSVC 14.52.
2. Build the engines from source at this release, on **both an x86-64 and an arm64 host**
   (GCC and Clang on each; the MSVC anchor on Windows / x86-64).
3. Regenerate each engine's determinism proof and hash it.

You should get the digests in the table above, from **every leg**. That equality — across
five legs and two ISAs, not any single run — is the guarantee.

---
*Published under CC-BY-4.0. Evidence-only: this folder holds results and method, not a
runnable copy of the private engine.*
