#!/bin/bash

# 部署SEO文件到网站

echo "🚀 部署SEO优化文件到Stratronix网站..."
echo ""

# 检查是否在正确目录
if [ ! -f "index.html" ]; then
    echo "❌ 错误: 请在网站根目录运行此脚本"
    exit 1
fi

# 创建验证文件目录
mkdir -p verification-files

# 复制Google验证文件模板
if [ -f "google-site-verification.html" ]; then
    cp google-site-verification.html verification-files/
    echo "✅ 复制Google验证文件模板"
fi

# 确保robots.txt存在
if [ ! -f "robots.txt" ]; then
    echo "❌ robots.txt不存在，请创建"
else
    echo "✅ robots.txt已存在"
fi

# 确保sitemap.xml存在
if [ ! -f "sitemap.xml" ]; then
    echo "❌ sitemap.xml不存在，请创建"
else
    echo "✅ sitemap.xml已存在"
fi

echo ""
echo "📁 已创建的文件结构:"
echo "- verification-files/          # 验证文件目录"
echo "  └── google-site-verification.html"
echo "- seo-files/                  # SEO指南目录"
echo "  ├── google-search-console-guide.md"
echo "  ├── bing-webmaster-guide.md"
echo "  ├── baidu-webmaster-guide.md"
echo "  └── auto-check-verification.sh"
echo "- deploy-seo-files.sh         # 部署脚本"
echo "- check-seo-status.sh         # SEO状态检查"
echo ""

echo "🌐 现在你需要:"
echo "1. 将整个网站部署到服务器"
echo "2. 访问Google Search Console提交网站"
echo "3. 按照指南完成验证"
echo ""

echo "📧 如果需要帮助，可以:"
echo "1. 截图Google Search Console的验证页面发给我"
echo "2. 我帮你生成正确的验证代码"
echo "3. 或者寻找技术支持人员帮忙"
