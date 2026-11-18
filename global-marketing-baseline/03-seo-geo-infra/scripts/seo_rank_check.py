#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STRATRONIX 全球搜索可见度体检（零模型，纯代码）
用途：诊断 Google 品牌词纠错问题 + 监控 Google/Bing/Yandex/DuckDuckGo 收录与排名
输出：memory/seo_rank_check_latest.json + 控制台摘要
"""
import json, re, ssl, sys, urllib.parse, urllib.request, datetime, time

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

# 检测词：品牌词 + 品类词 + 地域词（覆盖 SEO + GEO 两条线）
QUERIES = [
    ("brand",      "STRATRONIX"),
    ("brand_long",'"Stratronix Technology (Shenzhen)"'),
    ("product",   "STRATRONIX STA-100"),
    ("category",  "private AI agent appliance"),
    ("geo",       "Shenzhen AI hardware company STRATRONIX"),
    ("geo_id",    "perangkat AI agent"),
    ("geo_ar",    "جهاز الذكاء الاصطناعي"),
    ("geo_ru",    "Shenzhen AI agent hardware manufacturer"),
]

ENGINES = {
    "duckduckgo": "https://html.duckduckgo.com/html/?q={q}",
    "bing":       "https://www.bing.com/search?q={q}&count=20",
    "yandex":     "https://yandex.com/search/?text={q}",
    "mojeek":     "https://www.mojeek.com/search?q={q}",
    "google":     "https://www.google.com/search?q={q}&num=20",
}

OUR_DOMAINS = ("stratronix.ai", "stratronix-seo", "stratronix-paa")

def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml",
    })
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        raw = r.read()
        try:
            return r.status, raw.decode("utf-8", "ignore")
        except Exception:
            return r.status, raw.decode("latin-1", "ignore")

def strip(html):
    html = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", html)
    return re.sub(r"(?s)<[^>]+>", " ", html)

def analyze(engine, query, html):
    """返回该引擎结果页的诊断信息"""
    d = {"engine": engine, "query": query, "ok": False,
         "blocked": False, "our_rank": None, "our_hits": 0,
         "competitors": [], "suggested": [], "brand_mentions": 0}
    low = html.lower()
    if "unusual traffic" in low or "captcha" in low or "are you a robot" in low \
       or "异常流量" in html or "checking your browser" in low:
        d["blocked"] = True
        return d
    # 是否出现我们的域名
    for dom in OUR_DOMAINS:
        n = low.count(dom)
        if n:
            d["our_hits"] += n
    # 提取外链域名
    links = re.findall(r'https?://([a-z0-9\-]+(?:\.[a-z0-9\-]+)+)', html.lower())
    seen, cands = set(), []
    for h in links:
        if h in seen:
            continue
        seen.add(h)
        if h in ("google.com", "www.google.com", "bing.com", "www.bing.com",
                 "yandex.com", "yandex.ru", "duckduckgo.com", "html.duckduckgo.com",
                 "microsoft.com", "gstatic.com", "googleusercontent.com",
                 "microsofttranslator.com", "w3.org", "schema.org"):
            continue
        if any(k in h for k in OUR_DOMAINS):
            continue
        cands.append(h)
    d["competitors"] = cands[:12]
    # 建议词
    for m in re.findall(r'(?i)(?:related|searches for|suggestions)[^<]{0,20}?>([^<]{2,40})<', html)[:8]:
        d["suggested"].append(m.strip())
    d["brand_mentions"] = low.count("stratronix")
    d["ok"] = True
    return d

def main():
    results = []
    for qname, q in QUERIES:
        row = {"query_name": qname, "query": q, "engines": {}}
        for eng, tpl in ENGINES.items():
            url = tpl.format(q=urllib.parse.quote(q))
            try:
                status, html = fetch(url)
            except Exception as e:
                row["engines"][eng] = {"engine": eng, "query": q, "ok": False,
                                      "error": f"{type(e).__name__}: {e}"[:120]}
                time.sleep(1.5)
                continue
            d = analyze(eng, q, html)
            d["status"] = status
            d["bytes"] = len(html)
            row["engines"][eng] = d
            time.sleep(2.0)
        results.append(row)
        print(f"[done] {qname} :: {q}", flush=True)

    out = {
        "checked_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "results": results,
    }
    path = "/home/donald/.openclaw/workspace/memory/seo_rank_check_latest.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    print("\n===== 摘要 =====")
    for row in results:
        for eng, d in row["engines"].items():
            if d.get("blocked"):
                print(f"{eng:11s} {row['query'][:38]:40s} BLOCKED/反爬")
            elif not d.get("ok"):
                print(f"{eng:11s} {row['query'][:38]:40s} ERR {d.get('error','?')[:60]}")
            else:
                print(f"{eng:11s} {row['query'][:38]:40s} ours={d['our_hits']:2d} "
                      f"brand={d['brand_mentions']:3d} 竞争站前6: {d['competitors'][:6]}")
    print(f"\n写入: {path}")

if __name__ == "__main__":
    main()
