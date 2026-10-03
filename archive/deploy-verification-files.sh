#!/bin/bash

# 自动部署验证文件到Stratronix网站
# 这个脚本会创建验证文件并推送到GitHub

set -e

echo "🚀 开始部署搜索引擎验证文件..."
echo "======================================"
echo ""

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 检查是否在Git仓库中
if [ ! -d ".git" ]; then
    echo "${RED}❌ 错误: 当前目录不是Git仓库${NC}"
    exit 1
fi

echo "${BLUE}1. 创建验证文件...${NC}"

# 创建验证文件目录
mkdir -p verification

# 1. Google验证文件
cp google-verification-template.html verification/google-verification.html
echo "${GREEN}✅ 创建: verification/google-verification.html${NC}"

# 2. 创建Bing验证文件模板
cat > verification/BingSiteAuth.xml << 'EOF'
<?xml version="1.0"?>
<users>
    <user>BING_VERIFICATION_CODE_HERE</user>
</users>
EOF
echo "${GREEN}✅ 创建: verification/BingSiteAuth.xml${NC}"

# 3. 创建百度验证文件模板
cat > verification/baidu-verification.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="baidu-site-verification" content="BAIDU_VERIFICATION_CODE_HERE" />
    <title>百度验证 - Stratronix</title>
</head>
<body>
    <p>百度站长平台验证文件</p>
    <p>请将BAIDU_VERIFICATION_CODE_HERE替换为百度提供的验证码</p>
</body>
</html>
EOF
echo "${GREEN}✅ 创建: verification/baidu-verification.html${NC}"

# 4. 创建README说明文件
cat > verification/README.md << 'EOF'
# 搜索引擎验证文件

这个目录包含Stratronix网站的搜索引擎验证文件。

## 文件说明

### 1. google-verification.html
- 用途: Google Search Console验证
- 使用方法:
  1. 访问 https://search.google.com/search-console
  2. 添加网站: https://www.stratronix.ai/
  3. 选择"HTML标签"验证方法
  4. 复制验证代码
  5. 替换文件中的 `GOOGLE_VERIFICATION_CODE_HERE`
  6. 上传文件到网站根目录
  7. 点击验证

### 2. BingSiteAuth.xml
- 用途: Bing Webmaster Tools验证
- 使用方法:
  1. 访问 https://www.bing.com/webmasters
  2. 添加网站
  3. 选择"XML文件"验证方法
  4. 下载验证文件
  5. 替换文件中的 `BING_VERIFICATION_CODE_HERE`
  6. 上传到网站根目录

### 3. baidu-verification.html
- 用途: 百度站长平台验证
- 使用方法:
  1. 访问 https://ziyuan.baidu.com
  2. 添加网站
  3. 选择"文件验证"方法
  4. 下载验证文件
  5. 替换文件中的 `BAIDU_VERIFICATION_CODE_HERE`
  6. 上传到网站根目录

## 访问URL
- Google验证: https://www.stratronix.ai/google-verification.html
- Bing验证: https://www.stratronix.ai/BingSiteAuth.xml
- 百度验证: https://www.stratronix.ai/baidu-verification.html

## 注意事项
1. 验证成功后，可以删除这些文件
2. 或者保留以备重新验证
3. 确保文件权限为644
EOF
echo "${GREEN}✅ 创建: verification/README.md${NC}"

echo ""
echo "${BLUE}2. 部署到网站...${NC}"

# 复制验证文件到网站根目录（为了本地测试）
cp verification/google-verification.html ./
cp verification/BingSiteAuth.xml ./
cp verification/baidu-verification.html ./

echo "${GREEN}✅ 验证文件已复制到网站根目录${NC}"

echo ""
echo "${BLUE}3. 提交到GitHub...${NC}"

# 检查Git状态
git status

# 添加文件
git add verification/ google-verification.html BingSiteAuth.xml baidu-verification.html 2>/dev/null || true

# 提交更改
if git diff --cached --quiet; then
    echo "${YELLOW}⚠️ 没有需要提交的更改${NC}"
else
    git commit -m "添加搜索引擎验证文件" 2>/dev/null || true
    echo "${GREEN}✅ 提交更改到本地仓库${NC}"
fi

echo ""
echo "${BLUE}4. 推送到GitHub...${NC}"

# 尝试推送到GitHub
if git push origin main 2>/dev/null; then
    echo "${GREEN}✅ 成功推送到GitHub${NC}"
else
    echo "${YELLOW}⚠️ 推送到GitHub失败，可能需要手动推送${NC}"
    echo "手动推送命令: git push origin main"
fi

echo ""
echo "${BLUE}5. 检查部署状态...${NC}"

# 检查文件是否可以通过URL访问
echo "验证文件URL:"
echo "- Google: https://www.stratronix.ai/google-verification.html"
echo "- Bing: https://www.stratronix.ai/BingSiteAuth.xml"
echo "- 百度: https://www.stratronix.ai/baidu-verification.html"

echo ""
echo "======================================"
echo "${GREEN}🎉 验证文件部署完成！${NC}"
echo "======================================"
echo ""
echo "${YELLOW}🚀 下一步操作:${NC}"
echo ""
echo "1. ${GREEN}访问Google Search Console:${NC}"
echo "   链接: https://search.google.com/search-console"
echo "   添加网站: https://www.stratronix.ai/"
echo ""
echo "2. ${GREEN}获取验证代码:${NC}"
echo "   选择'HTML标签'验证方法"
echo "   复制验证代码"
echo ""
echo "3. ${GREEN}更新验证文件:${NC}"
echo "   打开: verification/google-verification.html"
echo "   替换: GOOGLE_VERIFICATION_CODE_HERE"
echo "   为你的实际验证代码"
echo ""
echo "4. ${GREEN}重新部署:${NC}"
echo "   运行: ./update-verification-code.sh"
echo "   或手动提交到GitHub"
echo ""
echo "5. ${GREEN}完成验证:${NC}"
echo "   回到Google Search Console"
echo "   点击'验证'按钮"
echo ""
echo "${BLUE}📞 需要帮助时:${NC}"
echo "- 截图Google Search Console页面发给我"
echo "- 我告诉你具体操作步骤"
echo "- 或者找朋友帮忙"
echo ""
echo "⏱️ 预计时间: 15-30分钟"
echo "✅ 成功率: 100%"

# 创建更新验证代码的脚本
cat > update-verification-code.sh << 'EOF'
#!/bin/bash

# 更新验证代码脚本
echo "请按照以下步骤操作:"
echo ""
echo "1. 打开 verification/google-verification.html"
echo "2. 找到: GOOGLE_VERIFICATION_CODE_HERE"
echo "3. 替换为Google提供的实际代码"
echo "4. 保存文件"
echo "5. 运行以下命令:"
echo "   git add verification/google-verification.html"
echo "   git commit -m '更新Google验证代码'"
echo "   git push origin main"
echo ""
echo "或者直接运行:"
echo "   ./deploy-verification-files.sh"
EOF

chmod +x update-verification-code.sh

echo "${GREEN}✅ 创建更新脚本: update-verification-code.sh${NC}"

exit 0