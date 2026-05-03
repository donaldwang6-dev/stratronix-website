#!/bin/bash
echo "翻译Products页面关键内容..."

# 1. 修改语言和标题
sed -i 's/<html lang="en">/<html lang="zh-CN">/' zh/products.html.new
sed -i 's|<title>Products - Stratronix PAA Solutions</title>|<title>产品 - Stratronix PAA解决方案</title>|' zh/products.html.new

# 2. 翻译导航菜单（与Home页面一致）
sed -i 's|Home|首页|g' zh/products.html.new
sed -i 's|About|关于|g' zh/products.html.new
sed -i 's|Products|产品|g' zh/products.html.new
sed -i 's|News|新闻|g' zh/products.html.new
sed -i 's|Contact|联系|g' zh/products.html.new

# 3. 翻译主要标题
sed -i 's|Our Product Line|我们的产品线|g' zh/products.html.new
sed -i 's|A100 Private AI-Agent Appliance|A100 私有AI代理设备|g' zh/products.html.new

# 4. 翻译规格标签
sed -i 's|Technical Specifications|技术规格|g' zh/products.html.new
sed -i 's|Engineered for performance and reliability|为性能和可靠性而设计|g' zh/products.html.new
sed -i 's|Stable Server-used System|稳定的服务器级系统|g' zh/products.html.new
sed -i 's|High-efficiency architecture|高效能架构|g' zh/products.html.new
sed -i 's|High-Speed Memory|高速内存|g' zh/products.html.new
sed -i 's|Network Interfaces|网络接口|g' zh/products.html.new
sed -i 's|Uptime Guarantee|运行时间保证|g' zh/products.html.new
sed -i 's|Power Consumption|功耗|g' zh/products.html.new
sed -i 's|Warranty Period|保修期|g' zh/products.html.new

# 5. 翻译Use Cases部分
sed -i 's|Use Cases|应用场景|g' zh/products.html.new
sed -i 's|Transforming industries with autonomous AI agents|用自主AI代理改变行业|g' zh/products.html.new
sed -i 's|Financial Analysis|金融分析|g' zh/products.html.new
sed -i 's|Healthcare Diagnostics|医疗诊断|g' zh/products.html.new
sed -i 's|Industrial Automation|工业自动化|g' zh/products.html.new

# 6. 翻译页脚（与Home页面一致）
sed -i 's|Quick Links|快速链接|g' zh/products.html.new
sed -i 's|Contact Info|联系信息|g' zh/products.html.new
sed -i 's|Follow Us|关注我们|g' zh/products.html.new

echo "Products页面翻译完成"