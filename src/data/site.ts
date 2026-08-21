// Single source of truth for site-wide content and config.
// Editing this file is how the operator tunes the site without touching markup.

export type LinkStatus = 'live' | 'planned';

export interface PlatformLink {
  /** stable key — also the CSS hook for the row's icon */
  key: string;
  /** row label, rendered uppercase */
  label: string;
  /** what shows on the right of the row: @handle, a domain, whatever reads best */
  handle: string;
  /** full URL. EMPTY STRING = not claimed yet; the row does not render. */
  url: string;
  /** one-word category, shown only on wide screens */
  kind: string;
  status: LinkStatus;
}

export const site = {
  name: 'DJ SEITH',
  tagline: 'Music producer & live performer',
  // One-line positioning shown in the hero. Keep it short and uppercase-friendly.
  heroStatement: 'Late-night sets for rooms that want to feel something.',

  // ── ACTION NEEDED BEFORE LAUNCH ──────────────────────────────────────────
  // Placeholder. v0 does not publish a personal address without ratification.
  booking: {
    email: 'bookings@djseith.example', // ← set a real booking inbox
  },
  // ─────────────────────────────────────────────────────────────────────────

  // ══ THE LINK HUB ═════════════════════════════════════════════════════════
  // The spine of the page (decisions.md D9). This site is the ONE address that
  // is not owned by a platform; every account points here, and this points out.
  //
  // TO ADD A LINK: paste the URL into `url`. The row appears. That's the whole
  // workflow — no markup to touch.
  // TO ADD A PLATFORM: copy any row, change key/label/kind. Order here IS the
  // order on the page.
  //
  // `status: 'planned'` rows are the roster of accounts not yet claimed. They
  // never render; they exist so the list of what's outstanding lives in one
  // place. Flip to 'live' when the URL goes in.
  links: [
    { key: 'instagram',  label: 'Instagram',  handle: '', url: '', kind: 'Daily',    status: 'planned' },
    { key: 'mixcloud',   label: 'Mixcloud',   handle: '', url: '', kind: 'Sets',     status: 'planned' },
    { key: 'youtube',    label: 'YouTube',    handle: '', url: '', kind: 'Video',    status: 'planned' },
    { key: 'twitch',     label: 'Twitch',     handle: '', url: '', kind: 'Live',     status: 'planned' },
    { key: 'soundcloud', label: 'SoundCloud', handle: '', url: '', kind: 'Tracks',   status: 'planned' },
    { key: 'bandcamp',   label: 'Bandcamp',   handle: '', url: '', kind: 'Buy',      status: 'planned' },
    { key: 'spotify',    label: 'Spotify',    handle: '', url: '', kind: 'Stream',   status: 'planned' },
    { key: 'bluesky',    label: 'Bluesky',    handle: '', url: '', kind: 'Text',     status: 'planned' },
  ] as PlatformLink[],

  // Tools — small credibility detail for the about section.
  tools: ['Mixed In Key', 'four-deck digital + analog hybrid'],

  // City/region for Person/LocalBusiness schema + local SEO. Blank = omitted.
  locality: '', // e.g. 'Lexington, KY'
} as const;

/** Rows that actually render: claimed accounts, in roster order. */
export function liveLinks(): PlatformLink[] {
  return site.links.filter((l) => l.status === 'live' && l.url.trim() !== '');
}

/** Accounts still to claim — surfaced in the build log, never on the page. */
export function plannedLinks(): PlatformLink[] {
  return site.links.filter((l) => l.status !== 'live' || l.url.trim() === '');
}

/** True once the operator has a real inbox in place (not the placeholder). */
export function hasRealBookingEmail(): boolean {
  return !site.booking.email.endsWith('.example');
}

export function bookingMailto(): string {
  const subject = encodeURIComponent('Booking — DJ Seith');
  return `mailto:${site.booking.email}?subject=${subject}`;
}
