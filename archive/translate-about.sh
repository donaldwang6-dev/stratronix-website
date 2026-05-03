#!/bin/bash
echo "翻译About页面关键内容..."

# 1. 修改语言和标题
sed -i 's/<html lang="en">/<html lang="zh-CN">/' zh/about.html.new
sed -i 's|<title>About Stratronix - The PAA Category Creator</title>|<title>关于Stratronix - PAA类别创造者</title>|' zh/about.html.new

# 2. 翻译导航菜单（与其他页面一致）
sed -i 's|Home|首页|g' zh/about.html.new
sed -i 's|About|关于|g' zh/about.html.new
sed -i 's|Products|产品|g' zh/about.html.new
sed -i 's|News|新闻|g' zh/about.html.new
sed -i 's|Contact|联系|g' zh/about.html.new

# 3. 翻译主要部分标题
sed -i 's|Our Mission|我们的使命|g' zh/about.html.new
sed -i 's|Vision & Strategy|愿景与战略|g' zh/about.html.new
sed -i 's|Industry Shift: AI 2.0 (Agent Era)|行业转变：AI 2.0（代理时代）|g' zh/about.html.new
sed -i 's|Category Strategy|类别战略|g' zh/about.html.new

# 4. 翻译Our Philosophy部分
sed -i 's|Our Philosophy|我们的哲学|g' zh/about.html.new

# 5. 翻译Category Strategy卡片
sed -i 's|Standardize|标准化|g' zh/about.html.new
sed -i 's|Associate|关联|g' zh/about.html.new
sed -i 's|Educate|教育|g' zh/about.html.new
sed -i 's|Ecosystem|生态系统|g' zh/about.html.new

# 6. 翻译页脚（与其他页面一致）
sed -i 's|Quick Links|快速链接|g' zh/about.html.new
sed -i 's|Contact Info|联系信息|g' zh/about.html.new
sed -i 's|Follow Us|关注我们|g' zh/about.html.new

echo "About页面翻译完成"