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
