#!/bin/bash
# 00:00 SEO+GEO 全量推送 —— 零模型调用
set -u
WS=/home/donald/.openclaw/workspace
LOG=$WS/memory/geo_push.log
TARGET=user:ou_c84e7b0208ec4b0c3f1255b5258525da
COOK_HOST="User@192.168.1.184"   # 汪杰 2026-10-26：例行报告只发 COOK，不直发汪总
cd "$WS"
echo "===== $(date '+%F %T') =====" >> "$LOG"
G="$WS/stratronix-seo/2026-09-22-geo-boost"

# 1) 启动 GEO 永恒循环（后台，8小时上限）
( cd "$G" && MAX_HOURS=8 setsid bash scripts/geo_eternal_loop.sh > logs/geo_run_$(date +%Y%m%d_%H%M%S).log 2>&1 < /dev/null & disown ) >> "$LOG" 2>&1
sleep 3
PID=$(pgrep -f geo_eternal_loop.sh | head -1)

# 2) 官网检查
MAIN=$(curl -s -o /dev/null -w "%{http_code}" --max-time 20 https://www.stratronix.ai)
STORE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 20 https://store.stratronix.ai)

# 3) 百度主动推送（remain>5 才推）
BD=$(curl -s --max-time 30 "http://data.zz.baidu.com/urls?site=https://www.stratronix.ai&token=${BAIDU_TOKEN}" -X POST -H "Content-Type: text/plain" -d "https://www.stratronix.ai")

# 4) IndexNow 全平台推送
IN=$(timeout 900 python3 "$G/scripts/push_all_platforms.py" 2>&1 | tail -5)

SUM="主站 $MAIN / 门店 $STORE | GEO PID ${PID:-无} | 百度 $(echo "$BD" | head -c 120) | IndexNow $(echo "$IN" | tr '\n' ' ' | head -c 200)"

# 例行推送 → 只发 COOK（汪杰 2026-10-26 06:50 指令）
PAYLOAD=$(jq -nc --arg d "$(date +%F)" --arg s "$SUM" \
  '{task_id:("geo-push-"+$d), status:"completed", type:"SEO+GEO推送", date:$d, summary:$s, note:"例行推送结果，仅供 COOK 汇总"}')
bash /home/donald/.agents/push-to-cook.sh result "geo-push-$(date +%F)" "$PAYLOAD" >> "$LOG" 2>&1
echo "done main=$MAIN store=$STORE (已推COOK)" >> "$LOG"
