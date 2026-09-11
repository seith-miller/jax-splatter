# Main rig case

**Concept:** The playback/VJ/DJ rig — the heart of the show that runs
track, video and DMX from the riser — lives permanently wired inside one
case: **drop it, plug in power, plug in outputs, go.** Same philosophy as
the stage boxes, applied to the brain of the set.
**Role in the set:** every show, first thing on the riser. DJ passages
between songs, track playback, video to the projector, DMX to the boxes /
T-bar / fog, wireless links to the roaming instruments (Mach, keytar,
chest rig pucks).
**Stage debut target:** debut (Phase 1) — the rig exists already; the case
is what makes it a one-minute setup.
**Tier:** $100–500 (custom build) — or $500+ if bought as a flight case.

## Spec (v0.2, Seith 2026-09-10 — modelled in smart-part as `rig-case`)

- **Form factor:** the 22 × 14 × 9 in overhead-bin case, ATA style (3/8 in
  laminated ply, aluminium tongue-and-groove extrusion, ball corners, butterfly
  latches), **split 50/50** into two 4.5 in trays.
- **Opening:** unlatch, flip the top tray over to the right onto the riser.
  Both trays are now open tubs side by side.
- **Half-hex bites:** each tray takes two half-hexagon bites out of its rim
  (280 mm wide at the rim, 60 deep, 60° sides), one in the join-end wall and
  one in the audience-side wall. Closed, the bites pair up into two full
  hexagonal openings (280 × 120) centred on the mating line; **two identical
  inserts** span both trays and fill them (front: controller jacks; end:
  the pass-through). Open, the end bites face each other and the front bites
  give access. Tray B is tray A's mirror.
- **Tray A (front):** the DDJ-FLX4 deck. Two 64 mm inline luggage wheels in
  printed housings at its X0 Z0 corners, so the closed case rolls on its end
  like a roller bag (pull point to decide: a grab handle on the end insert,
  or a strap).
- **Tray B (back):** the laptop stand folded, the Launchkey Mini, the small
  Yamaha mixer, the power/cable well. At the gig the stand goes up over B; the
  laptop travels separately (bag) and lands on the stand.
- **No raceway, no jack plate** in v0.2 (Seith): cable management is done by
  hand in the fit-out; the harness leaves over the rim or through the join.
- **No jack plate in v0.2** (Seith): the harness leaves over the rim or
  through the join when the case is open. A Neutrik D-series rear panel stays
  modelled in smart-part as a later option.
- **Lit like everything else:** DMX pucks in both trays (not modelled).

smart-part: `components/rig-case` (open) and `rig-case-closed` (transport)
place the same four parts (two trays, two hex inserts). Only the
case is modelled; internal gear, layout, foam and cable management are the
fit-out, done by hand later. Construction: aluminium angle frame per tray,
laser-cut ply skins, printed corner caps, routed drop-in walls, metal latches
and a spring surface-mount handle. Tracker: the Rig Case Build Book (smart-part
`components/rig-case/build.yml`).

## Draft BOM

| Part | Source | Est. | Actual | Have it? |
|---|---|---|---|---|
| Two ply trays + two hex inserts (3/8 in laminated ply, cut from the smart-part flat patterns) | shop | $90 | | |
| Hardware: butterfly latches ×4 (L905 surface), RH-0533 handle, rivets, M4 | Penn Elcom / Reliable | $85 | | |
| Inline luggage wheels 64 × 24 mm ×2 + M6 axles | Amazon | $14 | | |
| Foam, cable well and deck plate (fit-out) | shop | $50 | | |
| Power: inlet + strip + PD bricks per the shared standard | new | $60 | | |
| Cable set (short, permanent, internal) | new | $40 | | |
| DMX pucks ×2 (lighting) | self | $50 | | |

**Subtotal:** $389 · **+25%:** ~$97 · **Budget: ~$490**

## Open questions for Jax

- What is actually in the rig today (laptop, interface, controller,
  receivers)? The panel is designed off that list.
- Laptop in the case or on top? (heat, sightlines, theft)
- 19" rack rails inside, or a custom tray? Rack is heavier but standard.
- Buy a case and cut a panel, or build the shell? Buying is faster; building
  matches the boxes.
- Who operates it live (per debut-staging.md open decisions) changes the
  performance-surface layout.

## smart-part

The case is a smart-part product: panels as sheet parts, printed corners
and tray, and a connector panel whose cut-outs are driven by the connector
list above. Tracked in the smart-part backlog.

## Build log

- 2026-09-10 — concept + draft BOM, spec for review.
- 2026-09-10 — v0.2: two-tray split with removable end walls (Seith); modelled in smart-part (#227). No jack plate and no raceway in the first version. Half-hex bites at the rim pairing into two hexagonal openings; two identical inserts.
