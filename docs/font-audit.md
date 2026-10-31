# Font audit and Montserrat migration (2026-10-31)

## Findings before any change
| Where | What was set |
|---|---|
| Elementor kit (Site Settings → Global Fonts) | Primary Syne 800 · Secondary Syne 600 · Text DM Sans 400 · Accent Syne 500. Body typography "custom" with no family. |
| Elementor Google Fonts loading | On (default). Loaded **Syne and DM Sans, every weight 100–900 + italics** (2 stylesheets, 36 faces declared). |
| Astra Customizer typography | Body DM Sans 400, headings Syne 700 → separate Google Fonts stylesheet (`ver=4.14.0`) + inline `font-family:'Syne'` rules. |
| Custom CSS: HALO-V2 block (`theme/halo-v2.css`) | `--f-display: Syne`, `--f-body: DM Sans`, `--f-mono: IBM Plex Mono`. Display headings line-height 0.98, letter-spacing −0.035em. |
| Custom CSS: legacy v1 block (kit) | `.halo-eyebrow`, `.halo-btn*` used `'Syne'` (only used on drafted v1 pages). |
| Hard-coded `<link>` | Header + homepage HTML widgets loaded DM Sans 400/500/600, IBM Plex Mono 400/500, Syne 600/700 from Google. |
| Per-widget typography overrides | **None** on any live page, header or footer. (Drafted v1 pages 10/762 have some; not rendered.) |
| Child theme `style.css` | No font rules. |
| Clipping | `.hv2-case-card { overflow: hidden }` wrapped the Halo Effect case headings. No clip-path, no entrance animations. |
| Images without alt | Logo (header + footer, every page), Inventory and Sales screenshots. |
| Titles / meta | Home `<title>` was just "Halo". No meta descriptions or Open Graph tags anywhere. |

## Changes
- **Self-hosted fonts** via WordPress Font Library (`/wp-content/uploads/fonts/`, 1-year cache): Montserrat variable 400–800 (latin + latin-ext) and IBM Plex Mono 400/500 (latin + latin-ext). `@font-face` with `font-display: swap` in the kit CSS.
- **Elementor Google Fonts: off.** Kit Global Fonts → Montserrat (700/600/400/500) + new "Label (mono)" global = IBM Plex Mono 400. `halo-v2.css` reads families from `--e-global-typography-*`, so the kit is the single source of truth.
- Header/homepage Google Fonts `<link>` removed. Legacy v1 CSS `'Syne'` → `'Montserrat'`.
- Type scale: display line-height 1.05–1.08, letter-spacing −0.02em (H3 −0.01em), sizes scaled ~8% with `clamp()`; hero H1 800. Body 16px/1.65. Heading line counts verified unchanged on 195/196 headings across 7 pages × 4 widths.
- Case-card `overflow: hidden` removed.
- Home title "Halo – Dealership Command Center" (site tagline). About page title "About". Alt text set on the logo and four product screenshots (media library, applies site-wide).

## Still open
- **Astra Customizer** still requests a tiny Google Fonts stylesheet naming Syne/DM Sans (no font files download because nothing uses them). Fix in wp-admin: Appearance → Customize → Global → Typography → set Body and Headings font family to **Default System Font** (or Inherit) → Publish.
- **Meta descriptions + Open Graph:** see `docs/seo-head.md`.
- QA sheets: `docs/qa/montserrat/*.jpg`, descender close-ups `docs/qa/montserrat/descenders-closeup.jpg`.
