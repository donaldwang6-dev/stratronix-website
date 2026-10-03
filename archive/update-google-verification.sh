#!/bin/bash

# 一键更新Google验证代码脚本
# 使用方法: ./update-google-verification.sh YOUR_VERIFICATION_CODE

set -e

echo "🚀 更新Google验证代码"
echo "========================"

# 检查参数
if [ $# -eq 0 ]; then
    echo "❌ 错误: 请提供Google验证代码"
    echo "使用方法: ./update-google-verification.sh YOUR_CODE"
    echo "示例: ./update-google-verification.sh abc123def456ghi789"
    exit 1
fi

VERIFICATION_CODE="$1"

echo "验证代码: $VERIFICATION_CODE"
echo ""

# 更新Google验证文件
echo "📝 更新Google验证文件..."

# 更新根目录的文件
sed -i "s/GOOGLE_VERIFICATION_CODE_HERE/$VERIFICATION_CODE/g" google-verification.html

# 更新verification目录的文件
sed -i "s/GOOGLE_VERIFICATION_CODE_HERE/$VERIFICATION_CODE/g" verification/google-verification.html

echo "✅ Google验证文件已更新"
echo ""

# 提交到Git
echo "📦 提交更改到Git..."
git add google-verification.html verification/google-verification.html
git commit -m "更新Google验证代码: $VERIFICATION_CODE" 2>/dev/null || true

echo "✅ 更改已提交"
echo ""

# 推送到GitHub
echo "🚀 推送到GitHub..."
if git push origin main 2>/dev/null; then
    echo "✅ 成功推送到GitHub"
else
    echo "⚠️ 推送到GitHub失败，可能需要手动推送"
    echo "手动推送命令: git push origin main"
fi

echo ""
echo "========================"
echo "🎉 Google验证代码更新完成！"
echo "========================"
echo ""
echo "📋 下一步操作:"
echo ""
echo "1. 回到Google Search Console页面"
echo "2. 点击'验证'按钮"
echo "3. 等待验证结果（通常立即生效）"
echo ""
echo "🔗 验证文件URL:"
echo "- https://www.stratronix.ai/google-verification.html"
echo ""
echo "⏱️ 部署时间: 1-2分钟生效"
echo "✅ 验证时间: 立即生效"
echo ""
echo "📞 如果验证失败:"
echo "1. 截图错误信息发给我"
echo "2. 我帮你分析原因"
echo "3. 提供解决方案"
echo ""
echo "🚀 验证成功后，我会帮你提交到Bing和百度！"

exit 0