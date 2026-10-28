# DriveHalo.ai — Website Design

Redesign workspace for https://drivehalo.ai (WordPress · Astra child · Elementor Pro · SiteGround).

## Layout
- `baseline/` — snapshot of the live site before any redesign changes (2026-10-28)
  - `elementor/page-10.json` — live homepage (Elementor data + page settings)
  - `elementor/page-762.json` — "Redesign Homepage" draft page
  - `elementor/template-*.json` — header (30), footer (77), saved Homepage template (759), global kit (6)
  - `elementor/kit-6-settings.json` — global colors + typography
  - `screenshots/` — full-page desktop (1440) and mobile (390) captures
  - `theme.json`, `plugins.json` — active theme and plugin inventory

Any page can be restored by writing its `_elementor_data` back through the REST API.

## v2 build (invite-only preview)
- `theme/halo-v2.css` — design system, scoped to `.hv2`, synced into the Elementor kit custom CSS between `HALO-V2` markers.
- `build/content.py` — all page copy. `build/build.py` — creates/updates pages, menu, header/footer via REST (idempotent).
- Re-run after edits: `python3 build/build.py` (`--css-only` for style tweaks, `--dry-run` to write JSON to `build/out/` only).
- `docs/site-plan.md` — sitemap + decisions. `docs/client-prompts.md` — ChatGPT prompts for the client.
