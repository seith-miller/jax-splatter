# The playback rig

**The heart of the show is the VJ rig that already exists** — the one
built for the Interzone livestreams: OBS scene collection + midi-bridge
(Launchkey control, DMX out) + projector. For small shows, that is the
entire playback side: backing tracks, per-song video packages, and light
cues all run from it.

The rig's operational home stays with its tooling (midi-bridge repo, and
the deployed assets dir); event-specific scenes stay with events in
interzone. What lives here is the act-level view: what the rig is, and
what it needs to tour.

## The projector (owned)

**Epson EX3210** (V11H430020), 3LCD.

| | |
|---|---|
| Native resolution | **800 x 600 (SVGA), 4:3** |
| Brightness | 2800 lumens |
| Throw ratio | **1.45 – 1.96** (zoom) |
| Weight | **5.1 lb** (2.3 kg) |
| Inputs | VGA (D-sub 15), composite, S-video, USB display — **no HDMI** |
| Geometry correction | auto vertical keystone, manual horizontal slider; **no lens shift** |
| Mounting | M4 threaded inserts in the base (measure the pattern before buying a plate) |

**Throw distances** for the image widths we care about (multiply image width
by 1.45 for the closest the zoom allows, 1.96 for the furthest):

| Image width | Closest | Furthest |
|---|---|---|
| 100 in 16:9 screen (87 in wide) | 10.5 ft | 14.2 ft |
| 8 ft wide | 11.6 ft | 15.7 ft |
| 6 ft wide | 8.7 ft | 11.8 ft |

**Live with its limits, or replace it.** 800 x 600 across an 87 in width is
about 9 pixels per inch, and a 4:3 frame on a 16:9 screen wastes the top and
bottom. The Interzone runbook's verdict holds: bold type and high-contrast
line art survive, camera detail and feedback smear do not. 2800 lumens is
plenty in a dark room and marginal with house lights up. Every per-song video
package should be authored knowing this is the output device, or the act
should budget a 1080p replacement before the projector becomes the ceiling on
the visuals.

Also owned by Interzone and used at **Interzone XVII: MULTIPASS** (Al's Bar,
Sat 19 Sep 2026) — see `interzone/docs/rig.md`. One projector, two acts: check
the calendar before promising it to a Jax Splatter date.

## Venue-adaptation kit (open — venue-specific, spec as gigs demand)

| Need | Notes | Est. |
|---|---|---|
| Projector mounting | clamps / stand / truss adapter — varies per room. Beam-mount plan for the fixed rig: smart-part `docs/beam-rig/BRIEF.md` | TBD |
| Throw & surface realities | lens/distance per venue; scout sheet per gig | — |
| Power + cable kit | extensions, adapters, gaff | TBD |

Carry-on rule applies to whatever this kit becomes.
