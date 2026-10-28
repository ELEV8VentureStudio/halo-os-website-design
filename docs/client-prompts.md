# Client prompts — Halo launch site

Paste each prompt into ChatGPT as-is. Answer its questions, then send the
final output back to David. Each prompt asks for a fixed format so it drops
straight into the site.

---

## Prompt 1 — About Halo page

```
You are helping me write the "About Halo" page for Halo OS (drivehalo.ai), an AI platform that unifies a dealer group's DMS, CRM, inventory, and marketing data and sends prioritized alerts across six profit centers: Inventory, Sales, Service, Marketing, Retention, and Executive View. We launch at NADA 2027. The audience is dealer principals, GMs, and dealer-group executives.

Before writing anything, interview me. Ask me these one at a time and wait for each answer:
1. What problem did you personally live through inside a dealership or dealer group that led to Halo? Give me a specific moment.
2. What did you try before building Halo, and why didn't it work?
3. What does Halo do that other tools don't?
4. Who is on the leadership team? For each person: name, title, and their most relevant automotive experience (stores run, roles held, years).
5. Is there one sentence you've said to a dealer about Halo that really landed?

Then write the page in exactly this format:

HEADLINE: (max 8 words, plain language, no AI buzzwords)
INTRO: (1–2 sentences: why Halo exists and who it's for)
FOUNDER QUOTE: (one line, in my own words from my answers)
STORY PARAGRAPH 1: (the problem we lived, max 60 words)
STORY PARAGRAPH 2: (what we tried first and why it fell short, max 60 words)
STORY PARAGRAPH 3: (what Halo does differently and who it's for, max 60 words)
LEADERSHIP: for each person: Name | Title | one line of automotive experience (max 20 words)

Rules:
- Write like a dealer talking to another dealer. Short sentences. Concrete details.
- Don't use: revolutionize, unlock, seamless, cutting-edge, game-changer, empower, leverage, synergy, "in today's fast-paced world".
- Don't invent facts. If something is missing, write [NEEDS INPUT] instead.
- No long biographies or generic company history.
```

---

## Prompt 2 — The Halo Effect (one real example)

```
You are helping me write the one example on the "The Halo Effect" page of drivehalo.ai, the website for Halo OS, an AI platform for dealer groups. The page shows ONE real situation, start to finish: what Halo detected, what it was costing, what action the team took, and the outcome Halo tracked. It has to be credible to a skeptical dealer principal.

Interview me first. Ask these one at a time and wait for each answer:
1. Which profit center did this happen in (Inventory, Sales, Service, Marketing, Retention)? Was it a pilot store, internal testing, or a customer?
2. What exactly did Halo flag? Give numbers: how many units/ROs/leads/customers, and what was wrong.
3. When was it caught (day/time, or how far into the month)?
4. What was it costing, in dollars per day, week, or month? How was that calculated?
5. Who got the alert (role), and what did they do?
6. What happened? Numbers and timeframe.
7. Can we name the store, or should it stay anonymous (e.g. "a 6-rooftop Midwest group")?

Then write it in exactly this format:

CASE LABEL: (e.g. "Used inventory · Single rooftop")
01 DETECTED, when: (short) | headline: (max 14 words, includes the number) | detail: (max 30 words)
02 IMPACT, headline: (dollar figure, max 14 words) | detail: (how it's calculated, max 30 words)
03 ACTION, sent to: (role) | headline: (what they did, max 14 words) | detail: (max 30 words)
04 OUTCOME, headline: (result with numbers and timeframe, max 14 words) | detail: (max 30 words)
IS THIS REAL DATA OR ILLUSTRATIVE?: (Real / Illustrative)

Rules:
- Use real numbers only. If I don't have one, write [NEEDS INPUT]. Never make up figures.
- If it's illustrative rather than real, say so plainly. The website will label it that way.
- Plain dealer language: no "AI-powered insights", no "unlock value".
- Don't include customer names, phone numbers, VINs, or anything personally identifiable.
```

---

## Prompt 3 — Security & Governance (claim verification)

```
You are helping me fact-check the Security & Governance page of drivehalo.ai (Halo OS, an AI platform that connects to dealer groups' DMS, CRM, inventory, and marketing systems). Every statement on this page has to be true today and defensible if a dealer's IT or compliance team asks. Unverified security claims are a legal and trust risk.

These are the statements currently on the draft page:

1. "DMS, CRM, and inventory data lives in a dealer-owned environment, kept separate from every other group."
2. "One admin panel controls access by role and by rooftop, with a full audit trail of who did what."
3. "Deal, customer, and operational data isn't sent to outside model-training pipelines."
4. "We don't sell your data or combine it with other dealer groups' data."
5. Diagram: dealer systems → Halo OS inside "your group's environment"; "Outside AI model training: not connected".

For EACH statement, ask me these questions one at a time and wait for my answers:
- Is this fully true today, partly true, or planned?
- What makes it true? (hosting provider and setup, tenant isolation, which AI/LLM providers we use and their data-retention / no-training terms, how access control and audit logs work)
- Do we have documentation, a contract term, or a certification to back it up (e.g. SOC 2, vendor DPA, zero-retention API agreement)?

Then return a table with these columns:
Statement | Status (True today / Partly / Planned) | Evidence | Recommended website wording

Rules for the recommended wording:
- If it's fully true: keep it short and plain.
- If it's partly true: narrow it to exactly what is true.
- If it's planned: remove it, or rephrase it as a commitment only if I confirm that's acceptable.
- No jargon a dealer principal wouldn't use. No absolute words like "never", "guaranteed", "bank-level", "military-grade", or "100% secure" unless I can prove them.
- Finish with any NEW statements worth adding that I've shown to be true (e.g. encryption, hosting region, SSO), plus a list of anything that should go to legal before launch.
```
