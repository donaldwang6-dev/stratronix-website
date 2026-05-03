#!/bin/bash

# Stratronix.ai Vercel部署脚本
# 使用方法：./deploy-vercel.sh

set -e

echo "🚀 开始部署 Stratronix.ai 到 Vercel..."

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 检查是否安装了vercel-cli
if ! command -v vercel &> /dev/null; then
    echo "📦 安装 Vercel CLI..."
    npm install -g vercel
fi

# 检查当前目录
if [ ! -f "index.html" ]; then
    echo "❌ 错误：请在网站根目录运行此脚本"
    exit 1
fi

echo "📁 检查网站文件..."
ls -la

echo "🔧 创建部署配置..."
cat > .vercel/project.json << EOF
{
  "orgId": "team_xxx",
  "projectId": "prj_xxx",
  "settings": {
    "createdAt": 1712563200000,
    "framework": "static",
    "devCommand": null,
    "installCommand": null,
    "buildCommand": null,
    "outputDirectory": null,
    "rootDirectory": null,
    "directoryListing": false,
    "nodeVersion": "18.x"
  }
}
EOF

echo "🌐 开始部署到 Vercel..."
echo "请按照以下步骤操作："
echo ""
echo "1. 访问 https://vercel.com"
echo "2. 使用 GitHub 账号登录"
echo "3. 点击 'New Project'"
echo "4. 导入 stratronix-website 项目"
echo "5. 配置设置："
echo "   - Framework: Static"
echo "   - Build Command: (留空)"
echo "   - Output Directory: (留空)"
echo "6. 点击 'Deploy'"
echo ""
echo "或者使用 Vercel CLI："
echo "vercel --prod"

echo ""
echo "📋 部署完成后，需要配置自定义域名："
echo "1. 在 Vercel 项目设置中"
echo "2. 找到 'Domains' 部分"
echo "3. 添加域名：stratronix.ai"
echo "4. 添加域名：www.stratronix.ai"
echo ""
echo "🔧 DNS 配置："
echo "在你的域名管理面板添加以下记录："
echo ""
echo "CNAME 记录："
echo "  类型：CNAME"
echo "  名称：www"
echo "  值：cname.vercel-dns.com"
echo "  TTL：自动"
echo ""
echo "A 记录（根域名重定向）："
echo "  类型：A"
echo "  名称：@"
echo "  值：76.76.21.21"
echo "  TTL：自动"
echo ""
echo "⏱️ DNS 传播时间：5-30分钟"
echo "🔒 SSL 证书：自动配置"
echo "🚀 CDN：全球加速"

echo ""
echo -e "${GREEN}✅ 部署指南已生成！${NC}"
echo ""
echo "📁 项目文件已准备就绪："
echo "- index.html (语言选择页)"
echo "- en/ (英文版本)"
echo "- zh/ (中文版本)"
echo "- admin/ (后台管理)"
echo "- vercel.json (部署配置)"
echo ""
echo "🚀 现在你可以："
echo "1. 手动上传到 Vercel"
echo "2. 或使用 GitHub 仓库自动部署"
echo "3. 或联系我帮你完成部署"

exit 0