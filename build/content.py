"""Copy for the Halo v2 launch site. Edit here, then re-run build.py.

Placeholders the client still owes are wrapped in <span class="ph">[…]</span>
so they're easy to spot on the preview and impossible to miss before launch.
"""

SITE = "https://drivehalo.ai"


def ph(s):
    return f'<span class="ph">[{s}]</span>'


# Order = header nav order = page numbering
NAV = [
    ("Platform", "platform"),
    ("The Halo Effect", "the-halo-effect"),
    ("How It Works", "how-it-works"),
    ("Security", "security"),
    ("About", "about"),
    ("FAQs", "faqs"),
]

HOME = {
    "label": "Halo OS — By invitation, for select dealer groups",
    "h1": "Total Command of Your Dealership.",
    "tagline": "Your Dealership. <em>Your Data.</em> Powered by AI.",
    "primary": "Join the Wait List",
    # Typeset wordmarks until official logo files are supplied (brand use to be confirmed).
    "works_with_label": "Works with the platforms you already run",
    "works_with": [
        ("AI & cloud", ["Google Cloud", "Vertex AI", "Gemini", "OpenAI", "Anthropic"]),
        ("Dealer systems", ["CDK Global", "Tekion", "VinSolutions", "vAuto", "DealerVault"]),
        ("Marketing", ["Google Ads", "Meta", "Microsoft Bing"]),
    ],
}

CTA_LABEL = "Join the Wait List"

CTA = {
    "h2": "See Halo on your own stores’ numbers.",
    "body": "Halo onboards a limited number of dealer groups by invitation. Join the wait list to see if yours is a fit.",
    "button": "Join the Wait List",
}

PAGES = {
    "platform": {
        "title": "Platform",
        "num": "01",
        "name": "Platform",
        "h1": "Six profit centers. One read on all of them.",
        "lead": "Halo watches the parts of the store that make or lose money every day, and tells the right person when something moves.",
        "figure": {"key": "ui-inventory", "alt": "Halo OS Inventory Tracking screen",
                   "caption": "Inventory Tracking in Halo OS. One of six profit-center views."},
        "rows": [
            {"kicker": "Inventory", "title": "Protect capital before it ages.",
             "body": "Spot units that are mispriced, stalled, or sitting at the wrong rooftop while there’s still time to act."},
            {"kicker": "Sales", "title": "Catch slipping deals early.",
             "body": "See where leads stall, follow-up lags, or pricing drifts before it shows up in the month-end number."},
            {"kicker": "Service", "title": "Find the revenue hiding in your ROs.",
             "body": "Surface one-line ROs, missed customer-pay work, and open recalls your team can still capture."},
            {"kicker": "Marketing", "title": "Know what your spend is actually doing.",
             "body": "Cost per lead, pacing, and vendor results across every channel, in one place."},
            {"kicker": "Retention", "title": "Keep customers from drifting away.",
             "body": "Know who’s going quiet, and when a service visit is the right moment for a trade conversation."},
            {"kicker": "Executive View", "title": "Run the group from one screen.",
             "body": "Every rooftop and department side by side: what changed, where, and what to do first."},
        ],
    },
    "the-halo-effect": {
        "title": "The Halo Effect",
        "num": "02",
        "name": "The Halo Effect",
        "h1": "What it looks like when Halo catches something.",
        "lead": "One example, start to finish: what Halo found, what it was costing, what the team did, and what happened next.",
        "visual_html": (
            '<div class="hv2-case-card">'
            '<div class="hv2-case-top"><span>Case · Used inventory · Single rooftop</span>'
            f'<span class="tag">Illustrative example {ph("replace with pilot data")}</span></div>'
            '<ol class="hv2-case-steps">'
            f'<li><div class="when"><b>01 Detected</b>{ph("Day / time")}</div><div>'
            f'<h3>{ph("#")} used units crossed 60 days, priced above the local market.</h3>'
            '<p>Halo’s nightly scan flagged them together because they share the same problem: priced like it’s week one, aging like it’s week nine.</p></div></li>'
            f'<li><div class="when"><b>02 Impact</b>Calculated by Halo</div><div>'
            f'<h3>About {ph("$ per day")} in holding cost, and shrinking gross every week they sit.</h3>'
            '<p>Floorplan, depreciation, and recon already spent, shown as a dollar figure the GM can act on.</p></div></li>'
            f'<li><div class="when"><b>03 Action</b>Sent to Used Car Manager</div><div>'
            f'<h3>Reprice {ph("#")} units. Move {ph("#")} to a sister store where they turn faster.</h3>'
            '<p>A short, prioritized list, sent to the person who owns the fix, not a report someone has to go find.</p></div></li>'
            f'<li><div class="when"><b>04 Outcome</b>Tracked by Halo</div><div>'
            f'<h3>{ph("#")} of {ph("#")} sold within {ph("#")} days. {ph("$")} recovered.</h3>'
            '<p>Halo follows each unit until it’s sold and records what worked, so the next alert is sharper.</p></div></li>'
            '</ol></div>'
        ),
        "visual_caption": "Every Halo alert follows the same path: detected, priced, assigned, tracked.",
        "rows_intro": "The same loop runs in every profit center.",
        "rows": [
            {"kicker": "Service", "title": "A one-line RO trend at one store.",
             "body": "Flagged by advisor, with the customer-pay work that’s being left on the table."},
            {"kicker": "Marketing", "title": "A channel spending ahead of results.",
             "body": "Caught mid-month, while there’s still budget to move."},
            {"kicker": "Retention", "title": "Customers going quiet after the sale.",
             "body": "Surfaced before they book service somewhere else."},
        ],
    },
    "how-it-works": {
        "title": "How It Works",
        "num": "03",
        "name": "How It Works",
        "h1": "Connect. Identify. Act.",
        "lead": "Halo pulls the data your stores already create into one place, scans every rooftop for what matters, and tells your team where to focus first.",
        "figure": {"key": "ui-sales", "alt": "Halo OS Sales Dashboard screen",
                   "caption": "One view across every rooftop, built from the systems you already run."},
        "rows": [
            {"kicker": "Step one", "title": "Connect your sources.",
             "body": "Halo brings together the systems you already run (DMS, CRM, inventory, and marketing) into one clean, dealer-mapped view of the business. Nothing gets replaced."},
            {"kicker": "Step two", "title": "Identify what matters.",
             "body": "AI agents watch every rooftop at once: pace to goal, inventory health, service capture, marketing performance, and retention, so problems surface before month-end."},
            {"kicker": "Step three", "title": "Act on it.",
             "body": "Prioritized alerts, not reports, go to the people who own the fix, showing what changed, why it matters, and what to do next. Halo tracks the outcome so every signal gets sharper."},
        ],
    },
    "security": {
        "title": "Security & Governance",
        "num": "04",
        "name": "Security & Governance",
        "h1": "Your data. Your control.",
        "lead": "Dealer groups should ask hard questions before connecting anything to their DMS. Here are our answers.",
        "visual_html": (
            '<div class="hv2-diagram hv2-diagram--v2" role="img" aria-label="Your systems feed Halo OS inside your group’s private environment, managed by Halo. AI requests go out to Google Cloud and come back, and are not used for training.">'
            '<div class="env"><span class="t">Your group’s private environment, managed by Halo</span>'
            '<div class="srcs"><div class="src">DMS</div><div class="src">CRM</div><div class="src">Inventory</div><div class="src">Marketing</div></div>'
            '<div class="flow">↓</div>'
            '<div class="core">Halo OS · alerts, actions, activity log</div></div>'
            '<div class="link" aria-hidden="true">⇄</div>'
            '<div class="ext"><b>AI processing</b>via Google Cloud<span>Not used for training</span></div>'
            '</div>'
        ),
        "visual_caption": "How your data flows. Halo runs inside your group’s own environment. AI requests go to Google Cloud and come back, and aren’t used to train models.",
        "rows": [
            {"kicker": "Isolation", "title": "Your own private environment.",
             "body": "Every dealer group runs in its own private Google Cloud environment. Your DMS, CRM and inventory data is stored there, separate from every other dealer group."},
            {"kicker": "Access", "title": "You decide who sees what.",
             "body": "One admin panel controls who can see what, by role and by rooftop, with an activity log of who did what. Two-factor login protects every account."},
            {"kicker": "AI safeguards", "title": "Your data doesn’t train AI models.",
             "body": "Your deal, customer and operational data isn’t used to train AI models. Halo’s AI runs through Google Cloud, under terms that exclude training on customer data."},
            {"kicker": "Privacy", "title": "We don’t sell your data.",
             "body": "Your store’s operations aren’t shared with or used to help other dealer groups. Benchmarks come from industry sources and may include anonymized, combined data."},
            {"kicker": "Encryption", "title": "Encrypted and hosted in the U.S.",
             "body": "Your data is encrypted in storage and in transit, and hosted in the United States."},
            {"kicker": "Deployment", "title": "Your cloud, or your servers.",
             "body": "Want it in your own cloud account? We’ll set Halo up in your group’s own Google Cloud or AWS account. Prefer AI on your own servers? We can set up a private AI model that runs entirely on your infrastructure."},
        ],
    },
    "about": {
        "title": "About Halo",
        "num": "05",
        "name": "About Halo",
        "h1": "Built by Dealers. For Dealers.",
        "lead": "Halo was born from firsthand experience with the operational challenges of running dealerships. We built it to give dealer principals, GMs, and executive teams greater visibility, faster decisions, and more control over profitability.",
        "story": {
            "quote": "<p>“We built Halo because we lived that tension. We saw how information lag quietly drains profitability. We saw how fragmentation forces reactive leadership. And we believed there was a better operating standard.”</p>",
            "body": ("<p>We know what it’s like to run a dealership across 10 to 30 different platforms. Disconnected systems. Departmental silos. Endless reporting. By the time problems reach leadership, the damage is often done. Aging inventory ties up capital. Marketing dollars go to waste. Sales opportunities disappear. Fragmentation quietly erodes profitability.</p>"
                     "<p>Like most dealers, we relied on more platforms, more dashboards, manual reports, and additional staffing to manage growing complexity. But more technology didn’t mean better visibility. More reporting didn’t mean faster decisions. The result was fragmented operations, rising costs, slower execution, and increasing pressure on margins. We knew there had to be a better way.</p>"
                     "<p>That’s why we built Halo. One command center connecting dealership data across Inventory, Sales, Service, Marketing, Retention, and Executive View. Halo continuously identifies risks, prioritizes opportunities, and tells your team what changed, why it matters, and what to do next. Less time chasing reports. More time running a profitable business.</p>"),
            "people_title": "Leadership",
            "people": [
                # (name, title, experience or "" until verified)
                ("Trace Przybylowicz", "Managing Partner", ""),
                ("Joe Castle", "Managing Partner", "Founder and CEO of Castle Automotive Group, with extensive automotive retail leadership experience."),
                ("David Ortiz", "Managing Partner",
                 "30+ year automotive operator, entrepreneur, and builder. He leads sales and marketing across 18 Castle Automotive Group rooftops and has founded ventures spanning dealership marketing, analytics, and AI, bringing the operator’s view and the builder’s toolkit to Halo."),
                ("Phillip Rather", "Managing Partner", ""),
                ("Alexandra Castle", "Managing Partner", ""),
            ],
        },
    },
    "faqs": {
        "title": "FAQs",
        "num": "06",
        "name": "FAQs",
        "h1": "Straight answers.",
        "lead": "The questions dealers ask us most. If yours isn’t here, bring it to the demo.",
        "body_html": None,  # filled below
    },
}

FAQS = [
    ("Does Halo replace my DMS, CRM, or inventory tools?",
     "No. Halo connects to the tools you already use and makes sense of them together. Nothing gets ripped out, and your team keeps working in the systems they know."),
    ("Is this another dashboard my team has to check?",
     "No. Halo sends prioritized alerts to the person who owns each fix. The point is that nobody has to go digging."),
    ("Can we start with one store?",
     "Yes. Start with a single rooftop, prove the value, then add stores at your pace. The group view fills in as more rooftops connect."),
    ("How long does setup take?",
     "It depends on your systems and number of rooftops. We handle the integration work, so your team’s lift is light: a few confirmations, not a project."),
    ("Which systems does Halo connect to?",
     "The systems that run your stores: DMS, CRM, inventory, and marketing platforms, with more being added. Bring your list and we’ll walk through it with you."),
    ("Can we set alerts to match how we run our stores?",
     "Yes. Thresholds, targets, and who gets which alert are set per rooftop and per group, and Halo learns your baselines over time."),
    ("What happens to our data?",
     f'It stays in its own isolated environment, separate from every other dealer group. We don’t sell it, and it isn’t used to train AI models. See <a href="{SITE}/security/">Security &amp; Governance</a> for the details.'),
]

PAGES["faqs"]["body_html"] = '<div class="hv2-faq">' + "".join(
    f'<details><summary><span class="n">{i:02d}</span><span>{q}</span></summary><div class="a"><p>{a}</p></div></details>'
    for i, (q, a) in enumerate(FAQS, 1)) + "</div>"

DEMO = {
    "label": "Wait list · By invitation",
    "h1": "See Halo on your own numbers.",
    "lead": "Halo is invite-only. We onboard a limited number of dealer groups at a time so every rollout gets the attention it needs. Join the wait list and tell us about your group.",
    "next": [
        "A real person reviews every request. No automated drip.",
        "If your group is a fit, we’ll reach out with an invitation and a walkthrough.",
        "The walkthrough focuses on your stores, not a canned slide deck.",
    ],
    "button": "Join the Wait List",
    "success": "You’re on the list. If your group is a fit, we’ll reach out with an invitation.",
}

FOOTER = {
    "tagline": "Your Dealership. Your Data. Powered by AI.",
    "cols": [
        {"title": "Product", "links": [("Platform", f"{SITE}/platform/"), ("The Halo Effect", f"{SITE}/the-halo-effect/"),
                                        ("How It Works", f"{SITE}/how-it-works/"), ("Security", f"{SITE}/security/")]},
        {"title": "Company", "links": [("About", f"{SITE}/about/"), ("FAQs", f"{SITE}/faqs/"),
                                        ("Join the Wait List", f"{SITE}/waitlist/")]},
        {"title": "Legal", "links": [("Privacy Policy", f"{SITE}/privacy-policy/"), ("Terms of Use", f"{SITE}/terms/")]},
    ],
    "legal": "© 2026 Halo OS. All rights reserved.",
    "domain": "drivehalo.ai",
}


# --------------------------------------------------------------------------
# Legal pages — client copy ("halo-security-privacy-terms.md", Oct 28 2026),
# drafts for legal review. Placeholders resolved for the live site:
#   [Halo legal entity] -> "Halo OS"   [privacy email]/[Email] -> LEGAL_CONTACT
#   [Mailing address], governing-law [state] -> omitted until provided
# Correction: client draft said the site uses Google Analytics. It doesn't
# (checked 2026-10-28): Cloudflare Web Analytics (cookieless) + Google Fonts.
# --------------------------------------------------------------------------
LEGAL_UPDATED = "January 2026"
LEGAL_CONTACT = "hello@drivehalo.ai"
MAIL = f'<a href="mailto:{LEGAL_CONTACT}">{LEGAL_CONTACT}</a>'

PRIVACY_SECTIONS = [
    ("Who we are", """
<p>Halo OS (“Halo,” “we”) provides an AI operating system for automotive dealers. This policy explains how we handle information on our website and in our platform.</p>"""),
    ("Two kinds of information", """
<ul>
<li><strong>Information about you as a website visitor or user:</strong> your name, work email, phone number, company, role, and number of rooftops when you join the wait list, and how you use our website and platform.</li>
<li><strong>Dealer data:</strong> information our dealer customers connect to Halo, such as deal, vehicle, customer and operational data. We process it on behalf of our dealer customers, under our contracts with them. If you’re a car buyer whose information a dealer holds, contact that dealer.</li>
</ul>"""),
    ("How we use information", """
<ul>
<li>To provide, secure and support the Halo platform</li>
<li>To respond to inquiries and requests for early access</li>
<li>To improve our website and platform</li>
<li>To create anonymized, combined industry benchmarks that don’t identify any dealer, store or person</li>
</ul>"""),
    ("What we don’t do", """
<ul>
<li>We don’t sell personal information or dealer data.</li>
<li>We don’t share one dealer group’s data with another, or use a group’s specific operations to help another group.</li>
<li>Dealer data isn’t used to train AI models. Our AI runs through Google Cloud, under terms that exclude training on customer data.</li>
</ul>"""),
    ("Who we share information with", """
<p>Only service providers that help us run Halo, such as Google Cloud for hosting and AI processing, under contracts that limit how they use it. We may also disclose information if the law requires it, or as part of a merger or acquisition, subject to this policy.</p>"""),
    ("Security", f"""
<p>Each dealer group’s data is kept in its own isolated environment in the United States, encrypted in storage and in transit, and protected by two-factor login and role-based access. See our <a href="{SITE}/security/">Security &amp; Governance</a> page.</p>"""),
    ("Retention", """
<p>We keep dealer data for the length of our contract with the dealer, then return and delete it as the contract provides. We keep website and account information as long as needed for the purposes above.</p>"""),
    ("Your choices and rights", f"""
<p>You can ask to access, correct or delete your personal information, or opt out of marketing emails, by contacting {MAIL}. Depending on where you live, you may have more rights under state law.</p>"""),
    ("Cookies and analytics", """
<p>Our website uses Cloudflare Web Analytics, a privacy-focused tool that doesn’t use cookies, to understand how visitors use it. The site also loads fonts from Google Fonts, which shares your IP address with Google when a page loads.</p>"""),
    ("Contact", f"<p>{MAIL}</p>"),
]

TERMS_SECTIONS = [
    ("Agreement to these terms", """
<p>By using drivehalo.ai (the “Site”), you agree to these Terms of Use. If you don’t agree, don’t use the Site. The Site is operated by Halo OS (“Halo,” “we”).</p>"""),
    ("The Halo platform", """
<p>These terms cover the Site only. Use of the Halo platform is governed by your organization’s agreement with Halo, which controls if it conflicts with these terms.</p>"""),
    ("Using the Site", """
<p>You may use the Site to learn about Halo and contact us. You agree not to:</p>
<ul>
<li>Copy, scrape or resell the Site’s content</li>
<li>Interfere with the Site’s operation or security</li>
<li>Try to access parts of the Site or Halo’s systems you aren’t authorized to use</li>
<li>Submit false information, or information you don’t have the right to share</li>
</ul>"""),
    ("Early access and inquiries", f"""
<p>If you request early access, a demo or more information, what you submit must be accurate. We handle it as described in our <a href="{SITE}/privacy-policy/">Privacy Policy</a>.</p>"""),
    ("Our content", """
<p>The Site’s text, design, logos and graphics belong to Halo or its licensors. The Halo name and logo are Halo’s trademarks and may not be used without our written permission.</p>"""),
    ("Third-party links", """
<p>The Site may link to other websites. We don’t control them and aren’t responsible for their content or practices.</p>"""),
    ("Disclaimers", """
<p>The Site and its content are provided “as is” for general information. We work to keep it accurate but don’t promise it is complete, current or error-free.</p>"""),
    ("Limitation of liability", """
<p>To the extent the law allows, Halo isn’t liable for indirect, incidental or consequential damages arising from your use of the Site.</p>"""),
    ("Changes", """
<p>We may update these terms. The date below shows when they last changed. Continuing to use the Site means you accept the updated terms.</p>"""),
    # ("Governing law", "<p>These terms are governed by the laws of [state].</p>"),  # pending legal
    ("Contact", f"<p>{MAIL}</p>"),
]


def legal_html(sections):
    return '<div class="hv2-legal">' + "".join(
        f'<section><h2><span class="n">{i:02d}</span>{h}</h2>{body}</section>'
        for i, (h, body) in enumerate(sections, 1)
    ) + f'<p class="updated">Last updated: {LEGAL_UPDATED}</p></div>'


PAGES["privacy-policy"] = {
    "title": "Privacy Policy", "num": "", "name": "Legal", "h1": "Privacy Policy",
    "lead": "How Halo handles information on our website and in our platform, and the choices you have.",
    "cta": False, "legal_html": legal_html(PRIVACY_SECTIONS),
}
PAGES["terms"] = {
    "title": "Terms of Use", "num": "", "name": "Legal", "h1": "Terms of Use",
    "lead": "The rules for using drivehalo.ai. Use of the Halo platform itself is covered by your organization’s agreement with Halo.",
    "cta": False, "legal_html": legal_html(TERMS_SECTIONS),
}
