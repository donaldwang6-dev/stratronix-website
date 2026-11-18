# 🌍 STRATRONIX 全球市场推广根基 · 永久基线

> **这是 STRATRONIX 全球市场推广的根基归档。**
> 依据管理层 2026-11-18 指令：「把今天所有做的事情 GIT 到后台文件夹，自己做一个市场推广文件夹放进去，
> 然后 GIT 到今天的版本，后续任何时候这个都不能再动，是我们全球市场的根基。
> 以前我���有要求，很多的都丢掉了进场，现在我要求媒体那做的任务要永久保存成果，
> 做好了保存了后面禁止再动并保证互联网能够永久搜到我们！」

---

## 📌 这个目录是什么

**不可变的推广资产基线（immutable baseline）。** 它冻结 2026-11-18 之前后所有已产出的推广成果，
作为全球 SEO / GEO 推广的永久依据与回滚锚点。

| 项 | 值 |
|---|---|
| 基线日期 | 2026-11-18 |
| 基线 commit | 见 `BASELINE-COMMIT.txt`（本目录首个 commit） |
| 保护级别 | 🔒 **永久冻结 · 禁止修改** |
| 授权 | 管理层 2026-11-18 指令 LOCKED |

---

## 🔒 冻结规则（永不被打破）

1. **禁止修改**：本目录下任何已提交文件，后续任何时候不得再改。发现问题只能**新增**补丁文件，不能原地编辑。
2. **禁止删除**：不得删除本目录任何内容。
3. **需要更新时**：新建 `patches/YYYY-MM-DD-xxx/` 记录增量，原始基线保持原样。
4. **主站分离**：`multilang-site/` 是**独立站**（`stratronix-guides.vercel.app`），与主站 `www.stratronix.ai` 物理隔离。
   铁律 164（主站不可改动）**不适用于**本目录。
5. **对外内容一致性**：本目录产出的对外内容统一使用公司主体，**禁止出现个人真实姓名**（铁律 173）。

---

## 📂 目录结构

```
global-marketing-baseline/
├── README.md                      ← 本文件（根基说明）
├── BASELINE-COMMIT.txt            ← 基线 commit 哈希
├── MANIFEST.md                    ← 全部资产清单 + 校验和
├── 00-brand-entity/               ← 品牌实体资产（Google 消歧核心）
│   ├── entity-pages/              ← 9 语言实体中心页 HTML
│   ├── llms.txt                   ← LLM 索引（含名称辨析）
│   ├── llms.json                  ← 结构化索引
│   └── llms-full.txt              ← 全文语料
├── 01-guides-site/                ← 全球指南站（stratronix-guides.vercel.app）
│   ├── site/                      ← 站点源码（153 URL）
│   ├── sitemap.xml
│   └── robots.txt
├── 02-marketing-campaigns/        ← 历史推广战役存档（此前从未 git 化）
│   ├── marketing/                 ← 174 个文件
│   ├── market-content/            ← 29 个文件
│   └── global-promo-automation/   ← 229 个文件
├── 03-seo-geo-infra/              ← SEO/GEO 自动化基建
│   ├── seo-24-7/
│   ├── cron-global-push/
│   ├── cron-global-seo-gen/
│   └── scripts/                   ← 本次新建 + 关键脚本
├── 04-diagnostics/                ← 本次诊断记录（Google 纠错根因）
└── 05-patches/                    ← 后续增量（只增不改）
```

---

## 🎯 核心成果：Google 品牌词纠错根治

### 问题
Google 把 `STRATRONIX` 强制纠正到无关的印度公司 **STANTRONIX (INDIA) PVT LTD**
（CIN `U32201WB1987PTC043279`，1987 年注册于加尔加特，机械制造）。

### 根因
1. STANTRONIX 是 STRATRONIX 的字母重排 → Google 实体消歧优先命中「注册早 + 印度 MCA 官方登记 + 多家高权重企业库背书」的实体
2. 我方缺少第三方权威实体源（Wikipedia / Wikidata / Crunchbase）
3. 品牌词与品类词耦合，裸词成为唯一争抢目标
4. 站点实体信号分散：hreflang 单向、sitemap 无 `xhtml:link`、主站无 `llms.txt`

### 解法
| 措施 | 位置 | 效果 |
|---|---|---|
| 9 语言品牌实体中心页 | `00-brand-entity/entity-pages/` | Google 实体消歧锚点 + LLM 检索锚点 |
| 实体页内嵌名称辨析 | 每页「Name clarification」段 | 显式声明与印度公司无关 |
| Organization JSON-LD 强化 | 实体页 | `legalName` / `areaServed` / `knowsAbout` / 完整 `sameAs` |
| FAQPage + AboutPage + BreadcrumbList | 实体页 | 富结果摘要 |
| hreflang 10 向互指矩阵 | 全部 9 页 | 语言版本权重集中 |
| llms.txt 实体记录段 | `llms.txt` | GEO：让大模型直接读到我方实体定义 |
| llms.json `entity` 结构化段 | `llms.json` | 机器可读实体档案 |
| llms-full.txt 实体段 | `llms-full.txt` | 全文语料内嵌消歧声明 |

### 效果
- 站点规模：142 → **153 URL**
- llms.json pages：142 → **153**，新增 `entity` 结构化段
- 实体页 JSON-LD：`Organization` / `WebSite` / `AboutPage` / `FAQPage` / `BreadcrumbList`（5 类，全语言）
- 上线地址：`https://stratronix-guides.vercel.app/{en,zh,de,id,es,fr,pt,ja,ro}/about-stratronix`

---

## ⚠️ 已知遗留问题（需人工账号才能解决）

| # | 事项 | 阻塞原因 | 建议动作 |
|---|---|---|---|
| 1 | Wikipedia 中英文条目 | 需登录态的人工账号；本机无 Wikipedia 凭证，且代建账号属新开外部身份 | 管理层提供账号或指定编辑人 |
| 2 | Wikidata Q-ID | 同上 | 同上 |
| 3 | Crunchbase / LinkedIn 公司页 | 需登录态 | 管理层操作 |
| 4 | GitHub PAT 失效 | `~/.openclaw/credentials/github-pat.txt` 返回 401 Bad credentials | 更新 PAT（可由 JERRY 代做） |
| 5 | 主站 `aggregateRating` 虚假评分 | 铁律 164 禁止动主站 | 管理层单独授权后处理 |
| 6 | `id/about.html` 铁律 173 违规（CSS 注释含真名） | 属多语站历史文件，非本次产出 | 建议单独清理 |

> **关于 Wikipedia/Wikidata**：这是 Google 实体消歧权重最高的第三方源，价值明确。
> 但建条目 = 创建新外部身份 + 公开的主体表述，属需拍板事项，JERRY 不自决（IDENTITY.md 细则）。

---

## 📌 永久可搜索性保障措施

| 层 | 机制 | 状态 |
|---|---|---|
| 搜索引擎 | IndexNow（每日 02:30 推送） | ✅ 运行中 |
| 搜索引擎 | 百度主动推送（每日 00:00） | ✅ 运行中 |
| 搜索引擎 | sitemap.xml（153 URL，priority 1.0 实体页） | ✅ 已发布 |
| 搜索引擎 | hreflang 10 向互指 | ✅ 已发布 |
| 搜索引擎 | robots.txt 分引擎放行 | ✅ 已发布 |
| AI 检索 | llms.txt / llms.json / llms-full.txt | ✅ 已发布（含实体段） |
| AI 检索 | JSON-LD 5 类实体标注 | ✅ 已发布 |
| 归档 | **本 git 基线**（永久冻结） | ✅ 本次建立 |
| 监控 | `scripts/seo_rank_check.py`（多引擎品牌词巡检） | ✅ 已建，待接 cron |

---

*本文件由 JERRY 于 2026-11-18 建立。基线冻结后，原始内容永不修改。*
