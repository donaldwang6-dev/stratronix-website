#!/usr/bin/env python3
"""
seed-new-langs.py — 全球 SEO 新语言种子落地页生成器
铁律 12 (24/7 全球 SEO) + 铁律 3 (自主推进) — 不问 Donald, 0 元成本

7 个新语言 ISO: kk/uz/mn/tg/ne/si/hy
每个语言 5 个核心页 = 35 个新 URL
"""

import os
from pathlib import Path

ROOT = Path("/home/donald/.openclaw/workspace/stratronix-seo")
BASE_URL = "https://donaldwang6-dev.github.io/stratronix-seo"
ANALYTICS_URL = "https://previously-january-theories-vanilla.trycloudflare.com/collect"

# 7 个新语言配置
LANGS = {
    "kk": {
        "name": "Қазақша",   # 哈萨克语
        "country": "Қазақстан",  # 哈萨克斯坦
        "region": "Kazakhstan",
        "title": "Stratronix — Шэньчжэнь AI компаниясы | Private AI-Agent Appliance (PAA) өндірушісі",
        "desc": "Шэньчжэнь AI компаниясы. Private AI-Agent Appliance (PAA) — GDPR / EU AI Act деректер сұлтандығы. 8 сала: Заң, Денсаулық, Өндіріс, Қаржы, Білім, Мемлекет, SaaS, Шекарааралық e-commerce.",
        "kw": "Stratronix, STRATRONIX, Шэньчжэнь AI компаниясы, PAA, Private AI, GDPR, EU AI Act, OpenClaw, edge AI",
        "h1": "Шэньчжэнь AI компаниясы · Stratronix",
        "subtitle": "Private AI-Agent Appliance (PAA) өндірушісі · Cloud-based AI API · Деректер сұлтандығы",
        "industry_label": "8 сала",
        "cta": "Баға ұсынысын сұрау",
        "contact": "Байланыс",
    },
    "uz": {
        "name": "Oʻzbekcha",
        "country": "Oʻzbekiston",
        "region": "Uzbekistan",
        "title": "Stratronix — Shenchjen AI kompaniyasi | Private AI-Agent Appliance (PAA) ishlab chiqaruvchisi",
        "desc": "Shenchjen AI kompaniyasi. Private AI-Agent Appliance (PAA) — GDPR / EU AI Act maʼlumotlar suvereniteti. 8 soha: Huquq, Tibbiyot, Ishlab chiqarish, Moliya, Taʼlim, Davlat, SaaS, Xalqaro e-commerce.",
        "kw": "Stratronix, STRATRONIX, Shenchjen AI kompaniyasi, PAA, Private AI, GDPR, EU AI Act, OpenClaw, edge AI",
        "h1": "Shenchjen AI kompaniyasi · Stratronix",
        "subtitle": "Private AI-Agent Appliance (PAA) ishlab chiqaruvchisi · Cloud-based AI API · Maʼlumotlar suvereniteti",
        "industry_label": "8 soha",
        "cta": "Narx soʻrovi",
        "contact": "Aloqa",
    },
    "mn": {
        "name": "Монгол",
        "country": "Монгол",
        "region": "Mongolia",
        "title": "Stratronix — Шэньжэнь AI компани | Private AI-Agent Appliance (PAA) үйлдвэрлэгч",
        "desc": "Шэньжэнь AI компани. Private AI-Agent Appliance (PAA) — GDPR / EU AI Act мэдээллийн бүрэн эрх. 8 салбар: Хууль, Эрүүл мэнд, Үйлдвэрлэл, Санхүү, Боловсрол, Төрийн, SaaS, Хил дамнасан e-commerce.",
        "kw": "Stratronix, STRATRONIX, Шэньжэнь AI, PAA, Private AI, GDPR, EU AI Act, OpenClaw, edge AI",
        "h1": "Шэньжэнь AI компани · Stratronix",
        "subtitle": "Private AI-Agent Appliance (PAA) үйлдвэрлэгч · Cloud-based AI API · Мэдээллийн бүрэн эрх",
        "industry_label": "8 салбар",
        "cta": "Үнийн санал авах",
        "contact": "Холбоо барих",
    },
    "tg": {
        "name": "Тоҷикӣ",
        "country": "Тоҷикистон",
        "region": "Tajikistan",
        "title": "Stratronix — Шэньчжэнь AI ширкат | Private AI-Agent Appliance (PAA) истеҳсолкунанда",
        "desc": "Шэньчжэнь AI ширкат. Private AI-Agent Appliance (PAA) — GDPR / EU AI Act маълумот соҳибият. 8 соҳа: Ҳуқуқ, Тандурустӣ, Истеҳсолот, Молия, Таҳсилот, Давлат, SaaS, Сарҳадӣ e-commerce.",
        "kw": "Stratronix, STRATRONIX, Шэньчжэнь AI, PAA, Private AI, GDPR, EU AI Act, OpenClaw, edge AI",
        "h1": "Шэньчжэнь AI ширкат · Stratronix",
        "subtitle": "Private AI-Agent Appliance (PAA) истеҳсолкунанда · Cloud-based AI API · Маълумот соҳибият",
        "industry_label": "8 соҳа",
        "cta": "Нарх пурсед",
        "contact": "Тамос",
    },
    "ne": {
        "name": "नेपाली",
        "country": "नेपाल",
        "region": "Nepal",
        "title": "Stratronix — Shenzhen AI कम्पनी | Private AI-Agent Appliance (PAA) निर्माता",
        "desc": "Shenzhen मा आधारित AI कम्पनी. Private AI-Agent Appliance (PAA) — GDPR / EU AI Act डाटा सम्प्रभुता। 8 उद्योग: कानुनी, स्वास्थ्य, निर्माण, वित्त, शिक्षा, सरकारी, SaaS, क्रस-बोर्डर e-commerce।",
        "kw": "Stratronix, STRATRONIX, Shenzhen AI, PAA, Private AI, GDPR, EU AI Act, OpenClaw, edge AI",
        "h1": "Shenzhen AI कम्पनी · Stratronix",
        "subtitle": "Private AI-Agent Appliance (PAA) निर्माता · Cloud-based AI API · डाटा सम्प्रभुता",
        "industry_label": "८ उद्योग",
        "cta": "मूल्य बुझ्नुहोस्",
        "contact": "सम्पर्क",
    },
    "si": {
        "name": "සිංහල",
        "country": "ශ්‍රී ලංකාව",
        "region": "Sri Lanka",
        "title": "Stratronix — ෂෙන්සියන් AI සමාගම | Private AI-Agent Appliance (PAA) නිෂ්පාදක",
        "desc": "ෂෙන්සියන් පදනම් කරගත් AI සමාගම. Private AI-Agent Appliance (PAA) — GDPR / EU AI Act දත්ත ස්වෛරීභාවය. කර්මාන්ත 8ක්: නීති, සෞඛ්‍ය, නිෂ්පාදන, මූල්‍ය, අධ්‍යාපන, රජය, SaaS, සමුද්‍ර e-commerce.",
        "kw": "Stratronix, STRATRONIX, ෂෙන්සියන් AI, PAA, Private AI, GDPR, EU AI Act, OpenClaw, edge AI",
        "h1": "ෂෙන්සියන් AI සමාගම · Stratronix",
        "subtitle": "Private AI-Agent Appliance (PAA) නිෂ්පාදක · Cloud-based AI API · දත්ත ස්වෛරීභාවය",
        "industry_label": "කර්මාන්ත 8",
        "cta": "මිල ගණන් විමසන්න",
        "contact": "සම්බන්ධ වන්න",
    },
    "hy": {
        "name": "Հայերեն",
        "country": "Հայաստան",
        "region": "Armenia",
        "title": "Stratronix — Շենժեն AI ընկերություն | Private AI-Agent Appliance (PAA) արտադրող",
        "desc": "Շենժեն հիմքով AI ընկերություն: Private AI-Agent Appliance (PAA) — GDPR / EU AI Act տվյալների ինքնիշխանություն: 8 ոլորտ՝ իրավական, առողջապահություն, արտադրություն, ֆինանսներ, կրթություն, պետական, SaaS, սահմանային e-commerce:",
        "kw": "Stratronix, STRATRONIX, Շենժեն AI, PAA, Private AI, GDPR, EU AI Act, OpenClaw, edge AI",
        "h1": "Շենժեն AI ընկերություն · Stratronix",
        "subtitle": "Private AI-Agent Appliance (PAA) արտադրող · Cloud-based AI API · Տվյալների ինքնիշխանություն",
        "industry_label": "8 ոլորտ",
        "cta": "Գնանշում ստանալ",
        "contact": "Կապ",
    },
}

def page_template(lang_code, page_slug, page_title, page_h1, page_intro, body_extra=""):
    """生成一个标准 HTML 页面"""
    L = LANGS[lang_code]
    canonical = f"{BASE_URL}/{lang_code}/{page_slug}"
    title = page_title.format(L=L["name"], region=L["region"])
    
    return f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<meta name="description" content="{L['desc']}">
<meta name="keywords" content="{L['kw']}">
<meta name="robots" content="index, follow">
<meta name="author" content="Stratronix">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="zh-CN" href="{BASE_URL}/">
<link rel="alternate" hreflang="en" href="{BASE_URL}/en/">
<link rel="alternate" hreflang="x-default" href="{BASE_URL}/">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', sans-serif; line-height: 1.7; color: #1a1a1a; background: #fafafa; }}
header {{ background: linear-gradient(135deg, #E6417F 0%, #c9296c 100%); color: white; padding: 60px 20px; text-align: center; }}
header h1 {{ font-size: 2.2rem; margin-bottom: 12px; font-weight: 700; }}
header p {{ font-size: 1.1rem; opacity: 0.95; }}
.container {{ max-width: 1200px; margin: 0 auto; padding: 40px 20px; }}
section {{ margin: 40px 0; }}
h2 {{ font-size: 1.5rem; color: #E6417F; margin-bottom: 20px; border-left: 4px solid #E6417F; padding-left: 12px; }}
.cards {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }}
.card {{ background: white; padding: 24px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }}
.card h3 {{ color: #1a1a1a; margin-bottom: 8px; font-size: 1.15rem; }}
.card p {{ color: #666; font-size: 0.95rem; }}
footer {{ background: #1a1a1a; color: #999; padding: 30px 20px; text-align: center; margin-top: 60px; }}
footer a {{ color: #E6417F; }}
.cta {{ display: inline-block; background: white; color: #E6417F; padding: 14px 32px; border-radius: 8px; text-decoration: none; font-weight: 700; margin-top: 24px; font-size: 1.05rem; }}
ul {{ padding-left: 22px; }}
li {{ margin-bottom: 8px; }}
</style>
</head>
<body>
<header>
<h1>{page_h1}</h1>
<p>{L['subtitle']}</p>
<a href="mailto:sales@stratronix.ai" class="cta">{L['cta']} → sales@stratronix.ai</a>
</header>

<div class="container">
<section>
<h2>{L['region']} · STRATRONIX</h2>
<p>{page_intro}</p>
</section>

{body_extra}

<section>
<h2>{L['industry_label']} · Key Industries</h2>
<div class="cards">
<div class="card"><h3>Legal</h3><p>GDPR-compliant AI agents for law firms and legal-tech.</p></div>
<div class="card"><h3>Healthcare</h3><p>HIPAA-friendly private AI inference for clinics and hospitals.</p></div>
<div class="card"><h3>Manufacturing</h3><p>Edge AI for production lines and quality control.</p></div>
<div class="card"><h3>Finance</h3><p>On-premise AI for banks, fintech, and trading desks.</p></div>
<div class="card"><h3>Education</h3><p>Privacy-first AI tutoring and campus deployments.</p></div>
<div class="card"><h3>Government</h3><p>Data-sovereign AI for public sector and defense.</p></div>
<div class="card"><h3>SaaS</h3><p>White-label PAA for SaaS platforms needing local AI.</p></div>
<div class="card"><h3>Cross-border E-commerce</h3><p>Multilingual AI agents for global commerce.</p></div>
</div>
</section>

<section>
<h2>Specifications · STA-100</h2>
<ul>
<li>8-core ARM Cortex CPU · 16GB RAM · 128GB NVMe</li>
<li>Pre-installed OpenClaw · Offline inference · GDPR / EU AI Act ready</li>
<li>Cloud AI API compatible · Drop-in replacement for GPT-class workloads</li>
<li>Use case: {L['region']} businesses needing on-prem AI</li>
<li>Price: $399 USD (bulk discounts available)</li>
</ul>
</section>

<section>
<h2>{L['contact']}</h2>
<p>Email: <a href="mailto:sales@stratronix.ai">sales@stratronix.ai</a></p>
<p>Headquarters: Bao'an District, Shenzhen, China</p>
<p>Company: 鼎图太易信息技术（深圳）有限公司 · Stratronix Technology (Shenzhen) Company, Limited</p>
<p>Website: <a href="https://www.stratronix.ai/">www.stratronix.ai</a></p>
</section>
</div>

<footer>
<p>© 2026 STRATRONIX 鼎图太易 · {L['region']}</p>
<p><a href="{BASE_URL}/">Home</a> · <a href="{BASE_URL}/en/">English</a> · <a href="{BASE_URL}/">中文</a></p>
</footer>

<!-- STRATRONIX AI Analytics (汪总 13:09 LOCKED) -->
<script>
(function(){{
  try {{
    var SITE = '{lang_code}';
    var ENDPOINT = '{ANALYTICS_URL}';
    var payload = JSON.stringify({{
      site: SITE,
      path: window.location.pathname,
      ref: document.referrer || '',
      ts: Date.now()
    }});
    if (navigator.sendBeacon) {{
      navigator.sendBeacon(ENDPOINT, new Blob([payload], {{type:'application/json'}}));
    }} else if (window.fetch) {{
      fetch(ENDPOINT, {{method:'POST', body:payload, keepalive:true, headers:{{'Content-Type':'application/json'}}}}).catch(function(){{}});
    }}
  }} catch(e) {{}}
}})();
</script>
</body>
</html>"""


def generate_lang(lang_code):
    """为一个新语言生成 5 个核心页面"""
    L = LANGS[lang_code]
    out_dir = ROOT / lang_code
    out_dir.mkdir(exist_ok=True)
    
    pages = {
        "index.html": (
            f"{L['h1']}",
            f"As a {L['region']}-focused AI strategy partner, Stratronix provides Private AI-Agent Appliance (PAA) hardware for cloud-based AI API deployment with full GDPR / EU AI Act / data sovereignty compliance. Based in Shenzhen, China — manufacturing AI appliances since 2026.",
        ),
        "ai-agent.html": (
            f"AI-Agent Appliance · {L['name']}",
            f"What is an AI-Agent Appliance? Stratronix PAA is an 8-core ARM Cortex box with pre-installed OpenClaw for running private AI agents locally. Perfect for {L['region']} enterprises that need cloud-grade AI without cloud-grade data leaks.",
        ),
        "sta-100.html": (
            f"STA-100 PAA · {L['region']}",
            f"STRATRONIX STA-100 Private AI-Agent Appliance (PAA) — $399 USD · 8-core ARM · 16GB RAM · Pre-installed OpenClaw. Available worldwide including {L['country']}.",
        ),
        "industries.html": (
            f"{L['industry_label']} · {L['region']}",
            f"STRATRONIX PAA serves 8 verticals: Legal, Healthcare, Manufacturing, Finance, Education, Government, SaaS, Cross-border E-commerce. Each vertical has dedicated PAA configuration for {L['region']}.",
        ),
        "about.html": (
            f"About · {L['country']}",
            f"STRATRONIX (鼎图太易) is a Shenzhen-based AI company founded in 2026. Headquartered in Bao'an District. Manufacturing Private AI-Agent Appliance (PAA) for {L['region']} and global markets.",
        ),
    }
    
    for slug, (h1, intro) in pages.items():
        page_path = out_dir / slug
        # 生成对应语言的页面标题
        if slug == "index.html":
            page_title = L['title']
        elif slug == "ai-agent.html":
            page_title = f"AI-Agent Appliance (PAA) · {{L}} | Stratronix · {L['region']}"
        elif slug == "sta-100.html":
            page_title = f"STRATRONIX STA-100 PAA · $399 USD · {{L}} | {L['region']}"
        elif slug == "industries.html":
            page_title = f"{L['industry_label']} · {{L}} | Stratronix PAA"
        elif slug == "about.html":
            page_title = f"About · {{L}} | Stratronix · {L['country']}"
        else:
            page_title = L['title']
        
        # 替换 {L} placeholder
        page_title = page_title.replace("{L}", L["name"])
        
        html = page_template(lang_code, slug, page_title, h1, intro)
        page_path.write_text(html, encoding="utf-8")
        print(f"  ✅ {lang_code}/{slug}")


def main():
    print(f"🌍 全球 SEO 新语言种子落地页生成器")
    print(f"=" * 60)
    print(f"目标: 7 个新语言 × 5 个核心页 = 35 个新 URL")
    print(f"基础 URL: {BASE_URL}")
    print(f"=" * 60)
    
    for lang_code in LANGS.keys():
        print(f"\n📝 {lang_code} ({LANGS[lang_code]['region']}):")
        generate_lang(lang_code)
    
    print(f"\n✅ 完成: {len(LANGS)} 语言, {len(LANGS) * 5} URL")
    print(f"\n下一步:")
    print(f"  1. git add + commit + push")
    print(f"  2. IndexNow API 推送")
    print(f"  3. 加 sitemap-{lang}.xml")


if __name__ == "__main__":
    main()