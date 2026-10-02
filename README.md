# ankosoftlab-site

Official website of **AnKo Software Labs**, an independent software studio (trading name of Anton Kozyrev, Individual Entrepreneur, Georgia) — <https://www.ankosoftlab.com>.

Static multi-page site in English (root `/`) and Russian (`/ru/`).

## Stack

- [Hugo](https://gohugo.io/) **extended**, pinned to `0.167.0` (local and CI). No Node.js, no npm, no third-party theme.
- Own layouts in `layouts/`, plain CSS with custom properties in `assets/css/main.css` (minified + fingerprinted by Hugo Pipes).
- **No JavaScript.** The mobile menu uses the native Popover API; reveal-on-scroll uses CSS scroll-driven animations.
- System font stacks, no external requests (no CDNs, fonts, analytics or cookies).
- Images resized/converted to WebP by Hugo image processing; icons and OG images are pre-generated PNGs in `static/`.

Why these choices: see [`docs/DECISIONS.md`](docs/DECISIONS.md).

## Run locally

```sh
hugo server            # http://localhost:1313, live reload
```

## Build

```sh
hugo --minify --gc     # output → public/
python3 scripts/qa.py  # optional: links, JSON-LD, titles/descriptions, page weight
```

`public/` is git-ignored. `static/CNAME` (`www.ankosoftlab.com`) is copied into the build root.

> Don't run `scripts/qa.py` while `hugo server` is running — the dev server rewrites `public/` with `localhost` URLs.

## Deploy

### GitHub Pages (current, via GitHub Actions)

Workflow: `.github/workflows/pages.yml` — builds with Hugo `0.167.0` and deploys with `actions/deploy-pages` on every push to `main`.

> ⚠️ **Before the first push of this version:** open *GitHub → Settings → Pages → Build and deployment → Source* and select **GitHub Actions**.
> The repository root no longer contains `index.html`. If Pages still serves “Deploy from a branch”, the live site will break (404).

Order: switch Source → `git push origin main` → check the Actions run → open https://www.ankosoftlab.com and make sure the custom domain is still `www.ankosoftlab.com` (Settings → Pages).

`static/_headers` and `static/_redirects` are Cloudflare Pages features; GitHub Pages ignores them (no CSP/security headers on GitHub Pages — that's expected).

### Cloudflare Pages (planned, after the DNS move — not before December 2026)

| Setting | Value |
|---|---|
| Framework preset | Hugo |
| Build command | `hugo --minify --gc` |
| Build output directory | `public` |
| Environment variable | `HUGO_VERSION = 0.167.0` (and optionally `HUGO_EXTENDED = true`) |

`_headers` (strict CSP, security headers, caching) and `_redirects` will apply automatically. After the move, disable the GitHub Pages workflow and update the hosting paragraph in the Privacy Policy (EN + RU).

## Where things are

| What | Where |
|---|---|
| Texts (EN) | `content/en/*.md` — most page copy is in front matter |
| Texts (RU) | `content/ru/*.md` — same file names as EN (that's how translations are linked) |
| UI strings (buttons, labels) | `i18n/en.toml`, `i18n/ru.toml` |
| Menus, languages | `hugo.toml` |
| Public email, product URLs, IE ID, legal date | `[params]` in `hugo.toml` (`email`, `tapreplyURL`, `terroirURL`, `ieID`, `legalUpdated`) |
| Design tokens / styles | `assets/css/main.css` (`:root` variables; light theme in `prefers-color-scheme: light`) |
| Inline SVG diagrams | `layouts/_partials/diagram.html` |
| Structured data (JSON-LD) | `layouts/_partials/jsonld.html` |
| Brand sources | `assets/brand/anko_logo.jpg` (studio), `assets/brand/tapreply.png` |
| Icons, manifest, OG images | `static/` |

Note: the `email` param is used for all links/templates in layouts; legal Markdown pages contain the address as plain text — update them too if the address changes.

## TODO(Anton)

Run `grep -rn "TODO(Anton)" content layouts hugo.toml` for the current list. Summary in `docs/sessions/2026-10-02.md`.
