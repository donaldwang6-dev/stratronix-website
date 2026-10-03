#!/bin/bash
echo "=== 同步英文修改到中文版本 ==="
echo "开始时间: $(date)"
echo ""

# 1. 同步About页面修改
echo "1. 同步About页面修改..."
echo "----------------------------------------"

# 检查中文About页面是否有Our Mission部分
if grep -q "Our Mission" zh/about.html; then
    echo "✓ 中文About页面已有Our Mission部分"
else
    echo "⚠ 中文About页面可能需要更新Our Mission部分"
fi

# 检查The Stratum Philosophy是否已改为Our Philosophy
if grep -q "The Stratum Philosophy" zh/about.html; then
    echo "⚠ 中文About页面需要将'The Stratum Philosophy'改为'我们的哲学'"
    # 这里需要实际修改
fi

# 检查Category Strategy文字颜色
if grep -q "color: #5f6368 !important" zh/about.html; then
    echo "✓ 中文About页面已有正确的文字颜色"
else
    echo "⚠ 中文About页面可能需要更新文字颜色"
fi

echo ""

# 2. 同步Home页面修改
echo "2. 同步Home页面修改..."
echo "----------------------------------------"

# 检查Core Values副标题
if grep -q "Focused on AI Agents" zh/index.html; then
    echo "✓ 中文Home页面已有'Focused on AI Agents'"
else
    echo "⚠ 中文Home页面需要更新Core Values副标题"
fi

# 检查Featured Performance标题颜色
if grep -q "color: #1a73e8 !important" zh/index.html; then
    echo "✓ 中文Home页面已有蓝色标题"
else
    echo "⚠ 中文Home页面需要将Featured Performance标题改为蓝色"
fi

echo ""

# 3. 同步Products页面修改
echo "3. 同步Products页面修改..."
echo "----------------------------------------"

# 检查规格修改
if grep -q "Linux" zh/products.html && grep -q "Octa-core ARM Cortex" zh/products.html; then
    echo "✓ 中文Products页面已有Linux和ARM Cortex规格"
else
    echo "⚠ 中文Products页面需要更新规格"
fi

if grep -q "2 Years" zh/products.html; then
    echo "✓ 中文Products页面已有2年保修"
else
    echo "⚠ 中文Products页面需要将保修改为2年"
fi

echo ""
echo "=== 同步完成 ==="
echo "建议手动检查以下页面:"
echo "1. 中文About页面: zh/about.html"
echo "2. 中文Home页面: zh/index.html"
echo "3. 中文Products页面: zh/products.html"
echo ""
echo "需要同步的修改包括:"
echo "1. About页面文字颜色和可见性修复"
echo "2. Home页面副标题和标题颜色修改"
echo "3. Products页面规格更新"
echo "4. 所有设计一致性修改"