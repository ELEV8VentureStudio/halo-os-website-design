# SEO head tags — ready to install

Elementor Custom Code snippets created through the REST API don't render (Elementor needs its internal document type, which the API can't set), and WordPress core has no meta-description field. Two ways to install these:

- **A. Elementor > Custom Code (no plugin, ~15 min):** create one snippet per block below in wp-admin, Location = `<head>`, set the condition shown, Publish.
- **B. SEO plugin (recommended for ongoing edits):** e.g. Yoast SEO or Slim SEO; paste each description into the page's SEO box and set the default social image to the og image below.

Social share image: https://drivehalo.ai/wp-content/uploads/2026/10/halo-og.jpg (1200×630, media ID 1635)

## 1. Site-wide snippet — condition: Entire Site

```html
<link rel="preload" href="https://drivehalo.ai/wp-content/uploads/fonts/montserrat-400-800-latin.woff2" as="font" type="font/woff2" crossorigin>
<meta property="og:site_name" content="Halo">
<meta property="og:type" content="website">
<meta property="og:title" content="Halo – Dealership Command Center">
<meta property="og:description" content="Halo is the AI command center for dealer groups: one view of inventory, sales, service, marketing and retention across every rooftop. By invitation.">
<meta property="og:image" content="https://drivehalo.ai/wp-content/uploads/2026/10/halo-og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Halo: Total Command of Your Dealership.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://drivehalo.ai/wp-content/uploads/2026/10/halo-og.jpg">
```

## 2. Per-page meta descriptions — one snippet each, condition: Singular → Page → (page)

### Home — `/` (148 chars)
```html
<meta name="description" content="Halo is the AI command center for dealer groups: one view of inventory, sales, service, marketing and retention across every rooftop. By invitation.">
```

### Platform — `/platform/` (146 chars)
```html
<meta name="description" content="Six profit centers, one read on all of them. Halo watches inventory, sales, service, marketing, retention and executive KPIs across every rooftop.">
```

### The Halo Effect — `/the-halo-effect/` (147 chars)
```html
<meta name="description" content="How Halo catches a problem, prices its impact, routes it to the manager who owns the fix and tracks the outcome, in every dealership profit center.">
```

### How It Works — `/how-it-works/` (140 chars)
```html
<meta name="description" content="Connect. Identify. Act. Halo connects the systems your stores already run, flags what matters at every rooftop and tracks what happens next.">
```

### Security — `/security/` (155 chars)
```html
<meta name="description" content="Your data. Your control. Each dealer group runs in its own private environment, with role-based access, encryption, and AI that isn&#x27;t trained on your data.">
```

### About — `/about/` (158 chars)
```html
<meta name="description" content="Dealer DNA. Silicon Valley ingenuity. Meet the founders behind Halo, pairing decades of dealership leadership with deep technology and advertising experience.">
```

### FAQs — `/faqs/` (148 chars)
```html
<meta name="description" content="Straight answers about Halo: what it replaces, how setup works, which systems it connects to, starting with one store, and how your data is handled.">
```

### Wait List — `/waitlist/` (122 chars)
```html
<meta name="description" content="Halo onboards a limited number of dealer groups by invitation. Join the wait list to see Halo on your own stores&#x27; numbers.">
```

### Privacy Policy — `/privacy-policy/` (90 chars)
```html
<meta name="description" content="How Halo handles information on our website and in our platform, and the choices you have.">
```

### Terms of Use — `/terms/` (51 chars)
```html
<meta name="description" content="The terms for using drivehalo.ai, the Halo website.">
```
