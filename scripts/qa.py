#!/usr/bin/env python3
"""Static QA for the built site (public/). Standard library only.

Checks: internal links/assets resolve, external hosts are allow-listed, JSON-LD parses
(and has no aggregateRating/offers), title <= 60 / description <= 155 chars, exactly one <h1>,
lang attribute, canonical, img width/height/alt, page weights.
Usage: hugo --minify && python3 scripts/qa.py
"""
import json
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT = os.path.join(os.path.dirname(__file__), "..", "public")
ROOT = os.path.abspath(ROOT)
ALLOWED_HOSTS = {"www.ankosoftlab.com", "tapreply.net", "terroir-app.com", "schema.org",
                 # /work/ case links (public store and project pages), added 2026-10-08
                 "apps.apple.com", "zhabby.info", "teleport.run", "jobline.one"}
SKIP_DIRS = {"_t"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self.assets, self.imgs, self.jsonld = [], [], [], []
        self.h1 = 0
        self.lang = None
        self.title = ""
        self.desc = None
        self.canonical = None
        self.ids = set()
        self._in_title = False
        self._in_ld = False
        self._ld = ""
        self._svg = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "svg":
            self._svg += 1
        elif tag == "title" and not self._svg:
            self._in_title = True
        elif tag == "h1":
            self.h1 += 1
        elif tag == "a" and "href" in a:
            self.links.append(a["href"])
        elif tag == "link" and "href" in a:
            if a.get("rel") == "canonical":
                self.canonical = a["href"]
            self.assets.append(a["href"])
        elif tag == "img":
            self.imgs.append(a)
            if "src" in a:
                self.assets.append(a["src"])
            for part in (a.get("srcset") or "").split(","):
                if part.strip():
                    self.assets.append(part.strip().split()[0])
        elif tag == "meta" and a.get("name") == "description":
            self.desc = a.get("content")
        elif tag == "script":
            if a.get("type") == "application/ld+json":
                self._in_ld = True
                self._ld = ""
            else:
                self.assets.append(a.get("src", "INLINE-SCRIPT"))

    def handle_endtag(self, tag):
        if tag == "svg":
            self._svg -= 1
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_ld:
            self._in_ld = False
            self.jsonld.append(self._ld)

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_ld:
            self._ld += data


def resolve(path):
    p = unquote(path.split("#")[0].split("?")[0])
    full = os.path.join(ROOT, p.lstrip("/"))
    if p.endswith("/") or os.path.isdir(full):
        full = os.path.join(full, "index.html")
    return full


def main():
    errors, warns, pages = [], [], {}
    for dirpath, dirnames, files in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(".html"):
                full = os.path.join(dirpath, f)
                rel = "/" + os.path.relpath(full, ROOT)
                p = Page()
                with open(full, encoding="utf-8") as fh:
                    p.feed(fh.read())
                pages[rel] = p

    redirect_stub = lambda p: not p.title or p.title.startswith("https://")
    for rel, p in sorted(pages.items()):
        if redirect_stub(p):
            continue
        is404 = rel.endswith("404.html")
        if not p.lang:
            errors.append(f"{rel}: missing <html lang>")
        if p.h1 != 1:
            errors.append(f"{rel}: {p.h1} <h1> elements")
        if len(p.title) > 60:
            warns.append(f"{rel}: title {len(p.title)} chars: {p.title}")
        if not p.desc:
            errors.append(f"{rel}: no meta description")
        elif len(p.desc) > 155:
            warns.append(f"{rel}: description {len(p.desc)} chars")
        if not is404 and not (p.canonical or "").startswith("https://www.ankosoftlab.com/"):
            errors.append(f"{rel}: bad canonical {p.canonical}")
        for img in p.imgs:
            for k in ("width", "height", "alt"):
                if k not in img:
                    errors.append(f"{rel}: <img {img.get('src')}> missing {k}")
        for blob in p.jsonld:
            try:
                data = json.loads(blob)
            except json.JSONDecodeError as e:
                errors.append(f"{rel}: JSON-LD invalid: {e}")
                continue
            s = json.dumps(data)
            for bad in ("aggregateRating", "offers", "review"):
                if f'"{bad}"' in s:
                    errors.append(f"{rel}: JSON-LD contains {bad}")
        for href in p.links + p.assets:
            if href == "INLINE-SCRIPT":
                errors.append(f"{rel}: inline/external <script> found")
                continue
            u = urlparse(href)
            if u.scheme == "mailto":
                continue
            if u.scheme in ("http", "https"):
                if u.hostname not in ALLOWED_HOSTS:
                    errors.append(f"{rel}: external host not allowed: {href}")
                if u.hostname == "www.ankosoftlab.com":
                    if not os.path.exists(resolve(u.path)):
                        errors.append(f"{rel}: broken absolute link {href}")
                continue
            if href.startswith("#"):
                if href[1:] and href[1:] not in p.ids:
                    errors.append(f"{rel}: missing anchor {href}")
                continue
            target = href if href.startswith("/") else os.path.join(os.path.dirname(rel), href)
            if not os.path.exists(resolve(target)):
                errors.append(f"{rel}: broken link {href}")
            elif "#" in href:
                frag = href.split("#", 1)[1]
                tp = "/" + os.path.relpath(resolve(target), ROOT)
                if tp in pages and frag not in pages[tp].ids:
                    errors.append(f"{rel}: missing anchor {href}")

    # Page weight: HTML + CSS + images referenced (unique), excluding fonts (none used).
    print("Page weight (HTML + linked CSS/images, bytes):")
    for rel in ("/index.html", "/services/index.html", "/products/tapreply/index.html", "/ru/index.html", "/privacy/index.html"):
        p = pages.get(rel)
        if not p:
            continue
        total = os.path.getsize(os.path.join(ROOT, rel.lstrip("/")))
        seen = set()
        for a in p.assets:
            if a.startswith("/") and (a.endswith(".css") or a.endswith(".webp")) and a not in seen:
                seen.add(a)
                f = resolve(a)
                if os.path.exists(f):
                    total += os.path.getsize(f)
        print(f"  {rel:35s} {total:>8d}  ({total/1024:.1f} KB)")

    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(pages)} HTML files, {len(errors)} errors, {len(warns)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
