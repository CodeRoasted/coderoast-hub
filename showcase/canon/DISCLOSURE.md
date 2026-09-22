# DISCLOSURE — this render publishes identifying content, by a recorded ruling

**These files are what an open log-analysis engine extracts from real operational logs.** The
inputs are a published academic corpus of production system logs; the output shows what the
engine made of them, including the parts that are identifying. Routable network addresses,
authentication records naming an account, home-directory paths naming a person and a small
number of mail addresses survive into this render — some of them into the *masked* half, which
is the point the render exists to make honestly. Nothing here was cleaned. If you are asking
*"is this known?"* — yes, it is known, it is bounded, and the boundary is checked mechanically
before these bytes leave.

**Ruling:** Founder, Emmanuel Prunet, 2026-08-21

**Ground:** the showcase keeps LogHub — a reproducible view of an already-declared tree earns its own entry rather than relaxing the byte-identity condition that authorised the source.

**Discharges:** ADR-33.D5 — the derived-artifact entry, a ruling that did not exist before this date and which no verdict about the source tree could have supplied.

## Why a derivation needs its own record

The source tree's disclosure **cannot** be carried here, and that is the design rather than an
inconvenience. A declaration is a claim about a **measurement**, and any transform moves the
measurement: the source fires six classes, this render fires four. Carried onto this render the
source's record would claim two exposures that are not here — and the gate refuses it, in that
direction, with a control that proves it.

The condition that authorises the source is **byte-identity** to the upstream Zenodo record.
This render is a new arrangement we authored, so that condition fails here, and it is **not**
relaxed. What replaces it is the property byte-identity exists to guarantee — that a reader who
does not trust us can verify what we shipped — restored by a different mechanism: **re-run the
tool.** The inputs are public, the engine core is Apache-2.0, the derivation is deterministic,
and `PINS.md` beside this file names every input actually read, in order, by digest.

Four conditions hold, all of them checked in the run that produced these bytes:

1. **The source holds a verdict of its own** — `loghub` DISCLOSED, `marker_corpus` CLEAR,
   `revert_corpus` CLEAR. The derived entry never launders a tree that had no verdict.
2. **The derivation is deterministic and reproducible from published inputs by a published
   tool**, and the producer proves it by rendering twice and comparing bytes.
3. **This artifact carries its own measured class set** — below — and the attribution its
   source licence requires (`ATTRIBUTION.md`, beside this file).
4. **No class fires here that does not fire on the source.** Four of the source's six. An
   operation that *introduced* a class would not be a view of the source; it would be a new
   exposure, covered by no ruling about the source, and it is refused as one.

## The accepted classes

Measured by `_shared/samples_safety_lint.py` in artifact mode over the rendered output on
**2026-08-21**. **5 916** line-hits over four classes, all of them in `loghub.canon.txt`:

```disclosed-classes
email 32
home-path 308
public-ipv4 3248
ssh-authlog 2328
```

The other rendered corpora — `marker_corpus.canon.txt` and `revert_corpus.canon.txt` — fired
**no declared class**. That is stated rather than left blank: a corpus that was measured clean
and a corpus that was never measured must not look the same.

The counts are a **record, not a threshold**. The gate compares the class *set* and prints the
recorded counts beside a fresh measurement on every run, so drift is visible without being
fatal.

## The boundary

* This record accepts **these four classes**, in **this render**, and nothing else. A class
  outside the set makes the artifact **REFUSED** again, immediately and without a further
  decision — and so does one of the four ceasing to fire, because a record read as current must
  be current.
* **It binds the class set of the ACT, not the per-file distribution.** A class moving between
  files inside one render is invisible to this record. Declared, so no one reads the pass as
  more than it is.
* **This record grants nothing on the redistribution right.** The right for these bytes is
  `ATTRIBUTION.md`, beside this file, and it is a separate axis. A derivative of a CC-BY work
  owes its notice whatever any content record says.
* It is a claim about **this artifact only**. Carried onto the source tree, or onto any other
  derivation, it is refused.
* **The gate is a floor, not a guarantee.** It matches declared byte-shapes, one line at a time.
  It cannot see a person's name, a free-text address, an identifier with no fixed shape, a value
  split across two lines, or anything inside a compressed member. Four classes fired — that is
  not the complete inventory of what is in these bytes.
