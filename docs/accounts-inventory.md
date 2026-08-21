# DJ Seith accounts inventory

What exists, what's wired, what's outstanding. **No secrets here** — this file
only tracks *what exists*. Mirrors the format of
[dildozer/docs/accounts-inventory.md](https://github.com/seith-miller/dildozer/blob/develop/docs/accounts-inventory.md).

Legend: ✅ confirmed live · ⬜ not found · ❓ ownership unconfirmed

## ⚠️ Unresolved: whose accounts are these?

Probed 2026-08-21 after the operator said *"I don't think there are any
dj-seith accounts, I will need to make them."* **That turns out not to be
true — every major handle is taken and active under `djseith`.**

Two readings, and they lead to opposite strategies:

1. **They're yours** — dormant or forgotten. Then there is nothing to claim;
   the work is reactivating them and pointing them at one hub.
2. **They're a different DJ Seith** — someone who already owns the name across
   every platform *and* the .com. Then this is a naming collision, and the
   brand question comes before the website question.

Evidence pointing at reading 2: the bios describe a **hip-hop / funk / soul /
jazz vinyl DJ**, not the Blade Runner–electronic identity in
[docs/brief.md](brief.md). See "The positioning conflict" below.

**Do not fill these into `src/data/site.ts` until this is resolved.**
Linking the hub at another artist's profiles would be worse than linking nothing.

## Web

| Thing | Status | Notes |
|---|---|---|
| `djseith.com` | ❓ live | WordPress + Elementor store, *"True Taxi In Gentle Rain by Ben FM & DJ Seith"*. Cassettes, CDs, stickers, zines, art prints; mailing list; events page. Registrar **Launchpad**, DNS **HostGator**, created 2022-05-16, expires 2027-05-16. |
| `djseith.net` | ❓ live | Same site. Registrar **GoDaddy**, created 2024-12-31, expires 2027-12-31. |
| `djseith.org` / `.live` / `.club` / `.xyz` | ⬜ available | Fallbacks if the name is not ours. |

## Platforms

| Platform | Handle | Status | What the profile says |
|---|---|---|---|
| Instagram | `@djseith` | ❓ live | bio: *"DJ Seith \| Hip-hop DJ and Producer"* |
| Twitch | `djseith` | ❓ live | bio: *"An award-winning DJ, producer and vinyl collector… funky rhythms, soul fantasies, jazzy vibrations and headnodding hip-hop."* |
| Bandcamp | `djseith.bandcamp.com` | ❓ live | 4+ albums (Action Figures, Ekphrasis Edan, The Motor Mix, True Taxi In Gentle Rain) + merch |
| Mixcloud | `djseith` | ❓ live | titled "DJ Seith" |
| SoundCloud | `djseith` | ❓ live | titled "DJ Seith" |
| YouTube | `@djseith` | ❓ live | titled "DJSeith" |
| Facebook | `facebook.com/djseith` | ❓ live | linked from djseith.com |
| Bluesky | `djseith.bsky.social` | ❓ live | resolves to `did:plc:j7chmweyotjqm3pnhgnn3gzo` |
| **TikTok** | `@djseith` | ⬜ **available** | the one handle nobody holds |
| Spotify | — | ⬜ unchecked | needs a name search, not a handle probe |

## The positioning conflict

Even if the accounts are ours, the existing bios and this site describe
different artists:

| | Existing accounts | [docs/brief.md](brief.md) + this site |
|---|---|---|
| Genre | hip-hop, funk, soul, jazz | electronic, dark |
| Persona | award-winning DJ, producer, **vinyl collector** | Blade Runner — night, city, motion |
| Proof | a back catalogue + physical merch | one Al's Bar set, Sep 2025 |

A hub that points from one identity at profiles presenting the other reads as
a mistake to anyone who follows the link. Resolve the identity before wiring
the links.

## Open questions

- Are these accounts ours? Is the Launchpad/HostGator registrar login ours?
- Who is **Ben FM**, and does the existing store site stay up?
- Does this site replace `djseith.com`, or live beside it (hub vs. store)?
- The existing site has a **mailing list** — the owned, portable audience layer.
  Is it live, and who holds it?
- A month-old **Porkbun domain verification** email is unactioned in the
  smartsquared.ai inbox (seith-hq log, 2026-08-16). ICANN suspends after 15
  days. Unrelated domain, but same registrar account.
