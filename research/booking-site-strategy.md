# Booking-site strategy — deep research findings

Verified deep-research report (104 agents, 22 sources, 25 claims adversarially verified, 22 confirmed / 3 killed). Run 2026-06-12. This is the evidence base for the v0 design decisions in [docs/decisions.md](../docs/decisions.md).

## Headline

For a $150–250 local/event DJ, the strategy that the evidence supports: a **booking-first site that shows the price**, keeps the inquiry form minimal, proves activity with real photos and a show log, and hosts mixes on **Mixcloud** (not SoundCloud). Build it static on **Astro**, deploy to GitHub Pages via the official action.

## What the research established (confirmed claims)

### Pricing — show it (HIGH confidence)
- Budget mismatch and ghosting are the two dominant reasons event-DJ inquiries fail to convert.
- The Knot: **78% of couples say pricing is the #1 factor** in deciding which vendors to even contact.
- Vendors added price estimates to first replies *because* prospects stopped answering without numbers.
- Visible pricing pre-qualifies leads (WeddingPro reports ~25% higher response rates for storefronts showing rates).
- **→ Display the $150–250 range**, woven into the services/offer content with a one-line explanation of what drives the variance. (Don't use a standalone price list.)

### Inquiry form — keep it minimal (MEDIUM)
- Name, email, event date, location are enough to start. Each extra field measurably cuts conversion (~4.1%/field, HubSpot 2024; 3–5 fields is the sweet spot, Formstack 2025).
- Optionally one "event type" field. (Vote was 2-1: the dissent favored qualification fields like budget/guest count — a real tradeoff, but friction wins for a small operator.)

### Trust signals (MEDIUM)
- **Real event photos, never stock.** NN/g eye-tracking: users ignore generic stock people, engage with authentic photos as credibility content. Stock imagery actively reduces trust.
- Note: our brief forbids faces/recognizable AI artifacts — so "real photos" here means real *rooms, crowds-from-behind, the booth, the lights* — proof-of-work without faces.

### Event-type pages (MEDIUM)
- Per-event-type pages (wedding / corporate / birthday / private) help **local SEO** vs one generic services page — but 2026 sources warn thin per-type pages risk "doorway page" treatment.
- **→ For a one-pager-plus-archive, capture this with anchored sections**, not thin separate pages, until there's real distinct content per type.

### Mixes — Mixcloud, not SoundCloud (HIGH)
- **Mixcloud** is licensed/partnered with major rights holders; enforcement is identify→monetize-or-disable at the rights-holder's request, **no uploader strikes** (~83% of revenue to rights holders). Conditioned on Featured Artist Rules (~3 tracks/release, 4/artist/show), varies by territory, rights holders can still disable specific uploads. "Safer," not "risk-free."
- **SoundCloud** is hostile to mixes: official policy requires explicit permission from *every* rights holder; reinstating a takedown means proving permission for ALL tracks or the dispute is rejected; promo/non-commercial use is explicitly *not* fair use; content-ID removals + 3-strike termination.
- Both offer embeds; **Mixcloud's player has a dark mode** that fits the Blade Runner aesthetic.
- **→ Embed Mixcloud (dark) for recorded sets.**

### Stack — Astro or Eleventy, both verified for GH Pages (HIGH)
- **Astro:** official `withastro/action` (v6, active), recommended path; under a repo path set both `site` and `base: '/jax-splatter'` in config (skip `base` only for `<user>.github.io` repos or a custom domain serving from root).
- **Eleventy:** production-ready default build to `_site`, documented Pages workflow.
- No verified comparison of Hugo or plain HTML. **→ Chose Astro** for content collections (shows-as-data), build-time image optimization, and component reuse on an image-heavy site. See [docs/decisions.md](../docs/decisions.md).

## What the research did NOT settle (caveats + open questions)

- **Discovery (RQ4) is largely unanswered.** "Google is the top lead source" was **refuted** (1-2). No verified claims on Instagram, directories, or word-of-mouth for $150–250 DJs.
- **Schema markup value unverified.** No MusicEvent/LocalBusiness claim survived. We add modest, standard JSON-LD anyway (low cost, conventional) but should not assume SEO lift.
- **Wedding-market skew.** Most pricing evidence comes from wedding sources (higher budgets, The Knot has commercial interest in price display). Transfer to bars/birthdays at $150–250 is plausible but unproven.
- **Tracklist/setlist posting as *text*** — no verified claim on whether posting a text tracklist carries licensing exposure distinct from the recorded mix. Treated as low-risk (informational), but flagged.
- **Refuted, do not cite:** "81% of brides want prices" (0-3); "Google top lead source" (1-2); "Mixcloud … without takedown risk" (1-2, overreach).

## Key sources
- Pricing/UX: saradoesseo.com (2025 Wedding Pro Survey, 553 respondents), pros.weddingpro.com, byemilyjane.com, djsondemand.co.uk
- Licensing (primary): help.mixcloud.com, help.soundcloud.com
- Stack (primary): docs.astro.build/en/guides/deploy/github, 11ty.dev/docs/deployment
- Trust: nngroup.com/articles/photos-as-web-content
