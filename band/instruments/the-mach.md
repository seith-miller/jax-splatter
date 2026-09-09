# The Mach

**Concept:** An off-the-shelf HOTAS flight-sim controller (stick +
throttle) wired to a lit chest rig — a musician runs the stage flying the
**risers, laser beams, sweeps and drops** live with a joystick.
**Role in the set:** the purest expression of the instrument philosophy:
electronic music is full of gestures nobody can see. This makes them
visible — the audience watches the stick get yanked and hears the riser
climb. Visual/tactile anchor for the most synthetic sounds in the show.
**Named by Jax, 2026-09-09.**
**Stage debut target:** TBD.
**Tier:** $100–500.

## Spec (Jax, 2026-09-09)

- Off-the-shelf HOTAS (stick + throttle), chest-rig mounted, with lights.
- Drives riser/laser/FX parameters in the rig, live, while roaming.

## Draft BOM

| Part | Source | Est. | Actual | Have it? |
|---|---|---|---|---|
| HOTAS stick + throttle (used; T.Flight/X52-class) | used | $70 | | |
| Chest carrier (used) + mounting plate | used/shop | $120 | | |
| HID→MIDI bridge (Pi Zero 2 W-class, USB host, reads stick, sends wireless MIDI/OSC) | new | $40 | | |
| USB-C PD brick + trigger cable (shared standard) | new | $28 | | |
| DMX pucks ×2 on the rig | self | $50 | | |

**Subtotal:** $308 · **+25%:** ~$77 · **Budget: ~$385**

## Build notes

- Stick and throttle are separate units — mount them as two pods on the
  plate; each packs individually (carry-on rule).
- The bridge is the maker task: joystick HID in, MIDI/OSC out over the
  wireless link; map axes to FX macros in the rig. FX-tier latency is
  forgiving compared to note input.
- Every knob/hat on a HOTAS is a mappable performance control — start
  with 3 mappings max so the gestures stay legible.

## Build log

- 2026-09-09 — spec'd; draft BOM.
