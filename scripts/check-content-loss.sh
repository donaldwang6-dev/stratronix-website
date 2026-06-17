#!/usr/bin/env bash
# stratronix-website 防丢围栏检查脚本
# 用途：在 git commit / 部署前自动扫描，禁止以下丢失性 bug：
#   1. en/zh/*.html 引用相对路径 js/... （应该 ../js/...）
#   2. HTML 引用 stratonix.ai 1t 拼写（应该 stratronix.ai 2t）
#   3. HTML 引用不存在的 CSS/JS/IMG 路径
#
# Donald 2026-06-17 "做好了就不能丢" 原则：
#   客户看到的网页不能因为路径错/拼写错而内容丢失。
#   这个脚本是"嵌入在代码里的围栏"。
#
# 用法：
#   ./scripts/check-content-loss.sh           # 检查所有
#   ./scripts/check-content-loss.sh en/ zh/   # 检查指定目录

set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGETS=("$@")
[ ${#TARGETS[@]} -eq 0 ] && TARGETS=(en zh)

cd "$ROOT" || { echo "FAIL: cannot cd to $ROOT"; exit 2; }

errors=0
warnings=0

echo "════════════════════════════════════════════════════"
echo "  STRATRONIX Website 防丢围栏检查"
echo "  目标目录: ${TARGETS[*]}"
echo "  $(date '+%Y-%m-%d %H:%M:%S')"
echo "════════════════════════════════════════════════════"

# ─────────────────────────────────────────────────────
# Check 1: en/zh/*.html 不能引用相对路径 'js/...' 'css/...' 'images/...'
#          （应该用 '../js/...' '../css/...' '../images/...'）
# ─────────────────────────────────────────────────────
echo ""
echo "[Check 1] 错误相对路径 (en/zh/ 内引用裸 js/css/images/...)"
for dir in "${TARGETS[@]}"; do
  # 排除 backup / .bak
  hits=$(grep -rnE '(src|href)="(js|css|images)/' "$dir/" 2>/dev/null \
    | grep -vE '\.(backup|bak)' \
    || true)
  if [ -n "$hits" ]; then
    echo "  ❌ $dir:"
    echo "$hits" | sed 's/^/      /'
    errors=$((errors + 1))
  else
    echo "  ✅ $dir/ 无错误相对路径"
  fi
done

# ─────────────────────────────────────────────────────
# Check 2: 不能有 1t 拼写 stratonix.ai
#          （品牌是 2t 拼写 stratronix.ai）
# ─────────────────────────────────────────────────────
echo ""
echo "[Check 2] 域名拼写 (禁止 1t 'stratonix.ai'，应该是 2t 'stratronix.ai')"
# 只看 href/src/action 属性里的 1t 拼写（不看注释）
for dir in "${TARGETS[@]}"; do
  hits=$(grep -rnE '(href|src|action)="[^"]*stratonix\.ai[^"]*"' "$dir/" 2>/dev/null \
    | grep -vE 'stratronix\.ai' \
    | grep -vE '\.(backup|bak)' \
    || true)
  if [ -n "$hits" ]; then
    echo "  ❌ $dir:"
    echo "$hits" | sed 's/^/      /'
    errors=$((errors + 1))
  else
    echo "  ✅ $dir/ 无 1t 拼写（仅看 HTML attribute）"
  fi
done

# ─────────────────────────────────────────────────────
# Check 3: 所有 HTML 引用 (CSS/JS/IMG) 文件必须存在
#          排除 http(s):// 绝对 URL
# ─────────────────────────────────────────────────────
echo ""
echo "[Check 3] HTML 引用文件存在性"
for dir in "${TARGETS[@]}"; do
  for html in "$dir"/*.html; do
    [ -f "$html" ] || continue
    base=$(dirname "$html")
    # 解析 src/href=" 不含 http 的
    refs=$(grep -oE '(src|href)="\.\./[^"]+' "$html" 2>/dev/null | sed -E 's/^(src|href)="//' || true)
    for ref in $refs; do
      # ../js/.. → js/.. in repo root
      resolved="$ROOT/${ref#../}"
      if [ ! -f "$resolved" ]; then
        echo "  ❌ $html → $ref (NOT FOUND: $resolved)"
        errors=$((errors + 1))
      fi
    done
  done
done
echo "  ✅ Check 3 通过（如上无 ❌）"

# ─────────────────────────────────────────────────────
# Check 4: 12 个客户页面必须存在
# ─────────────────────────────────────────────────────
echo ""
echo "[Check 4] 12 个客户页面存在性"
expected=(
  en/index.html en/about.html en/products.html en/news.html en/contact.html
  zh/index.html zh/about.html zh/products.html zh/news.html zh/contact.html
)
for f in "${expected[@]}"; do
  if [ ! -f "$ROOT/$f" ]; then
    echo "  ❌ MISSING: $f"
    errors=$((errors + 1))
  fi
done
echo "  ✅ Check 4 通过（如上无 ❌，10 客户页 + 2 后台页 = 12）"

# ─────────────────────────────────────────────────────
# Check 5: nav 结构完整性
# ─────────────────────────────────────────────────────
echo ""
echo "[Check 5] nav 结构完整性 (id='navToggle' + id='navMenu' 存在)"
for f in "${expected[@]}"; do
  if [ -f "$ROOT/$f" ]; then
    if ! grep -q 'id="navToggle"' "$f" || ! grep -q 'id="navMenu"' "$f"; then
      echo "  ❌ $f 缺 navToggle/navMenu"
      errors=$((errors + 1))
    fi
  fi
done
echo "  ✅ Check 5 通过（如上无 ❌）"

echo ""
echo "════════════════════════════════════════════════════"
if [ $errors -eq 0 ]; then
  echo "  ✅ 所有检查通过 — 内容防丢围栏 OK"
  echo "════════════════════════════════════════════════════"
  exit 0
else
  echo "  ❌ $errors 个错误 — 内容防丢围栏触发！"
  echo "  Donald 2026-06-17 原则：做好了就不能丢"
  echo "  请修复以上问题后再 commit / 部署"
  echo "════════════════════════════════════════════════════"
  exit 1
fi
