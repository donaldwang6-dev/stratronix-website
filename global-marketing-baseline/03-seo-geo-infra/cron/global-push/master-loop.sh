#!/usr/bin/env bash
# ============================================================================
# master-loop.sh — 24/7 全球推送 STRATRONIX 总调度 (CEO LOCKED 13:52)
# 用途: 调度所有 7 个推送子脚本 + 索引重推 + 监控
# 频率: cron 每 30 分钟调用一次
# ============================================================================
set -e

ROOT="/home/donald/.openclaw/workspace/cron/global-push"
SCRIPTS="$ROOT/scripts"
LOG_DIR="$ROOT/logs"
MASTER_LOG="$LOG_DIR/master.log"

mkdir -p "$LOG_DIR"
ts=$(date '+%Y-%m-%d %H:%M:%S')

# 总日志
echo "" >> "$MASTER_LOG"
echo "============================================================" >> "$MASTER_LOG"
echo "  [$ts] Master Loop — STRATRONIX Global Push (24/7)" >> "$MASTER_LOG"
echo "============================================================" >> "$MASTER_LOG"

# 调度子脚本
total=0
total_ok=0

# 1. RSS Ping (16 个 ping 服务)
echo "" >> "$MASTER_LOG"
echo "--- [1/7] RSS Ping ---" >> "$MASTER_LOG"
if bash "$SCRIPTS/01-rss-ping.sh" >> "$MASTER_LOG" 2>&1; then
    total_ok=$((total_ok + 1))
fi
total=$((total + 1))
sleep 2

# 2. AI 目录 form_post
echo "" >> "$MASTER_LOG"
echo "--- [2/7] AI Directory Push ---" >> "$MASTER_LOG"
if bash "$SCRIPTS/02-ai-directory-push.sh" >> "$MASTER_LOG" 2>&1; then
    total_ok=$((total_ok + 1))
fi
total=$((total + 1))
sleep 2

# 3. Multi-Ping (搜索引擎 + Pingomatic)
echo "" >> "$MASTER_LOG"
echo "--- [3/7] Multi-Ping ---" >> "$MASTER_LOG"
if bash "$SCRIPTS/03-multi-ping.sh" >> "$MASTER_LOG" 2>&1; then
    total_ok=$((total_ok + 1))
fi
total=$((total + 1))
sleep 2

# 4. Wayback 实时归档
echo "" >> "$MASTER_LOG"
echo "--- [4/7] Wayback Machine ---" >> "$MASTER_LOG"
if bash "$SCRIPTS/04-wayback-realtime.sh" >> "$MASTER_LOG" 2>&1; then
    total_ok=$((total_ok + 1))
fi
total=$((total + 1))
sleep 2

# 5. Cross-link audit
echo "" >> "$MASTER_LOG"
echo "--- [5/7] Cross-Link Audit ---" >> "$MASTER_LOG"
if bash "$SCRIPTS/05-cross-link-audit.sh" >> "$MASTER_LOG" 2>&1; then
    total_ok=$((total_ok + 1))
fi
total=$((total + 1))
sleep 2

# 6. Content rotate (每日主推)
echo "" >> "$MASTER_LOG"
echo "--- [6/7] Content Rotate ---" >> "$MASTER_LOG"
if bash "$SCRIPTS/06-content-rotate.sh" >> "$MASTER_LOG" 2>&1; then
    total_ok=$((total_ok + 1))
fi
total=$((total + 1))
sleep 2

# 7. Aggregator RSS check
echo "" >> "$MASTER_LOG"
echo "--- [7/7] Aggregator RSS ---" >> "$MASTER_LOG"
if bash "$SCRIPTS/07-aggregator-rss.sh" >> "$MASTER_LOG" 2>&1; then
    total_ok=$((total_ok + 1))
fi
total=$((total + 1))

# === IndexNow 重推 (复用已有 seo-multi-push) ===
echo "" >> "$MASTER_LOG"
echo "--- [EXTRA] IndexNow Multi-Engine Push ---" >> "$MASTER_LOG"
if bash /home/donald/.openclaw/workspace/cron/seo-multi-push/auto-indexnow-seo.sh >> "$MASTER_LOG" 2>&1; then
    total_ok=$((total_ok + 1))
fi
total=$((total + 1))

# === 百度主动推送 (铁律 42 LOCKED 21:07) ===
echo "" >> "$MASTER_LOG"
echo "--- [EXTRA] Baidu Push (master_loop integration) ---" >> "$MASTER_LOG"
if python3 /home/donald/.openclaw/workspace/cron/auto-register/baidu_extreme_push.py >> "$MASTER_LOG" 2>&1; then
    total_ok=$((total_ok + 1))
fi
total=$((total + 1))

# === 总结 ===
echo "" >> "$MASTER_LOG"
echo "  [$ts] === Master Loop 完成: $total_ok/$total 子任务成功 ===" >> "$MASTER_LOG"
echo "" >> "$MASTER_LOG"

# 简化输出
echo "📡 STRATRONIX Master Loop [$ts]: $total_ok/$total 子任务成功"