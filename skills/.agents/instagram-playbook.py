#!/usr/bin/env python3
"""Generate the Instagram Playbook 2025-2026 PDF for Passionbits."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "instagram-playbook-2025-2026.pdf")

# Passionbits brand colors
PRIMARY = HexColor("#1a1a2e")
ACCENT = HexColor("#e94560")
LIGHT_BG = HexColor("#f5f5f5")
GREEN = HexColor("#27ae60")
ORANGE = HexColor("#f39c12")
BLUE = HexColor("#3498db")
GRAY = HexColor("#7f8c8d")
TABLE_HEADER = HexColor("#1a1a2e")
TABLE_ALT = HexColor("#f9f0f2")
ACCENT_LIGHT = HexColor("#fce4ec")
TEXT_DARK = HexColor("#2c3e50")

styles = getSampleStyleSheet()

styles.add(ParagraphStyle("CoverTitle", parent=styles["Title"], fontSize=32, leading=38, textColor=PRIMARY, spaceAfter=4, alignment=TA_LEFT, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("CoverSub", parent=styles["Normal"], fontSize=16, leading=20, textColor=ACCENT, spaceAfter=20, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("CoverTagline", parent=styles["Normal"], fontSize=12, leading=16, textColor=GRAY, spaceAfter=8))
styles.add(ParagraphStyle("ChapterTitle", parent=styles["Title"], fontSize=24, leading=30, textColor=PRIMARY, spaceBefore=0, spaceAfter=6, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("H1", parent=styles["Heading1"], fontSize=20, leading=24, textColor=PRIMARY, spaceBefore=20, spaceAfter=10, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("H2", parent=styles["Heading2"], fontSize=14, leading=18, textColor=PRIMARY, spaceBefore=14, spaceAfter=6, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("H3", parent=styles["Heading3"], fontSize=11, leading=14, textColor=TEXT_DARK, spaceBefore=10, spaceAfter=4, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("Body", parent=styles["Normal"], fontSize=9.5, leading=13, textColor=TEXT_DARK, spaceAfter=5))
styles.add(ParagraphStyle("BodySmall", parent=styles["Normal"], fontSize=8.5, leading=11, textColor=TEXT_DARK, spaceAfter=3))
styles.add(ParagraphStyle("BulletPB", parent=styles["Normal"], fontSize=9.5, leading=13, textColor=TEXT_DARK, leftIndent=18, spaceAfter=2, bulletIndent=6, bulletFontSize=9))
styles.add(ParagraphStyle("BulletSmall", parent=styles["Normal"], fontSize=8.5, leading=11, textColor=TEXT_DARK, leftIndent=18, spaceAfter=2, bulletIndent=6, bulletFontSize=8))
styles.add(ParagraphStyle("Callout", parent=styles["Normal"], fontSize=9.5, leading=13, textColor=PRIMARY, spaceAfter=6, leftIndent=12, borderPadding=6, backColor=ACCENT_LIGHT))
styles.add(ParagraphStyle("TableCell", parent=styles["Normal"], fontSize=8, leading=10.5, textColor=TEXT_DARK))
styles.add(ParagraphStyle("TableHeader", parent=styles["Normal"], fontSize=8, leading=10.5, textColor=white, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("Footer", parent=styles["Normal"], fontSize=7, leading=9, textColor=GRAY, alignment=TA_CENTER))
styles.add(ParagraphStyle("TrendNum", parent=styles["Normal"], fontSize=9, leading=12, textColor=ACCENT, fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("ChapterNum", parent=styles["Normal"], fontSize=14, leading=18, textColor=ACCENT, fontName="Helvetica-Bold", spaceAfter=2))


def hr():
    return HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceAfter=10, spaceBefore=4)

def hr_light():
    return HRFlowable(width="100%", thickness=0.5, color=HexColor("#ddd"), spaceAfter=8, spaceBefore=4)

def sp(h=6):
    return Spacer(1, h)

def p(text, style="Body"):
    return Paragraph(text, styles[style])

def b(text, style="BulletPB"):
    return Paragraph(f"<bullet>&bull;</bullet> {text}", styles[style])

def bs(text):
    return Paragraph(f"<bullet>&bull;</bullet> {text}", styles["BulletSmall"])

def make_table(headers, rows, col_widths=None):
    header_cells = [Paragraph(h, styles["TableHeader"]) for h in headers]
    data = [header_cells]
    for row in rows:
        data.append([Paragraph(str(c), styles["TableCell"]) for c in row])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#ddd")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), TABLE_ALT))
    t.setStyle(TableStyle(style_cmds))
    return t

def stat_box(stats, W):
    """Create a stat highlight box."""
    vals = [[s[0] for s in stats], [s[1] for s in stats]]
    n = len(stats)
    t = Table(vals, colWidths=[W/n]*n)
    cmds = [
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 22),
        ("FONTSIZE", (0, 1), (-1, 1), 7),
        ("TEXTCOLOR", (0, 0), (-1, 0), ACCENT),
        ("TEXTCOLOR", (0, 1), (-1, 1), GRAY),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("BOX", (0, 0), (-1, -1), 1, HexColor("#eee")),
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BG),
    ]
    for i in range(1, n):
        cmds.append(("LINEBEFORE", (i, 0), (i, -1), 0.5, HexColor("#ddd")))
    t.setStyle(TableStyle(cmds))
    return t


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=0.7*inch, rightMargin=0.7*inch,
        topMargin=0.65*inch, bottomMargin=0.65*inch
    )
    story = []
    W = doc.width

    # ============================================================
    # COVER PAGE
    # ============================================================
    story.append(sp(60))
    story.append(p("The Instagram", "CoverTitle"))
    story.append(p("Playbook 2025-2026", "CoverTitle"))
    story.append(sp(8))
    story.append(hr())
    story.append(sp(6))
    story.append(p("100 Viral Trends. Algorithm Secrets. Brand Strategies.", "CoverSub"))
    story.append(sp(10))
    story.append(p("The definitive guide for creators and brands to dominate Instagram Reels, crack the algorithm, and build a content engine that drives real results.", "CoverTagline"))
    story.append(sp(30))

    story.append(stat_box([
        ("200B+", "Daily Reel\nPlays"),
        ("2B", "Monthly Reel\nUsers"),
        ("50%", "Time Spent\non Reels"),
        ("55%", "Views from\nNon-Followers"),
    ], W))

    story.append(sp(40))
    story.append(hr_light())
    story.append(p("<b>Created by Passionbits</b> | passionbits.io", "Footer"))
    story.append(p("AI-Powered Video Production for Brands", "Footer"))

    story.append(PageBreak())

    # ============================================================
    # TABLE OF CONTENTS
    # ============================================================
    story.append(sp(20))
    story.append(p("Table of Contents", "ChapterTitle"))
    story.append(hr())
    story.append(sp(10))

    toc_items = [
        ("Chapter 1", "How the Instagram Algorithm Actually Works in 2026", "3"),
        ("Chapter 2", "100 Instagram Trends Going Viral Right Now", "6"),
        ("Chapter 3", "The Creator Playbook: How to Make Viral Reels", "14"),
        ("Chapter 4", "The Brand Playbook: Cracking Instagram Video", "20"),
        ("Chapter 5", "110 Viral Hooks That Stop the Scroll", "25"),
        ("Chapter 6", "Content Frameworks & Posting Strategy", "29"),
        ("Chapter 7", "Tools, Features & Platform Updates", "32"),
        ("Chapter 8", "Key Metrics & Benchmarks", "35"),
    ]
    for ch, title, pg in toc_items:
        story.append(p(f"<font color='#e94560'><b>{ch}</b></font> &nbsp;&nbsp; {title} <font color='#7f8c8d'>{'.' * 40} {pg}</font>", "Body"))
        story.append(sp(4))

    story.append(PageBreak())

    # ============================================================
    # CHAPTER 1: ALGORITHM
    # ============================================================
    story.append(p("Chapter 1", "ChapterNum"))
    story.append(p("How the Instagram Algorithm Actually Works in 2026", "ChapterTitle"))
    story.append(hr())
    story.append(sp(6))

    story.append(p("Instagram doesn't have one algorithm. It runs <b>multiple AI-powered ranking systems</b> -- one each for Feed, Stories, Reels, Explore, and Search. Each surface prioritizes different signals.", "Body"))
    story.append(sp(6))

    # 3 Confirmed Ranking Factors
    story.append(p("The 3 Confirmed Ranking Factors (Adam Mosseri, Jan 2025)", "H2"))
    story.append(p("Instagram's head confirmed these are the three most important signals:", "Body"))
    story.append(sp(4))

    story.append(make_table(
        ["Rank", "Signal", "What It Means", "Impact"],
        [
            ["#1", "Watch Time", "How long people watch your content. Viewers decide within 1.7 seconds whether to keep watching.", "Most important for initial distribution"],
            ["#2", "Likes Per Reach", "Percentage of viewers who like your post.", "Matters more for reaching existing followers"],
            ["#3", "Sends Per Reach (DM Shares)", "694,000 Reels are sent via DM every minute. Mosseri called this the most heavily weighted signal.", "Strongest signal for reaching NEW audiences"],
        ],
        col_widths=[W*0.07, W*0.18, W*0.45, W*0.30]
    ))
    story.append(sp(8))

    # Engagement Hierarchy
    story.append(p("The Full Engagement Hierarchy", "H2"))
    story.append(p("From highest to lowest algorithmic weight:", "Body"))
    story.append(b("<b>DM Shares/Sends</b> -- 3-5x higher weight than likes. Strongest signal for non-follower distribution."))
    story.append(b("<b>Saves</b> -- Signal lasting interest. Weighted significantly higher than likes."))
    story.append(b("<b>Meaningful Comments</b> -- Instagram uses NLP to evaluate comment quality. 20 thoughtful comments outperform 200 emoji reactions."))
    story.append(b("<b>Watch Time / Completion Rate</b> -- Most important for initial distribution."))
    story.append(b("<b>Rewatches</b> -- A video watched twice outperforms one with numerous likes."))
    story.append(b("<b>Likes</b> -- Weakest major signal. No longer the primary optimization target."))
    story.append(sp(6))

    story.append(p("<font color='#e94560'><b>Key Insight:</b></font> A single save is worth roughly 10 likes in algorithmic weight. Optimize for saves and shares, not likes.", "Callout"))
    story.append(sp(8))

    # How Each Surface Ranks
    story.append(p("How Each Surface Ranks Content", "H2"))

    story.append(p("<b>Reels Algorithm</b>", "H3"))
    story.append(b("Emphasizes entertainment value and discovery"))
    story.append(b("Top signals: watch time, DM shares, saves, rewatches"))
    story.append(b('<b>"Audition system"</b>: Reels shown to random non-followers first. Strong performance triggers wider distribution.'))
    story.append(b("Posts reaching 60%+ viewership past 3 seconds trigger wider distribution"))
    story.append(b("Penalizes: watermarked content, low resolution, TikTok logos, silent videos, excessive text, political content"))
    story.append(sp(4))

    story.append(p("<b>Feed Algorithm</b>", "H3"))
    story.append(b("Prioritizes content from close connections"))
    story.append(b("Signals: content popularity, interaction history with poster, user activity patterns"))
    story.append(b("Content from frequently-messaged accounts ranks higher"))
    story.append(sp(4))

    story.append(p("<b>Stories Algorithm</b>", "H3"))
    story.append(b("Relationship-based only. Designed for close connections."))
    story.append(b("Interactive stickers (polls, questions) boost visibility"))
    story.append(b("Poor for reaching new audiences. Best for deepening community."))
    story.append(sp(4))

    story.append(p("<b>Explore Algorithm</b>", "H3"))
    story.append(b("Rewards 95%+ completion rate, 5+ second image lingering, follow conversions"))
    story.append(b("Video and carousels prioritized over static images"))
    story.append(sp(4))

    story.append(p("<b>Search</b>", "H3"))
    story.append(b("Now operates like a search engine. Analyzes voiceover, on-screen text, captions, keywords, alt text."))
    story.append(b("Keyword-rich captions function like SEO copy"))
    story.append(b("Since mid-2025, public posts are indexed by Google"))
    story.append(sp(8))

    # Major Algorithm Updates
    story.append(p("Major Algorithm Updates (2025-2026)", "H2"))

    story.append(p('<b>Original Content Prioritization</b>', "H3"))
    story.append(b("Original content receives <b>40-60% more distribution</b> than reposts"))
    story.append(b("Accounts posting 10+ reposts in 30 days get excluded from recommendations"))
    story.append(b("Aggregator accounts saw 60-80% reach drops"))
    story.append(sp(4))

    story.append(p('<b>"Raw Content" Initiative (Dec 2025)</b>', "H3"))
    story.append(b('Mosseri: Instagram will prioritize "raw, real human content" over AI-generated material in 2026'))
    story.append(b("Visible AI content reduces trust. Using AI invisibly behind the scenes is the winning approach."))
    story.append(sp(4))

    story.append(p('<b>Hashtag Changes</b>', "H3"))
    story.append(b("Hashtags no longer drive reach or enable follows (removed Dec 2024)"))
    story.append(b("3-5 relevant hashtags for categorization only"))
    story.append(b("Keywords in captions now drive discovery through search"))
    story.append(b("Keyword-rich captions generate ~30% more reach than hashtag-heavy posts"))
    story.append(sp(4))

    story.append(p('<b>"Your Algorithm" User Control (Dec 2025)</b>', "H3"))
    story.append(b("Users can review and customize topics shaping their recommendations"))
    story.append(b("Reset wipes algorithmic history across Explore, Reels, and suggested posts"))
    story.append(b("Makes niche clarity mandatory for creators and brands"))
    story.append(sp(6))

    # Content Eligibility
    story.append(p("Content Eligibility Requirements", "H2"))
    story.append(p("Posts must meet ALL these criteria to be eligible for recommendations:", "Body"))
    story.append(make_table(
        ["#", "Requirement"],
        [
            ["1", "No watermarks from other platforms (TikTok, CapCut)"],
            ["2", "Must include audio (music or voiceover)"],
            ["3", "Videos under 3 minutes (for recommendation eligibility)"],
            ["4", "Original or substantially transformed content"],
            ["5", "Account in good standing (no flags or restrictions)"],
        ],
        col_widths=[W*0.08, W*0.92]
    ))

    story.append(PageBreak())

    # ============================================================
    # CHAPTER 2: 100 TRENDS
    # ============================================================
    story.append(p("Chapter 2", "ChapterNum"))
    story.append(p("100 Instagram Trends Going Viral Right Now", "ChapterTitle"))
    story.append(hr())
    story.append(sp(6))

    # Reel Format Trends
    story.append(p("Reel Format Trends (1-25)", "H1"))

    trends_formats = [
        ("1. Faceless Reels", "B-roll footage, screen recordings, or product shots with text overlays and trending audio. No on-camera presence needed. The most scalable format -- many creators have built 6-figure businesses from faceless accounts."),
        ("2. Mini Vlogs", "Short day-in-the-life snippets in 30-60 seconds with calming music and voiceover. Raw, authentic, unscripted."),
        ("3. POV (Point of View) Reels", "First-person perspective with text overlays describing relatable situations. Top-performing format for engagement."),
        ("4. GRWM (Get Ready With Me)", "Morning routines, work prep, or event preparation. Works across niches: GRWM for a sales call, coffee opening, workout. Niche GRWMs are exploding."),
        ("5. Transformation / Before-and-After", "Quick transitions showing dramatic contrast. Show the end result FIRST, then rewind to process."),
        ("6. Reaction / Commentary Reels", "Using Remix or Dual Camera to react to trending content. Leverages existing momentum."),
        ("7. 'Send This To...' Reels", "Prompts asking viewers to share with specific people. Increases DM shares -- the algorithm's #1 signal."),
        ("8. Tour Videos", "Office tours, product showrooms, workspace walkthroughs, behind-the-scenes factory visits. Major brand trend in 2025-2026."),
        ("9. Video Memes", "Brands remixing trending meme Reels with current audio and putting their own spin on it. Comedic and shareable."),
        ("10. 'How I Fixed It' Trend", "Childhood logic vs adult solutions. Nostalgic humor format with broad appeal."),
        ("11. Interactive Polls / 'This or That'", "Using Instagram's built-in poll stickers in Reels to get viewers involved. Drives comment volume."),
        ("12. Panoramic Format Reels (5120x1080)", "Experimental wide-format Reels that stand out in feeds and attract new audiences."),
        ("13. ASMR Reels", "Satisfying sounds and visuals triggering relaxation. Effective for unboxings, cooking, craft, beauty content."),
        ("14. Educational / How-To Reels", "Quick tutorials providing instant value: step-by-step tips, checklists, one-mistake-to-avoid format."),
        ("15. Behind-the-Scenes Content", "Packing orders, brainstorming, campaign prep, team rituals. Unpolished footage outperforms polished product shots."),
        ("16. 'In the Moment' Reels", "Raw, unscripted clips from daily life with natural product integration and meaningful takeaways."),
        ("17. 'Click, Click' Transformation", "Quick cuts with click sounds and a reveal at the end. 1.2M+ uses for makeup, hair, outfits."),
        ("18. Day-in-the-Life Content", "Entrepreneurs and CEOs sharing routines. Performs especially well for personal brands."),
        ("19. Storytelling Reels", "Carousel-style storytelling using Problem > Solution > Result arc. Can extend to 60-90 seconds."),
        ("20. Talking Head Reels", "Creator speaks directly to camera delivering tips or stories. Face-in-frame increases retention by 35%."),
        ("21. Transition Reels", "Match cuts advancing a narrative. Swipe transitions between looks, angles, or products."),
        ("22. Fake Text Message Conversations", "Dramatic, funny, or shocking text exchanges unfolding in real-time. One of the most viral faceless formats."),
        ("23. Quiz/Trivia Reels", "Present questions on-screen where viewers attempt answers. Drives high comment volume and rewatches."),
        ("24. Top 5 / Listicle Videos", "Countdown-style content building toward final reveal. Creates anticipation."),
        ("25. Walk + Voiceover Reels", "Short walk with overlay thoughts on life, growth, creativity. Calm and reflective."),
    ]
    for title, desc in trends_formats:
        story.append(p(f"<font color='#e94560'><b>{title}</b></font>", "Body"))
        story.append(p(desc, "BodySmall"))
        story.append(sp(2))

    story.append(PageBreak())

    # Audio Trends
    story.append(p("Trending Audio & Music (26-42)", "H1"))

    audio_trends = [
        ("26. Bruno Mars 'Cha Cha Cha'", "Recipe montages, interior design reveals, and dance Reels."),
        ("27. Charli XCX '360' Orchestral Cover", "Sparked by Bridgerton. Theatrical moments in unexpected locations."),
        ("28. Sabrina Carpenter 'House Tour'", "Syncing transitions to lyrics for home, shop, restaurant, office tours."),
        ("29. Black Beatles Resurgence", "'The new 2016.' Group pose nostalgia content."),
        ("30. Harry Styles 'Aperture'", "Sync transitions for recommendations, recaps, product spotlights."),
        ("31. 'I Asked the Universe for a Sign'", "Humorous sign-reveal format. Caption-driven comedy."),
        ("32. Justin Bieber 'DAISIES'", "Trending for cooking, cozy travel, and outfit content."),
        ("33. Tyler the Creator 'Ring Ring Ring'", "Smooth retro-funk for laid-back content."),
        ("34. Olivia Dean 'Man I Need'", "Jazzy, playful vibe making everyday content feel cute."),
        ("35. Chappell Roan 'Pink Pony Club'", "23,000+ reels post-Grammy win. Pop anthem energy."),
        ("36. 'Sports Car x Promiscuous' Remix", "Nelly Furtado sample with timeless appeal."),
        ("37. Caesars 'Jerk it Out'", "2002 song resurging with 200,000+ reels."),
        ("38. Delana Hope 'New Month Declaration'", "Lip-syncing affirming lyrics to set monthly intentions."),
        ("39. Tame Impala 'The Less I Know'", "Trending segment for various moody content types."),
        ("40. Original Audio / Voiceover", "Gets algorithmic preference in 2026. Establish brand voice."),
        ("41. Calm/Ambient Audio", "Aesthetic shots and reflective content. Growing trend for travel and lifestyle."),
        ("42. Comedic/Sarcastic Audio", "Brand humor format. Self-aware and shareable."),
    ]
    for title, desc in audio_trends:
        story.append(p(f"<font color='#e94560'><b>{title}</b></font>", "Body"))
        story.append(p(desc, "BodySmall"))
        story.append(sp(2))
    story.append(sp(6))

    # Content Format Trends
    story.append(p("Content Format Innovations (43-60)", "H1"))

    format_trends = [
        ("43. Carousels as Mini-Blogs", "Up to 20 slides. Carousels achieve 154 more interactions than single-image posts. Highest engagement format."),
        ("44. Hybrid Carousels", "Mixing photos with 3-5 second video clips within carousels. The winning 2026 format."),
        ("45. Extended 3-Minute Reels", "Longer Reels now reach non-followers through recommendations -- if retention is strong."),
        ("46. Trial Reels", "Test content with non-followers before full publication. 80% of users saw increased non-follower reach."),
        ("47. Collaborative Posts (Up to 5)", "Cross-niche collabs outperform same-niche. The single most reliable organic growth tactic in 2026."),
        ("48. Broadcast Channels", "One-to-many messaging with 60-70% open rates. No algorithm filtering. 'The new email list.'"),
        ("49. Instagram Notes", "60-character ephemeral messages in DM inbox. Get more replies than Reels."),
        ("50. Nostalgia-Driven Content", "Throwback imagery, Y2K vibes, childhood references. Shared cultural memories drive shares."),
        ("51. People-Centric Content", "Featuring founders and employees, not logos. 'Audiences buy into humans far more than logos.'"),
        ("52. Imperfection Honesty Format", "'The perfect product doesn't exist, but this solves [specific problem].' Builds trust."),
        ("53. Sarcastic Call-Out Format", "'Come on [product], say your stupid line...' then subvert expectations. Self-aware brand positioning."),
        ("54. Girl-to-Girl Advice Format", "Direct, intimate messaging like advice from a friend. Authentic and relatable."),
        ("55. Educational Reversal Format", "'I stopped using [product] and here's what I noticed.' Demonstrates product necessity through humor."),
        ("56. Camera Roll Blackmail Format", "'Show me $5,000 or I'll leak your camera roll.' Portfolio showcase disguised as humor."),
        ("57. Multi-Angle Hype Format", "'The back, stunning. The front, gorgeous...' Showcases products from every angle."),
        ("58. Money Drain Transition", "'Show me why you don't have money' then product reveal. Humorous consumption."),
        ("59. Contrarian/Opinion-Based", "Statements challenging common beliefs. Creates cognitive dissonance that demands explanation."),
        ("60. Aspirational Questions", "'What if your content finally started paying you?' Forces mental engagement."),
    ]
    for title, desc in format_trends:
        story.append(p(f"<font color='#e94560'><b>{title}</b></font>", "Body"))
        story.append(p(desc, "BodySmall"))
        story.append(sp(2))

    story.append(PageBreak())

    # Niche Trends
    story.append(p("Niche-Specific Trends (61-80)", "H1"))

    niche_trends = [
        ("61. Fashion: Outfit Transition Reels", "Try-on with fun transitions between looks. Capsule wardrobe concepts."),
        ("62. Fashion: 'Most Expensive Thing I Own'", "Reveal format that drives massive curiosity and engagement."),
        ("63. Food: Snap Cooking Transition Parody", "Snap at ingredient expecting instant transformation. Comedic and shareable."),
        ("64. Food: Recipe Showcase + Description", "Written recipe in description drives saves. Satisfying food ASMR."),
        ("65. Food: 'Girl Dinner' Format", "Pairing products together in casual, relatable meal content."),
        ("66. Fitness: '30-Day Transformation' Narratives", "Progress documentation with milestone content. Inspirational and saveable."),
        ("67. Fitness: 'The Face I Make When...'", "Reaction format applied to fitness myths. Relatable humor."),
        ("68. Business: 'If You Are...' Question Format", "Speaking to ideal clients. Powerful lead-generation audio trend."),
        ("69. Business: FAQ Answer Videos", "Pick frequent customer questions, answer on camera. Authority building."),
        ("70. Business: Industry Tip of the Day", "Daily micro-education content. Positions brand as helpful authority."),
        ("71. Beauty: Before-and-After Transformations", "Product application reveals with dramatic contrast."),
        ("72. Beauty: 'In Your 20s, It's Important...'", "Age-specific product advice format. Targeted and shareable."),
        ("73. Travel: Cinematic Recap Reels", "Aesthetic moments stitched with calm/ambient audio."),
        ("74. Travel: Destination Reveals + Trending Audio", "Surprise location drops synced to music beats."),
        ("75. Tech: Product Demo in 30 Seconds", "Fast-paced, hands-on feature walkthroughs."),
        ("76. Tech: 'Little-Known Tool' Discovery Reels", "Hidden gem format drives saves and shares."),
        ("77. Pet: 'POV of a Dog Sniffing [Product]'", "Pet reaction format for product brands. Universally engaging."),
        ("78. Design: Sketch-to-Final Time-Lapses", "Process documentation that showcases skill and builds trust."),
        ("79. Coaching: 'Myth vs Truth' Series", "Busting misconceptions in 30-60 seconds. Authority positioning."),
        ("80. Coaching: Mini Lessons (One Concept, 60 Seconds)", "Single-idea education with clear takeaway."),
    ]
    for title, desc in niche_trends:
        story.append(p(f"<font color='#e94560'><b>{title}</b></font>", "Body"))
        story.append(p(desc, "BodySmall"))
        story.append(sp(2))

    story.append(sp(6))

    # Platform & Strategy Trends
    story.append(p("Platform & Strategy Trends (81-100)", "H1"))

    platform_trends = [
        ("81. Instagram SEO Is the New Hashtag", "Keywords in captions generate ~30% more reach. Captions function like SEO copy now."),
        ("82. Google Indexing Instagram Posts", "Since mid-2025, public posts appear in Google search results. Massive discovery opportunity."),
        ("83. Reels-First Navigation Redesign", "App opens to Reels feed. Bottom bar: Home > Reels > DMs > Search > Profile."),
        ("84. Instagram Edits App", "Native editing app with 5M+ users in 4 days. Teleprompter, AI styling, 4K export, no watermark."),
        ("85. Comment-to-DM Automation", "Post Reel with CTA 'Comment GROWTH and I'll send you the guide.' Automate DM delivery."),
        ("86. Nano-Influencer Partnerships", "Nano-influencers (1-10K) have 8%+ engagement and 2-3x conversion rates. 75.9% of all influencers."),
        ("87. AI-Invisible Content Creation", "Using AI behind the scenes for scripting, editing, repurposing -- but keeping the output human-feeling."),
        ("88. Reposts Feature (Aug 2025)", "Officially reshare public Reels and posts to your feed. Dedicated profile tab."),
        ("89. Friends Feed + Friends Map", "Dedicated feed showing Reels friends interact with. Location sharing."),
        ("90. '2025 Wrapped' Carousels", "Inspired by Spotify. Brands recap their year with bold text across slides."),
        ("91. Content Repurposing Pipeline", "One video becomes 3-5 Reels, carousel posts, voiceover B-roll, text-overlay clips."),
        ("92. Reels Templates", "Pre-built templates handle timing, transitions, audio sync. Under 5 min per Reel."),
        ("93. Serialized Content Over One-Off Viral", "Weekly series with recurring formats outperform one-off viral attempts."),
        ("94. Looping Videos", "Seamless loops stretch watch time -- the algorithm's top ranking signal."),
        ("95. 20-Minute Reels", "Maximum length expanded to 20 minutes for deep content. Requires strong retention."),
        ("96. Carousel Collabs", "Get 2-3x the saves of Reel collabs. Micro-creator partnerships perform best."),
        ("97. Enhanced Analytics", "Post-level follower growth, demographics by post, content interest breakdown."),
        ("98. Reels Polls in Comments", "Polls expanded beyond Stories to feed and Reels comments. New engagement driver."),
        ("99. Meta AI Restyle", "Edit Stories photos/videos using text prompts. AI-powered visual editing."),
        ("100. 'Raw Content' Aesthetic", "Mosseri announced: authenticity over polish. Smartphone footage with natural light outperforms studio quality."),
    ]
    for title, desc in platform_trends:
        story.append(p(f"<font color='#e94560'><b>{title}</b></font>", "Body"))
        story.append(p(desc, "BodySmall"))
        story.append(sp(2))

    story.append(PageBreak())

    # ============================================================
    # CHAPTER 3: CREATOR PLAYBOOK
    # ============================================================
    story.append(p("Chapter 3", "ChapterNum"))
    story.append(p("The Creator Playbook: How to Make Viral Reels", "ChapterTitle"))
    story.append(hr())
    story.append(sp(6))

    # The 3-Second Rule
    story.append(p("The 3-Second Rule", "H1"))
    story.append(p("Content that fails to capture attention in the first 2-3 seconds faces immediate abandonment. <b>50% of viewers drop off in the first 3 seconds.</b> The target: get 60%+ of viewers past the 3-second mark.", "Body"))
    story.append(sp(4))
    story.append(p("<font color='#e94560'><b>Key Insight:</b></font> Users decide within 1.7 seconds whether to continue watching. Your hook isn't the first 3 seconds -- it's the first 1.5 seconds before Instagram even displays the caption overlay.", "Callout"))
    story.append(sp(8))

    # 5 Core Hook Formulas
    story.append(p("5 Core Hook Formulas That Go Viral", "H2"))

    story.append(p("<b>1. The Contrarian Hook</b>", "H3"))
    story.append(p("Structure: 'Everyone says [belief], but [your take]'", "Body"))
    story.append(p("Example: 'Everyone tells you to post daily on Instagram, but I grew to 100K posting twice a week.'", "BodySmall"))
    story.append(sp(3))

    story.append(p("<b>2. The Mistake Hook</b>", "H3"))
    story.append(p("Structure: 'I lost [value] because I [mistake]'", "Body"))
    story.append(p("Example: 'I wasted $5,000 on Instagram ads before learning this one targeting trick.'", "BodySmall"))
    story.append(sp(3))

    story.append(p("<b>3. The Numbered List Hook</b>", "H3"))
    story.append(p("Structure: '[Number] [things] that [outcome]'", "Body"))
    story.append(p("Example: '5 Reels mistakes killing your reach.' Best range: 3-7 items.", "BodySmall"))
    story.append(sp(3))

    story.append(p("<b>4. The Time-Based Hook</b>", "H3"))
    story.append(p("Structure: 'How I [result] in [timeframe]'", "Body"))
    story.append(p("Example: 'What 30 days of posting Reels daily taught me about the algorithm.'", "BodySmall"))
    story.append(sp(3))

    story.append(p("<b>5. The Question Hook</b>", "H3"))
    story.append(p("Structure: 'Are you [doing something wrong]?'", "Body"))
    story.append(p("Example: 'Are you using Instagram's algorithm against yourself?' Avoid simple yes/no -- spark curiosity.", "BodySmall"))
    story.append(sp(8))

    # Editing Techniques
    story.append(p("Editing Techniques for Maximum Watch Time", "H2"))
    story.append(b("<b>Jump cutting:</b> Remove every millisecond of dead air. Keeps energy high."))
    story.append(b("<b>Pattern interrupts:</b> Change angle, zoom, or visual element every 3-5 seconds to reset attention."))
    story.append(b("<b>B-roll layering:</b> Layer supplementary footage to illustrate what you're discussing."))
    story.append(b("<b>Edit every 3 seconds:</b> Jump cuts, zooms, transitions. Never let the visual stay static."))
    story.append(b("<b>Bold animated captions:</b> 85% of viewers watch without sound. Add text in the first 1-2 seconds."))
    story.append(b("<b>Sound design:</b> Layer ambient sounds with background music for emotional connection."))
    story.append(b("<b>Center text placement:</b> Position text in the safe zone (center 80%) to avoid interface overlap."))
    story.append(b("<b>Seamless loops:</b> End where you began to maximize watch time through replays."))
    story.append(sp(8))

    # Audio Strategy
    story.append(p("Audio Strategy for Creators", "H2"))
    story.append(p("<b>Recommended Audio Mix:</b>", "Body"))

    story.append(make_table(
        ["Audio Type", "Percentage", "Why"],
        [
            ["Original audio / voiceover", "40-50%", "Gets algorithmic preference in 2026. Builds brand voice."],
            ["Trending sounds", "30-40%", "Discovery boost. Can land on Explore page."],
            ["Evergreen / mood music", "15-20%", "Timeless appeal. Works year-round."],
        ],
        col_widths=[W*0.30, W*0.15, W*0.55]
    ))
    story.append(sp(6))

    story.append(p("<b>How to Find Trending Audio:</b>", "H3"))
    story.append(b("In-app Trending tab (top 50, updated every few days)"))
    story.append(b("Look for the upward arrow indicator while scrolling Reels"))
    story.append(b("Monitor TikTok trends 1-2 weeks ahead (they migrate to Instagram)"))
    story.append(b("Look for sounds under 10K uses -- early adoption = less saturation"))
    story.append(b("Post within 24-48 hours of spotting a rising sound for the strongest boost"))
    story.append(sp(8))

    # Posting Strategy
    story.append(p("Optimal Posting Strategy", "H2"))

    story.append(p("<b>Best Times to Post (from 9.6M posts analyzed):</b>", "H3"))
    story.append(make_table(
        ["Day", "Best Times", "Content Type"],
        [
            ["Monday", "7 PM, 6 PM, 8 PM", "Motivational, week-ahead content"],
            ["Tuesday", "7 PM, 3 PM, 5 PM", "Tips, tutorials, educational"],
            ["Wednesday", "12 PM, 6 PM, 8 AM", "Peak day -- highest engagement"],
            ["Thursday", "9 AM, 8 AM, 7 AM", "Peak day -- strongest morning performance"],
            ["Friday", "10 PM, 9 PM, 6 AM", "Entertaining, casual content"],
            ["Saturday", "9 PM, 10 PM, 8 PM", "Lifestyle, personal content"],
            ["Sunday", "9 PM, 10 PM, 8 PM", "Week-ahead prep, reflection"],
        ],
        col_widths=[W*0.18, W*0.32, W*0.50]
    ))
    story.append(sp(4))
    story.append(p("<font color='#e94560'><b>Top 3 overall:</b></font> Thursday 9 AM, Wednesday 12 PM, Wednesday 6 PM", "Body"))
    story.append(sp(6))

    story.append(p("<b>Posting Frequency:</b>", "H3"))
    story.append(b("3-5 Reels per week. Consistency matters more than daily posting."))
    story.append(b("Posting 3-5 times weekly doubles follower growth rate."))
    story.append(b("10+ posts weekly boosts average reach per post by 24%."))
    story.append(b("Ideal content mix: 60-70% Reels, 20-30% carousels, 10% static posts."))
    story.append(sp(6))

    # Hashtag Strategy
    story.append(p("Hashtag Strategy (Major Shift)", "H2"))
    story.append(b("<b>3-5 hashtags</b> is now the ideal range (per Adam Mosseri)"))
    story.append(b("Posts with 25+ hashtags see <b>40% less reach</b>"))
    story.append(b("Hashtags are now categorization signals, not reach boosters"))
    story.append(b("Caption placement delivers ~30% better results vs first comment"))
    story.append(b("Target hashtags with 10K-200K posts (sweet spot for discoverability)"))
    story.append(sp(6))

    # Engagement Tactics
    story.append(p("Engagement Acceleration Tactics", "H2"))
    story.append(b("Reply to comments within the first hour -- posts get +21% engagement"))
    story.append(b("Pin thoughtful/funny comments to boost conversation"))
    story.append(b("Share Reels via Stories for additional distribution"))
    story.append(b("Use the Collab feature for cross-audience exposure"))
    story.append(b("'Comment-to-DM' strategy: 'Comment GROWTH and I'll send you my free guide'"))
    story.append(b("Post daily Notes to stay visible in DM inboxes"))

    story.append(PageBreak())

    # ============================================================
    # CHAPTER 4: BRAND PLAYBOOK
    # ============================================================
    story.append(p("Chapter 4", "ChapterNum"))
    story.append(p("The Brand Playbook: Cracking Instagram Video", "ChapterTitle"))
    story.append(hr())
    story.append(sp(6))

    story.append(p("The strategic landscape has shifted fundamentally. Instagram now rewards signal over noise. Three new meta-metrics dominate:", "Body"))
    story.append(b("<b>Retention density</b> -- how long users pause and return"))
    story.append(b("<b>Conversation depth</b> -- quality of human interaction"))
    story.append(b("<b>Searchable reputation</b> -- brand discoverability for intent-driven queries"))
    story.append(sp(8))

    # Content Formats That Convert
    story.append(p("Content Formats That Convert for Brands", "H2"))

    story.append(make_table(
        ["Format", "Reach", "Engagement", "Best For"],
        [
            ["Reels", "30.81% avg reach rate", "55% views from non-followers", "Discovery, awareness, viral moments"],
            ["Carousels", "1.4x more reach than static", "Highest engagement format", "Depth, saves, education, reference content"],
            ["Stories", "35% reach increase (<10K)", "Interactive sticker engagement", "Community, feedback loops, daily touchpoints"],
            ["Broadcast Channels", "60-70% open rates", "Bypass algorithm entirely", "Loyal fans, product launches, exclusives"],
        ],
        col_widths=[W*0.18, W*0.25, W*0.27, W*0.30]
    ))
    story.append(sp(8))

    # Brand Video Best Practices
    story.append(p("Video Best Practices for Brands", "H2"))

    story.append(p("<b>Optimal Video Length:</b>", "H3"))
    story.append(make_table(
        ["Content Type", "Duration", "Why"],
        [
            ["Trending/viral", "7-15 seconds", "Highest completion rate, encourages replays"],
            ["Quick tips", "15-30 seconds", "Best discovery window"],
            ["Tutorials", "30-60 seconds", "Balances depth with retention"],
            ["Storytelling", "60-90 seconds", "Builds connection if well-paced"],
            ["In-depth guides", "90-180 seconds", "Requires strong retention hooks throughout"],
        ],
        col_widths=[W*0.25, W*0.20, W*0.55]
    ))
    story.append(sp(6))

    story.append(p("<b>Recommended Content Mix:</b>", "H3"))
    story.append(b("60-70% Reels (discovery and reach)"))
    story.append(b("20-30% Carousels (saves, education, depth)"))
    story.append(b("~10% Single images or culture-driven posts"))
    story.append(b("Daily Stories in addition to feed posts"))
    story.append(sp(6))

    story.append(p("<b>Posting Frequency:</b>", "H3"))
    story.append(b("3-4 Reels per week"))
    story.append(b("2-3 Carousels per week"))
    story.append(b("1-2 Static posts per week"))
    story.append(b("Consistency over volume. Fewer high-quality pieces with strong engagement outperform daily low-signal posting."))
    story.append(sp(8))

    # Brand Case Studies
    story.append(p("What Winning Brands Are Doing", "H2"))

    story.append(p("<b>Duolingo</b> -- Intentionally chaotic Reels force users to pause, replay, and comment. Leans into narrative risk and cultural responsiveness.", "Body"))
    story.append(sp(3))
    story.append(p("<b>CeraVe</b> -- 'Michael CeraVe' campaign blended offline PR with online lore, rewarding attention, rewatching, and community speculation.", "Body"))
    story.append(sp(3))
    story.append(p("<b>Glossier</b> -- Succeeds through educational captions explaining product usage in natural language (Instagram SEO play).", "Body"))
    story.append(sp(3))
    story.append(p("<b>Fenty Beauty</b> -- 'F Club' Broadcast Channel (38,300 members) for product launches and exclusives. Direct-to-fan communication.", "Body"))
    story.append(sp(3))
    story.append(p("<b>Shake Shack</b> -- 4,000-member broadcast channel using polls for menu decisions. Community co-creation.", "Body"))
    story.append(sp(3))
    story.append(p("<font color='#e94560'><b>Key Insight:</b></font> A roofing company's 15-second Reel of crew tearing off shingles in the rain got 3x the engagement of a competitor's professionally edited brand video. Authenticity wins.", "Callout"))
    story.append(sp(8))

    # Collaboration Strategy
    story.append(p("Collaboration & Partnership Strategy", "H2"))
    story.append(b("Instagram supports up to 5 collaborators per post"))
    story.append(b("Collab posts can generate <b>4.78x more impressions</b> vs solo posts"))
    story.append(b("78% of brands now use influencer partnerships as core marketing"))
    story.append(b("Cross-niche collabs outperform same-niche partnerships"))
    story.append(b("Smaller, engaged audiences are worth more than ever"))
    story.append(sp(6))

    # B2B / Service Business
    story.append(p("'Boring' B2B / Service Business Strategy", "H2"))
    story.append(b("Construction/manufacturing averages <b>4.4% engagement</b> (higher than retail or entertainment!)"))
    story.append(b("Best formats: before-and-after Reels, quick-tip carousels, day-in-the-life Stories, team spotlights"))
    story.append(b("Smartphone footage with natural light consistently outperforms studio quality"))
    story.append(b("36% of Instagram users now use the platform as a search engine"))
    story.append(b("1 in 4 business owners report SEO-optimized Instagram content drives more traffic than paid ads"))
    story.append(sp(6))

    # UGC Strategy for Brands
    story.append(p("UGC Video Strategy for Brands", "H2"))
    story.append(p("User-generated content is the fastest way to produce authentic, high-performing video at scale. Brands using UGC in their Instagram strategy see:", "Body"))
    story.append(b("Higher trust: audiences trust real creators over polished brand content"))
    story.append(b("Lower cost: UGC starts at ~$49/video vs $5K-$50K for agency production"))
    story.append(b("Faster turnaround: 5-7 business days vs weeks/months with agencies"))
    story.append(b("Creative variety: multiple creator perspectives vs single brand voice"))
    story.append(b("Algorithm alignment: authentic content matches Instagram's 'raw content' initiative"))
    story.append(sp(4))
    story.append(p("<font color='#e94560'><b>Pro Tip:</b></font> Use a platform like <b>Passionbits</b> (passionbits.io) to match with vetted creators from a 3,000+ global network. Order videos in 5 minutes, get delivery in 5-7 days, with up to 4 revision rounds.", "Callout"))

    story.append(PageBreak())

    # ============================================================
    # CHAPTER 5: 110 HOOKS
    # ============================================================
    story.append(p("Chapter 5", "ChapterNum"))
    story.append(p("110 Viral Hooks That Stop the Scroll", "ChapterTitle"))
    story.append(hr())
    story.append(sp(6))

    story.append(p("Use these as opening lines for your Reels. Adapt to your niche and brand voice.", "Body"))
    story.append(sp(4))

    # Curiosity Hooks
    story.append(p("Curiosity & Question Hooks", "H2"))
    curiosity = [
        "I wish someone told me this sooner...",
        "Stop scrolling if you want to...",
        "Have you ever wondered why...?",
        "This one mistake is costing you...",
        "The secret nobody talks about...",
        "What if I told you...",
        "Here's what they don't want you to know...",
        "If you're still struggling with...",
        "You won't believe what happened next...",
        "I was today years old when I learned this...",
    ]
    for i, hook in enumerate(curiosity, 1):
        story.append(bs(f"<b>{i}.</b> {hook}"))
    story.append(sp(6))

    # Problem-Solution Hooks
    story.append(p("Problem-Solution Hooks", "H2"))
    problem = [
        "Struggling with [problem]? Try this...",
        "Tired of [issue]? Here's the fix...",
        "If you hate [common pain], watch this...",
        "This changed everything for me...",
        "Stop wasting time on [bad habit]...",
        "The easiest way to [goal]...",
        "How I fixed [problem] in 3 days...",
        "The one thing that finally worked...",
        "No more [pain] -- here's how...",
        "Level up your [skill] with this...",
    ]
    for i, hook in enumerate(problem, 11):
        story.append(bs(f"<b>{i}.</b> {hook}"))
    story.append(sp(6))

    # Bold Statement Hooks
    story.append(p("Bold Statement & Shock Hooks", "H2"))
    bold = [
        "This is the best [thing] I've ever tried...",
        "I can't believe this actually worked...",
        "Everyone is wrong about...",
        "This is why you're not growing...",
        "The truth about [topic]...",
        "You've been lied to...",
        "This is a game-changer...",
        "I was shocked when I found out...",
        "Everything you know about [topic] is wrong...",
        "You're wasting your money on [common strategy]...",
    ]
    for i, hook in enumerate(bold, 21):
        story.append(bs(f"<b>{i}.</b> {hook}"))
    story.append(sp(6))

    # Story Hooks
    story.append(p("Story & Relatable Hooks", "H2"))
    story_hooks = [
        "I used to hate [thing] until...",
        "My biggest mistake was...",
        "The day everything changed...",
        "I tried this for 30 days...",
        "Here's what nobody tells you...",
        "From broke to [result]...",
        "The moment I realized...",
        "I almost gave up until...",
        "Here's how I completely failed at [task]...",
        "The biggest lesson after [timeframe] in [industry]...",
    ]
    for i, hook in enumerate(story_hooks, 31):
        story.append(bs(f"<b>{i}.</b> {hook}"))
    story.append(sp(6))

    # Number Hooks
    story.append(p("Number & List Hooks", "H2"))
    number = [
        "3 mistakes you're making...",
        "5 things I wish I knew...",
        "7 ways to [goal]...",
        "Only 1% of people know this...",
        "The 4-step method to...",
        "6 hacks that actually work...",
        "5-minute trick for...",
        "10 tools that will save you hours...",
        "The 3-second rule that changes everything...",
        "8 signs you need to change your [strategy]...",
    ]
    for i, hook in enumerate(number, 41):
        story.append(bs(f"<b>{i}.</b> {hook}"))
    story.append(sp(6))

    # Challenge Hooks
    story.append(p("Challenge & Bet Hooks", "H2"))
    challenge = [
        "Bet you can't do this...",
        "Watch till the end if you dare...",
        "I bet this will surprise you...",
        "This will blow your mind...",
        "Can you guess what happens next?",
        "Prove me wrong...",
        "I dare you to try this for one week...",
        "You'll never look at [thing] the same way...",
        "Try this tonight and tell me it doesn't work...",
        "Name one person who doesn't need this...",
    ]
    for i, hook in enumerate(challenge, 51):
        story.append(bs(f"<b>{i}.</b> {hook}"))
    story.append(sp(6))

    # Value Hooks
    story.append(p("Value Promise & Transformation Hooks", "H2"))
    value = [
        "How to get [result] fast...",
        "Transform your [thing] in...",
        "This hack saved me hours...",
        "Double your [metric] with this...",
        "From zero to [result]...",
        "The fastest way to...",
        "Get [goal] without...",
        "The exact framework I use to [result]...",
        "Don't buy [product] until you know these [number] things...",
        "How to [achieve goal] without [common pain point]...",
    ]
    for i, hook in enumerate(value, 61):
        story.append(bs(f"<b>{i}.</b> {hook}"))
    story.append(sp(6))

    # Emotional Hooks
    story.append(p("Emotional & Relatable Hooks", "H2"))
    emotional = [
        "If you've ever felt...",
        "You're not alone if...",
        "I felt so seen when...",
        "This gave me chills...",
        "POV: You just discovered...",
        "Wait for it...",
        "The glow-up you didn't expect...",
        "Stop what you're doing...",
        "Real talk...",
        "This is your sign...",
    ]
    for i, hook in enumerate(emotional, 71):
        story.append(bs(f"<b>{i}.</b> {hook}"))
    story.append(sp(6))

    # Professional Hooks
    story.append(p("Professional / Business Hooks", "H2"))
    professional = [
        "Are you making this common [industry] mistake?",
        "What if [common belief] is completely wrong?",
        "Do you know the #1 reason [problem] happens?",
        "Is [common tactic] actually hurting your business?",
        "Unpopular opinion: [contrarian view]...",
        "I'm going to get a lot of hate for this, but...",
        "If you're a [job title], you need to hear this.",
        "Attention [target audience]!",
        "It's 2026, and you're still [doing outdated practice]?",
        "My predictions for [topic] in the next [timeframe]...",
    ]
    for i, hook in enumerate(professional, 81):
        story.append(bs(f"<b>{i}.</b> {hook}"))
    story.append(sp(6))

    # Contrarian Hooks
    story.append(p("Contrarian & Myth-Busting Hooks", "H2"))
    contrarian = [
        "The biggest lie about [topic]...",
        "Why I stopped doing this even though everyone recommends it...",
        "Stop doing [common practice]. Do this instead.",
        "Forget everything you know about [topic]...",
        "The biggest myth is completely backwards...",
        "Everyone preaches [thing]. The paradox: doing the opposite works.",
        "I cracked the [industry] code everyone is gatekeeping...",
        "What [famous brand]'s team actually does (not what they tell you)...",
        "The counterintuitive habit shared by every [successful person]...",
        "Teams with less [thing] outperform those with more...",
    ]
    for i, hook in enumerate(contrarian, 91):
        story.append(bs(f"<b>{i}.</b> {hook}"))
    story.append(sp(6))

    # Niche-Targeted Hooks
    story.append(p("Niche-Targeted Hooks", "H2"))
    niche = [
        "A message to every [job title] who feels [frustration]...",
        "What the latest [platform] update means for your business.",
        "[Number] tips to fix your [problem] in under [timeframe].",
        "I'm sharing something I probably shouldn't...",
        "This is for all the [type of person] struggling with...",
        "Somebody had to say it...",
        "Don't sleep on this...",
        "Here's the tea...",
        "Truth bomb incoming...",
        "Quick tip that took me [timeframe] to learn...",
    ]
    for i, hook in enumerate(niche, 101):
        story.append(bs(f"<b>{i}.</b> {hook}"))

    story.append(PageBreak())

    # ============================================================
    # CHAPTER 6: CONTENT FRAMEWORKS
    # ============================================================
    story.append(p("Chapter 6", "ChapterNum"))
    story.append(p("Content Frameworks & Posting Strategy", "ChapterTitle"))
    story.append(hr())
    story.append(sp(6))

    # 4-Pillar Framework
    story.append(p("The Four-Pillar Content Mix", "H1"))
    story.append(make_table(
        ["Pillar", "Percentage", "Content Types", "Goal"],
        [
            ["Value Content", "40%", "Tips, education, tutorials, how-tos", "Build trust & authority"],
            ["Relatable Content", "25%", "Pain points, humor, trends, POV", "Build reach & shares"],
            ["Behind-the-Scenes", "20%", "Process, team, authenticity, BTS", "Build connection"],
            ["Promotional", "15%", "Products, services, CTAs, launches", "Drive conversions"],
        ],
        col_widths=[W*0.18, W*0.12, W*0.38, W*0.32]
    ))
    story.append(sp(8))

    # 3 E's Framework
    story.append(p("The Three E's Framework", "H2"))
    story.append(p("Every Reel should <b>Educate, Entertain, or Inspire</b>. Ask: 'What is the viewer getting out of this?'", "Body"))
    story.append(b("<b>Educational Reels</b> build trust and authority. Highest save rate."))
    story.append(b("<b>Entertainment Reels</b> build reach and shareability. Highest share rate."))
    story.append(b("<b>Inspirational Reels</b> build saves and emotional connection. Highest rewatch rate."))
    story.append(sp(8))

    # Hero-Hub-Help
    story.append(p("Hero-Hub-Help Framework", "H2"))
    story.append(make_table(
        ["Type", "Percentage", "Description", "Examples"],
        [
            ["Hero", "5-10%", "Bold, high-production campaigns for maximum reach", "Launches, collabs, viral attempts"],
            ["Hub", "50-60%", "Regular series that keeps audience coming back", "Weekly series, recurring formats"],
            ["Help", "30-40%", "Always-on, evergreen problem-solving resources", "Tutorials, FAQs, how-tos"],
        ],
        col_widths=[W*0.10, W*0.12, W*0.43, W*0.35]
    ))
    story.append(sp(8))

    # Customer Journey Framework
    story.append(p("Customer Journey Content Map", "H2"))
    story.append(make_table(
        ["Stage", "Content Type", "Goal", "Metrics to Track"],
        [
            ["Awareness", "Entertaining, relatable, trend-based Reels", "Broad reach, new eyeballs", "Reach, impressions, views"],
            ["Consideration", "Educational, tutorial, comparison content", "Build trust, demonstrate expertise", "Saves, watch time, profile visits"],
            ["Decision", "Testimonial, product demo, transformation Reels", "Convert viewers to customers", "Link clicks, DMs, comments"],
        ],
        col_widths=[W*0.15, W*0.30, W*0.25, W*0.30]
    ))
    story.append(sp(8))

    # Content Repurposing
    story.append(p("Content Repurposing Pipeline", "H2"))
    story.append(p("One pillar piece converts into 10+ assets:", "Body"))
    story.append(b("Long-form video becomes 3-5 Reels clips"))
    story.append(b("Reels become carousel posts"))
    story.append(b("Audio becomes voiceover for B-roll Reels"))
    story.append(b("Key points become text-overlay Reels"))
    story.append(b("Results/data become infographic carousels"))
    story.append(sp(8))

    # Posting Times by Content Type
    story.append(p("Best Posting Times by Content Type", "H2"))
    story.append(make_table(
        ["Time Window", "Best For", "Why"],
        [
            ["7-9 AM local", "Educational / professional content", "Morning commute, learning mindset"],
            ["11 AM-1 PM local", "Entertainment / quick tips", "Peak engagement, lunch break scroll"],
            ["5-7 PM local", "Lifestyle / relatable content", "Post-work relaxation mode"],
            ["10 PM-12 AM local", "Entertainment / longer content", "Highest average views (25K). Night scrolling."],
        ],
        col_widths=[W*0.20, W*0.35, W*0.45]
    ))

    story.append(PageBreak())

    # ============================================================
    # CHAPTER 7: TOOLS & FEATURES
    # ============================================================
    story.append(p("Chapter 7", "ChapterNum"))
    story.append(p("Tools, Features & Platform Updates", "ChapterTitle"))
    story.append(hr())
    story.append(sp(6))

    story.append(p("Instagram Features to Leverage in 2026", "H1"))

    story.append(make_table(
        ["Feature", "What It Does", "How to Use It"],
        [
            ["Trial Reels", "Test content with non-followers before committing", "A/B test hooks, formats, and topics risk-free. 80% saw more non-follower reach."],
            ["Instagram Edits App", "Native video editor. 4K export, no watermark, teleprompter", "Replace CapCut. Built-in insights tab for performance tracking."],
            ["Broadcast Channels", "Direct messaging to opt-in subscribers", "60-70% open rates. Use for product launches, exclusives, polls."],
            ["Notes", "60-char ephemeral messages in DM inbox", "Daily conversation starters. Trigger DM-based ranking signals."],
            ["Collaborative Posts", "Up to 5 collaborators per post", "Cross-niche collabs. 4.78x more impressions than solo posts."],
            ["Reels Templates", "Pre-built timing, transitions, audio sync", "Under 5 min per Reel. Template Reels perform equally to hand-edited."],
            ["Reels Polls", "Polls in Reels comments (beyond Stories)", "New engagement driver. Boosts comment volume."],
            ["Meta AI Restyle", "Edit photos/videos with text prompts", "Quick visual editing for Stories content."],
            ["Enhanced Analytics", "Post-level demographics, follower growth by post", "Track which content converts followers. Optimize content mix."],
            ["Instagram Search SEO", "Captions indexed like SEO copy", "Use keywords in captions. 30% more reach than hashtag-heavy posts."],
        ],
        col_widths=[W*0.20, W*0.35, W*0.45]
    ))
    story.append(sp(8))

    story.append(p("Production Specifications Cheat Sheet", "H2"))
    story.append(make_table(
        ["Element", "Specification"],
        [
            ["Reels / Stories format", "9:16 vertical (1080 x 1920 px)"],
            ["Feed video format", "3:4 (1080 x 1440 px) or 4:5 (1080 x 1350 px)"],
            ["Text safe zone", "Center 80% of frame (1080 x 1440 px)"],
            ["Captions", "Always include -- 85% watch without sound"],
            ["Audio", "Required for recommendation eligibility"],
            ["Watermarks", "Remove all cross-platform watermarks"],
            ["Hook timing", "Movement or visual change in first 1.5 seconds"],
            ["Cut frequency", "Every 1.5-3 seconds for maximum retention"],
            ["Caption keywords", "Include target keywords naturally (Instagram SEO)"],
            ["Hashtags", "3-5 relevant, in caption (not first comment)"],
        ],
        col_widths=[W*0.30, W*0.70]
    ))

    story.append(PageBreak())

    # ============================================================
    # CHAPTER 8: METRICS & BENCHMARKS
    # ============================================================
    story.append(p("Chapter 8", "ChapterNum"))
    story.append(p("Key Metrics & Benchmarks", "ChapterTitle"))
    story.append(hr())
    story.append(sp(6))

    # Engagement Benchmarks
    story.append(p("Engagement Rate Benchmarks (2025-2026)", "H1"))
    story.append(make_table(
        ["Content Type", "2024 Rate", "2025 Rate", "YoY Change"],
        [
            ["Carousels", "0.55%", "0.55%", "Stable"],
            ["Reels", "0.50%", "0.52%", "+0.02%"],
            ["Images", "0.45%", "0.37%", "-17%"],
            ["Overall Average", "--", "0.48%", "-24% YoY"],
        ],
        col_widths=[W*0.25, W*0.25, W*0.25, W*0.25]
    ))
    story.append(sp(8))

    story.append(p("Healthy Engagement Targets by Account Size", "H2"))
    story.append(make_table(
        ["Account Size", "Target Range", "Notes"],
        [
            ["Under 5K followers", "8-10%", "Highest engagement potential"],
            ["5K - 100K followers", "5-7%", "Growth phase"],
            ["100K+ followers", "3-4%", "Scale phase"],
            ["General 'good' range", "3-6%", "--"],
            ["Excellent", "6%+", "Top performer"],
        ],
        col_widths=[W*0.30, W*0.25, W*0.45]
    ))
    story.append(sp(8))

    # Average Views
    story.append(p("Average Views by Account Size", "H2"))
    story.append(make_table(
        ["Followers", "Reels Views", "Carousel Views", "Image Views"],
        [
            ["1-5K", "580", "993", "417"],
            ["5-10K", "1,000", "2,117", "1,068"],
            ["10-50K", "2,460", "4,275", "2,340"],
            ["50-100K", "6,095", "11,597", "7,405"],
            ["100K-1M", "16,035", "35,370", "22,900"],
        ],
        col_widths=[W*0.20, W*0.25, W*0.28, W*0.27]
    ))
    story.append(sp(8))

    # Viral Thresholds
    story.append(p("Viral Thresholds", "H2"))
    story.append(make_table(
        ["Account Size", "Viral = This Many Views"],
        [
            ["Under 10K followers", "50K-100K views"],
            ["10K - 100K followers", "250K-500K views"],
            ["100K+ followers", "1M+ views"],
        ],
        col_widths=[W*0.40, W*0.60]
    ))
    story.append(sp(8))

    # Year-over-Year Changes
    story.append(p("Year-over-Year Platform Changes (2025)", "H2"))
    story.append(make_table(
        ["Metric", "Change", "Implication"],
        [
            ["Posts published", "+21%", "More competition for attention"],
            ["Reels published", "+35%", "Reels dominate content volume"],
            ["Average post reach", "-31%", "Organic reach declining"],
            ["Reels reach", "-35%", "More Reels = more competition per Reel"],
            ["Overall engagement", "-24% to -26%", "Quality and relevance matter more than ever"],
            ["Instagram ad reach", "+12.2%", "Paid reach still growing"],
        ],
        col_widths=[W*0.25, W*0.20, W*0.55]
    ))
    story.append(sp(8))

    # Influencer Stats
    story.append(p("Influencer & Creator Economy Stats", "H2"))
    story.append(b("Nano-influencers (1K-10K): 8%+ engagement, 2-3x higher conversion rates"))
    story.append(b("Nano-influencers make up 75.9% of all Instagram influencers"))
    story.append(b("Micro-influencers: 60% higher engagement at 1/10th cost of macro"))
    story.append(b("Average creator earns $288 per sponsored Reel"))
    story.append(b("U.S. creator economy investment: $37B in 2025, projected $44B in 2026"))
    story.append(b("Carousel ads deliver 111% higher ROAS than normal ads"))
    story.append(b("Over 50% of all Instagram ads now run in Reels format (up from 35% in 2024)"))
    story.append(b("Brands getting $4.12 return for every $1 spent on Instagram campaigns"))
    story.append(sp(8))

    # Key Takeaways Box
    story.append(p("Platform Summary: What Works in 2026", "H2"))
    story.append(stat_box([
        ("DM Shares", "Signal #1"),
        ("3-5", "Hashtags\nMax"),
        ("60%+", "3-Sec Hold\nRate Target"),
        ("3-5/wk", "Reel Posting\nFrequency"),
    ], W))

    story.append(sp(20))
    story.append(hr())
    story.append(sp(10))

    # Footer
    story.append(p("<b>The Instagram Playbook 2025-2026</b>", "Footer"))
    story.append(p("Created by <b>Passionbits</b> | passionbits.io", "Footer"))
    story.append(p("AI-Powered Video Production for Brands | 3,000+ Global Creators | Starting at $49/video", "Footer"))
    story.append(sp(6))
    story.append(p("Need authentic video content for your Instagram? Visit passionbits.io to get started.", "Footer"))

    doc.build(story)
    print(f"PDF saved to: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
