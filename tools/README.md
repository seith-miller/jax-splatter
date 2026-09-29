# tools

## `og-card.html` → `public/og.png`

The social share card. It is the most-seen asset on this site: every platform
bio links here, so this image is what renders in DMs, Slack, Discord, iMessage
and every feed preview.

**It must ship as a PNG.** Facebook/Instagram, X, iMessage, Slack and Discord
do not render SVG OpenGraph images — an `og.svg` silently shows nothing.

To change the card: edit `og-card.html`, then re-render it at 1200×630:

```bash
python3 - <<'PY'
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={'width': 1200, 'height': 630})
    pg.goto('file://' + __import__('pathlib').Path('tools/og-card.html').resolve().as_posix())
    pg.wait_for_timeout(3000)          # let Oswald load from Google Fonts
    pg.locator('.card').screenshot(path='public/og.png')
    b.close()
PY
```

## `wordmark-svg.py` → `brand/reference/wordmark/svg/`

Outlines the JAX-A002 wordmark from Pathway Gothic One (OFL, `tools/`) into
SVG paths with the signed spacing (letter-spacing .015em, .30em word gap,
kerning via HarfBuzz). Dark, light, one-colour cut, and JAX-crop variants.

```bash
python3 -m venv .venv && .venv/bin/pip install fonttools uharfbuzz
.venv/bin/python tools/wordmark-svg.py            # writes the five SVGs
```
