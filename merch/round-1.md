# Merch round 1 — the plan

Drafted 2026-09-10; **the round was decided by Jax the same day** (see "The
round"). The first round of Jax Splatter merchandise, made mostly at the
Lexington Public Library makerspaces ([makerspace.md](makerspace.md)), sized
to be on a table at **DILDOZER, Oct 24** and restocked for **Louisville,
Nov 6**. Per D13, merch is the act's first revenue and it reinvests: this
round's net is earmarked for Phase 1 of the debut build (crew percussion
crate first).

## Ground rules for anything that goes to print

1. **A JAX-A### behind every print file.** The released marks (A002
   wordmark, A005 key art, A006 avatar) are the only source art. Each
   production file (sticker sheet, button face, HTV cut file, marking
   file…) becomes a candidate and gets signed before the machine runs —
   proposed IDs below.
2. **Neon by cut, photo by print.** Slime #39ff14 sits at 99% of sRGB's
   green chroma and Splatter Pink is near the edge — no CMYK, eco-solvent
   or dye-sub process can hit them; they print dull. The neons are
   achievable in **cut vinyl** (fluorescent HTV / adhesive stocks),
   **thread** (neon polyester), **acrylic** (fluorescent cast sheet),
   **anodized metal**, **filament** and **fluorescent plastisol** (screen
   print). So: the wordmark on garments is cut or screened, not CMYK; the
   key-art splat is printed and reads as photo-green, which is fine — it
   is a photo.
3. **Garment colorway per the swatch notes** as the starting point: blanks
   in Static Gray or Night; shirt-art ink Bone; the X always Splatter Pink.
   Light goods (can coolers, white stickers) use the sanctioned
   light-ground wordmark — Night letters, pink X. The tee design pass may
   revise the garment rule; it revises it in the registry, not on the press.
4. **No faces on merch.** Mark and key art only. The wordmark is never
   stacked, outlined or distressed; splatter lives around it.
5. **Rights gate on the splat.** A005/A006 are built on four keyed
   paintball photos whose source is not recorded in the repo. Confirm the
   licence before anything carrying the splat is *sold*. Fallback if it
   can't be cleared: regenerate the splat with `tools/splat-gen.py` (our
   own code) and sign a v2. Wordmark-only items are clean (Pathway Gothic
   One is SIL OFL).

## The round (Jax, 2026-09-10)

Stickers · buttons · magnets · dog tags · T-shirts · lighters · can coolers.

**Button standard (Jax, 2026-09-10): one size, 2.25".** It is the only size
both branches stock, it fits the A006 avatar and the full wordmark legibly,
and one face template (2.633" circle) serves buttons and magnets alike.

| Item | Make | COGS ea | Sell | Qty | Outlay | Gross at sell-through | Status |
|---|---|---|---|---|---|---|---|
| **Stickers** — wordmark kiss-cut 4×1.25", JAX splat die-cut 3", QR tile 2.5" | Marksbury Roland, sticker paper $2/ft | $0.06–0.13 | $2 · 3/$5 · free in every bag | ~150 | ~$14 | ~$85 (50 sold) | ready to file |
| **Buttons** — 2.25" only (the one size both branches have); avatar face | either branch, 2.25" button maker | ~$0.36 | $3 · 2/$5 | 50 | ~$18 | ~$125 | ready to file |
| **Magnets** — 2.25", same face, magnet back | either branch, 2.25" button maker | ~$0.41 | $4 | 30 | ~$13 | ~$120 | ready to file |
| **Dog tags** — colored anodized aluminum blanks (50×29×2 mm, ~100/pack with chains), laser-marked, numbered | either laser; test one tag first (painted vs anodized) | ~$0.30 | $8 | 30 | ~$25 (one pack) | ~$240 | blank candidate found (Jax, 2026-09-10); pink or black, not green |
| **T-shirt** — flagship; design pass first | library = prototype shop (Cricut HTV / stencil samples); production likely screen print | samples ~$7 · run ~$10 | $25 | 4 samples now; run of 24 after the design pass | ~$30 samples · ~$240 run | ~$100 samples · ~$600 run | **design open** (see below) |
| **Lighters** — Bic/Clipper with a permanent-vinyl wordmark decal | Cricut permanent vinyl, either branch | ~$1.00 | $3 | 50 | ~$50 | ~$150 | ready to file |
| **Can coolers** — light-ground wordmark + "Get Splattered!" on white neoprene | Marksbury sublimation + heat press; BYO blanks | ~$1.70 | $5 | 24 | ~$41 | ~$120 | ready to file |

| | Without the tee run | With a 24-tee screen run |
|---|---|---|
| Outlay | ~$195 | ~$435 |
| Gross at full sell-through | ~$945 | ~$1,445 |
| Break-even sell-through | ~21% | ~30% |

**Table kit, not merch (confirm):** 24×72" wordmark banner with URL + QR on
the Eastside HP (~$27) and a price card in the brand type. The table has to
look like the act.

**On hold:** beanies, hats and patches — wait for the embroidery machine
landing later in September (Jax, 2026-09-10). Marksbury already lists one;
the hold stands regardless.

**Out of round 1:** acrylic keychains (dog tags own that slot), key-art
print (needs print-res re-render + the rights gate), mugs, totes, key-art
printable-HTV tee, 3D-printed tags, kiln/CNC pieces. Bench for round 2.

Same trips, not for sale: **DMX puck enclosures ×2** (~70 g PLA, ~$10.50
each — gate 1 of [dmx-puck.md](dmx-puck.md)), **show flyers** for Oct 24 /
Nov 6 (11×17 on plain paper, ~$0.35 each), the mark engraved into the crew
percussion crate.

## The two open design threads

**The tee.** The flagship, not a line item: the surface people wear for
years and the one that carries the brand into rooms Jax isn't in. Great band
tees are an artwork with a name attached, not a logo alone. The library can
cut one or two flat neon colors (HTV) or cut the letters as a **stencil
mask** for fluorescent fabric spray — which is the wall-splat process
(`tools/wall-splat.py`) applied to a shirt: the blank is the wall, a pink
streak, the name as negative space, slime thrown over. Neither branch screen
prints; a production run of two-color fluorescent plastisol is the standard
route at ~$10/shirt. Plan: library = prototype shop (3–4 samples across
directions, worn at MULTIPASS Sep 19, photographed), then decide production.
Open: wordmark vs artwork front; blank (Static Gray vs black); cut (unisex vs
crop/tank — the scene buys both); back copy ("GET SPLATTERED!" / "NEON GLITCH
SLUT POP", both ratified lines). Next step once Jax answers "wordmark or
artwork": a tee pick sheet, 4–6 directions rendered on the blank.

**The dog tag.** In. The effect decides the process:

| Effect wanted | Process | Where |
|---|---|---|
| Military authenticity — stamped steel, the rattle | embossing machine (neither branch) or hand letter-punches at home (rough, punk) | home / supplier |
| Neon brand object — pink or slime tag, silver letters | laser-engraved anodized aluminum (dye removal) | either laser |
| Crew token — numbered stainless, cast wears theirs first | IR/fiber marking on bare steel; verify Marksbury's small laser has it (it sells metal keychain blanks) | Marksbury |

Whichever: 24" ball chain + 4" mini chain, pink or slime rubber silencer as
the neon accent, wordmark front, a subverted GI five-line back (name / number
/ GET SPLATTERED / NEON GLITCH SLUT POP / jaxsplatter.com).

## Proposed sign-off candidates

| Proposed ID | slug | what gets signed |
|---|---|---|
| JAX-A007 | sticker-set | the Roland print+cut sheet: three designs with bleed and CutContour |
| JAX-A008 | button-face | one 2.633" face circle for the 2.25" maker — buttons and magnets |
| JAX-A009 | tee | the design that wins the pass: art, placement, blank, ink/process |
| JAX-A010 | dog-tag | marking file, both faces, numbering scheme |
| JAX-A011 | lighter-decal | permanent-vinyl cut file, ~2.3×0.8" |
| JAX-A012 | can-cooler | light-ground sublimation wrap |
| JAX-A013 | table-banner | 24×72 layout with URL + QR (if confirmed) |

Rows land in the registry's Candidates table when the files exist; none
of them exist yet. The wordmark needs a vector export first (Pathway Gothic
One → outlined SVG from `brand/reference/wordmark/jax-wordmark.html`) —
that one file feeds the Cricut, the lasers, the Roland and the sublimation
wrap.

## Schedule against Oct 24

| Week | What | Where |
|---|---|---|
| Sep 14–18 | Sign the agreement; recon visit with the [first-visit checklist](makerspace.md#first-visit-checklist--questions-for-staff) — laser metal-marking and acrylic answers decide the dog-tag process. Order blanks: lighters, can coolers, dog-tag blanks + chains + silencers, tee samples, fluorescent HTV / fabric spray. Wordmark SVG + sticker/button/lighter/cooler files → candidates → Jax signs. Tee pick sheet → tee samples cut. Optional: Sep 15 button class (Eastside), Sep 17 Cricut class (Marksbury). | both |
| Sep 19 | MULTIPASS — wear the tee samples. Otherwise clear. | — |
| Sep 21–25 | Marksbury run: Roland stickers + button faces (reserve); buttons and magnets pressed same visit; can coolers sublimated; lighter decals cut; dog-tag marking test. Sep 26–27 weekend walk-in for overflow. | Marksbury |
| Sep 28–Oct 2 | Tee production decision from the sample reactions; screen-print order placed if that's the route (2–3 wk turnaround). Dog-tag run. Banner on the HP if confirmed (reserve). Oct 3–4 Eastside weekend for overflow. | Eastside / printer |
| Oct 5–9 | Fixes and second batch; flyers for Oct 24; puck enclosures. | either |
| Oct 12–16 | Buffer; screen-printed tees land. Oct 17–18 Eastside weekend if needed. | — |
| **Oct 24** | **DILDOZER — the merch table debuts.** | — |
| Oct 26–30 | Restock for Nov 6 Louisville from the sell-through numbers. | both |

## Selling it

- **At the table:** cash box seeded with ones and fives; Square Tap to Pay
  on the phone (no hardware, ~2.6% + a per-tap fee); Venmo / Cash App QR
  on the table sign. Prices on one card in the brand type.
- **Bundles:** any two small items $5; a sticker in every bag; tee + tag
  $30.
- **Online:** none in round 1. Bandcamp (accounts-inventory row 4, still
  unclaimed) is the round-2 unlock — it is the store and the only platform
  that pays directly.
- **Tax:** Kentucky charges 6% sales tax on tangible goods sold in person;
  registering with the Department of Revenue is a Jax task before Oct 24,
  not something this plan resolves.
- **Books:** `merch/inventory.md` gets created when the run is produced —
  counts in, counts out per show, cash in. Merch income posts to
  `band/instruments/BUDGET.md`'s running total as the reinvestment source.

## Open questions for Jax

- Tee: wordmark front, or an artwork the name rides on? (unlocks the tee
  pick sheet)
- Dog tag: which of the three effects?
- Table banner — confirm as table kit?
- Who clears the paintball-photo rights (ground rule 5)?

## Pick sheet

**Merch Round 1 Selects** — <https://claude.ai/code/artifact/faad70f9-526b-4f28-b3e4-d7f50a37a18e>
(artifact `faad70f9-526b-4f28-b3e4-d7f50a37a18e`). The round was picked in
chat 2026-09-10; the sheet is republished with those picks baked in and
stands as the record of the options considered.
