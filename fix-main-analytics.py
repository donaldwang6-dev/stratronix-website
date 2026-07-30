#!/usr/bin/env python3
"""
fix-main-analytics.py — 主站 analytics 注入 + 死链修复
Donald 2026-07-30 18:16 LOCKED: 「可以；破例」

修复:
  1. 替换 25 个主站 HTML 中死链的 trycloudflare URL
  2. analytics.js 改成引用附属站 (donaldwang6-dev.github.io/stratronix-seo/analytics.js)
     - 跨域脚本, 不需主站部署, 避免触发 Vercel 大改动
  3. collect endpoint 改成新 tunnel
  4. site ID 从 "stratronix-seo" 改为 "www.stratronix.ai" (主站 ID)
  5. 给 5 个核心页 (zh/index, en/index, index, about, products, contact) 加 analytics.js
     (zh/index.html 之前没有, en/index.html 已有)

最小破例范围: 只改 analytics 注入, 不动任何 H1/H2/meta/content
"""

import os
import sys
import re
from pathlib import Path

MAIN_REPO = Path("/home/donald/.openclaw/workspace/stratronix-website-new")

NEW_TUNNEL = "https://profits-phoenix-bonus-pendant.trycloudflare.com"
SEO_CDN = "https://donaldwang6-dev.github.io/stratronix-seo"
MAIN_SITE_ID = "www.stratronix.ai"

# Analytics 注入代码 (2 行: script + noscript img)
ANALYTICS_HTML = f"""<!-- STRATRONIX AI Analytics (主站破例: Donald 2026-07-30 18:16 LOCKED) -->
<script async src="{SEO_CDN}/analytics.js" data-site="{MAIN_SITE_ID}"></script>
<noscript><img src="{NEW_TUNNEL}/collect?site={MAIN_SITE_ID}" width="1" height="1" alt="" /></noscript>
"""

# 注入标记 (用于检测是否已注入)
INJECT_MARKER = "STRATRONIX AI Analytics"

# 不部署的 HTML (备份/草稿)
SKIP_PATTERNS = [".backup", ".bak", ".tmp"]

# 核心页 (没 analytics 但需要加)
CORE_PAGES = [
    "zh/index.html",
    "index.html",
    "about.html",
    "products.html",
    "contact.html",
    "en/about.html",
    "en/products.html",
    "en/contact.html",
]


def should_skip(fp: Path) -> bool:
    return any(p in fp.name for p in SKIP_PATTERNS)


def inject_analytics(fp: Path) -> bool:
    """在 </head> 前注入 analytics 代码"""
    if not fp.exists():
        return False
    if should_skip(fp):
        return False
    content = fp.read_text(encoding="utf-8")
    if INJECT_MARKER in content:
        return False  # 已有
    if "</head>" not in content:
        return False
    new_content = content.replace("</head>", ANALYTICS_HTML + "\n</head>", 1)
    fp.write_text(new_content, encoding="utf-8")
    return True


def fix_existing(fp: Path) -> bool:
    """修复已存在的 analytics 引用 (替换旧 URL + site ID)"""
    if not fp.exists() or should_skip(fp):
        return False
    content = fp.read_text(encoding="utf-8")
    original = content

    # 替换所有 trycloudflare URL
    content = re.sub(
        r"https://[a-z0-9-]+\.trycloudflare\.com/analytics\.js",
        f"{SEO_CDN}/analytics.js",
        content
    )
    content = re.sub(
        r"https://[a-z0-9-]+\.trycloudflare\.com/collect",
        f"{NEW_TUNNEL}/collect",
        content
    )

    # 替换 site ID (主站用 www.stratronix.ai, 不是附属站 stratronix-seo)
    content = re.sub(
        r'data-site="stratronix-seo"',
        f'data-site="{MAIN_SITE_ID}"',
        content
    )
    content = re.sub(
        r'\?site=stratronix-seo',
        f'?site={MAIN_SITE_ID}',
        content
    )

    if content != original:
        fp.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    print(f"=== 主站 analytics 注入 + 死链修复 ===")
    print(f"扫描目录: {MAIN_REPO}")
    print(f"新 tunnel: {NEW_TUNNEL}")
    print(f"附属站 CDN: {SEO_CDN}")
    print(f"主站 site ID: {MAIN_SITE_ID}")
    print()

    fixed_count = 0
    injected_count = 0

    # 1. 修复所有含 trycloudflare 的 HTML (死链)
    print("--- 阶段 1: 修复死链 (替换旧 trycloudflare URL) ---")
    for f in MAIN_REPO.rglob("*.html"):
        if ".git" in str(f):
            continue
        if fix_existing(f):
            print(f"  ✅ {f.relative_to(MAIN_REPO)}")
            fixed_count += 1

    # 2. 给核心页注入 analytics (没 analytics 的核心页)
    print()
    print("--- 阶段 2: 注入 analytics 到核心页 ---")
    for path in CORE_PAGES:
        fp = MAIN_REPO / path
        if inject_analytics(fp):
            print(f"  ✅ {path}")
            injected_count += 1
        else:
            print(f"  ⏭️  {path} (已有或无 </head>)")

    print()
    print(f"=== 完成 ===")
    print(f"死链修复: {fixed_count}")
    print(f"核心页注入: {injected_count}")
    print()
    print("下一步:")
    print(f"  1. cd {MAIN_REPO}")
    print(f"  2. git add -A && git commit -m 'fix(analytics): 主站破例接入 (Donald 18:16 LOCKED)'")
    print(f"  3. git push origin master (触发 Vercel 部署)")
    print(f"  4. 访问主站任一页, 验证 DB 新增 pageview (site=www.stratronix.ai)")


if __name__ == "__main__":
    main()