# SEO

Installed: **Yoast SEO 28.8** (2026-10-31). Titles and meta descriptions live in `build/content.py` (`SEO`) and are pushed by `build/build.py` through Yoast's bulk-editor API. og:description falls back to the meta description; og:image is each page's featured image (`halo-og.jpg`, media 1635, 1200×630).

Edit a description: change `SEO` in `build/content.py` and re-run `python3 build/build.py` — or edit it in wp-admin (page → Yoast box). A re-run of the build overwrites wp-admin edits for these pages.

Sitemap: https://drivehalo.ai/sitemap_index.xml
