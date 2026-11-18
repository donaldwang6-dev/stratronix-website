# STRATRONIX OFF-SITE 发布指南 (Day 2 — 2026-07-15)

## 现状
- 22 篇博客/微信文章已备份到 `marketing/legacy-blog-backup/`
- 44 个 OFF-SITE 发布草稿已生成
- 全部 OFF-SITE 平台（不在 stratronix-website-new/）

## 发布清单

### 🇺🇸 英文平台 (Day 2 立即可发)

| 平台 | 帖子数 | 草稿位置 | 状态 |
|------|--------|----------|------|
| **Medium** | 4 | `medium-en/` | ⏳ 待 Donald 登录发布 |
| **Dev.to** | 4 | `devto-en/` | ⏳ 待 Donald 登录发布 |
| **Hashnode** | 4 | `hashnode-en/` | ⏳ 自动发布脚本 |
| **Reddit** | 4 | `reddit-en/` | ⏳ 需 Donald 手动 (反垃圾) |

### 🇨🇳 中文平台 (Day 2 立即可发)

| 平台 | 帖子数 | 草稿位置 | 状态 |
|------|--------|----------|------|
| **Medium 中文版** | 13 | `medium-zh/` | ⏳ 待 Donald 登录发布 |
| **知乎** | 12 | `zhihu-zh/` | ⏳ 自动发布（5 答案 + 7 文章） |
| **V2EX** | 2 | `v2ex-zh/` | ⏳ 待 Donald 手动 |
| **掘金** | 1 | `juejin-zh/` | ⏳ 待 Donald 手动 |
| **微信公众号** | 6 | `marketing/legacy-blog-backup/zh-wechat/` | ⏳ Donald 直接发布原文 |

### 🌐 通用 (跨平台)

- **LinkedIn 文章** — 1 篇主文 + 1 篇副文（已生成在 `day2-content-pack-20260715/linkedin-main-en.md`）

## 建议发布顺序

### Day 2 上午（9:00-12:00）
1. **Reddit r/LocalLLM** — 真实讨论帖（最有可能被 upvote）
2. **Reddit r/SelfHosted** — TCO 对比
3. **Dev.to** — 4 篇技术长文

### Day 2 下午（14:00-18:00）
4. **Medium 英文** — 4 篇文章
5. **Hashnode** — 4 篇文章
6. **知乎** — 5 答案（自动）

### Day 3 (2026-07-16)
7. **微信公众号** — 6 篇原文（Donald 直接发布）
8. **V2EX / 掘金** — 中文深度帖
9. **Medium 中文** — 13 篇文章

## 反垃圾策略

- ✅ Reddit：先回复 5 个相关帖，再发自己帖
- ✅ 知乎：先点赞 10 个同领域答案，再发
- ✅ V2EX：先回帖 3 个，再发主帖
- ✅ LinkedIn：每天最多 1 帖，间隔 4 小时
- ❌ 不批量发布（铁律 zoho-social 禁止）

## 链接策略（铁律 18 v2）

每个 OFF-SITE 帖都包含 1 个链接 → `https://www.stratronix.ai`
- 主页（不要 /blog/、/zh/blog/，已删）
- /products 或 /zh/products

## 自动化

我已经写好了发布脚本（`scripts/post-offsite.sh`），可一键发布：
- Hashnode 自动发布
- Dev.to 自动发布
- 知乎答案自动发布

但**首次发布需 Donald 登录**（反垃圾 + Cookie 验证）

## 估算产出

- 44 个新 OFF-SITE 内容
- 5-10 个高质量反向链接（Reddit / Dev.to / Medium / 知乎）
- SEO 长尾词覆盖：local AI / PAA / private AI appliance / 私有 AI 智能体 / 鼎图太易 等
