# determinism — the reproducibility evidence

**Machine-checkable proof that the CodeRoast engines are deterministic** — the same
input yields a **bit-identical** result, and that result is **identical across
compilers, standard libraries, instruction-set architectures, and optimization
levels**. This folder holds the
committed *goldens* (the expected output) and their SHA-256 digests. Rebuild the
engines from source at this release and you get these exact digests back.

> Evidence snapshot for **v1.10.6**. Regenerated on every cut; the digests below move
> only when the deterministic output legitimately changes.

## The goldens

| file | sha256 | what it pins |
| --- | --- | --- |
| `canon.det_proof.txt` | `5e4fb383d61b7cad2be65f638fe67d302ada226a02b62c516e97905b86872beb` | canon public determinism proof — tokenization + event extraction over a fixed corpus |
| `metalog.determinism_golden.txt` | `83fda0029e3dc06e8435a4c6a25bf5b53ba3caa2ebed53d03f4833c5308e3873` | the serialized MetaLog document — the cross-toolchain bit-identity anchor |
| `eidos.parse_replay_golden.txt` | `3fe0ccf57f86707a68e2fcbf257ccf2f5b21d20fdeaacc725e6d6ad1cd6e46be` | eidos parse -> replay classification golden over the fuzz corpus |

Each `.sha256` is a `sha256sum`-compatible line, so a reader can verify a copy with:

```
sha256sum -c canon.det_proof.txt.sha256
```

## The claim, and why it holds

The serialized MetaLog document is **bit-identical** across **five independent build
legs** — GCC-16.2 / libstdc++ and Clang-21 / libc++ on **both x86-64 and arm64**, plus an
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
   `setup-gcc`, `setup-clang21-libcxx`, and — for the Windows anchor — MSVC 14.52.
2. Build the engines from source at this release, on **both an x86-64 and an arm64 host**
   (GCC and Clang on each; the MSVC anchor on Windows / x86-64).
3. Regenerate each engine's determinism proof and hash it.

You should get the digests in the table above, from **every leg**. That equality — across
five legs and two ISAs, not any single run — is the guarantee.

---
*Published under CC-BY-4.0. Evidence-only: this folder holds results and method, not a
runnable copy of the private engine.*
