# Jax Splatter — accounts inventory & claim schedule

The roster of accounts the brand needs, in the order they should be claimed,
with the reason for each. **No secrets here** — credentials go in the keystore
(KeePass), same as [dildozer's](https://github.com/seith-miller/dildozer/blob/develop/docs/accounts-inventory.md).

Legend: ✅ claimed · ◐ in progress · ⬜ todo · ⏸ deferred

> **The name is `Jax Splatter`, handle `jaxsplatter` everywhere.** Decided
> 2026-08-22 after finding that "DJ Seith" is an established hip-hop DJ with
> the .com and every handle — see [the collision](#appendix-the-dj-seith-collision).

## Ordering principle

Claim by **how badly it hurts to lose**, not by convenience. A handle someone
else takes is gone permanently and there is no appeal. A domain is safe for a
few days. Anything that can be created later without losing the name goes last.

## Wave 1 — today (2026-08-22)

The irreversible ones. If a squatter takes one of these, the name is
compromised and we are back to picking a new one.

| # | Account | Handle | Why first | Status |
|---|---|---|---|---|
| 1 | **Porkbun domain** | `jaxsplatter.com` | The one address no platform owns. Everything else points here. | ✅ 2026-08-22 — $11.08/yr, auto-renew + lock + WHOIS privacy on, 2FA on the account. |
| 2 | **Email on the domain** | `accounts@` + `booking@` | Two free forwards, both to the personal gmail: `accounts@` for logins and resets, `booking@` public. Split so platform noise can't bury a booking, and so the public address can change without touching account recovery. | ✅ 2026-08-22 — delivery verified end-to-end. A sending mailbox ($3/mo) is still open; the free trial lapses 2026-09-06. |
| 3 | **Instagram** | `@jaxsplatter` | Scarcest handle, no recourse if squatted, and the channel the whole promo loop targets. | ✅ 2026-08-22 — **Creator** account, category shown, signed up with `accounts@`. |
| 4 | **Bandcamp** | `jaxsplatter.bandcamp.com` | The store, and the only platform that pays directly. Subdomain is permanent once set. | ⬜ |

## Wave 2 — this weekend (by Sun 2026-08-23)

Park the name. These don't need content yet; they need to be *held*.

| # | Account | Handle | Why | Status |
|---|---|---|---|---|
| 5 | **YouTube** | `@jaxsplatter` | Create as a **Brand Account** under the existing Google login — separate channel identity, no second Gmail, no phone verification, and it can take additional owners later. | ⬜ |
| 6 | **TikTok** | `@jaxsplatter` | Verified available. Short-form is where a set clip travels furthest. | ⬜ |
| 7 | **Twitch** | `jaxsplatter` | Livestreams. Interzone Undead already streams at `twitch.tv/interzone_live`, so this is the personal channel, not the event's. | ⬜ |
| 8 | **SoundCloud** | `jaxsplatter` | Originals and edits. | ⬜ |
| 9 | **Mixcloud** | `jaxsplatter` | Full recorded sets — blanket licensing, no uploader strikes (decisions.md D5). | ⬜ |
| 10 | **Bluesky** | `jaxsplatter.bsky.social` | Text mirror, least lock-in of anything on this list. Later: set the handle to `jaxsplatter.com` via DNS — free, and it verifies the domain. | ⬜ |
| 11 | **Facebook page** | `facebook.com/jaxsplatter` | **Promoted to Wave 1 in practice.** Low value on its own, but it is the prerequisite for Meta Business Suite — and Business Suite is the *only* way to post Stories and Reels from a desktop. The operator does not want Instagram on their phone, and the Death to Summer campaign is five Stories and a Reel. Without this, that campaign cannot run. Also the dependency for the publishing API and Postiz. | ⬜ **blocker** |

## Wave 3 — before Death to Summer (Fri 2026-08-28)

The event is the forcing deadline: the first time the new name goes in front of
an audience. Everything here is content, not claiming.

| # | Task | Why | Status |
|---|---|---|---|
| 12 | Same avatar + bio on every account | A hub pointing at profiles that look unrelated reads as broken. One image, one sentence, everywhere. | ⬜ |
| 13 | Bio copy written once, pasted everywhere | See [the identity question](#open-the-visual-identity-is-stale). | ⬜ |
| 14 | URLs pasted into `src/data/site.ts` | Rows appear as they're filled; `npm run build` reports what's missing. | ⬜ |
| 15 | Site rebranded + deployed | Wordmark, title, OG card, schema, repo README. | ⬜ |

## Wave 4 — when there's a release

Not claimable in advance; these are created *by* distribution.

| Account | How | Status |
|---|---|---|
| **DistroKid** | The distributor. One upload feeds Spotify, Apple, Tidal, Amazon, YouTube Music. Also handles cover mechanical licensing. | ⏸ |
| **Spotify** artist profile | Created by DistroKid on first release. Then claim **Spotify for Artists** for stats and control — there is no handle to reserve now. | ⏸ |
| Apple / Amazon / YT Music | Auto, via DistroKid. | ⏸ |

## Deferred — on purpose

| Account | Why not now |
|---|---|
| **Patreon** | Nothing to sell a subscription to yet. Bandcamp covers paid support at this stage. |
| **Discord** | A server with no members is worse than no server. Wait for an audience that wants one. |
| **Threads** | Comes automatically with the Instagram handle; nothing separate to claim. |
| **X / Twitter** | Optional text mirror. Claim it only to stop someone else having it. |
| **Gmail** | Blocked — the phone number has hit Google's verification cap, and the domain mailbox is better anyway. Only needed if something demands a Google login that a Brand Account can't cover. |

## Hygiene — do these as you go, not after

- **2FA on the domain registrar and the email first.** Those two are the master keys; every other account resets through them.
- **Credentials into the keystore** (KeePass), not the browser.
- **Keep this off the smartsquared.ai account.** The [seith-hq log](https://github.com/seith-miller/seith-hq) already records that boundary — work mail is smartsquared.ai, personal is the gmail. A Porkbun verification email sat unread in the work inbox for a month; that's what happens when the line blurs.
- **Same handle everywhere, no variants.** `jaxsplatter` or nothing. A qualified handle on one platform reads as an impersonator of yourself.

## Open: the visual identity is stale

[docs/brief.md](brief.md) and [CLAUDE.md](../CLAUDE.md) both record "Blade Runner —
black+blue mournful, black+red frenetic" as the standing identity. Per the
operator (2026-08-22) that was **specific to one fall-2025 show**, not the brand.

The actual artist: **high energy, slightly juvenile, slightly slutty — neon
glitch slut pop. Ghost in the Shell meets Aeon Flux.**

That's close to the opposite of what's currently in [theme.css](../src/styles/theme.css)
(cold electric blue on near-black, mournful default). The bio copy in Wave 3
and the site re-skin both depend on rewriting this first.

## Appendix: the DJ Seith collision

Why the name changed. Probed 2026-08-21; all confirmed live and **not ours**:

| Thing | What it is |
|---|---|
| `djseith.com` / `.net` | WordPress store, *"True Taxi In Gentle Rain by Ben FM & DJ Seith"* — cassettes, CDs, zines, mailing list. Registered 2022, expires 2027. |
| Instagram `@djseith` | *"DJ Seith \| Hip-hop DJ and Producer"* |
| Twitch `djseith` | *"An award-winning DJ, producer and vinyl collector… headnodding hip-hop."* |
| Bandcamp | 4+ albums, merch |
| Mixcloud, SoundCloud, YouTube, Facebook, Bluesky | All live under `djseith` |

An established act with four years, a catalogue, physical merch, and every
handle. Not winnable, and renaming was near-free at one archived flyer credit.
