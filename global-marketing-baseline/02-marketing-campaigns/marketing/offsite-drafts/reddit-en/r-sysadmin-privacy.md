# Reddit r/sysadmin — Privacy Discussion

## Title
LLM privacy math: how do you decide which queries can go to cloud APIs?

## Body

I'm the IT lead at a small company. We're evaluating LLM use and I'm stuck on the privacy question.

Our current rule: anything with customer PII or financial data stays local. Everything else can go to ChatGPT API.

But the rules feel arbitrary. What if a customer name leaks in an "innocent" prompt?

Curious how others are handling this:
1. **Hard line**: never send PII to cloud
2. **Anonymize first**: scrub names/numbers, then send
3. **Self-hosted only**: only on-prem models
4. **Trust the provider**: zero-retention API tier + audits

We've been doing #2 (anonymize) for a year. But our small appliance (local model) handles about 30% of queries fully offline, which makes the rules clearer.

What's working for you?

---

**Engagement prompt**: "How do you explain your policy to non-technical staff?"
