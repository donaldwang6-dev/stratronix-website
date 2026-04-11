## 📥 PDF文件下载

### 文件列表：

1. **专业版PDF** (1MB) - 完整企业级设计
   - 文件名: a100-specifications-professional.pdf
   - 大小: 1012KB

2. **简洁版PDF** (40KB) - 快速查看版本
   - 文件名: a100-specifications-simple.pdf
   - 大小: 40KB

### 获取方式：

由于当前环境限制，你可以通过以下方式获取文件：

1. **SSH访问**：
   ```bash
   scp root@your-server-ip:/root/.openclaw/workspace/stratronix.com-website/*.pdf .
   ```

2. **HTTP服务**（临时）：
   ```bash
   # 在服务器上运行
   python3 -m http.server 8080
   # 然后访问 http://your-server-ip:8080
   ```

3. **Base64编码**（小文件）：
   ```bash
   base64 a100-specifications-simple.pdf
   ```

### 文件预览：

**专业版包含：**
- 企业品牌头部
- 产品展示区域
- 核心规格网格
- 详细技术规格表
- 应用场景卡片
- 联系信息页脚

**简洁版包含：**
- 所有技术规格
- 简洁表格布局
- 适合打印和快速查看
