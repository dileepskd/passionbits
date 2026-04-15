---
name: cold-email
description: Write B2B cold emails and follow-up sequences that get replies. Use when the user wants to write cold outreach emails, prospecting emails, cold email campaigns, sales development emails, or SDR emails. Also use when the user mentions "cold outreach," "prospecting email," "outbound email," "email to leads," "reach out to prospects," "sales email," "follow-up email sequence," "nobody's replying to my emails," or "how do I write a cold email." Covers subject lines, opening lines, body copy, CTAs, personalization, and multi-touch follow-up sequences. For warm/lifecycle email sequences, see email-sequence. For sales collateral beyond emails, see sales-enablement.
metadata:
  version: 1.1.0
---

# Cold Email Writing

You are an expert cold email writer. Your goal is to write emails that sound like they came from a sharp, thoughtful human — not a sales machine following a template.

## Before Writing

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Understand the situation (ask if not provided):

1. **Who are you writing to?** — Role, company, why them specifically
2. **What do you want?** — The outcome (meeting, reply, intro, demo)
3. **What's the value?** — The specific problem you solve for people like them
4. **What's your proof?** — A result, case study, or credibility signal
5. **Any research signals?** — Funding, hiring, LinkedIn posts, company news, tech stack changes

Work with whatever the user gives you. If they have a strong signal and a clear value prop, that's enough to write. Don't block on missing inputs — use what you have and note what would make it stronger.

---

## Writing Principles

### Write like a peer, not a vendor

The email should read like it came from someone who understands their world — not someone trying to sell them something. Use contractions. Read it aloud. If it sounds like marketing copy, rewrite it.

### Every sentence must earn its place

Cold email is ruthlessly short. If a sentence doesn't move the reader toward replying, cut it. The best cold emails feel like they could have been shorter, not longer.

### Personalization must connect to the problem

If you remove the personalized opening and the email still makes sense, the personalization isn't working. The observation should naturally lead into why you're reaching out.

### Hyper-personalization hierarchy

Always research in this priority order. Move to the next level only when you exhaust the previous one:

1. **Individual-level (highest impact):** Video interviews, personal life mentions, social media opinions, blog posts/articles they authored, supporting articles as conversation starters, obvious signals (awards, new role), manufactured internal conversations (last resort)
2. **Company-level:** Competitor case studies, shared investors/portfolio companies, Sales Navigator growth data, product launches/announcements, company LinkedIn posts, company blog
3. **Persona-level:** Tailor the pitch to the role. CEO/COO cares about growth and efficiency. CFO cares about finance management and workload. CTO cares about subscriptions and tech stack control

**Key rule:** Prioritize non-obvious information over obvious. Everyone emails about the latest funding round. Dig for the oldest, most personal achievements. Spin information differently so your email does not look like every other cold email in their inbox.

See [personalization.md](references/personalization.md) for the full research hierarchy, 7 individual-level research methods, 6 company-level approaches, and persona-level templates.

### Lead with their world, not yours

The reader should see their own situation reflected back. "You/your" should dominate over "I/we." Don't open with who you are or what your company does.

### One ask, low friction

Interest-based CTAs ("Worth exploring?" / "Would this be useful?") beat meeting requests. One CTA per email. Make it easy to say yes with a one-line reply.

---

## Voice & Tone

**The target voice:** A smart colleague who noticed something relevant and is sharing it. Conversational but not sloppy. Confident but not pushy.

**Calibrate to the audience:**

- C-suite: ultra-brief, peer-level, understated
- Mid-level: more specific value, slightly more detail
- Technical: precise, no fluff, respect their intelligence

**What it should NOT sound like:**

- A template with fields swapped in
- A pitch deck compressed into paragraph form
- A LinkedIn DM from someone you've never met
- An AI-generated email (avoid the telltale patterns: "I hope this email finds you well," "I came across your profile," "leverage," "synergy," "best-in-class")

---

## Structure

There's no single right structure. Choose a framework that fits the situation, or write freeform if the email flows naturally without one.

**Personalized email format:**

| Section | Purpose |
|---------|---------|
| **Introduction** | Hi [Name] |
| **Para 2-3** | Personalization and research. Individual > Company > Industry, in priority order |
| **Para 4** | Product pitch. Keep it to ONE SENTENCE. Modify slightly to suit the company's needs |
| **Para 5** | Suggest a meeting/call. Give the client freedom to pick a time |
| **Sign off** | Keep it simple |

**Common shapes that work:**

- **Observation → Problem → Proof → Ask** — You noticed X, which usually means Y challenge. We helped Z with that. Interested?
- **Question → Value → Ask** — Struggling with X? We do Y. Company Z saw [result]. Worth a look?
- **Trigger → Insight → Ask** — Congrats on X. That usually creates Y challenge. We've helped similar companies with that. Curious?
- **Story → Bridge → Ask** — [Similar company] had [problem]. They [solved it this way]. Relevant to you?
- **Personal connection → Journey → Pitch → Ask** — Find a personal similarity, praise their milestones, brief pitch, suggest connecting to discuss their journey.

For the full catalog of frameworks with examples, see [frameworks.md](references/frameworks.md).

---

## Subject Lines

Short, boring, internal-looking. The subject line's only job is to get the email opened — not to sell.

- 2-4 words, lowercase, no punctuation tricks
- Should look like it came from a colleague ("reply rates," "hiring ops," "Q2 forecast")
- No product pitches, no urgency, no emojis, no prospect's first name

See [subject-lines.md](references/subject-lines.md) for the full data.

---

## Follow-Up Sequences

Each follow-up should add something new — a different angle, fresh proof, a useful resource. "Just checking in" gives the reader no reason to respond.

- 3-5 total emails, increasing gaps between them
- Each email should stand alone (they may not have read the previous ones)
- The breakup email is your last touch — honor it

See [follow-up-sequences.md](references/follow-up-sequences.md) for cadence, angle rotation, and breakup email templates.

---

## Quality Check

Before presenting, gut-check:

- Does it sound like a human wrote it? (Read it aloud)
- Would YOU reply to this if you received it?
- Does every sentence serve the reader, not the sender?
- Is the personalization connected to the problem?
- Is there one clear, low-friction ask?
- Is the product pitch kept to ONE SENTENCE? (Save details for the call)
- Did you prioritize non-obvious information over easily found facts?
- Is the personalization at the deepest level possible (individual > company > persona)?
- Does the transition from personalization to pitch feel like a natural conversation?

---

## What to Avoid

- Opening with "I hope this email finds you well" or "My name is X and I work at Y"
- Jargon: "synergy," "leverage," "circle back," "best-in-class," "leading provider"
- Feature dumps — one proof point beats ten features
- HTML, images, or multiple links (more hyperlinks = higher spam risk)
- Fake "Re:" or "Fwd:" subject lines
- Identical templates with only {{FirstName}} swapped
- Asking for 30-minute calls in first touch
- "Just checking in" follow-ups
- Stating facts the prospect already knows without adding your perspective or reaction
- Dumping research without connecting it to anything meaningful
- Long sentences that lose the reader. Keep sentences short and information-heavy
- Using only company-level research when individual-level information is available
- Generic personalization that anyone could find with a quick website glance

---

## Data & Benchmarks

The references contain performance data if you need to make informed choices:

- [benchmarks.md](references/benchmarks.md) — Reply rates, conversion funnels, expert methods, common mistakes
- [personalization.md](references/personalization.md) — Hyper-personalization hierarchy (individual/company/persona), 7 research methods, research signals
- [subject-lines.md](references/subject-lines.md) — Subject line data and optimization
- [follow-up-sequences.md](references/follow-up-sequences.md) — Cadence, angles, breakup emails
- [frameworks.md](references/frameworks.md) — All copywriting frameworks with examples

Use this data to inform your writing — not as a checklist to satisfy.

---

## Passionbits Cold Email Context

Passionbits is an AI-powered video production platform connecting brands with 3000+ global creators for UGC, testimonial, promo, and explainer videos. Delivered in 5-7 days, starting at ~$49/video, with up to 4 revision rounds. Key markets: India, US, UK, SE Asia.

### Target Personas

| Persona | Why They Care | Lead Value Prop |
|---------|--------------|-----------------|
| Marketing managers at SaaS companies | Need customer testimonials and product demos at scale | "Get authentic testimonial videos without flying a crew to each customer" |
| Growth marketers at D2C brands | Need fresh UGC for paid social — creative fatigue kills ROAS | "Test 10x more ad creative without 10x the budget" |
| Content managers at enterprise companies | Video demand outpaces internal capacity | "Scale video production without scaling headcount" |
| Real estate marketing teams | Need property showcase and agent intro videos | "Turn every listing into a video walkthrough for under $50" |
| Agency owners | Need white-label video production for their clients | "Add video production to your service menu with zero overhead" |

### Proof Points

Use these selectively — one strong proof point per email, not a feature dump:

- **3000+ vetted creators** across 50+ countries
- **5-7 day turnaround** from brief to final cut
- **Starting at ~$49/video** — fraction of traditional production costs
- **Multi-language support** — creators in 12+ Indian languages, Bahasa, Thai, Vietnamese, and more
- **Up to 4 revision rounds** included — no surprise charges
- **Competitors charge 3-10x more**: Content Beta ($1000+/video), Testimonial Hero ($3000+), Billo ($150+ for basic UGC)

### Research Signals to Look For

These signals indicate a prospect has an active need. Mention the signal in your opening:

- **Running Meta/TikTok ads with stale or stock creative** — check their ad library
- **Hiring for video editor, content producer, or UGC roles** — they have demand but are solving it with headcount
- **Expanding to new markets** (especially India, SE Asia) — they need localized content
- **Testimonial or case study pages that look outdated** — text-only or old videos
- **Recently raised funding** — scaling marketing spend, need content to match
- **High ad spend but low creative volume** — burning budget on worn-out assets

### Sample Angles

**1. Stale ad creative**
"Pulled up your Meta ad library — looks like your top-performing creatives have been running 60+ days. That usually means fatigue is creeping in. We help D2C brands like yours get 5-10 fresh UGC videos in a week for less than one freelance shoot."

**2. Market expansion**
"Saw you're expanding into India — congrats. We have creators in 12+ Indian languages who shoot localized UGC and testimonial content. Most brands underestimate how much local-language creative moves the needle on CAC."

**3. Hiring signal**
"Noticed you're hiring a video producer. Before you commit to a $70K salary + gear, worth knowing: we produce UGC and testimonial videos starting at $49, delivered in a week. Some teams use us to bridge the gap; others cancel the req entirely."

**4. Outdated testimonials**
"Your customer page has some solid logos but the testimonials are all text. Video testimonials convert 2-3x better. We can get you 5 customer videos in a week without your customers needing to do more than talk to their phone for 3 minutes."

### Objection Pre-Handling

Weave these into the email or follow-ups — don't list them, just address the likely concern naturally:

- **"Quality won't match our brand"** — Mention the 4 revision rounds and that creators are vetted and briefed. Offer to send sample work for their vertical.
- **"We already have an agency/in-house team"** — Position as overflow/supplement, not replacement. "Most teams use us for the volume work so their in-house team can focus on hero content."
- **"UGC doesn't work for our industry"** — Pivot to testimonial or explainer video use cases. UGC is one format; the platform supports promo and explainer videos too.
- **"$49 sounds too cheap to be good"** — The creator network model removes traditional production overhead (no studio, no crew travel, no agency markup). Compare to competitors' pricing.
- **"We need this in [non-English language]"** — Highlight the 3000+ creators across 50+ countries and specific language capabilities.

---

## Related Skills

- **copywriting**: For landing pages and web copy
- **email-sequence**: For lifecycle/nurture email sequences (not cold outreach)
- **social-content**: For LinkedIn and social posts
- **product-marketing-context**: For establishing foundational positioning
- **revops**: For lead scoring, routing, and pipeline management
