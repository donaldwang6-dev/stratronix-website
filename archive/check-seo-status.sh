#!/bin/bash

# Stratronix网站SEO状态检查脚本
# 使用方法: ./check-seo-status.sh

set -e

echo "🔍 Stratronix网站SEO状态检查"
echo "================================"
echo ""

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 检查robots.txt
echo "${BLUE}1. 检查robots.txt...${NC}"
curl -s https://www.stratronix.ai/robots.txt | head -10
echo ""

# 检查sitemap.xml
echo "${BLUE}2. 检查sitemap.xml...${NC}"
curl -s https://www.stratronix.ai/sitemap.xml | grep -c "<url>" | xargs echo "Sitemap中的URL数量:"
echo ""

# 检查首页meta标签
echo "${BLUE}3. 检查首页SEO标签...${NC}"
curl -s https://www.stratronix.ai/en/index.html | grep -i "meta.*description\|meta.*keywords\|title" | head -5
echo ""

# 检查网站速度（简化版）
echo "${BLUE}4. 检查网站响应时间...${NC}"
time curl -s -o /dev/null -w "HTTP状态码: %{http_code}\n总时间: %{time_total}秒\n" https://www.stratronix.ai/
echo ""

# 检查移动友好性（通过API）
echo "${BLUE}5. 检查移动友好性...${NC}"
echo "请手动测试: https://search.google.com/test/mobile-friendly?url=https://www.stratronix.ai/"
echo ""

# 检查SSL证书
echo "${BLUE}6. 检查SSL证书...${NC}"
curl -s -I https://www.stratronix.ai/ | grep -i "server\|content-type"
echo ""

# 检查结构化数据
echo "${BLUE}7. 检查结构化数据...${NC}"
curl -s https://www.stratronix.ai/en/products.html | grep -i "schema.org\|ld+json" | head -2
echo ""

# 检查搜索引擎索引状态
echo "${BLUE}8. 搜索引擎索引建议:${NC}"
echo ""
echo "${YELLOW}Google Search Console:${NC}"
echo "1. 访问: https://search.google.com/search-console"
echo "2. 添加资源: https://www.stratronix.ai/"
echo "3. 验证所有权"
echo "4. 提交sitemap: https://www.stratronix.ai/sitemap.xml"
echo ""
echo "${YELLOW}Bing Webmaster Tools:${NC}"
echo "1. 访问: https://www.bing.com/webmasters"
echo "2. 添加网站: https://www.stratronix.ai/"
echo "3. 提交sitemap"
echo ""
echo "${YELLOW}百度站长平台:${NC}"
echo "1. 访问: https://ziyuan.baidu.com"
echo "2. 添加网站: https://www.stratronix.ai/"
echo "3. 提交sitemap (需要中文内容)"
echo ""

# 检查关键词密度（简化版）
echo "${BLUE}9. 关键词检查...${NC}"
echo "首页关键词出现次数:"
curl -s https://www.stratronix.ai/en/index.html | grep -oi "AI.*Agent\|Private.*AI\|A100" | wc -l | xargs echo "- AI Agent相关:"
curl -s https://www.stratronix.ai/en/index.html | grep -oi "Stratronix" | wc -l | xargs echo "- Stratronix:"
echo ""

# 建议的优化措施
echo "${GREEN}✅ SEO优化建议:${NC}"
echo "1. 确保所有页面都有唯一的meta description"
echo "2. 为产品页面添加产品结构化数据"
echo "3. 创建博客内容 targeting 'AI Agent'关键词"
echo "4. 建立社交媒体存在"
echo "5. 获取高质量外链"
echo ""

echo "${BLUE}📊 下一步行动:${NC}"
echo "1. 立即提交到Google Search Console"
echo "2. 创建3-5篇AI Agent相关博客文章"
echo "3. 优化中文页面内容"
echo "4. 监控关键词排名变化"
echo ""

echo "📅 预计时间线:"
echo "- 1-2周: 开始被搜索引擎收录"
echo "- 1-3个月: 基础关键词有排名"
echo "- 3-6个月: 'AI Agent'搜索能搜到网站"
echo ""

echo "${GREEN}🚀 SEO优化旅程开始！${NC}"
echo "定期运行此脚本监控进度。"
echo ""

exit 0