#!/bin/bash
# STRATRONIX 全自动推送脚本
# 每日凌晨 + 多次触发，推送所有 URL 到 IndexNow + 多个搜索引擎
# Donald 30 天内不用再操作

set -e

LOG="/home/donald/.openclaw/workspace/baidu-launch/cron/auto-push.log"
URLS_FILE="/home/donald/.openclaw/workspace/stratronix-website-new/scripts/all-urls.txt"
mkdir -p "$(dirname $LOG)" "$(dirname $URLS_FILE)"

# 收集所有 URL
cat > "$URLS_FILE" << 'EOF'
https://www.stratronix.ai/
https://www.stratronix.ai/products
https://www.stratronix.ai/about
https://www.stratronix.ai/contact
https://www.stratronix.ai/news
https://www.stratronix.ai/brand
https://www.stratronix.ai/zh
https://www.stratronix.ai/zh/products
https://www.stratronix.ai/zh/about
https://www.stratronix.ai/zh/contact
https://www.stratronix.ai/zh/news
https://www.stratronix.ai/zh/wechat-articles
https://www.stratronix.ai/zh/ai-glossary
https://www.stratronix.ai/zh/paa-vs-cloud
https://www.stratronix.ai/zh/blog
https://www.stratronix.ai/zh/sales-support
https://www.stratronix.ai/zh/blog/sta-100-price
https://www.stratronix.ai/zh/blog/stratronix-vs-jetson-raspberry-pi
https://www.stratronix.ai/zh/blog/stratronix-customer-cases
https://www.stratronix.ai/zh/blog/dingtu-medical-paa
https://www.stratronix.ai/zh/blog/dingtu-legal-paa
https://www.stratronix.ai/zh/blog/dingtu-education-paa
https://www.stratronix.ai/zh/blog/dingtu-smb-paa
https://www.stratronix.ai/zh/blog/dingtu-finance-paa
https://www.stratronix.ai/zh/cases
https://www.stratronix.ai/zh/cases/law-firm-case
https://www.stratronix.ai/zh/cases/hospital-case
https://www.stratronix.ai/zh/cases/manufacturing-case
https://www.stratronix.ai/zh/cases/bank-case
https://www.stratronix.ai/zh/cases/school-case
https://www.stratronix.ai/zh/cases/smb-case
https://www.stratronix.ai/blog/stratronix-vs-chatgpt
https://www.stratronix.ai/blog/stratronix-paa-setup-guide
https://www.stratronix.ai/blog/stratronix-self-hosted-ai
https://www.stratronix.ai/blog/stratronix-paa-roi
https://www.stratronix.ai/sales-support/
https://www.stratronix.ai/sitemap.xml
EOF

URL_COUNT=$(wc -l < "$URLS_FILE")
echo "[$(date '+%Y-%m-%d %H:%M:%S')] 自动推送启动：$URL_COUNT 个 URL" >> "$LOG"

# 1. IndexNow 批量推送（覆盖 Bing + Yandex + Seznam + Naver）
INDEX_KEY="stratronix2026test"
KEY_LOCATION="https://www.stratronix.ai/${INDEX_KEY}.txt"

batch_count=0
total_pushed=0

while IFS= read -r url; do
  urls_json="$urls_json\"$url\","
done < "$URLS_FILE"
urls_json="[${urls_json%,}]"

curl -sS --max-time 30 -X POST "https://api.indexnow.org/IndexNow" \
  -H "Content-Type: application/json" \
  -d "{
    \"host\": \"www.stratronix.ai\",
    \"key\": \"$INDEX_KEY\",
    \"keyLocation\": \"$KEY_LOCATION\",
    \"urlList\": $urls_json
  }" >> "$LOG" 2>&1
echo "[$(date '+%Y-%m-%d %H:%M:%S')] IndexNow 大批量推送 $URL_COUNT URL" >> "$LOG"

# 2. 百度主动推送（10/天 quota）
if [ -f "/home/donald/.openclaw/workspace/baidu-launch/baidu-active-push.sh" ]; then
  bash /home/donald/.openclaw/workspace/baidu-launch/baidu-active-push.sh >> "$LOG" 2>&1
fi

# 3. Bing sitemap ping
curl -sS --max-time 10 "https://www.bing.com/ping?sitemap=https://www.stratronix.ai/sitemap.xml" >> "$LOG" 2>&1

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 自动推送完成" >> "$LOG"