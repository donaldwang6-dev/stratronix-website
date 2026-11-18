import glob, os

NEW = "https://stratronix-guides.vercel.app"
rows = {}

for f in glob.glob("**/*.html", recursive=True):
    f = f.replace(os.sep, "/")
    d, base = os.path.split(f)
    slug = base[:-5] if base.endswith(".html") else base
    if slug == "index":                       # index.html 就是目录本身
        u = "/" + d if d else "/"
    else:
        u = "/" + "/".join(p for p in (d, slug) if p)
    if u == "/404":
        continue
    if slug == "about-stratronix":
        # 2026-11-18 P1：品牌实体中心页 = Google 实体消歧 + GEO 锚点，最高优先级
        pri = "1.0"
    elif d in ("id/panduan", "de/leitfaden"):
        pri = "0.9"
    elif d in ("id", "de", "en", "es", "fr", "pt", "ja", "ro", "zh"):
        pri = "0.8"
    else:
        pri = "0.7"
    rows[u] = pri

lines = [
    f'  <url><loc>{NEW}{u}</loc><lastmod>2026-10-27</lastmod>'
    f'<changefreq>monthly</changefreq><priority>{rows[u]}</priority></url>'
    for u in sorted(rows)
]
xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
       + "\n".join(lines) + "\n</urlset>\n")
open("sitemap.xml", "w", encoding="utf-8").write(xml)
print(f"sitemap: {len(rows)} 条 URL")
for u in sorted(rows)[:5]:
    print("  ", u)