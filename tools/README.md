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
