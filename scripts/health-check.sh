#!/usr/bin/env bash
# stratronix-website 生产环境健康检查（cron 调用）
# 用途：每小时检查 12 个页面 + 关键资源，发现掉内容时飞书告警 Donald
#
# Donald 2026-06-17 "做好了就不能丢" 原则的运行时围栏
# 即使 Vercel 部署成功，也要在用户访问前发现内容丢失

set -uo pipefail

SITE="https://www.stratronix.ai"
LOG="/home/donald/.openclaw/workspace/stratronix-website-new/logs/health-check.log"
ALERT="/home/donald/.openclaw/workspace/stratronix-website-new/logs/health-alert.log"
mkdir -p "$(dirname "$LOG")"

# 12 个页面（10 客户 + 2 后台 shop）
PAGES=(
  "en/index.html"
  "en/about.html"
  "en/products.html"
  "en/news.html"
  "en/contact.html"
  "zh/index.html"
  "zh/about.html"
  "zh/products.html"
  "zh/news.html"
  "zh/contact.html"
  "en/shop.html"
  "zh/shop.html"
)

# 关键资源
RESOURCES=(
  "css/style.css"
  "js/main.js"
  "js/core-values-animation.js"
  "js/simple-cards-animation.js"
)

ts() { date '+%Y-%m-%d %H:%M:%S'; }
log() { echo "[$(ts)] $*" >> "$LOG"; }
alert() { echo "[$(ts)] ALERT: $*" >> "$ALERT"; log "ALERT: $*"; }

# 清空上轮 alert
> "$ALERT"

log "Health check started"

fail_count=0
content_loss_count=0

# Check 1: 12 页面 HTTP 200
for page in "${PAGES[@]}"; do
  url="$SITE/$page"
  code=$(curl -sL -o /dev/null -w "%{http_code}" --max-time 8 "$url" 2>/dev/null)
  if [ "$code" != "200" ]; then
    alert "页面 HTTP 非 200: $url → $code"
    fail_count=$((fail_count + 1))
  fi
done
log "Page check done: $fail_count failures"

# Check 2: 关键资源存在 + mobile nav 元素存在
mobile_fail=0
# 各页面期望 nav-link 数量
#   en/index.html, en/products.html: 6 (含 Buy)
#   en/about.html, en/news.html, en/contact.html: 5 (无 Buy)
#   zh/ 所有客户页: 5 (无 Buy)
#   shop.html: 0 (后台页)
declare -A EXPECTED_NAV=(
  [en/index.html]=6
  [en/products.html]=6
  [en/about.html]=5
  [en/news.html]=5
  [en/contact.html]=5
  [zh/index.html]=5
  [zh/about.html]=5
  [zh/products.html]=5
  [zh/news.html]=5
  [zh/contact.html]=5
)
for page in "${!EXPECTED_NAV[@]}"; do
  body=$(curl -sL --max-time 8 "$SITE/$page" 2>/dev/null)
  if ! echo "$body" | grep -q 'id="navToggle"'; then
    alert "$page 缺 navToggle（mobile 汉堡按钮丢失！）"
    mobile_fail=$((mobile_fail + 1))
    content_loss_count=$((content_loss_count + 1))
  fi
  if ! echo "$body" | grep -q 'id="navMenu"'; then
    alert "$page 缺 navMenu（mobile 菜单容器丢失！）"
    mobile_fail=$((mobile_fail + 1))
    content_loss_count=$((content_loss_count + 1))
  fi
  expected=${EXPECTED_NAV[$page]}
  actual_links=$(echo "$body" | grep -cF 'class="nav-link' || true)
  if [ "$actual_links" -lt $expected ]; then
    alert "$page nav-link 数量异常: 实际 $actual_links, 期望 ≥$expected"
    content_loss_count=$((content_loss_count + 1))
  fi
done
log "Mobile nav check done: $mobile_fail failures"

# Check 3: 关键资源 200
for res in "${RESOURCES[@]}"; do
  url="$SITE/$res"
  code=$(curl -sL -o /dev/null -w "%{http_code}" --max-time 8 "$url" 2>/dev/null)
  if [ "$code" != "200" ]; then
    alert "关键资源 404/失败: $url → $code"
    fail_count=$((fail_count + 1))
  fi
done
log "Resource check done"

# Check 4: 1t 拼写检测（en/zh 各抽查首页）
for page in en/index.html zh/index.html; do
  body=$(curl -sL --max-time 8 "$SITE/$page" 2>/dev/null)
  # 排除注释里说明性的 '1t typo'
  bad=$(echo "$body" | grep -oE 'https?://[^"]*stratonix\.ai[^"]*' \
    | grep -vE 'stratronix\.ai' \
    | grep -vE 'intentionally|typo' \
    || true)
  if [ -n "$bad" ]; then
    alert "$page 仍有 1t 拼写 URL: $bad"
    content_loss_count=$((content_loss_count + 1))
  fi
done
log "Typo check done"

# 总结
total_issues=$((fail_count + content_loss_count))
if [ $total_issues -gt 0 ]; then
  log "FAILED: $total_issues issues detected"
  # 飞书告警（用现有的 feishu 工具）
  if [ -x /home/donald/.npm-global/bin/openclaw ]; then
    msg="🚨 STRATRONIX 网站健康检查失败 ($total_issues 问题)
- 页面 200 失败: $fail_count
- 内容丢失/拼写错误: $content_loss_count

详情: $ALERT
时间: $(ts)"

    /home/donald/.npm-global/bin/openclaw message send feishu "$msg" 2>/dev/null || true
  fi
  exit 1
else
  log "PASSED: all checks OK"
  exit 0
fi
