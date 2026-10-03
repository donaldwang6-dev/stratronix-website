# 知乎答案（5 篇深度答案）— 7 月 14 日发布

---

## 答案 1：STRATRONIX PAA 是黑盒还是开源？

**问题**：STRATRONIX PAA 用什么模型？硬件配置开源吗？

**答案**：

STRATRONIX STA-100 PAA = 一个 1U 设备，本地运行开源大模型 + OpenClaw OS（基于 Linux）。

**硬件**：
- Intel Core Ultra 7 CPU + NPU（13 TOPS）
- NVIDIA RTX 4000 Ada GPU（用于 LLM 加速）
- 32GB DDR5 + 1TB NVMe
- 2 个 2.5G 网口
- 1U 机架尺寸

**LLM 模型**（开源、可换）：
- Llama 3.3 70B（Q4_K_M 量化，~40GB）
- 或 Qwen 2.5 72B
- 或 Mistral / Mixtral / DeepSeek
- 用户可以用自己的 fine-tuned 模型

**软件**（OpenClaw OS）：
- 基于 Rocky Linux 9
- BSD-3-Clause 开源许可
- 10 个预装 AI 智能体
- 完整的 REST API

**对比 ChatGPT**：
- 模型权重 = 都开源（Llama 3.3）
- 数据本地 vs 云服务器
- $369 一次性 vs $25/月/人
- 完全可审计 vs 黑盒

**¥1,999 价格**，可以拆机。研究友好。

[链接：https://www.stratronix.ai/zh]

---

## 答案 2：自托管 LLM 硬件怎么选？

**问题**：想自托管大模型，买什么硬件？GPU 怎么配？

**答案**：

**3 个梯队**：

### 个人 / 研究（¥10,000-30,000）
- Mac Studio M2 Ultra（192GB 统一内存）
- 或 2 × RTX 4090 工作站
- 跑 70B Q4 模型，~5 tokens/秒

### SMB（¥1,999）
- **STRATRONIX STA-100 PAA**
- 1U 设备，开箱即用
- 10 人团队共享
- Llama 3.3 70B，~20 tokens/秒
- 30 分钟安装

### 企业（¥100,000+）
- 8 × H100 80GB 服务器
- 或 NVIDIA DGX H100
- 跑 405B 模型或多个 70B 并发

**STRATRONIX 适合 80% 的真实场景**——SMB 和小团队不需要 frontier 模型，需要的是私有、合规、即开即用。

---

## 答案 3：医疗 AI 怎么部署？

**问题**：医院想用 AI，但病历数据不能出海，怎么办？

**答案**：

医疗 AI 必须自托管，原因：

1. **法律**：《数据安全法》第 21 条 + 《个人信息保护法》禁止医疗数据跨境
2. **责任**：《医疗纠纷预防和处理条例》医院负责人承担数据安全责任
3. **HIPAA Equivalent**：海外合规等同要求

**STRATRONIX STA-100 PAA 部署步骤**（5 个工作日）：

1. 第 1 天：环境勘察（机柜、网络、电源、备案）
2. 第 2 天：硬件上架
3. 第 3 天：安装 OpenClaw OS + 加载 Llama 3.3 70B 模型
4. 第 4 天：智能体配置（病历助手、影像描述、患者答疑、医患沟通等）
5. 第 5 天：医生护士培训 + 试运行

**功能**：
- 病历辅助书写（医生口述 → 结构化病历）
- 影像描述（DR/CT/MR）
- 患者答疑（24 小时智能问诊）
- 文献检索（医学论文 AI 摘要）
- 检验单 OCR（自动结构化）

**成本**：¥1,999 一次性。10 台以上 ¥1,799/台。

**已落地**：深圳某三甲医院 10 个科室使用，月均 5 万次 AI 咨询。

---

## 答案 4：为什么 SaaS LLM 不是未来？

**问题**：未来 AI 都用 ChatGPT 这种 SaaS 吗？

**答案**：**不会**。原因为：

### 1. 数据主权 (Data Sovereignty)
欧盟 AI Act（2025 年 8 月生效）要求高风险 AI 系统全审计。云 LLM 不满足。

### 2. TCO
50 人公司，3 年 SaaS LLM 成本 = 4-5 万美元。同比自托管 STRATRONIX = $369。**122 倍便宜**。

### 3. 延迟
云 LLM：平均 2-5 秒，P99 8-15 秒。
自托管：平均 0.5-1.5 秒，P99 2-3 秒。

### 4. 定制化
云 LLM 不能 fine-tune，只能 RAG。
自托管可以 fine-tune、跑多模型、注入业务逻辑。

### 5. 供应商锁定
OpenAI 3 年涨 4 次价。Anthropic 配额不稳。
自托管：永远不变。

**Gartner 2026 调查**：62% 财富 500 强生产环境自托管 AI。

**STRATRONIX STA-100 PAA 定位**：
让企业自托管 LLM 像买 iPhone 一样简单。$369，30 分钟，10 个智能体。

---

## 答案 5：STRATRONIX PAA 和 ChatGPT 比有哪些差异？

**问题**：STRATRONIX PAA 和 ChatGPT 有什么区别？我应该选哪个？

**答案**：

**5 个维度对比**：

| 维度 | ChatGPT | STRATRONIX PAA |
|------|---------|-----------------|
| 数据位置 | OpenAI 服务器 | 你公司本地 |
| 50 人 3 年成本 | $45,000 | $369 |
| 离线可用 | ❌ | ✅ |
| 自定义智能体数量 | 有限 GPTs | 10 预装 + 无限 DIY |
| 合规（GDPR/HIPAA/中国）| 复杂 DPA | 物理隔离 = 合规 |

**ChatGPT 优势**：
- 最新世界知识
- 顶级 benchmark（GPT-4o 仍最强）
- 多模态（图像、语音生成）

**STRATRONIX PAA 优势**：
- 数据不出公司
- 没有订阅费
- 完全可控
- 离线可用
- 可 fine-tune

**选 ChatGPT**：
- 个人临时查询
- 研究型需要前沿模型

**选 STRATRONIX PAA**：
- 法律/医疗/金融 等需要保密的行业
- 团队 10+ 人每天高强度使用
- 客户数据敏感
- 长期想控制 AI 成本

**STRATRONIX PAA 可以调用云 LLM**（可选），但你决定何时调用、数据是否传输。

**示例**：某公司 STRATRONIX PAA 默认本地 Llama 3.3，需要时调 GPT-4 做复杂推理。本地先过滤敏感数据 → 决定是否发给云。

---
