# Halo OS — Launch Site Plan (R1, reconciled)

Source: client brief "HALO WEBSITE COPY — WORKING DOCUMENT R1" + live-site audit (2026-10-28).
Target: NADA 2027 launch. Revise the existing site — no rebuild.

**Flow:** Watch the video → Explore a pillar → Request a Demo.

## Sitemap

| # | Page | Slug | Job | Source content on current homepage |
|---|------|------|-----|-----------------------------------|
| 1 | Home | `/` | Video + headline + one CTA | Hero only |
| 2 | Platform | `/platform/` | Six profit centers, one benefit line each | "AI Intelligence Across Every Profit Center" cards (trim to 1 line each) |
| 3 | The Halo Effect | `/the-halo-effect/` | One worked example: issue → $ impact → action → outcome | New — needs one real or clearly-labeled example |
| 4 | How It Works | `/how-it-works/` | Connect → Identify → Act (3 steps) | "From raw data to action" (collapse 4 steps → 3) |
| 5 | Security & Governance | `/security/` | Ownership, access, AI safeguards, privacy | Security section (claims need client sign-off) |
| 6 | About Halo | `/about/` | Why Halo exists, auto expertise, leadership | New — needs story + leadership |
| 7 | FAQs | `/faqs/` | 6–8 Q&As | Existing 6 FAQs (dedupe vs. other pages) |
| — | Request a Demo | popup + `/request-a-demo/` | Single conversion point | Repurpose waitlist form |
| — | Privacy / Terms | footer | Legal | Privacy is a draft; Terms does not exist |

## Homepage

- Headline: **Total Command of Your Dealership.**
- Supporting line: **Your Dealership. Your Data. Powered by AI.**
- Primary CTA: Request a Demo · Secondary: Watch Video (only if not autoplaying)
- Video: poster image + compressed web encode; headline/CTA visible above the fold on mobile without the video
- Removed: stats band, problem lists, duplicate profit-center grids, How It Works, Security, FAQ, waitlist block

## Page template (all pillar pages)

Headline → brief explanation → one visual → key information → Request a Demo band.
One Elementor template, reused. No added sections or animations.

## Navigation

Logo · Platform · The Halo Effect · How It Works · Security · About · FAQs · **[Request a Demo]**
Below ~1200px: About + FAQs move under "More". Mobile: hamburger with Request a Demo pinned.

## Request a Demo

- Elementor Pro popup triggered from every CTA, plus a standalone page for QR codes, emails, and NADA booth traffic.
- Fields: Name, Dealership/Group, Rooftops, Role, Email, Phone.
- Routing: TBD — designated sales follow-up (email + CRM webhook).

## Design direction within the brief's constraints

The brief caps scope, so "human, not AI-generated" comes from execution, not added features:
- Keep the dark brand; drop the glow grid, pill eyebrows, and identical card rows.
- Uneven, editorial layouts; stronger type scale; teal used as a signal, not decoration.
- Real imagery: product UI, leadership photos, dealership environments.
- Plain dealer-voice copy; cut generic AI phrasing.

## Compliance fixes from the brief

- Remove the "LIVE" badge on the alerts mockup, or label it as an example ("conceptual dashboards presented as live").
- Verify or soften: "No external LLM exposure", "AI runs internally", "isolated by design" ("unverified security claims").
- Replace "Join Waitlist" with "Request a Demo" site-wide.
- Fix dead `#` links, the stray bar over the video, the empty card, the duplicated Executive View bullet, and the monospace stat text.

## Decisions (2026-10-28)

- Video: existing film (re-encoded 107 MB → 10.9 MB, 1080p). Poster = Marketing Campaigns frame.
- CTA: "Join the Wait List" site-wide → /waitlist/ (form emails hello@drivehalo.ai).
- Home: film autoplays muted full-width at the top (Sound on button restarts it with audio); menu bar sits beneath it and sticks on scroll.
- "Invite only" = sales positioning (select dealer groups), reflected in copy. All v2 pages are public (no password).
- About, Halo Effect example, Security claims: client fills via `docs/client-prompts.md`.

## Launch (2026-10-28)

- v2 Home (page 1419, slug `home`) is the WordPress front page.
- Header v2 + Footer v2 apply site-wide (Home excluded from the template header; it renders its own menu bar under the film).
- v1 header (30) / footer (77) kept but unassigned. Old homepage (10), Redesign Homepage (762), Sample Page (2) set to draft.
- Rollback: set front page back to 10, re-assign 30/77 to Entire Site, re-publish 10.

## Open items

1. Legal review: `docs/legal.md` (Privacy Policy + Terms). Needs legal entity name, mailing address, governing-law state, dedicated privacy inbox.
2. Security page: "activity log" claim depends on the admin log view shipping (client note).
3. About: verified one-line experience for Trace Przybylowicz, Phillip Rather and Alexandra Castle; headshots for all five.
4. The Halo Effect: real pilot example (Prompt 2).
5. Original unblurred `Halo-4.mp4` (media 1162) is still in the Media Library at a public URL.
