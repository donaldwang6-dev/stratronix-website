#!/bin/bash

# Stratronix / 鼎图 双语网站部署脚本
# 使用方法：./deploy.sh [选项]

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 函数：打印带颜色的消息
print_message() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 函数：检查命令是否存在
check_command() {
    if ! command -v $1 &> /dev/null; then
        print_error "命令 '$1' 未找到，请先安装"
        exit 1
    fi
}

# 函数：启动本地服务器
start_local_server() {
    print_message "启动本地服务器..."
    
    # 检查Python3
    if command -v python3 &> /dev/null; then
        print_message "使用Python3启动服务器..."
        python3 -m http.server 8000 &
        SERVER_PID=$!
        print_success "本地服务器已启动：http://localhost:8000"
        print_message "按 Ctrl+C 停止服务器"
        wait $SERVER_PID
    elif command -v python &> /dev/null; then
        print_message "使用Python启动服务器..."
        python -m SimpleHTTPServer 8000 &
        SERVER_PID=$!
        print_success "本地服务器已启动：http://localhost:8000"
        print_message "按 Ctrl+C 停止服务器"
        wait $SERVER_PID
    else
        print_error "未找到Python，无法启动本地服务器"
        exit 1
    fi
}

# 函数：检查网站文件
check_files() {
    print_message "检查网站文件..."
    
    REQUIRED_FILES=("index.html" "en/index.html" "zh/index.html" "css/style.css" "js/main.js")
    
    for file in "${REQUIRED_FILES[@]}"; do
        if [ -f "$file" ]; then
            print_success "找到文件: $file"
        else
            print_error "缺少文件: $file"
            exit 1
        fi
    done
    
    print_success "所有必需文件都存在"
}

# 函数：显示部署选项
show_deploy_options() {
    echo ""
    echo "======= Stratronix / 鼎图 网站部署选项 ======="
    echo "1. 本地预览"
    echo "2. 部署到GitHub Pages"
    echo "3. 部署到Vercel"
    echo "4. 部署到Netlify"
    echo "5. 检查文件完整性"
    echo "6. 显示后台信息"
    echo "7. 退出"
    echo "=============================================="
    echo ""
    
    read -p "请选择选项 (1-7): " choice
    
    case $choice in
        1)
            check_files
            start_local_server
            ;;
        2)
            deploy_github_pages
            ;;
        3)
            deploy_vercel
            ;;
        4)
            deploy_netlify
            ;;
        5)
            check_files
            ;;
        6)
            show_admin_info
            ;;
        7)
            print_message "退出部署脚本"
            exit 0
            ;;
        *)
            print_error "无效选项"
            show_deploy_options
            ;;
    esac
}

# 函数：部署到GitHub Pages
deploy_github_pages() {
    print_message "部署到GitHub Pages..."
    
    # 检查git
    check_command git
    
    # 检查是否在git仓库中
    if [ ! -d ".git" ]; then
        print_message "初始化Git仓库..."
        git init
        git add .
        git commit -m "初始提交：Stratronix / 鼎图 双语网站"
    fi
    
    print_message "请按照以下步骤操作："
    echo ""
    echo "1. 在GitHub创建新仓库：https://github.com/new"
    echo "2. 设置仓库名为：stratronix-website"
    echo "3. 复制仓库URL"
    echo "4. 添加远程仓库：git remote add origin [仓库URL]"
    echo "5. 推送代码：git push -u origin main"
    echo "6. 进入仓库设置 → Pages"
    echo "7. 选择分支：main，目录：/(root)"
    echo "8. 保存设置，等待部署完成"
    echo ""
    print_success "部署完成后，网站将可通过 https://[用户名].github.io/stratronix-website 访问"
}

# 函数：部署到Vercel
deploy_vercel() {
    print_message "部署到Vercel..."
    
    # 检查是否安装vercel-cli
    if command -v vercel &> /dev/null; then
        print_message "使用Vercel CLI部署..."
        vercel
    else
        print_message "请按照以下步骤操作："
        echo ""
        echo "1. 访问 https://vercel.com"
        echo "2. 使用GitHub账号登录"
        echo "3. 点击'New Project'"
        echo "4. 导入stratronix-website仓库"
        echo "5. 点击'Deploy'"
        echo ""
        print_success "部署完成后，网站将可通过 [项目名].vercel.app 访问"
    fi
}

# 函数：部署到Netlify
deploy_netlify() {
    print_message "部署到Netlify..."
    
    # 检查是否安装netlify-cli
    if command -v netlify &> /dev/null; then
        print_message "使用Netlify CLI部署..."
        netlify deploy --prod
    else
        print_message "请按照以下步骤操作："
        echo ""
        echo "1. 访问 https://app.netlify.com"
        echo "2. 使用GitHub账号登录"
        echo "3. 点击'Add new site' → 'Import an existing project'"
        echo "4. 连接GitHub仓库"
        echo "5. 选择stratronix-website仓库"
        echo "6. 点击'Deploy site'"
        echo ""
        print_success "部署完成后，网站将可通过 [项目名].netlify.app 访问"
    fi
}

# 函数：显示后台信息
show_admin_info() {
    echo ""
    echo "======= 后台管理信息 ======="
    echo ""
    echo "后台登录地址："
    echo "  http://[你的域名]/admin/index.html"
    echo ""
    echo "默认登录凭据："
    echo "  用户名：admin"
    echo "  密码：stratronix2024"
    echo ""
    echo "后台功能："
    echo "  • 用户管理"
    echo "  • 内容编辑"
    echo "  • 数据分析"
    echo "  • 系统设置"
    echo ""
    echo "安全建议："
    echo "  1. 首次登录后立即修改密码"
    echo "  2. 定期备份网站数据"
    echo "  3. 启用HTTPS"
    echo "  4. 限制后台访问IP"
    echo ""
    echo "技术支持："
    echo "  邮箱：support@stratronix.ai"
    echo "  电话：+86 21 1234 5678"
    echo ""
}

# 主函数
main() {
    echo ""
    echo "========================================"
    echo "  Stratronix / 鼎图 双语网站部署脚本"
    echo "========================================"
    echo ""
    
    # 检查当前目录
    if [ ! -f "index.html" ]; then
        print_error "请在网站根目录运行此脚本"
        exit 1
    fi
    
    # 显示选项
    show_deploy_options
}

# 运行主函数
main "$@"