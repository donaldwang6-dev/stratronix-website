#!/bin/bash
# STRATRONIX 全自动推送（主站 + 指南站）—— 2026-10-26 JERRY 重写
#
# ⚠️ 本脚本只做「提交 URL 给搜索引擎」，**不下载、不修改、不部署**任何站点文件。
#    主站 www.stratronix.ai 只被读取 sitemap（只读 HTTP GET），铁律 164 绝对不违反。
#
# 通道：
#   1. IndexNow 批量推送（覆盖 Bing / Yandex / Seznam / Naver 等）—— 主站全量 sitemap + 指南站全量 sitemap
#   2. 百度主动推送（主站，quota 用尽自动跳过）
#   3. Wayback Machine 归档（供 AI 训练语料与引用）
#   4. Yandex / Bing sitemap ping
set -u
WS=/home/donald/.openclaw/workspace
LOG=$WS/baidu-launch/cron/auto-push.log
mkdir -p "$(dirname "$LOG")"

MAIN_HOST="www.stratronix.ai"
GUIDES_HOST="stratronix-guides.vercel.app"
MAIN_KEY="stratronix2026test"           # 主站 IndexNow key（已存在线上）
GUIDES_KEY=$(cat /home/donald/.openclaw/secrets/indexnow_key.txt 2>/dev/null | tr -d '\n\r')
BAIDU_TOKEN=$(cat /home/donald/.openclaw/secrets/baidu_token.txt 2>/dev/null | tr -d '\n\r')
TODAY=$(date +%F)

log() { echo "[$(date '+%F %T')] $1" >> "$LOG"; }

# ---------- 收集 URL（只读 sitemap） ----------
collect() {
  curl -s --max-time 45 "$1/sitemap.xml" | grep -o '<loc>[^<]*</loc>' | sed 's|<loc>||; s|</loc>||'
}

MAIN_URLS=$(collect "https://$MAIN_HOST")
GUIDES_URLS=$(collect "https://$GUIDES_HOST")
MAIN_N=$(echo "$MAIN_URLS" | grep -c . || true)
GUIDES_N=$(echo "$GUIDES_URLS" | grep -c . || true)
log "收集完成: 主站 $MAIN_N URL / 指南站 $GUIDES_N URL"

# ---------- 1. IndexNow 批量推送 ----------
push_indexnow() {
  local host="$1" key="$2" keyloc="$3" urls="$4" n="$5"
  [ -z "$urls" ] && return
  python3 - "$key" "$host" "$keyloc" "$urls" <<'PY' >> "$LOG" 2>&1
import json, sys, urllib.request
key, host, keyloc, urls = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4].split()
body = json.dumps({"host": host, "key": key, "keyLocation": keyloc, "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                             headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
try:
    with urllib.request.urlopen(req, timeout=90) as r:
        print("IndexNow", host, r.status, r.read()[:200].decode(errors="replace"))
except Exception as e:
    print("IndexNow", host, "FAIL", e)
PY
  log "IndexNow 已提交 $host ($n URL)"
}

push_indexnow "$MAIN_HOST" "$MAIN_KEY" "https://$MAIN_HOST/${MAIN_KEY}.txt" "$MAIN_URLS" "$MAIN_N"
[ -n "$GUIDES_KEY" ] && push_indexnow "$GUIDES_HOST" "$GUIDES_KEY" "https://$GUIDES_HOST/${GUIDES_KEY}.txt" "$GUIDES_URLS" "$GUIDES_N"

# ---------- 2. 百度主动推送（主站） ----------
if [ -n "$BAIDU_TOKEN" ]; then
  BD=$(echo "$MAIN_URLS" | head -10 | while read -r u; do
        curl -s --max-time 20 "http://data.zz.baidu.com/urls?site=https://$MAIN_HOST&token=$BAIDU_TOKEN" \
          -X POST -H "Content-Type: text/plain" -d "$u"; echo; done | tail -1)
  log "百度主动推送: $BD"
fi

# ---------- 3. Wayback 归档（AI 语料 / 可引用快照） ----------
WB=$(curl -s --max-time 30 "https://web.archive.org/save/https://$GUIDES_HOST/llms.txt" -o /dev/null -w "%{http_code}")
log "Wayback 归档 llms.txt → $WB"

# ---------- 4. sitemap ping ----------
for h in "$GUIDES_HOST" "$MAIN_HOST"; do
  Y=$(curl -s --max-time 15 -o /dev/null -w "%{http_code}" "https://webmaster.yandex.com/ping?sitemap=https://$h/sitemap.xml")
  B=$(curl -s --max-time 15 -o /dev/null -w "%{http_code}" "https://www.bing.com/ping?sitemap=https://$h/sitemap.xml")
  log "ping $h → Yandex:$Y Bing:$B"
done

log "自动推送完成 ($TODAY)"
