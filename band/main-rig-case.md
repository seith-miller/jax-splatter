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
- **Removable end walls:** the two 14 × 4.5 in end walls that face each other
  drop out (retained by the extrusion groove when latched), so the trays butt
  into **one 44 × 13 × 4 in channel**. A notch in each wall's floor edge lets
  the harness cross the join with the walls in.
- **Tray A (front):** the DDJ-FLX4 deck. A **removable front insert** (like the
  removable front on ProX controller cases) exposes the FLX4's headphone/mic
  jacks.
- **Tray B (back):** the laptop stand folded, the Launchkey Mini, the small
  Yamaha mixer, the power/cable well. At the gig the stand goes up over B; the
  laptop travels separately (bag) and lands on the stand.
- **Raceway:** a 45 mm trough along the back of both trays (glued ply divider,
  lift-out lid strip) for USB, master out, mixer tails and power; the panel
  opens into it.
- **No jack plate in v0.2** (Seith): the harness leaves over the rim or
  through the join when the case is open. A Neutrik D-series rear panel stays
  modelled in smart-part as a later option.
- **Lit like everything else:** DMX pucks in both trays (not modelled).

smart-part: `components/rig-case` (open) and `rig-case-closed` (transport)
place the same seven parts; the FLX4 is placed as an envelope body so the fit
is proven by the assembly interference check. Internal fit-out (foam, well,
deck plate, securing the gear) is deliberately not modelled yet.

## Draft BOM

| Part | Source | Est. | Actual | Have it? |
|---|---|---|---|---|
| Two ply trays + removable end walls + front insert (3/8 in laminated ply, cut from the smart-part flat patterns) | shop | $90 | | |
| ATA hardware: extrusion, ball corners, butterfly latches ×4, handles ×2 | Penn Elcom | $110 | | |
| Raceway strips, foam, cable well and deck plate (fit-out) | shop | $50 | | |
| Power: inlet + strip + PD bricks per the shared standard | new | $60 | | |
| Cable set (short, permanent, internal) | new | $40 | | |
| DMX pucks ×2 (lighting) | self | $50 | | |

**Subtotal:** $400 · **+25%:** ~$100 · **Budget: ~$500**

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
- 2026-09-10 — v0.2: two-tray split with removable end walls (Seith); modelled in smart-part (#227). No jack plate in the first version.
