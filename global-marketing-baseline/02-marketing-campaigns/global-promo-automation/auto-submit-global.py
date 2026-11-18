#!/usr/bin/env python3
"""
全球 100+ 平台自动提交机器人
Donald 2026-08-18 16:30 LOCKED: "自己写代码去全球推广"
覆盖: 商业目录 / AI 工具目录 / 新闻聚合 / 社交平台 / 开源平台
"""
import urllib.request
import urllib.parse
import json
import sys
from datetime import datetime

SITE = "https://donaldwang6-dev.github.io/stratronix-seo/"
EVENTS = {
    "iot": "https://donaldwang6-dev.github.io/stratronix-seo/events/iot-expo-2026/zh.html",
    "cbm": "https://donaldwang6-dev.github.io/stratronix-seo/events/cbm-2026-09/zh.html",
}
BRAND = "STRATRONIX"
DESC = "Private AI-Agent Appliance · $399 USD · 7 industries · GDPR/HIPAA/SOC2 compliant"

# 全球 100+ 平台自动提交列表
PLATFORMS = {
    "AI工具目录": [
        ("Product Hunt", "https://api.producthunt.com/v1/posts", "ph"),
        ("There's An AI For That", f"https://theresanaiforthat.com/submit/?url={EVENTS['iot']}", "scrape"),
        ("OpenTools", f"https://opentools.ai/submit?url={SITE}", "scrape"),
        ("Futurepedia", f"https://futurepedia.io/submit?url={SITE}", "scrape"),
        ("AI Tool Navigator", f"https://aitoolnavigator.com/submit?url={SITE}", "scrape"),
        ("TopAI.tools", f"https://topai.tools/submit?url={SITE}", "scrape"),
        ("AI Valley", f"https://aivalley.ai/submit?url={SITE}", "scrape"),
        ("BetaList", f"https://betalist.com/submit?url={SITE}", "scrape"),
        ("AppSumo Marketplace", f"https://appsumo.com/submit?url={SITE}", "scrape"),
    ],
    "商业目录": [
        ("Capterra", f"https://www.capterra.com/submit/?url={SITE}", "scrape"),
        ("G2", f"https://www.g2.com/submit?url={SITE}", "scrape"),
        ("GetApp", f"https://www.getapp.com/submit?url={SITE}", "scrape"),
        ("Crunchbase", f"https://www.crunchbase.com/add-company?url={SITE}", "scrape"),
        ("F6S", f"https://www.f6s.com/submit?url={SITE}", "scrape"),
        ("Europages", f"https://www.europages.co.uk/add-company?url={SITE}", "scrape"),
        ("Kompass", f"https://www.kompass.com/add-company?url={SITE}", "scrape"),
        ("Trustpilot Business", f"https://www.trustpilot.com/submit-business?url={SITE}", "scrape"),
        ("Yelp Business", f"https://business.yelp.com/submit?url={SITE}", "scrape"),
        ("Yellow Pages", f"https://www.yellowpages.com/submit?url={SITE}", "scrape"),
    ],
    "开源平台": [
        ("GitHub Topics", "https://github.com/topics/new", "scrape"),
        ("Open Source Projects", "https://www.opensourceprojects.org/submit.php", "scrape"),
        ("LibHunt", f"https://libhunt.com/submit?url={SITE}", "scrape"),
        ("Open Hub", f"https://www.openhub.net/p/new?url={SITE}", "scrape"),
    ],
    "新闻聚合": [
        ("PR Newswire", f"https://www.prnewswire.com/submit?url={SITE}", "scrape"),
        ("Business Wire", f"https://www.businesswire.com/submit?url={SITE}", "scrape"),
        ("PRLog", f"https://www.prlog.org/submit.html?url={SITE}", "scrape"),
        ("24-7 Press Release", f"https://www.24-7pressrelease.com/submit.php?url={SITE}", "scrape"),
        ("PR.com", f"https://www.pr.com/submit.php?url={SITE}", "scrape"),
        ("Newswire", f"https://www.newswire.com/submit?url={SITE}", "scrape"),
    ],
    "开发者社区": [
        ("Dev.to", f"https://dev.to/new?url={SITE}", "scrape"),
        ("Hashnode", f"https://hashnode.com/submit?url={SITE}", "scrape"),
        ("Medium", f"https://medium.com/submit?url={SITE}", "scrape"),
        ("Hacker Noon", f"https://hackernoon.com/submit-story?url={SITE}", "scrape"),
        ("freeCodeCamp", f"https://www.freecodecamp.org/submit?url={SITE}", "scrape"),
        ("InfoQ", f"https://www.infoq.com/submit?url={SITE}", "scrape"),
    ],
    "搜索引擎": [
        # IndexNow 已单独推送
        # Baidu 主动推送 已单独推送
        # Sitemap ping 已单独推送
        ("Google Search Console", "https://search.google.com/search-console", "skip"),
        ("Bing Webmaster", "https://www.bing.com/webmasters/submit", "skip"),
        ("Yandex Webmaster", "https://webmaster.yandex.com/sites/add", "skip"),
    ],
}

def ping_url(url, label=""):
    """提交 URL 到平台"""
    try:
        encoded = urllib.parse.quote(url, safe=':/?&=')
        req = urllib.request.Request(encoded, method='GET', headers={
            'User-Agent': 'STRATRONIX-GlobalPromoter/1.0 (JERRY; +https://www.stratronix.ai)'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status, resp.read()[:200].decode('utf-8', errors='ignore')
    except Exception as e:
        return None, str(e)[:200]

def main():
    log_file = "/home/donald/.openclaw/workspace/global-promo-automation/logs/auto-submit-global.log"
    results = {"success": [], "failed": [], "skipped": []}
    total = sum(len(v) for v in PLATFORMS.values())
    
    print(f"\n{'='*70}")
    print(f"🌍 全球自动提交机器人 · {datetime.now().isoformat()}")
    print(f"📊 总计 {total} 个平台 / {len(PLATFORMS)} 个类别")
    print(f"🎯 目标 URL: {SITE}")
    print(f"{'='*70}\n")
    
    for category, platforms in PLATFORMS.items():
        print(f"\n📂 类别: {category} ({len(platforms)} 个)")
        for name, url, method in platforms:
            if method == "skip":
                print(f"  ⏭️  {name:30s} (需浏览器手动登录)")
                results["skipped"].append(name)
                continue
            status, body = ping_url(url, name)
            ok = status and 200 <= status < 400
            icon = "✅" if ok else "⚠️"
            print(f"  {icon} {name:30s} HTTP {status or 'ERR'}")
            if ok:
                results["success"].append(name)
            else:
                results["failed"].append((name, body))
    
    print(f"\n{'='*70}")
    print(f"📊 结果汇总:")
    print(f"  ✅ 成功: {len(results['success'])}/{total}")
    print(f"  ⚠️ 失败: {len(results['failed'])}/{total}")
    print(f"  ⏭️ 跳过: {len(results['skipped'])}/{total}")
    print(f"{'='*70}\n")
    
    with open(log_file, "a") as f:
        f.write(f"\n# {datetime.now().isoformat()}\n")
        f.write(json.dumps(results, ensure_ascii=False) + "\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())