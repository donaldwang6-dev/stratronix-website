#!/bin/bash
# STRATRONIX 全球 24/7 SEO 推广系统
# LOCKED 2026-07-14 00:42 — 铁律 12 永久任务
# 2026-07-15 修正：去掉 set -e，单点网络错误不阻塞整体流程；保证最后一行"完成"必写。

LOG="/home/donald/.openclaw/workspace/seo-24-7/logs/global-seo.log"
mkdir -p "$(dirname $LOG)"

# 用 trap 保证任何情况下都写入"完成"行
trap 'echo "[$(date "+%Y-%m-%d %H:%M:%S")] 全球 SEO 推送流程结束（trap）" >> "$LOG"' EXIT

echo "[$(date '+%Y-%m-%d %H:%M:%S')] === 全球 SEO 24/7 自动推送启动 ===" >> "$LOG"

# 1. IndexNow 推送（覆盖 Bing + Yandex + Seznam + Naver + DuckDuckGo + Ecosia 等）
INDEX_KEY="stratronix2026test"
KEY_LOCATION="https://www.stratronix.ai/${INDEX_KEY}.txt"

# 全部 URL
URLS=(
  "https://www.stratronix.ai/"
  "https://www.stratronix.ai/zh"
  "https://www.stratronix.ai/products"
  "https://www.stratronix.ai/about"
  "https://www.stratronix.ai/contact"
  "https://www.stratronix.ai/brand"
  "https://www.stratronix.ai/blog/stratronix-vs-chatgpt"
  "https://www.stratronix.ai/blog/stratronix-paa-setup-guide"
  "https://www.stratronix.ai/blog/stratronix-self-hosted-ai"
  "https://www.stratronix.ai/blog/stratronix-paa-roi"
  "https://www.stratronix.ai/zh/products"
  "https://www.stratronix.ai/zh/about"
  "https://www.stratronix.ai/zh/contact"
  "https://www.stratronix.ai/zh/news"
  "https://www.stratronix.ai/zh/wechat-articles"
  "https://www.stratronix.ai/zh/ai-glossary"
  "https://www.stratronix.ai/zh/paa-vs-cloud"
  "https://www.stratronix.ai/zh/blog"
  "https://www.stratronix.ai/zh/blog/sta-100-price"
  "https://www.stratronix.ai/zh/blog/stratronix-vs-jetson-raspberry-pi"
  "https://www.stratronix.ai/zh/blog/stratronix-customer-cases"
  "https://www.stratronix.ai/zh/blog/dingtu-medical-paa"
  "https://www.stratronix.ai/zh/blog/dingtu-legal-paa"
  "https://www.stratronix.ai/zh/blog/dingtu-education-paa"
  "https://www.stratronix.ai/zh/blog/dingtu-smb-paa"
  "https://www.stratronix.ai/zh/blog/dingtu-finance-paa"
  "https://www.stratronix.ai/zh/cases"
  "https://www.stratronix.ai/zh/cases/law-firm-case"
  "https://www.stratronix.ai/zh/cases/hospital-case"
  "https://www.stratronix.ai/zh/cases/manufacturing-case"
  "https://www.stratronix.ai/zh/cases/bank-case"
  "https://www.stratronix.ai/zh/cases/school-case"
  "https://www.stratronix.ai/zh/cases/smb-case"
  "https://www.stratronix.ai/ai"
  "https://www.stratronix.ai/ai-agent"
  "https://www.stratronix.ai/ai-company"
  "https://www.stratronix.ai/shenzhen-ai"
  "https://www.stratronix.ai/ai-box"
  "https://www.stratronix.ai/ai-china"
  "https://www.stratronix.ai/openclaw"
  "https://www.stratronix.ai/sales-support"
  "https://www.stratronix.ai/sitemap.xml"
  "https://www.stratronix.ai/rss.xml"
  "https://www.stratronix.ai/producthunt"
)

# 构建 JSON urlList
URLS_JSON="["
for url in "${URLS[@]}"; do
  URLS_JSON+="\"$url\","
done
URLS_JSON="${URLS_JSON%,}]"

# 推 IndexNow（容错）
if curl -sS --max-time 30 -X POST "https://api.indexnow.org/IndexNow" \
  -H "Content-Type: application/json" \
  -d "{
    \"host\": \"www.stratronix.ai\",
    \"key\": \"$INDEX_KEY\",
    \"keyLocation\": \"$KEY_LOCATION\",
    \"urlList\": $URLS_JSON
  }" >> "$LOG" 2>&1; then
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ IndexNow 推送 ${#URLS[@]} URL 成功" >> "$LOG"
else
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] ⚠️ IndexNow 推送失败（curl exit $?），跳过" >> "$LOG"
fi

# 2. 百度主动推送（如 quota 可用）
if [ -f "/home/donald/.openclaw/workspace/baidu-launch/baidu-active-push.sh" ]; then
  BAIDU_TOKEN="${BAIDU_TOKEN:-}"  # 凭证走环境变量，明文不入库（2026-11-18 归档脱敏） \
    bash /home/donald/.openclaw/workspace/baidu-launch/baidu-active-push.sh >> "$LOG" 2>&1 || \
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ⚠️ 百度推送脚本异常退出（quota 耗尽或网络问题）" >> "$LOG"
fi

# 3. Bing sitemap ping（容错）
if curl -sS --max-time 15 "https://www.bing.com/ping?sitemap=https://www.stratronix.ai/sitemap.xml" >> "$LOG" 2>&1; then
  :
else
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] ⚠️ Bing sitemap ping 失败（curl exit $?）" >> "$LOG"
fi

# 4. Pingomatic RSS 多服务（容错 + 单次失败可重试）
if ! curl -sS --max-time 15 -X POST "https://rpc.pingomatic.com/" \
  -d "url=https://www.stratronix.ai/rss.xml" >> "$LOG" 2>&1; then
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] ⚠️ Pingomatic 第 1 次失败，5s 后重试" >> "$LOG"
  sleep 5
  curl -sS --max-time 15 -X POST "https://rpc.pingomatic.com/" \
    -d "url=https://www.stratronix.ai/rss.xml" >> "$LOG" 2>&1 || \
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ⚠️ Pingomatic 重试仍失败，跳过本次" >> "$LOG"
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 全球 SEO 推送完成" >> "$LOG"