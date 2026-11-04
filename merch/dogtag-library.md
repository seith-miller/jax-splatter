# Dog tags — what Dildozer built, and what Jax can reuse

Handoff from the Dildozer dog tag work (2026-11-01 → 11-03, one Claude
session with Seith). The Dildozer logo tag was signed off and cataloged
(DLDZR-0037). Everything generic about it now lives in smart-part, so Jax's
dog tags (always a pair; round 1: long tags numbered 021–045, `round-1.md`) start from working
code, not from scratch.

## Where things are

| What | Where |
|---|---|
| **The generic library** — blanks, placing art on a tag, the printed laser rack, laser files, the spray-stencil look | smart-part [`scripts/dogtag/`](https://github.com/smartsquared/smart-part/tree/develop/scripts/dogtag) (its README is the manual) |
| The rack and its test piece, as parts | smart-part `components/dogtag-rack`, `dogtag-rack-test`; build book `components/dogtag/build.yml` |
| Dildozer's own: art, `design.yml`, laser files, BOM | dildozer [`merch/dogtag/`](https://github.com/seith-miller/dildozer/tree/develop/merch/dogtag) |
| The rack test piece, queued to print | shopfloor job `dogtag-rack-test-01` (any Berea printer, PLA, ~18 g) |
| The record | ledger `dildozer-dogtag` |

To make Jax tags, Jax gets its own `design.yml` beside its art (format in the
library's README) and runs `scripts/dogtag/make.py` on it. Jax keeps only what
is Jax's: art, design file, the laser files it generates.

## What carries straight over

- **The rack** — a 3D-printed plate (H2D, 320 × 310 mm) that carries 50 tags
  to the laser and holds each one exactly: a peg in the chain hole, a bump
  that sets the angle, a printed spring finger that pushes the tag onto both.
  An ORIGIN target to jog the laser to. 320 × 310 also fits Eastside's big
  laser (19.6 × 12.5 in bed). Print the 2-pocket test piece first.
- **Placement** — art is fitted by its own outline, centred between the hole
  and the far end, lifted 0.5 mm (optical centre), 3.5 mm clear of the edge.
  An anchor point (e.g. a star's centre) can be pinned to the centre line.
- **The spray-stencil look** — crisp shapes, a hair of edge wander, overspray
  dots the size of a laser spot; dialled per part (0 crisp → 2 rough), seeded
  so it repeats exactly, never touches the crisp art. Engraved as an image at
  254 dpi (one dot per line).
- **Print rules** for the rack, set by its geometry, good on any printer:
  0.4 mm nozzle or smaller, 0.2 mm layers, 2+ walls, flat, no supports.

## What Jax needs that isn't there yet

1. **Jax's blank.** Decided 2026-11-04: Jax uses the same DogTagBlanks BDT-01
   as Dildozer, so the rack and blank entry carry over. Colour still open (a
   pink coat would need checking against Splatter Pink).
2. **A number on every long tag (021–045).** The library engraves the same art
   on every tag, which suits the short tags as is. Numbering needs per-pocket text in the laser file, and a record
   of which number went in which pocket. Dildozer wanted the same for the
   second tag of its set ("unique text"), so build it once, in the library.
3. **Jax's look.** Jax's spray-paint / splat aesthetic may want its own
   spray `LOOK` values — they live in Jax's `design.yml`, not the library.

## Lessons that apply to Jax too

- **Check the material is allowed on the laser before the visit.** Berea's
  Nova 51 CO2 lists wood, glass, fabric, acrylic, paper (leather by
  approval) — no coated or anodized metal. Ask staff first. Berea's fiber
  laser (60 W MOPA, needs Lasers 102) is the metal tool, but its galvo field
  is small, so its rack would be 12–20 tags, not 50.
- **A CO2 laser doesn't mark bare metal;** it removes a coating (powder coat,
  paint, anodise) to the metal underneath. Anodized aluminium marks white.
- **Fit the blank to the real thing.** The BDT-01 outline was fitted to the
  seller's photo (±0.15 mm); measure a real tag before cutting a rack.
- **Files reach Berea's laser through the design computer** (Ethernet only);
  bring them by Drive/USB/email into LightBurn there.
- **Colour.** Jax's rule is `brand/reference/swatch/NOTES.md` (ΔE 5 to canon,
  ΔE 2 part-to-part). Dildozer's rule as Seith stated it (2026-11-01): a spec
  names a material within ΔE 5, the built part within ΔE 2 of the palette.
  They overlap but aren't the same — worth settling which one is universal.

## Open on the Dildozer side (not blocking Jax)

Print the rack test piece and try a real tag; Berea's OK for powder coat on
the Nova; engrave one test tag; the unique-text second tag of the set.
