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
