#!/bin/bash

# 自动检查验证文件是否可访问

echo "🔍 检查搜索引擎验证文件..."
echo ""

# 检查Google验证文件
echo "1. Google验证文件:"
if [ -f "../google-site-verification.html" ]; then
    echo "   ✅ 文件存在: google-site-verification.html"
else
    echo "   ❌ 文件不存在"
fi
echo ""

# 检查robots.txt
echo "2. Robots.txt:"
curl -s -I https://www.stratronix.ai/robots.txt | head -1
echo ""

# 检查sitemap.xml
echo "3. Sitemap.xml:"
curl -s -I https://www.stratronix.ai/sitemap.xml | head -1
echo ""

# 检查网站可访问性
echo "4. 网站可访问性:"
curl -s -I https://www.stratronix.ai/ | head -1
echo ""

echo "📋 下一步:"
echo "1. 按照指南提交到搜索引擎"
echo "2. 运行: ./check-seo-status.sh 监控进度"
echo "3. 等待1-2天让搜索引擎抓取"
