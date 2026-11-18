# 📋 STRATRONIX 全球市场推广基线 · 资产清单（MANIFEST）

> 生成时间：2026-11-18 16:39:55
> 基线目录：`global-marketing-baseline/`
> 文件总数：**479**
> 格式：SHA-256 前 16 位校验和，用于验证基线未被篡改。

## 目录结构与内容

| 分区 | 内容 |
|---|---|
| `00-brand-entity/` | 品牌实体资产：9 语言实体中心页 + llms.txt/json/full |
| `01-guides-site/` | 全球指南站源码（153 URL 站点） |
| `02-marketing-campaigns/` | 历史推广战役存档（此前从未 git 化）+ 独立 repo bundle |
| `03-seo-geo-infra/` | SEO/GEO 自动化基建 + 关键脚本 |
| `04-diagnostics/` | Google 纠错根因诊断记录 + 巡检数据 |
| `05-patches/` | 后续增量区（只增不改） |

## 🔒 完整性校验

```bash
cd global-marketing-baseline
find . -type f ! -name MANIFEST.md ! -name BASELINE-COMMIT.txt | sort | xargs sha256sum
```

任何一项与基线不符 = 基线被改动，**立即上报管理层**（铁律 185 发现修改立刻告知）。

## 文件类型分布

| 扩展名 | 数量 |
|---|---|
| `.html` | 190 |
| `.md` | 162 |
| `.json` | 88 |
| `.py` | 9 |
| `.sh` | 7 |
| `.log` | 7 |
| `.pdf` | 4 |
| `.txt` | 3 |
| `.jpg` | 3 |
| `.xml` | 2 |
| `.png` | 2 |
| `.bundle` | 1 |
| `.csv` | 1 |

## ⚠️ 归档脱敏记录

| 项 | 处理 |
|---|---|
| 百度推送 API token（3 处明文） | ✅ 已替换为环境变量 `$BAIDU_TOKEN`，明文不入库 |
| IndexNow key `b85a1d78-...` | ⬜ 保留 —— 该 key 按设计公开托管于站点供搜索引擎校验，非机密 |
| GitHub / Vercel / 社交平台凭证 | ✅ 未发现于基线内 |

---

*本清单随基线一同冻结。基线提交后，本文件不再修改。*
