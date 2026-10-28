#!/usr/bin/env python3
"""Build the Halo v2 launch pages in WordPress/Elementor via the REST API.

Idempotent: pages, menu, and templates are looked up by slug/title and updated
in place. Auth is injected by the environment's network proxy.

Usage: python3 build/build.py [--only slug,slug] [--dry-run]
"""
import argparse
import json
import os
import pathlib
import secrets

import requests

import content

API = "https://drivehalo.ai/wp-json"
SITE = "https://drivehalo.ai"
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "build" / "out"
CA = "/root/.ccr/ca-bundle.crt"
PASSWORD = os.environ.get("HALO_PREVIEW_PASSWORD", "HaloPreview27")
V1_TEMPLATES = (30, 77)  # original Elementor header/footer
# All v2 pages are public. Add slugs to PRIVATE to put a page back behind PASSWORD.
PRIVATE = set()
CSS_START = "/* ==== HALO-V2 START ==== */"
CSS_END = "/* ==== HALO-V2 END ==== */"

MEDIA = {
    "logo": (1409, f"{SITE}/wp-content/uploads/2026/10/halo-logo.png"),
    "film": (1476, f"{SITE}/wp-content/uploads/2026/10/halo-film-web-safe.mp4"),  # customer column blurred (tools/)
    "poster": (1416, f"{SITE}/wp-content/uploads/2026/10/halo-ui-marketing.jpg"),
    "ui-inventory": (1415, f"{SITE}/wp-content/uploads/2026/10/halo-ui-inventory.jpg"),
    "ui-sales": (1417, f"{SITE}/wp-content/uploads/2026/10/halo-ui-sales.jpg"),
    "ui-halo-ai": (1414, f"{SITE}/wp-content/uploads/2026/10/halo-ui-halo-ai.jpg"),
    "ui-marketing": (1416, f"{SITE}/wp-content/uploads/2026/10/halo-ui-marketing.jpg"),
}

ASTRA_META = {
    "site-sidebar-layout": "no-sidebar",
    "ast-site-content-layout": "full-width-container",
    "site-content-style": "default",
    "site-sidebar-style": "default",
    "site-post-title": "disabled",
    "ast-featured-img": "disabled",
}

s = requests.Session()
s.verify = CA


def api(method, path, **kw):
    r = s.request(method, API + path, timeout=60, **kw)
    if r.status_code >= 400:
        raise SystemExit(f"{method} {path} -> {r.status_code}: {r.text[:800]}")
    return r.json() if r.content.strip() else None


def url(slug):
    return f"{SITE}/{slug}/"


# --------------------------------------------------------------------------
# Elementor element helpers
# --------------------------------------------------------------------------
def _id():
    return secrets.token_hex(4)[:7]


def con(cls, *children, inner=True, **settings):
    base = {"content_width": "full", "flex_direction": "column", "css_classes": cls}
    base.update(settings)
    return {"id": _id(), "elType": "container", "settings": base,
            "elements": [c for c in children if c], "isInner": inner}


def section(cls, *children, **settings):
    return con(f"hv2 hv2-section {cls}", con("hv2-wrap", *children), inner=False, **settings)


def widget(kind, cls="", **settings):
    if cls:
        settings["_css_classes"] = cls
    return {"id": _id(), "elType": "widget", "widgetType": kind, "settings": settings, "elements": []}


def heading(text, tag="h2", cls="hv2-h2"):
    return widget("heading", cls, title=text, header_size=tag)


def text(html, cls="hv2-body"):
    return widget("text-editor", cls, editor=html)


def html(code, cls=""):
    return widget("html", cls, html=code)


def button(label, href, cls="hv2-btn"):
    return widget("button", cls, text=label, link={"url": href, "is_external": "", "nofollow": ""})


def image(key, cls="", alt=""):
    mid, src = MEDIA[key]
    return widget("image", cls, image={"url": src, "id": mid, "source": "library", "alt": alt},
                  image_size="full")


def label(num, name):
    n = f'<span class="n">{num}</span>' if num else ""
    return text(f"<p>{n}{name}</p>", "hv2-label")


def demo_cta():
    c = content.CTA
    return section(
        "hv2-cta",
        heading(c["h2"], "h2", "hv2-h2"),
        con("hv2-cta-side",
            text(f"<p>{c['body']}</p>", "hv2-lead"),
            button(c["button"], url("waitlist"))),
    )


def page_head(num, name, h1, lead):
    return section("hv2-head", label(num, name), heading(h1, "h1", "hv2-h1"),
                   text(f"<p>{lead}</p>", "hv2-lead"))


def figure(key, caption, alt):
    return section("hv2-fig", image(key, alt=alt), text(f"<p>{caption}</p>", "hv2-caption"))


def rows(items, intro=None):
    els = []
    if intro:
        els.append(heading(intro, "h2", "hv2-h2 hv2-rows-intro"))
    for i, it in enumerate(items, 1):
        k = [heading(it["title"], "h3", "hv2-h3")]
        if it.get("kicker"):
            k.insert(0, text(f"<p>{it['kicker']}</p>", "hv2-kicker"))
        els.append(con("hv2-row",
                       text(f"<p>{i:02d}</p>", "hv2-num"),
                       con("hv2-row-k", *k),
                       text(f"<p>{it['body']}</p>", "hv2-body")))
    return section("hv2-rows", *els)


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
def build_home(menu_slug):
    c = content.HOME
    _, src = MEDIA["film"]
    _, psrc = MEDIA["poster"]
    stage = html(
        FONTS +
        '<div class="hv2-stage" id="film">'
        f'<video autoplay muted loop playsinline preload="auto" poster="{psrc}" aria-label="Halo OS brand film">'
        f'<source src="{src}" type="video/mp4"></video>'
        '<button class="hv2-sound" type="button" aria-pressed="false">'
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4z" fill="currentColor"/>'
        '<path class="w" d="M16 8.5a5 5 0 0 1 0 7M18.5 6a8.5 8.5 0 0 1 0 12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>'
        '<span class="t">Sound on</span></button></div>'
        '<script>(function(){var w=document.getElementById("film");if(!w)return;'
        'var v=w.querySelector("video"),b=w.querySelector(".hv2-sound"),t=b.querySelector(".t"),first=true;'
        'if(window.matchMedia("(prefers-reduced-motion: reduce)").matches){v.pause();v.controls=true;}'
        'else{var p=v.play();if(p&&p.catch)p.catch(function(){v.controls=true;});}'
        'b.addEventListener("click",function(){if(v.muted){if(first){v.currentTime=0;first=false;}'
        'v.muted=false;v.play();t.textContent="Sound off";b.setAttribute("aria-pressed","true");w.classList.add("is-sound");}'
        'else{v.muted=true;t.textContent="Sound on";b.setAttribute("aria-pressed","false");w.classList.remove("is-sound");}});})();</script>'
    )
    return [
        con("hv2 hv2-section hv2-stage-sec", stage, inner=False),
        header_bar(menu_slug, "hv2-header--inpage"),
        section("hv2-hero",
                label("", c["label"]),
                heading(c["h1"], "h1", "hv2-h1"),
                con("hv2-hero-foot",
                    text(f"<p>{c['tagline']}</p>", "hv2-tagline"),
                    con("hv2-btn-row", button(c["primary"], url("waitlist"), "hv2-btn")))),
    ]


def people_html(people):
    cards = []
    for name, title, bio in people:
        initials = "".join(w[0] for w in name.split()[:2]).upper()
        cards.append(f'<div class="hv2-person"><div class="mono" aria-hidden="true">{initials}</div>'
                     f'<h3>{name}</h3><p class="role">{title}</p>' + (f"<p>{bio}</p>" if bio else "") + "</div>")
    return f'<div class="hv2-people">{"".join(cards)}</div>'


def build_pillar(key):
    c = content.PAGES[key]
    els = [page_head(c["num"], c["name"], c["h1"], c["lead"])]
    if c.get("figure"):
        f = c["figure"]
        els.append(figure(f["key"], f["caption"], f["alt"]))
    if c.get("visual_html"):
        els.append(section("hv2-fig", html(c["visual_html"]),
                           text(f"<p>{c['visual_caption']}</p>", "hv2-caption") if c.get("visual_caption") else None))
    if c.get("rows"):
        els.append(rows(c["rows"], c.get("rows_intro")))
    if c.get("body_html"):
        els.append(section("hv2-rows", html(c["body_html"])))
    if c.get("story"):
        st = c["story"]
        els.append(section("hv2-rows",
                           con("hv2-story",
                               con("hv2-story-k", text(st["quote"], "hv2-quote")),
                               con("hv2-story-v", text(st["body"], "hv2-body"))),
                           heading(st["people_title"], "h2", "hv2-h2 hv2-rows-intro"),
                           html(people_html(st["people"]))))
    if c.get("legal_html"):
        els.append(section("hv2-rows", html(c["legal_html"])))
    if c.get("cta", True):
        els.append(demo_cta())
    return els


def build_demo():
    c = content.DEMO
    fields = [
        {"custom_id": "name", "field_label": "Your name", "placeholder": "First and last name", "required": "true", "width": "100"},
        {"custom_id": "dealership", "field_label": "Dealership or group", "placeholder": "e.g. Castle Automotive Group", "required": "true", "width": "100"},
        {"custom_id": "rooftops", "field_type": "select", "field_label": "Rooftops", "field_options": "Select…|\n1\n2–5\n6–15\n16–30\n30+", "required": "true", "width": "50"},
        {"custom_id": "role", "field_label": "Your role", "placeholder": "e.g. Dealer Principal, GM", "width": "50"},
        {"custom_id": "email", "field_type": "email", "field_label": "Work email", "placeholder": "you@dealership.com", "required": "true", "width": "50"},
        {"custom_id": "phone", "field_type": "tel", "field_label": "Phone", "placeholder": "(555) 555-5555", "width": "50"},
    ]
    for f in fields:
        f["_id"] = _id()
    form = widget(
        "form", "hv2-form",
        form_name="Wait List",
        form_fields=fields,
        show_labels="yes",
        mark_required="",
        button_text=c["button"],
        button_width="100",
        submit_actions=["email"],
        email_to="david@drivehalo.ai",
        email_subject='Halo wait list: [field id="dealership"] ([field id="rooftops"] rooftops)',
        email_content="[all-fields]",
        email_from="email@drivehalo.ai",
        email_from_name="Halo",
        email_reply_to='[field id="email"]',
        success_message=c["success"],
        error_message="Something went wrong. Email david@drivehalo.ai and we'll take it from there.",
        required_field_message="Required.",
        column_gap={"unit": "px", "size": 16, "sizes": []},
        row_gap={"unit": "px", "size": 4, "sizes": []},
    )
    steps = "".join(f'<li><span class="n">{i:02d}</span><span>{t}</span></li>' for i, t in enumerate(c["next"], 1))
    return [
        section("hv2-demo",
                con("hv2-demo-k",
                    label("", c["label"]),
                    heading(c["h1"], "h1", "hv2-h1"),
                    text(f"<p>{c['lead']}</p>", "hv2-lead"),
                    html(f'<ul class="hv2-next">{steps}</ul>')),
                con("hv2-demo-form", form)),
    ]


# --------------------------------------------------------------------------
# Header / footer
# --------------------------------------------------------------------------
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600'
         '&family=IBM+Plex+Mono:wght@400;500&family=Syne:wght@600;700&display=swap">')


def header_bar(menu_slug, extra=""):
    logo = image("logo", "hv2-logo", alt="Halo — Automotive Intelligence")
    logo["settings"]["link_to"] = "custom"
    logo["settings"]["link"] = {"url": f"{SITE}/", "is_external": "", "nofollow": ""}
    nav = widget("nav-menu", "hv2-nav", menu=menu_slug, layout="horizontal", align_items="center",
                 pointer="none", dropdown="tablet", toggle="burger", full_width="stretch",
                 text_align="aside")
    return con(f"hv2 hv2-header {extra}".strip(),
               con("hv2-wrap",
                   html(FONTS),
                   logo,
                   nav,
                   con("hv2-head-cta", button(content.CTA_LABEL, url("waitlist"), "hv2-btn"))),
               inner=False, sticky="top", sticky_on=["desktop", "tablet", "mobile"])


def build_header(menu_slug):
    return [header_bar(menu_slug)]


def build_footer():
    c = content.FOOTER
    cols = "".join(
        f"<div><h4>{col['title']}</h4><ul>" +
        "".join(f'<li><a href="{href}">{name}</a></li>' for name, href in col["links"]) +
        "</ul></div>" for col in c["cols"])
    logo = image("logo", "hv2-logo", alt="Halo — Automotive Intelligence")
    logo["settings"]["align"] = "left"
    return [con("hv2 hv2-footer",
                con("hv2-wrap",
                    con("hv2-foot-brand", logo, text(f"<p>{c['tagline']}</p>", "hv2-body")),
                    html(f'<nav class="hv2-foot-cols" aria-label="Footer">{cols}</nav>'),
                    con("hv2-foot-base",
                        text(f"<p>{c['legal']}</p>", "hv2-label"),
                        text(f"<p>{c['domain']}</p>", "hv2-label"))),
                inner=False)]


# --------------------------------------------------------------------------
# WordPress sync
# --------------------------------------------------------------------------
def find_page(slug):
    r = api("GET", f"/wp/v2/pages?slug={slug}&status=publish,draft,private&context=edit")
    return r[0] if r else None


def upsert_page(slug, title, data, dry, page_settings=None):
    (OUT / f"page-{slug}.json").write_text(json.dumps(data, indent=1))
    if dry:
        return None
    body = {
        "title": title,
        "slug": slug,
        "status": "publish",
        "password": PASSWORD if slug in PRIVATE else "",
        "meta": {
            **ASTRA_META,
            "_elementor_edit_mode": "builder",
            "_elementor_template_type": "wp-page",
            "_elementor_page_settings": {"hide_title": "yes", **(page_settings or {})},
            "_elementor_data": json.dumps(data),
        },
    }
    p = find_page(slug)
    res = api("POST", f"/wp/v2/pages/{p['id']}" if p else "/wp/v2/pages", json=body)
    print(f"{'updated' if p else 'created'} page {res['id']} {res['link']}")
    return res["id"]


def upsert_template(title, kind, data, conds, dry):
    (OUT / f"template-{kind}.json").write_text(json.dumps(data, indent=1))
    if dry:
        return None
    existing = api("GET", f"/wp/v2/elementor_library?search={requests.utils.quote(title)}&context=edit")
    existing = [t for t in existing if t["title"]["raw"] == title]
    body = {"title": title, "status": "publish",
            "meta": {"_elementor_edit_mode": "builder", "_elementor_template_type": kind,
                     "_elementor_data": json.dumps(data)}}
    if existing:
        tid = existing[0]["id"]
        api("POST", f"/wp/v2/elementor_library/{tid}", json=body)
    else:
        tid = api("POST", "/wp/v2/elementor_library", json=body)["id"]
    api("PUT", f"/elementor/v1/site-editor/templates-conditions/{tid}", json={"conditions": conds})
    print(f"{kind} template {tid} -> {conds}")
    return tid


def ensure_menu(pages, dry):
    slug = "main-menu-v2"
    if dry:
        return slug
    menus = [m for m in api("GET", "/wp/v2/menus") if m["slug"] == slug]
    mid = menus[0]["id"] if menus else api("POST", "/wp/v2/menus", json={"name": "Main Menu v2", "slug": slug})["id"]
    for item in api("GET", f"/wp/v2/menu-items?menus={mid}&per_page=100"):
        api("DELETE", f"/wp/v2/menu-items/{item['id']}?force=true")
    for order, (label_, slug_) in enumerate(content.NAV, 1):
        api("POST", "/wp/v2/menu-items", json={
            "title": label_, "status": "publish", "menus": mid, "menu_order": order,
            "type": "post_type", "object": "page", "object_id": pages[slug_]})
    print(f"menu {mid} ({slug}) with {len(content.NAV)} items")
    return slug


def sync_css(dry):
    css = (ROOT / "theme" / "halo-v2.css").read_text()
    if dry:
        return
    kit = api("GET", "/wp/v2/elementor_library/6?context=edit")
    settings = kit["meta"]["_elementor_page_settings"]
    cur = settings.get("custom_css", "")
    if CSS_START in cur:
        cur = cur[: cur.index(CSS_START)].rstrip() + cur[cur.index(CSS_END) + len(CSS_END):]
    settings["custom_css"] = cur.rstrip() + f"\n\n{CSS_START}\n{css}\n{CSS_END}\n"
    api("POST", "/wp/v2/elementor_library/6", json={"meta": {"_elementor_page_settings": settings}})
    print("kit CSS synced")


def flush():
    api("DELETE", "/elementor/v1/cache")
    s.put(API + "/siteground-optimizer/v1/purge-cache", timeout=60)
    print("caches flushed")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--css-only", action="store_true")
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)

    sync_css(args.dry_run)
    if args.css_only:
        flush()
        return

    pages = {}
    menu_slug = "main-menu-v2"
    # Home: film first, then the menu bar, so the site template header is hidden there.
    pages["home"] = upsert_page("home", "Home", build_home(menu_slug), args.dry_run,
                                   {"custom_css": "body .elementor-location-header { display: none; }"})
    for key in content.PAGES:
        pages[key] = upsert_page(key, content.PAGES[key]["title"], build_pillar(key), args.dry_run)
    pages["waitlist"] = upsert_page("waitlist", "Join the Wait List", build_demo(), args.dry_run)

    menu_slug = ensure_menu(pages, args.dry_run)
    site_wide = [{"type": "include", "name": "general", "sub_name": "", "sub_id": ""}]
    # Home renders its own menu bar under the film, so it opts out of the template header.
    upsert_template("Header v2", "header", build_header(menu_slug),
                    site_wide + [{"type": "exclude", "name": "singular", "sub_name": "page",
                                  "sub_id": str(pages["home"])}] if pages["home"] else site_wide, args.dry_run)
    upsert_template("Footer v2", "footer", build_footer(), site_wide, args.dry_run)
    if not args.dry_run:
        # v1 header/footer stay saved for rollback but no longer display anywhere.
        for tid in V1_TEMPLATES:
            api("PUT", f"/elementor/v1/site-editor/templates-conditions/{tid}", json={"conditions": []})
        api("POST", "/wp/v2/settings", json={"show_on_front": "page", "page_on_front": pages["home"]})
        print(f"front page -> {pages['home']}")
        flush()
        (OUT / "pages.json").write_text(json.dumps(pages, indent=1))


if __name__ == "__main__":
    main()
