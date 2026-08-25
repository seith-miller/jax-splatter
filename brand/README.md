# brand

Brand art for Jax Splatter, split by a hard line:

- **[releases/](releases/)** — official, signed-off art. The registry
  ([releases/REGISTRY.md](releases/REGISTRY.md)) defines the naming/tracking
  scheme. **No release is official until the operator signs off**; sign-off is
  recorded in the registry. Currently empty — no finished Jax Splatter art
  exists yet.
- **[reference/](reference/)** — the archive. Everything that informs the brand
  but isn't (or isn't yet) an official release.

## reference/originals

The three "Jack Splatter" AI-generated images (ChatGPT, Jul 2025) from the Drive
folder [P32: Release Jack Splatter](https://drive.google.com/drive/folders/1xmnZTiHMYDFYFXroYTGpU8gLpAz9ions),
archived here verbatim. The act was renamed **Jax Splatter** in Aug 2026
(docs/accounts-inventory.md), so these carry the dead name — reference only.

## reference/remakes

Same-style rebuilds of the originals under the new name, kept as editable
sources so a future release candidate is an edit away, not a regeneration:

| source | export | notes |
|---|---|---|
| `jax-logotype.html` | `exports/jax-logotype.png` | Nosifer drip logotype |
| `jax-new-song-put-it-in-my.html` | `exports/jax-new-song-put-it-in-my.png` | Creepster / Permanent Marker / Anton |
| `jax-put-it-in-my-shirt.html` | `exports/jax-put-it-in-my-shirt.png` | keeps the original raster: old title inpainted out (OpenCV TELEA + re-grain) into `assets/put-it-in-my-shirt-base.png`, new title set over it |

Palette sampled from the originals: logotype pink `#ea3e86` · promo pink
`#d54f7d` · off-white `#d1cac2` · near-black grounds.

### To re-render a remake

Edit the HTML, then (from the repo root):

```bash
python3 - <<'PY'
from playwright.sync_api import sync_playwright
import pathlib
with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={'width': 1024, 'height': 1024})
    for name in ['jax-logotype', 'jax-new-song-put-it-in-my', 'jax-put-it-in-my-shirt']:
        pg.goto('file://' + pathlib.Path(f'brand/reference/remakes/{name}.html').resolve().as_posix())
        pg.wait_for_timeout(3000)          # let the Google Fonts load
        pg.locator('.card').screenshot(path=f'brand/reference/remakes/exports/{name}.png')
    b.close()
PY
```

The site's social share card (`public/og.png`, source `tools/og-card.html`) is
site infrastructure, not brand art — it doesn't go through the registry.
