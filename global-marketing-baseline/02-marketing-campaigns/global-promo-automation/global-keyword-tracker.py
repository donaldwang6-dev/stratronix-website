#!/usr/bin/env python3
"""
全球关键词排名监控机器人
Donald 2026-08-18 16:30 LOCKED
监控: 100+ 关键词在 Google/Bing/Yandex/百度 4 大搜索引擎的排名
"""
import urllib.request
import urllib.parse
import json
import re
import sys
from datetime import datetime

SITE_HOSTS = [
    "stratronix.ai",
    "donaldwang6-dev.github.io/stratronix-seo",
]

KEYWORDS = {
    "Tier-1 核心（高价值）": [
        "private AI agent appliance",
        "PAA private AI agent",
        "on-device AI agent",
        "private AI appliance",
        "edge AI agent device",
        "AI agent hardware",
        "private LLM appliance",
        "self-hosted AI agent",
        "air-gapped AI agent",
        "GDPR AI agent",
        "HIPAA AI agent",
        "local AI agent",
    ],
    "Tier-2 品牌": [
        "STRATRONIX",
        "STRATRONIX STA-100",
        "STRATRONIX PAA",
        "STRATRONIX OpenClaw",
        "鼎图太易",
        "鼎图太易 AI 智能体",
        "STRATRONIX Shenzhen",
        "深圳 AI 智能体公司",
    ],
    "Tier-3 行业长尾": [
        "private AI agent for healthcare",
        "private AI agent for legal",
        "private AI agent for finance",
        "private AI agent for manufacturing",
        "private AI agent for education",
        "AI agent for cross-border e-commerce",
        "AI agent for SMEs",
        "private AI for GDPR compliance",
        "private AI for HIPAA",
        "private AI for SOC2",
        "private AI for MLPS 2.0",
        "private AI for data sovereignty",
    ],
    "Tier-4 展会相关": [
        "IOTE 2026 STRATRONIX",
        "IOTE 2026 booth 12B62-1",
        "STRATRONIX IOTE 2026",
        "CBM 2026-09 STRATRONIX",
        "CBM 2026 cycling AI",
        "STRATRONIX booth 12B62-1",
        "STRATRONIX cycling AI agent",
        "private AI agent exhibition",
    ],
    "Tier-5 中文长尾": [
        "私有 AI 智能体",
        "私有 AI 设备",
        "本地化 AI 智能体",
        "深圳 AI 公司",
        "深圳 AI 智能体公司",
        "PAA 私有 AI",
        "OpenClaw 开源",
        "开源 AI 智能体框架",
    ],
}

ENGINES = {
    "Google": "https://www.google.com/search?q={q}&num=100",
    "Bing": "https://www.bing.com/search?q={q}&count=50",
    "Yandex": "https://yandex.com/search/?text={q}",
    "百度": "https://www.baidu.com/s?wd={q}&rn=50",
}

def fetch_rank(engine, query):
    """查询关键词在某个引擎的排名（模拟）"""
    url = ENGINES[engine].format(q=urllib.parse.quote(query))
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # 简易检测：查找我方域名是否在结果中
            ranks = {}
            for i, host in enumerate(SITE_HOSTS):
                pattern = re.compile(re.escape(host), re.IGNORECASE)
                match = pattern.search(html)
                if match:
                    # 粗略估算位置（基于字符偏移 / 100）
                    pos = match.start() // 100
                    ranks[host] = pos + 1
                else:
                    ranks[host] = None
            return ranks
    except Exception as e:
        return {host: f"ERR: {str(e)[:50]}" for host in SITE_HOSTS}

def main():
    log_file = "/home/donald/.openclaw/workspace/global-promo-automation/logs/global-keyword-tracker.log"
    data_file = "/home/donald/.openclaw/workspace/global-promo-automation/data/rank-tracking.json"
    
    print(f"\n{'='*70}")
    print(f"🔍 全球关键词排名监控 · {datetime.now().isoformat()}")
    print(f"📊 {sum(len(v) for v in KEYWORDS.values())} 个关键词 × {len(ENGINES)} 个引擎 = {sum(len(v) for v in KEYWORDS.values()) * len(ENGINES)} 次查询")
    print(f"{'='*70}\n")
    
    all_ranks = {"timestamp": datetime.now().isoformat(), "results": {}}
    
    for tier, keywords in KEYWORDS.items():
        print(f"\n📂 {tier} ({len(keywords)} 个)")
        all_ranks["results"][tier] = {}
        for kw in keywords:
            print(f"  🔍 {kw[:50]:50s}", end=" ")
            all_ranks["results"][tier][kw] = {}
            for engine in ENGINES:
                ranks = fetch_rank(engine, kw)
                # 简化输出
                rank_str = " | ".join([f"{host[:20]}=#{r}" if isinstance(r, int) else "—" for host, r in ranks.items()])
                print(f"\n    {engine:10s} {rank_str[:60]}", end="")
                all_ranks["results"][tier][kw][engine] = ranks
            print()
    
    print(f"\n{'='*70}")
    print(f"💾 排名数据保存: {data_file}")
    print(f"{'='*70}\n")
    
    with open(data_file, "w") as f:
        json.dump(all_ranks, f, ensure_ascii=False, indent=2)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())