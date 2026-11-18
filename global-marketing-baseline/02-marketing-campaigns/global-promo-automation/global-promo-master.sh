#!/bin/bash
# 全球推广主控脚本 - 一键运行所有自动化
# Donald 2026-08-18 16:30 LOCKED: "自己写代码去全球推广"

set -e
cd /home/donald/.openclaw/workspace/global-promo-automation

LOG_FILE="logs/master-$(date +%Y%m%d).log"
echo "" >> $LOG_FILE
echo "============================================" >> $LOG_FILE
echo "🌍 全球推广主控 · $(date -Iseconds)" >> $LOG_FILE
echo "============================================" >> $LOG_FILE

echo "🟢 1. 全球 100+ 平台自动提交..."
python3 auto-submit-global.py >> $LOG_FILE 2>&1

echo ""
echo "🟢 2. 跨平台文案生成..."
python3 multi-platform-auto-poster.py >> $LOG_FILE 2>&1

echo ""
echo "🟢 3. 8 语言软文批量改写..."
python3 auto-rewrite-publish.py >> $LOG_FILE 2>&1

echo ""
echo "🟢 4. 关键词排名监控（可选 / 慢）..."
if [ "${SKIP_TRACKER:-false}" != "true" ]; then
  python3 global-keyword-tracker.py >> $LOG_FILE 2>&1 || true
fi

echo ""
echo "✅ 全球推广主控完成 · $(date -Iseconds)"
echo "📊 日志: $LOG_FILE"
echo ""
echo "🎯 下一步:"
echo "  1. 查看 social-media-drafts.json → 汪总授权后实际发布"
echo "  2. 查看 data/articles-8lang/ → 80 篇文章待发布"
echo "  3. 查看 data/rank-tracking.json → 关键词排名变化"