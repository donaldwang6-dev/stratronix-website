#!/bin/bash
echo "=== Stratronix网站最终验证 ==="
echo "检查时间: $(date)"
echo ""

echo "1. 检查About页面关键文字颜色..."
echo "----------------------------------------"
echo "检查Our Mission文字颜色..."
grep -n "Our Mission" en/about.html | head -2
echo ""

echo "检查Vision & Strategy文字颜色..."
grep -n "Vision & Strategy" en/about.html
echo ""

echo "检查Category Strategy文字颜色..."
echo "Standardize卡片:"
grep -n "Standardize" en/about.html
echo "Ecosystem卡片:"
grep -n "Ecosystem" en/about.html
echo ""

echo "2. 检查Home页面核心部分..."
echo "----------------------------------------"
echo "检查Core Values副标题..."
grep -n "Focused on AI Agents" en/index.html
echo ""

echo "检查Featured Performance副标题..."
grep -n "Plug and Play AI Server" en/index.html
echo ""

echo "3. 检查蓝色横线是否已移除..."
echo "----------------------------------------"
echo "检查.card-title::after背景..."
grep -n "card-title::after" css/style.css
grep -A2 "card-title::after" css/style.css | grep "background"
echo ""

echo "4. 检查响应式设计..."
echo "----------------------------------------"
echo "检查移动端媒体查询..."
grep -n "max-width: 768px" css/style.css | wc -l
echo "找到 $(grep -n "max-width: 768px" css/style.css | wc -l) 个移动端媒体查询"
echo ""

echo "5. 检查Git状态..."
echo "----------------------------------------"
git status --short
echo ""

echo "=== 验证完成 ==="
echo "建议:"
echo "1. 访问 https://www.stratronix.ai/en/about.html?v=final 验证About页面"
echo "2. 访问 https://www.stratronix.ai/en/index.html?v=final 验证Home页面"
echo "3. 使用不同设备测试响应式设计"
echo "4. 检查所有文字是否清晰可见"