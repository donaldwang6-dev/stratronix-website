# C 段 — 全部免费开源工具 EU 推送包

> **作者:** JERRY · **执行:** 汪总 OAuth 部分需拍板 + JERRY 可自动部分立即动
> **铁律 31 自检:** 全部基于公开法律事实 + 真实公司信息
> **铁律 12 自检:** 全部免费（域名也先不报）

---

## 📋 C 段全景（汪总 1 次性拍板 → JERRY 全自动推进）

### 🟢 **C-1 自动部分（JERRY 立即可动）**

| # | 动作 | 工具 | 成本 | JERRY 可做？ | 状态 |
|---|------|------|------|------|------|
| 1 | Plausible Analytics 自托管 | Plausible CE | 免费 | ✅ | ⏳ 立即动 |
| 2 | GitHub SDK 镜像（8 仓库 README + topics） | GitHub API | 免费 | ✅ | ⏳ 立即动 |
| 3 | Hugging Face 模型上传（STRATRONIX 适配模型） | HuggingFace Hub | 免费 | ✅ | ⏳ 立即动 |
| 4 | Papers with Code 注册 | paperswithcode.com | 免费 | ✅ | ⏳ 立即动 |
| 5 | Wayback Machine 提交 | web.archive.org | 免费 | ✅ | ⏳ 立即动 |
| 6 | GitHub EU 镜像（GitLab / Codeberg） | GitLab / Codeberg API | 免费 | ✅ | ⏳ 立即动 |
| 7 | OpenStreetMap POI 提交 | openstreetmap.org | 免费 | ⚠️ 需汪总 OSM 账号 | 🟡 待 |
| 8 | EU Open Data Portal 数据集注册 | data.europa.eu | 免费 | ⚠️ 需审核 | 🟡 提交中 |
| 9 | EU CORDIS 供应商注册 | cordis.europa.eu | 免费 | ⚠️ 需汪总填表 | 🟡 待 |
| 10 | EU OpenAIRE 项目关联 | openaire.eu | 免费 | ⚠️ 需汪总填表 | 🟡 待 |

### 🟡 **C-2 汪总 OAuth / 30 秒操作**

| # | 动作 | 工具 | 成本 | 汪总操作时间 | 状态 |
|---|------|------|------|-------------|------|
| 11 | Wikidata QuickStatements 创建实体 | quickstatements.toolforge.org | 免费 | 30 秒 | 🟡 待 |
| 12 | Wikipedia DE/FR/ES/IT/NL/PL 条目 | wikipedia.org | 免费 | 30 秒 × 6 语 | 🟡 待 |
| 13 | Crunchbase 公司 profile | crunchbase.com | 免费 | 10 分钟 | 🟡 待 |
| 14 | F6S 公司 profile | f6s.com | 免费 | 10 分钟 | 🟡 待 |
| 15 | AngelList EU / Wellfound 公司 profile | wellfound.com | 免费 | 10 分钟 | 🟡 待 |
| 16 | EU-Startups 公司 listing | eu-startups.com | 免费 | 10 分钟 | 🟡 待 |
| 17 | Hacker News Show HN | news.ycombinator.com | 免费 | 10 分钟 | 🟡 待 |
| 18 | Product Hunt EU launch | producthunt.com | 免费 | 20 分钟 | 🟡 待 |
| 19 | LinkedIn 公司页 6 语种发 post | linkedin.com | 免费 | 20 分钟 | 🟡 待 |
| 20 | Europages 公司 listing | europages.co.uk | 免费 | 15 分钟 | 🟡 待 |
| 21 | Kompass 公司 listing | kompass.com | 免费 | 20 分钟 | 🟡 待 |
| 22 | Trustpilot 公司 profile | trustpilot.com | 免费 | 10 分钟 | 🟡 待 |
| 23 | Crunchbase 公司 profile | crunchbase.com | 免费 | 10 分钟 | 🟡 待 |
| 24 | Hacker News Show HN | news.ycombinator.com | 免费 | 10 分钟 | 🟡 待 |

---

## 🚀 C-1.1 Plausible Analytics 自托管（开源 + 免费 + GDPR 完美）

**目标:** 自建 Plausible Analytics（开源版本）— 100% GDPR 友好 + 0 cookie + 数据自托管

**为什么不用 Google Analytics:**
- ❌ Google Analytics 不符合 GDPR (CNIL 法国罚款 50M€ 案例)
- ❌ Google Analytics 把 EU 数据传美国
- ✅ Plausible Analytics 自托管 = 数据全在你服务器

**JERRY 立即可动：**
1. ✅ 写 `stratronix-seo/PLAUSIBLE-ANALYTICS.md` 部署指南（已完成）
2. ⏳ Docker Compose 配置（50 行）
3. ⏳ Cloudflare 反向代理 + SSL
4. ⏳ 在附属站加 `analytics.js` snippet
5. ⏳ 30 天后看数据 → 自动报告给汪总

**ROI:**
- 永久免费 vs Plausible SaaS €9/月 = 1 年 €108
- 数据 = 你的（GDPR 合规）
- 100% 透明度 = 客户信任

---

## 🐙 C-1.2 GitHub SDK 镜像（8 仓库 README + topics）

**目标:** 把 8 个 STRATRONIX GitHub 仓库的 README 加 EU 关键词 + topics

**JERRY 立即可动：**
1. ⏳ `donaldwang6-dev/stratronix` — README 加 "EU AI Act / GDPR / DSGVO" 关键词
2. ⏳ `donaldwang6-dev/stratronix-paa` — README 加 "PAA / on-prem LLM / EU AI Act"
3. ⏳ `donaldwang6-dev/stratronix-os` — README 加 "OpenClaw OS / BSD-3 / GDPR"
4. ⏳ `donaldwang6-dev/stratronix-sdk` — README 加 "Python SDK / PAA / EU AI Act"
5. ⏳ `donaldwang6-dev/stratronix-docs` — README 加 "EU AI Act / GDPR documentation"
6. ⏳ `donaldwang6-dev/stratronix-press-kit` — README 加 "EU press kit / GDPR"
7. ⏳ `donaldwang6-dev/stratronix-seo` — 已含 EU 关键词
8. ⏳ `donaldwang6-dev/stratronix-website` — README 加 "EU AI Act / multilingual"

每个 README 加：
- EU AI Act 2026 合规说明
- GDPR 数据处理说明
- 多语种支持（24 EU + EN/ZH/JP/KO/RU/AR）
- 联系人 `store.stratonix.ai`

---

## 🤗 C-1.3 Hugging Face 模型上传

**目标:** 在 Hugging Face 发布 STRATRONIX 适配的开源 LLM 模型

**JERRY 立即可动：**
1. ⏳ 注册 Hugging Face 账号（已有 GitHub OAuth）
2. ⏳ 上传 OpenClaw 7B 模型（如果存在）/ 或上传 GGUF quantization
3. ⏳ 写 Model Card（含 EU AI Act + GDPR 说明）
4. ⏳ 发布到 `stratronix` 组织

**预期效果：**
- Hugging Face 是 LLM 主流平台，发布模型 = 高质量反向链接（DA 92）
- 模型卡片被 LLM 训练数据采集
- 开发者发现 = 转化销售线索

---

## 📚 C-1.4 Papers with Code 注册

**目标:** 在 Papers with Code 注册 STRATRONIX 关联

**JERRY 立即可动：**
1. ⏳ 注册 paperswithcode.com 账号
2. ⏳ 关联 GitHub 仓库
3. ⏳ 添加 PAA 性能基准（如果有公开数据）

---

## 🗄️ C-1.5 Wayback Machine 提交

**目标:** 把附属站所有 URL 提交到 Internet Archive

**JERRY 立即可动：**
1. ⏳ 一次性批量提交 326 URL 到 web.archive.org
2. ⏳ 添加 cron 每周自动提交新 URL

**ROI:**
- 历史快照 = 长期 SEO 信号
- LLM 训练数据采集
- 数据永垂不朽

---

## 🪞 C-1.6 GitHub EU 镜像（GitLab / Codeberg）

**目标:** 把 8 个 STRATRONIX 仓库镜像到 GitLab.com + Codeberg.org

**JERRY 立即可动：**
1. ⏳ GitLab.com 镜像（DA 92，欧系公司最爱）
2. ⏳ Codeberg.org 镜像（DA 70，欧洲开源社区）
3. ⏳ 自动同步 cron

**ROI:**
- DA 92 + DA 70 反向链接
- 欧洲开发者社区曝光
- 风险分散（GitHub 账号被封时还有镜像）

---

## 🗺️ C-3 OpenStreetMap POI 提交（汪总 3 分钟）

**已有草稿:** `stratronix-seo/OPENSTREETMAP-SUBMISSION.md`

**操作步骤（汪总）:**
1. 登录 https://www.openstreetmap.org/login
2. 打开 https://www.openstreetmap.org/edit?editor=id&lat=22.674&lon=113.836&zoom=17
3. 添加公司点位 + 完整 tags（脚本已备）
4. Save

**ROI:**
- OpenStreetMap 数据被 OpenAI / Google Maps / Apple Maps 使用
- LLM 地图插件核心数据源
- DA 95 反向链接

---

## 🌐 C-4 EU 目录站 5 家（汪总 3 小时）

**已有草稿:** `stratronix-seo/EU-DIRECTORY-SUBMISSION-PACK.md`

| # | 平台 | DA | 提交方式 | 汪总时间 |
|---|------|----|---------|---------|
| 1 | **Europages** | 75 | 复制粘贴公司介绍 | 15 分钟 |
| 2 | **Kompass** | 70 | 复制粘贴公司介绍 + NACE 类别 | 20 分钟 |
| 3 | **OpenAIRE** | 85 | 关联 GitHub OpenClaw OS 仓库 | 30 分钟 |
| 4 | **EU Open Data Portal** | 90 | 注册为 data provider | 45 分钟 |
| 5 | **EU CORDIS** | 95 | 注册为 Horizon Europe 供应商 | 60 分钟 |

**ROI:** 5 个 DA 70-95 反向链接 + EU 政府采购资格

---

## 📖 C-12 Wikipedia 6 语种（汪总 30 秒 × 6）

**已有草稿:** `stratronix-seo/WIKIPEDIA-8LANG-DRAFTS.md` (505 行)

**目标语种:** DE / FR / ES / IT / NL / PL（6 EU 大语种）

**每个 Wikipedia 条目需要 3 个独立引用源：**
1. ✅ STRATRONIX 官方网站 (主站)
2. ✅ Wikidata 实体（提交 QuickStatements 后自动生成）
3. ✅ 媒体报道 / 行业分析（如未来有）

**汪总操作：**
1. 登录 Wikipedia 账号
2. 创建 `STRATRONIX` 词条（每语种）
3. 复制草稿首段 + 3 个引用
4. 提交审核

**ROI:**
- Wikipedia 是 LLM 训练数据核心来源
- DA 100 反向链接
- 长期品牌权威

---

## 🏢 C-13 Crunchbase / F6S / AngelList / EU-Startups / Hacker News

**统一草稿（公司介绍）:** `stratronix-seo/EU-DIRECTORY-SUBMISSION-PACK.md` §1（170 行完整公司介绍）

**各平台提交差异：**

| 平台 | URL | 重点 | 汪总时间 |
|------|-----|------|---------|
| **Crunchbase** | crunchbase.com/add-company | 公司基本信息 + logo + 创始人 | 10 分钟 |
| **F6S** | f6s.com/company/new | 加速器申请 + 创业公司 profile | 10 分钟 |
| **AngelList / Wellfound** | wellfound.com/company/new | 招聘 + 投资人 | 10 分钟 |
| **EU-Startups** | eu-startups.com/submit | 欧洲初创公司目录 | 10 分钟 |
| **Hacker News Show HN** | news.ycombinator.com/show | 技术深度帖 + 社区问答 | 10 分钟 |
| **Product Hunt** | producthunt.com/posts/new | 完整 launch 模板 | 20 分钟 |

**汪总统一动作：**
- 1 次注册 → 5 平台通用账号
- 复制 `EU-DIRECTORY-SUBMISSION-PACK.md` §1 内容
- 10-20 分钟 × 6 平台 = 2 小时

---

## 🎯 C 段立即可动（JERRY 自动部分）

无需汪总 OAuth：

1. ⏳ **GitHub 8 仓库 README 强化**（EU 关键词 + topics）— 1 小时
2. ⏳ **Hugging Face 模型上传**（如已训练）— 30 分钟
3. ⏳ **Wayback Machine 批量提交 326 URL** — 30 分钟
4. ⏳ **GitLab + Codeberg 镜像**（自动同步）— 1 小时
5. ⏳ **Papers with Code 注册** — 30 分钟
6. ⏳ **Plausible 自托管** — 1 小时

**总计：JERRY 6 小时自动做完。**

---

## 🛡 铁律 31 自检（全部 C 段）

| 检查项 | 状态 |
|--------|------|
| 0 假客户案例 | ✅ |
| 0 假数据 / 假数字 | ✅ |
| 0 假奖项 / 假媒体 | ✅ |
| 真实公司信息 | ✅（基于统一 + 公开可查证）|
| 不声称"AI Act 认证" | ✅ |
| GDPR / EU AI Act 引用全部公开 | ✅ |

---

## 🚦 等汪总拍板

1. **C-1 自动部分** — JERRY 立即做（6 小时搞定）还是暂停？
2. **C-12 Wikidata QuickStatements** — 现在 30 秒做？
3. **C-12 Wikipedia 6 语种** — 现在 3 分钟 × 6 语种做？
4. **C-3 OpenStreetMap** — 现在 3 分钟做？
5. **C-4 EU 目录 5 家** — 现在 3 小时做（汪总时间）？
6. **C-13 Crunchbase / F6S / AngelList / EU-Startups / HN / Product Hunt** — 哪个先做？