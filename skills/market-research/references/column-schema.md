# Column Schema Reference

## Company sheets (sheets 1-9, 11)

| Column | Definition | Example |
|--------|------------|---------|
| Company | Legal / trading name | Mamaearth |
| Category | 1-3 word category tag (use sub-category tag for Sheet 2) | D2C beauty; UGC production agency |
| HQ | City, Country | Mumbai, India |
| Target Market | Where they sell / expand to | US; India; US+SEA |
| Why-fit signal | 1-sentence reason this row belongs on this sheet | Hiring India Country Manager (Dec 2025) |
| Meta Ad Library URL | Direct link to their advertiser page | https://www.facebook.com/ads/library/?id=… |
| Website | Root domain | https://mamaearth.in |
| LinkedIn | Company LinkedIn URL | https://linkedin.com/company/mamaearth |
| Headcount | LinkedIn-stated range or approx | 1000-5000 |
| Ad Spend signal | Dollar/rupee estimate or qualitative signal + source | ~$2M/mo Meta — Sensor Tower Q4 2025 |
| UGC signal | Evidence of UGC-heavy creative | 40+ active creator-format video ads on Meta Ad Library |
| Source URL | One citation URL (can be same as Meta Ad Library URL) | https://… |
| Confidence | High / Medium / Low | High |
| Outreach hook | 1-sentence opener specific to this account | "Your new moisturizer line has 12 variants — here's what Sugar is testing that you're not" |
| As-of date | YYYY-MM-DD | 2026-04-16 |

## Sheet 10 (Region × Category spend heatmap)

| Column | Definition | Example |
|--------|------------|---------|
| Region | Country / city cluster | India |
| Category | D2C vertical | Beauty & personal care |
| Spend signal ($) | Annual or monthly spend estimate | $450M/year Meta |
| Top brands (3-5) | Comma-separated list | Mamaearth; Sugar; Plum |
| Meta Ad Library sample URL | One category-representative advertiser | https://… |
| Data source | Named source with date | Statista / Meta Transparency 2025 |
| Confidence | High / Medium / Low | Medium |
| Hook angle | 1-sentence Passionbits angle for the region×category | "India D2C beauty spends $X on creator content — we cut that 60% with pre-vetted creators" |
| As-of date | YYYY-MM-DD | 2026-04-16 |

## Formatting rules

- Use **pipes** `|` as column separators (GFM).
- Do NOT use pipes inside cells. If you need a pipe, use `/`.
- Avoid commas inside cells where possible; use `;` for lists.
- Dates must be ISO `YYYY-MM-DD`.
- URLs must start with `https://`.
- Confidence is case-sensitive: `High`, `Medium`, `Low`.
