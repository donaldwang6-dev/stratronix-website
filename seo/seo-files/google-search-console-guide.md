# Google Search Console 提交指南

## 步骤1: 访问Google Search Console
- 网址: https://search.google.com/search-console
- 使用你的Google账号登录

## 步骤2: 添加网站资源
1. 点击左上角的"添加资源"按钮
2. 选择"网址前缀"方式
3. 输入: `https://www.stratronix.ai/`
4. 点击"继续"

## 步骤3: 验证所有权
### 方法A: HTML标签验证（推荐）
1. 选择"HTML标签"验证方法
2. 复制提供的meta标签代码，例如:
   ```html
   <meta name="google-site-verification" content="abc123def456ghi789" />
   ```
3. 将此标签添加到网站首页的`<head>`部分
4. 回到Search Console点击"验证"

### 方法B: HTML文件上传
1. 选择"HTML文件"验证方法
2. 下载提供的HTML文件
3. 上传到网站根目录: `/verification-files/google-verification.html`
4. 确保可以通过 https://www.stratronix.ai/verification-files/google-verification.html 访问
5. 点击"验证"

## 步骤4: 提交Sitemap
1. 验证成功后，点击左侧菜单的"Sitemaps"
2. 在"添加新的Sitemap"框中输入: `https://www.stratronix.ai/sitemap.xml`
3. 点击"提交"

## 步骤5: 请求索引
1. 点击左侧菜单的"网址检查"
2. 输入首页URL: `https://www.stratronix.ai/`
3. 点击"请求编入索引"

## 重要设置
1. **目标国家/地区**: 设置为"中国"或"全球"
2. **增强功能**: 启用所有可用的增强功能
3. **安全与手动操作**: 定期检查是否有安全问题

## 监控指标
- 索引覆盖率
- 搜索性能
- 移动设备适合性
- 核心网页指标
