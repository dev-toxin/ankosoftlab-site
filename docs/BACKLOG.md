# Backlog

## P1 — before / right after the first push
- [ ] Switch GitHub Pages Source to **GitHub Actions**, then push; verify custom domain + HTTPS (see README).
- [ ] Legal review of Privacy / Terms / Imprint (EN + RU), then remove “Draft” (`legal: true` banner in `layouts/page.html`) and update `params.legalUpdated`.
- [x] 2026-10-07 — IE identification number published (`params.ieID = "304822565"`), operator wording unified.
- [ ] Confirm response time and time zone on Contact (EN + RU).
- [ ] Proof-read About texts (founder bio) — EN and RU.
- [ ] Run Lighthouse (mobile) on Home, Services, TapReply, Privacy — target ≥ 95 in all categories. Not run in session 1 (no Lighthouse CLI without npm/network).
- [ ] Validate structured data in Google Rich Results Test / Schema.org validator after deploy.

## P2 — content and brand
- [ ] Real founder photo for About (replace placeholder in `layouts/about.html`).
- [ ] GitHub / LinkedIn links on About (currently commented out).
- [ ] Terroir logo (text mark placeholder in `layouts/_partials/product-logo.html`) + regenerate `static/og/terroir.png`.
- [ ] Vector (SVG) version of the studio logo; then add `icon.svg` favicon and crisper header mark.
- [ ] Transparent-background studio logo (current source is a JPEG on black).
- [ ] Multi-size `favicon.ico` (16+32+48); current one is 32×32 only.
- [ ] Commit OG image HTML sources + a small script to regenerate them with headless Chrome.
- [ ] Decide on indicative pricing on Services.
- [ ] Case studies — only when there are real, publishable projects.
- [ ] Self-host Inter (OFL) as woff2 if system fonts look too different across platforms.

## P3 — later
- [ ] Move to **Cloudflare Pages** after the DNS move (not before December 2026): connect repo, build `hugo --minify --gc`, output `public`, `HUGO_VERSION=0.167.0`; disable the GitHub workflow; update the hosting section of the Privacy Policy.
- [ ] Cloudflare Web Analytics (cookieless) — **only after Anton decides**; Privacy Policy must be updated first.
- [ ] Contact form via Cloudflare Pages Functions + Email Routing (instead of mailto) — later, needs Privacy update and spam protection without third-party captchas.
- [ ] Optional studio blog / engineering notes.
- [ ] Optional manual theme toggle (needs a tiny external JS file + CSP update; no inline script).
- [ ] `humans.txt`, `security.txt` (`/.well-known/security.txt`).
