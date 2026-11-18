# Reddit r/SelfHosted — Hardware Comparison

## Title
$369 ARM appliance vs Jetson Orin Nano vs RTX 4090 workstation for private LLM — actual TCO comparison

## Body

I see a lot of "just buy a 4090" advice on this sub. So I did the math.

**Setup A: $369 ARM appliance**
- STRATRONIX STA-100 (8-core ARM, 4GB RAM, 32GB eMMC)
- Pre-installed OpenClaw OS + Mistral 7B quantized
- Inference: 15-20 tokens/sec
- Power: ~15W
- Use case: Chat, doc drafting, workflow automation
- Time to first query: 30 min

**Setup B: $599 Jetson Orin Nano**
- 8-core ARM + 8GB RAM + 32GB eMMC + 1024-core Ampere GPU
- Manual setup required
- Inference: 30-50 tokens/sec (LLM)
- Power: ~25W
- Time to first query: 4-8 hours

**Setup C: $2,500 RTX 4090 workstation**
- i7 + 64GB RAM + 4090 GPU
- Run anything
- Inference: 100+ tokens/sec (70B models)
- Power: ~450W
- Time to first query: 1 day
- Noise: jet engine

**Where I land after 50 deployments:**

For "I need a chat assistant for my team" — Setup A wins on TCO and ease.

For "I want to fine-tune models or run 70B locally" — Setup C wins, no contest.

Setup B is awkward middle ground: too much setup for non-tech users, not enough power for serious ML.

The thing nobody talks about: **Setup A vs Setup C is 5x upfront cost difference + 30x power difference**. For a law firm doing 100 queries/day, Setup A pays for itself in <6 months on power alone.

Anyone else running TCO comparisons like this? Curious where the breakeven is for medium-sized deployments.

---

**Engagement prompt**: "What's your breakeven point for switching from cloud API to local?"
