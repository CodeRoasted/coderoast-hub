# DISCLOSURE — this render publishes identifying content, by a recorded ruling

**These files are what an open log-analysis engine extracts from real operational logs.** The
inputs are a published academic corpus of production system logs; the output shows what the
engine made of them, including the parts that are identifying. Authentication records naming an
account, home-directory paths naming a person, a small number of mail addresses and one
routable network address survive into this render — some of them into the *masked* half, which
is the point the render exists to make honestly. Nothing here was cleaned. If you are asking
*"is this known?"* — yes, it is known, it is bounded, and the boundary is checked mechanically
before these bytes leave. **Read the amendment of 2026-09-05 below before reading the
`public-ipv4` count**: that count is the detector's output, and on this render it is not a
count of addresses.

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

## Amendment — 2026-09-05: what the `public-ipv4` count is, and what it is not

The class set above is unchanged and every count still reproduces exactly. What this amendment
adds is the **subject** of one of them, which the record did not carry and which points in both
directions. It is written as an amendment rather than a silent edit because a signed disclosure
is a claim about a measurement, and correcting one is itself a measurement.

**① The 3 248 `public-ipv4` line-hits are NOT addresses — all 3 248 of them.** Re-measured
2026-09-05 with this gate's own predicate over the published bytes: **16 distinct matched
tokens, every one of them a Windows `6.1` servicing version**, and **every one of the 3 248
occurrences immediately preceded by `~` and followed by `,`** — the version field of a Windows
servicing package identifier, `Package_for_KBnnnnnnn~31bf3856ad364e35~amd64~~<four-part
version>,`. This is the predicate's **own declared false positive**, stated in its header: it
fires on a four-component version string and cannot tell one from an address. **Zero routable
fire this class in this render.** The error is in the SAFE direction — the record over-declared
what is here — and it is corrected because the product's claim is precision-first.

This is also the masker working, and it is worth reading that way: the SOURCE tree fires the
same class **3 629** times on **189 distinct tokens**, and there they are real — globally
routable unicast addresses spread across seven files, the largest of them appearing 867 times.
**None of them survives into this render.** They are not quoted here, for the reason the next
paragraph makes concrete.

**② And one routable address DOES survive, in a form this gate cannot see.** The render carries
a reverse-DNS hostname of the shape `dsl-Chn-static-<zero-padded IPv4>.touchtelindia.net` on
**188** lines. The name spells out a globally routable address — an Indian DSL allocation — while
the IP field on the same line was masked to `<*>`. `public-ipv4` does not fire on it: the quad is
embedded in a name, so the predicate's trailing boundary declines the candidate before any
address test runs. **Whether this class claims an address spelled inside a hostname is a claim
boundary and not a defect**, so it is disclosed here and left open rather than decided by a lint
change. It is named because a record that corrected only ① would be a half-truth in the
flattering direction.

**AND THIS RECORD IS SCANNED AS PART OF ITS OWN ARTIFACT — learned by tripping it, twice.** A
first draft of this amendment quoted three of the source tree's real addresses as examples and
the gate's next run reported `public-ipv4` at **3 252 against a recorded 3 248**; a second draft
still spelled two four-part version strings and reported **3 250**. The drift was the prose both
times, never the render. **A disclosure may describe a class but must never spell an instance of
it** — including an instance of the class's own false positive, which matches just as hard. Every
identifying shape in this file is therefore elided, and the counts in the block above are again a
claim about `loghub.canon.txt` alone.

**A repair that came out of the same pass, with no subject in these bytes:** `ipaddress` refuses
a zero-padded octet outright, so a padded quad **standing alone** would have been dropped by the
parser rather than by a judgement. The predicate now judges such a token on its decimal reading,
with controls in both directions. **No count above moved** — the padded occurrences here are the
hostname ones, which that arm does not reach.
