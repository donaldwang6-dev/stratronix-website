# 跨源数据冲突核查 —— Google 实体权威度风险

**核查日期**：2026-11-18 ｜ **执行人**：JERRY ｜ **方式**：只读取证，未做任何修改

## 一、结论

Google 会同时抓取官网 / GitHub / 第三方展会页。**公开 GitHub 仓库里的价格与规格与线上主站不一致**，
这些冲突信号会削弱 STRATRONIX 实体权威度，直接影响「一搜就出全部信息」的目标。

## 二、口径对照（实测）

| 数据源 | 价格 | 规格/描述 | 与主站一致 |
|---|---|---|---|
| **主站线上** `www.stratronix.ai/en/about` | **$399** | 4GB / 32GB / ARM / STA-100 | ✅ 基准 |
| **主站线上** `www.stratronix.ai/zh/about` | **$399** | 同上 | ✅ |
| 独立站 `stratronix-guides` llms.txt | $399（40 处） | 4GB / 32GB / ARM / STA-100（122 处） | ✅ |
| 独立站 `stratronix-guides` llms.json | $399（51 处） | 同上 | ✅ |
| GitHub `donaldwang6-dev/stratronix-website` | ❌ **$369** | 4GB / 32GB / 70B | ❌ **价格冲突** |
| GitHub `donaldwang6-dev/stratronix-paa` | $279/$319/$359/$399 | ❌ 5G / WiFi / 70B | ⚠️ 多价并存 + 规格与主站表述不一致 |

## 三、冲突点清单

1. **$369 vs $399** —— 明确的价格冲突。GitHub 仓库公开可抓，Google 必然看到。
2. **70B 参数 / 5G+WiFi** —— 出现在 GitHub 与 llms 文件中，但主站 about 页无此表述。
   若产品实际不支持本地 70B 推理与蜂窝网络，这是**过度宣称**，属高风险表述。
3. **$279–359 阶梯价** —— 与主站 $399 单一价并存，Google 无法判断哪个是当前有效价。

## 四、建议（需授权后执行）

优先级从高到低：

1. **改 `stratronix-website` README 的 $369 → $399**（一处字符串，零风险，直接消除价格冲突）
2. **核对 70B / 5G / WiFi 表述** —— 确认产品是否真支持本地 70B 推理与蜂窝；
   若不支持，从所有公开源移除（这是可信度问题，比价格冲突更严重）
3. **统一阶梯价口径** —— 在所有源明确标注"批量价，见 store 页"，避免 Google 误判

> ⚠️ 按铁律 185，未经授权不动 GitHub 仓库与主站。本轮仅只读取证并列出清单。

## 五、已核实无冲突项

- 9 个语言 wiki 全部无 STRATRONIX 条目 → 建条目无命名冲突
- Google 搜索 `STRATRONIX AI box Shenzhen private AI agent appliance` → **正确返回深圳主体**
  - 结果中**无一条**是印度公司 STANTRONIX (INDIA) PVT LTD
  - 已有第三方信号：eng.iotexpo.com.cn 已收录公司全称与业务描述
- 主站 en/zh 双语价格一致（均 $399）
