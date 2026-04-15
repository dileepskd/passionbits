# Passionbits.io SEO Audit Report

*Audit date: 2026-04-04*
*Site: https://passionbits.io*

---

## Executive Summary

**Overall health: Critical issues found.** The main passionbits.io site has a fundamental rendering problem — almost all pages serve **empty HTML** to crawlers (no meta tags, no headings, no content, no schema). The blog (WordPress/Yoast) is in better shape with basic SEO elements, but has its own issues. Google has indexed some pages despite the rendering problem, but massive ranking potential is being left on the table.

### Top 5 Priority Issues

1. **Next.js pages serve empty HTML to crawlers** — homepage, pricing, alternatives, location, creator pages all invisible
2. **Main sitemap has only 9 URLs** — missing 80+ blog posts, 4+ location pages, 2+ alternative pages
3. **No sitemap reference in robots.txt**
4. **No hreflang tags** despite targeting India, US, UK markets
5. **Alternative/competitor pages (/alternatives/*) serve zero content** — highest-intent SEO pages are invisible

---

## Site Architecture Overview

```
passionbits.io (Next.js — client-side rendered, mostly empty HTML)
├── / (homepage)
├── /pricing
├── /about-us
├── /contact
├── /case-studies
├── /creator
├── /alternatives/contentbeta
├── /alternatives/testimonial-hero
├── /location/us/nyc
├── /location/us/la
├── /location/us/francisco
├── /location/india/jaipur
├── /terms-condition
├── /privacy
├── /refund
│
├── /blog/ (WordPress + Yoast SEO — separate CMS)
│   ├── 80 blog posts (trend reports, guides, case studies, competitor comparisons)
│   └── 16 category pages
│
└── creator.passionbits.io (separate subdomain — creator dashboard)
```

---

## Technical SEO Findings

### 1. Client-Side Rendering Blocks Crawlers

| Detail | |
|--------|--|
| **Issue** | All Next.js pages return HTML containing only tracking scripts (GTM, Clarity), font declarations, and a Next.js config object. Zero visible content, zero meta tags, zero headings. |
| **Impact** | **CRITICAL** — Google can render JS but deprioritizes JS-heavy pages. Bing, DuckDuckGo may not render at all. AI bots (GPTBot, PerplexityBot, ClaudeBot) cannot read these pages. |
| **Evidence** | Fetching homepage, pricing, /alternatives/contentbeta, /location/us/nyc all returned empty content. `nextExport: true` confirms static export with client-side hydration. |
| **Fix** | Switch critical pages to **Server-Side Rendering (SSR)** or **Static Site Generation (SSG)** via Next.js. At minimum: homepage, pricing, all /alternatives/ pages, all /location/ pages, creator page, about-us. |
| **Priority** | **CRITICAL — Fix first** |

### 2. Sitemap Deficiencies

| Detail | |
|--------|--|
| **Issue** | Main sitemap.xml has only 9 URLs. Missing: all 80 blog posts (separate Yoast sitemap at /blog/sitemap.xml), 4+ location pages, 2+ alternative pages, creator page. |
| **Impact** | **HIGH** — Crawl discovery severely limited. |
| **Evidence** | sitemap.xml returns 9 URLs. Blog sitemap index at /blog/sitemap.xml (Yoast) has 80 posts + 16 categories + author/tag pages. Location and alternatives pages absent from all sitemaps. |
| **Fix** | (1) Add `Sitemap:` references to robots.txt. (2) Add /location/*, /alternatives/*, /creator to main sitemap. (3) Create a sitemap index referencing both main and blog sitemaps. |
| **Priority** | **HIGH** |

**Main sitemap (9 URLs):**
1. https://passionbits.io/
2. https://passionbits.io/blog/
3. https://passionbits.io/pricing
4. https://passionbits.io/case-studies
5. https://passionbits.io/about-us
6. https://passionbits.io/contact
7. https://passionbits.io/terms-condition
8. https://passionbits.io/privacy
9. https://passionbits.io/refund

**Missing from sitemap:**
- /alternatives/contentbeta
- /alternatives/testimonial-hero
- /location/us/nyc
- /location/us/la
- /location/us/francisco
- /location/india/jaipur
- /creator
- All 80 blog posts (in separate Yoast sitemap, not linked)

### 3. robots.txt Missing Sitemap References

| Detail | |
|--------|--|
| **Issue** | robots.txt only has `Disallow: /private/` and `Allow: /public/`. No sitemap reference. |
| **Impact** | **MEDIUM** |
| **Fix** | Add: `Sitemap: https://passionbits.io/sitemap.xml` and `Sitemap: https://passionbits.io/blog/sitemap.xml` |
| **Priority** | **HIGH (5-minute fix)** |

**Current robots.txt:**
```
User-agent: *
Disallow: /private/
Allow: /public/
```

**Recommended robots.txt:**
```
User-agent: *
Disallow: /private/
Disallow: /dashboard/
Allow: /public/

Sitemap: https://passionbits.io/sitemap.xml
Sitemap: https://passionbits.io/blog/sitemap.xml
```

### 4. No Hreflang Tags

| Detail | |
|--------|--|
| **Issue** | Passionbits targets India, US, and UK markets with location-specific pages but has zero hreflang implementation. |
| **Impact** | **MEDIUM** |
| **Fix** | Implement hreflang tags on location pages. If the main site doesn't have per-locale variants, lower priority. |
| **Priority** | **MEDIUM** |

### 5. No Canonical Tags on Main Site

| Detail | |
|--------|--|
| **Issue** | No canonical tags in the initial HTML of any Next.js page. |
| **Impact** | **MEDIUM** — Risk of duplicate content with trailing slash and parameter variations. |
| **Fix** | Add self-referencing canonical tags via Next.js `<Head>` component (bundle with SSR fix). |
| **Priority** | **HIGH (bundle with SSR fix)** |

### 6. Missing Open Graph Tags

| Detail | |
|--------|--|
| **Issue** | No OG tags on any main site page. Blog also missing OG tags despite Yoast. |
| **Impact** | **MEDIUM** — Shared links on LinkedIn, Twitter, Facebook look generic/broken. Critical for a social-focused video marketing brand. |
| **Fix** | Add og:title, og:description, og:image, og:url. Check Yoast Social settings for blog. |
| **Priority** | **MEDIUM** |

### 7. Blog/Main Site Integration Gap

| Detail | |
|--------|--|
| **Issue** | Blog (WordPress/Yoast) at /blog/ and main site (Next.js) have separate sitemaps, separate CMS, no shared navigation visible in initial HTML. |
| **Impact** | **MEDIUM** — Link equity may not flow between blog (80 posts) and commercial pages. |
| **Fix** | Strong internal links from blog posts to main site (pricing, alternatives, creator). Add blog to main site navigation. Verify canonical handling across both systems. |
| **Priority** | **MEDIUM** |

---

## On-Page SEO Findings

### 8. Main Site Pages — All On-Page Elements Missing

| Page | Title | Description | H1 | Schema | Canonical | OG |
|------|:-----:|:-----------:|:--:|:------:|:---------:|:--:|
| Homepage | -- | -- | -- | -- | -- | -- |
| Pricing | -- | -- | -- | -- | -- | -- |
| About Us | -- | -- | -- | -- | -- | -- |
| /alternatives/contentbeta | -- | -- | -- | -- | -- | -- |
| /alternatives/testimonial-hero | -- | -- | -- | -- | -- | -- |
| /location/us/nyc | -- | -- | -- | -- | -- | -- |
| /location/us/la | -- | -- | -- | -- | -- | -- |
| /location/us/francisco | -- | -- | -- | -- | -- | -- |
| /location/india/jaipur | -- | -- | -- | -- | -- | -- |
| /creator | -- | -- | -- | -- | -- | -- |

*All dashes = missing from server-rendered HTML. May exist in client-rendered DOM but crawlers likely don't see them.*

**Fix:** SSR/SSG for all pages resolves this entirely.

### 9. Blog SEO Elements (Yoast)

| Element | Status |
|---------|--------|
| Meta title | Present ("Passionbits blog - UGC videos Resources and Guides") |
| Meta description | Present |
| Schema markup | Present (WebPage, BreadcrumbList, WebSite, Person) |
| H1 | **Missing** on blog listing page |
| Canonical | Not detected |
| Open Graph | Not detected |

**Fix:** Add H1 to blog listing. Verify canonical output in Yoast. Enable OG in Yoast Social.

### 10. Blog URL Slugs Excessively Long

| Example Slug | Length |
|-------------|--------|
| `10-viral-instagram-trends-for-professional-brands-in-the-us-march-2026-part-2` | 78 chars |
| `current-tiktok-trends-in-the-us-for-professional-b2b-saas-brands-february-2026-part-1` | 85 chars |

**Fix:** Shorter slugs for future posts (e.g., `instagram-trends-us-pro-march-2026`). Don't redirect existing URLs.

### 11. "Uncategorized" Category in Sitemap

**Issue:** /blog/category/uncategorized/ exists in category sitemap.
**Fix:** Re-categorize posts. Noindex or remove the uncategorized page.

---

## Content Findings

### 12. Blog Content Volume (80 Posts)

| Category | Posts (approx) | Topics |
|----------|:--------------:|--------|
| Social media trends | ~40 | Monthly TikTok/Instagram trends for US and India, consumer and professional brands |
| Industry guides | ~15 | Real estate, insurance, fintech, SaaS, babycare marketing |
| Competitor comparisons | ~7 | Content Beta, Testimonial Hero, Billo, HeyGen, MakeUGC alternatives |
| Case studies | ~6 | Vibiz.ai, Parakeet AI, Bigged, Blort AI, Klap App, Flowith.io |
| UGC education | ~5 | What is UGC, creating UGC videos, mastering UGC content |
| YouTube/ads guides | ~7 | YouTube SEO, YouTube ads for SaaS, Facebook ads for insurance |

### 13. Content Gaps

| Gap | Search Volume Potential | Priority |
|-----|:----------------------:|:--------:|
| "UGC platform" / "video production platform" pillar page | High | HIGH |
| "UGC creator pricing" guide | High | HIGH |
| Video marketing ROI / benchmarks (original research) | Medium | HIGH |
| Location pages with actual local content | Medium | MEDIUM |
| Blog listing pagination (only 6 of 80 posts visible) | -- | MEDIUM |

### 14. Keyword Cannibalization Risk

**Issue:** Multiple posts target similar queries with Part 1/Part 2 splits and monthly variations:
- "Instagram trends US consumer February Part 1" vs "Part 2"
- "Instagram trends US consumer March Part 1" vs "Part 2"
- Same pattern for TikTok, India market, professional brands

**Fix:** Consolidate Part 1/Part 2 into single posts. Consider updating previous month's posts with new data rather than creating new posts each month (add "Last updated" dates).

---

## Indexed Pages Check

**Google `site:passionbits.io` results show these indexed:**
- Homepage, About Us (main site)
- creator.passionbits.io (subdomain)
- /location/us/nyc (location page)
- Multiple blog posts (trend reports, alternatives, case studies)
- /alternatives/contentbeta, /alternatives/testimonial-hero

**Notable:** Google has indexed location and alternative pages despite empty HTML, likely from link signals. But these pages have no content for Google to rank.

---

## Blog Category Analysis (16 Categories)

| Category | Likely Post Count | Issue |
|----------|:-----------------:|-------|
| content-marketing | Many | Primary category |
| instagram | Many | Well-populated |
| tiktok | Many | Well-populated |
| ugc | Several | Core topic |
| case-study | Several | Good |
| real-estate-marketing | Several | Industry vertical |
| advertising | Few | May be thin |
| car-insurance | Few | Very niche |
| life-insurance | Few | Very niche |
| fintech | Few | May be thin |
| mutual-funds | Few | Very niche |
| content-strategies | Few | Overlaps with content-marketing |
| youtube-ads-tips | Few | Nested category |
| youtube-ads-for-saas | Few | Sub-category |
| marketing | Varies | Parent category |
| **uncategorized** | **?** | **Remove** |

**Recommendations:**
- Consolidate thin categories (car-insurance + life-insurance = "insurance-marketing")
- Remove or noindex "uncategorized"
- Noindex very thin category pages or add intro content

---

## Prioritized Action Plan

### Phase 1: Critical Fixes (Blocking Indexation)

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 1 | Switch to SSR/SSG for all main site pages | High (dev) | Unlocks ALL on-page SEO |
| 2 | Add meta title + description to all pages | Bundled with #1 | High |
| 3 | Add H1 to all pages | Bundled with #1 | High |
| 4 | Add self-referencing canonical tags | Bundled with #1 | High |
| 5 | Add schema markup (Organization, Product, FAQPage) | Bundled with #1 | High |

### Phase 2: High-Impact Improvements

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 6 | Add sitemap references to robots.txt | 5 min | High |
| 7 | Add location + alternative pages to main sitemap | 30 min | High |
| 8 | Add internal links from blog posts to commercial pages | Medium | High |
| 9 | Create "UGC video platform" pillar page | Medium | High |
| 10 | Implement hreflang for location pages | Medium | Medium |
| 11 | Add Open Graph tags to all pages | Low | Medium |

### Phase 3: Quick Wins

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 12 | Enable OG + verify canonical in Yoast settings | 10 min | Medium |
| 13 | Add H1 to blog listing page | 5 min | Low |
| 14 | Remove/noindex "uncategorized" category | 5 min | Low |
| 15 | Add blog link to main site navigation | Low | Medium |

### Phase 4: Long-Term Growth

| # | Action |
|---|--------|
| 16 | Create "UGC creator pricing" guide (high search volume keyword) |
| 17 | Create original research content (video marketing benchmarks, UGC ROI data) |
| 18 | Consolidate Part 1/Part 2 trend posts into single comprehensive posts |
| 19 | Build more /alternatives/ pages (Billo, Insense, HeyGen, MakeUGC) with SSR |
| 20 | Expand location pages with unique local content per city |
| 21 | Fix blog pagination to surface all 80 posts |
| 22 | Shorten future blog URL slugs |
| 23 | Consolidate thin blog categories |
| 24 | Monitor competitor domains monthly (contentbeta.com, testimonialhero.com, billo.app, insense.pro) |

---

## Competitor Domains to Benchmark

| Competitor | Domain | Compare |
|-----------|--------|---------|
| Content Beta | contentbeta.com | DA, indexed pages, top keywords, page speed |
| Testimonial Hero | testimonialhero.com | DA, indexed pages, top keywords |
| Billo | billo.app | DA, indexed pages, top keywords |
| Insense | insense.pro | DA, indexed pages, top keywords |

---

## Key Takeaway

**The #1 priority is fixing the Next.js rendering.** Until the main site serves real HTML to crawlers, everything else (schema, meta tags, content optimization) is invisible to search engines. The WordPress blog is carrying all organic weight — connect it better to commercial pages while fixing the main site rendering.
