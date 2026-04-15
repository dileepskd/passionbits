# Query Templates by Segment

Use WebSearch with these queries. Follow up promising hits with WebFetch. Always cross-check with Meta Ad Library when the segment is UGC / ad-spend related.

## Sheet 1 — India agencies serving US clients

- `site:clutch.co india UGC agency "United States"`
- `site:sortlist.com india performance marketing agency US clients`
- `india UGC agency "US clients" case study`
- `india influencer marketing agency serves US brands`
- `"performance marketing agency" india "based in" bangalore OR mumbai OR gurgaon US clients`
- `site:linkedin.com/company india UGC agency new york OR san francisco`
- DesignRush, GoodFirms India agency directories

## Sheet 2 — US UGC agencies (3 sub-categories)

**UGC production:**
- `site:clutch.co US UGC production agency`
- `top UGC agencies US 2025`
- `"UGC production" agency new york OR los angeles OR austin`

**UGC influencer:**
- `top influencer marketing agencies US 2025 UGC`
- `site:sortlist.com US influencer agency meta ads`

**Performance-creative testing:**
- `top performance creative agencies US meta ads`
- `"creative testing" agency US "meta ads"`
- `disrupt advertising OR thumbstop OR motion agency US UGC`

Cross-reference: Meta Ad Library "Ad Library Report" for top spenders.

## Sheet 3 — US brands expanding to India

- `"US brand" "expand" OR "expansion" india 2025`
- `"India Country Manager" hiring US brand site:linkedin.com/jobs`
- `"India launch" US D2C brand press release 2025`
- `US beauty brand india launch 2025`
- `US supplement brand india expansion site:yourstory.com`
- Crunchbase filter: US brands with India operations

## Sheet 4 — India brands expanding to US (seed from existing list)

Start from `.agents/prospect-lists/india-top-100-growing-d2c.md`. For each, verify US expansion:
- Root domain check — does the site have a `/us` or `.com` variant?
- Meta Ad Library — US advertiser page?
- LinkedIn jobs — "US roles" posted?
- Amazon.com seller presence

## Sheet 5 — Consumer / prosumer apps on UGC

- `top consumer apps instagram UGC ads 2025`
- `"prosumer SaaS" UGC meta ads top spenders`
- `canva OR clickup OR notion OR grammarly OR duolingo UGC creator ads`
- Sensor Tower / data.ai top grossing app lists + Meta Ad Library cross-check
- Instagram ad creative aggregators (Foreplay, Atria, Motion) — filter by SaaS/app

## Sheet 6 — Content farms

- `top instagram content farm networks 2025`
- `Doing Things Media portfolio`
- `Underscore Talent content network accounts`
- `"content farm" instagram brand playbook 2025`
- `top reels accounts network ownership`
- Search for network-operator terms: "Betches Media", "Morning Brew Media", "Overtime", "Barstool", "Arkadium"

## Sheet 7 — Singapore companies expanding to US

- `singapore startup US expansion 2025 "series A" OR "series B"`
- `singapore SaaS US launch site:techinasia.com`
- `singapore D2C brand US amazon launch`
- `"based in singapore" "headquartered in US" 2025`
- Tech in Asia, e27, DealStreetAsia expansion coverage

## Sheet 8 — Indonesia companies expanding to US

- `indonesia startup US expansion 2025`
- `indonesia beauty brand US launch`
- `indonesia D2C US amazon site:dailysocial.id`
- East Ventures / Alpha JWC / AC Ventures portfolio expanding to US

## Sheet 9 — US companies expanding to Indonesia

- `US beauty brand indonesia launch 2025`
- `US D2C brand indonesia distributor`
- `"enters indonesia" US brand 2025`
- Indonesia beauty/F&B is a big category — search:
  - `US supplements indonesia launch`
  - `US skincare brand indonesia 2025`

## Sheet 10 — Region × Category spend heatmap

- `meta ad spend india D2C 2025 statista`
- `indonesia beauty digital ad spend 2025`
- `US supplements meta ad spend report 2025`
- `emarketer social ad spend by region 2025`
- Meta Q1 2026 transparency report
- Magna Global, GroupM forecasts by region

## Sheet 11 — US brands heavy on UGC + Meta ads (seed)

Start from `.agents/prospect-lists/global-top-100-meta-ugc-spenders.md`. For each:
- Pull Meta Ad Library URL
- Verify still actively advertising
- Update spend signal if Sensor Tower / Similarweb has fresh data

## Universal cross-checks

- **Meta Ad Library:** `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q={company}`
- **LinkedIn company:** `site:linkedin.com/company/{slug}`
- **Crunchbase:** `site:crunchbase.com {company}`
- **News:** `{company} expansion OR launch 2025`
