# Attribution for the rendered artifacts in this folder

Each `*.canon.txt` here is a **derived work**: the open (Apache-2.0) canon core run over a
sample corpus published at [coderoast-hub](https://github.com/CodeRoasted/coderoast-hub)
under `samples/`. Where the source corpus is third-party material under a redistribution
licence, that licence conditions this derivative too, and its notice is below.

The renders are **not** verbatim copies. Canon collapses each line to a template, emits one
event row per line, and computes an integer entropy term; the output is a new arrangement of
the source data, authored by CodeRoast. Line counts, ordering and content all differ from the
source logs. Treat every section below as *"Changes: yes — rendered through canon"*, whatever
the upstream declaration says about its own copy.

## `loghub.canon.txt` — derived from the `loghub` corpus

Source declaration, quoted verbatim from `loghub/samples/ATTRIBUTION.md` in the corpus this render
was produced from:

> # LogHub 2k samples — attribution (CC-BY-4.0)
> 
> These 16 `*_2k.log` files are the **LogHub** 2,000-line-per-system sample set,
> redistributed here under **CC-BY-4.0** as the committed smoke slice for the
> `loghub` corpus. LogHub's licence permits redistribution, so the real bytes may
> live in public git.
> 
> - **Source:** LogHub — Zenodo record `8196385` (https://doi.org/10.5281/zenodo.8196385).
> - **License:** Creative Commons Attribution 4.0 International (CC-BY-4.0).
> - **Changes:** none — verbatim 2k samples. The *full* LogHub corpus (e.g. `BGL.log`,
>   4.7 M lines) is **not** redistributed here; it comes from the Zenodo record above.
> 
> Cite: S. He, J. Zhu, P. He, M. R. Lyu, "Loghub: A Large Collection of System Log
> Datasets for AI-driven Log Analytics," ISSRE 2023.
> 
> > A derivative of these bytes owes its own notice. The canon renders under
> > [`showcase/canon/`](../../../showcase/canon/) are modified works, not copies, and carry
> > their own [`ATTRIBUTION.md`](../../../showcase/canon/ATTRIBUTION.md) stating the derivation.

**Derivation:** rendered by `insight-canon/scripts/samples_showcase.sh` using canon's
`det_proof`. Deterministic and reproducible from the published inputs above with the
published Apache-2.0 canon core; this script byte-compares two runs and refuses to
publish if they differ.

## `marker_corpus.canon.txt` — derived from the `marker_corpus` corpus

The source corpus is a **fabricated fixture** (`SLICE.json "synthetic": true`) with no
third-party bytes, so no third-party notice is owed. Read as of this run, not asserted.

## `revert_corpus.canon.txt` — derived from the `revert_corpus` corpus

The source corpus is a **fabricated fixture** (`SLICE.json "synthetic": true`) with no
third-party bytes, so no third-party notice is owed. Read as of this run, not asserted.
