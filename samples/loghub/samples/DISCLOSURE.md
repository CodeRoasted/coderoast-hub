# DISCLOSURE — this tree publishes identifying content, by a recorded ruling

**These are real operational logs.** They come from a published academic corpus of production
system logs, and they carry the identifying content such logs carry: routable network
addresses, authentication records naming an account, home-directory paths naming a person,
hardware addresses, and a small number of mail addresses. Nothing here was cleaned, and nothing
here is claimed to be clean. If you are asking *"is this known?"* — yes, it is known, it is
bounded, and the boundary is checked mechanically on every publication run.

**Ruling:** Founder, Emmanuel Prunet, 2026-08-21

**Ground:** the LogHub slice stays published — ruled 2026-08-18 and signed 2026-08-21; our copy is byte-identical to a record its authors deliberately made public, so it adds nothing to an exposure they chose.

**Discharges:** DN-39.D3 field 1 — the signature on this tree's disclosure, which only a human can give and which this gate can never mint for itself.

## The upstream publication of record

| | |
|---|---|
| **Publisher** | LogHub — S. He, J. Zhu, P. He, M. R. Lyu (ISSRE 2023) |
| **Stable identifier** | Zenodo record `8196385` — https://doi.org/10.5281/zenodo.8196385 |
| **Licence** | Creative Commons Attribution 4.0 International (CC-BY-4.0) |
| **Byte-identity** | The 16 `*_2k.log` files here are **verbatim** members of that record. No slicing, no transformation, no recombination. |

Byte-identity is the load-bearing condition, not a formality. It is what makes *"our copy adds
nothing to an exposure its authors chose"* **true** rather than merely comforting: a reader who
does not trust us can fetch the Zenodo record and compare. Break it — re-slice, transform,
recombine — and we become the publisher of a derived artifact, the identifier above stops
describing what we shipped, and every miss becomes ours. Which is also why these bytes are not
scrubbed: a scrub would destroy exactly the fact this publication rests on, and a heuristic
scrub is never a guarantee anyway.

## The accepted classes

Measured by `_shared/samples_safety_lint.py` over this tree on **2026-08-21**; the bytes
measured are those committed at `f9ea7e6` (2026-07-09) and unchanged since. **4 279** line-hits
over six classes:

```disclosed-classes
email 4
home-path 45
mac-addr 60
public-ipv4 3629
public-ipv6 20
ssh-authlog 521
```

The counts above are a **record, not a threshold**. The gate compares the class *set* and
prints the recorded counts beside a fresh measurement on every run, so drift is visible without
being fatal — a pinned count would be a golden that gets bumped without thought.

## The boundary

* This record accepts **these six classes**, in **this tree**, and nothing else. A class outside
  the set — a token, a key, a payment identifier, anything the gate learns to see later — makes
  this tree **REFUSED** again, immediately and without a further decision.
* It cuts the other way too. If one of the six stops firing, this record has become a claim
  about an exposure that is no longer here, and the tree is **REFUSED** until the record is
  re-measured and re-signed. A claim that is too strong is still a false claim, and a stale
  record is worse than none, because it is read as current.
* **This record grants nothing on the redistribution right.** It narrows a content refusal; it
  can never widen a licence one. A tree with no right to redistribute is refused with or
  without it. The right for these bytes is `ATTRIBUTION.md`, beside this file, and it is a
  separate axis.
* It is a claim about **this tree only**. A derived artifact — a render, a bundle, a re-slice —
  is a different measurement and needs its own record. Carrying this file onto one is refused
  by the gate, in both directions, and there is a control that proves it.
* **The gate is a floor, not a guarantee.** It matches declared byte-shapes, one line at a time.
  It cannot see a person's name, a free-text address, an identifier with no fixed shape, a value
  split across two lines, or anything inside a compressed member. The six classes above are what
  *fired* — they are not the complete inventory of what is in these logs.
