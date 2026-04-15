#!/usr/bin/env python3
"""Generate SEO Audit PDF report for Passionbits.io using reportlab."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib import colors
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "seo-audit-report.pdf")

# Colors
PRIMARY = HexColor("#1a1a2e")
ACCENT = HexColor("#e94560")
LIGHT_BG = HexColor("#f5f5f5")
DARK_BG = HexColor("#1a1a2e")
GREEN = HexColor("#27ae60")
ORANGE = HexColor("#f39c12")
RED = HexColor("#e74c3c")
BLUE = HexColor("#3498db")
GRAY = HexColor("#7f8c8d")
WHITE_BG = HexColor("#ffffff")
TABLE_HEADER = HexColor("#2c3e50")
TABLE_ALT = HexColor("#ecf0f1")

styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    "CoverTitle", parent=styles["Title"],
    fontSize=28, leading=34, textColor=PRIMARY,
    spaceAfter=6, alignment=TA_LEFT
))
styles.add(ParagraphStyle(
    "CoverSub", parent=styles["Normal"],
    fontSize=14, leading=18, textColor=GRAY,
    spaceAfter=20
))
styles.add(ParagraphStyle(
    "H1", parent=styles["Heading1"],
    fontSize=20, leading=24, textColor=PRIMARY,
    spaceBefore=24, spaceAfter=12,
    borderPadding=(0, 0, 4, 0)
))
styles.add(ParagraphStyle(
    "H2", parent=styles["Heading2"],
    fontSize=15, leading=19, textColor=PRIMARY,
    spaceBefore=16, spaceAfter=8
))
styles.add(ParagraphStyle(
    "H3", parent=styles["Heading3"],
    fontSize=12, leading=15, textColor=HexColor("#34495e"),
    spaceBefore=12, spaceAfter=6
))
styles.add(ParagraphStyle(
    "BodyText2", parent=styles["Normal"],
    fontSize=10, leading=14, textColor=HexColor("#2c3e50"),
    spaceAfter=6
))
styles.add(ParagraphStyle(
    "BulletCustom", parent=styles["Normal"],
    fontSize=10, leading=14, textColor=HexColor("#2c3e50"),
    leftIndent=20, spaceAfter=3,
    bulletIndent=8, bulletFontSize=10
))
styles.add(ParagraphStyle(
    "CriticalTag", parent=styles["Normal"],
    fontSize=10, leading=12, textColor=white,
    backColor=RED, alignment=TA_CENTER
))
styles.add(ParagraphStyle(
    "HighTag", parent=styles["Normal"],
    fontSize=10, leading=12, textColor=white,
    backColor=ORANGE, alignment=TA_CENTER
))
styles.add(ParagraphStyle(
    "MedTag", parent=styles["Normal"],
    fontSize=10, leading=12, textColor=white,
    backColor=BLUE, alignment=TA_CENTER
))
styles.add(ParagraphStyle(
    "TableCell", parent=styles["Normal"],
    fontSize=9, leading=12, textColor=HexColor("#2c3e50"),
))
styles.add(ParagraphStyle(
    "TableHeader", parent=styles["Normal"],
    fontSize=9, leading=12, textColor=white,
    fontName="Helvetica-Bold"
))
styles.add(ParagraphStyle(
    "FooterStyle", parent=styles["Normal"],
    fontSize=8, leading=10, textColor=GRAY,
    alignment=TA_CENTER
))


def hr():
    return HRFlowable(width="100%", thickness=1, color=HexColor("#ddd"), spaceAfter=12, spaceBefore=6)


def spacer(h=6):
    return Spacer(1, h)


def p(text, style="BodyText2"):
    return Paragraph(text, styles[style])


def bullet(text):
    return Paragraph(f"<bullet>&bull;</bullet> {text}", styles["BulletCustom"])


def make_table(headers, rows, col_widths=None):
    """Create a styled table."""
    header_cells = [Paragraph(h, styles["TableHeader"]) for h in headers]
    data = [header_cells]
    for row in rows:
        data.append([Paragraph(str(c), styles["TableCell"]) for c in row])

    t = Table(data, colWidths=col_widths, repeatRows=1)
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#bdc3c7")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
    # Alternate row colors
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(("BACKGROUND", (0, i), (-1, i), TABLE_ALT))

    t.setStyle(TableStyle(style_cmds))
    return t


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
        topMargin=0.75*inch, bottomMargin=0.75*inch
    )

    story = []
    W = doc.width

    # --- COVER ---
    story.append(spacer(40))
    story.append(p("SEO Audit Report", "CoverTitle"))
    story.append(p("passionbits.io", "CoverSub"))
    story.append(hr())
    story.append(spacer(12))
    story.append(p("<b>Audit Date:</b> April 4, 2026"))
    story.append(p("<b>Site:</b> https://passionbits.io"))
    story.append(p("<b>Platform:</b> Next.js (main site) + WordPress/Yoast (blog)"))
    story.append(p("<b>Overall Health:</b> <font color='#e74c3c'><b>Critical issues found</b></font>"))
    story.append(spacer(20))

    story.append(p("<b>Top 5 Priority Issues</b>", "H2"))
    issues = [
        ("CRITICAL", "Next.js pages serve empty HTML to crawlers — homepage, pricing, alternatives, location pages all invisible to search engines"),
        ("HIGH", "Main sitemap has only 9 URLs — missing 80+ blog posts, 4+ location pages, 2+ alternative pages"),
        ("HIGH", "No sitemap reference in robots.txt"),
        ("MEDIUM", "No hreflang tags despite targeting India, US, UK markets"),
        ("CRITICAL", "Alternative/competitor pages (/alternatives/*) serve zero content — highest-intent SEO pages are invisible"),
    ]
    for priority, desc in issues:
        color = "#e74c3c" if priority == "CRITICAL" else "#f39c12" if priority == "HIGH" else "#3498db"
        story.append(bullet(f"<font color='{color}'><b>[{priority}]</b></font> {desc}"))
    story.append(spacer(12))

    # Key stat boxes
    stat_data = [
        ["9", "80", "0", "0"],
        ["Pages in\nMain Sitemap", "Blog Posts\n(Separate Sitemap)", "Schema Markup\non Main Site", "Meta Tags on\nMain Site Pages"],
    ]
    stat_table = Table(stat_data, colWidths=[W/4]*4)
    stat_table.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 24),
        ("FONTSIZE", (0, 1), (-1, 1), 8),
        ("TEXTCOLOR", (0, 0), (-1, 0), ACCENT),
        ("TEXTCOLOR", (0, 1), (-1, 1), GRAY),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("BOX", (0, 0), (-1, -1), 1, HexColor("#ddd")),
        ("LINEBEFORE", (1, 0), (1, -1), 0.5, HexColor("#ddd")),
        ("LINEBEFORE", (2, 0), (2, -1), 0.5, HexColor("#ddd")),
        ("LINEBEFORE", (3, 0), (3, -1), 0.5, HexColor("#ddd")),
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_BG),
    ]))
    story.append(stat_table)

    story.append(PageBreak())

    # --- TECHNICAL SEO ---
    story.append(p("Technical SEO Findings", "H1"))
    story.append(hr())

    # Issue 1
    story.append(p("1. Client-Side Rendering Blocks Crawlers", "H2"))
    story.append(p("<font color='#e74c3c'><b>Priority: CRITICAL</b></font> &nbsp;|&nbsp; <b>Impact: Blocks all on-page SEO for main site</b>"))
    story.append(spacer(6))
    story.append(p("<b>Issue:</b> All Next.js pages (homepage, pricing, about, alternatives, location, creator) return HTML containing only tracking scripts (GTM, Clarity), font declarations, and a Next.js config object. Zero visible content, zero meta tags, zero headings, zero schema."))
    story.append(spacer(4))
    story.append(p("<b>Evidence:</b> Fetching homepage, pricing, /alternatives/contentbeta, /location/us/nyc all returned empty content. <font face='Courier'>nextExport: true</font> confirms static export with client-side hydration only."))
    story.append(spacer(4))
    story.append(p("<b>Fix:</b> Switch critical pages to <b>Server-Side Rendering (SSR)</b> or <b>Static Site Generation (SSG)</b> via Next.js. At minimum: homepage, pricing, all /alternatives/ pages, all /location/ pages, creator page, about-us. This single fix unblocks meta tags, H1s, canonical tags, schema, and content indexation."))
    story.append(spacer(8))

    # Pages table
    story.append(p("Main Site Pages — SEO Elements in Server-Rendered HTML", "H3"))
    story.append(make_table(
        ["Page", "Title", "Description", "H1", "Schema", "Canonical", "OG"],
        [
            ["Homepage", "--", "--", "--", "--", "--", "--"],
            ["Pricing", "--", "--", "--", "--", "--", "--"],
            ["About Us", "--", "--", "--", "--", "--", "--"],
            ["/alternatives/contentbeta", "--", "--", "--", "--", "--", "--"],
            ["/alternatives/testimonial-hero", "--", "--", "--", "--", "--", "--"],
            ["/location/us/nyc", "--", "--", "--", "--", "--", "--"],
            ["/location/us/la", "--", "--", "--", "--", "--", "--"],
            ["/creator", "--", "--", "--", "--", "--", "--"],
        ],
        col_widths=[W*0.28, W*0.12, W*0.12, W*0.12, W*0.12, W*0.12, W*0.12]
    ))
    story.append(p("<i>All dashes = missing from server-rendered HTML. Elements may exist in client-rendered DOM but crawlers won't see them.</i>"))
    story.append(spacer(10))

    # Issue 2
    story.append(p("2. Sitemap Deficiencies", "H2"))
    story.append(p("<font color='#f39c12'><b>Priority: HIGH</b></font> &nbsp;|&nbsp; <b>Impact: Crawl discovery severely limited</b>"))
    story.append(spacer(6))
    story.append(p("<b>Issue:</b> Main sitemap.xml has only 9 URLs. Missing: all 80 blog posts (in separate Yoast sitemap), 4+ location pages, 2+ alternative pages, creator page."))
    story.append(spacer(4))
    story.append(p("<b>Fix:</b> (1) Add Sitemap references to robots.txt. (2) Add /location/*, /alternatives/*, /creator to main sitemap. (3) Create a sitemap index referencing both main and blog sitemaps."))
    story.append(spacer(8))

    story.append(p("Pages Missing from Sitemap", "H3"))
    missing = [
        "/alternatives/contentbeta", "/alternatives/testimonial-hero",
        "/location/us/nyc", "/location/us/la",
        "/location/us/francisco", "/location/india/jaipur",
        "/creator", "All 80 blog posts (in separate Yoast sitemap, not linked)"
    ]
    for m in missing:
        story.append(bullet(m))
    story.append(spacer(8))

    # Issue 3
    story.append(p("3. robots.txt Missing Sitemap References", "H2"))
    story.append(p("<font color='#f39c12'><b>Priority: HIGH (5-minute fix)</b></font>"))
    story.append(spacer(6))
    story.append(p("<b>Current:</b>"))
    story.append(p("<font face='Courier' size='9'>User-agent: *<br/>Disallow: /private/<br/>Allow: /public/</font>"))
    story.append(spacer(4))
    story.append(p("<b>Recommended:</b>"))
    story.append(p("<font face='Courier' size='9'>User-agent: *<br/>Disallow: /private/<br/>Disallow: /dashboard/<br/>Allow: /public/<br/><br/>Sitemap: https://passionbits.io/sitemap.xml<br/>Sitemap: https://passionbits.io/blog/sitemap.xml</font>"))
    story.append(spacer(8))

    # Issue 4-7
    story.append(p("4. No Hreflang Tags", "H2"))
    story.append(p("<font color='#3498db'><b>Priority: MEDIUM</b></font>"))
    story.append(p("Passionbits targets India, US, UK with location-specific pages but has zero hreflang implementation. Fix: Implement hreflang on location pages."))
    story.append(spacer(6))

    story.append(p("5. No Canonical Tags on Main Site", "H2"))
    story.append(p("<font color='#f39c12'><b>Priority: HIGH (bundle with SSR fix)</b></font>"))
    story.append(p("No canonical tags in initial HTML of any Next.js page. Risk of duplicate content with trailing slash and parameter variations."))
    story.append(spacer(6))

    story.append(p("6. Missing Open Graph Tags", "H2"))
    story.append(p("<font color='#3498db'><b>Priority: MEDIUM</b></font>"))
    story.append(p("No OG tags on any page. For a video marketing brand active on social media, shared links look generic/broken on LinkedIn, Twitter, and Facebook."))
    story.append(spacer(6))

    story.append(p("7. Blog/Main Site Integration Gap", "H2"))
    story.append(p("<font color='#3498db'><b>Priority: MEDIUM</b></font>"))
    story.append(p("Blog (WordPress/Yoast) and main site (Next.js) have separate sitemaps, separate CMS, no shared navigation. Link equity from 80 blog posts may not flow to commercial pages (pricing, alternatives, creator)."))

    story.append(PageBreak())

    # --- CONTENT FINDINGS ---
    story.append(p("Content Findings", "H1"))
    story.append(hr())

    story.append(p("Blog Content Volume: 80 Posts", "H2"))
    story.append(make_table(
        ["Category", "Posts (approx)", "Topics"],
        [
            ["Social media trends", "~40", "Monthly TikTok/Instagram trends for US and India"],
            ["Industry guides", "~15", "Real estate, insurance, fintech, SaaS marketing"],
            ["Competitor comparisons", "~7", "Content Beta, Testimonial Hero, Billo, HeyGen, MakeUGC"],
            ["Case studies", "~6", "Vibiz.ai, Parakeet AI, Bigged, Blort AI, Klap, Flowith"],
            ["UGC education", "~5", "What is UGC, creating UGC, mastering UGC content"],
            ["YouTube/ads guides", "~7", "YouTube SEO, YouTube ads, Facebook ads for insurance"],
        ],
        col_widths=[W*0.25, W*0.15, W*0.60]
    ))
    story.append(spacer(12))

    story.append(p("Content Gaps", "H2"))
    story.append(make_table(
        ["Gap", "Search Potential", "Priority"],
        [
            ['"UGC platform" / "video production platform" pillar page', "High", "HIGH"],
            ['"UGC creator pricing" comprehensive guide', "High", "HIGH"],
            ["Video marketing ROI / benchmarks (original research)", "Medium", "HIGH"],
            ["Location pages with actual local content", "Medium", "MEDIUM"],
            ["Blog listing pagination (only 6 of 80 posts visible)", "--", "MEDIUM"],
        ],
        col_widths=[W*0.55, W*0.20, W*0.15]
    ))
    story.append(spacer(12))

    story.append(p("Keyword Cannibalization Risk", "H2"))
    story.append(p("Multiple posts target similar queries with Part 1/Part 2 splits and monthly variations. Example: 'Instagram trends US consumer February Part 1' competes with 'Part 2' and with 'March Part 1'. <b>Fix:</b> Consolidate Part 1/Part 2 into single posts. Update previous months rather than creating new posts."))
    story.append(spacer(6))

    story.append(p("Blog SEO Status (Yoast)", "H2"))
    story.append(make_table(
        ["Element", "Status", "Action"],
        [
            ["Meta title", "Present", "OK"],
            ["Meta description", "Present", "OK"],
            ["Schema markup", "Present (WebPage, Breadcrumb, Person)", "OK"],
            ["H1 on listing page", "Missing", "Add H1"],
            ["Canonical tags", "Not detected", "Verify in Yoast"],
            ["Open Graph tags", "Not detected", "Enable in Yoast Social"],
            ["URL slugs", "Excessively long (70-85 chars)", "Shorten for future posts"],
            ['"Uncategorized" category', "Present in sitemap", "Remove or noindex"],
        ],
        col_widths=[W*0.30, W*0.35, W*0.25]
    ))

    story.append(PageBreak())

    # --- ACTION PLAN ---
    story.append(p("Prioritized Action Plan", "H1"))
    story.append(hr())

    story.append(p("Phase 1: Critical Fixes (Blocking Indexation)", "H2"))
    story.append(make_table(
        ["#", "Action", "Effort", "Impact"],
        [
            ["1", "Switch to SSR/SSG for all main site pages", "High (dev)", "Unlocks ALL on-page SEO"],
            ["2", "Add meta title + description to all pages", "Bundled with #1", "High"],
            ["3", "Add H1 to all pages", "Bundled with #1", "High"],
            ["4", "Add self-referencing canonical tags", "Bundled with #1", "High"],
            ["5", "Add schema (Organization, Product, FAQPage)", "Bundled with #1", "High"],
        ],
        col_widths=[W*0.06, W*0.48, W*0.20, W*0.26]
    ))
    story.append(spacer(12))

    story.append(p("Phase 2: High-Impact Improvements", "H2"))
    story.append(make_table(
        ["#", "Action", "Effort", "Impact"],
        [
            ["6", "Add sitemap references to robots.txt", "5 min", "High"],
            ["7", "Add location + alternative pages to sitemap", "30 min", "High"],
            ["8", "Internal links from blog to commercial pages", "Medium", "High"],
            ["9", 'Create "UGC video platform" pillar page', "Medium", "High"],
            ["10", "Implement hreflang for location pages", "Medium", "Medium"],
            ["11", "Add Open Graph tags to all pages", "Low", "Medium"],
        ],
        col_widths=[W*0.06, W*0.48, W*0.20, W*0.26]
    ))
    story.append(spacer(12))

    story.append(p("Phase 3: Quick Wins", "H2"))
    story.append(make_table(
        ["#", "Action", "Effort", "Impact"],
        [
            ["12", "Enable OG + verify canonical in Yoast", "10 min", "Medium"],
            ["13", "Add H1 to blog listing page", "5 min", "Low"],
            ["14", 'Remove/noindex "uncategorized" category', "5 min", "Low"],
            ["15", "Add blog link to main site navigation", "Low", "Medium"],
        ],
        col_widths=[W*0.06, W*0.48, W*0.20, W*0.26]
    ))
    story.append(spacer(12))

    story.append(p("Phase 4: Long-Term Growth", "H2"))
    story.append(make_table(
        ["#", "Action"],
        [
            ["16", 'Create "UGC creator pricing" guide (high search volume)'],
            ["17", "Create original research (video marketing benchmarks, UGC ROI data)"],
            ["18", "Consolidate Part 1/Part 2 trend posts into single comprehensive posts"],
            ["19", "Build more /alternatives/ pages (Billo, Insense, HeyGen, MakeUGC) with SSR"],
            ["20", "Expand location pages with unique local content per city"],
            ["21", "Fix blog pagination to surface all 80 posts"],
            ["22", "Shorten future blog URL slugs"],
            ["23", "Consolidate thin blog categories"],
            ["24", "Monthly competitor monitoring (contentbeta.com, testimonialhero.com, billo.app, insense.pro)"],
        ],
        col_widths=[W*0.06, W*0.94]
    ))

    story.append(spacer(20))
    story.append(hr())
    story.append(spacer(6))
    story.append(p("<b>Key Takeaway:</b> The #1 priority is fixing the Next.js rendering. Until the main site serves real HTML to crawlers, everything else (schema, meta tags, content optimization) is invisible to search engines. The WordPress blog is carrying all organic weight right now -- connect it better to commercial pages while fixing the main site rendering.", "BodyText2"))

    story.append(spacer(20))
    story.append(p("Competitors to Benchmark", "H2"))
    story.append(make_table(
        ["Competitor", "Domain", "Compare"],
        [
            ["Content Beta", "contentbeta.com", "DA, indexed pages, top keywords, page speed"],
            ["Testimonial Hero", "testimonialhero.com", "DA, indexed pages, top keywords"],
            ["Billo", "billo.app", "DA, indexed pages, top keywords"],
            ["Insense", "insense.pro", "DA, indexed pages, top keywords"],
        ],
        col_widths=[W*0.20, W*0.30, W*0.50]
    ))

    story.append(spacer(30))
    story.append(hr())
    story.append(p("Generated on April 4, 2026 | Passionbits.io SEO Audit", "FooterStyle"))

    doc.build(story)
    print(f"PDF saved to: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
