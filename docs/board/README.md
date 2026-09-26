# Splatter Ops — the internal board

Jax's internal-facing page for the act. **Locally hosted** — it is not part
of the Astro site and never deploys to jaxsplatter.com. `docs/` sits outside
`src/` and `public/`, so `astro build` doesn't see it.

## Run it

```bash
npm run board          # serves docs/board on 127.0.0.1:8787
```

Then open **http://localhost:8787**. Bound to localhost only — nothing on
the network can reach it. Stop it with Ctrl-C.

## What's on it

**Stripped to one thing (Jax, 2026-09-26):** the next show and how many days
out. DILDOZER, Saturday October 24, venue TBD.

An earlier version carried gates, an hour meter, cast fields and money —
too much. That detail lives in [debut-calendar.md](../debut-calendar.md) and
[debut-staging.md](../debut-staging.md) where it belongs.

We build back from October 24, not December 19.

## Editing

`index.html` is the page — plain static HTML, no build step. Save and
refresh.

Keep the `<meta charset="utf-8">`. `python3 -m http.server` sends
`text/html` with no charset, so without that line the browser guesses
windows-1252 and every non-ASCII character breaks — the middle dot in
"Sat · Oct 24" turns into `Â·`.
