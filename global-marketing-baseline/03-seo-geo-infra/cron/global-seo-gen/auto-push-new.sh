#!/usr/bin/env bash
# ============================================================================
# auto-push-new.sh — 新 URL 全引擎主动推送器
# 铁律 12 (24/7 全球 SEO) + 铁律 3 (自主推进)
# 用法: ./auto-push-new.sh <lang1> <lang2> ... (留空推所有新语言)
# ============================================================================

set -e

ROOT="/home/donald/.openclaw/workspace/stratronix-seo"
LOG="/home/donald/.openclaw/workspace/cron/global-seo-gen/push-new.log"
TIME=$(date '+%Y-%m-%d %H:%M:%S')

mkdir -p "$(dirname "$LOG")"

# 默认新语言列表
DEFAULT_LANGS="kk uz mn tg ne si hy"
LANGS="${*:-$DEFAULT_LANGS}"

INDEXNOW_KEY="b85a1d78-d57d-4e5b-a15d-51b2de911ef2"
INDEXNOW_KEYLOCATION="https://donaldwang6-dev.github.io/stratronix-seo/indexnow-key.txt"
HOST_URL="https://donaldwang6-dev.github.io/stratronix-seo"

echo "============================================================" >> "$LOG"
echo "[$TIME] === 全球 SEO 新语言推送: $LANGS ===" >> "$LOG"

# 收集所有 URL
URLS_JSON=""
COUNT=0
for L in $LANGS; do
    for f in $ROOT/$L/*.html; do
        [ -f "$f" ] || continue
        slug=$(basename "$f")
        url="$HOST_URL/$L/$slug"
        if [ -z "$URLS_JSON" ]; then
            URLS_JSON="\"$url\""
        else
            URLS_JSON="$URLS_JSON,\"$url\""
        fi
        COUNT=$((COUNT + 1))
    done
done

echo "[$TIME] 收集 URL: $COUNT" >> "$LOG"

if [ "$COUNT" -eq 0 ]; then
    echo "[$TIME] ❌ 没找到 URL，退出" >> "$LOG"
    exit 1
fi

URLS_LIST="[$URLS_JSON]"

# ============= IndexNow (Bing/Yandex/Seznam/Naver + Brave/Ecosia/Mojeek/Yep/Yep.com) =============
for endpoint in \
    "https://api.indexnow.org/indexnow" \
    "https://yandex.com/indexnow" \
    "https://search.seznam.cz/indexnow" \
    "https://searchadvisor.naver.com/indexnow"
do
    host=$(echo "$endpoint" | awk -F/ '{print $3}')
    result=$(curl -s -X POST "$endpoint" \
        -H "Content-Type: application/json" \
        -d "{\"host\":\"donaldwang6-dev.github.io\",\"key\":\"$INDEXNOW_KEY\",\"keyLocation\":\"$INDEXNOW_KEYLOCATION\",\"urlList\":$URLS_LIST}" \
        -m 60 -w "HTTP:%{http_code}" -o /dev/null 2>&1)
    echo "[$TIME] [IndexNow → $host] $result" >> "$LOG"
    sleep 1
done

# ============= Google sitemap ping =============
for sitemap_file in $(echo "$LANGS" | tr ' ' '\n' | sed 's/^/sitemap-/' | sed 's/$/.xml/'); do
    sitemap_url="$HOST_URL/$sitemap_file"
    gp=$(curl -s -A "STRATRONIX-Bot/1.0" \
        "https://www.google.com/ping?sitemap=$sitemap_url" \
        -m 15 -o /dev/null -w "HTTP:%{http_code}" 2>/dev/null || echo "000")
    echo "[$TIME] [Google sitemap ping] $sitemap_file → $gp" >> "$LOG"
    sleep 0.5
done

# ============= Bing sitemap ping (legacy 备份) =============
for L in $LANGS; do
    bp=$(curl -s -A "STRATRONIX-Bot/1.0" \
        "https://www.bing.com/ping?sitemap=$HOST_URL/sitemap-$L.xml" \
        -m 15 -o /dev/null -w "HTTP:%{http_code}" 2>/dev/null || echo "000")
    echo "[$TIME] [Bing sitemap ping] $L → $bp" >> "$LOG"
    sleep 0.3
done

# ============= Yandex sitemap ping =============
for L in $LANGS; do
    yp=$(curl -s -A "STRATRONIX-Bot/1.0" \
        "https://webmaster.yandex.com/ping?sitemap=$HOST_URL/sitemap-$L.xml" \
        -m 15 -o /dev/null -w "HTTP:%{http_code}" 2>/dev/null || echo "000")
    echo "[$TIME] [Yandex sitemap ping] $L → $yp" >> "$LOG"
    sleep 0.3
done

# ============= Baidu 站长平台 (主站 token 配额 10/天，省着用) =============
# 35 个新 URL 太多,先推送最重要的 8 个 (每语言 index.html)
BAIDU_TOKEN="${BAIDU_TOKEN:-}"  # 凭证走环境变量，明文不入库（2026-11-18 归档脱敏）
BAIDU_PUSH_COUNT=0
for L in $LANGS; do
    if [ $BAIDU_PUSH_COUNT -ge 8 ]; then
        echo "[$TIME] [Baidu] 配额保护: 已推送 8 URL，今日停止" >> "$LOG"
        break
    fi
    url="$HOST_URL/$L/index.html"
    bp=$(curl -s -X POST \
        "http://data.zz.baidu.com/urls?site=stratronix.ai&token=$BAIDU_TOKEN" \
        -H "Content-Type: text/plain" \
        -d "$url" \
        -m 15 2>/dev/null || echo "skip")
    echo "[$TIME] [Baidu 主动推送] $url → $bp" >> "$LOG"
    BAIDU_PUSH_COUNT=$((BAIDU_PUSH_COUNT + 1))
    sleep 1
done

# ============= Ping-O-Matic (一键 ping 30+ 服务) =============
RSS_URL="$HOST_URL/feed.xml"
PING_XML="<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<methodCall>
  <methodName>weblogUpdates.extendedPing</methodName>
  <params>
    <param><value>STRATRONIX 鼎图太易</value></param>
    <param><value>$HOST_URL/</value></param>
    <param><value>$RSS_URL</value></param>
    <param><value>$HOST_URL/blog/</value></param>
  </params>
</methodCall>"
pm=$(curl -s -m 15 -X POST -H "Content-Type: text/xml" \
    -d "$PING_XML" "https://rpc.pingomatic.com/" \
    -o /dev/null -w "HTTP:%{http_code}" 2>/dev/null || echo "000")
echo "[$TIME] [Ping-O-Matic] $pm (一次性 ping 30+ 服务)" >> "$LOG"

# ============= 总结 =============
echo "[$TIME] === 全球新语言推送完成: $COUNT URL ===" >> "$LOG"
echo "✅ 推送完成: $COUNT URL"
cat "$LOG" | tail -25