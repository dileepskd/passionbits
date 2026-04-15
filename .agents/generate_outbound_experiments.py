#!/usr/bin/env python3
"""Generate Passionbits Outbound Experiments + Training Plan PDF."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "passionbits-outbound-experiments.pdf")

PRIMARY = HexColor("#0f172a")
ACCENT = HexColor("#e94560")
MUTED = HexColor("#64748b")
LIGHT = HexColor("#f1f5f9")
BORDER = HexColor("#cbd5e1")
BLUE = HexColor("#2563eb")
GREEN = HexColor("#059669")
DARK_HEAD = HexColor("#1e293b")

styles = getSampleStyleSheet()

def add(name, **kw):
    if name in styles.byName:
        del styles.byName[name]
    styles.add(ParagraphStyle(name, parent=styles["Normal"], **kw))

add("CoverTitle", fontSize=30, leading=36, textColor=PRIMARY, spaceAfter=6, alignment=TA_LEFT, fontName="Helvetica-Bold")
add("CoverSub", fontSize=14, leading=18, textColor=MUTED, spaceAfter=20)
add("H1", fontSize=22, leading=26, textColor=PRIMARY, spaceBefore=18, spaceAfter=10, fontName="Helvetica-Bold")
add("H2", fontSize=16, leading=20, textColor=ACCENT, spaceBefore=14, spaceAfter=8, fontName="Helvetica-Bold")
add("H3", fontSize=13, leading=17, textColor=DARK_HEAD, spaceBefore=10, spaceAfter=6, fontName="Helvetica-Bold")
add("H4", fontSize=11, leading=15, textColor=BLUE, spaceBefore=8, spaceAfter=4, fontName="Helvetica-Bold")
add("Body", fontSize=10, leading=14, textColor=PRIMARY, spaceAfter=6, alignment=TA_LEFT)
add("Mono", fontSize=9.5, leading=13, textColor=PRIMARY, spaceAfter=6, fontName="Helvetica", backColor=LIGHT, borderPadding=(6,8,6,8), leftIndent=0)
add("Small", fontSize=9, leading=12, textColor=MUTED, spaceAfter=4)
add("Label", fontSize=9, leading=12, textColor=MUTED, fontName="Helvetica-Bold", spaceAfter=2)

story = []

def p(text, style="Body"):
    story.append(Paragraph(text, styles[style]))

def sp(h=6):
    story.append(Spacer(1, h))

def hr():
    story.append(HRFlowable(width="100%", thickness=0.7, color=BORDER, spaceBefore=8, spaceAfter=8))

def pb():
    story.append(PageBreak())

def icp_table(rows):
    t = Table(rows, colWidths=[55*mm, 115*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), LIGHT),
        ("TEXTCOLOR", (0,0), (0,-1), DARK_HEAD),
        ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
        ("FONTNAME", (1,0), (1,-1), "Helvetica"),
        ("FONTSIZE", (0,0), (-1,-1), 9.5),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("BOX", (0,0), (-1,-1), 0.5, BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.3, BORDER),
    ]))
    story.append(t)
    sp(6)

def ab_table(rows, headers=None):
    data = []
    if headers:
        data.append(headers)
    data.extend(rows)
    col_widths = [18*mm] + [(170-18)/max(1,len(rows[0])-1)*mm]*(len(rows[0])-1)
    t = Table(data, colWidths=col_widths)
    style = [
        ("FONTSIZE", (0,0), (-1,-1), 9),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("BOX", (0,0), (-1,-1), 0.5, BORDER),
        ("INNERGRID", (0,0), (-1,-1), 0.3, BORDER),
    ]
    if headers:
        style += [
            ("BACKGROUND", (0,0), (-1,0), DARK_HEAD),
            ("TEXTCOLOR", (0,0), (-1,0), HexColor("#ffffff")),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ]
    style += [
        ("BACKGROUND", (0, 1 if headers else 0), (0,-1), LIGHT),
        ("FONTNAME", (0, 1 if headers else 0), (0,-1), "Helvetica-Bold"),
    ]
    t.setStyle(TableStyle(style))
    story.append(t)
    sp(6)

# ========== COVER ==========
p("Passionbits Outbound Experiments", "CoverTitle")
p("ICPs, Messaging, A/B/C/D Variants + Training Plan", "CoverSub")
p("Prepared: 2026-04-15 &nbsp;&nbsp;|&nbsp;&nbsp; Goal: 10–15 meetings / week", "Small")
hr()
p("This document covers 10 outbound experiments mapped to the framework "
  "(Company size, Funding, Geography, Signals, Role, Jobs to be done, Messaging, Sequences). "
  "Each experiment includes a 150-word Email and LinkedIn message, A/B subject-line tests, "
  "and A/B/C/D variants for CTA and value prop. A training plan for the show sits at the end.", "Body")
sp(10)

# How to read
p("How to read each experiment", "H3")
p("<b>ICP</b> — industry, size, revenue, location, technographics, pain, goals.<br/>"
  "<b>Buyer Persona</b> — role(s), responsibilities, motivations, JTBD.<br/>"
  "<b>Signals</b> — the exact trigger that qualifies an account for this experiment.<br/>"
  "<b>Messaging</b> — a 150-word email + 150-word LinkedIn note. First line is always "
  "<b>[PERSONALIZATION]</b> (replaced at send-time). Subject lines are A/B. CTAs and value "
  "props are tested A/B/C/D independently of the body.<br/>"
  "<b>Sequence</b> — 4-touch cadence across email + LinkedIn.", "Body")
pb()

# ================================================================
# EXPERIMENT BUILDER
# ================================================================
def experiment(num, title, tagline, icp, persona, signals, jtbd,
               subj_email, subj_li, email_body, li_body,
               ctas, vprops, sequence, notes=None):
    p(f"Experiment {num} — {title}", "H1")
    p(tagline, "Small")
    hr()

    p("ICP (Ideal Customer Profile)", "H2")
    icp_table([
        ["Industry", icp["industry"]],
        ["Company size", icp["size"]],
        ["Revenue", icp["revenue"]],
        ["Funding", icp["funding"]],
        ["Geography", icp["geo"]],
        ["Technographics", icp["tech"]],
        ["Pain points", icp["pain"]],
        ["Goals", icp["goals"]],
    ])

    p("Buyer Persona", "H2")
    icp_table([
        ["Job titles", persona["titles"]],
        ["Responsibilities", persona["responsibilities"]],
        ["Motivations", persona["motivations"]],
        ["Challenges", persona["challenges"]],
        ["Buying process", persona["buying"]],
    ])

    p("Signals (qualifier triggers)", "H2")
    for s in signals:
        p(f"&bull; {s}", "Body")

    p("Jobs to be done", "H2")
    for j in jtbd:
        p(f"&bull; {j}", "Body")

    p("Subject lines — A/B test", "H2")
    ab_table([
        ["Email A", subj_email[0]],
        ["Email B", subj_email[1]],
        ["LinkedIn A", subj_li[0]],
        ["LinkedIn B", subj_li[1]],
    ], headers=["Channel", "Subject / Connection note"])

    p("Email — 150 words", "H2")
    p(email_body.replace("\n", "<br/>"), "Mono")

    p("LinkedIn DM — 150 words", "H2")
    p(li_body.replace("\n", "<br/>"), "Mono")

    p("CTA — A/B/C/D test", "H2")
    ab_table([
        ["A", ctas[0]],
        ["B", ctas[1]],
        ["C", ctas[2]],
        ["D", ctas[3]],
    ], headers=["Variant", "CTA"])

    p("Value Prop — A/B/C/D test", "H2")
    ab_table([
        ["A", vprops[0]],
        ["B", vprops[1]],
        ["C", vprops[2]],
        ["D", vprops[3]],
    ], headers=["Variant", "Value prop one-liner"])

    p("Sequence (4 touches)", "H2")
    for i, s in enumerate(sequence, 1):
        p(f"<b>Day {s['day']} &middot; {s['channel']}</b> — {s['angle']}", "Body")
        p(s["note"], "Small")

    if notes:
        p("Notes", "H2")
        p(notes, "Body")

    pb()

# ================================================================
# EXPERIMENT 1 — ROSHAN'S CONNECTIONS
# ================================================================
experiment(
    num=1,
    title="Roshan's 1st-degree connections",
    tagline="Warm intros + peer-to-peer outreach leveraging Roshan's founder/CMO network on LinkedIn.",
    icp={
        "industry": "Mixed — D2C, SaaS, agency, consumer apps (whatever Roshan's network includes)",
        "size": "20–500 employees",
        "revenue": "$1M–$100M ARR / revenue",
        "funding": "Seed to Series C",
        "geo": "India + US primary, UK/SEA secondary",
        "tech": "Meta Ads Manager, Shopify / HubSpot / Segment, creator tools",
        "pain": "Creative velocity vs. ad spend; limited visibility into what competitors ship weekly",
        "goals": "Scale paid + organic without ballooning creative cost",
    },
    persona={
        "titles": "Founder, CEO, CMO, Head of Growth, Head of Marketing",
        "responsibilities": "Own revenue, marketing P&L, brand + performance",
        "motivations": "Move fast, beat category incumbents, avoid burning budget on wrong creative",
        "challenges": "Don't have time to audit every competitor; rely on gut for creative calls",
        "buying": "Founder-led; 1 demo → pilot → contract. 2–3 week cycle.",
    },
    signals=[
        "1st-degree connection of Roshan on LinkedIn",
        "Engaged with Roshan's last 3 posts OR mutual in 2+ WhatsApp/founder groups",
        "Company has 10+ live Meta ads OR clear UGC/testimonial gap on site",
    ],
    jtbd=[
        "Find the next creative that will scale without losing 2 weeks to shoots",
        "Know what competitors are running, weekly",
        "Produce 30+ variants/month without hiring in-house video",
    ],
    subj_email=["Roshan mentioned you", "quick one — via Roshan"],
    subj_li=["Roshan connect", "via Roshan"],
    email_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. 'Loved your take on the pricing rework Roshan shared last week — "
        "the 3-tier collapse is exactly what we're seeing work for [their category].']\n\n"
        "Roshan and I have been comparing notes on how brands like [Company] are scaling creative "
        "without scaling headcount. He thought it'd be worth a quick intro.\n\n"
        "We run Passionbits — it pulls your competitors' live ads + your own experiment history "
        "and produces 30–100 video variants/month via 6,000 vetted creators. Two Shark Tank India "
        "brands + a handful of US D2C teams are on it.\n\n"
        "If you're testing more than 20 variants/month — or wish you were — I'd love 15 mins to "
        "show you what [top competitor] shipped last week and where your creative gap is.\n\n"
        "Reply 'send it' and I'll share the snapshot before we talk.\n\n"
        "— [Sender]"
    ),
    li_body=(
        "Hi [First Name] — saw we're both connected to Roshan.\n\n"
        "[PERSONALIZATION — e.g. 'Your comment on Roshan's post about UGC burnout was spot on — "
        "we see the same pattern in [their category].']\n\n"
        "Short version: we pull your category's live ad library + your ad history and show you "
        "exactly which formats are working that your team hasn't tested yet — then produce them "
        "via 6,000 creators globally. Useful if your top creative has been running 60+ days.\n\n"
        "Happy to send a free competitor snapshot for [Company] — no call needed unless it's "
        "actually useful. Worth pinging?"
    ),
    ctas=[
        "Reply 'send it' and I'll share a free competitor creative snapshot within 24 hours",
        "Open to 15 mins next week? I'll bring [top competitor]'s last 30 days of ads",
        "Want me to just send the snapshot and you decide if a call makes sense?",
        "Worth a quick Loom walkthrough of your category's top performers?",
    ],
    vprops=[
        "See your competitors' live ads + your own experiment history, in one dashboard",
        "Know what to shoot next — before you spend another ₹10L on ads that won't work",
        "30–100 video variants a month via 6,000 creators, at a fraction of agency cost",
        "The only platform that tells you what to make AND makes it",
    ],
    sequence=[
        {"day": 1, "channel": "LinkedIn connect + note", "angle": "Mutual (Roshan) + specific observation", "note": "Plain connect with 150-word note above. No pitch link."},
        {"day": 3, "channel": "Email #1", "angle": "Competitor snapshot offer", "note": "Send email above. Subject A on Tuesday, Subject B on Thursday."},
        {"day": 7, "channel": "LinkedIn DM follow-up", "angle": "Send the snapshot itself (free, no call)", "note": "Attach 1-page PDF with 3 competitor ad screenshots + annotation."},
        {"day": 12, "channel": "Email breakup", "angle": "Soft close — 'last note'", "note": "2-line. 'If timing is off, happy to circle back in Q3.' No CTA."},
    ],
)

# ================================================================
# EXPERIMENT 2 — INDIAN BRANDS EXPANDING TO US
# ================================================================
experiment(
    num=2,
    title="Indian brands expanding to the US",
    tagline="Indian D2C / SaaS / consumer brands that have opened a US entity or run US-targeted ads.",
    icp={
        "industry": "D2C consumer, SaaS, consumer apps (India-origin)",
        "size": "50–500 employees (India) + 5–30 (US office)",
        "revenue": "₹25Cr–₹500Cr India + <$5M US ARR",
        "funding": "Series A–C, recent US-market round preferred",
        "geo": "HQ India (Bangalore/Delhi/Mumbai) — expanding to US",
        "tech": "Meta + TikTok ads, Shopify US store, Klaviyo, US landing stack",
        "pain": "Can't shoot US-native content from India — flights cost more than the pilot",
        "goals": "Build US brand equity without a US crew; localise creative cheaply",
    },
    persona={
        "titles": "CMO, VP International, Head of US Marketing, Global Growth Lead",
        "responsibilities": "Launch + scale US GTM, build US brand equity, manage India-US creative",
        "motivations": "Hit US CAC targets, prove US unit economics to the board",
        "challenges": "Indian creative doesn't translate — accent, context, setting all feel 'off'",
        "buying": "CMO-led, fast (4–6 weeks) if pilot delivers in week 1",
    },
    signals=[
        "Just announced US expansion OR registered US entity (OpenCorporates / Crunchbase)",
        "Hiring 'US Marketing Manager' / 'US Content Lead' on LinkedIn in last 90 days",
        "Running Meta ads geo-targeted to US in Ads Library with India-shot creative",
        "Raised capital explicitly for US expansion",
    ],
    jtbd=[
        "Ship US-native UGC without flying a team or opening a US studio",
        "Test 10+ US creative variants in month 1 of launch",
        "Localise hooks, accents, settings to match US viewer expectations",
    ],
    subj_email=["US creative — Indian brands", "about your US launch"],
    subj_li=["India → US creative", "US launch note"],
    email_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. 'Saw the press release on [Company]'s US launch — congrats. "
        "Noticed you're running 6 Meta ads geo-targeted to the US but all shot in Mumbai.']\n\n"
        "That usually doesn't work past the pilot budget — US viewers clock non-native in 2 "
        "seconds and CPMs punish it.\n\n"
        "We've helped 4 Indian brands (2 Shark Tank alums) produce US-native UGC without "
        "sending anyone on a flight. US creators, US homes, US voiceovers — briefed and "
        "delivered in 5–7 days, starting at $49/video. Our network has 2,000+ US creators "
        "vetted by niche.\n\n"
        "For a brand in your category, we'd shoot 10 variants against your top 3 hooks in "
        "week 1 — and you'd see CPM drop in week 2.\n\n"
        "Worth 15 mins to show you what we did for [comparable Indian brand]?\n\n"
        "— [Sender]"
    ),
    li_body=(
        "Hi [First Name] — congrats on the US push.\n\n"
        "[PERSONALIZATION — e.g. 'Your LinkedIn post on building the US team from scratch "
        "hit — specifically the line about creative being the bottleneck.']\n\n"
        "Quick one: we run the production layer for Indian brands launching in the US — "
        "2,000+ vetted US creators, $49–$199/video, 5–7 day delivery. No flights, no crew, "
        "no agency markup. Two Shark Tank alums use us for all their US creative.\n\n"
        "Want me to send the 10-variant pilot menu + sample US UGC from your category?"
    ),
    ctas=[
        "15 mins this week — I'll show you 3 US UGC samples from your category",
        "Want the pilot menu? 10 US-shot variants in 5 days, $490 total",
        "Reply 'samples' and I'll send US creator work in [their vertical]",
        "Book directly: [calendar link] — your slot, your time zone",
    ],
    vprops=[
        "US-native UGC without flying a crew — shot by 2,000+ vetted US creators",
        "Localise hooks, accents, settings in 5–7 days for under $200/video",
        "The production stack Indian brands use to launch in the US without a US office",
        "Every US creative shot by someone who lives there — zero accent/context mismatch",
    ],
    sequence=[
        {"day": 1, "channel": "LinkedIn connect + note", "angle": "Congrats + US launch observation", "note": "Connect with 120-char context. No pitch in note."},
        {"day": 2, "channel": "Email #1", "angle": "US-native creative gap", "note": "Reference specific geo-targeted ad from their library."},
        {"day": 6, "channel": "LinkedIn DM", "angle": "Sample pack — 3 US UGC clips from their vertical", "note": "Attach or link Dropbox/Drive of 3 reference clips."},
        {"day": 11, "channel": "Email #2 / breakup", "angle": "Case study: comparable Indian brand's US CPM drop", "note": "1 stat, 1 link, 1 CTA."},
    ],
)

# ================================================================
# EXPERIMENT 3 — EVENT SPONSORS → B2B
# ================================================================
experiment(
    num=3,
    title="Event sponsors & exhibitors — Event → B2B",
    tagline="B2B companies exhibiting / sponsoring at major industry events who need event-day video assets.",
    icp={
        "industry": "B2B SaaS, fintech, HR tech, devtools, martech",
        "size": "50–2000 employees",
        "revenue": "$5M–$500M ARR",
        "funding": "Series A–D",
        "geo": "US, UK, Middle East (Dubai), India (SaaSBoomi, Nasscom)",
        "tech": "HubSpot / Salesforce, event platform (Cvent, Bizzabo), LinkedIn Ads",
        "pain": "Spent $50K–$500K on the booth; walking away with 3 blurry iPhone clips",
        "goals": "Turn the event into 10–15 shareable assets within 48 hours",
    },
    persona={
        "titles": "Event Marketing Manager, Field Marketing, Brand Manager, Demand Gen Lead",
        "responsibilities": "Event P&L, pipeline sourced from events, post-event content",
        "motivations": "Justify the booth spend internally, feed sales enablement, extend reach",
        "challenges": "2–3 person team on-site, no bandwidth for full videography, vendors ghost",
        "buying": "Tactical — can sign for <$2K/event on their own card, no procurement.",
    },
    signals=[
        "Listed as sponsor/exhibitor on upcoming conference site (SaaStr, Dreamforce, HubSpot Inbound, Web Summit, Gitex, Money20/20, Nasscom, SaaSBoomi)",
        "Hiring 'Event Marketing' role in last 6 months",
        "Posted a 'we'll be at [event]' LinkedIn post with a booth number",
        "Previous events had text-only recaps, no video",
    ],
    jtbd=[
        "Get 10–15 event-day video assets shot, edited, delivered within 48 hours",
        "Pre-book a creator before the event — not scramble day-of",
        "Turn booth conversations into testimonials + reels without hiring a video crew",
    ],
    subj_email=["re: [Event name]", "booth coverage — [Event]"],
    subj_li=["[Event] coverage", "seeing you at [Event]"],
    email_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. 'Saw [Company] is at booth B-24 at SaaStr next month — "
        "your sales deck said you closed 40% of last year's pipeline from events.']\n\n"
        "If last year looked like most event teams, you walked away with a few iPhone clips and "
        "a 'we'll make a recap video later' that never happened.\n\n"
        "We pre-book one of our creators (we have them in SF, NYC, Dubai, Bangalore, London) "
        "to cover your booth for 1–2 days. You get 10–15 edited assets — demos, testimonials, "
        "keynote reactions, booth-life reels — delivered within 48 hours. $500–$1,000 per event.\n\n"
        "We've done this for [similar B2B brand] at [event] — 14 assets in 36 hours, fed sales "
        "for a quarter.\n\n"
        "Want me to send a 1-pager on the [Event] package before you finalise your event plan?\n\n"
        "— [Sender]"
    ),
    li_body=(
        "Hi [First Name] — saw you're at [Event].\n\n"
        "[PERSONALIZATION — e.g. 'Your post about [company]'s booth setup last year was "
        "great — noticed there was no video recap though.']\n\n"
        "We cover booths for B2B brands — 1 creator on-site for 1–2 days, 10–15 edited "
        "assets in 48 hours, $500–$1,000 flat. We're already covering [brand A] and [brand B] "
        "at [Event].\n\n"
        "Want the package 1-pager? Happy to lock a creator for your booth before they're gone."
    ),
    ctas=[
        "Want the [Event] package 1-pager? I'll send it today",
        "Pre-book a creator before [event date] — 2 slots left in [city]",
        "15 mins to walk through the event asset plan?",
        "Reply 'yes' and I'll hold a creator for your booth for 24 hours",
    ],
    vprops=[
        "10–15 event-day video assets in 48 hours — $500–$1,000 flat",
        "Pre-book a local creator in any city — no flights, no crew, no scramble",
        "Turn your $100K booth into a quarter's worth of content",
        "B2B brands use us to extract every shareable moment from the event floor",
    ],
    sequence=[
        {"day": 1, "channel": "LinkedIn connect", "angle": "Event observation + booth number", "note": "Reference exact event + booth."},
        {"day": 3, "channel": "Email #1 (6–8 weeks before event)", "angle": "Asset-gap framing", "note": "Subject A. Reference last year's event recap or lack of it."},
        {"day": 8, "channel": "LinkedIn DM", "angle": "'2 slots left in [city]'", "note": "Soft scarcity — real if inventory is real."},
        {"day": 14, "channel": "Email #2", "angle": "Case study — similar B2B brand at similar event", "note": "One-pager attached."},
    ],
)

# ================================================================
# EXPERIMENT 4 — INDIAN DECISION-MAKERS IN THE US
# ================================================================
experiment(
    num=4,
    title="Indian decision-makers at US companies",
    tagline="India-origin CMOs, VPs Marketing, Heads of Growth at US-based companies. Warm cultural bridge + US creative needs.",
    icp={
        "industry": "US SaaS, consumer apps, D2C, marketplaces",
        "size": "100–5000 employees",
        "revenue": "$10M–$1B ARR",
        "funding": "Series B+ or public",
        "geo": "US — SF Bay, NYC, Austin, Seattle, Boston",
        "tech": "Meta + TikTok Ads, LinkedIn Ads, HubSpot / Salesforce, creator / UGC tools",
        "pain": "US creative costs $3–10K/video; Indian options feel risky for US brand",
        "goals": "Cut creative cost 5–10x while maintaining US-native quality",
    },
    persona={
        "titles": "CMO, VP Marketing, Head of Growth, Head of Creative, Head of Performance",
        "responsibilities": "US marketing P&L, creative strategy, agency relationships",
        "motivations": "Personal — 'help a team back home win' + professional ROAS targets",
        "challenges": "Trust gap between US leadership and 'offshore creative' stigma",
        "buying": "CMO / VP signs; 2–4 week cycle; references matter heavily",
    },
    signals=[
        "India-origin last name + current US company",
        "US company running Meta / TikTok ads at scale (Meta Ads Library 50+ active)",
        "Posted about India / Bangalore / Hyderabad on LinkedIn in last 12 months",
        "Attended or spoke at India-SaaS events (SaaSBoomi, Nasscom)",
    ],
    jtbd=[
        "Justify lower-cost creative without a quality compromise story",
        "Run more creative variants per month without adding US headcount",
        "Back a team / stack they believe in culturally",
    ],
    subj_email=["Indian creator stack", "from Bangalore"],
    subj_li=["from BLR", "India → US creative"],
    email_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. 'Saw your post on building [Company]'s team across Bangalore "
        "and SF — the comment about creative being the one function that didn't move over was "
        "honest.']\n\n"
        "Most US marketing leaders pay $3–10K per video because their agency is still the default. "
        "We're running the stack you'd probably build yourself if you had the time — 6,000 creators "
        "globally, 2,000+ in the US, delivered in 5–7 days starting at $49/video. Competitor + "
        "experiment intelligence layered on top so you know what to shoot, not just who.\n\n"
        "Two Shark Tank India alums use us for their US creative, and a couple of US SaaS brands "
        "for testimonials and product explainers.\n\n"
        "If you're running 20+ creative variants/month — or want to — worth 15 mins?\n\n"
        "— [Sender]"
    ),
    li_body=(
        "Hi [First Name] — fellow BLR-to-Bay Area-ish story.\n\n"
        "[PERSONALIZATION — e.g. 'Loved your post on the creative-ops hire you just made — "
        "we're building the stack she'll probably wish existed.']\n\n"
        "Short version: we run competitor intelligence + production (6,000 creators, 2,000 "
        "in the US) for brands shooting 20+ variants/month. $49–$199/video, 5–7 day delivery. "
        "Two Shark Tank India alums + a few US SaaS teams on it.\n\n"
        "Open to me sending a sample of what we'd shoot for [Company] based on your current "
        "Meta ads?"
    ),
    ctas=[
        "Want a free competitor + creative gap snapshot for [Company]?",
        "15 mins next week — I'll show you [competitor]'s last 30 days of ads",
        "Reply 'sample' and I'll send 3 US UGC clips for your category",
        "Calendly — whatever works: [link]",
    ],
    vprops=[
        "Competitor intelligence + production in one stack — what US agencies don't offer",
        "5–10x cheaper than US production without the 'offshore' feel — creators shoot from where they live",
        "Know what to make (category data) AND make it (creator network) — in one platform",
        "The creative stack a sharp India-US marketer would build themselves",
    ],
    sequence=[
        {"day": 1, "channel": "LinkedIn connect + cultural note", "angle": "Genuine — BLR/Hyd/Chennai shared context", "note": "Never fake. Only use if sender has real India context too."},
        {"day": 4, "channel": "Email #1", "angle": "Stack-you'd-build-yourself", "note": "Reference Meta ads library specifics."},
        {"day": 9, "channel": "LinkedIn DM", "angle": "Send free competitor snapshot (1-pager)", "note": "No CTA in DM — let snapshot sell."},
        {"day": 14, "channel": "Email #2", "angle": "Reference case — similar US SaaS / D2C brand", "note": "One stat, one link."},
    ],
)

# ================================================================
# EXPERIMENT 5 — AGENCIES
# ================================================================
experiment(
    num=5,
    title="Performance marketing agencies",
    tagline="Boutique performance agencies managing 5–20 D2C / SaaS accounts. White-label Passionbits as their creative backend.",
    icp={
        "industry": "Performance marketing / growth / creative agencies",
        "size": "10–100 employees",
        "revenue": "₹2Cr–₹50Cr / $500K–$10M",
        "funding": "Bootstrapped or small raise",
        "geo": "India (Bangalore/Mumbai/Delhi), US (NYC/Austin), UK",
        "tech": "Meta Business Manager, Google Ads, client CRM integrations, Foreplay / Motion",
        "pain": "Creative velocity = client retention; can't staff in-house production per client",
        "goals": "Increase margin per client without hiring; retain clients past month 6",
    },
    persona={
        "titles": "Agency founder, Account Director, Media Buyer, Creative Director",
        "responsibilities": "Client P&L, creative briefs, retention, team utilization",
        "motivations": "Margin, not being the agency that 'plateaued at month 6'",
        "challenges": "Creative team can't scale linearly with client count",
        "buying": "Founder-led; 1–2 weeks from demo to pilot client",
    },
    signals=[
        "5+ D2C / SaaS case studies on site",
        "Hiring 'creative strategist' or 'video editor' recently",
        "Running their own Meta ads targeting D2C founders",
        "Listed on performance agency directories (GrowthCollective, Mayple)",
    ],
    jtbd=[
        "Scale creative production across 10+ clients without linear headcount",
        "Give clients competitor intelligence reports — look smarter at QBRs",
        "Turn a service margin into a product-like margin",
    ],
    subj_email=["white-label creative backend", "agency margin question"],
    subj_li=["for agencies", "white-label backend"],
    email_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. 'Your case study on [client]'s 3x ROAS was a great read — "
        "the part about shipping 60 variants in 45 days is what caught me.']\n\n"
        "The math most agencies hit at 8+ clients: creative team can't scale, margin compresses, "
        "clients churn at month 6 when results plateau.\n\n"
        "We're the creative backend a few performance agencies quietly run on — Passionbits. "
        "6,000 creators globally, 5–7 day delivery, $49–$199/video. Plus a competitor + "
        "experiment intelligence layer your strategists can drop straight into client QBRs. "
        "White-label friendly.\n\n"
        "One agency here went from 12 clients to 22 without hiring a single creative. Another "
        "raised retainers 20% by adding our intel layer as a 'premium tier'.\n\n"
        "Worth 15 mins to walk through how they set it up?\n\n"
        "— [Sender]"
    ),
    li_body=(
        "Hi [First Name] — [PERSONALIZATION — e.g. 'saw your post about hiring a 4th creative "
        "— the scaling math on agency creative is brutal.']\n\n"
        "We're the creative + intelligence backend a few performance agencies run on — "
        "6,000 creators, 5–7 day delivery, white-label. One agency on us went 12 → 22 clients "
        "without a single creative hire.\n\n"
        "Worth me sending the agency one-pager + pricing?"
    ),
    ctas=[
        "15 mins — I'll walk through how [reference agency] set it up",
        "Want the agency one-pager + white-label pricing?",
        "Pilot 1 client free — we'll deliver 10 variants in a week, you decide",
        "Book time: [calendar] — bring your trickiest current client",
    ],
    vprops=[
        "The white-label creative + competitor intelligence backend for performance agencies",
        "Scale client count without scaling headcount — one agency went 12 → 22 clients",
        "Add a premium intelligence tier to your retainer — raise margins 20%",
        "6,000 creators + competitor data — look 3x smarter at every client QBR",
    ],
    sequence=[
        {"day": 1, "channel": "LinkedIn connect", "angle": "Case-study observation + agency math", "note": "Reference a specific case study."},
        {"day": 3, "channel": "Email #1", "angle": "Agency-margin framing", "note": "Subject A or B based on recipient tone."},
        {"day": 8, "channel": "LinkedIn DM", "angle": "Offer free pilot on 1 client", "note": "Lower the friction."},
        {"day": 13, "channel": "Email breakup", "angle": "Round-up of 3 agency case studies", "note": "1-pager attached."},
    ],
)

# ================================================================
# EXPERIMENT 6 — TOP 100 META ADS LIBRARY (US)
# ================================================================
experiment(
    num=6,
    title="Top 100 US accounts by Meta Ads Library volume",
    tagline="Highest-spend US D2C / consumer brands on Meta. High creative volume = high creative-fatigue risk.",
    icp={
        "industry": "US D2C consumer, beauty, apparel, fitness, home, pet, supplements",
        "size": "100–2000 employees",
        "revenue": "$20M–$500M",
        "funding": "Series B+ or PE-backed",
        "geo": "US",
        "tech": "Meta + TikTok Ads at heavy spend, Northbeam / Triple Whale, Shopify Plus",
        "pain": "Creative fatigue at scale — top creatives running 60+ days, CPM climbing",
        "goals": "Sustain ROAS by increasing creative velocity without proportional cost",
    },
    persona={
        "titles": "VP Growth, Head of Performance, Director of Paid Media, Head of Creative",
        "responsibilities": "Paid P&L, creative pipeline, ROAS targets, agency management",
        "motivations": "Hit quarterly ROAS, avoid the 'everything's fatiguing' quarter",
        "challenges": "Creative pipeline is the bottleneck; hiring a video editor takes 90 days",
        "buying": "Director/VP signs pilots; 3–6 week cycle with pilot → contract",
    },
    signals=[
        "50+ active ads in Meta Ads Library",
        "Top-performing ads running 60+ days (fatigue proxy)",
        "Low ratio of UGC-style to brand-shot creative",
        "Hiring 'creative strategist' or 'video producer' on LinkedIn",
    ],
    jtbd=[
        "Ship 30–100 fresh variants/month without hiring",
        "Identify which formats are fatiguing before ROAS collapses",
        "Beat competitors on creative velocity, not just bid",
    ],
    subj_email=["your top ad — 63 days", "fatigue on [creative name]"],
    subj_li=["Meta Ads Library note", "your top 3 ads"],
    email_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. 'Pulled [Company]'s Meta Ads Library — your top 3 creatives "
        "have been running 63, 58, and 71 days respectively. That's the fatigue window for "
        "[their category] based on what we see across the top 100 US D2C spenders.']\n\n"
        "Most teams find out about fatigue when ROAS drops 15%. By then you've lost the quarter.\n\n"
        "We pull your ad history + your top 5 competitors' live ads and tell you which formats "
        "are breaking out that you haven't tested. Then we produce them — 6,000 creators, "
        "$49–$199/video, 5–7 day delivery.\n\n"
        "[Reference D2C brand] shipped 47 variants last month on us; their previous in-house "
        "record was 9.\n\n"
        "Want me to send a free creative-gap snapshot for [Company]? No call needed unless it's "
        "actually useful.\n\n"
        "— [Sender]"
    ),
    li_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. 'Your top Meta creative has been running 63 days — that's "
        "the fatigue window for your category.']\n\n"
        "We pull your ad history + 5 competitors' live ads and tell you which formats you "
        "haven't tested that are breaking out. Then produce them via 6,000 creators in 5–7 "
        "days, $49–$199/video.\n\n"
        "Want a free creative-gap snapshot for [Company]?"
    ),
    ctas=[
        "Reply 'snapshot' and I'll send your creative gap + 3 competitor wins within 24h",
        "15 mins to walk through your Meta ads library vs top 3 category peers",
        "Pilot: 10 variants in 5 days, $990 — you run them, you decide",
        "Book directly: [link] — I'll bring your competitor data live",
    ],
    vprops=[
        "Spot creative fatigue before ROAS drops — 60+ day ads flagged automatically",
        "See which formats are breaking out in your category that you haven't tested",
        "30–100 variants/month at $49–$199 each — match Meta's creative velocity",
        "Competitor intelligence + production in one stack — agency cost in one bucket",
    ],
    sequence=[
        {"day": 1, "channel": "Email #1", "angle": "Specific ad-age call-out (from their library)", "note": "Use real ad IDs / creative names when possible."},
        {"day": 4, "channel": "LinkedIn connect + brief note", "angle": "'Sent you a note earlier — here's the short version'", "note": "Bridge email → LinkedIn."},
        {"day": 8, "channel": "LinkedIn DM", "angle": "Send the free creative-gap snapshot", "note": "Attach PDF — no call ask."},
        {"day": 14, "channel": "Email #2", "angle": "Reference brand case study", "note": "[Brand] shipped 47 variants in 30 days."},
    ],
)

# ================================================================
# EXPERIMENT 7 — CONSUMER APPS (CANVA, CLICKUP TYPE)
# ================================================================
experiment(
    num=7,
    title="Consumer / prosumer SaaS apps (Canva, ClickUp, Notion-type)",
    tagline="High-scale prosumer SaaS needing constant UGC, tutorials, feature launches, and testimonials.",
    icp={
        "industry": "Prosumer / consumer SaaS, productivity, creator tools, design, collaboration",
        "size": "200–5000 employees",
        "revenue": "$30M–$1B ARR",
        "funding": "Series C+ or public",
        "geo": "US HQ, global user base",
        "tech": "Product-led growth stack, TikTok / YouTube / Instagram creator programs, HubSpot / Marketo",
        "pain": "Constant feature-launch cadence; need UGC-style content at platform scale",
        "goals": "Ship 20+ UGC-style videos per feature launch across markets and languages",
    },
    persona={
        "titles": "Head of Brand, Head of Content, Head of Creator Program, Social Media Lead",
        "responsibilities": "Content calendar, creator relations, feature launches, multilingual content",
        "motivations": "Stay above the content treadmill; keep share of voice vs. fast-moving peers",
        "challenges": "Creator programs are slow and expensive; translation / localisation overhead",
        "buying": "Director-level; 4–6 week cycle; values large portfolio + multi-language proof",
    },
    signals=[
        "Active creator / ambassador program",
        "YouTube / TikTok channel posting 3+ per week",
        "Multilingual site (5+ languages) but English-heavy UGC",
        "Hired 'community manager' or 'creator lead' recently",
    ],
    jtbd=[
        "Ship launch-day UGC in 5+ languages in week 1",
        "Offload 70% of volume UGC so in-house team focuses on hero content",
        "Fill the tutorial + 'use case' content layer without a studio",
    ],
    subj_email=["UGC for [feature launch]", "multi-language creator layer"],
    subj_li=["creator layer for [Product]", "launch UGC"],
    email_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. 'Saw [Product]'s [feature] launch last week — loved the "
        "demo video, but noticed it's English-only. Your Spanish, Hindi, and Portuguese "
        "pages are still running the old launch clip.']\n\n"
        "Most prosumer SaaS teams ship hero launch videos well and then run dry on the "
        "'use-case' and localised UGC layer. That's where we live.\n\n"
        "6,000 creators across 50+ countries, 12+ Indian languages, 5+ global — UGC, "
        "tutorials, feature walkthroughs. $49–$199 per video, 5–7 day delivery. Your team "
        "focuses on hero content; we do volume.\n\n"
        "A prosumer SaaS currently uses us for 80 feature-UGC videos per quarter across 4 "
        "languages.\n\n"
        "Worth 20 mins to walk through how they set it up for their launch calendar?\n\n"
        "— [Sender]"
    ),
    li_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. 'Your last feature launch demo was sharp — noticed the "
        "non-English pages didn't get the update.']\n\n"
        "We run the volume UGC + multi-language creator layer for prosumer SaaS — 6,000 "
        "creators, 12+ Indian languages, 5+ global. $49–$199 per video, 5–7 day delivery. "
        "One SaaS on us: 80 feature-UGC clips per quarter, 4 languages.\n\n"
        "Want the launch-UGC playbook?"
    ),
    ctas=[
        "Reply 'playbook' and I'll send the launch-UGC one-pager",
        "20 mins to walk through the 80-video/quarter setup?",
        "Pilot: 10 UGC videos for your next launch, 3 languages, $990",
        "Book: [calendar link]",
    ],
    vprops=[
        "Volume UGC + multi-language creator layer — your team ships hero, we ship everything else",
        "Launch-day UGC in 5+ languages by day 3, not month 2",
        "80 feature-UGC videos per quarter is normal — $49–$199 each",
        "The creator layer prosumer SaaS actually uses — not an enterprise agency",
    ],
    sequence=[
        {"day": 1, "channel": "Email #1", "angle": "Feature-launch observation + localisation gap", "note": "Reference specific feature + which languages missed it."},
        {"day": 4, "channel": "LinkedIn connect", "angle": "Short note — 'sent a quick email earlier'", "note": "Bridge."},
        {"day": 9, "channel": "LinkedIn DM", "angle": "Sample reel: 5 clips from a peer SaaS (with permission)", "note": "Visual proof beats description."},
        {"day": 15, "channel": "Email #2", "angle": "Case study — 80 videos/quarter setup", "note": "1 stat, 1 link."},
    ],
)

# ================================================================
# EXPERIMENT 8 — D2C (INDIAN HIGH-SPEND)
# ================================================================
experiment(
    num=8,
    title="Indian D2C brands (high Meta ad spend)",
    tagline="Indian D2C brands scaling aggressively on Meta — the Sugar / Mamaearth / Souled Store / boAt cohort.",
    icp={
        "industry": "D2C — beauty, apparel, F&B, home, pet, supplements, electronics",
        "size": "50–1000 employees",
        "revenue": "₹20Cr–₹1000Cr",
        "funding": "Series A+ or profitable bootstrap",
        "geo": "India (Tier 1 + 2), some GCC / US expansion",
        "tech": "Meta + Google Ads, Shopify / Unicommerce, WebEngage / CleverTap",
        "pain": "Creative fatigue, ROAS compression, agency plateau",
        "goals": "30–100 variants/month, category leadership, brand + performance balance",
    },
    persona={
        "titles": "Head of Growth, Head of Performance, CMO, Founder, Creative Director",
        "responsibilities": "Paid P&L, creative pipeline, brand voice, agency oversight",
        "motivations": "Hit scale targets without losing ROAS discipline",
        "challenges": "Agency produces what they know; in-house too slow; UGC quality inconsistent",
        "buying": "Founder / Head of Growth signs; 2–4 week cycle with pilot",
    },
    signals=[
        "₹5L+/month Meta spend (inferred from ad volume)",
        "10+ active Meta ads in library",
        "Recent funding or 'scaling' / 'hiring' LinkedIn post",
        "Featured on Shark Tank India / major D2C roundup",
    ],
    jtbd=[
        "Produce category-leading creative volume without burning ₹20L/month on shoots",
        "Know what [top competitor] is shipping this week",
        "Diversify hooks + formats — break the 'same 3 ads' pattern",
    ],
    subj_email=["[Competitor] shipped 47", "your vs [competitor] — creative"],
    subj_li=["D2C creative note", "[Competitor] vs [You]"],
    email_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. 'Ran [Company]'s Meta Ads Library next to [top competitor] — "
        "they shipped 47 new creatives last month, you shipped 11. Their top format "
        "(problem-solution UGC with on-screen captions) isn't in your library at all.']\n\n"
        "Most D2C teams I talk to in India aren't short on budget — they're short on a pipeline "
        "that ships 30+ clean variants a month without torching ₹20L on shoots.\n\n"
        "We run that pipeline — 6,000 creators (India-heavy, US on-demand), $49–$199/video, "
        "5–7 day delivery — with a competitor intelligence layer that tells you which format "
        "to test next. Two Shark Tank India alums on us.\n\n"
        "Want a free creative-gap report for [Company] vs [competitor]? No call needed unless "
        "it's actually useful.\n\n"
        "— [Sender]"
    ),
    li_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. '[Competitor] shipped 47 creatives last month, [Company] "
        "shipped 11 — and their top format isn't in your library.']\n\n"
        "We run the pipeline D2C brands use to close that gap — 6,000 creators, $49–$199 "
        "per video, 5–7 day delivery, plus competitor intel. Two Shark Tank India alums "
        "on us.\n\n"
        "Want the free creative-gap report for [Company] vs [competitor]?"
    ),
    ctas=[
        "Reply 'report' and I'll send the [Company] vs [Competitor] creative gap within 24h",
        "15 mins to walk through it live — I'll pull the ad library in the call",
        "Pilot: 15 variants in 7 days, ₹99,000 flat — run them, decide",
        "Book: [calendar]",
    ],
    vprops=[
        "[Competitor] ships 4x your creative volume — here's how to close that without agency cost",
        "30–100 variants/month at ₹4,000–₹15,000 each — India and US creators",
        "The only platform that shows you what competitors ship AND ships yours",
        "Two Shark Tank India alums use us — both tripled creative volume in 60 days",
    ],
    sequence=[
        {"day": 1, "channel": "Email #1", "angle": "Specific [competitor] volume callout", "note": "Must reference real numbers from Meta Ads Library."},
        {"day": 3, "channel": "LinkedIn connect", "angle": "Bridge — 'sent you a quick email'", "note": "Short note."},
        {"day": 8, "channel": "LinkedIn DM + free gap report", "angle": "Deliver the free value", "note": "PDF attached; no call ask."},
        {"day": 14, "channel": "Email #2", "angle": "Case — Shark Tank alum's creative scale", "note": "1 stat + meeting ask."},
    ],
    notes="Example target accounts to seed this experiment: The Souled Store, Gabbit, Sugar, Mamaearth, Bombay Shaving Company, Pant Project, Wakefit, Man Matters."
)

# ================================================================
# EXPERIMENT 9 — B2B CLIENT TESTIMONIALS
# ================================================================
experiment(
    num=9,
    title="B2B SaaS — client testimonial / sales enablement video",
    tagline="B2B SaaS needing customer testimonials for sales enablement, content marketing, and CS expansion. Target Head of CS, Sales Enablement, Content Marketing. Reference: Nota AI.",
    icp={
        "industry": "B2B SaaS — devtools, data, AI, HR tech, fintech, security",
        "size": "50–1000 employees",
        "revenue": "$5M–$200M ARR",
        "funding": "Series A–C",
        "geo": "US, UK, India (sales HQ US, team global)",
        "tech": "Salesforce / HubSpot, Gong, Gainsight, Webflow, Wistia / Loom",
        "pain": "Customer page is logos + text; 1 testimonial video from 2022; sales reps ask for more",
        "goals": "5–15 testimonial / case-study videos per quarter, plus sales-enablement snippets",
    },
    persona={
        "titles": "Head of Customer Success, Head of Sales Enablement, Head of Content Marketing, Director of Product Marketing",
        "responsibilities": "Customer advocacy program, sales collateral, case study pipeline",
        "motivations": "Close-rate lift from video proof, customer expansion signal, content velocity",
        "challenges": "Customers are willing but scheduling + production is painful; videos take 8+ weeks",
        "buying": "Director-level signs; 3–5 week cycle; values turnaround SLA and revision rounds",
    },
    signals=[
        "Customer page is text-only or has outdated videos (2022 or older)",
        "Recently announced customer wins / case studies (blog post only)",
        "Hiring 'customer marketing' or 'content marketing' manager",
        "Sales team requesting more proof content (visible on LinkedIn posts / job descriptions)",
    ],
    jtbd=[
        "Capture 5–15 customer testimonials per quarter without a production team",
        "Turn each testimonial into a long-form case study + 3–5 cutdowns for sales",
        "Scale across customer regions (customer in APAC / EU doesn't need flying to)",
    ],
    subj_email=["your customer page", "testimonial velocity"],
    subj_li=["testimonial pipeline", "Nota-style testimonials"],
    email_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. 'Your customer page has 24 logos but only 1 video — from 2022. "
        "Saw on LinkedIn that [AE] asked for more video proof last week.']\n\n"
        "Video testimonials close at 2–3x the rate of text quotes — but most B2B CS + enablement "
        "teams are stuck on the production side. Customer agrees; 8 weeks later you still haven't "
        "shipped.\n\n"
        "We run the testimonial pipeline for B2B SaaS. Customer books a 20-minute self-record "
        "(we send them a clean brief + lighting kit); we edit; you get a long-form testimonial "
        "+ 3–5 cutdowns for sales within 5–7 days. $199–$399 per customer, globally.\n\n"
        "Nota AI-type teams use this to ship 12+ testimonials per quarter without anyone on-site.\n\n"
        "Want the 1-pager + a sample testimonial for your category?\n\n"
        "— [Sender]"
    ),
    li_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. 'Your customer page has solid logos but only 1 testimonial "
        "video — from 2022. Noticed [AE]'s LI post asking for more video proof.']\n\n"
        "We run the async testimonial pipeline for B2B SaaS — customer self-records 20 mins, "
        "we edit, you get a long-form + 3–5 cutdowns in 5–7 days. $199–$399 per customer, "
        "global. Ship 12+ per quarter without anyone on-site.\n\n"
        "Want the sample + 1-pager?"
    ),
    ctas=[
        "Reply 'sample' and I'll send a B2B SaaS testimonial + the 1-pager",
        "15 mins — I'll walk through the 12-per-quarter setup",
        "Pilot: 3 testimonials in 14 days, $897 flat",
        "Book: [calendar]",
    ],
    vprops=[
        "Async testimonial pipeline — customer self-records 20 mins, you ship a full asset in 7 days",
        "5–15 testimonials per quarter without flying, without a production team",
        "Each customer → long-form case study + 3–5 sales cutdowns, one cost",
        "The testimonial stack B2B CS + enablement teams actually ship on",
    ],
    sequence=[
        {"day": 1, "channel": "Email #1", "angle": "Customer-page observation + sales-ask signal", "note": "Reference actual logos + last testimonial date."},
        {"day": 4, "channel": "LinkedIn connect", "angle": "'Sent an email — short version here'", "note": "Bridge."},
        {"day": 9, "channel": "LinkedIn DM — sample + 1-pager", "angle": "Free value", "note": "No CTA; let sample land."},
        {"day": 14, "channel": "Email #2", "angle": "Case — Nota-style SaaS, 12 testimonials / quarter", "note": "1 stat, 1 link."},
    ],
    notes="Triangulate across 3 buyers per account: Head of CS (expansion angle), Head of Sales Enablement (close-rate angle), Head of Content Marketing (content volume angle). Same account, 3 different opening value props."
)

# ================================================================
# EXPERIMENT 10 — CONTENT FARMS (ORGANIC TOF AT SCALE)
# ================================================================
experiment(
    num=10,
    title="Content farms — brands running organic at scale (signal-based)",
    tagline="Brands running 5–10 social accounts, high-volume organic content, content-farm playbook. Volume is the signal.",
    icp={
        "industry": "Consumer + creator brands, new-wave media, D2C, edtech, finance creator, personal-brand-led SaaS",
        "size": "10–300 employees",
        "revenue": "$1M–$50M",
        "funding": "Pre-seed to Series B, some bootstrapped",
        "geo": "India, US, UK",
        "tech": "TikTok / IG / YouTube Shorts, Later / Hypefury, Descript, Airtable content ops",
        "pain": "Content ops is the whole team; quality dips as volume climbs; editors burn out",
        "goals": "Millions of organic views at $4–5 CPM equivalent, with unit economics that work",
    },
    persona={
        "titles": "Head of Content, Head of Organic, Head of Social, Founder (creator-led), Content Ops Lead",
        "responsibilities": "Content calendar, posting velocity, account-level performance, editor team",
        "motivations": "Own a disproportionate share of organic attention in their niche",
        "challenges": "Editor bandwidth is the ceiling; freelancers inconsistent; good hooks dry up",
        "buying": "Content lead / founder signs; 1–3 weeks; proof = sample volume delivered",
    },
    signals=[
        "5+ active social handles (brand + sub-brands + creator accounts)",
        "Posting 3+ times/day across IG / TikTok / YT Shorts",
        "Recently hired 2+ content editors / producers in 90 days",
        "Public content-farm playbook LinkedIn posts (founders talking about volume math)",
    ],
    jtbd=[
        "Hit 20–50 posts/day across accounts without burning the team",
        "Find hooks that work across 5+ account personas",
        "Scale editing throughput without linear headcount",
    ],
    subj_email=["content volume question", "5 accounts, 1 team"],
    subj_li=["content-ops note", "volume stack"],
    email_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. 'Saw [Company] runs 7 social accounts posting 25+ times/day. "
        "Loved your LinkedIn post last week on the 'editor as bottleneck' — that hit.']\n\n"
        "The content-farm math breaks around account #5: editors can't keep up, quality dips, "
        "hooks get recycled. Most teams solve it by hiring another editor. That fixes it for 3 "
        "months.\n\n"
        "We're the creator + editor layer a few content-farm teams quietly run on — 6,000 "
        "creators globally, volume-priced ($12–$49 per short-form clip at scale), 3–5 day "
        "turnaround, hook-library built from what's winning in their niche this week.\n\n"
        "One team on us went from 18 posts/day to 52 without hiring a single editor.\n\n"
        "Want the 1-pager + volume pricing? Happy to send without a call.\n\n"
        "— [Sender]"
    ),
    li_body=(
        "Hi [First Name],\n\n"
        "[PERSONALIZATION — e.g. '7 accounts, 25+ posts/day — your content ops is doing "
        "more than most media companies.']\n\n"
        "We're the creator + editor layer content-farm teams use to scale past 5 accounts. "
        "6,000 creators, $12–$49 per short-form at scale, 3–5 day turnaround. One team went "
        "18 → 52 posts/day without an editor hire.\n\n"
        "Want the 1-pager + volume pricing?"
    ),
    ctas=[
        "Reply 'pricing' and I'll send the volume grid + case study",
        "20 mins — I'll walk through the 52-posts/day setup",
        "Pilot: 100 short-forms in 10 days, $1,900 flat — fire-hose test",
        "Book: [calendar]",
    ],
    vprops=[
        "Break the editor-as-bottleneck ceiling — scale past 5 accounts without hiring",
        "$12–$49 per short-form at volume, 3–5 day turnaround",
        "Hook library refreshed weekly from your niche's top-performing clips",
        "The layer content-farm teams run on — 18 → 52 posts/day, same team size",
    ],
    sequence=[
        {"day": 1, "channel": "LinkedIn connect + volume-math note", "angle": "Specific post/account count observation", "note": "Never round — use exact numbers."},
        {"day": 3, "channel": "Email #1", "angle": "Editor-bottleneck framing", "note": "Reference their LinkedIn post if one exists."},
        {"day": 8, "channel": "LinkedIn DM — pricing grid + case", "angle": "Free value", "note": "Attach PDF; no call ask."},
        {"day": 14, "channel": "Email breakup", "angle": "Soft close + reference case", "note": "2-line."},
    ],
    notes="Content farms don't have to be a separate ICP — they're a signal layered on top of ICPs 7 (consumer SaaS), 8 (D2C), and 10. If a target account shows content-farm signals, elevate priority and adjust the opening to volume-math."
)

# ================================================================
# TRAINING PLAN SECTION
# ================================================================
p("Training Plan — for the show", "H1")
p("Goal: get every rep to consistently book 10–15 meetings/week within 4 weeks of joining.", "Small")
hr()

p("Structure (5 modules, delivered over 2 weeks)", "H2")
p("Each module = 45–60 mins of recorded content + 1 live working session + 1 async assignment. "
  "Reps are expected to book their first 3 meetings by end of week 2.", "Body")

# Module 1
p("Module 1 — GTM basics + experimentation mindset", "H3")
p("<b>Why this first:</b> Reps who don't internalise the mindset will execute templates. "
  "Reps who internalise it will ship their own variants.", "Body")
p("<b>Cover:</b>", "Label")
p("&bull; The three-stage funnel: ICP → Signal → Message. What each does, what breaks when any is weak.<br/>"
  "&bull; Why outbound is experimentation, not repetition. Every week is a new hypothesis.<br/>"
  "&bull; The 4-variable ladder: ICP, signal, subject, body. Change ONE at a time.<br/>"
  "&bull; Reading reply rates as signal — open &lt;40% = subject problem; open &gt;40% reply &lt;2% = body/CTA problem.<br/>"
  "&bull; Killing bad experiments fast: 200-send test. If &lt;1% positive reply, kill the variant, don't iterate.<br/>"
  "&bull; Personalisation hierarchy: individual &gt; company &gt; persona &gt; nothing.<br/>"
  "&bull; The cost of generic — why one well-researched 30-account list beats 300 scraped.<br/>"
  "&bull; Measuring what matters: positive reply rate, not open rate. Meetings booked, not replies.", "Body")
p("<b>Assignment:</b> Pick 1 of the 10 experiments. Write your own A-variant email for 5 prospects. "
  "Compare against the template. Explain what you changed and why.", "Body")

# Module 2
p("Module 2 — Two channels that work today", "H3")
p("<b>Cover only what's working right now, not everything we've ever tried.</b>", "Body")
p("<b>Channel 1 — LinkedIn (primary)</b>", "H4")
p("&bull; <b>Why it works for us:</b> Passionbits buyers (CMOs, Heads of Growth, agency founders) live on LI. "
  "Acceptance rate 35–45% when we lead with mutual (Roshan) or specific observation.<br/>"
  "&bull; <b>Daily cadence:</b> 40 connect requests + 80 DMs (reply-to-accept) = 120 touches/day.<br/>"
  "&bull; <b>What to do:</b> Connect with 150-char personalised note. On accept, wait 48 hours, send the DM "
  "in the DM format from the experiment.<br/>"
  "&bull; <b>What not to do:</b> Don't pitch in the connect note. Don't auto-DM on accept. Don't include links in the first DM.<br/>"
  "&bull; <b>Expected conversion:</b> 120 touches → 40 acceptances → 8–12 replies → 3–5 meetings/week per rep.", "Body")
p("<b>Channel 2 — Email (paired with LinkedIn)</b>", "H4")
p("&bull; <b>Why it works for us:</b> LinkedIn gets attention; email carries the value. Reference the LI ping in the email.<br/>"
  "&bull; <b>Daily cadence:</b> 80–100 sends/day per rep. Monday + Tuesday + Thursday (avoid Fridays, Mondays spike reply).<br/>"
  "&bull; <b>Tech:</b> Sending from warmed domain (passionbits.co or sender-specific), SPF/DKIM/DMARC aligned, "
  "Smartlead / Instantly with 3–5 mailboxes per rep for volume.<br/>"
  "&bull; <b>Subject lines:</b> 2–4 words, lowercase, internal-looking. A/B test per experiment.<br/>"
  "&bull; <b>Expected conversion:</b> 400 sends/week → 1.5–3% positive reply → 6–12 meetings/week per rep.", "Body")
p("<b>Combined math:</b> LinkedIn 3–5/week + Email 6–12/week = <b>10–15 meetings/week per rep</b>. "
  "This is the goal — and it's achievable with disciplined daily volume, not heroics.", "Body")

# Module 3
p("Module 3 — The 10 experiments to start with", "H3")
p("Reps don't have to run all 10 — pick 2–3 based on list availability and rep strength. "
  "Suggested pairings:", "Body")
p("<b>New rep, first 30 days:</b> Experiment 1 (Roshan's connections) + Experiment 6 (Top 100 US Meta Ads Library). "
  "Warm + high-signal cold.<br/>"
  "<b>Rep comfortable with research:</b> Experiment 2 (India → US) + Experiment 9 (B2B testimonials). "
  "Specific trigger-based, higher reply rates.<br/>"
  "<b>Agency-focused rep:</b> Experiment 5 (Agencies) + Experiment 10 (Content farms). "
  "Founder-to-founder tone, shorter sales cycle.<br/>"
  "<b>Event rep (seasonal):</b> Experiment 3 (Event sponsors) — spikes around major conferences; plan list "
  "6–8 weeks before every target event.", "Body")
p("<b>Each experiment should ship at 200 touches minimum before calling it.</b> Anything less is noise.", "Body")

# Module 4
p("Module 4 — The funnel as it stands today", "H3")
p("Use this as the current benchmark. If your numbers beat this, share what's working in the daily standup.", "Body")
funnel = [
    ["Stage", "Volume / week", "Conversion", "Next stage"],
    ["Touches (email + LI)", "500–600", "—", "—"],
    ["Positive replies", "12–20", "2–4% of touches", "→ Book"],
    ["Meetings booked", "10–15", "~70% of positive replies", "→ Show up"],
    ["Meetings held", "7–11", "~70% show rate", "→ SQL"],
    ["Qualified opportunities (SQL)", "3–5", "~45% of held", "→ Pilot"],
    ["Pilots closed", "1–2", "~30% of SQL", "→ Customer"],
    ["Paying customer (contract)", "1", "~50% of pilots", "— "],
]
t = Table(funnel, colWidths=[55*mm, 30*mm, 42*mm, 35*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), DARK_HEAD),
    ("TEXTCOLOR", (0,0), (-1,0), HexColor("#ffffff")),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 9.5),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("BOX", (0,0), (-1,-1), 0.5, BORDER),
    ("INNERGRID", (0,0), (-1,-1), 0.3, BORDER),
    ("BACKGROUND", (0,1), (-1,1), LIGHT),
    ("BACKGROUND", (0,3), (-1,3), LIGHT),
    ("BACKGROUND", (0,5), (-1,5), LIGHT),
    ("BACKGROUND", (0,7), (-1,7), LIGHT),
]))
story.append(t)
sp(8)
p("<b>Implication:</b> to hit 10–15 meetings booked/week, a rep must run 500–600 touches/week — that's "
  "~120/day across email + LinkedIn. Below 400/week and the math doesn't work. Above 800/week and personalisation "
  "collapses. The sweet spot is tight.", "Body")

# Module 5
p("Module 5 — Daily rhythm + reporting", "H3")
p("<b>Rep daily rhythm (90-min morning block + 60-min afternoon block):</b>", "Body")
p("&bull; <b>08:30–09:00</b> — Review yesterday's replies; send any same-day follow-ups.<br/>"
  "&bull; <b>09:00–10:30</b> — Morning send block: 80 emails + 40 LinkedIn connects (with personalised notes).<br/>"
  "&bull; <b>14:00–15:00</b> — Afternoon block: 40 DMs to accepted-connects from prior days + reply handling.<br/>"
  "&bull; <b>16:30–17:00</b> — List enrichment for next day (adding 100 prospects with signal verification).", "Body")
p("<b>Weekly reporting (Friday end-of-day):</b>", "Body")
p("&bull; Touches sent (email + LI), opens, positive replies, meetings booked, meetings held.<br/>"
  "&bull; Experiment-level reply rate — which of the 2–3 experiments is winning.<br/>"
  "&bull; One thing that worked, one thing that didn't.<br/>"
  "&bull; Next week's experiment pivot (if any).", "Body")

# Closing
p("How to know the training landed", "H2")
p("&bull; Week 2: rep has sent 500+ touches, booked first 3 meetings.<br/>"
  "&bull; Week 4: rep consistently at 10+ meetings/week.<br/>"
  "&bull; Week 6: rep proposes their own experiment variant — signals internalised mindset.<br/>"
  "&bull; Week 8: rep running 2 experiments, hitting 12–15 meetings/week, owning one full ICP.", "Body")

sp(10)
p("— End of document —", "Small")

# ================================================================
# BUILD
# ================================================================
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=18*mm, rightMargin=18*mm,
    topMargin=18*mm, bottomMargin=18*mm,
    title="Passionbits Outbound Experiments + Training Plan"
)
doc.build(story)
print(f"Wrote: {OUTPUT}")
