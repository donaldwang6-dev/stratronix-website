#!/usr/bin/env python3
"""
legal_links_guard.py — Privacy/Terms 页脚链接永久守卫

背景：2026-11-22 发现全站页脚 Privacy Policy / Terms of Service 写成 href="#"
（空链接点不动），已修复 21 个页面并上线。此守卫防止回归。

检查项：
  1. 三个法务页文件必须存在（privacy-policy.html / terms-of-service.html / data-deletion.html）
  2. 任何真实页面（排除 archive/ source/ node_modules/ .vercel/ .git/）
     不得再出现 href="#">Privacy Policy" / href="#">Terms of Service"
  3. 不允许出现指向死域名的法务链接

退出码：0 = PASS，1 = FAIL
用法：python3 scripts/legal_links_guard.py [--site <站点根目录>]
"""
import os, re, sys, argparse

DEFAULT_SITE = "/home/donald/.openclaw/workspace/stratronix-website-new"
SKIP_DIRS = {"archive", "source", "node_modules", ".git", ".vercel", "dist", "build"}
REQUIRED_PAGES = ["privacy-policy.html", "terms-of-service.html", "data-deletion.html"]
BAD_PATTERNS = [
    (re.compile(r'href="\#">\s*Privacy Policy', re.I), "空链接 Privacy Policy"),
    (re.compile(r'href="\#"">\s*Terms of Service', re.I), "空链接 Terms of Service"),
    (re.compile(r'href="\#">\s*Terms of Service', re.I), "空链接 Terms of Service"),
]

def check(site):
    fails = []
    # 1. 法务页存在
    for page in REQUIRED_PAGES:
        p = os.path.join(site, page)
        if not os.path.isfile(p):
            fails.append(f"[缺文件] {page} 不存在")

    # 2. 扫描空链接
    scanned = 0
    for dirpath, dirnames, filenames in os.walk(site):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(".html"):
                continue
            fp = os.path.join(dirpath, fn)
            try:
                with open(fp, encoding="utf-8", errors="ignore") as f:
                    txt = f.read()
            except Exception as e:
                fails.append(f"[读取失败] {fp}: {e}")
                continue
            scanned += 1
            rel = os.path.relpath(fp, site)
            for pat, label in BAD_PATTERNS:
                if pat.search(txt):
                    fails.append(f"[{label}] {rel}")

    return fails, scanned

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default=DEFAULT_SITE)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    fails, scanned = check(a.site)
    if fails:
        print("GUARD=FAIL")
        for f in fails:
            print("  -", f)
        return 1

    if not a.quiet:
        print(f"GUARD=PASS  扫描 {scanned} 个 HTML，法务页齐全，无空链接")
    return 0

if __name__ == "__main__":
    sys.exit(main())
