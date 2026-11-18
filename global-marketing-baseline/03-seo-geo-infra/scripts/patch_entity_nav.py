#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P1 · 实体页导航接线：把 /{lang}/about-stratronix 挂进各语言首页与 footer
只改 multilang-site/site（不碰主站）
"""
import os, re, glob

SITE = "/home/donald/.openclaw/workspace/multilang-site/site"
BASE = "https://stratronix-guides.vercel.app"

# 语言目录 → 实体页语言代码
LANGS = ["en", "zh", "de", "id", "es", "fr", "pt", "ja", "ro"]

# 各语言"关于"文案
LBL = {
    "en": "About STRATRONIX", "zh": "关于 STRATRONIX", "de": "Über STRATRONIX",
    "id": "Tentang STRATRONIX", "es": "Sobre STRATRONIX", "fr": "À propos de STRATRONIX",
    "pt": "Sobre a STRATRONIX", "ja": "STRATRONIX について", "ro": "Despre STRATRONIX",
}

FOOTER_LINK = (
    '<a href="{base}/{lg}/about-stratronix">{label}</a> &nbsp;|&nbsp; '
)


def patch_footer(path, lg):
    h = open(path, encoding="utf-8").read()
    if "about-stratronix" in h:
        return "skip(已含)"
    # 在 footer 内找 llms.txt 链接前插入实体页链接
    m = re.search(r'(<footer[^>]*>)', h)
    if not m:
        return "no-footer"
    ins = FOOTER_LINK.format(base=BASE, lg=lg, label=LBL[lg])
    # 插到 footer 首个 <p> 之后
    fm = re.search(r'(<footer[^>]*>\s*<p>)', h)
    if fm:
        h = h[:fm.end()] + "\n" + ins + h[fm.end():]
    else:
        h = h[:m.end()] + "\n<p>" + ins + h[m.end():]
    open(path, "w", encoding="utf-8").write(h)
    return "ok"


def main():
    changed = 0
    # 1) 各语言首页
    for lg in LANGS:
        p = os.path.join(SITE, lg, "index.html")
        if os.path.exists(p):
            r = patch_footer(p, lg)
            print(f"[home] {lg:3s} {r}")
            if r == "ok":
                changed += 1
        else:
            print(f"[home] {lg:3s} 无 index.html")

    # 2) 各语言实体页自身 footer 加上同语言首页 + 兄弟语言
    for lg in LANGS:
        p = os.path.join(SITE, lg, "about-stratronix.html")
        if not os.path.exists(p):
            continue
        h = open(p, encoding="utf-8").read()
        if 'class="langs"' in h:
            print(f"[entity] {lg:3s} skip")
            continue
        links = " · ".join(
            f'<a href="{BASE}/{l}/about-stratronix">{LBL[l]}</a>' for l in LANGS
            if l != lg
        )
        block = (
            '<p style="margin-top:8px"><strong>Company identity pages</strong><br>'
            f'{links}</p>\n'
        )
        m = re.search(r'(<footer>\s*<p>STRATRONIX)', h)
        if m:
            h = h[:m.start()] + block + h[m.start():]
        else:
            m2 = re.search(r'(<footer>)', h)
            h = h[:m2.end()] + "\n" + block + h[m2.end():]
        open(p, "w", encoding="utf-8").write(h)
        print(f"[entity] {lg:3s} ok")
        changed += 1

    print(f"\n共改动 {changed} 个文件")


if __name__ == "__main__":
    main()
