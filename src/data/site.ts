// Single source of truth for site-wide content and config.
// Editing this file is how the operator tunes the site without touching markup.

export const site = {
  name: 'DJ SEITH',
  tagline: 'Music producer & live performer',
  // One-line positioning shown in the hero. Keep it short and uppercase-friendly.
  heroStatement: 'Late-night sets for rooms that want to feel something.',

  // Pricing — research strongly supports SHOWING this (see docs/decisions.md D2).
  price: {
    low: 150,
    high: 250,
    unit: 'event',
    // One line on what moves the number — turns a bare range into useful info.
    note: 'Set length, travel, and whether you need lights + visuals move the number.',
  },

  // ── ACTION NEEDED BEFORE LAUNCH ──────────────────────────────────────────
  // These are placeholders. v0 does not publish a personal address or a live
  // form endpoint without ratification (see docs/decisions.md D6).
  booking: {
    email: 'bookings@djseith.example', // ← set a real booking inbox
    // Formspree: create a form at https://formspree.io, paste its ID here.
    // While this is the placeholder value, the form falls back to mailto.
    formspreeId: 'YOUR_FORM_ID',
  },
  // ─────────────────────────────────────────────────────────────────────────

  // Service angles. Anchored sections, NOT thin separate pages (decisions.md D8).
  services: [
    { key: 'private', label: 'Private parties', blurb: 'Birthdays, house parties, whatever the occasion — read the room, keep it moving.' },
    { key: 'bar', label: 'Bars & venues', blurb: 'Resident-style sets that hold a room for the long night.' },
    { key: 'event', label: 'Events & corporate', blurb: 'Curated sound for launches, openings, and brand nights.' },
  ],

  // Social / listening links. Leave a value empty ('') to hide that icon.
  // Mixes are hosted on Mixcloud (research: safer licensing — decisions.md D5).
  links: {
    mixcloud: '', // e.g. 'https://www.mixcloud.com/djseith/'
    instagram: '', // e.g. 'https://instagram.com/djseith'
    youtube: '',
    github: 'https://github.com/seith-miller/djseith',
  },

  // Tools — small credibility detail for the about section.
  tools: ['Mixed In Key', 'four-deck digital + analog hybrid'],

  // City/region for LocalBusiness schema + local SEO. Left blank pending the operator.
  locality: '', // e.g. 'Lexington, KY'
} as const;

export function formspreeAction(): string | null {
  const id = site.booking.formspreeId;
  if (!id || id === 'YOUR_FORM_ID') return null;
  return `https://formspree.io/f/${id}`;
}

export function priceRange(): string {
  return `$${site.price.low}–${site.price.high}`;
}
