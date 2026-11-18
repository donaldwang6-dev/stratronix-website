#!/bin/bash
# 多语指南站 GEO 巡检 + IndexNow 推送 (2026-10-25 JERRY)
# 作用: 保证 stratronix-guides.vercel.app 对搜索引擎/AI 爬虫持续可见
# 1) 关键路径可达性 (llms.txt / robots.txt / sitemap.xml / hub)
# 2) llms.txt 内链死链检测
# 3) IndexNow 主动推送 sitemap 全部 URL
set -u
BASE="https://stratronix-guides.vercel.app"
LOG="/home/donald/.openclaw/workspace/memory/guides-geo-check.log"
echo "===== $(date '+%F %T') =====" >> "$LOG"

FAIL=0
for p in / /en /en/ai-agent /en/sta100-spec /en/on-premise-vs-cloud /llms.txt /llms-full.txt /llms.json /robots.txt /sitemap.xml /id /de/leitfaden; do
  code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 25 "${BASE}${p}")
  echo "check ${p} → ${code}" >> "$LOG"
  [ "$code" = "200" ] || FAIL=$((FAIL+1))
done

# sitemap URL 数
N=$(curl -s --max-time 40 "${BASE}/sitemap.xml" | grep -c "<loc>")
echo "sitemap URLs = ${N}" >> "$LOG"

# llms.txt 死链（并发，最多 12）
curl -s --max-time 30 "${BASE}/llms.txt" | grep -o 'https://[^ )]*' | sed 's/[,.;:]$//' | sort -u \
 | xargs -P 12 -I{} sh -c 'c=$(curl -s -o /dev/null -w "%{http_code}" --max-time 25 -L "{}"); [ "$c" = "200" ] || echo "DEADLINK $c {}"' 2>/dev/null >> "$LOG"

bash /home/donald/.openclaw/workspace/scripts/guides_indexnow_push.sh >> "$LOG" 2>&1
echo "FAIL_COUNT=${FAIL}" >> "$LOG"
exit 0
