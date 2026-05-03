#!/bin/bash
echo "翻译Home页面关键内容..."

# 1. 修改语言和标题
sed -i 's/<html lang="en">/<html lang="zh-CN">/' zh/index.html.new
sed -i 's|<title>Stratronix - Private AI-Agent Appliance</title>|<title>Stratronix - 私有AI代理设备</title>|' zh/index.html.new

# 2. 翻译导航菜单
sed -i 's|Home|首页|g' zh/index.html.new
sed -i 's|About|关于|g' zh/index.html.new
sed -i 's|Products|产品|g' zh/index.html.new
sed -i 's|News|新闻|g' zh/index.html.new
sed -i 's|Contact|联系|g' zh/index.html.new

# 3. 翻译主要标题
sed -i 's|Think Big, Compute Small|大处着眼，小处着手|g' zh/index.html.new
sed -i 's|Start Your PAA Transformation Journey|开启您的PAA转型之旅|g' zh/index.html.new

# 4. 翻译Core Values部分
sed -i 's|Our Core Values|我们的核心价值|g' zh/index.html.new
sed -i 's|Innovation Driven|创新驱动|g' zh/index.html.new
sed -i 's|Reliable & Stable|可靠稳定|g' zh/index.html.new
sed -i 's|Customer Centric|客户至上|g' zh/index.html.new
sed -i 's|Focused on AI Agents|专注于AI代理|g' zh/index.html.new
sed -i 's|Enterprise-Grade Quality|企业级质量|g' zh/index.html.new
sed -i 's|Personalized Solutions|个性化解决方案|g' zh/index.html.new

# 5. 翻译Featured Performance部分
sed -i 's|Featured Performance|特色性能|g' zh/index.html.new
sed -i 's|OpenClaw Pre-installed|预装OpenClaw|g' zh/index.html.new
sed -i 's|Private AI Assistant|私有AI助手|g' zh/index.html.new
sed -i 's|Private Cloud Platform|私有云平台|g' zh/index.html.new

# 6. 翻译页脚
sed -i 's|Quick Links|快速链接|g' zh/index.html.new
sed -i 's|Contact Info|联系信息|g' zh/index.html.new
sed -i 's|Follow Us|关注我们|g' zh/index.html.new
sed -i 's|Request Demo|申请演示|g' zh/index.html.new
sed -i 's|Consult Solutions|咨询方案|g' zh/index.html.new

echo "Home页面翻译完成"