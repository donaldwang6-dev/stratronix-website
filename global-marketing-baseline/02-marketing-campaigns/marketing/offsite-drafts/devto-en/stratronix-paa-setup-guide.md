# STRATRONIX PAA Setup Guide: From Box to First Query in 30 Minutes | STRATRONIX

> Step-by-step STRATRONIX STA-100 PAA setup guide: unbox, plug in, install OpenClaw OS, run your first private AI query. STRATRONIX 30-min setup.

# STRATRONIX PAA Setup Guide: From Box to First Query in 30 Minutes

By [STRATRONIX](https://www.stratronix.ai) | July 14, 2026 | 10 min read

## What You're Getting

Inside the **STRATRONIX STA-100 PAA** box:

- 1 × STA-100 appliance (300×300×45mm, 4.5kg)

- 1 × Power cable (C13, US/EU/UK/CN variants)

- 1 × Ethernet cable (Cat 6, 2m)

- 1 × Quick Start card (with QR to this guide)

Total cost: **$369**. No subscription. No monthly bill.

## Before You Start

You'll need:

- A network port near your workspace (or WiFi)

- A computer / tablet to access the admin panel

- 30 minutes of time

That's it. No IT team needed.

## Step-by-Step Setup

### Step 1: Plug In (2 minutes)

- Place the PAA in your server room / closet / even your desk drawer

- Connect the power cable

- Connect the Ethernet cable to your router / switch

- Press the power button (front panel)

The LED will turn green within 30 seconds. The device is booting.

### Step 2: Find Your PAA on Network (3 minutes)

The PAA advertises itself via mDNS as `stratronix-paa.local`.

From any computer on the same network:

$ ping stratronix-paa.local
PING stratronix-paa.local (192.168.1.42): 56 data bytes
64 bytes from 192.168.1.42: icmp_seq=0 ttl=64 time=0.345 ms

Or scan your network. Default IP is DHCP-assigned.

### Step 3: Open Admin Panel (5 minutes)

Open `https://stratronix-paa.local:8443` in your browser.

First-boot wizard appears:

- Accept license (BSD-3-Clause for OS, commercial for hardware)

- Set admin password

- Choose timezone

- Configure network (DHCP or static)

- (Optional) Set up user accounts (LDAP/AD integration supported)

Save and continue.

### Step 4: Install OpenClaw OS (10 minutes)

OpenClaw OS is the "operating system" for AI agents. Click "Install OpenClaw OS":

- Latest stable: v2026.07.14 (auto-selected)

- Install size: ~50GB (LLM model + system)

- Time: 5-10 minutes (depends on network for initial model download)

The installer will:

- Download Llama 3.3 70B (Q4_K_M) model (~40GB) — or bring-your-own model

- Set up RAG vector database

- Install 10 pre-built AI agents

- Configure audit log

Progress shown live. When done, you see ✓ on all components.

### Step 5: Activate Your First Agent (5 minutes)

From the admin panel, "Agents" tab:

- Click "Activate" on "Personal Assistant"

- Set your name + email

- Pick your 3 favorite tools (calendar, email, notes)

- Save

You can activate any/all of the 10 pre-built agents. Each takes ~5 minutes.

### Step 6: First Query (2 minutes)

Open the user portal at `https://stratronix-paa.local:8443/user`.

Type in the chat:

You: Draft an email to my team about the Q3 results

AI (in 1.2s): Subject line options:
1. Q3 Results Recap
2. Strong Q3, Looking Ahead
3. ...

Body draft:
Hi team,
...

You have your first private AI result. **Zero bytes left your network**.

### Step 7: Add More Users / Agents (5 minutes each)

- Add team members: "Users" → "Invite"

- Activate more agents: "Agents" → "Activate"

- Connect knowledge base: "Knowledge" → "Upload Folder"

## Advanced Setup (Optional)

### Connect to Your Company Identity

- LDAP / Active Directory (sync users)

- OAuth / SAML SSO

- API tokens for scripts

### Customize Models

- Swap Llama 3.3 for Qwen 2.5, Mixtral, DeepSeek, or your fine-tuned model

- Set per-agent model (small model for sales, big model for legal)

- Load balancing across multiple PAAs

### Integrations

- Slack / Teams bot

- Email auto-reply

- CRM (Salesforce / HubSpot / Feishu)

- Document management (Notion / Confluence / SharePoint)

- Custom HTTP / gRPC API

## Troubleshooting

IssueFix
Can't find PAA on networkCheck Ethernet, try direct PC→PAA cable
Admin panel won't loadWait 2 min for first boot, then check `https://<ip>:8443`
Slow responsesClose other apps; reduce concurrent agents
Agent doesn't know my docUpload to "Knowledge" → re-index

## What's Next

- Invite your team

- Activate more agents

- Browse the agent marketplace (we add new ones monthly)

- Join the STRATRONIX community (Discord / Forum)

## Get Your PAA

- 1 × STA-100: **$369 USD**

- Bulk discounts: 10+ units $332 / 50+ $295 / 100+ $258

- 2-year hardware warranty

- Lifetime OS updates

Order at [stratronix.ai](https://www.stratronix.ai) or email sales@stratronix.ai.

[Home](/) | [All blogs](/blog) | [Watch video setup](https://www.youtube.com/@stratronix/featured)
