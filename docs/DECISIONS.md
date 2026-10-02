# Decisions log

Format: date — decision — why — alternatives considered.

## 2026-10-02 — Session 1 (autonomous rebuild)

### D1. Static site generator: Hugo extended, no npm
- **Decision:** Hugo extended (local `hugo v0.167.0+extended`), custom layouts, plain CSS with custom properties, minimal vanilla JS. No `package.json`, no `node_modules`.
- **Why:** `node -v` → v18.12.1 (below Astro's requirement of Node ≥ 20). Hugo is a single binary, builds in milliseconds, has built-in i18n, sitemap, image processing and asset pipeline (minify + fingerprint). Zero JS dependencies = nothing to update, smaller attack surface.
- **Alternatives:** Astro via `nvm use 22` (possible, but adds npm dependency tree for a mostly-text site); hand-written HTML (no i18n, no shared layouts).
- **Notes:** No third-party Hugo theme — own layouts for control over weight and quality. Hugo version pinned in CI to `0.167.0`.

### D2. Fonts: system font stacks, no web fonts
- **Decision:** `ui-sans-serif, -apple-system, "Segoe UI", Inter, Roboto, sans-serif` for text, `ui-monospace, "SF Mono", Menlo, Consolas, monospace` for engineering details.
- **Why:** No licence-clean woff2 fonts found in the repo/system to self-host; system stacks cost 0 KB and keep the site free of external requests.
- **Alternatives:** self-hosting Inter (OFL) — would need downloading; deferred to backlog.

### D3. Brand source and accent colour
- **Decision:** The studio logo source is `anko_logo.jpg` (2048×2048, black background, white wordmark "AnKo" + rule + "ENGINEERED SOFTWARE"). It is moved to `assets/brand/anko_logo.jpg` via `git mv` and only resized copies are served.
- **Why:** All PNGs in `~/Desktop/AnKo Software Labs/logo/` (`4d24bf8c…png`, `archive/*.png`, `archive (1)/*.png`, `a403548d…png`) turned out to be **TapReply** logo variants (orange, with a "Higgsfield AI" watermark), not the studio logo. There is no transparent studio logo.
- **Accent:** logo is monochrome → single restrained cool cyan accent (`#22d3ee` dark theme / `#0e7490` light theme). Green status dot `#22c55e` from the old site is kept for "in development" status.
- **TapReply logo:** `~/Desktop/AnKo Software Labs/tr_logo.png` (2048², no watermark) → downscaled copy in `assets/brand/tapreply.png` (512px) for the product card.
- **Terroir:** no logo → text mark placeholder in site palette, `TODO(Anton)`.

### D4. Public contact email
- **Decision:** `params.email = contact@ankosoftlab.com` (single variable in `hugo.toml`). `ceo@ankosoftlab.com` is not published.
- **Why:** Already public on the old site (continuity for platform verifications); role address is better than a personal-sounding one; both forward to the same inbox.

### D5. Content changes vs. old `index.html`
Kept:
- Dark visual language (palette `#050505 / #0d0d0f / #151518 / #27272a / #a1a1aa / #22c55e`), big negative-tracked headings, "Engineered Software" tagline.
- Service areas: product engineering, backend systems, AI workflows.
- TapReply description (AI-assisted review replies for local businesses), founder facts: commercial mobile development since 2022, Flutter/Dart, REST APIs, Firebase, realtime, local storage, architecture, release support.
- `contact@ankosoftlab.com`, link to tapreply.net.

Changed:
- "Independent software company", "the company" → "independent software studio" / "software lab". The business is a sole proprietorship (Individual Entrepreneur Anton Kozyrev, Georgia), not a company.
- "B2B SaaS / proprietary products only" → studio = own products **and** development services (matches the registered activity).
- "EU-facing" claim removed (not substantiated).
- Stack: removed vendor-specific "OpenRouter API" (no model/provider names on the site), removed "Dio" (too granular); added Go, Firebase.
- TapReply status made explicit: "In development — pilot (PWA) in preparation". Feature list reduced to what exists/planned, planned items marked as planned. Multi-platform + local-language replies added (from business context).
- Added Terroir (early development / early access).
- "© 2026 AnKo Software Labs. All rights reserved." → footer with legal owner line and legal pages.
- "Leadership" section → About page; no team, no offices.

### D6. Commit author
- `git config user.name` = "Anton Kozyrev" (not "dev-toxin"), email = `214382463+dev-toxin@users.noreply.github.com` (GitHub noreply of dev-toxin, same globally).
- **Decision:** commits are made with `git -c user.name="dev-toxin" -c user.email="214382463+dev-toxin@users.noreply.github.com" commit …`.
