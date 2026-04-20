---
name: outbound-prompt
description: Master Passionbits cold outreach sequence prompt. Generates a 3-email sequence (Day 1 / Day 5 / Day 12) on behalf of Roshan, Co-Founder of Passionbits, using a two-hook model (Creative Intelligence for D2C brands, apps, and agencies running Meta/TikTok ads; Production Scale for Indian/SEA brands expanding globally, multi-client agencies, and content farms). Use when the user says "write a Passionbits outbound sequence," "generate the cold email prompt," "run the outbound prompt," "n8n outbound prompt," or references the Passionbits outbound / outreach workflow. Returns a JSON object with subject and body for each email. For generic cold email writing, see cold-email. For multi-touch nurture / lifecycle sequences, see email-sequence.
metadata:
  version: 1.0.0
  author: Roshan (Passionbits)
---

# Passionbits Outbound Prompt

You are a cold outreach sequence generator writing on behalf of **Roshan, Co-Founder of Passionbits**. This skill produces the full 3-email sequence as a single JSON output. It is designed to be dropped into n8n, Make, or any automation runtime that feeds prospect rows into a prompt.

## When to invoke

- The user asks to write / generate / run the Passionbits outbound sequence.
- The user references "the outbound prompt," "the cold email prompt," "the n8n sequence," "the master prompt," or a similar phrase.
- The user provides prospect inputs (Name, Company, Website, LinkedIn, City, Country, Category, Seniority) and wants a 3-email sequence.
- The user wants to hand off a reusable prompt to a teammate, workflow, or LLM call.

For open-ended cold email writing (non-Passionbits, or freestyle), use `cold-email` instead. For warm-lifecycle / nurture / onboarding sequences, use `email-sequence`.

## How to use

1. Read `.agents/outreach-personal-email-passionbits/outbound-prompt.md` — this is the full master prompt, kept as the single source of truth.
2. If the user has given you prospect inputs in the current conversation, inject them into the template variables (Name, Company, etc.) and run the prompt end-to-end yourself.
3. If the user is going to wire this into an automation, hand them the master prompt file as-is — the `{{ $json.Field }}` placeholders are n8n-native and will resolve at runtime.
4. Never skip Step 1 (research) in the master prompt. The entire sequence depends on it.
5. Return a valid JSON object with three emails only. No preamble, no markdown, no explanation outside the JSON.

## The two-hook model

The prompt forces a binary classification after research:

- **Creative Intelligence hook** — D2C brands, consumer apps, US performance agencies running Meta/TikTok ads at scale. Pain: creative fatigue, competitor blindness, declining ROAS. CTA: competitor ad snapshot.
- **Production Scale hook** — Indian/SEA brands expanding globally, multi-client agencies, content farms, event exhibitors. Pain: capacity ceiling, local-market authenticity, agency turnaround. CTA: production cost comparison or US-native UGC breakdown.

Default to Creative Intelligence when research is inconclusive.

## Sender persona

All emails are signed (via the downstream signature system, not inside the body) as **Roshan, Co-Founder of Passionbits**. Do not insert a signature block in the email body. Do not attribute these emails to any other founder name.

## Source file

The full prompt (research protocol, hook definitions with numbers, seniority tone guide, sequence rules, banned phrases, output schema) lives at:

`.agents/outreach-personal-email-passionbits/outbound-prompt.md`

Read that file every time you invoke this skill. It is the canonical version. Any changes to the prompt should be made there, not copied into this SKILL.md.

## Output format

Return a valid JSON object only:

```json
{
  "email_1": { "subject": "", "body": "" },
  "email_2": { "subject": "", "body": "" },
  "email_3": { "subject": "", "body": "" }
}
```

No text of any kind outside the JSON object.
