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
            '<div class="hv2-diagram" role="img" aria-label="Your systems feed Halo inside an environment your group controls. Outside AI model training is not connected.">'
            '<div class="env"><span class="t">Your group’s environment</span>'
            '<div class="srcs"><div class="src">DMS</div><div class="src">CRM</div><div class="src">Inventory</div><div class="src">Marketing</div></div>'
            '<div class="flow">↓</div>'
            '<div class="core">Halo OS · alerts, actions, audit trail</div></div>'
            '<div class="out"><s>Outside AI model training</s><br>not connected</div>'
            '</div>'
        ),
        "visual_caption": f"How your data flows. {ph('Client to confirm all statements on this page before launch')}",
        "rows": [
            {"kicker": "Ownership", "title": "Your data stays yours.",
             "body": "DMS, CRM, and inventory data lives in a dealer-owned environment, kept separate from every other group."},
            {"kicker": "Access", "title": "You decide who sees what.",
             "body": "One admin panel controls access by role and by rooftop, with a full audit trail of who did what."},
            {"kicker": "AI safeguards", "title": "Your data doesn’t train anyone else’s AI.",
             "body": "Deal, customer, and operational data isn’t sent to outside model-training pipelines."},
            {"kicker": "Privacy", "title": "No selling. No pooling.",
             "body": "We don’t sell your data or combine it with other dealer groups’ data."},
        ],
    },
    "about": {
        "title": "About Halo",
        "num": "05",
        "name": "About Halo",
        "h1": f"Built by people who’ve run dealerships. {ph('client headline')}",
        "lead": f"{ph('One or two sentences: why Halo exists and who it’s for.')}",
        "story": {
            "quote": f"<p>{ph('Founder quote, one line, in their own words')}</p>",
            "body": (f"<p>{ph('Paragraph 1: the problem the founders lived inside a dealer group.')}</p>"
                     f"<p>{ph('Paragraph 2: what they tried first, and why it didn’t work.')}</p>"
                     f"<p>{ph('Paragraph 3: what Halo does differently, and who it’s built for.')}</p>"),
            "people_html": (
                '<div class="hv2-people">' + "".join(
                    '<div class="hv2-person"><div class="photo">Headshot</div>'
                    f'<h3>{ph("Name")}</h3><p class="role">{ph("Title")}</p>'
                    f'<p>{ph("One line of relevant automotive experience.")}</p></div>'
                    for _ in range(3)) + '</div>'
            ),
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
    ("Who owns the data?",
     f'You do. See <a href="{SITE}/security/">Security &amp; Governance</a> for how it’s stored, who can access it, and how AI is handled.'),
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
