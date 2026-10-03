#!/bin/bash

# Stratronix网站搜索引擎自动提交助手
# 这个脚本不能自动登录，但会生成所有需要的文件和指南

set -e

echo "🚀 Stratronix网站搜索引擎提交助手"
echo "=========================================="
echo ""

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 创建必要的目录
mkdir -p seo-files
mkdir -p verification-files

echo "${BLUE}📁 创建SEO优化文件...${NC}"
echo ""

# 1. 创建Google Search Console指南
cat > seo-files/google-search-console-guide.md << 'EOF'
# Google Search Console 提交指南

## 步骤1: 访问Google Search Console
- 网址: https://search.google.com/search-console
- 使用你的Google账号登录

## 步骤2: 添加网站资源
1. 点击左上角的"添加资源"按钮
2. 选择"网址前缀"方式
3. 输入: `https://www.stratronix.ai/`
4. 点击"继续"

## 步骤3: 验证所有权
### 方法A: HTML标签验证（推荐）
1. 选择"HTML标签"验证方法
2. 复制提供的meta标签代码，例如:
   ```html
   <meta name="google-site-verification" content="abc123def456ghi789" />
   ```
3. 将此标签添加到网站首页的`<head>`部分
4. 回到Search Console点击"验证"

### 方法B: HTML文件上传
1. 选择"HTML文件"验证方法
2. 下载提供的HTML文件
3. 上传到网站根目录: `/verification-files/google-verification.html`
4. 确保可以通过 https://www.stratronix.ai/verification-files/google-verification.html 访问
5. 点击"验证"

## 步骤4: 提交Sitemap
1. 验证成功后，点击左侧菜单的"Sitemaps"
2. 在"添加新的Sitemap"框中输入: `https://www.stratronix.ai/sitemap.xml`
3. 点击"提交"

## 步骤5: 请求索引
1. 点击左侧菜单的"网址检查"
2. 输入首页URL: `https://www.stratronix.ai/`
3. 点击"请求编入索引"

## 重要设置
1. **目标国家/地区**: 设置为"中国"或"全球"
2. **增强功能**: 启用所有可用的增强功能
3. **安全与手动操作**: 定期检查是否有安全问题

## 监控指标
- 索引覆盖率
- 搜索性能
- 移动设备适合性
- 核心网页指标
EOF

echo "${GREEN}✅ Google Search Console指南已创建: seo-files/google-search-console-guide.md${NC}"

# 2. 创建Bing Webmaster Tools指南
cat > seo-files/bing-webmaster-guide.md << 'EOF'
# Bing Webmaster Tools 提交指南

## 步骤1: 访问Bing Webmaster Tools
- 网址: https://www.bing.com/webmasters
- 使用Microsoft账号登录（可以用Google账号登录）

## 步骤2: 添加网站
1. 点击"添加网站"按钮
2. 输入网站URL: `https://www.stratronix.ai/`
3. 点击"添加"

## 步骤3: 验证所有权
### 方法A: XML文件验证（最简单）
1. 选择"XML文件"验证方法
2. 下载提供的XML文件（名称类似: `BingSiteAuth.xml`）
3. 上传到网站根目录
4. 确保可以通过 https://www.stratronix.ai/BingSiteAuth.xml 访问
5. 点击"验证"

### 方法B: Meta标签验证
1. 选择"Meta标签"验证方法
2. 复制提供的meta标签
3. 添加到网站首页的`<head>`部分
4. 点击"验证"

## 步骤4: 提交Sitemap
1. 验证成功后，点击左侧的"配置我的网站"
2. 选择"Sitemaps"
3. 输入: `https://www.stratronix.ai/sitemap.xml`
4. 点击"提交"

## 步骤5: 提交URL
1. 点击左侧的"提交URL"
2. 输入重要页面的URL
3. 点击"提交"

## Bing特有功能
1. **关键词研究**: 查看用户在Bing上搜索什么
2. **SEO报告**: 获取网站SEO建议
3. **反向链接**: 查看谁链接到你的网站
EOF

echo "${GREEN}✅ Bing Webmaster Tools指南已创建: seo-files/bing-webmaster-guide.md${NC}"

# 3. 创建百度站长平台指南
cat > seo-files/baidu-webmaster-guide.md << 'EOF'
# 百度站长平台提交指南

## 重要说明
百度站长平台需要中国手机号验证，如果你没有，可以考虑以下替代方案：

## 替代方案A: 通过合作伙伴
1. 寻找在中国的合作伙伴或朋友帮忙验证
2. 使用他们的手机号接收验证码
3. 完成后将账号转移给你

## 替代方案B: 国际版百度
尝试访问: https://ziyuan.baidu-intl.com (国际版)

## 替代方案C: 专注其他搜索引擎
如果百度验证太困难，可以优先做好Google和Bing

## 如果能够验证的步骤:

### 步骤1: 访问百度站长平台
- 网址: https://ziyuan.baidu.com
- 使用百度账号登录

### 步骤2: 添加网站
1. 点击"添加网站"
2. 输入: `https://www.stratronix.ai/`
3. 选择网站类型: "PC站"和"移动站"

### 步骤3: 验证所有权
1. **文件验证**: 下载HTML文件，上传到网站根目录
2. **CNAME验证**: 在DNS中添加CNAME记录
3. **代码验证**: 添加meta标签到首页

### 步骤4: 提交Sitemap
1. 点击"链接提交"
2. 选择"sitemap"提交方式
3. 输入: `https://www.stratronix.ai/sitemap.xml`

### 步骤5: 百度优化建议
1. **移动适配**: 确保网站在手机上显示良好
2. **MIP加速**: 考虑使用百度MIP技术
3. **结构化数据**: 添加百度支持的结构化数据
EOF

echo "${GREEN}✅ 百度站长平台指南已创建: seo-files/baidu-webmaster-guide.md${NC}"

# 4. 创建自动化检查脚本
cat > seo-files/auto-check-verification.sh << 'EOF'
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
EOF

chmod +x seo-files/auto-check-verification.sh

echo "${GREEN}✅ 自动检查脚本已创建: seo-files/auto-check-verification.sh${NC}"

# 5. 创建一键部署脚本
cat > deploy-seo-files.sh << 'EOF'
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
EOF

chmod +x deploy-seo-files.sh

echo "${GREEN}✅ 部署脚本已创建: deploy-seo-files.sh${NC}"

echo ""
echo "=========================================="
echo "${GREEN}🎉 SEO提交工具包创建完成！${NC}"
echo "=========================================="
echo ""
echo "📋 已创建的文件:"
echo ""
echo "1. ${BLUE}SEO指南文件:${NC}"
echo "   - seo-files/google-search-console-guide.md"
echo "   - seo-files/bing-webmaster-guide.md"
echo "   - seo-files/baidu-webmaster-guide.md"
echo ""
echo "2. ${BLUE}工具脚本:${NC}"
echo "   - seo-files/auto-check-verification.sh"
echo "   - deploy-seo-files.sh"
echo "   - check-seo-status.sh (之前已创建)"
echo ""
echo "3. ${BLUE}验证文件模板:${NC}"
echo "   - google-site-verification.html"
echo ""
echo "🚀 ${YELLOW}下一步操作:${NC}"
echo ""
echo "A. ${GREEN}简单方法（推荐）:${NC}"
echo "   1. 访问 https://search.google.com/search-console"
echo "   2. 添加网站: https://www.stratronix.ai/"
echo "   3. 选择'HTML文件'验证方法"
echo "   4. 下载Google提供的HTML文件"
echo "   5. 上传到网站根目录"
echo "   6. 点击'验证'"
echo ""
echo "B. ${GREEN}详细方法:${NC}"
echo "   1. 运行: ./deploy-seo-files.sh"
echo "   2. 阅读: seo-files/google-search-console-guide.md"
echo "   3. 按照步骤操作"
echo ""
echo "C. ${GREEN}需要帮助时:${NC}"
echo "   1. 截图Google Search Console验证页面"
echo "   2. 发给我，我告诉你具体操作"
echo "   3. 或者找懂技术的朋友帮忙"
echo ""
echo "⚠️ ${RED}重要提醒:${NC}"
echo "- 我不能直接登录你的账号（安全原因）"
echo "- 验证需要你亲自操作"
echo "- 整个过程大约需要30分钟"
echo "- 验证后1-2天搜索引擎开始抓取"
echo ""
echo "📞 随时告诉我进展，我会指导下一步！"
EOF

chmod +x automated-seo-submission.sh

echo "${GREEN}✅ 自动化提交助手脚本已创建: automated-seo-submission.sh${NC}"

echo ""
echo "=========================================="
echo "${YELLOW}🚀 现在运行自动化脚本:${NC}"
echo "=========================================="
echo ""
echo "运行命令:"
echo "./automated-seo-submission.sh"
echo ""
echo "这将创建所有需要的文件和指南！"

exit 0